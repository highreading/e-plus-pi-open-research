> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Eight row sets suffice at the unresolved Xi residue precision

Continuation status: the finite residue has now been evaluated in
raw_Xi_remaining_class_mod_eight.md and its independent review,
completing the all-index cubic-degree condition. The reduction below
is retained with its original scope as a proof dependency.

Date: 2026-09-13. Original structural continuation by audit_sources.

Assume n>=5, n=1 modulo4, and put `a=v_2(n-1)>=2`. This note proves
an exact finite reduction for the actual remaining cross-minor Xi_n.
It does not evaluate the final eight-set quadratic residue.

The top-block factorization in `raw_Xi_top_block_factorization.md`
shows that its distinguished quadratic part cancels to a+1 powers
above the product baseline. The present lemma retains every row set
that can contribute through that depth, rather than only that part.

## 1. The correct n+1-column interpolation matrix

Set c=2n and N=n+1. The top exponential block has rows c+i,
`0<=i<=n`, and columns `1/(k-j)!`, `0<=j<=n`. A replacement row is
c-d. For all coefficient determinants needed below, `1<=d<=n+1`;
the final possible row c-(n+1)=n-1 uses the exact falling-factorial
convention at the last exponential column.

Its integral interpolation coordinates are

    M_(d,i)=((c+i)!/(c-d)!) L_i(-d),
    L_i(-d)=(-1)^i (d)^(overline N)
                    /[(d+i)i!(N-1-i)!],             (1)

where the cardinal nodes are 0,...,N-1. All coordinates are integers:

    L_i(-d)=(-1)^i binom(d+i-1,i)
                              binom(d+N-1,N-1-i).

The exact ratio of any replaced exponential determinant to the top
one is, up to sign, the corresponding square minor of M.

## 2. Uniform divisibility outside a small block

For every d>=3, the factorial ratio in (1) contains the factors
c-2=2(n-1) and c=2n. Their valuations sum to a+2. Therefore every
entry in such a row is divisible by `2^(a+2)`.

Consider d=1,2. For i>=2 the cardinal weights can be written as

    L_i(-1)=(-1)^i N(N-1)(N-2)/[(i-1)i(i+1)]
                              *binom(N-3,i-2),
    L_i(-2)=(-1)^i (N+1)N(N-1)(N-2)/[(i-1)i(i+2)]
                              *binom(N-3,i-2).       (2)

Their numerator has valuation a+1, because v_2(N)=1,
v_2(N-2)=a, and N-1,N+1 are odd. A product of i+d consecutive
integers is divisible by (i+d)!. Thus (1)–(2) imply

    v_2(M_(1,i))>=a+1+phi(i-2),
    v_2(M_(2,i))>=a+1+phi(i-2)+v_2(i+1).            (3)

For i>=4, both are at least a+2. This proof is uniform up to i=n;
it does not assume that i is small compared with n or 2^a.

The eight remaining entries have the following exact valuations:

| | i=0 | i=1 | i=2 | i=3 |
|---|---:|---:|---:|---:|
| d=1 | 2 | 1 | a+3 | a+1 |
| d=2 | 1 | 2 | a+1 | a+3 |

For verification, the first row is

    M_(1,i)=(-1)^i ((2n+i)!/(2n-1)!) binom(n+1,i+1).

Use `v_2(2n)=1`, `v_2(2n+2)=2` and `v_2(n-1)=a` for i=0,...,3.
The second-row ratio is exactly

    M_(2,i)/M_(1,i)=(2n-1)(n+2)(i+1)/(i+2),         (4)

whose two leading factors are odd. These give the displayed table.

## 3. Complete classification of replacement minors at this precision

Any replacement using a row d>=3, or a column i>=4, has determinant
divisible by `2^(a+2)`. A replacement of at least three rows must use
such a row, since only d=1,2 remain below this threshold.

For a two-row replacement using rows 1,2, the upper-left column pair
0,1 has determinant valuation exactly two: its two product terms have
valuations four and two. Every other column pair is divisible by
`2^(a+2)`. For pairs 0,2; 0,3; 1,2; 1,3 the respective lower bounds
from the table are a+3,a+2,a+2,a+3; for 2,3 the lower bound is
2a+2, also sufficient. There is no cancellation assumption in these
lower bounds.

It follows that, modulo `2^(a+2)`, the only possible exponential
row sets are precisely these eight:

1. The unchanged set S_0={2n,...,3n}.
2. Four single replacements `(d,i)=(1,0),(1,1),(2,0),(2,1)`.
3. The double replacement with D={1,2}, I={0,1}.
4. The two exceptional singles `(d,i)=(1,3),(2,2)`.

The notation (d,i) means replace the top row 2n+i by the lower row
2n-d. Every listed row exists in each actual coefficient determinant
for n>=5. All other exponential minors are suppressed to the next
power, with a bound uniform in their row count and positions.

## 4. Transfer of the precision to the actual coefficient minors

Take the actual reduced cofactor determinants for

    A=a_n, H=a_(n-1)-c_n, C=c_n, D=c_(n-1),

all divided by the same actual reduced endpoint determinant. Keep
only the C-border Laplace terms whose exponential rows are in the
eight-set list above, with their original signs and complementary C
minors. Denote these exact truncated rational coefficients by
`A_8,H_8,C_8,D_8`. This definition uses the original minors; it
does not rescale or separately normalize the four coefficients.

For the A,H numerators, every complementary C-border minor has
valuation at least L_n. For C,D it has valuation at least L_(n-1)
in the current odd class. The signed Cauchy proof remains valid for
the single modified H row with t_(-1)=1. The same row is outside
the eight-set list whenever assigned to the exponential block,
because its replacement index is d=n+1>=6.

The baseline values of the four normalized coefficients, already
proved for n=1 modulo4, are

    alpha=-n=v_2(A)=v_2(H),
    chi=-n-2phi(n-1)=v_2(C)=v_2(D).                 (5)

Since the top exponential determinant has its known Vandermonde
valuation, the uniform minor suppression therefore gives

    v_2(A-A_8), v_2(H-H_8)>=alpha+a+2,
    v_2(C-C_8), v_2(D-D_8)>=chi+a+2.                (6)

The other endpoint-border assignment also satisfies (6). Its gaps
are `2+n+2phi(n)-c_n^val` for A,H and
`2+n+2phi(n-1)-c_(n-1)^val` for C,D. Here
`c_n^val=c_(n-1)^val=(n-1)/2`; both gaps exceed a+2 because
`n-1>=2^a>=2a` and n>=5. Thus (6) does not omit the -4 assignment.

## 5. An exact finite quadratic residue problem

Define the eight-set approximation to the cross-minor by

    Xi_8=A_8 D_8-H_8 C_8.

Equations (5)–(6) imply that each truncated coefficient retains its
baseline valuation, and multiplication gives the rigorous error
bound

    v_2(Xi_n-Xi_8)>=-2n-2phi(n-1)+a+2.              (7)

Consequently a nonzero residue of

    2^(2n+2phi(n-1)-a-1) Xi_8 modulo2               (8)

would prove the full Xi_n nonzero, with valuation equal to the
baseline plus a+1. If Xi_8 has an earlier nonzero valuation, (7)
would likewise transfer it. Neither alternative has yet been
established; (8) is not assumed to be integral until the lower
valuation layers of Xi_8 have been checked.

The remaining task is now an explicit finite family of bordered
Cauchy/moment products and their signs at the required precision.
This is stronger than examining only the unchanged top block, whose
factorization was already known, and stronger than entrywise bounds
that ignore multiple replacements. No broad scan or asymptotic
extrapolation is used in the reduction.
