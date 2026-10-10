> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Directed two-law energy: exact bridge and public barrier-certificate gate

Status: discarded original Genesis candidate. No certificate search, semidefinite optimization, or differential-independence route is started.

## Global nonlinear operation and numerical bridge

Retain the complete actual state trajectory

    X(z)=exp(z), Y(z)=4 arctan(z), 0<=z<=1,
    X'=X, Y'=4/(1+z^2), X(0)=1, Y(0)=0.

For a rational target r=a/b (b>0), consider a polynomial directed energy B(z,X,Y) with real or rational coefficients such that

1. B(0,1,0)=0;
2. B(1,X,Y) is divisible by b(X+Y)-a;
3. along the actual trajectory, its cleared Lie derivative

       L B=(1+z^2) B_z+(1+z^2)X B_X+4 B_Y

   is strictly positive on 0<z<1.

These conditions would prove S!=a/b: integration gives B(1,e,pi)>0, whereas the rationality hypothesis gives B(1,e,pi)=0. Weak nonnegativity together with a positive integral also suffices. Condition 3 cannot be inferred from formal polynomial manipulations or imposed as an independence axiom; it must be established on a region containing the complete actual trajectory.

This is a valid exact bridge with both laws retained. In particular, it does not assume rationality of an endpoint derivative, transformed constant, or source component. A proposed tool would construct such energies for all rational targets using global positivity and the actual laws.

## Immediate gate verdict

The essential operation is already the public barrier-certificate/unreachability mechanism: a function separates endpoint data from trajectories using the sign of its Lie derivative. The arctangent denominator is positive and can be cleared, or a positive time change can make the displayed rational system polynomial. The endpoint divisibility condition is a concrete special case of imposing an unsafe target set.

Consequently this candidate is discarded under the human's essential-mechanism rule even though this specific rationality application was not located in the bounded searches. No SOS hierarchy, denominator-dependent certificate family, or parameter optimization is developed.

## Scoped bounded-complexity observation

Suppose a sound fixed-complexity certificate scheme has a real-target feasibility set F that is semialgebraic over Q. Suppose S lies in a rational open interval I, S is not in F (as soundness requires), and every rational target in I is in F. Then S is algebraic.

Proof: I\F is semialgebraic over Q and contains no rational number. A one-dimensional semialgebraic set with an interval contains rational numbers; hence I\F is a finite set of points. Each such point is a boundary point among the finitely many polynomial sign conditions in a quantifier-free description, and is a root of a nonzero rational polynomial. Since S belongs to it, S is algebraic.

The hypothesis about semialgebraic feasibility must be checked for the particular scheme. It holds for a finite polynomial template with real coefficient variables and a finite first-order formula of polynomial equalities/inequalities with rational data, by real quantifier elimination. It does not automatically hold for rational-coefficient existence, arbitrary degree, or positivity tested only on an analytically defined actual trajectory. Rational-coefficient certificates imply real-coefficient feasibility, but these two feasible sets are not identified.

This observation does not prove that such certificates exist, that S is algebraic, or that fixed-degree certificates cannot prove irrationality: algebraic irrational exceptional points are compatible with its conclusion. It identifies a substantive consequence that a uniform finite scheme would have to establish, rather than silently assuming it. This is classical semialgebraic support, not a retained new obstruction tool.

An exact comparison model prevents a stronger false no-go claim. Consider x'=1/(2x), x(0)=1, on 0<=z<=1, so x(1)=sqrt(2) and I=x^2-1-z is invariant. For any real target r put c=r^2-2 and

    B_r(z,x)=z c^2-c(x^2-1-z).

Then B_r(0,1)=0, B_r(1,x)=c(r^2-x^2) is divisible by x-r, and its derivative along the complete rational vector field is c^2. It is strictly positive for every rational r. Thus a degree-two polynomial in the state/time variables supplies a directed-energy certificate excluding every rational endpoint, with coefficients rational whenever r is rational. The exceptional targets are exactly the algebraic points +/-sqrt(2), consistent with the semialgebraic lemma. This model does not preserve the actual exponential/arctangent laws; it demonstrates that the legitimate direct rational-target exclusion bridge should not be replaced by an unjustified demand for a second algebraic output or by a blanket impossibility claim for fixed-degree certificates.

## Archive and fresh primary receipts

Archive query, over sources and work Markdown: `barrier certificate|Prajna|Jadbabaie|Positivstellensatz|sum.of.squares.{0,40}(differential|trajectory|invariant)|Lie derivative.{0,40}(positive|barrier)`. No exact match was returned; this bounded negative result does not imply novelty.

Fresh online queries:

- `Prajna Jadbabaie safety verification dynamical systems barrier certificates polynomial differential 2004 pdf`
- `polynomial barrier certificate endpoint equality unreachable state Lie derivative positive invariant rational differential equations`
- `sum of squares transcendental constants irrationality differential equation barrier certificate`
- `Safety verification of hybrid systems using barrier certificates pdf Caltech`
- `On the necessity of barrier certificates pdf Rantzer Prajna`
- `barrier certificates for nonlinear model validation pdf Prajna`

Opened primary materials:

- Prajna's full 25-slide author presentation, *Barrier Certificates for Nonlinear Model Validation*, CDC2003, https://www.mit.edu/~parrilo/cdc03_workshop/Prajna.pdf, especially slides 4--10: endpoint/time-domain data, Lie-derivative invalidation theorem, and polynomial/SOS certificates. These directly match the proposed operation.
- The full 24-page primary CAV2021 paper, *Synthesizing Invariant Barrier Certificates via Difference-of-Convex Programming*, https://fiction-zju.github.io/papers/CAV2021-a.pdf.
- Platzer's full 66-page author chapter on hybrid-system verification, https://www.cs.cmu.edu/~aplatzer/pub/HBMC.pdf, for the established differential-invariant framework; no unseen arithmetic theorem is attributed to it.

Failed reads: the Prajna--Rantzer2005 full PDF on CiteSeer returned403, and the Prajna2006 publisher article fetch returned403. Their search metadata is not claimed as a full read. The successful author presentation already supplies the decisive mechanism match.
