> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the large-prime nullity and Smith reduction

Date: 2026-09-13. Root verification of
`raw_large_prime_nullity_and_smith.md`.

**Verdict: the rank restrictions and exact local Smith formulas pass.**

For a nonzero high-kernel triple of degree at most n-1, the reviewed
origin order and degree bound force N=kappa z^(3n-1). Its top
coefficient is b_(n-1) times the displayed quadratic expression;
kappa!=0 therefore makes the top-B linear functional injective on
this entire subspace. Its dimension is at most one. Degrees at most
n-2 are impossible by the same order/degree comparison. At n=1,
the convention for negative-index coefficients gives b0*c0^2,
which is the correct degree-two leading coefficient for constants.

For any three high-kernel triples, replacing the first column of
their coefficient determinant by the truncated remainders changes
no determinant. The resulting order exceeds its original degree
3n, so the determinant is identically zero. Its degree-3n
coefficient bounds the leading-coefficient image dimension by two.
Together with the preceding one-dimensional kernel bound this
gives high nullity at most three over every F_p, p>3n.

In the exceptional case, T and zT satisfy the same high conditions
and are independent; a third vector S completes the asserted basis.
The common-factor contradiction for T compares 3m with an origin
order h<=m and correctly uses only the allowed truncated jets.
The endpoint functional takes the same value on T and zT, so the
two equations on T,S are exactly the remaining nullity-three
condition. Their compatibility with (z-1)T is real; the carrier
argument supplies no exclusion.

Over Z_p the characteristic-zero rank and the residue-field bound
permit an identity block of size 2n-1 with the single remaining
high row (p^e,0,0). Eliminating the initial coordinates of the
endpoint row leaves the displayed 2-by-3 block. The gcd of its
entries has valuation min(e,v(a),v(b),v(c)); the gcd of its maximal
minors has valuation e+min(v(b),v(c)). These are exactly the first
Smith valuation and the sum of the two. The case e=0 is included;
then the first invariant is a unit. The integral free kernel of
the high matrix is the last two coordinate directions, so the
interpretation of the second term as endpoint-functional content
is also correct. The modular torsion direction explains why a
vanishing restriction on that integral kernel alone does not force
nullity three.

The result limits the number of positive Smith valuations and
separates their two sources. It neither bounds their magnitudes nor
proves that the exceptional case occurs. No sample was needed in
this review.
