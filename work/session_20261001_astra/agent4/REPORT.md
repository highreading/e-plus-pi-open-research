> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Agent 4 report

Assigned bounded audits completed; detailed review documents have been prepared in this directory.

- Inherited odd-dyadic denominator transfer and exclusion outside n=15 modulo 16: PASS.
- Inherited six-prime threshold/CRT synthesis: PASS.
- Draft (A): PASS for the intersection of these two unexcluded conditions: 146 classes modulo 397936, density 73/198968 among all integers.
- Draft (B): PASS as an eventual necessary condition for shrinking b=1 sequences: v_2(Ccal_n)=v_2(n-nu)>n/2 and successive tail indices satisfy m-n>=2^ceil(n/2). No infinite-subsequence exclusion follows from spacing alone.

INHERITED_SYNTHESIS_REVIEW.md records exact endpoint signs/scales, small P_0/P_1 handling, odd Delta and Qpart bounds, rational reduction, analytic nonvanishing, uniform margins, dependencies, and scope limits.

DRAFT_OBSERVATIONS_REVIEW.md supplies the uniform low-c unique-minimum proof, the exact strict rate inequality, CRT intersection, all eventual quantifiers, and the zero-numerator treatment. It additionally notes that the accepted p=5 seed/lift theorem already implies Ccal_n!=0 for ordinary integers n>=2; the spacing argument does not require that strengthening.

The independent checker check_inherited_rates_counts.py ran successfully (exit code 0, all_checks_pass=true). Its real outputs are audit_rate_count_certificate.json and audit_rate_count_stdout.txt. It confirms the inherited certificate, component counts 36+15+20+2=73, 146 classes modulo 24871, and 146 classes modulo 397936. Draft (B)'s exact comparison is 104000>(1+sqrt(2))^12.

All writes are confined to work/session_20261001_astra/agent4/. No network, installation, new primes, canonical HP degree computations, edits to inherited sources, or full dyadic-germ rerun were used. No new-prime or b=2 review is claimed; those await the main agent's separate assignment.


## Subsequent assignment: whole b=1 exclusion

Completed independent review: PASS. See B1_WHOLE_FAMILY_REVIEW.md for the theorem, proof checks, accepted dependencies, and limitations. This supersedes the earlier statement that the new-prime assignment was still pending; the preceding bounded reviews retain their original scopes.

The independent checker reconstructed 67 exact rational seeds and verified every one of the 1,050 coordinates for 210 rows at primes 41,43,59,67 against both saved constructions. All four complete zero sets are {1}. Fresh 32-term rational logarithm bounds verified the saved intervals, weighted sums, stopping comparisons, and margin 20453/200000. Execution returned exit code 0 with all_checks_pass=true. Evidence: check_whole_family.py, whole_family_checks.json, whole_family_check_stdout.txt.

Together with the explicitly reviewed all-index transfer, all-depth residue-one lift, actual numerator separation, reduced-q formula, eventual Delta nonvanishing, and full signed evaluated-error theorem, this proves liminf log|L_n|/n >=20453/200000>0 for this endpoint-matched b=1 family. It proves neither rationality nor irrationality of e+pi. No prime scan was extended and no original artifact was modified.


## Subsequent assignment: whole b=2 exclusion

Completed independent review: PASS for each requested component: normalization, all-index transfer including residue p-1, the ternary theorem/refinement, complete normalized seeds at 7 and 11, and whole-family synthesis. See B2_WHOLE_FAMILY_REVIEW.md for the proof, domain qualifications, evidence, and source dependencies.

The independent execution passed 14 formal identities and all 21 residue rows at exactly p=3,7,11, using 11 distinct scalar seeds. It reproduced Vtilde_0,Vtilde_1,Vtilde_2=4,16,5452 and the complete nonzero vectors at 7 and 11. Nine existing raw endpoint controls and twelve applicable finite denominator checks also passed. Evidence: check_b2_whole_family.py, b2_whole_family_checks.json, and b2_whole_family_check_stdout.txt; execution returned exit code 0.

Exact cancellation over Q gives V=(n+1)Vtilde and the actual endpoint (Qtilde+2^(n+1)Vtilde/(n!)^2)/Dtilde. For p=3,7,11, n>=p, and Dtilde!=0, strict numerator separation and final reduction give v_p(q_n)=2v_p(n!)+v_p(Dtilde_n)>=2v_p(n!). The accepted fixed-b theorem at b=2 supplies eventual endpoint and remainder nonvanishing.

The three simultaneous prime bounds yield liminf log|L_n|/n >= W-tau > log(27/25) > 2/27. In particular |L_n|>=exp(n/27) eventually; no effective initial index is claimed. This excludes shrinking primitive forms throughout this specific b=2 construction, without deciding rationality or irrationality of e+pi.

The completed b=1 audit documents, checkers, and certificates remain unchanged. No 5-adic lifting or prime-13 result is certified, and no prime search or canonical HP degree scan was extended. Original shared artifacts were preserved. This report update only appends the b=2 result.


## Subsequent assignment: growing arithmetic and endpoint content

Completed independent review: PASS for the monic Rodrigues factors, all-size derivative divisibility, elementary endpoint extension, signed minors, final clearer, exact gcd correspondence, automatic factorial divisor, and b=1/b=2 compatibility. Content removal passes with an explicit deficient-rank clarification. See GROWING_ARITHMETIC_CONTENT_REVIEW.md.

The saved independent checker executed successfully with exit code 0. All 12 formal checks passed. Its certificate and real execution record were read back and agree: growing_content_scale_checks.json and growing_content_scale_stdout.txt. The completed review was also read back. These checks supplement the all-size proofs; they do not establish growing-degree nonvanishing.

The automatic divisor A_b^2 divides every maximal high-row minor and both specified cleared monic endpoints. Consequently A_b^2 divides g on Y!=0. The empty-block b=1 convention is included. Deficient high-row rank makes this cofactor representative zero; it does not exclude other solutions of the original system. No division by zero content is permitted.

The exact scale relation is

    g=Crows*mu*d * (2n+1)!/[2(n+2)!(n!)^4] * gamma,
    gamma=gcd(|Lambda Nstar|,|Lambda Dstar|),
    Nstar=Qstar+2fVstar,
    Lambda=2^(n+1)(n+2)!(2n+1)!(n!)^2,
    f=2^n/(n!)^2.

The rational denominator must be retained. The positive rational endpoint content of (Nstar,Dstar) is gamma/Lambda, and q=Lambda|Dstar|/gamma.

GROWING_BOUND_OBSTRUCTION_DRAFT.md was read. The former strict residual-content target is not endorsed as attainable; its combined analytic audit remains Agent 2's scope. The algebraic divisor remains valid independently of that target. Agent 1's additional recurrence is not certified by this review.

Both completed family audits and their evidence remain preserved. No new prime or degree scan, networking, installation, external path, or modification of reviewed files was used. This update appends the growing-arithmetic conclusion without changing earlier report contents.
