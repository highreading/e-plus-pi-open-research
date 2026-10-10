> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large selectors: a factorial exponential-error bound for every fixed rho

Status: new main-agent author deduction, not independently reviewed. This extends LARGE_SELECTOR_DYADIC_DENOMINATOR_DRAFT.md without changing its preserved arguments. No computation, numerical experiment, or completed-check replay is claimed. The result bounds the exponential component, not the complete error involving pi.

## 1. Exact exponential component

Let n>=1, m>=0, and define

    B(t)=(1-2t+2t^2)^n(1-4t+2t^2)^(2m)
         =sum_(j=0)^N b_j t^j,
    N=2n+4m,
    K(t)=t^n B^(n)(t)/n!, U=K(1).

Assume U!=0. For the direct saddle-selector center write c=alpha+beta, with alpha its rational exponential component and beta its rational logarithmic component. Set E_j=sum_(r=0)^j 1/r!. The exact forcing normalization gives

    alpha=(1/U)sum_(j=n)^N binom(j,n)b_j E_j,
    U=sum_(j=n)^N binom(j,n)b_j.

Consequently the COMPLETE exponential error is

    e-alpha=(1/U)sum_(j=n)^N binom(j,n)b_j(e-E_j).    (1)

This formula retains the entire exponential tail. In particular, no large-degree selector coefficient has been discarded.

The elementary bound

    0<e-E_j<3/(j+1)!

implies

    |e-alpha| < 3/(n!|U|)
       sum_(h=0)^(N-n) |b_(n+h)|/[(n+h+1)h!].       (2)

Since alpha is rational, e-alpha is nonzero.

## 2. Coefficientwise majorization

All coefficients of B alternate in sign. Indeed B(-t) is a product of polynomials with nonnegative coefficients. Thus |b_j| is the coefficient of t^j in

    (1+2t+2t^2)^n(1+4t+2t^2)^(2m).

Coefficientwise, as power series with nonnegative coefficients,

    1+2t+2t^2 <= exp(2t),
    1+4t+2t^2 <= exp(4t).

Multiplication preserves this ordering. With the positive integer

    Lambda=2n+8m,

we obtain the explicit all-degree bound

    |b_j|<=Lambda^j/j!.                              (3)

This avoids the former replacement of the entire coefficient sum by the selector height 7^(2m).

Since (n+h)!>=n!(n+1)^h, equation (3) gives

    sum_(h=0)^(N-n) |b_(n+h)|/h!
       <= Lambda^n/n! * exp(Lambda/(n+1)).

Together with (2), this proves

    0<|e-alpha| <
      3 Lambda^n exp(Lambda/(n+1)) /
      [(n+1)(n!)^2 |U|].                             (4)

Equation (4) holds for every n>=1 and m>=0 on U!=0. It needs no contact normality, inverse estimate, saddle approximation, or coefficient-sign assertion about U.

## 3. Large-degree consequence

Fix rho>0 and suppose

    m=rho n log n+O(n).

Then Lambda=8rho n log n+O(n), and the logarithm of the right side of (4) is

    -n log n+n log log n+O_rho(n)-log|U|.             (5)

Thus the exponential component remains factorially accurate for EVERY fixed rho>0. The older restriction rho<1/(2log 7), arising from the crude selector-height bound, is unnecessary for this purpose.

On the explicit congruence allocation in LARGE_SELECTOR_DYADIC_DENOMINATOR_DRAFT.md, n=4k and m=-k modulo a power of two P with k<P<=2k. The earlier author argument gives

    U!=0, v_2(U)=n/2,
    log|U|<=n log log n/2+O_rho(n).

Therefore the normalization in (5) is explicit and subleading at the n log n scale. The congruence adjustment of m remains O(n); its effect on oscillatory phases is not ignored.

## 4. Stronger compulsory reduced-denominator rate

Retain the exact logarithmic-denominator bound from the preceding dyadic draft:

    Bbeta=den(beta) divides O_N |U|/2,

where O_N is the lcm of odd positive integers at most N. Its proved coarse bound is O_N<=4^N.

Let q be the ACTUAL positive reduced denominator of c=alpha+beta. Then den(alpha)<=q Bbeta. The saved elementary rational-approximation bound for e states that, for every fixed epsilon>0, some C_epsilon>0 satisfies

    |e-alpha|>=C_epsilon(q Bbeta)^(-2-epsilon).

Combining this with (4), and writing A=|U|, gives

    (2+epsilon)log q >=
       2log(n!)-n log Lambda-Lambda/(n+1)
       -(1+epsilon)log A-(2+epsilon)log O_N
       +log(n+1)+O_epsilon(1).                       (6)

The constant in the last term incorporates the harmless factors 2 and 3. No product of separately cleared center denominators is substituted for q.

For the fixed-rho congruence allocation, divide (6) by n log n, use log A=o(n log n), and then let epsilon decrease to zero. This gives

    liminf log q/(n log n)>=1/2-4rho log 4.           (7)

The exact dyadic law in the preceding author draft separately gives

    liminf log q/(n log n)>=2rho log 2.

Thus the strengthened combined constraint is

    liminf log q/(n log n)
      >=max{2rho log 2, 1/2-4rho log 4}.              (8)

In particular the right side is at least 1/10 for every fixed rho>0. To see this put x=2rho log 2; the two terms become x and 1/2-4x, whose maximum is minimized at x=1/10. Equivalently the meeting value is rho=1/(20log 2).

The new coefficientwise bound removes the former negative term -rho log 7 from this denominator budget. Equations (7)-(8) remain author consequences of the named exact dyadic and logarithmic-denominator inputs until their limited examination completes.

## 5. What this resolves and what it does not

The complete exponential contribution is now controlled at factorial scale for all fixed rho. The logarithmic contribution still needs a uniform signed estimate on the same nonvanishing sequence. If its error obeyed a lower bound

    |beta-pi|>=exp(-a n log n+o(n log n))

with a<min(1, max{2rho log 2, 1/2-4rho log 4}), then (5) would make the exponential error negligible relative to it, and (8) would force divergence of these primitive forms. No such logarithmic-error lower bound is asserted here.

For example, a proved logarithmic error of size exp(-O(n log log n)) on an unbounded subsequence would suffice to stop that subsequence. Oscillatory conjugate contributions might prevent such a lower bound; their cancellation cannot be discarded.

Conversely, a successful construction would have to make its COMPLETE error overcome the actual denominator cost, including the compulsory dyadic contribution. A small raw logarithmic integral or a nonzero integer U is insufficient.

This note supplies a new uniform exponential estimate and a stronger arithmetic constraint. It does not settle the rationality or irrationality of e+pi.
