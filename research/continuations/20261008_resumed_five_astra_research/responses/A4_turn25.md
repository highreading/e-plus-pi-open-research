> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A Different Audit of A1 Turns 20–22

## Actual critical-index evaluation, finite first-four return, and the remaining next-digit obstruction

### Executive conclusions

The principal new claim of Turn 22 **passes this audit on the unchanged original domain**:



$$
\boxed{
\eta_{i_\star}=\eta_{i_\star+1}=0,\qquad
h_{i_\star}=0,\qquad
i_\star=\frac{P/27-1}{2}.
}
$$



This conclusion follows from the **actual finite equation**


$$
\mathcal S_Hv_T=\upsilon_T,
$$


not from a freely chosen element of the exceptional module. The proof retains both mixed LOW returns, the extra $3H$ channel, the literal finite HIGH boundaries, and all fourteen terms of $\Omega_P$. It establishes that the **whole stationary numerator** is in $3^{30}\mathbb Z_3$ before division by $3^{29}$.

The resulting discrepancy is genuine. At the same original index,


$$
c_{\kappa_2-i_\star}=1,
$$


whereas the other three coefficients in the proposed alternating-direction identity vanish. Consequently,


$$
\boxed{(B_6z_{\rm alt})_{i_\star}=1\quad\text{in }\mathbb F_3.}
$$


Thus the proposed alternating vector is not a leading kernel vector of the retained finite core assembly.

This is a **local candidate failure**. It is not a proof that the full construction cannot be repaired, and it gives no rationality or irrationality conclusion for $e+\pi$.

The principal conclusions of Turns 20 and 21 also pass at their stated core scopes:

- Turn 20 pays the complete mixed-prefix quotient and proves
  

$$
P_{ui}=0
$$


  for every original amplitude and every stated column.
- Its finite first-four inverse certificate retains the upper $3y$ corner and proves the **entire leading returned operator**
  

$$
R_4=0.
$$


- Turn 21 proves the all-interior bare cancellation, the fully divided four-window HIGH source law, and its stated noncritical $\eta$- and $h$-zero laws.

There is one harmless hypothesis repair in Turn 22: the deduction


$$
\mathcal B(3^L,0)\equiv-4\pmod{27}
$$


requires $L\ge3$, not merely $L\ge2$. The original domain has $L=S+31\ge62$, so this repair changes none of the original-index conclusions.

A distinct new calculation is supplied below for the first-four next-digit problem. For the literal integer moment lifts on the original complement, their returned operator satisfies


$$
\boxed{
R_4^\sharp\equiv-3C^{\rm mom}\pmod9.
}
$$


This evaluates a nontrivial part of the first-four next digit. It does **not** identify those integer lifts with the actual whole first-four blocks. The actual next digit still requires the complete source and return corrections specified in Section 6.

No unconditional decision about $e+\pi$ is obtained.

---

## 1. Scope, original objects, and accepted dependencies

Write $v_3$ for the $3$-adic valuation. All congruences below are in the appropriate finite $\mathbb Z_3$-module, and every uniform assertion concerns sufficiently large members of exactly the admitted family


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
D=P_0+N_0,\qquad r\equiv2\pmod9,\qquad r\text{ odd},
$$


and


$$
4^j=243(3^{26}-1)P-243r+1.
$$


Also,


$$
Q=27P,\qquad Q-N_0=2R,\qquad \chi=P-R,
$$


so that


$$
N_0=25P+2\chi,\qquad D=268P+2\chi.
$$



The subwindow is unchanged:


$$
\boxed{\frac3{25}<\frac{\chi}{P}<\frac{31}{250}.}
\tag{1.1}
$$


No independent choices of $P,\chi$, or the index bounds will be made.

Set


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


The retained arithmetic gives


$$
v_3(D)=v_3(\chi)=v_3(t)=5,\qquad
\chi/243\equiv1\pmod9,
$$




$$
t+I=\chi-2,\qquad I\equiv-2\pmod{243}.
\tag{1.2}
$$


In particular $I\equiv25\pmod{27}$.

Define


$$
c_r=[y^r](1-y)^t,\qquad c_r=0\quad(r<0\text{ or }r>t),
\qquad
\kappa_2=\frac{P/9-1}{2}.
$$



### 1.1 Literal finite spaces and complete columns

With $x=y-1$, retain


$$
U_u=x^u,\quad 0\le u<D,
$$




$$
z_i^{\rm mid}=x^Dy^i,\quad 0\le i<\nu,
\qquad \nu=D/2-1=134P+\chi-1,
$$




$$
Y_s=y^s,\quad d\le s\le m,
\qquad d=D+\nu=402P+3\chi-1.
$$


Thus


$$
r_H:=\frac{H-1}{2}=m+\nu.
\tag{1.3}
$$



The physical terminal is $Y_m$. It is not the last middle input $y^{\nu-1}$.

The finite prefix and tail data remain


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
Q_c=(y+1)x^A(\beta+3y),\qquad
\beta=D-H-71,
$$




$$
G_c(f,g)=\mathcal M(Q_cfg),\qquad W=[U\ Y],
\qquad E_c=G_c(W,W),
$$


and the complete columns


$$
\boxed{
F[p]=x^Dp-WE_c^{-1}G_c(W,x^Dp).
}
\tag{1.4}
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
\tag{1.5}
$$


The normalized inverses are integral. The physical LOW inverse is still


$$
\boxed{3^{-1}M_L.}
$$



### 1.2 All fourteen sources

The complete polynomial is


$$
\begin{aligned}
\Omega_P(y)={}&
(1-y)^{2P}(y^{122P}+3y^{41P})\\
&+9(1+y^P+y^{2P})
(2y^{14P}+2y^{41P}+2y^{95P}-y^{131P}).
\end{aligned}
$$


For $0\le i\le I$,


$$
p_i=\Omega_P(1-y)^ty^i
=\sum_{(\Delta,b,c)\in\mathcal T}
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


For each row, both channels


$$
c\beta,\qquad 3c\,y
$$


remain present until their valuations have been paid.

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
a\eta_i
=-\frac{G_c(F[y^{\nu-1}],F[p_i])}{3^{29}}\pmod3,
\qquad a=\overline B_{\ell,\tau-1}\ne0,
\tag{1.9}
$$


and $h_i=\eta_i+\eta_{i+1}$.

### 1.3 Reuse and audit convention

The audit reuses, without enlarging their scopes:

- the established finite LOW/HIGH unit theorems;
- the finite terminal-module theorem and its actual terminal certificate;
- the original complete prefix/terminal interface;
- complete corrected-pairing compression through source precision $33$, only for admitted ordinary polynomial parts;
- the original finite prefix inverse and finite first-four complement theorem;
- the previously passed core $\eta_0$ result;
- the standard finite binomial, beta, Hankel and Schur identities.

No ordinary compression is applied to $y^{\nu-1}$ or $P_d$ merely because an ordinary-source theorem exists.

The separately passed higher ternary theorem supplies only its stated local producer/weighted-period conclusion. It is not an actual physical-$7$ transport or source-$34$ theorem. The literature abstracts mentioned in the assignment are not used as finite source or LOW theorems.

“PASS” below means that the new proof has been checked within these exact established dependencies. It does not upgrade an unrelated inherited proof or a later physical claim.

---

## 2. Priority audit: Turn 22’s actual stationary evaluation

## 2.1 The HIGH kernel and its extra $3H$ channel

For nonnegative integers $N,q$, the beta identity is


$$
\mathcal B(N,q)
=\sum_{r=0}^N\frac{(-1)^r\binom Nr}{2q+2r+1}
=
\frac{4^N N!(N+q)!(2q)!}{q!(2N+2q+1)!}.
$$


Set


$$
L=S+31,\qquad H=3^L,\qquad
\kappa(q)=-3H\mathcal B(H,q).
$$



On the actual range


$$
0\le q\le H-2D+2,
$$


the indicator formula gives


$$
v_3\kappa(q)=
\begin{cases}
L+1-v_3(2q+1),&q<r_H,\\
0,&q=r_H,\\
L-v_3(2q+1),&q>r_H.
\end{cases}
\tag{2.1}
$$



Here is the reason for the change above $r_H$. At levels $e\le L$, $H\bmod3^e=0$, so the indicators count divisibility of $2q+1$. At modulus $3H$, the additional indicator occurs exactly when $q\ge r_H$ on this range. Higher indicators are absent. This is the extra channel that cannot be discarded in upper-side contractions.

Modulo $9$, only


$$
q=r_H,\qquad q=r_H+H/3
$$


survive.

At $q=r_H$, the denominator-$H$ endpoint contributes $-3$, and the denominator-$3H$ endpoint contributes $1$. All other weights are in $9\mathbb Z_3$. Hence


$$
\kappa(r_H)\equiv7\pmod9.
$$



At $q=r_H+H/3$, the only relevant denominator divisible by $H$ is $3H$, at binomial exponent $2H/3$. Its contribution is


$$
-\binom H{2H/3}\equiv-3\equiv6\pmod9.
$$


Therefore


$$
\boxed{
\kappa(q)\equiv
7\mathbf1_{q=r_H}
+6\mathbf1_{q=r_H+H/3}\pmod9.
}
\tag{2.2}
$$



**Verdict: PASS.** The additional $3H$ channel has the stated coefficient and is essential.

---

## 2.2 The literal inverse certificate $M_Hf_i\bmod9$

Define


$$
\Phi_H
=3y^{4H/9}+y^{H/3}+6y^{2H/9}+3y^{H/9},
$$


and let $Z_i$ be the original HIGH coefficient vector of


$$
V_{Z_i}=x^D\Phi_Hp_i.
\tag{2.3}
$$



### Finite boundaries

The smallest possible exponent exceeds $d$, because $H/9\gg P$. At the upper boundary,


$$
\begin{aligned}
m-\bigl(4H/9+D+\deg p_i\bigr)
&\ge
\frac H{18}-535P-4\chi+\frac52\\
&>0
\end{aligned}
$$


on the original domain. Thus every term of $V_{Z_i}$ lies in the literal interval $d\le s\le m$.

### LOW force

For each of the fourteen sources, a shifted LOW beta term has


$$
N=H+t+\Delta,\qquad
q=wH/9+u+bP+i+\delta,
$$


where $w\in\{1,2,3,4\}$, $0\le u<D$, and $\delta=0,1$.

The low part satisfies


$$
(t+\Delta)+u+bP+i+\delta<402P.
$$


Each macro shift is divisible by


$$
B_\circ=2187P=3^{S+7}.
$$


At levels $S+7,\ldots,L$, the least possible half-residue is farther from the low part than $N-H$. At modulus $3H$, all these arguments are still below $r_H$, so the extra indicator is absent. Thus at most $S+6$ indicators occur, giving


$$
\boxed{\alpha[\Phi_Hp_i]\in3^{25}.}
\tag{2.4}
$$


This includes all fourteen coefficients and the $3y$ channel.

For a HIGH polynomial $x^DP$,


$$
\mathcal S_H[x^DP]
=G_c(Y,x^DP)-3\mathcal X^TM_L\alpha[P].
\tag{2.5}
$$


The LOW correction for $P=\Phi_Hp_i$ is therefore in $3^{26}$.

The resonant coefficient $7$ in (2.2) converts the four coefficients of $\Phi_H$ into


$$
7(3,1,6,3)\equiv(3,7,6,3)\pmod9,
$$


which are precisely the four-window source coefficients.

For the second pole, only the unit term $y^{H/3}p_i$ can matter modulo $9$. Its row would be


$$
s=r_H-j,\qquad 0\le j\le\deg p_i<\nu,
$$


so $s>m$. The other three terms have an extra factor $3$, and their second-pole contributions vanish modulo $9$.

It follows that


$$
\mathcal S_HZ_i\equiv f_i\pmod9.
$$


The actual finite matrix $\mathcal S_H$ is a unit matrix over $\mathbb Z_3$, hence


$$
\boxed{M_Hf_i\equiv Z_i\pmod9.}
\tag{2.6}
$$



This is an inverse application certified by multiplication in the original finite matrix. It is not an inference from source support.

### Terminal-side mixed LOW return

Since


$$
\mathcal XZ_i=\alpha[\Phi_Hp_i]\in3^{25},
$$


equation (2.6) gives


$$
\mathcal XM_Hf_i\in9.
$$


Using $\alpha_T\in3^{25}$,


$$
d_T^TM_Hf_i
=\alpha_T^TM_L\mathcal XM_Hf_i\in3^{27}.
$$


Therefore


$$
\boxed{27d_T^TM_Hf_i\in3^{30}\qquad(0\le i\le I).}
\tag{2.7}
$$



**Verdict: PASS, uniformly on the stated original index range.**

---

## 2.3 Primitivity of the finite bulk coordinates

The unweighted interior generators are


$$
x^Dy^{vB_\circ+\nu-1+a},\quad 0\le a\le27,
$$




$$
x^Dy^{vB_\circ}P_{d+a},\quad 0\le a\le26,
$$




$$
x^Dy^{vB_\circ+a},\quad 0\le a\le26,
\tag{2.8}
$$


for


$$
1\le v\le C_\circ=\frac{3^{24}-1}{2}.
$$


At the lower boundary use $y^{d+a}$, $0\le a\le26$.

Their block widths are less than $B_\circ$. The uppermost block ends before $m$, since


$$
C_\circ B_\circ=\frac{H-B_\circ}{2}
$$


and


$$
\frac{H-B_\circ}{2}+d+26<m.
$$


Thus distinct $v$-blocks, and the lower boundary block, have disjoint supports.

Within one interior block, factor out the injective polynomial multiplier $x^Dy^{vB_\circ}$. Write


$$
P_{d+a}=\sum_{j=0}^{\nu+a}b_jy^{\nu+a-j},
\qquad b_j=\binom{D+j-1}{j}.
$$


Because $v_3(D)=5$,


$$
b_j\equiv0\pmod3\quad\text{unless }243\mid j,
\qquad
b_{243}\equiv D/243\equiv2\pmod3.
$$


For each $a$, the coefficient of $y^{\nu+a-243}$ isolates $P_{d+a}$. The other quotient generators have coefficient zero there modulo $3$, while the two monomial families do not reach that degree.

After eliminating the quotient coefficients, the remaining monomial degrees are distinct. The lower masks are already in the span of the weighted lower monomials supplied by the quotient family.

Hence the unweighted family is independent modulo $3$. Repeated reduction and division by $3$ proves the stronger statement:

> If an integral linear combination of these unweighted generators belongs to $3^r\mathscr V$, every coefficient belongs to $3^r\mathbb Z_3$.

This is exactly the primitivity needed to recover coefficients from an original-coordinate congruence.

The actual terminal certificate is


$$
V^{(0)}=e_d+3z_0+9\widehat z_1,
$$


with


$$
V_{z_0}=x^Dy^{H/3+\nu-1}-y^{d+1},
$$




$$
\begin{aligned}
V_{\widehat z_1}={}&x^D\bigl(
y^{4H/9+\nu-1}-y^{2H/9+\nu-1}
+y^{H/9+\nu-1}-y^{H/3}P_d
\bigr)\\
&+y^{d+2}-y^d.
\end{aligned}
\tag{2.9}
$$


Together with


$$
v_T=V^{(0)}+27w_2
$$


and the actual terminal-module containment


$$
v_T=b_T+3^{25}e_T+3^{27}r_T,\qquad b_T\in\mathscr B,
$$


primitivity transfers $b_T\equiv V^{(0)}\pmod{27}$ to canonical coefficients.

The resulting quotient coefficients are exactly:



$$
\begin{array}{c|c}
\text{weighted family}&\text{coefficient precision}\\ \hline
Q_{0,v}&-9\,\mathbf1_{vB_\circ=H/3}\pmod{27}\\
Q_{1,v}=3(\text{unweighted quotient})&0\pmod9\\
Q_{2,v}=9(\text{unweighted quotient})&0\pmod3.
\end{array}
\tag{2.10}
$$



The lower weighted coordinates


$$
y^d,\qquad 3y^{d+1},\qquad 9y^{d+2}
$$


have coefficients


$$
\boxed{-8,\ -1,\ 1}
\tag{2.11}
$$


at precisions $27,9,3$, respectively.

**Verdict: PASS.** This is a finite primitive-coordinate argument, not an infinite saturation assumption.

---

## 2.4 The two complete contractions and the exceptional pairing

Put


$$
E_i=f_i-\mathcal S_HZ_i\in9\mathscr V.
$$



For every unweighted canonical bulk generator $g$,


$$
g^Tf_i\in3^{24}.
$$


For $g^T\mathcal S_HZ_i$, exact LOW adaptation leaves a rational kernel contraction with arguments


$$
q=vB_\circ+wH/9+q_{\rm lo},
\qquad 0<2q_{\rm lo}+1<1072P<B_\circ.
$$


Consequently


$$
v_3(2q+1)\le S+6.
$$


The largest macro shift is below $17H/18$, and the full argument remains in


$$
0\le q\le H-2D+2.
$$


Formula (2.1), including its upper-side extra indicator, gives raw depth at least $25$. The Schur LOW term has depth at least $51$. Hence


$$
g^TE_i\in3^{24}.
\tag{2.12}
$$



Also,


$$
\upsilon_T^TZ_i
=\frac{G_c(x^Dy^{\nu-1},x^D\Phi_Hp_i)}3
\in3^{29},
\tag{2.13}
$$


by the uniform translated terminal estimate audited in Section 4 below.

The actual equation now gives


$$
v_T^Tf_i=\upsilon_T^TZ_i+v_T^TE_i.
$$


The exceptional part contributes at least $3^{25}\cdot9=3^{27}$. The bulk coefficient difference $b_T-V^{(0)}$ is divisible by $27$, and (2.12) pays its contraction. Therefore


$$
\boxed{
v_T^Tf_i\equiv
(V^{(0)})^Tf_i-(V^{(0)})^T\mathcal S_HZ_i
\pmod{3^{27}}.
}
\tag{2.14}
$$



This step fixes the contracted exceptional digit by the actual source equation.

Define


$$
\mathcal R_i=G_c(x^DP_d,x^Dy^{H/3}p_i).
\tag{2.15}
$$



### First contraction

In $(V^{(0)})^Tf_i$, all terminal and lower-mask terms are paid by the uniform terminal and lower-mask estimates. The only surviving quotient term is


$$
-9x^Dy^{H/3}P_d.
$$


Since $f_i$ is the HIGH source divided by $9$,


$$
\boxed{(V^{(0)})^Tf_i\equiv-\mathcal R_i\pmod{3^{27}}.}
\tag{2.16}
$$



### Second contraction

The exact monic quotient of $V^{(0)}$ is


$$
\begin{aligned}
P^{(0)}={}&-8P_d-3P_{d+1}+9P_{d+2}-9y^{H/3}P_d\\
&+3y^{H/3+\nu-1}
+9\bigl(y^{4H/9+\nu-1}-y^{2H/9+\nu-1}
+y^{H/9+\nu-1}\bigr).
\end{aligned}
\tag{2.17}
$$


Its LOW force is in $3^{25}$, so


$$
(V^{(0)})^T\mathcal S_HZ_i
\equiv G_c(x^DP^{(0)},x^D\Phi_Hp_i)\pmod{3^{27}}.
$$



The complete payment is:



$$
\begin{array}{c|c|c}
\text{term type}&\text{raw depth}&\text{effect of explicit weights}\\ \hline
P_d,P_{d+1},P_{d+2}\text{ with a single }\Phi_H\text{ shift}
&\ge26&\text{only }-8P_d\cdot y^{H/3}p_i\text{ can survive}\\
y^{H/3}P_d\text{ with a }\Phi_H\text{ shift}
&\ge25&\text{its factor }9\text{ pays depth }27\\
\text{translated terminal terms}
&\ge29&\text{their factors }3\text{ or }9\text{ pay depth }30.
\end{array}
$$



For the translated terminal terms, the low-level indicator count is unchanged. Above level $S+6$, at most one new indicator appears: the $3H$ indicator. Thus the old raw depth $30$ becomes at worst $29$, not an unaccounted lower depth.

Therefore


$$
\boxed{
(V^{(0)})^T\mathcal S_HZ_i
\equiv-8\mathcal R_i\pmod{3^{27}}.
}
\tag{2.18}
$$



Combining (2.14), (2.16), and (2.18),


$$
\boxed{v_T^Tf_i\equiv7\mathcal R_i\pmod{3^{27}}.}
\tag{2.19}
$$



Moreover,


$$
b_T^Tf_i\equiv(V^{(0)})^Tf_i\pmod{3^{27}},
$$


so the complete exceptional pairing is


$$
\boxed{3^{25}e_T^Tf_i\equiv8\mathcal R_i\pmod{3^{27}}.}
\tag{2.20}
$$



### Evaluating $\mathcal R_i$

Set


$$
q_9=\frac{729P-1}{2},
\qquad
\zeta_i=[y^{q_9}](1-y)^DP_dp_i\pmod3.
$$


The polynomial multiplying the shifted kernel has degree less than $536P$. All arguments are below $r_H$. Modulo $3^{27}$, the only possible surviving local argument is $q_9$, since


$$
0<2q_{\rm lo}+1<1072P
$$


and the required divisibility is $729P\mid2q_{\rm lo}+1$.

At that point


$$
v_3\kappa(H/3+q_9)=26.
$$


The recurrence


$$
(2q+1)\mathcal B(H,q)
=\mathcal B(H,0)
\prod_{r=1}^q\frac{2r+1}{2H+2r+1}
$$


shows that the normalized unit is $1\pmod3$: below $r_H$, every product factor is $1\pmod3$, while $\mathcal B(H,0)\equiv2\pmod3$, and the minus sign in $\kappa$ supplies the final unit.

Thus


$$
\boxed{
\mathcal R_i\equiv3^{26}\zeta_i,\qquad
v_T^Tf_i\equiv3^{26}\zeta_i\pmod{3^{27}}.
}
\tag{2.21}
$$


Equation (2.20) has zero depth-$25$ digit and depth-$26$ digit $2\zeta_i$.

**Verdict: PASS for both complete contractions and both exceptional digits.**

---

## 2.5 Literal LOW remainder, recurrence, and all five pole weights

For $r\ge D$, use exact monic division


$$
y^r=C_r+x^DP_r,\qquad
C_r=\sum_{u=0}^{D-1}\binom ru x^u.
$$


The remainder of $V^{(0)}$ is


$$
C^{(0)}=-8C_d-3C_{d+1}+9C_{d+2}.
\tag{2.22}
$$



Exact LOW adaptation gives


$$
(V^{(0)})^Td_i
=(C^{(0)})^T\alpha_i
+\alpha[P^{(0)}]^TM_L\alpha_i.
$$


The second term is in $3^{50}$, and


$$
9(v_T-V^{(0)})^Td_i\in3^{30}.
$$


Therefore


$$
\boxed{
9v_T^Td_i\equiv3G_c(C^{(0)},x^Dp_i)\pmod{3^{30}}.
}
\tag{2.23}
$$



Put $J_D=D/2$. Then $\nu=J_D-1$ and $d=3J_D-1$. The exact recurrence is


$$
yC_{d+a}=C_{d+a+1}+b_{\nu+a+1}x^D.
\tag{2.24}
$$



For the needed coefficients,


$$
v_3b_{J_D}=\frac{s_3(D)}2-1.
$$


Since


$$
D=268P+2\chi,\qquad 0<2\chi<P,\qquad s_3(268)=6,
$$


and $2\chi$ is a positive even integer, $s_3(2\chi)\ge2$. Hence


$$
b_{J_D}\in3^3.
$$


Also


$$
b_{J_D+1}
=\frac D{J_D+1}\binom{D+J_D}{J_D},
$$


and $J_D+1$ is a unit, so $b_{J_D+1}\in3^5$.

Now $\beta\equiv10\pmod{27}$. Expanding $(\beta+3y)C^{(0)}$ using (2.24), the coefficients of $C_d,C_{d+1},C_{d+2}$ are


$$
-8\beta,\qquad -3\beta-24,\qquad 9\beta-9,
$$


which are $1,0,0\pmod{27}$. The remaining terms are multiples of $27$, including the $x^D$ corrections. Thus


$$
\boxed{(\beta+3y)C^{(0)}\equiv C_d\pmod{27}.}
\tag{2.25}
$$



The degree of the LOW polynomial is less than $402P$. Every relevant kernel value has depth at least $26$, so the error in (2.25), after the outer factor $3$, is in $3^{30}$.

For


$$
u\in\{1,3,5,7,9\},\qquad
q_u=\frac{81uP-1}{2},
\qquad
C_{u,i}=[y^{q_u}]C_dp_i,
$$


only these five positions can survive.

### The small hypothesis repair

The central-binomial congruence


$$
\binom{2\cdot3^L}{3^L}\equiv20\pmod{27}
$$


is valid for the range used in the source. But the further conclusion


$$
\mathcal B(3^L,0)\equiv20^{-1}=-4\pmod{27}
$$


also uses $2\cdot3^L+1\equiv1\pmod{27}$, and therefore requires $L\ge3$.

For $L=2$, that latter conclusion is false. The original domain has $L\ge62$, so the correct hypothesis is automatically satisfied.

For $q<402P$, the product in the beta recurrence is $1\pmod{3^{25}}$. Consequently,


$$
3\kappa(q_u)\equiv4\,\frac{3^{29}}u\pmod{3^{30}},
$$


with the factors $3$ in $u=3,9$ divided out before reduction. Explicitly,


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
\tag{2.26}
$$


The required coefficient precisions are exactly


$$
\boxed{3,\quad9,\quad3,\quad3,\quad27.}
\tag{2.27}
$$



Because $v_3(D)=v_3(t)=5$, the relevant finite binomial polynomials and reciprocal coefficients modulo $27$ have degrees in multiples of $27$. Thus $C_dp_i\bmod27$ has grade $i-1\pmod{27}$, while every $q_u\equiv13\pmod{27}$. Hence


$$
9v_T^Td_i\in3^{30}\quad\text{if }i\not\equiv14\pmod{27}.
\tag{2.28}
$$



**Verdict: PASS after the harmless $L\ge3$ repair.**

---

## 2.6 The whole stationary numerator

Using the physical LOW inverse $3^{-1}M_L$, the exact Schur expansion is


$$
\begin{aligned}
g_T^TE_c^{-1}G_c(W,x^Dp_i)
={}&27v_T^Tf_i+3\alpha_T^TM_L\alpha_i\\
&-9v_T^Td_i-27d_T^TM_Hf_i
+9d_T^TM_Hd_i.
\end{aligned}
\tag{2.29}
$$



The direct and double LOW terms have depths $51$ and $52$. The bare pairing is in $3^{30}$, and (2.7) pays the terminal-side mixed term.

Let


$$
N_i=-G_c(F[y^{\nu-1}],F[p_i]).
$$


Then


$$
\boxed{
\begin{aligned}
N_i\equiv{}&
3^{29}\bigl(\zeta_i-C_{1,i}-2C_{5,i}-C_{7,i}\bigr)\\
&-4\cdot3^{28}C_{3,i}
-4\cdot3^{27}C_{9,i}
\pmod{3^{30}}.
\end{aligned}}
\tag{2.30}
$$



This is a whole-numerator congruence. It does not license separate division of its individual displayed terms by $3^{29}$.

**Verdict: PASS.**

---

## 3. The actual original critical index

Put


$$
g=P/27,\qquad i_\star=\frac{g-1}{2}.
$$


The original window gives


$$
i_\star+1\le I,\qquad i_\star<I-1
$$


for sufficiently large admitted tuples. Moreover,


$$
i_\star\equiv13,\qquad i_\star+1\equiv14\pmod{27}.
$$



Write


$$
\chi=3g+u.
$$


Then


$$
\frac6{25}<\frac ug<\frac{87}{250},\qquad 2u<g,
$$




$$
v_3(u)=5,\qquad u/243\equiv1\pmod9,
$$


and


$$
J_D=3621g+u.
$$



### 3.1 The finite quotient range and carry lemma

For exactly


$$
0\le n\le3621,
$$


define


$$
t_n=b_{J_D-ng}.
\tag{3.1}
$$


These are coefficients of the actual finite $P_{d+1}$: its coefficient at $y^{ng}$ is $t_n$, and no $n<0$ or $n>3621$ is admitted.

Kummer’s carry rule counts carries in


$$
(D-1)+(J_D-ng).
$$


Modulo $g$, the summands are $2u-1$ and $u$.

The ternary digits of $u$ at positions $5,6$ are $1,0$. Since $u>6g/25$, there is a later nonzero digit below the $g$-boundary. At its first occurrence, adding $u$ to $2u-1$ produces a carry, whether the digit is $1$ or $2$. Therefore


$$
t_n\in3.
\tag{3.2}
$$



If $n\equiv4\pmod9$, then modulo $9g$,


$$
J_D-ng\equiv8g+u,\qquad
D-1\equiv6g+2u-1.
$$


Their sum exceeds $9g$, producing a further carry across that boundary, distinct from the lower carry. Thus


$$
\boxed{
t_n\in3\quad\text{for every }n,\qquad
t_n\in9\quad\text{if }n\equiv4\pmod9.
}
\tag{3.3}
$$



**Verdict: PASS.** The finite range is exact.

### 3.2 HIGH coefficient evaluation

At $i_\star$, the degree grade of


$$
(1-y)^DP_dp_{i_\star}\pmod3
$$


is $i_\star-1\equiv12\pmod{27}$, whereas $q_9\equiv13\pmod{27}$. Hence


$$
\zeta_{i_\star}=0.
$$



For $i_\star+1$, use


$$
yP_d=P_{d+1}-b_{J_D},\qquad b_{J_D}\in27.
$$


Only the coefficient-$1$ source survives modulo $3$. Since


$$
D+t+2P=7299g,
$$


the requested coefficient is


$$
\sum_{n=0}^{3621}
(-1)^{6547-n}\binom{7299}{6547-n}t_n
\pmod3.
$$


Every $t_n$ is in $3$, so


$$
\zeta_{i_\star+1}=0.
$$


Therefore


$$
\boxed{
v_T^Tf_{i_\star},\ v_T^Tf_{i_\star+1}\in3^{27}.
}
\tag{3.4}
$$


Equation (2.20) also evaluates the exceptional pairing at both indices: both its depth-$25$ and depth-$26$ contracted digits vanish.

### 3.3 The fixed $7299$ binomial band

For


$$
2926\le l\le6547,
$$


the needed statement is


$$
\boxed{
\begin{cases}
v_3\binom{7299}{l}\ge2,&9\nmid l,\\
v_3\binom{7299}{l}\ge1,&9\mid l.
\end{cases}}
\tag{3.5}
$$



If $3\nmid l$, this follows from


$$
\binom{7299}{l}
=\frac{7299}{l}\binom{7298}{l-1},
\qquad v_3(7299)=2.
$$



For the remaining cases, the finite congruence


$$
\begin{aligned}
(1-Z)^{7299}\equiv{}&
(1-Z^9)^{811}\\
&+3\cdot811(-Z^3+Z^6)(1-Z^9)^{810}
\pmod9
\end{aligned}
\tag{3.6}
$$


is sufficient.

Over $\mathbb F_3$,


$$
(1-Z)^{810}=(1-Z^{729})(1-Z^{81}),
$$


with support $\{0,81,729,810\}$, and


$$
(1-Z)^{811}=(1-Z)(1-Z^{81})(1-Z^{729}),
$$


with support


$$
\{0,1,81,82,729,730,810,811\}.
$$


These supports miss the respective ranges $325\le r\le727$ and $326\le r\le727$ arising from $l=9r+3,9r+6$ and $l=9r$. This proves (3.5).

**Verdict: PASS by a symbolic finite proof; no long scan is needed.**

### 3.4 All fourteen LOW contributions

Since $yC_d\equiv C_{d+1}\pmod{27}$, and the leading term $y^{d+1}$ lies above every requested coefficient range,


$$
C_{u,i_\star+1}
\equiv-[y^{q_u-i_\star}] (1-y)^DP_{d+1}\Omega_P(1-y)^t
\pmod{27}.
$$



Set


$$
K_u=\frac{2187u-1}{2},\qquad R_{u,b}=K_u-27b.
$$


The exact finite carry congruences


$$
(1-y)^{D+t+2P}\equiv(1-y^g)^{7299}\pmod{27},
$$




$$
(1-y)^{D+t}\equiv(1-y^g)^{7245}\pmod{27}
$$


hold because $7299$ and $7245$ are both divisible by $9$. Thus


$$
\boxed{
C_{u,i_\star+1}\equiv
-\sum_{(\Delta,b,c)\in\mathcal T}c
\sum_{n=0}^{3621}
(-1)^{R_{u,b}-n}
\binom{M_\Delta}{R_{u,b}-n}t_n
\pmod{27},
}
\tag{3.7}
$$


where $M_{2P}=7299$, $M_0=7245$, with out-of-range binomial coefficients zero.

This sum is evaluated, rather than merely named:

- For $u=1,5,7$, every term contains $t_n\in3$. Hence
  

$$
C_{1,i_\star+1},C_{5,i_\star+1},C_{7,i_\star+1}\in3.
$$



- For $u=3$, the coefficient-$1$ source has
  

$$
R_{3,122}=-14,
$$


  so it is identically absent. Every other source has a factor $3$, and every $t_n$ supplies another:
  

$$
C_{3,i_\star+1}\in9.
$$



- For $u=9$, the coefficient-$1$ source has
  

$$
R_{9,122}=6547.
$$


  Thus $l=6547-n$ lies in the band of (3.5). If $9\nmid l$, the binomial supplies two powers of $3$; if $9\mid l$, then $n\equiv4\pmod9$, and $t_n$ supplies two powers. Every term is in $27$.

- The coefficient-$3$ source has $b=41$, hence
  

$$
R_{9,41}=8734\equiv4\pmod9.
$$


  When $9\nmid l$, $\binom{7299}{l}$ has at least one factor $3$; when $9\mid l$, $t_n\in9$. With the source factor $3$, all terms are in $27$.

- Each of the twelve remaining source coefficients is in $9$, and every $t_n$ is in $3$. All twelve are therefore zero modulo $27$.

Consequently,


$$
\boxed{
C_{1,i_\star+1},C_{5,i_\star+1},C_{7,i_\star+1}\in3,\quad
C_{3,i_\star+1}\in9,\quad
C_{9,i_\star+1}\in27.
}
\tag{3.8}
$$



At $i_\star$, the LOW return already vanishes by its degree grade.

Substituting (3.4) and (3.8) into the whole numerator (2.30), and retaining the already paid terminal-side LOW, direct LOW, double LOW, and bare terms, gives


$$
N_{i_\star},N_{i_\star+1}\in3^{30}.
$$


Only now divide by $3^{29}$ in (1.9):


$$
\boxed{
\eta_{i_\star}=\eta_{i_\star+1}=0,\qquad h_{i_\star}=0.
}
\tag{3.9}
$$



### 3.5 Does this really contradict the alternating direction?

Yes.

Since


$$
t=3g-2u,\qquad 2<t/g<3,
$$


Lucas’s congruence gives


$$
c_g=(-1)^g\binom tg\equiv-2=1\pmod3.
$$


Also $243\mid t$, while


$$
g-1,\qquad g-I,\qquad g-I-1
$$


have residues $-1,2,1\pmod{243}$. Their coefficients vanish. Therefore the proposed identity requires


$$
h_{i_\star}=\varepsilon,
$$


contrary to (3.9).

In


$$
B_6=N^TC^{\rm mom}N-(e'h^T+he'^T),
\qquad
C^{\rm mom}_{ij}=c_{\kappa_2-i-j},
$$


the row $i_\star$ is not the last row. Thus the term involving $e'_{i_\star}$ is absent, and the other return term vanishes because $h_{i_\star}=0$. Direct evaluation gives


$$
\boxed{(B_6z_{\rm alt})_{i_\star}=1.}
\tag{3.10}
$$



This row calculation does not need an endpoint scalar to substitute for the interior source. In particular, the earlier free-module perturbation is not the proof of (3.10); the actual stationary calculation is.

Any correction $z=z_{\rm alt}+u$ must satisfy the explicit necessary row equation


$$
\boxed{
\sum_{j=0}^{I-1}
\bigl(
c_{\kappa_2-i_\star-j}
+2c_{\kappa_2-i_\star-j-1}
+c_{\kappa_2-i_\star-j-2}
\bigr)u_j=-1.
}
\tag{3.11}
$$


The remaining critical-coordinate and repaired-kernel evaluation is the separate A1 Turn 23 task and is not duplicated here.

---

## 4. Audit of Turn 21

## 4.1 LOW depth and the fully divided HIGH source

For LOW grading, the change between $x^u$ and $y^u$, $0\le u<D$, is integral unimodular and does not alter contractions with the actual finite inverse.

The LOW terms have


$$
N=H+t+\Delta,\qquad q=u+bP+i+\delta.
$$


The bound


$$
(t+\Delta)+q<402P
$$


excludes every indicator above $S+6$. The first five indicators number


$$
\min\{5,v_3(2q+1)\},
$$


and at most $S+1$ further indicators occur. The normalized LOW scale is $3^{S+31}$, so each term has depth at least


$$
30+v_3(c)+\delta-\min\{5,v_3(2q+1)\}.
$$


Hence


$$
\alpha_i\in3^{25}.
$$


Outside $q\equiv13\pmod{27}$, the depth is at least $28+v_3(c)+\delta$. This gives the stated three-digit LOW grade


$$
3^{-25}\widetilde\alpha_i
\in\mathscr L_{13-i}+3\mathscr L_{12-i}+27\mathbb Z_3^D.
$$



For the HIGH division by $9$, the largest rational degree is


$$
H+m+\deg p_I+1=\frac{3H-1}{2}-P.
$$


Thus the denominator $3H$ is not present in this source. The only potentially nonintegral normalized denominator is $H$. Its constant macro contribution is exactly absent, because


$$
r_H-s\ge\nu>\deg((\beta+3y)p_i).
$$


Every remaining coefficient of $(1-y)^H$ in that extraction is divisible by $3$. Therefore the full HIGH source is divisible by $9$ before reduction.

Using


$$
(1-y)^H\equiv(1-y^{H/9})^9\pmod{27},
$$


the denominator-$H$ contributions at $r_7,r_5,r_3,r_1$ are


$$
(3,6,1,3)\pmod9.
$$


The $H/3$ layer adds


$$
-1-\frac35+\frac17\equiv6\pmod9
$$


at $r_3$. The $H/9$ layer cancels in pairs:


$$
-\frac3a+\frac3{a+18}\equiv0\pmod9,
\qquad a=1,5,7.
$$


All four windows lie strictly inside the literal HIGH interval.

Therefore


$$
\boxed{
(f_i)_s\equiv
3[T_i]_{r_1-s}+7[T_i]_{r_3-s}
+6[T_i]_{r_5-s}+3[T_i]_{r_7-s}\pmod9,
}
\tag{4.1}
$$


where $T_i=(\beta+3y)p_i$.

The twelve $9$-weighted sources become invisible here only **after** the dangerous denominator-$H$ division has been paid.

**Verdict: PASS.**

---

## 4.2 Uniform bare, terminal, ordinary, and lower-mask payments

For terminal, ordinary, and quotient seeds on the safe grid, the beta top is


$$
N=H+D+t+\Delta=H+268P+\Pi+\Delta,
$$


with $v_3(N)=S-1$.

Writing $q=vB_\circ+q_{\rm lo}$, the actual bounds give


$$
N-H+q_{\rm lo}<540P<B_\circ/2.
$$


This excludes all indicators above $S+6$ on the original safe grid. It also gives


$$
N+q<\frac{3H}{2}<K_{\rm phys},
$$


so the beta evaluation does not extend the physical cutoff.

For a terminal seed,


$$
q_{\rm lo}=(134+b)P+q_0,\qquad
q_0=\chi+i-2+a+\delta.
$$


The original window gives


$$
\frac{2P}{9}<2q_0+1<\frac P3.
$$


Hence $v_3(2q+1)\le S-3$. The level-$S$ indicator is absent. For the two $\Delta=2P$ sources, the level-$S+1$ indicator is also absent. At normalized scale $3^{S+30}$, the corresponding depths are at least $28$; the twelve $\Delta=0$ sources have their extra two source powers of $3$.

Restoring the division by $9$ proves


$$
\boxed{
G_c(x^Dy^{\nu-1},x^Dp_i)\in3^{30}
\quad(0\le i\le I).
}
\tag{4.2}
$$


This is genuinely an all-interior proof, not an extrapolation from $\eta_0$.

For ordinary seeds, $q_0=i+a+\delta$ satisfies


$$
0<2q_0+1<P/9,
$$


and the same two excluded levels give normalized depth at least $28$.

For the literal lower HIGH mask $y^{d+a}$,


$$
q=(402+b)P+3\chi+i-1+a+\delta.
$$


The difference


$$
j_P-t>\frac P{250}+\frac52-a-\delta
$$


is positive. For the two $\Delta=2P$ sources, the relevant higher macro residues are exactly the source’s displayed rows for $524$ and $443$; their minimum is $2$. Thus all indicators at levels $S,\ldots,S+6$ are absent. The normalized lower-mask depth is at least $31$.

The finite lower masks are consequently paid as printed; none has been replaced by an unmasked continuation.

**Verdict: PASS for every stated terminal, ordinary, and lower-mask range.**

---

## 4.3 Quotient contractions and the noncritical mask

For the actual finite coefficient $b_j$ of $P_{d+a}$, put


$$
u=a+\delta,\qquad
\omega_i(u)=2\chi+2i+2u-1.
$$


The general weighted bound is


$$
24+u+v_3(c)+v_3(b_j).
$$



If $u\ge3$, this is already at least $27$. If $u=0,1,2$ and


$$
i\bmod27\notin\{12,13,14,15\},
$$


then $\lambda=v_3(\omega_i(u))\le2$.

- If $v_3(j)\ne\lambda$, the low-level indicators number at most $\lambda$, giving a much deeper term.
- If $v_3(j)=\lambda$, the exact identity
  

$$
b_j=\frac Dj\binom{D+j-1}{j-1}
$$


  gives $v_3(b_j)\ge5-\lambda$, and the depth is at least
  

$$
29+u+v_3(c)-\lambda\ge27.
$$



This covers the entire finite quotient, including its tail.

The exceptional-module intersection check is also correct. With


$$
\mathscr E=
\mathscr V_{25}+\mathscr V_{26}+\mathscr V_0
+3\mathscr V_1+9\mathscr V
$$


and


$$
f_i\in\mathscr V_{13-i}+3\mathscr V_{12-i}+9\mathscr V,
$$


a pairing modulo $9$ can occur only for


$$
i\bmod27\in\{12,13,14,15\}.
$$



The mixed LOW intersection tables in Turn 21 are arithmetically correct at the stated inherited finite matrix gradings. Those gradings must be actual finite-operator statements; they do not follow from source support alone. Independently, the explicit inverse certificate and literal remainder calculation in Section 2 validate the needed mixed-return conclusions without making any finer inverse-locality assumption.

Thus, on the stated noncritical mask, every term of the whole stationary numerator is in $3^{30}$, and


$$
\boxed{
\eta_i=0\quad\text{if }i\bmod27\notin\{12,13,14,15\},
}
\tag{4.3}
$$




$$
\boxed{
h_i=0\quad\text{if }i\bmod27\notin\{11,12,13,14,15\},
\qquad 0\le i<I.
}
\tag{4.4}
$$



**Verdict: PASS at exactly the stated mask.**

The theorem’s range includes $i=I$, since $I\equiv25\pmod{27}$. Accordingly, the audited uniform proof supplies a core endpoint conclusion independently of the earlier complementary-source proof. This does not retroactively certify every step of that earlier proof. In particular, the passed $\eta_0$ theorem alone was not used to infer $\eta_I$.

### Turn 21’s perturbation discussion

The literal coordinate


$$
s_\star=r_3-122P-i_\star
$$


is inside HIGH, has grade $0\pmod{243}$, and satisfies


$$
e_{s_\star}^T(f_{i_\star}+f_{i_\star+1})=1\pmod3.
$$


Thus the free perturbation $3^{26}e_{s_\star}$ really demonstrates that module containment alone does not fix the critical normalized residue.

**Verdict: PASS as a limitation of that proof method.** It was not an actual counterexample. Turn 22 supplies the actual counterexample by solving the relevant contracted source equation.

---

## 5. Audit of Turn 20

## 5.1 The whole two-digit amplitude source

Retain


$$
\mathsf A=-\frac{G_c(F_{\rm pref},F_{\rm pref})}{3^{26}},
\qquad
d_u=\frac{G_c(F_{\rm pref},\mathcal F[y^u])}{3^{28}}.
$$


The amplitude lifts and all prefix inputs lie in the admitted ordinary compression domain.

With


$$
T=(1-y)^{10Q},\qquad z=p+u+1,
$$


the compact degree bound is


$$
2\deg+1\le38Q+3+2R<39Q.
$$


The visible pole layers after normalization are $27Q,9Q,3Q,Q$.

The unit-$Q$ cancellation is valid: after omitting the higher-layer denominators, the terms


$$
\frac1{2s+9}-\frac1{2s+11}
-\frac1{2s+27}+\frac1{2s+29}
$$


cancel modulo $3$, with matching inclusion conditions. The weighted low term and the $3y$ term at this layer already have depth $2$.

The remaining full source is


$$
\begin{aligned}
D(z)={}&
\frac{T_{Q+z}+3T_{z-2Q}}9
+\frac65T_{7Q+z}
+\frac{26}{35}T_{4Q+z}\\
&+\frac37T_{Q+z}
+\frac1{11}T_{z-2Q}
\pmod9,
\end{aligned}
\tag{5.1}
$$


and


$$
(d_u)_p\equiv K_N\{\beta D(z)+3D(z+1)\}\pmod9.
\tag{5.2}
$$



To pay the division in (5.1), write


$$
A=(1-y)^Q,\qquad B=1-y^Q,\qquad A=B+3E.
$$


Then


$$
A^{10}\equiv AB^9+27B^9E\pmod{81}.
\tag{5.3}
$$


This follows directly from the ninth-power binomial expansion; every omitted term has valuation at least $4$.

For $z=sQ+l$, $0<l<Q$, the **whole numerator** in (5.1) is


$$
b_sA_l\pmod{81},
\qquad
(b_0,b_1,b_2,b_3,b_4)=(-9,36,-81,99,-18).
$$


Thus its division by $9$ is legitimate. The resulting source digits are


$$
D(sQ+l)\equiv
3e_s\bigl(-\mathbf1_{l=Q/3}+\mathbf1_{l=2Q/3}\bigr)\pmod9,
$$


where


$$
(e_0,e_1,e_2,e_3,e_4)=(2,1,2,2,1),
$$


and


$$
(D(Q),D(2Q),D(3Q),D(4Q))=(5,1,6,5)\pmod9.
$$



For the literal finite columns


$$
(E_M(u))_p=\mathbf1_{p+u+1=M},
$$


this gives


$$
d_u\equiv K_N(d_u^{[0]}+3d_u^{[1]})\pmod9,
$$




$$
d_u^{[0]}=2E_Q(u)+E_{2Q}(u)+2E_{4Q}(u),
$$




$$
\begin{aligned}
d_u^{[1]}={}&E_Q(u)+2E_{3Q}(u)+E_{4Q}(u)\\
&+\sum_{s=0}^4e_s
\{-E_{sQ+Q/3}(u)+E_{sQ+2Q/3}(u)\}\\
&+2E_{Q-1}(u)+E_{2Q-1}(u)+2E_{4Q-1}(u).
\end{aligned}
\tag{5.4}
$$


The last line is exactly the $3y$ correction.

The location $126P=14Q/3$ is outside the actual prefix for every admitted amplitude. Every other displayed active location, including the one-step shifts, is inside. The literal integer coefficients of


$$
H_i=(1-y)^\Pi y^{L+i},\qquad L=(P-1)/2,
$$


are contracted before reduction; their full support lies in $0\le u\le R$.

**Verdict: PASS.** The mod-$81$ payment is a whole-numerator calculation, and the source correction is complete.

---

## 5.2 All $P_{ui}$ zeros and the finite shifted prefix inverse

Let


$$
U=(1-y)^{N_0},
\qquad
(A_\Delta)_{pq}=U_{a_0+\Delta-p-q}.
$$


The exact finite inverse is


$$
(A_0^{-1})_{pq}=[y^{p+q-a_0}]U^{-1}.
$$


The normalized prefix inverse through its next digit is


$$
\mathsf A^{-1}\equiv K_N^{-1}
\left[
A_0^{-1}
+3A_0^{-1}(A_0-A_{-1}+A_{3Q})A_0^{-1}
\right]\pmod9.
\tag{5.5}
$$


The signs and both genuine finite shifts in this formula are correct.

Put


$$
r=P-1-u-i,\qquad t+1\le r\le P-1,
$$




$$
f=(1-y)^{t-25P}.
$$


The leading-source contraction is exactly


$$
S_{00}=8f_{12P+r}+4f_{39P+r}+4f_{93P+r}.
\tag{5.6}
$$



To evaluate its next digit, use


$$
(1-y)^{-25P}\equiv(1-y^\Pi)^{-75}\pmod9
$$


and


$$
(1-z)^{-75}\equiv
(1-z^3)^{-25}
+3(z-z^2)(1-z^3)^{-26}\pmod9.
$$


Over $\mathbb F_3$,


$$
(1-z)^{-26}=\frac{1-z}{1-z^{27}}.
$$


Its coefficients at $12,39,93$ are zero. Writing $r=e\Pi+d$, the case $e=0,d\le t$ is excluded by $r>t$; the cases $e=1,2$ are paid by the displayed next-digit identity. Thus every coefficient in (5.6) is zero modulo $9$.

For the first-order source corrections,


$$
f\equiv
\frac{(1-y)^t(1+y^P+y^{2P})}{1-y^Q}\pmod3.
$$


Its support in each $Q$-period lies only in


$$
[0,t],\quad[P,P+t],\quad[2P,2P+t].
$$


The actual source-correction residues


$$
12P+r,\quad21P+r,\quad3P+r,\quad12P+r-1
$$


miss all three bands. Hence both $S_{01}$ and $S_{10}$ vanish modulo $3$, including the $3y$ contribution.

For the inverse correction, the exact finite inverse images are


$$
Z_u^{[0]}=2y^{(Q+1)/2+u}(1-y)^b(1+y^Q+y^{3Q}),
$$




$$
Z_{H,i}^{[0]}=
2y^{14P+i}(1-y)^t(1+y^P+y^{2P})(1+y^Q+y^{3Q}).
\tag{5.7}
$$


The finite truncation is justified because precisely the translates $0,\ldots,j-1$ fit for each source location $jQ$; the next starts at $R_*+u>a_0$.

For $\Delta=0,-1,3Q$,


$$
\begin{aligned}
(Z_u^{[0]})^TA_\Delta Z_{H,i}^{[0]}
={}&[y^{93P+r+\Delta}]
(1-y^Q)(1+y^Q+y^{3Q})^2\\
&\hspace{18mm}\cdot(1+y^P+y^{2P})(1-y)^t.
\end{aligned}
\tag{5.8}
$$


The first part is a finite polynomial in $y^Q$; the remaining part has the same three support bands. Each extraction in (5.8) is zero.

Thus every term of the complete inverse expansion is paid, giving


$$
\boxed{
d_u^T\mathsf A^{-1}d_H{}_i\in9\mathbb Z_3,
\qquad
P_{ui}=0
}
\tag{5.9}
$$


for all original $u,i$.

**Verdict: PASS.** Neither an infinite inverse nor the already closed second-kernel quadratic was used in place of this calculation.

---

## 5.3 The original complement inverse and the whole leading $R_4$

The complement is exactly


$$
\mathcal C=\{0,\ldots,L-1\}\ \cup\ \{M,\ldots,R\},
\qquad M=L+\chi-1.
$$


The leading first-four block and complete cross are


$$
(\overline A_4)_{uv}
=-[y^{\kappa-u-v}](1-y)^b,
\qquad \kappa=3L,
$$




$$
(C_H)_{ui}
=-c_{2\Pi-1-u-i}+c_{\Pi-1-u-i}
-2\mathbf1_{u=R,\ i=I}.
\tag{5.10}
$$



Set $\rho=(\Pi-1)/2$. The original bounds give $0\le\rho+i<L$. Since


$$
b=5\Pi+t,
$$


the six macro coefficients of $(1-z)^5$ over $\mathbb F_3$ are


$$
(1,1,1,-1,-1,-1).
$$


Direct multiplication in the original finite matrix gives


$$
(\overline A_4e_{\rho+i})_u
=-c_{2\Pi-1-u-i}+c_{\Pi-1-u-i}.
$$



Let $v_\partial$ be the coefficient vector of


$$
V_\partial=y^M(1-y)^{2\chi}.
$$


Its full support lies in the upper complement because


$$
R-(M+2\chi)=L+2-4\chi>0.
$$


Using $b+2\chi=2P$ and $\kappa-M=R$,


$$
\overline A_4v_\partial
=-[y^{R-u}](1-y)^{2P}
=-e_R.
$$


Therefore


$$
\boxed{
\overline A_4^{-1}(C_H)_i
=e_{\rho+i}+2\mathbf1_{i=I}v_\partial.
}
\tag{5.11}
$$


The upper $3y$ corner is retained and has a nontrivial inverse image.

For every $i,j$,


$$
(C_H)_j^Te_{\rho+i}
=-c_{L-i-j}+c_{\rho-i-j}=0,
$$


because


$$
\rho-2I-t=\frac{P+7}{2}-4\chi>0.
$$


Also


$$
(C_H)_j^Tv_\partial=0.
$$


The two possible moment equalities are excluded by the original window, and the corner coefficient at $R$ is zero because $\deg V_\partial<R$.

Thus


$$
\boxed{R_4=C_H^T\overline A_4^{-1}C_H=0}
\tag{5.12}
$$


as an entire matrix over $\mathbb F_3$, not merely on the alternating scalar.

**Verdict: PASS.**

---

## 5.4 Physical-$6$ assembly and force scope

The first-four physical return has scale


$$
3^5\cdot3^{-4}\cdot3^5=3^6.
$$


Equation (5.12) removes its leading physical-$6$ core term. It does not evaluate its physical-$7$ digit.

The retained core assembly is


$$
C_6=C^{\rm mom}-(e_I\eta^T+\eta e_I^T).
$$


The endpoint-dependent force formulas in Turn 20 are correct conditional deductions:


$$
a_6=0,\qquad
w_6=\bar\gamma N^TC^{\rm mom}e_0,
$$




$$
B_6=N^TC^{\rm mom}N-(e'h^T+he'^T),
\qquad
\bar\gamma=(\sigma2^t)^{-1}.
$$


They require the stated endpoint hypotheses in their original derivation. The earlier complementary-endpoint proof is not upgraded merely by a favorable review label; the audited uniform Turn 21 theorem supplies the core endpoint conclusion by a separate route.

The scalar identities


$$
z_{\rm alt}^TB_6z_{\rm alt}=0,\qquad z_{\rm alt}^Tw_6=0
$$


are consistent with the actual row discrepancy. An isotropic vector need not be a kernel vector.

Finally, an allowed $3^{-1}$ solve still requires


$$
\overline B_6z_0=0,
$$


followed by


$$
\boxed{
\overline B_6z_1+
\overline{B_6\widehat z_0/3}
=\overline w_6.
}
\tag{5.13}
$$


This is a whole modulo-$9$ equation. Neither scalar compatibility nor the leading zero $R_4=0$ pays it.

---

## 6. A distinct new first-four next-digit calculation

The remaining critical-coordinate evaluation is assigned elsewhere. The following calculation instead advances the first-four next-digit problem.

### 6.1 Literal integer moment lifts

On the same original complement $\mathcal C$, define integer matrices


$$
A^\sharp_{uv}
=-[y^{\kappa-u-v}](1-y)^b,
$$




$$
C^\sharp_{ui}
=-c_{2\Pi-1-u-i}+c_{\Pi-1-u-i}
-2\mathbf1_{u=R,\ i=I},
\tag{6.1}
$$


where the $c_r$ in this section are literal integer coefficients.

Let


$$
X^\sharp_i=e_{\rho+i}+2\mathbf1_{i=I}v_\partial,
$$


again using the literal integer polynomial $V_\partial=y^M(1-y)^{2\chi}$.

These are not replacements for the actual whole first-four blocks. They are fixed integer representatives, on the actual finite coordinates, of the leading formulas already proved.

Since


$$
A^\sharp X^\sharp\equiv C^\sharp\pmod3,
$$


and $A^\sharp$ is a $3$-adic unit matrix, the exact residual identity gives


$$
\begin{aligned}
R_4^\sharp
&:=(C^\sharp)^T(A^\sharp)^{-1}C^\sharp\\
&\equiv
(C^\sharp)^TX^\sharp+(X^\sharp)^TC^\sharp
-(X^\sharp)^TA^\sharp X^\sharp
\pmod9.
\end{aligned}
\tag{6.2}
$$


The omitted term is


$$
(C^\sharp-A^\sharp X^\sharp)^T
(A^\sharp)^{-1}
(C^\sharp-A^\sharp X^\sharp)\in9.
$$



We now evaluate every term on the right.

### 6.2 The mixed terms vanish modulo $9$

The products


$$
(C^\sharp)_j^Te_{\rho+i}
=-c_{L-i-j}+c_{\rho-i-j}
$$


are exactly zero over the integers by the same support inequality used above.

For the boundary vector,


$$
(C^\sharp)_j^Tv_\partial
=-[y^{a_j}](1-y)^\Pi,
\qquad
a_j=2\Pi-1-j-M.
$$


The other moment extraction is negative, and the corner coefficient is absent.

The original window gives


$$
0<a_j<P/9.
$$


But


$$
(1-y)^\Pi\equiv(1-y^{P/9})^3\pmod9.
$$


There is no positive supported exponent strictly below $P/9$. Therefore


$$
\boxed{(C^\sharp)^TX^\sharp\equiv0\pmod9.}
\tag{6.3}
$$



### 6.3 The ordinary–ordinary quadratic term

Put


$$
a=P/9,\qquad \Pi=3a,\qquad P=9a.
$$


For the $e_{\rho+i},e_{\rho+j}$ entry, the extraction index is


$$
\kappa-2\rho-i-j=P+\rho-i-j.
$$


Write $r_0=\rho-i-j$. The original inequalities give


$$
t<r_0<\frac{3a}{2},\qquad t<a.
$$



Since $b=5\Pi+t$,


$$
(1-y)^b\equiv(1-y^a)^{15}(1-y)^t\pmod9.
$$


The coefficient at $9a+r_0$ has only one possible nonzero contribution:

- the macro index $9$ would require $c_{r_0}$, which is zero because $r_0>t$;
- the macro index $10$ gives $c_{r_0-a}$;
- all other macro indices are excluded by $t<a$.

Now


$$
\binom{15}{10}=3003\equiv6\pmod9,
$$


and


$$
r_0-a=\kappa_2-i-j.
$$


Including the minus sign in $A^\sharp$,


$$
\boxed{
e_{\rho+i}^TA^\sharp e_{\rho+j}
\equiv3c_{\kappa_2-i-j}\pmod9.
}
\tag{6.4}
$$



### 6.4 All boundary quadratic terms vanish modulo $9$

For an ordinary–boundary product,


$$
e_{\rho+i}^TA^\sharp v_\partial
=-[y^{R-\rho-i}](1-y)^{2P}.
$$


The original window gives


$$
2\Pi<R-\rho-i<3\Pi.
$$


Since


$$
(1-y)^{2P}\equiv(1-y^\Pi)^6\pmod9,
$$


there is no supported exponent in this open interval. Hence this product is zero modulo $9$.

For the boundary–boundary product,


$$
v_\partial^TA^\sharp v_\partial
=-[y^{L-2\chi+2}](1-y)^{2P+2\chi}.
$$


The extraction index lies strictly between $2\chi$ and $\Pi$. Modulo $9$, the $(1-y)^{2P}$ factor contributes only its constant term below $\Pi$, while $(1-y)^{2\chi}$ has smaller degree. Thus this product also vanishes modulo $9$.

Combining (6.2)–(6.4),


$$
\boxed{
R_4^\sharp\equiv-3C^{\rm mom}\pmod9.
}
\tag{6.5}
$$



This is a new evaluated finite coefficient theorem. It shows explicitly why the leading zero does not determine the next digit.

### 6.5 Exact remaining first-four premise

Let $\mathcal A_4,\mathcal C_4$ denote the **actual complete finite core** first-four normalized block and cross. Write


$$
\mathcal A_4=A^\sharp+3\Delta A,\qquad
\mathcal C_4=C^\sharp+3\Delta C.
$$


Then the same residual identity gives


$$
\boxed{
\frac{\mathcal C_4^T\mathcal A_4^{-1}\mathcal C_4}{3}
\equiv
-C^{\rm mom}
+\Delta C^TX^\sharp+(X^\sharp)^T\Delta C
-(X^\sharp)^T\Delta A X^\sharp
\pmod3.
}
\tag{6.6}
$$



The term $-C^{\rm mom}$ has been evaluated. The remaining correction has **not** been evaluated, and (6.6) is not asserted to close the actual first-four next digit.

A concrete follow-on obligation is:

> Evaluate the actual restrictions of $\Delta A$ and $\Delta C$ appearing in (6.6), including the boundary vector $v_\partial$, from the complete original source and finite prefix/$J$/complementary returns. Determine the resulting matrix coefficient law; do not identify the actual blocks with their integer moment representatives.

For clarity, these restrictions involve the entries at $\rho+i,\rho+j$, the pairings of $\Delta C_j$ with $v_\partial$, the pairings of $\Delta A e_{\rho+i}$ with $v_\partial$, and $v_\partial^T\Delta A v_\partial$. The boundary terms are not optional.

### 6.6 Required source and return precisions

To evaluate the actual first-four return modulo $9$, one needs


$$
\mathcal A_4\bmod9,\qquad \mathcal C_4\bmod9.
$$


Equivalently, the physical first-four block must be known modulo $3^6$, and its physical cross modulo $3^7$.

In the original raw normalization by $3^{26}$, this requires:



$$
\begin{array}{c|c}
\text{input}&\text{required whole precision}\\ \hline
\text{direct ordinary complement–complement pairing}&\bmod\,3^{32}\\
\text{direct ordinary complement–}H_i\text{ pairing}&\bmod\,3^{33}\\
\text{prefix complement–complement contraction}&d_C^T\mathsf A^{-1}d_C\bmod9\\
\text{prefix complement–}H_i\text{ contraction}&d_C^T\mathsf A^{-1}d_H\bmod27.
\end{array}
$$



A sufficient source precision for the last line is


$$
d_u,d_H\bmod27,\qquad \mathsf A\bmod27,
$$


requiring raw source pairings modulo $3^{31}$ and raw prefix pairings modulo $3^{29}$, respectively. The dominant source fraction divided by $9$ then requires its **whole numerator modulo $243$**, not merely the mod-$81$ numerator audited above.

For a literal $J$-return with inverse factor $3^{-1}$, its undivided block contraction must be known modulo $3^7$, and its undivided mixed contraction modulo $3^8$. For a complementary return with inverse factor $3^{-2}$, the corresponding requirements are modulo $3^8$ and $3^9$. These are whole-contraction requirements before the paid divisions.

This is a core first-four next-digit task. It does not pay actual/core transport for $Q_{\rm act}$, later physical-$5$ complementary or kernel-pivot returns, the whole $B_6\bmod9$, or source precision $34$.

---

## 7. Complete forcing, physical transport, and primitive error remain unchanged

The actual producer is still


$$
\boxed{Q_{\rm act}=Q_c+3^7\mathscr R.}
$$



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


Under their original existence and nonzero-denominator hypotheses,


$$
[x^a](3^7\mathscr R)
=-\frac{F_{\rm fac}}{a!}
\bigl((t_{\rm force})_a+\xi v_a\bigr),
\qquad 0\le a\le n-1,
$$




$$
\mathscr R(-1)=-\frac{\xi F_{\rm fac}^2}{3^7}.
$$



Neither these hypotheses nor the required actual inverse/source transport follow from a core cancellation.

The complete forcing identity remains


$$
\boxed{
J^T\boldsymbol\varepsilon+\omega
=
-\boldsymbol\varepsilon
-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
}
\tag{7.1}
$$


Both forcing terms remain.

The moment recurrence remains


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


is retained; the displayed pole occurs at $r=r_*+2$.

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
\tag{7.2}
$$


Neither the leading $C_H$-return nor the new integer moment-lift calculation evaluates this different force contraction.

### Actual contents and ALL-prime normalization

No actual integer column content is changed or evaluated by this audit. The columns are the complete original columns, with their actual contents.

The least simultaneous clearer is the actual $\ell_{\rm clr}$, not a convenient multiple or a power of $3$. Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the final **ALL-prime gcd**


$$
\boxed{G=\gcd(|A_\ell|,|B_\ell|).}
$$



For $B_\ell\ne0$, the actual primitive pair is


$$
\boxed{
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{G},
\qquad
q=\frac{|B_\ell|}{G}.
}
$$


The whole evaluated error is


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
G\det H_{\rm complete}.
}
\tag{7.3}
$$



An irrationality proof still requires, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\boxed{
\log G-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|\longrightarrow+\infty.
}
\tag{7.4}
$$


These conditions would make the nonzero whole errors tend to zero. If $e+\pi=a/b$ were rational, every nonzero integer linear error would have magnitude at least $1/b$.

No such same-index nonvanishing and decay theorem has been established here.

---

## 8. Consolidated PASS / REPAIR / OPEN ledger

### Turn 22

| Claim | Audit result |
|---|---|
| HIGH kernel modulo $9$, including extra $3H$ channel | **PASS** |
| Literal $Z_i$ HIGH support and shifted LOW depth $25$ | **PASS** |
| Actual $M_Hf_i\bmod9$ certificate | **PASS** |
| Uniform terminal-side mixed LOW payment | **PASS** |
| Primitive independence of finite bulk generators | **PASS** |
| First three weighted quotient coefficients and lower coefficients | **PASS** |
| Dual residual identity from the actual terminal equation | **PASS** |
| Both complete contractions (3.12)–(3.14) | **PASS**, including upper-side macro shifts |
| Exceptional pairing through depths $25,26$ | **PASS** |
| Literal LOW remainder and $(\beta+3y)$ recurrence | **PASS** |
| $\mathcal B(H,0)\equiv-4\pmod{27}$ stated for $L\ge2$ | **REPAIR:** require $L\ge3$; original domain satisfies it |
| All five pole weights and precisions | **PASS** |
| Whole stationary numerator before division | **PASS** |
| Exact $i_\star,i_\star+1$ range, finite $t_n$, carry lemma | **PASS** |
| Fixed $7299$ band and all fourteen LOW contributions | **PASS** |
| Actual $\eta_{i_\star}=\eta_{i_\star+1}=h_{i_\star}=0$ | **PASS** |
| Alternating leading-kernel claim | **DISPROVED for that candidate** |
| Full repaired kernel, rank, and leading force compatibility | **OPEN; separate A1 Turn 23 task** |

### Turn 21

| Claim | Audit result |
|---|---|
| Uniform LOW depth and source grades | **PASS** |
| HIGH division by $9$ before reduction | **PASS** |
| Four-window source law with both finite HIGH edges | **PASS** |
| All-interior bare cancellation | **PASS** |
| Terminal, ordinary, and literal lower-mask contractions | **PASS** |
| Entire finite quotient payment off the stated critical mask | **PASS** |
| Both mixed LOW payments on that mask | **PASS** at actual finite grading scope; independently supported by Turn 22’s explicit calculations |
| Noncritical $\eta$- and $h$-zero laws | **PASS** |
| Free-module perturbation as proof-method obstruction | **PASS only in that scope** |
| Perturbation as an actual solution counterexample | **Not claimed and not valid** |
| Proposed all-critical alternating identity | **Fails at the actual Turn 22 test index** |

### Turn 20 and the new first-four calculation

| Claim | Audit result |
|---|---|
| Two-digit amplitude source, all pole layers and $3y$ correction | **PASS** |
| Whole mod-$81$ numerator before division by $9$ | **PASS** |
| Leading-source next digit and both source corrections | **PASS** |
| Literal finite shifted prefix inverse correction | **PASS** |
| All $P_{ui}=0$ | **PASS** |
| Actual finite first-four inverse, including upper corner | **PASS** |
| Entire leading $R_4=0$ | **PASS** |
| Leading physical-$6$ assembly | **PASS at stated core scope** |
| Endpoint-dependent force deductions | **Conditional in their inherited derivation; not a substitute for endpoint proofs** |
| Actual whole first-four next digit | **OPEN** |
| New integer moment-lift law $R_4^\sharp\equiv-3C^{\rm mom}\pmod9$ | **NEW PROVED AUXILIARY RESULT** |
| Identifying that lift with the actual whole blocks | **Not justified; explicitly not done** |
| Whole $B_6\bmod9$, allowed $3^{-1}$ solve, source $34$ | **OPEN** |
| Actual physical-$7$ transport and $\lambda_4$ | **OPEN** |
| Contents, least clearer, ALL-prime $G$, primitive $q$, whole nonzero error | **UNEVALUATED / OPEN** |
| Rationality or irrationality of $e+\pi$ | **UNRESOLVED** |

---

## 9. Computation and final proof status

No tools or numerical execution were used. No new external calculation is indispensable to the audited conclusions or to the new first-four coefficient theorem.

In particular, this report does not request:

- an original matrix or inverse array;
- an original-length source solve;
- a rerun of the closed LOW, $729$, or full-fourteen scans;
- an optional carry receipt in place of a proof.

The bounded arithmetic needed in the arguments has been displayed symbolically. The $7299$ band follows from the two fixed characteristic-$3$ support factorizations, and the new first-four digit uses the explicit integer


$$
\binom{15}{10}=3003\equiv6\pmod9.
$$


A finite check of those constants would verify only those constants; it would not establish the uniform source, inverse, physical-transport, or primitive-error obligations.

The exact remaining first-four bottleneck is the evaluation of the **actual** correction terms in (6.6), at the source and return moduli in Section 6.6. The exact later local bottlenecks remain the repaired whole leading kernel and force system, the whole modulo-$9$ lift, actual physical-$7$ transport, and source precision $34$.

The global bottleneck remains more demanding: the actual contents and least simultaneous clearer, the ALL-prime final gcd and primitive denominator, and a nonzero whole evaluated error tending to zero at the same infinite original indices.

## Conclusion

The new actual original-index discrepancy in Turn 22 survives a different complete audit:


$$
\boxed{
\eta_{i_\star}=\eta_{i_\star+1}=0,\qquad
h_{i_\star}=0,\qquad
(B_6z_{\rm alt})_{i_\star}=1.
}
$$



The first-four leading calculations and Turn 21’s stated uniform payments also pass, with their finite boundaries, complete columns, source masks, and paid divisions intact.

A distinct next-digit calculation has now been proved:


$$
\boxed{R_4^\sharp\equiv-3C^{\rm mom}\pmod9}
$$


for the literal integer moment representatives on the original complement. Its actual-block correction is precisely identified but remains unpaid.

Accordingly, the alternating direction must be repaired or replaced; the whole construction is not thereby disproved. No local zero, local discrepancy, or leading scalar compatibility evaluates the actual primitive error.



$$
\boxed{\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$


