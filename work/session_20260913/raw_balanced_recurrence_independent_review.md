> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the raw balanced ladder and remainder quotient

Date: 2026-09-13. Reviewer: audit_results.
Reviewed `raw_balanced_recurrence_state.md`, Sections2--5.

The stated identities pass. No closed recurrence for the selected
remainder, or asymptotic conclusion, is inferred by this review.

1. The monic Legendre derivative identity has coefficient
   gamma_k=k^2/(2k-1)=(2k+1)beta_k. The three stated Borel identities
   are exact on each monomial. They give
   JF_k=(k+1)integral F_k+gamma_k F_(k-1), hence the ladder coefficient
   on F_(k-1) is gamma_k-(k+1)beta_k=k beta_k, as claimed.
2. J=D x D+x is formally self-adjoint. Its integration-by-parts
   boundary term is x(PF'-P'F), zero at0 and equal to the displayed
   term at1. Moving it to the other side gives precisely the two signs
   in the moment-transfer equation. The new n+1 degree window requires
   the three additional upper rows listed in the source relative to
   the interior window where both shifted old moments vanish.
3. Leibniz's rule gives the jet update
   u_(r+2)+(r+1)u_(r+1)+u_r+r u_(r-1). The polynomial
   (x-1)^(m+2) supplies the proposed counterexample to closure on jets
   through order m, with nonzero updated mth jet (m+2)!. Its scope is
   all polynomial degrees; this does not exclude an extra identity for
   the actual selected P_n.
4. Repeated integration by parts proves
   integral_(-infinity)^1 e^(x-1)P(x)dx=sum(-1)^rP^(r)(1).
   Thus b(P) is exactly the original B(1) functional. Cramer's rule with
   constraints b(P)=1 and m(P)=0 yields the displayed determinant ratio
   with the numerator rows r,m and denominator rows b,m. The signs and
   normalization are correct, and both determinants acquire the same
   factor after a basis change of the actual two-dimensional annihilator.
5. The skew matrix Omega reproduces each term of the previously proved
   four-jet Green form; its Pfaffian is-1, so its determinant is1.
   Dividing by lambda_k-lambda_j gives the stated rational observation
   formula. The high indices exclude all poles and no diagonal limit is
   required. The tail representation for r(P) is absolutely convergent:
   its absolute terms are bounded by the integral of |P| against the
   positive, uniformly convergent tail kernel. Under a degree shift the
   old first observation disappears and the two stated final observations
   are added.

The source correctly keeps the n+1 scalar residues of its four-component
rational function. Four components do not make a four-dimensional free
state when its degree and pole count grow. The missing degree-shift rule
and accessory-parameter asymptotics remain missing; none is supplied by
the exact identities alone.
