"""Author L23 exact receipts for the proved regular subfamily.

No parent projection is reconstructed, and no full rational determinant is
substituted for the symbolic complete-pair theorem. Moment states are new
author evidence only. The finite four-term recurrence supports a proof.
"""
from fractions import Fraction
from math import factorial, comb
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent


def vp(x):
    x = Fraction(x)
    if not x:
        return None
    a, b = abs(x.numerator), x.denominator
    return (a & -a).bit_length() - (b & -b).bit_length()


def b_moments(count):
    b = [1, 1]
    for r in range(1, count - 1):
        b.append((r + 1) * (2 * r + 1) * b[r]
                 - r * (r + 1) * b[r - 1] - r)
    return b


def matrix(u):
    return [[-2*u-2*u*u+4*u**3+4*u**4,
             u+2*u*u-u**3-2*u**4],
            [-u+2*u*u, u-u*u]]


def forcing(u):
    return [1+u-u*u-2*u**3, 1-u]


def eo_residues(count):
    e, o = [], []
    for i in range(count):
        e.append(int(i in (0, 2, 3))
                 ^ (e[i-1] if i >= 1 else 0)
                 ^ (e[i-4] if i >= 4 else 0))
        o.append(int(i in (0, 1, 3))
                 ^ (o[i-1] if i >= 1 else 0)
                 ^ (o[i-4] if i >= 4 else 0))
    return e, o


def residue_entry(i, j, e, o):
    if i == j == 0:
        return 0
    if not i or not j:
        t = max(i, j)
        d = (t-1)//2
        return o[d] if t % 2 else e[d]
    d, f = (i-1)//2, (j-1)//2
    if d & f:
        return 0
    return o[d+f] if (i+j) % 2 else e[d+f]


def gf2_rank(rows, n):
    rows = rows[:]
    rank = 0
    for j in range(n):
        pivot = next((i for i in range(rank, n)
                      if (rows[i] >> j) & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(rank+1, n):
            if (rows[i] >> j) & 1:
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def exact_normalized_state(b, n):
    mu = [0] + b[1:]
    mat = [[Fraction(mu[i+j]) for j in range(n)]
           + [Fraction(-mu[i+n])] for i in range(n)]
    determinant = Fraction(1)
    for j in range(n):
        pivot = next(i for i in range(j, n) if mat[i][j])
        if pivot != j:
            mat[j], mat[pivot] = mat[pivot], mat[j]
            determinant = -determinant
        z = mat[j][j]
        determinant *= z
        mat[j] = [x/z for x in mat[j]]
        for i in range(j+1, n):
            w = mat[i][j]
            if w:
                mat[i] = [x-w*y for x, y in zip(mat[i], mat[j])]
    q = [Fraction(0)]*n
    for i in range(n-1, -1, -1):
        q[i] = mat[i][-1] - sum(mat[i][j]*q[j]
                                    for j in range(i+1, n))
    q.append(Fraction(1))
    vals = [vp(x) for x in q]
    assert all(x is None or x >= 0 for x in vals)
    base_depth = 2*sum((i-1)//2+vp(factorial((i-1)//2))
                       for i in range(1, n))
    assert vp(determinant) == base_depth
    m = (n-1)//2
    sigma = m + vp(factorial(m))
    normal_q0 = vp(q[0])
    return {
        "n": n,
        "signed_normalized_Hankel_v2": vp(determinant),
        "proved_monic_basis_row_scale_depth": base_depth,
        "normalized_Gram_unit_at_this_state": True,
        "all_monic_normalized_coefficients_two_integral": True,
        "normal_monic_constant_v2": normal_q0,
        "endpoint_q_minus_one_v2": n+normal_q0,
        "sigma": sigma,
        "eta_v2": normal_q0-sigma,
        "actual_center_q2_from_PROVED_complete_pair_theorem":
            n+normal_q0-2*sigma,
        "bounded_state_not_an_eta_formula": True,
    }


def run():
    b = b_moments(100)
    for t in range(1, 40):
        M, c = matrix(2*t), forcing(2*t)
        old = [b[2*t-1], b[2*t-2]]
        got = [sum(M[i][j]*old[j] for j in range(2))+c[i]
               for i in range(2)]
        assert got == [b[2*t+1], b[2*t]]
    e, o = eo_residues(520)
    a = [x ^ y for x, y in zip(e, o)]
    assert a[:4] == [0, 1, 0, 0]
    assert a[15:19] == a[:4]
    assert all(a[i+15] == a[i] for i in range(500))
    assert all(a[2**h-1] == (h % 2) for h in range(1, 9))
    diff_checks = 0
    for r in range(0, 32):
        for d in range(0, 13):
            diff = sum((-1)**(d-j)*comb(d,j)*b[r+2*j]
                       for j in range(d+1))
            den = 2**d*factorial(d)
            assert diff % den == 0
            assert (diff//den) % 2 == (o[d] if r % 2 else e[d])
            diff_checks += 1
    gram_rows = []
    for n in (5, 13, 17, 65, 257):
        rows = [sum(residue_entry(i,j,e,o) << j for j in range(n))
                for i in range(n)]
        rank = gf2_rank(rows, n)
        assert rank == n
        gram_rows.append({"n": n, "normalized_Gram_rank_mod2": rank,
                          "derived_from_exact_series_not_degree_extrapolation": True})
    # Separate signed/unsigned finite states support but do not prove eta law.
    states = [exact_normalized_state(b, n) for n in (5, 13, 17)]
    out = {
        "status": "AUTHOR exact proof-interface receipt; not independent audit",
        "theorem": "WEIGHTED_REGULAR_DYADIC_SUBFAMILY.md",
        "recurrence_pair_checks": 39,
        "normalized_difference_checks": diff_checks,
        "Abar_first_period": a[:15],
        "Abar_period_initial_state_certificate": a[15:19],
        "period15_follows_from_four_term_recurrence": True,
        "all_degree_regular_subfamily": "n=4^j+1, j>=1",
        "basis_units": gram_rows,
        "new_exact_moment_states": states,
        "full_pair_gcd_is_in_symbolic_theorem": True,
        "all_degree_eta_valuation": "UNPROVED; separate next target",
        "general_all_n_integrality": "UNPROVED",
        "no_odd_content_or_irrationality_conclusion": True,
    }
    (BASE/'WEIGHTED_REGULAR_DYADIC_SUBFAMILY_RECEIPT.json').write_text(
        json.dumps(out, indent=2)+'\n')
    print(json.dumps(states, indent=2))


if __name__ == '__main__':
    run()
