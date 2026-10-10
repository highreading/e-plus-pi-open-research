> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 363 — exact fixed-$M$ radical for the joint $j=1$ Hasse–transverse gate and a gate-only elimination no-go

Date: 2026-09-01

## 0. Scope correction

The initial assignment mentioned the phase $p=6m+2d+1$.  That notation
belongs to the ordinary-$j=2$ chain.  Root corrected the scope before this
item was packaged.  Nothing from that chain is imported here.

Throughout this report the canonical fixed-$j=1$ family is



$$
p=4h+6s+3, M=3h+4s+2, h,s\geq1.                 \tag{0.1}
$$



This is a research-management correction, not a mathematical theorem or a
change in the Route 1 ledger.

## 1. Outcome and capacity first

At fixed $M$, put



$$
\mathcal P_M=
\left\{p\text{ prime}:{4M+3\over3}\leq p\leq{3M-1\over2}\right\}.
                                                               \tag{1.1}
$$



For $p\in\mathcal P_M$, the actual row is



$$
h_p=3M-2p, s_p={3p-4M-1\over2}.                         \tag{1.2}
$$



Let $Q_0$ be Item 360's transverse period and let



$$
\mathfrak a_p=a_{2s_p+1,\,2h_p}                             \tag{1.3}
$$



be the selected integral Hasse coordinate.  The joint event is



$$
Q_0(p)=0, \mathfrak a_p=0\pmod p.                        \tag{1.4}
$$



Item 363 proves an exact cross-prime formulation of (1.4).  Let



$$
P_M=\prod_{p\in\mathcal P_M}p, 
\overline C_\nu(M)={C_\nu(M)\over P_M}\in\mathbb Z,          \tag{1.5}
$$



where $C_0,C_1$ are Item 197's fixed integers.  Define an integral
clearing $Y_{h,s}$ of the endpoint coordinate $y_{h,s}$ in Section 3,
and let $Z_M$ be the unique CRT representative satisfying



$$
0\leq Z_M<P_M, Z_M\equiv Y_{h_p,s_p}\pmod p
\quad(p\in\mathcal P_M).                                   \tag{1.6}
$$



If $R_{H\mathscr T}(M)$ is the product of the distinct primes satisfying
(1.4), then



$$
\boxed{
R_{H\mathscr T}(M)=
\gcd\!\left(P_M,\overline C_0(M),\overline C_1(M)Z_M\right).}
                                                               \tag{1.7}
$$



This is an exact fixed-$M$, target-free integer formula.  It is not a new
independent arithmetic restriction: $Z_M$ is the CRT packing of the
remaining boundary coordinate itself.  CRT can pack an arbitrary subset
of $\mathcal P_M$ into an integer smaller than $P_M$, so (1.7) alone
does not imply nonconcentration.

The raw capacity is



$$
\log P_M={M\over6}+o(M), 
{1\over6M}\log P_M={1\over36}+o(1).                         \tag{1.8}
$$



No theorem proves



$$
\log R_{H\mathscr T}(M)=o(M).                               \tag{1.9}
$$



Therefore



$$
\boxed{
\text{new linear log rate}=0, 
\text{new fixed-}j=1\text{ capacity reduction}=0, 
\text{booking}=0.}                                         \tag{1.10}
$$



Route 1 remains ACTIVE and the $1/36$ ceiling is retained.

## 2. Remove the compulsory first prime copy globally

Item 197 defines



$$
C_\nu(M)=[z^{4M+\nu}]
{(1-z)^{6M}(1+z)^{1+3\nu}\over
 (1+z^2)^{4M+1+\nu}}\in\mathbb Z, \nu=0,1.              \tag{2.1}
$$



Every $p\in\mathcal P_M$ is an actual rank-zero row and hence



$$
p\mid C_0(M),C_1(M).                                       \tag{2.2}
$$



The primes in $\mathcal P_M$ are distinct, so (2.2) proves



$$
P_M\mid C_0(M),C_1(M),                                     \tag{2.3}
$$



and the integers in (1.5) are well defined, including the degenerate case
$C_\nu(M)=0$.

Item 218's exact bridge is



$$
{C_\nu(M)\over p}\equiv6Q_\nu(p)\pmod p.                  \tag{2.4}
$$



Since $P_M/p$ is a $p$-unit, equations (1.5) and (2.4) give



$$
\boxed{
Q_\nu(p)\equiv
u_{M,p}\overline C_\nu(M)\pmod p, 
u_{M,p}={P_M/p\over6}\in\mathbb F_p^\times.}               \tag{2.5}
$$



Thus $\overline C_0,\overline C_1$ remove exactly the compulsory first
copy across all fixed-$M$ candidate primes.  No raw gcd content is booked
twice.

## 3. The joint gate is the full two-coordinate gate plus one boundary

Retain Item 360's normalized forms



$$
f_0={Q_0\over\mathsf A}=2x-\lambda y, 
f_1={Q_1\over\mathsf A}=2\alpha u-\beta\lambda v,           \tag{3.1}
$$



and the selected Hasse eliminant



$$
H=\beta xv-\alpha uy.                                      \tag{3.2}
$$



All displayed scalar factors are units on an actual row, and Item 360
proved



$$
\mathfrak a_p=0\quad\Longleftrightarrow\quad H=0\pmod p.    \tag{3.3}
$$



The exact syzygy is



$$
\beta vf_0-yf_1=2H.                                        \tag{3.4}
$$



On the transverse-zero locus $f_0=0$, equation (3.4) becomes



$$
2H=-yf_1.                                                   \tag{3.5}
$$



Consequently



$$
\boxed{
Q_0=\mathfrak a_p=0
\quad\Longleftrightarrow\quad
Q_0=0\ \text{ and }\ (Q_1=0\ \text{ or }\ y=0).}          \tag{3.6}
$$



This is an exact union, not a probabilistic codimension heuristic.  The
first branch is the original full collision.  The second is Item 360's
retained chart boundary.

To clear the boundary integrally, write



$$
K_0(z)=(1-z)^{2h}(1+z)=\sum_j k_jz^j                        \tag{3.7}
$$



and use Item 218's terminating tail



$$
y_{h,s}=\sum_{t=0}^{h}(-1)^t
{(h+1)_t\over(2s+h+2)_t}k_{2t+1}.                          \tag{3.8}
$$



Put



$$
D_{h,s}=(2s+h+2)_h                                         \tag{3.9}
$$



and



$$
\boxed{
Y_{h,s}=D_{h,s}y_{h,s}
=\sum_{t=0}^{h}(-1)^t(h+1)_t
(2s+h+2+t)_{h-t}k_{2t+1}\in\mathbb Z.}                    \tag{3.10}
$$



Every factor of $D_{h,s}$ lies strictly between $0$ and $p$, so



$$
y_{h,s}=0\pmod p\quad\Longleftrightarrow\quad
Y_{h,s}=0\pmod p.                                         \tag{3.11}
$$



Combining (2.5), (3.3), (3.6), and (3.11) yields the primewise theorem



$$
\boxed{
Q_0(p)=\mathfrak a_p=0
\quad\Longleftrightarrow\quad
p\mid\overline C_0(M), 
p\mid\overline C_1(M)Y_{h_p,s_p}.}                         \tag{3.12}
$$



This preserves every implication from the actual collision and every
boundary component.

## 4. Exact CRT radical and branch decomposition

Define three squarefree radicals:



$$
\begin{aligned}
R_{\rm full}(M)
 &=\gcd(P_M,\overline C_0,\overline C_1),\\
R_{\rm bdry}(M)
 &=\gcd(P_M,\overline C_0,Z_M),\\
R_{H\mathscr T}(M)
 &=\prod_{\substack{p\in\mathcal P_M\\Q_0(p)=\mathfrak a_p=0}}p.
\end{aligned}                                               \tag{4.1}
$$



Because $P_M$ is squarefree, equations (1.6) and (3.12) prove, prime by
prime,



$$
\boxed{
R_{H\mathscr T}
=\operatorname {lcm}(R_{\rm full},R_{\rm bdry})
=\gcd(P_M,\overline C_0,\overline C_1Z_M).}                 \tag{4.2}
$$



In the original, not de-overlapped, integers this also gives



$$
R_{H\mathscr T}(M)^2\mid C_0(M), 
R_{H\mathscr T}(M)^2\mid C_1(M)Z_M.                        \tag{4.3}
$$



Equation (4.2) is the most compressed exact fixed-$M$ arithmetic form
obtained here.  It distinguishes the full-collision branch from the
boundary instead of silently identifying them.

## 5. Why the CRT target is information-neutral

For any squarefree product $P=\prod_{p\in\mathcal P}p$ and any subset
$\mathcal S\subseteq\mathcal P$, CRT supplies a unique $0\leq Z<P$
with



$$
Z\equiv0\pmod p\quad(p\in\mathcal S), 
Z\equiv1\pmod p\quad(p\notin\mathcal S).                   \tag{5.1}
$$



Then



$$
\gcd(P,Z)=\prod_{p\in\mathcal S}p.                         \tag{5.2}
$$



Thus even an arbitrary zero pattern has a single carrier satisfying



$$
\log\max(1,Z)\leq\log P={M\over6}+o(M).                    \tag{5.3}
$$



Linear height at exactly the raw support scale cannot prove a strict
weighted saving.  A useful theorem would have to show special arithmetic
structure of the actual $Z_M$, not merely its existence or the bound
(5.3).

There is a second fixed-phase warning.  From (1.2),



$$
h_p\equiv3M\pmod p, 
2s_p\equiv-(4M+1)\pmod p.                                  \tag{5.4}
$$



Hence a polynomial in the moving prime satisfies



$$
F_M(p)\equiv F_M(0)\pmod p,                                \tag{5.5}
$$



and any bounded-degree rational parameter expression with unit
denominator collapses to the fixed phase (5.4).  Polynomial degree in
$p$ does not encode the varying boundary residues; its constant term
must already contain their CRT data.

## 6. Exact elimination and resultant no-go

In the universal period-coordinate ring, direct elimination gives



$$
\boxed{
\operatorname {Res}_y(f_0,H)=xf_1, 
\operatorname {Res}_x(f_0,H)=-yf_1.}                        \tag{6.1}
$$



The resultants recover the unused second gate multiplied by one of the
boundary coordinates.  They do not produce a third condition.

Moreover



$$
\boxed{
\langle f_0,H\rangle\cap
\mathbb Q[\lambda,\alpha,\beta]=\langle0\rangle.}           \tag{6.2}
$$



The projection remains dominant on the nonzero chart.  For arbitrary
nonzero $\alpha$, take



$$
y=v=1, x={\lambda\over2}, 
u={\beta\lambda\over2\alpha};                              \tag{6.3}
$$



then $f_0=f_1=H=0$.  Thus saturation does not create a parameter-only
divisor.

This proves a sharply scoped no-go:

> Gate-only elimination, resultants, saturation, and fixed-phase
> substitution cannot create a nonzero target-free parameter divisor from
> the joint Hasse–transverse equations.  They return the original full
> gate plus its explicit boundary.

This does not rule out an identity special to the actual hypergeometric
orbit, a sheaf-theoretic joint nonconcentration theorem, or an average-gcd
estimate for (4.2).

## 7. The Frobenius formulation is exact but not a third coordinate

Set



$$
\mathscr L_p(w)={(1+w)^p-1-w^p\over p}\in\mathbb Z[w].      \tag{7.1}
$$



For $1\leq k<p$,



$$
[w^k]\mathscr L_p(w)={1\over p}\binom pk
\equiv{(-1)^{k-1}\over k}\pmod p.                          \tag{7.2}
$$



Since Item 218's indices



$$
T=2h+6s+2, L_0=4h+4s+2                                \tag{7.3}
$$



both lie below $p$, its exact finite-log reduction becomes



$$
\boxed{
Q_0\equiv
\bigl(2[z^T]-[z^{L_0}]\bigr)
(1-z)^{2h}(1+z)(1+z^2)^{2s}\mathscr L_p(z^2)
\pmod p.}                                                  \tag{7.4}
$$



The selected Hasse coordinate is independently



$$
\mathfrak a_p=
\sum_{k=0}^{\lfloor h/2\rfloor}
\binom{2s+k}{k}
\binom{8s+2h+3}{2h-4k}\pmod p.                             \tag{7.5}
$$



Equations (7.4)–(7.5), joined through (3.4), are an exact Frobenius/Hasse
description of the two conditions.  The first coordinate remains the
original Frobenius defect.  No extra Frobenius divisor is generated.

The two Item 360 rows $p=13,47$ have $\mathfrak a_p=0$ and
$Q_0\neq0$.  Item 218's row



$$
(p,h,s)=(109,10,11)                                       \tag{7.6}
$$



has $Q_0=0$ and $\mathfrak a_p=70\neq0$.  These are declared finite
separation controls only.  They prove neither density nor universal
nonintersection.

## 8. Weighted audit

The exact target is



$$
W_{H\mathscr T}(M)=\log R_{H\mathscr T}(M)=o(M).            \tag{8.1}
$$



Three currently available bounds fail to improve the raw ceiling.

1.  The exact gcd formula (4.2) gives only
    $W_{H\mathscr T}\leq\log P_M=M/6+o(M)$.
2.  Item 197's best direct Cauchy constant is
    $H_0=6.327627545440858\ldots$.  When $C_0(M)\ne0$, (4.3)
    and the square-divisor route give only
    

$$
W_{H\mathscr T}(M)\leq {H_0\over2}M+o(M)
    =3.163813772720429\ldots M+o(M),                         \tag{8.2}
$$


    much worse than $M/6$.  If $C_0(M)=0$, that coefficient-height
    bound is unavailable and the raw ceiling remains; either case gives no
    strict improvement.
3.  The canonical CRT representative has at best the raw-scale height
    (5.3), and the arbitrary-pattern theorem shows that this fact is
    information-neutral.

Therefore neither exact elimination, the Frobenius rewrite, the existing
height, nor CRT compression proves any strict constant.

The smallest admissible new inputs are now explicit:

1. a sequence-specific theorem that the actual CRT carrier $Z_M$ has a
   sublinear-height or sparse-divisor representation;
2. an average-gcd theorem for
   $\gcd(P_M,\overline C_0,\overline C_1Z_M)$; or
3. separate weighted bounds for the full radical and the boundary radical
   in (4.1).

## 9. Deterministic controls

The replay uses exactly three fixed values, chosen before Item 363
computation:

- $M=9$, containing Item 360's $p=13$ selected-zero separation row;
- $M=34$, containing Item 360's $p=47$ selected-zero separation row;
- $M=76$, containing Item 218's opposite $p=109$ separation row and
  four candidate primes, so the CRT identity is nontrivial.

There are six candidate rows in total.  The certificate reconstructs
$C_0,C_1,Q_0,Q_1,H,\mathfrak a_p,Y,D$, the quotient bridges, the
finite-log coordinate, and all three radicals.  It also verifies all 16
zero patterns on the four-prime $M=76$ support as a declared control of
the general CRT information-neutrality theorem.

No collision search, zero census, or extrapolation is performed.

## 10. Strict decision

### PROVED

- exact compulsory-prime de-overlap at fixed $M$;
- the primewise joint criterion (3.12);
- the exact CRT/gcd radical and branch decomposition (4.2);
- the integral $p$-unit clearing of the boundary coordinate;
- the resultants (6.1) and zero parameter elimination ideal (6.2);
- the finite-log Frobenius form (7.4);
- the scoped gate-only elimination and CRT information-class no-go;
- zero booking.

### EXACT FINITE ONLY

- three declared fixed-$M$ controls, six rows total;
- the two Hasse-zero/transverse-nonzero rows and one converse separation
  row;
- 16 declared CRT subset controls;
- no density inference.

### OPEN

- special arithmetic structure of $Z_M$;
- a weighted average-gcd theorem for (4.2);
- $W_{H\mathscr T}(M)=o(M)$ or any strict constant below $1/6$ per
  $M$;
- any fixed-$j=1$ capacity reduction, Route 1, and every conclusion
  about $e+\pi$.
