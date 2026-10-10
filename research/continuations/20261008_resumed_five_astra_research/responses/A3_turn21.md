> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent proof audit of A1 Turn 19 and A5 Turns 18–19

## Abstract

The supplied work does not prove that $e+\pi$ is rational or irrational. The two original constructions must remain separate: a local ternary conclusion for the A1 core construction cannot be transferred to the A5 primitive producer, and neither construction presently supplies the required global arithmetic conclusion.

The principal audit results are as follows.

1. **A1 Turn 19 passes at its original core scope.** The complementary source at
   

$$
I=k-1=3\chi-\Pi-2
$$


   has the asserted finite degree, integral HIGH normalization by $9$, three-digit LOW support, and two-digit HIGH support. Both mixed LOW returns—not only the direct LOW product—vanish at the precision needed for the endpoint quotient. The shifted fourteen-term bulk estimate also passes, including every quotient coefficient and the literal lower HIGH mask.

   The accepted terminal-module theorem and accepted prefix/bare interface discharge the provisional dependencies stated in A1 Turn 19. Thus, at the original sufficiently large core indices,
   

$$
G_c(F[y^{\nu-1}],F[p_I])\in3^{30}\mathbb Z_3,
   \qquad \eta_I=0
$$


   in the stated residual normalization. This does **not** assert vanishing of all higher residual digits or transport to the actual physical-$7$ producer.

2. **The alternating physical-$6$ scalar identity passes at its leading-frame scope.** The full endpoint $2\times2$ moment block vanishes in the retained characteristic-$3$ frame. The remaining scalar is exactly the specified $R_4$ quadratic. The full vector equation still contains $N^T\eta$, and the first-four return remains unevaluated here.

3. **A5 Turn 18 passes.** The six-step transport, its two different affine forcing corrections, all four complete source/endpoint constants, strict negativity of the actual determinant, integer remainder identities, determinant-deep cap, divided Gaussian height bill, and complete non-arc $p^2$-block are valid at their stated scopes.

4. **A5 Turn 19 passes as a lifting and payment theorem, not as a noncollision theorem.** The actual Hermite defects must be retained. The all-depth quotient recurrence and the complete source and endpoint tests modulo $p^3$ follow exactly. At determinant-critical primes the correct comparison is
   

$$
c_p-2\le a_p\le c_p-2+v_p(\Delta);
$$


   it does not imply $c_p\le v_p(\Delta)+2$.

5. **A further proved payment is available.** Because $\Delta$ involves $\alpha,\beta$, but not $\delta$, its height has a better Gaussian exponential scale than the remainder divisor:
   

$$
\boxed{
   0<|\Delta|
   <3\cdot10^9(2N)^{14}\frac{5^{2N}}{g_B^2}.
   }
$$


   This sharpens the determinant-conditioning bill. It does not bound the surviving contact mass.

No numerical execution is needed for these symbolic audits.

---

# Part I. Audit of A1 Turn 19

## 1. Original domain and the exact finite objects

All A1 statements below concern only the original family


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$


with


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



The retained arithmetic is


$$
P=3^{h-32},\qquad P_0=243P,\qquad N_0=243r,
$$




$$
D=P_0+N_0,\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$




$$
4^j=243(3^{26}-1)P-243r+1.
$$


Also,


$$
Q=27P,\qquad Q-N_0=2R,\qquad \chi=P-R,
$$


so


$$
N_0=25P+2\chi,\qquad D=268P+2\chi.
$$



The subwindow is unchanged:


$$
\frac3{25}<\frac{\chi}{P}<\frac{31}{250}.
$$


Write


$$
S=h-32,\qquad P=3^S,\qquad H=3^{S+31},\qquad S\ge31,
$$




$$
\Pi=P/3,\qquad t=\Pi-2\chi,\qquad
k=3\chi-\Pi-1,\qquad I=k-1.
$$


Then


$$
t+I=\chi-2,\qquad I\equiv25\pmod{27},
$$


and


$$
\frac{2P}{75}-2<I<\frac{29P}{750}-2.
$$


Thus $t>0$, $I\ge0$, and $k>1$ in the retained sufficiently large domain. No independent choice of $P,\chi$, or $I$ is made.

The arithmetic


$$
v_3(\chi)=5,\qquad \chi/243\equiv1\pmod9
$$


implies


$$
v_3(D)=v_3(t)=v_3(A)=5.
$$


Moreover,


$$
\beta=D-H-71\equiv1\pmod3,
$$


so $\beta$ is a $3$-adic unit.

### 1.1 Literal boundaries

Set $x=y-1$. The original spaces are


$$
U_u=x^u,\quad 0\le u<D,
$$




$$
z_i^{\mathrm{mid}}=x^Dy^i,\quad 0\le i<\nu,
\qquad \nu=D/2-1=134P+\chi-1,
$$


and


$$
Y_s=y^s,\quad d\le s\le m,
\qquad d=D+\nu=402P+3\chi-1.
$$


The identity


$$
m+\nu=r_H,\qquad r_H=(H-1)/2
$$


will locate the physical terminal.

The three indices


$$
I,\qquad \nu-1,\qquad m
$$


have different roles:

- $I$ is the complementary residual coordinate;
- $y^{\nu-1}$ is the last middle polynomial;
- $Y_m$ is the physical HIGH terminal.

They are not interchangeable.

The retained prefix and tail boundaries are


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
a=\overline B_{\ell,\tau-1}\ne0.
$$



### 1.2 Complete functional and correction

The functional remains


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{v=0}^{K_{\mathrm{phys}}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
$$


where


$$
\mathfrak f(y^a)=(2a)!,
\qquad
K_{\mathrm{phys}}=2n-2=2H-2D+2.
$$



The core producer and form are


$$
Q_c=(y+1)x^A(\beta+3y),\qquad
G_c(f,g)=\mathcal M(Q_cfg).
$$


With $W=[U\ Y]$,


$$
E_c=G_c(W,W)
=
\begin{pmatrix}
3\mathcal L&3\mathcal X\\
3\mathcal X^T&E_Y
\end{pmatrix}.
$$


The actual inverses used in this audit are


$$
M_L=\mathcal L^{-1},\qquad
\mathcal S_H=E_Y-3\mathcal X^TM_L\mathcal X,\qquad
M_H=\mathcal S_H^{-1}.
$$


Their integrality and finite unit premises are established reuse.

The complete corrected column is


$$
F[p]=x^Dp-WE_c^{-1}G_c(W,x^Dp).
$$


In particular, the physical LOW inverse is $(3\mathcal L)^{-1}=M_L/3$, not $M_L$.

---

## 2. The inherited endpoint identity applies to this source

Retain


$$
\begin{aligned}
\Omega_P(y)={}&
(1-y)^{2P}(y^{122P}+3y^{41P})\\
&+9(1+y^P+y^{2P})
(2y^{14P}+2y^{41P}+2y^{95P}-y^{131P}),
\end{aligned}
$$


and


$$
p_i=\Omega_P(y)(1-y)^t y^i.
$$



The accepted prefix/bare interface gives, for the original coordinates,


$$
a\eta_i
=
-\frac{G_c(F[y^{\nu-1}],F[p_i])}{3^{29}}\pmod3.
$$


Its finite prefix inverse image and interior $J$-return are already included.

Put


$$
g_T=G_c(W,x^Dy^{\nu-1}),\qquad
b_I=G_c(W,x^Dp_I).
$$


Stationarity gives the exact identity


$$
G_c(F[y^{\nu-1}],F[p_I])
=
G_c(x^Dy^{\nu-1},x^Dp_I)-g_T^TE_c^{-1}b_I.
$$


The accepted bare calculation gives


$$
G_c(x^Dy^{\nu-1},x^Dp_I)\in3^{30}\mathbb Z_3.
$$


Consequently the target is


$$
a\eta_I=\frac{g_T^TE_c^{-1}b_I}{3^{29}}\pmod3.
$$


The whole return must therefore be controlled modulo $3^{30}$.

### 2.1 All fourteen source terms

The expansion


$$
p_I=\sum_{\mathcal T}c(1-y)^{t+\Delta}y^{bP+I}
$$


has exactly the following fourteen terms:


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
$$


Each term has both channels $\epsilon=0,1$, with multiplier


$$
c\,\beta^{1-\epsilon}3^\epsilon.
$$


The twelve terms of coefficient valuation $2$ are retained below.

---

## 3. Exact source formulas, finite degree, and normalized digits

### 3.1 The evaluated beta ratio

For nonnegative integers $N,q$,


$$
\mathcal B(N,q)
=\sum_{r=0}^N\frac{(-1)^r\binom Nr}{2(q+r)+1}
=\frac{4^NN!(N+q)!(2q)!}{q!(2N+2q+1)!}.
$$


The integral


$$
\int_0^1 z^{2q}(1-z^2)^N\,dz
$$


proves the equality.

For $M=3^e$, the contribution of the factorial valuations is


$$
\left\lfloor\frac{N\bmod M+q\bmod M}{M}\right\rfloor
+\left\lfloor\frac{2(q\bmod M)}M\right\rfloor
-\left\lfloor\frac{2(N\bmod M+q\bmod M)+1}M\right\rfloor.
$$


Since $M$ is odd, this equals $-1$ exactly when


$$
N\bmod M\ge
\left(\frac{M-1}{2}-q\right)\bmod M,
$$


and is otherwise zero. Thus


$$
v_3\mathcal B(N,q)
=
-\sum_{e\ge1}
\mathbf1_{\{N\bmod3^e\ge j_e(q)\}},
\quad
j_e(q)=\left(\frac{3^e-1}{2}-q\right)\bmod3^e.
$$



This is an evaluated factorial ratio with an exact valuation rule.

### 3.2 LOW coordinates are changed integrally, not replaced

For support arguments, use


$$
\widetilde U_u=y^u,\quad 0\le u<D.
$$


If $\widetilde U=UC$, then


$$
C_{r,u}=\binom ur
$$


is integral unimodular. Hence


$$
\widetilde{\mathcal L}=C^T\mathcal LC,\qquad
\widetilde{\mathcal X}=C^T\mathcal X,
$$




$$
\widetilde M_L=C^{-1}M_LC^{-T},\qquad
\widetilde\alpha=C^T\alpha.
$$


In particular,


$$
\widetilde{\mathcal X}^{\,T}\widetilde M_L\widetilde\alpha
=\mathcal X^TM_L\alpha,
$$


and the Schur complement is unchanged.

Define


$$
g_T=3\binom{\alpha_T}{\upsilon_T},
\qquad
b_I=\binom{3\alpha_I}{9f_I}.
$$



Because $Q_c(-1)=0$, the rational part of the complete functional is a finite coefficient functional on $Q_cfg/(y+1)$. Since $A+D=H$ is odd, the exact normalized formulas are


$$
(\widetilde\alpha_I)_u
=
-3^{h-1}\sum_{\mathcal T}\sum_{\epsilon=0}^1
c\beta^{1-\epsilon}3^\epsilon
\mathcal B(H+t+\Delta,u+bP+I+\epsilon)
+\mathcal F_{U,u},
$$


where


$$
\mathcal F_{U,u}
=-\frac{3^{h-1}}4\mathfrak f(Q_cy^ux^Dp_I)
\in3^{h-1}\mathbb Z_3,
$$


and


$$
(f_I)_s
=
-3^{h-2}\sum_{\mathcal T}\sum_{\epsilon=0}^1
c\beta^{1-\epsilon}3^\epsilon
\mathcal B(H+t+\Delta,s+bP+I+\epsilon)
+\mathcal F_{H,s},
$$


where


$$
\mathcal F_{H,s}
=-\frac{3^{h-2}}4\mathfrak f(Q_cY_sx^Dp_I)
\in3^{h-2}\mathbb Z_3.
$$



The factorial contributions are included, even when their valuations make them locally invisible.

### 3.3 Actual finite degree and pole exclusion

The highest term of $p_I$ comes from $b=133,\Delta=0$:


$$
\deg p_I=133P+t+I=133P+\chi-2.
$$


Therefore


$$
\deg(x^Dp_I)=401P+3\chi-2=d-P-1.
$$


In particular $p_I$ lies within the original middle polynomial range.

At $Y_m$, including the $3y$-channel, the largest degree after division by $y+1$ is


$$
H+m+133P+\chi-1
=\frac{3H-1}{2}-P.
$$


Thus the pole $2v+1=3H$, whose coefficient index is $(3H-1)/2$, is absent from every new HIGH source entry.

For LOW rows,


$$
(t+\Delta)+(u+bP+I+\epsilon)
\le(268+b)P+3\chi+\Delta-3+\epsilon<402P.
$$


The maximum uses $b=133,\Delta=0$; the two $\Delta=2P$ terms are smaller. All these polynomials remain inside $K_{\mathrm{phys}}$.

### 3.4 The division by $9$ is valid term by term

Consider one source term and channel. Set


$$
N=H+n_0,\quad n_0=t+\Delta,\quad
q=s+bP+I+\epsilon.
$$


All odd denominators are below $3H$. Apart from denominator $H$, their $3$-adic valuations are at most $h-2$, so $3^h$ supplies at least $3^2$.

At denominator $H$, the binomial coefficient index is


$$
r=r_H-q.
$$


Since $s\le m$ and $r_H-m=\nu$,


$$
r\ge \nu-bP-I-\epsilon
=(134-b)P+t+1-\epsilon.
$$


Hence


$$
r-n_0\ge(134-b)P-\Delta+1-\epsilon\ge P.
$$


Also $r<H$. Thus $n_0<r<H$, and


$$
(1-y)^{H+n_0}\equiv(1-y^H)(1-y)^{n_0}\pmod3
$$


has zero coefficient at $y^r$. This supplies the extra factor of $3$ at the denominator $H$.

The factorial part is in $3^h\mathbb Z_3$. Therefore


$$
G_c(Y_s,x^Dp_I)\in9\mathbb Z_3
$$


for every original HIGH row.

**Verdict: PASS.** The normalization $f_I=G_c(Y,x^Dp_I)/9$ is valid on the literal finite interval, without extending the old source.

### 3.5 All three required LOW digits

For the LOW beta ratio, $v_3(H+t+\Delta)=5$. The preceding bound $n_0+q<402P$ excludes every indicator above level $S+6$.

At the first five levels, $N\bmod3^e=0$, so their number is


$$
\min\{5,v_3(2q+1)\}.
$$


There are at most $S+1$ further indicators. Since $h-1=S+31$, each term has valuation at least


$$
30+v_3(c)+\epsilon-\min\{5,v_3(2q+1)\}.
$$


Thus


$$
\alpha_I\in3^{25}\mathbb Z_3^D.
$$



If $q\not\equiv13\pmod{27}$, then $v_3(2q+1)\le2$, so that term is in $3^{28}\mathbb Z_3$. Since


$$
q\equiv u+25+\epsilon\pmod{27},
$$


the visible grades after division by $3^{25}$, modulo $27$, are $15$ in the $\beta$-channel and $14$ in the $3y$-channel.

Writing $\mathscr L_b$ for the finite LOW vectors supported on indices $b\bmod27$,


$$
\boxed{
3^{-25}\widetilde\alpha_I
\in\mathscr L_{15}+3\mathscr L_{14}+27\mathbb Z_3^D.
}
$$


This includes contributions of the twelve valuation-$2$ source terms at the third retained LOW digit.

### 3.6 The HIGH grading is source-specific

In the functional divided by $9$, the smallest possible denominator weight has valuation $-1$, at denominator $H$. Every pole visible modulo $9$ has coefficient index $v\equiv13\pmod{27}$.

For


$$
r=v-(s+bP+I+\epsilon),
$$


if $27\nmid r$ and $0<r\le N$, then


$$
v_3\binom Nr
\ge v_3(N)-v_3(r)\ge3.
$$


Even a weight of valuation $-1$ therefore gives valuation at least $2$. A visible coefficient requires


$$
s+bP+I+\epsilon\equiv13\pmod{27}.
$$


The two grades are consequently $15$ and $14$, with the latter retaining its factor $3$:


$$
\boxed{
f_I\in\mathscr V_{15}+3\mathscr V_{14}+9\mathscr V.
}
$$


The proof uses actual rows $d\le s\le m$, including both boundaries.

### 3.7 Terminal source and the genuine $3H$ resonance

Put


$$
\kappa(q)=-3H\mathcal B(H,q).
$$


The normalized terminal source has rational part


$$
(\upsilon_T)_s
=
\frac{\beta\kappa(s+\nu-1)}3+\kappa(s+\nu).
$$



For $q<r_H$, the valuation rule gives


$$
v_3\kappa(q)=S+32-v_3(2q+1).
$$


At $q=r_H$, there is one additional indicator at modulus $3H$, and $\kappa(r_H)$ is a unit.

Thus:

- the $\beta$-argument is always below $r_H$;
- the second argument equals $r_H$ exactly at $s=m$;
- the physical terminal unit is retained.

Since $\nu\equiv26\pmod{27}$,


$$
\boxed{
\upsilon_T\in
\mathscr V_{14}+3\mathscr V_{15}+27\mathscr V.
}
$$



For LOW terminal rows,


$$
2(u+\nu)+1<3D<3^{S+7}.
$$


The same formula gives


$$
\alpha_T\in3^{25}\mathbb Z_3^D,
$$


and


$$
\boxed{
3^{-25}\widetilde\alpha_T
\in\mathscr L_{15}+3\mathscr L_{14}+9\mathbb Z_3^D.
}
$$



The ordinary new source has no $3H$ pole; the unchanged terminal source does. The distinction is essential and is respected by the proof.

---

## 4. Finite inverse orientation and both mixed LOW returns

### 4.1 Reflection and shift rules

A reflection of grade $r$ sends grade $b$ to $r-b$; a shift of grade $r$ sends grade $b$ to $b+r$.

On the actual finite index sets,


$$
\widetilde{\mathcal L}\equiv L_0+3L_1,\quad
\widetilde{\mathcal X}\equiv X_0+3X_1,\quad
E_Y\equiv Y_0+3Y_1\pmod{27},
$$


where the $0$-parts have reflection grade $13$ and the $1$-parts have reflection grade $12$.

Applicability follows from the complete functional:

- normalized LOW/LOW and LOW/HIGH entries avoid $3H$;
- HIGH/HIGH entries retain $3H$;
- every visible pole index is $13\bmod27$;
- $v_3(A)=5$ implies
  

$$
27\nmid r\Longrightarrow v_3\binom Ar\ge3;
$$


- the $3y$-channel shifts the reflection grade from $13$ to $12$.

Finite row and column restrictions preserve support. No infinite convolution inverse is used.

For a finite unit matrix $L_0$,


$$
(L_0+3L_1)^{-1}
\equiv
L_0^{-1}
-3L_0^{-1}L_1L_0^{-1}
+9L_0^{-1}L_1L_0^{-1}L_1L_0^{-1}\pmod{27}.
$$


The three reflection grades are $13,14,15$. Therefore


$$
\widetilde M_L\equiv M_{L,0}+3M_{L,1}+9M_{L,2}\pmod{27}.
$$



Composition gives


$$
\widetilde{\mathcal X}^{\,T}\widetilde M_L\widetilde{\mathcal X}
\equiv Z_0+3Z_1+9Z_2\pmod{27},
$$


where $Z_j$ has reflection grade $13-j$. Hence the **true** Schur matrix is


$$
\mathcal S_H
\equiv(Y_0-3Z_0)+3(Y_1-3Z_1)\pmod{27}.
$$


Its inverse has reflection grades $13,14,15$:


$$
M_H\equiv M_{H,0}+3M_{H,1}+9M_{H,2}\pmod{27}.
$$



Finally,


$$
\boxed{
\widetilde{\mathcal X}^{\,T}\widetilde M_L
\equiv T_0+3T_1+9T_2\pmod{27},
}
$$


where $T_j$ shifts grade by $-j$. This orientation is correct: it is a LOW-to-HIGH map, not its reverse.

### 4.2 Exact block pairing

Set


$$
v_T=M_H\upsilon_T,\qquad
d_T=\mathcal X^TM_L\alpha_T,\qquad
d_I=\mathcal X^TM_L\alpha_I.
$$


The Schur formula, including the physical LOW inverse $M_L/3$, gives


$$
\boxed{
g_T^TE_c^{-1}b_I
=
3\alpha_T^TM_L\alpha_I
+
27(\upsilon_T-d_T)^TM_H
\left(f_I-\frac{d_I}{3}\right).
}
$$


The quotient $d_I/3$ is integral because $d_I\in3^{25}\mathscr V$.

Since the forms and inverse blocks are symmetric, expansion gives


$$
\begin{aligned}
g_T^TE_c^{-1}b_I={}&27v_T^Tf_I
+3\alpha_T^TM_L\alpha_I\\
&-9v_T^Td_I
-27d_T^TM_Hf_I
+9d_T^TM_Hd_I.
\end{aligned}
$$


These are all the LOW source returns.

### 4.3 Source-side mixed return

The terminal grading and the inverse reflections imply


$$
v_T\in
\mathscr V_{26}
+3\mathscr V_{25}
+3\mathscr V_0
+9\mathscr V_1
+27\mathscr V.
$$


The LOW source grading and the LOW-to-HIGH shifts imply


$$
3^{-25}d_I\in
\mathscr V_{15}
+3\mathscr V_{14}
+9\mathscr V_{13}
+27\mathscr V.
$$


The visible support sets are disjoint. Therefore


$$
v_T^T(3^{-25}d_I)\equiv0\pmod{27},
$$


so


$$
\boxed{v_T^Td_I\in3^{28}\mathbb Z_3.}
$$


Multiplication by the actual factor $9$ places this mixed term in $3^{30}\mathbb Z_3$.

### 4.4 Terminal-side mixed return

Modulo $9$,


$$
3^{-25}d_T\in\mathscr V_{15}+3\mathscr V_{14}+9\mathscr V,
$$


while


$$
M_Hf_I\in\mathscr V_{25}+3\mathscr V_{26}+9\mathscr V.
$$


Again the supports are disjoint. Thus


$$
\boxed{d_T^TM_Hf_I\in3^{27}\mathbb Z_3.}
$$


Its actual factor $27$ also places the term in $3^{30}\mathbb Z_3$.

The other two LOW terms satisfy


$$
3\alpha_T^TM_L\alpha_I\in3^{51}\mathbb Z_3,
\qquad
9d_T^TM_Hd_I\in3^{52}\mathbb Z_3.
$$


Consequently


$$
\boxed{
g_T^TE_c^{-1}b_I
\equiv27v_T^Tf_I\pmod{3^{30}}.
}
$$



**Verdict: PASS.** Both mixed returns have been paid at their full required depths. The operator return in $\mathcal S_H$ and the two source returns are distinct mechanisms; all are retained.

---

## 5. Audit of the shifted bulk estimate

### 5.1 The unchanged finite module

Put


$$
B_\circ=H/3^{24}=2187P,\qquad
C_\circ=(3^{24}-1)/2.
$$


The original inequalities imply


$$
B_\circ>4D+60,\qquad B_\circ/2>540P,\qquad \nu>28.
$$



For


$$
b_j=\binom{D+j-1}{j},
$$


the exact finite quotient is


$$
P_{d+a}(y)=\sum_{j=0}^{\nu+a}b_jy^{\nu+a-j},
$$


with


$$
y^{d+a}=C_{d+a}+x^DP_{d+a},\qquad \deg C_{d+a}<D.
$$



The retained bulk module is generated by


$$
\mathsf T_{a,v}
=
3^{(a-1)_+}\operatorname{pr}_{[d,m]}
\left(x^Dy^{vB_\circ+\nu-1+a}\right),
\quad 0\le a\le27,
$$




$$
\mathsf Q_{a,v}
=
3^a\operatorname{pr}_{[d,m]}
\left(x^Dy^{vB_\circ}P_{d+a}\right),
\quad0\le a\le26,
$$




$$
\mathsf O_{a,v}
=
3^a\operatorname{pr}_{[d,m]}
\left(x^Dy^{vB_\circ+a}\right),
\quad0\le a\le26,
$$


where $0\le v\le C_\circ$.

For $v\ge1$, the support inequalities place these polynomials wholly inside $[d,m]$. At $v=0$,


$$
\mathsf Q_{a,0}=3^ay^{d+a},\qquad \mathsf O_{a,0}=0,
$$


and


$$
\mathsf T_{a,0}
=
3^{a-1}\sum_{b=0}^{a-1}
(-1)^{a-1-b}\binom D{a-1-b}y^{d+b}
\quad(a\ge1),
$$


while $\mathsf T_{0,0}=0$.

These are the literal masks, not limiting or extended ones.

### 5.2 Exact shifted arguments

For an interior generator,


$$
N=H+D+t+\Delta=H+268P+\Pi+\Delta,
\qquad v_3(N)=S-1.
$$


The arguments are


$$
\begin{array}{c|l|c}
\text{family}&q&\text{fixed low part of }2q+1\\ \hline
\mathsf T_{a,v}
&
vB_\circ+(134+b)P-\Pi+4\chi-4+a+\epsilon
&
2a+2\epsilon-7\\
\mathsf O_{a,v}
&
vB_\circ+bP-\Pi+3\chi-2+a+\epsilon
&
2a+2\epsilon-3\\
\mathsf Q_{a,v},\ b_j
&
vB_\circ+(134+b)P-\Pi+4\chi-3+a-j+\epsilon
&
2a+2\epsilon-5-2j.
\end{array}
$$



For a lower-edge monomial $y^{d+a}$,


$$
N=H+t+\Delta,\qquad v_3(N)=5,
$$




$$
q=(402+b)P-\Pi+6\chi-3+a+\epsilon,
$$


whose fixed low part is


$$
2a+2\epsilon-5.
$$



These formulas follow directly from $I=3\chi-\Pi-2$. In particular, the quotient and edge constant is $-5$, not the old unshifted constant.

### 5.3 All high indicators are absent

Write


$$
N=H+N_{\mathrm{lo}},\qquad q=vB_\circ+q_{\mathrm{lo}}.
$$


The complete source table gives


$$
N_{\mathrm{lo}}+q_{\mathrm{lo}}
\le535P+4\chi+24<536P
$$


for terminal and quotient generators,


$$
N_{\mathrm{lo}}+q_{\mathrm{lo}}
\le401P+3\chi+25<402P
$$


for ordinary generators, and the edge bound is also below $536P$. Thus


$$
N_{\mathrm{lo}}+q_{\mathrm{lo}}<540P<B_\circ/2.
$$



For $S+7\le e\le S+31$, the modulus $3^e$ is an odd multiple of $B_\circ$. The residue of $j_e(q)$ modulo $B_\circ$ is


$$
(B_\circ-1)/2-q_{\mathrm{lo}}>N_{\mathrm{lo}},
$$


so the corresponding indicator vanishes.

At modulus $3H$,


$$
q\le(H-B_\circ)/2+q_{\mathrm{lo}},
$$


and therefore


$$
(3H-1)/2-q>H+N_{\mathrm{lo}}.
$$


All higher indicators vanish as well.

The same inequalities give a degree bound with a positive margin below the $3H$ pole:


$$
N+q
\le H+(H-B_\circ)/2+540P
<(3H-1)/2<K_{\mathrm{phys}}.
$$



### 5.4 Terminal and ordinary generators

The normalized functional contributes $3^{h-2}=3^{S+30}$.

For $\mathsf T$, the first $S-1$ indicators count


$$
v_3(2a+2\epsilon-7)\le3;
$$


for $\mathsf O$, they count


$$
v_3(2a+2\epsilon-3)\le3.
$$


All omitted parts of $2q+1$ are divisible by $3^5$, and the displayed odd integers are nonzero with absolute value below $81$.

Only seven further indicators remain. Thus these contractions have valuation at least


$$
S+30-10=S+20\ge51
$$


before their nonnegative weights and coefficient valuations are added.

### 5.5 Every coefficient of every finite quotient

Let


$$
u=a+\epsilon,\qquad \omega=2u-5,\qquad
\lambda=v_3(\omega)\le3.
$$


If $v_3(j)\ne\lambda$, including $j=0$, then


$$
v_3(2q+1)\le\lambda,
$$


and the term is already much deeper than required.

If $v_3(j)=\lambda$, use the exact integer identity


$$
b_j=\frac Dj\binom{D+j-1}{j-1}.
$$


It gives


$$
v_3(b_j)\ge5-\lambda.
$$


Even allowing all $S+6$ possible indicators, the weighted term has valuation at least


$$
S+30+a+\epsilon+v_3(c)+(5-\lambda)-(S+6)
=
29+u+v_3(c)-\lambda.
$$



The needed payment is


$$
v_3(2u-5)\le u.
$$


For $u=0,1,2$, the valuations are $0,1,0$. For $u\ge3$,


$$
0<2u-5<3^u,
$$


so the inequality follows. Therefore every quotient coefficient contributes at depth at least $29$.

No quotient tail is omitted.

### 5.6 The complete lower mask

For $3^ay^{d+a}$, the first five indicators contribute


$$
\lambda=v_3(2a+2\epsilon-5)\le3,
$$


and there are at most $S+1$ further indicators. The valuation is at least


$$
29+a+\epsilon+v_3(c)-\lambda\ge29.
$$



In $\mathsf T_{a,0}$, the factor $3^{a-1}$ contains $3^b$ for every $b\le a-1$. Therefore each term of the actual lower mask is covered by this edge estimate.

The factorial part is in $3^{S+30}\mathbb Z_3$, and all source, quotient, and generator coefficients are integral. Summation cannot reduce the common lower bound.

We have proved


$$
\boxed{\mathscr B^Tf_I\subseteq3^{29}\mathbb Z_3.}
$$



**Verdict: PASS.** The proof covers all fourteen shifted terms, both channels, every finite quotient coefficient, and the actual lower HIGH edge.

---

## 6. Exceptional module, accepted terminal theorem, and the endpoint

The exceptional module is


$$
\mathscr E=
\mathscr V_{25}+\mathscr V_{26}+\mathscr V_0
+3\mathscr V_1+9\mathscr V.
$$


Its visible grades are disjoint from $15,14$, so


$$
\mathscr E^Tf_I\subseteq9\mathbb Z_3.
$$


For


$$
\mathscr N=\mathscr B+3^{25}\mathscr E+3^{27}\mathscr V,
$$


it follows that


$$
\mathscr N^Tf_I\subseteq3^{27}\mathbb Z_3.
$$



The now accepted terminal-module theorem concerns the unchanged finite operator:


$$
\mathcal K_H\upsilon_T\in\mathscr N,\qquad
(\mathcal K_H\mathcal S_H)\mathscr N\subseteq\mathscr N,
\qquad
\mathcal K_H\mathcal S_H\equiv I\pmod3,
$$


where


$$
V_{\mathcal K_Hv}(y)=
\operatorname{pr}_{[d,m]}
\left(x^Dy^{r_H}V_v(y^{-1})\right).
$$


Its scope includes both finite HIGH masks, the physical $3y$-terminal resonance, the exceptional grid interactions, and the true LOW feedback in $\mathcal S_H$.

Since $\mathscr N$ contains $3^{27}\mathscr V$, inversion modulo $3^{27}$ is a finite polynomial in $I-\mathcal K_H\mathcal S_H$. Stability of $\mathscr N$ therefore gives


$$
v_T=M_H\upsilon_T\in\mathscr N.
$$


Consequently


$$
v_T^Tf_I\in3^{27}\mathbb Z_3,
$$


and the complete block reduction gives


$$
g_T^TE_c^{-1}b_I\in3^{30}\mathbb Z_3.
$$



Using the accepted bare term,


$$
\boxed{
G_c(F[y^{\nu-1}],F[p_I])\in3^{30}\mathbb Z_3,
\qquad \eta_I=0.
}
$$



### 6.1 No stale provisional dependency remains

A1 Turn 19 described the terminal theorem and prefix/bare interface as pending. Those dependencies are discharged by the supplied completed audit gates.

Thus the complementary core conclusion is now **PASS**, not a deduction conditional on an unaudited terminal-module theorem.

This does not certify the actual/core transport, other coordinates of $\eta$, or physical $7$/source $34$.

### 6.2 The unchanged terminal certificate retains its LOW return

The accepted terminal certificate includes


$$
\begin{aligned}
r_2={}&
\frac{\delta_{\rm raw}-G_c(Y,x^DP_*)
-3G_c(Y,x^DP^{[1]})}{9}\\
&+\frac19\mathcal X^TM_L\alpha_d
+\frac13\mathcal X^TM_L\alpha_*
+\mathcal X^TM_L\alpha_{[1]},
\end{aligned}
$$


where


$$
\delta_{\rm raw}
=\frac{\upsilon_T-G_c(Y,x^DP_d)}3,
\qquad
P_*=y^{H/3+\nu-1}-P_{d+1},
$$




$$
\begin{aligned}
P^{[1]}={}&
y^{4H/9+\nu-1}-y^{2H/9+\nu-1}
+y^{H/9+\nu-1}\\
&-y^{H/3}P_d+P_{d+2}-P_d,
\end{aligned}
$$


and


$$
\alpha_d=G_c(U,x^DP_d)/3,\quad
\alpha_*=G_c(U,x^DP_*)/3,\quad
\alpha_{[1]}=G_c(U,x^DP^{[1]})/3.
$$


In particular,


$$
r_2\equiv
\frac{\delta_{\rm raw}-G_c(Y,x^DP_*)
-3G_c(Y,x^DP^{[1]})}{9}
+3^{23}R_d\pmod{3^{24}}.
$$


The $3^{23}R_d$ term is not deleted.

### 6.3 The $w_2$ normalization

The retained decomposition is


$$
v_T=V^{(0)}+27w_2,\qquad
V^{(0)}=e_d+3z_0+9\widehat z_1\in\mathscr B.
$$


Therefore


$$
(V^{(0)})^Tf_I\in3^{29}\mathbb Z_3,
\qquad
w_2^Tf_I\in3^{24}\mathbb Z_3.
$$


Only after the complete LOW reduction is paid may one write


$$
a\eta_I=\frac{w_2^Tf_I}{3^{23}}\pmod3.
$$


That normalization passes.

---

## 7. Alternating physical-$6$ scalar: what vanishes and what remains

Use the previously proved source-specific core endpoint $\eta_0=0$, together with the newly audited $\eta_I=0$. This does not assert completion of the separate review of the earlier $\eta_0$ interface, and does not extend its scope to the actual physical-$7$ producer.

In the retained leading frame,


$$
C_6=C^0-(e_I\eta^T+\eta e_I^T),\qquad
C^0=C^{\mathrm{mom}}-R_4,
$$




$$
R_4=C_H^TA_4^{-1}C_H,
\qquad B_6=N^TC_6N,\qquad
w_6=\bar\gamma N^TC_6e_0,
$$


where the columns of $N$ are $e_j+e_{j+1}$.

For


$$
z_{\mathrm{alt}}=(1,-1,\ldots,(-1)^{k-2})^T,\qquad
\varepsilon_{\mathrm{alt}}=(-1)^{k-2},
$$


telescoping gives


$$
Nz_{\mathrm{alt}}=e_0+\varepsilon_{\mathrm{alt}}e_I.
$$


Let $h=N^T\eta$. Then


$$
z_{\mathrm{alt}}^Th=\eta_0+\varepsilon_{\mathrm{alt}}\eta_I=0.
$$


Consequently


$$
B_6z_{\mathrm{alt}}
=
B^0z_{\mathrm{alt}}-\varepsilon_{\mathrm{alt}}h,
\qquad
w_6=w^0,
$$


and


$$
z_{\mathrm{alt}}^TB_6z_{\mathrm{alt}}
=z_{\mathrm{alt}}^TB^0z_{\mathrm{alt}}.
$$



The vector $h$ remains in the directional equation. The scalar cancellation does not remove it.

### 7.1 The entire endpoint moment block vanishes

In the inherited moment frame, the endpoint moment entries use the coefficients of $(1-y)^t$ at


$$
\kappa_2,\quad \kappa_2-I,\quad \kappa_2-2I,
\qquad
\kappa_2=(P/9-1)/2.
$$


Since $243\mid t$,


$$
(1-y)^t=(1-y^{243})^{t/243}\quad\text{in }\mathbb F_3[y].
$$


Also,


$$
\kappa_2\equiv121,\qquad I\equiv-2\pmod{243}.
$$


Thus the three indices have residues $121,123,125$, none divisible by $243$. All three coefficients vanish.

Therefore the endpoint $2\times2$ block of $C^{\mathrm{mom}}$ is zero, and


$$
\boxed{
z_{\mathrm{alt}}^TB_6z_{\mathrm{alt}}
=
-\left((R_4)_{00}
+2\varepsilon_{\mathrm{alt}}(R_4)_{0I}
+(R_4)_{II}\right).
}
$$


Equivalently, with


$$
v_{\mathrm{end}}=C_H(e_0+\varepsilon_{\mathrm{alt}}e_I),
$$


the scalar is


$$
-v_{\mathrm{end}}^TA_4^{-1}v_{\mathrm{end}}.
$$



**Normalization clarification.** The moment cancellation is in the retained leading characteristic-$3$ frame. It is not an assertion that the corresponding unreduced integer moment coefficients vanish identically.

The complete first-four cross remains


$$
P_{ui}=\frac{d_u^T\mathsf A^{-1}d_H{}_i}{3}\pmod3,
$$




$$
(C_H)_{ui}
=
-c_{P-1-u-i-\Pi}
+c_{P-1-u-i-2\Pi}
-2\mathbf1_{u=R,\ i=I}
-P_{ui}.
$$


Neither the mixed-prefix division, the actual $A_4^{-1}$, nor the upper $3y$ corner is evaluated here. That separate first-four evaluation is not duplicated.

The paid direction


$$
B_6x=w_6,\qquad x\in3^{-1}\mathbb Z_3^{k-1}
$$


remains a larger obligation than this scalar identity.

### 7.2 A1 precision ledger



$$
\begin{array}{l|l}
\text{operation}&\text{paid precision/depth}\\ \hline
\text{endpoint quotient }/3^{29}&\text{whole numerator modulo }3^{30}\\
\alpha_I=G_c(U,x^Dp_I)/3&\alpha_I\in3^{25}\\
3^{-25}\widetilde\alpha_I\bmod27&
\text{raw LOW source modulo }3^{29}\\
3^{-25}\widetilde\alpha_T\bmod9&
\text{raw terminal LOW source modulo }3^{28}\\
f_I=G_c(Y,x^Dp_I)/9&\text{integral on every original HIGH row}\\
d_I/3&d_I\in3^{25},\ d_I/3\in3^{24}\\
9v_T^Td_I&v_T^Td_I\in3^{28},\ \text{whole term in }3^{30}\\
27d_T^TM_Hf_I&\text{pairing in }3^{27},\ \text{whole term in }3^{30}\\
\mathscr B^Tf_I&\subseteq3^{29}\\
3^{25}\mathscr E^Tf_I&\subseteq3^{27}\\
w_2^Tf_I&\in3^{24};\ \text{final quotient }/3^{23}\\
r_2\bmod3^{24}\text{ after }/9&
\text{its polynomial numerator modulo }3^{26}\\
\delta_{\rm raw}\text{ after }/3&
\upsilon_T-G_c(Y,x^DP_d)\bmod3^{27}.
\end{array}
$$



---

# Part II. Audit of A5 Turn 18

## 8. Original A5 family and actual normalization

The second family is


$$
\boxed{N=9^{18+32u}=3^{36+64u},\qquad u\ge0,}
$$


with


$$
n=2N,\qquad m=N-3,\qquad \ell=2N-6.
$$


The physical terminal is $n$. No A1 index is identified with this $N$.

Let


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$




$$
C_0=1,\quad C_1=2t-1,\quad
C_{j+1}=(4t-2)C_j-C_{j-1}.
$$


The actual division is


$$
g_B=\gcd(b_{N-1},b_N)>0,
$$




$$
\alpha=b_{N-1}/g_B,\quad
\beta=b_N/g_B,\quad
\delta=(a_Nb_{N-1}-a_{N-1}b_N)/g_B.
$$


Then


$$
F=\alpha C_N-\beta C_{N-1},\qquad F(\pm i)=\delta,
\qquad \gcd(\alpha,\beta)=1.
$$



### 8.1 Gaussian admissibility can be checked directly

Define


$$
\omega_j^{G}=\operatorname{Im}
\bigl(C_j(i)\overline{C_{j-1}(i)}\bigr).
$$


The Gaussian recurrence gives


$$
\omega_j^{G}=4|C_{j-1}(i)|^2+\omega_{j-1}^{G},
\qquad \omega_1^{G}=2.
$$


Thus $\omega_j^{G}>0$. Consequently


$$
a_Nb_{N-1}-a_{N-1}b_N=-\omega_N^{G}<0.
$$


In particular, $b_{N-1},b_N$ cannot both vanish, $g_B>0$, and $\delta\ne0$. This is a real nonvanishing statement, not a $p$-adic unit assertion.

For integer polynomials,


$$
\eta(H)=\sum_jj![z^j]H(1-z),\qquad
E(H)=\sum_j(-1)^jj![t^j]H(t).
$$


Set


$$
\mathcal H=t(1-t)(1+t^2)^2,\qquad K=\mathcal H C_m^2,
$$




$$
U=-\eta(K),\qquad V=\eta(F^2)-\delta^2,\qquad c=\gcd(U,V).
$$


The established original-domain normalization is retained:


$$
\operatorname{cont}(W_{\rm raw})=g_B^2c,\qquad
\tau=U/c,\quad \nu=V/c,
$$




$$
W_{\rm prim}=\tau F^2+\nu K,\qquad M=\tau\delta^2.
$$


The established signs $U,V,M>0$ are used only on the original family.

### 8.2 Exact all-prime credit

Retain


$$
L(x)=(x-1)(x-9)(x-25),
$$




$$
A_K(x)=13x^3-455x^2+3502x-5850,
$$


and the actual reduced arc


$$
R_K=\frac{A_K(\ell^2)}{30L(\ell^2)}=\frac{a_K}{d_K},
$$


with


$$
g_{\rm arc}=90\,5^{\varepsilon_5}19^{\varepsilon_{19}}31^{\varepsilon_{31}},
$$




$$
\varepsilon_5=\mathbf1_{u\equiv1\pmod5},\quad
\varepsilon_{19}=\mathbf1_{u\equiv3\pmod9},\quad
\varepsilon_{31}=\mathbf1_{u\equiv5,7\pmod{15}},
$$




$$
a_K=A_K(\ell^2)/g_{\rm arc},\qquad
d_K=30L(\ell^2)/g_{\rm arc}.
$$


This closed reduction is reused, not recomputed.

Put


$$
E_K=E(K),\qquad y_K=d_KE_K-a_K,
$$


so $\gcd(d_K,y_K)=1$, and retain


$$
\gamma=\gcd(\tau,y_K),\qquad
b^\circ=\gcd(\gamma,a_K),\qquad r^\circ=\gamma/b^\circ.
$$



The Hermite integers are defined only through the original endpoint $N$:


$$
P_0^{\mathrm H}=Q_0^{\mathrm H}=1,\quad
P_1^{\mathrm H}=3,\quad Q_1^{\mathrm H}=1,
$$




$$
Z_{a+1}=(4a+2)Z_a+Z_{a-1},\qquad1\le a\le N-1.
$$



The fixed-product multiplier is


$$
\kappa_N^{\mathrm{prod}}
=
\frac{c}{\gcd(c,Q_{N-1}^{\mathrm H}Q_N^{\mathrm H}(y_K/r^\circ)^2)}.
$$


For every prime,


$$
c_p=\min(v_p(U),v_p(V)),\quad t_p=v_p(U)-c_p,
$$




$$
z_p=v_p(y_K),\quad b_p=v_p(b^\circ),\quad
h_p=v_p(Q_{N-1}^{\mathrm H}Q_N^{\mathrm H}).
$$


Indeed,


$$
v_p(r^\circ)=\min(t_p,z_p)-b_p,
$$


so


$$
v_p(y_K/r^\circ)=(z_p-t_p)_++b_p.
$$


Therefore


$$
\boxed{
k_p=v_p(\kappa_N^{\mathrm{prod}})
=[c_p-H_p]_+,
\quad
H_p=h_p+2b_p+2(z_p-t_p)_+.
}
$$


This derivation is valid at every prime. No credit has been suppressed.

---

## 9. Complete source and endpoint columns

The original affine states satisfy


$$
\Theta_0=\Phi_0=0,\qquad \Theta_1=\Phi_1=1,
$$


and exactly for $1\le j\le n-1$,


$$
\Theta_{j+1}+4j\Theta_j-\Theta_{j-1}=2,
$$




$$
\Phi_{j+1}+4j\Phi_j-\Phi_{j-1}=2(-1)^j.
$$


Their moment interpretations are


$$
\eta(C_j)=1-2j\Theta_j,\qquad
E(C_j)=(-1)^j-2j\Phi_j.
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


Define


$$
\mathscr A=2\ell((2\ell+1)\mathcal Q-\mathcal P),\qquad
\mathscr B=-2\ell\mathcal Q,
$$




$$
\mathscr C_U=\mathcal F-\mathcal P+2\ell\mathcal Q,\qquad
\mathscr C_E=\mathcal G+\mathcal P-2(\ell+1)\mathcal Q.
$$


The established complete $K$-columns are


$$
16U=\mathscr C_U-\mathscr A\Theta_\ell-\mathscr B\Theta_{\ell-1},
$$




$$
16E_K=\mathscr C_E+\mathscr A\Phi_\ell+\mathscr B\Phi_{\ell-1}.
$$



At the physical terminal,


$$
V=C_V-P\Theta_n-Q\Theta_{n-1},
$$




$$
E_F=C_F^E-P\Phi_n-Q\Phi_{n-1},
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
$$



These complete corrected column identities are reused at their established scope. In particular, $-\delta^2$ and $4\alpha\beta$ are not optional terms.

---

## 10. Independent derivation of the six-step transport

Let


$$
x_j=4(\ell+j),\qquad0\le j\le5.
$$


Define


$$
a_0^\ast=1,\ a_1^\ast=x_0,\qquad
b_0^\ast=0,\ b_1^\ast=1,
$$




$$
a_{j+1}^\ast=x_ja_j^\ast+a_{j-1}^\ast,\qquad
b_{j+1}^\ast=x_jb_j^\ast+b_{j-1}^\ast.
$$


The forcing corrections have


$$
f_0=g_0=0,\qquad f_1=g_1=2,
$$




$$
f_{j+1}=-x_jf_j+f_{j-1}+2,
$$




$$
g_{j+1}=-x_jg_j+g_{j-1}+2(-1)^j.
$$


The second forcing uses the actual fact that $\ell$ is even.

Induction in the original recurrences yields


$$
\Theta_{\ell+j}
=(-1)^ja_j^\ast\Theta_\ell
+(-1)^{j-1}b_j^\ast\Theta_{\ell-1}+f_j,
$$


and the corresponding formula for $\Phi$ with $g_j$, for $1\le j\le6$. The last step is $\ell+5=n-1$, not above the physical terminal.

The complete forced scalars are explicitly determined by


$$
\begin{aligned}
F_3&=x_2(x_1-1)+2,&
F_4&=-x_3F_3+2-x_1,\\
F_5&=-x_4F_4+F_3+1,&
F_6&=-x_5F_5+F_4+1,
\end{aligned}
$$


with $f_j=2F_j$ for $3\le j\le6$, and


$$
\begin{aligned}
G_3&=x_2(x_1+1)+2,&
G_4&=-x_3G_3-x_1-2,\\
G_5&=-x_4G_4+G_3+1,&
G_6&=-x_5G_5+G_4-1,
\end{aligned}
$$


with $g_j=2G_j$.

At $j=6,5$, substitution gives


$$
V=C^{\rm s}-\Pi\Theta_\ell-\Omega\Theta_{\ell-1},
$$




$$
E_F=C^{\rm e}-\Pi\Phi_\ell-\Omega\Phi_{\ell-1}.
$$


Initially,


$$
\Pi=Pa_6^\ast-Qa_5^\ast,\qquad
\Omega=-Pb_6^\ast+Qb_5^\ast.
$$


Using


$$
a_6^\ast=4(n-1)a_5^\ast+a_4^\ast
$$


and the analogous identity for $b^\ast$,


$$
\boxed{
\begin{aligned}
\Pi={}&na_6^\ast\alpha^2
+2(n-1)a_5^\ast\alpha\beta
+(n-2)a_4^\ast\beta^2,\\
\Omega={}&-nb_6^\ast\alpha^2
-2(n-1)b_5^\ast\alpha\beta
-(n-2)b_4^\ast\beta^2.
\end{aligned}}
$$



Similarly,


$$
C^{\rm s}=C_V-Pf_6-Qf_5,\qquad
C^{\rm e}=C_F^E-Pg_6-Qg_5.
$$


The last forced steps are


$$
f_6=-4(n-1)f_5+f_4+2,
$$




$$
g_6=-4(n-1)g_5+g_4-2.
$$


Consequently


$$
\boxed{
\begin{aligned}
C^{\rm s}={}&(1-nf_6)\alpha^2
+2(n-1)f_5\alpha\beta\\
&+(1-(n-2)f_4)\beta^2-\delta^2,\\
C^{\rm e}={}&(1-ng_6)\alpha^2
+(4+2(n-1)g_5)\alpha\beta\\
&+(1-(n-2)g_4)\beta^2.
\end{aligned}}
$$



**Verdict: PASS.** The source and endpoint constants differ for a mathematical reason: their affine forcings differ. Neither can replace the other.

---

## 11. Strict negativity of the actual determinant

Define


$$
\Delta=\mathscr A\Omega-\mathscr B\Pi.
$$


Let


$$
b_K=-\mathscr B=2\ell\mathcal Q(\ell^2)>0,
\qquad
R_j=\mathscr A b_j^\ast-b_Ka_j^\ast.
$$


Then


$$
R_{j+1}=x_jR_j+R_{j-1},
\qquad R_0=-b_K,
$$


and


$$
R_1=2\ell S(\ell),
$$


where


$$
\begin{aligned}
S(\ell)={}&
8\ell^6-152\ell^5+1192\ell^4-4816\ell^3\\
&+10558\ell^2-11274\ell+5486.
\end{aligned}
$$


For $\ell\ge20$,


$$
\begin{aligned}
S(\ell)={}&8\ell^5(\ell-19)
+\ell^3(1192\ell-4816)\\
&+\ell(10558\ell-11274)+5486>8\ell^5.
\end{aligned}
$$


Also


$$
\mathcal Q(\ell^2)<100\ell^4<160\ell^4\le8\ell^5.
$$


Hence $R_1>b_K$, $R_2>R_1>0$, and all later $R_j$ are positive and increasing.

The transported coefficients give


$$
-\Delta
=nR_6\alpha^2+2(n-1)R_5\alpha\beta+(n-2)R_4\beta^2.
$$


Set


$$
t_0=R_3/R_4\in(0,1),\qquad
x_0=R_5/R_4=4(n-2)+t_0.
$$


The determinant of this quadratic form, divided by $R_4^2$, is


$$
\begin{aligned}
&n(n-2)(4(n-1)x_0+1)-(n-1)^2x_0^2\\
&=16(n-1)(n-2)^2+n(n-2)\\
&\quad-4(n-1)(n-2)^2t_0-(n-1)^2t_0^2\\
&>12(n-1)(n-2)^2-1>0.
\end{aligned}
$$


The first diagonal coefficient is positive. The form is positive definite, and $(\alpha,\beta)\ne(0,0)$. Therefore


$$
\boxed{\Delta<0.}
$$



These ratios are used only for real positivity. No modular division by $R_j$ or $\Delta$ is hidden in this argument.

---

## 12. Integer remainders, determinant-deep cap, and height bill

Define


$$
\mathscr I_1=\Pi\mathscr C_U-\mathscr A C^{\rm s},
\qquad
\mathscr I_2=\Omega\mathscr C_U-\mathscr B C^{\rm s}.
$$


Their coefficients in the actual divided Gaussian data are


$$
\begin{array}{c|c|c}
&\mathscr I_1&\mathscr I_2\\ \hline
\alpha^2&
na_6^\ast\mathscr C_U-\mathscr A(1-nf_6)&
-nb_6^\ast\mathscr C_U-\mathscr B(1-nf_6)\\
\alpha\beta&
2(n-1)(a_5^\ast\mathscr C_U-\mathscr A f_5)&
-2(n-1)(b_5^\ast\mathscr C_U+\mathscr B f_5)\\
\beta^2&
(n-2)a_4^\ast\mathscr C_U-\mathscr A(1-(n-2)f_4)&
-(n-2)b_4^\ast\mathscr C_U-\mathscr B(1-(n-2)f_4)\\
\delta^2&\mathscr A&\mathscr B.
\end{array}
$$



Direct elimination gives


$$
\boxed{
16\Pi U-\mathscr A V
=\mathscr I_1+\Delta\Theta_{\ell-1},
}
$$




$$
\boxed{
16\Omega U-\mathscr B V
=\mathscr I_2-\Delta\Theta_\ell.
}
$$


There is no determinant division.

Moreover,


$$
\mathscr A\mathscr I_2-\mathscr B\mathscr I_1
=\mathscr C_U\Delta,
$$


and


$$
\begin{aligned}
\mathscr C_U={}&
8\ell^6+152\ell^5+1120\ell^4+4816\ell^3\\
&+8642\ell^2+11274\ell+5312>0.
\end{aligned}
$$


Thus the remainders are not both zero, and


$$
J_N^{\rm aff}=\gcd(\mathscr I_1,\mathscr I_2)>0
$$


is an actual numerical joint divisor.

### 12.1 Exact all-prime cap

Let


$$
d_p=v_p(\Delta),\qquad j_p=v_p(J_N^{\rm aff}).
$$


If $d_p>j_p$, choose a remainder of valuation $j_p$. In its elimination identity, the term containing $\Delta$ has greater valuation. The right side therefore has valuation exactly $j_p$.

The left side is an integer linear combination of $U,V$, so it is divisible by $c$. Hence


$$
\boxed{d_p>j_p\Longrightarrow c_p\le j_p.}
$$


This proof works at every prime, including $2$, and at primes dividing any Gaussian or coefficient quantity. It uses no inverse of $16$.

With the actual credit $H_p$ left unchanged,


$$
k_p\le[j_p-H_p]_+.
$$


For


$$
\mathcal D_N^{\rm off}
=
\{p>N:p\nmid L(\ell^2),\ d_p>j_p\},
$$




$$
\prod_{p\in\mathcal D_N^{\rm off}}p^{k_p}\mid J_N^{\rm aff}.
$$


This includes its $p>2N$ portion without any factorial allowance.

### 12.2 Correct exponential bill after Gaussian division

The Gaussian recurrence coefficient has absolute value $2\sqrt5$. Since


$$
2\sqrt5+\frac15<5,
$$


induction gives


$$
|C_j(i)|\le5^j.
$$


Thus


$$
|\alpha|\le5^{N-1}/g_B,\qquad
|\beta|\le5^N/g_B,\qquad
|\delta|\le2\,5^{2N-1}/g_B.
$$


Consequently


$$
H_G=\alpha^2+\beta^2+\delta^2
<5^{4N}/g_B^2.
$$



The six-step recurrences give


$$
|a_j^\ast|,\ |b_j^\ast|,\ |f_j|,\ |g_j|\le(5n)^j
\quad(0\le j\le6).
$$


Also


$$
|P|\le nH_G,\quad |Q|\le5n^2H_G,\quad |C_V|\le2nH_G.
$$


The stated conservative bounds follow:


$$
|\Pi|,|\Omega|\le93750n^8H_G,\qquad
|C^{\rm s}|\le100000n^8H_G.
$$


From the displayed polynomials,


$$
|\mathscr A|<70000n^7,\quad
|\mathscr B|<17000n^5,\quad
|\mathscr C_U|<32000n^6.
$$


Therefore


$$
J_N^{\rm aff}\le
\max(|\mathscr I_1|,|\mathscr I_2|)
\le10^{10}n^{15}H_G,
$$


and


$$
\boxed{
J_N^{\rm aff}
<10^{10}(2N)^{15}\frac{5^{4N}}{g_B^2}.
}
$$



Every transported Gaussian expression and remainder is homogeneous quadratic in the divided data. Thus


$$
\Delta_{\rm raw}=g_B^2\Delta,\qquad
\mathscr I_{i,\rm raw}=g_B^2\mathscr I_i,
$$


and


$$
J_{N,\rm raw}^{\rm aff}=g_B^2J_N^{\rm aff}.
$$


At $p\mid g_B$, the actual remainder valuation loses exactly $2v_p(g_B)$ from its raw value.

**Verdict: PASS.** The determinant-depth comparison and the numerical height bill are valid after, not before, the actual Gaussian division.

---

## 13. Complete non-arc $p^2$-block

Let


$$
N<p<2N,\qquad p\nmid2N-1.
$$


Then $p$ is odd, and


$$
r=n-p
$$


is odd with $3\le r<N$. The actual $K$-residual is


$$
s=r-6,\qquad \ell=p+s.
$$



### 13.1 Polynomial and factorial boundaries

For $r\ge7$, put $w=1-2z$ and


$$
S_p(z)=(w^2-1)\mathcal U_{p-1}(w).
$$


The exact addition formula is


$$
T_{p+j}(w)=T_p(w)T_j(w)+S_p(z)\mathcal U_{j-1}(w).
$$


The square identity


$$
F(1-z)^2
=\frac{\alpha^2+\beta^2}{2}-\alpha\beta w
+\frac{\alpha^2}{2}T_n(w)
+\frac{\beta^2}{2}T_{n-2}(w)
-\alpha\beta T_{n-1}(w)
$$


therefore uses exactly $r,r-1,r-2$ after the $p$-block split. At the endpoint, the cross signs reverse:


$$
F(z)^2
=\frac{\alpha^2+\beta^2}{2}+\alpha\beta w
+\frac{\alpha^2}{2}T_n(w)
+\frac{\beta^2}{2}T_{n-2}(w)
+\alpha\beta T_{n-1}(w).
$$


The $K$-square uses $s=r-6$, because


$$
C_m^2=(1+C_\ell)/2.
$$


Every displayed product has degree at most $n$.

For $r=3,5$, the $K$-indices are respectively


$$
(\ell,\ell-1)=(p-3,p-4),\qquad(p-1,p-2),
$$


and are evaluated in the actual base block. No negative residual index is introduced.

Since $n<2p$, write any original polynomial uniquely as


$$
H(z)=H_0(z)+z^pH_1(z),\qquad \deg H_0,\deg H_1<p.
$$


Wilson’s congruence gives


$$
(p+j)!\equiv-pj!\pmod{p^2}.
$$


Hence


$$
\mathcal M_+(H)\equiv
\mathcal M_+(H_0)-p\mathcal M_+(H_1)\pmod{p^2},
$$




$$
\mathcal M_-(H)\equiv
\mathcal M_-(H_0)+p\mathcal M_-(H_1)\pmod{p^2}.
$$


The opposite signs are correct.

A factor $T_p(1-2z)-1\in(p,z^p)$ supplies one factorial depth; it cannot generally be discarded modulo $p^2$.

### 13.2 Evaluated recurrence block

Let


$$
\mathcal L_jZ=Z_{j+1}+4jZ_j-Z_{j-1}.
$$


Define


$$
(\mathcal A_0,\mathcal A_1)=(1,0),\qquad
(\mathcal B_0,\mathcal B_1)=(0,1),
$$




$$
\mathcal L_j\mathcal A=\mathcal L_j\mathcal B=0.
$$


Define


$$
(\mathcal D_0,\mathcal D_1)=(0,-4),
$$


and zero initial pairs for $\mathcal E,\mathcal T,\mathcal W$, with


$$
\mathcal L_j\mathcal D=-4\mathcal A_j,\quad
\mathcal L_j\mathcal E=-4\mathcal B_j,
$$




$$
\mathcal L_j\mathcal T=-4\Theta_j,\quad
\mathcal L_j\mathcal W=-4\Phi_j.
$$


All recurrences stop at $j=r-1$.

Put


$$
\begin{aligned}
H_j^+&=\mathcal A_j\Theta_p+
\mathcal B_j(\Theta_{p-1}+1)+\Theta_j,\\
K_j^+&=\mathcal D_j\Theta_p+
\mathcal E_j(\Theta_{p-1}+1)+\mathcal T_j,
\end{aligned}
$$


and


$$
\begin{aligned}
H_j^-&=\mathcal A_j\Phi_p+
\mathcal B_j(\Phi_{p-1}-1)-\Phi_j,\\
K_j^-&=\mathcal D_j\Phi_p+
\mathcal E_j(\Phi_{p-1}-1)-\mathcal W_j.
\end{aligned}
$$


Let $X_j^\pm=H_j^\pm+pK_j^\pm$.

The unperturbed forcings are


$$
\mathcal L_jH^+=2,\qquad
\mathcal L_jH^-=-2(-1)^j=2(-1)^{p+j},
$$


and


$$
\mathcal L_jK^\pm=-4H_j^\pm.
$$


Therefore


$$
X_{j+1}^\pm+4(p+j)X_j^\pm-X_{j-1}^\pm
=f_j^\pm+4p^2K_j^\pm.
$$


At $j=0,1$, the formulas agree with the original states modulo $p^2$, with exact first updates


$$
X_1^+=-4p\Theta_p+\Theta_{p-1}+2,
$$




$$
X_1^-=-4p\Phi_p+\Phi_{p-1}-2.
$$


Finite recurrence uniqueness proves


$$
\boxed{
\Theta_{p+j}\equiv X_j^+\pmod{p^2},\qquad
\Phi_{p+j}\equiv X_j^-\pmod{p^2}
}
$$


for $0\le j\le r$.

### 13.3 All four outputs

Use $X_r^\pm,X_{r-1}^\pm$ at $n,n-1$, and $X_s^\pm,X_{s-1}^\pm$ at $\ell,\ell-1$ when $r\ge7$. For $r=3,5$, use the actual base $K$-states.

The outputs are


$$
\widehat U=
16^{-1}(\mathscr C_U-\mathscr A\widehat\Theta_\ell
-\mathscr B\widehat\Theta_{\ell-1}),
$$




$$
\widehat V=C_V-P\widehat\Theta_n-Q\widehat\Theta_{n-1},
$$




$$
\widehat E_K=
16^{-1}(\mathscr C_E+\mathscr A\widehat\Phi_\ell
+\mathscr B\widehat\Phi_{\ell-1}),
$$




$$
\widehat E_F=C_F^E-P\widehat\Phi_n-Q\widehat\Phi_{n-1},
$$


all modulo $p^2$.

These use the actual coefficients at $N,n,\ell$, not coefficients obtained by replacing $N$ by $r$. The only modular division is by $16$, a unit at the admitted primes.

### 13.4 Exact depth certificate and combined payment

Define


$$
d_{p,N}^{\mathrm{block}}
=\gcd(p^2,\widehat U,\widehat V).
$$


If it is less than $p^2$, then


$$
c_p=v_p(d_{p,N}^{\mathrm{block}})\le1,
\qquad k_p\le[1-H_p]_+.
$$



For


$$
\mathcal C_N^{\rm off}
=
\{N<p<2N:p\nmid L(\ell^2),\ d_{p,N}^{\mathrm{block}}<p^2\},
$$


the restriction $p\nmid2N-1$ is automatic because $2N-1$ is a factor of $L(\ell^2)$.

At $N<p<2N$,


$$
v_p\binom{2N}{N}=1.
$$


Thus


$$
\prod_{p\in\mathcal C_N^{\rm off}}p^{k_p}
\mid\binom{2N}{N},
$$


and its logarithmic mass is at most $2N\log2$.

Combining with the determinant-deep set,


$$
\boxed{
\prod_{p\in\mathcal D_N^{\rm off}\cup\mathcal C_N^{\rm off}}
p^{k_p}
\mid J_N^{\rm aff}\binom{2N}{N}
<10^{10}(2N)^{15}\frac{2500^N}{g_B^2}.
}
$$



**Verdict: PASS.** This pays all depths at the specified primes. It supplies no coverage theorem for their complement.

---

# Part III. Audit of A5 Turn 19

## 14. Exact remaining branch and its boundary admissions

Define


$$
\mathcal S_N=
\{p:N<p<2N,\ p\nmid L(\ell^2),\
d_{p,N}^{\mathrm{block}}=p^2,\ d_p\le j_p\}.
$$


For $p\in\mathcal S_N$,


$$
p^2\mid U,\qquad p^2\mid V.
$$



The factorization


$$
L(\ell^2)
=(n-7)(n-5)(n-9)(n-3)(n-11)(n-1)
$$


is exact. Each factor lies strictly between $0$ and $2p$. Thus a prime $p>N$ divides one of them exactly when it equals that factor. The excluded residuals are


$$
r=1,3,5,7,9,11.
$$


Consequently


$$
\boxed{
r=n-p\ge13,\quad r<N,\quad r\ \text{odd},
\quad s=r-6\ge7.
}
$$


For


$$
k=(p+1)/2=N-(r-1)/2,
$$




$$
\boxed{k\le N-6.}
$$



All new Hermite indices are therefore at most $N$, and all shifted recurrence steps end at $n-1$. Also $p\nmid d_K$, because $p>N>31$ and $p\nmid L(\ell^2)$. This does not imply $p\nmid a_K$.

---

## 15. Independent verification of the universal Hermite anchor

The base congruences can be checked without transferring an arc-specific Gaussian jet.

Let


$$
h_0=(p-1)/2,\qquad k=h_0+1,\qquad \chi_p=2k!.
$$


Over $\mathbb F_p$, the Chebyshev identities


$$
\boxed{
T_k(w)-T_{h_0}(w)=2^{h_0}(w-1)^k,
\qquad
T_k(w)+T_{h_0}(w)=2^{h_0}(w+1)^k
}
$$


hold.

To prove them, substitute $w=(z+z^{-1})/2$. Multiplication of twice the first left side by $z^k$ gives


$$
z^{p+1}+1-z^p-z=(z-1)(z^p-1)=(z-1)^{p+1}.
$$


The plus identity similarly gives $(z+1)^{p+1}$. This is an identity in a Laurent polynomial ring, so it proves the polynomial identities.

At $w=1-2z$,


$$
C_k(1-z)-C_{h_0}(1-z)
\equiv2(-1)^kz^k\pmod p.
$$


Since $2h_0\equiv-1$ and $2k\equiv1\pmod p$, the moment identities give


$$
\Theta_{h_0}+\Theta_k
\equiv(-1)^{h_0}\chi_p\pmod p.
$$


At $w=2t-1$, the plus identity gives


$$
C_k(t)+C_{h_0}(t)\equiv2t^k\pmod p,
$$


and hence


$$
\Phi_{h_0}-\Phi_k\equiv(-1)^k\chi_p\pmod p.
$$



Now define, modulo $p$,


$$
S_j=\Theta_j+\Theta_{p-j},
\qquad
A_j=\Phi_j-\Phi_{p-j}.
$$


Reflection of the original forced recurrences shows that both are homogeneous:


$$
\mathcal L_jS=\mathcal L_jA=0.
$$


At the center,


$$
S_{h_0}=S_{h_0+1},\qquad
A_{h_0}=-A_{h_0+1}.
$$


Backward recurrence has coefficient


$$
4(h_0-a)\equiv-(4a+2)\pmod p.
$$


Therefore its symmetric central solution is governed by $Q_a^{\mathrm H}$, with seeds $1,1$, and its antisymmetric central solution by $P_a^{\mathrm H}$, with seeds $1,3$.

Using the evaluated central values gives


$$
\Theta_p\equiv\chi_pQ_{h_0}^{\mathrm H},
\qquad
\Theta_{p-1}+1\equiv-\chi_pQ_{h_0-1}^{\mathrm H},
$$




$$
\Phi_p\equiv\chi_pP_{h_0}^{\mathrm H},
\qquad
\Phi_{p-1}-1\equiv-\chi_pP_{h_0-1}^{\mathrm H}.
$$


Finally,


$$
Z_{h_0+1}^{\mathrm H}
=(4h_0+2)Z_{h_0}^{\mathrm H}+Z_{h_0-1}^{\mathrm H}
=2pZ_{h_0}^{\mathrm H}+Z_{h_0-1}^{\mathrm H}.
$$


Thus


$$
\boxed{
\begin{aligned}
\Theta_p&\equiv\chi_pQ_{k-1}^{\mathrm H},&
\Theta_{p-1}+1&\equiv-\chi_pQ_k^{\mathrm H},\\
\Phi_p&\equiv\chi_pP_{k-1}^{\mathrm H},&
\Phi_{p-1}-1&\equiv-\chi_pP_k^{\mathrm H}
\end{aligned}
\pmod p.
}
$$



This proof uses only actual states through $p$, moment polynomials through $k$, and Hermite integers through $k\le N-6$. It uses no arc-root hypothesis.

### 15.1 Both actual defect pairs are indispensable

Define the four integers


$$
\sigma_0^+
=\frac{\Theta_p-\chi_pQ_{k-1}^{\mathrm H}}p,\qquad
\sigma_1^+
=\frac{\Theta_{p-1}+1+\chi_pQ_k^{\mathrm H}}p,
$$




$$
\sigma_0^-
=\frac{\Phi_p-\chi_pP_{k-1}^{\mathrm H}}p,\qquad
\sigma_1^-
=\frac{\Phi_{p-1}-1+\chi_pP_k^{\mathrm H}}p.
$$


Their integrality is now proved in the original objects.

Replacing the base states by their Hermite reductions modulo $p^2$ or $p^3$ would discard these actual defects and would be incorrect.

---

## 16. The $Z_0/Z_1$ columns and exact all-depth quotient

Using the residual sequences from the $p^2$-block, define


$$
Z_{0,j}^+
=\chi_p(\mathcal A_jQ_{k-1}^{\mathrm H}
-\mathcal B_jQ_k^{\mathrm H})+\Theta_j,
$$




$$
\begin{aligned}
Z_{1,j}^+={}&
\chi_p(\mathcal D_jQ_{k-1}^{\mathrm H}
-\mathcal E_jQ_k^{\mathrm H})+\mathcal T_j\\
&+\mathcal A_j\sigma_0^+
+\mathcal B_j\sigma_1^+,
\end{aligned}
$$


and


$$
Z_{0,j}^-=
\chi_p(\mathcal A_jP_{k-1}^{\mathrm H}
-\mathcal B_jP_k^{\mathrm H})-\Phi_j,
$$




$$
\begin{aligned}
Z_{1,j}^-={}&
\chi_p(\mathcal D_jP_{k-1}^{\mathrm H}
-\mathcal E_jP_k^{\mathrm H})-\mathcal W_j\\
&+\mathcal A_j\sigma_0^-
+\mathcal B_j\sigma_1^-.
\end{aligned}
$$


Let


$$
Z_j^\pm=Z_{0,j}^\pm+pZ_{1,j}^\pm.
$$



Substitution of the exact defect definitions into $X_j^\pm$ gives


$$
\boxed{
X_j^\pm
=
Z_j^\pm+
p^2(\mathcal D_j\sigma_0^\pm+\mathcal E_j\sigma_1^\pm).
}
$$


This is an exact integer identity.

### 16.1 A direct uniqueness proof of the all-depth transport

The definitions give


$$
\mathcal L_jZ_0^+=2,\qquad
\mathcal L_jZ_0^-=-2(-1)^j,
$$


and


$$
\mathcal L_jZ_1^\pm=-4Z_{0,j}^\pm.
$$


Therefore


$$
Z_{j+1}^\pm+4(p+j)Z_j^\pm-Z_{j-1}^\pm
=f_j^\pm+4p^2Z_{1,j}^\pm,
$$


where $f_j^+=2$ and $f_j^-=2(-1)^{p+j}$.

Define integers $\mathfrak e_j^\pm$ by


$$
\mathfrak e_0^\pm=0,\qquad
\mathfrak e_1^\pm=-4\sigma_0^\pm,
$$




$$
\boxed{
\mathfrak e_{j+1}^\pm
+4(p+j)\mathfrak e_j^\pm-\mathfrak e_{j-1}^\pm
=-4Z_{1,j}^\pm.
}
$$


Then $Z_j^\pm+p^2\mathfrak e_j^\pm$ satisfies the exact original shifted recurrence. Its first two values are the actual states at $p,p+1$: the second equality follows directly from the recurrence at $p$ and the defect formulas.

Finite uniqueness therefore proves


$$
\boxed{
\Theta_{p+j}=Z_j^++p^2\mathfrak e_j^+,\qquad
\Phi_{p+j}=Z_j^-+p^2\mathfrak e_j^-.
}
$$


This proves both the quotient integrality and its all-depth recurrence.

The state identity itself needs the admitted base congruences and finite boundaries; the double source collision is needed later for the divided source and target carries.

**Verdict: PASS.** Both affine forcings and both defect pairs are present, and the final recurrence step is $n-1$.

---

## 17. Full third digits and both source and endpoint tests

Define zero initial pairs for


$$
\mathcal D^{\langle2\rangle},
\mathcal E^{\langle2\rangle},
\mathcal T^{\langle2\rangle},
\mathcal W^{\langle2\rangle},
$$


and


$$
\mathcal L_j\mathcal D^{\langle2\rangle}=-4\mathcal D_j,\qquad
\mathcal L_j\mathcal E^{\langle2\rangle}=-4\mathcal E_j,
$$




$$
\mathcal L_j\mathcal T^{\langle2\rangle}=-4\mathcal T_j,\qquad
\mathcal L_j\mathcal W^{\langle2\rangle}=-4\mathcal W_j.
$$



Set


$$
\begin{aligned}
Y_j^+={}&
\mathcal D_j\sigma_0^++\mathcal E_j\sigma_1^+\\
&+\chi_p(
\mathcal D_j^{\langle2\rangle}Q_{k-1}^{\mathrm H}
-\mathcal E_j^{\langle2\rangle}Q_k^{\mathrm H})
+\mathcal T_j^{\langle2\rangle},
\end{aligned}
$$




$$
\begin{aligned}
Y_j^-={}&
\mathcal D_j\sigma_0^-+\mathcal E_j\sigma_1^-\\
&+\chi_p(
\mathcal D_j^{\langle2\rangle}P_{k-1}^{\mathrm H}
-\mathcal E_j^{\langle2\rangle}P_k^{\mathrm H})
-\mathcal W_j^{\langle2\rangle}.
\end{aligned}
$$


These satisfy


$$
\mathcal L_jY^\pm=-4Z_{1,j}^\pm,\qquad
Y_0^\pm=0,\quad Y_1^\pm=-4\sigma_0^\pm.
$$


Reducing the exact quotient recurrence modulo $p$ proves


$$
\mathfrak e_j^\pm\equiv Y_j^\pm\pmod p,
$$


and hence


$$
\boxed{
\Theta_{p+j}\equiv Z_j^++p^2Y_j^+\pmod{p^3},\quad
\Phi_{p+j}\equiv Z_j^-+p^2Y_j^-\pmod{p^3}.
}
$$



### 17.1 Complete source carries

Define


$$
B_U=\mathscr C_U-\mathscr A Z_s^+-\mathscr B Z_{s-1}^+,
$$




$$
B_V=C_V-PZ_r^+-QZ_{r-1}^+.
$$


The exact identities are


$$
16U=B_U-p^2(\mathscr A\mathfrak e_s^+
+\mathscr B\mathfrak e_{s-1}^+),
$$




$$
V=B_V-p^2(P\mathfrak e_r^++Q\mathfrak e_{r-1}^+).
$$


Since $p^2\mid U,V$, the integers $B_U,B_V$ are divisible by $p^2$.

Thus the actual third source digit is


$$
\boxed{
\begin{aligned}
\mathscr L_U&=
B_U/p^2-\mathscr A Y_s^+-\mathscr B Y_{s-1}^+,\\
\mathscr L_V&=
B_V/p^2-PY_r^+-QY_{r-1}^+
\end{aligned}
\pmod p.
}
$$


It satisfies


$$
\mathscr L_U\equiv16U/p^2,\qquad
\mathscr L_V\equiv V/p^2\pmod p.
$$



A nonzero pair proves


$$
c_p=2,\qquad k_p=[2-H_p]_+.
$$


This is an all-depth conclusion at that prime. The derivation does not prove that the pair is universally nonzero.

### 17.2 Complete endpoint outputs

The endpoint tests are


$$
\begin{aligned}
16E_K\equiv{}&
\mathscr C_E+\mathscr A Z_s^-+\mathscr B Z_{s-1}^-\\
&+p^2(\mathscr A Y_s^-+\mathscr B Y_{s-1}^-)
\pmod{p^3},
\end{aligned}
$$




$$
\begin{aligned}
E_F\equiv{}&
C_F^E-PZ_r^--QZ_{r-1}^-\\
&-p^2(PY_r^-+QY_{r-1}^-)
\pmod{p^3}.
\end{aligned}
$$


Thus $y_K=d_KE_K-a_K$ is evaluated to this precision using its actual reduced numerator and denominator.

All four constants


$$
\mathscr C_U,\quad\mathscr C_E,\quad
\alpha^2+(2n-3)\beta^2-\delta^2,\quad
\alpha^2+(5-2n)\beta^2+4\alpha\beta
$$


remain present.

**Verdict: PASS.** A third digit $Y$ alone would not suffice: the divided carries $B_U/p^2,B_V/p^2$ are essential parts of the actual source test.

---

## 18. Actual target, contact identity, and critical-prime loss

Define the integer carries


$$
\rho_\ell=(\mathscr I_2-\Delta Z_s^+)/p^2,
\qquad
\rho_{\ell-1}=(\mathscr I_1+\Delta Z_{s-1}^+)/p^2.
$$


Their integrality follows from the elimination identities, the actual double source zero, and the exact state transport.

Set


$$
\mathbf T_{p,N}=
\begin{pmatrix}
\rho_\ell-\Delta\mathfrak e_s^+\\
\rho_{\ell-1}+\Delta\mathfrak e_{s-1}^+
\end{pmatrix}.
$$


The exact identity is


$$
\boxed{
\mathbf T_{p,N}
=
\begin{pmatrix}
\Omega&-\mathscr B\\
\Pi&-\mathscr A
\end{pmatrix}
\begin{pmatrix}
16U/p^2\\V/p^2
\end{pmatrix}.
}
$$


For example, multiplying the first coordinate by $p^2$ gives


$$
\mathscr I_2-\Delta\Theta_\ell
=16\Omega U-\mathscr B V.
$$


The second coordinate is checked similarly.

Modulo $p$,


$$
\mathbf T_{p,N}\equiv
\begin{pmatrix}
\rho_\ell-\Delta Y_s^+\\
\rho_{\ell-1}+\Delta Y_{s-1}^+
\end{pmatrix}.
$$



### 18.1 Unit determinant

The matrix has determinant $-\Delta$. If $p\nmid\Delta$, it is an automorphism over $\mathbb Z_p$, so


$$
\boxed{
c_p-2
=
\min\bigl(
v_p(\rho_\ell-\Delta\mathfrak e_s^+),
v_p(\rho_{\ell-1}+\Delta\mathfrak e_{s-1}^+)
\bigr).
}
$$



The actual target is unchanged:


$$
\boxed{
\Theta_\ell^*=\frac{\mathscr I_2}{\Delta},
\qquad
\Theta_{\ell-1}^*=-\frac{\mathscr I_1}{\Delta}.
}
$$


Indeed,


$$
\mathscr A\Theta_\ell^*
+\mathscr B\Theta_{\ell-1}^*=\mathscr C_U,
$$




$$
\Pi\Theta_\ell^*+\Omega\Theta_{\ell-1}^*=C^{\rm s}.
$$


Thus the complete source coefficient matrix, not a homogeneous substitute, gives


$$
c_p=
\min\left(
v_p(\Theta_\ell-\Theta_\ell^*),
v_p(\Theta_{\ell-1}-\Theta_{\ell-1}^*)
\right).
$$



A third common depth survives precisely when


$$
\rho_\ell\equiv\Delta Y_s^+,\qquad
\rho_{\ell-1}\equiv-\Delta Y_{s-1}^+\pmod p.
$$


This is an evaluated collision criterion, not an avoidance theorem.

### 18.2 Determinant-critical primes: both inequalities

Let


$$
a_p=\min(v_p(T_{p,N,1}),v_p(T_{p,N,2})),
\qquad d_p=v_p(\Delta).
$$


Because the contact matrix has integer coefficients,


$$
a_p\ge c_p-2.
$$


Multiplication by its integer adjugate yields $-\Delta$ times the source vector. The resulting coordinates all have valuation at least $a_p$, while their minimum valuation is $d_p+c_p-2$. Therefore


$$
a_p\le c_p-2+d_p.
$$


Hence


$$
\boxed{c_p-2\le a_p\le c_p-2+d_p.}
$$



The contact vector is not identically zero: $\Delta\ne0$, and $U,V>0$. Thus the minimum valuation is finite.

**Verdict: PASS.** The upper inequality has the correct direction. It controls conditioning loss only. It does not bound $a_p$, and therefore does not prove $c_p\le d_p+2$.

At critical primes, the direct source test remains valid without determinant inversion. A zero adjugate digit need not mean that the direct source digit is zero.

---

## 19. Complete credit splitting and quantified payment

For $c_p\ge2$,


$$
\boxed{
[c_p-H_p]_+
=
[2-H_p]_+
+[c_p-2-(H_p-2)_+]_+.
}
$$


If $H_p\le2$, this is immediate because $c_p-2\ge0$. If $H_p>2$, both sides reduce to $[c_p-H_p]_+$.

Since $N<p<2N$,


$$
\prod_{p\in\mathcal S_N}p^{[2-H_p]_+}
\mid\binom{2N}{N}^2,
$$


and


$$
\sum_{p\in\mathcal S_N}[2-H_p]_+\log p
\le4N\log2.
$$



Define the actual full-depth contact quantity


$$
\mathfrak C_N^{\rm lift}
=
\sum_{p\in\mathcal S_N}
[a_p-(H_p-2)_+]_+\log p.
$$


The positive-part function is increasing and $1$-Lipschitz. The two-sided valuation comparison therefore gives


$$
\boxed{
\begin{aligned}
0\le{}&
\sum_{p\in\mathcal S_N}[2-H_p]_+\log p
+\mathfrak C_N^{\rm lift}
-\sum_{p\in\mathcal S_N}k_p\log p\\
\le{}&\sum_{p\in\mathcal S_N}d_p\log p
\le\log|\Delta|.
\end{aligned}}
$$



All components of


$$
H_p=h_p+2b_p+2(z_p-t_p)_+
$$


are still the actual components. In particular:

- $h_p$ uses $Q_{N-1}^{\mathrm H}Q_N^{\mathrm H}$;
- $b_p$ is not set to zero merely because $p\nmid d_K$;
- deeper endpoint zeros are not assigned truncated valuations.

### 19.1 A new sharper determinant-conditioning bill

The determinant contains no $\delta$. Put


$$
H_2=\alpha^2+\beta^2
\le\frac{26}{25}\frac{5^{2N}}{g_B^2}.
$$


From the exact forms before expansion,


$$
\Pi=Pa_6^\ast-Qa_5^\ast,\qquad
\Omega=-Pb_6^\ast+Qb_5^\ast,
$$


we obtain the stronger bounds


$$
|\Pi|,|\Omega|
\le nH_2(5n)^6+5n^2H_2(5n)^5
=31250n^7H_2.
$$


Therefore


$$
\begin{aligned}
|\Delta|
&\le(|\mathscr A|+|\mathscr B|)
\max(|\Pi|,|\Omega|)\\
&<(70000n^7+17000n^5)\,31250n^7H_2\\
&\le2{,}718{,}750{,}000\,n^{14}H_2\\
&<3\cdot10^9n^{14}\frac{5^{2N}}{g_B^2}.
\end{aligned}
$$


Thus


$$
\boxed{
\log|\Delta|
<
2N\log5+14\log(2N)+\log(3\cdot10^9)-2\log g_B.
}
$$



This is a new proved improvement in the paid conditioning loss. The remainder divisor $J_N^{\rm aff}$ still has its separate $5^{4N}$ bill because its complete source constant contains $\delta^2$.

### 19.2 The avoidance implication remains conditional

If, for every $p\in\mathcal S_N$,


$$
(\mathscr L_U,\mathscr L_V)\ne(0,0)\pmod p,
$$


then $c_p=2$, and


$$
k_p=[2-H_p]_+\le2.
$$


Partitioning the non-arc interval into determinant-deep primes, noncolliding $p^2$-block primes, and $\mathcal S_N$, one obtains


$$
\boxed{
\prod_{\substack{N<p<2N\\p\nmid L(\ell^2)}}p^{k_p}
\mid J_N^{\rm aff}\binom{2N}{N}^{\,2}.
}
$$


The single square of the binomial coefficient covers both the first-depth noncollision set and the remaining depth-$2$ set; a third binomial factor is not needed. Hence, conditionally,


$$
\prod_{\substack{N<p<2N\\p\nmid L(\ell^2)}}p^{k_p}
<
10^{10}(2N)^{15}\frac{10000^N}{g_B^2}.
$$



**Verdict: PASS as an implication; OPEN as a universal conclusion.**

Neither coefficient primitiveness, determinant invertibility, coefficient height, a period-density statement, nor an ordinary resultant proves the required actual nonzero pair.

---

## 20. Exact division and precision bill for the Hermite lift

Let


$$
a=v_p(g_B),\qquad g_B=p^ag_0,\qquad p\nmid g_0.
$$



1. **Gaussian data.** To obtain $\alpha,\beta,\delta\bmod p^3$, raw linear data must be sufficient through $p^{a+3}$, followed by the proved $p^a$-division and division by the actual unit $g_0$. A raw quadratic expression divided afterwards must be known modulo $p^{2a+3}$.

2. **Hermite defects.** To obtain $\sigma^\pm\bmod p^2$, their numerators must be known modulo $p^3$. The division by $p$ is justified by the proved base congruences. The factorial $k!$ is a unit because $k<p$, but no division by it is used.

3. **Second-collision carries.** To compute
   

$$
B_U/p^2,\ B_V/p^2,\ \rho_\ell,\ \rho_{\ell-1}\pmod p,
$$


   their numerators must be known modulo $p^3$. A double-zero input does not supply these quotient digits without the extra precision.

4. **State precision.**
   

$$
Z_{0,j}^\pm\bmod p^3,\qquad
   Z_{1,j}^\pm\bmod p^2,\qquad
   Y_j^\pm\bmod p
$$


   are the appropriate levels.

5. **Determinant.** No determinant division occurs in the direct source tests or the contact identity. At a determinant unit, inversion is legitimate. At depth $d_p>0$, recovering source precision $p^b$ from adjugate data generally requires precision $p^{b+d_p}$.

6. **Full credits.** Endpoint data modulo $p^3$ determine only truncated endpoint valuations when a deeper zero occurs. A post-credit certificate $c_p\le H_p+2$ requires validated information about the actual $H_p$ and source precision through $p^{H_p+3}$.

All residual states have indices at most $r<N$, all shifted steps stop at $n-1$, and all Hermite indices remain at most $N$.

---

## 21. Symbolic audit of the optional constant-size receipt

No execution is required. The receipt’s claims follow by two polynomial substitutions.

With formal inputs $z,S,B$, source seed


$$
Y_0=S,\qquad Y_1=-4zS+B+1,
$$


and endpoint seed


$$
Y_0=S,\qquad Y_1=-4zS+B-1,
$$


the coefficients are:



$$
\begin{array}{c|c|c|c|c}
j&[S]Y_j&[B]Y_j&\text{source constant}&\text{endpoint constant}\\ \hline
2&
1+16z+16z^2&
-4-4z&
-2-4z&
6+4z\\
3&
-8-136z-192z^2-64z^3&
33+48z+16z^2&
19+40z+16z^2&
-51-56z-16z^2.
\end{array}
$$


The second corrections give


$$
\mathcal D_2^{\langle2\rangle}=16,\qquad
\mathcal E_2^{\langle2\rangle}
=\mathcal T_2^{\langle2\rangle}
=\mathcal W_2^{\langle2\rangle}=0,
$$


and


$$
\mathcal D_3^{\langle2\rangle}=-192,\qquad
\mathcal E_3^{\langle2\rangle}
=\mathcal T_3^{\langle2\rangle}
=\mathcal W_3^{\langle2\rangle}=16.
$$



**Verdict: PASS as constant-size polynomial identities.** They check signs and correction coefficients, not an original-family noncollision. No old prime receipt or scan is reopened.

---

# Part IV. Complete producers, forcing, primitive normalization, and whole errors

## 22. A1 actual producer remains distinct from the audited core

The actual producer is still


$$
Q_{\rm act}=Q_c+3^7\mathscr R.
$$


The complementary core theorem is not an actual/core transport theorem.

Retain


$$
F_{\rm fac}=(n-1)!,
\qquad
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},\quad0\le a,b<n,
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


The complete coefficients are


$$
[x^a](3^7\mathscr R)
=-\frac{F_{\rm fac}}{a!}
\bigl((t_{\rm force})_a+\xi v_a\bigr),
\quad0\le a\le n-1,
$$


and


$$
\mathscr R(-1)=-\frac{\xi F_{\rm fac}^2}{3^7}.
$$



The forcing identity remains


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$


Both terms and the physical terminal remain.

The complete moment recurrence is


$$
\mu_{r+1}+\mu_r
=
\frac{3^h}{2r+1}
-\frac{3^h}{4}\bigl((2r+2)!+(2r)!\bigr),
\quad0\le r\le2n-2.
$$


For the retained label $r_*=(3^h-5)/2$, the pole of this displayed denominator is at $r_*+2$, not at $r_*$.

The later diagonal payments remain


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


No unit numerator is assumed.

The accepted higher ternary block gate is not reopened. Its discharged local/weighted dependency does not supply the missing complete physical-$7$/source-$34$ contraction.

### 22.1 A1 primitive pair and whole error

No new content calculation has been obtained. The least simultaneous clearer remains the actual $\ell_{\rm clr}$. Put


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and use the gcd over all primes:


$$
G=\gcd(|A_\ell|,|B_\ell|).
$$


For $B_\ell\ne0$,


$$
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{G},
\qquad q=\frac{|B_\ell|}{G}.
$$


The whole evaluated error is


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
G\det H_{\rm complete}.
}
$$



The local endpoint theorem does not establish


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


or


$$
\log G-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|\longrightarrow+\infty
$$


at the same infinite original indices.

---

## 23. A5 complete forcing and returns are unchanged

The source balance follows exactly from $\nu U-\tau V=0$:


$$
\begin{aligned}
&(\nu\mathscr A-16\tau\Pi)\Theta_\ell
+(\nu\mathscr B-16\tau\Omega)\Theta_{\ell-1}\\
&\hspace{12mm}=\nu\mathscr C_U-16\tau C^{\rm s}.
\end{aligned}
$$


For


$$
T=\tau(E_F-\delta^2)+\nu E_K,
$$


the endpoint is


$$
\begin{aligned}
16T={}&16\tau(C^{\rm e}-\delta^2)+\nu\mathscr C_E\\
&+(\nu\mathscr A-16\tau\Pi)\Phi_\ell
+(\nu\mathscr B-16\tau\Omega)\Phi_{\ell-1}.
\end{aligned}
$$



### 23.1 Source and endpoint returns

The source return has


$$
z_\ell^{\rm ret}=16\Omega U-\mathscr B V,\qquad
z_{\ell-1}^{\rm ret}=\mathscr A V-16\Pi U,
$$




$$
z_j^{\rm ret}=-\Delta\Theta_j+\varrho_j,
$$




$$
\varrho_\ell=\mathscr I_2,\qquad
\varrho_{\ell-1}=-\mathscr I_1,
$$




$$
\varrho_{j-1}=\varrho_{j+1}+4j\varrho_j-2\Delta.
$$


The forcing cancels exactly, leaving


$$
z_{j-1}^{\rm ret}=z_{j+1}^{\rm ret}+4jz_j^{\rm ret}.
$$



After actual arc clearing, define


$$
k_E=D\mathscr C_E-16DR_K,\qquad
f_E=DC^{\rm e}-DR_F.
$$


The endpoint return is


$$
w_\ell=16\Omega Y+\mathscr B X,\qquad
w_{\ell-1}=-16\Pi Y-\mathscr A X,
$$




$$
w_j=D\Delta\Phi_j+\sigma_j,
$$


where


$$
\sigma_\ell=\Omega k_E+\mathscr Bf_E,\qquad
\sigma_{\ell-1}=-\Pi k_E-\mathscr Af_E,
$$




$$
\sigma_{j-1}
=\sigma_{j+1}+4j\sigma_j+2D\Delta(-1)^j.
$$


Again the complete forcing cancels, giving a homogeneous return. Direct expansion yields


$$
\boxed{
z_\ell^{\rm ret}w_{\ell-1}
-z_{\ell-1}^{\rm ret}w_\ell
=-16\Delta(UX+VY).
}
$$


No determinant division occurs.

For exactly $0\le a\le N$, the canonical return is


$$
\mathcal R_{a;N}=d_KP_a^{\mathrm H}U+Q_a^{\mathrm H}y_K.
$$


With


$$
\Psi_j^{(a)}=Q_a^{\mathrm H}\Phi_j-P_a^{\mathrm H}\Theta_j,
$$




$$
\Psi_{j+1}^{(a)}+4j\Psi_j^{(a)}-\Psi_{j-1}^{(a)}
=2(Q_a^{\mathrm H}(-1)^j-P_a^{\mathrm H}),
$$


and


$$
\begin{aligned}
16\mathcal R_{a;N}
={}&d_K\bigl(
P_a^{\mathrm H}\mathscr C_U+Q_a^{\mathrm H}\mathscr C_E
+\mathscr A\Psi_\ell^{(a)}
+\mathscr B\Psi_{\ell-1}^{(a)}
\bigr)\\
&-16Q_a^{\mathrm H}a_K.
\end{aligned}
$$


Both forcings, both constants, and the reduced arc term remain.

The old rational interface retains its actual clearers


$$
Q_{\rm loc}(n)=\prod_{a=0}^{12}(n-a),\qquad
\mathcal L_n=\operatorname{lcm}(1,\ldots,n),
$$


and its nonsingular forcing identity


$$
\frac{2\mathcal L_n}{j^2-1}
=\frac{\mathcal L_n}{j-1}-\frac{\mathcal L_n}{j+1}.
$$


Neither is the least simultaneous arc clearer.

---

## 24. A5 least clearers, all-prime final gcd, primitive denominator

Retain


$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,\qquad
R_K=4\int_0^1\frac K{1+t^2}\,dt.
$$


The monic quotient degrees are at most $2N-2$.

The complete square-arc return has zero seeds at $0,1$, and


$$
\xi_{j+1}=4\upsilon_j-2\xi_j-\xi_{j-1}+16b_j,
$$




$$
\upsilon_{j+1}
=-4\xi_j-2\upsilon_j-\upsilon_{j-1}+16(\ell_j-a_j),
$$


where


$$
\ell_j=
\begin{cases}
0,&j\text{ odd},\\
(1-j^2)^{-1},&j\text{ even}.
\end{cases}
$$


Its physical output is


$$
R_F=
\frac{\alpha^2\xi_n+\beta^2\xi_{n-2}
-2\alpha\beta\xi_{n-1}}2.
$$



After reducing both arcs completely,


$$
D=\operatorname{lcm}(\operatorname{den}R_F,\operatorname{den}R_K),
$$




$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K).
$$


Independently reduce


$$
\tau R_F+\nu R_K=b/\lambda,\qquad
\gcd(b,\lambda)=1,\quad\lambda>0.
$$


Then


$$
E=\tau E_F+\nu E_K,\qquad A=\lambda E-b,
$$




$$
\boxed{G=\gcd(M,A),\qquad p_N=A/G,\qquad q_N=\lambda M/G.}
$$


The gcd is over all primes.

Because


$$
\gcd(\lambda,A)=\gcd(\lambda,b)=1,
$$




$$
\gcd(A,\lambda M)=\gcd(A,M)=G.
$$


Thus $q_N$ is the actual primitive denominator. None of $\Delta$, $J_N^{\rm aff}$, a binomial payment, or a local modular inverse replaces $D,\lambda$, or $G$.

---

## 25. A5 whole nonzero error at the same original indices

The producer is


$$
P_N(t)=\frac{F^2+(V/U)K}{\delta^2}
=\frac{W_{\rm prim}}M.
$$


Since $U,V>0$, $\delta\ne0$, and $F^2,K\ge0$ on $[0,1]$, with a nonzero polynomial numerator,


$$
\epsilon_N=
\int_0^1P_N(t)\left(e^t+\frac4{1+t^2}\right)\,dt>0.
$$



The exact balance is


$$
\eta(W_{\rm prim})
=\tau(\delta^2+V)-\nu U=M.
$$


Finite integration by parts gives


$$
\int_0^1e^tW_{\rm prim}(t)\,dt=eM-E.
$$


The arc relation gives


$$
4\int_0^1\frac{W_{\rm prim}(t)}{1+t^2}\,dt
=\pi M+b/\lambda.
$$


Therefore


$$
\epsilon_N=e+\pi-\frac{A}{\lambda M},
$$


and


$$
\boxed{
q_N(e+\pi)-p_N=q_N\epsilon_N>0.
}
$$



The complete enclosure remains


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


and, with $j_a=(1-4a^2)^{-1}$,


$$
J_K=\frac{61}{420}
+\frac{
916j_m-399(j_{m+1}+j_{m-1})
-58(j_{m+2}+j_{m-2})
-(j_{m+3}+j_{m-3})
}{8192}.
$$


Thus


$$
\boxed{
q_NJ_N=\frac{\lambda_N}{G_N}
(\tau_NJ_F+\nu_NJ_K).
}
$$


Both positive summands are retained.

A future strict all-prime multiplier estimate has only its supplied conditional consequence: it would make this primitive whole error grow and retire this producer. It would not decide the rationality of $e+\pi$.

---

# Part V. Status, exact obstructions, and continuation

## 26. PASS / REPAIR / OPEN ledger

### A1 Turn 19

| Claim | Audit result |
|---|---|
| Original complementary index and finite degree | **PASS** |
| New HIGH division by $9$ | **PASS**, termwise on the actual interval |
| Three-digit LOW source and terminal LOW grading | **PASS** |
| New HIGH support $15+3(14)\bmod9$ | **PASS**, without boundary extension |
| $M_L,M_H$ orientation and reflection/shift rules | **PASS**, for actual finite blocks |
| Exact block formula with physical LOW inverse $1/3$ | **PASS** |
| Source-side mixed LOW return to whole depth $30$ | **PASS** |
| Terminal-side mixed LOW return to whole depth $30$ | **PASS** |
| Fourteen-term shifted bulk annihilation | **PASS**, including quotients and lower mask |
| Exceptional module pairing | **PASS** |
| Dependence on terminal-module and prefix/bare audits | **REPAIR of status:** those dependencies are discharged |
| $\eta_I=0$ | **PASS** at original sufficiently large core indices, in its residual normalization |
| Alternating scalar and full endpoint moment block | **PASS** in the leading frame |
| Literal unreduced $3$-adic moment-zero interpretation | **Not justified**; the vanishing is at the stated characteristic-$3$ precision |
| Full physical-$6$ direction and $R_4$ evaluation | **OPEN here**; separate first-four work not duplicated |
| Actual physical $7$/source $34$ | **OPEN** |

### A5 Turn 18

| Claim | Audit result |
|---|---|
| Actual divided Gaussian normalization | **PASS** |
| Six-step coefficient transport and both forcing corrections | **PASS** |
| All four complete constants | **PASS** |
| Strict negativity of actual $\Delta$ | **PASS** |
| Integer remainder coefficients and identities | **PASS** |
| Numerical joint divisor is nonzero | **PASS** |
| Determinant-deep source cap | **PASS at every prime** |
| Raw-to-divided height and valuation bill | **PASS** |
| Complete non-arc $p^2$-block | **PASS**, including $r=3,5$ boundary admissions |
| Binomial payment for certified noncollisions | **PASS** |
| Coverage or useful bound for all remaining primes | **OPEN** |

### A5 Turn 19

| Claim | Audit result |
|---|---|
| Non-arc residual $r\ge13$, $s\ge7$, $k\le N-6$ | **PASS** |
| Universal Hermite base congruences | **PASS**, independently derived above |
| Both actual defect pairs | **PASS**, integral and indispensable |
| $Z_0/Z_1$ columns | **PASS** |
| All-depth quotient recurrence and seeds | **PASS** |
| Full $Y^\pm$ third corrections | **PASS** |
| Both complete source and endpoint tests modulo $p^3$ | **PASS** |
| Actual target and determinant-unit contact identity | **PASS** |
| Two-sided critical-prime loss bound | **PASS** |
| Full-credit positive-part splitting | **PASS** |
| First-two-layer binomial payment | **PASS** |
| $\mathfrak C_N^{\rm lift}$ comparison with at most $\log|\Delta|$ loss | **PASS** |
| Improved $5^{2N}/g_B^2$ determinant bill | **NEW PROVED CONSEQUENCE** |
| Universal third-depth avoidance | **OPEN** |
| Exponential full non-arc interval bound | **CONDITIONAL** |
| All-prime strict factorial saving | **OPEN** |

---

## 27. Precise obstructions and a concrete follow-on lemma

### 27.1 A1 obstruction

The scalar


$$
-z_{\mathrm{end}}^TR_4z_{\mathrm{end}}
$$


does not evaluate the full first-four return, and


$$
B_6z_{\mathrm{alt}}
=B^0z_{\mathrm{alt}}-\varepsilon_{\mathrm{alt}}N^T\eta
$$


still contains the unknown interior residual vector.

The next needed local input is the actual complete first-four returned data, including the mixed-prefix division and upper $3y$ corner. That work is assigned separately. Even after it is available, actual/core transport and the physical-$7$/source-$34$ stationary contraction remain necessary.

### 27.2 A5 obstruction

At a determinant-unit prime, the unresolved cancellation is exactly


$$
\rho_\ell\equiv\Delta Y_s^+,\qquad
\rho_{\ell-1}\equiv-\Delta Y_{s-1}^+\pmod p,
$$


and its higher-depth continuation through the exact quotient recurrence.

A unit determinant makes the source and state-contact formulations equivalent. It does not make either nonzero. The exponential heights of $\mathscr I_1,\mathscr I_2,\Delta$ do not bound the precision with which the actual forced states approach the actual rational target.

At critical primes, the conditioning loss is paid, but the contact itself is not.

A concrete sufficient continuation lemma is:

> **Actual post-credit continuation lemma — open.**  
> For every original $N$ and $p\in\mathcal S_N$, using the actual $H_p$, prove that the two exact integers
> 

$$
> B_U/p^2-\mathscr A\mathfrak e_s^+
> -\mathscr B\mathfrak e_{s-1}^+,
>
$$


> 

$$
> B_V/p^2-P\mathfrak e_r^+-Q\mathfrak e_{r-1}^+
>
$$


> are not both divisible by $p^{H_p+1}$, or prove an $O(N)$ logarithmic bound for the excesses at the exceptions.

The displayed pair is exactly $(16U/p^2,V/p^2)$. The proposed nonvanishing would prove $c_p\le H_p+2$, hence $k_p\le2$, and would give the same exponential interval payment. Its first layer is the explicit third-digit pair audited above. The lemma remains an arithmetic obligation; naming it does not prove it.

For $p>2N$, all factorials in the original degree range are units. The coefficient of $z$ in $K(1-z)$ is $4$, and $\gcd(\alpha,\beta)=1$ ensures that $F$ remains nonconstant modulo an odd prime. These facts rule out an automatic coefficient-content substitute for the missing factorial tail, but do not prove either factorial functional is a unit.

The remaining smaller primes, determinant-unit primes above $2N$, critical determinant primes, and surviving interval contacts all remain part of the all-prime obligation.

Finally, since successive original A5 indices have ratio $3^{64}>2$, a fixed prime belongs to $N<p<2N$ for at most one original $N$. Fixed-prime period arguments do not automatically produce admissible interval lifts.

---

## 28. Computation status and final conclusion

No original matrix, inverse solve, table, or prime scan was executed or requested. No new bounded execution is indispensable for the symbolic proofs in this report.

The only auxiliary bounded objects discussed were the formal degree-three recurrence identities in Section 21. Their fixed inputs are $\mathbb Z[z,S,B]$, the two stated seeds, and indices $0,1,2,3$; their expected outputs are the displayed coefficient table and second-correction values. Their scope is algebraic bookkeeping only. They do not test an original $N$, prove avoidance, or bound the remaining prime mass.

The new proved conclusions are:



$$
\boxed{
G_c(F[y^{\nu-1}],F[p_{k-1}])\in3^{30}\mathbb Z_3,
\qquad \eta_{k-1}=0
}
$$


at the original sufficiently large A1 core indices, with both mixed LOW returns fully paid;

the full A5 transport, lifting, and post-credit payment identities at their stated scopes; and the sharper determinant bill


$$
\boxed{
0<|\Delta|
<3\cdot10^9(2N)^{14}\frac{5^{2N}}{g_B^2}.
}
$$



The exact unresolved global bottleneck is still the primitive arithmetic of the complete producers:

- for A1, the actual transport, contents, least clearer, all-prime final $G$, primitive denominator, and a nonzero whole error tending to zero at the same infinite original indices;
- for A5, the surviving full post-credit contact mass, the remaining prime ranges, and the all-prime factorial-saving question, with the actual $D,\lambda,G,q_N$ and whole positive error retained.

If $e+\pi=a/b$ were rational, every nonzero integer linear error would have absolute value at least $1/b$. Neither audited construction presently supplies a same-index sequence of nonzero primitive whole errors tending to zero.



$$
\boxed{\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$


