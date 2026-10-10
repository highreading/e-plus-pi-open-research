> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Background and results map

## Objective and evidence standards

Determine unconditionally whether the actual real number e+pi is irrational or rational. No solution is present in the material examined. Algebraicity and transcendence are different questions; the older README's objective does not replace the current task.

An unconditional sufficient criterion is an infinite sequence of nonzero integer forms q(e+pi)-p tending to zero. Finite searches, numerical relations, conjectures, and small normalized errors without reduced-denominator control do not establish this criterion.

Historical FULL PASS means an independent mathematical review within its specified scope, not formal proof-assistant verification. Below, inherited results remain distinguished from checks performed during this reconstruction.

## Material examined

Read completely: SESSION_20260927.md; E_PI_RESEARCH_REPORT_20260927.md; CLOSING_VERIFICATION_REGISTER_20260927.md; E_PI_RESEARCH_REPORT_20260913.md; CLOSING_VERIFICATION_REGISTER_20260913.md.

Read targeted beginnings and recent tails of README.md, ROUTE_STATUS.md, ROUTE1_MASTER_CAPACITY.md, and research_log.md. Their recent tails retain the old matched-integral ledger; they do not contain a later solution. The September closing reports supersede older route-status descriptions within their mathematical scope.

Read the following proof or review texts directly:

- work/session_20260913/raw_all_parity_raw_exclusion.md
- work/session_20260913/hp_b2_contiguous_endpoint_arithmetic.md
- work/session_20260927/hp_b1_ternary_actual_denominator.md
- work/session_20260927/hp_b1_prime_seed_transfer_and_closed_atlas.md
- work/session_20260927/hp_b1_uniform_5_13_independent_review.md
- work/session_20260927/hp_b1_dyadic_independent_root_review.md
- work/session_20260927/hp_b1_odd_dyadic_actual_numerator.md
- work/session_20260927/hp_b1_odd_dyadic_germs_independent_review.md
- work/session_20260927/hp_b1_closed_prime_odd_index_restriction.md
- work/session_20260927/hp_b2_cubic_maximal_minor_gate.md
- work/session_20260927/fixed_exponential_degree_error_theorem.md
- work/session_20260927/fixed_exponential_degree_error_independent_review.md

This is a bounded reconstruction, not a fresh audit of every historical proof, script, or certificate. No old certificate has been rerun in the present reconstruction.

## Established background

The transcendence of e and pi separately does not determine their sum. At least one of e+pi and e*pi is transcendental: otherwise e and pi would satisfy a quadratic over the algebraic numbers. This disjunction does not identify the sum. Schanuel's conjecture would imply algebraic independence of e and pi and hence transcendence of their sum; that implication is conditional.

The archived literature reviews report no applicable unconditional solution. Their source-specific reading boundaries must be retained. Network access is disabled for this session, so these reports are not a fresh literature survey.

## Closed or rigorously obstructed constructions

### Original raw family

The September 13 assembly proves divergence of every sufficiently large actual primitive raw form, with both parities and final endpoint gcd included. Its lower bound is exp(3n/200)/(4 sqrt(2) C n^10), C=25839289479611181, beyond an unspecified finite analytic threshold.

Status: inherited reviewed theorem; assembly read here, all underlying analytic and seed certificates not freshly replayed. It excludes subsequences and nonzero integer multiples of those particular forms. It does not exclude new linear combinations or a different construction. Do not repeat its degree scans.

### Degree-one matched Hermite–Padé construction

Use F(z)=4 arctan(z/(2-z)), F(1)=pi, degree caps (n,1,n), and matched endpoints B(1)=C(1)=Y. The all-even subsequence is excluded by reviewed lower bounds for the actual reduced q at primes 2,5,13 and the full endpoint error. Do not reopen the even construction.

The existing rational companion to e has reviewed error of first factorial order, log|e-r_n*|=-n log n+n+o(n). Seeking second factorial decay for this same companion is a closed target. This is inherited from the September 13 report and register, without a fresh reading of its full proof here.

### Original matched-integral program

Its sufficient synchronized target is limsup log(c_m Delta_m g_m)/(6m)>T, with T=1.1561471519642446... . The booked lower gain remains r1=0.1365141682948128... . Gains must concern the same indices, with overlap removed.

The recent historical tails describe genuine counterexamples to auxiliary-carrier interpretations: at (m,p)=(13,11), actual content has valuation 2 while the normalized carrier coordinates are units. An additional first integral Witt digit explains the discrepancy but books no new positive mass. These statements are inherited from the historical summaries; their original exact certificates were not reread here.

Fixed layers, thin supports, and larger formal identities do not automatically supply the missing positive weighted gain. The route is unresolved, not globally excluded.

## The exact live endpoint arithmetic

### b=1

Keep the source notation local. Here K_{n+1}=H_{n+1}(1)+H'_{n+1}(1)/(n+1), not the b=2 second-derivative combination.

The actual endpoint is X/Y=U_n/Delta_n, where

U_n=Qpart_n+2^(n+1) Ccal_n/(n!)^2,
Ccal_n=K_{n+1} Acal_n-H_n Bcal_n,
Qpart_n=2K_{n+1}Q_n-(n+1)H_n Q_{n+1},
Delta_n=(n+1)P_{n+1}H_n-2P_n K_{n+1}.

The positive reduced denominator satisfies v_p(q_n)=max(0,v_p(Delta_n)-v_p(U_n)) whenever Delta_n is nonzero. Cancellation between the two terms of U_n must be addressed before using this formula. Eventual nonzero endpoints follow from the accepted analytic theorem.

Reviewed arithmetic inputs:

- For n>=5, n=2 mod 3, v_3(q_n)=2v_3(n!). The n=2 exception is real: q_2=28.
- The full residue vector (H,K,Acal,Bcal,Ccal) transfers modulo every odd prime, with the residue p-1 boundary handled separately.
- At every p>=5, the residue-one root has all-depth valuation v_p(Ccal_n)=v_p(n-1), with compensating divisibility in H,K,Delta and Qpart.
- Complete seeds at 5 and 13 plus that root theorem give v_p(q_n)>=2v_p(n!) at every sufficiently large index.
- The other already certified primes 7,11,17,19 give the same bound outside unresolved residue sets {2,3}, {2}, {3,11}, {14}, respectively.

The odd dyadic germ review accepts exact Ccal valuations: v_2(n-1) on n=1 mod 8 except n=1; valuation 2 on n=3,5 mod 8; and v_2(n-nu) on n=7 mod 8, with nu in 15+16 Z_2. Its PASS does not include Section 3's transfer to q.

The ternary root xi in 55+81 Z_3 and associated conditional q formulas are reported independently reviewed in the closing register. Their complete source and review have not yet been read in this reconstruction. Neither nu nor xi has a proved arithmetic nature or an integer-proximity bound.

### b=2

The September 13 exact formula is X/Y=Xcal_n/Dcal_n. With the source's derivative combinations H,J,K, define

S=J_{n+1}^2-H_{n+1}K_{n+1},
C=(J_{n+1}-H_{n+1})J_n-(K_{n+1}-J_{n+1})H_n,
W=J_{n+1}J_n-K_{n+1}H_n.

Then Dcal_n=(n+1)^2 P_{n+1} C-2P_n S, and Xcal_n retains second-kind values, partial-exponential contractions, and a factorial term. Its displayed integer clearer is deliberately nonminimal. Only reduction of the complete quotient gives q.

At p>2n+4, the primitive full endpoint gcd is bounded above by the gcd Omega_n of three actual maximal minors. The September 27 theorem reduces v_p(Omega_n) to two scalar depths, including a cubic in H'_n/H_n, subject to the stated unit conditions. This is a necessary gate on endpoint cancellation, not a sufficient condition for it.

Adjacent large-prime coprimality and Omega nonvanishing are inherited reviewed results. They do not bound isolated deep cancellation. Fixed small primes lie outside the large-prime gate and require a separate numerator analysis. The endpoint source also reports cancellation at n=p-1; its original scope needs checking before use.

## Analytic theorem and its strict boundary

For every fixed b>=1, the (n,b,n) matched system is eventually projectively unique with Y nonzero, and

(-1)^n R(1)/(Y epsilon_n) -> (sqrt(2)-1)^b,
log epsilon_n/n -> -tau,
tau=2 log(1+sqrt(2)).

Both the proof and independent review were read. The proof keeps full tails and determinant cancellation. Its constants depend on fixed b. It supplies no growing-b theorem and no reduced-denominator estimate.

For fixed b, writing p_n/q_n=-A_n(1)/Y_n in lowest terms gives the nonzero integer form q_n(e+pi)-p_n=q_n R_n(1)/Y_n and

log|q_n(e+pi)-p_n|=log q_n-tau n+o(n).

A liminf denominator rate strictly below tau would suffice for irrationality via a subsequence. A lower rate strictly above tau excludes this family. Neither conclusion follows merely from an upper bound on coefficient denominators.

## Outstanding audits and earlier draft observations

1. Section 3 of hp_b1_odd_dyadic_actual_numerator.md: actual-q transfer and odd exclusion outside 15 mod 16. Pending independent review.
2. hp_b1_closed_prime_odd_index_restriction.md: the combined rate logic and 146 CRT classes modulo 24871. Premises reviewed historically; synthesis audit pending.
3. Earlier main-agent intersection: 146 classes modulo 16*24871=397936, density 73/198968 among all integers. Conditional on the two pending deductions; not yet independently checked.
4. Earlier main-agent spacing draft: a shrinking increasing b=1 subsequence would eventually require v_2(n-nu)>n/2, hence successive n<m would satisfy m-n>=2^ceil(n/2). The numerator separation and actual-q transfer need independent checking. Even if correct, exponential spacing does not exclude an infinite subsequence.

No draft above is a solution of the main problem.

## Most useful next directions

- Attempt a finite, exact extension of uniform b=1 primes beyond the old closed list. If enough primes have only the already resolved residue-one root, their combined reduced-denominator bound could bypass all unresolved local roots. This changes the available arithmetic input; it is not a repetition of the closed raw-family scan.
- Derive the b=2 analogue of the complete factorial numerator and its residue transfer. This directly addresses the small-prime gap instead of misapplying a large-prime minors theorem.
- Investigate a specified genuinely growing b regime. First obtain exact identities and identify the uniform nonvanishing and primitive-height requirements; fixed-b limits cannot be extrapolated.
- Complete the two inherited synthesis audits and assess the earlier drafts, with explicit review scope.

## Current-session update: normalized b=2 stage

The complete b=1 exclusion is now independently passed and inspected by the main agent; the older b=1 open-frontier descriptions above record the initial background only. See agent4/B1_WHOLE_FAMILY_REVIEW.md.

The growing-degree reduction and intended absolute bounds passed review with an explicit factorial-domain correction; author repair is pending. New normalized b=2 arithmetic has an exact common-factor certificate and author-reported unit primes 3,7,11,13. The sufficient 3/7/11 whole-family synthesis remains under independent audit. The main problem and growing-degree primitive arithmetic remain unresolved. See VERIFICATION_REGISTER.md for current evidence boundaries.

## Update after the complete b=2 audit

Both the b=1 and b=2 families are now excluded by independently reviewed actual-denominator theorems and their accepted analytic errors. The main agent has read both complete reviews. Earlier descriptions of unresolved b=1/b=2 whole-family exclusion above record the initial background, not the current frontier.

The surviving growing-degree work now has exact row/content reductions and a sharper Gaussian absolute bound. Its nonvanishing and final arithmetic content remain unresolved. GROWING_CONTENT_CRITERION_DRAFT.md and GROWING_FACTORIAL_CONTENT_DRAFT.md are pending independent review; they are not solutions.

## Current frontier after the bound-ratio correction

The main-agent note GROWING_BOUND_OBSTRUCTION_DRAFT.md identifies a limitation of the chosen growing-degree upper bounds: their remainder bound exceeds four times their endpoint bound. The corresponding strict leading content targets are marked unattainable, subject to the stated normalization audit. This is not a whole-family exclusion.

The actual growing-degree remainder, endpoint nonvanishing, and precise residual arithmetic remain open. Agent 1's additional recurrence is reported complete but awaits inspection and independent review. The three interrupted reviews are recovery work, not completed results.

## Current frontier: revised remainder and high-row slack

The completed arithmetic/content reviews are now incorporated in VERIFICATION_REGISTER.md. The old strict content thresholds are rejected. The revised projection remainder preserves a genuine scalar saving but retains the coarse high-row product; its newly identified quadratic loss is recorded precisely in GROWING_HIGH_ROW_SLACK_DRAFT.md, pending independent audit.

The n=6 Bernstein control is successful finite evidence only. The new GROWING_TWO_SCALAR_QUOTIENT_DRAFT.md isolates a weaker actual determinant sign condition and keeps the full companion explicit. No growing-degree nonvanishing or successful primitive-form estimate is established.

## Update: actual determinant quotients

The additional recurrence/minor audit is complete and has been inspected, with a stale-target documentation repair outstanding. Exact arithmetic and gcd-scale identities are accepted within that scope.

The new two-scalar quotient cancels common high rows before estimating the remainder. Its uniform endpoint signs, companion conditioning, actual denominator growth, and full-remainder nonvanishing remain unresolved. The saved Bernstein control and difference checks are finite evidence only. See VERIFICATION_REGISTER.md for outstanding independent reviews.
