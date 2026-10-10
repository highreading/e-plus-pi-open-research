> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Odd-degree extension and the genuine remaining Xi tie

Continuation status: the remaining tied class is now proved in
raw_Xi_remaining_class_mod_eight.md, with dedicated independent
review in raw_Xi_remaining_class_independent_review.md. The tie
and coefficient estimates below remain dependencies of that proof.

Date: 2026-09-13. Original continuation by audit_sources.

This supplement proves the penultimate-C valuation in all odd degrees
and proves Xi_n!=0 whenever n=3 modulo4. It leaves the products tied
in the class n=1 modulo4; no choice of one tied product as uniquely
least is made.

All coefficients use the actual canonical normalization
`B_n(1)=1`, `C_n(1)=4`. The reduced determinant convention and the
exact modified row for `h=a_(n-1)-c_n` are those in
`raw_leading_A_dyadic_and_Xi_gate.md` and `raw_Xi_even_dyadic.md`.

## 1. Penultimate C in every odd degree

Put n=2r+1. Delete the actual C_(n-1) coordinate column. Its remaining
even poles are `0,2,...,2r-2`, numbering r; its odd poles are
`1,3,...,2r+1`, numbering r+1. The C-border determinant has 2r
ordinary rows. The two admissible parity lower bounds are exactly

    K_A=3g(r)+beta(r+1),
    K_B=2g(r+1)+g(r-1)+beta(r),                       (1)

with the second orientation absent at r=0. Here

    g(j)=j(j-1)/2+S(j), S(j)=sum_(i=0)^(j-1)phi(i),
    beta(R)=g(R-1)+(R-1)+epsilon_(R-1),
    phi(i)=v_2(i!), epsilon_j=1 if j is odd, else 0.

The original parity calculation gives `K_B>=K_A` and
`K_A=L_(n-1)`, where `L_m=2S(m)+c_m^val` and
`c_m^val=2 floor((m+2)/4)`.

For the unique factorial-maximal exponential set `{2n,...,3n}`,
the complementary C rows are `{n+1,...,2n-1}`. Their even and odd
counts both equal r. Thus the square block uses the r even poles,
and the border goes to the r+1 odd poles. The latter's first row is
2r+2 and first pole is one, giving first difference 2r+1. Both row
sets are consecutive within parity. If the bordered size r+1 is
even, r is odd and the first difference is 3 modulo4, so the equality
criterion applies. Consequently this C minor attains L_(n-1).
At r=0 the C minor is the one-entry endpoint row and also attains
that bound.

All other exponential sets lose at least one in their factorial sum.
The other border assignment has gap at least

    2+n+2phi(n-1)-c_(n-1)^val>0                     (2)

above the attained value: its pure C columns have parity counts
r,r+1 and global valuation `2g(r)+2g(r+1)=2S(n)`. Hence the
coordinate determinant is nonzero and

    v_2(c_(n-1))=-n+L_(n-1)-L_n
                 =-n-2phi(n-1), n odd.               (3)

The last equality uses `c_(n-1)^val=c_n^val` for odd n. Combined
with the even-degree proof, (3) now holds for every n>=1.

## 2. The two needed leading-row parity estimates

For c_n, delete C_n rather than C_(n-1). The remaining C poles
number r+1 even and r odd. The top complementary rows again are
`{n+1,...,2n-1}`, with r of each parity. The square block uses the
odd poles, while the border goes to the r+1 even poles. Its first
ordinary row is 2r+3 and first pole is zero, so its first difference
is 2r+3. Its global lower bound is L_(n-1).

For h=a_(n-1)-c_n, use its exact modified coefficient row at
k=n-1, with `f_(-1)=0`, `t_(-1)=1`. The top complementary rows are
`{n-1} union {n+1,...,2n-1}`. Their even/odd counts are r+1,r;
both C pole sets have size r+1. The square block uses the odd poles
and the border goes to the even poles. Once again its first
row-to-pole difference is 2r+3. Its global lower bound is L_n.
The single negative odd denominator, if present, belongs to the
square block and does not change its valuation formula. Global
minor lower bounds for the modified row remain valid by the exact
signed Cauchy argument already given in the even-degree note.

If r is even, equivalently n=1 mod4, the bordered block in both
cases has an even number r of ordinary rows. The equality criterion
therefore applies. The top exponential set is uniquely least, giving

    v_2(c_n)=-n-2phi(n-1),
    v_2(h)=-n, n=1 mod4.                             (4)

These include n=1 with the empty ordinary-row convention.

If r is odd, equivalently n=3 mod4, the bordered size r+1 is even
but the first difference 2r+3 is 1 modulo4. The archived congruence
`F_r(2r+3)=2r+2 mod4=0 mod4` supplies at least one power beyond
the general bordered lower bound. Thus the top terms each gain at
least one. Every other exponential set also loses at least one,
since `v_2(2n)=1` for odd n. The other-border gaps, respectively
(2) and `2+n+2phi(n)-c_n^val`, are positive integers, so cannot
weaken these one-power bounds. Consequently

    v_2(c_n)>=-n-2phi(n-1)+1,
    v_2(h)>=-n+1, n=3 mod4.                          (5)

Both inequalities allow zero. The equality cases in (4) do not
assert an exact Xi valuation.

## 3. Xi nonvanishing for n=3 mod4

The leading-A theorem and (3) show that

    v_2(a_n c_(n-1))=-2n-2phi(n-1)

and that this product is nonzero. For n=3 mod4, (5) puts h c_n at
least two powers above it. Hence

    v_2(Xi_n)=-2n-2phi(n-1), n=3 mod4.              (6)

Since b_n is a dyadic unit in this class and `[z^3]Q_n=b_n Xi_n`,
Q_n has degree three at every such index. Together with the
independently reviewed even-degree theorem, this proves the cubic
degree condition for every n not congruent to one modulo4.

## 4. What the remaining tie actually says

For n=1 mod4, (3)–(4) give two nonzero products of exactly the same
valuation:

    v_2(a_n c_(n-1))=v_2(h c_n)=-2n-2phi(n-1).       (7)

Their difference has at least one further power, but could still
vanish. Both products must be compared as dyadic units to settle
Xi in this class. The all-index B-leading interpolation lemma has
not yet been transferred to this quadratic product comparison.

The isolated n=1 triple has

    A=7-(19/2)z, B=-7+8z,
    C=17/2-(9/2)z,

so Xi_1=-29 and the cubic condition holds there. This single exact
case is not a proof for the remaining n=1 mod4, n>=5.

The theorem supplies exact arithmetic nonvanishing and valuation
information. It does not provide quantitative real noncancellation,
accessory-root control, or a proof about e+pi.
