> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit: the cubic accessory coefficient at every even index

Date: 2026-09-13. Reviewer: audit_results.
Sources reviewed in full: raw_penultimate_C_even_dyadic.md and
raw_Xi_even_dyadic.md. The original bordered-Cauchy proof and actual
integer/coefficient row conventions were read directly during this audit.

**Verdict:** both proofs pass. In the actual B(1)=1, C(1)=4 normalization,

    v2(Xi_n)=-2n-2phi(n-1)       if4 divides n,
    v2(Xi_n)=-2n-2phi(n-1)-2     if n=2 mod4,

for every even n>=2. Since the independently established b_n is a
dyadic unit at every even index, the identity [z³]Q_n=b_n Xi_n proves
deg Q_n=3 throughout the even subsequence. No claim about odd indices,
Archimedean size, or irrationality follows from this audit.

## 1. The penultimate C determinant

Appending the coordinate row for C_(n-1) and expanding it deletes
that column with no factorial factor. For n=2r the remaining pole
sets have sizes r-1 and r+1: odd poles1,...,2r-3 and even poles0,...,2r.
The two admissible ordinary-row count pairs are (r-1,r) and (r-2,r+1).
The second is absent at r=1.

The source's global bounds are exactly

    K1=2g(r-1)+g(r)+beta(r+1),
    K2=2g(r+1)+g(r-2)+beta(r-1).

Using beta(R)=g(R-1)+R-1+epsilon_(R-1), I independently get

    K2-K1=2+2[phi(r)-phi(r-2)]>0.

This identity is used only for r>=2. For the complement
{n+1,...,2n-1}, both parity row sets are consecutive and the bordered
even-pole block starts at difference2r+1. If its size r+1 is even,
that difference is3 modulo4; if its size is odd, the archived
even-ordinary-row equality already applies. Hence K1 is attained.

Also S(2r-1)=g(r-1)+g(r) gives directly

    K1=2S(n-1)+r+epsilon_r
      =2S(n-1)+c_n^val.

The top n+1 exponential rows {2n,...,3n} uniquely maximize the
factorial sum because phi(2n)>phi(2n-1). They attain the consecutive
Vandermonde bound, and no complementary C minor falls below K1.
The competing exponential-border assignment has pure-C bound
2g(r-1)+2g(r+1); its gap is exactly bounded below by

    2+n+r+2phi(r)-epsilon_r>0.

Subtracting the actual denominator valuation therefore gives
v2(c_(n-1))=-n-2phi(n-1). The r=1 bordered block has no missing
ordinary-row hypothesis, and the same calculation includes n=2.

## 2. The leading C bound and its equality class

Deleting C_n leaves consecutive C columns0,...,n-1, so the global
bordered bound is L_(n-1), and the pure-C bound is2S(n).
For the top exponential row set, the bordered parity block has size r,
first difference2r+1, and r-1 ordinary rows. When r is odd, the latter
number is even, so the bound is attained. This proves equality for
n=2 mod4 and only a lower bound when4 divides n, as the source states.

The other-border gap2+n+2phi(n-1)-c_(n-1)^val follows by subtracting
the exact top-term lower bound, with the -4 factor retained.
Finally

    L_(n-1)-L_n=-2phi(n-1)-2*1_(n=2 mod4),

which gives precisely the source's bound on v2(c_n), with equality
in the class where it is needed. Zero c_n is legitimately permitted
in the divisible-by-four class.

## 3. The modified index-minus-one row is exact

Ordinary reconstruction gives

    a_(n-1)=-sum_j b_j f_(n-1-j)-sum_(j<=n-1)c_j t_(n-1-j).

Consequently h=a_(n-1)-c_n is the negative coefficient-style row at
k=n-1 if and only if f_-1=0 and t_-1=1. These are exactly the stated
conventions. The exponential value is also the falling-factorial
evaluation (n-1)_n/(n-1)!=0. No factorial row scale is missing.

For s=-1 the algebraic odd-index formula (-1)^((s-1)/2)/s equals1.
It therefore preserves both parity row/column sign identities of the
Cauchy reduction. The only newly possible negative denominator is-1;
it is nonzero and a dyadic unit.

I checked that the archived bordered valuation proof survives this
sign change. Its determinant identity can be written with the signed
common denominator and the signed product sum

    S_q=sum_h binom(q,h) product_i(a_i-2h).

For arbitrary odd integers a_i, expanding powers of h in falling
factorials shows S_q/2^q is integral. Modulo2, only the terms of
orders0 and1 can remain. At even q only the constant term remains;
at odd q those two terms cancel. This proves the same lower bounds
regardless of whether some a_i-2h is negative. Square Cauchy
valuations likewise depend on Vandermondes and odd denominators,
not their real signs. No positivity claim is required here.

## 4. The H parity blocks and every competing term

The ordinary row set is {n-1} union {n+1,...,3n}. Its factorial-maximal
n+1-row subset remains {2n,...,3n}. Every different subset loses at
least phi(2n)-phi(2n-1)=v2(n)+1 in the denominator valuation sum.

The complementary set U_h has r+1 odd rows and r-1 even rows.
Thus its square block uses the even poles and has size r+1, while
its bordered odd-pole block has size r. The single negative
denominator occurs in the square block of this particular top term;
the bordered block's first difference is still2r+1.

The original second-orientation bound satisfies

    L_B-L_n=0 when r is odd,
    L_B-L_n=2+2v2(r)=2v2(n) when r is even.

All parity rows are consecutive. When r is odd, the bordered block
has an even number of ordinary rows, so its lower bound is attained.
The top exponential term is then uniquely least and gives v2(h)=-n.

When r is even, let v=v2(n)>=2. The top term is at least2v above
the baseline V_n-n; every other C-border term is at least v+1 above
it. Thus all C-border terms have gain at least min(2v,v+1)=v+1.
The exponential-border assignment has gap

    G_n=2+n+2phi(n)-c_n^val>=1+n/2>=v+1.

This checks the entire competing assignment, not only a presumed
dominant term. The resulting lower bound v2(h)>=-n+v+1 includes
h=0 and does not come from subtracting separate coefficient bounds.

## 5. Product comparison and a closed existing-degree control

The first Xi product has exact valuation
-2n-2phi(n-1). For4|n, the second product has valuation at least
v2(n)+1 higher, so the first uniquely controls the difference.
For n=2 mod4, the second product instead has exact valuation two
powers lower, so it uniquely controls the difference. A change in
the real sign of either product cannot affect this dyadic argument.

As a normalization check at the already available n=2 row, direct
reconstruction from its saved B coefficients gives

    a_2=18891/(4*1027),
    c_1=-535/(4*1027),
    c_2=27215/(16*1027),
    h=-12927/(4*1027).

Thus the two Xi products have valuations-4 and-6, exactly as required.
This reuses an existing degree and is not an increasing-degree scan;
the all-index proof is the parity/Cauchy and unique-term argument above.

The exact cofactor identity [z³]Q=b_n Xi uses the canonical polynomial
normalization. The source retains the separate one- and two-power
endpoint determinant scales for b_n and Xi. No replacement by a raw
unreduced coefficient or an endpoint value is made.
