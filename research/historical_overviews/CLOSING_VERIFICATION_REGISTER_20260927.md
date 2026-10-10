> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Closing verification register — 2026-09-27

Research stopped at the user's explicit request, after finishing active calculations and reviews. No proof of rationality or irrationality of e+pi was obtained. This register supersedes intermediate pending labels only within the exact scopes specified below.

All filenames below are relative to `work/session_20260927/`. A FULL PASS is an independent mathematical audit within the project, not a claim of formal proof-assistant verification or global literature novelty.

| Item | Final status | Proof / independent review |
|---|---|---|
| Every fixed b: eventual normality and signed full endpoint error | FULL PASS | `fixed_exponential_degree_error_theorem.md` / `fixed_exponential_degree_error_independent_review.md` |
| b1 actual quotient and ternary n=2 mod3 denominator | FULL PASS | `hp_b1_ternary_actual_denominator.md` / `hp_b1_ternary_actual_denominator_independent_review.md` |
| b1 all-even dyadic numerator and q bound | FULL PASS | `hp_b1_dyadic_numerator_and_six_class_exclusion.md` / `hp_b1_dyadic_independent_root_review.md` |
| b1 general prime transfer and all 72 closed-list seeds | FULL PASS | `hp_b1_prime_seed_transfer_and_closed_atlas.md` / `hp_b1_uniform_5_13_independent_review.md` |
| b1 all-depth residue-one lift at every p>=5 | FULL PASS | `hp_b1_residue_one_actual_numerator.md`, §§1–2 / `hp_b1_uniform_5_13_independent_review.md` |
| b1 uniform actual q bounds at 5,13 and all-even exclusion | FULL PASS | `hp_b1_uniform_five_thirteen_and_even_exclusion.md` / `hp_b1_uniform_5_13_independent_review.md` |
| b1 ternary root xi and conditional actual-q formulas | FULL PASS | `hp_b1_residue_one_actual_numerator.md`, §§3–5 / `hp_b1_ternary_root_independent_root_review.md` |
| b1 ternary zero class | FULL PASS for its arithmetic statement | `hp_b1_ternary_zero_class_addendum.md` / residue-one note §5 and `hp_b1_ternary_root_independent_root_review.md` |
| b1 odd dyadic entire germs, root nu, exact C valuations | FULL PASS | `hp_b1_odd_dyadic_actual_numerator.md`, §§1–2 / `hp_b1_odd_dyadic_germs_independent_review.md` |
| b1 odd dyadic transfer from C to q and combined exclusion | Written corollary; separate independent transfer review not completed | `hp_b1_odd_dyadic_actual_numerator.md`, §3. Do not extend the preceding PASS to this section. |
| b1 six-prime odd CRT restriction and rate synthesis | Exact certificate passed; independent synthesis review not completed | `hp_b1_closed_prime_odd_index_restriction.md`; its seed/lift inputs are independently accepted. |
| b2 exact cubic/minor depth gate | FULL PASS | `hp_b2_cubic_maximal_minor_gate.md` / `hp_b2_cubic_maximal_minor_independent_review.md` |
| b2 adjacent large-prime coprimality and all-index Omega nonvanishing | FULL PASS | `hp_b2_adjacent_content_coprimality.md` / `two_local_lemmas_independent_root_review.md`, §1 |
| Odd-prime analytic interpolation and finite compactness criterion | FULL PASS for the mathematical lemma | `literature_update_and_b2_analytic_certificate.md`, §§3–5 / `two_local_lemmas_independent_root_review.md`, §2 |
| Literature applicability update | Scoped primary-source reading completed | `literature_update_and_b2_analytic_certificate.md`, §2; not an exhaustive bibliography or an independently rechecked proof of each external theorem. |

## Checks and their proper meaning

The saved exact checks include the independent 72-row seed reconstruction, formal b2 polynomial identities, full-coefficient ternary and dyadic germs with proved tails, the two frozen controls inherited from the earlier session, and exact algebraic rate/CRT comparisons. Reproducible files have names `check_*.py`; corresponding outputs are JSON. No floating-point evidence, sampled integer relations, or finite degree scans were used as substitutes for infinite proofs.

The dyadic germ checker uses four complete residue disks at one predeclared precision. Its proof of the tail and coefficientwise integrality is essential. The ternary germ checker likewise uses all coefficients plus an explicit tail estimate. Neither is an empirical extrapolation from a few HP indices.

## Barriers that remain open

- The main rationality/irrationality question.
- Whole-family exclusion or success of b1. The all-even exclusion is accepted; p-adic root proximity and final outstanding synthesis reviews remain distinct issues.
- Diophantine upper bounds for v2(n-nu) and v3(n-xi); no arithmetic nature of either root is established.
- Actual b2 reduced denominator growth, isolated large-prime depth, and small-prime factorial/moment losses.
- Uniformity for growing b, which is outside the fixed-b theorem.
- The original matched-integral synchronized gain threshold; its numerical ledger is unchanged.

## Administrative closeout

User instruction overrides the earlier quota termination rule. Monitoring gate inactive; worker terminated; app heartbeat `e-plus-pi-research-quota-every-five-minutes` PAUSED. No quota reset used in this resumed session. All three agents reported their active tasks complete and stopped. Last logged quota was 84%, a historical observation, not a closure-time balance.

Old session files are preserved. `session_file_manifest.json` inventories this session's final files by SHA-256, excluding itself. `SESSION_20260927.md` and the Chinese main report are the recommended entry points.
