> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the odd Toeplitz deformation and Schur coefficients

Date: 2026-09-13. Reviewer: audit_results.

Target: raw_odd_toeplitz_deformation_and_schur_coefficients.md.
Verdict: FULL PASS. No mathematical correction required.

This audit checks the all-order signed formula, not merely the two displayed low-order coefficients. It also checks the inverse-corner normalization and the complex uniform disk argument. The resulting scalar estimate is local near zero and is not promoted to the actual point x=1.

## 1. Rectangular specialization and differentiated columns

For lambda=((n+1)^n), the conjugate partition has n+1 parts all equal to n. The dual Jacobi--Trudi matrix is (e_(n-i+j)) of size n+1, exactly the transpose of the displayed Toeplitz matrix. This proves the rectangular shape and its orientation. The specialization of elementary generating functions is correctly e^(xt)(1+t^2)^n; the paired alphabet is n copies each of i and -i.

The exponential specialization gives the skew coefficient f^(lambda/mu) x^r/r!. Its size r is n(n+1)-|mu|, so no factorial or rectangle conjugation is missing in (2). This identity is finite; it does not use a positivity assertion about the imaginary alphabet.

The direct column proof of (7) is also correct. Differentiation increases a selected column index by one. If it becomes equal to the next selected index the determinant vanishes; otherwise the ordered indices remain ordered. The legal histories correspond to standard tableaux of the partition defined by kappa_j=j+lambda_(2L-j), with coefficient f^lambda. This independently fixes the tableau orientation.

## 2. General binomial column minors

After removing the column factor in Section 2, the row-i expression is

    (a+L-1-kappa) falling_(L-1-i)
    times (b+kappa) falling_i.

It is a polynomial in kappa of degree at most L-1. Its determinant is its fixed coefficient determinant times the Vandermonde in the ordered nodes. Comparison with the original columns proves (3), including its sign.

The support convention is legitimate: if the largest chosen column exceeds a+L-1, every binomial in that column vanishes. The box-product formula (4) also contains the zero factor. Within support, any individual row entry outside its binomial range is handled by its falling-factorial zero, rather than by an invalid negative factorial.

The three ratios in (5) follow directly. Partitions longer than L must indeed be omitted. This matters at m=0 in the fourth derivative.

## 3. Parity, signs, and the second and fourth derivatives

For odd n, even rows couple only to odd selected columns at x=0, and odd rows couple only to even selected columns. The two blocks have parameters (m,m+1) and (m+1,m) in precisely the order stated. Their determinants agree by transposition. The relative block permutation gives D_n(0)=(-1)^L Delta_L(m,m+1)^2.

A balanced selected set has L columns of each parity. Its increasing even and odd half-indices are at least 0,1,...,L-1, and therefore define genuine nonnegative partitions. Their total excess is r/2. The column regrouping sign in (8) retains all cross-parity inversions.

I independently checked the five size-four assignments:

    (4): B_(2);
    (3,1): -C_(2);
    (2,2): B_(1)C_(1);
    (2,1,1): -B_(1,1);
    (1,1,1,1): C_(1,1).

Their tableau multiplicities are respectively 1,3,2,3,1. Substituting the exact ratios gives

    D''(0)/D(0)=-(3m+2)/(2(2m+1)),

    D^(4)(0)/D(0)
       =(m+3)(3m+2)/(4(2m+1)(2m+3)),  m>=1.

A separate symbolic simplification, with m left symbolic, confirms these rational identities and the displayed fourth logarithmic derivative. No canonical degree was constructed.

The m=0 restriction is correct: its deformation has degree two and the forbidden partitions cannot be retained by formal substitution in the m>=1 formula. The Gaussian comparison is an appropriate obstruction to that specific proposed limiting shape, not a claim of convergence to another shape.

## 4. Inverse-corner coefficient and metric normalization

At x=0 the corner minor has unequal parity counts. Differentiating any column except the last produces a repeated column, so only the last derivative survives. After parity regrouping its block sizes are m+1 and m, with total sign (-1)^m. Dividing by D_n(0) leaves the negative ratio of the size-m and size-(m+1) binomial determinants. Their product formula telescopes to

    C_n'(0)/D_n(0)
       =-(2m+1)!(2m)!/[m!(3m+1)!].

For m=0, the size-zero determinant is understood as 1; this is the ordinary empty-determinant convention and gives C_1'(0)=1 directly.

The conversion to g_m is exact. For the previously specified unit vector v,

    v* Atilde_n(x)^(-1) v
       =(A_n(x)^(-1))_(0,0)/c_m=g_m(x).

Thus division by c_m gives slope -(3m+2)/(2m+1), and the actual scalar at x=1 is exactly 1/g_m(1). The deformation symmetry makes g_m odd. It is not legitimate to replace the corner by the full determinant: the former vanishes at zero while the latter does not, as the note explicitly states.

## 5. Uniform complex disk and local scalar estimate

At x=0, the normalized matrix is Hermitian. The two orthogonal subspaces P_+,P_- give diagonal blocks exactly +I/2,-I/2. Squaring that block matrix cancels its off-diagonal blocks, so the inverse norm is at most 2. This argument supplies an actual inverse estimate because this undeformed matrix is Hermitian; it does not repeat the invalid implication from a general indefinite Hermitian part.

The complex perturbation bound follows from |e^(xz)-1|<=e^|x|-1 and the previously proved positive-weight comparison. Neumann inversion gives precisely (13)-(14), with radius log(1+1/sqrt(5)).

At R=1/4, the stated elementary bounds give inverse norm less than 28/5, hence certainly less than 6. The unit-vector representation of g_m therefore gives its uniform modulus bound on the complete complex circle, as required by Cauchy's estimate.

Oddness leaves only degrees 3,5,... in the remainder after the linear term. At |x|<=1/32 the displayed geometric series divided by |x| is at most 8/21. Together with 3/2<=|g_m'(0)|<=2 this yields

    |x|<=|g_m(x)|<=(5/2)|x|

throughout the complex punctured disk, not only for real x. It follows that the actual high compression is invertible there and that the reciprocal scalar satisfies (16).

## 6. Scope and result

All formulas pass, including the factorial normalizations, parity signs, small-m conventions, uniform complex constants, and the distinction between full determinant and high compression.

The proved local disk has fixed radius less than one. Neither the signed coefficient formula nor its first four derivatives extends the scalar estimate to x=1. The remaining actual-point target log|s_m(1)|=o(m) remains open.

Only symbolic rational-function simplification and the already stated low-degree conventions were used in this audit. No degree, prime, root, or singular-value scan was performed.
