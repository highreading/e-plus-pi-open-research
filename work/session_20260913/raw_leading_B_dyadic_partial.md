> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Leading B coefficient: three parity classes proved, one genuine tie

Continuation status: the remaining class has subsequently been proved
in `raw_leading_B_dyadic_all_indices.md`, with independent review in
`raw_leading_B_all_indices_independent_review.md`. The partial argument
below is retained as a dependency and record of the actual tie.

Date: 2026-09-13. Original dyadic continuation. This note proves that
the actual normalized leading coefficient b_n is a 2-adic unit when
n is even or n=3 modulo 4. It isolates the unresolved class n=1 modulo
4 without importing an endpoint determinant valuation for a different
appended row.

## 1. Actual determinant convention and result

Use the canonical raw triple of degrees at most n, with
B(1)=1 and C(1)=4. Let J_n be the integer high-jet matrix, including
its row C(1)-4B(1), with columns b_0,...,b_n,c_0,...,c_n. Put

    Delta_B=det[J_n; row B(1)],
    B_star=det[J_n; row b_n].

The existing cofactor identity is b_n=B_star/Delta_B, and the proved
rank theorem gives Delta_B!=0. Define

    phi(k)=v_2(k!), S(n)=sum_(j=0)^(n-1) phi(j),
    c_n=2 floor((n+2)/4), L_n=2S(n)+c_n.

**Theorem.** For every n>=1 with n even or n=3 modulo 4,

    v_2(B_star)=sum_(k=n+1)^(2n)phi(k)+S(n)+L_n
               =v_2(Delta_B),
    v_2(b_n)=0.                                       (1)

In particular B has degree exactly n in these three residue classes.
For n=1 modulo 4 the proof instead gives the unconditional divisibility
b_n in 2 Z_(2), allowing b_n=0. At n=1 the exact triple has
B(z)=-7+8z, so b_1=8 is nonzero. Nonvanishing in the remaining
indices n>=5, n=1 modulo 4 is not proved here.

## 2. The changed appended row and the reduced matrix

Divide each high row k by k!, and expand the appended coordinate row
b_n. Up to a global sign the remaining square determinant D_n has
2n high rows k=n+1,...,3n and one final border. Its columns are

    B_0,...,B_(n-1) | C_0,...,C_n,

and its entries are

    (1/(k-j)! | t_(k-j)),
    border=(-4,...,-4 | 1,...,1),                     (2)

where t_a=(-1)^((a-1)/2)/a for positive odd a and zero otherwise.
Thus exactly

    v_2(B_star)=sum_(k=n+1)^(3n)phi(k)+v_2(D_n).        (3)

There is no extra n! factor: the appended row extracts b_n itself.
This differs from both of the old endpoint rows.

Expand D_n along its n exponential columns. There are two assignments:
the border is either in the arctangent block or in the exponential
block. The latter carries the factor -4.

## 3. The arctangent minor is the previously audited bordered block

When the border is assigned to the arctangent block, that block has
n high rows U and the n+1 columns C_0,...,C_n. Its determinant is,
up to sign, exactly

    det[(t_(k-j))_(k in U,0<=j<=n); (1,...,1)].

The incidence-column identity (11a) in
`sources/raw_arctan_bordered_rank_proof.md` identifies this with the
size-n arctangent difference minor in that proof, with its parameter
ell=n. Therefore its all-row-set lower bound L_n applies without
modification. The exponential minor in the present problem is
different and will be treated separately.

Write n=2r+1 when n is odd and R=r+1. For the two particular
complementary high sets needed below, the bordered-Cauchy equality
and parity checks are as follows.

    U_0={n+1,...,2n},
    U_*={n+1,...,2n-1} union {2n+1}.

For even n, the U_0 minor attains L_n, as in the archived parity
calculation. For odd n, the U_* minor attains L_n.

For odd n, the U_0 minor has a square odd-pole block and a bordered
even-pole block of size R. The r ordinary rows of the latter are
2r+3,2r+5,...,4r+1 and its poles start at zero. Consequently the
first row-to-pole difference in the archived formula is a=2r+3.
That formula uses the integer polynomial

    F_r(a)=2^(-r) sum_(h=0)^r binom(r,h)
                   product_(i=0)^(r-1)(a+2i-2h),

with the proved congruences F_(2s)(a)=1 mod4 and
F_(2s+1)(a)=a-1 mod4 for odd a.

If n=3 mod4, then r is odd and a=1 mod4, so the bordered block
has at least one more power of two than its global lower bound.
The U_0 minor therefore has valuation at least L_n+1. If n=1 mod4,
r is even and F_r(a) is odd, so the U_0 minor attains L_n exactly.

For U_*, the bordered block instead uses first difference a=2r+1.
When r is odd this is 3 mod4 and the bound is exact; when r is even
the same even-index unit congruence applies. This confirms equality
for U_* in both odd classes, including the empty-row convention at
n=1.

## 4. Exponential minors with the border assigned to C

For a set S of n high rows, the exponential block has columns
(k)_j/k!, j=0,...,n-1. Its determinant is the ordinary alternant

    det P_S=V(S)/product_(k in S) k!,
    v_2(det P_S)>=S(n)-sum_(k in S)phi(k).              (4)

There is no Lambda factor in (4), unlike the archived rank proof's
exponential difference columns.

Let

    H_n=sum_(k=2n+1)^(3n)phi(k),
    V_n=S(n)-H_n+L_n.

The maximum factorial sum is H_n, attained only by

    S_0={2n+1,...,3n},
    S_*={2n} union {2n+2,...,3n}.                      (5)

Indeed phi(2n)=phi(2n+1), while phi(2n)>phi(2n-1).
Every other set loses at least one. The exact Vandermonde comparison is

    v_2(V(S_0))=S(n),
    v_2(V(S_*))=S(n)+v_2(n).                          (6)

For even n, S_0 attains V_n; S_* pays the strictly positive cost
v_2(n), and every other set pays a factorial-sum cost. Thus S_0 is
the unique least term within this border assignment.

For n=3 mod4, n is odd, so S_* has no extra Vandermonde cost. Its
complement U_* attains L_n. The S_0 complement U_0 instead pays
the extra power proved in Section 3. Again S_* is the unique least
term, of valuation V_n.

For n=1 mod4, both S_0 and S_* have valuation exactly V_n, and every
other term in this assignment has valuation at least V_n+1. This is
a real two-term tie, not an omitted factorial factor.

## 5. The other border assignment has a strict gap

Suppose the border is assigned to the exponential block. There are
n-1 ordinary high rows and the row -4 Lambda, where
Lambda((x)_j)=1 for j=0,...,n-1. The integral alternant identity gives
the valuation lower bound

    2+S(n-1)-H_(n-1),

where H_(n-1) is the sum of factorial valuations of the largest n-1
high indices. The remaining arctangent block consists of n+1 pure
moment rows, whose valuation is at least 2S(n+1), by the monic
dyadically integral orthogonal-basis lemma.

Its total lower bound minus V_n is therefore

    2+n+2phi(n)+v_2(n)-c_n > 0.                       (7)

Here H_n-H_(n-1)=phi(2n+1)=phi(n)+n and
phi(n)-phi(n-1)=v_2(n). Positivity follows, for example, from
c_n<= (n+2)/2. These inequalities include zero minors and possible
cancellation inside Lambda.

Thus the factor -4 assignment cannot cancel the unique minimum
in either of the classes proved in Section 4.

## 6. Integer valuation and the unresolved quarter class

For n even or n=3 mod4, the full Laplace expansion has a unique
least term of valuation V_n. Hence D_n is nonzero and

    v_2(D_n)=S(n)-H_n+L_n.

Combining this with (3) gives (1). Comparing with the old Delta_B
valuation is legitimate only at this final step: both valuations have
now been proved for their respective actual appended rows.

For n=1 mod4, the two least summands each have an odd unit after
division by 2^V_n. Their sum is therefore divisible by a further
factor two. All other terms already have that divisibility, by
Sections 4–5. Thus v_2(D_n)>=V_n+1, allowing infinity, which gives
b_n in 2 Z_(2). This says nothing about nonvanishing.

One must analyze the sum of the two tied terms together with all
subsequent valuation layers, or find a different determinant argument,
to complete that class. Merely choosing either of the two maximal
factorial row sets as the unique minimum would be incorrect. Nor can
the independent nonzero endpoint Delta_B be substituted for B_star.

At n=1 the entire C-border part of D_n cancels exactly; the -4
assignment is nonzero and gives b_1=8. This example shows why a proof
must retain both border assignments even though one has a large gap
in the three classes already settled.

### Exact sum of the tied pair

The two tied summands can themselves be evaluated more sharply. Write
q_j=Q_j(1) for the raw monic Legendre polynomial in the dyadic moment
lemma, and beta_j=j^2/(4j^2-1), so q_(j+1)=q_j+beta_j q_(j-1).
These q_j are positive rational numbers, independently of any claim
about the HP leading coefficient.

After reversing the C columns, the U_0 bordered moment determinant is

    product_(j=0)^(n-1) h_j * q_n,

up to the common reversal sign. The U_* rows have moment degrees
0,...,n-2,n. In the monic orthogonal basis their final two-by-two
block is [[0,h_n],[q_(n-1),q_n]], since
L(t^n Q_(n-1))=0 by parity. Consequently

    C_(U_*)/C_(U_0)=beta_n q_(n-1)/q_n.

The exponential determinant ratio is n(2n+1), while the Laplace signs
are opposite. If T_0,T_* denote the full signed summands, this proves
the exact identity

    T_0+T_*=T_0 *
       [(2n-1)q_n-n^3q_(n-1)]/[(2n-1)q_n].            (8)

Now let n=4s+1>=5 and a=v_2(n-1)>=2. The even-index equality case
in Section 3 and the same moment determinant formula give

    v_2(q_(n-1))=2s,
    v_2(q_(n-2))>=2s+1.

The second inequality uses the already checked extra bordered-Cauchy
power for the index n-2=3 mod4. Thus q_n=q_(n-1)+beta_(n-1)q_(n-2)
has valuation 2s. Moreover

    (2n-1)q_n-n^3q_(n-1)
      =-(n-1)(n^2+n-1)q_(n-1)
        +(2n-1)beta_(n-1)q_(n-2).                    (9)

The first term has valuation a+2s, while the second has valuation
at least 2a+2s+1. The first is uniquely least. Since T_0 has valuation
V_n, equations (8)–(9) prove

    v_2(T_0+T_*)=V_n+v_2(n-1)
                       (n>=5, n=1 mod4).            (10)

At n=1 the numerator in (8) is exactly zero, consistent with the
direct calculation. Formula (10) is a sharper pair lemma, not a
valuation formula for the whole determinant: the current bounds for
all other C-border terms give only V_n+1. They must be controlled
through the deeper layer V_n+v_2(n-1), and possible cancellation there
must be settled, before (10) can prove nonvanishing in this class.

## 7. Scope

This is an all-index exact nonvanishing theorem for three residue
classes, and a precise obstruction in the remaining class. It proves
neither a nonzero infinity cross-minor Xi_n nor cubic accessory degree
by itself. It supplies no real absolute-value lower bound for b_n,
no endpoint noncancellation angle, and no shrinking primitive forms.

Selected independent determinant controls use only the already studied
degrees 1,2,3,4,5,8. They track the C-border and -4B-border contributions
separately, the two distinguished Laplace terms, the integer factorial
restoration, and agreement with available stored polynomial inputs.
The controls are not used to infer the all-index valuation theorem.
They are saved in `check_raw_leading_B_dyadic.py` and
`raw_leading_B_dyadic_checks.json`. The normalized b_n valuations at
these six degrees are respectively 3,0,0,0,2,0. In particular the n=5
pair sum and full determinant both lie two powers above the baseline;
this finite coincidence is not promoted to all n=1 mod4.
