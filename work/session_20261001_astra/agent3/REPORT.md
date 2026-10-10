> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Agent 3 report: bounded prime extension succeeds

Status: SUCCESS_READY_FOR_INDEPENDENT_AUDIT.

The newly certified primes are 41,43,59,67. Each has complete Ccal zero set exactly {1}. Together with the reviewed primes 5 and 13 they give

    S={5,13,41,43,59,67},
    W=sum_(p in S) 2log(p)/(p-1),
    W-2log(1+sqrt(2)) >= 20453/200000 > 0.

The inequality is certified by exact rational logarithm bounds, not floating-point logs. Combining the complete finite seeds with the reviewed general transfer, all-depth residue-one theorem, and evaluated-error theorem yields

    v_p(q_n)>=2v_p(n!) for every p in S,
    liminf log|L_n|/n >=20453/200000>0.

The valuation assertions hold for n>=67 whenever Delta_n!=0; the accepted analytic theorem supplies eventual Delta nonvanishing. Thus the assembled result excludes every shrinking subsequence of this b=1 family, on both parities, independently of the dyadic and ternary roots. It does not solve rationality or irrationality of e+pi. New certificates and the proof assembly require independent audit before promotion to an independently reviewed result.

## Scan and stopping record

The predeclared list was all 38 primes from 23 through 199 in increasing order. The exact tested zero sets were:

| p | Z_p |
|---:|---|
| 23 | {1,18} |
| 29 | {1,14} |
| 31 | {1,12} |
| 37 | {1,23} |
| 41 | {1} |
| 43 | {1} |
| 47 | {1,27} |
| 53 | {1,3,32} |
| 59 | {1} |
| 61 | {1,33,40} |
| 67 | {1} |

After adding 59 the accumulated weight was still below the target; its certified upper bound is 1737599/1000000, whereas tau>=1762747174039/1000000000000. Adding 67 produced the first strict surplus. Scanning stopped immediately at 67. The remaining 27 candidates, starting at 71 and ending at 199, were not tested. No conclusion about their zero sets or an infinite density of successful primes is drawn.

## Verification and proof boundaries

The checker computed 491 complete modular scalar rows. For the four selected new primes it compared every H,K,Acal,Bcal,Ccal entry against a distinct construction using ordinary integer Legendre coefficients and exact rational factorial functionals: 210 rows, 1050 coordinate comparisons, all passing. It stores both residue constructions and exact rational scalar values for residues 0 through 66.

The old full atlas was neither overwritten nor rerun. Existing 5/13 evidence and the general transfer and all-depth lift are cited within the reviewed scope of work/session_20260927/hp_b1_uniform_5_13_independent_review.md. No canonical HP nullspace, actual-degree scan, network access, installation, or historical/shared-file edit was used.

Local validation checked certificate and source hashes, all stored determinant identities, selected rational-to-modular reductions, complete zero sets, the stopping prefix, and every saved logarithm interval using fresh 24-term rational sums. This validation did not recompute or extend the scalar scan and is not an independent researcher audit.

The proof explicitly uses the actual quotient Ucal_n/Delta_n. Away from residue one, the factorial numerator term has uniquely least valuation -2v_p(n!). On residue one with a=v_p(n-1), the all-depth lift gives v_p(Ccal_n)=a, while both H_n and K_(n+1) are divisible by p^a. Therefore Delta_n is divisible by p^a, and actual reduction gives

    v_p(q_n)=2v_p(n!)+v_p(Delta_n)-a>=2v_p(n!).

This compensation is essential. Finite seed zeros alone do not supply the all-depth lift, and the argument does not assume Legendre endpoints are units. Eventual Delta nonvanishing and the evaluated-error asymptotic remain explicit analytic dependencies.

## Deliverables

All new files are under work/session_20261001_astra/agent3/:

- PREDECLARATION.md — fixed candidate list and stopping rule, written before computation.
- check_bounded_prime_extension.py — deterministic exact checker; no external packages required.
- exact_certificate.json — complete tested scalar rows, both constructions for selected primes, exact rational seeds, rate history, and provenance hashes.
- certificate_summary.json — compact zero sets, selected primes, untested list, and exact rate bounds.
- stored_certificate_validation.json — local validation receipt.
- PROOF_DRAFT.md — finite-list-to-all-index proof including actual reduction and primitive-form divergence.
- REPORT.md — this report.

The exact certificate has 142258 bytes and SHA-256

    a422ac8d69dc74d4f15ce26906216ce4ddbf925e0fd60c676b8c6a59c8399e48

For an auditor, reproduction from the research workspace root is:

    python3 work/session_20261001_astra/agent3/check_bounded_prime_extension.py --verify

This deterministic verification regenerates the declared stopping prefix and compares the saved certificate and summary without writing. It was not additionally executed during this task: the original exact run and the separate saved-payload validation already passed. Independent audit should assess the two constructions, the transfer/lift dependencies, and the finite-rate-to-primitive-form implication. No additional prime scan is requested.
