> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 report: the endpoint-matched $b=3$ cofactor family

## Summary and scope

The assignment concerns


$$
A_n(z)+B_n(z)e^z+C_n(z)F(z)=O(z^{2n+4}),\qquad
F(z)=4\arctan\frac{z}{2-z},
$$


with degree caps $(n,3,n)$ and


$$
B_n(1)=C_n(1)=Y_n.
$$


Throughout the actual approximation problem, $n\ge3$.

This object is **already contained as the $b=3$ specialization of the supplied growing-degree cofactor reduction**. It is not a newly invented family, and it is not the excluded $b=3,m=1$ Gram center.

The new deductions below are:

1. An explicit, fixed-size scalar construction of its complete endpoint quotient, with all row, maximal-minor and contraction contents accounted for, and with the final endpoint gcd retained.
2. A five-coordinate, polynomial-coefficient recurrence computing all factorial contractions needed for this quotient.
3. An all-prime-power transfer theorem for these scalar coordinates and for the complete factorial numerator contraction.
4. A seven-row exact certificate giving the new, all-index bound
   

$$
\boxed{v_7(q_n)\ge 2v_7(n!)}
$$


   on the nonzero-endpoint domain, for $n\ge7$. This concerns the **actual reduced denominator** of this endpoint-matched cofactor family.

The single-prime rate is insufficient to exclude this family or to prove shrinking primitive forms. A precisely bounded additional prime certificate is proposed at the end.

All new results here are author-level derivations. No tool execution or independent review is claimed.

---

## 1. A five-scalar recurrence

Write


$$
\phi(z)=1-z+\frac{z^2}{2},\qquad
H_n(x)=n![z^n]e^{xz}\phi(z)^n,
$$


and define


$$
h_n=H_n(1),\qquad u_n=H_n'(1),\qquad v_n=H_n''(1).
$$



To avoid confusion with the approximating polynomial $A_n(z)$, denote the two factorial contractions by $\mathcal A_n,\mathcal B_n$. Introduce one additional scalar $\mathcal M_n$, as follows:


$$
\mathscr F_n(x)=x^nH_n(x),\qquad
I(P)=\int_1^\infty e^{1-x}P(x)\,dx,
$$




$$
\mathcal A_n=I(\mathscr F_n),\qquad
\mathcal M_n=I(x\mathscr F_n).
$$



For a polynomial $P$,


$$
I(P)=\sum_{r\ge0}P^{(r)}(1),
$$


where the sum terminates. Thus all five coordinates


$$
(h_n,u_n,v_n,\mathcal A_n,\mathcal M_n)
$$


are integers.

### Proposition 1: exact recurrence

Starting from


$$
(h_0,u_0,v_0,\mathcal A_0,\mathcal M_0)=(1,0,0,1,2),
$$


put $t=n+1$. Then


$$
\boxed{
\begin{aligned}
h_{n+1}&=-nh_n+nu_n+\frac{v_n}{2},\\
u_{n+1}&=t\left(h_n-u_n+\frac{v_n}{2}\right),\\
v_{n+1}&=t\left(nh_n+u_n-\frac{n+2}{2}v_n\right),\\
\mathcal A_{n+1}&=t\mathcal M_n+h_n-u_n+\frac{v_n}{2},\\
\mathcal M_{n+1}
&=t^3\mathcal A_n+t(2n+3)\mathcal M_n\\
&\quad +(n^2+3n+4)h_n-(n+3)u_n+(n+2)v_n .
\end{aligned}}
\tag{1}
$$



Moreover, the adjacent contraction in the supplied endpoint reduction is exactly


$$
\boxed{\mathcal B_n=\mathcal M_n+h_n-u_n.}
\tag{2}
$$



In particular, the complete scalar state evolves by a fixed $5\times5$ matrix with coefficients in $\mathbb Z[1/2][n]$. No growing determinant is needed to compute it.

### Derivation

The first three identities are the coefficient-extraction transition for $H_n$. For the last two, the corresponding polynomial transition is


$$
\mathscr F_{n+1}
=\frac{x^2}{2}\mathscr F_n''
+x(1-x)\mathscr F_n'
+\left(x^2-x-\frac{n(n+1)}2\right)\mathscr F_n.
\tag{3}
$$



Set


$$
J_n=\mathscr F_n'(1)=nh_n+u_n,
$$




$$
K_n=\mathscr F_n''(1)=n(n-1)h_n+2nu_n+v_n.
$$


The differential equation for $H_n$, after multiplication by the appropriate power of $x$, becomes


$$
\begin{aligned}
0={}&x^2\mathscr F_n'''
+\bigl((2-2n)x-2x^2\bigr)\mathscr F_n''\\
&+\bigl(n(n-1)+(4n-2)x+2x^2\bigr)\mathscr F_n'
-(2n^2+4nx)\mathscr F_n.
\end{aligned}
\tag{4}
$$



Let $M_j=I(x^j\mathscr F_n)$, so $M_0=\mathcal A_n$, $M_1=\mathcal M_n$. Integration by parts in (4), first directly and then after multiplication by $x$, gives


$$
\begin{aligned}
M_2={}&2(n+1)M_1+n(n+1)M_0\\
&+K_n-(2n+1)J_n+(n^2+3n+1)h_n,
\end{aligned}
\tag{5}
$$


and


$$
\begin{aligned}
M_3={}&(2n+3)M_2+(n^2+n-2)M_1+(n+1)(n+2)M_0\\
&+K_n-2(n+1)J_n+(n^2+5n+3)h_n.
\end{aligned}
\tag{6}
$$



Applying $I$ and $I(x\,\cdot)$ to (3) yields


$$
\mathcal A_{n+1}
=\frac12M_2-\frac{n(n+1)}2M_0+\frac12(h_n-J_n),
\tag{7}
$$




$$
\mathcal M_{n+1}
=\frac12M_3+\left(1-\frac{n(n+1)}2\right)M_1
+h_n-\frac12J_n.
\tag{8}
$$


Substitution of (5)–(6), followed by the displayed expressions for $J_n,K_n$, gives (1).

Finally, Rodrigues and integration by parts identify


$$
\mathcal B_n=\frac{I(\mathscr F_{n+1}')}{n+1}
=\frac{\mathcal A_{n+1}-h_{n+1}}{n+1}.
$$


The first and fourth equations of (1) give


$$
\mathcal A_{n+1}-h_{n+1}
=(n+1)(\mathcal M_n+h_n-u_n),
$$


proving (2) without a modular division by $n+1$.

For comparison with the supplied finite sums, if


$$
a_s(n)=[z^s]\phi(z)^n,\qquad D_j=j!\sum_{a=0}^j\frac1{a!},
$$


then


$$
\mathcal A_n=\sum_s(n)_s a_s(n)D_{2n-s},
\tag{9}
$$




$$
\mathcal B_n
=2D_{2n+1}
+\sum_{s\ge1}(n)_{s-1}(2n+2-s)a_s(n+1)D_{2n+1-s}.
\tag{10}
$$


Thus (1) computes the same complete contractions, not replacements omitting their partial-exponential sums.

---

## 2. Explicit $b=3$ high rows

Suppress the index $n$ on $h,u,v$, and put


$$
t=n+1,\qquad
a=-nh+nu+\frac v2,
$$




$$
\alpha=h-u+\frac v2,\qquad
\beta=nh+u-\frac{n+2}{2}v.
\tag{11}
$$


Hence


$$
a=H_t(1),\qquad H_t'(1)=t\alpha,\qquad H_t''(1)=t\beta.
$$



Let


$$
E_{k,r}=\left.\frac{d^r}{dx^r}\bigl(x^kH_k(x)\bigr)\right|_{x=1}.
$$


The two integer high rows needed at $b=3$ can be taken as


$$
r=(E_{t,0},E_{t,1},E_{t,2},E_{t,3}),
$$




$$
s=\frac1{t+1}(E_{t+1,1},E_{t+1,2},E_{t+1,3},E_{t+1,4}).
\tag{12}
$$


The division in the second row is an exact integer division. It removes the forced row factor $n+2$ before any local reduction.

Here are division-free formulas over $\mathbb Z[1/2]$:


$$
\begin{aligned}
r_0&=a,\\
r_1&=t(a+\alpha),\\
r_2&=t\bigl((t-1)a+2t\alpha+\beta\bigr),\\
r_3&=t\bigl((t^2-3t+4)a+3t(t-1)\alpha+2t\beta\bigr),
\end{aligned}
\tag{13}
$$


and


$$
\begin{aligned}
s_0={}&(1-t)a+t(t-1)\alpha+t\beta,\\
s_1={}&(-t^2+3t+2)a+t(t^2-2t-1)\alpha+t^2\beta,\\
s_2={}&t\bigl((-t^2+6t+3)a
 +(t^3-4t^2+t+2)\alpha +(t^2-2t-1)\beta\bigr),\\
s_3={}&t(-t^3+10t^2-7t-6)a\\
&+t^2(t^3-7t^2+11t+7)\alpha
+t(t^3-5t^2+2t+2)\beta .
\end{aligned}
\tag{14}
$$



These follow by applying (1) once more and using


$$
H_k'''(1)=2kH_k(1)-kH_k''(1),
$$




$$
H_k''''(1)=-(k+1)H_k'''(1)
+2H_k''(1)+2(k-1)H_k'(1).
$$



Define


$$
j=a+\alpha,\quad
k=(t-1)a+2t\alpha+\beta,
$$




$$
\ell=(t^2-3t+4)a+3t(t-1)\alpha+2t\beta.
$$


The cumulative rows from the general cofactor reduction now become


$$
\mathbf u=(0,j,j+k,j+k+\ell),
$$




$$
\mathbf p=(0,h,h+J,h+J+K),
\tag{15}
$$


where


$$
J=nh+u,\qquad K=n(n-1)h+2nu+v.
$$


Let $\mathbf e=(1,1,1,1)$, and define the three raw integer contractions


$$
\boxed{
\begin{aligned}
\sigma_n&=-\det[r;s;\mathbf e;\mathbf u],\\
\chi_n&=-\det[r;s;\mathbf e;\mathbf p],\\
\kappa_n&=\det[r;s;\mathbf u;\mathbf p].
\end{aligned}}
\tag{16}
$$



Equations (1), (11), and (13)–(16) are an exact fixed-size scalar algorithm for this family.

---

## 3. The complete endpoint quotient and every content cancellation

Let


$$
L_k(y)=2^ki^kP_k(-i(2y-1)),\qquad P_k=L_k(1),
$$


and define the rational second-kind endpoints


$$
w_k=\mathcal L\!\left(\frac{L_k(y)-P_k}{y-1}\right),
\qquad
\mathcal L(f)=\int_{-1}^1f\!\left(\frac{1+iu}{2}\right)\,du.
$$


As in the supplied contiguous endpoint source,


$$
G_n=P_nw_{n+1}-P_{n+1}w_n
=\frac{(-1)^n2^{2n+3}}{n+1}.
\tag{17}
$$



Using the raw contractions (16), set


$$
\boxed{
\begin{aligned}
D_n&=tP_{n+1}\chi_n-2P_n\sigma_n,\\
Q_n&=2w_n\sigma_n-tw_{n+1}\chi_n,\\
V_n&=\sigma_n\mathcal A_n-\chi_n\mathcal B_n-\kappa_n.
\end{aligned}}
\tag{18}
$$


Here $D_n,V_n$ are integers. The term $-\kappa_n$ is essential.

### Exact quotient before primitive contraction normalization

For the actual endpoint pair $X_n=A_n(1)$, $Y_n=B_n(1)$, one has


$$
\boxed{
\frac{X_n}{Y_n}
=\frac{Q_n+\dfrac{2^{n+1}}{(n!)^2}V_n}{D_n}
}
\qquad(D_n\ne0).
\tag{19}
$$



For completeness, the common endpoint scale in the monic high-row convention is explicit. Put


$$
\rho_n=\frac{n+2}{(2n+2)!(2n+4)!},
\qquad f_n=\frac{2^n}{(n!)^2}.
$$


Then


$$
Y_n=\rho_n\frac{f_n}{tG_n}D_n,
\qquad
X_n=\rho_n\frac{f_n}{tG_n}(Q_n+2f_nV_n).
\tag{20}
$$



The determinant expansion proving (19) uses


$$
T(L_n)=T_P\mathbf e-f_n\mathbf p,
\qquad
T(L_{n+1})=T_U\mathbf e-\frac{2f_n}{t}\mathbf u,
$$


with


$$
T_P=f_n\mathcal A_n,\qquad
T_U=\frac{2f_n}{t}\mathcal B_n.
$$


The supplied adjacent endpoint identities give the endpoint rows as linear combinations of these two $T$-rows. Bilinearity then gives


$$
Q_n+2f_nV_n
=2(w_n+T_P)\sigma_n
-t(w_{n+1}+T_U)\chi_n-2f_n\kappa_n,
$$


which is precisely the whole reconstructed numerator.

### Row, maximal-minor and contraction contents

The individual row contents are


$$
c_1=\gcd_i|r_i|,\qquad c_2=\gcd_i|s_i|.
$$


If either row is zero, or if the high block has rank less than two, the endpoint cofactors vanish. Otherwise normalize the rows and let $\mu_n$ be the gcd of their six maximal minors. Forming the contractions from the primitive maximal-minor vector gives a further contraction gcd $d_n$.

Equivalently—and more economically for this fixed $b=3$ family—define directly


$$
\boxed{\delta_n=\gcd(|\sigma_n|,|\chi_n|,|\kappa_n|).}
\tag{21}
$$


On $D_n\ne0$, this is positive, and exactly


$$
\delta_n=c_1c_2\mu_nd_n.
\tag{22}
$$


Thus dividing the raw contractions by $\delta_n$ removes **all** these contents at once. This is not an assumption that row contents exhaust the gcd.

Set


$$
(\sigma_n^*,\chi_n^*,\kappa_n^*)
=\frac1{\delta_n}(\sigma_n,\chi_n,\kappa_n),
$$


and define $D_n^*,Q_n^*,V_n^*$ from (18) using these primitive contractions. Then


$$
\boxed{
\frac{X_n}{Y_n}
=\frac{Q_n^*+\dfrac{2^{n+1}}{(n!)^2}V_n^*}{D_n^*}.
}
\tag{23}
$$


The scale in (20) acquires the common factor $\delta_n$, which cancels.

### The final endpoint gcd is still separate

Let


$$
\lambda_n=\operatorname{lcm}\!\left(
(n!)^2,\;
2^n\operatorname{lcm}(1,2,\ldots,n+1)
\right).
\tag{24}
$$


This is a valid, not necessarily minimal, clearer. Indeed, the moment formula


$$
\mu_j=
\frac{(1+i)^{j+1}-(1-i)^{j+1}}
{i\,2^j(j+1)}
$$


shows that $2^n\operatorname{lcm}(1,\ldots,n+1)$ clears both second-kind endpoints.

Define the integers


$$
N_n=\lambda_n\left(
Q_n^*+\frac{2^{n+1}}{(n!)^2}V_n^*
\right),\qquad
Z_n=\lambda_nD_n^*,
$$


and retain the final gcd


$$
g_n=\gcd(|N_n|,|Z_n|).
\tag{25}
$$


The actual rational center approximating $S=e+\pi$ is


$$
c_n=-\frac{X_n}{Y_n}=\frac{p_n}{q_n},
$$


where


$$
\boxed{
q_n=\frac{|Z_n|}{g_n},\qquad
p_n=-\operatorname{sign}(Z_n)\frac{N_n}{g_n}.
}
\tag{26}
$$


Consequently $\gcd(p_n,q_n)=1$, $q_n>0$. Equations (23)–(26) retain the complete numerator and every endpoint cancellation.

---

## 4. An all-prime-power scalar transfer theorem

The five-state recurrence is useful beyond ordinary residue transfer.

### Proposition 2: transfer at every modulus $p^a$

For every odd prime $p$, every integer $a\ge1$, and all nonnegative integers $m,n$ satisfying


$$
m\equiv n\pmod{p^a},
$$


one has


$$
\boxed{
(h_m,u_m,v_m,\mathcal A_m,\mathcal M_m)
\equiv
(h_n,u_n,v_n,\mathcal A_n,\mathcal M_n)
\pmod{p^a}.
}
\tag{27}
$$


The same is true of


$$
\mathcal B_n,\quad \sigma_n,\quad\chi_n,\quad\kappa_n,\quad V_n.
\tag{28}
$$



This is a theorem about the scalar contractions. It does not assert a comparable simple periodicity for $P_n$, $w_n$, or the reduced $q_n$.

### Proof

Assume $m\ge n$ and $p^a\mid m-n$. For $s\ge1$, the binomial expansion of $\phi(z)^{m-n}$ gives


$$
v_p\bigl(a_s(m)-a_s(n)\bigr)
\ge a-\lfloor\log_p s\rfloor.
\tag{29}
$$


Indeed,


$$
\binom{m-n}{j}=\frac{m-n}{j}\binom{m-n-1}{j-1},
$$


and only $1\le j\le s$ can contribute.

For integer $x$, a falling factorial of length $s$ satisfies


$$
v_p((x)_s)\ge v_p(s!)\ge\lfloor\log_p s\rfloor.
\tag{30}
$$


Also, $(x)_s$ is a polynomial with integer coefficients, so


$$
(m)_s\equiv(n)_s\pmod{p^a}.
$$


Combining these statements proves transfer term by term in


$$
H_n^{(d)}(1)=\sum_s(n)_{s+d}a_s(n),\qquad d=0,1,2.
\tag{31}
$$



To handle the $D$-indices uniformly, define on $\mathbb Z_p$


$$
\mathfrak D(x)=\sum_{r\ge0}(x)_r.
$$


This converges uniformly because $v_p((x)_r)\ge v_p(r!)\to\infty$. It is $1$-Lipschitz: each finite partial sum is an integer polynomial. At nonnegative integers it equals the ordinary $D_j$. Applying this to (9), together with (29)–(30), proves transfer of $\mathcal A_n$.

For (10), the weight


$$
W_s(x)=(x)_{s-1}(2x+2-s)
$$


satisfies


$$
v_p(W_s(x))\ge\lfloor\log_p s\rfloor.
\tag{32}
$$


The only additional boundary requiring attention is $s=p$. If $(x)_{p-1}$ is a unit, then $x\equiv-1\pmod p$, and $2x+2-p$ is divisible by $p$. For $s\ge p+1$, the factorial valuation supplies the required bound; when $\lfloor\log_p s\rfloor\ge2$, use


$$
v_p((s-1)!)\ge p^{\lfloor\log_p s\rfloor-1}-1
\ge\lfloor\log_p s\rfloor.
$$


Thus (10) transfers term by term as well.

Equation (2) now gives transfer of $\mathcal M_n$. Finally, (11), (13)–(16), and (18) express the remaining quantities polynomially over $\mathbb Z[1/2]$ in $n$ and the state. This proves (27)–(28). ∎

### A finite certificate consequence

Fix $p^a$. If the explicitly computable residues


$$
V_r\pmod{p^a},\qquad 0\le r<p^a,
$$


are all nonzero, then


$$
v_p(V_n)\le a-1
$$


for every $n\ge0$.

Thus this family admits a genuine finite-state arithmetic certificate at any prescribed odd prime-power modulus. Its infinite force comes from Proposition 2, not from extrapolating a list of large canonical degrees.

---

## 5. A new actual-denominator theorem at $7$

The following table is computed by (1) and (13)–(18), entirely modulo $7$. The $\mathcal B$-column is recovered from $\mathcal M+h-u$.



$$
\begin{array}{c|rrrrr|rrrr}
r&h&u&v&\mathcal A&\mathcal M&
\sigma&\chi&\kappa&V\\ \hline
0&1&0&0&1&2&0&5&0&6\\
1&0&1&0&3&4&5&1&1&4\\
2&1&5&2&0&4&6&5&5&2\\
3&2&5&2&2&4&1&2&1&6\\
4&3&6&3&0&2&0&2&1&1\\
5&3&3&3&5&0&2&4&5&5\\
6&5&2&3&5&5&6&3&5&1
\end{array}
\tag{33}
$$



In particular,


$$
\boxed{(V_0,\ldots,V_6)\equiv(6,4,2,6,1,5,1)\pmod7.}
\tag{34}
$$


All entries are nonzero. As an additional finite recurrence control, the state at $n=7$ returns to


$$
(1,0,0,1,2)\pmod7.
$$



Some exact small controls, independent of reduction modulo $7$, are


$$
(\sigma_0,\chi_0,\kappa_0,V_0)=(0,-16,0,48),
$$




$$
(\sigma_1,\chi_1,\kappa_1,V_1)=(-30,22,-20,-290),
$$




$$
(\sigma_2,\chi_2,\kappa_2,V_2)
=(7132,-7660,13816,1154736).
\tag{35}
$$



These small scalar seeds are defined even when $r<3$; no claim is made that those seed indices themselves are admissible $b=3$ approximants.

### Theorem 3: actual $7$-adic denominator depth

For every $n\ge7$ with $D_n\ne0$,


$$
\boxed{
v_7(q_n)=2v_7(n!)+v_7(D_n)
       =2v_7(n!)+v_7(D_n^*)
       \ge2v_7(n!).
}
\tag{36}
$$



### Proof, including complete numerator cancellation

Proposition 2 and (34) give $v_7(V_n)=0$ for every $n$. Hence $\delta_n$ is also a $7$-adic unit.

Put


$$
F=v_7(n!),\qquad \ell=\lfloor\log_7(n+1)\rfloor.
$$


The moment denominators give


$$
v_7(w_n),v_7(w_{n+1})\ge-\ell,
$$


and therefore


$$
v_7(Q_n)\ge-\ell.
\tag{37}
$$


For $n\ge7$,


$$
2F>\ell.
\tag{38}
$$


Thus the factorial term in the **complete** numerator of (19) has valuation $-2F$, strictly below that of the second-kind term:


$$
v_7\left(Q_n+\frac{2^{n+1}}{(n!)^2}V_n\right)=-2F.
\tag{39}
$$


There is no equal-depth cancellation.

For a nonzero rational quotient, actual reduction gives exactly


$$
v_7(q_n)
=\max\left\{0,\,
v_7(D_n)-
v_7\left(Q_n+\frac{2^{n+1}}{(n!)^2}V_n\right)
\right\}.
\tag{40}
$$


Since $D_n$ is a nonzero integer, (39) proves (36). This calculation already includes the final gcd (25). ∎

The seven-row table is a displayed exact certificate, not a claim of an independently run computation. Its proposed independent check is bounded and specified below.

---

## 6. Combining with the complete signed error

The supplied fixed-$b$ theorem applies here at the fixed value $b=3$. It proves that, for every sufficiently large integer $n$,

- the projective solution is unique;
- $Y_n\ne0$, equivalently $D_n\ne0$;
- the whole normalized error is nonzero; and
- with $\epsilon_n>0$,
  

$$
\boxed{
  \frac{(-1)^n(S-c_n)}{\epsilon_n}
  \longrightarrow(\sqrt2-1)^3>0,
  }
  \tag{41}
$$


  

$$
\frac{\log\epsilon_n}{n}\longrightarrow
  -\tau,\qquad \tau=2\log(1+\sqrt2).
$$



The primitive integer form is


$$
L_n=q_nS-p_n=q_n(S-c_n),
$$


so


$$
\boxed{
\log|L_n|=\log q_n-\tau n+o(n).
}
\tag{42}
$$


This uses both complete evaluated tails, not a first omitted Taylor coefficient.

From Theorem 3 and Legendre’s formula,


$$
\log q_n\ge \frac{\log7}{3}\,n-O(\log n).
\tag{43}
$$


Consequently,


$$
\liminf_{n\to\infty}\frac{\log|L_n|}{n}
\ge \frac{\log7}{3}-\tau.
\tag{44}
$$


The right side is negative. Therefore:

- the new $7$-adic theorem does **not** exclude this family;
- it does **not** prove that the primitive forms shrink;
- it does **not** decide the irrationality of $e+\pi$.

It does establish one unconditional factorial-depth prime factor in the actual denominator, throughout the eventual nonzero-endpoint domain.

---

## 7. The next arithmetic lemma, and the obstruction at numerator roots

For any odd prime $p$, the exact complete reduction can be written using the raw scalars as


$$
\mathcal R_{n,p}
=V_n+\frac{(n!)^2}{2^{n+1}}Q_n,
$$




$$
v_p(q_n)
=\max\{0,\;2v_p(n!)+v_p(D_n)-v_p(\mathcal R_{n,p})\},
\tag{45}
$$


provided the complete numerator is nonzero.

This is invariant under dividing by $\delta_n$: numerator and denominator lose the same content.

### A useful general finite-certificate criterion

Suppose, for a fixed $p$, a proved bound gives


$$
v_p(V_n)\le b_p\qquad\text{for all }n.
$$


For all sufficiently large $n$,


$$
2v_p(n!)-b_p>\lfloor\log_p(n+1)\rfloor,
$$


so the factorial term separates from the second-kind term, and


$$
\boxed{
v_p(q_n)\ge2v_p(n!)-b_p.
}
\tag{46}
$$



Proposition 2 supplies a bounded way to prove such a hypothesis: find a modulus $p^a$ for which no scalar seed $V_r$ vanishes. Then $b_p=a-1$.

For a fixed finite set $\mathcal P$ of primes certified in this way,


$$
\log q_n\ge
\left(\sum_{p\in\mathcal P}\frac{2\log p}{p-1}\right)n
-O_{\mathcal P}(\log n).
\tag{47}
$$


Hence the exact next exclusion criterion is


$$
\boxed{
\sum_{p\in\mathcal P}\frac{2\log p}{p-1}
>2\log(1+\sqrt2).
}
\tag{48}
$$


If established, it would exclude this particular cofactor family—not decide the arithmetic nature of $S$.

### Why scalar roots cannot simply be discarded

The exact seed in (35) factors as


$$
V_2=1154736=16\cdot11\cdot3^8.
\tag{49}
$$


Also,


$$
\delta_2=\gcd(7132,7660,13816)=4.
$$


Thus the high ternary depth in (49) survives contraction-content removal.

By Proposition 2, for every nonnegative


$$
n\equiv2\pmod{3^9},
$$


one has


$$
v_3(V_n)=8.
\tag{50}
$$


Moreover, $\sigma_n$ is a ternary unit on this progression, so the contraction gcd does not remove this depth.

This is not a ternary exclusion theorem, and it does not assert an unbounded ternary depth. It demonstrates concretely why a blanket “all small primes are units after content removal” argument is false for this object. On deeper zero disks one must control the actual $V_n$, its possible common depth with $D_n$, and—when separation fails—the complete $\mathcal R_{n,p}$ in (45).

---

## 8. Closing deliverables

### (1) New result and proof status

**Author-level proved results:**

- The explicit five-state recurrence (1), including the identity
  

$$
\mathcal B_n=\mathcal M_n+h_n-u_n.
$$


- The complete $b=3$ quotient (23), with row, maximal-minor and contraction contents removed through (21)–(22), and with the actual primitive denominator defined by the final gcd (25)–(26).
- The all-prime-power scalar transfer theorem (27)–(28).
- The new actual-denominator bound
  

$$
v_7(q_n)\ge2v_7(n!)
$$


  for $n\ge7$ on the nonzero-endpoint domain, using the explicit seven-row certificate (33).

The analytic nonvanishing and signed whole-error statement are inherited only at the supplied fixed-$b=3$ theorem’s stated scope. No excluded Gram-center arithmetic has been transferred to this construction.

### (2) Exact remaining bottleneck

The established $7$-adic weight is below the full-error threshold. What remains is either:

- enough further certified prime contributions to make (48) hold, thereby excluding this cofactor family; or
- a genuinely different total estimate for the final gcd in (25), strong enough to determine whether any primitive subsequence can shrink.

At primes with scalar zeros, the unresolved quantity is the complete cancellation-sensitive expression (45), not a coefficient clearer or a high-row content.

**The irrationality of $e+\pi$ remains unresolved.**

### (3) Bounded exact computation request

If the coordinator elects to perform a computation, the following fixed task would decide stated finite certificate lemmas.

**Inputs**

1. Independently reconstruct the seven scalar seeds $r=0,\ldots,6$ from the defining $H_r$ polynomials and finite sums (9)–(10), and verify every entry of (33). This is a check of scalar identities, not a canonical-degree extrapolation.
2. For exactly
   

$$
\mathcal P_0=
   \{11,13,17,19,23,31,37,41,43,47,
   53,59,61,67,71,73,79,83,89,97\},
$$


   compute (1), (11), and (13)–(18) modulo $p$ at every $0\le r<p$.

This second task contains exactly **1,014 residue rows**. No extension of the prime list is requested.

**Expected verifiable output**

- For every requested prime, the complete $V_r\bmod p$ vector and its exact zero set.
- The associated state and contraction rows, sufficient to reproduce each entry.
- For the primes with empty zero set, exact rational logarithm bounds for
  

$$
W=\frac{\log7}{3}
  +\sum_{\substack{p\in\mathcal P_0\\
                   V_r\not\equiv0\ (p)\ \forall r}}
       \frac{2\log p}{p-1}
$$


  and for $2\log(1+\sqrt2)$, together with the certified sign of their difference if separated.

An empty zero set proves the corresponding all-index unit lemma through Proposition 2. If the certified aggregate weight crosses the threshold, Theorem 3’s complete-numerator argument and (41)–(42) then supply an unconditional exclusion of **this distinct endpoint-matched cofactor family**. No finite output by itself would establish the irrationality of $e+\pi$.
