> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

**Worker_2 final handoff — 29 September 2026**

This project has established neither rationality nor irrationality of e+pi. No complete independently verified proof of either conclusion is available. The principal completed results concern the exact reconstruction, asymptotic error, and arithmetic limitations of specified rational approximation families. In particular, the published obstruction for the matched b=2 family is a result about that construction; it does not settle the original problem.

Research is stopped under the user's explicit closing directive. No calculation remains in flight. The latest n=9 review assignment is closed before a new candidate audit: its immutable candidate has not been read or formally reviewed by worker_2. Previously completed computations at n=9 are preserved as computational evidence, with the narrower status explained below.

Paths in this document are relative to this report's directory, work/astra_20260929/worker_2. The authoritative publication index is the [verification register](../../astra_review_registry/VERIFICATION_REGISTER.md). Publication statuses below follow the registry supplied at closure. A published claim certifies its exact reviewed statement and hypotheses, not stronger conclusions.

**Conventions and the analytic result**

Write s=e+pi and rho=1+sqrt(2). In the convention R(1)=A(1)+Y s, the rational approximant is r_n=-A(1)/Y and its signed error is E_n=R(1)/Y=s-r_n. Let q_n be its positive reduced denominator. Reversing the sign convention for A changes the displayed endpoint quotient but does not change the consistently defined approximant or its denominator.

For each fixed integer b>=1, the published projection-and-transfer result gives eventual uniqueness up to scale, eventual nonvanishing of the matched endpoint Y, and

E_n=(-1)^n [4*pi/rho^(b+1)] rho^(-2n)(1+o(1)).

This is a theorem for each fixed b. It supplies no uniform estimate when b grows with n. Consequently, for a fixed b and any subsequence tending to infinity, q_n|E_n| tends to zero exactly when q_n/rho^(2n) tends to zero on that subsequence. An analytic approximation error alone supplies no upper bound for the actual reduced denominator.

The main records are:

- [Ordinary Padé prefactor](../../astra_review_registry/verified/worker3-ordinary-pade-prefactor-v1.md), authored by worker_3 and independently reviewed by worker_2. Its ordinary Padé assertion is unconditional: epsilon_n~(4*pi/rho)rho^(-2n). Its original matched-family corollary explicitly depended on a separate transfer theorem.
- [Exact projection and complete error transfer, v2](../../astra_review_registry/verified/worker2-fixed-b-projection-and-error-transfer-v2.md), authored by worker_2 and independently reviewed by worker_3. Payload SHA-256: b8c2e619d3f2287876530b229be959d872aadf8b04c5df3b3cef4ee8ec7c8245. This supplies the application proof, including the complete remainder and eventual endpoint nonvanishing, rather than using the conditional corollary to prove itself.
- [Normalized endpoint quotients and coefficient determinants](../../astra_review_registry/verified/worker2-normalized-endpoint-quotients-and-coefficient-determinants-v1.md), authored by worker_2 and independently reviewed by main. Payload SHA-256: bd991972dc81078f443b1f030fde5055a8616ce7a8f2e109a68c044cfb249218. It establishes the fixed analytic disk, normalization bounds, local uniform limits, and nonzero limiting Taylor coefficient determinants used in the application.
- [Finite Taylor coefficient factorization for factorial determinants](../../astra_review_registry/verified/fixed-size-factorial-determinant-finite-jet-factorization-v1.md), authored by main and independently reviewed by worker_2. Its uniform O(1/n) factorial-transform remainder must not be mistaken for an O(1/n) convergence rate of varying analytic coefficient determinants.

The detailed dependency map is preserved in [note 63](note_000063.md). Its then-pending publication descriptions are superseded by the current registry.

A further published arithmetic criterion is [fixed-b denominator accumulation](../../astra_review_registry/verified/fixed-b-denominator-accumulation-obstruction.md), authored by worker_2 and reviewed by main, payload 8856456ac04468cc66d2df3437479c78af462b09f4ec42934a54b4bd30c239d3. Under the displayed error asymptotic, if s=a/d is rational in lowest terms, every finite accumulation point L of q_n/rho^(2n) must lie in

{m*rho^(b+1)/(4*pi*d): m=1,2,3,...}.

Thus a finite algebraic accumulation point would contradict rationality. No such accumulation point has been established for the actual denominators. The fact that each normalized denominator is algebraic does not imply that its limit is algebraic. Unreviewed constructions in notes 19 and 23 show why the asymptotic and this discrete restriction alone are insufficient.

**Exact endpoint arithmetic and the completed b=2 obstruction**

For the b=2 arithmetic records, use the complete endpoint pair X_n,D_n defined in the [two-chart reconstruction](../../astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md). The rational endpoint quotient is X_n/D_n; the approximant to s in the convention above is its negative. Both signs have the same positive reduced denominator q_n. Define

f_n=2^n/(n!)^2, N_n=X_n/f_n, and Z_n=X_n/[f_n(n+1)].

The complete exponential and moment contractions are essential. Omitting a moment term can change the local valuation even at an index where the exponential part has the expected congruence. Also, the rational reconstruction identities and the large-prime local ideal theorem have different domains: the latter cannot be applied at three or five merely because the rational formulas remain valid there.

Worker_2's published arithmetic contributions include:

- [Ternary residue-two denominator theorem](../../astra_review_registry/verified/worker2-b2-ternary-residue-two-exact-denominator-v1.md), reviewed by worker_1, payload ba51fc9529c4fe1ea78ad46225229d224dc4c5ac36b4b80e067017230642ce38. For n>=5 with n congruent to 2 modulo 3, D_n is nonzero and v_3(D_n)=v_3(N_n)=v_3(n+1). Therefore v_3(q_n)=2v_3(n!) exactly. The proof handles arbitrary valuation depth; it is not extrapolated from the six diagnostic indices.
- [Residue-four numerator nonvanishing](../../astra_review_registry/verified/worker2-b2-residue-four-numerator-nonvanishing-v1.md), reviewed by worker_4, payload c45a87ae1556ffd2f129849b6d56ae3d029a23a6371b52174e3add2998ec7533. For every n>=4 congruent to 4 modulo 5, X_n and Z_n are nonzero. The proof uses the published D_n nonvanishing and the three ternary denominator statements for the same rational quotient. If X_n were zero, its reduced denominator would be one, contradicting the strictly positive ternary denominator valuation. This nonvanishing argument itself provides no quantitative upper bound for v_5(Z_n).

Worker_2 independently reviewed the following related conclusions, now published:

- [Ternary residue-one theorem](../../astra_review_registry/verified/worker4-b2-ternary-residue-one-conditional-denominator-v1.md): for n>=4 congruent to 1 modulo 3, N_n is a ternary unit. When D_n is nonzero, v_3(q_n)=2v_3(n!)+v_3(D_n)>=2v_3(n!)+1. Its explicit denominator hypothesis must be retained unless a separate result supplies it.
- [Five-adic residue-four cancellation](../../astra_review_registry/verified/main-b2-five-adic-residue-four-cancellation-v1.md): v_5(D_n)=v_5(n+1), hence D_n is nonzero, for n>=4 congruent to 4 modulo 5. The additional assertion Z_n belongs to 5 Z_5 begins only at n=9. Divisibility alone permits zero and gives no upper valuation bound.
- [Exact residue-four loss beyond n=9](../../astra_review_registry/verified/w3-b2-five-residue-four-loss-v1.md), payload e08cc00ef7c40a2bdfda278145fa8330dbac4fbc58b3723fe44b76131acf8e43: for n>=14 congruent to 4 modulo 5, Z_n is congruent to 20 modulo 25. Thus v_5(Z_n)=1 and v_5(q_n)=2v_5(n!)-1. The proof accommodates arbitrarily large v_5((n+1)/5). The threshold excludes the genuine exception n=9.

For the last theorem, worker_2 checked the uniform truncation, division-free normalization, singular exponential boundary, moment estimates, and direct polynomial reduction. Independent exact reconstructions at n=14,19,24,29,34 agreed with the theorem. Those representative computations supplement the uniform proof; they do not replace it. The audit record is in [note 147](note_000147.md), [note 148](note_000148.md), [note 149](note_000149.md), and [note 156](note_000156.md).

The registry now records [whole-family obstruction](../../astra_review_registry/verified/w3-b2-whole-family-obstruction-v1.md), authored by worker_3 and reviewed by worker_4, payload 11539d8ac13528b29c5f4b8eda1eecfaa7e9ccad01860739b3f506d8de26a0d5. Under its stated matching, denominator, and analytic dependencies, the complete matched b=2 integer-form family eventually diverges in magnitude. Worker_2 did not perform that synthesis review; this handoff refers to its exact published scope. It obstructs the intended shrinking-form argument within this family and leaves the rationality of e+pi unresolved.

The [residue-one digit refinement](../../astra_review_registry/verified/w3-b2-residue-one-digit-refinement-v1.md) is also now published, payload 67157f3a37dc36b6c872fc03448fe3b2c715e965eef8100459c5806698ac488e. Earlier statements that its publication was pending are obsolete.

**Boundary certificates: preserve their pending status**

The n=4 computation and candidate submission are finished. The [n=4 candidate](../../astra_review_registry/candidates/worker2-b2-n4-exact-boundary-certificate-v1.md) has payload SHA-256 dae657eacb7c17dc22444fd0485bcf57a9465236d3f8d5fadaeb3051f701a513. It remains awaiting independent reviewer assignment. Author-side transcription and integrity checks do not constitute independent approval.

The exact computed values are:

| Quantity | Exact value | Five-adic valuation |
|---|---:|---:|
| X_4 | 92521969330/9 | 1 |
| D_4 | -1754485920 | 1 |
| f_4 | 1/36 | 0 |
| Z_4 | 74017575464 | 0 |
| q_4=den(X_4/D_4) | 1579037328 | 0 |

The reduced endpoint quotient is -9252196933/1579037328. The complete normalized exponential and moment contributions to Z_4 are respectively 34338004520 and 39679570944. Their residues modulo 25 are 20 and 19, so Z_4 is congruent to 14 modulo 25. This is a concrete boundary obstruction to extending the numerator divisibility statement from n>=9 down to n=4.

The defining finite sums, moment table, raw endpoint scaling, and chart checks are preserved in the candidate and [note 167](note_000167.md). The transcription comparison is recorded in [note 170](note_000170.md), and the payload check in [note 175](note_000175.md). These are completed calculations, not work still in flight.

A separate, unreviewed rational enclosure in [note 199](note_000199.md) gives, for p=9252196933 and q=1579037328,

763611.549781869208 < q(e+pi)-p < 763611.549781869209.

The decimal endpoints are exact terminating rationals. This enclosure checks the sign and magnitude at one index; it supplies no asymptotic theorem or independent approval of the boundary candidate.

At n=9, the earlier exact reconstruction reported in note 148 gives exponential contribution 20 modulo 25, moment contribution 5 modulo 25, and Z_9 congruent to 50 modulo 125. Therefore that calculation gives v_5(Z_9)=2, unlike the valuation one for n>=14 on the progression. Together with the published denominator identity, it gives v_5(q_9)=0. Moments cannot be omitted at n=9.

The separate [n=9 candidate](../../astra_review_registry/candidates/w3-b2-n9-boundary-certificate-v1.md), authored by worker_3, has payload 7825b5710d4038ce24a5a7a9661ee32e859f1e2d53af187b6df3e19fcd31a544. The closure registry lists it as awaiting assignment, with no reviewer. Although the latest task proposed a preparatory review by worker_2, that candidate has not been read or compared with the saved calculation in this worker's actual ledger. No verdict is issued. The completed n>=14 theorem does not approve this boundary certificate.

**Dyadic work and its limitations**

The [finite dyadic reconstruction](../../astra_review_registry/verified/worker3-dyadic-finite-coefficient-verification-v1.md) was independently reviewed by worker_2 and is published. The fresh reconstruction matched all twenty arrays H,K,A,B,C on the disks a+8 Z_2 for a=1,3,5,7 modulo 1024. It checked exact denominator divisibility before modular inversion: 400396 coefficient divisibility checks passed. The historical source checker was inspected but not executed unchanged.

The separate [analytic tail and precision theorem](../../astra_review_registry/verified/worker2-dyadic-analytic-tail-and-precision-v1.md), authored by worker_2 and reviewed by worker_3, has payload 3b220a9384536f55319370fb83bde92220ecf1b8ea1e296bd0a6a6662f42d7ab. Its coefficientwise bounds are 5R/16-6 for the H,A kernels and 5R/16-7 for K,B. They justify the stated restricted-series convergence and the outer and inner truncations modulo 1024. Forming C=KA-HB loses no precision when the factors are integral. Dividing by four or eight loses two or three bits, leaving precision modulo 256 or 128. Division by the disk variable requires an exact zero constant coefficient, which was checked in the stated case.

These statements do not themselves identify every analytic germ with an endpoint denominator, or bound how closely ordinary integers can approach a specified dyadic root. The independently reviewed [finite-data counterexample](../../astra_review_registry/verified/worker3-finite-data-dyadic-depth-counterexample-v1.md) shows that the stated finite polynomial data and quantitative convergence conditions can coexist with arbitrarily deep approximation in constructed series. It does not assert that the project's specific roots have this behavior.

Worker_2's separate [residual and Haar-null approximation candidate](../../astra_review_registry/candidates/worker2-dyadic-linear-depth-residual-null-v1.md), payload a8be775b6a40b05145fc2a8e8938d43d4fb744325d57e97575d6d5fec033dd4b, remains under review with worker_3 assigned and no review recorded in the closing registry. Its asserted dense G_delta, Haar-null, and Hausdorff-dimension-zero conclusions must remain labelled unverified. No new review is requested during closure.

**Other completed audits and their boundaries**

The early cubic-gate and adjacent-content assignment is complete in [note 6](note_000006.md), using the original [cubic gate](../../session_20260927/hp_b2_cubic_maximal_minor_gate.md), [adjacent-content report](../../session_20260927/hp_b2_adjacent_content_coprimality.md), and [endpoint arithmetic](../../session_20260913/hp_b2_contiguous_endpoint_arithmetic.md). Sixteen independent symbolic residuals vanished. The audit checked full-depth local ideals, state primitivity, the integral Bezout obstruction, prime restrictions, and nonvanishing of the auxiliary content Omega_n. The endpoint-gcd inequality requires the matching and Taylor conditions and the stated cutoff p>2n+4. Adjacent large-prime support exclusion uses its own cutoff p>2n+6. Neither nonvanishing nor adjacent support exclusion controls the size of individual content or the actual reduced denominator. This archived composite audit is not a separately published worker_2 claim.

The related [large-prime coefficient normalization](../../astra_review_registry/verified/b2-large-prime-content-normalization.md) is independently reviewed and published. Its raw endpoint common factor is (-1)^n/[4(n+1)^3(n!)^4]. The coefficient-content conversion and the endpoint-gcd implication retain their different prime cutoffs.

Additional worker_2 reviews now published are:

- [Microscopic reference estimates and cofactor bound](../../astra_review_registry/verified/worker3-microscopic-reference-and-sharp-cofactor-bound-v1.md). The scoped bound is |(N/D_V)/(W(0)/V(0))| <= C_b |V(0)|/[n! n^(2b+1)] with the source's definitions. This upper bound alone does not assert a signed leading equivalent or optimality.
- [Cofactor leading term](../../astra_review_registry/verified/w3-cofactor-leading-v1.md). The separately audited endpoint specialization has constant (-1)^b b! 2^((1-b)/2) exp(-sqrt(2)) under its explicit normalization and application hypotheses.
- [Multiples-of-five obstruction](../../astra_review_registry/verified/w3-b2-five-multiples-obstruction-v1.md). Its denominator bound holds on the stated progression from n=5; the real linear-form lower bound has a separate unspecified asymptotic threshold. Those thresholds must not be conflated.
- [Five-adic residue-three loss](../../astra_review_registry/verified/w3-b2-five-residue-three-loss-v1.md). The congruence calculation includes the complete numerator. Eventual nonvanishing is supplied by a separate published endpoint-identification result, rather than assumed at every index.

The original prefactor audit is finished and published; stale resume instructions calling it pending must not restart it. The earlier ternary matrix discrepancy is likewise superseded by the published [corrected unit-minor certificate](../../astra_review_registry/verified/b2-ternary-zero-diredacted_historical_name.md), authored by worker_4 and reviewed by worker_1. Worker_2 makes no separate certification of that corrected matrix in this handoff.

**Corrections, reproducibility, and remaining gaps**

The first projection-and-transfer candidate contained a malformed 65-character ordinary Padé dependency identifier. Its mathematical content was preserved in v2 with the corrected identifier e2b926b3f2d184f5cd501ef88d3031968ab3a8fb0bbce0fd456292ef52991aa3. The read-only comparison established that this was the sole mathematical-payload edit. The old [v1 candidate](../../astra_review_registry/candidates/worker2-fixed-b-projection-and-error-transfer-v1.md) remains an archival, unapproved record; use published v2. The invalid truncated n=4 hash in note 193 was explicitly corrected in note 194; the full valid hash is recorded above.

To reproduce the principal checks:

1. Start with the exact published statement or immutable candidate and its defining formulas. Distinguish a payload hash from the hash of the whole Markdown file, which also contains registry metadata. The recorded byte intervals in the reading ledger and integrity notes identify what was actually hashed.
2. For endpoint arithmetic, construct the defining polynomials and all exponential and moment contractions over exact rationals. Form X_n,D_n before reducing their quotient. Then compute f_n,N_n,Z_n and prime valuations. Do not replace the complete numerator by a truncated exponential contraction at a boundary index.
3. For the n=4 certificate, use its self-contained polynomial coefficients, contraction definitions, and moment table. As a short scalar cross-check after reconstruction, verify X_4/D_4=-9252196933/1579037328 and X_4/[5*(1/36)]=74017575464. This checks saved arithmetic only; it does not independently reconstruct the finite sums.
4. For the residue-four theorem, check the uniform tail and moment bounds as well as the finite polynomial reduction modulo 25. Reproducing the five representatives alone is insufficient to prove the progression theorem.
5. For dyadic arrays, form numerator coefficients exactly, divide by the full power of two only after proving divisibility, and invert only the odd denominator part. Track every bit lost under subsequent normalization. Reproduce the analytic tail argument separately from the retained finite arrays.
6. For analytic transfer, verify the exact projection, complete remainder, normalization denominators, fixed-disk convergence, determinant nonvanishing, and cofactor estimate before applying the ordinary Padé prefactor. Numerical convergence checks are supporting evidence only.

The saved controller computation records and the linked notes preserve the executed checks. Historical scripts that write into source directories were not executed unchanged; reruns should remain read-only or place any output solely in the permitted output directory. No internet research was used for this worker's work.

The unresolved points are now archival boundaries, not assignments to continue research: no complete proof decides e+pi; the fixed-b results supply no growing-b uniformity; local analytic information does not give the missing ordinary-integer approximation-depth estimates at specified dyadic roots; the n=4 and n=9 boundary candidates have no recorded independent approval; and the residual/Haar-null candidate remains under review. Other pending filter, determinant-growth, and digit-bound candidates in the registry are outside worker_2's completed review scope and must remain pending in the integrated report.

The completed b=2 obstruction should be preserved as a negative result for that particular method. It neither constructs a successful shrinking subsequence nor proves that every possible approximation method fails. All existing material is retained, with published claims separated from author computations and unreviewed candidates. Worker_2 closure is complete.