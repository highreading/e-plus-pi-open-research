"""New, bounded standard-library interface checks; no archive code is loaded.

These examples check implications and normalization, not asymptotic theorems.
Writes only beside this file.  All inputs below are explicit small integers.
"""
from fractions import Fraction as Q
from math import factorial, comb
from pathlib import Path
import datetime
import hashlib
import json


def rank(matrix):
    a = [[Q(x) for x in row] for row in matrix]
    pivot = 0
    for j in range(len(a[0])):
        pos = next((i for i in range(pivot, len(a)) if a[i][j]), None)
        if pos is None:
            continue
        a[pivot], a[pos] = a[pos], a[pivot]
        q = a[pivot][j]
        a[pivot] = [x / q for x in a[pivot]]
        for i in range(len(a)):
            if i != pivot:
                q = a[i][j]
                a[i] = [x - q * y for x, y in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def valuation(x, p):
    x = Q(x)
    if not x:
        return None  # infinity, not a finite value
    a, b = abs(x.numerator), x.denominator
    v = 0
    while a % p == 0:
        v += 1
        a //= p
    while b % p == 0:
        v -= 1
        b //= p
    return v


def F_jets(order):
    f = [0, 2]
    for n in range(1, order):
        f.append(n * f[n] - (n * (n - 1) // 2) * f[n - 1])
    return f


def L(s):
    return sum((Q(4 * (-1) ** r, 2 * s - 1 - 2 * r)
                for r in range(s)), Q(0))


def b2_f(u):
    # n=2, h=1: C = u^3 + 4u - 8.
    return u ** 3 + 4 * u - 8


f = F_jets(8)
g = [Q(x, factorial(k)) for k, x in enumerate(f)]
# The actual nonpolynomial phi equals z + O(z^7), so these first
# coefficients also apply to that G through order 4.
matrix = [[Q(1, factorial(k)), Q(1, factorial(k - 1)), g[k], g[k - 1]]
          for k in (2, 3)] + [[Q(1), Q(1), Q(-1), Q(-1)]]
bc = [2, -2, -1, 1]
assert rank(matrix) == 3
assert all(sum(x * y for x, y in zip(row, bc)) == 0 for row in matrix)
a = [-2, 2]
remainder = []
for k in range(5):
    val = Q(a[k]) if k < len(a) else Q(0)
    for j in range(2):
        if k >= j:
            val += Q(bc[j], factorial(k - j)) + bc[j + 2] * g[k - j]
    remainder.append(val)
assert remainder[:4] == [0] * 4
assert remainder[4] == Q(1, 12)
assert sum(a) == sum(bc[:2]) == sum(bc[2:]) == 0

# Normalized q alone, even with q(0) odd and w nonzero, does not imply
# the same-y-basis V gate. This synthetic q is NOT the actual orthogonal q.
n, i, j = 9, 4, 4
q = [comb(n, t) for t in range(n + 1)]
q[0] += 2 ** n  # (y+1)^9 + 2^9
V = sum((Q(c) * L(i + j + t) for t, c in enumerate(q)), Q(0))
required = i + j + valuation(factorial(i), 2) + valuation(factorial(j), 2) + 1
assert valuation(V, 2) < required
assert sum(c * (-1) ** t for t, c in enumerate(q)) == 2 ** n
assert q[0] % 2 == 1

# An integer symmetric moment operator need not give integral monic
# orthogonal coefficients. Its first moments are (1,0,2,3).
T = [[0, 1, 1], [1, 0, 1], [1, 1, 1]]
vec = [1, 0, 0]
moments = []
for k in range(4):
    moments.append(vec[0])
    vec = [sum(T[i][j] * vec[j] for j in range(3)) for i in range(3)]
assert moments == [1, 0, 2, 3]
assert Q(-2) * moments[0] + Q(-3, 2) * moments[1] + moments[2] == 0
assert Q(-2) * moments[1] + Q(-3, 2) * moments[2] + moments[3] == 0

# The b2 polynomial equations allow unbounded Hensel depths for synthetic
# states.  They do NOT assert that an actual H_n recurrence attains them.
p, u = 11, 7
assert b2_f(u) % p == 0
assert (3 * u * u + 4) % p != 0
states = []
for depth in range(1, 7):
    modulus = p ** depth
    assert b2_f(u) % modulus == 0
    v = Q(6 - 2 * u - u * u, u)
    D = Q(6) - 2 * u - u * u - u * v
    C = b2_f(u)
    assert D == 0 and valuation(C, p) >= depth
    states.append({'depth': depth, 'u_integer': u, 'v_rational': str(v),
                   'D': str(D), 'C': C, 'v11_C': valuation(C, p),
                   'actual_HP_state': False})
    digit = (-(C // modulus) * pow(3 * u * u + 4, -1, p)) % p
    u += digit * modulus

# Single-jet N=4 illustration with base P=z. No radius>2 is claimed for it.
N = 4
c = sum((Q(1 + f[k], factorial(k)) for k in range(N + 1)), Q(0))
Z = c * factorial(N)
assert Z.denominator == 1 and Z.numerator % 2
dyadic = valuation(factorial(N), 2)
odd = factorial(N) // 2 ** dyadic
K = (-pow(2, -1, odd) * Z.numerator) % odd
if K > (odd - 1) // 2:
    K -= odd
changed = c + Q(2 * K, factorial(N))
assert changed.denominator == 2 ** dyadic

result = {
    'author': '/root/organization_evidence',
    'computed_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'scope': 'Bounded exact checks of implication/normalization examples only',
    'archived_code_or_libraries_executed': False,
    'network_or_subprocess_or_dynamic_exec': False,
    'F_jets_0_through_8': f,
    'n1_actual_HP_endpoint_counterexample': {
        'unknown_order': ['B0', 'B1', 'C0', 'C1'],
        'high_matrix': [[str(x) for x in row] for row in matrix],
        'rank': 3, 'nullity': 1,
        'primitive_A': a, 'primitive_B': bc[:2], 'primitive_C': bc[2:],
        'ordinary_R_coefficients_0_through_4': list(map(str, remainder)),
        'endpoint_pair_A1_B1': [0, 0], 'C1': 0,
        'normalization': 'opposite ray to archived negative first-free convention',
        'excluded_claim': 'full row rank + nonzero first free jet implies nonzero endpoint pair at every n',
        'not_excluded': 'eventual nonzero endpoint or a specified subfamily theorem'
    },
    'synthetic_normalized_weighted_polynomial_without_orthogonality': {
        'n': n, 'q_y_coefficients': q,
        'q_2z_minus1_over_2n': 'z^9+1', 'q0_odd': True, 'q_minus1': 512,
        'i': i, 'j': j, 'V8': str(V), 'v2_V8': valuation(V, 2),
        'required_same_y_basis_gate': required,
        'actual_orthogonal_ray': False,
        'excluded_claim': 'normalized coefficient integrality alone gives the complete arctangent gate'
    },
    'integer_symmetric_operator_counterexample': {
        'T': T, 'moments': moments, 'monic_orthogonal_polynomial': 'z^2-(3/2)z-2',
        'leading_moment_matrix_rank': 2, 'not_2_integral': True
    },
    'b2_arbitrary_depth_synthetic_equation_states': {
        'n': 2, 'p': p, 'h': 1,
        'f_u': 'u^3+4u-8', 'simple_root_mod_p': 7,
        'states': states,
        'scope_warning': 'model local equations only; no actual HP index or gcd construction'
    },
    'single_jet_N4_exact_denominator_example': {
        'base_P': 'z', 'N': N, 'cN': str(c), 'Z': Z.numerator,
        'fN': dyadic, 'ON': odd, 'KN': K, 'changed_cN': str(changed),
        'final_denominator': changed.denominator,
        'scope_warning': 'one finite algebra check; base P=z has no claimed radius>2'
    }
}
directory = Path(__file__).resolve().parent
result['owned_program_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
(directory / 'OWN_EXACT_INTERFACE_EXAMPLES.json').write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'all_assertions_passed': True,
                  'n1_rank': rank(matrix), 'n1_endpoint': [0, 0],
                  'synthetic_V8_v2': valuation(V, 2), 'required': required,
                  'Hensel_model_depths': len(states), 'source_code_run': False},
                 ensure_ascii=False))
