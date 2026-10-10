> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 211 — the second lift on the exact common-content ray

Date: 2026-08-31

## 1. Scope and verdict

This item specializes Item 209's exact second-lift digit to Item 205's
proved common-content ray



$$
s\equiv3\pmod4,\qquad p=5s+4\text{ prime}.             \tag{1.1}
$$



The regular minimal anchor $j=1$ is treated symbolically.  The result is
an explicit algebraic congruence criterion, not a global nonvanishing
theorem:



$$
\boxed{A_1\equiv{5\over24}\Phi_s\pmod p},              \tag{1.2}
$$



where $\Phi_s$ is the four-sum expression in (6.2).  Thus
$A_1=0$ if and only if $\Phi_s=0\pmod p$.  A finite scan of all 285
ray primes $p\le20000$ found no $j=1$ zero.  This is explicitly
**FINITE** and is not extrapolated.  No proof that the congruence is always
nonzero is known.

The ray does admit an actual zero after changing the anchor: Item 209's
row



$$
(s,p,j,m)=(3,19,3,36)                 \tag{1.3}
$$



has $A_0=A_1=B_0=0$.  Hence common content does not force either outcome
for the second lift across anchors.  A finite $j=3$, $p\le500$ replay
found (1.3) as its only $A_1$-zero; that count is not an asymptotic
statement.

Finally, the entire ray has fixed-$m$ log weight $O(\log m)$.  Even a
complete theorem deciding (1.2) would add zero Route-1 exponent.  The value
of the formula is structural: it exhibits exactly which incomplete-beta
tails enter the first genuine carry.

## 2. The integral support gap

Write $s=4t+3$, so $p=20t+19\equiv3\pmod4$.  On $j=1$,



$$
m={9s+7\over2},\qquad F={u^5\over Q^4},               \tag{2.1}
$$



and Item 172's two residual polynomials simplify over the integers to



$$
\begin{aligned}
 P_0&=u^{2s+1}Q^{2s+1}
     =x^{2s+1}(1-x^4)^{2s+1},\\
 P_1&=u^{2s+1}Q^{2s}
     =x^{2s+1}(1-x)(1-x^4)^{2s}.
 \end{aligned}                                         \tag{2.2}
$$



The resonant degree is $p-1=5s+3$.  In $P_0$, the difference from
the initial degree is $3s+2\equiv3\pmod4$.  In the two sections of
$P_1$, the differences are $3s+2\equiv3\pmod4$ and
$3s+1\equiv2\pmod4$.  Consequently



$$
[x^{p-1}]P_0=[x^{p-1}]P_1=0                           \tag{2.3}
$$



over $\mathbb Z$, not merely modulo $p$.  This strengthens the
description of the ray: its two Cartier scalars vanish by an exact support
gap.

Let $T_0,T_1$ be the zero-constant primitives



$$
T_0=\sum_{r=0}^{2s+1}{(-1)^r{2s+1\choose r}\over
                           2s+2+4r}x^{2s+2+4r},          \tag{2.4}
$$





$$
T_1=\sum_{r=0}^{2s}(-1)^r{2s\choose r}
 \left({x^{2s+2+4r}\over2s+2+4r}
       -{x^{2s+3+4r}\over2s+3+4r}\right).              \tag{2.5}
$$



No displayed denominator is divisible by $p$; equivalently, (2.3)
removes the only possible denominator $p$.  Therefore the exact
Bockstein identity can be applied separately to each row:



$$
F^pP_\nu\,dx=d(F^pT_\nu)-pF^{p-1}F'T_\nu\,dx.         \tag{2.6}
$$



Because $F(0)=F(1)=0$, the first term has zero relative boundary.

## 3. Five root values collapse to three scalar sums

Define



$$
\begin{aligned}
 \beta&=\sum_{r=0}^{2s+1}{(-1)^r{2s+1\choose r}\over2s+2+4r},\\
 A&=\sum_{r=0}^{2s}{(-1)^r{2s\choose r}\over2s+2+4r},\\
 B&=\sum_{r=0}^{2s}{(-1)^r{2s\choose r}\over2s+3+4r}.
 \end{aligned}                                         \tag{3.1}
$$



For every fourth root of unity $a$, equations (2.4)--(2.5) give



$$
T_0(a)=\beta,\qquad T_1(a)=A-aB,           \tag{3.2}
$$



while $T_0(0)=T_1(0)=0$.  The beta integral also gives the exact
relation



$$
\beta={2(2s+1)\over5s+3}A,\qquad
 \beta\equiv(s+2)A\pmod p.                             \tag{3.3}
$$



The three numbers $\beta,A,B$ are nonzero modulo $p$: each has a
factorial/product expression whose factors are nonzero below $p$.
This nonvanishing does not by itself decide (1.2), because two incomplete
tails remain.

## 4. The polynomial Cartier scalar is an explicit high tail

Put



$$
R={3s+3\over4},                                      \tag{4.1}
$$



and define



$$
H_0=\sum_{r=R}^{2s+1}{(-1)^r{2s+1\choose r}\over2s+2+4r}, \tag{4.2}
$$





$$
H_1=\sum_{r=R}^{2s}(-1)^r{2s\choose r}
 \left({1\over2s+2+4r}-{1\over2s+3+4r}\right).       \tag{4.3}
$$



These are exactly the coefficients of the monomials of $T_0,T_1$
whose degree is at least $p$.  In fact their first degrees are
$p+1$ and $p+1,p+2$, so degree $p$ never occurs.

Let



$$
{F'\over F}=\sum_{a\in\{0,1,-1,i,-i\}}{n_a\over x-a},
 \quad(n_0,n_1,n_{-1},n_i,n_{-i})=(5,5,-4,-4,-4),      \tag{4.4}
$$



and decompose



$$
T_\nu{F'\over F}=D_\nu(x)+
   \sum_a{n_aT_\nu(a)\over x-a}.                       \tag{4.5}
$$



For a monomial $c_dx^d$, its contribution to
$[x^{p-1}]D_\nu$ is



$$
c_d\sum_a n_aa^{d-p}.                     \tag{4.6}
$$



Every high exponent in $T_0$ is $1\pmod4$ after subtracting $p$,
and those in the two sections of $T_1$ are $1,2\pmod4$.  In all
three cases



$$
\sum_a n_aa^{d-p}=9.               \tag{4.7}
$$



Thus the two polynomial Cartier scalars are exactly



$$
d_0=[x^{p-1}]D_0\equiv9H_0,\qquad
 d_1=[x^{p-1}]D_1\equiv9H_1\pmod p.                    \tag{4.8}
$$



This is the new carry datum that is invisible in the reduced common
moving vector.

## 5. The divided coordinate vectors

Use only the $(R,L)$ coordinates relevant to the $A$-minor.  At
$j=1$, exact partial fractions give



$$
\begin{aligned}
 v&=\operatorname{coord}_{R,L}(F\,dx)=(-11/6,-5),\\
 z_0&=\operatorname{coord}_{R,L}(F/x\,dx)=(-35/24,7),\\
 W_3&=\sum_an_aa^3\operatorname{coord}_{R,L}
       (F/(x-a)\,dx)=(-577/24,75).
 \end{aligned}                                         \tag{5.1}
$$



Also $\sum_an_az_a=0$, because $F'\,dx=dF$ has zero relative
coordinates.  Since $p\equiv3\pmod4$, inverse Frobenius sends
$a$ to $a^p=a^3$ on the fourth roots.  Applying Cartier to (2.6),
using (3.2), and retaining the polynomial scalar (4.8) gives



$$
\boxed{
 \begin{aligned}
 q_0&:=((X_0/p),(L_0/p))\equiv5\beta z_0-d_0v,\\
 q_1&:=((X_1/p),(L_1/p))\equiv5Az_0+BW_3-d_1v
 \end{aligned}\pmod p.}                               \tag{5.2}
$$



This formula is more informative than the bare determinant quotient: it
recovers both divided coordinate pairs.  The standalone checker compares
(5.2) with the independent modulo-$p^3$ Hasse engine.

## 6. Closed formula and exact zero criterion

The three fixed wedges are



$$
\det(v,z_0)=-{161\over8},\qquad
 \det(v,W_3)=-{6185\over24},\qquad
 \det(z_0,W_3)={707\over12}.                            \tag{6.1}
$$



Item 209's convention gives $A_1=\det(q_0,q_1)$.  Expanding (5.2),
then substituting (4.8), proves



$$
\boxed{
 \begin{aligned}
 \Phi_s={}&1414\beta B-4347\beta H_1
             +4347AH_0+11133H_0B,\\
 A_1\equiv{}&{5\over24}\Phi_s\pmod p.
 \end{aligned}}                                        \tag{6.2}
$$



Every ray point has $s\ge3$ and hence $p\ge19$; in particular, $p=5$
never occurs and the prefactor $5/24$ is a nonzero $p$-unit.  All other
displayed denominators are also $p$-units.  Hence the exact algebraic criterion is



$$
A_1=0\iff\Phi_s=0\pmod p.      \tag{6.3}
$$



Equation (6.2) does not visibly factor into quantities already known to be
nonzero.  Therefore this item neither claims nor proves that $A_1$ is
forced nonzero at $j=1$.  It replaces the large modulo-$p^3$ Hasse
calculation by four explicit modulo-$p$ sparse sums.

## 7. Finite checks and actual witnesses

All observations in this section are **FINITE**.

1. The formula scan includes every ray prime $p\le20000$: 285 primes,
   with no $j=1$ zero of (6.2).
2. For every ray prime $p\le500$, plus $p=1499$, the independent
   Item 209 Hasse recurrence reproduces both vectors in (5.2) and the
   value in (6.2).
3. On $j=3$ and ray primes $p\le500$, the actual Hasse scan finds the
   single zero (1.3).  In particular, an actual ray zero exists, but it is
   anchor-dependent.

The first exact controls are



$$
\begin{array}{c|c|c|c}
p&s&j&A_1\\ \hline
19&3&1&16\\
19&3&3&0\\
59&11&1&58\\
79&15&1&53\\
1499&299&1&925
\end{array}                                             \tag{7.1}
$$



No density or eventual-nonvanishing claim is inferred from these data.

## 8. Rate and off-ray scope

On the common-content ray, the cell relation gives



$$
10m+1=(5j+4)p.                \tag{8.1}
$$



For fixed $m$, all such primes divide one integer.  Their total log
weight is at most $\log(10m+1)=O(\log m)=o(m)$.  Therefore even a full
classification of (6.3) cannot fill any part of the positive global
Route-1 exponent deficit.

Off the ray, the exact support gap (2.3) generally disappears.  The
Cartier scalar need not be zero over $\mathbb Z$, and the divided vectors
acquire additional first-digit/carry terms.  Thus (6.2) is not an off-ray
formula.  What does transfer is the method: on another exact-resonance
family, one may form the integral primitives, retain the polynomial
Cartier coefficient, and reduce the remaining contribution to fixed
divisor values.  Finding a positive-mass family where that template closes
remains open.

## 9. Deterministic portable package

The checker

    work/item211_a1_structural_ray_certificate.py

uses only the Python standard library and the pinned Item 209 Hasse helper.
It:

1. evaluates (3.1), (4.2)--(4.3), and (6.2) modulo every scanned prime;
2. independently evaluates (5.2) from the fixed Cayley vectors;
3. verifies $\beta\equiv(s+2)A$ and nonvanishing of
   $\beta,A,B$;
4. replays the bounded $j=1$ and $j=3$ controls through Item 209;
5. labels every finite scan without extrapolation.

Canonical and replay JSON files are required to be byte-identical.  The
portable manifest uses only archive-relative keys and pins the Item 209
helper.  No archive metadata is edited by this item.

Status ledger:

- **PROVED:** the integral support gap (2.3), quotient-vector formula
  (5.2), closed criterion (6.2)--(6.3), and zero-rate bound (8.1).
- **FINITE:** the $p\le20000$ formula scan and bounded Hasse replays.
- **OPEN:** global $j=1$ nonvanishing or a classification of zeros of
  $\Phi_s$; any positive-rate off-ray consequence; any improvement to
  the Route-1 exponent; and the arithmetic nature of $e+\pi$.
