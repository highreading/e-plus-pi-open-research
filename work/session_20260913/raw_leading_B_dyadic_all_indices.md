> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# All-degree nonvanishing of the raw leading B coefficient

Date: 2026-09-13. Original continuation by audit_sources.

This note replaces an indefinite residue-class analysis with an exact
integral interpolation lemma. It concerns the canonical raw
Hermite–Padé triple normalized by `B_n(1)=1`, `C_n(1)=4` and proves
that `B_n` has degree exactly n for every n>=1. It does not prove the
nonzero infinity cross-minor, a real endpoint lower bound, or the
irrationality of e+pi.

The actual determinant convention and global arctangent-minor bound
are those already independently reviewed in
`raw_leading_B_dyadic_partial.md`. The two exact bordered-moment ratios
are derived in `raw_leading_B_dyadic_five_mod_eight.md`, Section 4;
their algebraic identities do not require that residue restriction.

## 1. Exact theorem

Write `b_n=B_{n,n}` for the actual normalized leading coefficient. Then

    v_2(b_n)=3                         if n=1;
    v_2(b_n)=v_2(n-1)                  if n>=5 and n=1 mod4;
    v_2(b_n)=0                         otherwise.     (1)

In particular b_n is nonzero for every n>=1. The first and third
lines are the previously proved cases. This note proves the second
line for all of its indices at once.

Throughout its proof assume `n>=5`, `n=1 mod4`, and put

    a=v_2(n-1)>=2, A=2n+1,
    phi(k)=v_2(k!), S(n)=sum_(j=0)^(n-1)phi(j),
    L_n=2S(n)+2 floor((n+2)/4),
    H_n=sum_(k=2n+1)^(3n)phi(k),
    V_n=S(n)-H_n+L_n.

The symbol A here denotes the integer 2n+1, not the polynomial in
the HP triple. Let E(k) be the exponential high row with columns
`1/(k-j)!`, `0<=j<=n-1`. Its top consecutive square block has rows
`k=A+i`, `0<=i<=n-1`; call it E_0. It is invertible by the ordinary
Vandermonde formula.

## 2. Exact integral interpolation coordinates

Every lower high row is `k=A-d`, with `1<=d<=n`. The interpolation
identity for polynomials of degree at most n-1 gives

    E(A-d)=sum_(i=0)^(n-1) M_(d,i) E(A+i),            (2)

where

    M_(d,i)=((A+i)!/(A-d)!) L_i(-d),
    L_i(-d)=(-1)^i (d)^(overline n)
                        /[(d+i)i!(n-1-i)!].           (3)

Here `(d)^(overline n)=d(d+1)...(d+n-1)` is the rising factorial,
and L_i is the cardinal Lagrange polynomial for nodes 0,...,n-1.
Indeed, after multiplying a row by k!, its jth entry is the falling
factorial `(k)_(underline j)`, to which ordinary interpolation applies.

Crucially, these coordinates are integers, since

    L_i(-d)=(-1)^i binom(d+i-1,i)
                           binom(d+n-1,n-1-i).        (4)

The factorial ratio in (3) is also an integer. In particular, no
denominator can undermine a valuation estimate for a minor of M.

**Interpolation divisibility lemma.** In the indicated finite ranges,

    M_(d,i) is divisible by 2^(a+1) whenever i>=1;
    M_(d,i) is divisible by 2^(a+2) whenever d>=4.    (5)

The three entries not covered by these suppressions have valuations

    v_2(M_(1,0))=0,
    v_2(M_(2,0))=v_2(M_(3,0))=1.                     (6)

The modulus in (5) is uniform in d and i; the proof below includes
the columns near the right endpoint of their range.

## 3. Proof of the interpolation divisibility lemma

For d>=4, the factorial ratio in (3) contains both the factors
`2n-2` and `2n`. Their valuations are respectively a+1 and one.
Thus it is divisible by `2^(a+2)`, proving the second assertion of
(5) in every column, by integrality of L_i(-d).

It remains to consider d=1,2,3 and i>=1. Put k=i+1, so
`2<=k<=n`. The first-row formula simplifies to

    M_(1,k-1)=(-1)^(k-1) ((2n+k)!/(2n)!) binom(n,k).
                                                               (7)

If `k>2^a`, the factorial ratio in each of the rows d=1,2,3 is a
product of `k+d-1` consecutive integers. Such a product is divisible
by `(k+d-1)!`. Its valuation is at least

    phi(k+d-1)>=phi(2^a+1)=2^a-1>=a+1.               (8)

The last inequality holds for every a>=2. The Lagrange weight is an
integer, so this proves the claim in this whole range without an
estimate for its binomial valuation.

Now assume `2<=k<=2^a`. Since `v_2(n-1)=a`, the k falling factors
in the binomial numerator give exactly

    v_2(binom(n,k))=a- v_2(k)-v_2(k-1).              (9)

To see this directly, n is odd, n-1 has valuation a, and for
`2<=j<=k-1` the factor n-j has valuation `v_2(j-1)`. Their valuation
sum is `a+phi(k-2)`, from which subtract phi(k).

Also `2n=2 mod 2^(a+1)`. Since `t+2<2^(a+1)` for
`1<=t<=k<=2^a`, it follows that

    v_2((2n+k)!/(2n)!)=phi(k+2)-1.                  (10)

Combining (7), (9) and (10), and cancelling the last four factorial
increments, yields

    v_2(M_(1,k-1))
      =a+phi(k-2)+v_2(k+1)+v_2(k+2)-1.              (11)

This is at least a+1. For k=2 or3 the last two valuations sum to
two; for k>=4, phi(k-2)>=1 and at least one of k+1,k+2 is even.

The next two rows have the exact ratios

    M_(2,k-1)/M_(1,k-1)
          =2n(n+1)k/(k+1),
    M_(3,k-1)/M_(1,k-1)
          =2n(2n-1)(n+1)(n+2)k/[2(k+2)].            (12)

They follow either from (3) or from the factorial and binomial
ratios separately. Since `v_2(n+1)=1` and n+2 is odd, equations
(11)–(12) give respectively

    v_2(M_(2,k-1))
      =a+phi(k-2)+v_2(k)+v_2(k+2)+1,
    v_2(M_(3,k-1))
      =a+phi(k-2)+v_2(k)+v_2(k+1).                  (13)

Both are at least a+1. This completes (5). At k=1, formula (7) is
`M_(1,0)=n(2n+1)`, a dyadic unit. The ratios (12) at k=1 show
exactly one additional power in each of d=2 and d=3. This proves (6).

## 4. Consequence for every exponential minor, not just single exchanges

Let `S_0={A,...,3n}`. A size-n set S of the full high rows is
obtained from S_0 by deleting a set I of top indices and adding the
same number of lower indices A-d. By (2), the exact ratio of its
exponential determinant to det E_0 is, up to a sign, the square minor

    det M_(D,I),                                     (14)

where deleted row A+i corresponds to column i. This is the usual
row-replacement determinant identity; it also follows by multilinear
expansion after expressing all replacement rows in the basis E_0.

If at least two rows are replaced, I contains a column i>=1. Every
entry in that column is divisible by `2^(a+1)`, and all other entries
are integers. Thus the minor (14) is divisible by `2^(a+1)`.
If just one row is replaced, the same conclusion holds unless
`i=0` and d is one of 1,2,3. This proves a complete classification
at the needed precision, without enumerating factorial-loss layers:

    det E(S)/det E_0 is divisible by 2^(a+1),

except for the original S_0 and exactly the three single exchanges

    S_*: replace A by A-1,
    S_A: replace A by A-2,
    S_B: replace A by A-3.                           (15)

Their exponential ratios have valuations zero, one and one by (6).
This argument includes every multiple exchange and every possible
deleted column.

## 5. The four exceptional terms reduce to three units

The general arctangent-minor theorem gives valuation at least L_n
for every complementary bordered C minor. For S_0 the exact
valuation is L_n in the current class. Since
`v_2(det E_0)=S(n)-H_n`, every term excluded by Section 4 is
divisible by `2^(V_n+a+1)`.

Retain the raw monic orthogonal endpoint values q_j and
`beta_j=j^2/(4j^2-1)`. Set `s_j=j(j-1)/(2(2j-1))`.
For `n=4r+1`, the established parity facts are

    v_2(q_n)=v_2(q_(n-1))=v_2(q_(n-3))=2r,
    v_2(q_(n-2))>=2r+1.                              (16)

The two bordered-moment identities, with the actual complementary
rows and unchanged endpoint border, are

    C_A/C_0=s_n+beta_n beta_(n-1)q_(n-2)/q_n,
    C_B/C_0=beta_n[s_(n-1)q_(n-1)
                    +beta_(n-1)beta_(n-2)q_(n-3)]/q_n. (17)

They were derived by exact three-by-three and four-by-four
orthogonal moment blocks in the preceding note. Here

    v_2(s_n)=v_2(s_(n-1))=a-1,
    v_2(beta_(n-1))=2a,
    v_2(beta_n)=v_2(beta_(n-2))=0.

In each identity (17), the term of valuation a-1 is uniquely least:
the other term has valuation at least 2a+1 in the first identity and
2a in the second. Therefore

    v_2(C_A/C_0)=v_2(C_B/C_0)=a-1.                  (18)

Combining (18) with their one-power exponential cost proves that
each of the signed terms T_A and T_B has valuation `V_n+a`.
The independently reviewed exact paired-term identity gives

    v_2(T_0+T_*)=V_n+a.                              (19)

Consequently, after division by `2^(V_n+a)`, precisely the following
three contributions remain nonzero modulo two:

    (T_0+T_*), T_A, T_B.

Each is a dyadic unit and hence has residue one, regardless of its
sign. Every other C-border term has residue zero by Section 4.
Their sum is one modulo two. Thus the entire C-border part has
valuation exactly `V_n+a`.

## 6. The other border and the actual normalized coefficient

The exponential-border assignment has the already proved gap

    G_n=2+n+2phi(n)+v_2(n)-2 floor((n+2)/4)
       =(n+5)/2+2phi(n)

above V_n in the present odd class. It is strictly greater than a.
For example, `n-1>=2^a>=2a` for a>=2 gives `(n+5)/2>=a+3`.
The factor -4 border therefore cannot change the leading residue.
The full actual reduced determinant satisfies

    v_2(D_n)=V_n+a.                                  (20)

Restoring all original high-row factorials gives

    v_2(B_star)=sum_(k=n+1)^(3n)phi(k)+V_n+a
              =v_2(Delta_B)+a.

The cofactor identity `b_n=B_star/Delta_B` then proves the second
line of (1). The endpoint normalization and the appended coordinate
row are exactly those in the original construction; no different
bordered determinant has been substituted.

## 7. Scope and verification

The argument is an all-index valuation proof. It establishes a
previously missing necessary factor of the cubic accessory gate:
`B_{n,n}!=0`. The distinct cross-minor Xi_n remains to be controlled,
and no real size estimate for B_{n,n} follows from this dyadic result.

No residue-class numerical scan is needed. The already saved n=5
control checks the four exceptional terms and their moment ratios.
The interpolation identity and divisibility estimates are intended
for independent symbolic review, including the finite ranges
`1<=d<=n`, `0<=i<=n-1` and the split at k=2^a. The exact n=1
exception is retained rather than applying the valuation a there.
