import json
import math
from fractions import Fraction

# Single finite identity: for k=27 and the central coefficient constraints
# forced by the actual lower block, 3^a B^{-1}D is 3-integral.
# B is the full prescribed integer Legendre coefficient matrix; D multiplies
# precisely the constrained monomial coefficients by 3.
a = 3
k = 3**a
n = 2*k
middle = (3*k-1)//2
central = set(range(middle-(k-2), middle+1))

def vp(x):
    x = abs(int(x))
    if x == 0:
        return None
    answer = 0
    while x % 3 == 0:
        answer += 1
        x //= 3
    return answer

def one_digits(x):
    answer = 0
    place = 1
    while x:
        x, digit = divmod(x, 3)
        if digit == 1:
            answer += place
        place *= 3
    return answer

lucas_flags = []
support_flags = []
for j in range(n):
    exponent = one_digits(2*j)//2
    coefficients = [((-1)**(j-r)*math.comb(2*j,j-r)*math.comb(2*j+2*r,2*j)) % 3 for r in range(j+1)]
    expected = [int(r == exponent) for r in range(j+1)]
    lucas_flags.append(coefficients == expected)
    index = middle-exponent
    support_flags.append(index < 0 or index >= n or index in central)

minimum = 0
witness = None
entries_checked = 0
for i in range(n):
    for j in range(i+1):
        # Exact coefficient [ell_j] y^i, including every basis factor.
        coefficient = Fraction((4*j+1)*math.factorial(2*i)*math.factorial(i+j), math.factorial(i-j)*math.factorial(2*i+2*j+1))
        valuation = vp(coefficient.numerator)-vp(coefficient.denominator)
        valuation += int(i in central)
        entries_checked += 1
        if valuation < minimum:
            minimum = valuation
            witness = {'legendre_row': j, 'monomial_column': i, 'valuation_after_D': valuation}

basis_valuation = sum(vp(math.comb(4*j,2*j)) for j in range(n))
receipt = {
    'scope': 'One matrix identity at k=27, a=3, n=54; no actual-kernel valuation or infinite unit claim is tested.',
    'identity': '3^a B_inverse D has entries in Z_(3), with D_ii=3 on the forced central interval and 1 otherwise.',
    'central_interval': [min(central), max(central)],
    'entries_checked': entries_checked,
    'lucas_collapse_all_columns': all(lucas_flags),
    'highest_denominator_support_all_columns': all(support_flags),
    'minimum_entry_valuation_after_D': minimum,
    'conversion_bound_holds': minimum >= -a,
    'minimum_witness': witness,
    'v3_Delta_54': basis_valuation,
    'basis_carry_formula_matches': basis_valuation == a*k+(k+3)//4
}
assert receipt['lucas_collapse_all_columns']
assert receipt['highest_denominator_support_all_columns']
assert receipt['conversion_bound_holds']
assert receipt['basis_carry_formula_matches']
with open('THREE_ADIC_CONVERSION_RECEIPT.json', 'w') as handle:
    json.dump(receipt, handle, indent=2)
print(json.dumps(receipt, indent=2))
