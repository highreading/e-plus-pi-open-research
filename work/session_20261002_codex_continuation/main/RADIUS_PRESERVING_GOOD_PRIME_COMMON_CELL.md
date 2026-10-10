> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Radius-preserving good-prime common residue cell

Author result, 2026-10-02. This is original research within the continuing session. It does not decide the rationality of e+pi.

## Novelty and source gate

The archive was searched for a radius-preserving prime perturbation, a Rouché/common-cell construction, and a good-prime pullback common zero. The earlier single-jet endpoint tuning and the present session's Cartier and Mahler formulas are credited prerequisites. No completed example combining a certified radius above two with good-prime actual endpoint cancellation was found. A fresh online search inspected Waldschmidt's *Integer-valued functions, Hurwitz functions and related topics: a survey*, arXiv:2002.01223, Section 2.1, and primary author material on polynomial root perturbation. Flajolet–Sedgewick's author-hosted book gives the familiar zero-preserving perturbation principle. The proof below actually uses a uniform triangle inequality, so does not depend on an unverified numerical root calculation or a delicate version of Rouché's theorem.

Sources: https://arxiv.org/abs/2002.01223 ; https://algo.inria.fr/flajolet/Publications/book.pdf . The direct CUHK lecture PDF and the full book PDF fetch failed; their unavailable full text is not represented as having been read. The relevant author-hosted book theorem was returned in the search excerpt.

## Construction and analytic proof

Let P81 be the frozen degree-81 polynomial in `EXPLICIT_DEGREE81_RADIUS2005_CERTIFICATE.json`. Its exact Gaussian Schur certificate puts every zero of P81-(1+i) and P81-(1-i) strictly outside |z|=401/200. It has P81(0)=0, P81(1)=1, P81'(0)=1 and integral derivative jets. Define

    P(z) = P81(z) - 31 z^159(1-z)/159!.

This is a degree-160 rational polynomial with the same endpoint and first-derivative constraints and integral derivative jets. Its coefficient denominators are prime to 163.

For either puncture, the baseline polynomial has constant term of modulus sqrt(2), and factoring by its 81 roots gives, for every |z|<=2,

    |P81(z)-(1+-i)| > sqrt(2) (1-400/401)^81 > 401^-81.

The perturbation is bounded there by 31*3*2^159/159!. The stronger exact integer inequality

    81*3*2^159*401^81 < 159!

has been checked (71 bits of slack between the two integer bit lengths). Thus the perturbed polynomial also omits both punctures throughout the closed disk of radius two. Its finitely many roots are strictly outside that disk, and F(P(z)), where F(w)=4 arctan(w-1)+pi is the origin branch, has analytic radius strictly greater than two. Composition integrality gives even derivative jets g_j=G^(j)(0) for all j.

## Actual endpoint cancellation

For the complete exponential-gauged endpoint, retain the previously proved definitions

    D_N = N! sum_(k=0)^N (-1)^k/k!,
    B_N = N! + sum_(j=0)^N binom(N,j) g_j D_(N-j),
    c_N = B_N/D_N,   q_N = |D_N|/gcd(D_N,B_N).

Fresh integer jet and convolution calculations give D_159=0 mod163. The perturbation changes g_159 by -62, changes B_159 by -62, and leaves all earlier g_j unchanged. It was chosen so that

    B_159 - 159! = 0 mod163.

There is an essential factorial distinction here: B_159 itself is a unit modulo163, because 159! is a unit. The common residue cell concerns the factorial-subtracted numerator; actual cancellation appears after the factorial vanishes. At N=159+163=322, the all-index carry identity gives D_322=B_322=0 mod163. The receipt independently recomputes the original full convolution through N=322 and verifies that its actual gcd is divisible by163. Thus the reduced endpoint denominator loses this prime factor.

The script and JSON receipt freeze the baseline dependency hash, the integer K=-31, exact analytic bound, good-prime support, complete D_322/B_322/gcd/q and the factorial distinction. They are new computations, not another review of the baseline Schur certificate.

## Meaning and boundary

A certified analytic radius greater than two is compatible with a good-prime common residue cell and an actual denominator cancellation. In particular, the earlier finite list of nonzero good-prime residues for the degree-61 example cannot be generalized to all endpoint-fixed integral-Hurwitz pullbacks. This result establishes neither a common p-adic zero nor cancellation to arbitrary prime-power depth. It also supplies no favorable global growth bound for q_N and no irrationality criterion. Those remain new research targets.
