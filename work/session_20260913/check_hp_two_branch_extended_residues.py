"""Predeclared exact falsification test, 103 <= p <= 1009.

Test all odd primes in increasing order and stop at the first common
root outside +/-1.  Modular h,E recurrences are the primary method;
predeclared direct coefficient controls are p=103,257,509,1009 when
reached, and every counterexample is independently verified directly.
The finite test is not a proof of the restriction being tested.
"""
import json
from math import gcd
from pathlib import Path

LOWER, UPPER = 103, 1009
DIRECT_CONTROLS = {103, 257, 509, 1009}


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p**0.5) + 1))


def recurrence_gates(p):
    inv2 = pow(2, -1, p)
    h = [1, 0, 1, -5 % p]
    for n in range(3, p):
        h.append(inv2 * (
            -n*(n+7)*h[n] + n*(6-n-3*n*n)*h[n-1]
            + n*(n-1)**2*(6-n)*h[n-2]
            + n*(n-1)**2*(n-2)**2*h[n-3]
        ) % p)
    ee = [1]
    for n in range(1, p+1):
        ee.append((h[n]+n*h[n-1]-n*(n-1)*ee[n-1]) % p)
    jj = [n*(h[n]+ee[n]) % p for n in range(p+1)]
    return h, ee, jj


def direct_gates(p, wanted=None):
    inv2 = pow(2, -1, p)
    coeff = [1]
    h, dh, j = [], [], []
    maximum = p if wanted is None else max(wanted)
    for n in range(maximum+1):
        falling = [1]
        for r in range(1, n+2):
            falling.append(falling[-1]*(n-r+1) % p)
        h.append(sum(coeff[r]*falling[r] for r in range(n+1)) % p)
        dh.append(sum(coeff[r]*falling[r+1] for r in range(n+1)) % p)
        j.append((n*h[-1]+dh[-1]) % p)
        nxt = [0]*(len(coeff)+2)
        for k, value in enumerate(coeff):
            nxt[k] = (nxt[k]+value) % p
            nxt[k+1] = (nxt[k+1]-value) % p
            nxt[k+2] = (nxt[k+2]+inv2*value) % p
        coeff = nxt
    return h, dh, j


out = {
    "predeclared_min_prime": LOWER,
    "predeclared_max_prime": UPPER,
    "stop_rule": "first root outside +/-1, followed by exact independent verification",
    "primary_method": "proved h four-coordinate recurrence and E first-order coupling",
    "direct_control_primes": sorted(DIRECT_CONTROLS),
    "tested": [],
    "counterexample": None,
}

for p in range(LOWER, UPPER+1, 2):
    if not is_prime(p):
        continue
    h, ee, jj = recurrence_gates(p)
    for n in range(1, p):
        assert (2*h[n+1]+3*n*h[n]-n*n*h[n-1]-n*n*ee[n]) % p == 0
        assert (2*ee[n+1]-(2-n)*h[n]-n*n*h[n-1]+n*(n+2)*ee[n]) % p == 0
    for r in range(1, p-1):
        assert any((h[r], h[r-1], ee[r]))
        assert (h[r] == jj[r+1] == 0) == (h[r] == 0 and (ee[r]-r*h[r-1]) % p == 0)
    roots = [r for r in range(p) if h[r] == jj[r+1] == 0]
    extra = [r for r in roots if r not in (1, p-1)]
    row = {"p": p, "roots": roots}
    row["three_state_identity_and_gate_check"] = True
    if p in DIRECT_CONTROLS or extra:
        hd, dhd, jd = direct_gates(p)
        assert hd == h and jd == jj
        assert all(dhd[n] == n*ee[n] % p for n in range(p+1))
        row["independent_direct_full_gate_check"] = True
    out["tested"].append(row)
    if extra:
        r = extra[0]
        out["counterexample"] = {
            "p": p, "r": r, "H_r_mod_p": h[r],
            "J_r_plus_1_mod_p": jj[r+1],
            "r_squared_minus_1_mod_p": (r*r-1) % p,
            "independent_direct_verified": True,
        }
        break

out["number_of_primes_tested"] = len(out["tested"])
out["finite_test_only"] = True
Path(__file__).with_name("hp_two_branch_extended_residue_checks.json").write_text(
    json.dumps(out, indent=2) + "\n"
)
print(json.dumps(out, indent=2))
