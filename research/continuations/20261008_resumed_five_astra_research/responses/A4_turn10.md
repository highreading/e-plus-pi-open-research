> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A fixed 55-row HIGH band gives one further actual/core matrix digit

## Abstract and audit decision

The rationality or irrationality of $e+\pi$ remains unresolved.

The proposed $p=25$ argument **does pass the matrix audit**, provided that “25-digit terminal dual” is read correctly: its **pairing residual** is divisible by $3^{25}$, while the corresponding finite-space approximation, after the paid mixed inverse, has precision $24$.

On the same sufficiently large original indices, the new conclusions are


$$
\boxed{S_{\mathrm{act}}-S_c\in3^{29}\operatorname{Mat}(\mathbb Z_3)}
\tag{A}
$$


on the **entire original middle space**, including its last column, and


$$
\boxed{
\delta S(\mathrm{one},\mathrm{one})\in3^{33}\mathbb Z_3
}
\tag{B}
$$


on all prescribed one-lift columns. Propagation through the complete finite prefix, $J$- and rank-$b$ returns gives


$$
\boxed{
T_{\mathrm{act},\mathrm{red}}-T_{c,\mathrm{red}}
\in3^7\operatorname{Mat}(\mathbb Z_3).
}
\tag{C}
$$



The essential additional calculation is the following actual finite-band statement. For the shortened representatives


$$
U_p=x^{D-72}a_p(y)R_{3^{24}}(y^{81Q}),
\qquad \deg a_p\le \nu+126,
$$


the vector $w_p=\mathcal B(W,U_p)$, reduced modulo $3$, is supported in precisely the allowed band


$$
Y_{m-54},\ldots,Y_m.
$$


Its LOW coordinates are divisible by $3$, so the **full actual inverse image** $E_{\mathrm{act}}^{-1}w_p$ is integral. The already established HIGH inverse zero region then gives


$$
\boxed{w_p^TE_{\mathrm{act}}^{-1}w_q\in3\mathbb Z_3.}
\tag{D}
$$


The old HIGH inverse isotropy theorem is background; the new work is the bounded 55-row support and its complete nonlinear propagation.

The leading actual endpoint is also background, not an open obligation:


$$
\overline{f_{\mathrm{act},\mathrm{new}}}(g_s)
=(-1)^{R_*+s}.
$$


The earlier OPEN designation for this lowest endpoint digit was redundant.

By contrast, the supplied material does **not** provide the initial bordered-column jets needed to evaluate the next actual endpoint digit


$$
f_{\mathrm{act},\mathrm{returned}}(g_s+g_{s+1})/3\pmod3.
$$


Below, this missing datum is reduced to six specified first endpoint jets, together with the appropriate unit-complement return if the common monomial-complement frame is used. No value is substituted from $g(-1)$ at higher precision. Consequently, (C) does **not** prove equality through $3^7$ after separate exact actual/core endpoint adaptations.

No growing primitive-denominator saving, actual directional inverse bound, or nonzero whole-error estimate is obtained.

---

## 1. Original objects, finite boundaries, and reused mathematics

### 1.1 The original family is unchanged

All uniform assertions concern sufficiently large indices satisfying exactly


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


and


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$


The fixed subwindow remains


$$
\frac{103}{1000}<\frac{N_0}{P_0}<\frac{104}{1000}.
$$



Retain


$$
P_0=243P=3^{h-27},\qquad N_0=243r,\qquad D=P_0+N_0,
$$




$$
P=3^{h-32},\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$




$$
4^j=243(3^{26}-1)P-243r+1.
$$


Put


$$
x=y-1,\qquad Q=27P=3^{h-29},
\qquad b=Q-N_0,\qquad R=b/2.
$$


Thus


$$
D=10Q-b,\qquad .064<\frac bQ<.073,
$$


and, with $\chi=P-R$,


$$
.0145<\frac{\chi}{P}<.136.
$$



No independent choice of $P,r,R$ replaces an original index. The accepted density result is used only to retain infinitely many original indices in this same subwindow.

For the fixed-width estimates below, it is enough to discard a finite initial segment so that


$$
D\ge216,\quad h\ge31,\quad Q-4b>69,
\tag{1.1}
$$


and, with $L=81Q$,


$$
L>4D+105,\qquad 4D+215<L,
\tag{1.2}
$$




$$
d+24<\frac{L-1}{2},\qquad m-d>108,\qquad m>D+53.
\tag{1.3}
$$


These follow from the displayed original window; for example, $Q\ge243$ already suffices for these coarse bounds. This is only removal of finitely many original indices, not a new congruence restriction or a new subwindow.

### 1.2 Actual finite spaces

The coordinates are


$$
U_s=x^s\quad(0\le s<D),
$$




$$
z_i=x^Dy^i\quad(0\le i<\nu),\qquad \nu=D/2-1,
$$




$$
Y_t=y^t\quad(d\le t\le m),\qquad d=D+\nu,
$$


and


$$
W=[U\ Y].
$$



The physical terminal is $Y_m$. It is not $z_{\nu-1}$.

The complete displayed basis $[U,z,Y]$ is integral unimodular relative to the monomial basis: it contains one monic polynomial of each degree $0,\ldots,m$. Thus coefficientwise divisibility of a polynomial of degree at most $m$ is equivalent to divisibility in this actual finite basis.

The complete functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{K_{\mathrm{phys}}}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!,
$$


with


$$
K_{\mathrm{phys}}=2n-2=2H-2D+2.
$$


Its largest denominator is


$$
2K_{\mathrm{phys}}+1=4H-4D+5<3^{h+1}.
$$


Consequently, the complete functional preserves coefficientwise $3$-adic integrality and divisibility. In particular,


$$
\mathcal M(\mathbb Z_3[y])\subseteq\mathbb Z_3.
\tag{1.4}
$$


This uses the fixed truncation and monic division by $y+1$; it is not an identification with an untruncated integral.

Write


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A,
$$




$$
G_c(f,g)=\mathcal M(Q_cfg),\qquad E_c=G_c(W,W).
$$


Here $\beta\equiv1\pmod3$. For $\deg p<\nu$, the complete-core corrected column is


$$
F[p]=x^Dp-WE_c^{-1}G_c(W,x^Dp).
\tag{1.5}
$$



All finite polynomials used below have degree at most $m$ before pairing. Hence their complete-core products have degree at most


$$
(A+2)+2m=2n-1,
$$


the original allowed complete-functional degree.

### 1.3 Complete producer and signed force

The exact producer remains


$$
Q_{\mathrm{act}}=Q_c+c\mathscr R,\qquad c=3^7.
$$


Nothing in the argument replaces its signed force by a core-only force.

Let


$$
F_{\mathrm{fac}}=(n-1)!=(A+1)!.
$$


Retain


$$
\gamma_0=1,\qquad \gamma_1=0,\qquad
\gamma_{k+1}=(4k+2)\gamma_k+4\gamma_{k-1},
$$




$$
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},
\qquad 0\le a,b<n,
$$




$$
h_{\mathrm{vec}}
=T_n^{-1}
\left(\binom{n+a}{a}\gamma_{n+a}\right)_{a=0}^{n-1},
$$




$$
u_a=\frac{F_{\mathrm{fac}}(-2)^a}{a!},
\qquad v=T_n^{-1}u,
$$




$$
b_{\mathrm{force}}=-n-66,
$$




$$
t=3nh_{\mathrm{vec}}
+(b_{\mathrm{force}}+6)e_{n-1}
+\frac{2b_{\mathrm{force}}}{n-1}e_{n-2}.
$$


The signed normalization is


$$
\xi=\frac{u^Tt}{F_{\mathrm{fac}}^2-u^Tv}.
$$


Its original ternary-unit property is a reused result. The correction coefficients and endpoint are exactly


$$
[x^a](3^7\mathscr R)
=-\frac{F_{\mathrm{fac}}}{a!}(t_a+\xi v_a),
\qquad 0\le a\le A+1,
\tag{1.6}
$$




$$
\mathscr R(-1)=-\frac{\xi F_{\mathrm{fac}}^2}{3^7}.
\tag{1.7}
$$



The accepted support theorem, including the actual $3^7$ division, is


$$
\mathscr R=(y+1)x^{A-72}q_{31}(x)\pmod{3^{31}},
\qquad \deg q_{31}\le72.
\tag{1.8}
$$


The entire reciprocal is retained:


$$
r_{31}(y)=\beta^{-1}\sum_{k=0}^{30}
\left(-\frac{3y}{\beta}\right)^k,
\qquad
(\beta+3y)r_{31}\equiv1\pmod{3^{31}}.
\tag{1.9}
$$


Set


$$
\mathcal B(f,g)=\mathcal M(\mathscr Rfg).
$$


This is the bilinear form of the **complete actual producer**.

The use of (1.8) below does not delete (1.7). It replaces the producer only modulo a stated power of $3$, and (1.4) pays the resulting complete-functional error.

### 1.4 Closed inputs reused, not recalculated

The following are used at their stated scope.

1. The actual mixed inverse bounds:
   

$$
E_c^{-1},E_{\mathrm{act}}^{-1}\in3^{-1}\operatorname{Mat}(\mathbb Z_3),
$$


   

$$
E_cE_{\mathrm{act}}^{-1},
   \ E_{\mathrm{act}}^{-1}E_c
   \in\operatorname{Mat}(\mathbb Z_3).
   \tag{1.10}
$$



2. The $p\le25$ mixed filters, finite Jacobi orthogonality, and the unit first exceptional moment.

3. The complete original middle normalization, including its last coordinate:
   

$$
G_c(F[p],F[q])\in3^{26}\mathbb Z_3
   \qquad(\deg p,\deg q<\nu).
   \tag{1.11}
$$



4. A4 Turn 8’s paid $p=26$ physical overflow argument and its resulting bounds
   

$$
\mathcal B(W,\mathcal F[a])\in3^{25}M,
   \tag{1.12}
$$


   

$$
\delta S(p,\Psi[a])\in3^{32}\mathbb Z_3
   \qquad(\deg p<\nu,\ \deg a\le R).
   \tag{1.13}
$$


   Its natural physical representative has precision $25$, not $26$. That closed obstruction and long overflow certificate are not repeated.

5. The finite prefix lift, H2, the actual $J$- and rank-$b$ unit blocks, and the initial precision-$6$ matrix comparison.

6. A1 Turn 5’s exact radical, saturated basis, and unit complement.

7. The old HIGH inverse zero region:
   

$$
(E_Y^{-1})_{ij}=0\pmod3
   \quad\text{when }i+j>m+d,
   \qquad d\le i,j\le m.
   \tag{1.14}
$$


   This is explicitly supplied by old A1 Turn 20. It is not a new theorem of this report.

---

## 2. The physical $p=25$ terminal dual

Put


$$
N=3^{24},\qquad M=(N-1)/2,\qquad L=3^{h-25}=81Q,
$$




$$
\Phi(y)=R_N(y^L).
$$


The reused filter has


$$
R_N(0)=1,\qquad \deg R_N=M,\qquad \Phi\equiv1\pmod3,
$$


so


$$
\deg\Phi=(H-L)/2.
$$



### 2.1 The exact finite-moment input

Write


$$
C_N(Y)=(Y-1)^NR_N(Y)=\sum_q c_qY^q.
$$


The accepted Jacobi orthogonality, in the normalization needed here, says


$$
3^{25}\sum_q\frac{c_q}{2(q+a)+1}=0
\qquad(0\le a<M),
\tag{2.1}
$$


and


$$
\mathfrak t_{25}
:=3^{25}\sum_q\frac{c_q}{2(q+M)+1}
\in\mathbb Z_3^\times.
\tag{2.2}
$$


This is the already known exceptional moment, not a new unevaluated functional.

Here is why the same identities apply to the present physical rows. The accepted Frobenius congruence is


$$
x^H\equiv(y^L-1)^N\pmod{3^{25}}.
\tag{2.3}
$$


For a nonsparse monomial $y^t$, if $L\nmid 2t+1$, then


$$
v_3(2t+1+2qL)=v_3(2t+1)\le h-26.
$$


Thus every physical pole weight in that monomial calculation is divisible by $3^{26}$, hence is zero modulo $3^{25}$.

If $L\mid2t+1$, write


$$
t=(L-1)/2+aL.
$$


The macro moment is then exactly the one in (2.1) or (2.2). The first exceptional exponent is


$$
n_*=(H-1)/2=m+\nu.
\tag{2.4}
$$


For all polynomials used in the terminal construction, the nonsparse degree is below $n_*+L$, so no second exceptional moment can occur.

The last denominator needed to complete the first exceptional moment is


$$
(4N-1)L=4H-L.
$$


It is physical because


$$
4H-L<4H-4D+5.
\tag{2.5}
$$


Thus the complete finite moment, rather than a virtual continuation beyond the cutoff, is being used.

The factorial contribution is in $3^h$, and the error in (2.3) remains in $3^{25}$ by (1.4).

### 2.2 The 25 terminal columns are in the actual $W$

Define


$$
\Omega_k
=y^{d+k}-\sum_{u=0}^{D-1}\binom{d+k}{u}x^u
=x^Ds_k,
$$


where


$$
s_k(y)=\sum_{\ell=0}^{\nu+k}
a_\ell^{(D)}y^{\nu+k-\ell},
\qquad
a_\ell^{(D)}=\binom{D+\ell-1}{\ell}.
\tag{2.6}
$$


Set $a_\ell^{(D)}=0$ for $\ell<0$.

For $0\le k\le24$, $\Omega_k$ is an actual LOW/HIGH combination. Every nonconstant filter term begins at degree at least $L>d+24$, and


$$
m-\deg(\Omega_k\Phi)
=\frac{L-4D+3-2k}{2}>0.
\tag{2.7}
$$


Hence


$$
\Omega_k\Phi\in W\mathbb Z_3.
\tag{2.8}
$$



For a LOW row, the nonsparse degree in


$$
x^H(\beta+3y)s_k\,w\,\Phi
$$


is at most $d+k<(L-1)/2$; no active macro exponent occurs.

For a HIGH row $w=y^{m-r}$, only the coefficient at $n_*=m+\nu$ can survive modulo $3^{25}$. From (2.6), that coefficient is


$$
\beta a_{k-r}^{(D)}+3a_{k-r+1}^{(D)}.
$$


Therefore


$$
G_c(W,\Omega_k\Phi)
\equiv
\mathfrak t_{25}
\sum_{r=0}^{k+1}
\left(\beta a_{k-r}^{(D)}
+3a_{k-r+1}^{(D)}\right)e_{Y_{m-r}}
\pmod{3^{25}}.
\tag{2.9}
$$


All rows $Y_{m-r}$, $0\le r\le25$, lie in the actual HIGH window.

### 2.3 Explicit evaluation of the geometric convolution

Put


$$
\theta=-3/\beta,
$$


and define


$$
\mathscr D_{25}
=
\frac{\Phi}{\beta\mathfrak t_{25}}
\sum_{k=0}^{24}\theta^k\Omega_k.
\tag{2.10}
$$


The only divisions here are by the certified units $\beta$ and $\mathfrak t_{25}$.

For $0\le r\le25$, the normalized coefficient in (2.9) is


$$
\begin{aligned}
\frac1\beta
\sum_{k=0}^{24}\theta^k
\left(\beta a_{k-r}^{(D)}
+3a_{k-r+1}^{(D)}\right)
&=
\sum_{k=0}^{24}\theta^k a_{k-r}^{(D)}
-\sum_{k=0}^{24}\theta^{k+1}a_{k-r+1}^{(D)}\\
&=\delta_{r0}-\theta^{25}a_{25-r}^{(D)}.
\end{aligned}
\tag{2.11}
$$


Thus the uncancelled term has valuation at least $25$, and


$$
\boxed{
G_c(W,\mathscr D_{25})-e_{Y_m}\in3^{25}M.
}
\tag{2.12}
$$



This proves the proposed 25-digit **dual residual**. Applying the mixed inverse costs one digit, so the exact terminal dual differs from $\mathscr D_{25}$ by an element of $3^{24}W$, not by an unproved element of $3^{25}W$.

### 2.4 The last-middle residue is retained

For $\deg p<\nu$, let


$$
\tau(p)=[y^{\nu-1}]p.
$$


In the raw trial


$$
x^Dp\Phi,
$$


the only possible exceptional HIGH extraction comes from the $3y$ term of $\beta+3y$, the coefficient $\tau(p)$, and the physical row $Y_m$. Hence


$$
\boxed{
G_c(W,x^Dp\Phi)
\equiv
3\mathfrak t_{25}\tau(p)e_{Y_m}
\pmod{3^{25}}.
}
\tag{2.13}
$$


In particular, for $p=y^{\nu-1}$, the exceptional residue is genuinely


$$
3\mathfrak t_{25}e_{Y_m}.
$$


It has not been suppressed by an ordinary-middle compression theorem.

Define


$$
\widetilde F[p]
=x^Dp\Phi
-3\mathfrak t_{25}\tau(p)\mathscr D_{25}
=x^D\pi_p\Phi,
$$


where


$$
\pi_p
=p-\frac{3\tau(p)}{\beta}
\sum_{k=0}^{24}\theta^ks_k,
\qquad
\deg\pi_p\le\nu+24.
\tag{2.14}
$$


Equations (2.12)–(2.13) give a residual in $3^{25}$. Moreover,


$$
\widetilde F[p]-x^Dp\in W,
\qquad
\deg\widetilde F[p]\le m.
$$


Applying the paid inverse therefore yields


$$
\boxed{
\widetilde F[p]-F[p]\in3^{24}W\mathbb Z_3
\qquad(\deg p<\nu).
}
\tag{2.15}
$$



This establishes the whole-middle $p=25$ representative with the original last-middle column and physical terminal both retained.

---

## 3. Shortened representatives in the actual $W$

We now prove, rather than assume from a degree label, the proposed bound


$$
U_p=x^{D-72}a_p\Phi,\qquad \deg a_p\le\nu+126.
$$



### 3.1 An exact monic decomposition

For the $\pi_p$ in (2.14), set


$$
H_p=x^{D-72}q_{31}r_{31}\pi_p.
$$


The complete degree-$30$ reciprocal gives


$$
\deg H_p\le d+54,
\tag{3.1}
$$


and $x^{D-72}\mid H_p$.

Remove degrees $d,\ldots,d+54$, in descending order, using the monic polynomials


$$
\Omega_0,\ldots,\Omega_{54}.
$$


Their span lies in the actual LOW/HIGH space and every $\Omega_k$ is divisible by $x^D$. After this removal, the remaining polynomial has degree below $d$ and is still divisible by $x^{D-72}$.

Perform monic division of that remainder by $x^D$. We obtain an exact decomposition


$$
H_p=B_p+x^Db_p,
\tag{3.2}
$$


where

* $\deg b_p<\nu$;
* $B_p$ lies in the span of LOW coordinates and $y^d,\ldots,y^{d+54}$;
* $x^{D-72}\mid B_p$;
* $\deg B_p\le d+54$.

The LOW remainder is divisible by $x^{D-72}$ because both the dividend and the subtracted $x^D$-multiple are. No division by a nonunit is involved.

### 3.2 Filtering preserves the actual finite boundary

For $0\le k\le54$,


$$
m-\deg(\Omega_k\Phi)
=\frac{L-4D+3-2k}{2}>0
$$


by (1.2). Nonconstant filter terms begin above the middle window. Consequently,


$$
B_p\Phi\in W\mathbb Z_3.
\tag{3.3}
$$



Using (2.14) for $b_p$,


$$
x^Db_p\Phi
=\widetilde F[b_p]
+3\mathfrak t_{25}\tau(b_p)\mathscr D_{25}.
$$


Define


$$
U_p
=B_p\Phi+3\mathfrak t_{25}\tau(b_p)\mathscr D_{25}.
\tag{3.4}
$$


Then $U_p\in W\mathbb Z_3$, and


$$
U_p
=
\left(
B_p+\frac{3\tau(b_p)}{\beta}
\sum_{k=0}^{24}\theta^k\Omega_k
\right)\Phi.
$$


Every term in parentheses is divisible by $x^{D-72}$. Therefore


$$
\boxed{
U_p=x^{D-72}a_p(y)\Phi(y),
\qquad
\deg a_p\le\nu+126.
}
\tag{3.5}
$$


Indeed,


$$
(d+54)-(D-72)=\nu+126,
$$


while the terminal-correction part has the smaller bound $\nu+96$.

### 3.3 Exact transport of the complete producer

From (1.8)–(1.9),


$$
\mathscr R\,\widetilde F[p]
\equiv Q_cH_p\Phi\pmod{3^{31}}.
\tag{3.6}
$$


This congruence retains all coefficients of $q_{31}$ and all 31 reciprocal terms.

By (3.2)–(3.4),


$$
H_p\Phi
=U_p+\widetilde F[b_p].
$$


Since $F[b_p]$ is exactly core-orthogonal to $W$, (2.15) gives


$$
G_c(W,H_p\Phi)=G_c(W,U_p)+3^{24}M.
$$


Replacing $\widetilde F[p]$ by $F[p]$ in the complete producer pairing costs $3^{24}$, again by (2.15) and integrality.

Let $u_p$ be the actual $W$-coordinate vector of $U_p$. We have proved


$$
\boxed{
\mathcal B(W,F[p])=E_cu_p+3^{24}e_p,
\qquad e_p\in M(\mathbb Z_3).
}
\tag{3.7}
$$



Thus both the proposed shortened degree and the actual $W$-membership are valid.

---

## 4. Compact norms and the fixed 55-row HIGH band

### 4.1 Compact filtered norm

Let $B_0\in\mathbb Z_3[y]$ with


$$
\deg B_0\le2D+107.
$$


Then


$$
\boxed{
\Lambda_h(x^HB_0\Phi^2)\in3^{25}\mathbb Z_3,
}
\tag{4.1}
$$


where


$$
\Lambda_h(P)=3^h\sum_{v=0}^{K_{\mathrm{phys}}}
\frac{[y^v]P}{2v+1}.
$$



To prove this, use (2.3) and set


$$
A_0(Y)=(Y-1)^NR_N(Y)^2=\sum_q a_qY^q.
$$


We have


$$
A_0(1)=0,\qquad \deg A_0\le2N-1.
$$


All macro terms are physical, since


$$
(2N-1)L+\deg B_0
\le2H-L+2D+107
\le2H-2D+2.
\tag{4.2}
$$



For $0\le s\le\deg B_0$, put $c_s=2s+1$. By (1.2),


$$
c_s\le4D+215<L=3^{h-25},
$$


so


$$
v_3(c_s)\le h-26.
$$


The denominators $c_s+2qL$ have the same valuation as $c_s$, and


$$
v_3\!\left[
3^h\left(\frac1{c_s+2qL}-\frac1{c_s}\right)
\right]\ge27.
\tag{4.3}
$$


For each fixed $s$, the macro sum is therefore zero modulo $3^{27}$, because $\sum_q a_q=0$. The Frobenius replacement costs only $3^{25}$, proving (4.1).

### 4.2 Complete pairings of the shortened representatives

For $U_p,U_q$ in (3.5), the compact factors are


$$
x^{D-144}(\beta+3y)a_pa_q
$$


for $G_c(U_p,U_q)$, and


$$
x^{D-216}q_{31}a_pa_q
$$


for $\mathcal B(U_p,U_q)$.

Their degrees are bounded by


$$
(D-144)+1+2(\nu+126)=2D+107,
$$


and


$$
(D-216)+72+2(\nu+126)=2D+106,
$$


respectively. The exponents are nonnegative by $D\ge216$. The full factorial contributions are in $3^h$, and the producer support error remains in $3^{31}$. Hence


$$
\boxed{
G_c(U_p,U_q)\in3^{25}\mathbb Z_3,
\qquad
\mathcal B(U_p,U_q)\in3^{25}\mathbb Z_3.
}
\tag{4.4}
$$



For the $\widetilde F[p]$, the producer compact factor has degree at most


$$
(D-72)+72+2(\nu+24)=2D+46.
$$


Thus its raw filtered pairing is in $3^{25}$. The linear replacement errors in (2.15) are in $3^{24}$, so


$$
\boxed{
\mathcal B(F[p],F[q])\in3^{24}\mathbb Z_3
\qquad(\deg p,\deg q<\nu).
}
\tag{4.5}
$$



### 4.3 The actual HIGH support is the last 55 rows

Set


$$
w_p=\mathcal B(W,U_p).
$$


Modulo $3$, the filter is $1$, and the complete source quotient is


$$
x^{H-144}q_{31}a_p
$$


times the actual row polynomial.

Before multiplication by a HIGH row $y^i$, its degree is at most


$$
H-144+72+(\nu+126)=H+\nu+54.
\tag{4.6}
$$


The sole unit-weight physical pole is at


$$
r_3=\frac{3H-1}{2}=H+m+\nu.
\tag{4.7}
$$


Therefore


$$
(w_p)_{Y_i}=0\pmod3
\qquad\text{if }i<m-54.
$$


Equivalently,


$$
\boxed{
\operatorname{supp}(\overline{w_p}_{\,\mathrm{HIGH}})
\subseteq\{m-54,\ldots,m\}.
}
\tag{4.8}
$$



For a LOW row of degree at most $D-1$, the corresponding degree is at most


$$
H+\nu+54+D-1=H+d+53<r_3.
$$


Hence


$$
\boxed{(w_p)_{\mathrm{LOW}}\in3M.}
\tag{4.9}
$$



The number 55 is consequently correct: it is $54+1$, with the endpoint row included.

### 4.4 The full actual inverse image is integral

The LOW rows and LOW/HIGH couplings of $E_{\mathrm{act}}$ vanish modulo $3$, while its HIGH block is the accepted unit block modulo $3$.

Choose an integral vector $z_0$, supported on HIGH coordinates, satisfying


$$
E_{\mathrm{act}}z_0\equiv w_p\pmod3.
$$


This is possible by (4.9) and the HIGH block’s nonsingularity. Then


$$
E_{\mathrm{act}}^{-1}w_p
=z_0+E_{\mathrm{act}}^{-1}(w_p-E_{\mathrm{act}}z_0).
$$


The last residual is divisible by $3$, and the global inverse costs at most $3^{-1}$. Thus


$$
\boxed{z_p:=E_{\mathrm{act}}^{-1}w_p\in M(\mathbb Z_3).}
\tag{4.10}
$$



Only after this payment may the equation be reduced modulo $3$. Its HIGH part is


$$
\overline{z_p}_{\,\mathrm{HIGH}}
=\overline{E_Y}^{-1}\overline{w_p}_{\,\mathrm{HIGH}}.
$$



### 4.5 Applying the old inverse zero region to the new band

The LOW contribution to $w_p^Tz_q$ vanishes modulo $3$. On the HIGH coordinates, every possible pair of support indices satisfies


$$
i+j\ge2(m-54)>m+d
$$


because $m-d>108$. The old theorem (1.14) therefore gives


$$
\overline{w_p}_{\,\mathrm{HIGH}}^T
\overline{E_Y}^{-1}
\overline{w_q}_{\,\mathrm{HIGH}}=0.
$$


Consequently,


$$
\boxed{
w_p^TE_{\mathrm{act}}^{-1}w_q\in3\mathbb Z_3
\qquad\text{for every original }p,q.
}
\tag{4.11}
$$



This uses the full actual inverse and pays the LOW transport. It does not identify the full inverse with a HIGH inverse.

---

## 5. Exact nonlinear payment and the one/one improvement

### 5.1 Whole-middle Schur difference

Let


$$
b_p=\mathcal B(W,F[p]).
$$


In the basis consisting of $W$ and the exactly core-corrected middle columns, the actual Gram matrix has cross block $cb_p$. Thus the exact Schur difference is


$$
\delta S(p,q)
=c\mathcal B(F[p],F[q])
-c^2b_p^TE_{\mathrm{act}}^{-1}b_q.
\tag{5.1}
$$



The exact nonlinear identity is


$$
E_cE_{\mathrm{act}}^{-1}E_c
=
E_c-c\mathcal B(W,W)
+c^2\mathcal B(W,W)E_{\mathrm{act}}^{-1}\mathcal B(W,W).
\tag{5.2}
$$


This follows by substituting $E_c=E_{\mathrm{act}}-c\mathcal B(W,W)$; it is not a truncated inverse expansion.

On $u_p,u_q$, the three terms on the right of (5.2) have valuations at least


$$
25,\qquad 7+25=32,\qquad 14+1=15,
$$


using (4.4) and (4.11). Therefore


$$
u_p^TE_cE_{\mathrm{act}}^{-1}E_cu_q\in3^{15}\mathbb Z_3.
\tag{5.3}
$$



Now insert


$$
b_p=E_cu_p+3^{24}e_p
$$


from (3.7) into (5.1). The exact payments are:

| Term | Valuation lower bound |
|---|---:|
| $c\mathcal B(F[p],F[q])$ | $7+24=31$ |
| Main $u/u$ source return | $14+15=29$ |
| Either cross error | $14+24=38$ |
| Error/error return | $14+48-1=61$ |

The cross-error estimate uses the integral products in (1.10). Thus


$$
\boxed{
S_{\mathrm{act}}-S_c\in3^{29}\operatorname{Mat}(\mathbb Z_3)
}
\tag{5.4}
$$


on the whole middle space.

The limiting term in this argument is the $c^4$-weighted nonlinear return controlled by the 55-row isotropy. No stronger uniform exponent is asserted.

### 5.2 Admissibility of the ordinary $p=25$ trial on one-lift inputs

For an amplitude $a(y)$, $\deg a\le R$, the middle input is


$$
p_a=x^b a(y)y^{k_0}(y^{3Q}+3),
\qquad k_0=\frac{3Q+1}{2}.
$$


Its largest degree is


$$
p_{\max}=\frac{9Q+3b+1}{2}.
$$


The original margin is


$$
\nu-32-p_{\max}=\frac{Q-4b-67}{2}>0.
\tag{5.5}
$$


Hence all these inputs satisfy the ordinary $p=25$ hypothesis, without a last-middle exception.

Set


$$
V[p_a]=x^Dp_a\Phi.
$$


The ordinary residual is in $3^{25}$, so


$$
V[p_a]-F[p_a]\in3^{24}W.
\tag{5.6}
$$


There is no physical overflow: the ordinary trial has a gap much larger than the reciprocal degree $30$.

### 5.3 One-sided substitution pays the extra source digit

Use only one replacement in the pairing with another one-lift column. By the reused actual mixed bound (1.12),


$$
\mathcal B(V[p_a]-F[p_a],F[p_c])\in3^{24+25}=3^{49}.
\tag{5.7}
$$


This is the crucial advantage over replacing both arguments at their bare coefficientwise precision.

Define


$$
L[p_a]=x^{D-72}q_{31}r_{31}p_a\Phi.
$$


It has degree at most $\deg V[p_a]+30<m$, and


$$
\mathscr R\,V[p_a]\equiv Q_cL[p_a]\pmod{3^{31}}.
\tag{5.8}
$$



Perform monic division


$$
x^{D-72}q_{31}r_{31}p_a=x^Dp_a'+u_a,
$$


where


$$
\deg u_a<D,\qquad
\deg p_a'\le\deg p_a+30\le\nu-2.
$$


The polynomial $u_a\Phi$ lies in the actual $W$: its constant-filter part is LOW, its other terms start above $d$, and


$$
m-\deg(u_a\Phi)\ge\frac{L-3D+3}{2}>0.
$$


Likewise, $x^Dp_a'\Phi-x^Dp_a'\in W$. Hence


$$
L[p_a]-F[p_a']\in W
$$


exactly, and core orthogonality gives


$$
G_c(L[p_a],F[p_c])=G_c(F[p_a'],F[p_c]).
\tag{5.9}
$$



Combining (5.7)–(5.9),


$$
\mathcal B(F[p_a],F[p_c])
\equiv G_c(F[p_a'],F[p_c])\pmod{3^{31}}.
$$


The original core normalization (1.11) now yields


$$
\boxed{
\mathcal B(F[p_a],F[p_c])\in3^{26}\mathbb Z_3.
}
\tag{5.10}
$$



The quadratic source term in (5.1) has valuation at least


$$
14+25+25-1=63.
$$


Therefore


$$
\boxed{
\delta S(\Psi[a],\Psi[c])\in3^{33}\mathbb Z_3.
}
\tag{5.11}
$$



For a general middle column paired with a one-lift column, the reused bound remains


$$
\boxed{\delta S(p,\Psi[a])\in3^{32}\mathbb Z_3.}
\tag{5.12}
$$



No $p=26$ trial is newly substituted here. Its already paid mixed conclusion is reused, while the new physical multiplier is a nonoverflowing $p=25$ multiplier.

---

## 6. Propagation through all finite matrix returns

Let


$$
G_0a=x^ba,\qquad \deg a\le R.
$$


The finite prefix is $0,\ldots,R_*-1$, with


$$
R_*=\frac{9Q+1}{2}.
$$


The retained tail is partitioned into


$$
K=\{0,\ldots,3R\},\qquad
J=\{3R+1,\ldots,\tau-1\},
$$


where


$$
\tau=(N_0-3)/2,\qquad R_*+\tau=\nu.
$$



### 6.1 Prefix return

The exact core-prefix lift of $G_0$ is the one-lift column plus $9Z$, with $Z$ integral. Thus (5.4), (5.11), and (5.12) give:

| Pair of core-prefix-lifted arguments | Physical perturbation precision |
|---|---:|
| General/general | $29$ |
| General/$G_0$ | $31$ |
| $G_0/G_0$ | $33$ |

For example, the last line is


$$
\min\{33,\ 2+32,\ 4+29\}=33.
$$


The general/$G_0$ line is


$$
\min\{32,\ 2+29\}=31.
$$



The physical prefix inverse costs $3^{-26}$. Its unit normalization remains valid, because the normalized whole perturbation is in $3^3M$.

In a core-prefix-orthogonal frame, the exact perturbation of the prefix Schur complement is the direct perturbation minus the quadratic perturbation through the actual prefix inverse. The quadratic physical valuations are at least


$$
29+29-26=32,
$$




$$
29+31-26=34,
$$




$$
31+31-26=36.
$$


After division by $3^{26}$, these are $6,8,10$, all deeper than the corresponding direct terms.

Using the archive normalization $\mathsf U_\alpha=-S_\alpha/3^{26}$, we obtain


$$
\boxed{\mathcal R_{\mathrm{act}}-\mathcal R_c\in3^3M,}
\tag{6.1}
$$




$$
\boxed{
(\mathcal R_{\mathrm{act}}-\mathcal R_c)_{T,K}G_0
\in3^5M,
}
\tag{6.2}
$$




$$
\boxed{
G_0^T(\mathcal R_{\mathrm{act},KK}-\mathcal R_{c,KK})G_0
\in3^7M.
}
\tag{6.3}
$$



All prefix boundaries are the original finite boundaries.

### 6.2 Complete $J$-return, including its inverse change

Retain


$$
\mathcal R_{\alpha,JJ}=3B_\alpha,\qquad
\mathcal R_{\alpha,KJ}=9L_\alpha.
$$


Equations (6.1)–(6.2) give


$$
B_{\mathrm{act}}-B_c\in3^2M,
\qquad
L_{\mathrm{act}}-L_c\in3M,
\tag{6.4}
$$


and


$$
(L_{\mathrm{act}}-L_c)^TG_0\in3^3M.
\tag{6.5}
$$


Since the accepted core terminal theorem gives $L_c^TG_0\in3M$, define


$$
C_\alpha=\frac{L_\alpha^TG_0}{3}.
$$


Then


$$
C_{\mathrm{act}}-C_c\in3^2M.
\tag{6.6}
$$


The unit inverse identity gives


$$
B_{\mathrm{act}}^{-1}-B_c^{-1}
=-B_{\mathrm{act}}^{-1}(B_{\mathrm{act}}-B_c)B_c^{-1}
\in3^2M.
\tag{6.7}
$$



The entire contracted $J$-return is


$$
27G_0^TL_\alpha B_\alpha^{-1}L_\alpha^TG_0
=3^5C_\alpha^TB_\alpha^{-1}C_\alpha.
$$


Every term of its exact actual-core difference contains either a difference in $C_\alpha$ or a difference in $B_\alpha^{-1}$, each divisible by $3^2$. Therefore


$$
\boxed{
27G_0^T
\left(
L_{\mathrm{act}}B_{\mathrm{act}}^{-1}L_{\mathrm{act}}^T
-L_cB_c^{-1}L_c^T
\right)G_0
\in3^7M.
}
\tag{6.8}
$$


Combining with (6.3),


$$
\boxed{
G_0^T(\mathcal S_{\mathrm{act}}^{(2)}
-\mathcal S_c^{(2)})G_0\in3^7M.
}
\tag{6.9}
$$



### 6.3 Mixed rank-$b$ channels

Let $E_b$ be the original monomial complement. Put


$$
D_\alpha=E_b^TL_\alpha.
$$


Then


$$
D_{\mathrm{act}}-D_c\in3M.
$$


The cross $J$-return is


$$
27D_\alpha B_\alpha^{-1}L_\alpha^TG_0
=3^4D_\alpha B_\alpha^{-1}C_\alpha.
$$


Its difference lies in $3^5M$: a change in $D_\alpha$ contributes one additional digit, while changes in $B_\alpha^{-1}$ or $C_\alpha$ contribute two. With (6.2),


$$
E_b^T(\mathcal S_{\mathrm{act}}^{(2)}
-\mathcal S_c^{(2)})G_0\in3^5M.
\tag{6.10}
$$



On the $E_b,E_b$ block, the $J$-return difference is in $3^4M$, while the prefix-returned difference is in $3^3M$. Hence


$$
E_b^T(\mathcal S_{\mathrm{act}}^{(2)}
-\mathcal S_c^{(2)})E_b\in3^3M.
\tag{6.11}
$$



Using the actual rank-$b$ normalizations


$$
9A_{b,\alpha}=E_b^T\mathcal S_\alpha^{(2)}E_b,
\qquad
27M_{b,\alpha}=E_b^T\mathcal S_\alpha^{(2)}G_0,
$$


we obtain


$$
\boxed{
A_{b,\mathrm{act}}-A_{b,c}\in3M,
\qquad
M_{b,\mathrm{act}}-M_{b,c}\in3^2M.
}
\tag{6.12}
$$


Both $A_{b,\alpha}$ are the accepted unit blocks. Thus


$$
A_{b,\mathrm{act}}^{-1}-A_{b,c}^{-1}\in3M.
\tag{6.13}
$$


The closed core result $M_{b,c}\in3M$, together with (6.12), also gives $M_{b,\mathrm{act}}\in3M$.

### 6.4 Complete rank-$b$ return

The full return is


$$
81M_{b,\alpha}^TA_{b,\alpha}^{-1}M_{b,\alpha}.
$$


A change in either $M_b$ has valuation at least


$$
4+2+1=7.
$$


A change in the inverse has valuation at least


$$
4+1+1+1=7.
$$


Therefore


$$
\boxed{
81\left(
M_{b,\mathrm{act}}^TA_{b,\mathrm{act}}^{-1}M_{b,\mathrm{act}}
-
M_{b,c}^TA_{b,c}^{-1}M_{b,c}
\right)\in3^7M.
}
\tag{6.14}
$$



Together with (6.9), this proves the primary target:


$$
\boxed{
T_{\mathrm{act},\mathrm{red}}-T_{c,\mathrm{red}}\in3^7M.
}
\tag{6.15}
$$



In the earlier producer notation, the corresponding sharpened bounds are


$$
\boxed{\Delta_{GG}\in3^3M,\qquad \Delta_{bG}\in3^2M.}
\tag{6.16}
$$



No actual inverse change or matrix return has been omitted.

### 6.5 Common unit-complement elimination

Reuse


$$
\kappa=\frac{3P-3}{2},
\qquad
\delta=\min\left\{\chi-1,\frac{P+3}{2}-3\chi\right\},
$$




$$
g_s=(1-y)^{2\chi}y^s,
\qquad
L_*=\frac{P-1}{2}\le s\le L_*+\delta-1.
$$


Let $\mathscr G$ be these coefficient columns, and let $E_{\mathcal C}$ be the explicit monomial complement from A1 Turn 5. The established results are


$$
[E_{\mathcal C}\ \mathscr G]\in\operatorname{GL}_{R+1}(\mathbb Z),
$$




$$
T_{\alpha,\mathrm{red}}/81\equiv-\mathsf H_\kappa\pmod3,
$$


with $E_{\mathcal C}^T\mathsf H_\kappa E_{\mathcal C}$ nonsingular.

In the same monomial-complement frame, the physical cross block is in $3^5M$, the complement inverse costs $3^{-4}$, and the matrix perturbation is in $3^7M$. A changed cross block contributes to the changed return at valuation at least


$$
7-4+5=8.
$$


The inverse difference has valuation at least


$$
-4+7-4=-1,
$$


so its contribution has valuation at least


$$
5-1+5=9.
$$


Thus the common-complement return difference is in $3^8M$.

It follows that the two returned radical matrices in this **common matrix frame** still differ by $3^7M$. Since each is in $3^5M$,


$$
\boxed{
D_{\mathrm{act}}^{\mathrm{common}}/3^5
\equiv D_c^{\mathrm{common}}/3^5\pmod9.
}
\tag{6.17}
$$



This compares two radical matrix digits. It does not evaluate those core digits numerically, and it does not compare separately endpoint-adapted frames.

---

## 7. The higher actual endpoint: what is known and what is missing

### 7.1 The leading endpoint is already solved

The accepted H2 endpoint formula is


$$
\overline{f_{\mathrm{act}}^{(2)}}_u
=(-1)^{R_*+u},
\qquad 0\le u\le3R.
$$


The accepted deduction on the current amplitude space is


$$
\overline{f_{\mathrm{act},\mathrm{new}}}(a)
=(-1)^{R_*}a(-1).
\tag{7.1}
$$


Therefore


$$
\boxed{
\overline{f_{\mathrm{act},\mathrm{new}}}(g_s)
=(-1)^{R_*+s}\ne0.
}
\tag{7.2}
$$



This is reused mathematics. It is not an unknown primitive-functional hypothesis.

The leading endpoint-annihilator inside the full radical is exactly


$$
(1-y)^{2\chi}y^{L_*}(y+1)
\mathbb F_3[y]_{\le\delta-2},
$$


with basis


$$
h_s=g_s+g_{s+1},
\qquad L_*\le s\le L_*+\delta-2.
\tag{7.3}
$$


When $\delta=1$, this list is empty.

### 7.2 Complete endpoint and diagonal returns remain present

The exact retained channels are


$$
f_\alpha^{(2)}
=f_{\alpha,K}-3L_\alpha B_\alpha^{-1}f_{\alpha,J},
$$




$$
\lambda_\alpha^{(2)}
=\lambda_\alpha-\frac13f_{\alpha,J}^TB_\alpha^{-1}f_{\alpha,J},
\tag{7.4}
$$


and


$$
f_{\alpha,\mathrm{new}}
=G_0^Tf_\alpha^{(2)}
-3M_{b,\alpha}^TA_{b,\alpha}^{-1}f_{\alpha,b},
$$




$$
\lambda_{\alpha,\mathrm{new}}
=\lambda_\alpha^{(2)}
-\frac19f_{\alpha,b}^TA_{b,\alpha}^{-1}f_{\alpha,b}.
\tag{7.5}
$$



The initial finite-prefix formulas remain


$$
f=e_R-\mathsf B^T\mathsf A^{-1}e_C,
$$




$$
\lambda=3^{26}d_{\mathrm{act}}-e_C^T\mathsf A^{-1}e_C.
\tag{7.6}
$$


The full forcing identity also remains


$$
J^T\varepsilon+\omega
=-\varepsilon-s_{\mathrm{ret}}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
\tag{7.7}
$$


Neither forcing term is deleted before its original normalization and returns.

The old H2 scalar theorem $v_3(\lambda^{(2)})=-1$, and any subsequent frame-specific normalization $\lambda_{\mathrm{new}}=\eta/3$, are retained only at their accepted scopes. They do not evaluate the individual $1/3$ or $1/9$ numerators.

### 7.3 A precise six-sample formula for the first higher endpoint jet

The bounds


$$
L_{\mathrm{act}}^TG_0\in3M,
\qquad
M_{b,\mathrm{act}}\in3M
$$


show from the **complete** formulas (7.4)–(7.5) that


$$
f_{\mathrm{act},\mathrm{new}}
\equiv G_0^Tf_{\mathrm{act},K}\pmod9.
\tag{7.8}
$$


Indeed, both returned endpoint corrections are divisible by $9$. They vanish at this particular modulus for a proved reason; they remain in the exact endpoint.

Define the actual first prefix-endpoint jet


$$
d_i=
\frac{(f_{\mathrm{act},K})_i-(-1)^{R_*+i}}{3}
\pmod3.
\tag{7.9}
$$


This division is legal by the accepted leading H2 formula.

For $h_s=g_s+g_{s+1}$,


$$
G_0h_s=x^{2P}y^s(1+y).
\tag{7.10}
$$


The exact sign-evaluation functional annihilates this polynomial, because of the factor $1+y$. Also


$$
x^{2P}\equiv1+y^P+y^{2P}\pmod3.
$$


Consequently,


$$
\boxed{
\frac{f_{\mathrm{act},\mathrm{new}}(h_s)}3
\equiv
\sum_{j=0}^{2}
\bigl(d_{s+jP}+d_{s+jP+1}\bigr)
\pmod3.
}
\tag{7.11}
$$


All six indices are actual $K$-indices: $h_s$ has degree at most $R$, so $G_0h_s$ has degree at most $3R$.

Formula (7.11) is a genuine additional reduction of the endpoint obligation. It is **not an evaluation of its right-hand side**, because the packet supplies the leading signs but not these first jets.

### 7.4 The latest unit complement: two frames must not be confused

#### The common monomial-complement frame

Put


$$
K_{\mathrm{act}}=T_{\mathrm{act},\mathrm{red}}/81,
$$




$$
A_{\mathcal C}=E_{\mathcal C}^TK_{\mathrm{act}}E_{\mathcal C},
\qquad
C_{\mathcal C}=E_{\mathcal C}^TK_{\mathrm{act}}\mathscr G.
$$


Then


$$
A_{\mathcal C}^{-1}\in M(\mathbb Z_3),\qquad
C_{\mathcal C}\in3M.
$$



If “returned endpoint” refers to the common monomial-complement orthogonal lift, its exact value is


$$
f_{\mathrm{common}}
=\mathscr G^Tf_{\mathrm{act},\mathrm{new}}
-C_{\mathcal C}^TA_{\mathcal C}^{-1}
f_{\mathcal C},
\qquad
f_{\mathcal C}=E_{\mathcal C}^Tf_{\mathrm{act},\mathrm{new}}.
\tag{7.12}
$$


Let $v_s$ be the radical-coordinate vector selecting $g_s+g_{s+1}$, and define


$$
\rho_s=\overline{(C_{\mathcal C}/3)v_s},
$$




$$
z_{\mathcal C}
=\overline{A_{\mathcal C}}^{-1}\overline{f_{\mathcal C}}.
$$


The leading matrix and endpoint give


$$
\overline{A_{\mathcal C}}
=-E_{\mathcal C}^T\mathsf H_\kappa E_{\mathcal C},
\qquad
(\overline{f_{\mathcal C}})_i=(-1)^{R_*+i}.
$$


Thus the complete first higher endpoint digit in this frame is


$$
\boxed{
\frac{f_{\mathrm{common}}(h_s)}3
\equiv
\sum_{j=0}^{2}
(d_{s+jP}+d_{s+jP+1})
-\rho_s^Tz_{\mathcal C}
\pmod3.
}
\tag{7.13}
$$



The division defining $\rho_s$ is paid because $h_s$ lies in the leading radical. Equivalently,


$$
\rho_s=
\frac{E_{\mathcal C}^TT_{\mathrm{act},\mathrm{red}}h_s}{3^5}
\pmod3.
\tag{7.14}
$$


The new matrix comparison proves that this cross digit agrees with the corresponding core cross digit. The supplied sources do not evaluate that cross digit.

If this unadapted complement were eliminated as a full bordered block, its diagonal return would also have to be retained:


$$
3^{-4}f_{\mathcal C}^TA_{\mathcal C}^{-1}f_{\mathcal C}.
$$


The matrix-only comparison in Section 6 does not authorize dropping this bordered return.

#### The endpoint-adapted complement that preserves the complete current diagonal

The old endpoint-adapted complement theorem is preferable for the bordered problem. Its hypotheses are now validated:

* $T_{\mathrm{act},\mathrm{red}}\in3^4M$;
* its leading radical is the complete $\mathscr G$;
* the leading complementary block is a unit;
* the actual endpoint is nonzero on every $g_s$, by (7.2).

Choose $g_0=g_{L_*}$ and


$$
v=\frac{g_0}{f_{\mathrm{act},\mathrm{new}}(g_0)}.
$$


This divides only by a certified ternary unit. Replace each complementary vector $e_i$ by


$$
e_i-vf_{\mathrm{act},\mathrm{new}}(e_i).
$$


The complement now lies inside the **exact** endpoint kernel and retains the same nondegenerate leading form.

The old theorem gives:

* physical complement inverse $3^{-4}$ times a unit inverse;
* cross block in $3^5M$;
* matrix return in $3^6M$;
* zero endpoint return from this complement;
* zero diagonal return from this complement.

Therefore this latest elimination preserves exactly


$$
\boxed{\lambda_{\mathrm{act},\mathrm{new}}}
$$


from (7.5), including its earlier $1/3$ and $1/9$ contributions. It neither erases nor evaluates their numerators.

In this endpoint-adapted-complement frame, before correcting the leading annihilators themselves, their endpoint values are unchanged by complement elimination. Their higher digit is therefore (7.11). If instead one also replaces


$$
h_s\longmapsto h_s-vf_{\mathrm{act},\mathrm{new}}(h_s),
$$


the endpoint is zero by construction—but the coefficient used in this replacement is exactly the still-uncomputed higher endpoint datum. This construction is not a computation of that datum.

### 7.5 Exact archived data needed for a numerical or uniform endpoint evaluation

The supplied excerpt (7.6) gives the form of the prefix return but does not define the initial bordered columns $e_C,e_R$ to the required higher precision, nor their exact formation from the complete original source normalization.

Since $\mathsf B_K\in3M$, the needed jet can be written more explicitly:


$$
d_K
\equiv
\frac{e_{R,K}-\varepsilon_K}{3}
-
\overline{\mathsf B_K/3}^{\,T}
\overline{\mathsf A}^{-1}\overline{e_C}
\pmod3,
\qquad
(\varepsilon_K)_i=(-1)^{R_*+i}.
\tag{7.15}
$$


Thus the exact missing defining data are:

1. the original definition of $e_C,e_R$ after the finite $W$-correction and the original $3^{26}$ normalization;
2. $e_{R,K}\pmod9$, with its complete force, terminal term, and normalization included;
3. $e_C\pmod3$, and the actual normalized prefix coupling $\mathsf B_K/3\pmod3$, in the same finite prefix frame;
4. for the common monomial-complement convention, the cross jet in (7.14), or its equivalent complete-return certificate;
5. if a different archived returned frame is intended, its exact unit change of basis.

The full identity (7.7), including both
$\theta e_{\nu-1}$ and $3^{26}b^{\langle26\rangle}$, must be carried through the definition in item 1. A term cannot be discarded merely from its displayed power before checking the intervening normalization divisions.

The leading endpoint theorem supplies none of items 2–4 by itself. In particular, it does not justify setting $d_i=0$.

There is a precise insufficiency here. In the saturated basis
$[E_{\mathcal C},\mathscr G]$, adding $3$ times a functional supported on one radical coordinate preserves every leading endpoint value and every matrix congruence, while changing a value in (7.13). This is not a modification of the actual original source; it demonstrates why the displayed leading facts alone cannot determine the omitted higher jet.

### 7.6 Why raw matrix precision $7$ does not synchronize exact adaptations

Let $D\in3^5M$ be a common-frame radical matrix, and suppose the retained endpoint $F$ has the accepted leading signs. For a unit-normalized pivot $v$, write


$$
F(h_s)=3\tau_s\pmod9.
$$


The exact adapted vector is


$$
h_s^{\mathrm{ex}}=h_s-vF(h_s).
$$


Expanding the pairing gives


$$
\begin{aligned}
D(h_s^{\mathrm{ex}},h_t^{\mathrm{ex}})
={}&D(h_s,h_t)
-F(h_s)D(v,h_t)-F(h_t)D(h_s,v)\\
&+F(h_s)F(h_t)D(v,v).
\end{aligned}
$$


The last term is in $3^7$. Therefore


$$
\boxed{
\frac{
D(h_s^{\mathrm{ex}},h_t^{\mathrm{ex}})
-D(h_s,h_t)
}{3^6}
\equiv
-\tau_s\frac{D(v,h_t)}{3^5}
-\tau_t\frac{D(h_s,v)}{3^5}
\pmod3.
}
\tag{7.16}
$$



Thus a difference of $3$ in exact endpoint lifts can alter the physical $3^6$ matrix digit. If actual and core endpoints have different first jets, equality of their common-frame matrices through $3^7$ does not remove the right-hand side of (7.16).

A sufficient synchronization condition would be equality of the relevant actual/core $\tau_s$, together with the matching pivot normalization at the required precision. Alternatively, a separately proved vanishing of all displayed leading pivot pairings could make the change harmless. Neither is supplied here.

---

## 8. The concrete next local lemma

The lowest endpoint pivot is no longer an obligation. The next useful target is the following original-object certificate.

> **Higher actual endpoint and adaptation certificate.**  
> On the same original indices:
>
> 1. derive the actual prefix jets $d_i$ in (7.9) from the complete defining data in (7.15), with all forcing and normalization terms retained;
> 2. evaluate the six-sample expression (7.11) for every allowed $s$;
> 3. if the common monomial-complement frame is used, evaluate the additional cross contraction in (7.13);
> 4. use these evaluated values in the exact adaptation formula (7.16), rather than identifying separate actual/core adapted matrices from the raw comparison alone;
> 5. evaluate the resulting actual radical matrix and direction sufficiently to prove the required Smith-direction divisibilities.

The last point is substantive. For the endpoint-annihilator system, the previously established paid unit-complement reduction gives an exact smaller system


$$
Sv_R=r.
$$


If


$$
USV=\operatorname{diag}(3^{e_i})
$$


is a Smith form, the desired bound $v_R\in3^{-1}M$ requires


$$
v_3((Ur)_i)\ge e_i-1
$$


for every nonzero Smith entry, and $(Ur)_i=0$ for every zero entry. A large radical or a fixed-depth zero does not prove this directional condition.

The retained rank-one modification


$$
B^\sharp=B+\frac{27\eta}{u}ww^T,
\qquad u=1-27\eta\alpha,
$$


also remains actual. Its paid reduction depends on an actual solution for $B$, not on a chosen normal form or raw nullity.

Even a successful fixed-depth directional certificate would still not establish an unbounded relative-cofactor saving.

---

## 9. Division and boundary ledger

| Operation | Paid result or boundary |
|---|---|
| Complete functional | Fixed $K_{\mathrm{phys}}=2n-2$; coefficientwise integral |
| Complete producer | Signed $t+\xi v$, actual $3^7$ division, width $72$ support modulo $3^{31}$ |
| Reciprocal | All terms $0,\ldots,30$ retained |
| $p=25$ terminal columns | $\Omega_0,\ldots,\Omega_{24}$, all in actual $W$ |
| Terminal macro completion | Last required denominator $4H-L<4H-4D+5$ |
| Last-middle exception | $3\mathfrak t_{25}\tau(p)e_{Y_m}$, explicitly retained |
| Terminal dual | Residual $3^{25}$, using only unit divisions |
| Mixed inverse | $3^{-1}$, yielding representative error $3^{24}$ |
| Shortening | Monic operations only; $\deg a_p\le\nu+126$ |
| Shortened physical boundary | $\Omega_0,\ldots,\Omega_{54}$ remain below $m$ after filtering |
| Compact norms | Degree at most $2D+107$; every macro term below the physical cutoff |
| New HIGH support | Last 55 actual rows modulo $3$ |
| Full actual inverse image | LOW residual in $3$, hence integral inverse image |
| HIGH isotropy | Old inverse zero region, now applied to the fixed 55-row band |
| Whole nonlinear middle difference | $3^{29}$ |
| Reused $p=26$ certificate | Physical overflow $3^{26}$, actual approximation precision $25$ |
| One-sided $p=25$ substitution | Error $3^{49}$ using the reused mixed source bound |
| One/one middle difference | $3^{33}$ |
| General/one middle difference | Reused $3^{32}$ |
| Prefix inverse | Physical cost $3^{-26}$ |
| Complete $J$-inverse change | Included; normalized inverse difference in $3^2M$ |
| Rank-$b$ inverse | Physical cost $3^{-2}$; its change included |
| Fully returned matrix difference | $T_{\mathrm{act},\mathrm{red}}-T_{c,\mathrm{red}}\in3^7M$ |
| Common final complement | Physical inverse $3^{-4}$; changed matrix return in $3^8M$ |
| Exact endpoint adaptation | Unit divisions only; higher jets still required |
| Complete diagonal | Earlier $1/3$ and $1/9$ returns retained exactly |
| Global contents and clearer | No alteration and no new global division |

---

## 10. Original contents, least clearer, all-prime gcd, and whole error

The complete-source recurrence remains


$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\qquad 0\le t\le2n-2.
$$


The archived physical resonant step


$$
t_*=\frac{3^h-5}{2}
$$


retains its genuine $3^h$ divisor. It is distinct from both the unit-pole coefficient index $r_3$ used in Section 4 and the physical basis terminal $Y_m$. The highest required complete moment remains physical because


$$
H-4D+5\ge0.
$$



All original column contents remain those of the complete original construction. The local $3$-adic unit divisions and auxiliary filtered columns do not redefine those contents or the actual least simultaneous clearer $\ell_{\mathrm{clr}}$.

Retain


$$
A_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_0,
\qquad
B_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_1,
$$


and the gcd over **all primes**


$$
\boxed{G=\gcd(|A_\ell|,|B_\ell|).}
$$


For $B_\ell\ne0$, the actual primitive denominator and numerator are


$$
q=\frac{|B_\ell|}{G},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{G}.
$$


The whole evaluated error is exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\mathrm{clr}}^{m+1}}
{G}\det H_{\mathrm{complete}}.
}
\tag{10.1}
$$



An irrationality proof still requires, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad \det H_{\mathrm{complete}}\ne0,
\tag{10.2}
$$


and


$$
\boxed{
\log G-(m+1)\log\ell_{\mathrm{clr}}
-\log|\det H_{\mathrm{complete}}|
\longrightarrow+\infty.
}
\tag{10.3}
$$


These conditions would make the nonzero whole errors in (10.1) tend to zero, which is incompatible with rationality.

The new local matrix digit establishes none of (10.2)–(10.3). A common determinant factor can occur in both distinguished cofactors and disappear in the actual primitive quotient. Fixed local precision, growing nullity, or an endpoint-adapted normal form is not a proof of a growing primitive-denominator saving.

---

## 11. Bounded exact-arithmetic receipts

No tool computation was performed. The matrix theorem above is symbolic and uniform. It needs no dense original matrix computation, no rerun of the $p=26$ overflow certificate, and no reevaluation of a closed Jacobi or terminal constant.

Two optional finite receipts can be specified precisely.

### 11.1 Small terminal-convolution receipt

**Inputs**

For one specified original tuple, use:

* the ternary unit $\beta$;
* the 26 integers
  

$$
a_j^{(D)}=\binom{D+j-1}{j},\qquad 0\le j\le25;
$$


* $\theta=-3/\beta$;
* modulus $3^{25}$.

**Expected verifiable output**

For every $0\le r\le25$,


$$
\frac1\beta\sum_{k=0}^{24}\theta^k
\left(\beta a_{k-r}^{(D)}+3a_{k-r+1}^{(D)}\right)
-\delta_{r0}
=-\theta^{25}a_{25-r}^{(D)}
\equiv0\pmod{3^{25}}.
$$


There are only $26\cdot25$ summands. This checks the newly extended finite convolution; it does not reevaluate $\mathfrak t_{25}$.

### 11.2 Sparse higher-endpoint receipt

**Inputs**

Fix one fully specified admissible original tuple and one


$$
L_*\le s\le L_*+\delta-2.
$$


Supply the six **actual** residues


$$
(f_{\mathrm{act},K})_{s+jP},
\quad
(f_{\mathrm{act},K})_{s+jP+1}
\pmod9,
\qquad j=0,1,2,
$$


already formed with the complete original prefix endpoint and force.

For the common monomial-complement frame, additionally supply:

* the contracted cross jet $\rho_s$ from (7.14);
* a vector $z_{\mathcal C}$ with a certificate
  

$$
\overline{A_{\mathcal C}}z_{\mathcal C}
  =\overline{f_{\mathcal C}}.
$$



The last certificate can be verified without a dense original matrix: for


$$
Z(y)=\sum_{i\in\mathcal C}(z_{\mathcal C})_iy^i,
$$


the required matrix-vector product is the finite coefficient extraction


$$
-\,[y^{\kappa-i}](1-y)^bZ(y),
\qquad i\in\mathcal C.
$$


Only a polynomial of degree at most $3R$ is involved.

**Expected verifiable outputs**

1. The six leading-sign checks are zero:
   

$$
(f_{\mathrm{act},K})_i-(-1)^{R_*+i}\equiv0\pmod3.
$$



2. The legal divided jets $d_i\in\mathbb F_3$ are output.

3. The endpoint-adapted-complement convention gives the residue
   

$$
\tau_s^{\mathrm{adapted\ complement}}
   =
   \sum_{j=0}^{2}(d_{s+jP}+d_{s+jP+1}).
$$



4. The common monomial-complement convention gives
   

$$
\tau_s^{\mathrm{common}}
   =
   \sum_{j=0}^{2}(d_{s+jP}+d_{s+jP+1})
   -\rho_s^Tz_{\mathcal C}.
$$



The residue $0,1,$ or $2$ is an output, not an asserted value. The packet does not contain these inputs, so this calculation has not been performed. Even a completed receipt would establish only its stated original instance. A uniform endpoint-synchronization theorem requires a uniform derivation of the input jets.

---

## 12. Conclusion and proof status

The parent’s precision-$7$ matrix candidate is valid after the explicit payments made here:

1. the physical terminal dual extends through $\Omega_0,\ldots,\Omega_{24}$;
2. the last-middle residue $3\mathfrak t_{25}e_{Y_m}$ is retained;
3. the mixed inverse gives a $24$-digit finite representative;
4. monic shortening constructs actual $W$-vectors with
   

$$
\deg a_p\le\nu+126;
$$


5. their source vectors have a fixed last-55-row HIGH support modulo $3$;
6. the full actual inverse image is integral;
7. the old inverse zero region gives the additional isotropy digit;
8. the exact nonlinear identity yields whole-middle precision $29$;
9. a one-sided $p=25$ substitution yields one/one precision $33$;
10. complete prefix, $J$- and rank-$b$ inverse changes and returns preserve the claimed final precision.

The new proved result is therefore


$$
\boxed{
S_{\mathrm{act}}-S_c\in3^{29}M,\qquad
\delta S(\mathrm{one},\mathrm{one})\in3^{33},\qquad
T_{\mathrm{act},\mathrm{red}}-T_{c,\mathrm{red}}\in3^7M.
}
$$



The leading actual endpoint is already known and remains a unit on every displayed full-radical generator. Its lowest OPEN label is corrected by reuse, not by a new proof.

The exact remaining local bottleneck is now genuinely higher:

* the first actual endpoint jets in (7.9);
* the complete frame-appropriate endpoint return in (7.11) or (7.13);
* synchronization under exact endpoint adaptation at the physical $3^6$ digit;
* the evaluated actual radical matrix and direction needed for the Smith-direction conditions.

The latest endpoint-adapted complement can preserve the complete current diagonal using only unit divisions. It does not evaluate or erase earlier $1/3$ and $1/9$ returns.

The global bottleneck is unchanged: nonvanishing and decay of the **whole** error after the actual contents, least simultaneous clearer, all-prime final gcd, and actual primitive denominator are used at the same infinite original indices.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ is obtained.}}
$$


