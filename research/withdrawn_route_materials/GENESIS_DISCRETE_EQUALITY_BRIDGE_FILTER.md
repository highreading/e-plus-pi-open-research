> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Numerical equality bridge filters for discrete candidates

These are elementary design constraints, not a retained new irrationality mechanism and not a novelty claim. They collect the precise failures found while authoring G1–G4. All relevant archive/public gates are in `GENESIS_DISCRETE_CANDIDATE_LEDGER.md`.

## 1. Local complexity can coexist with a rational scalar

Consider an almost surely terminating rational-transition tree. First toss fair bits until the first 1, at time K>=1, then toss K further fair bits and output the last bit. The output probability is 1/2, and the expected running time is finite because E[K]=2.

A reachable state with d fair tosses remaining has probability zero of reaching either output in fewer than d steps, and probability one of reaching an output at step d. Those properties distinguish states for distinct d under every output-labelled, time-preserving probabilistic bisimulation. Infinitely many such states are reachable. Thus even rational output and finite expected work together do not imply a finite quotient of the chosen sampler. The single-output law is also realized by a one-toss tree.

This rules out using the original representation's unbounded state count as the numerical bridge. It does not rule out every imaginable value-sensitive combinatorial invariant.

## 2. A continuous local cancellation charge vanishes identically

Let V be the abelian group of rational-valued, absolutely summable sequences, with the inherited ell^1 metric. Let A be a Hausdorff topological abelian group and let J:V->A be a continuous group homomorphism. Suppose J annihilates every finitely supported rational sequence.

Then J=0. For w in V, its finite truncations w^{(N)} converge to w in ell^1. Every J(w^{(N)})=0; continuity gives J(w)=0. Hausdorffness makes the limit unique.

Equivalently, if a proposed local charge regards all finite rational masses as trivial and is continuous under absolutely summable tail removal, it cannot distinguish ANY convergent rational-weight expansion from a rational finite mass. A nontrivial irrationality charge must abandon at least one of those hypotheses; doing so requires an actual justified numerical bridge. Calling the target a new grade does not provide one.

For a scalar function f:R->A with f(x+q)=f(x) for every q in Q, the same elementary argument shows that continuity forces f to be constant, since Q is dense. This is classical density, credited as such. No discontinuous charge is constructed here.

## 3. The legitimate ray bridge exposes a boundary problem

For rational weights w_n with sum (n+1)|w_n| finite, the unique real sequence u_n tending to zero and satisfying u_n-u_{n+1}=w_n is

    u_n = sum_{j>=n} w_j.

It lies in ell^1. If sum w_n is rational, each u_n is rational. Conversely u_0 is the total sum, so the existence of such a rational sequence is sufficient. For the e+pi weights

    w_n = 1/n! + 2^(n+1)(n!)^2/(2n+1)!,

this is an exact equivalence. The second term's ratio is (n+1)/(2n+3)<1/2, so the required moment convergence is immediate; its total is pi by the integral expansion in G4.

The recurrence itself is solvable with EVERY rational initial u_0: all its finite values remain rational. Decay at infinity singles out the actual S. Consequently showing no primitive in a chosen symbolic term class is not enough. Rationality supplies rational values, not a closed-form representation or a finite algebraic certificate. This separation is particularly relevant when proposing a new combinatorial cancellation flow.

## 4. Scope and next design requirement

None of these elementary statements establishes whether e+pi is rational. They delimit three failed bridges: original representation complexity, a limit-continuous rational-annihilating charge, and restricted symbolic solvability.

A new discrete operation must give a necessary property of the actual scalar equality with a rational number and prove its violation from the specific exponential/circular data. No representation-faithfulness axiom, scalar-independence conjecture, or closed-form restriction will be assumed.
