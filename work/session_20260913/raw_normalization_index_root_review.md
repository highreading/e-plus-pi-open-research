> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent root review of the tangent and normalization-index note

Date: 2026-09-13. Verdict: PASS, with all conditional hypotheses retained.

Reviewed `raw_exponential_tangent_and_normalization_index.md` in full.

The actual tangent equations are correctly differentiated. The top B
coefficient is fixed, so its variation lies in degree at most d−1; the
upper pivots m−d prove uniqueness. The C forcing has degree at most d−1,
including the cancellation of a degree-d term when C has full degree.
The fixed nonzero cofactor coordinate makes the restriction of L an
isomorphism. Differentiating the normalized pole condition gives exactly
2 dot C'−S dot C−(uz+v)C modulo 1+z². Changing from the integral
cofactor residues to this chart scales their differentials by a unit at
the common zero. The full four-row transversality theorem proves only
injectivity of this residue map on E tangents. The note correctly does
not turn that injectivity into vanishing of the tangent space.

The added Jacobian ideal has scalar quotient of length
min(f,v_p(j_E)), independent of the chosen lift of j_E. This uses the
proved full quotient R/(p^f) and keeps the normalization of the integer
Jacobian. It is an exact restatement of the additional unit problem.

The Hermite-leading countermodel has the specified filtered basis and
rank. Its only geometric special-fiber point is the origin by the
unit-pivot Hermite recurrence. Both E gradients vanish there for d≥2,
whereas the coordinate residue rows have rank two and the full quotient
is R/(p^h). The proof of reduced generic fiber also checks: at gamma=0
the two coordinate derivatives are independent, while at gamma≠0 the
nonzero derivative of P_d and the weighted Euler direction separate the
two equations. This is a countermodel to deductions from the listed
structural hypotheses, not an actual-family defect.

For the new index theorem, completeness of Z_p permits the finite
algebra's decomposition into local factors. On a factor where the
residue ideal is the unit ideal, one of the residues is a unit, so its
norm pencil has a nonzero constant or leading coefficient modulo p.
Its Gauss valuation is zero, without needing that factor to be reduced.
Only the one relevant local factor requires the explicitly stated
reduced generic fiber hypothesis.

The integral closure of that factor is a product of local rings of
integers. Norms agree on the original order and its integral closure
because they are the same rational multiplication maps on different
lattices. For one field factor with residue degree f_nu and valuation
m_nu of the two-generated residue ideal, the norm-pencil Gauss
valuation is f_nu m_nu. This follows by multiplicativity over the
embeddings with their p-adic valuations; it equals the Z_p-length of
the quotient by that ideal, including ramification. Thus

    c=length(B_*/I B_*)

is exact. The cokernel of A_*/I→B_*/IB_* is B_*/(A_*+IB_*), a quotient
of B_*/A_*. Its length is at most delta_*, and the image length is at
most f. This proves c≤f+delta_* without assuming that the map is
injective. The separate primitive-evaluation-row argument proves c≥f;
the inclusion p^f∈I proves c≤r f. All three inequalities can therefore
be combined as stated.

The discriminant-index identity contributes exactly twice the lattice
index length. The maximal-order discriminant valuation is nonnegative,
so the displayed half-discriminant upper bound follows. It cannot be
used when the actual generic fiber has not been shown reduced or when
the discriminant is zero. The rank-two sharpness example has lattice
determinant −2p^h, scalar quotient R/(p^h), and norm
p^(2h)(t²−1), giving c=f+delta=2h at odd p exactly.

This supplies a valid alternative conditional route to exact norm
valuation under maximality, even allowing ramification. It does not
establish actual all-degree reducedness, maximality, small index, a
Jacobian unit theorem, or the missing content-height bound.
