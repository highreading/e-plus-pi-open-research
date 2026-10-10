> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An explicit exceptional Schur problem after the weighted-angle closure

Date: 2026-09-13. Original continuation by audit_computations.
Independent root review: raw_exceptional_schur_root_review.md passes
the complete reduction and all normalization factors without correction.

This note continues the reviewed
`raw_positive_weight_channel_angle_closure.md`. It identifies the
good directions by their exact component degrees, rather than by
unknown singular vectors of the high matrix. Eliminating those
directions leaves a concrete (k+2)-by-k matrix, k=O(n^(3/4)),
with controlled surrounding blocks. The physical amplitude/cardinal
map is retained in an explicit positive metric of dimension k+2.

The remaining small matrix is not proved full rank. This is an exact
reduction of the outstanding directions, beyond a rank count.

## 1. Actual normalized maps and the reviewed error

Use N=2n, p=n−1, L={0,...,n}, the reoptimized cutoff
b=ceil(n^(3/4)), and polynomial degree m=ceil(24n^(3/4)).
All statements below concern sufficiently large n, as in the closure
theorem. Retain its exact matrices



$$
X=[R(K)W_a,W_b],\quad
\widetilde X=[p_m(K)W_a,W_b],\quad F=F_b(K)>0,
\quad Z=FX.
\tag{1}
$$



The original seeds are v_0=e_0 and v_1=e_1−(sqrt3/2)e_0;
the factors L_sigma, F_sigma and domain counts d_sigma are those
of the actual node polynomials. Only their previously specified
fixed column signs and ordering are suppressed.

Let



$$
B=\operatorname{diag}(G_a^{1/2},G_b^{1/2}),\quad
E=F^{1/2}XB^{-1},\quad G=E^TE>0,\quad
T_0=B^{-1}G^{-1/2},
$$





$$
O=F^{1/2}XT_0,\quad
\widetilde O=F^{1/2}\widetilde XT_0,\quad
\mathcal A=F[L,L]^{-1/2}Z_LT_0.
\tag{2}
$$



O has p orthonormal columns. Write Pi for the orthogonal projection
onto F^(1/2) of the coordinate prefix L and D=(I−Pi)O. The
closure theorem supplies



$$
\|O-\widetilde O\|\le\eta_n,
\qquad \eta_n=O(n^3e^{-2\sqrt{6n}}),
\qquad \mathcal A^T\mathcal A=I-D^TD.
\tag{3}
$$



In particular ||D||<=1. The explicit retained orthonormal frame
is F^(1/2)P_L^T F[L,L]^(−1/2), giving exactly the A in (2).

## 2. The exceptional degrees are explicit

Set q_sigma=floor((n−sigma)/2). The first n+1 branch rows
are exactly the vector polynomials whose channel-sigma degree is
at most q_sigma. Thus a surrogate combination has no coordinate
above n if and only if



$$
\deg u_a\le q_a-\ell_a-m,\qquad
\deg u_b\le q_b-\ell_b.
\tag{4}
$$



There is no cross-channel cancellation in this condition: its
branch polynomial is `(p_m L_a u_a,L_b u_b)` in the respective
channels. A nonzero scalar multiplier raises that component's
degree by its exact degree.

Here p_m has degree exactly m for m>=1 when a high pair remains.
Indeed each Chebyshev resolvent polynomial

    [1−T_(m+1)(z(t))/T_(m+1)(z_beta)]/(beta−t)

has positive leading coefficient, and p_m is one minus their
strictly positive weighted sum. Thus its leading coefficient
cannot cancel. There are high pairs for all sufficiently large n
under the present cutoff. Empty finite cases can instead use the
actual degree of p_m and do not affect the theorem.

Let I_g select the low multiplier coefficients specified by (4)
from the original p-dimensional coefficient domain. Its column
count g and complementary count k are exactly



$$
g_\sigma=\min\{d_\sigma,\max(0,q_\sigma-\ell_\sigma
-m_\sigma^{\rm app}+1)\},\quad
m_a^{\rm app}=m,\quad m_b^{\rm app}=0,
$$





$$
g=g_0+g_1,\qquad
k=p-g=\sum_\sigma
\min\{d_\sigma,\max(0,d_\sigma+\ell_\sigma
+m_\sigma^{\rm app}-q_\sigma-1)\}.
\tag{5}
$$



For large n the inner counts are neither truncated nor zero.
For even n the two offsets d_sigma−q_sigma−1 are −2,0;
for odd n they are −1,−1. Therefore



$$
\boxed{k=m+\ell_0+\ell_1-2
\in\{m+b-1,m+b\}=O(n^{3/4}).}
\tag{6}
$$



The two choices correspond to whether one extra high root was
moved into a low list. This explicit count is smaller than the
earlier safe support enlargement 2m+b+O(1).

By (4), the good orthonormal-input subspace is exactly



$$
\mathcal G=T_0^{-1}\operatorname{ran}I_g
=G^{1/2}B\operatorname{ran}I_g.
\tag{7}
$$



It is the kernel of the surrogate coordinate-tail map above n,
not a subspace chosen from singular vectors of the actual A.
An explicit orthonormal frame is



$$
Q_g=Y_g(Y_g^TY_g)^{-1/2},\qquad
Y_g=G^{1/2}BI_g.
\tag{8}
$$



Let Q_e be any orthonormal complement, with k columns. Choices
of this complement only change the small matrix by orthogonal
basis changes. Since tilde(O)Q_g lies in the retained energy
space, (3) gives



$$
\boxed{\|DQ_g\|\le\eta_n.}
\tag{9}
$$



## 3. An exact rectangular Schur matrix with controlled good blocks

Write A_g=AQ_g, A_e=AQ_e, and define



$$
R_g=(A_g^TA_g)^{1/2},\qquad U_g=A_gR_g^{-1}.
\tag{10}
$$



For eta_n<1, (3),(9) imply



$$
\boxed{\sqrt{1-\eta_n^2}\,I\preceq R_g\preceq I.}
\tag{11}
$$



Thus U_g has orthonormal columns. Complete it by an orthonormal
U_e with k+2 columns in the retained (n+1)-dimensional space.
The exact remaining matrices are



$$
\mathcal B=U_g^TA_e,\qquad
\boxed{\mathcal T_n=U_e^TA_e\in\mathbb R^{(k+2)\times k}.}
\tag{12}
$$



They give the exact identity



$$
\boxed{
[U_g,U_e]^T\mathcal A[Q_g,Q_e]
=\begin{pmatrix}R_g&\mathcal B\\0&\mathcal T_n\end{pmatrix}.}
\tag{13}
$$



Moreover, using Q_g^TQ_e=0,



$$
\mathcal B=-R_g^{-1}(DQ_g)^T DQ_e,
\qquad
\boxed{\|\mathcal B\|\le
\frac{\eta_n}{\sqrt{1-\eta_n^2}}.}
\tag{14}
$$



In particular ||T_n||<=1. Right multiplication by
`[[I,−R_g^(-1)B],[0,I]]` reduces (13) exactly to the rectangular
block diagonal matrix diag(R_g,T_n). Both this multiplier and
its inverse have norm at most



$$
1+\frac{\eta_n}{1-\eta_n^2}.
\tag{15}
$$



All other transformations in (13) are orthogonal. Thus this is
a Schur reduction with uniformly controlled surrounding energy
blocks, rather than an assertion merely that most singular values
are large. In particular



$$
\boxed{\operatorname{rank}Z_L=g+\operatorname{rank}\mathcal T_n.}
\tag{16}
$$



Full retained rank is now equivalent to full column rank of this
specific (k+2)-by-k matrix. Its small singular values, up to the
controlled factors (11),(15), are the remaining energy singular
values of the original projection.

## 4. A small positive Gram and an explicit surrogate comparison

Put D_g=DQ_g and D_e=DQ_e. Eliminating the good Gram block
in (13) gives the exact k-by-k positive semidefinite matrix



$$
\boxed{\mathcal T_n^T\mathcal T_n
=I-D_e^TD_e
-D_e^TD_g(I-D_g^TD_g)^{-1}D_g^TD_e.}
\tag{17}
$$



The last term is positive semidefinite and has norm at most
eta_n^2/(1−eta_n^2). This identifies precisely the good-block
correction; it is already exponentially small on the sqrt(n) scale.

For a construction involving only the explicit surrogate tail,
enlarge L to the smallest prefix containing tilde(X), and denote
its additional coordinate indices by J. Its size r is at most
2m+b+3. Define the actual positive coordinate Schur complement



$$
\Sigma_F=F[J,J]-F[J,L]F[L,L]^{-1}F[L,J]>0,
\quad
\mathcal L_e=\Sigma_F^{1/2}\widetilde X[J,:]T_0Q_e.
\tag{18}
$$



An orthonormal basis of the corresponding extra energy space is



$$
V_J=F^{1/2}
\begin{pmatrix}-F[L,L]^{-1}F[L,J]\\ I_J\\0\end{pmatrix}
\Sigma_F^{-1/2}.
$$



Direct block multiplication shows
`(I−Pi)tilde(O)Q_e=V_J L_e`. By (3),
`||D_e−V_J L_e||<=eta_n`, and hence ||L_e||<=1+eta_n.
Combining this with (17) gives the quantitative small-matrix test



$$
\boxed{\left\|\mathcal T_n^T\mathcal T_n
-(I-\mathcal L_e^T\mathcal L_e)\right\|
\le2\eta_n+\eta_n^2+
\frac{\eta_n^2}{1-\eta_n^2}.}
\tag{19}
$$



Thus a lower bound for `I−L_e^T L_e` exceeding this explicit
error would prove complete rank and an energy inverse bound.
No such contraction bound is proved here. In particular the
positivity of Sigma_F alone does not establish it.

## 5. All physical amplitude and cardinal factors remain in a small metric

Retain the exact complementary identity



$$
H_{\rm hi}=-Z_H^{-T}Z_L^TS,\qquad
S=Y_{\rm low}\operatorname{diag}(g_0,\ldots,g_n).
\tag{20}
$$



The matrices Z_H and S are invertible. From (2),
`Z_L^T=T_0^(-T) A^T F[L,L]^(1/2)`. The triangular form
(13) shows that `ker A^T=U_e ker T_n^T`: its first block
equation forces the U_g coordinate to zero. Consequently



$$
\boxed{\ker H_{\rm hi}
=J_e\ker\mathcal T_n^T,\qquad
J_e=S^{-1}F[L,L]^{-1/2}U_e.}
\tag{21}
$$



All actual amplitudes remain in S, with their original node and
parity order. Define the positive definite small physical metric



$$
M_e=J_e^TJ_e\in\mathbb R^{(k+2)\times(k+2)},\qquad
W_e=J_eM_e^{-1/2}.
\tag{22}
$$



W_e is an exact isometry into the physical spectral-coordinate
space. Equivalently the entire remaining physical kernel problem
is the small matrix



$$
\boxed{\widehat{\mathcal T}_n=M_e^{-1/2}\mathcal T_n,
\qquad \ker H_{\rm hi}=W_e\ker\widehat{\mathcal T}_n^T.}
\tag{23}
$$



The metric in (22) is not assumed well conditioned. This transfers
its actual effect into (23); it does not discard that effect.

If T_n has full column rank, choose orthonormal V with two columns
spanning ker(T_n^T). The original endpoint determinant/angle from
the cardinal reduction is then exactly



$$
\boxed{\mathfrak d_n=
\frac{\det((P_*J_e)V)^2}{\det(V^TM_eV)},
\qquad P_*\text{ selects spectral coordinates }n-1,n.}
\tag{24}
$$



Alternatively an orthonormal basis of ker(hat(T)_n^T), multiplied
by the isometry W_e, gives the physical orthonormal kernel directly.
If T_n is deficient, its larger kernel and all physical nullvectors
are still represented by (21)-(23), but the two-dimensional
formula (24) is not invoked.

## 6. The remaining concrete estimates

The exceptional directions are precisely the high multiplier-degree
complement to (4), expressed in the actual combined normalization.
Their count k=m+b+O(1) is explicit. The surrounding good block
has inverse norm at most (1−eta_n^2)^(−1/2), and its interaction
with the exceptional columns is O(eta_n).

The unresolved estimates can therefore be pursued on matrices of
dimension O(n^(3/4)):

* Prove T_n has full column rank, or quantitatively bound its least
  singular value. Equation (19) gives one precise sufficient
  surrogate-tail contraction criterion.
* Control the physical metric M_e and the two endpoint rows in
  (24) on the small remaining kernel. All g_l and low-cardinal
  factors are retained in this request.

The construction itself does not prove either estimate. In particular
an arbitrary exp(−Ck) lower bound would still need comparison with
the actual error scale in (19); k grows faster than sqrt(n).
Neither full high rank, the physical endpoint angle, primitive
shrinking, nor irrationality is inferred. No numerical scan or
canonical HP coefficient solve was used.
