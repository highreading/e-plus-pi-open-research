> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Uniform base-polynomial asymptotics from its exact differential equation

Date: 2026-09-13. Original continuation by root. Independent review requested.
This note derives an explicit analytic phase and transport factor without
assuming an asymptotic theorem for a different varying weight.

Write f_m(w)=Phi_m^*(w), with the explicit circular-binomial polynomial
from raw_circular_binomial_prediction_bounds.md. Its coefficient formula
is equivalently the terminating hypergeometric polynomial

    f_m(w)=sum_(j=0)^m (-m)_j(m)_j/[(-2m)_j j!] w^j.

No singular lower parameter is used beyond this finite sum. Direct
coefficient comparison gives the exact equation

    w(1-w)f_m''+(-2m-w)f_m'+m^2 f_m=0,
    f_m(0)=1,       f_m'(0)=m/2.                         (1)

All zeros of f_m are outside the closed unit disk by the earlier
positive-measure extremal proof. Set A=w(1-w), Delta=1-w+w^2, and
let S=sqrt(Delta) be the analytic branch on |w|<1 with S(0)=1.
The two zeros of Delta lie on the unit circle. Define

    r(w)=1/(1+S(w)),
    h(w)=[A(w)r'(w)-w r(w)]/[2S(w)],
    L(w)=integral_0^w r(t)dt,       H(w)=integral_0^w h(t)dt.

These functions are analytic throughout the disk. In particular 1+S
cannot vanish there: S=-1 would imply w(w-1)=0, and S(0)=1.

For each fixed compact subset of the open unit disk,

    f_m(w)=exp(mL(w)+H(w)) [1+O(1/m)]                    (2)

uniformly. All derivatives also have the corresponding local expansions.
The error constant may depend on the compact set, not on m.

## Proof, including uniformity and the transport term

Let r_m=f_m'/(m f_m). The reciprocal root representation gives
|r_m(w)|<=1/(1-|w|), uniformly in m. Thus the family and its
derivatives are locally bounded and it is a normal family. Dividing
(1) by m^2 f_m gives

    A(r_m^2+r_m'/m)-(2+w/m)r_m+1=0.                     (3)

Every locally uniform subsequential limit satisfies Ar_*^2-2r_*+1=0
and r_*(0)=1/2. The latter fixes the branch r_*=r near zero, and
analytic continuation fixes it on the disk. Every subsequence has
the same limit, so r_m->r locally uniformly.

Subtract the limiting equation from (3). For delta_m=r_m-r,

    [A(r_m+r)-2]delta_m=(w r_m-A r_m')/m.                (4)

The bracket converges locally uniformly to -2S, which is bounded
away from zero on every compact subdisk. The right numerator is
uniformly bounded there by the root estimate and Cauchy's derivative
bound on a slightly larger disk. Therefore delta_m=O(1/m), and
Cauchy's estimate also gives delta_m'=O(1/m) on smaller compact sets.

Putting delta_m=h/m+eta_m into (4), or comparing the terms of order
1/m in (3), gives

    -2S h=w r-A r'.

The same bounded-denominator argument, now using delta_m and its
derivative bounds, gives eta_m=O(1/m^2) locally uniformly. Hence

    f_m'/f_m=m r+h+O(1/m).

The logarithm normalized by log f_m(0)=0 exists on the disk.
Integration along line segments gives log f_m=mL+H+O(1/m), and
exponentiation proves (2). No limiting zero distribution or unproved
normality of the actual Hermite--Pade family was used.

## Transfer to the actual even polynomial and its reversal

The independently reviewed Hardy theorem gives, for n=2m,

    v(z)/v0 = F_m(z) R_n(z),       F_m(z)=f_m(-z^2),
    ||R_n||_(H2)<=e sec(1),       R_n(0)=1.

It also bounds log R_n on every compact disk of radius below cos(1).
Consequently, with the logarithm normalized at zero,

    (1/n)log(v(z)/v0) -> Phi(z)=(1/2)L(-z^2),
    Phi'(z)=-z/[1+sqrt(1+z^2+z^4)]                       (5)

locally uniformly on |z|<cos(1). The sharper multiplicative identity

    v(z)/v0=exp(nPhi(z)+H(-z^2)) R_n(z)[1+O(1/n)]         (6)

holds on every compact subdisk of |z|<1, without dividing by R_n
or asserting it is nonzero there. The relative error in (6) belongs
only to the explicitly known base factor.

The reversal continuation supplies the same Hardy norm bound for
Rtilde_n(z)=v*(z)/(v0 F_m(z)), where v*=z^n v(1/z) uses formal
degree n even if v has a defect. Thus for compact subsets of |z|>1,

    v(z)/v0=z^n exp[(n/2)L(-1/z^2)+H(-1/z^2)]
                 Rtilde_n(1/z)[1+O(1/n)].                (7)

No nonzero value or lower bound for Rtilde_n at a proposed saddle
is inferred from its upper Hardy norm.

## The two algebraic saddle candidates and the homology issue

For the arctangent kernel D(z)^n v(z)/[z^(2n+1)(z-1)^(n+1)],
the interior phase has derivative

    H_in'=2z/D-2/z-1/(z-1)-z/(1+sqrt(1+z^2+z^4)).

Writing P=z^3+3z-2, its rational first three terms equal
-P/[zD(z-1)]. Squaring the equation H_in'=0 and clearing
denominators yields

    z^2 D(z-1)^2+2P(z-1)-P^2
      =-2zD(z^2+z-1)=0.                                 (8)

Away from the excluded poles and zeros, the candidates are
(sqrt(5)-1)/2 and -(sqrt(5)+1)/2. Substitution, not just the squared
equation, is necessary. The positive candidate is an interior-branch
stationary point. The negative candidate is not one for that branch.
Moving the left contour through the positive candidate crosses the
pole at zero unless an additional residue is retained.

For the exterior reversal phase, differentiation instead gives

    H_out'=2z/D-1/z-1/(z-1)
             +1/[z^3(1+sqrt(1+z^(-2)+z^(-4)))].

Direct substitution shows H_out'(-phi)=0, phi=(1+sqrt(5))/2.
This point is on the left exterior side and is compatible with a
possible outward deformation. Its unknown multiplier is
Rtilde_n(-1/phi), at modulus 1/phi>cos(1). The available zero-free
disk does not cover it. A valid steepest contour, endpoint estimates,
and control of this actual multiplier are still required before a
signed asymptotic formula can be claimed. Equations (5)--(8) alone
are not an estimate for Ra or for the primitive integer form.
