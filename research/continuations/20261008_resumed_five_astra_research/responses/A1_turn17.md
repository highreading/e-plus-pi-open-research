> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1, Turn 17 — A second actual finite HIGH direction and its complete source contraction

## Abstract and status

The requested value


$$
w_1^Tf_H\pmod{3^{25}}
$$


is **not yet evaluated**. In particular, this report does not give the precision-$27$ certificate requested in the primary assignment.

There is, however, a new source-specific finite directional calculation. Put


$$
V=\frac H9,\qquad T=\frac H3=3V,
$$


and retain the actual finite quotient


$$
P_d(y)=\sum_{i=0}^{\nu}\binom{D+i-1}{i}y^{\nu-i}.
$$


Define the integral HIGH polynomial


$$
\boxed{
\begin{aligned}
\widehat Z_1(y)
={}&x^D\left(
y^{4V+\nu-1}-y^{2V+\nu-1}+y^{V+\nu-1}
-y^T P_d(y)
\right)\\
&\quad+y^{d+2}-y^d .
\end{aligned}}
\tag{A}
$$



I prove, using the literal finite HIGH inverse and its two edge masks, that


$$
\boxed{w_1\equiv\widehat z_1\pmod3.}
\tag{B}
$$


Consequently,


$$
\boxed{
\mathcal S_H(e_d+3z_0+9\widehat z_1)-\upsilon_T
\in3^3\mathbb Z_3^{\{d,\ldots,m\}}.
}
\tag{C}
$$


The exponent in (C) is **$3$, not $27$**. Thus $\widehat z_1$ is a chosen integral lift of the next digit, not an actual inverse solution modulo $3^{25}$.

The whole contraction of this particular lift is nevertheless evaluated, with all fourteen source terms and both channels:


$$
\boxed{\widehat z_1^Tf_H\in3^{29}\mathbb Z_3.}
\tag{D}
$$


This is substantially stronger than a leading-support calculation.

Define the next actual vector by the paid division


$$
w_2=\frac{w_1-\widehat z_1}{3}.
$$


Then the remaining endpoint problem becomes


$$
\boxed{
w_1^Tf_H\equiv3w_2^Tf_H\pmod{3^{25}},
\qquad
a\eta_0=\frac{w_2^Tf_H}{3^{23}}\pmod3,
}
\tag{E}
$$


where


$$
w_2^Tf_H\in3^{23}\mathbb Z_3
$$


uses the inherited endpoint divisibility.

A complete polynomial formula for the next force, including the surviving LOW return, is also obtained below. No LOW return is removed from


$$
\boxed{\mathcal S_H=E_Y-3\mathcal X^TM_L\mathcal X.}
$$



Neither endpoint, the actual physical-seven layer, nor the global rationality question for $e+\pi$ is settled.

---

## 1. Original objects and exact scope of reuse

### 1.1 The original index family is unchanged

All uniform assertions concern sufficiently large tuples in exactly the supplied original domain:


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


so that


$$
N_0=25P+2\chi,\qquad D=268P+2\chi.
$$


The real Range III restriction remains


$$
\boxed{\frac3{25}<\frac{\chi}{P}<\frac{31}{250}.}
\tag{1.1}
$$



Set


$$
\Pi=P/3,\qquad t=\Pi-2\chi,\qquad k=3\chi-\Pi-1,
$$


and retain


$$
v_3(\chi)=5,\qquad \chi/243\equiv1\pmod9.
$$


Write


$$
S=h-32,\qquad P=3^S,\qquad H=3^{S+31},
$$


and take $S\ge31$.

No independent choices of $P$ and $\chi$ are made. The inherited infinitude statement is used only at this original-index scope.

For the new calculation,


$$
V=H/9=3^{29}P,\qquad T=H/3=3V.
$$


In particular,


$$
V>3000P>4D+10.
\tag{1.2}
$$


This stronger separation, available in the original family, will pay all new finite support assertions.

### 1.2 Literal finite spaces and the complete core

The spaces remain


$$
U_u=x^u,\quad 0\le u<D,\qquad x=y-1,
$$




$$
z_i^{\rm mid}=x^Dy^i,\quad 0\le i<\nu,\qquad \nu=D/2-1,
$$




$$
Y_s=y^s,\quad d\le s\le m,\qquad d=D+\nu=\frac{3D}{2}-1.
$$


Thus


$$
m+\nu=r_H,\qquad r_H=\frac{H-1}{2}.
$$



The physical HIGH terminal is $Y_m$. The last middle polynomial remains $y^{\nu-1}$.

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


The core producer and corrected columns are


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=D-H-71,
$$




$$
G_c(f,g)=\mathcal M(Q_cfg),\qquad W=[U\ Y],\qquad E_c=G_c(W,W),
$$




$$
F[p]=x^Dp-WE_c^{-1}G_c(W,x^Dp).
$$



The finite decomposition remains


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
\tag{1.3}
$$


The established finite unit results give integral $M_L,M_H$. The physical LOW inverse still costs $3^{-1}$.

The prefix and tail boundaries remain


$$
R_*=\frac{9Q+1}{2},\qquad a_0=R_*-1,
$$




$$
\tau=\frac{N_0-3}{2},\qquad \ell=3R+1,
$$




$$
K=\{0,\ldots,3R\},\qquad J=\{\ell,\ldots,\tau-1\},
\qquad R_*+\tau=\nu,
$$


and


$$
a=\overline B_{\ell,\tau-1}.
$$



### 1.3 The complete source

Retain


$$
\begin{aligned}
\Omega_P(y)={}&
(1-y)^{2P}\bigl(y^{122P}+3y^{41P}\bigr)\\
&+9(1+y^P+y^{2P})
\bigl(2y^{14P}+2y^{41P}+2y^{95P}-y^{131P}\bigr),
\end{aligned}
$$


and


$$
p_0=\Omega_P(y)(1-y)^t.
$$


Its literal expansion is


$$
p_0=\sum_{(\Delta,b,c)\in\mathcal T}
c(1-y)^{t+\Delta}y^{bP},
\tag{1.4}
$$


with all fourteen terms:


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
\tag{1.5}
$$



The actual core sources are


$$
\upsilon_T=\frac{G_c(Y,x^Dy^{\nu-1})}{3},
\qquad
f_H=\frac{\upsilon_0}{3}
=\frac{G_c(Y,x^Dp_0)}9.
\tag{1.6}
$$



### 1.4 Results reused, not reproved

I reuse the following at their proved finite scope.

1. The Turn 15 contracted LOW-source cancellation and endpoint reduction:
   

$$
a\eta_0=\frac{w_H^Tf_H}{3^{25}}\pmod3,
   \qquad
   w_H=\frac{M_H\upsilon_T-e_d}{3}.
$$



2. The Turn 16 complete column-defect result:
   

$$
\delta_H=\frac{\upsilon_T-\mathcal S_He_d}{3}
   \equiv\delta_{\rm raw}+3^{25}R_d\pmod{3^{26}},
$$


   where
   

$$
\delta_{\rm raw}=
   \frac{\upsilon_T-G_c(Y,x^DP_d)}3.
$$



3. The actual first lift
   

$$
Z_0=x^Dy^{T+\nu-1}-y^{d+1},
   \qquad
   w_H\equiv z_0\pmod3,
$$


   together with its already evaluated complete contraction
   

$$
z_0^Tf_H\in3^{29}\mathbb Z_3.
$$



4. The actual next force:
   

$$
w_1=\frac{w_H-z_0}{3},\qquad
   \mathcal S_Hw_1=r_1,
$$


   

$$
r_1\equiv
   \frac{\delta_{\rm raw}-G_c(Y,x^DP_*)}{3}
   +3^{24}R_d
   \pmod{3^{25}},
   \tag{1.7}
$$


   with
   

$$
P_*=y^{T+\nu-1}-P_{d+1}.
$$



5. The literal finite HIGH inverse modulo $3$:
   

$$
(\overline M_He_t)_s
   =[Z^{m+d-s-t}](1-Z)^D,
   \qquad d\le s,t\le m.
   \tag{1.8}
$$



The favorable parent reviews and separate pending audits attached to the inherited results remain distinct from the new proofs below. No inherited leading statement is promoted to a full endpoint value.

---

## 2. A small new beta-unit calculation

Use the established exact beta ratio


$$
\mathcal B(N,q)=
\frac{4^N N!(N+q)!(2q)!}
{q!(2N+2q+1)!},
\tag{2.1}
$$


and its valuation formula


$$
v_3\mathcal B(N,q)
=
-\sum_{e\ge1}
\mathbf1_{\{N\bmod3^e\ge j_e(q)\}},
\qquad
j_e(q)=
\left(\frac{3^e-1}{2}-q\right)\bmod3^e.
\tag{2.2}
$$



The existing factorial-unit producer is reused. No $729$-position calculation is repeated.

### Lemma 2.1 — Scaling a complete beta value

Let $L_0=3^E$, $E\ge1$, and let $b,u$ be positive integers with $u$ odd. Then


$$
L_0\mathcal B\!\left(bL_0,\frac{uL_0-1}{2}\right)
=
\mathcal B\!\left(b,\frac{u-1}{2}\right)\mathcal F,
\qquad
\mathcal F\in1+9\mathbb Z_3.
\tag{2.3}
$$


In particular, when the beta value on the right is a unit, the two beta expressions agree modulo $9$.

#### Proof

The product form of (2.1) is


$$
\mathcal B(N,q)
=
\frac{2^N N!}{\prod_{j=0}^{N}(2q+1+2j)}.
$$


Hence


$$
L_0\mathcal B\!\left(bL_0,\frac{uL_0-1}{2}\right)
=
\frac1u\prod_{j=1}^{bL_0}\frac{2j}{uL_0+2j}.
$$


The factors with $L_0\mid j$, together with $1/u$, give exactly


$$
\mathcal B\!\left(b,\frac{u-1}{2}\right).
$$


All remaining factors are


$$
\left(1+\frac{uL_0}{2j}\right)^{-1}\in1+3\mathbb Z_3.
$$



Modulo $9$, only $v_3(j)=E-1$ can matter. Write


$$
j=3^{E-1}v,\qquad 1\le v\le3b,\qquad 3\nmid v.
$$


Their product is


$$
1-\frac{3u}{2}
\sum_{\substack{1\le v\le3b\\3\nmid v}}v^{-1}
\pmod9.
$$


There are $b$ occurrences of each nonzero residue modulo $3$, so the sum is zero modulo $3$. Thus the product belongs to $1+9\mathbb Z_3$. ∎

### The specific units needed now

The inherited resonant unit satisfies


$$
\mathcal U=3H\mathcal B(H,r_H)\equiv2\pmod9.
$$


Lemma 2.1 gives


$$
\boxed{
T\mathcal B(H,r_T)\equiv
\mathcal B(3,0)=\frac{16}{35}\equiv2\pmod9,
\qquad r_T=\frac{T-1}{2}.
}
\tag{2.4}
$$



For the three new valuation classes,


$$
\boxed{
\begin{array}{c|ccc}
u&1&5&7\\ \hline
V\mathcal B\!\left(H,\frac{uV-1}{2}\right)\bmod3
&2&1&2 .
\end{array}}
\tag{2.5}
$$



Here is a bounded derivation of the three entries. First,


$$
\mathcal B(9,0)
=\frac{4^9}{19\binom{18}{9}}
\equiv2\pmod3,
$$


since $\binom{18}{9}\equiv2\pmod3$. Also,


$$
\frac{\mathcal B(N,q+1)}{\mathcal B(N,q)}
=\frac{2q+1}{2N+2q+3},
$$


so


$$
\mathcal B(9,2)=\frac{\mathcal B(9,0)}{7\cdot23},
\qquad
\mathcal B(9,3)=\frac{\mathcal B(9,2)}5.
$$


Their residues are $1$ and $2$. Applying Lemma 2.1 with $L_0=V$ proves (2.5).

These are evaluations of complete beta ratios, not replacements by individual poles.

---

## 3. Evaluation of the actual residual $r_1\bmod3$

Define


$$
b_i=\binom{D+i-1}{i},
\qquad
s_0=r_T-\nu,\qquad s_*=s_0+1,
$$


and, for $u=1,5,7$,


$$
s_u=\frac{uV+1}{2}-\nu.
\tag{3.1}
$$


All these rows lie in the literal HIGH interval by (1.2).

Introduce the finite binomial band


$$
\mathsf B_T=\sum_{i=0}^{\nu}b_i e_{s_0+i}.
\tag{3.2}
$$


Its entire support is also inside $[d,m]$.

### 3.1 Which complete beta values can survive modulo $9$?

For $0\le q<r_H$,


$$
v_3\mathcal B(H,q)=-v_3(2q+1).
\tag{3.3}
$$


For $r_H<q<H$, the actual $3H$ indicator contributes one additional unit of negative valuation:


$$
v_3\mathcal B(H,q)=-v_3(2q+1)-1.
\tag{3.4}
$$


At $q=r_H$, the valuation is $-h$.

These statements follow directly from the already established indicator formula. In particular, (3.4) is retained when evaluating the shifted source $y^{T+\nu-1}$.

The original arithmetic gives


$$
\beta\equiv1\pmod9,\qquad D\equiv H\equiv0\pmod{3^5}.
\tag{3.5}
$$



### Proposition 3.1 — The raw defect through the carry digit

The complete raw defect satisfies


$$
\boxed{
\begin{aligned}
\delta_{\rm raw}\equiv{}&
-2e_{s_*}-6e_{s_0}
+3e_{s_1}-3e_{s_5}+3e_{s_7}\\
&+6\mathsf B_T+2e_{m-1}+6e_m
\pmod9.
\end{aligned}}
\tag{3.6}
$$



#### Derivation

Use the established complete raw-column law, rather than constructing another column formula.

The first terminal-source channel is


$$
-\frac H3\,\beta\,\mathcal B(H,s+\nu-1).
$$


Its unit class has $2(s+\nu-1)+1=T$, giving $s=s_*$. Its full value modulo $9$ is $-2$ by (2.4).

Its depth-one classes have


$$
2(s+\nu-1)+1=uV,\qquad u=1,5,7.
$$


After extracting the factor $3$, (2.5) gives coefficients $1,-1,1$.

The other terminal-source channel is


$$
-H\mathcal B(H,s+\nu).
$$


Away from the physical terminal, its sole visible class modulo $9$ has


$$
s+\nu=r_T,
$$


giving $-6e_{s_0}$.

For the $P_d$-$\beta$ channel, the visible ordinary argument is $q=r_T$. Writing $j=\nu-i$, its coefficient occurs at


$$
s=r_T-j=s_0+i
$$


and equals $6b_i$ modulo $9$. This gives $6\mathsf B_T$.

The $P_d$-$3y$ physical resonance gives $2e_{m-1}$.

At $s=m$, the individually nonintegral resonant terms must first be combined. The already paid complete terminal formula is


$$
(\delta_{\rm raw})_m
=
\frac{4D-H-72}{3}\mathcal U
\pmod{3^{26}}.
$$


Therefore


$$
(\delta_{\rm raw})_m\equiv(-24)\cdot2\equiv6\pmod9.
$$


This is the $6e_m$ in (3.6). No terminal division is performed on an isolated nonintegral summand.

All remaining ordinary valuation classes have depth at least $2$ in the relevant channel. The factorial terms are much deeper than the present precision. ∎

### Proposition 3.2 — The complete first-lift source through the same carry digit

With


$$
P_*=y^{T+\nu-1}-P_{d+1},
$$


one has


$$
\boxed{
G_c(Y,x^DP_*)
\equiv
-2e_{s_*}-6e_{s_0}
+2e_{m-1}+6e_{m-2}
\pmod9.
}
\tag{3.7}
$$



#### Derivation

For $y^{T+\nu-1}$, the complete $\beta$-resonance occurs at


$$
s+T+\nu-1=r_H,
$$


namely at $s=s_*$, and gives $-\beta\mathcal U\equiv-2$. The complete $3y$-resonance is at $s=s_0$, giving $-3\mathcal U\equiv-6$.

The largest argument in this shifted source is


$$
T+r_H=\frac{5T-1}{2}.
$$


The potential upper ordinary class with odd denominator $5T$ occurs only in the $3y$ channel at $s=m$. Its valuation, including the extra $3H$ indicator in (3.4), is $2$. It therefore contributes zero modulo $9$, but only after that valuation is included.

For $P_{d+1}$, its leading coefficient is $1$, and its next coefficients are


$$
b_1=D,\qquad b_2=\frac{D(D+1)}2.
$$


Both $b_1,b_2$ are divisible by $3^5$. Thus its visible resonances modulo $9$ are


$$
G_c(Y,x^DP_{d+1})
\equiv-2e_{m-1}-6e_{m-2}\pmod9.
$$


Subtracting gives (3.7). ∎

### Theorem 3.3 — The next actual residual digit

The actual residual in (1.7) satisfies


$$
\boxed{
r_1\equiv
e_{s_1}-e_{s_5}+e_{s_7}
-\mathsf B_T-e_m+e_{m-2}
\pmod3.
}
\tag{3.8}
$$



#### Proof

Subtract (3.7) from (3.6), then divide the resulting known multiple of $3$ by $3$. The term $3^{24}R_d$ in (1.7) is zero modulo $3$. Since $2=-1$ in $\mathbb F_3$, the result is (3.8). ∎

The equality of the complete values in (2.4) is important: it pays the carry at $s_*$. Knowing only the leading residues of the two sources would not have justified (3.8).

---

## 4. Applying the literal finite HIGH inverse

For a HIGH vector $v$, write


$$
V_v(y)=\sum_{t=d}^{m}v_ty^t,
$$


and let $\operatorname{pr}_{[d,m]}$ retain exactly the coefficients with exponents in the original HIGH interval.

The reused finite kernel (1.8) is equivalently


$$
\boxed{
V_{\overline M_Hv}(y)
=
\operatorname{pr}_{[d,m]}
\left(x^Dy^{m+\nu}V_v(y^{-1})\right).
}
\tag{4.1}
$$


This is a finite identity with both boundary masks. It is not an infinite triangular inverse followed by an assumed projection.

### 4.1 The three interior point sources

For $u=1,5,7$,


$$
m+\nu-s_u
=\frac{9-u}{2}V+\nu-1.
$$


Consequently,


$$
\begin{aligned}
\overline M_He_{s_1}&\leftrightarrow x^Dy^{4V+\nu-1},\\
\overline M_He_{s_5}&\leftrightarrow x^Dy^{2V+\nu-1},\\
\overline M_He_{s_7}&\leftrightarrow x^Dy^{V+\nu-1}.
\end{aligned}
\tag{4.2}
$$



Each polynomial lies wholly in $[d,m]$. Indeed,


$$
V+\nu-1\ge d,
$$


and


$$
4V+d-1\le m
$$


are consequences of $V>4D+10$.

### 4.2 The finite binomial band

Applying (4.1) to (3.2) gives


$$
\begin{aligned}
V_{\overline M_H\mathsf B_T}(y)
&=
\operatorname{pr}_{[d,m]}
\left(
x^Dy^{T+\nu}\sum_{i=0}^{\nu}b_i y^{-i}
\right)\\
&=
x^Dy^TP_d(y).
\end{aligned}
\tag{4.3}
$$


No tail is omitted: the polynomial has support contained in


$$
[T,T+d]\subseteq[d,m].
$$



### 4.3 The actual upper-edge masks

For $e_m$, the projection in (4.1) leaves only the top coefficient:


$$
\overline M_He_m=e_d.
\tag{4.4}
$$



For $e_{m-2}$, the projection retains exactly


$$
y^{d+2}-D y^{d+1}+\binom D2y^d.
$$


Because $3\mid D$ and $3\mid\binom D2$,


$$
\boxed{\overline M_He_{m-2}=e_{d+2}.}
\tag{4.5}
$$



This calculation uses the original lower boundary $d$ and the actual upper input row $m-2$. In particular, the entire polynomial $x^Dy^{\nu+2}$ is not substituted for this edge inverse image.

### Theorem 4.1 — The new actual finite direction

Let $\widehat Z_1$ be the polynomial in (A). Then


$$
\boxed{\widehat z_1\equiv M_Hr_1=w_1\pmod3.}
\tag{4.6}
$$


Therefore


$$
\boxed{
\mathcal S_H(e_d+3z_0+9\widehat z_1)-\upsilon_T
\in3^3\mathbb Z_3^{\{d,\ldots,m\}}.
}
\tag{4.7}
$$



#### Proof

Apply (4.2)–(4.5) to every term of (3.8). This gives exactly (A) modulo $3$.

Since $\mathcal S_Hw_1=r_1$, equation (4.6) implies


$$
\mathcal S_H\widehat z_1-r_1\in3\mathbb Z_3^{\{d,\ldots,m\}}.
$$


Multiplication by $9$ gives (4.7). ∎

### 4.4 A compact coefficient law, without a long vector

The finite division


$$
y^d=C_d+x^DP_d,\qquad
C_d=\sum_{u=0}^{D-1}\binom du x^u
$$


gives the alternative exact representation


$$
\boxed{
\begin{aligned}
\widehat Z_1={}&
x^D\left(y^{4V+\nu-1}-y^{2V+\nu-1}+y^{V+\nu-1}\right)\\
&-y^{T+d}+y^TC_d+y^{d+2}-y^d.
\end{aligned}}
\tag{4.8}
$$



For $0\le v<D$,


$$
\boxed{
[y^v]C_d
=
(-1)^{D-1-v}
\binom dv\binom{d-v-1}{D-1-v},
}
\tag{4.9}
$$


and the coefficient is zero outside this finite range.

To verify (4.9), expand $x^u=(y-1)^u$:


$$
[y^v]C_d
=
\binom dv\sum_{j=0}^{D-1-v}(-1)^j\binom{d-v}{j},
$$


then use the finite alternating-binomial identity.

Thus one coefficient of $\widehat Z_1$ requires at most five binomial coefficients and a fixed number of range tests and monomial indicators. At any fixed precision at most $26$, the already paid factorial-unit producer evaluates these in $O(h)$ operations on bounded-precision residues.

This is a compact explicit polynomial direction. No array of length $m-d+1$, $D$, or $\nu+1$ is constructed.

---

## 5. Evaluation of the whole contraction of $\widehat Z_1$

The new direction is now contracted as an integral polynomial, not merely as a vector modulo $3$.

By its verified HIGH support,


$$
\widehat z_1^Tf_H
=
\frac{G_c(\widehat Z_1,x^Dp_0)}9.
\tag{5.1}
$$



### Theorem 5.1 — Complete second-lift contraction

Uniformly on the original sufficiently large Range III family,


$$
\boxed{\widehat z_1^Tf_H\in3^{29}\mathbb Z_3.}
\tag{5.2}
$$



#### Proof

Every term of the fourteen-term table (1.5) is retained. Write the channel index as $\epsilon=0,1$, with channel multiplier


$$
\beta^{1-\epsilon}3^\epsilon.
$$


The rational functional divided by $9$ has scale


$$
3^{h-2}=3^{S+30}.
\tag{5.3}
$$



We treat the three types of polynomial in (A).

### 5.1 The three shifted $x^D$-monomials

For


$$
x^Dy^{cV+\nu-1},\qquad c=1,2,4,
$$


the beta arguments against a source term $(\Delta,b,c_{\rm src})$ are


$$
N=H+D+t+\Delta
=H+268P+\Pi+\Delta,
$$




$$
q=cV+(134+b)P+\chi-2+\epsilon.
\tag{5.4}
$$


Here


$$
v_3(N)=S-1.
$$


Thus, for the first $S-1$ indicators, the count is determined by $v_3(2q+1)$. It is $1$ for $\epsilon=0$, because


$$
v_3(2\chi-3)=1,
$$


and $0$ for $\epsilon=1$, because


$$
v_3(2\chi-1)=0.
$$



There are only seven possible indicators at levels $S,\ldots,S+6$.

To verify that all higher indicators vanish, write


$$
N=H+N_{\rm lo},\qquad q=cV+q_{\rm lo}.
$$


The original bounds and the literal table imply


$$
N_{\rm lo}+q_{\rm lo}<540P.
\tag{5.5}
$$


For $S+7\le e\le S+29$, the $cV$ part disappears modulo $3^e$, and (5.5) is below the corresponding half-modulus.

At modulus $3V$, the possible high residues of $q$ are $V,2V,V$. Their distance, in the indicator test, from a possible crossing is at least $V/2$, which is larger than $540P$.

At modulus $H=9V$,


$$
q\le4V+q_{\rm lo}<H/2-N_{\rm lo}.
$$


At modulus $3H$,


$$
N+q\le13V+540P<\frac{3H-1}{2}.
$$


All still higher indicators are also absent.

Therefore the total beta-indicator count is at most $8$ in the $\beta$ channel and at most $7$ in the $3y$ channel. After (5.3), every such term has valuation at least


$$
S+22\ge53.
\tag{5.6}
$$



### 5.2 The complete finite quotient term

Consider


$$
x^Dy^TP_d
=
\sum_{i=0}^{\nu}b_i x^Dy^{T+\nu-i}.
$$


Set $j=\nu-i$. The beta arguments are


$$
N=H+268P+\Pi+\Delta,
\qquad
q=T+j+bP+\epsilon.
\tag{5.7}
$$


Again $v_3(N)=S-1$, and all indicators above $S+6$ vanish by the same finite residual bound as in (5.5). The shift is now $T=3V$, which gives an even larger gap at the relevant upper moduli.

There are two cases.

**Case 1: $3\mid i$, including $i=0$.** Since $\nu\equiv-1\pmod3$,


$$
j+\epsilon\equiv-1+\epsilon\pmod3.
$$


Neither channel has $3\mid 2(j+\epsilon)+1$. Hence none of the first $S-1$ indicators occurs. The total count is at most $7$, giving valuation at least


$$
S+23.
$$



**Case 2: $3\nmid i$.** The exact identity


$$
b_i=\frac Di\binom{D+i-1}{i-1}
$$


gives


$$
v_3(b_i)\ge5.
\tag{5.8}
$$


Even allowing all $S-1$ initial indicators and all seven subsequent indicators, the count is at most $S+6$. Including (5.8), the $\beta$-term has valuation at least


$$
S+30+5-(S+6)=29.
$$


The $3y$-term is at least one digit deeper.

Thus the **entire finite quotient term** has contraction in $3^{29}$. No coefficients of $P_d$ are enumerated, and no tail is suppressed.

### 5.3 The two first-edge monomials

For $y^{d+a}$, $a=0,2$, the beta arguments are


$$
N=H+t+\Delta,
$$




$$
q=(402+b)P+3\chi-1+a+\epsilon.
\tag{5.9}
$$


Now $v_3(N)=5$.

For the first five indicators, the relevant fixed residues of $2q+1$ are


$$
\begin{array}{c|cc}
&\epsilon=0&\epsilon=1\\ \hline
a=0&-1&1\\
a=2&3&5.
\end{array}
$$


Thus at most one of these five indicators occurs.

The sixth indicator is also absent, and here the actual original residue of $\chi$ is useful. Since $\chi/243\equiv1\pmod3$,


$$
N\bmod729=-2\chi\bmod729=243.
$$


The four possibilities for $q\bmod729$ are


$$
-1,\ 0,\ 1,\ 2.
$$


Their corresponding $j_6(q)$ are


$$
365,\ 364,\ 363,\ 362,
$$


all larger than $243$. Hence the level-six indicator is zero.

Only the $S$ levels $7,\ldots,S+6$ remain possible. Indicators above $S+6$ vanish because the unshifted residual satisfies


$$
N-H+q<540P.
$$


Therefore the total count is at most $S+1$, giving valuation at least


$$
S+30-(S+1)=29.
\tag{5.10}
$$


The $3y$ multiplier only improves this bound.

### 5.4 Physical cutoff and factorial payment

For every term just considered, the rational-polynomial degree is below


$$
H+\frac{4H}{9}+540P
<
\frac{3H-1}{2}
<
K_{\rm phys}.
\tag{5.11}
$$


Thus the beta evaluation has not extended the physical functional. In this contraction, the $3H$ resonance is excluded by the proved degree bound—not by a convention.

The factorial contribution in (5.1) is an integral polynomial functional multiplied by


$$
3^{h-2}/4,
$$


so it lies in $3^{S+30}\mathbb Z_3$, far beyond the target.

Every coefficient in (1.5) is integral. Applying the preceding estimates separately to all fourteen terms and both channels proves (5.2). ∎

This evaluates the whole chosen-lift contribution, not just its first digit.

---

## 6. The remaining actual vector and its complete next force

Define


$$
\boxed{w_2=\frac{w_1-\widehat z_1}{3}.}
\tag{6.1}
$$


The division is paid by Theorem 4.1.

The exact decomposition is now


$$
\boxed{w_H=z_0+3\widehat z_1+9w_2.}
\tag{6.2}
$$


Thus every displayed lifted contribution is accounted for before reducing the scalar.

Using the inherited $z_0^Tf_H\in3^{29}$ and Theorem 5.1,


$$
w_H^Tf_H\equiv9w_2^Tf_H\pmod{3^{26}},
$$


and


$$
w_1^Tf_H\equiv3w_2^Tf_H\pmod{3^{25}}.
\tag{6.3}
$$


The inherited endpoint divisibility consequently gives


$$
\boxed{
w_2^Tf_H\in3^{23}\mathbb Z_3,\qquad
a\eta_0=\frac{w_2^Tf_H}{3^{23}}\pmod3.
}
\tag{6.4}
$$



No whole scalar zero follows from the cancellation of the two chosen lifts.

### 6.1 Exact finite polynomial adaptation of $\widehat Z_1$

For $a\ge D$, let


$$
y^a=C_a+x^DP_a,
$$


where


$$
C_a=\sum_{u=0}^{D-1}\binom au x^u,
\qquad
P_a=\sum_{i=0}^{a-D}b_i y^{a-D-i}.
$$


These are exact finite Euclidean divisions; they do not enlarge the middle space.

Put


$$
\boxed{
\begin{aligned}
P^{[1]}={}&
y^{4V+\nu-1}-y^{2V+\nu-1}+y^{V+\nu-1}
-y^TP_d\\
&+P_{d+2}-P_d .
\end{aligned}}
\tag{6.5}
$$


Then


$$
\widehat Z_1=x^DP^{[1]}+C_{d+2}-C_d.
\tag{6.6}
$$



Define the actual LOW force


$$
\alpha_{[1]}=\frac{G_c(U,x^DP^{[1]})}{3}.
$$


The exact Schur adaptation is


$$
\boxed{
\mathcal S_H\widehat z_1
=
G_c(Y,x^DP^{[1]})
-3\mathcal X^TM_L\alpha_{[1]}.
}
\tag{6.7}
$$



### Proposition 6.1 — The new LOW force is paid at depth $25$

In the original LOW coordinates,


$$
\boxed{\alpha_{[1]}\in3^{25}\mathbb Z_3^D.}
\tag{6.8}
$$



#### Proof

Use the monomial LOW basis temporarily; the change to the original $x$-basis is integral and unimodular.

Every monomial in the four types of terms in (6.5) gives beta top $H$. Its LOW argument has one of the forms


$$
q=cV+u+\nu-1+\epsilon,\quad c=1,2,4,
$$




$$
q=T+u+j+\epsilon,\quad 0\le j\le\nu,
$$


or


$$
q=u+j+\epsilon,\quad 0\le j\le\nu+2,
$$


with $0\le u<D$.

All these arguments are below $r_H$, by (1.2). The residual odd denominator, after removing the displayed $V$- or $T$-shift, is positive and less than $807P$. Since the shifts are divisible by $3^{S+29}$,


$$
v_3(2q+1)\le S+6.
$$


For beta top $H$, formula (3.3) therefore gives


$$
v_3\!\left(H\mathcal B(H,q)\right)\ge S+31-(S+6)=25.
$$


The $3y$ channel is deeper, the finite quotient coefficients are integral, and the factorial term after division by $3$ is in $3^{h-1}$. ∎

### 6.2 The next residual with all LOW feedback

Set


$$
r_2=\frac{r_1-\mathcal S_H\widehat z_1}{3},
\qquad
\mathcal S_Hw_2=r_2.
\tag{6.9}
$$



Retain the earlier LOW forces


$$
\alpha_d=\frac{G_c(U,x^DP_d)}3,\qquad
\alpha_*=\frac{G_c(U,x^DP_*)}3.
$$


The inherited results are


$$
M_L\alpha_d\equiv3^{25}c_d\pmod{3^{26}},
\qquad
\alpha_*\in3^{25}\mathbb Z_3^D.
$$



Exact substitution, before any reduction, gives


$$
\boxed{
\begin{aligned}
r_2={}&
\frac{
\delta_{\rm raw}
-G_c(Y,x^DP_*)
-3G_c(Y,x^DP^{[1]})
}{9}\\
&+\frac19\mathcal X^TM_L\alpha_d
+\frac13\mathcal X^TM_L\alpha_*
+\mathcal X^TM_L\alpha_{[1]}.
\end{aligned}}
\tag{6.10}
$$


All three displayed LOW divisions are paid by their depth-$25$ forces.

At the required new precision this becomes


$$
\boxed{
r_2\equiv
\frac{
\delta_{\rm raw}
-G_c(Y,x^DP_*)
-3G_c(Y,x^DP^{[1]})
}{9}
+3^{23}R_d
\pmod{3^{24}}.
}
\tag{6.11}
$$



The numerator in (6.11) is divisible by $9$. This follows either from (6.9) and the integral returns in (6.10), or directly from the proved next-digit solve.

The depth accounting is:


$$
\begin{array}{c|c|c}
\text{term}&\text{depth before its displayed division}&
\text{depth in }r_2\\ \hline
\mathcal X^TM_L\alpha_d&25&23\\
\mathcal X^TM_L\alpha_*&25&24\\
\mathcal X^TM_L\alpha_{[1]}&25&25.
\end{array}
$$


Thus the last two terms disappear modulo $3^{24}$, while the first leaves the actual $3^{23}R_d$. The matrix return inside $\mathcal S_H$ remains unchanged.

### 6.3 The new force is still value-produced with finite masks

The polynomial source in (6.11) is not left as an unspecified matrix product.

Put


$$
B_{\rm win}=243P,\qquad r_{\rm win}=\frac{B_{\rm win}-1}{2}.
$$


For $a=0,1,2$, and for the shifts $c$ occurring above, define


$$
j_\epsilon(s,c)=
(r_{\rm win}-s-c-\epsilon)\bmod B_{\rm win}.
$$


Because


$$
\nu+2<B_{\rm win},
$$


there is at most one selected monomial per channel in $y^cP_{d+a}$. Explicitly,


$$
\boxed{
\begin{aligned}
G_c(Y_s,x^Dy^cP_{d+a})
\equiv{}&
-3H\sum_{\substack{\epsilon=0,1\\
0\le j_\epsilon(s,c)\le\nu+a}}
3^\epsilon\beta^{1-\epsilon}
b_{\nu+a-j_\epsilon(s,c)}\\
&\hspace{18mm}\times
\mathcal B\!\left(H,s+c+j_\epsilon(s,c)+\epsilon\right)
\pmod{3^{26}}.
\end{aligned}}
\tag{6.12}
$$



To justify the mask, all relevant arguments satisfy $0\le q<H$. If
$B_{\rm win}\nmid2q+1$, then


$$
v_3(2q+1)\le S+4.
$$


Even including the additional $3H$ indicator when $q\ge r_H$, the weighted beta contribution in (6.12) has valuation at least


$$
S+32-(S+5)=27.
$$


It is therefore absent modulo $3^{26}$. The selected beta value retains the full $3H$ indicator, including $q=r_H$.

The highest rational degree in $G_c(Y,x^DP^{[1]})$ is


$$
H+r_H+4V=\frac{35H}{18}-\frac12<K_{\rm phys},
\tag{6.13}
$$


by $V>4D+10$. Thus the physical cutoff is also paid for the new force, including its upper shifted term.

Combining the existing raw-column law with (6.12), one entry of (6.11) requires at most twenty beta-ratio evaluations and ten binomial evaluations. These amount to at most $130(h+1)$ calls to the fixed block formula underlying the already paid unit producer, plus $O(h)$ digit comparisons.

This is an entry producer for the complete new force, **not** a compact inverse of that force.

For the quotient in (6.11), the numerator must be retained modulo $3^{26}$. No division by $9$ is performed on a residue known only modulo $3^{24}$.

---

## 7. What remains mathematically open

### 7.1 The primary certificate is still missing

The chosen $\widehat z_1$ satisfies only


$$
\mathcal S_H\widehat z_1-r_1\in3\mathbb Z_3^{\{d,\ldots,m\}}.
$$


It does not satisfy


$$
\mathcal S_H\widehat z_1-r_1\in3^{25}\mathbb Z_3^{\{d,\ldots,m\}}.
$$



The exact remaining local obligation is therefore to construct a compact actual $z_2$ with


$$
\boxed{
\mathcal S_H(e_d+3z_0+9\widehat z_1+27z_2)-\upsilon_T
\in3^{27}\mathbb Z_3^{\{d,\ldots,m\}},
}
\tag{7.1}
$$


and to evaluate


$$
\boxed{z_2^Tf_H\pmod{3^{24}}.}
\tag{7.2}
$$


Because $M_H$ is integral, (7.1) implies


$$
z_2-w_2\in3^{24}\mathbb Z_3^{\{d,\ldots,m\}},
$$


so (7.2) is exactly the remaining contraction in (6.4).

### 7.2 A concrete next directional lemma

A smaller immediate follow-on is now well specified:

> Reduce the numerator in (6.11) modulo $27$, retaining the full $\beta\bmod27=10$, the next $H/27$-valuation classes, the translated finite quotient bands in $P^{[1]}$, and the literal terminal corrections. Apply the same finite kernel with both masks to obtain the next chosen digit, and contract that whole integral polynomial with $f_H$ modulo $3^{24}$.

The new source is explicitly given by (6.5), (6.11), and (6.12). The difficulty is no longer an unspecified force. It is proving manageable closure of the successive finite inverse directions, including their carries and LOW feedback, through all the remaining precision.

No such closure theorem is proved here.

### 7.3 Why the literature does not fill this gap

No rational-diagonal automaticity theorem is applied. The supplied Rowland–Yassawi scope requires a $p$-integral rational representation with unit constant denominator. Such a representation for the normalized source/operator and its finite inverse has not been established.

Likewise, finite representation product identities do not imply finite inverse closure. The warnings recorded from Bacher remain applicable.

The rank-at-most-two terminal unfolding at its specified split remains a seed fact only. It is not used as an inverse-rank assertion.

The present advance instead uses an explicit finite kernel calculation for one actual residual direction, followed by a complete symbolic contraction.

---

## 8. Later physical layers and complete forcing remain unchanged

No endpoint has closed. Therefore no first-four mixed-prefix value or actual physical-seven value is inferred.

The physical-six assembly remains


$$
C_6=
C^{\rm mom}
-\bigl(e_{k-1}\eta^T+\eta e_{k-1}^T\bigr)
-R_4
\pmod3.
$$


The mixed-prefix division and upper corner remain


$$
P_{ui}=\frac{d_u^T\mathsf A^{-1}d_H{}_i}{3}\pmod3,
$$




$$
(C_H)_{ui}
=
-c_{P-1-u-i-\Pi}
+c_{P-1-u-i-2\Pi}
-2\,\mathbf1_{u=R,\ i=k-1}
-P_{ui}.
$$


The later direction remains


$$
B_6x=w_6,\qquad x\in3^{-1}\mathbb Z_3^{k-1}.
$$



The diagonal payments are still


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



The actual producer remains


$$
\boxed{Q_{\rm act}=Q_c+3^7\mathscr R.}
$$


A full physical-seven value still requires the complete source at precision $34$, together with the actual/core transport and the physical-five complementary and kernel-pivot returns.

For completeness, the retained physical correction is


$$
F_{\rm fac}=(n-1)!,
$$




$$
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},\qquad 0\le a,b<n,
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


Thus


$$
[x^a](3^7\mathscr R)
=
-\frac{F_{\rm fac}}{a!}
\bigl((t_{\rm force})_a+\xi v_a\bigr),
\qquad 0\le a\le n-1,
$$


and


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
$$


The moment recurrence retains its entire factorial term:


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
$$



The local factorial payments in this report do not delete these terms from the complete construction.

---

## 9. Actual contents, least clearer, final gcd, and whole error

The new local direction does not determine the actual integer column contents. They remain those of the complete original construction.

The least simultaneous clearer remains the actual $\ell_{\rm clr}$, not a convenient common multiple and not a power of $3$. Retain


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


The whole error remains


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
G\det H_{\rm complete}.
}
\tag{9.1}
$$



An irrationality argument still requires, at the **same infinite original indices**,


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
\tag{9.2}
$$


These conditions would make the nonzero whole errors tend to zero. None follows from the vanishing of either chosen-lift contraction.

Thus neither the actual primitive denominator nor the nonzero whole evaluated error is replaced by a local $3$-adic surrogate.

---

## 10. Bounded arithmetic and proof-status ledger

No tool use or numerical computation was performed.

No new large solve, state enumeration, original-index vector, $729$-product receipt, LOW48 calculation, or optional $\mathcal U$ calculation is needed for the new theorem.

The only new fixed arithmetic seeds used in the proof were:


$$
\begin{array}{c|c|c}
(N,q)&\text{modulus}&\text{proved residue of }\mathcal B(N,q)\\ \hline
(3,0)&9&2\\
(9,0)&3&2\\
(9,2)&3&1\\
(9,3)&3&2.
\end{array}
$$


Their exact rational derivations were given in Section 2. If independently checked, these bounded inputs should return exactly the four displayed residues. Such a check would establish only those four arithmetic values; the uniform transfer is the proof of Lemma 2.1.

No endpoint calculation is proposed before the remaining inverse compression is proved.

| Item | Status |
|---|---|
| Turn 15 contracted LOW-source cancellation | Reused at its stated scope; audit status unchanged |
| Turn 16 complete column law and first-lift contraction | Reused, not recalculated |
| Actual $r_1\bmod3$, including carry and edge terms | Newly evaluated in (3.8) |
| Literal finite inverse action on this residual | Newly evaluated |
| Compact chosen lift $\widehat Z_1$ | Newly proved, with both edge masks |
| Whole $\widehat z_1^Tf_H$ | Newly proved to lie in $3^{29}$ |
| Accuracy of the new cumulative lift | $3^3$, not $3^{27}$ |
| New LOW force and feedback precision | Newly paid in (6.8)–(6.11) |
| Complete new force entry law | Explicit, finite-masked, value-produced |
| $w_1^Tf_H\bmod3^{25}$ | Still open |
| Equivalent remaining $w_2^Tf_H\bmod3^{24}$ | Still open |
| $\eta_0,\eta_{k-1}$ | Open |
| First-four mixed prefix and actual physical seven | Open |
| Actual contents, least clearer, all-prime gcd, actual $q$ | Not evaluated |
| Same-index nonzero whole error and decay | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

---

## Conclusion

The new proved result is the explicit second actual finite HIGH direction


$$
\boxed{
\widehat Z_1
=
x^D\left(
y^{4H/9+\nu-1}-y^{2H/9+\nu-1}+y^{H/9+\nu-1}
-y^{H/3}P_d
\right)
+y^{d+2}-y^d,
}
$$


together with


$$
\boxed{
w_1\equiv\widehat z_1\pmod3,
\qquad
\widehat z_1^Tf_H\in3^{29}\mathbb Z_3.
}
$$



The two chosen lifts have both been contracted in full. Their cancellation leaves—not eliminates—the actual remaining contribution:


$$
\boxed{
w_H^Tf_H\equiv9w_2^Tf_H\pmod{3^{26}},
\qquad
a\eta_0=\frac{w_2^Tf_H}{3^{23}}\pmod3.
}
$$



The exact next force is (6.11), with the surviving $3^{23}R_d$, complete polynomial divisions, full $\beta/3y$ channels, physical resonance rules, and the true finite Schur inverse retained.

The remaining bottleneck is a compact precision-$24$ inverse contraction for this force, or an equivalent proved method that evaluates the same scalar without original-length enumeration. No finite-state or low-rank closure is inferred from the successful directions.



$$
\boxed{\text{The HIGH endpoint and the global question for }e+\pi\text{ remain open.}}
$$


