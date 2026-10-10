> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The remaining leading-B determinant: the class n=5 modulo 8

Continuation status: the all-index interpolation theorem in
`raw_leading_B_dyadic_all_indices.md` now resolves the other residue
classes as well. This proof and its two exact bordered-moment ratios
remain valid dependencies of that theorem.

Date: 2026-09-13. Exact continuation by audit_sources. This note uses the
actual determinant convention and the already independently reviewed
lemmas in `raw_leading_B_dyadic_partial.md`. It resolves the next
valuation layer for every `n=5 mod 8`; there is no degree scan in the
proof.

## 1. Result and inherited notation

Let `b_n=B_{n,n}` be the leading coefficient in the canonical raw triple
normalized by `B_n(1)=1` and `C_n(1)=4`. Retain

    phi(k)=v_2(k!), S(n)=sum_(j=0)^(n-1) phi(j),
    L_n=2S(n)+2 floor((n+2)/4),
    H_n=sum_(k=2n+1)^(3n) phi(k),
    V_n=S(n)-H_n+L_n.

Let `D_n` be the reduced determinant of Section 2 of the preceding
note. In its Laplace expansion along the n exponential columns, a
C-border term uses n high rows `S`, and its complementary arctangent
minor uses the remaining high rows and the endpoint row.

**Theorem.** For every integer `n>=5` with `n=5 mod 8`,

    v_2(D_n)=V_n+2,
    v_2(B_star)=v_2(Delta_B)+2,
    v_2(b_n)=2.                                      (1)

In particular, `B_n` has degree exactly n in this class. Combined with
the preceding note, this proves exact degree n for all n except
possibly `n=1 mod 8`, `n>=9`; n=1 is separately known and has `b_1=8`.
This is an exact nonvanishing statement, not an Archimedean lower
bound or a proof of the cubic accessory condition.

## 2. Complete list of factorial losses at most two

Set `h=2n` and `F=phi(h)`. Because `n=5 mod 8`,

    phi(h-2)=phi(h-1)=F-1,
    phi(h)=phi(h+1)=F,
    phi(h+2)=phi(h+3)=F+2,
    phi(h+4)=F+3,
    phi(h-3)<=F-4.                                   (2)

The last inequality follows from `v_2(h-2)>=3`; monotonicity handles
all still smaller indices. Let `S_0={h+1,...,3n}`. Every size-n set S
is obtained by deleting a set from `S_0` and adding an equally sized
set of indices at most h. Write its factorial loss as

    ell(S)=H_n-sum_(k in S)phi(k)>=0.

If at least two indices are exchanged, the sum of the two cheapest
deletions is `2F+2`, while the sum of the two most expensive additions
is `2F-1`. Each further deletion/addition pair has nonnegative loss.
Thus every multiple exchange has loss at least three. A single
exchange involving a deleted index at least `h+4`, or an added index
at most `h-3`, also has loss at least three. Therefore the complete
list with loss at most two is

| Set | Change from S_0 | Factorial loss |
|---|---|---:|
| S_0 | none | 0 |
| S_* | replace h+1 by h | 0 |
| S_A | replace h+1 by h-1 | 1 |
| S_B | replace h+1 by h-2 | 1 |
| S_C | replace h+2 by h | 2 |
| S_D | replace h+3 by h | 2 |

There is no omitted low-loss set in this list.

## 3. Exact Vandermonde costs

The exponential minor is `Vand(S)/prod_(k in S) k!`. Relative to
the consecutive Vandermonde for `S_0`, the positive absolute ratios
for the five changed sets are

    S_*: n,
    S_A: n(n+1)/2,
    S_B: n(n+1)(n+2)/6,
    S_C: n(n-1)/2,
    S_D: n(n-1)(n-2)/6.                              (3)

Each follows by cancelling the unchanged pairwise differences.
Since `v_2(n-1)=2`, `v_2(n+1)=1`, and n and n+/-2 are odd, their
valuation costs are respectively `0,0,0,1,1`. Consequently S_C and
S_D contribute at least `V_n+3` using the general C-minor bound
`v_2(C_U)>=L_n`. Every unlisted set also contributes at least
`V_n+3` by its factorial loss and the global Vandermonde bound.

The only additional terms that can interact with the distinguished
pair through `V_n+2` are therefore S_A and S_B. We now determine
their C-minor valuations, rather than assuming that the global bound
is attained.

## 4. Two exact bordered-moment ratios

Reverse the C columns. Its entries are then moments
`mu_(d+j)=t_(d+j+1)`, where the moment degree of high row k is
`d=k-n-1`. Use the monic orthogonal polynomials Q_j for this moment
functional, and write

    q_j=Q_j(1), beta_j=j^2/(4j^2-1),
    h_j=L(Q_j^2), h_j/h_(j-1)=-beta_j,
    Q_(j+1)=t Q_j+beta_j Q_(j-1).

Their parity and monicity imply

    L(t^j Q_j)=h_j,
    L(t^(j+1) Q_j)=0,
    L(t^(j+2) Q_j)=-s_(j+2) h_j,
    s_k=sum_(i=1)^(k-1) beta_i=k(k-1)/(2(2k-1)).     (4)

The last equality follows by telescoping
`beta_i=1/4+1/[4(4i^2-1)]`. Column changes from monomials to Q_j are
unit triangular and preserve every bordered determinant. The common
column-reversal sign cancels in ratios.

The complement U_0 of S_0 has moment degrees `0,...,n-1`; its
bordered determinant is

    C_0=(prod_(j=0)^(n-1) h_j) q_n.                  (5)

The complement of S_A has moment degrees
`0,...,n-3,n-1,n`. Eliminating the first n-2 orthogonal columns leaves
the rows n-1, n and the endpoint, on columns n-2,n-1,n. By (4) its
three-by-three matrix is

    [ 0                 h_(n-1)       0   ]
    [ -s_n h_(n-2)      0             h_n ]
    [ q_(n-2)           q_(n-1)        q_n ].

Taking its determinant and dividing by (5) gives exactly

    C_A/C_0=s_n+beta_n beta_(n-1) q_(n-2)/q_n.        (6)

The complement of S_B has moment degrees
`0,...,n-4,n-2,n-1,n`. The analogous four-by-four matrix, on columns
n-3 through n, is

    [ 0                    h_(n-2)        0          0   ]
    [ -s_(n-1) h_(n-3)     0              h_(n-1)    0   ]
    [ 0                    -s_n h_(n-2)   0          h_n ]
    [ q_(n-3)              q_(n-2)        q_(n-1)     q_n ].

The zero in its third row, first column uses opposite parity. Hence

    C_B/C_0=beta_n [s_(n-1)q_(n-1)
                  +beta_(n-1)beta_(n-2)q_(n-3)]/q_n. (7)

All these matrices follow by elimination of lower moment rows; no
claim about the selected HP coefficient has been used.

## 5. Their exact valuations and the final residue

Write `n=4r+1`; here r is odd. The endpoint-value facts already
proved in the preceding note and its bordered-Cauchy dependency give

    v_2(q_n)=v_2(q_(n-1))=2r,
    v_2(q_(n-2))>=2r+1,
    v_2(q_(n-3))=2r.                                 (8)

For the last equality use the even-index case at `n-3=4r-2`.
Furthermore

    v_2(s_n)=v_2(s_(n-1))=1,
    v_2(beta_(n-1))=4,
    v_2(beta_n)=v_2(beta_(n-2))=0.                   (9)

In (6), its first term has valuation one and its second term has
valuation at least five. In (7), the two summands inside the brackets,
after division by q_n, have respectively valuations one and four.
Thus

    v_2(C_A/C_0)=v_2(C_B/C_0)=1.                     (10)

Since `v_2(C_0)=L_n`, S_A and S_B each have total signed-term
valuation exactly `V_n+2`: their factorial loss is one and their
Vandermonde cost is zero. The exact paired-term lemma in the preceding
note gives

    v_2(T_0+T_*)=V_n+v_2(n-1)=V_n+2.               (11)

Divide the entire C-border Laplace sum by `2^(V_n+2)`. Equations
(10)–(11) leave exactly three dyadic units modulo two: the paired
term, S_A and S_B. Each has residue one independently of its sign.
Every other term has residue zero by Sections 2–3. Since
`1+1+1=1 mod 2`, their sum is a unit. Therefore the C-border part
has valuation exactly `V_n+2`.

The other border assignment, which carries -4, has gap at least

    2+n+2phi(n)+v_2(n)-2 floor((n+2)/4)

above V_n. For n>=5 this is strictly greater than two (already n=5
gives gap eleven). Thus it cannot alter the residue just obtained.
This proves `v_2(D_n)=V_n+2`. Restoring the actual factorial row
clearers and comparing with the independently proved Delta_B
valuation gives (1).

## 6. What remains

For n=1 modulo 8, the distinguished pair and both newly analyzed
terms lie `v_2(n-1)>=3` powers above baseline. Other configurations
then enter the relevant layers, so the three-unit argument here does
not apply. Their classification and possible cancellation remain
open. Nothing in this proof asserts an all-index real endpoint
bound, nonzero infinity cross-minor, or irrationality of e+pi.

The already available n=5 exact determinant is a check of the formulas,
not a premise. A separate small checker records the six classified
terms and the bordered-moment identities at that previously studied
degree; no new degree family is sampled.
