> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Automatic factorial content of the growing high-row minors

## Status correction: current bound obstruction

The earlier strict content-rate target is now marked unattainable by the main-agent deduction in GROWING_BOUND_OBSTRUCTION_DRAFT.md, pending independent audit. The original argument below is preserved for provenance. Exact normalization and divisibility claims must be reviewed separately from that target.

Status: main-agent paper draft, awaiting independent review. This is a lower bound for a specified common content, not an irrationality proof.

Use the monic cofactor normalization and endpoint clearer in GROWING_CONTENT_CRITERION_DRAFT.md. Let 1<=b<=n and let the integer high block have rows l=1,...,b-1 and columns j=0,...,b:

    R_lj=E_(n+l,l+j-1),
    E_(k,r)=(d/dx)^r[x^k H_k(x)] at x=1.

The established integrality H_k in Z[x] implies r! divides E_(k,r): each derivative of a monomial has coefficient r! times an integer binomial coefficient. Therefore

    R_lj=(l-1)! j! Z_lj,
    Z_lj in Z,

because (l+j-1)!/((l-1)!j!) is an integer.

Define

    A_b=product_(j=0)^(b-2) j!,

with A_1=1. Every maximal minor of R contains the row factor A_b. Its selected b-1 column indices can be ordered j_1<...<j_(b-1), with j_s>=s-1. Thus product_s j_s! is divisible by A_b. Consequently

    A_b^2 divides every maximal minor of R.

This holds even when some minors vanish. If the high block has full row rank, its positive maximal-minor content is therefore divisible by A_b^2. In Agent 1's notation this content is Crows*mu, before the further three-contraction content d is removed.

## Connection to the endpoint content

Put F=(2n+1)!, rho_plus=product_(l=1)^(b-1)(2n+2l)!, and

    M=2^(2n+3) F^2 rho_plus.

Let g=gcd(|MX|,|MY|) on Y!=0, in exactly the original monic cofactor scale. The endpoint-clearer argument in GROWING_CONTENT_CRITERION_DRAFT.md needs to be independently checked before the following connection is accepted.

Expansion along the last two rows writes every endpoint determinant as a linear combination of the maximal minors of R. Divide all those minors by A_b^2. The resulting alternating bilinear form has integer coefficients. The same endpoint formulas and clearing proof therefore apply after this division: every partial-exponential row is cleared by F, and (n+1)F clears both second-kind values. This would prove

    MX/A_b^2 in Z, MY/A_b^2 in Z,
    A_b^2 divides g.

No division by a residue-class parameter is involved. No row factor is counted twice: A_b^2 is a divisor of the complete high-minor content, not a factor to add to that content separately.

## Scale and remaining target

For b=floor(n/2), elementary factorial summation gives

    log(A_b^2)=n^2 log(n)/4+O(n^2).

If the separately audited sufficient threshold log g/(n^2 log n)>3/4 is correct, this automatic contribution leaves the sufficient residual target

    liminf log(g/A_b^2)/(n^2 log n)>1/2

on the same unbounded index set, together with nonzero endpoint and nonzero full remainder. This is a sufficient target, not a necessary condition for every possible successful estimate.

Neither the residual content estimate nor growing-degree nonvanishing is proved here. The review should check the exact endpoint scale, divisibility after clearing, empty-block conventions, and compatibility with Agent 1's row/minor/contraction contents.
