> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Shifted short rectangular family: joint M26 analytic gate

Author: Agent 3, 2026-10-02. Root explicitly assigns this analytic component and owns the exact primitive interface/cost recurrence. It combines the smaller degree of M24 with a positive moment shift. This is distinct from Root's M23 fixed-k scalar-multiplier family and from M25's one-extra-column rational coefficient lattice.

Fresh archive query in work/ and sources/, Markdown only:

```
(shift|M\+i|M.i.j|rho_M).{0,70}(short|rectangular|width|2k)|rectangular.{0,70}(shift|positive.power|Jacobi)|short.{0,65}(shift|Gamma|M/k)
```

It found unrelated short-shift arithmetic and the current scope notes. Selector's progress explicitly separates its M23 fixed-dimension scalar recurrence from Root's M24 shorter wedge family. No completed exact shifted-short full-center theorem was identified by this bounded query; no global novelty is inferred.

Fresh primary queries:

* `site:arxiv.org multiple orthogonal polynomials varying positive powers moment determinant Christoffel kernel Jacobi`
* `site:arxiv.org Hermite Pade overlapping supports positive polynomial modification multiple orthogonality`

Full primary papers opened in this gate:

* Kozhan--Vaktnas, *Christoffel Transform and Multiple Orthogonal Polynomials*, https://arxiv.org/pdf/2407.13946. It treats polynomial modifications, finite-support measures, determinantal formulas, and zero interlacing under specified multiple-orthogonality hypotheses. Those hypotheses are not assumed for the present signed atom/overlap system.
* Szehr--Zarouf, *On the asymptotic behavior of Jacobi polynomials with first varying parameter*, https://arxiv.org/pdf/1605.02509. Its varying-parameter tools overlap the reference exponential scale; our exterior value at 3 admits a direct positive-binomial estimate.
* Krattenthaler, *A determinant identity for moments of orthogonal polynomials that implies Uvarov's formula for the orthogonal polynomials of rationally related densities*, https://arxiv.org/pdf/2103.03969. Polynomial moment modifications and evaluation determinants are classical overlap. The full mixed measure and actual inverse-conditioning estimate will be established by the explicit tail coercivity from M24, with the shifted costs retained.

The precise construction will use even M>=0, upper functional rho_M=y^M mu-delta_{-1}, and lower COMPLETE measure sigma_M=y^M sigma. Its lower endpoint coefficient is still (-1)^(i+j), so the same scalar S=e+pi is retained. The final denominator is always taken after full rational clearing and evaluated gcd; the analytic theorem will not estimate it from raw Gamma mass.
