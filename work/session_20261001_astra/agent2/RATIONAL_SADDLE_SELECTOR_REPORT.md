> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rational saddle selector report

New author analytic result; no numerical scans or independent review.

For L_m(t)=(2t^2-4t+1)^(2m), the complete positive and logarithmic forcing contractions both contain the exact factor

    (-4)^m sin(theta)^(2m) cos(2m theta).

Their scalar weights are respectively (1+sqrt(2)cos theta)^n on the full circle and (sqrt(2)cos theta-1)^n on the logarithmic arc. Both conjugate contributions and all signs are retained before estimates.

A uniform Gaussian-moment estimate is proved for n>=exp(100), 0<=m<=log n. Its explicit relative error is at most

    eps=100(m+1)^2 n^(-3/5)
           +2exp(5(m+1)-n^(1/5)/32)<1/4.

It proves denominator nonvanishing and sign D_n(L_m)=(-1)^m before any quotient is used.

The normalized logarithmic residual is

    (-1)^(n+1)4pi s^(n+m+1/2)(1+O(eps)),
    s=(sqrt(2)-1)^2,

with relative-error bound 2eps/(1-eps). The n^(-m) factors cancel, but the different saddle curvatures leave a genuine additional factor s^m. Thus conjugate vanishing does NOT imply complete loss of the approximation gain.

The complete exponential residual divided by the same denominator is bounded by

    Bexp=24pi (1+sqrt(2))^(2m)(n c_plus)^(m+1/2)
                  /[(n+1)n! Gamma(m+1/2)],
    c_plus=sqrt(2)/(2(1+sqrt(2))).

This is factorially smaller than s^(n+m+1/2), uniformly for m<=log n. The research note gives the full signed additive enclosure, retaining the exponential term. Consequently the complete rational error has the same signed leading term uniformly in this growing range.

For m=floor(kappa log n), 0<kappa<=1, the extra gain is polynomial, n^(-2kappa log(1+sqrt(2))) up to bounded rounding factors. The principal exponential rate is unchanged. Require 4m<b in a forcing window; b=4m+1 is eventually compatible with the earlier slow-growth domain.

This is a gain in the actual quotient error, not merely its raw residual. No estimate for the quotient's fully reduced denominator is proved, so no shrinking integer form or irrationality conclusion follows. The result neither optimizes nor excludes other rational selectors.

Saved proof: RATIONAL_SADDLE_SELECTOR.md. The initial working note and earlier reconstruction results are preserved. Both final deliverables require read-back.
