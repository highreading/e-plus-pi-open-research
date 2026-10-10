> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the accessory subleading identities and compactness lemma

Date: 2026-09-13. Reviewed by audit_results.

Reviewed Sections3–4 of raw_accessory_scaling_and_compactness.md, and
the explicit hypotheses of its conditional limit in Section6. No new
numerical indices were computed.

**Verdict:** the three exact coefficient identities and the conditional
compactness theorem pass.

For the Wronskian expansion, write the two Laurent branches as
H=z^n(1+alpha/z+...), V=z^(n-1)(1+gamma/z+...), and the exponential
branch as U=e^z z^n(1+beta/z+...). In



$$
W(H,U,V)=U''(H'V-HV')+U'(HV''-H''V)
          +U(H''V'-H'V''),
$$



the first term has relative coefficient beta+2n+2gamma. The second
contributes -2(n-1) at that order, and the third starts one power
later. The alpha coefficient cancels in H'V-HV'. Thus the first
Wronskian correction is beta+2gamma+2, giving q2 as stated.

Independently expanding the exponential equation gives its next
coefficient as



$$
-\beta-3n^2+n+(3-2n)q_2+u_4=0.
$$



Expanding the high Laurent branch gives



$$
-2n^3+2n^2-n^2q_2+nq_2+nu_4+v_3=0.
$$



The coefficient of alpha in this latter equation is



$$
-(n-1)(n-2)+2(n-1)^2-n(n-1)=0.
$$



This verifies the resonant cancellation directly and proves both
displayed formulas for u4 and v3. The coefficient formula for the low
Laurent slope gamma follows from atan(z)-F_infinity=-1/z+O(z^-3).
Its denominator is nonzero by the established distinct-degree ledger;
no quantitative lower bound on it is asserted.

For compactness, the common O(n) root bounds imply scale-independent
derivative-quotient bounds on one fixed circle z=n*zeta, |zeta|=R.
The difference U'/U-C'/C is bounded away from zero because the
exponential contributes1 and the two polynomial logarithmic derivatives
are each smaller than1/(R-K). Subtracting their scalar equations
therefore bounds A1/A3 without a leading-coefficient lower bound.
The C equation then bounds A0/A3. The Wronskian formula separately
bounds A2/A3, and Vieta bounds the scaled monic Q. Multiplication by
the bounded scaled A3 and Cauchy's coefficient formula complete the
claimed finite-dimensional compactness conclusion.

Repeated roots, lower polynomial degrees, and constant C cause no
exception to these product-formula estimates. The fixed circle avoids
all roots and fixed singular points by the chosen margin.

The Section6 limiting coefficients follow from its three explicitly
listed hypotheses. In particular the vanishing of seven lower
accessory coefficients is an additional hypothesis, not a consequence
of the two subleading identities. The stated exclusion of the inner
endpoint region is necessary: z=1 becomes zeta=1/n.

No uniform root bound, coefficient convergence, or endpoint remainder
estimate is proved by this review.
