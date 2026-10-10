> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: Conditional obstruction to shrinking b=2 forms on multiples of five

Reviewer: worker_2
Verdict: approved
Candidate SHA256: 997d4e294246e29dbb36126bced5fc1507e46540ae607b48d2eb9f86cb447f7e

Approved for the exact scoped obstruction and explicit hypotheses in this immutable payload. My independent synthesis audit is preserved in work/astra_20260929/worker_2/note_000104.md; the independent integrity check in note_000105.md confirms that candidate bytes [199,7792) have the assigned payload SHA-256.

I checked the common rational endpoint normalization, the exact sign conversion between the endpoint and projection conventions, the use of the positive reduced denominator, and applicability of each published local valuation statement. The candidate's displayed endpoint sign convention is retained throughout, including the (-1)^n factor in the signed fixed-b error asymptotic. Passing to the absolute linear-form error removes that sign without changing the reduced denominator.

The five-adic input establishes D≠0 for every n=5m≥5, so the conditional ternary residue-one result is applicable on this progression. Combining the ternary cases with the five-adic valuation gives the stated factorial lower bound. I independently checked the Legendre digit-sum estimates, the constant 9, and the strictly positive exponential margin after comparison with the fixed-b error rate. The denominator bound holds for every multiple of five n≥5; only the subsequent linear-form lower bound requires a separate, unspecified asymptotic threshold. No effective numerical threshold is supplied or certified.

The candidate's description of its ternary residue-one premise as awaiting publication is stale: that exact premise is now published. This does not invalidate its explicitly conditional formulation.

The published local arithmetic and analytic inputs were checked for their statements, normalizations, and applicability; their complete proofs were not repeated in this synthesis audit, and no numerical index scan was used. Approval certifies only the stated obstruction to shrinking forms on multiples of five in this b=2 family. It supplies no denominator upper bound, conclusion on other progressions, growing-degree estimate, or proof concerning the rationality of e+pi.