> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Targeted literature comparison: modular Wronskian reduction

2026-09-13. Root reviewed the primary PDF of Codrut Grosu and Corina
Grosu, [The irreducibility of some Wronskian Hermite polynomials](https://arxiv.org/pdf/2007.00065),
Theorem 8 and its Section 5 proof (PDF pages 4 and 18–19; numbering in
the displayed version). The preprint identifier dates to 2020; search
engine crawl dates are not publication dates.

Theorem 8 reduces normalized Hermite Wronskians by reducing their degree
sequence modulo an odd modulus, under coprimality of that modulus with
the original degree Vandermonde. The proof uses the ordinary Hermite
congruence, derivative compatibility, and an invertible Vandermonde.
Their Theorem 7 also gives Newton-polygon slope bounds under separate
hypotheses; it is not an endpoint gcd estimate for this project.

## Exact relevance to the current original construction

The elementary Wronskian inflation mechanism in the new session proof
has a classical close analogue. No global novelty is claimed for that
mechanism. The current Appell sequence has generating function
exp(xt)(1+t^2)^n, so the Hermite theorem is not directly its theorem.
We proved the needed ordinary Appell congruence from its integer
falling-factorial expansion.

More importantly, the original rectangle has degree set n,...,2n.
For fixed p and sufficiently large n its original Vandermonde is
p-divisible. Directly reducing that original normalized determinant
would divide by a nonunit. Merely copying the Hermite conclusion would
therefore leave the central obstruction unresolved.

The new proof first invokes the separately verified INTEGRAL
same-size central-character comparison. It replaces the rectangle,
modulo p, by a same-size partition obtained from a small rectangle
by enlarging its first row. Only after that step does it use the
Wronskian calculation. The new degree set has pairwise distinct residues
when p>2k, so its Vandermonde is a unit. The original primitive b vector,
exact differential identity, and integer endpoint border then transfer
the congruence to V and Pe. Those additional steps are indispensable
for a statement about the actual reduced denominator q_n.

The most useful next problem remains exceptional finite seed primes
and the complementary negative residue classes. Neither the quoted
Hermite theorem nor its Newton-polygon theorem supplies a bound for
cancellation in Pe+4Pa at a singular seed. The same-size comparison
plus a valid unit-denominator model is the current concrete route.
