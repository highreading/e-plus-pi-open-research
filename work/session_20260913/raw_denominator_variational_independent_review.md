> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: denominator dual variational interpolation

Date: 2026-09-13. Reviewer: audit_results.

**Verdict: PASS on the final stable file, including (13a).** Reviewed all seven sections of `raw_denominator_dual_variational_interpolation.md` after the author's completion messages. Two wording issues were reported and corrected before finalization: the approximation threshold is sufficient, not equivalent to positivity of the Schur singular value; and an O(sqrt(n)) low-factor excess is specific to the new cutoff. No unresolved mathematical correction remains.

The separate new `raw_single_channel_denominator_extremizers.md` has not been reviewed as part of this audit. No conclusion from that separate note is assumed here.

## 1. Matrix measure and actual energy

The finite symmetric K_N spectral theorem gives the measure V^T Pi_lambda V at every distinct eigenvalue, with the full spectral projector if an eigenvalue is repeated. Expanding both functional-calculus vectors verifies the bilinear identity in Section 1. Since F(K)>0, multiplication by F^(1/2) gives the stated energy isometry. The qualification that functions with the same row vector are identified is necessary and correctly included: an unrestricted function-space strict positivity claim would be false.

For the actual multiplier domain, the coefficient map is Z and its columns are independent by the previously proved actual branch degree representation. Thus H=Z^T F^(-1)Z is positive definite. Substituting Rcal(u)=F^(-1)diag(Q_0,Q_1)u gives energy u^T H u exactly. The signs in the high-factor split may be absorbed into the corresponding channel coordinate and do not affect any subsequent norm or Gram formula. All factors, including the nonorthogonal offset seeds, remain present.

## 2. Affine interpolation and the data norm

The jet constraints are the actual normalized jets of Q_a u_a: the radius contributes r_j^r, division by r! is already encoded by coefficient extraction, and the amplitude is d_j^(-1). True/artificial coprimality makes local multiplication by Q_a invertible. The Hermite degree-D quotient gives rank D and kernel precisely the Q-divisible first multipliers, in the established large-index regime where D fits in the multiplier degree cap.

Lagrange multipliers in the positive definite H norm yield

    u_h=H^(-1)J^T G^(-1)h,
    G=J H^(-1)J^T,
    min energy=h^T G^(-1)h.

The minimizer is orthogonal to ker J in H energy. Hence its image is exactly the denominator orthogonal complement used in the resolvent bridge. Replacing the data norm by unweighted Euclidean norm would change the question; the note does not do so.

## 3. Retained approximation and the exact good-tail correction

The parity caps in (9) sum to a space of dimension n+1. The inverse branch identity B(R_k^T)=e_k identifies its norm matrix with F[L,L]. For f_h, its inner products with those basis elements are exactly Z_L u_h. Solving the positive definite normal equations gives b=F[L,L]^(-1)Z_Lu_h and error matrix H-Z_L^T F[L,L]^(-1)Z_L. This is a positive semidefinite error matrix, not an asymptotic replacement.

Putting h=G^(1/2)v makes the denominator vector unit exactly when ||v||=1. Substitution gives the G^(-1/2) factors on both sides of (12), with the correct order. It proves 0<=alpha_N<=1.

Here is a direct check of the strongest exact statement (13a). Let O_g and O_D be the actual orthonormal good and denominator frames, so O_g^T O_D=0. Write

    D_g=(I-Pi_L)O_g,   D_a=(I-Pi_L)O_D.

The retained Gram blocks are

    O_g^T Pi_L O_g=I-D_g^T D_g,
    O_g^T Pi_L O_D=-D_g^T D_a,
    O_D^T Pi_L O_D=I-D_a^T D_a.

Taking the Schur complement of the first block, and using ||D_g||<=eta_N<1, gives

    T_D^T T_D
      =I-D_a^T D_a-D_a^T D_g(I-D_g^T D_g)^(-1)D_g^T D_a
      =I-D_a^T(I-D_g D_g^T)^(-1)D_a.

The inverse acts on the ambient energy space and exists even if the good frame is rectangular. Therefore

    gamma_N^2=1-||(I-D_gD_g^T)^(-1/2)D_a||^2.

Since ||D_a||=alpha_N and I<=(I-D_gD_g^T)^(-1)<=(1-eta_N^2)^(-1)I, both inequalities in (13) follow, including the zero lower cutoff. This also proves why alpha_N<sqrt(1-eta_N^2) is only a sufficient criterion in general. The exact weighted-tail norm gives the necessary-and-sufficient criterion.

On a data subspace one uses the inherited G^(-1) norm, or equivalently an orthonormal subspace in the v coordinates above. The same Gram argument then gives controlled independent columns on that subspace. No existence of such a quantitatively controlled nonzero subspace is asserted by this note.

## 4. Dual formulation and singular cases

The good frame has dimension n-1-D-k_0 and injects into the retained prefix because eta_N<1. Its orthogonality equations therefore have exactly that rank in the n+1 dimensional retained space. Thus dim A_L=D+k_0+2. Expanding the energy pairing with Rcal(u_g) cancels the single F factor and leaves precisely the moment equations (15), with both true Q factors and the actual two-component measure.

For fixed h, the supremum of the normalized squared pairing over A_L is the squared norm of the projection of f_h onto that subspace. In an orthonormal retained basis orthogonal to the good frame this is ||T_D G^(-1/2)h||^2. Taking the data Rayleigh quotient proves (16).

The constraints in (17), for all h', are exactly

    T_D^T y=G^(-1/2)h.

If T_D has full column rank, the minimum ||y||^2 is the inverse Gram quadratic form in G^(-1/2)h; its largest Rayleigh quotient is gamma_N^(-2). If T_D is rank deficient, some nonzero right-hand side is infeasible and the supremum is infinite. Thus (18) is valid in both cases, with the stated convention. These are exact minimum-energy formulas, not a proof of the missing lower bound.

## 5. True-factor jets and the coefficient right inverse

The gap |x_j-xi_l|>=1/21 implies that on |z-x_j|<=1/(84N), each normalized true factor differs from one by at most 1/(4N). For at most N factors, the forward product is bounded by exp(1/4), and the inverse product by (1-1/(4N))^(-N)<=exp(1/2). Cauchy's estimate, after changing to s=(z-x_j)/r_j, gives coefficients at most exp(1/2)(84N r_j)^k for both the normalized factor and its inverse. Summing the norms of the truncated shift operators proves (19), uniformly through the actual multiplicity nu. At the actual radii r_j=O(N log N) and nu=O(sqrt(N)), this is exp(O(sqrt(N)log N)).

The exact normalized map Lambda_a^(-1)J is local multiplication by Q_a/Q_a(x_j), followed by scalar multiplier evaluation. Invert the former with (19), then apply the already reviewed global Hermite interpolation inverse in the coefficient basis (z/N^2)^k. The interpolant has degree <D and fits in the first-channel domain for all sufficiently large indices under discussion. The resulting right inverse has norm exp(O(D log N)). This proof retains the signed, node-dependent scalars Q_a(x_j)/d_j in Lambda_a.

For unnormalized data h the constructed coefficient vector is Rhat Lambda_a^(-1)h. Comparing its actual H_sc energy with the minimum proves exactly

    G^(-1)<=Lambda_a^(-T) Rhat^T H_sc Rhat Lambda_a^(-1).

There is no bound on H_sc in this formula, and none is silently supplied by the coefficient inverse bound.

## 6. Scalar approximation and the remaining degree obstruction

Only the first channel changes when R is replaced by a scalar approximant. Since all scalar functions of K commute with F(K), the difference norm is bounded by epsilon times the actual first-channel norm before R multiplication. This proves (23), including its matrix-measure setting; no scalarization of that measure is used.

The full angle estimate, and R>=2/n, imply chi_N<=n/(2delta_N). The independently reviewed square-root-cutoff theorem supplies the required full angle on the actual full pair at that same cutoff. It would not be legitimate to use an angle known only on a divisible subfamily.

The resulting surrogate is generally outside the exact degree caps in (9). The note now correctly writes the low-factor excess as ell_a+O(1), which is O(sqrt(n)) only at the new cutoff; multiplication by a degree-m approximant adds another m. No weighted projection bound follows from simply discarding these coefficients. Consequently this scalar estimate and the coefficient right inverse do not prove alpha_N<1.

## 7. Final scope

The stable note correctly presents an exact dual characterization and a separate sufficient approximation criterion. All energy and data normalizations, finite dimensions, singular cases, and subspace qualifications pass. It identifies the actual remaining analytic problem but does not solve it. Physical S, cardinal amplitudes, and retained F factors are still present in the downstream map. No endpoint remainder estimate or irrationality conclusion is obtained from these variational identities alone.
