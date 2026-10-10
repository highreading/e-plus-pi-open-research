> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A Hardy--$H^2$ circle bound for the saturated $k=2$ low-endpoint image

## Exact exponential-monomial Gram matrices and finite $m=2,d=2$ diagnostics

Checked: 2026-08-27 UTC

## 1. Scope and verdict

This note replaces the coefficientwise $\ell^1$ circle majorant by the
quadratic Hardy norm for a **fixed centered exponential polynomial**.  The
analytic part is exact.  If



$$
f_{r,a}(z)=z^a e^{rz},\qquad r\in\mathbb R,quad a\in\mathbb Z_{\geq0},
$$



then its normalized circle Gram matrix has the explicit branch-free formula



$$
\boxed{
 \left\langle f_{r,a},f_{s,b}\right\rangle_R
 =\sum_{\ell\geq\max(a,b)}
   \frac{R^{2\ell}r^{\ell-a}s^{\ell-b}}
        {(\ell-a)!(\ell-b)!}.}                           \tag{1}
$$



If an analytic function $F$ has a zero of order at least $K$ at the
origin and $H=F/z^K$, then, for every $R>\pi$,



$$
\boxed{
 |F(i\pi)|\leq
 \frac{\pi^K\lVert H\rVert_{2,R}}
      {\sqrt{1-\pi^2/R^2}}.}                             \tag{2}
$$



For a finite-dimensional endpoint fiber, minimizing the square of the norm
in (2) is a positive-definite quadratic problem with an exact Schur-complement
formula.  If the fiber is defined over $\mathbb Q$, its rational points have
the same infimum as its real points.

The finite replay applies these identities to the intrinsically saturated
global $k=2$ image from
`sources/root_unity_k2_global_image_saturation_audit.md`, with



$$
m=2,\qquad d=2,
 \qquad n\in\{5,8,10\}.                                  \tag{3}
$$



All common-origin cancellations are performed and checked over
$\mathbb Z$ before conversion to high-precision real arithmetic.  For the
best tested primitive endpoint at each $n$, the optimized $H^2$ logarithmic
upper bound improves on the optimized coefficientwise $\ell^1$ bound for
the **same analytic function** by



$$
15.4798\ldots,quad30.1299\ldots,quad
             36.0468\ldots.                              \tag{4}
$$



These are large finite savings, approximately $3.10n,3.77n,3.60n$.
Dividing the same savings by $n\log n$ gives
$1.924,1.811,1.565$, respectively.  Thus the three rows are consistent
with an $O(n)$ improvement and give no evidence that the leading
$n\log n$ ledger has changed.  They do not prove an asymptotic estimate in
either direction.

At $n=8$, one tested primitive endpoint has



$$
p_0-p_2\pi^2=-0.0204039538\ldots,
 \qquad \log U_{H^2}=-3.6019703263\ldots,                 \tag{5}
$$



where $U_{H^2}$ denotes the numerically optimized right side of (2).
Nevertheless its relative exponent is only $1.21038\ldots$, below the
strict degree-two rank-one threshold $3$.  More importantly, the continuous
optimizer carries no denominator or integer shortest-vector control.

The decimal optimization is a reproducible high-precision diagnostic, not
an interval-arithmetic theorem.  The exact results in this note are
(1), (2), and the quadratic minimization and rational-density statements
below.  No irrationality or transcendence conclusion about $e+\pi$ follows.

## 2. The centered global functions and their exact origin jets

Write a centered global exponential polynomial in the unique form



$$
F(z)=\sum_{r=-m}^{m}\sum_{a=0}^{A}c_{r,a}z^ae^{rz}.     \tag{6}
$$



For the cleared $k=2$ Wronskian image, $A=2n$.  Multiplying the
uncentered function by $e^{-mz}$ produces (6), does not change its origin
order, and has modulus one at $z=i\pi$.  In the present $m=2$ rows the
endpoint itself is unchanged, because $e^{-2i\pi}=1$.

The derivative of (6) at the origin is exactly



$$
F^{(j)}(0)=
 \sum_{r=-m}^{m}\sum_{0\leq a\leq\min(A,j)}
 c_{r,a}\frac{j!}{(j-a)!}r^{j-a}.                       \tag{7}
$$



For integral coefficient arrays every term in (7) is integral.  Therefore
the assertion that $F$ has order at least $K$ can, and in the replay does,
get checked by the exact identities



$$
F^{(j)}(0)=0,qquad0\leq j<K.   \tag{8}
$$



In the exterior-square rows used here,



$$
K=2m(n+1)=4(n+1).               \tag{9}
$$



This exact check is essential: forming nearly cancelling exponential sums
in floating point before removing the common zero would make the quotient
Gram matrix unreliable.

## 3. Exact circle Gram matrix

Use the normalized boundary inner product



$$
\langle f,g\rangle_R=
 \frac1{2\pi}\int_0^{2\pi}
 f(Re^{i\theta})\overline{g(Re^{i\theta})}\,d\theta,
 \qquad \lVert f\rVert_{2,R}^2=\langle f,f\rangle_R.    \tag{10}
$$



Let



$$
\Phi(r,s;R)
 =\sum_{j\geq0}\frac{(rsR^2)^j}{(j!)^2}.                \tag{11}
$$



Then



$$
\boxed{
 \langle z^ae^{rz},z^be^{sz}\rangle_R
 =\partial_r^a\partial_s^b\Phi(r,s;R).}                 \tag{12}
$$



Indeed



$$
z^ae^{rz}
 =\sum_{\ell\geq a}
   \frac{r^{\ell-a}}{(\ell-a)!}z^\ell,                 \tag{13}
$$



and distinct monomials are orthogonal on the circle, with
$\lVert z^\ell\rVert_{2,R}^2=R^{2\ell}$.  Multiplying the two Taylor
series proves (1).  Termwise differentiation of (11) proves (12).  Equally,
the circle integral is the constant term of



$$
R^{2b}z^{a-b}\exp\!\left(rz+\frac{sR^2}{z}\right).    \tag{14}
$$



These formulas are valid at zero and for opposite-sign rates without any
choice of square-root branch.  When $r,s>0$, (1) may also be written



$$
R^{a+b}\left(\frac r s\right)^{(b-a)/2}
 I_{|a-b|}(2R\sqrt{rs}),                                 \tag{15}
$$



where $I_\nu$ is the modified Bessel function.

Now suppose $F_i$ are integral global basis functions and every $F_i$
has the common zero (8).  Put



$$
d_{i,j}=F_i^{(j)}(0),\qquad H_i(z)=\frac{F_i(z)}{z^K}.
$$



The quotient Gram matrix has the positive outer-product expansion



$$
\boxed{
 A_{ij}(R)=\langle H_i,H_j\rangle_R
 =\sum_{\ell\geq0}
 \frac{d_{i,K+\ell}d_{j,K+\ell}R^{2\ell}}
      {((K+\ell)!)^2}.}                                  \tag{16}
$$



Formula (16) both preserves the exact cancellations and avoids subtracting
large, nearly equal Gram entries.  If the coefficient arrays of the
$F_i$ are linearly independent, uniqueness of (6) implies that
$A(R)$ is positive definite.

## 4. The zero-factored Hardy evaluation bound

Expand



$$
H(z)=\sum_{j\geq0}h_jz^j.
$$



Parseval and Cauchy--Schwarz give



$$
\begin{aligned}
 \lVert H\rVert_{2,R}^2
   &=\sum_{j\geq0}|h_j|^2R^{2j},\\
 |H(i\pi)|
   &\leq
   \left(\sum_{j\geq0}|h_j|^2R^{2j}\right)^{1/2}
   \left(\sum_{j\geq0}(\pi/R)^{2j}\right)^{1/2}\\
   &=\frac{\lVert H\rVert_{2,R}}
           {\sqrt{1-\pi^2/R^2}}.                        \tag{17}
 \end{aligned}
$$



Multiplication by $\pi^K$ proves (2).  Since
$\lVert H\rVert_{2,R}=R^{-K}\lVert F\rVert_{2,R}$, the equivalent form is



$$
|F(i\pi)|\leq
 \left(\frac\pi R\right)^K
 \frac{\lVert F\rVert_{2,R}}
      {\sqrt{1-\pi^2/R^2}}.                              \tag{18}
$$



The factor in (17) is the exact norm of point evaluation on the full Hardy
space of the disk of radius $R$.  It need not be sharp after restricting
to the finite-dimensional global-image subspace.

## 5. Exact constrained quadratic minimum

Let $F_x=\sum_{i=1}^t x_iF_i$, let $A=A(R)$ be the quotient Gram matrix,
and encode the retained endpoint coefficients by a rational matrix
$B\in\mathbb Q^{t\times q}$:



$$
B^tx=p.                         \tag{19}
$$



Assume that $A$ is positive definite, $B$ has column rank $q$, and
the fiber (19) is nonempty.  Lagrange multipliers give



$$
\boxed{
 x_*=A^{-1}B(B^tA^{-1}B)^{-1}p}                         \tag{20}
$$



and



$$
\boxed{
 \min_{B^tx=p}\lVert F_x/z^K\rVert_{2,R}^2
 =p^t(B^tA^{-1}B)^{-1}p.}                               \tag{21}
$$



For completeness, put $S=B^tA^{-1}B$.  The vector (20) satisfies (19).
Every other feasible vector is $x_*+v$, where $B^tv=0$, and



$$
v^tAx_*=v^tBS^{-1}p=0.                                 \tag{22}
$$



Thus its quadratic value is the value in (21) plus $v^tAv$, proving the
claim.

If $B,p$ are rational and the real fiber is nonempty, ordinary rational
linear algebra supplies one rational point $x_0$ and a rational basis of
$\ker B^t$.  Rational coordinate vectors in that basis are dense in the
real coordinate space.  Continuity of the quadratic form therefore proves



$$
\inf_{\substack{x\in\mathbb Q^t\\B^tx=p}}x^tAx
 =\min_{\substack{x\in\mathbb R^t\\B^tx=p}}x^tAx.       \tag{23}
$$



Equation (23) is only an infimum statement.  It supplies neither a bound for
the denominators of a near-minimizer nor a short integral vector after
clearing those denominators.  This is the central arithmetic obstruction to
turning the continuous $H^2$ optimization into a primitive linear-form
certificate.

## 6. Comparison with the coefficientwise bound

For the same centered function (6), the elementary coefficientwise circle
majorant is



$$
M_1(R;c)=
 \sum_{r=-m}^{m}\sum_{a=0}^{A}
                  |c_{r,a}|R^ae^{|r|R}.                 \tag{24}
$$



The maximum principle applied after dividing by the common zero gives



$$
|F(i\pi)|
 \leq\left(\frac\pi R\right)^K M_1(R;c).                \tag{25}
$$



The replay first optimizes (2) over the real endpoint fiber and over $R$.
It then freezes that analytic function and separately minimizes (25) over
$R$.  Consequently the reported difference compares two analytic
majorants for one and the same function; it does not compare unrelated
lattice vectors.  The $H^2$ advantage comes from quadratic cancellation
and orthogonality on the circle, both of which (24) discards.

There is no general implication that the difference between (25) and (2)
is $O(n)$.  Proving such a bound would require all-parameter control of
the quotient Gram spectrum together with the arithmetic size of a rational
near-minimizer.  The replay supplies only three finite rows.

## 7. Finite saturated-image diagnostics

The replay reconstructs the frozen saturated global image rather than
loading decimal matrices.  The exact structural rows are



$$
\begin{array}{c|c|c|c|c}
n&D&\nu&\operatorname{rank}L_{\rm sat}&K\\ \hline
5&4&5&3&24\\
8&5&6&4&36\\
10&5&6&3&44
\end{array}                                               \tag{26}
$$



Every endpoint coefficient outside degrees $0,2$ vanishes exactly.  For
each $n$, the replay tests the shortest saturated LLL row in Euclidean
global-coefficient norm and the row having the smallest
$|p_0-p_2\pi^2|$ among that LLL basis.  The latter rows give:



$$
\begin{array}{c|r|r|r|r|r|r}
n&(p_0,p_2)&\log|p_0-p_2\pi^2|&R_{H^2}&\log U_{H^2}
 &\log U_{\ell^1}&\log U_{\ell^1}-\log U_{H^2}\\ \hline
5 &(1867776,189247)& 2.834630&4.424896& 3.464238&18.943998&15.479761\\
8 &(27262976,2762317)&-3.892027&4.960888&-3.601970&26.528003&30.129973\\
10&(927363469867650908160,93961564433655820907)
 &11.156189&5.432940&11.528682&47.575516&36.046834
\end{array}                                               \tag{27}
$$



The optimized $H^2$ logarithmic upper bounds exceed the directly evaluated
endpoint logarithms by $0.629608$, $0.290056$, and $0.372493$.  This
positive slack is an important orientation and normalization check.

For the shortest global LLL rows, the corresponding $H^2$ savings over
the same-function $\ell^1$ bound are



$$
15.479900,qquad30.131464,qquad33.706923. \tag{28}
$$



At 180 decimal digits the endpoint residuals are below $10^{-141}$, and a
120-digit recomputation changes the optimized logarithmic values by less
than $4\cdot10^{-88}$.  The quotient-Gram series uses 240 post-zero Taylor
terms; repeating it with 180 terms changes none of the reported digits.
An independent direct circle quadrature agrees with (1) below
$6\cdot10^{-95}$ on five mixed-rate and mixed-degree samples.

These checks are numerical stability diagnostics, not directed-rounding
error bounds.  The exact cancellation check (8), by contrast, is performed
over $\mathbb Z$; its largest individual cancelling summands have 20, 38,
and 58 decimal digits for $n=5,8,10$.

Define the finite relative exponent diagnostic



$$
\widehat\Theta_{H^2}
 =1-\frac{\log U_{H^2}}{\log\max(|p_0|,|p_2|)}.          \tag{29}
$$



For the best-value rows in (27), it equals



$$
0.760099,qquad1.210383,qquad0.761207. \tag{30}
$$



All are below the strict rank-one degree-two threshold $3$.  In
particular, a negative logarithmic upper bound at one finite $n$ is not
the Roth-breaking height relation needed by the present route.

## 8. What this does and does not change in the ledger

The reusable conclusion is analytic: the exact Gram formula (1), the stable
zero-jet form (16), and the constrained minimum (21) provide the correct
Hardy replacement for a coefficientwise circle estimate on any finite
global-image subspace.

The finite data show that this replacement matters substantially at
moderate $n$.  They do **not** prove that its saving is subleading.  What
can be said rigorously is narrower:

1. no all-parameter bound for the spectrum or determinant of $A(R)$ is
   proved here;
2. no rational denominator, Smith-content, or integer-SVP estimate for a
   near-minimizer in (23) is proved;
3. the three observed savings are of size a few multiples of $n$, and the
   normalized values in (4) decrease on this small grid;
4. none of the tested endpoints meets the required relative exponent.

Thus the replay gives no observed change to the leading $n\log n$ ledger,
but it is not an obstruction theorem against such a change.  A successful
arithmetic use of $H^2$ would still need a uniform Gram estimate and a
simultaneous rational-denominator/content theorem.

## 9. Replay and files

The package consists of:

* `sources/root_unity_hardy_h2_saturated_circle_audit.md`;
* `scripts/root_unity_hardy_h2_saturated_circle_certificate.py`;
* `results/root_unity_hardy_h2_saturated_circle_certificate.json`; and
* `results/root_unity_hardy_h2_saturated_circle_hashes.sha256`.

Replay from the archive root with

    python3 scripts/root_unity_hardy_h2_saturated_circle_certificate.py

The script verifies the frozen saturation dependency by SHA-256 before
import, reconstructs the exact lattices for (3), checks the origin jets over
$\mathbb Z$, builds (16), performs the high-precision optimizations, and
checks the stated precision and truncation stability.  It asserts that peak
resident memory remains below 2 GiB.  The observed runtime and peak RSS are
reported by the replay but omitted from the deterministic JSON.

