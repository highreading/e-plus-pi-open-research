> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Toeplitz local arithmetic report

New author deductions, offline, 2026-10-01. No scans, HP sweeps, old audits, or repeated controls were performed.

Use 0<=i,j<b, p>2b+3 odd with the additional restriction p>=3b, n=ap+r, and

 b<=r<=floor((p-b)/2).

This nonempty interior range keeps r+i-j>=0, r+i<p, and 2r+i<p. The proof establishes integrality of the proposed row normalization 2^n(n+i)! for the matrix and BOTH forcing columns before reduction.

Write the normalized positive forcing as P and the second forcing as Z=E+L. The exact separation is

 P=(n!)^2 V,
 V_i=((n+i)!/n!) 2^n [z^(n+i)]Q0^n/(1-z)^(n+1).

For every a>=1 the actual-family all-index transfer is

 M(n)=2^a M(r),
 V(n)=2^a h_a V(r),
 Z(n)=2^a E(r) mod p,

where h_a=[w^a]Q0(w)^a/(1-w)^(a+1) has an explicit dyadic multinomial sum. Its unit status is not assumed. The second forcing transfers to the EXPONENTIAL seed, not generally the complete seed.

The logarithmic recurrence has an exceptional block L_(p+t)=-2(-1)^((p-1)/2)t! mod p and vanishes from index 2p onward. This boundary is retained. A stronger bound for its normalized row is

 v_p(L_i)>=v_p(n!)+v_p((n+i)!)-floor(log_p(2n+b-1)).

Concrete conditional gates: a unit residual column-replacement determinant for V gives min v_p(x_P)=2v_p(n!)-v_p(det M); a unit replacement determinant for the exponential seed gives min v_p(x_Z)=-v_p(det M). These are exact valuations of actual forcing responses, conditional on the specified residual tests and det M!=0 over Q. Neither determinant nor numerator is assumed to be a unit. A left-nullvector test also gives an explicit obstruction to integral solutions of the combined forcing equation.

Raw positive-column reduction is stopped as vacuous when n>=p. If h_a or all residual replacement determinants vanish, the required lift is the first nonzero coefficient of the actual determinant and replacement determinants modulo higher powers of p. Combined forcing requires the complete numerator (n!)^2 X C_j+Y D_j, including possible equal-depth cancellation and the logarithmic contribution when it reaches the required precision.

No unit test was asserted to hold uniformly or numerically evaluated. The note provides the local transfer input for Child 4; it does not choose a center or equate a row clearer with its reduced denominator.

Full derivation: work/session_20261001_astra/agent1/TOEPLITZ_LOCAL_ARITHMETIC.md.
