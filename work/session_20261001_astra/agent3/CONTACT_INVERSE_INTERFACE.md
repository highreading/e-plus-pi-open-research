> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Endpoint-lift interface for the remainder analysis

Status: working derivation for the new quantitative task. Contact normality and its exact reduction remain explicitly provisional pending Child 4's examination. This is not an independent audit or a replay of that proof. The completed certificates are preserved.

Let N=2n+b, q(z)=1-z+z^2/2, G_n(z)=exp(z)q(z)^n, and T_ij=[z^(n+i-j)]G_n for 0<=i,j<b. Endpoint data are denoted (P,Q); the quadratic q(z) is a separate object.

Write the actual triple as

    A=P+(z-1)a, B=Q+(z-1)d, C=Q+(z-1)c,
    deg a,c<n, deg d<b.

Then its contact condition is precisely

    a+exp(z)d+F(z)c = h_(P,Q)(z) mod z^N,
    h_(P,Q)=[P+Q(exp(z)+F(z))]/(1-z).

Define the TWO forcing columns, without dropping their scales, by

    f^P_i=[z^(n+i)]q(z)^n D^n[1/(1-z)],
    f^Q_i=[z^(n+i)]q(z)^n D^n[(exp(z)+F(z))/(1-z)].

With dtilde=(D+1)^n d, the exact reduced solve is

    T dtilde = P f^P + Q f^Q.

Both columns are rational. In particular

    f^P_i=n! 2^(-n) sum_(l=0)^floor(n/2)
                    binom(n,l) binom(2n+i-2l,n+i).

For either forcing column, if h_m are the Taylor coefficients of its h, an entirely rational construction is

    f_i=sum_(s=0)^min(2n,n+i) [z^s]q^n
             * (2n+i-s)!/(n+i-s)! * h_(2n+i-s).

Here h^P_m=1 and h^Q_m=sum_(j=0)^m(1/j!+[z^j]F). All factorial arguments are nonnegative.

After the solve, reconstruction is

    d=(D+1)^(-n)dtilde
      =sum_(l=0)^(b-1)(-1)^l binom(n+l-1,l) D^l dtilde,
    p=T_<n(q^n D^n h-G_n dtilde),
    c=U_n^(-1)p, where U_n(c)=q^n D^n(cF),
    a=T_<n(h-exp(z)d-Fc).

These formulas preserve the endpoints exactly. The forthcoming research note will also reconstruct C through the actual moment projection, giving explicit coefficient bounds without leaving U_n^(-1) inside a norm estimate.

For a useful real-direction decomposition put S=exp(1)+pi. Although the lift and both forcing columns are rational, its analysis can use

    f^Q=S f^P+e_F+e_E.

The residuals have exact analytic representations

    q^n D^n[(exp(z)-exp(1))/(1-z)]
      =-q^n integral_0^1 t^n exp(1-t)exp(tz) dt,

    q^n D^n[(F(z)-pi)/(1-z)]
      =-n! integral_-1^1 [t q(z)/(1-tz)]^n
                              /[(1-t)(1-tz)] du,
    t=(1+iu)/2.

They retain the complete functions and both conjugate endpoints of the segment.

The planned scaled norm uses r=sqrt(2), D_r=diag((-r)^j), j=0,...,b-1. Its squared coefficient weights are the rational numbers 2^j. Set M=1+r, d0=b-1, and

    C_int=(16 b^2 n)^d0 binom(2d0,d0)/(d0!)^2,
    K0=2048 b sqrt(n) C_int.

The new quantitative target being written out is

    ||D_r T^(-1) f||_2 <= K0 M^(-n)||D_r f||_2

throughout n>=16, 2<=b<=n, n>=512 b^4 log n. Its proof uses a one-variable accretivity estimate and polynomial interpolation on separated short intervals, rather than the earlier determinant lower bound or a Neumann series.

The forcing estimates to accompany it are

    n! 2^n/(2n+1) <= ||D_r f^P||_2
                       <= n! sqrt(b) M^(n+b),
    ||D_r e_F||_2 <=16 sqrt(b) r^(b-1)n!(3/2)^n,
    ||D_r e_E||_2 <=27 sqrt(b) M^n/(n+1).

These are intended to yield a rank-one approximation for the actual lift after reconstruction, with leading endpoint covector (1,S), not merely an inverse bound for a rescaled matrix. The detailed proof and constants belong in CONTACT_INVERSE_RESEARCH.md.

Remainder interface: if beta_j are the coefficients of the reconstructed ACTUAL B polynomial, then beta_0=Q-d_0, beta_j=d_(j-1)-d_j for 1<=j<b, and beta_b=d_(b-1). They satisfy precisely the relaxed high annihilations l=1,...,b-2. The complete evaluated remainder is

    R(1)=ell_beta(W_n)=P+Q S.

Thus every multi-row subtraction proved by Child 2 can be applied directly to beta. In particular, if

    p_(n+1)/(1-t)-sum_l c_l p_(n+l)=t^m J(t)/(1-t)

uses retained high rows, then

    R(1)=Q v_(n+1)/p_(n+1)(1)
            +ell_beta(t^m J/(1-t))/p_(n+1)(1).

The common n in ell_j and every factorial must remain unchanged. Minimal integral lifting multipliers cancel against the final endpoint gcd; they provide no additional saving.

A planned positive rational full-coefficient norm uses ordinary Euclidean B coefficients and scales A,C by explicit reconstruction bounds. It will make the full triple norm comparable to the B coefficient norm, so that Child 2's complete functional estimate transfers without an uncontrolled reconstruction factor. The rational center of its pulled-back Gram matrix will be retained exactly; no reduced-denominator estimate is inferred from its magnitude.
