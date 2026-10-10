> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Family021: exact inspected scope and original-index transfer filter

9 October2026. This is a literature/application scope note, not acceptance
of the claimed new Jacobsthal theorem. The official pinned source manifest
is in ../literature/family021_selection_scope/SOURCE_MANIFEST.json.
All acquired data match their pinned Git blob hashes. No downloaded build,
verification program or source instructions are executed.

Read in FULL: introduction.tex (269lines), inputs.tex (206lines),
assembly.tex (257lines), main.tex and README. The bibliography is acquired
but its entries are not independently verified. The intervening tree,
renewal functions, prime paths, reference, inverse, boxes, variance and
stopping proofs are NOT read in this scope. Thus the main theorem is NOT
audited, and neither its declared proof status nor a Lean file substitutes
for those missing dependency checks.

The inspected manuscript claims a uniform bound
h(k)<=C*k^2/(loglog(3k))^2 for arbitrary prime sets and translations,
and a quantitative lower count avoiding ONE prescribed residue at each
prime below a cutoff. Its assembly explicitly depends on reference,
inverse, variance and stopped-path propositions that are not inspected
here. The constant is not explicit. The exact permitted class condition
is important: one residue per prime, not arbitrary sets of residues at
composite recurrence periods or an unevaluated large-prime depth sum.

Primary source:
https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/paper.pdf

## Classical finite avoidance is already enough for infinite existence

This is REUSE of CRT and irrational rotation, not a new research theorem.
Suppose the actual frozen progression is j=j0+3^E*t. Let P be a FIXED
finite set of primes other than3, and suppose all proven bad conditions
at each p exclude at most ONE residue t=r_p modulo p. If any additional
fixed condition at3 is present, it must first be compatible with the
chosen source progression; a forced bad class cannot be removed by CRT.

Choose an admissible residue s_p at each p in P and set K=product P.
CRT gives t=a+K*v satisfying every selected avoidance condition. Every
such original j remains in j0 modulo3^E. For the real RangeIII window,
the step3^E*K*log_3(4) is irrational by unique prime factorization.
The already used irrational-rotation density argument therefore yields
infinitely many sufficiently large members in the same strict real
window. No quantitative Jacobsthal bound is required for this existence
claim. More generally, the finite union of admissible CRT cosets has
the product avoidance density when each prime excludes one residue.

This does NOT establish that our actual bad source conditions have this
form. In particular a recurrence period divisible by p-1, a multivalued
bad class, incompatibility at3, or a changing prime set needs a separate
proof. The signed original N=9^(18+32u) and the forced Gaussian states
cannot be replaced by an arbitrary affine parameter just to invoke a
one-class-per-prime statement.

## Exact remaining application gap

The present all-prime binary/odd final-G and signed intrinsic-J0 targets
involve EVERY prime and depth, including primes beyond the factorial
allowance and source-dependent unit collisions. No fixed finite prime
set containing all excess mass, no one-bad-class description for those
actual parameters, and no residual large-prime allowance is established.
Avoiding finitely many known exceptions cannot settle these targets.

Family021 may become useful for a QUANTITATIVE short search after a
source-specific finite-class reduction is proved. At the present scope
its claimed sharper interval length does not repair the missing reduction
or replace the already available qualitative CRT/window argument. No
full dependent-proof acquisition or external audit is requested merely
to repeat this conditional selection implication. The actual joint-depth
and finite inverse-return work continues.
