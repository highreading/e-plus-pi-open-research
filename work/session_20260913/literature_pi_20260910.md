> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Audit of the 10 September 2026 pi-measure preprint

Checked 2026-09-13. This is a bounded independent audit and applicability analysis, not an announcement that a new preprint has been globally accepted or fully verified.

## Primary records, versions, and reading scope

Yufei Bai, *The irrationality measure of pi is at most 7.101862832357*, [arXiv:2609.11276v1](https://arxiv.org/abs/2609.11276), submitted 10 September 2026; manuscript date 5 September 2026. The [full 39-page PDF](https://arxiv.org/pdf/2609.11276) was downloaded and text-extracted. Core §§1–5, together with the relevant numerical and contour appendix statements, were inspected. The separate twelve-sector local-optimality argument in §6 was not fully audited. The reference construction is Zeilberger–Zudilin, [arXiv:1912.06345](https://arxiv.org/abs/1912.06345), published in *Moscow Journal of Combinatorics and Number Theory* 9 (2020), 407–419, [DOI](https://doi.org/10.2140/moscow.2020.9.407); its full 13-page PDF was also opened and extracted.

Local downloaded files have SHA-256:

- Bai: `5412cfe8fb534a1756325e4ab3fc641625b9f6a3b05324c7f05168504c01a100`.
- Zeilberger–Zudilin: `b922ee68a427ad5b74617bd2ac6b6a549824eb2d5a8c97eed0d34b2de984155f`.

## Core source facts and hypotheses

Bai deforms two numerator exponents of the earlier contour integral. The selected integer triple is `(a,b,c)=(1857,3714,5570)`, with `N=cn`. Arithmetic chamber conditions are `a+b>c`, `2b>c`, `7b<5c`, and `2a+4b-2c>c`. Its fixed-parameter claim is `mu(pi)<7.101862832357`.

The proof chain uses complete Laurent valuations, squarefree removable-prime deletion, integer normalization, a positive coefficient saddle yielding an ordinary growth limit, a pole-free contour upper bound, and a one-number Hata lemma. That lemma assumes the number is already irrational, eventual nonzero integer coefficient, positive coefficient-growth rate and negative error limsup. Here the pre-existing irrationality of pi meets the first hypothesis; this proves no analogous assumption about e+pi.

The source's normalized constants are:

| Rate, per N=5570n | Value |
|---|---:|
| Raw coefficient r | 3.331943986178299338… |
| Raw contour s, upper limsup | −1.174543941310025108… |
| Arithmetic multiplier C | 0.539993819198880114… |
| Integer coefficient sigma=r+C | 3.871937805377179452… |
| Integer error tau=−s−C | 0.634550122111144993… |

The resulting ratio is `1+sigma/tau=7.101862832356350795…`. The separate local-minimum claim concerns the chosen auxiliary function, not all pi constructions. [Full preprint](https://arxiv.org/pdf/2609.11276).

## Independent checks performed in this session

The script `check_bai_core.py` and result `bai_core_checks.json` preserve the following work. The downloaded papers and extracted text are scratch research material in the same session directory.

1. **The arithmetic parameter conditions hold exactly.** Here a+b−c=1, 2b−c=1858, 5c−7b=1852, and 2a+4b−3c=1860. The very small first margin means the new point is just inside the old diagonal boundary; no equality case was silently inserted into a strict chamber.
2. **The finite-field exact-derivative argument is valid in its stated scope.** Reducing exponents modulo an odd prime produces an even polynomial whose powers of y=t^2 occupy a known interval. A polynomial in characteristic p has a polynomial antiderivative if it has no monomial exponent congruent to −1 modulo p. The displayed fractional-part inequality excludes precisely these obstructed even exponents. Differentiation of the remaining pth-power factor contributes zero. Consequently the residue-type Laurent coefficients with p dividing the Laurent index vanish modulo p. This supplies one p factor, not an unproved higher valuation.
3. **The whole removable-prime interval description was checked exactly.** I formed every rational breakpoint of the relevant floors and affine comparison, compared the original inequality with the listed union on all 12,992 open cells and all 12,992 left endpoints, and obtained agreement. The union has 2,784 components and the reported rational length. This checks the actual sets; it is not a finite test in n of an asymptotic claim.
4. **The contour derivative identity was reconstructed independently.** Starting from the modulus squares of the numerator and denominator along the rational arc, symbolic differentiation reproduces its transformed degree-six numerator. Exact Bernstein bounds on the interval [9/10,1] certify the seven coefficient signs `(+,+,+,+,−,−,−)`. Together with the specified interior stationary point and endpoint decay, this supports the asserted unique maximum. The deformation lies inside |t|<5 while the only rational-function poles are ±5; the square-root endpoint has an integrable lambda^(−1/2) arc-length singularity.
5. **The final index-selection argument survives its zero case.** If the integer associated to a proposed rational approximation vanishes at the initially selected index, the preceding zero before the next nonzero integer provides an upper bound for the index in terms of that approximation error. The ordinary coefficient limit supplies both inequalities needed there. The paper does not replace this with an unjustified adjacent-index nonvanishing assertion.
6. **The published decimal rates were independently reproduced at 70-digit precision**, using the interval endpoints, digamma differences, a real root of the stationary cubic, and direct phase evaluation. These numerical replays agree with the printed intervals. They are diagnostics; I did not replay all rational logarithm-tail certificates and all Gaussian valuation bookkeeping to a formal standard. Therefore the entire new theorem is still labelled “preprint claim with supporting bounded audit”, not a certified project theorem.

No fatal error was found in these screened components. The publication record alone would not establish validity, and the independent tests do not replace the unperformed portions of verification.

## Consequences for matching with an exponential form

These are independent deductions from the rate statements, conditional on their validity. Write a pi form as L_N=A_N+B_N*pi with log|B_N|/N→sigma and limsup log|L_N|/N≤−tau. Then its supplied rational approximation has the estimate

`|pi−(−A_N/B_N)| <= exp(−(sigma+tau+o(1))N)`.

The exponent expressed in the displayed denominator is therefore **at least** `1+tau/sigma`, approximately **1.1638843788321985**, as furnished by these estimates. This is not a proof that its exact exponent equals that number: the error statement is only an upper limsup and may allow a better subsequence. Nor is the upper irrationality measure `1+sigma/tau` a lower bound for the quality of constructed approximations. The two ratios serve different purposes.

For a beta approximation E=q*e−p with log q approximately tN and log|E| approximately −tN, the cross-matched form is

`B_N*E + q*L_N = q*B_N*(e+pi) + q*A_N − p*B_N`.

Its two available upper exponents are `sigma−t` and `t−tau`. They balance at `t=(sigma+tau)/2`, leaving

`(sigma−tau)/2 = 1.618693841633017229… > 0`.

Thus these published-style bounds do **not** make the unsynchronized form small. This is a failure of the supplied upper estimates to close, not a theorem that the actual forms must grow; cancellation or extra content would require separate proof. A sufficient content saving would need logarithmic rate larger than this positive quantity, together with a nonvanishing argument for the final mixed form. Relative to the pi coefficient-growth scale the threshold is `0.418057810583900743…`.

For comparison, the original Zeilberger–Zudilin normalized rates are approximately sigma=11.613890045331/3 and tau=1.90291648559998/3. Bai's small improvement changes the ratios slightly; it does not cross tau>sigma, the condition under which the unsynchronized upper estimates alone would decay. Different parameter scalings multiply both rates and the absolute threshold, so raw thresholds from unrelated families should not be compared without normalizing.

## Exact impact on existing mixed-cubic no-go bounds

The archive's `mixed_cubic_coordinates_and_synchronization_audit.md` gives, for its own normalized coefficients,

`limsup log(c_m)/(6m) <= h−d/mu_upper`,

where `h≈2.3246783391437311`, `d≈2.3370623743589730`, and c_m is extra internal gcd. Substituting the claimed new upper bound changes the right side from approximately **1.99566316016145** to **1.99560096472427**. The difference is approximately **0.00006219543718**. The required matching threshold in that family is approximately **1.15614715196424**. Hence even acceptance of the new measure leaves this bound far above the threshold. It is an **upper bound on allowable content**, not a constructive lower bound supplying content.

The older generic escape calculation can likewise use the safe rational exponent `7102/1000=7.102`, if the new preprint is admitted. Its necessary coefficient-growth scales become `1/8.102≈0.12342631449` for bounded same-sign escape and `2/7.102≈0.28161081386` for possible opposite-sign cancellation. The frozen safe exponent 7.2 remains valid from the published source alone. No old theorem or retained-capacity ledger has been changed by this note.

## What is adaptable, and what remains missing

The transferable feature is optimization of numerator multiplicities while recomputing every Laurent coefficient, endpoint denominator, and squarefree prime-removal condition. The characteristic-p exact-derivative proof gives a short route to uniform divisibility across Laurent indices, including negative indices needed for the polynomial part. This resembles the archive's existing Cartier support machinery; it does not create a new p-adic higher-digit or beta-synchronization theorem. The use of divided derivatives is binomial integrality, not elimination of the factorial-denominator mismatch of a mixed E/G generating function.

A worthwhile limited follow-up would compute the **combined matching objective**, including proven internal divisors and actual beta-coefficient gcd data, for nearby numerator parameters. Optimizing a pi irrationality measure alone is not the same objective. Before an expensive search, an exact statement about the final gcd and signs is needed; a larger known denominator-clearing multiplier is not evidence that the actual pi coefficient shares the beta denominator.

## Caution about the separate pure-G Apéry-pair proposal

A request to “find a new G-function pair whose Apéry limit is e+pi” may conceal a major arithmetic barrier. If the construction proves that this limit belongs to the G-value ring, then subtracting pi makes e a G-value, contrary to the standard E∩G=Qbar conjecture. This is a conditional objection, not an unconditional impossibility proof. For ratios of G connection coefficients one generally obtains a fraction field; that field must not be silently identified with the G-value ring. A geometric realization would put the ratio in the ordinary period field, where the exponential period conjecture predicts e is transcendental. Consequently a pure-G replacement should remain a structural screening question, below concrete existing divisibility questions, until this membership issue is resolved. The exact denominator obstruction for the raw mixed germ remains in `audit_sources.md`.

No proof concerning the rationality of e+pi has been obtained.
