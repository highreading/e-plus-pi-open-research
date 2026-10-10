> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Genesis discrete/combinatorial mechanism ledger

Status: active original research. L24 is complete in `WEIGHTED_REGULAR_EXACT_DYADIC_ENDPOINT_THEOREM.md`; no old-route extension is being developed. Read the root's `main/GENESIS_STAGE_PROTOCOL.md`. A negative bounded search is never a global novelty claim.

## G1 — paired rounded cuts / mechanical-word complementation — DISCARDED

Object: for positive integer b, C_b(n)=floor(b n e)+floor(b n pi), n>=1. If e+pi=a/b, the irrationality of e and pi separately gives C_b(n)=a n−1. Conversely that identity for all n implies e+pi=a/b by division by b n and passage to the limit. First differences give complementary mechanical words after removing integer slopes. The proposed falsifiable target was failure of this identity for every a,b.

Archive gate: searched `sources` and `work` Markdown with `Beatty|Sturmian|mechanical.word|groupoid|combinatorial.species|Bernoulli.factory|probabilistic.bisimulation|decision.tree|weight.*bijection|sign.reversing.involution`. No Beatty/Sturmian route was located in those files. An inherited lattice-path sign-reversing involution occurs in `work/session_20261001_astra/agent3/ENDPOINT_FACTORIAL_KERNEL.md`; it is unrelated to rounded cuts.

Public queries: `complementary Beatty sequences Sturmian words sum irrational slopes rational primary paper`; `mechanical words fractional parts rational linear relation complementary Beatty theorem arxiv`.

Primary sources opened successfully:

- J.-P. Allouche and F. M. Dekking, *Generalized Beatty sequences and complementary triples* (2019), https://arxiv.org/pdf/1809.03424 . Its introduction and Section 2 explicitly use floor sequences, complementary partitions, and homogeneous Sturmian first differences.
- Kevin O'Bryant, *Sturmian Words and the Permutation that Orders Fractional Parts*, https://www.math.csi.cuny.edu/~obryant/Mathematician/Papers/BeattyMatrices/SWPOFP.pdf . This studies mechanical words and the ordering of fractional parts.

Decision: the essential operation is classical rotation/Beatty/Sturmian coding. The exact specialization to e and pi supplies no new tool. Discard promptly; do not pursue word statistics, finite residues or digit refinements.

## Research discipline

Each subsequent candidate must have a numerical-value equality bridge. An invariant of two chosen representations, without an implication from equality of their real values, is insufficient. No unproved faithfulness axiom or independence conjecture will be added.

## G2 — exact sampler / finite probabilistic quotient — DISCARDED

Object: a rational-transition decision tree generating Bernoulli(S/8). An explicit tree exists because rational interval bounds for e and pi compute S/8, which lies in (0,1): compare a uniform random binary real with those bounds until separated. An equivalent mixture uses Bernoulli(e/4) and Bernoulli(pi/4) with equal choice weights.

Proposed obstruction: prove that this specific tree has no finite output-preserving probabilistic quotient, and infer irrationality from the fact that a rational Bernoulli probability has a finite rational-transition sampler.

Fatal bridge defect, proved by countermodel: toss fair bits until the first 1, at time K; then toss K more fair bits and output the last one. The output has probability exactly 1/2. Its reachable delay states have arbitrarily large different minimum times to an output. Output-labelled, time-preserving probabilistic bisimulation must preserve all finite-time output probabilities; delay states of different lengths therefore cannot be identified. Thus the original tree has no finite such quotient despite rational output. A different two-leaf tree realizes the same output law. Unbounded representation complexity is not an invariant of that single scalar probability.

Archive gate: the G1 combined `sources`/`work` search included `Bernoulli.factory|probabilistic.bisimulation|decision.tree`; no substantive match was located in those Markdown files.

Public queries: `Knuth Yao complexity nonuniform random number generation decision tree rational probabilities primary paper`; `probabilistic bisimulation rational probability infinite Markov chain finite quotient primary paper`; `exact random sampling arbitrary computable distribution rational Bernoulli decision tree primary paper`.

Primary sources opened:

- C.-D. Hong, A. W. Lin, R. Majumdar and P. Rümmer, *Probabilistic Bisimulation for Parameterized Systems* (2019), https://link.springer.com/chapter/10.1007/978-3-030-25540-4_27 . Its full HTML defines rational-transition systems, bisimulation, and finite/regular symbolic quotients. These are the essential candidate operations.
- L. Devroye and C. Gravel, *The expected bit complexity of the von Neumann rejection algorithm*, https://arxiv.org/pdf/1511.02273 . Opened the primary full PDF; exact sampling and decision-tree complexity are already established objects.
- The 1991 Larsen–Skou ScienceDirect full-page fetch failed; it is not counted as a read.

Decision: DISCARD both because the operation is established and because the required equality-to-finite-quotient implication is false. No sampling-complexity, automatic-tree or Bernoulli-factory refinement will be pursued as a Genesis mechanism.

## G3 — finite-set/cyclic groupoid cancellation — DISCARDED

Object: take the finite-set groupoid E, with one component B(S_n) for every n>=0, so |E|=sum 1/n!=e. A positive cyclic-groupoid representation of pi comes from pi=2 sum_{n>=0} binom(2n,n)/(4^n(2n+1)); use 2 binom(2n,n) copies of B(C_{4^n(2n+1)}) at level n. Their disjoint union has cardinality S. Proposed target: a new cancellation operation detecting that this union cannot be equivalent, after allowable local refinements, to a finite groupoid of cardinality a/b.

Bridge limitation: equal cardinality does not imply equivalence even for finite groupoids. B(C_1) and two copies of B(C_2) both have cardinality 1 but different numbers of isomorphism classes. Therefore a cancellation obstruction stronger than numerical cardinality is not forced by rationality. Adding a numerical-faithfulness theorem without proof would be precisely the forbidden extra premise.

Archive gate: the earlier combined search covered groupoids and species. The later query `cancellation.*compact|bounded.*transport|mass.*transport|common.refinement|prefix.code|Kraft|group.ring|Atiyah|Betti|refinement.*invariant|continuous.*invariant|value.*faithful|representation.*faithful` located root's newly discarded origin-to-value grading, but no developed groupoid cancellation route in the searched Markdown.

Public queries: `countable rational weighted partitions equal sum common refinement locally finite matching transport`; `irrationality groupoid cardinality combinatorial rational sum equivalence`; `rationality invariant infinite weighted combinatorial cancellation refinement`.

Primary sources opened:

- J. C. Baez, A. E. Hoffnung and C. D. Walker, *Higher Dimensional Algebra VII: Groupoidification* (2009), https://math.ucr.edu/home/baez/hda7.pdf . Section 2 explicitly contains the finite-set groupoid of cardinality e and groupoid cardinality as the sum of reciprocal automorphism orders.
- J. E. Bergner and C. D. Walker, *Groupoid Cardinality and Egyptian Fractions* (2011), https://math.ucr.edu/~jbergner/GpdEFrac.pdf . Opened full primary PDF; rational cardinalities and groupoid realization are established.
- *On analytic groupoid cardinality*, https://arxiv.org/pdf/2104.11399 . Opened full primary PDF; recursive/nested equivalence and analytic cardinality already exist.

Decision: DISCARD. Groupoidification/cardinality is an established essential operation, and the equality-to-equivalence bridge fails. No replacement of ordinary cardinality by a representation grade is retained.

## G4 — rational summable ray primitive / boundary cancellation — DISCARDED

Object: a directed ray with rational source weights

    w_n = 1/n! + 2^(n+1)(n!)^2/(2n+1)!, n>=0.

The second positive series sums to pi. To see this without invoking a special identity, expand 1/(1+x^2)=(1/2) sum_{n>=0} ((1−x^2)/2)^n on [0,1] and integrate; the elementary beta integral gives the displayed coefficients. Both components have finite first moment.

Exact numerical bridge: S is rational iff there is u in ell^1(Q) with u_n−u_{n+1}=w_n. Indeed the unique real decaying solution is u_n=sum_{j>=n}w_j. If S is rational, u_n=S−sum_{j<n}w_j is rational and sum_n |u_n|=sum_j(j+1)w_j<infinity. Conversely a rational decaying solution gives S=u_0. The proposed obstruction was a new boundary-cancellation invariant forbidding a rational ell^1 primitive for the two different source recurrences.

Why closed-form nonsummability does not bridge the gap: the rationality hypothesis implies only a rational-valued decaying sequence, not a rational function of n times either hypergeometric source. Every such sequence is determined by a single initial number; restricting the admissible primitives to a symbolic difference field would add a hypothesis that scalar rationality does not supply.

Archive gate: `cohomolog|coboundar|summable.*primitive|rational.*primitive|telescop.*irrational|Gosper|indefinite.*summ|boundary.*flow|discrete.*primitive` located extensive earlier Gosper and coboundary work. Opened `sources/mixed_extension_moment_kernel_audit.md` for its gate-level exact reduction statement only: closed rational integration-by-parts cancellation is a split coboundary, with endpoint values in Qbar+Qbar e+Qbar pi. This is an existing essential mechanism; no independent review was undertaken.

Public queries: `rational summation difference equations cohomology irrationality telescoping hypergeometric series`; `Gosper algorithm indefinite summation hypergeometric terms primary paper`; `discrete coboundary summable sequence zero sum primitive`.

Opened primary PDFs: Chen–Huang–Kauers–Li, *A Modified Abramov-Petkovsek Reduction and Creative Telescoping for Hypergeometric Terms*, https://arxiv.org/pdf/1501.04668 ; *Gosper Summability of Rational Multiples of Hypergeometric Terms*, https://arxiv.org/pdf/2105.05567 . The former explicitly reduces summation to quotienting by differences and constructing residual forms.

Decision: DISCARD. The actual equality bridge is elementary telescoping; the proposed essential obstruction is existing difference/coboundary summation, and symbolic nonexistence would not decide rational-valued decaying existence.

## G5 — signed rational two-clock subdivision — DISCARDED

Exact operation and gate are in `GENESIS_SIGNED_CLOCK_ADJUSTMENT_GATE.md`. A rational word has exponential product exp(sum t_j) and full circular increment 4 sum atan(t_j). The zero-angle triple `(1/(2d),1/(2d),-4d/(4d^2-1))` permits an exact finite adjustment of the first time by any rational number. An explicit 34-letter word preserves the actual pair (e,pi) without opposite-letter cancellation. Three-letter simultaneous refinements are exactly `{1,t,-t}`.

Opened the full primary Abrate--Barbero--Cerruti--Murru PDF, https://arxiv.org/pdf/1409.6455, Section1. Its rational tangent addition operation and exact angular-word constructions are the essential public match. The formulas above are proved elementary background, not attributed as an exact theorem in that paper or claimed globally novel. The prospective obstruction through subdivision rigidity is discarded; preserving the original trace gives no new arithmetic relation, and changing the time does not preserve algebraicity by any proved theorem. No Machin approximation, content, or functional-cocycle variant is pursued.
