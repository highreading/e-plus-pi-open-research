> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 359 - fixed-$M$ cross-prime coefficient bridge and selector barrier

Checked: 2026-09-01 (Beijing time)

## 1. Scope, capacity, and verdict

Retain the actual ordinary-$j=2$ fixed-family equations



$$
p=2r+6s+3,
 \qquad
 2M=5r+14s+7,
\tag{1.1}
$$



and, on the nondegenerate chart, the complete collision gate



$$
\boxed{4^s=c_r^*,\qquad H_{s-1}=\Theta_{r,s}\pmod p}.
\tag{1.2}
$$



Item 355 proved that a within-prime magnitude-square moment cannot
control the fixed-$M$ selector.  This item therefore keeps $M$
fixed and couples the different primes before taking any moment.

The exact selector is



$$
\boxed{
 r=6M-7p,
 \qquad
 s=\frac{5p-4M-1}{2},
 \qquad
 k=r-1=6M-7p-1.}
\tag{1.3}
$$



The candidate primes fill



$$
\frac{4M+3}{5}\le p\le\frac{6M-1}{7},
\tag{1.4}
$$



so their raw logarithmic mass and normalized capacity are



$$
\boxed{\frac{2}{35}M+o(M)},
 \qquad
 \boxed{\mathcal C_{j=2}=\frac1{105}\text{ per }6M}.
\tag{1.5}
$$



The main result is a genuine cross-prime realization, followed by a
sharp limitation of what that realization gives for free.

> **PROVED - one fixed-$M$ coefficient kernel contains every old
> determinant gate.**  There is an explicit rational function
> $\mathcal K_M(X)\in\mathbb Q(X)$, independent of the selected
> prime, such that every actual row satisfies
> 

$$
> 16^{M-1}rG_{r,s}
> \equiv-12[X^{6M-7p-1}]\mathcal K_M(X)\pmod p,
>
$$


> where $G_{r,s}=18\,4^sa_r+11b_r$ is Item 314's exact old
> determinant gate.  All coefficient denominators are $p$-units.
> Thus different primes really do sample different coefficients of one
> common fixed-$M$ object; this is not another within-prime moment.

> **PROVED - one fixed bivariate rational function contains all
> $M$.**  The series $\sum_{M\ge1}\mathcal K_M(X)Y^M$ is a fixed
> rational function in $X,Y$.  Hence the selected gate is an affine
> coefficient diagonal of a single rational kernel.

> **PROVED - linear pole and recurrence obstruction.**  The reduced
> denominator of $\mathcal K_M$ has an exact pole of order $6M$
> at each of $X=1$ and $X=-1$.  Therefore every eventual scalar
> constant-coefficient recurrence for its full coefficient sequence has
> order at least $12M$.  The entire selected window has
> $0\le k\le(2M-26)/5$.  The natural common-denominator recurrence is
> inhomogeneous throughout this window and supplies no cross-prime
> propagation there.

> **PROVED - rational-kernel and height metadata alone are
> insufficient.**  A second explicit fixed bivariate rational function
> has coefficient exactly $p$ at every tied selector
> $(M,k=6M-7p-1)$ on the two prime residue rays.  It has only
> $O(\log M)$ pointwise height, yet every selected prime divides its
> selected coefficient.  Thus fixed rationality, holonomicity, small
> pointwise height, and coefficientwise Parseval cannot by themselves
> imply a saving on the selector diagonal.  This comparison kernel is
> a method-class obstruction, not the actual gate.

> **OPEN.**  The actual coefficient diagonal may still have strong
> arithmetic nonconcentration.  What is missing is a theorem about
> divisibility by the *matched modulus*
> $p=(6M-k-1)/7$, or a joint theorem also using
> $H_{s-1}-\Theta_{r,s}$.  Neither follows from rationality,
> recurrence, height, or the exact character identities already known.

Consequently



$$
\boxed{\text{new booking}=0},
 \qquad
 \boxed{\text{new capacity reduction}=0},
 \qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling remains }1/105}.
\tag{1.6}
$$



No prime scan or collision census is used.

Item 359 treats the nondegenerate chart inherited from Item 355.  The
degenerate Item 349 chart is disjoint row by row but belongs to the same
interval (1.4).  Its capacity is therefore not added to (1.5); the two
charts partition one ordinary-$j=2$ ceiling.

## 2. Exact selector and the Fermat collapse

Solving (1.1) gives (1.3), as well as



$$
m=s-1=\frac{5p-4M-3}{2},
 \qquad
 d=r+4=6M-7p+4,
 \qquad
 q=2(M-p)+1.
\tag{2.1}
$$



The lower and upper endpoints in (1.4) are precisely $m\ge0$ and
$d\ge5$.  For primes larger than $3$, the parity and
$3\nmid r$ conditions are automatic on this grid, so (1.4) is the
actual raw prime interval.

The first important fixed-$M$ identity is



$$
s-2(1-M)=\frac{5(p-1)}2.
\tag{2.2}
$$



Euler-Fermat applied to the square base $4$ gives



$$
\boxed{4^s\equiv16^{1-M}\pmod p}.
\tag{2.3}
$$



This removes the selected prime from the exponential endpoint.  Item
314's exact unit-cleared determinant gate is



$$
G_{r,s}=18\,4^sa_r+11b_r,
 \qquad
 D_{r,s}\equiv0\pmod p
 \Longleftrightarrow G_{r,s}\equiv0\pmod p.
\tag{2.4}
$$



Multiplying by the $p$-unit $16^{M-1}$, (2.3) gives



$$
16^{M-1}G_{r,s}
 \equiv18a_r+11\,16^{M-1}b_r\pmod p.
\tag{2.5}
$$



The branch index $r=6M-7p$ still moves.  The next two sections put
all those moving branch coefficients into one common kernel.

## 3. A truncated exponent lemma

The needed Frobenius input is elementary but must be stated with its
range.  Let $p$ be prime, $0\le k<p$, and let
$\alpha,\alpha'\in\mathbb Z_{(p)}$ satisfy
$\alpha\equiv\alpha'\pmod p$.  Then



$$
\boxed{
 [X^j](1+X)^\alpha
 \equiv[X^j](1+X)^{\alpha'}\pmod p
 \quad(0\le j\le k).}
\tag{3.1}
$$



Indeed, $j!$ is a $p$-unit and every factor in
$\binom\alpha j$ is congruent to the corresponding factor in
$\binom{\alpha'}j$.  The same statement holds after replacing
$X$ by a polynomial with zero constant term and truncating at degree
$k$, because every contributing exponent is at most $k$.

On an actual row, $r<p$, so $k=r-1<p$.  Moreover



$$
\frac{2r}{3}=4M-\frac{14p}{3}\equiv4M\pmod p,
 \qquad
 -r=-6M+7p\equiv-6M\pmod p.
\tag{3.2}
$$



All denominators in (3.2) are units because $p>3$.  Thus Item 314's
generalized binomial powers may be replaced, through the selected
coefficient, by powers depending only on $M$.

## 4. The common fixed-$M$ kernel

Keep Item 314's polynomials



$$
\begin{aligned}
 E_-(X)&=2X^3+X^2+6X-3,\\
 P_-(X)&=16X^6+55X^5-199X^4+278X^3-42X^2-33X+45,\\
 E_+(X)&=2X^3+7X^2+14X+6,\\
 P_+(X)&=16X^6+151X^5+316X^4+352X^3
          +388X^2+292X+120,
\end{aligned}
\tag{4.1}
$$



and put



$$
\begin{aligned}
 Q(X)&=1+X+\frac{X^2}{2},\\
 R_-(X)&=\frac{(1+X)(1+X^2)P_-(X)}{E_-(X)^4},\\
 R_+(X)&=\frac{(X+2)(X^2+2X+2)P_+(X)}{E_+(X)^4},\\
 U_-(X)&=\frac{(1+X^2)^4}{(1-X)^6},\\
 U_+(X)&=\frac{Q(X)^4}{(1+X)^6}.
\end{aligned}
\tag{4.2}
$$



Define



$$
\boxed{
 \mathcal K_M(X)
 =18R_-(X)U_-(X)^M
 +11\,16^{M-1}R_+(X)U_+(X)^M.}
\tag{4.3}
$$



Item 314's two Lagrange formulas are



$$
\begin{aligned}
 ra_r&=-12[X^{r-1}]R_-(X)
       (1+X^2)^{2r/3}(1-X)^{-r},\\
 rb_r&=-12[X^{r-1}]R_+(X)
       Q(X)^{2r/3}(1+X)^{-r}.
\end{aligned}
\tag{4.4}
$$



Apply (3.1)-(3.2) at degree $r-1$, multiply (2.5) by $r$,
and use (4.3).  This proves the exact cross-prime bridge



$$
\boxed{
 16^{M-1}rG_{r,s}
 \equiv-12[X^{r-1}]\mathcal K_M(X)\pmod p.}
\tag{4.5}
$$



The Taylor coefficients of $R_\pm$ have denominators supported only
at $2,3$, and the same is true for $U_+$; hence the selected
coefficient denominator is a $p$-unit.  Since $p\nmid12r16$, if



$$
U_{M,k}:=\operatorname {num}([X^k]\mathcal K_M(X)),
\tag{4.6}
$$



then every actual row satisfies



$$
\boxed{
 D_{r,s}\equiv0\pmod p
 \Longleftrightarrow
 p\mid U_{M,,6M-7p-1}.}
\tag{4.7}
$$



This is the requested cross-prime coupling: the modulus changes, but
the rational function $\mathcal K_M$ does not.

There is also one kernel for every $M$.  Summing (4.3) geometrically
gives



$$
\boxed{
 \sum_{M\ge1}\mathcal K_M(X)Y^M
 =18R_-(X)\frac{YU_-(X)}{1-YU_-(X)}
 +11R_+(X)\frac{YU_+(X)}{1-16YU_+(X)}.}
\tag{4.8}
$$



Thus $U_{M,k}$ is, up to primitive denominator clearing, a
coefficient of one fixed bivariate rational function.  The selected
array itself has the constant-term realization



$$
\sum_{M,p\ge0}[X^{6M-7p-1}]\mathcal K_M(X)A^MB^p
 =\operatorname {CT}_X
 \frac{X\,\mathcal K(X,AX^{-6})}{1-BX^7},
\tag{4.9}
$$



where $\mathcal K(X,Y)$ denotes the right side of (4.8).  Formula
(4.9) is structural; it is not a divisibility theorem.

## 5. The actual two-coordinate residual is retained

The second coordinate has not been replaced by a fixed target.  Put



$$
\Delta_M(p)=
 \left(
 U_{M,,6M-7p-1},
 H_{(5p-4M-3)/2}
 -\Theta_{6M-7p,,(5p-4M-1)/2}
 \right).
\tag{5.1}
$$



The second entry is interpreted in $\mathbb F_p$ after its certified
unit denominator is cleared.  Equations (1.2) and (4.7) give



$$
\boxed{
 p\text{ is a nondegenerate original collision on }M
 \Longleftrightarrow
 \Delta_M(p)=(0,0)\pmod p.}
\tag{5.2}
$$



In particular, a zero-density theorem for the first coefficient alone
would close the nondegenerate branch, while a joint theorem could be
stronger.  Item 359 proves neither.  It merely puts the first necessary
condition into its smallest presently known common cross-prime object
while retaining the legitimate second target in (5.1).

## 6. Exact pole order and the recurrence barrier

The first summand in (4.3) has an exact pole of order $6M$ at
$X=1$.  The second is regular there, and



$$
P_-(1)=120,
 \qquad
 (1+1)(1+1^2)P_-(1)=480,
 \qquad
 E_-(1)=6.
\tag{6.1}
$$



Similarly, the second summand has an exact pole of order $6M$ at
$X=-1$, the first is regular there, and



$$
P_+(-1)=45,
 \qquad
 (-1+2)((-1)^2-2+2)P_+(-1)=45,
 \qquad
 E_+(-1)=-3,
 \qquad Q(-1)=\frac12.
\tag{6.2}
$$



No cancellation between the summands is possible at either point.
Therefore the reduced denominator of $\mathcal K_M$ is divisible by



$$
(1-X)^{6M}(1+X)^{6M},
\tag{6.3}
$$



and has degree at least $12M$.  The minimal eventual scalar
constant-coefficient recurrence order of a rational generating series
is the degree of its reduced denominator.  Hence



$$
\boxed{\operatorname {ord}_{\rm rec}(\mathcal K_M)\ge12M.}
\tag{6.4}
$$



A direct common denominator for (4.3) is



$$
\mathcal D_M(X)=
 E_-(X)^4E_+(X)^4(1-X)^{6M}(1+X)^{6M},
\tag{6.5}
$$



of degree $12M+24$.  After multiplication by (6.5), each numerator
summand has degree $14M+21$.  Thus its direct homogeneous coefficient
recurrence begins only beyond that degree.

By (1.4), the selected indices satisfy



$$
0\le k=r-1\le\frac{2M-26}{5}<\frac{2M}{5}.
\tag{6.6}
$$



Consequently the full selected interval lies far before the homogeneous
range of the natural recurrence, and its length is much smaller than
the unavoidable eventual order (6.4).  This proves a scoped no-go for
bounded or sublinear constant-coefficient propagation of the selected
coefficients.  It does not exclude a new arithmetic identity special
to the affine selector.

## 7. Pointwise height and product localization do not reach the mass scale

For $0\le k\le2M/5$, elementary binomial bounds in (4.2)-(4.3),
together with the fixed inverse-polynomial bounds from Item 314, give



$$
\boxed{
 \log^+\operatorname {ht}([X^k]\mathcal K_M)=O(M).}
\tag{7.1}
$$



For example, the coefficients of $(1+X^2)^{4M}$,
$(1-X)^{-6M}$, $Q(X)^{4M}$, and $(1+X)^{-6M}$ through this
range are bounded by $C^M$ after a denominator $6^{O(M)}$ is
cleared.  Convolution with either fixed $R_\pm$ preserves this form.

There are $O(M/\log M)$ prime rows in (1.4).  Therefore multiplying
the nonzero selected coefficient numerators yields only



$$
\sum_{p\text{ in }(1.4)}
 \log^+|U_{M,,6M-7p-1}|
 =O\!\left(\frac{M^2}{\log M}\right).
\tag{7.2}
$$



This is much larger than the raw $O(M)$ mass in (1.5), so the height
product is noncompetitive.  Exact-zero coefficient rows must be
stratified separately: height says nothing at all there.  Finally,
replacing each numerator by its gcd with the matched modulus gives only



$$
\sum_p\log\gcd\bigl(p,|U_{M,,6M-7p-1}|\bigr)
 \le\sum_p\log p,
\tag{7.3}
$$



which is precisely the raw interval bound.  Thus neither individual
height nor the obvious common product changes the ledger.

## 8. A fixed rational comparison kernel with full selector mass

The insufficiency of rational-kernel metadata can be made exact.  Define



$$
\boxed{
 \mathcal V(X,Y)=
 \frac{X^4Y^2(1+5Y^7)+Y^6(5+Y^7)}
 {(1-X^6Y)(1-Y^7)^2}.}
\tag{8.1}
$$



For $p=6a+1$, $r=6b+5$, one has



$$
M=b+7a+2,
 \qquad
 [X^{r-1}Y^M]\mathcal V=6a+1=p.
\tag{8.2}
$$



For $p=6a+5$, $r=6b+1$, one has



$$
M=b+7a+6,
 \qquad
 [X^{r-1}Y^M]\mathcal V=6a+5=p.
\tag{8.3}
$$



Indeed,



$$
\sum_{a\ge0}(6a+1)T^a=\frac{1+5T}{(1-T)^2},
 \qquad
 \sum_{a\ge0}(6a+5)T^a=\frac{5+T}{(1-T)^2},
\tag{8.4}
$$



and summing over $b\ge0$ supplies $(1-X^6Y)^{-1}$.

Every actual prime $p>3$ lies on one of these two rays, and
$6M=r+7p$.  Hence, on every actual selector in (1.4),



$$
p\mid[X^{6M-7p-1}Y^M]\mathcal V.
\tag{8.5}
$$



The coefficient in (8.5) has logarithmic height $O(\log M)$, and
$\mathcal V$ is one fixed rational function.  Nevertheless its tied
prime support has the full mass (1.5).

This comparison does **not** assert that $\mathcal V=\mathcal K$, or
that the actual branch behaves adversarially.  It proves the precise
information-class statement



$$
\boxed{
 \text{fixed rationality + holonomicity + pointwise height do not
 control matched-modulus coefficient divisibility}.}
\tag{8.6}
$$



A theorem using the actual numerator, monodromy, a reciprocity law, or
an average gcd can still succeed.

## 9. The missing cross-prime statistic

Let



$$
W_{j=2}^{\rm nd}(M)=
 \sum_{p\text{ in }(1.4)}(\log p)
 1_{\Delta_M(p)=(0,0)}.
\tag{9.1}
$$



Closure requires



$$
\boxed{W_{j=2}^{\rm nd}(M)=o(M)},
\tag{9.2}
$$



and even the first-coordinate theorem



$$
\sum_{p\text{ in }(1.4)}(\log p)
 1_{p\mid U_{M,,6M-7p-1}}=o(M)
\tag{9.3}
$$



would suffice.  Formula (9.3) is the smallest currently exposed
selector-aware cross-prime statistic.

Additive character inversion rewrites each divisibility indicator, but
the moduli and the sampled coefficient both change with $p$.  A
standard large sieve controls a common coefficient vector sampled by
many characters; it does not estimate this affine coefficient-modulus
diagonal without an additional cross-prime relation.  Taking absolute
squares returns the collision-blind statistic already closed by Item
355.

Likewise, Item 355's possible almost-all-$M$ route would require



$$
\sum_{p\asymp X}(\log p)\sqrt{E_p}=o(X^2).
\tag{9.4}
$$



Pointwise height (7.1) gives no saving for the collision energy $E_p$,
and coefficientwise character Parseval is exactly the identity defining
that energy.  The comparison kernel (8.1) shows that even fixed rational
structure with much smaller height is compatible with a full prescribed
selector diagonal.  Therefore neither input can imply (9.4) by itself.

The first genuinely new required input is one of:

1. a reciprocity or factor-localization theorem for the actual matched
   pair $(p,U_{M,6M-7p-1})$;
2. an average-gcd theorem for that affine diagonal;
3. a joint cross-prime theorem using the moving second coordinate in
   (5.1); or
4. an actual-family exceptional-set theorem strong enough to justify an
   almost-all-$M$ construction.

All four remain **OPEN**.

## 10. Strict labels and deterministic replay

The companion certificate verifies:

- the selector, Fermat collapse, and kernel congruence on seven
  predeclared actual rows;
- the two branchwise truncated-exponent coefficient identities modulo
  the selected prime;
- the exact pole evaluations and degree formulas;
- the comparison-kernel coefficient formulas on declared symbolic
  rectangles; and
- the raw rational capacity normalization.

These declared rows and rectangles are **EXACT FINITE ONLY**.  They are
not a prime scan or collision census.

The selector identities (1.3), Fermat identity (2.3), truncated exponent
lemma (3.1), common-kernel theorem (4.5)-(4.9), pole theorem
(6.1)-(6.6), height-scale obstruction (7.1)-(7.3), and comparison
kernel theorem (8.1)-(8.6) are **PROVED** for their stated all-parameter
families.

Weighted nonconcentration for the actual coefficient diagonal, joint
cross-prime control of the moving target, and the almost-all-$M$
energy saving are **OPEN**.  Accordingly every ledger change is zero.
