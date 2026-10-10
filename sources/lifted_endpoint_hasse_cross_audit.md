> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent cross-audit of the lifted endpoint Hasse-band package

Date: 2026-08-28

## Verdict

No mathematical or normalization flaw was found in
`work/lifted_endpoint_hasse_formula.md`,
`work/lifted_endpoint_hasse_certificate.py`, or
`work/lifted_endpoint_hasse_certificate_m30.json`.

The band formula is an exact regrouping of the partial-fraction endpoint
sum, the modulus and valuation indices are correct in both normalization
branches, the Gaussian root algebra is handled correctly, and the
$(m,p)=(6,7)$ lower-band counterexample independently reproduces.

Two scope clarifications are advisable but do not change the theorem:

1. “The top band does not determine $\eta$” is proved for the literal
   top-band truncation.  The example does not exclude a separate identity
   special to the actual $m$-family that reconstructs the omitted band
   from top-band data plus additional information.
2. The archived $m\le30$ JSON exercises band indices $h=0,1$ only.  It
   does not exercise the possible rank-zero $h=2$ band.  The proof covers
   that band, and a separate exact spot check at $(m,p)=(46,11)$, where
   $(e,\delta)=(2,1)$, finds band indices $0,1,2$ and agreement with the
   frozen coordinate.

The result remains a formula for the next digit, not a positive-mass
vanishing theorem.

## 1. Files audited

At the time of audit:

```text
d1b0a3804e5e0097f7939d88c00ebfb0414dc413f6a55d2bbc4da6e89ea8f211  work/lifted_endpoint_hasse_formula.md
0408acbd448b81a00092ece49c4aa6513fc815c1ecd0bf72df882ea060001c65  work/lifted_endpoint_hasse_certificate.py
54025499d507749259d7d52a231f5594a77885bf0bf1ee0df747d94d86afde3c  work/lifted_endpoint_hasse_certificate_m30.json
```

An independent rerun with `--max-m 30` was byte-identical to the staged
JSON and had zero mismatches on all 118 rows.

## 2. Partial fractions and endpoint signs

At a root $\alpha\in\{-1,i,-i\}$, put



$$
Q(x)=(x-\alpha)Q_\alpha(x),\qquad x=\alpha+t.
$$



Then



$$
{u(x)^N\over Q(x)^{K_s}}
=t^{-K_s}{u(\alpha+t)^N\over Q_\alpha(\alpha+t)^{K_s}},
$$



so the coefficient of $(x-\alpha)^{-j}$ is exactly



$$
C_{s,\alpha}(K_s-j).
$$



The numerator degree is $12m$, while the denominator degrees are
$12m+3$ and $12m+6$; hence there is no polynomial quotient.

For $j=n+1\ge2$, direct integration gives



$$
\int_0^1{dx\over(x-\alpha)^{n+1}}
={(-\alpha)^{-n}-(1-\alpha)^{-n}\over n}.
$$



This confirms the sign and the coefficient index in formula (3.2).  The
simple-pole integrals give



$$
L_s=4C_{s,-1}(K_s-1)+2C_{s,i}(K_s-1)
                     +2C_{s,-i}(K_s-1),
$$



so the determinant convention



$$
qA_m=L_1(qR_0)-L_0(qR_1)
$$



also has the stated sign.

## 3. Root-field audit

The displayed local expansions are correct:



$$
\begin{array}{c|c|c}
\alpha&u(\alpha+t)&Q_\alpha(\alpha+t)\\ \hline
-1&-2+3t-t^2&2-2t+t^2\\
i&1+i+(1-2i)t-t^2&-2+2i+(1+3i)t+t^2.
\end{array}
$$



The $-i$ row is the Gaussian conjugate.  For every odd $p$, all constant
terms and endpoint factors that are inverted have norm a power of two, hence
are units in the etale algebra $(\mathbb Z/p^a\mathbb Z)[i]$.  This remains
true when $p\equiv1\pmod4$ and the algebra splits.  The script's
norm-inverse implementation is therefore valid in every audited branch.

Conjugate local terms cancel their imaginary parts.  Both the modular replay
and an independent exact Gaussian-rational calculation give rational band
sums.

## 4. Band indices and required precision

Every endpoint denominator index satisfies



$$
1\le n\le K_s-1\le4m+1<pq,
$$



where $q=p^e$ is the largest $p$-power at most $4m+1$.  Thus
$v_p(n)\le e$.  Writing



$$
n=p^v k,\qquad p\nmid k,
$$



gives



$$
{q\over n}={p^{e-v}\over k}.
$$



With $h=e-v$, all terms with $h\ge D+1$ vanish modulo $p^{D+1}$,
because every local Hasse coefficient and endpoint factor is $p$-integral.
The retained indices are therefore exactly



$$
h=0,\ldots,\min(e,D),
$$



corresponding to denominator-index bands



$$
q,\ q/p,\ldots,q/p^D.
$$



This proves the stated endpoint congruence



$$
qR_s\equiv\sum_{h=0}^{\min(e,D)}p^h\mathcal B_{s,h}
\pmod {p^{D+1}}.
$$



The local series need only be known modulo $p^{D+1}$; multiplication by
the integral $L_s$ loses no precision.

For $\delta=0$, $D=1$.  Item 149 or 151 gives
$v_p(qA_m)\ge1$, so division modulo $p^2$ returns



$$
\eta_{m,p}=qA_m/p\pmod p.
$$



For $\delta=1$, $D=2$.  The already removed squarefree $G_m$-factor
means the proved starting valuation is $v_p(qA_m)\ge2$; the next digit is



$$
\eta_{m,p}=qA_m/p^2\pmod p,
$$



so the bracket must be computed modulo $p^3$.  These are exactly the
indices and moduli used in the note and script.

## 5. Clearing and determinant normalization

For a forced prime $p<2m$, one has $p\nmid T_m$.  Write



$$
D_m^\sharp=q\,d_p,\qquad G_m=p^\delta g_p,
$$



with $d_p,g_p$ $p$-adic units.  Since



$$
U_m={D_m^\sharp A_m\over G_m},
$$



exactly



$$
{qA_m\over p^{1+\delta}}
={U_m\over p}\,{g_p\over d_p}.                              \tag{5.1}
$$



The certificate's `expected_eta_from_u` implements (5.1):
`g_unit` is $g_p$ and `clearing_unit` is $d_p$.  The dyadic clearing is
a unit at odd $p$, and the middle-prime product is excluded correctly.
No copy of $G_m$ is counted twice.

## 6. Independent $(6,7)$ replay

An exact rational Hermite reduction from the frozen item-140 generator,
independent of the builder's local-series code, gives



$$
L_0\equiv14,\qquad L_1\equiv5\pmod {49},
$$



and



$$
v_7(7A_6)=1,\qquad {7A_6\over7}\equiv4\pmod7.
$$



A second independent computation using exact Gaussian rational numbers,
rather than modular series arithmetic, gives



$$
\begin{array}{c|cc|c}
&\mathcal B_{s,0}&7\mathcal B_{s,1}&7R_s\\ \hline
s=0&42&21&14\\
s=1&10&28&38
\end{array}
\qquad(\bmod49).
$$



Therefore the literal top-band truncation gives



$$
7^{-1}(5\cdot42-14\cdot10)\equiv3\pmod7,
$$



while the complete formula gives



$$
7^{-1}(5\cdot14-14\cdot38)\equiv4\pmod7.
$$



The counterexample and all signs are correct.

## 7. Third-band coverage spot check

The staged $m\le30$ JSON reports only band indices $0,1$.  The first
available rank-one row with $\delta=1,e=2$ is $(m,p)=(46,11)$, where
$q=121$.  A separate exact run gives

```text
eta = 0
expected_eta_from_frozen_U = 0
bands for both endpoints = [0, 1, 2]
```

Thus the possible $q/p^2$ band is exercised successfully outside the
staged window.  This is a finite normalization check only; the uniform
justification is the valuation grouping in Section 4.

## 8. Final classification

- **PROVED:** the partial-fraction identity, endpoint signs, Hasse-band
  grouping, modulus $p^{2+\delta}$, determinant normalization, and the
  $(6,7)$ top-only counterexample.
- **EXPERIMENTAL:** 118-row counts, the number of changed or zero digits,
  and the isolated $(46,11)$ third-band check.
- **OPEN:** a positive weighted-mass theorem for zeros of the complete
  Hasse determinant.

The package is mathematically sound within its stated scope and does not
decide the status of $e+\pi$.
