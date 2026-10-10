> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 385 — aggregate fixed-$j=2$ bounded-window propagation no-go

Checked: 2026-09-01 (Beijing time)

## 1. Scope, outcome, and capacity

Retain the complete ordinary-$j=2$ fixed-$M$ family



$$
p=2r+6s+3,
 \qquad 2M=5r+14s+7,
 \qquad r\geq1\text{ odd},\quad 3\nmid r,\quad s\geq1.
\tag{1.1}
$$



Items 334 and 349 give exact target-retaining primitive carriers on the
nondegenerate and degenerate charts.  Their collision masses are disjoint
row by row but belong to the same raw interval.  This item does not replace
either carrier and does not eliminate the actual incomplete-beta target.
It instead settles, at once, every proposed **bounded-offset cross-row
propagation mechanism** that requires two actual candidate primes.

> **PROVED — complete fixed-$M$ alignment lattice.**  Consecutive
> algebraic rows have
> 

$$
> (p,r,s)\longmapsto(p+2d,r-14d,s+5d).
>
$$


> A shift confined to one ordinary ray, $r\mapsto r+6j$, returns to
> the fixed-$M$ lattice if and only if $7\mid j$.  Writing
> $j=7k$, the return is
> 

$$
> \boxed{(r,s,p)\longmapsto(r+42k,s-15k,p-6k).}
>
$$


> In particular, a step-$6$ operator window of order at most six
> contains no second fixed-$M$ row; the first possible return is the
> Item-322 displacement and changes the selected modulus by six.

> **PROVED — all fixed bounded-offset prime-pair mass is zero-rate.**
> Let $\mathcal H\subset\mathbb Z\setminus\{0\}$ be any fixed finite
> set.  The total logarithmic mass of fixed-$M$ candidate primes $p$
> for which $p+h$ is also prime for some $h\in\mathcal H$ is
> 

$$
> \boxed{O_{\mathcal H}(M/\log M)=o(M).}
>
$$


> Hence this holds for every fixed collection of same-ray offsets
> $h=6k$, for cross-ray offsets, and for any union of the two connection
> charts.

> **PROVED — isolated rows retain the full raw capacity.**  Removing all
> rows participating in the preceding bounded-offset pairs leaves
> logarithmic mass
> 

$$
> \boxed{\frac{2}{35}M+o(M).}
>
$$


> Thus a bounded-window gcd, resultant, or transfer whose use requires a
> second actual prime row cannot reduce the aggregate $1/105$ ceiling.

> **PROVED — sharp information-class countermodel.**  On the exact
> fixed-$M$ grid, the rank-two integral state
> 

$$
> V_M(r)=\binom{1}{6M-r}
>
$$


> has an invertible unipotent translation under every row shift.  At the
> selected row, $6M-r=7p$, so its safely fixed-factor-saturated carrier
> is exactly $p$.  It therefore has full selected mass despite an exact
> first-order translation module, pointwise height $O(\log M)$, and
> pairwise-coprime saturated row carriers.  Recurrence/translation
> metadata alone cannot supply the missing cross-modulus implication.

This is a global no-go for a whole mechanism, not a finite scan and not a
claim about the values of the actual carriers.  It extends Item 322's
single $p,p+6$ transfer obstruction to every fixed bounded window and
to the chart-aggregate ledger.  The strict effect is



$$
\boxed{\Delta r_1=0},\qquad
 \boxed{\Delta\text{capacity}=0},\qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling}=1/105}.
\tag{1.2}
$$



## 2. Exact row parametrization and chart aggregation

Solving (1.1) gives



$$
\boxed{r=6M-7p},
 \qquad
 \boxed{s=\frac{5p-4M-1}{2}}.
\tag{2.1}
$$



The positivity conditions are exactly



$$
\frac{4M+3}{5}\leq p\leq\frac{6M-1}{7}.
\tag{2.2}
$$



Apart from the irrelevant small characteristic, every prime in (2.2)
gives one actual row, and every actual row is obtained this way.  Therefore
the prime number theorem gives



$$
\sum_{p\text{ in }(2.2)}\log p
 =\left(\frac67-\frac45\right)M+o(M)
 =\frac{2}{35}M+o(M).
\tag{2.3}
$$



Let $\mathcal C_M^{\rm nd}$ and $\mathcal C_M^{\rm deg}$ denote the
actual collision-prime sets on the two safely saturated charts.  They are
disjoint subsets of the same interval, so



$$
W_{\rm nd}(M)+W_{\rm deg}(M)
 \leq\frac{2}{35}M+o(M),
\tag{2.4}
$$



not twice this quantity.  The argument below is deliberately independent
of the chart label: any event requiring two different actual prime rows is
contained in a prime-pair set before either carrier is evaluated.

## 3. The full alignment lattice

Fix $M$.  Replacing $p$ by $p+2d$ in (2.1) gives



$$
\boxed{
 p'=p+2d,\qquad r'=r-14d,\qquad s'=s+5d.}
\tag{3.1}
$$



This is the complete algebraic fixed-$M$ grid.  The two actual
$r\bmod6$ rays are interlaced in it.  A same-ray operator has shifts



$$
r'=r+6j.
\tag{3.2}
$$



Combining (3.1) and (3.2) gives



$$
6j=-14d,
 \qquad 3j=-7d.
\tag{3.3}
$$



Since $\gcd(3,7)=1$, (3.3) is integral exactly when



$$
\boxed{j=7k,\qquad d=-3k}
\tag{3.4}
$$



for an integer $k$.  Substitution yields



$$
\boxed{
 r'=r+42k,qquad s'=s-15k,qquad p'=p-6k.}
\tag{3.5}
$$



The returned row is actual precisely when its new $r,s$ remain in the
declared range.  For $k=1$, this requires $s\geq16$.  Reversing the
direction gives Item 322's exact transfer



$$
(r,s,p)\mapsto(r-42,s+15,p+6).
\tag{3.6}
$$



Equations (3.3)-(3.5) prove more than the order-three observation.  Every
fixed step-$6$ window with largest shift $j<7$ meets the fixed-$M$
lattice only at its source row.  A longer fixed window meets it at finitely
many offsets $p\mapsto p-6k$, all with different characteristics.

## 4. The bounded-window prime-pair theorem

For a fixed nonzero integer $h$, the classical Brun--Selberg
upper-bound sieve gives, uniformly in an interval of length $O(M)$,



$$
\#\{p\asymp M:p\text{ and }p+h\text{ are prime}\}
 =O_h\!\left(\frac{M}{(\log M)^2}\right).
\tag{4.1}
$$



For odd $h$, there are only the trivial possibilities involving the
prime $2$, so (4.1) is more than sufficient.  Since every candidate
prime in (2.2) is $O(M)$, partial summation or the elementary bound
$\log p=O(\log M)$ gives



$$
\sum_{\substack{p,\,p+h\text{ both in }(2.2)\\
                  p,\,p+h\text{ prime}}}\log p
 =O_h\!\left(\frac{M}{\log M}\right)=o(M).
\tag{4.2}
$$



For a fixed finite set $\mathcal H$, the union bound over (4.2) proves



$$
\boxed{
 W_{\rm pair}(M;\mathcal H)
 :=\sum_{\substack{p\text{ in }(2.2)\\
             \exists h\in\mathcal H:\ p+h\text{ lies in }(2.2)
             \text{ and is prime}}}\log p
 =o(M).}
\tag{4.3}
$$



Subtracting (4.3) from (2.3) gives



$$
\boxed{
 \sum_{\substack{p\text{ in }(2.2)\\
             p+h\text{ composite or out of range for every }h\in\mathcal H}}
 \log p
 =\frac{2}{35}M+o(M).}
\tag{4.4}
$$



Thus bounded-window isolated candidates retain the full raw mass.  This
conclusion is unconditional and does not assume anything about which of
those isolated rows collide.

For a fixed order-$J$ same-ray recurrence, take



$$
\mathcal H_J=\{6k:0<|7k|\leq J\}.
\tag{4.5}
$$



Every pair of distinct fixed-$M$ rows visible in that recurrence lies in
(4.3).  Allowing a fixed finite collection of recurrences, both residue
rays, or both connection charts merely replaces $\mathcal H_J$ by
another fixed finite set and leaves (4.3) unchanged.

## 5. Why an exact recurrence still lives in the wrong field

Suppose an exact rational recurrence or finite-dimensional translation
module is regular at a source row.  Reducing its identity modulo the
source prime $p$ relates all transported values inside $\mathbb F_p$.
At the returned row (3.5), the selected collision is instead tested in



$$
\mathbb F_{p-6k}.
\tag{5.1}
$$



There is no unital ring homomorphism
$\mathbb F_p\to\mathbb F_{p-6k}$ for $k\ne0$: a unital map preserves
characteristic.  Hence a same-modulus relation such as



$$
p\mid A(r)\quad\Longrightarrow\quad p\mid A(r+42k)
\tag{5.2}
$$



does not imply the selected statement



$$
p-6k\mid A(r+42k).
\tag{5.3}
$$



If a recurrence coefficient has a pole at $p$, it supplies no valid
mod-$p$ propagation there; if it is a unit, it remains confined to
$\mathbb F_p$.  Thus singularities do not evade the dichotomy.

This is the same moving-modulus obstruction seen in Item 322's exact
period transfer, now proved for the complete fixed-$M$ alignment lattice
and every fixed bounded window.  It applies equally to determinant gates,
actual-period residuals, safely saturated degenerate carriers, and any
finite vector containing them.  It does not say that a new reciprocity
law is impossible; such a law is precisely the missing extra input.

## 6. A sharp full-mass comparison module

The logical limitation is witnessed by an exact integral model on the
same grid.  Define



$$
V_M(r)=\binom{1}{A_M(r)},
 \qquad A_M(r)=6M-r.
\tag{6.1}
$$



For every integer shift $u$,



$$
\boxed{
 V_M(r+u)=
 \begin{pmatrix}1&0\\-u&1\end{pmatrix}V_M(r).}
\tag{6.2}
$$



The matrix is integral, unipotent, and invertible over every residue
field.  In particular, it gives exact fixed-grid and same-ray transfers



$$
A_M(r-14d)=A_M(r)+14d,
 \qquad
 A_M(r+42k)=A_M(r)-42k.
\tag{6.3}
$$



At the actual selector (2.1),



$$
\boxed{A_M(r)=7p.}
\tag{6.4}
$$



Removing the fixed factor $7$, which is a unit for every asymptotic
candidate prime, gives the primitive row carrier



$$
\widetilde{\mathfrak G}_{M,p}=p.
\tag{6.5}
$$



It is squarefree, distinct row carriers are pairwise coprime, its
logarithmic height is $O(\log M)$, and it belongs to the exact rank-two
translation module (6.2).  Nevertheless



$$
\sum_{p\mid\widetilde{\mathfrak G}_{M,p}}\log p
 =\frac{2}{35}M+o(M).
\tag{6.6}
$$



At the first same-ray return, (6.3) reads



$$
7p\longmapsto7(p-6),
\tag{6.7}
$$



so both selected divisibilities hold at their own moduli even though no
same-field implication connects them.  This comparison family is not the
actual carrier.  It proves the information-class theorem:



$$
\boxed{
 \begin{gathered}
 \text{exact finite-rank translation, integral regularity, primitive}\
 \text{rowwise gcd localization, small height, and pairwise coprimality}\
 \text{do not imply a saving on the matched-modulus diagonal.}
 \end{gathered}}
\tag{6.8}
$$



## 7. Exact consequence for proposed aggregate mechanisms

Let a proposed cross-row closer require an original collision at one row
and a second actual candidate-prime row at one of finitely many fixed
offsets.  This includes:

1. a bounded-window recurrence whose use requires two selected zeros;
2. a cross-row gcd or resultant evaluated only when both row moduli are
   prime;
3. a finite collection of same-ray period transfers;
4. a finite mixture of degenerate and nondegenerate chart transfers; and
5. a bounded chain of such steps.

Before imposing either collision condition, the support of the mechanism
is already contained in (4.3), hence has logarithmic mass $o(M)$.
It therefore controls no isolated candidate.  Equation (4.4) shows that
those isolated candidates retain the full raw ceiling.

There is one important conditional escape.  If a new theorem proved that
**every** original collision forces a second actual prime row in one of
the bounded offsets, then (4.3) would immediately give the desired
$o(M)$ collision mass.  No existing recurrence, transfer, determinant,
or primitive carrier proves that propagation.  Formula (6.8) shows that
the listed structural properties cannot prove it by themselves.

Thus the admissible next inputs are genuinely one-row or genuinely
cross-prime arithmetic:

- a matched-modulus average-gcd/factor-localization theorem for the actual
  aggregate carrier;
- a reciprocity law that changes characteristic and forces propagation;
- a target-retaining weighted theorem for the isolated rows; or
- an unbounded-window theorem accompanied by quantitative control strong
  enough to survive the growing set of offsets.

Merely certifying another fixed-order operator or iterating Item 322 a
fixed number of times is now closed as strategic progress.

## 8. Certificate and strict labels

The deterministic companion checker verifies:

- the exact parametrization and row-grid identities;
- the Diophantine alignment classification $3j=-7d$;
- all fixed windows $|j|\leq24$ in the declared replay;
- the rank-two comparison module and primitive carrier on declared
  fixed-$M$ slices;
- exact prime-pair and isolated-mass diagnostics for a declared finite
  offset set; and
- dependency hashes for the prior fixed-$j=2$ carrier, transfer,
  chart, and selector packages.

The bounded row counts and Chebyshev ratios in the JSON are **EXACT FINITE
ONLY / DIAGNOSTIC**.  The all-parameter alignment theorem, comparison
module, and bounded-offset mass theorem follow from Sections 3, 4, and 6,
not from those diagnostics.

### PROVED

- the complete fixed-$M$/same-ray alignment lattice;
- no step-$6$ window of order below seven contains a second fixed-$M$
  row;
- the all-fixed-finite-offset prime-pair bound (4.3);
- full raw mass of the corresponding isolated complement (4.4);
- the exact rank-two full-mass comparison module; and
- the aggregate bounded-window propagation no-go across both charts.

### EXACT FINITE ONLY / DIAGNOSTIC

- every declared replay row, prime-pair count, numerical ratio, and digest.

### OPEN / NOT CLAIMED

- $W_{\rm nd}(M)+W_{\rm deg}(M)=o(M)$, or any strict constant saving;
- a one-row average-gcd or radical-mass theorem for the actual carrier;
- a cross-characteristic reciprocity or forced-propagation theorem;
- any theorem for windows growing with $M$;
- any new booking or Route-1 completion; and
- any conclusion about $e+\pi$.
