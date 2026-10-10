> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The exterior golden saddle, its exact residue alternative, and controlled endpoint tails

Date: 2026-09-13. Original continuation by audit_computations.
Independent review: PASS by audit_sources; see raw_exterior_saddle_endpoint_independent_review.md. The scope is the actual even family n=2m.
No canonical degree or root scan is used.

This note locates the relevant saddle on the correct sheet, computes
its exact curvature and exponential scale, constructs a residue-free
exterior contour through it, and bounds that contour's endpoint tails.
It does NOT claim the complete saddle asymptotic. The remaining
middle-contour maximum and actual multiplier are explicitly separated.

## 1. Retained normalization and the two phases

Write D=1+z^2, v=q/(n!V(1)), v_0=v(0), and

    u_n=n!V(1)v_0,
    Ra(1)/u_n=(1/(2i)) integral_(gamma_L)
       D(z)^n[v(z)/v_0]/[z^(2n+1)(z-1)^(n+1)] dz.        (1)

The coefficient u_n is the nonzero leading coefficient of the actual
integer polynomial U. The path gamma_L runs clockwise from -i to i
through the left half-plane. It can be deformed there without crossing
the poles 0 or 1.

The reviewed base asymptotic uses

    f_m(w)=Phi_m^*(w),
    f_m(w)=exp(m L(w)+H(w))[1+O(1/m)],
    L'(w)=1/[1+sqrt(1-w+w^2)],

uniformly on compact subdisks of |w|<1. The square root has value one
at zero. Formal degree-n reversal gives the exact multiplier

    Rtilde_n(u)=v^*(u)/[v_0 f_m(-u^2)],
    ||Rtilde_n||_(H^2)<=C_*=e sec(1).

On compact subsets of |z|>1,

    v(z)/v_0=z^n exp[(n/2)L(-1/z^2)+H(-1/z^2)]
                     Rtilde_n(1/z)[1+O(1/n)].             (2)

The relative error in (2) belongs only to the known base factor.
It remains valid when the multiplier is zero.

In a neighborhood of the negative real axis define the real-normalized
exterior phase

    mathcal H(z)=log D(z)-log(-z)-log(1-z)
                                      +(1/2)L(-1/z^2).    (3)

Because n is even, these logarithms reproduce exactly the nth-power
factor in (1). Its derivative is

    mathcal H'(z)=2z/D-1/z-1/(z-1)
        +1/[z^3(1+sqrt(1+z^(-2)+z^(-4)))].               (4)

The interior formula instead has -2/z and the derivative of
(1/2)L(-z^2). It must not be used at an exterior stationary point.

## 2. A closed primitive and exact saddle constants

For |w|<1 set

    chi(w)=1/[1-w+sqrt(1-w+w^2)].

This is analytic, chi(0)=1/2, and satisfies

    w=(2chi-1)/[chi(2-chi)].

Differentiating this relation, or substituting directly, gives

    L(w)=log[(27/4)chi(w)/((2-chi(w))(1+chi(w))^2)].        (5)

The logarithm is the branch with value zero at w=0. To check the
integral, change variable from w to chi; its differential becomes

    L'(w)dw=[1/chi-1/(chi-2)-2/(chi+1)]dchi.

The factors inside the logarithm do not vanish or have poles in
the disk; the expression is continued analytically from zero.

Let

    rho=(sqrt(5)-1)/2,       phi=1/rho=(sqrt(5)+1)/2.

Substitution in (4), using rho^2+rho=1, proves

    mathcal H'(-phi)=0,
    mathcal H''(-phi)=(25-11sqrt(5))/4>0.                 (6)

For the second identity one can differentiate (4) before substituting
sqrt(1+rho^2+rho^4)=2rho; the resulting rational expression reduces
modulo rho^2+rho-1 to 7/2-11rho/2. Positivity follows from
25^2>121*5.

At w=-rho^2, chi(w)=rho^2. Formula (5) and the rational prefactor
in (3) then simplify exactly to

    exp[2 mathcal H(-phi)]=27rho^5/4,
    tau:=exp[mathcal H(-phi)]=(3sqrt(3)/2)rho^(5/2)<1.      (7)

The phase is real at this point. Its positive second derivative
means that a vertical tangent is locally a direction of decay of
its real part, rather than a direction of growth.

## 3. Why the positive saddle is in a different contour class

Squaring the interior stationary equation produces the candidates
rho and -phi. Direct substitution retains rho on the interior
sheet; -phi is extraneous for that sheet. The point rho lies to
the right of the pole at zero. Moving the left path there without
an explicit residue would change the actual arctangent error.

The residue can be identified exactly. Let

    I(z)=D(z)^n v(z)/[z^(2n+1)(z-1)^(n+1)],
    Z=Qhat(1).

Then, for even n,

    Res_(z=0) I(z)=-Z/(n!V(1)).                           (8)

Here is a coefficient proof retaining the original factorials.
Put S(t)=(1+t^2)^n U(t). The already proved dual reconstruction
gives T=S^(n) and Qhat(1)=T(1)/n!. Also

    D(z)^n v(z)=z^(3n)S(1/z)/(n!V(1)).

Since n+1 is odd, the residue is minus the coefficient of z^(2n)
in D^n v(1-z)^(-n-1). Thus it is

    -1/(n!V(1)) sum_(k=n)^(3n) [t^k]S binom(k,n)
       =-T(1)/[(n!)^2V(1)]
       =-Z/(n!V(1)),

as claimed. This proof distinguishes S from the inverse-Borel
polynomial and does not repeat the earlier false identification
of their derivatives.

If gamma_R is a right path from -i to i, lying to the left of 1,
whose difference from gamma_L winds once counterclockwise around
zero, define I_R=n!V(1)/(2i) integral_(gamma_R) I(z)dz.
The residue theorem gives the exact relation

    Ra(1)=I_R+pi Z.                                      (9)

Thus an interior saddle analysis of I_R would still require the
explicit cancellation of this residue term. It is not an analysis
of the original left integral with the same value.

## 4. A residue-free contour through the exterior saddle

Take the LEFT arc Gamma of

    |z+1/2|=sqrt(5)/2

from -i to i. It passes through -phi and has a vertical tangent
there, oriented upward. Everywhere on this arc

    |z|^2=1-Re z>=1,

with equality only at the endpoints. Its interior lies strictly
in the exterior disk. The region between it and the original
left unit semicircle is contained in the left half-plane and
contains neither pole 0 nor pole 1. Cauchy's theorem therefore
replaces gamma_L by Gamma in (1) with no residue.

Write a=-Re z. On either endpoint portion of the arc,

    |z|^2=1+a,
    |D(z)|=sqrt(5)a,
    |z-1|^2=2+3a,
    (Im z)^2=1+a-a^2.                                   (10)

The upper half is z(a)=-a+i sqrt(1+a-a^2), 0<=a<=phi;
the lower half is its conjugate. These identities provide explicit
control at the two endpoints even though the compact base asymptotic
does not apply there.

## 5. Uniform endpoint-tail bound without a saddle multiplier lower bound

The base root exclusion gives

    |f_m(-1/z^2)|<=[1+1/|z|^2]^m.

Hardy evaluation gives on Gamma away from its endpoints

    |Rtilde_n(1/z)|<=C_* sqrt((1+a)/a).

Combining these inequalities with the exact reversal identity in
(1), the nth-power part of the integrand is at most

    [sqrt(5)a sqrt(2+a)/((1+a)sqrt(2+3a))]^n
       <=(sqrt(5)a)^n.                                  (11)

The remaining rational factor 1/[z(z-1)] has modulus at most
1/sqrt(2). For 0<=a<=delta=1/8 the arclength derivative is at
most two, since |d(Im z)/da|<=1/2 there. Integrating the two
endpoint pieces in absolute value therefore proves the safe bound

    |(Ra/u_n)_(endpoint pieces)|
       <=4 C_* sqrt(delta)/(n+1/2) (sqrt(5)delta)^n.        (12)

In particular the exponential base sqrt(5)/8 is strictly smaller
than tau in (7). This is an unconditional estimate of these parts
of the actual signed contour. It does not rely on a nonzero saddle
value or a guessed limiting root distribution.

## 6. The precise middle-contour question

For a in [delta,phi], the compact exterior base asymptotic is
uniform, as are all Hardy bounds for the multiplier and its
derivatives near the saddle. The real phase on the upper arc is
an explicit algebraic function. With z=z(a), w=-1/z^2, and chi
as in (5), set

    E(a)=exp[2 Re mathcal H(z(a))]
       =5a^2/[(1+a)(2+3a)]
          * (27/4)|chi(w)|/[|2-chi(w)| |1+chi(w)|^2].      (13)

At a=phi it equals tau^2. The exact remaining contour inequality
for this particular candidate arc is

    E(a)<tau^2 for delta<=a<phi.                         (14)

It has NOT been proved here. The nonzero local curvature (6)
proves the strict inequality locally near phi along the arc, but
does not by itself prove it on the whole middle arc. Formula
(13) reduces that question to a specific one-variable algebraic
inequality, with all branches specified. No numerical sampling
of (13) is substituted for a proof of (14).

If (14) holds, compactness supplies a strict phase gap away from
the saddle, while (6) controls a neighborhood of it. Together
with (12), this would already give an upper estimate of order
tau^n/sqrt(n) for |Ra/u_n|, using only the upper Hardy bound.

To obtain a signed leading term one additionally needs information
on the ACTUAL multiplier Rtilde_n(-rho). For example, if it tends
to a nonzero real number A, and a valid steepest-descent deformation
has the stated single maximum, the local Gaussian calculation gives

    Ra(1)/u_n ~ [rho^3 exp(H(-rho^2))/2]
                sqrt(2pi/mathcal H''(-phi))
                A tau^n/sqrt(n).                        (15)

The orientation and the factor 1/2 in (15) come from dz=i dy
at the upward vertical tangent and the original prefactor 1/(2i).
Its rational denominator is z(z-1)=phi^3 at the saddle. This is
a conditional formula, not a proved asymptotic for the actual family.

The existing zero-free disk for v does not apply to the reversal
multiplier at -rho, and rho>cos(1). A bound on its Hardy norm
supplies an upper bound and bounded derivatives, but no nonzero
lower bound. The at-most-two-negative-real-roots theorem likewise
does not exclude a root near this specific point or exponentially
small values there. Neither (14) nor the amplitude condition is
silently imported from the base polynomial.

## 7. Relation to the main arithmetic target

All formulas here use u_n=(2n)![t^n]V_n. An exponential estimate
relative to u_n is not an estimate relative to an integer of bounded
height. The original connection scalar is still

    a_n=(2n+1)! Ra(1)/(n!V(1)),

and the combined primitive form is

    sign(Z)[Re(1)+4Ra(1)]/g,
    g=gcd(|Z|,|Pe(1)+4Pa(1)|).

The new exact achievements are the correct exterior phase constants,
the quantified residue alternative, the admissible exterior arc,
and the negligible endpoint tails. They leave a concrete global
phase inequality and an actual scalar connection estimate before
even the unreduced signed arctangent asymptotic is established.
