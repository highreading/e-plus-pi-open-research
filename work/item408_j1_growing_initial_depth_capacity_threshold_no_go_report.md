> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 408 — the linear-depth barrier for initial-orbit exclusions and the exact shortened-interval cluster coefficient

Date: 2026-09-01

## 1. Outcome and capacity decision first

Retain the actual fixed-$j=1$ family



$$
p=4h+6s+3,\qquad M=3h+4s+2,\qquad h,s\geq1,
 \tag{1.1}
$$



and Item 401's fixed-prime column.  Its lower endpoint and column age are



$$
M_{p,0}=\left\lceil{2p+1\over3}\right\rceil,
 \qquad a_p(M)=M-M_{p,0}.                              \tag{1.2}
$$



Item 405 proves that the actual joint Hasse--transverse gate is absent for
the first three levels $a_p=0,1,2$.  It also proves that those finitely
many levels remove only $O(\log M)$ weight and cannot change Item 395's
strict logarithmic-cluster target



$$
\log\mathcal C_{M,D}<
 \left(a(c)-\varepsilon\right)M,
 \qquad
 a(c)={2c-1\over12c},\quad D\sim c\log M,\quad c>{1\over2}.
 \tag{1.3}
$$



This item performs the capacity screen for a genuinely growing initial
depth $B=B(M)$.  Its outcome is stronger than the bounded-depth closure.

1. **PROVED — exact endpoint localization for every depth.**  The first
   $B$ levels at fixed $M$ are exactly the candidate primes in one top
   interval:
   

$$
a_p(M)<B
    \quad\Longleftrightarrow\quad
    p>{3M-3B-1\over2}=U_M-{3B\over2}.                 \tag{1.4}
$$


   Thus retaining ages $a_p\ge B$ shortens the tied candidate interval
   by precisely $3B/2$, up to its rational endpoint convention.

2. **PROVED — every sublinear depth has zero linear rate.**  If
   $B(M)=o(M)$, the ambient prime logarithmic weight in the retained
   interval is still
   

$$
{M\over6}+o(M).                                  \tag{1.5}
$$


   Hence the excluded initial strip has weight $o(M)$.  This closes not
   merely bounded or sublogarithmic depth, but the entire sublinear class.

3. **PROVED — the exact shortened-interval witness coefficient.**  If
   $B(M)/M\to b$, put
   

$$
r(b)=\max\left(0,{1\over6}-{3b\over2}\right).
                                                               \tag{1.6}
$$


   The maximal selector permitted by an initial-strip theorem has a
   logarithmic-window cluster radical satisfying
   

$$
\liminf {1\over M}\log\mathcal C^{(B)}_{M,D}
    \ge a_b(c):=r(b)\left(1-{1\over2c}\right).        \tag{1.7}
$$


   At $b=0$, this is exactly Item 395's coefficient $a(c)$.  At
   $c=1$ and $0\le b\le1/9$,
   

$$
a_b(1)={1\over12}-{3b\over4}.                  \tag{1.8}
$$



4. **PROVED — the first capacity-relevant depth scale is linear.**  A
   positive change in linear logarithmic mass requires
   $B(M)=\Omega(M)$, not $M/\log M$.  To reduce the witness coefficient
   by $\varepsilon$ at a fixed $c$, it is necessary that
   

$$
{B(M)\over M}\ \text{reach at least}\
       {4c\varepsilon\over3(2c-1)}.                   \tag{1.9}
$$


   At $c=1$, the required ratio is at least $4\varepsilon/3$.
   This is necessary only to escape the support witness; it is not an
   actual-orbit theorem and is not sufficient by itself.

No growing-depth actual gate exclusion is proved here.  No recurrence
interpolation model is identified with actual values, and no cross-prime
resultant or reciprocity law is claimed.  The proved result is a global,
sharp capacity no-go for any continuation whose only new arithmetic
conclusion is exclusion of a sublinear initial strip.  Therefore



$$
\boxed{
 \text{new booking}=0,\qquad
 \text{new whole-cell capacity reduction}=0,\qquad
 \text{retained fixed-}j=1\text{ ceiling}=1/36.}
 \tag{1.10}
$$



## 2. Pinned setup and the growing-depth information class

Items 391, 395, and 400 use the tied candidate interval



$$
L_M={4M+3\over3},\qquad
 U_M={3M-1\over2},\qquad
 H_M=U_M-L_M={M-9\over6},                             \tag{2.1}
$$



and



$$
\mathcal P_M=\{p\text{ prime}:L_M\le p\le U_M\}.   \tag{2.2}
$$



Solving (1.1) gives



$$
h=3M-2p,\qquad s={3p-4M-1\over2}.                   \tag{2.3}
$$



Thus (2.2) is exactly the set of prime characteristics for which
$h,s\ge1$.  Item 401 proves that fixed $p$ occurs on the consecutive
block



$$
I_p=\left[
 \left\lceil{2p+1\over3}\right\rceil,
 \left\lfloor{3p-3\over4}\right\rfloor
 \right]\cap\mathbb Z                                \tag{2.4}
$$



and moves by



$$
(M,h,s,p)\longmapsto(M+1,h+3,s-2,p).                \tag{2.5}
$$



For an integer depth $B\ge0$, define the initial strip and its
complement by



$$
\mathcal J_M(B)=\{p\in\mathcal P_M:a_p(M)<B\},
 \qquad
 \mathcal A_M(B)=\mathcal P_M\setminus\mathcal J_M(B).
 \tag{2.6}
$$



The **initial-strip information class at depth $B$** consists of
arguments whose only new selector-specific conclusion is



$$
\mathcal Z_M\subseteq\mathcal A_M(B),               \tag{2.7}
$$



together with the already-pinned support, prime-distribution, packing, and
same-prime recurrence facts.  An explicit consequence of the actual
Item 401 operator after its determining state, a later-orbit congruence,
or an equation containing two distinct residue characteristics is outside
this class.

The witness used below is $\mathcal A_M(B)$ itself.  It is an abstract
support witness showing what (2.7) alone permits.  It is not asserted to
be the actual gate set, the actual Hasse orbit, or the output of the actual
Item 401 recurrence.  When $B<3$, the already-proved Item 405 input is
respected by using $\mathcal A_M(\max(B,3))$.  This fixed replacement
does not change any limiting ratio or coefficient below, so the notation
$\mathcal A_M(B)$ is retained.

## 3. Exact all-depth endpoint lemma

Because $M-B$ is an integer, the elementary equivalence



$$
\lceil x\rceil>M-B\quad\Longleftrightarrow\quad x>M-B
 \tag{3.1}
$$



gives



$$
\begin{aligned}
 a_p(M)<B
 &\Longleftrightarrow
 M-\left\lceil{2p+1\over3}\right\rceil<B\\
 &\Longleftrightarrow
 \left\lceil{2p+1\over3}\right\rceil>M-B\\
 &\Longleftrightarrow {2p+1\over3}>M-B\\
 &\Longleftrightarrow p>{3M-3B-1\over2}.
\end{aligned}                                         \tag{3.2}
$$



Put



$$
T_{M,B}:={3M-3B-1\over2}=U_M-{3B\over2}.            \tag{3.3}
$$



Then the exact set identities are



$$
\boxed{
 \mathcal J_M(B)=\mathcal P_M\cap(T_{M,B},U_M],
 \qquad
 \mathcal A_M(B)=\mathcal P_M\cap[L_M,T_{M,B}].}
 \tag{3.4}
$$



The retained real interval has length



$$
H_{M,B}=\max(0,T_{M,B}-L_M)
 =\max\left(0,{M-9-9B\over6}\right).                 \tag{3.5}
$$



This identity is the smallest actual structural lemma needed for the
capacity screen.  It uses the genuine Item 401 column endpoints, not an
interpolation model.  It also explains why counting levels as though each
carried logarithmic mass $\log M$ gives the wrong critical scale: primes
in a growing numerical interval have Chebyshev mass proportional to the
interval length, not to the number of integer levels times $\log M$.

## 4. Global sublinear-depth zero-rate theorem

Let $B(M)=o(M)$.  Then



$$
{T_{M,B}\over M}\to{3\over2},\qquad
 {L_M\over M}\to{4\over3},                           \tag{4.1}
$$



so the ordinary prime number theorem, applied at the two moving linear
endpoints, gives



$$
\begin{aligned}
 \sum_{p\in\mathcal A_M(B)}\log p
 &=\vartheta(T_{M,B})-\vartheta(L_M^-)\\
 &=T_{M,B}-L_M+o(M)\\
 &={M-9-9B\over6}+o(M)
 ={M\over6}+o(M).                                    
\end{aligned}                                         \tag{4.2}
$$



The full candidate interval has weight $M/6+o(M)$.  Subtracting (4.2)
therefore yields



$$
\boxed{
 \sum_{p\in\mathcal J_M(B)}\log p=o(M)
 \qquad\text{for every }B(M)=o(M).}                  \tag{4.3}
$$



No short-interval prime theorem is needed: both retained endpoints remain
fixed positive multiples of $M$, and the two standard PNT estimates are
subtracted only after retaining their $o(M)$ errors.

Equation (4.3) includes all of the following depths:



$$
O(1),\quad o(\log M),\quad (\log M)^A,\quad
 M^\alpha\ (0<\alpha<1),\quad {M\over\log\log M},
 \tag{4.4}
$$



and every other sublinear function.  A theorem excluding any such strip
may be arithmetically genuine, as Item 405's depth-three theorem is, but
the strongest direct change it can force in a linear logarithmic capacity
coefficient is zero.

## 5. Exact cluster witness after a growing exclusion

Join two primes of $\mathcal A_M(B)$ when their numerical distance is at
most $2D$, and let $\mathcal C^{(B)}_{M,D}$ be the radical of the
positive-degree vertices.  Let $\mathcal I^{(B)}_{M,D}$ be the isolated
vertices.  Distinct isolated primes are more than $2D$ apart in an
interval of length $H_{M,B}$.  Therefore



$$
|\mathcal I^{(B)}_{M,D}|
 \le1+\left\lfloor{H_{M,B}\over2D}\right\rfloor,    \tag{5.1}
$$



with the evident empty-set interpretation, and



$$
\begin{aligned}
 \log\mathcal C^{(B)}_{M,D}
 &\ge \vartheta(T_{M,B})-\vartheta(L_M^-)\\
 &\quad-
 \left(1+{H_{M,B}\over2D}\right)\log U_M.           
\end{aligned}                                         \tag{5.2}
$$



Suppose



$$
{B(M)\over M}\to b\ge0,
 \qquad D\sim c\log M,qquad c>{1\over2}.           \tag{5.3}
$$



The PNT at the two linear endpoints gives the retained-mass coefficient



$$
r(b)=\max\left(0,{1\over6}-{3b\over2}\right).       \tag{5.4}
$$



The packing term in (5.2) has coefficient $r(b)/(2c)$.  Hence



$$
\boxed{
 \liminf_{M\to\infty}{1\over M}
 \log\mathcal C^{(B)}_{M,D}
 \ge
 a_b(c):=r(b)\left(1-{1\over2c}\right).}             \tag{5.5}
$$



For $b=0$,



$$
a_0(c)={1\over6}\left(1-{1\over2c}\right)
 ={2c-1\over12c}=a(c),                               \tag{5.6}
$$



which is exactly Item 395's strict admission coefficient and Item 400's
ambient lower coefficient.  Thus, for every $B=o(M)$, the permitted
selector still violates every proposed uniform bound



$$
\log\mathcal C_{M,D}\le(a(c)-\varepsilon)M+o(M).
 \tag{5.7}
$$



At the standard choice $c=1$, (5.5) reads



$$
\boxed{
 a_b(1)=\max\left(0,{1\over12}-{3b\over4}\right).}   \tag{5.8}
$$



The cutoff $b=1/9$ is also exact: at that depth the shortened interval
has zero linear length, and a slightly larger depth eventually covers the
whole candidate interval.

## 6. Three quantitative depth thresholds

The word "capacity-relevant" can refer to three distinct tests.  They
should not be conflated.

### 6.1 Affecting any linear support mass

For $0\le b\le1/9$, the excluded upper interval has Chebyshev mass



$$
{3b\over2}M+o(M).                                    \tag{6.1}
$$



Thus removing $\eta M$ ambient logarithmic mass requires



$$
b\ge {2\eta\over3}.                                 \tag{6.2}
$$



In particular, a positive linear effect requires $b>0$, i.e.
$B=\Omega(M)$.  This is the first admissible scale.  The tempting
$M/\log M$ estimate comes from assigning $\log M$ to every integer
level; it ignores the prime density and is not the actual mass scale.

### 6.2 Escaping the shortened-interval cluster witness

For $0\le b\le1/9$, subtract (5.5) from (5.6):



$$
a(c)-a_b(c)
 ={3b\over2}\left(1-{1\over2c}\right)
 ={3b(2c-1)\over4c}.                                 \tag{6.3}
$$



Therefore a claimed improvement of $\varepsilon M$ below Item 395's
coefficient is still contradicted by the permitted selector unless



$$
\boxed{
 b\ge {4c\varepsilon\over3(2c-1)}.}                  \tag{6.4}
$$



At $c=1$, this is $b\ge4\varepsilon/3$.  Equation (6.4) is a
necessary threshold for escaping this information-class witness.  It does
not prove that an actual orbit exclusion at that depth exists, nor that
such an exclusion controls the later orbit.

### 6.3 Passing Item 395 by support deletion alone

If an actual theorem did prove exclusion through depth $B\sim bM$, then
the trivial upper bound $\mathcal C_{M,D}\mid\prod_{p\in\mathcal A_M(B)}p$
would have coefficient $r(b)$.  To make this bound itself satisfy



$$
r(b)<a(c)-\varepsilon,                               \tag{6.5}
$$



one needs



$$
\boxed{
 b>{1\over18c}+{2\varepsilon\over3}.}                \tag{6.6}
$$



At $c=1$, even an arbitrarily small strict margin requires depth just
over $M/18$ if strip deletion is the only cluster input.  A smaller
positive linear depth would still improve the raw support ceiling
conditionally, but would need additional arithmetic clustering control to
pass Item 395's sharper test.

Equations (6.2), (6.4), and (6.6) are respectively a mass threshold, a
necessary witness-escape threshold, and a sufficient support-only
admission threshold.  Only the first scale statement and the no-go are
unconditional here; all positive savings remain conditional on a new
actual-orbit theorem.

## 7. Relation to Items 401 and 405

Item 401 proves bounded-rank same-characteristic transport and explains
why recurrence existence alone does not couple distinct prime columns.
Item 405 then computes the two exact depth-three initial states and proves
actual joint-gate nonvanishing throughout them.  It uses a separately
labelled polynomial interpolation model only to close a bounded-depth
recurrence information class.

This item neither extends that interpolation model nor turns it into an
actual value theorem.  Its witness is only the set
$\mathcal A_M(B)$, used to test what an initial-strip conclusion by
itself can force.  In particular:

1. no value of $Q_0$, $Q_1$, or $E_h^*$ beyond Item 405's six exact
   initials is asserted;
2. no recurrence coefficient is guessed or fitted;
3. no full-minus-strip selector is claimed to satisfy the distinguished
   actual Item 401 operator;
4. no finite control is promoted to an infinite gate statement; and
5. the actual depth-three exclusion is still booked at zero linear rate,
   not counted once per column as positive capacity.

The smallest live growing-depth lemma is now precise: to obtain any direct
linear saving from initial-orbit exclusion, one must prove actual joint-gate
nonvanishing uniformly through $B\sim bM$ levels for some fixed $b>0$,
or prove an equivalent positive-linear weighted exclusion.  To meet the
cluster test by that exclusion alone, $b$ must satisfy (6.6).  An
operator-specific theorem that controls later zeros without excluding a
contiguous initial strip could be stronger and lies outside this no-go.

The other live route is a genuine cross-prime law: an identity involving
the $p$- and $q$-columns simultaneously when
$0<|p-q|\le2\log M$.  Same-prime vertical transport and the endpoint
lemma contain no such coupling.

## 8. Deterministic replay and finite-data policy

The standard-library checker pins canonical Items 391, 395, 400, 401 and
the complete work Item 405 package.  It verifies:

1. the exact candidate equations and the age/endpoint equivalence (3.2)
   on four declared structural grids and every declared depth;
2. the retained interval length (3.5);
3. finite cluster/isolated partitions and the exact packing bound (5.1);
4. the rational formulas $r(b)$, $a_b(c)$, and their specializations;
5. equality $a_0(c)=(2c-1)/(12c)$, including $a_0(1)=1/12$; and
6. the cutoff $r(1/9)=0$.

The finite prime grids are structural controls only.  They are not actual
joint-gate zero sets, and no asymptotic prime or gate density is inferred
from them.  The asymptotic statements are proved from the ordinary prime
number theorem and packing in Sections 4--6.

From the archive root run

~~~text
python work/item408_j1_growing_initial_depth_capacity_threshold_no_go_certificate.py \
  --output work/item408_j1_growing_initial_depth_capacity_threshold_no_go_certificate_replay.json
~~~

The replay must be byte-identical to the shipped certificate.

## 9. Strict decision and ledger

### PROVED

- the exact all-depth endpoint localization (3.4);
- the exact retained interval length (3.5);
- zero linear mass for every sublinear depth $B=o(M)$;
- the global support-information-class no-go for all such depths;
- the shortened-interval cluster lower coefficient (5.5);
- exact recovery of Item 395's coefficient at $b=0$;
- the linear minimum scale and quantitative thresholds (6.2), (6.4), and
  (6.6);
- zero new booking and retention of the $1/36$ ceiling.

### DECLARED EXACT CONTROL ONLY

- four finite prime grids, their endpoint splits, and their cluster
  partitions;
- no actual-gate or density inference from those grids.

### NOT AN ACTUAL-ORBIT CLAIM

- $\mathcal A_M(B)$ is an information-class support witness only;
- no recurrence interpolation countermodel is promoted to an actual value;
- no actual exclusion beyond Item 405's first three levels is claimed.

### OUTSIDE THE CLOSED CLASS

- the explicit actual recurrence operator plus determining state used to
  prove later-orbit nonconcentration;
- a non-contiguous positive-linear weighted exclusion;
- a genuine cross-prime resultant, reciprocity, or common subthreshold
  carrier.

### OPEN

- every actual growing-depth joint-gate theorem beyond depth three;
- the actual logarithmic-window cluster-radical upper bound;
- $W_{H\mathscr T}(M)=o(M)$ or any strict fixed-$j=1$ retained
  constant;
- any new Route-1 booking and every conclusion about $e+\pi$.



$$
\boxed{
 \text{new proved linear log rate}=0,\quad
 \text{new booked mass}=0,\quad
 \text{new whole-cell capacity reduction}=0.}        \tag{9.1}
$$


