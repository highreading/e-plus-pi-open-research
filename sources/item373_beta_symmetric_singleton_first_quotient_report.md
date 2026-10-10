> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 373 — the actual symmetric singleton carrier and its first quotient

Checked: 2026-09-01 (Beijing time)

## 1. Verdict and capacity admission

Item 370 leaves two q-free possibilities: a correlation holding only at the
unique actual canonical point, or a full-support degree-$N$ state.  Item 373
studies the most canonical such states, the top two elementary symmetric
functions of the actual nonzero loads.

Let



$$
P_n=\prod_{j\in\mathcal J_n}Z_{j,n},
\qquad
E_n=e_{N-1}(Z)
=\sum_{j\in\mathcal J_n}\frac{P_n}{Z_{j,n}},
\qquad
N=|\mathcal J_n|.
\tag{1.1}
$$



Item 373 proves three exact results.

1. There is a prime-independent symmetric saturation
   

$$
S_n^{\rm sym}
   =\frac{P_n}{\gcd(P_n,(|t_n|E_n)^N)}
$$


   whose primes larger than $A$ are exactly the $t$-avoiding singleton
   incidences, each with exponent one.
2. At every genuine singleton prime $p>A$, one has
   

$$
v_p(P_n)=1,
   \qquad
   E_n\in\mathbb Z_p^\times,
   \qquad
   \frac{P_n/p}{E_n}\equiv\frac{Z_{j(p),n}}p\not\equiv0\pmod p.
$$


   Thus the top symmetric product has no second $p$-adic digit to exploit.
3. For a bounded-degree top-symmetric first-quotient residual
   $C_n(E_n)/D_n$ with coefficient and denominator height $b^{o(1)}$, a
   nonconstant $C_n$ cannot have sub-beta value on a positive-singleton-mass
   subsequence.  The only sub-beta case is again a constant/content residual.

The first result is a genuine actual-family formula, but its raw height is at
most two beta copies and intersection with $Q^{[1]}$ returns the old one-copy
ceiling.  The second and third results are scoped no-go theorems.  No nonzero
sub-beta carrier is constructed, so booking is zero.

## 2. Actual loads and the top symmetric pair

Assume the genuine Item-316 target at $n\ge5$.  It fixes the unique canonical
word, endpoint, sign, and actual loads.  Remove every exact-zero integer load
and write



$$
\mathcal J=\{j:Z_j\ne0\},
\qquad
N=|\mathcal J|.
\tag{2.1}
$$



If $N=0$, then the singleton carrier is $1$ and the branch is trivial.  Below
assume $N\ge1$.  Canonical digit bounds give



$$
0<Z_j<A^2.
\tag{2.2}
$$



For a prime $p>A$, define its actual incidence count



$$
k_p=\#\{j\in\mathcal J:p\mid Z_j\}.
\tag{2.3}
$$



Because $p^2>A^2>Z_j$, every hit is simple:



$$
v_p(Z_j)\in\{0,1\},
\qquad
v_p(P)=k_p.
\tag{2.4}
$$



The top derivative $E=e_{N-1}(Z)$ detects the singleton stratum exactly:



$$
\boxed{
k_p=1\Longrightarrow p\nmid E,
\qquad
k_p\ge2\Longrightarrow p\mid E.}
\tag{2.5}
$$



Indeed, when $k_p=1$, exactly one summand $P/Z_j$ is a $p$-unit.  When
$k_p\ge2$, every summand still contains at least one hit factor.

This uses the actual positive integer loads and their tied size range; it is
not the generic chart saturation already proved in Item 370.

## 3. Exact symmetric saturation

Define



$$
\boxed{
S^{\rm sym}
=
\frac{P}{\gcd(P,(|t|E)^N)}.}
\tag{3.1}
$$



Fix $p>A$.  There are four cases.

* If $k_p=0$, then $p\nmid P$.
* If $k_p=1$ and $p\nmid t$, then $p\nmid tE$, so (2.4) gives
  $v_p(S^{\rm sym})=1$.
* If $k_p=1$ and $p\mid t$, then
  $v_p((tE)^N)\ge N\ge v_p(P)$, so the full factor is removed.
* If $k_p\ge2$, then $p\mid E$ and
  $v_p((tE)^N)\ge N\ge k_p=v_p(P)$, so again the full factor is removed.

Therefore



$$
\boxed{
v_p(S^{\rm sym})
=
\begin{cases}
1,&p\nmid t\text{ and }k_p=1,\\
0,&\text{otherwise},
\end{cases}
\qquad(p>A).}
\tag{3.2}
$$



If $t=0$, then (3.1) gives $S^{\rm sym}=1$, as it should.  Let
$\operatorname{rad}_{>A}$ retain only prime divisors larger than $A$.  The
actual Item-358 singleton carrier now has the exact symmetric formula



$$
\boxed{
\mathcal U_{1,1}
=
\gcd\!\left(
Q^{[1]},
\operatorname{rad}_{>A}(S^{\rm sym})
\right).}
\tag{3.3}
$$



This is prime-independent and imposes genuine earlier- and later-row
avoidance through $E$, not through a selected-hit surrogate.

## 4. Capacity audit of the symmetric carrier

Since $S^{\rm sym}\mid P$ and $Z_j<A^2$,



$$
\log S^{\rm sym}
\le\log P
=\sum_{j\in\mathcal J}\log Z_j
<2N\log A.
\tag{4.1}
$$



With $N\le n-4$ and $\log b=(1+o(1))n\log A$,



$$
\boxed{
\log S^{\rm sym}\le(2+o(1))\log b.}
\tag{4.2}
$$



After the intersection in (3.3), one only recovers



$$
\log\mathcal U_{1,1}\le\log Q\le\log b.
\tag{4.3}
$$



Thus (3.3) is an exact structural compression from exponentially many
incidence subsets to two symmetric integers, but it gives no new exponent
bound.  No mass is booked from the formula alone.

## 5. Exact first quotient at a singleton prime

Let $p\in\mathcal P_{1,1}$ and let $j(p)$ be its unique hit row.  Equations
(2.4)-(2.5) give



$$
v_p(P)=1,
\qquad
v_p(E)=0.
\tag{5.1}
$$



Modulo $p$, the unique unit summand of $E$ is



$$
E\equiv\prod_{i\ne j(p)}Z_i\pmod p.
\tag{5.2}
$$



Therefore



$$
\boxed{
\frac{P}{p}E^{-1}
\equiv
\frac{Z_{j(p)}}p
\pmod p.}
\tag{5.3}
$$



The actual tied size gives



$$
1\le\frac{Z_{j(p)}}p<\frac{A^2}{p}<A<p.
\tag{5.4}
$$



Hence the right side of (5.3) is never zero.  In particular,



$$
\boxed{p^2\nmid P.}
\tag{5.5}
$$



More generally, for every fixed $r\ge0$ and every rational denominator $V$
which is a $p$-unit at the actual point,



$$
v_p\!\left(\frac{PE^r}{V}\right)=1
\tag{5.6}
$$



whenever the quotient is defined.  Thus powers of the top derivative,
endpoint-unit denominators, and monomial top-symmetric quotients cannot create
an extra digit.  This is an actual-family valuation theorem, not a finite
zero census.

## 6. General first-quotient reduction

Let $C_n(T)\in\mathbb Z[T]$ be prime-independent and let $V_n$ be a $p$-unit
at every actual singleton prime.  For



$$
F_n=\frac{P_nC_n(E_n)}{V_n},
\tag{6.1}
$$



one has the exact equivalence



$$
\boxed{
v_p(F_n)\ge2
\iff
p\mid C_n(E_n)
\qquad(p\in\mathcal P_{1,1}).}
\tag{6.2}
$$



Thus every proposed first-quotient lift in this class simply transfers the
whole problem to the q-free integer $C_n(E_n)$.  A finite portfolio transfers
it to



$$
H_n=\prod_{\ell=1}^{L}C_{\ell,n}(E_n).
\tag{6.3}
$$



If the portfolio forces an extra digit for every actual singleton prime, then



$$
\mathcal U_{1,1}(n)\mid H_n.
\tag{6.4}
$$



Equation (6.4) would be a real carrier only if a new upper bound for $H_n$
beats one beta copy.  The next section rules out sub-beta height for the
bounded-degree nonconstant class on any positive-mass subsequence.

## 7. Bounded-degree top-symmetric no-go

Assume along a subsequence that



$$
\log\mathcal U_{1,1}\ge\eta\log b
\tag{7.1}
$$



for a fixed $\eta>0$.  A load $Z_j<A^2$ contains at most one prime larger
than $A$.  Since every such prime has logarithm below $2\log A$, (7.1)
requires at least



$$
r\ge\frac{\eta\log b}{2\log A}
=\left(\frac\eta2+o(1)\right)n
\tag{7.2}
$$



distinct singleton rows whose loads exceed $A$.

Choose one of those rows in a summand $P/Z_j$ of $E$.  The remaining product
contains at least $r-1$ loads larger than $A$.  Hence



$$
\boxed{
E>A^{r-1},
\qquad
\log E\ge\left(\frac\eta2+o(1)\right)\log b.}
\tag{7.3}
$$



Now let



$$
C_n(T)=c_{d,n}T^d+\cdots+c_{0,n},
\qquad
1\le d\le d_0,
\tag{7.4}
$$



where $d_0$ is fixed, $c_{d,n}\ne0$, and



$$
\max_i|c_{i,n}|\le B_n,
\qquad
\log B_n=o(\log b).
\tag{7.5}
$$



For large $n$, (7.3) gives $E>2dB_n$.  The leading term dominates:



$$
\boxed{
|C_n(E)|
\ge E^d-dB_nE^{d-1}
\ge\frac12E^d.}
\tag{7.6}
$$



If the first-quotient residual is the integer



$$
R_n=\frac{C_n(E_n)}{D_n},
\qquad
1\le D_n\le B_n,
\tag{7.7}
$$



then



$$
\log|R_n|
\ge d\log E-o(\log b)
\ge\left(\frac{d\eta}{2}+o(1)\right)\log b.
\tag{7.8}
$$



It is not sub-beta.  The same conclusion holds for a fixed product portfolio
if at least one factor is nonconstant and the total clearing denominator has
sub-beta height.

Therefore the only sub-beta member of this bounded-degree univariate class is
a constant/content residual.  If a nonzero constant residual satisfies
(6.4), it immediately proves zero rate; no such actual divisibility theorem
is known.  The zero polynomial is inadmissible.

Equation (7.8) is scoped to sub-beta residuals.  It does not claim a useful
upper bound for $C_n(E_n)$, nor does it exclude a quotient with a beta-height
denominator or a new gcd cancellation.

## 8. Surviving symmetric directions

The following remain open.

1. A multivariate polynomial in several elementary symmetric functions with
   actual cancellations not reducible to $C(E)$.
2. A beta-height denominator or gcd/radical quotient whose cancellation can
   be bounded arithmetically.
3. A full-support recurrence with linear load degree but a nontrivial height
   theorem beyond (4.2).
4. A nonzero constant/content residual forced by the actual canonical point.

These require new arithmetic.  Neither generic saturation nor the exact
first quotient supplies them.

## 9. Strict labels

### PROVED

* The actual top-symmetric incidence detector (2.5).
* The exact symmetric saturation and carrier (3.1)-(3.3).
* The singleton valuation-one and first-quotient bridge (5.1)-(5.5).
* The general top-symmetric first-quotient reduction (6.2).
* The positive-mass lower bound for $E$ and polynomial dominance
  (7.2)-(7.8).
* Zero booking.

### PROVED SCOPED NO-GO

* $P$, $PE^r$, and their $p$-unit monomial quotients as extra-digit
  mechanisms.
* Nonconstant fixed-degree $C_n(E_n)$ with sub-beta coefficient and clearing
  denominator height as a sub-beta carrier on a positive-mass branch.
* Finite products of such factors when at least one is nonconstant.

### EXACT FINITE ONLY

* The replay's declared incidence subsets, symmetric saturations, quotient
  bridges, polynomial coefficient boxes, and height-scale rows.
* No declared prime or load vector is promoted to an actual beta target or
  density datum.

### OPEN

* Multivariate elementary-symmetric cancellation.
* Beta-height denominators and gcd/radical quotient compression.
* Full-support degree-$N$ recurrence height beyond the raw product.
* A nonzero constant/content residual with actual $\mathcal U_{1,1}$
  divisibility.
* The singleton bound, growing low incidence, $\Xi_Q$, squarefull excess,
  beta capacity, Route 1, and $e+\pi$.

### BOOKING



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new Route-1 rate}=0.}
\tag{9.1}
$$



No canonical, master, status, checkpoint, or research-log file is edited by
this work package.

## 10. Deterministic replay

From the archive root:

~~~text
python work/item373_beta_symmetric_singleton_first_quotient_certificate.py ^
  --output work/item373_beta_symmetric_singleton_first_quotient_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer
arithmetic.  It performs no actual prime census, target search, factorization,
or half-bound scan.
