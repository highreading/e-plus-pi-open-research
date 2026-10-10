> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent check of the exact modal parity transform

Date: 2026-09-13. Reviewer: audit_results.

Reviewed Sections3–5 of raw_legendre_endpoint_sign_attempt.md and its
explicit n=2 counterexample. No additional degree was constructed or
tested.

The Rodrigues formula has the correct positive sign: l integrations
by parts cancel the factor(-1)^l in t^l(t-1)^l. Differentiating the
actual reflected polynomial contributes1/(n-j-l)!, and the beta
integral contributes (n-j)!l!/(n-j+l+1)!. This gives exactly



$$
p_{n,l}=(2l+1)\sum_{j=0}^{n-l}
B_{n,j}\frac{(n-j)!}{(n-j-l)!(n-j+l+1)!}.
$$



The generating-function representation uses the normalized
Beta(l+1,l+1) law. Its prefactor is



$$
\frac{2l+1}{l!}\frac{(l!)^2}{(2l+1)!}
=\frac{l!}{(2l)!}.
$$



Centering at1/2 gives



$$
\mathbb E[(t-1/2)^{2r}]
=4^{-r}\frac{(1/2)_r}{(l+3/2)_r}.
$$



Division by (2r)!=4^r r!(1/2)_r leaves the denominator
16^r r!(l+3/2)_r. Odd centered moments vanish. Consequently the
displayed positive parity transform is exact, including its factor
l!/(2l)!, its coefficient index n-l-2r, and its termination.

The positivity applies to the transform weights; it does not impose
signs on the centered coefficients of B exp(z/2).

The n=2 polynomial expands into the three displayed shifted Legendre
coefficients exactly. Its endpoint ratio simplifies to291/535, so
the full-sign-cone counterexample requires no floating-point step.

The bordered determinant ratios use the same actual B(1)=1
normalization as the integral-transfer and projected-moment notes.
Last-row linearity gives the endpoint sum identity. The equivalence
between kappa>=c and opposite signed mass at most(1-c)/(1+c) times
the aligned signed mass is algebraically correct.

No correction was found. No uniform noncancellation or sign estimate
is inferred from these identities or finite examples.
