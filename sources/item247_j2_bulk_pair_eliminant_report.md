> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 247 — A unit-determinant eliminant for the two $j=2$ bulk residuals

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

This item studies simultaneous vanishing of the two canonical Item 244
bulk residuals



$$
\mathsf B_\nu=\mathcal B_L[D_\nu],\qquad \nu=0,1,                 \tag{1.1}
$$



using the exact Item 246 functional $\mathcal B_L$.

Throughout this report



$$
r=r_{(j=2)}=\frac{p-6s-3}{2}                                    \tag{1.2}
$$



is the exponent in the **Item 244 fixed $j=2$ parameterization**.
It is not the parameter called $r$ in the separate $j=1$ branch.
In particular, the parity statement below creates no cross-branch
constraint on the $j=1$ parameter.

> **PROVED — unit common-state determinant.**  If
> $F=P_0/(1+z^2)$ has selected parity $A$ and companion parity
> $C$, put
> 

$$
> X=\mathcal B_L[A],\quad Y=\mathcal B_L[tA],\quad
> Z=\mathcal B_L[(3+t)C].
>
$$


> Then
> 

$$
> \binom{\mathsf B_0}{\mathsf B_1-Z}
> =\begin{pmatrix}1&1\\1&3\end{pmatrix}\binom{X}{Y},
> \qquad \det=2.                                      \tag{1.3}
>
$$


> Thus the common $A$-state has no singular locus in the admissible
> odd characteristics.

> **PROVED — exact one-seed eliminant.**  Actual $j=2$ admissibility
> forces the Item 244 exponent $r$ to be odd.  Put
> 

$$
> R=r-1,\qquad G(t)=(1-t)(1+t)^{2s-1},
> \qquad (1-z)^R=E(z^2)-zO(z^2).                     \tag{1.4}
>
$$


> For $R>0$, both coordinate polynomials and the eliminated residual
> reduce to the single odd seed $O$:
> 

$$
> \boxed{
> \begin{aligned}
> D_0&=-G(1+t)O,\\
> R D_1&=G\{[3-R-2t+(R-1)t^2]O
>       +2t(1-t)(3+t)O'\},\\
> R(\mathsf B_1-3\mathsf B_0)&=\mathcal B_L[GJ_R(O)],
> \end{aligned}}                                      \tag{1.5}
>
$$


> where
> 

$$
> J_R(O)=[2R+3+(3R-2)t+(R-1)t^2]O
>       +2t(1-t)(3+t)O'.                              \tag{1.6}
>
$$



> **PROVED — exact singular locus of this elimination.**  The two
> displayed elimination steps have block determinant
> 

$$
> \boxed{2R=2(r-1).}                                  \tag{1.7}
>
$$


> It is a $p$-unit on every regular actual row.  Its only singular
> locus is $r=1$, where
> 

$$
> D_0=0,\qquad D_1=(1-t)(1+t)^{2s-1}(3+t).            \tag{1.8}
>
$$


> This classifies the algebraic elimination singularity; it does not
> classify modular zeros of the remaining scalar in (1.8).

> **PROVED — canonical arithmetic content criterion.**  A single
> common denominator clears both rational functionals.  The resulting
> integer pair $(I_0,I_1)$ satisfies
> 

$$
> \boxed{
> \mathsf B_0=\mathsf B_1=0\pmod p
> \iff p\mid\gcd(I_0,I_1).}                          \tag{1.9}
>
$$


> This is an exact moving-prime criterion, not an all-prime
> nonvanishing theorem.

> **SCOPED CONCLUSION.**  The suggested common-state and companion
> eliminations are now exact and nonsingular away from the completely
> classified line $r=1$.  They reduce the problem to two explicit
> scalar functionals of one seed.  No factorization of their arithmetic
> content, Bezout unit, or all-prime simultaneous nonvanishing theorem
> is proved.

> **GLOBAL INTERFACE / BOOKING.**  These bulk residuals occur only in
> the stronger Item 239 $p^3$ carry.  Item 247 does not strengthen the
> ordinary $p^2$ common-log gate and books no rate or capacity.

## 2. The actual (j=2) locus

The Item 239/244 admissible rows satisfy



$$
p\ge17\text{ prime},\qquad s\ge2,\qquad
 s\le\frac{p-3}{6},\qquad 5p-2s-1\equiv0\pmod4.     \tag{2.1}
$$



Substitution of $p=2r+6s+3$ gives



$$
5p-2s-1=2(5r+14s+7).                                \tag{2.2}
$$



Consequently the last congruence is equivalent to $r$ odd.  The
inequality in (2.1) gives $r\ge0$, hence every actual row has
$r\ge1$ odd and $L=(r+1)/2$.

The value $r=3$ would give



$$
p=6s+9=3(2s+3)>3,                                   \tag{2.3}
$$



which is composite.  Thus every regular prime row has $r\ge5$.

The singular line $r=1$ is not formal or empty.  It gives
$p=6s+5$.  For every $s\ge2$ for which this number is prime,
$p\ge17$, the upper bound in (2.1) holds with
$\lfloor(p-3)/6\rfloor=s$, and



$$
5p-2s-1=4(7s+6).                                    \tag{2.4}
$$



Hence all original admissibility conditions are satisfied.

## 3. Eliminating the common (A)-state

Because actual rows have odd $r$, the Item 246 pair relation is



$$
D_0=(1+t)A,\qquad D_1=(1+3t)A+(3+t)C.              \tag{3.1}
$$



Linearity of $\mathcal B_L$ gives (1.3).  Its determinant is the
fixed unit $2$, so



$$
\mathsf B_0=\mathsf B_1=0
 \iff
 \mathsf B_0=0\quad\text{and}\quad
 \mathcal E:=\mathsf B_1-3\mathsf B_0=0.            \tag{3.2}
$$



Moreover



$$
\mathcal E=Z-2X.                                    \tag{3.3}
$$



This is the exact scalar elimination of the common $tA$-state.  It
does not assert that $\mathcal E$ is nonzero.

## 4. Eliminating the companion parity

For odd $r$, factor



$$
F(z)=(1-z)^r(1+z)(1+z^2)^{2s-1}
     =G(z^2)(1-z)^R.                                 \tag{4.1}
$$



With the convention (1.4), the selected odd and companion even
parities are



$$
A=-GO,\qquad C=GE.                                  \tag{4.2}
$$



Differentiate $(1-z)^R=E(z^2)-zO(z^2)$.  Since
$f'/f=-R/(1-z)=-R(1+z)/(1-t)$, comparison of even parts gives



$$
(1-t)(O+2tO')=R(E-tO).
$$



Rearrangement yields the polynomial identity



$$
\boxed{
 R E=[1+(R-1)t]O+2t(1-t)O'.}                        \tag{4.3}
$$



Substitution of (4.2)--(4.3) into (3.1) proves the first two lines of
(1.5).  Equations (3.3) and (4.2) also give



$$
\mathcal E
 =\mathcal B_L\!\left[G\{(3+t)E+2O\}\right].       \tag{4.4}
$$



Multiplying (4.4) by $R$ and using (4.3) proves (1.6).

For clarity, the determinant in (1.7) is the determinant of the block
elimination matrix



$$
\mathscr M_R=
 \operatorname{diag}\!\left(
 \begin{pmatrix}1&1\\1&3\end{pmatrix},R\right),
 \qquad \det\mathscr M_R=2R.                        \tag{4.5}
$$



It records exactly the divisions used in eliminating the common state
and then $E$.  Since $0<R<p$ on a regular row, (4.5) is invertible
modulo $p$.  This is not the determinant of the two final scalar
functionals and therefore does not by itself prohibit their joint
vanishing.

The Item 246 factor and seed recurrences evaluate both terms in (3.2)
without full expansion.  Thus (3.2), (1.5), and (1.6) are the requested
finite symbolic eliminant for the actual pair.

## 5. The singular line $r=1$

Here $R=0$, $E=1$, and $O=0$.  Equations (4.1)--(4.2) give
$A=0$, $C=G$, hence (1.8).  Simultaneous vanishing reduces exactly
to the one moving-prime condition.  Here $L=1$, so it is



$$
\mathcal B_1\!\left[(1-t)(1+t)^{2s-1}(3+t)\right]
 \equiv0\pmod {6s+5}.                                \tag{5.1}
$$



No all-prime classification of (5.1) is proved.  The extended finite
scan in Section 7 is evidence only.

## 6. A common-denominator arithmetic content

Let $d=\max(\deg D_0,\deg D_1)=\deg D_1$ and



$$
N_k=2(L+k)+1,\qquad
 Q=\prod_{k=0}^{d}N_k,\qquad
 I_\nu=Q^2\mathcal B_L[D_\nu].                       \tag{6.1}
$$



Every summand in the Item 246 triangular formula has denominator
$N_kN_v$, so $I_0,I_1\in\mathbb Z$.  Here



$$
d=L+2s,\qquad N_d=2r+4s+3<p=2r+6s+3.               \tag{6.2}
$$



Thus $Q$ is a $p$-unit, and multiplying both residuals by $Q^2$
proves (1.9).  The integer



$$
\mathscr C_{r,s}:=\gcd(I_0,I_1)                    \tag{6.3}
$$



is the canonical content, or first Smith invariant, of the cleared
two-entry row.  Classifying simultaneous bulk zeros is exactly the
moving-prime divisibility problem $p\mid\mathscr C_{r,s}$.  Calling
it a content avoids claiming a polynomial resultant factorization that
has not been proved.

## 7. Exact witnesses and finite evidence

Through $p\le401$, the full pair replay has 1,115 admissible rows:



$$
\begin{array}{c|r}
\text{quantity}&\text{count}\\ \hline
r=1\text{ singular rows}&38\\
r>1\text{ regular rows}&1077\\
\text{separate nonempty coordinate zeros}&6\\
\mathcal E=0&4\\
\mathsf B_0=\mathsf B_1=0&0.
\end{array}                                           \tag{7.1}
$$



In particular, the eliminated scalar is not universally nonzero.  At
$(p,s)=(127,11)$,



$$
(\mathsf B_0,\mathsf B_1,\mathcal E)=(97,37,0)\pmod {127},        \tag{7.2}
$$



and indeed $37=3\cdot97\pmod {127}$.  This is an exact counterexample
to treating the unit determinant as a nonvanishing theorem.

The exact rational content replay through $p\le101$ has 74 rows and
no moving prime dividing $\mathscr C_{r,s}$.  Separately, the direct
singular-line recurrence checks all 1,134 primes $p=6s+5\le20000$
and sees no zero in (5.1).  Both statements are strictly finite.

## 8. Replay, status, and booking

The standard-library checker
`item247_j2_bulk_pair_eliminant_certificate.py`:

1. reconstructs the actual selected and companion parity polynomials;
2. verifies the common-state matrix and its determinant;
3. verifies the parity differential identity and one-seed eliminant;
4. checks the regular and singular loci under the original admissibility
   conditions;
5. constructs and verifies the common-denominator content criterion; and
6. produces separately labelled full-pair, rational, and singular-line
   finite censuses.

From the archive root, run:

    python scripts/item247_j2_bulk_pair_eliminant_certificate.py --output results/item247_j2_bulk_pair_eliminant_certificate.json
    python scripts/item247_j2_bulk_pair_eliminant_certificate.py --output results/item247_j2_bulk_pair_eliminant_certificate_replay.json

Canonical and replay outputs are byte-identical and contain no host path,
timestamp, random seed, or elapsed time.

### Status ledger

**PROVED**

- the actual $j=2$ parity reduction and distinction from the $j=1$
  parameter;
- the unit common-state determinant and exact eliminated residual;
- the parity differential identity and one-seed normal form;
- the determinant $2(r-1)$ and its exact singular-locus classification;
- genuine admissibility of the singular $r=1$ rows; and
- the common-denominator integer-content criterion.

**EXACT FINITE ONLY**

- the 1,115-row full-pair census through $p\le401$;
- the 74-row rational content replay through $p\le101$; and
- the 1,134-row singular-locus scan through $p\le20000$.

**OPEN**

- an all-prime factorization or nondivisibility theorem for
  $\mathscr C_{r,s}$;
- an all-prime classification of the singular scalar (5.1);
- all-prime simultaneous nonvanishing of the two bulk residuals; and
- any Route-1 rate or capacity improvement.

The booking is



$$
\boxed{
\text{new unconditional log rate}=0,\qquad
\text{new divisibility exponent}=0,\qquad
\text{capacity reduction}=0.}                        \tag{8.1}
$$



Item 247 proves no statement about the arithmetic nature of $e+\pi$.
