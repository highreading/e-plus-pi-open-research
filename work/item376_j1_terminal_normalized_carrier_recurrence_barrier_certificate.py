#!/usr/bin/env python3
"""Deterministic exact replay for Item 376.

The checker verifies the terminal-normalized reverse sums, their minimal
integer clearing and primitive numerator carriers, the 3-adic unit
normalization, actual-prime denominator units, and the order-one 3-free
comparison used in the scoped recurrence-height barrier.

There is no prime scan, collision census, or recurrence extrapolation.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = (
    HERE / "item376_j1_terminal_normalized_carrier_recurrence_barrier_certificate.json"
)

DEPENDENCIES = {
    "sources/item364_j1_saturation_boundary_phase_carrier_report.md":
        "2c18f6ac22220e553349e44a723e200d20f4f3c89cfec5cd83812db260834e92",
    "scripts/item364_j1_saturation_boundary_phase_carrier_certificate.py":
        "ef9046fc4d7071779a73bf6e1bfd7d312789b994bd3274eec2a78d818d027b07",
    "results/item364_j1_saturation_boundary_phase_carrier_certificate.json":
        "ca1987d1688789dbf0e64f3eec2c4b771b9873f829e61d1b5f62302f47443926",
    "results/item364_j1_saturation_boundary_phase_carrier_root_audit.json":
        "fa6170a0c014cee655ba00c5288905344a969aa22b141d44b64ae4a2d3219a89",
    "results/item364_j1_saturation_boundary_phase_carrier_ledger_delta.json":
        "225840be16db3950187672d556065553017b1a76f65641a2c82b67c9227f914f",
    "manifests/item364_j1_saturation_boundary_phase_carrier_manifest.json":
        "bd0c5435fe4d0b7266d81b4f97dfacf8b2fca55fb2c95770e7cb853c2f77426c",
    "sources/item368_j1_boundary_whipple_rank_obstruction_report.md":
        "34bfdc2b2e4035ae78c0147d0a22f442e7f0fd148103e5eeee44d62042768cc6",
    "scripts/item368_j1_boundary_whipple_rank_obstruction_certificate.py":
        "f9d72b05fd24d62aa58fbca72221ff246a4d270b1eefb9023351cfd1aff932c5",
    "results/item368_j1_boundary_whipple_rank_obstruction_certificate.json":
        "8814c95cca55bf80b735668813909ed7e0f85ff30a1926a0df4b5b0c6f3c396d",
    "results/item368_j1_boundary_whipple_rank_obstruction_root_audit.json":
        "f20929fc3aa756419cf4263b439d90e6c44084c63f9acf64a4540134e3198321",
    "results/item368_j1_boundary_whipple_rank_obstruction_ledger_delta.json":
        "30a39fc4bdb919d53864a3f56f180dfe95dcb98dd58ffc87b9185fceeeb33bc8",
    "manifests/item368_j1_boundary_whipple_rank_obstruction_manifest.json":
        "eec70fc17c33e4ec7d3f8851a423debcca5abb333bbbe58decd3ab14736fd11a",
    "sources/item372_j1_boundary_exact_zero_strata_report.md":
        "70908ecaac3940afbadc9abe752b904972c17b20058782d0b10840c0da245e11",
    "scripts/item372_j1_boundary_exact_zero_strata_certificate.py":
        "6c05f7446a246c4efe91cda75f2c6e7f315f267a7a75110fa6ce542b87c6cb5e",
    "results/item372_j1_boundary_exact_zero_strata_certificate.json":
        "22521478fac4e39d00c071c679b5e2bb34543ae4232e4cc196c9fd6e44e9fbd5",
    "results/item372_j1_boundary_exact_zero_strata_root_audit.json":
        "fbfda454f9ba31c2bc6af23fdf868fdcc16edfe628c21e4f6905d6cce0b334c7",
    "results/item372_j1_boundary_exact_zero_strata_ledger_delta.json":
        "5481ddd7e9cd38afa7f746984371b0b8f3088ef0fbabbdade866be796fc12398",
    "manifests/item372_j1_boundary_exact_zero_strata_manifest.json":
        "2cd8c4a7f8902e2decbfd4848b443e9672abe3dfcf85ae99696e6ca8f04effd8",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise AssertionError((relative, expected, actual))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


verify_dependencies()
ITEM364 = load_module(
    "item376_pinned_item364",
    ROOT / "scripts/item364_j1_saturation_boundary_phase_carrier_certificate.py",
)


def pochhammer(value: Fraction, length: int) -> Fraction:
    answer = Fraction(1)
    for offset in range(length):
        answer *= value + offset
    return answer


def product(values) -> int:
    answer = 1
    for value in values:
        answer *= value
    return answer


def terminal_normalizations(h_value: int) -> tuple[Fraction, Fraction]:
    sigma = Fraction(-(4 * h_value + 3), 6)
    terminal_x = (
        ((-1) ** h_value)
        * pochhammer(sigma + 1, h_value)
        / pochhammer(3 * sigma + 2, h_value)
    )
    n_value = h_value + 2
    terminal_u = (
        ((-1) ** n_value)
        * pochhammer(sigma, n_value)
        / pochhammer(3 * sigma, n_value)
    )
    return terminal_x, terminal_u


def reverse_sum(
    kernel: list[int],
    h_value: int,
    terminal: int,
    c_value: Fraction,
) -> Fraction:
    answer = Fraction(0)
    for r_value in range(terminal + 1):
        answer += (
            ((-1) ** r_value)
            * kernel[2 * r_value]
            * pochhammer(Fraction(2 * h_value + 1, 2), r_value)
            / pochhammer(c_value, r_value)
        )
    return answer


def odd_step_product(h_value: int, length: int) -> int:
    return product(2 * h_value + 1 + 2 * offset for offset in range(length))


def cleared_pair(
    kernel: list[int],
    h_value: int,
    terminal: int,
    tail_constant: int,
) -> tuple[int, int]:
    """Return A,D with normalized value A/D.

    tail_constant is 3 for x and -3 for u:
      D=prod_(j=0)^(terminal-1)(tail_constant-2h+6j).
    """
    denominator = product(
        tail_constant - 2 * h_value + 6 * j_value
        for j_value in range(terminal)
    )
    numerator = 0
    for r_value in range(terminal + 1):
        tail = product(
            tail_constant - 2 * h_value + 6 * j_value
            for j_value in range(r_value, terminal)
        )
        numerator += (
            ((-1) ** r_value)
            * kernel[2 * r_value]
            * (3**r_value)
            * odd_step_product(h_value, r_value)
            * tail
        )
    return numerator, denominator


def primitive_record(numerator: int, denominator: int) -> dict[str, int]:
    common = math.gcd(abs(numerator), abs(denominator))
    primitive_numerator = numerator // common
    primitive_denominator = denominator // common
    if primitive_denominator < 0:
        primitive_numerator = -primitive_numerator
        primitive_denominator = -primitive_denominator
    if math.gcd(abs(primitive_numerator), primitive_denominator) != 1:
        raise AssertionError("primitive reduction")
    return {
        "cleared_numerator": numerator,
        "cleared_denominator": denominator,
        "gcd": common,
        "primitive_numerator": primitive_numerator,
        "primitive_denominator": primitive_denominator,
    }


def fraction_mod(value: Fraction, prime: int) -> int:
    if value.denominator % prime == 0:
        raise ZeroDivisionError((value, prime))
    return value.numerator * pow(value.denominator, -1, prime) % prime


def normalized_carrier_replay() -> dict[str, Any]:
    controls = (1, 2, 4, 5, 7, 8, 10, 11)
    rows = []
    for h_value in controls:
        if h_value % 3 == 0:
            raise AssertionError((h_value, "composite ray"))
        kernel_0 = ITEM364.ITEM218.kernel_integer(h_value, 1)
        kernel_1 = ITEM364.ITEM218.kernel_integer(h_value, 4)
        x_phase, _, u_phase, _ = ITEM364.phase_values(h_value)
        terminal_x, terminal_u = terminal_normalizations(h_value)
        normalized_x = x_phase / terminal_x
        normalized_u = u_phase / terminal_u

        reverse_x = reverse_sum(
            kernel_0,
            h_value,
            h_value,
            Fraction(1, 2) - Fraction(h_value, 3),
        )
        reverse_u = reverse_sum(
            kernel_1,
            h_value,
            h_value + 2,
            -Fraction(1, 2) - Fraction(h_value, 3),
        )
        if reverse_x != normalized_x or reverse_u != normalized_u:
            raise AssertionError((h_value, "reverse sum"))

        ax, dx = cleared_pair(kernel_0, h_value, h_value, 3)
        au, du = cleared_pair(kernel_1, h_value, h_value + 2, -3)
        if Fraction(ax, dx) != normalized_x or Fraction(au, du) != normalized_u:
            raise AssertionError((h_value, "integer clearing"))
        if ax % 3 != dx % 3 or au % 3 != du % 3:
            raise AssertionError((h_value, "1 mod 3 quotient"))
        if ax % 3 == 0 or dx % 3 == 0 or au % 3 == 0 or du % 3 == 0:
            raise AssertionError((h_value, "3-adic unit"))

        primitive_x = primitive_record(ax, dx)
        primitive_u = primitive_record(au, du)
        if primitive_x["primitive_numerator"] % 3 == 0:
            raise AssertionError((h_value, "primitive X numerator divisible by 3"))
        if primitive_u["primitive_numerator"] % 3 == 0:
            raise AssertionError((h_value, "primitive U numerator divisible by 3"))

        max_dx = max(abs(3 - 2 * h_value + 6 * j) for j in range(h_value))
        max_du = max(
            abs(-3 - 2 * h_value + 6 * j) for j in range(h_value + 2)
        )
        if max_dx > 4 * h_value + 3 or max_du > 4 * h_value + 3:
            raise AssertionError((h_value, max_dx, max_du, "denominator bound"))

        rows.append(
            {
                "h": h_value,
                "normalized_x": {
                    "numerator": normalized_x.numerator,
                    "denominator": normalized_x.denominator,
                },
                "normalized_u": {
                    "numerator": normalized_u.numerator,
                    "denominator": normalized_u.denominator,
                },
                "primitive_x": primitive_x,
                "primitive_u": primitive_u,
                "maximum_X_cleared_denominator_factor": max_dx,
                "maximum_U_cleared_denominator_factor": max_du,
            }
        )

    return {
        "classification": "EXACT PREDECLARED SYMBOLIC CONTROLS; NO PRIME SCAN",
        "rows": rows,
        "reverse_sums": {
            "x": (
                "sum_(r=0)^h (-1)^r*k0_(2r)*(h+1/2)_r/(1/2-h/3)_r"
            ),
            "u": (
                "sum_(r=0)^(h+2) (-1)^r*k1_(2r)*(h+1/2)_r/(-1/2-h/3)_r"
            ),
        },
        "clearing": {
            "D_x": "product_(j=0)^(h-1)(3-2h+6j)",
            "D_u": "product_(j=0)^(h+1)(-3-2h+6j)",
            "A_congruence": "A_x=D_x mod 3 and A_u=D_u mod 3, both nonzero",
            "minimal": "divide A,D by their exact integer gcd and normalize denominator positive",
        },
        "actual_prime_bridge": (
            "all primitive denominators and both terminal normalizers are p-units for "
            "p>=4h+9; X=0 mod p iff p divides N_x, and U=0 mod p iff p divides N_u"
        ),
    }


def actual_prime_bridge_replay() -> dict[str, Any]:
    controls = (
        (1, 1, 13),
        (2, 1, 17),
        (4, 4, 43),
        (8, 2, 47),
    )
    rows = []
    for h_value, s_value, prime in controls:
        if prime != 4 * h_value + 6 * s_value + 3:
            raise AssertionError((h_value, s_value, prime, "tie"))
        if not ITEM364.ITEM218.is_prime(prime):
            raise AssertionError((prime, "not prime"))
        kernel_0 = ITEM364.ITEM218.kernel_integer(h_value, 1)
        kernel_1 = ITEM364.ITEM218.kernel_integer(h_value, 4)
        x_phase, _, u_phase, _ = ITEM364.phase_values(h_value)
        terminal_x, terminal_u = terminal_normalizations(h_value)
        ax, dx = cleared_pair(kernel_0, h_value, h_value, 3)
        au, du = cleared_pair(kernel_1, h_value, h_value + 2, -3)
        primitive_x = primitive_record(ax, dx)
        primitive_u = primitive_record(au, du)
        if dx % prime == 0 or du % prime == 0:
            raise AssertionError((prime, "cleared denominator"))
        if fraction_mod(x_phase / terminal_x, prime) != (
            primitive_x["primitive_numerator"]
            * pow(primitive_x["primitive_denominator"], -1, prime)
        ) % prime:
            raise AssertionError((prime, "X bridge"))
        if fraction_mod(u_phase / terminal_u, prime) != (
            primitive_u["primitive_numerator"]
            * pow(primitive_u["primitive_denominator"], -1, prime)
        ) % prime:
            raise AssertionError((prime, "U bridge"))
        rows.append({"h": h_value, "s": s_value, "p": prime})
    return {
        "classification": "EXACT PREDECLARED ACTUAL-ROW CONTROLS; NO SCAN",
        "rows": rows,
        "theorem": (
            "B_xy implies p|N_x(h), and B_uv implies p|N_u(h); these are "
            "one-coordinate overcarriers and need not be as sharp as the paired gcd carriers"
        ),
    }


def three_free_product(h_value: int) -> int:
    return product(
        value
        for value in range(4 * h_value + 1, 18 * h_value + 1)
        if value % 3
    )


def comparison_replay() -> dict[str, Any]:
    recurrence_controls = (1, 2, 4, 5, 7, 8)
    recurrences = []
    for h_value in recurrence_controls:
        base = three_free_product(h_value)
        shifted = three_free_product(h_value + 3)
        numerator = product(
            value
            for value in range(18 * h_value + 1, 18 * h_value + 55)
            if value % 3
        )
        denominator = product(
            value
            for value in range(4 * h_value + 1, 4 * h_value + 13)
            if value % 3
        )
        if shifted * denominator != base * numerator:
            raise AssertionError((h_value, "3-free recurrence"))
        comparison = base * base
        if comparison % 3 != 1:
            raise AssertionError((h_value, "comparison is not 1 mod 3"))
        recurrences.append(
            {
                "h": h_value,
                "numerator_factor_count": 36,
                "denominator_factor_count": 8,
                "comparison_mod_3": comparison % 3,
            }
        )

    actual_controls = (
        (12, 2, 1, 17),
        (34, 8, 2, 47),
        (30, 4, 4, 43),
    )
    actual_rows = []
    for m_value, h_value, s_value, prime in actual_controls:
        if m_value != 3 * h_value + 4 * s_value + 2:
            raise AssertionError((m_value, h_value, s_value, "M tie"))
        if prime != 4 * h_value + 6 * s_value + 3:
            raise AssertionError((prime, h_value, s_value, "p tie"))
        if 12 * h_value < m_value:
            raise AssertionError((m_value, h_value, "comparison bulk"))
        if not (4 * h_value + 3 < prime < 18 * h_value):
            raise AssertionError((prime, h_value, "factor interval"))
        comparison = three_free_product(h_value) ** 2
        if comparison % prime:
            raise AssertionError((prime, h_value, "comparison divisibility"))
        if comparison % 3 != 1:
            raise AssertionError((h_value, "comparison unit"))
        actual_rows.append({"M": m_value, "h": h_value, "s": s_value, "p": prime})

    return {
        "classification": "EXACT PREDECLARED COMPARISON CONTROLS",
        "carrier": "C_h=(product_(4h<k<=18h, 3 does not divide k) k)^2",
        "unit": "C_h is an integer congruent to 1 mod 3",
        "recurrence": (
            "on each h mod 3 class, E_h^2*C_(h+3)=N_h^2*C_h with E_h and "
            "N_h fixed products of 8 and 36 integer-linear factors"
        ),
        "height": "log C_h=O(h log(h+2))",
        "positive_rate_bulk": (
            "every actual p on M/12<=h<=M/3 divides C_h; mass M/8+o(M), "
            "capacity 1/48 per 6M"
        ),
        "recurrence_controls": recurrences,
        "actual_controls": actual_rows,
        "scope": (
            "3-adic normalization, primitive integrality, fixed-order recurrence, and "
            "pointwise height alone cannot force selector-weighted zero density"
        ),
    }


def capacity_replay() -> dict[str, Any]:
    if Fraction(1, 6) / 6 != Fraction(1, 36):
        raise AssertionError("fixed-j1 normalization")
    if Fraction(1, 8) / 6 != Fraction(1, 48):
        raise AssertionError("comparison normalization")
    return {
        "raw_fixed_j1_mass_per_M": "1/6",
        "shared_full_fixed_j1_ceiling_per_6M": "1/36",
        "comparison_mass_per_M": "1/8",
        "comparison_capacity_per_6M": "1/48",
        "new_booking": 0,
        "new_capacity_reduction": 0,
    }


def build_result() -> dict[str, Any]:
    return {
        "item": 376,
        "schema": "item376-j1-terminal-normalized-carrier-recurrence-barrier-v1",
        "classification": "PROVED_TERMINAL_NORMALIZED_CARRIERS_AND_SCOPED_RECURRENCE_BARRIER",
        "dependencies": DEPENDENCIES,
        "dependency_hashes_verified": True,
        "normalized_carrier_replay": normalized_carrier_replay(),
        "actual_prime_bridge_replay": actual_prime_bridge_replay(),
        "comparison_replay": comparison_replay(),
        "holonomic_scope": {
            "proved": (
                "on each h mod 3 class, the unreduced cleared sums are finite sums of "
                "proper hypergeometric terms and therefore admit some fixed-order "
                "polynomial recurrence by creative telescoping"
            ),
            "not_proved": (
                "the primitive numerators after division by gcd(A_h,D_h) satisfy a "
                "fixed-order recurrence; primitive reduction is nonlinear"
            ),
            "moving_modulus_barrier": (
                "a recurrence at fixed modulus does not couple actual fixed-M events, "
                "because consecutive actual fixed-M parameters have h->h+4 and the "
                "selected modulus changes from p_h to p_h-2"
            ),
        },
        "capacity_replay": capacity_replay(),
        "strict_labels": {
            "proved": [
                "exact reverse terminal-normalized sums for x_h and u_h",
                "exact minimal integer clearing by primitive gcd reduction",
                "x_h and u_h lie in 1+3Z_3",
                "actual-prime p-unit denominator bridge to primitive numerator overcarriers",
                "holonomicity of the unreduced proper-hypergeometric sums on each residue class",
                "scoped no-go for generic recurrence/unit/height/selector reasoning",
                "zero booking and zero capacity reduction",
            ],
            "finite_only": [
                "eight declared normalized controls, four actual-row controls, six recurrence controls, and three comparison controls",
                "no prime scan, collision census, recurrence guess promotion, or extrapolation",
            ],
            "open": [
                "fixed-order recurrence for the primitive reduced numerator sequences",
                "target-specific cross-prime average gcd or weighted zero density",
                "any strict fixed-j1 capacity reduction",
            ],
        },
        "scope_warning": (
            "The normalized values are nonzero 3-adic units in characteristic zero, "
            "but their primitive numerators may still vanish modulo an actual tied prime. "
            "The one-coordinate carriers overcount the paired boundary gates."
        ),
        "verdict": (
            "Terminal normalization gives exact primitive one-coordinate carriers and "
            "holonomic unreduced sums, but fixed-order recurrence, 3-adic unit structure, "
            "and pointwise height cannot control the moving selector primes; no mass changes."
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_result()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "classification": result["classification"],
                "new_booking": result["capacity_replay"]["new_booking"],
                "new_capacity_reduction": result["capacity_replay"]["new_capacity_reduction"],
                "verdict": result["verdict"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
