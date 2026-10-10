> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root review of the fixed-prime bounded-run result

Status: the new auxiliary upper bound passes this review, conditional on
the explicitly identified global recurrence and branch identities in
Items 237, 309 and 314. It does not prove the main irrationality result.

Read the complete new `fixed_prime_stepanov_attempt.md` and checker, the
second-branch derivation in Item309 Section6, and the complete Item314
report. Re-executed the exact rational-function verification. All residue
identities, factorizations and initial minors agree with the report.

The substantive checks were:

1. The actual rows at fixed p are exactly r=e+6n, s=s0-2n, with
   0<=n<floor((p-2e+3)/12). There is no additional unhandled residue class.
   The phase is 4^s0 16^{-n}; hence Item309's branch scaling cancels it.
2. The reverse recurrence is a rational-function identity. Its quintic
   factors cancel before evaluation modulo p. The normalized coefficient
   of u_n is exactly one. All remaining variable denominator numerators
   are at most 2r+51, so s>=9 makes them strictly smaller than p.
3. The new recurrence reduces legitimately modulo p: Item314's uniform
   clearer 6^{r+3}r! is a p-unit on every actual row, not only nonsingular
   connection charts. Thus each u_n appearing in a propagation step is
   p-integral. Fixed rational coefficient denominators are included in
   the finite exceptional prime set.
4. Four consecutive zeros beginning at j>=1 propagate backward using
   the recurrence at j-1, whose s value is at least 9. This eventually
   contradicts the nonzero first-two-coordinate branch minor. A block
   beginning at zero contradicts that minor immediately.
5. For a three-zero block beginning at j>=1, the preceding entry cannot
   vanish. The original order-three recurrence therefore forces
   P_0(h_j-3)=0. Its linear factors are units because the start has s>=7
   and the largest numerator is 2r+39. Hence Q(h_j)=0. Distinct actual
   indices give distinct h_j modulo p; a nonzero quintic has at most
   five roots. This is an exact finite-field polynomial theorem, not an
   observed root count.
6. Disjoint blocks of three yield at most (2/3)|I|+17/3 zeros, so the
   displayed additive constant six is safe even at both interval ends.
7. The map M=(7p+e)/6+n takes an M interval to an n interval. Summing the
   additive errors over p costs O(X), not O(X^2), on a dyadic block.
   A fixed exceptional prime contributes only finitely many actual rows
   and eventually disappears. The prime support width is 6/7-4/5=2/35,
   giving the normalized average upper bound 2/315.

No correction was necessary. The global order-three recurrence itself
was not independently re-derived in this particular review; the note
retains it as an explicit archived theorem dependency.

The distinction between quantifiers is essential: an averaged upper cap
does not bound the limsup on a sparse favorable subsequence. Therefore
the improvement from 1/105 to 2/315 cannot be subtracted from the global
favorable-subsequence lower-gain target. The gain ledger remains exactly
as it was. This result narrows one support estimate and identifies short
clusters and isolated zeros as the remaining o(p) obstruction.
