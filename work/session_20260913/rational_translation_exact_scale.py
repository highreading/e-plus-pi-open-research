"""Exact finite-state certificates for the proven rational-translation formula.

No floating-point calculations and no numerical assertions about pi occur here.
The proof of the formula and finite-state termination is in the companion note.
"""

import json
from fractions import Fraction
from math import gcd
from pathlib import Path


def certificate(a, b):
    if b <= 0 or gcd(a, b) != 1:
        raise ValueError("a/b must be reduced with b positive")
    modulus = b * b
    initial = ((a - 3 * b) % modulus, (a - b) % modulus, 1 % modulus)
    state = initial
    seen = set()
    gcd_values = set()
    maximum = 0
    first_maximum = None
    while state not in seen:
        seen.add(state)
        u, v, t = state
        d = gcd(u, modulus)
        gcd_values.add(d)
        if d > maximum:
            maximum = d
            first_maximum = len(seen)
        next_state = ((4 * t + 2) * u + v) % modulus, u, (t + 1) % modulus
        un, vn, tn = next_state
        previous_t = (tn - 1) % modulus
        inverse = vn, (un - (4 * previous_t + 2) * vn) % modulus, previous_t
        assert inverse == state
        state = next_state
    assert state == initial, "invertibility implies return to the initial state"
    assert len(seen) <= modulus ** 3
    value = Fraction(b * b, 2 * maximum * maximum)
    return {
        "a": a,
        "b": b,
        "modulus": modulus,
        "initial_state": initial,
        "return_state": state,
        "period": len(seen),
        "gcd_values": sorted(gcd_values),
        "D": maximum,
        "first_index_attaining_D": first_maximum,
        "C_exact": str(value),
    }


if __name__ == "__main__":
    rows = [certificate(a, b) for a, b in
            [(0, 1), (1, 2), (1, 3), (1, 5), (1, 7), (2, 7),
             (1, 11), (1, 14), (1, 17), (1, 49)]]
    output = Path(__file__).with_name("rational_translation_exact_scale_examples.json")
    output.write_text(json.dumps(rows, indent=2) + "\n")
    for row in rows:
        print("{a}/{b}: period={period}, D={D}, C={C_exact}, first k={first_index_attaining_D}".format(**row))
