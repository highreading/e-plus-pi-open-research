#!/usr/bin/env python3
"""Exact finite certificate for Gaussian phase mixing of parity blocks.

The certificate works in the full endpoint space E = Q[z]_{<=D}.  It
reconstructs the corrected exterior coefficient map from the frozen
nondecomposable-exterior package, splits it into its even- and odd-output
blocks, kills every coefficient above a target degree d in each block by
a saturated integer kernel, and audits the resulting joint low-image
lattice.

All ranks, HNF/LLL transformations, Smith factors, contents, coefficient
vectors, and phase identities are exact.  Decimal values at pi are
diagnostics only.  No finite pattern is extrapolated.
"""

from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import math
import resource
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp
from flint import __version__ as flint_version
from flint import fmpz_mat


ROOT = Path(__file__).resolve().parents[1]
BASE_SCRIPT = ROOT / "scripts" / "root_unity_nondecomposable_exterior_sum_certificate.py"
BASE_SCRIPT_SHA256 = "3056828b21e08759fd7520c169db074aa9250c4e8bf4c8b6357c460881c3dd5f"
OUT = ROOT / "results" / "root_unity_gaussian_parity_mixing_certificate.json"
RSS_LIMIT_KIB = 2 * 1024 * 1024


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


assert sha256_file(BASE_SCRIPT) == BASE_SCRIPT_SHA256
spec = importlib.util.spec_from_file_location("nondecomposable_base", BASE_SCRIPT)
assert spec is not None and spec.loader is not None
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def nonzero_rows(matrix: sp.Matrix) -> sp.Matrix:
    rows = [
        i
        for i in range(matrix.rows)
        if any(matrix[i, j] != 0 for j in range(matrix.cols))
    ]
    if not rows:
        return sp.zeros(0, matrix.cols)
    return matrix.extract(rows, range(matrix.cols))


def exact_rank(matrix: sp.Matrix) -> int:
    if matrix.rows == 0 or matrix.cols == 0:
        return 0
    return base.exact_rank(matrix)


def saturated_kernel_allow_zero(matrix: sp.Matrix) -> tuple[sp.Matrix, dict]:
    """Saturated integer kernel, including the zero-kernel case."""
    rank = exact_rank(matrix)
    if rank == matrix.cols:
        basis = sp.zeros(matrix.cols, 0)
        return basis, {
            "kernel_dimension": 0,
            "zero_kernel_verified_by_full_column_rank": True,
            "saturated": True,
        }
    basis, audit = base.saturated_integer_kernel(matrix)
    assert matrix * basis == sp.zeros(matrix.rows, basis.cols)
    assert basis.cols == matrix.cols - rank
    audit["zero_kernel_verified_by_full_column_rank"] = False
    audit["saturated"] = True
    return basis, audit


def matrix_digest(matrix: sp.Matrix) -> str:
    digest = hashlib.sha256()
    digest.update(f"{matrix.rows},{matrix.cols}\n".encode())
    for value in matrix:
        digest.update(f"{int(value)}\n".encode())
    return digest.hexdigest()


def row_lattice_audit(image: sp.Matrix) -> dict:
    """Audit the column-image lattice image * Z^k in Z^rows."""
    rank = exact_rank(image)
    if rank == 0:
        return {
            "rank": 0,
            "smith_invariant_factors": [],
            "index_in_saturation": "1",
            "reduced_basis_rows": [],
            "reduced_basis_height": "0",
            "reduced_basis_digest_sha256": matrix_digest(sp.zeros(0, image.rows)),
            "hnf_and_lll_unimodular_transforms_verified": True,
        }

    row_generators = base.to_flint(image.transpose())
    hermite, hnf_transform = row_generators.hnf(transform=True)
    assert hermite == hnf_transform * row_generators
    assert abs(int(hnf_transform.det())) == 1
    nonzero = [
        i
        for i in range(hermite.nrows())
        if any(hermite[i, j] != 0 for j in range(hermite.ncols()))
    ]
    hnf_basis = fmpz_mat(
        [[hermite[i, j] for j in range(hermite.ncols())] for i in nonzero]
    )
    assert hnf_basis.nrows() == rank
    reduced, lll_transform = hnf_basis.lll(transform=True)
    assert reduced == lll_transform * hnf_basis
    assert abs(int(lll_transform.det())) == 1
    reduced_sympy = base.from_flint(reduced)
    assert exact_rank(reduced_sympy) == rank

    smith = base.to_flint(image).snf()
    invariant_factors = [
        abs(int(smith[i, i]))
        for i in range(min(smith.nrows(), smith.ncols()))
        if smith[i, i] != 0
    ]
    assert len(invariant_factors) == rank
    assert all(
        invariant_factors[i + 1] % invariant_factors[i] == 0
        for i in range(len(invariant_factors) - 1)
    )
    saturation_index = math.prod(invariant_factors)
    reduced_rows = [
        [str(int(reduced[i, j])) for j in range(reduced.ncols())]
        for i in range(reduced.nrows())
    ]
    height = max(abs(int(value)) for value in reduced_sympy)
    return {
        "rank": rank,
        "smith_invariant_factors": [str(value) for value in invariant_factors],
        "smith_invariant_factor_decimal_digits": [
            len(str(value)) for value in invariant_factors
        ],
        "index_in_saturation": str(saturation_index),
        "index_in_saturation_decimal_digits": len(str(saturation_index)),
        "reduced_basis_rows": reduced_rows,
        "reduced_basis_height": str(height),
        "reduced_basis_height_decimal_digits": len(str(height)),
        "reduced_basis_digest_sha256": matrix_digest(reduced_sympy),
        "hnf_and_lll_unimodular_transforms_verified": True,
    }


def primitive(values: list[int]) -> tuple[list[int], int]:
    content = math.gcd(*(abs(value) for value in values))
    assert content > 0
    result = [value // content for value in values]
    first = next(value for value in result if value)
    if first < 0:
        result = [-value for value in result]
    assert math.gcd(*(abs(value) for value in result)) == 1
    return result, content


def select_joint_candidate(reduced_basis_rows: list[list[str]]) -> dict | None:
    """Select a convenient full-support primitive image from a tiny box.

    This is a deterministic bounded search in a reduced basis, not an SVP
    certificate.  The returned raw vector lies in the actual image lattice;
    dividing by its content is the intrinsic endpoint normalization.
    """
    if not reduced_basis_rows:
        return None
    rows = [[int(value) for value in row] for row in reduced_basis_rows]
    dimension = len(rows)
    assert dimension <= 4
    best = None
    tested = 0
    for coefficients in itertools.product((-1, 0, 1), repeat=dimension):
        if not any(coefficients):
            continue
        raw = [
            sum(coefficients[i] * rows[i][j] for i in range(dimension))
            for j in range(len(rows[0]))
        ]
        if not any(raw):
            continue
        tested += 1
        normalized, content = primitive(raw)
        even_nonzero = any(normalized[0::2])
        odd_nonzero = any(normalized[1::2])
        support = sum(value != 0 for value in normalized)
        height = max(abs(value) for value in normalized)
        norm_squared = sum(value * value for value in normalized)
        key = (
            -support,
            not (even_nonzero and odd_nonzero),
            height,
            norm_squared,
            tuple(normalized),
            coefficients,
        )
        if best is None or key < best[0]:
            best = (key, raw, normalized, content, coefficients)
    assert best is not None
    _, raw, normalized, content, coefficients = best

    # If C(z) has coefficient c_j for even j and -i c_j for odd j,
    # then C(z)=A(-iz), where a_j=(-1)^floor(j/2)c_j.
    integer_pi_coefficients = [
        (-1) ** (j // 2) * value for j, value in enumerate(normalized)
    ]
    y = sp.symbols("y", real=True)
    gaussian_value = sum(
        (value if j % 2 == 0 else -sp.I * value) * (sp.I * y) ** j
        for j, value in enumerate(normalized)
    )
    integer_value = sum(
        value * y**j for j, value in enumerate(integer_pi_coefficients)
    )
    assert sp.expand(gaussian_value - integer_value) == 0
    assert max(abs(value) for value in integer_pi_coefficients) == max(
        abs(value) for value in normalized
    )

    mp.mp.dps = 100
    endpoint_value = mp.fsum(
        mp.mpf(value) * mp.pi**j
        for j, value in enumerate(integer_pi_coefficients)
    )
    endpoint_height = max(abs(value) for value in integer_pi_coefficients)
    relative_exponent = None
    if endpoint_height > 1 and endpoint_value != 0:
        relative_exponent = -mp.log(abs(endpoint_value) / endpoint_height) / mp.log(
            endpoint_height
        )
    return {
        "bounded_search_box": [-1, 0, 1],
        "bounded_search_vectors_tested": tested,
        "selected_reduced_basis_coefficients": list(coefficients),
        "selected_raw_image_coefficients_ascending": [str(value) for value in raw],
        "selected_raw_content": str(content),
        "selected_raw_content_decimal_digits": len(str(content)),
        "primitive_unphased_coefficients_ascending": [
            str(value) for value in normalized
        ],
        "primitive_integer_pi_polynomial_coefficients_ascending": [
            str(value) for value in integer_pi_coefficients
        ],
        "primitive_gaussian_coefficient_pairs_real_imag_ascending": [
            [str(value), "0"] if j % 2 == 0 else ["0", str(-value)]
            for j, value in enumerate(normalized)
        ],
        "primitive_gaussian_content_is_one": True,
        "ordinary_integer_content_is_one": True,
        "phase_identity_C_of_i_y_equals_A_of_y_verified_symbolically": True,
        "endpoint_height": str(endpoint_height),
        "endpoint_height_decimal_digits": len(str(endpoint_height)),
        "gaussian_house_equals_integer_height": True,
        "support_size": sum(value != 0 for value in normalized),
        "uses_both_parities": any(normalized[0::2]) and any(normalized[1::2]),
        "absolute_value_at_pi": mp.nstr(abs(endpoint_value), 50),
        "relative_value_over_height": mp.nstr(
            abs(endpoint_value) / endpoint_height, 50
        ),
        "relative_small_value_exponent": (
            None
            if relative_exponent is None
            else mp.nstr(relative_exponent, 40)
        ),
        "decimal_values_are_diagnostic_only": True,
        "bounded_search_is_not_a_shortest_vector_certificate": True,
    }


def block_audit(
    corrected_map: sp.Matrix,
    pairs: list[tuple[int, int]],
    target_degree: int,
    output_parity: int,
) -> tuple[sp.Matrix, dict]:
    columns = [
        column
        for column, (u, v) in enumerate(pairs)
        if (u + v - 1) % 2 == output_parity
    ]
    block = corrected_map[:, columns]
    wrong_rows = [
        row
        for row in range(corrected_map.rows)
        if row % 2 != output_parity
    ]
    assert all(block[row, column] == 0 for row in wrong_rows for column in range(block.cols))
    tail = nonzero_rows(block[target_degree + 1 :, :])
    primitive_tail = base.primitive_integer_rows(tail)
    kernel, kernel_audit = saturated_kernel_allow_zero(primitive_tail)
    low_image = block[: target_degree + 1, :] * kernel
    assert block[target_degree + 1 :, :] * kernel == sp.zeros(
        block.rows - target_degree - 1, kernel.cols
    )
    assert all(
        low_image[row, column] == 0
        for row in range(low_image.rows)
        if row % 2 != output_parity
        for column in range(low_image.cols)
    )
    rank = exact_rank(low_image)
    return low_image, {
        "output_parity": "even" if output_parity == 0 else "odd",
        "ambient_exterior_column_count": len(columns),
        "nonzero_tail_row_count": tail.rows,
        "tail_rank": exact_rank(primitive_tail),
        "saturated_tail_kernel_dimension": kernel.cols,
        "low_image_rank": rank,
        "wrong_parity_entries_exactly_zero": True,
        "tail_kernel_audit": kernel_audit,
        "low_image_digest_sha256": matrix_digest(low_image),
    }


def grid_row(m: int, n: int, target_degree: int) -> dict:
    D = n
    M = m * (n + 1)
    moments = base.logistic_moments(M + n + 8)
    _, beta, _ = base.interpolation_data(m, n, D, moments)
    Q = base.universal_Q(m, n)
    corrected = base.corrected_Q_map(beta, Q, n, D)
    pairs = list(itertools.combinations(range(D + 1), 2))

    # The parity splitting is asserted entry by entry before any rank work.
    assert all(
        corrected[row, column] == 0
        for column, (u, v) in enumerate(pairs)
        for row in range(corrected.rows)
        if row % 2 != (u + v - 1) % 2
    )
    even_image, even_audit = block_audit(corrected, pairs, target_degree, 0)
    odd_image, odd_audit = block_audit(corrected, pairs, target_degree, 1)
    joint_image = even_image.row_join(odd_image)
    joint_rank = exact_rank(joint_image)
    assert joint_rank == even_audit["low_image_rank"] + odd_audit["low_image_rank"]
    lattice = row_lattice_audit(joint_image)
    assert lattice["rank"] == joint_rank
    candidate = select_joint_candidate(lattice["reduced_basis_rows"])
    if candidate is not None:
        assert candidate["support_size"] <= target_degree + 1
        if joint_rank == target_degree + 1:
            assert candidate["support_size"] == target_degree + 1
            assert candidate["uses_both_parities"]

    return {
        "m": m,
        "n": n,
        "D": D,
        "nu_full_endpoint_dimension": D + 1,
        "M": M,
        "target_degree": target_degree,
        "exterior_dimension": len(pairs),
        "corrected_output_degree_bound": n + D,
        "universal_Q_decimal_digits": len(str(Q)),
        "all_off_parity_entries_exactly_zero": True,
        "even_block": even_audit,
        "odd_block": odd_audit,
        "joint_low_image_rank": joint_rank,
        "joint_rank_is_sum_of_parity_ranks": True,
        "joint_low_image_has_full_rational_span": joint_rank == target_degree + 1,
        "joint_low_image_lattice": lattice,
        "selected_joint_candidate": candidate,
        "row_digest_sha256": hashlib.sha256(
            (
                f"{m},{n},{D},{target_degree}\n"
                + matrix_digest(corrected)
                + matrix_digest(joint_image)
                + lattice["reduced_basis_digest_sha256"]
            ).encode()
        ).hexdigest(),
    }


def main() -> None:
    start = time.perf_counter()
    rows: list[dict] = []
    for target_degree, n_values in ((2, range(2, 9)), (3, range(3, 9))):
        for m in (2, 3):
            for n in n_values:
                rows.append(grid_row(m, n, target_degree))

    full_rows = [
        row
        for row in rows
        if row["joint_low_image_has_full_rational_span"]
    ]
    assert all(row["n"] >= 4 for row in full_rows)
    assert all(
        row["joint_low_image_has_full_rational_span"] == (row["n"] >= 4)
        for row in rows
    )
    assert all(
        row["selected_joint_candidate"]["support_size"]
        == row["target_degree"] + 1
        for row in full_rows
    )
    assert all(
        row["selected_joint_candidate"]["uses_both_parities"]
        for row in full_rows
    )
    rank_table = {
        f"d={target_degree},m={m}": [
            row["joint_low_image_rank"]
            for row in rows
            if row["target_degree"] == target_degree and row["m"] == m
        ]
        for target_degree in (2, 3)
        for m in (2, 3)
    }
    assert rank_table["d=2,m=2"] == [1, 2, 3, 3, 3, 3, 3]
    assert rank_table["d=2,m=3"] == [1, 2, 3, 3, 3, 3, 3]
    assert rank_table["d=3,m=2"] == [3, 4, 4, 4, 4, 4]
    assert rank_table["d=3,m=3"] == [3, 4, 4, 4, 4, 4]

    payload = {
        "schema": "root-unity-gaussian-parity-mixing-certificate-v1",
        "dependency": {
            "path": str(BASE_SCRIPT.relative_to(ROOT)),
            "sha256": BASE_SCRIPT_SHA256,
            "hash_verified_before_import": True,
        },
        "exact_phase_normalization": {
            "definition": (
                "For an integer coefficient vector c_j, put C_j=c_j for "
                "even j and C_j=-i*c_j for odd j, and put "
                "a_j=(-1)^floor(j/2)c_j. Then C(z)=A(-iz) and C(i*y)=A(y)."
            ),
            "gaussian_content_equals_integer_content": True,
            "gaussian_house_equals_integer_height": True,
            "verified_symbolically_on_every_selected_row": True,
        },
        "grid": {
            "endpoint_space": "full monomial endpoint space E=Q[z]_{<=D}",
            "D_rule": "D=n",
            "m_values": [2, 3],
            "target_degree_2_n_values": list(range(2, 9)),
            "target_degree_3_n_values": list(range(3, 9)),
            "row_count": len(rows),
            "rank_tables_in_increasing_n": rank_table,
            "all_off_parity_entries_exactly_zero": all(
                row["all_off_parity_entries_exactly_zero"] for row in rows
            ),
            "all_joint_ranks_equal_sum_of_block_ranks": all(
                row["joint_rank_is_sum_of_parity_ranks"] for row in rows
            ),
            "full_joint_span_occurs_exactly_for_n_at_least_4_on_this_grid": True,
            "full_row_count": len(full_rows),
            "all_full_rows_have_a_bounded_search_candidate_using_every_degree_and_both_parities": True,
            "rows": rows,
            "finite_only_no_extrapolation": True,
        },
        "logical_scope": {
            "exact": (
                "Parity zeros, ranks, saturated tail kernels, HNF/LLL "
                "transformations, Smith factors, lattice indices, contents, "
                "coefficient vectors, and phase identities are exact."
            ),
            "diagnostic_only": (
                "Decimal values at pi and bounded {-1,0,1} candidate searches "
                "are diagnostics and are not shortest-vector or asymptotic proofs."
            ),
            "not_a_measure_test": (
                "This certificate audits the joint lattice only. The algebraic "
                "e-measure threshold is proved in the companion source, not "
                "numerically inferred here."
            ),
            "not_classification": (
                "The finite ranks are not extrapolated and no conclusion about "
                "e+pi is claimed."
            ),
        },
        "versions": {
            "python": sys.version,
            "sympy": sp.__version__,
            "mpmath": mp.__version__,
            "python_flint": flint_version,
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak_rss_kib < RSS_LIMIT_KIB
    print(json.dumps(rank_table, indent=2, sort_keys=True))
    print(f"rows={len(rows)} full_rows={len(full_rows)}")
    print(f"elapsed_seconds={time.perf_counter() - start:.6f}")
    print(f"observed_peak_rss_kib={peak_rss_kib}")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
