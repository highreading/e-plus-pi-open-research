#!/usr/bin/env python3
"""Independent exact audit of the nonpolynomial integral-Hurwitz pullback.

The source certificate uses hand-written Gaussian-integer pairs.  This audit
reconstructs the truncation with SymPy polynomials and performs the
fraction-free Cohn recursion in SymPy's ZZ_I domain.  It also constructs a
second, finer 160-bit reflection-product bound, independently checks the
exponential tail and Rouche inequality, and verifies integral jets.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from functools import reduce
from math import factorial, gcd, isqrt, lcm
from pathlib import Path

import mpmath as mp
import sympy as sp
from sympy import ZZ, ZZ_I


sys.set_int_max_str_digits(0)

BASE = Path("/content/drive/MyDrive/e_pi_research_20260826")
SOURCE_NOTE = BASE / "sources/nonpolynomial_integral_hurwitz_pullback.md"
CERT_SCRIPT = BASE / "scripts/nonpolynomial_integral_hurwitz_pullback_certificate.py"
CERT_RESULT = BASE / "results/nonpolynomial_integral_hurwitz_pullback_certificate.json"
HP_NOTE = BASE / "sources/nonpolynomial_integral_hurwitz_hp_diagnostic.md"
HP_SCRIPT = BASE / "scripts/nonpolynomial_integral_hurwitz_hp_probe.py"
HP_RESULT = BASE / "results/nonpolynomial_integral_hurwitz_hp_n15.json"

EXPECTED_FIXED_HASHES = {
    str(SOURCE_NOTE): "7c194175b3a5501740d0b0d46bd720dc4396ebb46e35210aa879c3a7c5f405af",
    str(CERT_SCRIPT): "2e4ad9a01716d1e808b60ae04f5137d9d6020d46f52d22853c2415c105c41efd",
    str(CERT_RESULT): "9d24c15e4f69fc5e8e1618f812e95ffa9d0351b401951795a023c4eaff9afb15",
    str(HP_NOTE): "aa93d76dea21a3d7ab24bd40362d6948c8586df11fc7e7138866247e6b79f78b",
    str(HP_SCRIPT): "27574fa09fc8a63231347776fa06f6a17b6fa8aafebec48224d5619ad29066b9",
    str(HP_RESULT): "ab01f6a7a731066f860c6f2f91423f30940b5cf9ecccb785c703fdfa867206fc",
}

BASE_TERMS = (
    (7, 46),
    (9, 213),
    (10, -762),
    (11, 20073),
)
EXPONENTIAL_TERMS = (
    (15, -1, 1215540),
    (26, -1, 65574371633155024),
    (40, 1, 40126919362525583214229456433446912),
)
RADIUS = Fraction(707, 400)
TRUNCATION = 20
ARCHIVED_BITS = 128
INDEPENDENT_BITS = 160


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def integer_sha256(value: int) -> str:
    return sha256_bytes(str(value).encode())


def vector_sha256(values: list[int]) -> str:
    return sha256_bytes(json.dumps(values, separators=(",", ":")).encode())


def fraction_record(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def fraction_from_record(record: dict) -> Fraction:
    return Fraction(record["numerator"], record["denominator"])


def gaussian_state_sha256(values) -> str:
    digest = hashlib.sha256()
    for value in values:
        for coordinate in (int(value.x), int(value.y)):
            sign = b"-" if coordinate < 0 else b"+"
            magnitude = abs(coordinate)
            length = max(1, (magnitude.bit_length() + 7) // 8)
            digest.update(sign)
            digest.update(length.to_bytes(8, "big"))
            digest.update(magnitude.to_bytes(length, "big"))
    return digest.hexdigest()


def zzi(real: int, imag: int = 0):
    return ZZ_I.dtype(ZZ(real), ZZ(imag))


def conjugate(value):
    return ZZ_I.dtype(value.x, -value.y)


def norm(value) -> int:
    return int(value.x * value.x + value.y * value.y)


def primitive_state(values) -> tuple[list, int]:
    content = 0
    for value in values:
        content = gcd(content, abs(int(value.x)))
        content = gcd(content, abs(int(value.y)))
    assert content > 0
    if content > 1:
        values = [
            zzi(int(value.x) // content, int(value.y) // content)
            for value in values
        ]
    return values, content


def exact_truncation() -> tuple[list[Fraction], list[Fraction]]:
    """Construct q_20 with SymPy polynomial expansion, independently."""
    z = sp.symbols("z")
    phi = z
    for m, coefficient in BASE_TERMS:
        phi += sp.Rational(coefficient, factorial(m)) * z**m * (1 - z)
    for m, a, k in EXPONENTIAL_TERMS:
        exponential = sum(
            sp.Rational(a**n, factorial(n)) * z**n
            for n in range(TRUNCATION + 1)
        )
        phi += sp.Rational(k, factorial(m)) * z**m * (z - 1) * exponential
    polynomial = sp.Poly(sp.expand(phi - (1 + sp.I)), z, extension=sp.I)
    degree = polynomial.degree()
    assert degree == 61
    real: list[Fraction] = []
    imag: list[Fraction] = []
    for j in range(degree + 1):
        x, y = sp.expand(polynomial.nth(j)).as_real_imag()
        assert x.is_Rational and y.is_Rational
        real.append(Fraction(int(x.p), int(x.q)))
        imag.append(Fraction(int(y.p), int(y.q)))
    return real, imag


def initial_reversed_state(
    real: list[Fraction], imag: list[Fraction]
) -> tuple[list, int, int]:
    scaled = [
        (real[j] * RADIUS**j, imag[j] * RADIUS**j)
        for j in range(len(real))
    ]
    denominator = 1
    for x, y in scaled:
        denominator = lcm(denominator, x.denominator, y.denominator)
    state = [
        zzi(int(x * denominator), int(y * denominator))
        for x, y in scaled
    ]
    primitive, content = primitive_state(state)
    return primitive, denominator, content


def ceil_sqrt_ratio(numerator: int, denominator: int, bits: int) -> int:
    assert 0 <= numerator < denominator
    scale = 1 << bits
    target = numerator * scale * scale
    candidate = isqrt(target // denominator)
    if candidate * candidate * denominator < target:
        candidate += 1
    assert (candidate - 1) ** 2 * denominator < target <= (
        candidate**2 * denominator
    )
    assert candidate < scale
    return candidate


def fraction_free_schur(initial: list, archived_records: list[dict]) -> dict:
    state = initial
    archived_product_numerator = 1
    independent_product_numerator = 1
    archived_scale = 1 << ARCHIVED_BITS
    independent_scale = 1 << INDEPENDENT_BITS
    comparisons: list[dict] = []
    independent_factors: list[int] = []

    for expected in archived_records:
        degree = len(state) - 1
        assert degree == expected["degree"]
        leading = state[0]
        constant = state[-1]
        leading_norm = norm(leading)
        constant_norm = norm(constant)
        gap = leading_norm - constant_norm
        assert gap > 0

        archived_upper = ceil_sqrt_ratio(
            constant_norm, leading_norm, ARCHIVED_BITS
        )
        archived_factor = archived_scale - archived_upper
        archived_product_numerator *= archived_factor

        independent_upper = ceil_sqrt_ratio(
            constant_norm, leading_norm, INDEPENDENT_BITS
        )
        independent_factor = independent_scale - independent_upper
        independent_product_numerator *= independent_factor
        independent_factors.append(independent_factor)

        transformed = [
            conjugate(leading) * state[j]
            - constant * conjugate(state[-1 - j])
            for j in range(len(state))
        ]
        assert transformed[-1] == ZZ_I.zero
        transformed, content = primitive_state(transformed[:-1])

        comparison = {
            "degree": degree == expected["degree"],
            "state_sha256": gaussian_state_sha256(state)
            == expected["state_sha256"],
            "leading_norm_bit_length": leading_norm.bit_length()
            == expected["leading_norm_bit_length"],
            "constant_norm_bit_length": constant_norm.bit_length()
            == expected["constant_norm_bit_length"],
            "gap_bit_length": gap.bit_length() == expected["gap_bit_length"],
            "gap_sha256": integer_sha256(gap) == expected["gap_sha256"],
            "dyadic_upper": archived_upper
            == expected["dyadic_modulus_upper_scaled"],
            "dyadic_factor": archived_factor
            == expected["dyadic_factor_numerator"],
            "removed_content_bit_length": content.bit_length()
            == expected["removed_integer_content_bit_length"],
            "next_state_sha256": gaussian_state_sha256(transformed)
            == expected["next_state_sha256"],
        }
        assert all(comparison.values())
        comparisons.append(comparison)
        state = transformed

    assert len(state) == 1 and state[0] == ZZ_I.one
    archived_product = Fraction(
        archived_product_numerator,
        archived_scale ** len(archived_records),
    )
    independent_product = Fraction(
        independent_product_numerator,
        independent_scale ** len(archived_records),
    )
    return {
        "all_stage_comparisons_pass": all(
            all(item.values()) for item in comparisons
        ),
        "comparisons": comparisons,
        "archived_128_bit_product": archived_product,
        "independent_160_bit_product": independent_product,
        "independent_160_bit_factor_sha256": vector_sha256(independent_factors),
        "final_constant": [int(state[0].x), int(state[0].y)],
    }


def exact_tail_bound() -> Fraction:
    remainder = (
        Fraction(9)
        * RADIUS ** (TRUNCATION + 1)
        / factorial(TRUNCATION + 1)
    )
    return sum(
        (
            Fraction(abs(k), factorial(m))
            * RADIUS**m
            * (1 + RADIUS)
            * remainder
            for m, _a, k in EXPONENTIAL_TERMS
        ),
        Fraction(0),
    )


def phi_jets(maximum: int) -> list[int]:
    jets = [0] * (maximum + 1)
    if maximum >= 1:
        jets[1] = 1
    for m, coefficient in BASE_TERMS:
        if m <= maximum:
            jets[m] += coefficient
        if m + 1 <= maximum:
            jets[m + 1] -= (m + 1) * coefficient
    for m, a, k in EXPONENTIAL_TERMS:
        if m <= maximum:
            jets[m] -= k
        for n in range(m + 1, maximum + 1):
            r = n - m
            jets[n] += (
                k
                * math.comb(n, m)
                * (r * a ** (r - 1) - a**r)
            )
    return jets


def convolution_truncated(
    left: list[Fraction], right: list[Fraction], maximum: int
) -> list[Fraction]:
    result = [Fraction(0)] * (maximum + 1)
    for i, x in enumerate(left):
        if not x:
            continue
        for j, y in enumerate(right):
            if i + j > maximum:
                break
            if y:
                result[i + j] += x * y
    return result


def base_F_coefficients(maximum: int) -> list[Fraction]:
    derivative: list[Fraction] = []
    for n in range(maximum):
        h1 = derivative[n - 1] if n >= 1 else Fraction(0)
        h2 = derivative[n - 2] if n >= 2 else Fraction(0)
        rhs = Fraction(4) if n == 0 else Fraction(0)
        derivative.append((rhs + 2 * h1 - h2) / 2)
    return [Fraction(0)] + [
        derivative[n] / (n + 1) for n in range(maximum)
    ]


def composed_G_jets(maximum: int, jets: list[int]) -> list[int]:
    phi = [
        Fraction(jets[k], factorial(k)) for k in range(maximum + 1)
    ]
    base = base_F_coefficients(maximum)
    result = [Fraction(0)] * (maximum + 1)
    power = [Fraction(0)] * (maximum + 1)
    power[0] = 1
    for k in range(1, maximum + 1):
        power = convolution_truncated(power, phi, maximum)
        for j, value in enumerate(power):
            result[j] += base[k] * value
    answer = []
    for k, coefficient in enumerate(result):
        value = coefficient * factorial(k)
        assert value.denominator == 1
        answer.append(value.numerator)
    return answer


def falling(k: int, j: int) -> int:
    return 0 if j > k else factorial(k) // factorial(k - j)


def primitive_rational_vector(values) -> list[int]:
    fractions = []
    for value in values:
        if isinstance(value, sp.Rational):
            fractions.append(Fraction(int(value.p), int(value.q)))
        else:
            fractions.append(Fraction(value))
    denominator = reduce(lcm, (x.denominator for x in fractions), 1)
    integers = [
        x.numerator * (denominator // x.denominator) for x in fractions
    ]
    content = reduce(gcd, (abs(x) for x in integers if x))
    integers = [x // content for x in integers]
    first = next(x for x in integers if x)
    return integers if first > 0 else [-x for x in integers]


def hp_rows(n: int, jets: list[int]) -> list[list[int]]:
    rows = []
    for k in range(n + 1, 3 * n + 1):
        row = [falling(k, j) for j in range(n + 1)]
        row.extend(
            falling(k, j) * jets[k - j] for j in range(n + 1)
        )
        rows.append(row)
    rows.append([-1] * (n + 1) + [1] * (n + 1))
    return rows


def reconstruct_hp_triple(
    n: int, kernel: list[int], jets: list[int]
) -> list[int]:
    b = kernel[: n + 1]
    c = kernel[n + 1 :]
    a: list[Fraction] = []
    for k in range(n + 1):
        derivative = sum(
            falling(k, j) * (b[j] + c[j] * jets[k - j])
            for j in range(k + 1)
        )
        a.append(Fraction(-derivative, factorial(k)))
    return primitive_rational_vector(a + b + c)


def hp_first_free(n: int, triple: list[int], jets: list[int]) -> Fraction:
    b = triple[n + 1 : 2 * (n + 1)]
    c = triple[2 * (n + 1) :]
    k = 3 * n + 1
    return sum(
        (
            Fraction(
                b[j] + c[j] * jets[k - j],
                factorial(k - j),
            )
            for j in range(n + 1)
        ),
        Fraction(0),
    )


def e_interval(last: int = 900) -> tuple[Fraction, Fraction]:
    partial = sum(
        (Fraction(1, factorial(k)) for k in range(last + 1)),
        Fraction(0),
    )
    return partial, partial + Fraction(1, last * factorial(last))


def atan_interval(inv: int, last: int) -> tuple[Fraction, Fraction]:
    partial = sum(
        (
            (-1 if k & 1 else 1)
            * Fraction(1, (2 * k + 1) * inv ** (2 * k + 1))
            for k in range(last + 1)
        ),
        Fraction(0),
    )
    omitted = Fraction(
        1, (2 * last + 3) * inv ** (2 * last + 3)
    )
    return (
        (partial, partial + omitted)
        if last & 1
        else (partial - omitted, partial)
    )


def e_plus_pi_interval() -> tuple[Fraction, Fraction]:
    elo, ehi = e_interval()
    a5lo, a5hi = atan_interval(5, 1200)
    a239lo, a239hi = atan_interval(239, 320)
    return (
        elo + 16 * a5lo - 4 * a239hi,
        ehi + 16 * a5hi - 4 * a239lo,
    )


def floor_log10(value: Fraction) -> int:
    assert value > 0
    guess = len(str(value.numerator)) - len(str(value.denominator))
    power = (
        Fraction(10**guess)
        if guess >= 0
        else Fraction(1, 10 ** (-guess))
    )
    while value < power:
        guess -= 1
        power /= 10
    while value >= 10 * power:
        guess += 1
        power *= 10
    return guess


def endpoint_summary(
    alpha: int,
    beta: int,
    interval: tuple[Fraction, Fraction],
) -> dict:
    lo, hi = sorted(
        (
            Fraction(alpha) + beta * interval[0],
            Fraction(alpha) + beta * interval[1],
        )
    )
    if lo > 0:
        abs_lo, abs_hi, sign = lo, hi, 1
    elif hi < 0:
        abs_lo, abs_hi, sign = -hi, -lo, -1
    else:
        return {"contains_zero": True, "sign": 0, "decade": None}
    decade_lo = floor_log10(abs_lo)
    decade_hi = floor_log10(abs_hi)
    assert decade_lo == decade_hi
    return {
        "contains_zero": False,
        "sign": sign,
        "decade": decade_lo,
    }


def independent_hp_audit(
    jets: list[int], archived: dict, max_n: int = 15
) -> list[dict]:
    archived_by_n = {item["n"]: item for item in archived["records"]}
    interval = e_plus_pi_interval()
    answer = []
    for n in range(1, max_n + 1):
        rows = hp_rows(n, jets)
        matrix = sp.Matrix(rows)
        nullspace = matrix.nullspace(simplify=False)
        assert len(nullspace) == 1
        kernel = primitive_rational_vector(list(nullspace[0]))

        # Deliberately use the last nonzero coordinate; the source generic
        # routine uses the first.
        index = max(j for j, value in enumerate(kernel) if value)
        minor = matrix[:, :index].row_join(matrix[:, index + 1 :])
        determinant = int(minor.det(method="bareiss"))
        signed = determinant if index % 2 == 0 else -determinant
        assert signed and signed % kernel[index] == 0
        content = abs(signed // kernel[index])

        triple = reconstruct_hp_triple(n, kernel, jets)
        a = triple[: n + 1]
        b = triple[n + 1 : 2 * (n + 1)]
        c = triple[2 * (n + 1) :]
        assert sum(b) == sum(c)
        raw = [sum(a), sum(b)]
        endpoint_gcd = gcd(abs(raw[0]), abs(raw[1]))
        reduced = (
            [raw[0] // endpoint_gcd, raw[1] // endpoint_gcd]
            if endpoint_gcd
            else [0, 0]
        )
        free = hp_first_free(n, triple, jets)
        endpoint = endpoint_summary(
            reduced[0], reduced[1], interval
        )
        record = {
            "n": n,
            "shape": [len(rows), len(rows[0])],
            "rank": len(rows),
            "nullity": 1,
            "matrix_sha256": vector_sha256(
                [entry for row in rows for entry in row]
            ),
            "primitive_high_kernel_sha256": vector_sha256(kernel),
            "cofactor_content_digits": len(str(content)),
            "primitive_triple_sha256": vector_sha256(triple),
            "primitive_triple_height_digits": len(
                str(max(map(abs, triple)))
            ),
            "raw_endpoint_pair": raw,
            "endpoint_gcd": endpoint_gcd,
            "reduced_endpoint_pair": reduced,
            "first_free": {
                "index": 3 * n + 1,
                "numerator": free.numerator,
                "denominator": free.denominator,
                "nonzero": bool(free),
            },
            "endpoint": endpoint,
        }
        expected = archived_by_n[n]
        comparisons = {
            "shape": record["shape"] == expected["shape"],
            "rank": record["rank"] == expected["rank"],
            "nullity": record["nullity"] == expected["nullity"],
            "kernel_hash": record["primitive_high_kernel_sha256"]
            == expected["primitive_high_kernel_sha256"],
            "cofactor_content_digits": record[
                "cofactor_content_digits"
            ]
            == expected["maximal_cofactor_common_content_digits"],
            "triple_hash": record["primitive_triple_sha256"]
            == expected["primitive_triple_sha256"],
            "triple_height_digits": record[
                "primitive_triple_height_digits"
            ]
            == expected["primitive_triple_height_digits"],
            "raw_endpoint_pair": raw == expected["raw_endpoint_pair"],
            "endpoint_gcd": endpoint_gcd == expected["endpoint_gcd"],
            "reduced_endpoint_pair": reduced
            == expected["reduced_endpoint_pair"],
            "first_free": record["first_free"] == expected["first_free"],
            "endpoint_sign": endpoint["sign"]
            == expected["endpoint_interval_certificate"]["certified_sign"],
            "endpoint_contains_zero": endpoint["contains_zero"]
            == expected["endpoint_interval_certificate"][
                "interval_contains_zero"
            ],
            "endpoint_decade": endpoint["decade"]
            == expected["endpoint_interval_certificate"].get(
                "single_certified_base10_decade"
            ),
        }
        assert all(comparisons.values())
        record["archive_comparisons"] = comparisons
        answer.append(record)
    return answer


def numerical_phi(z):
    value = z
    for m, coefficient in BASE_TERMS:
        value += mp.mpf(coefficient) / factorial(m) * z**m * (1 - z)
    for m, a, k in EXPONENTIAL_TERMS:
        value += (
            mp.mpf(k)
            / factorial(m)
            * z**m
            * (z - 1)
            * mp.exp(a * z)
        )
    return value


def numerical_root_crosscheck(archived_roots: list[dict]) -> list[dict]:
    mp.mp.dps = 85
    result = []
    for expected in archived_roots:
        start = mp.mpc(expected["real"], expected["imag"])
        root = mp.findroot(
            lambda z: numerical_phi(z) - (1 + 1j),
            start,
            solver="secant",
            tol=mp.mpf("1e-70"),
            maxsteps=200,
        )
        expected_modulus = mp.mpf(expected["modulus"])
        result.append(
            {
                "real": mp.nstr(root.real, 65),
                "imag": mp.nstr(root.imag, 65),
                "modulus": mp.nstr(abs(root), 65),
                "absolute_residual": mp.nstr(
                    abs(numerical_phi(root) - (1 + 1j)), 12
                ),
                "modulus_difference_from_archive": mp.nstr(
                    abs(abs(root) - expected_modulus), 12
                ),
            }
        )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    actual_hashes = {
        path: file_sha256(Path(path)) for path in EXPECTED_FIXED_HASHES
    }
    assert actual_hashes == EXPECTED_FIXED_HASHES
    archived = json.loads(CERT_RESULT.read_text())
    archived_hp = json.loads(HP_RESULT.read_text())

    real, imag = exact_truncation()
    real_hash = sha256_bytes(
        json.dumps(
            [fraction_record(x) for x in real],
            separators=(",", ":"),
            sort_keys=True,
        ).encode()
    )
    assert real_hash == archived["truncated_q_real_coefficients_sha256"]
    assert imag[0] == -1 and all(x == 0 for x in imag[1:])

    initial, denominator, initial_content = initial_reversed_state(real, imag)
    initial_hash = gaussian_state_sha256(initial)
    assert initial_hash == archived[
        "initial_reversed_primitive_gaussian_state_sha256"
    ]
    assert denominator == archived["initial_cleared_denominator"]
    assert initial_content == 1
    schur = fraction_free_schur(
        initial, archived["fraction_free_schur_records"]
    )
    archived_product = fraction_from_record(
        archived["reflection_factor_product_rational_lower"]
    )
    assert schur["archived_128_bit_product"] == archived_product
    archived_boundary = 2 * archived_product**2
    assert archived_boundary == fraction_from_record(
        archived["boundary_modulus_squared_rational_lower"]
    )

    tail = exact_tail_bound()
    assert tail == fraction_from_record(
        archived["exponential_tail_rational_upper"]
    )
    assert tail**2 == fraction_from_record(
        archived["exponential_tail_squared_rational_upper"]
    )
    assert archived_boundary > tail**2
    independent_boundary = 2 * schur["independent_160_bit_product"] ** 2
    assert independent_boundary > tail**2

    jets = phi_jets(120)
    jet_hash = vector_sha256(jets)
    assert jet_hash == archived["computed_integral_jets_sha256"]
    g_jets = composed_G_jets(60, phi_jets(60))
    phi_hp_jets = phi_jets(46)
    g_hp_jets = g_jets[:47]
    assert vector_sha256(phi_hp_jets) == archived_hp["phi_jets_sha256"]
    assert vector_sha256(g_hp_jets) == archived_hp["G_jets_sha256"]
    hp_records = independent_hp_audit(g_hp_jets, archived_hp)

    result = {
        "audit_script_sha256": file_sha256(Path(__file__)),
        "frozen_certificate_hashes": actual_hashes,
        "python_version": sys.version,
        "sympy_version": sp.__version__,
        "candidate": {
            "base_terms": [list(item) for item in BASE_TERMS],
            "exponential_terms": [list(item) for item in EXPONENTIAL_TERMS],
            "phi_at_zero": "0",
            "phi_at_one": "1",
            "real_entire": True,
        },
        "integral_jets": {
            "phi_computed_through": 120,
            "phi_jet_sha256": jet_hash,
            "matches_archive": True,
            "all_order_phi_formula_is_integral_by_binomial_expression": True,
            "G_direct_composition_checked_through": 60,
            "all_computed_G_jets_integral": True,
            "G_jet_sha256": vector_sha256(g_jets),
        },
        "truncation": {
            "degree": len(real) - 1,
            "real_coefficients_sha256": real_hash,
            "matches_archive": True,
            "initial_primitive_state_sha256": initial_hash,
            "initial_state_matches_archive": True,
            "preprimitive_common_denominator": denominator,
            "removed_initial_integer_content": initial_content,
            "cleared_denominator_matches_archive": True,
        },
        "fraction_free_schur": {
            "orientation": (
                "conj(leading)*P-constant*P_star, then divide by w "
                "and ordinary integer content"
            ),
            "stage_count": len(archived["fraction_free_schur_records"]),
            "all_61_gaps_positive": True,
            "all_stage_records_match_archive": schur[
                "all_stage_comparisons_pass"
            ],
            "stage_comparisons": schur["comparisons"],
            "final_constant": schur["final_constant"],
        },
        "boundary_and_tail": {
            "archived_128_bit_reflection_product": fraction_record(
                archived_product
            ),
            "archived_boundary_squared_lower": fraction_record(
                archived_boundary
            ),
            "independent_160_bit_reflection_product": fraction_record(
                schur["independent_160_bit_product"]
            ),
            "independent_160_bit_factor_sha256": schur[
                "independent_160_bit_factor_sha256"
            ],
            "independent_boundary_squared_lower": fraction_record(
                independent_boundary
            ),
            "tail_upper": fraction_record(tail),
            "tail_squared_upper": fraction_record(tail**2),
            "archived_exact_rouche_inequality": archived_boundary > tail**2,
            "independent_160_bit_exact_rouche_inequality": (
                independent_boundary > tail**2
            ),
            "archived_squared_margin_floor_log10": math.floor(
                math.log10(float(archived_boundary / tail**2))
            ),
        },
        "both_targets": {
            "one_plus_i_zero_free_closed_disk": True,
            "one_minus_i_by_real_coefficient_conjugation": True,
            "radius": [RADIUS.numerator, RADIUS.denominator],
        },
        "diagonal_hp": {
            "phi_jet_sha256_through_46": vector_sha256(phi_hp_jets),
            "G_jet_sha256_through_46": vector_sha256(g_hp_jets),
            "jet_hashes_match_archive": True,
            "max_n": 15,
            "records": hp_records,
            "all_records_match_archive": True,
            "endpoint_decades": [
                item["endpoint"]["decade"] for item in hp_records
            ],
        },
        "root_diagnostics": numerical_root_crosscheck(
            archived["nearest_roots_of_phi_equals_1_plus_i_diagnostic"]
        ),
        "conclusion": (
            "The degree-61 truncation, fraction-free Schur chain, "
            "reflection-product boundary bound, exponential-tail bound, "
            "Rouche comparison, conjugate-target transfer, and integral "
            "jet formulas independently pass; all diagonal HP records "
            "through n=15 independently match."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
