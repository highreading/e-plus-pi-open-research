> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Proposed classical-logarithm route to actual Jacobi continuation

Status: a coordinator proposal, not a verified application of a published theorem.
The unresolved object is exactly A1 turn30's later-resonance block, not a new
construction. Archive checks found the existing Matveev application audit,
which should be reused for the classical theorem. No specific 243/4 or
Bugeaud continuation application was located in the bounded searches.

Primary literature located before this proposal:

* E. M. Matveev, Corollary2.3, DOI10.1070/im2000v064n06ABEH000314:
  https://www.mathnet.ru/eng/im314 . The archive already contains a precise
  application audit and complete-source provenance; it is attached separately.
* Y. Bugeaud and M. Laurent, Journal of Number Theory61(1996),311--342,
  DOI10.1006/jnth.1996.0152. Publisher abstract confirms two-power p-adic
  bounds, but does not supply a theorem statement sufficient for the next claim.
* T. Yamada's primary note, https://arxiv.org/pdf/math/0607072 , Theorem1.1
  gives a determinant-parameter version with cardinality hypotheses. It is
  not automatically the simplified bound proposed below.

Every denominator factor is
4A+1+4b-2i=4^(j+1)-(2i+3-4b).
For i in the later-resonance block, the integer B=2i+3-4b is positive,
bounded by O(u), and either is not a 3-adic unit (valuation0 immediately),
or can be addressed by a two-logarithm theorem. A sufficient classical
bound, to be sourced and verified, is

v3(4^(j+1)-B)<=C(1+log B)(1+log(j+1))^2.

If4 and B are multiplicatively dependent, B is a positive power of2.
The relevant B=1mod3 forces an even exponent, so LTE supplies a bound
O(log(j+1)), provided the difference is nonzero. In the actual intermediate
range i<2h=O(j), B cannot equal4^(j+1) for largej.

For a>L=floor(log3u), at most one denominator residue occurs in [0,u).
These residues are nested as a increases. Hence the entire high-depth
unmatched count is at most the maximum valuation of one denominator
factor, rather than u times that maximum. A1 turn30(16) would then give

v3(R_bu)>=u+t-L-C(1+log u)(1+log(j+1))^2.

To make this sufficient uniformly for u>=3^t, choose a simultaneous
original-index family with exact resonance deptht, the real window,
and log(j+1)=O(t). Density alone did not supply this, but the classical
real logarithm bound may do so quantitatively:

Matveev applied to q log4-a log3 gives ||q log_3(4)||>=c q^-K,
for fixed effectiveK,c>0. In either exact-resonance progression
j=j0+M k, M=3^t, its rotation step is beta=M log_3(4).
Continued fractions plus ||q beta||>=c(Mq)^-K should produce a
fixed-window hitting bound k<=C M^Kprime. This implies j<=C3^(Kt)
and hence logj=O(t), without building huge4^j.

If both classical bounds pass their exact hypotheses, 3^t dominates
the O(t^3) loss throughout the later-resonance block, and continuation
closes for sufficiently larget on an infinite original family. The
finite fixed part, nonresonant sum and u>=2h tail remain as in turn30.

This still concerns only the core polynomial. It does not evaluate the
terminal Wronskian, strengthen actual polynomial precision beyond3^6,
or control the final gcd and primitive denominator. Missing theorem
hypotheses or an unsourced simplified p-adic estimate must be reported
as a conditional dependency, never silently assumed.
