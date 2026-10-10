> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact finite integer-jet trees and the sixth-derivative ceiling

Root original method/application,2026-10-02. Author proof and exact certificates. Main research remains active.

## Scope and checks

Archive searches for an integral/Hurwitz Schur radius tree found earlier moment Schur complements and polynomial constructions, but no completed tree for this omitted-value endpoint problem. Fresh online searches and primary reads of Abate's multipoint Julia paper and Waldschmidt's Hurwitz-function survey confirmed the classical ingredients; this is a new arithmetic application of standard Schur interpolation. The correct inverse-coordinate coefficients come from the rational Schwarzian already derived, not from an unverified high-order derivative formula.

## Exact theorem

For a real endpoint-fixing map omitting1+i and1-i, integrality of its first six derivatives at0 implies

    R < 267/100 = 2.67.

The fifth-derivative certificate separately gives R<67/25=2.68, and the corrected fourth-derivative certificate gives R<27/10=2.70. The earlier manual2.66 fourth-jet claim is withdrawn because of a missing term in the fourth inverse derivative. These current trees use the full correct recurrence.

## Local inverse recurrence

Write r=xi''/xi', v=xi'. The exact rational Schwarzian is

    S(w)=((w-1)^2-3)/(2(1+(w-1)^2)^2).

At0 r=ell and v=1/a. Expand ordinary Taylor coefficients. The recurrences

    r'=S+(1/2)r^2,
    v'=rv,
    xi(w)=integral_0^w v(u)du

produce every required coefficient. They imply xi''''/xi'=S'+4rS+3r^3, so the erroneous3rS formula cannot enter the calculation. All scalar inputs a,t,ell have exact rational enclosures from SECOND_JET_RADIUS_CERTIFICATE.json.

## Exhaustion of integer choices

Let s=1/R. At any node, a real Schur function has prescribed endpoint T at s and its next constant is b=B+Fj, where j is the new integer derivative and

    F=R^k/[a k! product_(earlier b)(1-b^2)]>0.

The endpoint Schwarz-Pick condition is equivalent to

    (T-s)/(1-sT)<=b<=(T+s)/(1+sT).

Thus exact outward intervals give a finite complete integer interval for j. The lower endpoint is rounded DOWN before the integer ceiling, and the upper endpoint UP before the integer floor; no feasible integer is discarded. Each remaining j is explicitly checked or continued, with new prescribed endpoint R(T-b)/(1-bT). B is obtained by full formal composition of the inverse covering with the previous derivative jets, followed by the actual previous Schur divisions. This includes every lower-order mixed contribution.

Every arithmetic operation rounds outward on the rational grid10^-40. A coefficient or denominator that could touch a problematic boundary causes the program to stop as unresolved; it is never silently excluded. At the chosen test radii no boundary ambiguity occurs.

At R=2.67, the exact successive frontier counts are

    1,1,2,1,1,0.

The empty order6 frontier excludes every possible six-tuple of integer derivatives, and hence excludes every larger disk by restriction. FIFTH_JET_RADIUS_CERTIFICATE.json and SIXTH_JET_RADIUS_CERTIFICATE.json preserve all nodes, slopes, offsets, integer ranges and inequalities; integral_jet_schur_tree.py reproduces the trees.

## Positive uses and limits

A surviving finite prefix is not an infinite-jet existence proof. In this session, a special exact order8 prefix at R=2.65 also enters a separately proved contracting integer-lattice invariant; the normal-family and polynomial approximation argument is in INFINITE_INTEGRAL_JET_PULLBACK_EXISTENCE.md. That additional argument, rather than the mere presence of finite survivors, establishes the lower existence theorem.

The omission radius controls analytic Taylor decay only. It does not imply a useful primitive denominator or decide e+pi. The new exact tree is a tool for original construction and obstruction; it is not a re-audit of the archive's earlier constructions.
