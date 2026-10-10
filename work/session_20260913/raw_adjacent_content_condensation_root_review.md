> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root review of adjacent high-content condensation

Date: 2026-09-13. Reviewed `raw_adjacent_high_content_condensation.md`.

The original determinant identities pass. Laplace expansion along
the single lost row for H_n, and along the three new rows for
H_(n+1), gives the common lower divisor with the correct direction.
Each complementary minor is among the extended shared-core minors.
The nonzero contents follow from the characteristic-zero ranks.

The old shared core has at least 2n-2 independent rows modulo every
stated prime. A unit minor of that size therefore exists. The row
and column counts after selecting it are respectively 2 by 4 and
4 by 6. The bordered determinants equal the unit pivot determinant
times the corresponding Schur entries; the k-by-k Sylvester formula
has factor Delta^(k-1), as stated. Integral invertible operations
give equality of the maximal determinantal ideals after removing
the unit block, so the exact prime-power content equations follow.
The assertions I_1(U)=R and I_3(V)=R follow from the previously
proved ranks of H_n and H_(n+1). The empty n=1 pivot is legitimate.

The conditional two-new-column elimination has the correct residual
rows r-s D^(-1)W and b-d_3 D^(-1)W. Its 2-by-2 pivot must be a
unit for that particular simplification. The note does not infer
that unit status from total rank, and does not reverse its lower
divisibility into an upper estimate.

A subsequent root theorem, proved in
`raw_shared_core_large_prime_saturation.md` and checked in
`raw_shared_core_module_independent_review.md`, now closes the
large-prime zeta_n obstruction left open by the original note:
v_p(zeta_n)=0 for all p>3n. In the deficient old-core chart it
forces at least one of the two new-column rho entries to be a
unit. Thus a full shared-row pivot for the next matrix always
exists, possibly using a new column. It still does not imply
the unit two-new-column pivot needed for the final two-form
comparison, or control the full high content D_n.
