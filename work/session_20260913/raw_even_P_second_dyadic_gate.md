> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Both even-degree P gates from the actual moment equations

Date: 2026-09-13. Original continuation by audit_results.

This note proves, for the actual canonical raw family in every even
degree n>=2, a bound for BOTH coefficients p_1 and p_2 of



$$
P(z)=(1+z^2)(A'C-AC')+C^2,\qquad
p_j=[z^{2n-j}]P,\quad p_0=\Xi_n.
$$



Put v=v_2(n), phi(j)=v_2(j!), and epsilon=1 when n=2 modulo4,
zero otherwise. The precise result is



$$
\boxed{v_2(p_s)\ge v_2(\Xi_n)+\min\{n,v+1\},\quad s=1,2.}
\tag{1}
$$



Zero coefficients satisfy the inequality with infinite valuation.
The proof uses the FULL actual reversed C polynomial and the exact
Hermite--Pade moment equations. No approximation by the largest
factorial row set is made. Together with the all-coefficient B
theorem this excludes a triple root of the actual accessory cubic
at every even degree; squarefreeness remains a distinct question.

## 1. Inputs and raw orthogonal normalization

Use the unique canonical triple with B(1)=1, C(1)=4 and
A+B exp(z)+C arctan(z)=O(z^(3n+1)). The independently reviewed inputs
are the B theorem in raw_B_coefficient_dyadic_divisibility.md and
the even Xi theorem in raw_Xi_even_dyadic.md:



$$
v_2(b_j)\ge\phi(n)-\phi(j),\quad 0\le j\le n,
\tag{2}
$$




$$
v_2(c_n)\ge M:=-n-2\phi(n-1)-2\epsilon,
\quad v_2(\Xi_n)=M-n=:K.
\tag{3}
$$



Here a_j,b_j,c_j are ascending polynomial coefficients. The raw
moment functional and its monic orthogonal polynomials are



$$
\mathcal L(f)=\frac12\int_{-1}^1f(iu)\,du,
\qquad Q_0=1,\ Q_1=t,
\quad Q_{j+1}=tQ_j+\frac{j^2}{4j^2-1}Q_{j-1}.
\tag{4}
$$



Write h_j=L(Q_j^2), and
S_j(t)=L_s((Q_j(t)-Q_j(s))/(t-s)). Every Q_j belongs to
Z_(2)[t]. Their norms and the needed central values obey



$$
v_2(h_j)=2\phi(j),\quad Q_{2r}(0)\in\mathbb Z_{(2)}^\times,
\quad Q_{2r+1}'(0)\in\mathbb Z_{(2)}^\times.
\tag{5}
$$



The first statement follows from
h_j=(-1)^j4^j/((2j+1)binom(2j,j)^2). The even central value
is the product of the odd-index coefficients in (4), all units.
For odd j, the exact derivative identity
Q_j'(0)=j^2 Q_(j-1)(0)/(2j-1) gives the last statement.
These statements include Q_0(0)=1 and Q_1'(0)=1.

## 2. Bounds for every coefficient in the orthogonal expansion

Reverse C at its prescribed degree n:



$$
U(t)=t^n C(1/t)=\sum_{j=0}^n u_jQ_j(t).
\tag{6}
$$



The exact high Taylor equations give



$$
\mathcal L(t^kU)=-[z^{n+1+k}](B(z)e^z),
\qquad 0\le k\le2n-1.
\tag{7}
$$



Indeed the coefficient of C arctan(z) at that index is the sum of
c_(n-r) times mu_(k+r), where
mu_a=L(t^a)=0 for odd a and (-1)^(a/2)/(a+1) for even a.
There is no A contribution since the index exceeds n.

For N>=n+1, (2) and the integrality of binomial coefficients give



$$
v_2([z^N]B e^z)\ge\phi(n)-\phi(N).
\tag{8}
$$



Every summand b_j/(N-j)! has at least that valuation because
phi(j)+phi(N-j)<=phi(N). Since Q_j has dyadically integral
coefficients and only powers up to j, (7)--(8) and orthogonality
give the actual, unscaled estimate



$$
\boxed{v_2(u_j)\ge
\phi(n)-\phi(n+1+j)-2\phi(j),\quad 0\le j<n.}
\tag{9}
$$



The right side decreases with j. Its value at j=n-1 is
-n-2phi(n-1), because phi(2n)=phi(n)+n. Thus every u_j with
j<n has valuation at least M. Finally evaluate (6) at zero.
The left side is c_n, whose bound is (3), while Q_n(0) is a unit
because n is even. All lower even terms already have valuation
at least M. It follows without dividing by an endpoint Q_n(1) that



$$
\boxed{v_2(u_j)\ge M\quad(0\le j\le n).}
\tag{10}
$$



Consequently every ordinary coefficient of U also has valuation
at least M. This step retains all actual cofactor contributions.

## 3. Exact polarized second-kind identities

Let D=1+t^2, lambda_j=j(j+1), and



$$
T_U=U^2+D(US_U'-U'S_U),\qquad S_U=\sum_j u_jS_j.
\tag{11}
$$



The finite polynomial identities



$$
(D Q_j')'=\lambda_jQ_j,\qquad
(D S_j')'=\lambda_jS_j-2Q_j'
\tag{12}
$$



and the second-kind Wronskian yield T_(Q_j)=(2j+1)h_j, a
constant. For i<j, define the polarized cross term



$$
T_{ij}=2Q_iQ_j+D(Q_iS_j'+Q_jS_i'-Q_i'S_j-Q_j'S_i).
\tag{13}
$$



Direct differentiation using (12) cancels all four derivative
products and gives



$$
T_{ij}'=(\lambda_j-\lambda_i)(Q_iS_j-Q_jS_i).
\tag{14}
$$



All signs use S_j=L((Q_j(t)-Q_j(s))/(t-s)); for example
T_(0,1)=2t, and (14) gives its derivative 2.

For even i, the constant identity for T_(Q_i) gives



$$
S_i'(0)=\frac{(2i+1)h_i}{Q_i(0)}-Q_i(0).
\tag{15}
$$



For odd i the adjacent second-kind identity gives



$$
S_i(0)=\frac{h_{i-1}}{Q_{i-1}(0)}.
\tag{16}
$$



The index i=0 in (15) gives S_0'=1-1=0, correctly.
For odd i, phi(i-1)=phi(i).

### The quadratic coefficient

Opposite parities make T_ij odd, so its t^2 coefficient is zero.
For equal parities, (14) gives



$$
[t^2]T_{ij}=\frac{\lambda_j-\lambda_i}{2}
[Q_i'S_j+Q_iS_j'-Q_j'S_i-Q_jS_i']_{t=0}.
\tag{17}
$$



For even i,j, substituting (15) cancels the two products
Q_i(0)Q_j(0); the remaining terms have valuations at least
2phi(i), since all even central Q values are units. For odd
i,j, (5) and (16) give the same lower bound 2phi(i).
As lambda_j-lambda_i=(j-i)(j+i+1), the second factor is odd
in these parity cases. Hence



$$
\boxed{v_2([t^2]T_{ij})\ge
2\phi(i)+v_2(j-i)-1\quad(i<j,\ i=j\bmod2).}
\tag{18}
$$



Since i<=n-2 for such a pair, (9), (10), and (18) imply



$$
\begin{aligned}
v_2(u_i u_j[t^2]T_{ij})
&\ge M+\phi(n)-\phi(n+1+i)+v_2(j-i)-1\\
&\ge M+\phi(n)-\phi(2n-1)\\
&=K+v+1.
\end{aligned}
\tag{19}
$$



Here v_2(j-i)>=1 and phi(2n)-phi(2n-1)=v+1. Diagonal terms
T_(Q_i) have no quadratic coefficient. Summing all actual pairs
therefore proves v_2([t^2]T_U)>=K+v+1, including cancellations.

### The linear coefficient, as a strengthening of the first gate

Equal parities make T_ij even. For opposite parities, (14) gives
[t]T_ij=(lambda_j-lambda_i)[Q_i(0)S_j(0)-Q_j(0)S_i(0)].
By (5)--(16) the bracket has valuation at least 2phi(i), and
v_2(lambda_j-lambda_i)>=1. When i<=n-2, the same estimate as
(19), with this extra factor instead of a division by two,
places the term at least at K+v+2.

The sole remaining possible pair is i=n-1,j=n. For this pair,
lambda_n-lambda_(n-1)=2n, and (9) at i=n-1 gives



$$
v_2(u_{n-1}u_n[t]T_{n-1,n})\ge
(-n-2\phi(n-1))+M+2\phi(n-1)+(v+1)=K+v+1.
\tag{20}
$$



Thus v_2([t]T_U)>=K+v+1 as well. This independently strengthens
the first gate proved by bordered determinants in
raw_even_P_first_dyadic_gate.md.

## 4. The full exponential correction is above both baselines

The exact low Taylor reconstruction is



$$
V(t):=t^n A(1/t)=-S_U(t)-E_B(t),\qquad
E_B(t)=t^n[\operatorname{Taylor}_{\le n}(B e^z)]_{z=1/t}.
\tag{21}
$$



The same factorial argument as in (8), now for N=n-s, gives



$$
v_2([t^s]E_B)\ge\phi(n)-\phi(n-s)\ge0.
\tag{22}
$$



Indeed only 0<=j<=N occurs in that Taylor coefficient, so (2)
applies to every summand. Reversing P exactly, with no asymptotic
remainder, gives



$$
t^{2n}P(1/t)=T_U+D(E_B'U-E_BU').
\tag{23}
$$



By (10), (22), and integer differentiation, every coefficient of
the correction has valuation at least M=K+n. Combining with
(19)--(20) proves (1) for the full actual P.

## 5. Consequence: the even-degree accessory cubic has no triple root

Write b_0^*=b_n, b_1^*=b_(n-1), b_2^*=b_(n-2), and let q_3,q_2,q_1
be the top three actual coefficients of the accessory cubic Q.
The already checked all-index identities are



$$
\begin{aligned}
q_3&=b_0^*p_0,\\
q_2&=b_0^*p_1+(b_1^*+2b_0^*)p_0,\\
q_1&=b_0^*(p_2-p_0)+(b_1^*+3b_0^*)p_1
 +(b_2^*+2b_0^*)p_0.
\end{aligned}
\tag{24}
$$



At even n, b_n is a dyadic unit. Equation (2) gives even
b_(n-1) and b_(n-2), since phi(n)-phi(n-1)=v>=1 and
phi(n-1)=phi(n-2). By (1), p_1/p_0 and p_2/p_0 are even.
Consequently



$$
q_2/q_3\equiv0\pmod2,\qquad q_1/q_3\equiv1\pmod2.
\tag{25}
$$



It follows that (q_2^2-3q_3q_1)/q_3^2 is a dyadic unit.
Every cubic with a triple root satisfies q_2^2=3q_3q_1;
therefore the actual Q has no triple root over the algebraic
closure of Q in every even degree n>=2.

This does not exclude a double root. It supplies no Archimedean
root bound, no endpoint gcd size estimate, and no irrationality
conclusion. It does eliminate the exact cubic degeneration
Q(z)=q_3(z-1)^3 over Q at every even degree.

## 6. Verification scope

Every displayed bound is all-index and comes from the actual
canonical moment equations. The dependence on n modulo4 enters
only the proved value K and the matching c_n bound M. All cases
n=2 and i=0,1 are included explicitly above. No new canonical
degree construction or numerical scan was used in this proof.
The independent audit status is recorded separately.

The frozen exact controls n=2,4,8,16 all pass in
raw_even_P_moment_gates_checks.json. They reuse existing triples,
normalize each by B(1), and verify the moment equations, every
orthogonal-coordinate bound, exact reversal/reconstruction and
both coefficient estimates. They are controls of the proved
identities, not the basis of an all-index assertion.
