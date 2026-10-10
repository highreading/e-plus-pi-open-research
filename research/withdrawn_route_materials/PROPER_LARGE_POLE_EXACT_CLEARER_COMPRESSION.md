> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# M34. Proper large-pole moments: exact restricted clearer, old-mass compression and complete tail

Original algebraic/arithmetic interface, 2026-10-02. This completes Root's currently planned large-pole target before the human-requested Genesis transition. No independent review or main irrationality proof is claimed.

## Fresh archive and primary-paper gate

Fresh bounded archive searches covered beta-prime moments, pole order3k, order tending to infinity, delta-limit response and large arctangent order in sources and the20260913/20260927/20261001_astra/current sessions. Read M31 GENERAL_POLE_RANK_M_PRIMITIVE_INTERFACE.md for its exact jets, normalization and universal response/moment clearers. Older rational-multiplier/prime-support hits concern distinct contours and local content. The existing m<=k theorem does not cover this proper-moment regime.

Fresh online queries covered beta-prime moments, Wallis/arctan irrationality integrals and large-parameter Jacobi-to-Laguerre asymptotics. Opened the primary NIST DLMF5.12 https://dlmf.nist.gov/5.12, Euler's beta integral. The beta-prime moment evaluation is established mathematics and is derived directly below. Primary large-parameter papers found during the query do not supply a uniform full primitive determinant conclusion for this matching matrix; no uninspected asymptotic theorem is used. Agent3's separately fresh-gated PROPER_LARGE_POLE_FULL_STACK_GATE.md contains the analytic gate and complete large-m perturbation result.

Novelty boundary: the exact restricted-response denominator prefix walk, the actual complete rational old-mass compression, and its full primitive-cost interface in this new regime. Neither beta-prime moments nor the integer small-form criterion is claimed novel.

## Positive proper moment functional and its LEAST restricted clearer

Let R=3k-2 and m>=R+1. With c_m=4^m/binom(2m-2,m-1), define the probability measure on y>=0

    dpsi_m(y)=c_m/[4pi sqrt(y)(1+y)^m] dy.

Euler's beta integral gives, for0<=r<=R,

    nu_(m,r)=psi_m(y^r)
            =product_(j=1)^r (2j-1)/(2m-2j-1).             (1)

Its0th moment is1. The formula equals the exact rational jet response from M31, but only the proper degrees in (1) are asserted to have this positive-measure representation. No integral of a divergent higher degree is assigned a formal moment.

The LEAST common response clearer is

    A_(m,R)=lcm_(0<=r<=R) den(nu_(m,r)),
    v_p(A)=max(0,max_(1<=r<=R)
                sum_(j=1)^r[v_p(2m-2j-1)-v_p(2j-1)]).     (2)

This prefix maximum is exact at every prime. It is not generally the denominator of the last moment. At(m,R)=(10,3), the three positive-degree denominators are17,85,221, so A=1105 while den(nu3)=221.

Writing D_(m,R)=product_(j=1)^R(2m-2j-1), every prefix denominator divides D_(m,R), hence

    A_(m,R)|D_(m,R),   log A<=R log(2m).                    (3)

The restricted period response thus has polynomial-in-m cost at fixed k; the full-degree universal B_m from M31 must not be imposed as a necessary cost for these proper nu moments alone.

## Exact rational correction and one-scalar old-mass compression

The actual compact rational-pole moment is

    c_m integral_0^1 x^(2r)/(1+x²)^m dx
                       =alpha_(m,r)+pi nu_(m,r).

For r>=1, integrate the derivative of x^(2r-1)/(1+x²)^(m-1). BOTH endpoints are included: its boundary value is2^(1-m). Therefore

    (2m-2r-1) alpha_r=(2r-1)alpha_(r-1)-b_m,
    b_m=c_m2^(1-m)=2^(m+1)/binom(2m-2,m-1).               (4)

Let h0=0, h_r=[(2r-1)h_(r-1)+1]/(2m-2r-1). The FULL correction is exactly

    alpha_r=alpha0 nu_r-b_m h_r,
    alpha0=2 sum_(j=0)^(m-2) j!/(2j+1)!!.                 (5)

The complete matching construction consequently compresses to

    beta_(k,m)(T)=det[mu-nu;
                   -factorials-b_m H+(T+alpha0)V],        (6)

where H_(i,j)=h_(i+j), V_(i,j)=nu_(i+j). No exponential row, rational endpoint term or period coefficient has been discarded. In particular alpha0 is an actual rational quantity tending to pi; it is not replaced by pi within any integer arithmetic claim.

Because v2 binom(2d,d)=s2(d)<=d for d=m-1, the numerator2^(m+1) removes its complete dyadic part. The EXACT denominator of b_m is

    B_m=oddpart binom(2m-2,m-1).                           (7)

It can have exponential cost in m. The small REAL size of b_m does not imply a small rational denominator.

## ENTIRE tail and the rank-one large-m limit

Define the actual positive omitted-tail integral

    tail_(m,r)=c_m integral_1^infty x^(2r)/(1+x²)^m dx>0.

The proper full half-line moment is2pi nu_r, so EXACTLY

    alpha_r=pi nu_r-tail_(m,r).                            (8)

The elementary induction binom(2d,d)>=4^d/(d+1) gives c_m<=4m. Using1+x²>=2x on x>=1 gives, when m>2R+1,

    0<tail_(m,r)<=4m2^(-m)/(m-2r-1).

Thus for m>=4R+2, ALL0<=r<=R satisfy tail_r<=8·2^(-m). Also for m>=4R+2,

    0<nu_r<=nu1=1/(2m-3),   1<=r<=R.                      (9)

Every ratio in(1) after the first is at most1 in this range. Equations(8)--(9) prove the FIXED-k complete limit

    beta_(k,m)(T) --> beta_infinity,k(T)
      =det[mu-delta0; -factorials+(T+pi)delta0].            (10)

This is a real-coefficient affine limiting polynomial. It is not a rational-coefficient polynomial because the actual rational alpha0 approaches pi. The proper regime has not generated an independent growing set of periods: its response collapses to a single evaluation at0.

Agent3 supplies the actual cofactor sign, the limiting root near e-pi, and an explicit whole-coefficient perturbation threshold. That threshold, rather than arbitrary m/k tending to infinity, defines the proved large-m exclusion range.

## Actual entry clearers, all final coefficients and content

Every h_r has denominator dividing D_(m,R), by its exact recurrence. Let a0=den(alpha0). The explicit whole-entry clearer

    delta=a0 B_m D_(m,R)                                  (11)

clears C, V and the COMPLETE R block in(6). This is a sufficient clearer; the least one is the lcm of the actual entry denominators and can be smaller. M31's partial-fraction bound supplies a0|B_m2^(3m+2)lcm(1,...,m), so log delta=O(m+Rlog(2m)). Thus the stack clearer cost is O(km+k²log(2m)), including the rational correction. Only the restricted nu cost in(3) is O(klog m).

If I_j=[T^j]delta^(2k) beta_(k,m)(T) and g=gcd_j(I_j), the FINAL primitive polynomial is I(T)/g, with its actual height H. A smaller consistent row clearer produces the identical primitive polynomial. No raw determinant, period-only denominator or exponent from(3) is substituted for this final H or g.

The analytic no-small-form theorem in the explicit very-large-m range compares |beta(S)| directly with its coefficient height. Such a ratio is unchanged by the positive scaling delta^(2k)/g, so its exclusion is independent of unproved content estimates. It does not settle the intermediate m range, which remains explicitly outside the result.
