> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1, Turn 14 — A source-specific LOW digit law and a 48-coordinate leading LOW solve

## Abstract and proof status

The rationality or irrationality of $e+\pi$ remains unresolved.

I do **not** obtain a value of either $\eta_0$ or $\eta_{k-1}$. The complete HIGH return, with the physical terminal $Y_m$, remains unpaid. I do obtain a new, uniformly proved result for the actual source defining $\eta_0$:

1. **A digit-support law at the required source precision.**  
   The complete LOW force
   

$$
b_{U,u}=G_c\!\left(x^u,x^D\Omega_P(y)(1-y)^t\right),
   \qquad 0\le u<D,
$$


   satisfies an explicit valuation bound determined by two elementary ternary comparison processes. In particular, a $120$-state support filter certifies which rows are zero modulo $3^{31}$. This is a support theorem, not a producer of all nonzero entries.

2. **An evaluated leading LOW force.**  
   Every LOW entry belongs to $3^{26}\mathbb Z_3$. Its quotient modulo $3$ is exactly $-1$ on one specified ternary-digit set and zero elsewhere.

3. **A 48-coordinate leading LOW inverse image.**  
   Applying the original finite LOW inverse, with its correct reversal convention and physical factor $3^{-1}$, turns that growing digit-supported force into a vector with exactly $48$ nonzero coordinates modulo $3$:
   

$$
-Z^{27P+\Pi}(1+Z^P)^{122}.
$$


   The equality is in the original LOW coordinate space, not in a replacement matrix.

4. **An evaluated leading HIGH force produced by that LOW return.**  
   The resulting HIGH profile consists of three explicitly evaluated binomial bands, repeated with period $243P$, and then restricted to the literal interval $d\le s\le m$. Its coordinate at the physical terminal $Y_m$ is zero. This is only the leading LOW-return contribution at $Y_m$, not the complete terminal response and not a value of $\eta_0$.

5. **A partial certificate of the proposed type.**  
   The resulting sparse integral $W$-coordinate vector $\zeta^{(0)}$ satisfies
   

$$
g_T^T\zeta^{(0)}\in3^{51}\mathbb Z_3,
$$


   so the pairing half of the suggested certificate is paid. However, its LOW residual is only proved to lie in $3^{27}$, and its complete HIGH residual has not been evaluated. Thus
   

$$
b_0-E_c\zeta^{(0)}\in3^{31}M
$$


   has **not** been established.

These statements are proved directly for the current complete core. No old actual-producer terminal scalar is imported, no $12\times12$ Gram replacement is used, and no original-length numerical solve is proposed.

---

## 1. Original domain and the precise target

### 1.1 The original infinite family

All uniform assertions below concern sufficiently large members of exactly the original family


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


with


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
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


As before,


$$
x=y-1,\qquad Q=27P,\qquad Q-N_0=2R,\qquad \chi=P-R,
$$


so


$$
N_0=25P+2\chi,\qquad D=268P+2\chi.
$$



The retained Range III subwindow is


$$
\boxed{\frac3{25}<\frac{\chi}{P}<\frac{31}{250}.}
\tag{1.1}
$$


Its previously certified infinitude is reused at that original-index scope. Nothing below chooses $P$ and $\chi$ independently.

Put


$$
\Pi=P/3,\qquad t=\Pi-2\chi,\qquad
k=3\chi-\Pi-1,\qquad L_*=\frac{P-1}{2}.
$$


After removing a finite initial segment, $k\ge2$. Also


$$
v_3(\chi)=5,\qquad \chi/243\equiv1\pmod9.
$$


Consequently $t>0$, $t$ is odd, and $v_3(t)=5$.

For the proofs it is convenient to write


$$
S=h-32,\qquad P=3^S,\qquad H=3^{S+31}.
\tag{1.2}
$$


We may, and do, restrict to $h\ge63$. This removes only a finite initial segment.

### 1.2 Complete finite spaces and the physical terminal

The spaces remain


$$
U_u=x^u\quad(0\le u<D),
$$




$$
z^{\rm mid}_i=x^Dy^i\quad(0\le i<\nu),
\qquad \nu=D/2-1,
$$




$$
Y_s=y^s\quad(d\le s\le m),
\qquad d=D+\nu=\frac{3D}{2}-1,
$$


and


$$
W=[U\ Y].
$$



The physical HIGH terminal is $Y_m$.

The complete functional is


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^a)=(2a)!.
\tag{1.3}
$$


Its cutoff is exactly


$$
K_{\rm phys}=2n-2=2H-2D+2,
$$


and


$$
2K_{\rm phys}+1=4H-4D+5<3^{h+1}.
$$



For the current complete core,


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A,
$$




$$
G_c(f,g)=\mathcal M(Q_cfg),\qquad E_c=G_c(W,W),
$$




$$
F[p]=x^Dp-WE_c^{-1}G_c(W,x^Dp).
\tag{1.4}
$$


In particular, $\beta\equiv1\pmod3$.

### 1.3 Prefix adaptation and the reused endpoint identity

The finite boundaries remain


$$
R_*=\frac{9Q+1}{2},\qquad a_0=R_*-1,
$$




$$
\tau=\frac{N_0-3}{2},\qquad \ell=3R+1,
$$




$$
K=\{0,\ldots,3R\},\qquad
J=\{\ell,\ldots,\tau-1\},\qquad R_*+\tau=\nu.
$$


The last middle column is


$$
F_T=F[y^{\nu-1}],
$$


and the true unit in the normalized finite $J$-border is


$$
a=\overline B_{\ell,\tau-1}\ne0.
$$



I reuse Turn 13’s specific residual identity and endpoint bare-source theorem. Their ten-response derivation and coefficient calculation are not repeated here. Write


$$
V(y)=1+y^P+y^{2P}
$$


and retain the already derived polynomial


$$
\begin{aligned}
\Omega_P(y)={}&
(1-y)^{2P}\bigl(y^{122P}+3y^{41P}\bigr)\\
&+9V(y)\bigl(2y^{14P}+2y^{41P}+2y^{95P}-y^{131P}\bigr).
\end{aligned}
\tag{1.5}
$$


Its prefix correction is part of its provenance; it is not a bare one-lift with the prefix return omitted.

For


$$
p_0(y)=\Omega_P(y)(1-y)^t,
$$


put


$$
g_T=G_c(W,x^Dy^{\nu-1}),\qquad
b_0=G_c(W,x^Dp_0).
\tag{1.6}
$$


The reused target identity is


$$
\boxed{
\eta_0
=
a^{-1}\frac{g_T^TE_c^{-1}b_0}{3^{29}}
\pmod3.
}
\tag{1.7}
$$


Its quotient is integral. This is the terminal of the complete **core** block.

The new work below evaluates a genuine force channel inside (1.7). It does not identify the core terminal with a terminal of the different actual producer.

---

## 2. Exact LOW/HIGH normalization in the current core

Write the original finite matrix as


$$
E_c=
\begin{pmatrix}
3\mathcal L&3\mathcal X\\
3\mathcal X^T&E_Y
\end{pmatrix},
\tag{2.1}
$$


where


$$
\mathcal L=G_c(U,U)/3,\qquad
\mathcal X=G_c(U,Y)/3.
$$


Set


$$
M_L=\mathcal L^{-1},
\qquad
\mathcal S_H=E_Y-3\mathcal X^TM_L\mathcal X,
\qquad
M_H=\mathcal S_H^{-1}.
\tag{2.2}
$$



All these are the original finite blocks.

### 2.1 Why the displayed normalized blocks are integral and unit

For LOW/LOW and LOW/HIGH products, the rational polynomial in (1.3) has degree strictly below


$$
\frac{3H-1}{2}.
$$


Thus the odd denominator $3H=3^h$ is absent, and division of those pairings by $3$ is an integral map on the relevant integral coefficient spaces.

For example, the LOW/HIGH degree is at most


$$
A+(D-1)+m+1=H+m<\frac{3H-1}{2}
$$


for the present sufficiently large $D$. The LOW/LOW bound is smaller.

Let


$$
r_H=\frac{H-1}{2},\qquad a_L=r_H+1=\frac{H+1}{2}.
$$


The established LOW convolution structure, specialized to this core, is


$$
\boxed{
\overline{\mathcal L}_{uv}
=
[Z^{D-1-u-v}](1+Z)^{-a_L},
\qquad 0\le u,v<D.
}
\tag{2.3}
$$


Here and below a coefficient at a negative index is zero.

For clarity, the scope check for (2.3) is short. Modulo $3$, after division by $3$, only the pole with denominator $H$ survives. Its coefficient is


$$
[y^{r_H}]x^{H-D+u+v}.
$$


If $u+v\ge D$, this vanishes because


$$
x^H\equiv y^H-1\pmod3
$$


and the remaining degree is below $r_H$. If


$$
u+v=D-1-j,
$$


the coefficient is


$$
(-1)^j\binom{r_H+j}{j}
=[Z^j](1+Z)^{-a_L}.
$$


The antidiagonal entries are therefore $1$, proving that $\mathcal L$ is a unit matrix.

Similarly, modulo $3$, $E_Y$ is read from the physical pole $3H$. Its entries below the antidiagonal $s+t=m+d$ are zero, and its entries on that antidiagonal are $1$. Thus $E_Y\bmod3$, and hence $\mathcal S_H\bmod3$, are nonsingular.

It follows that


$$
M_L,\ M_H\in\operatorname{Mat}(\mathbb Z_3).
$$


The physical LOW inverse still costs $3^{-1}$. This is consistent with, and gives the block-level payment behind,


$$
E_c^{-1}\in3^{-1}\operatorname{Mat}(\mathbb Z_3).
$$



No old actual-producer terminal residue is used in this validation.

### 2.2 The two source vectors are divisible by $3$

Partition


$$
g_T=3\binom{\alpha_T}{\upsilon_T},
\qquad
b_0=3\binom{\alpha_0}{\upsilon_0}.
\tag{2.4}
$$


These four vectors are integral.

For $b_0$, the polynomial $x^Dp_0$ lies strictly below the last middle degree. In fact,


$$
\deg(x^Dp_0)=D+133P+t=401P+\Pi=d-P-k.
\tag{2.5}
$$


Every HIGH pairing with it therefore avoids the pole $3H$.

For $g_T$, that pole can occur only at $Y_m$, and only through the $3y$ term of $\beta+3y$. Its coefficient has the required factor $3$. This verifies integrality of $\upsilon_T$ without deleting the physical terminal.

---

## 3. A factorial-ratio lemma for the actual LOW source

The new LOW evaluation uses an exact rational identity, followed by digit counting. No original factorial matrix is constructed.

### 3.1 An evaluated coefficient functional

For integers $N,q\ge0$, define


$$
\mathcal B(N,q)
=
\sum_{j=0}^{N}\frac{(-1)^j\binom Nj}{2(q+j)+1}.
$$


This sum has the exact evaluation


$$
\boxed{
\mathcal B(N,q)
=
\frac{2^N N!}{\displaystyle\prod_{j=0}^{N}(2q+2j+1)}
=
\frac{4^N N!(N+q)!(2q)!}
{q!(2N+2q+1)!}.
}
\tag{3.1}
$$



One derivation is


$$
\mathcal B(N,q)
=\frac12\int_0^1 y^{q-1/2}(1-y)^N\,dy,
$$


followed by $N$ integrations by parts. Thus (3.1) is an evaluation, not an unevaluated named coefficient sum.

For each $e\ge1$, let


$$
j_e(q)
$$


be the least nonnegative residue of


$$
\frac{3^e-1}{2}-q\pmod{3^e}.
$$


Counting the factors divisible by $3^e$ in the odd denominator product gives


$$
\boxed{
v_3\mathcal B(N,q)
=
-\sum_{e\ge1}
\mathbf1_{\{N\bmod3^e\ge j_e(q)\}}.
}
\tag{3.2}
$$



Indeed, the denominator contains


$$
\left\lfloor\frac N{3^e}\right\rfloor
+
\mathbf1_{\{N\bmod3^e\ge j_e(q)\}}
$$


multiples of $3^e$, whereas $N!$ contains
$\lfloor N/3^e\rfloor$. The factor $2^N$ is a unit.

### 3.2 The fourteen actual source terms

For this calculation only, expand the already established residual as


$$
p_0
=
\sum_{(\Delta,a,c)\in\mathcal T}
c\,(1-y)^{t+\Delta}y^{aP},
\tag{3.3}
$$


where the finite set $\mathcal T$ consists of



$$
\begin{array}{c|c|c}
\Delta&a&c\\ \hline
2P&122&1\\
2P&41&3\\
0&14,15,16&18\\
0&41,42,43&18\\
0&95,96,97&18\\
0&131,132,133&-9
\end{array}
\tag{3.4}
$$



This table retains both weighted low terms and every term contributed by $V$. It is not another derivation of $\Omega_P$.

For a LOW row $u$,


$$
b_{U,u}=G_c(x^u,x^Dp_0).
$$


Because $Q_c(-1)=0$, its rational part is


$$
(-1)^{H+u}3^h
\sum_{(\Delta,a,c)\in\mathcal T}
c\left\{
\beta\,\mathcal B(H+u+t+\Delta,aP)
+
3\,\mathcal B(H+u+t+\Delta,aP+1)
\right\}.
\tag{3.5}
$$



The factorial contribution remains part of the complete pairing. It is in $3^h\mathbb Z_3$, so it is invisible at the local precisions used below.

Every term of (3.5) is within the true cutoff. Indeed, with


$$
N=H+r_0,\qquad r_0=u+t+\Delta,\qquad q=aP+\epsilon,
\quad \epsilon\in\{0,1\},
$$


the original finite bound $u\le D-1$ gives


$$
\boxed{r_0+q\le401P+\Pi.}
\tag{3.6}
$$


For the high term with $\Delta=2P,a=122$, the stronger bound is
$392P+\Pi$. Thus the rational polynomial degree is below
$H+402P$, far below $K_{\rm phys}$.

---

## 4. A source-specific ternary support law through $3^{31}$

### 4.1 The two comparison processes

For each original LOW row $u$, let


$$
v(u)=(u+t)\bmod P,\qquad 0\le v(u)<P.
$$


For $\epsilon=0,1$, define


$$
C_e^{(\epsilon)}(u)
=
\mathbf1_{\left\{
v(u)\bmod3^e
\ge \frac{3^e-1}{2}-\epsilon
\right\}},
\qquad 1\le e\le S,
\tag{4.1}
$$


and the defect counts


$$
D_\epsilon(u)
=
\sum_{e=1}^{S}\bigl(1-C_e^{(\epsilon)}(u)\bigr).
\tag{4.2}
$$



These are directly digit-evaluable.

If


$$
v(u)=v_0+3v_1+\cdots+3^{S-1}v_{S-1},
\qquad v_j\in\{0,1,2\},
$$


then


$$
C_1^{(0)}=\mathbf1_{\{v_0\ge1\}},
\qquad C_1^{(1)}=1.
$$


For $e\ge2$, both processes obey the same transition:


$$
C_e^{(\epsilon)}
=
\begin{cases}
0,&v_{e-1}=0,\\
C_{e-1}^{(\epsilon)},&v_{e-1}=1,\\
1,&v_{e-1}=2.
\end{cases}
\tag{4.3}
$$


Thus no binomial array of length $P$ is needed.

### Theorem 4.1 — Complete LOW source valuation law

For every original $0\le u<D$,


$$
\boxed{
v_3(b_{U,u})
\ge
\min\{26+D_0(u),\ 27+D_1(u)\}.
}
\tag{4.4}
$$


Equivalently, for the normalized LOW force $\alpha_0=b_U/3$,


$$
\boxed{
v_3((\alpha_0)_u)
\ge
\min\{25+D_0(u),\ 26+D_1(u)\}.
}
\tag{4.5}
$$



#### Proof

For every source term in (3.5), write $N=H+r_0$.

If


$$
S+7\le e\le S+31,
$$


then $3^e\mid H$, and (3.6) implies


$$
q+r_0<\frac{3^e-1}{2}.
$$


Hence $j_e(q)>r_0=N\bmod3^e$, so the corresponding indicator in (3.2) is zero.

For $e>S+31$, the smallest modulus is $3H$. The whole odd denominator interval lies below $3H$, again by (3.6), so those indicators are also zero.

Only the first $S+6$ indicators can contribute.

For $1\le e\le S$, both $H$ and $\Delta$ are divisible by $3^e$, while $aP\equiv0\pmod{3^e}$. Therefore the first $S$ indicators are exactly $C_e^{(\epsilon)}(u)$, and their sum is $S-D_\epsilon(u)$.

The remaining six indicators contribute at most six. Consequently


$$
v_3\!\left(3^h\mathcal B(N,aP+\epsilon)\right)
\ge
h-\bigl(S-D_\epsilon(u)+6\bigr)
=
26+D_\epsilon(u).
$$


The $\epsilon=1$ term has its additional coefficient $3$, giving
$27+D_1(u)$. Every coefficient $c$ in (3.4) is integral, and $\beta$ is a unit. The factorial part has valuation at least $h$, which is no weaker than these bounds.

Taking the minimum proves (4.4), and division by $3$ proves (4.5). ∎

### 4.2 A precision-sized support filter, with its exact limitation

A consequence at the requested source precision is


$$
\boxed{
D_0(u)\ge5,\quad D_1(u)\ge4
\quad\Longrightarrow\quad
b_{U,u}\equiv0\pmod{3^{31}}.
}
\tag{4.6}
$$



To test this, one need only retain:

- the two binary flags $C^{(0)},C^{(1)}$;
- the first defect count capped at $5$;
- the second defect count capped at $4$.

There are at most


$$
2\cdot2\cdot6\cdot5=120
$$


states. The input is the $S$-digit ternary expansion of the actual residue
$(u+t)\bmod P$.

Likewise, at modulus $3^{29}$,


$$
D_0(u)\ge3,\quad D_1(u)\ge2
\quad\Longrightarrow\quad
b_{U,u}\equiv0\pmod{3^{29}},
\tag{4.7}
$$


with at most $48$ states.

These are uniform source-specific zero tests. They do **not** claim that every accepted row is nonzero, nor do they evaluate the nonzero digits through $3^{31}$. In particular, they are not a precision-sized producer of complete returned Gram entries.

---

## 5. Exact evaluation of the leading LOW force

The preceding bound can be sharpened to an exact leading value.

### Theorem 5.1 — The evaluated order-$26$ LOW source

For $0\le u<D$,


$$
\boxed{
\frac{b_{U,u}}{3^{26}}
=
-\mathbf1_{\left\{
u=240P-t+v,\ 
0\le v<P,\ 
\text{every ternary digit of }v\text{ is }1\text{ or }2
\right\}}
\pmod3.
}
\tag{5.1}
$$



Every row on the right lies inside the original finite LOW interval.

### 5.1 Identification of the possible support

All terms in (3.5), except the $\beta$-part with


$$
\Delta=2P,\qquad a=122,\qquad c=1,
$$


have at least one extra factor of $3$. Thus only that term can contribute to $b_U/3^{26}\bmod3$.

Put


$$
r=u+t+2P,\qquad N=H+r,\qquad q=122P.
$$


A nonzero residue at order $26$ requires all of the first $S+6$ indicators in (3.2) to be $1$.

At the modulus $243P$, the relevant least residue is


$$
j_{S+5}(122P)=242P+\frac{P-1}{2}=242P+L_*.
$$


Since


$$
0<r<271P<2\cdot243P,
$$


this forces


$$
r=242P+v,\qquad L_*\le v<P.
\tag{5.2}
$$



On this interval, the six indicators for moduli


$$
3P,\ 9P,\ 27P,\ 81P,\ 243P,\ 729P
$$


are all $1$. For example, $242\equiv-1\pmod{3^a}$ for $1\le a\le5$, and the relevant residue threshold is


$$
(3^a-1)P+L_*.
$$



For the first $S$ indicators, all comparisons hold if and only if every ternary digit of $v$ is $1$ or $2$. This follows immediately from (4.3): a digit $0$ makes its current comparison fail, whereas digits $1,2$, starting with a true comparison, preserve truth.

Thus the only possible support is


$$
u=240P-t+v
$$


with all digits of $v$ in $\{1,2\}$.

The finite boundaries are explicit:


$$
u\ge240P-t+L_*>0,
$$


and


$$
u\le241P-t-1<D,
$$


because


$$
D-(241P-t-1)=27P+\Pi+1>0.
\tag{5.3}
$$



### 5.2 Evaluation of the normalized unit

It remains to determine the residue, rather than merely its support.

For an integer $n\ge0$, write $N_2(n)$ for the number of digits equal to $2$ in its ternary expansion. The unit part of a factorial satisfies


$$
\boxed{
\frac{n!}{3^{v_3(n!)}}
\equiv
(-1)^{v_3(n!)+N_2(n)}
\pmod3.
}
\tag{5.4}
$$


Indeed, each complete block of nonmultiples of $3$ contributes $1\cdot2=-1$, and iteration through $n,\lfloor n/3\rfloor,\ldots$ gives (5.4).

On the support (5.2),


$$
N=H+242P+v,\qquad q=122P.
$$


Write $N_v=N_2(v)$, and put


$$
w=2v+1-P.
$$


Because every digit of $v$ is $1$ or $2$, the digits of $w$ are respectively $0$ or $2$. Hence


$$
N_2(w)=N_v.
$$



The five factorial arguments in (3.1) have the following counts:


$$
\begin{array}{c|c}
\text{argument}&N_2(\text{argument})\\ \hline
N&5+N_v\\
N+q&N_v\\
2q&0\\
q&1\\
2N+2q+1&1+N_v
\end{array}
\tag{5.5}
$$


Here one uses


$$
242=(22222)_3,\quad
122=(11112)_3,\quad
244=(100001)_3,\quad
364=(111111)_3,
$$


and


$$
2N+2q+1=2H+729P+w.
$$



The valuation in (3.2) is exactly $-(S+6)$. Using (3.1), (5.4), and (5.5), the normalized beta unit is


$$
3^{S+6}\mathcal B(N,q)
\equiv(-1)^{S+1+N_v}\pmod3.
$$


The source in (3.5) has the additional sign $(-1)^{H+u}=(-1)^{u+1}$, and $\beta\equiv1$. Therefore


$$
\frac{b_{U,u}}{3^{26}}
\equiv(-1)^{u+S+N_v}.
$$



Finally,


$$
u=240P-t+v,
$$


with $t$ odd, while


$$
v\equiv S-N_v\pmod2.
$$


Thus $u+S+N_v$ is odd. The residue is $-1$, proving (5.1). ∎

### 5.3 Compact generating polynomial for the leading force

Let $\mathbf c_0$ be the leading LOW vector in (5.1), and use $Z$ as a coordinate-generating variable:


$$
C_0(Z)=\sum_{u=0}^{D-1}(\mathbf c_0)_u Z^u.
$$


The digit description gives


$$
\boxed{
C_0(Z)
=
-Z^{240P-t+L_*}(1+Z)^{L_*}
\quad\text{in }\mathbb F_3[Z].
}
\tag{5.6}
$$


Indeed,


$$
\sum_{\substack{0\le v<P\\v_e\in\{1,2\}}}Z^v
=
Z^{L_*}\prod_{e=0}^{S-1}(1+Z^{3^e})
=
Z^{L_*}(1+Z)^{L_*}.
$$



This polynomial has growing support, but its actual LOW inverse image does not.

---

## 6. The original finite LOW inverse produces 48 coordinates

### 6.1 The convolution orientation is retained

For the matrix (2.3), the finite inverse rule is


$$
\boxed{
(\overline{\mathcal L}^{-1}c)_u
=
[Z^u](1+Z)^{a_L}
\sum_{j=0}^{D-1}c_{D-1-j}Z^j.
}
\tag{6.1}
$$


Thus the LOW rule reverses the input and takes increasing output coefficients.

This is the supplied finite LOW convention. The HIGH inverse uses a different reversal convention; it is not substituted into (6.1).

### Theorem 6.1 — A 48-coordinate leading LOW solution

Let


$$
\mathbf z_L=\overline{\mathcal L}^{-1}\mathbf c_0.
$$


Then


$$
\boxed{
\sum_{u=0}^{D-1}(\mathbf z_L)_u Z^u
=
-Z^{27P+\Pi}(1+Z^P)^{122}
\quad\text{in }\mathbb F_3[Z].
}
\tag{6.2}
$$


The right side lies entirely inside the original LOW interval.

Consequently,


$$
\boxed{
M_L\alpha_0
=
3^{25}\mathbf z_L+3^{26}\mathbf e_L
}
\tag{6.3}
$$


for a definite integral vector $\mathbf e_L$.

#### Proof

Reverse the polynomial (5.6) through the actual length $D$:


$$
\begin{aligned}
Z^{D-1}C_0(Z^{-1})
&=
-Z^{D-1-(240P-t+2L_*)}(1+Z)^{L_*}\\
&=
-Z^{27P+\Pi}(1+Z)^{L_*}.
\end{aligned}
\tag{6.4}
$$


The cancellation


$$
D-241P+t=27P+\Pi
$$


uses the original identity $D=268P+2\chi$ and $t=\Pi-2\chi$.

Applying (6.1) gives


$$
-Z^{27P+\Pi}(1+Z)^{(H+P)/2}\pmod{Z^D}.
\tag{6.5}
$$


In characteristic $3$,


$$
(1+Z)^{(H+P)/2}
=
(1+Z^P)^{(3^{31}+1)/2}.
$$


Moreover,


$$
\frac{3^{31}+1}{2}\equiv122\pmod{243}.
$$


The original boundary satisfies


$$
D-(27P+\Pi)<241P.
\tag{6.6}
$$


Hence terms of degree $243$ or higher in the variable $Z^P$ cannot enter the finite output. Therefore (6.5) equals


$$
-Z^{27P+\Pi}(1+Z^P)^{122}.
$$



Its degree is


$$
149P+\Pi<D.
$$


Finally, (5.1) gives


$$
\alpha_0=b_U/3=3^{25}\mathbf c_0+3^{26}M,
$$


and the integral unit inverse $M_L$ proves (6.3). ∎

### 6.2 Literal coordinates and values

Define


$$
\mathcal J_{122}
=
\left\{
a_0+3a_1+9a_2+27a_3+81a_4:
a_0\in\{0,1,2\},\
a_1,a_2,a_3,a_4\in\{0,1\}
\right\}.
\tag{6.7}
$$


This set has $3\cdot2^4=48$ elements.

The nonzero coordinates of $\mathbf z_L$ are precisely


$$
\boxed{
u=27P+\Pi+jP,\qquad j\in\mathcal J_{122}.
}
\tag{6.8}
$$


Their values are


$$
(\mathbf z_L)_u=
-\binom{2}{a_0}
=
\begin{cases}
2,&a_0=0\text{ or }2,\\
1,&a_0=1,
\end{cases}
\quad\text{in }\mathbb F_3.
\tag{6.9}
$$



Thus the growing digit-supported leading LOW force has a fixed-size inverse-coordinate certificate. This is a statement about one normalized force and one leading inverse action. It is not a fixed-size construction of the whole matrix $E_c^{-1}$.

---

## 7. The evaluated HIGH profile of the leading LOW return

The leading LOW solution in (6.2) has a particularly simple interpretation in the original polynomial space:


$$
U\mathbf z_L
=
-x^{27P+\Pi}y^{122P}
\quad\text{in }\mathbb F_3[y].
\tag{7.1}
$$


Indeed,


$$
1+x^P=(1+x)^P=y^P
$$


in characteristic $3$.

Define the actual leading HIGH return profile


$$
\Lambda=\overline{\mathcal X}^{\,T}\mathbf z_L
\in\mathbb F_3^{\{d,\ldots,m\}}.
\tag{7.2}
$$



### Theorem 7.1 — Three finite binomial bands for the HIGH LOW-return channel

For every original $d\le s\le m$, put


$$
\varrho_s=\frac{H-1}{2}-s-122P.
\tag{7.3}
$$


Let $r_s$ be its least nonnegative residue modulo $243P$. Then


$$
\boxed{
\Lambda_s=
\begin{cases}
(-1)^{r_s-qP}\displaystyle\binom{t}{r_s-qP}\pmod3,
&
r_s\in qP+[0,t]\text{ for some }q\in\{0,1,2\},
\\[2mm]
0,&\text{otherwise}.
\end{cases}
}
\tag{7.4}
$$


The three intervals in (7.4) are disjoint.

In particular,


$$
\boxed{\Lambda_m=0.}
\tag{7.5}
$$


Also,


$$
\boxed{
\Lambda_s\ne0\quad\Longrightarrow\quad s\equiv121\pmod{243}.
}
\tag{7.6}
$$



#### Proof

The normalization $\mathcal X=G_c(U,Y)/3$ is an integral map on the entire bounded-degree LOW space. Therefore reduction of (7.1) modulo $3$ is legitimate before applying $\overline{\mathcal X}^{\,T}$.

At this normalized precision, only the pole with denominator $H$ contributes. Thus


$$
\Lambda_s
=
-[y^{\varrho_s}]x^{A+27P+\Pi}.
$$


Since


$$
A+27P+\Pi=H-241P+t
$$


is odd, this becomes


$$
\Lambda_s
=
[y^{\varrho_s}](1-y)^{H-241P+t}.
\tag{7.7}
$$



For every original HIGH row,


$$
0\le\varrho_s<H.
$$


At the upper boundary,


$$
\varrho_m=\nu-122P=12P+\chi-1>0.
$$


Therefore, for the coefficient in (7.7), the factor
$(1-y)^H=1-y^H$ can be replaced by $1$ in $\mathbb F_3$. We get


$$
\begin{aligned}
\Lambda_s
&=
[y^{\varrho_s}]
\frac{(1-y)^t}{(1-y^P)^{241}}\\
&=
[y^{\varrho_s}]
\frac{(1-y)^t(1-y^P)^2}{1-y^{243P}}.
\end{aligned}
\tag{7.8}
$$


Since


$$
(1-y^P)^2=1+y^P+y^{2P}
\quad\text{in }\mathbb F_3,
$$


formula (7.8) gives exactly the three bands in (7.4). Because $t<P$, they do not overlap.

At $s=m$, the residue is literally


$$
r_m=12P+\chi-1.
$$


It lies below $243P$ and above $2P+t$, since


$$
12P+\chi-1-(2P+t)=10P+k>0.
$$


This proves (7.5).

Finally, $v_3(t)=5$, so


$$
(1-y)^t\in\mathbb F_3[y^{243}].
$$


Every nonzero band coefficient therefore has $r_s\equiv0\pmod{243}$. As $243\mid P$,


$$
\varrho_s\equiv121-s\pmod{243},
$$


which proves (7.6). ∎

### 7.1 How the law enters the complete HIGH force

Choose the canonical integral lift of the $48$-coordinate vector $\mathbf z_L$. Equation (6.3) gives the exact expansion


$$
M_L\alpha_0=3^{25}\mathbf z_L+3^{26}\mathbf e_L.
$$


Consequently,


$$
\boxed{
\upsilon_0-\mathcal X^TM_L\alpha_0
\equiv
\upsilon_0-3^{25}\Lambda
\pmod{3^{26}}.
}
\tag{7.9}
$$



This is an evaluated leading LOW-return correction to the actual HIGH source. The unknown higher LOW returns remain in the modulus-$3^{26}$ remainder.

The value $\Lambda_m=0$ does not remove $Y_m$ from the next solve. In particular:

- $(M_H\Lambda)_m$ need not be zero;
- the complete HIGH source $\upsilon_0$ has not been evaluated here;
- the terminal test vector is not replaced by a coordinate functional;
- the higher LOW-return digits have not vanished merely because their leading terminal coordinate does.

---

## 8. The complete bilinear return and the exact remaining obstruction

### 8.1 The direct LOW/LOW bilinear term is too deep to matter here

The same factorial-ratio count used above gives


$$
\boxed{g_{T,U}\in3^{26}\mathbb Z_3^D.}
\tag{8.1}
$$


Indeed, for these entries the beta top is $H+u$, and the two shifts are
$\nu-1$ and $\nu$. Their residual upper bound is


$$
u+\nu\le d-1=402P+3\chi-2<403P.
$$


Thus all denominator indicators above $S+6$ vanish, giving valuation at least $26$.

Hence


$$
\alpha_T,\alpha_0\in3^{25}\mathbb Z_3^D.
\tag{8.2}
$$



Define the complete LOW-returned HIGH sources


$$
\mathfrak t_H=\upsilon_T-\mathcal X^TM_L\alpha_T,
\qquad
\mathfrak b_H=\upsilon_0-\mathcal X^TM_L\alpha_0.
\tag{8.3}
$$


Exact block elimination in (2.1) yields


$$
\boxed{
g_T^TE_c^{-1}b_0
=
3\alpha_T^TM_L\alpha_0
+
9\mathfrak t_H^TM_H\mathfrak b_H.
}
\tag{8.4}
$$


Every LOW and HIGH return is present in this identity.

By (8.2), the first term belongs to $3^{51}\mathbb Z_3$. Combining (1.7) and (8.4),


$$
\boxed{
a\eta_0
=
\frac{\mathfrak t_H^TM_H\mathfrak b_H}{3^{27}}
\pmod3.
}
\tag{8.5}
$$


The numerator in (8.5) is integral and divisible by $3^{27}$, as follows from the reused endpoint identity and the paid $3^{51}$ LOW term.

Equation (8.5) is not presented as an evaluation. Its purpose is to place the newly evaluated channel (7.9) inside the complete return, with the physical $Y_m$ still in $M_H$.

### 8.2 What the sparse certificate does prove

Define an integral $W$-coordinate vector


$$
\zeta^{(0)}
=
\binom{3^{25}\mathbf z_L}{0}.
\tag{8.6}
$$


It uses only the $48$ original LOW coordinates in (6.8).

The LOW part of its residual satisfies


$$
\boxed{
b_{0,U}-3\mathcal L(3^{25}\mathbf z_L)
\in3^{27}\mathbb Z_3^D.
}
\tag{8.7}
$$


Moreover, by (8.1),


$$
\boxed{
g_T^T\zeta^{(0)}
=
g_{T,U}^T(3^{25}\mathbf z_L)
\in3^{51}\mathbb Z_3.
}
\tag{8.8}
$$



Thus the second half of the proposed certificate


$$
g_T^T\zeta\in3^{30}\mathbb Z_3
$$


is established for this sparse vector, with substantial margin.

The first half is not established. Its exact residual is


$$
b_0-E_c\zeta^{(0)}
=
\binom{
b_{0,U}-3^{26}\mathcal L\mathbf z_L
}{
b_{0,Y}-3^{26}\mathcal X^T\mathbf z_L
}.
\tag{8.9}
$$


The upper component is known only modulo $3^{27}$, not $3^{31}$. The lower component still contains the complete unevaluated HIGH force.

Consequently, the $3^{-1}$ inverse allowance cannot turn (8.7) into the required $3^{30}$ return cancellation.

### 8.3 The precise unpaid source information

For (8.5), it is sufficient to evaluate the whole scalar


$$
\mathfrak t_H^TM_H\mathfrak b_H\pmod{3^{28}}.
\tag{8.10}
$$


The present work does not do so.

The new LOW result supplies only


$$
3^{-25}M_L\alpha_0\bmod3.
$$


To obtain this LOW-returned vector modulo $3^{28}$, two further digits are required:


$$
M_L\alpha_0
\equiv
3^{25}\bigl(\mathbf z_L+3\mathbf z_1+9\mathbf z_2\bigr)
\pmod{3^{28}}.
\tag{8.11}
$$


Neither $\mathbf z_1$ nor $\mathbf z_2$ is evaluated here.

The complete HIGH obligation additionally retains:

- the actual $\upsilon_0=b_{0,Y}/3$;
- the actual $\upsilon_T=g_{T,Y}/3$;
- the LOW return of $\alpha_T$;
- the original finite unit inverse $M_H$, including both ends of $d,\ldots,m$.

A 48-coordinate leading LOW solution is not a precision-sized producer of these complete data.

### 8.4 A concrete next source lemma

The new support filter gives a specific next LOW task rather than an unspecified large solve:

> **Two-jet LOW extension lemma for the residual source.**  
> Construct precision-local descriptions of $\mathbf z_1,\mathbf z_2$ in (8.11), in the original finite LOW interval, and verify
> 

$$
> \mathcal L
> \bigl(\mathbf z_L+3\mathbf z_1+9\mathbf z_2\bigr)
> \equiv
> b_{0,U}/3^{26}
> \pmod{27}.
>
$$


> The source side has the $48$-state support restriction (4.7). The proof must retain the actual next two digits of $\mathcal L$, including the carries caused by the chosen integral lifts.

This lemma would finish the LOW source contribution at the precision needed in (8.10). It would not by itself evaluate the full HIGH return.

The main endpoint bottleneck is still the source-specific evaluation of (8.10), or an equally strong compact certificate for the full residual (8.9).

---

## 9. Scope of reuse and limitations of the old terminal framework

The old terminal-representer excerpts are useful structural evidence, but their evaluated objects are different.

Their polynomial


$$
\rho=YH_{\rm inv}e_m-UMXH_{\rm inv}e_m
$$


contains a LOW return and is a true HIGH terminal representer. Their LOW and HIGH convolution conventions are different. Their finite Neumann expansions retain original-length vectors.

None of the following has been imported here:

- an old value of $\rho$, $g$, $k$, $\tau$, or $\gamma$;
- a residue belonging to the older correction $3^6R$;
- the older producer precision budget $p+9$;
- an identification of the old actual terminal with the present core terminal.

The sole convolution rule used in the new calculation is the finite LOW rule (6.1), and its parameters were checked directly in the current core in Section 2. The $48$-coordinate result is a new application to the current residual source, not a rerun of an old inverse-block receipt.

Likewise, the already closed prefix-$6$, terminal-aware $J6$, and bare endpoint calculations are not reopened. Their scope does not supply the missing value of (8.10).

---

## 10. Consequences that are not yet available

Since neither endpoint coordinate has closed, I do not proceed to the secondary mixed-prefix calculation.

The known physical-$6$ assembly still has the form


$$
C_6
=
C^{\rm mom}
-\bigl(e_{k-1}\eta^T+\eta e_{k-1}^T\bigr)
-R_4
\pmod3,
\tag{10.1}
$$


with $\eta$ and the actual first-$4$ return $R_4$ not fully evaluated.

In particular, the first-$4$ cross retains


$$
P_{ui}=\frac{d_u^T\mathsf A^{-1}d_H{}_i}{3}\pmod3
$$


and its upper $3y$ corner:


$$
(C_H)_{ui}
=
-c_{P-1-u-i-\Pi}
+c_{P-1-u-i-2\Pi}
-2\,\mathbf1_{u=R,\ i=k-1}
-P_{ui}.
\tag{10.2}
$$


The inverse in $R_4=C_H^TA_4^{-1}C_H$ remains the original finite inverse.

The later direction is still


$$
B_6x=w_6,\qquad x\in3^{-1}\mathbb Z_3^{k-1}.
$$


A leading matrix calculation does not decide this paid directional lift. The physical-$5$ complementary and kernel-pivot returns, the higher endpoint adaptation, the actual/core difference, and source precision $34$ remain necessary at the next whole layer.

The diagonal payments also remain


$$
\lambda_{\rm new}
=
\lambda^{\rm pref}
-\frac13f_J^TB^{-1}f_J
-\frac19f_b^TA_b^{-1}f_b
\in3^{-2}\mathbb Z_3,
$$




$$
\lambda_4
=
\lambda_{\rm new}
-\frac1{3^4}f_C^TA_4^{-1}f_C
\in3^{-4}\mathbb Z_3.
$$


No unit numerator or missing return is inferred from the new LOW law.

---

## 11. Bounded exact arithmetic that can verify the new constants

No computation was performed.

No original factorial matrix, moment matrix, old terminal table, old inverse receipt, or original-length vector calculation is requested.

### 11.1 Optional universal polynomial receipt

The new constant-size identities can be checked with coefficient arrays of length at most $244$.

**Inputs**


$$
122,\quad241,\quad243,\quad \frac{3^{31}+1}{2},
$$


the field $\mathbb F_3$, and coefficient indices $0,\ldots,243$.

**Expected verifiable outputs**

1. The truncated identity
   

$$
(1+Z)^{(3^{31}+1)/2}
   \equiv(1+Z)^{122}
   \pmod{3,\ Z^{241}}.
$$



2. The exact factorization in $\mathbb F_3[Z]$
   

$$
(1+Z)^{122}
   =
   (1+Z)^2(1+Z^3)(1+Z^9)(1+Z^{27})(1+Z^{81}).
$$



3. Exactly $48$ nonzero coefficients, at the exponents in (6.7), with
   

$$
-[Z^j](1+Z)^{122}
   =
   \begin{cases}
   2,&j\bmod3=0\text{ or }2,\\
   1,&j\bmod3=1,
   \end{cases}
$$


   on that support.

4. The periodic-band identity
   

$$
(1-Z)^{241}(1+Z+Z^2)=1-Z^{243}
   \quad\text{in }\mathbb F_3[Z].
$$



These identities have already been proved algebraically above. Such a receipt would be an auxiliary finite check of the new constants, not an original-index endpoint computation.

### 11.2 What is not yet a feasible endpoint experiment

The $120$-state filter and the $48$-coordinate vector do not produce the complete returned HIGH entries in (8.10). Therefore no numerical experiment for $\eta_0$ is advertised as feasible on the basis of this report.

Before an endpoint experiment, one still needs a proved precision-sized producer for the relevant complete HIGH source and inverse action, with the literal interval $d,\ldots,m$ and the physical terminal retained.

---

## 12. Complete producer, forcing, and unchanged global normalization

The current actual producer remains


$$
Q_{\rm act}=Q_c+3^7\mathscr R.
$$


Nothing in the local core calculation changes it.

Retain


$$
F_{\rm fac}=(n-1)!,
$$




$$
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},
$$




$$
\gamma_0=1,\qquad\gamma_1=0,\qquad
\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1},
$$




$$
h_{\rm vec}
=
T_n^{-1}
\left(\binom{n+a}{a}\gamma_{n+a}\right)_{a=0}^{n-1},
$$




$$
u_a=\frac{F_{\rm fac}(-2)^a}{a!},
\qquad v=T_n^{-1}u,
$$




$$
b_{\rm force}=-n-66,
$$




$$
t_{\rm force}
=
3nh_{\rm vec}
+(b_{\rm force}+6)e_{n-1}
+\frac{2b_{\rm force}}{n-1}e_{n-2},
$$




$$
\xi=\frac{u^Tt_{\rm force}}{F_{\rm fac}^2-u^Tv}.
$$


The complete signed coefficients and endpoint remain


$$
[x^a](3^7\mathscr R)
=
-\frac{F_{\rm fac}}{a!}
\bigl((t_{\rm force})_a+\xi v_a\bigr),
\qquad0\le a\le n-1,
$$




$$
\mathscr R(-1)=-\frac{\xi F_{\rm fac}^2}{3^7}.
\tag{12.1}
$$



The complete forcing identity is unchanged:


$$
\boxed{
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
}
\tag{12.2}
$$


Neither forcing term nor the terminal coordinate is discarded.

The complete moment recurrence remains


$$
\mu_{r+1}+\mu_r
=
\frac{3^h}{2r+1}
-\frac{3^h}{4}\bigl((2r+2)!+(2r)!\bigr),
\qquad0\le r\le2n-2,
$$


with its genuine resonant division at


$$
r_*=\frac{3^h-5}{2}.
\tag{12.3}
$$



The factorial part was invisible only at the explicitly paid local ternary precisions. It has not been removed from the complete functional, producer, recurrence, determinant, or whole error.

### 12.1 Actual contents, least clearer, and all-prime gcd

All actual integer column contents remain those of the original complete construction. The least simultaneous clearer remains the actual $\ell_{\rm clr}$. Neither is replaced by a power of $3$, by a convenient common multiple, or by a content measured in the present local coordinate system.

Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the final gcd over **all primes**


$$
G=\gcd(|A_\ell|,|B_\ell|).
$$


For $B_\ell\ne0$, the actual primitive numerator and denominator are


$$
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{G},
\qquad
q=\frac{|B_\ell|}{G}.
$$


The whole evaluated error remains


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{G}\det H_{\rm complete}.
}
\tag{12.4}
$$



An irrationality proof would require, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\log G-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|
\longrightarrow+\infty.
\tag{12.5}
$$


These conditions would make the nonzero whole errors tend to zero. If $e+\pi$ were rational with denominator $d$, every such nonzero error would have absolute value at least $1/d$, a contradiction.

No assertion in (12.5) follows from the local LOW source calculation.

---

## 13. Conclusion

### New proved results

Uniformly on the original sufficiently large Range III subwindow:

1. The complete LOW force for the actual residual source at $i=0$ obeys
   

$$
v_3(b_{U,u})
   \ge\min\{26+D_0(u),27+D_1(u)\},
$$


   giving a $120$-state zero filter modulo $3^{31}$.

2. Its leading quotient is fully evaluated:
   

$$
b_{U,u}/3^{26}
   =
   -1
$$


   exactly on the specified ternary-digit band
   

$$
u=240P-t+v,\qquad v_e\in\{1,2\},
$$


   and is zero elsewhere modulo $3$.

3. The original finite LOW inverse turns this into the $48$-coordinate vector
   

$$
\boxed{
   -Z^{27P+\Pi}(1+Z^P)^{122}.
   }
$$



4. Its leading HIGH LOW-return channel is the explicitly evaluated three-band law (7.4), on the literal interval $d\le s\le m$. In particular, its physical terminal coordinate is zero.

5. The resulting sparse integral vector satisfies
   

$$
g_T^T\zeta^{(0)}\in3^{51}\mathbb Z_3,
$$


   but its complete residual has not reached the required $3^{31}$ precision.

### Exact remaining local bottleneck

Neither $\eta_0$ nor $\eta_{k-1}$ has been evaluated.

The remaining value of $\eta_0$ is the complete finite HIGH bilinear return


$$
\frac{\mathfrak t_H^TM_H\mathfrak b_H}{3^{27}}\pmod3,
$$


with the full LOW-returned sources and the physical $Y_m$ retained. The leading LOW profile, even with its zero physical terminal coordinate, does not determine that scalar.

The next concrete LOW lemma is the two-jet extension (8.11). The full endpoint gate additionally needs a source-specific precision-local evaluation of the complete HIGH return.

### Global proof status

The new result is a **source-specific digit-support theorem, an evaluated leading force, and a compact original-coordinate LOW solve**. It is not a completed endpoint evaluation, an actual/core terminal transport theorem, or a proof about the all-prime primitive whole error.



$$
\boxed{
\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ is obtained.}
}
$$


