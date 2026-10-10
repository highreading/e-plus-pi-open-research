#!/usr/bin/env python3
import sys
import json
import math
import hashlib
from pathlib import Path

P = 29
P2 = 841
P3 = 24389
L = 707281
BSTAR = 687936
NREP = 2791829217
BREP = 1395217

SHAPES = [(0, 1), (1, 1), (1, 0)]
F_EXPECTED = [
    5, 25, 21, 14, 23, 15, 7, 9, 9, 28, 6, 9, 6,
    9, 6, 28, 9, 9, 7, 15, 23, 14, 21, 25, 5
]

def sha256(data):
    return hashlib.sha256(data).hexdigest()

def prepare(receipt_name, cache_name):
    raw = Path(receipt_name).read_bytes()
    receipt = json.loads(raw)
    assert receipt["status"] == "PASS"
    assert receipt["p"] == P
    assert receipt["n"] == NREP
    assert receipt["b"] == BREP

    # Established inputs: read them; do not reconstruct their contact operators.
    hA = receipt["hA_newton_mod841"]
    hQ = receipt["hQ_newton_mod24389"]
    ch = receipt["boundary_c_h0_to59_mod707281"]

    assert len(hA) == 58 and len(hQ) == 58 and len(ch) == 60
    assert all(0 <= z < P2 for z in hA)
    assert all(0 <= z < P3 for z in hQ)
    assert all(0 <= z < L for z in ch)

    # Basic filtration checks of the supplied vectors.
    assert all(z % P == 0 for z in hA[29:])
    assert all(z % P == 0 for z in hQ)
    assert all(z % P2 == 0 for z in hQ[29:])

    # Actual ordinary small-lower binomials.
    At = [
        math.comb(2 * NREP + t - 1, t) % P3
        for t in range(58)
    ]

    E = []
    for k in range(60):
        E.append(sum(
            (-1 if h & 1 else 1) * ch[h] * math.comb(h, k)
            for h in range(k, 60)
        ) % L)
    E.append(0)       # E_60
    assert E[0] % P == 2
    assert E[1] % P == 1
    assert (E[2] + E[1]) % P != 0  # exceptional full-period slope

    def reconstruct(eta, modulus, choose_x):
        # T_t = x S_t(x-1), evaluated by
        # x*binom(x-1,k) = (k+1)*binom(x,k+1).
        S = [0] * 58
        T = [0] * 58
        for t in range(58):
            S[t] = sum(
                eta[i] * choose_x[i-t]
                for i in range(t, 58)
            ) % modulus
            T[t] = sum(
                eta[i] * (i-t+1) * choose_x[i-t+1]
                for i in range(t, 58)
            ) % modulus

        out = [0] * 59
        for q in range(59):
            z = 0
            if q >= 1:
                z += At[q-1] * (S[q-1] + T[q-1])
            if q <= 57:
                z += At[q] * T[q]
            out[q] = z % modulus
        return out

    rows = []
    zero_tail_checks = 0
    for x in range(P2):
        choose_x = [
            (math.comb(x, k) % P3) if k <= x else 0
            for k in range(59)
        ]
        aa = reconstruct(hA, P2, choose_x)
        qq = reconstruct(hQ, P3, choose_x)

        assert all(z == 0 for z in aa[31:])
        assert all(z == 0 for z in qq[31:])
        zero_tail_checks += 2 * 28

        rows.append(aa[:31] + qq[:31])

    receipt_digest = sha256(raw)
    with open(cache_name, "w", encoding="ascii") as out:
        out.write("A2GAMMA0v1 " + receipt_digest + "\n")
        out.write(" ".join(map(str, E)) + "\n")
        for row in rows:
            out.write(" ".join(map(str, row)) + "\n")

    cache_raw = Path(cache_name).read_bytes()
    manifest = {
        "receipt_file": str(receipt_name),
        "receipt_sha256": receipt_digest,
        "cache_file": str(cache_name),
        "cache_sha256": sha256(cache_raw),
        "p": P,
        "representative_n": NREP,
        "representative_b": BREP,
        "positive_cache_rows": P2,
        "positive_Laurent_powers": [0, 30],
        "boundary_Laurent_powers": [-60, 0],
        "checked_zero_tail_positions": zero_tail_checks,
        "hA_hQ_contact_constructions_recomputed": False,
        "scope": "Preparation only; universal contraction not yet run."
    }
    Path(str(cache_name) + ".manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n"
    )
    print(json.dumps(manifest, indent=2))

# Ordinary bivariate polynomial operations.
# Dictionary key (i,j) represents D^i J^j.

def padd(A, B, modulus, scale=1):
    C = dict(A)
    for ij, z in B.items():
        C[ij] = (C.get(ij, 0) + scale*z) % modulus
        if C[ij] == 0:
            del C[ij]
    return C

def pmul(A, B, modulus):
    C = {}
    for (i,j), a in A.items():
        for (k,l), b in B.items():
            ij = (i+k, j+l)
            C[ij] = (C.get(ij, 0) + a*b) % modulus
    return {ij: z for ij, z in C.items() if z}

def basis_poly(e, u, v, modulus):
    ans = {(0,0): 1}
    factors = [
        ({(0,0): 3, (0,1): -1}, 2*e),
        ({(1,0): 1, (0,0): 7, (0,1): -1}, 2*u),
        ({(1,0): 1, (0,1): -1}, v)
    ]
    for f, multiplicity in factors:
        for _ in range(multiplicity):
            ans = pmul(ans, f, modulus)
    return ans

def specialize_D(poly, d):
    out = {}
    for (i,j), a in poly.items():
        out[j] = (out.get(j, 0) + a*pow(d, i, P)) % P
    return {j: a for j, a in out.items() if a}

def ordinary_jet(poly, t):
    val = sum(a*pow(t, j, P) for j, a in poly.items()) % P
    der = sum(
        j*a*pow(t, j-1, P)
        for j, a in poly.items() if j
    ) % P
    return val, der

def factor_jet(d, t, e, u, v):
    # Value and ordinary derivative of
    # (3-J)^(2e) (d+7-J)^(2u) (d-J)^v.
    bases = [(3-t) % P, (d+7-t) % P, (d-t) % P]
    exps = [2*e, 2*u, v]

    value = 1
    for b, a in zip(bases, exps):
        value = value * pow(b, a, P) % P

    derivative = 0
    for i, a in enumerate(exps):
        if not a:
            continue
        term = -a
        for k, (b, exponent) in enumerate(zip(bases, exps)):
            term = term * pow(b, exponent - (k == i), P) % P
        derivative = (derivative + term) % P
    return value, derivative

def finish(table_name, certificate_name):
    raw = Path(table_name).read_bytes()
    tab = json.loads(raw)
    assert tab["format"] == "A2T27v1"
    assert tab["rows_processed"] == L
    assert tab["Laurent_records"] == L * 91
    assert tab["all_normalizations_verified"] is True
    assert tab["all_flat_divisions_verified"] is True
    assert tab["support_size"] == 9108
    assert tab["shape_counts"] == [191113, 171762, 344406]

    rows = tab["table"]
    assert len(rows) == 9
    for row in rows:
        assert len(row) == 3
        f, hd, hj = row
        assert 0 <= f < P2 and f % P == 0
        assert 0 <= hd < P and 0 <= hj < P

    # First reconstruction: expand H_flat modulo p^2,
    # divide all its ordinary coefficients, then add H_harm.
    flat = {}
    harm = {}
    k = 0
    for e, u in SHAPES:
        for v in range(3):
            f, hd, hj = rows[k]
            k += 1
            flat = padd(flat, basis_poly(e,u,v,P2), P2, f)
            bh = basis_poly(e,u,v,P)
            lin = {(1,0): hd, (0,1): hj}
            harm = padd(harm, pmul(bh, lin, P), P)

    assert all(z % P == 0 for z in flat.values())
    divided_flat = {
        ij: (z // P) % P for ij, z in flat.items()
        if (z // P) % P
    }
    RC = padd(divided_flat, harm, P)

    # Second reconstruction: divide each of the nine flat entries first.
    RC2 = {}
    k = 0
    for e, u in SHAPES:
        for v in range(3):
            f, hd, hj = rows[k]
            k += 1
            lin = {(0,0): f//P, (1,0): hd, (0,1): hj}
            RC2 = padd(
                RC2, pmul(basis_poly(e,u,v,P), lin, P), P
            )
    assert RC == RC2
    assert all(i+j <= 7 for i,j in RC)

    H = [0]
    for i in range(1, P):
        H.append((H[-1] + pow(i, -1, P)) % P)

    gamma = []
    f_values = []
    beta_values = []
    gamma_crosscheck = []

    for d in range(25):
        admissible = []
        for t in range(4):
            v = d-t
            if 0 <= v <= 22:
                w = (math.comb(3,t)**2 *
                     math.comb(v+6,6)**2) % P
                r = (H[3-t]-H[t]+H[v]-H[v+6]) % P
                admissible.append((t,w,r))

        K = {
            0: (11*(d+7)**2 + 18*9) % P,
            1: (-22*(d+7) - 108) % P
        }
        f = sum(
            w*ordinary_jet(K,t)[0]
            for t,w,r in admissible
        ) % P
        beta = sum(
            w*(ordinary_jet(K,t)[1] +
               2*r*ordinary_jet(K,t)[0])
            for t,w,r in admissible
        ) % P

        assert f == F_EXPECTED[d]
        assert f != 0
        ratio = beta * pow(f, -1, P) % P
        f_values.append(f)
        beta_values.append(beta)

        def L_from_jet(jet):
            return sum(
                w*(jet(t)[1] + (2*r-ratio)*jet(t)[0])
                for t,w,r in admissible
            ) % P

        # Primary calculation: derivative of expanded ordinary polynomial.
        V = specialize_D(RC, d)
        g = L_from_jet(lambda t: ordinary_jet(V,t))
        gamma.append(g)

        # Product-rule cross-check, without using the expanded RC polynomial.
        g2 = 0
        k = 0
        for e, u in SHAPES:
            for v in range(3):
                flat_entry, hd, hj = rows[k]
                k += 1
                tau = flat_entry // P

                def jetB(t, e=e, u=u, v=v):
                    return factor_jet(d,t,e,u,v)

                def jetJB(t, e=e, u=u, v=v):
                    value, derivative = factor_jet(d,t,e,u,v)
                    return (
                        t*value % P,
                        (value+t*derivative) % P
                    )

                g2 += (tau+d*hd)*L_from_jet(jetB)
                g2 += hj*L_from_jet(jetJB)

        g2 %= P
        assert g == g2
        gamma_crosscheck.append(g2)
        assert L_from_jet(lambda t: ordinary_jet(K,t)) == 0

    # Exact bounded original-digit reachability data.
    exponent_period = 682892
    assert exponent_period == 28 * P**3
    assert pow(3, 28, P2) == 1 + 15*P
    assert pow(3, exponent_period, P**5) == 1 + 15*L
    b0_mod_p5 = pow(3, 432827, P**5)
    assert b0_mod_p5 % L == BSTAR
    d0 = (b0_mod_p5-BSTAR)//L

    cert = {
        "status": "PASS",
        "scope": (
            "Exact universal finite table and ordinary-polynomial contraction. "
            "Original-family consequences use the retained reconstruction "
            "dependencies. No all-depth or irrationality conclusion."
        ),
        "table_sha256": sha256(raw),
        "input_receipt_sha256": tab["input_receipt_sha256"],
        "shape_order": SHAPES,
        "v_order_per_shape": [0,1,2],
        "T_flat_mod841": [r[0] for r in rows],
        "tau_mod29": [r[0]//P for r in rows],
        "T_D_mod29": [r[1] for r in rows],
        "T_J_mod29": [r[2] for r in rows],
        "RC_ordinary_coefficients": [
            {"D_degree": i, "J_degree": j, "coefficient": RC[(i,j)]}
            for i,j in sorted(RC)
        ],
        "f_d0_to24_mod29": f_values,
        "beta_d0_to24_mod29": beta_values,
        "Gamma0_d0_to24_mod29": gamma,
        "Gamma0_product_rule_crosscheck": gamma_crosscheck,
        "Gamma0_all_zero": all(g == 0 for g in gamma),
        "Gamma1_status": "Reused established zero table; not recomputed.",
        "original_digit_reachability": {
            "d_at_a432827": d0,
            "formula": "d(t) = d0 - t mod29, a=432827+682892*t",
            "t_residue_for_each_d0_to24": [
                (d0-d) % P for d in range(25)
            ]
        },
        "checks": {
            "nine_flat_divisions": True,
            "aggregate_ordinary_coefficient_division": True,
            "two_RC_reconstructions_agree": True,
            "ordinary_derivative_and_product_rule_agree": True,
            "L_d_K_d_zero": True
        }
    }
    Path(certificate_name).write_text(
        json.dumps(cert, indent=2) + "\n"
    )
    print(json.dumps(cert, indent=2))

def main():
    if len(sys.argv) != 4 or sys.argv[1] not in ("prepare", "finish"):
        raise SystemExit(
            "Usage:\n"
            "  universal29.py prepare kernel_receipt.json cache29.txt\n"
            "  universal29.py finish table29.json Gamma0_certificate.json"
        )
    if sys.argv[1] == "prepare":
        prepare(sys.argv[2], sys.argv[3])
    else:
        finish(sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()
