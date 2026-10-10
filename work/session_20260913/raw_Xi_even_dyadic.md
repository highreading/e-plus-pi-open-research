> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The infinity cross-minor is nonzero in every even degree

Date: 2026-09-13. Original dyadic continuation by audit_sources.

This note proves, for the actual raw canonical triple normalized by
`B_n(1)=1`, `C_n(1)=4`, that

    Xi_n=a_n c_(n-1)-(a_(n-1)-c_n)c_n != 0

for every even n>=2. Consequently the accessory polynomial Q_n has
degree three at every even index. Odd-index Xi nonvanishing and all
Archimedean asymptotics remain separate questions.

## 1. Inputs and exact theorem

Write `phi(j)=v_2(j!)` and `v=v_2(n)`. The established coefficient
lemmas give

    v_2(b_n)=0,
    v_2(a_n)=-n,
    v_2(c_(n-1))=-n-2phi(n-1)                       (1)

for every even n>=2. Their proofs are respectively
`raw_leading_B_dyadic_all_indices.md`,
`raw_leading_A_dyadic_and_Xi_gate.md`, and
`raw_penultimate_C_even_dyadic.md`.

The theorem proved here is the exact valuation

    v_2(Xi_n)=-2n-2phi(n-1)             if n=0 mod4,
    v_2(Xi_n)=-2n-2phi(n-1)-2           if n=2 mod4.  (2)

The two residue classes have different uniquely least products;
assuming that the same product dominates in both would be incorrect.

Retain the reduced endpoint determinant valuation

    V_n=S(n)-H_n+L_n,
    S(m)=sum_(j=0)^(m-1)phi(j),
    H_n=sum_(k=2n+1)^(3n)phi(k),
    L_n=2S(n)+c_n^val,
    c_n^val=2 floor((n+2)/4).                        (3)

## 2. The leading C coefficient: a bound and one equality class

Append the coordinate row selecting c_n to the original bordered
high-jet matrix, then delete that coordinate column. Its reduced
determinant has exponential columns B_0,...,B_n and C columns
C_0,...,C_(n-1). The C-border block has n-1 ordinary rows, so the
original global bound is L_(n-1).

The unique factorial-maximal set of n+1 exponential rows is
`{2n,...,3n}`. Its complementary C rows are `{n+1,...,2n-1}`.
Writing n=2r, the C-pole sets both have size r. The odd ordinary rows
make the square even-pole block, and the even ordinary rows make the
bordered odd-pole block of size r. Its first row-to-pole difference
is 2r+1. If n=2 mod4, then r is odd and the bordered block has an
even number r-1 of ordinary rows, so the exact even-index equality
case in the archived Cauchy formula applies. Thus the top C minor
attains L_(n-1) in that class. In the other class retain only the
global lower bound; no equality is asserted.

The border assigned to the exponential block has gap at least

    2+n+2phi(n-1)-c_(n-1)^val>0                     (4)

above the top-term lower bound. This follows from the -4 Lambda
alternant and the pure C bound `2S(n)` in exactly the actual column
normalization. Every other C-border term has a strictly smaller
factorial sum. Therefore

    v_2(c_n)>=-n+L_(n-1)-L_n
             =-n-2phi(n-1)-2*1_(n=2 mod4),          (5)

and equality holds in (5) whenever n=2 mod4. Zero c_n is allowed by
the inequality in the class divisible by four.

## 3. The cancellation-adapted H coefficient is an exact modified row

Set `h=a_(n-1)-c_n`. The appended reconstruction row for h is the
negative of the coefficient-style row at k=n-1, provided that

    f_(-1)=0,
    t_(-1)=1.                                       (6)

This is an exact algebraic statement about that appended row. The
first convention agrees with the falling-factorial value, since
`(n-1)_(underline n)=0`. The ordinary reconstruction of a_(n-1)
has no c_n term; assigning t_(-1)=1 puts exactly the additional -c_n
into the negative row. This is not a claim that arctangent has a
negative Taylor coefficient.

For k-j=-1, the same algebraic formula
`t_s=(-1)^((s-1)/2)/s` for odd s gives the value one. The parity
sign transformations in the Cauchy proof therefore still hold.
There is one possible negative denominator -1; all nonzero
denominators remain odd and nonzero. The valuation proof for square
and bordered Cauchy blocks uses odd products, integer Vandermondes,
and the parity congruence for the signed product sum. It does not
require those products to be positive. Hence its global lower
bounds L_n and `2S(n+1)` continue to hold for this modified row.
This direct Cauchy argument avoids inventing a positive measure or
unjustified negative-moment extension.

After inserting this row and reordering, the ordinary row indices
are

    {n-1} union {n+1,n+2,...,3n}.                    (7)

The unique factorial-maximal n+1 exponential set is again
`{2n,...,3n}`. Its complementary C rows are

    U_h={n-1} union {n+1,...,2n-1}.                  (8)

Every other set loses at least `phi(2n)-phi(2n-1)=v+1` in the
factorial sum: all added rows are at most 2n-1, while every deleted
row is at least 2n. All Vandermondes retain their global bound.

## 4. Its exact parity orientation yields the needed H estimates

With n=2r, the C columns C_0,...,C_n have r odd and r+1 even poles.
The rows U_h have r-1 even rows and r+1 odd rows. Thus the square
block is the even-pole block of size r+1; the bordered odd-pole
block has size r and r-1 ordinary rows. This is the original rank
proof's second orientation. Its lower bound L_B satisfies

    L_B-L_n=0                         if r odd,
    L_B-L_n=2+2v_2(r)=2v              if r even.      (9)

The rows in each parity block are consecutive. The bordered block
starts at even row 2r+2 and odd pole one, so its first difference is
2r+1. If r is odd, its r-1 ordinary rows have even cardinality and
the equality criterion applies. Thus the U_h minor attains L_n for
n=2 mod4. In that class the corresponding exponential top term is
uniquely least, and

    v_2(h)=-n, n=2 mod4.                             (10)

If r is even, the top term is at least 2v powers above the generic
baseline V_n-n. Every other C-border term is at least v+1 powers
above it by (8). As v>=2 in this class, `min(2v,v+1)=v+1`.

The other border assignment has gap at least

    G_n=2+n+2phi(n)-c_n^val                           (11)

above V_n-n. It is at least v+1 for n divisible by four: using
`c_n^val<=(n+2)/2` gives `G_n>=1+n/2`, and `n/2>=v` for n>=4.
Consequently it does not weaken the bound, and

    v_2(h)>=-n+v+1, n=0 mod4.                       (12)

The estimate includes h=0. For n=2 mod4, G_n is positive, as needed
for the unique-minimum claim in (10). No estimate for h was obtained
by subtracting separate valuations of a_(n-1) and c_n.

## 5. Unique product comparisons and the cubic accessory gate

By (1), the first product is always nonzero in even degree and has

    v_2(a_n c_(n-1))=-2n-2phi(n-1).                 (13)

If n is divisible by four, (5) and (12) give

    v_2(h c_n)>=-2n-2phi(n-1)+v+1,

strictly above (13). Thus the first product uniquely controls Xi_n.

If n=2 mod4, the equalities (5) and (10) instead give

    v_2(h c_n)=-2n-2phi(n-1)-2,

exactly two powers below (13). Thus the second product uniquely
controls Xi_n. Both cases prove (2).

The already proved exact identity is `[z^3]Q_n=b_n Xi_n`. The
normalization factors are respectively one and two powers of the
canonical endpoint determinant, as recorded in
`raw_homogeneous_ode_independent_review.md` and
`raw_leading_A_dyadic_and_Xi_gate.md`. Because b_n is a dyadic unit
in even degree, (2) also gives the valuation of the cubic coefficient
and proves its nonvanishing. Therefore `deg Q_n=3` at every even
index n>=2.

This establishes the hypothesis needed for the cubic-stratum
integral transfer at each such current index; it does not assert
that all odd-index transfers also meet that hypothesis. There is no
Archimedean bound, accessory-root estimate, remainder asymptotic, or
main irrationality conclusion in this theorem.
