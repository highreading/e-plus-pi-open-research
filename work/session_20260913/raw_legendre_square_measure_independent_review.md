> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the exact Legendre-square measure

Date: 2026-09-13. Reviewer: audit_results.

Target: raw_coupled_pencil_exact_legendre_square.md, Sections 1–4,
as saved before any additional edge asymptotics. The preceding pencil
has already passed raw_coupled_high_parity_independent_review.md.

**Verdict: PASS, with the same one-dimensional cross-measure scope
correction as in the preceding note.** The correction is now applied:
the cross-measure sign obstruction is for $r\ge2$, covering every
actual high block. The $r=1$ cross measure has one positive atom.
The exact compression, strict eigenvalue bounds and interlacing,
associated probability measure, complete density formula, finite
quadrature, and original two-boundary normalization all check.
No numerical or degree scan was used.

## 1. The precise compression and its boundaries

In $L^2([-1,1],du/2)$, the normalized Legendre recurrence has
coefficients $\alpha_k=k/\sqrt{4k^2-1}$. Applying it twice gives


$$
u^2\ell_{2m}
=\alpha_{2m}\alpha_{2m-1}\ell_{2m-2}
+(\alpha_{2m}^2+\alpha_{2m+1}^2)\ell_{2m}
+\alpha_{2m+1}\alpha_{2m+2}\ell_{2m+2}.
$$


The rational diagonal identity and squared off-diagonal identity in
(1) follow exactly from the displayed $\gamma_m,\delta_m$. Their
positive square roots and the alternating diagonal gauge fix every
sign. Thus the relevant space contains only the even degrees
$2a,2a+2,\ldots,2b$.

Compression of multiplication by $u^2$ retains both diagonal terms
at each boundary. Squaring multiplication by $u$ after compression
to this even space would instead give zero; squaring a prematurely
truncated adjacent-degree matrix can also lose a boundary term.
The target uses the correct compression throughout.

For a nonzero element of this finite polynomial space, both integrals
$\int u^2|q|^2\,du/2$ and $\int(1-u^2)|q|^2\,du/2$ are strictly
positive. Therefore $0<J_+<I$, yielding all $\omega_j>1$, not
merely the asymptotic lower bound from the previous perturbation
estimate.

## 2. The specified squared Legendre zeros

The ordinary Jacobi matrix on indices $0,\ldots,2b+1$ has characteristic
polynomial proportional to $P_{2b+2}$, by its determinant recurrence.
In even/odd ordering it is bipartite; its square has blocks $CC^T$
and $C^TC$. The even block is exactly the multiplication-by-$u^2$
compression on even indices $0,\ldots,2b$, including the highest
diagonal term $\alpha_{2b+1}^2$.

The matrix has no zero eigenvalue, because the even Legendre polynomial
has nonzero constant term. Each positive zero of $P_{2b+2}$ therefore
gives one eigenvalue $x_j^2$ of each squared block. There are $b+1$
such distinct values.

Removing the first coordinate of an irreducible tridiagonal matrix
gives strict interlacing: the characteristic determinant recurrence
excludes any common root of a matrix and its adjacent tail. Repeating
this $a$ times gives


$$
x_j^2<\theta_j<x_{j+a}^2.
$$


All indices are in range because $j\le r=b-a+1$. Taking positive
inverse square roots reverses the inequalities exactly as in (4).
For the separately stated $a=0$ extension there is equality.

## 3. Infinite tail, support and endpoint atoms

The change of variable $y=u^2$ gives precisely
$d\mu_0=dy/(2\sqrt y)$ and the orthonormal polynomials in (5).
Polynomial density on $[0,1]$ (continuous approximation followed
by $L^2$ density) makes the infinite Jacobi representation complete.
Alternatively, its tail is defined directly as the compression to
the closed span of the stated orthonormal polynomials.

That tail compression is a bounded selfadjoint positive contraction.
It need not be a reducing restriction of multiplication by $y$;
no such claim is used. If it had an eigenvector at zero or one, its
quadratic form would give respectively
$\int y|f|^2d\mu_0=0$ or
$\int(1-y)|f|^2d\mu_0=0$. Both force $f=0$ in $L^2(\mu_0)$.
Thus there are no endpoint eigenvectors and no endpoint atoms in its
first-coordinate spectral measure. The vector has norm one, so that
measure is a probability measure supported in $[0,1]$.

## 4. Stieltjes transform and the full density

The initial integral is


$$
m_0(z)=\int_0^1\frac{du}{z-u^2}.
$$


For real $z>1$, direct antiderivation gives (6). Defining the complex
function from this integral fixes its analytic continuation and avoids
any ambiguity in the square root and logarithm.

The tail Schur complement gives


$$
m_a(z)=\frac1{z-d_a-c_a^2m_{a+1}(z)}.
$$


Solving this identity proves (7), with the stated numerator sign and
$c_a^2$ factor. Composing in the order $a-1,\ldots,0$ gives the
matrix product in (8), whose determinant is $\prod c_k^2>0$.

On the upper side of the interval, the sign convention $1/(z-y)$
gives negative imaginary part:


$$
m_0(y+i0)=
\frac1{2\sqrt y}\log\frac{1+\sqrt y}{1-\sqrt y}
-\frac{i\pi}{2\sqrt y}.
$$


For a real Möbius transformation,


$$
\operatorname{Im}\frac{Aw+B}{Cw+D}
=\frac{(AD-BC)\operatorname{Im}w}{|Cw+D|^2}.
$$


The denominator is nonzero throughout $0<y<1$: if $C\ne0$ its
imaginary part is nonzero; if $C=0$, the positive determinant
forces $D\ne0$. This gives exactly (9), including its factor $1/2$.

The assertion that (9) describes the *entire* measure is justified.
On any compact interior interval, the upper branch of $m_0$ extends
analytically to a neighborhood of that interval, and its transformed
denominator stays bounded away from zero on a smaller neighborhood.
Its upper boundary imaginary parts therefore converge uniformly.
Stieltjes inversion gives absolute continuity there with the displayed
continuous density, excluding all interior singular measure.
An increasing union of such compact intervals leaves only the two
endpoints; their atoms were already excluded. No estimate uniform in
the growing index $a$ has been inferred from this argument.

## 5. Quadrature and the actual boundary transfer

For a first-coordinate matrix moment, a tridiagonal walk leaving
the first $r$ coordinates and returning must take at least $2r$
steps. Consequently the finite and infinite first-coordinate moments
agree through degree $2r-1$. The spectral theorem gives (10) with
$w_j=|v_j(1)|^2$, and eigenvector endpoint nonvanishing gives
strictly positive weights summing to one. This proof includes $r=1$.

The original transfer factors exactly as


$$
M+\tau H=M^{1/2}(I+\tau J)M^{1/2},\qquad J=DJ_+D.
$$


Inverting and inserting the original $B$ gives (11) with
$\widetilde B=DM^{-1/2}B$. Both the mass factor and the gauge are
necessary and are retained.

In a $J_+$ eigenbasis, each term initially has denominator
$1+\tau\theta_j$. Rewriting it as
$\theta_j(\tau+1/\theta_j)$ recovers the prior pencil's pole at
$-1/\theta_j=-\omega_j^2<-1$. The positive factor $1/\theta_j$
does not change any residue signs. Every pole remains visible at both
endpoints. For $r\ge2$ the cross residues alternate and cannot be
the weights of a positive scalar measure; at $r=1$ the sole cross
weight is positive, as now explicitly stated.

The fixed positive associated measure and finite quadrature are valid
new structure. They do not remove the actual two-boundary factors,
the high-block coefficient constraints, or the growing derivative
cancellation in the original polynomial solution. The note correctly
leaves the mixed zero-count and irrationality consequences unresolved.
