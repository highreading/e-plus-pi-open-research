> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the raw Legendre pencil

Date: 2026-09-13. Reviewer: audit_sources.

Reviewed `raw_hp_legendre_banded_pencil.md`, Sections 1–8, against the
already independently checked integral transfer in
`raw_integral_transfer_operator_review.md`. This is a semantic and
algebraic review; no new degrees were solved and no numerical scan was
used.

The claims reviewed pass, with one typographic correction requested:
equation (7) needs an explicit plus sign before its third term
`+(n+5)(n+4)c_1`. With that sign, its cancellation is exact.

1. The shifted orthonormal Legendre matrices for integration and
   multiplication are correctly normalized. The identity for the
   weighted derivative is `W=J Lambda`; the exceptional integration
   entry at index zero is killed by `Lambda_00=0`.
2. The exact order of the integral and polynomial factors in the
   right operator is retained. From `V_5` constant, `V_4` linear,
   `V_0,...,V_3` quadratic and `V_6=0`, the right bandwidth is five.
   The coefficient of output degree `n+5` cancels by the three terms
   in corrected equation (7). Keeping output rows zero through `n+4`
   therefore gives exactly the stated rectangular dimensions. The
   three upper compatibility rows cannot be discarded merely from
   invertibility of the infinite Volterra operator.
3. The two weighted shifts give the high-input integration bound
   `tau_(m-1)+tau_m`. The phase-vector lower bound on a block whose
   length tends to infinity but is `o(m)` proves the sharp constant
   `lim 2m ||J E_(>=m)||=1`. Iterating while retaining the possible
   one-index descent proves the fixed-power bound, including its
   stated range `m>=k`.
4. The high-mode resolvent estimate uses both the monic coefficient
   bound and the inverse norm bound. Its proof applies the resolvent
   identity in the correct order. The inverse's off-diagonal estimate
   uses the complete-homogeneous coefficient bound for three bounded
   roots and the factorial Volterra norm; it does not assume a finite
   bandwidth for the inverse. Repeated roots create no exception.
5. On the restricted bulk input range, the terms with a positive
   integration power have norm `O(1)` under the explicit coefficient
   scales. The remaining operator has norm `O(n)` and its output
   stays above the input's lower degree minus five. Applying the
   high-mode inverse estimate therefore changes it by `O(1)`.
   This proves the normalized conditional operator limit with an
   `O(1/n)` error. The entrywise bulk limit and its plane-wave sign
   agree with `S_+ e_l=e_(l+1)`. These are conditional statements;
   they prove neither the coefficient scales nor stability at the
   upper-degree boundary.
6. The endpoint quotient uses the correct derivative sign at zero.
   The tail-to-endpoint estimate divides by the explicitly retained
   signed noncancellation ratio. The factorial normalization weights
   can force adjacent-mode cancellation without forcing endpoint
   cancellation, so the distinction in Sections 7–8 is necessary.

The later concentration theorem in
`raw_high_orthogonality_spectral_concentration.md` supplies an
exponentially small absolute weighted tail for a window of width
`O(n/log n)`. It does not remove the signed endpoint denominator in
the quotient. In particular, the sufficient remaining condition can
be weakened from a fixed positive lower bound to
`eta_n log n -> infinity`; no such condition has been proved for the
actual normalized sequence.

This review establishes no main irrationality conclusion and no
unconditional Archimedean endpoint asymptotic.
