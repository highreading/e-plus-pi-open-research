> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root mathematical review of the odd limiting certificate

Date: 2026-09-13. Reviewer: root. PASS.
The separate full implementation/rerun audit is
raw_odd_limiting_certificate_independent_review.md by audit_sources.

I independently checked the analytic argument in
raw_odd_limiting_determinant_interval_certificate.md and its connection
to the reviewed operator-limit theorem.

On R=4/3, the imaginary-part bound for y is 7sqrt(3)/24<17/33, so
|t|<25/8. With q=9/5, both maximum row and column sums of the entire
matrix series are <=cosh(q)+q sinh(q)<=q exp(q)<16. This bounds the
operator norm and every Laurent coefficient. The alias estimate includes
both signs of the Fourier index and remains valid through k=128.

The 24-term exponential-series enclosures and the exact dyadic vectors
are appropriate finite witnesses. Their numerical discovery does not
enter the proof. The infinite convolution tail begins at r=127 for the
output tail beginning at r=128, because A0 has bandwidth one. The
geometric exponent 128-L in the norm bound is correct. The true v tail
has norm 3^(-64). The full residual bound multiplied by the proved norm
bound ||Q||<12 certifies each solution without trusting a finite inverse.

The boundary test norm is less than three, and testing against the
geometric endpoint vector has norm one. The resulting componentwise
rectangles are valid enclosures for the determinant formulas. The phase
gauge i^r makes the matrices and vectors real: F_k is real for even k
and imaginary for odd k, while the extra boundary phase is removed by
Jb. Thus the real rational intervals state meaningful signed bounds.

The matrix limits were proved before any determinant inversion. Their
certified nonzero values therefore imply s_m tends to a nonzero negative
constant. Woodbury gives a uniform full inverse for sufficiently large
m; the compression formula divides by 1/s_m, which also has a nonzero
limit. Earlier exact finite nonvanishing covers the finite prefix. No
effective first degree is needed for the stated existence of a bound,
and none has been claimed.

The factorial ratio gives the all-degree absolute root-product limit
3sqrt(3)/e. This is an intermediate theorem about the actual dual
construction. It does not supply the signed arctangent error, the
endpoint gcd, or a shrinking primitive form.
