#!/usr/bin/env python3
"""Exact certificate for the common-kernel two-form audit.

This is a verifier, not a search program.  It checks two saturated-lattice
witnesses at g_degree=40, their exact coefficient determinant and shifted-
Chebyshev L1 bounds, and the finite witnesses proving that the coefficient
image is 8 Z x 2 Z once deg(H) >= 6.

All algebraic assertions use Python integers and fractions.Fraction.  The
only decimal strings in the output are presentations of rigorously bracketed
rational intervals for e + pi and the two finite linear forms.
"""

from __future__ import annotations

from decimal import Decimal, localcontext
from fractions import Fraction
import json
import math


ROWS = [
    {
        "h": [
            -461515305521655600, 0, 153838435173885200, 0,
            -92303061104331116, -482, 65930757931692817, -1006912,
            -51279478365459305, -498189459, 41955944369935747,
            -90672448622, -35500281547655382, -7341284601930,
            30818147942358238, -293402742768892,
            -25695426639948069, -6151908266544618,
            46650705001800828, -69852477682017961,
            165502470330655435, -431146618797011914,
            864582102724254122, -1393290173864306361,
            1877383119436032177, -2036571379396784218,
            1552530965177864966, -408066030868110354,
            -934473227571679177, 1832395393035383687,
            -1964159576942462350, 1507737650884391879,
            -882394651106129320, 399908943992292704,
            -139488463620305290, 36558545744702825,
            -6867755692364982, 844645328977184,
            -55153961514524, 646233951621, 59502596865,
        ],
        "expected_a": 461515305521655600,
        "expected_b": -2704421761901323052,
        "expected_l1": [1672003183159179573, 4835703278458516698824704],
    },
    {
        "h": [
            805266044026219440, 0, -268422014675406480, 0,
            161053208805243887, 142, -115038006289469832, 436721,
            89474004878404307, 302638939, -73206009230648808,
            71039049942, 61942766161877225, 6922242086904,
            -53735567245674183, 316530863156720,
            45716055787203894, 7325648225731655,
            -70074866357059615, 89483348488380880,
            -208910400410065167, 582985920593545707,
            -1201487205284369627, 1959173245192104186,
            -2673013582751592551, 2939617747197194618,
            -2264333001974711135, 596862771509309774,
            1369033076358577649, -2659136623282220168,
            2803202204387411822, -2097203987438122184,
            1182048003381670708, -507123379601546954,
            162916899454246537, -37429081152306181,
            5529115871270438, -371220207405301,
            -17485364567717, 3240797845764, 77726079544,
        ],
        "expected_a": -805266044026219440,
        "expected_b": 4718757942649659800,
        "expected_l1": [195801091420686753, 302231454903657293676544],
    },
]


def endpoint_a_monomials(n: int) -> list[int]:
    """u_j=A(x^j), using u_0=1 and u_j=1-j*u_{j-1}."""
    u = [1]
    for j in range(1, n + 1):
        u.append(1 - j * u[-1])
    return u


def polynomial_from_h(h: list[int]) -> tuple[int, list[int]]:
    """Return a and f=a+(1+x^2)H', with h[j-1]=[x^j]H."""
    a = -h[0]
    f = [0] * (len(h) + 2)
    f[0] = a
    for j, hj in enumerate(h, start=1):
        coefficient = j * hj
        f[j - 1] += coefficient
        f[j + 1] += coefficient
    while f and f[-1] == 0:
        f.pop()
    return a, f


def eval_at_i(f: list[int]) -> tuple[int, int]:
    real = 0
    imag = 0
    for j, coefficient in enumerate(f):
        residue = j % 4
        if residue == 0:
            real += coefficient
        elif residue == 1:
            imag += coefficient
        elif residue == 2:
            real -= coefficient
        else:
            imag -= coefficient
    return real, imag


def shifted_chebyshev_coefficients(f: list[int]) -> list[Fraction]:
    """Coefficients in T_k(2x-1), by the exact binomial formula for x^j."""
    degree = len(f) - 1
    answer = [Fraction(0) for _ in range(degree + 1)]
    for j, monomial_coefficient in enumerate(f):
        if monomial_coefficient == 0:
            continue
        if j == 0:
            answer[0] += monomial_coefficient
            continue
        denominator = 2 ** (2 * j)
        answer[0] += Fraction(
            monomial_coefficient * math.comb(2 * j, j), denominator
        )
        for k in range(1, j + 1):
            answer[k] += Fraction(
                2 * monomial_coefficient * math.comb(2 * j, j - k),
                denominator,
            )
    return answer


def b_coordinate(f: list[int], h: list[int]) -> int:
    # B(f)=sum_k (-1)^k f^(k)(0)=sum_j (-1)^j j! [x^j]f.
    b_at_zero = sum(
        (-1) ** j * math.factorial(j) * coefficient
        for j, coefficient in enumerate(f)
    )
    return -b_at_zero + 4 * sum(h)


def one_row_coordinates(h_tail: list[int]) -> tuple[int, int, int]:
    """Return c.h, a, b for h_tail=(h_2,...,h_M)."""
    M = len(h_tail) + 1
    u = endpoint_a_monomials(M + 1)
    common_constraint = 0
    a = 0
    b = 0
    for m, hm in enumerate(h_tail, start=2):
        common_constraint += m * (u[m - 1] + u[m + 1] - 4) * hm
        a += 2 * m * hm
        b += (
            (-1) ** m * (m * m + m + 1) * math.factorial(m)
            + 4 * (1 - m)
        ) * hm
    return common_constraint, a, b


def e_bracket(n: int = 30) -> tuple[Fraction, Fraction]:
    partial = sum(Fraction(1, math.factorial(k)) for k in range(n + 1))
    return partial, partial + Fraction(1, n * math.factorial(n))


def atan_bracket(q: int, even_last_index: int) -> tuple[Fraction, Fraction]:
    assert even_last_index % 2 == 0
    upper = sum(
        Fraction((-1) ** j, (2 * j + 1) * q ** (2 * j + 1))
        for j in range(even_last_index + 1)
    )
    next_term = Fraction(
        1,
        (2 * (even_last_index + 1) + 1)
        * q ** (2 * (even_last_index + 1) + 1),
    )
    return upper - next_term, upper


def alpha_bracket() -> tuple[Fraction, Fraction]:
    e_lower, e_upper = e_bracket(30)
    a5_lower, a5_upper = atan_bracket(5, 24)
    a239_lower, a239_upper = atan_bracket(239, 4)
    pi_lower = 16 * a5_lower - 4 * a239_upper
    pi_upper = 16 * a5_upper - 4 * a239_lower
    return e_lower + pi_lower, e_upper + pi_upper


def decimal_string(value: Fraction, digits: int = 36) -> str:
    with localcontext() as context:
        context.prec = digits
        return str(Decimal(value.numerator) / Decimal(value.denominator))


def main() -> None:
    certified_rows = []
    alpha_lower, alpha_upper = alpha_bracket()

    for data in ROWS:
        h = data["h"]
        a, f = polynomial_from_h(h)
        u = endpoint_a_monomials(len(f) - 1)
        endpoint_a = sum(coefficient * u[j] for j, coefficient in enumerate(f))
        f_i_real, f_i_imag = eval_at_i(f)
        b = b_coordinate(f, h)
        chebyshev = shifted_chebyshev_coefficients(f)
        l1 = sum(abs(value) for value in chebyshev)
        expected_l1 = Fraction(*data["expected_l1"])

        assert a == data["expected_a"]
        assert b == data["expected_b"]
        assert endpoint_a == a
        assert (f_i_real, f_i_imag) == (a, 0)
        assert f[0] == 0 and sum(f) == 0
        assert l1 == expected_l1

        if a >= 0:
            form_lower = a * alpha_lower + b
            form_upper = a * alpha_upper + b
        else:
            form_lower = a * alpha_upper + b
            form_upper = a * alpha_lower + b
        assert form_lower > 0 and form_upper > 0

        certified_rows.append(
            {
                "a": a,
                "b": b,
                "degree_f": len(f) - 1,
                "A_f": endpoint_a,
                "f_at_i": [f_i_real, f_i_imag],
                "f_at_0": f[0],
                "f_at_1": sum(f),
                "chebyshev_l1": [l1.numerator, l1.denominator],
                "strict_form_bound_5_l1": [
                    (5 * l1).numerator,
                    (5 * l1).denominator,
                ],
                "certified_form_interval_decimal": [
                    decimal_string(form_lower),
                    decimal_string(form_upper),
                ],
            }
        )

    a1, b1 = certified_rows[0]["a"], certified_rows[0]["b"]
    a2, b2 = certified_rows[1]["a"], certified_rows[1]["b"]
    determinant = a1 * b2 - a2 * b1
    assert determinant == 559082349120

    # These two M=6 witnesses prove that the already established containment
    # Gamma_M subset 8 Z x 2 Z is sharp.
    image_witness_1 = [-55, 30, 6, 0, 0]
    image_witness_2 = [-687, 1352, -693, 0, 15]
    image_1 = one_row_coordinates(image_witness_1)
    image_2 = one_row_coordinates(image_witness_2)
    assert image_1 == (0, 8, -178)
    assert image_2 == (0, 0, 2)

    # Finite replay check of the congruence used in the source-note proof.
    u = endpoint_a_monomials(258)
    congruence_checked_through = 256
    for m in range(2, congruence_checked_through + 1):
        c_m = m * (u[m - 1] + u[m + 1] - 4)
        assert c_m % 2 == 0
        assert (c_m // 2 + m) % 4 == 0

    output = {
        "schema": "common-kernel-two-form-certificate-v1",
        "arithmetic": "exact Python integers and fractions except decimal presentations",
        "finite_degree_40_rows": certified_rows,
        "coefficient_pair_determinant": determinant,
        "image_lattice_M_ge_6": {
            "claimed_exact_image": "8 Z x 2 Z",
            "witness_h2_through_h6": [
                {
                    "h": image_witness_1,
                    "constraint_a_b": list(image_1),
                },
                {
                    "h": image_witness_2,
                    "constraint_a_b": list(image_2),
                },
            ],
            "derived_witness": "(8,0)=(8,-178)+89(0,2)",
            "congruence_replay_checked_through_m": congruence_checked_through,
        },
        "alpha_bracket": {
            "construction": (
                "e partial sum through 30 with tail <1/(30*30!); "
                "Machin pi=16 atan(1/5)-4 atan(1/239), alternating "
                "brackets ending at indices 24 and 4"
            ),
            "width_decimal": decimal_string(alpha_upper - alpha_lower),
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
