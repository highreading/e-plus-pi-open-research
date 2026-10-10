> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the weaker top-two endpoint criterion

Date: 2026-09-13. Reviewer: audit_sources.

Reviewed all of `raw_weaker_top_two_endpoint_criterion.md`, including
its dependence on the proved broad concentration band and the exact
top-mode normalization. No correction is required.

The squared endpoint weights for the intermediate block are exactly

    (n-1)^2-(d_n+1)^2=(w_n-2)(2n-w_n).

Dividing by `2n-1` gives `w_n(1+o(1))`, since the chosen `w_n` tends
to infinity and is `o(n)`. Cauchy–Schwarz on this block, the lower
block, and the separate top mode gives equation (4) with the stated
normalizations. The top-mode term in its numerator is `O(n^(-1/2))`,
and becomes `O(1/n)` after division by the dominant mode's endpoint
weight. The identity for the dominant coefficient follows from the
orthogonal decomposition and the already proved `a_n/N_n=O(1/n)`.

Consequently equation (5) is valid under `e_n=o(1)`. Both subsequent
hypotheses imply that assumption. The triangle inequality yields
`|P_n(0)|>=m_n(1-r_n)` and total absolute endpoint mass
`m_n(1+r_n)`, giving exactly the signed ratio in equation (6).

Under the strict limsup bound in equation (7), a fixed
`A>c_0=log(16)+3` can be chosen with `sqrt(A)L<1`. This produces a
uniform positive lower endpoint ratio. Under the little-o hypothesis,
the ratio tends to one. The strict inequality in (7), rather than an
inequality allowing the endpoint value, is necessary for this argument.

The quotient proof retains signed endpoint control. Its high-band
contribution after division by `n^2` is `O(w_n/n)`; its low-band
contribution is `O(sqrt(n) epsilon_n)` using the derived
`|P_n(0)|>=c sqrt(n)N_n`. Therefore `beta_n/n^2 -> -1`, with the
claimed `O(1/log n)` error under the strict limsup condition. For
`e_n=O(1/n)`, the endpoint error is
`O(1/sqrt(n log n))`, and the top-mode contribution is smaller.

These conclusions remain conditional on the unproved narrower
top-two concentration estimate. The broad concentration theorem alone
does not imply it. A bound on the actual selected direction suffices;
invertibility or a graph estimate for the entire two-dimensional
space is a stronger possible route. No new computation, arithmetic
estimate, or conclusion about e+pi enters this review.
