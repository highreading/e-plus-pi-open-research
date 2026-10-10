> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the actual high-cofactor contour reduction

Date: 2026-09-13. Reviewer: audit_results.

Scope: raw_actual_high_cofactor_contour_reduction.md, especially
Sections3–4, with the two fixed canonical endpoint rows retained.
No new canonical degree solve, spectral sample, or asymptotic claim.

The exact contour identities pass. Start with ordered coefficient
extraction at indices a,...,a+r−1. Antisymmetrizing against the
alternating determinant Phi gives1/r! times the determinant of the
weights z_p^(−i), i=0,...,r−1. Its determinant is
(-1)^(r(r−1)/2) Delta(z) product z_p^(−r+1).
The remaining Cauchy factor z_p^(−a−1) therefore gives exponent
a+r=2n. This verifies simultaneously the sign, factorial and
power in(6)–(7). A direct r=2 check has weight
(z_2^(−1)−z_1^(−1))/2=−Delta/(2z_1z_2), agreeing with the sign.

Replacing the exponent list0,...,r−1 by0,...,r with r−j omitted
changes its alternant by e_j(z_1^(−1),...,z_r^(−1)). The coefficient
sign from the degree-r monic polynomial in each reciprocal variable
is canceled by moving the inserted row to its increasing position.
No endpoint row moves. Consequently(8) has exactly the positive
factor e_j, and summing the elementary symmetric functions gives
the product in(9). Its j=1 term is precisely(10).

For the original unscaled F rows, replacing b=2n−1 by b+1=2n
removes the explicit factor c_(b+1)/c_b; its inverse is
c_b/c_(b+1)=(b+1)/(2b+1)=2n/(4n−1). This agrees with the note.
The denominator is the known nonzero actual bordered determinant;
the derivation does not substitute a generic high-row minor.

I also checked the normalization adjacent to these formulas.
The endpoint beta row is sum_l(-1)^l(j)_l, equal to the displayed
(-1)^j j! sum_h(-1)^h/h!. The odd spectral factor1/sqrt3 in(5)
agrees with c_k F_k=r_k^0(T)v_0+r_k^1(T)v_1/sqrt3. The stated
absolute spectral convergence is justified by the already proved
factorial amplitude decay and the fixed-radius branch bound for
each fixed polynomial column. It is not uniform in the column
degree, and the note does not claim otherwise.

The total-variation bound in(11)–(12) follows from the triangle
inequality and |e_j(z_1^(−1),...,z_r^(−1))|<=binom(r,j)rho^(−j).
The distinction between a proved identity and the unproved relative
integral bound is maintained throughout. Neither positive measures
nor D_n!=0 establish the missing uniform denominator estimate.

One prose correction was sent to the author: the final paragraph's
'second-order equation in the spectral parameter' must read a
second-order equation in the transform variable w, with xi as
spectral parameter. The displayed mathematics and its contour
conclusions do not depend on that wording.
