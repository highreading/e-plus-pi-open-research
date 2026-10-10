> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 347 - chosen-prime Kummer completion and linear-conductor obstruction

Checked: 2026-09-01 (Beijing time)

## 1. Scope, capacity, and verdict

Retain the actual ordinary-$j=2$ phase



$$
p=2r+6s+3=6m+2d+1,
 \qquad m=s-1,
 \qquad d=r+4,
\tag{1.1}
$$



and Item 341's exact nondegenerate collision coordinates



$$
\boxed{4^{m+1}=c_r^*,\qquad H_m=\Theta_{r,s}\pmod p},
 \qquad
 H_m=\sum_{u=0}^m\frac1{8^u}\binom{2u}{u}.
\tag{1.2}
$$



Item 344 showed that the quadratic Frobenius carrier does not remove
the moving prefix, and that bounded-degree or bounded-mode cutoff-first
completion cannot reach positive-rate rows.  This item retains the full
mode set and asks whether it collapses to one legitimate complete
finite-field or Greene-hypergeometric object of bounded conductor.

The answer has two parts.

> **PROVED - exact target-forced complete-sum theorem.**  Let
> $\chi$ be the quadratic character of $\mathbf F_p$, extended by
> $\chi(0)=0$, and put
> 

$$
> W_m(x)=\sum_{u=0}^m x^{-u}\qquad(x\in\mathbf F_p^*).
>
$$


> Then
> 

$$
> \boxed{
> H_m=-\sum_{x\in\mathbf F_p^*}W_m(x)\chi(1-x/2)\pmod p.}
>
$$


> Consequently the second equation of (1.2) is exactly the single
> target-retaining complete sum
> 

$$
> \boxed{
> H_m-\Theta_{r,s}
> =\sum_{x\in\mathbf F_p^*}
> \left(\Theta_{r,s}-W_m(x)\chi(1-x/2)\right)\pmod p.}
>
$$



> **PROVED - linear Kummer-rank/conductor obstruction.**  At a chosen
> prime above $p$, the canonical multiplicative-character lift of
> $W_m$ is the direct sum of the $m+1$ distinct Kummer modes
> $1,\omega^{-1},\ldots,\omega^{-m}$.  Character orthogonality proves
> that this semisimple length is minimal.  Tensoring by the fixed
> quadratic factor preserves distinctness.  Hence every exact lift in
> this diagonal Greene/Kummer category has rank, and therefore
> conductor, at least $m+1$.

> **PROVED - the original full completion is genuinely full.**  On the
> exponent group of order $N=p-1$, the sharp cutoff has exactly
> 

$$
> N-\gcd(N,m+1)+1>\frac{5N}{6}
>
$$


> nonzero Fourier modes.  The normalization $1/N$ is a $p$-unit;
> there is no lost $p$-adic digit, but there is unavoidable linear
> rank after the collapse.

> **PROVED - positive-rate implication.**  Item 344's fixed-$M$ edge
> theorem shows that rows with $m=o(M)$ have $o(M)$ logarithmic
> prime mass.  Therefore every portion capable of retaining positive
> linear mass has $m+1\asymp M$, and the preceding conductor lower
> bound is linear there.

> **OPEN.**  The theorem closes bounded-conductor completion inside the
> natural semisimple Kummer/Greene transform category.  It does not
> exclude a nonlinear, nonsemisimple, or target-specific sheaf whose
> trace is only congruent at the chosen prime and is not an exact lift
> of the cutoff weight.

No weighted nonconcentration theorem follows.  Thus



$$
\boxed{\text{new booking}=0},\qquad
 \boxed{\text{new capacity reduction}=0},\qquad
 \boxed{\text{ceiling remains }1/105\text{ per }6M}.
\tag{1.3}
$$



The degenerate triple-minor chart remains open and unchanged.  No
finite zero census is used.

## 2. Every half-binomial term is a complete quadratic moment

Set



$$
N=p-1,
 \qquad n=\frac{N}{2}=3m+d.
\tag{2.1}
$$



For $0\leq u\leq m$, Euler's criterion and the actual inequality
$m<n$ give



$$
\begin{aligned}
 -\sum_{x\in\mathbf F_p^*}x^{-u}\chi(1-x/2)
 &=-2^{-u}\sum_{y\in\mathbf F_p^*}y^{-u}(1-y)^n\\
 &=2^{-u}(-1)^u\binom nu\\
 &\equiv\frac1{8^u}\binom{2u}{u}\pmod p.
 \end{aligned}
\tag{2.2}
$$



For completeness, the middle equality follows by expanding
$(1-y)^n$.  If $u>0$, the only exponent contributing to the power
sum over $\mathbf F_p^*$ is $N-u+u=N$; if $u=0$, the trivial
character is extended by zero at the omitted point and gives the same
formula.  The final congruence is



$$
\binom nu\equiv\binom{-1/2}{u}
 =(-1)^u4^{-u}\binom{2u}{u}\pmod p.
\tag{2.3}
$$



Summing (2.2) for $0\leq u\leq m$ and interchanging two finite sums
proves



$$
\boxed{
 H_m=-\sum_{x\in\mathbf F_p^*}
 \left(\sum_{u=0}^m x^{-u}\right)\chi(1-x/2)\pmod p.}
\tag{2.4}
$$



There is no discarded endpoint and no denominator crossing $p$.
The formula is valid for every actual tied prime, not just for a fixed
ray or a finite sample.

Because $\sum_{x\in\mathbf F_p^*}1=N=-1\pmod p$, subtracting the
legitimate moving target gives



$$
\boxed{
 H_m-\Theta_{r,s}
 =\sum_{x\in\mathbf F_p^*}
 \left(\Theta_{r,s}-W_m(x)\chi(1-x/2)\right)\pmod p.}
\tag{2.5}
$$



Thus the target is retained inside the complete sum.  Formula (2.5)
is not a fixed-target surrogate.

## 3. The chosen-prime Jacobi/Greene interpretation

Formula (2.4) has an exact multiplicative-character lift.  Let



$$
K=\mathbf Q(\mu_N).
\tag{3.1}
$$



Since $p\equiv1\pmod N$, $p$ splits completely in $K$.  Choose a
prime $\mathfrak P\mid p$ and the Teichmuller character



$$
\omega:\mathbf F_p^*\longrightarrow\mu_N
\tag{3.2}
$$



so that $\omega(x)\equiv x\pmod{\mathfrak P}$.  Put



$$
B_u=\omega^{-u},
 \qquad \varphi=\omega^{N/2}.
\tag{3.3}
$$



With all multiplicative characters extended by zero at zero, the
Jacobi sum



$$
J(B_u,\varphi)=\sum_{y\in\mathbf F_p}B_u(y)\varphi(1-y)
\tag{3.4}
$$



satisfies



$$
\boxed{
 -B_u(2)J(B_u,\varphi)
 \equiv\binom nu\left(-\frac12\right)^u
 \equiv\frac1{8^u}\binom{2u}{u}pmod{\mathfrak P}}
\tag{3.5}
$$



for every $0\leq u\leq m$.  Therefore



$$
\boxed{
 H_m\equiv-\sum_{u=0}^mB_u(2)J(B_u,\varphi)pmod{\mathfrak P}.}
\tag{3.6}
$$



Up to standard normalization, (3.6) is a truncated Greene-binomial
transform.  It is genuinely a congruence at the selected prime
$\mathfrak P$; this choice cannot be replaced by an unspecified
complex embedding.

## 4. Full Fourier completion and exact collapse

Choose a generator $g$ of $\mathbf F_p^*$, put
$\xi=\omega(g)$, and let



$$
L=m+1,
 \qquad
 \widehat I_L(a)=\sum_{u=0}^{L-1}\xi^{-au}
 \quad(a\in\mathbf Z/N\mathbf Z).
\tag{4.1}
$$



Fourier inversion on the character-exponent group gives the cutoff
$1_{0\leq u<L}$ with normalization $1/N$.  Completing (3.6) over
all $N$ multiplicative characters produces inner sums



$$
\sum_{B}B(2g^{-a})J(B,\varphi).
\tag{4.2}
$$



Multiplicative-character orthogonality collapses (4.2) exactly:



$$
\begin{aligned}
 \sum_BB(y)J(B,\varphi)
 &=\sum_{t\in\mathbf F_p}\varphi(1-t)\sum_B B(yt)\\
 &=N\varphi(1-y^{-1}).
 \end{aligned}
\tag{4.3}
$$



Taking $y=2g^{-a}$ yields



$$
H_m\equiv-\sum_{a\bmod N}
 \widehat I_L(a)\varphi(1-g^a/2)\pmod{\mathfrak P},
\tag{4.4}
$$



which is the chosen-prime lift of (2.4), after writing $x=g^a$.

The cutoff completion is genuinely full.  For $a\ne0$,
$\widehat I_L(a)=0$ exactly when



$$
N\mid aL.
\tag{4.5}
$$



There are $\gcd(N,L)-1$ such nonzero $a$, so the exact support is



$$
\boxed{N-\gcd(N,L)+1.}
\tag{4.6}
$$



The actual tied phase gives



$$
N=6m+2r+8=6L+2r+2>6L.
\tag{4.7}
$$



Consequently



$$
\boxed{
 N-\gcd(N,L)+1\geq N-L+1>\frac{5N}{6}+1.}
\tag{4.8}
$$



Unlike the additive $p$-mode completion, $1/N$ is a $p$-unit.
Thus (4.4) avoids an extra-$p$-adic-digit loss.  What survives is a
linear number of nonzero modes.

## 5. Minimal rank of the collapsed Kummer weight

The canonical lift of the weight in (2.4) is



$$
\widetilde W_m(x)=\sum_{u=0}^mB_u(x)
 =1+\omega^{-1}(x)+\cdots+\omega^{-m}(x).
\tag{5.1}
$$



The $L=m+1$ characters in (5.1) are distinct because $m<N$.
Multiplicative characters form an orthogonal basis for functions on
$\mathbf F_p^*$.  Hence (5.1) has no expression as a linear
combination of fewer than $L$ character modes.

Sheaf-theoretically, (5.1) is the trace of a semisimple direct sum of
$L$ distinct rank-one Kummer sheaves.  Tensoring each summand with
the fixed pullback having trace $\varphi(1-x/2)$ preserves geometric
nonisomorphism: the ratio of the $u$- and $v$-summands is the
nontrivial Kummer character $\omega^{v-u}$ whenever $u\ne v$.
Therefore



$$
\boxed{
 \operatorname {rank}\mathcal F_{p,m}\geq m+1,
 \qquad
 \operatorname {cond}\mathcal F_{p,m}\geq m+1}
\tag{5.2}
$$



for every exact semisimple Kummer/Greene lift of this diagonal
completion.  Adding the constant target in (2.5) cannot cancel any of
these constituents, because all of them retain the quadratic branch at
$x=2$; it contributes at most one additional constant constituent.

This is stronger than observing that one displayed formula has high
degree.  Orthogonality proves minimal semisimple length inside the
natural category used by the full character transform.

The scope remains precise.  A general $p$-dependent nonsemisimple
sheaf, an $F$-crystal with no exact characteristic-zero trace lift, or
a nonlinear target-specific construction need not decompose in this
Kummer basis.  Those mechanisms are not closed by (5.2).

## 6. Positive-rate bulk and capacity

At fixed $M$,



$$
5p=4M+2m+3,
 \qquad r=6M-7p.
\tag{6.1}
$$



Item 344 proved that for every $u(M)=o(M)$, the total logarithmic
prime mass of rows with $m\leq u(M)$ is $o(M)$.  More uniformly,
discarding $m<\delta M$ costs $O(\delta M)+o(M)$.  On the remaining
bulk,



$$
\operatorname {rank}\mathcal F_{p,m}\geq m+1\geq\delta M.
\tag{6.2}
$$



Thus every bounded-conductor subfamily of the completion (2.5) lies in
a zero-rate edge.  Allowing conductor $o(M)$ still reaches only an
$o(M)$-mass edge.  The raw ordinary-$j=2$ mass and capacity remain



$$
\frac{2}{35}M+o(M),
 \qquad
 \frac1{105}\text{ per }6M.
\tag{6.3}
$$



The complete-sum formula therefore changes representation but not the
ledger.  A positive result would still require a weighted theorem
uniform in linearly growing rank, or a genuinely different compression
of the **joint** target.

## 7. Chosen-prime versus Archimedean information

Three distinctions are essential.

First, (3.5) is a congruence at the chosen
$\mathfrak P\mid p$.  Galois conjugation changes the Teichmuller
identification and permutes character exponents; it does not preserve
the ordered cutoff $0\leq u\leq m$.  A norm over all conjugates is
therefore a product of different cutoffs, not the actual target.

Second, nontrivial Jacobi sums have complex absolute value $\sqrt p$,
but complex nonvanishing does not imply nonvanishing modulo
$\mathfrak P$.  An algebraic integer can be nonzero in every complex
embedding and still lie in $\mathfrak P$.  The triangle bound for
(3.6) is in any case $O(m\sqrt p)$, which is larger than $p$ on the
positive-rate bulk and supplies no divisibility exclusion.

Third, the $p$-th-root additive completion and the present
$(p-1)$-st-root Mellin completion behave differently.  At a prime
above $p$, a primitive $p$-th root satisfies $\zeta_p\equiv1$,
so its additive modes coalesce and division by $p$ costs precision.
In contrast, $p$ splits in $\mathbf Q(\mu_{p-1})$, the Teichmuller
modes remain distinct, and $1/(p-1)$ is a unit.  The price is the
linear rank (5.2), not an extra digit.

Therefore neither an ordinary Weil bound nor a characteristic-zero
hypergeometric nonvanishing statement can be credited toward the
chosen-prime collision gate.

## 8. Strategic closure and next input

**PROVED:** the full multiplicative-character completion, its exact
collapse to one target-retaining complete quadratic correlation, exact
Fourier support greater than $5(p-1)/6$, and minimal Kummer rank
$m+1$.

**EXACT FINITE ONLY:** deterministic replays of the identities on
declared rows.  No zero search is performed.

**CLOSED AS SUFFICIENT BY ITSELF:** a bounded-rank or bounded-conductor
Greene/Kummer completion obtained by diagonalizing the actual cutoff;
Archimedean Jacobi/Weil bounds without chosen-prime control; any direct
sublinear-rank restriction as a positive-rate mechanism.

**OPEN:** a nonlinear or nonsemisimple compression, a genuinely
chosen-prime $F$-crystal of bounded complexity for the whole joint
residual, weighted distribution with linearly growing conductor, and
the degenerate triple-minor branch.

No new prime mass is booked and no existing ceiling is reduced.

## 9. Deterministic certificate

The companion checker verifies:

1. the termwise complete-moment identity (2.2);
2. the collapsed complete sum (2.4) and target-retaining identity
   (2.5) on declared actual rows;
3. Jacobi reduction using exact finite-field character sums;
4. the exact cutoff Fourier-support count (4.6)-(4.8);
5. orthogonality and minimal Kummer support $m+1$;
6. the fixed-$M$ identities and all unit/range inequalities.

All row data are labeled **EXACT FINITE REPLAY ONLY**.  The general
statements follow from the displayed symbolic proofs.
