> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Research on the rationality of e plus pi

This report records the completed research stage begun on 2 October 2026. The rationality of S=e+π remains unresolved. The original planned families produced substantial auxiliary theorems and precise arithmetic obstructions.

Closeout began only after the actual account read at **2026-10-02 18:10:42 UTC**, or **2026-10-03 02:10:42 Asia/Shanghai**, showed **91% used and 9% remaining** in the available Codex seven-day window. At the preceding read, 18:04:40 UTC, remaining quota was exactly 10%, and research continued. The secondary window was unavailable; it was not treated as zero. The stop was triggered by quota, and main_problem_solved is false.

## Scope and evidence

Root and three existing subagents worked in separate directories. Arithmetic handled discrete and arithmetic mechanisms, selector handled selection and geometric mechanisms, and analysis handled analytic mechanisms. Analysis was the sole subagent assigned limited earlier reviews, then returned to original work.

Each selected target has an archive search and a public-literature gate in its proof note or ledger. Exact calculations, asymptotic proofs and finite receipts have separate scopes. A formula verified for several indices is not promoted to an all-degree theorem. An authored theorem remains an author-level result unless a particular narrow review is explicitly documented. None of these records is a published or independently validated solution of S.

The full original target sequence is in [TARGET_LEDGER.md](TARGET_LEDGER.md). The three detailed author handoffs are [arithmetic](agent1_arithmetic/CLOSEOUT.md), [selector](agent2_selector/CLOSEOUT.md), and [analysis](agent3_analysis/CLOSEOUT.md).

## Main results from the planned routes

### Analytic pullbacks with integral derivatives

An exact Schur-prefix construction proves that endpoint-fixing polynomial compositions with integral Hurwitz derivatives can achieve every radius r<2.665. The earlier 2.65 theorem received a narrow pass conditional on inherited cover constants and the Schwarzian; the refined 2.665 prefix has an exact author certificate and was not separately audited. The located upper obstruction 2.67 is also outside that narrow review. The bounded interval is a statement about this pullback class.

An explicit degree 81 polynomial has a complete exact zero-free certificate beyond radius 401/200=2.005. This supplies a concrete finite vector, while the 2.665 result is an existence theorem. Both preserve the actual circular endpoint. Analytic radius alone does not control the primitive denominator in a mixed irrationality form.

Sources: [existence and review scope](main/INFINITE_INTEGRAL_JET_PULLBACK_EXISTENCE.md), [explicit degree 81 construction](main/EXPLICIT_DEGREE81_HURWITZ_PULLBACK.md).

### Actual common divisors with a finite radius budget

Parameter Hensel lifting at prime163 produces ten different rational specializations, each retaining radius>2 and the corresponding actual common divisor 163^k, for k=1,...,10. The construction retains the full endpoint numerator. A two-prime construction at 163 and 347 likewise gives four distinct specializations with actual common divisor (163·347)^k.

These are genuine finite constructions. The polynomial changes with the requested depth, and its archimedean coefficient budget is part of the proof. A fixed rational polynomial supporting arbitrary depth, an adequate supply of primes, and a favorable global final denominator were not proved.

Source: [parameter lifting and radius budget](main/PRIME_PARAMETER_HENSEL_WITH_RADIUS_BUDGET.md); the two-prime continuation and finite receipts are indexed in the main ledger.

### Paired determinants and complete primitive outputs

The paired and short matching constructions produce exact linear forms in S and, for higher pole order, primitive polynomials in S. They retain the actual greatest common divisor of all output coefficients. Original analytic work proves nonzero signed determinants and complete errors in the specified infinite ranges. Original arithmetic work identifies factorial and dyadic content, basis indices and quotient matrices.

The short k-by-2k family reduces the required polynomial degrees to 2k−1. For k≥24 the complete determinant and its S coefficient are nonzero, and its actual center c approaches S from the stated side at exponential scale. The coefficient growth remains substantial. The later wider construction realizes every rational polynomial direction of degree≤m in its stated range. It preserves the full multiplier and final common divisor; freedom to choose a direction does not provide a cheap small form.

Sources: [short construction](main/SHORT_PAIRED_KERNEL_LINEAR_S.md), [signed error](agent3_analysis/SHORT_RECTANGULAR_COMPLETE_SIGNED_ERROR.md), [wide polynomial realization](main/WIDE_RANK_M_COMPLETE_POLYNOMIAL_REALIZATION.md).

### Fixed and slowly growing shifted dimensions are excluded

For every fixed dimension k, the shifted short family has an actual primitive denominator lower bound of factorial scale. Combined with its complete error, the reduced integer forms grow rather than tend to zero as the even shift M→∞.

The uniform extension covers dimensions satisfying

    k (log(k+1))² = o(log M).

It proves

    log q ≥ [1−o(1)] log((2M)!)/(k+1),
    log(q |S−c|) → +∞,

where q is the fully reduced denominator of the actual center. The proof uses a uniform evaluated nonzero leading coefficient, and retains the degree-dependent threshold in the published transcendence measure. This excludes that entire regime after the final gcd. Proportional shifts and faster dimension growth lie outside the theorem.

Sources: [fixed dimension](main/SHIFTED_SHORT_FIXED_DIMENSION_TRANSCENDENCE_OBSTRUCTION.md), [slowly growing dimensions](main/SHIFTED_SHORT_SLOW_GROWING_DIMENSION_OBSTRUCTION.md).

### Growing poles expose the complete content requirement

For the actual higher-pole short stack, uniformly for 1≤m≤k and k≥131072, the complete determinant obeys

    log|β(k,m)(S)| = 4k² log k + O(k²).

After the complete moment clearer and final coefficient gcd g, the primitive polynomial P obeys

    log|P(k,m)(S)| = 4k² log k − log g + O(k²).

Therefore a subsequence of primitive values tending to zero requires

    liminf log g/(k² log k) ≥ 4.

This is a necessary arithmetic budget, with the actual evaluated gcd still unresolved. The guaranteed factorial content does not establish this budget. Separately, the properly normalized very-large-pole window has a proved exclusion: its actual primitive evaluation exceeds the full coefficient height and is at least 1. The intermediate range remains open.

Sources: [uniform actual value and content](main/GROWING_POLE_ACTUAL_NORM_CONTENT_BUDGET.md), [proper large-pole normalization](main/PROPER_LARGE_POLE_EXACT_CLEARER_COMPRESSION.md), [complete perturbation bound](agent3_analysis/PROPER_LARGE_POLE_COMPLETE_PERTURBATION.md).

### Fixed Gram exclusions and an exact dyadic endpoint law

The specified b=3,m=1 Gram-center family has an actual reduced-denominator theorem using a 17-prime certificate. Together with its separately authored signed-error theorem, it excludes that fixed family; the denominator and analytic error were the subjects of two limited early reviews. The distinct b=5,m=1 family has a ten-prime denominator certificate and a proved primitive-error growth gap greater than 1/25, using the attributed fixed-b signed error. This does not establish a general b theorem. The b=4 denominator rate alone was not promoted to an exclusion without a complete error input.

On the infinite regular weighted subfamily n=4^j+1, j≥1, the completed endpoint/carry computation proves

    v₂(q_center)=n+2,

where q_center is the fully reduced denominator of the actual center. The normalization and arctangent premises hold in the same basis. This resolves the complete dyadic factor on that subfamily, while the total odd content remains open. Nine regenerated exact receipts accompany the theorem, and the superseded residue formulas are explicitly withdrawn in the author handoff.

Sources: [b=3 denominator](agent1_arithmetic/ODD_PRIME_ALL_DEPTH_GRAM_DENOMINATOR.md), [b=5 fixed-family exclusion](agent1_arithmetic/B5_WHOLE_FIXED_FAMILY_DENOMINATOR_EXCLUSION.md), [weighted actual dyadic endpoint](agent1_arithmetic/WEIGHTED_REGULAR_EXACT_DYADIC_ENDPOINT_THEOREM.md).

### Additional subagent results

The selector handoff records all-start nonzero blocks for the actual selector certificates, rational correction formulas preserving final denominators, and explicit right-block quotient/content interfaces. The arithmetic handoff records local carried endpoint laws, regular weighted dyadic families, and the arithmetic conditions left unresolved by saturation. The analysis handoff records complete signed errors for the earlier corrected families, uniform shifted leading nonzero coefficients, and growing-pole root localization.

These results remove several previously conditional steps. Their remaining global primitive-content conditions are explicit. Completing a bounded family or excluding its parameter window does not decide the arithmetic nature of S.

## Files and final state

All original notes, finite certificates, scripts and provenance remain in the session's main and three agent directories. Shared ledgers preserve corrections and superseded scopes. The final index points to the authoritative notes; the inventory records file sizes and SHA256 hashes; a session archive provides a download copy.

Quota monitoring receipts are retained in [usage_log.jsonl]([private local path removed]) and [latest_usage.json]([private local path removed]). The local stop flag is set because of the actual 9% read. The existing monitor is paused after closeout completion to prevent additional automatic research stages.

The requested ten-minute monitoring cadence was not perfectly met: 17 recorded intervals exceeded ten minutes; the longest was 13.37 minutes. The original timestamped receipts are preserved, and the closeout timing receipt reports the intervals without changing them. The stop decision used an actual available-window read, not a missing value.

The delivered result is a documented research advance and a set of precise construction boundaries. The rationality question is still open.

