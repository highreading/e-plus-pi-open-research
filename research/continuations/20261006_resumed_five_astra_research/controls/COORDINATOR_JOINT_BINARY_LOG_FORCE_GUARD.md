> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Joint symbol/logarithmic protection for the complete binary force

This coordinator derivation is submitted for independent mathematical audit. It uses the exact complete finite source in A5turn10, not an exponential-only replacement. Scoped archive searches located the older bound of approximately n/2, but no completed use of the following joint s+(2n+i-s) estimate. Classical factorial valuation and integer binomial expansions are reused. No exhaustive novelty claim is made.

Let phi(z)=1-z+z^2/2, lambda_s=s![z^s]phi(z)^n, and let F(0)=0, F'(z)=2/phi(z). Put g_r=F^(r)(0) and L_m=m![z^m](e^z F(z)), so L_m=m L_(m-1)+g_m. The complete source is

    h_i^F = sum_(s=0)^(n+i) lambda_s binom(n+i,s) L_(2n+i-s), 0<=i<b.

Every original contact row and source summand remains. Assume positive integers b<=n, and put ell=floor(log2(2n+b-1)).

## 1. Paid symbol coefficient bound

The exact ordinary coefficient expansion is

    [z^s]phi(z)^n = sum_(r=0)^floor(s/2) (-1)^(s-2r) binom(n,s-r) binom(s-r,r) 2^(-r).

Terms outside polynomial degree are zero. Both binomial factors are integers. Consequently

    v2(lambda_s) >= v2(s!)-floor(s/2) = ceil(s/2)-s2(s).

The right side is a lower bound and may be negative at a small s; that causes no invalid inversion. One can take its maximum with the established integrality bound0 when useful. For s=0 the displayed expression is exactly0.

## 2. Paid logarithmic exponential coefficient bound

The exact identity

    1/phi(z) = (1+z+z^2/2)/(1+z^4/4)

gives v2([z^k]1/phi)>=-floor(k/2), including its zero coefficients. Since g_r=2(r-1)![z^(r-1)]1/phi,

    v2(g_r) >= 1+v2((r-1)!)-floor((r-1)/2).

Furthermore the whole exponential convolution is

    L_m = sum_(r=1)^m m!/r! * g_r.

Thus every summand, and hence L_m as a whole, has valuation at least

    1+v2(m!)-floor(log2m)-floor((m-1)/2)
    = floor(m/2)+2-s2(m)-floor(log2m).

No factorial denominator is inverted modulo2. The formula is an exact integer identity; the displayed valuation payment precedes reduction.

## 3. Joint estimate on each complete force summand

Set m=2n+i-s. Then n<=m<=2n+b-1, and s+m=2n+i. The integral binomial multiplier contributes nonnegative valuation. Combining the two paid bounds gives

    v2(lambda_s binom(n+i,s) L_m)
    >= ceil(s/2)+floor(m/2)+2-s2(s)-s2(m)-floor(log2m)
    >= n+floor(i/2)+2-s2(s)-s2(m)-floor(log2m).

Both s and m are at most2n+b-1; therefore s2(s),s2(m)<=ell+1 and floor(log2m)<=ell. This proves the uniform whole-source bound

    v2(h_i^F) >= n+floor(i/2)-3ell >= n-3ell, 0<=i<b.

The outer sum has not been shortened, and cancellation can only increase its valuation. The gain comes from retaining BOTH coefficient factors rather than discarding the valuation of lambda_s.

## 4. Transport into the actual binary columns

For the retained binary even producer A^(-1) and the reconstruction R are integral over Z2. The actual logarithmic part of the normalized second column is

    y^F = R A^(-1) h^F /(4b!).

Hence

    y^F in 2^Bnew Z2^(b+1),
    Bnew = n-v2(b!)-2-3ell
         = (1-1/4002)n+O(logn)

on n=4002b. This retains the actual division by4b!, the same finite inverse and every reconstructed row0..b. The physical terminal is already in the exponential part and has not been moved into a logarithmic source.

If x=2^a x0 with x0 primitive and nu=v2(x0^T x0), then the logarithmic mixed contraction has valuation at least a+Bnew. It may be omitted for testing delta2=v2(H)-v2(N)>=k only when

    Bnew >= a+nu+k

(with a strict inequality when the first nonzero target digit is to be preserved). The new bound does not prove a or nu sublinear. At the necessary k~.54109n, it protects the target if a+nu is below approximately.45866n with the exact logarithmic losses paid. Any case violating that condition remains a genuine deep-norm/content exception requiring actual analysis.

At the proposed auxiliary b9,n36018, ell=16 and v2(9!)=7, so Bnew=35961>20000. Therefore the specified twenty-thousand-bit logarithmic diagnostic vanishes by proof if these identities are accepted; computing its full source to rediscover this zero is unnecessary. No result of that unexecuted diagnostic is claimed.

This does not change the exact prime3 denominator, the shallow-binary scale obstruction, or any whole real error. It only strengthens the modular complete-logarithmic guard. It gives no rationality or irrationality decision for e+pi.
