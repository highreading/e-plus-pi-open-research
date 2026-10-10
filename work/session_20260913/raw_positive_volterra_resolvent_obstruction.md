> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A positive Volterra operator whose actual spectral resolvent creates sign changes

Date: 2026-09-13. Original continuation by audit_computations. Independent root review passed: raw_positive_resolvent_root_review.md.

This note proves an eventual obstruction for the ACTUAL scalar resolvent
at lambda_k=k(k+1). It does not refute total positivity of either regular
origin branch sampled on its own grid, and does not refute the proposed
n-zero bound for the actual high span. The forcing used below is a smooth
localized function, not an element of that high span.

## 1. What the positive factorization really proves

Use the exact operator and inverse from
`raw_mixed_parity_volterra_and_darboux.md`, Section 7:

    L=D s^(-1) D x^2 s^2 D s^(-1) D,
    K=I M_s I M_(x^(-2)s^(-2)) I M_s I,
    s=sin(x)/x>0 on (0,1).

For continuous inputs the two integrations preceding the singular weight
produce O(x^2), so all these operations are defined. Each multiplication
preserves sign changes, and integration from zero cannot increase them.
For the latter assertion, if an integral has alternating nonzero values
at ordered points, the fundamental theorem of calculus supplies input
values of the corresponding alternating signs, starting with the first
interval from zero. Applying this to each factor proves

    signchanges(Kf) <= signchanges(f).                       (1)

Its scalar kernel, for strictly positive source and target arguments,
is also totally nonnegative of every order. One proof composes the
kernels 1_(t<x) with the positive weights. Their ordered minors are 0 or
1; continuous Cauchy--Binet preserves their nonnegative signs. Truncate
the intermediate integrations below epsilon>0 before applying this
argument, and then take the finite pointwise limit epsilon down to zero.
No assertion of strict positivity at causally forbidden node patterns
is intended.

For lambda>=0 the regular-origin Green operator is

    K_lambda=(I-lambda K)^(-1)K
            =sum_(j>=0) lambda^j K^(j+1).                    (2)

The factorial iteration bound in the preceding note proves convergence.
The kernel is positive for 0<y<x<1. The positivity in (2) does NOT preserve
all minor signs under summation.

## 2. The exact local large-parameter limit

Fix a=1/2, put epsilon=(a^2/lambda)^(1/4), and denote the causal kernel
of (2) by k_lambda(x,y). It solves

    (L_x-lambda)k_lambda(x,y)=0  for x>y,
    k=k_x=k_xx=0,  k_xxx=1/y^2  at x=y+.

The jump follows by integrating the differential equation against its
unit point source. Define

    g_epsilon(u,v)=(a^2/epsilon^3)
                   k_lambda(a+epsilon u,a+epsilon v).        (3)

On every fixed triangle 0<=v<=u<=T, provided epsilon T<a/2,
its homogeneous differential equation has coefficients

    [(a+epsilon u)^2/a^2] g_uuuu
    +[4epsilon(a+epsilon u)/a^2] g_uuu
    +[epsilon^2((a+epsilon u)^2+2)/a^2] g_uu
    +[2epsilon^3(a+epsilon u)/a^2] g_u - g =0,                 (4)

with initial third derivative a^2/(a+epsilon v)^2. All other initial
jets vanish. Thus uniformly on the triangle, through the first three
u derivatives,

    g_epsilon(u,v)=g(u-v)+O_T(epsilon),
    g(t)=(sinh(t)-sin(t))/2.                                  (5)

This is a direct ordinary differential equation estimate, not WKB
extrapolation. After division by the leading coefficient, the first-order
4x4 companion matrices differ from the constant limiting matrix by
O_T(epsilon), and their initial vectors differ by O_T(epsilon).
Variation of constants and Gronwall on the fixed interval prove (5),
with an explicitly computable constant. In particular it holds along
EVERY sufficiently large lambda_k=k(k+1), not just a selected subsequence.

## 3. A strictly negative two-by-two minor

Take h=pi/2 and t=2pi. At source coordinates 0,h and target coordinates
t,t+h, the limiting determinant is

    Delta=g(t)^2-g(t-h)g(t+h)
         =[cosh(h)^2-2cosh(t)sinh(h)]/4 <0.                  (6)

To verify the identity, use sin(t)=0, sin(t-h)=-1,
sin(t+h)=1 and
`sinh(t-h)sinh(t+h)=sinh(t)^2-sinh(h)^2`.
The strict inequality follows, for example, from sinh(pi/2)>1 and
cosh(2pi)>cosh(pi/2)^2. All four entries are strictly positive.

Choose T=t+h. Formula (5) and (6) imply that for every sufficiently
large lambda the corresponding ACTUAL determinant of k_lambda at

    sources a, a+epsilon h;
    targets a+epsilon t, a+epsilon(t+h)

is negative. The common normalization factor in (3) is positive, so
it cannot change the sign. All four points lie in (0,1).
Hence K_lambda fails total nonnegativity of order two for all sufficiently
large actual lambda_k. This is an exact asymptotic sign proof based on
a nonzero limiting determinant; it contains no finite root or matrix scan.

## 4. A smooth forcing with one input sign change and two output changes

The same construction proves failure of variation diminution, not just
failure of a particular minor sign. The limiting source ratio

    q(u)=g(u)/g(u-h), u>h,

satisfies q(u)->infinity as u decreases to h, while (6) says
q(t)<q(t+h). Choose c strictly between those last two values and then
choose u0 in (h,t) sufficiently close to h that q(u0)>c.
For all sufficiently small epsilon, the actual function

    k_lambda(x,a)-c k_lambda(x,a+epsilon h)

has signs +,-,+ at the three target points with coordinates u0,t,t+h.
Replace the two point sources by nonnegative smooth bumps of equal
unit integral supported in sufficiently small disjoint neighborhoods
of a and a+epsilon h. Give the second bump coefficient -c. The input
has exactly one sign change. Continuity of the Green kernel away from
its diagonal preserves all three strict output signs, proving at least
two output sign changes.

The bumps can be supported before all three targets. Therefore the
identity part of `(I-lambda K)^(-1)=I+lambda K_lambda` vanishes at those
targets, and that full resolvent fails variation diminution as well.
The bump width may depend on lambda; no false uniform forcing claim
is used.

## 5. Exact scope and remaining family-specific lemma

There is no contradiction with positivity of K_lambda: the constructed
input has both signs. There is also no contradiction with absolute
monotonicity of the two normalized origin solutions G0,G1 in lambda.
Their seeds are the specific functions 1 and Si, not the localized
forcing in Section 4. Moving x near a fixed positive a while lambda
runs over the actual grid does not convert this example into a mixed
high-block combination.

The general resolvent variation-diminishing bridge is therefore closed.
The remaining plausible use of (1) must preserve the actual coupled
parity recurrences and their boundary members. One concrete next problem
is to control zeros of the coupled finite high block driven by those
few boundary functions; arbitrary-forcing positivity cannot replace
that additional argument.
