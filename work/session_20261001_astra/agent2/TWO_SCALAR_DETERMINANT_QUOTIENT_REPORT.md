> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Report: actual two-scalar determinant quotient

The two contractions z0,z1 are rational because the exponential parts of their tail rows vanish against evec. Their actual monic identities are

D_V=(A1 z1-A0 z0)/h_n,
D_W=(v_n z0-v_(n+1)z1)/h_n,
T=-Bform(arow,crow)/h_n.

The proposed conditional lemma is proved: z0*z1<=0 and a nonzero pair imply a nonzero actual endpoint and |D_W/D_V|<=epsilon_n. The cases z0=0 and z1=0 are included explicitly.

All four frozen controls n=4,6,8,10 satisfy z0<0<z1. The exact checker completed successfully without new canonical solves or additional degrees. It also reproduced both saved rational companions and the existing fully reduced q. Full evidence and primitive high minors are in two_scalar_quotient_evidence.json; the frozen source was preserved.

The complete companion reduces using Bform=gamma Bbar to

Bform(arow,crow)/(h_n D_V)=e+K_tail/d,
d=A1 Z1-A0 Z0,
K_tail=Bbar(T(Uref),T(p_n)).

Thus r_e=-K_tail/d is rational, T/D_V=r_e-e, and the actual endpoint ratio is X/Y=-r_pi-r_e. The actual q is den(-r_pi-r_e), including all final cancellation.

A Plucker identity supplies a bound with the same primitive minor coordinates. Let N be their antisymmetric matrix and

C=min_(j:Bbar(evec,f_j)!=0) sum_k|N_jk|/|Bbar(evec,f_j)|,
Delta=|d|/(A0|Z0|+A1|Z1|).

On D_V!=0, Delta>0 and C is defined. Then

|R(1)/Y|<=[epsilon_n+C e4^(n+1)/(n+1-b)!]/Delta.

Under the sign hypothesis Delta=1. The displayed factorial factor has logarithm -n log n/2+O(n) for b=floor(n/2). No uniform bound on C is proved, and the inequality preserves the actual endpoint pole separation rather than dividing independent upper bounds.

The required recurrence investigation produced exact factorial-array and shifted-minor recurrences, documented in TWO_SCALAR_DETERMINANT_QUOTIENT.md. The n to n+2 step introduces additional minors and coefficients without established sign control. No closed sign-preserving recurrence or uniform even-degree determinant inequality was obtained. Finite success is not promoted to a sign theorem.

Remaining inputs are uniform sign or quantitative pole avoidance, companion control through C or the exact rational companion, sufficient actual q, and full-remainder nonvanishing at the same indices. Separate irrationality of e and pi proves the two individual companion errors nonzero; it does not prevent their sum from vanishing.

Files for this continuation are TWO_SCALAR_DETERMINANT_QUOTIENT.md, this report, check_two_scalar_quotient.py, and two_scalar_quotient_evidence.json. Earlier corrections, reports, and frozen certificates remain preserved. No fixed-b determinant limit, wider degree or prime sweep, networking, installation, or edit outside Agent 2's directory was used.
