> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of odd dual flatness and the exponential error

Date: 2026-09-13. Reviewer: audit_computations.
Status: PASS on all substantive mathematics. Two editorial normalization
clarifications were sent to the author; neither changes an estimate.

Target: raw_odd_dual_flatness_and_exponential_error.md, all sections.
I also checked its normalization against raw_odd_dual_toeplitz_scalar_obstruction.md,
raw_odd_boundary_operator_limit.md, and the separately completed full
review raw_odd_limiting_certificate_independent_review.md. The fixed
operator interval certificate is an independently proved input here,
not an inference from a finite canonical-degree sample. I did not rerun
or extend a numerical degree, root, or prime scan.

## 1. Uniform inverse and the finite prefix

The passed operator limit supplies a uniform inverse bound for T_m and
uniform bounds for both exterior factors in the rank-two formula.
The certified nonzero limit of det D2_m bounds D2_m^(-1) eventually.
Woodbury then bounds the actual normalized Atilde_m^(-1) eventually.
The independent all-index added-column theorem gives invertibility
at each remaining finite m, so taking the maximum over the finite
prefix proves a finite K_A. This is a valid existence proof of a
uniform constant. It does not give an effective transition index,
and the target correctly does not claim one.

The displayed high-compression inverse identity is the standard
block-inverse rearrangement for the distinguished unit vector.
Its denominator v*Atilde^(-1)v=1/s_m tends to the nonzero number
1/s_infty. Together with the separately proved all-index invertibility
of the compression, this also bounds its full inverse family. This
stronger consequence is not needed for the coefficient proof.

## 2. Positive metric and actual coefficient normalization

For n=2m+1 the positive comparison metric is the Gram matrix of
|1+z^2|^(2m+2), with BOTH parity blocks of dimension m+1.
The exact inverse corner is

    c_m=((2m+1)!)^2/[m!(3m+2)!].

The identity G^(1/2)u=Atilde_m^(-1)G^(-1/2)e_0 therefore gives
||u||_(w_+)<=K_A sqrt(c_m). No positivity of the original odd
matrix is used or needed. The actual moment equation and its
factorial reconstruction agree with the earlier joint note:

    b_r=integral f u z^r,
    V(1+t)/V(1)=sum_(r=0)^n n!b_r t^r/(n+r)!,
    b_0=1.

The nonzero V(1) needed here follows from the passed added-column
theorem, rather than from the eventual sign of s_m.

## 3. Both prediction parities and their normalizing ratios

The lower positive weight is w_-=|1+z^2|^(2m). For r=2s, the
even predictor contains m powers. For r=2s+1, the odd predictor
contains m+1 powers. After factoring out a unit-modulus monomial
and setting w=-z^2, these are the stated gaps after w^s. This
unequal dimension is essential and is retained correctly.

The previously proved reversed-polynomial residual applies with
degree M=m and M=m+1, respectively, under the same parameter-m
weight |1-w|^(2m). Its squared norm is

    h_M^(m)=M!(2m+M)!/((m+M)!)^2.

Multiplying by c_m and canceling factorials gives exactly

    c_m h_m^(m)=(2m+1)^2/[(3m+1)(3m+2)],
    c_m h_(m+1)^(m)=(m+1)/(3m+2).

Both are at most one. If 1<=r<=2m+1, every factor in the
relevant binomial numerator is at most n: for even r one has
m+s<=2m, and for odd r one has m+1+s<=2m+1. This proves
sqrt(c_m D_(m,r))<=n^floor(r/2)/(floor(r/2))!.

For m=0 the lower weight is Haar measure and the reversed
polynomial is one. The dimension-zero even predictor and the
dimension-one odd predictor are correctly covered separately.
No formula requiring a positive rising-factorial parameter is
silently applied at zero.

Pointwise |f|<=e sqrt(w_+w_-). Subtracting a predictor from
z^(-r) is legitimate because its conjugate pairs to zero with
f u. Weighted Cauchy--Schwarz proves

    |b_r|<=e K_A sqrt(c_m D_(m,r)).

The target takes a square root of the squared prediction distance
at precisely the required step.

## 4. Flatness, zero exclusion, and the full beta integral

Applying n!/(n+r)!<=n^(-r) and summing even and odd r separately
gives exactly

    |V(1+t)/V(1)-1|
       <=C{exp(|t|^2/n)-1+(|t|/n)exp(|t|^2/n)},
    C=e K_A.

The estimate holds for every complex t and all odd n. Taking
eta=log(1+1/(4C)) makes the first contribution 1/4 on the
radius-sqrt(eta n) disk. The stated threshold
n>=16C^2 eta exp(2eta) bounds the second contribution by 1/4.
Thus the zero-free disk follows without an implicit root ansatz.

On the real interval x in [0,1], the relative error is bounded
by epsilon_n=2C exp(1/n)/n. The signed Rodrigues integral has
the factor (-1)^n/n!, hence is negative relative to V(1) for
odd n once this relative error is small. For the beta(n+1,n+1)
law, symmetry removes the odd part of exp(-(X-1/2)), and the
variance is 1/[4(2n+3)]. The stated quadratic upper bound for
cosh(y)-1 follows termwise from its power series on |y|<=1/2.
The resulting xi_n and combined relative error theta_n are
correct, including the factor epsilon_n(1+xi_n).

Finally B(n+1,n+1)/n!=n!/(2n+1)! gives the COMPLETE error

    Re_n(1)=-sqrt(e)V_n(1)n!/(2n+1)!(1+O(1/n)).

This is neither a first omitted Taylor coefficient nor just an
absolute integral estimate.

## 5. Stirling constant, sign, and arithmetic scope

The exact odd scalar identity retains s_m and gives the factorial
ratio

    B_m^odd n!/(2n+1)!
       =m!(3m+2)!/[(2m+1)!^2(4m+3)].

For a direct check of the constant, the even inner factorial ratio
m!(3m)!/(2m)!^2 is asymptotic to (sqrt(3)/2)beta^(2m),
where beta=3sqrt(3)/4. The two added numerator factors and the
two denominator factors contribute a limit of 9/4, and division
by 4m+3 gives 9sqrt(3)/(32m) beta^(2m). Replacing 2m by
n=2m+1 makes this exactly (3/(4n))beta^n to leading order.

Therefore the claimed limit is -(3/4)sqrt(e)s_infty. Its sign
is positive because the independently certified interval is
-0.47<s_infty<-0.45. The resulting positive constant interval
(27sqrt(e)/80,141sqrt(e)/400) is correct. The nonzero integer
leading coefficient then gives eventual unreduced growth at
least c beta^n/n. Combining with the passed even theorem is valid
for the all-degree root rate and eventual lower bound.

These conclusions concern the unreduced exponential contribution.
They do not estimate cancellation with Ra or the endpoint gcd.
For the conventional positive-denominator primitive form, the
precise expression is sign(Z_n)[Re_n(1)+4Ra_n(1)]/g_n. The
target's final display omitted only this overall sign; the author
was asked to include it or state explicitly that the formula is
up to an overall sign. The header was also asked to reflect the
now-completed independent certificate review.

No substantive gap was found.
