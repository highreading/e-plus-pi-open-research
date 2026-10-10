> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent root review of the finite-difference Smith reduction

Date: 2026-09-13. Reviewed `raw_high_smith_finite_difference_reduction.md`.

Verdict: the exact reductions and entry recurrences pass. No assertion
of large-prime full rank or of a bound on the content is established.

The row transformation in (1) is lower triangular with diagonal one:
its new row at position m+r has its last nonzero coefficient, equal
to one, in the old row at that position. Thus retaining the first m
rows does not compromise integral invertibility. The first m columns
are polynomials of degrees 0 through m-1, so the lower block vanishes.
The upper block determinant is the consecutive Vandermonde
product of j! for 0<=j<m, independently of the starting index a.
It is a unit at every stated prime. Eliminating the upper-right
block and reducing this upper-left block to I gives a genuine
equivalence over Z_p, including prime-power determinantal ideals.

For H_n the row range, factorial factors, and tau indices in (4)
agree with the actual high equations. Every k-j is positive and
k!/(k-j) is integral. The last original row is 3n. There are n-1
remaining rows and n+1 arctangent columns. The empty n=1 case and
the nonzero maximal-minor gcd for n>=2 are handled correctly.

For the extremal system m=d+1, the original 2m+1 rows are
k=m,...,3m. There are m+1 remaining rows after eliminating the
m exponential columns. The row k=m, which enforces the degree
bound on A, has been retained. The operator in (8) expands to
exactly the finite sum: D^r D^m(D-1)^m uses derivatives of order
r+m+s with the binomial signs in (7). It annihilates both A and
B exp(z), and its residual arctangent coefficient vanishes for
deg C<m. This remains a finite derivative identity at the allowed
primes and does not require factorials at or above p.

For (10), the exact discrete product rule is
Delta^m(k f(k-1))=k Delta^m f(k-1)+m Delta^(m-1)f(k).
Together with the stated column shift this proves the recurrence.
For (12), applying Delta^(m+2) to y_(k+2)+k(k+1)y_k=0
gives, in terms of f=Delta^m y,

    S^2 Delta^2 f + k(k+1)Delta^2 f
      +2(m+2)(k+1)S Delta f +(m+2)(m+1)S^2 f=0.

Expanding Delta=S-1 produces every coefficient in (12), including
the coefficient (k+m+2)(k+m+3)+1 of f_(k+2).

The note correctly distinguishes unbordered content from the
additional endpoint restriction content. It also correctly avoids
reversing the implication from a row-rank loss to an extremal
lower-degree triple. Entry recurrences alone supply no recurrence
for a gcd of growing maximal minors. The final open target is
therefore retained without weakening or resolving it.
