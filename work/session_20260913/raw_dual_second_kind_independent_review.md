> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent root audit of the arctangent second-kind reduction

Date: 2026-09-13. Verdict: PASS.

I independently checked raw_dual_arctangent_toeplitz_second_kind.md.
The finite exterior Cauchy expansion uses moments only through 2n
and has the stated factorials. The divided-difference test has degree
at most n-1. On the unit circle U(z)=z^n conjugate(q(z)), giving
the product identity with U(s), rather than q(s). This distinction
is correct and essential.

The real-part formula for e^z/(a+z) has a positive numerator when
a>1. The strengthened ratio lower bound follows from
(a-1)(1-cos(theta))>=0. Pairing conjugate points makes the integral
real, and the rational C_q has no pole at -1. Therefore the endpoint
limit in the proof is legitimate without a principal-value claim.
The substitutions into the product bound give precisely
v(x)B(x)>=v(0)/(1-x); all factors and signs are correct.

I independently inverted the Rodrigues integral. Its minus from
dt=-dz/z^2 cancels the reversal of the image path. The left unit
semicircle from -i through -1 to i is clockwise. Its parametrization
therefore gives the minus one-half in equation (14). The deforming
region excludes both poles 0 and 1. Differentiation with respect to
a gives positive n!/(z-a)^(n+1), so the nth-derivative normalization
and the dimensionless scalar are correct.

The finite Laurent block uses the actual Toeplitz coefficient
conditions. Its positive-power remainder is entire, but its incomplete
contour integral is not controlled by those conditions. The note
correctly retains that contribution and does not replace an incomplete
circle by the full exterior Cauchy function.

The complete combined-error bracket has the same n!V(1)/(2n+1)!
factor as the independently reviewed exponential estimate. The fixed
endpoint gcd is still present. The negative-real sign theorem alone
does not supply a sign for the partial-circle scalar a_n.

I checked the frozen n=2 coefficients directly: the first three
nonzero C_q coefficients are 1850,204,1176, and normalization by
1850 gives the stated B. The U/q reversals and the arctangent
endpoint 4108*pi-12852 agree with the previously saved actual
simultaneous numerators. No correction was needed.

