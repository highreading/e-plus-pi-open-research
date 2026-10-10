> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Degree-two exponential coefficient: eventual normality and the exact evaluated asymptotic

Date: 2026-09-13. Independent continuation from the exact projection in
`unequal_degree_hp_attempt.md`. This note proves statements for all
sufficiently large integers, not extrapolations from a finite degree scan.
The final reduced endpoint denominator remains an arithmetic unknown.

## 1. Result and archive overlap

For the original function



$$
F(z)=4\arctan\frac{z}{2-z},
$$



consider



$$
R=A+Be^z+CF=O(z^{2n+3}),\quad
 \deg A,\deg C\le n,\quad\deg B\le2,
 \quad B(1)=C(1)=Y.
\tag{1}
$$



For every sufficiently large n this system has exactly one projective
solution. Its B(0) is nonzero. Normalize B(0)=1. Then Y<0 and



$$
\boxed{\frac{(-1)^nR(1)}{Y\epsilon_n}
       \longrightarrow(\sqrt2-1)^2>0,}
\tag{2}
$$



where epsilon_n is the positive ordinary logarithmic Padé error from the
b=0 and b=1 notes. In particular the entire evaluated remainder is
nonzero, and



$$
\log|R(1)/Y|=-2n\log(1+\sqrt2)+o(n).
\tag{3}
$$



This is an eventual theorem; no numerical threshold for "sufficiently
large" is claimed. The proof gives limiting positive constants and
uniform domination, so it does establish a single finite threshold.

The prior complete computational archive audit, a renewed text search for
the exact allocation (n,2,n) and quadratic exponential coefficients, and
coordination with the author of the b=1 continuation found no preceding
treatment of this allocation. The general b-by-(b+1) projection and
coefficient amplification are already known in this project and are used
below. Item176 imposes B=C as polynomials and constant A; it does not
cover (1). The composed high-radius function is also different.

## 2. The exact two-row system and whole-remainder identity

Use the verified moment functional and monic polynomials



$$
\mathcal L(P)=\int_{-1}^1P((1+iu)/2)\,du,\qquad
 p_k(t)=\frac{i^kP_k(-i(2t-1))}{\binom{2k}{k}},
$$





$$
h_k=\mathcal L(p_k^2)=\frac{2(-1)^k}{(2k+1)\binom{2k}{k}^2},
 \qquad
 K_n(t,s)=\sum_{k=0}^n\frac{p_k(t)p_k(s)}{h_k}.
\tag{4}
$$



Set U=p_{n+1}, V(t)=K_n(t,1), and, for j=0,1,2,



$$
\ell_j(t^k)=\frac1{(n+k+1-j)!},\quad
 a_j=\ell_j(U),\quad t_j=\ell_j(V).
\tag{5}
$$



The exact projection theorem states that



$$
C^*(t)=-\sum_{j=0}^2B_j\ell_j^{(s)}K_n(t,s),
 \qquad C^*(t)=t^nC(1/t),
\tag{6}
$$



and the only two remaining rows are



$$
\sum_{j=0}^2a_jB_j=0,\qquad
 \sum_{j=0}^2(1+t_j)B_j=0.
\tag{7}
$$



In particular, whenever their cross product is nonzero, a rational
projective solution is



$$
\begin{aligned}
 B_0&=a_1(1+t_2)-a_2(1+t_1),\\
 B_1&=a_2(1+t_0)-a_0(1+t_2),\\
 B_2&=a_0(1+t_1)-a_1(1+t_0).
 \end{aligned}
\tag{8}
$$



Until explicitly dividing by B_0, this note uses the raw scale (8).

Let h(t)=1/(1-t), let H_n be its orthogonal projection onto degree at
most n, and put W=Psi_n=h-H_n. The earlier Christoffel–Darboux proof gives



$$
W(t)=\frac{v_n}{h_n}\frac{p_{n+1}(t)-\alpha_n^*p_n(t)}{1-t},
 \quad v_k=\mathcal L\left(\frac{p_k(t)}{1-t}\right),
 \quad\alpha_n^*=v_{n+1}/v_n<0.
\tag{9}
$$



Write w_j=ell_j(W), with each functional applied to the Taylor series;
these series converge absolutely because of their factorial denominators.
The exact identity R(1)=ell_B(W) follows by subtracting the polynomial
Taylor parts of Be^z and CF. It holds for degree two just as for degree
one: the exponential tail is ell_B(h), and (6) makes the logarithmic tail
minus ell_B(H_n). No first-tail approximation is involved.

For any two such functions P,Q define



$$
\Delta(P)=(\ell_1-\ell_0)(P),\quad
 \Theta(P)=(\ell_2-\ell_1)(P),\quad
 S(P,Q)=\Theta(P)\Delta(Q)-\Delta(P)\Theta(Q).
\tag{10}
$$



Direct expansion of the three-by-three determinants now gives the exact
identities



$$
\boxed{Y=-S(U,V),\qquad
 R(1)=S(U,W)+\det\begin{pmatrix}
 a_0&a_1&a_2\\t_0&t_1&t_2\\w_0&w_1&w_2
 \end{pmatrix}.}
\tag{11}
$$



Both signs in (11) matter: Y is det(a,1+t,1), which is the negative of
det(a,1,t). When the Delta values do not vanish, put r(P)=Theta(P)/Delta(P).
Then S(P,Q)=Delta(P)Delta(Q)(r(P)-r(Q)).

## 3. A factorial-transform covariance lemma

The following elementary lemma provides the cancellation control absent
from a coefficient norm bound.

Let U_n be a degree n+1 polynomial with U_n(0) nonzero. Suppose every
reciprocal root has absolute value at most 2, and



$$
U_n(z/n)/U_n(0)\longrightarrow e^{-c z}
\tag{12}
$$



locally uniformly for a real c. Let G_n be analytic on one fixed closed
disk |t|<=rho>0, with G_n(0)=1, uniformly bounded there, and
G_n'(0)->d. Then, with (5) and (10),



$$
\Delta(U_n)\sim\frac{U_n(0)}{n!}e^{-c},\qquad
 r(U_n)=n-c+o(1),
\tag{13}
$$





$$
\Delta(G_nU_n)/\Delta(U_n)\to1,\qquad
 \boxed{n\{r(G_nU_n)-r(U_n)\}\to d.}
\tag{14}
$$



For each fixed integer m>=0, one has more explicitly



$$
\frac{n!n^m\Delta(t^mU_n)}{U_n(0)}\to e^{-c},
 \qquad r(t^mU_n)-n\to m-c.
\tag{15}
$$



Here the functions need only have convergent Taylor expansions on a disk;
the factorial functional is well defined even outside that disk.

Proof. Write U_n/U_n(0)=sum u_{n,k}t^k. The root bound gives



$$
|u_{n,k}|\le\binom{n+1}{k}2^k.
\tag{16}
$$



Equation (12) gives u_{n,k}/n^k->(-c)^k/k! for every fixed k. On a
monomial t^q the numerator factors defining Delta and Theta are n+q and
(n+q)^2-1, respectively, over (n+q+1)!. Consequently



$$
(\Theta-n\Delta)(t^q)
  =\frac{(n+q)q-1}{(n+q+1)!}.
\tag{17}
$$



The bound n!/(n+q)!<=n^{-q}, together with (16), dominates the relevant
sums by constant multiples of 3^k/k! and (k+m+1)3^k/k!. Termwise limits
therefore prove (15), and (13) follows by taking m=0.

For completeness, the cancellation limit in (14) requires a uniform
remainder estimate, not just pointwise limits. Write G_n=sum g_{n,m}t^m;
Cauchy's estimate gives |g_{n,m}|<=C rho^{-m}. Since r(U_n)-n is bounded,
(16) and (17) give, uniformly for every m>=0 and all sufficiently large n,



$$
\frac{n!}{|U_n(0)|}
 \left|\Theta(t^mU_n)-r(U_n)\Delta(t^mU_n)\right|
 \le C_1(m+1)n^{-m}.
\tag{18}
$$



Indeed the absolute sum is bounded by
n^{-m} sum_k binom(n+1,k)(2/n)^k(m+k+C_2), which is at most the right
side. The analogous bound for Delta omits the factor m+k+C_2.
Thus all m>=2 terms in the covariance numerator contribute O(n^-2)
relative to |U_n(0)|/n!. The m=0 term is exactly zero. By (15), the m=1
term, divided by Delta(U_n), is g_{n,1}(1+o(1))/n. Also
Delta(G_nU_n)/Delta(U_n)=1+O(1/n). This proves (14), including nonvanishing
of all denominators for sufficiently large n. Absolute domination also
justifies every exchange of the two Taylor sums.

## 4. Verifying the lemma's hypotheses for the actual three functions

The recurrence and endpoint symmetry are



$$
p_{k+1}=(t-1/2)p_k+\beta_kp_{k-1},\quad
 \beta_k=\frac{k^2}{4(4k^2-1)},\quad
 p_k(0)=(-1)^kp_k(1),\quad p_k(1)>0.
\tag{19}
$$



The roots of p_{n+1} have real part 1/2, so their reciprocals have
absolute value at most 2. Set



$$
b_n=p_{n+1}(1)/p_n(1),\qquad
 \lambda_+=(1+\sqrt2)/4,\quad\lambda_-=(1-\sqrt2)/4.
$$



The positive recurrence b_n=1/2+beta_n/b_{n-1}, with b_n>=1/2, is
contractive in its preceding entry with derivative at most 1/3.
Since beta_n->1/16, it follows that b_n->lambda_+.
Differentiate the same rational recurrence at t=1. Its derivatives obey
d_n=1-beta_n d_{n-1}/b_{n-1}^2; the contraction proves convergence to
1/(1+(1/16)/lambda_+^2). Hence



$$
\frac{p_{n+1}'(0)}{p_{n+1}(0)}-
 \frac{p_n'(0)}{p_n(0)}\longrightarrow-\sqrt2.
\tag{20}
$$



Cesaro summation gives p_{n+1}'(0)/(n p_{n+1}(0))->-sqrt2. Factoring U
over its roots, the sum of squared absolute reciprocal roots is at most
4(n+1), so the quadratic remainder in log(U(z/n)/U(0)) is O(1/n) on each
compact z set. This proves (12) with c=sqrt2.

The strict alternating signs of v_n and the recurrence (19) imply



$$
0<|\alpha_n^*|
   =\frac{\beta_{n+1}}{1/2+|\alpha_{n+1}^*|}<1/6.
\tag{21}
$$



The maps on the right are also uniformly contractive, with derivative at
most 1/3. Iterating a fixed number of steps, then allowing n and finally
the number of steps to tend to infinity, proves alpha_n^*->lambda_-.

For a fixed disk |t|<=rho<1/2, the quotient p_n(t)/p_{n+1}(t) is uniformly
bounded. One precise proof uses the tridiagonal matrix with diagonal 1/2
and off-diagonal i sqrt(beta_k): its characteristic polynomial is
p_{n+1}, and the corresponding corner resolvent entry is p_n/p_{n+1}.
The Hermitian part of the matrix is (1/2)I, so the inverse norm on this
disk is at most 1/(1/2-rho). This proof controls the whole disk uniformly.

Christoffel–Darboux and (9) now give the normalized quotients



$$
G_V(t):=\frac{V(t)/V(0)}{U(t)/U(0)}
   =\frac{1-b_n p_n(t)/p_{n+1}(t)}{2(1-t)},
\tag{22}
$$





$$
G_W(t):=\frac{W(t)/W(0)}{U(t)/U(0)}
   =\frac{1-\alpha_n^* p_n(t)/p_{n+1}(t)}
    {(1+\alpha_n^*/b_n)(1-t)}.
\tag{23}
$$



Their denominators are uniformly nonzero: b_n>=1/2 and
|alpha_n^*|<1/6 make 1+alpha_n^*/b_n>2/3. Both G values at zero equal1,
and the resolvent bound proves the required uniform analytic bounds.
Using (20), their first derivatives satisfy



$$
G_V'(0)\to d_V=1+1/\sqrt2,
 \qquad G_W'(0)\to d_W=1/\sqrt2.
\tag{24}
$$



For example, writing c_n=alpha_n^*/b_n,
G_W'(0)=1+c_n( p_n'/p_n-p_{n+1}'/p_{n+1})(0)/(1+c_n).
Substitution of c_n->-(sqrt2-1)^2 gives the second limit in (24).

## 5. Determinant asymptotics, endpoint sign, and normality

The covariance lemma applied to (22)–(23) gives



$$
S(U,V)\sim-\frac{d_V}{n}\frac{U(0)V(0)}{(n!)^2}e^{-2\sqrt2},
 \quad
 S(U,W)\sim-\frac{d_W}{n}\frac{U(0)W(0)}{(n!)^2}e^{-2\sqrt2}.
\tag{25}
$$



All factors here are nonzero: V(0)=K_n(0,1)>0, and U(0),W(0) have the
strict signs already specified in the earlier Padé identity.
The same dominated sums prove, for j=0,1,2 and P=U,V,W,



$$
\ell_j(P)\sim\frac{P(0)}{n!}n^{j-1}e^{-\sqrt2}.
\tag{26}
$$



The known elementary estimate V(0)<= (n+1)^2 64^n gives t_j->0. Hence
(8) satisfies B_0~ -n U(0)e^{-sqrt2}/n!, which is nonzero eventually.
The two reduced rows then have rank two, proving full normality of the
original projected system. Equation (11) and (25) show that, after
normalizing B_0=1,



$$
\boxed{Y\sim-\left(1+\frac1{\sqrt2}\right)
       \frac{e^{-\sqrt2}K_n(0,1)}{n^2 n!}<0.}
\tag{27}
$$



The third determinant in (11) cannot alter the leading remainder. A
deliberately loose bound from (26) is



$$
|\det(a,t,w)|\le C n^3
 \frac{|U(0)V(0)W(0)|}{(n!)^3}.
\tag{28}
$$



Its ratio to the nonzero second expression in (25) is at most
C' n^4 V(0)/n!, which tends to zero. Thus (11) proves



$$
\frac{R(1)}Y
   =-\frac{d_W}{d_V}\frac{W(0)}{V(0)}(1+o(1)).
\tag{29}
$$



In the ordinary logarithmic Padé normalization, |v_n|=p_n(1)epsilon_n.
Using V(0)=2p_n(1)p_{n+1}(1)/|h_n| in (9) gives the exact identity



$$
\frac{W(0)}{V(0)}
  =(-1)^{n+1}\epsilon_n\frac{1+\alpha_n^*/b_n}{2}.
\tag{30}
$$



Finally d_W/d_V=sqrt2-1 and (1+lambda_-/lambda_+)/2=sqrt2-1.
Equations (29)–(30) prove (2), including eventual nonvanishing and its
sign. The limits v_{n+1}/v_n->lambda_- and p_{n+1}(1)/p_n(1)->lambda_+
also prove log epsilon_n/n->log|lambda_-/lambda_+|, which is (3).

## 6. Arithmetic meaning and the next useful question

Let q_n be the reduced positive denominator of A(1)/Y. The fully primitive
endpoint form, including every polynomial content and endpoint gcd, is



$$
L_n=q_nR(1)/Y,
 \qquad
 \boxed{\log|L_n|=\log q_n-2n\log(1+\sqrt2)+o(n).}
\tag{31}
$$



No bound on q_n is proved here. The new degree-two coefficient changes the
leading positive constant in the normalized logarithmic error from its
degree-one value to (sqrt2-1)^2, while preserving the same exponential
rate. It adds a factor n^-2 in the B(0)-normalized endpoint (27); the
fixed-b factorial amplification barrier remains. These analytic gains
alone supply no shrinking primitive integer form.

The real new arithmetic object is the explicit pair of rational
three-by-three cofactors. If x_j is the rational endpoint A(1) reconstructed
from B=z^j and C_j^*=-ell_j K_n, then at the raw scale (8)



$$
X=A(1)=\det(a,1+t,x),\qquad Y=-S(U,V),\qquad
 q_n=\operatorname{den}(X/Y).
\tag{32}
$$



The next useful mathematical step is to study cancellation in this pair,
especially the prime-power interaction between the added high row a_j and
the already analyzed endpoint kernel. Displayed coefficient clearers are
not primitive factors. No claim that degree two improves q_n follows from
normality, from (27), or from its constant-factor analytic improvement.

Selected exact algebraic normalization checks are recorded separately in
`hp_b2_endpoint_checks.py` and its JSON output; they do not establish any
asymptotic claim. The proof of (2) is Sections 2–5 alone.

The small-index qualification is necessary: the exact normalized endpoint
is 251/696 at n=2 and 23005/49016 at n=3, both positive. The theorem asserts
an eventual negative sign, not a negative sign at every degree.

## 7. Two useful corollaries, with primitive arithmetic kept separate

### 7.1 Sharpening the degree-one analytic constant

Apply (13)–(14) without the covariance difference to the already proved
degree-one identity
R_1(1)=-Delta(W)+Y_1 ell_1(W), Y_1=Delta(V)/(1+t_1), with B_1(0)=1.
The factorially small Y_1 term vanishes relatively, and (30) gives



$$
\frac{(-1)^nR_1(1)}{Y_1\epsilon_n}\to\sqrt2-1,
 \qquad
 \frac{Y_2}{Y_1}\sim-\frac{1+1/\sqrt2}{n^2}.
\tag{33}
$$



Thus the extra degree gives a constant-factor normalized error improvement
and a polynomially smaller coefficient-normalized endpoint. It does not
improve the normalized error's exponential rate.

### 7.2 An actual reduced-prime exclusion at n=p-1

For every odd prime p, the degree pattern (p-1,2,p-1) is normal and has
nonzero endpoint. In its final reduced endpoint denominator q, one has



$$
\boxed{p\nmid q.}
\tag{34}
$$



This holds even below the eventual analytic threshold. Here is the full
local proof. Work over the rationals integral at p. The independently
proved boundary kernel identity in `hp_b1_prime_folding_independent_review.md`
is



$$
K_{p-1}(t,s)/p\equiv\frac{\chi_p}{2}(t-s)^{p-1}\pmod p,
 \qquad\chi_p=(-1)^{(p-1)/2}.
\tag{35}
$$



The kernel has coefficients divisible by p. For j=0,1,2 all factorials in
ell_j(K) have index p+k-j<2p, so their p-adic valuation is at most one.
Thus each elementary projection C_j^*=-ell_j K is p-integral, as are t_j
and the rational reconstructed endpoint x_j: the exponential Taylor
factorials through p-1 and the Taylor denominators of F through p-1 are
p-units. This proves integrality of X once a p-integral B is selected.

At t=1 every coefficient of (35) equals chi_p/2 modulo p. Wilson's theorem
therefore gives, with E_m=sum_(k=0)^m 1/k! modulo p,



$$
t_j\equiv-\frac{\chi_p}{2}E_{p-1-j}\pmod p,
 \quad j=0,1,2,
 \qquad t_2-t_1\equiv\chi_p/2\ne0.
\tag{36}
$$



Indeed the k<j terms have p-integral factorial inverses and retain the
factor p from the kernel; the other terms use p/(p+d)! = -1/d! modulo p.
For j=2 and p=3 the final sum is E_0, so this includes the smallest case.

The monic polynomial U=p_p is p-integral and satisfies



$$
p_p(t)\equiv t^p-1/2\pmod p.
\tag{37}
$$



One may obtain this from P_p(x)=x^p modulo p and binom(2p,p)=2 modulo p.
In a_0=ell_0(p_p), the leading term 1/(2p)! is the only term whose
denominator has p-adic valuation two. All other terms have valuation at
least minus one; and every term of a_1,a_2 also has valuation at least
minus one. Consequently



$$
p^2(a_0,a_1,a_2)\equiv(1/2,0,0)\pmod p,
\tag{38}
$$



since (2p)!/p^2=2 modulo p. Scale the cross product (8) by p^2. Its entries
are p-integral, and the sum of those entries reduces to



$$
p^2Y\equiv\frac{t_1-t_2}{2}=-\chi_p/4\ne0\pmod p.
\tag{39}
$$



The two-row matrix has rank two, the endpoint is nonzero, and p^2X is
p-integral by the previously proved integrality of the elementary x_j.
Thus X/Y is p-integral, which is precisely (34), including all endpoint
cancellations. The prime 2 is not covered; its n=1 would not satisfy b<=n.

This single-prime exclusion is not a denominator growth theorem. In
particular it does not override the factorial raw-endpoint divisibility
proved by the general moment-interpolation argument elsewhere in this
session.
