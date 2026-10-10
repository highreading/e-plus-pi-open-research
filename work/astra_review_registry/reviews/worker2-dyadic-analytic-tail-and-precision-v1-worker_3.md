> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: Coefficientwise dyadic convergence, truncation, and normalization precision for the odd-disk contractions

Reviewer: worker_3
Verdict: approved
Candidate SHA256: 3b220a9384536f55319370fb83bde92220ecf1b8ea1e296bd0a6a6662f42d7ab

Approved within the candidate's stated scope, using the completed independent audit preserved in work/astra_20260929/worker_3/note_000029.md through note_000031.md. The exact 6832-byte payload beginning at byte 237 has the assigned SHA-256. The complete file's different hash, 69d7d01eb3dd684ffbb530f2f76f4530d3b378ab0eace8673d9e1257232e75a7, includes its registry wrapper and is not a content discrepancy.

I checked coefficientwise convergence using Gauss valuations of the falling products, rather than merely pointwise divisibility. On the slope-8 disks, a product of length L has valuation at least floor(L/2)+floor(L/4)+floor(L/8), hence at least 7L/8−3. The resulting outer-kernel bounds 5R/16−6 for H and 5R/16−7 for K tend to infinity and make the omitted R≥55 tails vanish coefficientwise modulo 1024. I also checked the slope-16 inner D-series estimate: the bound floor(j/2) makes j≥20 terms vanish modulo 1024. The argument is uniform over the four specified odd disks. The treatment of the contractions correctly keeps the retained-kernel integrality premise separate from these infinite-tail estimates.

The published worker3-dyadic-finite-coefficient-verification-v1 supplies the finite arithmetic input. Its reconstruction was not repeated during this review; this approval does not replace or enlarge that certificate. Fresh exact normalization checks confirmed H(1)=K(1)=0, A(1)=3, B(1)=10 and the stated normalized coefficient arrays. In particular, the exact identity C(1)=0 justifies division by Y on the disk X=1+8Y; a zero constant coefficient known only modulo 1024 would not suffice.

Precision accounting is correct: division by 4 retains modulus 256, and division by 8 retains modulus 128. The resulting simple-root arguments use only that retained precision. On X=7+8Y, knowing the root coordinate Y modulo 128 determines X modulo 1024, so the exceptional residue 79 modulo 1024 does not restore any unjustified normalized precision.

I found no candidate-specific defect. Approval covers the defined analytic germs, their stated convergence and truncation properties, and normalization and simple-root consequences under the identified finite certificate. It does not certify identification with actual endpoint quantities, actual reduced-denominator bounds, or integer-approximation depth at the exceptional root. Those application dependencies remain separate.