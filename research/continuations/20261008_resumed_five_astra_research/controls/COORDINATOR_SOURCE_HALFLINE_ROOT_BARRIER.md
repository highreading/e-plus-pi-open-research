> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A uniform root-exponential lower bound for the entire source-positive cone

Coordinator proof,8 October2026; independent review required. This extends
the already independently accepted two-square Taylor argument to the full
half-line-positive cone. It is an analytic lower bound, not a primitive-gcd
estimate or a decision on e+pi. No other producer's positivity is presumed.

## Gate and classical inputs

The complete common-kernel interval positivity/fixed-target/growing-target
notes were read earlier. They already distinguish interval positivity from
source-half-line positivity. Scoped archive searches for root-exponential
and half-line Laguerre/source lower estimates found no evaluated version of
this proposed cone-wide bound in the searched Markdown. This is not an
exhaustive novelty claim. Classical Markov--Lukacs representation is REUSED.
The primary UCSD polynomial-optimization notes were read only at
Theorem2.2.1 and its proof, PDF pages4--5, extracted lines317--382:
https://mathweb.ucsd.edu/~njw/Teaching/Sp19_245C/LectureNotes_245C02.pdf.
Laguerre norms for alpha0,1 were verified in DLMF18.3 Table18.3.1 rowLaguerre,
and the finite expansion in18.5.12:
https://dlmf.nist.gov/18.3.T1 and https://dlmf.nist.gov/18.5.E12.
The prior accepted Legendre finite coefficient formula is reused; the bound
below needs only binomial inequalities, not an extra asymptotic theorem.

## Statement

Let N>=1 and let P be a REAL polynomial of degree at most2N satisfying

    P(t)>=0 for ALL t<=1,
    eta(P)=int_(-infinity)^1 e^(t-1)P(t)dt=1,
    P(i)=1.

Put M=min(N,ceil(32sqrt(N))). Then

    J=int_0^1 P(t)dt >=1/[64*(M+1)^2*10^(2M)].       (1)

Thus any rational producer in this cone with the accepted complete source
identity has a positive ordinary error epsilon>=3J. If its ACTUAL final
primitive denominator q_N>=exp(cN) for a fixed c>0, then its whole error
q_N*epsilon_N tends to infinity. Such a q floor must be proved separately
for the same producer/indices, with actual content, least clearer and G.

## 1. The half-line representation and paid real norms

The classical half-line theorem applied to P(1-x) gives

    P(t)=F(t)^2+(1-t)G(t)^2,
    deg F<=N, deg G<=N-1.

F,G have real coefficients; no rational or integral representation is
asserted or used as a free arithmetic normalization. Since eta(P)=1,

    eta(F^2)+eta((1-t)G^2)=1.

Expand F in L_j(1-t), orthonormal for alpha0, and G in
L_j^(1)(1-t)/sqrt(j+1), orthonormal for alpha1. Each coefficient-vector
norm is at most1. All norms are positive and the degrees remain original.

At i,

    1=|F(i)^2+(1-i)G(i)^2|
      <=|F(i)|^2+sqrt(2)*|G(i)|^2.

Since (1+sqrt(2))/4<1, at least one H in {F,G} satisfies |H(i)|>1/2.
That SAME H is used below. No real sign inference is made at complex i.

## 2. A uniform entire-polynomial bound

The finite Laguerre expansions give

    |L_j(z)|<=exp(2sqrt(j|z|)),
    |L_j^(1)(z)|<= (j+1)*exp(2sqrt(j|z|)).

For the second inequality, the r-th absolute coefficient is
binom(j+1,r+1)/r! <= (j+1)j^r/(r!)^2.
For j=0 the formula is read directly. The exponential domination uses
binom(2r,r)<=4^r, exactly as in the already accepted root-lower proof.

Cauchy--Schwarz and the coefficient norms therefore give, for BOTH F,G,

    |H(t)| <= C_N=(N+1)*exp(2sqrt(101N)), |t|<=100.  (2)

Here sum_(j=0)^(N-1)(j+1)=N(N+1)/2<=(N+1)^2; the alpha0 sum is smaller.

## 3. One Taylor tail, at i and on the retained real interval

Let H_M be the Taylor polynomial through degree M at0. If M=N its tail
is zero. Otherwise Cauchy's coefficient bound from(2) gives

    |H(t)-H_M(t)|<=delta=C_N*100^(-M)/99, |t|<=1.   (3)

This includes i and the entire interval[0,1/2]. Define

    K_M=sqrt(2)*(M+1)*10^M.

When M<N, M>=32sqrtN, M+1<=34sqrtN, N+1<=2N,
2sqrt101<21 and log10>2 (because e<3). Thus

    delta*K_M <2*N^(3/2)*exp(-43sqrtN)<1/8.         (4)

For the last bound, x^3 exp(-43x) decreases for x>=1, and e>2.
No logarithmic precision or large-index computation is used.

## 4. The smaller-interval complex evaluation kernel

The shifted Legendre polynomial P_j(4t-1) has squared norm
1/[2(2j+1)] on[0,1/2]. Its finite coefficient formula is

    P_j(4t-1)=sum_r (-1)^(j+r) binom(j,r)binom(j+r,r)*(2t)^r.

At i, binom(j+r,r)<=2^(j+r), so its absolute value is at most

    2^j*sum_r binom(j,r)*4^r=10^j.

For every real polynomial A of degree at most M, complex Cauchy--Schwarz
therefore proves

    ||A||_(L2[0,1/2]) >= |A(i)|/K_M.              (5)

In the nonzero-tail case, |H_M(i)|>1/2-delta>3/8. Equations(3)--(5) and
the reverse triangle inequality give

    ||H|| >=(3/8)/K_M-delta >=1/(4K_M).

In the zero-tail case(5) gives the stronger1/(2K_M) lower bound directly.
On[0,1/2], P>=F^2 and P>=(1/2)G^2. Therefore, whichever H was selected,

    J>= (1/2)*||H||^2
      >=1/(32*K_M^2)=1/[64*(M+1)^2*10^(2M)].

This proves(1) at EVERY N>=1, independently of coefficient rationality.

## 5. Scope and a useful exclusion test

This proof applies to all source-half-line-positive producers satisfying
the two complete normalizations, including global sums of squares, at their
ACTUAL degree. It does not apply merely because a determinant/matrix has a
positive integral representation, or because a polynomial is positive on
[0,1]. A proposed application must identify the actual source polynomial
and verify its sign on(-infinity,1], eta(P)=1 and P(i)=1.

The distinct signed Chebyshev producer deliberately escapes this hypothesis.
Its proposed exponential ordinary upper bound, if validated, is compatible
with the present theorem precisely because source-half-line positivity has
been relinquished. This says nothing by itself about that producer's actual
primitive denominator. No binary, compact or ternary producer is retired
by this note without a separate exact hypothesis check and paid q bound.
