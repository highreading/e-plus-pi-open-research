> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Denominator-free Hardy endpoint quotients and their exact two-dimensional geometry

## A correction to the clearing interpretation, an evaluation-collapse criterion, and the Dirichlet boundary

Checked: 2026-08-27 UTC

## 1. Scope and verdict

Let $V_{\mathbb Q}$ be a finite-dimensional rational space of entire
exponential polynomials, all having a common zero of order at least $K$ at
the origin.  Suppose that a rational endpoint map



$$
E:V_{\mathbb Q}\longrightarrow \mathbb Q^2
$$



satisfies, after the fixed centering normalization,



$$
E(F)=(p_0,p_2)\quad\Longrightarrow\quad
 F(i\pi)=p_0-p_2\pi^2.                                  \tag{1}
$$



This is the situation of the even, degree-two, saturated $k=2$ image.
There are two conclusions.

First, **denominators of a global representative do not obstruct the
Hardy/e-measure argument**.  If a primitive integer endpoint $p$ lies in
the rational image of $E$, one may minimize the Hardy norm over the real
fiber $E(F)=p$.  The real minimizer is a legitimate entire auxiliary
function: the common zero and (1) are exact complex-linear identities, and
the Hardy estimate has no integrality hypothesis on the coefficients of
$F$.  If rational coefficients are desired, rational points in the exact
fiber approach the same minimum.  Their denominators are not present in
the conditional lower bound for the already integral endpoint polynomial



$$
A_p(X)=p_0-p_2X^2.              \tag{2}
$$



Thus the large clearing multipliers found in the exact quotient--LP audit
remain correct finite arithmetic data, but they are irrelevant to this
endpoint-only analytic route.  They matter only for a different method
which independently requires the *global* coefficient vector to be
integral.

Second, the resulting $2$-by-$2$ quotient form has an exact normal form.
Writing



$$
u=p_0-\pi^2p_2,\qquad v=p_2,
$$



there are $a>0$, $\eta\in\mathbb R$, and $\tau>0$ such that



$$
\boxed{\frac{Q_R(p_0,p_2)}a=(u+\eta v)^2+\tau v^2.}     \tag{3}
$$



Consequently, with $\varepsilon=\sqrt{\eta^2+\tau}$,



$$
\boxed{
 \left|\frac{\sqrt{Q_R(p_0,p_2)}}{\sqrt a\,|p_2|}
       -\left|\pi^2-\frac{p_0}{p_2}\right|\right|
 \leq\varepsilon\qquad(p_2\ne0).}                       \tag{4}
$$



Formula (4) is the precise small-eigenvector obstruction.  When the quotient
form collapses projectively to the evaluation functional, optimizing it over
primitive integer endpoints becomes, up to the additive floor
$\varepsilon$, the original problem of finding good rational
approximations to $\pi^2$.  Continued fractions give the generic relative
exponent $2$; no exponent strictly larger than $2$ follows from positive
definiteness or collapse alone.  Conversely, the abstract quadratic
optimization does not forbid a larger exponent: if $\pi^2$ has an
exceptional approximant and the collapse floor is smaller than its error,
the form can select it.  Thus there is an equivalence/circularity statement,
not an all-parameter impossibility theorem for $\pi^2$.

The finite saturated rows $n=5,8,10,12$ display extremely small collapse
floors.  This is strong finite evidence that the quotient is approaching
the evaluation functional, but no asymptotic bound for the floor is proved.
Nothing here classifies $e+\pi$.

## 2. Exact rational and complex-linear setup

Choose a rational basis $F_1,\ldots,F_t$ of $V_{\mathbb Q}$, and write



$$
F_x=\sum_{j=1}^t x_jF_j.         \tag{5}
$$



For $0\leq j<K$, the origin condition is



$$
F_x^{(j)}(0)=0.                 \tag{6}
$$



Every derivative in (6) is a complex-linear functional of $x$.  Since it
vanishes on the basis, it vanishes for every
$x\in\mathbb C^t$, not only for integral or rational $x$.  Hence



$$
H_x(z)=F_x(z)/z^K               \tag{7}
$$



is entire throughout the complex span.

Let $B\in\mathbb Q^{t\times2}$ encode the endpoint:



$$
E(F_x)=B^tx.                    \tag{8}
$$



Identity (1) is likewise complex-linear and therefore remains exact for
every complex $x$.  If $B$ has column rank two, rational Gaussian
elimination gives



$$
B^t\mathbb Q^t=\mathbb Q^2.     \tag{9}
$$



In particular, every primitive $p\in\mathbb Z^2$ has a rational global
representative.  If the endpoint rank is smaller, all statements below
remain valid for endpoints in the rational image; rank alone must not be
used to claim an endpoint outside that image.

For $R>\pi$, put



$$
A_{ij}(R)=\langle F_i/z^K,F_j/z^K\rangle_{2,R}.          \tag{10}
$$



Linear independence of the exponential polynomials makes $A(R)$ positive
definite.  The real endpoint fiber is a nonempty closed affine subspace, and
the unique minimum is



$$
x_*=A^{-1}B(B^tA^{-1}B)^{-1}p,                          \tag{11}
$$



with squared quotient norm



$$
\boxed{Q_R(p)=p^tC_Rp,\qquad
 C_R=(B^tA(R)^{-1}B)^{-1}\succ0.}                        \tag{12}
$$



The zero-factored Hardy estimate gives the rigorous endpoint bound



$$
\boxed{
 |p_0-p_2\pi^2|
 \leq\Gamma_R^{1/2}\sqrt{Q_R(p)},\qquad
 \Gamma_R={\pi^{2K}\over1-\pi^2/R^2}.}                 \tag{13}
$$



No coefficient-integrality hypothesis occurs in (10)--(13).

## 3. Why clearing denominators is unnecessary

The rational fiber in (8) has the form



$$
x_0+\ker(B^t),                  \tag{14}
$$



where $x_0$ and a basis of the kernel may be chosen over $\mathbb Q$.
Rational coordinates in that basis are dense in the real fiber.  Therefore,
for every $\delta>0$, there is $x_\delta\in\mathbb Q^t$ with



$$
B^tx_\delta=p,
 \qquad
 \|F_{x_\delta}/z^K\|_{2,R}
 <\sqrt{Q_R(p)}+\delta.                                  \tag{15}
$$



Both its endpoint and common zero are exact.  Applying Hardy to (15) and
letting $\delta\downarrow0$ is another proof of (13) which uses only
rational auxiliary coefficients.

The normalization used in the quotient--LP audit is $E(F)=p/H(p)$.
Nothing changes: the exact endpoint identity is then



$$
F(i\pi)={A_p(\pi)\over H(p)},    \tag{15a}
$$



and the analytic bound is directly a relative bound for
$|A_p(\pi)|/H(p)$.  Multiplying the final inequality by $H(p)$ restores
the primitive linear form.  It does not require clearing the coefficients
of $F$.

If $Lx_\delta$ is integral, then its endpoint is $Lp$.  Dividing the
endpoint back to the primitive vector $p$ divides the global function by
the same $L$ and returns $F_{x_\delta}$.  Charging $L$ while retaining
the primitive endpoint changes the normalization and is not required by the
analytic inequality.  Accordingly:

* an integral global representative with endpoint exactly $p$ is not
  needed;
* a uniform denominator bound for rational near-minimizers is not needed;
* denominator bounds can still be essential for arguments using global
  coefficient content, an integral determinant, or an integer shortest
  vector before the endpoint is formed.

This corrects the interpretation, not the exact computations, of the finite
clearing multipliers in the quotient--LP audit.  More explicitly, it
supersedes the claim that those multipliers prevent a rational or real
quotient minimizer from being an endpoint linear-form certificate.  They do
not prevent such a certificate in either the Hardy-$H^2$ route or the
coefficientwise weighted-$\ell^1$ Schwarz route: both analytic bounds are
homogeneous and valid for arbitrary complex coefficients.  The multipliers
remain relevant if a later argument imposes global integrality for a separate
arithmetic reason.

## 4. Conditional e-measure comparison

Assume temporarily that



$$
s=e+\pi
$$



is algebraic of degree $r$.  The explicit $e$-measure reduction recorded
in the Gaussian parity audit implies, for every fixed degree $d$ and every
fixed $\epsilon>0$, that all sufficiently large primitive
$A\in\mathbb Z[X]$ of degree $d$ satisfy



$$
|A(\pi)|>
 H(A)^{-(r^2d+r-1+\epsilon)}.                            \tag{16}
$$



This is the asymptotic form of the explicit norm-and-$e$-measure inequality;
the threshold is independent of any analytic representative of $A(\pi)$.
For (2), $d=2$, so



$$
|p_0-p_2\pi^2|>
 H(p)^{-(2r^2+r-1+\epsilon)}.                            \tag{17}
$$



Thus a rigorously proved sequence of real minimizers for which the right
side of (13) violates (17) is logically sufficient for a contradiction.
One does not need to exhibit rational coefficients.  This is an ordinary
existence theorem in a finite-dimensional real Hilbert space.

There is nevertheless a separate certification issue.  Decimal output from
a numerical minimizer does not prove a strict inequality.  A proof may use
directed interval bounds for (10)--(12), an analytic spectral estimate, or
one explicit rational point from (15) together with a rigorous tail bound.
The last option is constructive, but the denominator size affects only the
cost of displaying or checking that point, not the mathematical exponent in
(17).  Whenever the desired inequality has a strict gap, continuity ensures
that a sufficiently accurate rational point exists.

To exclude rational $s$, set $r=1$.  The absolute linear-form threshold
in (17) is $2$.  For approximants with
$H(p)\asymp|p_2|$, the corresponding relative rational-approximation
threshold is



$$
\left|\pi^2-{p_0\over p_2}\right|
 <|p_2|^{-3-\epsilon}.                                   \tag{18}
$$



The generic continued-fraction exponent $2$ is therefore one full power
short of the present rational-$s$ contradiction.  For general algebraic
degree $r$, the relative threshold is $2r^2+r$.

Finally, excluding one fixed degree $r$ is not by itself a transcendence
proof.  To prove $e+\pi$ transcendental by this route one must exclude every
algebraic degree (possibly with a construction depending on $r$).

## 5. Exact two-by-two quotient geometry

Write



$$
C_R=\begin{pmatrix}c_{00}&c_{02}\\c_{02}&c_{22}\end{pmatrix},
 \qquad \alpha=\pi^2,
 \qquad
 T=\begin{pmatrix}1&\alpha\\0&1\end{pmatrix}.           \tag{19}
$$



The change of coordinates



$$
\binom{p_0}{p_2}=T\binom uv,
 \qquad u=p_0-\alpha p_2,\quad v=p_2                     \tag{20}
$$



gives



$$
G=T^tC_RT=\begin{pmatrix}a&b\\b&d\end{pmatrix}\succ0. \tag{21}
$$



Set



$$
\eta={b\over a},
 \qquad
 \tau={\det G\over a^2}>0,
 \qquad
 \varepsilon=\sqrt{\eta^2+\tau}=\sqrt{d/a}.             \tag{22}
$$



In intrinsic quotient notation this last identity is



$$
\boxed{\varepsilon^2
 ={Q_R(\pi^2,1)\over Q_R(1,0)}.}                         \tag{22a}
$$



The numerator is the minimum norm for the real endpoint whose evaluation at
$i\pi$ is zero; the denominator is the minimum norm for the unit constant
endpoint.  Thus the collapse residual has a direct Hilbert-quotient meaning,
not merely a condition-number interpretation.

Completing the square proves (3).  The reverse triangle inequality in
$\mathbb R^2$, applied to



$$
{Q_R(p)\over a}
 =\|(u,0)+v(\eta,\sqrt\tau)\|_2^2,                      \tag{23}
$$



gives



$$
\boxed{\left|{\sqrt{Q_R(p)}\over\sqrt a}-|u|\right|
 \leq\varepsilon|v|.}                                   \tag{24}
$$



Division by $|v|$ proves (4).

For a sequence of forms, the following are equivalent:



$$
{C_R\over a}\longrightarrow
 \binom1{-\alpha}(1,-\alpha),
 \qquad
 {G\over a}\longrightarrow\begin{pmatrix}1&0\\0&0\end{pmatrix},
 \qquad
 \varepsilon\longrightarrow0.                          \tag{25}
$$



Indeed $d/a=\varepsilon^2$, positivity gives
$|b/a|\leq\sqrt{d/a}$, and (19)--(21) transport the rank-one limit.
Thus $\varepsilon$, rather than the condition number alone, is the exact
projective evaluation-collapse parameter.  A nearly singular form whose thin
direction is misaligned need not satisfy (25).

There is also an exact Hardy floor.  Minimizing (21) over $v$ at fixed
$u$ gives



$$
\min_v Q_R(u,v)={\det G\over d}u^2=:h_Ru^2.             \tag{26}
$$



Since (13) holds for every real endpoint,



$$
\boxed{h_R\geq\Gamma_R^{-1}
 ={1-\pi^2/R^2\over\pi^{2K}}.}                          \tag{27}
$$



Equivalently, $h_R^{-1}$ is the squared norm of evaluation restricted to
the global-image subspace, while $\Gamma_R$ is the full Hardy-space bound.

## 6. Primitive endpoints and the exact approximation equivalence

For $q\ne0$, define



$$
\Phi_R(p,q)={\sqrt{Q_R(p,q)}\over\sqrt a\,|q|}.         \tag{28}
$$



Both $\Phi_R(p,q)$ and the rational number $p/q$ are unchanged when
$(p,q)$ is divided by its gcd.  Thus restricting to primitive endpoints
loses nothing.  Define the best approximation function



$$
\delta_\alpha(X)=\min_{\substack{(p,q)\in\mathbb Z^2,
                       \gcd(p,q)=1\\1\leq|q|\leq X}}
                   \left|\alpha-{p\over q}\right|.      \tag{29}
$$



Taking minima in (4) gives the exact comparison



$$
\boxed{
 \left|
 \min_{\substack{(p,q)=1\\1\leq|q|\leq X}}\Phi_R(p,q)
 -\delta_{\pi^2}(X)
 \right|\leq\varepsilon.}                              \tag{30}
$$



More generally, for any sequence of primitive endpoints with
$|q_n|\to\infty$, if



$$
\varepsilon_n=O(|q_n|^{-\mu}), \tag{31}
$$



then



$$
\Phi_{R_n}(p_n,q_n)=O(|q_n|^{-\mu})
 \quad\Longleftrightarrow\quad
 \left|\pi^2-{p_n\over q_n}\right|=O(|q_n|^{-\mu}).    \tag{32}
$$



This proves the claimed circularity precisely.  A quotient exponent beyond
two can occur, but after (31) it is exactly an approximation exponent beyond
two for $\pi^2$, not a free consequence of the Hilbert-space minimization.

## 7. The small-eigenvector/Dirichlet balance

Let $p/q$ be a continued-fraction convergent of $\alpha=\pi^2$.  Then



$$
|p-\alpha q|<|q|^{-1}.                                  \tag{33}
$$



Equations (3) and (22) give the rigorous bound



$$
{Q_R(p,q)\over a}
 \leq2\left(q^{-2}+\varepsilon^2q^2\right).             \tag{34}
$$



The two terms balance at



$$
|q|\asymp\varepsilon^{-1/2}.    \tag{35}
$$



At that scale the rational error is generically
$q^{-2}\asymp\varepsilon$.  This is the exponent-two balance observed when
a thin ellipse aligned with $(\pi^2,1)$ selects ordinary convergents.  Large
continued-fraction gaps mean that a convergent need not occur at every
prescribed scale, so (35) is a balance law, not a uniform denominator theorem.

Conversely, (24) gives for every primitive endpoint



$$
\left|\pi^2-{p\over q}\right|
 \leq\Phi_R(p,q)+\varepsilon.                            \tag{36}
$$



Thus a shortest-vector theorem strong enough to beat exponent two, together
with a subordinate collapse floor, would itself prove a corresponding
exceptional rational approximation theorem for $\pi^2$.  Positive
definiteness alone cannot do this: there are badly approximable irrational
numbers for which exponent two is optimal.  Nor is there a universal upper
cap from quadratic optimization: any prescribed primitive vector can be made
the unique shortest direction of some positive definite form.

## 8. Finite quotient-collapse diagnostics

The deterministic replay reconstructs the saturated even endpoint images,
forms the stable post-zero Taylor Gram matrix, and evaluates (21)--(27) at
the radii selected by the finite Hardy endpoint diagnostics.  The following
numbers are high-precision stability diagnostics, not directed intervals:



$$
\begin{array}{c|c|c|c|c|c}
n&D&R&\eta&\tau&h_R/\Gamma_R^{-1}\\ \hline
5&4&4.4248958951&-2.32164\,10^{-7}&6.87745\,10^{-14}&1.96472\\
8&5&4.9608883116&-8.02602\,10^{-15}&3.21190\,10^{-28}&1.48784\\
10&5&5.4329404060&-1.80726\,10^{-16}&3.83247\,10^{-32}&1.76942\\
12&6&5.0420477449&-9.16276\,10^{-23}&4.33666\,10^{-44}&1.45428
\end{array}                                               \tag{37}
$$



For these rows the projective residuals



$$
\varepsilon^2={d\over a}=\eta^2+\tau                  \tag{38}
$$



are respectively



$$
1.2267445607\,10^{-13},\qquad
 3.8560670623\,10^{-28},\qquad
 7.0986650706\,10^{-32},\qquad
 5.1762264371\,10^{-44}.                                \tag{39}
$$



The $n=12,D=6$ replay first saturates the even reflection block, because
the complete minimal endpoint image also contains an odd block.  Its row is
recorded by the certificate together with (37)--(39).

The tiny values in (39) verify finite near-collapse, and the order-one ratios
in (37) show that restricted evaluation is within an order-one factor of the
full Hardy evaluation bound.  The rows are not monotone evidence for a
specific asymptotic rate, and they do not prove $\varepsilon_n\to0$.

## 9. Replay and logical status

The package consists of:

* `sources/root_unity_hardy_endpoint_quotient_geometry_correction.md`;
* `scripts/root_unity_hardy_endpoint_quotient_geometry_certificate.py`;
* `results/root_unity_hardy_endpoint_quotient_geometry_certificate.json`;
* `results/root_unity_hardy_endpoint_quotient_geometry_hashes.sha256`.

Replay from the archive root with

    python3 scripts/root_unity_hardy_endpoint_quotient_geometry_certificate.py

The exact results are the denominator-free endpoint theorem, formulas
(3)--(4), the collapse criterion (25), the Hardy floor (27), the primitive
approximation equivalence (30), and the balance inequalities (34), (36).
The decimal table is finite evidence only.  The package proves neither an
asymptotic collapse rate nor an approximation exponent beyond two, and it
does not classify $e+\pi$.
