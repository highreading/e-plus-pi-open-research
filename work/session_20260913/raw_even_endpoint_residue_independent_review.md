> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the even endpoint residue asymptotic

Date: 2026-09-13. Reviewer: audit_results.
Target: raw_even_endpoint_residue_asymptotic.md, all sections.
Verdict: PASS. No mathematical correction required.

I checked the new algebraic global-circle argument, its analytic domains,
the exact residue and saddle normalization, and the reduction to the
actual primitive denominator. This review uses the already passed
interior multiplier theorem and the separately completed end-to-end
audit of the exterior arctangent assembly. It does not assume a bound
on the primitive denominator.

## 1. Domain and the algebraic circle maximum

The functions L and its selected square root are analytic on the unit
disk. For the new variable x, the zeros of 1+x+x^2 are on the unit
circle, so its square root S with S(0)=1 is analytic in |x|<1.
The denominator 1+x+S cannot vanish there: S=-1-x would imply x=0
after squaring, contradicting S(0)=1. Thus b is well-defined.

Its exact quadratic is

    x b^2-2(1+x)b+1=0,

which proves b!=0,2. Also b=1 would force x=-1, outside the disk.
Consequently all displayed denominators in the source's equation
(3), including 1-b, are nonzero. The logarithm log(1+x) is likewise
the analytic branch normalized at zero on this disk.

Direct substitution gives exactly

    x=(1-2b)/[b(2-b)],
    x h'(x)=(1-2b)/[2(1-b)].

For b=u+iv, clearing the positive squared denominator verifies

    Im x=-2v(u^2+v^2-u+1)/|b(2-b)|^2.

The factor u^2+v^2-u+1 is strictly positive, while

    Im[xh'(x)]=-v/[2|1-b|^2].

Thus these two imaginary parts have the SAME strict sign whenever
Im x is nonzero. This is a global algebraic sign proof, not a
local Taylor assertion or a sampled inequality.

On x=s exp(i theta), the angular derivative is minus the latter
imaginary part. Hence Re h is strictly decreasing on the upper
semicircle and strictly increasing on the lower semicircle, with
its unique maximum at x=s. This proves the asserted maximum for
each fixed radius 0<s<1.

For z on |z|=r, the even part h(z^2) is maximal at exactly z=+r
and z=-r. The remaining term -log|1-z| has its unique maximum
at z=+r. Their individual upper bounds are simultaneously attained
only at +r, so the sum has a unique strict maximum there. This
argument correctly rules out a competing contribution at -r.
Compactness supplies a positive gap off any fixed neighborhood.

## 2. Exact residue, orientation, and the original leading coefficient

The original dual reconstruction and its even Toeplitz equation give

    u_n=[t^n]U_n=(2n)![t^n]V_n=n!V_n(1)v_0!=0.

The already passed residue identity, now divided by v_0, is

    Z_n/u_n=-Res_0
       D^n(v/v_0)/[z^(2n+1)(z-1)^(n+1)].

Since n is even, (z-1)^(n+1)=-(1-z)^(n+1). These two minus
signs cancel. The counterclockwise circle of radius rho encloses
only zero, since rho<1. Cauchy's residue formula therefore has
the POSITIVE prefactor 1/(2 pi i) in equation (2).

This is a closed contour for the residue itself. It is not an
unjustified move of the left arctangent path through the positive
saddle. The explicit residue which distinguishes those paths
remains present in the earlier identity.

After substituting the compact base expansion, the nth-power
factor is

    D(z) exp(L(-z^2)/2)/[z^2(1-z)].

The leftover rational factor is 1/[z(1-z)]. Parameterization
dz=i z dtheta cancels exactly this leftover z and changes
1/(2 pi i) to 1/(2 pi). Thus the source's amplitude is precisely

    exp(H(-z^2)) R_n(z)/(1-z) [1+O(1/n)],

with no extra rho, 2, pi or factorial.

## 3. Stationary point, height, and positive curvature

Differentiating the exact xh' formula proves

    H_in'(z)=-1/[z(1-b(z^2))]+1/(1-z).

At z=rho, b(rho^2)=rho^2 and 1-b=rho, so it vanishes.
The inverse derivative is exactly

    b'(x)=-b^2(2-b)^2/[2(b^2-b+1)].

At x=rho^2 this simplifies to -1/4. Direct differentiation then
gives

    H_in''(rho)=[1+rho+rho^2/2]/rho^4
               =(25+11sqrt(5))/4.

Multiplying by rho^2 gives

    kappa=rho^2 H_in''(rho)=rho^(-3)+1/2
                           =5/2+sqrt(5)>0.

Thus the angular second derivative is -kappa, not
-H_in''(rho). The source retains the correct rho^2 factor.

For the height, the closed primitive is evaluated at
chi=b=rho^2:

    exp L(-rho^2)
       =(27/4)rho^2/[(2-rho^2)(1+rho^2)^2].

Substitution into the square of the nth-power factor, using
1-rho=rho^2 and 2-rho^2=1/rho, gives

    exp(2 H_in(rho))=27/(4rho^5).

The branch is real at this positive saddle, so its exponential is
the positive xi, not an unspecified square root. The exact
identity tau/xi=rho^5 follows immediately.

The symbolic residuals for the inverse derivative, imaginary-sign
identity, circle curvature and curvature ratio all simplify to
zero. These were algebraic checks only, not new degree computations.

## 4. Complete varying-amplitude saddle argument

The circle and a neighborhood of it lie in |z|<1, so both the
base-polynomial relative expansion and the proved actual R_n
convergence apply on fixed compact sets, uniformly as m grows.
The relative error belongs only to the base factor; no division
by a possibly zero R_n is made.

The explicitly parameterized phase

    P(theta)=h(rho^2 exp(2i theta))
       -2 log rho-2i theta-log(1-rho exp(i theta))

avoids a false global branch of log z. Its endpoint values can
differ by an integer multiple of 2 pi i; its nth exponential is
the exact periodic factor for every integer n. There is no
additional contribution from that bookkeeping difference.

At theta=0, P'=0 and P''=-kappa. A fixed neighborhood therefore
has the uniform Gaussian majorant exp(-kappa n theta^2/4).
The strict maximum gives an exponentially smaller bound on the
remainder of the circle, with a fixed positive gap.

The actual amplitudes are uniformly bounded and converge uniformly
on the circle. On theta=t/sqrt(n), their values tend to

    a_0=exp(H(-rho^2)) B_s/(1-rho)>0.

Extending the rescaled local integrand by zero outside its growing
interval gives an integrable Gaussian majorant independent of n.
Dominated convergence therefore applies to the complete local
integral. The outside-circle part is already negligible. This
justifies the relative 1+o(1) result without a convergence rate
for R_n.

Finally,

    (1/(2pi)) integral_R exp(-kappa t^2/2)dt
       =1/sqrt(2pi kappa),

so the source's constant is exactly

    C_Z=exp(H(-rho^2)) B_s/
          [(1-rho)sqrt(2pi kappa)]>0.

The endpoint asymptotic therefore proves, in particular,

    sign Z_n=sign u_n=sign([t^n]V_n)

for every sufficiently large even n. This is an eventual sign
theorem; it does not impose a sign on the initially chosen
primitive cofactor orientation.

## 5. The exact relative approximation constant

The exterior arctangent theorem was independently audited as a
complete chain in raw_even_saddle_assembly_independent_review.md.
It does not depend on this endpoint residue theorem or its
interior amplitude. Hence combining them here creates no cycle.

Its constant is

    C_a=(rho^3/2) exp(H(-rho^2))
                    sqrt(2pi/h_out) A_s.

The common transport factor cancels. The direct exact identity

    H_in''(rho)/h_out=rho^(-10)

and kappa=rho^2 H_in''(rho) give

    C_a/C_Z
       =pi rho^3(1-rho)sqrt(kappa/h_out) A_s/B_s
       =pi rho A_s/B_s.

All factors under the square roots are positive, which selects
the positive value of this quotient. The even exterior amplitude
retains its factor (-1)^m; the interior one has none. Therefore

    Ra_n(1)/Z_n
       =(-1)^m pi rho (A_s/B_s) rho^(5n)[1+o(1)].

The independent exponential upper bound has the same original
leading coefficient, so

    Re_n(1)/Ra_n(1)
       =O((beta/tau)^n/[(2n)!sqrt(n)])->0.

The factor FOUR in the original error Re+4Ra now gives exactly

    (e+pi)-N_n/Z_n
       =(-1)^m [4pi rho A_s/B_s] rho^(5n)[1+o(1)].

This is the actual approximation error, not an unrelated
reconstructed family. Its eventual sign and nonvanishing follow
from the strictly positive fixed constant.

## 6. Primitive denominator and the exact remaining threshold

The reduction is correctly written as

    g_n=gcd(|Z_n|,|N_n|),
    q_n=|Z_n|/g_n>0,
    p_n=sign(Z_n)N_n/g_n,

so p_n/q_n=N_n/Z_n and

    ell_n=q_n(e+pi)-p_n
         =sign(Z_n)[Z_n(e+pi)-N_n]/g_n.

The residue asymptotic alone does not bound q_n. However, the
proved relative approximation now gives the exact relation

    |ell_n| ~ C_app q_n rho^(5n),
    C_app=4pi rho A_s/B_s>0.

Consequently, on any even subsequence tending to infinity,
ell_n tends to zero if and only if q_n rho^(5n) tends to zero.
This is a full asymptotic equivalence; no regularity, monotonicity
or exponential rate for q_n is assumed.

Using |Z_n|~C_Z|u_n|xi^n/sqrt(n), and xi rho^5=tau,
the same condition is equivalent to

    g_n/[|u_n|tau^n/sqrt(n)]->infinity.

The stated strict limsup bound on log(q_n)/n is sufficient.
The liminf condition likewise supplies a shrinking subsequence.
Neither condition is established by the analytic proof.

The final conditional irrationality implication is elementary
and valid: if the target equaled a/b, each nonzero primitive
form would be an integer multiple of 1/b. Eventual nonvanishing
is already supplied by the signed error asymptotic. What remains
missing is precisely the required shrinking denominator/gcd
condition, so the note correctly draws no irrationality conclusion.

## 7. Verdict

PASS on the complete endpoint theorem and its approximation
corollaries. The algebraic global maximum, square-root domains,
positive height and curvature, 2 pi contour factor, original u_n
normalization, both amplitude phases, exact quotient constant,
eventual sign and primitive-denominator threshold all check.

No canonical degree, root, prime or numerical contour scan was
performed. No change to the proved mathematical statement is needed.

