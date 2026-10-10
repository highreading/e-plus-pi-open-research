> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A sharp dual interpolation problem for the denominator Schur Gram

Date: 2026-09-13. Original bounded continuation by audit_computations.

This gives an exact extremal formulation of the unresolved Gram in
`raw_denominator_exceptional_resolvent_bridge.md`. It retains the actual
two-component spectral measure, the common high factor, every true low
factor, and the normalization of the artificial jets. It also gives a
quantitative right inverse for the scalar jet constraints in the explicitly
scaled coefficient norm. That coefficient statement is distinguished from
the still unproved energy and retained-projection estimates.

The formulas are valid for any of the established cutoffs with the same
actual factorization and good-space estimate. A change of cutoff changes
$F,L_a,L_b$, the energy norm, and the extremizers; none is silently held
fixed across such a change.

## 1. The exact positive matrix measure and its weights

Use $N=2n$, the actual symmetric matrix $K=K_N$, and the actual
offset seeds



$$
V=[v_0,v_1],\qquad v_0=e_0,\quad v_1=e_1-(\sqrt3/2)e_0.
$$



Let $\Pi_\lambda$ be the spectral projector of $K$ at each distinct
eigenvalue, including its full multiplicity, and define the finite positive
two-by-two matrix measure



$$
d\Sigma(t)=\sum_{\lambda\in\operatorname{spec}K}
V^T\Pi_\lambda V\,\delta_\lambda(dt).
\tag{1}
$$



For vector functions having no pole on the row spectrum, put
$\mathfrak Bf=\sum_{\sigma=0}^1 f_\sigma(K)v_\sigma$. Then exactly



$$
(\mathfrak Bf)^T\mathfrak Bg=\int f(t)^T d\Sigma(t)g(t).
$$



Retain $F(t)=F_b(t)>0$ on the row spectrum. The actual energy product is



$$
\langle f,g\rangle_F=\int F(t)f(t)^T d\Sigma(t)g(t),
\qquad\|f\|_F=\|F(K)^{1/2}\mathfrak Bf\|_2.
\tag{2}
$$



Functions with identical row vectors are identified. Thus (2) is the actual
finite-dimensional energy inner product, not a claim of strict positivity
on an unrestricted function space. It is positive definite on each of the
polynomial and rational spaces used below. No atom or rank-one spectral
weight has been omitted.

Write $\boldsymbol Q=\operatorname{diag}(Q_0,Q_1)$, with the two true
parity node polynomials, and let



$$
\mathcal U=\{u=(u_0,u_1):\deg u_\sigma<d_\sigma\},
\qquad \mathcal R u=F^{-1}\boldsymbol Q u.
\tag{3}
$$



Its energy is precisely



$$
\boxed{\mathcal E(u)=\|\mathcal Ru\|_F^2
=\int\frac{(\boldsymbol Q u)^T d\Sigma(\boldsymbol Q u)}F
=u^THu,\qquad H=Z^TF(K)^{-1}Z>0.}
\tag{4}
$$



Here the last expression uses whichever fixed multiplier coefficient basis
is declared; all subsequent extremal statements are basis-independent.
The actual functions in (3), in the labels of the high-factor split, are



$$
\mathcal Ru=
\bigl((-1)^{h_a}R L_a u_a,;(-1)^{h_b}L_bu_b\bigr),
\tag{5}
$$



with the two components put in their original order. The displayed signs
can equivalently be included in the multiplier coordinates.

## 2. Minimum-energy interpolation at the artificial denominator nodes

Use the actual artificial nodes $x_j$, radii $r_j$, and amplitudes
$d_j=|\det P_N(x_j)|^{1/2}$ from the preceding bridge. The jet map is



$$
(\mathcal Ju)_{j,r}=d_j^{-1}[s^r]
\{Q_a(x_j+r_js)u_a(x_j+r_js)\},\qquad0\le r<\nu.
\tag{6}
$$



It has rank $D$. Its kernel is exactly the true multiplier space with
$u_a$ divisible by the artificial $Q$; the true factor $Q_a$ is
a unit at every artificial node.

For every data vector $h\in\mathbb R^D$, define



$$
u_h=\arg\min\{\mathcal E(u):u\in\mathcal U,\ \mathcal Ju=h\},
\qquad f_h=\mathcal Ru_h.
\tag{7}
$$



This is a unique strictly convex minimization problem. With
$G=\mathcal JH^{-1}\mathcal J^T>0$, the exact solution and value are



$$
\boxed{u_h=H^{-1}\mathcal J^TG^{-1}h,
\qquad\|f_h\|_F^2=h^TG^{-1}h.}
\tag{8}
$$



The functions $f_h$ are orthogonal in (2) to every
$\mathcal Ru$ with $\mathcal Ju=0$. Hence they are precisely the
energy-orthogonal denominator complement from the preceding note. The
choice of data norm in (8) is essential: replacing $G^{-1}$ by the
identity would change the question.

## 3. Exact best approximation into the retained prefix

Let



$$
q_\sigma=\lfloor(n-\sigma)/2\rfloor,\qquad
\mathcal P_L=\{p=(p_0,p_1):\deg p_\sigma\le q_\sigma\}.
\tag{9}
$$



Its dimension is $n+1$. The actual branch rows $R_0,\ldots,R_n$
are a basis, with $\mathfrak B(R_k^T)=e_k$. Thus its norm matrix in
that basis is exactly $F[L,L]$, not an asymptotic moment replacement.
The orthogonal projection onto $\mathcal P_L$ in (2) corresponds to
the retained energy projector $\Pi_L$.

For an extremizer from (7), its best-approximation coefficients in this
basis and its error are therefore explicit:



$$
p_h^{\rm best}(t)=\sum_{k=0}^n b_kR_k(t)^T,
\quad b=F[L,L]^{-1}Z_Lu_h,
$$





$$
\boxed{\inf_{p\in\mathcal P_L}\|f_h-p\|_F^2
=u_h^T\{H-Z_L^TF[L,L]^{-1}Z_L\}u_h.}
\tag{10}
$$



Define the actual worst relative error



$$
\alpha_N^2=\sup_{h\ne0}
\frac{\inf_{p\in\mathcal P_L}\|f_h-p\|_F^2}{h^TG^{-1}h}.
\tag{11}
$$



One always has $0\le\alpha_N\le1$. The matrix form, with its exact
data normalization, is



$$
\alpha_N^2=\left\|G^{-1/2}\mathcal JH^{-1}
\{H-Z_L^TF[L,L]^{-1}Z_L\}
H^{-1}\mathcal J^TG^{-1/2}\right\|.
\tag{12}
$$



This tests the selected minimum-energy interpolants, not every rational
function with those poles and not every multiplier coefficient vector.

Let $\mathcal G$ be the proved good subspace inside
$\mathcal R(\ker\mathcal J)$, and let its orthonormal frame have
retained defect at most $\eta_N<1$. Write $\gamma_N$ for the least
singular value of the actual denominator Schur columns after eliminating
that good frame. Then



$$
\boxed{\max\left\{0,1-\frac{\alpha_N^2}{1-\eta_N^2}\right\}
\le\gamma_N^2\le1-\alpha_N^2.}
\tag{13}
$$



To prove the lower bound, a unit denominator vector has retained norm
squared at least $1-\alpha_N^2$. Its full inner products with the
good frame vanish, by (8). Therefore its retained inner products with
the normalized retained good frame have norm at most
$\eta_N\alpha_N/\sqrt{1-\eta_N^2}$, using both discarded tails.
Subtracting that squared quantity gives the lower bound in (13).
For the upper bound, removal of the good directions can only decrease the
retained norm, and the worst discarded denominator tail has norm
$\alpha_N$.

There is also an exact version retaining the good-tail weight. For actual
orthonormal good and denominator frames put
$D_g=(I-\Pi_L)O_g$, $D_a=(I-\Pi_L)O_D$. The exact Schur formula
and the identity
$I+D_g(I-D_g^TD_g)^{-1}D_g^T=(I-D_gD_g^T)^{-1}$ give



$$
\boxed{\mathcal T_D^T\mathcal T_D
=I-D_a^T(I-D_gD_g^T)^{-1}D_a,
\qquad\gamma_N^2
=1-\|(I-D_gD_g^T)^{-1/2}D_a\|^2.}
\tag{13a}
$$



The inverse exists because $\|D_g\|\le\eta_N<1$. Comparing its
weight with $I$ and $(1-\eta_N^2)^{-1}I$ recovers (13). This
refinement was supplied and checked by the independent reviewer.

In particular, a proved uniform $\alpha_N\le c<1$ would remove all
$D$ denominator directions for large $N$, with a uniform lower
bound for their Schur block. More generally the same proof on any data
subspace of dimension $r$ gives $r$ controlled independent Schur
columns. No such nonzero-dimensional subspace estimate is proved here.

## 4. A sharp dual low-degree interpolation problem

The exact test space is



$$
\mathcal A_L=\{p\in\mathcal P_L:
\langle p,g\rangle_F=0\ \hbox{for every }g\in\mathcal G\}.
\tag{14}
$$



Its dimension is $D+k_0+2$, because projection is injective on the
good space. Its orthogonality equations retain the true factors:



$$
\int p(t)^T d\Sigma(t)\boldsymbol Q(t)u_g(t)=0
\qquad(u_g\hbox{ in the actual good multiplier space}).
\tag{15}
$$



Explicitly, in channel $a$, those multipliers are
$u_a=Qv$, $\deg v\le q_a-\ell_a-D$, and in channel $b$
they obey $\deg u_b\le q_b-\ell_b$. Thus (15) is a prescribed finite
family of moments against $Q_aQv$ and $Q_bu_b$, with the matrix
measure (1), rather than an unspecified scalar orthogonality condition.

The exact infimum-supremum formula for the desired lower bound is



$$
\boxed{\gamma_N^2=
\inf_{h\ne0}\ \sup_{p\in\mathcal A_L\setminus\{0\}}
\frac{|\langle p,f_h\rangle_F|^2}
{\|p\|_F^2\,h^TG^{-1}h}.}
\tag{16}
$$



The supremum is the norm squared of the projection onto the retained
space orthogonal to the retained good frame, so (16) is the Gram (21)
of the preceding bridge with its actual weights.

A constructive dual version makes a sufficient interpolation estimate
particularly explicit. Given $h$, minimize $\|p\|_F^2$ over
$p\in\mathcal A_L$ subject to



$$
\langle p,f_{h'}\rangle_F=h^TG^{-1}h'
\qquad\hbox{for every }h'\in\mathbb R^D.
\tag{17}
$$



Denote the value by $I_N(h)$, with value $+\infty$ if infeasible.
Then



$$
\boxed{\sup_{h\ne0}\frac{I_N(h)}{h^TG^{-1}h}
=\gamma_N^{-2},}
\tag{18}
$$



where the right side is infinite if $\gamma_N=0$. Indeed, in an
orthonormal basis of (14), the constraints are exactly
$\mathcal T_D^Ty=G^{-1/2}h$; their minimum squared Euclidean norm is
the inverse Gram quadratic form. This proves (18) and all singular cases.

Thus a construction satisfying (15), (17), with
$\|p\|_F^2\le B_N h^TG^{-1}h$, would give precisely
$\gamma_N\ge B_N^{-1/2}$. The polynomial degrees, moment constraints,
jet data, and both energy weights are fixed in this problem.

## 5. Quantitative true-factor jets and a coefficient right inverse

The independently checked theorem in
`raw_uniform_true_artificial_node_gap.md` gives
$|x_j-\xi_l|\ge1/21$. It already suffices for the following weaker,
but useful, fully explicit estimate. Let $V$ be any product of at most
$N$ true node factors, including $L_a,F_a,Q_a$. On
$|z-x_j|\le1/(84N)$, each normalized linear factor differs from one
by at most $1/(4N)$. Hence



$$
|V(z)/V(x_j)|,\ |V(x_j)/V(z)|\le e^{1/2}.
$$



In the actual local variable $s=(z-x_j)/r_j$, the two normalized
Taylor coefficient sequences therefore have bounds
$e^{1/2}(84Nr_j)^k$. Their truncated Toeplitz maps and inverses obey



$$
\boxed{\|\mathcal T_j(V/V(x_j))\|,
\|\mathcal T_j(V(x_j)/V)\|
\le e^{1/2}\nu\max(1,84Nr_j)^{\nu-1}
=\exp\{O(\sqrt N\log N)\}.}
\tag{19}
$$



This proof does not require the stronger reciprocal-distance-sum corollary.
The estimate applies to each true low and high factor separately. Their
possibly large, distinct, signed values $V(x_j)$ have not been discarded.

For example define the exact diagonal jet weight



$$
\Lambda_a=\bigoplus_j[Q_a(x_j)/d_j]I_\nu.
\tag{20}
$$



Use the explicitly scaled multiplier coefficients
$u_a(z)=\sum c_k(z/N^2)^k$. The map
$\widehat{\mathcal J}=\Lambda_a^{-1}\mathcal J$ has a right inverse
of norm $\exp\{O(D\log N)\}$ in those coefficient and Euclidean jet
norms. Construct it by inverting (19), using the global degree-$(D-1)$
Hermite interpolant, and embedding that polynomial in the first channel
with the other channel zero. Its range has $\deg u_a<D$, so it lies
in the actual multiplier domain.

This is a concrete controlled solution of the affine jet constraints. It
does not bound its energy (4) by the minimum energy in (8): that comparison
uses the actual matrix $H$, not the scaled coefficient identity.
In the scaled coefficient basis, if $\widehat R$ is this right inverse,
the valid energy comparison retains the full matrix:



$$
G^{-1}\preceq
\Lambda_a^{-T}\widehat R^TH_{\rm sc}\widehat R\Lambda_a^{-1}.
\tag{21}
$$



No operator-norm bound for $H_{\rm sc}$, and no replacement of
$\Lambda_a$ by a common scalar, has been inserted into (21).

## 6. Why the scalar approximation alone does not yet bound (11)

For the minimum-energy interpolants, define the actual cancellation factor



$$
\chi_N=\sup_{h\ne0}
\frac{\|(L_au_{a,h},0)\|_F}{\|f_h\|_F},
\tag{22}
$$



with the component in its actual parity position. A scalar approximation
$\|R-p\|_{\infty,\operatorname{spec}K}\le\varepsilon$ then gives
the valid error bound



$$
\|f_h-((\pm pL_au_{a,h}),\pm L_bu_{b,h})\|_F
\le\varepsilon\chi_N\|f_h\|_F.
\tag{23}
$$



At a cutoff where a full actual channel angle $\delta_N>0$ has also
been proved, the lower bound $R\ge2/n$ implies



$$
\chi_N\le n/(2\delta_N).
\tag{24}
$$



This is conditional only on the stated full-angle input; it never imports
an angle bound proved merely on a $Q$-restricted family. It applies
directly at the new large-constant $O(\sqrt n)$ cutoff of
`raw_sqrt_cutoff_full_channel_angle.md`, whose full-angle theorem has
passed independent review.

Even with (24), (23) need not be a competitor in (10). In general
$\deg(L_au_{a,h})$ can be $q_a+\ell_a+O(1)$, and multiplying by
a polynomial approximant of degree $m$ adds $m$ more degrees.
The low-factor excess is $O(\sqrt n)$ at the new square-root cutoff;
it was larger at the earlier $n^{3/4}$ cutoff.
The allowed prefix degree remains exactly $q_a$. The second component
can likewise exceed $q_b$ by its low-factor excess. Thus a norm bound
for (23) does not prove $\alpha_N<1$ unless the degree excess is
handled for the actual extremizers. Simply discarding those coefficients
has no established bound in the weighted norm (2).

The rational surrogate avoids that excess on the already divisible family.
On the denominator complement it produces proper rational parts and their
actual projected Gram from the preceding bridge. The coefficient right
inverse in Section 5 and the full-space resolvent bound do not by themselves
control that weighted projection.

## 7. Concrete remaining mathematical target

Two fully specified sufficient targets are now available:

* Construct low-degree vector polynomials satisfying (15), (17), with the
  relative norm estimate in (18); or
* Prove a relative best-approximation bound (11) below
  $\sqrt{1-\eta_N^2}$ for the minimum-energy actual interpolants (7).

The first target is an exact dual characterization of the desired inverse
bound. The second is a sufficient approximation criterion, not a necessary
condition for a positive but potentially much smaller Schur singular value.

The second target need only concern those extremizers, not arbitrary
coefficient vectors. The first allows the $k_0+2$ excess test degrees
remaining after the good constraints and prescribed denominator data.
Either could also be proved on a growing data subspace to improve the
exceptional count partially. No such subspace or uniform estimate is
established in this note.

All these statements concern the actual energy Schur block. Its physical
kernel still passes through $S^{-1}F[L,L]^{-1/2}U_e$, with the original
cardinal and $g_l$ factors. A successful interpolation estimate would
enable the exact further reduction already recorded in the bridge; it does
not remove those physical weights or prove an endpoint remainder bound.

The separate continuation `raw_single_channel_denominator_extremizers.md`
sharpens the full-to-single energy comparison, gives the exact positive
scalar reproducing kernel, and proves a growing-subspace retained bound
before mixed good-space subtraction. It preserves the latter subtraction
as an additional estimate.
