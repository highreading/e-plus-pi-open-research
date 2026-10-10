> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large saddle selectors: nonvanishing, exact dyadic denominator, and forcing height

Status: new main-agent author deductions, not independently reviewed. This note preserves the previously unsaved dyadic arguments and adds an archimedean forcing-height bound. No numerical execution or independent verification is claimed. The conclusions concern the actual reduced denominator but do not determine the complete approximation error.

## 1. Exact integer representation

Let n=4k with k>=1, m>=0, and put

    L_m(t)=(2t^2-4t+1)^(2m),
    B(t)=(1-2t+2t^2)^n(1-4t+2t^2)^(2m),
    K(t)=t^n B^(n)(t)/n!,
    U=K(1), N=2n+4m, J=N-n=n+4m.

This is the integer polynomial K from DIRECT_SELECTOR_HEIGHT_OBSTRUCTION_DRAFT.md. The direct forcing denominator is exactly

    F_L=(n!/2^n)U.

Taylor expansion at t=1 gives the separate useful identity

    U=[x^n](1+2x+2x^2)^n(1-2x^2)^(2m).              (1)

All identities hold without an HP coordinate-window restriction. A rational center is formed only when U!=0.

Write B(t)=sum_j b_j t^j. Each nonconstant coefficient in each quadratic factor is even, and at least ceil(j/2) nonconstant factors are needed to produce degree j. Consequently

    v_2(b_j)>=ceil(j/2),
    b_N=2^(N/2).

The coefficient of t^j in K is binom(j,n)b_j for j>=n, with lower coefficients zero. Thus

    K0(t)=2^(-n/2)K(t) belongs to Z[t].

All coefficients of K0 above degree n are even. The coefficient at degree n, reduced modulo two, is supplied only by selections of quadratic terms; selections including linear terms have an extra factor two. Therefore

    K0(t)=binom(n+2m,n/2)t^n modulo 2.               (2)

No claim is made that the odd coefficient content is one.

## 2. Explicit nonvanishing allocation

Choose a power of two P with k<P<=2k and impose m=-k modulo P. Then

    binom(4k+2m,2k)=binom(2k+m,k) modulo 2.

Since k+m=jP for a positive integer j,

    (1+x)^(2k+m)=(1+x)^k(1+x^P)^j modulo 2.

Its coefficient at x^k is one because k<P. Equation (2) proves

    K0(t)=t^n modulo 2,
    v_2(U)=n/2,
    U!=0.                                           (3)

In particular, the dyadic valuation of the coefficient gcd of K is exactly n/2.

For fixed rho>0 choose

    m_n=P ceil((rho n log n+k)/P)-k, n=4k.

Then rho n log n<=m_n<rho n log n+P. Hence m_n=rho n log n+O(n), and (3) holds at every selected index. This is an explicit nonvanishing family. The O(n) adjustment does not authorize ignoring subleading saddle phases.

## 3. Complete exponential and logarithmic components

Let c=alpha+beta be the rational direct forcing center and q its positive reduced denominator. Define

    D_j=j! sum_(r=0)^j 1/r!.

The exact exponential component is

    alpha=Vexp/[n! J! U],
    Vexp=sum_(j=n)^N b_j (J)_(N-j) D_j.              (4)

To derive this, the coefficient formula for the exponential forcing gives a sum b_j D_j/(j-n)!, divided by n!U. Multiplication by J! gives (4). Every falling factorial has a nonnegative integer index.

The logarithmic component is

    beta=calL((K-U)/(t-1))/U,                         (5)

where calL(g)=integral_-1^1 g((1+iu)/2)du. These are the complete rational components, not truncated errors.

## 4. Unique lowest dyadic term in the exponential numerator

Since J is a positive multiple of four, for 1<=h<=J,

    v_2((J)_h)>=floor(h/2)+1.                        (6)

For h=1,2,3 the initial factors J,J-1,J-2 prove the bound. For h>=4 the first four factors supply at least three powers of two, and the remaining consecutive factors supply at least floor((h-4)/2).

For j=N-h<N, the valuation bounds on b_j and (6) give

    v_2(b_j (J)_h D_j)>=N/2+1.

The last term j=N has valuation exactly N/2. Indeed b_N=2^(N/2), and D_N is odd because N is even and D_N=N D_(N-1)+1. Therefore

    v_2(Vexp)=N/2,
    v_2(alpha)=N/2-v_2(n!)-v_2(J!)-v_2(U).           (7)

This conclusion does not require U to satisfy (3), only U!=0.

## 5. Logarithmic moments and complete noncancellation

For mu_r=calL(t^r), the explicit formula is

    mu_r=((1+i)^(r+1)-(1-i)^(r+1))/(i 2^r(r+1)).

It implies

    v_2(mu_r)>=1-floor((r+1)/2).                     (8)

If r+1 is divisible by four, the moment is zero. For odd r+1 or r+1 equal to two modulo four, writing powers of 1+i and 1-i gives the bound directly, with their respective powers of two retained.

Expanding (K-U)/(t-1) as a sum of its degree-j coefficients times 1+t+...+t^(j-1), equations (8) and v_2([t^j]K)>=ceil(j/2) show

    v_2(calL((K-U)/(t-1)))>=1,
    v_2(beta)>=1-v_2(U).                             (9)

For every positive integer a divisible by four, v_2(a!)>=3a/4, by grouping its factors into blocks of four. Since n and J are such integers,

    v_2(n!)+v_2(J!)>=3N/4.

Thus (7) is strictly smaller than the lower bound (9). Also U is divisible by 2^(n/2), so (7) is negative. The exponential and logarithmic components cannot cancel at their least dyadic order. The ACTUAL reduced denominator therefore satisfies

    v_2(q)=v_2(n!)+v_2(J!)+v_2(U)-N/2.              (10)

This is an equality after final rational reduction, not a denominator-clearer estimate.

On the allocation (3), Legendre's binary factorial formula gives

    v_2(q)=3n/2+2m-s_2(n)-s_2(n+4m),                (11)

where s_2 is binary digit sum. For m=rho n log n+O(n),

    liminf log q/(n log n)>=2rho log 2.              (12)

No complete-error conclusion follows from (12) alone.

## 6. Improved denominator bound for beta

Let O_N be the lcm of the odd positive integers at most N. On allocation (3), U0=K0(1) is odd. Equation (8) and the coefficient bounds for K0 give

    den(beta) divides 2^(n/2-1) O_N |U0|
                       =O_N |U|/2.                  (13)

The odd part follows because the odd denominator of mu_r divides the odd part of r+1. The dyadic part follows term by term from

    v_2([t^j]K0)>=ceil(j/2)-n/2.

Thus the moment contribution to the dyadic denominator does not grow with m. The odd denominator and the exponential/logarithmic cancellation at odd primes remain separate questions.

A convenient all-size bound is lcm(1,...,a)<=4^a. Here is an elementary induction. For a=2r, the quotient lcm(1,...,2r)/lcm(1,...,r) divides binom(2r,r), so the inductive bound and binom(2r,r)<=4^r suffice. For a=2r+1, compare with lcm(1,...,r+1); the quotient divides binom(2r+1,r)<=4^r, because the two central binomial terms are equal. A newly appearing prime power is above the smaller endpoint and contributes a prime factor to the binomial coefficient; the interval ratio is less than or equal to two, so no larger exponent increment is needed. The case a=1 starts the induction. In particular O_N<=4^N.

## 7. New archimedean bound for the actual forcing normalization

For m>0, take a Cauchy circle of radius r=sqrt(n/(4m)) in (1). The coefficient bound and elementary exponential inequalities give

    |U|<=r^(-n)(1+2r+2r^2)^n(1+2r^2)^(2m)
         <=(4m/n)^(n/2) exp(n+n sqrt(n/m)).           (14)

Indeed 1+2r+2r^2<=exp(2r), and (1+2r^2)^(2m)<=exp(4mr^2). This estimate does not assume coefficient positivity in (1); absolute values are taken only for the upper bound.

For m=rho n log n+O(n), equations (3) and (14) imply

    (n/2)log 2<=log|U|<= (n/2)log log n+O_rho(n).

In particular log|U|=o(n log n). The actual forcing normalization has much smaller logarithmic height than the selector coefficient height, which is exactly

    H=7^(2m).

This fact must be retained when assessing the denominator budget.

## 8. Additional reduced-denominator rate constraint

Let Bbeta=den(beta). The complete exponential bound from the general selector argument gives

    0<|e-alpha|<=27(2M)^n H/[(n+1)n!|U|],
    M=1+sqrt(2).

Since alpha=c-beta, its reduced denominator is at most q Bbeta. The saved elementary approximation bound for e yields, for every epsilon>0,

    (2+epsilon)(log q+log Bbeta)
       >=log(n!)-log(H/|U|)-O_epsilon(n).

Use (13)-(14), O_N<=4^N, and m=rho n log n+O(n). Letting epsilon decrease to zero proves

    liminf log q/(n log n)
      >=max{2rho log 2, 1/2-rho log 7-4rho log 4}.    (15)

The second lower bound is conservative because it replaces the actual odd logarithmic denominator by an lcm bound. Both inequalities concern the same fully reduced q. In particular the right side of (15) is at least log 2/log 7168 for every fixed rho>0: the two affine functions meet at rho=1/(2log 7168).

This new estimate supplies a compulsory denominator cost throughout this explicit family. It is not a proof of divergence of its primitive forms: the complete error could conceivably decay at a sufficiently strong n log n rate. Establishing its actual rate, including the exponential contribution and signed contour cancellation, is the next analytic task.

## 9. Scope

Equations (3), (10)-(11), and (14)-(15) are new author deductions awaiting the limited examination requested from Child 4. They preserve the unsaved nonvanishing and dyadic arguments and add an actual forcing-height budget. No existing certificate is overwritten and no computation is claimed.

The unresolved quantities are the complete large-degree error, the actual odd denominator cancellation, and the resulting primitive form. The unconditional rationality or irrationality of e+pi remains open.
