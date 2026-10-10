#!/usr/bin/env python3
"""Replay the exact quadratic Stein--Robin correction package.

The companion note contains the all-parameter proofs.  This script checks
their polynomial, Gaussian-endpoint, Robin-lattice, integral-coordinate,
denominator, and primitive-content normalizations exactly through N=80.
Finite checks are not extrapolated to a statement about e+pi.
"""

from __future__ import annotations

import hashlib
import json
import math
import time
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT / "sources/common_kernel_stein_robin_quadratic_correction_barrier.md"
)
OUTPUT = (
    ROOT
    / "results/common_kernel_stein_robin_quadratic_correction_certificate.json"
)

# Failure guard only.  It neither allocates nor caps the available Colab RAM.
RSS_GUARD_KIB = 8 * 1024 * 1024
MAX_N = 80
SELECTED_N = {1, 2, 3, 4, 5, 6, 8, 10, 16, 25, 40, 60, 80}

DEPENDENCIES = {
    "sources/common_kernel_stein_robin_parameterization.md":
        "6853ceef8ae4065c65d0954a5ef0d0c7b1ae43e76167f999cbd3a11818432406",
    "scripts/common_kernel_stein_robin_certificate.py":
        "a841840c5b6abe8778ae58cb50eb00eb201cacdcbde389f32a9f4cdae9673bbf",
    "results/common_kernel_stein_robin_certificate.json":
        "be08f99f85f11a42f9f9efc32091eb6d6300a81b4511352ca58d0c6792d09aa5",
    "sources/common_kernel_positive_cone_endpoint_bootstrap_barrier.md":
        "596e21e493f16447307764b100bae383f5a639c7ad466150a50932b4a878d487",
    "scripts/common_kernel_positive_cone_endpoint_bootstrap_certificate.py":
        "ca1db0bc142979bb9e566d5a93664ae3bcb914c9ec7aaa698e3f36c3b2171d4e",
    "results/common_kernel_positive_cone_endpoint_bootstrap_certificate.json":
        "35cf99fe9eb6e4a2203d2c357a3a04b36478628bce686a4907bb3dcd6e248a3d",
}


Number = int | Fraction
Polynomial = list[Number]
GaussianInteger = tuple[int, int]
Coordinates = tuple[Fraction, Fraction, Fraction, Fraction]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def control_audit(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    forbidden = [
        {"offset": index, "byte": byte}
        for index, byte in enumerate(data)
        if byte < 32 and byte != 10
    ]
    return {
        "path": str(path.relative_to(ROOT)),
        "bytes": len(data),
        "forbidden_control_bytes": forbidden,
        "clean": not forbidden,
    }


def peak_rss_kib() -> int:
    for line in Path("/proc/self/status").read_text().splitlines():
        if line.startswith("VmHWM:"):
            fields = line.split()
            assert fields[2] == "kB"
            return int(fields[1])
    raise RuntimeError("VmHWM is unavailable")


def trim(poly: Polynomial) -> Polynomial:
    result = poly[:]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    if not result:
        return [0]
    return result


def poly_add(*polynomials: Polynomial) -> Polynomial:
    size = max((len(poly) for poly in polynomials), default=1)
    output: Polynomial = [0] * size
    for poly in polynomials:
        for index, value in enumerate(poly):
            output[index] += value
    return trim(output)


def poly_scale(poly: Polynomial, scalar: Number) -> Polynomial:
    return trim([scalar * value for value in poly])


def poly_multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    output: Polynomial = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            output[left_index + right_index] += left_value * right_value
    return trim(output)


def poly_power(poly: Polynomial, exponent: int) -> Polynomial:
    assert exponent >= 0
    result: Polynomial = [1]
    base = poly[:]
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = poly_multiply(result, base)
        remaining >>= 1
        if remaining:
            base = poly_multiply(base, base)
    return result


def derivative(poly: Polynomial) -> Polynomial:
    if len(poly) <= 1:
        return [0]
    return trim([index * poly[index] for index in range(1, len(poly))])


def shift(poly: Polynomial, amount: int = 1) -> Polynomial:
    assert amount >= 0
    if trim(poly) == [0]:
        return [0]
    return [0] * amount + poly


def stein_t(poly: Polynomial) -> Polynomial:
    """-t C'(t)-(1-t)C(t), with ascending t coefficients."""
    return poly_add(
        poly_scale(shift(derivative(poly)), -1),
        poly_scale(poly, -1),
        shift(poly),
    )


def stein_x(poly: Polynomial) -> Polynomial:
    """(1-x)P'(x)-xP(x), with ascending x coefficients."""
    deriv = derivative(poly)
    return poly_add(deriv, poly_scale(shift(deriv), -1), poly_scale(shift(poly), -1))


def divide_monic(numerator: Polynomial, denominator: Polynomial) -> tuple[Polynomial, Polynomial]:
    """Exact Euclidean division; denominator must be monic."""
    denominator = trim(denominator)
    remainder = trim(numerator)
    assert denominator[-1] == 1
    if len(remainder) < len(denominator):
        return [0], remainder
    quotient: Polynomial = [0] * (len(remainder) - len(denominator) + 1)
    while remainder != [0] and len(remainder) >= len(denominator):
        offset = len(remainder) - len(denominator)
        leading = remainder[-1]
        quotient[offset] += leading
        subtractor = [0] * offset + [leading * value for value in denominator]
        remainder = poly_add(remainder, poly_scale(subtractor, -1))
    return trim(quotient), trim(remainder)


def t_to_x(poly: Polynomial) -> Polynomial:
    """Substitute t=1-x.  The same map also sends x-coefficients to t."""
    output: Polynomial = [0]
    for power, coefficient in enumerate(poly):
        term = [
            coefficient * math.comb(power, index) * ((-1) ** index)
            for index in range(power + 1)
        ]
        output = poly_add(output, term)
    return trim(output)


def gaussian_multiply(left: GaussianInteger, right: GaussianInteger) -> GaussianInteger:
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c


def gaussian_power_w(exponent: int) -> GaussianInteger:
    result = (1, 0)
    base = (1, -1)
    for _ in range(exponent):
        result = gaussian_multiply(result, base)
    return result


def gaussian_eval_w(poly: Polynomial) -> tuple[Fraction, Fraction]:
    real = Fraction(0)
    imag = Fraction(0)
    power = (1, 0)
    for coefficient in poly:
        real += Fraction(coefficient) * power[0]
        imag += Fraction(coefficient) * power[1]
        power = gaussian_multiply(power, (1, -1))
    return real, imag


def functional_a_t(poly: Polynomial) -> Fraction:
    return sum(
        (Fraction(value) * math.factorial(index) for index, value in enumerate(poly)),
        Fraction(0),
    )


def tail_constants(max_degree: int) -> list[int]:
    """K_j with integral exp coordinate int e^(1-t)t^j = j! e-K_j."""
    values = [1]
    for index in range(1, max_degree + 1):
        values.append(index * values[-1] + 1)
    return values


def weighted_coordinates_t(poly: Polynomial) -> Coordinates:
    """Coordinates of the weighted integral in (e,pi,log(2),1)."""
    tails = tail_constants(len(poly) - 1)
    e_coefficient = functional_a_t(poly)
    rational_constant = -sum(
        (Fraction(value) * tails[index] for index, value in enumerate(poly)),
        Fraction(0),
    )

    denominator: Polynomial = [2, -2, 1]
    quotient, remainder = divide_monic(poly, denominator)
    rational_constant += 4 * sum(
        (Fraction(value, index + 1) for index, value in enumerate(quotient)),
        Fraction(0),
    )
    padded = remainder + [0] * (2 - len(remainder))
    alpha = Fraction(padded[0])
    beta = Fraction(padded[1])
    pi_coefficient = alpha + beta
    log_two_coefficient = -2 * beta
    return (
        Fraction(e_coefficient),
        pi_coefficient,
        log_two_coefficient,
        rational_constant,
    )


def coordinate_add(*coordinates: Coordinates) -> Coordinates:
    return tuple(
        sum((coordinate[index] for coordinate in coordinates), Fraction(0))
        for index in range(4)
    )  # type: ignore[return-value]


def coordinate_scale(coordinate: Coordinates, scalar: int) -> Coordinates:
    return tuple(scalar * value for value in coordinate)  # type: ignore[return-value]


def fraction_string(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def coordinate_record(coordinate: Coordinates) -> dict[str, str]:
    return {
        "e": fraction_string(coordinate[0]),
        "pi": fraction_string(coordinate[1]),
        "log_2": fraction_string(coordinate[2]),
        "rational": fraction_string(coordinate[3]),
    }


def lcm(left: int, right: int) -> int:
    return left // math.gcd(left, right) * right


def antiderivative_denominator(poly: Polynomial) -> int:
    output = 1
    for index, raw_value in enumerate(poly):
        value = int(raw_value)
        assert value == raw_value
        if value == 0:
            continue
        reduced_denominator = (index + 1) // math.gcd(index + 1, abs(value))
        output = lcm(output, reduced_denominator)
    return output


def polynomial_digest(poly: Polynomial) -> str:
    digest = hashlib.sha256()
    for index, value in enumerate(trim(poly)):
        encoded = f"{index}:{value};".encode()
        digest.update(encoded)
    return digest.hexdigest()


def exact_static_checks() -> dict[str, object]:
    denominator: Polynomial = [2, -2, 1]
    u_poly: Polynomial = [0, 1, Fraction(-1, 2)]
    one_minus_t: Polynomial = [1, -1]
    j_poly: Polynomial = [4, -6, 4, -1]

    assert poly_add(poly_scale(u_poly, 2), denominator) == [2]
    assert poly_multiply([2, -1], denominator) == j_poly
    positivity_remainder = poly_add(j_poly, poly_scale(one_minus_t, -3))
    expected_remainder = poly_add([0, 0, 1], poly_power([1, -1], 3))
    assert positivity_remainder == expected_remainder == [1, -3, 4, -1]

    assert functional_a_t(u_poly) == 0
    assert functional_a_t(one_minus_t) == 0
    assert functional_a_t(j_poly) == 0
    assert gaussian_eval_w(u_poly) == (1, 0)
    assert gaussian_eval_w(one_minus_t) == (0, 1)
    assert gaussian_eval_w(j_poly) == (0, 0)

    u_coordinate = weighted_coordinates_t(u_poly)
    one_minus_t_coordinate = weighted_coordinates_t(one_minus_t)
    j_coordinate = weighted_coordinates_t(j_poly)
    assert u_coordinate == (0, 1, 0, Fraction(-3, 2))
    assert one_minus_t_coordinate == (0, 0, 2, 1)
    assert j_coordinate == (0, 0, 0, 10)

    # Images of 1,t,t^2 at w form a rank-two integral endpoint map.
    endpoint_columns = [
        gaussian_eval_w(stein_t([1])),
        gaussian_eval_w(stein_t([0, 1])),
        gaussian_eval_w(stein_t([0, 0, 1])),
    ]
    assert endpoint_columns == [(0, -1), (-2, 0), (-2, 4)]
    kernel_direction: Polynomial = [-4, 1, -1]
    assert gaussian_eval_w(stein_t(kernel_direction)) == (0, 0)
    assert stein_t(kernel_direction) == j_poly
    # Equations -2*c1-2*c2=0 and -c0+4*c2=0 have primitive
    # integer kernel Z*(-4,1,-1) after the sign convention c2=-q.
    assert math.gcd(math.gcd(4, 1), 1) == 1

    return {
        "U_coefficients_t": [fraction_string(Fraction(value)) for value in u_poly],
        "one_minus_t_coefficients": one_minus_t,
        "J_coefficients_t": j_poly,
        "J_factorization": "J=(2-t)(t^2-2t+2)",
        "positivity_identity": "J-3(1-t)=t^2+(1-t)^3",
        "endpoint_map_columns_for_1_t_t2": [
            [fraction_string(real), fraction_string(imag)]
            for real, imag in endpoint_columns
        ],
        "primitive_integer_kernel_direction": kernel_direction,
        "integral_coordinates": {
            "U": coordinate_record(u_coordinate),
            "1-t": coordinate_record(one_minus_t_coordinate),
            "J": coordinate_record(j_coordinate),
        },
    }


def exact_row(n_value: int) -> tuple[dict[str, object], dict[str, object]]:
    target = math.factorial(n_value)
    real_part, imag_part = gaussian_power_w(n_value)
    m_value = target - real_part
    assert m_value % 2 == 0
    assert m_value >= 0
    q_value = 0 if imag_part <= 0 else (imag_part + 2) // 3

    p_zero_t: Polynomial = [
        target // math.factorial(index + 1) for index in range(n_value)
    ]
    t_power_n: Polynomial = [0] * n_value + [1]
    assert poly_add([target], stein_t(p_zero_t)) == t_power_n

    correction_t: Polynomial = [
        imag_part - 4 * q_value,
        q_value - m_value // 2,
        -q_value,
    ]
    u_poly: Polynomial = [0, 1, Fraction(-1, 2)]
    one_minus_t: Polynomial = [1, -1]
    j_poly: Polynomial = [4, -6, 4, -1]
    correction_image = stein_t(correction_t)
    expected_image = poly_add(
        poly_scale(u_poly, m_value),
        poly_scale(one_minus_t, -imag_part),
        poly_scale(j_poly, q_value),
    )
    assert correction_image == expected_image

    # Check several members of the full affine family, not only the
    # positivity choice.  The static endpoint-map computation proves the
    # integer kernel direction is primitive.
    particular_correction: Polynomial = [imag_part, -m_value // 2, 0]
    for test_q in sorted({-4, -1, 0, 1, 3, q_value}):
        test_correction = poly_add(
            particular_correction,
            poly_scale([-4, 1, -1], test_q),
        )
        assert gaussian_eval_w(stein_t(test_correction)) == (
            target - real_part,
            -imag_part,
        )

    p_t = poly_add(p_zero_t, correction_t)
    residual_t = poly_add([target], stein_t(p_t))
    expected_residual = poly_add(t_power_n, expected_image)
    assert residual_t == expected_residual
    assert functional_a_t(residual_t) == target
    assert gaussian_eval_w(residual_t) == (target, 0)

    positivity_remainder = poly_add(j_poly, poly_scale(one_minus_t, -3))
    if imag_part <= 0:
        positive_decomposition = poly_add(
            t_power_n,
            poly_scale(u_poly, m_value),
            poly_scale(one_minus_t, -imag_part),
        )
        positive_scalars = [1, m_value, -imag_part]
        decomposition_label = "t^N+M*U+(-I)*(1-t)"
    else:
        positive_decomposition = poly_add(
            t_power_n,
            poly_scale(u_poly, m_value),
            poly_scale(positivity_remainder, q_value),
            poly_scale(one_minus_t, 3 * q_value - imag_part),
        )
        positive_scalars = [1, m_value, q_value, 3 * q_value - imag_part]
        decomposition_label = (
            "t^N+M*U+q*(J-3(1-t))+(3q-I)*(1-t)"
        )
    assert residual_t == positive_decomposition
    assert all(value >= 0 for value in positive_scalars)
    for grid_index in range(101):
        t_value = Fraction(grid_index, 100)
        evaluation = sum(
            (Fraction(value) * t_value**index for index, value in enumerate(residual_t)),
            Fraction(0),
        )
        assert evaluation >= 0

    p_x = t_to_x(p_t)
    residual_x = t_to_x(residual_t)
    assert t_to_x(p_x) == trim(p_t)
    assert poly_add([target], stein_x(p_x)) == residual_x

    robin_modulus: Polynomial = [1, 0, 2, 0, 1]
    q_robin, remainder = divide_monic(p_x, robin_modulus)
    padded_remainder = remainder + [0] * (4 - len(remainder))
    u_value = int(padded_remainder[0])
    v_value = -int(padded_remainder[2])
    expected_remainder_x: Polynomial = [
        u_value,
        2 * u_value + 9 * v_value,
        -v_value,
        u_value + 4 * v_value,
    ]
    assert trim(expected_remainder_x) == trim(remainder)
    reconstructed_p = poly_add(
        poly_multiply(robin_modulus, q_robin),
        expected_remainder_x,
    )
    assert reconstructed_p == p_x

    image_x = stein_x(p_x)
    g_x, g_remainder = divide_monic(image_x, [1, 0, 1])
    assert g_remainder == [0]
    quotient_t, quotient_remainder = divide_monic(
        poly_add(residual_t, [-target]), [2, -2, 1]
    )
    assert quotient_remainder == [0]
    assert t_to_x(quotient_t) == g_x

    d_p = antiderivative_denominator(g_x)
    rho_from_x = Fraction(-target - int(p_x[0]), 1) + 4 * sum(
        (Fraction(int(value), index + 1) for index, value in enumerate(g_x)),
        Fraction(0),
    )
    tails = tail_constants(len(residual_t) - 1)
    exponential_tail = sum(
        (int(value) * tails[index] for index, value in enumerate(residual_t)),
        0,
    )
    rho_from_t = Fraction(-exponential_tail, 1) + 4 * sum(
        (Fraction(int(value), index + 1) for index, value in enumerate(quotient_t)),
        Fraction(0),
    )
    assert rho_from_x == rho_from_t
    numerator = rho_from_x.numerator
    denominator = rho_from_x.denominator
    assert d_p % denominator == 0

    h_value = math.gcd(target * denominator, abs(numerator))
    assert h_value == math.gcd(target, abs(numerator))
    assert target % h_value == 0
    primitive_a = target * denominator // h_value
    primitive_b = numerator // h_value
    assert math.gcd(abs(primitive_a), abs(primitive_b)) == 1
    cleared_b = (d_p // denominator) * numerator
    cleared_content = math.gcd(target * d_p, abs(cleared_b))
    assert cleared_content == (d_p // denominator) * h_value
    assert (target * d_p // cleared_content, cleared_b // cleared_content) == (
        primitive_a,
        primitive_b,
    )

    residual_coordinate = weighted_coordinates_t(residual_t)
    assert residual_coordinate == (
        Fraction(target),
        Fraction(target),
        Fraction(0),
        rho_from_t,
    )
    t_power_coordinate = weighted_coordinates_t(t_power_n)
    rhs_coordinate = coordinate_add(
        coordinate_scale((0, 1, 0, Fraction(-3, 2)), m_value),
        t_power_coordinate,
        coordinate_scale((0, 0, 2, 1), -imag_part),
        coordinate_scale((0, 0, 0, 10), q_value),
    )
    assert rhs_coordinate == residual_coordinate

    compact_row = {
        "N": n_value,
        "R_N": real_part,
        "I_N": imag_part,
        "M_N": m_value,
        "q_N": q_value,
        "D_P": d_p,
        "D": denominator,
        "B": numerator,
        "h": h_value,
        "cleared_content": cleared_content,
        "primitive_a": primitive_a,
        "primitive_b": primitive_b,
        "P_degree": len(trim(p_x)) - 1,
        "G_degree": -1 if trim(g_x) == [0] else len(trim(g_x)) - 1,
        "Q_Robin_degree": -1 if trim(q_robin) == [0] else len(trim(q_robin)) - 1,
        "u_Robin": u_value,
        "v_Robin": v_value,
        "positivity_decomposition": decomposition_label,
        "P_coefficients_sha256": polynomial_digest(p_x),
        "F_coefficients_t_sha256": polynomial_digest(residual_t),
        "G_coefficients_sha256": polynomial_digest(g_x),
    }
    selected_row = {
        **compact_row,
        "a_N": target,
        "correction_coefficients_t": [int(value) for value in correction_t],
        "residual_nonzero_coefficients_t": {
            str(index): int(value)
            for index, value in enumerate(residual_t)
            if value != 0
        },
        "weighted_integral_coordinates": coordinate_record(residual_coordinate),
        "primitive_linear_form": f"{primitive_a}*(e+pi)+({primitive_b})",
        "primitive_scale_D_over_h": f"{denominator}/{h_value}",
    }
    return compact_row, selected_row


def main() -> None:
    started = time.perf_counter()

    dependency_checks = {}
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        assert actual == expected, (relative, expected, actual)
        dependency_checks[relative] = {"expected": expected, "actual": actual}

    source_control = control_audit(SOURCE)
    script_control = control_audit(Path(__file__))
    assert source_control["clean"] and script_control["clean"]

    static_checks = exact_static_checks()
    compact_rows = []
    selected_rows = []
    for n_value in range(1, MAX_N + 1):
        compact, selected = exact_row(n_value)
        compact_rows.append(compact)
        if n_value in SELECTED_N:
            selected_rows.append(selected)

    rows_encoding = json.dumps(
        compact_rows, sort_keys=True, separators=(",", ":")
    ).encode()
    payload = {
        "schema": "common_kernel_stein_robin_quadratic_correction_certificate_v1",
        "logical_scope": (
            "Exact finite replay for the all-parameter quadratic correction "
            "and bounded-degree primitive-gap proofs in the companion note. "
            "It constructs a positive correction but proves that bounded "
            "degree cannot make the primitive form tend to zero; it proves "
            "no irrationality or transcendence statement about e+pi."
        ),
        "all_parameter_theorem": {
            "correction": (
                "C_Nq=I_N-4q+(q-M_N/2)t-q*t^2, where "
                "(1-i)^N=R_N+iI_N and M_N=N!-R_N"
            ),
            "residual": "t^N+M_N*U-I_N*(1-t)+q*J",
            "positive_choice": "q=0 if I_N<=0, otherwise ceil(I_N/3)",
            "quadratic_exhaustion": (
                "The endpoint map on corrections of degree <=2 has primitive "
                "integer kernel Z*(-4+t-t^2), whose Stein image is J."
            ),
            "quadratic_primitive_gap": "liminf Lambda >= pi-3/2",
            "fixed_degree_gap": (
                "For deg(C)<=m fixed, liminf Lambda >= "
                "3/(8*(m+1)^2*C_R*R^(m+1))>0."
            ),
            "open_scope": (
                "Growing-degree sparse or nonlocal corrections are not ruled out."
            ),
        },
        "static_exact_checks": static_checks,
        "finite_replay": {
            "N_range": [1, MAX_N],
            "row_count": len(compact_rows),
            "compact_rows_sha256": hashlib.sha256(rows_encoding).hexdigest(),
            "selected_rows": selected_rows,
            "finite_scope": (
                "Checks normalizations and examples only; all-N claims use "
                "the symbolic proofs in the companion source."
            ),
        },
        "dependency_checks": dependency_checks,
        "source_sha256": sha256(SOURCE),
        "control_audit": {"source": source_control, "script": script_control},
        "resource_policy": {
            "RSS_guard_kib": RSS_GUARD_KIB,
            "meaning": (
                "Failure guard only; it neither allocates nor limits the "
                "approximately 50 GiB available Colab RAM."
            ),
            "hardware_accelerator": (
                "Not used: exact integer and rational polynomial arithmetic "
                "at degree 80 is CPU-suitable."
            ),
        },
        "missing_lemma": (
            "A growing-degree Robin correction with sign control and enough "
            "primitive output cancellation, or a theorem ruling out that "
            "regime."
        ),
    }

    measured_peak = peak_rss_kib()
    assert measured_peak < RSS_GUARD_KIB
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    OUTPUT.write_bytes(encoded)
    elapsed = time.perf_counter() - started
    print(f"wrote {OUTPUT}")
    print(f"sha256 {hashlib.sha256(encoded).hexdigest()}")
    print(f"elapsed_seconds {elapsed:.6f}")
    print(f"peak_rss_kib {measured_peak}")


if __name__ == "__main__":
    main()
