> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The actual accessory cubic has no triple root at any index

Date: 2026-09-13. Original continuation by audit_results, using the
odd-degree central-derivative observation of audit_sources.

For the actual canonical raw Hermite--Pade family, the accessory
polynomial Q_n has degree three at every n>=1. This note proves
the further all-index statement



$$
\boxed{Q_n\text{ has no triple root over }\overline{\mathbb Q}.}
\tag{1}
$$



More precisely, the following necessary condition for a triple root
never occurs:



$$
\mathcal H_n=q_{2,n}^2-3q_{3,n}q_{1,n}=0.
\tag{2}
$$



This does not exclude a double root and is not a squarefreeness
theorem. All coefficients refer to the same actual canonical scale;
the ratios below are invariant under a common rescaling of Q_n.

## 1. Even degrees and common notation

For even n>=2, raw_even_P_second_dyadic_gate.md proves (1) through
the exact actual moment equations. Here p_j denotes the coefficient
of z^(2n-j) in



$$
P=(1+z^2)(A'C-AC')+C^2,\qquad p_0=\Xi_n.
$$



Write phi(j)=v_2(j!) and K_0=-2n-2phi(n-1). The all-index Xi and
B coefficient theorems give



$$
v_2(p_0)=
\begin{cases}
K_0+2,&n=1\pmod4,\\
K_0-2,&n=2\pmod4,\\
K_0,&n=0,3\pmod4,
\end{cases}
\tag{3}
$$



and v_2(b_j)>=phi(n)-phi(j). Furthermore, for n>=2,



$$
B_n(z)\equiv
\begin{cases}z^{n-1},&n=1\pmod4,\\z^n,&\text{otherwise}
\end{cases}\pmod2,
\tag{4}
$$



with exact v_2(b_n)=v_2(n-1) in the first class and zero
otherwise. These are the reviewed actual coefficient results in
raw_B_coefficient_dyadic_divisibility.md and
raw_all_index_cubic_gate.md.

## 2. The odd-degree version of the moment bound

Let n be odd and set M_0=-n-2phi(n-1), so K_0=M_0-n.
Use the same raw monic Legendre polynomials Q_j, second-kind
polynomials S_j, and exact expansion



$$
U(t)=t^n C(1/t)=\sum_{j=0}^n u_jQ_j(t).
$$



The actual moments and the B theorem give, without any parity
restriction on n,



$$
v_2(u_j)\ge\phi(n)-\phi(n+1+j)-2\phi(j)\ge M_0,
\qquad j<n.
\tag{5}
$$



The last inequality uses the monotonicity in j and equality with
M_0 at j=n-1. In odd degree the correct central equation is



$$
U'(0)=c_{n-1}.
$$



The right side has the proved exact valuation M_0. The coefficient
Q_n'(0) is a dyadic unit; all lower terms already have valuation
at least M_0. It follows that v_2(u_n)>=M_0. Hence every u_j
and every ordinary coefficient of U has valuation at least M_0.
This argument does not divide by Q_n(0), which is zero in odd
degree, or by the potentially nonunit value Q_n(1).

The proof of the polarized second-kind estimates in
raw_even_P_second_dyadic_gate.md, Section 3, now applies with
M_0,K_0 and v_2(n)=0. In detail, for the quadratic coefficient,
same-parity pairs i<j satisfy i<=n-2 and have lower bound



$$
M_0+\phi(n)-\phi(n+1+i)+v_2(j-i)-1\ge K_0+1.
\tag{6}
$$



Here phi(2n)-phi(2n-1)=1. Opposite-parity pairs contribute zero
to this coefficient. For the linear coefficient, all pairs with
i<=n-2 gain at least the same amount. The sole additional pair
i=n-1,j=n has eigenvalue difference 2n, of valuation one, and
also has valuation at least K_0+1. All diagonal second-kind
quadratics are constant.

The exact exponential reconstruction correction has all coefficients
of valuation at least M_0, as proved in the same note. Thus for
every odd n>=1,



$$
\boxed{v_2(p_1),v_2(p_2)\ge K_0+1.}
\tag{7}
$$



For n=1 this is only a bound at the unshifted K_0 baseline;
the separate exact cubic is used below. No claim that p_1/p_0
or p_2/p_0 is integral in the class n=1 modulo4 is made.

## 3. The two odd residue classes have different dominant terms

Put



$$
r_1=p_1/p_0,\quad r_2=p_2/p_0,\qquad
d_1=b_{n-1}/b_n,\quad d_2=b_{n-2}/b_n.
$$



The exact leading coefficient identities, at the actual common
scale, read



$$
\frac{q_2}{q_3}=r_1+d_1+2,
\qquad
\frac{q_1}{q_3}=r_2-1+(d_1+3)r_1+d_2+2.
\tag{8}
$$



If n=3 modulo4, (3) and (7) make r_1,r_2 even. By (4), d_1,d_2
are even and b_n is a unit. Hence q_2/q_3 is even and q_1/q_3
is a unit, exactly as in even degree. Therefore



$$
v_2(\mathcal H_n/q_3^2)=0,\qquad n=3\pmod4.
\tag{9}
$$



If n=1 modulo4 and n>=5, put a=v_2(n-1)>=2. Equations (3)
and (7) give only v_2(r_1),v_2(r_2)>=-1. On the other hand,
(4) and the exact leading-B valuation give



$$
v_2(d_1)=-a,
\qquad v_2(d_2)\ge0.
\tag{10}
$$



For the second inequality, phi(n)-phi(n-2)=a, so the B coefficient
bound exactly offsets the a in the denominator. The d_1 term
is uniquely least in the first equation (8), since -a<-1. Thus



$$
v_2(q_2/q_3)=-a,\qquad
v_2(q_1/q_3)\ge-a-1.
\tag{11}
$$



As -2a<-a-1 for a>=2, the square (q_2/q_3)^2 uniquely
dominates 3q_1/q_3 in the Hessian. Consequently



$$
\boxed{v_2(\mathcal H_n/q_3^2)=-2v_2(n-1),
\quad n\ge5,\ n=1\pmod4.}
\tag{12}
$$



The argument does not reuse the even-degree dominant term in this
exceptional class.

## 4. Degree one and the final all-index statement

For n=1 the previously saved primitive cubic divided by four is



$$
-464z^3-1746z^2-2697z+1403.
$$



Its Hessian is
1746^2-3(464)(2697)=-705708!=0. In fact its normalized Hessian
valuation is -6. Thus (1) holds at n=1 as well.

Combining the even proof and (9), (12), the actual nonzero cubic
coefficients satisfy the all-index exact valuation statement



$$
v_2\!\left(\frac{q_2^2-3q_3q_1}{q_3^2}\right)=
\begin{cases}
-6,&n=1,\\
-2v_2(n-1),&n\ge5,\ n=1\pmod4,\\
0,&n\ge2,\ n\ne1\pmod4.
\end{cases}
\tag{13}
$$



Since q_3=b_n Xi_n, the exceptional leading-B valuation exactly
cancels the negative value in (13). Equivalently, at the canonical
triple scale one has the simpler all-index statement



$$
\boxed{v_2(q_2^2-3q_3q_1)=2v_2(\Xi_n),\qquad n\ge1.}
\tag{14}
$$



Thus (q_2^2-3q_3q_1)/Xi_n^2 is always a dyadic unit. The equation
uses the canonical scale: under rescaling the entire HP triple,
the cubic coefficients and Xi have different degrees in that scale.
The nonvanishing and the ratio formulation (13) are scale invariant.

In particular Q_n cannot equal q_3(z-r)^3 for any algebraic r.
The three rational integers Q_n(1),Q_n'(1),Q_n''(1)/2 therefore
cannot all vanish after any integral common scaling. Their gcd is
nonzero. This is an exact exclusion of a degeneration, not an
Archimedean bound for that gcd or for its prime-power factors.
The main rationality or irrationality question remains unresolved.
