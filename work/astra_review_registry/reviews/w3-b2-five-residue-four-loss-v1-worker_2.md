> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: Exact five-adic numerator loss for the b=2 endpoint on indices congruent to four modulo five beyond n=9

Reviewer: worker_2
Verdict: approved
Candidate SHA256: e08cc00ef7c40a2bdfda278145fa8330dbac4fbc58b3723fe44b76131acf8e43

Approved for the exact scoped statement in this immutable payload. The independent integrity check recorded in worker_2/note_000156.md confirms that candidate bytes [235,11129) have the assigned payload SHA-256; the whole-file hash also matches the reading ledger.

I compared the complete candidate with the independent audit preserved in worker_2/notes 000147–000149 and the polynomial derivation in note_000153.md. The newly displayed polynomial reductions agree modulo 25 with my independently derived formulas. The coefficientwise calculation passed all twelve polynomial checks, including the constant exponential contribution F_n≡20; the subsequent candidate-table verification passed all 32 exact checks. These calculations support the finite algebra within the uniform proof, rather than extrapolating a theorem from sampled indices.

I checked the division-free normalization, falling-factorial truncation estimates, and singular exponential boundary contribution. The estimates remain valid with no upper bound on v_5((n+1)/5); they do not invert that possibly nonunit quantity. Comparison with main/note_000188.md and the published cancellation identity confirms the complete numerator decomposition. The audited moment estimate puts the omitted contribution in 125Z_5 throughout n≥14, n≡4 mod5, so it does not affect the claimed congruence modulo 25.

The preserved independent reconstructions used the original Rodrigues polynomials and complete rational contractions at n=14,19,24,29,34. Each gave Z_n≡20 mod25, with moment valuations 3,5,8,10,12 respectively. They were not repeated for this review. The separately reconstructed n=9 has exponential contribution 20 and moment contribution 5 modulo 25, yielding Z_9≡50 mod125. It therefore remains outside the approved theorem; its moment cannot be omitted.

The source dependencies used are the published b2-two-chart-actual-denominator-identities, payload ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d, for the rational endpoint normalization, and main-b2-five-adic-residue-four-cancellation-v1, payload b123168c159b9a62d863ee40ffdae485533f2229e99c368b6cd671e04f321519, for the cancellation identity and v_5(D_n)=v_5(n+1), hence D_n≠0. No large-prime ideal theorem was applied at five.

Finally, with f_n=2^n/(n!)^2 and Z_n=X_n/[f_n(n+1)], the proved congruence gives v_5(Z_n)=1. Thus v_5(X_n/D_n)=1−2v_5(n!), and the positive reduced denominator q_n=den(X_n/D_n) satisfies v_5(q_n)=2v_5(n!)−1 on the stated domain. This verifies the normalization and denominator conclusion directly. Approval does not cover the separate whole-family obstruction synthesis, growing-degree behavior, or any assertion deciding the rationality of e+pi.