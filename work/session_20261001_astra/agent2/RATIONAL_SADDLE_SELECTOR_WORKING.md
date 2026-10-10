> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rational saddle selector: initial exact reduction

New author research; incomplete uniform estimates. Existing reconstruction results are preserved. No numerical checks are requested or claimed.

Put R=sqrt(2), M=1+R, chi=R-1, and V(t)=t^2-t+1/2. Let L_m(t)=(2t^2-4t+1)^(2m), with m a nonnegative integer and 4m<b when using a b-entry forcing window.

The polynomial coefficient identity for the positive forcing gives, for any polynomial L,

    D_n(L)=sum_i lambda_i fP_i=D_t^n[V(t)^n L(t)] evaluated at t=1.

Indeed expansion of V(t)^n=t^(2n)Q0(1/t) gives exactly the factorial coefficient expression for each fP_i. Cauchy's derivative formula on t=1+exp(i theta)/sqrt(2) therefore yields

    D_n(L)=n!/(2pi) integral_-pi^pi
       (1+sqrt(2)cos theta)^n L(1+exp(i theta)/sqrt(2)) dtheta.

This is the complete positive-forcing contraction, although the contracted integrand need not be positive.

The previously derived arbitrary-polynomial logarithmic arc identity gives

    E_F,n(L)=sum_i lambda_i eF_i
      =(-1)^(n+1)2n! integral_-pi/4^pi/4
        (sqrt(2)cos theta-1)^n
        L(1-exp(i theta)/sqrt(2)) dtheta.

For the specified selector BOTH polynomial factors equal

    (exp(2i theta)-1)^(2m)
      =(-4)^m sin(theta)^(2m) exp(2mi theta).

Conjugation symmetry therefore gives the exact real formulas

    D_n(L_m)=(-4)^m n!/(2pi) integral_-pi^pi
       (1+sqrt(2)cos theta)^n sin(theta)^(2m) cos(2m theta) dtheta,

    E_F,n(L_m)=(-1)^(n+1)(-4)^m 2n! integral_-pi/4^pi/4
       (sqrt(2)cos theta-1)^n sin(theta)^(2m) cos(2m theta) dtheta.

No denominator nonvanishing has yet been established in this working note. No quotient estimate is asserted here.

The complete exponential residual remains

    E_E,n(L)=-integral_0^1 s^n exp(1-s)
       sum_i lambda_i [z^(n+i)]Q0(z)^n exp(sz) ds.

Only on D_n(L)!=0 is the rational selector quotient defined, and then exactly

    c_n(L)-(e+pi)=[E_F,n(L)+E_E,n(L)]/D_n(L).

There is no reconstructed endpoint constant in this direct forcing quotient. The complete exponential residual must nevertheless remain.

The local Gaussian curvatures at theta=0 are

    c_plus=sqrt(2)/(2(1+sqrt(2))),
    c_minus=sqrt(2)/(2(sqrt(2)-1)).

Both integrals have a Gaussian moment of order 2m. Their n^(-m) factors are expected to cancel after normalization, but their curvature factors differ. A uniform proof must retain the ratio (c_plus/c_minus)^(m+1/2), rather than declaring no gain merely because both saddles vanish. Needed next: uniform relative remainder estimates for growing m, a signed nonzero lower bound for D_n(L_m), and a complete exponential-residual budget on that same denominator.
