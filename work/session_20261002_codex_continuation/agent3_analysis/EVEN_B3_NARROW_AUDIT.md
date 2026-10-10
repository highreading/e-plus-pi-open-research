> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Narrow independent examination of the even-index B3 signed asymptotic

Examiner: Codex continuation Agent 3, 2026-10-02. Scope deliberately limited to the unreviewed author claim in `work/session_20261001_astra/CANONICAL_B3_SIGNED_ERROR_ASYMPTOTIC_DRAFT.md`. No accepted normality/log(2) review, historical finite check, or controller was replayed. The audit phase stops with the verdict below.

Verdict: PASS for the precise fixed b=3,m_w=1 factorial B-only Gram center at sufficiently large EVEN integers n, conditional only on the retained exact contact/forcing/reconstruction identities in their archived scope. The draft's determinant/cofactor normalization, actual metric, and complete error constant agree. This is an analytic theorem for one rational approximation family; it is not a rationality theorem for e+pi.

Let sigma=sqrt(2), M=1+sigma, a=sigma/(2M), v=(1,-2,1)^T. The r-fold Gaussian Vandermonde integral is

    I_r = r! product_(j=0)^(r-1) [sqrt(pi) j!/(2^j a^(j+1/2))].

Thus I_2=pi/a^2 and I_3=(3/2)pi^(3/2)/a^(9/2). With the draft's 1/[r!(2pi)^r] factor, this gives

    C2=exp(-2sigma)/(8pi a^2),
    C3=exp(-3sigma)/(32pi^(3/2) a^(9/2)),
    C2/C3=4sqrt(pi) exp(sigma) a^(5/2).

The two alternants in the r=3 determinant have index Vandermonde 2 divided by 0!1!2!=2; each ratio is 1. Their opposite phases cancel. For r=2 each ratio is exactly the retained row or column gap. Cofactor signs therefore produce v v^T, rather than an extra factor or an opposite sign. The n-powers are n^(-r/2-r(r-1)/2): n^(-9/2) at r=3 and n^(-2) at r=2. Exponential off-saddle tails and Gaussian domination with the explicit alternating factors justify division of cofactor asymptotics by the determinant. No inversion of an entrywise rank-one limit is used.

For Dsc=diag(1,-sigma,2), Dsc^(-1)v=(1,sigma,1/2)^T=r and Dsc v=(1,2sigma,2)^T=l. The transpose/inverse orientation in the draft is correct. The forcing direction is fstar=(1,Aplus,Aplus^2)^T, and l^T fstar=(2+sigma)^2=B0>0.

The actual finite reconstruction columns and factorial weights yield G_n -> 6 e2 e2^T and r^T G_infty r=3/2. Both numerator and denominator of the Gram-normalized selector therefore have nonzero leading constants. In particular f0 lambda -> l/B0; the weight degeneracy does not cause an unaccounted normalization loss.

The complete logarithmic forcing from both conjugate endpoints has eF_i=-2n! integral h(t)^n (1-exp(it)/sigma)^i dt for even n. Its scalar ratio is

    eF0/f0=-4pi M^(-2n-1)(1+o(1)),

and contraction by the limiting selector contributes
(1+sigma Aminus)^2/(2+sigma)^2=M^(-2). The resulting constant is exactly -4pi M^(-2n-3).

The retained entire exponential forcing gives lambda^T eE=O(1/(n!sqrt(n))). Weighted Cauchy-Schwarz gives |kappa|<=w0/sqrt(a_n)=O(1/(n!n^5)). Both are o(M^(-2n)). Hence neither endpoint correction nor complete exponential forcing can change the even-index leading signed term.

One convenient simplification, useful for subsequent ORIGINAL work, is a^2 B0=1. Therefore xi2~exp(sigma)n!n^2 at even n and a_n~6exp(2sigma)(n!)^2 n^4.

Scope boundary: for odd n the exact contact relation is H_n=(-1)^n Dsc T_n Dsc^(-1), whereas the author draft intentionally writes the even specialization. One must retain this sign to extend the center. This is not a defect in the stated even theorem.

## Archive and current primary-literature check

Archive queries executed before selecting this target:
- rg for B3, b=3, signed asymptotic/error, odd/center, Toeplitz moment/saddle determinant across the October 1 session, September sessions and sources.
- rg for exact weight, forcing-circle, Dsc, and logarithmic arc expressions.
- rg for Gram center, odd Gram, factorial B-only and b=3 signed errors across the full archive.

Closest archive overlap: the draft audited here; agent2/LOGARITHMIC_FORCING_VECTOR.md supplies the all-parity exact endpoint identity; agent3/RATIONAL_CENTER_ASYMPTOTICS_REPORT.md records a more general conditional saddle approximation without the decisive adjoint direction. No completed all-parity theorem for this exact center was found by these bounded searches. Search absence is not a global novelty claim.

Current web queries:
1. fixed size Toeplitz determinant varying weight saddle point asymptotics moments Hermite Pade exponential arctangent
2. Hermite Pade approximants e pi factorial Toeplitz determinant moment saddle asymptotics
3. site.arxiv.org Toeplitz determinants fixed size large parameter saddle Andreief
4. site.arxiv.org Hermite-Pade approximation block Toeplitz determinants Mano Tsuda
5. Asymptotic Properties of Special Function Solutions of the Painleve III Equation Pan 2025 arxiv
6. fixed Toeplitz large Andreief determinant asymptotics Pan

Primary papers opened:
- Hao Pan and Andrei Prokhorov (2025), [Asymptotic Properties of Special Function Solutions of the Painleve III Equation for Fixed Parameters](https://onlinelibrary.wiley.com/doi/10.1111/sapm.70051). Publication PDF at [UChicago repository](https://knowledge.uchicago.edu/record/14957/files/Asymptotic-Properties-of-Special-Function-Solutions-of-the-Painlev%C3%A9-III-Equation-for-Fixed-Parameters.pdf). Overlap: fixed-size Toeplitz determinants, Andreief multiple integrals, and elementary parameter asymptotics. Different cylinder-function symbol and Painleve target. No theorem for this factorial Gram center is imported.
- Toshiyuki Mano and Teruhisa Tsuda, [Hermite-Pade approximation, isomonodromic deformation and hypergeometric integral](https://arxiv.org/abs/1502.06695). Overlap: block-Toeplitz determinant structure of Hermite-Pade approximants/remainders. Different hypergeometric/isomonodromic objective; no center asymptotic imported.
- F. Wielonsky, [Asymptotics of Diagonal Hermite-Pade Approximants to e^z](https://www.sciencedirect.com/science/article/pii/S0021904596930816), publisher search result accessed; direct open returned an internal error. Overlap: fixed number of functions and exact approximant/remainder asymptotics. This source was not relied on for a proof.

