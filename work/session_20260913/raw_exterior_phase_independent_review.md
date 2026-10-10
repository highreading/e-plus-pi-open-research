> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the exterior phase maximum certificate

Date: 2026-09-13. Reviewer: audit_computations.
Status: PASS, including an independent rerun and exact coverage check.

Reviewed files:
raw_exterior_phase_strict_maximum.md,
check_exterior_phase_monotonicity.py,
exterior_phase_monotonicity_certificate.json.

The verifier was rerun unchanged with /opt/homebrew/bin/python3.13.
It completed successfully at 60-digit outward interval precision, with
128 accepted proof boxes and no canonical degree calculation. Its
SHA256 at review was

    58bd43b580d9f60ab61d5be487a64779e64f56d3eb8109230b354e75d7ec41f6

## 1. Derivatives and orientation

For z(u)=-1/2-(sqrt(5)/2)cos u+i(sqrt(5)/2)sin u, direct
differentiation gives z'=-i(z+1/2), z''=-(z+1/2), exactly as
implemented. The curve runs from the saddle toward the upper
endpoint as u increases.

With w=-z^(-2), one has w'=2z^(-3). Differentiating
r=1/(1+sqrt(1-w+w^2)) gives

    r'=(1-2w)/[2sqrt(1-w+w^2)(1+sqrt(1-w+w^2))^2].

The derivative of r(w)/z^3 is consequently
2r'(w)/z^6-3r(w)/z^4. This verifies the two displayed phase
derivatives, including the sign and factor two of the last term.
The formulas G'=Re(H'z') and G''=Re(H''(z')^2+H'z'') then
follow by the chain rule. The code evaluates precisely these
formulas and does not differentiate sampled values.

## 2. Square-root sheet and interval evaluation

On the retained curve a=-Re z is positive, and |z|^2=1+a>1,
so |w|<1. If w=x+iy, the imaginary part of Delta=1-w+w^2 is
y(2x-1). At y=0 its real part is positive. At x=1/2 its real
part is 3/4-y^2>0 in the open disk. Thus Delta never meets the
nonpositive real axis there. The positive-real square root in
the code is exactly the analytic branch normalized at zero.

The implementation encloses this root by computing its positive
real part from (|Delta|+Re Delta)/2, and then its imaginary part
as Im Delta divided by twice that real part. An interval box is
accepted only if that denominator has a strictly positive lower
bound. Failure triggers subdivision, not a branch choice.

All initial endpoints are Fraction rationals, converted through
integer numerators and denominators into outward intervals. The
trigonometric, square-root, complex-arithmetic, and division
operations are mpmath interval operations. Wider rectangular
enclosures can lose correlations, but cannot falsely sharpen a
bound. Every sign decision compares an enclosing upper endpoint
with an enclosing lower endpoint of the exact rational threshold.
No ordinary floating-point approximation is used for those decisions.

## 3. Complete interval coverage and endpoint overlap

The independent rerun certified one second-derivative box covering
[0,1/100] and 127 first-derivative boxes covering
[1/100,1913/1000]. I independently parsed all leaf endpoints as
exact Fractions and checked their ordering, positive widths,
pairwise adjacency, and both terminal endpoints. There are no
gaps or overlapping intervals being used to hide an uncovered point.
The depth limit is an explicit failure condition, never an
acceptance rule.

The output again encloses the final a value in

    [0.12482826182419082943827939977029887126130426052306029087538080652,
     0.12482826182419082943827939977029887126130426052306029087538111767].

It proves 0<a<1/8 by strict interval comparisons. Since sin u>0
on this angular interval, a decreases with u; hence the entire
certified interval is in the exterior disk. The remaining curve
to the endpoint has a<=1/8 and is covered by the separately
proved endpoint estimate. There is a genuine overlap.

## 4. Strict maximum and its precise consequence

The exact saddle identity gives G'(0)=0. The certified inequality
G''<-1/10 on [0,1/100] gives G'(u)<0 for 0<u<=1/100.
The first-derivative boxes prove strict negativity thereafter.
Reflection treats the lower arc. Thus the middle arc has its
unique maximum at the saddle, and compactness supplies a positive
phase gap outside any fixed saddle neighborhood.

This proves input P in raw_even_dual_saddle_assembly.md. It is
a rigorous interval proof for one fixed analytic curve, not a
statistical or asymptotic inference from finite canonical data.
The actual multiplier and the varying-amplitude saddle argument
remain separate inputs, as the target correctly states.

No correction was required.
