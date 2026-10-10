> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 — executable universal $\Gamma _0$ calculation, with exact digit compression

## Status

The outstanding calculation can be implemented as **one deterministic pass through**


$$
x=0,\ldots,707280,
$$


without a contact inverse, without 25 repeated passes, and without repeatedly performing four-level factorial stripping.

The main implementation improvement proved below is a **two-digit record decomposition and a 91-entry sliding window**. It preserves:

- the full four-digit factorial units modulo $841$;
- all low carry counts;
- both harmonic variables;
- every Laurent power $-60,\ldots,30$;
- the actual $x$-dependent raw coefficient at $q=-2$;
- all exact divisions before reduction.

I give complete local code for:

1. preparing the coefficient cache from the **supplied, completed** kernel receipt;
2. performing the single universal pass;
3. reconstructing the ordinary polynomial $R_C(D,J)$;
4. computing all 25 values $\Gamma _0(d)$, with two independent implementations of their final contraction.

**Execution status:** I have not executed this calculation in this interface. Therefore I do **not** supply invented numerical values for the 27 constants or for $\Gamma _0$. The code below is an executable bounded calculation request, not a receipt that the calculation has run. The numerical $\Gamma _0$-table remains the immediate outstanding result.

I reuse, rather than recompute, the supplied closure


$$
R_{29}=20K_d,\qquad \Gamma _1(d)=0\quad(0\le d\le24).
$$


I also use the supplied $h_A,h_Q,c_h$ residue lists directly. Their contact construction is not repeated as a substitute for the universal contraction.

---

## 1. Exact mathematical inputs and scope

Set


$$
p=29,\qquad L=p^4=707281,\qquad b_*=687936.
$$


The original index domain remains


$$
b=3^a,\qquad n=2001b,\qquad
a\ge1,\qquad a\equiv432827\pmod{682892}.
$$


Contact inverses retain indices $0\le i,j<b$; actual weighted coordinates retain $0\le j\le b$.

The finite kernel receipt used by the implementation is:

> `twenty_nine_kernel_control.json`, supplied SHA256  
> `d75b8e18ad606c397bdd3db90f193448646d11b8d7646c1e0098011d6d226bff`.

The implementation reads from it:

- `hA_newton_mod841`;
- `hQ_newton_mod24389`;
- `boundary_c_h0_to59_mod707281`.

It does **not** reconstruct $h_A$ or $h_Q$ by another contact calculation.

The fixed representative


$$
b^\circ=1395217,\qquad n^\circ=2791829217
$$


is used only for the proved low-parameter coefficient construction. It is not represented as an original power-$3$ index.

At the retained reconstruction dependencies, on


$$
0\le d\le24,\qquad T=0,\qquad D_1=0,
$$


the outstanding identity is


$$
\boxed{
\frac{M-(6C_n)^{-1}D}{p^2}
=C_nU\,\Gamma _0(d)\pmod p.
}
\tag{1.1}
$$


Here the falling-factorial metric is


$$
\omega_j=j!\binom{n+2}{j},\qquad
\Omega=\operatorname{diag}(\omega_j^2).
$$


The earlier “rising” terminology for this expression is not retained.

The universal calculation concerns $P,Q\bmod p^2$. Its use in (1.1) still depends on the stronger precision-three reconstruction, including:

- boundary factorial indices through $88$;
- negative powers through $-89$;
- the unfrozen $LJ\,W_jB_{-2}(j)$ correction;
- the whole logarithmic-force bound;
- the actual endpoint $W_b(1+b\theta^Q_{b-1})$.

Those are not replaced by the shorter kernel used in the universal pass.

---

# Part I. A proved efficient representation of every stripping record

## 2. Four low digits encoded by two two-digit records

For $0\le t<L$, write


$$
t=t_0+pt_1+p^2t_2+p^3t_3,\qquad 0\le t_i<p.
$$


Define


$$
\begin{aligned}
\mathfrak f(t)&=\prod_{i=0}^3t_i!\pmod{p^2},\\
\mathfrak g(t)&=\sum_{i=1}^3\left\lfloor t/p^i\right\rfloor,\\
\mathfrak e(t)&=t_1H_{t_0}+t_2H_{t_1}+t_3H_{t_2}\pmod p,\\
\mathfrak h(t)&=H_{t_3}\pmod p.
\end{aligned}
\tag{2.1}
$$


All factorials here are units.

Put $t=l+p^2h$, with $0\le l,h<p^2$, and for a two-digit integer $z=z_0+pz_1$ define


$$
f_2(z)=z_0!z_1!,\qquad
e_2(z)=z_1H_{z_0}.
$$


Then


$$
\boxed{
\begin{aligned}
\mathfrak f(t)&=f_2(l)f_2(h)\pmod{p^2},\\
\mathfrak g(t)&=\lfloor l/p\rfloor+(p+1)h+\lfloor h/p\rfloor,\\
\mathfrak e(t)&=e_2(l)+e_2(h)+(h\bmod p)H_{\lfloor l/p\rfloor}\pmod p,\\
\mathfrak h(t)&=H_{\lfloor h/p\rfloor}.
\end{aligned}}
\tag{2.2}
$$


Thus all four-digit records are obtained from tables of length $841$. The cross term in $\mathfrak e$ is essential; deleting it would lose the middle-digit harmonic interaction.

### Proof

The factorial identity follows by splitting the four digits into two pairs. Also


$$
\begin{aligned}
\mathfrak g(t)
&=\lfloor l/p\rfloor+ph+h+\lfloor h/p\rfloor,\\
\mathfrak e(t)
&=t_1H_{t_0}+t_3H_{t_2}+t_2H_{t_1}.
\end{aligned}
$$


These are exactly (2.2). No periodicity in $t\bmod841$ is asserted. ∎

---

## 3. Carry, unit, and harmonic formulas from these records

For each $x$, retain the source definitions


$$
v=b_*-x,\quad
e=\mathbf1_{x>191112},\quad
u=\left\lfloor\frac{382219+v}{L}\right\rfloor,\quad
r_q=\mathbf1_{v-q<0}.
$$


The three shapes are


$$
(0,1),\quad(1,1),\quad(1,0).
$$



Let the six low factorial arguments be


$$
\begin{array}{c|c}
\text{argument}&\text{low part}\\ \hline
W_{\rm top}&191112\\
W_{\rm bot1}&x\\
W_{\rm bot2}&191112-x+Le\\
B_{\rm top}&382219+v-Lu\\
B_{\rm bot1}&v-q+Lr_q\\
B_{\rm bot2}&382219+q .
\end{array}
\tag{3.1}
$$


All six lie in $[0,L)$.

Write


$$
S=1+p+p^2+p^3=25260.
$$


Since the sum of the signed high parts is $e+u+r_q$, the exact low carry count is


$$
\boxed{
c_{xq}
=S(e+u+r_q)
+\mathfrak g(W_{\rm top})+\mathfrak g(B_{\rm top})
-\mathfrak g(W_{\rm bot1})-\mathfrak g(W_{\rm bot2})
-\mathfrak g(B_{\rm bot1})-\mathfrak g(B_{\rm bot2}).
}
\tag{3.2}
$$


It lies in $0,\ldots,8$.

The stripped unit is


$$
\boxed{
u_{xq}
=(28!)^{c_{xq}}\,
\frac{\mathfrak f(W_{\rm top})\mathfrak f(B_{\rm top})}
{\mathfrak f(W_{\rm bot1})\mathfrak f(W_{\rm bot2})
 \mathfrak f(B_{\rm bot1})\mathfrak f(B_{\rm bot2})}
\pmod{841}.
}
\tag{3.3}
$$


In particular, $28!$ is retained modulo $841$, not replaced by $-1$.

The harmonic coefficients are


$$
\boxed{
\lambda_D=\mathfrak h(B_{\rm top})-\mathfrak h(B_{\rm bot1}),
}
\tag{3.4}
$$




$$
\boxed{
\lambda_J=-\mathfrak h(W_{\rm bot1})+\mathfrak h(W_{\rm bot2})
-\mathfrak h(B_{\rm top})+\mathfrak h(B_{\rm bot1}),
}
\tag{3.5}
$$


and


$$
\boxed{
\begin{aligned}
\lambda_0={}&
\mathfrak e(W_{\rm top})+\mathfrak e(B_{\rm top})
-\mathfrak e(W_{\rm bot1})-\mathfrak e(W_{\rm bot2})
-\mathfrak e(B_{\rm bot1})-\mathfrak e(B_{\rm bot2})\\
&+3\mathfrak h(W_{\rm top})-(3-e)\mathfrak h(W_{\rm bot2})\\
&+(6+u)\mathfrak h(B_{\rm top})
+r_q\mathfrak h(B_{\rm bot1})
-6\mathfrak h(B_{\rm bot2})\pmod p.
\end{aligned}}
\tag{3.6}
$$



These are algebraic rearrangements of the supplied four-level stripping formulas. They retain their ordinary $D,J$-dependence.

### Why the unit formula has the stated precision

For $z=pm+s$, $0\le s<p$,


$$
U_p(z)\equiv(28!)^m s!(1+pmH_s)\pmod{p^2}.
$$


The full-block correction vanishes because $H_{28}=0\bmod29$. Applying this at the four factorial levels and multiplying the first-order corrections gives (3.3)–(3.6). Products of two first-order corrections are multiples of $p^2$.

No theorem concerning logarithmic forms is needed for this step.

---

## 4. Sliding-window lemma: only one new $B_{\rm bot1}$ record per row

For fixed $x$, the 91 relevant arguments are


$$
t(x,q)=(b_*-x-q)\bmod L,\qquad -60\le q\le30.
$$


They satisfy


$$
\boxed{t(x+1,q)=t(x,q+1).}
\tag{4.1}
$$


Therefore a circular array of length 91 retains 90 records when passing from $x$ to $x+1$. Only the record at $q=30$ must be newly constructed.

This reduces approximately $64.4$ million four-digit record constructions to:

- 91 initial constructions;
- one new sliding-window construction per row after the first;
- three other changing records per row.

The pass still visits every actual $x$. It does **not** identify distinct four-digit units merely because their two low digits agree.

---

## 5. Exact affine boundary recurrence, including $q=-2$

From the supplied $c_h\bmod p^4$, compute once


$$
E_k=\sum_{h=k}^{59}(-1)^hc_h\binom hk\pmod{p^4},
\quad 0\le k\le59,
$$


with $E_{-1}=E_{60}=0$. Every raw boundary coefficient is


$$
t_{-k}(x)=E_k+x(E_k+E_{k-1})\pmod{p^4},
\quad0\le k\le60.
\tag{5.1}
$$


It can be updated by


$$
\boxed{
t_{-k}(x+1)=t_{-k}(x)+E_k+E_{k-1}\pmod{p^4}.
}
\tag{5.2}
$$



For $k=2$, the slope $E_2+E_1$ is a unit. Consequently this recurrence has full period $p^4$, not $p^2$. The implementation maintains it modulo $p^4$ throughout. It never replaces $x$ by $x\bmod841$ in this coefficient.

This is a safe finite-state representation of the exceptional boundary insertion: its state is the actual affine residue modulo $707281$.

---

# Part II. Normalization and the universal constants

## 6. Raw divisions

For each nonnegative Laurent power, use


$$
z_A=p^{c_{xq}-2}a_q(x)\pmod{p^2}.
$$


For every Laurent power, use


$$
z_Q=p^{c_{xq}-3}y_q(x)\pmod{p^2}.
$$


When an exponent is negative, division is performed on the raw integer residue only after checking divisibility.

The implementation checks, for every normalization,


$$
v_p(a_q(x))+c_{xq}\ge2,\qquad
v_p(y_q(x))+c_{xq}\ge3.
\tag{6.1}
$$


It also checks that the available raw precision is enough to determine the quotient modulo $p^2$.

For $q=-2$, this is a division of the **complete affine coefficient**, including its $x$-dependent part.

The normalized coefficient $z$ contributes


$$
zu_{xq}(1+p\lambda_0)\pmod{p^2}
$$


to its constant slot, and


$$
(z\bmod p)(u_{xq}\bmod p)\lambda_D,\qquad
(z\bmod p)(u_{xq}\bmod p)\lambda_J
$$


to its two harmonic slots modulo $p$.

The grouping is by $r_q=0,1$, not by a truncated Laurent support.

---

## 7. Table and ordinary-polynomial reconstruction

The code accumulates the supplied nine flat and eighteen harmonic constants. With the shape order


$$
(0,1),(1,1),(1,0)
$$


and $v=0,1,2$, it returns rows


$$
\bigl(T^{(0)}_{eu,v},T^{(D)}_{eu,v},T^{(J)}_{eu,v}\bigr).
$$



It checks all nine divisions


$$
\tau_{eu,v}=T^{(0)}_{eu,v}/29\pmod{29}.
$$


Then


$$
\boxed{
R_C(D,J)=
\sum_{eu,v}(3-J)^{2e}(D+7-J)^{2u}(D-J)^v
\left(\tau_{eu,v}+DT^{(D)}_{eu,v}+JT^{(J)}_{eu,v}\right).
}
\tag{7.1}
$$


This is expanded as an ordinary bivariate polynomial of total degree at most seven. No reduction modulo $J^{29}-J$ occurs.

For each $d=0,\ldots,24$, the code evaluates


$$
\Gamma _0(d)=\mathcal L_d(R_C(d,J))
\tag{7.2}
$$


in two ways:

1. differentiation of the fully expanded ordinary polynomial;
2. direct product-rule differentiation of each factor in (7.1).

The two answers must agree.

---

# Part III. Complete implementation

The following two files suffice. They perform no network access and launch no remote computation.

## 8. Python preparation and final contraction

Save as `universal29.py`.

```python
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
```

The preparation stage uses only ordinary integer binomial coefficients. The identity


$$
x\binom{x-1}{k}=(k+1)\binom{x}{k+1}
$$


avoids any special handling of negative arguments at $x=0$.

---

## 9. C++ single-pass kernel

Save as `pass29.cpp`.

```cpp
#include <array>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>

using i64 = std::int64_t;
using u64 = std::uint64_t;

constexpr int P = 29;
constexpr int P2 = 841;
constexpr int P3 = 24389;
constexpr int L = 707281;
constexpr int BSTAR = 687936;
constexpr int QMIN = -60;
constexpr int QMAX = 30;
constexpr int NQ = 91;
constexpr int CARRY_SCALE = 25260;

[[noreturn]] void fail(const std::string& s) {
    std::cerr << "FAIL: " << s << "\n";
    std::exit(1);
}

void require(bool b, const std::string& s) {
    if (!b) fail(s);
}

int mod(i64 a, int m) {
    int r = int(a % m);
    return r < 0 ? r + m : r;
}

int inverse(int a, int m) {
    i64 old_r = a, r = m;
    i64 old_s = 1, s = 0;
    while (r != 0) {
        i64 q = old_r / r;
        i64 nr = old_r - q*r;
        old_r = r; r = nr;
        i64 ns = old_s - q*s;
        old_s = s; s = ns;
    }
    require(old_r == 1, "nonunit passed to inverse");
    return mod(old_s, m);
}

struct Half {
    int fact, invfact;
    int lo, hi;
    int eh;
};

struct Record {
    int fact, invfact;
    int g, eh, htop;
};

struct Slot {
    int z = 0;  // constant residue modulo p^2
    int d = 0;  // D harmonic residue modulo p
    int j = 0;  // J harmonic residue modulo p
};

std::array<int, P> harm;
std::array<Half, P2> half_table;
std::array<int, 9> wilson_power;
u64 normalization_counts[2][3] = {};

Record record4(int t) {
    require(0 <= t && t < L, "four-digit argument out of range");
    int lo = t % P2;
    int hi = t / P2;
    const Half& a = half_table[lo];
    const Half& b = half_table[hi];

    Record R;
    R.fact = int(i64(a.fact)*b.fact % P2);
    R.invfact = int(i64(a.invfact)*b.invfact % P2);
    R.g = a.hi + (P+1)*hi + b.hi;
    R.eh = mod(a.eh + b.eh + b.lo*harm[a.hi], P);
    R.htop = harm[b.hi];
    return R;
}

int normalize_raw(
    int coeff, int carry, int base, int available_precision, int column
) {
    // coeff is a nonnegative representative modulo p^available_precision.
    require(available_precision + carry >= base + 2,
            "insufficient raw precision for normalized residue");

    int division_exponent = carry < base ? base-carry : 0;
    require(division_exponent <= 2, "unexpected division depth");
    ++normalization_counts[column][division_exponent];

    if (carry >= base+2) return 0;

    if (carry >= base) {
        int z = coeff % P2;
        if (carry == base+1) z = z*P % P2;
        return z;
    }

    int divisor = division_exponent == 1 ? P : P2;
    require(coeff % divisor == 0, "raw coefficient not exactly divisible");
    return (coeff/divisor) % P2;
}

void insert_slot(
    Slot& s, int z, int unit, int lambda0, int lambdaD, int lambdaJ
) {
    if (z == 0) return;

    int zu = int(i64(z)*unit % P2);
    int constant = int(i64(zu)*(1 + P*lambda0) % P2);
    s.z += constant;
    if (s.z >= P2) s.z -= P2;

    int zu1 = (z % P)*(unit % P) % P;
    s.d = (s.d + zu1*lambdaD) % P;
    s.j = (s.j + zu1*lambdaJ) % P;
}

int main(int argc, char** argv) {
    if (argc != 3) {
        std::cerr << "Usage: pass29 cache29.txt table29.json\n";
        return 2;
    }

    std::ifstream in(argv[1]);
    require(bool(in), "cannot open input cache");

    std::string magic, receipt_sha;
    in >> magic >> receipt_sha;
    require(magic == "A2GAMMA0v1", "wrong cache format");

    std::array<int, 61> E;
    for (int& z : E) {
        in >> z;
        require(bool(in) && 0 <= z && z < L, "bad boundary coefficient");
    }
    require(E[60] == 0, "E_60 must be zero");
    require(E[0] % P == 2 && E[1] % P == 1,
            "wrong leading boundary");
    require((E[2]+E[1]) % P != 0,
            "q=-2 slope unexpectedly not a unit");

    static int acache[P2][31];
    static int qcache[P2][31];
    for (int x = 0; x < P2; ++x) {
        for (int q = 0; q <= 30; ++q) {
            in >> acache[x][q];
            require(bool(in) && 0 <= acache[x][q] &&
                    acache[x][q] < P2, "bad A cache entry");
        }
        for (int q = 0; q <= 30; ++q) {
            in >> qcache[x][q];
            require(bool(in) && 0 <= qcache[x][q] &&
                    qcache[x][q] < P3, "bad Q cache entry");
        }
    }
    std::string extra;
    require(!(in >> extra), "extra input after cache");

    std::array<int, P> factorial, invfactorial;
    factorial[0] = 1;
    harm[0] = 0;
    for (int i = 1; i < P; ++i) {
        factorial[i] = factorial[i-1]*i % P2;
        harm[i] = (harm[i-1] + inverse(i,P)) % P;
    }
    for (int i = 0; i < P; ++i)
        invfactorial[i] = inverse(factorial[i], P2);

    for (int z = 0; z < P2; ++z) {
        int lo = z % P, hi = z / P;
        half_table[z] = {
            factorial[lo]*factorial[hi] % P2,
            invfactorial[lo]*invfactorial[hi] % P2,
            lo, hi, hi*harm[lo] % P
        };
    }

    wilson_power[0] = 1;
    for (int c = 1; c <= 8; ++c)
        wilson_power[c] =
            wilson_power[c-1]*factorial[28] % P2;

    const Record Wtop = record4(191112);

    // Fixed B_bot2 records.
    std::array<Record, NQ> Bbot2;
    for (int qi = 0; qi < NQ; ++qi)
        Bbot2[qi] = record4(382219 + QMIN + qi);

    // Sliding window for B_bot1, initially at x=0.
    std::array<Record, NQ> ring;
    int head = 0;
    for (int qi = 0; qi < NQ; ++qi)
        ring[qi] = record4(BSTAR - (QMIN + qi));

    // Complete affine raw boundary state modulo p^4.
    std::array<int, 61> boundary = E;
    std::array<int, 61> slope;
    for (int k = 0; k <= 60; ++k)
        slope[k] = (E[k] + (k ? E[k-1] : 0)) % L;

    int T0[3][3] = {};
    int TD[3][3] = {};
    int TJ[3][3] = {};

    u64 carry_histogram[NQ][9] = {};
    u64 r_one_counts[NQ] = {};
    u64 shape_counts[3] = {};
    u64 support_size = 0;
    int support_kappa[3] = {};
    int support_g[3] = {};

    const int inv6_p2 = inverse(6, P2);
    const int inv6_p = inverse(6, P);

    for (int x = 0; x < L; ++x) {
        int e = x > 191112;
        int raw_top = 382219 + BSTAR - x;
        int u = raw_top >= L;
        int shape = (e == 0) ? 0 : (u == 1 ? 1 : 2);
        ++shape_counts[shape];

        int vlow = BSTAR - x;
        int wb2low = 191112 - x + L*e;
        int btoplow = raw_top - L*u;

        Record Wbot1 = record4(x);
        Record Wbot2 = record4(wb2low);
        Record Btop = record4(btoplow);

        int carry_base =
            CARRY_SCALE*(e+u) + Wtop.g + Btop.g
            - Wbot1.g - Wbot2.g;

        int unit_base = Wtop.fact;
        unit_base = int(i64(unit_base)*Btop.fact % P2);
        unit_base = int(i64(unit_base)*Wbot1.invfact % P2);
        unit_base = int(i64(unit_base)*Wbot2.invfact % P2);

        int harmonic_base =
            Wtop.eh + Btop.eh - Wbot1.eh - Wbot2.eh
            + 3*Wtop.htop - (3-e)*Wbot2.htop
            + (6+u)*Btop.htop;

        int lambdaJ_base =
            -Wbot1.htop + Wbot2.htop - Btop.htop;

        std::array<Slot,2> A{};
        std::array<Slot,2> Q{};
        int cache_x = x % P2;

        for (int qi = 0; qi < NQ; ++qi) {
            int q = QMIN + qi;
            int ring_index = head + qi;
            if (ring_index >= NQ) ring_index -= NQ;

            const Record& B1 = ring[ring_index];
            const Record& B2 = Bbot2[qi];
            int r = (vlow-q < 0);
            if (r) ++r_one_counts[qi];

            int c = carry_base + CARRY_SCALE*r - B1.g - B2.g;
            require(0 <= c && c <= 8, "invalid low carry count");
            ++carry_histogram[qi][c];

            if (q >= 0)
                require(c >= 2, "positive-power carry bound failed");
            else
                require(c >= 1, "negative-power carry bound failed");
            if (q == 0 || q == -1)
                require(c >= 3, "special unit-boundary carry bound failed");

            int y;
            int q_precision;
            if (q > 0) {
                y = qcache[cache_x][q];
                q_precision = 3;
            } else if (q == 0) {
                y = (qcache[cache_x][0] + boundary[0]) % L;
                q_precision = 3; // contact part is known modulo p^3
            } else {
                y = boundary[-q];
                q_precision = 4;
            }

            int zQ = normalize_raw(y, c, 3, q_precision, 1);
            int zA = 0;
            if (q >= 0)
                zA = normalize_raw(acache[cache_x][q], c, 2, 2, 0);

            if (zA == 0 && zQ == 0) continue;

            int unit = unit_base;
            unit = int(i64(unit)*B1.invfact % P2);
            unit = int(i64(unit)*B2.invfact % P2);
            unit = int(i64(unit)*wilson_power[c] % P2);

            int lambda0 = mod(
                harmonic_base - B1.eh - B2.eh
                + r*B1.htop - 6*B2.htop, P
            );
            int lambdaD = mod(Btop.htop-B1.htop, P);
            int lambdaJ = mod(lambdaJ_base+B1.htop, P);

            insert_slot(A[r], zA, unit, lambda0, lambdaD, lambdaJ);
            insert_slot(Q[r], zQ, unit, lambda0, lambdaD, lambdaJ);
        }

        // Checks of the retained natural leading-column identities.
        require(A[1].z % P == 0, "leading A r=1 slot is nonzero");

        if (x > BSTAR) {
            require(A[0].z == 0 && A[0].d == 0 && A[0].j == 0,
                    "exterior A row lost its h-J factor");
        }

        int a_lead = A[0].z % P;
        if (a_lead != 0) {
            require(shape != 1, "leading support in middle shape");
            require(Q[1].z % P == 0, "leading Q r=1 on A support");
            ++support_size;
            support_kappa[shape] =
                (support_kappa[shape]+a_lead*a_lead) % P;
            support_g[shape] =
                (support_g[shape]+a_lead*(Q[0].z % P)) % P;
        }

        // All four ordered pairs are retained.
        for (int r = 0; r <= 1; ++r) {
            for (int s = 0; s <= 1; ++s) {
                int degree = r+s;

                i64 flat =
                    i64(A[r].z)*Q[s].z
                    - i64(inv6_p2)*A[r].z*A[s].z;
                T0[shape][degree] =
                    mod(T0[shape][degree]+flat, P2);

                int ar = A[r].z % P;
                int as = A[s].z % P;
                int qs = Q[s].z % P;

                i64 hd =
                    i64(ar)*Q[s].d + i64(A[r].d)*qs
                    - i64(inv6_p)*(i64(ar)*A[s].d
                                      + i64(A[r].d)*as);
                i64 hj =
                    i64(ar)*Q[s].j + i64(A[r].j)*qs
                    - i64(inv6_p)*(i64(ar)*A[s].j
                                      + i64(A[r].j)*as);

                TD[shape][degree] = mod(TD[shape][degree]+hd, P);
                TJ[shape][degree] = mod(TJ[shape][degree]+hj, P);
            }
        }

        if (x+1 < L) {
            // Full-modulus affine update, including the q=-2 unit slope.
            for (int k = 0; k <= 60; ++k) {
                boundary[k] += slope[k];
                if (boundary[k] >= L) boundary[k] -= L;
            }

            // Exact shift t(x+1,q)=t(x,q+1).
            ++head;
            if (head == NQ) head = 0;
            int last = head + NQ - 1;
            if (last >= NQ) last -= NQ;

            int new_t = BSTAR - (x+1) - QMAX;
            if (new_t < 0) new_t += L;
            ring[last] = record4(new_t);
        }
    }

    require(shape_counts[0] == 191113 &&
            shape_counts[1] == 171762 &&
            shape_counts[2] == 344406, "wrong shape counts");
    require(support_size == 9108, "wrong leading support size");
    require(support_kappa[0] == 11 && support_kappa[2] == 18,
            "kappa cross-check failed");
    require(support_g[0] == 26 && support_g[2] == 3,
            "mixed leading-constant cross-check failed");

    for (int qi = 0; qi < NQ; ++qi) {
        int q = QMIN + qi;
        require(r_one_counts[qi] == u64(19344+q),
                "wrong r=1 count");
        u64 sum = 0;
        for (int c = 0; c <= 8; ++c) sum += carry_histogram[qi][c];
        require(sum == u64(L), "carry histogram is incomplete");
    }

    for (int s = 0; s < 3; ++s)
        for (int v = 0; v < 3; ++v)
            require(T0[s][v] % P == 0,
                    "one of nine flat constants is not divisible by p");

    u64 countA = 0, countQ = 0;
    for (int k = 0; k <= 2; ++k) {
        countA += normalization_counts[0][k];
        countQ += normalization_counts[1][k];
    }
    require(countA == u64(L)*31, "wrong A normalization count");
    require(countQ == u64(L)*91, "wrong Q normalization count");

    std::ofstream out(argv[2]);
    require(bool(out), "cannot open output file");

    out << "{\n";
    out << "  \"format\": \"A2T27v1\",\n";
    out << "  \"input_receipt_sha256\": \"" << receipt_sha << "\",\n";
    out << "  \"rows_processed\": " << L << ",\n";
    out << "  \"Laurent_records\": " << u64(L)*NQ << ",\n";
    out << "  \"all_normalizations_verified\": true,\n";
    out << "  \"all_flat_divisions_verified\": true,\n";
    out << "  \"support_size\": " << support_size << ",\n";
    out << "  \"shape_counts\": ["
        << shape_counts[0] << "," << shape_counts[1] << ","
        << shape_counts[2] << "],\n";
    out << "  \"normalization_counts_by_division_exponent\": [";
    for (int col = 0; col < 2; ++col) {
        if (col) out << ",";
        out << "[" << normalization_counts[col][0] << ","
            << normalization_counts[col][1] << ","
            << normalization_counts[col][2] << "]";
    }
    out << "],\n";

    out << "  \"table\": [\n";
    int row = 0;
    for (int s = 0; s < 3; ++s) {
        for (int v = 0; v < 3; ++v) {
            out << "    [" << T0[s][v] << ","
                << TD[s][v] << "," << TJ[s][v] << "]";
            out << (++row == 9 ? "\n" : ",\n");
        }
    }
    out << "  ],\n";

    out << "  \"carry_histogram_q_minus60_to30\": [\n";
    for (int qi = 0; qi < NQ; ++qi) {
        out << "    [";
        for (int c = 0; c <= 8; ++c) {
            if (c) out << ",";
            out << carry_histogram[qi][c];
        }
        out << "]" << (qi+1 == NQ ? "\n" : ",\n");
    }
    out << "  ]\n";
    out << "}\n";
    require(bool(out), "output write failed");
    return 0;
}
```

### Important implementation distinction

The code skips the *unit multiplication* when both normalized raw coefficients are zero. It does **not** skip their divisibility checks or their carry record. Thus the certificate still covers all prescribed Laurent positions and all normalization obligations.

---

# Part IV. Correctness, bounded work, and expected certificate

## 10. Why this computes the requested table

The correctness argument is finite and explicit.

1. **Positive kernels.**  
   The preparation stage applies the supplied exact reconstruction to the completed Newton vectors. It checks the vanishing of powers $31,\ldots,58$ on every cache residue. The infinite validity of the $841$-cache uses the retained coefficient-period proof, not this finite check alone.

2. **Complete raw boundary.**  
   Formula (5.2), initialized at $x=0$, proves by induction that the boundary state at row $x$ is exactly (5.1) modulo $p^4$. In particular, the $q=-2$ state is not $841$-periodized.

3. **Stripping records.**  
   Equations (2.2) and (3.2)–(3.6) give the same carry, unit, and harmonic data as the six-factorial definition.

4. **Sliding window.**  
   Equation (4.1) proves that the circular array contains the correct $B_{\rm bot1}$ record for every $x,q$.

5. **Normalization.**  
   Each division is checked before use, and the available precision is checked against the required normalized precision.

6. **Slot contraction.**  
   All four ordered pairs $r,s\in\{0,1\}$ are accumulated. These are exactly the definitions of the 27 constants.

7. **Ordinary derivatives.**  
   The finishing stage uses ordinary polynomial coefficient differentiation and checks it against the explicit product rule. No field-function interpolation is used.

Consequently, **if the supplied kernel/reconstruction inputs are valid and the code completes its checks**, its output is the requested universal table and all 25 $\Gamma _0$-values. This statement proves the algorithm’s mathematical meaning; it does not claim its unexecuted output.

---

## 11. Exact local execution request

The coordinator can inspect the two files and then run, explicitly:

```text
python3 universal29.py prepare \
    twenty_nine_kernel_control.json cache29.txt

g++ -O3 -std=c++17 -Wall -Wextra -pedantic \
    pass29.cpp -o pass29

./pass29 cache29.txt table29.json

python3 universal29.py finish \
    table29.json Gamma0_certificate.json
```

No subprocess is launched by the Python utility. No remote operation is requested.

### Exact bounded work

The C++ contraction performs:

- $707281$ actual coordinate rows;
- $91$ Laurent records per row;
- exactly
  

$$
707281\cdot91=64362571
$$


  Laurent records;
- exactly
  

$$
707281\cdot31=21925711
$$


  $A$-normalizations;
- exactly
  

$$
707281\cdot91=64362571
$$


  $Q$-normalizations.

The C++ data structures are comfortably below 1 MiB. No length-$b$ object is allocated.

The Python preparation uses only the $841$-row coefficient cache and bounded-degree integer binomials. A conservative inspection allocation is **one CPU, 256 MiB memory, and a 30-minute wall-time allowance**. That is a proposed resource cap, not a measured benchmark.

### Expected verifiable output

A successful run returns:

1. nine flat residues modulo $841$;
2. eighteen harmonic residues modulo $29$;
3. all nine exact flat divisions by $29$;
4. the ordinary coefficient list of $R_C(D,J)$;
5. all 25 numerical $\Gamma _0(d)$;
6. agreement between ordinary differentiation and product-rule contraction;
7. complete carry histograms and normalization counts;
8. the fixed shape counts
   

$$
(191113,171762,344406);
$$


9. the retained leading-support checks
   

$$
|\mathcal X|=9108,\quad \kappa=(11,18),\quad g=(26,3);
$$


10. input and output hashes.

The expected output is **not specified to be zero**. A failed divisibility or support assertion must be investigated rather than suppressed.

---

# Part V. Original-index reachability and primitive arithmetic

## 12. Every fifth digit is reachable on the original exponent progression

There is a useful unconditional reachability fact that does not require the universal table.

Let


$$
a=432827+682892t,\qquad t\ge0.
$$


Since


$$
682892=28\cdot29^3,
$$


and direct small modular arithmetic gives


$$
3^{28}\equiv436=1+15\cdot29\pmod{29^2},
$$


binomial lifting yields


$$
3^{682892}\equiv1+15\cdot29^4\pmod{29^5}.
$$


Therefore


$$
3^{432827+682892t}
\equiv 3^{432827}(1+15Lt)\pmod{29^5}.
$$


Because $3^{432827}\equiv b_*\equiv27\pmod{29}$,


$$
15b_*\equiv15\cdot27\equiv-1\pmod{29}.
$$



Writing


$$
d(t)=\frac{3^{432827+682892t}-b_*}{L}\pmod{29},
$$


we obtain


$$
\boxed{d(t)=d(0)-t\pmod{29}.}
\tag{12.1}
$$


Thus **every $d=0,\ldots,28$ occurs infinitely often among the original indices**.

The finishing script computes $d(0)$ by the bounded operation


$$
3^{432827}\bmod29^5
$$


and returns the corresponding residue class of $t$ for each requested $d$.

### What this does not prove

It does not establish simultaneous reachability of


$$
T=0,\qquad D_1=0,\qquad U\ne0.
$$


Those quantities retain the higher residual index:


$$
A=69h+67,\qquad h=29H+d,
$$




$$
X_k=\binom Ak\binom{2A+H-k}{H-k},
$$




$$
\mathcal T=\sum_{k=0}^H X_k^2,\qquad
U=\sum_{k=0}^H kX_k^2\pmod{29}.
$$


A nonzero entry in the $\Gamma _0$-table is therefore not automatically an original-family nonzero defect.

---

## 13. Exact consequences of each possible table outcome

On the stated locus, $D\in p^2\mathbb Z_p$. Put


$$
D_2=D/p^2\bmod p,\qquad M_2=M/p^2\bmod p.
$$


Then (1.1) is


$$
\boxed{
M_2-(6C_n)^{-1}D_2=C_nU\Gamma _0(d).
}
\tag{13.1}
$$



### If all 25 values vanish

Then


$$
M_2=(6C_n)^{-1}D_2
$$


throughout the stated original locus, at the retained reconstruction dependencies.

Since $C_n$ is a unit:

- if $D_2\ne0$, then $\delta=\mu=2$;
- if $D_2=0$, then $\delta,\mu\ge3$.

This is third-depth alignment. It is not an all-depth estimate.

### If some value is nonzero

One must still establish an original index with the required locus conditions and $U\ne0$. Even then, a nonzero proportionality defect need not mean that one of $D_2,M_2$ vanishes.

To obtain a next-depth zero-alignment counterexample from (13.1), one would additionally need the appropriate vanishing condition—for example $D_2=0$, in which case a nonzero right-hand side forces $M_2\ne0$.

---

## 14. Final gcd, actual denominator, and whole error

Retain the actual least two-column denominator


$$
N_B=d_B[u,v],\qquad v_{29}(d_B)=0.
$$


With the actual falling metric,


$$
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$


and


$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad
q_n=\frac{A_B}{g_B}>0.
$$


The primitive multiplier is $1/g_B$ on the integer Gram pair, or $d_B^2/g_B$ on the rational Gram pair.

With


$$
F_n=v_{29}(n!),\qquad F_b=v_{29}(b!),\qquad
\delta=v_{29}(D),\quad\mu=v_{29}(M),
$$


the retained exact interface is


$$
\boxed{
v_{29}(g_B)=
\min\{4F_n+4+\delta,\;2F_n+F_b+5+\mu\},
}
$$




$$
\boxed{
v_{29}(q_n)=
\max\{0,\;2F_n-F_b-1+\delta-\mu\}.
}
$$



Norm nonvanishing follows from positivity. Mixed nonvanishing retains its supplied original-family dependency; it is not supplied by this finite calculation.

For the complete real error,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the whole primitive evaluated form remains


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$


The supplied signed-error theorem retains its hypotheses and proof status. Neither a local $29$-adic denominator contribution nor a partial forcing term substitutes for $q_n$ or for this whole evaluated form.

---

# Conclusion

## New result and proof status

The new proved implementation reduction consists of:

- an exact two-digit decomposition of all four-digit stripping records;
- a 91-entry sliding-window algorithm requiring only one new variable stripping record per coordinate;
- a full-modulus affine boundary recurrence preserving the exceptional $q=-2$ insertion;
- a complete single-pass pure-integer implementation of the 27 universal constants;
- a complete ordinary-polynomial reconstruction and two checked calculations of every $\Gamma _0(d)$;
- the original-index reachability formula
  

$$
d(t)=d(0)-t\pmod{29}.
$$



The established $\Gamma _1=0$ and completed kernel vectors are reused.

## Exact remaining bottleneck

**The numerical universal table has not been evaluated in this response.** Running the bounded calculation above is the immediate missing finite result. An unevaluated program is not presented as a completed mixed identity.

If the table vanishes under the functional, the retained reduction proves the stated third-depth relation. If it does not, simultaneous original-index reachability of the residual conditions remains necessary.

Beyond either outcome, the work still lacks all-depth relative valuation control and a global bound for the **actual primitive denominator** strong enough to make the complete nonzero integer linear form tend to zero.

Accordingly, **the irrationality or rationality of $e+\pi$ remains unresolved by this work.**
