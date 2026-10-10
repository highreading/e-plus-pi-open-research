> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

Worker_3 final research handoff — 29 September 2026

The original problem is not solved. This research has not produced a complete independently verified proof that e+π is rational or irrational. The strongest completed conclusion relevant to worker_3 is an obstruction for the specified matched b=2 approximation family: its reduced integer-coefficient forms eventually grow in absolute value under the published synthesis’s explicit hypotheses. This is a conclusion about that family, not about the rationality of its target.

This handoff closes worker_3 at the existing checkpoint in response to the explicit instruction to end research and organize the results. No calculation remains in flight. Existing notes, calculations, candidates, and verified records should be preserved. Publication status below follows the registry snapshot supplied at closing; the report itself does not grant independent approval.

Links are relative to this file’s intended location, work/astra_20260929/worker_3/FINAL_REPORT.md. The central navigation record is [VERIFICATION_REGISTER.md](../../astra_review_registry/VERIFICATION_REGISTER.md). Candidate payload hashes identify the immutable submitted content; complete files can have different hashes because their metadata wrappers are additional bytes.

The approximation convention and the arithmetic criterion are essential to interpreting the results. Write S=e+π and ρ=1+√2. In the convention R(1)=X+YS, the rational approximant is −X/Y. If −X/Y=p_n/q_n is reduced with q_n>0, then

L_n=q_nS−p_n=q_nR(1)/Y.

The coefficients of L_n are integers; L_n itself is not known to be an integer. Under the hypothetical equality S=u/v, the quantity vL_n would be an integer. Eventual nonzero error together with L_n→0 along an unbounded subsequence would contradict that hypothesis.

The alternate polynomial convention R=B exp(z)+CF−A gives the same approximant A(1)/Y when A is changed consistently. The earlier contrary wording in note_000071.md was corrected in note_000072.md. There is no change of rational approximant or signed error under this consistent conversion.

For the complete b=2 endpoint contractions used in the arithmetic records, the approximant is −X_n/D_n. Records using X_n/D_n have the same positive reduced denominator q_n. These are denominators of the actual rational endpoint values, not polynomial coefficient contents or auxiliary maximal minors.

The following analytic results are independently reviewed and published within their stated scopes.

| Record | Precise contribution and qualification |
|---|---|
| [Ordinary Padé prefactor](../../astra_review_registry/verified/worker3-ordinary-pade-prefactor-v1.md) | Proves ε_n=|π−f_n|∼(4π/ρ)ρ^(−2n). Its matched-family consequence explicitly depends on the fixed-b transfer theorem. Reviewed by worker_2. |
| [Conditional matched endpoint transfer](../../astra_review_registry/verified/worker3-fixed-b-matched-endpoint-transfer-conditional-v1.md) | Exact projection, complete remainder, matching, and fixed-b transfer, conditional on its factorial-determinant lemma. Reviewed by main. The separately cited determinant result is now published; the immutable claim retains its conditional wording. |
| [Projection and error transfer v2](../../astra_review_registry/verified/worker2-fixed-b-projection-and-error-transfer-v2.md) | Worker_2’s independently reviewed fixed-b treatment. Worker_3 checked the complete remainder, signs, ranks, normalizations, and application hypotheses. This is the operative published version; the older unapproved v1 should not be presented as an additional unresolved dependency. |
| [Microscopic reference and sharper cofactor bound](../../astra_review_registry/verified/worker3-microscopic-reference-and-sharp-cofactor-bound-v1.md) | Quantitative microscopic reference estimates and the additional-cofactor bound stated below. Reviewed by worker_2. |
| [Leading cofactor term](../../astra_review_registry/verified/w3-cofactor-leading-v1.md) | Full factorial-determinant leading term and its conditional endpoint specialization. Reviewed by worker_2. Fixed degree and the exact source normalizations remain essential. |
| [Endpoint identification and eventual D nonvanishing](../../astra_review_registry/verified/w3-b2-eventual-d-nonzero-v1.md) | Identifies the two-chart denominator with the matched b=2 endpoint at the same index and proves eventual nonvanishing. Reviewed by worker_1. It is not an all-index nonvanishing theorem. |

Together, the ordinary prefactor and fixed-b transfer give, for each fixed b,

S−p_n/q_n=(−1)^n[4π/ρ^(b+1)]ρ^(−2n)(1+o(1)).

Consequently, along any unbounded subsequence with b fixed,

|L_n|=[4π/ρ^(b+1)](q_n/ρ^(2n))(1+o(1)).

Thus the forms shrink along that subsequence exactly when q_n/ρ^(2n) tends to zero. Existence of a shrinking subsequence is equivalent to liminf q_n/ρ^(2n)=0. A strict exponential denominator upper bound is sufficient, but not necessary: a polynomial saving below ρ^(2n) would also suffice. Equality of exponential rates alone is inconclusive because the subexponential factor matters. No estimate uniform in growing b follows from these fixed-b statements.

The published microscopic estimate uses the source’s monic Legendre reference polynomial p_{n+1} and gives p_{n+1}(z/n)/p_{n+1}(0)→exp(−√2z), with relative error O_K(1/n) on fixed compact sets. The normalized high-row and V factors have the stated O(n^(−2)) convergence. The argument does not infer the same rate for W merely from the ordinary-error prefactor.

In the exact determinant notation of the linked cofactor records, the sharper bound is

|(N/D_V)/(W(0)/V(0))|=O_b(|V(0)|/[n! n^(2b+1)]).

The leading-term specialization is

n! n^(2b+1) N/[D_V W(0)] → (−1)^b b! 2^((1−b)/2) exp(−√2).

The definitions, row order, factorial indices, and endpoint hypotheses are part of those records. The limit does not supply an unstated O(1/n) convergence rate for every varying coefficient determinant. Neither cofactor result controls the actual reduced denominator.

For the endpoint identification, the exact common scalar is

Y_raw=α_nD_n,  α_n=(−1)^n/[4(n+1)^3(n!)^4]≠0.

The raw coefficient vector is 2^(n+1) binom(2n+2,n+1) times the matched theorem’s signed cofactor vector, with no index shift. Eventual nonvanishing follows from this identification and the matched theorem. Endpoint nonvanishing and approximation-error nonvanishing have separate eventual thresholds. The finite boundary example n=b=1 has Y=0, so replacing eventual nonvanishing by all-index nonvanishing would be incorrect.

The arithmetic results below are also independently reviewed and published.

| Record | Result and scope |
|---|---|
| [Multiples-of-five obstruction](../../astra_review_registry/verified/w3-b2-five-multiples-obstruction-v1.md) | For 5∣n, n≥5, the stated local inputs give q_n≥(3√5)^n/(9n^4). The corresponding matched forms diverge eventually. Reviewed by worker_2. The source’s hypotheses and separate eventual analytic threshold remain explicit. |
| [Five-adic residue-three loss](../../astra_review_registry/verified/w3-b2-five-residue-three-loss-v1.md) | For n≥8, n≡3 mod5, X_n/f_n≡1 and D_n≡0 mod5, where f_n=2^n/(n!)². Whenever D_n≠0, v_5(q_n)=2v_5(n!)+v_5(D_n)≥2v_5(n!)+1. Reviewed by worker_2. Eventual D nonvanishing makes this unconditional eventually. |
| [Five-adic residue-four loss](../../astra_review_registry/verified/w3-b2-five-residue-four-loss-v1.md) | For n≥14, n≡4 mod5, Z_n=X_n/[(n+1)f_n] satisfies Z_n≡20 mod25. Hence v_5(Z_n)=1 and v_5(q_n)=2v_5(n!)−1. Reviewed by worker_2. The index n=9 is explicitly excluded. |
| [Whole matched b=2 family obstruction](../../astra_review_registry/verified/w3-b2-whole-family-obstruction-v1.md) | Conditional eventual divergence of the specified matched forms and their nonzero integer multiples. Reviewed by worker_4. The immutable statement retains its residue-four hypothesis H4, whose supporting theorem is now separately published. |
| [Residue-one form growth](../../astra_review_registry/verified/worker1-b2-five-adic-residue-one-form-growth-v1.md) | Worker_1’s synthesis, independently reviewed by worker_3. Arithmetic bounds hold for every n≥6, n≡1 mod5; matched-family identification and analytic growth remain eventual. |

The whole-family synthesis combines all three ternary classes and all five five-adic classes for n≥max(14,N_D), where N_D is an unspecified eventual-nonvanishing threshold. In particular, its explicit local premises give

q_n≥3^(2v_3(n!))5^(2v_5(n!)−1)≥(3√5)^n/(1125n^4).

With the b=2 error asymptotic, this implies, for all sufficiently large n,

|q_nS−p_n|≥[2π/(1125ρ³)] n^(−4) [3√5/ρ²]^n.

The exponential base is approximately 1.15094583649, with logarithmic margin approximately 0.140584070846. The strict inequality that the base exceeds one has an exact proof in the synthesis; these decimal values only describe its size.

The conclusion also applies to any nonzero integer multiple of an individual reduced form. It does not apply automatically to combinations involving different approximants. If an integer polynomial normalization introduces a common divisor into the endpoint pair, its endpoint form is a nonzero integer multiple of the reduced form, so an endpoint coprimality assumption is unnecessary for this implication.

This is a negative result for the specified irrationality construction. Divergence of these forms does not prove rationality, and a rational target can be compatible with exponential approximation errors accompanied by sufficiently large denominators.

One worker_3 arithmetic refinement is independently approved but not yet published in the supplied snapshot. The exact candidate [w3-b2-residue-one-digit-refinement-v1](../../astra_review_registry/candidates/w3-b2-residue-one-digit-refinement-v1.md), reviewed by worker_1, has payload SHA-256

67157f3a37dc36b6c872fc03448fe3b2c715e965eef8100459c5806698ac488e.

For n≥6, n≡1 mod5, it gives

q_n≥3^(η_n)(3√5)^n/[9√5 n²(n−1)²],

where η_n=1 if n≡1 mod3 and η_n=0 otherwise. Its analytic consequence has a separate unspecified eventual threshold. The [recorded review](../../astra_review_registry/reviews/w3-b2-residue-one-digit-refinement-v1-worker_1.md) requests no correction. The lead may publish this already approved exact payload through the existing gate during closing. Stronger constants discussed in [note_000123.md](note_000123.md) and [note_000136.md](note_000136.md) remain unreviewed addenda and must not be substituted into the immutable approved or published records.

The dyadic work established several scoped facts and limitations.

| Record | Verified scope |
|---|---|
| [Finite dyadic coefficient reconstruction](../../astra_review_registry/verified/worker3-dyadic-finite-coefficient-verification-v1.md) | Fresh exact reconstruction of every retained H,K,A,B,C coefficient on four odd disks modulo 1024. Reviewed by worker_2. Infinite-tail interpretation and actual endpoint transfer are separate issues. |
| [Dyadic analytic tails and precision](../../astra_review_registry/verified/worker2-dyadic-analytic-tail-and-precision-v1.md) | Worker_2’s coefficientwise convergence, truncation, and normalization theorem, independently reviewed by worker_3. Division by 4 retains modulus 256; division by 8 retains modulus 128. |
| [Conditional depth and index gaps](../../astra_review_registry/verified/conditional-dyadic-depth-and-index-gaps.md) | Main’s conditional necessity theorem, independently reviewed by worker_3. It preserves the assumed denominator and error estimates and allows infinitely many sufficiently sparse surviving indices. |
| [Algebraic-root depth obstruction](../../astra_review_registry/verified/worker3-algebraic-dyadic-root-depth-obstruction-v1.md) | Elementary logarithmic upper bound on integer approximation depth at an algebraic dyadic root. Reviewed by worker_1. Algebraicity of the project’s specified root is not established. |
| [Finite-data counterexample](../../astra_review_registry/verified/worker3-finite-data-dyadic-depth-counterexample-v1.md) | Under its stated admissibility conditions, prescribed finite polynomial data and quantitative convergence are compatible with a simple root having very deep integer approximations. Reviewed by worker_2. This constructs other germs, not the project’s germ. |
| [Simple-root precision transfer](../../astra_review_registry/verified/worker3-simple-root-precision-transfer-v1.md) | Sharp accounting of normalization losses and index-coordinate precision. Reviewed by worker_1. Exact division by Y requires an exact zero constant coefficient. |

The finite reconstruction used outer cutoff R<55, inner cutoff j<20, 784 outer pairs per disk, and a 60-bit working modulus. It performed 6268 denominator-divisibility checks; every retained coefficient agreed with the archived target and the difference list was empty. The largest denominator valuation was 50, leaving the required ten output bits. This execution is documented in [calculation_000009.py](calculation_000009.py) and [note_000010.md](note_000010.md).

The analytic tail estimates are distinct from that finite computation. For slope eight, the audited lower bounds are 5R/16−6 for H and 5R/16−7 for the division-free K kernel. They justify omission of R≥55 at the required precision. The normalized simple-root computation yields the exceptional index residue 79 modulo 1024, with its coordinate precision accounted for. This residue is not a bound on how closely large ordinary integers can approximate the full dyadic root.

The algebraic-root lemma says that if α∈Z_2, P∈Z[x] is nonzero with P(α)=0, d=deg P, and A is the sum of absolute values of its coefficients, then

v_2(n−α)≤d log_2 n+log_2 A

for positive integers n with P(n)≠0. Consequently, a requirement v_2(n−α)≥ηn−K log_2(n+2), with η>0, can hold only finitely often for algebraic α. The needed algebraicity hypothesis is not known for the particular exceptional germ root.

The counterexample record explains why the finite coefficient certificate, rational coefficients, convergence, and a simple-root theorem do not supply that missing arithmetic information. Such general properties can coexist with a transcendental root having very deep sparse integer approximations, even under prescribed odd-modulus congruences. The actual root is not identified with any constructed example.

For precision transfer, knowing a germ modulo 2^N and dividing by 2^s leaves N−s normalized bits when N>s. Under the simple-root hypotheses, a coordinate change X=r+2^hY converts this to N−s+h bits for the corresponding index root. A separate exact Y factor can be removed only after proving the constant coefficient is exactly zero. Generic sharpness examples establish limitations of finite precision; they do not give additional bits for the project germ.

A completed preliminary review has a publication-workflow issue that must remain visible. The candidate [worker2-dyadic-linear-depth-residual-null-v1](../../astra_review_registry/candidates/worker2-dyadic-linear-depth-residual-null-v1.md), payload

a8be775b6a40b05145fc2a8e8938d43d4fb744325d57e97575d6d5fec033dd4b,

was mathematically assessed by worker_3. The preserved substantive review is [note_000047.md](note_000047.md). It checks, for fixed c>0 and an odd modulus, the residual, Haar-null, and Hausdorff-dimension-zero statements for the linear-depth approximation set. It does not determine membership of a specified project root. Two review submissions returned the exact registry error “wrong candidate version or status”; neither established acceptance. The closing registry still lists this claim as under_review with no review record. It must remain outside the verified collection. Closing does not restart that audit or retry the gate.

The completed n=9 boundary calculation remains an unapproved candidate. The record is [w3-b2-n9-boundary-certificate-v1](../../astra_review_registry/candidates/w3-b2-n9-boundary-certificate-v1.md), payload SHA-256

7825b5710d4038ce24a5a7a9661ee32e859f1e2d53af187b6df3e19fcd31a544.

The exact author calculation retained both complete exponential contractions, both moment contractions, and the auxiliary correction. It checked the exponential contractions separately against their Rodrigues expansions. Its recorded values are

D_9=−16288952758072398513390080,

X_9=30686517292378474786419257881060/321489,

−X_9/D_9=1534325864618923739320962894053/261835956661996866283563171456.

For f_9=2^9/(9!)²=1/257191200 and Z_9=X_9/(10f_9), the certificate gives

Z_9=2454921383390277982913540630484800,

Z_9/25=98196855335611119316541625219392≡17 mod625.

Thus the author-established valuation is v_5(Z_9)=2, with leading unit 2 modulo five. The complete exponential contribution is 95 modulo 125, and the moment contribution is 80 modulo 125; their sum is 50 modulo 125. The moments are indispensable at this boundary.

The deductions are v_5(X_9)=1, v_5(D_9)=1, and v_5(q_9)=0. Independent integer gcd reduction found gcd 20 before reduction, and the candidate includes a Bézout certificate for the displayed reduced fraction. Extending the published n≥14 residue-four formula to n=9 would instead predict v_5(q_9)=1, so the finite calculation identifies a concrete boundary exception at the author-verification level.

The full computation is [calculation_000140.py](calculation_000140.py); its result and certificate consolidation are in [note_000141.md](note_000141.md) and [note_000145.md](note_000145.md). Independent review has not been assigned in the closing snapshot. A future review, if separately authorized, would need to check the complete endpoint contractions against their definitions, not merely the final fraction reduction. The result remains separate from the published n≥14 theorem and the eventual whole-family obstruction.

A supplementary author computation using rational series enclosures found a strictly negative error S−p_9/q_9 for the displayed fraction. See [calculation_000156.py](calculation_000156.py) and the rounding clarification in [note_000158.md](note_000158.md). The tighter internal rational interval and its coarser outward-rounded display have different widths; this was checked and is consistent. This supplementary finite check is also unreviewed and does not independently certify the endpoint identification.

The latest assignment concerned worker_4’s three-term filter. The full [source note](../worker_4/note_000181.md) and [registered candidate](../../astra_review_registry/candidates/worker4-b2-three-term-filter-denominator-v1.md) were returned and read completely at the existing checkpoint. The candidate has registry payload

41527527f21a77d80f491516b9a2ca7f0386a152bd1afac6cfdc2ebbec48cbd0.

The bounded closing assessment concerns the abstract arithmetic implication only. Let r_k=p_k/q_k be reduced, q_k>0, and let Q_n be the positive reduced denominator of

t_n=(r_n+6r_{n+1}+r_{n+2})/8.

Assume eventual A3 and A5 for this same rational sequence: the stated exact ternary denominator valuations on residues zero and two, a strictly larger ternary valuation on residue one, the exact five-adic valuations on residues one and two, a strictly larger five-adic valuation on residue three, and the residue-four upper bound. All required rational values must be defined.

For n≡2 mod3, put a=v_3(n!) and s=v_3(n+1)≥1. At sufficiently large indices the three summands before division by eight have ternary valuations

−2a, 1−2a−2s, −2a−2s−δ_3(n+2),

where δ_3(n+2)≥1. The third is uniquely smallest. Hence v_3(Q_n)=v_3(q_{n+2})≥2a+3. The factor six contributes exactly one ternary valuation; eight is a ternary unit.

For n≡1 mod5, the three factorial valuations coincide and the third summand uniquely has least valuation. For n≡2 mod5, the middle summand uniquely has least valuation. The factors six and eight are five-adic units. The residue-four summand needs only a valuation lower bound; it may be zero or have a five-adic-unit denominator. Therefore v_5(Q_n)≥2v_5(n!)+1 in both cases.

The CRT intersections are exactly n≡11 and 2 modulo 15. On these progressions the conditional conclusion is

Q_n≥135·3^(2v_3(n!))5^(2v_5(n!))≥3(3√5)^n/(5n^4),

so log Q_n≥n log(3√5)−O(log n). This follows from Legendre’s formula and the displayed coarse digit-sum bounds. The candidate’s stronger residue-four upper bound is sufficient; the preliminary note’s weaker bound already suffices for uniqueness of the minimum.

No defect was identified in this elementary implication under its explicit hypotheses. This closing assessment is not an accepted registry review. The candidate remains awaiting assignment, and its application-specific source identification has not been newly certified by worker_3. The unique minimum proves that t_n is nonzero; it does not prove that S−t_n is nonzero. The leading matched errors cancel under this filter, and the denominator estimate supplies no lower bound for the remaining error. Consequently it does not prove divergence of Q_n(S−t_n), exclude every shrinking filtered subsequence, or decide the original rationality problem.

The following evidence pointers support reproducibility without reopening completed work.

| Preserved artifact | What its recorded execution checks |
|---|---|
| [calculation_000009.py](calculation_000009.py) | Exact finite dyadic coefficient reconstruction on all four odd disks. Its successful result is recorded in note_000010.md. |
| [calculation_000071.py](calculation_000071.py) | Eighteen exact parameter pairs, 121 orthogonality checks, original Taylor equations, matching, ranks, complete remainder coefficients, and determinant signs. The successful result is recorded in note_000072.md. Finite cases do not prove asymptotics. |
| [calculation_000102.py](calculation_000102.py) | Complete residue-three endpoint reconstructions at n=8,23,28. The triples (v_5(D),v_5(X),v_5(q)) are (1,−2,3), (2,−8,10), and (1,−12,13). |
| [calculation_000110.py](calculation_000110.py) | Immutable payload identification and digit bookkeeping at 3999 indices for the residue-one synthesis review. It does not reprove the imported local endpoint theorems. |
| [calculation_000125.py](calculation_000125.py), [calculation_000127.py](calculation_000127.py) | Bounded residue-four exploratory reductions and representative coefficient calculations. The universal theorem rests on the published symbolic proof, not sample periodicity. |
| [calculation_000140.py](calculation_000140.py) | Complete n=9 rational endpoint contractions and independent Rodrigues comparisons; this certificate remains unapproved. |
| [calculation_000156.py](calculation_000156.py) | Supplementary rational enclosures for the displayed n=9 approximant; author evidence only. |

For reproduction, inspect each preserved calculation’s imports and inputs, and use the authorized isolated Python compute environment with its existing limits. Standard exact-integer and Fraction arithmetic suffice for the finite endpoint and reduction certificates. Where needed, the existing SymPy/mpmath library directory is [private local path removed] No installation or network research is required. Preserve project sources and the registry as read-only inputs, and keep any permitted output in the authorized worker output directory. Historical checkers that write beside their source files should not be executed unchanged.

Read the cited verified statement and its review together when checking a theorem. A successful archived computation is evidence only for its actual tested identities and range. The reading ledger records completed byte ranges and whole-file hashes; an earlier read request by itself is not proof of completed reading. No historical PASS label, numerical agreement, or peer consensus is treated here as a complete proof.

The closing distinctions are these: the published prefactor audit is complete; the corrected ternary matrix certificate with third row (2,0) is already published within its scope, so the stale (0,0) discrepancy must not be represented as unresolved; the whole-family synthesis remains conditionally worded even though its residue-four supporting theorem is published; the approved digit refinement awaits only publication in the supplied snapshot; and the n=9 certificate, residual-null gate issue, and three-term filter candidate remain outside the verified collection.

The remaining mathematical gaps are unchanged. No successful sufficient denominator upper bound has been obtained for an irrationality proof. The specific exceptional dyadic root’s arithmetic approximation depth is not settled by finite data. Fixed-b estimates provide no growing-b uniformity. Filtered errors lack the needed established nonzero lower asymptotic. These are descriptions of the final research status, not new assignments. Worker_3 is closed, with no proof_candidate claiming a resolution of e+π.