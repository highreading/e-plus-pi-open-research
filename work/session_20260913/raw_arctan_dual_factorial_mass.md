> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Factorial absolute mass and a later positive kernel for the actual raw family

Date: 2026-09-13. Original quantitative continuation of
`raw_arctan_positive_kernel_attempt.md`. The estimates concern the
actual endpoint-matched family; they do not prove small linear forms.

## 1. Statement and notation

Use the raw monic Legendre polynomials Q_k, their Borel transforms F_k,
norms h_k, and kernels G_k from the positive-kernel note. Normalize the
canonical degree-(n,n,n) family by B_n(1)=1, and put



$$
P_n(x)=\sum_{j=0}^n B_{n,j}\frac{(1-x)^{n-j}}{(n-j)!},\qquad
 M_n=\int_0^1|P_n(x)|\,dx.
$$



The exact equations are



$$
\int_0^1P_nF_k=0\quad(n+1\le k\le2n-1),\qquad
 \int_0^1P_n T_n=-4,
\tag{1}
$$



where T_n=\mathcal B(K_n(1,t)). This note proves



$$
\boxed{M_n\ge
 \frac{n!}{n^2(n+1)(2n+1)(32e^3)^n}\quad(n\ge4).}
\tag{2}
$$



In particular log M_n>=n log n-O(n). The constant is deliberately
coarse; the factorial scale, rather than its exponential constant, is
the useful conclusion.

There is also an exact later-index whole-remainder formula



$$
\boxed{R_n(1)=\int_0^1P_n(x)G_{2n-1}(x)\,dx\quad(n\ge1),}
\tag{3}
$$



whose positive kernel satisfies uniformly on [0,1]



$$
\log G_{2n-1}(x)=2n\log(\sqrt2-1)+o(n).
\tag{4}
$$



Thus the actual signed polynomial has at least factorial absolute mass,
while its normalized remainder depends on strong signed cancellation.
Section7 proves that the high orthogonality automatically forces
vartheta_n<=exp(O(n))/n!. This cancellation is therefore established,
rather than an additional unproved requirement. Its precise size and
the product M_n vartheta_n remain uncontrolled.

## 2. Spectral interpolation of the Borel polynomials

For parity sigma in {0,1}, put q_{k,sigma}=[t^sigma]Q_k(t)>0 when
k=sigma mod2, and lambda_k=k(k+1). Define



$$
p_{r,\sigma}(\lambda)=
 \prod_{a=0}^{r-1}
   [\lambda-(2a+\sigma)(2a+\sigma+1)].
$$



The raw Legendre equation, or its coefficient recurrence, gives the
exact finite expansion



$$
\frac{F_k(x)}{q_{k,\sigma}}=
 \sum_{r\ge0}
 \frac{p_{r,\sigma}(\lambda_k)}{((2r+\sigma)!)^2}
 x^{2r+\sigma}.
\tag{5}
$$



It is finite because the product first acquires a zero factor as soon
as 2r+sigma>k. Each p_r is monic of degree r.

Fix n>=4. Let h_0<...<h_(m-1) be the indices of this parity in
[n+1,2n-1]. Both parity sets are nonempty. For a low index k<=n of the
same parity, let l_j(lambda_k) be the Lagrange weights for interpolation
at lambda_(h_j), and set



$$
I_k(x)=\sum_{j=0}^{m-1}l_j(\lambda_k)
              \frac{F_{h_j}(x)}{q_{h_j,\sigma}},\qquad
 E_k(x)=\frac{F_k(x)}{q_{k,\sigma}}-I_k(x).
$$



Because interpolation is exact on each p_r for r<m, E_k has no
monomial below degree d=2m+sigma. The two possible d's are n-2,n+1
when n is even, and n-1,n when n is odd. In every case



$$
n-2\le d\le n+1,\qquad m\le n/2.
\tag{6}
$$



## 3. Uniform size of the interpolation error

For j!=a, since h_j-h_a=2(j-a),



$$
|\lambda_{h_j}-\lambda_{h_a}|
 =2|j-a|(h_j+h_a+1)\ge4n|j-a|.
$$



Every low-to-high numerator |lambda_k-lambda_(h_a)| is at most4n^2.
Consequently



$$
\sum_{j=0}^{m-1}|l_j(\lambda_k)|
 \le \frac{(2n)^{m-1}}{(m-1)!}\le e^{2n}.
\tag{7}
$$



For any index l<=2n-1 of this parity, the factors defining p_r(lambda_l)
are nonnegative and at most4n^2 until the product becomes zero.
Therefore



$$
|p_{r,\sigma}(\lambda_l)|\le(4n^2)^r.
$$



The coefficients of E_k below r=m vanish, and the remaining ones are
bounded using (7). For r>=m the ratio of two consecutive majorants is



$$
\frac{4n^2}{(2r+\sigma+1)^2(2r+\sigma+2)^2}
 \le\frac4{(n-1)^2}<\frac12\quad(n\ge4).
$$



Hence, uniformly for 0<=x<=1,



$$
|E_k(x)|\le
 2(1+e^{2n})\frac{(4n^2)^m}{(d!)^2}.
\tag{8}
$$



Using (6), 4^m<=2^n, n^(2m)<=n^d,
n^d/d!<=e^n, and n!/d!<=n^2, we obtain



$$
\boxed{\|E_k\|_\infty\le
       \frac{4n^2(2e^3)^n}{n!}.}
\tag{9}
$$



All bounds are uniform in the chosen low index and its parity. No
claim about the sign of E_k or a collocation determinant is used.

## 4. The normalization kernel is factorially close to the high span

Write the low-index kernel exactly as



$$
T_n(x)=\sum_{k=0}^n a_k
                 \frac{F_k(x)}{q_{k,k\bmod2}},\qquad
 a_k=\frac{Q_k(1)q_{k,k\bmod2}}{h_k}.
$$



Since the raw recurrence has positive coefficients and beta_k<=1/3,
Q_k(1)<=2^k, and q_(k,sigma)<=Q_k(1). The exact norm gives



$$
|h_k|^{-1}=
 \frac{(2k+1)\binom{2k}{k}^2}{4^k}\le(2k+1)4^k.
$$



Thus



$$
\sum_{k=0}^n|a_k|\le(n+1)(2n+1)16^n.
$$



Let S_n=sum a_k I_k; it belongs to the actual high span
span(F_(n+1),...,F_(2n-1)). Applying (9) gives



$$
\boxed{\|T_n-S_n\|_\infty\le
 \frac{4n^2(n+1)(2n+1)(32e^3)^n}{n!}.}
\tag{10}
$$



Since P_n annihilates S_n, (1) and the elementary integral norm inequality
give 4=|integral P_n(T_n-S_n)|<=M_n||T_n-S_n||_infinity. This proves(2).
The result is a quantitative statement about the selected normalized
family, not merely a general possibility of large polynomial norms.

## 5. Using every exact high row in the positive-kernel formula

For all integers m>=n,



$$
\Psi_n-\Psi_m=
 \sum_{k=n+1}^m\frac{v_k}{h_k}Q_k,
 \qquad v_k=\mathcal L(Q_k/(1-t)).
$$



At m=2n-1 all terms on the right are annihilated by the actual ell_B.
The beta/Borel identity therefore proves (3). The previously independently
audited uniform estimate for G_m, applied to m=2n-1, proves (4).
This change of index requires no infinite orthogonal expansion and
has no convergence issue.

Define the cancellation ratio specifically for this later kernel by



$$
\vartheta_n=
 \frac{|\int_0^1P_nG_{2n-1}|}
 {\int_0^1|P_n|G_{2n-1}}\in[0,1].
$$



For every nonzero evaluated form, the exact arithmetic normalization
L_n=q_n R_n(1) then gives



$$
\boxed{\log|L_n|=\log q_n+2n\log(\sqrt2-1)
                  +\log M_n+\log\vartheta_n+o(n).}
\tag{11}
$$



The uniform kernel estimate makes the o(n) valid even though P_n varies
with n and changes sign. It is a different cancellation ratio from the
one attached to G_n in the earlier note.

For example, if |R_n(1)| remains bounded on a subsequence, then (2),
(4) and its definition force



$$
\vartheta_n\le\frac{\exp(O(n))}{n!}
$$



on that subsequence. This is a necessary condition, not an impossibility:
the defining orthogonality can create precisely such cancellation.
The pairwise-distinct rational theorem ensures at most one zero value,
but gives no quantitative lower bound for vartheta_n.

## 6. Remaining mathematical target

An upper bound that makes M_n small is now ruled out on the factorial
scale. A proof of primitive shrinking must instead estimate the actual
product M_n vartheta_n accurately enough to compare with q_n. The useful
next determinant problem is a quantitative estimate for the residual
functional on the two-dimensional polynomial space annihilating the
high rows, after imposing both endpoint normalizations. Positivity of
G_m and finite-dimensional normality alone do not estimate that value.

## 7. The factorial cancellation is automatically forced

In fact the same interpolation proves the complementary quantitative
statement



$$
\boxed{\operatorname{dist}_{\infty,[0,1]}
 (G_{2n-1},\operatorname{span}(F_{n+1},\ldots,F_{2n-1}))
 \le\frac{\exp(O(n))}{n!},\qquad
 \vartheta_n\le\frac{\exp(O(n))}{n!}.}
\tag{12}
$$



The implied constants are independent of n. This does not give a
lower bound for vartheta_n or an upper bound for M_n.

First, the exact finite identity



$$
G_N-G_M=\sum_{k=N+1}^M(v_k/h_k)F_k
$$



and the already proved uniform decay G_M->0 on [0,1] show that



$$
G_N(x)=\sum_{k>N} b_k f_k(x),\qquad
 f_k=F_k/q_{k,k\bmod2},\quad
 b_k=(v_k/h_k)q_{k,k\bmod2}>0,
\tag{13}
$$



uniformly there. Thus no infinite orthogonal expansion theorem is
needed to establish this series identity.

Here is a uniform elementary bound for its weights. The square identity
used in the positive-kernel note gives



$$
0<v_k/h_k\le1/Q_k(1).
$$



Indeed the ratio of its integral to h_k is a positive weighted average
of 1/(1+u^2), which is at most1. Set alpha=(1+sqrt2)/2 and
eta=sqrt2-1=1/(2alpha). Since beta_k>=1/4 and alpha^2=alpha+1/4,
the recurrence gives Q_k(1)>=alpha^(k-1). For even k,



$$
q_{k,0}=\frac{\binom{k}{k/2}}{\binom{2k}{k}}
 \le(2k+1)2^{-k}.
$$



For odd k, the exact coefficient formula gives
q_(k,1)=k^2 q_(k-1,0)/(2k-1). Therefore in both parities



$$
\boxed{0<b_k\le4\alpha(k+1)^2\eta^k.}
\tag{14}
$$



Now extend the same interpolation I_k,E_k of Section2 to all k>=2n.
The coefficients below r=m still cancel exactly. Let c=-log eta>0.
The Lagrange weights now obey



$$
L(k):=\sum_j|l_j(\lambda_k)|
 \le\frac{((k+1)^2/(2n))^{m-1}}{(m-1)!}.
\tag{15}
$$



For every r the coefficient of E_k at x^(2r+sigma) is bounded in
absolute value by



$$
\frac{(k+1)^{2r}+L(k)(4n^2)^r}{((2r+\sigma)!)^2},
\tag{16}
$$



and is zero when r<m. This uses the nonnegative factors in p_r until
they become zero, exactly as in Section3.

For any integer s>=0 the elementary integral comparison gives



$$
\sum_{k\ge0}(k+1)^s e^{-ck}
 \le e^{2c}\int_0^\infty x^s e^{-cx}\,dx
 =e^{2c}\frac{s!}{c^{s+1}}.
\tag{17}
$$



Combining (14), (16), and (17), the total contribution of the first
term in (16) to sum_(k>=2n) b_k||E_k|| is bounded by



$$
C\sum_{r\ge m}
 \frac{(2r+2)!}{c^{2r+3}((2r+\sigma)!)^2}
 \le C\sum_{r\ge m}
 \frac{(2r+2)^2 c^{-2r-3}}{(2r)!}
 \le\frac{\exp(O(n))}{n!}.
\tag{18}
$$



For the last inequality use the exponential-series tail and 2m>=n-2.
More explicitly, for fixed A>0 and integer D,
sum_(j>=D)(j+2)^2 A^j/j! is at most
C_A(D+2)^2 A^D/D!, so its logarithm is -log(D!)+O(D).

For the second term of (16), (14), (15), and (17) give



$$
\sum_{k\ge2n}b_kL(k)
 \le C\frac{(2m)!c^{-2m-1}}
 {(2n)^{m-1}(m-1)!}=\exp(O(n)).
\tag{19}
$$



Indeed (2m)!/(m-1)!<=(2m)^(m+1)<=n^(m+1), so the quotient
apart from c-powers is at most n^2/2^(m-1). Multiplying (19) by
sum_(r>=m)(4n^2)^r/((2r+sigma)!)^2, which is exp(O(n))/n! by
Section3, proves the same bound for the second contribution.

Consequently sum_(k>=2n)b_k E_k converges absolutely in the sup norm,
with norm exp(O(n))/n!. Equation(19) also proves convergence of each
coefficient in sum b_k I_k, so this sum belongs to the finite-dimensional
actual high span. Together with (13), these facts prove the distance
bound in (12).

Finally, P_n annihilates that approximant. Hence



$$
|R_n(1)|\le M_n\frac{\exp(O(n))}{n!},\qquad
 \int_0^1|P_n|G_{2n-1}\ge M_n\min_{[0,1]}G_{2n-1}.
$$



The minimum is exp(-O(n)) by (4); division proves the claimed bound
for vartheta_n. This division is legitimate because M_n>0 and the
kernel is strictly positive, including when R_n(1)=0.

The paired results M_n>=n!exp(-O(n)) and
vartheta_n<=exp(O(n))/n! exhibit the two automatically opposing
factorial scales. They do not estimate their product or its remaining
exponential rate. In particular (12) does not establish primitive
shrinking and does not bound the final rational denominator q_n.
