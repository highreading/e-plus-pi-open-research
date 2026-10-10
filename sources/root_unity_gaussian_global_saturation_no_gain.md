> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Gaussian phase alignment inside the saturated $k=2$ global image

## Fixed-locus saturation, $2$-primary unphased glue, and an exact coefficientwise no-gain theorem

Checked: 2026-08-27 UTC

## 1. Verdict

The intrinsically saturated global Wronskian lattice from
sources/root_unity_k2_global_image_saturation_audit.md becomes much
shorter than its raw exterior-coordinate presentation. It is therefore
natural to ask whether combining its even- and odd-output components over
$\mathbb Z[i]$ creates a second saturation gain before evaluating at
$z=i\pi$.

There is a tempting gain in the **unphased** global image. If
$S_+$ and $S_-$ are the separately saturated centered-reflection
eigenlattices and



$$
S_0=(V_+\oplus V_-)\cap\mathbb Z^P,                       \tag{1}
$$



then



$$
S_++S_-\subseteq S_0,\qquad
 2S_0\subseteq S_++S_-.                                   \tag{2}
$$



Thus the quotient in (2) is $2$-elementary. On the exact grid below its
index is $2,4,8$, or $16$.

That glue cannot be used by a Gaussian endpoint aligned to an integer
polynomial $A(\pi)$. Let $J$ be the integral signed reflection on
centered global coefficients, let



$$
S_{\mathbb G}
 =\bigl((V_+\oplus V_-)\otimes_{\mathbb Q}\mathbb Q(i)\bigr)
   \cap\mathbb Z[i]^P,                                    \tag{3}
$$



and let $\sigma(w)=J\overline w$. The exact fixed-lattice identity is



$$
\boxed{S_{\mathbb G}^{\sigma=1}=S_+\oplus iS_-.}          \tag{4}
$$



The right side is already intrinsically saturated in the real-doubled
integer lattice. In particular, no cross-parity $1+i$ divisor survives
phase alignment.

There is also an exact analytic obstruction. For $u\in S_+$ and
$v\in S_-$, phase-align



$$
w=u-iv.                           \tag{5}
$$



At every centered circle radius $R$, the exact coefficientwise
majorant for $w$ is no smaller than the corresponding majorant for
either nonzero component. The joint endpoint content is the gcd of the
two component contents, while its primitive height and degree are no
smaller. Consequently, for the leading fixed-degree $e$-measure
exponent



$$
\kappa_r(d)=r^2d+r-1,             \tag{6}
$$



the optimized coefficientwise Schwarz margin of a genuine mix is no
larger than the margin of either component. Allowing one block to vanish,



$$
\boxed{
 \sup_{u,v}\mathfrak M_r(u-iv)
 =\max\left\{
       \sup_u\mathfrak M_r(u),\
       \sup_v\mathfrak M_r(-iv)
      \right\}.}                                           \tag{7}
$$



Thus joint Gaussian saturation gives exactly zero incremental gain for
the rigorous absolute-coefficient majorants (29)--(32), even after adding
the exact reflected-pair supremum (32a)--(32b). It neither lowers the
unchanged strict relative threshold $r^2d+r$ nor moves that
coefficientwise construction beyond the generic Dirichlet boundary.

This does **not** rule out an exceptionally short or high-content vector
inside one separately saturated parity component. No all-parameter bound
for those successive minima is proved. The result isolates the remaining
survivor rather than classifying $e+\pi$.

The deterministic replay files are

* scripts/root_unity_gaussian_global_saturation_certificate.py;
* results/root_unity_gaussian_global_saturation_certificate.json.

## 2. Parity-split global image spaces

Use a full endpoint space



$$
E=\mathbb Q[z]_{\le D},\qquad \nu=D+1.                    \tag{8}
$$



Let $G$ be the complete cleared $k=2$ Wronskian coefficient map from
exterior coordinates to



$$
\mathbb Z^P,\qquad P=(2m+1)(2n+1),                        \tag{9}
$$



and let $T_{>d}$ be the corrected endpoint-tail map. The exterior
coordinates split according to the parity of $a+b-1$. Write



$$
G_\epsilon,\ T_{\epsilon,>d},\qquad \epsilon\in\{+1,-1\},\tag{10}
$$



for the even-output and odd-output blocks, respectively. Define their
rational valid global spaces by



$$
V_\epsilon
 =G_\epsilon\bigl(\ker_{\mathbb Q}T_{\epsilon,>d}\bigr)
 \subseteq\mathbb Q^P                                    \tag{11}
$$



and their intrinsic integer saturations by



$$
S_\epsilon=V_\epsilon\cap\mathbb Z^P.
                                                                    \tag{12}
$$



Every vector in (12) is a complete integer-coefficient exponential
polynomial with a rational tail-kernel preimage. Endpoint evaluation is
integral and has no coefficient above degree $d$.

Center frequencies $0,\ldots,2m$ to $-m,\ldots,m$. For a coefficient
array $x=(x_{r,k})$, define



$$
(Jx)_{r,k}=(-1)^kx_{-r,k}.         \tag{13}
$$



This is an integral involution. The exact reflection law for centered
Wronskians gives



$$
Jx=\epsilon x\qquad(x\in V_\epsilon).
                                                                    \tag{14}
$$



Hence $V_+\cap V_-=0$, and all the sums below are direct over
$\mathbb Q$.

## 3. Intrinsic Gaussian saturation

### 3.1 The unphased quotient is killed by two

Put $V=V_+\oplus V_-$ and $S_0=V\cap\mathbb Z^P$. For $x\in S_0$,



$$
x_+=x+Jx\in S_+,\qquad x_-=x-Jx\in S_-,                 \tag{15}
$$



and



$$
2x=x_++x_-.                      \tag{16}
$$



This proves (2). Equivalently, every Smith invariant of
$S_++S_-$ inside $S_0$ is $1$ or $2$. The corresponding index is
a power of two. This is an all-parameter statement; it does not require a
formula for the dimensions of the two blocks.

The factor in (2) is the familiar failure of integral eigenspace
projections:



$$
P_\pm={1\over2}(I\pm J).           \tag{17}
$$



An integral unphased vector can have half-integral parity projections.

### 3.2 Phase alignment is an anti-linear fixed locus

Complexify $V$ and take its intrinsic Gaussian lattice as in (3).
Every $w\in S_{\mathbb G}$ has a unique representation



$$
w=a+ib,\qquad a,b\in\mathbb Z^P.  \tag{18}
$$



Because $V$ is rational, membership in
$V\otimes\mathbb Q(i)$ is equivalent to $a,b\in V$. The fixed
condition for $\sigma(w)=J\overline w$ is



$$
Ja=a,\qquad Jb=-b.                                      \tag{19}
$$



Thus $a\in S_+$ and $b\in S_-$, proving (4). Conversely, every
$a+ib$ with $a\in S_+$, $b\in S_-$ plainly satisfies (19).
The fixed locus is a $\mathbb Z$-lattice, not a
$\mathbb Z[i]$-submodule: multiplication by $i$ changes the
anti-linear fixed condition. It is precisely this real-rank lattice that
has endpoint value $A(\pi)$.

This proof also establishes intrinsic saturation. Under the real-doubled
embedding



$$
\mathbb Z[i]^P\longrightarrow\mathbb Z^{2P},\qquad
 a+ib\longmapsto(a,b),                                    \tag{20}
$$



the aligned lattice is exactly the block direct sum of the two saturated
lattices. Therefore



$$
\bigl((V_+\times V_-)\cap\mathbb Z^{2P}\bigr)
 =S_+\times S_-.                                         \tag{21}
$$



Its saturation index is one.

The extra vectors in (2) belong to the full unphased or unrestricted
Gaussian saturation, but their eigenspace projections contain halves.
There is a useful projective check that endpoint-content normalization
does not recover a hidden gain. If $x\in S_0$, put



$$
u={x+Jx\over2},\qquad v={x-Jx\over2},\qquad w=u-iv.       \tag{21a}
$$



The desired $w$ can be half-integral. Multiplication by $1+i$ gives



$$
(1+i)w=x+iJx\in\mathbb Z[i]^P,                           \tag{21b}
$$



but its endpoint has the same factor $1+i$. On the other hand,



$$
2w=(x+Jx)-i(x-Jx)\in S_+\oplus iS_-                     \tag{21c}
$$



and its endpoint has the factor $2$. Dividing by the respective
Gaussian endpoint contents in (21b) and (21c) produces the same primitive
analytic form $w$, up to a unit. Every homogeneous coefficientwise
circle bound is consequently identical after primitive normalization.
Thus the $2$-primary glue is arithmetically real, but it supplies only
an alternative cleared presentation and no endpoint-height or circle-bound
gain for this strategy.

For completeness, if ${\cal E}_k$ extracts the degree-$k$ endpoint
coefficient, then (13) gives



$$
{\cal E}_k(Jx)=(-1)^k{\cal E}_k(x).   \tag{21d}
$$



Hence the even endpoint coefficients of $u$ and the odd endpoint
coefficients of $v$ are the corresponding integral coefficients of
$x$, despite the possible global halves in (21a). If their common
ordinary content is $c$, the endpoint contents in (21b) and (21c) are
exactly $(1+i)c$ and $2c$, respectively. This proves the primitive
normalization assertion rather than merely comparing its absolute scale.

## 4. Endpoint phase, content, and height

Let ${\cal E}$ denote endpoint evaluation at $e^{i\pi}=-1$. For
$u\in S_+$ and $v\in S_-$, write



$$
\begin{aligned}
 {\cal E}(u)&=\sum_{j\ {\rm even}}n_jz^j,\\
 {\cal E}(v)&=\sum_{j\ {\rm odd}}n_jz^j.
 \end{aligned}                                             \tag{22}
$$



For $w=u-iv$, define



$$
A(X)=\sum_{j=0}^{d}(-1)^{\lfloor j/2\rfloor}n_jX^j.      \tag{23}
$$



Then



$$
{\cal E}(w)(z)=A(-iz),\qquad
                         {\cal E}(w)(i\pi)=A(\pi).          \tag{24}
$$



Let $c_+$ and $c_-$ be the contents of the two nonzero component
endpoint vectors. Since their coefficient supports are disjoint, the
joint Gaussian content is exactly



$$
c=\gcd(c_+,c_-).                  \tag{25}
$$



If $H_+$ and $H_-$ are the heights after separate primitive
normalization, and $H$ is the joint primitive height, then



$$
H\ge H_+,\qquad H\ge H_-.         \tag{26}
$$



Likewise, if $d,d_+,d_-$ are the actual degrees,



$$
d\ge d_+,\qquad d\ge d_-.         \tag{27}
$$



If one component has zero endpoint, deleting it preserves the endpoint
and can only improve every coefficientwise bound considered below.
Therefore no optimizer needs a nonzero endpoint-kernel component.

## 5. Exact coefficientwise centered bounds

Let $R>0$, and put



$$
H_+(t)=\cosh t,\qquad H_-(t)=\sinh t.                    \tag{28}
$$



For $x\in S_\epsilon$, reflection pairs its positive and negative
frequencies. The exact coefficientwise hyperbolic majorant is



$$
\begin{aligned}
 {\cal B}_\epsilon(x;R)
 ={}&
 \sum_{\substack{0\le k\le2n\\ {(-1)^k=\epsilon}}}
       |x_{0,k}|R^k\\
 &+2\sum_{r=1}^{m}\sum_{k=0}^{2n}
       |x_{r,k}|R^kH_{\epsilon(-1)^k}(rR).
\end{aligned}                                             \tag{29}
$$



This is equation (31) of
sources/root_unity_centered_exterior_reflection_reciprocity.md, applied
to the intrinsically saturated vector rather than to a raw exterior
coordinate vector.

For the phase-aligned mix $w=u-iv$, two coefficientwise bounds are
available.

First, separate the reflection eigenspaces:



$$
{\cal B}_{\rm sep}(u,v;R)
 ={\cal B}_+(u;R)+{\cal B}_-(v;R).                        \tag{30}
$$



Second, use the Gaussian modulus of every centered coefficient directly:



$$
\begin{aligned}
 {\cal B}_{\mathbb G}(u,v;R)
 ={}&
 \sum_{k=0}^{2n}\sqrt{u_{0,k}^2+v_{0,k}^2}\,R^k\\
 &+2\sum_{r=1}^{m}\sum_{k=0}^{2n}
 \sqrt{u_{r,k}^2+v_{r,k}^2}\,R^ke^{rR}.
\end{aligned}                                             \tag{31}
$$



The negative-frequency coefficient is the signed conjugate of the
positive-frequency coefficient, so the two moduli in each pair agree.
Take the better valid bound



$$
{\cal B}_{\rm mix}(u,v;R)
 =\min\{{\cal B}_{\rm sep}(u,v;R),
         {\cal B}_{\mathbb G}(u,v;R)\}.                   \tag{32}
$$



One can strengthen the audit to the exact supremum of each individual
reflected Gaussian pair. For $r>0$, put



$$
\begin{aligned}
 {\cal P}_{r,k}(u,v;R)
 =R^k\max_{|\zeta|=R}\bigl|
 &(u_{r,k}-iv_{r,k})e^{r\zeta}\\
 &+(-1)^k(u_{r,k}+iv_{r,k})e^{-r\zeta}
 \bigr|,                                                   \tag{32a}\\
 {\cal B}_{\rm pair}(u,v;R)
 ={}&\sum_{k=0}^{2n}|u_{0,k}-iv_{0,k}|R^k
     +\sum_{r=1}^m\sum_{k=0}^{2n}{\cal P}_{r,k}(u,v;R).
                                                               \tag{32b}
\end{aligned}
$$



This takes the exact circle supremum before applying the triangle
inequality between distinct coefficient pairs. At the single real point
$\zeta=R$, its paired modulus is



$$
2R^k
 \begin{cases}
 \sqrt{u_{r,k}^2\cosh^2(rR)+v_{r,k}^2\sinh^2(rR)},
       &k\ {\rm even},\\
 \sqrt{u_{r,k}^2\sinh^2(rR)+v_{r,k}^2\cosh^2(rR)},
       &k\ {\rm odd}.
 \end{cases}                                               \tag{32c}
$$



It therefore dominates both component pair terms. At $r=0$, the two
component supports are disjoint by (14), so (32b) again agrees termwise
with the appropriate component. Consequently



$$
\min\{{\cal B}_{\rm mix},{\cal B}_{\rm pair}\}
 \ge\max\{{\cal B}_+,{\cal B}_-\}.                         \tag{32d}
$$



Both alternatives dominate each component. For (30) this is immediate.
For (31), use



$$
\sqrt{a^2+b^2}\ge|a|,\ |b|,
 \qquad e^{rR}\ge\cosh(rR),\ \sinh(rR).                   \tag{33}
$$



Therefore, pointwise for every $R>0$,



$$
\boxed{
 {\cal B}_{\rm mix}(u,v;R)
 \ge\max\{{\cal B}_+(u;R),{\cal B}_-(v;R)\}.}             \tag{34}
$$



Equation (32d) shows that (34), and hence the no-gain theorem below,
remains valid when the exact per-pair bound (32b) is also admitted. The
finite replay reports the two closed-form bounds (30)--(31); no numerical
maximization in $\zeta$ is needed for the all-parameter conclusion.

### 5.1 Exact radius optimization

In the full endpoint space every remainder has origin order at least



$$
M=m(n+1),                         \tag{35}
$$



so every saturated global $k=2$ vector has origin order at least $2M$.
For endpoint content $c$, Schwarz's lemma and either bound above give



$$
U_R(w)
 ={ {\cal B}_{\rm mix}(u,v;R)\over c}
  \left({\pi\over R}\right)^{2M},
 \qquad R\ge\pi,                                          \tag{36}
$$



as an upper bound for the primitive endpoint modulus.

Each summand of (29)--(31), after writing $R=e^t$, has a convex
logarithm. For example,



$$
{d\over dt}\log\{R^k\cosh(rR)\}
 =k+rR\tanh(rR),                                         \tag{37}
$$



with analogous formulas $k+rR\coth(rR)$ and $k+rR$ for the
$\sinh$ and exponential terms. Log-sum-exp preserves convexity.
Consequently each separate logarithmic Schwarz bound is convex in $t$,
and its interior optimum is the unique solution of



$$
{d\over d\log R}\log{\cal B}(R)=2M.                      \tag{38}
$$



The replay solves (38) by high-precision monotone bisection. Since (32)
is the minimum of two valid bounds,



$$
\inf_R\min(U_{\rm sep}(R),U_{\mathbb G}(R))
 =\min\{\inf_RU_{\rm sep}(R),\inf_RU_{\mathbb G}(R)\}.     \tag{39}
$$



Thus no radius grid or local nonlinear optimizer is hidden in the
reported diagnostics.

## 6. Exact no-gain comparison with the $e$-measure

Under the temporary algebraicity hypothesis



$$
r=[\mathbb Q(e+\pi):\mathbb Q],   \tag{40}
$$



the preceding Gaussian phase audit proves that a primitive actual
degree-$d$ endpoint has leading absolute measure cost



$$
\kappa_r(d)=r^2d+r-1              \tag{41}
$$



and strict relative threshold $r^2d+r$.

Define the optimized leading margin



$$
\mathfrak M_r(w)
 =-\log\inf_{R\ge\pi}U_R(w)-\kappa_r(d)\log H.             \tag{42}
$$



For a nonzero even component, (25), (34), and (36) give



$$
\inf_RU_R(u-iv)
 \ge\inf_R
 \left\{
 { {\cal B}_+(u;R)\over c_+}
 \left({\pi\over R}\right)^{2M}
 \right\}.                                                 \tag{43}
$$



Equations (26)--(27) and monotonicity of $\kappa_r(d)$ then imply



$$
\mathfrak M_r(u-iv)\le\mathfrak M_r(u). \tag{44}
$$



The identical argument gives



$$
\mathfrak M_r(u-iv)\le\mathfrak M_r(-iv). \tag{45}
$$



Equations (44)--(45) prove (7). This is stronger than saying that the
measure exponent remains unchanged: for the absolute-coefficient
majorants (29)--(32b), a genuine Gaussian mix cannot even improve the
best separately saturated component at finite parameters.

The result is deliberately limited to the displayed absolute-coefficient
Schwarz majorants, including exact interference only within each single
reflected pair. A sharper whole-polynomial circle estimate exploiting
interference between distinct pairs, or an exact cancellation in the
numerical endpoint value $A(\pi)$, is not excluded. Nor is an
exceptional short vector inside $S_+$ or $S_-$.

At the dimension-counting level, phase alignment still combines the two
endpoint ranks into at most $d+1$ integer coefficients. As proved in
sources/root_unity_gaussian_parity_mixing_barrier.md, this restores only
the generic relative Dirichlet exponent $d+1$: it meets the
$r=1$ threshold without the strict gain required, and is below the
threshold for $r>1$. Intrinsic global saturation changes constants and
can change the scale of individual vectors, but the joint operation adds
no new aligned lattice direction or coefficientwise gain.

## 7. Exact representative replay

The replay takes



$$
m\in\{2,3\},\qquad n\in\{4,5,6\},\qquad D=n,\qquad
 d\in\{2,3\}.                                             \tag{46}
$$



The choice $D=n$, rather than the minimal total exterior dimension, is
intentional: both parity tail spaces are then nonzero.

The exact saturated global ranks 

$$
(\operatorname {rank}S_+,
\operatorname {rank}S_-)
$$

 and unphased glue indices are



$$
\begin{array}{c|c|ccc}
d&m&n=4&n=5&n=6\\ \hline
2&2&(3,1;2)&(4,2;4)&(5,3;8)\\
2&3&(3,1;2)&(5,2;4)&(6,4;16)\\
3&2&(3,2;4)&(4,3;4)&(5,4;8)\\
3&3&(3,2;2)&(5,3;8)&(6,5;16)
\end{array}                                               \tag{47}
$$



Here $(a,b;I)$ means ranks $a,b$ and index
$I=[S_0:S_++S_-]$. Every quotient Smith invariant is exactly $1$ or
$2$. In contrast, the real-doubled aligned lattice has saturation index
one on every row, verifying (4) directly.

For each parity component, the replay enumerates the coefficient box
$\{-1,0,1\}$ in a saturated LLL basis, removes any global scalar content
intrinsically, and optimizes (29), (36), and (38) for every nonzero
endpoint candidate. This is a complete search only in that displayed
basis box, not a shortest-vector certificate.

For the easiest hypothetical field degree $r=1$, the best selected
component margins and the representative genuine-mix margins are:



$$
\begin{array}{c|c|ccc}
d&m&n=4&n=5&n=6\\ \hline
2&2&-14.798/-34.040&-17.674/-43.884&-18.096/-42.970\\
2&3&-20.048/-70.484&-24.286/-57.924&-29.061/-77.909\\
3&2&-26.126/-45.157&-25.513/-45.940&-35.263/-58.938\\
3&3&-42.118/-78.066&-43.155/-67.026&-58.161/-80.240
\end{array}                                               \tag{48}
$$



Each entry is best selected component / selected genuine mix. All are
negative. On every row the separated hyperbolic bound (30), rather than
the direct Gaussian exponential bound (31), is the better mixed bound.

These finite signs are diagnostics only. The rigorous conclusion is the
all-parameter inequality (44)--(45), not failure of a bounded LLL search.

## 8. Replay and logical scope

Run from the archive root:

    python3 scripts/root_unity_gaussian_global_saturation_certificate.py

The replay verifies dependency hashes before import. It reconstructs every
complete global pair map and parity tail kernel; computes separate HNF
saturations; verifies centered reflection on both saturated and LLL bases;
computes the unphased Smith glue; constructs every aligned real-doubled
lattice and applies the exact product-intersection identity (21);
independently replays a tall-HNF saturation anchor; and checks exact
endpoint parity, content, degree, height, and coefficientwise domination
data.

All ranks, lattices, Smith invariants, contents, coefficient vectors, and
endpoint identities are exact. Radius optimizations, logarithmic margins,
and decimal values at $\pi$ are high-precision diagnostics. The replay
asserts a per-process RSS ceiling of 2 GiB and omits variable resource
measurements from its deterministic JSON.

This package proves no all-parameter bound for a saturated successive
minimum, no primitive-content formula inside one parity block, no
endpoint-cancellation theorem, and no irrationality or transcendence
result for $e+\pi$.
