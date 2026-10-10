> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: Exact projection, complete remainder, and error transfer for each fixed exponential degree

Reviewer: worker_3
Verdict: approved
Candidate SHA256: b8c2e619d3f2287876530b229be959d872aadf8b04c5df3b3cef4ee8ec7c8245

I approve this exact scoped payload following the completed independent audit. Its identity was verified: the 15183-byte payload beginning at byte 222 of the 15405-byte candidate file has the assigned SHA-256. The preserved evidence is work/astra_20260929/worker_3/calculation_000071.py and notes 000071–000073; the sign clarification in note_000072.md supersedes the earlier wording in note_000071.md.

I checked the original Taylor vanishing equations and endpoint matching, the projection indices obtained through bilinear orthogonality with explicitly nonzero norms, and the complete evaluated remainder retaining both Taylor tails. The reference normalizations, factorial indices, endpoint determinant, and additional remainder cofactor have consistent signs under the stated row order. These checks used the original unequal_degree_hp_attempt.md derivation and comparison with the published matched-endpoint transfer claim. Eventual nonvanishing of the endpoint determinant also establishes the required reduced rank.

I checked the qualitative microscopic reference limit, the normalized analytic factors, the nonzero limiting coefficient determinants, and the sufficient coarse bound for the additional remainder cofactor. The factorial-transform reasoning agrees with the published fixed-size-factorial-determinant-finite-jet-factorization-v1. The ordinary Padé prefactor is the separately published input worker3-ordinary-pade-prefactor-v1. The candidate supplies its qualitative reference estimates and coarse cofactor control internally; it does not require the newer microscopic-rate, sharper-cofactor, or leading-cofactor refinements.

The independent exact reconstruction passed all assertions for 18 pairs with 1≤n≤7 and 1≤b≤min(3,n), including 121 bilinear orthogonality identities, original Taylor equations, endpoint matching, full and reduced ranks, complete remainder coefficients, and determinant signs. These finite computations verify the tested identities; the asymptotic argument was audited separately. The case n=b=1 has Y=0, consistent with the theorem's necessary qualification that endpoint nonvanishing is eventual.

The sign convention is consistent. Writing R=B exp(z)+CF−A_minus=A_plus+B exp(z)+CF requires A_plus=−A_minus. Consequently A_minus(1)/Y=−A_plus(1)/Y is the same rational approximant in both conventions, and R(1)/Y=e+pi−A_minus(1)/Y is the same signed error. For each fixed b, the resulting asymptotic is R(1)/Y=(−1)^n[4pi/(1+sqrt(2))^(b+1)](1+sqrt(2))^(−2n)(1+o(1)).

No candidate-specific mathematical defect remains unresolved in this scope. This approval excludes uniformity for growing b, endpoint nonvanishing at every finite index, sufficient bounds for actual reduced denominators, and any rationality or irrationality conclusion. It supplies no approval of w3-cofactor-leading-v1 or any other separate candidate.