> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: the actual two-function Padé equation

Date: 2026-09-13. Reviewer: root. FULL PASS.

Reviewed raw_two_function_dual_pade_equation.md in full, independently
checking its algebra against the actual Toeplitz equation.

1. C=z^n B(1/z) is monic, C(0)=v0>0, and Ev-C has order at least
   2n+1. Dividing a hypothetical common factor gives a genuine null
   vector for the same invertible A, so coprimality is proved.
2. W(C,Ev)=e^z D^(n-1) z^(2n)K. The origin order uses C(0)!=0;
   the infinity degree uses the unique top term z^2 Cv. Thus K is
   nonzero of degree k<=2, deg(v)=n+k-2, and the error order is
   2n+1+ord_0 K, including all defects.
3. Differentiating W gives the displayed A1 with both the 2n/z and
   (n-1)D'/D terms. Expanding h'+h^2 gives exactly the numerator
   displayed for A0. Its divisibility follows from W(C',F'), whose
   order is at least 2n-1. It is therefore a polynomial, not merely
   a rational coefficient with an unchecked pole.
4. Substitution of the degree-n polynomial solution C at infinity
   gives A0/A2=n/z+O(z^-2), and all three exact degree claims follow.
   The converse integrates the ratio with initial value one and uses
   the degree-n coefficient to recover Av=e0; no free normalization
   or unproved Padé normality enters.
5. At ordinary roots, coprimality makes the other solution a unit,
   so root multiplicity is one plus the corresponding K multiplicity.
   At i and -i, the orders r and n+s are distinct since real C has
   r<=n/2<n+s. This proves r+s=ord K at those points.
6. The negative-axis Rolle argument includes its extra critical point
   before the first root because Ev/C tends to zero at minus infinity.
   For C in (-1,0), positive endpoint values force an even total
   multiplicity; the bound k+1<=3 then yields at most two. These are
   real-root counts and do not assert a sign for the complex-arc integral.

The derivative J_n^(n)(1)/n! and the definition of a_n agree with the
previously reviewed error identity. The primitive gcd is retained.
The bounded equation by itself supplies neither an estimate for its
connection value nor a proof of a shrinking primitive integer form.
