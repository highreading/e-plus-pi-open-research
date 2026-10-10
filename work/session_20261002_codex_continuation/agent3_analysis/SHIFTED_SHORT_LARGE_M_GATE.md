> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# M26 short rectangular family: unbounded-shift analytic gate

Author: Agent 3 / analysis. Date: 2026-10-02. This is original analysis, not an audit. Root owns the actual primitive denominator arithmetic and its separate M27 k=1 extraction. No M27 arithmetic is duplicated here.

## Exact new target

Extend the complete signed M26 error from compact M/k to M/k tending to infinity, allowing exponential or superpolynomial M. Retain the exact power of M, the endpoint constant, a uniform error estimate, both actual endpoint components, and the final reduced denominator Q. The existing proportional F(kappa) formula has O_K(log k) only for bounded kappa; it does not supply a uniform estimate in this new regime.

The odd-parity directional extension is already saved in Section 6 of SHIFTED_SHORT_COMPLETE_SIGNED_ERROR.md: sign(S-c)=(-1)^M, with the correct cofactor response sign. That extension supplies no odd-M arithmetic theorem.

## Archive search

From the research archive root, ran:

    rg -n 'Jacobi.{0,70}(large.parameter|unbounded|superpolynomial|exponential|Poisson|crossover)|Christoffel.{0,70}(M/k|unbounded|large.M)|endpoint.{0,70}M.\^.{0,20}2k|M.{0,10}k.{0,20}infinity.{0,40}Jacobi' work sources -g '*.md'

The bounded result did not contain a completed exact exterior Jacobi crossover theorem for this short rectangular construction. Relevant established overlap remains the archive's Christoffel and fixed-parameter exterior bounds, the preceding M26 compact-parameter theorem, and Root's different scalar M23 fixed-k large-M result. Search absence does not establish global novelty.

## Fresh primary search and open

Searches:

1. `site:arxiv.org Jacobi polynomials large beta parameter uniform Laguerre approximation varying degree`
2. `site:arxiv.org Jacobi polynomial large parameter asymptotic outside interval Laguerre uniform`

Opened and read the full primary paper:

- A. Gil, J. Segura, N. M. Temme, *Asymptotic Expansions of Jacobi Polynomials for Large Values of beta and of Their Zeros*, SIGMA 14 (2018), 073. https://arxiv.org/abs/1804.06749 ; full paper https://arxiv.org/pdf/1804.06749 ; DOI https://doi.org/10.3842/SIGMA.2018.073 .

Overlap: the paper develops large-parameter Jacobi/Laguerre expansions and starts from exact integral/polynomial representations. Its Section 2, Remark 1 states bounded degree, bounded other parameter, and bounded scaled argument for the asymptotic property. Its discussion after the numerical examples explicitly distinguishes fixed general argument from the bounded scaled argument. The growing degree and fixed exterior argument 3 required here are not imported as a consequence of that theorem. The planned proof will instead use the exact positive binomial sum and a finite Poisson-type remainder, coupled to the actual determinant insertion ratio.

The classical Jacobi identities themselves are standard. The target-dependent work is the uniform control of the complete M26 determinant/cofactor, concentration of its actual endpoint weight, and the resulting complete primitive-form interface. No claim of a new general Jacobi identity or a rationality theorem is made.

Also opened the authoritative primary-reference formulas https://dlmf.nist.gov/18.9 (Jacobi recurrence, equations 18.9.2 and 18.9.2_2) and https://dlmf.nist.gov/18.5 (explicit polynomial representations). They support the classical finite recurrence/binomial identities; the target's signed determinant normalization and endpoint-weight comparison are proved directly in the author note.
