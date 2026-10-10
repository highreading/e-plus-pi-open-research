> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1, Turn 15 — Cancellation of both LOW source returns in the complete HIGH contraction

## Abstract and proof status

The rationality or irrationality of $e+\pi$ remains unresolved. Neither $\eta _0$ nor $\eta _{k-1}$ is evaluated in this report.

There is, however, a new complete inverse-return result at the precision required for $\eta _0$. Write


$$
\mathcal R_T=\mathcal X^TM_L\alpha_T,\qquad
\mathcal R_0=\mathcal X^TM_L\alpha_0,
$$


so that the two complete HIGH sources are


$$
\mathfrak t_H=\upsilon_T-\mathcal R_T,\qquad
\mathfrak b_H=\upsilon_0-\mathcal R_0.
$$


For the actual finite HIGH Schur inverse $M_H$, I prove


$$
\boxed{
\mathfrak t_H^TM_H\mathfrak b_H
\equiv
\upsilon_T^TM_H\upsilon_0
\pmod{3^{28}}.
}
\tag{A}
$$



This is a cancellation of the **contracted contributions of both LOW-returned sources**. It is not permission to delete the LOW return from the Schur matrix:


$$
M_H=
\left(E_Y-3\mathcal X^TM_L\mathcal X\right)^{-1}
$$


remains unchanged.

The proof uses the actual matrices modulo $27$, not merely their reductions modulo $3$. It therefore includes the effects of their next two digits and all carries from integral lifts. No evaluation of the separate LOW jets $z_1,z_2$ is needed for this particular contraction.

A second consequence strengthens the supplied leading calculation:


$$
\boxed{
(\mathfrak b_H)_d\equiv0\pmod{3^{28}}.
}
\tag{B}
$$


Thus the entire source coordinate paired with the leading test $e_d$, not just its leading LOW-return digit, vanishes at the target precision. The higher test still remains.

I also give a deterministic value-producing formula for every entry of the two unreturned HIGH sources, through modulus $3^{28}$. It retains:

- all fourteen terms of $\Omega_P$;
- both the $\beta$ and $3y$ contributions;
- the actual HIGH shift $q=s+aP+\epsilon$;
- the $3H$ resonance at the physical terminal;
- the physical cutoff;
- the factorial payment.

Its universal arithmetic table has $729$ positions, rather than a number of positions proportional to $P$ or $H$. This is a complete **entry producer**, not a producer of the finite HIGH inverse contraction. No endpoint experiment based on enumerating the HIGH interval is proposed.

The exact remaining local digit can now be written


$$
\boxed{
a\eta_0
=
\frac{w_H^Tf_H}{3^{25}}\pmod3,
\qquad
f_H=\frac{\upsilon_0}{3},\qquad
w_H=\frac{M_H\upsilon_T-e_d}{3}.
}
\tag{C}
$$


The new result removes the separate LOW source jets from this obligation and lowers the required HIGH inverse precision to $3^{27}$. It does not evaluate the remaining directional contraction.

---

## 1. Original domain, finite boundaries, and the paid target

### 1.1 The unchanged original family

All assertions below are pointwise for sufficiently large tuples in exactly the original domain


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



Retain


$$
P=3^{h-32},\qquad P_0=243P=3^{h-27},\qquad N_0=243r,
$$




$$
D=P_0+N_0,\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$


and


$$
4^j=243(3^{26}-1)P-243r+1.
$$


Also retain


$$
Q=27P,\qquad Q-N_0=2R,\qquad \chi=P-R,
$$


so


$$
N_0=25P+2\chi,\qquad D=268P+2\chi.
$$



The Range III restriction is unchanged:


$$
\boxed{\frac3{25}<\frac{\chi}{P}<\frac{31}{250}.}
\tag{1.1}
$$


The previously certified infinitude is reused only at this original-index scope. No argument below chooses $P$ and $\chi$ independently.

Set


$$
\Pi=P/3,\qquad t=\Pi-2\chi,\qquad
k=3\chi-\Pi-1,\qquad L_*=\frac{P-1}{2}.
$$


We retain


$$
v_3(\chi)=5,\qquad \chi/243\equiv1\pmod9.
$$


Consequently $t>0$, $t$ is odd, and $v_3(t)=5$. After removing a finite initial segment, $k\ge2$.

For the local proofs write


$$
S=h-32,\qquad P=3^S,\qquad H=3^{S+31},
$$


and take $h\ge63$, hence $S\ge31$.

### 1.2 The literal finite spaces

The original spaces are


$$
U_u=x^u,\qquad 0\le u<D,\qquad x=y-1,
$$




$$
z_i^{\rm mid}=x^Dy^i,\qquad 0\le i<\nu,\qquad
\nu=D/2-1,
$$




$$
Y_s=y^s,\qquad d\le s\le m,\qquad
d=D+\nu=\frac{3D}{2}-1,
$$


and


$$
W=[U\ Y].
$$



The physical HIGH terminal is $Y_m$. The last middle column is instead associated with $y^{\nu-1}$. These are not interchanged.

The prefix and tail boundaries also remain


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


The unit


$$
a=\overline B_{\ell,\tau-1}
$$


is the true unit of the normalized finite $J$-border.

### 1.3 Complete functional and corrected columns

The complete functional is


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^a)=(2a)!.
\tag{1.2}
$$


Its physical cutoff is


$$
K_{\rm phys}=2n-2=2H-2D+2.
$$



For the current complete core,


$$
Q_c=(y+1)x^A(\beta+3y),\qquad
\beta=-71-A=D-H-71,
$$




$$
G_c(f,g)=\mathcal M(Q_cfg),\qquad E_c=G_c(W,W),
$$




$$
F[p]=x^Dp-WE_c^{-1}G_c(W,x^Dp).
\tag{1.3}
$$



Retain the already derived, prefix-corrected residual polynomial


$$
\begin{aligned}
\Omega_P(y)={}&
(1-y)^{2P}\bigl(y^{122P}+3y^{41P}\bigr)\\
&+9(1+y^P+y^{2P})
\bigl(2y^{14P}+2y^{41P}+2y^{95P}-y^{131P}\bigr).
\end{aligned}
\tag{1.4}
$$


Put


$$
p_0=\Omega_P(y)(1-y)^t,
$$




$$
g_T=G_c(W,x^Dy^{\nu-1}),\qquad
b_0=G_c(W,x^Dp_0).
\tag{1.5}
$$



I reuse the complete residual identity and the endpoint bare-source vanishing from Turn 13, with exactly their stated hypotheses. They give


$$
\boxed{
\eta_0
=
a^{-1}\frac{g_T^TE_c^{-1}b_0}{3^{29}}\pmod3.
}
\tag{1.6}
$$


This is a coordinate of the complete **core** block, not an imported terminal value of the different actual producer.

### 1.4 LOW/HIGH payments

The finite block decomposition is


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


The established finite unit results imply


$$
M_L,M_H\in\operatorname{Mat}(\mathbb Z_3).
$$


The physical LOW inverse still costs $3^{-1}$.

Write


$$
g_T=3\binom{\alpha_T}{\upsilon_T},
\qquad
b_0=3\binom{\alpha_0}{\upsilon_0}.
$$


The LOW forces satisfy


$$
\alpha_T,\alpha_0\in3^{25}\mathbb Z_3^D.
$$


With


$$
\mathfrak t_H=\upsilon_T-\mathcal X^TM_L\alpha_T,
\qquad
\mathfrak b_H=\upsilon_0-\mathcal X^TM_L\alpha_0,
$$


exact block elimination gives


$$
g_T^TE_c^{-1}b_0
=
3\alpha_T^TM_L\alpha_0
+
9\mathfrak t_H^TM_H\mathfrak b_H.
\tag{1.8}
$$


The first summand is in $3^{51}\mathbb Z_3$. Thus


$$
\boxed{
a\eta_0
=
\frac{\mathfrak t_H^TM_H\mathfrak b_H}{3^{27}}\pmod3.
}
\tag{1.9}
$$


The numerator is divisible by $3^{27}$. Its value modulo $3^{28}$ is the outstanding target.

---

## 2. Audit of the supplied leading HIGH baseline

Put


$$
r_H=\frac{H-1}{2}.
$$


The exact identities


$$
m+\nu=r_H,\qquad A+D=H
$$


give, after cancelling $y+1$, the rational polynomial for $g_{T,Y_s}$:


$$
x^Hy^{\nu-1+s}(\beta+3y).
$$



After the source division by $3$, the pole with odd denominator $H$ has weight $1$. Its $\beta$-coefficient is


$$
[y^{r_H-\nu+1-s}]x^H
=
[y^{m+1-s}]x^H.
$$


For $d\le s\le m$, this is an interior coefficient of $x^H$. Since


$$
x^H\equiv y^H-1\pmod3,
$$


it vanishes modulo $3$. The $3y$-part at the $H$-pole has an additional factor $3$.

The pole $3H$ can be reached only by the $3y$-part at $s=m$. Its complete coefficient is $3$, so after the displayed source division it contributes $1$. Smaller poles have extra powers of $3$, and the factorial term is paid. Hence


$$
\upsilon_T\equiv e_m\pmod3.
$$


The LOW correction is in $3^{25}$, so


$$
\mathfrak t_H\equiv e_m\pmod3.
$$



For the HIGH column indexed by $d$, the finite antidiagonal theorem gives


$$
E_Y(s,d)\equiv0\pmod3\quad(s<m),\qquad
E_Y(m,d)\equiv1\pmod3.
$$


The Schur return in $\mathcal S_H$ has the explicit factor $3$. Therefore


$$
M_He_m\equiv e_d\pmod3,
\qquad
\mathfrak t_H^TM_H\equiv e_d^T\pmod3.
\tag{2.1}
$$



Finally,


$$
d\equiv-1\pmod{243},
$$


whereas Turn 14’s leading LOW-return profile $\Lambda$ is supported at
$s\equiv121\pmod{243}$. Thus $\Lambda_d=0$.

The supplied baseline is correct. Its scope is only the leading digit. The proof below does not replace the full test by $e_d$.

---

## 3. Complete HIGH sources with the original shift and cutoff

### 3.1 The fourteen terms

Use the following literal expansion of the already established polynomial:


$$
p_0=
\sum_{(\Delta,a,c)\in\mathcal T}
c(1-y)^{t+\Delta}y^{aP},
\tag{3.1}
$$


where


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
\tag{3.2}
$$


contains fourteen terms.

For a HIGH row, the row shift belongs in $q$, not in the beta top. Define


$$
\mathcal B(N,q)
=
\frac{4^N N!(N+q)!(2q)!}
{q!(2N+2q+1)!}.
\tag{3.3}
$$


This is the evaluated beta functional from Turn 14.

Since $H$ is odd, the complete rational HIGH source is


$$
\boxed{
(\upsilon_0)_s
\equiv
-3^{h-1}
\sum_{(\Delta,a,c)\in\mathcal T}
c\left\{
\beta\,\mathcal B(H+t+\Delta,s+aP)
+
3\,\mathcal B(H+t+\Delta,s+aP+1)
\right\}
\pmod{3^{28}}.
}
\tag{3.4}
$$


Thus, specifically,


$$
N=H+t+\Delta,\qquad q=s+aP+\epsilon.
$$


This differs from the LOW formula with $N=H+u+t+\Delta$.

Likewise,


$$
\boxed{
(\upsilon_T)_s
\equiv
-3^{h-1}
\left\{
\beta\,\mathcal B(H,\nu-1+s)
+
3\,\mathcal B(H,\nu+s)
\right\}
\pmod{3^{28}}.
}
\tag{3.5}
$$



Section 7 gives an explicit value-producing algorithm for every beta ratio in these formulas. Equations (3.4)–(3.5) are therefore not being left as named unevaluated sums.

### 3.2 Physical support and the $3H$ resonance

The largest degree in $p_0$ is $133P+t$. Since


$$
\nu-(133P+t+1)=P+k-1>0,
\tag{3.6}
$$


every term in (3.4), including its $3y$-part, has rational-polynomial degree at most


$$
H+m+133P+t+1
=
\frac{3H-1}{2}-(P+k-1).
\tag{3.7}
$$


It is strictly below the $3H$-pole and below $K_{\rm phys}$.

For (3.5), the largest rational-polynomial degree is


$$
H+m+\nu=\frac{3H-1}{2}.
$$


Equality occurs only in the $3y$-term at $s=m$. Thus the physical $3H$ resonance is present exactly where the baseline says it is.

The factorial contribution to either normalized source has valuation at least


$$
h-1\ge62.
$$


It is consequently invisible modulo $3^{28}$. This is a local payment, not a deletion of the factorial term from the complete functional.

### 3.3 Exact valuation count

For $N,q\ge0$, let $j_e(q)$ be the least nonnegative residue of


$$
\frac{3^e-1}{2}-q\pmod{3^e}.
$$


The established beta-ratio evaluation gives


$$
v_3\mathcal B(N,q)
=
-\sum_{e\ge1}
\mathbf1_{\{N\bmod3^e\ge j_e(q)\}}.
\tag{3.8}
$$


For all the HIGH source arguments above, the largest factorial argument is at most $3H=3^h$, so the sum need only run through $e=h$.

In particular, the $e=h$ indicator must not be suppressed at the physical terminal in (3.5).

---

## 4. An exact residue grading for the actual matrices modulo $27$

The main new argument takes place over


$$
\mathscr A=\mathbb Z/27\mathbb Z.
$$


It uses actual matrix entries in this ring. It does not lift a matrix known only modulo $3$.

### 4.1 Arithmetic residues forced by the original domain

The original hypotheses give


$$
v_3(D)=v_3(A)=5.
$$


Indeed, $D=268P+2\chi$, $S\ge31$, and $v_3(\chi)=5$. Thus


$$
D\equiv0,\qquad \nu\equiv-1,\qquad
d\equiv26,\qquad m\equiv14\pmod{27}.
\tag{4.1}
$$


Also


$$
r_H\equiv13\pmod{27},\qquad m+d\equiv13\pmod{27}.
$$



We use $\rho=13$ for this residue.

For an integer $N$ with $v_3(N)\ge5$,


$$
27\nmid i
\quad\Longrightarrow\quad
v_3\binom Ni
\ge v_3(N)-v_3(i)\ge3.
$$


Hence


$$
(1-y)^N\bmod27
$$


is supported only at exponents divisible by $27$. In particular, this applies to $N=A$ and to $N=H+t+\Delta$.

### 4.2 A temporary unimodular LOW basis change

For the proof only, replace the LOW basis $x^u$ by $y^u$, $0\le u<D$.

If


$$
U_x=U_yC,
\qquad
C_{v,u}=(-1)^{u-v}\binom uv\quad(v\le u),
$$


then $C$ is an integral unit triangular matrix. Thus


$$
\mathcal L_x=C^T\mathcal L_yC,\qquad
\mathcal X_x=C^T\mathcal X_y,\qquad
\alpha_x=C^T\alpha_y,
$$


and


$$
\mathcal X_x^T\mathcal L_x^{-1}\alpha_x
=
\mathcal X_y^T\mathcal L_y^{-1}\alpha_y.
\tag{4.2}
$$


The HIGH Schur matrix is also unchanged.

This is an exact coordinate change inside the original LOW space. It does not replace the finite matrix or alter the original frame used for later physical layers.

### 4.3 Separating the $\beta$ and $3y$ parts

Let


$$
G_\epsilon(f,g)
=
\mathcal M\bigl((y+1)x^Ay^\epsilon fg\bigr),
\qquad \epsilon=0,1.
$$


Then


$$
G_c=\beta G_0+3G_1.
$$



In the monomial LOW basis, define


$$
L_\epsilon=G_\epsilon(U_y,U_y)/3,\qquad
X_\epsilon=G_\epsilon(U_y,Y)/3,\qquad
E_\epsilon=G_\epsilon(Y,Y).
$$


All these matrices are integral.

For LOW/LOW and LOW/HIGH pairings, the $3H$-pole is absent even for $\epsilon=1$, so their division by $3$ is paid. For HIGH/HIGH pairings no division by $3$ is made. Their actual degree remains at most $K_{\rm phys}$.

Every pole visible modulo $27$ in these normalized matrices has coefficient-extraction index


$$
\frac{b-1}{2}\equiv13\pmod{27},
$$


because its odd denominator $b$ is divisible by a power of $3$ much greater than $27$. The factorial terms are too deep to contribute. The preceding binomial divisibility therefore proves:


$$
\boxed{
L_\epsilon(u,v)=0
\quad\text{unless}\quad u+v+\epsilon\equiv\rho\pmod{27},
}
\tag{4.3}
$$




$$
\boxed{
X_\epsilon(u,s)=0
\quad\text{unless}\quad u+s+\epsilon\equiv\rho\pmod{27},
}
\tag{4.4}
$$




$$
\boxed{
E_\epsilon(s,t)=0
\quad\text{unless}\quad s+t+\epsilon\equiv\rho\pmod{27}.
}
\tag{4.5}
$$



These are assertions about actual entries modulo $27$.

### 4.4 Why finite inversion preserves the grading

Call a matrix reflection-graded by $b$ if its $(i,j)$-entry vanishes unless


$$
i+j\equiv b\pmod{27}.
$$


A unit square matrix with this grading has an inverse with the same grading: after arranging coordinates by residue, it is a permutation of independent square blocks.

The required block-size condition is valid here:

- the LOW interval has length $D$, a multiple of $27$;
- the HIGH interval is preserved by the literal reflection
  

$$
s\longmapsto m+d-s,
$$


  whose residue sum is $\rho$.

Thus no periodic extension of either finite interval is involved.

Introduce a formal variable $\lambda$:


$$
L(\lambda)=\beta L_0+\lambda L_1,\qquad
X(\lambda)=\beta X_0+\lambda X_1,
$$




$$
E(\lambda)=\beta E_0+\lambda E_1,
$$




$$
S(\lambda)=E(\lambda)-3X(\lambda)^TL(\lambda)^{-1}X(\lambda).
\tag{4.6}
$$


At $\lambda=3$, these are exactly the current core blocks.

Both $L(0)$ and $S(0)$ are unit matrices. The latter statement follows from the actual finite HIGH unit theorem, because its LOW Schur return has the explicit factor $3$.

Expand


$$
L(\lambda)^{-1}=\sum_{j\ge0}\lambda^jL^{[-1]}_j.
$$


The coefficient $L^{[-1]}_j$ is reflection-graded by $\rho+j$. Indeed, each insertion of $L_1$, whose grade is $\rho-1$, between two inverse factors raises the inverse grade by one.

The coefficient of $\lambda^j$ in $S(\lambda)$ is reflection-graded by $\rho-j$. For the Schur term, the grades combine as


$$
(\rho-\epsilon_1)-(\rho+j)+(\rho-\epsilon_2)
=
\rho-(j+\epsilon_1+\epsilon_2).
$$


It follows by inversion that


$$
S(\lambda)^{-1}=\sum_{j\ge0}\lambda^jM_j,
\qquad
M_j\text{ has grade }\rho+j.
$$


Substituting $\lambda=3$ gives


$$
\boxed{
M_H\equiv M_0+3M_1+9M_2\pmod{27},
\qquad
(M_j)_{st}=0\ \text{unless}\ s+t\equiv\rho+j.
}
\tag{4.7}
$$



The coefficient $M_0$ contains the actual LOW Schur return at $\lambda=0$. It is not the inverse of $E_Y\bmod3$, nor is it a chosen lift of that inverse.

This is precisely where the actual mod-$9$ and mod-$27$ matrix digits and their carries are retained.

---

## 5. Source and return grades at the precision needed for the scalar

### 5.1 The LOW source for $\Omega_P$

Use the monomial LOW row $y^u$, $0\le u<D$. Its normalized rational source has


$$
N=H+t+\Delta,\qquad q=u+aP+\epsilon.
$$


The original finite bound gives


$$
t+\Delta+q\le401P+\Pi.
$$


Therefore every beta indicator above $S+6$ vanishes.

For $1\le e\le5$, $N\bmod3^e=0$, and the indicator is $1$ precisely when


$$
3^e\mid 2u+2\epsilon+1.
$$


Consequently


$$
v_3\!\left(3^{h-1}\mathcal B(N,q)\right)
\ge
30-\min\{v_3(2u+2\epsilon+1),5\}.
\tag{5.1}
$$



For the $\beta$-part to survive modulo $3^{28}$, one must have


$$
u\equiv13\pmod{27}.
$$


For the $3y$-part, the corresponding residue is $u\equiv12$.

Thus the actual source, including all fourteen terms, has a decomposition


$$
\boxed{
\alpha_{0,y}
\equiv
3^{25}\bigl(a_{13}+3a_{12}\bigr)
\pmod{3^{28}},
}
\tag{5.2}
$$


where the subscripts denote residue support modulo $27$. The values of these vectors need not be evaluated for the argument below.

### 5.2 The LOW terminal source

For the LOW terminal source the beta top is $H$, and


$$
q=u+\nu-1+\epsilon.
$$


The finite range gives $q<403P$, so no $3H$ resonance occurs.

For $N=H$, all indicators through $h-1$ are true exactly for the divisors of $2q+1$, and the higher indicators are absent. Hence


$$
v_3\!\left(3^{h-1}\mathcal B(H,q)\right)
=h-1-v_3(2q+1).
\tag{5.3}
$$


Since $2q+1<805P<3^{S+7}$, this valuation is at least $25$.

A term visible modulo $3^{28}$ has $q\equiv13\pmod{27}$. Because
$\nu-1\equiv-2$, this gives source residue $15$ for the $\beta$-part and residue $14$ for the $3y$-part. Therefore


$$
\boxed{
\alpha_{T,y}
\equiv
3^{25}\bigl(a_{15}+3a_{14}\bigr)
\pmod{3^{28}}.
}
\tag{5.4}
$$



### 5.3 The two complete LOW-return profiles through the needed precision

Apply the exact grading of $L(\lambda)^{-1}$ and $X(\lambda)^T$ to (5.2)–(5.4).

A LOW source supported at residue $b$, after $j$ inverse insertions and an $\epsilon$-part of $X^T$, returns to HIGH residue


$$
b-j-\epsilon,
$$


with the corresponding factor $3^{j+\epsilon}$.

It follows that the actual return vectors satisfy


$$
\boxed{
\mathcal R_0
\equiv
3^{25}\bigl(R_{13}+3R_{12}+9R_{11}\bigr)
\pmod{3^{28}},
}
\tag{5.5}
$$




$$
\boxed{
\mathcal R_T
\equiv
3^{25}\bigl(T_{15}+3T_{14}+9T_{13}\bigr)
\pmod{3^{28}}.
}
\tag{5.6}
$$



These statements include all carry corrections. They are proved in the actual residue ring, not by assigning arbitrary lifts to leading inverse images.

In particular, the previously evaluated leading $\Lambda$ is compatible with (5.5), since $121\equiv13\pmod{27}$. No proof of Turn 14’s 48-coordinate solve is repeated.

### 5.4 The unreturned HIGH sources modulo $27$

For $\upsilon_T$, the $\beta$-part has no $3H$ resonance and has valuation at least $1$. When visible modulo $27$, it satisfies


$$
\nu-1+s\equiv13\pmod{27},
$$


hence $s\equiv15$.

The $3y$-part is supported at residue $14$. At $s=m$ it includes the physical $3H$ resonance and can be a unit. Away from $m$, it has valuation at least $2$. Therefore


$$
\boxed{
\upsilon_T\equiv t_{14}+3t_{15}\pmod{27},
\qquad t_{14}\equiv e_m\pmod3.
}
\tag{5.7}
$$



For $\upsilon_0$, every individual $\beta$-channel is divisible by $3$. One way to see this is that the $H$-pole modulo $3$ extracts a coefficient of a polynomial of degree less than $\nu$, while $r_H-s\ge\nu$; the $3H$-pole is absent.

Since $v_3(H+t+\Delta)=5$, the binomial grading from Section 4 shows that the $\beta$-channel is supported at residue $13$, and the $3y$-channel at residue $12$, modulo $27$. The latter has one additional factor $3$. Thus


$$
\boxed{
\upsilon_0\equiv3b_{13}+9b_{12}\pmod{27}.
}
\tag{5.8}
$$


In particular,


$$
\upsilon_0\in3\mathbb Z_3^{\{d,\ldots,m\}}.
\tag{5.9}
$$



### 5.5 The two HIGH inverse images needed for the contraction

From (4.7) and (5.7), the support of $M_H\upsilon_T\bmod27$ is contained in


$$
\boxed{\{25,26,0,1\}\pmod{27}.}
\tag{5.10}
$$


Indeed:

- residue $14$ is sent by $M_j$ to residue $-1+j$;
- residue $15$, already carrying a factor $3$, is sent to residue $-2+j$.

Similarly, (4.7) and (5.8) give


$$
\boxed{
\operatorname{supp}(M_H\upsilon_0\bmod27)
\subseteq\{0,1\}\pmod{27}.
}
\tag{5.11}
$$



These are joint finite source/inverse-return statements at exactly the three digits required to contract the depth-$25$ LOW returns.

---

## 6. New complete inverse-return theorem

### Theorem 6.1 — Both LOW source returns have zero contracted contribution

For every sufficiently large original tuple in Range III,


$$
\boxed{
(\upsilon_T-\mathcal R_T)^TM_H(\upsilon_0-\mathcal R_0)
\equiv
\upsilon_T^TM_H\upsilon_0
\pmod{3^{28}}.
}
\tag{6.1}
$$



#### Proof

Expand the difference:


$$
\begin{aligned}
&(\upsilon_T-\mathcal R_T)^TM_H(\upsilon_0-\mathcal R_0)
-\upsilon_T^TM_H\upsilon_0\\
&\qquad=
-(M_H\upsilon_T)^T\mathcal R_0
-\mathcal R_T^T(M_H\upsilon_0)
+\mathcal R_T^TM_H\mathcal R_0.
\end{aligned}
\tag{6.2}
$$



For the first term, $\mathcal R_0/3^{25}\bmod27$ is supported at residues


$$
\{13,12,11\},
$$


whereas $M_H\upsilon_T\bmod27$ is supported at


$$
\{25,26,0,1\}.
$$


The sets are disjoint. Hence


$$
(M_H\upsilon_T)^T\mathcal R_0\in3^{28}\mathbb Z_3.
$$



For the second term, $\mathcal R_T/3^{25}\bmod27$ is supported at


$$
\{15,14,13\},
$$


whereas $M_H\upsilon_0\bmod27$ is supported at $\{0,1\}$. Thus


$$
\mathcal R_T^T(M_H\upsilon_0)\in3^{28}\mathbb Z_3.
$$



Finally, $M_H$ is integral and both returns lie in $3^{25}$, so


$$
\mathcal R_T^TM_H\mathcal R_0\in3^{50}\mathbb Z_3.
$$


Substitution in (6.2) proves the theorem. ∎

### What has and has not been removed

The theorem evaluates three actual contracted terms, uniformly, as zero modulo $3^{28}$. It is not a redefinition of the target.

It removes the need to determine the separate source jets


$$
3^{-25}M_L\alpha_0\bmod27,\qquad
3^{-25}M_L\alpha_T\bmod27
$$


for this endpoint scalar.

It does **not** remove


$$
3\mathcal X^TM_L\mathcal X
$$


from $\mathcal S_H$. That matrix return remains inside the actual finite inverse throughout the proof.

### Corollary 6.2 — The full source coordinate at the first HIGH row vanishes

At the actual first HIGH row,


$$
\boxed{
(\mathfrak b_H)_d\equiv0\pmod{3^{28}}.
}
\tag{6.3}
$$



#### Proof

First, $d\equiv26\pmod{27}$, so (5.5) gives


$$
(\mathcal R_0)_d\in3^{28}\mathbb Z_3.
$$



For the raw source at $s=d$, use


$$
N=H+t+\Delta,\qquad q=d+aP+\epsilon.
$$


The finite bounds give


$$
t+\Delta+q<536P.
$$


As before, indicators above $S+6$ vanish.

For $1\le e\le5$, $N\bmod3^e=0$, while


$$
q\equiv-1+\epsilon\pmod{243}.
$$


Thus $2q+1$ is congruent to $-1$ or $1$ modulo $243$, so all five initial indicators are zero. There are at most $S+1$ remaining indicators. Consequently


$$
v_3\!\left(3^{h-1}\mathcal B(N,q)\right)\ge30.
$$


The $3y$-part has an additional factor $3$. Every coefficient in the fourteen-term table is integral, and the factorial part is deeper still. Hence


$$
(\upsilon_0)_d\in3^{30}\mathbb Z_3.
\tag{6.4}
$$


Subtracting the LOW return proves (6.3). ∎

This is stronger than the supplied $\Lambda_d=0$, but it still does not determine the contraction with the higher HIGH test.

---

## 7. A value-producing arithmetic rule for both complete raw HIGH sources

The beta-ratio formulas in Section 3 must produce values, not just support tests. This section supplies such a producer without a table of length $3^{28}$, $P$, or $H$.

### 7.1 Factorial units

For $n\ge0$, define


$$
U(n)=\frac{n!}{3^{v_3(n!)}}\in\mathbb Z_3^\times,
$$


and


$$
F_3(n)=\prod_{\substack{1\le i\le n\\3\nmid i}}i.
$$


Then


$$
U(n)=F_3(n)\,U(\lfloor n/3\rfloor),
$$


so


$$
\boxed{
U(n)=\prod_{e\ge0}F_3(\lfloor n/3^e\rfloor).
}
\tag{7.1}
$$



Only $O(\log_3(n+1))$ factors occur.

### 7.2 A $729$-position table

Fix


$$
M=3^{28},\qquad B=3^6=729.
$$


For $0\le R<B$, define


$$
C_R=
\prod_{\substack{1\le i\le R\\3\nmid i}}i\pmod M,
$$


and, for $1\le a\le4$,


$$
H_{a,R}
=
\sum_{\substack{1\le i\le R\\3\nmid i}}i^{-a}\pmod M.
\tag{7.2}
$$


Put


$$
C=C_{B-1},\qquad H_a=H_{a,B-1}.
$$



There are $5\cdot729=3645$ stored residues. All inversions are of units among $1,\ldots,728$.

Write


$$
n=QB+R,\qquad 0\le R<B.
$$


Let


$$
S_a(Q)=\sum_{b=0}^{Q-1}b^a.
$$


Only $a=1,2,3,4$ is needed, with the explicit integer formulas


$$
S_1(Q)=\frac{Q(Q-1)}2,
$$




$$
S_2(Q)=\frac{Q(Q-1)(2Q-1)}6,
$$




$$
S_3(Q)=\left(\frac{Q(Q-1)}2\right)^2,
$$




$$
S_4(Q)=
\frac{Q(Q-1)(2Q-1)(3Q^2-3Q-1)}{30}.
\tag{7.3}
$$



Define


$$
L(Q,R)=
\sum_{a=1}^{4}
\frac{(-1)^{a+1}B^a}{a}
\left(H_aS_a(Q)+Q^aH_{a,R}\right)
\pmod M.
\tag{7.4}
$$


Then


$$
L(Q,R)\in3^6\mathbb Z_3.
$$



### Proposition 7.1 — Explicit unit-factor product

For every $n\ge0$,


$$
\boxed{
F_3(n)
\equiv
C^Q C_R
\left(
1+L+\frac{L^2}{2}+\frac{L^3}{6}+\frac{L^4}{24}
\right)
\pmod{3^{28}},
}
\tag{7.5}
$$


where $L=L(Q,R)$.

#### Proof

Split the nonmultiples of $3$ into complete blocks and a final partial block:


$$
\begin{aligned}
F_3(n)
={}&C^Q C_R
\prod_{b=0}^{Q-1}
\prod_{\substack{1\le i<B\\3\nmid i}}
\left(1+\frac{bB}{i}\right)\\
&\times
\prod_{\substack{1\le i\le R\\3\nmid i}}
\left(1+\frac{QB}{i}\right).
\end{aligned}
\tag{7.6}
$$


Each factor in parentheses belongs to $1+3^6\mathbb Z_3$.

For the logarithm, a term of order $a$ has valuation at least


$$
6a-v_3(a).
$$


For every $a\ge5$, this is at least $28$. Thus the logarithm of the product in parentheses is exactly (7.4) modulo $3^{28}$.

Since $v_3(L)\ge6$,


$$
v_3(L^j/j!)\ge6j-v_3(j!)\ge28
\qquad(j\ge5).
$$


The exponential therefore truncates after degree $4$, proving (7.5). ∎

### 7.3 Every division in the producer is paid

The apparent divisions by $3$ in (7.4)–(7.5) cause no loss:

- $B^3/3=3^{17}$ is integral;
- $L^3/6$ and $L^4/24$ are integral because $L\in3^6\mathbb Z_3$;
- the expressions in (7.3) are exact integers.

For modular evaluation of the integer polynomials in $Q$, one can retain $Q\bmod 2\cdot3^{29}$. The extra ternary digit pays the possible factor $3$ in the denominators $6,24,30$, while the factor $2$ retains parity.

There is also no large-exponent operation hidden in $C^Q$. The product of all units modulo $B$ is $-1$, so


$$
-C\in1+3^6\mathbb Z_3.
$$


Writing $\varrho=-C$,


$$
\boxed{
C^Q
\equiv
(-1)^Q
\sum_{j=0}^{4}\binom Qj(\varrho-1)^j
\pmod{3^{28}}.
}
\tag{7.7}
$$


Terms with $j\ge5$ contain $3^{30}$.

Equations (7.1), (7.3)–(7.5), and (7.7) are a complete bounded-register value algorithm for factorial units.

### 7.4 Producing a weighted HIGH beta term

For a beta argument $(N,q)$, calculate


$$
C(N,q)=
\sum_{e=1}^{h}
\mathbf1_{\{N\bmod3^e\ge j_e(q)\}}.
\tag{7.8}
$$


For $1\le K\le28$, calculate


$$
\mathscr U_K(N,q)=
4^N
\frac{U(N)U(N+q)U(2q)}
{U(q)U(2N+2q+1)}
\pmod{3^K}
\tag{7.9}
$$


using the preceding factorial-unit algorithm. Every denominator in (7.9) is a unit.

The exact valuation identity gives


$$
3^{C(N,q)}\mathcal B(N,q)
\equiv\mathscr U_K(N,q)\pmod{3^K}.
$$



For a term in (3.4), write


$$
c=3^{\delta_c}c^\times,\qquad 3\nmid c^\times,
$$


and put


$$
N=H+t+\Delta,\qquad q=s+aP+\epsilon,
$$




$$
\lambda=h-1+\delta_c+\epsilon-C(N,q).
\tag{7.10}
$$


Its actual contribution modulo $3^{28}$ is:

- zero if $\lambda\ge28$;
- otherwise
  

$$
\boxed{
  -3^\lambda c^\times\beta^{1-\epsilon}
  \mathscr U_{28-\lambda}(N,q).
  }
  \tag{7.11}
$$



In this HIGH source $\lambda\ge0$; in fact every $\beta$-channel has $\lambda\ge1$.

The same rule applies to (3.5), using $c=1$, $N=H$, and


$$
q=\nu-1+s+\epsilon.
$$


At the physical terminal $s=m,\epsilon=1$,


$$
C(H,r_H)=h,\qquad \lambda=h-1+1-h=0.
$$


Thus the $3H$ resonance produces its full unit value. It is neither omitted nor treated as an ordinary integral unweighted $G_1/3$ source.

Finally,


$$
\boxed{\beta\equiv2\chi-71\pmod{3^{28}},}
\tag{7.12}
$$


because $H$ and $P$ are divisible by $3^{28}$. The full $\beta$-digits, rather than just $\beta\bmod3$, are used in (7.11).

### 7.5 Complexity and limitation

For the two HIGH sources, every factorial argument is at most $3H$. Hence a call to $U(n)$ uses at most $h+1$ evaluations of (7.5).

A direct implementation of one $\upsilon_0$-entry requires at most:

- $28$ weighted beta terms;
- five factorial-unit calls per term;
- $140(h+1)$ evaluations of the fixed formula (7.5), before common-subexpression reuse.

Each such evaluation uses a fixed number of operations on residues of at most $3^{29}$, together with parity. A generous explicit bound is fewer than $512$ such modular arithmetic operations per evaluation once the universal table is supplied. The indicator counts require $O(h)$ further digit comparisons per beta term.

Thus the producer is linear in the ternary input length $h$, with a fixed precision-dependent constant. It is not proportional to $P$, and it requires no original factorial array.

However, producing one entry and producing all entries are different tasks. Enumerating the literal HIGH interval would still require


$$
m-d+1
$$


calls, an exponentially large number in $h$. More importantly, this entry rule does not construct or contract the true finite $M_H$.

Therefore it does **not** justify an endpoint experiment by an original-length solve or Neumann vector.

---

## 8. The exact reduced endpoint obligation

Theorem 6.1 gives


$$
a\eta_0
=
\frac{\upsilon_T^TM_H\upsilon_0}{3^{27}}\pmod3.
\tag{8.1}
$$


By the audited baseline,


$$
M_H\upsilon_T-e_d\in3\mathbb Z_3^{\{d,\ldots,m\}},
$$


and by (5.9),


$$
\upsilon_0\in3\mathbb Z_3^{\{d,\ldots,m\}}.
$$


Define the actual integral vectors


$$
w_H=\frac{M_H\upsilon_T-e_d}{3},
\qquad
f_H=\frac{\upsilon_0}{3}.
\tag{8.2}
$$


Then


$$
\upsilon_T^TM_H\upsilon_0
=
(\upsilon_0)_d+9w_H^Tf_H.
$$


Since $(\upsilon_0)_d\in3^{30}$, it follows that


$$
\boxed{
a\eta_0=\frac{w_H^Tf_H}{3^{25}}\pmod3.
}
\tag{8.3}
$$


The numerator in (8.3) is divisible by $3^{25}$.

The precise remaining arithmetic is therefore


$$
\boxed{w_H^Tf_H\pmod{3^{26}}.}
\tag{8.4}
$$



### 8.1 What information has genuinely been removed

The new result has removed:

1. the separate $z_1,z_2$ source jets for $\alpha_0$;
2. the corresponding LOW source jets for $\alpha_T$;
3. the entire direct contribution of the leading test coordinate $e_d$;
4. one digit from the required HIGH inverse precision.

For (8.4), it suffices to know


$$
f_H\bmod3^{26},
\qquad
M_H\upsilon_T\bmod3^{27}.
$$


The first is completely value-produced by Section 7. The second remains open.

This is not merely a renamed large solve: the eliminated LOW-source contractions have been explicitly proved to be zero at the required precision, without producing any of their unknown entries. Nevertheless, the remaining HIGH inverse problem is still a genuine unresolved problem. It would be misleading to call (8.4), by itself, a compact inverse algorithm.

### 8.2 A concrete next HIGH certificate

A source-specific next lemma can be stated with a smaller and fully paid budget.

> **Finite HIGH column-defect certificate.**  
> Construct a precision-sized description of an integral polynomial
> 

$$
> Z_H(y)=\sum_{s=d}^{m}z_s y^s
>
$$


> in the literal HIGH interval, such that
> 

$$
> \boxed{
> \mathcal S_H(e_d+3z)-\upsilon_T
> \in3^{27}\mathbb Z_3^{\{d,\ldots,m\}}.
> }
> \tag{8.5}
>
$$


> Then evaluate
> 

$$
> \boxed{z^Tf_H\pmod{3^{26}}.}
> \tag{8.6}
>
$$



Because $M_H$ is integral, (8.5) implies


$$
z-w_H\in3^{26}\mathbb Z_3^{\{d,\ldots,m\}},
$$


so (8.6) is exactly the remaining digit in (8.4).

For example, a proof that


$$
z^Tf_H\in3^{26}\mathbb Z_3
$$


would prove $\eta_0=0$. A different residue would evaluate a nonzero $\eta_0$.

The source $\upsilon_T$, the source $f_H$, their physical cutoff, and their value rules are now explicit. The difficulty is to produce and contract $z$ with the **true** Schur operator, not to invent another name for an original-length vector. No such compact $z$ is supplied here.

### 8.3 Why the original HIGH ends still matter

The physical terminal enters $\upsilon_T$ through a unit $3H$-resonance. The first HIGH row enters through the actual baseline $M_H e_m=e_d\bmod3$, the exact interval reflection, and the vanishing proved in Corollary 6.2.

Deleting either end would change:

- the unit antidiagonal structure;
- the residue block sizes;
- the finite inverse;
- the source/test contraction.

Likewise, replacing $\mathcal S_H$ by $E_Y$, or constructing a $12\times12$ replacement Gram matrix, is not justified by this report.

---

## 9. No advance to first $4$, actual physical $7$, or primitive normalization

Neither endpoint is closed, so the first-$4$ mixed-prefix calculation is not undertaken.

The retained physical-$6$ assembly is still


$$
C_6=
C^{\rm mom}
-\bigl(e_{k-1}\eta^T+\eta e_{k-1}^T\bigr)
-R_4
\pmod3,
$$


with both the needed terminal data and the actual first-$4$ return still incomplete.

The mixed-prefix quantity retains its division


$$
P_{ui}=\frac{d_u^T\mathsf A^{-1}d_H{}_i}{3}\pmod3,
$$


and the corresponding cross retains the upper $3y$ corner


$$
(C_H)_{ui}
=
-c_{P-1-u-i-\Pi}
+c_{P-1-u-i-2\Pi}
-2\,\mathbf1_{u=R,\ i=k-1}
-P_{ui}.
$$


No finite boundary or actual complementary inverse is altered.

The later direction remains


$$
B_6x=w_6,\qquad x\in3^{-1}\mathbb Z_3^{k-1}.
$$


The actual physical-$7$ obligation still includes the actual/core difference, the physical-$5$ complementary and kernel-pivot returns, higher endpoint adaptation, and source precision $34$.

The diagonal payments remain


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


No numerator is assumed to be a unit.

---

## 10. Complete actual producer and forcing retained

The actual producer is still


$$
Q_{\rm act}=Q_c+3^7\mathscr R.
$$


The correction is $3^7\mathscr R$, not an older $3^6$-correction.

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
\qquad
v=T_n^{-1}u,
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
\tag{10.1}
$$



The complete forcing identity remains


$$
\boxed{
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
}
\tag{10.2}
$$


Neither forcing term nor the terminal coordinate is discarded.

The moment recurrence remains


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
\tag{10.3}
$$



No computation of the original $T_n$, factorial moment matrix, or complete terminal table is proposed.

---

## 11. Actual contents, least simultaneous clearer, all-prime gcd, and whole error

All actual integer column contents remain those of the original complete construction. The least simultaneous clearer remains the actual $\ell_{\rm clr}$. Neither is replaced by a power of $3$ or by a convenient common multiple.

Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the final gcd over **all primes**


$$
G=\gcd(|A_\ell|,|B_\ell|).
$$


For $B_\ell\ne0$, the actual primitive pair is


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
{G}\det H_{\rm complete}.
}
\tag{11.1}
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
\tag{11.2}
$$


These conditions would make the nonzero whole errors tend to zero. If $e+\pi$ were rational with denominator $b$, every such nonzero error would have absolute value at least $1/b$, a contradiction.

None of the conditions in (11.2) follows from the new HIGH return cancellation.

---

## 12. Bounded exact arithmetic for independent checking

No computation was performed. The proof of Theorem 6.1 is symbolic and needs no original-index numerical solve.

### 12.1 A new universal source-value receipt

If an arithmetic implementation of Section 7 is desired, the following is a bounded auxiliary calculation.

**Inputs**

- modulus $3^{28}$;
- block length $B=729$;
- integers $1,\ldots,728$ not divisible by $3$;
- prefix indices $R=0,\ldots,728$;
- harmonic powers $a=1,2,3,4$.

**Expected verifiable outputs**

1. The arrays $C_R,H_{a,R}$ defined by (7.2).
2. Their defining recurrences:
   

$$
C_R=
   \begin{cases}
   C_{R-1},&3\mid R,\\
   RC_{R-1},&3\nmid R,
   \end{cases}
$$


   and
   

$$
H_{a,R}=
   \begin{cases}
   H_{a,R-1},&3\mid R,\\
   H_{a,R-1}+R^{-a},&3\nmid R.
   \end{cases}
$$


3. The check
   

$$
C_{728}\equiv-1\pmod{729}.
$$


4. For $0\le n\le1470=2\cdot729+12$, agreement modulo $3^{28}$ between:
   - the factorial-unit value obtained from (7.1), (7.5), and (7.7);
   - a direct product of $1,\ldots,n$, with each factor’s power of $3$ stripped before multiplication.

The expected mismatch list is empty. The calculation checks only this finite arithmetic range and the table construction. The proof of the general formula is the argument in Section 7, not the finite test.

This is a new small unit-arithmetic receipt. It is not the old optional $244$-entry check, and it is not an original source or terminal table.

### 12.2 What is not yet a justified endpoint calculation

The source-value rule does not supply $M_H\upsilon_T\bmod3^{27}$ in a compact form. Therefore no proposed calculation of $\eta_0$ by:

- enumerating the HIGH interval;
- constructing an original-length Neumann vector;
- computing an original factorial or moment matrix;
- substituting a fixed twelve-column Gram problem

is justified here.

A future endpoint calculation needs the joint finite HIGH certificate in (8.5)–(8.6), or an equivalent proved contraction method with a stated complexity bound.

---

## 13. Evaluated/open status ledger

| Item | Status and exact scope |
|---|---|
| Supplied leading baseline $\mathfrak t_H=e_m$, $M_He_m=e_d\bmod3$ | Audited and valid on the literal finite interval |
| Turn 14 LOW digit law, 48-coordinate solve, leading $\Lambda$ | Reused at their stated scope; their proofs and optional constant check are not repeated |
| Complete raw HIGH source formulas | All fourteen $\Omega_P$-terms and both $\beta,3y$ parts explicitly retained |
| Raw HIGH source values through $3^{28}$ | Deterministic factorial-unit value algorithm proved; no original-index execution performed |
| $3H$ terminal resonance | Retained and explicitly paid; it is the unit case $\lambda=0$ in the value rule |
| Actual mod-$27$ matrix/source grading | Newly proved, including actual matrix digits and integral-lift carries |
| Both contracted LOW source returns | Newly evaluated as zero modulo $3^{28}$, Theorem 6.1 |
| Full coordinate $(\mathfrak b_H)_d$ | Newly evaluated as zero modulo $3^{28}$ |
| LOW return inside $\mathcal S_H$ | Retained; not evaluated away |
| Complete scalar $\eta_0$ | Open; exact remaining digit is $w_H^Tf_H/3^{25}\bmod3$ |
| Endpoint $\eta_{k-1}$ | Open |
| First-$4$ mixed-prefix digit | Not undertaken before an endpoint closes |
| Actual physical $7$, source $34$, $3^7\mathscr R$ transport | Open and distinct from the present core calculation |
| Actual contents and least simultaneous clearer | Open |
| All-prime final gcd and actual primitive denominator | Open |
| Same-index nonzero whole error and decay | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

---

## 14. Conclusion

The new proved result is a **complete contracted inverse-return cancellation**:


$$
\boxed{
\mathfrak t_H^TM_H\mathfrak b_H
\equiv
\upsilon_T^TM_H\upsilon_0
\pmod{3^{28}},
}
$$


with the true finite HIGH Schur inverse, both original HIGH ends, and the physical terminal retained.

The proof strictly reduces the outstanding endpoint information. The two additional LOW source jets are no longer needed for this scalar, and the full first-HIGH-row source coordinate is zero at the target precision. The remaining source values are produced by an explicit bounded-precision factorial-unit rule.

The exact bottleneck is now the finite HIGH directional contraction


$$
\boxed{
w_H^Tf_H\pmod{3^{26}},
\qquad
w_H=\frac{M_H\upsilon_T-e_d}{3},
\qquad
f_H=\frac{\upsilon_0}{3}.
}
$$


No compact producer or evaluated value for this contraction is proved here. In particular, the leading test $e_d$ has not been promoted to the full precision-$27$ test.

The optional bounded arithmetic is only the new $729$-position unit-factor table and its finite verification range. It is not an endpoint computation and has no direct global irrationality consequence.



$$
\boxed{
\text{Neither endpoint nor the global rationality question for }e+\pi
\text{ is settled.}
}
$$


