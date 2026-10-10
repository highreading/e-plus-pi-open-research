> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Bounded differential equations and asymptotics: applicability to the raw family

Date: 2026-09-13. Targeted primary literature search prompted by the
actual raw remainder and its new homogeneous differential equation.
The searches also covered exponential/logarithmic HP asymptotics,
Riemann–Hilbert methods, Nikishin systems and accessory polynomials.
No source is being used as a theorem about e+pi.

## Primary results inspected

1. Martínez-Finkelshtein, Rakhmanov and Suetin,
   [Asymptotics of type I Hermite–Padé polynomials for semiclassical functions](https://arxiv.org/pdf/1502.01202),
   version3, May2015. Inspected the hypotheses, Theorems1.1–1.2,
   the explicit two-branch-point example, and the Wronskian strategy in
   Section3.1. Their algebraic-product class has rational logarithmic
   derivatives and regular behavior at infinity. A bounded-degree
   differential equation is the starting point; unknown accessory
   coefficients remain a separate asymptotic obstruction in the general
   case. The explicitly solved system has the form1,f,f^2. This supplies
   a methodological precedent for the project's Wronskian construction.
   It is not a directly applicable asymptotic theorem for1,exp,atan:
   atan'/atan is not rational, exp has different behavior at infinity,
   and the endpoint matching is an additional condition. The actual raw
   homogeneous equation is proved separately by its rational differential
   module and endpoint order, rather than by claiming these hypotheses.

2. Kuijlaars, Van Assche and Wielonsky,
   [Quadratic Hermite–Padé approximation to the exponential function: a Riemann–Hilbert approach](https://arxiv.org/pdf/math/0302357),
   February2003. Inspected the defining exponential system, its contour
   phase and cubic surface in Section2, and the scaled Riemann–Hilbert
   formulation. The paper proves strong asymptotics for the system with
   exp(-z),1,exp(z), scaled by3n. Its explicit contour phase is what
   determines the corresponding three-sheeted surface. Substituting the
   raw mixed family into that surface is unjustified: the logarithmic
   term and its finite singularities change the analytic problem. The
   next transferable step would be to derive the actual connection or
   contour data first, not reuse the exponential saddle equation.

3. González Ricardo, López Lagomasino and Medina Peralta,
   [Logarithmic asymptotic of multi-level Hermite–Padé polynomials](https://arxiv.org/abs/2002.06194),
   February2020 preprint. The abstract's scope is a rational perturbation
   of a Nikishin system. This was an abstract-level applicability screen,
   not a full paper audit. No required Nikishin representation for the
   actual high Borel block has been established, so its convergence rate
   cannot be imported. The project's exact sign and Favard obstructions
   must be respected by any proposed representation.

## What the actual differential route still needs

The source agent is deriving a homogeneous third-order equation for the
three actual analytic functions R_n,B_n exp,C_n. This is a continuation
of the already proved cubic Wronskian forcing, not a consequence of a
generic statement that all HP approximants share the same asymptotics.
The coefficients have bounded degree, but their n-dependent rational
accessory values are not yet bounded or classified.

There are three distinct requirements for using such an equation here:

* Recover its actual coefficient scaling as n increases, including any
  degenerate subsequences or apparent singularities.
* Select the solution with the imposed large zero at the origin and the
  endpoint normalization, controlling its connection to z=1. A formal
  characteristic root or a possible limiting zero measure is insufficient.
* Retain the actual primitive denominator when comparing the evaluated
  error with an integer lower bound.

These are additional mathematical tasks. Local singular exponents alone
do not determine a connection coefficient or select the actual small
solution. A rational degree-shift matrix, if proved, can help express
the accessory evolution, but its existence does not make its coefficients
known functions of n or establish a limiting exponential rate.

The current direct alternative remains the actual two-dimensional
annihilator and its determinant quotient. The paired factorial mass and
cancellation estimates are rigorous, but neither gives the exponential
rate of their product. The differential route is ranked by its potential
to determine that missing rate, not by an asserted application of a
literature theorem whose hypotheses fail.
