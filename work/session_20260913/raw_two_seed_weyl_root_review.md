> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root review of the actual two-seed Weyl/Nikishin test

Date: 2026-09-13. Verdict: PASS, including the explicit finite scope.

Reviewed `raw_two_seed_weyl_nikishin_test.md` in full and re-ran its
single N=4 exact counterexample and separate fixed moment-stabilization
check. All asserted rational identities, brackets and determinant signs
passed. No mathematical correction is required.

The alternating gauge makes both off-diagonals positive and sends the
actual second seed to −e1−(sqrt(3)/2)e0. The scalar block inverse gives
the displayed m, g and cross-resolvent r, including the signs and the
offset in both off-diagonal and lower-right entries. The block continued
fraction has the correct forward block orientation B_j W_(j+1) B_jᵀ.
The alternative quotient (8) is exactly W_01/W_00 before the seed
conversion. Exterior positivity follows by shifting to an irreducible
entrywise nonnegative matrix; its inverse powers preserve the stated
strict derivative signs. This does not force individual residues of a
cross-resolvent to have one sign.

The N=4 cubic pole brackets and quadratic zero brackets account for
all roots and are disjoint. The numerator is positive at each pole,
so the residue signs are +,−,+. The first five moments give exactly the
negative three-by-three Hankel determinant in (11). The separate
stabilized five moments at N≥6 give a positive determinant, correctly
preventing an extrapolation of that finite witness. The path-length
stabilization includes all scalar indices that a walk of those lengths
can reach and return from.

I checked the relevant definition in Fidalgo Prieto–López Lagomasino,
[Nikishin systems are perfect](https://arxiv.org/pdf/1001.0554),
Definition 1.2 on printed page 3 and its preceding measure construction.
The note retains constant-sign measures on disjoint support intervals
and the infinite-support limitation of the cited all-index theorem.
It tests one precise finite-atomic identification instead of treating
every positive matrix measure as such a system.

The necessary residue-sign lemma in Section 5 is self-contained and
correct. At a zero nu of the first Cauchy transform, subtracting
phi(nu) removes the constant term. The product
(lambda−s)(nu−s) is positive since s is outside the entire root-measure
support interval; its integral therefore has one sign. Dividing by the
negative derivative of the first Cauchy transform fixes a common sign
for all quotient residues. The actual N=4 signs violate this necessary
condition, even after the permitted constant shift or scalar change of
the second seed. Nonzero coupling at all three tail poles gives the
required cyclicity and four positive first-seed weights.

Finally the first-to-next block is invertible. Hence no nonzero vector
in the original two-seed span has its K image in that span, ruling out
the proposed constant scalar-Jacobi-chain identification for N≥4.
This does not rule out an individual scalar measure for either seed.

The conclusions remain scoped correctly: an all-N standard first-row
Nikishin claim is refuted, whereas eventual or transformed AT structure,
the large-index mixed Schur lower bound and irrationality are not
settled. The exact matrix continued fraction and scalar factorization
remain valid all-index tools for further work.
