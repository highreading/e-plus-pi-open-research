> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# audit_computations closeout — 2026-09-27

The user requested an early end. Original research is stopped; this
register organizes the work already completed. No quota or reset tool
was queried by this agent. No main irrationality proof is claimed.

All files below are in:
`work/session_20260927/`.

## Independently passed results

1. **Exact actual ternary denominator depth.**
   `hp_b1_ternary_actual_denominator.md` proves
   v_3(q_n)=2v_3(n!) for every n>=5 with n=2 modulo3.
   Source review: `hp_b1_ternary_actual_denominator_independent_review.md`,
   FULL PASS, including the conditional general odd-prime gate.
   The proof evaluates the formerly unresolved actual numerator;
   it does not substitute a coefficient clearer for reduced q.

2. **Exact all-even dyadic numerator and reduced-q lower bound.**
   `hp_b1_dyadic_numerator_and_six_class_exclusion.md` proves
   v_2(mathscr U_n)=n+2-2v_2(n!) and
   v_2(q_n)>=2v_2(n!)-n/2 for even n>=2 when Delta_n!=0.
   Root review: `hp_b1_dyadic_independent_root_review.md`, FULL PASS.
   With the ternary result this already excludes shrinking on n=2 mod6.

3. **Second ternary residue.**
   `hp_b1_ternary_zero_class_addendum.md` proves
   v_3(q_n)>=2v_3(n!) on n=0 mod3, n>=3, whenever Delta_n!=0.
   The arithmetic was independently checked and recorded by sources
   in Section5 of `hp_b1_residue_one_actual_numerator.md`.
   There is no separate standalone review artifact for this short addendum.

## Closing dedicated review and remaining unreviewed synthesis

4. `hp_b1_prime_seed_transfer_and_closed_atlas.md` proves the all-residue
   modulo-p transfer for the normalized numerator and supplies the
   complete predeclared seed list p=5,7,11,13,17,19. Only5 and13
   have sole seed zero1. Every scalar coordinate was independently
   crosschecked within the exact checker by a different formula.
   Dedicated external review: FULL PASS in
   `hp_b1_uniform_5_13_independent_review.md` (audit_results), including
   all 72 rows independently rebuilt from a third exact formula.

5. `hp_b1_uniform_five_thirteen_and_even_exclusion.md` assembles
   uniform v_p(q_n)>=2v_p(n!) for p=5,13 from the transfer and
   sources' root-disk theorem, then excludes every sufficiently large
   even b=1 index using the passed dyadic result. The resulting lower
   rate is 1.5log2+0.5log5+(log13)/6, strictly above
   2log(1+sqrt2). Closing dedicated review is FULL PASS in
   `hp_b1_uniform_5_13_independent_review.md`.

6. `hp_b1_closed_prime_odd_index_restriction.md` gives the exact remaining
   odd CRT set for this closed prime list: n mod7 in {2,3}, and at least
   two of n mod11=2, n mod17 in {3,11}, n mod19=14.
   There are146 such classes modulo24871 among odd integers, hence
   density146/49742 among all indices once the even exclusion is used.
   This synthesis/CRT calculation was NOT independently reviewed under
   the user's stop instruction; its arithmetic inputs separately passed.
   This is an unexcluded set, not a set of successful approximants or
   an upper bound for actual q.

The separate root-disk dependency is sources'
`hp_b1_residue_one_actual_numerator.md`, Sections1–2. It proves
v_p(mathscr C_n)=v_p(n-1) for p>=5 via integral analytic index germs.
Sections1–2 now have FULL PASS in the same dedicated review. Its deeper ternary
analytic-root result is sources' work, outside this agent's audit scope.

## Reproducible checks already run successfully

* `check_hp_b1_ternary_actual_denominator.py` and
  `hp_b1_ternary_actual_denominator_checks.json`: only frozen n=2,8,
  original endpoint identity and exact dyadic/ternary normalizations.
* `check_hp_b1_predeclared_prime_seeds.py` and
  `hp_b1_predeclared_prime_seed_certificate.json`: every residue of the
  six predeclared primes, two distinct scalar constructions; no HP solve.
* `check_hp_b1_closed_prime_rate_and_crt.py` and
  `hp_b1_closed_prime_rate_and_crt_certificate.json`: exact Pell-integer
  comparisons for all rate inequalities and the complete CRT count.

No prime beyond the predeclared list was tested. No new canonical HP
degree was solved. The open issue is still whether any remaining odd
subsequence or another construction yields shrinking nonzero primitive
integer forms. The present work supplies route exclusions, not a proof
about the irrationality of e+pi.
