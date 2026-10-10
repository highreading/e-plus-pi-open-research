> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1, Turn 19 — The complementary endpoint and its complete finite LOW return

## Abstract and status

The global rationality or irrationality of $e+\pi$ is not decided in this report.

At the local core level, the complementary endpoint can be evaluated. Put


$$
I=k-1=3\chi-\Pi-2,
\qquad
p_I(y)=\Omega_P(y)(1-y)^t y^I.
$$


The new source calculations below prove, in the original finite spaces, that:

1. The exact LOW/HIGH elimination gives
   

$$
\boxed{
   g_T^TE_c^{-1}b_I
   \equiv
   27\,(M_H\upsilon_T)^Tf_H(I)
   \pmod{3^{30}},
   }
   \tag{A}
$$


   where
   

$$
b_I=G_c(W,x^Dp_I),\qquad
   f_H(I)=G_c(Y,x^Dp_I)/9.
$$


   Every LOW source return in this reduction is retained and proved to vanish at the required precision. This is a new reduction for $I$, not an application of the previously accepted reduction for $i=0$.

2. For the unchanged Turn 18 bulk module $\mathscr B$,
   

$$
\boxed{\mathscr B^Tf_H(I)\subseteq3^{29}\mathbb Z_3.}
   \tag{B}
$$


   The proof includes all fourteen source terms, both channels, the complete finite quotients, and the literal lower HIGH mask.

3. The actual shifted HIGH source satisfies
   

$$
\boxed{
   f_H(I)\equiv f_{15}+3f_{14}\pmod9,
   }
   \tag{C}
$$


   with the subscripts denoting support modulo $27$. This is derived from the complete functional on the original HIGH interval; it is not obtained by extending the old source beyond its finite boundary.

Consequently, **conditional on the inherited Turn 13 endpoint interface and the provisionally parent-reviewed Turn 18 terminal-module theorem**, the complete return is evaluated:


$$
\boxed{
g_T^TE_c^{-1}b_I\in3^{30}\mathbb Z_3,
\qquad
\eta_{k-1}=0.
}
\tag{D}
$$



The dependency in (D) is important. Turn 18’s new uniform transition theorem still awaits a DIFFERENT audit. This report proves the additional source and LOW-return statements needed to apply it at $I$; it does not declare that audit completed. The older finite matrix gradings are reused at their independently admitted scope.

After the endpoint calculation, one concrete physical-$6$ consequence is derived in the existing common pivot frame. The other coordinates of $\eta$, the first-four return, physical $7$/source $34$, primitive normalization, and the whole nonzero real error remain separate obligations.

---

## 1. Original domain, boundaries, and complete columns

All assertions concern sufficiently large members of exactly the original family


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
P=3^{h-32},\qquad P_0=243P,\qquad N_0=243r,
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


so


$$
N_0=25P+2\chi,\qquad D=268P+2\chi.
$$



The subwindow remains


$$
\boxed{\frac3{25}<\frac{\chi}{P}<\frac{31}{250}.}
\tag{1.1}
$$


No independent experimental choices of $P,\chi$, or $I$ are made.

Write


$$
S=h-32,\qquad P=3^S,\qquad H=3^{S+31},
\qquad S\ge31,
$$


and


$$
\Pi=P/3,\qquad t=\Pi-2\chi,\qquad
k=3\chi-\Pi-1,\qquad I=k-1.
$$


The retained arithmetic gives


$$
v_3(\chi)=5,\qquad \chi/243\equiv1\pmod9,
$$


hence


$$
v_3(D)=v_3(t)=v_3(A)=5.
\tag{1.2}
$$



Two exact endpoint identities will be used repeatedly:


$$
\boxed{t+I=\chi-2,\qquad I\equiv25\pmod{27}.}
\tag{1.3}
$$


The second follows from the first displayed formula for $I$, since $27\mid\chi,\Pi$. Moreover,


$$
\frac{2P}{75}-2<I<\frac{29P}{750}-2,
\tag{1.4}
$$


so $I\ge0$ in the retained sufficiently large domain.

### 1.1 Literal finite spaces

Set $x=y-1$. The original spaces are


$$
U_u=x^u,\qquad 0\le u<D,
$$




$$
z_i^{\rm mid}=x^Dy^i,\qquad 0\le i<\nu,
\qquad \nu=D/2-1=134P+\chi-1,
$$


and


$$
Y_s=y^s,\qquad d\le s\le m,
\qquad d=D+\nu=402P+3\chi-1.
$$


Thus


$$
m+\nu=r_H,\qquad r_H=\frac{H-1}{2}.
\tag{1.5}
$$



The physical HIGH terminal is $Y_m$. The last middle polynomial is $y^{\nu-1}$. They remain different objects.

The finite prefix and tail boundaries remain


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


The endpoint unit is


$$
a=\overline B_{\ell,\tau-1}\ne0.
$$



### 1.2 Complete functional and corrected columns

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
$$



The core producer and form are


$$
Q_c=(y+1)x^A(\beta+3y),
\qquad
\beta=D-H-71,
$$




$$
G_c(f,g)=\mathcal M(Q_cfg),
\qquad W=[U\ Y],
\qquad E_c=G_c(W,W).
$$


The complete $W$-corrected column is


$$
\boxed{
F[p]=x^Dp-WE_c^{-1}G_c(W,x^Dp).
}
\tag{1.6}
$$



The exact finite block decomposition is


$$
E_c=
\begin{pmatrix}
3\mathcal L&3\mathcal X\\
3\mathcal X^T&E_Y
\end{pmatrix},
$$




$$
M_L=\mathcal L^{-1},
\qquad
\boxed{\mathcal S_H=E_Y-3\mathcal X^TM_L\mathcal X},
\qquad
M_H=\mathcal S_H^{-1}.
\tag{1.7}
$$


The established unit results give integral $M_L,M_H$. The physical LOW inverse costs $3^{-1}$; it is not replaced by $M_L$ without its normalization.

---

## 2. Start from the complete Turn 13 residual identity

Retain


$$
\begin{aligned}
\Omega_P(y)={}&
(1-y)^{2P}\bigl(y^{122P}+3y^{41P}\bigr)\\
&+9(1+y^P+y^{2P})
\bigl(2y^{14P}+2y^{41P}+2y^{95P}-y^{131P}\bigr).
\end{aligned}
\tag{2.1}
$$


For every original coordinate,


$$
p_i=\Omega_P(y)(1-y)^t y^i.
$$



The inherited complete residual identity is


$$
\boxed{
a\eta_i
=
-\frac{G_c(F[y^{\nu-1}],F[p_i])}{3^{29}}
\pmod3.
}
\tag{2.2}
$$


Its provenance includes the original prefix inverse image and the finite interior $J$-return. Those corrections are not reconstructed or omitted here.

Put


$$
g_T=G_c(W,x^Dy^{\nu-1}),\qquad
b_I=G_c(W,x^Dp_I).
$$


The exact stationary identity is


$$
G_c(F[y^{\nu-1}],F[p_I])
=
G_c(x^Dy^{\nu-1},x^Dp_I)-g_T^TE_c^{-1}b_I.
\tag{2.3}
$$


Turn 13’s admitted bare endpoint calculation gives


$$
G_c(x^Dy^{\nu-1},x^Dp_I)\in3^{30}\mathbb Z_3.
$$


Therefore the correct starting target is


$$
\boxed{
a\eta_I
=
\frac{g_T^TE_c^{-1}b_I}{3^{29}}
\pmod3.
}
\tag{2.4}
$$



This quotient is integral by the inherited interface. Its numerator must be controlled modulo $3^{30}$, with the whole $W$-return present.

### 2.1 All fourteen terms

Write


$$
p_I=
\sum_{(\Delta,b,c)\in\mathcal T}
c(1-y)^{t+\Delta}y^{bP+I},
\tag{2.5}
$$


with the complete table


$$
\begin{array}{c|c|c|c}
\Delta&b&c&v_3(c)\\ \hline
2P&122&1&0\\
2P&41&3&1\\
0&14,15,16&18&2\\
0&41,42,43&18&2\\
0&95,96,97&18&2\\
0&131,132,133&-9&2.
\end{array}
\tag{2.6}
$$


For each term, both channels $\epsilon=0,1$ retain the multiplier


$$
c\,\beta^{1-\epsilon}3^\epsilon.
\tag{2.7}
$$


In particular, the twelve terms carrying $9$ are retained in the deep bulk estimates even when they are invisible in a two-digit source grading.

---

## 3. The normalized sources: exact formulas and paid divisions

Define


$$
g_T=3\binom{\alpha_T}{\upsilon_T},
\qquad
b_I=\binom{3\alpha_I}{9f_I},
\qquad
f_I=f_H(I).
\tag{3.1}
$$


Thus


$$
\alpha_T=\frac{G_c(U,x^Dy^{\nu-1})}{3},
\quad
\upsilon_T=\frac{G_c(Y,x^Dy^{\nu-1})}{3},
$$




$$
\alpha_I=\frac{G_c(U,x^Dp_I)}3,
\quad
f_I=\frac{G_c(Y,x^Dp_I)}9.
\tag{3.2}
$$



The integrality of the new division by $9$, and the source-specific depth of $\alpha_I$, must be proved. They do not follow merely from the corresponding assertions for $p_0$.

### 3.1 An integral change of LOW coordinates, not a replacement LOW space

For grading arguments only, use the monomial LOW basis


$$
\widetilde U_u=y^u,\qquad 0\le u<D.
$$


If $\widetilde U=UC$, then


$$
C_{r,u}=\binom ur
$$


is integral unimodular. Consequently


$$
\widetilde{\mathcal L}=C^T\mathcal LC,\qquad
\widetilde{\mathcal X}=C^T\mathcal X,
$$




$$
\widetilde M_L=C^{-1}M_LC^{-T},
\qquad
\widetilde\alpha=C^T\alpha.
$$


In particular,


$$
\widetilde{\mathcal X}^{\,T}\widetilde M_L\widetilde\alpha
=\mathcal X^TM_L\alpha,
\tag{3.3}
$$


and


$$
E_Y-3\widetilde{\mathcal X}^{\,T}
\widetilde M_L\widetilde{\mathcal X}
=\mathcal S_H.
\tag{3.4}
$$


All LOW/HIGH contractions below are therefore contractions in the original finite objects.

### 3.2 The evaluated beta ratio

Use the established exact evaluation


$$
\mathcal B(N,q)
=
\frac{4^N N!(N+q)!(2q)!}
{q!(2N+2q+1)!}
$$


and its valuation formula


$$
\boxed{
v_3\mathcal B(N,q)
=
-\sum_{e\ge1}
\mathbf1_{\{N\bmod3^e\ge j_e(q)\}},
\qquad
j_e(q)=\left(\frac{3^e-1}{2}-q\right)\bmod3^e.
}
\tag{3.5}
$$


This is an evaluated factorial ratio, not an unevaluated source sum.

Because $Q_c(-1)=0$, the rational part of the new LOW source is exactly


$$
\boxed{
(\widetilde\alpha_I)_u
=
-3^{h-1}
\sum_{\mathcal T}\sum_{\epsilon=0}^1
c\,\beta^{1-\epsilon}3^\epsilon
\mathcal B(H+t+\Delta,u+bP+I+\epsilon)
+\mathcal F_{U,u},
}
\tag{3.6}
$$


where


$$
\mathcal F_{U,u}
=
-\frac{3^{h-1}}4
\mathfrak f(Q_cy^ux^Dp_I)
\in3^{h-1}\mathbb Z_3.
$$


Similarly,


$$
\boxed{
(f_I)_s
=
-3^{h-2}
\sum_{\mathcal T}\sum_{\epsilon=0}^1
c\,\beta^{1-\epsilon}3^\epsilon
\mathcal B(H+t+\Delta,s+bP+I+\epsilon)
+\mathcal F_{H,s},
}
\tag{3.7}
$$


with


$$
\mathcal F_{H,s}
=
-\frac{3^{h-2}}4
\mathfrak f(Q_cY_sx^Dp_I)
\in3^{h-2}\mathbb Z_3.
$$


The minus signs come from $x^H=-(1-y)^H$, since $H$ is odd.

### 3.3 The physical cutoff for the shifted source

The degree of the shifted source is


$$
\deg p_I=133P+t+I=133P+\chi-2.
$$


Hence


$$
\boxed{\deg(x^Dp_I)=d-P-1.}
\tag{3.8}
$$


At $Y_m$, including the $3y$-channel, the largest rational-polynomial degree is


$$
H+m+133P+\chi-1
=
\frac{3H-1}{2}-P.
\tag{3.9}
$$


Thus the pole $3H$ is absent from every entry of $G_c(Y,x^Dp_I)$. All fourteen terms remain within the actual physical cutoff.

For the LOW formula (3.6),


$$
(t+\Delta)+(u+bP+I+\epsilon)
\le
(268+b)P+3\chi+\Delta-3+\epsilon
<402P.
\tag{3.10}
$$


This also lies well inside the physical cutoff.

### Lemma 3.1 — The new HIGH division by $9$ is integral

For every original $d\le s\le m$,


$$
G_c(Y_s,x^Dp_I)\in9\mathbb Z_3.
$$



#### Proof

By (3.9), all odd denominators are below $3H$. Except at denominator $H$, the factor $3^h$ supplies at least two powers of $3$.

For one term and one channel, put


$$
N=H+n_0,\qquad n_0=t+\Delta,\qquad
q=s+bP+I+\epsilon.
$$


The coefficient at denominator $H$ has index


$$
r=r_H-q.
$$


Using $s\le m$ and $r_H-m=\nu$,


$$
r\ge\nu-bP-I-\epsilon
=(134-b)P+t+1-\epsilon.
$$


Therefore


$$
r-n_0\ge(134-b)P-\Delta+1-\epsilon\ge P.
\tag{3.11}
$$


Also $r<H$. Thus $n_0<r<H$, and


$$
(1-y)^{H+n_0}\equiv(1-y^H)(1-y)^{n_0}\pmod3
$$


has zero coefficient at $y^r$. The denominator-$H$ coefficient supplies the additional factor $3$.

The factorial contribution is divisible by $3^h$. This proves the division by $9$ for the complete source. ∎

---

## 4. New complete LOW source estimates and source gradings

For a LOW or HIGH index set, let the subscript $b$ denote support at indices congruent to $b\pmod{27}$. Write these modules as $\mathscr L_b$ and $\mathscr V_b$, respectively.

### Lemma 4.1 — The shifted LOW source, through its three required digits

One has


$$
\boxed{\alpha_I\in3^{25}\mathbb Z_3^D.}
\tag{4.1}
$$


More precisely, in the monomial LOW coordinates,


$$
\boxed{
3^{-25}\widetilde\alpha_I
\in
\mathscr L_{15}+3\mathscr L_{14}+27\mathbb Z_3^D.
}
\tag{4.2}
$$



#### Proof

In (3.6),


$$
N=H+t+\Delta,\qquad v_3(N)=5.
$$


By (3.10), every indicator above level $S+6$ is absent. Indeed, at levels $S+7,\ldots,S+31$,


$$
(t+\Delta)+q<402P<
\frac{3^{S+7}-1}{2},
$$


and at modulus $3H$ the half-modulus is still farther away.

For the first five indicators, $N\bmod3^e=0$. Their number is therefore exactly


$$
\min\{5,v_3(2q+1)\}.
$$


There are at most $S+1$ remaining indicators, at levels $6,\ldots,S+6$. Consequently the individual term in (3.6) has valuation at least


$$
\boxed{
30+v_3(c)+\epsilon-\min\{5,v_3(2q+1)\}.
}
\tag{4.3}
$$


This is at least $25+v_3(c)+\epsilon$, proving (4.1).

If $q\not\equiv13\pmod{27}$, then $v_3(2q+1)\le2$, and (4.3) is at least


$$
28+v_3(c)+\epsilon.
$$


Such an entry disappears after division by $3^{25}$, modulo $27$.

Since


$$
q=u+bP+I+\epsilon\equiv u+25+\epsilon\pmod{27},
$$


the visible $\beta$-channel has LOW grade $15$, and the visible $3y$-channel has LOW grade $14$ with its additional factor $3$.

This argument includes the $c=3$ term and all twelve $v_3(c)=2$ terms. For example, the latter can still contribute at depth $27$ in the $\beta$-channel; they have not been removed from the three-digit LOW source. The factorial contribution is much deeper. ∎

### Lemma 4.2 — The shifted HIGH grading

The complete integral source satisfies


$$
\boxed{
f_I\in\mathscr V_{15}+3\mathscr V_{14}+9\mathscr V.
}
\tag{4.4}
$$



#### Proof

The division by $9$ has just been proved term by term. In the normalized coefficient functional, a denominator contributes weight


$$
3^{h-2}/(2v+1).
$$


Its smallest possible valuation is $-1$, occurring at denominator $H$.

Every pole visible modulo $9$ has $v\equiv13\pmod{27}$. For the coefficient index


$$
r=v-(s+bP+I+\epsilon),
$$


if $27\nmid r$, then, for $0<r\le N$,


$$
v_3\binom Nr
\ge v_3(N)-v_3(r)\ge3.
$$


Indices outside $0,\ldots,N$ give zero. Thus even the weight of valuation $-1$ leaves valuation at least $2$.

A visible coefficient therefore requires


$$
s+bP+I+\epsilon\equiv13\pmod{27}.
$$


Using $I\equiv25$, the grades are $15$ and $14$, respectively. The second channel retains its factor $3$.

This proof applies directly on $d\le s\le m$, including both ends. No value of the old source at $s+I>m$ is invoked. ∎

### 4.1 The unchanged terminal source: its required grading

Let


$$
\kappa(q)=-3H\mathcal B(H,q).
$$


The actual normalized terminal source has rational part


$$
\boxed{
(\upsilon_T)_s
=
\frac{\beta\kappa(s+\nu-1)}3+\kappa(s+\nu)
+\text{factorial term}.
}
\tag{4.5}
$$



For $q<r_H$,


$$
v_3\kappa(q)=S+32-v_3(2q+1),
$$


while $\kappa(r_H)$ is a unit. In (4.5), the $\beta$-argument is always below $r_H$; the second argument equals $r_H$ exactly at $s=m$. Thus the physical terminal unit is retained.

The visible $\beta$-channel is divisible by $3$ and has grade


$$
13-(\nu-1)\equiv15.
$$


The second channel has grade


$$
13-\nu\equiv14,
$$


including its unit at $Y_m$. Hence


$$
\boxed{
\upsilon_T\in
\mathscr V_{14}+3\mathscr V_{15}+27\mathscr V.
}
\tag{4.6}
$$



Likewise, for the LOW terminal source, the same formula with $s=u$, $0\le u<D$, has both arguments below $r_H$. Since


$$
2(u+\nu)+1<3D<2187P=3^{S+7},
$$


it gives the reused depth bound


$$
\alpha_T\in3^{25}\mathbb Z_3^D
$$


and the source-specific grading


$$
\boxed{
3^{-25}\widetilde\alpha_T
\in\mathscr L_{15}+3\mathscr L_{14}+9\mathbb Z_3^D.
}
\tag{4.7}
$$



No LOW48 calculation is used or repeated.

---

## 5. Finite matrix grading rules needed for the complete LOW returns

The old finite matrix gradings are admitted at the current complete-core premises. The following records the precise consequences needed here, including the true Schur return.

A matrix is **reflection-graded by $r$** if it maps grade $b$ to grade $r-b$. A matrix is **shift-graded by $r$** if it maps grade $b$ to grade $b+r$.

In the monomial LOW coordinates, the finite blocks satisfy, modulo $27$,


$$
\widetilde{\mathcal L}\equiv L_0+3L_1,\qquad
\widetilde{\mathcal X}\equiv X_0+3X_1,\qquad
E_Y\equiv Y_0+3Y_1,
\tag{5.1}
$$


where the subscript $0$ matrices are reflection-graded by $13$, and the subscript $1$ matrices by $12$.

For completeness, applicability to the unchanged objects can be checked without any old table computation. The LOW/LOW and LOW/HIGH normalizations avoid the pole $3H$; the HIGH/HIGH normalization retains it. Every pole visible modulo $27$ has exponent $13\pmod{27}$. Since $v_3(A)=5$,


$$
27\nmid r\quad\Longrightarrow\quad
v_3\binom Ar\ge3.
$$


Thus the $\beta$-channel has grade $13$, and the $3y$-channel has grade $12$ with its explicit factor $3$. The finite row and column masks preserve these support statements. The factorial terms are too deep at this precision.

Since $L_0$ is a unit, inversion gives


$$
\widetilde M_L
\equiv M_{L,0}+3M_{L,1}+9M_{L,2}\pmod{27},
\tag{5.2}
$$


where $M_{L,j}$ is reflection-graded by $13+j$.

Now the complete LOW matrix return satisfies


$$
\widetilde{\mathcal X}^{\,T}
\widetilde M_L\widetilde{\mathcal X}
\equiv Z_0+3Z_1+9Z_2\pmod{27},
$$


where $Z_j$ is reflection-graded by $13-j$. Therefore


$$
\mathcal S_H
\equiv (Y_0-3Z_0)+3(Y_1-3Z_1)\pmod{27}.
\tag{5.3}
$$


In particular, the grade-$13$ part here contains the appropriate LOW matrix return. It is not $E_Y$ alone.

The resulting inverse rules are


$$
\boxed{
M_H\equiv M_{H,0}+3M_{H,1}+9M_{H,2}\pmod{27},
}
\tag{5.4}
$$


with reflection grades $13,14,15$, and


$$
\boxed{
\widetilde{\mathcal X}^{\,T}\widetilde M_L
\equiv T_0+3T_1+9T_2\pmod{27},
}
\tag{5.5}
$$


where $T_j$ shifts grade by $-j$.

These are finite inverse consequences of the admitted unit blocks and their actual gradings, not an infinite convolution substitution.

---

## 6. Evaluation of every additional LOW source contraction

Set


$$
v_T=M_H\upsilon_T,
\qquad
d_T=\mathcal X^TM_L\alpha_T,
\qquad
d_I=\mathcal X^TM_L\alpha_I.
\tag{6.1}
$$



### 6.1 Exact block elimination

The exact Schur pairing is


$$
\boxed{
g_T^TE_c^{-1}b_I
=
3\alpha_T^TM_L\alpha_I
+
27(\upsilon_T-d_T)^TM_H
\left(f_I-\frac{d_I}{3}\right).
}
\tag{6.2}
$$


The additional division by $3$ is paid:


$$
d_I\in3^{25}\mathscr V,
\qquad d_I/3\in3^{24}\mathscr V.
$$


Expanding (6.2),


$$
\begin{aligned}
g_T^TE_c^{-1}b_I={}&
27v_T^Tf_I
+3\alpha_T^TM_L\alpha_I\\
&-9v_T^Td_I
-27d_T^TM_Hf_I
+9d_T^TM_Hd_I.
\end{aligned}
\tag{6.3}
$$


These are all the LOW source terms. The two mixed terms cannot be discarded just from the depth-$25$ bounds; their contractions require additional proof.

### Lemma 6.1 — The new source-side LOW return is annihilated

One has


$$
\boxed{v_T^Td_I\in3^{28}\mathbb Z_3.}
\tag{6.4}
$$



#### Proof

From (4.6) and the finite inverse grading (5.4),


$$
v_T
\in
\mathscr V_{26}
+3\mathscr V_{25}
+3\mathscr V_0
+9\mathscr V_1
+27\mathscr V.
\tag{6.5}
$$


Indeed, applying reflection grades $13,14,15$ to terminal grade $14$ produces grades $26,0,1$; applying them to the factor-$3$ grade $15$ produces grades $25,26$ at the visible precisions.

From (4.2) and the actual LOW-return map (5.5),


$$
3^{-25}d_I
\in
\mathscr V_{15}
+3\mathscr V_{14}
+9\mathscr V_{13}
+27\mathscr V.
\tag{6.6}
$$


The visible support sets


$$
\{26,25,0,1\},\qquad \{15,14,13\}
$$


are disjoint modulo $27$. Hence


$$
v_T^T(3^{-25}d_I)\equiv0\pmod{27},
$$


which is exactly (6.4). ∎

### Lemma 6.2 — The terminal-side LOW return is annihilated

One has


$$
\boxed{d_T^TM_Hf_I\in3^{27}\mathbb Z_3.}
\tag{6.7}
$$



#### Proof

Equations (4.7) and (5.5), now modulo $9$, give


$$
3^{-25}d_T\in
\mathscr V_{15}+3\mathscr V_{14}+9\mathscr V.
\tag{6.8}
$$


Equations (4.4) and (5.4) give


$$
M_Hf_I\in
\mathscr V_{25}+3\mathscr V_{26}+9\mathscr V.
\tag{6.9}
$$


Their visible grades are disjoint. Thus their pairing is zero modulo $9$, proving (6.7). ∎

The remaining two terms in (6.3) satisfy


$$
3\alpha_T^TM_L\alpha_I\in3^{51}\mathbb Z_3,
$$




$$
9d_T^TM_Hd_I\in3^{52}\mathbb Z_3.
$$


Together with (6.4)–(6.7), this proves the new complete reduction


$$
\boxed{
g_T^TE_c^{-1}b_I
\equiv27v_T^Tf_I\pmod{3^{30}}.
}
\tag{6.10}
$$



This completes the extra LOW-source obligation before any application of the Turn 18 annihilator.

There are two distinct LOW mechanisms here:

* the operator return $-3\mathcal X^TM_L\mathcal X$, retained in the true $\mathcal S_H$;
* the source returns $d_T,d_I$, whose complete contractions have just been evaluated.

The first does not imply the second. Both have now been paid at their required scopes.

---

## 7. The unchanged terminal module and the shifted whole-source annihilator

The terminal response $v_T=M_H\upsilon_T$ has not changed. The test source has.

Set


$$
B_\circ=\frac{H}{3^{24}}=2187P,
\qquad
C_\circ=\frac{3^{24}-1}{2}.
\tag{7.1}
$$


The original inequalities give


$$
B_\circ>4D+60,\qquad B_\circ/2>540P,\qquad \nu>28.
\tag{7.2}
$$



For


$$
b_j=\binom{D+j-1}{j},
$$


retain the exact finite quotients


$$
P_{d+a}(y)=\sum_{j=0}^{\nu+a}b_jy^{\nu+a-j},
\qquad
y^{d+a}=C_{d+a}+x^DP_{d+a},
\quad \deg C_{d+a}<D.
\tag{7.3}
$$



The Turn 18 bulk module $\mathscr B$ is the span of


$$
\mathsf T_{a,v}
=
3^{(a-1)_+}
\operatorname{pr}_{[d,m]}
\left(x^Dy^{vB_\circ+\nu-1+a}\right),
\quad 0\le a\le27,
$$




$$
\mathsf Q_{a,v}
=
3^a
\operatorname{pr}_{[d,m]}
\left(x^Dy^{vB_\circ}P_{d+a}\right),
\quad 0\le a\le26,
$$




$$
\mathsf O_{a,v}
=
3^a
\operatorname{pr}_{[d,m]}
\left(x^Dy^{vB_\circ+a}\right),
\quad 0\le a\le26,
\tag{7.4}
$$


where $0\le v\le C_\circ$.

No grid coefficients are enumerated.

### 7.1 Literal boundary behavior

For $1\le v\le C_\circ$, the polynomials in (7.4) are wholly inside the original HIGH interval. At $v=0$,


$$
\mathsf Q_{a,0}=3^ay^{d+a},
\qquad
\mathsf O_{a,0}=0,
$$


and, for $a\ge1$,


$$
\mathsf T_{a,0}
=
3^{a-1}\sum_{b=0}^{a-1}
(-1)^{a-1-b}\binom D{a-1-b}y^{d+b},
\tag{7.5}
$$


while $\mathsf T_{0,0}=0$.

These are the same finite masks as in Turn 18. Multiplying the test source by $y^I$ does not change the terminal module or these boundaries.

### Theorem 7.1 — Shifted whole-source bulk annihilation

For the actual complementary source,


$$
\boxed{\mathscr B^Tf_I\subseteq3^{29}\mathbb Z_3.}
\tag{7.6}
$$



#### Proof

It suffices to treat the displayed generators. Every source term retains $c\beta^{1-\epsilon}3^\epsilon$, and the functional divided by $9$ has scale


$$
3^{h-2}=3^{S+30}.
\tag{7.7}
$$



### 7.2 Exact shifted beta arguments

For an interior generator, put


$$
N=H+D+t+\Delta
=H+268P+\Pi+\Delta.
\tag{7.8}
$$


Thus $v_3(N)=S-1$.

The actual arguments and fixed low integers are:


$$
\begin{array}{c|l|c}
\text{family}&q&\text{fixed part of }2q+1\\ \hline
\mathsf T_{a,v}
&
vB_\circ+(134+b)P-\Pi+4\chi-4+a+\epsilon
&
2a+2\epsilon-7
\\[1mm]
\mathsf O_{a,v}
&
vB_\circ+bP-\Pi+3\chi-2+a+\epsilon
&
2a+2\epsilon-3
\\[1mm]
\mathsf Q_{a,v},\ \text{coefficient }b_j
&
vB_\circ+(134+b)P-\Pi+4\chi-3+a-j+\epsilon
&
2a+2\epsilon-5-2j .
\end{array}
\tag{7.9}
$$


These follow by inserting $I=3\chi-\Pi-2$, not by a guessed modular shift.

For the lower-edge monomial $y^{d+a}$,


$$
N=H+t+\Delta,\qquad v_3(N)=5,
$$




$$
q=(402+b)P-\Pi+6\chi-3+a+\epsilon.
\tag{7.10}
$$


Its fixed low integer is again


$$
\boxed{2a+2\epsilon-5.}
\tag{7.11}
$$



Thus the diagnostic shift from $-1$ to $-5$ in the quotient and boundary estimates is correct, but only after the exact arguments have been derived.

### 7.3 Safe-grid bounds and all high indicators

Write $q=vB_\circ+q_{\rm lo}$, $N=H+N_{\rm lo}$. In the terminal and quotient cases,


$$
N_{\rm lo}+q_{\rm lo}
\le535P+4\chi+24<536P.
$$


In the ordinary case,


$$
N_{\rm lo}+q_{\rm lo}
\le401P+3\chi+25<402P.
$$


The edge case also has


$$
N-H+q<536P.
$$


Consequently, uniformly for all fourteen source terms and both channels,


$$
\boxed{N_{\rm lo}+q_{\rm lo}<540P<B_\circ/2.}
\tag{7.12}
$$



For $S+7\le e\le S+31$, the modulus $3^e$ is an odd multiple of $B_\circ$. The least residue $j_e(q)$ has residue


$$
\frac{B_\circ-1}{2}-q_{\rm lo}>N_{\rm lo}
$$


modulo $B_\circ$. Therefore $j_e(q)>N\bmod3^e$.

At modulus $3H$,


$$
q\le\frac{H-B_\circ}{2}+q_{\rm lo},
$$


so


$$
\frac{3H-1}{2}-q
>
H+N_{\rm lo}.
$$


All higher indicators are also absent.

Only the first $S+6$ levels can contribute.

### 7.4 Interior terminal and ordinary families

For $\mathsf T_{a,v}$, the first $S-1$ indicators count


$$
v_3(2a+2\epsilon-7)\le3.
$$


For $\mathsf O_{a,v}$, they count


$$
v_3(2a+2\epsilon-3)\le3.
$$


The remaining terms in $2q+1$ have valuation at least $5$, and the displayed fixed integers are nonzero and have absolute value below $81$.

There are only seven intervening indicators. Hence these contractions have valuation at least


$$
S+30-10=S+20\ge51,
$$


before including their nonnegative weights and source coefficients.

### 7.5 Every coefficient of the finite quotients

For a quotient coefficient $b_j$, set


$$
u=a+\epsilon,\qquad
\omega=2u-5,\qquad
\lambda=v_3(\omega)\le3.
\tag{7.13}
$$


If $v_3(j)\ne\lambda$, including $j=0$, then


$$
v_3(2q+1)\le\lambda,
$$


so the term is much deeper than required.

If $v_3(j)=\lambda$, use the exact identity


$$
b_j=\frac Dj\binom{D+j-1}{j-1}.
$$


It gives


$$
v_3(b_j)\ge5-\lambda.
\tag{7.14}
$$


Allowing every one of the first $S-1$ indicators and all seven intermediate indicators, the valuation of the weighted term is at least


$$
\begin{aligned}
&S+30+a+\epsilon+v_3(c)+(5-\lambda)-(S+6)\\
&\hspace{15mm}
=29+a+\epsilon+v_3(c)-\lambda.
\end{aligned}
\tag{7.15}
$$



The required new inequality is


$$
\boxed{v_3(2u-5)\le u\qquad(u\ge0).}
\tag{7.16}
$$


For $u=0,1,2$, the valuations are $0,1,0$. For $u\ge3$,


$$
0<2u-5<3^u,
$$


so the inequality follows. Therefore (7.15) is at least $29$.

This proves the whole finite quotient estimate. No quotient tail is omitted.

### 7.6 Complete lower-edge contraction

For $3^ay^{d+a}$, use (7.10). The first five indicators contribute


$$
\lambda=v_3(2a+2\epsilon-5)\le3.
$$


There are at most $S+1$ further indicators. Thus the valuation is at least


$$
S+30+a+\epsilon+v_3(c)-(S+1+\lambda)
=
29+a+\epsilon+v_3(c)-\lambda
\ge29.
\tag{7.17}
$$



In (7.5), the weight $3^{a-1}$ pays $3^b$ for every $b\le a-1$. Consequently the entire literal lower mask satisfies the same bound.

### 7.7 Physical cutoff and factorial part

Every interior contraction used above has


$$
N+q
\le
H+\frac{H-B_\circ}{2}+540P
<
\frac{3H}{2}
<
K_{\rm phys}.
\tag{7.18}
$$


The edge contractions are smaller.

The factorial contribution after division by $9$ belongs to


$$
3^{h-2}\mathbb Z_3=3^{S+30}\mathbb Z_3.
$$


All finite quotient coefficients, generator weights, and source coefficients are integral. Summing the complete fourteen-term, two-channel source cannot lower the proved common bound.

This proves (7.6). ∎

---

## 8. Exceptional jets, both HIGH ends, and the conditional terminal theorem

Retain the Turn 18 exceptional module


$$
\boxed{
\mathscr E=
\mathscr V_{25}+\mathscr V_{26}+\mathscr V_0
+3\mathscr V_1+9\mathscr V.
}
\tag{8.1}
$$


The newly derived source grading (4.4) immediately gives


$$
\boxed{\mathscr E^Tf_I\subseteq9\mathbb Z_3,}
\tag{8.2}
$$


because its visible grades $25,26,0,1$ are disjoint from $15,14$.

Set


$$
\mathscr N=\mathscr B+3^{25}\mathscr E+3^{27}\mathscr V.
$$


The new bulk theorem and (8.2) give


$$
\boxed{\mathscr N^Tf_I\subseteq3^{27}\mathbb Z_3.}
\tag{8.3}
$$



### 8.1 Exact dependency on Turn 18

The terminal-only result needed from Turn 18 is the following statement about the unchanged original finite operator:


$$
\mathcal K_H\upsilon_T\in\mathscr N,\qquad
(\mathcal K_H\mathcal S_H)\mathscr N\subseteq\mathscr N,
\tag{8.4}
$$


where


$$
V_{\mathcal K_Hv}(y)
=
\operatorname{pr}_{[d,m]}
\left(x^Dy^{r_H}V_v(y^{-1})\right),
\qquad
\mathcal K_H\mathcal S_H\equiv I\pmod3.
$$



This is precisely the provisionally parent-reviewed Turn 18 transition theorem. Its DIFFERENT audit remains pending.

Since $\mathscr N$ contains $3^{27}\mathscr V$, finite inversion of an operator congruent to the identity modulo $3$ in the quotient $\mathscr V/3^{27}\mathscr V$ gives


$$
\boxed{v_T=M_H\upsilon_T\in\mathscr N.}
\tag{8.5}
$$


This is only a module-membership consequence of the admitted transition law. It is not a proposal to execute original-length inverse updates.

The Turn 18 statement retains:

* the literal lower and upper HIGH masks;
* the physical resonance in the $3y$-terminal channel;
* the upper interaction at the $729P$ grid;
* both-edge interactions at the $243P$ grid;
* the true operator $\mathcal S_H=E_Y-3\mathcal X^TM_L\mathcal X$.

The new source pairs to zero with the complete exceptional module through the required two digits. Thus neither HIGH end leaves a nonannihilating jet at this precision.

### 8.2 The unchanged residual has not lost a LOW return

For clarity, the reused terminal certificate retains the exact residual


$$
\begin{aligned}
r_2={}&
\frac{\delta_{\rm raw}-G_c(Y,x^DP_*)
-3G_c(Y,x^DP^{[1]})}{9}\\
&+\frac19\mathcal X^TM_L\alpha_d
+\frac13\mathcal X^TM_L\alpha_*
+\mathcal X^TM_L\alpha_{[1]},
\end{aligned}
\tag{8.6}
$$


where


$$
\delta_{\rm raw}
=\frac{\upsilon_T-G_c(Y,x^DP_d)}3,
$$




$$
P_*=y^{H/3+\nu-1}-P_{d+1},
$$




$$
\begin{aligned}
P^{[1]}={}&
y^{4H/9+\nu-1}-y^{2H/9+\nu-1}+y^{H/9+\nu-1}\\
&-y^{H/3}P_d+P_{d+2}-P_d,
\end{aligned}
$$


and


$$
\alpha_d=\frac{G_c(U,x^DP_d)}3,\quad
\alpha_*=\frac{G_c(U,x^DP_*)}3,\quad
\alpha_{[1]}=\frac{G_c(U,x^DP^{[1]})}3.
$$


At the inherited precision,


$$
r_2\equiv
\frac{\delta_{\rm raw}-G_c(Y,x^DP_*)
-3G_c(Y,x^DP^{[1]})}{9}
+3^{23}R_d
\pmod{3^{24}}.
\tag{8.7}
$$


The $3^{23}R_d$ term remains. Its cumulative depth-$26$ effect is covered by the true-operator terminal theorem; it is not deleted before inversion.

---

## 9. Evaluation of the complementary endpoint

Combining (8.3) and (8.5),


$$
\boxed{v_T^Tf_I\in3^{27}\mathbb Z_3.}
\tag{9.1}
$$


The complete LOW/HIGH reduction (6.10) now gives


$$
\boxed{g_T^TE_c^{-1}b_I\in3^{30}\mathbb Z_3.}
\tag{9.2}
$$


By the unchanged Turn 13 residual identity,


$$
\boxed{\eta_{k-1}=0.}
\tag{9.3}
$$



Equivalently, the completely corrected pairing itself satisfies


$$
\boxed{
G_c(F[y^{\nu-1}],F[p_I])\in3^{30}\mathbb Z_3.
}
\tag{9.4}
$$



These are uniform statements at the same original indices, with the dependencies stated in Section 8. They are not finite sample conclusions.

### 9.1 Compatibility with the $w_2$ normalization

The unchanged terminal decomposition is


$$
v_T=V^{(0)}+27w_2,
\qquad
V^{(0)}=e_d+3z_0+9\widehat z_1.
$$


The established displayed directions give $V^{(0)}\in\mathscr B$. The new bulk theorem therefore proves


$$
(V^{(0)})^Tf_I\in3^{29}\mathbb Z_3.
$$


Together with (9.1),


$$
\boxed{w_2^Tf_I\in3^{24}\mathbb Z_3.}
\tag{9.5}
$$



Only after the new LOW-source reduction has been paid is it legitimate to write


$$
\boxed{
a\eta_I=\frac{w_2^Tf_I}{3^{23}}\pmod3.
}
\tag{9.6}
$$


Thus the familiar-looking final normalization is valid at the complementary endpoint, but its validity is a conclusion of the new derivation, not an automatic reuse of the $\eta_0$ reduction.

---

## 10. One physical-$6$ consequence, with the other $\eta$-coordinates retained

The previously accepted core endpoint value is $\eta_0=0$, at its inherited interface scope. Together with the new complementary value,


$$
\eta_0=\eta_{k-1}=0.
\tag{10.1}
$$


No assertion is made about $\eta_1,\ldots,\eta_{k-2}$.

Retain


$$
C_6=C^0-\bigl(e_{k-1}\eta^T+\eta e_{k-1}^T\bigr),
\qquad
C^0=C^{\rm mom}-R_4,
$$




$$
R_4=C_H^TA_4^{-1}C_H,
$$


and the same common pivot frame


$$
B_6=N^TC_6N,\qquad
w_6=\bar\gamma N^TC_6e_0,
$$


where the columns of $N$ are $e_j+e_{j+1}$.

Let


$$
z_{\rm alt}=(1,-1,1,\ldots,(-1)^{k-2})^T,
\qquad
\varepsilon_{\rm alt}=(-1)^{k-2}.
$$


Then


$$
Nz_{\rm alt}=e_0+\varepsilon_{\rm alt}e_{k-1}.
\tag{10.2}
$$


Put $h=N^T\eta$. The two endpoint values imply the new explicit relation


$$
\boxed{z_{\rm alt}^Th=0.}
\tag{10.3}
$$



Writing $B^0=N^TC^0N$ and $w^0=\bar\gamma N^TC^0e_0$, one obtains the concrete directional identities


$$
\boxed{
B_6z_{\rm alt}=B^0z_{\rm alt}-\varepsilon_{\rm alt}h,
\qquad
w_6=w^0,
}
\tag{10.4}
$$


and therefore


$$
\boxed{
z_{\rm alt}^TB_6z_{\rm alt}
=z_{\rm alt}^TB^0z_{\rm alt}.
}
\tag{10.5}
$$


The unknown vector $h$ remains in the full directional equation (10.4). The quadratic cancellation is not a license to delete the terminal coupling.

There is a further explicit simplification of this one scalar. Since $243\mid t$,


$$
(1-y)^t\in\mathbb F_3[y^{243}].
$$


For


$$
\kappa_2=\frac{P/9-1}{2},
\qquad I=k-1,
$$


the three endpoint moment indices have residues


$$
\kappa_2\equiv121,\qquad
\kappa_2-I\equiv123,\qquad
\kappa_2-2I\equiv125\pmod{243}.
$$


None is divisible by $243$. Hence the endpoint $2\times2$ block of $C^{\rm mom}$ is zero, and


$$
\boxed{
z_{\rm alt}^TB_6z_{\rm alt}
=
-\bigl(
(R_4)_{00}
+2\varepsilon_{\rm alt}(R_4)_{0I}
+(R_4)_{II}
\bigr).
}
\tag{10.6}
$$



This is a concrete next first-four directional consequence in the original frame. It isolates an actual first-four returned scalar; it does not evaluate that scalar or solve the paid direction.

The first-four cross remains


$$
P_{ui}=\frac{d_u^T\mathsf A^{-1}d_H{}_i}{3}\pmod3,
$$




$$
(C_H)_{ui}
=
-c_{P-1-u-i-\Pi}
+c_{P-1-u-i-2\Pi}
-2\,\mathbf1_{u=R,\ i=I}
-P_{ui}.
\tag{10.7}
$$


The original finite $A_4^{-1}$, the mixed-prefix division, and the upper $3y$ corner are all still present.

The later direction is still


$$
B_6x=w_6,\qquad x\in3^{-1}\mathbb Z_3^{k-1}.
$$


A leading quadratic identity such as (10.6) does not settle that allowance.

---

## 11. Precision ledger

The key payments are as follows.

| Quantity or conclusion | Division/payment | Required precision or proved depth |
|---|---:|---|
| Inherited endpoint quotient | $3^{29}$ | Whole numerator modulo $3^{30}$ |
| $\alpha_I$ | $3$ | $G_c(U,x^Dp_I)\in3^{26}$ |
| $3^{-25}\widetilde\alpha_I\bmod27$ | $3^{26}$ from raw source | Raw LOW source modulo $3^{29}$ |
| $3^{-25}\widetilde\alpha_T\bmod9$ | $3^{26}$ from raw source | Raw terminal LOW source modulo $3^{28}$ |
| $f_I$ | $9$ | Integrality proved in Lemma 3.1 |
| $d_I/3$ | $3$ | $d_I\in3^{25}$, so quotient is in $3^{24}$ |
| Source-side mixed term | $9v_T^Td_I$ | $v_T^Td_I\in3^{28}$, whole term in $3^{30}$ |
| Terminal-side mixed term | $27d_T^TM_Hf_I$ | Pairing in $3^{27}$, whole term in $3^{30}$ |
| Direct LOW term | $3\alpha_T^TM_L\alpha_I$ | In $3^{51}$ |
| Double LOW return | $9d_T^TM_Hd_I$ | In $3^{52}$ |
| Bulk contraction | Functional divided by $9$ | Whole contraction in $3^{29}$ |
| Exceptional contraction | $3^{25}\mathscr E$ | Two source digits give $3^{27}$ |
| Unshortened HIGH route | $v_T^Tf_I\bmod3^{27}$ | If produced coefficientwise, raw HIGH source modulo $3^{29}$ |
| $w_2$ route after bulk payment | $f_I\bmod3^{24}$ | Raw HIGH source modulo $3^{26}$ |
| Final $w_2$ endpoint normalization | $3^{23}$ | Whole contraction proved in $3^{24}$ |

For the unchanged residual certificate, obtaining $r_2\bmod3^{24}$ after its division by $9$ requires its polynomial numerator modulo $3^{26}$. The preceding $\delta_{\rm raw}$ division by $3$ requires


$$
\upsilon_T-G_c(Y,x^DP_d)\pmod{3^{27}},
$$


and $\upsilon_T\bmod3^{27}$ requires its raw terminal source modulo $3^{28}$.

These are alternative symbolic precision routes, not instructions to construct original-length vectors.

---

## 12. Complete actual producer and later forcing remain separate

The result is for the complete core $Q_c$. The actual producer remains


$$
\boxed{Q_{\rm act}=Q_c+3^7\mathscr R.}
\tag{12.1}
$$


No equality between a core endpoint and an actual-producer endpoint is inferred without the required transport theorem.

Retain


$$
F_{\rm fac}=(n-1)!,
$$




$$
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},
\qquad 0\le a,b<n,
$$




$$
\gamma_0=1,\qquad \gamma_1=0,\qquad
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


The complete coefficients and endpoint remain


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



The full forcing identity remains


$$
\boxed{
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
}
\tag{12.2}
$$


Neither forcing term nor the physical terminal is removed.

The complete moment recurrence is


$$
\mu_{r+1}+\mu_r
=
\frac{3^h}{2r+1}
-\frac{3^h}{4}\bigl((2r+2)!+(2r)!\bigr),
\qquad 0\le r\le2n-2.
\tag{12.3}
$$


Retain the original shifted label $r_*=(3^h-5)/2$. In the recurrence as printed, the pole $2r+1=3^h$ occurs at $r=r_*+2$; any use of $r_*$ as a resonant-step label must retain that indexing shift. No such division is used or suppressed in the present local proof.

The factorial part was negligible only at the explicitly paid local ternary precisions. It has not been removed from the actual producer, recurrence, determinant, or real error.

At physical $7$, the remaining work still includes:

* the actual/core difference;
* the physical-$5$ complementary return;
* the physical-$5$ kernel-pivot directional return;
* higher endpoint adaptation and the next digits of earlier returns;
* the stationary contribution at source precision $34$.

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
\tag{12.4}
$$


No unit numerator is assumed.

---

## 13. Actual contents, least clearer, all-prime gcd, and whole error

No actual integer column content is evaluated by the endpoint cancellation. All contents remain those of the complete original construction.

The least simultaneous clearer is still the actual $\ell_{\rm clr}$, not a convenient common multiple or a power of $3$. Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,
\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the final gcd over **all primes**


$$
\boxed{G=\gcd(|A_\ell|,|B_\ell|).}
\tag{13.1}
$$


For $B_\ell\ne0$, the actual primitive pair is


$$
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{G},
\qquad
q=\frac{|B_\ell|}{G}.
\tag{13.2}
$$



The whole evaluated error remains exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
G\det H_{\rm complete}.
}
\tag{13.3}
$$



An irrationality proof would still require, at the same infinite original indices,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\boxed{
\log G-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|
\longrightarrow+\infty.
}
\tag{13.4}
$$


These conditions make the nonzero whole errors tend to zero. If $e+\pi=a/b$ were rational, every nonzero integer linear error would have absolute value at least $1/b$.

The local cancellation proves none of the nonvanishing, normalization, or real-decay assertions in (13.4). In particular, it gives no primitive denominator saving by itself.

---

## 14. Bounded exact arithmetic and status ledger

No tools or numerical calculations were used. No new arithmetic execution is indispensable for the endpoint proof.

### Optional bounded bookkeeping check

A coordinator-authored auxiliary check can be restricted to the following explicit inputs:

* the fourteen triples in (2.6);
* $0\le a\le27$, $\epsilon\in\{0,1\}$;
* the fixed integers
  

$$
2a+2\epsilon-7,\qquad
  2a+2\epsilon-5,\qquad
  2a+2\epsilon-3;
$$


* residue grades modulo $27$;
* the rational endpoints $3/25,31/250$, with $P\ge3^{31}$.

Expected verifiable outputs are:

1. In their stated ranges, the fixed integers are nonzero and have valuation at most $3$.

2. For the quotient and boundary ranges,
   

$$
v_3(2a+2\epsilon-5)\le a+\epsilon.
$$



3. The shifted arguments are exactly those in (7.9)–(7.10), and their residual bounds are below $540P$.

4. The LOW-return support propagation is
   

$$
15+3(14)
   \xrightarrow{\ \mathcal X^TM_L\ }
   15+3(14)+9(13)
   \pmod{27}.
$$



5. The terminal response support through three digits is contained in
   

$$
26+3(25)+3(0)+9(1),
$$


   disjoint from the preceding returned source support.

6. The exceptional visible grades $25,26,0,1$ are disjoint from the new HIGH source grades $15,14$.

Such a check has only bounded offset and residue inputs. It does not enumerate any $P$-, $H$-, LOW-, or HIGH-length array. It would verify only this bookkeeping, not the uniform source estimates or the pending Turn 18 theorem.

### Proof-status ledger

| Item | Status |
|---|---|
| Original finite unit blocks and older gradings | Reused at independently admitted current-core premises |
| Turn 13 residual identity and bare endpoint cancellation | Reused at the inherited endpoint-interface scope |
| Turn 17 admitted terminal directions | Reused; no new audit claim |
| Turn 18 terminal-module transition theorem | Favorable parent review; DIFFERENT audit still pending |
| New $f_I$ division by $9$ | Proved here for all original HIGH rows |
| New shifted LOW source depth and three-digit support | Proved here |
| Complete source-side and terminal-side LOW contractions | Evaluated here at their required depths |
| Shifted fourteen-term bulk annihilator | Proved here, with both channels and finite masks |
| Complementary $w_2^Tf_I\bmod3^{24}$ | Evaluated as zero, conditional on the Turn 18 terminal theorem |
| Core $\eta_{k-1}$ | Zero under the stated inherited dependencies |
| Core $\eta_0$ | Reused as zero at its existing scope |
| Other $\eta_i$ | Not evaluated |
| Alternating physical-$6$ directional identity | Proved at the leading complete-frame scope |
| First-four mixed return and paid physical-$6$ solve | Open |
| Actual physical $7$/source $34$ | Open |
| Actual contents, least clearer, all-prime $G$, primitive $q$ | Not evaluated |
| Same-index nonzero whole error and decay | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

---

## Conclusion

The complementary endpoint is no longer blocked by an unspecified LOW source return.

The new exact reduction is


$$
g_T^TE_c^{-1}b_I
\equiv27(M_H\upsilon_T)^Tf_H(I)\pmod{3^{30}}.
$$


Its proof retains and evaluates both mixed LOW source contractions, using the original finite blocks and the true Schur matrix.

The new shifted source satisfies


$$
f_H(I)\equiv f_{15}+3f_{14}\pmod9,
$$


and the unchanged weighted bulk module satisfies


$$
\mathscr B^Tf_H(I)\subseteq3^{29}\mathbb Z_3.
$$


The quotient and lower-boundary estimates use the actually derived integer


$$
2a+2\epsilon-5,
$$


whose valuation is paid by the generator and channel weights. Both finite HIGH ends remain covered by the unchanged exceptional module, whose complete pairing with this new source is zero modulo $9$.

Accordingly, at the mandated provisional status of the Turn 18 terminal theorem,


$$
\boxed{
w_2^Tf_H(I)\equiv0\pmod{3^{24}},
\qquad
g_T^TE_c^{-1}b_I\equiv0\pmod{3^{30}},
\qquad
\eta_{k-1}=0.
}
$$



The exact remaining local bottlenecks are the independent audit of the reused Turn 18 theorem, the still unknown interior coordinates of $\eta$, and the actual first-four mixed return needed for the complete paid physical-$6$ and physical-$7$ calculations. No original-length calculation is proposed to bypass those obligations.

The global bottleneck remains unchanged: the actual all-prime primitive normalization and a nonzero whole error tending to zero at the same infinite original indices.



$$
\boxed{\text{No unconditional decision about the rationality of }e+\pi\text{ follows.}}
$$


