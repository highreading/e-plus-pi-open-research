> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root review of the free model and zero-transfer obstruction

Date: 2026-09-13. Independent review of
`raw_free_chebyshev_model_and_zero_transfer_obstruction.md`.

**Outcome: PASS.** The specified free model, bounded zero theorem,
all-index comparison identities, and stated obstructions check.
The all-index mixed zero count remains unproved for both families.

I independently substituted the imaginary Chebyshev recurrence and
its coefficient formula into the Borel transform. This gives exactly
the model generating function, the even second-derivative recurrence,
and the odd derivative differences. The two choices of a,b for even
and odd n reproduce every prescribed high member and all the endpoint
coefficient constraints. The Laplace formula retains the factor 1/s
and the sign (−1)^m. The scalar fourth-order equation has the stated
3xD term; its forced constant self-adjoint weight is incompatible
with that term, even though its finite coupled pencil is symmetric.

For n=4 I checked the displayed T(1), the explicit positive derivative
bound, and the two nonsingular weighted Rolle operations. Their last
image is a constant multiple of the third Wronskian, giving at most
three zeros with multiplicity. At its simple zero, the derivative
evaluation matrix has rank two and the next derivative is nonzero.
The proposed small perturbation retains the central zero and creates
two nearby real zeros, proving the stated sharpness. I replayed the
exact symbolic certificate successfully, using the project's installed
math packages. The first attempt lacked that package path; this was
an environment issue, not a mathematical failure or changed proof.
No additional degree was computed.

The Legendre/free generating identity follows by the beta dilation
integral. Its index multiplier is sqrt(1−z²), so every nonconstant
coefficient has the negative sign stated in the note. Both it and
its inverse introduce lower rows; neither preserves the high block.
The two kernel configurations have opposite determinant signs exactly
as claimed. This refutes a general sign-regular-kernel transfer, not
a theorem restricted to the special polynomial family.

I checked the two normalized coefficient products directly against
the actual even and odd factorial recurrences. The fourth-moment
bound gives E[N]≤1+sqrt(2(m+1)x); integration over [x,cx], with
c=exp(1/(4m)), proves the uniform exp(1/sqrt m) comparisons. The
highest-derivative products have logarithm tending to (log 2)/2.
These are consistent statements in distinct norms. The pointwise
comparison cannot be promoted to a relative comparison of every
growing-order derivative. The proposed confluent evaluation criterion
retains this missing condition explicitly.

No numerical trend, assumed polynomial sign, or unproved all-block
Chebyshev property is used in any accepted statement.
