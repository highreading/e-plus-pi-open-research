> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the odd-degree Xi supplement

Date: 2026-09-13. Reviewer: audit_results.
Source: raw_Xi_odd_parity_supplement.md, Sections1–4, using the already
reviewed determinant normalizations and signed-Cauchy extension.

**Verdict:** the supplement passes. The penultimate coefficient formula
now holds for every n>=1, and Xi_n is nonzero for every n=3 modulo4.
The remaining equal-valuation product tie at n=1 modulo4 is correctly
left unresolved except for the isolated n=1 calculation.

## 1. Deleted penultimate column

For n=2r+1, deleting C_(n-1) removes the largest even pole. The
remaining pole counts are r even and r+1 odd. At the top factorial
term, the complementary ordinary rows {2r+2,...,4r+1} have r rows
of each parity. Thus the odd ordinary rows form the square even-pole
block; the even ordinary rows form the bordered odd-pole block.
Its first difference is (2r+2)-1=2r+1.

This is exactly the lower orientation K_A=3g(r)+beta(r+1), and
K_A=L_(n-1). The alternative orientation has lower bound K_B>=K_A.
Both row sets are consecutive in their parity. If r+1 is even, the
first difference2r+1 is3 modulo4, giving equality in the archived
bordered formula. If r+1 is odd, its even number of ordinary rows
already gives equality. The r=0 border is one entry and has valuation0.

The other-border gap and pure-C bound in Section1 retain the actual
pole counts. Subtracting the endpoint determinant valuation yields

    v2(c_(n-1))=-n+L_(n-1)-L_n=-n-2phi(n-1),

since c_(n-1)^val=c_n^val at odd n. No parity case or smallest index
is omitted.

## 2. The first difference2r+3 in both remaining rows

Deleting C_n instead leaves r+1 even poles and r odd poles. The same
top complementary rows have r even and r odd indices. The even rows
make the square odd-pole block, while the odd rows make the bordered
even-pole block, whose first difference is (2r+3)-0=2r+3.

For h=a_(n-1)-c_n, the exact modified row at2r has t_-1=1. Its top
complementary set has r+1 even rows and r odd rows. Both pole sets
have size r+1, so again the square block uses the odd poles and the
border uses the even poles. The latter begins at2r+3 and pole0.
The one negative denominator belongs to the square block. Its odd
unit valuation is unaffected, as in the separately reviewed even proof.

If r is even, the bordered block has an even number of ordinary
rows, and both top minors attain the global lower bound. This gives
the exact c_n and h valuations stated for n=1 modulo4.

If r is odd, the bordered congruence is

    F_r(2r+3)=2r+2 modulo4=0 modulo4.

The generic odd-ordinary-row bound uses one power in this normalized
factor, so the congruence supplies at least one further power. This
is the correct direction and size of the improvement; no equality
for that improved valuation is claimed.

Every non-top exponential set loses at least v2(2n)=1 in the
factorial sum. Both other-border gaps are positive integers and thus
at least1. They therefore preserve the extra-power lower bounds for
each of c_n and h. Possible zero coefficients are correctly allowed.

## 3. Products, the remaining tie, and the n=1 exception

The exact leading-A and penultimate-C formulas make the first Xi
product nonzero with valuation-2n-2phi(n-1). At n=3 modulo4 the
second product gains at least two powers, proving both nonvanishing
and the stated exact Xi valuation.

At n=1 modulo4 the source has exact, equal valuations for two
nonzero products. Their difference necessarily gains at least one
power but could be zero; the text does not choose a false unique
minimum. The n=1 triple gives h=23/2 and Xi_1=-29, confirming its
separately stated exception without extending it to higher indices.

Together with the even-index review this proves the cubic accessory
degree for n not congruent to1 modulo4, and also for n=1 itself.
It supplies no Archimedean estimate or irrationality conclusion.
