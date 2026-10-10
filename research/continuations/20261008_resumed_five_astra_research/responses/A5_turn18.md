> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An exponentially paid large-prime depth band and a complete non-arc $p$-block reduction

## Abstract and proof status

The rationality or irrationality of $e+\pi$ remains unresolved. The strict global estimate


$$
\kappa_N^{\mathrm{prod}}\le (N!)^{1-\eta}e^{CN},
\qquad \eta>0,
$$


is not proved here.

This report makes two concrete advances outside the small arc-root support.

1. **A full-depth payment on a new large-prime band.**  
   From the actual divided Gaussian source and the complete corrected $K$-column, I construct two explicit integer forcing remainders
   

$$
\mathscr I_{1,N},\qquad \mathscr I_{2,N},
$$


   and prove that their numerical joint divisor
   

$$
J_N^{\mathrm{aff}}=\gcd(\mathscr I_{1,N},\mathscr I_{2,N})>0
$$


   satisfies
   

$$
J_N^{\mathrm{aff}}
   <10^{10}(2N)^{15}\frac{5^{4N}}{g_B^2}.
$$


   At every prime for which the actual coefficient determinant has greater depth than this actual numerical joint divisor, **all** unpaid source depths are bounded by $v_p(J_N^{\mathrm{aff}})$. This applies in particular to primes $p>2N$, without a factorial allowance, without excluding primes of $g_B$, and without treating a coefficient row as a numerical gcd theorem.

2. **A complete second-precision block reduction for $N<p<2N$, $p\nmid 2N-1$.**  
   The reduction retains the actual residual indices
   

$$
2N-p,\quad 2N-p-1,\quad 2N-p-2,\quad 2N-p-6,
$$


   both affine forcings, all four complete source/endpoint constants, and the changing divided $\alpha,\beta,\delta$. It gives an explicit finite test for whether the two actual sources collide modulo $p^2$. The complete unpaid contribution of primes passing the noncollision test divides
   

$$
\binom{2N}{N},
$$


   and hence is at most $2N\log 2$.

Combining these two paid sets gives the explicit bound


$$
\boxed{
\prod_{p\in\mathcal D_N^{\mathrm{off}}\cup\mathcal C_N^{\mathrm{off}}}
p^{k_p}
<
10^{10}(2N)^{15}\frac{2500^N}{g_B^2}.
}
\tag{A}
$$


This is an upper bound on **all positive-part depths at the specified primes**, not merely on their support.

The limitation is equally important. No theorem below shows that these sets contain a fixed fraction of the possible $N\log N$ unpaid mass. The determinant-unit branch, the surviving numerical second collisions, and the remaining smaller primes are still open.

---

## 1. Original objects and the exact target

Throughout,


$$
\boxed{
N=9^{18+32u}=3^{36+64u},\qquad u\in\mathbb Z_{\ge0},
}
$$


and


$$
n=2N,\qquad m=N-3,\qquad \ell=2N-6.
$$


The physical terminal remains $n=2N$. In particular, $\ell$ is even and $\ell\ge20$.

Let


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


where


$$
C_0=1,\quad C_1=2t-1,\quad
C_{j+1}=(4t-2)C_j-C_{j-1}.
$$


Retain the actual Gaussian division


$$
g_B=\gcd(b_{N-1},b_N)>0,
$$




$$
\alpha=\frac{b_{N-1}}{g_B},\qquad
\beta=\frac{b_N}{g_B},\qquad
\delta=\frac{a_Nb_{N-1}-a_{N-1}b_N}{g_B}.
$$


Thus


$$
\gcd(\alpha,\beta)=1,\qquad
F=\alpha C_N-\beta C_{N-1},\qquad F(\pm i)=\delta.
$$



For integer polynomials define


$$
\eta(H)=\sum_j j![z^j]H(1-z),\qquad
E(H)=\sum_j(-1)^jj![t^j]H(t).
$$


Put


$$
\mathcal H=t(1-t)(1+t^2)^2,\qquad
K=\mathcal H C_m^2,
$$




$$
U=-\eta(K),\qquad
V=\eta(F^2)-\delta^2,\qquad
c=\gcd(U,V).
$$


The supplied normalization is retained:


$$
\operatorname{cont}(W_{\rm raw})=g_B^2c,\qquad
\tau=U/c,\quad \nu=V/c,\quad
W_{\rm prim}=\tau F^2+\nu K,\quad M=\tau\delta^2.
$$


On the original domain, $U,V,M>0$.

### 1.1 Reduced arc and intrinsic factors

Write


$$
L(x)=(x-1)(x-9)(x-25),\qquad
A_K(x)=13x^3-455x^2+3502x-5850.
$$


The actual reduced arc is


$$
R_K=\frac{A_K(\ell^2)}{30L(\ell^2)}=\frac{a_K}{d_K}.
$$


Its supplied original-domain reduction is retained:


$$
g_{\rm arc}
=90\,5^{\varepsilon_5}19^{\varepsilon_{19}}31^{\varepsilon_{31}},
$$


where


$$
\varepsilon_5=\mathbf1_{u\equiv1\pmod5},\quad
\varepsilon_{19}=\mathbf1_{u\equiv3\pmod9},\quad
\varepsilon_{31}=\mathbf1_{u\equiv5,7\pmod{15}},
$$


and


$$
a_K=A_K(\ell^2)/g_{\rm arc},\qquad
d_K=30L(\ell^2)/g_{\rm arc}.
$$


Thus $\gcd(a_K,d_K)=1$. Set


$$
E_K=E(K),\qquad y_K=d_KE_K-a_K,
$$


so that


$$
\gcd(d_K,y_K)=1.
$$



Retain


$$
\gamma=\gcd(\tau,y_K),\qquad
b^\circ=\gcd(\gamma,a_K),\qquad
r^\circ=\gamma/b^\circ.
$$


The actual least fixed-product multiplier is


$$
\kappa_N^{\mathrm{prod}}
=
\frac{c}{
\gcd\!\left(c,Q_{N-1}^{\mathrm H}Q_N^{\mathrm H}
                  (y_K/r^\circ)^2\right)}.
$$


For every prime $p$, its exact valuation remains


$$
\boxed{
k_p=
[c_p-h_p-2b_p-2(z_p-t_p)_+]_+,
}
\tag{1.1}
$$


where


$$
c_p=\min(v_p(U),v_p(V)),\qquad t_p=v_p(U)-c_p,
$$




$$
z_p=v_p(y_K),\qquad b_p=v_p(b^\circ),\qquad
h_p=v_p(Q_{N-1}^{\mathrm H}Q_N^{\mathrm H}).
$$



The fixed-product theorem and the canonical-return bounds are reused only on this original domain. Their reuse does not assert that a pending different review has been completed.

---

## 2. The complete columns used below

The two original affine states are


$$
\Theta_0=\Phi_0=0,\qquad \Theta_1=\Phi_1=1,
$$


and, for exactly $1\le j\le n-1$,


$$
\Theta_{j+1}+4j\Theta_j-\Theta_{j-1}=2,
$$




$$
\Phi_{j+1}+4j\Phi_j-\Phi_{j-1}=2(-1)^j.
\tag{2.1}
$$


Their polynomial interpretations are


$$
\eta(C_j)=1-2j\Theta_j,\qquad
E(C_j)=(-1)^j-2j\Phi_j,\qquad 0\le j\le n.
$$



At $x=\ell^2$, retain


$$
\begin{aligned}
\mathcal P(x)&=-8x^3-1116x^2-8150x+151,\\
\mathcal Q(x)&=76x^2+2408x+5637,\\
\mathcal F(x)&=4x^2+492x+5463,\\
\mathcal G(x)&=4x^2+556x-3325.
\end{aligned}
$$


For brevity set


$$
\mathscr A=2\ell((2\ell+1)\mathcal Q-\mathcal P),\qquad
\mathscr B=-2\ell\mathcal Q,
$$




$$
\mathscr C_U=\mathcal F-\mathcal P+2\ell\mathcal Q,\qquad
\mathscr C_E=\mathcal G+\mathcal P-2(\ell+1)\mathcal Q.
$$


The complete corrected $K$-columns are


$$
16U=\mathscr C_U-\mathscr A\Theta_\ell-\mathscr B\Theta_{\ell-1},
$$




$$
16E_K=\mathscr C_E+\mathscr A\Phi_\ell+\mathscr B\Phi_{\ell-1}.
\tag{2.2}
$$



The divided Gaussian columns at the physical terminal are


$$
V=C_V-P\Theta_n-Q\Theta_{n-1},
$$




$$
E_F=C_F^E-P\Phi_n-Q\Phi_{n-1},
\tag{2.3}
$$


where


$$
P=n\alpha^2+(n-2)\beta^2,
$$




$$
Q=4(n-1)(n-2)\beta^2-2(n-1)\alpha\beta,
$$




$$
C_V=\alpha^2+(2n-3)\beta^2-\delta^2,
$$




$$
C_F^E=\alpha^2+(5-2n)\beta^2+4\alpha\beta.
\tag{2.4}
$$



These identities are established reuse. No old thirteen-weight calculation is repeated.

---

# Part I. A new full-depth payment outside the arc support

## 3. An evaluated six-step transport of both Gaussian columns

The first task is to put the two source columns at the same actual basis without discarding their forcing constants.

Let


$$
x_j=4(\ell+j),\qquad 0\le j\le5.
$$


Define positive continuants $a_j^\ast,b_j^\ast$ by


$$
a_0^\ast=1,\quad a_1^\ast=x_0,\qquad
b_0^\ast=0,\quad b_1^\ast=1,
$$




$$
a_{j+1}^\ast=x_ja_j^\ast+a_{j-1}^\ast,\qquad
b_{j+1}^\ast=x_jb_j^\ast+b_{j-1}^\ast
\quad(1\le j\le5).
\tag{3.1}
$$


These are fixed six-step integer polynomials, not new endpoint sequences extending the terminal.

Define the two forcing corrections by


$$
f_0=g_0=0,\qquad f_1=g_1=2,
$$




$$
f_{j+1}=-x_jf_j+f_{j-1}+2,
$$




$$
g_{j+1}=-x_jg_j+g_{j-1}+2(-1)^j
\quad(1\le j\le5).
\tag{3.2}
$$


The endpoint sign in the second recurrence uses the validated fact that $\ell$ is even.

For an explicit factored evaluation of all forcing scalars needed below, put


$$
F_3=x_2(x_1-1)+2,\qquad
F_4=-x_3F_3+2-x_1,
$$




$$
F_5=-x_4F_4+F_3+1,\qquad
F_6=-x_5F_5+F_4+1.
$$


Then


$$
f_3=2F_3,\quad f_4=2F_4,\quad f_5=2F_5,\quad f_6=2F_6.
\tag{3.3}
$$


Similarly, put


$$
G_3=x_2(x_1+1)+2,\qquad
G_4=-x_3G_3-x_1-2,
$$




$$
G_5=-x_4G_4+G_3+1,\qquad
G_6=-x_5G_5+G_4-1.
$$


Then


$$
g_3=2G_3,\quad g_4=2G_4,\quad g_5=2G_5,\quad g_6=2G_6.
\tag{3.4}
$$


Thus the remainders constructed below contain no unevaluated factorial moment.

Direct induction in the original recurrences gives


$$
\Theta_{\ell+j}
=(-1)^ja_j^\ast\Theta_\ell
 +(-1)^{j-1}b_j^\ast\Theta_{\ell-1}+f_j,
$$




$$
\Phi_{\ell+j}
=(-1)^ja_j^\ast\Phi_\ell
 +(-1)^{j-1}b_j^\ast\Phi_{\ell-1}+g_j,
\qquad 1\le j\le6.
\tag{3.5}
$$


The largest recurrence step is $\ell+5=n-1$, exactly the allowed last step.

Substitution into (2.3) gives


$$
V=C^{\rm s}-\Pi\Theta_\ell-\Omega\Theta_{\ell-1},
$$




$$
E_F=C^{\rm e}-\Pi\Phi_\ell-\Omega\Phi_{\ell-1},
\tag{3.6}
$$


with the following evaluated quadratic forms:


$$
\boxed{
\begin{aligned}
\Pi={}&n a_6^\ast\alpha^2
       +2(n-1)a_5^\ast\alpha\beta
       +(n-2)a_4^\ast\beta^2,\\
\Omega={}&-n b_6^\ast\alpha^2
       -2(n-1)b_5^\ast\alpha\beta
       -(n-2)b_4^\ast\beta^2,
\end{aligned}}
\tag{3.7}
$$


and


$$
\boxed{
\begin{aligned}
C^{\rm s}={}&(1-nf_6)\alpha^2
 +2(n-1)f_5\alpha\beta
 +(1-(n-2)f_4)\beta^2-\delta^2,\\
C^{\rm e}={}&(1-ng_6)\alpha^2
 +\bigl(4+2(n-1)g_5\bigr)\alpha\beta
 +(1-(n-2)g_4)\beta^2.
\end{aligned}}
\tag{3.8}
$$



For example,


$$
a_6^\ast=4(n-1)a_5^\ast+a_4^\ast,
$$


and


$$
f_6=-4(n-1)f_5+f_4+2.
$$


These identities reduce the $\beta^2$-coefficients to the displayed forms. At the endpoint,


$$
g_6=-4(n-1)g_5+g_4-2,
$$


which is why its complete constant has the different expression in (3.8).

Both the source subtraction $-\delta^2$ and the endpoint contribution $4\alpha\beta$ remain present.

---

## 4. The coefficient determinant is nonzero in the actual Gaussian data

Define


$$
\Delta=\mathscr A\Omega-\mathscr B\Pi.
\tag{4.1}
$$


To use numerical forcing remainders, their nonvanishing must be established. It is not enough to name a determinant.

Write


$$
b_K=-\mathscr B=2\ell\mathcal Q(\ell^2)>0
$$


and define


$$
R_j=\mathscr A b_j^\ast-b_Ka_j^\ast.
\tag{4.2}
$$


Then


$$
R_{j+1}=x_jR_j+R_{j-1}.
$$


We first verify the signs needed in the determinant.

We have


$$
R_0=-b_K
$$


and


$$
R_1=2\ell S(\ell),
$$


where


$$
\begin{aligned}
S(\ell)
&=(1-2\ell)\mathcal Q(\ell^2)-\mathcal P(\ell^2)\\
&=8\ell^6-152\ell^5+1192\ell^4-4816\ell^3
  +10558\ell^2-11274\ell+5486.
\end{aligned}
\tag{4.3}
$$


For $\ell\ge20$, the three grouped differences


$$
8\ell^5(\ell-19),\qquad
\ell^3(1192\ell-4816),\qquad
\ell(10558\ell-11274)
$$


are positive. Moreover,


$$
S(\ell)>8\ell^5\ge160\ell^4,
$$


whereas


$$
\mathcal Q(\ell^2)<100\ell^4.
$$


Consequently,


$$
R_1>b_K,\qquad R_2=x_1R_1-b_K>R_1>0.
$$


Induction gives


$$
R_4>R_3>0,\qquad R_5>0,\qquad R_6>0.
\tag{4.4}
$$



Using (3.7),


$$
\boxed{
-\Delta
=nR_6\alpha^2+2(n-1)R_5\alpha\beta+(n-2)R_4\beta^2.
}
\tag{4.5}
$$


This quadratic form is positive definite.

Indeed, put


$$
x=\frac{R_5}{R_4}=4(n-2)+t,\qquad
t=\frac{R_3}{R_4}\in(0,1).
$$


The determinant of its symmetric coefficient matrix, divided by $R_4^2$, is


$$
\begin{aligned}
D(x)
&=n(n-2)\bigl(4(n-1)x+1\bigr)-(n-1)^2x^2\\
&=16(n-1)(n-2)^2+n(n-2)\\
&\quad-4(n-1)(n-2)^2t-(n-1)^2t^2\\
&>12(n-1)(n-2)^2-1>0.
\end{aligned}
\tag{4.6}
$$


The leading coefficient is positive. Since $(\alpha,\beta)\ne(0,0)$,


$$
\boxed{\Delta<0.}
\tag{4.7}
$$



The ratios in this positivity proof are real-number comparisons only. No $R_j$, Gaussian coefficient, or determinant is inverted in a divisibility argument.

---

## 5. Explicit integer forcing remainders and their numerical joint divisor

Define


$$
\boxed{
\mathscr I_1=\Pi\mathscr C_U-\mathscr A C^{\rm s},
\qquad
\mathscr I_2=\Omega\mathscr C_U-\mathscr B C^{\rm s}.
}
\tag{5.1}
$$


These are evaluated integer quadratic forms in the **divided** $\alpha,\beta,\delta$. For clarity, their four coefficients are:



$$
\begin{array}{c|c|c}
&\mathscr I_1&\mathscr I_2\\ \hline
\alpha^2&
n a_6^\ast\mathscr C_U-\mathscr A(1-nf_6)&
-n b_6^\ast\mathscr C_U-\mathscr B(1-nf_6)\\[1mm]
\alpha\beta&
2(n-1)(a_5^\ast\mathscr C_U-\mathscr A f_5)&
-2(n-1)(b_5^\ast\mathscr C_U+\mathscr B f_5)\\[1mm]
\beta^2&
(n-2)a_4^\ast\mathscr C_U-\mathscr A(1-(n-2)f_4)&
-(n-2)b_4^\ast\mathscr C_U-\mathscr B(1-(n-2)f_4)\\[1mm]
\delta^2&\mathscr A&\mathscr B .
\end{array}
\tag{5.2}
$$



The actual source identities now give


$$
\boxed{
16\Pi U-\mathscr A V
=\mathscr I_1+\Delta\Theta_{\ell-1},
}
\tag{5.3}
$$




$$
\boxed{
16\Omega U-\mathscr B V
=\mathscr I_2-\Delta\Theta_\ell.
}
\tag{5.4}
$$


There is no division by $\Delta$.

These remainders cannot both vanish. In fact,


$$
\mathscr A\mathscr I_2-\mathscr B\mathscr I_1
=\mathscr C_U\Delta,
\tag{5.5}
$$


and


$$
\mathscr C_U
=8\ell^6+152\ell^5+1120\ell^4+4816\ell^3
 +8642\ell^2+11274\ell+5312>0.
$$


Together with $\Delta<0$, this proves


$$
\boxed{
J_N^{\mathrm{aff}}
:=\gcd(\mathscr I_1,\mathscr I_2)>0.
}
\tag{5.6}
$$



This is the actual numerical joint divisor of the two displayed forcing remainders. It is not a coefficient content, an ordinary polynomial resultant, or a claimed unit.

### 5.1 Exact depth theorem

For every prime put


$$
d_p=v_p(\Delta),\qquad j_p=v_p(J_N^{\mathrm{aff}}).
$$



**Theorem 5.1 — Determinant-deep source cap.**  
At every original index,


$$
\boxed{
d_p>j_p\quad\Longrightarrow\quad c_p\le j_p.
}
\tag{5.7}
$$


Consequently,


$$
\boxed{
d_p>j_p\quad\Longrightarrow\quad
k_p\le
[j_p-h_p-2b_p-2(z_p-t_p)_+]_+.
}
\tag{5.8}
$$



**Proof.** Choose $\mathscr I_i$ with valuation $j_p$. In the corresponding identity (5.3) or (5.4), the term involving $\Delta$ has valuation at least $d_p>j_p$. The right side therefore has valuation exactly $j_p$.

The left side is an integer linear combination of $U,V$, hence is divisible by $c$. Therefore $c_p\le j_p$. Substitution into the unchanged formula (1.1) proves (5.8). ∎

The strict inequality $d_p>j_p$ is essential. It cannot be replaced by $p\mid\Delta$.

### 5.2 A large-prime set outside the arc-root support

Define


$$
\mathcal D_N^{\mathrm{off}}
=
\left\{
p>N:\ p\nmid L(\ell^2),\quad
v_p(\Delta)>v_p(J_N^{\mathrm{aff}})
\right\}.
\tag{5.9}
$$


The theorem gives the actual divisibility


$$
\boxed{
\prod_{p\in\mathcal D_N^{\mathrm{off}}}p^{k_p}
\mid J_N^{\mathrm{aff}}.
}
\tag{5.10}
$$


In particular, this pays every surviving depth at these primes, including $p>2N$.

No factorial divisibility is being asserted on the $p>2N$ part.

---

## 6. Full division and height bill for the new numerical divisor

The bound on $J_N^{\mathrm{aff}}$ must be evaluated after the actual Gaussian division.

Put


$$
H_G=\alpha^2+\beta^2+\delta^2.
$$


The Gaussian recurrence at $i$ has coefficient $2(-1+2i)$, of absolute value $2\sqrt5$. Induction gives


$$
|C_j(i)|\le5^j,
$$


since $2\sqrt5+1/5<5$. Therefore


$$
|\alpha|\le\frac{5^{N-1}}{g_B},\qquad
|\beta|\le\frac{5^N}{g_B},\qquad
|\delta|\le\frac{2\,5^{2N-1}}{g_B},
$$


and hence


$$
\boxed{
H_G<\frac{5^{4N}}{g_B^2}.
}
\tag{6.1}
$$



For $0\le j\le6$, the recurrences in Section 3 give


$$
|a_j^\ast|,\ |b_j^\ast|,\ |f_j|,\ |g_j|
\le(5n)^j.
\tag{6.2}
$$


For the forced recurrences, the induction follows from


$$
4n(5n)^j+(5n)^{j-1}+2\le(5n)^{j+1}
\qquad(n\ge2,\ j\ge1).
$$



The original Gaussian coefficients satisfy


$$
|P|\le nH_G,\qquad |Q|\le5n^2H_G,\qquad |C_V|\le2nH_G.
$$


Thus


$$
|\Pi|,\ |\Omega|\le93750\,n^8H_G,
\qquad
|C^{\rm s}|\le100000\,n^8H_G.
\tag{6.3}
$$


The corrected $K$-coefficients satisfy the elementary bounds


$$
|\mathscr A|<70000n^7,\quad
|\mathscr B|<17000n^5,\quad
|\mathscr C_U|<32000n^6.
\tag{6.4}
$$


Combining (5.1), (6.3), and (6.4),


$$
|\mathscr I_1|,\ |\mathscr I_2|
\le10^{10}n^{15}H_G.
$$


Since they are not both zero,


$$
\boxed{
J_N^{\mathrm{aff}}
\le10^{10}n^{15}H_G
<
10^{10}(2N)^{15}\frac{5^{4N}}{g_B^2}.
}
\tag{6.5}
$$



Therefore the new paid mass obeys


$$
\boxed{
\sum_{p\in\mathcal D_N^{\mathrm{off}}}k_p\log p
<
4N\log5+15\log(2N)+10\log10-2\log g_B.
}
\tag{6.6}
$$



This is an $O(N)$ bound on the **entire unpaid depth contribution of the specified band**, rather than the previous possible factorial scale.

### 6.1 Primes dividing $g_B$ are paid, not omitted

Every expression


$$
\Pi,\ \Omega,\ C^{\rm s},\ C^{\rm e},\
\Delta,\ \mathscr I_1,\ \mathscr I_2
$$


is homogeneous quadratic in $\alpha,\beta,\delta$.

If the corresponding raw Gaussian quantities are used, then exactly


$$
\Delta_{\rm raw}=g_B^2\Delta,\qquad
\mathscr I_{i,\rm raw}=g_B^2\mathscr I_i,
$$


and


$$
\boxed{
J_{N,\rm raw}^{\mathrm{aff}}=g_B^2J_N^{\mathrm{aff}}.
}
\tag{6.7}
$$


Thus at a prime $p\mid g_B$, the actual bill is


$$
v_p(J_N^{\mathrm{aff}})
=v_p(J_{N,\rm raw}^{\mathrm{aff}})-2v_p(g_B).
$$


The determinant-depth comparison is unchanged by this common subtraction, but the source-depth allowance is not.

No prime factor of $\alpha,\beta,\delta,\mathscr A,\mathscr B$, or $\Delta$ was inverted. Their exceptional factors remain in the actual numerical divisor $J_N^{\mathrm{aff}}$.

---

# Part II. The unrestricted non-arc interval $N<p<2N$

## 7. Actual residual Chebyshev indices and the factorial bill

Let


$$
N<p<2N,\qquad p\nmid2N-1.
$$


Since $n$ is even and $p$ is odd, write


$$
\boxed{r=n-p,}
\qquad r\ \text{odd},\qquad 3\le r<N.
\tag{7.1}
$$


The $K$-index is


$$
\ell=p+s,\qquad s=r-6.
\tag{7.2}
$$



For $r\ge7$, $s\ge1$. With


$$
w=1-2z,\qquad
S_p(z)=(w^2-1)\mathcal U_{p-1}(w),
$$


the exact addition formula is


$$
T_{p+j}(w)=T_p(w)T_j(w)+S_p(z)\mathcal U_{j-1}(w).
\tag{7.3}
$$


Thus the actual residual indices in the Gaussian square are


$$
r,\quad r-1,\quad r-2,
$$


and the actual residual $K$-index is $s=r-6$.

More explicitly, define


$$
A_r^\pm
=\frac{\alpha^2}{2}T_r(w)
 +\frac{\beta^2}{2}T_{r-2}(w)
 \mp\alpha\beta T_{r-1}(w),
$$




$$
B_r^\pm
=\frac{\alpha^2}{2}\mathcal U_{r-1}(w)
 +\frac{\beta^2}{2}\mathcal U_{r-3}(w)
 \mp\alpha\beta\mathcal U_{r-2}(w).
$$


Then


$$
F(1-z)^2
=\frac{\alpha^2+\beta^2}{2}-\alpha\beta w
 +T_p(w)A_r^++S_pB_r^+,
\tag{7.4}
$$


whereas


$$
F(z)^2
=\frac{\alpha^2+\beta^2}{2}+\alpha\beta w
 +T_p(w)A_r^-+S_pB_r^-.
\tag{7.5}
$$


Also,


$$
K(1-z)=\frac{\mathcal H(1-z)}2
 \left(1+T_p(w)T_s(w)+S_p\mathcal U_{s-1}(w)\right),
\tag{7.6}
$$


and


$$
K(z)=\frac{\mathcal H(z)}2
 \left(1+T_p(w)T_s(w)+S_p\mathcal U_{s-1}(w)\right).
\tag{7.7}
$$



Every displayed term in (7.4)–(7.7) has degree at most $p+r=n$.

For $r=3,5$, the $K$-indices are respectively $p-3,p-1$. Below they are evaluated directly in the original base block through $p$; no negative residual index and no above-terminal product is introduced.

### 7.1 The complete tail modulo $p^2$

Because $n<2p$, any original polynomial can be written uniquely as


$$
H(z)=H_0(z)+z^pH_1(z),\qquad \deg H_0,\deg H_1<p.
$$


For $0\le j<p$,


$$
(p+j)!\equiv-pj!\pmod{p^2}.
$$


Consequently,


$$
\boxed{
\begin{aligned}
\mathcal M_+(H)&\equiv
 \mathcal M_+(H_0)-p\mathcal M_+(H_1)\pmod{p^2},\\
\mathcal M_-(H)&\equiv
 \mathcal M_-(H_0)+p\mathcal M_-(H_1)\pmod{p^2}.
\end{aligned}}
\tag{7.8}
$$



The opposite signs are part of the full factorial bill.

The previously proved filtration for


$$
R_p=T_p(1-2z)-1\in(p,z^p)
$$


is applicable here. In particular, a factor $R_p$ supplies one factorial depth, not two. It would be incorrect to discard all $R_p$-terms modulo $p^2$.

The next section evaluates the block through the exact affine recurrences, retaining these first-order corrections rather than leaving the moments in (7.4)–(7.7) unevaluated.

---

## 8. A completely specified second-precision block

The following six residual sequences contain only integer operations.

Start with


$$
\mathcal A_0=1,\quad\mathcal A_1=0,\qquad
\mathcal B_0=0,\quad\mathcal B_1=1,
$$


and, for $1\le j\le r-1$,


$$
\mathcal A_{j+1}=-4j\mathcal A_j+\mathcal A_{j-1},
\qquad
\mathcal B_{j+1}=-4j\mathcal B_j+\mathcal B_{j-1}.
\tag{8.1}
$$



Define


$$
\mathcal D_0=0,\quad\mathcal D_1=-4,\qquad
\mathcal E_0=\mathcal E_1=0,
$$




$$
\mathcal T_0=\mathcal T_1=
\mathcal W_0=\mathcal W_1=0,
$$


and


$$
\begin{aligned}
\mathcal D_{j+1}
 &=-4j\mathcal D_j+\mathcal D_{j-1}-4\mathcal A_j,\\
\mathcal E_{j+1}
 &=-4j\mathcal E_j+\mathcal E_{j-1}-4\mathcal B_j,\\
\mathcal T_{j+1}
 &=-4j\mathcal T_j+\mathcal T_{j-1}-4\Theta_j,\\
\mathcal W_{j+1}
 &=-4j\mathcal W_j+\mathcal W_{j-1}-4\Phi_j
\end{aligned}
\quad(1\le j\le r-1).
\tag{8.2}
$$


Here $\Theta_j,\Phi_j$ are the actual original states at the residual indices $j$. They are not free coordinates.

Put


$$
\boxed{
\begin{aligned}
X_j^+={}&
(\mathcal A_j+p\mathcal D_j)\Theta_p\\
&+(\mathcal B_j+p\mathcal E_j)(\Theta_{p-1}+1)
+\Theta_j+p\mathcal T_j,
\end{aligned}}
\tag{8.3}
$$


and


$$
\boxed{
\begin{aligned}
X_j^-={}&
(\mathcal A_j+p\mathcal D_j)\Phi_p\\
&+(\mathcal B_j+p\mathcal E_j)(\Phi_{p-1}-1)
-\Phi_j-p\mathcal W_j.
\end{aligned}}
\tag{8.4}
$$



### Theorem 8.1 — Actual non-arc block evaluation

For $0\le j\le r$,


$$
\boxed{
\Theta_{p+j}\equiv X_j^+\pmod{p^2},\qquad
\Phi_{p+j}\equiv X_j^-\pmod{p^2}.
}
\tag{8.5}
$$



**Proof.**

At $j=0$, both formulas are identities. At $j=1$, they give


$$
X_1^+=-4p\Theta_p+\Theta_{p-1}+2,
$$




$$
X_1^-=-4p\Phi_p+\Phi_{p-1}-2.
$$


These are the original recurrence equations at $p$, since $p$ is odd.

For the source, write the right side of (8.3) as $H_j+pK_j$, where


$$
H_j=\mathcal A_j\Theta_p+
     \mathcal B_j(\Theta_{p-1}+1)+\Theta_j.
$$


Equations (8.1)–(8.2) imply


$$
H_{j+1}=-4jH_j+H_{j-1}+2,
$$




$$
K_{j+1}=-4jK_j+K_{j-1}-4H_j.
$$


Therefore


$$
X_{j+1}^+
\equiv-4(p+j)X_j^++X_{j-1}^++2\pmod{p^2}.
$$


This is the actual shifted source recurrence.

For the endpoint, the unperturbed term in (8.4) has forcing


$$
-2(-1)^j=2(-1)^{p+j},
$$


and its first-order correction is again driven by minus four times that unperturbed term. Hence


$$
X_{j+1}^-
\equiv-4(p+j)X_j^-+X_{j-1}^-+2(-1)^{p+j}
\pmod{p^2}.
$$


Induction proves both assertions. ∎

### 8.1 Complete four-column output

Use


$$
\widehat\Theta_n=X_r^+,\quad
\widehat\Theta_{n-1}=X_{r-1}^+,
$$


and similarly for $\Phi$.

If $r\ge7$, use


$$
\widehat\Theta_\ell=X_s^+,\quad
\widehat\Theta_{\ell-1}=X_{s-1}^+,\qquad s=r-6,
$$


and similarly for $\Phi$.

If $r=3$ or $5$, use the actual base-block values at


$$
(\ell,\ell-1)=(p-3,p-4)
\quad\text{or}\quad(p-1,p-2).
$$



The four residues are then


$$
\boxed{
\widehat U
=16^{-1}
\bigl(\mathscr C_U-\mathscr A\widehat\Theta_\ell
                    -\mathscr B\widehat\Theta_{\ell-1}\bigr),
}
$$




$$
\boxed{
\widehat V
=C_V-P\widehat\Theta_n-Q\widehat\Theta_{n-1},
}
$$




$$
\boxed{
\widehat E_K
=16^{-1}
\bigl(\mathscr C_E+\mathscr A\widehat\Phi_\ell
                    +\mathscr B\widehat\Phi_{\ell-1}\bigr),
}
$$




$$
\boxed{
\widehat E_F
=C_F^E-P\widehat\Phi_n-Q\widehat\Phi_{n-1},
}
\tag{8.6}
$$


all modulo $p^2$.

The coefficients in (8.6) are the original coefficients at $n,\ell$, not coefficients obtained by substituting the residual index for $N$. In particular, the four complete constants remain


$$
\mathscr C_U,\quad \mathscr C_E,\quad
\alpha^2+(2n-3)\beta^2-\delta^2,\quad
\alpha^2+(5-2n)\beta^2+4\alpha\beta.
$$



This is a finite evaluated recurrence receipt: no factorial moment, resultant, or freely chosen affine triple remains as an input.

### 8.2 Boundaries and divisions

All base-state indices are at most $p\le n-3$. All residual indices are at most $r<N$. The shifted recurrence is used only through $p+r-1=n-1$.

The only modular division in (8.6) is by $16$, a unit at these odd primes.

The inputs $\alpha,\beta,\delta$ are already the actual divided integers. If raw data are used to obtain them, the full $g_B$-division must first be performed at sufficient precision. A raw test modulo $p^2$ is not a divided-source test when $p\mid g_B$.

---

## 9. An $O(N)$ bound on the complete certified interval contribution

Choose canonical integer representatives of $\widehat U,\widehat V$ modulo $p^2$, and define the actual numerical block divisor


$$
\boxed{
d_{p,N}^{\mathrm{block}}
=\gcd(p^2,\widehat U,\widehat V).
}
\tag{9.1}
$$


Its possible values are $1,p,p^2$.

Define


$$
\mathcal C_N^{\mathrm{off}}
=
\left\{
N<p<2N:\ p\nmid L(\ell^2),\
d_{p,N}^{\mathrm{block}}<p^2
\right\}.
\tag{9.2}
$$



**Theorem 9.1 — Complete interval-depth certificate.**  
For every $p\in\mathcal C_N^{\mathrm{off}}$,


$$
c_p=v_p(d_{p,N}^{\mathrm{block}})\le1.
$$


Consequently,


$$
\boxed{
k_p\le
[1-h_p-2b_p-2(z_p-t_p)_+]_+
\le[1-h_p]_+.
}
\tag{9.3}
$$


Moreover,


$$
\boxed{
\prod_{p\in\mathcal C_N^{\mathrm{off}}}p^{k_p}
\mid\binom{2N}{N},
}
\tag{9.4}
$$


and therefore


$$
\boxed{
\sum_{p\in\mathcal C_N^{\mathrm{off}}}k_p\log p
\le2N\log2.
}
\tag{9.5}
$$



**Proof.** Theorem 8.1 and (8.6) evaluate the actual $U,V$ modulo $p^2$. If their joint divisor with $p^2$ is smaller than $p^2$, the minimum of their full valuations is exactly zero or one. This excludes every higher common source depth at that prime.

Formula (1.1) gives (9.3), with the full actual Hermite and endpoint credits retained.

For $N<p<2N$,


$$
v_p\binom{2N}{N}=1,
$$


because $p^2>2N$. Thus every exponent in (9.4) is at most the corresponding binomial exponent. Finally,


$$
\binom{2N}{N}<4^N.
$$


∎

The numerical noncollision condition in (9.2) is not asserted to hold for every original prime in the interval. The theorem is an exact all-depth certificate where it holds.

---

## 10. Combined new quantitative result

Combining (5.10), (6.5), and (9.4),


$$
\prod_{p\in\mathcal D_N^{\mathrm{off}}\cup\mathcal C_N^{\mathrm{off}}}
p^{k_p}
\mid
J_N^{\mathrm{aff}}\binom{2N}{N}.
$$


Hence


$$
\boxed{
\prod_{p\in\mathcal D_N^{\mathrm{off}}\cup\mathcal C_N^{\mathrm{off}}}
p^{k_p}
<
10^{10}(2N)^{15}\frac{2500^N}{g_B^2}.
}
\tag{10.1}
$$


Equivalently,


$$
\boxed{
\sum_{p\in\mathcal D_N^{\mathrm{off}}\cup\mathcal C_N^{\mathrm{off}}}
[c_p-h_p-2b_p-2(z_p-t_p)_+]_+\log p
<
N\log2500+15\log(2N)+10\log10-2\log g_B.
}
\tag{10.2}
$$



This is the new proved quantitative contribution.

It is not merely a bound on
$\sum_{p\mid\Delta}\log p$. At each prime in $\mathcal D_N^{\mathrm{off}}$, all higher source depths are capped by the actual numerical remainder divisor. Likewise, at each prime in $\mathcal C_N^{\mathrm{off}}$, all common source depths above one are excluded by the evaluated second-precision block.

Nevertheless, there is no proved coverage estimate for these sets. An $O(N)$ bill for a specified band does not establish a fixed saving from the entire possible $N\log N$ mass.

---

# Part III. Exact obstructions and the remaining proof obligation

## 11. Why the determinant-unit branch is still open

Suppose $p>N$ and $p\nmid\Delta$. Then $16$ and $\Delta$ are $p$-adic units. The two source equations are equivalent, at every precision, to proximity of the **actual** state to the actual rational target


$$
\Theta_\ell^\ast=\frac{\mathscr I_2}{\Delta},
\qquad
\Theta_{\ell-1}^\ast=-\frac{\mathscr I_1}{\Delta}.
$$


More precisely,


$$
\boxed{
c_p=
\min\left\{
v_p\!\left(\Theta_\ell-\frac{\mathscr I_2}{\Delta}\right),
v_p\!\left(\Theta_{\ell-1}+\frac{\mathscr I_1}{\Delta}\right)
\right\}.
}
\tag{11.1}
$$


This follows because the source coefficient matrix has unit determinant, so it preserves the minimum valuation of a two-coordinate vector.

Equation (11.1) identifies the obstruction; it does not resolve it. The targets are fixed by the original Gaussian data and complete forcing constants. The states are fixed by the original seeds and recurrence. There is no justification for replacing either by freely chosen affine coordinates.

In particular, the exponential height of $\mathscr I_1,\mathscr I_2,\Delta$ does **not** bound the depth of the differences in (11.1). A unit coefficient permits cancellation to arbitrary precision unless a source-specific noncoincidence theorem is supplied.

At determinant primes with


$$
v_p(\Delta)\le v_p(J_N^{\mathrm{aff}}),
$$


the strict valuation comparison in Theorem 5.1 also fails. These critical depths remain unpaid.

---

## 12. The exact factorial-unit obstruction for $p>2N$

For $p>n=2N$, every factorial appearing in the original source moments is a $p$-adic unit:


$$
v_p(j!)=0,\qquad 0\le j\le n.
$$


Thus the factorial-tail filtration supplies no automatic depth.

This failure occurs in the actual original polynomials, not only in a generic model.

* In the source coordinate, the coefficient of $z$ in
  

$$
K(1-z)=\mathcal H(1-z)C_m(1-z)^2
$$


  is $4$, since $C_m(1)=1$. Thus $K(1-z)$ is not coefficientwise divisible by such a $p$.

* Because $\gcd(\alpha,\beta)=1$, the reduction of $F$ modulo an odd prime is a nonconstant polynomial: if $\alpha$ is a unit its degree is $N$; otherwise $\beta$ is a unit and its degree is $N-1$. Hence
  

$$
F(1-z)^2-\delta^2
$$


  also has a unit coefficient at $p>n$.

Therefore neither actual source polynomial acquires a coefficientwise $p$-factor to replace the absent factorial tail.

This does not prove that either source value is a unit. A factorial functional can annihilate a polynomial with unit coefficients. It proves the precise obstruction to transferring the turn17 tail payment to $p>2N$: there is no tail in the physical degree range, and no automatic coefficient-content substitute in the original sources.

The determinant-deep band of Part I is consequently a genuine separate payment on part of this branch. It does not solve the determinant-unit part.

---

## 13. A concrete follow-on lemma

The new block reduction makes the next interval question finite and source-specific at each $(N,p)$, while preserving the infinite original family.

> **Non-arc block noncollision lemma — open.**  
> At every original $N$, let
> 

$$
> N<p<2N,\qquad p\nmid L(\ell^2),
>
$$


> and suppose $p\notin\mathcal D_N^{\mathrm{off}}$. Prove that the two residues in (8.6) are not both zero modulo $p^2$; or, for the simultaneous-zero cases, prove a quantitatively summable upper bound on the full remaining depth in (1.1), after the whole actual Hermite and endpoint credits.

The first alternative would imply


$$
\prod_{\substack{N<p<2N\\p\nmid L(\ell^2)}}p^{k_p}
\le J_N^{\mathrm{aff}}\binom{2N}{N}=e^{O(N)}.
$$


That conditional implication is rigorous. The noncollision assertion itself is not proved and is not presented as an established conjecture.

A simultaneous zero modulo $p^2$ is not automatically a counterexample to the desired multiplier bound: it may be paid by $h_p$, $b_p$, or endpoint surplus. But without a further evaluated lift, it cannot be assigned a depth cap.

For $p>2N$, the remaining question is the higher-precision noncoincidence in (11.1), with all credits in (1.1). No factorial allowance is available there.

---

# Part IV. Preservation of the complete producer

## 14. Source balance, endpoint forcing, and returns

The common-center transport changes only the basis in which the original columns are written. It does not change the source balance:


$$
\boxed{
\begin{aligned}
&(\nu\mathscr A-16\tau\Pi)\Theta_\ell
 +(\nu\mathscr B-16\tau\Omega)\Theta_{\ell-1}\\
&\hspace{12mm}
=\nu\mathscr C_U-16\tau C^{\rm s}.
\end{aligned}}
\tag{14.1}
$$


For


$$
T=\tau(E_F-\delta^2)+\nu E_K,
$$


the matching endpoint is


$$
\boxed{
\begin{aligned}
16T={}&16\tau(C^{\rm e}-\delta^2)+\nu\mathscr C_E\\
&+(\nu\mathscr A-16\tau\Pi)\Phi_\ell
 +(\nu\mathscr B-16\tau\Omega)\Phi_{\ell-1}.
\end{aligned}}
\tag{14.2}
$$



### 14.1 Source and endpoint returns in the same finite basis

The source return can be initialized by


$$
z_\ell=16\Omega U-\mathscr B V,\qquad
z_{\ell-1}=\mathscr A V-16\Pi U.
$$


It has


$$
z_j=-\Delta\Theta_j+\varrho_j,
$$


with


$$
\varrho_\ell=\mathscr I_2,\qquad
\varrho_{\ell-1}=-\mathscr I_1,
$$


and the complete forcing


$$
\varrho_{j-1}=\varrho_{j+1}+4j\varrho_j-2\Delta.
$$


The corresponding $z$-return is homogeneous:


$$
z_{j-1}=z_{j+1}+4jz_j.
$$



After the actual arc clearing defined below, put


$$
k_E=D\mathscr C_E-16DR_K,\qquad
f_E=DC^{\rm e}-DR_F.
$$


Then


$$
w_\ell=16\Omega Y+\mathscr B X,\qquad
w_{\ell-1}=-16\Pi Y-\mathscr A X,
$$




$$
w_j=D\Delta\Phi_j+\sigma_j,
$$


where


$$
\sigma_\ell=\Omega k_E+\mathscr B f_E,\qquad
\sigma_{\ell-1}=-\Pi k_E-\mathscr A f_E,
$$


and


$$
\sigma_{j-1}
=\sigma_{j+1}+4j\sigma_j+2D\Delta(-1)^j.
$$


Thus


$$
w_{j-1}=w_{j+1}+4jw_j,
$$


and


$$
z_\ell w_{\ell-1}-z_{\ell-1}w_\ell
=-16\Delta(UX+VY).
\tag{14.3}
$$


Again, there is no division by $\Delta$.

### 14.2 Canonical signed returns

The Hermite endpoints remain at $0\le r\le N$:


$$
P_0^{\mathrm H}=Q_0^{\mathrm H}=1,\qquad
P_1^{\mathrm H}=3,\quad Q_1^{\mathrm H}=1,
$$




$$
Z_{r+1}=(4r+2)Z_r+Z_{r-1}.
$$


The canonical returns are unchanged:


$$
\mathcal R_{r;N}=d_KP_r^{\mathrm H}U+Q_r^{\mathrm H}y_K.
$$


With


$$
\Psi_j^{(r)}
=Q_r^{\mathrm H}\Phi_j-P_r^{\mathrm H}\Theta_j,
$$


their complete representation is


$$
\begin{aligned}
16\mathcal R_{r;N}
={}&d_K\bigl(
P_r^{\mathrm H}\mathscr C_U+
Q_r^{\mathrm H}\mathscr C_E+
\mathscr A\Psi_\ell^{(r)}+
\mathscr B\Psi_{\ell-1}^{(r)}
\bigr)\\
&-16Q_r^{\mathrm H}a_K,
\end{aligned}
$$


and


$$
\Psi_{j+1}^{(r)}+4j\Psi_j^{(r)}-\Psi_{j-1}^{(r)}
=2\bigl(Q_r^{\mathrm H}(-1)^j-P_r^{\mathrm H}\bigr).
$$


Both forcing terms remain.

The established determinant-$2$ payment, signed-return bounds, and fixed-product theorem are reused; their closed calculations are not repeated.

---

## 15. Both arcs, least clearers, and the all-prime final gcd

Retain


$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,\qquad
R_K=4\int_0^1\frac K{1+t^2}\,dt.
$$


The monic quotient degrees are at most $2N-2$.

The complete square-arc return remains


$$
\xi_{j+1}=4\upsilon_j-2\xi_j-\xi_{j-1}+16b_j,
$$




$$
\upsilon_{j+1}
=-4\xi_j-2\upsilon_j-\upsilon_{j-1}
 +16(\ell_j-a_j),
$$


with zero seeds at $j=0,1$, and


$$
\ell_j=
\begin{cases}
0,&j\text{ odd},\\
(1-j^2)^{-1},&j\text{ even}.
\end{cases}
$$


The actual square arc is


$$
R_F=
\frac{\alpha^2\xi_n+\beta^2\xi_{n-2}
      -2\alpha\beta\xi_{n-1}}2.
$$



After reducing both arcs completely, use the actual least simultaneous clearer


$$
D=\operatorname{lcm}(\operatorname{den}R_F,\operatorname{den}R_K),
$$


and


$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K).
$$


Independently reduce


$$
\tau R_F+\nu R_K=b/\lambda,\qquad \gcd(b,\lambda)=1,\quad\lambda>0.
$$


Then


$$
E=\tau E_F+\nu E_K,\qquad
A=\lambda E-b,\qquad
G=\gcd(M,A),
$$


and


$$
\boxed{
p_N=A/G,\qquad q_N=\lambda M/G.
}
\tag{15.1}
$$


Since $\gcd(\lambda,A)=1$, this is the actual primitive denominator. The gcd $G$ is over all primes.

Neither $J_N^{\mathrm{aff}}$, the binomial coefficient in (9.4), nor a local modular clearer replaces $D,\lambda$, or $G$.

### 15.1 Division ledger

| Operation | Exact payment |
|---|---|
| Gaussian division | Actual $g_B$; raw remainder costs lose exactly $2v_p(g_B)$ |
| Source content | Actual $c=\gcd(U,V)$, with $\operatorname{cont}(W_{\rm raw})=g_B^2c$ |
| Six-step transport | Integer recurrences only |
| Remainder identities | Multiplication by $16$; no determinant division |
| Positive-definiteness ratios | Real comparisons only, not modular divisions |
| Non-arc block | Integer recurrences; $16^{-1}$ used only at odd $p>N$ |
| Factorial tail | Complete two-block formula (7.8), including opposite endpoint signs |
| Hermite credit | Actual $Q_{N-1}^{\mathrm H}Q_N^{\mathrm H}$, not a residual-index substitute |
| Rational recurrence interface | Previously paid local/global clearers retained; neither replaces $D$ |
| Arcs and aggregate arc | Actual reduced $D,\lambda$ |
| Final cancellation | Actual all-prime $G$ |

---

## 16. The whole nonzero error at the same original indices

The producer is unchanged:


$$
P_N(t)=\frac{F(t)^2+(V/U)K(t)}{\delta^2}.
$$


Its whole error is


$$
\boxed{
\epsilon_N=
\int_0^1P_N(t)\left(e^t+\frac4{1+t^2}\right)\,dt>0.
}
\tag{16.1}
$$


At the same original indices,


$$
\boxed{
q_N(e+\pi)-p_N=q_N\epsilon_N>0,
\qquad q_N=\frac{\lambda_NM_N}{G_N}.
}
\tag{16.2}
$$



The complete rational enclosure remains


$$
3J_N<\epsilon_N<7J_N,
\qquad
J_N=\frac{J_F+(V/U)J_K}{\delta^2},
$$


where


$$
J_F=
\alpha^2\frac{2N^2-1}{4N^2-1}
+\beta^2\frac{2(N-1)^2-1}{4(N-1)^2-1},
$$


and, with $j_r=(1-4r^2)^{-1}$,


$$
J_K=\frac{61}{420}
+\frac{
916j_m-399(j_{m+1}+j_{m-1})
-58(j_{m+2}+j_{m-2})
-(j_{m+3}+j_{m-3})
}{8192}.
$$


Consequently,


$$
q_NJ_N
=\frac{\lambda_N}{G_N}
  \bigl(\tau_NJ_F+\nu_NJ_K\bigr).
$$


Both positive summands remain.

The supplied signed-return implication still has only its stated conditional force. A future all-prime strict estimate for $\kappa_N^{\mathrm{prod}}$ would imply


$$
\log(q_N\epsilon_N)
\ge\frac{\eta}{2}N\log N-O(N)\longrightarrow+\infty
$$


along these same original indices. That would retire this producer, not decide whether $e+\pi$ is rational or irrational.

The new paid sets do not yet justify that implication.

---

## 17. Remaining mass, computation status, and conclusion

### 17.1 Exact remaining bottleneck

The reviewed binary payment and reviewed arc-band bounds remain available at their established scope. The new contribution is (10.2).

After removing those paid sets, the remaining obligation is still the actual sum


$$
\boxed{
\sum_{p\ \text{outside the proved paid sets}}
[c_p-h_p-2b_p-2(z_p-t_p)_+]_+\log p.
}
\tag{17.1}
$$


It includes, in particular:

1. determinant-unit primes $p>2N$, with the exact target collision (11.1);
2. critical determinant primes with
   

$$
v_p(\Delta)\le v_p(J_N^{\mathrm{aff}});
$$


3. primes $N<p<2N$ for which the evaluated block divisor is $p^2$, at all further depths not paid by the actual Hermite or endpoint terms;
4. every remaining smaller prime and depth outside the reviewed paid bands.

Primes of $g_B$ in these remaining sets are not omitted. Their divided data must continue to be used.

### 17.2 Computation status

No numerical computation was performed, and no enormous original-index computation is proposed.

No new bounded arithmetic calculation is mathematically indispensable for the proofs above:

* the six-step scalar remainders are given as explicit factored integer expressions;
* determinant nonvanishing and the exponential bill are proved algebraically;
* the non-arc $p$-block is proved by induction in the original finite recurrences.

The existing $p=23,a=3$ audit is not repeated or enlarged. It remains a separate unrun finite receipt.

A finite evaluation of (9.1) would certify only the stated $(N,p)$ inputs. It could not establish the infinite noncollision lemma or the global multiplier estimate.

### 17.3 Final proof-status ledger

| Statement | Status |
|---|---|
| Original index family, physical terminal, actual Gaussian division | Retained |
| Complete source and endpoint columns, both forcings and returns | Retained |
| Actual contents, least $D,\lambda$, all-prime $G$, primitive $q_N$ | Retained |
| Nonzero whole error at the same original indices | Retained |
| Six-step complete common-center Gaussian columns | **Proved here** |
| Nonvanishing of the actual coefficient determinant | **Proved here** |
| Explicit numerical forcing remainders and full Gaussian division bill | **Proved here** |
| Full-depth cap on $\mathcal D_N^{\mathrm{off}}$ | **Proved here** |
| Complete non-arc block modulo $p^2$ | **Proved here** |
| Binomial upper bound on the complete certified interval contribution | **Proved here** |
| Combined bound (10.1) | **Proved here** |
| Uniform coverage of the unrestricted large-prime complement | **Open** |
| Non-arc block noncollision at all original indices | **Open** |
| Fixed $\eta>0$ in the strict global multiplier estimate | **Not proved** |
| Producer retirement | **Still conditional** |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

## Final conclusion

The new result is an explicit exponential payment for a source-specific large-prime depth band, including part of the factorial-unit branch $p>2N$, together with a complete second-precision reduction and binomial depth certificate for the unrestricted interval $N<p<2N$.

The main numerical conclusion is


$$
\boxed{
\prod_{p\in\mathcal D_N^{\mathrm{off}}\cup\mathcal C_N^{\mathrm{off}}}
p^{\,v_p(\kappa_N^{\mathrm{prod}})}
<
10^{10}(2N)^{15}\frac{2500^N}{g_B^2}.
}
$$



The exact unresolved issue is not coefficient primitiveness or factorial clearing. It is simultaneous higher-precision cancellation in the actual Gaussian-dependent forced states, after the full credits in (1.1), at primes not covered by the two proved tests. No fixed fractional-factorial saving, producer retirement, or conclusion about $e+\pi$ follows until that remaining all-prime depth mass is controlled.
