> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Agent 1: normalized prime-seed report

Exact execution: PASS. Independent researcher review: not yet supplied for this deliverable. All new files are under work/session_20261001_astra/agent1/.

The complete Vtilde=V/(n+1) seed vectors for the authorized list are:

| p | Vtilde residues, ordered by r | Zero residues |
|---|---|---|
| 5 | 4,1,2,2,0 | {4} |
| 7 | 4,2,6,4,4,6,3 | none |
| 11 | 4,5,7,8,3,4,2,7,2,5,5 | none |
| 13 | 4,3,5,9,7,10,9,8,11,2,12,6,2 | none |

Two exact constructions agree on every state coordinate at all 36 residue entries. The checker uses the 13 distinct scalar seeds 0 through 12 and adjacent polynomial data only as needed. It verifies eight formal identities and checks the original rational-minor endpoint expression, including second-kind terms, at the seeds in its n>=2 domain. No canonical HP degree sweep or additional prime list was used.

The proved exact factor identities are

    V=(n+1)Vtilde,
    Xcal=(n+1)(Qtilde+2^(n+1)Vtilde/(n!)^2),
    Dcal=(n+1)Dtilde.

The factor is cancelled over Q after proving the identities. V and Vtilde remain distinct. The transfer proof for Vtilde works at every residue, including n=-1 modulo p, without modular division by n+1.

Combining complete unit seeds with the written all-index transfer and strict second-kind separation gives, for each p=7,11,13,

    v_p(q_n)=2v_p(n!)+v_p(Dtilde_n)>=2v_p(n!)

for every n>=p with Dtilde_n!=0. The same statement holds at p=5 on residues 0,1,2,3. Eventual endpoint nonvanishing is inherited; it is not inferred from unit numerator seeds.

The sole zero is genuinely still present after normalization: n=4 modulo 5. Its state gives Dtilde_n=P_n modulo 5. The Legendre generating function proves the digit factors (1,2,3,2,1), so every P_n is a 5-adic unit. Therefore Dtilde_n is a unit on this residue and the endpoint is nonzero there. No further common factor of positive 5-adic valuation in Dtilde removes this normalized zero.

Let F=v_5(n!) and R=Vtilde+(n!)^2 Qtilde/2^(n+1). The unresolved depth is precisely v_5(R), with

    v_5(q_n)=max(0,2F-v_5(R))

when R!=0; if R=0 then q_n=1. The second-kind summand has valuation at least 2F-floor(log_5(n+1)). A bound for Vtilde's depth below that threshold would give strict separation; otherwise the complete R must be studied. No lifts are assumed.

Next attainable lemma: derive an all-index modulo-25 formula for the complete Vtilde on this residue, controlling discarded tails, then analyze any surviving zeros. Modulo-25 data alone would not establish an all-depth bound.

Both checkers returned exit code 0 with sandboxed=true. The residual checker reused the saved seeds and verified only the digit polynomial and exceptional-state algebra; it introduced no extra degrees or lifts.

Deliverables:

- NORMALIZED_PRIME_SEEDS.md: normalization, transfer proof, full seed table, denominator theorem, exceptional-residue proof, and precise remaining depth question.
- check_normalized_prime_seeds.py and normalized_prime_seed_certificate.json: reproducible exact seed and endpoint checks.
- check_normalized_five_residual.py and normalized_five_residual_certificate.json: reproducible exceptional-residue algebra.
- NORMALIZED_REPORT.md: this report.

Shared main-agent records and Agent 2's review were not modified. Their review status is not promoted by these calculations. The large-prime gate retains p>2n+4. No networking, larger prime search, global shrinking conclusion, or solution of e+pi is claimed.
