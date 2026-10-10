> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 221 — Frobenius resonance and twisted cohomology in the fixed $j=2$ cell

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain only the Item 219 cell



$$
4m+1=5p-2s,\qquad 1\le s\le\frac{p-3}{6},\qquad
 s\equiv\frac{p-1}{2}\pmod2,\qquad p\ge11,           \tag{1.1}
$$



and put



$$
r=\frac{p-6s-3}{2},\qquad
 f_0(z)=z^r(1-z)^r(1+z)(1+z^2)^{2s},                \tag{1.2}
$$





$$
f_1(z)=z^r(1-z)^r(1+z)^4(1+z^2)^{2s-1},\qquad
 \frac{f_1}{f_0}=\frac{(1+z)^3}{1+z^2}.             \tag{1.3}
$$



This item studies exactly the two mechanisms left open by Item 219.  It
does not combine $j=2$ with another cell.

> **PROVED — the first Frobenius-resonant scalar term is forced away by
> the common gate.**  Let $F'_\nu=f_\nu$, $F_\nu(0)=0$, and suppose
> 

$$
>       K=F_1-RF_0+c z^p                              \tag{1.4}
>
$$


> vanishes at $1,i,-i$.  For both phases
> $\chi=(-1)^{(p-1)/2}=\pm1$, the Item 219 path functional has
> 

$$
> \mathcal L_\chi(z^p)=7.                             \tag{1.5}
>
$$


> Hence the common-log equations
> $\mathcal L_\chi(F_0)=\mathcal L_\chi(F_1)=0$
> force $7c=0$, so $c=0$.  Item 219's unit minor then excludes the
> remaining nonresonant scalar reduction.  Thus a single $z^p$
> resonance cannot close or evade the scalar obstruction on any
> admissible row.

> **PROVED — exact non-scalar contiguity reduction.**  In $\mathbb F_p(z)$,
> 

$$
>              f_1(z)\,dz=d(Hf_0)+Q(z)f_0(z)\,dz,    \tag{1.6}
>
$$


> where
> 

$$
> H(z)=\frac{(10s-3)z+2z^2-(10s+1)z^3+2z^4}
>            {2s(10s-1)(1+z)},                       \tag{1.7}
>
$$


> and
> 

$$
> Q(z)=\frac{100s^2-12s-3+(10-4s)z+(8s-4)z^2}
>            {4s(10s-1)}.                            \tag{1.8}
>
$$


> Every displayed denominator is a unit on (1.1).  In particular,
> $p\mid10s-1$ is impossible by the exact bound-and-parity argument in
> Section 2.

> **PROVED — the quadratic remainder is a genuine cohomology barrier.**
> The three forms
> 

$$
>                  f_0\,dz,\qquad zf_0\,dz,\qquad z^2f_0\,dz           \tag{1.9}
>
$$


> are linearly independent modulo boundary-free sub-Frobenius exact
> forms.  An explicit $8\times8$ coefficient minor is
> 

$$
>          36864s^2(2s+1)^2(10s-1),                  \tag{1.10}
>
$$


> a unit on every admissible row.  Therefore (1.8) cannot be reduced to
> a scalar or linear remainder by first-order boundary-free Hermite
> reduction of this degree.

> **PROVED — one-polynomial reduced common gate.**  Let
> $T_k=\mathcal L_\chi(\int_0^\bullet z^kf_0(z)\,dz)$ for
> $k=0,1,2$.  Then
> 

$$
> 4s(10s-1)S_1=(100s^2-12s-3)T_0+(10-4s)T_1+(8s-4)T_2, \tag{1.11}
>
$$


> while $S_0=T_0$.  Consequently the $j=2$ common-log condition is
> exactly
> 

$$
> \boxed{T_0=0,\qquad (5-2s)T_1+2(2s-1)T_2=0.}       \tag{1.12}
>
$$


> Unlike Item 219's two different polynomials $P_0,P_1$, (1.12) uses
> three shifted periods of the single polynomial $f_0$.

> **EXACT FINITE ONLY.**  The replay verifies (1.11) on all 1,153
> admissible rows through $p\le401$, with the same five separate
> $T_0$-zeros, six separate $S_1$-zeros, and no common zero.  This is
> not an all-prime or density theorem.

> **OPEN.**  No all-prime nonvanishing theorem is proved for (1.12).
> Higher polynomials in $z^p$, non-polynomial remainders, and arithmetic
> control of the genuine two-period residual remain open.  Thus Item 221
> books no common-log capacity reduction and proves nothing about
> $e+\pi$.

## 2. The complete unit audit

Item 219 proved



$$
r\ge1,\qquad 1\le2s+1<p.          \tag{2.1}
$$



It remains to audit $10s-1$.  The cell bound gives



$$
0<10s-1<2p.                            \tag{2.2}
$$



If $p\mid10s-1$, equations (2.2) force



$$
p=10s-1.                    \tag{2.3}
$$



But then



$$
\frac{p-1}{2}=5s-1\equiv s-1\pmod2,                \tag{2.4}
$$



contradicting the admissibility condition
$s\equiv(p-1)/2\pmod2$.  Hence



$$
p\nmid 2\cdot3\cdot7\cdot s(2s+1)(10s-1) \tag{2.5}
$$



on every row.  This audits (1.5), (1.7), (1.8), and the minors below.

## 3. The path functional and the first $z^p$ resonance

Work in $\mathbb F_p[i]$, $i^2=-1$, and put



$$
\chi=(-1)^{(p-1)/2},\qquad
 \mathcal L_\chi(U)=9U(1)+(-10+\chi i)U(i)
                         +(-10-\chi i)U(-i).          \tag{3.1}
$$



Item 219's exact all-prime reduction is



$$
S_\nu=\mathcal L_\chi(F_\nu),      \tag{3.2}
$$



up to the common nonzero normalization
$-35(-1)^{r+1}$.  Since



$$
i^p=\chi i,\qquad (-i)^p=-\chi i,                  \tag{3.3}
$$



direct substitution gives



$$
\begin{aligned}
 \mathcal L_\chi(z^p)
 &=9+(-10+\chi i)\chi i+(-10-\chi i)(-\chi i)\\
 &=9+(-10\chi i-1)+(10\chi i-1)=7.                 \tag{3.4}
\end{aligned}
$$



This calculation retains both $p\bmod4$ phases; no choice of a square
root of $-1$ in $\mathbb F_p$ is assumed.

Now let (1.4) vanish at all three terminal points.  Applying
$\mathcal L_\chi$ and using the common gate gives



$$
0=S_1-RS_0+7c=7c.                                  \tag{3.5}
$$



Equation (2.5) yields $c=0$.  The remaining primitive
$F_1-RF_0$ is below Frobenius degree and boundary-free, exactly the
scalar ansatz excluded by Item 219's determinant
$2304s(2s+1)^2$.  This proves the first theorem in Section 1.

The scope matters.  A general polynomial $C(z^p)$ can contain several
independent endpoint phases.  Equation (3.5) treats the first resonant
term $cz^p$, not arbitrary higher $z^{kp}$ terms.

## 4. Exact quadratic contiguity

Logarithmic differentiation gives



$$
\frac{f'_0}{f_0}
 =\frac rz-\frac r{1-z}+\frac1{1+z}
    +\frac{4sz}{1+z^2}.                              \tag{4.1}
$$



In characteristic $p$, the cell relation is



$$
r=-3s-\frac32.                \tag{4.2}
$$



Substitute (1.7)--(1.8) into



$$
H'+\frac{f'_0}{f_0}H
       =\frac{(1+z)^3}{1+z^2}-Q(z).                 \tag{4.3}
$$



Clearing
$4s(10s-1)z(1-z)(1+z)^2(1+z^2)$ leaves the zero
polynomial in $z,s$.  Thus (4.3), and hence (1.6), is an exact
finite-field identity rather than a guessed contiguity relation.

The boundary term is



$$
Hf_0=\frac{(10s-3)z+2z^2-(10s+1)z^3+2z^4}
              {2s(10s-1)}
        z^r(1-z)^r(1+z^2)^{2s}.                     \tag{4.4}
$$



It vanishes at $0,1,i,-i$ because $r\ge1$ and $s\ge1$.
Integrating (1.6) along the three paths therefore gives (1.11) directly.

For a coefficient-only formula, write



$$
(1-z)^r(1+z)(1+z^2)^{2s}=\sum_\ell p_\ell z^\ell \tag{4.5}
$$



and retain Item 219's four-phase weight



$$
\begin{array}{c|rrrr}
 n\bmod4&0&1&2&3\\ \hline
 W_\chi(n)&-11&9-2\chi&29&9+2\chi.
\end{array}                                          \tag{4.6}
$$



Then



$$
T_k=\sum_\ell p_\ell
       \frac{W_\chi(r+\ell+k+1)}{r+\ell+k+1}\pmod p,
 \qquad k=0,1,2.                                    \tag{4.7}
$$



The largest denominator in (4.7) is $p-2s+1\le p-1$, so (4.7) has
no hidden zero denominator.  Combining (1.11) with $S_0=T_0$ and the
unit audit proves (1.12).

## 5. The three-dimensional cohomology quotient is genuine

Suppose a quadratic form is boundary-free exact below Frobenius degree:



$$
d(Hf_0)=(q_0+q_1z+q_2z^2)f_0(z)\,dz.              \tag{5.1}
$$



The same endpoint-multiplicity argument as in Item 219 forces



$$
H=\frac{c_0+c_1z+c_2z^2+c_3z^3+c_4z^4}{1+z}.      \tag{5.2}
$$



After substituting (4.1)--(4.2), the coefficient matrix for
$(c_0,c_1,c_2,c_3,c_4,q_0,q_1,q_2)$ is



$$
M_s=
\begin{pmatrix}
-6s-3&0&0&0&0&0&0&0\\
6s+3&-6s-1&0&0&0&-2&0&0\\
14s+3&6s+3&1-6s&0&0&-2&-2&0\\
6s+3&14s+3&6s+3&3-6s&0&0&-2&-2\\
4s+6&6s+3&14s+3&6s+3&5-6s&0&0&-2\\
0&4s+4&6s+3&14s+3&6s+3&2&0&0\\
0&0&4s+2&6s+3&14s+3&2&2&0\\
0&0&0&4s&6s+3&0&2&2\\
0&0&0&0&4s-2&0&0&2
\end{pmatrix}.                                       \tag{5.3}
$$



The determinant of the first eight rows is exactly (1.10).  By Section
2 it is a unit, so $M_s$ has column rank eight.  Equation (5.1)
therefore has only the zero solution.  This proves both the independence
of (1.9) and the uniqueness of the quadratic remainder (1.8).

The conclusion is a method barrier, not an impossibility theorem for the
common gate: after imposing $T_0=0$, equation (1.12) remains one
arithmetic relation between two genuinely independent period
coordinates.  Exact first-order reduction cannot eliminate that last
projective coordinate.

## 6. Deterministic replay and status ledger

The standard-library checker

`scripts/item221_j2_twisted_cohomology_certificate.py`

performs the following exact tasks.

1. It verifies (4.3) symbolically as a bivariate rational identity using
   exact rational arithmetic.
2. It expands the $8\times8$ determinant in (5.3) and checks the full
   factorization (1.10).
3. It evaluates (3.4) independently for $\chi=1$ and $\chi=-1$.
4. It imports the frozen Item 219 polynomial/weight routines and verifies
   (1.11)--(1.12) on every scanned row.
5. It records the finite separate zeros and a SHA-256 digest of all
   $(T_0,T_1,T_2,S_1)$ rows.

The canonical and replay JSON are required to be byte-identical.  The
checker contains no host path, timestamp, random seed, elapsed time, or
non-standard package dependency.

### PROVED

- The first $z^p$ scalar resonance is forced to vanish under the common
  gate and then falls under Item 219's scalar no-go.
- The exact quadratic contiguity identity (1.6)--(1.8), including every
  denominator unit.
- The all-row cohomology independence minor (1.10).
- The one-polynomial reduced gate (1.12).

### EXACT FINITE ONLY

- The 1,153-row replay through $p\le401$, its separate zeros, and its
  absence of a common zero.

### OPEN

- All-prime nonvanishing of the two-period gate (1.12).
- Higher polynomials in $z^p$, higher-degree or non-polynomial
  cohomology mechanisms, and any arithmetic theorem controlling the last
  projective period coordinate.
- Any reduction of the common-log capacity ceiling.
- Any conclusion about $e+\pi$.
