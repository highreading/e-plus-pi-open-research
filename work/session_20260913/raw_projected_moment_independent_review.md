> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the integrated n=4 moment counterexample

Date: 2026-09-13. Reviewed Sections 1–3 of
`raw_projected_moment_positivity_attempt.md`. The counterexample and
its row/column sign obstruction pass. No additional degree was tested.

The Rodrigues integration-by-parts formula has positive sign: the
factor (-1)^l from integration by parts cancels that from (t-1)^l.
For k>l the derivative F_k^(l) is strictly positive on (0,1), since
the monic positive coefficient at degree k survives. Hence all entries
of the actual projected moment matrix are indeed positive.

I independently reconstructed F5,F6,F7 from the monic raw three-term
recurrence, applied the Borel factorials, and integrated each against
the explicit shifted-Legendre coefficients. This reproduces all 15
displayed entries of the n=4 matrix exactly. I then verified the two
opposite maximal minors 012 and 013 and all five minors used by the
triangle certificate. The exact certificate is
`raw_projected_moment_independent_checks.json`.

The sign-reorientation argument is correct. For an r by (r+2) matrix,
row signs contribute the same product to every maximal minor. A minor
omitting columns i,j acquires, apart from one common product, the
factor c_i c_j. Therefore a possible common final sign requires
e_ij=tau c_i c_j, and all triangle products must equal the same tau.
The two verified triangles have signs -1 and +1, contradicting this
necessary condition. The argument does not require an exhaustive
enumeration of sign patterns.

This establishes a finite obstruction to maximal-minor sign
regularity after the actual integration and shifted-Legendre
projection. It is distinct from an opposite-sign summand in a
Cauchy–Binet expansion. It does not exclude a theorem beyond an
unspecified threshold, an eventual subsequence, arbitrary column
permutations, or a general non-diagonal basis change. These limitations
are correctly retained in the original note.
