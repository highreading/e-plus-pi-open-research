> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Short rectangular paired kernel: analytic gate

Author: Agent 3, 2026-10-02. Root's M24 target is the unshifted k by 2k matching kernel, right polynomial degree <=2k-1. Root retains all-degree algebra, basis invariance, and final primitive content; this agent studies the complete signed determinant, its affine coefficient, and center convergence.

## Archive searches

Fresh query in work/ and sources/, Markdown only:

```
(rectangular|short|kernel).{0,65}(derangement|paired|D_\(2|rank.one|matching)|derangement.{0,65}(multiple.orthogonal|Chebyshev|Angelesco|Nikishin)|D_\(2.{0,40}(stack|kernel)
```

Matches were unrelated kernel/matching constructions, the current shifted M23 note, and existing scope notes. No completed all-degree complete-center theorem for this exact short rectangular pair was identified. This bounded search is not evidence of global novelty. Root supplied main/SHORT_PAIRED_KERNEL_CERTIFICATE.json, k=1,...,9 exact center/content matching and diagnostic errors; the real values are not an asymptotic or nonvanishing proof.

## Fresh primary searches and full papers opened

Queries:

* `site:arxiv.org multiple orthogonal polynomials overlapping supports Chebyshev AT system Hankel determinants`
* `site:arxiv.org Hermite Pade negative mass Nikishin multiple orthogonal polynomials normality`

Opened full primary papers:

* Lopez Lagomasino, *An introduction to multiple orthogonal polynomials and Hermite-Pade approximation*, https://arxiv.org/pdf/1910.08548. Sections 1--2 specify Angelesco disjoint-support and Nikishin Cauchy-product hypotheses, AT systems, and perfectness. They provide the relevant classical analytic framework, not an automatic theorem for a negative atom plus overlapping densities.
* Zhang--Filipuk, *On Certain Wronskians of Multiple Orthogonal Polynomials*, https://arxiv.org/pdf/1402.1569. Constant-sign and oscillatory Wronskian results assume an algebraic Chebyshev system. That assumption must be established for the actual present measures before such a theorem can be used.

The actual functionals are rho=mu-delta_{-1} and sigma on [0,1], with

    dmu(y)=[exp(-1-sqrt(y))+1_{y<1}exp(-1+sqrt(y))]dy/[2sqrt(y)],
    dsigma(y)=[exp(sqrt(y))+4/(1+y)]dy/[2sqrt(y)].

The rectangular stack is the (k,k) moment determinant for (rho,sigma). Entrywise its lower moment block is eC+R+S V; subtracting e times the corresponding upper rows gives the lower rational endpoint block plus S times its rank-one response without changing the determinant. Both exponential and arctangent integrals are included in sigma. An unsigned replacement measure or a basis change within the same kernel cannot supply its missing sign/nonzero theorem.
