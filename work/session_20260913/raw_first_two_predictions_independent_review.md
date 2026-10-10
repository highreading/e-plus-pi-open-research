> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the first two negative-row prediction bounds

Date: 2026-09-13. Reviewer: audit_results.

Target: raw_first_two_negative_toeplitz_predictions.md by audit_computations.
Verdict: FULL PASS. No correction required.

The review covers the two finer distance identities as well as the exact prediction and derivative normalizations. It does not replace them by the separate all-r prediction estimate.

## 1. Exact prediction identity and complex-weight estimate

The joint equation with q=n!V(1)A^(-1)e_0 gives

    sum_j a_(2n-j)(1+t)v_j=t^n V(1+t)/(n!V(1)).

Expanding the coefficient polynomials in t yields at order l the row n-l of Av. For l<n that row is one of the zero high rows; l=n gives 1; l=n+r gives exactly b_r. Orders above 2n vanish because their coefficient indices are negative. This proves (2), with factor n!/(n+r)!, as a polynomial identity including t=0.

The Fourier convention is consistent: integration of conjugate(z^k)v against f gives row k of A, while conjugate(z^(-r)) gives b_r. Subtracting any polynomial in the span of z,...,z^n is therefore legitimate before applying Cauchy–Schwarz in the positive base weight. The argument retains the complex f and does not assert positive orthogonality for it.

From v*Re(A)v=v_0 and Re(A)>=e^(-1)cos(1)G0, together with the reviewed inverse-corner bound v_0<=e c_m/cos(1), one gets ||v||_w<=e sqrt(c_m)/cos(1). The extra factor e from |f|<=e w gives exactly C=e^2/cos(1) in (4).

## 2. First omitted-power distance

Parity orthogonality removes all positive even powers when predicting z^(-1). Multiplication by z maps the problem to prediction of 1 from u,...,u^m with u=z^2, preserving the normalized circle norm. Thus the Schur-complement distance is det(T_(m+1))/det(T_m)=eta_m=1/c_m.

No coordinate was added to the prediction span. The Fourier orientation is immaterial for these real symmetric base Gram matrices but is consistent with the preceding convention.

## 3. Second distance and the exact inverse entries

For r=2, parity selects z^2,...,z^(2m). Multiplication by z^2 gives prediction of 1 from u^2,...,u^(m+1). It excludes u, so the squared distance is entry (0,0) of the leading two-coordinate Schur complement of T_(m+2), not a one-coordinate determinant ratio.

I checked the three required inverse ratios for R=T_(K+1)^(-1):

    R_00=1/eta_K,
    R_01/R_00=-Km/(m+K),
    R_(0,K)/R_00=(-1)^K m/(m+K).

For the last ratio, the shifted cofactor determinant has binomial parameters m-1,m+1, both nonnegative since m>=1, and its product formula telescopes to m/(m+K). For the first off-diagonal ratio, after factoring the stated row factorials the determinant is a fixed coefficient determinant times a Vandermonde. Replacing the node 1 by 0 changes that Vandermonde by K and the row factor by m/(m+K). The cofactor sign is negative. Falling factorials provide the out-of-range binomial zeros, so no negative factorial is used.

The leading and trailing principal blocks both equal T_K. Deleting the last coordinate gives their common inverse entry as R_00-R_(0,K)^2/R_00; deleting the first gives R_11-R_01^2/R_00. This proves (7) using persymmetry, with no missing corner term.

Inverting the leading two-by-two block gives

    d_2^2=eta_K(1+alpha^2-beta^2)/(1-beta^2).

The identity eta_K/eta_(K-1)=1-m^2/(m+K)^2 cancels the denominator. At K=m+1, multiplication by c_m=1/eta_m yields precisely

    c_m d_2^2=1+m^3(m+2)/(2m+1)^2.

Every inverse here belongs to a positive definite base Gram matrix; none depends on an unproved HP minor.

## 4. Derivatives, reciprocal roots and scope

The elementary bound on the square root in (9) is valid for m>=1. The derivative formula contributes a factor 2 to V''(1)/V(1), which cancels the factor 1/2 in the b_2 bound. This gives exactly C(m+2)/[(n+1)(n+2)], and hence the stated weaker C/(n+1).

The reciprocal-root identities are the logarithmic derivative and its derivative. Thus the second complex power sum is (V'/V)^2-V''/V, giving O(1/n). These are signed complex sums; the note correctly does not turn them into sums of absolute values or individual root-distance bounds.

The frozen n=2 data give V'(1)=34 and V''(1)=98. Thus b_1=3*34/925=102/925 and b_2=(3*4/2)*98/925=588/925. The base distances at m=1 are 3/2 and 2, respectively, as the stated projection problems require. No new degree or root was examined.

The exact first and second prediction bounds pass in full. The note's restriction to even degrees and its distinction from all-r analytic control remain appropriate.

