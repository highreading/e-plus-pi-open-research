> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Plateau propagation report

Original author derivation; no independent audit, numerical scan, or replay. CENTER_CONTIGUOUS_RESEARCH.md and its exact integer zero test remain unchanged.

The new note constructs a closed 31-coordinate rational input state: three coefficients of exp(z)q^n and fourteen coefficients of each of the TWO actual forcing functions q^n D^n h. The forcing window uses offsets -2 through 11. Three forward eliminations close its update; backward elimination at the singular extreme factors is never used.

A common transition denominator is q0=(n+1)d8*d9*d10, where dj=(n+j+1)(n+j+2)(n+j+3)(n+j+4)(2n+j). It is positive throughout n>=b+16. Its degree is 16 and the cleared transition numerator has degree at most 17.

For fixed b,m the UNREDUCED actual B-only contractions A_n,H_n become degree-2b homogeneous polynomials in that state after multiplication by the explicitly listed positive factor B(n)^(2b). The allocated monomial-state size is exactly N=binom(2b+30,30); no minimality is asserted.

A finite signed-minor elimination on paired output rows produces one scalar recurrence annihilating BOTH contractions, with order d<=2N and coefficients independent of the proposed constant rational r. In original normalization it is

    sum_(j=0)^d c_j(n) B(n+j)^(2b)
                    (H_(n+j)-r A_(n+j))=0.

Every factor and row needed to construct this recurrence is specified in the main note. With e=40(b+1)^2, the nonzero leading polynomial satisfies

    deg c_d <= K=d(e+34bd)+32bd.

There are therefore at most K admissible exceptional starting indices. Beyond the last exceptional index, d consecutive zeros imply a fixed-b,m tail identity. This is genuine finite propagation, conditional only on absence of subsequent leading-coefficient zeros; it does not assert that the tail identity is impossible.

For b=floor(log n), m=floor((b-1)/2), the retained large-n admissibility n>=2^96 applies. The state and exceptional-count bounds grow polynomially in b, whereas the blocks have exponential length. The remaining issues are control of the locations of the leading-polynomial roots and exclusion of a constant-center identity for the actual fixed-b family, or a compatible contradiction across changing dimensions. Neither has been obtained. A fixed-b continuation past a boundary is not the prescribed variable-b sequence.

Thus infinite nonstabilization remains open. The deliverable supplies an explicit state size, denominator ledger, r-independent elimination, and exceptional-set bound rather than abstract holonomic closure. Contact/lift normality retains its provisional status; reduced denominators and primewise normalization are not addressed.

Both files require controller-confirmed save and subsequent read-back before operational completion is reported.
