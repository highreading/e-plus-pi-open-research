"""Original L24 coupled endpoint residue and exact scalar receipts.

The all-degree rate is proved in the companion note. These bounded exact
receipts retain the one Schur scalar and do not extrapolate its next digit.
"""
from fractions import Fraction
from math import factorial, comb
from pathlib import Path
import json
from weighted_regular_dyadic_subfamily import b_moments, eo_residues, vp

BASE = Path(__file__).resolve().parent


def solve2(rows, rhs, n):
    rows = [row | (rhs[i] << n) for i, row in enumerate(rows)]
    for j in range(n):
        p = next(i for i in range(j, n) if (rows[i] >> j) & 1)
        rows[j], rows[p] = rows[p], rows[j]
        for i in range(j+1, n):
            if (rows[i] >> j) & 1:
                rows[i] ^= rows[j]
    answer = 0
    for i in range(n-1, -1, -1):
        x = ((rows[i] >> n) & 1) ^ ((rows[i] & answer).bit_count() % 2)
        answer |= x << i
    return [(answer >> i) & 1 for i in range(n)]


def residue_check(m, e, o):
    def B(i,j):
        d,f = i//2,j//2
        if d & f:
            return 0
        return e[d+f] if i%2 == j%2 else o[d+f]
    rows = [sum(B(i,j) << j for j in range(2*m))
            for i in range(2*m)]
    response = [e[m+d] if t == 0 else o[m+d]
                for d in range(m) for t in range(2)]
    eta = solve2(rows, response, 2*m)
    swapped = [response[i^1] for i in range(2*m)]
    lower = sum(x*y for x,y in zip(eta,swapped)) % 2
    a = [x^y for x,y in zip(e,o)]
    assert lower == a[2*m-1] == 0
    assert all(not(d& (m-1-d)) for d in range(m))
    return {
        "m": m, "n": 2*m+1,
        "complete_pair_block_unit": True,
        "coupled_lower_sum_residue": lower,
        "endpoint_coefficient_a_2m_minus_1": a[2*m-1],
        "proved_actual_q2_lower_bound": 2*m+2,
        "next_digit_not_claimed": True,
    }


def solve_fraction(a, rhs):
    n = len(a)
    mat = [[Fraction(x) for x in row]+[Fraction(rhs[i])]
           for i,row in enumerate(a)]
    determinant = Fraction(1)
    for j in range(n):
        p = next(i for i in range(j,n) if mat[i][j])
        if p != j:
            mat[j],mat[p] = mat[p],mat[j]
            determinant = -determinant
        z = mat[j][j]
        determinant *= z
        mat[j] = [x/z for x in mat[j]]
        for i in range(j+1,n):
            w = mat[i][j]
            if w:
                mat[i] = [x-w*y for x,y in zip(mat[i],mat[j])]
    answer = [Fraction(0)]*n
    for i in range(n-1,-1,-1):
        answer[i] = mat[i][-1]-sum(mat[i][j]*answer[j]
                                         for j in range(i+1,n))
    return answer,determinant


def schur_state(b,n):
    def pair_info(i):
        if i == 0:
            return 0,0,1
        d = (i-1)//2
        return (1 if i%2 else 2),d,2**d*factorial(d)
    def plus(i,j):
        a,d,D = pair_info(i)
        c,f,F = pair_info(j)
        t = d+f
        return Fraction(sum((-1)**(t-r)*comb(t,r)*b[a+c+1+2*r]
                            for r in range(t+1)),D*F)
    mat = [[plus(i,j) for j in range(n)] for i in range(n)]
    block = [row[1:] for row in mat[1:]]
    mixed = [mat[0][i]+mat[2][i] for i in range(1,n)]
    scalar0 = mat[0][0]+2*mat[0][2]+mat[2][2]
    answer,detB = solve_fraction(block,mixed)
    s = scalar0-sum(x*y for x,y in zip(mixed,answer))
    assert vp(detB) == 0 and s > 0
    assert all(vp(x) is None or vp(x)>=1 for x in mixed)
    return {
        "n": n, "nonconstant_block_determinant_v2": vp(detB),
        "exact_schur_scalar": str(s), "s_v2": vp(s),
        "actual_center_q2_from_full_pair_theorem": vp(s)-n+4,
        "predicted_lower_bound_only": n+1,
        "next_digit_agrees_at_this_degree_only": vp(s)==2*n-2,
    }


def run():
    e,o = eo_residues(260)
    checks = [residue_check(m,e,o) for m in (2,8,32,128)]
    b = b_moments(40)
    scalar = [schur_state(b,n) for n in (5,17)]
    assert [r['s_v2'] for r in scalar] == [8,32]
    out = {
        "status": "AUTHOR L24 new coupled endpoint arithmetic, not audit",
        "theorem": "WEIGHTED_REGULAR_ENDPOINT_DYADIC_RATE.md",
        "all_degree_proved_bound": "v2(actual q_center)>=n+1 for n=4^j+1",
        "coupled_residue_receipts": checks,
        "complete_endpoint_schur_receipts": scalar,
        "bounded_n65_source": "WEIGHTED_REGULAR_ENDPOINT_N65_PROBE.json",
        "exact_linear_equality_is_unproved": True,
        "odd_content_or_irrationality_not_inferred": True,
    }
    (BASE/'WEIGHTED_REGULAR_ENDPOINT_DYADIC_RATE_RECEIPT.json').write_text(
        json.dumps(out,indent=2)+'\n')
    print(json.dumps([dict(n=r['n'],s_v2=r['s_v2'],actual_q2=r[
        'actual_center_q2_from_full_pair_theorem']) for r in scalar],indent=2))


if __name__ == '__main__':
    run()
