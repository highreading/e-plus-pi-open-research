from math import gcd
import json


def ev(coefficients, x):
    value = 0
    for coefficient in reversed(coefficients):
        value = value * x + coefficient
    return value


def capped_v2(value, precision):
    if value == 0:
        return precision
    magnitude = abs(value)
    return min(precision, (magnitude & -magnitude).bit_length() - 1)


def lift_root(evaluate, precision):
    root = 0
    for bit in range(precision):
        if (evaluate(root) >> bit) & 1:
            root += 1 << bit
    assert evaluate(root) % (1 << precision) == 0
    return root


cases = 0
residue_checks = 0
constant_witnesses = 0
displacement_checks = 0
examples = []
h_polynomials = [(0,), (1,), (2,), (0, 1), (1, 1), (1, 2, 1)]

for beta in (-3, -2, 0, 1, 2, 4):
    factors = [
        ('one', (1,)),
        ('T', (0, 1)),
        ('T^2', (0, 0, 1)),
        ('T^4', (0, 0, 0, 0, 1)),
        ('T-1', (-1, 1)),
        ('(T-1)(T+2)', (-2, 1, 1)),
        ('T-beta', (-beta, 1)),
        ('2+2T', (2, 2)),
        ('four', (4,)),
        ('zero', (0,)),
    ]
    for q_index, q in enumerate(((1, 1, 1), (-2, 3, -1))):
        def f(x):
            return (x - beta) * (1 + 2 * ev(q, x))

        for N in (1, 2, 3):
            for factor_name, A in factors:
                A_beta = ev(A, beta)
                for precision in (7, 9):
                    modulus = 1 << precision
                    exponent = min(precision, N + capped_v2(A_beta, precision))
                    predicted = set(range(beta % (1 << exponent), modulus, 1 << exponent))
                    observed = set()

                    # A residue x occurs for some constant perturbation exactly
                    # when this elementary linear congruence in c is soluble.
                    for x in range(modulus):
                        f_x = f(x)
                        coefficient = (1 << N) * ev(A, x)
                        divisor = gcd(coefficient, modulus)
                        residue_checks += 1
                        if f_x % divisor:
                            continue
                        reduced_modulus = modulus // divisor
                        if reduced_modulus == 1:
                            c = 0
                        else:
                            c = ((-f_x // divisor) * pow(coefficient // divisor, -1, reduced_modulus)) % reduced_modulus
                        assert (f_x + coefficient * c) % modulus == 0
                        observed.add(x)
                        constant_witnesses += 1

                    assert observed == predicted, (beta, q, N, factor_name, precision, observed ^ predicted)

                    # Check the exact displacement identity for nonconstant h
                    # as well, with valuations truncated at the working precision.
                    for h in h_polynomials:
                        def g(x):
                            return f(x) + (1 << N) * ev(A, x) * ev(h, x)

                        root = lift_root(g, precision)
                        actual_depth = capped_v2(root - beta, precision)
                        expected_depth = capped_v2((1 << N) * A_beta * ev(h, beta), precision)
                        assert actual_depth == expected_depth, (beta, N, factor_name, h, precision)
                        assert root in predicted
                        displacement_checks += 1

                    if q_index == 0 and precision == 9 and ((beta == -3 and N == 2 and factor_name == 'T^4') or (beta == 2 and N == 1 and factor_name == 'T^2') or (beta == 0 and N == 1 and factor_name == 'T')):
                        examples.append({'beta': beta, 'N': N, 'factor': factor_name, 'modulus': modulus, 'root_precision_at_least': exponent, 'number_of_possible_root_residues': len(observed)})
                    cases += 1

print(json.dumps({'status': 'PASS', 'polynomial_cases': cases, 'residue_checks': residue_checks, 'constant_witnesses': constant_witnesses, 'displacement_checks': displacement_checks, 'examples': examples, 'scope': 'Finite corroboration of the supplementary factor-constrained root-ball lemma; no project-germ or denominator claim.'}, indent=2))