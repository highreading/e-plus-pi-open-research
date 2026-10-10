> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent root review of the improved extremal-content height

Date: 2026-09-13. Review of `raw_extremal_large_prime_height_improvement.md`.

**Outcome: PASS.** The all-index height improvement, including every
large-prime valuation, is proved. The two infinite denominator obstructions
are also proved. This review does not assert an O(n²) height estimate.

## Exact arithmetic reduction

I reread the finite-difference elimination at its source. The row operation
is unit triangular, with the original first n rows retained; its polynomial
column block has determinant product(j!, j=0,...,n−1). At p>3n this block
is invertible, so the remaining n maximal Smith valuations are exactly
those of the (n+1)-by-n matrix G. Multiplication of its row r by
L_(3n)/(n+r)! is a p-adic unit. Thus equation (3) is an equality of
determinantal valuations at arbitrary depth, not just a rank equivalence.

Every arctangent index n+r+s−j lies between 1 and 3n. Its denominator
divides L_(3n), while the factorial ratio in equation (2) is an integer.
Consequently the normalized matrix Z is integral. Full rational rank
supplies at least one nonzero n-minor. Its large-prime part is divisible
by F_(n,>3n), so an upper bound for that actual integer minor suffices.

## Archimedean bound and constants

For t_s=binom(n,s)(n+r+s)!/(n+r)!, the ratio

    t_(s−1)/t_s = s/[(n−s+1)(n+r+s)]

is at most n/(2n+r) and hence at most 1/2. This can also be seen directly:
s/(n+r+s) increases with s, and 1/(n−s+1) increases with s. The finite
geometric estimate gives sum(t_s)≤2t_n. Hadamard applied to each row of
any selected minor gives precisely equation (5). Each factorial ratio
has n factors bounded by 3n, so their n-fold product is at most
(3n)^(n²).

The stated lcm recursion is valid. If a prime's largest power below N
exceeds ceil(N/2), only that last power can be missing from the smaller
lcm. The binomial coefficient supplies it, by its factorial valuation;
every other prime exponent is already present. Summing the successive
ceilings bounds their total by 2N+ceil(log₂N). Thus
L_(3n)≤6n·64^n, and substitution gives

    F_(n,>3n)≤(12n^(3/2))^n (192n)^(n²).

Its logarithm is n² log n+O(n²). All constants are independent of n.
The known large-prime divisibility of the unbordered high content into
F_n transfers this bound, but it gives no bound for the distinct
endpoint scalar Z_n.

## Infinite obstructions to the next entrywise normalization

For odd n, the first entry of G contains only even s. Factoring (n−1)!
leaves exactly equation (9), whose nonconstant terms all contain n.
Its residual integer b_n is therefore prime to every divisor of n.
This proves the exact denominator valuation of G_00/(n!)² at p|n.
For n equal to powers of any fixed product of odd primes, Legendre's
formula gives the displayed lower limit sum(log p/(p−1)). These sums
are unbounded. Multiplication by L_(3n) subtracts only O(log n) at each
fixed prime and cannot alter that limit. The resulting obstruction is
to a uniform exponential clearer for the actual entries; it does not
control cancellation among terms in a determinant.

The last-column prime-power test was suggested by root and independently
verified by audit_sources. I checked it again in the exact convention
tau_(s+1). For n=p^a, p>3 and a≥2, every nonzero summand except s=0
has valuation a+v_p((s−1)!)-v_p(s+1)≥1. At s=n−1 the factorial contains
p; at s=n the parity coefficient vanishes. Thus G_(0,n−1)/n! is a
p-unit and v_p Z_(0,n−1)=a<v_p(n!). This is an infinite actual-family
counterexample to the proposed extra n! row divisor.

No numerical estimate or finite extrapolation is needed for any reviewed
claim. The possible determinant-level small-prime divisor in the final
section remains a sufficient target, not an established fact.
