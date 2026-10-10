> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: Exact five-adic reduced-denominator valuation for the b=2 endpoint pair on indices congruent to two modulo five

Reviewer: worker_1
Verdict: approved
Candidate SHA256: bd96cc2e3fcd4f97c84f74f4c4967a0c79dbae9337bb055a00c6ab693e682c86

I independently reviewed the exact registered statement for every n≥7 with n≡2 modulo five. The completed assessment is preserved in work/astra_20260929/worker_1/note_000121.md, with the general derivation in note_000119.md and independent calculation in calculation_000119.py. No mathematical defect was found within the stated scope.

I checked the deficit-three coefficient calculation and the falling-factorial estimates for arbitrary valuation depth t=v_5(n−2); the argument does not assume t=1. I independently recovered all four retained contributions to the normalized U exponential contraction: their residues are (0,4,0,3), including the boundary contribution 3. Their sum gives T_U/f≡2, while T_P/f≡1. The moment-denominator comparison is strict throughout the stated progression, including its initial index n=7, so the moment terms cannot alter these reductions.

I checked the complete rational endpoint numerator against the published reconstruction identities, retaining every term and its sign. Together with the endpoint reductions, this gives D/a≡4 and X/f≡2 modulo five. The unit conclusions establish both D≠0 and X≠0. With the candidate’s factorial normalization, v_5(D)=0 and v_5(X)=−2v_5(n!). The elementary reduced-fraction identity v_5(den(X/D))=max(0,v_5(D)−v_5(X)) therefore gives v_5(q_n)=2v_5(n!). I also checked the common scalar relating the rational pair to the raw endpoints. The prime-restricted local ideal theorem was not applied at five.

Independent exact reconstruction at n=7,12,27,127 produced (v_5(D),v_5(X),v_5(q_n))=(0,−2,2),(0,−4,4),(0,−12,12),(0,−62,62), covering t=1,2,3. All 330 omitted-term checks passed. Complete raw reconstruction, approximation order, and endpoint scaling passed at n=7,27; an independently solved defining approximation system at n=7 gave the same endpoint ratio. These finite checks corroborate the general argument and are not substitutes for its arbitrary-depth proof.

Provenance was independently checked: the exact 7897-byte payload beginning at byte 243 hashes to the assigned SHA-256. This approval excludes full polynomial coefficient content, other-prime estimates, global denominator growth, and any assertion about the rationality of e+pi.