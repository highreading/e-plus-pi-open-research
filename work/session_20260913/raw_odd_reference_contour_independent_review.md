> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the odd reference and contour assembly

Date: 2026-09-13. Reviewer: audit_sources. **FULL PASS.**

Audited in full: raw_odd_reference_and_contour_asymptotic.md.
The separately named multiplier input has also passed in
raw_odd_saddle_multipliers_independent_review.md. This review does not
repeat the already reviewed global phase certificates.

## 1. Fixed-offset polynomial and analytic expansion

The reference coefficient and hypergeometric formulas agree with the
positive circular moments. The falling-polynomial finite-difference
orthogonality argument works for a=m+lambda, lambda>=0; all required
moments are integrable. The terminating denominators are nonzero through
degree m, including lambda=0. The leading coefficient (m+lambda)/
(2m+lambda), the actual lambda=1 reference, its extra factor z,
and its positive norm 1/c_m all check.

The hypergeometric equation is exactly



$$
w(1-w)f''-[2m+\lambda+(\lambda+1)w]f'
       +m(m+\lambda)f=0.
$$



Root exclusion gives a uniformly bounded analytic logarithmic derivative
on each compact subdisk. Any limit selects r=1/(1+S) by its value
at zero. The subtraction argument is strong enough for the stated
orders: the coefficient of r_m-r tends to -2S, bounded away from
zero; Cauchy bounds first give an O(1/m) error, and then control its
derivative to give the O(1/m^2) refinement. Integration normalized at
zero therefore gives the full relative reference expansion and fixed
derivative estimates. No convergence rate was inferred solely from
normal-family convergence.

The new correction J satisfies the displayed exact differential identity
in chi. Its normalization at chi=1/2 gives



$$
e^J=\frac{9\chi}{2(1+\chi)^2}.
$$



At the saddle, chi=rho^2, Q(chi)=2rho^2,
e^J=9/10, and e^L=27rho/20. Thus



$$
e^{K(w_s)}
 =e^{H_0(w_s)}\sqrt{\frac3{5\rho}}
 =\frac{3\sqrt{10}}{20\rho^{3/2}}.
$$



The n=2m+1 conversion K=H_1-L/2 is essential and correct.
The separately stated lambda=1/2 correction is also consistent, but is
properly kept out of the actual lambda=1 contour.

## 2. All-parity inversion and residue sign

Inverting the original arctangent path reverses its endpoints. The
minus sign from dt=-z^(-2)dz cancels that reversal, leaving the
original explicit factor (-1)^n/(2i). The inherited left-contour
homology applies to odd n as well. At infinity the rational integrand
is O(z^(-2)), so the connecting arc from an inversion near t=0
does not introduce a contribution.

Expanding the integrand at zero gives



$$
\operatorname{Res}_0 I_n=(-1)^{n+1}Z_n/u_n.
$$



The binomial sum is exactly S_n^(n)(1)/n!=Z_n; normalization by
n!V_n(1)v_0=u_n is retained. Replacing (z-1)^(n+1) by
(1-z)^(n+1) cancels this parity sign. The counterclockwise coefficient
contour for Z/u_n therefore has the same positive sign in both parities.
The frozen n=1 control agrees with both identities.

## 3. Phases and global contour estimates

The degree-n reversal identity
v(z)/v_0=z^nF_m(1/z)Rtilde_n(1/z) is exact despite
deg F_m=n-1. Consequently both n-based phase functions are precisely
the previously reviewed even functions. The actual offset changes only
the bounded analytic transport from H_0 to K.

On the exterior arc, (-z)(1-z)=z(z-1) introduces no additional
integer-power sign. The only parity sign outside the multiplier is
the (-1)^n already present in the original integral.

The accepted strict maxima and curvatures therefore apply unchanged.
For the endpoint arcs, root exclusion gives the bound with exponent m,
which is no worse than the old exponent n/2. The independently proved
odd Hardy bound supplies the same required type of uniform control.
Thus the geometric endpoint estimate remains valid; no compact
asymptotic is extended without proof to the boundary points.

## 4. Gaussian constants and primitive normalization

At the exterior saddle dz=i dy and z(z-1)=rho^(-3). The arctangent
prefactor is therefore (-1)^n rho^3/2, and multiplication by the
actual phase (-1)^m gives (-1)^(m+1). At the interior saddle,
dz=i z dtheta cancels the extra z, leaving 1/(1-rho).

These facts give the source's exact c_a and c_Z. The varying-multiplier
Gaussian estimates are uniform because the independent Hardy bound and
Cauchy estimates control the entire actual amplitude family. Their
absolute error statements do not divide by the amplitudes and are valid
before their nonzero limits are inserted.

The curvature relation gives



$$
\frac{c_a}{c_Z}
 =\pi\rho^3(1-\rho)\sqrt{\kappa/h_o}=\pi\rho.
$$



In particular the common odd transport cancels. The exponential
remainder is negligible relative to the arctangent remainder after
using u_n=(2n)![t^n]V_n; the displayed factorial estimate is correct.

With the independently certified A_o<0 and B_o>0 now available,



$$
(e+\pi)-\frac{N_n}{Z_n}
 =(-1)^m C_o\rho^{5n}(1+o(1)),\qquad
 C_o=-4\pi\rho A_o/B_o>0,\quad n=2m+1.
$$



The factor four comes from the original numerator Pe+4Pa; the
arctangent-only ratio has pi*rho. The reduced denominator remains
q_n=|Z_n|/gcd(|Z_n|,|N_n|). Thus the source's final primitive-error
criterion has the correct actual normalization.

No arithmetic lower bound is silently imported into the contour proof.
All sections pass without correction. No effective first index or
relative error rate beyond o(1) is claimed after inserting the
multiplier limits.

## 5. Explicit dependency map and absence of circularity

The proof dependencies can be ordered as follows:

1. The original exact raw polynomial identities, high-row rank, and
   added-column nonvanishing are algebraic inputs. The circular binomial
   orthogonal polynomials and their positive norms are separate exact
   finite-moment inputs.
2. The inherited odd boundary-operator limit uses those positive
   polynomials and the exact rank-two factorization. The independently
   audited fixed-operator interval certificate proves nonzero D_2 and
   D_3. Together with finite-degree nonvanishing, these imply
   s_m->s_infty!=0 and a uniform full inverse bound.
3. The odd Hardy framework uses only items 1--2: exact finite moments,
   the uniform inverse, and u_0=c_m/s_m. Its independent review does
   not use the new multipliers or either new contour.
4. The odd imaginary-node kernel limits use only the exact positive
   recurrence and a summable reversed-tail estimate. The amplitude
   theorem combines those kernels with item 2's full Woodbury solution
   and the old certified witness columns. Item 3 supplies local analytic
   compactness. It does not use the arctangent or endpoint contour
   asymptotics.
5. The fixed-offset reference ODE expansion uses only the explicit
   circular polynomial and root exclusion. The inherited phase maximum
   and Gaussian estimates used here are the phase/contour lemmas of
   the reviewed even work; their proofs do not require any odd
   amplitude. The new odd contour assembly combines these with
   items 3--4 and the original exact contour identities.
6. The old odd exponential-error estimate uses item 2's inverse bound
   and the original exact exponential integral. It does not use the
   new arctangent or Z asymptotics. Combining it with item 5 proves
   the odd relative-error theorem.
7. The residue-transfer, finite prime certificates, and actual reduced
   denominator divisors are independent algebraic/arithmetic results.
   Their all-index use is combined with the two parity relative-error
   theorems only in the subsequent exclusion assembly.

In particular, the independent Hardy review, amplitude interval
certificate, and contour Gaussian proof are not mutual assumptions.
The new all-parity exclusion may use all of them without feeding that
conclusion back into a nonvanishing or inverse bound.

The elementary all-index arithmetic extension is also checked:
the exact dyadic exponent satisfies a_n>=3n/2-1/2, so the same ten
uniform odd primes give



$$
q_n\ge\frac{\exp(Ln)}
 {\sqrt2\,25839289479611181\,n^{10}}\qquad(n\ge302)
$$



without a parity restriction. The new odd asymptotic and the reviewed
even asymptotic each have a positive, nonzero magnitude constant.
This makes the subsequent all-index primitive-divergence deduction
valid. Its standalone assembly is being recorded separately by
audit_results.
