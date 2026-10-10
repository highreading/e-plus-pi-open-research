> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1, Turn 16 — A complete HIGH column-defect law and a paid first directional lift

## Abstract and proof status

The rationality or irrationality of $e+\pi$ remains unresolved. In particular, this report does **not** evaluate $\eta _0$ or $\eta _{k-1}$.

There is nevertheless a new reduction of the actual HIGH problem.

Let


$$
\delta_H=\frac{\upsilon_T-\mathcal S_H e_d}{3},
\qquad
\mathcal S_H=E_Y-3\mathcal X^TM_L\mathcal X.
$$


I obtain a complete, precision-$26$ law


$$
\boxed{\delta_H\equiv \delta_{\rm raw}+3^{25}R_d\pmod{3^{26}}.}
\tag{A}
$$


Here:

* every coordinate of $\delta_{\rm raw}$ is given by at most four evaluated factorial ratios and two negative-binomial coefficients;
* $R_d$ is an explicit finite binomial profile;
* no LOW inverse remains unevaluated in this column law;
* both original HIGH boundaries are retained.

The physical edge values are particularly simple:


$$
\boxed{
(\delta_H)_d=0,\qquad
(\delta_H)_{m-1}=\mathcal U,\qquad
(\delta_H)_m=
\frac{4D-H-72}{3}\mathcal U+3^{25}
\pmod{3^{26}},
}
\tag{B}
$$


where $\mathcal U$ is a fixed, explicitly specified $3$-adic unit, independent of the sufficiently large original index. The term $3^{25}$ at $Y_m$ is an actual LOW **matrix-return** contribution. It is not deleted.

A second new result is an actual finite leading inverse action. Put


$$
a_*=\frac H3+\nu-1
$$


and let $z^{(0)}$ be the HIGH-coordinate vector of


$$
\boxed{
Z^{(0)}(y)=x^Dy^{a_*}-y^{d+1}.
}
\tag{C}
$$


Both terms lie wholly in the literal interval $d,\ldots,m$. I prove


$$
\boxed{
w_H\equiv z^{(0)}\pmod3,
\qquad
\mathcal S_H(e_d+3z^{(0)})-\upsilon_T\in 3^2\mathbb Z_3^{\{d,\ldots,m\}}.
}
\tag{D}
$$


This is only a modulus-$9$ certificate, not the requested modulus-$3^{27}$ certificate.

Crucially, the chosen integral lift in (C) is then contracted with the **complete** fourteen-term source, not merely its leading digit:


$$
\boxed{
(z^{(0)})^Tf_H\in3^{29}\mathbb Z_3.
}
\tag{E}
$$


Thus its contribution to the requested scalar is evaluated as zero modulo $3^{26}$.

Writing


$$
w_H=z^{(0)}+3w^{(1)},
$$


the remaining scalar is reduced to


$$
\boxed{
a\eta_0=\frac{(w^{(1)})^Tf_H}{3^{24}}\pmod3,
\qquad
(w^{(1)})^Tf_H\pmod{3^{25}}.
}
\tag{F}
$$


The true finite Schur matrix remains in this last inverse problem. No endpoint value follows yet.

The earlier source-return cancellation, LOW48 result, leading terminal baseline, and their distinct audit statuses are retained. Their proofs and the $729$-position unit-product derivation are not repeated.

---

## 1. Original objects and scope of reuse

### 1.1 The unchanged original indices

All uniform assertions below concern sufficiently large tuples in exactly the supplied original domain:


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
P=3^{h-32},\qquad P_0=243P=3^{h-27},\qquad N_0=243r,
$$




$$
D=P_0+N_0,\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$




$$
4^j=243(3^{26}-1)P-243r+1.
$$


Also retain


$$
Q=27P,\qquad Q-N_0=2R,\qquad \chi=P-R,
$$


so that


$$
N_0=25P+2\chi,\qquad D=268P+2\chi,
$$


and the original Range III restriction is


$$
\boxed{\frac3{25}<\frac{\chi}{P}<\frac{31}{250}.}
\tag{1.1}
$$



No independent choices of $P$ and $\chi$ are made. The previously established infinitude is reused only at this original-index scope.

Put


$$
\Pi=P/3,\qquad t=\Pi-2\chi,\qquad
k=3\chi-\Pi-1,
$$


and retain


$$
v_3(\chi)=5,\qquad \chi/243\equiv1\pmod9.
$$


As in the supplied reports, write


$$
S=h-32,\qquad P=3^S,\qquad H=3^{S+31},
$$


and restrict to $h\ge63$, hence $S\ge31$.

Useful consequences are


$$
D<269P,\qquad
\nu=134P+\chi-1<135P,
\qquad
H>12D+10.
\tag{1.2}
$$



### 1.2 Literal finite spaces and corrected columns

The spaces remain


$$
U_u=x^u,\quad 0\le u<D,\qquad x=y-1,
$$




$$
z_i^{\rm mid}=x^Dy^i,\quad 0\le i<\nu,\qquad \nu=D/2-1,
$$




$$
Y_s=y^s,\quad d\le s\le m,\qquad d=D+\nu=\frac{3D}{2}-1,
$$


and


$$
W=[U\ Y].
$$



The physical HIGH terminal is $Y_m$. The last middle polynomial is $y^{\nu-1}$. Neither is replaced.

The complete functional is


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{v=0}^{K_{\rm phys}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
$$


where


$$
\mathfrak f(y^a)=(2a)!,
\qquad
K_{\rm phys}=2n-2=2H-2D+2.
\tag{1.3}
$$



For the current complete core,


$$
Q_c=(y+1)x^A(\beta+3y),
\qquad
\beta=D-H-71,
$$




$$
G_c(f,g)=\mathcal M(Q_cfg),\qquad E_c=G_c(W,W),
$$




$$
F[p]=x^Dp-WE_c^{-1}G_c(W,x^Dp).
\tag{1.4}
$$



The finite prefix and tail boundaries remain


$$
R_*=\frac{9Q+1}{2},\qquad a_0=R_*-1,
$$




$$
\tau=\frac{N_0-3}{2},\qquad \ell=3R+1,
$$




$$
K=\{0,\ldots,3R\},\qquad J=\{\ell,\ldots,\tau-1\},
\qquad R_*+\tau=\nu.
$$


The endpoint unit remains


$$
a=\overline B_{\ell,\tau-1}.
$$



### 1.3 The complete residual source

Retain the already prefix-corrected polynomial


$$
\begin{aligned}
\Omega_P(y)={}&
(1-y)^{2P}\bigl(y^{122P}+3y^{41P}\bigr)\\
&+9(1+y^P+y^{2P})
\bigl(2y^{14P}+2y^{41P}+2y^{95P}-y^{131P}\bigr),
\end{aligned}
$$


and put


$$
p_0=\Omega_P(y)(1-y)^t.
$$



Its literal fourteen-term expansion is


$$
p_0=\sum_{(\Delta,b,c)\in\mathcal T}
c(1-y)^{t+\Delta}y^{bP},
\tag{1.5}
$$


with


$$
\begin{array}{c|c|c}
\Delta&b&c\\ \hline
2P&122&1\\
2P&41&3\\
0&14,15,16&18\\
0&41,42,43&18\\
0&95,96,97&18\\
0&131,132,133&-9 .
\end{array}
\tag{1.6}
$$



Define


$$
g_T=G_c(W,x^Dy^{\nu-1}),\qquad
b_0=G_c(W,x^Dp_0).
$$



The finite decomposition is


$$
E_c=
\begin{pmatrix}
3\mathcal L&3\mathcal X\\
3\mathcal X^T&E_Y
\end{pmatrix},
$$




$$
M_L=\mathcal L^{-1},\qquad
\mathcal S_H=E_Y-3\mathcal X^TM_L\mathcal X,\qquad
M_H=\mathcal S_H^{-1}.
\tag{1.7}
$$


The established finite unit results give integral $M_L,M_H$. The physical LOW inverse still costs $3^{-1}$.

As before,


$$
g_T=3\binom{\alpha_T}{\upsilon_T},
\qquad
b_0=3\binom{\alpha_0}{\upsilon_0},
$$


and


$$
f_H=\frac{\upsilon_0}{3}
=\frac{G_c(Y,x^Dp_0)}9.
\tag{1.8}
$$



The previously proved local cancellation reduces the endpoint to


$$
a\eta_0=\frac{w_H^Tf_H}{3^{25}}\pmod3,
\qquad
w_H=\frac{M_H\upsilon_T-e_d}{3}.
\tag{1.9}
$$


Its proof has favorable parent review and a separate pending audit. Nothing here promotes it to an audited endpoint value.

The new column and polynomial identities below are proved directly in the displayed core objects. Their interpretation as $\eta_0$ uses (1.9), including its inherited endpoint hypotheses.

---

## 2. Arithmetic facts used at their established scope

For $N,q\ge0$, use the evaluated beta ratio


$$
\mathcal B(N,q)
=
\frac{4^N N!(N+q)!(2q)!}
{q!(2N+2q+1)!}.
\tag{2.1}
$$


If $j_e(q)$ is the least nonnegative residue of


$$
\frac{3^e-1}{2}-q\pmod{3^e},
$$


the established exact valuation is


$$
v_3\mathcal B(N,q)
=
-\sum_{e\ge1}
\mathbf 1_{\{N\bmod3^e\ge j_e(q)\}}.
\tag{2.2}
$$



All new value formulas below use the already proved factorial-unit producer, not a new factorial array. Explicitly, with


$$
U(n)=\frac{n!}{3^{v_3(n!)}},
$$


a weighted beta term is evaluated by counting (2.2), then computing


$$
4^N\frac{U(N)U(N+q)U(2q)}
{U(q)U(2N+2q+1)}
$$


at the remaining unit precision. Every inversion here is of a unit. Binomial coefficients are handled by the same valuation/unit separation.

The fixed $729$-position implementation remains coordinator-owned. No repeat of its derivation or existing finite receipt is proposed.

### A small new unit specialization

Let


$$
H=3^L,\qquad T=3^E,\qquad 1\le E<L,
\qquad r_T=\frac{T-1}{2}.
$$


Then


$$
\boxed{
v_3\mathcal B(H,r_T)=-E,\qquad
T\mathcal B(H,r_T)\equiv-1\pmod3.
}
\tag{2.3}
$$



The valuation follows from (2.2). To check the unit, reuse the established factorial-unit rule


$$
U(n)\equiv(-1)^{v_3(n!)+N_2(n)}\pmod3,
$$


where $N_2(n)$ counts ternary digits equal to $2$.

For the five factorial arguments


$$
H,\quad H+r_T,\quad T-1,\quad r_T,\quad 2H+T,
$$


the corresponding $N_2$-counts are


$$
0,\quad0,\quad E,\quad0,\quad1.
$$


Their signed difference is $E-1$, while the signed factorial-valuation difference is $-E$. The total sign is therefore $(-1)^{-1}=-1$, proving (2.3).

This specialization will be used twice, for two different actual forces.

---

## 3. Exact adaptation of the first HIGH column through the LOW space

### 3.1 A finite quotient, not a new middle column

Define


$$
b_i=\binom{D+i-1}{i},\qquad i\ge0,
$$


and the finite polynomial


$$
P_d(y)=\sum_{i=0}^{\nu}b_i\,y^{\nu-i}.
\tag{3.1}
$$


It is the polynomial quotient in the exact Euclidean division


$$
\boxed{
y^d=C_d(y)+x^DP_d(y),\qquad \deg C_d<D.
}
\tag{3.2}
$$


Equivalently,


$$
C_d(y)=\sum_{u=0}^{D-1}\binom du x^u.
\tag{3.3}
$$



The polynomial $P_d$ has degree $\nu$. It is an auxiliary quotient used to analyze the HIGH column $y^d$; it does **not** enlarge the middle interval $0,\ldots,\nu-1$.

Let $c_d$ denote the original $x$-basis LOW coordinate vector in (3.3), and set


$$
\alpha_d=\frac{G_c(U,x^DP_d)}3.
\tag{3.4}
$$


The exact identity (3.2) gives


$$
\mathcal X e_d=\mathcal Lc_d+\alpha_d.
\tag{3.5}
$$


Consequently,


$$
\boxed{
\mathcal S_H e_d
=
G_c(Y,x^DP_d)-3\mathcal X^TM_L\alpha_d.
}
\tag{3.6}
$$



This is the required joint source/operator adaptation. It has not replaced $\mathcal S_H$ by $E_Y$.

### 3.2 The new LOW force and its leading inverse image

Put


$$
T_0=729P=3^{h-26},
\qquad
r_0=\frac{T_0-1}{2},
\qquad
u_0=r_0-\nu.
\tag{3.7}
$$


The original inequalities imply


$$
0<u_0<D,\qquad D<T_0,\qquad r_0>D-1.
\tag{3.8}
$$



#### Proposition 3.1

In the original LOW coordinates,


$$
\boxed{
\alpha_d\in3^{25}\mathbb Z_3^D,\qquad
M_L\alpha_d\equiv3^{25}c_d\pmod{3^{26}}.
}
\tag{3.9}
$$



#### Proof

Temporarily use the monomial LOW row $y^u$, $0\le u<D$. Since $A+D=H$, its rational source is


$$
(\alpha_d)_{y,u}
=
-H\sum_{j=0}^{\nu}[y^j]P_d
\left\{
\beta\mathcal B(H,u+j)+3\mathcal B(H,u+j+1)
\right\},
\tag{3.10}
$$


up to a factorial term in $3^{h-1}$.

Here


$$
0\le u+j+1\le d<403P.
$$


For $N=H$ and these arguments, the $3H$ resonance is absent, and


$$
v_3\mathcal B(H,q)=-v_3(2q+1).
$$


Since


$$
2q+1<807P<3^{S+7},
$$


every term in (3.10) has valuation at least $25$.

At order $25$, only the $\beta$-part can contribute. Moreover, the only possible odd denominator divisible by $T_0$ in this range is $T_0$ itself. Thus


$$
u+j=r_0.
$$


Using (2.3),


$$
-\frac{H}{3^{25}}\mathcal B(H,r_0)
=-T_0\mathcal B(H,r_0)\equiv1\pmod3.
$$


Therefore


$$
\frac{(\alpha_d)_{y,u}}{3^{25}}
=
[y^{r_0-u}]P_d
=
\begin{cases}
b_{u-u_0},&u\ge u_0,\\
0,&u<u_0,
\end{cases}
\pmod3.
\tag{3.11}
$$



Let $C_y(Z)$ be the generating polynomial of this leading force. Then


$$
C_y(Z)\equiv Z^{u_0}(1-Z)^{-D}\pmod{Z^D}.
$$


The finite binomial change from $y^u$ to $x^u=(y-1)^u$ gives


$$
C_x(Z)
\equiv
\frac1{1+Z}C_y\!\left(\frac Z{1+Z}\right)
=
Z^{u_0}(1+Z)^{D-u_0-1}
\pmod{Z^D}.
\tag{3.12}
$$


The right side already has degree $D-1$, so no tail remains.

Now apply the established **finite LOW** inverse convention:


$$
(\overline{\mathcal L}^{-1}c)_u
=
[Z^u](1+Z)^{(H+1)/2}
\sum_{j=0}^{D-1}c_{D-1-j}Z^j.
$$


Reversing (3.12) through the actual length $D$ gives


$$
(1+Z)^{D-u_0-1}.
$$


Thus the solution polynomial is


$$
(1+Z)^{(H+1)/2+D-u_0-1}
=
(1+Z)^{d+(H-T_0)/2}
\pmod{Z^D}.
$$


Because


$$
\frac{H-T_0}{2}=T_0\frac{3^{25}-1}{2}
$$


is a multiple of $T_0$, and $D<T_0$,


$$
(1+Z)^{d+(H-T_0)/2}\equiv(1+Z)^d\pmod{3,Z^D}.
$$


This is exactly the LOW vector $c_d$ in (3.3). ∎

This is a new source-specific LOW calculation. It is not a repetition of the LOW48 solve.

---

## 4. The evaluated LOW matrix-return profile for this column

Define


$$
R_d=\overline{\mathcal X}^{\,T}\overline c_d
\in\mathbb F_3^{\{d,\ldots,m\}}.
\tag{4.1}
$$


For a HIGH row $s$, put


$$
j_s=\frac{H-1}{2}-s-d.
$$



#### Proposition 4.1

On the literal HIGH interval,


$$
\boxed{
(R_d)_s
=
\mathbf1_{\{s=m\}}
-
\begin{cases}
\displaystyle\binom{D+j_s-1}{j_s},&j_s\ge0,\\
0,&j_s<0,
\end{cases}
\pmod3.
}
\tag{4.2}
$$


In particular,


$$
\boxed{
(R_d)_d=0,\qquad (R_d)_{m-1}=0,\qquad (R_d)_m=1.
}
\tag{4.3}
$$


Also,


$$
\boxed{
(R_d)_s\ne0\ \Longrightarrow\ s\equiv122\pmod{243}.
}
\tag{4.4}
$$



#### Proof

The normalized pairing of a LOW polynomial with a HIGH row has no $3H$ pole. At its leading digit, only the $H$-pole contributes. Hence


$$
(R_d)_s
=
[y^{(H-1)/2-s}]x^AC_d(y).
$$


Using (3.2),


$$
x^AC_d=x^Ay^d-x^HP_d.
$$


Modulo $3$, $x^H=y^H-1$. The extraction index is below $H$, so


$$
(R_d)_s
=
[y^{j_s}]x^A+[y^{(H-1)/2-s}]P_d.
$$


Since


$$
\frac{H-1}{2}-s\ge\nu
$$


with equality only at $s=m$, the second term is precisely $\mathbf1_{\{s=m\}}$.

For $0\le j_s<H$,


$$
x^A=-(1-y)^{H-D}
\equiv-\frac{1-y^H}{(1-y)^D},
$$


giving (4.2).

Because $243\mid D$,


$$
(1-y)^{-D}\in\mathbb F_3[[y^{243}]].
$$


Thus its nonzero coefficients have index divisible by $243$. Since


$$
\frac{H-1}{2}-d\equiv122\pmod{243},
$$


the binomial part has the support in (4.4). The terminal $m$ has the same residue. The three edge values now follow. ∎

This profile is different from Turn 14’s $\Lambda$: its residue is $122$, not $121$, and its terminal coordinate is $1$, not $0$.

Combining (3.6), (3.9), and (4.1),


$$
\boxed{
\frac{\upsilon_T-\mathcal S_He_d}{3}
\equiv
\frac{\upsilon_T-G_c(Y,x^DP_d)}3
+
3^{25}R_d
\pmod{3^{26}}.
}
\tag{4.5}
$$



The LOW matrix-return correction in this column has now been evaluated at the precision required by the original certificate.

---

## 5. A compact complete value law for the raw column defect

Set


$$
B_0=243P=3^{h-27},\qquad r_B=\frac{B_0-1}{2},
\qquad r_H=\frac{H-1}{2}.
\tag{5.1}
$$


Since $\nu<B_0$, an interval of $\nu+1$ consecutive exponents contains at most one residue congruent to $r_B\pmod{B_0}$.

Write


$$
p_j=[y^j]P_d=
\begin{cases}
\displaystyle\binom{D+\nu-j-1}{\nu-j},&0\le j\le\nu,\\
0,&\text{otherwise}.
\end{cases}
\tag{5.2}
$$



For each $s\in[d,m]$ and $\epsilon=0,1$, define


$$
j_\epsilon(s)
=
(r_B-s-\epsilon)\bmod B_0,
\qquad 0\le j_\epsilon(s)<B_0.
\tag{5.3}
$$


If $j_\epsilon(s)>\nu$, the corresponding term below is zero. Otherwise put


$$
q_\epsilon(s)=s+j_\epsilon(s)+\epsilon.
$$



Define the actual integral raw defect


$$
\delta_{\rm raw}
=
\frac{\upsilon_T-G_c(Y,x^DP_d)}3.
\tag{5.4}
$$



### Theorem 5.1 — Complete raw column law

For $d\le s<m$,


$$
\boxed{
\begin{aligned}
(\delta_{\rm raw})_s\equiv{}&
-\frac H3\,\beta\,\mathcal B(H,s+\nu-1)
-H\,\mathcal B(H,s+\nu)\\
&+H\beta\,p_{j_0(s)}\mathcal B(H,q_0(s))\\
&+3H\,p_{j_1(s)}\mathcal B(H,q_1(s))
\pmod{3^{26}}.
\end{aligned}
}
\tag{5.5}
$$


A term involving $j_\epsilon(s)>\nu$ is omitted.

At the physical terminal,


$$
\boxed{
(\delta_{\rm raw})_m
\equiv
\frac{4D-H-72}{3}\,\mathcal U
\pmod{3^{26}},
}
\tag{5.6}
$$


where


$$
\mathcal U=3H\mathcal B(H,r_H)\pmod{3^{26}}.
\tag{5.7}
$$



Together with (4.5), these formulas give every coordinate of the **complete** column defect modulo $3^{26}$.

### Proof: physical support and precision-sized selection

All pairings in (5.4) retain the physical cutoff. For $P_d$, the largest rational-polynomial degree is


$$
H+m+\nu+1=\frac{3H-1}{2}+1<K_{\rm phys}.
$$


Thus the beta evaluation is valid without extending the functional.

The factorial part in (5.4) has valuation at least $h-2\ge61$, so it is invisible modulo $3^{26}$.

For $0\le q<r_H$, (2.2) specializes to


$$
v_3\mathcal B(H,q)=-v_3(2q+1).
\tag{5.8}
$$


If $B_0\nmid2q+1$, then


$$
v_3(2q+1)\le h-28.
$$


Consequently,


$$
H\mathcal B(H,q)\in3^{27}\mathbb Z_3,
\qquad
3H\mathcal B(H,q)\in3^{28}\mathbb Z_3.
\tag{5.9}
$$


Such monomials in $P_d$ do not contribute to (5.4) modulo $3^{26}$.

The sole congruence class that remains is


$$
q\equiv r_B\pmod{B_0}.
$$


Because $\nu<B_0$, each of the $\beta$ and $3y$ channels has at most one surviving monomial. This is exactly (5.3).

The only argument above $r_H$ is $q=r_H+1$, occurring at the extreme $3y$ corner. Formula (2.2) gives valuation $-1$ there, so its weighted contribution is much deeper than $3^{26}$. It is omitted only after this payment.

At $s=m$, the resonant contributions at $q=r_H$ must be combined **before** division. They are:

* $-H\mathcal B(H,r_H)$ from the terminal source;
* $H\beta\mathcal B(H,r_H)$ from $p_\nu=1$;
* $3HD\mathcal B(H,r_H)$ from $p_{\nu-1}=D$.

Their sum is


$$
H(\beta-1+3D)\mathcal B(H,r_H)
=
\frac{4D-H-72}{3}\mathcal U.
$$


Since


$$
v_3(4D-H-72)=2,
$$


the displayed division by $3$ is paid. This proves (5.5)–(5.6). ∎

### 5.1 A fixed value for the resonant unit

The constant in (5.7) stabilizes at a bounded input.

Let $H=3^L$. Directly from the product form of the beta ratio,


$$
3H\mathcal B(H,r_H)
=
2\prod_{j=1}^{H-1}\left(1+\frac{H}{2j}\right)^{-1}.
\tag{5.10}
$$


Pair $j$ with $H-j$. The paired factor is


$$
\left(1+\frac{H}{2j}\right)
\left(1+\frac{H}{2(H-j)}\right)
=
1+\frac{3H^2}{4j(H-j)}.
$$


If $v_3(j)=L-e$, this becomes


$$
1+\frac{3^{2e+1}}{4u(3^e-u)},
\qquad 3\nmid u.
\tag{5.11}
$$


For $e\ge13$, it is $1$ modulo $3^{26}$. Hence, for every present original $H$,


$$
\boxed{
\mathcal U
=
3^{13}\mathcal B\!\left(3^{12},\frac{3^{12}-1}{2}\right)
\pmod{3^{26}}.
}
\tag{5.12}
$$



This is a fixed rational unit, not an original-index table. In particular,


$$
\mathcal U\equiv2\pmod{27},
\qquad
\mathcal U\equiv\frac{16}{35}\equiv56\pmod{243}.
\tag{5.13}
$$



### 5.2 Both HIGH edge corrections

The complete column law gives


$$
\boxed{
(\delta_H)_d=0,\qquad
(\delta_H)_{m-1}=\mathcal U,\qquad
(\delta_H)_m=
\frac{4D-H-72}{3}\mathcal U+3^{25}
\pmod{3^{26}}.
}
\tag{5.14}
$$



For the first row, the possible $P_d$-arguments lie strictly between


$$
\frac{729P-1}{2}
\quad\text{and}\quad
\frac{1215P-1}{2},
$$


so neither channel meets the required residue class modulo $243P$. The two terminal-source terms are also too deep. Finally $(R_d)_d=0$.

At $s=m-1$, only the upper $3y$ resonance survives, giving $\mathcal U$, and $(R_d)_{m-1}=0$.

At $s=m$, the raw resonance is (5.6), and the actual matrix-return correction is $3^{25}(R_d)_m=3^{25}$.

Thus neither edge is supplied by an infinite Toeplitz extension.

### 5.3 Description size and value complexity

The complete law (4.5), (5.3), and (5.5) has a description of size $O(h)$:

* a fixed number of original integer parameters;
* two residue selections modulo the explicit power $B_0$;
* at most four beta-ratio evaluations;
* at most two negative-binomial evaluations;
* one Lucas product for $R_d$.

Given one original row $s$, the law uses at most $26$ factorial-unit calls, each with $O(h)$ ternary input length. Thus it requires at most $26(h+1)$ calls to the fixed block formula underlying the existing unit producer, plus $O(h)$ digit operations. No operation count is proportional to $m-d+1$.

This is a compact, complete **column-defect law**. It is not a compact inverse of $\mathcal S_H$, and it does not authorize enumeration of the HIGH interval.

---

## 6. One contracted matrix-return term is now evaluated

The new return profile also has a paid scalar consequence.

The previously established source grading gives


$$
f_H\bmod3\ \text{supported at }s\equiv13\pmod{27}.
$$


The actual leading finite HIGH inverse is reflection-graded by $13$ modulo $27$, so


$$
M_Hf_H\bmod3\ \text{is supported at }s\equiv0\pmod{27}.
$$


But $R_d$ is supported at $122\equiv14\pmod{27}$. Therefore


$$
\boxed{
3^{25}R_d^TM_Hf_H\equiv0\pmod{3^{26}}.
}
\tag{6.1}
$$



Since $w_H=M_H\delta_H$, symmetry gives


$$
\boxed{
w_H^Tf_H
\equiv
\delta_{\rm raw}^TM_Hf_H
\pmod{3^{26}}.
}
\tag{6.2}
$$



This evaluates a specific actual operator-return contribution. It does **not** remove the LOW matrix return from $M_H$. The matrix in (6.2) is still


$$
M_H=(E_Y-3\mathcal X^TM_L\mathcal X)^{-1}.
$$



---

## 7. A new actual finite HIGH directional lift

### 7.1 The complete leading defect

Let


$$
s_*=\frac{H/3+1}{2}-\nu.
\tag{7.1}
$$


The original inequalities imply


$$
d\le s_*<m-1.
$$



From the full column law,


$$
\boxed{
\delta_H\equiv e_{s_*}-e_{m-1}\pmod3.
}
\tag{7.2}
$$



Indeed, away from the physical resonance:

* the $P_d$-$\beta$ channel in (5.5) is divisible by $3$;
* its $3y$ channel is divisible by $9$;
* the second terminal-source term is divisible by $3$;
* the first terminal-source term can be a unit only when
  

$$
2(s+\nu-1)+1=H/3,
$$


  which is $s=s_*$.

Its value there is $1$ by (2.3). At $m-1$, the value is
$\mathcal U\equiv-1\pmod3$. At $m$, (5.14) is divisible by $3$.

### 7.2 Applying the real finite leading inverse

The supplied finite HIGH antidiagonal structure, specialized to the present $A+D=H$, gives


$$
(\overline E_Y)_{st}
=
[Z^{s+t-m-d}](1-Z)^A.
\tag{7.3}
$$


After the literal finite reversal, its inverse satisfies


$$
\boxed{
(\overline M_H e_t)_s
=
[Z^{m+d-s-t}](1-Z)^{-A}.
}
\tag{7.4}
$$


Only coefficients of degree at most $m-d<H$ occur. Hence, in precisely this finite range,


$$
(1-Z)^{-A}
=
\frac{(1-Z)^D}{(1-Z)^H}
\equiv\frac{(1-Z)^D}{1-Z^H}
\equiv(1-Z)^D\pmod3.
\tag{7.5}
$$


The last step is a paid finite projection: the first omitted term has degree $H$, beyond the entire finite inverse range.

Now


$$
m-s_*=\frac H3-1.
$$


Therefore


$$
\overline M_He_{s_*}
$$


is represented by


$$
y^{H/3+\nu-1}x^D.
$$


All of this polynomial’s support lies in the HIGH interval, because


$$
d\le \frac H3+\nu-1,
\qquad
\frac H3+d-1\le m.
\tag{7.6}
$$



For $e_{m-1}$, formula (7.4) uses only coefficients $0,1$ of $(1-Z)^D$. Since $3\mid D$,


$$
\overline M_He_{m-1}=e_{d+1}.
$$


Combining this with (7.2) proves


$$
\boxed{
w_H\equiv z^{(0)}\pmod3,
\quad
Z^{(0)}(y)=x^Dy^{H/3+\nu-1}-y^{d+1}.
}
\tag{7.7}
$$



The full polynomial is finite and lies inside the original HIGH space. No infinite inverse is substituted.

---

## 8. Contracting this computed direction with the complete source

The leading inverse action alone would not pay any higher-precision scalar. We now evaluate the whole contraction of the specific integral lift (7.7).

By (1.8) and the verified HIGH support,


$$
(z^{(0)})^Tf_H
=
\frac{
G_c(x^Dy^{a_*},x^Dp_0)
-
G_c(y^{d+1},x^Dp_0)
}{9},
\qquad a_*=\frac H3+\nu-1.
\tag{8.1}
$$



Every term of $\Omega_P$, every $\beta$-channel, and every $3y$-channel remains in this expression.

### Theorem 8.1 — The whole first-lift contraction vanishes

Uniformly on the original sufficiently large Range III family,


$$
\boxed{
(z^{(0)})^Tf_H\in3^{29}\mathbb Z_3.
}
\tag{8.2}
$$



### Proof

#### First polynomial in $Z^{(0)}$

For a term $(\Delta,b,c)\in\mathcal T$ and channel $\epsilon=0,1$, the beta arguments in


$$
G_c(x^Dy^{a_*},x^Dp_0)/9
$$


are


$$
N=H+D+t+\Delta
=H+268P+\Pi+\Delta,
$$




$$
q=\frac H3+(134+b)P+\chi-2+\epsilon.
\tag{8.3}
$$



The identity $D+t=268P+\Pi$ is essential here. It gives


$$
v_3(N)=S-1.
$$


For $1\le e\le S-1$, the beta indicator is therefore true exactly when $3^e\mid2q+1$.

For $\epsilon=0$,


$$
v_3(2q+1)=v_3(2\chi-3)=1;
$$


for $\epsilon=1$,


$$
v_3(2q+1)=v_3(2\chi-1)=0.
$$


Thus the first $S-1$ indicators contribute at most $1$ and $0$, respectively.

For $e=S,\ldots,S+6$, there are only seven possible indicators.

For $S+7\le e\le S+30$, the high parts $H,H/3$ disappear modulo $3^e$, and the residual sum in (8.3) is less than $536P$. This lies below


$$
\frac{3^{S+7}-1}{2},
$$


so all these indicators vanish.

At modulus $H$, the shift is near $H/3$, while the residual top is less than $271P$. The gap to $H/2$ is much larger than their sum, so that indicator also vanishes. At modulus $3H$, the same inequality shows that the $3H$ pole is absent.

Consequently the beta-indicator count is at most $8$ for $\epsilon=0$ and at most $7$ for $\epsilon=1$.

The rational functional divided by $9$ has scale $3^{h-2}=3^{S+30}$. Hence every $\beta$-term has valuation at least


$$
S+30-8=S+22\ge53,
$$


and every $3y$-term is deeper still.

All corresponding rational-polynomial degrees are below


$$
\frac{4H}{3}+536P<\frac{3H-1}{2}<K_{\rm phys}.
$$


Thus this estimate has not used an extension beyond the physical cutoff.

#### The first-HIGH-neighbor polynomial

For


$$
G_c(y^{d+1},x^Dp_0)/9,
$$


the beta arguments are


$$
N=H+t+\Delta,
\qquad
q=d+1+bP+\epsilon
=(402+b)P+3\chi+\epsilon.
\tag{8.4}
$$


Here $v_3(N)=5$.

For the first five indicators:

* the $\beta$-channel has $2q+1\equiv1\pmod{243}$, so none occurs;
* the $3y$-channel has $v_3(2q+1)=1$, so exactly one can occur.

Indicators above $S+6$ vanish by the same residual bound $N-H+q<536P$. Between levels $6$ and $S+6$ there are $S+1$ indicators. Hence


$$
C_{\beta}\le S+1,\qquad C_{3y}\le S+2.
$$


After the scale $3^{S+30}$, and including the extra factor $3$ of the $3y$-channel, both valuations are at least $29$.

Finally, the factorial contribution in (8.1) is in $3^{h-2}$, well beyond $3^{29}$.

The argument applies separately to all fourteen entries of (1.6), whose coefficients are integral. Summing them proves (8.2). ∎

This is an evaluated contracted term, not a support-only statement and not a consequence of choosing an arbitrary lift modulo $3$.

---

## 9. The precisely reduced remaining certificate

Define the actual integral vector


$$
w^{(1)}=\frac{w_H-z^{(0)}}3.
\tag{9.1}
$$


Theorem 8.1 gives


$$
w_H^Tf_H\equiv3(w^{(1)})^Tf_H\pmod{3^{26}}.
$$


Using the inherited endpoint divisibility,


$$
\boxed{
(w^{(1)})^Tf_H\in3^{24}\mathbb Z_3,
\qquad
a\eta_0=\frac{(w^{(1)})^Tf_H}{3^{24}}\pmod3.
}
\tag{9.2}
$$



Thus the remaining scalar precision is $25$, not $26$.

Set


$$
r_1=\frac{\upsilon_T-\mathcal S_H(e_d+3z^{(0)})}{9}.
\tag{9.3}
$$


This is integral by (7.7), and


$$
\mathcal S_Hw^{(1)}=r_1.
$$



The original requested certificate is now equivalent to constructing a finite, precision-sized $z^{(1)}$ such that


$$
\boxed{
\mathcal S_H(e_d+3z^{(0)}+9z^{(1)})-\upsilon_T
\in3^{27}\mathbb Z_3^{\{d,\ldots,m\}},
}
\tag{9.4}
$$


and evaluating


$$
\boxed{(z^{(1)})^Tf_H\pmod{3^{25}}.}
\tag{9.5}
$$


Then $z=z^{(0)}+3z^{(1)}$ is the original required $z$.

### 9.1 The next force also has an explicit column-adapted form

This next force need not be defined only by an unevaluated matrix product.

Let


$$
P_{d+1}(y)=\sum_{i=0}^{\nu+1}b_i\,y^{\nu+1-i},
\qquad
P_*(y)=y^{a_*}-P_{d+1}(y).
\tag{9.6}
$$


The same exact LOW remainder decomposition used in Section 3 gives


$$
\mathcal S_Hz^{(0)}
=
G_c(Y,x^DP_*)-3\mathcal X^TM_L\alpha_*,
$$


where


$$
\alpha_*=\frac{G_c(U,x^DP_*)}{3}.
$$


For both components of $P_*$,


$$
\alpha_*\in3^{25}\mathbb Z_3^D.
\tag{9.7}
$$


For $P_{d+1}$, this follows from $u+j\le d<403P$. For $y^{a_*}$, the shift is $H/3+u+\nu-1<H/2$; its residual odd denominator has valuation at most $S+6$. No $3H$ resonance occurs in either LOW force.

It follows that


$$
\boxed{
r_1\equiv
\frac{\delta_{\rm raw}-G_c(Y,x^DP_*)}{3}
+
3^{24}R_d
\pmod{3^{25}}.
}
\tag{9.8}
$$


The first numerator is divisible by $3$, as follows from the proved leading finite solve and the depth-$25$ and depth-$26$ LOW corrections.

The polynomial part $P_{d+1}$ still has length below $B_0$, so the same one-residue-per-channel rule evaluates it at the needed precision. The remaining term $y^{a_*}$ requires just its two beta channels. Its largest rational degree is below $11H/6<K_{\rm phys}$.

Thus the next forcing description is explicit and retains all returns. What remains unproved is a compact finite inverse action on this force through $3^{25}$, together with its contraction.

### 9.2 The exact obstruction

The obstruction is no longer the first LOW column return or the first HIGH directional digit. Those have been evaluated.

It is the higher finite directional return


$$
\boxed{
M_Hr_1\bmod3^{25}
}
$$


in the actual interval $d,\ldots,m$, or an equivalent method that evaluates its contraction with $f_H$ without constructing an original-length vector.

The matrix


$$
\mathcal S_H=E_Y-3\mathcal X^TM_L\mathcal X
$$


must remain. The results above do not justify replacing it by $E_Y$, a fixed small Gram matrix, or a projected infinite triangular inverse.

---

## 10. Bounded exact arithmetic: one optional fixed constant

No computation was performed.

No new $729$-table construction, old LOW48 check, leading-test audit, or original-index endpoint solve is requested.

The new symbolic proofs do not require a numerical receipt. If the coordinator wishes to instantiate the fixed edge constant $\mathcal U$ using the already owned unit producer, the bounded inputs are:



$$
M=3^{26},\qquad H_*=3^{12}=531441,
$$


and the five factorial-unit arguments


$$
531441,\quad797161,\quad531440,\quad265720,\quad1594323.
$$



The expected output is the unique residue $u_*\in[0,3^{26})$ satisfying


$$
\boxed{
u_*\,U(265720)U(1594323)
\equiv
4^{531441}U(531441)U(797161)U(531440)
\pmod{3^{26}}.
}
\tag{10.1}
$$


Additional expected checks are


$$
u_*\equiv2\pmod{27},
\qquad
u_*\equiv56\pmod{243}.
\tag{10.2}
$$



All denominator factors in (10.1) are units. The uniform identification $u_*=\mathcal U$ is proved by (5.10)–(5.12), not inferred from this finite calculation.

This is a fixed constant receipt with largest factorial-unit argument $1594323$. It is not an original-index source table or an endpoint computation.

---

## 11. Later layers and the actual producer remain unchanged

No endpoint has closed, so no first-$4$ mixed-prefix value or next physical-layer value is inferred.

The physical-$6$ assembly remains


$$
C_6=
C^{\rm mom}
-\bigl(e_{k-1}\eta^T+\eta e_{k-1}^T\bigr)
-R_4
\pmod3.
$$


The mixed-prefix digit retains


$$
P_{ui}=\frac{d_u^T\mathsf A^{-1}d_H{}_i}{3}\pmod3,
$$


and


$$
(C_H)_{ui}
=
-c_{P-1-u-i-\Pi}
+c_{P-1-u-i-2\Pi}
-2\,\mathbf1_{u=R,\ i=k-1}
-P_{ui}.
$$


No finite complementary inverse or upper $3y$ corner is removed.

The later direction remains


$$
B_6x=w_6,\qquad x\in3^{-1}\mathbb Z_3^{k-1},
$$


with the physical-$5$ complementary and kernel-pivot returns, higher endpoint adaptation, and source precision $34$ still required.

The diagonal divisions remain


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



The actual producer is still


$$
\boxed{Q_{\rm act}=Q_c+3^7\mathscr R.}
$$


It is distinct from the core analyzed here.

Retain


$$
F_{\rm fac}=(n-1)!,
$$




$$
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},
\qquad 0\le a,b<n,
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
\xi=
\frac{u^Tt_{\rm force}}{F_{\rm fac}^2-u^Tv}.
$$


The complete signed coefficients and endpoint remain


$$
[x^a](3^7\mathscr R)
=
-\frac{F_{\rm fac}}{a!}
\bigl((t_{\rm force})_a+\xi v_a\bigr),
\qquad 0\le a\le n-1,
$$




$$
\mathscr R(-1)=-\frac{\xi F_{\rm fac}^2}{3^7}.
$$



The complete forcing identity is unchanged:


$$
\boxed{
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
}
$$


The moment recurrence retains its full factorial term:


$$
\mu_{r+1}+\mu_r
=
\frac{3^h}{2r+1}
-\frac{3^h}{4}\bigl((2r+2)!+(2r)!\bigr),
\qquad0\le r\le2n-2,
$$


and its genuine resonant division at


$$
r_*=\frac{3^h-5}{2}.
$$



The factorial terms were discarded only in the explicitly paid local congruences above.

---

## 12. Actual contents, least clearer, final gcd, and whole error

The new local coordinate calculations do not determine or alter the actual integer column contents of the complete construction.

The least simultaneous clearer remains the actual $\ell_{\rm clr}$, not a convenient common multiple and not a power of $3$. Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the final gcd over **all primes**


$$
G=\gcd(|A_\ell|,|B_\ell|).
$$


For $B_\ell\ne0$, the actual primitive pair remains


$$
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{G},
\qquad
q=\frac{|B_\ell|}{G}.
$$


The whole evaluated error is


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
G\det H_{\rm complete}.
}
\tag{12.1}
$$



An irrationality proof still requires, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad
\det H_{\rm complete}\ne0,
$$


and


$$
\boxed{
\log G-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|
\longrightarrow+\infty.
}
\tag{12.2}
$$


These would make the nonzero whole errors tend to zero. A rational number with denominator $b$ cannot have nonzero integer linear errors of absolute value below $1/b$.

No assertion in (12.2) follows from the present column-defect law or from the vanishing of the first lifted contraction.

---

## 13. Evaluated and open scopes

| Object | Status |
|---|---|
| Earlier complete contracted LOW source cancellation | Reused at its stated local scope; separate audit remains pending |
| Earlier LOW48 result and leading HIGH terminal baseline | Not recalculated |
| Actual LOW adaptation of the HIGH column $e_d$ | Newly proved |
| $M_L\alpha_d\bmod3^{26}$ | Newly evaluated as $3^{25}c_d$ |
| Complete HIGH column defect $\delta_H\bmod3^{26}$ | Newly given by a compact complete value law |
| Both HIGH edge corrections | Explicitly evaluated in (5.14) |
| Physical $3H$ resonance | Retained, combined before division, and paid |
| The new residual LOW matrix-return contraction | Evaluated as zero modulo $3^{26}$, without deleting the matrix return from $M_H$ |
| First actual HIGH directional lift $z^{(0)}$ | Newly proved in the original finite interval |
| Whole contraction $(z^{(0)})^Tf_H$ | Newly proved to lie in $3^{29}$, with all fourteen source terms |
| Required precision-$27$ certificate | Not completed |
| $\eta_0$ | Open; remaining contraction is at modulus $3^{25}$ |
| $\eta_{k-1}$, first-$4$, actual physical $7$ | Open |
| Actual contents, least clearer, all-prime gcd, primitive denominator | Not evaluated |
| Same-index nonzero whole error and decay | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

---

## Conclusion

The new result is not an endpoint value. It is a complete, actual column reduction and a paid finite directional step:



$$
\boxed{
\delta_H
\equiv
\delta_{\rm raw}+3^{25}R_d
\pmod{3^{26}},
}
$$


with an explicit finite law for every term, including the physical terminal contribution


$$
3^{25}(R_d)_m=3^{25}.
$$



The real leading finite inverse sends this defect to the compact HIGH polynomial


$$
\boxed{
Z^{(0)}(y)=x^Dy^{H/3+\nu-1}-y^{d+1},
}
$$


and its whole contraction with the complete residual source is rigorously zero modulo $3^{26}$, in fact modulo $3^{29}$.

The exact remaining local bottleneck is now:

> Construct a precision-sized finite $z^{(1)}$ satisfying (9.4), with the true LOW-returned Schur matrix and both HIGH ends, and evaluate $(z^{(1)})^Tf_H\bmod3^{25}$.

The optional arithmetic is only the fixed resonant-unit receipt in Section 10. It has bounded inputs and no original-index endpoint solve.



$$
\boxed{
\text{The complete HIGH endpoint and the global rationality question for }e+\pi
\text{ remain open.}
}
$$


