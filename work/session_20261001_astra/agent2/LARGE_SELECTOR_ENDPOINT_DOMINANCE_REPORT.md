> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large selector endpoint report

New author analytic result; the main dyadic allocation and actual denominator theorem remain provisional arithmetic inputs. No scans or old checks were repeated.

A signed asymptotic lower bound on an explicit unbounded subsequence is still open. The delivered alternative is an explicit two-contribution formula with a uniform bounded remainder.

For alpha=(1+i)/2, h=-i/2, expand the retained rational differential as G(alpha+z)=sum_(j>=n)g_j z^j. The note gives every g_j by a finite formula in Q(i), retaining the EXACT congruence-adjusted m. Put

    Z_K=-sum_(j=n)^K g_j h^(j+1)/(j+1).

The open contour has contributions Z_K+r_K and -conjugate(Z_K+r_K). Thus

    Flog=(-1)^(n+1)4n! Im(Z_K+r_K).

A Cauchy estimate on radius 3/5 proves

    |r_K|<=3*10^(n+1)*25^m*(5/6)^(K+1)/(K+2).

An explicit K=O_rho(n log n) makes the normalized logarithmic remainder at most exp(-2n log n). This is a convergent expansion of growing depth, not an unjustified fixed-order Watson approximation.

With D=n!2^(-n)U and

    A_K=(-1)^(n+1)2^(n+2)Im Z_K/U,

one obtains the COMPLETE enclosure

    |c-(e+pi)-A_K|<=Delta_K,
    Delta_K=2^(n+2)|r_K|_bound/|U|
       +27(2(1+sqrt(2)))^n 7^(2m)/((n+1)n!|U|).

The second term is the entire exponential residual. Its logarithmic upper rate is -(1-2rho log 7)n log n+O_rho(n), so it is factorially small in the requested rho range.

The precise noncancellation condition is |A_K|>Delta_K. It gives the full-error sign and lower bound |A_K|-Delta_K. No claim that this condition holds on an explicit unbounded subsequence is made.

The ACTUAL denominator input gives q>=q2, where

    q2=2^(3n/2+2m-s2(n)-s2(n+4m)).

Consequently the primitive form has lower bound q2(|A_K|-Delta_K) whenever positive. Establishing a signed margin of rate exp(-sigma n log n) with sigma<2rho log 2 would imply subsequence divergence. That margin remains unproved; no raw denominator clearer is used in this test.

The separately saved small-saddle correction records +1/2 rather than -1/2. Earlier saddle results are preserved. The new formulas do not discard either conjugate contribution or treat the O(n) adjustment of m as phase-negligible.

Files: LARGE_SELECTOR_ENDPOINT_DOMINANCE.md and this report. Read-back remains required before reporting completion.
