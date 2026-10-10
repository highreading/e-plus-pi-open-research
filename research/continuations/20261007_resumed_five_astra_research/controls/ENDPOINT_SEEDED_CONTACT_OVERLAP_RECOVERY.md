> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Existing companion and complete-contact residual: overlap recovery

The coordinator checked the preceding round before commissioning another
companion or projected-residual calculation. Previous A3turn6, sections7--8,
already contains the same classical companion rho, normalized by

  tau_n rho_(n+1) - tau_(n+1) rho_n = (-1)^n/(n+1),

the exact integral complete terminal decomposition

  C_complete = S_n v' + T_n w' + (n+1)Z_n e_2,
  S_n = (n+1)b_n/2 + 2 n! (n+1)! rho_n,
  T_n = b_(n+1) - (n+1)b_n/2 + 2 n! (n+1)! rho_(n+1),

and exact large-prime ideal equalities involving the evaluated complete contact
C_j = r_j C_complete. Current A3turn3's sigma with seeds0,1 has this same
normalization. Thus Usharp=S_n, Vsharp=T_n. Since the recovered V has columns
v',w',e_2, the current numerator is EXACTLY

  pi_1 Usharp + pi_2 Vsharp + pi_3 (n+1)Z_n = C_j/kappa_j.

Consequently the new residual is

  E_j = C_j/(kappa_j b_(c,j)).

This is a paid refinement of an existing complete-contact quantity, not a new
independent seed invariant or a new general companion method. Current planar
content payment and comparison with T_aff may still sharpen the arithmetic;
their claims require review with the existing residual theorem supplied.

Previous A3turn6 also proves, using the actual primitive rows and moment
primitivity,

  gcd(G_3,C_3) divides 4(n+1)^2(n+2)^2,
  gcd(G_0,C_0) divides 4(n+1)^2(n+2)^2(n+3),
  G_j = gcd(r_j v',r_j w').

Because kappa_j b_(c,j) divides BOTH G_j and C_j, it obeys those polynomial
all-prime bounds at their retained original scope. In particular its large
prime part above n+2 is trivial on the odd original family. This deduction
does not control gcd(D_j,C_j), the moving-prime inventory, final row contents
or the all-prime approximation denominator.

The exact archived sections accompany the next packet. No old companion,
producer3375, or closed gauge computation should be repeated.
