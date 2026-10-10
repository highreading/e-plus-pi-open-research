#!/usr/bin/env python3
"""Exact replay for the adjacent joint-output thin-strip obstruction.

The replay checks the algebraic identities, Gaussian-power residue table,
primitive-normal normalization, factorial cancellation, and rigorous rational
constant comparisons used in the source.  Numerical integral rows only
illustrate asymptotic scales; the source contains the all-parameter proofs.
"""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/common_kernel_adjacent_joint_output_thin_strip_no_go.md"
OUTPUT = ROOT / "results/common_kernel_adjacent_joint_output_thin_strip_certificate.json"
RSS_GUARD_KIB = 40 * 1024 * 1024

DEPENDENCIES = {
    "results/common_kernel_native_sign_output_range_sharp_width_hashes.sha256":
        "de1348caca545595e79ddc00929ece5d0ef7f18fb7eeb3f979beb26f2b766677",
    "results/common_kernel_finite_multimoment_exact_approximation_hashes.sha256":
        "b53b8e6f1855fe3eb7ef1b1eae1c303fad3b9cd5344462616606794fd0d9ce6d",
}

t = sp.symbols("t", real=True)


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


def gaussian_power(n: int) -> tuple[int, int]:
    """Return exact R,I with (1-i)^n=R+iI."""
    real, imag = 1, 0
    for _ in range(n):
        real, imag = real + imag, imag - real
    return real, imag


def native_parameters(n: int) -> tuple[int, int, int, int]:
    real, imag = gaussian_power(n)
    numerator = math.factorial(n) - real
    assert numerator % 2 == 0
    a = -imag
    b = numerator // 2
    return real, imag, a, b


def symbolic_kernel_checks() -> dict[str, object]:
    a_n, b_n, a_m, b_m, d_h = sp.symbols(
        "a_n b_n a_m b_m d_h", nonzero=True,
    )
    eps_n = a_n / b_n
    eps_m = a_m / b_m
    q = b_n / b_m
    common = t * sp.exp(-t) * d_h
    d_g_n = common * (a_n + b_n * t)
    d_g_m = common * (a_m + b_m * t)
    thin = sp.simplify(d_g_n - q * d_g_m)
    expected_thin = b_n * (eps_n - eps_m) * t * sp.exp(-t) * d_h
    assert sp.simplify(thin - expected_thin) == 0

    late = sp.simplify(q * (eps_n - eps_m) * d_g_m / (t + eps_m))
    assert sp.simplify(thin - late) == 0

    r = sp.Function("R")(t)
    w_n = sp.exp(-t) * t ** sp.Symbol("N", integer=True, positive=True)
    # The adjacent baseline factor is checked with a concrete symbolic N.
    n = sp.symbols("n", integer=True, positive=True)
    baseline = sp.exp(-t) * (t**n - t ** (n + 1))
    expected_baseline = sp.exp(-t) * t**n * (1 - t)
    assert sp.simplify(baseline - expected_baseline) == 0

    v = t**2 - 2 * t + 2
    response = sp.E + 4 * sp.exp(t) / v
    response_prime = sp.factor(sp.diff(response, t))
    expected_prime = 4 * sp.exp(t) * (2 - t) ** 2 / v**2
    assert sp.simplify(response_prime - expected_prime) == 0
    assert sp.simplify(response.subs(t, 0) - (sp.E + 2)) == 0
    assert sp.simplify(response.subs(t, 1) - 5 * sp.E) == 0

    l_n, l_m = sp.symbols("L_N L_M")
    thin_coordinate = l_n - q * l_m
    assert sp.simplify(l_n - (q * l_m + thin_coordinate)) == 0

    return {
        "thin_identity": str(thin),
        "late_identity_difference": "0",
        "adjacent_baseline_factor": str(expected_baseline),
        "response_derivative": str(response_prime),
        "response_endpoints": ["e+2", "5e"],
        "coordinate_recovery_difference": "0",
        "response_bound_ledger": [
            "exp(t)<=e on [0,1]",
            "(2-t)^2<=4 on [0,1]",
            "(t^2-2t+2)^2>=1 on [0,1]",
            "therefore 0<R'(t)<=16e",
        ],
    }


def gaussian_residue_checks() -> dict[str, object]:
    base = []
    for residue in range(8):
        real, imag = gaussian_power(residue)
        base.append({
            "residue": residue,
            "R_residue": real,
            "I_residue": imag,
            "a_residue": -imag,
        })

    # (1-i)^(8k+r)=16^k(1-i)^r, so these base rows are the
    # all-parameter residue table, not a finite extrapolation.
    r8, i8 = gaussian_power(8)
    assert (r8, i8) == (16, 0)
    monotone_residues = []
    for residue in [0, 1, 2]:
        _, imag_0 = gaussian_power(residue)
        _, imag_1 = gaussian_power(residue + 1)
        assert -imag_1 >= -imag_0
        monotone_residues.append({
            "N_mod_8": residue,
            "a_N_scale": -imag_0,
            "a_N_plus_1_scale": -imag_1,
        })
    _, imag_3 = gaussian_power(3)
    _, imag_4 = gaussian_power(4)
    assert -imag_4 < -imag_3

    finite_b_rows = []
    for n in range(2, 257):
        real, imag, a, b = native_parameters(n)
        real_next, imag_next, a_next, b_next = native_parameters(n + 1)
        assert b > 0 and b_next > b
        assert 2 * b_next >= 7 * b
        ratio_ledger = 2 * (2 * b_next - 7 * b)
        expected_ratio_ledger = (
            (2 * n - 5) * math.factorial(n) + 7 * real - 2 * real_next
        )
        assert ratio_ledger == expected_ratio_ledger >= 0
        delta = b_next - (n + 1) * b
        expected_delta = ((n + 1) * real - real_next) // 2
        assert 2 * expected_delta == (n + 1) * real - real_next
        assert delta == expected_delta
        assert delta != 0
        divisor = math.gcd(b, b_next)
        assert delta % divisor == 0
        if n in [2, 3, 4, 7, 8, 15, 32, 64, 128, 256]:
            finite_b_rows.append({
                "N": n,
                "N_mod_8": n % 8,
                "sign_possible_adjacent": imag <= 0 and imag_next <= 0,
                "a_N": str(a),
                "a_N_plus_1": str(a_next),
                "b_N_digits": len(str(b)),
                "b_N_plus_1_digits": len(str(b_next)),
                "factorial_defect": str(delta),
                "gcd_b_layers": str(divisor),
                "gcd_divides_defect": True,
                "two_b_next_minus_seven_b": str(2 * b_next - 7 * b),
                "q_at_most_two_sevenths": True,
            })

    # Exact proof ledger for b_(N+1)>b_N.  The N=2 case is direct.
    assert native_parameters(2)[3] == 1
    assert native_parameters(3)[3] == 4
    finite_inequality = []
    for n in range(3, 80):
        # Use an integer-safe upper bound for
        # 2^(n/2)+2^((n+1)/2).
        upper = 2 ** ((n + 1) // 2) + 2 ** ((n + 2) // 2)
        assert upper < n * math.factorial(n)
        if n in [3, 4, 8, 16, 32, 64]:
            finite_inequality.append({
                "N": n,
                "integer_upper": str(upper),
                "N_times_factorial": str(n * math.factorial(n)),
            })
    return {
        "period_identity": "(1-i)^(8k+r)=16^k(1-i)^r",
        "base_residue_table": base,
        "monotone_adjacent_residues": monotone_residues,
        "transition_residue": {
            "N_mod_8": 3,
            "a_N_scale": -imag_3,
            "a_N_plus_1_scale": -imag_4,
        },
        "selected_exact_b_and_gcd_rows": finite_b_rows,
        "selected_b_monotonicity_bounds": finite_inequality,
        "all_parameter_ratio_bound": (
            "b_(N+1)>=(7/2)b_N; hence b_N/b_M<=2/7 for every M>N"
        ),
        "scope": (
            "Residue conclusions use the exact period identity; N<=256 "
            "gcd rows are replay diagnostics only."
        ),
    }


def rational_constant_checks() -> dict[str, object]:
    # Rigorous elementary upper bound e<11/4.  For k>=6, successive terms
    # in sum 1/k! have ratio at most 1/7.
    partial = sum(Fraction(1, math.factorial(k)) for k in range(6))
    tail_bound = Fraction(1, math.factorial(6)) * Fraction(7, 6)
    e_upper = partial + tail_bound
    assert e_upper < Fraction(11, 4)
    assert e_upper < 3

    # f(x)=16(x+2)-10x^2 decreases for x>4/5.  At 11/4 it is positive.
    x = Fraction(11, 4)
    f_at_upper = 16 * (x + 2) - 10 * x * x
    assert f_at_upper > 0
    # Therefore 10e^2 < 16(e+2), which is precisely the N=14 threshold.

    return {
        "exp_series_partial_0_through_5": str(partial),
        "exp_tail_ge_6_upper": str(tail_bound),
        "rigorous_e_upper": str(e_upper),
        "comparison_upper": "11/4",
        "f_11_over_4": str(f_at_upper),
        "conclusion": "10e^2<16(e+2), hence (36) for every N>=14",
        "thin_coordinate_constant": (
            "e<3 gives 2-3e/7>5/7, hence T>5 B_N/7"
        ),
    }


def factorial_cancellation_checks() -> dict[str, object]:
    rows = []
    for n, m in [(2, 3), (4, 8), (8, 9), (14, 15), (14, 22), (32, 64)]:
        fact_n = math.factorial(n)
        fact_m = math.factorial(m)
        ratio = fact_m // fact_n
        assert fact_m == ratio * fact_n
        assert math.gcd(ratio, 1) == 1
        # Kernel of (fact_n,fact_m) over primitive Z^2 is +/-(ratio,-1).
        assert ratio * fact_n - fact_m == 0
        rows.append({
            "N": n,
            "M": m,
            "factorial_ratio": str(ratio),
            "primitive_cancel_vector": [str(ratio), "-1"],
        })

    return {
        "rows": rows,
        "all_parameter_identity": (
            "u*N!+v*M!=0 iff (u,v)=k*(M!/N!,-1) for integer k"
        ),
        "analytic_separation": (
            "r L_N-L_M >= (e+2)/e-5e/(M+1) "
            ">= (e+2)/(2e) for N>=14"
        ),
    }


def exact_dependence_checks() -> dict[str, object]:
    rows = []
    for n, m in [(4, 8), (8, 12), (8, 16), (12, 20), (16, 32)]:
        _, imag_n, a_n, b_n = native_parameters(n)
        _, imag_m, a_m, b_m = native_parameters(m)
        assert imag_n == imag_m == 0
        assert a_n == a_m == 0
        assert b_m > b_n > 0
        q = Fraction(b_n, b_m)
        assert 0 < q < 1
        # For 0<t<1 and M>N, t^N-q t^M
        # =t^N(1-q t^(M-N))>0.
        rows.append({
            "N": n,
            "M": m,
            "q": str(q),
            "epsilon_N": "0",
            "epsilon_M": "0",
            "normal_integrand_factor": f"t^{n}*(1-({q})*t^{m-n})",
        })
    return {
        "rows": rows,
        "all_parameter_identity": (
            "if epsilon_N=epsilon_M then delta G_N-q delta G_M=0, "
            "so T=T(0)=integral R e^-t (t^N-q t^M)>0"
        ),
        "scope": "Rows illustrate the exact a_N=a_M=0 subfamily.",
    }


def primitive_normal_checks() -> dict[str, object]:
    rows = []
    for n in range(2, 129):
        real, _, _, b_n = native_parameters(n)
        real_m, _, _, b_m = native_parameters(n + 1)
        g = math.gcd(b_n, b_m)
        defect = b_m - (n + 1) * b_n
        assert defect == ((n + 1) * real - real_m) // 2
        assert defect != 0 and defect % g == 0
        primitive = (b_m // g, -b_n // g)
        assert math.gcd(abs(primitive[0]), abs(primitive[1])) == 1
        # q=b_n/b_m and U=(b_m/g)*(L_N-q L_M).
        if n in [2, 3, 4, 7, 8, 15, 16, 31, 32, 63, 64, 127, 128]:
            rows.append({
                "N": n,
                "g": str(g),
                "defect": str(defect),
                "primitive_normal_first_digits": len(str(abs(primitive[0]))),
                "primitive_normal_second_digits": len(str(abs(primitive[1]))),
                "b_M_over_g": str(primitive[0]),
            })
    return {
        "rows": rows,
        "identity": (
            "gcd(b_N,b_(N+1)) divides ((N+1)R_N-R_(N+1))/2"
        ),
        "normalization": (
            "primitive U=(b_M/g)L_N-(b_N/g)L_M=(b_M/g)T"
        ),
        "scope": "Finite rows replay exact identities; the divisibility is all-N.",
    }


def major_gap_checks() -> dict[str, object]:
    rows = []
    for p, q, limit in [(1, 1, 7), (2, 3, 11), (-3, 5, 13)]:
        assert math.gcd(abs(p), q) == 1
        checked = 0
        for d in range(1, limit + 1):
            for a in range(-2 * limit, 2 * limit + 1):
                for b in range(-2 * limit, 2 * limit + 1):
                    normal = Fraction(q * a - p * b, d)
                    assert not (0 < normal < Fraction(1, limit))
                    checked += 1
        rows.append({
            "p": p,
            "q": q,
            "Q": limit,
            "finite_pairs_checked": checked,
        })
    return {
        "rows": rows,
        "exact_reason": (
            "for (x,y)=(A/d,B/d), qx-py is an integer divided by d; "
            "if nonzero and d<=Q its magnitude is at least 1/d>=1/Q"
        ),
        "scope": "Enumeration is illustrative; the integer-over-d proof is exact.",
    }


def numerical_scale_diagnostics() -> dict[str, object]:
    mp.mp.dps = 90
    e = mp.e
    c0 = 4 * e - 2
    c1 = 16 * e
    rows = []
    boundary_rows = []
    for n in [8, 9, 10, 11, 16, 24, 32, 48, 64, 96]:
        real_n, imag_n, a_n, b_n = native_parameters(n)
        real_m, imag_m, a_m, b_m = native_parameters(n + 1)
        if imag_n > 0 or imag_m > 0:
            continue
        eps_n = mp.mpf(a_n) / b_n
        eps_m = mp.mpf(a_m) / b_m
        q = mp.mpf(b_n) / b_m
        b_mass = mp.gammainc(n + 2, 0, 1)
        A = c1 * b_n / 2
        B = 2 * c0 * q * b_mass
        tau = (B / (2 * A)) ** (mp.mpf(1) / 3)
        tau_used = min(mp.mpf(1), tau)
        thin_bound = abs(eps_n - eps_m) * (
            A * tau_used**2 + B / (tau_used + eps_m)
        )
        broad_bound = c0 * b_mass
        first_coordinate_bound = q * broad_bound + thin_bound
        area_bound = broad_bound * thin_bound
        rows.append({
            "N": n,
            "N_mod_8": n % 8,
            "optimizer_tau": mp.nstr(tau, 18),
            "log10_thin_bound": mp.nstr(mp.log10(thin_bound), 18)
                if thin_bound else "-inf",
            "log10_broad_bound": mp.nstr(mp.log10(broad_bound), 18),
            "log10_first_coordinate_bound": mp.nstr(
                mp.log10(first_coordinate_bound), 18
            ),
            "log10_area_bound": mp.nstr(mp.log10(area_bound), 18)
                if area_bound else "-inf",
            "epsilon_equal": eps_n == eps_m,
            "R_N": str(real_n),
            "R_N_plus_1": str(real_m),
        })
        response = lambda x: e + 4 * mp.exp(x) / (x * x - 2 * x + 2)
        base_difference = mp.quad(
            lambda x: response(x) * mp.exp(-x) * x**n * (1 - x),
            [0, 1],
        )
        loose_mass = mp.quad(
            lambda x: mp.exp(-x) * x**n * (1 - x), [0, 1]
        )
        assert base_difference >= (e + 2) * loose_mass
        boundary_rows.append({
            "N": n,
            "N_squared_base_difference": mp.nstr(n * n * base_difference, 18),
            "N_squared_loose_lower_bound": mp.nstr(
                n * n * (e + 2) * loose_mass, 18
            ),
        })
    return {
        "rows": rows,
        "exact_boundary_diagnostics": boundary_rows,
        "scope": (
            "High-precision scale and boundary rows are diagnostics only.  "
            "Equations (6)-(11), including N^2 D_N^0 -> 5, are proved "
            "symbolically and asymptotically in the source."
        ),
    }


def main() -> None:
    dependency_audit = {}
    for relative, expected in DEPENDENCIES.items():
        observed = sha256(ROOT / relative)
        assert observed == expected, (relative, observed, expected)
        dependency_audit[relative] = observed

    controls = [control_audit(SOURCE), control_audit(Path(__file__))]
    assert all(item["clean"] for item in controls)

    result = {
        "theorem": "adjacent joint-output thin-strip and determinant no-go",
        "dependency_audit": dependency_audit,
        "control_audit": controls,
        "symbolic_kernel": symbolic_kernel_checks(),
        "gaussian_residues": gaussian_residue_checks(),
        "rational_constants": rational_constant_checks(),
        "factorial_cancellation": factorial_cancellation_checks(),
        "exact_dependence": exact_dependence_checks(),
        "primitive_normal": primitive_normal_checks(),
        "major_gap": major_gap_checks(),
        "numerical_scales": numerical_scale_diagnostics(),
        "scope": {
            "proved_all_parameter": [
                "exact thin-coordinate bound for every sign-possible pair",
                "all-pair position T>5 B_N/7>=5/(7e(N+1))",
                "adjacent factorial thinness and area upper bound",
                "positive invariant line in the exact-dependence edge case",
                "one-sided adjacent gap for N mod 8 in {0,1,2}",
                "conditional linear common-denominator floor under temporary rationality",
                "all-pair separation of the unique factorial-cancel direction",
                "primitive integer normalization of the analytic thin normal",
            ],
            "not_claimed": [
                "translation-free rational lattice point from small area",
                "effective rational patch or numerator-content estimate",
                "exclusion of every conceivable two-output arithmetic identity",
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
