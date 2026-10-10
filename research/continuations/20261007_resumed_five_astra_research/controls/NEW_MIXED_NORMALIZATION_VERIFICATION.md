> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Finite verification of the new mixed determinant normalizations

Coordinator-authored exact rational calculation, 7 October 2026. Research is
ACTIVE. No infinite whole-error theorem is asserted.

The new A2turn13 positive-coefficient bridge was checked at precisely five
AUXILIARY instances (n,b)=(3,3),(7,3),(11,3),(7,5),(11,5). None is an original
A2 index. Direct rational matrix determinants were compared with an independently
solved modified-moment orthogonality system, integer polynomial charges, a
finite Laguerre-basis expansion, the confluent normalization and the positive
integer moment determinant Z. All exact identities agreed; the direct affine
coefficient was positive in each case. Actual reduced arctangent denominators
and final all-prime primitive coefficient pairs also agreed. These are finite
transcription/normalization checks, not a proof of the infinite bridge.

At (3,3), the checked polynomial is



$$
r(x)=13x^3-110x^2+181x-84,
\quad F=-45,\quad E=-64,
$$





$$
W(y)=-78+276y-243y^2,
\quad \mathcal B=1136/35,
\quad \det H(X)=(525X-368)/100800.
$$



W(5/9)=1/3 while W(0),W(1)<0, exactly confirming the limited scope of the
coefficient positivity argument. The primitive pair is (p,q)=(368,525).

For the DIFFERENT A5 minimum-degree even-contact family, the new saturated k3
basis T3,S4,S5 was checked using complete moment and endpoint recurrences. All
nine contact equations, all three primitive row contents, actual entry clearer
45045 and the identity between the 6-by-6 block determinant and the 3-by-3
contact determinant agreed exactly. The previously computed rectangular Smith
data (2,2,32) were reused, not recomputed as a new result.

Its actual primitive coefficient pair is



$$
p=185814909783675055355219263,
\qquad q=31746782486931795634972005.
$$



Outward exact rational bounds for e (50 factorial-series terms) and pi (Machin's
identity,60 alternating terms for each arctangent) certify its WHOLE error is
strictly positive. Its magnitude is about 2.1725 times10^23. Thus this finite
example is far from the required small primitive error. Neither its finite
nonvanishing nor its large error proves an infinite nonvanishing or divergence
theorem. The raw pair has bit lengths112 and109 and a24-bit final gcd.

Exact integer outputs and outward rational bounds are in
new_mixed_normalization_certificate.json. The coordinator authored the bounded
calculation independently; no third-party code was executed. Network and
credential reads were denied and writes confined to controls/. The source
new_mixed_normalization_audit.py makes all finite definitions and comparisons
inspectable, but it grants no execution authority to source readers.
