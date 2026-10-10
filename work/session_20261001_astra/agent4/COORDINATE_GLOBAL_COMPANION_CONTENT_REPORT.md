> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Global coordinate companion content report

New paper results for the same eligible positive b=3 coordinates on n=13^(s+1)+3, s>=5. No previous review or computation was repeated, and no prime scan was performed.

The complete moment admits the odd global clearer O=lcm(odd integers <=2n+2). For the three universal basis selectors define integer endpoint values U_i and integer moments J_i=O R_i. The actual adjugate selector C_j therefore maps through the explicit integer matrix

Z=[[O U_0,O U_1,O U_2],[J_0,J_1,J_2]].

This removes the raw factorial scale from the global denominator formula.

In the rank-two branch, integer column operations reduce Z to [[g,0,0],[a,t,0]]. Put d=gcd(g,a,t), (g',a',t')=(g,a,t)/d, and D=gt/d^2. Transform the actual selector by the inverse column operations, obtaining z. Remove the effective image content r_j=gcd(z_0,z_1), and write (u_j,v_j)=(z_0,z_1)/r_j. The exact new factorization is

(X_j,L_j/(n!)^2)=(d r_j/O)(g'u_j,a'u_j+t'v_j).

Consequently

B_j=g'|u_j|/e_j,
e_j=gcd(D,g'u_j,a'u_j+t'v_j),
e_j divides D.

The universal determinantal modulus satisfies log D=O(n), and log g'=O(n), by explicit coefficient and moment bounds. Hence

log B_j=log|u_j|+O(n)=log|X_j|-log r_j+O(n).

This is a global rate reduction to effective image content, not a favorable rate estimate for the actual adjugate rows. That remaining gcd is not assumed large. It can exceed ordinary selector coefficient content because the third transformed coordinate belongs to the common kernel.

If Z has rank one, handled explicitly rather than excluded by an unsupported rank assertion, B_j=g/gcd(g,|a|)<=exp(O(n)) for every defined coordinate. The three explicit two-row minors decide the branch. No claim is made that the rank-one branch occurs.

For every p dividing D, cancellation is decided by the two primitive output congruences modulo p^ell, 1<=ell<=v_p(D). At primes outside D the denominator exponent equals v_p(u_j); these primes are not assumed absent. To obtain primitive inputs modulo p^k from the unnormalized image coordinates requires precision p^(v_p(r_j)+k), and certification of v_p(r_j) requires the next nonzero digit. These precision requirements are included in the proof.

Deliverables: COORDINATE_GLOBAL_COMPANION_CONTENT.md and this report. They are new exact paper deductions using the retained coordinate moment identity. The completed 13-adic theorem is preserved as a consistency condition. No Gram-center transfer, global favorable exponent, or irrationality conclusion is asserted. Both files must be read back before delivery is reported complete.
