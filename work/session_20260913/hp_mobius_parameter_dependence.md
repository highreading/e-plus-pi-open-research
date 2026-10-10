> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact Möbius-parameter dependence in degree-(n,1,n) endpoint matching

Date: 2026-09-13. This is an auxiliary construction theorem, not a proof
about the rationality of e+pi.

## Outcome and archive overlap

The real parameter in



$$
F_b(z)=4\arctan\frac{z}{1+b-bz},\qquad b\ge0,
 \qquad F_b(1)=\pi
$$



is redundant for the **pure diagonal pi Padé endpoint approximant**, but
is **not redundant for the anchored degree-(n,1,n) Hermite–Padé problem**
with e^z kept fixed. An exact degree-two identity below proves that its
final reduced rational endpoint and denominator change with b.

For every fixed rational b>0, the matched family is eventually normal,
its endpoint is nonzero, and its normalized remainder satisfies



$$
\frac{(-1)^nR(1)}{Y\epsilon_n}\longrightarrow
 k(b):=\frac{b+\sqrt{1+b^2}+1-\sqrt2}
 {b+\sqrt{1+b^2}+1+\sqrt2}>0.
$$



Here epsilon_n is the same pure pi Padé error for every b. Section 5 first
gives an independent half-plane proof on b>1/3; section 7 then proves this
stronger result for every fixed positive b using the factorial-transform
lemma from `hp_b2_endpoint_attempt.md`. The exponential error rate is
always -2log(1+sqrt(2)). A possible asymptotic improvement from this
parameter must therefore come from the **actual reduced endpoint
denominator**. No favorable denominator estimate is obtained here.

Archive search/read dependencies: `sources/pi_g_function_pullback_route.md`
section 3 already proves that b=1 uniquely maximizes the Taylor radius
(1+b)/sqrt(1+b^2), with maximum sqrt(2). The original
`sources/endpoint_matched_mobius_hp_rank_and_content.md` works with that
fixed pullback. `unequal_degree_hp_attempt.md` and
`hp_b1_endpoint_attempt.md` vary the degree of the exponential coefficient,
not this Möbius parameter. No preceding general-parameter endpoint formula
was found in those sources or the targeted archive searches. This is not
a claim to have reread every archive file for every possible synonym.
Here b always means the Möbius parameter; the degree of B is always one.

## 1. Exact vertical measure, polynomials, and kernel

Put a=1+b. Define



$$
\mathcal L_b(P)=\frac2a\int_{-1}^1
 P\left(\frac{b+iu}{a}\right)du.
 \tag{1}
$$



The prefactor 2/a is necessary. Direct integration or differentiation
gives



$$
F_b(z)=z\mathcal L_b((1-tz)^{-1}),\qquad
 F_b'(z)=\frac{4a}{(a-bz)^2+z^2}.
 \tag{2}
$$



Let P_k be the ordinary Legendre polynomial and define the monic
orthogonal polynomials and their nonzero squared norms by



$$
p_{k,b}(t)=\frac{(2i/a)^k}{\binom{2k}{k}}
 P_k(-i(at-b)),\qquad
 h_{k,b}=\frac{4(-4)^k}{a^{2k+1}(2k+1)\binom{2k}{k}^2}.
 \tag{3}
$$



All coefficients are rational when b is rational. Orthogonality follows
by substitution into the ordinary Legendre integral, including its
normalization 2/(2k+1). Set



$$
S_b(t)=\frac{at-b+1}{2},\qquad S_b(1)=1.
$$



Comparison with the fixed b=1 objects gives exactly



$$
p_{k,b}(t)=(2/a)^k p_{k,1}(S_b(t)),\qquad
 h_{k,b}=(2/a)^{2k+1}h_{k,1}.
 \tag{4}
$$



The reproducing kernel on polynomials of degree at most n consequently
satisfies



$$
K_{n,b}(t,s)=\sum_{k=0}^n\frac{p_{k,b}(t)p_{k,b}(s)}{h_{k,b}}
 =\frac a2 K_{n,1}(S_b(t),S_b(s)).
 \tag{5}
$$



This identity includes its scalar factor. Its endpoint specialization is
K_(n,b)(1,s)=(a/2)K_(n,1)(1,S_b(s)). In particular S_b(0)=(1-b)/2,
so the value sampled by the factorial contractions changes with b.

## 2. What is invariant: the pure diagonal pi Padé endpoint

Let N_(n,0)/D_(n,0) be the canonical diagonal Padé approximant of
4arctan(z), with D_(n,0)(0)=1 and both degree bounds at most n. For
w=z/(a-bz), define



$$
D_{n,b}(z)=\frac{(a-bz)^n}{a^n}D_{n,0}(w),\qquad
 N_{n,b}(z)=\frac{(a-bz)^n}{a^n}N_{n,0}(w).
 \tag{6}
$$



Both expressions are polynomials of degree at most n; D_(n,b)(0)=1.
Their remainder has order at least 2n+1 at zero, since w has a simple
zero there. Nonzero Legendre norms give the canonical denominator
D_(n,b)(z)=z^n p_(n,b)(1/z); in particular its value at one is positive.
The possible parity-related drop in its actual degree when b=0 does not
invalidate these degree bounds or the transformation.

Since a-b=1, evaluation at one gives the exact identities



$$
\frac{N_{n,b}(1)}{D_{n,b}(1)}
 =\frac{N_{n,0}(1)}{D_{n,0}(1)}=:f_n,\qquad
 D_{n,b}(1)=a^{-n}D_{n,0}(1).
 \tag{7}
$$



Thus the **reduced rational number** f_n, including its reduced
denominator, is independent of b. Raw polynomial endpoint denominators
are not themselves reduced rational denominators.

For the second-kind integral and projection error, put



$$
v_{k,b}=\mathcal L_b\left(\frac{p_{k,b}(t)}{1-t}\right),\quad
 H_{n,b}(t)=\mathcal L_b^{(s)}\left(\frac{K_{n,b}(t,s)}{1-s}\right),
 \quad\Psi_{n,b}(t)=\frac1{1-t}-H_{n,b}(t).
$$



The same change of variable, including 1/(1-t)=(a/2)/(1-S_b(t)), yields



$$
v_{k,b}=(2/a)^k v_{k,1},\qquad
 \Psi_{n,b}(t)=\frac a2\Psi_{n,1}(S_b(t)).
 \tag{8}
$$



In particular v_(n,b)/p_(n,b)(1)=pi-f_n. Write
epsilon_n=|pi-f_n|>0. Its already proved Legendre-square integral estimate
gives log(epsilon_n)/n -> -2log(1+sqrt(2)).

## 3. What changes: exact HP contractions and endpoint denominator

For fixed n define the functionals



$$
\ell_0(t^j)=\frac1{(n+j+1)!},\qquad
 \ell_1(t^j)=\frac1{(n+j)!},\qquad \ell_\Delta=\ell_1-\ell_0.
 \tag{9}
$$



They stay fixed as b varies, because the exponential remains e^z. The
high-order equations in



$$
R=A+B e^z+C F_b=O(z^{2n+2}),\qquad
 \deg A,\deg C\le n,\quad B=B_0+B_1z
 \tag{10}
$$



are equivalent to



$$
C^*(t)=-\ell_B^{(s)}K_{n,b}(t,s),\qquad
 C^*(t)=t^nC(1/t),\quad \ell_B=B_0\ell_0+B_1\ell_1.
 \tag{11}
$$



Indeed the coefficient equations at degrees n+1 through 2n+1 pair C*
against t^j for j=0,...,n under L_b; reproducing the prescribed
factorial functional gives (11). Thus this formula uses every high-order
equation, not just a leading coefficient.

Define



$$
t_j(b)=\ell_j^{(s)}K_{n,b}(1,s),\qquad
 \delta_b=t_1(b)-t_0(b),\qquad
 C_j^*(t)=-\ell_j^{(s)}K_{n,b}(t,s),
$$



reverse C_j* to obtain C_j(z), and put



$$
a_j(b)=-[T_n(z^j e^z+C_j(z)F_b(z))](1),\quad j=0,1.
$$



The matching equation B(1)=C(1) is exactly



$$
(1+t_0(b))B_0+(1+t_1(b))B_1=0.
 \tag{12}
$$



Unless both coefficients in (12) vanish, a projective representative is
B_0=1+t_1(b), B_1=-1-t_0(b), with endpoint pair



$$
X_b=(1+t_1(b))a_0(b)-(1+t_0(b))a_1(b),\qquad
 Y_b=\delta_b.
 \tag{13}
$$



When Y_b is nonzero, the exact rational number x_(n,b)=X_b/Y_b and its
positive reduced denominator q_(n,b) define the primitive form



$$
q_{n,b}(e+\pi+x_{n,b})
 =q_{n,b}\frac{R(1)}{Y_b}.
 \tag{14}
$$



The exact evaluated remainder is



$$
R(1)=\ell_B(\Psi_{n,b}),\qquad
 \frac{R(1)}{Y_b}
 =-\frac{1+t_1(b)}{\delta_b}\ell_\Delta(\Psi_{n,b})
   +\ell_1(\Psi_{n,b}).
 \tag{15}
$$



The functionals on the rational functions are defined by their Taylor
series; the factorially weighted sums converge absolutely. The identity
follows because A cancels the first n+1 Taylor coefficients, the
exponential tail is ell_B(1/(1-t)), and the remaining logarithmic tail is
-ell_B(H_(n,b)). For b>0 the F_b Taylor series converges absolutely at one.
At b=0 the identity also follows by an Abel limit, or by continuity of
these rational-coefficient expressions in b and the endpoint pi. Equations
(5), (8), and (15) are exact parameter dependence of the evaluated error.

For an integer ledger take b=r/s in lowest terms, r>=0,s>=1, and A=r+s.
Define the integral polynomial



$$
J_{k,b}(t)=(2s)^k i^k P_k(-i(At-r)/s)\in\mathbb Z[t].
$$



The usual integral coefficient formula for 2^k P_k verifies integrality.
Then



$$
K_{n,b}(t,u)=\frac A{4s}\sum_{k=0}^n
 \frac{(-1)^k(2k+1)}{(4s^2)^k}J_{k,b}(t)J_{k,b}(u).
 \tag{16}
$$



The final useful ledger is sharper than separately clearing F_b and C_j.
Put H=4^(n+1)(2n+1)! and L_n=lcm(1,...,n), for n>=1. Section 8 proves the
polynomial identities and degree bounds



$$
Ht_j\in\mathbb Z[b],\quad HL_n a_j\in\mathbb Z[b],\qquad
 \deg_b X_b\le2n+1,\quad\deg_b Y_b\le n+1.
$$



Thus D=H^2 L_n s^(2n+1) clears both X_b and Y_b at b=r/s. The powers of
A=r+s that appear if the Taylor coefficients of F_b are cleared on their
own cancel in the actual endpoint formulas. The **exact**,
normalization-safe denominator formula is



$$
q_{n,b}=\frac{|DY_b|}{\gcd(|DX_b|,|DY_b|)}.
 \tag{17}
$$



This is only a common clearer. Its excess factors cancel in the displayed
gcd and must not be counted as arithmetic gain.

## 4. A symbolic counterexample to full projective redundancy

At n=2 the exact endpoint ratio is



$$
x_{2,b}=-\frac{13b^5+b^4+2562b^3-382b^2-191b+3277}
 {32(b+1)(14b^2-17b+17)}.
 \tag{18}
$$



In the normalization (13), Y_b=(b+1)(14b^2-17b+17)/32, which is
strictly positive for b>=0 because the quadratic has negative
discriminant and positive leading coefficient. Thus (18) has not
silently canceled a zero endpoint. The
following are three specializations of this single symbolic identity,
not a parameter scan or an asymptotic inference:

| b | x_(2,b) in lowest terms | q_(2,b) |
|---|---|---|
| 0 | -3277/544 | 544 |
| 1 | -165/28 | 28 |
| 2 | -1715/288 | 288 |

The accompanying checker derives (18) from the kernel, directly checks
all Taylor and matching equations, and independently checks the pure
Padé change of variable. Thus no projective rescaling can identify all
of these HP endpoint pairs: projective rescaling preserves X/Y.

The structural reason is also explicit. Under the inverse coordinate
change z=aw/(1+bw), the exponential becomes
exp(aw/(1+bw)). Clearing the degree-n polynomial factor changes B into
(1+bw)^(n-1)(B_0+(bB_0+aB_1)w). This does not remain the same problem with
the fixed exponential e^w and a degree-one coefficient. Pure logarithmic
Padé covariance therefore cannot be used to remove b in (10).

Small-index degeneracies must still be respected: at n=1,b=1 the actual
matched endpoint has X=Y=0. A removable limit of a symbolic quotient is
not a nonzero primitive form at that index.

## 5. Fixed b>1/3: normality and the unchanged analytic rate

This section proves the stated extension, rather than inferring it from
the three specializations. All constants and thresholds may depend on the
fixed b. No uniform assertion is made as b approaches 1/3 or varies with n.

The monic recurrence is



$$
p_{k+1,b}=(t-b/a)p_{k,b}+\alpha_{k,b}p_{k-1,b},\qquad
 \alpha_{k,b}=\frac{k^2}{a^2(4k^2-1)}\in(1/(4a^2),1/(3a^2)].
 \tag{19}
$$



For b>0 its values satisfy p_(k,b)(1)>0 and
(-1)^k p_(k,b)(0)>0. Every term in K_(n,b)(1,0) is therefore positive.
The roots of p_(k,b) have real part b/a.

Here is the precise fixed-half-plane extension of the factorial sign
lemma proved in `hp_b1_endpoint_attempt.md`. Let c>0, M=1/c, and let Q be
a real polynomial of degree k<=N+1 with all roots of real part at least c.
For all sufficiently large N depending only on M,



$$
e^{-4M}\frac{N|Q(0)|}{(N+1)!}
 \le\operatorname{sign}(Q(0))\ell_{\Delta,N}(Q)
 \le e^{2M}\frac{N|Q(0)|}{(N+1)!},
 \tag{20}
$$



and ell_(1,N)(Q) has the same sign and absolute value at most
e^(2M)|Q(0)|/N!. The ell_(0,N) transform has that sign as well.

For completeness, the reciprocal roots lie in the disk with center M/2
and radius M/2. For the Laguerre symbol
f_(N,k)(z)=sum_j (-1)^j binom(k,j) z^j/(N+2)_j, its roots lambda_i obey
lambda_i>=N/6-1 and sum_i 1/lambda_i<=1. For N>=24M+12, the zeros of
g=Nf+zf' are greater than 2M: on [0,2M], g/f=N-sum_i z/(lambda_i-z)>0,
and Rolle's theorem gives positive interlacing zeros. Also
sum_i 1/gamma_i<=2. Factoring g therefore bounds |g(z)/N| between e^(-4M)
and e^(2M) on |z|<=M. The same bounds apply to ((N+1)f+zf')/(N+1),
and the corresponding simpler bounds apply to f. The
Grace–Walsh–Szegő theorem applies to the symmetric multiaffine
polarization in this convex disk. Moving conjugate reciprocal-root pairs
to its positive real center keeps the value real and nonzero, proving
the sign as well as the absolute bounds. This is the same primary-source
theorem and proof mechanism already verified in the preceding note; no
positivity of the complex measure is assumed.

Apply (20) to each p_(k,b), k<=n. The signs of the summands agree, so



$$
\delta_b\asymp_b K_{n,b}(1,0)/n!,\qquad
 0<t_0(b)<t_1(b)\ll_b K_{n,b}(1,0)/n!.
 \tag{21}
$$



The kernel grows at most exponentially for fixed b, by (19) and (3).
Thus t_1(b)->0. Equation (12) proves eventual uniqueness up to scaling,
and under B_0=1 its endpoint is



$$
Y=\delta_b/(1+t_1(b))>0,\qquad
 Y\asymp_b K_{n,b}(1,0)/n!.
 \tag{22}
$$



To control the evaluated remainder, let



$$
a_{n,b}=v_{n+1,b}/v_{n,b}<0,\qquad
 Q_{n,b}=p_{n+1,b}-a_{n,b}p_{n,b}.
$$



Christoffel–Darboux gives



$$
\Psi_{n,b}(t)=\frac{v_{n,b}}{h_{n,b}}
 \frac{Q_{n,b}(t)}{1-t}.
 \tag{23}
$$



The previously proved b=1 bound |a_(n,1)|<1/6 and (8) imply
|a_(n,b)|<1/(3a). The complex symmetric Jacobi matrix for Q_(n,b) has
Hermitian part diagonal with entries b/a, except the last entry
b/a+a_(n,b). Its roots consequently have real part at least
c_b=(b-1/3)/a>0. This verifies the actual numerator's root hypothesis.

Write P=p_(n,b)(1), P'=p_(n+1,b)(1),
U=(-1)^n p_(n,b)(0), V=(-1)^(n+1)p_(n+1,b)(0), all positive. The recurrence
gives V>=bU/a and P'/P<=4/(3a). Hence



$$
\operatorname{sign}Q_{n,b}(0)=(-1)^{n+1},\qquad
 (1-1/(3b))V\le |Q_{n,b}(0)|\le V,
$$



while Christoffel–Darboux gives K_(n,b)(1,0)=(P'U+PV)/|h_(n,b)|.
Using |v_(n,b)|=P epsilon_n, we obtain the uniform-in-n comparison



$$
\frac{3b-1}{3b+4}\,\epsilon_n
 \le\frac{|\Psi_{n,b}(0)|}{K_{n,b}(1,0)}
 \le\epsilon_n.
 \tag{24}
$$



Apply (20), with c=c_b, to each t^r Q term by instead using Q with
N=n+r. The sum of N/(N+1)! for r>=0 is exactly 1/n!. All terms have the
same sign. Thus ell_Delta(Psi) has the sign of Psi(0) and magnitude
comparable to |Psi(0)|/n!; ell_1(Psi) has the same sign and absolute value
at most e^(2/c_b+1)|Psi(0)|/n!. Since Y tends to zero, the two terms in
R(1)=-ell_Delta(Psi)+Y ell_1(Psi), under B_0=1, cannot cancel for large n.
Its sign is (-1)^n because v_(n,b)/h_(n,b)>0. Combining (22) and (24)
proves



$$
0<c(b)\epsilon_n\le (-1)^n R(1)/Y\le C(b)\epsilon_n
 \quad(n\ge n_0(b)).
 \tag{25}
$$



For additional scale information, positive recurrence comparison in
(19), with alpha_(k,b)->1/(4a^2), gives



$$
\frac1n\log K_{n,b}(1,0)
 \longrightarrow
 \log\bigl((1+\sqrt2)(b+\sqrt{1+b^2})\bigr).
 \tag{26}
$$



Indeed the positive endpoint sequences have respective growth roots
(1+sqrt(2))/(2a) and (b+sqrt(1+b^2))/(2a), whereas
|h_(n,b)|^(1/n)->1/(4a^2). Each kernel summand has the resulting growth
factor, which exceeds one, and the positive sum has the same rate.
Comparison with constant-coefficient recurrences whose second coefficient
is 1/(4a^2) and 1/(4a^2)+eta proves the two sequence limits without any
unproved asymptotic expansion.

The individual factorially small endpoint therefore changes its
geometric factor with b. Its normalized evaluated error still obeys



$$
\log|R(1)/Y|=-2n\log(1+\sqrt2)+o(n),\qquad
 \log|q_{n,b}R(1)/Y|
 =\log q_{n,b}-2n\log(1+\sqrt2)+o(n).
 \tag{27}
$$



This half-plane argument deliberately leaves 0<=b<=1/3 outside its scope:
the present Jacobi half-plane bound no longer proves the requisite
factorial-transform sign there. The exact identities (1)–(18) remain
valid, subject to their explicit endpoint nonvanishing conditions.
Section 7 supplies a different argument for every fixed b>0.

## 6. Exact obstruction and next mathematical step

There is an arithmetic degree of freedom, but no proved improvement in
primitive endpoint size. For any one fixed rational b>0, a theorem
liminf_n log(q_(n,b))/n < 2log(1+sqrt(2)) would, by section 7, yield a nonzero
shrinking subsequence of integer forms in e+pi. Proving such a bound,
or a contrary lower bound for the explicit ratio (13), is the concrete
remaining task. Pure pi Padé invariance neither proves nor rules it out.

Choosing b=b_n introduces a separate arithmetic height cost through the
values of the integer polynomials in r and s underlying (17), although
section 8 removes an artificial (r+s)^n denominator. The constants and
threshold in the analytic theorem also depend on b. An optimization over
varying rational parameters cannot legitimately
use the fixed-parameter estimate as a uniform theorem. No such
optimization or large parameter scan was performed.

Likewise, approximating a real parameter that makes the fixed-degree
normalized remainder small by rational parameters is not by itself an
irrationality proof: the resulting primitive denominator grows with the
parameter's denominator, and (17) must still be controlled. A small real
remainder before this normalization is insufficient.

The bounded exact certificate is `check_hp_mobius_parameter.py`, with
results `hp_mobius_parameter_checks.json`. It verifies the affine kernel,
norms, moments against F_b', all n=2 HP equations, the symbolic endpoint
formula, and the pure diagonal Padé covariance. These algebra checks
support the formulas; the all-n arguments above carry the mathematical
claims.

## 7. Stronger extension: every fixed positive b and its exact constant

This improvement was suggested by root after the half-plane proof above
and independently checked by the reviewer. It uses only the leading
factorial-transform asymptotic already proved in
`hp_b2_endpoint_attempt.md`, not its more delicate covariance difference.
It also avoids asserting that every root of Q_(n,b) lies to the right of
zero when b is small.

Fix b>0 throughout, and write a=1+b. Define



$$
\mu_n=-\frac{p_{n+1,b}(0)}{p_{n,b}(0)}>0,\qquad
 \lambda_n=\frac{p_{n+1,b}(1)}{p_{n,b}(1)}>0,\qquad
 \alpha_n^*=\frac{v_{n+1,b}}{v_{n,b}}<0.
$$



Their limits are



$$
\mu=\frac{b+\sqrt{1+b^2}}{2a},\quad
 \lambda=\frac{1+\sqrt2}{2a},\quad
 \alpha^*=\frac{1-\sqrt2}{2a}.
 \tag{28}
$$



Here is a ratio proof that remains valid for arbitrarily small fixed b.
The origin recurrence is
mu_n=b/a+alpha_(n,b)/mu_(n-1), with alpha_(n,b)->gamma=1/(4a^2).
The positive ratios lie in a fixed compact subinterval of (0,infinity),
because they are at least b/a and at most b/a+1/(3ab). If L and U are
their liminf and limsup, monotonicity and continuity of this decreasing
recurrence give L=b/a+gamma/U and U=b/a+gamma/L. Multiplying by U and L
respectively shows (b/a)U=(b/a)L, so L=U, and the positive quadratic root
is mu. The same argument with b replaced by 1 in the first coefficient
gives lambda. The second-kind limit follows from
alpha_n^*=(2/a)alpha_(n,1)^* and the already verified limit
alpha_(n,1)^*->(1-sqrt(2))/4. In particular mu+alpha^*>0, since
b+sqrt(1+b^2)>1>sqrt(2)-1.

Put U_n(t)=p_(n+1,b)(t). Its reciprocal roots have absolute value at most
a/b. Its small-argument limit is



$$
\frac{U_n(z/n)}{U_n(0)}\longrightarrow e^{-c_b z}
 \quad\text{locally uniformly},\qquad
 c_b=\frac a{\sqrt{1+b^2}}.
 \tag{29}
$$



One elementary derivation of the first logarithmic derivative uses
(1-x^2)P_n'(x)=n(P_(n-1)(x)-xP_n(x)) at x=ib. The monic normalization
in (3) gives exactly, for n>=1,



$$
\frac{p_{n,b}'(0)}{n p_{n,b}(0)}
 =-\frac a{1+b^2}\left(
 b+\frac{n}{a(2n-1)\mu_{n-1}}\right)
 \longrightarrow-\frac a{\sqrt{1+b^2}}.
 \tag{30}
$$



The reciprocal-root bound makes the sum of their squared absolute values
at most (n+1)(a/b)^2. The quadratic remainder in the logarithm of
U_n(z/n)/U_n(0) is therefore O_b(1/n), uniformly on every compact z set.
This proves (29) from (30), including local uniformity.

For clarity, the portion of the factorial-transform lemma needed here
has the following precise form. If a degree n+1 polynomial U_n has a
fixed reciprocal-root bound L, and normalized limit (29), and G_n is
uniformly analytic and bounded on a fixed disk around zero with G_n(0)=1,
then



$$
\Delta(G_nU_n)\sim\frac{U_n(0)e^{-c_b}}{n!},\qquad
 \ell_1(G_nU_n)\sim\frac{U_n(0)e^{-c_b}}{n!}.
 \tag{31}
$$



There is no requirement that the zeros of G_nU_n satisfy a half-plane
bound. To check that the earlier lemma's reciprocal bound 2 can be
replaced by any fixed L, write U_n/U_n(0)=sum_k u_(n,k)t^k. Then
|u_(n,k)|<=binom(n+1,k)L^k and u_(n,k)/n^k->(-c_b)^k/k!.
The factorial bound n!/(n+k)!<=n^(-k) dominates the relevant sums by a
constant multiple of (2L)^k/k!. Cauchy's coefficient bound for G_n on
its fixed disk makes its terms of positive order contribute O_b(1/n)
relative to |U_n(0)|/n!. This proves (31) and justifies both Taylor-sum
interchanges. Its nonzero leading term supplies eventual nonvanishing.

Let V_n=K_(n,b)(t,1) and W_n=Psi_(n,b). Their normalized quotients by U_n
are exactly



$$
G_{V,n}(t)=\frac{V_n(t)/V_n(0)}{U_n(t)/U_n(0)}
 =\frac{1-\lambda_n p_{n,b}(t)/p_{n+1,b}(t)}
 {(1+\lambda_n/\mu_n)(1-t)},
 \tag{32}
$$





$$
G_{W,n}(t)=\frac{W_n(t)/W_n(0)}{U_n(t)/U_n(0)}
 =\frac{1-\alpha_n^* p_{n,b}(t)/p_{n+1,b}(t)}
 {(1+\alpha_n^*/\mu_n)(1-t)}.
 \tag{33}
$$



The scalar denominators in these formulas are bounded away from zero
for large n by (28); W_n(0) is consequently nonzero then. Choose a fixed
rho with 0<rho<min(1,b/a). The tridiagonal matrix whose characteristic
polynomial is p_(n+1,b) has diagonal b/a and purely imaginary symmetric
off-diagonal entries i sqrt(alpha_(k,b)). Its Hermitian part is (b/a)I.
For |t|<=rho, its inverse has norm at most 1/(b/a-rho), as follows by
taking the real part of the corresponding quadratic form. Its corner
resolvent entry is p_(n,b)(t)/p_(n+1,b)(t). Thus (32) and (33) are uniformly
analytic and bounded on that disk, and both equal 1 at zero. All
hypotheses of (31) are now verified for the actual V_n and W_n.

It follows that



$$
\Delta(V_n)\sim V_n(0)e^{-c_b}/n!,\quad
 \Delta(W_n)\sim W_n(0)e^{-c_b}/n!,\quad
 \ell_1(W_n)\sim W_n(0)e^{-c_b}/n!.
 \tag{34}
$$



The positive kernel V_n(0) grows at most exponentially by (19) and (3),
so t_1=ell_1(V_n)->0. The matching row is consequently nonzero for
large n, B_0 can be normalized to 1, and
Y=Delta(V_n)/(1+t_1) is positive and asymptotic to
V_n(0)e^(-c_b)/n!. Using the exact degree-one identity (15) gives



$$
\frac{R(1)}Y
 =-(1+t_1)\frac{\Delta(W_n)}{\Delta(V_n)}+\ell_1(W_n)
 =-\frac{W_n(0)}{V_n(0)}(1+o(1)).
 \tag{35}
$$



The last term is relatively negligible because its ratio to W_n(0)/V_n(0)
is asymptotic to V_n(0)e^(-c_b)/n!, which tends to zero. Thus this step
controls the entire evaluated remainder, including its potentially
cancelling terms.

Finally the exact Christoffel–Darboux identities give



$$
\frac{W_n(0)}{V_n(0)}
 =(-1)^{n+1}\epsilon_n
 \frac{\mu_n+\alpha_n^*}{\mu_n+\lambda_n}.
 \tag{36}
$$



Substituting (28) into (35)–(36) proves the strengthened theorem



$$
\boxed{\frac{(-1)^nR(1)}{Y\epsilon_n}\longrightarrow
 \frac{b+\sqrt{1+b^2}+1-\sqrt2}
 {b+\sqrt{1+b^2}+1+\sqrt2}=k(b)>0.}
 \tag{37}
$$



In particular k(1)=sqrt(2)-1, agreeing with the independently proved
fixed-map result in section 7.1 of the degree-two note. As b decreases
to zero through fixed positive values, k(b) tends to (sqrt(2)-1)^2;
as b tends to infinity, it tends to 1. These are limits of the **constant
in a fixed-parameter theorem**, not a theorem allowing b to vary with n.
The proof supplies no uniform threshold as b approaches zero: its
reciprocal-root bound a/b and its resolvent disk both degenerate. It does
not assert the same formula at b=0, where origin values of the Legendre
polynomials have parity zeros.

Consequently all fixed positive rational parameters have the same
normalized exponential rate, with the precise constant (37), while
their actual rational endpoint denominators differ by (13), (17), and
(18). This sharpens the analytic conclusion without resolving its
primitive denominator problem.

## 8. Polynomial endpoint structure and the final parameter-height ledger

The following refinement was checked independently by root and the
reviewer. It removes the artificial denominator from the low Taylor
products and proves the actual degrees of the endpoint rational map.

Write V_b(t)=K_(n,b)(t,1), and define the polynomial



$$
\mathcal J_b(t)=\pi V_b(t)-H_{n,b}(t).
$$



It has rational coefficients for rational b, and in fact polynomial
dependence on b over Q. To see rationality without assuming it, note that



$$
v_{k,b}=\pi p_{k,b}(1)
 -\mathcal L_b\left(\frac{p_{k,b}(1)-p_{k,b}(t)}{1-t}\right).
$$



The last integrand is a polynomial with rational coefficients and the
moments of L_b are rational. The pi coefficient in H_(n,b) is therefore
exactly V_b. Equations (5) and (8) give



$$
V_b(t)=\frac a2 V_1(S_b(t)),\qquad
 \mathcal J_b(t)=\frac a2\mathcal J_1(S_b(t)).
 \tag{38}
$$



Both fixed polynomials on the right have t-degree at most n. Their
coefficients as polynomials in b have degree at most n+1.

Let E_m=sum_(k=0)^m 1/k!. The exact whole-tail identity for the elementary
coefficient B=z^j, j=0,1, reads
a_j+e-pi t_j=ell_j(h-H_(n,b)), whereas ell_j(h)=e-E_(n-j).
Consequently



$$
a_j=-E_{n-j}+\ell_j(\mathcal J_b),\qquad
 t_j=\ell_j(V_b).
 \tag{39}
$$



Thus both a_j and t_j have degree at most n+1 in b. More is true for the
endpoint determinant X=(1+t_1)a_0-(1+t_0)a_1. For any fixed polynomial
P of degree at most n, the coefficient of b^(n+1) in
(a/2)P(S_b(t)) is a scalar multiple of (t-1)^n, including the possibility
of the zero multiple if P has lower degree. Therefore the leading
coefficient pairs of (a_0,a_1) and (t_0,t_1) are proportional to the same
pair (ell_0((t-1)^n),ell_1((t-1)^n)). The coefficient of b^(2n+2) in
t_1a_0-t_0a_1 vanishes identically. Since a_0-a_1 has degree at most n+1,



$$
\boxed{\deg_b X\le2n+1,\qquad \deg_b Y\le n+1.}
 \tag{40}
$$



This conclusion includes all degree-drop cases and requires only n>=1.
It explains the degree-five over degree-three shape in (18).

For the coefficient denominator, the Legendre formula also gives



$$
K_{n,b}(t,u)=\frac a4\sum_{k=0}^n(2k+1)
 P_k(-i(at-b))P_k(-i(au-b)).
 \tag{41}
$$



Since 2^k P_k is an integral polynomial, 4^(n+1) clears the rational
coefficients in b,t,u. The coefficient of t^(n-l) additionally has the
polynomial factor a^(n-l+1). Applying a factorial functional shows



$$
Ht_j\in\mathbb Z[b],\qquad
 H[z^l]C_j(z)/a^{n-l+1}\in\mathbb Z[b],\quad
 H=4^{n+1}(2n+1)!.
 \tag{42}
$$



For the low product C_jF_b, its coefficient involving z^l from C_j and
z^k from F_b has l+k<=n and k>=1. The exact coefficient



$$
[z^k]F_b(z)=\frac{4\operatorname{Im}(b+i)^k}{k a^k}
$$



therefore cancels against a^(n-l+1) in (42), leaving a nonnegative power
at least one. Only the integer denominator k remains beyond H. The
exponential Taylor coefficients through n have denominators dividing H.
Thus HL_n a_j belongs to Z[b], with L_n=lcm(1,...,n), as asserted above.
It follows that H^2 L_n X and H Y are integer polynomials.

At b=r/s in lowest terms, (40) proves that



$$
\boxed{D_{n,b}=H^2 L_n s^{2n+1}}
 \tag{43}
$$



clears both endpoint numbers. Formula (17) with this D is the final
ledger. It records all cancellations arising solely from the Möbius
substitution and the polynomial degree, and still leaves the actual
gcd of the evaluated endpoint integers to be determined. None of these
identities proves a favorable asymptotic size for q_(n,b).
