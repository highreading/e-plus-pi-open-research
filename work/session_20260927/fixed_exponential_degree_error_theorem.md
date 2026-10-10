> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Every fixed exponential degree: normality and the evaluated error

Date:2026-09-27. Root original continuation from the reviewed b=1,b=2
notes. Status: FULL PASS by audit_results in
fixed_exponential_degree_error_independent_review.md.
No degree scan is used. This does not control the reduced endpoint gcd.

Let b>=1 be FIXED. Use the original function
F(z)=4 arctan(z/(2-z)) and degree caps(n,b,n), order2n+b+1,
with B(1)=C(1)=Y. For all sufficiently large n the projective
solution is unique and Y is nonzero. Let epsilon_n>0 denote the
ordinary logarithmic Pade error in the earlier boundary theorem.
The claim proved here is

    (-1)^n R(1)/(Y epsilon_n) -> (sqrt(2)-1)^b.           (1)

Consequently, for every one fixed b, the actual normalized error has
the same exponential rate -2log(1+sqrt(2)). The constant improves with
b. No uniformity as b grows with n is asserted.

The previous b=1,b=2 constants are recovered. The b=0 theorem is
separate and already proved. Previous general-b coefficient amplification
and forced-divisor bounds do not establish (1); conversely (1) supplies
no actual reduced-denominator estimate.

## 1. Exact reduced rows and the entire remainder

Use the monic polynomials p_k, their alternating nonzero norms, and
the kernel K_n from unequal_degree_hp_attempt.md. Put

    U_l=p_(n+l), l=1,...,b-1;
    V(t)=K_n(t,1), W(t)=1/(1-t)-H_n(t),
    ell_j(t^k)=1/(n+k+1-j)!, j=0,...,b.

Here H_n is the orthogonal projection of1/(1-t), not the integer
auxiliary sequence also named H in the arithmetic notes.
For n>=b the original equations are exactly

    sum_j B_j ell_j(U_l)=0, l=1,...,b-1,
    sum_j B_j(1+ell_j(V))=0.                            (2)

The first n+1 moment rows uniquely reconstruct C*=-ell_B K_n.
Taylor reconstruction uniquely gives A. The full evaluated remainder
is EXACTLY R(1)=ell_B(W), by the same subtraction of both complete
tails used in the b=1 and b=2 proofs. The factorial sums converge
absolutely; this is not a first-Taylor-coefficient estimate.

Write e=(1,...,1), v=(ell_j(V)), w=(ell_j(W)), and let U denote
the b-1 high rows. The maximal-cofactor vector of [U;e+v] gives

    Y=det[U;e+v;e]=-det[U;e;v],
    R(1)=det[U;e;w]+det[U;v;w].                        (3)

All determinants have b+1 columns. A common orientation factor in
the cofactor vector cancels from R/Y.

## 2. A fixed-size factorial determinant lemma

Let d>=1 be fixed and let U=U_n be a degree n+1 polynomial with
U(0)!=0, reciprocal roots bounded by a fixed L, and

    U(z/n)/U(0) -> exp(-c z)

locally uniformly. Suppose d functions have the form

    P_i(t)=a_i U(t)G_i(t)/U(0),

where a_i!=0, and G_i are uniformly analytic and bounded on one fixed
disk about zero, converging locally to G_i,infinity. Define
D_j=ell_(j+1)-ell_j, j=0,...,d-1. Then, with S=d(d-1)/2,

    (n!)^d n^S det[D_j(P_i)] / product_i a_i
      -> exp(-dc) product_(j=0)^(d-1)(j!)
         det[[t^j]G_i,infinity]_(i=1..d,j=0..d-1).      (4)

This limit remains meaningful when its right side is zero; only
applications with a nonzero right side will be divided by it.

### Proof including the cancellation scale

Write U/U(0)=sum u_k t^k. Then
|u_k|<=binom(n+1,k)L^k and u_k/n^k->(-c)^k/k!.
For the monomial shift t^r U/U(0), the functional D_j is

    sum_k u_k P_j(n+k+r+1)/(n+k+r+1)!,
    P_j(X)=(X)_(j+1)-(X)_j,

where (X)_j is falling. Each P_j is monic of degree j+1.
For a fixed vector r=(r_1,...,r_d), expand the row determinant
multilinearly in its k_i. The polynomial determinant
det[P_j(X_i)] is divisible by Vandermonde(X_i). Its highest
homogeneous part is product_i X_i times Vandermonde(X_i); its
remaining quotient has degree at most d-1. Therefore

    n^(-d) det[P_j(n+k_i+r_i+1)]
      -> Vandermonde(k_i+r_i).

The corresponding factorial ratios and coefficient limits imply

    (n!)^d n^(sum r_i) det[D_j(t^r_i U/U(0))]
      -> sum_(k_1,...,k_d>=0)
           product_i [(-c)^k_i/k_i!] Vandermonde(k_i+r_i)
       = exp(-dc) Vandermonde(r_i).                    (5)

The last equality can be proved without probability: the sum is an
alternating polynomial in the r_i, of total degree at most S. It is
therefore a scalar multiple of their Vandermonde. Its top-degree
coefficient is the product of the d exponential sums, exp(-dc).

Domination and Taylor remainders are essential. For n>=1,
n!/(n+k+r+1)!<=n^(-k-r-1), while the root bound after division by
n^k is at most (2L)^k/k!. The polynomial determinant after division
by n^d is bounded by a fixed polynomial in all k_i+r_i+1, since
its quotient by the Vandermonde has degree d and n>=1.
Summation against the factorial weights thus gives a bound

    |(n!)^d n^(sum r_i) det[D_j(t^r_i U/U(0))]|
       <= C product_i(1+r_i)^M                         (6)

for fixed C,M depending only on d,L. Identical shifts give identical
rows, so their determinants vanish exactly.

Expand every G_i in its uniformly Cauchy-bounded Taylor series and
use multilinearity. The least possible sum of DISTINCT nonnegative
r_i is S, attained by permutations of0,...,d-1. Those terms give
the determinant on the right of(4), with
Vandermonde(0,...,d-1)=product_j j!.
All remaining terms have sum r_i>=S+1. Combining (6) with the
geometric Cauchy coefficient bounds makes their normalized total
O(1/n), once n exceeds twice the inverse common disk radius.
This proves (4) and justifies every sum interchange. The argument
requires only fixed d; its constants are not uniform in d.

## 3. Local ratios of the actual reference polynomials

Set a=(1+sqrt(2))/4, beta=1/16, and choose

    lambda(t)=(t-1/2-sqrt((t-1/2)^2+1/4))/2,
    lambda(0)=-a,
    h(t)=lambda(t)/lambda(0).

The actual recurrence is
p_(k+1)=(t-1/2)p_k+beta_k p_(k-1),
beta_k=k^2/[4(4k^2-1)] ->beta, with beta_k<=1/12.
On |t|<=1/20, each ratio p_(k+1)/p_k has real part at most-9/20:
this is true initially, and the reciprocal of a number with negative
real part has negative real part. The ratios are thus nonzero and
uniformly bounded. The recurrence maps have Lipschitz constant at
most (1/12)/(9/20)^2<1 on these ratios and the displayed branch.
Comparison with the fixed-point equation for lambda and beta_k->beta
therefore proves uniform convergence to lambda on a smaller disk.
Cauchy's formula gives convergence of fixed derivatives.

Consequently, with U=p_(n+1),

    (U_l(t)/U_l(0))/(U(t)/U(0)) -> h(t)^(l-1).          (7)

The already reviewed b=2 proof gives U(z/n)/U(0)->exp(-sqrt(2)z)
and the reciprocal-root bound2. It also gives the exact normalized
quotients for V and W:

    G_V,n=[1-b_n p_n/p_(n+1)]/[2(1-t)],
    G_W,n=[1-alpha_n^* p_n/p_(n+1)]/
                     [(1+alpha_n^*/b_n)(1-t)],

where b_n->a and alpha_n^*->(1-sqrt(2))/4.
Their denominators are uniformly bounded away from zero locally.
Put kappa=sqrt(2)-1 and s=kappa^2. The limits simplify to

    G_V=(1-s)/(h-s),       G_W=2/(h+1).                (8)

For verification lambda=-a h and beta/a=a s give
1-t=a(h+1)(h-s)/h; also a(1-s)=1/2. These identities prove both
expressions in(8) exactly. In particular h'(0)=-sqrt(2)!=0.

## 4. Nonzero endpoint determinant and its limiting ratio

Subtract each column from its successor in det[U;e;v] or det[U;e;w],
retaining the first column. This transformation has determinant1.
The e row becomes(1,0,...,0), leaving the d=b determinant in(4)
for the functions U_1,...,U_(b-1),V or W respectively. The expansion
sign is identical for V and W and cancels from their quotient.

Their limiting Taylor-jet rows are

    1,h,...,h^(b-2),G_V      or      1,h,...,h^(b-2),G_W.

Changing the local variable from t to h-1 multiplies both jet
determinants by the same nonzero power of h'(0). The polynomial
rows span all polynomials of degree<=b-2. Thus their ratio is the
ratio of order b-1 derivatives of the last row with respect to h,
evaluated at h=1. Both are nonzero and

    det_jets(W)/det_jets(V)
       =((1-s)/2)^(b-1)=kappa^(b-1).                 (9)

Formula(4) now proves det[U;e;v]!=0 eventually, and

    det[U;e;w]/det[U;e;v]
       ~ (W(0)/V(0)) kappa^(b-1).                    (10)

For b=1 the list of high rows is empty and the same argument uses
the order-zero derivative; its ratio is1, as required.

## 5. Eventual rank and the remaining determinant

Consider the b-column minor of [U;e] using columns0,...,b-1.
Column differences leave the r=b-1 version of(4) with limiting
rows1,h,...,h^(b-2). Its jet determinant is nonzero. For b=1
the minor is simply1. The same minor of [U;e+v] differs by the
minor of [U;v]. Each factorial functional at fixed j has an
absolute bound C n^j |P(0)|/n! for the normalized functions here.
Compared with the proved nonzero leading minor, the perturbation
has relative bound C n^M |V(0)|/n!, with M fixed depending on b.
The reference estimates give |V(0)|=exp(O(n)), so this tends to0.
Hence (2) has rank b eventually and its projective solution is unique.
Section4 and(3) prove its endpoint Y is nonzero eventually.

The same entry bounds show

    det[U;v;w]/det[U;e;v]
          = (W(0)/V(0)) O(n^M |V(0)|/n!).             (11)

Indeed the numerator has one additional factorially small row;
the nonzero denominator asymptotic from(4) loses only a fixed power
of n. This bound uses absolute values for each normalization factor
and does not require a positive complex measure.
Thus (11) is negligible compared with(10), whose limiting constant
is nonzero.

## 6. Signed error and the precise fixed-degree limitation

Combining(3),(10),(11) gives

    R(1)/Y ~ -(W(0)/V(0)) kappa^(b-1).

The prior exact reference identity is

    W(0)/V(0)=(-1)^(n+1)epsilon_n(1+alpha_n^*/b_n)/2.

Its final positive factor tends to kappa. This proves(1), including
eventual nonvanishing and sign. Since
log epsilon_n/n -> -2log(1+sqrt(2)), the asserted exponential rate
follows for each fixed b.

For the ACTUAL reduced denominator q_(n,b)=den(A(1)/Y), this yields

    log|q_(n,b) R(1)/Y|
      =log q_(n,b)-2n log(1+sqrt(2))+o(n).             (12)

No estimate for q_(n,b) has been derived here. Fixed b cannot change
the analytic exponential rate, although it changes the constant and
may change the unresolved arithmetic. To consider b=b(n), one must
prove uniform determinant, ratio, and nonvanishing estimates; taking
b to infinity in(1) is not justified. The next substantive issue is
uniformity versus the actual endpoint gcd, not another fixed-b scan.
