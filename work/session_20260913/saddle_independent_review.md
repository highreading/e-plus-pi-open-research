> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the new saddle checker and the fixed-circle proof

Date: 2026-09-13. Reviewer: audit_results subagent.

Reviewed `check_saddle_independent.py` in full, its saved result JSON, the
defining formulas in `sources/mixed_cubic_accessible_saddle_exact_algebraic_certificate.md`,
and Sections2-5 of
`sources/mixed_cubic_fixed_circle_complex_laplace_theorem.md`.
I did not run an archived certificate or use its program as the arithmetic
implementation. This was an independent code and mathematical review of
root's new checker, including a direct derivation of the angular numerator.

**Verdict:** no serious arithmetic-containment or asymptotic hypothesis gap
was found. The new checker provides exact algebraic and sign evidence for
the fixed-circle saddle theorem. The existing complex-Laplace argument
then proves eventual nonvanishing at every sufficiently large m, subject
to its separately stated coefficient-integral and determinant identities.
This review does not certify the remaining arithmetic gain needed for
irrationality of e+pi.

## 1. Outward dyadic intervals

Let S=2^192. The class stores an interval [lo/S,hi/S] using integer
endpoints. Conversion from rational endpoints uses floor for the lower
endpoint and ceiling for the upper endpoint, including negative values.
Addition and negation are exact on this grid. For multiplication, the
minimum and maximum of the four products are the correct extremal bounds;
the subsequent division by S rounds outward.

For division the divisor is required to exclude zero. Its reciprocal is
enclosed by [S/hi,S/lo], where lo and hi are the stored integer endpoints.
The order is correct on both positive and negative intervals. Conversion
to the dyadic grid and multiplication each preserve containment.
Repeated interval multiplication in powers may enlarge a bound, but
cannot incorrectly narrow it. The same applies to all dependency losses
when the same radius occurs repeatedly.

The strict sign method fails if zero remains in the interval. Therefore a
successful sign call is a rigorous sign assertion, not a midpoint test.
The midpoint used in Sturm normalization is different: it selects an exact
positive rational scaling factor only after the whole leading-coefficient
interval has a strict sign. It is not used to infer a mathematical sign.

## 2. Exact algebraic coordinate identities

The polynomial utilities used for reduction modulo G have Fraction
coefficients. Their division is exact rational polynomial division.
Consequently the two zero remainders assert the polynomial identities

    X(alpha)^2+Y(alpha)^2=alpha,
    4tau^3+(6-i)tau^2-i tau-1-i=0,

for every root alpha of G, with tau=X(alpha)+iY(alpha).
Irreducibility of G is unnecessary for this implication.

At the squared rational radius endpoints, G has opposite strict signs.
Interval evaluation of G' is strictly negative throughout their interval.
The intermediate value theorem and strict monotonicity therefore prove
existence and uniqueness of the selected root there. The norm identity
then makes the constructed tau lie on the selected radius circle.

The checker does not prove that this is G's smallest positive root. That
extra characterization is unnecessary for the fixed-circle argument and
is not claimed in the saved result. Its result label correctly says only
that the selected root is unique in its interval.

## 3. Angular numerator independently rederived

For v=R exp(i theta), write the positive quantities

    A=1+4R cos(theta)+4R^2,
    B=1+2R(cos(theta)+sin(theta))+2R^2,
    C=1+2R cos(theta)+R^2.

Then |Psi(v)|=A^3 B^3/(R^4 C^2). Thus the sign of its logarithmic angular
derivative is the sign of

    D=3A'BC+3B'AC-2C'AB.

For q=tan(theta/2), the numerators of A,B,C over 1+q^2 are exactly the
three polynomials constructed in the checker. Direct substitution gives

    D=(-2R)/(1+q^2)^3 *
      [12q Bhat Chat+(-3+6q+3q^2) Ahat Chat-4q Ahat Bhat].

This bracket is exactly the checker's P. Hence its sign is opposite the
angular derivative sign. Using the squared modulus would multiply the
derivative by the positive constant 2, so the code comment about deriving
the numerator from |Psi|^2 does not change any sign conclusion.

The selected R is strictly between 0 and 1/2. Consequently A,B,C are
positive everywhere on the circle. Their potential zeros correspond to
complex points of moduli 1/2, 1/sqrt(2), and 1 respectively, none on this
circle.

## 4. Why the interval Sturm calculation is rigorous

Fix any exact R in the checked radius interval. At each stage, the stored
coefficient intervals contain the coefficients of the exact polynomial
obtained by Euclidean division from the preceding exact polynomials.
When a leading coefficient is divided, its divisor interval excludes
zero, so the quotient interval contains the exact quotient.

The line that drops the leading remainder coefficient is legitimate:
for this fixed R, the quotient was defined to cancel that very leading
coefficient, and the cancellation is identically zero. Retaining the
dependency-free interval subtraction would only create artificial width.
Discarding it uses the exact algebraic fact, rather than assuming the
width contains a small numerical value. The remaining coefficients are
updated with valid outward interval arithmetic. This proves containment
inductively through every division step.

Each new nonzero remainder is multiplied by the same positive rational
normalization for every R. Positive scaling preserves the Sturm sign
property. The asserted nonzero leading intervals ensure that exact
degrees cannot drop anywhere in the radius interval. In the saved result
the degrees are 6,5,4,3,2,1,0, and the final constant is nonzero. Thus P
has no repeated root for the selected R and the sign variations at the
two infinities give the usual Sturm count. The count is exactly two.

The four test points have signs +,-,-,+, so there is one root in
(-282,-281) and one in (11/40,69/250), exhausting the two real roots.
The exact saddle's half-angle coordinate lies in the latter interval.
At q=+/-infinity, the degree-six leading coefficient is
3(1-2R)^2(1-R)^2>0. Therefore the omitted angle theta=pi is not another
stationary point. The angular derivative has one minimum and one maximum,
and the positive-half-angle saddle is the unique maximum on the circle.

This last inference is mathematical interpretation of the checked data;
the current program reports the data rather than a separate boolean
named `unique_global_maximum`. A reader should retain this argument when
using the result.

## 5. Curvature and amplitude formulas

Differentiating the explicit logarithmic derivative gives, at S(tau)=0,

    lambda=tau^2(log Psi)''(tau)
      =(2-2i)tau S'(tau)
        /[(1+tau)(1+2tau)(1+(1-i)tau)].

The code constructs S'=12tau^2+(12-2i)tau-i, so all coefficients and signs
match. The interval complex division encloses the direct rational
expression, without relying on the old reduced curvature polynomial.
Its denominator norm is required to exclude zero. The resulting strict
lower bound Re(lambda)>2 gives nondegenerate negative real angular
curvature.

The amplitudes satisfy

    b2(tau)/b0(tau)
      =(1-i)(4tau^4+8tau^3+2tau^2-2tau-1)
        /[32tau(1+tau)(1+(1+i)tau)],

which is precisely the code's direct expression. The factors are nonzero
on the selected point, also following from its modulus. In particular
b0(tau) is nonzero. The positive imaginary part therefore proves

    Im(b2(tau) conjugate(b0(tau)))
      =|b0(tau)|^2 Im(b2(tau)/b0(tau))>0.

These formulas suffice for the desired sign conclusions. The checker does
not need to reproduce the stronger numerical intervals from the old
algebraic note.

## 6. Fixed-circle complex-Laplace hypotheses and error

The fixed circle lies inside radius 1/2 and has positive radius. A thin
annular neighborhood avoids the pole at zero, the pole at -1, and the
zeros at -1/2 and -(1+i)/2. Thus Psi is holomorphic and nonzero and both
amplitudes are holomorphic on that annulus. An interior pole at zero is
consistent with a coefficient contour; the lemma only needs an annulus.
The original coefficient-integral formulas permit deformation from a
smaller circle without crossing a pole.

The unique global maximum just established supplies a fixed exponential
modulus gap outside any sufficiently small neighborhood of the saddle,
by compactness. The local logarithm exists because Psi(tau) is nonzero;
its phase has no linear term since Psi'(tau)=0, and its quadratic term is
-lambda u^2/2 with Re(lambda)>0.

In the source lemma, the cutoff |u|<=m^(-2/5) becomes
|t|<=m^(1/10) after t=sqrt(m)u. The cubic exponential correction is then
uniformly small: t^3/sqrt(m)=O(m^(-1/5)). The quadratic Taylor remainder
of the amplitude, fourth-order phase remainder, square of the cubic
term, and their cross terms are bounded by m^(-1) times a fixed polynomial
in |t| under a Gaussian. The displayed degree-eight polynomial is ample.
The entire term of order m^(-1/2) is odd and integrates to zero on the
symmetric interval, also when lambda and the coefficients are complex.
This yields the stated absolute O(|Psi(tau)|^m m^(-3/2)) integral error.

The complex Gaussian identity holds on Re(lambda)>0 by analytic
continuation with the square root whose real part is positive. There is
no need to deform this local real integration line into a separate
steepest-descent contour. Uniformity over two fixed amplitudes follows by
taking the larger of their finitely many bounds.

Multiplying I2 by conjugate(I0) removes the common saddle phase. The
strictly positive amplitude then proves the determinant has the stated
sign and is nonzero for every sufficiently large integer m. No favorable
subsequence or parity intersection is needed for this nonvanishing step.

## 7. Scope and small clarity points

- The unusual `half_angle.lo*SCALE**0` is harmless since SCALE**0=1;
  removing that factor would make the comparison easier to read.
- The angular numerator derivation should accompany the data when making
  the unique-maximum claim; the program alone outputs a root count and
  sign table, with the geometric interpretation supplied above.
- The result is an independent certificate for saddle identities and
  signs, plus a review of the analytic lemma. It does not independently
  rederive the upstream coefficient-integral representation, residue
  determinant normalization, Cartier integrality, beta matching, or the
  missing positive arithmetic gain. Those remain separately scoped
  proof dependencies, as the program's `not_checked_here` field states.

No modification to root's checker or archived sources was needed.
