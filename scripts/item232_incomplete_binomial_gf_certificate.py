#!/usr/bin/env python3
"""Exact certificate for Item 232's incomplete-binomial generating function.

The symbolic checks use only fractions and univariate polynomial arithmetic.
Finite coefficient replays are included as regression checks, not as the basis
of the all-n statements.  Output is deterministic and has no clock, host, or
absolute-path dependence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item232_incomplete_binomial_gf_certificate.json"

DEPENDENCIES = {
    "scripts/item229_j1_fixed_h_theta_certificate.py":
        "a8e2028ca6a53f8c843c25be375feac50e4704538686ee1e3a835f89aa11780f",
    "sources/item229_j1_fixed_h_theta_report.md":
        "7d70b934c2a7ba35f9bd48ad31d74c9eb1dc9ddca7bb4fdebd674286a13830c6",
    "results/item229_j1_fixed_h_theta_certificate.json":
        "3dcde380403f3e2080f87d8bb9cd81b55f5a9bfd34f3544a04a7d3acfa65b589",
}


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def resolve_dependency(relative_name: str) -> Path:
    candidates = (
        HERE.parent / relative_name,
        HERE / Path(relative_name).name,
    )
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise FileNotFoundError(relative_name)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def trim(poly: list[Fraction] | tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    answer = list(poly)
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return tuple(answer or [Fraction(0)])


def poly_add(left, right):
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else Fraction(0))
        + (right[index] if index < len(right) else Fraction(0))
        for index in range(size)
    ])


def poly_neg(poly):
    return tuple(-value for value in poly)


def poly_sub(left, right):
    return poly_add(left, poly_neg(right))


def poly_scale(poly, scalar):
    scalar = Fraction(scalar)
    return trim([scalar * value for value in poly])


def poly_mul(left, right):
    answer = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            answer[left_index + right_index] += left_value * right_value
    return trim(answer)


def poly_pow(poly, exponent: int):
    answer = (Fraction(1),)
    for _ in range(exponent):
        answer = poly_mul(answer, poly)
    return answer


def poly_derivative(poly):
    if len(poly) == 1:
        return (Fraction(0),)
    return trim([index * poly[index] for index in range(1, len(poly))])


def poly_divmod(dividend, divisor):
    remainder = list(trim(dividend))
    divisor = trim(divisor)
    if divisor == (Fraction(0),):
        raise ZeroDivisionError("zero polynomial")
    quotient = [Fraction(0)] * max(1, len(remainder) - len(divisor) + 1)
    while len(remainder) >= len(divisor) and any(remainder):
        offset = len(remainder) - len(divisor)
        scalar = remainder[-1] / divisor[-1]
        quotient[offset] += scalar
        for index, value in enumerate(divisor):
            remainder[offset + index] -= scalar * value
        remainder = list(trim(remainder))
    return trim(quotient), trim(remainder)


def poly_gcd(left, right):
    left = trim(left)
    right = trim(right)
    while right != (Fraction(0),):
        _, remainder = poly_divmod(left, right)
        left, right = right, remainder
    if left == (Fraction(0),):
        return (Fraction(1),)
    return poly_scale(left, 1 / left[-1])


def poly_eval(poly, value):
    value = Fraction(value)
    answer = Fraction(0)
    for coefficient in reversed(poly):
        answer = answer * value + coefficient
    return answer


def poly_shift_argument(poly, shift_value):
    """Return P(n+shift_value), with coefficients low-to-high in n."""
    answer = (Fraction(0),)
    for degree, coefficient in enumerate(poly):
        term = (Fraction(1),)
        for _ in range(degree):
            term = poly_mul(term, (Fraction(shift_value), Fraction(1)))
        answer = poly_add(answer, poly_scale(term, coefficient))
    return answer


class RationalFunction:
    """Reduced rational function in one indeterminate x."""

    def __init__(self, numerator, denominator=(Fraction(1),)):
        numerator = trim(tuple(Fraction(value) for value in numerator))
        denominator = trim(tuple(Fraction(value) for value in denominator))
        if denominator == (Fraction(0),):
            raise ZeroDivisionError("zero rational-function denominator")
        if numerator == (Fraction(0),):
            self.numerator = (Fraction(0),)
            self.denominator = (Fraction(1),)
            return
        common = poly_gcd(numerator, denominator)
        numerator, numerator_remainder = poly_divmod(numerator, common)
        denominator, denominator_remainder = poly_divmod(denominator, common)
        if numerator_remainder != (Fraction(0),) or denominator_remainder != (Fraction(0),):
            raise AssertionError("polynomial gcd division")
        if denominator[-1] < 0:
            numerator = poly_scale(numerator, -1)
            denominator = poly_scale(denominator, -1)
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def constant(value):
        return RationalFunction((Fraction(value),))

    def __add__(self, other):
        if not isinstance(other, RationalFunction):
            other = RationalFunction.constant(other)
        return RationalFunction(
            poly_add(
                poly_mul(self.numerator, other.denominator),
                poly_mul(other.numerator, self.denominator),
            ),
            poly_mul(self.denominator, other.denominator),
        )

    __radd__ = __add__

    def __neg__(self):
        return RationalFunction(poly_neg(self.numerator), self.denominator)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return RationalFunction.constant(other) - self

    def __mul__(self, other):
        if not isinstance(other, RationalFunction):
            other = RationalFunction.constant(other)
        return RationalFunction(
            poly_mul(self.numerator, other.numerator),
            poly_mul(self.denominator, other.denominator),
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        if not isinstance(other, RationalFunction):
            other = RationalFunction.constant(other)
        return RationalFunction(
            poly_mul(self.numerator, other.denominator),
            poly_mul(self.denominator, other.numerator),
        )

    def __pow__(self, exponent: int):
        return RationalFunction(
            poly_pow(self.numerator, exponent),
            poly_pow(self.denominator, exponent),
        )

    def derivative(self):
        return RationalFunction(
            poly_sub(
                poly_mul(poly_derivative(self.numerator), self.denominator),
                poly_mul(self.numerator, poly_derivative(self.denominator)),
            ),
            poly_mul(self.denominator, self.denominator),
        )

    def is_zero(self):
        return self.numerator == (Fraction(0),)


P0 = (-348, -2052, -3921, -2943, -756)
P1 = (1332, 7838, 14978, 11280, 2912)
P2 = (240, 1480, 2824, 1968, 448)
Q_POLY = (5, 25, 28)


def operator_symbolic_certificate() -> dict:
    """Verify the algebraic and differential identities after z=x(1+x)^2."""
    x = RationalFunction((0, 1))
    one = RationalFunction.constant(1)
    z = x * (one + x) ** 2
    g = (one + x) / ((one - x) * (one + 3 * x))
    theta_multiplier = x * (one + x) / (one + 3 * x)

    # (16+104z-27z^2)g^3-(16+108z)g^2+21zg-z = 0.
    algebraic = (
        (16 + 104 * z - 27 * z ** 2) * g ** 3
        - (16 + 108 * z) * g ** 2
        + 21 * z * g
        - z
    )
    if not algebraic.is_zero():
        raise AssertionError("algebraic parametrization identity")

    def theta(function):
        return theta_multiplier * function.derivative()

    def shifted_theta(function, shift_value):
        return theta(function) - shift_value * function

    def apply_polynomial(coefficients, shift_value, function):
        # Horner evaluation of P(theta-shift_value) on function.
        answer = RationalFunction.constant(0)
        for coefficient in reversed(coefficients):
            answer = shifted_theta(answer, shift_value) + coefficient * function
        return answer

    differential = (
        z ** 2 * apply_polynomial(P0, 0, g)
        + z * apply_polynomial(P1, 1, g)
        + apply_polynomial(P2, 2, g)
        - 40 * z
    )
    if not differential.is_zero():
        raise AssertionError("parametric differential identity")

    return {
        "classification": "EXACT_SYMBOLIC_CERTIFICATE",
        "parameter": "z=x(1+x)^2",
        "generating_function": "g=(1+x)/[(1-x)(1+3x)]",
        "algebraic_identity": (
            "(16+104z-27z^2)g^3-(16+108z)g^2+21zg-z=0"
        ),
        "theta_under_parameter": "theta=x(1+x)/(1+3x) d/dx",
        "differential_identity": (
            "z^2 P0(theta)g+z P1(theta-1)g+P2(theta-2)g=40z"
        ),
        "algebraic_numerator_zero": True,
        "differential_numerator_zero": True,
    }


def p_value(coefficients, n_value: int) -> int:
    return int(poly_eval(tuple(Fraction(value) for value in coefficients), n_value))


def s_direct(n_value: int) -> int:
    if n_value == 0:
        return 1
    return sum(
        (-1) ** index * math.comb(2 * n_value + index - 1, index)
        for index in range(n_value + 1)
    )


def t_boundary(n_value: int) -> int:
    return (-1) ** (n_value + 1) * math.comb(3 * n_value, n_value + 1)


def u_closed(n_value: int) -> Fraction:
    q_value = 28 * n_value * n_value + 25 * n_value + 5
    return Fraction(
        (-1) ** (n_value + 1) * q_value * math.comb(3 * n_value, n_value),
        4 * (n_value + 1) * (2 * n_value + 1),
    )


def factorization_certificate() -> dict:
    # P0=-3(3n+1)(3n+2)Q(n+1),
    # P2=8(n+2)(2n+3)Q(n), and 16P0+4P1+P2=0.
    n = (Fraction(0), Fraction(1))
    one = (Fraction(1),)
    q_n = tuple(Fraction(value) for value in Q_POLY)
    q_next = poly_add(q_n, poly_add(poly_scale(n, 56), (Fraction(53),)))
    p0_factored = poly_scale(
        poly_mul(poly_mul(poly_add(poly_scale(n, 3), one),
                          poly_add(poly_scale(n, 3), (Fraction(2),))), q_next),
        -3,
    )
    p2_factored = poly_scale(
        poly_mul(poly_mul(poly_add(n, (Fraction(2),)),
                          poly_add(poly_scale(n, 2), (Fraction(3),))), q_n),
        8,
    )
    p0_fraction = tuple(Fraction(value) for value in P0)
    p1_fraction = tuple(Fraction(value) for value in P1)
    p2_fraction = tuple(Fraction(value) for value in P2)
    if p0_factored != p0_fraction:
        raise AssertionError((p0_factored, p0_fraction))
    if p2_factored != p2_fraction:
        raise AssertionError((p2_factored, p2_fraction))
    if poly_add(poly_add(poly_scale(p0_fraction, 16),
                         poly_scale(p1_fraction, 4)), p2_fraction) != (Fraction(0),):
        raise AssertionError("Ore factor coefficient identity")
    return {
        "classification": "EXACT_SYMBOLIC_CERTIFICATE",
        "Q": "28n^2+25n+5",
        "P0_factor": "-3(3n+1)(3n+2)Q(n+1)",
        "P2_factor": "8(n+2)(2n+3)Q(n)",
        "coefficient_identity": "16P0+4P1+P2=0",
        "ore_factorization": (
            "P0+P1 E+P2 E^2=(-4P0+P2 E)(E-1/4)"
        ),
        "u_definition": "u_n=S_(n+1)-S_n/4",
        "u_closed_form": (
            "u_n=(-1)^(n+1)Q(n)binom(3n,n)/[4(n+1)(2n+1)]"
        ),
        "boundary_coupling": (
            "2n(2n+1)(4S_(n+1)-S_n)=Q(n)t_(n+1), "
            "t_(n+1)=(-1)^(n+1)binom(3n,n+1)"
        ),
    }


def literature_equivalence_certificate() -> dict:
    """Verify the sign/index conversion of OEIS A371813's recurrence."""
    # OEIS writes a(n)=(-1)^n S_n and, in its middle coefficient,
    # B(n)=1456n^4-6008n^3+8593n^2-4949n+960.
    oeis_middle = tuple(Fraction(value) for value in
                        (960, -4949, 8593, -6008, 1456))
    converted_middle = poly_scale(poly_shift_argument(oeis_middle, 2), 2)
    if converted_middle != tuple(Fraction(value) for value in P1):
        raise AssertionError(("OEIS middle coefficient", converted_middle, P1))

    # The other converted coefficients at OEIS index N=n+2 are exactly
    # -3(3n+1)(3n+2)Q(n+1) and 8(n+2)(2n+3)Q(n).
    factorization_certificate()
    return {
        "classification": "EXACT_SYMBOLIC_EQUIVALENCE",
        "reference": "https://oeis.org/A371813",
        "sequence_relation": "S_n=(-1)^n A371813(n)",
        "sum_reindexing": "OEIS k=n-j converts its defining sum to (-1)^n S_n",
        "gf_change": "A371813(-z)=G(z), with g(-z)=1/(1+X)",
        "recurrence_change": (
            "replace OEIS a(n) by (-1)^n S_n and then set its n=m+2; "
            "the three coefficients become P0(m),P1(m),P2(m)"
        ),
        "novelty_scope": (
            "independent exact proof and Route-1 application; no novelty "
            "claim for the sequence, algebraic generating function, or recurrence"
        ),
    }


def exact_replay(limit: int = 400) -> dict:
    values = [s_direct(index) for index in range(limit + 3)]
    rows = []
    for n_value in range(limit + 1):
        recurrence = (
            p_value(P0, n_value) * values[n_value]
            + p_value(P1, n_value) * values[n_value + 1]
            + p_value(P2, n_value) * values[n_value + 2]
        )
        if recurrence != 0:
            raise AssertionError((n_value, "recurrence", recurrence))
        u_value = Fraction(values[n_value + 1]) - Fraction(values[n_value], 4)
        if u_value != u_closed(n_value):
            raise AssertionError((n_value, "u formula", u_value, u_closed(n_value)))
        coupling_left = (
            2 * n_value * (2 * n_value + 1)
            * (4 * values[n_value + 1] - values[n_value])
        )
        coupling_right = (
            (28 * n_value * n_value + 25 * n_value + 5)
            * t_boundary(n_value)
        )
        if coupling_left != coupling_right:
            raise AssertionError((n_value, "boundary coupling"))
        rows.append((
            n_value,
            values[n_value],
            values[n_value + 1],
            u_value.numerator,
            u_value.denominator,
        ))
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "classification": "EXACT_FINITE_REGRESSION_OF_PROVED_IDENTITIES",
        "n_max": limit,
        "rows": len(rows),
        "initial_values": {"S_0": 1, "S_1": -1},
        "first_values": values[:12],
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for candidate in range(2, math.isqrt(limit) + 1):
        if not sieve[candidate]:
            continue
        start = candidate * candidate
        sieve[start:limit + 1:candidate] = b"\x00" * (
            (limit - start) // candidate + 1
        )
    return [value for value in range(2, limit + 1) if sieve[value]]


def row_lift_replay(prime_max: int = 2000) -> dict:
    """Finite regression for the proved same-row Frobenius/binomial lift."""
    s_values = [s_direct(index) for index in range((prime_max - 7) // 6 + 1)]
    rows = []
    for prime in primes_upto(prime_max):
        if prime < 13:
            continue
        for s_value in range(1, (prime - 7) // 6 + 1):
            numerator = prime - 6 * s_value - 3
            if numerator % 4:
                continue
            h_value = numerator // 4
            if h_value < 1:
                continue
            top = prime - 2 * s_value
            term = 1
            lifted = 1
            for index in range(1, s_value + 1):
                term = term * (top - index + 1) // index
                lifted += term
            residue = s_values[s_value] % prime
            if lifted % prime != residue:
                raise AssertionError((prime, h_value, s_value, lifted, residue))
            rows.append((prime, h_value, s_value, residue))
    if prime_max == 2000 and len(rows) != 22934:
        raise AssertionError(("actual row count", len(rows), 22934))
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "classification": "EXACT_FINITE_REGRESSION_OF_PROVED_CONGRUENCE",
        "prime_max": prime_max,
        "rows": len(rows),
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def dependency_certificate() -> dict:
    observed = {}
    for relative_name, expected in DEPENDENCIES.items():
        path = resolve_dependency(relative_name)
        actual = sha256_file(path)
        if actual != expected:
            raise AssertionError((relative_name, actual, expected))
        observed[relative_name] = actual
    return observed


def build_certificate() -> dict:
    dependencies = dependency_certificate()
    return {
        "item": 232,
        "definitions": {
            "S_n": "sum_(j=0)^n (-1)^j binom(2n+j-1,j), with S_0=1",
            "X": "the unique series X in z Q[[z]] satisfying X=z/(1+X)^2",
            "G": "sum_(n>=0) S_n z^n",
        },
        "generating_function_theorem": {
            "classification": "PROVED",
            "coefficient_diagonal": "S_n=[x^n](1-x)^(-1)(1+x)^(-2n)",
            "closed_form": "G=(1+X)/[(1-X)(1+3X)]",
        },
        "symbolic_operator_certificate": operator_symbolic_certificate(),
        "recurrence_theorem": {
            "classification": "PROVED",
            "range": "all integers n>=0",
            "identity": "P0(n)S_n+P1(n)S_(n+1)+P2(n)S_(n+2)=0",
            "P0_low_to_high": list(P0),
            "P1_low_to_high": list(P1),
            "P2_low_to_high": list(P2),
            "P2_nonzero_reason": "P2=8(n+2)(2n+3)(28n^2+25n+5)>0 for n>=0",
        },
        "ore_factorization_theorem": factorization_certificate(),
        "literature_equivalence": literature_equivalence_certificate(),
        "exact_replay": exact_replay(),
        "same_row_frobenius_theorem": {
            "classification": "PROVED",
            "row_relation": "p=6s+4h+3",
            "binomial_lift": (
                "S_s = sum_(k=0)^s binom(p-2s,k) "
                "= sum_(k=0)^s binom(4s+4h+3,k) (mod p)"
            ),
            "fixed_h_generating_function": (
                "A_h(z)=sum_(n>=0)[sum_(k=0)^n binom(4n+4h+3,k)]z^n "
                "=(1+Y)^(4h+4)/[(1-Y)(1-3Y)], Y=z(1+Y)^4"
            ),
            "neighbor_drift": (
                "A_h(s+r)=[x^(s+r)](1-x)^(-1)(1+x)^(-2(s+r))"
                "(1+x)^(6r) (mod p), for 0<=s+r<p"
            ),
            "cartier_scope": (
                "For s<p, Lambda_s(G)(0)=S_s merely extracts the moving "
                "base-p digit s; it does not descend to a smaller index."
            ),
        },
        "same_row_replay": row_lift_replay(),
        "item231_interface": {
            "classification": "SCOPED_INTERFACE_TO_SEPARATELY_CERTIFIED_ITEM231_IDENTITY",
            "high_partial_sum": (
                "T_(h,s)=sum_(j=r)^J t_j=S^((s))_J-S^((s))_(r-1), "
                "r=2h, J=3h+3s+1"
            ),
            "high_gosper_residual": "c_hi(h,s) T_(h,s) plus explicit t_r,t_J endpoints",
            "non_coupling_reason": (
                "Item232 shifts S_n=S^((n))_n, changing parameter and endpoint "
                "together; Item231's T_(h,s) changes only the endpoint at fixed s"
            ),
            "phase_coefficient_pattern": (
                "c_hi=c_h at s*=-(4h+3)/6 through h<=20 is Item231 "
                "EXACT_FINITE_ONLY evidence, not an Item232 theorem"
            ),
        },
        "item229_consequence": {
            "classification": "PROVED_SCOPED_REWRITE",
            "rewrite": (
                "Q(s)Theta_h(s)=[Q(s)c_h(s)-2s(2s+1)G_h(s)]S_s"
                "+8s(2s+1)G_h(s)S_(s+1)-2Q(s)Delta_minus(h,s)"
            ),
            "scope_warning": (
                "This introduces S_(s+1). A collision at s does not imply a "
                "collision or Theta_h(s+1)=0 at the adjacent index. Modulo p, "
                "division by Q(s) additionally requires Q(s) to be a unit."
            ),
        },
        "classification": {
            "PROVED": [
                "the formal diagonal and algebraic generating-function identity",
                "the polynomial recurrence for every n>=0",
                "the Ore factorization and hypergeometric first difference",
                "the exact coupling of S_n to Item 229's boundary term",
                "the denominator-free Item 229 rewrite",
                "the same-row Frobenius/binomial lift and its fixed-h algebraic series",
                "the exact sign/index equivalence with OEIS A371813",
            ],
            "EXACT_FINITE_ONLY": [
                "the coefficient regression through n<=400 (proof-independent)",
                "the same-row congruence replay through p<=2000",
            ],
            "OPEN": [
                "a second same-row condition controlling S_(s+1)",
                "a universal unit theorem for Q(s) on relevant row primes",
                "a uniform Cartier state or scalar phase formula for the moving digit s",
                "control of Item231's fixed-parameter high partial sum T_(h,s)",
                "an all-prime exclusion, density estimate, or positive Route-1 rate",
            ],
        },
        "rate_ledger": {
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "reason": (
                "the recurrence relates adjacent sequence values but supplies no "
                "adjacent collision condition"
            ),
        },
        "dependency_sha256": dependencies,
        "runtime": {"external_numeric_backend": None},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=default_output())
    arguments = parser.parse_args()
    certificate = build_certificate()
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
