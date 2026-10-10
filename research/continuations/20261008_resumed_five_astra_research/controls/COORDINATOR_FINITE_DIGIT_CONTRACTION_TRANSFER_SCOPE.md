> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Finite digit contraction: reuse, a paid inverse interface, and open transfer

9 October 2026, ongoing funded research. This is an application filter and
a concrete interface for a future assignment. It evaluates no original
endpoint and authorizes no large computation.

## Overlap and primary literature inspected before this direction

The original finite HIGH inverse kernel is ALREADY in the archive. In
particular, October 5 A1 turn25, lines 175--240, gives the finite inverse
orientation and retains the intersections with BOTH HIGH ends; its
larger argument is not newly proved here. October 5 A4 turn17, lines
180--250, explicitly distinguishes the coefficient-gap consequence from
the hypotheses identifying the actual finite matrix. The current A1
turn14, section 2, supplies the current core's actual normalized blocks
and their mod3 unit structure. Classical finite Neumann lifting is also
already reused in the current precision-local-producer gate. None of
these algebraic identities is claimed as new.

Scoped literal searches of the current and previous response trees,
October 5 records, and the primary-literature entry found no Bacher
recurrence-matrix application to this complete original contraction.
This is a scoped search result, not a claim that no related mathematics
exists elsewhere. A broad initial archive query hit large generated
indexes and was replaced by filename-scoped Markdown searches.

The PRIMARY reference inspected is Roland Bacher, *Recurrence matrices*,
arXiv:math/0601372v2 (24 November 2006):

https://arxiv.org/html/math/0601372v2

Personally inspected scopes: the introduction; the shift/recursive
closure definitions; Proposition 4.6 and its COMPLETE product proof;
the invertibility distinction in section15, especially Remarks15.4--15.5;
section17's inverse algorithm and termination hypotheses; the finite
state description in section24; and the length-dependent transition
definition and warnings in section28. Other sections and the full
81-page PDF are NOT claimed fully read or audited.

The useful product identity is

    rho(s,t)(AB) = sum_v rho(s,v)(A) rho(v,t)(B).

It supplies multiplication of given finite representations. It does
NOT say that an entrywise finite-state matrix has a finite-state inverse.
Remark15.5 explicitly warns against that implication. Section17's
algorithm presupposes membership in the group whose inverse is already
of finite recursive complexity; it may not terminate without this.
Section28 allows length-dependent transitions but warns that saturation
tests are no longer generally available. Its field-based saturation
algorithm is NOT imported over Z/3^K.

## Exact original mod3 inverse interfaces to reuse

Use the current core's A+D=H=3^(h-1), original LOW rows0..D-1, HIGH
rows d..m, and l_H=m-d+1. In HIGH local coordinates u=s-d,v=t-d,
the sole surviving normalized physical pole3H gives

    Ebar_H[u,v] = [z^(u+v-(l_H-1))](1-z)^A over F3.

Negative coefficient indices are zero. Indeed the complete rational
polynomial is (y-1)^A y^(s+t)(beta+3y), beta=1 mod3, and its physical
coefficient is at (3H-1)/2. At s+t=m+d that extraction asks for the
leading coefficient of (y-1)^A, hence1; all smaller sums are zero.
This is the current specialization of the already archived inverse.

Reversing the rows makes a finite upper triangular Toeplitz matrix,
so its ORIGINAL finite inverse is

    Rbar_H[u,v] = [z^(l_H-1-u-v)](1-z)^(-A).

Every coefficient degree used is below H. Since

    (1-z)^(-A) = (1-z)^D/(1-z^H) over F3,

the needed coefficients are those of (1-z)^D. This is an explicit
mod3 inverse on BOTH original finite ends, and not an infinite inverse
whose projection is being assumed. It sends the literal terminal
e_(l_H-1) to e_0. No full-precision inverse follows from that fact alone.

The current LOW law is likewise established reuse:

    Lbar[u,v] = [z^(D-1-u-v)](1+z)^(-a_L), a_L=(H+1)/2.

Its finite inverse has coefficients

    Rbar_L[u,v] = [z^(u+v-(D-1))](1+z)^(a_L).

These two orientations are different. Literal Lucas digit coefficients
in {0,1,2} give integral LIFT matrices T_L,T_H of these mod3 inverse
matrices; this does not make either lift the higher-precision inverse.

## Paid finite lifting, with no division of an unknown defect

For any fixed K, work over Z/3^K in the ACTUAL finite dimensions. Put

    B_L = I-L*T_L.
    M_L = T_L * sum_(j=0)^(K-1) B_L^j modulo3^K.

B_L is divisible by3 entrywise. The displayed finite expression is a
true inverse because L*T_L=I-B_L and B_L^K=0 modulo3^K. Now form the
complete HIGH Schur matrix

    S_H = E_Y-3*X^T*M_L*X,
    B_H = I-S_H*T_H,
    M_H = T_H * sum_(j=0)^(K-1) B_H^j modulo3^K.

Again B_H is divisible by3 and the actual finite inverse identity is
paid. These are classical finite Neumann identities, not a new theorem.
There is NO need to divide a matrix defect by3. In particular, the
LOW MATRIX return stays inside S_H.

For a digit product implementation, pad EACH original finite space
separately into a power-of-three box with identity on its complement,
and set the rectangular X and the sources to zero outside their actual
ranges. All products then have exactly the original sums. Range masks,
shifts, and reversal must be included in the digit representation;
using unmasked complete digit boxes would change the inverse.

The matrix-product transition identity above remains elementary over
the commutative ring Z/3^K: distribute the finite internal-digit sum.
Thus GIVEN explicit, validated finite digit representations for the
normalized actual entries, inverse lifts, range masks, and sources,
the two finite Neumann polynomials provide an inverse representation
by products and sums, without any general automatic-inverse theorem.
Contraction with the complete sources then uses the same product rule.

## What is still missing and cannot be inferred

An O(h) ONE-entry factorial-unit arithmetic producer is not yet a
proved small digit representation for ALL entries. Its unit windows,
parity, affine argument carries, valuation deficits, original cutoff,
and parameter digits need exact transitions. All14 Omega terms, both
beta/3y channels, and the physical3H unit resonance remain necessary.
The factorial part is integral and vanishes modulo the current target
after multiplication by3^h (or3^(h-1) in normalized LOW pairings), but
that fact does not remove any rational pole or LOW matrix return.

Even a valid product construction may have a state space growing as
a large power of the entry-state dimension. A bound independent of
the original exponentially large matrix dimension can still be far
too large to execute. A practical frontier/state reduction must be
proved before computation is proposed. No unbounded inverse-guessing,
original-length arrays, saturation search, or large tensor is approved.

For the currently open scalar use K=28 for the complete contracted
return, or a carefully paid K=27/K=26 split in

    w_H=(M_H*upsilon_T-e_d)/3,
    f_H=upsilon_0/3,
    w_H^T*f_H modulo3^26.

The coordinate quotient for w_H must retain one EXTRA precision digit;
it is not an entrywise ring division modulo3^26. The current column-
defect alternative remains S_H(e_d+3z)-upsilon_T in3^27. The complete
scalar has NOT been evaluated by this note. The possible new research
is the ACTUAL finite representation and a usable state bound, rather
than rederiving Jacobi, Lucas, finite Neumann, or generic automaticity.
