> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Single-channel denominator extremizers and an actual retained-band bound

Date: 2026-09-13. Original continuation by audit_computations.

This specializes the dual interpolation problem to a positive scalar
measure. It proves a retained-projection lower bound on a growing subspace
of the single-channel extremizers. It does not transfer that lower bound
through the actual mixed good-space subtraction; the precise remaining
weight mismatch is displayed below.

Use the independently checked full-channel theorem
`raw_sqrt_cutoff_full_channel_angle.md`, with
$b=\lceil192\sqrt n\rceil$, its actual common factor $F$, and
$\delta\ge1/(2A_n)$. Use the same cutoff for every space and norm here.
The node, jet, and scalar amplitude definitions are those in
`raw_denominator_dual_variational_interpolation.md`.

## 1. Full interpolation differs from one-channel interpolation by a controlled factor

In the actual first-channel coefficient order write



$$
H=\begin{pmatrix}H_a&H_{ab}\\H_{ab}^T&H_b\end{pmatrix}>0,
\qquad\mathcal J=[J_a,0],
$$





$$
G=\mathcal JH^{-1}\mathcal J^T,
\qquad G_a=J_aH_a^{-1}J_a^T>0.
$$



The full-angle theorem gives
$H\succeq\delta^2\operatorname{diag}(H_a,H_b)$. The block inverse
identity also gives the sharper one-sided comparison



$$
(H^{-1})_{aa}
=(H_a-H_{ab}H_b^{-1}H_{ab}^T)^{-1}\succeq H_a^{-1}.
$$



Consequently



$$
\boxed{G_a\preceq G\preceq\delta^{-2}G_a,
\qquad\delta^2G_a^{-1}\preceq G^{-1}\preceq G_a^{-1}.}
\tag{1}
$$



All true-factor jet maps and distinct node amplitudes remain inside $J_a$.

Let $f_h$ be the full minimum-energy lift of data $h$, and let
$f_h^a$ be its minimum-energy lift restricted to channel $a$, with
the other multiplier set to zero. Then



$$
E(h)=\|f_h\|_F^2=h^TG^{-1}h,\qquad
E_a(h)=\|f_h^a\|_F^2=h^TG_a^{-1}h,
$$





$$
\boxed{\delta^2 E_a(h)\le E(h)\le E_a(h),
\qquad\|f_h^a-f_h\|_F^2=E_a(h)-E(h).}
\tag{2}
$$



The last equality is Pythagoras: the difference has zero artificial jet
data, while the full minimum-energy lift is orthogonal to that entire
restricted space. In particular the full coupling costs at most
$\exp(O(\sqrt n))$ in norm at the present cutoff.

## 2. The exact positive scalar measure and Hermite kernel

Let $d\Sigma$ be the actual two-component left-seed spectral measure of
$K_N$ from the preceding note. Put



$$
d\nu_a(t)=F(t)\,d\Sigma_{aa}(t),\qquad
r_a(t)=Q_a(t)/F(t)=(-1)^{h_a}R(t)L_a(t),
$$





$$
\boxed{d\mu_a(t)=r_a(t)^2d\nu_a(t)
=F(t)R(t)^2L_a(t)^2d\Sigma_{aa}(t).}
\tag{3}
$$



Thus $f_h^a$ is the one-component function $r_au_h^a$, where
$u_h^a$ minimizes $\int |u|^2d\mu_a$, for $\deg u<d_a$,
subject to the exact constraints



$$
(J_au)_{j,r}=d_j^{-1}[s^r]
\{Q_a(x_j+r_js)u(x_j+r_js)\}=h_{j,r}.
\tag{4}
$$



The moment Gram is $H_a>0$, so orthonormal scalar polynomials
$p_0,\ldots,p_{d_a-1}$ exist for this finite positive measure.
Define its actual reproducing kernel



$$
K_a(t,z)=\sum_{k=0}^{d_a-1}p_k(t)p_k(z),
\quad
k_{j,r}(t)=d_j^{-1}[s^r]
\{Q_a(x_j+r_js)K_a(t,x_j+r_js)\}.
\tag{5}
$$



Writing $k(t)$ for the column vector of these $D$ functions,
one has exactly



$$
G_a=\left(\int k_i(t)k_j(t)d\mu_a(t)\right)_{i,j},
\qquad
\boxed{u_h^a(t)=k(t)^TG_a^{-1}h.}
\tag{6}
$$



This follows directly by the reproducing property and minimum-norm
interpolation. It is a genuine positive scalar kernel for the actual
single channel. It is not a claim that the full two-channel moment system
is scalar orthogonal. Both true high factors, the low polynomial, the
actual left-seed measure, and the factors $Q_a(x_j)/d_j$ are retained.

## 3. A growing scalar subspace has a proved retained lower bound

Set $q_a=\lfloor(n-a)/2\rfloor$ and



$$
t_a=\max\{0,d_a-q_a+\ell_a-1\}=O(\sqrt n).
$$



Impose the linear top-coefficient conditions



$$
\deg(L_au_h^a)\le q_a.
\tag{7}
$$



The maximal possible degree before these conditions is
$\ell_a+d_a-1$. Since $h\mapsto u_h^a$ is linear, (7) imposes
at most $t_a$ conditions. It defines a data subspace
$\mathcal H_{\rm band}$ of dimension at least $D-t_a$.

For such data, the same-channel polynomial
$p_h=(-1)^{h_a}L_au_h^a$ belongs to the actual prefix space.
Positivity $2/n\le R\le1$ gives



$$
\langle p_h,f_h^a\rangle_F
=\int F R(L_au_h^a)^2d\Sigma_{aa}
\ge\int F R^2(L_au_h^a)^2d\Sigma_{aa}
=\|f_h^a\|_F^2,
$$





$$
\|p_h\|_F\le(n/2)\|f_h^a\|_F.
$$



The variational characterization of the orthogonal projection onto the
retained prefix therefore proves



$$
\boxed{\|\Pi_L f_h^a\|_F\ge(2/n)\|f_h^a\|_F
\qquad(h\in\mathcal H_{\rm band}).}
\tag{8}
$$



This is an actual growing-subspace retained lower bound, obtained without
approximating $R$ or estimating a numerical matrix. It concerns the
single-channel extremizers before subtraction of the mixed good space.
It does not yet improve the unconditional full exceptional count.

## 4. A dimension reduction for comparing full and single extremizers

Write the actual restricted space as the orthogonal sum



$$
\mathcal W_Q=\mathcal G\oplus\mathcal L,
\qquad\dim\mathcal L=k_0=\ell_0+\ell_1-2.
$$



The linear map $h\mapsto\Pi_{\mathcal L}(f_h^a-f_h)$ has rank at
most $k_0$. Its kernel $\mathcal H_0$ therefore has dimension at
least $D-k_0$. On this data subspace,



$$
\boxed{f_h^a-f_h\in\mathcal G.}
\tag{9}
$$



In particular, after the retained good space is removed, the projections
of $f_h^a$ and $f_h$ are identical. The intersection
$\mathcal H_0\cap\mathcal H_{\rm band}$ has dimension at least
$D-k_0-t_a$, still growing with $D$.

This dimension statement alone is not a lower bound after subtraction.
Let $\Pi_{L,g}$ denote the projector onto the retained good space.
For $h\in\mathcal H_0$, the exact remaining quantity is



$$
\|(I-\Pi_{L,g})\Pi_Lf_h\|_F^2
=\|\Pi_Lf_h^a\|_F^2-\|\Pi_{L,g}f_h^a\|_F^2.
\tag{10}
$$



The lower bound (8) controls the first term. It does not bound the second
term away from the first.

There is a precise weight mismatch in the tempting positive test from
Section 3. Minimum-energy scalar interpolation makes $u_h^a$
orthogonal to zero-data multipliers in the measure
$F R^2L_a^2d\Sigma_{aa}$. But the pairing of $p_h$ with a
first-channel restricted good function contains



$$
\int F R L_a^2 u_h^a\,Qv\,d\Sigma_{aa},
\tag{11}
$$



which has only one power of $R$. It need not vanish. The other-channel
good pairings additionally contain the actual off-diagonal measure
$d\Sigma_{ab}$. Neither can be erased by the scalar kernel positivity
in (5)--(6). Thus (8) has not been promoted to a bound for the mixed
denominator Schur columns.

## 5. A valid sufficient single-channel approximation criterion

For reference, define the scalar best-approximation error



$$
\epsilon_a=
\sup_{h\ne0}
\frac{\inf_{\deg p\le q_a}
\|r_au_h^a-p\|_{L^2(\nu_a)}}{\|u_h^a\|_{L^2(\mu_a)}}.
\tag{12}
$$



This is a positive scalar weighted approximation problem with the explicit
kernel (5), not an assertion of a bound for it. Let $\eta$ be the actual
good-space retained defect. On $\mathcal H_0$, (2) and (9) imply



$$
\frac{\operatorname{dist}_F(f_h,\mathcal P_L)}{\|f_h\|_F}
\le\epsilon_*:=\delta^{-1}\epsilon_a+
\eta\sqrt{\delta^{-2}-1}.
\tag{13}
$$



Indeed approximate $f_h^a$ by its scalar prefix approximant and
$f_h^a-f_h\in\mathcal G$ by the retained projection of that good
function. Their relative norms are bounded by (2).

If the additional estimate $\epsilon_*^2<1-\eta^2$ is proved, the
sharp comparison in the dual note supplies at least $D-k_0$ independent
denominator Schur columns with lower bound
$\sqrt{1-\epsilon_*^2/(1-\eta^2)}$. The unconditional good columns
then give the conditional improvement



$$
\operatorname{rank}Z_L\ge p-2k_0,
\qquad p=n-1.
\tag{14}
$$



This sufficient criterion may be stronger than necessary: a direct small
positive lower bound for (10) would suffice without near-unit approximation.
The proved band statement (8), together with the exact subtraction (10),
identifies that weaker target on $D-O(\sqrt n)$ data directions.

With the presently conservative constants
$\eta=O(n^3e^{-2\sqrt{6n}})$ and
$\delta^{-1}=O(n^2e^{2\sqrt{6n}})$, their product is not proved small.
Thus even a hypothetical tiny $\epsilon_a$ would not justify (14)
from those bounds alone. Increasing the rational multiplicity constant,
for example to $\nu\ge\lceil6\sqrt{6n}/\log3\rceil$, would make the
corresponding bound for $\eta/\delta$ tend to zero without changing any
$O(\sqrt n\log n)$ dimension or $O(D\log N)$ interpolation order.
That would be a re-run with the newly specified denominator multiplicity,
not a claim about the currently fixed constant.

## 6. What has and has not improved

The full-to-single energy comparison (1)--(2), the positive scalar Hermite
kernel (5)--(6), the growing retained-band lower bound (8), and the
dimension comparison (9) are proved. They reduce the remaining question to
a specific positive scalar extremal family and its pairings with the actual
good space, while preserving the full channel correction.

No lower bound for (10) after its subtraction is proved. The additional
conditions for (14) are therefore left conditional, and the full
unconditional exceptional count is unchanged. If an actual mixed retained
bound is established, the further Schur reduction and its physical map
$S^{-1}F[L,L]^{-1/2}U_eV_{\rm rem}$ remain exactly as in the bridge,
including every original cardinal and $g_l$ factor.

