#!/usr/bin/env python3
"""Exact algebraic certificate for the mixed-cubic accessible saddle.

All theorem-facing decisions use integer or rational arithmetic.  Decimal
values are emitted only in a separately labelled diagnostic section.
"""

from __future__ import annotations

import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path
from typing import TypeAlias

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "sources/mixed_cubic_accessible_saddle_exact_algebraic_certificate.md"
)
OUTPUT = (
    ROOT
    / "results/mixed_cubic_accessible_saddle_exact_algebraic_certificate.json"
)
DEPENDENCIES = {
    "results/mixed_cubic_boundary_cartier_content_and_recurrence_hashes.sha256":
        "34e61497fa2df8dd4dfcaf143be574bd3ada434977d41e6be75b590ba927a14c",
    "sources/mixed_cubic_accessible_saddle_handoff_20260827.md":
        "c8eb9e3b6267bb6ccc949aa145ccb4bf3ac627a1a6f97d51aebcda930b29aa0b",
}
RSS_GUARD_KIB = 40 * 1024 * 1024

Interval: TypeAlias = tuple[Fraction, Fraction]
ComplexPair: TypeAlias = tuple[sp.Expr, sp.Expr]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def peak_rss_kib() -> int:
    for line in Path("/proc/self/status").read_text().splitlines():
        if line.startswith("VmHWM:"):
            fields = line.split()
            assert fields[2] == "kB"
            return int(fields[1])
    raise RuntimeError("VmHWM unavailable")


def control_audit(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    forbidden = [
        {"offset": index, "byte": byte}
        for index, byte in enumerate(data)
        if byte < 32 and byte not in (9, 10)
    ]
    return {
        "path": str(path.relative_to(ROOT)),
        "bytes": len(data),
        "forbidden_control_bytes": forbidden,
        "clean": not forbidden,
    }


def markup_audit(path: Path) -> dict[str, object]:
    lines = path.read_text(encoding="utf-8").splitlines()
    stack: list[int] = []
    displays = 0
    for line_number, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped == r"\[":
            assert not stack, ("nested display", line_number, stack)
            stack.append(line_number)
            displays += 1
        elif stripped == r"\]":
            assert stack, ("orphan display close", line_number)
            stack.pop()
    assert not stack
    text = "\n".join(lines)
    assert text.count(r"\(") == text.count(r"\)")
    tags = re.findall(r"\\tag\{([^}]+)\}", text)
    assert tags == [str(index) for index in range(1, 35)]
    for phrase in [
        "All theorem-facing signs",
        "No coefficient asymptotic",
        "does not prove that \\(e+\\pi\\) is",
    ]:
        assert phrase in text
    return {
        "display_blocks": displays,
        "inline_delimiters_each": text.count(r"\("),
        "tags": tags,
        "status": "PASS",
    }


def verify_manifest(path: Path) -> list[dict[str, str]]:
    entries = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        expected, relative = line.split(maxsplit=1)
        relative = relative.strip()
        observed = sha256(ROOT / relative)
        assert observed == expected, (relative, observed, expected)
        entries.append({"path": relative, "sha256": observed})
    assert entries
    return entries


def dependency_audit() -> dict[str, object]:
    output = {}
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        observed = sha256(path)
        assert observed == expected, (relative, observed, expected)
        record: dict[str, object] = {
            "sha256": observed,
            "status": "PASS",
        }
        if path.suffix == ".sha256":
            record["manifest_entries"] = verify_manifest(path)
        output[relative] = record
    return output


def to_fraction(value: sp.Expr) -> Fraction:
    rational = sp.Rational(value)
    return Fraction(int(rational.p), int(rational.q))


def interval_add(left: Interval, right: Interval) -> Interval:
    return left[0] + right[0], left[1] + right[1]


def interval_neg(value: Interval) -> Interval:
    return -value[1], -value[0]


def interval_mul(left: Interval, right: Interval) -> Interval:
    products = [
        left[index] * right[jndex]
        for index in (0, 1)
        for jndex in (0, 1)
    ]
    return min(products), max(products)


def interval_scale(value: Interval, scalar: Fraction) -> Interval:
    return interval_mul(value, (scalar, scalar))


def interval_horner(poly: sp.Poly, value: Interval) -> Interval:
    coefficients = [to_fraction(coefficient) for coefficient in poly.all_coeffs()]
    answer = (coefficients[0], coefficients[0])
    for coefficient in coefficients[1:]:
        answer = interval_add(
            interval_mul(answer, value),
            (coefficient, coefficient),
        )
    return answer


def sign(value: sp.Expr) -> str:
    if value > 0:
        return "+"
    if value < 0:
        return "-"
    return "0"


def variations(signs: list[str]) -> int:
    nonzero = [item for item in signs if item != "0"]
    return sum(left != right for left, right in zip(nonzero, nonzero[1:]))


R, q, z = sp.symbols("R q z", real=True)
I = sp.I

G = sp.Poly(
    128 * z**6
    - 384 * z**5
    + 280 * z**4
    - 20 * z**3
    - 55 * z**2
    + z
    + 2,
    z,
    domain=sp.QQ,
)
F = sp.Poly(sp.expand(G.as_expr().subs(z, R**2)), R, domain=sp.QQ)

X = -(
    (4 * z + 1)
    * (16 * z**4 - 52 * z**3 + 49 * z**2 - 18 * z + 1)
) / 5
Y = (
    64 * z**5
    - 208 * z**4
    + 196 * z**3
    - 67 * z**2
    - 11 * z
    + 5
) / 5

P = sp.Poly(
    R**4
    * (
        12 * q**6
        + 16 * q**5
        + 12 * q**4
        + 32 * q**3
        - 12 * q**2
        + 16 * q
        - 12
    )
    + R**3
    * (
        -36 * q**6
        - 80 * q**5
        + 20 * q**4
        + 20 * q**2
        + 80 * q
        - 36
    )
    + R**2
    * (
        39 * q**6
        + 106 * q**5
        - 89 * q**4
        - 44 * q**3
        + 89 * q**2
        + 106 * q
        - 39
    )
    + R
    * (
        -18 * q**6
        - 60 * q**5
        + 50 * q**4
        + 50 * q**2
        + 60 * q
        - 18
    )
    + (
        3 * q**6
        + 14 * q**5
        + 3 * q**4
        + 28 * q**3
        - 3 * q**2
        + 14 * q
        - 3
    ),
    q,
)

BROAD_R: Interval = (
    Fraction(458133, 10**6),
    Fraction(458136, 10**6),
)
NARROW_R: Interval = (
    Fraction(458133387942745, 10**15),
    Fraction(458133387942746, 10**15),
)
RATIONAL_BASE = Fraction(91627, 200000)


def mod_reduce(expression: sp.Expr) -> sp.Expr:
    poly = sp.Poly(sp.expand(expression), z, domain=sp.QQ)
    return sp.rem(poly, G).as_expr()


def cadd(left: ComplexPair, right: ComplexPair) -> ComplexPair:
    return (
        mod_reduce(left[0] + right[0]),
        mod_reduce(left[1] + right[1]),
    )


def cmul(left: ComplexPair, right: ComplexPair) -> ComplexPair:
    return (
        mod_reduce(left[0] * right[0] - left[1] * right[1]),
        mod_reduce(left[0] * right[1] + left[1] * right[0]),
    )


def cscale(value: ComplexPair, scalar: sp.Expr) -> ComplexPair:
    return mod_reduce(scalar * value[0]), mod_reduce(scalar * value[1])


def cpow(value: ComplexPair, exponent: int) -> ComplexPair:
    answer: ComplexPair = (sp.Integer(1), sp.Integer(0))
    base = value
    power = exponent
    while power:
        if power & 1:
            answer = cmul(answer, base)
        base = cmul(base, base)
        power >>= 1
    return answer


def algebraic_identity_audit() -> dict[str, object]:
    tau: ComplexPair = (X, Y)
    tau2 = cpow(tau, 2)
    tau3 = cmul(tau2, tau)

    norm_remainder = mod_reduce(X**2 + Y**2 - z)
    saddle = cadd(
        cadd(
            cscale(tau3, 4),
            cmul((sp.Integer(6), sp.Integer(-1)), tau2),
        ),
        cadd(
            cmul((sp.Integer(0), sp.Integer(-1)), tau),
            (sp.Integer(-1), sp.Integer(-1)),
        ),
    )
    assert norm_remainder == 0
    assert saddle == (0, 0)

    saddle_derivative = cadd(
        cadd(cscale(tau2, 12), cmul((12, -2), tau)),
        (0, -1),
    )
    lambda_numerator = cmul(cmul((2, -2), tau), saddle_derivative)
    lambda_denominator = cmul(
        cmul(cadd((1, 0), tau), cadd((1, 0), cscale(tau, 2))),
        cadd((1, 0), cmul((1, -1), tau)),
    )
    lambda_re = sp.Rational(4, 15) * (
        3456 * z**5
        - 11040 * z**4
        + 9680 * z**3
        - 2460 * z**2
        - 810 * z
        + 217
    )
    lambda_im = -sp.Rational(2, 15) * (
        3456 * z**5
        - 12160 * z**4
        + 13000 * z**3
        - 4820 * z**2
        - 505 * z
        + 222
    )
    lambda_cross = cadd(
        lambda_numerator,
        cscale(cmul((lambda_re, lambda_im), lambda_denominator), -1),
    )
    assert lambda_cross == (0, 0)

    tau4 = cpow(tau, 4)
    amplitude_poly = cadd(
        cadd(cscale(tau4, 4), cscale(tau3, 8)),
        cadd(cscale(tau2, 2), cadd(cscale(tau, -2), (-1, 0))),
    )
    amplitude_numerator = cmul((1, -1), amplitude_poly)
    amplitude_denominator = cscale(
        cmul(
            cmul(tau, cadd((1, 0), tau)),
            cadd((1, 0), cmul((1, 1), tau)),
        ),
        32,
    )
    claimed_amplitude = (
        (2 * z - 1)
        * (128 * z**4 - 416 * z**3 + 352 * z**2 - 44 * z - 47)
        / 400
    )
    nr, ni = amplitude_numerator
    dr, di = amplitude_denominator
    amplitude_cross = mod_reduce(
        ni * dr
        - nr * di
        - claimed_amplitude * (dr**2 + di**2)
    )
    assert amplitude_cross == 0

    sx, sy = sp.symbols("sx sy", real=True)
    generic = sx + I * sy
    reflected = -1 - sx + I * sy

    def saddle_function(value: sp.Expr) -> sp.Expr:
        return 4 * value**3 + (6 - I) * value**2 - I * value - 1 - I

    def phase_function(value: sp.Expr) -> sp.Expr:
        return (
            (1 + 2 * value) ** 6
            * (1 + (1 - I) * value) ** 6
            / (value**4 * (1 + value) ** 4)
        )

    saddle_symmetry = sp.factor(
        sp.together(
            saddle_function(reflected)
            + sp.conjugate(saddle_function(generic))
        )
    )
    phase_symmetry = sp.factor(
        sp.together(
            phase_function(reflected)
            + sp.conjugate(phase_function(generic))
        )
    )
    assert saddle_symmetry == 0
    assert phase_symmetry == 0

    return {
        "x_squared_plus_y_squared_minus_z_remainder": str(norm_remainder),
        "S_tau_remainder_pair": [str(item) for item in saddle],
        "lambda_cross_multiplication_remainder_pair": [
            str(item) for item in lambda_cross
        ],
        "amplitude_cross_multiplication_remainder": str(amplitude_cross),
        "saddle_reflection_identity_remainder": str(saddle_symmetry),
        "phase_reflection_identity_remainder": str(phase_symmetry),
        "status": "PASS",
    }


def angular_identity_and_discriminant_audit() -> tuple[dict[str, object], sp.Poly]:
    v = sp.symbols("v")
    psi = (
        (1 + 2 * v) ** 6
        * (1 + (1 - I) * v) ** 6
        / (v**4 * (1 + v) ** 4)
    )
    saddle_polynomial = 4 * v**3 + (6 - I) * v**2 - I * v - 1 - I
    log_derivative_remainder = sp.factor(
        sp.together(
            sp.diff(psi, v) / psi
            - (2 - 2 * I)
            * saddle_polynomial
            / (v * (1 + v) * (1 + 2 * v) * (1 + (1 - I) * v))
        )
    )
    assert log_derivative_remainder == 0

    xq = R * (1 - q**2) / (1 + q**2)
    yq = 2 * R * q / (1 + q**2)
    aq = R**2
    A = 1 + 4 * xq + 4 * aq
    B = 1 + 2 * xq + 2 * yq + 2 * aq
    C = 1 + 2 * xq + aq
    D = -12 * yq * B * C + 6 * (xq - yq) * A * C + 4 * yq * A * B
    angular_numerator = sp.factor(
        sp.together(D + 2 * R * P.as_expr() / (1 + q**2) ** 3)
    )
    assert angular_numerator == 0

    leading = sp.factor(P.LC())
    assert leading == 3 * (R - 1) ** 2 * (2 * R - 1) ** 2
    discriminant = sp.factor(sp.discriminant(P.as_expr(), q))
    H_expression = sp.cancel(discriminant / (2**27 * R**4))
    H = sp.Poly(H_expression, R, domain=sp.QQ)
    assert H.degree() == 32
    assert discriminant == 2**27 * R**4 * H.as_expr()

    H_interval = interval_horner(H, BROAD_R)
    assert H_interval[0] > 400000
    assert H_interval[1] < 600000
    return {
        "psi_log_derivative_remainder": str(log_derivative_remainder),
        "angular_identity_remainder": str(angular_numerator),
        "leading_coefficient_factorization": str(leading),
        "discriminant_factorization": "2^27*R^4*H(R)",
        "H_degree": int(H.degree()),
        "H_nonzero_term_count": len(H.terms()),
        "H_interval_coarse_certificate": ["400000", "600000"],
        "status": "PASS",
    }, H


def root_isolation_audit() -> dict[str, object]:
    broad_lo = sp.Rational(BROAD_R[0].numerator, BROAD_R[0].denominator)
    broad_hi = sp.Rational(BROAD_R[1].numerator, BROAD_R[1].denominator)
    narrow_lo = sp.Rational(NARROW_R[0].numerator, NARROW_R[0].denominator)
    narrow_hi = sp.Rational(NARROW_R[1].numerator, NARROW_R[1].denominator)
    a_lo = narrow_lo**2
    a_hi = narrow_hi**2

    assert BROAD_R[0] < NARROW_R[0] < NARROW_R[1] < BROAD_R[1]
    assert BROAD_R[0] < RATIONAL_BASE < BROAD_R[1]
    assert NARROW_R[1] < Fraction(1, 2)

    f_narrow_count = int(F.count_roots(narrow_lo, narrow_hi))
    f_half_count = int(F.count_roots(0, sp.Rational(1, 2)))
    f_positive_count = int(F.count_roots(0, sp.oo))
    assert f_narrow_count == 1
    assert f_half_count == 1
    assert f_positive_count == 2
    assert F.eval(narrow_lo) > 0 > F.eval(narrow_hi)

    g_before_count = int(G.count_roots(0, a_lo))
    g_narrow_count = int(G.count_roots(a_lo, a_hi))
    g_after_count = int(G.count_roots(a_hi, sp.oo))
    assert (g_before_count, g_narrow_count, g_after_count) == (0, 1, 1)
    assert G.eval(a_lo) > 0 > G.eval(a_hi)

    return {
        "broad_radius_interval": [str(item) for item in BROAD_R],
        "narrow_radius_interval": [str(item) for item in NARROW_R],
        "narrow_squared_radius_interval": [str(a_lo), str(a_hi)],
        "f_root_count_narrow": f_narrow_count,
        "f_root_count_(0,1/2)": f_half_count,
        "f_positive_root_count": f_positive_count,
        "g_positive_counts_before_inside_after": [
            g_before_count,
            g_narrow_count,
            g_after_count,
        ],
        "selected_root_is_smaller_positive_root": True,
        "radius_lt_one_half": True,
        "status": "PASS",
    }


def rational_sturm_and_homotopy_audit() -> dict[str, object]:
    base = sp.Rational(RATIONAL_BASE.numerator, RATIONAL_BASE.denominator)
    base_poly = sp.Poly(P.as_expr().subs(R, base), q, domain=sp.QQ)
    sequence = sp.sturm(base_poly)
    degrees = [int(poly.degree()) for poly in sequence]
    assert degrees == [6, 5, 4, 3, 2, 1, 0]

    negative_infinity = [
        sign(poly.LC() * (-1) ** poly.degree()) for poly in sequence
    ]
    positive_infinity = [sign(poly.LC()) for poly in sequence]
    assert negative_infinity == ["+", "-", "+", "-", "-", "-", "+"]
    assert positive_infinity == ["+", "+", "+", "+", "-", "+", "+"]
    variation_negative = variations(negative_infinity)
    variation_positive = variations(positive_infinity)
    assert (variation_negative, variation_positive) == (4, 2)
    assert base_poly.count_roots(-sp.oo, sp.oo) == 2

    return {
        "rational_base_radius": str(RATIONAL_BASE),
        "sturm_degrees": degrees,
        "negative_infinity_signs": negative_infinity,
        "positive_infinity_signs": positive_infinity,
        "variations": {
            "negative_infinity": variation_negative,
            "positive_infinity": variation_positive,
            "difference": variation_negative - variation_positive,
        },
        "homotopy_ledger": (
            "the leading coefficient and discriminant are nonzero on the "
            "connected broad interval, so the real-root count is constant"
        ),
        "selected_embedding_real_root_count": 2,
        "status": "PASS",
    }


def fixed_radius_sign_audit() -> dict[str, object]:
    points = [
        ("-282", sp.Integer(-282), "positive"),
        ("-281", sp.Integer(-281), "negative"),
        ("11/40", sp.Rational(11, 40), "negative"),
        ("69/250", sp.Rational(69, 250), "positive"),
    ]
    intervals: dict[str, Interval] = {}
    rows = []
    for label, point, expected in points:
        value_poly = sp.Poly(P.as_expr().subs(q, point), R, domain=sp.QQ)
        enclosure = interval_horner(value_poly, NARROW_R)
        intervals[label] = enclosure
        observed = (
            "positive"
            if enclosure[0] > 0
            else "negative"
            if enclosure[1] < 0
            else "undetermined"
        )
        assert observed == expected
        rows.append({
            "q": label,
            "certified_sign": observed,
        })

    assert intervals["-282"][0] > 6_000_000_000
    assert intervals["-281"][1] < -4_000_000_000
    assert intervals["11/40"][1] < Fraction(-2, 25)
    assert intervals["69/250"][0] > Fraction(3, 200)

    leading_interval = interval_horner(
        sp.Poly(P.LC(), R, domain=sp.QQ),
        NARROW_R,
    )
    assert leading_interval[0] > 0
    return {
        "point_signs": rows,
        "coarse_exact_margins": {
            "P(-282)": ">6000000000",
            "P(-281)": "<-4000000000",
            "P(11/40)": "<-2/25",
            "P(69/250)": ">3/200",
        },
        "leading_coefficient_positive": True,
        "root_brackets": [
            ["-282", "-281"],
            ["11/40", "69/250"],
        ],
        "P_sign_pattern": [
            "positive on (-infinity,q_-)",
            "negative on (q_-,q_+)",
            "positive on (q_+,+infinity)",
        ],
        "angular_derivative_sign_pattern": [
            "negative on (-infinity,q_-)",
            "positive on (q_-,q_+)",
            "negative on (q_+,+infinity)",
        ],
        "status": "PASS",
    }


def selected_saddle_interval_audit() -> dict[str, object]:
    a_interval = (
        NARROW_R[0] * NARROW_R[0],
        NARROW_R[1] * NARROW_R[1],
    )
    x_interval = interval_horner(sp.Poly(X, z, domain=sp.QQ), a_interval)
    y_interval = interval_horner(sp.Poly(Y, z, domain=sp.QQ), a_interval)
    denominator = interval_add(NARROW_R, x_interval)
    assert x_interval[0] > Fraction(3, 10)
    assert x_interval[1] < Fraction(1, 2)
    assert y_interval[0] > Fraction(1, 5)
    assert y_interval[1] < Fraction(1, 4)
    assert denominator[0] > 0

    low_q = Fraction(11, 40)
    high_q = Fraction(69, 250)
    low_margin = interval_add(
        y_interval,
        interval_neg(interval_scale(denominator, low_q)),
    )
    high_margin = interval_add(
        interval_scale(denominator, high_q),
        interval_neg(y_interval),
    )
    assert low_margin[0] > Fraction(1, 2000)
    assert high_margin[0] > Fraction(1, 10000)

    return {
        "x_coarse_interval": ["3/10", "1/2"],
        "y_coarse_interval": ["1/5", "1/4"],
        "R_plus_x_positive": True,
        "q_tau_definition": "y/(R+x)",
        "q_tau_interval": ["11/40", "69/250"],
        "comparison_margins": {
            "y-(11/40)(R+x)": ">1/2000",
            "(69/250)(R+x)-y": ">1/10000",
        },
        "identification": (
            "S(tau)=0 and the angular identity make q_tau a root; "
            "its interval identifies it with q_+"
        ),
        "status": "PASS",
    }


def curvature_and_amplitude_sign_audit() -> dict[str, object]:
    a_interval = (
        NARROW_R[0] * NARROW_R[0],
        NARROW_R[1] * NARROW_R[1],
    )
    lambda_re = sp.Poly(
        sp.Rational(4, 15)
        * (
            3456 * z**5
            - 11040 * z**4
            + 9680 * z**3
            - 2460 * z**2
            - 810 * z
            + 217
        ),
        z,
        domain=sp.QQ,
    )
    amplitude = sp.Poly(
        (2 * z - 1)
        * (128 * z**4 - 416 * z**3 + 352 * z**2 - 44 * z - 47)
        / 400,
        z,
        domain=sp.QQ,
    )
    lambda_interval = interval_horner(lambda_re, a_interval)
    amplitude_interval = interval_horner(amplitude, a_interval)
    assert lambda_interval[0] > 2
    assert lambda_interval[1] < 3
    assert amplitude_interval[0] > Fraction(8, 125)
    assert amplitude_interval[1] < Fraction(13, 200)
    return {
        "Re_lambda_coarse_interval": ["2", "3"],
        "angular_second_derivative": "-Re(lambda)<-2",
        "Im_b2_over_b0_coarse_interval": ["8/125", "13/200"],
        "Re_lambda_positive": True,
        "Im_b2_over_b0_positive": True,
        "status": "PASS",
    }


def numerical_diagnostics() -> dict[str, object]:
    root = sp.CRootOf(F.as_expr(), 2)
    radius = sp.N(root, 35)
    a_value = sp.N(root**2, 35)
    x_value = sp.N(X.subs(z, root**2), 35)
    y_value = sp.N(Y.subs(z, root**2), 35)
    q_value = sp.N(
        Y.subs(z, root**2) / (root + X.subs(z, root**2)),
        35,
    )
    return {
        "label": "diagnostic decimals; unused in every proof decision",
        "R": str(radius),
        "a": str(a_value),
        "x": str(x_value),
        "y": str(y_value),
        "q_tau": str(q_value),
    }


def main() -> None:
    dependencies = dependency_audit()
    controls = [control_audit(SOURCE), control_audit(Path(__file__))]
    assert all(record["clean"] for record in controls)

    angular, _ = angular_identity_and_discriminant_audit()
    result = {
        "theorem": "exact algebraic accessible-saddle certificate",
        "dependency_audit": dependencies,
        "control_audit": controls,
        "markup_audit": markup_audit(SOURCE),
        "root_isolation": root_isolation_audit(),
        "algebraic_identities": algebraic_identity_audit(),
        "angular_identity_and_discriminant": angular,
        "rational_sturm_and_homotopy": rational_sturm_and_homotopy_audit(),
        "fixed_radius_signs": fixed_radius_sign_audit(),
        "selected_saddle_interval": selected_saddle_interval_audit(),
        "curvature_and_amplitude_signs": curvature_and_amplitude_sign_audit(),
        "numerical_diagnostics": numerical_diagnostics(),
        "scope": {
            "proved_all_parameter": [
                "exact isolation of the selected algebraic radius and saddle",
                "exactly two angular critical points on the selected circle",
                "the selected saddle is the unique modulus maximum",
                "Re(lambda)>2",
                "8/125<Im(b2(tau)/b0(tau))<13/200",
            ],
            "not_claimed": [
                "the fixed-circle saddle asymptotic or its uniform error term",
                "a coefficient asymptotic for B_m",
                "irrationality or transcendence of e+pi",
            ],
        },
    }

    observed_peak = peak_rss_kib()
    assert observed_peak < RSS_GUARD_KIB
    result["rss_guard_kib"] = RSS_GUARD_KIB
    result["rss_guard_passed"] = True

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "output": str(OUTPUT.relative_to(ROOT)),
        "peak_rss_kib": observed_peak,
        "status": "PASS",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
