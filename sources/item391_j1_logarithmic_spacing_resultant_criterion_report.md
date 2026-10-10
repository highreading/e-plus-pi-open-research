> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 391 — the actual fixed-$j=1$ collision polynomial, a logarithmic spacing criterion, and the sublogarithmic cluster closure

Date: 2026-09-01

## 1. Outcome and strict scope

Keep Item 363's *actual* fixed-$j=1$ joint Hasse--transverse envelope.  At
fixed $M$, set



$$
\mathcal P_M=
 \left\{p\text{ prime}:{4M+3\over3}\le p\le {3M-1\over2}\right\},
 \qquad
 \mathcal Z_M=
 \{p\in\mathcal P_M:p\mid R_{H\mathscr T}(M)\}.       \tag{1.1}
$$



Thus $\mathcal Z_M$ is defined by the actual selected Hasse coordinate and
the actual transverse period, not by an ambient selector.  Write



$$
W_{H\mathscr T}(M)=\sum_{p\in\mathcal Z_M}\log p,
 \qquad N_M=|\mathcal Z_M|.                             \tag{1.2}
$$



This item proves three scoped results.

1. **PROVED — exact actual-family shifted identities.**  The monic collision
   polynomial
   

$$
F_M(X)=\prod_{p\in\mathcal Z_M}(X-p)\in\mathbb Z[X] \tag{1.3}
$$


   gives an exact shifted resultant whose vanishing is equivalent to an
   actual pair of joint-gate primes.  Evaluating $F_M$ at $\pm2d$ also
   gives exact gcd formulas for the lower and upper endpoint radicals of
   every such pair.

2. **PROVED — growing sublogarithmic clusters have zero rate.**  If
   $D=D(M)=o(\log M)$, then the total logarithmic weight of members of
   $\mathcal Z_M$ which have another member within $D$ fixed-$M$ row
   steps is $o(M)$.  This is an unconditional actual-family theorem.  It
   extends Item 279 from fixed $D$ to every sublogarithmic $D(M)$, using
   a uniform Selberg prime-pair bound and an exact average singular-series
   estimate.

3. **PROVED — logarithmic scale is the spacing threshold.**  Nonvanishing
   of all actual shifted resultants through $D\sim c\log M$ would retain at
   most $1/(72c)$ per $6M$.  This is strictly below the raw $1/36$
   ceiling exactly when $c>1/2$.  Nonvanishing through
   $D/\log M\to\infty$ would prove $W_{H\mathscr T}(M)=o(M)$.  Conversely,
   positive normalized mass forces a vanishing resultant at an offset
   $O(\log M)$, with the reciprocal constant made explicit below.

The missing nonvanishing/occupancy input is **not proved**.  In particular,
this item does not prove a strict retained constant for the whole cell and
does not prove $W_{H\mathscr T}(M)=o(M)$.  The new booking and the new
capacity reduction are both zero.  What is closed is the possibility that
fixed or growing-sublogarithmic collision clusters alone carry positive
linear mass.

## 2. The tied interval and the actual row map

Put



$$
L_M={4M+3\over3},\qquad U_M={3M-1\over2}.             \tag{2.1}
$$



The interval has the exact length



$$
U_M-L_M={M-9\over6}.                                  \tag{2.2}
$$



Every $p\in\mathcal P_M$ gives the unique actual row



$$
h_p=3M-2p,qquad s_p={3p-4M-1\over2},                  \tag{2.3}
$$



and



$$
p=4h_p+6s_p+3,qquad M=3h_p+4s_p+2.                   \tag{2.4}
$$



The fixed-$M$ step



$$
(h,s,p)\longmapsto(h-4,s+3,p+2)                       \tag{2.5}
$$



therefore identifies row offset $d$ with prime difference $2d$.
Items 216 and 217 supply no normalized cross-prime gcd bound, Item 279
settles fixed windows only, Item 363 gives the exact actual radical, and
Item 384 proves that ambient filtered-selector data cannot replace actual
cross-prime arithmetic.  The present construction uses (1.1) itself.

## 3. Exact shifted resultant and norm/gcd identities

Let



$$
R_M=R_{H\mathscr T}(M)=\prod_{p\in\mathcal Z_M}p,
 \qquad n=N_M.                                         \tag{3.1}
$$



The empty-set convention is $F_M=R_M=1$.  For $d\ge1$, define



$$
\Delta_{M,d}=\operatorname {Res}_X
       \bigl(F_M(X),F_M(X+2d)\bigr).                   \tag{3.2}
$$



Because both polynomials are monic and (1.3) is squarefree,



$$
\boxed{
 \Delta_{M,d}=
 \prod_{p,q\in\mathcal Z_M}(p+2d-q).}                 \tag{3.3}
$$



Consequently



$$
\boxed{
 \Delta_{M,d}=0
 \iff \exists p\in\mathcal Z_M:\ p+2d\in\mathcal Z_M.} \tag{3.4}
$$



This is an exact all-$M$ equivalence for the actual gate.  It is not a
claim that $F_M$, which encodes the still-unknown collision set, has a
smaller description than Item 363's radical.

There is also an exact aggregate gcd form.  Define



$$
\mathcal N^-_{M,d}=(-1)^nF_M(2d)
     =\prod_{q\in\mathcal Z_M}(q-2d),
 \qquad
 \mathcal N^+_{M,d}=(-1)^nF_M(-2d)
     =\prod_{q\in\mathcal Z_M}(q+2d).                  \tag{3.5}
$$



If $2d<L_M$, then for $p,q\in[L_M,U_M]$, the positive integer
$q-2d$ is smaller than $2p$.  Hence



$$
p\mid q-2d\iff q=p+2d.                                \tag{3.6}
$$



If in addition $U_M+2d<2L_M$, the same argument gives



$$
p\mid q+2d\iff p=q+2d.                                \tag{3.7}
$$



Since $R_M$ is squarefree, (3.6)--(3.7) prove



$$
\boxed{
 \gcd(R_M,\mathcal N^-_{M,d})
   =\prod_{\substack{p\in\mathcal Z_M\\p+2d\in\mathcal Z_M}}p,}
                                                               \tag{3.8}
$$





$$
\boxed{
 \gcd(R_M,\mathcal N^+_{M,d})
   =\prod_{\substack{p\in\mathcal Z_M\\p-2d\in\mathcal Z_M}}p.}
                                                               \tag{3.9}
$$



Thus (3.8) and (3.9) are exactly the lower- and upper-endpoint radicals of
the actual $2d$-pairs.  Both size hypotheses hold uniformly for
$d=o(M)$, in particular throughout every logarithmic window considered
below.

A generic height estimate for (3.3) is not enough.  When it is nonzero,



$$
\log|\Delta_{M,d}|
 \le n^2\log(U_M-L_M+2d),                              \tag{3.10}
$$



which is of order $M^2/\log M$ at raw prime density.  The useful new
input would have to control the *zero pattern* or a special factorization,
not merely invoke integrality and this height.

## 4. Exact pair-free packing and its capacity constant

Assume



$$
\Delta_{M,d}\ne0\qquad(1\le d\le D).                 \tag{4.1}
$$



All primes in (1.1) are odd for large $M$, so every difference between
two of them is even.  By (3.4), consecutive members of $\mathcal Z_M$
are then more than $2D$ apart.  Equations (2.2) and elementary packing
give the exact safe bound



$$
N_M\le 1+\left\lfloor{M-9\over12D}\right\rfloor.     \tag{4.2}
$$



Therefore



$$
\boxed{
 W_{H\mathscr T}(M)
 \le\left(1+{M-9\over12D}\right)\log U_M.}            \tag{4.3}
$$



If $D\sim c\log M$, (4.3) gives



$$
\boxed{
 \limsup_{M\to\infty}{W_{H\mathscr T}(M)\over6M}
 \le {1\over72c}.}                                    \tag{4.4}
$$



The raw Item 363 ceiling is $1/36$, so (4.4) is a strict saving exactly
when



$$
c>{1\over2}.                                          \tag{4.5}
$$



If $D=o(M)$, $D/\log M\to\infty$, and (4.1) holds through $D$,
then (4.3) proves



$$
W_{H\mathscr T}(M)=o(M).                              \tag{4.6}
$$



More generally, for $1\le D\le M$, let $K_M(D)$ be the largest number of collision primes
in any half-open interval of numerical length $2D$.  Partitioning
$[L_M,U_M]$ into such intervals gives



$$
N_M\le K_M(D)\left(2+{M-9\over12D}\right).           \tag{4.7}
$$



Hence



$$
{K_M(D)\log M\over D}\longrightarrow0
 \quad\Longrightarrow\quad W_{H\mathscr T}(M)=o(M).   \tag{4.8}
$$



For $D\sim c\log M$ and fixed $K_M(D)\le K$, the corresponding
normalized ceiling is $K/(72c)$.  Equations (4.4) and (4.8) are
**conditional criteria**: the needed actual resultant nonvanishing or
occupancy theorem remains open.

## 5. Converse: positive mass forces a logarithmic-offset pair

Suppose along a sequence of $M$'s that



$$
{W_{H\mathscr T}(M)\over6M}\ge\rho>0.                \tag{5.1}
$$



Since every collision prime is at most $U_M$,



$$
N_M\ge {6\rho M\over\log U_M}.                        \tag{5.2}
$$



For $N_M\ge2$, two consecutive collision primes have row offset $d$
satisfying the exact pigeonhole bound



$$
d\le {M-9\over12(N_M-1)}.                             \tag{5.3}
$$



Combining (5.2)--(5.3),



$$
\boxed{
 d\le(1+o(1)){\log U_M\over72\rho},
 \qquad \Delta_{M,d}=0.}                               \tag{5.4}
$$



At the full raw value $\rho=1/36$, the right side is
$(1/2+o(1))\log M$.  This matches the threshold (4.5): within the
spacing/resultant information class, a strict capacity theorem must reach
the logarithmic scale.  Fixed or sublogarithmic offset information cannot
by itself distinguish positive mass from the full ceiling.

## 6. Uniform Selberg closure of every sublogarithmic cluster window

Define the standard prime-pair counting function



$$
\pi_2(X;d)=\#\{n\le X:n\text{ and }n+2d\text{ are prime}\}. \tag{6.1}
$$



The uniform two-dimensional Selberg upper-bound sieve supplies an absolute
effective constant $C_{\rm S}$ such that, uniformly for
$1\le d\le\log X$,



$$
\pi_2(X;d)\le
 C_{\rm S}\,\mathfrak S(d){X\over(\log X)^2},          \tag{6.2}
$$



for all sufficiently large $X$, where



$$
\mathfrak S(d)=
 \prod_{\substack{q\mid d\\q>2}}{q-1\over q-2}.      \tag{6.3}
$$



This is the classical Selberg prime-pair upper bound in its uniform small-
shift form.  For completeness, sieve $n(n+2d)$ by primes up to a fixed
power of $X$.  The number of forbidden classes modulo an odd prime $q$
is two unless $q\mid d$, when it is one.  Comparing the resulting Euler
product with the dimension-two Mertens product gives exactly the factor
(6.3).  The sieve remainder and Euler-product comparison are uniform for
$d\le\log X$; all dependence on primes dividing $d$ is retained in
$\mathfrak S(d)$.  This proves (6.2) with one absolute constant rather
than the fixed-$d$ constants used in Item 279.

The average of (6.3) has an exact elementary bound.  Expanding over odd
squarefree divisors gives



$$
\mathfrak S(d)=
 \sum_{\substack{r\mid d\\r\ \mathrm{odd,\ squarefree}}}
 \prod_{q\mid r}{1\over q-2}.                          \tag{6.4}
$$



Therefore



$$
\begin{aligned}
 \sum_{d\le D}\mathfrak S(d)
 &\le D\prod_{q>2}\left(1+{1\over q(q-2)}\right)\\
 &\le D\prod_{\substack{n\ge3\\n\ \mathrm{odd}}}
          \left(1+{1\over n(n-2)}\right)\\
 &=D\prod_{k\ge1}{(2k)^2\over(2k-1)(2k+1)}
 ={\pi\over2}D<2D.                                    \tag{6.5}
\end{aligned}
$$



Let $\mathcal C_M(D)$ be the members of $\mathcal Z_M$ which have a
second member at row distance at most $D$.  Each pair is an ambient prime
pair and each pair has at most two endpoints.  Hence, using
$U_M=(3M-1)/2$, (6.2)--(6.5) give



$$
\begin{aligned}
 \sum_{p\in\mathcal C_M(D)}\log p
 &\le 2\log U_M\sum_{d\le D}\pi_2(U_M;d)\\
 &\le C_{\rm S}\pi\,{U_MD\over\log U_M}\\
 &\le\left({3\pi C_{\rm S}\over2}+o(1)\right)
       {DM\over\log M}.                               \tag{6.6}
\end{aligned}
$$



Consequently



$$
\boxed{
 D=o(\log M)\quad\Longrightarrow\quad
 \sum_{p\in\mathcal C_M(D)}\log p=o(M).}              \tag{6.7}
$$



This is an all-family theorem for the actual joint gate because
$\mathcal C_M(D)$ is a subset of the ambient prime-pair endpoints.  It
uses no finite zero census and no distribution hypothesis on the gate.
It also applies a fortiori to the original full ordinary-collision set,
which is contained in the joint-gate envelope.

The constant in (6.6) is completely separated: $C_{\rm S}$ is the one
absolute effective constant in the stated classical sieve theorem, the
exact average singular-series factor is $\pi/2$, the endpoint factor is
two, and $U_M/M\to3/2$.  The normalized rate in (6.7) is zero for every
such $D(M)$.

## 7. What arithmetic input is now minimally sufficient

Within the exact spacing/occupancy reduction, the remaining sufficient
inputs are now quantitative.

1. **Strict saving:** prove $\Delta_{M,d}\ne0$ for all
   $d\le(c+o(1))\log M$ with $c>1/2$.  The retained ceiling is then
   $1/(72c)<1/36$ per $6M$.
2. **Zero rate by pair exclusion:** prove the same through a window
   $D=o(M)$ with $D/\log M\to\infty$.
3. **Zero rate by bounded occupancy:** it is enough to prove
   $K_M(D)\log M/D\to0$, without universal pair nonvanishing.
4. **Equivalent obstruction to positive mass:** if a proposed theorem
   never reaches offsets of order $\log M$, (5.4) shows that it cannot
   exclude a positive normalized collision mass by spacing alone.

The unconditional theorem (6.7) reaches every $o(\log M)$ window but not
the logarithmic scale.  The next live arithmetic problem is therefore a
logarithmic-window theorem for the *actual* coefficients, or a different
average-gcd/factor-localization theorem that bypasses spacing.

## 8. Deterministic replay and finite-data policy

The standard-library certificate pins Items 216, 217, 279, 363, and 384 and
verifies:

1. the exact candidate interval and row bijection;
2. the collision-polynomial/resultant equivalence for predeclared subsets
   of actual candidate sets at $M=76,180$;
3. both shifted norm/gcd endpoint identities;
4. exact pair-free packing controls;
5. finite rational Wallis products; and
6. exact product/divisor-expansion controls for $\mathfrak S(d)$.

The predeclared root subsets are algebraic controls only.  They are not
asserted to be actual collision sets.  No actual collision search, zero
census, optimization, or finite-to-infinite inference is performed.  The
Selberg theorem and the asymptotic deductions are proved in Sections 5--6,
not inferred from the replay.

From the archive root run

```text
python work/item391_j1_logarithmic_spacing_resultant_criterion_certificate.py \
  --output work/item391_j1_logarithmic_spacing_resultant_criterion_certificate_replay.json
```

The replay must be byte-identical to the shipped certificate.

## 9. Strict decision and ledger

### PROVED

- the exact actual collision polynomial and shifted resultant criterion;
- the exact lower- and upper-endpoint shifted norm/gcd identities;
- the exact pair-free packing and capacity constant $1/(72c)$;
- the bounded-occupancy sufficient criterion;
- the logarithmic-offset converse for every positive normalized mass;
- the uniform growing-sublogarithmic cluster bound (6.7);
- closure of all fixed and $o(\log M)$ collision-cluster mechanisms as
  carriers of positive linear mass.

### CONDITIONAL CRITERIA ONLY

- any nonvanishing of the actual $\Delta_{M,d}$ at logarithmic or larger
  scale;
- any logarithmic-window bound on $K_M(D)$;
- any strict whole-cell capacity reduction or proof that
  $W_{H\mathscr T}(M)=o(M)$.

### DECLARED EXACT CONTROLS ONLY

- nine predeclared abstract root sets inside two actual candidate intervals;
- finite Wallis and singular-factor arithmetic checks;
- no density inference from these controls.

### OPEN

- a logarithmic-scale arithmetic theorem for the actual joint gate;
- a special factorization or useful height bound for (3.8)--(3.9);
- a strict retained constant below $1/36$ for the whole fixed-$j=1$ cell;
- any new Route-1 booking and every conclusion about $e+\pi$.



$$
\boxed{
 \text{new proved linear log rate}=0,\quad
 \text{new booked mass}=0,\quad
 \text{new whole-cell capacity reduction}=0.}          \tag{9.1}
$$



The genuine new theorem is the zero-rate classification of all
sublogarithmic clustered collision primes and the exact identification of
the logarithmic scale at which a future spacing theorem first becomes
capacity-relevant.
