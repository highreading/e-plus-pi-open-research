> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

Worker_4 final handoff, 29 September 2026.

**This research did not solve whether e+π is rational or irrational. No complete independently verified proof deciding the original problem was produced.** The strongest relevant published conclusion concerns failure of one specified matched b=2 approximation family to produce shrinking integer-coefficient forms. Its scope must remain separate from the original rationality question.

Worker_4 is ending research at the existing checkpoint. The final assigned source-identification check is recorded as complete in note_000182.md, and the resulting three-term-filter candidate is registered but independently unreviewed. The earlier whole-family synthesis review is complete, accepted, and published. No additional calculation, historical audit, or claim submission was performed for this closing handoff.

All verification statuses below refer to the registry supplied with the closing instruction. A published claim certifies only its exact reviewed statement, including its hypotheses and exclusions. An author check, a successful computation, and registration of a candidate are different forms of evidence. Registry payload hashes must also be distinguished from hashes of enclosing files containing metadata.

The principal preserved checkpoint documents are [the completed synthesis assessment](note_000134.md), [the arithmetic dependency audit](note_000119.md), and [the final filter submission checkpoint](note_000182.md). Earlier notes remain preserved, including their explicitly superseded statements.

The endpoint notation used throughout this work is as follows. Let X_n and D_n denote the complete rational contractions in the published b=2 endpoint reconstruction. Put f_n=2^n/(n!)² and γ_n=(-1)^n/[4(n+1)^3(n!)^4]. In the raw normalization, A_raw(1)=γ_n X_n and B_raw(1)=C_raw(1)=γ_n D_n. Whenever D_n≠0, the matched approximation to T=e+π is ρ_n=-X_n/D_n=p_n/q_n in lowest terms, with q_n>0. The ratios X_n/D_n and -X_n/D_n have the same positive reduced denominator.

Write v_p for the rational p-adic valuation, normalized by v_p(p)=1, and r_p(n)=v_p(n!). The normalized numerator is N_n=X_n/f_n. On the five-adic residue-four progression, Z_n=X_n/[f_n(n+1)]. These definitions retain both partial-exponential contractions and the correction term -2f_nη_nW_n in X_n. Omitting those terms changes the problem. The complete definitions and reconstruction are in [b2-two-chart-actual-denominator-identities](../../astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md).

The following local denominator statements are published. Conditional rows require D_n≠0; the separate eventual-nonvanishing theorem supplies that condition for sufficiently large n, without an effective threshold.

| Prime and index range | Published conclusion | Exact source |
|---|---|---|
| p=3, n≥3, n≡0 mod 3 | v_3(D_n)=0, v_3(X_n)=-2r_3(n), and v_3(q_n)=2r_3(n) | [Ternary endpoint and content theorem](../../astra_review_registry/verified/b2-ternary-endpoint-denominator-and-content-v1.md) |
| p=3, n≥4, n≡1 mod 3 | N_n∈1+3Z_3 and D_n∈3Z_3; if D_n≠0, v_3(q_n)=2r_3(n)+v_3(D_n)≥2r_3(n)+1 | [Ternary residue-one theorem](../../astra_review_registry/verified/worker4-b2-ternary-residue-one-conditional-denominator-v1.md) |
| p=3, n≥5, n≡2 mod 3 | v_3(q_n)=2r_3(n), under the endpoint hypotheses of the record | [Ternary residue-two theorem](../../astra_review_registry/verified/worker2-b2-ternary-residue-two-exact-denominator-v1.md) |
| p=5, n≥5, n≡0 mod 5 | D_n is a unit, N_n≡3 mod 5, and v_5(q_n)=2r_5(n) | [Five-adic multiples theorem](../../astra_review_registry/verified/b2-five-adic-endpoint-denominator-v1.md) |
| p=5, n≥6, n≡1 mod 5 | D_n is a unit, N_n≡4 mod 5, and v_5(q_n)=2r_5(n) | [Five-adic residue-one theorem](../../astra_review_registry/verified/worker4-b2-five-adic-residue-one-exact-denominator-v1.md) |
| p=5, n≥7, n≡2 mod 5 | D_n is a unit, N_n≡2 mod 5, and v_5(q_n)=2r_5(n) | [Five-adic residue-two theorem](../../astra_review_registry/verified/worker4-b2-five-adic-residue-two-exact-denominator-v1.md) |
| p=5, n≥8, n≡3 mod 5 | If D_n≠0, v_5(q_n)=2r_5(n)+v_5(D_n)≥2r_5(n)+1 | [Five-adic residue-three theorem](../../astra_review_registry/verified/w3-b2-five-residue-three-loss-v1.md) |
| p=5, n≥9, n≡4 mod 5 | v_5(D_n)=v_5(n+1), and v_5(q_n)=max(0,2r_5(n)-v_5(Z_n)); the published forced cancellation gives an upper bound v_5(q_n)≤2r_5(n)-1 | [Residue-four cancellation theorem](../../astra_review_registry/verified/main-b2-five-adic-residue-four-cancellation-v1.md) |
| p=5, n≥14, n≡4 mod 5 | Z_n≡20 mod 25, hence v_5(Z_n)=1 and v_5(q_n)=2r_5(n)-1 | [Exact residue-four loss theorem](../../astra_review_registry/verified/w3-b2-five-residue-four-loss-v1.md) |

Worker_4 authored the ternary residue-zero and residue-one records and the five-adic residue-zero, residue-one, and residue-two records. Worker_1 independently reviewed those records except for ternary residue one, which Worker_2 reviewed. The other rows are published dependencies, not additional claims authored or independently reproved by Worker_4 during closing.

The five-adic denominator proof on n≡4 mod 5 establishes D_n≠0 already for n≥4. Its normalized-numerator formula has the later threshold stated above. The exact loss theorem starts at n≥14 and must not be applied to n=4 or n=9. In particular, the boundary computations for those two indices remain separate evidence and have their own pending candidates.

The identification of the local ratio with the analytic matched endpoint, and eventual D_n≠0, are recorded in [w3-b2-eventual-d-nonzero-v1](../../astra_review_registry/verified/w3-b2-eventual-d-nonzero-v1.md). The identification uses a common nonzero scalar and introduces neither an index shift nor a change in the reduced denominator. It does not supply a numerical threshold for every eventual assertion.

Several additional published results explain the limits of these arithmetic statements.

The corrected auxiliary matrix on X∈3Z_3 is coefficientwise congruent to [[1,0],[1,2],[2,0]] modulo 3. Its ordered maximal minors for row pairs (12,13,23) are (2,0,2). Therefore its first minor is a unit throughout that disk, including X=-3/2, and v_3(Ω_n)=0 for nonnegative integer n divisible by 3. This is the exact normalization in which Ω_n is the gcd of the three unscaled maximal minors. The authoritative record is [b2-ternary-zero-diredacted_historical_name](../../astra_review_registry/verified/b2-ternary-zero-diredacted_historical_name.md), independently reviewed by Worker_1 and published with payload SHA-256 627b84db31ceb70a32d19d4ed78056281b5ae9e2bcc79510cfc396a8bc76364c.

The earlier third row (0,0) in note_000002.md is withdrawn. Its source was an incorrect constant coefficient in H_2: the correct polynomial is H_2(x)=x²-4x+4, not x²-4x+6. The corrected matrix and its certificate have already passed independent review. The stale resume instruction asking for this reconciliation has therefore been satisfied and must not trigger another audit.

An auxiliary unit minor does not eliminate small-prime cancellation in primitive endpoints. For n≥3 divisible by 3, let ν be the minimum valuation of all coefficients in the specified raw triple, r=v_3(n!), and L=floor(log_3 n). The published reconstruction bounds are -6r-L≤ν≤-6r. If c=-6r-ν, then 0≤c≤L; primitive endpoint valuations are c and 2r+c, so their common ternary factor has valuation c. The factor cancels from the rational ratio, leaving v_3(q_n)=2r.

The finite example n=12 makes the distinction concrete: c_3(A_raw)=-31, c_3(B_raw)=-20, c_3(C_raw)=-29, and the raw endpoint valuations are -30 and -20. Primitive endpoint valuations are 1 and 11, with endpoint gcd 73920, although Ω_12=2. The independently reviewed finite certificate is [worker1-b2-four-ternary-endpoint-certificates-v1](../../astra_review_registry/verified/worker1-b2-four-ternary-endpoint-certificates-v1.md); the author’s detailed supplement is [note_000045.md](note_000045.md).

The analogous five-adic content extension on n≥7, n≡2 mod 5 is published in [worker4-b2-five-adic-residue-two-conditional-content-v1](../../astra_review_registry/verified/worker4-b2-five-adic-residue-two-conditional-content-v1.md), reviewed by Worker_1. With r=v_5(n!), L=floor(log_5 n), and the same definition of ν, it gives -6r-L≤ν≤-6r and primitive endpoint gcd valuation c=-6r-ν∈[0,L], conditional on the specified raw endpoint valuations. Those endpoint hypotheses are supplied by the separately published residue-two theorem. The lower coefficient estimates and the conditional upper/content conclusions remain distinguished in the exact approved statement. Neither content theorem determines ν exactly for every index.

For odd-prime interpolation, the coefficientwise term estimate uses k=floor((u+2v)/p) and the lower bound k-v_p(k!). A sufficient block cutoff at precision p^d is K_p(d)=max(1,ceil((p-1)(d-1)/(p-2))); retaining u+2v<pK_p(d) suffices. The optimal uniform individual-summand block cutoff is K*_p(d)=1+max{k≥0:k-v_p(k!)<d}. This optimum concerns divisibility of individual summands across the stated derivative orders, not cancellation in their sum. Worker_4 independently reviewed [odd-prime-interpolation-tail-cutoff-v1](../../astra_review_registry/verified/odd-prime-interpolation-tail-cutoff-v1.md).

Worker_4’s separate [odd-prime-cutoff-sharpness-and-logarithmic-search-v1](../../astra_review_registry/verified/odd-prime-cutoff-sharpness-and-logarithmic-search-v1.md), independently reviewed by Worker_1, proves that the sufficient cutoff is attained at infinitely many precisions and gives an explicit search interval of O_p(log d) block indices for the optimal cutoff. The supporting author computation checked p=3,5,7,11,13 and d=1,…,1000, totaling 5,000 finite cases. Those checks supplement the proof; they do not prove optimality of a summed tail or estimate an actual endpoint denominator.

Worker_4 completed five formal independent reviews, all now published. These reviews are not pending work:

| Reviewed claim | Scope of Worker_4’s completed review |
|---|---|
| b2-two-chart-actual-denominator-identities | Exact reconstruction and scaling, both local ideal transformations, prime threshold p>2n+2, chart coverage, complete numerator, and zero cases subject to D≠0. No quantitative denominator growth bound was certified. |
| odd-prime-interpolation-tail-cutoff-v1 | Coefficientwise estimate, convergence of the omitted sum, sufficient cutoff, and optimal uniform individual-summand cutoff, including boundary cases. |
| worker1-b2-four-ternary-endpoint-certificates-v1 | Independent complete reconstruction at n=3,6,9,12, rational-system uniqueness, endpoint ratios, and n=12 primitive normalization. This is a finite certificate. |
| worker2-b2-residue-four-numerator-nonvanishing-v1 | Published dependency definitions and thresholds, all three ternary residue cases, D≠0, and the zero-numerator contradiction, including n=4. No valuation upper bound was inferred from nonvanishing. |
| w3-b2-whole-family-obstruction-v1 | Common reduced denominator, residue coverage, arithmetic thresholds, digit bounds, the exact published transfer theorem, and passage to primitive forms and nonzero integer multiples, retaining H4 explicitly. |

The nonvanishing review’s exact published statement is [worker2-b2-residue-four-numerator-nonvanishing-v1](../../astra_review_registry/verified/worker2-b2-residue-four-numerator-nonvanishing-v1.md). Its conclusion is X_n≠0 on n≥4, n≡4 mod 5. The later upper control of v_5(Z_n) for n≥14 comes from the separate exact loss theorem, not from this nonvanishing argument. Older notes calling the residue-four loss unresolved are superseded within that published range.

The published family obstruction uses κ=1+√2, G=3√5, and C=4π/κ³. The fixed-b transfer theorem, specialized to the same b=2 matched ratio, gives the eventual error law

T-ρ_n = (-1)^n C κ^(-2n)(1+o(1)).

The exact source checked during the completed synthesis audit is [worker2-fixed-b-projection-and-error-transfer-v2](../../astra_review_registry/verified/worker2-fixed-b-projection-and-error-transfer-v2.md). The ordinary Padé prefactor is also independently reviewed and published in [worker3-ordinary-pade-prefactor-v1](../../astra_review_registry/verified/worker3-ordinary-pade-prefactor-v1.md). The stale reminder that the prefactor is awaiting audit is superseded by those records.

Combining the local valuations gives, eventually and under the synthesis’s explicit residue-four premise H4,

q_n ≥ G^n/(1125 n^4).

Since G>κ², it follows that |q_n(T-ρ_n)|→∞. The same obstruction applies to the specified primitive matched integer-coefficient forms and their nonzero integer multiples. It does not cover arbitrary combinations across indices or approximation degrees varying with n.

The exact reviewed synthesis is [w3-b2-whole-family-obstruction-v1](../../astra_review_registry/verified/w3-b2-whole-family-obstruction-v1.md), payload SHA-256 11539d8ac13528b29c5f4b8eda1eecfaa7e9ccad01860739b3f506d8de26a0d5. Its conditional wording is preserved. H4 now has separate published support, but that does not authorize editing the immutable reviewed statement. The arithmetic threshold n≥14 is not an effective threshold for the eventual analytic law, uniqueness, or endpoint nonvanishing.

The finite computations are preserved separately from these all-index theorems. Important author evidence includes the following:

| Preserved record | Computation and results | Verification limit |
|---|---|---|
| [note_000045.md](note_000045.md) | Direct rational moment reconstruction and coefficient witnesses at n=12 | The related four-index certificate was independently reviewed; the note also preserves author detail. |
| [note_000053.md](note_000053.md) | Full n=5,10 reconstruction; v_5(q)=2,4 | Finite author computations are distinct from the independently reviewed general theorem. |
| [note_000067.md](note_000067.md) | n=4,7,10,28; triples (v_3(D),v_3(X),v_3(q))=(4,-2,6),(3,-4,7),(1,-8,9),(1,-26,27) | The general residue-one proof is published; its reviewer explicitly did not independently check n=28. |
| [note_000075.md](note_000075.md) | n=6,11,16,21,26; v_5(q)=2,4,6,8,12; full order conditions and scaling checked | Preserved author execution evidence. |
| [note_000085.md](note_000085.md) | n=7,12,27; v_5(q)=2,4,12; boundary terms retained | Preserved author execution evidence; the separate general theorem is published. |
| [note_000101.md](note_000101.md) | Seven residue-four indices, with full polynomial reconstruction only at n=9,24 | The composite dataset has not received a separate independent approval. |

The seven-index residue-four table is retained here to make its exceptional n=9 behavior explicit. The v_5(X) column is an arithmetic conversion from the saved normalized-numerator valuations, subtracting 2v_5(n!).

| n | v_5(D_n) | v_5(X_n) | v_5(Z_n) | v_5(q_n) |
|---:|---:|---:|---:|---:|
| 9 | 1 | 1 | 2 | 0 |
| 14 | 1 | -2 | 1 | 3 |
| 19 | 1 | -4 | 1 | 5 |
| 24 | 2 | -5 | 1 | 7 |
| 29 | 1 | -10 | 1 | 11 |
| 49 | 2 | -17 | 1 | 19 |
| 124 | 3 | -52 | 1 | 55 |

Every computed X_n and D_n was nonzero. At n=9, a five-adic unit reduced denominator alone implies only v_5(Z_9)≥2; the exact value 2 comes from the complete numerator computation. The raw scaling on this progression has valuation v_5(γ_n)=-4r_5(n)-3v_5(n+1). Omitting the second term gives incorrect raw endpoint valuations.

For reproducibility of the table, the recorded leading units modulo 625 are defined by removing the exact power of five. The Z units are 17,499,344,354,129,254,329; the D units are 109,399,158,381,7,189,6, in the displayed index order. The D unit divides by 5^v_5(D), not by n+1. Full reconstruction gave raw coefficient minima -9 at n=9 and -28 at n=24, hence primitive endpoint gcd valuations 3 and 1 respectively.

The retained executable is [calculation_000100.py](calculation_000100.py), 9,598 bytes, SHA-256 3d153b7ea4a1b6b6006eaf0a44b3227fffeaadb38f2d30008e9f7fa12827eeb3. The malformed hash transcription in note_000105.md is withdrawn. The successful read-only hash check in step 108 explicitly did not execute the reconstruction. Historical execution is documented by note_000101.md; a separate raw stdout artifact was not located. The source’s aggregate assertion checks reconstruction and normalization, while comparisons with proposed predictions are reported separately. An aggregate PASS must not be represented as checking those comparisons automatically.

Five Worker_4 supplementary candidates remain independently unreviewed. All are recorded as awaiting reviewer assignment in the closing registry. None should be copied into verified records without the required independent review and publication gate.

| Candidate | Exact registered payload SHA-256 |
|---|---|
| [worker4-b2-adjacent-determinant-growth-v1](../../astra_review_registry/candidates/worker4-b2-adjacent-determinant-growth-v1.md) | f5a8cdc9ca305b306e08758dec573beec4f617aa94bcdc21f1f243c2d7abdfd2 |
| [worker4-rational-target-growth-countermodel-v1](../../astra_review_registry/candidates/worker4-rational-target-growth-countermodel-v1.md) | c76bd9a3bb0782ba45ef5b2a5dd2bff28a0f9b092e6dd476f3dbb2984b81fc1e |
| [worker4-fixed-rational-weight-cancellation-v1](../../astra_review_registry/candidates/worker4-fixed-rational-weight-cancellation-v1.md) | 8901aa93f675fbd58e3c5a13b2cb1576cc5166615ac585d5ac05aac0181a3d09 |
| [worker4-multiple-root-filter-rate-v1](../../astra_review_registry/candidates/worker4-multiple-root-filter-rate-v1.md) | 0f1f2831c9e5f5d6b8b9f225786387401dc32496832ef055bb9fc3dadb5dfd98 |
| [worker4-b2-three-term-filter-denominator-v1](../../astra_review_registry/candidates/worker4-b2-three-term-filter-denominator-v1.md) | 41527527f21a77d80f491516b9a2ca7f0386a152bd1afac6cfdc2ebbec48cbd0 |

The adjacent-determinant candidate deduces exponential growth of the integer determinants of consecutive reduced approximants from the stated eventual error law and denominator lower bound. It would imply eventual distinctness and exclude determinants ±1. It gives no effective threshold and does not establish irrationality. The rational-target countermodel constructs reduced approximants with denominators 7^n satisfying analogous alternating exponential error and divergent integer-form and determinant behavior while converging to a rational target. It is a scope counterexample for those abstract estimates, not a construction satisfying the matched endpoint equations. Both candidates have completed author checks only.

The fixed-weight candidate sets z=-κ^(-2)=-3+2√2. For fixed rational weights c_j with sum one, put W(t)=Σc_jt^j. Cancellation of the leading matched error requires W(z)=0. Its minimal polynomial is t²+6t+1, whose value at t=1 is 8. The proposed result is that the least common coefficient denominator must be divisible by 8; integer weights with sum one cannot cancel the leading term. For degree at most two, the rational weights are uniquely (1,6,1)/8. The claim also supplies a rational counterexample in which this cancellation leaves an error proportional to z^n/n², with the original exponential rate. Leading-term cancellation therefore supplies only a little-o improvement under the leading asymptotic alone.

The multiplicity candidate extends that statement: multiplicity at least m requires degree at least 2m and a coefficient denominator divisible by 8^m. Its conditional error-rate conclusion assumes an expansion through n^(-m-1), with remainder o(n^(-m-1)), a nonzero 1/n coefficient, and exact filter-root multiplicity m. Under those hypotheses the filtered error retains the same exponential rate with a polynomial loss. A first-order expansion alone does not justify that conclusion. The required expansion has not been established here for the actual matched approximants. Exact author calculations for m=1,2,3,4 gave degrees 2,4,6,8 and coefficient denominators 8,64,512,4096; their source is [calculation_000174.py](calculation_000174.py). The malformed identifiers in note_000178.md are withdrawn; the table above gives the registry’s exact payload hash.

The latest three-term-filter candidate is the completion of the final assigned source check. Define ρ̃_n=(ρ_n+6ρ_{n+1}+ρ_{n+2})/8, and let Q_n be its positive reduced denominator. Its registered statement assumes n≥11, n≡2 or 11 mod 15, and D_nD_{n+1}D_{n+2}≠0. It records the exact identities

v_3(Q_n)=v_3(q_{n+2}),

v_5(Q_n)=v_5(q_{n+1}) when n≡2 mod 15,

v_5(Q_n)=v_5(q_{n+2}) when n≡11 mod 15.

Consequently, on those progressions it proposes v_3(Q_n)≥2v_3(n!)+3 and v_5(Q_n)≥2v_5(n!)+1. The proof uses a unique summand with strictly smallest local valuation after accounting for the coefficient 6. The published residue-four upper bound suffices for this comparison; the sharper H4 congruence is unnecessary. The existing endpoint-identification theorem supplies the three nonvanishing assumptions eventually, without an effective threshold.

The source comparison for this candidate is complete according to the recorded checkpoint, and the controller confirms registration. Independent approval is still absent. In particular, no lower bound for |T-ρ̃_n| has been proved here. The denominator result alone does not show that Q_n|T-ρ̃_n| grows, shrinks, or stays away from zero. It does not repair the missing higher error expansion and does not decide the rationality of T.

The remaining limits of the work are precise. The primitive coefficient-content bounds are intervals rather than exact formulas in general. Eventual analytic and nonvanishing assertions have no effective common threshold in these records. The filtered constructions lack the needed quantitative error information. The five supplementary claims have no independent verdict. None of these gaps is being assigned as new work during closure.

At the supplied team snapshot, the digit-refinement claim w3-b2-residue-one-digit-refinement-v1 is already independently approved at payload SHA-256 67157f3a37dc36b6c872fc03448fe3b2c715e965eef8100459c5806698ac488e but is not yet marked published. That is an existing lead publication item, not an outstanding Worker_4 audit. The n=4 and n=9 boundary certificates remain awaiting assignment. This handoff does not approve them or request new audits.

Reproduction should begin with the exact linked records and preserved sources. The principal historical originals actually read by Worker_4 were [literature_update_and_b2_analytic_certificate.md](../../session_20260927/literature_update_and_b2_analytic_certificate.md), [hp_b2_cubic_maximal_minor_gate.md](../../session_20260927/hp_b2_cubic_maximal_minor_gate.md), [hp_b2_contiguous_endpoint_arithmetic.md](../../session_20260913/hp_b2_contiguous_endpoint_arithmetic.md), and [hp_b2_endpoint_attempt.md](../../session_20260913/hp_b2_endpoint_attempt.md). Their contents were treated as research data. The reading ledger, rather than an old request list, records completed ranges and hashes.

For a separately authorized reproduction, use exact integer and Fraction arithmetic, or the already available SymPy library, within the existing compute isolation. Check every polynomial order condition and common endpoint scale, retain the complete contractions and their boundary terms, and compute the positive reduced denominator only after full rational reduction. The known calculation_000100.py can reproduce the seven-index table, including full polynomials only at n=9 and n=24. Calculation_000174.py reproduces the finite multiplicity checks. The source code should be supplied to the permitted compute action without network access or subprocesses; any output must remain in the role’s permitted directory. Historical scripts that write into source directories must not be run unchanged. No reproduction is requested or running as part of this closing handoff.

All existing material is preserved. The controller’s finish_closing action saves this report as Worker_4’s FINAL_REPORT.md and ends the role. Pending candidates remain explicitly unverified, and the original rationality question remains unsolved by this work.