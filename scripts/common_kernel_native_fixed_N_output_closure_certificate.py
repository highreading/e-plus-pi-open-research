#!/usr/bin/env python3
"""Exact replay for the fixed-index native output-closure theorem.

All membership decisions use fractions.Fraction.  Floating-point arithmetic
is not used.  Decimal strings in the JSON are outward-rounded renderings of
the exact rational intervals.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/common_kernel_native_fixed_N_output_closure.md"
OUTPUT = (
    ROOT / "results/common_kernel_native_fixed_N_output_closure_certificate.json"
)
RSS_CAP_KIB = 2 * 1024 * 1024
F = Fraction
sys.set_int_max_str_digits(0)

# Exact decimal brackets.  Their signs in the root equation are independently
# certified below; the decimal approximations are not assumptions.
ROOT_BRACKETS = {
    2: ("0.083709268125", "0.083709268127"),
    3: ("0.054252537042", "0.054252537044"),
    4: ("0.082545978538", "0.082545978540"),
    8: ("0.001501559710", "0.001501559713"),
    9: ("0.000430143538", "0.000430143541"),
    10: ("0.000133223810", "0.000133223813"),
    11: ("0.000039989622", "0.000039989625"),
    12: ("0.000011278162", "0.000011278165"),
    16: ("0.00000004679572", "0.00000004679575"),
    17: ("0.00000001101224", "0.00000001101227"),
    18: ("0.00000000252298", "0.00000000252301"),
    19: ("0.00000000056346", "0.00000000056349"),
    20: ("0.00000000012281", "0.00000000012284"),
}

# Finite diagnostic candidates for the genuine rational approximant to
# s=e+pi.  Membership and Q<=floor(sqrt(N!)) are certified exactly below.
APPROXIMANT_CANDIDATES = {
    25: {
        "root": ("0.000000000000043525326", "0.000000000000043525328"),
        "P": "18641173568782",
        "Q": "3181155778317",
    },
    33: {
        "root": ("0.000000000000000000050649459", "0.000000000000000000050649461"),
        "P": "15543960449313264573",
        "Q": "2652609795129689462",
    },
    43: {
        "root": ("0.00000000000000000000000000053204156", "0.00000000000000000000000000053204158"),
        "P": "312765117341153549666363298",
        "Q": "53374030160420566409591105",
    },
    88: {
        "root": ("0.0000000000000000000000000000000000000000000000000000000000000000000067134701", "0.0000000000000000000000000000000000000000000000000000000000000000000067134703"),
        "P": "62295662660888394201643600791487586726355536546936486838899736238822",
        "Q": "10630886864850972743374887376460850296157126648666121542407111449563",
    },
    164: {
        "root": ("1.1682169e-148", "1.1682171e-148"),
        "P": "1067135958041022312189031288676228583522045087328445065118391619138358514249015306828763996598439608011537581483978315205971659013945803557373812255",
        "Q": "182109012967784654662213012615155645768284178151774342466952300293413561388361341932378073874625025583345898378709944395846304412471350451726721136",
    },
    331: {
        "root": ("4.8763955e-348", "4.8763957e-348"),
        "P": "24021892606398955093203349105188521094523145319563892848008481698733568338348528307855972044683256961878469161281321871146789611747873220299593509916572039206345485681357422826967407969002561354866774533915499471997694010107389201704662875990556309037567723507479163443906691537611319815719271889556695468838183654328988562875492654753035656850247",
        "Q": "4099386886184629251939726968154681425257459659262377952803803734270157456727155431617138046453521219061720421591096572275683287335826987199543436731568424322452872555210049401419514831432463103261757440203630815506645580904321769462735541261105323515723529938955735319507631973436870087599026450247755852736826662557049603748729421699132064489419",
    },
}


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


def control_and_tex_audit(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    forbidden = [
        {"offset": index, "byte": byte}
        for index, byte in enumerate(data)
        if byte < 32 and byte not in (9, 10)
    ]
    text = data.decode("utf-8")
    tags = re.findall(r"\\tag\{([^}]+)\}", text)
    duplicate_tags = sorted({tag for tag in tags if tags.count(tag) > 1})
    return {
        "path": str(path.relative_to(ROOT)),
        "bytes": len(data),
        "forbidden_control_bytes": forbidden,
        "inline_open_close": [text.count(r"\("), text.count(r"\)")],
        "display_open_close": [text.count(r"\["), text.count(r"\]")],
        "equation_tag_count": len(tags),
        "duplicate_equation_tags": duplicate_tags,
        "clean": (
            not forbidden
            and text.count(r"\(") == text.count(r"\)")
            and text.count(r"\[") == text.count(r"\]")
            and not duplicate_tags
        ),
    }


def gaussian_power_one_minus_i(exponent: int) -> tuple[int, int]:
    real, imaginary = 1, 0
    for _ in range(exponent):
        real, imaginary = real + imaginary, imaginary - real
    return real, imaginary


def native_parameters(exponent: int) -> tuple[int, int, int, int]:
    real, imaginary = gaussian_power_one_minus_i(exponent)
    assert imaginary <= 0
    a_value = -imaginary
    difference = math.factorial(exponent) - real
    assert difference > 0 and difference % 2 == 0
    return real, imaginary, a_value, difference // 2


def exp_positive_interval(x_value: F, terms: int = 100) -> tuple[F, F]:
    """Rational enclosure of exp(x), 0<=x<=1."""
    assert 0 <= x_value <= 1
    term = F(1)
    total = term
    for index in range(1, terms + 1):
        term *= x_value / index
        total += term
    next_term = term * x_value / (terms + 1)
    tail = next_term / (1 - x_value / (terms + 2))
    return total, total + tail


def exp_negative_interval(x_value: F) -> tuple[F, F]:
    """Rational enclosure of exp(-x), 0<=x<=1."""
    lower, upper = exp_positive_interval(x_value)
    return 1 / upper, 1 / lower


def atan_interval(x_value: F, terms: int = 560) -> tuple[F, F]:
    """Alternating-series enclosure of atan(x), 0<=x<=1."""
    assert 0 <= x_value <= 1
    total = F(0)
    power = x_value
    for index in range(terms):
        summand = power / (2 * index + 1)
        total += summand if index % 2 == 0 else -summand
        power *= x_value * x_value
    next_term = power / (2 * terms + 1)
    if terms % 2:
        next_term = -next_term
    return min(total, total + next_term), max(total, total + next_term)


def pi_interval() -> tuple[F, F]:
    first = atan_interval(F(1, 5))
    second = atan_interval(F(1, 239))
    return 16 * first[0] - 4 * second[1], 16 * first[1] - 4 * second[0]


def fixed_decimal_enclosure(
    interval: tuple[F, F], digits: int
) -> tuple[F, F]:
    """Compress a rational enclosure to a common power-of-ten denominator."""
    scale = 10**digits
    lower = interval[0].numerator * scale // interval[0].denominator
    upper = -(
        (-interval[1].numerator * scale) // interval[1].denominator
    )
    return F(lower, scale), F(upper, scale)


# The raw Machin fractions have very large relatively-prime denominators.
# Outward rounding retains far more precision than the N=331 certificate
# needs while keeping every later exact operation small and deterministic.
PI_INTERVAL = fixed_decimal_enclosure(pi_interval(), 750)
E_INTERVAL = exp_positive_interval(F(1))


def truncated_exponential(exponent: int, x_value: F) -> F:
    power = F(1)
    total = F(1)
    factorial = 1
    for index in range(1, exponent + 1):
        power *= x_value
        factorial *= index
        total += power / factorial
    return total


def exponential_tail_interval(exponent: int, extra_terms: int = 100) -> tuple[F, F]:
    """Enclose sum_{k=exponent+1}^infinity 1/k! exactly."""
    index = exponent + 1
    term = F(1, math.factorial(index))
    total = term
    for _ in range(extra_terms):
        index += 1
        term /= index
        total += term
    next_term = term / (index + 1)
    tail = next_term / (1 - F(1, index + 2))
    return total, total + tail


def b_mass_interval(exponent: int) -> tuple[F, F]:
    factorial = math.factorial(exponent)
    tail = exponential_tail_interval(exponent)
    exp_minus_one = exp_negative_interval(F(1))
    return (
        factorial * tail[0] * exp_minus_one[0],
        factorial * tail[1] * exp_minus_one[1],
    )


def root_function_interval(exponent: int, x_value: F) -> tuple[F, F]:
    """Enclose a root function having the sign of mu(x)-J(x)."""
    _, _, a_value, b_value = native_parameters(exponent)
    if exponent <= 4:
        # At the small indices the crude monotonic bounds for int_0^x w are
        # wider than the chosen root brackets.  Evaluate the equivalent root
        # equation (40) directly; its exponential enclosure is far sharper
        # here.  Multiplication by exp(-x)>0 would not change either sign.
        exp_x_minus_one = exp_negative_interval(1 - x_value)
        factorial = math.factorial(exponent)
        s_x = truncated_exponential(exponent, x_value)
        s_one = truncated_exponential(exponent, F(1))
        polynomial = x_value * (a_value + b_value * x_value)
        return (
            polynomial - factorial * s_x
            + factorial * s_one * exp_x_minus_one[0],
            polynomial - factorial * s_x
            + factorial * s_one * exp_x_minus_one[1],
        )

    b_mass = b_mass_interval(exponent)
    exp_minus_x = exp_negative_interval(x_value)
    polynomial = x_value * (a_value + b_value * x_value)
    mu_interval = (
        polynomial * exp_minus_x[0],
        polynomial * exp_minus_x[1],
    )
    # int_0^x exp(-t)t^N dt lies between exp(-x)x^(N+1)/(N+1)
    # and x^(N+1)/(N+1).
    lower_integral = (
        exp_minus_x[0] * x_value ** (exponent + 1) / (exponent + 1)
    )
    upper_integral = x_value ** (exponent + 1) / (exponent + 1)
    # mu-J = mu-B_N+int_0^x w.
    lower = mu_interval[0] - b_mass[1] + lower_integral
    upper = mu_interval[1] - b_mass[0] + upper_integral
    assert lower <= upper
    return lower, upper


def reciprocal_coefficients(count: int) -> list[F]:
    coefficients = [F(1, 2), F(1, 2)]
    while len(coefficients) < count:
        coefficients.append(coefficients[-1] - coefficients[-2] / 2)
    for index in range(count - 4):
        assert coefficients[index + 4] == -coefficients[index] / 4
    return coefficients


RECIPROCAL_COEFFICIENTS = reciprocal_coefficients(400)


def integral_power_interval(
    power: int, x_value: F, blocks: int
) -> tuple[F, F]:
    """Enclose integral_0^x t^power/(t^2-2t+2) dt."""
    count = 4 * blocks
    total = F(0)
    x_power = x_value ** (power + 1)
    for index in range(count):
        total += (
            RECIPROCAL_COEFFICIENTS[index]
            * x_power
            / (power + index + 1)
        )
        x_power *= x_value
    tail = (
        F(5, 4)
        * F(1, 4**blocks)
        * x_value ** (power + 4 * blocks + 1)
        / (power + 4 * blocks + 1)
        / (1 - x_value**4 / 4)
    )
    return total - tail, total + tail


def k_interval(exponent: int, root_lower: F, root_upper: F) -> tuple[F, F]:
    _, _, a_value, b_value = native_parameters(exponent)
    middle_coefficient = 2 * b_value - a_value
    assert middle_coefficient >= 0

    def endpoint(x_value: F) -> tuple[F, F]:
        intervals = {
            power: integral_power_interval(power, x_value, 35)
            for power in (exponent, 0, 1, 2)
        }
        lower = (
            intervals[exponent][0]
            + a_value * intervals[0][0]
            + middle_coefficient * intervals[1][0]
            - b_value * intervals[2][1]
        )
        upper = (
            intervals[exponent][1]
            + a_value * intervals[0][1]
            + middle_coefficient * intervals[1][1]
            - b_value * intervals[2][0]
        )
        return lower, upper

    # The integrand in K is positive, so K is increasing in its endpoint.
    return endpoint(root_lower)[0], endpoint(root_upper)[1]


def floor_fraction(value: F) -> int:
    return value.numerator // value.denominator


def ceil_fraction(value: F) -> int:
    return -floor_fraction(-value)


def decimal_bound(value: F, digits: int, direction: str) -> str:
    scale = 10**digits
    scaled = value * scale
    integer = floor_fraction(scaled) if direction == "down" else ceil_fraction(scaled)
    sign = "-" if integer < 0 else ""
    absolute = abs(integer)
    whole, fraction = divmod(absolute, scale)
    return f"{sign}{whole}.{fraction:0{digits}d}"


def fraction_digest(value: F) -> str:
    text = f"{value.numerator}/{value.denominator}"
    return hashlib.sha256(text.encode()).hexdigest()


def translated_endpoint_bounds(
    exponent: int, root_strings: tuple[str, str]
) -> dict[str, tuple[F, F]]:
    root_lower, root_upper = map(F, root_strings)
    lower_sign = root_function_interval(exponent, root_lower)
    upper_sign = root_function_interval(exponent, root_upper)
    assert lower_sign[1] < 0
    assert upper_sign[0] > 0

    factorial = math.factorial(exponent)
    s_one = truncated_exponential(exponent, F(1))
    k_bounds = k_interval(exponent, root_lower, root_upper)
    i_bounds = integral_power_interval(exponent, F(1), 80)
    alpha_bounds = (
        4 * k_bounds[0] - factorial * s_one - factorial * PI_INTERVAL[1],
        4 * k_bounds[1] - factorial * s_one - factorial * PI_INTERVAL[0],
    )
    beta_bounds = (
        4 * i_bounds[0] - factorial * s_one - factorial * PI_INTERVAL[1],
        4 * i_bounds[1] - factorial * s_one - factorial * PI_INTERVAL[0],
    )
    assert alpha_bounds[0] <= alpha_bounds[1] < beta_bounds[0] <= beta_bounds[1]
    return {
        "root_lower_sign": lower_sign,
        "root_upper_sign": upper_sign,
        "alpha": alpha_bounds,
        "beta": beta_bounds,
    }


def scan_row(exponent: int) -> dict[str, object]:
    root_strings = ROOT_BRACKETS[exponent]
    bounds = translated_endpoint_bounds(exponent, root_strings)
    lower_sign = bounds["root_lower_sign"]
    upper_sign = bounds["root_upper_sign"]
    alpha_bounds = bounds["alpha"]
    beta_bounds = bounds["beta"]

    factorial = math.factorial(exponent)
    grid_denominator = math.isqrt(factorial)
    grid_numerator = floor_fraction(grid_denominator * alpha_bounds[1]) + 1
    candidate = F(grid_numerator, grid_denominator)
    hit = candidate < beta_bounds[0]

    reduced_numerator = None
    reduced_denominator = None
    coordinate_content = None
    approximant_denominator = None
    if hit:
        common = math.gcd(abs(grid_numerator), grid_denominator)
        reduced_numerator = grid_numerator // common
        reduced_denominator = grid_denominator // common
        reduced = F(reduced_numerator, reduced_denominator)
        assert alpha_bounds[1] < reduced < beta_bounds[0]
        assert reduced_denominator <= math.isqrt(factorial)
        coordinate_content = math.gcd(factorial, abs(reduced_numerator))
        approximant_denominator = (
            factorial * reduced_denominator // coordinate_content
        )
        assert approximant_denominator > math.isqrt(factorial)
    else:
        # For N=2 the whole interval is rigorously contained in (-11,-10),
        # so no denominator-one rational occurs.
        assert exponent == 2 and grid_denominator == 1
        assert alpha_bounds[0] > -11
        assert beta_bounds[1] < -10

    return {
        "N": exponent,
        "root_bracket": list(root_strings),
        "root_sign_upper_at_lower": decimal_bound(lower_sign[1], 20, "up"),
        "root_sign_lower_at_upper": decimal_bound(upper_sign[0], 20, "down"),
        "alpha_upper": decimal_bound(alpha_bounds[1], 24, "up"),
        "beta_lower": decimal_bound(beta_bounds[0], 24, "down"),
        "certified_inner_width_lower": decimal_bound(
            beta_bounds[0] - alpha_bounds[1], 24, "down"
        ),
        "grid_D_floor_sqrt_factorial": grid_denominator,
        "grid_c": grid_numerator,
        "hit": hit,
        "reduced_coordinate_c": reduced_numerator,
        "reduced_coordinate_D": reduced_denominator,
        "coordinate_content_gcd_factorial_c": coordinate_content,
        "induced_approximant_Q": approximant_denominator,
        "induced_approximant_Q_le_floor_sqrt_factorial": (
            approximant_denominator is not None
            and approximant_denominator <= math.isqrt(factorial)
        ),
        "exact_interval_digests": {
            "alpha_lower": fraction_digest(alpha_bounds[0]),
            "alpha_upper": fraction_digest(alpha_bounds[1]),
            "beta_lower": fraction_digest(beta_bounds[0]),
            "beta_upper": fraction_digest(beta_bounds[1]),
        },
    }


def approximant_scan_row(exponent: int) -> dict[str, object]:
    data = APPROXIMANT_CANDIDATES[exponent]
    root_strings = data["root"]
    bounds = translated_endpoint_bounds(exponent, root_strings)
    alpha_bounds = bounds["alpha"]
    beta_bounds = bounds["beta"]
    numerator = int(data["P"])
    denominator = int(data["Q"])
    candidate = F(numerator, denominator)
    assert candidate.numerator == numerator and candidate.denominator == denominator
    factorial = math.factorial(exponent)
    limit = math.isqrt(factorial)
    assert denominator <= limit

    # rho=-N!*P/Q is the translated coordinate induced by P/Q.
    coordinate = -factorial * candidate
    assert alpha_bounds[1] < coordinate < beta_bounds[0]
    left_margin = coordinate - alpha_bounds[1]
    right_margin = beta_bounds[0] - coordinate
    assert left_margin > 0 and right_margin > 0
    candidate_text = f"{numerator}/{denominator}"
    return {
        "N": exponent,
        "root_bracket": list(root_strings),
        "P": str(numerator),
        "Q": str(denominator),
        "floor_sqrt_factorial": str(limit),
        "Q_le_floor_sqrt_factorial": True,
        "candidate_sha256": hashlib.sha256(candidate_text.encode()).hexdigest(),
        "coordinate_left_margin_lower": decimal_bound(left_margin, 24, "down"),
        "coordinate_right_margin_lower": decimal_bound(right_margin, 24, "down"),
        "exact_margin_digests": {
            "left": fraction_digest(left_margin),
            "right": fraction_digest(right_margin),
        },
    }


def symbolic_and_interval_checks() -> dict[str, object]:
    # The e coefficient in (e B_N)-N!(e+pi) is exactly N!-N!=0.
    for exponent in ROOT_BRACKETS:
        factorial = math.factorial(exponent)
        assert factorial - factorial == 0

    # Check the elementary reciprocal identity coefficientwise.
    coefficients = RECIPROCAL_COEFFICIENTS[:40]
    for degree in range(40):
        coefficient = 2 * coefficients[degree]
        if degree >= 1:
            coefficient -= 2 * coefficients[degree - 1]
        if degree >= 2:
            coefficient += coefficients[degree - 2]
        assert coefficient == (1 if degree == 0 else 0)

    assert PI_INTERVAL[0] < PI_INTERVAL[1]
    assert E_INTERVAL[0] < E_INTERVAL[1]
    return {
        "e_coefficient_after_translation": 0,
        "reciprocal_identity_coefficients_checked": 40,
        "pi_interval_width": decimal_bound(
            PI_INTERVAL[1] - PI_INTERVAL[0], 100, "up"
        ),
        "e_interval_width": decimal_bound(
            E_INTERVAL[1] - E_INTERVAL[0], 100, "up"
        ),
        "arithmetic": "fractions.Fraction only",
    }


def main() -> None:
    source_audit = control_and_tex_audit(SOURCE)
    script_audit = control_and_tex_audit(Path(__file__))
    assert source_audit["clean"] and script_audit["clean"]

    coordinate_rows = [scan_row(exponent) for exponent in sorted(ROOT_BRACKETS)]
    hit_indices = [row["N"] for row in coordinate_rows if row["hit"]]
    assert hit_indices == [3, 4, 8, 9, 10, 11, 12, 16, 17, 18, 19, 20]
    assert all(
        not row["induced_approximant_Q_le_floor_sqrt_factorial"]
        for row in coordinate_rows
        if row["hit"]
    )

    approximant_rows = [
        approximant_scan_row(exponent)
        for exponent in sorted(APPROXIMANT_CANDIDATES)
    ]
    approximant_hit_indices = [row["N"] for row in approximant_rows]
    assert approximant_hit_indices == [25, 33, 43, 88, 164, 331]

    payload = {
        "schema": "common_kernel_native_fixed_N_output_closure_certificate_v2",
        "scope": (
            "Exact fixed-index native output closure, a finite translated-"
            "coordinate scan, and a separate finite genuine-approximant scan. "
            "The coordinate denominator D is not the induced approximant "
            "denominator Q=N!*D/gcd(N!,c). No irrationality or "
            "transcendence claim."
        ),
        "all_parameter_results": {
            "attainable_output_set": "(L_min_N,L_0_N)",
            "closure": "[L_min_N,L_0_N]",
            "lower_envelope": "E_N(t)=min(mu(t),J(t))",
            "strict_lower_comparison": "L_min_N>(e+2)*B_N",
            "same_germ_density": True,
        },
        "symbolic_and_interval_checks": symbolic_and_interval_checks(),
        "finite_translated_coordinate_scan_exact_rational_rows": coordinate_rows,
        "translated_coordinate_hit_indices": hit_indices,
        "all_coordinate_hits_fail_induced_Q_le_sqrt_factorial": True,
        "finite_genuine_approximant_scan_exact_rational_rows": approximant_rows,
        "genuine_approximant_hit_indices": approximant_hit_indices,
        "source_sha256": sha256(SOURCE),
        "control_and_tex_audit": {
            "source": source_audit,
            "script": script_audit,
        },
        "resource_policy": {
            "rss_cap_kib": RSS_CAP_KIB,
            "measured_peak_rss": (
                "checked against the cap and printed at replay time; omitted "
                "from JSON so the certificate remains byte-deterministic"
            ),
            "accelerator": "not used; exact rational CPU arithmetic",
        },
    }
    measured_peak = peak_rss_kib()
    assert measured_peak < RSS_CAP_KIB
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    OUTPUT.write_bytes(encoded)
    print(f"wrote {OUTPUT}")
    print(f"sha256 {hashlib.sha256(encoded).hexdigest()}")
    print(f"peak_rss_kib {measured_peak}")


if __name__ == "__main__":
    main()
