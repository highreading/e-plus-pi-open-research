> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Endpoint-zero amplitudes and their exact convergence transition

Root original target M21, 2026-10-02. Author theorem; research ACTIVE.

## Gate and scope

Fresh archive searches covered vanishing endpoint gauges, near-zero amplitudes, and the mixed D_N/u_N interface. Earlier endpoint-zero common-kernel ideals and generic weighted Padé constructions are acknowledged; no theorem for the complete exponential-gauged center in this target was found. Fresh primary searches identified nondiagonal exponential Hermite–Padé approximation; the full primary Van Assche survey https://arxiv.org/pdf/math/0609094 was opened, including its complete irrationality criterion in §3.2, and https://arxiv.org/pdf/math/0510278 was opened. The publisher full-page fetch for DOI10.1016/0377-0427(95)00106-9 failed; only its primary abstract was available. No result from that inaccessible full text is assumed.

M20 treats ONE fixed A with A(1)!=0. Here the new target is a fixed endpoint-zero direction combined with an index-dependent scalar; M20's fixed-weight asymptotics are not silently made uniform in variable A.

## Exact denominator collapse at A(1)=0

Use M20's complete integer arrays D_N,B_N,u_N and S=e+pi. For any fixed polynomial A=sum a_j z^j, its normalized denominator satisfies

    (-1)^N D_N^A=A(1)D*(N)+R_A(N),
    R_A(x)=-sum_(t=0)^(deg A-1) (-1)^t(x)_t sum_(j>t)a_j.  (1)

This is an exact polynomial identity. Apply D*(x)=1-xD*(x-1) repeatedly to each weighted term in M20. Thus an endpoint zero removes the derangement component, leaving a polynomial remainder; it does not by itself produce a rational approximation to S.

For A0(z)=(1-z)^m, fixed m>=1, write

    R_m(N)=sum_(j=0)^(m-1) binom(m-1,j)(N)_j,
    V_(m,N)=sum_(j=0)^(m-1) (-1)^j binom(m-1,j)(N)_j u_(N-j).

For N>=m,

    D_N^A0=(-1)^N R_m(N), B_N^A0=V_(m,N).          (2)

R_m has degree m-1, is positive for N>=m, and V_(m,N)=N![z^N](1-z)^(m-1)exp(-z)G(z). Formula(2) includes the full endpoint numerator; for m=1 it reads D=(-1)^N and B=u_N.

## Variable scalar, complete error, and actual content

Take any integer L_N and use the ACTUAL integral-jet polynomial

    A_N(z)=1+L_N(1-z)^m, A_N(1)=1.

Its complete endpoint is exactly

    d_N=D_N+L_N(-1)^N R_m(N),
    b_N=B_N+L_N V_(m,N), c_N=b_N/d_N,
    q_N=|d_N|/gcd(d_N,b_N),                         (3)

whenever d_N!=0. Put E_N=B_N/D_N-S and K_(m,N)=V_(m,N)-S(-1)^N R_m(N). Then

    c_N-S=[D_N E_N+L_N K_(m,N)]/d_N.              (4)

All polynomial and exponential endpoint responses are present. A nonzero integer common content in(3) must divide

    W_(m,N)=D_N V_(m,N)-(-1)^N R_m(N)B_N.         (5)

This follows by eliminating L_N. Formula(5) is a necessary exact divisor interface, not a favorable size estimate for that content.

## Uniform convergence window proved from fixed-direction estimates

Let R0>1 be the nearest logarithmic singularity radius of the ONE fixed G. Every singularity lambda differs from1; consequently (1-lambda)^(m-1) is nonzero. The complete fixed-direction coefficient has signed leading term

    K_(m,N)/N!=-(1/N)sum_(|lambda|=R0)
       L_lambda exp(-lambda)(1-lambda)^(m-1)lambda^(-N)
       +O(R0^(-N)/N^2).                            (6)

The polynomial S R_m/N! is included and is factorially small. The direct finite-log argument and Lindemann–Weierstrass grouping from M13 prove an upper bound O(R0^-N/N) and a sharp lower bound of this order in a bounded block of any fixed arithmetic progression.

Suppose log(1+|L_N|)=O(N). Then L_N R_m(N)=o(D_N), so d_N/D_N tends to1. Uniformly along these choices,

    |c_N-S|<=C(1+|L_N|)R0^(-N)/N.               (7)

In particular any bound |L_N|<=exp(theta N) with theta<log R0 preserves complete convergence. The raw denominator nevertheless has

    log|d_N|=N log N-N+O(log N).                  (8)

The final primitive q may be smaller by the gcd in(3); no lower or upper rate for that gcd is supplied here. For the frozen degree81 P, L_N=2^N is inside the proved convergence window because R0>2.005.

There is also a rigorous opposite boundary. Write epsilon_N=1/L_N with L_N!=0 and assume, at EVERY sufficiently large index of a fixed progression,

    |epsilon_N|<=R0^(-N)/N^2.                    (9)

Divide(4) by L_N. The denominator is bounded by C N!R0^-N/N^2 plus the fixed polynomial R_m(N). In each fixed bounded block, (6) has one member with |K_(m,N)|>=c N!R0^-N/N. The added epsilon_N D_N E_N is uniformly of smaller order there. Therefore either the endpoint denominator vanishes or that member has |c_N-S|>=c' N. Such a family cannot converge to S on the whole progression. In particular exponential choices with theta>log R0 eventually meet(9). This proof applies fixed-direction estimates to explicit scalar formulas; it does not assume a uniform theorem for arbitrary variable polynomials.

The block boundary leaves sparse exceptional selections and the transition scale |L_N|≈N R0^N open. It supplies no every-index lower bound, no main irrationality decision, and no exclusion of unrelated response-changing constructions.

## New exact finite receipt

ENDPOINT_ZERO_AMPLITUDE_TRANSITION_CERTIFICATE.json recomputes the frozen P's integer jets and checks m=1,2,3,4 through N=140. It independently compares M20's binomial endpoint arrays with the collapsed polynomial/jet formulas(2). For L=1,2^N,3^N it verifies actual content divisibility(5), retaining the complete numerator and final gcd. These are new exact finite checks; analytic convergence and the block boundary are proved above, not inferred from the finite center values. The receipt passed every assertion.
