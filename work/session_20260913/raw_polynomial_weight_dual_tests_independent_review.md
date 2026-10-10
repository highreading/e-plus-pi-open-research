> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the polynomial-weight denominator dual tests

Date: 2026-09-13. Reviewer: audit_computations.
Reviewed source: `raw_polynomial_weight_denominator_dual_tests.md`, Sections 1--5.

**PASS.** No mathematical correction identified. This review checks the
new exact scalar correction and its stated scope, not the unresolved
mixed-channel conclusion.

1. The measure identity is exact:
   `mu/R=F_b R L_a^2 Sigma_aa=F_a L_a^2 Sigma_aa`.
   Thus the new weight is a positive polynomial modification on the
   actual row spectrum. The Gram inequalities follow from `1<=1/R<=n/2`.
   The compression `C_a=H_a^{-1}H_tilde` is selfadjoint in the `H_a`
   inner product; the note correctly does not claim Euclidean symmetry.

2. The coefficient formula `w=H_tilde^{-1}J_a^TG_a^{-1}h` follows by
   inverting that compression. The relabeled data are precisely
   `G_tilde G_a^{-1}h`, whose normalized matrix is positive definite
   with eigenvalues in `[2/n,1]`. In particular the data map is
   invertible and `w` is not silently asserted to have original data `h`.

3. With the stated fixed channel sign, the pairing of `L_a w` with
   `R L_a v` is the `chi` pairing. This proves first-channel zero-data
   orthogonality for every polynomial in the full stated degree space,
   hence in particular for every first-channel good multiplier. The
   two-data pairing is exactly `h^TG_a^{-1}h'`, without missing factors
   `Q_a(x_j)`, `d_j`, or local jet radii: all are retained inside `J_a`.

4. The improved test norm is valid. The exact identity
   `||w||_chi^2=h^TG_a^{-1}G_tilde G_a^{-1}h<=E_a(h)` uses a single
   positive Gram comparison. A further factor `1/R<=n/2` gives
   `||L_a w||_F^2<=(n/2)E_a`, and therefore the retained lower bound
   `sqrt(2/n)` follows from the variational projection formula. The
   same positive pairing is with the original `mu` extremizer, as stated.

5. Since `h -> w` is linear and injective, imposing the top polynomial
   coefficients costs at most the displayed `t_a=O(sqrt(n))`
   dimensions at the fixed square-root cutoff. Intersection with `H_0`
   loses at most its already established `k_0` dimensions. Neither
   operation is presented as controlling the other-channel pairing.

6. The cross matrix (11) has the correct transpose orientation: the
   row of pairings associated with data `h` is `h^T B_cross`.
   The two measures in (12) differ by precisely `F_b-F_a`. The
   telescoping identity (13) checks term by term, has degree `h-1`
   for `h>0`, and has positive coefficients when expressed in
   `H_0=(2n+1)-t`. The empty-high-factor case is correctly zero.

7. The scope restriction is essential and correct: polynomial positivity
   of that change does not control the actual cross-channel projection.
   The note makes no assertion of full mixed retained rank or of a
   physical endpoint bound. No experiment was used in this review.

A complementary exact boundary and rank-four displacement reduction
for the remaining mixed operator is saved separately in
`raw_mixed_channel_boundary_schur_reduction.md`; that reduction itself
still leaves a genuine lower-bound problem.
