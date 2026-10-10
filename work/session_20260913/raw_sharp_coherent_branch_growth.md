> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Sharp exponential growth of both coherent branch directions

Date: 2026-09-13. Root combination of two independently reviewed
theorems. This is an all-index quantitative result for adjacent
branch matrices at one growing spectral parameter.

Let P_N(x) be the two-by-two matrix of actual symmetric-normalized
branch rows R_N(x),R_(N+1)(x). For c in any compact interval
[c0,c1] contained in (0,infinity), define

    F(c)=asinh(sqrt(c))+sqrt(c)asinh(1/sqrt(c)).

Then both singular values have the same uniform exponential rate:

    log sigma_i(P_N(cN^2))=N F(c)+o(N), i=1,2.     (1)

More precisely, the already proved polynomial condition-number
bound gives the exact comparison

    log sigma_i(P_N(cN^2))
      = (1/2)log|det P_N(cN^2)|+O(log N),         (2)

with uniform constants on the c-interval. Thus (1) controls
every direction in the actual two-dimensional branch space:

    exp(N F(c)-o(N))||v||
       <=||P_N(cN^2)v||
       <=exp(N F(c)+o(N))||v||                   (3)

uniformly in c and in all vectors v. The o(N) in these formulas
is a uniform deterministic error, not an assumed asymptotic
expansion of an individual polynomial coefficient.

Proof. The independently reviewed result
`raw_global_adjacent_branch_conditioning.md` gives
cond P_N<=C N^A. If sigma1>=sigma2>0, then

    sigma1*sigma2=|det P_N|,
    0<=log(sigma1/sigma2)<=log C+A log N.

Adding and subtracting these two equalities/inequalities proves
(2). The independently reviewed trace calculation in
`raw_row_spectral_density_and_determinant_rate.md` gives

    log|det P_N(cN^2)|=2N F(c)+o(N)

uniformly on the same interval. Combining proves (1), and the
definition of the extreme singular values gives (3).

The relation to the rational branch matrix is a diagonal row
factor and a fixed diagonal channel factor. Its two row factors
are sqrt(2N+1),sqrt(2N+3), so it changes logarithmic singular
values by only O(log N). The same exponential rate therefore
holds in rational normalization. Inserting the actual spectral
amplitudes g_l is a different operation and must still retain
their separately proved factorial scale.

This theorem improves the previous unspecific exp(O(N)) upper
and lower bounds to an explicit common rate in both directions.
It does not say that P_N is diagonal or that its normalized
entries converge. It also does not lower-bound a determinant
formed from different spectral parameters after prescribed row
deletions. The exact high matrix still contains the separate
remainder factor A_rem, and the primitive endpoint arithmetic
still requires a height or common-factor estimate.

Verification dependencies:
`raw_global_branch_conditioning_independent_review.md` and
`raw_row_spectral_density_independent_review.md`. No additional
numerical computation or unreviewed asymptotic input is needed
for the combination above.
