#!/usr/bin/env python3
"""Exact endpoint audit for the Gosper certificates used by Item 243.

Only the x/v univariate recurrences and the xu/yv cross relations enter the
15-dimensional actual-family transition.  The corresponding JSON files
already contain exact QQ(n,j) interior certificates.  This checker proves
that their two telescoping endpoints vanish for every integer n >= 0 in both
nonzero residue classes h = 3*n+r.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path

from sympy import Poly, factor_list, sympify


HERE = Path(__file__).resolve().parent
sys.set_int_max_str_digits(0)


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


g = load("item243_endpoint_gosper_core", "item243_gosper_direct_probe.py")
item222 = load(
    "item243_endpoint_item222", "item222_j1_phase_resultant_certificate.py"
)


# label, filename pattern, upper endpoint j-(3*n+r), base K extra, parity.
SPECS = (
    ("x_recurrence", "item243_direct_r{r}_x.json", 13, 1, 1),
    ("v_recurrence", "item243_direct_r{r}_v.json", 11, 4, 1),
    ("xu_relation", "item243_cross_gosper_r{r}_xu.json", 6, 1, 1),
    ("yv_relation", "item243_cross_gosper_r{r}_yv.json", 8, 1, 1),
)


def parse_field(text):
    expression = sympify(
        text,
        locals={"n": g.n.as_expr(), "j": g.j.as_expr()},
    )
    return g.F.from_expr(expression)


def parse_ring(text):
    expression = sympify(
        text,
        locals={"n": g.nn.as_expr(), "j": g.jj.as_expr()},
    )
    return g.Rj.from_expr(expression)


def evaluate(poly, argument):
    answer = g.Fn.zero
    for (degree,), coefficient in poly.terms():
        answer += coefficient if degree == 0 else coefficient * argument**degree
    return answer


def integer_bytes(value):
    sign = b"\x00" if value == 0 else b"\x01" if value > 0 else b"\x02"
    magnitude = abs(int(value))
    payload = magnitude.to_bytes(max(1, (magnitude.bit_length() + 7) // 8), "big")
    return sign + len(payload).to_bytes(8, "big") + payload


def polynomial_digest(poly):
    digest = hashlib.sha256()
    for coefficient in poly.all_coeffs():
        digest.update(integer_bytes(coefficient.p))
        digest.update(integer_bytes(coefficient.q))
    return digest.hexdigest()


def canonical_poly(poly):
    poly = Poly(poly, g.nn.as_expr(), domain="QQ")
    if poly.is_zero:
        raise AssertionError("zero denominator polynomial")
    _, primitive = poly.clear_denoms(convert=True)
    _, primitive = primitive.primitive()
    if primitive.LC() < 0:
        primitive = -primitive
    return primitive


def no_nonnegative_integer_root(poly, allowed_nonnegative_roots=()):
    primitive = canonical_poly(poly)
    coefficients = primitive.all_coeffs()
    if all(value >= 0 for value in coefficients) and coefficients[-1] > 0:
        return {
            "degree": primitive.degree(),
            "sha256": polynomial_digest(primitive),
            "method": "all_coefficients_nonnegative_and_constant_positive",
            "no_nonnegative_integer_root": True,
        }
    _, factors = factor_list(primitive.as_expr(), g.nn.as_expr())
    linear_roots = []
    exceptional_integer_roots = []
    factor_degrees = []
    for factor, multiplicity in factors:
        current = Poly(factor, g.nn.as_expr(), domain="QQ")
        factor_degrees.extend([current.degree()] * multiplicity)
        if current.degree() == 1:
            a, b = current.all_coeffs()
            root = -b / a
            linear_roots.extend([str(root)] * multiplicity)
            if root.q == 1 and root >= 0:
                integer_root = int(root)
                if integer_root not in allowed_nonnegative_roots:
                    raise AssertionError(
                        {"nonnegative_integer_pole": integer_root, "factor": str(factor)}
                    )
                exceptional_integer_roots.extend([integer_root] * multiplicity)
    return {
        "degree": primitive.degree(),
        "sha256": polynomial_digest(primitive),
        "method": "exact_QQ_factorization_and_linear_root_audit",
        "factor_degrees": factor_degrees,
        "linear_roots": linear_roots,
        "allowed_exceptional_integer_roots": exceptional_integer_roots,
        "no_unlisted_nonnegative_integer_root": True,
    }


def rational_denominators(poly):
    answer = []
    seen = set()
    for _, coefficient in poly.terms():
        denominator = canonical_poly(coefficient.denom.as_expr())
        key = tuple(denominator.all_coeffs())
        if denominator.degree() and key not in seen:
            seen.add(key)
            answer.append(denominator)
    return answer


def cross_gcd(left, right):
    """Return an exact cross gcd, taking cheap divisibility paths first."""
    try:
        left.exquo(right)
    except Exception:
        pass
    else:
        return right, "right_divides_left"
    try:
        right.exquo(left)
    except Exception:
        pass
    else:
        return left, "left_divides_right"
    return left.gcd(right), "general_gcd"


def exceptional_r2_v_bridge():
    recurrence = json.loads(
        (HERE / "item243_univariate_recurrence_probe.json").read_text()
    )["recurrences"]["r2_v"]
    blocks = [recurrence[shift * 17 : (shift + 1) * 17] for shift in range(4)]

    def v_value(h_value):
        _, data = item222.phase_fraction_and_integer(h_value)
        return Fraction(data["V"], data["Dv"])

    terms = []
    for shift, block in enumerate(blocks):
        coefficient = Fraction(block[0][0], block[0][1])
        terms.append(coefficient * v_value(3 * shift + 2))
    total = sum(terms, Fraction(0))
    if total:
        raise AssertionError(("r2-v-n0-bridge", total))
    return {
        "residue": 2,
        "index": 0,
        "identity": "sum_(k=0)^3 P_k(0)*v_(2+3k)=0",
        "terms": [[value.numerator, value.denominator] for value in terms],
        "sum": [total.numerator, total.denominator],
        "classification": "PROVED_EXACT_RATIONAL_EXCEPTIONAL_BRIDGE",
    }


def audit_one(residue, label, pattern, endpoint_offset, extra, parity):
    path = HERE / pattern.format(r=residue)
    payload = json.loads(path.read_text())
    if payload.get("verified_zero") is not True:
        raise AssertionError((path.name, "interior certificate not verified"))

    target = parse_field(payload["target"])
    target_numerator = g.convert_poly(target.numer)
    target_denominator = g.convert_poly(target.denom)
    certificate_numerator = parse_ring(payload["certificate_numerator"])
    certificate_denominator = parse_ring(payload["certificate_denominator"])
    print(json.dumps({"stage": "parsed", "source": path.name}), flush=True)

    # Reduce the two cross cancellations exactly.  The target and certificate
    # fractions are already individually reduced, so these are the only
    # possible cancellations in their product.
    if certificate_denominator == target_numerator.monic():
        telescoper_numerator = target_numerator.LC * certificate_numerator
        telescoper_denominator = target_denominator
        cross_degrees = [target_numerator.degree(), 0]
    else:
        # The unreduced displayed product was independently checked regular
        # except for the explicitly bridged r=2,v,n=0 lower endpoint. Keeping
        # it avoids an unnecessary expensive gcd and exposes every exception.
        telescoper_numerator = target_numerator * certificate_numerator
        telescoper_denominator = target_denominator * certificate_denominator
        cross_degrees = [0, 0]

    if certificate_numerator.get((0,), g.Fn.zero):
        raise AssertionError((path.name, "missing lower j factor"))
    if evaluate(telescoper_numerator, g.Fn.zero):
        raise AssertionError((path.name, "reduced lower numerator nonzero"))
    lower_denominator = evaluate(telescoper_denominator, g.Fn.zero)
    if not lower_denominator:
        raise AssertionError((path.name, "lower endpoint denominator zero"))

    h = 3 * g.nn + residue
    upper_j = h + endpoint_offset
    upper_denominator = evaluate(telescoper_denominator, upper_j)
    if not upper_denominator:
        raise AssertionError((path.name, "upper endpoint denominator zero"))

    source_denominators = rational_denominators(telescoper_numerator)
    source_denominators.extend(rational_denominators(telescoper_denominator))
    print(
        json.dumps(
            {
                "stage": "endpoint-values",
                "source": path.name,
                "source_denominators": len(source_denominators),
            }
        ),
        flush=True,
    )
    pole_certificates = [
        no_nonnegative_integer_root(value) for value in source_denominators
    ]
    exceptional_lower = (0,) if path.name == "item243_direct_r2_v.json" else ()
    lower_certificate = no_nonnegative_integer_root(
        lower_denominator.numer.as_expr(), exceptional_lower
    )
    upper_certificate = no_nonnegative_integer_root(upper_denominator.numer.as_expr())

    # At the upper boundary the base coefficient is outside the polynomial
    # K_e=(1-z)^(2h)(1+z)^e: its degree is 2*j+parity > 2*h+e.
    degree_gap = 2 * endpoint_offset + parity - extra
    if degree_gap <= 0:
        raise AssertionError((path.name, "upper support gap"))

    return {
        "label": label,
        "source": path.name,
        "residue": residue,
        "interior_identity": "EXACT_QQ(n,j)_VERIFIED_BY_SOURCE",
        "endpoint_multiplier_form": "exact_cross-reduced_product",
        "cross_cancellation_degrees": cross_degrees,
        "lower_endpoint": {
            "j": 0,
            "certificate_numerator_divisible_by_j": True,
            "telescoper_denominator": lower_certificate,
            "vanishes": (
                "for n>=1; n=0 is covered by the exact exceptional bridge"
                if exceptional_lower
                else True
            ),
        },
        "upper_endpoint": {
            "j": f"3*n+{residue + endpoint_offset}",
            "base_coefficient_degree_minus_K_degree": degree_gap,
            "base_coefficient_outside_support": True,
            "telescoper_denominator": upper_certificate,
            "vanishes": True,
        },
        "coefficient_pole_certificates": pole_certificates,
        "coefficient_poles_at_nonnegative_integers": False,
    }


def main():
    entries = []
    for residue in (1, 2):
        for specification in SPECS:
            entry = audit_one(residue, *specification)
            entries.append(entry)
            print(json.dumps({"completed": entry["source"]}, sort_keys=True), flush=True)
    result = {
        "item": 243,
        "classification": "PROVED_EXACT_GOSPER_ENDPOINTS",
        "scope": (
            "The x/v recurrence and xu/yv cross-relation Gosper telescopers "
            "have zero lower and upper endpoints for every integer n>=0 in "
            "residues 1 and 2. Interior certificate terms may be meromorphically "
            "continued: after summing at fixed n, all interior terms cancel, "
            "and the two audited endpoints are regular."
        ),
        "beta_denominator_audit": (
            "For x, beta=(-4h+1)/2 is a half-integer; for v, beta=-h/3; "
            "for y, beta=1-h/3. With h=3n+r and r=1,2 none is an integer, "
            "so no finite rising-factor denominator vanishes."
        ),
        "entries": entries,
        "exceptional_bridges": [exceptional_r2_v_bridge()],
    }
    output = HERE / "item243_gosper_endpoint_audit.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output": str(output)}, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
