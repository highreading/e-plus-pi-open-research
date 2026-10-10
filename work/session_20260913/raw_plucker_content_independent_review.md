> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the actual Plücker-content identity

Date: 2026-09-13. Reviewer: audit_results.

Reviewed Sections 4 and 5 of literature_hp_dvr_content_and_obstruction.md.
This is an independent algebraic review of the new actual-family
content identity and the separate formal-series counterexample. It
does not independently repeat the source retrieval in Sections 1--3.

**Verdict:** the content theorems and the arbitrary-depth example pass.
One displayed cross-product sign correction was communicated to the
author: the last two components of the ordinary cross product are
positive numerator polynomials, rather than negative ones. This has
no effect on any valuation or inequality in the note.
The author has applied this correction to both displayed identities
and their explanatory sentence.

## 1. Actual coefficient and polynomial content

Let K=[H_n;B(1);C(1)], E=det K, and let U,V be its last two
adjugate columns in that order. The identities KU=E e_(2n+1)
and KV=E e_(2n+2) have the claimed endpoint normalization.
Jacobi's identity for every two-coordinate minor of these columns
has exactly one factor E and the complementary maximal minor of
H_n. Every such maximal minor occurs. Hence

    cv_p(U wedge V)=v_p(E)+v_p(D_n).

The reconstruction of A uses Taylor coefficients only through n;
it is integral over Z_p for p>3n. Projection back to B,C is an
integral left inverse, including on the exterior squares. Thus
this reconstruction preserves the coefficient content exactly.
The subsequent map from coefficient exterior products to polynomial
cross products uses only integral additions and multiplications,
so it may increase content but cannot decrease it.

For the standard cross product of triples (A,B,C), direct substitution
of A=-Be-C atan+O(z^(3n+1)) gives

    S1-S0 e=O(z^(3n+1)),
    S2-S0 atan=O(z^(3n+1)).

Therefore the corrected exact cross product is

    (Qhat,+P_e,+P_atan)/Z_n.

This agrees with equations (19)--(21) of the independently reviewed
raw_extremal_dual_polynomial_and_content_identity.md. Since U,V
each have scale E, the polynomial cross product has scale E^2/Z_n.
Its Qhat component is p-primitive and all components are p-integral
before this common scale. Its exact content is consequently

    2v_p(E)-v_p(Z_n)=v_p(E)+v_p(F_n).

After division by the coordinate exterior content, the remaining
polynomial content is exactly v_p(F_n)-v_p(D_n), as claimed.
The distinction between independence of coefficient vectors and
polynomial dependence of their triples is essential and is kept.

## 2. The separate isolated-defect example

For delta=p^h and the author's different input

    g=e-1+delta z^2+2delta z^3+z^4+z^7 e^(2z),

the X_1 rows are exactly (1,1), (1,1+2delta),
(1,1+12delta). Their minors have gcd 2delta. The exponential
two-column H_1 minor is exactly one.

In the selected X_2 minor, subtracting the exponential columns
leaves, modulo p, the z^4 and z^5 columns. The top exponential
2-by-2 minor equals one, and the lower factorial diagonal gives
4!5!=2880. This is a unit for every prime p>6. Thus the valuations
h,0,0 for F_1,D_1,F_2 are correct for every positive h. The added
z^7 e^(2z) term does not enter any selected row, and all row-scaled
coefficients are integers.

This proves an obstruction to an input-independent depth theorem;
it does not produce an isolated defect for the actual arctangent
family. The note makes that distinction explicitly.
