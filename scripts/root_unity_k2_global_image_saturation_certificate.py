#!/usr/bin/env python3
"""Exact lattice audit for saturated k=2 global Wronskian images.

This replay imports the already audited root-unity interpolation and
Wronskian constructors from the nondecomposable exterior-sum certificate.
For representative minimal full-endpoint grids it forms the image of the
saturated corrected-tail kernel in the complete cleared Wronskian
coefficient lattice, then computes its rational saturation, Smith index,
Gram covolumes, and LLL scales exactly.

Finite growth patterns are diagnostics only.  The companion source proves
the general HNF/saturation identities used here.
"""

from __future__ import annotations

import gc
import hashlib
import importlib.util
import itertools
import json
import math
import resource
from pathlib import Path

import mpmath as mp
import sympy as sp
from flint import fmpz_mat


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_k2_global_image_saturation_certificate.json"
DEPENDENCY = ROOT / "scripts" / "root_unity_nondecomposable_exterior_sum_certificate.py"
RSS_LIMIT_KIB = 2 * 1024 * 1024


def load_dependency():
    specification = importlib.util.spec_from_file_location(
        "root_unity_nondecomposable_dependency", DEPENDENCY
    )
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


nd = load_dependency()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matrix_digest(matrix: fmpz_mat) -> str:
    digest = hashlib.sha256()
    digest.update(f"{matrix.nrows()},{matrix.ncols()}\n".encode())
    for i in range(matrix.nrows()):
        for j in range(matrix.ncols()):
            digest.update(f"{int(matrix[i, j])}\n".encode())
    return digest.hexdigest()


def fmpz_rows(matrix: fmpz_mat, indices: list[int]) -> fmpz_mat:
    return fmpz_mat(
        [
            [matrix[i, j] for j in range(matrix.ncols())]
            for i in indices
        ]
    )


def nonzero_row_indices(matrix: fmpz_mat) -> list[int]:
    return [
        i
        for i in range(matrix.nrows())
        if any(matrix[i, j] for j in range(matrix.ncols()))
    ]


def row_content(matrix: fmpz_mat) -> int:
    return math.gcd(
        *(
            abs(int(matrix[i, j]))
            for i in range(matrix.nrows())
            for j in range(matrix.ncols())
        )
    )


def row_squared_norms(matrix: fmpz_mat) -> list[int]:
    return [
        sum(int(matrix[i, j]) ** 2 for j in range(matrix.ncols()))
        for i in range(matrix.nrows())
    ]


def row_heights(matrix: fmpz_mat) -> list[int]:
    return [
        max(abs(int(matrix[i, j])) for j in range(matrix.ncols()))
        for i in range(matrix.nrows())
    ]


def exact_log(integer: int) -> mp.mpf:
    assert integer > 0
    return mp.log(integer)


def saturation_from_row_lattice(raw_generators: sp.Matrix) -> dict:
    """Return exact bases and invariants for Sat(row_Z(raw_generators))."""
    raw_flint = nd.to_flint(raw_generators)
    raw_hnf, raw_transform = raw_flint.hnf(transform=True)
    assert raw_hnf == raw_transform * raw_flint
    assert abs(int(raw_transform.det())) == 1
    nonzero = nonzero_row_indices(raw_hnf)
    raw_basis = fmpz_rows(raw_hnf, nonzero)
    rank = raw_basis.nrows()
    ambient_dimension = raw_basis.ncols()
    assert rank == int(raw_flint.rank())
    assert rank > 0

    # Tall HNF theorem.  If H=T B^t=[H0;0], then
    # B=H0^t S with S=(T^{-1}[:,0:r])^t, and rows(S) are exactly
    # span_Q(rows(B)) cap Z^P.
    tall_hnf, ambient_transform = raw_basis.transpose().hnf(transform=True)
    assert tall_hnf == ambient_transform * raw_basis.transpose()
    assert abs(int(ambient_transform.det())) == 1
    assert all(
        tall_hnf[i, j] == 0
        for i in range(rank, ambient_dimension)
        for j in range(rank)
    )
    top_block = fmpz_mat(
        [
            [tall_hnf[i, j] for j in range(rank)]
            for i in range(rank)
        ]
    )
    index = abs(int(top_block.det()))
    assert index > 0
    inverse_transform = ambient_transform.inv(integer=True)
    saturated_basis = fmpz_mat(
        [
            [inverse_transform[j, i] for j in range(ambient_dimension)]
            for i in range(rank)
        ]
    )
    assert raw_basis == top_block.transpose() * saturated_basis

    saturated_tall_hnf = saturated_basis.transpose().hnf()
    assert all(
        saturated_tall_hnf[i, j] == int(i == j)
        for i in range(rank)
        for j in range(rank)
    )
    assert all(
        saturated_tall_hnf[i, j] == 0
        for i in range(rank, ambient_dimension)
        for j in range(rank)
    )

    smith = raw_basis.snf()
    smith_invariants = [abs(int(smith[i, i])) for i in range(rank)]
    assert all(value > 0 for value in smith_invariants)
    assert all(
        smith_invariants[i + 1] % smith_invariants[i] == 0
        for i in range(rank - 1)
    )
    assert math.prod(smith_invariants) == index
    common_content = row_content(raw_basis)
    assert common_content == smith_invariants[0]
    residual_invariants = [value // common_content for value in smith_invariants]
    residual_index = math.prod(residual_invariants)
    assert index == common_content**rank * residual_index

    raw_gram = raw_basis * raw_basis.transpose()
    saturated_gram = saturated_basis * saturated_basis.transpose()
    raw_gram_determinant = int(raw_gram.det())
    saturated_gram_determinant = int(saturated_gram.det())
    assert raw_gram_determinant > 0 and saturated_gram_determinant > 0
    assert raw_gram_determinant == index**2 * saturated_gram_determinant

    raw_lll, raw_lll_transform = raw_basis.lll(transform=True)
    saturated_lll, saturated_lll_transform = saturated_basis.lll(transform=True)
    assert raw_lll == raw_lll_transform * raw_basis
    assert saturated_lll == saturated_lll_transform * saturated_basis
    assert abs(int(raw_lll_transform.det())) == 1
    assert abs(int(saturated_lll_transform.det())) == 1
    assert all(
        math.gcd(*(abs(int(saturated_lll[i, j])) for j in range(ambient_dimension)))
        == 1
        for i in range(rank)
    )

    return {
        "rank": rank,
        "ambient_dimension": ambient_dimension,
        "raw_basis": raw_basis,
        "saturated_basis": saturated_basis,
        "raw_lll": raw_lll,
        "saturated_lll": saturated_lll,
        "top_block": top_block,
        "index": index,
        "smith_invariants": smith_invariants,
        "common_content": common_content,
        "residual_invariants": residual_invariants,
        "residual_index": residual_index,
        "raw_gram_determinant": raw_gram_determinant,
        "saturated_gram_determinant": saturated_gram_determinant,
    }


def endpoint_rows(global_rows: fmpz_mat, m: int, n: int) -> sp.Matrix:
    expected_columns = (2 * m + 1) * (2 * n + 1)
    assert global_rows.ncols() == expected_columns
    output = sp.zeros(global_rows.nrows(), 2 * n + 1)
    for i in range(global_rows.nrows()):
        for frequency in range(2 * m + 1):
            sign = (-1) ** frequency
            offset = frequency * (2 * n + 1)
            for degree in range(2 * n + 1):
                output[i, degree] += sign * int(
                    global_rows[i, offset + degree]
                )
    return output


def full_endpoint_row(m: int, n: int, target_degree: int = 2) -> dict:
    D = nd.minimal_full_endpoint_D(n, target_degree)
    nu = D + 1
    M = m * (n + 1)
    moments = nd.logistic_moments(M + n + 10)
    interpolation, beta, labels = nd.interpolation_data(
        m, n, D, moments
    )
    Q = nd.universal_Q(m, n)
    corrected_map = nd.corrected_Q_map(beta, Q, n, D)
    tail_map = corrected_map[target_degree + 1 :, :]
    primitive_tail_rows = nd.primitive_integer_rows(tail_map)
    tail_kernel, tail_kernel_audit = nd.saturated_integer_kernel(
        primitive_tail_rows
    )
    exterior_dimension = math.comb(nu, 2)
    assert tail_kernel.rows == exterior_dimension

    coordinate_pairs = list(itertools.combinations(range(nu), 2))
    remainders = nd.cleared_remainders(
        m,
        n,
        D,
        Q,
        interpolation,
        labels,
        sp.eye(nu),
    )
    global_rows = []
    for i, j in coordinate_pairs:
        pair = nd.exp_wronskian(remainders[i], remainders[j])
        global_rows.append([value for frequency in pair for value in frequency])
    global_map = sp.Matrix(global_rows)
    global_pair_content = math.gcd(*(abs(int(value)) for value in global_map))

    # Rows of B are complete global coefficient vectors corresponding to
    # the columns of the saturated integer tail kernel.
    image_generators = tail_kernel.transpose() * global_map
    lattice = saturation_from_row_lattice(image_generators)
    rank = lattice["rank"]
    assert rank == tail_kernel.cols

    endpoint_image = endpoint_rows(lattice["saturated_basis"], m, n)
    assert all(
        endpoint_image[i, degree] == 0
        for i in range(endpoint_image.rows)
        for degree in range(target_degree + 1, endpoint_image.cols)
    )
    low_endpoint_rank = int(endpoint_image[:, : target_degree + 1].rank())
    assert low_endpoint_rank == int(corrected_map.rank()) - int(tail_map.rank())

    raw_lll = lattice["raw_lll"]
    saturated_lll = lattice["saturated_lll"]
    raw_norms = row_squared_norms(raw_lll)
    saturated_norms = row_squared_norms(saturated_lll)
    raw_heights = row_heights(raw_lll)
    saturated_heights = row_heights(saturated_lll)
    tail_coordinate_norms = [
        sum(int(tail_kernel[j, i]) ** 2 for j in range(tail_kernel.rows))
        for i in range(tail_kernel.cols)
    ]
    tail_coordinate_heights = [
        max(abs(int(tail_kernel[j, i])) for j in range(tail_kernel.rows))
        for i in range(tail_kernel.cols)
    ]

    raw_gram_det = lattice["raw_gram_determinant"]
    saturated_gram_det = lattice["saturated_gram_determinant"]
    index = lattice["index"]
    common_content = lattice["common_content"]
    residual_index = lattice["residual_index"]
    mp.mp.dps = 80
    log_index = exact_log(index)
    log_common_contribution = rank * exact_log(common_content)
    log_raw_covolume = exact_log(raw_gram_det) / 2
    log_saturated_covolume = exact_log(saturated_gram_det) / 2
    log_raw_root_determinant = log_raw_covolume / rank
    log_saturated_root_determinant = log_saturated_covolume / rank
    log_raw_lll_min_norm = exact_log(min(raw_norms)) / 2
    log_saturated_lll_min_norm = exact_log(min(saturated_norms)) / 2
    log_tail_coordinate_min_norm = exact_log(min(tail_coordinate_norms)) / 2

    assert common_content % global_pair_content == 0
    tail_content_amplification = common_content // global_pair_content
    q_squared_divisible = Q**2 % common_content == 0
    q_squared_quotient = Q**2 // common_content if q_squared_divisible else None

    scale = n * mp.log(n)
    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak_rss_kib < RSS_LIMIT_KIB
    return {
        "parameters": {
            "m": m,
            "n": n,
            "D": D,
            "nu": nu,
            "target_degree": target_degree,
        },
        "exterior_dimension": exterior_dimension,
        "tail_kernel_rank": tail_kernel.cols,
        "global_coefficient_slot_count": global_map.cols,
        "global_image_rank": rank,
        "tail_kernel_is_saturated": True,
        "tail_kernel_audit": tail_kernel_audit,
        "low_endpoint_image_rank": low_endpoint_rank,
        "global_pair_map_common_content": str(global_pair_content),
        "raw_tail_image_common_content": str(common_content),
        "tail_content_amplification": str(tail_content_amplification),
        "Q_squared_divisible_by_raw_common_content": q_squared_divisible,
        "Q_squared_over_raw_common_content": (
            None if q_squared_quotient is None else str(q_squared_quotient)
        ),
        "smith_invariants": [str(value) for value in lattice["smith_invariants"]],
        "smith_invariants_after_common_content": [
            str(value) for value in lattice["residual_invariants"]
        ],
        "row_lattice_saturation_index": str(index),
        "row_lattice_saturation_index_decimal_digits": len(str(index)),
        "common_scalar_index_factor": str(common_content**rank),
        "residual_cross_index": str(residual_index),
        "common_scalar_fraction_of_log_index": mp.nstr(
            log_common_contribution / log_index, 30
        ),
        "raw_gram_determinant": str(raw_gram_det),
        "saturated_gram_determinant": str(saturated_gram_det),
        "gram_determinant_identity_verified": True,
        "log_raw_covolume": mp.nstr(log_raw_covolume, 40),
        "log_saturated_covolume": mp.nstr(log_saturated_covolume, 40),
        "log_raw_root_determinant": mp.nstr(log_raw_root_determinant, 40),
        "log_saturated_root_determinant": mp.nstr(
            log_saturated_root_determinant, 40
        ),
        "tail_kernel_LLL_min_squared_norm": str(min(tail_coordinate_norms)),
        "tail_kernel_LLL_min_height": str(min(tail_coordinate_heights)),
        "log_tail_kernel_LLL_min_norm": mp.nstr(
            log_tail_coordinate_min_norm, 40
        ),
        "raw_image_LLL_min_squared_norm": str(min(raw_norms)),
        "raw_image_LLL_min_height": str(min(raw_heights)),
        "log_raw_image_LLL_min_norm": mp.nstr(log_raw_lll_min_norm, 40),
        "saturated_image_LLL_min_squared_norm": str(min(saturated_norms)),
        "saturated_image_LLL_min_height": str(min(saturated_heights)),
        "log_saturated_image_LLL_min_norm": mp.nstr(
            log_saturated_lll_min_norm, 40
        ),
        "log_LLL_norm_reduction_from_saturation": mp.nstr(
            log_raw_lll_min_norm - log_saturated_lll_min_norm, 40
        ),
        "saturated_root_log_over_n_log_n": mp.nstr(
            log_saturated_root_determinant / scale, 30
        ),
        "saturated_LLL_log_over_n_log_n": mp.nstr(
            log_saturated_lll_min_norm / scale, 30
        ),
        "raw_basis_sha256": matrix_digest(lattice["raw_basis"]),
        "saturated_basis_sha256": matrix_digest(lattice["saturated_basis"]),
        "raw_LLL_basis_sha256": matrix_digest(raw_lll),
        "saturated_LLL_basis_sha256": matrix_digest(saturated_lll),
        "exact_HNF_factorization_verified": True,
        "saturated_tall_HNF_is_identity_block": True,
        "saturated_basis_rows_are_primitive": True,
        "peak_RSS_checked_below_2GiB_after_row": True,
    }


def main() -> None:
    # Largest rows first avoids mistaking retained allocator memory for a
    # new parameter-driven spike during adaptive monitoring.
    parameters = [
        (3, 10),
        (2, 10),
        (3, 8),
        (2, 8),
        (3, 5),
        (2, 5),
        (3, 3),
        (2, 3),
        (3, 2),
        (2, 2),
    ]
    rows = []
    for m, n in parameters:
        rows.append(full_endpoint_row(m, n))
        gc.collect()
        assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < RSS_LIMIT_KIB
    rows.sort(key=lambda row: (row["parameters"]["m"], row["parameters"]["n"]))

    minimum_common_fraction = min(
        mp.mpf(row["common_scalar_fraction_of_log_index"])
        for row in rows
    )
    payload = {
        "schema": "root-unity-k2-global-image-saturation-v1",
        "dependency": {
            "path": str(DEPENDENCY.relative_to(ROOT)),
            "sha256": sha256_file(DEPENDENCY),
        },
        "representative_minimal_full_endpoint_grid": rows,
        "grid_summary": {
            "row_count": len(rows),
            "all_tail_kernels_saturated": True,
            "all_global_image_ranks_equal_tail_kernel_ranks": all(
                row["global_image_rank"] == row["tail_kernel_rank"]
                for row in rows
            ),
            "all_Q_squared_divisibilities_hold_on_grid": all(
                row["Q_squared_divisible_by_raw_common_content"]
                for row in rows
            ),
            "minimum_common_scalar_fraction_of_log_index": mp.nstr(
                minimum_common_fraction, 30
            ),
            "finite_growth_patterns_are_not_extrapolated": True,
        },
        "all_parameter_lattice_theorems_proved_in_source": {
            "tall_HNF_saturation_formula": True,
            "index_equals_top_block_determinant": True,
            "index_equals_product_of_nonzero_Smith_invariants": True,
            "index_equals_gcd_of_maximal_minors": True,
            "Gram_covolume_ratio_equals_index": True,
            "common_content_factorization_index_equals_g_to_rank_times_residual": True,
            "saturated_image_independent_of_tail_basis_size": True,
            "saturated_image_invariant_under_nonzero_global_scalar": True,
        },
        "limitations": {
            "no_uniform_parameter_formula_for_Smith_invariants": True,
            "no_proved_O_n_log_n_bound_for_saturated_successive_minima": True,
            "LLL_vectors_are_upper_bounds_not_shortest_vector_certificates": True,
            "short_global_vectors_do_not_prove_nonzero_primitive_endpoint_values": True,
            "no_irrationality_or_transcendence_conclusion": True,
        },
        "peak_RSS_omitted_for_determinism_but_asserted_below_2GiB": True,
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(
        json.dumps(
            {
                "output": str(OUT),
                "rows": len(rows),
                "all_assertions_passed": True,
                "peak_rss_mib": round(peak_rss_kib / 1024, 6),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
