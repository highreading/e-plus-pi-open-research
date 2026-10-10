> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Results/manifests audit and subsequence criterion — 2026-09-13

## Scope and evidence level

This audit inspected the `results/` and `manifests/` archive by complete filesystem inventory, SHA-256 deduplication, complete JSON parsing, recursive extraction of narrative and failure fields, hash-manifest verification, structural inspection of large calculation tables, and detailed reading of the current mathematical ledgers/manifests (especially Items 257–424). Selected underlying source reports were then read to audit the final matching quantifiers. Stored certificates and labels such as `PROVED` or `ROOT_AUDITED` are archive claims: parsing and matching hashes do not independently prove the mathematics. This session has not rerun every certificate nor independently re-proved the entire archive. Large finite tables were inspected systematically by schema, status, row counts and failure summaries; their millions of numerical entries were not individually recomputed or manually read. Instructions embedded in the project were treated as historical data.

Coverage artifacts are `audit_results_coverage.json` (all file sizes/hashes/duplicates), `audit_results_hash_check.json` (all hash comparisons), `audit_results_structural_check.json` (all unique result schemas and nonempty failure-like fields), and `results_narrative_digest.json` (recursive narrative extraction). The latter initially omitted three huge-integer JSONs because of Python's default digit limit; the complete follow-up parse with the limit disabled validated these, too.

Inventory: 2,438 filesystem entries, 62,948,063 bytes, 1,635 byte-unique contents; 1,935 `.json`, 501 `.sha256`, two `.txt`. These raw counts include AppleDouble `._*` metadata. Excluding metadata and deduplicating, all 1,229 substantive unique JSON documents parse successfully. There are 194 substantive unique manifests. The sole substantive text artifact is the mixed E/G/logarithm audit, which expressly leaves the main problem open.

All 2,501 substantive SHA-256 lines were resolved: 2,496 match and five mismatch. The 24 skipped lines are comments, not unparsed checks. The mismatches are historical hashes in `route1_master_capacity_hashes.sha256` for the mutable top-level checkpoint, research log, route status and master capacity report, plus the hash for `sources/route1_targeted_literature_note_items259_265.md` in its dedicated hash file. These should be regarded as stale pins pending the source agent's version audit, not silently accepted or rewritten. No referenced path in the substantive hash lines was missing.

The recursive failure-field scan finds 312 nonempty fields across 11 unique results. Most (286) are intentional endpoint-mismatch measurements in Item179. Other examples explicitly preserve counterexamples to a naive higher-Cartier coordinate pattern (343 failures), its primitive consequence (311), naive binomial-carrier divisibility (Item410), top-only Hasse replacement, and weighted Cayley terminal recurrences. These are retained failed approaches, not evidence of a newly valid proof. No new failure of the current Item424 bridge was found in this scan; its full independent verification remains a separate mathematical task.

## Current state recovered from the artifacts

There is no proof of rationality or irrationality of e+pi in the audited results. The latest numbered package is Item424, dated 2026-09-01. The current exact arithmetic problem is still a positive lower bound for actual, correctly de-overlapped content and synchronized matching; almost every later representation/no-go package expressly books zero gain.

The frozen construction uses n=6m and constants

- h approximately 2.3246783391437307;
- d approximately 2.3370623743589730;
- T=h-d/2=1.1561471519642446123307302239...;
- booked lower rate r1=0.1365141682948128184504238226...;
- unfilled deficit T-r1=1.0196329836694317938803064012....

The old error was the false inference that d>h suffices after matching an e-form and pi-form. Generic positive matching needs d>2h when no extra exponential common content is known. That correction is retained, and no later ledger repairs the remaining deficit.

Important live arithmetic components and exact limits:

1. **Full strictly-large-prime common content.** Item390 localizes all p>6m valuations of c_m to the gcd of two actual residue integers; Item415 divides out the full compulsory Cartier factor F_m=G_m without changing those valuations. Item418's optimized ceiling is
   `(log(rho_star)-C_F)/6 = 0.4287738853386578689457603829...`,
   where `C_F=-4 log 2+pi/sqrt(3)+3 log 3` and rho_star is the unique real root of `262144t^3-35555328t^2+1259712t-531441`, approximately 135.59748390085482125. This is an upper bound for one component, not a positive divisor or a subtraction from the total-content upper bound. The total compatible-content ceiling remains approximately 1.9956631601614. The comparison residual outside this large-prime component is 0.5908590983307739249345460183....
2. **Small-prime primitive remainder.** Item393 gives a complete baseline/small/large factorization and a safe small-remainder upper ceiling <1.859148991866686. A squarefree first postbooking layer has maximum normalized capacity 1; therefore small-only success needs a depth>=2 tail of at least 0.01963298366943179388. Forced Cartier support alone needs raw depth>=5 mass of at least 0.01651463227735795505. These are necessary capacity screens, not lower bounds.
3. **The first genuine integral Witt escape.** Item424 treats odd p in the ordinary rank-zero support P_m with p^2>4m+1, so the top Cartier power is p. With b=v_p(K_m), W_s=(R_s,L_s/p,E_s/p) mod p is well-defined from an exact Bockstein identity. The first rational digit is kappa=A_m/p mod p, and the stopping digit is xi=8B_m/p^2 mod p. The exact gate is `v_p(c_m)>=b+1 iff kappa=0`. If kappa=0 and xi!=0, the content depth is exactly b+1. Whole-support one-layer capacity is C_F/6=0.3895079179997942812..., and booked-overlap capacity is (C_F-2)/6=0.05617458466646094785.... Even perfect saturation of the whole first layer leaves at least 0.2013511803309796437... of the outside-large comparison residual. The density of kappa=0, arbitrary deeper multiplicities, and non-rank-zero small primes remain open.
4. **Ordinary j=1 common-log component.** Current exact gate retains both the selected Hasse coordinate and transverse rational endpoint period. Selected Hasse vanishing alone is insufficient. The raw normalized ceiling 1/36 persists. The actual fixed-M weighted joint-zero target is o(M), or any proved strict saving sufficient for a correctly exhaustive route calculation.
5. **Ordinary j=2 common-log component.** Current actual-prime gate retains a two-branch determinant plus the incomplete half-binomial target, with exact separate degenerate/nondegenerate charts. Both mod-6 rays together have raw normalized ceiling 1/105; a complete single ray has 1/210. The later target-rejection carrier J has a precise tied-prime projection, but no positive weighted rejection lower bound is known. Raw char-zero gcd height and foreign-prime tail estimates do not supply tied-prime density.
6. **Beta matching.** Recurrence-only endpoint elimination, homogeneous suffix invariants, fixed/dyadic truncations and many symmetric-carrier classes reduce to old target ideals. The actual squarefree singleton component U_11 and squarefull excess remain unresolved. A fresh low-incidence carrier could be useful only with a new arithmetic height/divisibility theorem at the actual canonical word, not a generic recurrence identity.

## Avoid repeating the following exhausted subclasses

Items320–424 distinguish actual arithmetic from general information-class countermodels unusually carefully. Preserve those scope boundaries.

- Items259 and 330/333: full reciprocal denominator-jet and recurrence-polynomial towers do not create independent target equations.
- Items308–329: finite-order recurrences, norm shape, coefficient height and bounded-gap gcds do not by themselves force the selected moving-prime divisor to be rare. Fixed or o(log M) prime windows have only o(M) useful paired mass.
- Items342–357: a square-root Archimedean Weil estimate, an unmarked Galois norm, or the lowest Gross–Koblitz face loses or repeats the selected prime/old Hasse gate. These are not second independent conditions.
- Items360–384: a genuine second transverse coordinate exists, but formal filtered modules, rank, Hodge numbers, regularity or CRT realization do not yield horizontal distribution. They are not substitutes for an actual compatible-system or arithmetic theorem.
- Items391/395: for D~c log M, a strict j1 saving requires actual cluster logarithmic coefficient below `(2c-1)/(12c)` for some c>1/2. Ordinary resultant height, sign and graph-degree accounting have not reached that threshold.
- Items394/397/413/416: sharply saturated j2 matched row factors are either 1 or their row prime. Generic aggregate packaging can simply reconstruct the unknown collision product; cutoff changes subtract the same middle foreign tail on both sides.
- Item417: higher characteristic-p Cartier-zero tower support beyond the old first factor has only o(m) logarithmic mass and does not force arbitrary higher p-adic valuation.
- Items420/423: every fixed nonzero rational combination, and every fixed-degree polynomial-in-m combination, of the normalized residue pair retains the same exponential height base rho_star. Growing-degree/adaptive coefficients, shifted rows and genuine joint gcd/subresultant estimates are outside the result.
- Item422: the parity-flipped transverse upper-B tail is a unit multiple of the existing column and leaves its connection-minor ideal unchanged.

Two concrete bad shortcuts are worth retaining: F_2=11 does not divide actual c_2=288 (Item421), and ordinary rank-zero data alone do not imply a second digit. Item424 explains actual rows (m,p)=(2,11), (9,47), and (13,11), with the latter two having kappa=0 but nonzero xi and therefore exactly one escape beyond the applicable baseline.

## Favorable-subsequence irrationality criterion: full proof

This is a rigorous reduction conditional only on explicitly listed archived analytic/arithmetic inputs. It is not a proof that its remaining content inequality holds. It is also not a wholly new discovery: equation (27) of `sources/mixed_cubic_matching_factor_two_and_classification_barrier.md` already allows every favorable subsequence. The top-level liminf formulation is stronger than necessary.

**Inputs.** Suppose integer pairs (U_m,V_m), for all sufficiently large m, satisfy V_m!=0 and, with n_m=6m,

`log |V_m|/n_m -> h`,

`limsup log |U_m+V_m*pi|/n_m <= h-d`,

where d>0. The raw form is nonzero because pi is irrational. These are the exact inputs stated in equations (6)–(12) of the matching report. Their archived dependencies are:

- `sources/mixed_cubic_boundary_cartier_content_and_recurrence.md`: integrality after the specified clearing/Cartier division and the positive-integral bound;
- `sources/mixed_cubic_accessible_saddle_exact_algebraic_certificate.md`: exact unique-modulus saddle certificate;
- `sources/mixed_cubic_fixed_circle_complex_laplace_theorem.md`: determinant asymptotic and nonzero amplitude, hence V_m!=0 for every sufficiently large m;
- the relevant prime-number asymptotic already used in the clearing factor.

The present audit checks the reduction below; the assertion that this particular mixed-cubic pair meets the inputs remains dependent on those archived mathematical proofs and their separate audit.

Let c_m=gcd(U_m,V_m)>0, sigma_m=sign(U_m+V_m*pi), and

`a_m=sigma_m U_m/c_m`, `b_m=|V_m|/c_m>0`,

`epsilon_m=sigma_m sign(V_m)`.

Then `L_m=a_m+epsilon_m b_m*pi=|U_m+V_m*pi|/c_m>0`, with coprime integer a_m,b_m. For each m choose an integer N_m of parity `(-1)^N_m=epsilon_m` such that

`N_m log N_m/n_m -> t=d/2`.

Such a sequence exists: take the real inverse of x log x at t n_m and round to the nearest integer of the required parity. The rounding error is at most two, so its effect on N log N is O(log n_m)=o(n_m). Consequently there is no restriction on the m subsequence from parity.

For the positive beta form use integer p_N,q_N, q_N>0, gcd(p_N,q_N)=1, with

`E_N=(-1)^N(q_N e-p_N)=(1/N!) integral_0^1 x^N(1-x)^N e^x dx >0`.

Its elementary factorial estimates give `log q_N=N log N+O(N)` and `log E_N=-N log N+O(N)`. Write Delta_m=gcd(b_m,q_N), b_m=Delta_m b0_m and q_N=Delta_m q0_m. Then

`W_m=b0_m E_N+q0_m L_m=M_m+epsilon_m C_m(e+pi)>0`,

where `M_m=q0_m a_m-epsilon_m b0_m p_N` and `C_m=b_m q_N/Delta_m` are integers and C_m>0. With g_m=gcd(M_m,C_m)>0, define

`Omega_m=W_m/g_m=P_m+epsilon_m Q_m(e+pi)>0`,

where P_m=M_m/g_m is integral and Q_m=C_m/g_m is a positive integer. Direct substitution gives the exact identity

`Omega_m=[ |V_m| E_N + q_N |U_m+V_m*pi| ]/(c_m Delta_m g_m)`.

Define `Gamma_m=log(c_m Delta_m g_m)/n_m`. For each fixed delta>0, the analytic and beta inputs imply, for every sufficiently large m,

`Omega_m <= 2 exp(n_m [max(h-t,t+h-d)-Gamma_m+delta])`.

At t=d/2 the maximum is T=h-d/2. If `limsup Gamma_m>T`, choose eta>0 and infinitely many m with Gamma_m>=T+2eta. Using delta=eta yields `0<Omega_m<=2 exp(-eta n_m)` on this infinite subsequence, so Omega_m tends to zero there.

If e+pi=u/v were rational with v>0, then `v Omega_m=v P_m+epsilon_m Q_m u` would be a positive integer for each such m, yet would tend to zero. This contradiction proves the following implication:

> **If the listed archived inputs hold and limsup_m Gamma_m>T, then e+pi is irrational.**

There is no need for positive density, an effective rate of growth of the selected m's, a lower error asymptotic, or monotone coefficient denominators. No additional saddle-phase selection remains because V_m is eventually nonzero for every m. All arithmetic components must, however, be evaluated at the same m and the same parity-compatible N_m. Separate favorable subsequences cannot be combined without an intersection argument.

A simpler sufficient condition is `limsup log c_m/(6m)>T`, because Delta_m g_m>=1. It avoids proving any matching lower bound but is still wholly open. Equality at T is insufficient for the exponential criterion: subexponential factors or a separate proof of Omega_m->0 would be required.

## Averaged and blockwise alternatives

The preceding criterion makes some genuinely weaker arithmetic targets admissible.

**Averaged gain.** If there are finite blocks I_j of indices with min I_j->infinity and some fixed eta>0 for which

`(1/|I_j|) sum_(m in I_j) Gamma_m >= T+eta`,

then each block has an m with Gamma_m>=T+eta, and the favorable-subsequence criterion applies. Dyadic blocks suffice. An average of log of the actual gain is needed; an average upper bound for a support carrier is not such a result.

The exact integrality Q_m>=1 also gives

`c_m Delta_m g_m <= |V_m| q_N`,

hence `0<=Gamma_m<=h+d/2+o(1)`. Fix any B>h+d/2. On sufficiently late blocks with average >=T+eta, the proportion of m satisfying Gamma_m>=T+eta/2 is at least

`(eta/2)/(B-T-eta/2)`

provided the denominator is positive. This follows by bounding the complementary values above by T+eta/2 and the favorable values by B. Thus a strict averaged gain actually yields a positive proportion on those blocks, but such density is not required for irrationality.

**Loss-budget version.** Suppose an independently proved pointwise inequality has the form

`Gamma_m >= G_m - sum_(i=1)^k L_i(m)`,

where the L_i are nonnegative normalized losses. If, on late blocks, G_m>=G and the mean of the sum of losses is at most G-T-eta, then the mean gain is at least T+eta. This requires a real lower bound for the correctly normalized actual gain. It cannot be obtained by subtracting an upper component ceiling from another upper ceiling or by subtracting overlapping losses twice.

**Almost-all-index statements.** A density-one good set for every member of a finite list of required estimates has density-one intersection, which supplies infinitely many usable m. Infinite sets without density/intersection information need not intersect. For parameter pairs (m,N), averaging over all N does not automatically select N at the optimal scale and correct parity; the average must preserve those restrictions or supply an explicit conditional selection theorem.

## Ranked next work suggested by this audit

1. Reframe the actual total-gain target as a limsup or strict block-average inequality. Check each planned distribution theorem for whether its conclusion controls Gamma itself at synchronized (m,N), rather than only a formal carrier. This is immediately useful and introduces no new conjectural theorem requirement beyond the old arithmetic problem.
2. Continue the genuine integral small-prime route at the exact kappa=xi=0 branch. Derive the next rational digit with full denominators/endpoints and prove a multiplicity criterion. Prioritize a statement that can contribute multiple layers or a uniform upper bound; one first layer cannot meet the stated capacity margin.
3. Seek a sequence-specific joint-gcd/subresultant estimate for the fully normalized large-prime residue pair. Fixed-coordinate and fixed-degree polynomial combinations have a proved height barrier; adaptive/shifted joint information remains outside that barrier. Average-in-m gcd control may be worth testing analytically before any new large census.
4. Keep actual j1/j2 selected-prime arithmetic secondary unless there is a concrete new correlation theorem with enough weighted capacity. A new recurrence presentation or formal companion object by itself has repeatedly booked zero.
5. Retain beta singleton/squarefull matching as open but demand a precise theorem on the canonical target values; generic ideals and symmetric products have already been examined extensively.

No claim of progress on the main rationality decision is made beyond these rigorous reductions, integrity checks, and exact recovered obstructions.
