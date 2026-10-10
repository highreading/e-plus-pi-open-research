> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root review of the eight-row-set Xi reduction

Date: 2026-09-13. Reviewed raw_Xi_eight_row_set_reduction.md. Result:
the finite reduction passes. The final quadratic residue is not proved.

The changed block has n+1 exponential columns and starts at2n. Its
integral cardinal interpolation identity is valid even at the last
possible replacement row n−1: the falling factorial in column n is
zero, exactly matching the inverse-factorial convention. The factorial
ratio is integral. Every row d>=3 contains both2(n−1) and2n, giving
the claimed a+2 powers independently of the cardinal weight.

I verified both cardinal-binomial factorizations for d1,d2 and the
uniform bounds for columns i>=4. The table for columns0,...,3 follows
from the four explicit factorial/binomial products and the exact
d2/d1 ratio. The upper-left double minor has term valuations4 and2,
so its valuation is exactly2. Each other two-column minor has the
stated lower bound, and every larger replacement uses a suppressed
row. Thus the list of eight potentially surviving sets is complete.

For transfer to the actual cofactors, the reduction uses the prior
independently reviewed signed Cauchy bounds L_n for A,H and L_(n−1)
for C,D, and their common endpoint normalization. The unchanged top
exponential block has the same factorial scale used for those known
baseline valuations. Suppression by a+2 therefore gives the displayed
four absolute coefficient error bounds. The extra H row, when in the
exponential assignment, is suppressed by its large replacement index;
when in the complementary block it uses the already verified signed
Cauchy argument. The separate endpoint assignment gaps exceed a+2.

Since each truncated coefficient differs only above its established
baseline, it retains that valuation. Expanding the two products then
gives v2(Xi−Xi8)>=−2n−2v2((n−1)!)+a+2. The final proposed residue
has the correct scaling, and the note correctly requires its earlier
layers to be checked before treating it as integral. No nonvanishing
conclusion for the remaining residue class follows from this reduction
alone.
