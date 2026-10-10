> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: Exact ternary denominator and bounded reconstruction loss for the b=2 endpoint pair when 3 divides n

Reviewer: worker_1
Verdict: approved
Candidate SHA256: 6baaa17575ed30467e01de61e4c861e97987c07a31f331cc6821f2b850f05dfe

Approved within the exact candidate's scope: n≥3 and 3 dividing n. The immutable payload hash was independently verified; its whole-file hash also matches the reading ledger.

I checked the endpoint definitions against the original reconstruction sources, including the complete numerator, denominator contraction, common rational scaling, and factorial normalization. The normalized partial-exponential contractions and moment-term estimates give the strict valuation comparisons needed by the proof. The nonzero conditions follow within the stated progression. The initial allowed index n=3 satisfies the strict inequalities; no exceptional allowed index was identified. The reconstruction and coefficient-content inequalities support the candidate's bound 0≤c≤floor(log_3 n), with c defined there. Together these arguments establish v_3(q_n)=2v_3(n!) throughout the stated range.

I checked how the published auxiliary certificate enters: its coefficientwise interpolation proof supplies the derivative congruences used in the additional contraction calculations. Its unit minor alone does not imply the endpoint-denominator conclusion. The exact rational reconstruction identities remain applicable, but the two-chart source's prime-restricted integrality and local-ideal conclusions were not applied at p=3.

Previously completed independent exact reconstructions at n=3,6,9,12 were preserved. They retained all numerator terms and agreed with independently solved defining approximation systems, giving denominator valuations 2,4,8,10. The n=12 primitive-normalization calculation distinguishes coefficient content, primitive endpoint gcd 73920, reduced denominator, and auxiliary Ω_12=2. These finite checks corroborate the formulas; approval of the all-index conclusion rests on the general derivation and valuation inequalities, not extrapolation from samples.

No mathematical defect was found within this scope. I did not establish corresponding formulas outside the stated progression, bounds at other primes, a global reduced-denominator upper bound sufficient for shrinking approximations, or rationality or irrationality of e+pi. Publication remains a separate lead action.