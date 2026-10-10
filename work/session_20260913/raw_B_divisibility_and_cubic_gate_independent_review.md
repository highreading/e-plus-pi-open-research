> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: all-coefficient B divisibility and the cubic gates

Date: 2026-09-13. Reviewer: audit_sources.

**Result: pass.** The all-index theorem in
`raw_B_coefficient_dyadic_divisibility.md` is justified by its stated,
previously reviewed C-block and endpoint-determinant inputs. Its use in
`raw_cubic_dyadic_squarefreeness_attempt.md` correctly removes two of the
four proposed coefficient conditions. Neither note proves either of
the remaining two P-coefficient conditions or full squarefreeness.

## 1. Coordinate normalization and both Laplace assignments

I checked the argument against the actual appended-coordinate convention
in `raw_leading_B_dyadic_partial.md`, rather than identifying that row
with an endpoint row. If Delta_(B,j) appends the row extracting B_(n,j)
to J_n and Delta_B appends B(1), cofactor reconstruction is exactly

    B_(n,j) = Delta_(B,j)/Delta_B.

There is no j!, n!, or leading-coefficient normalization in this
identity. Dividing every high row k by k! contributes the same factor
to both determinants.

With the endpoint border in the C block, the n exponential columns
are all degrees 0,...,n except j. Their determinant is

    (product_(d != j) d!)/(product_(k in I) k!)
        times det[binom(k,d)].

The last determinant is integral; no nonvanishing or uniqueness of
a lowest term is needed. The factorial numerator has valuation
S(n)+phi(n)-phi(j), and the largest possible denominator valuation
is H_n. The complementary bordered C determinant has the reviewed
lower bound L_n. Thus the lower bound on every such term is
V_n+phi(n)-phi(j).

With the endpoint border in the exponential block, expanding its
entry -4 on any column ell != j leaves n-1 exponential rows. The
valuation is at least

    2+S(n)+phi(n)-phi(j)-phi(ell)-H_(n-1)
    >= 2+S(n)-phi(j)-H_(n-1).

Here H_(n-1) denotes the largest n-1 row-factorial valuations in the
same high range n+1,...,3n; it is not H_n with its index replaced
everywhere by n-1. The remaining pure C determinant has n+1 rows
and lower bound 2S(n+1). The gap over the first assignment is

    2+H_n-H_(n-1)+2S(n+1)-L_n-phi(n)
      = 2+n+2phi(n)-c_n > 0.

This uses phi(2n+1)=n+phi(n), including n=1 with H_0=0.
The dimension-zero exponential minor at n=1 has determinant 1 and
causes no exception. The terminology “size-n bordered C block” in
the inputs refers to its n-row difference-minor parameter; the
bordered matrix itself has n+1 rows and columns, as used in the proof.

Restoring the high-row factors and dividing by the exact valuation
of Delta_B proves, for all n>=1 and 0<=j<=n,

    v_2(B_(n,j)) >= phi(n)-phi(j).

Zero minors and cancellations only increase this lower bound.

## 2. Reduction modulo 2 and the exceptional odd class

Every coefficient of the actual canonical B polynomial is now in
Z_(2), so reduction modulo 2 is well defined. For even n, all
coefficients below the leading one are even. For odd n>=3, all
coefficients below degree n-1 are even because
phi(n)=phi(n-1)>phi(n-2).

The previously independently reviewed leading-B valuation, together
with B(1)=1, then gives

    B_n(z) = z^(n-1) mod 2  if n=1 mod 4;
    B_n(z) = z^n mod 2      otherwise.

For n=1 mod 4 with n>=5 the leading coefficient has valuation
v_2(n-1)>=2, so the penultimate coefficient must be a unit. The
base case B_1=-7+8z gives the same reduction. This conclusion is
not an assertion about an arbitrary primitive integer scaling or
a monic scaling of B.

As a finite normalization check only, I reused the saved exact
n=2,4,8,16 inputs in `raw_accessory_scaling_probe.json`. Those
triples are stored in a common integer scale and do not have
B(1)=1. Dividing all three polynomials by that B endpoint verifies
C(1)=4, every coefficient lower bound, and the displayed monomial
reductions. No new canonical degree was solved. The cubic checker
does not need this division: its ratios are invariant under a common
triple scale.

## 3. Exact accessory identities and their scope

I independently expanded the Wronskian by the exponential column.
With K=H'C-HC'=P/(1+z^2), the identity is

    exp(-z) W(H,B exp(z),C)
      = (B+2B'+B'')K-(B+B')K'-B(H'C''-H''C').

The leading two coefficients of the last parenthesis are
-n(n-1)kappa_0 and -n(n-2)kappa_1. Collecting the four highest
Laurent degrees after multiplication by (1+z^2)^2 gives all four
formulas (7) in `raw_cubic_dyadic_squarefreeness_attempt.md`.
I also checked their cancellation of the n-dependent multipliers
symbolically with n formal, independently of the saved finite
controls. The Hessian expansion (11) is correct.

All common rational scalings are retained: P and each kappa scale
quadratically in the triple, and Q and its coefficients scale
cubically. The ratios in the proposed gates therefore do not
depend on that common scale. At small n the formal Laurent
coefficients h_j can be nonzero beyond the polynomial degree; using
P and kappa_2=p_2-p_0 avoids incorrectly deleting them.

For every even n, the new theorem and the proved unit b_0 give

    b_1/b_0 in 2 Z_(2),   b_2/b_0 in 2 Z_(2).

Consequently the still-unproved conditions

    kappa_1/kappa_0 in 2 Z_(2),
    kappa_2/kappa_0 in Z_(2)^times

would make q_2/q_3 even and q_1/q_3 odd. The Hessian divided by
q_3^2 would then be odd, excluding a triple root. Since
kappa_0=p_0, kappa_1=p_1 and kappa_2=p_2-p_0, these conditions
are exactly

    v_2(p_1)>v_2(p_0),  v_2(p_2)>v_2(p_0).

In particular the second strict inequality, rather than merely a
triangle lower bound on separate cross-products, is essential.
The all-index nonvanishing of b_0 and p_0 does not prove either
strict inequality. The present B theorem supplies only evenness,
not the stronger divisibility by 4 suggested by some saved cases.

## 4. Discriminant checks and retained limitations

The discriminant identity and the grouped first two terms in
equations (12)-(13) are correct. Under the explicitly stated
extra assumptions in (14), with a>=3, the term 18BCD_0 is uniquely
least and gives valuation a+2. The case a=2 cannot be included by
that argument. The n=4 tie and n=8 cancellation are correctly
retained as finite exact observations.

For the n=1 comparison, “the primitive cubic divided by 4” refers
to the cubic obtained from the primitive integral triple, followed
by its stated scalar division. This does not mean that a
content-primitive polynomial is divisible by 4. Its displayed
coefficients give the claimed three distinct Newton slopes.

The weaker Hessian gate excludes only a triple root. It does not
exclude a double root, prove a nonzero discriminant, bound
Archimedean root separation, or control the primitive endpoint
denominator. The notes preserve these distinctions. The two
P-coefficient gates remain the exact next arithmetic problem at
the time of this review.
