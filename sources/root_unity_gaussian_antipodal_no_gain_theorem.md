> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Antipodal no-gain for Gaussian parity mixing

## Exact whole-circle supremum domination and Hardy--$H^2$ orthogonality

Checked: 2026-08-27 UTC

## 1. Scope and theorem

The intrinsically saturated $k=2$ global image splits into centered
reflection eigenspaces.  Write their analytic functions as



$$
F_+(-z)=F_+(z),\qquad
                         F_-(-z)=-F_-(z),                 \tag{1}
$$



and form the Gaussian phase-aligned mix



$$
F(z)=F_+(z)-iF_-(z).             \tag{2}
$$



The coefficientwise no-gain theorem in
`sources/root_unity_gaussian_global_saturation_no_gain.md` left open the
possibility that exact interference among distinct reflected pairs might
make the whole-function circle maximum much smaller after mixing.  The
antipodal identity closes that caveat completely.

> **Theorem 1.1 (antipodal Gaussian no-gain).**  Let $F_+$ and $F_-$
> satisfy (1), and suppose both are divisible by $z^K$.  Put
>
> 

$$
> U=F_+/z^K,\qquad V=F_-/z^K,\qquad W=F/z^K.
>
$$


>
> Then, for every $R>0$,
>
> 

$$
> \boxed{
> \lVert W\rVert_{\infty,R}
> \geq\max\{\lVert U\rVert_{\infty,R},
>             \lVert V\rVert_{\infty,R}\},}             \tag{3}
>
$$


>
> and
>
> 

$$
> \boxed{
> \lVert W\rVert_{2,R}^2
> =\lVert U\rVert_{2,R}^2+
>  \lVert V\rVert_{2,R}^2.}                              \tag{4}
>
$$


>
> These statements remain true whether $K$ is even or odd.

For the root-unity Wronskian image, one may take the universal common order



$$
K_0=2m(n+1),                     \tag{5}
$$



which is even.  More sharply, if the nonzero component orders are
$K_+$ and $K_-$, the joint order is $K=\min(K_+,K_-)$; applying
Theorem 1.1 with this actual joint order gives a circle bound no smaller
than either component's individually factored bound.

Combining (3)--(4) with the exact arithmetic facts



$$
c=\gcd(c_+,c_-),\qquad H\geq\max\{H_+,H_-\},\qquad
 d\geq\max\{d_+,d_-\}.                                    \tag{6}
$$



extends the Gaussian no-gain margin theorem from coefficientwise majorants
to both:

1. the **exact whole-function circle supremum**, with all interference among
   all frequency-polynomial terms retained; and
2. the exact Hardy--$H^2$ circle norm.

Thus cross-parity Gaussian mixing cannot improve either optimized analytic
margin beyond either of its nonzero components.  Allowing a zero block, the
supremum over all mixes equals the better of the two separate parity
suprema.

This result does not bound successive minima inside one parity block, does
not control denominators of continuous Hardy optimizers, and does not rule
out an unusually small exact endpoint value.  It gives no classification of
$e+\pi$.

## 2. Reflection and the common-zero parity shift

For a centered coefficient array $x=(x_{r,a})$, let



$$
F_x(z)=\sum_{r=-m}^m\sum_a x_{r,a}z^ae^{rz}.             \tag{7}
$$



The signed reflection involution is



$$
(Jx)_{r,a}=(-1)^a x_{-r,a}.      \tag{8}
$$



Changing $z$ to $-z$ in (7) gives



$$
F_x(-z)=F_{Jx}(z).               \tag{9}
$$



Consequently the $+1$ and $-1$ eigenspaces of $J$ give exactly the
even and odd functions in (1).

If $F_\epsilon(-z)=\epsilon F_\epsilon(z)$ and
$H_\epsilon=F_\epsilon/z^K$, then



$$
H_\epsilon(-z)=\epsilon(-1)^K H_\epsilon(z).            \tag{10}
$$



Both eigenvalues acquire the same factor $(-1)^K$.  Their signs therefore
remain opposite.  When $K$ is odd, the even and odd labels swap after
division, but the two Taylor supports are still disjoint.  This resolves the
parity-shift issue without assuming that the common order is even.

For a nonzero even analytic function, the origin order is even; for a
nonzero odd analytic function, it is odd.  Hence $K_+\neq K_-$, and the
two lowest Taylor terms in (2) cannot cancel.  Therefore



$$
\operatorname {ord}_0F
 =\min(K_+,K_-).                                         \tag{11}
$$



The universal root-unity lower order (5) is sufficient for all estimates,
while (11) permits the sharper component comparison in Section 5.

## 3. The antipodal parallelogram identity

For arbitrary complex numbers $u,v$, the parallelogram identity gives



$$
|u-iv|^2+|u+iv|^2=2(|u|^2+|v|^2).                      \tag{12}
$$



Let



$$
\sigma=(-1)^K.
$$



Equation (10) gives



$$
U(-z)=\sigma U(z),\qquad V(-z)=-\sigma V(z),            \tag{13}
$$



and hence



$$
W(z)=U(z)-iV(z),\qquad
 W(-z)=\sigma\{U(z)+iV(z)\}.                             \tag{14}
$$



Substituting (14) into (12) proves the exact pointwise identity



$$
\boxed{
 |W(z)|^2+|W(-z)|^2
 =2\{|U(z)|^2+|V(z)|^2\}.}                              \tag{15}
$$



Both $z$ and $-z$ lie on the same centered circle.  Therefore



$$
\begin{aligned}
 \lVert W\rVert_{\infty,R}^2
 &\geq\frac{|W(z)|^2+|W(-z)|^2}{2}\\
 &=|U(z)|^2+|V(z)|^2
 \geq\max\{|U(z)|^2,|V(z)|^2\}.                         \tag{16}
 \end{aligned}
$$



Taking the appropriate suprema proves (3).  Notice that no triangle
inequality and no coefficientwise absolute-value majorant appears in this
argument.  Every cancellation inside $F_+$, inside $F_-$, and among
their frequency-polynomial terms is retained.

Integrating (15) over a full circle and using invariance of normalized arc
measure under $z\mapsto-z$ gives (4).  Equivalently, the Taylor supports
of $U$ and $V$ have opposite parity, so



$$
\langle U,V\rangle_R=0.          \tag{17}
$$



The phase factor $-i$ does not change the norm.

## 4. Exact supremum and Hardy evaluation bounds

If an analytic function $G$ has origin order at least $L$, the exact
whole-circle Schwarz bound is



$$
|G(i\pi)|
 \leq\left(\frac\pi R\right)^L
       \lVert G\rVert_{\infty,R}
 =\pi^L\lVert G/z^L\rVert_{\infty,R},\qquad R>\pi.       \tag{18}
$$



For endpoint content $c_G$, define the corresponding primitive upper
bound



$$
\mathcal S_R(G;L,c_G)
 =\frac{\pi^L}{c_G}\lVert G/z^L\rVert_{\infty,R}.        \tag{19}
$$



With normalized boundary $H^2$ norm, the exact Hardy evaluation bound is



$$
\mathcal H_R(G;L,c_G)
 =\frac{\pi^L}
 {c_G\sqrt{1-\pi^2/R^2}}
 \lVert G/z^L\rVert_{2,R}.                               \tag{20}
$$



Equation (20) is proved independently in
`sources/root_unity_hardy_h2_saturated_circle_audit.md`.  The present
orthogonality theorem applies to the exact infinite norm, not to a truncated
Taylor calculation.

## 5. Unequal actual origin orders strengthen the comparison

Put



$$
L=\min(K_+,K_-),\qquad \delta_\epsilon=K_\epsilon-L,
 \qquad G_\epsilon=F_\epsilon/z^{K_\epsilon}.             \tag{21}
$$



On $|z|=R$,



$$
\lVert F_\epsilon/z^L\rVert_{*,R}
 =R^{\delta_\epsilon}\lVert G_\epsilon\rVert_{*,R},     \tag{22}
$$



where $*$ may be either $\infty$ or $2$.  From (3) or (4),



$$
\begin{aligned}
 {\pi^L\over c}\lVert F/z^L\rVert_{*,R}
 &\geq {\pi^LR^{\delta_\epsilon}\over c}
        \lVert G_\epsilon\rVert_{*,R}\\
 &=\left({R\over\pi}\right)^{\delta_\epsilon}
   {\pi^{K_\epsilon}\over c}
        \lVert G_\epsilon\rVert_{*,R}\\
 &\geq {\pi^{K_\epsilon}\over c_\epsilon}
        \lVert G_\epsilon\rVert_{*,R}.                  \tag{23}
 \end{aligned}
$$



The last inequality uses $R>\pi$, $\delta_\epsilon\geq0$, and
$c\leq c_\epsilon$.  Multiplying every line by the common Hardy kernel
factor $(1-\pi^2/R^2)^{-1/2}$ proves the identical comparison for (20).

Thus using the joint, possibly smaller origin order never creates an
advantage.  The component having extra origin zeros contributes the factor
$(R/\pi)^{\delta_\epsilon}\geq1$, so unequal orders only strengthen its
domination by the mixed bound.

Pointwise in $R$, (23) gives



$$
\begin{aligned}
 \mathcal S_R(F;L,c)&\geq
    \mathcal S_R(F_\epsilon;K_\epsilon,c_\epsilon),\\
 \mathcal H_R(F;L,c)&\geq
    \mathcal H_R(F_\epsilon;K_\epsilon,c_\epsilon).     \tag{24}
 \end{aligned}
$$



Taking infima over $R>\pi$ preserves both inequalities.

## 6. Arithmetic normalization and the no-gain margin

Let the nonzero component endpoint contents be $c_+,c_-$.  Their even and
odd coefficient supports are disjoint after phase alignment.  As proved in
the Gaussian saturation audit,



$$
c=\gcd(c_+,c_-).                 \tag{25}
$$



After separate and joint primitive normalization, the joint height and
actual degree satisfy (6).  If one component has zero endpoint, deleting it
preserves the endpoint and weakly improves both exact circle norms, so no
optimizer needs such an endpoint-kernel component.

Under the temporary algebraicity hypothesis



$$
r=[\mathbb Q(e+\pi):\mathbb Q],
$$



the fixed-degree absolute measure cost is



$$
\kappa_r(d)=r^2d+r-1.            \tag{26}
$$



For $\mathcal A\in\{\mathcal S,\mathcal H\}$, define



$$
\mathfrak M_r^{\mathcal A}(F)
 =-\log\inf_{R>\pi}\mathcal A_R(F)
  -\kappa_r(d)\log H.                                    \tag{27}
$$



Equations (6), (24), and monotonicity of $\kappa_r$ give, for each nonzero
component,



$$
\boxed{
 \mathfrak M_r^{\mathcal A}(F_+-iF_-)
 \leq\mathfrak M_r^{\mathcal A}(F_+),\qquad
 \mathfrak M_r^{\mathcal A}(F_+-iF_-)
 \leq\mathfrak M_r^{\mathcal A}(-iF_-).}                \tag{28}
$$



Allowing either block to vanish therefore gives



$$
\boxed{
 \sup_{F_+,F_-}\mathfrak M_r^{\mathcal A}(F_+-iF_-)
 =\max\left\{
       \sup_{F_+}\mathfrak M_r^{\mathcal A}(F_+),
       \sup_{F_-}\mathfrak M_r^{\mathcal A}(-iF_-)
      \right\}.}                                         \tag{29}
$$



This is an all-parameter theorem.  It is stronger than the earlier
coefficientwise result with respect to cross-parity interference: even an
exact optimizer for the whole-function circle supremum or Hardy norm cannot
extract an incremental gain from mixing the two reflection blocks.

## 7. Exact saturated anchor

The replay reconstructs one actual row



$$
(m,n,D,d)=(2,4,4,2).             \tag{30}
$$



The saturated reflection-even and reflection-odd ranks are $3$ and $1$.
For their first saturated basis rows, every centered reflection coefficient
identity is checked exactly, and the actual origin orders are



$$
K_+=20,\qquad K_-=21,
 \qquad L=20.                                             \tag{31}
$$



Thus the anchor directly exercises the unequal-order case.  After division
by $z^{20}$, the replay checks $80$ exact Taylor coefficients: the two
supports are opposite, every cross product vanishes, and the truncated
Hardy norm identity is an exact polynomial identity in $R^2$.  The
coefficient reflection law proves the same support statement for all Taylor
orders.

The retained endpoint vectors before the harmless signed phase rotation are



$$
\begin{aligned}
 p_+&=(165869273088,0,16807710600),\\
 p_-&=(0,-6912,0).                                       \tag{32}
 \end{aligned}
$$



Their contents are



$$
c_+=72,\qquad c_-=6912,
 \qquad c=72.                                             \tag{33}
$$



The separate primitive heights are $2303739904$ and $1$; the joint
primitive height is $2303739904$.  The separate actual degrees are $2$
and $1$, while the joint degree is $2$.  Thus the gcd, height, and degree
relations used in Section 6 all hold exactly on the anchor.

For a concrete unequal-order comparison, take $R=4$.  The elementary
bound $\pi<22/7$ gives



$$
{R\over\pi}>{4\over22/7}
                         ={14\over11}>1.                 \tag{34}
$$



This is the extra factor in (23) for the odd component.

## 8. Logical scope

The theorem removes one specific possible escape from the Gaussian
parity-mixing barrier: cancellation between the two reflection eigenspaces
cannot improve an exact whole-circle supremum or exact Hardy norm.

It does **not** prove any of the following:

1. a lower bound for a successive minimum inside either separately
   saturated parity lattice;
2. a denominator or integral-content bound for a rational Hardy optimizer;
3. absence of cancellation in the numerical endpoint value $A(\pi)$;
4. an asymptotic height theorem for the surviving single-parity problem; or
5. irrationality, algebraicity, or transcendence of $e+\pi$.

## 9. Replay and files

The package consists of:

* `sources/root_unity_gaussian_antipodal_no_gain_theorem.md`;
* `scripts/root_unity_gaussian_antipodal_no_gain_certificate.py`;
* `results/root_unity_gaussian_antipodal_no_gain_certificate.json`; and
* `results/root_unity_gaussian_antipodal_no_gain_hashes.sha256`.

Replay from the archive root with

    python3 scripts/root_unity_gaussian_antipodal_no_gain_certificate.py

The script verifies the frozen Gaussian global-saturation dependency before
import.  It checks (12) symbolically for general complex scalars, verifies
the parity shift for common orders $0,\ldots,7$, reconstructs the exact
saturated anchor (30), verifies reflection and actual origin orders, checks
the Taylor-support and finite norm identities, and audits endpoint content,
height, and degree over $\mathbb Z$.  Resource measurements are omitted
from the deterministic JSON, and the replay asserts a 2 GiB RSS ceiling.
