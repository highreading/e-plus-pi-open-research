> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent root review of the auxiliary analytic-disk reduction

Date:2026-09-13. Status: PASS, within the explicit conditional scope.
Source:hp_auxiliary_simple_root_analytic_reduction.md.

I checked the two factorial sums against h_n and E_n, including E_0=1.
For X=a+pY every length-L falling product has floor(L/p) factors in
p Z_p[Y]. Division by b!c! loses at most v_p((b+c)!). This proves
the displayed Gauss bound, not just a bound on integer evaluations.
For odd p its lower bound tends to infinity, and for R>=2p it is
at least2. Thus the restricted analytic interpolation and termwise
calculations modulo p^2 are justified.

For R<2p the denominator has at most one p; coefficients of Y^j,
j>=3, vanish modulo p^2. A surviving quadratic coefficient requires
b>=p. The residual falling products and Wilson factor then reconstruct
h_a for H and e_a for E. I checked the exceptional E disk a=0:
the sole remaining pair has factors p(Y-1),pY and gives pY(Y-1),
so the quadratic coefficient is indeed e_0=1. Multiplication by X+1
proves the J formula; the a=p-1 branch reduces directly to2p(1+Y).

At a joint residue the normalized gate series have affine reductions.
The determinant compatibility condition is the exact condition for
two affine equations with a nonzero slope vector to share a solution.
For the selected unit-slope series, Hensel iteration gives one root;
the quotient after factoring that root is a unit throughout the disk.

One normalization detail in the difference estimate merits emphasis:
write the other gate as G(a+pY)=p G_a(Y), where G_a is integral by
the JOINT-residue hypothesis. Then
G(n)-G(xi) is divisible by p((n-xi)/p)=n-xi. Mere integrality of an
unscaled disk series would lose one p. The source's Section3 provides
exactly the scaled integrality needed, so no loss occurs. The minimum
valuation formula therefore follows in all three relative-valuation
cases, including equality and infinite compatibility valuation.

The proof establishes a reduction CONDITIONAL on nonzero index slope
at the residue under consideration. It establishes neither that every
joint residue has that property nor that its compatibility constant is
finite or small. Differentiation in the index is correctly distinguished
from differentiation of H_a(x) at x=1. The fixed-p theorem has no
automatic consequence in the growing-prime range p>2n+2. No new global
auxiliary-gcd or actual reduced-denominator bound is accepted here.
