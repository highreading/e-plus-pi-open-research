> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Turn 22 — Evaluation of the critical test index and an actual alternating-direction discrepancy

## Abstract

The rationality or irrationality of $e+\pi$ is not decided here.

At the finite-core level, however, the first critical test requested in the assignment can be evaluated. On the unchanged original domain, put


$$
i_\star=\frac{P/27-1}{2}.
$$


The new result is


$$
\boxed{\eta_{i_\star}=\eta_{i_\star+1}=0,\qquad h_{i_\star}=0.}
$$


Since the proposed alternating-direction identity requires $h_{i_\star}=\varepsilon$, with $\varepsilon\in\{1,-1\}$, that identity fails at an actual original index.

This conclusion is obtained from the actual equation


$$
\mathcal S_Hv_T=\upsilon_T.
$$


It is not inferred from a free vector in the exceptional module. Both mixed LOW source terms are retained and evaluated. The complete stationary numerator is proved to be zero modulo $3^{30}$ before division by $3^{29}$.

The main new ingredients are:

1. an explicit source-specific certificate for $M_Hf_i\bmod9$, including the extra $3H$ channel and the literal HIGH boundaries;
2. a primitive-coordinate lemma for the finite bulk module, which recovers the first three weighted quotient contributions from the actual modulo-$27$ terminal certificate;
3. a dual residual calculation that evaluates the complete exceptional pairing through depth $26$;
4. a finite binomial-carry argument that evaluates the remaining critical LOW coefficients, without constructing an original-length source or inverse vector.

The resulting discrepancy changes the next local task: the alternating vector cannot be retained as a leading kernel vector. The true leading kernel and its forcing compatibility must be determined from the repaired, actual terminal source law.

---

## 1. Scope, retained objects, and reused results

### 1.1 Original domain

Every uniform statement below concerns sufficiently large members of exactly the original family


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
D=P_0+N_0,\qquad r\equiv2\pmod9,\qquad r\text{ odd},
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



The retained subwindow is


$$
\boxed{\frac3{25}<\frac{\chi}{P}<\frac{31}{250}.}
\tag{1.1}
$$


No independent choices of $P,\chi$, or $I$ are introduced.

Write


$$
S=h-32,\qquad P=3^S,\qquad H=3^{S+31},\qquad S\ge31,
$$




$$
\Pi=P/3,\qquad t=\Pi-2\chi,
$$




$$
k=3\chi-\Pi-1,\qquad I=k-1=3\chi-\Pi-2,
\qquad \varepsilon=(-1)^{k-2}.
$$


The original arithmetic gives


$$
v_3(D)=v_3(\chi)=v_3(t)=5,\qquad
\chi/243\equiv1\pmod9,
$$




$$
t+I=\chi-2,\qquad I\equiv25\pmod{27}.
\tag{1.2}
$$



Put


$$
c_r=[y^r](1-y)^t,\qquad
c_r=0\quad(r<0\text{ or }r>t),
$$


and


$$
\kappa_2=\frac{P/9-1}{2}.
$$



### 1.2 Literal finite spaces and complete columns

Set $x=y-1$. The original spaces remain


$$
U_u=x^u,\qquad 0\le u<D,
$$




$$
z_i^{\rm mid}=x^Dy^i,\qquad 0\le i<\nu,
\qquad
\nu=D/2-1=134P+\chi-1,
$$




$$
Y_s=y^s,\qquad d\le s\le m,
\qquad d=D+\nu=402P+3\chi-1.
$$


Thus


$$
r_H:=\frac{H-1}{2}=m+\nu.
\tag{1.3}
$$



The physical HIGH terminal is $Y_m$. It is not replaced by the last middle input $y^{\nu-1}$.

The original prefix and tail boundaries remain


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
\qquad K_{\rm phys}=2n-2=2H-2D+2.
$$



Retain


$$
Q_c=(y+1)x^A(\beta+3y),
\qquad \beta=D-H-71,
$$




$$
G_c(f,g)=\mathcal M(Q_cfg),\qquad W=[U\ Y],
\qquad E_c=G_c(W,W),
$$


and every complete corrected column


$$
\boxed{F[p]=x^Dp-WE_c^{-1}G_c(W,x^Dp).}
\tag{1.4}
$$



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
\tag{1.5}
$$


Both normalized inverses are integral. The physical LOW inverse still costs $3^{-1}$.

### 1.3 All fourteen sources

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
p_i=\Omega_P(1-y)^ty^i,\qquad 0\le i\le I.
$$



Equivalently,


$$
p_i=\sum_{(\Delta,b,c)\in\mathcal T}
c(1-y)^{t+\Delta}y^{bP+i},
$$


where


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
\tag{1.6}
$$


Both channels, with multipliers $c\beta$ and $3c$, remain present.

The degree bound is


$$
\deg p_i\le133P+\chi-2=\nu-P-1.
\tag{1.7}
$$



Define


$$
g_T=G_c(W,x^Dy^{\nu-1})
=3\binom{\alpha_T}{\upsilon_T},
$$




$$
G_c(W,x^Dp_i)=\binom{3\alpha_i}{9f_i},
$$




$$
v_T=M_H\upsilon_T,\qquad
d_T=\mathcal X^TM_L\alpha_T,\qquad
d_i=\mathcal X^TM_L\alpha_i.
\tag{1.8}
$$



The complete interface is


$$
a\eta_i=-\frac{G_c(F[y^{\nu-1}],F[p_i])}{3^{29}}\pmod3,
\qquad
a=\overline B_{\ell,\tau-1}\ne0,
\tag{1.9}
$$


and $h_i=\eta_i+\eta_{i+1}$.

### 1.4 Reuse, without scope enlargement

The following established results are used rather than reproved:

- $\alpha_T,\alpha_i,d_T,d_i\in3^{25}$;
- the uniform bare cancellation
  

$$
G_c(x^Dy^{\nu-1},x^Dp_i)\in3^{30};
$$


- the complete four-window law
  

$$
(f_i)_s\equiv
  3[T_i]_{r_1-s}+7[T_i]_{r_3-s}
  +6[T_i]_{r_5-s}+3[T_i]_{r_7-s}\pmod9,
  \tag{1.10}
$$


  where $T_i=(\beta+3y)p_i$ and
  

$$
r_u=\frac{uH/9-1}{2};
$$


- the finite bulk module and actual terminal containment from Turn 18;
- the actual terminal certificate
  

$$
v_T=V^{(0)}+27w_2;
$$


- the complete first-four leading return $R_4=0$, at its stated scope.

No ordinary corrected-pairing compression is applied to $y^{\nu-1}$, $P_d$, or to any other input outside its admitted polynomial domain.

The review labels attached to the supplied work are not upgraded here. The new arguments below are mathematical proofs within these stated finite-core dependencies; no independent audit is claimed.

---

## 2. An evaluated two-digit inverse for the actual source

The first new calculation is an actual inverse application, not an inference from source support.

### 2.1 The two visible digits of the complete moment kernel

Put


$$
L=S+31,\qquad H=3^L,
$$


and use the exact rational kernel


$$
\kappa(q)=-3H\mathcal B(H,q),
$$


where


$$
\mathcal B(N,q)=
\frac{4^N N!(N+q)!(2q)!}
{q!(2N+2q+1)!}.
$$



On the actual range $0\le q\le H-2D+2$, the established valuation law is


$$
v_3\kappa(q)=
\begin{cases}
L+1-v_3(2q+1),&q<r_H,\\
0,&q=r_H,\\
L-v_3(2q+1),&q>r_H.
\end{cases}
\tag{2.1}
$$


The last line includes the extra $3H$ channel.

Modulo $9$, only two positions survive:


$$
\boxed{
\kappa(q)\equiv
7\,\mathbf1_{q=r_H}
+6\,\mathbf1_{q=r_H+H/3}
\pmod9.
}
\tag{2.2}
$$



Here are direct evaluations of both constants.

At $q=r_H$, in the defining beta sum, the denominator-$H$ and denominator-$3H$ terms contribute $-3$ and $1$; all other normalized weights are divisible by $9$. Hence


$$
\kappa(r_H)\equiv-3+1=7\pmod9.
$$



At $q=r_H+H/3$, the only denominator divisible by $H$ that can contribute modulo $9$ is $3H$. It occurs at exponent $2H/3$, giving


$$
-\binom H{2H/3}\equiv-3=6\pmod9.
$$


The congruence follows from


$$
(1-y)^H\equiv(1-y^{H/3})^3\pmod9.
$$



Thus the extra $3H$ channel has been evaluated, not omitted.

### 2.2 A literal HIGH polynomial certificate

Define


$$
\boxed{
\Phi_H(y)=
3y^{4H/9}+y^{H/3}+6y^{2H/9}+3y^{H/9},
}
\tag{2.3}
$$


and let $Z_i$ be the HIGH coefficient vector of


$$
\boxed{V_{Z_i}(y)=x^D\Phi_H(y)p_i(y).}
\tag{2.4}
$$



Every term lies wholly in the original HIGH interval. Indeed, its smallest possible exponent exceeds $d$, while


$$
4H/9+D+\deg p_i<m
$$


because


$$
m-\bigl(4H/9+D+\deg p_i\bigr)
=H/18-O(P)>0.
$$


Neither HIGH boundary is extended.

The LOW force of this polynomial satisfies


$$
\boxed{\alpha[\Phi_Hp_i]\in3^{25}\mathbb Z_3^D.}
\tag{2.5}
$$


To check the hypothesis in the original objects, expand all fourteen terms. Their beta tops are


$$
N=H+t+\Delta,
$$


and their LOW arguments are


$$
q=wH/9+u+bP+i+\delta,
\qquad w\in\{1,2,3,4\},\quad 0\le u<D.
$$


The same low-part bound used in Turn 21 is $<402P$. Each shift $wH/9$ is a multiple of $B_\circ=2187P$, and the actual arguments remain below $r_H$. Consequently all indicators above $S+6$ are absent. The scale is $H=3^{S+31}$, so the valuation is at least $25$. The source coefficients and the $3y$ channel only increase it.

For a HIGH polynomial $x^DP$, the exact adapted equation is


$$
\mathcal S_H[x^DP]
=
G_c(Y,x^DP)-3\mathcal X^TM_L\alpha[P].
\tag{2.6}
$$


The LOW term in (2.6), for $P=\Phi_Hp_i$, is in $3^{26}$.

Using (2.2), the resonant part of $G_c(Y,x^D\Phi_Hp_i)$ gives exactly the four-window coefficients


$$
7(3,1,6,3)\equiv(3,7,6,3)\pmod9.
$$



The second pole in (2.2) must also be checked. Modulo $3$, only the $y^{H/3}p_i$ term in $\Phi_Hp_i$ remains. Its extra-pole row would be


$$
s=r_H-j,\qquad 0\le j\le\deg p_i<\nu.
$$


Hence $s>r_H-\nu=m$, outside the literal HIGH interval. The other three shifted terms carry $3$, so their extra-pole contributions carry $18$ and vanish modulo $9$.

Therefore


$$
\boxed{\mathcal S_HZ_i\equiv f_i\pmod9.}
\tag{2.7}
$$


Since the actual finite $\mathcal S_H$ is a unit matrix over $\mathbb Z_3$,


$$
\boxed{M_Hf_i\equiv Z_i\pmod9.}
\tag{2.8}
$$



This is an evaluated original-coordinate inverse certificate.

### 2.3 The terminal-side mixed LOW term is now paid uniformly

Because $V_{Z_i}=x^D\Phi_Hp_i$,


$$
\mathcal XZ_i=\alpha[\Phi_Hp_i]\in3^{25}.
$$


Equation (2.8) and integrality of $\mathcal X$ give


$$
\mathcal XM_Hf_i\in9.
$$


Thus


$$
d_T^TM_Hf_i
=\alpha_T^TM_L\mathcal XM_Hf_i\in3^{27},
$$


and


$$
\boxed{27d_T^TM_Hf_i\in3^{30}\qquad(0\le i\le I).}
\tag{2.9}
$$



This pays the actual terminal-side LOW source return on all interior indices, including the critical classes.

---

## 3. Recovering the actual quotient contributions

### 3.1 A primitive-coordinate lemma for the finite bulk module

Retain


$$
B_\circ=2187P,\qquad C_\circ=\frac{3^{24}-1}{2}.
$$


For $1\le v\le C_\circ$, consider the unweighted polynomials


$$
x^Dy^{vB_\circ+\nu-1+a},\quad 0\le a\le27,
$$




$$
x^Dy^{vB_\circ}P_{d+a},\quad 0\le a\le26,
$$




$$
x^Dy^{vB_\circ+a},\quad 0\le a\le26.
\tag{3.1}
$$


At $v=0$, use the monomials


$$
y^{d+a},\qquad 0\le a\le26.
\tag{3.2}
$$



The weights are the inherited ones:


$$
3^{(a-1)_+},\qquad 3^a,\qquad 3^a,
$$


and $3^a$ for (3.2).

These generators give a canonical coordinate system for the weighted bulk module.

#### Lemma 3.1 — Primitive independence

The unweighted family (3.1)–(3.2) is linearly independent modulo $3$. Consequently, if an integral combination of these generators lies in $3^r\mathscr V$, then each of its unweighted coefficients lies in $3^r\mathbb Z_3$.

#### Proof

Different $v$-blocks have disjoint support: their widths are less than $B_\circ$, and the original safe-grid inequalities place every interior block wholly inside HIGH.

Within one interior block, factor out $x^Dy^{vB_\circ}$. It suffices to consider


$$
y^{\nu-1+a},\qquad P_{d+a},\qquad y^a.
$$



Write


$$
P_{d+a}=\sum_{j=0}^{\nu+a}b_jy^{\nu+a-j},
\qquad b_j=\binom{D+j-1}{j}.
$$


Since $v_3(D)=5$,


$$
b_j=0\pmod3\quad\text{unless }243\mid j,
$$


and


$$
b_{243}\equiv D/243\equiv2\pmod3.
$$



For each $a=0,\ldots,26$, the coefficient at


$$
y^{\nu+a-243}
$$


isolates $P_{d+a}$: the other quotient polynomials have zero at that position modulo $3$, and neither monomial family reaches it. After eliminating the quotient coefficients, the two monomial families have distinct degrees.

At $v=0$, the exact lower masks are in the span of the monomials (3.2), and the $Q_{a,0}$ already supply those weighted monomials. Thus there is no additional relation.

The assertion for $3^r$ follows by successive division by $3$. ∎

This is a finite-boundary statement. It is not a saturation assertion for an infinite continuation.

### 3.2 The first three weighted quotient coefficients

The actual terminal certificate is


$$
V^{(0)}=e_d+3z_0+9\widehat z_1,
$$


with


$$
V_{z_0}
=x^Dy^{H/3+\nu-1}-y^{d+1},
$$




$$
\begin{aligned}
V_{\widehat z_1}={}&
x^D\left(
y^{4H/9+\nu-1}-y^{2H/9+\nu-1}+y^{H/9+\nu-1}
-y^{H/3}P_d
\right)\\
&+y^{d+2}-y^d.
\end{aligned}
\tag{3.3}
$$



The actual solution satisfies


$$
v_T=V^{(0)}+27w_2
$$


and, by the terminal-module theorem,


$$
v_T=b_T+3^{25}e_T+3^{27}r_T,
\qquad b_T\in\mathscr B.
\tag{3.4}
$$


Therefore


$$
b_T\equiv V^{(0)}\pmod{27}
$$


as original HIGH vectors. Lemma 3.1 transfers this congruence to canonical bulk coefficients.

In the interior quotient families, the resulting paid coefficients are


$$
\begin{array}{c|c}
\text{family}&\text{actual coefficient at the precision that can matter}\\ \hline
Q_{0,v}&-9\,\mathbf1_{vB_\circ=H/3}\pmod{27}\\
Q_{1,v}=3(\text{unweighted quotient})&0\pmod9
\text{ in its weighted coefficient}\\
Q_{2,v}=9(\text{unweighted quotient})&0\pmod3
\text{ in its weighted coefficient}.
\end{array}
\tag{3.5}
$$



At the lower boundary, the first three weighted coefficients are


$$
\boxed{-8,\quad -1,\quad 1}
\tag{3.6}
$$


for


$$
y^d,\qquad 3y^{d+1},\qquad 9y^{d+2},
$$


at precisions $27,9,3$, respectively.

These values come from the actual source equation through its established modulo-$27$ certificate, together with the new primitive-coordinate lemma. Module containment alone would not supply them.

### 3.3 A source-specific quotient of the actual inverse equation

Let


$$
E_i=f_i-\mathcal S_HZ_i.
$$


By (2.7),


$$
E_i\in9\mathscr V.
\tag{3.7}
$$



For every unweighted canonical bulk generator $g$,


$$
\boxed{g^TE_i\in3^{24}.}
\tag{3.8}
$$



The first term $g^Tf_i$ has this depth by the established quotient estimate; terminal and ordinary generators have stronger bounds.

For the second term, adapt $g$ exactly through LOW. Its quotient is one of the actual finite seeds in (3.1), or $P_{d+a}$ at the lower boundary. The rational contraction with $Z_i$ is a finite sum of kernel values at arguments


$$
q=(v+w)B_\circ+q_{\rm lo},
\qquad 0<2q_{\rm lo}+1<1072P<B_\circ.
$$


Thus


$$
v_3(2q+1)\le S+6.
$$


The total grid shift is less than $17H/18$; the physical cutoff is not crossed. Formula (2.1), including its upper-side extra $3H$ contribution, gives depth at least $25$. The Schur LOW term has depth at least $51$. Hence $g^T\mathcal S_HZ_i\in3^{25}$, proving (3.8).

Also,


$$
\upsilon_T^TZ_i
=\frac{G_c(x^Dy^{\nu-1},x^D\Phi_Hp_i)}3\in3^{29},
\tag{3.9}
$$


by the reused uniform terminal-seed estimate on the safe grid.

Now use the actual equation:


$$
v_T^Tf_i
=\upsilon_T^TZ_i+v_T^TE_i.
$$


In (3.4), the exceptional contribution to $E_i$ is in $3^{25}\cdot9=3^{27}$. The canonical coefficients of $b_T-V^{(0)}$ are divisible by $27$, and each corresponding contraction with $E_i$ is in $3^{24}$. Therefore


$$
\boxed{
v_T^Tf_i\equiv
(V^{(0)})^Tf_i-(V^{(0)})^T\mathcal S_HZ_i
\pmod{3^{27}}.
}
\tag{3.10}
$$



This is the crucial source-specific quotient identity. It fixes the exceptional pairing using the actual equation; no exceptional coefficient is chosen freely.

### 3.4 Evaluation of the remaining finite contractions

Put


$$
\mathcal R_i=
G_c(x^DP_d,x^Dy^{H/3}p_i).
\tag{3.11}
$$



The terminal and ordinary terms of $V^{(0)}$, and its literal lower masks, have already been paid. Its only surviving HIGH quotient contribution is the displayed $-9y^{H/3}P_d$. Hence


$$
\boxed{(V^{(0)})^Tf_i\equiv-\mathcal R_i\pmod{3^{27}}.}
\tag{3.12}
$$



For the second contraction in (3.10), the exact monic quotient of $V^{(0)}$ is


$$
\begin{aligned}
P^{(0)}={}&
-8P_d-3P_{d+1}+9P_{d+2}-9y^{H/3}P_d\\
&+3y^{H/3+\nu-1}
+9\bigl(y^{4H/9+\nu-1}-y^{2H/9+\nu-1}
+y^{H/9+\nu-1}\bigr).
\end{aligned}
\tag{3.13}
$$


Its LOW force is in $3^{25}$. Thus


$$
(V^{(0)})^T\mathcal S_HZ_i
\equiv G_c(x^DP^{(0)},x^D\Phi_Hp_i)\pmod{3^{27}}.
$$



Here:

- quotient terms whose total macro shift remains below $r_H$ have raw depth at least $26$;
- arbitrary displayed sums of two macro shifts have raw depth at least $25$;
- the translated terminal terms have raw depth at least $29$.

For the last assertion, the low-level indicator counts from the reused terminal estimate are unchanged. Above level $S+6$, only one additional indicator—the $3H$ indicator—can now appear. The former raw depth $30$ therefore becomes at worst $29$.

The explicit weights in (3.13) and $\Phi_H$ consequently remove every term modulo $3^{27}$ except


$$
-8\,G_c(x^DP_d,x^Dy^{H/3}p_i).
$$


Therefore


$$
\boxed{
(V^{(0)})^T\mathcal S_HZ_i
\equiv-8\mathcal R_i\pmod{3^{27}}.
}
\tag{3.14}
$$



Combining (3.10), (3.12), and (3.14) proves the uniform actual HIGH-return identity


$$
\boxed{
v_T^Tf_i\equiv7\mathcal R_i\pmod{3^{27}}.
}
\tag{3.15}
$$



In particular, the complete exceptional pairing in (3.4) satisfies


$$
\boxed{
3^{25}e_T^Tf_i\equiv8\mathcal R_i\pmod{3^{27}}.
}
\tag{3.16}
$$


This evaluates its depth-$25$ and depth-$26$ contracted coefficients. It is not a claim that an arbitrary coordinate of $e_T$ can be read from module membership.

### 3.5 A single evaluated kernel coefficient

Define


$$
q_9=\frac{729P-1}{2},
\qquad
\zeta_i=[y^{q_9}](1-y)^DP_dp_i\pmod3.
\tag{3.17}
$$



The polynomial multiplying the shifted kernel in $\mathcal R_i$ has degree less than $536P$. Since its arguments are $H/3+q_{\rm lo}<r_H$, only


$$
q_{\rm lo}=q_9
$$


can survive modulo $3^{27}$. At this point


$$
v_3\kappa(H/3+q_9)=26,
\qquad
3^{-26}\kappa(H/3+q_9)\equiv1\pmod3.
$$


For completeness, the unit follows from


$$
(2q+1)\mathcal B(H,q)
=
\mathcal B(H,0)
\prod_{r=1}^q\frac{2r+1}{2H+2r+1}.
$$


For $q<r_H$, each factor is $1\pmod3$, while


$$
\mathcal B(H,0)
=\frac{4^H}{(2H+1)\binom{2H}{H}}
\equiv2\pmod3.
$$


The minus sign in $\kappa=-3H\mathcal B$ gives the stated unit.

Therefore


$$
\boxed{
\mathcal R_i\equiv3^{26}\zeta_i\pmod{3^{27}},
\qquad
v_T^Tf_i\equiv3^{26}\zeta_i\pmod{3^{27}}.
}
\tag{3.18}
$$


The exceptional contribution in (3.16) has zero depth-$25$ digit and depth-$26$ digit $2\zeta_i$.

---

## 4. The source-side mixed LOW return

This term must still be evaluated separately.

### 4.1 Removing the LOW inverse by exact monic division

For $r\ge D$, write


$$
y^r=C_r+x^DP_r,\qquad \deg C_r<D.
$$


In particular,


$$
C_r=\sum_{u=0}^{D-1}\binom ru x^u.
$$



The LOW remainder of $V^{(0)}$ is


$$
\boxed{C^{(0)}=-8C_d-3C_{d+1}+9C_{d+2}.}
\tag{4.1}
$$


The adapted quotient $P^{(0)}$ has LOW force in $3^{25}$, so


$$
(V^{(0)})^Td_i
=(C^{(0)})^T\alpha_i
+\alpha[P^{(0)}]^TM_L\alpha_i.
$$


The second term is in $3^{50}$.

Also,


$$
9(v_T-V^{(0)})^Td_i\in3^{30}.
$$


Thus


$$
\boxed{
9v_T^Td_i\equiv3G_c(C^{(0)},x^Dp_i)\pmod{3^{30}}.
}
\tag{4.2}
$$



### 4.2 The boundary coefficients in the remainder recurrence

Put


$$
J_D=D/2,
\qquad \nu=J_D-1,\qquad d=3J_D-1.
$$


The exact recurrence is


$$
yC_{d+a}=C_{d+a+1}+b_{\nu+a+1}x^D.
\tag{4.3}
$$



Two coefficients are needed:


$$
b_{\nu+1}=b_{J_D}
=\binom{3J_D-1}{J_D},
\qquad
b_{\nu+2}=b_{J_D+1}.
$$



Legendre’s formula gives


$$
v_3b_{J_D}
=\frac{s_3(D)}2-1.
$$


Since


$$
D=268P+2\chi,\qquad 0<2\chi<P,
$$


and $s_3(268)=6$, while the positive even integer $2\chi$ has ternary digit sum at least $2$,


$$
\boxed{b_{\nu+1}\in3^3,\qquad b_{\nu+2}\in3^5.}
\tag{4.4}
$$


The second assertion also follows directly from


$$
b_j=\frac Dj\binom{D+j-1}{j-1},
$$


because $J_D+1$ is a unit.

Now $\beta\equiv10\pmod{27}$. Substituting (4.3) into (4.1) yields


$$
\boxed{(\beta+3y)C^{(0)}\equiv C_d\pmod{27}.}
\tag{4.5}
$$


Explicitly, the coefficients of $C_d,C_{d+1},C_{d+2}$ are


$$
-8\beta,\qquad -3\beta-24,\qquad9\beta-9,
$$


which are $1,0,0\pmod{27}$; the two $x^D$ corrections vanish by (4.4).

### 4.3 The five-pole law with its paid precisions

Let


$$
\mathcal U=\{1,3,5,7,9\},
\qquad
q_u=\frac{81uP-1}{2},
$$


and define the literal integer coefficients


$$
C_{u,i}=[y^{q_u}]C_dp_i.
\tag{4.6}
$$



The degree of $(\beta+3y)C^{(0)}p_i$ is less than $402P$. Hence every local kernel value has valuation at least $26$. Equation (4.5) can therefore be used modulo $27$ after the outer factor $3$ in (4.2).

Only the five positions $q_u$ can survive modulo $3^{30}$, giving


$$
9v_T^Td_i\equiv
3\sum_{u\in\mathcal U}\kappa(q_u)C_{u,i}
\pmod{3^{30}}.
\tag{4.7}
$$



The required weights can also be evaluated. For $H=3^L$, $L\ge2$,


$$
\binom{2H}{H}\equiv20\pmod{27}.
$$


Indeed,


$$
\frac{\binom{6u}{3u}}{\binom{2u}{u}}
=
\prod_{\substack{1\le r\le3u\\3\nmid r}}
\left(1+\frac{3u}{r}\right).
$$


For $u$ divisible by $9$, this is $1\pmod{27}$; for $u=3$, the linear term vanishes because the unit residues occur in pairs summing to zero modulo $3$. Reduction to $\binom63=20$ follows. Consequently


$$
\mathcal B(H,0)\equiv20^{-1}=23=-4\pmod{27}.
$$



For $q<402P$, the product in the beta recurrence differs from $1$ by an element of $3^{25}$. Therefore


$$
3\kappa(q_u)\equiv4\,\frac{3^{29}}u\pmod{3^{30}},
$$


with the powers of $3$ in $u=3,9$ paid before reduction. Thus


$$
\boxed{
\begin{aligned}
9v_T^Td_i\equiv{}&
3^{29}C_{1,i}
+4\cdot3^{28}C_{3,i}
+2\cdot3^{29}C_{5,i}\\
&+3^{29}C_{7,i}
+4\cdot3^{27}C_{9,i}
\pmod{3^{30}}.
\end{aligned}}
\tag{4.8}
$$



The necessary coefficient precisions are, respectively,


$$
\boxed{3,\quad9,\quad3,\quad3,\quad27.}
\tag{4.9}
$$



As a useful uniform consequence, $C_dp_i\bmod27$ is supported at degree $i-1\pmod{27}$, whereas every $q_u\equiv13\pmod{27}$. Hence


$$
\boxed{
9v_T^Td_i\in3^{30}
\quad\text{if }i\not\equiv14\pmod{27}.
}
\tag{4.10}
$$


This is a new source-return statement, not a refinement assumed from source support alone.

---

## 5. A complete stationary coefficient law

The exact Schur expansion is


$$
\begin{aligned}
g_T^TE_c^{-1}G_c(W,x^Dp_i)={}&
27v_T^Tf_i+3\alpha_T^TM_L\alpha_i\\
&-9v_T^Td_i-27d_T^TM_Hf_i
+9d_T^TM_Hd_i.
\end{aligned}
\tag{5.1}
$$


The direct and double LOW terms are in $3^{51}$ and $3^{52}$. The bare pairing is in $3^{30}$, and (2.9) pays the terminal-side mixed LOW term.

Combining (3.18) and (4.8), the complete numerator in the interface satisfies


$$
\boxed{
\begin{aligned}
N_i\equiv{}&
3^{29}\bigl(\zeta_i-C_{1,i}-2C_{5,i}-C_{7,i}\bigr)\\
&-4\cdot3^{28}C_{3,i}
-4\cdot3^{27}C_{9,i}
\pmod{3^{30}},
\end{aligned}}
\tag{5.2}
$$


where


$$
a\eta_i=N_i/3^{29}\pmod3.
$$



Equation (5.2) is a source-specific finite coefficient law. It includes the complete HIGH correction and both mixed LOW source terms. It is not yet an evaluation of every critical index. The required coefficients are evaluated next at the literal test index.

---

## 6. Full evaluation at $i_\star$

Put


$$
g=P/27,\qquad i_\star=\frac{g-1}{2}.
$$


The original window gives $i_\star+1\le I$, and in fact $i_\star<I-1$, for all sufficiently large admitted tuples.

Also,


$$
i_\star\equiv13\pmod{27}.
$$



### 6.1 A finite-quotient divisibility lemma

Write


$$
\chi=3g+u.
$$


The retained window gives


$$
\frac6{25}<\frac ug<\frac{87}{250},
\qquad 2u<g,
$$




$$
v_3(u)=5,\qquad u/243\equiv1\pmod9.
$$


Moreover,


$$
J_D=134P+\chi=3621g+u.
$$



For $0\le n\le3621$, define


$$
t_n=b_{J_D-ng}.
\tag{6.1}
$$


These are coefficients of the actual finite quotient $P_{d+1}$, not of an extended reciprocal series.

#### Lemma 6.1

For every $0\le n\le3621$,


$$
\boxed{t_n\in3,}
\tag{6.2}
$$


and, if $n\equiv4\pmod9$,


$$
\boxed{t_n\in9.}
\tag{6.3}
$$



#### Proof

The coefficient


$$
t_n=\binom{D+J_D-ng-1}{J_D-ng}
$$


has valuation equal to the number of ternary carries in


$$
(D-1)+(J_D-ng).
$$



Modulo $g$, the two summands are $2u-1$ and $u$. The ternary digits of $u$ at positions $5,6$ are $1,0$. Since $u>6g/25$, there is a later nonzero digit below the $g$-boundary. At the first such digit, addition of $u$ and $2u-1$ produces a carry, whether that digit is $1$ or $2$. This proves (6.2).

If $n\equiv4\pmod9$, then


$$
J_D-ng\equiv8g+u\pmod{9g},
$$




$$
D-1\equiv6g+2u-1\pmod{9g}.
$$


Their sum exceeds $9g$, so there is an additional carry across the $9g$-boundary. It is distinct from the carry below $g$. This proves (6.3). ∎

### 6.2 Evaluation of the actual HIGH return

At $i=i_\star$, the polynomial


$$
(1-y)^DP_dp_i\bmod3
$$


has degree grade $i-1\equiv12\pmod{27}$, while $q_9\equiv13\pmod{27}$. Hence


$$
\zeta_{i_\star}=0.
\tag{6.4}
$$



For $i=i_\star+1$, use


$$
yP_d=P_{d+1}-b_{J_D},
\qquad b_{J_D}\in27.
$$


Modulo $3$, only the $(\Delta,b,c)=(2P,122,1)$ source remains. Also


$$
D+t+2P=7299g.
$$


The requested coefficient becomes a finite sum of coefficients $t_n$, multiplied by integer binomial coefficients. Each $t_n$ is divisible by $3$, by Lemma 6.1. Therefore


$$
\zeta_{i_\star+1}=0.
\tag{6.5}
$$



Equations (3.18), (6.4), and (6.5) give


$$
\boxed{
v_T^Tf_{i_\star},\quad v_T^Tf_{i_\star+1}\in3^{27}.
}
\tag{6.6}
$$



They also evaluate the actual exceptional pairing from (3.16): its depth-$26$ contracted coefficient is zero at both indices. The free perturbation discussed in Turn 21 is therefore excluded by the actual source equation.

### 6.3 A fixed binomial band

The source-side LOW term at $i_\star$ is already zero by (4.10). It remains to evaluate the five coefficients for $i_\star+1$.

The needed carry fact is the following fixed statement:


$$
\boxed{
\begin{array}{ll}
v_3\binom{7299}{l}\ge2,
&2926\le l\le6547,\quad9\nmid l,\\[1mm]
v_3\binom{7299}{l}\ge1,
&2926\le l\le6547,\quad9\mid l.
\end{array}}
\tag{6.7}
$$



For $3\nmid l$, the first bound follows from


$$
\binom{7299}{l}=\frac{7299}{l}\binom{7298}{l-1},
\qquad v_3(7299)=2.
$$



For $l=9r+3$ or $9r+6$, use the finite identity


$$
\begin{aligned}
(1-Z)^{7299}\equiv{}&
(1-Z^9)^{811}\\
&+3\cdot811(-Z^3+Z^6)(1-Z^9)^{810}
\pmod9.
\end{aligned}
\tag{6.8}
$$


Over $\mathbb F_3$,


$$
(1-Z)^{810}=(1-Z^{729})(1-Z^{81}),
$$


whose support is $\{0,81,729,810\}$. None lies in the relevant range $325\le r\le727$. Thus these coefficients vanish modulo $9$.

For $l=9r$, the leading coefficient is a coefficient of


$$
(1-Z)^{811}
=(1-Z)(1-Z^{81})(1-Z^{729})
\quad\text{over }\mathbb F_3.
$$


Its support is


$$
\{0,1,81,82,729,730,810,811\},
$$


disjoint from $326\le r\le727$. This proves the second line of (6.7).

No long binomial calculation is hidden in this step.

### 6.4 Evaluation of all fourteen LOW-source contributions

By (4.3)–(4.4),


$$
yC_d\equiv C_{d+1}\pmod{27}.
$$


The $y^{d+1}$ term in


$$
C_{d+1}=y^{d+1}-(1-y)^DP_{d+1}
$$


is outside every coefficient range now requested, because


$$
q_9-i_\star<365P<d+1.
$$



Set


$$
K_u=\frac{2187u-1}{2},
\qquad
R_{u,b}=K_u-27b.
$$


The exact finite carry congruences


$$
(1-y)^{D+t+2P}\equiv(1-y^g)^{7299}\pmod{27},
$$




$$
(1-y)^{D+t}\equiv(1-y^g)^{7245}\pmod{27}
$$


give


$$
\boxed{
C_{u,i_\star+1}\equiv
-\sum_{(\Delta,b,c)\in\mathcal T}
c\sum_{n=0}^{3621}
(-1)^{R_{u,b}-n}
\binom{M_\Delta}{R_{u,b}-n}t_n
\pmod{27},
}
\tag{6.9}
$$


where


$$
M_{2P}=7299,\qquad M_0=7245,
$$


and out-of-range binomial coefficients are zero.

The sum in (6.9) is now evaluated at the precision required by (4.9).

#### Unit-denominator positions $u=1,5,7$

Every $t_n$ is in $3$. Hence


$$
\boxed{C_{1,i_\star+1},C_{5,i_\star+1},C_{7,i_\star+1}\in3.}
\tag{6.10}
$$



#### The position $u=3$

For the coefficient-$1$ source $b=122$,


$$
R_{3,122}=3280-3294=-14,
$$


so its contribution is exactly zero.

Every other source coefficient is divisible by $3$, and every $t_n$ is divisible by $3$. Therefore


$$
\boxed{C_{3,i_\star+1}\in9.}
\tag{6.11}
$$



#### The position $u=9$

For the coefficient-$1$ source $b=122$,


$$
R_{9,122}=9841-3294=6547.
$$


Thus $l=6547-n$ lies in $2926\le l\le6547$.

- If $9\nmid l$, (6.7) supplies two powers of $3$, and $t_n$ supplies a third.
- If $9\mid l$, then $n\equiv6547\equiv4\pmod9$. Lemma 6.1 supplies two powers of $3$, and (6.7) supplies the third.

So the whole coefficient-$1$ source is zero modulo $27$.

For the coefficient-$3$ source $b=41$:

- if $9\nmid l$, the binomial coefficient supplies at least one power of $3$, and $t_n$ another;
- if $9\mid l$, then again $n\equiv4\pmod9$, so $t_n\in9$.

After the source factor $3$, every term is in $27$.

Finally, each of the twelve remaining source coefficients is already in $9$, and $t_n\in3$. Hence all twelve are zero modulo $27$.

Therefore


$$
\boxed{C_{9,i_\star+1}\in27.}
\tag{6.12}
$$



All fourteen sources have now been paid at their actual required precisions.

### 6.5 The whole numerator, before division

For $i=i_\star$, equations (4.10) and (6.4) make every term of (5.2) zero modulo $3^{30}$.

For $i=i_\star+1$, equations (6.5), (6.10), (6.11), and (6.12) do the same.

The terminal-side LOW return is zero modulo $3^{30}$ by (2.9), the direct and double LOW terms are deeper, and the complete bare pairing is zero modulo $3^{30}$.

Thus the complete stationary numerators satisfy


$$
\boxed{N_{i_\star},N_{i_\star+1}\in3^{30}.}
\tag{6.13}
$$


Only now divide the whole numerators by $3^{29}$ in the complete interface (1.9). Since $a$ is a unit,


$$
\boxed{
\eta_{i_\star}=\eta_{i_\star+1}=0,\qquad h_{i_\star}=0.
}
\tag{6.14}
$$



---

## 7. The actual directional discrepancy and the repaired obligation

The already checked original-index moment evaluation is


$$
c_{\kappa_2-i_\star}=c_{P/27}=1,
$$


while


$$
c_{\kappa_2-i_\star-1}
=c_{\kappa_2-I-i_\star}
=c_{\kappa_2-I-i_\star-1}=0.
$$


Hence the proposed identity requires


$$
h_{i_\star}=\varepsilon.
$$



The actual value (6.14) gives


$$
\boxed{
h_{i_\star}
-\varepsilon\left(
c_{\kappa_2-i_\star}+c_{\kappa_2-i_\star-1}
+\varepsilon(c_{\kappa_2-I-i_\star}
+c_{\kappa_2-I-i_\star-1})
\right)
=-\varepsilon\ne0.
}
\tag{7.1}
$$



This is an actual original-index discrepancy.

In the retained leading assembly


$$
B_6=N^TC^{\rm mom}N-(e'h^T+he'^T),
$$


the row $i_\star$ is not the last row. Since $h_{i_\star}=0$, the alternating vector satisfies


$$
\boxed{(B_6z_{\rm alt})_{i_\star}=1.}
\tag{7.2}
$$


Thus


$$
\boxed{z_{\rm alt}\notin\ker\overline B_6.}
$$



No full rank or kernel theorem follows from this one evaluated discrepancy.

### A concrete repaired direction condition

If a replacement is sought in the form $z=z_{\rm alt}+u$, its correction must satisfy the explicit original-row equation


$$
\boxed{
\sum_{j=0}^{I-1}
\left(
c_{\kappa_2-i_\star-j}
+2c_{\kappa_2-i_\star-j-1}
+c_{\kappa_2-i_\star-j-2}
\right)u_j=-1.
}
\tag{7.3}
$$


This row has no unknown terminal-return entry.

A concrete next lemma is therefore:

> **Repaired critical-source and kernel lemma.**  
> Evaluate the remaining critical coefficients $\zeta_i$ and $C_{u,i}$ in the actual finite law (5.2), at their stated precisions, and use the resulting true $h$ to determine the kernel of the original finite
> 

$$
> B_6=N^TC^{\rm mom}N-(e'h^T+he'^T).
>
$$


> Any proposed replacement direction must satisfy (7.3), the remaining original rows, and the actual leading force-compatibility equations.

Even after such a leading kernel calculation, an allowed $3^{-1}$ solve requires the whole next equation


$$
\overline B_6z_1+
\overline{B_6\widehat z_0/3}
=\overline w_6.
\tag{7.4}
$$


A leading kernel does not pay (7.4).

---

## 8. Precision ledger

| Quantity | Required information/payment | Result here |
|---|---|---|
| $f_i\bmod9$ | Raw HIGH source divided by $9$, with its dangerous denominator already paid | Four-window law reused |
| $M_Hf_i\bmod9$ | Actual finite Schur operator, both boundaries, extra $3H$ pole | Explicit $Z_i$ certificate |
| $\alpha[\Phi_Hp_i]$ | Full fourteen-term shifted LOW source | Depth $25$ |
| Terminal-side mixed LOW | $27d_T^TM_Hf_i$ | Uniformly in $3^{30}$ |
| First three weighted quotient coefficients | Actual $v_T\bmod27$, not module containment alone | Recovered by primitive-coordinate lemma |
| Exceptional HIGH pairing | $3^{25}$-layer through its next digit | Evaluated as $8\mathcal R_i\bmod3^{27}$ |
| Actual HIGH return | $v_T^Tf_i\bmod3^{27}$ | $3^{26}\zeta_i$ |
| Source-side mixed LOW | $9v_T^Td_i\bmod3^{30}$ | Five explicit coefficient weights |
| LOW coefficients at $i_\star+1$ | Moduli $3,9,3,3,27$ | All evaluated as zero at those precisions |
| Bare terminal pairing | Modulo $3^{30}$ | Reused uniform zero |
| Direct/double LOW terms | Physical LOW inverse $3^{-1}$ retained | Depths $51,52$ |
| Final $\eta$, $h$ division | Whole numerator modulo $3^{30}$ before $3^{29}$ division | Whole zero proved at both critical test indices |
| Whole $B_6\bmod9$, source $34$ | Separate next-digit calculation | Open |

The new proof does not require a finer exceptional inverse grading. It uses the actual two-digit source inverse and the actual finite terminal equation instead.

---

## 9. Later physical layers and complete forcing remain separate

The actual producer is still


$$
\boxed{Q_{\rm act}=Q_c+3^7\mathscr R.}
$$


No core cancellation above is promoted to physical $7$.

Retain


$$
F_{\rm fac}=(n-1)!,
$$




$$
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},
\qquad0\le a,b<n,
$$




$$
\gamma_0=1,\qquad\gamma_1=0,\qquad
\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1},
$$




$$
h_{\rm vec}
=T_n^{-1}
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
=3nh_{\rm vec}+(b_{\rm force}+6)e_{n-1}
+\frac{2b_{\rm force}}{n-1}e_{n-2},
$$




$$
\xi=\frac{u^Tt_{\rm force}}{F_{\rm fac}^2-u^Tv}.
$$


Under their original existence and denominator hypotheses,


$$
[x^a](3^7\mathscr R)
=-\frac{F_{\rm fac}}{a!}
\bigl((t_{\rm force})_a+\xi v_a\bigr),
\qquad0\le a\le n-1,
$$




$$
\mathscr R(-1)=-\frac{\xi F_{\rm fac}^2}{3^7}.
$$



The complete forcing identity remains


$$
\boxed{
J^T\boldsymbol\varepsilon+\omega
=
-\boldsymbol\varepsilon
-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
}
\tag{9.1}
$$


Both forcing terms remain.

The complete recurrence is


$$
\mu_{r+1}+\mu_r
=
\frac{3^h}{2r+1}
-\frac{3^h}{4}\bigl((2r+2)!+(2r)!\bigr),
\qquad0\le r\le2n-2.
$$


The shifted label


$$
r_*=\frac{3^h-5}{2}
$$


is retained; the displayed denominator pole occurs at $r=r_*+2$.

The diagonal force payments remain


$$
\lambda_{\rm new}
=
\lambda^{\rm pref}
-\frac13f_J^TB^{-1}f_J
-\frac19f_b^TA_b^{-1}f_b
\in3^{-2}\mathbb Z_3,
$$




$$
\boxed{
\lambda_4
=
\lambda_{\rm new}
-\frac1{3^4}f_C^TA_4^{-1}f_C
\in3^{-4}\mathbb Z_3.
}
\tag{9.2}
$$


The leading operator identity $R_4=0$ neither evaluates its next digit nor evaluates the different force contraction in $\lambda_4$.

Still open are:

- actual/core transport at physical $7$;
- physical-$5$ complementary and kernel-pivot returns;
- next digits of earlier returns;
- higher endpoint adaptation;
- the complete stationary source at precision $34$.

The passed higher ternary producer theorem does not supply these actual inverse and source statements.

---

## 10. Actual contents, least clearer, all-prime gcd, and whole error

No actual integer column content is changed or evaluated by the new local discrepancy. The contents remain those of the complete original columns.

The least simultaneous clearer remains the actual $\ell_{\rm clr}$, not a convenient multiple or a power of $3$. Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the final gcd over all primes


$$
\boxed{G=\gcd(|A_\ell|,|B_\ell|).}
$$


For $B_\ell\ne0$, the primitive pair is


$$
\boxed{
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{G},
\qquad q=\frac{|B_\ell|}{G}.
}
$$



The whole evaluated error remains


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
G\det H_{\rm complete}.
}
\tag{10.1}
$$


When the determinant is nonzero,


$$
|q(e+\pi)-p|
=
\frac{\ell_{\rm clr}^{m+1}}G
|\det H_{\rm complete}|>0.
$$



An irrationality proof still requires, at the same infinite original indices,


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
\tag{10.2}
$$


These conditions would make the nonzero whole errors tend to zero. If $e+\pi=a/b$ were rational, every nonzero integer linear error would have absolute value at least $1/b$.

The present finite-core result proves none of these global normalization, nonvanishing, or decay requirements.

---

## 11. Bounded exact arithmetic and proof status

No tools or numerical execution were used. No new computation is indispensable to the proof.

A coordinator-authored auxiliary receipt may check the new fixed binomial band only.

### Bounded inputs

- the integer top $7299$;
- the integer range $2926\le l\le6547$;
- the two fixed polynomials $(1-Z)^{810}$ and $(1-Z)^{811}$ over $\mathbb F_3$.

### Expected verifiable outputs

1. For every $l$ in that range with $9\nmid l$,
   

$$
\binom{7299}{l}\equiv0\pmod9.
$$


2. For every $l$ in that range with $9\mid l$,
   

$$
\binom{7299}{l}\equiv0\pmod3.
$$


3. The exact supports
   

$$
\operatorname{supp}(1-Z)^{810}
   =\{0,81,729,810\},
$$


   

$$
\operatorname{supp}(1-Z)^{811}
   =\{0,1,81,82,729,730,810,811\}
$$


   over $\mathbb F_3$.

This is a fixed calculation with binomial top $7299$. It is not an original-index solve, an original-length source table, or a rerun of the closed LOW/729 calculations. Its finite scope would verify only this new carry receipt; the uniform proof is the symbolic argument above.

### Consolidated status

| Item | Status |
|---|---|
| Uniform bare cancellation and noncritical results | Reused |
| Actual $M_Hf_i\bmod9$ | Newly evaluated |
| Terminal-side mixed LOW return | Newly paid uniformly |
| First three weighted quotient contributions | Newly recovered from actual terminal certificate |
| Complete exceptional pairing through depth $26$ | Newly evaluated by the actual source equation |
| Source-side mixed LOW return | New five-coefficient law |
| $\eta_{i_\star},\eta_{i_\star+1}$ | Newly proved zero |
| $h_{i_\star}$ | Newly proved zero |
| Proposed uniform alternating identity | Disproved at the original index $i_\star$ |
| Alternating leading kernel membership | Disproved in the retained leading assembly |
| True leading rank/kernel and force compatibility | Open |
| Whole allowed modulo-$9$ lift | Open |
| Actual physical $7$/source $34$ | Open |
| Actual contents, least clearer, all-prime $G$, primitive $q$ | Unevaluated |
| Same-index nonzero whole error and decay | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

---

## Conclusion

The critical test is now evaluated from the actual finite terminal equation:


$$
\boxed{
\eta_{i_\star}=\eta_{i_\star+1}=0,\qquad
h_{i_\star}=0,
\qquad i_\star=\frac{P/27-1}{2}.
}
$$



Both mixed LOW source terms have been included. The first three weighted quotient contributions are fixed by the actual modulo-$27$ certificate and a primitive-coordinate lemma. The exceptional pairing is fixed by an explicit source-specific inverse certificate and the actual equation $\mathcal S_Hv_T=\upsilon_T$. All fourteen LOW source terms are paid at their required precisions.

The complete stationary numerator is zero modulo $3^{30}$ before division by $3^{29}$.

Since the proposed directional identity requires $h_{i_\star}=\varepsilon\ne0$, the alternating direction fails:


$$
\boxed{(B_6z_{\rm alt})_{i_\star}=1.}
$$



The exact next local bottleneck is therefore no longer “prove that the alternating vector is a kernel vector.” It is to evaluate the remaining critical coefficients in the actual law (5.2), determine the true leading kernel subject to the explicit repaired row condition (7.3), and then pay the separate whole modulo-$9$ forcing equation.

The global bottleneck remains unchanged: actual physical transport, actual all-prime primitive normalization, and a nonzero whole error tending to zero at the same infinite original indices.



$$
\boxed{\text{No unconditional rationality or irrationality decision for }e+\pi\text{ follows.}}
$$


