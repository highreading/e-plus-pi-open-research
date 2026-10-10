> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root review of the actual mixed boundary-Schur reduction

Date: 2026-09-13. Verdict: PASS without correction.

Reviewed `raw_mixed_channel_boundary_schur_reduction.md` in full. The
actual mixed cross-angle estimate remains unproved; all dimension
improvements depending on it are correctly marked conditional.

The two polynomial channel spaces have the supported positive-weight
angle claimed in (3). The actual ratio acts only on the first space,
and elimination of the second block gives exactly S=V_aᵀPRV_a.
This cross matrix is not silently replaced by its symmetric part.

For the scalar Krylov basis of the second channel, the positive measure
gives the one-step Jacobi recurrence with one residual boundary vector.
Multiplying (x−K)V_b=V_b(x−J_b)−beta_b eta_b e_bᵀ by the full and
compressed inverses gives (7) with a positive sign. The last-row
tridiagonal cofactor formula (8), including the empty products and
leading principal determinant convention, checks. The zero-boundary
case is covered without needing a next positive-norm polynomial.

Decomposing V_a=PV_a+V_b C and substituting the exact Stieltjes
representation of R gives S=S_+−UVᵀ with precisely the columns in
(11). The determinant lemma and Woodbury inverse have the displayed
normalizations. The actual cross-channel spectral measure is retained
in C. Different left and right boundary vectors mean no positive
semidefinite inference for UVᵀ is justified; the note makes none.

I recomputed the displacement directly. The two external first-channel
boundary terms arise from replacing K V_a by V_a J_a+beta_a eta_a e_aᵀ;
the other two terms are V_aᵀ[K,P]R V_a. Since R commutes with K,
this gives all four signs and orientations of (15), hence displacement
rank at most four. The diagonal of the transformed matrix is not
determined by off-diagonal division in (16), as the note states.

For the full test construction, p_h=PV_a S^(−T)j_h is orthogonal to
the entire second channel and has the exact dual pairing (19) against
the first channel. With
M=G_Z^(−1/2) S H_R^(−1/2), the identity

    S⁻¹G_ZS^(−T)=H_R^(−1/2)M⁻¹M^(−T)H_R^(−1/2)

proves the norm estimate (21). The normalized matrix M is indeed the
cross Gram of the independently orthonormalized PV_a and RV_a spaces.
The previously proved full-channel angle controls a different
projection and cannot be substituted for this singular value.

The sufficient bound (22) implies the stated conservative estimate
gamma_mix≥(2/n)A_n⁻² tau: factor S through S_+^(1/2), use
S_+≥(2/n)A_n⁻²I, and use G_Z,H_R≤I in the two outside inverse
square roots. This is a lower singular-value argument, not a claim
that a nonsymmetric matrix has ordered positive eigenvalues.

Finally imposing the two top-degree conditions costs at most t_a+t_b
linear conditions on the data. On their kernel the actual test lies
in the retained energy prefix. Its exact full zero-data orthogonality
therefore implies orthogonality to the retained good image as well.
The pairing E_a(h) and norm bound gamma_mix⁻¹sqrt(E_a(h)), together
with E_full(h)≤E_a(h), prove the stated restricted retained lower
bound. The resulting O(sqrt(n)) count is conditional on gamma_mix>0;
the existing unconditional count is unchanged. The physical cardinal
and g_l factors remain in their original final maps.
