> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# End-to-end independent audit of the even signed arctangent asymptotic

Date: 2026-09-13. Reviewer: audit_results.
Target: raw_even_dual_saddle_assembly.md, all sections.
Verdict: PASS. No mathematical correction required.

This is an adversarial audit of the assembled theorem, not only a
confirmation that its individual inputs have review files. I checked the
original primitive normalization, reciprocal-contour sign, the absence of
a dependency cycle, the uniform estimates needed for the varying actual
polynomial, the transport constant, and the final endpoint-gcd equivalence.

I did not rerun already independently certified interval implementations
without a concrete reason. Their exact scope and full-space error
assumptions were checked against the way this assembly uses them.
The only fresh symbolic checks were rational identities for the transport
factor and the saddle prefactor; no canonical degree or root was computed.

## 1. A dependency chain with no cycle

The minimal logical graph is

    exact primitive dual reconstruction and full-column rank
          |                         |
          v                         v
    exact Re/Ra integrals       Aq=n!V(1)e0
          |                         |
          |                 even positive Toeplitz coercivity
          |                         |
          |                V(1), U_lead nonzero; Hardy bound
          |                         |
          |              +----------+-------------+
          |              |                        |
          |              v                        v
          |       explicit base ODE       Cayley/Jacobi right limit
          |       and compact L,H         and coercive E_+ inverse
          |              |                        |
          |              |                  certified witness
          |              |                  residuals + kernel tail
          |              |                        |
          |              v                        v
          +----> exterior contour, phase P       amplitude A_s
          |      and endpoint estimate              |
          |              |                          |
          |              +-------------+------------+
          |                            |
          |                            v
          |               uniform local Gaussian assembly
          |                            |
          |                            v
          |                     signed Ra asymptotic
          |
          +----> even prediction estimates + beta integral
                               |
                               v
                         independent Re upper bound
                               |
    exact type-I/dual endpoint bridge
                  |            |
                  +------ Ra dominates Re
                               |
                               v
                  exact primitive-gcd shrinking criterion

The relevant saved input chains are:

* Primitive identities and full errors:
  raw_dual_endpoint_error_integrals.md and
  raw_joint_dual_hankel_and_even_root_product.md, both independently
  passed. These supply the actual polynomials, not a surrogate family.
* The actual Hardy bound and explicit base:
  raw_actual_dual_hardy_factor_allocation.md,
  raw_dual_factor_accessory_and_boundary_operator.md, and
  raw_base_polynomial_uniform_asymptotic.md. The compact base theorem
  was independently passed in raw_base_uniform_asymptotic_independent_review.md.
* Contour, curvature and endpoints:
  raw_dual_exterior_saddle_and_endpoint_control.md, with
  raw_exterior_saddle_endpoint_independent_review.md.
  Its remaining middle-arc condition is supplied by
  raw_exterior_phase_strict_maximum.md and the independent
  raw_exterior_phase_independent_review.md.
* The actual amplitude:
  raw_even_endpoint_inverse_corner_limit.md and
  raw_even_saddle_multiplier_limit.md, with their independent reviews.
  Its two exact solved columns come from the fully checked fixed-operator
  residual certificate, not from a canonical-degree fit.
* The independent exponential bound:
  raw_even_dual_flatness_and_exponential_error.md and
  raw_even_dual_flatness_independent_review.md.
* The actual reduction:
  raw_actual_endpoint_integral_dual_numerators.md and its passed
  raw_actual_endpoint_integral_numerators_independent_review.md.

The amplitude proof does NOT assume this Ra asymptotic or any endpoint
residue asymptotic. In particular the fixed solved-vector errors use
Q=(A0 E_+)^(-1), whose inverse norm follows from the separate A0 bound
and positive coercivity of E_+. They do not depend on the subsequently
certified odd exceptional determinants being nonzero. Reusing those two
columns for the EVEN amplitude creates no circular dependency.

Likewise the even Re bound is derived from finite predictions and its
real beta integral, not from dominance by Ra. The new interior amplitude
and the prospective Z residue asymptotic are not inputs anywhere in this
assembly, so those results may later use the present theorem without
creating a cycle. No conclusion about e+pi is used in any of these steps.

## 2. Original scalar and both reciprocal-contour signs

Let

    W=t^n(t-1)^n V,
    T=sum_(r=0)^(2n)(n+r)!w_(n+r)t^r,
    S=(1+t^2)^n U,  S^(n)=T,
    q(z)=z^nU(1/z),  v=A^(-1)e0.

Taking the top coefficient in S^(n)=T gives

    [t^n]U=(2n)!w_(3n)=(2n)![t^n]V.

The exact Toeplitz equation is Aq=n!V(1)e0. Even coercivity makes A
invertible and forces V(1) nonzero; q is not the zero polynomial.
Thus q=n!V(1)v and

    u_n:=[t^n]U=q(0)=n!V(1)v_0=(2n)!v_n^lead.             (R1)

This verifies both equalities used in the assembly. The scalar u_n is
not the normalized Toeplitz polynomial named u in the multiplier note.
The assembly explicitly distinguishes them.

The original full arctangent error is, for even n,

    Ra(1)=(1/(2i)) integral_(-i)^i
                   (1+t^2)^n U(t)/(1-t)^(n+1) dt.

First deform the segment to the left unit semicircle. Its enclosed
region avoids t=1. Put t=1/z on that semicircle. The transformed
integrand is

    -D(z)^n q(z)/[z^(2n+1)(z-1)^(n+1)] dz.

Its endpoints are now i to -i. Reversing them cancels exactly this
minus sign. Substitution of q=n!V(1)v and division by (R1) gives

    Ra(1)/u_n=(1/(2i)) integral_(gamma_L)
               D^n(v/v0)/[z^(2n+1)(z-1)^(n+1)] dz.

Therefore the assembly's equation (5) is the complete original error,
with no omitted Taylor remainder, factorial, or global sign.

The further deformation to the left arc |z+1/2|=sqrt(5)/2 crosses
neither 0 nor 1. Both paths have the same endpoints and lie in the
left half-plane; the endpoints themselves are zeros of D^n and are
regular for the rational integrand. Thus this deformation introduces
no residue. In particular it does not silently substitute the
different right-hand interior contour.

## 3. Exact reversal, analytic sheets, and the parity factor

Formal reversal of degree n gives exactly

    v/v0=z^n f_m(-1/z^2)Rtilde_n(1/z).

The relative O(1/n) expansion belongs only to f_m. It therefore
remains valid when Rtilde_n vanishes; no reciprocal multiplier
is hidden in an error term.

After reversal the nth-power rational factor is D/[z(z-1)], and
the remaining prefactor is 1/[z(z-1)]. The real-normalized phase
log D-log(-z)-log(1-z)+(1/2)L(-1/z^2) has the same nth exponential
on the retained even family. The analytic square root agrees with
its value at zero since |z|>1 implies |-1/z^2|<1. The passed phase
certificate explicitly checks the positive-real square-root sheet;
it does not use a branch of the interior saddle equation.

A continuous analytic logarithm may be chosen on a neighborhood of
the compact middle arc, excluding its two endpoint zeros of D.
At the saddle the phase is real, its exponential is tau>0, and
its second derivative is the positive h_2 stated in the assembly.

The actual amplitude theorem gives

    A_n=(-1)^m Rtilde_n(-rho)->A_s>0.

Multiplying the whole contour equation by (-1)^m inserts exactly
that phase into b_n. There is no other parity factor from the
Gaussian orientation. At z_s=-phi,

    1/[z_s(z_s-1)]=rho^3>0.

The contour tangent is upward, so dz/(2i)=dy/2 at y=0.
These checks give the sign and factor 1/2 in equation (11).

## 4. Uniformity of the split, the varying multiplier, and the Gaussian error

Fix delta=1/8. On the compact middle arc a=-Re z>=delta,

    |z|^2=1+a>=9/8,
    |-1/z^2|<=8/9,      |1/z|<=sqrt(8/9)<1.

Thus both the base-polynomial expansion and the Hardy evaluation
bound apply on FIXED compacts uniformly in n=2m. Slightly larger
fixed neighborhoods give the required Cauchy derivative bounds.
There is no moving disk approaching the unit circle in this step.

The phase certificate covers the arc from the saddle to angular
parameter 1913/1000, where the independently enclosed a value is
strictly between zero and 1/8. The elementary endpoint estimate
covers all a<=1/8. This is a genuine overlap: no boundary layer is
left between the certified middle and the endpoint estimate.

On the endpoint pieces the compact base asymptotic is not invoked.
The exact base root estimate and Hardy loss a^(-1/2) yield the
integrable majorant a^(n-1/2). The resulting contribution is
O(sigma^n/n), sigma=sqrt(5)/8<tau, in the SAME Ra/u_n normalization.

Near the saddle the fixed contour can be parameterized by

    z(y)=-(1+sqrt(5-4y^2))/2+iy.

The exact curvature gives psi(y)=-h_2 y^2/2+O(y^3) and
Re psi(y)<=-c y^2 on a fixed small interval. Every b_n and its
first derivative is uniformly bounded there, because the
phase-adjusted Hardy multiplier has the same norm as Rtilde_n.
This uses only an upper Hardy bound, not a convergence rate for A_n.

For the phase error, the segment joining n psi(y) and
-nh_2 y^2/2 remains in Re<=-c'n y^2. Integrating the derivative
of the exponential on that segment proves the displayed bound
C n|y|^3 exp(-c'n y^2). Its integral is O(1/n).
The amplitude difference has bound C|y| and also integrates to
O(1/n). Extending the truncated Gaussian costs exponentially less.

Hence the local formula really has a uniform absolute O(1/n)
error before multiplication by tau^n. The base relative O(1/n)
error at the saddle contributes only O(n^(-3/2)) because A_n
is uniformly bounded. No term proportional to 1/A_n appears.

Outside this fixed local interval, the strict phase maximum and
compactness give a positive fixed gap. Together with the bounded
amplitude and endpoint estimates this proves exactly the assembly's

    (-1)^m Ra/u_n
       =C_s A_n tau^n/sqrt(n)+O(tau^n/n).

Only after this estimate is proved is A_n->A_s>0 used to obtain
a signed relative 1+o(1) asymptotic. This order avoids an unjustified
uniform-relative estimate at a potentially small finite A_n.

## 5. Independent transport-factor calculation

I checked the transport factor directly, rather than identifying it
from a numerical saddle value. With

    w=(2chi-1)/[chi(2-chi)],
    S=1/chi-1+w,    r=1/(1+S),

substitution in h=[w(1-w)r'-wr]/(2S) gives the rational identity

    h(w)dw=-(2chi-1)dchi/[2(chi^2-chi+1)].

Its difference from the right-hand side simplifies identically to
zero. Since chi(0)=1/2 and H(0)=0,

    exp H=sqrt[(3/4)/(chi^2-chi+1)]

with the branch equal to one at the origin. At w=-rho^2,
chi=rho^2 and chi^2-chi+1=2rho^2. Therefore

    exp H(-rho^2)=sqrt(3/8)/rho.

Combining this with the positive rho^3/2 from the actual contour
and the Gaussian factor gives

    C_s=(rho^3/2)(sqrt(3/8)/rho)sqrt(2pi/h_2)
       =(rho^2/4)sqrt(3pi/h_2).

Every scalar matches. The branch is positive at the real saddle;
a square-root sign is not inferred from its square alone.

## 6. Dominance and exact primitive arithmetic

The independent even exponential theorem gives
|Re/v_n^lead|<=C beta^n/n. The new signed estimate and A_s>0 give

    Re/Ra=O((beta/tau)^n/[(2n)!sqrt(n)])->0.

Here the common signed coefficient v_n^lead cancels, and its
nonvanishing was already proved before the saddle argument.
Thus Lambda=Re+4Ra has the stated leading factor FOUR and is
eventually nonzero on the even subsequence.

The exact endpoint bridge is

    Z=Qhat(1)!=0,   N=Pe(1)+4Pa(1),
    Lambda=Z(e+pi)-N,
    g=gcd(|Z|,|N|),
    ell=sign(Z)Lambda/g.

This is the actual canonical endpoint primitive form. Primitivity
of the cofactor polynomial V does not make g equal to one.
The assembly retains g throughout.

Taking absolute values gives, without any regularity assumption
on the integer sequence g,

    |ell| ~ 4 A_s C_s
       (2n)! |v_n^lead| tau^n/[g sqrt(n)].

The multiplier 4 A_s C_s is fixed and strictly positive.
Consequently, along any even subsequence tending to infinity,
ell->0 is equivalent to

    g/[(2n)! |v_n^lead| tau^n/sqrt(n)]->infinity.

This is an exact necessary-and-sufficient shrinking criterion for
this family and normalization, not merely an exponential-rate
heuristic. The assembly does not claim to prove this criterion.

The integer v_n^lead is nonzero, so the unreduced magnitude has
the asserted factorial lower scale. That observation alone says
nothing about the primitive magnitude after division by g.

## 7. Final verdict and limits

PASS on the full assembled intermediate theorem. I found no
dependency cycle, sign or factorial loss, uncovered endpoint region,
unjustified varying-multiplier interchange, or primitive-normalization
error. The absolute O(tau^n/n) estimate and the signed relative
asymptotic have the scopes stated in the source.

This audit does not establish a quantitative endpoint-gcd bound,
does not convert eventual nonvanishing of Lambda into primitive
shrinking, and does not resolve rationality or irrationality of e+pi.

