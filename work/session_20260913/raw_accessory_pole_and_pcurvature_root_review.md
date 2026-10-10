> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root audit of the new pole, enveloping-algebra and curvature identities

Date: 2026-09-13. Result: PASS for the original algebra in Sections3–5
of literature_accessory_heine_stieltjes_and_pole_identity.md.

The primary-theorem applicability record is the source agent's targeted
literature review. This independent pass checks the new identities and
their actual normalization, without claiming to reprove those external
classification theorems.

Applying the proposed sl2 expression to z^m gives exactly the four
coefficients in the actual operator. In particular the weight-preserving
factor expands to m(m-1)(m-3d)+(m-d)beta+2d^2(d-1), and the
two lowering factors give m(gamma-m+1) and
m(m-1)(m-3d-4). The expression is an integer Weyl-algebra identity,
so its characteristic-p use does not divide by a hidden generator
normalization. Preservation of P_d and the missing degree-d output
follow from the two stated leading cancellations.

In the cleared Wronskian, the only surviving first-column contribution
modulo D is -CD' in the final row. Its cofactor is -J, with positive
cofactor sign, giving N=CD'J modulo D. Since z is a unit in R[z]/D
and D'=2z, N=kappa z^s gives CJ=(kappa/2)z^(s-1).
The determinant norm of z is1, and that of2 is4; hence the displayed
resultant identity has exactly the factor4 and kappa^2. It preserves
the actual scalar of C and of the Wronskian. Product invertibility in
this commutative ring does imply both resultant factors are units.

Adding and subtracting the two logarithmic derivative equations at
i,-i gives the root-sum identities with the stated minus signs.
Repeated roots contribute their multiplicities. Unit C modulo D makes
all denominators nonzero. The local multiplicity arguments at ordinary
points and at0 retain every integer factor below p. They permit double
ordinary roots and do not assert squarefreeness.

For the companion connection, the rational columns from C and the
gauged B satisfy nabla w=0 and nabla v=-v. Their independence follows
from the nonzero rational logarithmic-derivative argument. The p-th
iterate of d/dz on K(z) is zero, so p-curvature has eigenvalues0,-1.
Because p>3, these distinct eigenvalues also rule out a nilpotent class
modulo scalar matrices; a rational gauge cannot remove this obstruction.
This says nothing against correspondences that allow a nonzero
semisimple curvature part.

Finally, the proposed second-order right factor has the correct
Wronskian logarithmic derivative1+J'/J and annihilates both known
branches. Multiplying by the displayed first-order factor recovers the
top two coefficients of L/(zD). Their difference has order at most1;
the determinant J then forces its two coefficients to vanish. All
operations take place in the rational function field, where the
previously proved nonzero C,J may be inverted.

No new prime-depth bound follows from these identities: the two pole
resultants are already units wherever the full local accessory algebra
is nonzero. That algebra can retain vertical p-power thickness. The
source note correctly preserves this obstruction.
