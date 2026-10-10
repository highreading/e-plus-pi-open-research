> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# All-degree Hardy endpoint collapse and the Dirichlet boundary

## Exact block geometry, primitive polynomial approximation, and the role of parity

Checked: 2026-08-27 UTC

## 1. Scope and verdict

Fix an endpoint degree $d\geq1$.  Let



$$
A_p(X)=p_0+p_1X+\cdots+p_dX^d,\qquad
 p=(p_0,\ldots,p_d)\in\mathbb Z^{d+1},                  \tag{1}
$$



and suppose a finite-dimensional analytic construction supplies a positive
quotient form



$$
Q_n(p)=p^tC_np,\qquad C_n\succ0. \tag{2}
$$



This note proves the all-degree version of the binary endpoint-collapse
theorem.

In the phase-aligned setting, the endpoint evaluation is the one-dimensional
real form



$$
\ell(p)=A_p(\pi).               \tag{3}
$$



Use $u=\ell(p)$ and $v=(p_1,\ldots,p_d)$.  There are exact parameters
$a_n>0$, $\eta_n\in\mathbb R^d$, and
$\mathcal T_n\succ0$ for which



$$
\boxed{
 {Q_n(p)\over a_n}
  =(u+\eta_n^tv)^2+v^t\mathcal T_nv.}                    \tag{4}
$$



Set



$$
\boxed{
 \varepsilon_n
 =\max_{\|x\|_\infty\leq1}
   \sqrt{x^t\bigl(\eta_n\eta_n^t+\mathcal T_n\bigr)x}.}   \tag{5}
$$



Then, for every real endpoint,



$$
\boxed{
 \left|\sqrt{Q_n(p)/a_n}-|A_p(\pi)|\right|
 \leq\varepsilon_n\|v\|_\infty.}                         \tag{6}
$$



Consequently, minimizing over primitive integer endpoints with
$1\leq\|v\|_\infty\leq H$ differs from the original problem of minimizing
$|A_p(\pi)|$ by at most $\varepsilon_nH$.  This is an exact comparison,
not an asymptotic heuristic.

For $d+1$ integer coefficients and one real evaluation form, the
geometry-of-numbers/Dirichlet critical exponent is



$$
\boxed{d}.                      \tag{7}
$$



It is sharp as a dimension-only statement.  Under the temporary hypothesis
that $s=e+\pi$ is algebraic of degree $r$, the conditional
$e$-measure lower exponent is



$$
\boxed{\kappa_r(d)=r^2d+r-1.}    \tag{8}
$$



Thus Dirichlet merely meets the boundary when $r=1$, and is strictly below
it when $r>1$.  A contradiction requires a strict improvement over (7),
not merely a quotient form which collapses to evaluation.

There are two important qualifications.

1. Projective collapse $\varepsilon_n\to0$ alone does not transfer an
   approximation exponent when the endpoint height $H_n\to\infty$.
   To transfer an absolute exponent $\mu$, one needs the quantitative rate

   

$$
\varepsilon_nH_n=o(H_n^{-\mu}). \tag{9}
$$



2. Ordinary integer coefficients evaluated directly at $i\pi$ do not
   phase-align the even and odd monomials.  The real and imaginary parity
   blocks are orthogonal and the best dimension-only exponent is only

   

$$
\boxed{\lfloor d/2\rfloor}.     \tag{10}
$$



   Gaussian phase alignment $A_p(-iz)$, whose value at $i\pi$ is
   $A_p(\pi)$, restores all $d+1$ coordinates and exponent $d$.
   Restricting parity reduces dimension but does not correspondingly halve
   the polynomial degree seen after substituting $\pi=s-e$.

The theorem identifies an exact equivalence/circularity barrier.  It proves
neither a collapse rate nor an exceptional approximation to $\pi$, and it
does not classify $e+\pi$.

## 2. A vector-valued quotient identity

It is useful first to allow a general real evaluation map.  Let



$$
L:\mathbb R^q\longrightarrow\mathbb R^m
$$



have rank $m$, and let $Q(x)=x^tCx$ with $C\succ0$.  Choose a right
inverse $S$ of $L$ and a basis matrix $N$ of $\ker L$.  Then



$$
x=Su+Nv,\qquad u=Lx             \tag{11}
$$



is a unique coordinate decomposition.  In these coordinates write



$$
\begin{pmatrix}S^t\\N^t\end{pmatrix}
 C
 \begin{pmatrix}S&N\end{pmatrix}
 =
 \begin{pmatrix}A&B\\B^t&D\end{pmatrix}.                 \tag{12}
$$



Both $A$ and $D$ are positive definite, and the Schur complement



$$
R=D-B^tA^{-1}B                  \tag{13}
$$



is positive definite.  Completing the square gives the exact identity



$$
\boxed{
 Q(x)=
 \left\|A^{1/2}u+A^{-1/2}Bv\right\|_2^2+v^tRv.}          \tag{14}
$$



View the two terms in (14) as orthogonal components.  The perturbation away
from $A^{1/2}u$ has squared norm



$$
v^t\left(B^tA^{-1}B+R\right)v=v^tDv.
$$



The reverse triangle inequality therefore yields



$$
\boxed{
 \left|\sqrt{Q(x)}-\sqrt{u^tAu}\right|
 \leq\sqrt{v^tDv}.}                                      \tag{15}
$$



This is the vector-valued collapse theorem.  It applies, for example, to the
two real components of an unaligned complex evaluation.  No rationality or
integrality hypothesis is used in (11)--(15).

If a sequence is normalized by positive scalars $a_n$, and



$$
{A_n\over a_n}\to H\succ0,\qquad
 {B_n\over a_n}\to0,\qquad
 {D_n\over a_n}\to0,                                    \tag{16}
$$



then $Q_n/a_n$ converges projectively to the evaluation seminorm
$u^tHu$.  A small determinant or condition number without the two alignment
conditions in (16) is not sufficient.

## 3. Exact rank-one coordinates in every degree

Return to (3).  Put



$$
\lambda=(\pi,\pi^2,\ldots,\pi^d)^t,\qquad
 v=(p_1,\ldots,p_d)^t,\qquad
 u=p_0+\lambda^tv.                                      \tag{17}
$$



Then



$$
p=
 \begin{pmatrix}1&-\lambda^t\\0&I_d\end{pmatrix}
 \binom uv.                                              \tag{18}
$$



Write the transformed quotient form as



$$
\begin{pmatrix}1&0\\-\lambda&I_d\end{pmatrix}
 C_n
 \begin{pmatrix}1&-\lambda^t\\0&I_d\end{pmatrix}
 =
 \begin{pmatrix}a_n&b_n^t\\b_n&D_n\end{pmatrix}.         \tag{19}
$$



Set



$$
\eta_n={b_n\over a_n},\qquad
 \mathcal T_n={1\over a_n}
       \left(D_n-{b_nb_n^t\over a_n}\right)\succ0.       \tag{20}
$$



Equations (4) and (5) now follow from



$$
\eta_n\eta_n^t+\mathcal T_n={D_n\over a_n}.             \tag{21}
$$



The maximum in (5) is finite and exact.  Since a positive semidefinite
quadratic form is convex in each coordinate separately,



$$
\boxed{
 \varepsilon_n^2
 =\max_{\sigma\in\{-1,1\}^d}
   \sigma^t{D_n\over a_n}\sigma.}                        \tag{22}
$$



This finite vertex formula is sometimes more convenient than an operator
norm.  Formula (6) follows by writing



$$
{Q_n(p)\over a_n}
 =\left\|(u,0)+
    \left(\eta_n^tv,\mathcal T_n^{1/2}v\right)\right\|_2^2
$$



and applying the reverse triangle inequality.

There is also an intrinsic interpretation:



$$
a_n=Q_n(1,0,\ldots,0),\qquad
 v^tD_nv=
 Q_n(-\lambda^tv,v).                                    \tag{23}
$$



Thus $\varepsilon_n$ measures the largest normalized quotient norm, on the
unit coefficient cube, of a real endpoint whose evaluation is exactly zero.

For fixed $d$, the following are equivalent:



$$
\varepsilon_n\to0,
\qquad
 {1\over a_n}
 \begin{pmatrix}a_n&b_n^t\\b_n&D_n\end{pmatrix}
 \to
 \begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
 {C_n\over a_n}\to\ell^t\ell,                            \tag{24}
$$



where $\ell(p)=p_0+\lambda^tv$.  Positivity gives
$\|b_n/a_n\|=o(1)$ once $D_n/a_n=o(1)$, so (22) controls both transverse
size and alignment.

## 4. Primitive integer optimization

For an integer $H\geq1$, define



$$
\begin{aligned}
 \Delta_\pi^{(d)}(H)
  &=\min_{\substack{p\in\mathbb Z^{d+1},\ \gcd(p)=1\\
                    1\leq\|v\|_\infty\leq H}}
       |A_p(\pi)|,\\
 \mathcal M_n^{(d)}(H)
  &=\min_{\substack{p\in\mathbb Z^{d+1},\ \gcd(p)=1\\
                    1\leq\|v\|_\infty\leq H}}
       \sqrt{Q_n(p)/a_n}.
                                                               \tag{25}
 \end{aligned}
$$



For each fixed nonzero $v$, each objective tends to infinity as
$|p_0|\to\infty$.  Hence its minimum over the admissible primitive integers
$p_0$ exists.  Since there are finitely many admissible $v$, both minima
in (25) exist.  Taking minima in (6) gives



$$
\boxed{
 \left|\mathcal M_n^{(d)}(H)-\Delta_\pi^{(d)}(H)\right|
 \leq\varepsilon_nH.}                                    \tag{26}
$$



Equivalently,



$$
\boxed{
 \left|{\mathcal M_n^{(d)}(H)\over H}
       -{\Delta_\pi^{(d)}(H)\over H}\right|
 \leq\varepsilon_n.}                                     \tag{27}
$$



Primitivity causes no loss.  Dividing an integer endpoint by its coefficient
gcd decreases its height and divides both its evaluation and the homogeneous
quotient norm by the same integer.

The cutoff in (25) uses the nonconstant coefficient height because it makes
(26) exact.  It is exponent-equivalent to the usual coefficient height.  If
$|A_p(\pi)|\leq1$, then



$$
H(A_p)\leq
 1+\left(1+\pi+\cdots+\pi^d\right)\|v\|_\infty,           \tag{28}
$$



while always $\|v\|_\infty\leq H(A_p)$.

Suppose $H_n\to\infty$.  For any $\mu\geq0$, condition (9) and (26)
imply



$$
\mathcal M_n^{(d)}(H_n)=O(H_n^{-\mu})
 \quad\Longleftrightarrow\quad
 \Delta_\pi^{(d)}(H_n)=O(H_n^{-\mu}),                    \tag{29}
$$



with the same statement for $o(H_n^{-\mu})$.  Without (9), even
$\varepsilon_n\to0$ gives no exponent transfer: the additive error
$\varepsilon_nH_n$ may dominate the desired small value.

## 5. Dirichlet exponent $d$

The numbers $1,\pi,\ldots,\pi^d$ are linearly independent over
$\mathbb Q$.  Consider the $(H+1)^d$ fractional parts



$$
\left\{\lambda^tv\right\},\qquad
                         v\in\{0,1,\ldots,H\}^d.          \tag{30}
$$



They are distinct.  Two adjacent points on the unit circle have cyclic
distance at most $(H+1)^{-d}$.  Subtracting their indices and choosing the
corresponding integer $p_0$ gives a nonzero endpoint with



$$
\|v\|_\infty\leq H,\qquad
 0<|A_p(\pi)|\leq(H+1)^{-d}.                             \tag{31}
$$



Primitive division only improves (31).  Moreover



$$
H(A_p)\ll_d H.                  \tag{32}
$$



This proves the absolute Dirichlet exponent $d$, or relative exponent
$d+1$ after division by coefficient height.

The exponent cannot be improved from dimension alone.  Let



$$
\theta=2^{1/(d+1)}.
$$



It is a real algebraic integer of degree $d+1$.  For every nonzero integer
polynomial $P$ of degree at most $d$, the algebraic integer
$P(\theta)$ is nonzero and



$$
|N_{\mathbb Q(\theta)/\mathbb Q}P(\theta)|\geq1.
$$



Each of the other $d$ conjugate factors is at most $C_dH(P)$, for a
constant $C_d$.  Hence



$$
|P(\theta)|\geq C_d^{-d}H(P)^{-d}. \tag{33}
$$



Thus there are evaluation vectors for which exponent $d$ is optimal.
Any exponent strictly beyond $d$ for $\pi$ must use special arithmetic or
analytic structure; it is not a consequence of having $d+1$ coordinates.

## 6. Comparison with the conditional $e$-measure

Assume temporarily that $s=e+\pi$ is algebraic of degree $r$.  The
fixed-degree norm reduction and quantitative $e$-measure give, for every
$\delta>0$, all sufficiently large primitive degree-$d$ polynomials,



$$
\boxed{
 |A_p(\pi)|
 >H(A_p)^{-\left(r^2d+r-1+\delta\right)}.}               \tag{34}
$$



Compare (31) with (34):



$$
\begin{array}{c|c|c}
 &\text{absolute exponent}&\text{relative exponent}\\ \hline
 \text{Dirichlet}&d&d+1\\
 \text{conditional \(e\)-measure}&r^2d+r-1&r^2d+r
 \end{array}.                                             \tag{35}
$$



The difference of the absolute exponents is



$$
(r^2-1)d+r-1.                   \tag{36}
$$



For $r=1$, it is zero.  Equality is insufficient: (34) is contradicted only
by a strict exponent improvement.  For $r>1$, the difference is positive.
Therefore the dimension-only exponents supplied by quotient collapse and
integer optimization do not by themselves exclude even rational $e+\pi$,
let alone every algebraic degree.

This comparison concerns the actual degree of $A_p$.  If a selected
endpoint loses its leading coefficients, $d$ in (34) must be replaced by
its actual degree.

## 7. Gaussian phase alignment

Define



$$
C_p(z)=A_p(-iz)
 =\sum_{j=0}^d p_j(-i)^jz^j\in\mathbb Z[i][z].           \tag{37}
$$



Then



$$
\boxed{C_p(i\pi)=A_p(\pi).}                             \tag{38}
$$



Every coefficient is changed only by a Gaussian unit.  Consequently,



$$
H(C_p)=H(A_p),\qquad
 \operatorname{cont}_{\mathbb Z[i]}(C_p)
 =\operatorname{cont}_{\mathbb Z}(A_p)                  \tag{39}
$$



up to a unit.  This is exactly the phase alignment obtained by combining an
even endpoint block with $-i$ times an odd endpoint block.  It turns the
complex value at $i\pi$ into one real evaluation form without changing
height, content, coefficient dimension, or degree.  Therefore the main
rank-one theorem and critical exponent $d$ apply to the aligned Gaussian
construction.

## 8. What happens without phase alignment

Let instead



$$
P_p(z)=\sum_{j=0}^dp_jz^j
 \in\mathbb Z[z].
$$



At $i\pi$,



$$
\begin{aligned}
 E_p&=\sum_{2k\leq d}(-1)^kp_{2k}\pi^{2k},\\
 O_p&=\sum_{2k+1\leq d}(-1)^kp_{2k+1}\pi^{2k+1},\\
 |P_p(i\pi)|^2&=E_p^2+O_p^2.                             \tag{40}
 \end{aligned}
$$



The even and odd coefficient sets are disjoint.  Let
$\Delta_{\rm e}(H)$ and $\Delta_{\rm o}(H)$ be the least nonzero values
of $|E_p|$ and $|O_p|$, respectively, among pure-parity primitive vectors
of coefficient height at most $H$.  Then exactly



$$
\boxed{
 \min_{\substack{0\ne p\in\mathbb Z^{d+1},\ \gcd(p)=1\\
                 H(p)\leq H}}
 |P_p(i\pi)|
 =\min\{\Delta_{\rm e}(H),\Delta_{\rm o}(H)\}.}           \tag{41}
$$



Indeed pure-parity vectors attain the right side.  A vector with both blocks
nonzero has modulus at least each of its two block moduli.  Dividing either
block by its own coefficient gcd can only reduce its height and modulus, so
each nonzero block is bounded below by its corresponding pure primitive
minimum.  Hence a mixed vector cannot do better.

The numbers of even and odd coefficients are



$$
q_{\rm e}=\left\lfloor{d\over2}\right\rfloor+1,\qquad
 q_{\rm o}=\left\lceil{d\over2}\right\rceil.             \tag{42}
$$



Their separate Dirichlet exponents are $q_{\rm e}-1$ and
$q_{\rm o}-1$.  Taking the better block in (41) gives



$$
\boxed{
 \max(q_{\rm e}-1,q_{\rm o}-1)=\left\lfloor{d\over2}\right\rfloor.} \tag{43}
$$



This parity exponent is also sharp as a dimension-only statement.  Put
$h=\lfloor d/2\rfloor\geq0$, take
$\beta=2^{1/(h+1)}$, and set $\vartheta=\sqrt\beta$.  At
$i\vartheta$, both parity blocks are, up to the fixed factor
$\vartheta$ in the odd block, integer polynomials in $\beta$ of degree at
most $h$.  The same algebraic-norm argument as in (33) bounds every nonzero
block below by $c_hH^{-h}$, while the even-block Dirichlet construction
attains exponent $h$.  For $h=0$, this is the trivial constant bound, so
the assertion includes $d=1$.

Thus ordinary real coefficients at $i\pi$ lose roughly half the available
dimension.  The vector-valued identity (14)--(15) describes the associated
rank-two evaluation seminorm, but it cannot create real/imaginary
cancellation.

Parity also does not produce a matching reduction in the conditional
measure cost.  More precisely, an even block of actual degree $2j$ has
$j+1$ integer coefficients and Dirichlet exponent $j$, whereas its
conditional absolute threshold is



$$
2r^2j+r-1.                       \tag{44}
$$



For every $j\geq1$ and $r\geq1$, (44) is strictly larger than $j$;
the case $j=0$ supplies no sequence tending to zero.  Writing the block as
a degree-$j$ polynomial in $\pi^2$ does not halve its degree after
$\pi=s-e$, because $\pi^2=(s-e)^2$.  An odd block of actual degree
$2j+1$ is $\pi$ times such an even block.  The fixed nonzero factor
$\pi$ leaves exponent $j$ unchanged, while the even factor still has
threshold (44) (and applying the measure directly in degree $2j+1$ gives
an even larger threshold).  Thus neither parity improves the comparison,
including when leading coefficients vanish and the actual degree drops.

## 9. Logical status and replay

The exact theorems are:

1. the vector-valued block identity (14) and comparison (15);
2. the all-degree rank-one normal form (4);
3. the transverse vertex formula (22);
4. the primitive optimization comparison (26)--(27);
5. the quantitative rate requirement (9);
6. the Dirichlet theorem (31) and its sharp dimension-only obstruction (33);
7. the conditional threshold comparison (35);
8. the aligned Gaussian identity (38)--(39); and
9. the unaligned parity decomposition (41)--(44).

No asymptotic statement about $C_n$ or $\varepsilon_n$ is assumed as a
theorem.  If a future construction proves a collapse rate, (26) and (29)
state exactly what approximation result follows.

The replay package consists of:

* sources/root_unity_hardy_all_degree_endpoint_collapse_theorem.md;
* scripts/root_unity_hardy_all_degree_endpoint_collapse_certificate.py;
* results/root_unity_hardy_all_degree_endpoint_collapse_certificate.json;
* results/root_unity_hardy_all_degree_endpoint_collapse_hashes.sha256.

The certificate checks the block identities over exact symbolic and rational
arithmetic, the Gaussian phase identity for degrees $1$ through $12$,
the parity counts, the threshold ledger, and finite exhaustive instances of
the Dirichlet pigeonhole construction.  This theorem does not classify
$e+\pi$.
