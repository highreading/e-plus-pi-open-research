> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3 Turn 18: Independent audit of the second finite HIGH lift

## Executive verdict

**All of the new scoped mathematical claims in A1 Turn 17 pass the audit below, at the finite matrix and source premises retained in the accepted A3 Turn 16 report.** No original-sized solve, new table construction, or numerical computation is needed for this conclusion.

The principal audited results are


$$
w_1\equiv \widehat z_1\pmod3,
$$


where the specified integral polynomial is


$$
\widehat Z_1
=
x^D\left(
y^{4V+\nu-1}-y^{2V+\nu-1}+y^{V+\nu-1}
-y^TP_d
\right)+y^{d+2}-y^d,
\qquad V=\frac H9,\quad T=\frac H3,
$$


and


$$
\widehat z_1^Tf_H\in3^{29}\mathbb Z_3.
$$


The latter is a statement about the **whole contraction of this particular integral lift**, with all fourteen source terms and both physical channels. It is not a statement about every lift of its reduction modulo $3$.

The next actual vector and force are therefore


$$
w_2=\frac{w_1-\widehat z_1}{3},\qquad \mathcal S_Hw_2=r_2,
$$


with


$$
\begin{aligned}
r_2={}&
\frac{\delta_{\rm raw}-G_c(Y,x^DP_*)-3G_c(Y,x^DP^{[1]})}{9}\\
&+\frac19\mathcal X^TM_L\alpha_d
+\frac13\mathcal X^TM_L\alpha_*
+\mathcal X^TM_L\alpha_{[1]}.
\end{aligned}
$$


In particular,


$$
r_2\equiv
\frac{\delta_{\rm raw}-G_c(Y,x^DP_*)-3G_c(Y,x^DP^{[1]})}{9}
+3^{23}R_d
\pmod{3^{24}}.
$$


The numerator here must be known modulo $3^{26}$, **before** division by $9$. The actual matrix remains


$$
\mathcal S_H=E_Y-3\mathcal X^TM_L\mathcal X.
$$



I also prove a new boundary consequence for the actual next force:


$$
\boxed{
(r_2)_d\equiv0,\qquad
(r_2)_{m-3}\equiv\mathcal U,\qquad
(r_2)_{m-2}\equiv
\frac{4D-H-72}{3}\mathcal U
\pmod{3^{24}},
}
$$


where the already established complete resonant unit is


$$
\mathcal U=3H\mathcal B(H,r_H).
$$


Thus


$$
v_3((r_2)_{m-3})=0,\qquad v_3((r_2)_{m-2})=1.
$$



This makes the accuracy of the chosen cumulative lift **sharp**:


$$
\boxed{
v_3\!\left(
\bigl[\mathcal S_H(e_d+3z_0+9\widehat z_1)-\upsilon_T\bigr]_{m-3}
\right)=3.
}
$$


Consequently, its residual belongs to $3^3\mathbb Z_3^{[d,m]}$, but not to $3^4\mathbb Z_3^{[d,m]}$. It is certainly not a precision-$27$, meaning $3^{27}$, certificate.

The scalar


$$
\boxed{w_2^Tf_H\pmod{3^{24}}}
$$


is still not evaluated. Neither endpoint, the first-$4$ return, the physical-$7$/source-$34$ problem, the separate higher ternary audit, nor the all-prime primitive-error problem is closed.

No proof of rationality or irrationality of $e+\pi$ follows.

---

## 1. Scope, original objects, and exact baseline reuse

Throughout, $v_3(0)=+\infty$. Matrix and vector congruences are entrywise.

### 1.1 The original index family is retained

All uniform statements concern sufficiently large tuples in precisely the supplied original family:


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



The retained relations are


$$
P=3^{h-32},\qquad P_0=243P,\qquad N_0=243r,\qquad D=P_0+N_0,
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


Hence


$$
N_0=25P+2\chi,\qquad D=268P+2\chi.
$$


The actual Range III restriction is


$$
\boxed{\frac3{25}<\frac{\chi}{P}<\frac{31}{250}.}
$$


Also,


$$
v_3(\chi)=5,\qquad \chi/243\equiv1\pmod9.
$$



Set


$$
S=h-32,\quad P=3^S,\quad H=3^{S+31},\quad S\ge31,
$$




$$
\Pi=P/3,\qquad t=\Pi-2\chi,\qquad k=3\chi-\Pi-1,
$$


and


$$
\nu=D/2-1,\qquad d=D+\nu=\frac{3D}{2}-1.
$$


In particular,


$$
D<269P,\quad \nu<135P,\quad d<403P,\quad v_3(D)=5.
$$


The new scales satisfy


$$
V=3^{S+29},\qquad T=3V,
$$


and therefore


$$
\boxed{V>3000P>4D+10.}
$$


This is a direct consequence of the original parameters, not an independently imposed choice.

No argument chooses $P$ and $\chi$ independently. The inherited infinitude assertion is used only at this original-index scope.

### 1.2 Literal finite spaces and physical boundaries

The bases remain


$$
U_u=x^u,\quad 0\le u<D,\qquad x=y-1,
$$




$$
z_i^{\rm mid}=x^Dy^i,\quad 0\le i<\nu,
$$




$$
Y_s=y^s,\quad d\le s\le m.
$$


We retain


$$
m+\nu=r_H,\qquad r_H=\frac{H-1}{2}.
$$



The physical HIGH terminal is $Y_m$. The last middle polynomial is $y^{\nu-1}$. These are different objects.

The prefix boundaries remain


$$
R_*=\frac{9Q+1}{2},\quad a_0=R_*-1,\quad
\tau=\frac{N_0-3}{2},\quad \ell=3R+1,
$$




$$
K=\{0,\ldots,3R\},\qquad J=\{\ell,\ldots,\tau-1\},\qquad
R_*+\tau=\nu,
$$


and


$$
a=\overline B_{\ell,\tau-1}.
$$



### 1.3 Complete functional and corrected columns

The functional is


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{v=0}^{K_{\rm phys}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^a)=(2a)!,
$$


where


$$
K_{\rm phys}=2n-2=2H-2D+2.
$$



The core producer is


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=D-H-71,
$$


with


$$
G_c(f,g)=\mathcal M(Q_cfg),\qquad W=[U\ Y],\qquad E_c=G_c(W,W).
$$


The complete corrected column remains


$$
F[p]=x^Dp-WE_c^{-1}G_c(W,x^Dp).
$$



The literal block decomposition is


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


The accepted baseline proves $M_L$ and $M_H$ integral. The physical LOW inverse still costs $3^{-1}$.

### 1.4 All fourteen source terms

The complete source is


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


Thus


$$
p_0=\sum_{(\Delta,b,c)\in\mathcal T}
c(1-y)^{t+\Delta}y^{bP},
$$


with the complete table


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



The sources under audit are


$$
\upsilon_T=\frac{G_c(Y,x^Dy^{\nu-1})}{3},
\qquad
f_H=\frac{G_c(Y,x^Dp_0)}9.
$$


Their established integral normalizations are reused.

### 1.5 Baseline results used without repeating closed calculations

The following accepted results are inputs to this audit.

1. The exact beta ratio and valuation law:
   

$$
\mathcal B(N,q)
   =
   \frac{4^NN!(N+q)!(2q)!}{q!(2N+2q+1)!},
$$


   

$$
v_3\mathcal B(N,q)
   =
   -\sum_{e\ge1}
   \mathbf1_{\{N\bmod3^e\ge j_e(q)\}},
   \qquad
   j_e(q)=\left(\frac{3^e-1}{2}-q\right)\bmod3^e.
$$



2. The complete resonant unit
   

$$
\mathcal U=3H\mathcal B(H,r_H),
$$


   with
   

$$
\mathcal U\equiv2\pmod{27},\qquad
   \mathcal U\equiv56\pmod{243},
$$


   and its established fixed finite representation modulo $3^{26}$:
   

$$
\mathcal U\equiv
   3^{13}\mathcal B\!\left(3^{12},\frac{3^{12}-1}{2}\right)
   \pmod{3^{26}}.
$$


   No numerical instantiation of this fixed value is repeated.

3. The finite quotients
   

$$
b_i=\binom{D+i-1}{i},\qquad
   P_d=\sum_{i=0}^{\nu}b_i y^{\nu-i},
$$


   and
   

$$
y^d=C_d+x^DP_d,\qquad
   C_d=\sum_{u=0}^{D-1}\binom du x^u.
$$



4. The actual adapted LOW force
   

$$
\alpha_d=\frac{G_c(U,x^DP_d)}3,
   \qquad
   M_L\alpha_d\equiv3^{25}c_d\pmod{3^{26}},
$$


   where $c_d$ is the original LOW coordinate vector of $C_d$.

5. The complete leading return
   

$$
R_d=\overline{\mathcal X}^{\,T}\overline c_d.
$$


   Writing $j_s=r_H-s-d$, its value is
   

$$
(R_d)_s=
   \mathbf1_{\{s=m\}}-
   \begin{cases}
   \binom{D+j_s-1}{j_s},&j_s\ge0,\\
   0,&j_s<0,
   \end{cases}
   \pmod3.
$$


   In particular,
   

$$
(R_d)_d=(R_d)_{m-1}=0,\qquad (R_d)_m=1,
$$


   and its support lies at $s\equiv122\pmod{243}$.

6. The exact first adaptation
   

$$
\delta_H=\frac{\upsilon_T-\mathcal S_He_d}{3}
   =\delta_{\rm raw}+\mathcal X^TM_L\alpha_d,
$$


   where
   

$$
\delta_{\rm raw}=
   \frac{\upsilon_T-G_c(Y,x^DP_d)}3.
$$



7. The first chosen lift and its complete contraction:
   

$$
Z_0=x^Dy^{T+\nu-1}-y^{d+1},
   \qquad w_H\equiv z_0\pmod3,
   \qquad z_0^Tf_H\in3^{29}\mathbb Z_3.
$$


   Put
   

$$
P_*=y^{T+\nu-1}-P_{d+1},\qquad
   \alpha_*=\frac{G_c(U,x^DP_*)}{3}\in3^{25}\mathbb Z_3^D.
$$


   For
   

$$
w_1=\frac{w_H-z_0}{3},\qquad \mathcal S_Hw_1=r_1,
$$


   the exact equation is
   

$$
r_1=
   \frac{\delta_{\rm raw}-G_c(Y,x^DP_*)}{3}
   +\frac13\mathcal X^TM_L\alpha_d
   +\mathcal X^TM_L\alpha_*.
$$



8. The literal finite HIGH inverse modulo $3$:
   

$$
(\overline M_He_t)_s
   =[Z^{m+d-s-t}](1-Z)^D,
   \qquad d\le s,t\le m.
$$



9. Conditional on the inherited endpoint identity and its divisibility premise,
   

$$
a\eta_0=\frac{w_H^Tf_H}{3^{25}}\pmod3.
$$



These inputs do not include an endpoint value or a higher-precision inverse certificate. The closed LOW48 calculation, the first-lift contraction, and the old factorial-unit receipts are not rerun.

---

## 2. Audit of the new beta-unit calculation

### 2.1 Scaling lemma — PASS

Let $L_0=3^E$, $E\ge1$, and let $b,u$ be positive integers, with $u$ odd. The product formula gives


$$
L_0\mathcal B\!\left(bL_0,\frac{uL_0-1}{2}\right)
=
\frac1u\prod_{j=1}^{bL_0}\frac{2j}{uL_0+2j}.
$$


The factors with $L_0\mid j$, together with $1/u$, equal


$$
\mathcal B\!\left(b,\frac{u-1}{2}\right).
$$


For the remaining factors,


$$
\frac{2j}{uL_0+2j}
=
\left(1+\frac{uL_0}{2j}\right)^{-1}.
$$



Every such factor is in $1+3\mathbb Z_3$. Modulo $9$, only indices with $v_3(j)=E-1$ can contribute. Writing $j=3^{E-1}v$, their product is


$$
1-\frac{3u}{2}
\sum_{\substack{1\le v\le3b\\3\nmid v}}v^{-1}
\pmod9.
$$


There are $b$ representatives of each nonzero residue modulo $3$, so the sum is zero modulo $3$. Therefore


$$
\boxed{
L_0\mathcal B\!\left(bL_0,\frac{uL_0-1}{2}\right)
=
\mathcal B\!\left(b,\frac{u-1}{2}\right)\mathcal F,
\qquad
\mathcal F\in1+9\mathbb Z_3.
}
$$



The qualification concerning units is important: literal congruence modulo $9$ follows immediately when the small beta value is a unit. That hypothesis holds in each new application.

### 2.2 The four small seeds — PASS

First,


$$
\mathcal B(3,0)=\frac{16}{35}\equiv2\pmod9.
$$


Using $H=3T$, the scaling lemma gives


$$
\boxed{T\mathcal B(H,r_T)\equiv2\pmod9},
\qquad r_T=\frac{T-1}{2}.
$$



Next,


$$
\mathcal B(9,0)=\frac{4^9}{19\binom{18}{9}}\equiv2\pmod3,
$$


since $\binom{18}{9}\equiv2\pmod3$.

The exact ratio


$$
\frac{\mathcal B(N,q+1)}{\mathcal B(N,q)}
=\frac{2q+1}{2N+2q+3}
$$


gives


$$
\mathcal B(9,2)=\frac{\mathcal B(9,0)}{7\cdot23},
\qquad
\mathcal B(9,3)=\frac{\mathcal B(9,2)}5.
$$


Consequently,


$$
\mathcal B(9,2)\equiv1,\qquad
\mathcal B(9,3)\equiv2\pmod3.
$$


Scaling with $L_0=V$ proves


$$
\boxed{
\begin{array}{c|ccc}
u&1&5&7\\ \hline
V\mathcal B\!\left(H,\frac{uV-1}{2}\right)\bmod3
&2&1&2.
\end{array}}
$$



These calculations evaluate complete beta ratios. They do not replace a complete value by a selected pole.

### 2.3 The upper ordinary valuation law — PASS

Put $L=S+31$, so $H=3^L$. For $e\le L$, the beta indicator is present exactly when $3^e\mid2q+1$, because $H\bmod3^e=0$.

For $0\le q<H$, the level $L+1$ indicator is present precisely when


$$
\frac{3H-1}{2}-q\le H,
$$


that is, when $q\ge r_H$. All higher indicators are absent. Hence


$$
\boxed{
v_3\mathcal B(H,q)
=
-v_3(2q+1)-\mathbf1_{\{q\ge r_H\}},
\qquad 0\le q<H.
}
$$


At $q=r_H$, this is $-L-1=-h$.

This independently verifies the extra $3H$ indicator used in A1 Turn 17. It must be retained above the physical resonance.

Finally, the original arithmetic gives


$$
\boxed{\beta\equiv1\pmod9,\qquad \beta\equiv10\pmod{27}.}
$$



---

## 3. Re-derivation of every mod-$9$ defect coefficient

Define


$$
s_0=r_T-\nu,\qquad s_*=s_0+1,\qquad
s_u=\frac{uV+1}{2}-\nu\quad(u=1,5,7),
$$


and the finite band


$$
\mathsf B_T=\sum_{i=0}^{\nu}b_i e_{s_0+i}.
$$



The rows are genuinely HIGH. For example,


$$
s_1-d=\frac{V-4D+5}{2}>0,\qquad m-s_7=V-1>0.
$$


The band starts above $d$, and its last row is $r_T<m$. No row is supplied by a periodic extension.

### 3.1 The raw defect — PASS

Below the physical terminal, the complete rational channels are


$$
-\frac H3\beta\mathcal B(H,s+\nu-1),
\qquad
-H\mathcal B(H,s+\nu),
$$




$$
H\beta\sum_{i=0}^{\nu}b_i\mathcal B(H,s+\nu-i),
\qquad
3H\sum_{i=0}^{\nu}b_i\mathcal B(H,s+\nu-i+1).
$$


The factorial contribution is beyond the present precision.

The contributions visible modulo $9$ are as follows.

| Channel | Visible ordinary or resonant condition | Contribution |
|---|---|---|
| Terminal $\beta$ | $2(s+\nu-1)+1=T$ | $-2e_{s_*}$ |
| Terminal $\beta$ | $2(s+\nu-1)+1=uV,\ u=1,5,7$ | $3e_{s_1}-3e_{s_5}+3e_{s_7}$ |
| Terminal $3y$, ordinary | $s+\nu=r_T$ | $-6e_{s_0}$ |
| $P_d$-$\beta$, ordinary | $s+\nu-i=r_T$ | $6\mathsf B_T$ |
| $P_d$-$3y$, physical | $s+\nu-i+1=r_H,\ s<m$ | $2e_{m-1}$ |

For the first row of the table, the value is


$$
-T\beta\mathcal B(H,r_T)\equiv-2\pmod9.
$$


For the three depth-one classes, the multiplier is $-3$, and the complete normalized units are $2,1,2$. Their coefficients are therefore $3,-3,3$ modulo $9$.

The finite band is complete: $i$ ranges from $0$ through $\nu$, including both ends.

#### The physical terminal must be combined before division

At $s=m$, the resonant pieces are


$$
-H\mathcal B(H,r_H),\qquad
H\beta\mathcal B(H,r_H),\qquad
3HD\mathcal B(H,r_H).
$$


The first two are individually nonintegral. Their combined value is


$$
H(\beta-1+3D)\mathcal B(H,r_H)
=
\frac{4D-H-72}{3}\mathcal U.
$$


Since


$$
v_3(4D-H-72)=2,
$$


the displayed division is paid. Modulo $9$,


$$
\frac{4D-H-72}{3}\mathcal U
\equiv(-24)\cdot2\equiv6.
$$


The argument $r_H+1$ that occurs in the neighboring $P_d$-$3y$ term has the extra indicator, but its weighted valuation is still far beyond the target.

Thus


$$
\boxed{
\begin{aligned}
\delta_{\rm raw}\equiv{}&
-2e_{s_*}-6e_{s_0}
+3e_{s_1}-3e_{s_5}+3e_{s_7}\\
&+6\mathsf B_T+2e_{m-1}+6e_m
\pmod9.
\end{aligned}}
$$


Every coefficient in A1 Turn 17, equation (3.6), is correct.

### 3.2 The first-lift source through the carry digit — PASS

The shifted monomial in


$$
P_*=y^{T+\nu-1}-P_{d+1}
$$


has beta arguments


$$
q=s+T+\nu-1+\epsilon,\qquad \epsilon=0,1.
$$



Its physical resonance is at $s=s_*$ for $\epsilon=0$, and at $s=s_0$ for $\epsilon=1$. Their complete values are


$$
-\beta\mathcal U\equiv-2,\qquad -3\mathcal U\equiv-6\pmod9.
$$



The maximum shifted argument is


$$
r_H+T=\frac{5T-1}{2}.
$$


Above $r_H$, the only possible ordinary class that could approach visibility modulo $9$ has odd denominator $5T$. It occurs only in the $3y$ channel, at $s=m$. Including the extra $3H$ indicator, its weighted valuation is $2$, so it vanishes modulo $9$. Omitting that indicator would be an incorrect valuation calculation, even though this term ultimately vanishes at the present precision.

For $P_{d+1}$, the physical coefficients relevant modulo $9$ are


$$
b_0=1,\qquad b_1=D,\qquad b_2=\frac{D(D+1)}2.
$$


Both $b_1$ and $b_2$ have valuation $5$. Hence


$$
G_c(Y,x^DP_{d+1})
\equiv-2e_{m-1}-6e_{m-2}\pmod9.
$$


It follows that


$$
\boxed{
G_c(Y,x^DP_*)
\equiv
-2e_{s_*}-6e_{s_0}+2e_{m-1}+6e_{m-2}
\pmod9.
}
$$



### 3.3 The actual residual digit — PASS

The exact baseline equation for $r_1$ shows that its LOW terms are invisible modulo $3$. Subtracting the last two boxed formulas and then dividing their known multiple of $3$ gives


$$
\boxed{
r_1\equiv
e_{s_1}-e_{s_5}+e_{s_7}
-\mathsf B_T-e_m+e_{m-2}
\pmod3.
}
$$



The equality of the complete values


$$
T\mathcal B(H,r_T)\equiv\mathcal U\equiv2\pmod9
$$


pays the carry at $s_*$. Leading residues alone would not justify this subtraction and division.

---

## 4. Both finite HIGH projection masks

### 4.1 Polynomial form of the literal inverse — PASS

For a HIGH vector $v$, write


$$
V_v(y)=\sum_{t=d}^{m}v_ty^t.
$$


The baseline kernel implies


$$
\boxed{
V_{\overline M_Hv}(y)
=
\operatorname{pr}_{[d,m]}
\left(x^Dy^{m+\nu}V_v(y^{-1})\right).
}
$$


Indeed, the coefficient of $y^s$ in the unprojected expression is


$$
\sum_{t=d}^{m}v_t
[y^{s-m-\nu+t}](y-1)^D
=
\sum_{t=d}^{m}v_t
[Z^{m+d-s-t}](1-Z)^D.
$$



This identity contains both output boundaries $d$ and $m$, as well as the original finite input interval. It is not an infinite inverse with an unproved truncation rule.

### 4.2 Interior sources and the complete band — PASS

For $u=1,5,7$,


$$
m+\nu-s_u=\frac{9-u}{2}V+\nu-1.
$$


Thus


$$
\overline M_He_{s_1}\leftrightarrow x^Dy^{4V+\nu-1},
$$




$$
\overline M_He_{s_5}\leftrightarrow x^Dy^{2V+\nu-1},
$$




$$
\overline M_He_{s_7}\leftrightarrow x^Dy^{V+\nu-1}.
$$



Their minimum exponent is at least $d$, and their maximum exponent is at most $m$, because


$$
V+\nu-1\ge d,\qquad 4V+d-1\le m.
$$


The second inequality is equivalent to


$$
\frac V2-2D+\frac52\ge0,
$$


and follows from the retained separation.

For the band,


$$
\begin{aligned}
V_{\overline M_H\mathsf B_T}
&=
\operatorname{pr}_{[d,m]}
\left(x^Dy^{T+\nu}\sum_{i=0}^{\nu}b_i y^{-i}\right)\\
&=x^Dy^TP_d.
\end{aligned}
$$


Its support lies in


$$
[T,T+d]\subseteq[d,m].
$$


The complete finite quotient is retained; no infinite tail has been introduced or dropped.

### 4.3 The physical upper inputs and lower output mask — PASS

For input $e_m$, the unprojected polynomial is $x^Dy^\nu$. Its only coefficient at exponent at least $d$ is its top coefficient, so


$$
\overline M_He_m=e_d.
$$



For input $e_{m-2}$, the unprojected polynomial is $x^Dy^{\nu+2}$. The literal lower boundary retains exactly


$$
y^{d+2}-Dy^{d+1}+\binom D2y^d.
$$


Because $3\mid D$ and $3\mid\binom D2$,


$$
\boxed{\overline M_He_{m-2}=e_{d+2}.}
$$



Substituting the whole polynomial $x^Dy^{\nu+2}$ for this inverse image would be wrong. The two lower-degree terms removed by the finite projection matter to subsequent exact adaptations.

### 4.4 The chosen second direction — PASS

Applying these finite images to the complete residual digit proves


$$
\boxed{
w_1\equiv\widehat z_1\pmod3,
}
$$


where


$$
\boxed{
\widehat Z_1
=
x^D\left(
y^{4V+\nu-1}-y^{2V+\nu-1}+y^{V+\nu-1}
-y^TP_d
\right)+y^{d+2}-y^d.
}
$$


This polynomial is supported wholly on the original HIGH interval.

Since $\mathcal S_Hw_1=r_1$, it follows that


$$
\mathcal S_H(e_d+3z_0+9\widehat z_1)-\upsilon_T
\in3^3\mathbb Z_3^{[d,m]}.
$$


At this point, the leading solve proves only this inclusion. Strict failure at higher precision requires a further argument; Section 8 below supplies it.

### 4.5 Compact coefficient law — PASS

The exact division for $y^d$ yields


$$
\begin{aligned}
\widehat Z_1={}&
x^D\left(y^{4V+\nu-1}-y^{2V+\nu-1}+y^{V+\nu-1}\right)\\
&-y^{T+d}+y^TC_d+y^{d+2}-y^d.
\end{aligned}
$$


For $0\le v<D$,


$$
\begin{aligned}
[y^v]C_d
&=\binom dv
\sum_{j=0}^{D-1-v}(-1)^j\binom{d-v}{j}\\
&=(-1)^{D-1-v}
\binom dv\binom{d-v-1}{D-1-v}.
\end{aligned}
$$


Outside that range the coefficient is zero.

Thus one coefficient of $\widehat Z_1$ uses at most three binomial coefficients from the shifted $x^D$ terms and two from $C_d$, together with range tests and monomial indicators. The stated $O(h)$ bounded-precision entry cost follows from the already established factorial-unit producer. This does not construct an original-length vector.

---

## 5. Whole fourteen-source contraction in $3^{29}$

The verified HIGH support permits the exact identity


$$
\widehat z_1^Tf_H
=
\frac{G_c(\widehat Z_1,x^Dp_0)}9.
$$


We now use the integral polynomial $\widehat Z_1$, not merely its reduction modulo $3$.

For a source term $(\Delta,b,c)$ and channel $\epsilon=0,1$, the multiplier is


$$
c\,\beta^{1-\epsilon}3^\epsilon.
$$


The common rational scale after division by $9$ is


$$
3^{h-2}=3^{S+30}.
$$


All signs in the polynomial and source are retained by linearity; the valuation estimates below hold term by term, so no unproved cancellation is used.

### 5.1 Three shifted $x^D$-monomials — PASS

For $x^Dy^{c_0V+\nu-1}$, $c_0=1,2,4$, the beta arguments are


$$
N=H+D+t+\Delta=H+268P+\Pi+\Delta,
$$




$$
q=c_0V+(134+b)P+\chi-2+\epsilon.
$$


Here


$$
v_3(N)=S-1.
$$


For the first $S-1$ indicators, the counts are therefore $1$ and $0$, respectively, because


$$
v_3(2\chi-3)=1,\qquad v_3(2\chi-1)=0.
$$


There are at most seven further indicators at levels $S,\ldots,S+6$.

Write $N=H+N_{\rm lo}$, $q=c_0V+q_{\rm lo}$. The literal source table and original range imply


$$
N_{\rm lo}+q_{\rm lo}<540P.
$$


At levels $S+7,\ldots,S+29$, the high shifts disappear modulo $3^e$, and this residual bound is below the half-modulus threshold.

At modulus $3V$, the high residues of $q$ are $V,2V,V$. In each case the indicator threshold stays at distance at least $V/2-540P$ from a crossing. At modulus $H=9V$,


$$
q<\frac H2-N_{\rm lo}.
$$


At modulus $3H$,


$$
N+q<13V+540P<\frac{3H-1}{2}.
$$


All higher indicators are absent as well.

Thus the total beta counts are at most $8$ and $7$, giving valuations at least


$$
S+22\quad\text{and}\quad S+24.
$$


Both are well beyond $29$.

### 5.2 The complete finite quotient $x^Dy^TP_d$ — PASS

Write


$$
x^Dy^TP_d=\sum_{i=0}^{\nu}b_i x^Dy^{T+\nu-i},
\qquad j=\nu-i.
$$


Then


$$
N=H+268P+\Pi+\Delta,\qquad
q=T+j+bP+\epsilon.
$$


Again $v_3(N)=S-1$, and the residual bound below $540P$ removes every indicator above $S+6$.

If $3\mid i$, including $i=0$, then


$$
j+\epsilon\equiv-1+\epsilon\pmod3.
$$


In neither channel is $2(j+\epsilon)+1$ divisible by $3$. Hence none of the first $S-1$ indicators occurs, and the total count is at most $7$. The valuation is at least $S+23$.

If $3\nmid i$, the exact identity


$$
b_i=\frac Di\binom{D+i-1}{i-1}
$$


gives


$$
v_3(b_i)\ge5.
$$


Even allowing all $S-1$ initial indicators and all seven later ones, the beta count is at most $S+6$. The $\beta$ channel consequently has valuation at least


$$
S+30+5-(S+6)=29.
$$


The $3y$ channel is one digit deeper.

This proves the required bound for every coefficient of the finite quotient, without enumerating it.

### 5.3 The two lower-edge monomials — PASS

For $y^{d+a}$, $a=0,2$,


$$
N=H+t+\Delta,\qquad
q=(402+b)P+3\chi-1+a+\epsilon.
$$


Now $v_3(N)=5$. At the first five levels, the fixed residues of $2q+1$ are


$$
\begin{array}{c|cc}
&\epsilon=0&\epsilon=1\\ \hline
a=0&-1&1\\
a=2&3&5.
\end{array}
$$


Thus at most one of these five indicators occurs.

The level-six indicator is absent. Indeed,


$$
N\bmod729=-2\chi\bmod729=243,
$$


whereas the possible $q\bmod729$ values are


$$
-1,\ 0,\ 1,\ 2.
$$


Their level-six thresholds are respectively


$$
365,\ 364,\ 363,\ 362,
$$


all greater than $243$.

There are $S$ remaining possible levels $7,\ldots,S+6$, and no later indicators because


$$
N-H+q<540P.
$$


The total count is therefore at most $S+1$. After the scale $3^{S+30}$, every $\beta$ contribution has valuation at least $29$; the $3y$ factor only improves this.

### 5.4 Physical cutoff and factorial contribution — PASS

The maximum rational-polynomial degree in this contraction is bounded by


$$
H+4V+540P
<
\frac{3H-1}{2}
<
K_{\rm phys}.
$$


Thus complete beta evaluation does not extend the physical functional. The $3H$ pole is absent here by a proved degree inequality.

The factorial contribution is an integral polynomial functional multiplied by $3^{h-2}/4$, so it lies in $3^{S+30}\mathbb Z_3$.

All fourteen source coefficients are integral. The estimates apply separately to both channels of every source term. Therefore


$$
\boxed{\widehat z_1^Tf_H\in3^{29}\mathbb Z_3.}
$$



This is a complete evaluation to zero modulo $3^{29}$, not an assertion of exact vanishing in $\mathbb Z_3$.

---

## 6. The actual $w_2$, its paid force, and the remaining scalar

### 6.1 The next division and endpoint reduction — PASS

The division


$$
w_2=\frac{w_1-\widehat z_1}{3}
$$


is paid by the finite leading solve. Exactly,


$$
w_H=z_0+3\widehat z_1+9w_2.
$$


Using the two complete contraction bounds,


$$
w_H^Tf_H\equiv9w_2^Tf_H\pmod{3^{26}},
$$


and


$$
w_1^Tf_H\equiv3w_2^Tf_H\pmod{3^{25}}.
$$



Conditional on the inherited endpoint divisibility,


$$
\boxed{
w_2^Tf_H\in3^{23}\mathbb Z_3,\qquad
a\eta_0=\frac{w_2^Tf_H}{3^{23}}\pmod3.
}
$$


Thus the required unresolved scalar is exactly


$$
\boxed{w_2^Tf_H\pmod{3^{24}}.}
$$


The two contracted chosen lifts do not determine it.

### 6.2 Exact finite adaptation of $\widehat Z_1$ — PASS

For $a\ge D$,


$$
y^a=C_a+x^DP_a,
$$


where


$$
C_a=\sum_{u=0}^{D-1}\binom au x^u,\qquad
P_a=\sum_{i=0}^{a-D}b_i y^{a-D-i}.
$$


These are auxiliary Euclidean divisions; they do not enlarge the middle domain.

Define


$$
\begin{aligned}
P^{[1]}={}&
y^{4V+\nu-1}-y^{2V+\nu-1}+y^{V+\nu-1}
-y^TP_d\\
&+P_{d+2}-P_d.
\end{aligned}
$$


Then


$$
\widehat Z_1=x^DP^{[1]}+C_{d+2}-C_d.
$$



Let


$$
\alpha_{[1]}=\frac{G_c(U,x^DP^{[1]})}{3}.
$$


If $c$ is the original LOW coordinate vector of $C_{d+2}-C_d$, then


$$
\mathcal X\widehat z_1=\alpha_{[1]}+\mathcal Lc.
$$


The LOW polynomial part cancels in the exact Schur adaptation, giving


$$
\boxed{
\mathcal S_H\widehat z_1
=
G_c(Y,x^DP^{[1]})
-3\mathcal X^TM_L\alpha_{[1]}.
}
$$


This is an identity for the true returned matrix, not for $E_Y$ alone.

### 6.3 The new LOW force has depth $25$ — PASS

Use monomial LOW coordinates temporarily. The change from $y^u$ to $x^u$ is integral and unimodular, so a coordinatewise depth bound transfers back to the original basis.

Every beta top is $H$. The arguments have the forms


$$
q=c_0V+u+\nu-1+\epsilon,\qquad c_0=1,2,4,
$$




$$
q=T+u+j+\epsilon,\qquad 0\le j\le\nu,
$$


or


$$
q=u+j+\epsilon,\qquad 0\le j\le\nu+2,
$$


with $0\le u<D$.

All these arguments lie below $r_H$. After removing the displayed $V$- or $T$-shift, the residual odd denominator is positive and less than $807P$. Since


$$
807P<3^{S+7}
$$


and the removed shifts have valuation at least $S+29$,


$$
v_3(2q+1)\le S+6.
$$


Consequently,


$$
v_3\bigl(H\mathcal B(H,q)\bigr)
\ge S+31-(S+6)=25.
$$


The $3y$ channel is deeper; all finite quotient coefficients are integral. The factorial contribution after division by $3$ is also deeper.

Therefore


$$
\boxed{\alpha_{[1]}\in3^{25}\mathbb Z_3^D.}
$$



### 6.4 Exact force and precision ledger — PASS

Set


$$
r_2=\frac{r_1-\mathcal S_H\widehat z_1}{3}.
$$


Substitution before reduction gives


$$
\boxed{
\begin{aligned}
r_2={}&
\frac{
\delta_{\rm raw}-G_c(Y,x^DP_*)-3G_c(Y,x^DP^{[1]})
}{9}\\
&+\frac19\mathcal X^TM_L\alpha_d
+\frac13\mathcal X^TM_L\alpha_*
+\mathcal X^TM_L\alpha_{[1]}.
\end{aligned}}
$$


The LOW payments are


$$
\begin{array}{c|c|c}
\text{term}&\text{depth before division}&\text{depth in }r_2\\ \hline
\mathcal X^TM_L\alpha_d&25&23\\
\mathcal X^TM_L\alpha_*&25&24\\
\mathcal X^TM_L\alpha_{[1]}&25&25.
\end{array}
$$


It follows that


$$
\boxed{
r_2\equiv
\frac{
\delta_{\rm raw}-G_c(Y,x^DP_*)-3G_c(Y,x^DP^{[1]})
}{9}
+3^{23}R_d
\pmod{3^{24}}.
}
$$



The numerator is an actual multiple of $9$: $r_2$ is integral by the next-digit solve, and every displayed LOW fraction is integral. This is not division of an arbitrary residue.

For its quotient modulo $3^{24}$, the numerator must be retained modulo


$$
3^{24+2}=3^{26}.
$$


In particular, knowing the numerator only modulo $3^{24}$ would lose two required digits.

At the physical terminal,


$$
(R_d)_m=1,
$$


so the surviving vector return includes an actual $3^{23}$ contribution there. It cannot be deleted from the force.

At contracted one-digit scope, the baseline residue separation still gives


$$
R_d^TM_Hf_H\equiv0\pmod3,
$$


and hence


$$
3^{23}R_d^TM_Hf_H\equiv0\pmod{3^{24}}.
$$


This last fact is only a contracted correction payment. It neither removes $R_d$ from the vector equation nor removes the LOW matrix feedback from $M_H$.

---

## 7. Complete finite entry production for the new force

### 7.1 The quotient mask — PASS

Put


$$
B_{\rm win}=243P=3^{S+5},\qquad
r_{\rm win}=\frac{B_{\rm win}-1}{2}.
$$


For each actual quotient $y^cP_{d+a}$, with $a=0,1,2$, define


$$
j_\epsilon(s,c)=
(r_{\rm win}-s-c-\epsilon)\bmod B_{\rm win}.
$$


Since


$$
\nu+2<B_{\rm win},
$$


there is at most one selected exponent in each channel.

The actual arguments satisfy $0\le q<H$. If $B_{\rm win}\nmid2q+1$, then


$$
v_3(2q+1)\le S+4.
$$


Even above $r_H$, where the extra indicator is present,


$$
v_3\bigl(3H\mathcal B(H,q)\bigr)\ge S+32-(S+5)=27.
$$


Thus every unselected term vanishes modulo $3^{26}$.

The complete entry law is therefore


$$
\boxed{
\begin{aligned}
G_c(Y_s,x^Dy^cP_{d+a})
\equiv{}&
-3H\sum_{\substack{\epsilon=0,1\\
0\le j_\epsilon(s,c)\le\nu+a}}
3^\epsilon\beta^{1-\epsilon}
b_{\nu+a-j_\epsilon(s,c)}\\
&\hspace{12mm}\times
\mathcal B\!\left(H,s+c+j_\epsilon(s,c)+\epsilon\right)
\pmod{3^{26}}.
\end{aligned}}
$$


The selected beta value remains complete, including the $3H$ indicator and the physical resonance $q=r_H$.

The raw terminal of $\delta_{\rm raw}$ is still evaluated by its combined formula; this mask is not a license to divide its nonintegral pieces separately.

### 7.2 Physical degree and entry complexity — PASS

The highest rational degree in the new HIGH force is attained by the $4V$-shift:


$$
H+r_H+4V=\frac{35H}{18}-\frac12.
$$


The distance to the actual cutoff is


$$
K_{\rm phys}-\left(\frac{35H}{18}-\frac12\right)
=
\frac V2-2D+\frac52>0.
$$


Thus the new force remains within the physical functional.

Counting the literal terms gives at most:

- four beta and two binomial evaluations for the raw law;
- four beta and two binomial evaluations for $P_*$;
- twelve beta and six binomial evaluations for $P^{[1]}$.

The total is at most twenty beta and ten binomial evaluations per queried entry. This gives at most


$$
20\cdot5+10\cdot3=130
$$


factorial-unit calls.

The largest relevant factorial argument is at most


$$
2H+2(r_H+4V)+1=3H+8V<3^{h+1},
$$


so each call uses at most $h+1$ stages of the established producer. The stated bound $130(h+1)$, with $O(h)$ additional digit work, is valid.

This is a full entry producer at the required precision. It is not a compact inverse or a completed contraction.

---

## 8. New consequence: the next boundary values and sharp certificate depth

The following is a new proved statement about the actual force, not merely a necessary residue condition.

### Theorem 8.1 — Actual next-force boundary profile

On the retained original family,


$$
\boxed{
(r_2)_d\equiv0,\qquad
(r_2)_{m-3}\equiv\mathcal U,\qquad
(r_2)_{m-2}\equiv
\frac{4D-H-72}{3}\mathcal U
\pmod{3^{24}}.
}
$$



#### Proof

Write


$$
G_* = G_c(Y,x^DP_*),\qquad
G_1 = G_c(Y,x^DP^{[1]}).
$$


We evaluate the relevant numerator entries modulo $3^{26}$, before division by $9$.

**Lower boundary $s=d$.** The baseline gives


$$
(\delta_{\rm raw})_d\equiv(G_*)_d\equiv0\pmod{3^{26}}.
$$


For a shifted monomial of $P^{[1]}$, the odd denominator is


$$
2c_0V+4D-5+2\epsilon.
$$


Its residual valuation is $0$ for $\epsilon=0$ and $1$ for $\epsilon=1$; these terms are far deeper than $3^{26}$.

For the quotient terms, the shift $0$ or $T$ is a multiple of $B_{\rm win}$. Their residual arguments lie between $d$ and $d+\nu+3$, strictly between


$$
\frac{729P-1}{2}
\quad\text{and}\quad
\frac{1215P-1}{2}.
$$


These are consecutive possible arguments in the selected residue class. Hence no quotient monomial is selected. Therefore


$$
(G_1)_d\equiv0\pmod{3^{26}}.
$$


Since $(R_d)_d=0$, the force equation gives $(r_2)_d\equiv0\pmod{3^{24}}$.

**Upper rows $s=m-k_0$, $k_0=2,3$.** For each shifted monomial $y^{c_0V+\nu-1}$, the odd denominators are


$$
(9+2c_0)V-2(k_0+1-\epsilon).
$$


Their valuations are at most $1$. They are above $r_H$, but even with the extra indicator the weighted beta terms are zero modulo $3^{26}$.

For $y^TP_d$, a monomial indexed by $i$ has odd denominator


$$
5T+2(\epsilon-k_0-i).
$$


Selection would require


$$
i\equiv\epsilon-k_0\pmod{B_{\rm win}}.
$$


For $k_0=2,3$, this residue is near the upper end of the window and lies outside $0\le i\le\nu$. Thus the complete shifted quotient also vanishes modulo $3^{26}$.

It remains to evaluate the unshifted physical resonances. In $P_{d+a}$, the resonance $q=r_H$ occurs at


$$
i=a-k_0+\epsilon.
$$


This gives the table


$$
\begin{array}{c|ccc}
s&(\delta_{\rm raw})_s&(G_*)_s&(G_1)_s\\ \hline
m-3&0&0&-3\mathcal U\\
m-2&0&3\mathcal U&-(\beta+3D)\mathcal U
\end{array}
\qquad \pmod{3^{26}}.
$$


For example, at $m-3$, only the $3y$ resonance of the leading term of $P_{d+2}$ survives in $G_1$. At $m-2$, the two $P_{d+2}$ resonant coefficients are $b_0=1$ and $b_1=D$.

These are the exact finite edge polynomials $P_{d+2}-P_d$ coming from the projected $y^{d+2}-y^d$. The unprojected edge inverse image has not been substituted.

For $s=m-k_0$,


$$
j_s=k_0-D<0,
$$


so


$$
(R_d)_{m-2}=(R_d)_{m-3}=0.
$$


The other two LOW returns are already zero modulo $3^{24}$ after their paid divisions. Consequently,


$$
(r_2)_{m-3}\equiv\frac{9\mathcal U}{9}=\mathcal U,
$$


and


$$
(r_2)_{m-2}
\equiv
\frac{3(\beta+3D-1)\mathcal U}{9}
=
\frac{4D-H-72}{3}\mathcal U
\pmod{3^{24}}.
$$


This proves the theorem. ∎

### Corollary 8.2 — The third-digit certificate is sharp

Since $\mathcal U$ is a unit,


$$
v_3((r_2)_{m-3})=0.
$$


Also $v_3(4D-H-72)=2$, so


$$
v_3((r_2)_{m-2})=1.
$$



Exactly,


$$
\mathcal S_H(e_d+3z_0+9\widehat z_1)-\upsilon_T=-27r_2.
$$


Therefore


$$
\boxed{
\bigl[\mathcal S_H(e_d+3z_0+9\widehat z_1)-\upsilon_T\bigr]_{m-3}
\equiv-27\mathcal U\pmod{3^{27}},
}
$$


and its valuation is exactly $3$.

Equivalently,


$$
(\mathcal S_H\widehat z_1-r_1)_{m-3}
\equiv-3\mathcal U\pmod{3^{25}},
$$


whose valuation is exactly $1$.

This supplies an explicit proof of the source’s assertion that $\widehat z_1$ does not solve the $r_1$ problem to precision $3^{25}$. That negative assertion does **not** follow merely from having proved only a leading solve; it follows from the boundary calculation above.

The result is useful but local. A nonzero coordinate of $r_2$ does not establish a nonzero endpoint contraction or a nonzero complete determinant.

---

## 9. Assertion-by-assertion verdict ledger

| New A1 Turn 17 assertion | Independent verdict | Scope or qualification |
|---|---|---|
| $V>3000P>4D+10$ | **PASS** | Derived from the original family and original $\chi$-range |
| Scaling lemma for complete beta values | **PASS** | Multiplicative factor lies in $1+9\mathbb Z_3$; unit hypothesis checked |
| Four small beta seeds | **PASS** | Exact rational derivations above |
| Upper ordinary valuation law | **PASS** | Extra $3H$ indicator retained for $q\ge r_H$ |
| $\beta\bmod9$, and proposed $\beta\bmod27$ input | **PASS** | Values $1$ and $10$, respectively |
| Raw defect modulo $9$ | **PASS** | Every point, band, and edge coefficient re-derived |
| Combined physical terminal | **PASS** | Nonintegral resonant pieces combined before division |
| First-lift source modulo $9$ | **PASS** | Both physical channels and the upper $5T$ class included |
| Actual $r_1\bmod3$ | **PASS** | Carry division justified by modulo-$9$ values |
| Finite inverse polynomial identity | **PASS** | Literal input interval and both output masks |
| Three interior inverse images | **PASS** | Full support checked against $d$ and $m$ |
| Complete finite band image | **PASS** | All $0\le i\le\nu$ retained |
| Images of $e_m,e_{m-2}$ | **PASS** | Lower projection performed before reduction |
| Chosen $\widehat Z_1$ | **PASS** | Actual integral HIGH polynomial |
| Coefficient formula and entry complexity | **PASS** | Entry scope only; no original-length array |
| Whole fourteen-source contraction | **PASS** | In $3^{29}$, both channels, physical cutoff and factorial payment |
| Definition and integrality of $w_2$ | **PASS** | Division by $3$ paid by the actual finite solve |
| Remaining endpoint reduction | **CONDITIONAL PASS** | Uses the inherited endpoint identity and divisibility |
| Exact finite adaptation $P^{[1]}$ | **PASS** | Does not enlarge the middle space |
| $\alpha_{[1]}\in3^{25}$ | **PASS** | Original LOW coordinates; all argument ranges checked |
| Exact $r_2$ law | **PASS** | All three LOW return terms retained before reduction |
| $3^{23}R_d$ in $r_2\bmod3^{24}$ | **PASS** | Survives as a vector term, including at $m$ |
| Numerator precision before division by $9$ | **PASS** | Must be modulo $3^{26}$ |
| Finite quotient entry mask | **PASS** | Complete selected beta values, including upper indicator |
| Force physical cutoff | **PASS** | Degree $35H/18-1/2<K_{\rm phys}$ |
| Twenty-beta/ten-binomial bound | **PASS** | At most $130(h+1)$ fixed-block calls per entry |
| Claimed failure of a full-precision certificate | **PASS with added proof** | Section 8 proves exact residual depth $3$ |
| Precision-$24$ inverse certificate for $w_2$ | **OPEN** | No compact actual solution supplied |
| $w_2^Tf_H\bmod3^{24}$ | **OPEN** | Not evaluated by the directional contractions |
| Proposed next $H/27$-class calculation | **OPEN FOLLOW-ON** | Well-specified input, not a proved closure theorem |
| Later physical and global conclusions | **UNCHANGED / OPEN** | No advance authorized by this audit |

No false scoped theorem was found. The additional sharpness proof closes a logical point that should not have been justified merely by absence of a higher-precision calculation.

---

## 10. Exact remaining mathematical bottleneck

A sufficient next certificate is an integral HIGH vector $z_2$, described without enumerating the original HIGH interval, such that


$$
\boxed{
\mathcal S_H(e_d+3z_0+9\widehat z_1+27z_2)-\upsilon_T
\in3^{27}\mathbb Z_3^{[d,m]},
}
$$


together with an evaluation of


$$
\boxed{z_2^Tf_H\pmod{3^{24}}.}
$$


Because


$$
M_H\upsilon_T=e_d+3z_0+9\widehat z_1+27w_2
$$


and $M_H$ is integral, the certificate is equivalent to


$$
z_2-w_2\in3^{24}\mathbb Z_3^{[d,m]}.
$$


Since $f_H$ is integral, its contraction would then give the actual remaining scalar.

The immediate next directional calculation is also concrete: reduce


$$
\delta_{\rm raw}-G_c(Y,x^DP_*)-3G_c(Y,x^DP^{[1]})
$$


modulo $27$, retain $\beta\equiv10\pmod{27}$, the $H/27$-valuation classes, the translated finite quotient bands, and the physical corner terms, then apply the same literal finite inverse.

The new boundary theorem supplies exact checks for such a calculation:


$$
(r_2)_{m-3}\equiv2\pmod3,\qquad
(r_2)_{m-2}\equiv0\pmod3,\qquad
(r_2)_d\equiv0\pmod3.
$$


These checks are not a substitute for the complete new direction, much less for its higher-precision contraction.

The unresolved obstruction is **finite higher-precision inverse-and-contraction closure**, including carries, both boundaries, and the true LOW feedback. Neither an entry producer, an infinite Toeplitz model, a named large inverse, nor the success of two chosen directions proves that closure.

The literature gate remains reuse-only. No $3$-integral rational representation with unit constant denominator for the actual normalized finite inverse has been established, so the cited automaticity scope cannot supply this certificate. Product representations and seed low-rank statements do not imply finite inverse closure.

The distinct higher ternary block audit remains open and queued; this focused audit does not pass it.

---

## 11. Complete later forcing and global normalization remain unchanged

### 11.1 Physical layers and all paid divisions

No endpoint is evaluated here. In particular, neither $\eta_0$ nor the alternate endpoint $\eta_{k-1}$ is determined.

The retained physical-$6$ assembly is


$$
C_6=C^{\rm mom}
-\bigl(e_{k-1}\eta^T+\eta e_{k-1}^T\bigr)-R_4\pmod3.
$$


The first-$4$ return and upper corner remain


$$
P_{ui}=\frac{d_u^T\mathsf A^{-1}d_H{}_i}{3}\pmod3,
$$




$$
(C_H)_{ui}
=
-c_{P-1-u-i-\Pi}
+c_{P-1-u-i-2\Pi}
-2\mathbf1_{u=R,\ i=k-1}
-P_{ui}.
$$


The later directional solve remains


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



The physical-$5$ complementary and kernel-pivot returns, actual/core transport, and complete source precision $34$ remain required for physical $7$.

### 11.2 Actual producer and full forcing

The actual producer is not replaced by the core:


$$
\boxed{Q_{\rm act}=Q_c+3^7\mathscr R.}
$$


Retain


$$
F_{\rm fac}=(n-1)!,
\qquad
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},\quad 0\le a,b<n,
$$




$$
\gamma_0=1,\quad\gamma_1=0,\quad
\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1},
$$




$$
h_{\rm vec}
=
T_n^{-1}\left(\binom{n+a}{a}\gamma_{n+a}\right)_{a=0}^{n-1},
$$




$$
u_a=\frac{F_{\rm fac}(-2)^a}{a!},\qquad v=T_n^{-1}u,
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


The complete correction is


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



The forcing identity remains


$$
\boxed{
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
}
$$


Both forcing terms are retained.

Likewise, the full moment recurrence is


$$
\mu_{r+1}+\mu_r
=
\frac{3^h}{2r+1}
-\frac{3^h}{4}\bigl((2r+2)!+(2r)!\bigr),
\qquad 0\le r\le2n-2.
$$


The later construction’s designated index


$$
r_*=\frac{3^h-5}{2}
$$


and its separate division obligations are unchanged. The factorial terms were discarded only in the explicitly paid local congruences above, not from the construction.

### 11.3 Actual contents, least clearer, all-prime gcd, and whole error

The temporary LOW basis used in valuation proofs does not redefine the complete integer columns or their actual contents. Those contents remain unevaluated.

The least simultaneous clearer is the actual $\ell_{\rm clr}$, not a convenient common multiple and not a power of $3$. Retain


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


The whole evaluated error remains


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{G}
\det H_{\rm complete}.
}
$$



An irrationality proof still needs, at the **same infinite original indices**,


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
$$


These would force the nonzero whole errors to tend to zero. If $e+\pi=a/b$ were rational, each nonzero integer linear error would have absolute value at least $1/b$, giving the contradiction.

None of these global conditions follows from the new local unit coordinate of $r_2$, or from the two chosen-lift contractions.

---

## 12. Bounded arithmetic and final proof status

No tools or numerical computation were used. No new indispensable arithmetic calculation is left unpaid by the proofs above.

The only new fixed arithmetic seeds in the second-lift argument are


$$
\begin{array}{c|c|c}
(N,q)&\text{modulus}&\text{verifiable output}\\ \hline
(3,0)&9&\mathcal B(3,0)\equiv2\\
(9,0)&3&\mathcal B(9,0)\equiv2\\
(9,2)&3&\mathcal B(9,2)\equiv1\\
(9,3)&3&\mathcal B(9,3)\equiv2.
\end{array}
$$


Their exact derivations were supplied in Section 2. An independent arithmetic receipt, if desired, would have only these four bounded inputs and outputs. It would verify only these four constants; the uniform transfer is the scaling proof.

No new LOW48 solve, $729$-position table, old source/jet array, resonant-unit numerical instantiation, original-index vector solve, or original factorial matrix computation is proposed.

A finite check at one or finitely many original indices would establish only those finite cases. It would not establish inverse closure or the required infinite-index primitive-error criterion.

---

## Conclusion

The second finite HIGH lift in A1 Turn 17 passes independent audit. Its complete content is


$$
\boxed{
w_1\equiv\widehat z_1\pmod3,\qquad
\widehat z_1^Tf_H\in3^{29}\mathbb Z_3,
}
$$


with both finite projection masks, all fourteen source terms, both physical channels, and every relevant division retained.

The new result of this report is the actual boundary profile


$$
\boxed{
(r_2)_d\equiv0,\quad
(r_2)_{m-3}\equiv\mathcal U,\quad
(r_2)_{m-2}\equiv\frac{4D-H-72}{3}\mathcal U
\pmod{3^{24}},
}
$$


which proves that the chosen cumulative certificate has **exactly** residual depth $3$, not merely a proved lower bound of $3$.

The exact remaining local bottleneck is still


$$
\boxed{w_2^Tf_H\pmod{3^{24}},}
$$


for the true finite returned matrix and the complete force containing $3^{23}R_d$. No compact precision-$24$ inverse-and-contraction certificate has been established.

The later physical, all-prime normalization, actual primitive-denominator, and same-index nonzero whole-error problems remain open.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi\text{ is obtained.}}
$$


