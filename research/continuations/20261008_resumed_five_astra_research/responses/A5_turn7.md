> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A paid Bessel decomposition of the actual balanced return

## An exponential height floor, a localized sign crossover, and the remaining strict-saving obstruction

### Abstract and proof status

The original index domain is unchanged:


$$
\mathcal N=\{N_u=9^{18+32u}:u\ge0\}.
$$


Every such $N$ is odd and exceeds $2^{54}$. All conclusions below concern these same indices; no replacement subsequence is introduced.

The source-coordinate correction is valid. For $x=1-t$, the source weights are $+r!$, not $(-1)^rr!$. A short independent first-digit calculation confirms


$$
7\mid c_{N_u}\quad\Longleftrightarrow\quad u\equiv13,17\pmod{21}.
$$


Thus the assertion $c_N=4$ on the entire original family is false. No uniform assertion about higher $7$-adic depth is made.

The principal new result is a **source-specific, ALL-prime exponential lower bound for the actual primitive balanced-return height**:


$$
\boxed{
H_N^{\rm ret}>
\frac{(2R)^N}{2^{40}(2N)^9},
\qquad
R=1+\sqrt2+\sqrt{2+2\sqrt2}.
}
\tag{A}
$$


The proof uses the actual terminal pair, both affine constants, the actual signed $\alpha,\beta,\delta$, and the entire source forcing. It does not infer a height bound from unimodularity alone.

The proof also evaluates the stable/dominant mixture. If


$$
x_N=\frac{Z_{N+1}}{Z_N},
\qquad
t_N^{B}=\frac{I_{N+1}(1/2)}{I_N(1/2)},
$$


then


$$
\boxed{
x_N>t_N^{B},
\qquad
\log(x_N-t_N^{B})
=-N\log(4R^2)+O(\log N).
}
\tag{B}
$$


The actual sign crossover occurs at


$$
\boxed{
j_N^\dagger
=N+\frac{\log(4R^2)}2\frac{N}{\log N}
+O\!\left(\frac{N}{(\log N)^2}\right).
}
\tag{C}
$$



These statements identify a precise limitation of the basic Bessel/continued-fraction argument: the actual midpoint slope approaches the stable Bessel slope at an **exponential**, not a superexponential, rate. The resulting height floor is substantial but does not have the form $e^{-CN}N^{\sigma N}$ for a fixed $\sigma>0$.

One consequence is the improved, but still critical-scale, bound


$$
\boxed{
c_N<2^{50}500^N N^{N+9}
\qquad(N\in\mathcal N).
}
\tag{D}
$$


Thus $\log c_N\le N\log N+O(N)$ remains the leading-order conclusion.

Neither strict saving, primitive-error decay, nor a signed-family no-go is proved. In particular, **the rationality or irrationality of $e+\pi$ remains unresolved**.

---

## 1. Exact objects and arithmetic retained throughout

Write


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


with


$$
C_0=1,\quad C_1=2t-1,\quad C_{j+1}=(4t-2)C_j-C_{j-1}.
$$


At a fixed original index $N$, retain


$$
d=a_Nb_{N-1}-a_{N-1}b_N,\qquad
B=b_{N-1}C_N-b_NC_{N-1}.
$$


The source functional is


$$
\eta(H)=\int_{-\infty}^{1}e^{t-1}H(t)\,dt.
$$



Set


$$
K=t(1-t)(1+t^2)^2C_{N-3}^2,\qquad
U=-\eta(K).
$$


The paid square normalization is


$$
g_B=\gcd(b_{N-1},b_N)>0,
$$




$$
\alpha=\frac{b_{N-1}}{g_B},\qquad
\beta=\frac{b_N}{g_B},\qquad
F=\alpha C_N-\beta C_{N-1},\qquad
\delta=\frac d{g_B}.
$$


These are the actual signed quantities. In particular,


$$
F(i)=F(-i)=\delta,\qquad \gcd(\alpha,\beta)=1.
$$



The source gcd is exactly


$$
V=\eta(F^2)-\delta^2,\qquad c=\gcd(U,V)>0.
\tag{1.1}
$$


Thus


$$
V_{\rm raw}=\eta(B^2)-d^2=g_B^2V.
$$


The established content theorem gives


$$
h=\operatorname{cont}(W_{\rm raw})=g_B^2c.
$$


Consequently


$$
\tau=\frac Uc,\qquad \nu=\frac Vc,\qquad
W_{\rm prim}=\tau F^2+\nu K,\qquad
M=\tau\delta^2,\qquad \gcd(\tau,\nu)=1.
\tag{1.2}
$$


At every required index,


$$
U>0,\qquad V>0,\qquad M>0.
$$



### 1.1 Complete endpoints, least aggregate clearer, and final gcd

For an integer polynomial $H$, let


$$
E(H)=\sum_{r=0}^{\deg H}(-1)^r r![t^r]H.
$$


Retain


$$
E_F=E(F^2),\qquad E_K=E(K),
$$




$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,\qquad
R_K=4\int_0^1\frac K{1+t^2}\,dt.
$$


Both quotients are obtained by complete exact monic division in $\mathbb Z[t]$.

Reduce the **single aggregate rational number**


$$
\tau R_F+\nu R_K=\frac b\lambda,
\qquad \gcd(b,\lambda)=1,\quad \lambda>0.
$$


Thus $\lambda$ is the actual least aggregate clearer. Put


$$
E=\tau E_F+\nu E_K,\qquad
A=\lambda E-b,\qquad G=\gcd(M,A).
$$


The actual primitive rational pair is


$$
\boxed{
q=\frac{\lambda M}{G},\qquad p=\frac A G.
}
\tag{1.3}
$$


No estimate below replaces this $G$ by a selected-prime gcd.

For the raw interface, with


$$
L_{\rm aff}=\operatorname{lcm}(1,\ldots,2N-1),
$$


the previously established exact identity remains


$$
(A_{\rm raw},B_{\rm raw})
=\frac{L_{\rm aff}h}{\lambda}(A,\lambda M),
$$


and hence


$$
\boxed{
\gcd(A_{\rm raw},B_{\rm raw})
=\frac{L_{\rm aff}h}{\lambda}G.
}
\tag{1.4}
$$



The physical polynomial terminal remains $2N$. The arc quotients have degree at most $2N-2$, so their integration denominators stop at $2N-1$.

### 1.2 The same whole error

The rational polynomial is


$$
P=\frac{F^2+(V/U)K}{\delta^2}.
$$


Its complete ordinary error is


$$
\epsilon_N=
\int_0^1P(t)\left(e^t+\frac4{1+t^2}\right)dt>0.
$$


The established analytic and arithmetic results, used at their stated scope $N\ge256$, are


$$
\epsilon_N\asymp R^{-2N},
\tag{1.5}
$$




$$
\boxed{q_N(e+\pi)-p_N=q_N\epsilon_N>0,}
\tag{1.6}
$$


and


$$
\boxed{
q_N\epsilon_N>
\frac{N^N}
{512\,2400^N\,c_N\sqrt{119N\log_2N}}.
}
\tag{1.7}
$$


This is a bound for the actual reduced $q_N$, after content, least clearing, and the final ALL-prime gcd.

---

## 2. Independent audit of the source correction

### 2.1 The sign is unambiguous

With $x=1-t$,


$$
\eta(H)=\int_0^\infty e^{-x}H(1-x)\,dx
       =\sum_{r\ge0}[x^r]H(1-x)\,r!.
\tag{2.1}
$$


The weights are positive.

For


$$
H=t(1-t)(1+t^2)^2,
$$


one has


$$
H(1-x)=4x-12x^2+16x^3-12x^4+5x^5-x^6,
$$


and therefore


$$
\eta(H)=4-24+96-288+600-720=-332.
\tag{2.2}
$$


Applying an additional $(-1)^r$ would instead give $-1732$, so it evaluates a different functional.

The seeds are likewise


$$
\eta(C_0)=1,\qquad
\eta(C_1)=\eta(1-2x)=-1,
$$




$$
\eta(C_2)=\eta(1-8x+8x^2)=9.
$$


The source recurrence and the turn-6 affine constant $1359872$ therefore use the corrected source, independently of the withdrawn jet tables.

### 2.2 A short first-digit verification at $7$

This audit does not repeat the full high-precision jet computations.

For $r\ge1$, the exact coefficient formula is


$$
[x^r]C_m(1-x)
=\frac{(-4)^r}{(2r)!}\,
m^2\prod_{k=1}^{r-1}(m^2-k^2).
\tag{2.3}
$$


Equivalently, it can be written using integer binomial coefficients and a power of $2$. Vandermonde’s identity shows that, for $r\le6$, these coefficients modulo $7$ have period $49$ in $m$. Terms of degree at least $7$ do not contribute to $\eta$ modulo $7$.

A direct multiplication using (2.2)–(2.3), with $m=N-3$, gives the following three affine formulas on the possible original residue classes:


$$
\begin{array}{c|c}
N\bmod7&U\bmod7\\ \hline
N=1+7\ell&2+4\ell\\
N=4+7\ell&3+2\ell\\
N=2+7\ell&3+5\ell.
\end{array}
\tag{2.4}
$$


For clarity, the small algebra behind this reduction is as follows. Write


$$
C_m(1-x)=1+d_1x+\cdots+d_5x^5+O(x^6),\qquad y=d_4.
$$


The original classes have $m^2\equiv4$ or $1\pmod7$. Positive factorial weighting gives


$$
\eta(HC_m^2)\equiv
\begin{cases}
5+4y,&m^2\equiv4,\\
4+3y,&m^2\equiv1.
\end{cases}
$$


Formula (2.3), with its exact division by $7$ paid before reduction, gives respectively


$$
y=-\ell,\qquad y=4\ell,\qquad y=3\ell
$$


in the three rows of (2.4).

Now


$$
N_u\equiv8(-3)^u\pmod{49},
$$


and $-3$ has order $21$ modulo $49$. Thus (2.4) shows


$$
7\mid U_{N_u}
\quad\Longleftrightarrow\quad
u\equiv9,13,17\pmod{21},
\tag{2.5}
$$


corresponding to


$$
N\bmod49=22,18,37.
$$



The paid Gaussian data can also be checked without a long period table. In $(\mathbb Z/49\mathbb Z)[i]$, put


$$
\lambda_*=29+15i,\qquad \lambda_*^{-1}=18-11i.
$$


Then


$$
\lambda_*+\lambda_*^{-1}=-2+4i,\qquad
\lambda_*^{24}=1+7(6+4i).
$$


Consequently, for $N=9+24k$,


$$
C_N(i)\equiv
(23+42k)+(7+35k)i\pmod{49},
$$




$$
C_{N-1}(i)\equiv
(10+7k)+(7+21k)i\pmod{49}.
\tag{2.6}
$$


Every original $N$ is $9\bmod24$. Formula (2.6) shows, in particular, that


$$
v_7(g_B)=1
$$


on the original family.

At the three zero-$U$ classes, let


$$
\widetilde B=B/7,\qquad \widetilde d=d/7.
$$


Using (2.3) through degree $6$, one obtains


$$
\begin{array}{c|c|c}
N\bmod49&\widetilde B(1-x)\pmod{7,x^7}
&\widetilde d\bmod7\\ \hline
22&3&2\\
18&1+3x+6x^2+3x^3+5x^4&0\\
37&x+x^2+6x^4+x^5+6x^6&6.
\end{array}
\tag{2.7}
$$


Positive factorial weighting gives


$$
\eta(\widetilde B^2)-\widetilde d^2
\equiv5,0,0\pmod7
\tag{2.8}
$$


in these three rows.

Since $g_B/7$ is a $7$-adic unit,


$$
V=
\frac{\eta(\widetilde B^2)-\widetilde d^2}{(g_B/7)^2}
$$


has the same first-digit vanishing. Combining (2.5) and (2.8) proves


$$
\boxed{
7\mid c_{N_u}
\quad\Longleftrightarrow\quad
u\equiv13,17\pmod{21}.
}
\tag{2.9}
$$



This independently verifies the corrected infinite first-digit conclusion. It does not infer higher uniform depths.

The supplied high-precision residues at $u=13,17$ give depth $1$ after the paid square division: $U$ has depth $1$, while $V_{\rm raw}$ has depth $3$ and $g_B^2$ has depth $2$. Those are finite certificate conclusions, not a higher-depth period theorem. No old U-unit table is used below.

---

## 3. The retained affine plane and complete integer return

Put


$$
n=2N,\qquad S_j=\eta(C_j),\qquad s_j=\frac{S_j}{j}\quad(j\ge1).
$$


The complete source recurrence is


$$
(j-1)S_{j+1}+4(j^2-1)S_j-(j+1)S_{j-1}=-2,
\qquad j\ge2,
$$


or


$$
s_{j-1}=s_{j+1}+4js_j+\frac2{j^2-1}.
\tag{3.1}
$$



No inverse of $j-1$ modulo an arbitrary prime is used. If


$$
\mathcal L_n=\operatorname{lcm}(1,\ldots,n),
$$


then


$$
\frac{2\mathcal L_n}{j^2-1}
=\frac{\mathcal L_n}{j-1}-\frac{\mathcal L_n}{j+1}\in\mathbb Z
\quad(2\le j\le n-1).
\tag{3.2}
$$


The singular indices $0,1$ are handled by the original seeds, not by extending (3.1) across them.

### 3.1 Complete affine coefficients

The accepted thirteen-weight reduction is


$$
8192U=1359872+\sum_{k=0}^{12}w_kS_{n-k},
$$


where


$$
(w_0,\ldots,w_{12})
=(1,8,58,168,399,-176,-916,-176,399,168,58,8,1).
\tag{3.3}
$$



For exact identification of the coefficients, retain


$$
(r_0,s_0^{*},e_0)=(1,0,0),\qquad
(r_1,s_1^{*},e_1)=(0,1,0),
$$


and, for $1\le k\le11$,


$$
\begin{aligned}
r_{k+1}&=r_{k-1}+4(n-k)r_k,\\
s_{k+1}^{*}&=s_{k-1}^{*}+4(n-k)s_k^{*},\\
e_{k+1}&=e_{k-1}+4(n-k)e_k+\frac2{(n-k)^2-1}.
\end{aligned}
\tag{3.4}
$$


Define


$$
\mathsf A=\sum_{k=0}^{12}w_k(n-k)r_k,\qquad
\mathsf B=\sum_{k=0}^{12}w_k(n-k)s_k^{*},
$$




$$
\mathsf E=1359872+\sum_{k=0}^{12}w_k(n-k)e_k.
$$


Then


$$
8192U=\mathsf A s_n+\mathsf B s_{n-1}+\mathsf E.
\tag{3.5}
$$


The polynomial


$$
Q_{\rm loc}(n)=\prod_{r=0}^{12}(n-r)
$$


clears every local denominator in (3.4)–(3.5).

The second actual direction is


$$
2V=\mathsf P s_n+\mathsf Q s_{n-1}+\mathsf T,
\tag{3.6}
$$


where


$$
\mathsf P=n\alpha^2+(n-2)\beta^2,
$$




$$
\mathsf Q=4(n-1)(n-2)\beta^2-2(n-1)\alpha\beta,
$$




$$
\mathsf T=(\alpha+\beta)^2-2\delta^2+\frac{2\beta^2}{n}.
\tag{3.7}
$$


In particular, neither $\mathsf E$ nor the term $-2\delta^2$ in $\mathsf T$ is omitted.

Let


$$
\Delta=\mathsf A\mathsf Q-\mathsf B\mathsf P.
$$


The established strict determinant theorem applies for $N\ge256$:


$$
\Delta<0.
\tag{3.8}
$$


Its hypotheses hold because $(\alpha,\beta)\ne(0,0)$.

We reuse that theorem and its fixed-length coefficient bounds; no determinant calculation is repeated. Write


$$
\mathcal H_n=2^{22}(5n)^{13}.
$$


Then


$$
|\mathsf A|,\ |\mathsf B|,\ |\mathsf E|\le\mathcal H_n.
\tag{3.9}
$$


A quantitative consequence of the already proved slope gap is, with


$$
\mathfrak a=\alpha^2+\beta^2,
$$




$$
\boxed{
\mathfrak a\le|\Delta|
\le6\mathcal H_n n^2\mathfrak a.
}
\tag{3.10}
$$


For the lower bound, the turn-6 inequalities give


$$
|\Delta|
\ge
\mathsf A\mathfrak a\,
\frac{3n-7}{4n(4n-7)}
\ge\frac{\mathsf A}{8n}\mathfrak a,
$$


and the established lower bound for $\mathsf A$ makes $\mathsf A/(8n)>1$ on this scope. The upper bound follows directly from


$$
\mathsf P\le n\mathfrak a,\qquad
|\mathsf Q|\le5n^2\mathfrak a.
$$



### 3.2 Integer terminal and complete forced return

The actual terminal integers are


$$
Z_n=8192\mathsf Q\,U-2\mathsf B\,V,
$$




$$
Z_{n-1}=2\mathsf A\,V-8192\mathsf P\,U.
\tag{3.11}
$$


Thus $c\mid Z_n,Z_{n-1}$.

Retain


$$
\rho_n=\mathsf Q\mathsf E-\mathsf B\mathsf T,\qquad
\rho_{n-1}=\mathsf A\mathsf T-\mathsf P\mathsf E.
$$


Backward propagation is


$$
Z_{j-1}=Z_{j+1}+4jZ_j,
\tag{3.12}
$$




$$
\rho_{j-1}
=\rho_{j+1}+4j\rho_j-\frac{2\Delta}{j^2-1}.
\tag{3.13}
$$


Exactly,


$$
Z_j=\Delta s_j+\rho_j.
\tag{3.14}
$$


Thus the source forcing is canceled by the explicitly retained opposite forcing; it has not been silently removed.

Integer unimodular propagation gives


$$
\gcd(Z_N,Z_{N+1})=c\,e_N,\qquad
e_N\mid2^{14}|\Delta|.
\tag{3.15}
$$


The adjacent pair is nonzero. Define its actual primitive height


$$
H_N^{\rm ret}
=\frac{\max(|Z_N|,|Z_{N+1}|)}
       {\gcd(Z_N,Z_{N+1})}.
\tag{3.16}
$$


The auxiliary factor $e_N$ is distinct from $g_B$, the polynomial content, and the final output gcd $G_N$.

---

## 4. Classical Bessel functions and an exact source remainder

Use the notation


$$
\mathbf I_j=I_j(1/2),\qquad \mathbf K_j=K_j(1/2).
$$


The classical recurrence, with the convention specified in the assignment, says that


$$
\mathbf I_j,\qquad (-1)^j\mathbf K_j
$$


solve


$$
Y_{j-1}-Y_{j+1}=4jY_j.
$$


This classical fact is reused, not claimed as a new observation.

The following elementary bounds will pay the decomposition quantitatively.

### 4.1 Bounds and normalization

The series


$$
\mathbf I_j
=4^{-j}\sum_{r=0}^\infty
\frac{16^{-r}}{r!(j+r)!}
$$


gives


$$
\frac{4^{-j}}{j!}
\le\mathbf I_j
\le\frac{16}{15}\frac{4^{-j}}{j!}.
\tag{4.1}
$$


For $j\ge2$, the integral representation


$$
\mathbf K_j
=\frac{4^j}{2}
\int_0^\infty t^{j-1}e^{-t-1/(16t)}\,dt
$$


and $1-y\le e^{-y}\le1$ imply


$$
\frac{15}{16}\frac{4^j}{2}(j-1)!
\le\mathbf K_j
\le\frac{4^j}{2}(j-1)!.
\tag{4.2}
$$


The sharper lower factor is $1-1/(16(j-1))$.

The adjacent Wronskian is


$$
\boxed{
\mathbf I_{j-1}\mathbf K_j
+\mathbf I_j\mathbf K_{j-1}=2.
}
\tag{4.3}
$$


For completeness, the recurrences make the left side independent of $j$. The leading terms in (4.1)–(4.2), with their relative errors tending to zero, show that its limit is $2$.

### 4.2 Exact source decomposition

The source moment has the representation


$$
S_j=\frac{e^{-1/2}}2
\int_{-\infty}^{1}e^{y/2}T_j(y)\,dy.
$$


Split this integral at $y=-1$, and on the lower interval put $y=-\cosh v$. Integration by parts gives


$$
\boxed{
s_j=e^{-1/2}(-1)^j\mathbf K_j+u_j,
}
\tag{4.4}
$$


where


$$
u_j=
\frac{(-1)^je^{-1}+L_j}{j}
-(-1)^je^{-1/2}
\int_0^\infty e^{-\cosh v/2-jv}\,dv,
\tag{4.5}
$$


and


$$
L_j=\frac{e^{-1/2}}2
\int_{-1}^{1}e^{y/2}T_j(y)\,dy.
$$


This is an exact identity, including the compact interval and the lower boundary term.

Since $|T_j(y)|\le1$ on $[-1,1]$,


$$
|L_j|\le1-e^{-1}.
$$


Also


$$
\int_0^\infty e^{-\cosh v/2-jv}\,dv
\le\frac{e^{-1/2}}j.
$$


Therefore


$$
\boxed{|u_j|<\frac2j.}
\tag{4.6}
$$



The remainder $u_j$ satisfies the complete inhomogeneous source recurrence because the Bessel part is homogeneous. Equation (4.4) is not a rational removal of the forcing.

---

## 5. The actual stable and dominant coefficients

Because $n=2N$ is even, the exact homogeneous representation of the integer return is


$$
\boxed{
Z_j=\mathcal C_N\mathbf I_j
+\mathcal D_N(-1)^j\mathbf K_j.
}
\tag{5.1}
$$


From (4.3),


$$
\mathcal D_N
=\frac{\mathbf I_{n-1}Z_n-\mathbf I_nZ_{n-1}}2,
$$




$$
\mathcal C_N
=\frac{\mathbf K_{n-1}Z_n+\mathbf K_nZ_{n-1}}2.
\tag{5.2}
$$


These real coefficients vary with $N$. No fixed-coefficient irrationality estimate is being assumed.

### 5.1 A phase-independent payment for $\delta^2/\mathfrak a$

The determinant identity


$$
d=-2-4\sum_{j=1}^{N-1}|C_j(i)|^2
$$


and the exterior Chebyshev formula give


$$
|d|\ge(1-R^{-2})^2R^{2N-2}.
$$


Also $|C_j(i)|\le R^j$. Hence


$$
\frac{\delta^2}{\mathfrak a}
=\frac{d^2}{b_{N-1}^2+b_N^2}
\ge\frac{R^{2N}}{2048}.
$$


Cauchy–Schwarz gives the reverse bound


$$
\frac{\delta^2}{\mathfrak a}
\le a_N^2+a_{N-1}^2
\le2R^{2N}.
$$


Thus


$$
\boxed{
\frac{R^n}{2048}
\le\frac{\delta^2}{\mathfrak a}
\le2R^n.
}
\tag{5.3}
$$


This estimate uses the actual paid coefficients and is independent of their phase or of the size of $g_B$.

### 5.2 The dominant coefficient

Substituting (3.14) and (4.4) into (5.2) yields


$$
\mathcal D_N=e^{-1/2}\Delta+
\frac{
\mathbf I_{n-1}(\Delta u_n+\rho_n)
-\mathbf I_n(\Delta u_{n-1}+\rho_{n-1})
}{2}.
\tag{5.4}
$$


The entire terminal return is present.

From (3.7), (3.9), (3.10), and (4.6),


$$
\max_{j=n-1,n}|\Delta u_j+\rho_j|
\le40\mathcal H_n n^2(\mathfrak a+\delta^2).
\tag{5.5}
$$


Using (4.1) and (5.3), the error in (5.4), divided by $|\Delta|$, is at most


$$
960\mathcal H_n n^2
\frac{(5/4)^n}{(n-1)!}.
\tag{5.6}
$$


It is less than $1/4$ for $n\ge2^{20}$.

Thus, throughout the original domain,


$$
\boxed{
\mathcal D_N<0,\qquad
\frac{\mathfrak a}{4}
\le|\mathcal D_N|
\le12\mathcal H_n n^2\mathfrak a.
}
\tag{5.7}
$$



### 5.3 The stable coefficient: the affine $-2\delta^2$ term is decisive

Define


$$
W_K=\mathsf A\mathbf K_n-\mathsf B\mathbf K_{n-1}.
$$


Homogeneous backward propagation in the fixed twelve-step evaluator gives


$$
W_K=\sum_{k=0}^{12}w_k(n-k)(-1)^k\mathbf K_{n-k}.
\tag{5.8}
$$


This expression is now evaluated by a signed bound. Since


$$
\frac{\mathbf K_{n-k}}{\mathbf K_n}
\le[4(n-12)]^{-k},
$$


and $|w_k|\le916$,


$$
\left|W_K-n\mathbf K_n\right|
\le
n\mathbf K_n\,
\frac{916}{4(n-12)-1}
<\frac12n\mathbf K_n
\quad(n\ge512).
$$


Therefore


$$
\boxed{
\frac12n\mathbf K_n<W_K<\frac32n\mathbf K_n.
}
\tag{5.9}
$$



Also put


$$
W_F=\mathsf P\mathbf K_n-\mathsf Q\mathbf K_{n-1}.
$$


Exact substitution in (5.2) gives


$$
\mathcal C_N
=\frac12\left[
\Delta(\mathbf K_{n-1}u_n+\mathbf K_nu_{n-1})
-\mathsf E W_F+\mathsf T W_K
\right].
\tag{5.10}
$$


Using the complete value


$$
\mathsf T=-2\delta^2+
\left((\alpha+\beta)^2+\frac{2\beta^2}{n}\right),
$$


we obtain


$$
\mathcal C_N=-\delta^2W_K+\mathcal R_N,
$$


with


$$
|\mathcal R_N|
\le40\mathcal H_n n^2\mathfrak a\,\mathbf K_n.
\tag{5.11}
$$


By (5.3), this is at most


$$
\frac14\delta^2 n\mathbf K_n
$$


on the original domain. Hence


$$
\boxed{
\mathcal C_N<0,\qquad
\frac14\delta^2n\mathbf K_n
\le|\mathcal C_N|
\le2\delta^2n\mathbf K_n.
}
\tag{5.12}
$$



This is the essential source-specific step. The large stable coefficient is produced by the **actual affine constant $-2\delta^2$**, while $\mathsf E$, the remaining terms of $\mathsf T$, and the entire source remainder are quantitatively paid. Omitting those constants would analyze a different terminal pair.

All polynomial-versus-exponential payments above follow, for example, from


$$
2^{80}n^{20}\le2^{n/2}\qquad(n\ge2^{20}),
\tag{5.13}
$$


together with $4<R<5$ and $(n-1)!\ge(n/4)^{n-1}$. No original-index normalization computation is required.

---

## 6. Evaluated midpoint mixture and size

Define, for this fixed return,


$$
\theta_j=
\frac{|\mathcal D_N|}{|\mathcal C_N|}
\frac{\mathbf K_j}{\mathbf I_j}>0.
\tag{6.1}
$$


Let


$$
\mathfrak B_N=\binom{2N}{N}.
$$


Equations (4.1)–(4.2) imply


$$
\frac1{\mathfrak B_N}
\le
\frac{\mathbf K_N}{\mathbf K_{2N}\mathbf I_N}
\le
\frac3{\mathfrak B_N}.
\tag{6.2}
$$


Combining (5.3), (5.7), and (5.12) therefore gives


$$
\boxed{
\frac1{16nR^n\mathfrak B_N}
\le\theta_N
\le
\frac{2^{19}\mathcal H_n n}{R^n\mathfrak B_N}.
}
\tag{6.3}
$$


Since


$$
\frac{4^N}{2N+1}\le\mathfrak B_N\le4^N,
$$


we have the uniform evaluation


$$
\boxed{
\log\theta_N=-N\log(4R^2)+O(\log N).
}
\tag{6.4}
$$


In particular, $\theta_N<1/4$ throughout the original domain.

Because the original $N$ is odd and both coefficients in (5.1) are negative,


$$
Z_N=-|\mathcal C_N|\mathbf I_N(1-\theta_N)<0,
$$




$$
Z_{N+1}
=-|\mathcal C_N|\mathbf I_{N+1}
-|\mathcal D_N|\mathbf K_{N+1}<0.
\tag{6.5}
$$


Thus this sign conclusion concerns the actual return, not an arbitrary homogeneous solution.

Equations (4.1), (4.2), and (5.12) also give


$$
\boxed{
\frac1{16}\delta^2\,4^N\frac{(2N)!}{N!}
<
|Z_N|
<
2\delta^2\,4^N\frac{(2N)!}{N!}.
}
\tag{6.6}
$$



### 6.1 Exact distance from the stable slope

Put


$$
x_N=\frac{Z_{N+1}}{Z_N},\qquad
t_N^B=\frac{\mathbf I_{N+1}}{\mathbf I_N}.
$$


The Wronskian identity gives


$$
x_N-t_N^B
=
\frac{2\theta_N}
{\mathbf I_N\mathbf K_N(1-\theta_N)}.
\tag{6.7}
$$


Since


$$
\frac{15}{32N}
\le\mathbf I_N\mathbf K_N
\le\frac8{15N},
$$


we obtain


$$
\boxed{
3N\theta_N<x_N-t_N^B<6N\theta_N.
}
\tag{6.8}
$$


In particular,


$$
0<t_N^B<x_N<1
$$


on the required domain, and


$$
\boxed{
\log(x_N-t_N^B)
=-N\log(4R^2)+O(\log N).
}
\tag{6.9}
$$



The lower bound in (6.8) matters. One cannot replace the actual return by the stable solution with a superexponentially small error: the actual dominant contamination is larger than that.

---

## 7. A new arithmetic lemma: the exponential return-height floor

The stable ratio has the classical continued fraction


$$
\boxed{
t_N^B=
[0;4(N+1),4(N+2),4(N+3),\ldots].
}
\tag{7.1}
$$


Indeed,


$$
\mathbf I_j=4(j+1)\mathbf I_{j+1}+\mathbf I_{j+2},
$$


and all ratios are positive. The tails tend to zero, giving (7.1). This uses the explicit continued fraction, not an imported generic Bessel irrationality measure.

Let its convergent denominators be $q_m^{(N)}$. Then


$$
q_m^{(N)}\ge[4(N+1)]^m.
\tag{7.2}
$$



### Lemma 7.1 — Uniform rational separation at the relevant heights

If a reduced rational $a/b$ has


$$
1\le b\le 2\cdot5000^N N^N,
\qquad N\ge2^{20},
$$


then


$$
\left|\frac ab-t_N^B\right|
>\frac1{16Nb^2}.
\tag{7.3}
$$



#### Proof

If $a/b$ is not a convergent and its error is below $1/(2b^2)$, Legendre’s criterion gives a contradiction. Thus the asserted weaker bound holds for nonconvergents.

For a convergent of index $m$, (7.2) and the height hypothesis give $m\le2N$. Its next partial quotient is therefore at most


$$
4(N+m+1)\le12N+4.
$$


The standard convergent lower bound is


$$
\left|\frac ab-t_N^B\right|
>\frac1{(a_{m+1}+2)b^2}
>\frac1{16Nb^2}.
$$


All parameters in this estimate vary explicitly with $N$. ∎

### Theorem 7.2 — Actual source-specific return-height floor

For every original index,


$$
\boxed{
H_N^{\rm ret}>
\frac{(2R)^N}{2^{40}(2N)^9}.
}
\tag{7.4}
$$



#### Proof

Because $0<x_N<1$, the denominator of $x_N$ in lowest terms is exactly


$$
H_N^{\rm ret}=\frac{|Z_N|}{\gcd(Z_N,Z_{N+1})}.
$$


Moreover, $|d|\le R^{2N-1}$, so $\delta^2\le R^{4N}$. Equation (6.6) yields


$$
H_N^{\rm ret}\le |Z_N|
<2(8R^4)^N N^N
<2\cdot5000^N N^N.
$$


Lemma 7.1 therefore applies to this actual reduced rational.

From (6.3) and (6.8),


$$
x_N-t_N^B
<
\frac{2^{21}\mathcal H_n n^2}
{R^n\mathfrak B_N}.
$$


Together with (7.3), this gives


$$
(H_N^{\rm ret})^2
>
\frac{R^n\mathfrak B_N}
{2^{24}\mathcal H_n n^3}.
$$


Hence


$$
H_N^{\rm ret}
>
\frac{R^N\sqrt{\mathfrak B_N}}
{2^{12}\sqrt{\mathcal H_n}\,n^{3/2}}.
$$


Now


$$
\mathfrak B_N\ge\frac{4^N}{n+1},
\qquad
\mathcal H_n<2^{53}n^{13}.
$$


Using these inequalities and $n=2N$ gives the stated bound. ∎

This is an ALL-prime arithmetic statement: the denominator of $x_N$ is reduced by its full gcd, not by a restricted set of primes.

### Corollary 7.3 — Improved critical-scale source-gcd bound

At every original index,


$$
c_N
<
2^{41}(2N)^9\delta_N^2
\left(\frac2R\right)^N
\frac{(2N)!}{N!}.
\tag{7.5}
$$


In particular,


$$
\boxed{
c_N<2^{50}500^N N^{N+9}.
}
\tag{7.6}
$$



#### Proof

From (3.15)–(3.16),


$$
c_N\le
\frac{\max(|Z_N|,|Z_{N+1}|)}{H_N^{\rm ret}}.
$$


Here the maximum is $|Z_N|$, since $0<x_N<1$. Combine (6.6) and (7.4) to obtain (7.5).

Finally use


$$
\delta^2\le R^{4N},\qquad
\frac{(2N)!}{N!}\le(2N)^N,\qquad
4R^3<500.
$$


No prime divisor has been excluded. ∎

---

## 8. Why this does not cross the strict-saving threshold

The new height theorem gives


$$
\log H_N^{\rm ret}\ge N\log(2R)-O(\log N).
$$


For RRE one needs


$$
\log H_N^{\rm ret}\ge \sigma N\log N-O(N)
$$


with a fixed $\sigma>0$. The former does not imply the latter.

The obstruction is now source-specific and quantified:

* the actual stable coefficient is of size
  

$$
|\mathcal C_N|\asymp \delta^2 n\mathbf K_n;
$$


* the actual dominant coefficient lies between polynomial multiples of
  $\alpha^2+\beta^2$;
* their actual midpoint contamination has logarithm
  

$$
-N\log(4R^2)+O(\log N).
$$



Thus the midpoint provides only an exponentially accurate rational approximation to the stable Bessel ratio. The explicit continued fraction turns that accuracy into an exponential denominator floor. It does not force a denominator of size $N^{\sigma N}$.

### 8.1 Localization of the actual crossover

The recurrence and positivity give


$$
16j(j+1)
<
\frac{\theta_{j+1}}{\theta_j}
<
(4j+1)(4j+5).
\tag{8.1}
$$


Let $j_N^\dagger$ be the least $j\ge N$ with $\theta_j\ge1$. Equation (6.4) and (8.1) show first that


$$
j_N^\dagger-N=O(N/\log N).
$$


For $k=O(N/\log N)$,


$$
\log\frac{\theta_{N+k}}{\theta_N}
=
2k\log(4N)+O(k^2/N+k/N).
$$


At the first crossing, $\log\theta_{j_N^\dagger}=O(\log N)$. Therefore


$$
\boxed{
j_N^\dagger
=N+\frac{\log(4R^2)}2\frac{N}{\log N}
+O\!\left(\frac{N}{(\log N)^2}\right).
}
\tag{8.2}
$$


In particular, this crossover is inside the retained finite range $N<j<2N$ for every sufficiently large original index.

For odd $j$,


$$
Z_j=|\mathcal C_N|\mathbf I_j(\theta_j-1);
$$


for even $j$, $Z_j<0$. Thus (8.2) locates the actual sign transition. It does not exclude an unusually short primitive integer pair near that transition.

That is the remaining arithmetic issue. Transport over $O(N/\log N)$ steps has only exponential height cost. Consequently, a very short primitive pair near the actual crossover is compatible with all the archimedean estimates proved here. It is not known to occur for this source, but the paid Bessel bounds do not rule it out.

A generic statement that a Bessel ratio is irrational would add nothing decisive: irrationality excludes exact equality with a rational, whereas the required result is a much stronger, source-specific lower bound on the reduced denominator of the actual rational return.

---

## 9. A concrete alternative follow-on obligation

The new proved arithmetic lemma is Theorem 7.2; it is an evaluated bound, not a renaming of RRE. The remaining strict-saving obligation may still be attacked directly through RRE.

There is also a different, explicitly coupled arithmetic target that could retire the producer without first proving strict saving for $c$ alone.

Let


$$
D=\operatorname{lcm}\bigl(\operatorname{den}(R_F),
                         \operatorname{den}(R_K)\bigr),
$$


where each complete column is reduced before its denominator is taken, and set


$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K).
$$


These are the complete retained integers, not truncated endpoints. The exact relation to the least aggregate clearer is


$$
\tau X+\nu Y=\frac D\lambda A,
$$




$$
\gcd(D\tau\delta^2,\tau X+\nu Y)=\frac D\lambda G.
\tag{9.1}
$$


Thus $D$ is not substituted for $\lambda$.

The established surviving-divisor theorem gives


$$
\frac{\tau}{\gcd(\tau,Y)}\mid q.
$$


Prime by prime,


$$
c\,\gcd(U/c,Y)=\gcd(U,VY).
$$


Consequently


$$
\boxed{
\frac{U}{\gcd(U,VY)}\mid q.
}
\tag{9.2}
$$



This exact identity is a useful reformulation, not a new quantitative estimate. It motivates the following genuinely different open estimate.

> **Joint source–endpoint cancellation lemma.**  
> Prove that there exist fixed $\delta_0>0$ and $C$ such that, for every sufficiently large original index,
> 

$$
> \boxed{
> \gcd(U_N,V_NY_N)
> \le e^{CN}U_N^{\,1-\delta_0}.
> }
> \tag{9.3}
>
$$



All inputs in (9.3) are actual complete source and endpoint columns. It allows the source gcd $c$ to be critical-sized, provided the remaining cancellation against the pure-$e$ column cannot simultaneously saturate its own critical bound.

Since


$$
\log U_N=2N\log N+O(N),
$$


(9.2)–(9.3) would imply


$$
q_N\ge e^{-CN}U_N^{\delta_0},
$$


and hence, using the same positive whole error $\epsilon_N\asymp R^{-2N}$,


$$
q_N\epsilon_N\longrightarrow\infty
\qquad(N\in\mathcal N).
$$


This implication is rigorous. Estimate (9.3) is open.

It is not claimed that the Bessel calculation proves (9.3), or that an unevaluated gcd expression closes it. Its purpose is to isolate the simultaneous source-content/final-cancellation regime which the separate critical estimates still permit.

---

## 10. Complete retained column evaluators

The following formulas are included to fix the complete finite objects used above. They are reused established evaluations, not recomputed normalizations.

Let


$$
\mathcal E_j=E(C_j).
$$


The source and endpoint recurrences are


$$
(j-1)S_{j+1}+4(j^2-1)S_j-(j+1)S_{j-1}=-2,
$$




$$
(j-1)\mathcal E_{j+1}
+4(j^2-1)\mathcal E_j
-(j+1)\mathcal E_{j-1}=2(-1)^j,
$$


for $j\ge2$, with


$$
(S_0,S_1,S_2)=(1,-1,9),\qquad
(\mathcal E_0,\mathcal E_1,\mathcal E_2)=(1,-3,25).
$$



For either complete functional $\mathcal L=\eta$ or $E$,


$$
\begin{aligned}
\mathcal L(F^2)
={}&\frac{\alpha^2+\beta^2}{2}
+\frac{\alpha^2}{2}\mathcal L(C_{2N})
+\frac{\beta^2}{2}\mathcal L(C_{2N-2})\\
&-\alpha\beta\{\mathcal L(C_{2N-1})+\mathcal L(C_1)\}.
\end{aligned}
\tag{10.1}
$$


With $m=N-3$ and


$$
(\gamma_0,\ldots,\gamma_6)
=(458,176,-399,-168,-58,-8,-1),
$$




$$
\mathcal L(K)=\frac1{8192}
\sum_{r=0}^6\gamma_r
\left(
2\mathcal L(C_r)+
\mathcal L(C_{2m+r})+
\mathcal L(C_{|2m-r|})
\right).
\tag{10.2}
$$


The divisions by $2$ and $8192$ are those of the exact polynomial identities.

For the complete arc return, retain


$$
R_j(t)=\frac{C_j(t)-a_j-b_jt}{1+t^2},
\qquad
\xi_j=4\int_0^1R_j,\qquad
\upsilon_j=4\int_0^1tR_j.
$$


Starting with zero values at $j=0,1$,


$$
\xi_{j+1}=4\upsilon_j-2\xi_j-\xi_{j-1}+16b_j,
$$




$$
\upsilon_{j+1}
=-4\xi_j-2\upsilon_j-\upsilon_{j-1}
+16(\ell_j-a_j),
$$


where


$$
\ell_j=
\begin{cases}
0,&j\text{ odd},\\
(1-j^2)^{-1},&j\text{ even}.
\end{cases}
$$


Thus


$$
R_F=
\frac{\alpha^2\xi_{2N}+\beta^2\xi_{2N-2}
-2\alpha\beta\xi_{2N-1}}2.
\tag{10.3}
$$


Writing $j_r=(1-4r^2)^{-1}=j_{-r}$,


$$
R_K=\frac{13}{30}
+\frac{42j_m-20(j_{m+1}+j_{m-1})
-(j_{m+2}+j_{m-2})}{128}.
\tag{10.4}
$$



The complete rational enclosure for the whole error remains


$$
J_F=
\alpha^2\frac{2N^2-1}{4N^2-1}
+\beta^2\frac{2(N-1)^2-1}{4(N-1)^2-1},
$$




$$
J_K=\frac{61}{420}
+\frac{
916j_m-399(j_{m+1}+j_{m-1})
-58(j_{m+2}+j_{m-2})
-(j_{m+3}+j_{m-3})
}{8192},
$$




$$
J_N=\frac{J_F+(V/U)J_K}{\delta^2}.
$$


Then


$$
\boxed{
3J_N<\epsilon_N<7J_N,\qquad
q_NJ_N=\frac{\lambda_N}{G_N}
(\tau_NJ_F+\nu_NJ_K).
}
\tag{10.5}
$$


Both positive summands of $P_N$ are retained.

---

## 11. What the new estimate says about the actual whole error

Substituting (7.6) into the established actual-denominator bound (1.7) yields


$$
q_N\epsilon_N>
\frac1{
2^{59}(1\,200\,000)^N
N^9\sqrt{119N\log_2N}
}.
\tag{11.1}
$$


This is positive but tends to zero. It proves neither decay nor divergence of the actual whole error.

The necessary critical regime for a successful producer therefore remains


$$
\log c_N=N\log N+O(N).
$$


The new theorem improves the exponential-scale constants and gives a source-specific primitive-height floor, but it does not remove that regime.

In particular:

* ordinary error decay $\epsilon_N\asymp R^{-2N}$ remains proved;
* the actual reduced denominator remains $q_N=\lambda_NM_N/G_N$;
* the decisive ratio $q_N/R^{2N}$ remains unresolved;
* large source content alone would not prove success;
* failure of this producer, if eventually proved, would not by itself decide the rationality of $e+\pi$.

---

## 12. Bounded exact arithmetic for an independent audit

No new full normalization, determinant expansion, or high-precision prime-jet calculation is needed for the new theorem. The coordinator’s separate twelve-step polynomial certificate need not be repeated.

An optional bounded certificate for the new size payments has the following inputs:


$$
n_0=2^{20},\qquad
\mathcal H_n<2^{53}n^{13},
\qquad 4<R<5.
$$


It need only verify the base power inequalities used in Section 5. Their expected exact outputs can be recorded as positive exponent gaps:


$$
\frac{n_0}{2}-80-20\log_2n_0
=523808>0,
$$




$$
2n_0-72-14\log_2n_0
=2096800>0,
$$




$$
2n_0-63-16\log_2n_0
=2096769>0.
$$


Together with the displayed monotonicity argument and $5/n_0<1/4$, these certify the stated polynomial-versus-exponential bounds. The inputs are fixed small descriptions; no gigantic original source polynomial is an input.

Such a finite certificate verifies only those base inequalities. Their extension to all $n\ge n_0$ comes from the proved monotonicity, not from finite extrapolation. It would not prove RRE, the joint cancellation lemma, or primitive-error decay.

---

## 13. Final conclusions

### New proved statements

For the unchanged original family:

1. The corrected source functional has positive $x$-moment weights, and the short first-digit audit proves
   

$$
7\mid c_{N_u}
   \iff u\equiv13,17\pmod{21}.
$$



2. The actual homogeneous return has a fully paid decomposition
   

$$
Z_j=\mathcal C_N I_j(1/2)
   +\mathcal D_N(-1)^jK_j(1/2),
$$


   with both coefficients negative and with the bounds in (5.7), (5.12).

3. The actual midpoint slope satisfies
   

$$
\log\!\left(
   \frac{Z_{N+1}}{Z_N}
   -\frac{I_{N+1}(1/2)}{I_N(1/2)}
   \right)
   =-N\log(4R^2)+O(\log N).
$$



4. The actual primitive return height satisfies
   

$$
\boxed{
   H_N^{\rm ret}>
   \frac{(2R)^N}{2^{40}(2N)^9}.
   }
$$



5. The ALL-prime source gcd satisfies
   

$$
\boxed{
   c_N<2^{50}500^N N^{N+9}.
   }
$$



### Exact remaining bottleneck

The Bessel approximation supplies only an exponential primitive-height floor. A strict saving requires a new arithmetic exclusion of unusually short primitive returns near the actual crossover, or an alternative estimate preventing simultaneous critical source-content and endpoint cancellation, such as (9.3).

Neither exclusion has been proved.

The least aggregate $\lambda_N$, the final ALL-prime $G_N$, the actual primitive $q_N$, and the nonzero whole error have all remained in force at the same infinite original indices.

**The new result is an unconditional source-specific exponential return-height theorem and an evaluated crossover obstruction—not a strict-saving theorem, not a signed-family no-go, and not a proof of rationality or irrationality of $e+\pi$.**
