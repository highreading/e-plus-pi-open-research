> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Proposed growing-degree content criterion

## Status correction: current bound obstruction

The earlier strict content-rate target is now marked unattainable by the main-agent deduction in GROWING_BOUND_OBSTRUCTION_DRAFT.md, pending independent audit. The original argument below is preserved for provenance. Exact normalization and divisibility claims must be reviewed separately from that target.

Status: main-agent draft; not independently reviewed. The estimates below must be checked against the completed arithmetic and Gaussian-bound documents before promotion. No solution of rationality or irrationality of e+pi is claimed.

## Fixed normalization

Let 1<=b<=n. Use exactly the monic cofactor normalization of agent2/PROOF_DRAFT.md, with endpoints X=A(1), Y=B(1)=-D_V and full remainder R(1)=D_W+T.

Put F=(2n+1)!, rho=product_{l=1}^{b-1}(2n+2l)!, and M=2^(2n+3) F^2 rho. An empty product is 1.

The proposed endpoint clearer is MX,MY in Z. To justify it, Rodrigues gives

    ell_j(p_{n+l})=E_{n+l,l+j-1}/(2n+2l)!,
    E_{k,r}=(d/dx)^r[x^k H_k(x)] at x=1 in Z.

Replace the b-1 high rows by their integer versions, forming H. Let e=(1,...,1), a_j=T_j(L_n), c_j=T_j(L_{n+1}), where the factorial indices retain the same n. Define

    Delta_P=det[H;e;a], Delta_U=det[H;e;c], E=det[H;c;a].

The proposed endpoint identities, with the original second-kind convention, are

    rho Y=(P_{n+1}Delta_P-P_n Delta_U)/G,
    rho X=(w_P Delta_U-w_U Delta_P-E)/G,
    G=(-1)^n 2^(2n+3)/(n+1).

These signs and the relation to Agent 1's primitive contractions require explicit cross-checking. Every partial-exponential denominator divides F, so F Delta_P, F Delta_U and F^2 E are integers. The moment formula bounds denominators of w_P,w_U by 2^n(n+1)!, and F/(2^n n!) is an integer. Thus (n+1)F w_P and (n+1)F w_U are integers, yielding the asserted clearer.

On Y!=0, put g=gcd(|MX|,|MY|). Then q=|MY|/g is the actual reduced endpoint denominator, and

    q/|D_V|=M/g,
    |qR(1)/Y|=(M/g)|D_W+T|.

This equality is scale-specific. Divisors extracted in another normalization must be translated before being counted in g. A large arbitrary clearer does not itself improve the primitive form.

## Proposed bound for b=floor(n/2)

The sharpened Gaussian factor is

    J_d(R)=(2pi)^(-d/2)(2a)^(-d^2/2) product_{j=1}^d j!,
    a=2R/pi^2.

Its proof is to use monic Hermite polynomials with squared norms sqrt(pi) k!/(2^k a^(k+1/2)), then determinant integration. The independent review must check all constants and the application to the absolute contour estimate.

Take R=lambda n for a fixed lambda>0, eventually R>20. Only the corrected functional domains are used: d=b for differences and d=b+1 for ordinary determinants. The factorial sum gives

    sum_{j=1}^d log(j!)=(d^2/2)log d-3d^2/4+O(d log d).

For either intended dimension, this suggests log J_d(R)=O(n^2): its n^2 log n terms cancel. The reference contour factor contributes

    d log E_n(R)=-(n^2/2)log n+O(n^2).

To conclude an actual upper bound, one must additionally prove uniform exponential bounds for the analytic factors V/p_{n+1} and W/p_{n+1}, not merely assert their finiteness. The proposed justification uses the finite Legendre projection, its explicit norms, geometric coefficient bounds on a fixed disk, and the established lower bound for p_{n+1}. High-row ratios have their already proved geometric bounds. The divided-difference factors and all remaining dimension factors should then contribute O(n^2).

Pending verification of these details, the proposed conclusion is

    B_W+B_T <= exp(-(n^2/2)log n+C n^2)

with fixed C, where B_W,B_T are the actual corrected-domain absolute bounds. This is not a determinant lower bound or a remainder nonvanishing theorem.

The explicit M has

    log M=(5/4)n^2 log n+O(n^2).

Therefore a sufficient, presently unproved criterion on the SAME unbounded index set is

    Y!=0, D_W+T!=0,
    liminf log(g)/(n^2 log n)>3/4.

Under these hypotheses the exact primitive-form bound tends to zero. The resulting nonzero integer forms would prove irrationality of e+pi. None of these growing-degree nonvanishing or content hypotheses is established here. Failure to meet this sufficient bound does not exclude the construction.

## Required review

Read agent1/GROWING_DEGREE_ARITHMETIC.md and agent3/GAUSSIAN_VANDERMONDE_BOUND.md. Check the exact cofactor scales, signs, endpoint clearer, relationship between g and removed contents, uniform analytic-factor estimates, and all asymptotic constants. Identify any automatic contribution already included in g before describing a residual arithmetic target. Save repairs explicitly; do not silently promote this draft.
