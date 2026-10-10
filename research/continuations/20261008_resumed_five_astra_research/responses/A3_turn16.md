> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the finite HIGH reduction

## Executive verdict

**The scoped mathematical results of A1 Turns 14, 15, and 16 pass the independent proof audit below.** In particular, the new Turn 16 reduction is valid for the actual finite core matrices, with their literal LOW and HIGH boundaries, the physical terminal $Y_m$, the complete fourteen-channel source, and the LOW matrix return retained.

The principal audited conclusions are


$$
\delta_H
=\frac{\upsilon_T-\mathcal S_He_d}{3}
\equiv \delta_{\rm raw}+3^{25}R_d\pmod{3^{26}},
$$


and


$$
w_H\equiv z^{(0)}\pmod3,\qquad
Z^{(0)}(y)=x^Dy^{H/3+\nu-1}-y^{d+1},
$$


where the **specified integral polynomial** $Z^{(0)}$, not an arbitrary lift of its reduction modulo $3$, satisfies


$$
(z^{(0)})^Tf_H\in3^{29}\mathbb Z_3.
$$


Consequently the remaining endpoint calculation, conditional on the inherited endpoint identity, is


$$
a\eta_0=\frac{(w^{(1)})^Tf_H}{3^{24}}\pmod3,
\qquad
w^{(1)}=\frac{w_H-z^{(0)}}3,
$$


and requires the actual contraction


$$
(w^{(1)})^Tf_H\pmod{3^{25}}.
$$



The certificate established for $z^{(0)}$ has precision **$3^2$, not $3^{27}$**. No endpoint value follows.

I also supply a small further result: an explicit entry-producing version of the next residual, including the previously abbreviated $P_{d+1}$ corner payments and the $3H$-pole behavior of its other component. It proves, in particular,


$$
(r_1)_d\equiv0,\qquad
(r_1)_{m-2}\equiv-\mathcal U\pmod{3^{25}},
$$


without evaluating $\eta_0$. The remaining $3^{24}R_d$ term has zero contracted contribution modulo $3^{25}$, but remains part of the actual residual vector and does not disappear from the matrix problem.

No computation was performed. The closed $729$-position receipt and the old $244$-value check were not rerun. The fixed resonant unit $\mathcal U$ was not numerically instantiated.

The rationality or irrationality of $e+\pi$ remains unresolved.

---

## 1. Exact scope and original objects

Write $v_3$ for the $3$-adic valuation, with $v_3(0)=+\infty$. All matrix congruences below are entrywise.

### 1.1 Original index domain

The pointwise proofs concern sufficiently large tuples in exactly the supplied original family


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


subject to


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



The additional retained identities are


$$
P=3^{h-32},\quad P_0=243P,\quad N_0=243r,\quad D=P_0+N_0,
$$




$$
r\equiv2\pmod9,\qquad r\ \text{odd},
$$




$$
4^j=243(3^{26}-1)P-243r+1,
$$


and


$$
Q=27P,\qquad Q-N_0=2R,\qquad \chi=P-R.
$$


Thus


$$
N_0=25P+2\chi,\qquad D=268P+2\chi.
$$


The Range III restriction is


$$
\frac3{25}<\frac{\chi}{P}<\frac{31}{250}.
$$


Also


$$
v_3(\chi)=5,\qquad \chi/243\equiv1\pmod9.
$$



Set


$$
S=h-32,\qquad P=3^S,\qquad H=3^{S+31},
$$


and retain $h\ge63$, hence $S\ge31$. Put


$$
\Pi=P/3,\qquad t=\Pi-2\chi,\qquad k=3\chi-\Pi-1.
$$


Then $t>0$, $t$ is odd, $v_3(t)=5$, and $k\ge2$ after removal of a finite initial segment.

Useful consequences, proved directly from these inequalities, are


$$
D<269P,\qquad
\nu:=D/2-1=134P+\chi-1<135P,
$$




$$
d:=D+\nu=402P+3\chi-1<403P,
$$


and


$$
H>12D+10.
$$


Moreover,


$$
m+\nu=\frac{H-1}{2}=:r_H,
$$


and, modulo $243$,


$$
D\equiv0,\qquad \nu\equiv d\equiv-1,\qquad m\equiv122,\qquad r_H\equiv121.
$$



No proof below chooses $P$ and $\chi$ independently of the original indices.

### 1.2 Literal finite spaces

The bases remain


$$
U_u=x^u\quad(0\le u<D),\qquad x=y-1,
$$




$$
z_i^{\rm mid}=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_s=y^s\quad(d\le s\le m),
\qquad W=[U\ Y].
$$


The physical HIGH terminal is $Y_m$. The last middle polynomial is $y^{\nu-1}$; it is not $Y_m$.

The prefix boundaries remain


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


The endpoint unit is the original


$$
a=\overline B_{\ell,\tau-1}.
$$



### 1.3 Complete functional, columns, and source

The functional is


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{v=0}^{K_{\rm phys}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
\qquad \mathfrak f(y^a)=(2a)!,
$$


with


$$
K_{\rm phys}=2n-2=2H-2D+2.
$$


For the core,


$$
Q_c=(y+1)x^A(\beta+3y),\qquad
\beta=D-H-71,
$$




$$
G_c(f,g)=\mathcal M(Q_cfg),\qquad E_c=G_c(W,W),
$$


and the complete corrected column is


$$
F[p]=x^Dp-WE_c^{-1}G_c(W,x^Dp).
$$



The source is the literal polynomial


$$
p_0=\Omega_P(y)(1-y)^t,
$$


where


$$
\begin{aligned}
\Omega_P(y)={}&
(1-y)^{2P}\bigl(y^{122P}+3y^{41P}\bigr)\\
&+9(1+y^P+y^{2P})
\bigl(2y^{14P}+2y^{41P}+2y^{95P}-y^{131P}\bigr).
\end{aligned}
$$


Its fourteen terms are


$$
p_0=\sum_{(\Delta,b,c)\in\mathcal T}
c(1-y)^{t+\Delta}y^{bP},
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
0&131,132,133&-9.
\end{array}
$$


Every argument below includes both the $\beta$ and $3y$ channel for each of these fourteen terms.

Define


$$
g_T=G_c(W,x^Dy^{\nu-1}),\qquad
b_0=G_c(W,x^Dp_0).
$$


The exact block decomposition is


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
$$


Write


$$
g_T=3\binom{\alpha_T}{\upsilon_T},\qquad
b_0=3\binom{\alpha_0}{\upsilon_0},\qquad
f_H=\frac{\upsilon_0}{3}.
$$



### 1.4 Inherited hypotheses, kept separate

The following are not proved afresh by the present packet:

1. Infinitude of the specified Range III subwindow at the original indices.
2. The provenance of $\Omega_P$ as the complete prefix-corrected residual.
3. The earlier residual and bare-endpoint results giving
   

$$
\eta_0=a^{-1}\frac{g_T^TE_c^{-1}b_0}{3^{29}}\pmod3,
$$


   including the integrality of its quotient and the stated unit property of $a$.
4. The older rank-$b$, ten-return, and later physical-layer premises, at their separate retained scopes.

The finite core identities audited below are direct statements about the displayed objects. Their interpretation as a value of $\eta_0$ uses item 3. None supplies actual/core transport or a global primitive-error theorem.

---

## 2. Arithmetic and finite-matrix foundations

### 2.1 The evaluated beta ratio — PASS

For $N,q\ge0$,


$$
\mathcal B(N,q)
=\sum_{j=0}^{N}\frac{(-1)^j\binom Nj}{2(q+j)+1}
$$


equals


$$
\boxed{
\mathcal B(N,q)=
\frac{2^NN!}{\prod_{j=0}^{N}(2q+2j+1)}
=
\frac{4^NN!(N+q)!(2q)!}{q!(2N+2q+1)!}.
}
$$


For example, the sum is


$$
\int_0^1 z^{2q}(1-z^2)^N\,dz;
$$


the substitution $y=z^2$, followed by integrations by parts, gives the product formula.

Let $j_e(q)$ be the least nonnegative residue of


$$
\frac{3^e-1}{2}-q\pmod{3^e}.
$$


The odd denominator product contains


$$
\left\lfloor\frac N{3^e}\right\rfloor+
\mathbf1_{\{N\bmod3^e\ge j_e(q)\}}
$$


multiples of $3^e$, whereas $N!$ contains $\lfloor N/3^e\rfloor$. Therefore


$$
\boxed{
v_3\mathcal B(N,q)=
-\sum_{e\ge1}\mathbf1_{\{N\bmod3^e\ge j_e(q)\}}.
}
$$


This is an exact valuation identity, not merely a lower bound.

For later use, if $H=3^L$ and $0\le q<r_H$, then


$$
v_3\mathcal B(H,q)=-v_3(2q+1).
$$


At $q=r_H$, however,


$$
v_3\mathcal B(H,r_H)=-(L+1).
$$


That extra indicator is the $3H$ resonance. Treating this point as ordinary would lose a division by $3$.

### 2.2 Normalized block integrality and units — PASS

After cancellation of $y+1$, the largest LOW/HIGH rational degree is


$$
A+(D-1)+m+1=H+m<\frac{3H-1}{2}.
$$


Thus the $3H$-pole is absent from LOW/LOW and LOW/HIGH pairings. Division by $3$ is integral there.

Modulo $3$, the normalized LOW block is


$$
\overline{\mathcal L}_{uv}
=[Z^{D-1-u-v}](1+Z)^{-(H+1)/2}.
$$


For $u+v\ge D$, the coefficient at $r_H$ vanishes by


$$
x^H\equiv y^H-1\pmod3.
$$


For $u+v=D-1-j$, it is


$$
(-1)^j\binom{r_H+j}{j}.
$$


The antidiagonal entries are $1$, so $\mathcal L$ is a unit matrix.

For HIGH/HIGH pairings, the physical $3H$-pole gives


$$
\boxed{
(\overline E_Y)_{st}
=[Z^{s+t-m-d}](1-Z)^A.
}
$$


Entries with $s+t<m+d$ vanish and entries on $s+t=m+d$ equal $1$. Hence $E_Y\bmod3$, and therefore $\mathcal S_H\bmod3$, are nonsingular.

Thus


$$
M_L,M_H\in\operatorname{Mat}(\mathbb Z_3).
$$


The physical LOW inverse still carries the factor $3^{-1}$.

---

## 3. Audit of Turn 14

## 3.1 LOW digit and cutoff laws — PASS

For a LOW row $x^u$, a source term has beta arguments


$$
N=H+u+t+\Delta,\qquad q=bP+\epsilon,\qquad \epsilon\in\{0,1\}.
$$


Its rational contribution is


$$
(-1)^{H+u}3^h c
\left\{\beta\mathcal B(N,bP)+3\mathcal B(N,bP+1)\right\}.
$$



The literal bound $u\le D-1$ gives


$$
u+t+\Delta+bP+\epsilon\le401P+\Pi.
$$


For the $(2P,122,1)$ channel the stronger bound is $392P+\Pi$. Thus every term lies below the physical cutoff.

All beta indicators at levels $S+7,\ldots,S+31$ vanish: their thresholds exceed the residual degree bound. Indicators above $S+31$ also vanish because the entire odd denominator interval is below $3H$.

For $1\le e\le S$, put


$$
v(u)=(u+t)\bmod P,
$$




$$
C_e^{(\epsilon)}(u)
=\mathbf1_{\{v(u)\bmod3^e\ge(3^e-1)/2-\epsilon\}},
$$


and


$$
D_\epsilon(u)=\sum_{e=1}^{S}(1-C_e^{(\epsilon)}(u)).
$$


The first $S$ indicators contribute $S-D_\epsilon(u)$; at most six further indicators contribute. Consequently


$$
v_3\bigl(3^h\mathcal B(N,bP+\epsilon)\bigr)
\ge26+D_\epsilon(u).
$$


The $3y$ channel has one additional factor of $3$. Therefore


$$
\boxed{
v_3(b_{U,u})
\ge\min\{26+D_0(u),\,27+D_1(u)\}.
}
$$



The factorial part is in $3^h\mathbb Z_3$. Since $D_\epsilon\le S$, its depth is sufficient for this inequality.

The digit transitions are also correct. If $v_e$ are the ternary digits of $v(u)$, then


$$
C_1^{(0)}=\mathbf1_{\{v_0\ge1\}},\qquad C_1^{(1)}=1,
$$


and for $e\ge2$,


$$
C_e^{(\epsilon)}=
\begin{cases}
0,&v_{e-1}=0,\\
C_{e-1}^{(\epsilon)},&v_{e-1}=1,\\
1,&v_{e-1}=2.
\end{cases}
$$


Capping the two defect counts at $5$ and $4$ gives at most


$$
2\cdot2\cdot6\cdot5=120
$$


states for the sufficient zero test modulo $3^{31}$.

This is correctly stated as a support filter, not a complete value producer.

## 3.2 Order-$26$ force, including its unit and carries — PASS

Only the $\beta$ channel $(\Delta,b,c)=(2P,122,1)$ can contribute at order $26$. Put


$$
r=u+t+2P,\qquad q=122P.
$$


At modulus $243P$,


$$
j_{S+5}(q)=242P+\frac{P-1}{2}.
$$


Since $0<r<271P$, saturation of all indicators forces


$$
r=242P+v,\qquad \frac{P-1}{2}\le v<P.
$$


The six larger relevant indicators are then all $1$. The first $S$ are all $1$ exactly when every ternary digit of $v$ is $1$ or $2$.

The sign calculation is essential. For


$$
U_{\rm fac}(n)=\frac{n!}{3^{v_3(n!)}},
$$


one has


$$
U_{\rm fac}(n)\equiv(-1)^{v_3(n!)+N_2(n)}\pmod3.
$$


This follows by multiplying the nonmultiples of $3$ in complete blocks and iterating through $\lfloor n/3\rfloor,\lfloor n/9\rfloor,\ldots$.

Let $N_v=N_2(v)$ and


$$
w=2v+1-P.
$$


The carry $1$ propagates through every digit of $2v+1$, so the digits of $w$ are $0$ or $2$, with $N_2(w)=N_v$. The five factorial arguments have counts


$$
\begin{array}{c|c}
H+242P+v&5+N_v\\
H+364P+v&N_v\\
244P&0\\
122P&1\\
2H+729P+w&1+N_v.
\end{array}
$$


Together with valuation $-(S+6)$, this gives


$$
3^{S+6}\mathcal B(H+242P+v,122P)
\equiv(-1)^{S+1+N_v}\pmod3.
$$


Multiplication by the original sign $(-1)^{H+u}$ yields $-1$, because


$$
u=240P-t+v,\qquad
v\equiv S-N_v\pmod2,\qquad t\ \text{odd}.
$$



Hence


$$
\boxed{
\frac{b_{U,u}}{3^{26}}
=
-\mathbf1_{\{u=240P-t+v,\;v_e\in\{1,2\}\}}\pmod3.
}
$$


The support lies in $0\le u<D$, since its largest coordinate is $241P-t-1$ and


$$
D-(241P-t-1)=27P+\Pi+1>0.
$$



## 3.3 Finite reversed LOW inverse and all 48 coordinates — PASS

The leading-force polynomial is


$$
C_0(Z)=-Z^{240P-t+(P-1)/2}(1+Z)^{(P-1)/2}.
$$


The actual finite inverse rule is


$$
(\overline{\mathcal L}^{-1}c)_u
=[Z^u](1+Z)^{(H+1)/2}
\sum_{j=0}^{D-1}c_{D-1-j}Z^j.
$$


Thus it reverses the input through the literal length $D$.

Reversing $C_0$ gives


$$
-Z^{27P+\Pi}(1+Z)^{(P-1)/2}.
$$


The output is therefore


$$
-Z^{27P+\Pi}(1+Z)^{(H+P)/2}\pmod{Z^D}.
$$


Since


$$
(1+Z)^{(H+P)/2}
=(1+Z^P)^{(3^{31}+1)/2}
$$


in characteristic $3$, and


$$
\frac{3^{31}+1}{2}\equiv122\pmod{243},
$$


the literal cutoff


$$
D-(27P+\Pi)<241P
$$


removes every contribution from exponent $243$ or greater in $Z^P$. Hence


$$
\boxed{
\sum_{u=0}^{D-1}(\mathbf z_L)_uZ^u
=-Z^{27P+\Pi}(1+Z^P)^{122}.
}
$$



For explicit coverage of all 48 coordinates, let


$$
\mathcal B_{16}
=\{0,3,9,12,27,30,36,39,81,84,90,93,108,111,117,120\}.
$$


For each $b\in\mathcal B_{16}$, the three coordinates


$$
u=27P+\Pi+(b+a_0)P,\qquad a_0=0,1,2,
$$


have respective values


$$
2,\ 1,\ 2\quad\text{in }\mathbb F_3.
$$


These are exactly the 48 nonzero coordinates. Their largest index is


$$
149P+\Pi<D.
$$


This enumeration follows algebraically from


$$
122=(11112)_3;
$$


it is not a rerun of a finite coefficient receipt.

Since $M_L$ is integral,


$$
M_L\alpha_0=3^{25}\mathbf z_L+3^{26}\mathbf e_L
$$


for an actual integral remainder $\mathbf e_L$.

## 3.4 Three finite HIGH bands — PASS

The reduced LOW polynomial is


$$
U\mathbf z_L=-x^{27P+\Pi}y^{122P}.
$$


For


$$
\Lambda=\overline{\mathcal X}^{\,T}\mathbf z_L,
\qquad
\varrho_s=r_H-s-122P,
$$


the $H$-pole gives


$$
\Lambda_s=[y^{\varrho_s}](1-y)^{H-241P+t}.
$$


Throughout $d\le s\le m$,


$$
0\le\varrho_s<H.
$$


Thus, only in this finite coefficient range,


$$
\Lambda_s
=[y^{\varrho_s}]
\frac{(1-y)^t(1-y^P)^2}{1-y^{243P}}.
$$


Because $(1-y^P)^2=1+y^P+y^{2P}$ modulo $3$, this is exactly the three-band formula


$$
\Lambda_s=
\begin{cases}
(-1)^{r_s-qP}\binom{t}{r_s-qP},&
r_s\in qP+[0,t],\ q=0,1,2,\\
0,&\text{otherwise},
\end{cases}
$$


where $r_s$ is the least residue of $\varrho_s$ modulo $243P$.

At the physical terminal,


$$
r_m=12P+\chi-1,
$$


which exceeds $2P+t$ by $10P+k>0$, so $\Lambda_m=0$. Since $243\mid t$, nonzero entries require


$$
s\equiv121\pmod{243}.
$$



The result is the leading LOW-source return only. It does not evaluate $M_H\Lambda$ or the complete terminal.

## 3.5 Turn 14 payment and certificate status — PASS at the stated scope

The terminal LOW source obeys $g_{T,U}\in3^{26}$, hence


$$
\alpha_T,\alpha_0\in3^{25}.
$$


Exact block elimination gives


$$
g_T^TE_c^{-1}b_0
=
3\alpha_T^TM_L\alpha_0+
9\mathfrak t_H^TM_H\mathfrak b_H,
$$


where


$$
\mathfrak t_H=\upsilon_T-\mathcal X^TM_L\alpha_T,\qquad
\mathfrak b_H=\upsilon_0-\mathcal X^TM_L\alpha_0.
$$


The direct LOW term is in $3^{51}$.

For the sparse vector $\zeta^{(0)}=(3^{25}\mathbf z_L,0)^T$,


$$
g_T^T\zeta^{(0)}\in3^{51},
$$


but its LOW residual is proved only in $3^{27}$. The complete $3^{31}$ residual certificate does not follow. Turn 14 correctly leaves that obligation open.

---

## 4. Audit of Turn 15

## 4.1 Leading HIGH baseline — PASS

For $g_{T,Y_s}$, cancellation of $y+1$ leaves


$$
x^Hy^{\nu-1+s}(\beta+3y).
$$


After division by $3$, the $H$-pole has coefficient


$$
[y^{m+1-s}]x^H,
$$


which is an interior coefficient and vanishes modulo $3$.

The $3H$-pole is attained only by the $3y$ term at $s=m$. Its coefficient before the source division is $3$, so its normalized value is $1$. Therefore


$$
\upsilon_T\equiv e_m\pmod3.
$$


The finite antidiagonal formula gives


$$
M_He_m\equiv e_d\pmod3.
$$



A crucial distinction is respected here: the terminal $3y$ source cannot be assigned an additional factor of $3$ after normalization. Its physical division has already used that factor.

## 4.2 Actual mod-$27$ grading and finite reflection counts — PASS

Use temporarily the monomial LOW basis $y^u$. The change


$$
x^u=\sum_{v\le u}(-1)^{u-v}\binom uv y^v
$$


is integral and unimodular. If its matrix is $C$, then


$$
\mathcal L_x=C^T\mathcal L_yC,\qquad
\mathcal X_x=C^T\mathcal X_y,\qquad
\alpha_x=C^T\alpha_y.
$$


Consequently


$$
\mathcal X_x^T\mathcal L_x^{-1}\alpha_x
=\mathcal X_y^T\mathcal L_y^{-1}\alpha_y,
$$


and the HIGH Schur matrix is unchanged.

For $v_3(N)\ge5$,


$$
27\nmid i
\quad\Longrightarrow\quad
v_3\binom Ni\ge v_3(N)-v_3(i)\ge3.
$$


Thus $(1-y)^N\bmod27$ is supported at multiples of $27$. This applies to $A$ and $H+t+\Delta$.

Every pole visible modulo $27$, with the appropriate normalization for its block, has extraction index


$$
\frac{b-1}{2}\equiv13\pmod{27}.
$$


All factorial terms are too deep.

Writing $\rho=13$, the actual matrices over $\mathbb Z/27\mathbb Z$ therefore satisfy


$$
L_\epsilon(u,v)=0
\quad\text{unless }u+v+\epsilon\equiv\rho,
$$




$$
X_\epsilon(u,s)=0
\quad\text{unless }u+s+\epsilon\equiv\rho,
$$




$$
E_\epsilon(s,t)=0
\quad\text{unless }s+t+\epsilon\equiv\rho.
$$



The finite block-size conditions are valid:

- $D$ is a multiple of $27$;
- the literal HIGH reflection $s\mapsto m+d-s$ preserves $[d,m]$, and $m+d\equiv13\pmod{27}$.

No periodic enlargement is used.

Introduce


$$
L(\lambda)=\beta L_0+\lambda L_1,\quad
X(\lambda)=\beta X_0+\lambda X_1,\quad
E(\lambda)=\beta E_0+\lambda E_1,
$$




$$
S(\lambda)=E(\lambda)-3X(\lambda)^TL(\lambda)^{-1}X(\lambda).
$$


The constant matrices $L(0)$ and $S(0)$ are units. The inverse coefficient of $\lambda^j$ in $L(\lambda)^{-1}$ has reflection grade $\rho+j$; the coefficient in $S(\lambda)$ has grade $\rho-j$; and inversion gives


$$
M_H\equiv M_0+3M_1+9M_2\pmod{27},
$$




$$
(M_j)_{st}=0\quad\text{unless }s+t\equiv\rho+j.
$$



This calculation takes place in the actual residue ring. In particular, $M_0$ contains the LOW matrix return at $\lambda=0$. The argument does not choose lifts of a matrix known only modulo $3$.

## 4.3 Complete depth-$25$ source grading — PASS

For the monomial LOW source $\alpha_{0,y}$,


$$
N=H+t+\Delta,\qquad q=u+bP+\epsilon.
$$


The degree bound removes all indicators above $S+6$. For the first five levels, $N\bmod3^e=0$, so the indicator is true exactly when $3^e\mid2u+2\epsilon+1$. Hence


$$
v_3\bigl(H\mathcal B(N,q)\bigr)
\ge30-\min\{v_3(2u+2\epsilon+1),5\}.
$$


Visibility modulo $3^{28}$ forces residue $13$ for the $\beta$ source and residue $12$ for the $3y$ source. Thus


$$
\alpha_{0,y}\equiv3^{25}(a_{13}+3a_{12})\pmod{3^{28}}.
$$



For the terminal LOW source,


$$
N=H,\qquad q=u+\nu-1+\epsilon<403P.
$$


There is no $3H$ resonance and


$$
v_3\bigl(H\mathcal B(H,q)\bigr)
=h-1-v_3(2q+1)\ge25.
$$


Since $\nu-1\equiv-2\pmod{27}$, the corresponding source residues are $15$ and $14$:


$$
\alpha_{T,y}\equiv3^{25}(a_{15}+3a_{14})\pmod{3^{28}}.
$$



Applying the actual inverse grades gives


$$
\mathcal R_0:=\mathcal X^TM_L\alpha_0
\equiv3^{25}(R_{13}+3R_{12}+9R_{11})\pmod{3^{28}},
$$




$$
\mathcal R_T:=\mathcal X^TM_L\alpha_T
\equiv3^{25}(T_{15}+3T_{14}+9T_{13})\pmod{3^{28}}.
$$


These statements include higher matrix digits and carries.

The complete unreturned HIGH sources have the actual forms


$$
(\upsilon_0)_s\equiv
-H\sum_{\mathcal T}c
\left\{\beta\mathcal B(H+t+\Delta,s+bP)
+3\mathcal B(H+t+\Delta,s+bP+1)\right\}
\pmod{3^{28}},
$$




$$
(\upsilon_T)_s\equiv
-H\left\{
\beta\mathcal B(H,\nu-1+s)
+3\mathcal B(H,\nu+s)
\right\}\pmod{3^{28}}.
$$


The HIGH row belongs in $q$, not in the top $N$.

The source $p_0$ lies far enough below $\nu$ that the $3H$-pole is absent in $\upsilon_0$, and each unweighted $H$-pole coefficient vanishes modulo $3$. Consequently


$$
\upsilon_0\equiv3b_{13}+9b_{12}\pmod{27}.
$$


For $\upsilon_T$, the terminal resonance instead gives


$$
\upsilon_T\equiv t_{14}+3t_{15}\pmod{27},
\qquad t_{14}\equiv e_m\pmod3.
$$


Thus


$$
\operatorname{supp}(M_H\upsilon_T\bmod27)
\subseteq\{25,26,0,1\},
$$




$$
\operatorname{supp}(M_H\upsilon_0\bmod27)
\subseteq\{0,1\}.
$$



## 4.4 Both contracted LOW source returns — PASS

The three terms in the difference are


$$
-(M_H\upsilon_T)^T\mathcal R_0
-\mathcal R_T^T(M_H\upsilon_0)
+\mathcal R_T^TM_H\mathcal R_0.
$$



For the first term, the residue sets


$$
\{25,26,0,1\}\quad\text{and}\quad\{13,12,11\}
$$


are disjoint modulo $27$. After the depth-$25$ factor, the contraction is in $3^{28}$.

For the second term, the sets


$$
\{15,14,13\}\quad\text{and}\quad\{0,1\}
$$


are disjoint. It too is in $3^{28}$.

The last term is in $3^{50}$, since both LOW returns have depth $25$ and $M_H$ is integral. Therefore


$$
\boxed{
\mathfrak t_H^TM_H\mathfrak b_H
\equiv\upsilon_T^TM_H\upsilon_0\pmod{3^{28}}.
}
$$



This is the claimed cancellation of source contractions. It does **not** cancel


$$
3\mathcal X^TM_L\mathcal X
$$


inside $\mathcal S_H$.

For clarity, the separate direct LOW block term in the original bilinear expression is in $3^{51}$; the LOW-return/LOW-return product just considered is in $3^{50}$. Both payments are valid.

## 4.5 Complete zero first HIGH coordinate — PASS

At $s=d$, the LOW return is zero modulo $3^{28}$ because $d\equiv26\pmod{27}$, outside $\{13,12,11\}$.

For the raw source,


$$
N=H+t+\Delta,\qquad q=d+bP+\epsilon.
$$


The residual degree is below $536P$. The first five indicators vanish, since


$$
q\equiv-1+\epsilon\pmod{243}
$$


makes $2q+1\equiv-1$ or $1\pmod{243}$. At most $S+1$ further indicators remain, yielding


$$
(\upsilon_0)_d\in3^{30}.
$$


Hence


$$
(\mathfrak b_H)_d\equiv0\pmod{3^{28}}.
$$



## 4.6 The $729$-position value rule — PASS, independently of its finite receipt

Let $B=729=3^6$, $M=3^{28}$, and


$$
F_3(n)=\prod_{\substack{1\le i\le n\\3\nmid i}}i.
$$


The exact recursion


$$
U_{\rm fac}(n)=F_3(n)U_{\rm fac}(\lfloor n/3\rfloor)
$$


gives


$$
U_{\rm fac}(n)=\prod_{e\ge0}F_3(\lfloor n/3^e\rfloor).
$$



For $0\le R<B$, the stored residues are


$$
C_R=\prod_{\substack{1\le i\le R\\3\nmid i}}i,\qquad
H_{a,R}=\sum_{\substack{1\le i\le R\\3\nmid i}}i^{-a},
\quad a=1,2,3,4.
$$


Write $C=C_{728}$, $H_a=H_{a,728}$, and $n=QB+R$. Splitting into blocks gives exactly


$$
F_3(n)=C^QC_R
\prod_{b=0}^{Q-1}\prod_{3\nmid i,\ 1\le i<B}
\left(1+\frac{bB}{i}\right)
\prod_{3\nmid i,\ 1\le i\le R}
\left(1+\frac{QB}{i}\right).
$$



Every parenthesized factor lies in $1+3^6\mathbb Z_3$. In its logarithm, a term of degree $a$ has valuation at least


$$
6a-v_3(a).
$$


Terms with $a\ge5$ are therefore zero modulo $3^{28}$. Thus the logarithm is


$$
L(Q,R)=\sum_{a=1}^4\frac{(-1)^{a+1}B^a}{a}
\bigl(H_aS_a(Q)+Q^aH_{a,R}\bigr),
$$


where


$$
S_1=\frac{Q(Q-1)}2,\quad
S_2=\frac{Q(Q-1)(2Q-1)}6,
$$




$$
S_3=\left(\frac{Q(Q-1)}2\right)^2,
$$




$$
S_4=\frac{Q(Q-1)(2Q-1)(3Q^2-3Q-1)}{30}.
$$


Since $v_3(L)\ge6$,


$$
6j-v_3(j!)\ge28\qquad(j\ge5),
$$


and


$$
\boxed{
F_3(n)\equiv C^QC_R
\left(1+L+\frac{L^2}{2}+\frac{L^3}{6}+\frac{L^4}{24}\right)
\pmod{3^{28}}.
}
$$



All divisions are paid:

- $B^3/3=3^{17}$;
- $L^3/6$ and $L^4/24$ are integral;
- the $S_a(Q)$ are integer-valued;
- retaining $Q\bmod 2\cdot3^{29}$ pays the possible ternary denominator and retains parity.

The product of the units modulo $B$ is $-1$, so $\varrho=-C\in1+3^6\mathbb Z_3$. Therefore


$$
C^Q\equiv(-1)^Q\sum_{j=0}^4\binom Qj(\varrho-1)^j\pmod{3^{28}},
$$


since the omitted terms contain $3^{30}$.

This proves the universal formula. The fixed operation bound is also reasonable and checkable: only four power sums, four logarithmic terms, four exponential terms, and four binomial terms are used. A straight-line implementation is comfortably below the stated generous bound of $512$ fixed-precision arithmetic operations per block evaluation.

Each beta value is then produced by its exact valuation and


$$
4^N\frac{U_{\rm fac}(N)U_{\rm fac}(N+q)U_{\rm fac}(2q)}
{U_{\rm fac}(q)U_{\rm fac}(2N+2q+1)}.
$$


All inversions in this expression are of units. The per-entry complexity is $O(h)$, not proportional to the number of HIGH rows.

### Finite receipt scope

The supplied receipt reports:

- $1471$ comparisons for $0\le n\le1470$;
- $55$ further comparisons at the listed inputs, up to $59777$;
- no mismatches.

I accept this only as the supplied finite receipt. I have not rerun it or independently checked its hashes. It establishes neither the infinite formula nor the finite HIGH inverse contraction. The infinite formula is justified by the proof above.

---

## 5. Audit of Turn 16: actual first-column adaptation

## 5.1 Euclidean division and exact Schur identity — PASS

Let


$$
b_i=\binom{D+i-1}{i},\qquad
P_d(y)=\sum_{i=0}^{\nu}b_i y^{\nu-i}.
$$


Expansion at infinity gives


$$
\frac{y^d}{(y-1)^D}
=y^\nu(1-y^{-1})^{-D},
$$


whose polynomial part is $P_d$. Equivalently, expanding $y^d=(1+x)^d$ at $x=0$ gives the exact remainder


$$
C_d(y)=\sum_{u=0}^{D-1}\binom du x^u.
$$


Hence


$$
\boxed{y^d=C_d+x^DP_d,\qquad \deg C_d<D.}
$$



The quotient has degree $\nu$, but it is only an auxiliary quotient. The middle domain remains $0\le i<\nu$.

If $c_d$ is the original LOW coordinate vector of $C_d$, and


$$
\alpha_d=\frac{G_c(U,x^DP_d)}3,
$$


then


$$
\mathcal Xe_d=\mathcal Lc_d+\alpha_d.
$$


Substituting this into the literal Schur complement yields


$$
\boxed{
\mathcal S_He_d
=G_c(Y,x^DP_d)-3\mathcal X^TM_L\alpha_d.
}
$$


The LOW matrix return has not been removed.

## 5.2 The actual adapted LOW force — PASS

Put


$$
T_0=729P=3^{h-26},\qquad
r_0=\frac{T_0-1}{2},\qquad
u_0=r_0-\nu.
$$


The original inequalities give


$$
0<u_0<D<T_0,\qquad r_0>D-1.
$$



In the temporary monomial LOW basis,


$$
(\alpha_d)_{y,u}
=-H\sum_{j=0}^{\nu}[y^j]P_d
\left\{\beta\mathcal B(H,u+j)+3\mathcal B(H,u+j+1)\right\},
$$


up to a factorial term in $3^{h-1}$.

Here $q\le d<403P$, so


$$
v_3(2q+1)\le S+6.
$$


Thus $\alpha_d\in3^{25}$. At order $25$, only the $\beta$ channel can contribute, and the only possible odd denominator divisible by $T_0$ is $T_0$ itself.

For $T=3^E<H=3^L$,


$$
v_3\mathcal B(H,(T-1)/2)=-E,\qquad
T\mathcal B(H,(T-1)/2)\equiv-1\pmod3.
$$


The unit follows from the factorial-unit sign rule: the signed digit-count difference is $E-1$, and the valuation difference is $-E$.

It follows that


$$
\frac{(\alpha_d)_{y,u}}{3^{25}}
=[y^{r_0-u}]P_d
=
\begin{cases}
b_{u-u_0},&u\ge u_0,\\
0,&u<u_0,
\end{cases}
\pmod3.
$$


Its generating polynomial is


$$
Z^{u_0}(1-Z)^{-D}\pmod{Z^D}.
$$


The exact covector basis change gives


$$
C_x(Z)
=\frac1{1+Z}C_y\!\left(\frac Z{1+Z}\right)
=Z^{u_0}(1+Z)^{D-u_0-1}\pmod{Z^D}.
$$


The displayed polynomial already has degree $D-1$.

Applying the finite LOW inverse gives


$$
(1+Z)^{d+(H-T_0)/2}\pmod{Z^D}.
$$


Since $(H-T_0)/2$ is a multiple of $T_0$ and $D<T_0$, this is


$$
(1+Z)^d\pmod{3,Z^D}.
$$


Therefore


$$
\boxed{
M_L\alpha_d\equiv3^{25}c_d\pmod{3^{26}}.
}
$$



## 5.3 Complete $R_d$ profile and both ends — PASS

Define


$$
R_d=\overline{\mathcal X}^{\,T}\overline c_d,
\qquad j_s=r_H-s-d.
$$


At the normalized $H$-pole,


$$
(R_d)_s=[y^{r_H-s}]x^AC_d.
$$


Using $x^AC_d=x^Ay^d-x^HP_d$, and $x^H=y^H-1$ modulo $3$,


$$
(R_d)_s=[y^{j_s}]x^A+[y^{r_H-s}]P_d.
$$


The second term is $1$ only at $s=m$. For $0\le j_s<H$,


$$
x^A\equiv-\frac{1-y^H}{(1-y)^D},
$$


so


$$
\boxed{
(R_d)_s=
\mathbf1_{\{s=m\}}
-
\begin{cases}
\binom{D+j_s-1}{j_s},&j_s\ge0,\\
0,&j_s<0,
\end{cases}
\pmod3.
}
$$



This is a full value formula. The binomial value can be read from


$$
\binom{D+j_s-1}{j_s}\equiv
\prod_e\binom{(D+j_s-1)_e}{(j_s)_e}\pmod3.
$$


It is not merely a necessary support condition.

Because $243\mid D$, the negative-binomial series has support at multiples of $243$. Thus


$$
(R_d)_s\ne0\Longrightarrow s\equiv122\pmod{243}.
$$


At $s=d$, $j_s\equiv123\pmod{243}$, so the binomial coefficient vanishes. At $s=m-1$, $j_s=1-D<0$. At $s=m$, $j_s=-D<0$. Therefore


$$
\boxed{(R_d)_d=0,\qquad (R_d)_{m-1}=0,\qquad (R_d)_m=1.}
$$



Combining this with the exact adaptation proves


$$
\boxed{
\delta_H\equiv\delta_{\rm raw}+3^{25}R_d\pmod{3^{26}},
\qquad
\delta_{\rm raw}
=\frac{\upsilon_T-G_c(Y,x^DP_d)}3.
}
$$



---

## 6. Complete raw column law, resonance, and fixed unit

## 6.1 Ordinary one-residue sources — PASS

Put


$$
B_0=243P=3^{h-27},\qquad r_B=\frac{B_0-1}{2},
$$




$$
p_j=[y^j]P_d
=\binom{D+\nu-j-1}{\nu-j}\quad(0\le j\le\nu).
$$


For each $\epsilon=0,1$, let


$$
j_\epsilon(s)=(r_B-s-\epsilon)\bmod B_0.
$$


If $j_\epsilon(s)>\nu$, its term is absent; otherwise let


$$
q_\epsilon(s)=s+j_\epsilon(s)+\epsilon.
$$



For $q<r_H$, if $B_0\nmid2q+1$, then


$$
v_3(2q+1)\le h-28,
$$


and hence


$$
H\mathcal B(H,q)\in3^{27},\qquad
3H\mathcal B(H,q)\in3^{28}.
$$


Since $\nu<B_0$, at most one monomial survives this selection in each channel.

For $d\le s<m$, this yields exactly


$$
\boxed{
\begin{aligned}
(\delta_{\rm raw})_s\equiv{}&
-\frac H3\beta\mathcal B(H,s+\nu-1)
-H\mathcal B(H,s+\nu)\\
&+H\beta p_{j_0(s)}\mathcal B(H,q_0(s))
+3Hp_{j_1(s)}\mathcal B(H,q_1(s))
\pmod{3^{26}}.
\end{aligned}
}
$$


Every displayed term here is integral.

The maximum rational degree for $P_d$ is


$$
H+m+\nu+1=\frac{3H-1}{2}+1<K_{\rm phys}.
$$


The sole argument above $r_H$ is $q=r_H+1$. It has valuation $-1$, not the ordinary valuation $0$, but its weighted contribution is still far beyond the required precision. Its omission is therefore paid.

The factorial part of $\delta_{\rm raw}$ is in $3^{h-2}$, hence invisible modulo $3^{26}$.

## 6.2 Combined physical terminal before division — PASS

At $s=m$, the resonant pieces at $q=r_H$ are


$$
-H\mathcal B(H,r_H),
\qquad
H\beta\mathcal B(H,r_H),
\qquad
3HD\mathcal B(H,r_H).
$$


The first two pieces separately have valuation $-1$. They must not be reduced as integral terms before combination.

Their sum is


$$
H(\beta-1+3D)\mathcal B(H,r_H)
=\frac{4D-H-72}{3}\mathcal U,
$$


where


$$
\mathcal U=3H\mathcal B(H,r_H).
$$


Since $v_3(D)=5$ and $v_3(H)\ge62$,


$$
v_3(4D-H-72)=2.
$$


Thus the division by $3$ is paid, and


$$
\boxed{
(\delta_{\rm raw})_m
\equiv\frac{4D-H-72}{3}\mathcal U\pmod{3^{26}}.
}
$$



At $s=m-1$, the sole surviving resonance is the upper $3y$ contribution with coefficient $p_\nu=1$, giving


$$
(\delta_{\rm raw})_{m-1}\equiv\mathcal U\pmod{3^{26}}.
$$



At $s=d$, the possible $P_d$ arguments lie between


$$
\frac{729P-1}{2}\quad\text{and}\quad\frac{1215P-1}{2},
$$


without meeting the selected residue class modulo $243P$. The two terminal-source terms are also too deep. Hence


$$
(\delta_{\rm raw})_d\equiv0\pmod{3^{26}}.
$$



Adding the actual matrix return gives


$$
\boxed{
(\delta_H)_d\equiv0,\quad
(\delta_H)_{m-1}\equiv\mathcal U,\quad
(\delta_H)_m\equiv
\frac{4D-H-72}{3}\mathcal U+3^{25}
\pmod{3^{26}}.
}
$$


These are congruences, not assertions of exact equality in $\mathbb Z_3$.

## 6.3 Stabilization of $\mathcal U$ at $H_*=3^{12}$ — PASS

Let $H=3^L$. The product evaluation gives


$$
3H\mathcal B(H,r_H)
=
2\prod_{j=1}^{H-1}\left(1+\frac H{2j}\right)^{-1}.
$$


Pair $j$ with $H-j$:


$$
\left(1+\frac H{2j}\right)
\left(1+\frac H{2(H-j)}\right)
=
1+\frac{3H^2}{4j(H-j)}.
$$


If $j=3^{L-e}u$, $3\nmid u$, the paired factor becomes


$$
1+\frac{3^{2e+1}}{4u(3^e-u)}.
$$



For each $e$, its set of pairs depends only on $e$, not on $L$. For $e\ge13$, every factor is $1\pmod{3^{26}}$. Therefore, for all present $H$,


$$
\boxed{
\mathcal U\equiv
3^{13}\mathcal B\!\left(3^{12},\frac{3^{12}-1}{2}\right)
\pmod{3^{26}}.
}
$$



This is the required uniform stabilization proof. It is not inferred from a finite test.

The low checks follow symbolically: all paired factors are $1\pmod{27}$, so $\mathcal U\equiv2\pmod{27}$. Modulo $243$, only $e=1$ matters, giving


$$
\mathcal U\equiv2\left(1+\frac{27}{8}\right)^{-1}
=\frac{16}{35}\equiv56\pmod{243}.
$$


No full numerical residue of $\mathcal U$ is calculated here.

## 6.4 Description and value complexity — PASS at entry scope

The raw law uses at most four beta evaluations and two binomial evaluations. These require at most


$$
4\cdot5+2\cdot3=26
$$


factorial-unit calls. The remaining operations are residue selections and digit products. Each call uses $O(h)$ fixed-block evaluations.

This is a complete one-column value law with $O(h)$ per queried entry. It is not a compact inverse or a compact contraction over the full HIGH interval.

---

## 7. Leading finite HIGH inverse and whole first-lift contraction

## 7.1 Leading matrix-return contraction — PASS at one-digit precision

From Turn 15,


$$
f_H\bmod3\ \text{is supported at residue }13\pmod{27}.
$$


The leading finite inverse has reflection grade $13$, so


$$
M_Hf_H\bmod3\ \text{is supported at residue }0.
$$


The vector $R_d$ is supported at residue $122\equiv14\pmod{27}$. Hence


$$
R_d^TM_Hf_H\equiv0\pmod3.
$$


Exactly the claimed payment follows:


$$
\boxed{
3^{25}R_d^TM_Hf_H\equiv0\pmod{3^{26}}.
}
$$


No higher valuation of the unscaled contraction has been established.

Since $w_H=M_H\delta_H$,


$$
w_H^Tf_H\equiv\delta_{\rm raw}^TM_Hf_H\pmod{3^{26}}.
$$


The inverse remains the true LOW-returned $M_H$.

## 7.2 Leading defect — PASS

Let


$$
s_*=\frac{H/3+1}{2}-\nu.
$$


The original inequalities give $d\le s_*<m-1$.

Away from the physical resonance, the $P_d$-$\beta$ term is divisible by $3$, its $3y$ term by $9$, and the second terminal-source term by $3$. The first terminal-source term is a unit precisely when


$$
2(s+\nu-1)+1=H/3.
$$


Its unit is $1$ by the $T<H$ specialization above. The value at $m-1$ is $\mathcal U\equiv-1\pmod3$, and the value at $m$ is divisible by $3$. Thus


$$
\boxed{\delta_H\equiv e_{s_*}-e_{m-1}\pmod3.}
$$



## 7.3 Actual finite inverse orientation — PASS

Let $N_H=m-d+1$, and relabel HIGH coordinates by $i=s-d$. The leading matrix has entries


$$
c_{i+j-(N_H-1)},\qquad c_r=[Z^r](1-Z)^A.
$$


Multiplication on the right by the literal reversal matrix turns it into a lower triangular Toeplitz matrix. Inverting and reversing back gives


$$
\boxed{
(\overline M_He_t)_s
=[Z^{m+d-s-t}](1-Z)^{-A}.
}
$$


This is the HIGH convention; it differs from the LOW rule audited earlier.

Every coefficient used has degree at most $m-d<H$. Therefore


$$
(1-Z)^{-A}
=\frac{(1-Z)^D}{(1-Z)^H}
\equiv\frac{(1-Z)^D}{1-Z^H}
\equiv(1-Z)^D
$$


in this finite range only.

Since $m-s_*=H/3-1$, the inverse image of $e_{s_*}$ is represented by


$$
x^Dy^{H/3+\nu-1}.
$$


Its support is wholly HIGH:


$$
d\le H/3+\nu-1,\qquad
H/3+d-1\le m.
$$


For $e_{m-1}$, only coefficients $0,1$ are used. Because $3\mid D$,


$$
\overline M_He_{m-1}=e_{d+1}.
$$


Hence


$$
\boxed{
w_H\equiv z^{(0)}\pmod3,\qquad
Z^{(0)}=x^Dy^{H/3+\nu-1}-y^{d+1}.
}
$$



It follows, and follows only, that


$$
\boxed{
\mathcal S_H(e_d+3z^{(0)})-\upsilon_T\in3^2\mathbb Z_3^{[d,m]}.
}
$$


This is not a precision-$27$ certificate.

## 7.4 Full fourteen-channel contraction — PASS

The polynomial $Z^{(0)}$ is now used with all its integer coefficients:


$$
(z^{(0)})^Tf_H
=
\frac{
G_c(x^Dy^{a_*},x^Dp_0)
-G_c(y^{d+1},x^Dp_0)
}{9},
\qquad a_*=\frac H3+\nu-1.
$$


Reducing $Z^{(0)}$ coefficientwise modulo $3$ before this calculation would not justify the result.

### First component

For each $(\Delta,b,c)\in\mathcal T$ and $\epsilon=0,1$,


$$
N=H+D+t+\Delta=H+268P+\Pi+\Delta,
$$




$$
q=\frac H3+(134+b)P+\chi-2+\epsilon.
$$


The exact cancellation $D+t=268P+\Pi$ implies


$$
v_3(N)=S-1.
$$


For levels $1,\ldots,S-1$, the counts are therefore


$$
v_3(2q+1)=
\begin{cases}
1,&\epsilon=0,\\
0,&\epsilon=1,
\end{cases}
$$


because the residual odd numbers are congruent to $2\chi-3$ and $2\chi-1$, respectively.

There are seven possible indicators at levels $S,\ldots,S+6$. At levels $S+7,\ldots,S+30$, the high parts disappear and the residual sum is below $536P$, less than half the first such modulus. These indicators vanish.

At modulus $H$, the shift is near $H/3$, and the residual is far smaller than $H/6$; the indicator vanishes. At modulus $3H$, the same inequality shows that the pole is absent. Higher levels are absent by the degree bound.

Thus the total counts are at most $8$ and $7$. With scale


$$
3^{h-2}=3^{S+30},
$$


the $\beta$ channel has valuation at least


$$
S+30-8=S+22\ge53,
$$


and the $3y$ channel at least $S+24$.

The physical degree is below


$$
\frac{4H}{3}+536P<\frac{3H-1}{2}<K_{\rm phys}.
$$



### Second component

Here


$$
N=H+t+\Delta,\qquad
q=(402+b)P+3\chi+\epsilon.
$$


Now $v_3(N)=5$. The first five indicators contribute:

- zero for $\epsilon=0$, because $2q+1\equiv1\pmod{243}$;
- exactly one for $\epsilon=1$, because $v_3(2q+1)=1$.

The remaining possible levels $6,\ldots,S+6$ number $S+1$. All later indicators vanish because


$$
N-H+q<536P.
$$


Therefore


$$
C_\beta\le S+1,\qquad C_{3y}\le S+2.
$$


After including scale $3^{S+30}$ and the extra factor $3$ in the second channel, both valuations are at least $29$.

The factorial contribution after division by $9$ is in $3^{h-2}$, again sufficient.

These estimates hold separately for all fourteen source terms. Thus


$$
\boxed{(z^{(0)})^Tf_H\in3^{29}\mathbb Z_3.}
$$



---

## 8. The actual next residual and an additional explicit lemma

## 8.1 Reduction to the actual $w^{(1)}$ — PASS

Define


$$
w^{(1)}=\frac{w_H-z^{(0)}}3.
$$


It is integral by the finite leading solve. The inherited endpoint divisibility and the just-proved contraction imply


$$
(w^{(1)})^Tf_H\in3^{24},
$$


and, conditionally on the endpoint identity,


$$
\boxed{
a\eta_0=\frac{(w^{(1)})^Tf_H}{3^{24}}\pmod3.
}
$$



Set


$$
r_1=\frac{\upsilon_T-\mathcal S_H(e_d+3z^{(0)})}{9}.
$$


Then


$$
\mathcal S_Hw^{(1)}=r_1.
$$


A vector $z^{(1)}$ is sufficient precisely when


$$
\mathcal S_H(e_d+3z^{(0)}+9z^{(1)})-\upsilon_T\in3^{27},
$$


equivalently,


$$
\mathcal S_Hz^{(1)}-r_1\in3^{25}.
$$


The integrality of $M_H$ then gives


$$
z^{(1)}-w^{(1)}\in3^{25}.
$$



A chosen mod-$3$ lift is not such a vector.

## 8.2 Both true LOW adapted forces — PASS, with all ranges made explicit

Let


$$
P_{d+1}(y)=\sum_{i=0}^{\nu+1}b_i y^{\nu+1-i},
\qquad
P_*=y^{a_*}-P_{d+1}.
$$


The exact division


$$
y^{d+1}=C_{d+1}+x^DP_{d+1}
$$


gives


$$
Z^{(0)}=-C_{d+1}+x^DP_*.
$$


Thus


$$
\mathcal S_Hz^{(0)}
=G_c(Y,x^DP_*)-3\mathcal X^TM_L\alpha_*,
$$


where


$$
\alpha_*=
\frac{G_c(U,x^Dy^{a_*})}{3}
-\frac{G_c(U,x^DP_{d+1})}{3}.
$$



Neither LOW force is set to zero.

For the $P_{d+1}$ component, in monomial LOW coordinates,


$$
q=u+j+\epsilon\le d+1<403P.
$$


The $\beta$ maximum is $d$; the $3y$ maximum is $d+1$. This explicit distinction fills in the abbreviated range statement in Turn 16.

For the $y^{a_*}$ component,


$$
q=\frac H3+u+\nu-1+\epsilon<\frac H2.
$$


Its residual odd number has valuation at most $S+6$, since its positive residual is below $807P$, while the $H/3$ part has much higher valuation. Both LOW forces therefore lie in $3^{25}$.

Using the exact column adaptation,


$$
r_1=
\frac{\delta_{\rm raw}-G_c(Y,x^DP_*)}{3}
+\frac13\mathcal X^TM_L\alpha_d
+\mathcal X^TM_L\alpha_*.
$$


The last term is in $3^{25}$, and


$$
\frac13\mathcal X^TM_L\alpha_d
\equiv3^{24}R_d\pmod{3^{25}}.
$$


Therefore


$$
\boxed{
r_1\equiv
\frac{\delta_{\rm raw}-G_c(Y,x^DP_*)}{3}
+3^{24}R_d
\pmod{3^{25}}.
}
$$



The first numerator is divisible by $3$: this follows from the actual leading solve and the displayed depths of both LOW corrections. To compute its quotient modulo $3^{25}$, the numerator must be retained modulo $3^{26}$.

## 8.3 Added lemma: fully explicit entry law for the next residual

The preceding formula can be made value-producing without an unevaluated $P_{d+1}$-sum.

Define


$$
p_j^+=[y^j]P_{d+1}
=\binom{D+\nu-j}{\nu+1-j},
\qquad 0\le j\le\nu+1.
$$


Use the same residue selection $j_\epsilon(s)$ as before, now retaining it when $j_\epsilon(s)\le\nu+1$. Put


$$
\mathcal A_s=
-3H\left\{
\beta\mathcal B(H,s+a_*)+
3\mathcal B(H,s+a_*+1)
\right\},
$$


and


$$
\mathcal B_s^+=
-3H\left\{
\beta p^+_{j_0(s)}\mathcal B(H,s+j_0(s))
+
3p^+_{j_1(s)}\mathcal B(H,s+j_1(s)+1)
\right\},
$$


with absent selected terms interpreted as zero.

Then


$$
\boxed{
(r_1)_s\equiv
\frac{(\delta_{\rm raw})_s-\mathcal A_s+\mathcal B_s^+}{3}
+3^{24}(R_d)_s
\pmod{3^{25}}.
}
$$



### Proof of completeness and corner payment

For $P_{d+1}$, the maximum argument is now


$$
q=r_H+2,
$$


not merely $r_H+1$. Both exceptional arguments $r_H+1,r_H+2$ have


$$
v_3\mathcal B(H,q)=-1.
$$


Their $G_c$-weights have valuation at least $h-1$, and even after the outer division by $3$ remain far above $25$. For $q<r_H$, every unselected term has $G_c$-valuation at least $28$, also sufficient after that division.

For the $y^{a_*}$ component, the arguments satisfy


$$
0\le q\le r_H+\frac H3=\frac{5H/3-1}{2}.
$$


Throughout this interval, direct indicator counting gives the useful exact law


$$
\boxed{
v_3\mathcal B(H,q)
=-v_3(2q+1)-\mathbf1_{\{q\ge r_H\}}.
}
$$


The extra indicator is exactly the physical $3H$-pole. It must be retained for this component; unlike the earlier LOW force, its HIGH arguments can exceed $r_H$.

Its largest rational degree is


$$
H+q\le\frac{11H}{6}-\frac12<K_{\rm phys}.
$$


The largest factorial argument is at most $11H/3<3^{h+1}$. Thus the already proved universal unit producer applies with at most $h+1$ block evaluations per factorial-unit call.

This proves the displayed entry law. It uses at most eight beta evaluations and four binomial evaluations, including the existing raw-column law: at most $52$ factorial-unit calls per queried entry. It does not enumerate the HIGH interval.

### Explicit last-corner values for the $P_{d+1}$ component

Writing $b_2=D(D+1)/2$, the selected resonances give


$$
\mathcal B_{m-2}^+\equiv-3\mathcal U,
$$




$$
\mathcal B_{m-1}^+\equiv-(\beta+3D)\mathcal U,
$$




$$
\mathcal B_m^+\equiv-(\beta D+3b_2)\mathcal U
\pmod{3^{26}}.
$$


All neighboring arguments above $r_H$ have already been paid before division.

At $s=d$, every term in the residual numerator is sufficiently deep and $R_d(d)=0$, so


$$
(r_1)_d\equiv0\pmod{3^{25}}.
$$


At $s=m-2$,


$$
(\delta_{\rm raw})_{m-2}\equiv0,\qquad
\mathcal A_{m-2}\equiv0,\qquad
R_d(m-2)=0
$$


at the required precision, while $\mathcal B_{m-2}^+\equiv-3\mathcal U$. Hence


$$
\boxed{(r_1)_{m-2}\equiv-\mathcal U\pmod{3^{25}}.}
$$



These are new finite-residual consequences, not endpoint evaluations.

## 8.4 Added contracted-return consequence

The same leading residue separation used earlier gives


$$
3^{24}R_d^TM_Hf_H\equiv0\pmod{3^{25}}.
$$


Therefore


$$
(w^{(1)})^Tf_H
\equiv
\left(\frac{\delta_{\rm raw}-G_c(Y,x^DP_*)}{3}\right)^TM_Hf_H
\pmod{3^{25}}.
$$



This evaluates one additional contracted correction. It does not remove $R_d$ from the actual vector equation, and it does not replace $M_H$.

---

## 9. Verdict ledger

| Claim | Verdict | Exact scope |
|---|---|---|
| Turn 14 beta evaluation and digit/cutoff law | **PASS** | Every original LOW row; support bound through the stated precision |
| Turn 14 order-$26$ unit calculation | **PASS** | Includes the carry in $2v+1$ and the original sign |
| Turn 14 finite reversed LOW solve | **PASS** | All 48 original coordinates and signs; physical LOW division retained |
| Turn 14 three HIGH bands | **PASS** | Literal interval $d,\ldots,m$; terminal zero only for that leading channel |
| Turn 14 partial sparse certificate | **PASS** | Pairing paid; full residual certificate remains open |
| Turn 15 actual mod-$27$ grading | **PASS** | Temporary unimodular LOW basis; actual matrix digits and finite reflection counts |
| Turn 15 inverse $\lambda$-grades | **PASS** | Includes the LOW matrix return in the constant coefficient |
| Turn 15 complete source payments | **PASS** | Depth $25$, all fourteen terms, special terminal source normalization |
| Turn 15 both contracted vanishings | **PASS** | Modulo $3^{28}$; does not delete the matrix return |
| Turn 15 first HIGH source coordinate | **PASS** | Complete coordinate zero modulo $3^{28}$ |
| Turn 15 universal unit producer | **PASS** | General symbolic formula and paid divisions |
| Supplied $729$-receipt | **FINITE PASS AS SUPPLIED** | Only the stated 1471+55 comparisons; not rerun |
| Turn 16 Euclidean division and Schur adaptation | **PASS** | Auxiliary quotient only; middle interval unchanged |
| Turn 16 $M_L\alpha_d$ | **PASS** | $3^{25}c_d\pmod{3^{26}}$ in the original LOW coordinates |
| Turn 16 complete $R_d$ law | **PASS** | Includes $d,m-1,m$, with terminal value $1$ |
| Turn 16 raw column law and terminal combination | **PASS** | All ordinary channels and paid exceptional corners |
| Turn 16 fixed-unit stabilization | **PASS** | Modulo $3^{26}$, by paired products; no numerical instantiation |
| Turn 16 leading return contraction | **PASS** | $3^{25}R_d^TM_Hf_H=0\pmod{3^{26}}$ only |
| Turn 16 finite HIGH inverse orientation | **PASS** | Actual finite reversal and projection below degree $H$ |
| Turn 16 first certificate | **PASS** | Precision $3^2$ only |
| Turn 16 whole first-lift contraction | **PASS** | In $3^{29}$, using the specified integral polynomial and all fourteen channels |
| Turn 16 $w^{(1)}$, $r_1$, and residual formula | **PASS** | Actual vectors; both LOW adapted forces retained and paid |
| Precision-$27$ HIGH certificate | **OPEN** | Not supplied by any audited theorem |
| $\eta_0,\eta_{k-1}$ | **OPEN** | No endpoint evaluated |
| First $4$, complete physical $7$, source $34$, actual/core transport | **OPEN** | Separate retained obligations |
| All-prime contents, primitive denominator, whole error | **OPEN** | No consequence from the local audit |

No false scoped theorem was found that requires a replacement theorem. The abbreviated $P_{d+1}$ ranges needed explicit completion: its LOW $3y$ argument can reach $d+1$, and its HIGH $3y$ argument can reach $r_H+2$. Both are harmless only after the payments proved above.

---

## 10. Later layers, actual producer, and normalization remain unchanged

The audited core reduction does not authorize advancement to an unevaluated physical layer.

The retained physical-$6$ assembly is


$$
C_6=C^{\rm mom}
-\bigl(e_{k-1}\eta^T+\eta e_{k-1}^T\bigr)-R_4\pmod3.
$$


The first-$4$ cross retains


$$
P_{ui}=\frac{d_u^T\mathsf A^{-1}d_H{}_i}{3}\pmod3,
$$




$$
(C_H)_{ui}
=-c_{P-1-u-i-\Pi}+c_{P-1-u-i-2\Pi}
-2\mathbf1_{u=R,\ i=k-1}-P_{ui}.
$$


The upper $3y$ corner and actual complementary inverse are not removed.

The later directional solve remains


$$
B_6x=w_6,\qquad x\in3^{-1}\mathbb Z_3^{k-1}.
$$


The physical-$5$ complementary and kernel-pivot returns, higher endpoint adaptation, actual/core difference, and source precision $34$ remain required.

The diagonal payments remain


$$
\lambda_{\rm new}
=\lambda^{\rm pref}
-\frac13f_J^TB^{-1}f_J
-\frac19f_b^TA_b^{-1}f_b
\in3^{-2}\mathbb Z_3,
$$




$$
\lambda_4
=\lambda_{\rm new}-\frac1{3^4}f_C^TA_4^{-1}f_C
\in3^{-4}\mathbb Z_3.
$$



### 10.1 Complete actual producer and forcing

The actual producer is still


$$
Q_{\rm act}=Q_c+3^7\mathscr R.
$$


Retain


$$
F_{\rm fac}=(n-1)!,
\qquad
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},
$$




$$
\gamma_0=1,\quad\gamma_1=0,\quad
\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1},
$$




$$
h_{\rm vec}
=T_n^{-1}\left(\binom{n+a}{a}\gamma_{n+a}\right)_{a=0}^{n-1},
$$




$$
u_a=\frac{F_{\rm fac}(-2)^a}{a!},\qquad v=T_n^{-1}u,
$$




$$
b_{\rm force}=-n-66,
$$




$$
t_{\rm force}
=3nh_{\rm vec}+(b_{\rm force}+6)e_{n-1}
+\frac{2b_{\rm force}}{n-1}e_{n-2},
$$




$$
\xi=\frac{u^Tt_{\rm force}}{F_{\rm fac}^2-u^Tv}.
$$


The complete signed correction remains


$$
[x^a](3^7\mathscr R)
=-\frac{F_{\rm fac}}{a!}\bigl((t_{\rm force})_a+\xi v_a\bigr),
\quad0\le a\le n-1,
$$




$$
\mathscr R(-1)=-\frac{\xi F_{\rm fac}^2}{3^7}.
$$



The full forcing is


$$
J^T\varepsilon+\omega
=-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$


Neither forcing term is discarded.

The moment recurrence retains the factorial part:


$$
\mu_{r+1}+\mu_r
=\frac{3^h}{2r+1}
-\frac{3^h}{4}\bigl((2r+2)!+(2r)!\bigr),
\qquad0\le r\le2n-2,
$$


including its genuine resonant division at


$$
r_*=\frac{3^h-5}{2}.
$$



The factorial terms were omitted only in the explicitly paid local congruences. They remain in the full construction.

### 10.2 Actual contents, least clearer, all-prime gcd, and whole error

The temporary LOW basis changes used for proofs do not redefine the complete integer columns, their actual contents, or their least simultaneous clearer $\ell_{\rm clr}$.

Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the final gcd over all primes


$$
G=\gcd(|A_\ell|,|B_\ell|).
$$


For $B_\ell\ne0$, the actual primitive numerator and denominator are


$$
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{G},
\qquad q=\frac{|B_\ell|}{G}.
$$


The whole evaluated error remains


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{G}
\det H_{\rm complete}.
}
$$



An irrationality proof still requires, at the same infinite original indices,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\log G-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|\longrightarrow+\infty.
$$


These conditions would force the nonzero whole errors to tend to zero. If $e+\pi=a/b$ were rational, every nonzero integer linear error $q(e+\pi)-p$ would have absolute value at least $1/b$, giving the contradiction.

No local ternary statement proved here establishes these conditions. In particular, a $3$-adic valuation cannot replace the final all-prime gcd or the actual primitive denominator.

---

## 11. Exact remaining bottleneck and computation status

### 11.1 Remaining local mathematical obligation

The unpaid problem is now specific:

> Construct, without enumerating the original HIGH interval, a precision-sized description of an integral vector $z^{(1)}$ supported on the literal interval $d\le s\le m$, prove
> 

$$
> \mathcal S_Hz^{(1)}-r_1\in3^{25}\mathbb Z_3^{[d,m]},
>
$$


> with
> 

$$
> \mathcal S_H=E_Y-3\mathcal X^TM_L\mathcal X,
>
$$


> and evaluate
> 

$$
> (z^{(1)})^Tf_H\pmod{3^{25}}.
>
$$



The residual $r_1$ now has a complete entry law, including all physical poles and corners. Entry production does not solve this joint finite inverse-and-contraction problem.

The actual obstruction is the higher finite Schur response. It is not resolved by:

- the mod-$3$ inverse orientation;
- the modulus-$9$ first certificate;
- the $3^{29}$ vanishing of one chosen integral direction;
- a named original-length inverse vector;
- an infinite Toeplitz surrogate;
- the one-entry factorial-unit algorithm;
- or the finite $729$-receipt.

The added explicit residual lemma is a concrete next input for proving that higher response. It does not itself pay it.

### 11.2 Bounded arithmetic needed now

**No new bounded exact-arithmetic calculation is indispensable for this audit.** All audited claims and the added residual lemma have symbolic proofs.

Accordingly:

- no new $729$-table construction is proposed;
- no repeat of the $1471+55$ comparisons is proposed;
- no old $244$-value check is proposed;
- no numerical instantiation of $\mathcal U$ is proposed;
- no original-index HIGH enumeration or original factorial matrix is proposed.

A future endpoint calculation would first need a proved compact certificate mechanism with a verifiable residual and contraction output. Such a mechanism has not yet been established.

---

## Conclusion

The new Turn 16 finite HIGH reduction passes independent audit. Its important content is not an endpoint value but a rigorously paid reduction:


$$
\boxed{
\delta_H\equiv\delta_{\rm raw}+3^{25}R_d\pmod{3^{26}},
}
$$


with the physical terminal matrix-return term retained, followed by the actual finite leading direction


$$
\boxed{
Z^{(0)}=x^Dy^{H/3+\nu-1}-y^{d+1}
}
$$


whose whole fourteen-channel contraction lies in $3^{29}$.

The prerequisite Turn 14 digit laws and finite LOW solve, and Turn 15 actual mod-$27$ cancellation and universal value rule, also pass at their stated scopes. The supplied arithmetic receipt remains finite evidence only.

The further result proved here makes the next residual explicitly value-producing, pays its additional corners, and gives two of its finite boundary values. The exact unresolved local task is still the actual precision-$25$ finite Schur inverse/test contraction.

Neither endpoint, the first-$4$ return, complete physical $7$, actual source-$34$ transport, actual contents, least simultaneous clearer, all-prime gcd, nor the same-index primitive whole-error criterion has been silently passed.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi\text{ is obtained.}}
$$


