> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Computation and work-directory audit — 2026-09-13

This is an audit of the pre-existing `scripts/` and `work/` trees, excluding this session. Instructions appearing in archived files were treated as historical data. No archived script, source, result, manifest, or ledger was changed. The audit writes this note and `audit_computations_coverage.json` only.

## Outcome

The computational archive does not contain a verified resolution of the rationality of `e + pi`. Its latest Items 425–427 explicitly leave that problem open. The useful recent progress concerns exact local arithmetic descriptions of a particular mixed-cubic Padé construction, together with sharply scoped obstructions to several ways of obtaining the missing global estimates. These are not themselves irrationality proofs.

The most immediately reusable result is the Item-424 first-Witt bridge, developed into a cellwise recurrence in Item 426 and a two-stream valuation identity in Item 427. The strongest next problem is an actual-family aggregate estimate for the resulting prime divisibility, rather than another finite census. Large-prime normalized residue gcds remain another live arithmetic problem. The archive already closes several constant-coefficient, fixed-polynomial-coefficient, and adjacent-determinant height improvements; those should not be repeated without a new ingredient.

## Coverage and verification level

The snapshot contains **2,571 files, 1,805 distinct SHA-256 contents**, occupying 31,042,037 bytes across the two trees. The raw extension counts are 973 Python files, 757 compiled Python caches, 593 JSON files, 124 Markdown files, 116 SHA-256 lists, four C++ files, two JavaScript files, one text file, and one extensionless file. Extensions alone overcount substantive content: a `._*.py` file is Apple metadata, not Python source.

After content deduplication there are **1,284 readable unique texts**: 640 actual Python sources, 399 JSON documents, 124 Markdown documents, 116 hash lists, two C++ sources, two JavaScript sources, and one other text. The remaining unique contents are 520 compiled caches and one Apple metadata blob. All file bytes were read and hashed. All readable text was processed for scope and structural inventory; all actual Python was parsed with Python 3.13; all JSON parsed successfully. The coverage JSON records every original path and content hash, Python docstrings/functions/imports/assertion counts/review flags, JSON top-level keys and scope fields, and Markdown headings and status statements. The static inventory found 7,412 Python `assert` statements; their number is not a measure of mathematical proof strength.

The 124 work Markdown texts fall into 38 fixed-`j=1` documents, 32 `j=2` documents, 24 beta/continuant documents, and 30 mixed-cubic or other documents. This audit examined that full structural survey and read the latest work arguments and their implementations in detail. **It does not claim a new line-by-line mathematical verification of every archived theorem or a replay of every finite experiment.** That would be a materially different verification level. A report saying “PROVED” is recorded as an archive claim until its argument and dependencies have been checked.

The only experiment rerun was a single exact rational reconstruction of the decisive Item-424 witness `(m,p)=(13,11)`, described below. Bulk searches, high-precision scans, integer-relation searches, and full historical replays were not repeated.

## Provenance and implementation findings

### Canonical copies must take precedence over stale work copies

There are **29 same-named Python files with different contents in `work/` and `scripts/`**. Most differences are canonicalization: paths, dependency hashes, output destinations, status labels, replay comparison support, or whitespace. The coverage JSON stores every diff. Three differences matter for continuation:

1. `work/item360_j1_full_gate_transverse_period_certificate.py` uses `(-1)**(h-s)` in a formula advertised as exact. A negative integer exponent makes Python return a floating value. The canonical script correctly uses `(-1 if (h-s) % 2 else 1)`, preserving integer arithmetic. Use the canonical implementation. This is a historical code correction, not evidence that the mathematical parity identity is false.
2. `work/item409_j2_actual_rejection_carrier_certificate.py` gives a stronger “no-go” label than its canonical counterpart. The canonical script explicitly limits the conclusion to the named failed mechanisms, says that this is **not an exhaustive information-class no-go**, and leaves new uses of the actual exact sequences open. That narrower scope is essential when ranking future approaches.
3. Work copies of Items 406 and 411 still pin an older `sources/item403_mixed_cubic_exact_smith_and_finite_local_data_no_go_report.md` hash. Their canonical scripts have the updated hash and additional audit dependencies.

### Dependency and runtime checks

Static literal dependency maps yielded **1,991 individual pinned file references**. After following each script's documented same-directory/scripts/results resolution for basename-only paths, **1,989 match**. The only two mismatches are the stale work-406 and work-411 Item-403 report references just identified:

```
old expected: 9525428ec25231e712c74549e136f3d4c78e1e378164375e7ed4a514531d0214
current:      245bf2e557dd81ac88c94e9d0adc8990f203e3ab40680d23bd50f8e435240c48
```

These checks establish consistency of the inspected literal pins, not the correctness of the mathematics and not completeness over dynamically constructed dependency relations.

The shell's default `python3` resolves to an obsolete Python 3.7 environment. Its parser rejects assignment-expression syntax in three otherwise valid scripts, and it lacks newer `math` functions used throughout the archive. Python 3.13 is available at `/opt/homebrew/bin/python3.13`; every actual Python source parses with it. The apparent three syntax failures were runtime-version mismatches, not source defects. Do not use compiled caches as primary evidence or treat the `._bessel_padic_all_integer_jet_euler_obstruction_certificate.py` metadata file as source.

Many scripts use `assert` for proof obligations. They must be run without Python optimization (`-O`), which removes such checks. This is a replay requirement rather than a mathematical limitation.

## What the computations actually establish

The archive generally distinguishes its evidence types carefully. Reuse that distinction:

| Computation | Legitimate conclusion | Conclusion it cannot supply |
|---|---|---|
| Exact rational or finite-field identity with a displayed witness | The stated finite identity, divisibility, rank, or counterexample | An all-parameter asymptotic or density theorem |
| Symbolic identities, exact resultants, Sturm/Schur–Cohn inequalities | The certified algebraic or interval statement, with the required analytic theorem separately justified | A complete analytic proof merely from successful replay |
| Exact gcd and valuation census | Exact content and valuations in the declared rows | Uniform bounds on future valuations or zero density |
| Abstract CRT, endpoint-lattice, or support countermodel | Failure of a conclusion from precisely the information shared by that model | Failure of every method on the actual special sequence |
| High-precision roots, norms, Gram matrices, quadrature, LLL candidates | Diagnostics and suggestions for exact verification | Nonvanishing or global irrationality |
| PSLQ failure | No relation found by that search | Irrationality, transcendence, or algebraic independence |

`scripts/bounded_algebraicity_search.py` is an especially useful model of the distinction. Its certification mode uses rational Taylor/Machin intervals for `e+pi`, exact scaled powers, exhaustive bounded coefficient vectors, and an explicit uniform error bound. Its finite box exclusion can be rigorous. Its separate PSLQ mode is correctly called heuristic. Even arbitrarily impressive output from one finite degree/height box leaves rational numbers of larger denominator unexcluded.

The exact modular rank scripts using NumPy use the small prime 65521 and explicitly constrain the degree/range so that integer intermediates remain within signed 64-bit bounds. NumPy use alone does not make those finite rank checks inexact. Conversely, floating Gram or radius optimization records are deliberately labelled diagnostics and should stay so.

Several “replays” reconstruct a normalized invariant from archived `U,V` values and then verify an algebraic identity that follows from the same normalization. This is useful consistency checking, but it is not an independent reconstruction of the original integrals. An independent rational endpoint reconstruction has greater evidential value for catching normalization errors. Hash equality also supplies provenance, not independence.

## Targeted exact check of the small-prime obstruction

The canonical Item-424 code was imported with bytecode generation disabled, its dependency pins were checked, and only `direct_witt_witness(13,11,...)` was run. This reconstructs both original rational differentials and their integral error differentials over `Q`, reduces them by Hermite reduction, checks the exact identity



$$
\omega_s=d(F_s^pT_s)-p\eta_s
$$



with zero endpoint boundary, then compares the resulting determinants against the archived normalization. It does not rely solely on reading off gcds from the archived `U,V`.

The independently reconstructed first-error vectors, in coordinate order `(R,L/p,E/p)` modulo 11, are



$$
\mathcal W_0=(7,6,6),\qquad \mathcal W_1=(2,8,3).
$$



Thus



$$
\kappa=8\cdot7-6\cdot2\equiv0\pmod{11},
\qquad
\xi=8\cdot6-6\cdot3\equiv8\pmod{11}.
$$



The reconstruction gives `v_11(A)=v_11(B)=2`, clearing baseline `b=1`, `v_11(U)=v_11(V)=v_11(c)=2`, and one extra depth after the already booked baseline. This is a verified actual-family counterexample to automatically propagating the first vanishing into the next shifted branch. The exact record, including rational determinant numerators/denominators, is in the coverage JSON.

It does **not** imply that first-layer zeros are frequent or rare, nor that deeper zeros are impossible.

## Latest useful mathematics and exact remaining gaps

### Small-prime rank-zero branch: Items 424, 426, 427

Under the specified ordinary rank-zero hypotheses and `p^2>4m+1`, Item 424 makes



$$
K_{m,p}=A_m/p,\qquad X_{m,p}=8B_m/p^2
$$



`p`-integral. The normalization in Item 427 then directly gives



$$
v_p(c_m)-b_{m,p}
=\min\{v_p(K_{m,p}),1+v_p(X_{m,p})\}.
$$



The displayed proof of this identity is straightforward and sound conditional on the preceding integrality and normalization statements: substitute `A=pK`, `B=p^2X/8`, note that `G_m` contains one copy of `p`, and take the minimum of the two valuations. The digit gate is exactly the base-`p` restatement of that identity. It organizes all depths but supplies no new distribution estimate.

Item 426 gives an actual step-two recurrence for the finite-field primitives. Its 49 homogeneous equations in 50 unknowns argument includes the necessary missing-kernel check: a derivative-only solution would produce a polynomial of degree below `p` with zero derivative and zero endpoint value, so it must vanish. Thus it really supplies a nonzero recurrence coefficient vector. This addresses a common possible defect in dimension-counting telescoper arguments. It still does not prove the leading and trailing recurrence coefficients are units on every row, and even an everywhere regular bounded-order recurrence does not bound isolated zeros by `o(p)`.

For the full tower define `R_n(m)` to be the prime radical where the post-baseline depth is at least `n`. The exact layer-cake identity reduces the aggregate problem to `sum_n log R_n(m)`. The most concrete new target in Item 427 is



$$
\sum_{n\ge2}\log R_n(m)=o(m),
$$



or another explicitly sufficient bound. Fixed-layer support ceilings cannot be summed over infinitely many layers without a uniform depth or tail estimate. The omitted small-prime set `p^2<=4m+1` has sublinear radical mass; this does **not** control its total valuation mass. Do not erase that tail in an all-depth argument.

The work-only status of Items 426 and 427 is retained; this audit is a targeted mathematical check, not a canonical promotion.

### Large-prime mixed-cubic branch: Items 390, 415, 418, 420, 423, 425

The useful exact object is the large-prime part of the gcd of the normalized pair



$$
\mu_{s,m}=\lambda_{s,m}/F_m,
$$



where the full forced squarefree Cartier factor is already removed. Item 418's recorded large-component upper ceiling is approximately `0.4287738853386578689457603829` per `6m`. It is an **upper bound for this component**, not a newly proved divisor lower bound and not a reduction of the whole unproved content requirement.

The archive's Items 420 and 423 prove scoped analytic barriers for fixed rational coordinate combinations and combinations with fixed polynomial coefficients in `m`. Item 425 extends this to the adjacent `2x2` determinant: the determinant contains `g_m g_{m+1}` but its exponential size is the square of the one-row size, so the average bound per row has no strict gain. Its algebraic coefficient identity is exact. Its claimed exact exponential limits depend on the saddle analysis in Items 420/423 and must be checked there; finite coefficient rows alone do not prove them.

The useful next target is a genuinely arithmetic bound on the **actual normalized gcd**, or a construction with growing complexity that overcomes its own height cost. Repeating fixed-coordinate cancellation, fixed-degree polynomial Bézout combinations, or the same adjacent determinant cannot supply the missing strict rate.

### Fixed j=1 and ordinary j=2 branches

The late `j=1` reports reduce the needed improvement to weighted prime collision mass. At a logarithmic window the actual cluster radical must beat a concrete coefficient, such as `1/12` per `M` in Item 400's retained setup. Generic discriminants and Vandermonde factors are coprime to the desired large endpoint primes; a small product of root differences does not carry those endpoints. Ambient support-only sieve estimates are explicitly saturated by countermodels. A new result must exploit the actual Hasse/transverse sequence across primes or across `M`.

The late `j=2` reports distinguish the tied prime from foreign prime divisors and show why transporting a degenerate gate does not automatically transport the target or its rejection. Items 419/422 settle parity issues on the second Frobenius sheet without producing a new independent period. The live problem remains a target-specific rejection/divisibility distribution theorem or a weighted anti-gcd estimate. Canonical Item 409 expressly keeps new formula-specific mechanisms open.

### Beta/continuant and older analytic constructions

The beta reports already analyze continuant divisor branches, all-depth transducers, endpoint resonance, first-hit localization, symmetric loads, and low-degree cancellation. Many formal extra coordinates collapse to the same target defect or saturate the same ambient content. A viable next step must control the actual first-hit or quotient correlation, not add another equivalent endpoint coordinate.

The older scripts contain extensive Padé, Hermite–Padé, pullback, root-of-unity, factorial-digit, Bessel, positive-kernel, quartic, and cyclotomic-unit work. Much of the remaining obstacle is arithmetic denominator/content growth or dependence on a target-specific approximation problem. An improved analytic radius or a smaller finite value alone does not bypass that arithmetic cost. Consult the existing exact endpoint and primitive-height formulas before launching another optimization.

## Ranked continuation from the computation archive

This ranking concerns concrete next subproblems, not an estimate that an irrationality proof is close.

1. **Actual first-Witt and higher-layer arithmetic.** Start with the explicit unbooked `j=0` cell in Item 426 and the two-stream invariant in Item 427. Seek a uniform structural relation, a provable regularity/zero estimate, or an aggregate valuation-tail theorem. Verify any proposed relation against `(13,11)`, `(24,11)`, and `(89,19)` before attempting a uniform argument.
2. **Actual normalized large-prime gcd.** Use the exact marked-branch residue description, with the full forced factor removed. Seek arithmetic restrictions on simultaneous prime divisibility that are absent from the analytic height argument. Keep marked and unmarked support distinct.
3. **Actual chosen-prime density in j=1/j=2.** Work on the concrete carrier whose divisibility is equivalent to the target, with the stated positive saving coefficient. Generic CRT realization or full ambient support is a test for whether a proposed theorem uses enough special information.
4. **A new growing-complexity approximation family.** Use only after writing the exact endpoint, denominator, content, nonzero condition, and exponential inequality needed. The archive has already ruled out many fixed-complexity variations.
5. **Additional numerical exploration.** Use only to test a sharply specified new lemma or seek a counterexample. Do not extend existing censuses merely to obtain more rows or more digits.

Every proposed improvement must say whether it is a lower bound for a divisor, an upper bound for a content component, a conditional implication, or a finite diagnostic. Those directions are not interchangeable. No computation inspected here changes the rationality status of `e+pi`.
