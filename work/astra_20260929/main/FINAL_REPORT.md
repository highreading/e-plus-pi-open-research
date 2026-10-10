> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

**Final research handoff — 29 September 2026**

**This project has not determined whether e+π is rational or irrational. No complete independently verified proof of either conclusion was produced.** The strongest completed result is an eventual obstruction for the specified matched b=2 approximation family: its reduced integer-coefficient linear forms grow in absolute value. This establishes a limitation of that construction and does not resolve the original problem.

Research ends under the explicit closing directive. All four worker final reports exist and have been read completely. No worker reports an outstanding calculation. No new research or audit was initiated during closure. The supplied registry contains no independently approved claim awaiting publication. Unreviewed candidates remain pending, including the two boundary certificates and the filter constructions.

This report organizes the archive through links without replacing or modifying existing sources, notes, candidates, or reviews. Mathematical summaries below retain the hypotheses of their cited records. The report is an integrated handoff, not a new independently reviewed theorem. No internet research was conducted for this closing work.

Paths below are relative to this report in work/astra_20260929/main. The verification register identifies exact publications; the worker reports provide more detailed calculation histories and local file indexes.

| Start here | Purpose |
|---|---|
| [Verification register](../../astra_review_registry/VERIFICATION_REGISTER.md) | Authoritative index of recorded independent reviews and publications. |
| [Worker_1 final report](../worker_1/FINAL_REPORT.md) | Endpoint normalization, independent finite certificates, interpolation cutoffs, digit estimates, and pending boundary-review status. |
| [Worker_2 final report](../worker_2/FINAL_REPORT.md) | Analytic transfer, denominator arithmetic, independent residue-four audit, dyadic precision, and boundary computations. |
| [Worker_3 final report](../worker_3/FINAL_REPORT.md) | Ordinary Padé prefactor, cofactor estimates, eventual endpoint nonvanishing, exact five-adic loss, and the whole-family obstruction. |
| [Worker_4 final report](../worker_4/FINAL_REPORT.md) | Small-prime denominator theorems, the corrected ternary certificate, synthesis review, and unreviewed filter candidates. |
| [Published whole-family obstruction](../../astra_review_registry/verified/w3-b2-whole-family-obstruction-v1.md) | Central negative result for the specified matched b=2 family. |
| [Published projection and error transfer, v2](../../astra_review_registry/verified/worker2-fixed-b-projection-and-error-transfer-v2.md) | Operative fixed-b analytic application theorem. |
| [Published endpoint reconstruction](../../astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md) | Exact definitions and normalization of the complete rational endpoint pair. |
| [Earlier research report](../../../research/historical_overviews/E_PI_RESEARCH_REPORT_20260927.md) | Historical context; its outstanding-work descriptions may be superseded by this session. |
| [Earlier session manifest](../../session_20260927/session_file_manifest.json) | Navigation of the preserved September 27 materials. |

Publication status must be read narrowly. An independently reviewed conditional theorem remains conditional in its immutable published text, even when another published theorem subsequently supplies a hypothesis. A finite certificate proves its stated finite calculation; it does not establish an infinite progression theorem. Author computations and peer agreement do not constitute independent approval.

| Record category | Interpretation at closure |
|---|---|
| Published scoped claim | The exact registered payload received independent approval and was published through the gate. Only its stated scope is certified. |
| Published conditional claim | The implication is independently reviewed. Each application must identify how its hypotheses are supplied. |
| Published computational certificate | The specified finite reconstruction was independently checked. Generalization beyond its scope requires an argument. |
| Registered but unpublished candidate | Preserved for reference; no independent approval is implied. |
| Working note or historical report | Research evidence with the qualifications recorded in that document and later corrections. It is not automatically a verified record. |

The common notation is essential. Write S=e+π and ρ=1+√2. In the convention R(1)=A(1)+YS, the rational approximant is r_n=−A(1)/Y. Reduce it as p_n/q_n with q_n>0 and gcd(p_n,q_n)=1. Its signed error and reduced linear form are

E_n=S−p_n/q_n=R(1)/Y,

L_n=q_nS−p_n=q_nE_n.

The coefficients of L_n are integers. Its value is not known to be an integer. Under a hypothetical equality S=u/v with integers u,v and v>0, vL_n would be an integer. An unbounded sequence of nonzero L_n tending to zero would therefore contradict rationality.

The alternate convention R=B exp(z)+CF−A gives the same approximant when A is changed consistently. It does not change the reduced numerator, positive denominator, or signed error. Earlier statements that a consistent convention change changes the actual approximant were explicitly corrected.

For the complete b=2 arithmetic construction, X_n and D_n denote the rational contractions defined in the published endpoint reconstruction. The approximant is −X_n/D_n. The positive reduced denominator of X_n/D_n is the same q_n. Define

f_n=2^n/(n!)²,

N_n=X_n/f_n,

Z_n=X_n/[f_n(n+1)].

Here f_n always denotes this factorial normalization, not an ordinary Padé approximant. Both exponential contractions and the full moment correction belong to X_n. Omitting the correction can change the local valuation.

The published endpoint identification uses

α_n=(−1)^n/[4(n+1)³(n!)⁴],

A_raw(1)=α_nX_n,

B_raw(1)=C_raw(1)=α_nD_n.

Its comparison with the ordered cofactor construction and its eventual nonvanishing conclusion are recorded in [the endpoint-identification theorem](../../astra_review_registry/verified/w3-b2-eventual-d-nonzero-v1.md). The exact identification applies under the source conventions for n≥2. The analytic argument supplies eventual D_n<0, without an effective starting index. It does not assert nonvanishing at every index.

For every prime ℓ and rational endpoint pair with D_n≠0,

v_ℓ(q_n)=max(0,v_ℓ(D_n)−v_ℓ(X_n)).

This identity does not require X_n or D_n to be integers. Common raw scaling cancels from the quotient. Polynomial coefficient content, the gcd of integer endpoint values, auxiliary maximal-minor content Ω_n, and the actual reduced denominator are distinct quantities.

If an integer polynomial triple has endpoint values a and y≠0, with g=gcd(|a|,|y|), then

q=|y|/g,   p=−sgn(y)a/g,

a+yS=sgn(y)g(qS−p).

Consequently, making the entire polynomial coefficient vector primitive need not make its endpoint pair coprime. The published n=12 certificate demonstrates this distinction explicitly.

The analytic part is complete within its fixed-degree scope. The ordinary Padé prefactor and the independently reviewed projection-and-transfer theorem give, for each fixed integer b≥1,

E_n=(−1)^n[4π/ρ^(b+1)]ρ^(−2n)(1+o(1)).

The construction is eventually unique up to scale and its matched endpoint is eventually nonzero, under the exact matching and degree conditions in the source theorem. These statements concern the specified construction. No estimate uniform in a growing b follows from them.

For an unbounded subsequence with b fixed,

|L_n|=[4π/ρ^(b+1)](q_n/ρ^(2n))(1+o(1)).

Thus shrinking reduced forms require and are equivalent to q_n/ρ^(2n) tending to zero on that subsequence. A strict exponential saving is sufficient, but a suitable subexponential saving would also suffice. Knowing only the exponential approximation rate does not control the reduced denominator.

The following published records give the analytic dependency chain and its refinements.

| Published record | Contribution and limitation |
|---|---|
| [Ordinary Padé prefactor](../../astra_review_registry/verified/worker3-ordinary-pade-prefactor-v1.md) | Proves ε_n∼(4π/ρ)ρ^(−2n). The original matched-family corollary explicitly requires a separate transfer theorem. Author worker_3; reviewer worker_2. |
| [Finite Taylor coefficient factorization](../../astra_review_registry/verified/fixed-size-factorial-determinant-finite-jet-factorization-v1.md) | Supplies fixed-size factorial-determinant normalization, a finite-coefficient factorization, and common-factor cancellation. Author main; reviewer worker_2. |
| [Normalized endpoint quotients](../../astra_review_registry/verified/worker2-normalized-endpoint-quotients-and-coefficient-determinants-v1.md) | Establishes scalar normalizations, a fixed analytic disk, local uniform limits, and nonzero limiting Taylor coefficient determinants. Author worker_2; reviewer main. |
| [Projection and error transfer v2](../../astra_review_registry/verified/worker2-fixed-b-projection-and-error-transfer-v2.md) | Checks exact projection, the complete remainder, application hypotheses, eventual rank and endpoint nonvanishing, and fixed-b transfer. Author worker_2; reviewer worker_3. |
| [Conditional matched-endpoint transfer](../../astra_review_registry/verified/worker3-fixed-b-matched-endpoint-transfer-conditional-v1.md) | Separately reviewed reconstruction and transfer conditional on its stated factorial-determinant lemma. That dependency has published support; the record retains its conditional wording. Author worker_3; reviewer main. |
| [Microscopic reference and sharper cofactor bound](../../astra_review_registry/verified/worker3-microscopic-reference-and-sharp-cofactor-bound-v1.md) | Quantitative reference-polynomial estimates and the stated additional-cofactor bound. Author worker_3; reviewer worker_2. |
| [Leading cofactor term](../../astra_review_registry/verified/w3-cofactor-leading-v1.md) | Full factorial-determinant leading term and its conditional endpoint specialization. Author worker_3; reviewer worker_2. |
| [Endpoint identification and eventual nonvanishing](../../astra_review_registry/verified/w3-b2-eventual-d-nonzero-v1.md) | Connects the arithmetic denominator to the ordered matched cofactor endpoint. Author worker_3; reviewer worker_1. |
| [Normalized-denominator accumulation obstruction](../../astra_review_registry/verified/fixed-b-denominator-accumulation-obstruction.md) | Restricts finite normalized-denominator accumulation points under rationality and the assumed error asymptotic. Author worker_2; reviewer main. |

The determinant lemma's O(1/n) factorial-transform remainder is not an O(1/n) convergence rate for every varying analytic coefficient determinant. Its application requires the specific fixed-size hypotheses. The microscopic reference estimate gives p_(n+1)(z/n)/p_(n+1)(0)→exp(−√2z), with relative O_K(1/n) error on fixed compact sets. Sharper rates for other normalized factors are stated individually in their records and must not be inferred merely from the ordinary-error equivalent.

In the cofactor records' notation, the published bound is

|(N/D_V)/(W(0)/V(0))|=O_b(|V(0)|/[n! n^(2b+1)]),

and the separately reviewed specialization gives

n! n^(2b+1)N/[D_VW(0)]→(−1)^b b! 2^((1−b)/2)exp(−√2).

Here N is the cofactor determinant in those records, not the arithmetic N_n defined above. Row order, factorial indices, and normalizations are part of the statements. Neither result controls the actual reduced denominator.

The accumulation theorem is another conditional criterion rather than a successful construction. If S=u/v is rational in lowest terms and the fixed-b error asymptotic holds, every finite accumulation point T of q_n/ρ^(2n) belongs to

{mρ^(b+1)/(4πv): m=1,2,3,…}.

A finite algebraic accumulation point would contradict rationality. None has been established for the actual denominator sequence. A sequence of algebraic numbers need not have an algebraic limit. For b=2, the published obstruction below instead forces the normalized denominators to diverge.

The arithmetic work now covers all residue classes needed for the eventual b=2 obstruction. Let r_ℓ(n)=v_ℓ(n!). The following table summarizes the exact local statements for the complete endpoint quotient. Where D_n≠0 is explicit, it remains an application hypothesis until supplied by a separate theorem.

| Prime and indices | Published conclusion | Source |
|---|---|---|
| ℓ=3, n≥3, n≡0 mod 3 | v_3(D_n)=0, v_3(X_n)=−2r_3(n), and v_3(q_n)=2r_3(n). | [Ternary residue zero](../../astra_review_registry/verified/b2-ternary-endpoint-denominator-and-content-v1.md) |
| ℓ=3, n≥4, n≡1 mod 3 | N_n∈1+3Z_3 and D_n∈3Z_3. If D_n≠0, v_3(q_n)=2r_3(n)+v_3(D_n)≥2r_3(n)+1. | [Ternary residue one](../../astra_review_registry/verified/worker4-b2-ternary-residue-one-conditional-denominator-v1.md) |
| ℓ=3, n≥5, n≡2 mod 3 | D_n≠0 and v_3(D_n)=v_3(N_n)=v_3(n+1), giving v_3(q_n)=2r_3(n). | [Ternary residue two](../../astra_review_registry/verified/worker2-b2-ternary-residue-two-exact-denominator-v1.md) |
| ℓ=5, n≥5, n≡0 mod 5 | D_n is a unit, N_n≡3 mod 5, and v_5(q_n)=2r_5(n). | [Five-adic residue zero](../../astra_review_registry/verified/b2-five-adic-endpoint-denominator-v1.md) |
| ℓ=5, n≥6, n≡1 mod 5 | D_n is a unit, N_n≡4 mod 5, and v_5(q_n)=2r_5(n). | [Five-adic residue one](../../astra_review_registry/verified/worker4-b2-five-adic-residue-one-exact-denominator-v1.md) |
| ℓ=5, n≥7, n≡2 mod 5 | D_n is a unit, N_n≡2 mod 5, and v_5(q_n)=2r_5(n). | [Five-adic residue two](../../astra_review_registry/verified/worker4-b2-five-adic-residue-two-exact-denominator-v1.md) |
| ℓ=5, n≥8, n≡3 mod 5 | If D_n≠0, v_5(q_n)=2r_5(n)+v_5(D_n)≥2r_5(n)+1. | [Five-adic residue three](../../astra_review_registry/verified/w3-b2-five-residue-three-loss-v1.md) |
| ℓ=5, n≥4, n≡4 mod 5 | v_5(D_n)=v_5(n+1), so D_n≠0. The additional forced cancellation Z_n∈5Z_5 begins at n≥9. | [Residue-four cancellation](../../astra_review_registry/verified/main-b2-five-adic-residue-four-cancellation-v1.md) |
| ℓ=5, n≥14, n≡4 mod 5 | Z_n≡20 mod 25, hence v_5(Z_n)=1 and v_5(q_n)=2r_5(n)−1. | [Exact residue-four loss](../../astra_review_registry/verified/w3-b2-five-residue-four-loss-v1.md) |

On the residue-four progression the general rational valuation identity specializes to

v_5(q_n)=max(0,2r_5(n)−v_5(Z_n)),

with v_5(0)=∞ when appropriate. Forced divisibility alone gives no upper bound on v_5(Z_n). The later theorem closes that particular gap for n≥14 by proving the exact congruence modulo 25. The proof handles arbitrarily large v_5((n+1)/5), retains the singular exponential boundary, and supplies uniform tail and moment estimates. Agreement at five representative indices was supplementary evidence, not the universal proof.

A separate published [numerator-nonvanishing theorem](../../astra_review_registry/verified/worker2-b2-residue-four-numerator-nonvanishing-v1.md) establishes X_n≠0 and Z_n≠0 for n≥4 on this progression. It uses the same endpoint quotient and the ternary denominator statements. Nonvanishing alone does not bound the valuation quantitatively and is not needed to infer nonvanishing from the n≥14 congruence.

Combining the local bounds with eventual endpoint identification gives, for all sufficiently large n in this matched b=2 family,

v_3(q_n)≥2r_3(n),

v_5(q_n)≥2r_5(n)−1.

Thus

q_n≥3^(2r_3(n))5^(2r_5(n)−1).

Legendre's formula expresses these exponents through base-three and base-five digit sums, giving the growth scale

q_n≥exp(n log(3√5)−O(log n)).

The b=2 analytic error has magnitude [4π/ρ³]ρ^(−2n)(1+o(1)). Consequently the published synthesis yields

|L_n|≥exp(n log(3√5/ρ²)−O(log n))→∞,

because 3√5>ρ²=3+2√2.

This is the content of the reviewed [whole-family obstruction](../../astra_review_registry/verified/w3-b2-whole-family-obstruction-v1.md). Its immutable statement retains explicit matching, arithmetic, and analytic hypotheses. The residue-four hypothesis called H4 in that statement now has a separate published proof with the same definitions. The exact arithmetic threshold n≥14 remains distinct from unspecified eventual thresholds for analytic estimates and endpoint identification. This report does not claim an effective common starting index.

The conclusion excludes a shrinking subsequence within these eventually defined reduced forms. It also excludes shrinking nonzero integer multiples of them. It does not cover arbitrary combinations of neighboring approximants, different approximation families, or growing b. In particular, divergent forms do not imply that their target is rational or irrational.

The following additional published records document normalization, finite checks, and narrower arithmetic consequences.

| Published record | Scope |
|---|---|
| [Large-prime coefficient content](../../astra_review_registry/verified/b2-large-prime-content-normalization.md) | Relates raw coefficient valuations and primitive normalization for p>2n+2. It supplies no global denominator estimate. |
| [Two-chart endpoint ideals](../../astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md) | Exact reconstruction, local chart coverage, and actual denominator identities with the stated prime and nonzero hypotheses. |
| [Corrected ternary auxiliary certificate](../../astra_review_registry/verified/b2-ternary-zero-diredacted_historical_name.md) | Coefficientwise unit-minor certificate on the auxiliary index disk 3Z_3; not an unrestricted endpoint-gcd theorem. |
| [Four ternary endpoint certificates](../../astra_review_registry/verified/worker1-b2-four-ternary-endpoint-certificates-v1.md) | Independent exact reconstruction at n=3,6,9,12 and full primitive normalization at n=12. |
| [Conditional five-adic coefficient content](../../astra_review_registry/verified/worker4-b2-five-adic-residue-two-conditional-content-v1.md) | Retains its reconstruction-loss hypothesis 0≤c≤L and distinguishes content from endpoint gcd and reduced denominator. |
| [Multiples-of-five obstruction](../../astra_review_registry/verified/w3-b2-five-multiples-obstruction-v1.md) | Earlier restricted-progression synthesis. Its arithmetic and eventual analytic conclusions have separate starting qualifications. |
| [Residue-one form growth](../../astra_review_registry/verified/worker1-b2-five-adic-residue-one-form-growth-v1.md) | Growth on n≡1 mod 5 under the stated matched-family identification. |
| [Residue-one digit refinement](../../astra_review_registry/verified/w3-b2-residue-one-digit-refinement-v1.md) | Sharper digit-sum constant for that progression. Publication is complete. |

The large-prime primitive endpoint-gcd implication has its own cutoff p>2n+4; adjacent auxiliary-content support exclusion has cutoff p>2n+6. These cannot be applied at three or five outside their hypotheses. Auxiliary Ω_n nonvanishing and adjacent support exclusion do not bound the size of individual content or the actual reduced denominator.

The earlier cubic-gate and adjacent-content investigation is preserved as a completed composite audit in [worker_2 note 6](../worker_2/note_000006.md), with original materials in [the cubic gate](../../session_20260927/hp_b2_cubic_maximal_minor_gate.md), [the adjacent-content report](../../session_20260927/hp_b2_adjacent_content_coprimality.md), and [the endpoint arithmetic](../../session_20260913/hp_b2_contiguous_endpoint_arithmetic.md). Worker_2 records sixteen independently computed vanishing symbolic residuals and checks of the prime restrictions and full-depth argument. This composite working audit is not itself a separately published registry claim.

The dyadic and interpolation work established useful scoped results but did not close the exceptional-root problem for b=1.

| Published record | Result and boundary |
|---|---|
| [Conditional dyadic depth and index gaps](../../astra_review_registry/verified/conditional-dyadic-depth-and-index-gaps.md) | Under its specified actual-denominator and analytic inputs, a shrinking b=1 subsequence requires linearly growing dyadic approximation depth and exponentially large index gaps. Sparse infinite survivors are not excluded. |
| [Finite dyadic coefficient reconstruction](../../astra_review_registry/verified/worker3-dyadic-finite-coefficient-verification-v1.md) | Independent reconstruction of twenty coefficient arrays on four odd disks modulo 1024. This is a finite certificate. |
| [Dyadic analytic tails and precision](../../astra_review_registry/verified/worker2-dyadic-analytic-tail-and-precision-v1.md) | Coefficientwise convergence, truncation bounds, and precision losses under normalization. Endpoint identification and ordinary-integer approximation depth are separate issues. |
| [Algebraic-root depth obstruction](../../astra_review_registry/verified/worker3-algebraic-dyadic-root-depth-obstruction-v1.md) | Rules out the required linear depth for algebraic roots, with the stated exceptions handled. Algebraicity of the project's exceptional root is not established. |
| [Finite-data counterexample](../../astra_review_registry/verified/worker3-finite-data-dyadic-depth-counterexample-v1.md) | Constructed analytic germs show that the specified finite data and quantitative convergence do not force a depth bound. This is not a statement about the project's particular germ. |
| [Simple-root precision transfer](../../astra_review_registry/verified/worker3-simple-root-precision-transfer-v1.md) | Tracks finite precision through simple-root normalization and coordinate changes; depths beyond the available precision remain unresolved. |
| [Odd-prime interpolation cutoff](../../astra_review_registry/verified/odd-prime-interpolation-tail-cutoff-v1.md) | Improved coefficientwise truncation and optimal individual-summand block cutoffs. |
| [Cutoff sharpness and logarithmic search](../../astra_review_registry/verified/odd-prime-cutoff-sharpness-and-logarithmic-search-v1.md) | Infinite sharpness and a bounded search interval for the individual-summand criterion. Neither cutoff record proves optimality after cancellation in the summed tail. |

The conditional b=1 depth coefficient is

δ=[(3/2)log 2+(1/2)log 5+(1/6)log 13−2log ρ]/log 2>0.

With the published conditional claim's input estimates, a shrinking subsequence must satisfy v_2(n−ν)≥δn−o(n) at the specified exceptional root ν. That is a necessary condition, not an upper bound on the approximation depth. Exponentially large gaps do not rule out infinitely many indices. Neither finite coefficient data, simple-root existence, nor general analytic convergence determines the arithmetic approximation behavior of this specific ν.

The finite dyadic review reproduced all twenty arrays and checked exact divisibility before modular inversion; worker_2 records 400396 coefficient divisibility checks. The analytic bounds 5R/16−6 and 5R/16−7 justify the stated separate tail treatment. Division of congruences modulo 1024 by four or eight leaves precision modulo 256 or 128 respectively unless more information is proved. Forming an integral product difference loses no precision, but division by a coordinate requires the stated exact divisibility. None of these computations supplies an ordinary-integer approximation-depth bound.

Finite endpoint evidence requires particular care at the boundary indices. The following statuses preserve the distinction between completed arithmetic and independently approved candidate text.

| Evidence | Values or observation | Verification status |
|---|---|---|
| n=3,6,9,12 ternary reconstruction | Complete endpoint reconstruction at four indices. At n=12 the primitive endpoint gcd is 73920, primitive endpoint ternary valuations are 1 and 11, and v_3(q_12)=10. | Independently reviewed and published in the four-certificate record. This does not certify a separate five-adic n=9 candidate. |
| n=4 boundary calculation | X_4=92521969330/9, D_4=−1754485920, f_4=1/36, Z_4=74017575464, and q_4=1579037328. | Completed author calculation; the immutable n=4 candidate remains unreviewed. |
| n=4 complete moment contribution | Normalized exponential and moment contributions to Z_4 are 34338004520 and 39679570944, with residues 20 and 19 modulo 25. Thus the reported Z_4 residue is 14 modulo 25. | Computational evidence in worker_2's boundary materials, outside independent candidate approval. |
| n=9 five-adic boundary calculation | Reported exponential contribution 20 mod 25, moment contribution 5 mod 25, and Z_9≡50 mod 125; hence the calculation gives v_5(Z_9)=2 and v_5(q_9)=0. | Preserved calculations support the boundary behavior, but the registered n=9 certificate has no accepted independent review. |
| n=14,19,24,29,34 residue-four reconstructions | Independent exact checks agree with Z_n≡20 mod 25. | Supplement the published uniform theorem; they are not its replacement. |

The n=4 reduced endpoint quotient is −9252196933/1579037328; its negative is the approximant to S. The claimed numerator divisibility beginning at n=9 must not be extended to n=4. The exact-loss theorem beginning at n=14 must not be extended to n=9. Neither boundary certificate is needed for the eventual whole-family obstruction.

Useful preserved evidence paths are [worker_2 note 167](../worker_2/note_000167.md) for n=4 definitions and finite sums, [worker_2 note 175](../worker_2/note_000175.md) for its candidate integrity check, [worker_2 notes 147](../worker_2/note_000147.md), [148](../worker_2/note_000148.md), [149](../worker_2/note_000149.md), and [156](../worker_2/note_000156.md) for the residue-four audit, and [worker_4's seven-index table](../worker_4/note_000101.md), [provenance note](../worker_4/note_000105.md), and [saved calculation source](../worker_4/calculation_000100.py). These records retain their own scopes; their presence does not imply that every later candidate using them was independently reviewed.

The pending registry entries are listed below. This index does not initiate reviews or endorse their mathematical claims.

| Candidate | Recorded status and closing disposition |
|---|---|
| [Residual and Haar-null dyadic approximation](../../astra_review_registry/candidates/worker2-dyadic-linear-depth-residual-null-v1.md) | Under review, reviewer worker_3; no accepted review is recorded. Earlier rejected submissions are not approval. The category, measure, and dimension assertions remain unverified in the registry. |
| [Projection and transfer v1](../../astra_review_registry/candidates/worker2-fixed-b-projection-and-error-transfer-v1.md) | Awaiting assignment as an archival candidate. Superseded for use by published v2, which corrected the malformed dependency identifier. This is not an additional unresolved dependency of v2. |
| [n=4 exact boundary certificate](../../astra_review_registry/candidates/worker2-b2-n4-exact-boundary-certificate-v1.md) | Awaiting assignment. Worker_1 closed before auditing the immutable candidate. Earlier independent n=4 work does not constitute that review. |
| [n=9 boundary certificate](../../astra_review_registry/candidates/w3-b2-n9-boundary-certificate-v1.md) | Awaiting assignment. Worker_2 closed before reading and comparing this candidate with its saved calculations. |
| [Adjacent determinant growth](../../astra_review_registry/candidates/worker4-b2-adjacent-determinant-growth-v1.md) | Awaiting assignment; conditional candidate, not a published consequence of the whole-family theorem. |
| [Rational-target growth countermodel](../../astra_review_registry/candidates/worker4-rational-target-growth-countermodel-v1.md) | Awaiting assignment; concerns constructed approximants rather than the actual endpoint family. |
| [Digit minima and conditional denominator bound](../../astra_review_registry/candidates/worker1-digit-minima-and-conditional-denominator-bound-v1.md) | Awaiting assignment. Distinct from the already published residue-one digit refinement. |
| [Fixed rational cancellation weights](../../astra_review_registry/candidates/worker4-fixed-rational-weight-cancellation-v1.md) | Awaiting assignment. No verified filtered approximation construction follows from registration. |
| [Multiple-root filter rate](../../astra_review_registry/candidates/worker4-multiple-root-filter-rate-v1.md) | Awaiting assignment; retains its expansion and rate hypotheses. |
| [Parity digit refinement](../../astra_review_registry/candidates/worker1-parity-digit-denominator-bound-v1.md) | Awaiting assignment; not merged into the published bounds. |
| [Three-term filtered denominator](../../astra_review_registry/candidates/worker4-b2-three-term-filter-denominator-v1.md) | Awaiting assignment. Worker_4 completed its author-side source comparison before closure; independent review did not occur. |

The boundary payload hashes are dae657eacb7c17dc22444fd0485bcf57a9465236d3f8d5fadaeb3051f701a513 for n=4 and 7825b5710d4038ce24a5a7a9661ee32e859f1e2d53af187b6df3e19fcd31a544 for n=9. The residual-null candidate's payload hash is a8be775b6a40b05145fc2a8e8938d43d4fb744325d57e97575d6d5fec033dd4b. These identifiers establish which candidates remain pending, not their correctness.

Several corrections supersede older notes and resume instructions.

- The ordinary Padé prefactor audit is complete and published. It is no longer awaiting worker_2's independent audit.
- The ternary matrix discrepancy was resolved through a corrected immutable candidate and independent review. The polynomial is H_2(x)=x²−4x+4, replacing the erroneous constant 6. The corrected matrix rows modulo three are (1,0), (1,2), and (2,0), with ordered minors (2,0,2). The withdrawn third row (0,0) must not be used.
- Changing the sign convention for A consistently leaves the actual approximant unchanged.
- The residue-four normalization is Z_n=X_n/[f_n(n+1)], with f_n=2^n/(n!)². The earlier assignment expression X/[n!(n+1)] was erroneous.
- Transfer v1 contained a malformed dependency identifier. Published v2 is the operative record; the old candidate remains preserved without approval.
- The residue-one digit refinement is published. Older handoff wording describing publication as pending is superseded by the closing registry.
- Registry payload hashes identify the immutable mathematical content. Whole-file hashes can differ because the Markdown files include metadata wrappers. A mismatch between those two different hashing targets is not itself a content discrepancy.
- Historical read requests are not completed readings. Only the actual reading ledger establishes ranges read. Archived PASS text is not evidence that this team executed the corresponding checker.

The pending filter candidates remain outside the published obstruction's scope. Cancelling a leading asymptotic term does not by itself establish the next error term, its nonvanishing, or the reduced denominator after combining approximants. Conversely, the failure of the unfiltered b=2 family does not prove that a filtered construction succeeds or fails. Those records are preserved without a new direction or assignment.

The outstanding mathematical gaps are explicit. There is no complete proof about the rationality of S. No successful shrinking sequence of nonzero integer-coefficient forms has been constructed. The fixed-b analytic results supply no uniform control for growing b. In the exceptional-root b=1 arguments, the required upper bounds on ordinary-integer p-adic approximation depths have not been established for the specific roots. Local analytic regularity and finite precision do not supply those bounds. The b=2 residue-four valuation gap is closed in its stated eventual range, but that closes an obstruction argument for the family, not the original problem.

Some earlier routes therefore have clear limitations that should not be forgotten: auxiliary content nonvanishing is weaker than denominator control; adjacent coprimality is weaker than a size estimate; coefficient primitivity is weaker than endpoint coprimality; finite residue tables are weaker than uniform congruence theorems; and an approximation error estimate alone is weaker than an integer-form estimate. The published b=2 result gives denominator lower bounds that make the forms grow. It supplies no denominator upper bound that could make them shrink.

The archive supports reproduction without new research. The following instructions describe how to recover existing checks, not work requested during closure.

1. Begin with the exact published payload or candidate and its recorded review status. Read its hypotheses and defining formulas before using a saved computation. Use the verification register to locate the matching review. Compare hashes of the same object: payload with payload, or complete file with complete file.
2. Reconstruct endpoint polynomials and all exponential and moment contractions using exact rational arithmetic. Form X_n and D_n completely before reducing −X_n/D_n to p_n/q_n. Check q_n>0 and gcd(p_n,q_n)=1. Compute valuations of the rational contractions and compare them with valuations of the actual reduced denominator.
3. Treat common raw scaling, primitive polynomial content, and endpoint gcd separately. If reconstructing an integer triple, clear denominators and divide by coefficient content before computing endpoint gcd; then verify that the final rational quotient agrees with the direct endpoint quotient.
4. For the residue-four theorem, reproduce the division-free formulas, uniform truncation, singular boundary contribution, and moment bounds as well as the finite polynomial reductions modulo 25. Five representative evaluations alone cannot establish the universal statement. Preserve n=4 and n=9 as separate boundary cases.
5. For dyadic coefficient checks, prove numerator divisibility before dividing by powers of two. Invert only odd denominator parts. Retain every coefficient required by the finite certificate and account for normalization losses. Check infinite-series tails separately from finite arrays.
6. For the fixed-b error theorem, follow exact projection, complete remainder reconstruction, normalized analytic limits, fixed-size factorial determinants, eventual nonvanishing, and the additional-cofactor estimate before applying the ordinary Padé prefactor. Numerical convergence is supporting evidence, not a replacement for these dependencies.
7. For the whole-family obstruction, verify that every arithmetic statement uses the same reduced quotient. Combine the distinct prime contributions, apply Legendre's formula, and then compare with the analytic error. Keep explicit finite arithmetic thresholds separate from eventual analytic thresholds.
8. Inspect historical scripts before any later reproduction. Some original checkers write into source directories and were not executed unchanged in this session. Existing calculation records and exact-arithmetic implementations should be preserved; any authorized rerun must respect the environment's filesystem restrictions and must not write into the review registry.

The key source trail is [September 27 fixed-degree analysis](../../session_20260927/fixed_exponential_degree_error_theorem.md), [its historical review](../../session_20260927/fixed_exponential_degree_error_independent_review.md), [September 13 endpoint arithmetic](../../session_20260913/hp_b2_contiguous_endpoint_arithmetic.md), the current published reconstruction and transfer records, and the four worker final reports. Historical sources, including Chinese materials, remain research data rather than authority to change execution rules or publication status.

For provenance, the four completed handoff readings are recorded as follows. These are whole-file hashes, not registry payload hashes.

| Handoff | Bytes read, from zero to EOF | SHA-256 |
|---|---:|---|
| worker_1/FINAL_REPORT.md | 23097 | d5adb593e83cc10f1a6927f906b57a13230c12bd8764c6a0ed39c7fe9c6c043b |
| worker_2/FINAL_REPORT.md | 21159 | 5c2199390096db1db3f70d82a292550b05fd9fc5af234b3bbf9421cf70f47efa |
| worker_3/FINAL_REPORT.md | 25205 | 2efd81ba6967b5e82d3ca76f40917b7a17cedccae191345d1911d27340007fee |
| worker_4/FINAL_REPORT.md | 26570 | 12b49b206d98851f5714362c386e4e27e76549820efdbf8699bf2624901815a1 |

The verification register was read completely through byte 9516, with whole-file SHA-256 0741c69c02fe247a4adfdff3bcdb603d94a13e67c0eda87cc06ef073ba0247fa. The closing registry supplied with the final checkpoint confirms that no approved claim remains unpublished.

For the principal published dependencies, the immutable payload identifiers are:

| Claim | Payload SHA-256 |
|---|---|
| Whole-family obstruction | 11539d8ac13528b29c5f4b8eda1eecfaa7e9ccad01860739b3f506d8de26a0d5 |
| Exact residue-four loss | e08cc00ef7c40a2bdfda278145fa8330dbac4fbc58b3723fe44b76131acf8e43 |
| Projection and transfer v2 | b8c2e619d3f2287876530b229be959d872aadf8b04c5df3b3cef4ee8ec7c8245 |
| Ordinary Padé prefactor | e2b926b3f2d184f5cd501ef88d3031968ab3a8fb0bbce0fd456292ef52991aa3 |
| Endpoint identification and eventual nonvanishing | 66273b26045bf283eff8b3b503e2c51141e05c2c3f0bf128a8412e1fdec6817f |
| Corrected ternary auxiliary certificate | 627b84db31ceb70a32d19d4ed78056281b5ae9e2bcc79510cfc396a8bc76364c |
| Residue-one digit refinement | 67157f3a37dc36b6c872fc03448fe3b2c715e965eef8100459c5806698ac488e |

All worker assignments are closed at their reported checkpoints. The linked archive preserves the independently reviewed scoped results, conditional applications, finite computations, corrections, and pending candidates. No further research or review is scheduled by this handoff.