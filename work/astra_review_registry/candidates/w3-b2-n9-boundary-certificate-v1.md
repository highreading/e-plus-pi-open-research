> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact n=9 five-adic boundary certificate for the complete b=2 endpoint pair

Status: UNVERIFIED CANDIDATE
Author: worker_3
Content SHA256: 7825b5710d4038ce24a5a7a9661ee32e859f1e2d53af187b6df3e19fcd31a544

Status: author-checked finite certificate, submitted for independent review. No independent approval is asserted.

Use the complete b=2 endpoint pair (X_n,D_n) of the published two-chart endpoint identities, with rational approximant −X_n/D_n. The normalization is f_n=2^n/(n!)² and Z_n=X_n/[(n+1)f_n]. Identification with those original endpoint definitions is an explicit source dependency. The preserved exact reconstruction described below supplies the finite evaluation; the subsequent normalization, valuation, and fraction reduction are proved explicitly here.

At n=9, the complete endpoint reconstruction gives

D_9=−16288952758072398513390080,
X_9=30686517292378474786419257881060/321489,
f_9=1/257191200.

Consequently,

Z_9=2454921383390277982913540630484800,
Z_9/25=98196855335611119316541625219392≡17 (mod 625).

In particular v_5(Z_9)=2 and its leading unit Z_9/25 is 2 modulo five. The reduced approximant is

−X_9/D_9=1534325864618923739320962894053/261835956661996866283563171456.

Its displayed denominator is positive and coprime to its numerator. The valuations are

v_5(f_9)=−2, v_5(D_9)=1, v_5(X_9)=1, v_5(Z_9)=2, v_5(q_9)=0.

The endpoint-evaluation evidence is work/astra_20260929/worker_3/calculation_000140.py, file SHA-256 aa5148b0a450d45d2b20eebc24bab533066526398811df9f3c02d08289b524bd. This preserved finite program evaluates the original rational contractions only at n=9. It retains both complete exponential contractions at the unchanged truncation index n=9, both complete moment contractions, and the auxiliary correction. It also checks the exponential contractions against separate Rodrigues expansions. The returned execution succeeded, and the implementation was subsequently inspected. It was not rerun for this submission. The exact definitions and finite sums in that artifact are part of the endpoint-evaluation dependency and must be checked against the original formulas during independent review.

In the program’s recorded decomposition of the normalized Z_9 into complete exponential and moment contributions, with the auxiliary correction retained, those contributions are respectively 95 and 80 modulo 125. Their sum is 50 modulo 125. Thus the moment contribution is indispensable at this boundary: omitting it would produce the wrong valuation. These residues are supporting checks; the exact rational value above supplies the valuation certificate.

The normalization can be checked directly without any asymptotic input. Write N=30686517292378474786419257881060. Since 10f_9=1/25719120 and 25719120=80·321489,

Z_9=X_9/(10f_9)=80N.

This multiplication gives the stated integer. Its quotient by 25 is an integer congruent to 17 modulo 625, hence congruent to 2 modulo five. Therefore the five-adic valuation is exactly two. The displayed denominator of X_9 is prime to five, its numerator has valuation one, and D_9 has valuation one; these also agree with v_5(X_9)=v_5(10)+v_5(f_9)+v_5(Z_9)=1−2+2=1.

For an independent method of fraction reduction, meaning a second method within the author’s calculation, form the integers

N=30686517292378474786419257881060,
M=321489·16288952758072398513390080=5236719133239937325671263429120.

Then −X_9/D_9=N/M. Let

p=N/20=1534325864618923739320962894053,
q=M/20=261835956661996866283563171456.

The exact integer identity

(−49459949379320167987153799443)p+289829099726729897703995103580q=1

proves gcd(p,q)=1, and hence gcd(N,M)=20. Because M>0, q is the positive reduced denominator. Its residue q≡1 modulo five proves v_5(q)=0 directly. This agrees with max(0,v_5(D_9)−v_5(X_9))=0 and does not rely on the fraction library’s normalization.

Source dependencies and evidence: the original endpoint conventions are in work/astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md, registered payload ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d. The source-level finite reconstruction is the hashed calculation_000140.py above. Its successful execution and exact normalization result are recorded in work/astra_20260929/worker_3/note_000141.md, file SHA-256 f81b5e39cecf3550e0d2b30d54da4febb9f14866db9fb5e67e191fbcff3057ed. The integer reduction and Bézout identity are fully specified in this candidate and were checked in the subsequent successful exact calculation. Historical reported valuations were comparison evidence only.

Scope and self-audit: this is a finite certificate at n=9, with exact rational arithmetic throughout. Independent review must cover both the identification and evaluation of the complete original contractions and the displayed arithmetic certificate; checking only the final gcd would not verify endpoint reconstruction. No eventual nonvanishing or analytic error theorem is needed for the displayed finite nonzero denominator. The published residue-four theorem applies to n≥14 and gives v_5(q_n)=2v_5(n!)−1 there. At n=9 that expression equals one, whereas the actual valuation is zero, so its exclusion of n=9 is essential. This certificate neither extends that theorem’s range nor supplies a rationality or irrationality proof for e+pi.