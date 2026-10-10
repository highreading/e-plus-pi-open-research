> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1, Turn 5 — A factorial-saturated producer lemma and vanishing of the actual force strip

## Executive conclusion

The actual producer-strip lemma can be proved **without** proving the stronger coefficientwise congruence


$$
3P_n-Q_c\in 3^7\mathbb Z_3[y].
$$



The essential new ingredient is a factorial normalization of the **even-subsequence derangement moment matrix before the rank-one subtraction**. In the shifted variable $x=y-1$, its normalized matrix is a $3$-adic unit matrix at every finite order. The signed producer then becomes a unit-matrix problem with one explicit scalar rank-one denominator. Retaining that denominator, the accepted integrality of $3P_n$ controls the scalar response and yields a strong localization of the actual correction polynomial.

On the entire retained domain


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,\qquad
A=n-2=H-D,\qquad 0<D<H/972,
$$


the result is


$$
\boxed{
[y^r]W_R=0\pmod3
\quad\text{for every }D<r<H,
}
$$


where, as before,


$$
R=\frac{3P_n-Q_c}{729},\qquad
W_R=
\frac{R(y)(y-1)^{2D}-R(-1)(-2)^{2D}}{y+1}.
$$



In particular, this covers the exact required strip


$$
r_1-(D-4)\le r\le r_1,
\qquad r_1=\frac{H-1}{2}.
$$


Thus


$$
\boxed{\mathcal F_R=0.}
$$



This conclusion uses the retained order-six producer congruence at its accepted scope. It does **not** assume an arbitrary-depth approximation, and it does not infer extra precision merely from $v_3(j)$.

Consequently, the previously established formula now becomes


$$
\boxed{
\mathscr R_{\rm act}/3^7\equiv\mathcal C_7\pmod3
}
$$


for the actual producer on the full original domain. The earlier core-radical analysis therefore applies to the actual depth-seven digit. In particular, that digit is singular; this does not produce an invertible depth-seven denominator branch.

A further useful result is obtained for the next complete force: **$R\bmod27$ is determined by a terminal shifted-factorial jet containing at most ten coefficients.** Its coefficients remain to be evaluated, but an arbitrary degree-$n$ correction is no longer required.

No tools were used. The irrationality or rationality of $e+\pi$ remains unresolved.

---

## 1. Scope, actual producer, and the retained interface

The actual producer is


$$
(C_n)_{ab}=D_{2(a+b)}-(-1)^{a+b},
\qquad
(f_n)_a=D_{2(n+a)}-(-1)^{n+a},
\qquad 0\le a,b<n,
$$


and


$$
P_n(y)=y^n-\sum_{a=0}^{n-1}(C_n^{-1}f_n)_a y^a.
$$



Equivalently, for


$$
\rho(y^r)=D_{2r}-(-1)^r,
$$


it satisfies


$$
\rho(y^aP_n)=0,\qquad 0\le a<n.
$$



Retain


$$
Q_c=(y+1)(y-1)^A(\beta+3y),
\qquad
A=n-2,\qquad \beta=-71-A,
$$


and the accepted order-six statement


$$
\mathcal E_n:=3P_n-Q_c=729R,
\qquad R\in\mathbb Z_3[y].
\tag{1.1}
$$



The leading coefficients of $3P_n$ and $Q_c$ are both $3$. Therefore


$$
\boxed{\deg\mathcal E_n,\deg R\le n-1.}
\tag{1.2}
$$



This exact degree improvement is useful below.

The proof uses two consequences of the retained interface:

1. $\mathcal E_n$ is $3$-integral, including its coefficient of $(y-1)^{n-1}$;
2. division by $729$ in (1.1) is coefficientwise legitimate.

It does **not** assume


$$
\mathcal E_n\in3^7\mathbb Z_3[y].
$$



The complete residual functional remains


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\!\!\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^s)=(2s)!.
\tag{1.3}
$$


Nothing in the producer analysis below replaces or deletes this factorial force, its endpoint subtraction, or its finite cutoff.

---

# Part I. The even-subsequence factorial normalization

## 2. Exact shifted moments from the derangement integral

The derangement exponential generating function, or direct expansion under the Gamma integral, gives


$$
D_m=\int_0^\infty e^{-t}(t-1)^m\,dt.
\tag{2.1}
$$


Indeed,


$$
\int_0^\infty e^{-t}(t-1)^m\,dt
=
\sum_{k=0}^m\binom mk(-1)^{m-k}k!
=
m!\sum_{\ell=0}^m\frac{(-1)^\ell}{\ell!}.
$$



Define the positive functional


$$
\mu(F)=\int_0^\infty e^{-t}F((t-1)^2)\,dt.
$$


Then


$$
\rho(F)=\mu(F)-F(-1).
\tag{2.2}
$$



Set


$$
x=y-1
$$


and define its positive moments


$$
\Lambda_r:=\mu(x^r)
=
\int_0^\infty e^{-t}\bigl(t(t-2)\bigr)^r\,dt.
\tag{2.3}
$$


Their exact finite factorial expansion is


$$
\boxed{
\Lambda_r
=
\sum_{k=0}^r
\binom rk(-2)^{r-k}(r+k)!.
}
\tag{2.4}
$$



In particular, $\Lambda_r/r!$ is an integer. Write


$$
\gamma_r=\frac{\Lambda_r}{r!}.
\tag{2.5}
$$



### 2.1 A short exact recurrence

Let $\sigma=t(t-2)$. For $r\ge1$, integration by parts gives


$$
\Lambda_{r+1}
=
2(r+1)\int_0^\infty e^{-t}(t-1)\sigma^r\,dt,
$$


and


$$
\int_0^\infty e^{-t}(t-1)\sigma^r\,dt
=
(2r+1)\Lambda_r+2r\Lambda_{r-1}.
$$


The boundary terms vanish because $\sigma(0)=0$ and $r\ge1$.

Hence


$$
\Lambda_{r+1}
=
2(r+1)(2r+1)\Lambda_r
+
4r(r+1)\Lambda_{r-1}.
\tag{2.6}
$$


Since


$$
\Lambda_0=1,\qquad \Lambda_1=0,
$$


division by $(r+1)!$ yields the integer recurrence


$$
\boxed{
\gamma_0=1,\qquad \gamma_1=0,\qquad
\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1}
\quad(r\ge1).
}
\tag{2.7}
$$



Modulo $3$, this gives the exact period-three pattern


$$
\boxed{
\gamma_r\equiv
\begin{cases}
1,&r\equiv0,2\pmod3,\\
0,&r\equiv1\pmod3.
\end{cases}
}
\tag{2.8}
$$


For example, $(\gamma_0,\gamma_1,\gamma_2)=(1,0,4)$, and the pair of initial residues repeats after three steps in the recurrence.

This is a statement about the actual even-subsequence moments, not ordinary unstepped derangement Hankel determinants.

---

## 3. A $3$-adic unit theorem for the normalized positive matrix

For every finite $n\ge1$, define


$$
\mathsf T_n
=
\left(\frac{\Lambda_{a+b}}{a!\,b!}\right)_{0\le a,b<n}
=
\left(\binom{a+b}{a}\gamma_{a+b}\right)_{0\le a,b<n}.
\tag{3.1}
$$


It is an integer matrix.

### Theorem 3.1 — Normalized even-moment unit theorem

For every $n\ge1$,


$$
\boxed{\mathsf T_n\in\operatorname{GL}_n(\mathbb Z_3).}
\tag{3.2}
$$



More precisely, if


$$
m_r=\#\{a:0\le a<n,\ a\equiv r\pmod3\},
$$


then


$$
\boxed{
\det\mathsf T_n\equiv(-1)^{m_1+m_2}\pmod3.
}
\tag{3.3}
$$



### Proof

Write


$$
a=3i+r,\qquad b=3j+s,\qquad 0\le r,s<3.
$$


If $r+s\ge3$, Lucas’s theorem makes


$$
\binom{a+b}{a}=0\pmod3.
$$


If $r+s<3$, (2.8) shows that the only nonzero residue blocks are


$$
(r,s)=(0,0),(0,2),(2,0),(1,1).
$$



Let


$$
Z_{p,q}=\left(\binom{i+j}{i}\right)_{\substack{0\le i<p\\0\le j<q}},
\qquad Z_p=Z_{p,p}.
$$


After grouping the original finite indices by residue, $\mathsf T_n\bmod3$ is


$$
\begin{pmatrix}
Z_{m_0}&0&Z_{m_0,m_2}\\
0&2Z_{m_1}&0\\
Z_{m_2,m_0}&0&0
\end{pmatrix}.
\tag{3.4}
$$



The finite Pascal factorization is


$$
Z_p=P_pP_p^T,
\qquad
(P_p)_{ij}=\binom ij,
\tag{3.5}
$$


with $P_p$ unit lower triangular. Moreover,


$$
Z_{m_0,m_2}
=
P_{m_0}
\begin{pmatrix}I_{m_2}\\0\end{pmatrix}
P_{m_2}^T.
\tag{3.6}
$$


Here $m_0=m_2$ or $m_2+1$, exactly as imposed by the endpoint $n-1$.

Applying these finite unimodular Pascal transformations reduces the $0,2$ part to $m_2$ blocks


$$
\begin{pmatrix}1&1\\1&0\end{pmatrix}
$$


and, when $m_0=m_2+1$, one additional entry $1$. The residue-$1$ part becomes $2I_{m_1}$.

Every block is invertible modulo $3$, and its determinant gives (3.3). ∎

### What has been gained

The original positive even-subsequence matrix is highly nonunit, but its entire factorial content is now explicit:


$$
\bigl(\Lambda_{a+b}\bigr)
=
\operatorname{diag}(a!)\,
\mathsf T_n\,
\operatorname{diag}(a!).
\tag{3.7}
$$


Consequently,


$$
\boxed{
v_3\det\bigl(\Lambda_{a+b}\bigr)
=
2\sum_{a=0}^{n-1}v_3(a!).
}
\tag{3.8}
$$



This is the special arithmetic fact needed for the producer. An unnormalized determinant congruence would not provide it.

---

# Part II. Exact rank-one subtraction and complete producer force

## 4. Retaining the rank-one denominator and determinant content

Let


$$
F=(n-1)!,
\qquad
u_a=\frac{F(-2)^a}{a!},
\qquad 0\le a<n.
\tag{4.1}
$$


The vector $u$ is integral.

In the shifted basis $1,x,\ldots,x^{n-1}$, the actual signed coefficient matrix is


$$
\Gamma_n
=
\bigl(\Lambda_{a+b}-(-2)^{a+b}\bigr)_{0\le a,b<n}.
$$


Thus, with $\mathsf J=\operatorname{diag}(a!)$,


$$
\boxed{
\Gamma_n
=
\mathsf J
\left(\mathsf T_n-\frac{uu^T}{F^2}\right)
\mathsf J.
}
\tag{4.2}
$$



The change from $y^a$ to $(y-1)^a$ is integral unit triangular. Therefore


$$
\det\Gamma_n=\det C_n.
$$



Define the exact scalar


$$
\boxed{
\eta_n=F^2-u^T\mathsf T_n^{-1}u.
}
\tag{4.3}
$$


It is $3$-integral, but it is **not** assumed to be a $3$-adic unit.

The determinant identity is


$$
\boxed{
\det C_n
=
\left(\prod_{a=0}^{n-1}(a!)^2\right)
\det\mathsf T_n\,
\frac{\eta_n}{F^2}.
}
\tag{4.4}
$$


In particular,


$$
\boxed{
v_3(\det C_n)
=
2\sum_{a=0}^{n-1}v_3(a!)
-2v_3(F)+v_3(\eta_n).
}
\tag{4.5}
$$



The exact inverse is


$$
\boxed{
\Gamma_n^{-1}
=
\mathsf J^{-1}
\left(
\mathsf T_n^{-1}
+
\frac{\mathsf T_n^{-1}uu^T\mathsf T_n^{-1}}{\eta_n}
\right)
\mathsf J^{-1}.
}
\tag{4.6}
$$



Thus the factorial divisions and the scalar inverse loss are retained explicitly. In particular, the loss-one lemma for the later eliminated residual block must not be confused with the inverse loss of this producer matrix.

### 4.1 Nonvanishing of the scalar

There is also a direct verification that $\eta_n\ne0$ for $n\ge2$.

The positive Gram space contains $1$ and $x=y-1$, whose positive Gram matrix is


$$
\begin{pmatrix}1&0\\0&8\end{pmatrix}.
$$


Evaluation at $y=-1$, equivalently $x=-2$, has squared norm at least


$$
1+\frac{(-2)^2}{8}=\frac32.
$$


The full squared evaluation norm is


$$
\frac{u^T\mathsf T_n^{-1}u}{F^2}.
$$


Therefore


$$
\eta_n\le-\frac{F^2}{2}<0.
\tag{4.7}
$$



This proves nonsingularity of the actual signed matrix for every $n\ge2$, without imposing a unit-denominator hypothesis.

---

## 5. The complete factorial force of $Q_c$

Put


$$
b=\beta+3=-68-A.
$$


In the shifted variable,


$$
Q_c=(x+2)x^A(b+3x)
=
3x^n+(b+6)x^{n-1}+2b\,x^{n-2}.
\tag{5.1}
$$



Because $Q_c(-1)=0$, its signed moment force has no residual point-mass term:


$$
\rho(x^aQ_c)=\mu(x^aQ_c).
$$


Define


$$
H_a
=
3\Lambda_{n+a}
+(b+6)\Lambda_{n-1+a}
+2b\Lambda_{n-2+a},
\qquad 0\le a<n.
\tag{5.2}
$$



This is the **whole producer force**, not a selected leading term.

On the original family $n\equiv2\pmod3$, so $n-1$ is a unit. Accordingly,


$$
\tau_a:=\frac{H_a}{a!\,F}\in\mathbb Z_3.
$$


Its explicit finite factorial formula is


$$
\boxed{
\begin{aligned}
\tau_a={}&
3n\binom{n+a}{a}\gamma_{n+a}\\
&+(b+6)\binom{n-1+a}{a}\gamma_{n-1+a}\\
&+\frac{2b}{n-1}\binom{n-2+a}{a}\gamma_{n-2+a}.
\end{aligned}
}
\tag{5.3}
$$


The values $\gamma_r$ are generated by the exact recurrence (2.7).

This is where the special producer, rather than an arbitrary matrix perturbation, enters the argument.

---

## 6. An exact coefficient formula with a controlled scalar response

Write


$$
\mathcal E_n(y)=\sum_{a=0}^{n-1}e_a x^a.
\tag{6.1}
$$


Orthogonality of $3P_n$ gives


$$
\rho(x^a\mathcal E_n)=-H_a,\qquad 0\le a<n.
\tag{6.2}
$$



Define


$$
\mathbf t=\mathsf T_n^{-1}\tau,
\qquad
\mathbf v=\mathsf T_n^{-1}u,
\qquad
\chi_n=u^T\mathbf t,
\qquad
\xi_n=\frac{\chi_n}{\eta_n}.
\tag{6.3}
$$


Both $\mathbf t$ and $\mathbf v$ are $3$-integral by Theorem 3.1. No integrality of $\xi_n$ is presumed yet.

Solving (6.2), using (4.6), gives the exact identities


$$
\boxed{
e_a=-\frac{F}{a!}\bigl(t_a+\xi_n v_a\bigr),
\qquad 0\le a<n,
}
\tag{6.4}
$$


and


$$
\boxed{
\mathcal E_n(-1)=-F^2\xi_n.
}
\tag{6.5}
$$



These retain the rank-one denominator $\eta_n$, all determinant content, and the complete force (5.3).

The remaining issue is whether its scalar quotient $\xi_n$ is integral. A terminal unit pivot answers that question.

---

## 7. The terminal unit pivot

### Lemma 7.1

If $n\equiv2\pmod3$, then


$$
\boxed{
(\mathsf T_n^{-1}u)_{n-1}\equiv2\pmod3.
}
\tag{7.1}
$$



### Proof

Write $n=3N+2$. Since $n-2$ is divisible by $3$,


$$
u_a\equiv0\pmod3\qquad(a\le n-3),
$$


whereas


$$
u_{n-2}\equiv u_{n-1}\equiv1\pmod3.
$$



The terminal index $n-1=3N+1$ belongs to the residue-$1$ block of (3.4). That block is independent of the others and is


$$
2Z_{N+1}.
$$


The last diagonal entry of $Z_{N+1}^{-1}$ is


$$
\frac{\det Z_N}{\det Z_{N+1}}=1.
$$


Hence the last coordinate of $\mathsf T_n^{-1}u$ is $2^{-1}=2\pmod3$. ∎

Taking $a=n-1$ in (6.4), where $F/a!=1$, gives


$$
e_{n-1}=-t_{n-1}-\xi_n v_{n-1}.
$$


The retained order-six interface makes $e_{n-1}$ integral, $t_{n-1}$ is integral, and $v_{n-1}$ is a unit. Therefore


$$
\boxed{\xi_n\in\mathbb Z_3.}
\tag{7.2}
$$



This is not an assertion that $\eta_n$ is a unit. It is a proof that the **actual complete numerator** $\chi_n$ has sufficient divisibility relative to that denominator.

Substitution into (6.4) now yields the principal localization theorem.

### Theorem 7.2 — Factorial-saturated actual producer correction

On the retained original family,


$$
\boxed{
v_3(e_a)\ge v_3\!\left(\frac{(n-1)!}{a!}\right),
\qquad 0\le a<n.
}
\tag{7.3}
$$


Furthermore,


$$
\boxed{
v_3\bigl(\mathcal E_n(-1)\bigr)\ge2v_3((n-1)!).
}
\tag{7.4}
$$



The lower bound (7.4) suffices for the endpoint subtraction used below. The stronger accepted exact endpoint law is not needed to prove the strip lemma.

For completeness, $P_n(-1)\ne0$: otherwise $P_n=(y+1)S$ with $\deg S=n-1$, and orthogonality would give


$$
0=\rho(P_nS)=\mu((y+1)S^2)>0,
$$


a contradiction. Thus the endpoint response in (6.5) is not identically zero.

---

# Part III. The actual producer-strip lemma

## 8. A bounded terminal jet modulo $3^7$

Let


$$
t=v_3(A)=1+v_3(j)\ge5.
$$


Define


$$
\kappa=
\begin{cases}
6,&t=5,\\
3,&t=6,\\
0,&t\ge7.
\end{cases}
\tag{8.1}
$$



The factorial bound (7.3) gives


$$
e_a\in3^7\mathbb Z_3
\qquad\text{whenever }a<A-\kappa.
\tag{8.2}
$$



Here are the exact terminal products establishing that bound:

- If $t=5$, the product
  

$$
\frac{(A+1)!}{(A-7)!}
  =(A-6)(A-5)\cdots(A+1)
$$


  contains $A$, $A-3$, and $A-6$, with valuations $5,1,1$. Its valuation is $7$.

- If $t=6$, the product
  

$$
\frac{(A+1)!}{(A-4)!}
  =(A-3)(A-2)\cdots(A+1)
$$


  contains factors of valuations $6$ and $1$.

- If $t\ge7$, the product
  

$$
\frac{(A+1)!}{(A-1)!}=A(A+1)
$$


  already has valuation at least $7$.

All earlier coefficients have at least as much factorial divisibility.

Since $\mathcal E_n=729R$, reduction modulo $3$ therefore gives


$$
\overline R=x^{A-\kappa}J(x),
\qquad
\deg J\le\kappa+1.
\tag{8.3}
$$



Also, (7.4) implies


$$
R(-1)\equiv0\pmod3,
\tag{8.4}
$$


because $2v_3((n-1)!)>6$ throughout the original domain.

At $y=-1$, $x=-2$ is a unit modulo $3$. Hence (8.3)–(8.4) imply that $x+2$ divides $J(x)$. We have proved


$$
\boxed{
\overline R(y)
=
(y+1)(y-1)^{A-\kappa}B(y-1),
\qquad
\deg B\le\kappa.
}
\tag{8.5}
$$



For the specifically requested subfamily $v_3(j)\ge5$, one has $t\ge6$, so at most a cubic $B$ is needed. On the full original domain, at most a sextic is needed.

Importantly, (8.5) does not say $B=0$. The stronger coefficientwise depth-seven congruence remains unnecessary and is not asserted.

---

## 9. Proof of the actual force-strip vanishing

Recall


$$
W_R=
\frac{R(y)(y-1)^{2D}-R(-1)(-2)^{2D}}{y+1}.
$$


Reduction modulo $3$, using (8.4)–(8.5), gives


$$
\overline W_R
=
(y-1)^{A+2D-\kappa}B(y-1).
$$


Since $A=H-D$,


$$
\overline W_R
=
(y-1)^{H+D-\kappa}B(y-1).
\tag{9.1}
$$



Here $H$ is a power of $3$, and $D\ge2\cdot3^t>\kappa$. Thus


$$
(y-1)^H=y^H-1
\quad\text{in }\mathbb F_3[y],
$$


and (9.1) becomes


$$
\boxed{
\overline W_R=(y^H-1)T_D(y),
\qquad
T_D(y)=(y-1)^{D-\kappa}B(y-1),
\qquad
\deg T_D\le D.
}
\tag{9.2}
$$



Therefore


$$
\boxed{
[y^r]W_R=0\pmod3
\qquad(D<r<H).
}
\tag{9.3}
$$



This is the desired producer-strip lemma, with a larger zero interval than required.

The actual residual indices satisfy


$$
0\le i,j<\nu,\qquad \nu=D/2-1,
$$


so


$$
0\le i+j\le D-4.
$$


Consequently the required coefficient indices are exactly


$$
r_1-(D-4),\ldots,r_1.
$$


The real-window hypothesis gives


$$
r_1-(D-4)>D,
\qquad
r_1<H.
$$


Indeed, the first inequality is equivalent to $H+7>4D$, which follows from $D<H/972$.

Thus every actual entry vanishes:


$$
\boxed{
(\mathcal F_R)_{ij}
=[y^{r_1-i-j}]W_R=0\pmod3,
\qquad 0\le i,j<\nu.
}
\tag{9.4}
$$



### What has—and has not—been proved

**Proved:** the actual $W_R$ strip vanishes on the entire original domain, using the accepted order-six producer interface.

**Not proved or needed:** the stronger coefficientwise assertion


$$
3P_n-Q_c\in3^7\mathbb Z_3[y].
$$



The proof controls the actual producer through its exact factorial force and signed moment system. It does not replace $R$ by a model perturbation.

---

# Part IV. Consequences and the next complete force

## 10. The depth-seven digit is now identified for the actual producer

The reviewed transfer and finite-boundary closure give


$$
\mathscr R_{\rm act}/3^7
\equiv\mathcal C_7+\mathcal F_R\pmod3.
$$


The new producer-strip theorem proves $\mathcal F_R=0$. Hence


$$
\boxed{
\mathscr R_{\rm act}/3^7\equiv\mathcal C_7\pmod3.
}
\tag{10.1}
$$



There is no need to repeat the earlier residue decomposition. Its algebraic conclusions now transfer to the actual digit:

- $\mathcal C_7$, and hence the actual depth-seven digit, is singular throughout the original domain;
- its previously specified radical, image, and endpoint projection are the actual depth-seven data;
- the whole actual depth-seven digit vanishes precisely when
  

$$
D<H/2916;
$$


- on
  

$$
D<H/2187,
$$


  the transported endpoint is outside the image of that digit.

These are consequences at depth seven. They do not determine the first nonzero actual residual depth or the full endpoint inverse contraction.

---

## 11. A bounded actual producer jet for the next force

The factorial localization is not limited to one digit.

For a fixed precision $p\ge1$, let $\ell_{6+p}$ be the smallest terminal length for which


$$
v_3\!\left(
\frac{(n-1)!}{(n-1-\ell_{6+p})!}
\right)\ge6+p.
\tag{11.1}
$$


Assume the displayed factorial is defined and


$$
2v_3((n-1)!)\ge6+p.
$$


Then the same proof gives


$$
\boxed{
R(y)\equiv
(y+1)(y-1)^{n-\ell_{6+p}}B_p(y-1)
\pmod{3^p},
\qquad
\deg B_p\le\ell_{6+p}-2.
}
\tag{11.2}
$$



This is a coefficientwise congruence over $\mathbb Z/3^p\mathbb Z$. The divisibility by $y+1$ is legitimate because $y-1$ evaluates to the unit $-2$ at $y=-1$.

### The precision needed for the next complete force

For $R\bmod27$, take $p=3$, so the required factorial depth is $9$. On the original family:


$$
\begin{array}{c|c|c}
t=v_3(A)&\ell_9&\deg B_3\text{ at most}\\ \hline
5&11&9\\
6&11&9\\
7&8&6\\
8&5&3\\
\ge9&2&0
\end{array}
\tag{11.3}
$$



For example, when $t=5$, the terminal product of length $11$ contains


$$
A,\quad A-3,\quad A-6,\quad A-9
$$


with valuations $5,1,1,2$, totaling $9$. The other cases follow from the same exact trailing factors.

Thus


$$
\boxed{
R\bmod27
\text{ is encoded by at most ten actual shifted coefficients.}
}
\tag{11.4}
$$



The coefficients of $B_3$ are not evaluated here. Their exact producer definition is supplied by (5.3), (6.3), and (6.4), with the scalar $\eta_n$ retained.

This is a concrete reduction of the next producer obligation, not a claim that a small-degree jet by itself makes the next residual digit nonzero.

---

## 12. The next residual must still use the whole force

Let $\widehat Z^{\,c}$ denote the exact core-corrected residual columns. The force entering the next calculation is


$$
(\Phi_R)_{ij}
=
\mathcal M(R\widehat z_i^{\,c}\widehat z_j^{\,c}).
\tag{12.1}
$$



The new jet (11.2) with $p=3$ may be substituted in this expression modulo $27$, because $\mathcal M$ is integral at the retained finite cutoff. But the corrected columns must still be known at the corresponding precision.

In particular, the next whole residual calculation must retain


$$
\mathscr R_{\rm act}
\equiv
G_c(Z,Z)
-9V\widehat E^{-1}V^T
+3^8\mathcal K_{\rm LOW}
+3^6\Phi_R
\pmod{3^9},
\tag{12.2}
$$


with the complete LOW cross term $\mathcal K_{\rm LOW}$ as defined in turn 4.

At precision $27$, the force evaluation still includes the top pole, the next pole, and all four admissible units at the following layer:


$$
\begin{aligned}
\mathcal M(F)\equiv{}&
[y^{r_*}]\frac{F-F(-1)}{y+1}
+
3[y^{r_1}]\frac{F-F(-1)}{y+1}\\
&+
9\sum_{c\in\{1,5,7,11\}}
c^{-1}
[y^{(cH/3-1)/2}]
\frac{F-F(-1)}{y+1}
\pmod{27}.
\end{aligned}
\tag{12.3}
$$


The factorial term is absent from this *evaluation modulo $27$* only by its established valuation; it remains in the exact definition (1.3).

On a wholly vanishing depth-seven branch, division by $3^8$ must occur **after summing the entire numerator** of (12.2). Carries cannot be split off and discarded.

### Concrete follow-on lemma

The immediate next target can now be stated more sharply:

> **Terminal-jet radical-force lemma.**  
> Evaluate the actual polynomial $B_3$ in (11.2)–(11.3), together with the complete corrected-column force (12.1), and determine the next actual Schur operator on $\ker\mathcal C_7$, retaining the LOW cross terms, all force poles, and the transported endpoint.

Only at most ten producer-jet coefficients are needed for $R\bmod27$. However, obtaining them uniformly still requires additional control of the finite unit-matrix solution and its exact scalar response. A bounded jet does not automatically imply a bounded-state computation in $n$.

---

## 13. Literature and source-claim audit

The derivation uses classical ingredients:

- the Gamma integral and exponential generating function for derangements;
- finite Hankel Gram matrices;
- factorial normalization;
- Pascal factorization and Lucas’s theorem;
- an exact rank-one modification.

Those general methods are not claimed as new.

The assignment’s focused references do not, in the supplied material, state a theorem with the exact hypotheses needed for the even-subsequence, rank-one-subtracted producer strip. I therefore do not attribute the strip theorem to them or import an ordinary derangement Hankel determinant formula.

The specialized application proved here is:

1. the exact recurrence (2.7) for the shifted **even-subsequence** normalized moments;
2. the finite-order unit theorem (3.2);
3. the retained signed denominator (4.3)–(4.6);
4. the terminal unit pivot (7.1);
5. the actual factorial-tail localization (7.3);
6. the actual strip identity (9.2).

The source qualification in A4 turn 26 remains correct: arbitrary-depth producer approximation was not previously established. This report does not restore that unsupported assertion. It instead proves the weaker strip statement that the depth-seven application actually needs.

---

# Part V. Primitive normalization and global status

## 14. The full gcd and whole evaluated error are unchanged

Restore the primitive polynomial multiplier


$$
Q_n=\lambda Q_n^{\rm loc},
\qquad
Q_n^{\rm loc}=3P_n,
\qquad
\lambda\in\mathbb Z_3^\times.
$$


The complete rational matrix is


$$
R_{\rm rat}=\frac{4\lambda}{3^h}G_{\rm act},
$$


and


$$
H_{\rm complete}
=
R_{\rm rat}+(e+\pi)Q_n(-1)vv^T.
$$



Without assuming nonsingularity of $G_{\rm act}$, retain


$$
\beta_0=\det R_{\rm rat},
\qquad
\beta_1=Q_n(-1)v^T\operatorname{adj}(R_{\rm rat})v.
$$


Where $G_{\rm act}$ is nonsingular,


$$
\frac{\beta_1}{\beta_0}
=
\frac{3^hQ_n^{\rm loc}(-1)}4
v^TG_{\rm act}^{-1}v.
\tag{14.1}
$$



The new producer-strip theorem does not evaluate that whole inverse contraction. In particular, singularity of the actual depth-seven digit does not by itself specify its depth.

For a clearing integer $\ell$, retain


$$
A_\ell=\ell^k\beta_0,\qquad
B_\ell=\ell^k\beta_1,
\qquad
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


When $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The exact whole evaluated error remains


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
\det H_{\rm complete}.
}
\tag{14.2}
$$



Nothing proved here determines the all-prime gcd, proves $B_\ell\ne0$, or establishes nonzero whole primitive errors tending to zero along the same original indices.

The nonvanishing of the **producer** endpoint $P_n(-1)$ proved above must not be confused with nonvanishing of $\beta_1$ or of the complete determinant error.

---

## 15. Bounded exact arithmetic for personal inspection

No new computation is needed for the mathematical proof of the producer-strip theorem. The following is an optional bounded certificate for its new producer arithmetic, not a request to rerun the residue-block corroboration.

### Inputs

For each $2\le n\le32$:

1. Generate $D_m$ exactly for $0\le m\le4n-2$.
2. Generate $\Lambda_r$ for $0\le r\le2n-1$, independently by:
   - the finite factorial sum (2.4);
   - the recurrence (2.6).
3. Construct the actual $C_n,f_n,P_n$.
4. Construct $\mathsf T_n,F,u,\eta_n$.
5. For $n\equiv2\pmod3$, construct the complete force $\tau$, and the vectors and scalars in (6.3).

### Expected verifiable output

The certificate should report:

1. exact agreement of the two constructions of every $\Lambda_r$;
2. integrality of $\gamma_r$ and the residue pattern (2.8);
3. $\det\mathsf T_n\not\equiv0\pmod3$, with the exact residue (3.3);
4. the determinant-content identity (4.4);
5. the inverse identity (4.6);
6. for $n\equiv2\pmod3$,
   

$$
(\mathsf T_n^{-1}u)_{n-1}\equiv2\pmod3;
$$


7. exact coefficientwise agreement between the actual
   

$$
3P_n-Q_c
$$


   and formula (6.4), including
   

$$
(3P_n-Q_c)(-1)=-F^2\xi_n.
$$



No original-domain order-six congruence is to be assumed for these auxiliary small values of $n$. Their role is to verify the new formulas, not to test the infinite original strip theorem.

As a hand-checkable anchor, at $n=2$,


$$
P_2=y^2-4y-117,
\qquad
3P_2-Q_c=56(y-5),
$$


while


$$
\mathsf T_2=\begin{pmatrix}1&0\\0&8\end{pmatrix},
\quad
F=1,\quad
u=(1,-2)^T,\quad
\eta_2=-\frac12,
\quad
\xi_2=336.
$$


These give the same correction and endpoint through (6.4)–(6.5). This is an auxiliary identity, not an original-family counterexample or congruence claim.

---

## 16. Closing ledger

### New results and proof status

**Proved directly from the actual even-subsequence moment representation:**

- the shifted normalized-moment recurrence;
- the finite-order unit theorem
  

$$
\mathsf T_n\in\operatorname{GL}_n(\mathbb Z_3);
$$


- the exact signed determinant and inverse formulas, retaining $\eta_n$;
- the complete normalized factorial force of $Q_c$;
- the terminal unit pivot.

**Proved using the retained order-six producer interface at its stated scope:**

- factorial saturation of the actual correction coefficients;
- the actual endpoint divisibility needed for subtraction;
- the actual producer-strip vanishing
  

$$
\mathcal F_R=0
$$


  on the full original $81\mid j,\ D<H/972$ domain;
- consequently,
  

$$
\mathscr R_{\rm act}/3^7\equiv\mathcal C_7\pmod3;
$$


- a representation of $R\bmod27$ by at most ten actual terminal shifted coefficients.

**Not proved:**

- the stronger coefficientwise congruence $3P_n-Q_c\in3^7\mathbb Z_3[y]$;
- the first nonzero actual residual operator on the depth-seven radical;
- the actual primitive-denominator depth or full gcd;
- nonzero whole primitive errors tending to zero.

### Exact remaining mathematical bottleneck

The previous producer-strip obstruction is resolved. The next local obstruction is now the **complete next actual operator on the depth-seven radical**, including its transported endpoint.

The producer input for that step has been reduced to the bounded jet $B_3$, but its actual coefficients and their interaction with the complete corrected-column force still need a uniform evaluation. On the wholly degenerate branch, the whole numerator in (12.2), including its carries, must be evaluated before division.

Globally, one still needs same-index control of the actual reduced denominator and the whole error:


$$
0<|q(e+\pi)-p|\longrightarrow0.
$$





$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


