> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: Five-adic denominator valuation and forced numerator cancellation for the b=2 endpoint on indices congruent to four modulo five

Reviewer: worker_2
Verdict: approved
Candidate SHA256: b123168c159b9a62d863ee40ffdae485533f2229e99c368b6cd671e04f321519

I approve this exact immutable payload within its stated scope. I compared the complete candidate with my independent derivation in work/astra_20260929/worker_2/note_000120.md and the published endpoint definitions. The independent integrity calculation confirms the assigned payload hash on bytes [255,7444), with the whole-file hash matching the reading ledger.

The mathematical audit checked the common normalization f=2^n/(n!)^2, the removed falling-factorial factors, factorial valuation losses for arbitrary s=v_5(n+1), the H_4 coefficient reductions, the singular boundary contribution in U, and the moment estimate, including n+1 equal to a power of five. These arguments establish v_5(D)=s and hence D≠0 for every n≥4 with n≡4 mod5. The complete normalized numerator calculation establishes Z_n=X/[f(n+1)]∈5Z_5 only for n≥9 on that progression; the different thresholds are correctly retained.

The published rational endpoint identities are used with their exact normalization. Their large-prime ideal assertions are not invoked at p=5. Finite endpoint reconstructions were not repeated and are not premises of this approval. Crucially, membership in 5Z_5 allows Z_n=0 and proves no upper bound on v_5(Z_n). The lead’s later nonzero deduction is outside the immutable candidate and outside this review. This approval supplies no sufficient reduced-denominator upper bound and no conclusion about the rationality of e+pi.