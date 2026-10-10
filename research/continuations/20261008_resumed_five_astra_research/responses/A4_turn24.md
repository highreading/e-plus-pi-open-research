> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 Turn 24 — Independent audit of the core LOW-return payment and the complete paired terminal expansion

## Executive conclusions

The two constructions in the sources have different original index domains. They are kept separate throughout this report.

The principal audit conclusions are as follows.

| Claim under review | Verdict |
|---|---|
| A3 Turn 19, Section 4.7: extension from the finite quotient estimates to the actual lower polynomials $C_{d+a}$ | **PASS** |
| A3 Turn 19, Section 10: $f_L\in3^{24}$, including its normalization by $9$ | **PASS** |
| Terminal LOW two-digit grades and the orientation of the LOW and HIGH inverse operations | **PASS** |
| Closure of the exceptional module under the **actual** inverse needed in Section 10 | **PASS** |
| $\mathscr N^T\mathcal X^TM_Lf_L\subseteq3^{29}\mathbb Z_3$ | **PASS** |
| Complete block payment $g_T^TE_c^{-1}b_0\in3^{30}\mathbb Z_3$ | **PASS** |
| Core conclusion $\eta_0=0$ at sufficiently large original core indices | **PASS at exactly that scope** |
| A2 Turn 14: complete weighted $u$-source normalization, including the new $r=d$ column | **PASS** |
| Exact unimodular paired pencil and both coefficient identities | **PASS** |
| Mixed $\theta$-jet formula and finite row-shift relation | **PASS** |
| Unique minimal factorial-adjugate source sets | **PASS** |
| Payments for every factorial forcing correction and for a bottom atom | **PASS** |
| Complete leading parity cancellation for every $3\le p\le\lfloor d/3\rfloor$ | **PASS**, for both parities of $p$ |
| A terminal upper bound inferred from those cancellations or from lower-rank unit cofactors | **OPEN; no such implication is valid** |

There is also a new proved consequence of the paired audit:



$$
\boxed{
\text{For every }3\le p\le\lfloor d/3\rfloor,\quad
\mathcal D_p\in2^{\mathcal L_p(d)+2}\mathbb Z_2,
}
\tag{E.1}
$$



where $\mathcal D_p$ is the **complete** $p$-product sector of


$$
\det[w_*,v^{(0)},\ldots,v^{(d)}].
$$


Thus the next nominal binary digit is zero as well. This conclusion includes all product-column choices, both Cauchy–Binet source sets, factorial forcing corrections, and the possibility that the atom is a bottom correction.

For $p\ge5$, a further exact excess-class reduction is proved below: modulo $2^{\mathcal L_p+3}$, only the minimal forcing/source pair remains, and its contribution is an explicitly normalized finite determinant with corank at least two modulo $2$. This is a paid reduction of the next possible digit, not an evaluation of that digit as nonzero.

No assertion here transports the core ternary result to physical $7$, supplies source precision $34$, settles the other endpoint or the separate higher ternary block, establishes the required joint terminal upper bound, or evaluates the final all-prime gcd.



$$
\boxed{\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$



---

# Part I. A different audit of the source-specific core LOW-return lemma

## 1. Original core domain, finite boundaries, and reusable results

### 1.1 The original indices are retained

The ternary construction remains on sufficiently large tuples satisfying



$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$




$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



The retained dependent parameters are



$$
P=3^{h-32},\quad P_0=243P,\quad N_0=243r,\quad D=P_0+N_0,
$$




$$
r\equiv2\pmod9,\qquad r\ \text{odd},
$$




$$
4^j=243(3^{26}-1)P-243r+1,
$$




$$
Q=27P,\qquad Q-N_0=2R,\qquad \chi=P-R,
$$


so that


$$
N_0=25P+2\chi,\qquad D=268P+2\chi.
$$



The original subwindow is



$$
\boxed{\frac3{25}<\frac{\chi}{P}<\frac{31}{250}.}
\tag{1.1}
$$



Write



$$
S=h-32,\quad P=3^S,\quad H=3^{S+31},\quad S\ge31,
$$




$$
\Pi=P/3,\qquad t=\Pi-2\chi.
$$



The retained arithmetic gives



$$
v_3(\chi)=5,\qquad \chi/243\equiv1\pmod9,\qquad v_3(D)=5.
$$



The literal finite boundaries are



$$
\nu=D/2-1=134P+\chi-1,
$$




$$
d=D+\nu=402P+3\chi-1,
$$




$$
m=\frac{H-D+1}{2},\qquad r_H=\frac{H-1}{2}=m+\nu.
$$



Consequently,



$$
D\equiv0,\qquad \nu\equiv d\equiv26,\qquad r_H\equiv13\pmod{27}.
\tag{1.2}
$$



No independent choices of $P,\chi,t$ are made.

### 1.2 The actual finite form and complete columns

Put $x=y-1$. The spaces are



$$
U_u=x^u\quad(0\le u<D),\qquad
Y_s=y^s\quad(d\le s\le m),\qquad W=[U\ Y].
$$



The complete functional is



$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{v=0}^{K_{\rm phys}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
$$




$$
\mathfrak f(y^a)=(2a)!,\qquad
K_{\rm phys}=2n-2=2H-2D+2.
$$



The core producer is



$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=D-H-71,
$$


and


$$
G_c(f,g)=\mathcal M(Q_cfg).
$$



The complete corrected column is



$$
\boxed{
F[p]=x^Dp-WE_c^{-1}G_c(W,x^Dp),
\qquad E_c=G_c(W,W).
}
\tag{1.3}
$$



The actual finite block decomposition is



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
\tag{1.4}
$$



The established finite unit results for $M_L,M_H$ are reused. In particular, the physical LOW inverse is still



$$
(3\mathcal L)^{-1}=\frac13M_L.
\tag{1.5}
$$



The last middle polynomial $y^{\nu-1}$ is not identified with the physical HIGH terminal $Y_m$.

### 1.3 The complete fourteen-term source

The source is



$$
p_0=\Omega_P(y)(1-y)^t,
$$




$$
\begin{aligned}
\Omega_P(y)={}&
(1-y)^{2P}(y^{122P}+3y^{41P})\\
&+9(1+y^P+y^{2P})
(2y^{14P}+2y^{41P}+2y^{95P}-y^{131P}).
\end{aligned}
$$



Equivalently,



$$
p_0=\sum_{(\Delta,b,c)\in\mathcal T}
c(1-y)^{t+\Delta}y^{bP},
$$



where the complete set $\mathcal T$ is



$$
\{(2P,122,1),(2P,41,3)\},
$$




$$
\{(0,b,18):b=14,15,16,41,42,43,95,96,97\},
$$




$$
\{(0,b,-9):b=131,132,133\}.
\tag{1.6}
$$



Both channels $\beta$ and $3y$ are retained in every estimate below.

Define



$$
\alpha_T=\frac{G_c(U,x^Dy^{\nu-1})}{3},
\qquad
\upsilon_T=\frac{G_c(Y,x^Dy^{\nu-1})}{3},
$$




$$
f_L=\frac{G_c(U,x^Dp_0)}9,
\qquad
f_H=\frac{G_c(Y,x^Dp_0)}9.
\tag{1.7}
$$



### 1.4 Precisely scoped reuse of the passed annihilator

The previously passed finite annihilator is reused, not recomputed.

For clarity, its modules are recalled. Put



$$
B_\circ=H/3^{24}=2187P,\qquad
C_\circ=(3^{24}-1)/2,
$$




$$
P_{d+a}=\sum_{i=0}^{\nu+a}b_i y^{\nu+a-i},
\qquad
b_i=\binom{D+i-1}{i}.
$$



The bulk module $\mathscr B$ is generated by



$$
\mathsf T_{a,v}
=
3^{(a-1)_+}\operatorname{pr}_{[d,m]}
(x^Dy^{vB_\circ+\nu-1+a}),
\quad 0\le a\le27,
$$




$$
\mathsf Q_{a,v}
=
3^a\operatorname{pr}_{[d,m]}
(x^Dy^{vB_\circ}P_{d+a}),
\quad 0\le a\le26,
$$




$$
\mathsf O_{a,v}
=
3^a\operatorname{pr}_{[d,m]}
(x^Dy^{vB_\circ+a}),
\quad 0\le a\le26,
$$


with $0\le v\le C_\circ$.

Let $\mathscr V_b$ denote HIGH support in residue class $b\bmod27$, and set



$$
\mathscr E=
\mathscr V_{25}+\mathscr V_{26}+\mathscr V_0
+3\mathscr V_1+9\mathscr V,
$$




$$
\mathscr N=\mathscr B+3^{25}\mathscr E+3^{27}\mathscr V.
\tag{1.8}
$$



The passed finite result supplies



$$
\mathscr B^Tf_H\subseteq3^{29}\mathbb Z_3,
\qquad
\mathscr E^Tf_H\subseteq9\mathbb Z_3,
$$


and, for


$$
w=M_H\upsilon_T,
$$




$$
\boxed{w\in\mathscr N,\qquad w^Tf_H\in3^{27}\mathbb Z_3.}
\tag{1.9}
$$



It also supplies the complete residual certificate, including its actual LOW return, and



$$
w=e_d+3z_0+9\widehat z_1+27w_2,
\qquad
w_2^Tf_H\equiv0\pmod{3^{24}}.
\tag{1.10}
$$



These are finite core statements. They are not assertions about an infinite convolution inverse.

---

## 2. Audit of the new quotient/lower-source extension

The first issue is whether the quotient argument really remains valid at the lower edge $v=0$, before projection.

Define the exact remainder



$$
C_{d+a}=y^{d+a}-x^DP_{d+a},
\qquad \deg C_{d+a}<D.
\tag{2.1}
$$



We must prove, for $0\le a\le26$,



$$
\frac{G_c(3^a x^DP_{d+a},x^Dp_0)}9\in3^{29}\mathbb Z_3,
\tag{2.2}
$$


and consequently the same assertion with $x^DP_{d+a}$ replaced by $C_{d+a}$.

### 2.1 The actual beta top and coefficient arguments

For a source term $(\Delta,b,c)$ and channel $\epsilon\in\{0,1\}$, the quotient contraction has beta top



$$
N=H+D+t+\Delta
=H+268P+\Pi+\Delta.
$$



Thus



$$
v_3(N)=S-1.
\tag{2.3}
$$



For the coefficient $b_i$, $0\le i\le\nu+a$, the argument is



$$
q=\nu+a-i+bP+\epsilon\ge0.
\tag{2.4}
$$



This includes both ends of the actual finite quotient. No negative argument or infinite quotient tail is introduced.

Write $u=a+\epsilon$ and



$$
\lambda=v_3(2u-1).
$$



In the present range $0\le u\le27$,



$$
\lambda\le3.
$$



Moreover,



$$
2q+1=(268+2b)P+2\chi+2u-2i-1.
\tag{2.5}
$$



The occurrence of $2\chi$ in this formula is important. It is harmless here because $v_3(\chi)=5>\lambda$; it is not silently set to zero.

### 2.2 The two coefficient cases

The exact beta-valuation formula from the accepted source work is



$$
v_3\mathcal B(N,q)
=
-\sum_{e\ge1}
\mathbf1_{\{N\bmod3^e\ge j_e(q)\}},
$$




$$
j_e(q)=\left(\frac{3^e-1}{2}-q\right)\bmod3^e.
\tag{2.6}
$$



For $e\le S-1$, $N\bmod3^e=0$. Hence those indicators count divisibility of $2q+1$.

* If $v_3(i)\ne\lambda$, including $i=0$, equation (2.5) gives
  

$$
v_3(2q+1)\le\lambda.
$$


* If $v_3(i)=\lambda$, then $i>0$, and
  

$$
b_i=\frac Di\binom{D+i-1}{i-1}
$$


  gives
  

$$
v_3(b_i)\ge5-\lambda.
  \tag{2.7}
$$



There are only seven further possible indicators, at levels $S,\ldots,S+6$. Indeed,



$$
N-H+q
\le
\left(402+\frac13+\frac{\Delta}{P}+b\right)P+\chi+27
<540P,
\tag{2.8}
$$



for every one of the fourteen triples in (1.6), whereas



$$
\frac{B_\circ-1}{2}>1093P.
$$



Thus the indicators at levels $S+7,\ldots,S+31$ are absent. At modulus $3H$ and above, $N+q<3H/2$, so they are absent there as well.

After division by $9$, the functional scale is $3^{S+30}$. In the potentially difficult case $v_3(i)=\lambda$, the complete coefficient payment is at least



$$
S+30+a+\epsilon+(5-\lambda)-(S+6)
=29+u-\lambda.
$$



Since



$$
v_3(2u-1)\le u\qquad(u\ge0),
$$



this is at least $29$. The other case is substantially deeper.

The source coefficient $c$, the factor $3^\epsilon$, and the integral unit $\beta^{1-\epsilon}$ have all been retained.

### 2.3 Lower monomials and remainders

For $3^a y^{d+a}$, the beta top is



$$
N=H+t+\Delta,\qquad v_3(N)=5,
$$


and



$$
q=d+a+bP+\epsilon.
$$



The first five indicators contribute at most



$$
v_3(2a+2\epsilon-1)=\lambda\le3.
$$



The remaining possible levels are $6,\ldots,S+6$, at most $S+1$ levels. Hence the normalized valuation is at least



$$
S+30+a+\epsilon-(S+1+\lambda)
=29+a+\epsilon-\lambda\ge29.
\tag{2.9}
$$



Combining (2.2), (2.9), and the exact identity (2.1) proves



$$
\boxed{
\frac{G_c(3^aC_{d+a},x^Dp_0)}9\in3^{29}\mathbb Z_3,
\qquad 0\le a\le26.
}
\tag{2.10}
$$



### 2.4 Physical cutoff and factorial payment

All rational degrees used above are below



$$
H+540P<\frac{3H}{2}<K_{\rm phys}.
$$



The factorial contribution after division by $9$ belongs to



$$
3^{h-2}\mathbb Z_3=3^{S+30}\mathbb Z_3.
$$



Thus (2.10) is a statement about the complete functional, not just its rational part.

**Verdict: PASS.** The extension at $v=0$ is valid in the original finite quotient. The dependence on $\chi$, both coefficient endpoints, both channels, and the physical cutoff are all paid.

---

## 3. Full normalized LOW-source depth and terminal LOW grades

### 3.1 Proof of $f_L\in3^{24}$

Use monomial LOW coordinates $y^u$, $0\le u<D$, only as an integral unimodular coordinate device.

For one source term and channel,



$$
N=H+t+\Delta,\qquad q=u+bP+\epsilon.
$$



Since $u\le D-1$,



$$
N-H+q
\le
\left(268+\frac13+b+\frac{\Delta}{P}\right)P
\le
\left(401+\frac13\right)P.
\tag{3.1}
$$



All indicators above level $S+6$ are absent. At most $S+6$ indicators remain. The normalization by $9$ therefore gives



$$
v_3\left(\frac{G_c(y^u,x^Dp_0)}9\right)
\ge S+30-(S+6)=24.
$$



The factorial part is deeper, and the degree remains below the physical cutoff.

Therefore



$$
\boxed{f_L\in3^{24}\mathbb Z_3^D.}
\tag{3.2}
$$



This is a bound for the full normalized source, not merely for one leading term.

### 3.2 Terminal LOW depth

For the terminal LOW source, the beta arguments are



$$
q=u+\nu-1,
$$



and the $3y$ arguments are $q+1=u+\nu$. Both remain strictly below $r_H$ on LOW.

The elementary bound



$$
0<2q+1<3D+O(1)<2187P
$$



gives $v_3(2q+1)\le S+6$. The exact beta-top-$H$ valuation below $r_H$ consequently yields



$$
\boxed{\alpha_T\in3^{25}\mathbb Z_3^D.}
\tag{3.3}
$$



This LOW estimate does not encounter the HIGH terminal resonance. In the HIGH terminal source, the $3y$ argument equals $r_H$ at $Y_m$; that physical contribution remains inside the already passed $\upsilon_T$ normalization.

### 3.3 The complete two-digit terminal LOW jet

After division by $3^{25}$, a beta-channel term visible modulo $9$ must have argument congruent to $13\bmod27$. Since $\nu-1\equiv25\bmod27$, its LOW row has grade



$$
13-25\equiv15.
$$



The $3y$ channel has its additional factor $3$, and $\nu\equiv26$, so its LOW row has grade



$$
13-26\equiv14.
$$



Hence, in monomial LOW coordinates,



$$
\boxed{
\alpha_T/3^{25}
\in
\mathscr U_{15}+3\mathscr U_{14}+9\mathbb Z_3^D.
}
\tag{3.4}
$$



This proves the claimed two-digit grade, including the channel payment.

**Verdict: PASS.**

---

## 4. Inverse orientation and actual inverse closure

This is a place where a formal reflection argument could fail if the inverse order were reversed. The order in A3 Turn 19 is correct.

### 4.1 LOW inverse grades

Let a reflection grade $a$ mean that a matrix entry can be nonzero only when row plus column is $a\bmod27$.

The established actual normalized blocks satisfy, modulo $9$,



$$
\mathcal L_y=L_0+3L_1,\qquad
\mathcal X_y=X_0+3X_1,
$$



with reflection grades $13,12$, respectively.

Finite inversion gives



$$
M_{L,y}
=
M_0-3M_0L_1M_0\pmod9.
$$



Here $M_0$ has reflection grade $13$, and



$$
13-12+13=14,
$$



so the first correction has reflection grade $14$.

The finite HIGH preconditioner $\mathcal K_H$ has reflection grade $13$ modulo $9$. Thus



$$
\mathcal K_H\mathcal X_y^TM_{L,y}
$$



has reflection grade $13$ at order zero and grade $14$ at order one:



$$
13-13+13=13,
$$




$$
13-12+13=14,\qquad
13-13+14=14.
$$



Applying this to (3.4) gives



$$
\mathcal K_H\mathcal X^TM_L\alpha_T
\in
3^{25}
\bigl(\mathscr V_{25}+3\mathscr V_{26}+9\mathscr V\bigr)
\subseteq3^{25}\mathscr E.
\tag{4.1}
$$



The coordinate changes used to establish these grades preserve the pairings. They do not redefine any actual integer column content.

### 4.2 The actual inverse is $\mathcal A^{-1}\mathcal K_H$

Put



$$
\mathcal A=\mathcal K_H\mathcal S_H.
$$



Then



$$
\boxed{M_H=\mathcal A^{-1}\mathcal K_H,}
\tag{4.2}
$$



not $\mathcal K_H\mathcal A^{-1}$.

Since $\mathcal A\equiv I\pmod3$,



$$
\mathcal A^{-1}\equiv2I-\mathcal A\pmod9.
\tag{4.3}
$$



The passed finite result gives $\mathcal A\mathscr E\subseteq\mathscr E$. Because $9\mathscr V\subseteq\mathscr E$, equation (4.3) proves closure under the actual inverse:



$$
\mathcal A^{-1}e=2e-\mathcal Ae+9z\in\mathscr E
\qquad(e\in\mathscr E).
$$



Thus



$$
\boxed{\mathcal A^{-1}\mathscr E\subseteq\mathscr E.}
\tag{4.4}
$$



Combining (4.1)–(4.4),



$$
\boxed{
v_T:=M_H\mathcal X^TM_L\alpha_T\in3^{25}\mathscr E.
}
\tag{4.5}
$$



Since $\mathscr E^Tf_H\subseteq9\mathbb Z_3$,



$$
\boxed{v_T^Tf_H\in3^{27}\mathbb Z_3.}
\tag{4.6}
$$



**Verdict: PASS.** The inverse orientation and the passage from two-digit closure to closure under the actual inverse are both justified.

---

## 5. Payment of $\mathscr N^T\mathcal X^TM_Lf_L$

Let $v\in\mathscr B$, and divide its literal HIGH polynomial exactly:



$$
V_v=x^DP+C,\qquad \deg C<D.
$$



If $c$ is the original LOW-coordinate vector of $C$, then



$$
\mathcal Xv=\alpha[P]+\mathcal Lc,
\qquad
\alpha[P]=G_c(U,x^DP)/3.
$$



Therefore



$$
\boxed{
v^T\mathcal X^TM_Lf_L
=
\alpha[P]^TM_Lf_L+c^Tf_L.
}
\tag{5.1}
$$



The accepted finite bulk LOW estimate gives $\alpha[P]\in3^{25}$, including all admitted masked lower-edge quotients. By (3.2),



$$
\alpha[P]^TM_Lf_L\in3^{49}.
\tag{5.2}
$$



For interior seeds, $C=0$. At the lower mask,



$$
\mathsf Q_{a,0}=3^ay^{d+a},
$$


and


$$
\mathsf T_{a,0}
=
3^{a-1}\sum_{b=0}^{a-1}
(-1)^{a-1-b}\binom D{a-1-b}y^{d+b}.
$$



Thus the remainder is in the weighted span of $3^aC_{d+a}$, $0\le a\le26$. In the terminal lower-mask formula, $3^{a-1}$ pays $3^b$ for every $b\le a-1$.

Equation (2.10) now gives



$$
c^Tf_L\in3^{29}.
$$



Hence



$$
\mathscr B^T\mathcal X^TM_Lf_L\subseteq3^{29}.
\tag{5.3}
$$



Furthermore,



$$
\mathcal X^TM_Lf_L\in3^{24}\mathscr V.
$$



The remaining pieces of $\mathscr N$ pair with this vector in depths at least



$$
25+24=49,\qquad 27+24=51.
$$



Consequently,



$$
\boxed{
\mathscr N^T\mathcal X^TM_Lf_L
\subseteq3^{29}\mathbb Z_3.
}
\tag{5.4}
$$



This payment uses the actual lower remainders. It does not impose a bulk adapted-force estimate on arbitrary exceptional vectors.

**Verdict: PASS.**

---

## 6. Exact block expansion and the physical LOW inverse loss

Set



$$
g_T=\binom{3\alpha_T}{3\upsilon_T},
\qquad
b_0=\binom{9f_L}{9f_H}.
$$



The exact inverse of (1.4) is



$$
E_c^{-1}=
\begin{pmatrix}
\frac13M_L+M_L\mathcal X M_H\mathcal X^TM_L
&
-M_L\mathcal X M_H\\
-M_H\mathcal X^TM_L&M_H
\end{pmatrix}.
\tag{6.1}
$$



Therefore



$$
\boxed{
\begin{aligned}
g_T^TE_c^{-1}b_0
={}&9\alpha_T^TM_Lf_L\\
&+27(\upsilon_T-\mathcal X^TM_L\alpha_T)^T
M_H(f_H-\mathcal X^TM_Lf_L).
\end{aligned}}
\tag{6.2}
$$



The first factor is exactly



$$
3\cdot\frac13\cdot9=9.
$$



Thus the physical $3^{-1}$ loss is explicitly present.

Using $w=M_H\upsilon_T$ and $v_T$ from (4.5), the five terms are



$$
9\alpha_T^TM_Lf_L,
\quad
27w^Tf_H,
\quad
-27v_T^Tf_H,
$$




$$
-27w^T\mathcal X^TM_Lf_L,
\quad
27v_T^T\mathcal X^TM_Lf_L.
$$



Their complete valuation ledger is

| Term | Proven lower bound for $v_3$ |
|---|---:|
| $9\alpha_T^TM_Lf_L$ | $2+25+24=51$ |
| $27w^Tf_H$ | $3+27=30$ |
| $-27v_T^Tf_H$ | $3+27=30$ |
| $-27w^T\mathcal X^TM_Lf_L$ | $3+29=32$ |
| $27v_T^T\mathcal X^TM_Lf_L$ | $3+25+24=52$ |

Thus



$$
\boxed{g_T^TE_c^{-1}b_0\in3^{30}\mathbb Z_3.}
\tag{6.3}
$$



No block return has been omitted.

---

## 7. Prefix provenance, final divisions, and the value of $\eta_0$

### 7.1 The prefix-returned identity is the correct interface

The original prefix boundaries remain



$$
R_*=(9Q+1)/2,\quad a_0=R_*-1,\quad
\tau=(N_0-3)/2,\quad \ell=3R+1,
$$




$$
K=\{0,\ldots,3R\},\qquad J=\{\ell,\ldots,\tau-1\},
\qquad R_*+\tau=\nu.
$$



The exact normalized prefix definitions are



$$
\mathsf A=-G_c(F_{\rm pref},F_{\rm pref})/3^{26},
$$




$$
q[p]=-G_c(F_{\rm pref},F[p])/3^{27},
$$




$$
\widehat F[p]=F[p]-3F_{\rm pref}\mathsf A^{-1}q[p].
$$



For the one-lift,



$$
d_i=G_c(F_{\rm pref},\mathcal F[H_i])/3^{28},
\qquad
Z_i=\mathsf A^{-1}d_i,
$$




$$
K_i=\mathcal F[H_i]+9F[Z_i].
$$



The factor $9$ follows from exact orthogonality:



$$
3^{28}d_i-9\cdot3^{26}\mathsf A Z_i=0.
$$



The finite interior inverse image is the admitted polynomial



$$
\mathcal T_i=y^{131P}(1+y^P+y^{2P})(1-y)^ty^i.
$$



The actual last row of the bordered solve gives



$$
a\eta_i
=
-\frac{G_c(\widehat F_T,K_i-9\widehat F[\mathcal T_i])}{3^{29}}
\pmod3.
$$



Both columns in the second argument are prefix-orthogonal. The prefix-image replacement errors have a factor $27$, while



$$
G_c(F_T,F_{\rm pref})\in3^{27}.
$$



They therefore contribute in $3^{30}$, giving



$$
\boxed{
a\eta_i
=
-\frac{G_c(F_T,F[\Omega_P(1-y)^ty^i])}{3^{29}}
\pmod3.
}
\tag{7.1}
$$



This is the complete residual identity from A1 Turn 13, with its actual endpoint provenance. No ordinary-column compression is applied to $F_T$.

### 7.2 The complete projection and bare payment

Expanding both corrected columns gives



$$
G_c(F_T,F[p_0])
=
G_c(x^Dy^{\nu-1},x^Dp_0)-g_T^TE_c^{-1}b_0.
\tag{7.2}
$$



The passed bare endpoint calculation applies at $i=0$. Its two binomial tops are



$$
H+D+t=(3^{32}+805)\Pi,\qquad
H+D+t+2P=(3^{32}+811)\Pi,
$$



both of valuation $h-33$. At a pole visible modulo $3^{30}$, the coefficient index has valuation $1$ in the beta channel and $0$ in the $3y$ channel. The coefficient payment, together with the active pole weight, is at least $h-33\ge30$. The physical cutoff and factorial term are already paid.

Thus



$$
G_c(x^Dy^{\nu-1},x^Dp_0)\in3^{30}.
\tag{7.3}
$$



Combining (6.3), (7.1)–(7.3),



$$
\boxed{\eta_0=0\in\mathbb F_3.}
\tag{7.4}
$$



### 7.3 The inherited $3^{23}$ scalar division is also paid

Equation (6.2) gives



$$
g_T^TE_c^{-1}b_0\equiv27w^Tf_H\pmod{3^{30}}.
$$



Using (1.10), the paid edge contraction and the two accepted lift contractions,



$$
g_T^TE_c^{-1}b_0
\equiv3^6w_2^Tf_H\pmod{3^{30}}.
$$



The prefix identity and bare cancellation establish integrality of the quotient by $3^{29}$. Hence, before evaluating the final digit,



$$
w_2^Tf_H\in3^{23}\mathbb Z_3,
$$



and division gives



$$
\boxed{
a\eta_0=\frac{w_2^Tf_H}{3^{23}}\pmod3.
}
\tag{7.5}
$$



The already passed annihilator supplies $w_2^Tf_H\equiv0\pmod{3^{24}}$.

The relevant modulus ledger is therefore:

| Operation | Required pre-division information |
|---|---|
| $f_L=G_c(U,x^Dp_0)/9\in3^{24}$ | raw LOW source in $3^{26}$ |
| Quotient/lower-source contraction divided by $9$, result in $3^{29}$ | raw contraction in $3^{31}$ |
| Terminal LOW two-digit jet after extracting $3^{25}$ and dividing by $3$ | raw terminal LOW source modulo $3^{28}$ |
| $\upsilon_T\bmod3^{27}$, divided by $3$ | raw terminal HIGH source modulo $3^{28}$ |
| Exact $r_2\bmod3^{24}$, divided by $9$ | complete numerator modulo $3^{26}$ |
| $3^{23}R_d$ in $r_2$ | retained as $3^{26}R_d$ in the unnormalized residual |
| Precision-$27$ witness divided by $27$ | resulting scalar difference modulo $3^{24}$ |
| Prefix terminal quotient divided by $3^{29}$ | complete pairing modulo $3^{30}$ |
| Final scalar divided by $3^{23}$ | $w_2^Tf_H\bmod3^{24}$ |

The $3^{23}R_d$ forcing term is not deleted. It is already part of the actual finite residual certificate being reused.

### 7.4 Scope of the core conclusion

The new Section 10 lemma does close $\eta_0$ at sufficiently large original **core** indices. No additional source-specific repair is needed.

It does not prove equality of the core and actual-producer terminal vectors, nor any all-orders vanishing in $\mathbb Z_3$. It is not transferred to



$$
Q_{\rm act}=Q_c+3^7\mathscr R,
$$



to physical $7$, or to source precision $34$. The other endpoint and the separate higher ternary block remain outside this audit.

---

# Part II. Independent audit of the complete paired coefficient system

## 8. Reset of notation: the original dyadic family and complete pencil

The symbol $d$ now has its dyadic meaning. It is not the ternary boundary from Part I.

The original domain is



$$
\boxed{k=9^{18+32u},\quad u\ge0,\qquad d=k-1.}
\tag{8.1}
$$



In particular,



$$
v_2(d)=4,\qquad d\equiv2\pmod3,\qquad d\equiv208\pmod{256}.
$$



The sequences are



$$
a_0=1,\qquad a_n=1-na_{n-1},
$$




$$
u_n=a_{2n},\quad f_n=(2n)!,\quad
w_n=(-1)^n,\quad c_n=u_n-w_n,
$$




$$
\rho_0=0,\qquad \rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad r_n=-f_n+4\rho_n.
$$



Their complete returns are



$$
\sigma_n=u_{n+1}+u_n,
$$




$$
\boxed{
\tau_n=-(2n+2)!-(2n)!+\frac4{2n+1}.
}
\tag{8.2}
$$



The physical last row is $2d+1$. The largest moment remains



$$
3d+1=3k-2,
$$



with factorial and odd denominator



$$
(6k-4)!,\qquad 6k-5.
\tag{8.3}
$$



Let



$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),\qquad T_n=\Lambda_k\tau_n,
$$




$$
P_d(x)=\prod_{h=0}^{d-1}(2x+2h+1),\qquad
\mathcal A_dy=\Delta^d(P_dy).
$$



The operator is applied only to the first $d$ original rows, with exact payment



$$
\Omega_k=\prod_{n=0}^{d-1}P_d(n).
$$



Write $\mathfrak b(t)=4t^2+6t+3$. The complete top forcing is



$$
F_k(n,j)=
-\Lambda_k\sum_{i=0}^d(-1)^i\binom di
P_d(n+i)\mathfrak b(n+i+j)(2(n+i+j))!,
$$



and



$$
F_k=-\Lambda_kD_fK_dD_f,\qquad
D_f=\operatorname{diag}((2n)!)_{n<d}.
$$



The established odd leading principal determinants of $K_d$ are reused.

Put



$$
h_d=(2d-2)!,\quad
\beta_d=v_2(h_d),\quad
\alpha_d=v_2((2d)!)=\beta_d+5,
$$




$$
N_d=(h_dD_f^{-1})\operatorname{adj}(K_d)(h_dD_f^{-1}),
$$




$$
\delta_k=\Lambda_k\det(K_d)h_d^2,
\qquad
F_k^{-1}=-N_d/\delta_k.
\tag{8.4}
$$



For residual row $i$, $0\le i<d+2$,



$$
R(i,j)=
\frac{\Lambda_k}{2(d+i+j)+1}
-\frac{\Lambda_k}{4}\mathfrak b(d+i+j)(2(d+i+j))!,
\qquad j<d.
\tag{8.5}
$$



Every Newton divisor is the full integer



$$
D_r=2^rr!.
$$



Define



$$
\mathscr T(y)
=
RN_d(\mathcal A_dy)_{\rm top}
+\frac{\delta_k}{4}y_{\rm bot}.
\tag{8.6}
$$



Then the complete pencil is



$$
\mathcal Q_k(s)
=
[x,z^{(0)},\ldots,z^{(d-1)},\mathfrak b_0+s\mathfrak b_1],
$$




$$
x=\mathscr T(c)/2^d,
\quad
z^{(r)}=\mathscr T(\Delta^r\sigma)/(2^{\alpha_d+1}D_r),
$$




$$
\mathfrak b_0=\Lambda_k\mathscr T(r),
\qquad
\mathfrak b_1=\Lambda_k\mathscr T(w).
\tag{8.7}
$$



Nothing in (8.5) or (8.7) discards either factorial term or the rational part of $r=-f+4\rho$.

---

## 9. Independent derivation of the $\theta$-source normalization

The new $u$-column extension needs more than the statement “replace $\eta$ by $\theta$.” The following derivation supplies its integer hypotheses.

### 9.1 Integer contact numbers and their parity

Let $\mathcal L(t^j)=j!$, extended linearly to polynomials. Then



$$
\mathcal L(F')=\mathcal L(F)-F(0).
\tag{9.1}
$$



The recurrence for $a_n$ gives



$$
u_m=\mathcal L((t-1)^{2m}).
$$



Put $X=t(t-2)=(t-1)^2-1$. Then



$$
\Delta^ru_0=\mathcal L(X^r).
$$



Define



$$
\theta_r=\frac{\mathcal L(X^r)}{2^rr!}.
$$



Using (9.1), first with $F=X^{r+1}$, then with $F=(t-1)X^r$, gives, for $r\ge1$,



$$
\theta_{r+1}=(2r+1)\theta_r+\theta_{r-1},
$$




$$
\theta_0=1,\qquad\theta_1=0.
\tag{9.2}
$$



Thus every $\theta_r$ is an integer. Modulo $2$, the sequence is periodic with values $1,0,1$, equivalently



$$
\theta_r=\operatorname{Tr}(\omega^{r+2})\pmod2.
\tag{9.3}
$$



For a physical base $m$,



$$
\theta_r^{(m)}
=
\frac{\Delta^ru_m}{2^rr!}
=
\sum_{j=0}^{m}
\binom mj2^j(r+1)_j\theta_{r+j}.
\tag{9.4}
$$



Consequently,



$$
\theta_r^{(m)}\in\mathbb Z,\qquad
\theta_r^{(m)}\equiv\theta_r\pmod2,
$$


and exactly



$$
\boxed{
\Delta^j\theta_r^{(m)}
=
2^j(r+1)_j\theta_{r+j}^{(m)}.
}
\tag{9.5}
$$



Also,



$$
\eta_r^{(m)}
=\theta_r^{(m)}+(r+1)\theta_{r+1}^{(m)}.
\tag{9.6}
$$



This proves the required $\theta$-integrality and explains precisely why the physical base disappears only after the specified parity normalization.

### 9.2 Full top rising-factor payment

Let



$$
\mathsf v_n^{(r)}
=
\frac{(\mathcal A_d\Delta^ru)_n}{2^{\alpha_d}D_r}.
$$



Write $o_d=d!/2^{v_2(d!)}$ and



$$
Q_h(n)=\prod_{a=h}^{d-1}(2n+2a+1).
$$



The identities



$$
\Delta^hP_d(n)=2^h\frac{d!}{(d-h)!}Q_h(n),
$$



and the shifted product rule give



$$
\boxed{
\frac{\Delta^j\mathsf v_n^{(r)}}{2^j(d+1)_j}
=
o_d\sum_{h=0}^d
\binom dh Q_h(n)
\binom{d-h+r+j}{r}
\theta_{d-h+r+j}^{(n+h)}
\in\mathbb Z.
}
\tag{9.7}
$$



This includes the new order $r=d$. It pays the full $D_d=2^dd!$, including the odd part of $d!$.

### 9.3 The actual $w$-atom

Let



$$
\mathsf a_w=(\mathcal A_dw)/2^d.
$$



Because $d$ is even,



$$
\frac{\Delta^j\mathsf a_w(n)}{2^j}
=
(-1)^jw_n
\sum_{h=0}^d
\binom{d+j}{h}\frac{d!}{(d-h)!}Q_h(n).
\tag{9.8}
$$



Every term is integral. The $h=0$ term is odd, while every $h\ge1$ term contains the even integer $d$. Hence



$$
\boxed{
\Delta^j\mathsf a_w(n)/2^j\equiv1\pmod2.
}
\tag{9.9}
$$



The original atom satisfies



$$
\frac{\mathcal A_dc}{2^d}
=
2^{\alpha_d-d}\mathsf v^{(0)}-\mathsf a_w.
$$



Thus the replacement used in the paired transformation is tied to the actual atom $c=u-w$, not to an unrelated source.

### 9.4 Complete bottom normalization

Put



$$
L_d=\alpha_d-12,\qquad
A_d=v_2(d!)=\alpha_d-d,
$$




$$
\gamma_k=\frac{\delta_k}{2^{2\beta_d}}
=\Lambda_k\det(K_d)\operatorname{odd}(h_d)^2.
$$



Then $\gamma_k$ is an actual odd integer, not an assumed value $1$, and



$$
v^{(r)}
=
\frac{\mathscr T(\Delta^ru)}{2^{\alpha_d}D_r}
=
RN_d\mathsf v^{(r)}
+2^{L_d}\gamma_k\theta_r^{\rm bot},
\tag{9.10}
$$




$$
w_*=\frac{\mathscr T(w)}{2^d}
=
RN_d\mathsf a_w
+2^{L_d}\gamma_k\,2^{A_d}w_{\rm bot}.
\tag{9.11}
$$



All these columns are integral.

The largest new bottom jet is at



$$
(2d+1)+d=3d+1=3k-2.
$$



Thus the extension does not pass beyond the physical terminal.

**Verdict: PASS for complete source normalization, full divisors, atom, and boundary.**

---

## 10. Exact paired transformation from both complete borders

### 10.1 Complete forcing annihilation

The bottom restriction of the original forcing column $T_j$ is $4Re_j$, while its transformed top is $F_ke_j$. Hence



$$
\mathscr T(T_j)
=
RN_dF_ke_j+\delta_kRe_j=0.
\tag{10.1}
$$



This uses the full $T_j$, with both factorial terms and its rational term.

For $0\le r<d$, $\Delta^r\tau$ is a linear combination of the first $d$ forcing shifts, so



$$
\mathscr T(\Delta^r\tau)=0.
$$



Since $d$ is even,



$$
y=
\frac12\sum_{r=0}^{d-1}
\left(-\frac{\Delta}{2}\right)^r(\Delta+2)y
+2^{-d}\Delta^dy.
$$



Applying this to the complete $r=-f+4\rho$ gives



$$
\boxed{
\mathfrak b_0=\Lambda_k2^{-d}\mathscr T(\Delta^dr).
}
\tag{10.2}
$$



The right side still contains $-\Delta^df+4\Delta^d\rho$.

### 10.2 The common-column relations

From $\sigma=(\Delta+2)u$,



$$
\boxed{z^{(r)}=v^{(r)}+(r+1)v^{(r+1)}.}
\tag{10.3}
$$



Also,



$$
\boxed{x=2^{\alpha_d-d}v^{(0)}-w_*.}
\tag{10.4}
$$



For $0\le r<d$,



$$
v^{(r)}-a_rv^{(d)}
=
\sum_{t=r}^{d-1}
(-1)^{t-r}\frac{t!}{r!}z^{(t)},
$$




$$
a_r=(-1)^{d-r}\frac{d!}{r!}.
\tag{10.5}
$$



The triangular matrix in (10.5) has diagonal entries $1$, determinant $1$, and integer entries.

Set



$$
\kappa_d=2^{\alpha_d-d}d!,
\qquad
\mathfrak c_k=\Lambda_k2^{\alpha_d}d!.
$$



Subtracting $2^{\alpha_d-d}$ times the transformed $r=0$ column from the atom yields



$$
\kappa_dv^{(d)}-w_*.
$$



The original affine border is



$$
\mathfrak b_0+s\Lambda_k2^dw_*.
$$



Adding $s\Lambda_k2^d$ times the transformed atom to this border gives



$$
\mathfrak b_0+s\mathfrak c_kv^{(d)}.
$$



Therefore the exact paired pencil is



$$
\boxed{
\widehat{\mathcal Q}_k(s)=
\left[
\kappa_dv^{(d)}-w_*,
\ (v^{(r)}-a_rv^{(d)})_{r<d},
\ \mathfrak b_0+s\mathfrak c_kv^{(d)}
\right].
}
\tag{10.6}
$$



These are determinant-one column operations over $\mathbb Z[s]$. Both coefficients are preserved exactly.

### 10.3 Audit of $I_1$

Multilinearity, with the affine border contributing $v^{(d)}$, kills every other occurrence of $v^{(d)}$. Thus



$$
\boxed{
I_{1,k}
=
-\mathfrak c_k
\det[w_*,v^{(0)},\ldots,v^{(d)}].
}
\tag{10.7}
$$



### 10.4 Audit of $I_0$

The atom term $\kappa_dv^{(d)}$ crosses $d$ columns, so its sign is positive because $d$ is even.

For the other terms, moving a selected $v^{(d)}$ from position $r$ to the end of the $v$-list contributes



$$
(-1)^{d-1-r}a_r=-d!/r!.
$$



Hence



$$
\boxed{
\begin{aligned}
I_{0,k}
={}&
\kappa_d\det[v^{(0)},\ldots,v^{(d)},\mathfrak b_0]\\
&-\sum_{r=0}^d\frac{d!}{r!}
\det[w_*,v^{(0)},\ldots,\widehat{v^{(r)}},\ldots,v^{(d)},\mathfrak b_0].
\end{aligned}}
\tag{10.8}
$$



Every factorial ratio and every odd factor remains in this identity.

**Verdict: PASS for the paired pencil and both coefficient formulas.**

---

## 11. Mixed $\theta$-jets and the exact finite shift

For a forcing-column set $I$, $|I|=p$, put



$$
Q_I(i)=\prod_{j\in I}(2(d+i+j)+1).
$$



The complete mixed Cauchy identity, with all odd denominators displayed, is



$$
\det[R^{\rm C}[M,I],Z[M,:]]
=
\frac{\Lambda_k^p2^{p(p-1)}\Phi_pV(I)}
{\prod_{i\in M}Q_I(i)}
\det\left[
\binom i0,\ldots,\binom i{p-1},Q_I(i)Z_i
\right].
\tag{11.1}
$$



Here



$$
\Phi_p=\prod_{j=0}^{p-1}j!.
$$



The normalization



$$
\frac{\Delta^\ell Q_I(i)}{2^\ell\ell!}\in\mathbb Z
$$



has parity $\binom p\ell$. Combining this with (9.5),



$$
\frac{\Delta^j(Q_I\theta_r)}{2^jj!}
\equiv
\sum_{t=0}^j
\binom p{j-t}\binom{r+t}{r}\theta_{r+t}
\pmod2.
\tag{11.2}
$$



At $j=p+a$, this is



$$
K_\theta^{(p)}(a,r)
=
\sum_{t=0}^p
\binom pt\binom{r+a+t}{r}\theta_{r+a+t}.
\tag{11.3}
$$



Thus the $\theta$-extension of the mixed residue theorem is valid.

Now let



$$
B_j(r)=\binom{r+j}{r}\theta_{r+j}.
$$



If $E$ shifts the row index $j$, then, exactly over $\mathbb F_2$,



$$
K_\theta^{(D)}(j,\bullet)=(1+E)^DB_j.
$$



Therefore, for every integer $0\le p\le d$,



$$
\boxed{
K_\theta^{(d)}(j,\bullet)
=
(1+E)^{d-p}K_\theta^{(p)}(j,\bullet).
}
\tag{11.4}
$$



This is a finite binomial identity. It has no even-$p$ restriction and does not reverse row and column shifts.

### Scope of the even-size unit recurrences

The already audited dyadic trace recurrence is reused at its stated finite scope. For $\theta$, the transformed kernel



$$
\operatorname{Tr}\left(
\omega^{2+2p}(1+\omega^2Y)^{2p}
\frac1{1+\omega(X+Y)}
\right)
$$



is valid for all $p$. For the displayed $\eta$-numerator in A2 Turn 14, the even-$p$ hypothesis remains relevant.

An even-size determinant recurrence is not a statement that every original product count is even. Nor does a unit in a permitted lower-rank mixed block imply a unit in the full terminal determinant.

The passed both-parity lower-rank windows, and the growing physical flags in their admitted correction window, are not re-proved or extended here.

---

## 12. Audit of the complete full-rank sector payments

Put



$$
n=d+2,\qquad
e_j=v_2\!\left(\frac{h_d}{(2j)!}\right),
\qquad
E_p=\sum_{j=d-p}^{d-1}e_j,
$$




$$
c_p=p(p-1)+2v_2(\Phi_p),
$$




$$
B_p(d)=\binom p2+\sum_{j=0}^{p-2}v_2((d+1)_j),
$$




$$
\lambda_j=j+v_2(j!).
$$



The nominal payment is



$$
\boxed{
\mathcal L_p(d)
=
(n-p)L_d+c_p+2E_p+B_p(d)
+\sum_{j=p}^{n-1}\lambda_j.
}
\tag{12.1}
$$



### 12.1 Exact complete expansion

Write



$$
R=R^{\rm C}-2^{\alpha_d-2}V,
$$




$$
V(i,j)=
\frac{\Lambda_k\mathfrak b(d+i+j)(2(d+i+j))!}{2^{\alpha_d}}.
\tag{12.2}
$$



The determinant in (10.7) is the determinant of



$$
RN_d[\mathsf a_w,\mathsf v^{(0)},\ldots,\mathsf v^{(d)}]
+
2^{L_d}\gamma_k[2^{A_d}w,\theta_0,\ldots,\theta_d].
\tag{12.3}
$$



For a sector with $p$ product columns, $h=n-p$ bottom corrections, and $v$ factorial forcing columns, the scalar is



$$
(2^{L_d}\gamma_k)^h(-2^{\alpha_d-2})^v.
\tag{12.4}
$$



The expansion includes every product-column set and both $p$-element Cauchy–Binet index sets.

### 12.2 Unique minimal $N_d$-sets

The sequence $e_j$ is strictly decreasing because



$$
e_j-e_{j+1}=1+v_2(j+1)\ge1.
\tag{12.5}
$$



Thus the unique $p$-element set minimizing its sum is



$$
T_p=\{d-p,\ldots,d-1\}.
$$



The minor of $\operatorname{adj}(K_d)$ on $T_p,T_p$ is odd: Jacobi’s complementary-minor identity reduces it, up to an odd power of $\det K_d$, to the leading principal minor of size $d-p$.

Consequently,



$$
v_2\det N_d[T_p,T_p]=2E_p,
\tag{12.6}
$$



and every other pair of source sets has at least one additional binary factor.

**Verdict: PASS.**

### 12.3 Every factorial forcing correction is paid

Set



$$
g_j=v_2((2(d+j))!)-\alpha_d.
$$



Column $j$ of $V$ is divisible by $2^{g_j}$, and



$$
\begin{aligned}
e_j+g_j
&=v_2((2(d+j))!)-v_2((2j)!)-5\\
&=2d+s_2(j)-s_2(d+j)-5\\
&\ge2d-m_d-6,
\end{aligned}
\tag{12.7}
$$



where $m_d=1+\lfloor\log_2d\rfloor$.

If $v$ forcing columns are factorial columns, only $a=p-v$ Cauchy columns remain. After Cauchy clearing, the $h$ bottom contact columns pay at least



$$
c_a+\sum_{j=a}^{n-v-1}\lambda_j.
$$



The factorial diagonal and the column payments give at least



$$
E_p+E_{p-v}+v(2d-m_d-6).
$$



Comparison with (12.1), using



$$
E_p-E_{p-v}\le v(2p+m_d),
$$




$$
c_p-c_{p-v}\le4pv,
$$




$$
\lambda_{b+h}-\lambda_b\le2h+m_d,
$$



gives the additional payment



$$
\boxed{
v\bigl(\alpha_d-4p-3m_d-12\bigr).
}
\tag{12.8}
$$



On the original indices this is greater than $2v$ for every $p\le d/3$. For example, $d>256$, $m_d\le d/16$, and $\alpha_d\ge2d-m_d$ give a large positive margin.

Thus factorial forcing corrections are invisible not only at $\mathcal L_p$, but also at the next two nominal layers used below.

This is a column-dependent payment for the complete factorial forcing. It is not an entrywise deletion.

### 12.4 A bottom atom

If the atom is a bottom correction, all $p$ top sources are $u$-contact sources. They have the additional payment



$$
b_p:=v_2((d+1)_{p-1}).
\tag{12.9}
$$



For $p\ge3$, $b_p\ge1$.

The atom has only normalized $2^j$-jets, rather than $2^jj!$-jets. Its explicit factor $2^{A_d}$ pays the missing factorial valuation because



$$
v_2(j!)\le v_2((d+1)!)=v_2(d!)=A_d
\qquad(j\le d+1).
\tag{12.10}
$$



No odd factorial factor is set equal to $1$; these are $\mathbb Z_2$-integral normalizations with their actual odd units retained.

**Verdict: PASS.**

---

## 13. The complete leading Laplace sector is zero

After the payments above, the nominal layer can only come from:

* the atom as a product column;
* no factorial forcing correction;
* $I=J=T_p$;
* every possible choice of which $p-1$ contact columns accompany the atom.

The top atom expansion leaves the following contact rows:

* if $p$ is odd,
  

$$
K_\theta^{(d)}(0),\ldots,K_\theta^{(d)}(p-2);
$$


* if $p$ is even,
  

$$
K_\theta^{(d)}(0),\ldots,K_\theta^{(d)}(p-3),
  \quad
  K_\theta^{(d)}(p-2)+K_\theta^{(d)}(p-1).
$$



The bottom mixed determinant supplies



$$
K_\theta^{(p)}(0),\ldots,K_\theta^{(p)}(h-1),
\qquad h=d+2-p.
$$



The Laplace sum over **all** product/contact choices is the determinant of this stacked $(d+1)$-column contact matrix.

For odd $p$, (11.4) places every row in the span of



$$
K_\theta^{(p)}(0),\ldots,K_\theta^{(p)}(d-2).
$$



For even $p$, the argument in A2 Turn 14 places them in a span of at most $d$ rows. Either bound proves the determinant is zero.

Therefore



$$
\boxed{
\mathcal D_p\in2^{\mathcal L_p(d)+1}\mathbb Z_2,
\qquad 3\le p\le\lfloor d/3\rfloor.
}
\tag{13.1}
$$



This is a complete sector cancellation. A unit in one mixed factor or one lower-rank cofactor cannot refute it.

**Verdict: PASS for every specified $p$, including both parities.**

### 13.1 The nominal minimizer is not an attained valuation

Direct subtraction gives



$$
\boxed{
\begin{aligned}
\mathcal L_{p+1}-\mathcal L_p
={}&8p-2d+5-s_2(p)\\
&+2s_2(d-p-1)-s_2(d+p-1).
\end{aligned}}
\tag{13.2}
$$



The digit terms are $O(\log d)$, so every nominal minimizer lies in



$$
\left|p-\frac d4\right|\le m_d+2.
$$



Also,



$$
\mathcal L_p
=
3d^2-2dp+4p^2+O(d\log d),
$$



whence



$$
\min_p\mathcal L_p=\frac{11}{4}d^2+O(d\log d).
$$



The cancellation theorem applies throughout the minimizing strip. This minimum is a minimum of payments, not an upper bound for the determinant valuation.

---

# Part III. A new complete next-digit result

## 14. The leading stacked matrix has corank at least two

The even-$p$ rank estimate can be sharpened without computing another digit.

For even $p\ge4$:

* the ordinary top rows $K_\theta^{(d)}(0),\ldots,K_\theta^{(d)}(p-3)$ lie in
  

$$
\operatorname{span}\{K_\theta^{(p)}(0),\ldots,K_\theta^{(p)}(d-3)\};
$$


* the bottom rows also lie in that span, since
  

$$
h-1=d+1-p\le d-3;
$$


* only the final combined top row can add one further direction.

Thus the contact rank is at most



$$
(d-2)+1=d-1.
$$



For odd $p$, the earlier span already has dimension at most $d-1$.

Hence, in both cases, the full $n\times n$ normalized matrix, including its atom column, has rank at most



$$
d=n-2
$$



modulo $2$.

An integral matrix of corank at least two modulo $2$ has determinant divisible by $4$: integral row operations lifting row reduction modulo $2$ produce at least two even rows.

This proves a second binary factor for the minimal normalized Laplace matrix. The remaining issue is to pay every other contribution at the same precision.

---

## 15. A uniform source-jet argument pays all tied nonminimal terms

Let $R_j=(d+1)_j$, and define the full source divisor



$$
\mathcal F_p=2^{\binom p2}\prod_{j=0}^{p-2}R_j.
$$



Consider any physical top-row set $J$, and expand it in the finite Newton basis. For a jet-order set



$$
U=\{j_0<\cdots<j_{p-1}\},
$$



an atom-containing source minor has the exact integer factor



$$
\mathcal F(U)
=
2^{\sum j_a}\prod_{a=0}^{p-2}R_{j_a}.
\tag{15.1}
$$



The normalized atom entries are



$$
\frac{R_{j_{p-1}}}{R_{j_a}}
\frac{\Delta^{j_a}\mathsf a_w}{2^{j_a}},
$$



and the normalized contact entries are those in (9.7). Thus all normalizations are integral.

Since $j_a\ge a$,



$$
v_2\bigl(\mathcal F(U)/\mathcal F_p\bigr)
\ge\sum_a(j_a-a).
\tag{15.2}
$$



There are only two jet patterns requiring attention below an excess of two:

1. $U_0=\{0,\ldots,p-1\}$, with excess zero;
2. $U_1=\{0,\ldots,p-2,p\}$, with excess one.

For $U_0$, Section 14 gives corank at least two, so its normalized determinant is divisible by $4$.

For $U_1$, the normalized atom is supported only on its last row modulo $2$. Indeed,



$$
R_p/R_{p-2}=(d+p-1)(d+p)
$$



is even, so no earlier atom entry survives. The remaining top contact rows are



$$
K_\theta^{(d)}(0),\ldots,K_\theta^{(d)}(p-2).
$$



Together with the bottom rows, these lie in the span of



$$
K_\theta^{(p)}(0),\ldots,K_\theta^{(p)}(d-2),
$$



again giving corank at least two.

Every other source-jet pattern already carries at least two extra binary factors by (15.2).

It follows that, for **every** fixed forcing/source pair $I,J$, the entire atom-product Cauchy Laplace sum has two extra factors after its universal nominal payment. This statement includes its complete first-order carries; it is not a parity assertion about one isolated summand.

---

## 16. Complete second-zero theorem

We now combine all categories.

### 16.1 Factorial forcing terms

Equation (12.8) pays at least three extra factors on the original range. They cannot contribute to the next nominal digit.

### 16.2 Atom-product Cauchy terms

Section 15 gives two extra factors for every $I,J$. The factorial-adjugate factors can only increase the payment.

### 16.3 Bottom-atom terms

If $p\ge5$,



$$
b_p=v_2((d+1)_{p-1})\ge3,
$$



because the product includes $d+2$, of valuation $1$, and $d+4$, of valuation $2$.

Only $p=3,4$ require another argument. There $b_p=1$. At their nominal bottom-atom layer, the top contact rows are



$$
K_\theta^{(d)}(0),\ldots,K_\theta^{(d)}(p-1),
$$



and the bottom contact rows are among



$$
K_\theta^{(p)}(0),\ldots,K_\theta^{(p)}(h-1).
$$



Expanding in the bottom atom column, every resulting $(d+1)$-column contact determinant lies in the span of



$$
K_\theta^{(p)}(0),\ldots,K_\theta^{(p)}(d-1),
$$



which has at most $d$ rows. Hence that leading layer is zero, supplying the second factor.

We have proved:

### Theorem 16.1 — complete second nominal digit

On every original dyadic index,



$$
\boxed{
\mathcal D_p\in2^{\mathcal L_p(d)+2}\mathbb Z_2,
\qquad
3\le p\le\lfloor d/3\rfloor.
}
\tag{16.1}
$$



This is a new proved statement. It strengthens A2 Turn 14’s complete sector cancellation by one digit.

It remains a lower divisibility statement. It does not supply a terminal gcd upper bound.

---

## 17. A paid next excess class and a concrete follow-on lemma

For $5\le p\le d/3$, the preceding proof gives a useful sharper reduction modulo $2^{\mathcal L_p+3}$.

* Factorial forcing terms are already deeper.
* Bottom-atom terms are already deeper.
* Every nonminimal $N_d$-source pair has at least one extra factor, and Section 15 supplies two more.

Thus only $I=J=T_p$ remains at this precision.

Let $a=d-p$. Define an $n\times n$ matrix $\mathcal Z_p$, with columns indexed by the atom and $r=0,\ldots,d$.

Its top $p$ rows, $0\le j<p$, are



$$
\left[
\frac{R_{p-1}}{R_j}
\frac{\Delta^j\mathsf a_w(a)}{2^j},
\quad
\left(
\frac{\Delta^j\mathsf v^{(r)}(a)}{2^jR_j}
\right)_{r=0}^d
\right].
\tag{17.1}
$$



Its bottom rows, $p\le j<n$, are



$$
\left[
0,\quad
\left(
\frac{
\Delta_i^j\bigl(Q_{T_p}(i)\theta_r^{(d+i)}\bigr)|_{i=0}
}{2^jj!}
\right)_{r=0}^d
\right].
\tag{17.2}
$$



All entries are integral. These rows use exactly the original physical sources and terminal.

The complete odd prefactor is



$$
\begin{aligned}
u_p={}&
\gamma_k^{\,n-p}\Lambda_k^p
\frac{\det N_d[T_p,T_p]}{2^{2E_p}}
\operatorname{odd}(\Phi_p)^2\\
&\times
\frac{\mathcal F_p}{2^{B_p(d)}}
\frac{\displaystyle\prod_{j=p}^{n-1}\operatorname{odd}(j!)}
{\displaystyle\prod_{i=0}^{n-1}Q_{T_p}(i)}.
\end{aligned}
\tag{17.3}
$$



It is a $\mathbb Z_2$-unit, with all of its actual odd factors retained.

The finite consecutive-row Newton transformations give



$$
\boxed{
\mathcal D_p
\equiv
2^{\mathcal L_p(d)}u_p\det\mathcal Z_p
\pmod{2^{\mathcal L_p(d)+3}},
\qquad 5\le p\le d/3.
}
\tag{17.4}
$$



Moreover,



$$
\det\mathcal Z_p\in4\mathbb Z_2.
$$



Thus the first possibly nonzero digit after the two proved zeros is controlled by a complete finite matrix, not by one selected contact minor.

### A concrete follow-on lemma

The next useful lemma is now specific.

* If $\operatorname{rank}(\overline{\mathcal Z_p})\le n-3$, then the next digit in (17.4) is also zero.
* If $\operatorname{rank}(\overline{\mathcal Z_p})=n-2$, choose a certified unit $(n-2)$-minor and, after fixed row and column permutations, write
  

$$
\mathcal Z_p=
  \begin{pmatrix}A&B\\C&D\end{pmatrix}.
$$


  Then $A^{-1}$ is integral,
  

$$
D-CA^{-1}B\in2M_2(\mathbb Z_2),
$$


  and
  

$$
\boxed{
  \frac{\det\mathcal Z_p}{4}
  =
  \pm\det A\,
  \det\left(\frac{D-CA^{-1}B}{2}\right).
  }
  \tag{17.5}
$$



To evaluate the residue in (17.5), one needs the complete source entries modulo $4$, including the actual atom and mixed $Q_{T_p}$-jets. The division by $2$ in the Schur block requires that pre-division modulus.

The required unit-minor certificate and the complete two-by-two effective residue have not been supplied here. They are an explicit open proof obligation, not an advertised original-sized solve.

Even a nonzero value for one $p$ would still have to be combined with every tied product count in the whole coefficient. In addition, the constant coefficient remains exactly (10.8), with its complete border $\mathfrak b_0$. No $\theta$-only argument has evaluated that border.

---

# Part IV. Audit ledger, normalization, and global status

## 18. Consolidated PASS/REPAIR/OPEN ledger

| New claim or inference | Status |
|---|---|
| A3 quotient extension at $v=0$ | **PASS** |
| A3 lower-source remainders $C_{d+a}$ | **PASS** |
| A3 full $f_L$-depth after division by $9$ | **PASS** |
| Terminal LOW two-digit grades | **PASS** |
| LOW inverse correction grade $14$ | **PASS** |
| Orientation $M_H=\mathcal A^{-1}\mathcal K_H$ | **PASS** |
| Actual inverse closure of $\mathscr E$ | **PASS** |
| Complete $\mathscr N$-LOW-source return payment | **PASS** |
| Five-term block expansion and physical $3^{-1}$ loss | **PASS** |
| Core $\eta_0=0$ | **PASS at the original core scope** |
| Core-to-actual physical-$7$ transfer | **OPEN here; not inferred** |
| A2 complete $\theta$-source normalization through $r=d$ | **PASS** |
| Actual $w$-atom and bottom factor $2^{A_d}$ | **PASS** |
| Forcing annihilation with $-f+4\rho$ retained | **PASS** |
| Unimodular paired pencil | **PASS** |
| Exact $I_0,I_1$ identities | **PASS** |
| Mixed $\theta$-jet formula | **PASS** |
| Exact finite shift for both parities of $p$ | **PASS** |
| Unique minimal $N_d$-sets | **PASS** |
| All factorial forcing corrections in $p\le d/3$ | **PASS** |
| Complete first nominal parity zero | **PASS** |
| Complete second nominal parity zero | **NEW PROVED RESULT** |
| Next excess-class reduction (17.4) | **NEW PROVED RESULT** |
| Nonzero next digit or an $O(d\log d)$ upper bound on excess | **OPEN** |
| Joint terminal upper bound from a lower-rank unit or a lower divisor | **INVALID INFERENCE; repair requires a whole-coefficient noncancellation theorem** |
| Required joint depth and all-prime gcd upper bounds | **OPEN** |

A minor boundary qualification is worth recording separately: a literal four-column flag prefix $1,0,5,4$ requires at least six available columns, hence a dyadic block of size at least $8$. At the size-$2$ unit block, only the truncated prefix $1,0$ is meaningful. This does not affect the paired audit or the growing flags.

---

## 19. The actual ternary forcing and global normalization are unchanged

The actual producer remains



$$
Q_{\rm act}=Q_c+3^7\mathscr R.
$$



Its retained definitions are



$$
F_{\rm fac}=(n-1)!,
$$




$$
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},
$$




$$
\gamma_0=1,\quad\gamma_1=0,\quad
\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1},
$$




$$
h_{\rm vec}
=
T_n^{-1}
\left(\binom{n+a}{a}\gamma_{n+a}\right)_{a=0}^{n-1},
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
\xi=
\frac{u^Tt_{\rm force}}{F_{\rm fac}^2-u^Tv}.
$$



The complete coefficients and endpoint are



$$
[x^a](3^7\mathscr R)
=
-\frac{F_{\rm fac}}{a!}
\bigl((t_{\rm force})_a+\xi v_a\bigr),
\qquad0\le a\le n-1,
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
\tag{19.1}
$$



The complete recurrence is



$$
\mu_{r+1}+\mu_r
=
\frac{3^h}{2r+1}
-\frac{3^h}{4}\bigl((2r+2)!+(2r)!\bigr),
\qquad0\le r\le2n-2.
$$



The later designated index



$$
r_*=(3^h-5)/2
$$



retains its separate division obligations; it is not identified with $r_H$ or with the pole index $(3^h-1)/2$.

The previously specified returns, including



$$
\lambda_{\rm new}
=
\lambda^{\rm pref}
-\frac13f_J^TB^{-1}f_J
-\frac19f_b^TA_b^{-1}f_b,
$$




$$
\lambda_4
=
\lambda_{\rm new}
-\frac1{3^4}f_C^TA_4^{-1}f_C,
$$



are not removed by the core endpoint result.

No actual integer column content has been evaluated here. Let $\ell_{\rm clr}$ remain the actual least simultaneous clearer, and retain



$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
\boxed{G=\gcd(|A_\ell|,|B_\ell|)}
$$



over all primes.

For $B_\ell\ne0$, the actual primitive pair is



$$
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{G},
\qquad
q=\frac{|B_\ell|}{G},
$$



and the whole evaluated error is



$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{G}
\det H_{\rm complete}.
}
\tag{19.2}
$$



An irrationality proof still needs, at the same infinite original ternary indices,



$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$




$$
\log G-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|\longrightarrow+\infty.
$$



The core cancellation supplies none of these global assertions.

---

## 20. The dyadic all-prime ledger and actual primitive error

The original right-column entry clearers remain



$$
\Lambda_{k,j}
=
\operatorname{lcm}(1,3,\ldots,4k+2j-3),
\qquad0\le j<k,
$$



with common least entry clearer $\Lambda_k$.

For



$$
H_k(s)=H_{0,k}+H_{1,k}s,
$$



retain



$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
$$




$$
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$



The actual least simultaneous coefficient clearer and subsequent content are



$$
\boxed{
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
\frac{G_k}{d_{H,k}}.
}
\tag{20.1}
$$



The actual maximal-minor contents of the original rectangles satisfy



$$
\operatorname{lcm}(\mathscr L_k,\mathscr R_k)
\mid G_k\mid\Lambda_k\mathscr L_k\mathscr R_k.
$$



The paid five-column pivots and their actual odd factors are reuse. In particular,



$$
(t_2,t_3,t_4,t_5)=(5,19,39,72),
$$



and, with



$$
\lambda_d=d\alpha_d+4d+4,\qquad
\mathfrak D_d=\prod_{r<d}2^rr!,
$$



the exact all-prime transfer remains



$$
\boxed{
|\delta_k|^{d+2}\Omega_k|\mu_{5,k}|^{d-4}G_k
=
|f_k|\,2^{\lambda_d+d+69}\mathfrak D_d\,g_k^{[5]}.
}
\tag{20.2}
$$



No odd factor in this identity is replaced by $1$.

The exact joint binary target remains



$$
\min(v_2(I_{0,k}),v_2(I_{1,k}))
=
d+69+\nu_k^{[5]},
$$



and the desired upper bound is



$$
\boxed{
\min(v_2(I_{0,k}),v_2(I_{1,k}))
\le
\frac{15}{4}k^2+d+5+O(k\log k).
}
\tag{20.3}
$$



Neither the first nor the second zero digit proves (20.3).

The actual primitive denominator and whole error remain



$$
q_k=\frac{|H_{1,k}|}{G_k}>0,
\qquad
p_k=-\frac{(-1)^kH_{0,k}}{G_k},
$$




$$
\boxed{
0<q_k(e+\pi)-p_k
=
\frac{|H_k(e+\pi)|}{G_k}.
}
\tag{20.4}
$$



The following independent arithmetic obligations are still needed:

* the required binary joint upper bound;
* the stated odd-prime descents for $5\le p\le6k-5$;
* exclusion of primes $p>6k-5$;
* the actual final all-prime $G_k$, rather than a lower divisor.

The established ternary bounds for the original rectangles remain at their stated scope. The accepted same-$H$ analytic lower estimate is also reuse.

If all the contemplated arithmetic upper bounds were proved, the certified analytic margin would show primitive whole-error divergence for this producer. That would retire this producer as a source of primitive error decay; it would not decide the rationality of $e+\pi$.

The ternary core family and this dyadic family have not been merged into a new index set.

---

## 21. Bounded arithmetic and the exact remaining bottleneck

No tools were used, and no new bounded arithmetic execution is indispensable to the proofs in this report.

In particular, no request is made for:

* an original factorial matrix or solve;
* an original-sized source array or Smith calculation;
* a repetition of the closed LOW48 or $729$-position calculations;
* a repeated phase, cofactor, or digit scan.

The new second-zero theorem is proved symbolically by finite Newton normalization, complete Laplace aggregation, and corank. A finite numerical example would verify only that example.

The next mathematical bottleneck is now explicit:

1. Produce a source-specific uniform certificate for the rank and complete modulo-$4$ effective return in (17.5), or prove a further uniform rank defect.
2. Include every tied product count when reconstructing the entire linear coefficient.
3. Evaluate or control the complete constant coefficient (10.8), with $-f+4\rho$, all factorial ratios, and its physical terminal retained.
4. Obtain a noncancellation statement strong enough to give the **joint upper bound**, not another lower divisor.
5. Finish the odd-prime and all-prime normalization ledger and evaluate the whole nonzero error at the same infinite original indices.

If a later coordinator-authorized bounded receipt is supplied for the two-by-two reduction, its required inputs must be certified residues of the actual blocks $A,B,C,D$ of $\mathcal Z_p$ modulo $4$, together with a certified odd determinant of $A\bmod2$. Its verifiable outputs would be:



$$
(D-CA^{-1}B)\equiv0\pmod2,
$$




$$
\det\left((D-CA^{-1}B)/2\right)\pmod2.
$$



This report does **not** claim that constructing those inputs is already a bounded original-index computation. Their uniform source-specific production is part of the open lemma.

---

## Final conclusion

The new A3 Turn 19 LOW-return lemma survives this different audit. In particular,



$$
\boxed{
f_L\in3^{24},\qquad
M_H\mathcal X^TM_L\alpha_T\in3^{25}\mathscr E,
\qquad
\mathscr N^T\mathcal X^TM_Lf_L\subseteq3^{29},
}
$$



and the exact block expansion pays the physical LOW inverse loss:



$$
\boxed{g_T^TE_c^{-1}b_0\in3^{30}\mathbb Z_3.}
$$



Together with the prefix-returned identity and bare endpoint payment, this proves



$$
\boxed{\eta_0=0\in\mathbb F_3}
$$



on the original sufficiently large **core** indices.

The paired A2 identities also pass. Both borders, the actual atom and $w$, the full $D_r$, every odd factor, and the physical terminal remain present. Its complete leading full-rank cancellation is valid for both parities of the specified product count.

The additional result proved here is stronger:



$$
\boxed{
\mathcal D_p\in2^{\mathcal L_p(d)+2}\mathbb Z_2
\quad
(3\le p\le\lfloor d/3\rfloor).
}
$$



Thus another complete nominal terminal digit is zero. The next possible excess class has been reduced with all competing terms paid, but its nonzero value—and, more importantly, the required whole paired upper bound—remains open.

No final all-prime gcd, least clearer, primitive denominator saving, or same-index nonzero whole-error decay has been obtained.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi\text{ is obtained.}}
$$


