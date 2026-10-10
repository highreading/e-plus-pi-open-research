> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Uniform growing-degree Gamma/compact leading coefficient: gate

Author: Agent 3 / analysis, 2026-10-02. This is original analytic continuation. Root owns M28's fixed-degree lemma and polynomial-transcendence transfer, and M29's degree/height arithmetic. Those are not rederived or audited here.

## New target

For the exact leading coefficient

    P_r(X)=(X+1)_(2r),
    c_r(X)=exp(-1) integral_0^1 exp(u)u^(X+2r)du,
    Z_k(X)=det[P_(i+j); c_(i+j)-(-1)^(i+j)],

prove an explicit UNIFORM growing-k nonzero region and conditional-root/insertion error bound. P is the normalized Gamma-square moment block. The fixed-k centered-Hermite argument and its unspecified eventual threshold are already Root's result; the present target is an effective k-dependent range.

## Archive query and overlap

Ran these bounded searches from the research root:

    rg -n 'Z_k|leading.f|Gamma.*compact|polynomial.*measure|leading.*homogeneous|M28' work/session_20261002_codex_continuation/main work/session_20261002_codex_continuation/agent3_analysis -g '*.md'

    rg -n 'Gamma.{0,60}(compact|Andreief|conditional.root)|leading.{0,50}(coefficient|homogeneous).{0,40}(derangement|Gamma|paired)|Mahler.{0,50}(measure|polynomial)|Z_k$X$' work sources -g '*.md'

The closest established overlap was Root's scalar fixed-degree Gamma/Hermite proof, the preceding M24/M26 insertion control, and general Mahler-measure notes for different arithmetic constructions. Root then supplied its new M28 source main/SHIFTED_SHORT_FIXED_DIMENSION_TRANSCENDENCE_OBSTRUCTION.md; its fixed-degree scope is explicitly retained. No search absence establishes novelty outside this archive.

## Fresh primary searches and opens

Queries:

1. `site:arxiv.org Christoffel transforms Gamma moment determinants polynomial modification varying degree`
2. `site:arxiv.org Laguerre large parameter uniform varying degree zeros Gamma orthogonal polynomials`

Opened full primary papers:

- I. Krasikov, *On extreme zeros of classical orthogonal polynomials*, https://arxiv.org/pdf/math/0306286 . Section 1 states explicit uniform Laguerre/Jacobi root bounds. These apply to their classical scalar orthogonality weights. The pushforward under u^2 and its node-dependent degree-k-1 polynomial modifier are not assumed to satisfy those classical hypotheses; no classical zero bound is imported to the modified signed interface.
- R. Kozhan and M. Vaktnas, *Christoffel Transform and Multiple Orthogonal Polynomials*, https://arxiv.org/pdf/2407.13946 (current full primary version opened). Polynomial modifications, finite-support additions, and determinantal formulas are classical/current overlap. Normality and zero-interlacing hypotheses are not assumed for the present compact-minus-exterior-atom stack.
- C. Krattenthaler, *A determinant identity for moments of orthogonal polynomials that implies Uvarov's formula for the orthogonal polynomials of rationally related densities*, https://arxiv.org/pdf/2103.03969 . The moment/characteristic insertion formulas are established overlap. The new target is direct uniform coercivity and the consequent actual leading coefficient nonzero region.

The proof will use elementary finite-dimensional tail estimates and the exact positive compact Christoffel minimum. No global quasi-definiteness, a polynomial measure for e, or actual primitive-denominator growth is asserted by this gate.
