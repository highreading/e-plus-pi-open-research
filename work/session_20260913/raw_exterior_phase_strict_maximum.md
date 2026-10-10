> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A certified strict maximum for the actual exterior reference phase

Date: 2026-09-13. Original continuation by root. Independent review requested.
This is a rigorous one-variable interval certificate, not a sampled
numerical maximum or a computation of additional canonical degrees.

Let phi=(1+sqrt(5))/2, R=sqrt(5)/2, and parameterize the upper
half of the exterior contour by

    z(u)=-1/2-R cos(u)+i R sin(u),
    0<=u<=u_end=arccos(-1/sqrt(5)).

It runs from -phi to i. Define

    G(u)=Re H_out(z(u)),
    H_out=log(1+z^2)-log z-log(z-1)+(1/2)L(-1/z^2),

where the real part is independent of logarithm choices and L is the
analytic primitive in raw_base_polynomial_uniform_asymptotic.md.

The certificate proves

    G''(u)<-1/10       for 0<=u<=1/100,
    G'(u)<0           for 1/100<=u<=1913/1000.             (1)

The exact saddle identity gives G'(0)=0. Hence G is strictly
decreasing on this whole middle interval away from zero. Moreover

    0<-Re z(1913/1000)<1/8.                              (2)

The endpoint estimate already proved for a=-Re z<=1/8 therefore
covers the rest of this contour, with an overlap. Reflection gives
the corresponding result on the lower half. In particular, outside
any fixed neighborhood of -phi in the retained middle contour, the
real phase has a strictly positive gap below its saddle value.

## Exact derivative formulas and branches

Put D=1+z^2, w=-1/z^2, S=sqrt(1-w+w^2), and r=1/(1+S). Then

    H_out'=2z/D-1/z-1/(z-1)+r/z^3,
    H_out''=2(1-z^2)/D^2+1/z^2+1/(z-1)^2
               -3r/z^4+2r'(w)/z^6,
    r'(w)=(1-2w)/[2S(1+S)^2],
    z'=-i(z+1/2),       z''=-(z+1/2).

Thus G'=Re(H_out'z') and G''=Re(H_out''(z')^2+H_out'z'').
These are the formulas evaluated by the verifier.

For |w|<1, Delta=1-w+w^2 never meets the nonpositive real axis.
Indeed if w=x+iy, Im Delta=y(2x-1). When y=0 its real value is
strictly positive. When x=1/2 it is 3/4-y^2>0 because |w|<1.
Therefore the square root with positive real part is the same analytic
branch as the one equal to one at zero. The contour's retained part
has |z|>1, as follows from |z|^2=1-Re z and (2).

The verifier evaluates the square root by

    s_re=sqrt((sqrt((Re Delta)^2+(Im Delta)^2)+Re Delta)/2),
    s_im=Im Delta/(2s_re),

requiring a strictly positive interval lower bound for s_re. A box
that cannot verify that condition is bisected; no branch is guessed.

## Finite reproducible certificate

The executable check_exterior_phase_monotonicity.py uses 60-digit
outward interval arithmetic. Inputs and subdivision endpoints are
exact rational numbers, enclosed from their integer numerators and
denominators. It recursively bisects rational intervals until the
entire derivative enclosure has the sign required in (1).

The run completed with 128 certified leaves. Their exact endpoints
and full enclosures are saved in exterior_phase_monotonicity_certificate.json.
The leaves cover [0,1/100] for the second derivative and
[1/100,1913/1000] for the first derivative without gaps. Adaptive
subdivision selects proof boxes, not sample points. Each accepted
box establishes the inequality at every point of that interval.

The same outward arithmetic proves (2), more narrowly

    0.12482826182419 < -Re z(1913/1000) < 0.12482826182420.

Only the rational inequality (2) is needed. A repeated run either
proves every box or fails; a maximum depth is an explicit failure
condition, not permission to accept an unresolved box.

Together with the independent endpoint bound, this closes the
middle-contour phase question. It still requires the actual multiplier
limit and a uniform local saddle argument to obtain a signed Ra
asymptotic. The endpoint gcd remains separate from both analytic steps.
