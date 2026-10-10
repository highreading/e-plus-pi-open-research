> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Joint companion and cancellation-deficit budgets

Status: main-agent author proofs, not independently reviewed. This note preserves the previously unsaved q-times-deficit bound and joint complete-error budget. It uses the retained elementary approximation theorem for e and the published pi theorem whose statement and quantifiers were inspected in the retained Zeilberger–Zudilin primary text. No numerical calculation is claimed. These are constraints on rational approximation families, not a decision about the irrationality of e+pi.

## 1. Reduced denominators and cancellation deficit

Let alpha and gamma be rational numbers. Define

    c=alpha+gamma,
    Q=den(alpha), B=den(gamma), q=den(c),
    C=gcd(q,B), delta=B/C.

All denominators are positive and reduced, including den(0)=1. Rational addition and subtraction imply

    q divides lcm(Q,B),
    Q divides lcm(q,B).

Taking the least common multiple with B proves exactly

    lcm(Q,B)=lcm(q,B)=q delta.                     (1)

The deficit delta is a positive integer. It also divides gcd(Q,B). To see this prime by prime, write a=v_p(Q), b=v_p(B). When a differs from b, the deeper denominator cannot cancel, so v_p(q)=max(a,b) and v_p(delta)=0. When a=b=t>0, the loss in the summed numerator is between zero and t, and is exactly v_p(delta). If a=b=0 there is no loss.

For an explicit common integer representation

    alpha=U/D, gamma=V/D, D>0,

put

    g_e=gcd(D,|U|), g_gamma=gcd(D,|V|),
    g_c=gcd(D,|U+V|), g_0=gcd(D,|U|,|V|).

Then

    Q=D/g_e, B=D/g_gamma, q=D/g_c,
    delta=g_c/g_0.                                (2)

Indeed gcd(g_c,g_gamma)=g_0, so B/gcd(q,B)=g_c/g_0. These formulas are invariant under a common scaling of D,U,V and include zero numerators.

The quantity delta measures additional cancellation in the sum after removing the common content of both companions. It must not be replaced by that common content or by the size of an unreduced denominator.

## 2. A denominator-product lower bound independent of the complete error

Suppose E>0 and |e-alpha|<=E. For every epsilon>0, the retained elementary theorem supplies C_epsilon>0 such that

    |e-u/v|>=C_epsilon v^(-nu), nu=2+epsilon,

for every reduced rational u/v. Applying it to alpha and using Q<=q delta from (1) gives

    E>=C_epsilon Q^(-nu)>=C_epsilon(q delta)^(-nu).

Consequently

    q delta>=C_epsilon^(1/nu) E^(-1/nu).           (3)

This needs no assumption about the complete approximation error or about pi.

Let X tend to infinity and assume

    liminf (-log E)/X>=a>0.

Taking logarithms in (3), then epsilon decreasing to zero, proves

    liminf (log q+log delta)/X>=a/2.               (4)

In particular, for factorial exponential accuracy with X=n log n and a=1:

    log q=o(X) implies liminf log delta/X>=1/2;
    log delta=o(X) implies liminf log q/X>=1/2.

More generally, limsup log q/X<=u gives

    liminf log delta/X>=max(0,a/2-u).              (5)

Because delta divides both Q and B, a small-q target also requires at least this much common denominator mass in both companions. Thus q=exp(O(n)) under factorial exponential accuracy requires B, Q, and their additional cancellation deficit delta to have factorial-scale size. This is a necessary requirement, not a construction achieving it.

## 3. Joint complete-error inequality

Use the safe exponent mu=36/5. The retained primary text of Zeilberger–Zudilin, arXiv:1912.06345v2, page 1, gives an irrationality-measure bound strictly smaller than 36/5. Its quantifiers, together with irrationality of pi and a decreased constant for bounded denominators, imply

    |pi-u/v|>=C_pi v^(-mu)

for some C_pi>0 and every reduced rational u/v. This uses a published theorem; it is not a new audit of its complete proof. No extra epsilon above 36/5 is necessary here, because 36/5 itself is already strictly above the published bound.

Put S=e+pi and R=q|c-S|. The complete decomposition gives

    C_pi B^(-mu)<=|pi-gamma|<=E+R/q.

Equation (3) implies

    1/q<=C_epsilon^(-1/nu) E^(1/nu) delta.

Therefore

    C_pi<=E B^mu
       +R C_epsilon^(-1/nu) E^(1/nu) B^mu delta.  (6)

This retains both complete error components. It needs no logarithmic-dominance premise, contour-sign assertion, or dyadic denominator theorem. It remains valid when the complete error is zero.

## 4. Necessary joint cost for bounded primitive errors

Define the nonnegative joint cost

    Tcost=mu log B+log delta.

Suppose R is bounded and liminf (-log E)/X>=a>0. Then

    liminf Tcost/X>=a/2.                           (7)

Proof. If this fails, choose a subsequence and t<a/2 with Tcost<=tX. Since delta>=1, mu log B<=Tcost. The first term on the right of (6) tends to zero. Choose epsilon>0 so that t<a/(2+epsilon). The second term also tends to zero, after allowing arbitrarily small slack in the lower rate for -log E. This contradicts C_pi>0.

For a=1, X=n log n, the condition is

    liminf [(36/5)log B+log delta]/(n log n)>=1/2. (8)

Separate limiting rates for B and delta are unnecessary. The two costs may vary together along the sequence; equation (8) retains their actual same-index sum.

Since delta<=B, (8) recovers the necessary bound liminf log B/X>=5/82. If log delta=o(X), it strengthens that bound to 5/72. Neither subfactorial deficit nor eventual B|q is presumed.

## 5. A sufficient joint-cost criterion for divergence

Suppose instead

    limsup Tcost/X<=t<a/2.

Then E B^mu tends to zero. For all sufficiently large indices, it is at most C_pi/2. Rearranging (6) gives

    R>=(C_pi/2) C_epsilon^(1/nu)
                     E^(-1/nu)/(B^mu delta).

It follows that

    liminf log R/X>=a/2-t>0.                       (9)

This proves primitive-error divergence from an upper bound on the joint cost. A nonpositive lower bound at or beyond the threshold does not prove convergence, boundedness, or nonvanishing.

For a prescribed upper shrinking rate

    R<=exp(-sigma X+o(X)), sigma>=0,

the same subsequence argument in (6) gives the additional author consequence

    liminf Tcost/X>=min(a,a/2+sigma).               (10)

Indeed, below both thresholds the first term has negative exponent at most -a+t, and the second has negative exponent at most -sigma-a/nu+t for nu sufficiently close to two. Equation (10) is only a necessary joint budget, not an assertion that such shrinking occurs.

## 6. Canonical application and its distinct targets

The main has read agent3/CANONICAL_COMPANION_TRANSFER.md and CANONICAL_DENOMINATOR_OVERLAP.md. They give the actual factorial B-only decomposition c=alpha+gamma with gamma=kappa+beta, retain the endpoint correction, and prove factorial accuracy of the chosen positive exponential bound E within their stated even slow-growth author hypotheses.

For the common integer data Dcommon,U,V in that overlap note, the exact deficit is

    delta=gcd(Dcommon,|U+V|)
                 /gcd(Dcommon,|U|,|V|).

There are two distinct global arithmetic tasks:

1. A subfactorial upper bound for delta would force log q/(n log n) to have lower limit at least 1/2. This would exclude a geometric-denominator target q=exp(O(n)), without itself establishing complete-error nonvanishing.
2. An upper bound for (36/5)log B+log delta with rate strictly below 1/2 would prove complete primitive-error divergence by (9).

Neither bound is established globally for the canonical family.

The author overlap theorem on n=11^h+3, h>=6, b=3,m=1 gives v_11(delta)=1. That contributes only log 11 to log delta. Any factorial-scale deficit required by a small-q construction on that progression must therefore come from other primes. This observation does not bound their combined contribution.

The new coordinate report gives exact 13-adic overlap on a different construction. It must not be transferred to this Gram center. Its new proof is still awaiting main inspection at this checkpoint.

## 7. Status

Equations (1)-(10) are author deductions from the stated rational identities and approximation inputs. The canonical application retains the construction-specific hypotheses of the saved bridge. No new computation, independent review, or global gcd estimate is claimed. The irrationality or rationality of the actual number e+pi remains unresolved.
