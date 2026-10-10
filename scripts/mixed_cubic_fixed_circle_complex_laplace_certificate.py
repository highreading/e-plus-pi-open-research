#!/usr/bin/env python3
"""Exact checks for the mixed-cubic fixed-circle Laplace theorem.

The script certifies rational-function identities, the selected algebraic
saddle's local data, finite coefficient-orientation anchors, and the hashes
of the frozen dependency that proves the global unique-maximum statement.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources" / "mixed_cubic_fixed_circle_complex_laplace_theorem.md"
FROZEN_SOURCE = ROOT / "sources" / "mixed_cubic_boundary_cartier_content_and_recurrence.md"
ALGEBRAIC_SOURCE = ROOT / "sources" / "mixed_cubic_accessible_saddle_exact_algebraic_certificate.md"
ALGEBRAIC_SCRIPT = ROOT / "scripts" / "mixed_cubic_accessible_saddle_exact_algebraic_certificate.py"
ALGEBRAIC_JSON = ROOT / "results" / "mixed_cubic_accessible_saddle_exact_algebraic_certificate.json"
ALGEBRAIC_MANIFEST = ROOT / "results" / "mixed_cubic_accessible_saddle_exact_algebraic_hashes.sha256"

PINNED_ALGEBRAIC_HASHES = {
    ALGEBRAIC_SOURCE: "55454aa99b2fcd06a87d94c1b51bedd912a740b731ba57eecfc391bd4572fc65",
    ALGEBRAIC_SCRIPT: "ee24e16ce7e13781792898deead7736cfd9539ba16dc0dbc97b89fa3d061bccb",
    ALGEBRAIC_JSON: "f3377fda1444c21e11483688f7059446c5b709841f8914bdce8f68d2916c6ae0",
    ALGEBRAIC_MANIFEST: "3521a1347ec499acf98d60bdd8f48ba991ef2a9e20c00c806313e91d1e5d8b10",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pinned_algebraic_dependency_audit() -> dict[str, object]:
    observed = {path: sha256(path) for path in PINNED_ALGEBRAIC_HASHES}
    if any(observed[path] != expected for path, expected in PINNED_ALGEBRAIC_HASHES.items()):
        raise AssertionError(
            {
                str(path.relative_to(ROOT)): {
                    "expected": PINNED_ALGEBRAIC_HASHES[path],
                    "observed": observed[path],
                }
                for path in PINNED_ALGEBRAIC_HASHES
            }
        )
    manifest_rows = []
    for line in ALGEBRAIC_MANIFEST.read_text(encoding="utf-8").splitlines():
        digest, relative = line.split("  ", 1)
        path = ROOT / relative
        if sha256(path) != digest:
            raise AssertionError((relative, digest, sha256(path)))
        manifest_rows.append({"path": relative, "sha256": digest})
    if len(manifest_rows) != 3:
        raise AssertionError(manifest_rows)
    return {
        "pinned_files": {
            str(path.relative_to(ROOT)): digest
            for path, digest in PINNED_ALGEBRAIC_HASHES.items()
        },
        "manifest_rows_verified": manifest_rows,
        "global_unique_circle_maximum_dependency_verified": True,
    }


def rational_identities() -> dict[str, bool]:
    v = sp.symbols("v")
    ii = sp.I
    psi = (1 + 2 * v) ** 6 * (1 + (1 - ii) * v) ** 6 / (
        v**4 * (1 + v) ** 4
    )
    b0 = (1 + (1 + ii) * v) / (1 + v)
    ratio = (
        (1 - ii)
        * (1 + (1 + ii) * v) ** 3
        / (8 * v * (1 + v))
    )
    saddle = 4 * v**3 + (6 - ii) * v**2 - ii * v - 1 - ii
    h = (-1 + ii) * (1 + 2 * v) * (1 + (1 - ii) * v) / 32
    b2 = (
        (1 - ii)
        * (4 * v**4 + 8 * v**3 + 2 * v**2 - 2 * v - 1)
        / (32 * v * (1 + v) ** 2)
    )
    log_derivative_target = (
        (2 - 2 * ii)
        * saddle
        / (v * (1 + v) * (1 + 2 * v) * (1 + (1 - ii) * v))
    )
    return {
        "log_derivative_factorization": sp.cancel(
            sp.diff(psi, v) / psi - log_derivative_target
        )
        == 0,
        "five_eighths_ratio": sp.cancel(
            ratio - sp.Rational(5, 8) - h * sp.diff(psi, v) / psi
        )
        == 0,
        "integration_by_parts_amplitude": sp.cancel(
            b2 + v * sp.diff(b0 * h / v, v)
        )
        == 0,
    }


class QuotientField:
    """Small exact implementation of Q[a]/(g), with degree below six."""

    def __init__(self, symbol: sp.Symbol, modulus: sp.Expr):
        self.a = symbol
        self.g = sp.Poly(modulus, symbol, domain=sp.QQ)

    def red(self, value: object) -> sp.Poly:
        if isinstance(value, sp.Poly):
            polynomial = value
        else:
            polynomial = sp.Poly(value, self.a, domain=sp.QQ)
        return polynomial.rem(self.g)

    def add(self, left: sp.Poly, right: sp.Poly) -> sp.Poly:
        return self.red(left + right)

    def neg(self, value: sp.Poly) -> sp.Poly:
        return self.red(-value.as_expr())

    def sub(self, left: sp.Poly, right: sp.Poly) -> sp.Poly:
        return self.add(left, self.neg(right))

    def mul(self, left: sp.Poly, right: sp.Poly) -> sp.Poly:
        return self.red(left * right)

    def inv(self, value: sp.Poly) -> sp.Poly:
        return self.red(sp.invert(value, self.g))

    def div(self, left: sp.Poly, right: sp.Poly) -> sp.Poly:
        return self.mul(left, self.inv(right))


def algebraic_local_certificate() -> dict[str, object]:
    a = sp.symbols("a")
    g_expr = 128 * a**6 - 384 * a**5 + 280 * a**4 - 20 * a**3 - 55 * a**2 + a + 2
    field = QuotientField(a, g_expr)
    zero = field.red(0)

    def complex_value(real: object = 0, imaginary: object = 0) -> tuple[sp.Poly, sp.Poly]:
        return field.red(real), field.red(imaginary)

    def cadd(
        left: tuple[sp.Poly, sp.Poly], right: tuple[sp.Poly, sp.Poly]
    ) -> tuple[sp.Poly, sp.Poly]:
        return field.add(left[0], right[0]), field.add(left[1], right[1])

    def cneg(value: tuple[sp.Poly, sp.Poly]) -> tuple[sp.Poly, sp.Poly]:
        return field.neg(value[0]), field.neg(value[1])

    def csub(
        left: tuple[sp.Poly, sp.Poly], right: tuple[sp.Poly, sp.Poly]
    ) -> tuple[sp.Poly, sp.Poly]:
        return cadd(left, cneg(right))

    def cmul(
        left: tuple[sp.Poly, sp.Poly], right: tuple[sp.Poly, sp.Poly]
    ) -> tuple[sp.Poly, sp.Poly]:
        return (
            field.sub(field.mul(left[0], right[0]), field.mul(left[1], right[1])),
            field.add(field.mul(left[0], right[1]), field.mul(left[1], right[0])),
        )

    def cinv(value: tuple[sp.Poly, sp.Poly]) -> tuple[sp.Poly, sp.Poly]:
        norm = field.add(field.mul(value[0], value[0]), field.mul(value[1], value[1]))
        return field.div(value[0], norm), field.neg(field.div(value[1], norm))

    def cdiv(
        left: tuple[sp.Poly, sp.Poly], right: tuple[sp.Poly, sp.Poly]
    ) -> tuple[sp.Poly, sp.Poly]:
        return cmul(left, cinv(right))

    def cpow(value: tuple[sp.Poly, sp.Poly], exponent: int) -> tuple[sp.Poly, sp.Poly]:
        answer = complex_value(1)
        base = value
        while exponent:
            if exponent & 1:
                answer = cmul(answer, base)
            base = cmul(base, base)
            exponent //= 2
        return answer

    x = -(4 * a + 1) * (16 * a**4 - 52 * a**3 + 49 * a**2 - 18 * a + 1) / 5
    y = (64 * a**5 - 208 * a**4 + 196 * a**3 - 67 * a**2 - 11 * a + 5) / 5
    tau = complex_value(x, y)

    norm = field.sub(
        field.add(field.mul(tau[0], tau[0]), field.mul(tau[1], tau[1])),
        field.red(a),
    )
    saddle = cadd(
        cadd(cmul(complex_value(4), cpow(tau, 3)), cmul(complex_value(6, -1), cpow(tau, 2))),
        cadd(cmul(complex_value(0, -1), tau), complex_value(-1, -1)),
    )

    saddle_prime = cadd(
        cadd(cmul(complex_value(12), cpow(tau, 2)), cmul(complex_value(12, -2), tau)),
        complex_value(0, -1),
    )
    lambda_numerator = cmul(cmul(complex_value(2, -2), tau), saddle_prime)
    lambda_denominator = cmul(
        cmul(cadd(complex_value(1), tau), cadd(complex_value(1), cmul(complex_value(2), tau))),
        cadd(complex_value(1), cmul(complex_value(1, -1), tau)),
    )
    lambda_value = cdiv(lambda_numerator, lambda_denominator)
    lambda_real_target = field.red(
        sp.Rational(4, 15)
        * (3456 * a**5 - 11040 * a**4 + 9680 * a**3 - 2460 * a**2 - 810 * a + 217)
    )
    lambda_imag_target = field.red(
        -sp.Rational(2, 15)
        * (3456 * a**5 - 12160 * a**4 + 13000 * a**3 - 4820 * a**2 - 505 * a + 222)
    )

    fourth = cadd(
        cadd(
            cadd(cmul(complex_value(4), cpow(tau, 4)), cmul(complex_value(8), cpow(tau, 3))),
            cmul(complex_value(2), cpow(tau, 2)),
        ),
        cadd(cmul(complex_value(-2), tau), complex_value(-1)),
    )
    amplitude_numerator = cmul(complex_value(1, -1), fourth)
    amplitude_denominator = cmul(
        complex_value(32),
        cmul(
            cmul(tau, cadd(complex_value(1), tau)),
            cadd(complex_value(1), cmul(complex_value(1, 1), tau)),
        ),
    )
    amplitude_ratio = cdiv(amplitude_numerator, amplitude_denominator)
    amplitude_imag_target = field.red(
        (2 * a - 1) * (128 * a**4 - 416 * a**3 + 352 * a**2 - 44 * a - 47) / 400
    )

    lower = sp.Rational(1049431, 5000000)
    upper = sp.Rational(2098863, 10000000)
    lambda_sign_polynomial = (
        3456 * a**5 - 11040 * a**4 + 9680 * a**3 - 2460 * a**2 - 810 * a + 217
    )
    amplitude_polynomial = (
        (2 * a - 1) * (128 * a**4 - 416 * a**3 + 352 * a**2 - 44 * a - 47)
    )
    exact_signs = {
        "g_lower_positive": bool(g_expr.subs(a, lower) > 0),
        "g_upper_negative": bool(g_expr.subs(a, upper) < 0),
        "one_g_root_in_interval": sp.count_roots(g_expr, lower, upper) == 1,
        "lambda_real_no_zero_in_interval": sp.count_roots(
            lambda_sign_polynomial, lower, upper
        )
        == 0,
        "lambda_real_positive_at_lower": bool(
            lambda_sign_polynomial.subs(a, lower) > 0
        ),
        "amplitude_no_zero_in_interval": sp.count_roots(
            amplitude_polynomial, lower, upper
        )
        == 0,
        "amplitude_positive_at_lower": bool(amplitude_polynomial.subs(a, lower) > 0),
        "radius_below_one_quarter": bool(upper < sp.Rational(1, 4)),
    }

    identities = {
        "circle_identity": norm == zero,
        "saddle_real_identity": saddle[0] == zero,
        "saddle_imag_identity": saddle[1] == zero,
        "lambda_real_identity": field.sub(lambda_value[0], lambda_real_target) == zero,
        "lambda_imag_identity": field.sub(lambda_value[1], lambda_imag_target) == zero,
        "amplitude_imag_identity": field.sub(amplitude_ratio[1], amplitude_imag_target)
        == zero,
    }
    if not all(identities.values()) or not all(exact_signs.values()):
        raise AssertionError((identities, exact_signs))

    root = sp.CRootOf(g_expr, 0)
    return {
        "isolating_interval": [str(lower), str(upper)],
        "identities": identities,
        "exact_sturm_sign_checks": exact_signs,
        "diagnostic_selected_a": str(sp.N(root, 30)),
        "scope": (
            "These are independent local checks. The separately pinned exact-algebraic "
            "dependency certifies the global unique-circle maximum (UM)."
        ),
    }


def coefficient(numerator: sp.Poly, power: int, degree: int) -> sp.Expr:
    v = numerator.gens[0]
    total = sp.S.Zero
    for exponent in range(min(degree, numerator.degree()) + 1):
        tail = degree - exponent
        total += (
            numerator.coeff_monomial(v**exponent)
            * (-1) ** tail
            * sp.binomial(power + tail - 1, tail)
        )
    return sp.simplify(total)


def raw_residue(m_value: int, shift: int) -> sp.Expr:
    t = sp.symbols("t")
    ii = sp.I
    power = 4 * m_value + 1 + shift
    degree = power - 1
    numerator = sp.Poly(
        sp.expand(
            (ii + t) ** (6 * m_value)
            * (1 - ii - t) ** (6 * m_value)
            * (1 + ii + t) ** (1 + 3 * shift)
        ),
        t,
    )
    answer = sp.S.Zero
    for exponent in range(min(degree, numerator.degree()) + 1):
        tail = degree - exponent
        answer += (
            numerator.coeff_monomial(t**exponent)
            * (-1) ** tail
            * sp.binomial(power + tail - 1, tail)
            / (2 * ii) ** (power + tail)
        )
    answer *= sp.Rational(1, 2 ** (2 * m_value + 1 + 2 * shift))
    return sp.simplify(answer)


def finite_orientation_rows(max_m: int = 6) -> list[dict[str, object]]:
    v = sp.symbols("v")
    ii = sp.I
    rows: list[dict[str, object]] = []
    for m_value in range(1, max_m + 1):
        common = (1 + 2 * v) ** (6 * m_value) * (1 + (1 - ii) * v) ** (
            6 * m_value
        )
        numerator0 = sp.Poly(sp.expand(common * (1 + (1 + ii) * v)), v)
        i0 = coefficient(numerator0, 4 * m_value + 1, 4 * m_value)
        numerator1 = sp.Poly(sp.expand(common * (1 + (1 + ii) * v) ** 4), v)
        i1 = (
            (1 - ii)
            * coefficient(numerator1, 4 * m_value + 2, 4 * m_value + 1)
            / 8
        )
        c_value = (
            sp.Rational(1, 2 ** (7 * m_value + 2))
            * (-1) ** m_value
            * ii**m_value
            * (1 - ii)
        )
        residue0 = raw_residue(m_value, 0)
        residue1 = raw_residue(m_value, 1)
        checks = {
            "c0_positive_orientation": sp.simplify(c_value * i0 - residue0) == 0,
            "c1_positive_orientation": sp.simplify(c_value * i1 - residue1) == 0,
        }
        b_value = sp.simplify(2 * sp.im(residue1 * sp.conjugate(residue0)))
        checks["residue_determinant_positive"] = bool(b_value > 0)
        if not all(checks.values()):
            raise AssertionError((m_value, checks))
        rows.append(
            {
                "m": m_value,
                "checks": checks,
                "B_from_residues": str(b_value),
            }
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "results" / "mixed_cubic_fixed_circle_complex_laplace_certificate.json",
    )
    args = parser.parse_args()

    identities = rational_identities()
    if not all(identities.values()):
        raise AssertionError(identities)
    payload = {
        "schema": "mixed-cubic-fixed-circle-complex-laplace-v2",
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256(SOURCE),
        "frozen_dependency": str(FROZEN_SOURCE.relative_to(ROOT)),
        "frozen_dependency_sha256": sha256(FROZEN_SOURCE),
        "exact_algebraic_dependency": pinned_algebraic_dependency_audit(),
        "rational_function_identities": identities,
        "algebraic_local_certificate": algebraic_local_certificate(),
        "finite_orientation_anchors": finite_orientation_rows(),
        "proved_scope": [
            "The contour orientations and integration-by-parts signs are exact.",
            "The selected saddle, positive real Gaussian curvature, and positive determinant amplitude are exact local algebraic facts.",
            "The pinned algebraic dependency proves the global unique-circle-maximum hypothesis (UM).",
            "Lemma 3.1 therefore gives the unconditional B_m asymptotic and eventual positive sign.",
        ],
        "unproved_scope": [
            "The finite coefficient rows are implementation anchors, not an extrapolation.",
            "No explicit numerical m threshold is extracted from the asymptotic error.",
            "Downstream height and e-form matching claims are outside this theorem and require a separate re-audit.",
            "Nothing in this package proves irrationality or transcendence of e+pi.",
        ],
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(encoded, encoding="utf-8")
    print(hashlib.sha256(encoded.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main()
