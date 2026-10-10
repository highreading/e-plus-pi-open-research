> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of mixed-parity Darboux and Volterra structure

Date: 2026-09-13. Reviewer: audit_results.

Reviewed in full: raw_mixed_parity_volterra_and_darboux.md.
**PASS. No mathematical correction is required.** In particular the
all-index obstruction to a positive scalar self-adjoint weight, the exact
positive Volterra inverse, and the actual-family Hermite–Biehler limitation
all pass. They do not establish the unresolved mixed zero bound.

I also read the same-parity ECT proof in
raw_weaker_oscillation_and_spectral_rank.md and the exact recurrence,
root-interlacing, and differential identities in
raw_borel_legendre_literature.md. I inspected the existing four seed controls
but did not construct additional polynomial degrees. A separate symbolic
operator check, using arbitrary parameters rather than further degrees, is
saved as mixed_parity_operator_independent_checks.py/.json.

## 1. Positive coupling and the individual Stieltjes ratios

The raw recurrence $Q_{k+1}=tQ_k+\beta_kQ_{k-1}$, after the coefficient
Borel transform, gives $F_{k+1}=IF_k+\beta_kF_{k-1}$.
Evaluating the raw derivative identity at zero for odd index gives


$$
\frac{b_m}{\alpha_m}=\frac{(2m+1)^2}{4m+1}.
$$


Combining this with the constant-term recurrence yields every factor in
(1), and therefore the two normalized recurrences (2)–(3), including
$m=0$, $E_0=1$, $O_0=x$, and $O_{-1}=0$.
Their matrix transfer factors as


$$
\begin{pmatrix}1&a_mI\\0&1\end{pmatrix}
 \begin{pmatrix}1&0\\c_mI&d_m\end{pmatrix}.
$$


Its entries are positive operators and its operator determinant is $d_m$.
The inverse has negative entries, so the stated limitation concerning
arbitrary signed combinations is necessary and correctly retained.

The previously reviewed strict imaginary-axis interlacing gives the order
$0<a_1<b_1<\cdots<a_m<b_m$. The residue at $-a_j^2$ has $j-1$
negative factors in both numerator and denominator, and hence is positive.
The leading coefficients $1/(2m)!$ and $1/(2m+1)!$ give the constant
$1/(2m+1)$ in (6). The second monic coefficient is exactly


$$
A_k=\frac{k^2(k-1)^2}{2(2k-1)}.
$$


Direct symbolic simplification verifies (7). The mass varies with $m$,
which rules out only the specified common Stieltjes function whose
approximants already match that coefficient. The note does not overstate
this as excluding other transformed or varying-weight constructions.

## 2. Same-parity ECT and the exact order-r elimination

The same-parity coefficient matrix is the Newton collocation matrix at
the ordered nodes $(\sigma+2j)(\sigma+2j+1)$, with positive factorial
column scales. I checked the applicable positive bidiagonal factorization
and increasing-node corollary in the primary
[Newton interpolation paper, Theorem 2 and Corollary 2(a)](https://arxiv.org/pdf/2312.14483).
Its terminology includes nonnegative minors. The triangular zero entries
are therefore compatible with the prior note's use of total
nonnegativity.

For any selected rows, the first $r$ coefficient columns have a strictly
positive Vandermonde minor. Every monomial derivative determinant is
positive at $y>0$. Cauchy–Binet consequently proves the required
Wronskian positivity, including all initial subsets. Multiplication by
the common positive $x^\sigma$ and the increasing substitution $y=x^2$
preserve nonvanishing. The multiplicity version of the ECT bound used in
Section 8 follows from successive quotient differentiation.

The resulting monic Wronskian operator $A_r$ is rational and smooth for
$x>0$, with kernel exactly the selected parity span. Right division of
$A_rL$ by the monic $A_r$ gives an order-four quotient and remainder
of order below $r$. That remainder kills all selected eigenfunctions;
their nonzero Wronskian forces every remainder coefficient to vanish.
Comparison of the terms of order $r+3$ cancels the coefficient of
$D^{r-1}$ in $A_r$, giving


$$
\widetilde a_4=x^2,\qquad \widetilde a_3=(2r+4)x.
$$


No second-order reduction or right-endpoint condition follows.

The transformed opposite-parity functions remain independent: an
annihilated combination would belong to the selected parity span, which
has zero intersection with the opposite-parity polynomial span.

## 3. Origin jets and their signs

Invertibility of the first $r$ Taylor coefficient columns gives a
kernel basis with successive leading powers
$x^\sigma,x^{\sigma+2},\ldots,x^{\sigma+2r-2}$.
Wronskian division therefore has a Laurent expansion


$$
A_r=x^{-r}\bigl(P_r(\theta)+x^2B_r(\theta)+O(x^4)\bigr).
$$


The coefficients after the leading term have degree at most $r-1$
in theta because the differential operator is monic. Annihilating the
first $r-1$ leading powers forces the stated roots of $B_r$.

For the final leading power, the ratio of the next coefficient is


$$
\frac{\mathcal S}{[(\sigma+2r)(\sigma+2r-1)]^2}.
$$


Indeed the determinant with Newton degrees $0,\ldots,r-2,r$, divided
by the one with degrees $0,\ldots,r-1$, is
$\sum_i\lambda_{k_i}-\sum_{j=0}^{r-1}\kappa_j=\mathcal S$;
the factorial column ratio supplies the denominator.
Evaluating the two theta polynomials at the final leading power gives
the factors $2^rr!$ and $2^{r-1}(r-1)!$, respectively, proving
the scalar $b_r$ in (10), including $r=1$.

For each coefficient of $H_r$, the $P_r$ term supplies its highest
lambda degree, while every later operator term multiplies a lower-degree
Taylor coefficient. This proves (12) with no missing terms. Opposite
parity makes every $P_r(\sigma'+2j)$ nonzero. The resulting signs are
exactly $(-1)^{\min(j,r-1)}$ for even elimination and
$(-1)^{\min(j,r)}$ for odd elimination. Formula (13) and the negative
first two-column minor in its stated ranges follow.

The existing controls at seeds (5), (6), (5,7), and (6,8) check these
normalizations, but the all-index proof does not depend on them.

## 4. No positive scalar self-adjoint weight after elimination

For an order-four expression with coefficients $\widetilde a_j$,
formal self-adjointness in weight $w$ requires


$$
\widetilde a_3=2(w\widetilde a_4)'/w.
$$


The exact leading coefficients therefore force $w'/w=r/x$;
every positive candidate is a constant multiple of $x^r$.

The original lowest part is $x^{-2}\theta^2(\theta-1)^2$.
Using $P_r(t-2)/P_r(t)=(t-\sigma-2r)/(t-\sigma)$ in the
lowest intertwining identity gives precisely the two polynomials (14).
For weight $x^r$, the adjoint of $x^{-2}p(\theta)$ is
$x^{-2}p(1-r-\theta)$. A self-adjoint expression would have the
same lowest polynomial and thus the indicated root reflection.

For even elimination $r\ge2$, the root $r$ reflects to $1-2r<-r$,
below all its roots. For odd elimination $r\ge1$, the root $r+1$
reflects to $-2r<-r$. These comparisons include multiplicities and
exclude every such case.

I separately derived the two full coefficients in the remaining even
case $r=1$ by noncommutative differential-operator multiplication.
Both formulas preceding (15) are exact for arbitrary $a(x)$. With
the forced weight $x$, the first-order symmetry requirement is


$$
\widetilde a_1=\widetilde a_2'
                   +\widetilde a_2/x-6/x.
$$


Subtracting gives exactly the displayed defect. The normalized even
seed has $f=1+\lambda_*x^2/4+O(x^4)$, so
$a=-f'/f=-\lambda_*x/2+O(x^3)$. The defect is therefore
$(1+2\lambda_*)x+O(x^3)$, nonzero for every actual seed.

This proves the claimed all-index obstruction for the actual Darboux
operator. It neither excludes matrix/indefinite formulations nor
contradicts a possible mixed zero theorem.

## 5. Exact positive Volterra inverse and convergence

Let $v=f'$ and $q=x^2s^2(v/s)'$, where $s=\sin x/x$.
The identity $(x^2s')'+x^2s=0$ gives


$$
s^{-1}q'=(x^2v')'+x^2v.
$$


Differentiation proves the entire factorization (16), not just its
leading terms. For analytic $f$, both $q(0)$ and $q'(0)$ vanish.
Successive integration then leaves exactly the two constants $f(0)$
and $f'(0)$, giving (17). There are no discarded origin constants.

For the zero-data inverse, putting $w=xv$ instead yields


$$
w''+w=\frac{If}{x},\qquad w(0)=w'(0)=0.
$$


The sine Green kernel and one final integration give (18). Its factors
are positive in $0<t<u<x<1$. This independently checks both the
positive inverse and the alternative integral normalization.

On the real interval, $c_0=\sin1\le s\le1$. Bounding the three
multiplication factors in $\mathcal K$ and performing the four
integrations gives exactly


$$
\mathcal K(x^d)\le
 \frac{c_0^{-2}x^{d+2}}{(d+1)^2(d+2)^2}.
$$


Iteration telescopes to the two squared-factorial bounds in the note.
They prove uniform convergence for $x\in[0,1]$ and lambda in any
compact complex set, as well as termwise lambda differentiation.

Uniqueness does not require an unproved regular-endpoint ODE theorem:
if a continuous solution of the homogeneous Volterra equation satisfies
$h=\lambda\mathcal Kh$, the same iterated bound applied to
$\|h\|_\infty$ makes $h=0$. The analytic normalized ODE solutions
exist from their explicit two-step Taylor recurrence (its ratio is
$O(j^{-2})$ on compact lambda sets). They satisfy (17), hence agree
with these unique Volterra sums. This supplies the analytic
identification without interchanging uncontrolled x derivatives.

Strict positivity of $\mathcal K^j1$ and $\mathcal K^jS$ for
$x>0$ proves every asserted lambda derivative is strictly positive
at every lambda at least zero, including lambda zero.

For the Rolle statement, the first two differentiations give at least
$q-2$ interior zeros of $q$. The endpoint zero $q(0)=0$ restores
one zero in the next differentiation, and $q'(0)=0$ restores one
in the last weighted differentiation. The result is at least $q-2$
zeros of $Lf$. If an intermediate expression vanishes identically,
the zero origin constants reduce $f$ to the span of $1,S$, or
$Lf=0$; the former has at most one zero and the latter is excluded
in the statement. Thus the degenerate cases cause no exception.

## 6. The actual-family Hermite–Biehler limitation

For $2s+1$ selected same-parity functions in $y=x^2$, the $2s$
value/derivative conditions leave a nonzero polynomial. ECT bounds
zeros with multiplicity by $2s$, so all prescribed zeros are
exactly double, there are no other positive zeros, and each second
derivative is nonzero. Its sign is constant off those points; after
choosing it positive, all the second derivatives are positive.

The selected positive polynomial $e_1$ makes $e+\epsilon e_1$
strictly positive on the positive real axis. More precisely, at each
double zero $y_i$, rescale $y=y_i+\sqrt\epsilon z$. Division by
epsilon converges locally uniformly in complex z to


$$
\tfrac12e''(y_i)z^2+e_1(y_i).
$$


Its roots are simple and nonreal. Disjoint small disks about these
roots and polynomial root continuity give one persistent conjugate
pair near each $y_i$. All coefficients remain real. The dimension
count for an arbitrary r-dimensional block follows by selecting
$2\lfloor(r-1)/2\rfloor+1$ functions.

I read the primary
[Kozhan–Tyaglov Theorem 3.1](https://arxiv.org/pdf/2302.07018).
It requires real strictly interlacing input polynomials of consecutive
degrees, in addition to its normalization and parameter assumptions.
The construction above validly excludes applying that hypothesis to
every arbitrary actual parity mixture. It does not classify all
indefinite-space or matrix versions of Hermite–Biehler theory.

Likewise, the reviewed
[Zhang–Filipuk Theorems 1.1–1.3](https://arxiv.org/pdf/1402.1569)
concern actual multiple-orthogonal paths under the stated AT-system
weight hypotheses. No such model for the transformed mixtures is
proved here, so the note's applicability restriction is accurate.

## 7. What remains unresolved

All exact identities and the three main structural conclusions pass.
The missing statement is still the zero bound for an arbitrary signed
combination of the remaining opposite-parity eigenfunctions after
elimination. Positive individual kernels, absolute monotonicity in
lambda, and the two separate parity ECT properties do not establish
that mixed statement. Consequently this review supplies no all-index
high spectral rank theorem, no quantitative endpoint estimate, and no
proof concerning the rationality of $e+\pi$.
