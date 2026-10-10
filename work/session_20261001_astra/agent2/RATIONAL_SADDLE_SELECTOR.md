> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rational saddle-cancelling selectors on the two forcing columns

New author analytic research. Existing reconstruction results and the initial working note are preserved. No numerical computation, scan, or independent audit is performed.

## Exact contractions before absolute values

Put R=sqrt(2), M=1+R, chi=R-1, s=chi/M=chi^2, and V(t)=t^2-t+1/2. Use the actual forcing columns fP,fQ and their complete decomposition fQ=(e+pi)fP+eF+eE.

For any rational polynomial L=sum lambda_i t^i, define D_n(L)=sum lambda_i fP_i. Direct coefficient comparison gives

    D_n(L)=D_t^n[V(t)^n L(t)] at t=1.

Consequently Cauchy's derivative formula on t=1+exp(i theta)/sqrt(2) gives

    D_n(L)=n!/(2pi) integral_-pi^pi
       (1+R cos theta)^n L(1+exp(i theta)/R) dtheta.       (1)

The arbitrary-polynomial complete logarithmic arc identity gives

    F_n(L)=sum lambda_i eF_i
      =(-1)^(n+1)2n! integral_-pi/4^pi/4
       (R cos theta-1)^n L(1-exp(i theta)/R) dtheta.      (2)

It follows by coefficient comparison, n integrations by parts with zero boundary terms at both roots of V, and deformation through a region excluding t=1. No center-adjoint normalization is needed.

The complete exponential residual is

    E_n(L)=-integral_0^1 x^n exp(1-x)
       sum_i lambda_i [z^(n+i)]Q0(z)^n exp(xz) dx,       (3)
    Q0(z)=1-z+z^2/2.

Only when D_n(L) is nonzero do we define the rational number c_n(L)=sum lambda_i fQ_i/D_n(L). Then exactly

    c_n(L)-(e+pi)=[F_n(L)+E_n(L)]/D_n(L).              (4)

There is no additional reconstructed endpoint constant in this direct quotient. Equation (3), however, cannot be dropped.

Take L_m(t)=(2t^2-4t+1)^(2m), m>=0, degree 4m. In a b-window require 4m<b. At BOTH contour parametrizations in (1)-(2),

    L_m(1 +/- exp(i theta)/R)
      =(exp(2i theta)-1)^(2m)
      =(-4)^m sin(theta)^(2m) exp(2mi theta).

Thus, by conjugation symmetry,

    D_n(L_m)=(-4)^m n! I_plus/(2pi),
    F_n(L_m)=(-1)^(n+1)(-4)^m 2n! I_minus,            (5)

where

    I_plus=integral_-pi^pi (1+R cos theta)^n
                        sin(theta)^(2m)cos(2m theta)dtheta,
    I_minus=integral_-pi/4^pi/4 (R cos theta-1)^n
                        sin(theta)^(2m)cos(2m theta)dtheta.

Both conjugate halves, the oscillatory cosine, and the possible negative weight for odd n in I_plus remain in (5).

## Uniform quantified saddle estimate

Here is one deliberately conservative effective domain:

    n>=exp(100), 0<=m<=log n, m an integer.             (6)

Logarithms are natural. This proves a genuinely growing-m statement, not merely fixed-m asymptotics. Define

    c_plus=R/(2M), c_minus=R/(2chi),
    G(c)=Gamma(m+1/2)/(nc)^(m+1/2),
    eps=100(m+1)^2 n^(-3/5)
         +2 exp(5(m+1)-n^(1/5)/32).                    (7)

Then eps<1/4 throughout (6), and

    I_plus=M^n G(c_plus)(1+delta_plus),
    I_minus=chi^n G(c_minus)(1+delta_minus),
    |delta_plus|, |delta_minus|<=eps.                 (8)

Proof with uniform tails: put d0=n^(-2/5). On |theta|<=d0 both scalar weights are positive. Taylor's theorem gives, for either normalized weight g,

    |log g(theta)+c theta^2|<=10 theta^4,
    |log(sin theta/theta)|<=theta^2,
    |1-cos(2m theta)|<=2m^2 theta^2.

The first estimate follows by writing g=1-k(1-cos theta), with k=R/M or R/chi<4, and using the convergent logarithm expansion on this tiny interval. The other two estimates follow from the sine series and 1-cos x<=x^2/2. Therefore the ratio of the exact central integrand to theta^(2m)exp(-nc theta^2) differs from one by at most

    100(m+1)^2 n^(-3/5).

The constant accommodates exponentiation, since 10n d0^4+2m d0^2 is less than one in (6).

For the complete plus contour, the elementary global inequality

    |1+R cos theta|/M<=exp(-theta^2/16), |theta|<=pi,

retains the odd-n portion as well. For the minus arc one has the stronger bound (R cos theta-1)/chi<=exp(-theta^2). These inequalities follow respectively by splitting the sign of 1+R cos theta, and by using 1-cos theta>=theta^2/3 on the shorter arc. Also |sin theta|<=|theta| and |cos(2m theta)|<=1.

Outside |theta|<=d0, extract exp(-n d0^2/32) and integrate theta^(2m)exp(-n theta^2/32) over the real line. Dividing by G(c) bounds this tail by

    exp(-n^(1/5)/32)(32c)^(m+1/2)
      <=exp(5(m+1)-n^(1/5)/32).

The missing Gaussian tail in the central comparison satisfies the same bound, since c_plus>1/16. Adding the two tails proves (8). This argument takes absolute values only for controlled remainders, after deriving the exact signed contractions.

Finally eps<1/4 follows at log n=100 and persists: (log n+1)^2 n^(-3/5) decreases there, and n^(1/5)/32-5(log n+1) increases there. All constants are independent of m,n,b within the stated domain.

## Nonvanishing and the normalized logarithmic error

Equation (8) proves I_plus>0 and I_minus>0. Hence the ACTUAL denominator is nonzero, with

    sign D_n(L_m)=(-1)^m,
    |D_n(L_m)| >= (1-eps)4^m n! M^n
                      Gamma(m+1/2)/(2pi(n c_plus)^(m+1/2)). (9)

This is a lower bound for the contraction, not a ratio of two upper estimates.

Since c_plus/c_minus=chi/M=s, equation (5) gives

    F_n(L_m)/D_n(L_m)
      =(-1)^(n+1)4pi s^(n+m+1/2)
                         (1+delta_minus)/(1+delta_plus). (10)

Its multiplicative error from the displayed signed leading value is at most 2eps/(1-eps). In particular the logarithmic quotient has sign (-1)^(n+1).

The n^(-m) zero saving cancels exactly between numerator and denominator. But the curvature ratio supplies s^m. Therefore a blanket no-gain theorem for this selector would be false. Relative to m=0, the normalized logarithmic error gains s^m with relative error tending to zero uniformly in (6).

For example m=floor(kappa log n), 0<kappa<=1, gives the additional factor

    s^m=n^(-2kappa log(1+sqrt(2))) times a bounded factor.

The main exponential rate s^n is unchanged. This is a polynomial gain, not an additional exponential-in-n improvement.

## Complete exponential residual on the same denominator

The absolute coefficient sum of L_m at radius 1/R is

    sum_i |lambda_i|R^(-i)=(1+4/R+2/R^2)^(2m)=(2M)^(2m).

The established full exponential integral (3), estimated on |z|=R, gives

    |E_n(L_m)|<=9 M^n (2M)^(2m)/(n+1).

Use the nonzero denominator lower bound (9). Since eps<1/4,

    |E_n(L_m)/D_n(L_m)|<=Bexp,
    Bexp=24pi M^(2m)(n c_plus)^(m+1/2)
                  /[(n+1)n! Gamma(m+1/2)].             (11)

No initial term of the exponential tail has replaced its full integral. All selector-coefficient amplification appears explicitly in (11).

Combining (10)-(11) yields the complete signed additive enclosure

    |c_n(L_m)-(e+pi)
       -(-1)^(n+1)4pi s^(n+m+1/2)|
      <=4pi s^(n+m+1/2) 2eps/(1-eps)+Bexp.             (12)

Uniformly for m<=log n,

    log Bexp <= -n log n+O(n+(log n)^2),

using n!>=(n/e)^n and Gamma(m+1/2)>=1 for integer m>=0. Thus Bexp/s^(n+m+1/2) tends to zero uniformly. Equation (12) is a signed relative asymptotic for the COMPLETE quotient, not only its logarithmic part.

In particular, as n tends to infinity in (6), uniformly in m,

    c_n(L_m)-(e+pi)
      =(-1)^(n+1)4pi s^(n+m+1/2)(1+o(1)).             (13)

The explicit additive enclosure (12), rather than an unspecified effective threshold for the final sign, is the finite-index statement.

## Budget and arithmetic scope

If a b-window is required, the precise selector budget is 4m<b. For m=floor(kappa log n) one may choose b=4m+1. This is compatible eventually with n>=512b^4 log n, although the direct contraction argument needs no Toeplitz inverse or normality theorem. Both parity classes of n are allowed.

The coefficients of L_m are integers, and D_n(L_m) is an actual nonzero rational contraction. Thus c_n(L_m) is a well-defined rational number. Reduction of its numerator and denominator must still be performed before making any assertion about an integer approximation form. The size of D_n(L_m), selector coefficient norms, and a common forcing clearer are not its reduced denominator q.

The gain proved here concerns the actual rational approximation error |c_n(L_m)-(e+pi)|. It does not prove that q times this error tends to zero, or establish an irrationality result. No coefficient clearer is substituted for q, and no statement is made about a reconstructed endpoint lattice for these direct selectors.

A different selector is not needed to obtain the polynomial gain above. This result does not optimize rational selectors, nor exclude stronger gains from other choices. The curvature calculation specifically explains why the conjugate zero cancels the n-power saving but does not cancel every normalized gain.

No previous author result was audited or replayed. RATIONAL_SADDLE_SELECTOR_WORKING.md is preserved as the initial reduction. This note and RATIONAL_SADDLE_SELECTOR_REPORT.md require read-back before reporting completion.
