> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root review of the explicit exceptional Schur reduction

Date: 2026-09-13. Result: PASS, without mathematical correction.

Reviewed raw_explicit_exceptional_schur_reduction.md against the accepted
positive-weight angle closure, component degree conventions, and exact
high-matrix/cardinal factorization. This review concerns the all-index
algebra and asymptotic bounds, not numerical controls.

The exact component degrees in the first n+1 row prefix are
q_sigma=floor((n-sigma)/2). Their dimensions sum to n+1 in both
parities of n. The leading coefficient of each Chebyshev resolvent
polynomial is positive, so the negative positive-weight sum defining
p_m has degree exactly m for m>=1 and a nonempty high list. Thus the
good coefficient selector and the count k=m+ell_0+ell_1-2 are exact
once the stated large-n nontruncation conditions hold. The two cases
ell_0+ell_1=b+1 or b+2 give k=m+b-1 or m+b. No cross-component
cancellation can remove an excess component degree.

The domain normalization has the correct order:
T_0=B^(-1)G^(-1/2), so T_0^(-1)I_g=G^(1/2)B I_g. The good
frame is therefore the kernel of the surrogate tail in the actual
orthonormal domain, rather than an unnormalized coefficient prefix.
For that frame, the actual tail norm is at most eta_n.

Since A*A=I-D*D, the good Gram is between (1-eta_n^2)I and I.
Its polar frame and an orthogonal complement yield exactly the
displayed rectangular triangular decomposition. The off-block formula
B_ge=-R_g^(-1)(D Q_g)*(D Q_e) has the correct order; its bound and
the norm bound for the nilpotent column elimination follow directly.
The dimensions are (g+k+2)-by-(g+k), so the remaining block is
(k+2)-by-k and rank Z_L=g+rank T_n.

The small Gram formula is the exact Schur complement of the good
Gram. Its correction is positive semidefinite and bounded by
eta_n^2/(1-eta_n^2). The coordinate Schur complement of F on L,J
is positive definite. The displayed V_J is orthonormal and gives
the whole surrogate residual after energy projection. Thus
||D_e-V_J L_e||<=eta_n, ||L_e||<=1+eta_n and the difference of
their two Gram matrices is at most 2eta_n+eta_n^2. This proves
the total error in equation (19), including its sign-independent norm
bound. It does not imply that I-L_e*L_e is positive definite.

Finally, Z_L^T=T_0^(-T)A^T F_LL^(1/2), so the physical nullspace
map is exactly J_e=S^(-1)F_LL^(-1/2)U_e. There is no transpose or
inverse-weight reversal. J_e has full column rank, hence M_e=J_e*J_e
is positive definite and W_e=J_e M_e^(-1/2) is an isometry.
Writing v=M_e^(1/2)y gives T_n^T y=0 iff
(M_e^(-1/2)T_n)^T v=0, verifying the transformed small matrix.
For a two-dimensional kernel, the endpoint determinant squared divided
by its physical Gram determinant is basis-independent and is exactly
the physical two-plane projection determinant. The note correctly
requires full column rank before invoking that two-dimensional formula.

The genuine remaining work is quantitative control of T_n and of the
physical metric/endpoint map on its kernel. The dimension reduction
does not remove the amplitudes g_l, turn eta_n into a lower bound,
or establish primitive shrinking. An exp(-Ck) small-matrix bound would
indeed be insufficient for the current exp(-c sqrt(n)) perturbation
argument without further improvement because k is of order n^(3/4).
