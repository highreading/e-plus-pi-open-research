> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: Ternary unit numerator and conditional reduced-denominator lower bound for indices congruent to one modulo three

Reviewer: worker_2
Verdict: approved
Candidate SHA256: 5268f1e9d2b38f15e4b00b9918dd6c98f6f57dcac0b6a75fc046e5bbb7738082

Approved for the exact scoped conditional statement. I independently compared the complete candidate with the preserved derivation in work/astra_20260929/worker_2/note_000073.md and the published b2-two-chart-actual-denominator-identities source. The completed mathematical audit is recorded in step 96, and the independent integrity check in step 97 confirms that candidate bytes [244,9172) have the assigned payload SHA-256. The audited source files also match their recorded hashes.

I checked the factorial normalization f=2^n/(n!)^2, the complete normalized numerator N=X/f, and all three surviving U-contraction contributions, including the d=n+1 boundary contribution. The normalized moment contributions have ternary valuation at least one throughout n≥4 with n≡1 mod3; the strict inequality includes n=4. The use of floor(log_3(n+1)) is valid on this progression. These checks retain the complete numerator and establish N≡1 mod3 and D≡0 mod3. The rational endpoint identities are applicable here; the separate large-prime chart ideal theorem is not being applied at p=3.

Whenever D≠0, the actual rational endpoint ratio is X/D. Since v_3(N)=0 and v_3(f)=−2v_3(n!), ordinary reduction of this rational number gives v_3(q)=2v_3(n!)+v_3(D)≥2v_3(n!)+1 for its positive reduced denominator q. No primitive-content assumption is required for this deduction.

This approval does not establish D≠0 at every index or import the separate eventual-nonvanishing candidate. The author's n=28 example was not independently recomputed and is not a premise of the proof. No denominator upper bound, sufficient shrinking subsequence, or conclusion concerning the rationality of e+pi is certified.