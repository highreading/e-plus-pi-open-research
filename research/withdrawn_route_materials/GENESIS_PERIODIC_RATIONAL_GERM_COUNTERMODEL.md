> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A complete rational Taylor germ with a nontrivial rational period

Status: proved scoped countermodel / candidate filter, not a new irrationality route and not a global novelty claim. Main e+pi problem remains open.

## Candidate, archive and public gate

Candidate principle tested: a nonconstant entire function with rational Taylor coefficients and finite growth order cannot have a nonzero rational period. Such a principle might have been used after a proposed periodic compactification of the endpoint condition. The compactification from S has NOT been proved; the general principle itself is false.

Archive search used periodic entire/entire periodic, rational Taylor period, Lidstone, period one. The inspected archive hits concerned an unrelated modular phase period and the elementary fact that a periodic polynomial is constant. No version of the construction below was found in that bounded search.

Fresh searches used entire/period one/rational coefficients, periodic entire function/Taylor coefficients, and periodic/rational power series/entire order. The last synonym yields many papers on EVENTUAL PERIODICITY OF COEFFICIENT SEQUENCES; that is not the same property as f(z+1)=f(z), and those hits are not treated as relevant matches. Opened author primary sources: Waldschmidt, https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/UnivariateLidstoneInterpolation.pdf; Alves--Lelis--Marques--Trojovsky, https://arxiv.org/pdf/2306.03281; Tao's original2021 complex-analysis notes on entire periodic functions, https://terrytao.wordpress.com/2021/02/. Entire interpolation and periodic-function growth theory are credited established background. The exact simultaneous period-one/rational-Taylor statement was not located by this bounded search; that is not evidence of global novelty. No interpolation mechanism is retained as a Genesis tool.

## Follow-up public-core match (2026-10-02 17:16UTC)

A more specific Hurwitz / periodic / integer-derivative search located the sine-power triangular core itself: Sato, *Utterly integer valued entire functions. I*, Pacific J.Math.118(1985),523--530, DOI10.2140/pjm.1985.118.523. Waldschmidt's opened author survey, https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/SurveyIntegerValuedEntireFunctions.pdf , §3.4, explicitly describes Sato's inductive coefficients in sum a_n sin^n(2*pi*z). This is an essential match to the present correction mechanism, even though integer rounding and the present arbitrarily close rational rounding impose different growth budgets. Therefore the mechanism is explicitly public; no novelty inference may be drawn from the earlier bounded search.

The publisher DOI landing page was obtained locally and identifies the original paper and advertised PDF. The advertised https://msp.org/pjm/1985/118-2/pjm-v118-n2-p26-s.pdf returned404, and the Project Euclid mirror returned an Incapsula challenge. The original full paper was not read. The accessible source for the specific mechanism attribution is Waldschmidt's author survey, whose §3.4 was read. The theorem and full proof below are the present scoped rational-rounding adaptation, not a claim that Sato states its exact order-one version.

## Constructive theorem

There exists a nonconstant entire function f such that:

    f(z+1)=f(z),  f(0)=0,  f'(0)=1,
    f in Q[[z]],
    log max(1,M_f(R)) = O(R log R).

It has order exactly1. In particular it has rational period1, a COMPLETE rational Taylor germ, and finite order. The theorem concerns rational coefficients without additional arithmetic denominator restrictions.

Proof. Put psi(z)=sin(2pi z)/(2pi). This is entire,1-periodic, real on R, and psi(z)=z+O(z^3). Start P_1=psi. Suppose P_(n-1) has rational coefficients through degree n-1. Its degree-n Taylor coefficient beta_n is real. Choose a_n in Q so that

    |a_n-beta_n| <= 2^(-2^n),

and set c_n=a_n-beta_n and

    P_n=P_(n-1)+c_n psi^n.

The leading term of psi^n is z^n. Therefore this correction leaves all lower coefficients unchanged and makes the degree-n coefficient exactly a_n. Every P_n remains entire and1-periodic. Define

    f=psi+sum_(n>=2)c_n psi^n.

For each compact disk, W=max(1,sup|psi|) is finite, and the series is dominated by sum2^(-2^n)W^n. It converges normally because the coefficient majorant decreases doubly exponentially. Thus f is entire; uniform compact convergence preserves period1. For each fixed Taylor degree, all later corrections vanish to higher order, so that coefficient stabilizes at a rational number. Normal convergence also justifies derivative convergence. In particular f(0)=0 and f'(0)=1, proving nonconstancy.

For the growth estimate, |psi(z)|<=exp(2pi R) on |z|<=R, R>=1. Write L=2pi R and N=ceil(2log_2(L+2)). The terms T_n=2^(-2^n) exp(nL), n>=N, have ratio

    T_(n+1)/T_n = exp(L-(log2)2^n) < 1/2.

The tail is bounded by2exp(NL). The earlier terms are at most N exp(NL), up to the initial psi term. Hence log max(1,M_f(R))=O(L log L)=O(R log R), proving order at most1.

For the matching lower order, every nonzero integer is a zero of f, by periodicity and f(0)=0. Let g(z)=f(z)/z; it is entire and g(0)=1. Jensen's formula on radii R which avoid zeros on the boundary, with N=floor(R/2), gives

    log M_f(R)-log R >= sum_(1<=|n|<=N)log(R/|n|)
                              >=2N log2.

The maximum-modulus bound extends to arbitrary large radii by monotonicity. Thus log M_f(R) grows at least linearly along large radii; order is at least1. Combined with the upper bound, the order is exactly1.

## Scope

The construction gives an actual nonconstant periodic entire function with all origin derivatives rational and rational values0 at every integer. It disproves the candidate general rigidity principle. It does not assert finite exponential TYPE, a fixed rational differential equation, integer coefficients, controlled common denominators, or the actual exponential/circular global laws. Those are different constraints and cannot be silently added.

No implication from rationality of S to an arithmetic periodic compactification has been established. A future tool using such an object must prove BOTH the compactification and whatever stronger arithmetic/growth properties its obstruction theorem actually needs. Generic rational coefficients and finite order alone cannot supply that theorem.
