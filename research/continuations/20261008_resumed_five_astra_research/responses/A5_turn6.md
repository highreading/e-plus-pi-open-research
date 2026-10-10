> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A uniform critical-scale bound for the actual Chebyshev source gcd

## Abstract and proof status

The original index domain is retained:


$$
\mathcal N=\{N_u=9^{18+32u}:u\in\mathbb Z_{\ge0}\}.
$$


No subsequence is substituted.

This report proves a new uniform, **ALL-prime** estimate for the actual source gcd after the paid $g_B^2$ division:


$$
\boxed{\log c_N\le N\log N+O(N).}
$$


More explicitly, the proof below gives


$$
\boxed{c_N<2^{15N}N^{N+15}\qquad(N\ge256).}
\tag{A}
$$



The estimate is obtained from:

1. an explicit reduction of the two selected source directions to the forced second-order source plane;
2. an evaluated, strictly nonzero quadratic determinant for those actual directions;
3. an integer Bézout return whose gcd is preserved by unimodular backward propagation;
4. a midpoint estimate that retains the entire inhomogeneous return.

This improves the immediate factorial-scale upper bound, whose logarithmic leading term is $2N\log N$, to the **critical leading term $N\log N$**. It does **not** give the strict saving


$$
\log c_N\le(1-\sigma)N\log N+O(N),\qquad \sigma>0,
$$


requested for a no-go theorem. Consequently:

- the signed producer is not proved successful or unsuccessful;
- the actual $q_N/R^{2N}$ remains unresolved;
- no conclusion about the rationality or irrationality of $e+\pi$ follows.

A precise next obligation is formulated below as a source-specific **short rational-return exclusion**. Its inputs are explicit lower source moments and a fully specified forced return, rather than an unevaluated high-degree source gcd.

---

## 1. Original objects and the normalization that remains in force

### 1.1 The paid source gcd

Write


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


and retain


$$
d=a_Nb_{N-1}-a_{N-1}b_N,\qquad
B=b_{N-1}C_N-b_NC_{N-1}.
$$


The source functional is


$$
\eta(H)=\int_{-\infty}^1e^{t-1}H(t)\,dt
       =\sum_{k=0}^{\deg H}(-1)^kH^{(k)}(1).
$$



Set


$$
K=t(1-t)(1+t^2)^2C_{N-3}^2,\qquad
U=-\eta(K),\qquad I=\eta(B^2).
$$


For the primitive square column, use


$$
g_B=\gcd(b_{N-1},b_N)>0,
$$




$$
\alpha=\frac{b_{N-1}}{g_B},\qquad
\beta=\frac{b_N}{g_B},\qquad
F=\frac B{g_B}=\alpha C_N-\beta C_{N-1},\qquad
\delta=\frac d{g_B}.
$$


Thus


$$
F(i)=F(-i)=\delta,\qquad \gcd(\alpha,\beta)=1.
$$



The scalar gcd studied here is exactly


$$
\boxed{
V=\eta(F^2)-\delta^2,\qquad c=\gcd(U,V).
}
\tag{1.1}
$$


In the coordinator’s raw notation,


$$
\boxed{V_{\rm raw}=I-d^2=g_B^2V.}
\tag{1.2}
$$


No assertion about $\gcd(U,V_{\rm raw})$ is substituted for an assertion about $c$.

The established endpoint-content theorem is reused, not reproved:


$$
h=\operatorname{cont}(W_{\rm raw})=g_B^2c.
$$


Consequently, with


$$
\tau=U/c,\qquad \nu=V/c,
$$


the actual primitive polynomial and target are


$$
W_{\rm prim}=\tau F^2+\nu K,\qquad
M=\tau\delta^2,\qquad \gcd(\tau,\nu)=1.
\tag{1.3}
$$


The previously proved positivity statements apply for every $N\ge256$, hence at every original index:


$$
U>0,\qquad V>0,\qquad M>0.
$$



### 1.2 Complete columns, least aggregate clearer, and final gcd

For an integer polynomial $H$, retain its complete factorial endpoint


$$
E(H)=\sum_{j=0}^{\deg H}(-1)^jj![t^j]H.
$$


Define


$$
E_F=E(F^2),\qquad E_K=E(K),
$$




$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,\qquad
R_K=4\int_0^1\frac K{1+t^2}\,dt.
$$


Both quotients are integer polynomials obtained by exact monic division.

The complete aggregate arc is reduced as one rational number:


$$
\tau R_F+\nu R_K=\frac b\lambda,\qquad
\gcd(b,\lambda)=1,\quad \lambda>0.
$$


Here $\lambda$ is the **least aggregate** clearer, not an entrywise lcm. Retain


$$
E=\tau E_F+\nu E_K,\qquad
A=\lambda E-b,\qquad
G=\gcd(M,A).
$$


Then the actual primitive pair is


$$
\boxed{
q=\frac{\lambda M}{G},\qquad p=\frac A G.
}
\tag{1.4}
$$



For comparison with the raw interface, let


$$
L_{\rm aff}=\operatorname{lcm}(1,\ldots,2N-1),
$$


and use the coordinator’s complete raw integers


$$
X_{\rm raw}=L_{\rm aff}
 \left(E(B^2)-4\int_0^1\frac{B^2-d^2}{1+t^2}\,dt\right),
$$




$$
Y_{\rm raw}=L_{\rm aff}(E_K-R_K).
$$


Then


$$
A_{\rm raw}=UX_{\rm raw}+V_{\rm raw}Y_{\rm raw},\qquad
B_{\rm raw}=L_{\rm aff}Ud^2,
$$


and the exact identity remains


$$
(A_{\rm raw},B_{\rm raw})
=\frac{L_{\rm aff}h}{\lambda}(A,\lambda M).
$$


In particular,


$$
\boxed{
\gcd(B_{\rm raw},A_{\rm raw})
=\frac{L_{\rm aff}h}{\lambda}G.
}
\tag{1.5}
$$


This accounts for the actual content, all clearing, and the final ALL-prime gcd.

The physical polynomial terminal is still $2N$. The monic arc quotients have degree at most $2N-2$, so their integration denominators stop at $2N-1$.

### 1.3 Complete forcing and returns in the retained evaluators

Let


$$
S_j=\eta(C_j),\qquad \mathcal E_j=E(C_j).
$$


The complete source and endpoint recurrences are


$$
(j-1)S_{j+1}+4(j^2-1)S_j-(j+1)S_{j-1}=-2,
\tag{1.6}
$$




$$
(j-1)\mathcal E_{j+1}
 +4(j^2-1)\mathcal E_j
 -(j+1)\mathcal E_{j-1}=2(-1)^j
\tag{1.7}
$$


for $j\ge2$, with


$$
(S_0,S_1,S_2)=(1,-1,9),\qquad
(\mathcal E_0,\mathcal E_1,\mathcal E_2)=(1,-3,25).
$$


The forcing terms are indispensable.

For either $\mathcal L=\eta$ or $\mathcal L=E$,


$$
\begin{aligned}
\mathcal L(F^2)
={}&\frac{\alpha^2+\beta^2}{2}
+\frac{\alpha^2}{2}\mathcal L(C_{2N})
+\frac{\beta^2}{2}\mathcal L(C_{2N-2})\\
&-\alpha\beta\{\mathcal L(C_{2N-1})+\mathcal L(C_1)\}.
\end{aligned}
\tag{1.8}
$$


Also, with $m=N-3$ and


$$
(\gamma_0,\ldots,\gamma_6)
=(458,176,-399,-168,-58,-8,-1),
$$




$$
\mathcal L(K)=\frac1{8192}\sum_{r=0}^6\gamma_r
\left(
2\mathcal L(C_r)+
\mathcal L(C_{2m+r})+
\mathcal L(C_{|2m-r|})
\right).
\tag{1.9}
$$


The divisions by $2$ and $8192$ in these formulas come from exact polynomial identities.

For completeness, the complete arc return is retained through


$$
R_j(t)=\frac{C_j(t)-a_j-b_jt}{1+t^2},
\quad
\xi_j=4\int_0^1R_j,\quad
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
R_F=\frac{\alpha^2\xi_{2N}+\beta^2\xi_{2N-2}
                    -2\alpha\beta\xi_{2N-1}}2.
\tag{1.10}
$$


Writing $j_r=(1-4r^2)^{-1}=j_{-r}$, the other complete arc is


$$
R_K=\frac{13}{30}
+\frac{42j_m-20(j_{m+1}+j_{m-1})
-(j_{m+2}+j_{m-2})}{128}.
\tag{1.11}
$$



No forcing, return, or terminal correction is removed by the source-gcd argument below.

### 1.4 The same nonzero whole error

The rational polynomial is


$$
P=\frac{F^2+(V/U)K}{\delta^2}.
$$


At all original indices,


$$
\epsilon_N=
\int_0^1P(t)\left(e^t+\frac4{1+t^2}\right)dt>0,
$$


and the closed analytic estimate is


$$
\epsilon_N\asymp R^{-2N},\qquad
R=1+\sqrt2+\sqrt{2+2\sqrt2}.
\tag{1.12}
$$


The exact normalized relation is


$$
\boxed{q_N(e+\pi)-p_N=q_N\epsilon_N>0.}
\tag{1.13}
$$



The complete rational enclosure is also retained. Namely,


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


and


$$
J_N=\frac{J_F+(V/U)J_K}{\delta^2}.
$$


Then


$$
3J_N<\epsilon_N<7J_N,\qquad
q_NJ_N=\frac{\lambda_N}{G_N}(\tau_NJ_F+\nu_NJ_K).
\tag{1.14}
$$


Both positive summands of $P$ are included.

The closed pure-$e$-column argument and effective Euler estimate give the actual-denominator lower bound


$$
\boxed{
q_N\epsilon_N>
\frac{N^N}
 {512\,2400^N\,c_N\sqrt{119N\log_2N}}.
}
\tag{1.15}
$$


That result is reused at its established scope; its proof and the endpoint-content proof are not repeated.

---

## 2. What the finite evidence does—and does not—show

The new scalar-square receipts give


$$
c_{18}=28,\quad c_{22}=1924,\quad c_{61}=596,\quad
c_{65}=116,\quad c_{67}=28.
$$


Thus a claim $c_N=4$ for every auxiliary integer $N\ge3$ is false. In particular,


$$
c_{61}=4\cdot149,\qquad 149>2\cdot61,
$$


so source-content primes cannot generally be restricted to primes at most the physical polynomial degree.

These are finite auxiliary counterexamples. None of those indices belongs to $\mathcal N$, so they do not disprove an original-domain-only assertion $c_N=4$. Conversely, the 24 original-index modular certificates do not prove that assertion.

There is also a short exact counterexample to the inference from consecutive-source primitivity to selected-output primitivity. The actual source values


$$
(S_1,S_2,S_3)=(-1,9,-113)
$$


give


$$
2S_1+S_2=7,\qquad -S_1+S_3=-112.
$$


The two coefficient rows


$$
(2,1,0),\qquad(-1,0,1)
$$


are primitive and their $2\times2$ minors have gcd $1$, but the selected outputs have gcd $7$.

Accordingly, neither the three-consecutive-source gcd theorem nor coefficient-lattice saturation supplies the missing bound. The argument below uses a different mechanism: **a nondegenerate affine source plane followed by an exact integer midpoint return**.

No further small-prime table is requested.

---

## 3. A fully specified two-dimensional source evaluator

Put


$$
n=2N.
$$


Throughout the new proof $N\ge256$, hence $n\ge512$.

### 3.1 Normalize the second-order recurrence, with every division paid

For $j\ge1$, define


$$
\mathscr S_j=\frac{S_j}{j}.
$$


Equation (1.6) becomes, for $j\ge2$,


$$
\mathscr S_{j+1}+4j\mathscr S_j-\mathscr S_{j-1}
=-\frac2{j^2-1}
=\frac1{j+1}-\frac1{j-1}.
\tag{3.1}
$$


Equivalently,


$$
\mathscr S_{j-1}
=\mathscr S_{j+1}+4j\mathscr S_j+\frac2{j^2-1}.
\tag{3.2}
$$



This is an equality over $\mathbb Q$, not a license to invert $j-1$ modulo an arbitrary prime.

Indeed, let


$$
\mathcal L_n=\operatorname{lcm}(1,\ldots,n).
$$


Then $\mathcal L_n\mathscr S_j$ is an integer for $1\le j\le n$, and


$$
\frac{2\mathcal L_n}{j^2-1}
=\frac{\mathcal L_n}{j-1}-\frac{\mathcal L_n}{j+1}\in\mathbb Z
\qquad(2\le j\le n-1).
\tag{3.3}
$$


Thus one explicitly known integer pays all divisions in the normalized recurrence. Later integrality will also follow directly from an integer terminal pair and unimodular propagation.

### 3.2 The exact thirteen-weight form of $U$

Equation (1.9), with $\eta(t(1-t)(1+t^2)^2)=-332$, gives


$$
8192U=1359872+\sum_{k=0}^{12}w_kS_{n-k},
\tag{3.4}
$$


where


$$
\boxed{
(w_0,\ldots,w_{12})
=(1,8,58,168,399,-176,-916,-176,399,168,58,8,1).
}
\tag{3.5}
$$


The constant is


$$
1359872=8192\cdot166.
$$


It is part of the evaluator and will not be discarded.

Define a fixed twelve-step backward evaluator:


$$
(r_0,s_0,e_0)=(1,0,0),\qquad
(r_1,s_1,e_1)=(0,1,0),
$$


and, for $1\le k\le11$,


$$
\begin{aligned}
r_{k+1}&=r_{k-1}+4(n-k)r_k,\\
s_{k+1}&=s_{k-1}+4(n-k)s_k,\\
e_{k+1}&=e_{k-1}+4(n-k)e_k+\frac2{(n-k)^2-1}.
\end{aligned}
\tag{3.6}
$$


Then exact backward substitution in (3.2) gives


$$
\mathscr S_{n-k}
=r_k\mathscr S_n+s_k\mathscr S_{n-1}+e_k
\qquad(0\le k\le12).
\tag{3.7}
$$



Set


$$
\mathsf A=\sum_{k=0}^{12}w_k(n-k)r_k,\qquad
\mathsf B=\sum_{k=0}^{12}w_k(n-k)s_k,
$$




$$
\mathsf E=1359872+\sum_{k=0}^{12}w_k(n-k)e_k.
\tag{3.8}
$$


These are fixed-length evaluators, independent of the size of $N$. They give


$$
\boxed{
8192U=\mathsf A\mathscr S_n+\mathsf B\mathscr S_{n-1}+\mathsf E.
}
\tag{3.9}
$$



Here $\mathsf A,\mathsf B\in\mathbb Z[n]$, with degrees at most $11,12$, respectively. The rational function $\mathsf E$ has all its divisions explicitly recorded in (3.6). For example, the polynomial


$$
Q_{\rm loc}(n)=\prod_{r=0}^{12}(n-r)
\tag{3.10}
$$


clears every denominator in (3.6)–(3.8).

### 3.3 The actual primitive-square direction

From (1.8), using $S_1=-1$,


$$
2V=
\alpha^2S_n+\beta^2S_{n-2}
-2\alpha\beta S_{n-1}
+(\alpha+\beta)^2-2\delta^2.
\tag{3.11}
$$


Using (3.2) once, at $j=n-1$, gives


$$
\boxed{
2V=\mathsf P\mathscr S_n+\mathsf Q\mathscr S_{n-1}+\mathsf T,
}
\tag{3.12}
$$


where


$$
\mathsf P=n\alpha^2+(n-2)\beta^2,
\tag{3.13}
$$




$$
\mathsf Q=4(n-1)(n-2)\beta^2-2(n-1)\alpha\beta,
\tag{3.14}
$$




$$
\mathsf T=(\alpha+\beta)^2-2\delta^2+\frac{2\beta^2}{n}.
\tag{3.15}
$$



This is the primitive-square direction: the paid quantities $\alpha,\beta,\delta$, not $b_{N-1},b_N,d$, occur in it.

Equations (3.9) and (3.12) are the selected affine source plane that will be used. Both constant columns, $\mathsf E$ and $\mathsf T$, remain present.

---

## 4. Uniform nondegeneracy of the actual selected directions

Define


$$
\Delta=\mathsf A\mathsf Q-\mathsf B\mathsf P.
\tag{4.1}
$$



The next result is the required evaluation of this determinant. In particular, it does not merely assume that the selected rows are generically independent.

### Theorem 4.1 — Strict transversality

For every $N\ge256$, and for every real pair $(\alpha,\beta)\ne(0,0)$,


$$
\boxed{\Delta<0.}
\tag{4.2}
$$


Thus the determinant is nonzero for the actual primitive Chebyshev coefficients.

#### Proof

Put


$$
s=\frac1{4n-7},\qquad r_*=4(n-1)+s,\qquad h=4(n-12).
$$


Since $n\ge512$,


$$
h\ge2n.
$$



First, $r_2=1$, and $r_k>0$ for $k\ge2$. From (3.6),


$$
r_{k+1}\ge h r_k\qquad(2\le k\le11).
$$


Only $w_5,w_6,w_7$ are negative, and their absolute values sum to $1268$. Therefore


$$
\mathsf A
\ge
\left((n-12)-\frac{1268n}{h^5}\right)r_{12}>0,
\tag{4.3}
$$


because $1268n/h^5<1$.

Now define


$$
f_k=s_k-r_*r_k.
$$


The initial values, obtained directly from (3.6), are


$$
f_0=-r_*,\qquad f_1=1,\qquad f_2=-s,\qquad
f_3=s,\qquad f_4=(4n-13)s.
$$


For $k\ge3$, the positive part then grows by at least the factor $h$:


$$
f_{12}\ge h^{12-k}f_k\quad(3\le k\le12),
\qquad
f_{12}\ge h^9s>128n^8.
\tag{4.4}
$$


Consequently,


$$
\begin{aligned}
\mathsf B-r_*\mathsf A
&=\sum_{k=0}^{12}w_k(n-k)f_k\\
&\ge (n-13)f_{12}-nr_*-58(n-2)s\\
&>0.
\end{aligned}
\tag{4.5}
$$


For the last inequality, $nr_*<4n^2$, $58(n-2)s<20$, while the first term is larger than $(n-13)128n^8$.

Hence


$$
\boxed{\frac{\mathsf B}{\mathsf A}>4(n-1)+\frac1{4n-7}.}
\tag{4.6}
$$



On the other hand, $\mathsf P>0$, and completing a square gives


$$
\begin{aligned}
\mathsf Q-4(n-1)\mathsf P
&=-4n(n-1)\alpha^2-2(n-1)\alpha\beta\\
&=-4n(n-1)\left(\alpha+\frac{\beta}{4n}\right)^2
+\frac{n-1}{4n}\beta^2\\
&\le \frac{n-1}{4n(n-2)}\mathsf P.
\end{aligned}
$$


Therefore


$$
\frac{\mathsf Q}{\mathsf P}
\le4(n-1)+\frac{n-1}{4n(n-2)}.
\tag{4.7}
$$


But


$$
\frac1{4n-7}-\frac{n-1}{4n(n-2)}
=\frac{3n-7}{4n(n-2)(4n-7)}>0.
\tag{4.8}
$$


Combining (4.6) and (4.7) proves


$$
\mathsf A\mathsf Q-\mathsf B\mathsf P<0.
$$


∎

The determinant can also be displayed as the evaluated quadratic form


$$
\boxed{
\Delta=
-\left[
n\mathsf B\,\alpha^2
+2(n-1)\mathsf A\,\alpha\beta
+(n-2)\bigl(\mathsf B-4(n-1)\mathsf A\bigr)\beta^2
\right].
}
\tag{4.9}
$$


The proof above establishes positive definiteness of the bracket at every required $n$. Its coefficients are explicit polynomials of degree at most $13$.

This excludes a genuine exceptional case in a source-plane argument. It is not inferred from finite evaluations or from a generic resultant being nonzero.

---

## 5. An integer Bézout return, including the entire forcing

Define the terminal integers


$$
Z_n=8192\mathsf Q\,U-2\mathsf B\,V,
\tag{5.1}
$$




$$
Z_{n-1}=2\mathsf A\,V-8192\mathsf P\,U.
\tag{5.2}
$$


They are integer linear combinations of the **actual** $U,V$, so


$$
c\mid Z_n,\qquad c\mid Z_{n-1}.
\tag{5.3}
$$



Equations (3.9) and (3.12) give


$$
Z_n=\Delta\mathscr S_n+\rho_n,\qquad
Z_{n-1}=\Delta\mathscr S_{n-1}+\rho_{n-1},
\tag{5.4}
$$


where the full terminal returns are


$$
\rho_n=\mathsf Q\mathsf E-\mathsf B\mathsf T,
\qquad
\rho_{n-1}=\mathsf A\mathsf T-\mathsf P\mathsf E.
\tag{5.5}
$$



Extend $Z_j$ backward by the integer homogeneous recurrence


$$
\boxed{Z_{j-1}=Z_{j+1}+4jZ_j.}
\tag{5.6}
$$


Simultaneously extend the rational return by


$$
\boxed{
\rho_{j-1}
=\rho_{j+1}+4j\rho_j-\frac{2\Delta}{j^2-1}.
}
\tag{5.7}
$$


Then (3.2) proves, by exact backward induction,


$$
\boxed{Z_j=\Delta\frac{S_j}{j}+\rho_j.}
\tag{5.8}
$$



The source forcing has not vanished without payment. It is canceled by the explicitly retained opposite forcing in (5.7).

### 5.1 Integrality at every prime

The sequence $Z_j$ is integral because (5.1)–(5.2) are integral and (5.6) uses an integer matrix. No division by $j$, $j-1$, $8192$, or $\Delta$ is performed modulo a prime.

Alternatively, $\mathcal L_n$ clears both terms on the right side of (5.8), by (3.3). Their sum is exactly the integer constructed by (5.6). This accounts for all rational source divisions.

### 5.2 Exact gcd propagation

The backward matrix


$$
\begin{pmatrix}0&1\\1&4j\end{pmatrix}
$$


has determinant $-1$. Hence


$$
\gcd(Z_j,Z_{j+1})
=\gcd(Z_{n-1},Z_n)
\tag{5.9}
$$


throughout the finite backward propagation.

The terminal transformation is


$$
\binom{Z_n}{Z_{n-1}}
=
\begin{pmatrix}
8192\mathsf Q&-2\mathsf B\\
-8192\mathsf P&2\mathsf A
\end{pmatrix}
\binom UV,
$$


whose determinant is


$$
2^{14}\Delta\ne0.
$$


Since $U>0$, the terminal pair, and therefore every adjacent propagated pair, is nonzero.

Applying the established selected-content principle to the primitive pair
$(U/c,V/c)$ gives the exact scoped conclusion


$$
\boxed{
\gcd(Z_N,Z_{N+1})=c\,e_N,\qquad
e_N\mid 2^{14}|\Delta|.
}
\tag{5.10}
$$


The auxiliary factor $e_N$ is not the polynomial content, not $g_B$, and not the final output gcd $G_N$.

In particular,


$$
\boxed{c\le\max(|Z_N|,|Z_{N+1}|).}
\tag{5.11}
$$



This is an ALL-prime statement: it does not exclude primes dividing any recurrence coefficient or any paid clearer.

---

## 6. A uniform midpoint bound

The terminal data $\Delta,\rho_n,\rho_{n-1}$ have only exponential height in $N$, apart from a fixed polynomial factor. Forward source growth and backward return growth can therefore be balanced at the midpoint.

### 6.1 Bounds for the fixed-length terminal evaluator

For $0\le k\le12$, (3.6) gives the coarse estimates


$$
|r_k|,\ |s_k|,\ |e_k|\le(5n)^{12}.
$$


Since


$$
\sum_{k=0}^{12}|w_k|=2536,
$$


the number


$$
H=2^{22}(5n)^{13}
\tag{6.1}
$$


satisfies


$$
|\mathsf A|,\ |\mathsf B|,\ |\mathsf E|\le H.
\tag{6.2}
$$



The established bounds $|C_j(i)|\le6^j$ and $|d|\le6^{2N-1}$ imply


$$
|\alpha|,|\beta|\le6^{n/2},\qquad |\delta|\le6^n.
$$


Thus


$$
H_V=16n^2\,36^n
\tag{6.3}
$$


bounds $|\mathsf P|,|\mathsf Q|,|\mathsf T|$.

Put


$$
B_*=2HH_V.
\tag{6.4}
$$


Then


$$
|\Delta|,\ |\rho_n|,\ |\rho_{n-1}|\le B_*.
\tag{6.5}
$$


Explicitly,


$$
B_*=2^{27}5^{13}n^{15}36^n.
\tag{6.6}
$$



### 6.2 Backward growth of the complete return

For $j\ge2$,


$$
\left|\frac{2\Delta}{j^2-1}\right|\le B_*.
$$


If


$$
B_j=\max(|\rho_{j+1}|,|\rho_j|,B_*),
$$


then (5.7) gives


$$
B_{j-1}\le(4j+2)B_j\le5jB_j.
$$


Starting from $B_{n-1}\le B_*$, this yields


$$
\boxed{
\max(|\rho_{N+1}|,|\rho_N|)
\le
B_*\,5^{N-1}\frac{(2N-1)!}{N!}.
}
\tag{6.7}
$$


Every forcing term in (5.7) is included in this estimate.

### 6.3 Forward source growth

Let $\|H\|_1$ denote the sum of the absolute values of the coefficients of a polynomial. The Chebyshev recurrence gives


$$
\|C_{j+1}\|_1\le6\|C_j\|_1+\|C_{j-1}\|_1,
$$


so, from the initial values,


$$
\|C_j\|_1\le7^j.
$$


Since


$$
|\eta(t^k)|={!k}\le k!,
$$


we obtain


$$
|S_j|\le7^jj!,\qquad
\left|\frac{S_j}{j}\right|\le7^j(j-1)!.
\tag{6.8}
$$


Therefore


$$
\max_{j=N,N+1}\left|\Delta\frac{S_j}{j}\right|
\le B_*\,7^{N+1}N!.
\tag{6.9}
$$



### Theorem 6.1 — Critical-scale ALL-prime source-gcd bound

For every $N\ge256$,


$$
\boxed{
c_N\le
B_*
\left(
7^{N+1}N!
+5^{N-1}\frac{(2N-1)!}{N!}
\right),
}
\tag{6.10}
$$


where $B_*$ is the explicit number in (6.6), with $n=2N$.

In particular,


$$
\boxed{c_N<2^{15N}N^{N+15}.}
\tag{6.11}
$$



#### Proof

Combine (5.8), (5.11), (6.7), and (6.9). This proves (6.10).

Next,


$$
N!\le N^N,\qquad
\frac{(2N-1)!}{N!}\le(2N)^{N-1},
$$


and hence


$$
7^{N+1}N!+
5^{N-1}\frac{(2N-1)!}{N!}
\le8(10N)^N.
$$


Using (6.6) with $n=2N$,


$$
c_N
\le2^{45}5^{13}N^{N+15}(12960)^N.
$$


Finally,


$$
5^{13}<2^{31},\qquad12960<2^{14},\qquad76<N
$$


for $N\ge256$. Thus


$$
c_N<2^{14N+76}N^{N+15}<2^{15N}N^{N+15}.
$$


∎

All hypotheses have been validated in the actual objects:

- the terminal is $n=2N$;
- the selected square direction uses $\alpha,\beta,\delta$ after division by $g_B$;
- $(\alpha,\beta)\ne(0,0)$;
- the selected determinant is nonzero by Theorem 4.1;
- the entire affine forcing is retained;
- the propagated pair is integral and nonzero;
- no prime has been omitted.

---

## 7. What this proves about the original producer

The new theorem gives, on the unchanged original domain,


$$
\boxed{\log c_N\le N\log N+O(N).}
\tag{7.1}
$$



This is a genuine reduction from the immediate bound $c_N\le U_N$, for which the factorial source estimates give


$$
\log U_N=2N\log N+O(N).
$$


However, it reaches exactly the leading exponent at which the established denominator obstruction becomes inconclusive.

Indeed, inserting (6.11) into (1.15) gives only an exponentially decaying lower bound:


$$
q_N\epsilon_N>
\frac{1}
 {512\,(2400\cdot2^{15})^N
  N^{15}\sqrt{119N\log_2N}}.
\tag{7.2}
$$


A positive lower bound tending to zero does not prove either decay or divergence of the actual whole error.

The existing necessary condition for success and the new upper bound now combine as follows.

### Corollary 7.1 — A narrower necessary growth regime

If this producer satisfies


$$
q_N\epsilon_N\longrightarrow0
\qquad(N\in\mathcal N),
$$


then necessarily


$$
\boxed{\log c_N=N\log N+O(N).}
\tag{7.3}
$$



Thus a successful primitive normalization would have to occupy the critical source-content regime. Supercritical leading growth is now excluded by a uniform theorem; subcritical leading growth would be excluded by the existing whole-error lower bound.

This still leaves a nonempty unresolved regime. In particular, large $c_N$ alone would not establish success, because $\lambda_N$, $G_N$, and the actual


$$
q_N=\frac{\lambda_N\tau_N\delta_N^2}{G_N}
$$


must still produce $q_N=o(R^{2N})$.

---

## 8. Why a simple rational removal of the forcing cannot finish the proof

A natural shortcut would be to remove the forcing in (3.1) by a fixed rational function of the index. That shortcut is impossible.

### Proposition 8.1 — The source recurrence has no rational particular solution

There is no $r(x)\in\mathbb Q(x)$ satisfying


$$
r(x+1)+4xr(x)-r(x-1)=-\frac2{x^2-1}.
\tag{8.1}
$$



#### Proof

Consider the finite set of poles of $r$, grouped by translation by integers. In any such orbit, an extreme pole of $r$ produces an uncanceled extreme pole of the left side of (8.1). Since the right side has poles only at $\pm1$, the only possible pole of $r$ is at $0$.

The poles at $\pm1$ on the right are simple, so $r$ can have only a simple pole at $0$. Thus


$$
r(x)=\frac A x+P(x)
$$


with $P\in\mathbb Q[x]$. But


$$
\frac A{x+1}+4x\frac A x-\frac A{x-1}
=4A-\frac{2A}{x^2-1}.
$$


Matching the poles forces $A=1$, after which $P$ would have to satisfy


$$
P(x+1)+4xP(x)-P(x-1)=-4.
$$


If $P\ne0$ has degree $d$, the left side has degree $d+1$, from the term $4xP(x)$. If $P=0$, it is zero. Neither case gives $-4$. ∎

Thus the affine source extension is genuine. One cannot replace the complete return by a fixed rational shift and then invoke a homogeneous gcd theorem.

Similarly, unimodularity alone cannot supply a quantitative lower bound for the primitive midpoint height: a homogeneous integer solution can be prescribed to have midpoint values $(1,0)$. Any further lower bound must use the **actual terminal source directions and returns**, not just the recurrence matrix.

---

## 9. A concrete next lemma: exclusion of short rational returns

The midpoint construction supplies an explicit arithmetic target beyond the original high-degree gcd.

Define the two integers


$$
\mathcal Z_0=
\Delta\frac{S_N}{N}+\rho_N,\qquad
\mathcal Z_1=
\Delta\frac{S_{N+1}}{N+1}+\rho_{N+1}.
\tag{9.1}
$$


Their integrality and non-simultaneous vanishing have been proved. Their inputs are:

- the fixed-length terminal evaluator (3.5)–(3.15);
- the actual $\alpha,\beta,\delta$;
- the explicitly forced return (5.5), (5.7), from $2N$ down to $N$;
- only the source moments $S_N,S_{N+1}$ at the lower end.

Define their primitive projective height by


$$
H_N^{\rm ret}
=
\frac{\max(|\mathcal Z_0|,|\mathcal Z_1|)}
     {\gcd(\mathcal Z_0,\mathcal Z_1)}.
\tag{9.2}
$$



### Follow-on lemma RRE — Short rational-return exclusion

Prove that there exist constants $\sigma>0$ and $C\ge0$ such that, for every sufficiently large original index,


$$
\boxed{
H_N^{\rm ret}\ge e^{-CN}N^{\sigma N}.
}
\tag{9.3}
$$



Equivalently, for every coprime integer pair $(a,b)\ne(0,0)$ with


$$
\max(|a|,|b|)<e^{-CN}N^{\sigma N},
$$


prove the explicit nonvanishing


$$
\boxed{
b\left(\Delta\frac{S_{N+1}}{N+1}+\rho_{N+1}\right)
-
a\left(\Delta\frac{S_N}{N}+\rho_N\right)\ne0.
}
\tag{9.4}
$$



This is a source-specific arithmetic nonvanishing problem. It is not a claim about arbitrary solutions of a recurrence.

### Why RRE would suffice

From (5.10),


$$
c_N\le\gcd(\mathcal Z_0,\mathcal Z_1)
=\frac{\max(|\mathcal Z_0|,|\mathcal Z_1|)}{H_N^{\rm ret}}.
$$


The proof of Theorem 6.1 bounds the numerator by
$2^{15N}N^{N+15}$. Therefore RRE would imply


$$
\log c_N\le(1-\sigma)N\log N+O(N),
$$


and (1.15) would give


$$
q_N\epsilon_N\longrightarrow\infty
\qquad(N\in\mathcal N).
$$



RRE is **open**. It is not presented as a proved replacement for the source-gcd problem. The substantive advance is that the complete source evaluation has now been transformed, with a proved nonzero determinant and paid integer divisions, into a balanced return of explicitly bounded size. The previously uncontrolled leading range $N\log N<\log c_N\le2N\log N+O(N)$ has been eliminated.

What is still missing is a source-specific reason why the balanced return cannot have unusually small primitive height.

---

## 10. A bounded exact-arithmetic certificate for the new algebra

No computation is needed for the proofs above. An optional independent certificate could check the new fixed-length algebra without recomputing any closed normalization or extending the 24 modular cases.

### Bounded inputs

Use the indeterminate $n$, the thirteen integers $w_k$ in (3.5), and


$$
Q_{\rm loc}(n)=\prod_{r=0}^{12}(n-r).
$$


Perform exactly the twelve-step recurrence (3.6), over $\mathbb Q(n)$, or equivalently with the forcing denominators cleared by $Q_{\rm loc}$.

The other formal inputs are $\alpha,\beta,\delta$ and the explicitly displayed quadratic expressions (3.13)–(3.15).

### Expected verifiable outputs

1. Integer coefficient arrays for
   

$$
\mathsf A(n),\quad\mathsf B(n),\quad
   Q_{\rm loc}(n)\mathsf E(n),
$$


   of degrees at most $11,12,22$, respectively.

2. The leading coefficients
   

$$
[n^{11}]\mathsf A=4^{10},\qquad
   [n^{12}]\mathsf B=4^{11}.
$$



3. The polynomially cleared constant column
   

$$
Q_{\rm loc}\mathsf T
   =Q_{\rm loc}\bigl((\alpha+\beta)^2-2\delta^2\bigr)
     +2(Q_{\rm loc}/n)\beta^2.
$$



4. Exact zero coefficient arrays for the two Bézout residuals obtained from
   

$$
8192U=\mathsf A X+\mathsf B Y+\mathsf E,\qquad
   2V=\mathsf P X+\mathsf QY+\mathsf T,
$$


   namely the identities yielding (5.4)–(5.5).

5. The exact determinant polynomial
   

$$
\Delta=
   -n\mathsf B\alpha^2
   -2(n-1)\mathsf A\alpha\beta
   -(n-2)(\mathsf B-4(n-1)\mathsf A)\beta^2.
$$



These are bounded polynomial calculations, not complete source normalization at a huge original index. Their expected output is an inspectable algebraic certificate. They would not establish RRE, a strict source-gcd saving, or primitive-error decay.

---

## 11. Final conclusions

### New proved statements

At every $N\ge256$, hence at every original index:

1. The actual selected source directions have a strictly nonzero, explicitly evaluated determinant:
   

$$
\Delta<0.
$$



2. A completely forced Bézout return produces a nonzero integer midpoint pair satisfying
   

$$
\gcd(Z_N,Z_{N+1})=c_Ne_N,\qquad
   e_N\mid2^{14}|\Delta|.
$$



3. The actual paid source gcd satisfies the uniform ALL-prime bound
   

$$
\boxed{c_N<2^{15N}N^{N+15}},
$$


   and therefore
   

$$
\boxed{\log c_N\le N\log N+O(N)}.
$$



4. A hypothetical success of this producer would now require the critical regime
   

$$
\log c_N=N\log N+O(N).
$$



### Conditional implication

A source-specific primitive-return height lower bound such as RRE would supply a positive saving in the coefficient of $N\log N$. Combined with the already proved pure-$e$-column lower bound, it would force the **actual nonzero whole errors** to diverge at the same infinite original indices.

### Auxiliary finite evidence

The supplied outliers and the 24 modular receipts retain only their stated finite scopes. No extension or repetition of those computations is used here.

### Exact remaining bottleneck

The new bound reaches, but does not cross, the critical exponent. The unresolved arithmetic is the exclusion of short primitive rational returns for the actual terminal data (3.9), (3.12), including their full forced constants.

The least aggregate $\lambda_N$, the final ALL-prime $G_N$, the actual primitive denominator


$$
q_N=\lambda_NM_N/G_N,
$$


and the positive whole error remain retained throughout. Their decisive ratio $q_N/R^{2N}$ is not yet resolved.

Accordingly, this report proves a new uniform source-content theorem, but **not a signed-family no-go and not a proof of rationality or irrationality of $e+\pi$**. The global research objective remains open.
