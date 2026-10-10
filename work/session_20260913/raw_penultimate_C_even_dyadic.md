> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact penultimate C coefficient in every even degree

Date: 2026-09-13. Original continuation by audit_sources.

Use the canonical raw normalization `B_n(1)=1`, `C_n(1)=4`. This
note proves the further coefficient theorem

    v_2(c_(n-1))=-n-2phi(n-1), n even, n>=2,          (1)

where `phi(j)=v_2(j!)`. This gives a concrete input for the distinct
infinity cross-minor Xi_n; it does not establish that cross-minor.

## 1. Actual coordinate determinant

Append the coordinate row selecting C_(n-1) to the original bordered
high-jet matrix. Expanding that row deletes its column. After dividing
the original high rows by their factorials, the resulting reduced
determinant has rows n+1,...,3n plus the endpoint border, and columns

    B_0,...,B_n | C_0,...,C_(n-2),C_n.

There is no factorial on the appended coordinate row. Its ratio to the
reduced endpoint denominator is, up to sign, the actual c_(n-1).
The reduced denominator valuation is

    V_n=S(n)-H_n+L_n,
    S(m)=sum_(j=0)^(m-1)phi(j),
    H_n=sum_(k=2n+1)^(3n)phi(k),
    L_n=2S(n)+c_n^val,
    c_n^val=2 floor((n+2)/4).                         (2)

## 2. The modified C-pole lower bound

Write n=2r. The C columns have r-1 odd poles
`1,3,...,2r-3`, and r+1 even poles `0,2,...,2r`.
Both pole sets are consecutive within parity. The only nonzero
bordered parity orientations have ordinary even/odd row counts

    (r-1,r), or (r-2,r+1).

The second orientation is absent when r=1. Using the exact square and
bordered Cauchy bounds from the original rank proof, define

    g(j)=j(j-1)/2+S(j),
    beta(R)=g(R-1)+(R-1)+epsilon_(R-1),

where epsilon_j is one for j odd and zero for j even. The two lower
bounds are

    K_1=2g(r-1)+g(r)+beta(r+1),
    K_2=2g(r+1)+g(r-2)+beta(r-1).                   (3)

For r>=2 their exact difference is

    K_2-K_1=2+2[phi(r)-phi(r-2)]
            =2+2v_2(r(r-1))>0.                     (4)

Thus K_1 is the global bound for every such C-border minor, including
zero minors. In the first orientation the square block has size r-1,
and the border goes to the even-pole block of size r+1.

The complement of the top n+1 exponential rows is

    U={n+1,n+2,...,2n-1}.

It has the first orientation and rows consecutive within each parity.
The bordered even-pole block begins at row 2r+1 and pole zero, so its
first difference is 2r+1. Whenever its size r+1 is even, r is odd and
this difference is 3 modulo4. Hence the archived equality criterion
applies and the C-border minor for U has valuation exactly K_1.
The r=1 case consists just of the bordered block and obeys the same
criterion.

For comparison with (2), direct substitution yields

    K_1=2S(n-1)+c_n^val.                            (5)

One way to check (5) is first to compare with the original lower
bound L_(n-1). The difference K_1-L_(n-1) is two if r is odd and
zero if r is even; exactly the same difference is
`c_n^val-c_(n-1)^val`.

## 3. Unique least term and the other border

The exponential block now has n+1 columns. With the border assigned
to C, its unique factorial-maximal row set is `{2n,...,3n}`. Its
consecutive Vandermonde attains S(n+1), and its complement attains
K_1 as proved above. Every other set loses at least one in the
factorial-valuation sum; no C minor falls below K_1. Therefore its
term is uniquely least and has valuation

    S(n+1)-H_n-phi(2n)+K_1.                          (6)

If the border is assigned to the exponential block, the -4 Lambda
alternant has valuation at least `2+S(n)-H_n`. The pure C block has
n columns, with odd/even pole counts r-1,r+1; the square Cauchy
factorization gives the global bound

    K_pure=2g(r-1)+2g(r+1).

The gap of this assignment above (6) is at least

    2+n+K_pure-K_1
      =2+n+r+2phi(r)-epsilon_r>0.                   (7)

This includes r=1. Thus the full reduced numerator has valuation
(6). Subtracting the denominator valuation (2), using
`phi(2n)=phi(n)+n` and (5), gives exactly (1).

## 4. The remaining comparison for Xi

The independently proved leading-A theorem gives `v_2(a_n)=-n`.
Thus in even degree the first product in

    Xi_n=a_n c_(n-1)-(a_(n-1)-c_n)c_n

is nonzero and has exact valuation

    v_2(a_n c_(n-1))=-2n-2phi(n-1).                  (8)

The second product is not bounded sharply enough here. An estimate
strictly above (8), or an exact residue comparison if the valuations
coincide, would prove Xi_n!=0. Its cancellation-adapted coefficient
`a_(n-1)-c_n` must be treated as one appended row; bounding its two
summands separately discards the cancellation that can matter.

The proof does not assume either product is dominant. No new degree
scan is used and no conclusion about the endpoint remainder or e+pi
follows from (1) alone.
