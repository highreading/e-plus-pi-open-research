> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent verification of the degree-two HP endpoint theorem

Date: 2026-09-13. Reviewed `hp_b2_endpoint_attempt.md`, particularly
Sections3–5, against the previously verified projection, Legendre,
Christoffel–Darboux, and b=1 identities.

## Verdict

No substantive gap was found. The new argument proves eventual
normality, the negative B(0)-normalized endpoint, and



$$
\frac{(-1)^nR_n(1)}{Y_n\epsilon_n}
 \longrightarrow(\sqrt2-1)^2.
$$



It does not prove a primitive-denominator bound. Every analytic
nonvanishing assertion is eventual; the proof claims no explicit
uniform numerical cutoff. Its limiting constants and uniform estimates
do supply a finite cutoff mathematically.

The proposed sharper degree-one corollary also follows:



$$
\frac{(-1)^nR_n^{(1)}(1)}{Y_n^{(1)}\epsilon_n}
 \longrightarrow\sqrt2-1,
 \qquad
 \frac{Y_n^{(2)}}{Y_n^{(1)}}
 \sim-\frac{1+1/\sqrt2}{n^2},
$$



where both endpoints use B(0)=1. Thus degree two changes a constant in
the normalized remainder and a polynomial factor in the endpoint;
it retains the same exponential error rate.

## 1. Exact projection and determinant identities

For caps(n,2,n) and order2n+3, the high Taylor rows are indexed by
k=0,...,n+1. The first n+1 rows uniquely determine C* by the nonsingular
moment projection, and the remaining row is ell_B(p_(n+1))=0. Together
with endpoint matching this gives exactly the two rows stated in the
note, with no missing constraint or extra free dimension. The low rows
then determine A uniquely.

Writing a=(a_0,a_1,a_2), t=(t_0,t_1,t_2), and w=(w_0,w_1,w_2), the raw
B vector is a cross (1+t). Consequently



$$
Y=\det(a,1+t,1)=-\det(a,1,t),\qquad
 R(1)=\det(a,1+t,w).
$$



For Delta=a_1-a_0 and Theta=a_2-a_1, direct expansion gives
det(a,1,t)=S(U,V) and det(a,1,w)=S(U,W). This verifies both signs in
the source's equation(11). An independent exact symbolic expansion of
the nine formal variables also returned zero for each identity.

The whole-remainder identity R(1)=ell_B(W) is valid for degree two.
The exponential tail is sum_j B_j sum_(k>=0)1/(n+k+1-j)!, and the
logarithmic tail is obtained from the exact degree-n projection.
The starting factorials are positive for n sufficiently large; there
is no formal use of a negative factorial. Factorial denominators make
the Taylor-series functionals absolutely convergent even though W
has a pole at t=1.

## 2. Uniform covariance lemma

The lemma's crucial conclusion is of order1/n after cancellation, so
pointwise limits of the uncanceled transforms would be insufficient.
The source does provide the required uniform estimate.

For U_n/U_n(0)=sum u_(n,k)t^k, the reciprocal-root bound gives
|u_(n,k)|<=binom(n+1,k)2^k. For n>=2,



$$
\binom{n+1}{k}(2/n)^k\le3^k/k!.
$$



Also, for q>=0,



$$
\Delta(t^q)=\frac{n+q}{(n+q+1)!},\qquad
 (\Theta-n\Delta)(t^q)
 =\frac{(n+q)q-1}{(n+q+1)!}.
$$



These bounds justify dominated convergence for every fixed shifted
monomial t^mU_n. They give Delta(U_n)~U_n(0)e^(-c)/n! and
r(t^mU_n)-n->m-c. Thus r(U_n)-n is bounded eventually.

For all m>=0 at once, cancellation against r(U_n) yields



$$
\frac{n!}{|U_n(0)|}
 |\Theta(t^mU_n)-r(U_n)\Delta(t^mU_n)|
 \le C(m+1)n^{-m}.
$$



The constant is independent of m and n: after the displayed monomial
identities, the absolute sum is bounded by
n^(-m) sum_k 3^k(m+k+C')/k!. If |g_(n,m)|<=C''rho^(-m), all m>=2
terms therefore sum to O(n^(-2)) relative to |U_n(0)|/n!, since
n rho tends to infinity. The m=0 covariance term is identically zero.
The m=1 term gives



$$
\frac{\Delta(tU_n)}{\Delta(U_n)}
 \{r(tU_n)-r(U_n)\}=\frac{1+o(1)}n.
$$



Multiplying by g_(n,1)->d proves the desired limit. The denominator
Delta(G_nU_n)/Delta(U_n)=1+O(1/n) is bounded away from zero. This checks
both the cancellation rate and every infinite-sum exchange used in the
lemma. The estimates also hold for the j=0,1,2 un-differenced transforms
after their stated n^(j-1) normalization.

## 3. Hypotheses for U, V, and W

The monic p_(n+1) roots have real part1/2, so their reciprocals have
absolute value at most2. The endpoint-ratio recurrence is contractive
with constant at most1/3. Its differentiated recurrence has the same
contractive coefficient, which proves convergence of both the ratio
and its derivative; it does not assume differentiability of a limit
function without justification. At t=1 this yields a logarithmic
derivative increment sqrt2, and symmetry gives its negative at zero.

Cesaro summation gives the scaled first log derivative. The sum of
squared absolute reciprocal roots is at most4(n+1), so the quadratic
remainder in log(U(z/n)/U(0)) is uniformly O(1/n) on compact z disks.
This verifies the locally uniform exponential limit with c=sqrt2.

The second-kind ratio alpha_n* obeys a backward contraction on a
uniform bounded interval. Fixing a number of backward steps, passing
n to infinity, then letting that number grow proves its limit lambda_-.
This argument requires only the already established strict alternating
signs, not an unproved generic second-kind asymptotic.

For p_n/p_(n+1), the tridiagonal matrix has Hermitian part(1/2)I.
For |t|<=rho<1/2, the real part of the inner product with (tI-J)
has absolute value at least(1/2-rho) times the squared norm. Hence
the inverse norm is at most1/(1/2-rho). Its corner cofactor is precisely
p_n/p_(n+1). This proves uniform analytic bounds on the full fixed disk,
not just at zero or on a real segment.

The source's formulas for G_V and G_W then give G_V(0)=G_W(0)=1.
Their denominators are uniformly separated from zero. Differentiating
them gives d_V=1+1/sqrt2 and d_W=1/sqrt2. In particular the nonzero
constant d_W needed for remainder noncancellation is proved for the
actual W quotient.

## 4. Determinant scale and eventual sign

The covariance result gives



$$
S(U,P)\sim-\frac{d_P}{n}
 \frac{U(0)P(0)}{(n!)^2}e^{-2\sqrt2},\quad P=V,W.
$$



The three functionals ell_j(V) all tend to zero because V(0) is at most
an exponential times a polynomial. Thus the raw cofactor B_0 is
asymptotic to -n U(0)e^(-sqrt2)/n!, nonzero eventually. This proves rank
two and a single projective solution of the full system. Dividing raw
Y by this B_0 gives the stated negative normalized endpoint with factor
n^(-2).

The loose determinant estimate in the source is sufficient:



$$
|\det(a,t,w)|\le Cn^3
 |U(0)V(0)W(0)|/(n!)^3.
$$



Relative to S(U,W), its absolute value is O(n^4 V(0)/n!), which tends
to zero. The possibly exponentially small W(0) cancels from this ratio;
it causes no hidden loss. The estimate therefore excludes cancellation
of the main remainder for all sufficiently large n.

Finally,



$$
W(0)/V(0)=(-1)^{n+1}\epsilon_n(1+\alpha_n^*/b_n)/2.
$$



The factor(1+lambda_-/lambda_+)/2 and the ratio d_W/d_V both equal
sqrt2-1. Together with the minus sign in R/Y this proves the positive
limit after multiplication by (-1)^n. An independent exact algebraic
check of these constants agrees.

## 5. Degree-one corollary and arithmetic scope

For the existing raw degree-one solution, Y=Delta(V) and



$$
R(1)=-\Delta(W)+t_1\ell_0(W)-t_0\ell_1(W).
$$



The two-product correction is factorially smaller than Delta(W), by
the same transform bounds. Hence R/Y~-W(0)/V(0), giving the degree-one
constant sqrt2-1. Its B(0)-normalized endpoint is asymptotic to
e^(-sqrt2)V(0)/n!, which also verifies the proposed endpoint ratio
between the two allocations.

The primitive q_n remains outside these analytic arguments. The
independently checked general interpolation divisor in Section9 of
`hp_b1_special_gcd_and_denominator.md` does show that, for every integral
degree-two triple, each B coefficient is divisible by



$$
\frac{(2n-1)!}{\gcd((2n-1)!,2d_n)},
 \qquad d_n=2^{2n}\operatorname{lcm}(1,\ldots,2n+1).
$$



Thus its nonzero matched endpoint has logarithm at least2n log n-O(n)
before division by the endpoint gcd. Neither that divisibility nor the
new normalized error asymptotic bounds the final reduced denominator.
The source's explicit disclaimer on that point is necessary and correct.
