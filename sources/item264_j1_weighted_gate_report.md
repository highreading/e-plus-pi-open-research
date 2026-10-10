> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 264 — global weighted support and the full $j=1$ gate barrier

Checked: 2026-08-31 (Beijing time)

## 1. Scope, admission test, and verdict

Work only on the actual fixed common-log cell $j=1$.  Its rows are



$$
p=4h+6s+3,\qquad h,s\ge1,                                    \tag{1.1}
$$



and the global coefficient index is



$$
M=3h+4s+2,\qquad 4M+1=3p-2s.                                \tag{1.2}
$$



The actual collision is the simultaneous pair



$$
Q_0(p,h,s)=Q_1(p,h,s)=0\pmod p,                              \tag{1.3}
$$



equivalently Item 218's two divided common-log coordinates, or



$$
p^2\mid C_0(M),\qquad p^2\mid C_1(M)                        \tag{1.4}
$$



for Item 197's fixed integers.  An individual observation seed, norm,
Wronskian, or recurrence coefficient is not substituted for (1.3).

> **PROVED — exact global support.**  Put
> 

$$
> \mathcal S_M={s\ge1:4s\le M-5,\ s\equiv M+1\pmod3\}.       \tag{1.5}
>
$$


> Then
> 

$$
> p_s={4M+2s+1\over3},\qquad
> h_s={M-4s-2\over3}=3M-2p_s.                                \tag{1.6}
>
$$


> The actual prime rows at fixed $M$ are in bijection with all primes
> in the interval
> 

$$
> \boxed{{4M+3\over3}\le p\le{3M-1\over2}.}                  \tag{1.7}
>
$$


> Consequently their raw logarithmic support is
> 

$$
> \boxed{
> \sum_{p\ \mathrm{in}\ (1.7)}\log p={M\over6}+o(M),}
> \qquad
> \boxed{\text{raw support per }6M={1\over36}.}               \tag{1.8}
>
$$



Before developing any proposed invariant, this item applies the following
master admission test:

1. it must be forced by the actual simultaneous gate (1.3), not by an
   individual seed;
2. it must survive the exact overlap with the already booked Cartier and
   post-Cartier layers;
3. it must leave an exceptional logarithmic ceiling strictly below
   $1/36$ per $6M$.

> **PROVED — the existing height method fails the admission threshold.**
> If $R_M^{(1)}$ is the product of the distinct actual $j=1$ collision
> primes, then
> 

$$
> (R_M^{(1)})^2\mid\gcd(C_0(M),C_1(M)).                        \tag{1.9}
>
$$


> Item 197's sharp available Cauchy constant is
> 

$$
> H=6.327627545440858\ldots.                                  \tag{1.10}
>
$$


> Thus the nondegenerate height argument gives only
> 

$$
> {\log R_M^{(1)}\over M}\le {H\over2}+o(1)
> =3.163813772720429\ldots+o(1),                              \tag{1.11}
>
$$


> or $H/12=0.5273022954\ldots$ per $6M$.  Both are much
> larger than the raw bounds $1/6$ and $1/36$.  Degenerate integer
> coefficients retain the raw bound, so no nonvanishing assumption is
> hidden.

> **PROVED, SHARPLY SCOPED INHERITED-ESTIMATE CEILING.**  If a bounded-degree
> integer recombination of $(C_0,C_1)$, with coefficient height
> $\exp(o(M))$, is bounded only by mechanically inheriting the two
> componentwise Cauchy estimates, then its certified height-to-valuation
> ratio is no better than $H/2$.  A homogeneous degree-$d$ expression
> gains the divisor $(R_M^{(1)})^{2d}$, while that inherited estimate is
> $dHM+o(M)$; a nonhomogeneous expression is weaker under the same
> estimate.  Thus linear recurrence changes of basis, determinants, and
> bounded-degree algebraic combinations do not improve (1.11) *from the
> componentwise estimate alone*.  A separately proved exponential
> cancellation, giving a genuinely smaller height for a particular
> combination, remains open.  At the existing componentwise height, a
> divisibility multiplicity
> 

$$
> t>6H=37.9657652726\ldots,
> \quad\text{hence }t\ge38,                                   \tag{1.12}
>
$$


> would be needed merely to improve the raw $j=1$ support.

This ceiling is scoped to the available fixed-$M$ integers and the
inherited componentwise estimate.  It is not a lower bound for the actual
height of every recombination, and it is not a theorem that every future
arithmetic representation must have the same height.

> **PROVED — Items 245/248 do not currently pass the admission test.**
> Their fourth-order Pearson recurrence has only $p$-unit pivots and
> computes forward without an exceptional pivot, but supplies no zero
> count.  Their Wronskian is necessary for a common
> *leading observation root*, not an established replacement for the full
> gate (1.3), and its universal-unit strategy has exact counterexamples.
> Exact actual rows with an individual seed loss or a Wronskian root loss
> still have $(Q_0,Q_1)\ne(0,0)$; see Section 5.

> **BOOKING DECISION.**  No weighted full-gate zero-density theorem and no
> admitted ceiling below $1/36$ is proved.  Therefore
> 

$$
> \boxed{\text{new unconditional Route-1 rate}=0,
> \qquad\text{new \(j=1\) capacity reduction}=0.}              \tag{1.13}
>
$$



No new large collision scan is used.  Every bounded replay is labelled
**EXACT FINITE ONLY**.

## 2. Exact global reindexing

Solving (1.2) for $p$ gives



$$
3p=4M+2s+1.                                                  \tag{2.1}
$$



Integrality is equivalent to



$$
2s\equiv-4M-1\pmod3
 \iff s\equiv M+1\pmod3.                                     \tag{2.2}
$$



Using (1.1) in (1.2) gives



$$
M=3h+4s+2,
 \qquad h={M-4s-2\over3}.                                    \tag{2.3}
$$



Thus $h\ge1$ is exactly $4s\le M-5$, proving (1.5)–(1.6).
Conversely, every odd prime in (1.7) gives



$$
s={3p-4M-1\over2}\ge1,
 \qquad h=3M-2p\ge1,                                         \tag{2.4}
$$



and recovers (1.1)–(1.2).  Since every actual $M\ge9$, the primes in
(1.7) exceed three.  The condition $3\nmid h$ is automatic:
$h\equiv p\pmod3$, so $3\mid h$ would force $p=3$.

The prime number theorem applied to (1.7) gives



$$
\vartheta((3M-1)/2)-\vartheta((4M+3)/3)
 =\left({3\over2}-{4\over3}\right)M+o(M)
 ={M\over6}+o(M),                                             \tag{2.5}
$$



which proves (1.8).

The congruence (2.2), the parity relation
$p\equiv1\pmod4\iff s$ is odd, and the inert/split distinction of
Item 248 are coordinate consequences of the same prime interval.  They
are not additional independent density sieves.

## 3. De-overlap and the retained-ceiling criterion

For the general common-log phase $j$, the PNT-scale interval is



$$
{4\over2j+1}M<p<{6\over3j+1}M.                              \tag{3.1}
$$



Adjacent intervals are disjoint because



$$
{6\over3j+4}<{4\over2j+1}
 \iff6(2j+1)<4(3j+4).                                        \tag{3.2}
$$



Hence the raw $j=1$ interval does not overlap the $j=0$, $j=2$,
or later fixed cells at the same $M$.

There is, however, exact valuation overlap.  Item 200 proved that every
PNT-side row already lies in the forced Cartier product and in Item 149's
post-Cartier set.  Therefore another statement that merely rediscovers a
first or second divisor at the same prime is not a new reservoir.  Two
types of theorem remain admissible:

* an actual-family exclusion or weighted upper bound for the collision
  set itself; or
* a genuinely new valuation theorem beyond the copies already booked.

If $\mathcal E_M^{(1)}$ denotes the full-gate collision primes, a theorem



$$
\sum_{p\in\mathcal E_M^{(1)}}\log p\le cM+o(M),
 \qquad c<{1\over6},                                          \tag{3.3}
$$



would retain at most $c/6<1/36$ per $6M$ and would book the saving



$$
{1\over36}-{c\over6}.                                       \tag{3.4}
$$



No current theorem supplies (3.3).  This is the exact quantitative
admission target, not a heuristic probability statement.

## 4. Full-gate inherited-estimate ceiling

The fixed integers are



$$
C_\nu(M)=[z^{4M+\nu}]
 { (1-z)^{6M}(1+z)^{1+3\nu}
  \over(1+z^2)^{4M+1+\nu}},\qquad\nu=0,1.                    \tag{4.1}
$$



On every actual row, $p\mid C_0,C_1$, and the simultaneous divided
gate is exactly (1.4).  Multiplication over the distinct collision primes
proves (1.9).

For $0<\rho<1$, Cauchy's estimate gives



$$
|C_\nu(M)|\le
 \rho^{-4M-\nu}(1+\rho)^{6M+1+3\nu}
 (1-\rho^2)^{-4M-1-\nu}.                                    \tag{4.2}
$$



The coefficient of $M$ is minimized at



$$
\rho={\sqrt{33}-3\over6},                                   \tag{4.3}
$$



and equals



$$
H=2\log(1+\rho)-4\log(1-\rho)-4\log\rho.                   \tag{4.4}
$$



Equations (1.9) and (4.2) prove (1.11).

The bounded-degree method ceiling can be stated exactly.  Let
$P(X,Y)\in\mathbb Z[X,Y]$ have coefficient height $\exp(o(M))$,
total degree $d$, no constant term, and smallest occurring total degree
$e$.  On a collision prime,



$$
p^{2e}\mid P(C_0(M),C_1(M)),                                 \tag{4.5}
$$



whereas the mechanically inherited componentwise Cauchy estimate is



$$
\log|P(C_0,C_1)|\le dHM+o(M).                               \tag{4.6}
$$



If the value is nonzero and no sharper height theorem is supplied, (4.5)
and (4.6) yield only



$$
{\log R_M^{(1)}\over M}\le{dH\over2e}+o(1)
 \ge{H\over2}+o(1).                                          \tag{4.7}
$$



If it is zero, it yields no bound.  For a homogeneous expression the
*inherited bound* reduces to the same $H/2$ ratio; for a nonhomogeneous
expression it is worse.  Therefore taking products, minors, resultants, or
Wronskians of bounded-degree transforms, while estimating them solely by
(4.6), cannot certify a better height ratio.

Equation (4.6) is only an upper bound obtained term by term.  It is not a
matching lower bound, and it does not rule out exponential cancellation in
a specially chosen $P$.  A separate theorem of the form
$\log|P(C_0,C_1)|\le H_P M+o(M)$ with $H_P/(2e)<1/6$, or a theorem
about the arithmetic factor distribution of the existing gcd, would be
real new information and could pass the admission test.

## 5. What the Items 245/248 data do and do not imply

Items 245/248 attach to each row the two leading observation pairs
$(\alpha_\nu,\beta_\nu)$ of a generalized $(1+Z^2)^4$-primary
kernel.  They prove exact observability and root-order formulas.  These
pairs describe the observation map for the later Witt kernel; they are not
the original values $(Q_0,Q_1)$.

The local coefficients are generated by a fourth-order Pearson recurrence
whose pivots are



$$
4n,\qquad1\le n<p.                                           \tag{5.1}
$$



Every pivot is a unit.  Hence the recurrence computes forward on every
actual row without a singular-pivot exclusion.  It compresses the
calculation, but the pivot theorem by itself supplies no zero count.

If the two leading observation factors vanish at a common root, Item 248
proves the division-free necessary Wronskian identity



$$
G_1'G_0-G_1G_0'=0.                                          \tag{5.2}
$$



Two exact split-root rows show that (5.2) is not universally a unit:



$$
\begin{array}{c|c|c|c|c}
(p,h,s,M)&W=(a,b)&I&a+bI&(Q_0,Q_1)\\ \hline
(109,4,15,74)&(88,70)&33&0&(71,106)\\
(149,26,7,108)&(42,60)&44&0&(42,106).
\end{array}                                                   \tag{5.3}
$$



All entries are reduced in their displayed prime field, and $I^2=-1$.
Thus a Wronskian root loss can occur while the actual two-coordinate gate
is not a collision.

There is also an exact inert individual-seed loss:



$$
(p,h,s,M)=(59,2,8,40),\qquad
 (\alpha_1,\beta_1)=(0,0),\qquad
 (Q_0,Q_1)=(39,11).                                           \tag{5.4}
$$



This disproves every strategy that replaces the simultaneous gate by
individual nonvanishing.  Conversely, Items 245/248 do not prove that an
actual full-gate collision must create a common leading root.  The valid
future target is therefore the intersection of the actual gate with the
later Witt compatibility equations—not the Wronskian-zero locus alone.

The existing finite census of leading roots is useful for debugging but
has no admission value as a density theorem.  This item performs no new
large collision scan.

## 6. The only current all-prime edge theorem has zero mass

Item 218 excludes the simultaneous gate on every fixed line
$0\le h\le8$.  At fixed $M$, each value of $h$ determines at most
one candidate prime



$$
p={3M-h\over2}.                                               \tag{6.1}
$$



Consequently the total logarithmic weight of all eight actual positive
lines is at most



$$
8\log(3M/2)=O(\log M)=o(M).                                  \tag{6.2}
$$



This is an all-prime exclusion, but it removes zero linear mass.  The
retained ceiling after de-overlap is still $M/6+o(M)$, or $1/36$ per
$6M$.

Similarly, any edge with $s\le S(M)=o(M/\log M)$ or bounded distance
from the upper phase endpoint has only $o(M)$ raw logarithmic support.
Such edge analyses can be structurally useful but cannot satisfy (3.3).

## 7. Explicit asymptotic target, strictly OPEN

The clean conjectural target is



$$
\boxed{
 \sum_{p\in\mathcal E_M^{(1)}}\log p=o(M).}                    \tag{7.1}
$$



If proved, (7.1) would retain zero $j=1$ mass and book the full
$1/36$ saving per $6M$.  The weaker estimate (3.3) with any
$c<1/6$ would already book a partial saving.

Equation (7.1) is **OPEN**.  No bounded computation in Items 218, 245,
248, or this item is promoted as evidence sufficient for it.  A proof
would require at least one of:

* a global arithmetic theorem for the simultaneous square divisors of
  $(C_0(M),C_1(M))$;
* an actual-family bridge from the full gate to a new low-height invariant,
  followed by a weighted zero theorem; or
* a genuinely independent later-Witt condition with a de-overlapped
  valuation or zero-density theorem.

## 8. Unit, boundary, and replay audit

Every actual $M\ge9$ has $p\ge13$, so the divisions by two and three
in (1.6), (2.4), and the gate formulas are units.  In Item 218's rational
tails, all factorial indices and recurrence denominators lie strictly
between zero and $p$.  In Items 245/248, every Pearson pivot (5.1) is a
$p$-unit.  The split-root witnesses explicitly satisfy $I^2=-1$.

The portable checker verifies:

* the exact bijection (1.5)–(1.7) for $9\le M\le600$;
* the general adjacent-interval inequality (3.2) on a bounded symbolic
  replay;
* the three declared rows (5.3)–(5.4), independently recomputing their
  full gate coordinates from Item 218's finite rational sums;
* the exact height constants and the integer threshold $t\ge38$.

It performs **no collision scan**.  The bounded arithmetic replay is
**EXACT FINITE ONLY** and supports no asymptotic inference.

### PROVED

* The exact global reindexing, prime interval, and raw $1/36$ support.
* The de-overlap and retained-ceiling admission criterion.
* The full-gate square-divisor height comparison.
* The bounded-degree inherited-estimate method ceiling; separately proved
  low-height cancellation remains open.
* The recurrence/Wronskian admission failures and exact counterexamples.
* The zero-linear-mass fixed-edge exclusion.
* Zero new booking.

### EXACT FINITE ONLY

* The declared bounded bijection replay and three exact witness
  recomputations.

### OPEN

* Any estimate (3.3) with $c<1/6$, including (7.1).
* Any all-row exclusion of the full $j=1$ collision.
* An actual-family bridge from the full gate to a later-Witt common root.
* Any new Route-1 rate or conclusion about $e+\pi$.
