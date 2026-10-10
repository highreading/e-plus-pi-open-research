> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the fixed-gap Möbius/order-three package

Date: 2026-08-28

## 1. Files audited

This audit is independent of the construction of the staged package and is
bound to the following exact SHA-256 hashes:

```text
5947a154c6eb45d673ab41e43c29e784fbe3aff3345adb2353be03cebe487e72  mobius_order3_fixed_gap_analysis.md
c97088afcd0ad813c336c6df621f6a364cb29d89a39c1ed7589c9def24acf2fe  mobius_order3_fixed_gap_certificate.py
df54b3628fa26941f7ac9a31deae38314c416e1f24b4f0db996757c39d524a7b  mobius_order3_fixed_gap_certificate_q301.json
```

The certificate was run twice with `--max-q 301`.  Both regenerated files
were byte-for-byte identical to one another and to the staged JSON; all three
had SHA-256

```text
df54b3628fa26941f7ac9a31deae38314c416e1f24b4f0db996757c39d524a7b.
```

## 2. Endpoint and Kummer identities

I independently expanded the two endpoint series.  For



$$
\omega_s={(1+t)^{1+3s}(1+t^2)^{\alpha-s}\over
 t^q(1-t)^q}\,dt,
 \qquad \alpha={2q-3\over3},
$$



the residue at zero is exactly $T_s$.  Under
$\phi(z)=z/(z+2)$, followed by $\iota(z)=2/z$, the powers of
$z$ and 2 reduce respectively to $z^{-q}$ and $-2^0$.  Comparing
with the defining differential for $C_s$ gives



$$
\gamma_s=-2^{-\alpha}\iota^*\phi^*\omega_s,
 \qquad
 C_s=-2^{-\alpha}\operatorname {Res}_{t=1}\omega_s.
$$



The final note now correctly synchronizes the value
$a=2^\alpha$ with this continuation.  Therefore, if
$X^3=4^{q-1}$ and $\xi=X/a$, then



$$
\xi^3=2,
 \qquad
 XC_s-T_s=-\left(\operatorname {Res}_0\omega_s+
 \xi\operatorname {Res}_1\omega_s\right).
$$



The contiguity quotient was also checked directly:



$$
{\omega_{s+1}\over\omega_s}={(1+t)^3\over1+t^2}.
$$



On $y^3=1+t^2$, this is $((1+t)/y)^3$, and every row has the
same deck character $\zeta^{2q-3}$.  The relative endpoint weight
$\xi$ is not that deck eigenvalue, as the note states.

## 3. Inverse-cubic bridge

For $S=2/(1+t)$, so that $t=(2-S)/S$ and
$dt=-2S^{-2}dS$, direct substitution gives



$$
1+t={2\over S},\qquad
 1+t^2={2(S^2-2S+2)\over S^2},
$$



and hence, with
$\Phi(S)=S(S^2-2S+2)$ and
$A_0(S)=(S-1)(2-S)$,



$$
{(1+t)^3\over1+t^2}={4\over\Phi(S)},
$$





$$
\omega_s=-2^{1+2s-q/3}
 {\Phi(S)^{\alpha-s}\over A_0(S)^q}\,dS.
$$



The endpoint correspondence is exactly $t=0,1\leftrightarrow S=2,1$.
Thus equations (3.6)--(3.8) are a valid coordinate bridge to the existing
inverse cubic, without asserting a new order-three closure.

## 4. Möbius classifications

A map preserving $\{0,\infty\}$ is $cz$ or $c/z$.  The condition
$-1\mapsto-2$ leaves $2z$ and $2/z$; only $2/z$ maps
$\{-2,-1+i,-1-i\}$ to $\{-1,-1+i,-1-i\}$.  Hence the actual
coefficient reflection is uniquely the projective involution $2/z$.
The positive-multiplicity divisor argument is now correctly restricted to
$q\ge5$, while the algebraic pullback identity remains valid for $q=1$.

For



$$
\sigma(t)={it+3\over t+i},\qquad
 M_\sigma=\begin{pmatrix}i&3\\1&i\end{pmatrix},
$$



I checked $M_\sigma^3=8iI$,



$$
1+\sigma(t)^2={8i(1+t^2)\over(t+i)^3},
$$



the branch cycle $i\mapsto-i\mapsto\infty\mapsto i$, and the endpoint
orbits



$$
\{0,-3i,3i\},\qquad \{1,2-i,2+i\}.
$$



The corrected wording is exact: closing under the full $\sigma$-orbit
adds four endpoints.  Since the stabilizer of a three-point branch set is
$S_3$, its only nonidentity order-three elements are
$\sigma^{\pm1}$; neither preserves $\{0,1\}$.

## 5. Pochhammer claim and theorem boundary

The identity



$$
P_q=\prod_{j=0}^{q-2}(2q-3-3j)
 =3^{q-1}(q-1)!\binom{(2q-3)/3}{q-1}
$$



is exact.  If a prime $\ell\nmid6P_q$ satisfied $\ell\le q-1$, the
indices $0,\ldots,q-2$ would contain a representative of
$\alpha\pmod\ell$, contradicting $\ell\nmid P_q$.  Thus
$\ell>q-1$, so the listed factorial and Pochhammer factors are units.
The note correctly labels this as necessary nonresonance, not as the
missing jet reduction.

## 6. Verdict

All claimed exact identities, finite certificate assertions, corrected
scope qualifications, and theorem/evidence boundaries passed this audit.
The package proves a structural endpoint/Kummer reduction and a no-go for
the tempting order-three PSL2 shortcut.  It does **not** prove
$d_3(q)\mid P_q$, and it does not claim to.

The three hash-bound staged files are safe to freeze as item 159 with this
status.  No archive files were modified during this audit.
