> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Scoped countermodel: global monotonicity and exact monodromy do not fix endpoint arithmetic

Status: proved countermodel, not a retained Genesis mechanism. Author: Agent 3, 2026-10-02. This note saves the already-derived refinement before leaving interpolation routes. Root independently owns an order-zero entire correction; that construction is not reproduced here.

Let F(z)=exp(z)+4 arctan(z), with the real branch on the real axis. Fix an integer J>=0. There exists an entire h with rational Taylor coefficients, h^(j)(0)=0 for 0<=j<=J, such that F(1)+h(1) is rational, F+h is strictly increasing on the entire real axis, all full monodromy increments of F are unchanged, and both real-axis endpoint asymptotics are unchanged. The rational endpoint can be any rational sufficiently close to S=e+pi. No differential equation or factorial-denominator constraint is preserved.

## Gate and attribution

Archive query: `\bband.?limited\b|Paley.{0,3}Wiener|\bsinc\b|globally monotone|monotone entire|monotonic.*entire|entire.*bounded on.*real|rational.*Taylor.*interpol`, over Markdown in the research archive. Hits included the older root-of-unity sinc/canonical-product notes, cardinal Newton arithmetic, and the present agent's finite-jet interpolation countermodel. No developed version of the precise global-monotone correction below was located in this bounded query; this is not a global novelty assertion.

Fresh queries:

- `entire function rational Taylor coefficients exponential type bounded real axis prescribed value monotone interpolation`
- `analytic increasing diffeomorphism rational coefficients prescribed countable dense sets entire function`
- `rational Taylor coefficients entire functions exponential type interpolation sinc functions arithmetic values`

Opened primary sources:

- Sato–Rankin, *Entire functions mapping countable dense subsets of the reals onto each other monotonically*, [publisher abstract](https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/entire-functions-mapping-countable-dense-subsets-of-the-reals-onto-each-other-monotonically/28C45647FCDA1709F972551033E58D92), DOI 10.1017/S0004972700040636. Only the publisher abstract was read.
- Melzak, *Existence of certain analytic homeomorphisms* (1959), [full five-page primary paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4157131FFA9E5A545D75EF3113848437/S0008439559051086a.pdf/existence-of-certain-analytic-homeomorphisms.pdf). Theorem 1 and Corollary 1 use successive approximation to preserve analytic monotonicity and finite differentiable approximation while prescribing dense-set images. Monotone interpolation is classical support, not a newly retained route.
- Hadassi–Sodin, *Taylor coefficients and zeroes of entire functions of exponential type* (2025), [full primary paper](https://arxiv.org/pdf/2504.13104). Introductory Theorems 1–2 concern additional coefficient-size restrictions; they do not apply to the unrestricted small rational coefficients used here.
- Alves–Lelis–Marques–Trojovsky, [arXiv:2306.03281](https://arxiv.org/pdf/2306.03281), previously opened full paper, supports the public interpolation background.

The essential interpolation route is already public and is discarded under Genesis. The purpose of this note is a falsifiable limitation on proposed analytic signatures.

## Uniform correction functions

For n>=1 define

    s(z)=sin(z/8)/(z/8),  phi_n(z)=s(z)^4 sin(z/(8n))^n.

Each phi_n is entire with rational Taylor coefficients, vanishes to order n at zero, and phi_n(1)>0. The integral formula s(z)=integral_0^1 cos(tz/8)dt and the elementary sine bound give

    |phi_n(z)| <= exp(5 |Im z|/8).

On the real axis |s(x)|<=min(1,8/|x|) and |s'(x)|<=1/16. Differentiating the second factor costs at most 1/8, uniformly in n. Consequently

    |phi_n'(x)| <= (1/8)|s(x)|^4+(1/4)|s(x)|^3,
    (1+x^2)|phi_n'(x)| <=195/8<25.

For |x|<=8, multiply the first bound by at most 65. For |x|>=8 the first bound is at most 512/x^4+128/|x|^3, and (1+x^2)<=65x^2/64 gives the same constant. Also |phi_n(x)|<=min(1,8/|x|)^4.

## Rational triangular selection

Put n0=J+1, eta=1/32, and d_n=eta 2^{-(n-n0+1)} for n>=n0. Thus sum d_n=eta. For any real delta with

    |delta| < eta phi_n0(1)/4,

choose rational c_n inductively with |c_n|<=d_n and residual after step n at most d_(n+1) phi_(n+1)(1)/2. At each step the current residual divided by phi_n(1) has absolute value at most d_n/2; density of the rationals therefore permits arbitrary accuracy while remaining within the coefficient bound. The initial inequality supplies this invariant at n0. Residuals tend to zero.

The series h=sum_(n>=n0) c_n phi_n converges uniformly on every compact set. It is entire and satisfies

    h(1)=delta,
    |h(z)|<=eta exp(5|Im z|/8),
    |h(x)|<=eta min(1,8/|x|)^4,
    |h'(x)|<=25 eta/(1+x^2).

Every Taylor coefficient is a finite sum, because phi_n begins at degree n. Hence all Taylor coefficients are rational and all derivatives through J vanish at zero.

## Countermodel and scope

Choose a rational r in the stated neighborhood of S, and put delta=r-S. Then F+h has endpoint r. Since h is entire it adds zero to every monodromy increment on every continuation loop; the full logarithmic branching of F, not merely finitely many singular jets, remains unchanged. On the entire real axis

    (F+h)'(x) >= exp(x)+(4-25/32)/(1+x^2)>0.

The correction is O(x^-4) at both real ends, so the limit -2pi at the negative end and the leading exp(x) with positive-end constant 2pi are unchanged. The original leading exp(z) is also preserved in every closed sector satisfying cos(theta)>(5/8)|sin(theta)|. This note does not claim preservation in all right sectors; root's separate order-zero construction has that different strength.

Thus rational Taylor data, any fixed finite origin jet, exact full monodromy, global real monotonicity, and both real-end asymptotics do not imply that the value at 1 is irrational. The countermodel does not preserve the exact differential law of F or arithmetic bounds on its Taylor denominators. It is not a statement about rationality of S itself.
