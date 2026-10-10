> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Assembly of the even signed dual saddle asymptotic

Date: 2026-09-13. Original continuation by audit_computations.
Independent review: PASS by audit_results; see
raw_even_saddle_assembly_independent_review.md for the end-to-end
normalization audit and dependency chain. Its separate phase and
amplitude inputs have also passed independent review, as recorded
below. The theorem does not assert a proof about the rationality of e+pi.

This note proves that a pointwise saddle-value limit, together with the
already proved uniform Hardy norm, suffices for the varying actual
multiplier. Uniform convergence of the whole multiplier is not needed.
All contour, factorial, and primitive-gcd normalizations are retained.

## 1. Inputs, status, and exact statement

Let n=2m, rho=(sqrt(5)-1)/2, phi=1/rho, and put

    z_s=-phi,
    h_2=(25-11sqrt(5))/4>0,
    tau=sqrt(27rho^5/4),
    C_s=(rho^2/4)sqrt(3pi/h_2)>0.                         (1)

The actual polynomials satisfy

    u_n=[t^n]U_n=(2n)! v_n^lead,
    v_n^lead=[t^n]V_n in Z,              v_n^lead!=0.

This u_n is the leading coefficient of U, not the Toeplitz polynomial
called u in the multiplier note. Here we retain v(z)=A^(-1)e_0 and
v_0=v(0)>0 for that normalized polynomial, so

    u_n=n!V_n(1)v_0.

The independently proved analytic inputs are:

1. The exact contour and residue-free outward deformation in
   raw_dual_exterior_saddle_and_endpoint_control.md. The contour Gamma
   is the left arc |z+1/2|=sqrt(5)/2 from -i to i, oriented through
   z_s with upward tangent.
2. The uniform Hardy bound
   ||Rtilde_n||_(H^2)<=C_*=e sec(1), from
   raw_actual_dual_hardy_factor_allocation.md and its reversal
   continuation.
3. The compact exterior base expansion with transport term in
   raw_base_polynomial_uniform_asymptotic.md, independently passed
   in raw_base_uniform_asymptotic_independent_review.md.
4. The unconditional endpoint estimate (12) of the exterior contour
   note, with delta=1/8 and exponential base sigma=sqrt(5)/8<tau.

The two final, independently reviewed inputs are explicitly isolated:

P. On the middle part of Gamma, a=-Re z in [delta,phi], the actual
   analytic phase mathcal H from the exterior note has its unique
   maximum of real part at z_s. Equivalently its explicitly specified
   function E(a) in (13) satisfies E(a)<tau^2 for delta<=a<phi.
   This is proved in raw_exterior_phase_strict_maximum.md, with an
   independent unchanged rerun and complete review in
   raw_exterior_phase_independent_review.md (PASS).

A. The actual multiplier satisfies

    A_n:=(-1)^m Rtilde_n(-rho) -> A_s>0.                  (2)

   This is proved in raw_even_saddle_multiplier_limit.md, with
   0.049<A_s<0.050. Its coordinate interface, alternating phase,
   and identical certificate rerun passed the complete review
   raw_even_saddle_multiplier_independent_review.md. The imaginary-node
   kernel input also passed raw_even_imaginary_kernel_independent_review.md.

Using P, the assembly proves the more precise bounded-sequence formula

    (-1)^m Ra_n(1)/u_n
       =C_s A_n tau^n/sqrt(n)+O(tau^n/n).                (3)

The implied constant does not depend on A_n or its convergence rate;
its uniform boundedness follows from the Hardy estimate. Using A as
well, it follows that

    Ra_n(1)
       =(-1)^m A_s C_s (2n)! v_n^lead
                      tau^n/sqrt(n) [1+o(1)].             (4)

The detailed proof is below. It uses no new canonical degree,
numerical root calculation, or unproved multiplier lower bound.

## 2. The exact contour and analytic amplitude

The whole-error identity, with all factorials intact, is

    Ra_n(1)/u_n=(1/(2i)) integral_Gamma
       D(z)^n[v(z)/v_0]/[z^(2n+1)(z-1)^(n+1)] dz,
    D=1+z^2.                                             (5)

Define f_m(w)=Phi_m^*(w). Formal degree-n reversal gives exactly

    v(z)/v_0=z^n f_m(-1/z^2) Rtilde_n(1/z).

On each compact subarc away from the endpoints,

    f_m(-1/z^2)
       =exp[(n/2)L(-1/z^2)+H(-1/z^2)](1+epsilon_n(z)),
    epsilon_n=O(1/n),                                    (6)

with the same local bounds for every fixed derivative. The relative
error belongs only to f_m and does not divide by Rtilde_n.
Let

    mathcal H(z)=log D-log(-z)-log(1-z)+(1/2)L(-1/z^2).

Use the analytic branches continued from the real saddle, where this
phase is real. Since n is even, its nth exponential reproduces the
exact nth-power factor in (5). Thus the middle-contour contribution
to (-1)^m Ra/u_n has integrand

    exp(n mathcal H(z)) b_n(z) dz/(2i),

where

    b_n(z)=exp[H(-1/z^2)]
       (-1)^m Rtilde_n(1/z) (1+epsilon_n(z))/[z(z-1)].     (7)

On every fixed neighborhood of the saddle contained in |z|>1,
the functions b_n and their first derivatives are uniformly bounded.
Indeed Hardy evaluation bounds Rtilde_n on every compact subdisk,
and Cauchy estimates then bound its derivatives. Composition with
1/z preserves these bounds near z_s. The other factors are fixed
analytic functions, except for the uniformly O(1/n) base error.

At the saddle the amplitude is exactly

    b_n(z_s)=rho^3 exp[H(-rho^2)] A_n [1+O(1/n)].          (8)

No uniform convergence of b_n on a neighborhood is required to
evaluate this expression or obtain its uniform derivative bounds.

## 3. Local Gaussian lemma for a varying multiplier

Use the imaginary coordinate y on the part of Gamma near the saddle:

    z(y)=-(1+sqrt(5-4y^2))/2+i y,
    z(0)=z_s,      z'(0)=i.

The contour orientation makes y increase from negative to positive.
Let psi(y)=mathcal H(z(y))-mathcal H(z_s). The known exact saddle
derivatives give

    psi(0)=psi'(0)=0,
    psi(y)=-(h_2/2)y^2+O(y^3).

For a sufficiently small fixed epsilon>0,

    Re psi(y)<=-c y^2,          |y|<=epsilon,

with c>0 independent of n. Put

    g_n(y)=b_n(z(y))z'(y)/(2i).

The preceding bounds give uniform bounds on g_n and its derivative.
In particular |g_n(y)-g_n(0)|<=C|y|. Comparing the phase with
-h_2y^2/2 gives the elementary uniform error estimate

    |exp(n psi(y))-exp(-n h_2 y^2/2)|
       <=C n |y|^3 exp(-c' n y^2),                      (9)

after decreasing epsilon if needed. To prove (9), integrate the
derivative of the exponential along the line segment between its
two exponents; both real parts, and every convex combination of
them, are bounded by -c' n y^2.

Integrating the amplitude error gives O(1/n), since
integral |y| exp(-c'n y^2)dy=O(1/n). Integrating (9) also gives
O(1/n), since n integral |y|^3 exp(-c'n y^2)dy=O(1/n).
The truncated Gaussian differs from the full one exponentially.
Consequently, uniformly for this varying sequence,

    integral_(-epsilon)^epsilon exp(n psi(y))g_n(y)dy
       =g_n(0)sqrt(2pi/(n h_2))+O(1/n).                 (10)

Because z'(0)=i, equations (7)-(8) give

    g_n(0)=(rho^3/2)exp[H(-rho^2)] A_n[1+O(1/n)].         (11)

This proves the local signed leading term. Pointwise convergence
of A_n, plus the uniform derivative bounds, is sufficient; the
proof does not assume convergence of the entire multiplier.

## 4. The rest of the contour and the transport constant

Under P, the compact middle arc outside this fixed saddle neighborhood
has a strictly smaller real phase, say at most log(tau)-eta with
eta>0. Its analytic amplitude is uniformly bounded by the Hardy
estimate and (6), so its contribution is O(tau^n exp(-eta n)).
The two endpoint pieces have absolute contribution O(sigma^n/n)
by the previously proved estimate, with sigma<tau. These are both
absorbed by O(tau^n/n) in (3).

The remaining transport constant can be evaluated exactly. Put

    chi=1/[1-w+sqrt(1-w+w^2)],
    Q(chi)=chi^2-chi+1.

The change of variable used for L in the exterior contour note
gives, for the transport derivative h=H',

    h(w)dw=-(2chi-1)/(2Q(chi)) dchi.

Since H(0)=0 and chi(0)=1/2, integration proves

    exp[H(w)]=sqrt[(3/4)/Q(chi(w))],                     (12)

with the analytic branch equal to one at zero. For example, this
identity can be checked directly from
h=[w(1-w)L''-wL']/(2sqrt(1-w+w^2)); it is not an independent
asymptotic assumption.

At w=-rho^2 one has chi=rho^2 and Q(chi)=2rho^2. Hence

    exp[H(-rho^2)]=sqrt(3/8)/rho.

Combining (10)-(11), the saddle value exp(mathcal H(z_s))=tau,
and the rest-of-contour estimates gives exactly (3), with

    (rho^3/2)exp[H(-rho^2)]sqrt(2pi/h_2)
       =(rho^2/4)sqrt(3pi/h_2)=C_s.

The sign and the factor 1/2 come from the original contour prefactor
and its upward tangent. They do not come from a freely chosen
orientation of a Gaussian integral.

## 5. The full integer combination and the actual gcd

The already passed even exponential-error theorem gives an upper
bound |Re_n(1)/v_n^lead|<=C beta^n/n, beta=3sqrt(3)/4.
Equation (4), using the positive limit in A, implies

    Re_n(1)/Ra_n(1)
       =O((beta/tau)^n/[(2n)!sqrt(n)]) ->0.

Therefore the SAME actual integer form has the asymptotic

    Lambda_n:=Re_n(1)+4Ra_n(1)
       =(-1)^m 4 A_s C_s (2n)! v_n^lead
                       tau^n/sqrt(n) [1+o(1)].            (13)

Thus it is eventually nonzero on the even subsequence, and its
sign relative to v_n^lead is (-1)^m. Since v_n^lead is a nonzero
integer, its unreduced magnitude grows at least at the indicated
factorial scale. This does not say that its reduced primitive
counterpart grows.

For the exact reduction, retain

    Z_n=Qhat_n(1),
    N_n=Pe_n(1)+4Pa_n(1),
    g_n=gcd(|Z_n|,|N_n|),
    ell_n=sign(Z_n)Lambda_n/g_n.

Equation (13) gives, with no assumption on how g_n varies,

    |ell_n| ~ 4A_s C_s
       (2n)! |v_n^lead| tau^n/[g_n sqrt(n)].              (14)

Accordingly, on any even subsequence tending to infinity, primitive
shrinking is equivalent to the concrete arithmetic condition

    g_n/[(2n)! |v_n^lead| tau^n/sqrt(n)] ->infinity.        (15)

An upper or lower estimate for this actual gcd has not been supplied
by the saddle calculation. Equations (13)-(15) do not decide whether
e+pi is rational or irrational.

## 6. Verification boundary

The general varying-multiplier lemma and its normalization are proved
here from the stated inputs. Both P and A retain their separate proof,
interval certificate, and independent PASS review. The complete assembly
has independently passed raw_even_saddle_assembly_independent_review.md,
including its dependency chain and exact primitive-gcd normalization.
The stronger local analytic
convergence proved in the multiplier note is useful but is not required
by this assembly. A pointwise nonzero limit at the saddle and the
already proved Hardy bound suffice.
