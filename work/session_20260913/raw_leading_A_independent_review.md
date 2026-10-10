> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the all-index leading-A valuation

Date: 2026-09-13. Reviewer: audit_results.
Source: raw_leading_A_dyadic_and_Xi_gate.md, Sections1–4.
Dependencies read directly: the original raw_arctan_bordered_rank_proof.md,
the actual coefficient reconstruction and integer-minor convention in
raw_homogeneous_ode_independent_review.md, and the established denominator
valuation. No new degree scan was made.

**Verdict:** the proof passes. For the actual normalization B(1)=1,
C(1)=4 it establishes v2(a_n)=-n for every n>=1. The distinct Xi gate
is correctly left open. No correction was needed.

## 1. Actual coefficient row and cancellation of row scales

The reconstruction identity is

    a_n=-sum_(j=0)^n b_j/(n-j)!-sum_(j=0)^n c_j t_(n-j).

Thus its appended row is precisely the negative ordinary Taylor row
at k=n. All original high rows at k=n+1,...,3n are scaled by k! in
the integer matrix. Dividing those same rows in both numerator and
denominator gives exactly

    a_n=D_A/D_B,

where D_A has ordinary coefficient rows n,...,3n and the endpoint
border. An extra n! appears only if the appended reconstruction row
is deliberately multiplied by n! to make the original integer minor
A_star. Then a_n=A_star/(n! Delta_B), and that additional factor
cancels on passage to D_A. The source makes this distinction correctly.

## 2. Why the new smallest row does not invalidate either Cauchy bound

Every selected row has k>=n and every arctangent column has 0<=j<=n.
The only possible zero difference is k=j=n. It has even difference,
so it belongs to a parity-zero block and its entry is exactly t_0=0.
Every nonzero, opposite-parity difference remains a positive odd
integer. Consequently the source does not need a negative moment
or an extension of the orthogonal moment functional.

For a pure-C block with m consecutive columns, the nonzero determinant
splits into square Cauchy blocks of sizes e=ceil(m/2), o=floor(m/2).
Each denominator is a dyadic unit. Its row Vandermonde valuation is
at least g(e) or g(o), and its consecutive pole Vandermonde valuation
is exactly the same quantity. Hence the total is at least

    2g(e)+2g(o)=2S(m).

I checked the equality g(e)+g(o)=S(m) separately in both parities,
using phi(2r)=phi(2r+1)=r+phi(r). Structural zero determinants satisfy
the same lower bound with infinite valuation.

For a bordered C block with n ordinary rows, the original archived
proof uses only row parity and distinctness, consecutive poles, and
odd nonzero differences. All remain valid after admitting k=n.
Its global lower bound is therefore still L_n=2S(n)+c_n^val,
c_n^val=2 floor((n+2)/4).

## 3. Exact equality for U_A and both parity orientations

For n=2r, U_A={2r,...,4r-1}. There are r even rows, making the
square odd-pole block; the r odd rows make the bordered even-pole
block of size r+1. The latter has first row-to-pole difference
2r+1. When r+1 is even, r is odd and this difference is3 modulo4,
exactly the additional equality condition in the archived lemma.

For n=2r+1, U_A={2r+1,...,4r+1}. Its r+1 odd rows make the square
even-pole block, and its r even rows make the bordered odd-pole
block of size r+1. The first difference is again2r+1, with the same
required residue when the bordered size is even. All parity row
sets are consecutive, so their Vandermonde lower bounds are attained.

The original formulas reduce to L_n in both cases: writing
delta_r=1 for odd r and0 for even r, the extra term is r+delta_r,
which equals2 floor((n+2)/4). At n=1 the bordered block has one
column and no ordinary rows; its determinant is1. Thus no smallest
index is omitted from the equality claim.

## 4. Unique least term and the competing border assignment

In the C-border assignment the n+1 exponential rows have a unique
maximum factorial valuation sum at S_A={2n,...,3n}. The strict
inequality phi(2n)>phi(2n-1) separates every included index from
every excluded index at the cutoff. Any different row set loses at
least one dyadic power, while no Vandermonde or C-minor valuation
can drop below its independently proved global lower bound.

At S_A the consecutive Vandermonde and the complementary U_A minor
both attain their bounds. Its valuation is exactly

    S(n+1)-H_n-phi(2n)+L_n
      =V_n+phi(n)-phi(2n)=V_n-n.

The other border assignment contributes the explicit -4 factor and
n ordinary exponential evaluation rows. The integral falling-factorial
functional therefore gives the bound2+S(n)-H_n. The complementary
pure C block has size n+1 and bound2S(n+1), established without any
negative-moment shortcut in Section2. Its gap above V_n-n is

    2+2phi(n)+n-c_n^val>0.

For example c_n^val<=(n+2)/2 makes the positivity immediate, including
n=1. This excludes cancellation with the unique minimal term.
Dividing by the actual denominator determinant of valuation V_n
therefore proves v2(a_n)=-n.

## 5. Independent smallest-index control and the Xi normalization

Solving the n=1 coefficient equations directly gives

    A(z)=7-(19/2)z,
    B(z)=-7+8z,
    C(z)=17/2-(9/2)z.

These satisfy B(1)=1, C(1)=4 and Taylor cancellation through degree3.
Their leading A coefficient has valuation-1, agreeing with the
all-index theorem. This is a separate hand-check, not evidence used
to infer the general valuation.

Finally the source defines

    H_minus=A_minus-(n-1)! C_star.

The identity

    Xi=[A_star C_minus-n H_minus C_star]/(n! Delta^2)

expands to the previously verified three-term numerator
A_star C_minus-n A_minus C_star+n!(C_star)^2. Both factorial scales
are correct. Nonzero a_n and b_n do not by themselves prevent
cancellation of this two-by-two Laurent determinant. The source's
remaining valuation comparison is a sufficient condition, not an
asserted result.
