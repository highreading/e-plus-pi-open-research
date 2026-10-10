> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: relative error and dyadic denominator growth

Date: 2026-09-13. Reviewer: root. FULL PASS.

Reviewed raw_relative_error_dyadic_denominator_growth.md using the exact
dyadic denominator theorem and the independently passed endpoint error.

Reduced numerators are odd, and the dyadic depths strictly increase.
Thus the two terms of every indicated determinant have different
valuations, giving exactly the earlier depth, not merely a lower bound.
The adjacent depth changes 4 and 2 match the floor formula. The
alternating error yields the factor 1+rho^10 in its absolute size.

The denominator-product bound and both limsup constants follow with
the correct factor of two. They are not all-index exponential lower
bounds. The strengthened version divides by the entire denominator
gcd, including prime powers in the odd part. The quotient is odd;
the associated spacing is exactly the reciprocal lcm lower bound.

For arbitrary later indices, the error estimates are uniform because
the tail supremum of the relative asymptotic error tends to zero.
The main difference factor is bounded below by 1-r^2 and above by
1+r, so the uniform relative-error assertion is justified. Fixed and
growing gaps have their different scale factors retained.

The two neighboring odd-factor restrictions follow by multiplying
the spacing bound by q_n|epsilon_n|/|epsilon_n-epsilon_m|. The earlier
neighbor cancels its entire dyadic factor; the later neighbor leaves
2^(a_n-a_(n+2)), equal to 1/16 or 1/4. Both have the stated positive
limits. For arbitrary gaps this factor cannot be omitted, and the
note correctly retains it.

These are necessary restrictions and limsup growth theorems. They
do not establish a shrinking subsequence, a factorial denominator
divisor, bounded neighboring odd quotients, or irrationality of e+pi.
