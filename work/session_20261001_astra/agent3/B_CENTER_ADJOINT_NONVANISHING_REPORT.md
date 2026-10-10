> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# B-Gram adjoint nonvanishing report

Original author research, not independently audited. No numerical scan, old-check replay, scalar nonstabilization work, or denominator transfer.

The actual factorially weighted B-only adjoint is represented as lambda=ell/V with V>0 and

    ell=adj(T)^T Krec^T W Krec adj(T)fP.

Both inverse factors and all reconstruction weights remain present. For P(z)=sum ell_i z^i, the note gives an explicit invertible coefficient transformation such that

    Re P(1-exp(i theta)/sqrt(2))=C(1-cos theta).

Here C_0=P(z*) and C_1=P'(z*)/sqrt(2)-P''(z*)/2. Every coefficient of C is an explicitly specified algebraic contraction of the actual adjoint.

The logarithmic arc becomes an exact finite sum sum C_j mu_j with positive moments. The note proves explicit bounds L_j<=mu_j<=U_j, both on the n^(-j) scale, uniformly for all degrees under consideration. This yields a local derivative-based dominance gate and a more general signed-coefficient gate that can work even when P(z*) vanishes.

The endpoint constant and the entire exponential error are retained in the explicit budget Bhat_n. For either sign sigma, the sufficient condition is

    sum_(sigma C_j>0)|C_j|L_j
       -sum_(sigma C_j<0)|C_j|U_j > Bhat_n,

with L_0=U_0=1. It proves a quantitative nonzero complete error of sign -sigma on even indices. A common coefficient sign is another concrete algebraic target, with a separate magnitude condition against Bhat_n.

These transformations, moment estimates, and conditional lower bounds are proved author deductions using the retained arbitrary-polynomial arc formula. Satisfaction of the gates for the actual adjoint on an unbounded set remains unproved. No entrywise or evaluation positivity is inferred from the even-index Toeplitz quadratic form.

Domain: even n>=2^96, b=floor(log n), m=floor((b-1)/2), within the retained provisional contact-normality range. SCALAR_CENTER_CONTIGUOUS and its recurrence are preserved.

The main note and this report must be read back after saving before operational completion is reported.
