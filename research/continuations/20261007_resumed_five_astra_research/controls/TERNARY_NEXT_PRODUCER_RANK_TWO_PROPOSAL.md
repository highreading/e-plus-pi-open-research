> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Parent proposal: the complete next producer digit has rank at most two

Status: coordinator derivation, awaiting independent review. This is not a
claim about the final cofactor, all-prime gcd or irrationality. Original domain,
complete functional cutoff and physical HIGH terminal are retained.

Use the accepted original Rcal=mathscr R mod3 jet
Rcal= kappa (y+1)x^A, its degree<=A+1 reset, and its exact endpoint, which
vanishes modulo9. Here kappa is the actual old producer coefficient, not a
freely chosen seed. The accepted first core jet is

 F_i = x^D (y^i -3 delta_i q_d) modulo9,
 delta_i=1 iff i=nu-1, deg(q_d)=nu, leading coefficient1.

For any integral Delta of degree<=m, the parent proposes the COMPLETE identity

 M(Rcal F_i Delta) = -3 kappa delta_i [y^m]Delta modulo9.          (1)

Proof to audit: endpoint divisibility and the reset give
Rcal=(y+1)(kappa*x^A+3 B1) mod9 with deg B1<=A. At the sole unit-weight pole
r*=(3H-1)/2, both x^H y^i Delta and B1*x^D*y^i*Delta have degree<=r*-1.
The first-jet term -3 kappa delta_i x^H q_d Delta has degree<=r*;
its top coefficient is exactly -3 kappa delta_i [y^m]Delta, since
H+nu+m=r*. At poles of weight3, only the mod3 leading product matters.
There is exactly one such pole below the original cutoff, denominatorH,
index r1=(H-1)/2. The reduction x^H=y^H-1 and i+m<=r1-1 make that extraction
zero. Remaining pole weights and the factorial contribution are divisible9.
Endpoint subtraction is paid because the model product has factor(y+1), and
complete functional integrality preserves the mod9 substitution.

Now take the accepted precision20 representative F_i*=x^D psi_i, with its
strict degree gap below m. Write F_i*=F_i+3^20 Delta_i. Thus the actual top
coefficients t_i=[y^m]F_i/3^20 are integral, and [y^m]Delta_i=-t_i.
No bound t_i=0 mod3 is presumed.

The parent proposes a new MODEL estimate

 M(Rcal F_i* F_j*) in3^22.                                    (2)

Its source payment is explicit: for a<=A-55,
v3((A+1)!/a!)>=5+v3(54!)=31, so after the actual division3^7 these coefficients
vanish even modulo3^24. At precision22 this gives
Rcal=(y+1)x^(A-54)q22 modulo3^22, deg q22<=54, by the exact endpoint identity.
Hence the model product has endpoint quotient x^H times
x^(D-54)q22 psi_i psi_j, supported in Omega20 Z+[-21D,21D].
The x^H grid at precision22 is Lambda=H/3^21=Omega20/9. Every contributing
pole is on Lambda's odd half-grid. The original ratio gives
Lambda/D>147968/729>42, so the entire extraction is zero modulo3^22.
The factorial term retains its factor3^h. All degree and endpoint conditions
are those of the finite model already used at precision21.

Expanding F*=F+3^20 Delta and using (1), with the quadratic term paid by3^40,
then predicts the EVALUATED next actual correction

 Phi_mathscrR /3^21 = -kappa (delta t^T+t delta^T) modulo3,
 Phi_R /3^22       = -kappa (delta t^T+t delta^T) modulo3.       (3)

The accepted Qquad in3^21 makes the quadratic Schur perturbation vanish after
division3^28. Consequently the complete next producer digit should be

 (S_act-S_c)/3^28 = -kappa (delta t^T+t delta^T) modulo3.        (4)

This is rank<=2 in the original middle coordinates even if t is unknown.
The coefficient t is an actual HIGH endpoint coefficient, not a generic
finite-rank replacement. The proposal does not omit it or assert that it
vanishes. It does not evaluate the precision29 core, new prefix elimination,
actual endpoint lift or bordered diagonal. Those must still be included before
any next radical or relative-cofactor claim. A referee must check every step,
including the sole weight3 pole, model support and signs.
