> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large-selector selection by finite and divided differences

Status: author proofs, not independently reviewed. No computation is claimed. The complete dyadic-denominator consequences below depend on the pending examination of LARGE_SELECTOR_DYADIC_DENOMINATOR_DRAFT.md. None of these results proves irrationality of e+pi or controls the complete logarithmic error.

All logarithms are natural. Fix rho>0. Write n=4k, r=n/2, and

U(n,m)=[x^n](1+2x+2x^2)^n(1-2x^2)^(2m), m>=0 an integer.

For fixed n, its binomial expansion defines a polynomial in m. The associated selector is L_m(t)=(2t^2-4t+1)^(2m).

## 1. Polynomial nonvanishing selection

Set a_j=[x^j](1+2x+2x^2)^n. Then

U(n,m)=sum_{ell=0}^r (-2)^ell binom(2m,ell) a_{n-2ell}.

Only ell=r contributes degree r. Since a_0=1 and r is even, its leading coefficient is 4^r/r!. Thus the degree is exactly r, and every r+1 distinct real arguments contain one where U is nonzero. In particular, taking the first nonzero argument among

floor(rho n log n),...,floor(rho n log n)+r

defines m_n=rho n log n+O(n) with U(n,m_n)!=0.

There is also uniform coefficient divisibility. A contribution to a_{2j} uses 2v linear terms and j-v quadratic terms, hence carries 2^(j+v). Consequently

2^j divides a_{2j}, and a_{2j}/2^j = binom(n,j) modulo 2.

Every summand in U is therefore divisible by 2^r. For nonzero U this gives v_2(U)>=r; it does not give equality without an additional parity condition.

## 2. Quantitative selection on an arithmetic progression

For every positive integer h, the degree and leading coefficient give

Delta_h^r U(n,m)=(4h)^r.

The sum of absolute values of the difference coefficients is 2^r. Therefore

max_{0<=j<=r}|U(n,m+jh)| >= (2h)^r.

For sufficiently large n, take h=floor(log n/log log n), m_0=floor(rho n log n), and choose the smallest maximizing argument among m_0,m_0+h,...,m_0+rh. This is a mathematical selection rule; no maximizer search has been executed. It gives

m_n=rho n log n+O(n log n/log log n)=rho n log n+o(n log n).

For every m>0 and R>0, coefficient majorization yields

|U(n,m)| <= R^(-n)(1+2R+2R^2)^n(1+2R^2)^(2m).

Use 1+2R+2R^2<=exp(2R), 1+2R^2<=exp(2R^2), and R=sqrt(n/(4m)). Then

|U(n,m)| <= (4m/n)^(n/2) exp(n+n sqrt(n/m)).

On the selected sequence the logarithm of this upper bound is at most (n/2)log log n+O_rho(n). The difference lower bound gives

log|U(n,m_n)| >= (n/2)(log log n-log log log n)+O(n).

Together these imply

log|U(n,m_n)|=(1/2+o(1))n log log n.

## 3. Simultaneous parity and quantitative selection

Restrict to n=2^s, s>=2, so k=n/4 is a power of two. The coefficient congruence from Section 1 and Vandermonde's identity give

U(n,m)/2^r = sum_{ell=0}^r binom(2m,ell)binom(n,r-ell)
           = binom(n+2m,r) modulo 2.

Reducing the identity (1+X)^(2a)=(1+X^2)^a modulo 2 gives

binom(n+2m,r)=binom(2k+m,k) modulo 2.

For k a power of two, the last binomial coefficient is odd exactly when the binary digit corresponding to k in 2k+m is one. Adding 2k does not change that digit. Thus it is odd exactly when

m modulo 2k belongs to [k,2k-1].

Every such m satisfies v_2(U)=r and in particular U!=0.

For sufficiently large n choose a power of two h with

log n/(2 log log n)<h<=log n/log log n.

Then h divides k. Put m_0=floor(rho n log n). The interval

[m_0,m_0+n(h+1)]

contains at least 2h+1 complete integer blocks of length 2k, aligned at multiples of 2k. Each contains exactly k/h multiples of h whose residues lie in [k,2k-1]. There are therefore at least

(2h+1)k/h=2k+k/h>=r+1

eligible nodes in the interval.

Choose the first r+1 eligible nodes m'_0<...<m'_r. Their spacing is at least h. The leading coefficient in Lagrange interpolation gives

4^r/r! = sum_{i=0}^r U(n,m'_i)/product_{j!=i}(m'_i-m'_j).

For each i,

|product_{j!=i}(m'_i-m'_j)| >= h^r i!(r-i)!.

Hence the sum of the absolute reciprocal denominators is at most 2^r/(h^r r!), and

max_i |U(n,m'_i)| >= (2h)^r.

Choose the smallest maximizing node. The interval length is O(n log n/log log n), so the same upper and lower estimates as in Section 2 prove simultaneously

m_n=rho n log n+o(n log n),
v_2(U(n,m_n))=n/2,
log|U(n,m_n)|=(1/2+o(1))n log log n.

This selection is explicit as a finite rule but has not been implemented or searched numerically.

## 4. Conditional complete-denominator consequences

Let q be the actual reduced denominator of the complete rational center alpha+beta associated with L_m. The proposed complete dyadic law in LARGE_SELECTOR_DYADIC_DENOMINATOR_DRAFT.md is

v_2(q)=v_2(n!)+v_2((n+4m)!)+v_2(U)-n-2m,

for n=4k and U!=0. Its independent examination is pending; it is not established by the selection arguments above.

If that law holds, Section 1 implies

v_2(q)>=3n/2+2m-s_2(n)-s_2(n+4m),

where s_2 denotes binary digit sum. For the sequence of Section 3, equality holds. In particular, on either quantitative selection sequence the law implies

liminf log q/(n log n)>=2rho log 2.

The equality of dyadic valuations belongs only to the parity-qualified sequence. It must not be transferred to arbitrary nonzero or maximizing nodes.

## 5. Consequence of the saved author exponential estimate

LARGE_SELECTOR_EXPONENTIAL_REMAINDER_DRAFT.md supplies the author estimate, with Lambda=2n+8m,

0<|e-alpha|<3 Lambda^n exp(Lambda/(n+1))/((n+1)(n!)^2 |U|).

Conditional on that estimate, either quantitative selection above gives

log|e-alpha| <= -n log n+(1/2+o(1))n log log n.

Indeed, n log Lambda-2log(n!)=-n log n+n log log n+O_rho(n), Lambda/(n+1)=O_rho(log n), and the forcing normalization contributes -log|U|=-(1/2+o(1))n log log n.

This exponential estimate concerns one component only. A small upper bound for it does not establish a signed lower bound for the complete approximation error.

## 6. Remaining obligation

Maximizing |U| controls the forcing denominator normalization. It supplies no lower bound for the logarithmic remainder and no dominance over a conjugate-endpoint enclosure. The parity-preserving construction changes m by O(n log n/log log n); estimates previously restricted to an O(n) adjustment require their uniformity to be checked before use here. Any branch exclusion still needs a complete-error lower bound on the same selected sequence. No such bound is proved in this note.
