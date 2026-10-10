> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

Worker_1 final handoff — 29 September 2026

**This project has not solved whether e+pi is rational or irrational.** No complete independently verified proof of either conclusion is available in this worker’s completed work. The results concern specified approximation families, their exact arithmetic, and limitations of proposed proof methods.

Research ends at the existing checkpoint in accordance with the explicit closing directive. No calculation is in flight. The newest assignment, preparation of an independent review of the n=4 boundary candidate, was not started before closing. It remains unreviewed. Earlier independent calculations at n=4 are preserved below, but they do not constitute a review of that immutable candidate.

This handoff preserves existing material through links and status distinctions. Paths are relative to this report’s location in work/astra_20260929/worker_1. Published status refers to the supplied review registry at closing. A published conditional theorem retains its hypotheses; publication does not establish a stronger conclusion.

**Endpoint conventions and the central distinction.** The matched b=2 construction uses rational polynomials A, B, C and a remainder R(z)=A(z)+B(z)e^z+C(z)F(z), with F(1)=pi and Y=B(1)=C(1). The arithmetic sources define a complete rational endpoint pair (X_n,D_n). Whenever D_n is nonzero, the approximation convention is

p_n/q_n = -X_n/D_n = -A(1)/Y,

where q_n>0 and gcd(p_n,q_n)=1. Consequently

q_n(e+pi)-p_n = q_n R_n(1)/Y_n.

The positive reduced denominator is also the denominator of X_n/D_n. For every prime p, the elementary identity

v_p(q_n)=max(0,v_p(D_n)-v_p(X_n))

holds for rational X_n and nonzero rational D_n. It needs no integrality assumption on either endpoint.

Polynomial coefficient content, the gcd of integer endpoint values, the auxiliary maximal-minor content Omega_n, and the actual reduced denominator are different quantities. If an integer polynomial triple has endpoint values a=A(1), y=B(1)=C(1)≠0, and g=gcd(|a|,|y|), then

q=|y|/g,  p=-sgn(y)a/g,

a+y(e+pi)=sgn(y)g[q(e+pi)-p].

Thus making the full polynomial coefficient vector primitive does not necessarily make the endpoint pair coprime. This distinction is documented in [the normalization assessment](note_000144.md) and demonstrated by the exact n=12 calculation below.

The audited identification with the ordered cofactor construction is

Y_raw=d_(n+1)Y_cof=alpha_n D_n,

alpha_n=(-1)^n/[4(n+1)^3(n!)^4].

This exact identity holds for n≥2 under the source normalizations. The published analytic argument also gives eventual D_n<0, with no effective starting index. See [the endpoint-identification theorem](../../astra_review_registry/verified/w3-b2-eventual-d-nonzero-v1.md). Its eventual conclusion must not be rewritten as nonvanishing at every index.

**Published findings authored by worker_1.** These five records have independent approval and publication in the supplied registry.

| Record | Exact scope and limitation |
|---|---|
| [Large-prime coefficient content and primitive normalization](../../astra_review_registry/verified/b2-large-prime-content-normalization.md) | For the rational b=2 triples and p>2n+2, identifies the minimum coefficient valuation with that of B. It makes the primitive scaling factor explicit. It does not bound the size of the actual denominator. |
| [Two-chart endpoint ideals and denominator identities](../../astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md) | Gives exact local chart identities, chart coverage, and reduced-denominator valuation formulas under the stated prime restriction and D≠0. These are identities, not denominator-growth estimates. |
| [Odd-prime interpolation tail cutoff](../../astra_review_registry/verified/odd-prime-interpolation-tail-cutoff-v1.md) | Improves coefficientwise truncation and characterizes optimal block cutoffs based on individual summands. It does not establish optimality after cancellation of the summed tail. |
| [Four ternary endpoint certificates](../../astra_review_registry/verified/worker1-b2-four-ternary-endpoint-certificates-v1.md) | Exact reconstruction at n=3,6,9,12 and full primitive normalization at n=12, independently reviewed by worker_4. These finite certificates are not an all-index theorem. |
| [Growth on n congruent to one modulo five](../../astra_review_registry/verified/worker1-b2-five-adic-residue-one-form-growth-v1.md) | Combines the matched-family error estimate with actual reduced-denominator arithmetic to establish exponential growth of the relevant integer forms on this progression. It supplies a limitation of this approximation method, not a rationality result. |

Their registered payload SHA-256 values, in the same order, are:

- a1e60ab2287008a0f177cf453b624f305f78327b23f4306abe5f555c5cd438dc
- ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d
- 2757da21024783fba7cd9c881de89c14db59b114a26787209ef0e639b8130799
- 52ab9bfa20ec804c2701c0c3adbee0c980eeda0a2f3db474b2c1183e912b7bed
- b67f9a7d1027f0019f1f0bcd6599e582cec92ae9858195b9a7959044d4435bd8

For the large-prime normalization result, let nu be the minimum coefficient valuation of the raw cross-product B. Under the stated source normalization and p>2n+2, the primitive endpoint-gcd valuation is min(v_p(X),v_p(D))-nu. Combining this with the separately audited auxiliary gate at p>2n+4 yields

min(v_p(X),v_p(D)) ≤ nu+v_p(Omega_n).

This inequality does not control the actual denominator without further information. In particular, it must not be applied at p=3 or p=5 when those primes violate the stated threshold.

For the interpolation result, let m=j+2k denote the summation weight in the source’s auxiliary double series. At an odd prime p and desired precision p^d, a sufficient coefficientwise truncation retains m<pK, where

K=max(1,ceil((p-1)(d-1)/(p-2))).

The underlying block valuation is g_p(k)=k-v_p(k!). The exact optimal cutoff for the individual-summand criterion uses the last k with g_p(k)<d. This function is not monotone: g_3(8)=6 but g_3(9)=5. A separate independently reviewed follow-up proves infinite sharpness and a logarithmic search interval; see [worker_4’s sharpness theorem](../../astra_review_registry/verified/odd-prime-cutoff-sharpness-and-logarithmic-search-v1.md).

**Completed independent reviews and substantive corrections.** Worker_1’s recorded approvals certify their exact scoped payloads, not the overall research goal. The following are principal completed audits; their full statements and review records remain authoritative.

- [Corrected ternary auxiliary certificate](../../astra_review_registry/verified/b2-ternary-zero-diredacted_historical_name.md): independently recovered H_2(x)=x^2-4x+4 and, coefficientwise on 3Z_3, the matrix [[1,0],[1,2],[2,0]] modulo 3. The ordered maximal minors are (2,0,2). The formerly reported third row (0,0) is incorrect and superseded. Both the finite arithmetic and the infinite coefficientwise tail argument were checked. This auxiliary certificate alone says nothing about unit actual denominators.
- [Algebraic dyadic root-depth obstruction](../../astra_review_registry/verified/worker3-algebraic-dyadic-root-depth-obstruction-v1.md): checked denominator clearing, divided-difference integrality, the direction of the valuation inequality, and integer-zero exceptions. Its fixed algebraic target hypothesis is essential. Algebraicity of the project’s exceptional root was not established.
- [Simple-root precision transfer](../../astra_review_registry/verified/worker3-simple-root-precision-transfer-v1.md): checked restricted-series root existence and uniqueness, root stability, all normalization losses, coordinate scaling, exact vanishing before division by the coordinate, and the sharpness examples. This general conditional lemma does not establish its hypotheses for every project germ.
- [Ternary denominator and reconstruction loss on 3|n](../../astra_review_registry/verified/b2-ternary-endpoint-denominator-and-content-v1.md): audited the complete contractions, factorial normalization, strict moment estimates, and coefficient-content argument. For n≥3 with 3|n, it gives v_3(q_n)=2v_3(n!) and the stated reconstruction-loss bound 0≤c≤floor(log_3 n).
- [Ternary denominator on n congruent to two modulo three](../../astra_review_registry/verified/worker2-b2-ternary-residue-two-exact-denominator-v1.md): audited arbitrary t=v_3(n+1), not merely t=1. For n≥5 on this progression, v_3(q_n)=2v_3(n!).
- [Five-adic denominator on multiples of five](../../astra_review_registry/verified/b2-five-adic-endpoint-denominator-v1.md), [residue one](../../astra_review_registry/verified/worker4-b2-five-adic-residue-one-exact-denominator-v1.md), and [residue two](../../astra_review_registry/verified/worker4-b2-five-adic-residue-two-exact-denominator-v1.md): audited all surviving exponential contributions, boundary terms, moment-denominator losses, endpoint nonvanishing, and actual reduced-denominator normalization. They give v_5(q_n)=2v_5(n!) for n≥5,6,7 respectively on the stated progressions.
- [Conditional coefficient content on the five-adic residue-two progression](../../astra_review_registry/verified/worker4-b2-five-adic-residue-two-conditional-content-v1.md): audited the common scalar, coefficient minima, reconstruction losses, and primitive endpoint gcd. Approval preserves the explicit endpoint hypotheses and 0≤c≤L. Sampled equality c=L is not a general theorem.
- [Eventual nonvanishing of D](../../astra_review_registry/verified/w3-b2-eventual-d-nonzero-v1.md): checked the exact ordered matrix, signed cofactors, scalar identification, and hypotheses of the published factorial-determinant argument. There is no effective threshold in this result.

The earlier ordinary Padé prefactor audit was performed by worker_2 and is already published. The old resume instruction identifying it as pending is stale. Similarly, the corrected ternary third row is resolved within the published auxiliary scope; it needs no renewed audit.

**Finite exact evidence and reproducibility.** These calculations used exact rational or integer arithmetic. Their finite scope is explicit. Successful sample reconstruction supports the associated derivations but does not replace general proofs.

For the source-scaled complete pair (X_n,D_n), the independently reconstructed ternary values are:

| n | v_3(X_n) | v_3(D_n) | v_3(q_n) |
|---|---:|---:|---:|
| 3 | -2 | 0 | 2 |
| 6 | -4 | 0 | 4 |
| 9 | -8 | 0 | 8 |
| 12 | -10 | 0 | 10 |

All three numerator terms were retained. The endpoint ratios were also checked against independently solved defining approximation systems. Each tested auxiliary matrix has minors (2,0,2) modulo 3, while every actual denominator in this table has positive ternary valuation. This explicitly rules out the inference from an auxiliary unit minor to a unit actual denominator.

At n=12, normalize the rational triple by B(1)=C(1)=1 and clear every coefficient denominator. The resulting integer coefficient vector has gcd 1, but its endpoint gcd is

73920=2^6·3·5·7·11.

The denominator-clearing factor has ternary valuation 11. The primitive endpoint valuations are v_3(A(1))=1 and v_3(B(1))=11, giving v_3(q_12)=10. The raw rational coefficient minimum has ternary valuation -31, the raw B endpoint has valuation -20, and Omega_12=2 has ternary valuation zero. These are compatible facts about distinct normalizations. See [the n=12 record](note_000064.md).

The following independent samples additionally corroborate the general local theorems:

| Audited progression | Indices checked | Resulting denominator valuations |
|---|---|---|
| 5|n | 5,10,15,25 | v_5(q)=2,4,6,12 |
| n≡2 mod3 | 5,8,11,26,80 | v_3(q)=2,4,8,20,72 |
| n≡1 mod5 | 6,11,26,126 | v_5(q)=2,4,12,62 |
| n≡2 mod5 | 7,12,27,127 | v_5(q)=2,4,12,62 |

The ternary residue-two samples cover t=v_3(n+1)=1,2,3,4. The five-adic residue-one and residue-two samples cover depth up to three in v_5(n-1) and v_5(n-2), respectively. Full raw reconstruction and independently solved approximation systems were included at the particular indices recorded in the scripts.

A separate coefficient calculation at n=7,12,27 gave reconstruction losses c=1,1,2 and exact primitive endpoint gcds 20, 73920, and 194941524377600. It checked that the full integer coefficient vectors have gcd 1. Its detailed checkpoint is [note_000130.md](note_000130.md); these examples do not strengthen the general inequality 0≤c≤L to equality.

Earlier independent boundary work at n=4 gave

D_4=-1754485920,

X_4=92521969330/9,

X_4/D_4=-9252196933/1579037328.

The ratio agrees with a directly solved approximation system, and (v_3(D_4),v_3(X_4),v_3(q_4))=(4,-2,6). These results are recorded in [note_000095.md](note_000095.md). They were obtained during the ternary residue-one preparation. They do not certify every exponential and moment contraction in the later n=4 five-adic candidate, whose formal review remains unperformed.

The main reproducibility entry points are:

| Script or record | Purpose |
|---|---|
| [calculation_000061.py](calculation_000061.py) | Complete endpoint reconstruction and independent defining-system comparison at n=3,6,9,12. |
| [calculation_000063.py](../worker_2/calculation_000063.py) | Full n=12 coefficient normalization and endpoint gcd. |
| [calculation_000081.py](calculation_000081.py) | Independent reconstruction on multiples of five. |
| [calculation_000086.py](calculation_000086.py) | Arbitrary-depth ternary residue-two sample validation. |
| [calculation_000106.py](calculation_000106.py) | Five-adic residue-one contractions and reconstruction. |
| [calculation_000119.py](calculation_000119.py) | Five-adic residue-two contributions and reconstruction. |
| [calculation_000188.py](calculation_000188.py) | Finite checks for the unreviewed digit-minima supplement. |
| [calculation_000202.py](calculation_000202.py) | Finite checks for the unreviewed parity supplement. |

For reproduction in an authorized calculation environment, inspect each script first, retain exact arithmetic and assertions, and use the project-provided SymPy/mpmath installation by adding [private local path removed] to sys.path when required. Resolve project paths against [private local path removed] Keep any generated output in the reproducing role’s authorized directory. Do not execute historical source checkers unchanged: some write into their source directories. No internet, package installation, subprocesses, or source-directory modification is required for the documented calculations.

Successful computation records are distinguished from failures. The initial symbolic validation failed at the SymPy import and produced no mathematical evidence; a subsequent calculation with the supplied library path passed. Early candidate-hash attempts also failed because a filename contained a literal redaction marker. Later successful checks reconciled the registered payload and whole-file hashes. A whole-file hash can differ from the payload hash because registry metadata is outside the hashed candidate content. Neither failure was treated as a successful verification.

**Analytic conclusions and negative results.** The source-bound assessment is in [note_000143.md](note_000143.md), with integer normalization in [note_000144.md](note_000144.md). For rho=1+sqrt(2), the published fixed-b=2 dependencies give the signed error

(e+pi)-p_n/q_n = (-1)^n (4pi/rho^3) rho^(-2n)(1+o(1)).

Its leading constant is positive. The statement concerns the same matched endpoint family and all sufficiently large integer indices, with an unspecified threshold. It uses [the complete fixed-b projection and error-transfer theorem, version 2](../../astra_review_registry/verified/worker2-fixed-b-projection-and-error-transfer-v2.md), [the ordinary Padé prefactor](../../astra_review_registry/verified/worker3-ordinary-pade-prefactor-v1.md), and the endpoint identification. Fixed-b statements must not be extrapolated to growing b without uniform estimates.

The separately reviewed [whole-family obstruction](../../astra_review_registry/verified/w3-b2-whole-family-obstruction-v1.md) is published with payload 11539d8ac13528b29c5f4b8eda1eecfaa7e9ccad01860739b3f506d8de26a0d5. Its exact conditional wording must be preserved. It concerns eventual divergence of the complete matched b=2 integer-form family under its listed premises. Its H4 premise is the exact residue-four loss formula

v_5(q_n)=2v_5(n!)-1 for n≥14, n≡4 mod5,

which has its own [published scoped record](../../astra_review_registry/verified/w3-b2-five-residue-four-loss-v1.md). The older residue-four cancellation theorem provided only an upper bound and was insufficient to supply this premise. The complete numerator theorem’s n≥14 range must not be replaced by the earlier range of an exponential-only congruence. In particular, n=9 requires separate boundary treatment.

Worker_4 performed the whole-family review; worker_1 supplied an analytic dependency assessment and statement comparisons, not a second formal approval of that synthesis. Divergence of these integer forms prevents this family from yielding the required shrinking forms. It does not imply that e+pi is rational, and it does not rule out unrelated approaches.

Other established limitations remain relevant: auxiliary content nonvanishing does not bound its size; adjacent auxiliary coprimality does not control individual actual denominators; finite p-adic coefficients do not establish an ordinary integer approximation-depth bound; and the fixed-algebraic-root obstruction does not establish algebraicity of a particular project root.

**Approved but awaiting publication.** The supplied registry records worker_1’s accepted APPROVED review of [w3-b2-residue-one-digit-refinement-v1](../../astra_review_registry/candidates/w3-b2-residue-one-digit-refinement-v1.md), payload

67157f3a37dc36b6c872fc03448fe3b2c715e965eef8100459c5806698ac488e.

The [recorded review](../../astra_review_registry/reviews/w3-b2-residue-one-digit-refinement-v1-worker_1.md) was read completely and confirms acceptance. Its whole-file SHA-256 is 3a05345160a60307f4f30c75fa6c1fb70ab2470dc780735b3e1f7e7e2dbe4428. The mathematical audit, payload verification, and finite checks are complete. Approval preserves the digit inequality’s hypotheses, the constant 9sqrt(5), actual reduced-denominator normalization, arithmetic range n≥6 on the specified progression, and a separate unspecified eventual analytic threshold. The supplied registry still has verified_path=null. The lead can publish this exact already-approved payload during closing without another audit. Repeated historical statements that its verdict remains outstanding are stale.

**Unreviewed material remains outside verified research records.** Two worker_1 supplements are registered but have no independent reviewer or approval:

- [worker1-digit-minima-and-conditional-denominator-bound-v1](../../astra_review_registry/candidates/worker1-digit-minima-and-conditional-denominator-bound-v1.md), payload 067ec2594e6d23d28cc4342397f71d62fed7517b3e4e86fa3d71191af3addc0a. It contains exact digit-minimum and equality assertions and a conditional two-prime denominator bound. Author validation and payload verification are complete. Its finite calculation recorded 40,970 digit checks, 238 minimum checks, 2,145 structured equality checks, and 202 conditional denominator checks. None establishes a new endpoint-valuation theorem.
- [worker1-parity-digit-denominator-bound-v1](../../astra_review_registry/candidates/worker1-parity-digit-denominator-bound-v1.md), payload 9677b1b1c9a80f4d833dd2ebdd9a2612ae352036e7625ac1fdb87821d3537150. For n≥6, n≡1 mod5, it assumes a positive integer q satisfying v_3(q)≥2v_3(n!) and v_5(q)≥2v_5(n!), and claims q>C_n(3sqrt(5))^n/[(n+1)^2(n+4)^2], with C_n=20sqrt(5)/3 for odd n and C_n=16 for even n. The strictness arguments and finite tests have author validation only. The calculation recorded 2,308 digit checks and 201 conditional denominator checks. This candidate is not independently approved.

Both supplements must remain clearly marked unverified at closing. No new reviewer appointments or audits are requested under the end-research directive.

The newest assigned candidate, [worker2-b2-n4-exact-boundary-certificate-v1](../../astra_review_registry/candidates/worker2-b2-n4-exact-boundary-certificate-v1.md), payload dae657eacb7c17dc22444fd0485bcf57a9465236d3f8d5fadaeb3051f701a513, remains awaiting_assignment in the supplied registry. This worker has not read or audited that immutable candidate. The previously obtained n=4 endpoint ratio is not a substitute for the requested complete contraction review. No verdict is issued. The [n=9 boundary candidate](../../astra_review_registry/candidates/w3-b2-n9-boundary-certificate-v1.md) likewise remains unapproved in the supplied registry and was not this worker’s completed review.

Supplementary notes on varying algebraic targets and finite coefficient-class root ambiguity also remain unreviewed. Their principal entry points are [note_000029.md](note_000029.md), [note_000033.md](note_000033.md), [note_000056.md](note_000056.md), and [note_000058.md](note_000058.md). They must not be promoted to verified project-germ assertions. Other workers’ unreviewed filtered-denominator and cancellation candidates receive no approval from this handoff.

**Source and closing index.** The original reconstruction sources actually read by this worker are [hp_b2_endpoint_attempt.md](../../session_20260913/hp_b2_endpoint_attempt.md), [hp_b2_contiguous_endpoint_arithmetic.md](../../session_20260913/hp_b2_contiguous_endpoint_arithmetic.md), and the [historical independent comparison](../../session_20260913/hp_b2_contiguous_endpoint_independent_review.md). Auxiliary interpolation was checked against [the original analytic certificate](../../session_20260927/literature_update_and_b2_analytic_certificate.md). Source assertions and historical PASS messages were treated as research data, not as this worker’s independent executions or as permission changes.

The unresolved mathematical gaps include effective all-index nonvanishing where only an eventual theorem exists, arithmetic hypotheses needed to apply general p-adic root lemmas to specific germs, and any argument producing suitable nonzero shrinking integer forms for the original constant outside the obstructed matched family. The unreviewed filters supply no established filtered-error lower bound or irrationality proof. These gaps are recorded for accuracy; no new investigation is initiated.

The remaining closing actions are organizational: preserve these artifacts, publish the exact already-approved digit-refinement payload through the existing gate, retain unreviewed candidates with pending status, and include this handoff in the lead’s integrated report and index. Worker_1 stops here without waiting for reassignment.