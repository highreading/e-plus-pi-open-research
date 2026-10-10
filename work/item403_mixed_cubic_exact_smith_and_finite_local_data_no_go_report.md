> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 403 — Exact cubic Smith localization and a finite-local-data no-go

Date: 2026-09-01  
Status: **WORK ONLY, UNAUDITED, NO BOOKING**

## 1. Verdict and maximum ledger consequence

Let $q>0$ be odd with $3\nmid q$, put $K=4^{q-1}$, and use the
actual fixed-gap coefficients $C_0,T_0,C_1,T_1\in\mathbb Z[1/6]$ of
canonical Items 157 and 396. This item proves the exact Smith formula



$$
\boxed{d_1(q)=d_2(q)=H_q,\qquad
        d_3(q)=H_qG_q^{\rm prim}}                    \tag{1.1}
$$



in $\mathbb Z[1/6]$, up to units. Here $H_q$ is the common
coefficient content, and $G_q^{\rm prim}$ is the primitive cubic defect
defined in Section 3. Formula (1.1) applies to the **actual** Item-157
matrix for every admissible $q$; it is not a finite-data inference.
Consequently the open target is exactly



$$
\boxed{H_qG_q^{\rm prim}\mid
 P_q:=\prod_{j=0}^{q-2}(2q-3-3j)}                    \tag{1.2}
$$



away from $2,3$. There is no hidden lower Smith factor.

A proof of (1.2), or only its compatible-prime radical weakening, would
force



$$
\boxed{c_m^>=1\quad\text{for every }m,}             \tag{1.3}
$$



closing the entire $p>6m$ common-content component from Item 390. Its
present separate upper ceiling is $(\log136)/6$. This conditional
closure would not itself add a divisor lower bound to $r_1$, and Item
393 still forbids subtracting one component upper bound from the
compatible total-content upper bound. Item 403 proves neither (1.2) nor
(1.3), so the proved booking and capacity reduction are both zero.

The second result is a globally quantified information-class no-go. For
every admissible $q$, every compatible prime $p=q+6m$, and every
finite $3$-adic precision, ambient perturbations of the actual four
rational coefficients can preserve:

* denominator support in $\{2,3\}$;
* all four coefficient valuations;
* the exact Item-148/396 determinant valuation;
* any prescribed finite set of $3$-adic digits;

while forcing $p\nmid P_q$ and $p\mid d_3$, with the appropriate
minimal Item-396 carrier vanishing.

These perturbations are **not actual mixed-cubic rows**. They do not
refute (1.2) for the actual coefficients. They show only that matrix
shape, denominator support, exact $3$-adic valuations, and any fixed
finite amount of $3$-adic digit data cannot by themselves prove (1.2).
An actual proof must use a global identity tying the true coefficient
jets together, or a genuinely $p$-local invariant of their exact
reductions.

## 2. Cubic matrix and forms

Choose a common denominator $D$, supported only at $2,3$, and write



$$
(c_0,t_0,c_1,t_1)=D(C_0,T_0,C_1,T_1)\in\mathbb Z^4.
$$



Over $\mathcal R=\mathbb Z[1/6]$, $D$ is a unit. The Item-157
multiplication map has matrix



$$
M=
 \begin{pmatrix}
 -t_0&0&Kc_0&-t_1&0&Kc_1\\
 c_0&-t_0&0&c_1&-t_1&0\\
 0&c_0&-t_0&0&c_1&-t_1
 \end{pmatrix}.                                      \tag{2.1}
$$



Put



$$
\rho=c_0t_1-c_1t_0,\qquad U_s=t_s^3-Kc_s^3.         \tag{2.2}
$$



Item 157 lists all maximal minors and proves that its two mixed cubics
have valuation at least



$$
\min\{v(\rho),v(U_0),v(U_1)\}                       \tag{2.3}
$$



when the coefficient quadruple is primitive.

## 3. Exact all-DVR Smith theorem

**Theorem 3.1.** Let $\mathcal O$ be a DVR with uniformizer $\pi$,
let $K\in\mathcal O^\times$, and let
$c_0,t_0,c_1,t_1\in\mathcal O$ be not all zero. Put



$$
h=\min\{v(c_0),v(t_0),v(c_1),v(t_1)\},
$$



divide all four entries by $\pi^h$, and attach a star to the divided
entries and forms. Define



$$
\gamma=\min\{v(\rho^*),v(U_0^*),v(U_1^*)\}.          \tag{3.1}
$$



If $M$ has rank three over the fraction field, its Smith invariant
valuations are exactly



$$
\boxed{(h,h,h+\gamma).}                              \tag{3.2}
$$



With the last entry $+\infty$, the same formula describes rank two.

**Proof.** First take $h=0$. Some member of
$(c_0,t_0,c_1,t_1)$ is a unit. If $t_0$ is a unit, the first two
rows and columns $0,1$ have determinant $t_0^2$. If $c_0$ is a
unit, rows $1,2$ and columns $0,1$ have determinant $c_0^2$.
Columns $3,4$ give the identical alternatives for $t_1,c_1$. Thus



$$
v(\Delta_1)=v(\Delta_2)=0.                           \tag{3.3}
$$



Every maximal minor has valuation at least $\gamma$ by Item 157.
Conversely, the maximal-minor list contains $U_0,U_1$ and each of
$c_0\rho,t_0\rho,c_1\rho,t_1\rho$. Multiplying $\rho$ by the unit
among the coefficients gives a minor of valuation $v(\rho)$. Therefore



$$
v(\Delta_3)=\min\{v(\rho),v(U_0),v(U_1)\}=\gamma.    \tag{3.4}
$$



This gives $(0,0,\gamma)$. Restoring $\pi^h$ multiplies each
$i$-minor by $\pi^{ih}$, proving (3.2). $\square$

Globally, let $H_q$ be the actual coefficient content in
$\mathcal R$, divide the four coefficients by $H_q$, and define



$$
G_q^{\rm prim}
 =\prod_{\ell>3}\ell^{
 \min\{v_\ell(\rho^*),v_\ell(U_0^*),v_\ell(U_1^*)\}}. \tag{3.5}
$$



Theorem 3.1 at every $\ell>3$ proves (1.1), sharpening Item 157's
one-sided $G_q\mid\Delta_3\mid d_3^3$. The inherited Item-148
nonvanishing of the actual $\rho$ ensures rank three over $\mathbb Q$;
no determinant nonvanishing argument is repeated here.

## 4. Exact compatible-prime carrier split

Let $p=6m+q$ and



$$
E=2m+q-1=\frac{p+2q-3}{3},\qquad X_p=2^E.
$$



Fermat gives



$$
X_p^3\equiv4^{q-1}=K\pmod p.                        \tag{4.1}
$$



If $p\nmid H_q$, equation (3.5) says that $p\mid G_q^{\rm prim}$
is exactly the simultaneous vanishing of the primitive
$\rho,U_0,U_1$. This contains the precise Item-396 split:

* For $q\equiv5\pmod6$, one has $p\equiv2\pmod3$, cubing is
  bijective, and $U_0=U_1=0$ already selects the unique common root.
* For $q\equiv1\pmod6$, one has $p\equiv1\pmod3$; the two cubic rows
  can choose different roots, so $\rho=0$ is also needed.

If $p\mid H_q$, all four entries vanish. Hence the actual
compatible-prime problem is exactly the radical support of
$H_qG_q^{\rm prim}$.

Every factor $f_j=2q-3-3j$ of $P_q$ satisfies



$$
3-q\le f_j\le2q-3,\qquad f_j\equiv-q\pmod3.          \tag{4.2}
$$



For compatible $p=q+6m$, one has $-p<f_j<2p$. A multiple of $p$
there could only be $0$ or $p$. Either option forces $3\mid q$.
Thus



$$
\boxed{p\nmid P_q.}                                  \tag{4.3}
$$



Equations (1.2) and (4.3) would prove (1.3).

## 5. Uniform finite-$3$-adic-data countermodel

The next theorem concerns an ambient coefficient class, not the actual
family.

**Theorem 5.1.** Fix admissible $q$, compatible prime $p=q+6m$, and
precision $J\ge1$. For sufficiently large $L$, there exist integers
$a_s,b_s$ such that



$$
C_s'=C_s+3^La_s,\qquad T_s'=T_s+3^Lb_s             \tag{5.1}
$$



have the following properties:

1. all coefficient valuations, any prescribed $J$ digits, and every
   fixed finite collection of continuous normalized ratios are preserved;
2. the exact determinant valuation is preserved:

   

$$
v_3(C_0'T_1'-C_1'T_0')
   =v_3(C_0T_1-C_1T_0);                              \tag{5.2}
$$



3. $C_0',C_1'\ne0\pmod p$ and

   

$$
T_s'\equiv X_pC_s'\pmod p;                        \tag{5.3}
$$



4. the perturbed matrix has rank two modulo $p$, hence its first two
   Smith invariants are $p$-units while $p\mid d_3'$, even though
   $p\nmid P_q$.

**Proof.** Put $\epsilon=3^L$. Actual denominators are $p$-units.
Choose $a_s\pmod p$ outside the unique class making
$C_s+\epsilon a_s=0$, and then solve



$$
b_s\equiv\epsilon^{-1}
 \bigl(X_p(C_s+\epsilon a_s)-T_s\bigr)\pmod p.        \tag{5.4}
$$



Integer lifts give (5.3). For large $L$, all nonzero coefficient
valuations are unchanged. Moreover,



$$
\begin{aligned}
 C_0'T_1'-C_1'T_0'
 ={}&C_0T_1-C_1T_0\\
 &+\epsilon(C_0b_1+a_0T_1-C_1b_0-a_1T_0)
 +\epsilon^2(a_0b_1-a_1b_0).
\end{aligned}                                        \tag{5.5}
$$



The perturbation terms eventually have valuation above the nonzero first
term, proving (5.2); continuity preserves any fixed finite digit data.
Modulo $p$, (4.1) and (5.3) give



$$
\rho'=U_0'=U_1'=0.                                  \tag{5.6}
$$



In $\mathbb F_p[Z]/(Z^3-K)$, both generators are nonzero scalar
multiples of $Z-X_p$. Since $p>3$ and $X_p\ne0$, the root is
simple and the generated ideal has dimension two. Thus the matrix rank is
two. Theorem 3.1 and (4.3) finish the proof. $\square$

This respects the exact carrier split: for $q\equiv5\pmod6$,
$U_0',U_1'$ vanish; for $q\equiv1\pmod6$, all three of
$\rho',U_0',U_1'$ vanish and select the same branch $X_p$.

## 6. Scope and ledger

Theorem 5.1 disproves, uniformly and without a finite scan, the ambient
implication



$$
\begin{gathered}
 \text{cubic matrix shape}
 +\text{ denominator support in }\{2,3\}\\
 +\text{ Item-396 carrier split}
 +\text{ exact }3\text{-adic valuations}\\
 +\text{ any fixed finite }3\text{-adic digits}
 \Longrightarrow d_3\mid P_q.
\end{gathered}                                        \tag{6.1}
$$



It does not close an exact length-$(q-1)$ Bezout identity, an all-jet
Cartier or hypergeometric identity, a moving-$q$ invariant of the exact
actual reductions, or the actual support conjecture itself. The sharp
remaining target is an actual-family theorem for $H_qG_q^{\rm prim}$.

The proved results are the exact Smith formula (1.1), its precise
Item-396 carrier interpretation, and the ambient no-go. Not proved are
(1.2), its radical weakening, (1.3), any new divisor lower bound, Route-1
closure, or irrationality of $e+\pi$. Therefore



$$
\boxed{\Delta r_{\rm booked}=0,\qquad
        \Delta C_{\rm total}^{\rm proved}=0.}          \tag{6.2}
$$



## 7. Replay

Run:

    python work/item403_mixed_cubic_exact_smith_and_finite_local_data_no_go_certificate.py --output work/item403_mixed_cubic_exact_smith_and_finite_local_data_no_go_certificate.replay.json

The standard-library replay checks the local Smith formula on transparent
valuation vectors, constructs normalization countermodels in both
$q\bmod6$ branches from the actual coefficient definitions, verifies
the preserved valuations and digits, and checks the carrier vanishing,
rank two, $p\mid d_3$, and $p\nmid P_q$. These normalization rows
check the construction; the uniform theorem rests on the proof above.

Primary dependencies:

* sources/mixed_cubic_cube_smith_reduction.md
* sources/item396_fixed_gap_resultant_3adic_report.md
* sources/item390_mixed_cubic_fresh_primitive_saturation_report.md
* sources/item393_mixed_cubic_small_prime_strata_ceiling_report.md
