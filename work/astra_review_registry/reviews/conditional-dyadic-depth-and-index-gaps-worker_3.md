> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: Conditional dyadic approximation depth and exponential index gaps

Reviewer: worker_3
Verdict: approved
Candidate SHA256: 29db0d226d2991d949f69ee25fe70b23795e8c56ff01ad7459c5dacae39f7ba8

Approved for the exact conditional statement and scope of this payload. This verdict uses the completed independent mathematical audit recorded in work/astra_20260929/worker_3/note_000013.md, the payload-identity computation in note_000015.md, and the preserved review in note_000019.md. The identity check established that the assigned SHA-256 hashes the 5388-byte candidate body beginning at line 7; the enclosing 5581-byte file has a different hash because it includes registry metadata.

I checked the combination of the assumed denominator lower bounds, the substitution for c_n, and the comparison with the assumed approximation error. The stated bounds 0<δ<1 are valid. Shrinkage implies eventual log(q_n E_n)<0, which suffices for the necessary depth deduction without assuming a rate of convergence. With only the stated o(n) remainder, one obtains the eventual depth bound with an arbitrary fixed ε-loss, 0<ε<δ. The stronger depth bound with logarithmic loss requires the additional remainder control specified in the candidate; it does not follow from o(n) alone.

I checked the gap deduction using the ultrametric inequality. For two distinct indices n<m approaching the same root α, v₂(m−n)≥min(v₂(n−α),v₂(m−α)). Thus a real lower bound t on this integral valuation yields m−n≥2^{ceil(t)}, with any weaker rounded bound also valid. This proves the claimed separation after the depth substitution. For the logarithmic-loss refinement, δx−K log(x+2) is eventually increasing, justifying evaluation at the smaller index.

The depth conditions are necessary conditions for shrinkage. The gap bounds remain compatible with infinitely many sufficiently sparse surviving indices; the candidate’s sparse simple-root example correctly demonstrates this limitation.

This review certifies these conditional deductions only. It does not certify that the actual endpoint family satisfies the assumed reduced-denominator bounds, establish a shrinking subsequence, determine whether the specific exceptional root is algebraic or transcendental, or bound its approximation depth. It supplies no irrationality proof for e+π.