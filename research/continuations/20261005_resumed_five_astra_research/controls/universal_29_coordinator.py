"""Coordinator-authored exact universal RC pass, from retained A2 turn24.

No remote code execution. Inputs are fixed authenticated-free arithmetic data.
The certificate distinguishes valid finite calculations from source theorems.
"""
import hashlib
import json
import math
import resource
from pathlib import Path

import numpy as np

resource.setrlimit(resource.RLIMIT_CPU, (300, 300))
HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / 'astra_pro5_20261004/controls/twenty_nine_kernel_control.json'
data = json.loads(SOURCE.read_text())
p = 29
L = p**4
n = 2791829217
b = 1395217
bstar = 687936
ha = data['hA_newton_mod841']
hq = data['hQ_newton_mod24389']
ch = data['boundary_c_h0_to59_mod707281']
assert len(ha) == len(hq) == 58 and len(ch) == 60


def choose(a, k):
    if k < 0:
        return 0
    return (math.comb(a, k) if k <= a else 0) if a >= 0 else (-1)**k * math.comb(k-a-1, k)


def kernel_cache(coeff, mod):
    at = [choose(2*n+t-1, t) % mod for t in range(58)]
    cache = np.zeros((31, p*p), dtype=np.int64)
    omitted_nonzero = 0
    for xx in range(p*p):
        st = [sum(coeff[i] * choose(xx, i-t) for i in range(t, 58)) % mod for t in range(58)]
        sm = [sum(coeff[i] * choose(xx-1, i-t) for i in range(t, 58)) % mod for t in range(58)]
        for q in range(59):
            z = (at[q-1] * (st[q-1] + xx*sm[q-1]) if q else 0)
            if q < 58:
                z += at[q] * xx*sm[q]
            z %= mod
            if q <= 30:
                cache[q, xx] = z
            else:
                omitted_nonzero += int(z != 0)
    assert omitted_nonzero == 0
    return cache


ac = kernel_cache(ha, p*p)
qc = kernel_cache(hq, p**3)
ee = [sum((-1)**h * ch[h] * choose(h, k) for h in range(k, 60)) % L for k in range(60)]
ee.extend([0])
fact = np.array([math.factorial(i) % (p*p) for i in range(p)], dtype=np.int64)
invfact = np.array([pow(int(z), -1, p*p) for z in fact], dtype=np.int64)
harm = [0]
for i in range(1, p):
    harm.append((harm[-1] + pow(i, -1, p)) % p)
H = np.array(harm, dtype=np.int64)
f28powers = np.array([pow(int(fact[28]), i, p*p) for i in range(9)], dtype=np.int64)
x = np.arange(L, dtype=np.int64)
v = bstar-x
e = (x > 191112).astype(np.int64)
u = (382219+v)//L
shape = np.where(e == 0, 0, np.where(u == 1, 1, 2))
shape_masks = [shape == k for k in range(3)]
xc = x % (p*p)
slots = np.zeros((2, 2, 3, L), dtype=np.int64)
normalization_checks = 0
precision_obstructions = []
carry_hist = [0]*9


def normalization(raw, c, divisor_depth, precision, q, column):
    global normalization_checks
    out = np.zeros(L, dtype=np.int64)
    for cc in range(9):
        mask = c == cc
        if not np.any(mask):
            continue
        delta = cc-divisor_depth
        rr = raw[mask]
        normalization_checks += int(mask.sum())
        if delta < 0:
            denom = p**(-delta)
            if np.any(rr % denom):
                bad = np.flatnonzero(mask & ((raw % denom) != 0))[:5]
                raise ArithmeticError(f'{column} q={q}, carry={cc}, division fails at x={bad.tolist()}')
            if precision+delta < 2:
                # The source kernel is too coarse to determine the normalized
                # next digit, even if its retained representative is zero.
                precision_obstructions.append({'column': column, 'q': q, 'carry': cc, 'rows': int(mask.sum()), 'required_raw_precision': 2-delta, 'available': precision})
            out[mask] = (rr//denom) % (p*p)
        else:
            out[mask] = (rr * (p**delta if delta < 2 else 0)) % (p*p)
    return out


for q in range(-60, 31):
    r = (v-q < 0).astype(np.int64)
    lows = [np.full(L, 191112, dtype=np.int64), x, 191112-x+L*e,
            382219+v-L*u, v-q+L*r, np.full(L, 382219+q, dtype=np.int64)]
    assert all(np.all((z >= 0) & (z < L)) for z in lows)
    signs = [1, -1, -1, 1, -1, -1]
    digits = [[(z//(p**i)) % p for i in range(4)] for z in lows]
    c = np.zeros(L, dtype=np.int64)
    unit = np.ones(L, dtype=np.int64)
    l0 = np.zeros(L, dtype=np.int64)
    for i in range(4):
        c += (e+u+r)*(p**(3-i))
        for j, sign in enumerate(signs):
            c += sign*(lows[j]//(p**(i+1)))
            unit = (unit*(fact if sign == 1 else invfact)[digits[j][i]]) % (p*p)
            if i < 3:
                l0 += sign*digits[j][i+1]*H[digits[j][i]]
    assert np.all((c >= 0) & (c <= 8))
    for cc in range(9):
        carry_hist[cc] += int(np.count_nonzero(c == cc))
    unit = (unit*f28powers[c]) % (p*p)
    l0 += 3*H[digits[0][3]] - (3-e)*H[digits[2][3]]
    l0 += (6+u)*H[digits[3][3]] + r*H[digits[4][3]] - 6*H[digits[5][3]]
    l0 %= p
    ld = (H[digits[3][3]]-H[digits[4][3]]) % p
    lj = (-H[digits[1][3]]+H[digits[2][3]]-H[digits[3][3]]+H[digits[4][3]]) % p
    araw = ac[q, xc] if q >= 0 else np.zeros(L, dtype=np.int64)
    yraw = qc[q, xc] if q >= 0 else np.zeros(L, dtype=np.int64)
    if q <= 0:
        k = -q
        boundary = (ee[k] + x*(ee[k]+(ee[k-1] if k else 0))) % L
        yraw = (yraw+boundary) % L
    aa = normalization(araw, c, 2, 2 if q >= 0 else 6, q, 'A')
    qq = normalization(yraw, c, 3, 3 if q >= 0 else 4, q, 'Q')
    for col, zz in enumerate((aa, qq)):
        base = (zz*unit*(1+p*l0)) % (p*p)
        dz = ((zz % p)*(unit % p)*ld) % p
        jz = ((zz % p)*(unit % p)*lj) % p
        for rr in (0, 1):
            mask = r == rr
            slots[col, rr, 0, mask] = (slots[col, rr, 0, mask]+base[mask]) % (p*p)
            slots[col, rr, 1, mask] = (slots[col, rr, 1, mask]+dz[mask]) % p
            slots[col, rr, 2, mask] = (slots[col, rr, 2, mask]+jz[mask]) % p
    if q % 10 == 0:
        print('Laurent position completed', q, flush=True)

inv6 = pow(6, -1, p*p)
table = []
for si, (ev, uv) in enumerate(((0, 1), (1, 1), (1, 0))):
    for vv in range(3):
        flat = np.zeros(L, dtype=np.int64)
        hh = [np.zeros(L, dtype=np.int64), np.zeros(L, dtype=np.int64)]
        for rr in (0, 1):
            ss = vv-rr
            if ss not in (0, 1):
                continue
            ar = slots[0, rr, 0]
            ass = slots[0, ss, 0]
            qs = slots[1, ss, 0]
            flat += (ar*qs-inv6*ar*ass) % (p*p)
            for zz in range(2):
                br = slots[0, rr, zz+1]
                bs = slots[0, ss, zz+1]
                cs = slots[1, ss, zz+1]
                hh[zz] += (ar*cs+br*qs-(inv6 % p)*(ar*bs+br*ass)) % p
        t0 = int(flat[shape_masks[si]].sum()) % (p*p)
        td, tj = [int(z[shape_masks[si]].sum()) % p for z in hh]
        table.append({'e': ev, 'u': uv, 'v': vv, 'flat_mod841': t0, 'D_mod29': td, 'J_mod29': tj})

all_divided = all(z['flat_mod841'] % p == 0 for z in table)
report = {'status': 'FINITE_PASS' if not precision_obstructions and all_divided else 'SOURCE_PRECISION_OR_DIVISION_OBSTRUCTION',
          'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
          'p': p, 'x_count': L, 'positions': [-60, 30], 'n': n, 'b': b,
          'normalization_checks': normalization_checks, 'carry_histogram': carry_hist,
          'precision_obstructions': precision_obstructions, 'table': table,
          'all_flat_entries_divisible_by29': all_divided,
          'scope': 'Coordinator exact arithmetic on the retained fixed representative and source kernel. No infinite transfer or irrationality claim. Raw coefficient precision is checked separately before acceptance.'}
(HERE/'universal_29_coordinator.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
