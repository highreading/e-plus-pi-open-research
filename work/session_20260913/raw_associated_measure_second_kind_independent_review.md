> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the associated Legendre second-kind measure

Date: 2026-09-13. Reviewer: audit_sources.

Target: raw_associated_measure_legendre_second_kind.md, Sections 1–3.
Dependency read in full: raw_coupled_pencil_exact_legendre_square.md and its passing raw_legendre_square_measure_independent_review.md.

**Verdict: PASS.** The stripping index, second-kind branch, probability-density normalization, both fixed-index edge asymptotics, harmonic shift, and limiting coefficient $K_a\to8/\pi$ are correct. No mathematical correction is needed. No numerical or degree scan was used. This review does not supply a growing-index estimate beyond what the target explicitly states.

## 1. Tail stripping and the exact factor $c_m^2$

Write $a=m+1$, $m\ge0$. For the original squared-Legendre probability measure


$$
d\mu_0(y)=\frac{dy}{2\sqrt y},
$$


the monic polynomial and norm are


$$
\pi_m(y)=\frac{P_{2m}(\sqrt y)}{\kappa_{2m}},
\qquad
h_m=\frac1{(4m+1)\kappa_{2m}^2}.
$$


The normalization is immediate after $y=u^2$: the norm is
$\int_0^1P_{2m}(u)^2du/\kappa_{2m}^2$, which is the ordinary even Legendre norm $1/[(4m+1)\kappa_{2m}^2]$.

For the monic recurrence, $h_m=\prod_{j=0}^{m-1}c_j^2$, with $h_0=1$. The lower row of the $(m+1)$-step stripping matrix is


$$
(C_{m+1},D_{m+1})
=c_m^2(\pi_m,-\sigma_{m-1}).
$$


This includes the boundary $m=0$: the matrix is
$\bigl(\begin{smallmatrix}z-d_0&-1\\c_0^2&0\end{smallmatrix}\bigr)$, while $\pi_0=1,\sigma_{-1}=0$. The next lower row is $c_1^2(z-d_0,-1)$, consistent with $\pi_1=z-d_0,\sigma_0=1$. The same product recurrence proves the general identity, and


$$
\det T_{m+1}=\prod_{j=0}^{m}c_j^2=c_m^2h_m.
$$


Thus the density belongs to $\mu_{m+1}$, not to $\mu_m$, and its coefficient contains the actual last off-diagonal $c_m^2$.

The integral identity needed in the denominator is exact:


$$
\pi_m(z)m_0(z)-\sigma_{m-1}(z)
=\int\frac{\pi_m(y)}{z-y}\,d\mu_0(y)
=\frac{Q_{2m}(\sqrt z)}{\kappa_{2m}\sqrt z}.
$$


For $s=\sqrt z$, evenness gives


$$
Q_{2m}(s)
=\frac12\int_0^1P_{2m}(u)
 \left(\frac1{s-u}+\frac1{s+u}\right)du
=s\int_0^1\frac{P_{2m}(u)}{s^2-u^2}\,du.
$$


The identity is first valid off the interval with the branch inherited from the integral; on its upper side near $0<y<1$, $\sqrt{y+i0}=\sqrt y+i0$.

Substitution into the previously proved full density yields


$$
\frac{c_m^2h_m}
 {2\sqrt y\,c_m^4|Q_{2m}(\sqrt y+i0)|^2/(\kappa_{2m}^2y)}
=
\frac{\sqrt y}
 {2c_m^2(4m+1)|Q_{2m}(\sqrt y+i0)|^2}.
$$


This checks the factors $2$, $4m+1$, and $c_m^2$ independently. The integral convention $1/(s-u)$ gives the negative imaginary boundary part
$-i\pi P_{2m}(x)/2$, exactly as stated.

The preceding reviewed measure theorem proves that this is the entire probability measure: there is no interior singular component or endpoint atom. The target appropriately invokes that theorem instead of inferring total mass merely from the density calculation.

## 2. The zero endpoint and the constant $8/\pi$

For fixed $m$, $P_{2m}$ is even with


$$
P_{2m}(0)=(-1)^m\binom{2m}{m}/4^m\ne0.
$$


The real boundary part of $Q_{2m}$ is an odd analytic function in a neighborhood of zero. This follows directly from its logarithmic-polynomial representation: $P_{2m}$ is even, the logarithm is odd and analytic there, and the corresponding polynomial $W_{2m-1}$ is odd.

Consequently


$$
P_{2m}(\sqrt y)^2=P_{2m}(0)^2+O_m(y),
\qquad
\mathsf Q_{2m}(\sqrt y)^2=O_m(y).
$$


Its denominator has a positive nonzero constant term, so taking its reciprocal is valid and gives exactly


$$
w_a(y)=
\frac{2\sqrt y}{\pi^2c_m^2(4m+1)P_{2m}(0)^2}
\bigl(1+O_m(y)\bigr).
$$


The $m=0$, $a=1$ case is included; no division by $m$ is used.

Finally,


$$
c_m\longrightarrow\frac14,\qquad
P_{2m}(0)^2\sim\frac1{\pi m}.
$$


Hence


$$
\pi^2c_m^2(4m+1)P_{2m}(0)^2\longrightarrow\frac\pi4,
$$


and the stated limit $K_a\to8/\pi$ follows. This is a limit of the exact fixed-edge coefficients, not a uniform assertion about $w_a(y)/\sqrt y$ when both variables change.

## 3. The one endpoint and the harmonic shift

Polynomial division gives


$$
\mathsf Q_l(x)=\frac12P_l(x)\log\frac{1+x}{1-x}-W_{l-1}(x).
$$


The recurrence


$$
(l+1)W_l=(2l+1)xW_{l-1}-lW_{l-2},
\quad W_{-1}=0,\quad W_0=1
$$


is consistent with the Legendre second-kind recurrence, including its first step. At $x=1$,


$$
(l+1)H_{l+1}=(2l+1)H_l-lH_{l-1}
$$


follows from $H_{l+1}-H_l=1/(l+1)$ and $H_l-H_{l-1}=1/l$. These initial values and recurrence establish $W_{l-1}(1)=H_l$, including $l=0$.

Put $x=\sqrt{1-\epsilon}$. Then


$$
\log\frac{1+x}{1-x}
=\log\frac4\epsilon+
2\log\frac{1+\sqrt{1-\epsilon}}2
=\log\frac4\epsilon+O(\epsilon).
$$


For fixed $l$, $P_l(x)=1+O_l(\epsilon)$ and
$W_{l-1}(x)=H_l+O_l(\epsilon)$. Multiplying the logarithm by the first polynomial retains the error
$O_l(\epsilon\log(1/\epsilon))$. This proves the target's expansion


$$
2\mathsf Q_l(\sqrt{1-\epsilon})
=\log(4/\epsilon)-2H_l+
O_l(\epsilon\log(1/\epsilon)).
$$


Squaring it, including the imaginary contribution
$\pi^2P_l(x)^2$, and retaining the numerator $\sqrt{1-\epsilon}$ gives the stated ratio asymptotic


$$
w_a(1-\epsilon)\sim
\frac{2}{c_m^2(4m+1)}
\frac1{[\log(4/\epsilon)-2H_{2m}]^2+\pi^2}.
$$


All errors are legitimate for each fixed index. None is uniform in $m$, and no such uniformity is asserted.

The limiting constant-coefficient Jacobi matrix has diagonal $1/2$ and off-diagonal $1/4$. Its first-coordinate density is
$(8/\pi)\sqrt{y(1-y)}$. For each fixed $a$, the ratio of the displayed endpoint asymptotic to this semicircle density is a positive constant times


$$
\frac1{\sqrt\epsilon\,\log^2(1/\epsilon)}\longrightarrow\infty.
$$


Thus the claimed failure of a global constant upper comparison is correct, even before allowing the index to grow. It does not imply that an edge interval has substantial total mass, or obstruct a comparison away from that edge.

The next uniform-measure theorem must therefore retain both the dependence on $a$ and an explicit edge scale. The fixed-index theorem supplies a correct normalization and a useful boundary constraint, but does not itself prove a mixed zero bound or an arithmetic conclusion.

