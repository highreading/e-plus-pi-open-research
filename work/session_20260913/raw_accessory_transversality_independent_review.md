> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of accessory transversality and unique lifts

Date: 2026-09-13. Reviewer: audit_results.

Reviewed raw_accessory_transversality_and_unique_lifts.md in full.
**Verdict: PASS.** No mathematical correction is required. The note
proves full parameter-Jacobian rank, unique possible congruence lifts,
and exact residual depth; it does not assume that those lifts continue
or bound their number.

## 1. Parameter recovery and dual-number reconstruction

I independently expanded the conjugated operator and obtained exactly

    -b1+beta-3d^2+d,
    -2b2+(beta-3d^2+d+2)b1+gamma-2d-2

as its first two relevant coefficient equations for monic B. Thus
both recovery formulas (1) have the stated signs and constants and
introduce no division. They remain valid in rings with nilpotents.

The extension of the four-equation sufficiency construction to
K[epsilon]/epsilon^2 is justified by actual unit charts: the selected
maximal minor of U_d, a coordinate of C*, and the initial determinant
all remain units because their residues are nonzero. The downward
exponential and finite-jet indicial pivots remain units, including
the allowed boundary p=M. There is no unproved analytic lifting step.

A vector in the four-row Jacobian kernel therefore produces a
normalized triple T+epsilon Tdot satisfying the same constant linear
Taylor matrix. Its top B derivative is zero; injectivity of that
functional on the residue-field extremal kernel forces Tdot=0.
The two recovery identities then force both parameter derivatives
to vanish. Equivalently the variation operator has leading
coefficients u and, after u=0, v. This proves rank exactly two.
It correctly does not identify the exponential pair as an invertible
Jacobian pair in every case.

## 2. Geometric uniqueness and all congruence depths

The unique monic kernel vector of a matrix over F_p is defined over
F_p even if the root is initially taken over an algebraic closure.
Parameter recovery gives uniqueness and descent of the accessory
point. The ideal-theoretic refinement is sound: the quotient with
one geometric point is zero-dimensional, and the rank-two linear
parts kill its cotangent space. Nakayama then kills the maximal
ideal of this Artinian local algebra. There is no remaining
nilpotent parameter direction in the residue-field quotient.

At depth h<=f, the actual rectangular Smith matrix has a free
rank-one kernel modulo p^h. Its final Smith column has unit top B
coefficient by the residue-field theorem, so monic normalization
selects exactly one vector. At h>f the remaining coordinate is
divisible by p and cannot have monic top B. The same recovery
formulas establish uniqueness of parameters at each allowed depth.

## 3. Two selected equations and the exact obstruction

Any nonzero two-row Jacobian minor gives a unit pair G. The stated
Newton correction is valid at every h>=1, since 2h>=h+1 makes
all quadratic errors disappear at the next depth. It yields exactly
one G-root over Z_p in the fixed residue class, without any assertion
about the other two equations H.

The remaining two residuals at that root therefore measure precisely
the largest common congruence depth. At least one is nonzero, or
there would be primitive approximate kernels at arbitrarily large
depth, contrary to the finite Smith valuation. Thus

    f=min(v_p rho1,v_p rho2)

is an exact finite equality. The one-step Schur obstruction
r_H-J_H J_G^(-1) r_G has the correct minus sign and is independent
of the representative, because replacing that representative adds
a vector in the full Jacobian image. Its cokernel has dimension two.

## 4. Completed local quotient and the remaining limitation

After centering at the selected pair's p-adic root, the two G
polynomials have zero constant terms and an invertible linear
coefficient matrix. Formal inversion over Z_p therefore gives
the claimed coordinate change, with no nonunit divisions. Modding
out by those two coordinates sends H to its two constant residuals.
The completed local algebra is exactly Z_p/(p^f).

This conclusion is about the completed local quotient. Promoting
it to the global finite quotient requires the separately proved
finite algebra for E0,E1; the note retains that distinction.

Finally the elementary ideal (u,v,p^a) confirms that a full
parameter Jacobian and a reduced residue-field point permit
arbitrarily large vertical p-adic thickness. The note consequently
does not turn transversality into an unsupported depth bound.
