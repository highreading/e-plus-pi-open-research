from math import isqrt
import json

def v2_nonzero(value):
    value = abs(value)
    assert value != 0
    return (value & -value).bit_length() - 1

rows = []
for n in range(3, 130, 2):
    target_square = (1 << (2 * n)) + n * n
    precision = 4 * n + 8
    root = n % 4
    assert (root * root - target_square) % 8 == 0

    # Lift the branch congruent to n modulo 4, retaining exact integers.
    for exponent in range(3, precision):
        modulus = 1 << exponent
        difference = target_square - root * root
        assert difference % modulus == 0
        next_bit = (difference // modulus) & 1
        root += next_bit * (1 << (exponent - 1))
        assert (root * root - target_square) % (1 << (exponent + 1)) == 0
        assert (root - n) % 4 == 0

    assert (root * root - target_square) % (1 << precision) == 0
    depth = v2_nonzero(root - n)
    assert depth == 2 * n - 1
    assert v2_nonzero(root + n) == 1
    assert v2_nonzero(n * n - target_square) == 2 * n

    lower_square_root = 1 << n
    assert isqrt(target_square) == lower_square_root
    assert lower_square_root ** 2 < target_square < (lower_square_root + 1) ** 2
    assert target_square.bit_length() == 2 * n + 1

    rows.append({'n': n, 'depth': depth, 'polynomial_evaluation_valuation': 2 * n, 'height_bits': target_square.bit_length(), 'root_precision': precision})

print(json.dumps({'status': 'passed', 'indices_checked': len(rows), 'scope': 'Finite corroboration of the varying quadratic-target construction; no project-root or irrationality conclusion.', 'samples': [row for row in rows if row['n'] in (3, 5, 9, 33, 65, 129)]}, indent=2))