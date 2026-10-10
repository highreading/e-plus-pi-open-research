> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 349 - the degenerate triple-minor carrier after safe saturation

Checked: 2026-09-01 (Beijing time)

## 1. Scope, capacity, and verdict

Retain the actual ordinary-$j=2$ family



$$
p=2r+6s+3,
 \qquad r\geq1\text{ odd},
 \qquad 3\nmid r,
\tag{1.1}
$$



and Item 341's degenerate chart



$$
\ell_r=\mu_r=C_r=0\pmod p.
\tag{1.2}
$$



This chart is disjoint from the nondegenerate $\ell_r\ne0$ chart but
lies inside the same ordinary-$j=2$ raw prime interval.  Its capacity
must therefore not be added to the nondegenerate $1/105$ ceiling.

The all-row normalizations from Items 314 and 319 are



$$
\boxed{\ell_r=2\sigma_{e,n}\mathfrak a_r},
 \qquad
 \boxed{\mu_r=-\sigma_{e,n}\mathfrak b_r},
 \qquad
 \boxed{C_r=\beta_rK_r},
\tag{1.3}
$$



where $r=6n+e$, $e\in\{1,5\}$, and both
$\sigma_{e,n}$ and $\beta_r$ are $p$-units on every actual row.

For a reduced rational number $x$, write
$\operatorname {num}(x)$ and $\operatorname {den}(x)>0$.  Define
the normalized primitive triple carrier



$$
\boxed{
 \Pi_r=gcd\left(
 |\operatorname {num}\mathfrak a_r|,
 |\operatorname {num}\mathfrak b_r|,
 |\operatorname {num}K_r|
 \right).}
\tag{1.4}
$$



The main result is a sharp localization, but not a density theorem.

> **PROVED - exact r-only carrier theorem.**  On every actual row,
> 

$$
> \boxed{
> \ell_r=\mu_r=C_r=0\pmod p
> \quad\Longleftrightarrow\quad p\mid\Pi_r.}
>
$$


> Thus every degenerate original collision prime divides the explicit
> $r$-only integer $\Pi_r$.

> **PROVED - full Item-338-safe saturation.**  Let $S_{r,s}$ be
> Item 338's exact saturation product, including all ingredient
> denominators and $\binom{2m}{m}$, $m=s-1$.  Then
> 

$$
> \Pi^{\rm sat}_{r,s}=(\Pi_r)_{(S_{r,s})}
>
$$


> satisfies
> 

$$
> \boxed{p\mid\Pi_r\Longleftrightarrow
> p\mid\Pi^{\rm sat}_{r,s}.}
>
$$


> No denominator, central-binomial, or already removed foreign factor is
> reintroduced.

> **PROVED - exact internal chart split.**  If
> $f=(f_0,f_1)\ne0\pmod p$, triple-minor vanishing is equivalent to
> $\mathfrak a_r=\mathfrak b_r=0\pmod p$; the third minor is then
> automatic.  If $f=0\pmod p$, the first two minors are automatic and
> the remaining condition is $K_r=0\pmod p$.

> **PROVED - fixed-M carrier localization.**  With
> 

$$
> r=6M-7p,
> \qquad s=\frac{5p-4M-1}{2},
>
$$


> the entire degenerate gate is contained exactly in the moving-divisor
> set $p\mid\Pi^{\rm sat}_{6M-7p,s}$ inside the raw prime interval.

> **PROVED - scoped height/product obstruction.**  The defining
> recurrences give $\log^+\Pi_r=O(r\log r)$.  Multiplying the carriers
> over a fixed-$M$ slice therefore gives only
> $O(M^2\log M)$, which is weaker than the existing $O(M)$ raw
> Chebyshev ceiling.  Pointwise height, a raw product, or mere
> P-recursiveness cannot establish the required $o(M)$ mass theorem.

> **OPEN.**  No theorem currently proves
> 

$$
> \sum_{p\mid\Pi^{\rm sat}_{6M-7p,s}}\log p=o(M).
>
$$


> The first missing input is an average gcd/moving-divisor theorem for
> the three normalized connection sequences, or a good-reduction
> theorem proving that the saturated carrier is identically one.

Accordingly



$$
\boxed{\text{new booking}=0},\qquad
 \boxed{\text{new capacity reduction}=0},\qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling remains }1/105}.
\tag{1.5}
$$



No finite prime census is used or promoted.

## 2. Explicit construction of the third normalized minor

For completeness, this section writes $K_r$ without defining it by a
quotient.  Put



$$
\bar q=-\frac{2r+3}{3},
 \qquad
 P_0(z)=(1-z)^r(1+z),
 \qquad
 P_1(z)=(1-z)^r(1+z)^4,
\tag{2.1}
$$



and write $P_{\nu,j}=[z^j]P_\nu(z)$.  Define the homogeneous chain



$$
\eta_{2t}=0,
 \qquad \eta_1=1,
 \qquad
 \eta_{k+2}=-\frac{\bar q+k}{3\bar q+k}\eta_k
 \quad(k\text{ odd}),
\tag{2.2}
$$



and the canonical inhomogeneous chain



$$
(\bar q+k)y_k+(3\bar q+k)y_{k+2}=1,
 \qquad y_0=0,
 \qquad y_{2r+3}=0,
\tag{2.3}
$$



with the even chain propagated forward and the odd chain solved
backward.  Set



$$
\begin{aligned}
 S_0&=\sum_{j=0}^{r+1}P_{0,j}(y_{j+1}+y_{j+3}),&
 S_1&=\sum_{j=0}^{r+4}P_{1,j}y_j,\\
 \Delta_0&=\sum_{j=0}^{r+1}P_{0,j}(\eta_{j+1}+\eta_{j+3}),&
 \Delta_1&=\sum_{j=0}^{r+4}P_{1,j}\eta_j.
\end{aligned}
\tag{2.4}
$$



Then



$$
\boxed{K_r=S_0\Delta_1-S_1\Delta_0,}
\tag{2.5}
$$



and Item 319 proves



$$
\boxed{
 \beta_r=-\frac{3(r+1)!}
 {2(2r+3)(-r/3)_{r+1}},
 \qquad C_r=\beta_rK_r.}
\tag{2.6}
$$



Every factor in $\beta_r$ is a tied-$p$ unit: the rising factors
are $(3j-r)/3$, $0\leq j\leq r$, and



$$
0<|3j-r|\leq2r<p,
 \qquad r+1<2r+3<p.
\tag{2.7}
$$



Thus removing $\beta_r$ loses no actual support.  Likewise Item 314
proves that $\sigma_{e,n}$ in (1.3) is a tied-$p$ unit.  These are
the complete certified compulsory scalar removals used here.

## 3. Exact primitive carrier and denominator audit

Let Item 250's connection vectors be



$$
f=(f_0,f_1),
 \qquad b=(b_0,b_1),
 \qquad v=(v_0,v_1).
\tag{3.1}
$$



Their minors are



$$
\ell=\det(f,b),
 \qquad \mu=\det(f,v),
 \qquad C=\det(b,v).
\tag{3.2}
$$



All reduced denominators in (3.1), those of
$\mathfrak a_r,\mathfrak b_r,K_r$, and the scales in (1.3) are
$p$-units on an actual row.  Therefore (1.3) gives



$$
\ell=\mu=C=0\pmod p
 \quad\Longleftrightarrow\quad
 \mathfrak a_r=\mathfrak b_r=K_r=0\pmod p.
\tag{3.3}
$$



Reduction of a rational with unit denominator vanishes exactly when its
reduced numerator vanishes.  Taking the gcd of the three numerators
proves (1.4) and the exact carrier theorem.

There is no hidden exact-zero carrier stratum.  On the two actual rays
$r=6n+e$, $e\in\{1,5\}$, Item 315's all-ray sign theorem gives



$$
\boxed{\mathfrak a_{6n+e}<0\qquad(n\geq0).}
\tag{3.4}
$$



For clarity, this is an exact induction rather than a finite sign
table.  The common four-term ray recurrence has coefficients
$p_0(h),p_1(h),p_2(h)<0<p_3(h)$ for every $h>0$; after the positive
rescaling $16^{-j}$, three consecutive negative values force the
fourth to be negative.  The three exact negative initial values on each
ray start the induction.  Hence
$\operatorname{num}\mathfrak a_r\ne0$ for every admissible $r$, and



$$
\boxed{\Pi_r\geq1\text{ for every admissible }r.}
\tag{3.5}
$$



Thus ordinary integer divisibility and the logarithms used below are
defined on every row; no convention such as ``every prime divides
zero'' enters the carrier theorem or the product bound.

It is essential **not** to divide $\Pi_r$ out of another gate.  The
same-index gcd is the degenerate condition itself.  Item 315's warning
against unproved primitive division applies with full force here.

## 4. Safe removal of foreign support

Define the r-only connection denominator product



$$
S_r^{\rm conn}
 =6\prod_{x\in\{f_0,f_1,b_0,b_1,v_0,v_1\}}
 \operatorname {den}(x),
\tag{4.1}
$$



and



$$
\Pi_r^{\rm conn}=(\Pi_r)_{(S_r^{\rm conn})}.
\tag{4.2}
$$



The integer $S_r^{\rm conn}$ divides the support of Item 338's larger
row product $S_{r,s}$.  The latter also contains the remaining period
and target denominators and the central-binomial factor.  Hence



$$
\Pi^{\rm sat}_{r,s}=(\Pi_r)_{(S_{r,s})}
 \quad\text{divides}\quad \Pi_r^{\rm conn}.
\tag{4.3}
$$



Item 338 proves



$$
p\nmid S_{r,s},
\tag{4.4}
$$



using all denominator audits and $p>2m$.  Consequently



$$
\boxed{
 p\mid\Pi_r
 \Longleftrightarrow p\mid\Pi_r^{\rm conn}
 \Longleftrightarrow p\mid\Pi^{\rm sat}_{r,s}.}
\tag{4.5}
$$



Thus (4.3) removes only foreign support.  In particular, a factor of a
normalized numerator that is already present in an ingredient
denominator or in $\binom{2m}{m}$ is not allowed back into the
degenerate carrier.

There is a useful exact declared example.  At



$$
(p,r,s)=(251,121,1),
\tag{4.6}
$$



the normalized raw carrier is



$$
\Pi_{121}=7,
\tag{4.7}
$$



but $7\mid S_{121}^{\rm conn}$, so



$$
\Pi_{121}^{\rm conn}
 =\Pi_{121,1}^{\rm sat}=1.
\tag{4.8}
$$



This is **EXACT FINITE ONLY**.  It demonstrates required saturation; it
is not evidence for an all-row identity or a density statement.

## 5. The exact internal chart split

The third normalized chain also gives



$$
b+v=(S_0,S_1),
 \qquad v=\beta_r(\Delta_0,\Delta_1).
\tag{5.1}
$$



The chart split itself needs only two-dimensional linear algebra.

If $f\ne0\pmod p$, then
$\ell=\mu=0$ forces both $b$ and $v$ to lie in the line spanned
by $f$.  Hence $C=0$ automatically.  Using the unit scales,



$$
f\ne0:\qquad
 \ell=\mu=C=0
 \Longleftrightarrow
 \mathfrak a_r=\mathfrak b_r=0\pmod p.
\tag{5.2}
$$



If $f=0\pmod p$, the first two minors vanish automatically and



$$
f=0:\qquad
 \ell=\mu=C=0
 \Longleftrightarrow K_r=0\pmod p.
\tag{5.3}
$$



For integer bookkeeping define



$$
\mathcal A_r=gcd(|\operatorname {num}\mathfrak a_r|,
                    |\operatorname {num}\mathfrak b_r|),
\tag{5.4}
$$





$$
\mathcal F_r=gcd(|\operatorname {num}f_0|,
                    |\operatorname {num}f_1|),
 \qquad
 \mathcal{FK}_r=gcd(\mathcal F_r,
                    |\operatorname {num}K_r|).
\tag{5.5}
$$



Then the exact good-reduction support is the disjoint logical union



$$
\boxed{
 \bigl(p\nmid\mathcal F_r\ \text{ and }\ p\mid\mathcal A_r\bigr)
 \quad\text{or}\quad
 p\mid\mathcal{FK}_r.}
\tag{5.6}
$$



This stratification may be useful for a future average-gcd theorem.  It
does not split the capacity additively: the two alternatives occupy the
same fixed-$M$ raw interval.

## 6. Exact fixed-M moving-divisor formulation

On a fixed target slice,



$$
2M=5r+14s+7.
\tag{6.1}
$$



Solving together with (1.1) gives



$$
\boxed{
 r=6M-7p,
 \qquad
 s=\frac{5p-4M-1}{2}.}
\tag{6.2}
$$



The positivity conditions give the familiar interval



$$
\frac{4M+3}{5}\leq p\leq\frac{6M-1}{7}.
\tag{6.3}
$$



Let $\mathcal R_M$ retain the ordinary congruence restrictions and
integrality of (6.2).  The exact saturated triple-minor gate mass is



$$
\boxed{
 W_{\rm deg}^{\rm gate}(M)
 =\sum_{\substack{p\in\mathcal R_M\\
 p\mid\Pi^{\rm sat}_{6M-7p,(5p-4M-1)/2}}}\log p.}
\tag{6.4}
$$



Every original degenerate collision is counted in (6.4).  The converse
need not hold, because on a rank-at-most-one connection line an
individual original coordinate must still vanish.  Thus (6.4) is the
correct Closer upper target, not a new Builder contribution.

The raw interval mass is



$$
\vartheta\left(\frac{6M-1}{7}\right)
 -\vartheta\left(\frac{4M+3}{5}\right)
 =\frac{2}{35}M+o(M).
\tag{6.5}
$$



The nondegenerate and degenerate events are disjoint at each tied prime,
but both range over (6.3).  Therefore



$$
W_{\rm nd}(M)+W_{\rm deg}(M)
 \leq\frac{2}{35}M+o(M),
\tag{6.6}
$$



not twice that quantity.  Conversely, proving only
$W_{\rm deg}=o(M)$ would close this chart but would not numerically
lower the worst-case $1/105$ ceiling while the nondegenerate chart can
still occupy the full interval.

## 7. Why pointwise height does not solve (6.4)

All chains in Section 2 have $O(r)$ steps.  Their linear factors have
height $O(\log r)$, and the binomial kernels in (2.1) have logarithmic
height $O(r)$.  A common master product of the forward and backward
pivots clears every state used in (2.4); its logarithm is
$O(r\log r)$.  Addition of $O(r)$ kernel terms does not change this
order.  The same Lagrange/recurrence clearing used for
$\mathfrak a_r,\mathfrak b_r$ gives



$$
\log^+|\operatorname {num}\mathfrak a_r|
 +\log^+|\operatorname {num}\mathfrak b_r|
 +\log^+|\operatorname {num}K_r|
 =O(r\log r).
\tag{7.1}
$$



In particular,



$$
\log^+\Pi_r=O(r\log r).
\tag{7.2}
$$



Here $\Pi_r\geq1$ by (3.5), so (7.2) is an ordinary finite integer
height bound on every row, including before safe saturation.

There are $O(M)$ possible $r$-values on a fixed-$M$ slice and
$0<r=O(M)$.  Consequently the direct carrier product gives only



$$
\sum_r\log^+\Pi_r=O(M^2\log M).
\tag{7.3}
$$



Even replacing each integer by its radical cannot improve (7.3)
without an arithmetic theorem about repeated or moving prime factors.
The existing raw Chebyshev bound (6.5) is already $O(M)$, so the
height/product estimate is strategically inert.

Likewise, a fixed-order recurrence or D-finiteness statement for any of
the three sequences would control evaluation, not zeros modulo the
moving prime $p=(6M-r)/7$.  Without a zero-density, average-gcd, or
good-reduction theorem, it cannot imply (6.4) is $o(M)$.

> **PROVED - scoped no-go.**  Individual-height bounds, the raw product
> of the r-only carriers, and recurrence existence without modular
> zero-density are insufficient to improve the ordinary-$j=2$ ledger.

## 8. Remaining arithmetic input and strict labels

One of the following would close the degenerate chart:

1. $W_{\rm deg}^{\rm gate}(M)=o(M)$ directly;
2. an average-gcd theorem for
   $(\mathfrak a_r,\mathfrak b_r,K_r)$ along (6.2);
3. a good-reduction theorem proving
   $\Pi_r^{\rm conn}=1$, or at least that every prime factor of it is
   too small to equal the tied prime; or
4. separate weighted theorems for the two exact branches in (5.6).

**PROVED:** the explicit normalized carrier, safe saturation, exact
internal chart split, moving-divisor formulation, and height/product
obstruction.

**EXACT FINITE ONLY:** the declared row (4.6)-(4.8) and deterministic
formula replays.  No scan or zero count is used.

**OPEN:** every weighted theorem listed above.  No prime mass is booked
and no capacity is removed.
