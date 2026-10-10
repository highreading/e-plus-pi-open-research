> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Closing verification register

Research stopping condition: observed5% remaining core quota and zero
reset credits at2026-09-13 04:39:23 UTC, confirmed by an independent
fresh supported-tool read. All tasks listed below were already active
at that point. Their finishing audits are now complete.

**Main result: unresolved. There is no proof that e+pi is rational or
irrational.** PASS denotes an independent mathematical review within
the written scope, not external peer review or proof-assistant checking.

| Result | Final status | Source and review |
|---|---|---|
| All-parity divergence of actual reduced raw forms | All dependencies PASS; assembly checked by root | [raw_all_parity_raw_exclusion.md](../../../work/session_20260913/raw_all_parity_raw_exclusion.md); [raw_odd_reference_contour_independent_review.md](../../../work/session_20260913/raw_odd_reference_contour_independent_review.md) |
| Even relative-error asymptotic | PASS | [raw_even_endpoint_residue_asymptotic.md](../../../work/session_20260913/raw_even_endpoint_residue_asymptotic.md); [raw_even_endpoint_residue_independent_review.md](../../../work/session_20260913/raw_even_endpoint_residue_independent_review.md) |
| Odd Hardy framework | PASS by computations | [raw_odd_hardy_reference_and_reversal_framework.md](../../../work/session_20260913/raw_odd_hardy_reference_and_reversal_framework.md); [raw_odd_hardy_framework_independent_review.md](../../../work/session_20260913/raw_odd_hardy_framework_independent_review.md) |
| Odd actual saddle multipliers | PASS by sources, with certified witness-error propagation | [raw_odd_saddle_multiplier_limits.md](../../../work/session_20260913/raw_odd_saddle_multiplier_limits.md); [raw_odd_saddle_multipliers_independent_review.md](../../../work/session_20260913/raw_odd_saddle_multipliers_independent_review.md) |
| Odd reference and complete contour assembly | PASS by sources; acyclic dependency map retained | [raw_odd_reference_and_contour_asymptotic.md](../../../work/session_20260913/raw_odd_reference_and_contour_asymptotic.md); [raw_odd_reference_contour_independent_review.md](../../../work/session_20260913/raw_odd_reference_contour_independent_review.md) |
| Positive and negative residue transfer | PASS, including corrected content transcription | [raw_positive_residue_transfer_independent_review.md](../../../work/session_20260913/raw_positive_residue_transfer_independent_review.md); [raw_negative_residue_transfer_independent_review.md](../../../work/session_20260913/raw_negative_residue_transfer_independent_review.md) |
| Complete seed certificates at23,43,71,83,101,109,127,151 | PASS through distinct exact reconstructions | [raw_uniform_23_43_independent_review.md](../../../work/session_20260913/raw_uniform_23_43_independent_review.md); [uniform_71_83_independent_review.md](../../../work/session_20260913/uniform_71_83_independent_review.md); [raw_uniform_101_109_independent_review.md](../../../work/session_20260913/raw_uniform_101_109_independent_review.md); [raw_uniform_127_151_root_review.md](../../../work/session_20260913/raw_uniform_127_151_root_review.md) |
| Exact strict rate separation | PASS, two different rational logarithm methods | [raw_closed_uniform_rate_independent_review.md](../../../work/session_20260913/raw_closed_uniform_rate_independent_review.md) |
| Positive-residue full prime-power lift | PASS by sources | [raw_positive_residue_full_prime_power_lift.md](../../../work/session_20260913/raw_positive_residue_full_prime_power_lift.md); [raw_positive_prime_power_lift_independent_review.md](../../../work/session_20260913/raw_positive_prime_power_lift_independent_review.md) |
| Degree-one adjacent scalar endpoint formula | FULL PASS by results | [hp_b1_adjacent_scalar_valuation_gate.md](../../../work/session_20260913/hp_b1_adjacent_scalar_valuation_gate.md); [hp_b1_adjacent_scalar_independent_review.md](../../../work/session_20260913/hp_b1_adjacent_scalar_independent_review.md) |
| Degree-two contiguous endpoint formula and large-prime gcd bound | FULL PASS by sources; nonzero-endpoint domain clarified | [hp_b2_contiguous_endpoint_arithmetic.md](reference_notes/hp_b2_contiguous_endpoint_arithmetic.md); [hp_b2_contiguous_endpoint_independent_review.md](../../../work/session_20260913/hp_b2_contiguous_endpoint_independent_review.md) |
| Exact first-factorial-order error of the existing degree-one companion | FULL PASS by computations | [hp_b1_companion_exact_error_rate.md](../../../work/session_20260913/hp_b1_companion_exact_error_rate.md); [hp_b1_companion_error_independent_review.md](../../../work/session_20260913/hp_b1_companion_error_independent_review.md) |
| Auxiliary analytic disks and simple-index-root reduction | PASS by root within explicit nonzero-slope hypothesis | [hp_auxiliary_simple_root_analytic_reduction.md](../../../work/session_20260913/hp_auxiliary_simple_root_analytic_reduction.md); [hp_auxiliary_analytic_reduction_root_review.md](../../../work/session_20260913/hp_auxiliary_analytic_reduction_root_review.md) |

## Last exact reductions and their unresolved parts

The b=1 formula now needs four scalar factorial sums. In the source's
notation, with K_(n+1)=J_(n+1)/(n+1),

    X/Y=[2K_(n+1)S_n-(n+1)H_nS_(n+1)]/Delta_n,
    Delta_n=(n+1)P_(n+1)H_n-2P_nK_(n+1).

After the displayed integer clearing M=(2n+1)!, its exact q valuation is

    v_p(q)=max(0,v_p(M)+v_p(Delta_n)-v_p(N_n)).

N_n here is the specifically cleared scalar numerator from the b=1 note;
it is NOT the raw-family N_n. The formula preserves every cancellation.
For odd p dividing n+1 with p not dividing P_n, the normalized kernel
endpoint delta has valuation -2v_p(n!). A proved Lucas identity makes
the unit condition automatic at p=3 when n=2 modulo3. This controls
the denominator side of the ratio; the numerator can still cancel it.

For b=2 the corresponding exact expression is

    q_n=|Lambda_n D_n|/gcd(|Lambda_n D_n|,|N_n|).

Every object is explicitly defined in the b=2 note from adjacent
integer Legendre values, second-kind values, finite partial-exponential
sums and integer transforms. The polynomial identities hold in their
stated scope; division requires the endpoint to be nonzero, which is
proved eventually.

For the primitive full integral b=2 triple, the large-prime endpoint
gcd obeys, at every p>2n+4, a full valuation upper bound by the gcd
of the maximal minors of

    [ H_n       J_n       ]
    [ J_(n+1)   K_(n+1)   ]
    [ K_(n+2)   M_(n+2)   ].

The K and M in this b=2 display are the derivative combinations defined
in its source; K is NOT the b=1 quotient J/k. Keep the two notes'
notation local. A symbolic identity check used independent variables,
not additional degree samples. No global upper bound for this minors'
gcd or small-prime q-growth theorem is proved.

The companion-error audit accepts

    e-r_n^* ~ exp(-sqrt(2)) W(0)/(n^3 n!),
    log|e-r_n^*|=-n log n+n+o(n).

Its hidden-second-factorial-order escape is closed, while reduced
height remains open.

## Exact continuation priorities

1. Read the two new endpoint reductions before doing any degree or prime
   computation. The next desired lemma must estimate the actual valuation
   difference or actual reduced q, including simultaneous numerator zeros.
2. For b=2, a growing-prime bound for the actual maximal-minor gcd is
   a concrete alternative. Its range p>2n+4 cannot silently include small
   primes with factorial/moment losses.
3. The original matched route still needs the same synchronized positive
   gain above T. None of these HP results changes that separate ledger.
4. Retain the auxiliary analytic formula only with its index-slope
   hypothesis; no common-root classification or uniform compatibility
   bound was proved.
5. Do not scan the closed raw family for shrinking subsequences, search
   for a sub-3/2 coefficient clearer for C_0-C_1, or seek second factorial
   decay for the same rational companion. Those exact targets are excluded.

## Evidence locations

The authoritative source notes and all exact certificates, witness
vectors, checks and logs remain in the Desktop project's
work/session_20260913 directory. The output package contains a snapshot
of its Markdown notes under reference_notes. Large data files, installed
math libraries and downloaded third-party papers were not duplicated
into that presentation snapshot. The snapshot manifest records hashes;
hash equality establishes provenance, not mathematical validity.

Earlier session indexes retain historical checkpoints. Their descriptions
of an open raw saddle, pending prime reviews, or a10% stopping threshold
are superseded by this register and the closing notice at their top.
