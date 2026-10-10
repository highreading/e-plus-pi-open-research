> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# M28. Every fixed-dimension shifted short family has large primitive forms

Author theorem: for EVERY fixed k>=1, the complete primitive forms of the shifted short construction diverge as even M tends to infinity. This extends M27's k=1 exclusion to every fixed dimension. It does not exclude growing k or decide the rationality of e+pi.

## Fresh archive and primary gate

Fresh archive queries covered leading homogeneous mixed stacks, Mahler bounds applied to the short shifted determinant, and fixed-k factorial exclusions. The existing algebraic-translation and rational-companion quantitative strategies are credited, as are M26's scalar compression and M27's inverse extraction. No completed full fixed-k application to this newly introduced short stack was found.

The fresh primary paper read is Ernvall-Hytönen, Matala-aho and Seppälä, *On Mahler's transcendence measure for e*, arXiv:1704.01374v3, published in Constructive Approximation49(2019),405--444. Its definition and Theorem1.1, including the explicit height threshold, were read, together with the corresponding proof estimates. For each fixed k>=2 and epsilon>0 it implies

    abs(P(e)) >= C_(k,epsilon) H(P)^(-k-epsilon)

for every nonzero integer polynomial of degree<=k, after adjusting a positive constant for the finite bounded-height cases. Reversing coefficients gives the same bound at1/e. At k=1 use the already sourced continued-fraction estimate. This is application of a published theorem, not a new transcendence measure or independent proof audit.

A search also located Fischler--Rivoal's2026 paper for algebraic arguments of degree>=2; its scope was read and it is not used for the present rational argument1.

## Leading factorial coefficient is eventually nonzero at every fixed k

Use the integer-cleared polynomials A(X,d,f),B(X,d,f) of M26, total degree<=k in d,f, and degree_f B<=k-1. The coefficient of f^k in A equals delta(X)^k times

    Z_k(X)=det[ Q-V ; -P ]=det[ P ; Q-V ].   (1)

Here P_(ij)=(X+1)_(2(i+j)), and Q_(ij) is the scalar recurrence polynomial Q_(2(i+j)). Both equalities include the block-swap and lower-row signs. We prove that this polynomial is NOT identically zero, for every fixed k.

Let Gamma_X be the probability pushforward y=u^2 of the Gamma(X+1,1) density. Its moments are P_(2r). Let c_X be the positive compact measure with moments

    c_r=e^(-1) integral_0^1 exp(u)u^(X+2r)du.

The exact decomposition of derangement moments is

    D_(X+2r)=X! P_(2r)/e+c_r,
    Q_(2r)=c_r-c_0P_(2r).

Adding c_0 times the corresponding P row to the upper block in(1) therefore gives

    Z_k(X)=det[ Gamma_X moments ; (c_X-delta_-1) moments ]. (2)

For fixed k and any k-1 nodes in[-1,1], the modified Gamma functional Gamma_X product(y-x_i) has a positive truncated Gram form for sufficiently large X, uniformly in those nodes. To see this explicitly, its tail modification is u^(2k-2) times a factor1+O_k(X^-2) on the centered Gamma window; the bounded small-u part is negligible relative to the Gamma mass and any of its finitely many centered moments. Center and scale u^2 by alpha^2 and2alpha^(3/2), alpha=X+2k-1. The normalized moments tend to standard Gaussian moments, uniformly in the node parameters. The finite limiting Gram matrix is positive definite. The corresponding monic degree-k compression polynomial tends to the Hermite polynomial, with all its physical roots X^2+O_k(X^(3/2)), hence greater than1.

Replacing an insertion node in[-1,1] by-1 changes the resulting determinant by1+O_k(X^-2), uniformly; this follows directly from the product over those k separated roots. Multi-Andreief for(2), including the ONE possible exterior atom, now writes

    Z_k(X)=(-1)^k(A_c-B_c),
    A_c/B_c=[1+O_k(X^-2)] Lambda_(c_X,k).

Here A_c,B_c are positive for sufficiently large X and Lambda is the positive exterior Christoffel minimum at-1, degree<k. Taking the constant test polynomial shows

    0<Lambda_(c_X,k)<=mass(c_X)<=1/(X+1).

Thus A_c<B_c for all sufficiently large X, and

    sign Z_k(X)=(-1)^(k+1).                 (3)

This is a bounded-degree proof. It is NOT asserted uniform in growing k. The analysis agent pursues an explicit growing-k version separately.

## Extract a nonzero small polynomial at1/e from the ACTUAL center

Write the actual full center as c=p_c/q in lowest terms, q>0, and the old mass l=p_l/a reduced, a>0. Its exact equation is

    F(d,f):=a q A(X,d,f)+(q p_l+a p_c)B(X,d,f)=0. (4)

Let F_k be its degree-k homogeneous component in d,f and define the INTEGER polynomial

    P_X(z)=F_k(z,1).

It is nonzero for sufficiently large X: its constant coefficient is a q delta^k Z_k(X), since B has no f^k term, and(3) is nonzero. This avoids any unsupported generic-coprimality or specialization assumption.

For fixed k, all scalar recurrence, tail and determinant coefficients have polynomial growth in X. The complete center and l stay bounded as M tends to infinity, by the full analytic theorem cited below. There is therefore an exponent C_k and a constant, independent of M, such that

    H(P_X)<=C_k a q X^(C_k).

Divide(4) by f^k. All lower homogeneous pieces are O_k(a q X^(C_k)/f), and

    d/f=1/e+O(1/(Xf)).

Controlling the polynomial derivative on this fixed bounded interval gives the COMPLETE extracted estimate

    0<abs(P_X(1/e))<=C_k a q X^(C_k)/f.     (5)

Strict positivity uses transcendence of e and the nonzero integer polynomial established above.

## Primitive q lower bound and the complete error

Apply the primary fixed-degree transcendence measure to(5). For every fixed epsilon>0,

    log q >= log(X!)/(k+1+epsilon)
              -log a-O_(k,epsilon)(log X). (6)

Since a<=lcm(1,...,X-1)<=4^X, this implies

    liminf_(M→infinity even) log q/log((2M)!) >=1/(k+1). (7)

The q in(6)--(7) is the ACTUAL denominator after every coefficient-pair cancellation. No gcd estimate was guessed.

The analysis agent's complete theorem in agent3_analysis/SHIFTED_SHORT_UNBOUNDED_M_COMPLETE_ERROR.md applies to ALL fixed k as soon as M>=max(100,16k), and gives

    S-c ~ (e+2)((k-1)!)^2/[2^(2k-1) M^(2k-1)] >0. (8)

It retains both endpoint contributions and the actual full determinant. Combining(7)--(8) yields

    abs(q(S-c)) tends to infinity,
    liminf log abs(q(S-c))/log((2M)!) >=1/(k+1). (9)

Every fixed-k even-shift subsequence is therefore excluded from the small nonzero integer-form method. There is no implication that e+pi is rational, and no exclusion of varying k from this bounded-degree argument.

## New exact structural certificate

SHIFTED_SHORT_TOP_FACTORIAL_COEFFICIENT_CERTIFICATE.json contains exact symbolic Z_k(X) for k1..3. Their degrees are2,10,23; all coefficients have the sign(-1)^(k+1), proving these three polynomial nonzero statements for every X>=0 independently of the asymptotic lemma. The all-fixed-k proof above does not infer its conclusion from these finite symbolic dimensions.

Files: SHIFTED_SHORT_TOP_FACTORIAL_COEFFICIENT_CERTIFICATE.json and shifted_short_top_factorial_coefficient.py. No new approximation atlas was extended.

Remaining original question: derive a uniform growing-k leading-coefficient and height budget, then compare it with the complete growing-shift error. The main problem is still open.
