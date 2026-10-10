> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root review of the boundary-free moment and spectral formulation

Date: 2026-09-13. Reviewed source: raw_boundary_free_moment_intertwiner.md,
including its projection and finite-Fourier additions. Result: the
substantive statements pass, with one short-interval correction already
incorporated by the author.

The direct composition of J² cancels both the fourth and third derivative
terms against the stated fourth-order operator. Subtracting J leaves
D x(x−1)D+x²−x+1. Its polynomial boundary form is zero at0 and1.
The scaling E_k=k!F_k/(a_1...a_k) gives exactly the symmetric row ladder;
no asymptotic equality is used. The shifted Legendre column matrix has
only distance-two couplings because its potential is3/4+(x−1/2)².

Every exterior row and column in the finite Sylvester equation is
present. The originally stated column boundary norm omitted a factor
for intervals of length1,2,3: a column can have two exterior couplings.
The corrected uniform bound is sqrt2 sup t_l t_(l+1); the sharper bound
holds for intervals of length at least4. This changes no claimed
concentration result, since none was inferred from that bound.

The row upper bound uses the compression of J², including paths that
leave and return to the interval. I checked the elementary inequality
for a_k, the two exceptional rows, and the rational constant361/324.
The resulting9/8 and b+7/4 bounds are valid. The Sylvester gap is
m(m+1)−2n, and the semigroup integral gives the stated operator and
Frobenius bounds. The two sign conjugations give a symmetric positive
definite matrix with nonpositive off-diagonal entries, so its inverse
is entrywise nonnegative. This does not give the forcing a sign.

The infinite operator is defined by a self-adjoint diagonal Legendre
operator plus a bounded real potential. This fixes its domain and
compact resolvent explicitly. The disjoint min-max intervals prove
simplicity and alternating reflection parity. The off-mode bound
1/(16l−1) follows by inverting the diagonal complement after centering
the potential at7/8. The uniform projection bound1/(16d+15) also passes:
the two cross projections solve separated Sylvester equations with
gap2d+15/8 and perturbation norm1/8. The norm of the projection difference
is the maximum of the two cross-projection norms. The unbounded
semigroup on its high spectral subspace has the required uniform decay.

The row recurrence has a nonzero leading coefficient at every index;
two initial values determine it. Reflection reduces this to one
nonzero amplitude in each branch. Irreducibility of each parity
Jacobi block proves nonzero amplitude without an asymptotic estimate.
The infinite spectral pairing is absolutely convergent for each fixed
row by Cauchy-Schwarz; it is not finitely truncated by polynomial degree.

Finally u=2x−1 gives the prolate operator with c=1/2 and the two stated
eigenvalue shifts. The finite Fourier commutation identity checks by
differentiating its kernel. For clarity, a smooth kernel image belongs
to the natural Legendre domain because integration by parts gives
lambda_j <g,phi_j>=<A0g,phi_j>, and Parseval bounds the sum of the
squared left sides. Its endpoint factors vanish. Polynomials form a
graph core, so boundedness of the Fourier operator and closedness of
the differential operator extend the identity to the full domain.
Injectivity follows from analyticity and polynomial density, giving
nonzero Fourier eigenvalues. Both central-amplitude formulas retain
the Jacobian and sqrt2 normalization. Direct multiplication gives the
concentration eigenvalue |mu_l|²/(4pi), as claimed.

This review validates the identities, domains and bounds. It does not
supply a bound for growing-index spectral weights, coherent boundary
forcing, the raw norm, or the primitive denominator. Those remain
separate mathematical tasks.
