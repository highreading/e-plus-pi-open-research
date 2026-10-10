> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The actual mixed test operator: a boundary-resolvent Schur reduction

Date: 2026-09-13. Original continuation by audit_computations.
Independent root review in raw_mixed_boundary_schur_root_review.md
passes the complete algebra and its conditional dimension consequence.

This note extends the scalar compressed-multiplier construction to the
actual two-channel test problem. It proves an exact rank-four Jacobi
displacement identity and an explicit sum of rank-one boundary resolvents
for the remaining Schur correction. A lower bound for that correction is
not proved. All statements use the common metric at the checked cutoff
`b=ceil(192 sqrt(n))`; neither the true node polynomials nor the seeds are
changed. The growing-data-subspace consequence in Section 6 is conditional.

## 1. Use orthonormal coordinates for the two actual polynomial spaces

Put `N=2n`, `K=K_N`, and `F=F_b(K)>0`. Include the fixed channel signs in
the corresponding coefficient maps. The relevant Euclidean spaces after
energy weighting are



$$
\mathcal A=\operatorname{span}\{F^{1/2}L_a(K)K^jv_a:j<d_a\},\qquad
\mathcal B=\operatorname{span}\{F^{1/2}L_b(K)K^jv_b:j<d_b\}.
\tag{1}
$$



Choose orthonormal bases `V_a,V_b` by increasing polynomial degree,
with positive leading coefficients. Their coefficient changes are
invertible: the original vanishing map is injective and the actual high
factors are invertible on the row spectrum. Set



$$
C=V_b^TV_a,\qquad P=I-V_bV_b^T,\qquad Z=PV_a,\qquad G_Z=Z^TZ.
\tag{2}
$$



These two polynomial spaces have independent component polynomials.
The positive-weight reflection lemma applies directly to their sum:
their support ends at `n+O(sqrt(n))` and `deg F<=n/2+1`. Consequently,
with `A_n=12 sqrt(28)n^2 exp(2 sqrt(6n))`,



$$
G_Z=I-C^TC\succeq A_n^{-2}I>0.                     \tag{3}
$$



Indeed the combined normalized angle is at least `1/A_n`; if `c` is
the largest cross cosine, `1-c^2>=1-c>=A_n^{-2}`. This is the
*polynomial* pair angle; it is not an assertion that projection `P`
commutes with the high-factor ratio.

Write `R=R(K)=F_a(K)/F_b(K)`, so `2I/n<=R<=I`. The actual full pair,
in these coordinates, is `[RV_a,V_b]`. The cross test matrix for the
polynomial tests `[V_a,V_b]` is exactly



$$
\mathcal A_0=
\begin{pmatrix}
 V_a^TRV_a&C^T\\ V_b^TRV_a&I
\end{pmatrix},\qquad
\boxed{S=V_a^TPRV_a=Z^TRV_a.}                       \tag{4}
$$



Eliminating the second row/column gives `det A_0=det S`. No positive
matrix interpretation of `A_0` or `S` is being made.

## 2. The actual second-channel Jacobi boundary is rank one

The scalar measure for the orthogonal basis of `B` is



$$
d\chi_b(t)=F(t)L_b(t)^2\,d\Sigma_{bb}(t),             \tag{5}
$$



where `Sigma` is the actual left-seed matrix spectral measure. If
`phi_0,...,phi_(d_b-1)` are its orthonormal polynomials, the columns
of `V_b` are `F^(1/2)L_b(K)phi_k(K)v_b`. Multiplication by `t` has
its usual three-term recurrence on these polynomials, because the
measure is positive. Thus



$$
KV_b=V_bJ_b+\beta_b\eta_b e_b^T,\quad
J_b=V_b^TKV_b,\quad V_b^T\eta_b=0,\quad\|\eta_b\|=1,
\tag{6}
$$



where `J_b` is the real symmetric tridiagonal Jacobi matrix, `e_b`
is its last coordinate, and `beta_b>=0`. If the next orthogonal
polynomial has zero norm, take `beta_b=0`; the space is invariant and
all terms containing `beta_b eta_b` below vanish. The same construction
applies to `V_a`, giving `J_a,beta_a,eta_a,e_a`. Empty-channel cases are
trivial and can be omitted for the sufficiently large indices here.

For any `x>lambda_max(K)`, equation (6), multiplied by the two exact
resolvents, gives



$$
\boxed{P(xI-K)^{-1}V_b
=\beta_b P(xI-K)^{-1}\eta_b e_b^T(xI-J_b)^{-1}.}       \tag{7}
$$



This has rank at most one. It follows from
`(xI-K)V_b=V_b(xI-J_b)-beta_b eta_b e_b^T`; in particular its sign
is positive. All eigenvalues of `J_b` lie in the row spectral interval,
so every inverse displayed in (7) exists at the actual high poles.

For completeness the boundary row in (7) has an explicit scalar
orthogonal-polynomial formula. Put



$$
D_b(x)=\det(xI-J_b),\qquad D_k(x)=\det(xI-J_b[0:k,0:k]),\quad D_0=1.
$$



If the positive internal Jacobi coefficients are `b_1,...,b_(d_b-1)`,
then for `0<=k<d_b`



$$
[e_b^T(xI-J_b)^{-1}]_k
=\frac{(b_{k+1}\cdots b_{d_b-1})D_k(x)}{D_b(x)}.      \tag{8}
$$



This is the tridiagonal cofactor formula; empty products equal one.
Thus the boundary row is an explicit Christoffel--Darboux resolvent
row, not an arbitrary vector introduced to factor a matrix.

## 3. A positive Schur term minus explicit Stieltjes boundary terms

Keep the actual interlacing high roots and positive weights



$$
R(t)=1-\sum_{i=1}^h\frac{c_i}{\beta_i-t},\qquad c_i>0,
\quad\sum_i\frac{c_i}{\beta_i-M_n}<1,
\quad M_n=2n+3/4.                                    \tag{9}
$$



Decompose `V_a=Z+V_b C`. Equations (7)--(9) prove



$$
\boxed{S=S_+-UV^T,\qquad S_+=Z^TRZ\succeq(2/n)G_Z,} \tag{10}
$$



where the `d_a` by `h` matrices have exact columns



$$
U_i=\beta_b c_i Z^T(\beta_iI-K)^{-1}\eta_b,
\qquad
V_i^T=e_b^T(\beta_iI-J_b)^{-1}C.                     \tag{11}
$$



The minus sign comes from (9). In particular



$$
\det S=\det S_+\det(I_h-V^TS_+^{-1}U).               \tag{12}
$$



If the last matrix is invertible, the exact inverse is



$$
S^{-1}=S_+^{-1}+S_+^{-1}U
(I_h-V^TS_+^{-1}U)^{-1}V^TS_+^{-1}.                 \tag{13}
$$



Both formulas remain valid when some columns vanish. The two factors
in each rank-one term (11) are different. Positivity of `c_i` and of
each resolvent therefore does not make `UV^T` positive semidefinite,
nor does it bound the spectrum of `V^TS_+^{-1}U` below one.

The overlap appearing here retains the actual cross-channel measure:
if `psi_j` is the orthonormal basis in `F L_a^2 dSigma_aa`, then



$$
C_{k,j}=\int F(t)L_b(t)L_a(t)\phi_k(t)\psi_j(t)
\,d\Sigma_{ba}(t).                                  \tag{14}
$$



Deleting this integral, or substituting a diagonal matrix measure,
would change the problem. Equations (8), (11), and (14) give a concrete
scalar-orthogonal-polynomial and boundary-resolvent description of the
remaining mixed correction.

## 4. The same Schur matrix has Jacobi displacement rank at most four

The operator identity from (6) is



$$
[K,P]=-\beta_b\eta_be_b^TV_b^T
       +\beta_bV_be_b\eta_b^T.
$$



Since `R` commutes with `K`, direct multiplication in (4) yields



$$
\begin{split}
J_aS-SJ_a={}&\beta_a(V_a^TPR\eta_a)e_a^T
-\beta_a e_a(\eta_a^TPRV_a)\\
&-\beta_b(V_a^T\eta_b)(e_b^TV_b^TRV_a)
+\beta_b(V_a^TV_be_b)(\eta_b^TRV_a).
\end{split}                                                     \tag{15}
$$



Every displayed summand has rank one. Thus `rank(J_aS-SJ_a)<=4`
for every index in scope, with explicit generators. This is a genuine
structured-matrix identity for the actual mixed test operator, not
merely a rank estimate for its defining Gram matrix. When `J_a` is
irreducible its eigenvalues `tau_j` are distinct; after orthogonal
diagonalization all off-diagonal entries are consequently



$$
\widetilde S_{ij}=\frac{\widetilde\Delta_{ij}}{\tau_i-\tau_j}
\quad(i\ne j),\qquad\Delta=J_aS-SJ_a.               \tag{16}
$$



The diagonal entries are still required. Low displacement rank by
itself proves neither nonvanishing nor a lower singular-value bound.

## 5. Exact full-channel test correction and the missing angle

Let `J_a` now denote the actual first-channel jet map in the `V_a`
coefficient basis only in this paragraph; to avoid confusion call it
`mathscr J_a`. It still contains the true-factor jets, the distinct
`d_j`, and the local jet scales. Put



$$
H_R=V_a^TR^2V_a>0,\qquad
G_a=\mathscr J_aH_R^{-1}\mathscr J_a^T>0,
\qquad j_h=\mathscr J_a^TG_a^{-1}h.                 \tag{17}
$$



If `S` is invertible, define



$$
w_h=S^{-T}j_h,\qquad p_h=PV_aw_h
=V_aw_h-V_bCw_h.                                    \tag{18}
$$



Then this actual polynomial test is orthogonal to the *entire* second
channel and satisfies, for every full multiplier pair `(u,v)`,



$$
\boxed{\langle p_h,RV_au+V_bv\rangle
=h^TG_a^{-1}\mathscr J_a u.}                        \tag{19}
$$



It is therefore orthogonal to the full zero-data space, including both
good channels. This is the exact extension of the scalar multiplier
correction; its solvability is precisely the new issue.

A useful normalized form of that issue is



$$
\boxed{\gamma_{\rm mix}
=\sigma_{\min}(G_Z^{-1/2}S H_R^{-1/2}).}              \tag{20}
$$



It is an actual angle between `PV_a` and `RV_a`, with their own
orthonormalizations. For `gamma_mix>0`, (18) gives



$$
\|p_h\|\le\gamma_{\rm mix}^{-1}\sqrt{h^TG_a^{-1}h}.  \tag{21}
$$



Indeed `||p_h||^2=j_h^T S^{-1}G_ZS^{-T}j_h`, while
`j_h^T H_R^{-1}j_h=h^TG_a^{-1}h`. The proved angle for `[RV_a,V_b]`
controls the projection of `RV_a` away from `V_b`; it does not establish
its cross angle with the distinct space `PV_a` in (20).

One sufficient explicit boundary estimate is



$$
\sigma_{\min}(I-S_+^{-1/2}UV^TS_+^{-1/2})\ge\tau>0.
\tag{22}
$$



It implies `gamma_mix >= (2/n) A_n^{-2} tau`, because `S_+`
has that lower bound by (3), (10), and both `G_Z,H_R<=I`.
An estimate `tau>=exp(-o(n))` would therefore be sufficient here.
No such estimate is established in this note.

## 6. Why this target would remove most denominator directions

The two polynomial components of (18) have degrees below `d_a,d_b`
before multiplication by `L_a,L_b`. Requiring their products to have
degrees at most `q_sigma=floor((n-sigma)/2)` imposes at most



$$
t_a+t_b,\qquad t_\sigma=\max(0,d_\sigma-q_\sigma+\ell_\sigma-1)
=O(\sqrt n)                                        \tag{23}
$$



linear conditions on the `D` data entries. On the resulting data space
of dimension at least `D-t_a-t_b`, `p_h` is an actual prefix test and,
by (19), is orthogonal to its retained good space. If `f_h` is the full
minimum-energy lift, then



$$
\langle p_h,f_h\rangle=h^TG_a^{-1}h=E_a(h),\quad
E(h)\le E_a(h).
$$



Together with (21), this gives a retained-after-good-subtraction lower
bound at least `gamma_mix` on these data directions, when they are
normalized in the full minimum-energy norm. Thus a proved positive
bound in (20), or the sufficient estimate (22), would eliminate
`D-O(sqrt(n))` denominator directions and leave only `O(sqrt(n))`
exceptional directions. This conclusion is conditional; no such
elimination is counted among the established theorems.

The resulting physical maps still require the factors
`S_cardinal^{-1} F[L,L]^{-1/2} U_e` from the denominator bridge, including
the original amplitudes `g_l`. All transformations above are energy
coordinates or explicitly invertible coefficient changes; none of
these physical factors has been absorbed into an unspecified constant.

## 7. Precise remaining step

The scalar positive multiplier removes first-channel good constraints.
The actual second-channel elimination replaces it by (10). Equations
(7)--(16) expose the remaining correction through one Jacobi boundary,
the true Stieltjes weights, and the actual cross measure. They offer
concrete targets for an orthogonal-polynomial or divided-difference
argument. They do not yet show that its spectrum avoids the forbidden
value in (12), nor do they prove the data-restricted solvability that
would already suffice instead of full invertibility of `S`.
