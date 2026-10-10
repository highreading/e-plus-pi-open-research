> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 419 — the transverse double-Frobenius parity boundary and a sharper actual foreign-tail screen

Checked: 2026-09-01 (Beijing time)

Status: **CANONICAL, ROOT-AUDITED, ZERO BOOKING**

## 1. Capacity first and verdict

Retain one actual ordinary-$j=2$ fixed-$M$ ray



$$
p=2r+6s+3,\qquad
 r=6M-7p,\qquad
 s={5p-4M-1\over2},\qquad
 r\equiv e\pmod6,\quad e\in\{1,5\}.
\tag{1.1}
$$



Items 409, 413, and 416 give



$$
\mathcal J_{r,s}\mid\Pi_r,
 \qquad
 j^{\rm tie}_{r,s}=\gcd(p,\mathcal J_{r,s})\in\{1,p\},
\tag{1.2}
$$



and, after the selected-prime cutoff,



$$
F^{[p]}_{r,s}
 =\operatorname {rad}_{q>p,\ q\ne p}\mathcal J_{r,s}.
\tag{1.3}
$$



Item 416 split this forward foreign support into an aligned part and a
transverse part.  The aligned primes satisfy



$$
q\equiv2r+3\pmod6
\tag{1.4}
$$



and transport to a future same-$r$ degenerate **gate**, but not to a
future target or rejection.  This item settles the exact phase geometry
of the other residue class and sharpens the unconditional actual-family
height screen.

> **PROVED — transverse double-Frobenius lift.**  Let $q>p$ be a
> transverse prime, so
> $q\not\equiv2r+3\pmod6$.  Then
> 

$$
> \boxed{
> Q^\perp={2q-2r-3\over3}\in\mathbb Z,
> \qquad Q^\perp\text{ is odd},
> \qquad3Q^\perp+2r+3=2q.}
> \tag{1.5}
>
$$


> Thus the phase specialization $\bar Q=-(2r+3)/3$ reduces to an
> odd exponent on the **second** Frobenius sheet.  It is not an ordinary
> same-$r$ row, whose exponent is $Q=2s$.

> **PROVED — the partial $A$-tail terminal survives, but the full
> connection does not transport.**  At (1.5), the denominators in the
> terminal $J_{2r+5}$ string are all even and end at $2q$.  Hence
> their only $q$-multiple is the top denominator $2q$, whose
> binomial coefficient is one.  The normalized terminal is still
> 

$$
> J_{2r+3}={c-1\over Q^\perp+2r+3}\pmod q.
> \tag{1.6}
>
$$


> However Item 250's upper-$B$ common-period parameter becomes
> 

$$
> \boxed{D={r+Q^\perp+1\over2}\in\mathbb Z+\frac12.}
> \tag{1.7}
>
$$


> Therefore the ordinary common factorial period, its $f$-vector,
> and the Item-409 target residual are not reductions of an odd-$Q$
> row.  A transverse factor cannot be promoted to a same-$r$ actual
> gate, much less to a target rejection, without a new parity-flipped
> $B$-tail derivation and an independent target bridge.

> **PROVED — sharper actual weighted-tail screen.**  Item 314 proves
> the algebraic branch coefficient $\mathfrak a_r$ has logarithmic
> height $O(r)$.  Since
> 

$$
> F^{[p]}_{r,s}\mid\operatorname {rad}\mathcal J_{r,s},
> \qquad
> \mathcal J_{r,s}\mid\Pi_r,
> \qquad
> \Pi_r\mid|\operatorname {num}\mathfrak a_r|,
> \tag{1.8}
>
$$


> one has on one fixed ray
> 

$$
> \boxed{B^{[p]}_e(M)=O\!\left({M^2\over\log M}\right),}
> \qquad
> \boxed{B^\perp_e(M)=O\!\left({M^2\over\log M}\right).}
> \tag{1.9}
>
$$


> Also
> 

$$
> \boxed{
> \sum\omega(F^{[p]}_{r,s})
> =O\!\left({M^2\over(\log M)^2}\right).}
> \tag{1.10}
>
$$



This replaces Item 416's $O(M^2)$ weighted screen and
$O(M^2/\log M)$ support-count screen by one additional logarithm.
It is still superlinear and therefore supplies no finite linear capacity
coefficient.  No $o(M)$ theorem, tail lower bound, or matched margin is
proved.  Consequently



$$
\boxed{\Delta r_1=0},\qquad
 \boxed{\Delta\mathcal C=0},\qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling remains }1/105}.
\tag{1.11}
$$



There is no prime census and no finite extrapolation.

## 2. Exact two-sheet classification

Put



$$
k_*=2r+3.
\tag{2.1}
$$



Both $q$ and $k_*$ are primes-to-six residues.  On the aligned
class, $q-k_*\equiv0\pmod6$, and Item 416 uses



$$
Q^\parallel={q-k_*\over3}=2{q-k_*\over6}\in2\mathbb Z.
\tag{2.2}
$$



This is precisely the ordinary exponent $Q=2s$, and



$$
3Q^\parallel+k_*=q.
\tag{2.3}
$$



On the transverse class, $q-k_*$ is not divisible by three.  Since
the two nonzero residue classes modulo three are opposite, one has



$$
2q-k_*\equiv0\pmod3.
\tag{2.4}
$$



Define $Q^\perp$ by (1.5).  Its numerator is odd: $2q$ is even and
$k_*$ is odd.  Division by the odd integer three preserves parity,
so $Q^\perp$ is odd.  Since $q>p>k_*$,



$$
0<2q-k_*<3q,
\tag{2.5}
$$



which proves $0<Q^\perp<q$.  Equations (1.5) now follow exactly.

This is not merely a congruence-class restatement.  It identifies which
integer representative of



$$
Q\equiv-{2r+3\over3}\pmod q
\tag{2.6}
$$



is selected.  Aligned support lies on the first sheet and has even
$Q$; transverse support lies on the second sheet and has odd $Q$.

## 3. The unique $2q$ terminal and why it does not repair parity

For an integer $Q>0$, Item 250 starts with



$$
J_k=\sum_{t=0}^{Q-1}\binom{Q-1}{t}{1\over Q+k+2t}
\tag{3.1}
$$



and the exact recurrence



$$
(3Q+k)J_{k+2}=2^Q-(Q+k)J_k.
\tag{3.2}
$$



Take $Q=Q^\perp$, $k=k_*$.  The denominators in
$J_{k_*+2}$ are



$$
Q^\perp+k_*+2,
 Q^\perp+k_*+4,
 \ldots,
 3Q^\perp+k_*=2q.
\tag{3.3}
$$



Every number in (3.3) is even, because both $Q^\perp$ and $k_*$
are odd.  The only positive multiples of the odd prime $q$ not
exceeding $2q$ are $q$ and $2q$.  Parity excludes $q$, and
the last entry is $2q$.  Its coefficient is



$$
\binom{Q^\perp-1}{Q^\perp-1}=1.
\tag{3.4}
$$



Thus multiplication by $3Q^\perp+k_*=2q$, before reduction, retains
one terminal residue.  This proves (1.6), with exactly the same
inhomogeneous $-1$ as on the first sheet.  No naive division by the
zero pivot occurs.

The similarity stops here.  Item 250's upper $B$-tail reduction uses



$$
D={r+Q+1\over2},\qquad R=Q+D,
\tag{3.5}
$$



with integer factorials $Q!,(D-1)!,R!$.  On an ordinary row, $r$
is odd and $Q$ is even, so $D\in\mathbb Z$.  On the transverse
lift both $r$ and $Q^\perp$ are odd, making the numerator in
(3.5) odd.  Hence (1.7) is exact.

Consequently, the rational $f=(f_0,f_1)$ used in



$$
\Pi_r=\gcd(
 |\operatorname {num}\mathfrak a_r|,
 |\operatorname {num}\mathfrak b_r|,
 |\operatorname {num}K_r|)
\tag{3.6}
$$



cannot simply be declared the reduction of an odd-$Q$ finite
$B$-tail.  The parity choice in the terminating-binomial formula has
changed.  The source statement



$$
q\mid\mathcal J_{r,s}
 \quad\Longrightarrow\quad
 q\mid\Pi_r,\quad q\nmid\Gamma_{r,s}
\tag{3.7}
$$



therefore remains a source gate/target statement.  Equation (1.5) does
not turn it into a target or rejection statement at characteristic
$q$.

## 4. The sharper actual-family height theorem

The improvement in (1.9) uses more than Item 416's generic connection
height.  Item 314 proves, from the exact algebraic generating functions,



$$
h(\mathfrak a_r)=O(r),\qquad
 h(\mathfrak b_r)=O(r).
\tag{4.1}
$$



It also proves $\mathfrak a_r<0$ on both complete rays, so its
numerator is nonzero.  For a reduced rational number, (4.1) implies



$$
\log|\operatorname {num}\mathfrak a_r|=O(r).
\tag{4.2}
$$



From (1.8), row by row,



$$
\log F^{[p]}_{r,s}
 \leq\log|\operatorname {num}\mathfrak a_r|
 =O(r).
\tag{4.3}
$$



On one actual fixed-$M$ ray,



$$
{4M+3\over5}\le p\le{6M-1\over7},
 \qquad
 0<r=6M-7p\le{2M\over5}.
\tag{4.4}
$$



The number of prime rows in this fixed-proportion interval and fixed
residue class is $O(M/\log M)$, by the same Chebyshev/
Brun--Titchmarsh input already used in Item 416.  Summing (4.3) proves



$$
B^{[p]}_e(M)
 \leq
 \sum_{\text{actual prime rows}}O(r)
 =O\!\left({M^2\over\log M}\right).
\tag{4.5}
$$



The transverse tail is a subproduct, proving its bound in (1.9).
Finally, every factor counted after the selected-prime cutoff satisfies



$$
q>p\ge{4M+3\over5}.
\tag{4.6}
$$



Each distinct factor therefore contributes $\gg\log M$ to (4.5),
which gives (1.10).  Radical support is counted once per row; no
valuation depth is credited.

## 5. Exact capacity boundary

Item 413's exact factorization and Item 416's adaptive version remain



$$
A^{[Y]}_e(M)-B^{[Y]}_e(M)
 =J_e(M)=D_e(M)-G_e(M).
\tag{5.1}
$$



The bound (4.5) is an upper bound on $B$, not a lower bound on
$A-B$.  Moreover,



$$
{M^2/\log M\over M}={M\over\log M}\longrightarrow\infty.
\tag{5.2}
$$



Thus (4.5) is not a finite linear coefficient and cannot be inserted
into the capacity ledger.  It improves the correct unconditional screen,
but it does not approach the required Closer statement



$$
\boxed{B^\perp_e(M)=o(M).}
\tag{5.3}
$$



Nor does it prove the Builder pair



$$
A^{[p]}_e(M)\ge aM+o(M),\qquad
 B^{[p]}_e(M)=o(M),\qquad a>0.
\tag{5.4}
$$



The raw one-ray mass remains $M/35+o(M)$, and the chart coupling from
Items 409 and 413 remains unchanged.  In particular, a thinner
degenerate-rejection channel would not by itself thin the nondegenerate
chart.

## 6. Scoped no-go and the next admissible theorem

The present input class consists of:

1. the actual source carrier $\mathcal J_{r,s}\mid\Pi_r$;
2. selected-prime saturation and the aligned/transverse split;
3. exact specialization $Q\equiv-(2r+3)/3\pmod q$;
4. the finite-beta $A$-tail recurrence and its Cartier terminal;
5. Item 250's ordinary even-$Q$ $B$-tail formula; and
6. algebraic coefficient height $O(r)$.

Within these inputs, a transverse factor lands on the odd second sheet,
where the ordinary $B$-tail normalization is unavailable.  The only
unconditional aggregate bound is (4.5), which is superlinear.  Hence
this class supplies no $o(M)$ foreign-tail theorem and no positive
tail-minus-foreign margin.

This is a scoped obstruction, not a theorem that transverse support is
large.  A successful continuation may still derive a parity-flipped
$B$-tail, prove a cross-$r$ reciprocity law, or obtain a direct
formula-specific average-gcd theorem.  Any such object must also bridge
back to the source target $\Gamma_{r,s}$; a gate-only construction is
insufficient.

The smallest admissible Closer statement remains



$$
\boxed{
 \sum_{\text{actual fixed-}M\ e\text{-ray rows}}
 \log\operatorname {rad}_{\substack{q>p\\
 q\not\equiv2r+3\ (6)}}\mathcal J_{r,s}=o(M).}
\tag{6.1}
$$



## 7. Deterministic replay and strict labels

The certificate pins audited canonical Items 315, 409, 413, and 416.
It verifies the two-sheet congruence, positivity and parity of
$Q^\perp$, the unique top $2q$ terminal, the half-integral
upper-$B$ parameter, and the exact asymptotic implication chain.  Its
five declared parameter rows are labelled geometry replays only: no
declared $q$ is asserted to divide $\mathcal J$.

Replay from the archive root:

~~~powershell
python scripts/item419_j2_transverse_double_sheet_certificate.py --replay results/item419_j2_transverse_double_sheet_certificate.json --output results/item419_j2_transverse_double_sheet_certificate_replay.json
~~~

### Strict labels

- **PROVED:** the odd double-Frobenius lift (1.5), the unique top
  $2q$ terminal and (1.6), the ordinary $B$-tail parity boundary
  (1.7), the actual-family bounds (1.9)--(1.10), and zero booking.
- **EXACT GEOMETRY REPLAY ONLY / NOT CARRIER DIVISIBILITY:** the five
  declared source/foreign parameter quadruples.
- **PROVED, SCOPED NO-GO:** same-$r$ ordinary gate transport and
  Item-409 target transport cannot be obtained by substituting the odd
  lift into the existing even-$Q$ formulas; height alone remains
  superlinear.
- **OPEN:** (6.1), every positive adaptive tail-minus-foreign margin,
  every target/rejection transport theorem, Route 1, and every
  conclusion about $e+\pi$.

Accordingly Item 419 gives a genuine structural boundary and a strictly
better actual upper screen, but no linear-exponent gain.
