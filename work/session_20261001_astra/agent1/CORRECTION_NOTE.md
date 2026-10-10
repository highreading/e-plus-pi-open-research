> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Correction of the b=2 boundary assertion

Status: the correction is proved algebraically and its targeted exact checks passed. The result has not received independent review.

The earlier PROOF_DRAFT.md and REPORT.md asserted that, whenever n=-1 modulo an odd prime p, S=C=W=V=0 modulo p. The assertion about C was false. The earlier successful certificate did not assert C=0, so its exact calculations remain valid.

The corrected statement is

H_(n+1)=1, J_(n+1)=K_(n+1)=0 modulo p,
S=W=0, C=-J_n modulo p,
V=Dcal_n=0 modulo p.

Here C need not vanish. The all-index derivative transfer proves the three adjacent-state congruences. Substitution into the actual definition gives

C=(J_(n+1)-H_(n+1))J_n-(K_(n+1)-J_(n+1))H_n
 =-J_n modulo p.

The erroneous implication had overlooked the term -H_(n+1)J_n. The other conclusions follow independently:

S=J_(n+1)^2-H_(n+1)K_(n+1)=0,
W=J_(n+1)J_n-K_(n+1)H_n=0,
V=S Acal_n-(n+1)C Bcal_n-H_(n+1)W=0,
Dcal_n=(n+1)^2 P_(n+1)C-2P_n S=0 modulo p.

In the last two lines, the factors n+1 and (n+1)^2 remove the C terms modulo p. No divisibility of C is required. This correction matters for any future higher-depth calculation: an extra factor p in C cannot be assumed.

The controller completed check_correction.py with exit code 0 and sandboxed=true. It checked the formal boundary substitution with independent symbols and exactly these four affected instances:

| p | n | J_n modulo p | C modulo p | S,W,V modulo p |
|---|---|---|---|---|
| 3 | 2 | 0 | 0 | 0,0,0 |
| 3 | 5 | 0 | 0 | 0,0,0 |
| 5 | 4 | 3 | 2 | 0,0,0 |
| 5 | 9 | 3 | 2 | 0,0,0 |

The p=5 rows are exact counterexamples to the old C assertion. The formal substitution also checks Dcal=0 for arbitrary Legendre endpoints. These finite checks support the corrected algebra; the all-index statement follows from the proof of derivative transfer and the displayed substitution.

The correction checker loaded only the definitions from check_exact.py. It did not rerun that script's endpoint checks or overwrite certificate.json. The earlier successful formal normalization, direct checks at n=2,8, and complete seed vectors modulo 3 and 5 are preserved.

The actual numerator identity remains

Xcal_n=Qpart2_n+2^(n+1)V_n/(n!)^2,
Qpart2_n=2w_n S-(n+1)^2 w_(n+1)C.

The second-kind part is retained. Its proved general lower valuation bound remains v_p(Qpart2_n)>=-floor(log_p(n+1)); the correction supplies no additional universal depth for this term.

Consequently the conditional denominator theorem is unchanged: for odd p, n>=p, Dcal_n!=0, and V_(n mod p)!=0 modulo p,

v_p(q_n)=2v_p(n!)+v_p(Dcal_n)>=2v_p(n!).

The boundary residue -1 remains outside this unit-seed theorem. Its vanishing denominator congruence does not assert that the integer Dcal_n is zero. Eventual endpoint nonvanishing is inherited from the reviewed source, and the hypothesis Dcal_n!=0 remains explicit at individual indices.

The historical source reports actual cancellation at n=p-1. Its underlying proof was not separately inspected after the earlier symbolic-link safety refusal. It is not used in the conditional theorem. Neither the corrected congruences nor the finite checks prove a general higher-depth statement at that boundary.
