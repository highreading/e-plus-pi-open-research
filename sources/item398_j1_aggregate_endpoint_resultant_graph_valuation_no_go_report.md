> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 398 — aggregate endpoint resultant, collision-graph valuations, and the near-perfect-power cancellation obstruction

Date: 2026-09-01

## 1. Outcome and strict scope

Item 395 compressed the capacity-relevant logarithmic-window problem to the
actual cluster radical



$$
\mathcal C_{M,D}=\operatorname {rad}\!\left(
   \prod_{d=1}^{D}E^-_{M,d}E^+_{M,d}\right),
 \qquad D\sim c\log M.                                 \tag{1.1}
$$



This item exploits the common product structure of all endpoint evaluations.
It obtains an exact arithmetic theorem, but not the upper bound required for
a Route-1 capacity reduction.

Let $F_M$ be the actual collision polynomial, let
$R_M=R_{H\mathscr T}(M)$, and define



$$
G_D(X)=\prod_{d=1}^{D}(X^2-4d^2),
 \qquad
 \mathcal A_{M,D}=\operatorname {Res}(F_M,G_D).         \tag{1.2}
$$



The main results are:

1. **PROVED — exact aggregate resultant.**
   

$$
\boxed{
    \mathcal A_{M,D}
     =\prod_{q\in\mathcal Z_M}G_D(q)
     =\prod_{d=1}^{D}\mathcal N^-_{M,d}\mathcal N^+_{M,d}.}
                                                               \tag{1.3}
$$


   Thus all logarithmic shifts are one resultant, not merely a union of
   unrelated gcds.

2. **PROVED — exact collision-graph valuation.**  Join two actual collision
   primes when their difference is at most $2D$, and let
   $\deg_D(p)$ be the graph degree of $p$.  Then
   

$$
\boxed{v_p(\mathcal A_{M,D})=\deg_D(p)}          \tag{1.4}
$$


   for every $p\mid R_M$.  Consequently
   

$$
\boxed{
    \gcd(\mathcal A_{M,D},R_M^{2D})
      =\prod_{p\mid R_M}p^{\deg_D(p)}
      =\prod_{\{p,q\}\in E_{M,D}}pq,}                 \tag{1.5}
$$


   and $\mathcal C_{M,D}$ is its radical.

3. **PROVED — the aggregate is almost a perfect power.**  If
   $D\sim c\log M$, then
   

$$
0\le-\log{\mathcal A_{M,D}\over R_M^{2D}}
      \le\left({c^3\over8}+o(1)\right){\log^2M\over M}.
                                                               \tag{1.6}
$$


   Hence $\mathcal A_{M,D}/R_M^{2D}=1-o(1)$.

4. **PROVED — near-power subtraction preserves all pair content.**  Put
   

$$
\mathcal B_{M,D}=R_M^{2D}-\mathcal A_{M,D}. \tag{1.7}
$$


   A modulo-3 obstruction gives
   $\deg_D(p)\le D+\lfloor D/3\rfloor<2D$.  Therefore
   

$$
\boxed{
     v_p(\mathcal B_{M,D})=v_p(\mathcal A_{M,D})
       =\deg_D(p),}                                     \tag{1.8}
$$


   and
   

$$
\boxed{
     \gcd(\mathcal B_{M,D},R_M^{2D})
      =\gcd(\mathcal A_{M,D},R_M^{2D}).}                \tag{1.9}
$$



Equation (1.9) is the sharper obstruction requested after Item 395.  Even
though the aggregate endpoint resultant is extremely close to the perfect
power $R_M^{2D}$, subtracting that power does not cancel a single
candidate-prime collision valuation.  It repackages the exact collision
graph with the same multiplicities.

The resulting integer $\mathcal B_{M,D}$ still has logarithmic height of
order $2D\log R_M$, which can be $\asymp M\log M$.  Neither (1.5) nor
(1.9) proves the admission target



$$
\log\mathcal C_{M,\lfloor\log M\rfloor}
 <(1/12-\varepsilon)M.                                  \tag{1.10}
$$



Thus the new booking and capacity reduction are zero; the fixed-$j=1$
ceiling remains $1/36$.

## 2. Actual tied family and endpoint norms

Retain the actual set



$$
\mathcal Z_M=\{p\in\mathcal P_M:p\mid R_{H\mathscr T}(M)\},
 \qquad
 F_M(X)=\prod_{p\in\mathcal Z_M}(X-p),
 \qquad R_M=\prod_{p\in\mathcal Z_M}p.                 \tag{2.1}
$$



The tied interval is



$$
L_M={4M+3\over3}\le p\le U_M={3M-1\over2},
 \qquad U_M-L_M={M-9\over6}.                            \tag{2.2}
$$



For $1\le d\le D=o(M)$, Item 395 uses



$$
\mathcal N^-_{M,d}=(-1)^{n_M}F_M(2d)
   =\prod_{q\in\mathcal Z_M}(q-2d),                    \tag{2.3}
$$





$$
\mathcal N^+_{M,d}=(-1)^{n_M}F_M(-2d)
   =\prod_{q\in\mathcal Z_M}(q+2d).                    \tag{2.4}
$$



All factors are positive at logarithmic scale.

## 3. One resultant for every shift

Because $F_M$ and $G_D$ are monic,



$$
\operatorname {Res}(F_M,G_D)
 =\prod_{q\in\mathcal Z_M}G_D(q)
 =\prod_{q\in\mathcal Z_M}\prod_{d=1}^{D}(q^2-4d^2). \tag{3.1}
$$



Reordering the factors and using (2.3)--(2.4) proves (1.3):



$$
\mathcal A_{M,D}
 =\prod_{d=1}^{D}
   \left(\prod_q(q-2d)\right)
   \left(\prod_q(q+2d)\right).
                                                               \tag{3.2}
$$



Equivalently, for every odd $q>2D$, the local block has the exact
double-factorial form



$$
G_D(q)=
 { (q+2D)!!\,(q-2)!!\over q!!\,(q-2D-2)!!}.           \tag{3.3}
$$



Equation (3.3) is a representation of the same integral block; it does not
by itself localize its prime factors.

## 4. Exact prime allocation is the collision graph

Let $\Gamma_{M,D}$ be the graph with vertex set $\mathcal Z_M$ and edge
set



$$
E_{M,D}=\{\{p,q\}:p,q\in\mathcal Z_M, 0<|p-q|\le2D\}. \tag{4.1}
$$



Fix $p\in\mathcal Z_M$.  Under



$$
4D<L_M,qquad U_M+2D<2L_M,                             \tag{4.2}
$$



which holds for $D=O(\log M)$, a factor
$q^2-4d^2=(q-2d)(q+2d)$ is divisible by $p$ if and only if



$$
q=p+2d\quad\text{or}\quad q=p-2d. \tag{4.3}
$$



Indeed, every positive factor $q\pm2d$ is smaller than $2p$, so its only
possible positive multiple of $p$ is $p$ itself.  Condition $4D<p$
also shows that the companion factor is not divisible by $p$, so the
valuation contributed by one neighbor is exactly one.  Distinct neighbors
give distinct factors.  This proves



$$
v_p(\mathcal A_{M,D})=\deg_D(p).                       \tag{4.4}
$$



Since $v_p(R_M^{2D})=2D$, equation (1.5) follows once
$\deg_D(p)<2D$.  It also follows directly that



$$
\operatorname {rad}\gcd(\mathcal A_{M,D},R_M^{2D})
 =\mathcal C_{M,D}.                                     \tag{4.5}
$$



The second equality in (1.5) is the handshake identity in multiplicative
form: every edge $\{p,q\}$ contributes one $p$ and one $q$, so



$$
\prod_{p}p^{\deg_D(p)}=\prod_{\{p,q\}\in E_{M,D}}pq. \tag{4.6}
$$



This is an exact prime-allocation theorem.  There is no cancellation among
shifts: repeated membership records graph degree.

## 5. A uniform modular degree bound

All tied primes are greater than $3$ for large $M$.  Fix such a vertex
$p$.  For each $1\le d\le D$:

- if $3\mid d$, neither residue $p\pm2d$ is forced to be $0\pmod3$,
  so at most two neighbors are possible;
- if $3\nmid d$, exactly one of $p-2d,p+2d$ is $0\pmod3$.  It is
  larger than $3$ under (4.2), hence composite, so at most one neighbor is
  possible.

There are $\lfloor D/3\rfloor$ multiples of three.  Therefore



$$
\boxed{
 \deg_D(p)\le
 2\left\lfloor{D\over3}\right\rfloor
 +D-\left\lfloor{D\over3}\right\rfloor
 =D+\left\lfloor{D\over3}\right\rfloor<2D.}           \tag{5.1}
$$



This modular theorem controls multiplicity at one vertex, not the number of
vertices of positive degree.  It does not bound $\mathcal C_{M,D}$.

## 6. The aggregate is asymptotically a perfect power

Divide (3.1) by $R_M^{2D}$:



$$
{\mathcal A_{M,D}\over R_M^{2D}}
 =\prod_{q\in\mathcal Z_M}\prod_{d=1}^{D}
       \left(1-{4d^2\over q^2}\right).                 \tag{6.1}
$$



Put



$$
\varepsilon_{M,D}
 =-\log{\mathcal A_{M,D}\over R_M^{2D}}.               \tag{6.2}
$$



Using $-\log(1-x)\le x/(1-x)$, $q\ge L_M$, and
$\sum_{d=1}^{D}d^2=D(D+1)(2D+1)/6$, one obtains the all-family bound



$$
0\le\varepsilon_{M,D}
 \le {4n_M\sum_{d=1}^{D}d^2\over L_M^2-4D^2}.          \tag{6.3}
$$



The prime number theorem on (2.2) gives



$$
n_M\le {M\over6\log M}+o\left({M\over\log M}\right). \tag{6.4}
$$



For $D\sim c\log M$, substitution into (6.3) yields



$$
\boxed{
 0\le\varepsilon_{M,D}
 \le\left({c^3\over8}+o(1)\right){\log^2M\over M}=o(1).} \tag{6.5}
$$



The constant $1/8$ is exact at leading order: it is



$$
4\cdot{1\over6}\cdot{1\over3}\cdot{9\over16}={1\over8}, \tag{6.6}
$$



coming respectively from the local factor, tied-prime count, sum of
squares, and $L_M^{-2}$.

Thus



$$
\mathcal A_{M,D}=R_M^{2D}e^{-\varepsilon_{M,D}}
 =R_M^{2D}\left(1-O_c\left({\log^2M\over M}\right)\right). \tag{6.7}
$$



This very strong relative approximation is not a small-integer theorem:
$R_M^{2D}$ itself has logarithmic height $2D\log R_M$.

## 7. Subtracting the perfect power preserves every collision valuation

Define $\mathcal B_{M,D}$ by (1.7).  It is positive whenever
$\mathcal Z_M\ne\varnothing$.  For a candidate prime $p\mid R_M$,



$$
v_p(R_M^{2D})=2D,qquad
 v_p(\mathcal A_{M,D})=\deg_D(p)<2D.                   \tag{7.1}
$$



The two valuations are unequal, so the nonarchimedean equality for a
difference gives



$$
v_p(\mathcal B_{M,D})
 =\min(2D,\deg_D(p))=\deg_D(p).                         \tag{7.2}
$$



This proves (1.8)--(1.9), and in particular



$$
\boxed{
 \operatorname {rad}\gcd(\mathcal B_{M,D},R_M^{2D})
 =\mathcal C_{M,D}.}                                    \tag{7.3}
$$



The closeness in Section 6 therefore creates no candidate-prime
cancellation at all.

Moreover, $1-e^{-x}\le x$ gives



$$
0<\mathcal B_{M,D}
 \le R_M^{2D}\varepsilon_{M,D}.                        \tag{7.4}
$$



At $D\sim c\log M$,



$$
\log\mathcal B_{M,D}
 \le2D\log R_M-log M+2\log\log M+O_c(1).              \tag{7.5}
$$



Under the raw possibility $\log R_M\asymp M$, the dominant term is
$\asymp M\log M$.  The relative cancellation subtracts only
$\log M+O(\log\log M)$ from the logarithmic height.  Divisibility of
$\mathcal C_{M,D}$ into $\mathcal B_{M,D}$ therefore gives no linear
upper bound competitive with (1.10).

## 8. Exact obstruction to product cancellation and prime allocation

Sections 3--7 settle the natural aggregate attempts.

1. **Multiply endpoint evaluations.**  The result is the exact resultant
   $\mathcal A_{M,D}$, whose candidate part is the edge product (4.6).
   Multiplication records, rather than cancels, every edge.
2. **Use the near-perfect-power approximation.**  Subtracting
   $R_M^{2D}$ yields $\mathcal B_{M,D}$, but (7.2) preserves every
   candidate-prime valuation exactly.
3. **Use only the size of the difference.**  Equation (7.5) is still
   superlinear at raw capacity and cannot imply the $<(1/12-\varepsilon)M$
   target.
4. **Exploit prime allocation across shifts.**  Allocation is exactly graph
   degree.  The modulo-3 bound (5.1) limits degree to about $4D/3$, but
   the cluster radical depends only on whether degree is positive.  No
   vertex-count saving follows.

Hence the following method class is closed:

> Aggregate the exact endpoint norms over $d\le D$, compare the aggregate
> with $R_M^{2D}$, subtract the near perfect power, and use only the
> resulting integer height or the allocation multiplicities.

This no-go is tied to the actual factors $F_M(\pm2d)$, their common
resultant, and their exact candidate-prime valuations.  It is stronger than
a generic statement that the individual norms are large.

The theorem does not rule out a new gate-specific relation forcing most
vertices to have degree zero, an external small carrier for the edge
product, or an average-gcd theorem using the actual Hasse--transverse
coefficients before they are compressed into $F_M$.

## 9. Remaining admission target

Item 395's master inequality remains the decision test.  At
$D\sim c\log M$, a strict saving requires



$$
\limsup {1\over M}\log\mathcal C_{M,D}
 <{2c-1\over12c},qquad c>{1\over2}.                   \tag{9.1}
$$



At $c=1$, the coefficient must be strictly below $1/12$.  Equations
(1.5) and (1.9) say that an equivalent target is a strict bound for the
radical of the candidate-prime part of either $\mathcal A_{M,D}$ or
$\mathcal B_{M,D}$.  Their total integer heights do not supply it.

The smallest live inputs are now:

1. a theorem bounding the number or weighted mass of positive-degree
   vertices in the actual collision graph;
2. a gate-specific carrier for the edge product in (4.6) of logarithmic
   height below (9.1);
3. an average-gcd estimate for
   $\gcd(R_M^{2D},\mathcal A_{M,D})$ that uses more than its two heights;
4. arithmetic information on the original Hasse--transverse moments that
   prevents simultaneous roots before the CRT/root-product compression.

## 10. Deterministic replay and finite-data policy

The standard-library certificate pins all Item 395 artifacts and verifies,
on four predeclared root sets inside actual candidate intervals:

1. the aggregate resultant/product identity;
2. every collision-graph degree and candidate-prime valuation;
3. the edge-product identity (4.6);
4. the modulo-3 degree bound;
5. equality of the candidate parts of $\mathcal A$ and $\mathcal B$;
6. the cluster radical recovered from both gcds; and
7. the exact rational parameter in (6.3).

The declared root sets are algebraic controls only.  They are not claimed
to be actual collision sets.  No actual gate scan, zero census, optimization,
or finite-to-infinite inference is performed.

From the archive root run

```text
python scripts/item398_j1_aggregate_endpoint_resultant_graph_valuation_no_go_certificate.py \
  --output results/item398_j1_aggregate_endpoint_resultant_graph_valuation_no_go_certificate_replay.json
```

The replay must be byte-identical to the shipped certificate.

## 11. Strict decision and ledger

### PROVED

- the aggregate endpoint resultant (1.3);
- exact collision-graph valuations and the edge-product identity;
- the modular degree bound $D+\lfloor D/3\rfloor$;
- the near-perfect-power estimate with leading constant $c^3/8$;
- exact preservation of all candidate-prime valuations after subtraction;
- the scoped aggregate-product/near-power-cancellation/degree-allocation
  no-go;
- zero booking and retention of the $1/36$ ceiling.

### CONDITIONAL TARGETS ONLY

- any strict bound satisfying (9.1);
- any gate-specific positive-degree vertex bound;
- any strict whole-cell capacity reduction.

### DECLARED EXACT CONTROLS ONLY

- four abstract root sets at $M=180,300$;
- no collision scan and no finite density inference.

### OPEN

- an actual arithmetic upper bound for $\log\mathcal C_{M,D}$;
- logarithmic-window weighted zero density;
- $W(M)=o(M)$, any new Route-1 booking, and every conclusion about
  $e+\pi$.



$$
\boxed{
 \text{new proved linear log rate}=0,\quad
 \text{new booked mass}=0,\quad
 \text{new whole-cell capacity reduction}=0.}          \tag{11.1}
$$


