> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Reflected two-pole kernel: complete signed-error progress

2026-10-02. Original analysis by Agent 3. This is not an audit. The exact construction and determinant positivity are attributed to Agent 2's `REFLECTION_DISTRIBUTED_POLE_REPAIR.md`; the analytic reduction below is new work in this continuation. No assertion about rationality of e+pi follows from this family analysis.

## Target and prior-art gate

Target: the actual projected center from n=4k>=4, h>=1, N=n+h, q(w)=1-2w+2w^2,

    F0=q(w)^N/[w^(N+1)(1-w)^h], F1=wF0,
    Ri=Res0 Fi-Res1 Fi, Ai=Res1(e^(w-1)Fi), Bi=Res0(e^w Fi),
    T=(h-1)!, mi=T(Ai-Ri), U=T(A1R0-A0R1).

The complete actual error includes both the exponential contour around 0 and 1 and the vertical endpoint integral. The question is its signed behavior when h is approximately kappa n log n, and which larger depth scales can change the balance.

Before derivation, archive searches covered `reflection.*kernel|symmetric.*pole|pole.depth|balanced.*pole|w\(1.w\)|\(1.w\).*symmetric|symmetric.*annihilat`, together with rational quartic and multiplier searches in the October 1 and current archives. Exact prior overlap is the two-pole projection, old rational-period gate, fixed real beta-kernel barrier, and polynomial quartic selector. No imported theorem gives this actual center's growing-depth error. Search absence is not a novelty claim.

Primary searches and opened texts:

- `site:arxiv.org Hermite Pade symmetric rational kernel poles zero one exponential logarithmic`
- `site:arxiv.org two point Pade exponential arctangent symmetric saddle residue`
- `site:arxiv.org rational function beta integral endpoint poles reflection asymptotics`
- Martinez-Finkelshtein, Rakhmanov, Suetin, https://arxiv.org/pdf/1502.01202 (semiclassical type-I Hermite-Pade; method overlap).
- Kuijlaars, Stahl, Van Assche, Wielonsky, https://arxiv.org/pdf/math/0510278 (exponential Hermite-Pade normality and contour/saddle methods; no direct theorem for the pi component).
- Bostan, Chyzak, Lairez, Salvy, https://arxiv.org/pdf/1805.03445 (Hermite reduction modulo derivatives; algebraic interface overlap).

After discovering the finite-sum reduction, additional searches were `site:arxiv.org Laguerre polynomials large alpha uniform asymptotic 1F1 parameters negative zeros` and `site:dlmf.nist.gov Laguerre large parameters confluent hypergeometric asymptotic`. Opened Dunster, Gil, Segura, https://arxiv.org/pdf/1705.01190, introduction and parameter/turning-point regimes, plus https://dlmf.nist.gov/18.5 and https://dlmf.nist.gov/13.8. Their Laguerre definitions and asymptotic methods overlap. The present degree/parameter ratio goes toward infinity and the corresponding turning point approaches zero in their scaled variables, so their fixed-separated-turning-point statements are not silently applied.

## Exact positive binomial and Laguerre reduction

Let epsilon=(-1)^h and X_l=N-2l. Define, with out-of-range polynomial degrees omitted,

    D = sum_(0<=l<=N/2) binom(N,l) binom(X_l+n,n),
    D1= sum_(0<=l<=(N-1)/2) binom(N,l) binom(X_l+n,n+1),
    C = sum_(X_l>=n+1) binom(N,l) binom(X_l-1,n),
    E = sum_(X_l>=n+1) binom(N,l) binom(X_l,n+1).

Then the ordinary residues are EXACTLY

    Res0 F0=epsilon D, Res0 F1=-epsilon D1,
    Res1 F0=epsilon C, Res1 F1=epsilon E.

In particular E=C+c_(h-2), in Agent 2's notation. Agent 2 independently proved D>C and Ai each has sign epsilon, hence U>0 for every positive even n and h>=1. This positivity is used with attribution, not independently re-audited.

Writing L_m^(a)(z) for the standard generalized Laguerre polynomial gives the additional EXACT formulas

    B(z)=sum_(X_l>=0) binom(N,l) L_(X_l)^(n)(z),
    B0=epsilon B(1), B1=epsilon B'(1),
    B(0)=D, -B'(0)=D1,
    A=sum_(X_l>=n+1) binom(N,l) L_(X_l-n-1)^(n)(-1),
    Aplus=sum_(X_l>=n+1) binom(N,l) L_(X_l-n-1)^(n+1)(-1),
    A0=epsilon A, A1=epsilon Aplus.

The A1 degree is X_l-n-1 and its parameter is n+1: the corresponding binomial top is X_l, as required by E. All six identities follow directly from the finite coefficient sums, without extending a small-pole contour across the other pole.

This reduction exposes the dominant pole-0 covariance exactly:

    D1 B(1)+D B'(1)
      =D B(1) [ (log B)'(1)-(log B)'(0) ].

It avoids treating a large circle as a contour around only one pole. Such a circle surrounds both poles and would otherwise introduce a false asymptotic for A0.

## Current analytic direction (not yet a theorem)

For h~kappa n log n, write R=sqrt(N/n). The positive binomial measure underlying D concentrates near X=nR, with width of order sqrt(N). The ordinary ratio D/C retains a bias of logarithmic size n/R. The exponential weight in B is approximately exp(-R), while that in A is approximately exp(R). Thus a balance calculation suggests that pole-0 projection covariance may grow after division by U, even though the vertical contribution tends to zero. This is a candidate requiring a controlled covariance expansion, not a proved signed limit.

The cancellation inside the actual linear projection is essential. Replacing the projection numerator by a product of two dominant residues loses a factor of order R^2/n and gives the wrong sign. The intended next calculation is a uniform expansion of log B(z), including its second derivative, using the positive binomial measure and the Laguerre differential equation or a direct coefficient expansion. All endpoint and exponential terms will remain in the final interface. This calculation is completed in `REFLECTED_KERNEL_NLOGN_SIGNED_DIVERGENCE.md`; this earlier note preserves the research gate and discovery path.
