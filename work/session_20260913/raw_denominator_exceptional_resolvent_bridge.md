> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The exact boundary-resolvent bridge to the denominator exceptional directions

Date: 2026-09-13. Original bounded continuation by audit_computations.

This identifies the artificial-denominator directions of the actual full
vanishing image by explicit boundary-resolvent jet constraints. It derives
their exact normalized columns in the retained Schur matrix. The full-space
jet family has a proved subexponential inverse bound; the additional weighted
projection required for the actual Schur columns remains explicit and is not
asserted to preserve that bound.

The inputs are the reviewed `raw_confluent_boundary_resolvent_gram.md`,
`raw_intermediate_holomorphic_jet_bounds.md`,
`raw_dyadic_hermite_interpolation_and_branch_composition.md`, and the actual
rational-surrogate and exceptional-Schur constructions.

## 1. Exact branch/resolvent identity with the right boundary factor

Put $N=2n$, $K=K_N$, and let $V_0$ insert the final two coordinates.
Use the actual symmetric branch rows $R_k(z)$, with seeds
$R_0=(1,0)$, $R_1=(\sqrt3/2,1)$, and set



$$
\Phi_N(z)=\begin{pmatrix}R_0(z)\\\vdots\\R_{N-1}(z)\end{pmatrix},
\qquad P_N(z)=\begin{pmatrix}R_N(z)\\R_{N+1}(z)\end{pmatrix},
$$





$$
\Gamma_N=\begin{pmatrix}a_{N-1}a_N&0\\-a_N&a_Na_{N+1}\end{pmatrix}.
$$



The first $N$ exact recurrence rows, including their two omitted right
boundary coordinates, give



$$
(zI-K)\Phi_N(z)=V_0\Gamma_NP_N(z).
$$



Consequently, away from the row spectrum,



$$
\boxed{\Phi_N(z)=(zI-K)^{-1}V_0\Gamma_NP_N(z).}
\tag{1}
$$



There is no left-source term: the actual seed rows solve the recurrence at
zero and one. There is no transpose on $\Gamma_N$ in (1).

Retain the exact artificial nodes, multiplicities, and radii



$$
x_j=N+3/4+(3/2)N2^j,\quad
\nu=\lceil4\sqrt{3N}/\log3\rceil,\quad
D=\nu J,\quad r_j=\sqrt{x_j}\log N/2,
$$



and put $d_j=|\det P_N(x_j)|^{1/2}>0$. Define the full normalized
branch-jet matrix by its two-column blocks



$$
\mathcal U_{j,r}=
\frac1{d_j}\frac{r_j^r}{r!}\Phi_N^{(r)}(x_j),
\qquad0\le j<J,\quad0\le r<\nu.
\tag{2}
$$



Let $\mathcal W^\Gamma$ have corresponding blocks



$$
\mathcal W^\Gamma_{j,r}
=\frac{r_j^r}{r!}
\left[\frac{d^r}{dz^r}(zI-K)^{-1}\right]_{z=x_j}V_0\Gamma_N.
\tag{3}
$$



These are precisely the reviewed scaled resolvent jets with the right factor
$\Gamma_N/N^2$: writing $a_j=x_j/N^2$, $\eta_j=r_j/N^2$,



$$
\mathcal W^\Gamma_{j,r}
=(-1)^r\eta_j^r(a_jI-K/N^2)^{-r-1}V_0(\Gamma_N/N^2).
\tag{4}
$$



Thus no factor of $N^2$ is lost in using the confluent Gram theorem.

If $A_j(t)=P_N(x_j+r_jt)/d_j=\sum A_{j,k}t^k$, the product rule in
(1) says exactly



$$
\boxed{\mathcal U=\mathcal W^\Gamma\mathscr T^{\rm up},}
\tag{5}
$$



where the block at derivative indices $(s,r)$ of the node-$j$ upper
Toeplitz matrix is $A_{j,r-s}$ for $s\le r$, and zero otherwise.
It is the usual local lower Toeplitz matrix conjugated by reversal of the
derivative order. Its inverse is the upper Toeplitz matrix for $A_j^{-1}$.

The independently proved resolvent and local jet bounds consequently give



$$
\boxed{e^{-C D\log N}\le\sigma_{\min}(\mathcal U)
\le\|\mathcal U\|\le e^{C D\log N}.}
\tag{6}
$$



For either actual channel $a\in\{0,1\}$, let $S_a$ select its one
column in every two-column jet block, and put



$$
U_a=\mathcal U S_a\in\mathbb R^{N\times D}.
\tag{7}
$$



Since $S_a$ is an isometry, the same singular-value bounds hold for
$U_a$. This is a bound for a specific selected-channel family in the
full original row space. It has not yet been compressed to retained rows
or projected into the vanishing image.

## 2. The artificial nodes do not coincide with any true node

The actual prolate node satisfies the strict bounds



$$
l(l+1)+3/4<\xi_l<l(l+1)+1.
\tag{8}
$$



For completeness, the reviewed operator is the Legendre operator plus
$3/4+u^2/4$ on $[-1,1]$. Multiplication by $u^2/4$ is strictly
positive on every nonzero square-integrable function, and strictly less
than $1/4$ in the same quadratic-form sense. On each finite-dimensional
subspace the relevant minimum is positive. Apply the min-max principle to
the span of the first $l+1$ perturbed eigenvectors for the strict lower
bound, and to the first $l+1$ unperturbed Legendre eigenvectors for the
strict upper bound. This proves (8), including $l=0$.

Every artificial $x_j$ is an integer plus $3/4$, by its exact formula
and even $N$. Thus it cannot equal any $\xi_l$. In particular each
actual parity node polynomial



$$
Q_\sigma(z)=\prod_{\substack{0\le l\le n\\l\equiv\sigma\ (2)}}
(z-\xi_l)
$$



is a unit modulo the artificial denominator



$$
Q(z)=\prod_{j=0}^{J-1}(x_j-z)^\nu.
\tag{9}
$$



This is a proved coprimality assertion. It does not give a quantitative
minimum distance between true and artificial nodes, and none is required
for the algebraic kernel identity below.

## 3. Exact first-channel jet constraints on the actual vanishing matrix

Use the actual full coefficient map



$$
Z(u_0,u_1)=Q_0(K)u_0(K)v_0+Q_1(K)u_1(K)v_1,
\quad v_0=e_0,\quad v_1=e_1-(\sqrt3/2)e_0,
\tag{10}
$$



with $\deg u_\sigma<d_\sigma=n-m_\sigma$. Its domain has dimension
$p=n-1$, and the reviewed triangular polynomial-coordinate argument
proves it injective. The fixed column signs which write it instead as
$F[R L_a u_a,L_bu_b]$ are invertible diagonal signs and are retained
when identifying coefficient matrices.

For any row coefficient vector $c$, its vector polynomial is
$\Phi_N(z)^Tc$. The exact Krylov coordinate identity for (10) therefore
gives



$$
\Phi_N(z)^TZ(u_0,u_1)
=\begin{pmatrix}Q_0(z)u_0(z)\\Q_1(z)u_1(z)\end{pmatrix}.
\tag{11}
$$



All degrees are at most $n-1$, so no finite-boundary reduction or
uncontrolled recurrence remainder occurs in this identity.

In the rational-surrogate construction let $a$ denote the channel on
which the artificial divisibility restriction was imposed. Equations
(2), (7), and (11) prove



$$
\boxed{(U_a^TZ(u_0,u_1))_{j,r}
=d_j^{-1}[t^r]\{Q_a(x_j+r_jt)u_a(x_j+r_jt)\}.}
\tag{12}
$$



The true node polynomial in (12) contains both of the actual low and high
factors. More explicitly, let $\mathcal E_a$ evaluate these locally
scaled jets of $u_a$, let $\mathcal B_a$ be block Toeplitz
multiplication by the jets of $Q_a$, and put
$\mathcal D_d=\bigoplus_jd_j I_\nu$. In the original multiplier
coefficient order,



$$
\boxed{\mathcal J_a:=U_a^TZ
=[\mathcal D_d^{-1}\mathcal B_a\mathcal E_a,\ 0],}
\tag{13}
$$



with the two displayed channel blocks permuted if $a=1$. Furthermore



$$
\mathcal B_a=(-1)^{h_a}\mathcal T(L_a)\mathcal T(F_a),
$$



where each $\mathcal T$ is the exact finite jet multiplication map at
the same nodes. Neither factor is replaced by a common parity polynomial.
The factor $d_j^{-1}$ in (12)--(13) is also retained.

By coprimality in Section 2, vanishing of all these jets is equivalent to
divisibility of $u_a$ by $Q$. Therefore



$$
\boxed{\ker\mathcal J_a
=\{(u_a,u_b):u_a=Qv,\ \deg v<d_a-D,\ \deg u_b<d_b\}.}
\tag{14}
$$



Since $d_a>D$ eventually, its codimension is exactly $D$. This is
the actual restricted family used in the rational rank proof, not a freely
chosen subfamily of the resolvent columns.

## 4. The omitted D directions in the actual energy metric

Retain $F=F_b(K)>0$ from the actual high-factor split. Define



$$
Y=F^{-1/2}Z,\quad H=Y^TY=Z^TF^{-1}Z>0,
\quad\mathcal W=\operatorname{ran}Y,
\quad\Pi_{\mathcal W}=YH^{-1}Y^T.
\tag{15}
$$



Thus $\mathcal W$ is exactly the full energy image used by the Schur
reduction; it equals $F^{1/2}\operatorname{ran}X$. Put



$$
C_a=F^{1/2}U_a,\qquad
G_a=C_a^T\Pi_{\mathcal W}C_a
=\mathcal J_a H^{-1}\mathcal J_a^T.
\tag{16}
$$



The equality follows from $C_a^TY=U_a^TZ=\mathcal J_a$. By (14),
$\mathcal J_a$ has full row rank $D$. Consequently $G_a>0$,
without any assumption about full retained rank.

Let $\mathcal W_Q\subset\mathcal W$ be the actual restricted energy
image with $u_a=Qv$. Exactly



$$
\mathcal W_Q=\mathcal W\cap\ker C_a^T,
\qquad \dim\mathcal W_Q=p-D.
$$



Its energy-orthogonal complement inside the full image has the explicit
orthonormal frame



$$
\boxed{O_D=\Pi_{\mathcal W}C_aG_a^{-1/2}
=YH^{-1}\mathcal J_a^TG_a^{-1/2}.}
\tag{17}
$$



Indeed the range of $\Pi_{\mathcal W}C_a$ is the orthogonal complement
of the kernel of $C_a^T$ restricted to $\mathcal W$, and its Gram
is (16). This exactly identifies all $D$ omitted directions in the
same energy metric as the rank theorem.

The lower bound for $U_a^TU_a$ in (6)--(7) is a different statement
from a lower bound for $G_a$. Equation (16) includes the actual high
factor, the projection into the full vanishing image, and its coefficient
Gram. These operations have not been assigned a new condition bound.

## 5. Exact denominator columns in the retained Schur matrix

Let $L=\{0,\ldots,n\}$, and let



$$
U_L=F^{1/2}P_L^T F[L,L]^{-1/2},\qquad\Pi_L=U_LU_L^T
\tag{18}
$$



be the isometric frame and orthogonal projector of the retained energy
space. Choose the reviewed orthonormal good frame $O_g$ inside
$\mathcal W_Q$. Its dimension is



$$
g=p-D-k_0,\qquad k_0=\ell_0+\ell_1-2=O(\sqrt n),
$$



and $\|(I-\Pi_L)O_g\|\le\eta_n$, with the proved
$\eta_n=O(n^3e^{-2\sqrt{6n}})$. Complete $O_g$ within
$\mathcal W_Q$ by an orthonormal $O_\ell$ with $k_0$ columns.
Then $[O_g,O_\ell,O_D]$ is an orthonormal frame of the full image.

Set



$$
R_g=(O_g^T\Pi_LO_g)^{1/2},\quad
U_g=U_L^TO_gR_g^{-1},
$$



and choose an orthonormal complement $U_e$ to $U_g$ in the retained
coordinate space. It has $k_0+D+2$ columns. The exact residual matrix is



$$
\mathcal T=[\mathcal T_\ell,\mathcal T_D]
=U_e^TU_L^T[O_\ell,O_D].
\tag{19}
$$



The good block and its off-diagonal coupling obey the already proved bounds;
choosing this particular orthonormal complement inside the full image does
not alter those estimates. In particular



$$
\operatorname{rank}Z_L=g+\operatorname{rank}\mathcal T.
$$



Combining (13), (15), and (17)--(19) gives the requested exact block identity:



$$
\boxed{\mathcal T_D=
U_e^TF[L,L]^{-1/2}Z_L
H^{-1}\mathcal J_a^TG_a^{-1/2}.}
\tag{20}
$$



Its Gram, written directly through the resolvent constraints, is



$$
\boxed{\mathcal T_D^T\mathcal T_D
=G_a^{-1/2}C_a^T\Pi_{\mathcal W}
U_L(I-U_gU_g^T)U_L^T
\Pi_{\mathcal W}C_aG_a^{-1/2}.}
\tag{21}
$$



Every projection and normalization in this positive semidefinite
$D$-by-$D$ matrix is specified by actual project matrices. The middle
factor is the projector onto the retained energy space after the good
directions have been removed. It is not the identity from the full boundary
Gram theorem.

For comparison, $O_g^TO_D=0$ and the good defect bound give



$$
\|U_g^TU_L^TO_D\|\le\eta_n/\sqrt{1-\eta_n^2}.
$$



Thus (21) differs from $O_D^T\Pi_LO_D$ by a positive semidefinite
matrix of norm at most $\eta_n^2/(1-\eta_n^2)$. This does not justify
discarding the correction relative to a potentially smaller lower bound.
The exact normalized Gram (21) is the sufficient target.

Equivalently, write $\mathcal G=\operatorname{ran}O_g$ and
$\mathcal D=\mathcal W\ominus\mathcal W_Q=\operatorname{ran}O_D$.
The missing singular value is exactly the actual distance



$$
\sigma_{\min}(\mathcal T_D)
=\inf_{\substack{w\in\mathcal D\\\|w\|=1}}
\operatorname{dist}(\Pi_Lw,\Pi_L\mathcal G).
\tag{21a}
$$



There is also an exact zero-kernel formulation. If
$\mathcal T_Dv=0$, set



$$
w=O_Dv-O_gR_g^{-1}U_g^TU_L^TO_Dv.
$$



Then $w\in\mathcal W\cap\ker\Pi_L$, its component in
$\mathcal W\ominus\mathcal W_Q$ is $O_Dv$, and its remaining
component is in $\mathcal G$, with no $O_\ell$ component.
Conversely every such retained-kernel vector comes from this formula;
injectivity of $\Pi_L$ on $\mathcal G$ gives uniqueness. Thus



$$
\dim\ker\mathcal T_D
=\dim\bigl[(\mathcal W\cap\ker\Pi_L)
\cap(\mathcal G\oplus\mathcal D)\bigr].
\tag{21b}
$$



This is a kernel obstruction involving the actual good subspace and the
exact artificial-divisibility complement. It does not replace them by
arbitrary subspaces of a well-conditioned full resolvent family.

## 6. What a bound for that Gram would remove, including the physical map

Suppose, additionally, that the specific matrix (21) is bounded below by
$\gamma_n^2I_D$, with $\gamma_n>0$. Then set



$$
R_D=(\mathcal T_D^T\mathcal T_D)^{1/2},\quad
V_D=\mathcal T_DR_D^{-1},
$$



and complete $V_D$ by $V_\ell$, with $k_0+2$ columns.
Permuting the residual columns to $[\mathcal T_D,\mathcal T_\ell]$
gives exactly



$$
[V_D,V_\ell]^T[\mathcal T_D,\mathcal T_\ell]
=\begin{pmatrix}R_D&B_D\\0&\mathcal T_{\rm low}\end{pmatrix},
\quad\mathcal T_{\rm low}=V_\ell^T\mathcal T_\ell.
\tag{22}
$$



Since $\|\mathcal T\|\le1$, $\|B_D\|\le1$. Eliminating it costs
at most $1+\gamma_n^{-1}$ in both multiplier and inverse norm.
Consequently



$$
\boxed{\operatorname{rank}Z_L
=g+D+\operatorname{rank}\mathcal T_{\rm low}
=p-k_0+\operatorname{rank}\mathcal T_{\rm low}.}
\tag{23}
$$



The remaining matrix has size $(k_0+2)$-by-$k_0$.

All physical factors can be retained through this further reduction. The
previous exact physical map was



$$
J_e=S^{-1}F[L,L]^{-1/2}U_e,\qquad M_e=J_e^TJ_e,
$$



where $S$ contains the actual low-cardinal and spectral amplitudes
$g_l$. Since $\ker\mathcal T^T=V_\ell\ker\mathcal T_{\rm low}^T$,



$$
\boxed{\ker H_{\rm high}=J_{\rm low}\ker\mathcal T_{\rm low}^T,
\quad J_{\rm low}=J_eV_\ell,\quad
M_{\rm low}=V_\ell^TM_eV_\ell.}
\tag{24}
$$



Thus a proved lower bound for (21) would remove the denominator directions
without dropping the cardinal, amplitude, or energy factors. The assertion
in this section is conditional on that precise lower bound; it is not a
consequence already drawn from (6).

## 7. The remaining obstruction is now a specified actual angle

The full normalized branch-jet family (7) is subexponentially conditioned.
The exact coefficient constraint (13) and the denominator complement (17)
are unconditional. The missing estimate is the least eigenvalue of (21),
which measures the angle between that actual denominator complement and the
retained energy space after the good columns are removed.

There are two concrete operations between the reviewed resolvent Gram and
this target: projection into $F^{-1/2}\operatorname{ran}Z$, with the
normalization (16), and the retained/good projection in (21). The actual
low-factor jet maps and the physical $S/g_l$ factors have been retained
in (13), (20), and (24). No estimate presently proves that these projections
preserve a subexponential inverse bound, or even that $\mathcal T_D$
has full column rank. Therefore the $D$ directions are identified exactly,
but have not yet been removed from the unconditional exceptional count.
