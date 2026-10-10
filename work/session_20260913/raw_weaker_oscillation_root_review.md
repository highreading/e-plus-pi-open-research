> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root audit of the weaker oscillation and same-parity theorem

Date: 2026-09-13. Verdict: PASS, after a citation-number clarification.

Reviewed `raw_weaker_oscillation_and_spectral_rank.md` in full and
independently checked the primary inputs and the closed exact n=4,5
certificates. No mathematical correction is required. The all-degree
mixed zero bound is still open.

## The singular-endpoint spectral bridge

The change u=2x−1 gives the stated order-zero prolate parameter c=1/2
and additive shift 3/4. I checked the simple-zero and parity statements
in Osipov's primary [Theorem 1](https://arxiv.org/pdf/1206.4056), printed
page 3. The project already fixes the analytic bounded branch and its
ordered differential eigenvalues. The Taylor argument for nonzero
endpoint values is correct, including its leading −m² coefficient.

The identity [p psi_0²(U/psi_0)']'=psi_0 U_1 has the correct sign.
The flux vanishes at both endpoints because p vanishes and the quotient
and its derivative are bounded. Rolle's theorem preserves at least the
number of distinct interior zeros through each iteration. The
normalized iterates converge in C¹ to the highest indexed eigenfunction;
its simple zeros and nonzero endpoints bound the number of zeros of
the late iterates, not merely that of their limiting function.

The proof is a valid adaptation of the regular-case argument in
Bérard–Helffer, [Section 2](https://arxiv.org/pdf/1807.03990), printed
pages 5–6. The note supplies the required singular endpoint check rather
than assuming the cited regular Dirichlet theorem applies unchanged.
The determinant interpolant through sign-change points then proves the
stated orthogonality implication; a continuous nonzero function has an
open set on which the one-sign product is nonzero.

## Same-parity total nonnegativity and Wronskians

The coefficient recurrence gives exactly the Newton factors and squared
factorial denominators in (4). I checked the positive bidiagonal
factorization in Khiar et al., [Theorem 2 and Corollary 2(a) of arXiv
v1](https://arxiv.org/pdf/2312.14483), printed pages 8–10. For ordered
interpolation nodes, its triangular Newton matrix has nonnegative
minors. The note had cited Corollary 1 without specifying version;
the arXiv citation was corrected to Corollary 2(a).

Selecting arbitrary increasing rows preserves minor signs. The first-r
column minor is strictly positive by the monic Newton-to-monomial
triangular change and the ordinary Vandermonde. The monomial derivative
determinant is exactly y^(sum j−r(r−1)/2) times the exponent
Vandermonde. Cauchy–Binet therefore makes every selected parity
Wronskian positive. Removing positive column constants, multiplying all
functions by x^sigma, and using y=x² multiply Wronskians by positive
factors. The resulting nonsingular initial Wronskians justify the
extended Chebyshev conclusion on (0,infinity), with multiplicities.

This does not assert total positivity of the mixed parity family or
of the two-seed spectral measure.

## The two exact finite cases

I re-ran the stored exact checker, restricted to the predeclared n=4,5.
All positive coefficient, Bernstein derivative, and disjoint rational
root-bracket assertions passed. I also checked the two Wronskian
quotient identities (7) symbolically at the general derivative level.
The n=4 transformed function has exactly one zero, so reversing the
two Rolle steps gives at most three zeros. For n=5 the transformed
ratio has exactly one pole and one distinct critical point, so its
three monotonic intervals give at most three intersections with a
horizontal line; a critical-point root is shared by its adjacent
intervals and does not add an extra intersection. Reversing the two
Rolle steps gives the claimed bound of five.

The all-index residual Wronskian problem has the correct count m+1
after r parity eliminations. The Descartes example indeed has nonzero
alternating coefficients in all degrees through 2n−1, so its variation
bound is too weak. Neither this example nor the two finite certificates
establishes the missing growing mixed zero bound. Full high rank for
all n, quantitative endpoint control and irrationality remain open.
