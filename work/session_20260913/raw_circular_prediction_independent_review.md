> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of circular binomial prediction bounds

Date: 2026-09-13. Reviewer: audit_computations.
Target: `raw_circular_binomial_prediction_bounds.md` by audit_sources.

**Verdict: PASS.** The all-gap residual construction and its uniform
factorially weighted norm bound are rigorous. Both parity spaces,
out-of-support moments, and growing gap constants are handled correctly.
No correction is needed. The target does not silently apply positive
orthogonality to the complex perturbed Toeplitz matrix.

## 1. Exact parity and distance normalization

The original weight is pi-periodic, so the two Laurent parity spaces
are orthogonal. For r=2s, the only useful predictors are z^2,...,z^(2m).
After w=-z^2 and multiplication by the unit monomial w^s, this is
exactly distance of 1 to w^(s+1),...,w^(s+m). For r=2s+1, multiplying
the target and odd predictors by z first gives the same reduction.
All constant phases can be absorbed in predictor coefficients. There
are precisely m predictors in both cases; no missing constant term
has been added. Thus D_(m,2s)=D_(m,2s+1) is exact.

The base value is a SQUARED distance H_m=1/c_m, not sqrt(H_m).
It agrees with the previously established positive Toeplitz inverse
corner and with the independent exact r=1 calculation in
`raw_first_two_negative_toeplitz_predictions.md`.

## 2. Explicit orthogonality without an external theorem

I independently expanded the product of a coefficient of Phi_k and
the moment mu_(j-ell). For 0<=ell<k it equals

    (-1)^(-ell)(2m)!/[(m-1)!(m+k)!]
      *(-1)^j binom(k,j)
      *(m+k-j-1)_(falling,k-ell-1)
      *(m+j)_(falling,ell).

This is exactly the target's constant and two factorial lengths.
Their total polynomial degree in j is at most k-1, so their kth
alternating finite difference vanishes. If a moment factorial is
outside its nonnegative range, the relevant falling factorial has
a zero factor. Its starting integer remains nonnegative, so the
polynomial formula continues to represent zero correctly. This
proves all k, including k>m, rather than only a no-zero-factor range.

The norm h_k follows from the exact binomial Toeplitz determinant
ratio. Alternating moment signs are a diagonal congruence, so they
do not affect the determinant. Reversing coefficients gives the
stated Phi_k* formula and constant coefficient one. The supplied
recurrence is consistent but is not needed as an orthogonality
assumption.

## 3. Strict roots and the exact base residual

Positive definiteness holds because the circle weight is positive
apart from one point. Orthogonality therefore gives the unique
minimum-norm monic polynomial. Replacing an exterior root a by
1/conjugate(a) would decrease its norm by the factor 1/|a|, so
exterior roots are impossible. For a boundary root, orthogonality
to the quotient gives a as the weighted average of the circle
coordinate. That average has modulus strictly less than one because
the positive measure is not supported at one phase. Boundary roots
are impossible as well.

For F=Phi_m*, reversal sends orthogonality against degrees 0,...,m-1
to orthogonality against w,...,w^m. Since 1-F belongs to that span,
F is the exact prediction residual, with squared norm h_m=H_m.
The factorization F=product(1-conjugate(a_j)w) and the strict disk
root property are therefore justified for the actual positive base
weight, not inferred from a coefficient pattern.

## 4. Every growing gap and summation

For the reciprocal series 1/F, the degree-s truncation B_s satisfies
F B_s=1+O(w^(s+1)) and degree at most m+s. Consequently
1-F B_s is an allowed predictor at gap s. This does not require
F B_s to be the minimizing residual.

Each reciprocal coefficient is a sum of exactly binom(m+j-1,j)
products of disk-root conjugates. Thus its absolute value is at
most that number, and ||B_s||_infinity<=binom(m+s,s). Multiplication
inside the positive norm proves the squared-distance bound for
every s>=0. For s<=m, each numerator factor in binom(m+s,s) is
at most n=2m, proving the further uniform factorial estimate.

The optional finite Schur-complement formula is consistent with
the signed moments. When s>=m all its off-diagonal moment entries
vanish, so the distance is the full norm binom(2m,m); this agrees
with the residual upper bound and causes no boundary exception.

Taking a square root BEFORE multiplying by n!/(n+r)! gives exactly

    n!/(n+r)! sqrt(D_(m,r)/H_m)
       <=n^(-ceil(r/2))/(floor(r/2)!).

Summing even and odd terms separately yields

    sum_(r=0)^n n!/(n+r)! sqrt(D_(m,r)/H_m)|x|^r
       <=(1+|x|/n)exp(|x|^2/n).

The squared-distance version has (s!)^2 instead and also checks.
All extensions to infinite positive series are upper bounds, so
there is no interchange involving signs or a growing-parameter
limit. The ranges r<=n+1 and s<=m agree exactly.

## 5. Interface and limits

The separate complex-weight Cauchy--Schwarz argument in the first-two
prediction note proves |b_r|<=C sqrt(D_(m,r)/H_m), with
C=e^2/cos(1), for the actual negative Toeplitz row. Thus the present
positive-base estimate has a verified route to actual coefficients;
one must still use their exact factorial expansion and normalization.

The target itself correctly confines its assertions to positive
base distances. It proves no sign for the perturbed coefficients,
no primitive-denominator estimate, and no arctangent-error bound.
No numerical controls or new canonical degree solves were needed
for this audit; the elementary all-index argument was checked directly.
