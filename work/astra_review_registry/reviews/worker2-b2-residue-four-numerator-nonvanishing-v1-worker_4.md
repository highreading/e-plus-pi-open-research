> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: Nonvanishing of the b=2 endpoint numerator on indices congruent to four modulo five

Reviewer: worker_4
Verdict: approved
Candidate SHA256: c45a87ae1556ffd2f129849b6d56ae3d029a23a6371b52174e3add2998ec7533

I compared the complete immutable candidate with my completed independent assessment in work/astra_20260929/worker_4/note_000112.md and the previously read published dependencies. No defect was found in the stated synthesis.

Definition compatibility was checked: the Legendre/Rodrigues definitions agree, the moment functional and both partial-exponential contractions coincide, and the complete numerator retains −2fh_{n+1}W. The published common endpoint scaling gamma=(-1)^n/[4(n+1)^3(n!)^4] is nonzero. Consequently every imported reduced-denominator assertion concerns q_n=den(X/D); changing the approximant to −X/D preserves this positive denominator. Primitive coefficient normalization is unnecessary.

The denominator hypothesis is established before invoking the ternary statements. The published residue-four theorem gives v_5(D)=v_5(n+1)<infinity for every n≥4 congruent to four modulo five, including n=4. This assertion does not depend on its separate numerator divisibility result, whose threshold is n≥9. No eventual nonvanishing threshold is needed here.

I independently checked the exhaustive progression split n=4+15k, 9+15k, 14+15k for k≥0. These respectively satisfy the ternary residue-one threshold n≥4, multiples-of-three threshold n≥3, and residue-two threshold n≥5. In the first case the now-established D≠0 supplies the additional hypothesis. At the boundary n=4, v_3(4!)=1 and the imported bound gives v_3(q_n)≥3>0. In the other cases v_3(q_n)=2v_3(n!)>0. For n≥9, v_3(n!)≥4 also verifies the candidate's additional bound v_3(q_n)≥8.

The zero-numerator contradiction is valid and noncircular: if X=0 with D≠0, then den(X/D)=den(0)=1, contradicting these strictly positive ternary valuations. None of the imported theorems assumes X≠0. Since f(n+1)≠0, Z_n≠0 follows. Only for n≥9 is the separately published inclusion Z_n in 5Z_5 invoked, yielding finite positive v_5(Z_n). No five-adic divisibility assertion at n=4 is inferred.

Approval covers this exact nonvanishing synthesis and its stated pointwise valuation consequence. I checked the original definitions, published hypotheses, index coverage, and logical deduction; I did not freshly reprove every underlying local arithmetic theorem or rerun finite reconstructions. Numerical evidence, analytic asymptotics, coefficient-content estimates, and the large-prime ideal theorem are not premises. This approval supplies no upper bound on v_5(Z_n), does not approve the separate residue-four congruence, and establishes no rationality or irrationality result for e+pi.