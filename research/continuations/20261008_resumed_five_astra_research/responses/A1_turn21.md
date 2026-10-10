> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Turn 21 — Interior source evaluation, uniform bare cancellation, and the remaining terminal jets

## Abstract

The global rationality or irrationality of $e+\pi$ is not decided here. Nor does this report prove that the proposed alternating vector is in the kernel of the actual leading $B_6$.

The interior problem can nevertheless be advanced by three source-specific results, proved below on the unchanged original index domain:

1. **The bare terminal pairing vanishes uniformly at the required precision:**
   

$$
\boxed{
   G_c(x^Dy^{\nu-1},x^Dp_i)\in3^{30}\mathbb Z_3
   \qquad(0\le i\le I),
   }
$$


   where $p_i=\Omega_P(1-y)^ty^i$. This is a new all-interior proof, not an extrapolation of the endpoint calculation.

2. **The complete HIGH source has an explicit four-window coefficient law modulo $9$.** Put
   

$$
T_i(y)=(\beta+3y)p_i(y),\qquad
   r_a=\frac{aH/9-1}{2}\quad(a=1,3,5,7).
$$


   Then, on the literal HIGH interval $d\le s\le m$,
   

$$
\boxed{
   f_H(i)_s
   \equiv
   3[T_i]_{r_1-s}
   +7[T_i]_{r_3-s}
   +6[T_i]_{r_5-s}
   +3[T_i]_{r_7-s}
   \pmod9.
   }
$$


   The proof pays the division by $9$, the potentially dangerous denominator-$H$ contribution, both HIGH boundaries, all fourteen $\Omega_P$ sources, and the $3y$ channel.

3. **A uniform portion of the actual interior vector is evaluated:**
   

$$
\boxed{
   \eta_i=0
   \quad\text{if}\quad
   i\bmod27\notin\{12,13,14,15\}.
   }
$$


   Consequently,
   

$$
\boxed{
   h_i=0
   \quad\text{if}\quad
   i\bmod27\notin\{11,12,13,14,15\},
   \qquad 0\le i<I.
   }
$$


   This uses the actual LOW source returns, not just the LOW term inside the HIGH Schur operator.

The remaining critical residue classes are not evaluated here. In particular, at the explicit original index


$$
i_\star=\frac{P/27-1}{2},
$$


the proposed directional identity requires $h_{i_\star}=\varepsilon$. An explicit coordinate of the inherited exceptional terminal module pairs nontrivially with this actual source. Thus the endpoint/module annihilator alone cannot establish that required value.

This is an obstruction to the proposed **proof method**, not a proof that the actual alternating candidate fails. The exact remaining local obligation is specified in Section 8.

---

## 1. Scope, dependencies, and proof status

The following results are reused at their stated scopes.

- The original finite unit statements for LOW and HIGH.
- The complete corrected-pairing compression through source precision $33$, only on its admitted ordinary polynomial domain.
- The A1 Turn 18 terminal-module theorem, including both finite HIGH masks and the actual Schur LOW feedback.
- The A1 Turn 13 complete prefix/terminal interface.
- The finite matrix gradings used in Turns 18–19.
- The Turn 20 mixed-prefix evaluation and the actual original-complement inverse certificate:
  

$$
P_{ui}=0,\qquad
  \overline A_4^{-1}(C_H)_i
  =
  e_{\rho+i}+2\mathbf1_{i=I}v_\partial,
  \qquad
  R_4=0.
$$



The supplied review statuses are retained:

- A1 Turn 18 and the A1 Turn 13 interface have DIFFERENT-passed.
- Turn 20's new first-four calculations have favorable parent review; their separate DIFFERENT audit remains pending.
- The new complete $\eta_0$ LOW-return lemma remains under the stated A4 Turn 24 audit.
- Turn 19's complementary-source proof remains under the stated A3 Turn 21 audit.
- The separate higher ternary block theorem has DIFFERENT-passed through A3 Turn 20, including its original $E33$ output modulo $3^{32}$. It does not supply actual physical inverse locality or source precision $34$.

The new results below have explicit proofs in this report. No independent audit status is claimed for them.

---

## 2. Original domain and complete finite objects

### 2.1 Unchanged admitted indices

All uniform assertions concern sufficiently large members of exactly


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
P=3^{h-32},\quad P_0=243P,\quad N_0=243r,\quad
D=P_0+N_0,
$$




$$
r\equiv2\pmod9,\qquad r\text{ odd},
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
\tag{2.1}
$$


There are no independent choices of $P,\chi$, or $I$.

Write


$$
S=h-32,\qquad P=3^S,\qquad H=3^{S+31},\qquad S\ge31,
$$




$$
\Pi=P/3,\qquad t=\Pi-2\chi,
$$




$$
k=3\chi-\Pi-1,\qquad I=k-1=3\chi-\Pi-2,
\qquad
\varepsilon=(-1)^{k-2}.
$$


The original arithmetic gives


$$
v_3(\chi)=v_3(D)=v_3(t)=5,
\qquad
\chi/243\equiv1\pmod9,
$$


and


$$
t+I=\chi-2,\qquad I\equiv25\pmod{27}.
\tag{2.2}
$$



We use


$$
c_d=[y^d](1-y)^t,
\qquad c_d=0\quad(d<0\text{ or }d>t),
$$


and


$$
\kappa_2=\frac{P/9-1}{2}.
$$



### 2.2 Literal spaces and physical terminal

Set $x=y-1$. The original spaces are


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
\qquad
d=D+\nu=402P+3\chi-1.
$$


In particular,


$$
m+\nu=r_H,\qquad r_H=\frac{H-1}{2}.
\tag{2.3}
$$



The physical HIGH terminal remains $Y_m$. The last middle input remains $y^{\nu-1}$. They are different objects.

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



### 2.3 Complete functional and corrected columns

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
\qquad \beta=D-H-71\equiv1\pmod9,
$$




$$
G_c(f,g)=\mathcal M(Q_cfg),\qquad W=[U\ Y],
\qquad E_c=G_c(W,W).
$$


Every corrected column below is the complete column


$$
\boxed{
F[p]=x^Dp-WE_c^{-1}G_c(W,x^Dp).
}
\tag{2.4}
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
\mathcal S_H=E_Y-3\mathcal X^TM_L\mathcal X,
\qquad M_H=\mathcal S_H^{-1}.
\tag{2.5}
$$


Thus the physical LOW inverse costs $3^{-1}$.

### 2.4 All fourteen sources and the complete interface

Retain


$$
\begin{aligned}
\Omega_P(y)={}&
(1-y)^{2P}(y^{122P}+3y^{41P})\\
&+9(1+y^P+y^{2P})
(2y^{14P}+2y^{41P}+2y^{95P}-y^{131P}).
\end{aligned}
\tag{2.6}
$$


For $0\le i\le I$, put


$$
p_i=\Omega_P(1-y)^ty^i.
$$



The fourteen terms are


$$
p_i=\sum_{(\Delta,b,c)\in\mathcal T}
c(1-y)^{t+\Delta}y^{bP+i},
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
\tag{2.7}
$$


For each term, both channels $\delta=0,1$ carry


$$
c\,\beta^{1-\delta}3^\delta.
\tag{2.8}
$$



The degree bound is uniform:


$$
\deg p_i\le\deg p_I=133P+\chi-2=\nu-P-1.
\tag{2.9}
$$


In particular, the $p_i$ are ordinary admitted polynomial inputs. No ordinary compression is applied to the terminal input $y^{\nu-1}$.

Let


$$
F_T=F[y^{\nu-1}],\qquad
a=\overline B_{\ell,\tau-1}\ne0.
$$


The inherited complete prefix/terminal interface is


$$
\boxed{
a\eta_i
=
-\frac{G_c(F_T,F[p_i])}{3^{29}}\pmod3.
}
\tag{2.10}
$$


Its linear consequence is the literal assigned source


$$
\boxed{
a h_i
=
-\frac{G_c(F_T,F[p_i(1+y)])}{3^{29}}\pmod3,
\qquad 0\le i<I.
}
\tag{2.11}
$$


No prefix or $J$-correction is removed from these formulas.

---

## 3. Uniform LOW source information and the explicit HIGH source law

Define


$$
g_T=G_c(W,x^Dy^{\nu-1})
=3\binom{\alpha_T}{\upsilon_T},
$$




$$
b_i=G_c(W,x^Dp_i)
=\binom{3\alpha_i}{9f_i},
\qquad f_i=f_H(i).
\tag{3.1}
$$



For LOW grading only, use the integral unimodular basis change from $x^u$ to $y^u$, $0\le u<D$. It leaves every contraction with the actual finite LOW inverse unchanged.

### 3.1 Uniform LOW depth and three-digit grading

Use the established evaluated beta ratio


$$
\mathcal B(N,q)=
\frac{4^N N!(N+q)!(2q)!}
{q!(2N+2q+1)!},
$$


with


$$
v_3\mathcal B(N,q)=
-\sum_{e\ge1}
\mathbf1_{\{N\bmod3^e\ge j_e(q)\}},
\qquad
j_e(q)=\left(\frac{3^e-1}{2}-q\right)\bmod3^e.
\tag{3.2}
$$



For the LOW source, the actual arguments are


$$
N=H+t+\Delta,\qquad q=u+bP+i+\delta,
\qquad 0\le u<D.
$$


The rational contribution to $\widetilde\alpha_i$ is


$$
-3^{h-1}
c\,\beta^{1-\delta}3^\delta\mathcal B(N,q).
\tag{3.3}
$$


Its factorial contribution lies in $3^{h-1}\mathbb Z_3$.

Since $i\le I$,


$$
(t+\Delta)+q
\le(268+b)P+3\chi+\Delta-3+\delta<402P.
\tag{3.4}
$$


Thus every indicator above level $S+6$ is absent. The first five indicators number


$$
\min\{5,v_3(2q+1)\},
$$


and there are at most $S+1$ further indicators. Each term of (3.3) therefore has valuation at least


$$
30+v_3(c)+\delta-\min\{5,v_3(2q+1)\}.
\tag{3.5}
$$



Consequently,


$$
\boxed{\alpha_i\in3^{25}\mathbb Z_3^D\qquad(0\le i\le I).}
\tag{3.6}
$$


If $q\not\equiv13\pmod{27}$, the lower bound in (3.5) is at least $28+v_3(c)+\delta$. Hence, in monomial LOW coordinates,


$$
\boxed{
3^{-25}\widetilde\alpha_i
\in
\mathscr L_{13-i}
+3\mathscr L_{12-i}
+27\mathbb Z_3^D.
}
\tag{3.7}
$$



This proof includes the $c=3$ source and all twelve sources with $v_3(c)=2$.

### 3.2 Why the new HIGH division by $9$ is legitimate

The largest rational-polynomial degree, at $Y_m$, is


$$
H+m+\deg p_I+1
=
\frac{3H-1}{2}-P.
\tag{3.8}
$$


Thus all odd denominators in the source are strictly below $3H$.

At denominator $H$, the potentially nonintegral normalized weight is $1/3$. But


$$
r_H-s\ge\nu>\deg((\beta+3y)p_i)
\qquad(d\le s\le m).
\tag{3.9}
$$


The coefficient from the constant macro term of $(1-y)^H$ is therefore exactly zero. Every other relevant coefficient of $(1-y)^H$ is divisible by $3$.

All remaining visible denominators have integral normalized weights. Thus


$$
\boxed{G_c(Y_s,x^Dp_i)\in9\mathbb Z_3}
\tag{3.10}
$$


for every original $s,i$.

Notice that (3.9) applies to the whole fourteen-term polynomial before any of its $9$-weighted terms is discarded.

### 3.3 The finite carry identities

For $H=3^{S+31}$,


$$
(1-y)^H\equiv(1-y^{H/9})^9\pmod{27},
\tag{3.11}
$$




$$
(1-y)^H\equiv(1-y^{H/3})^3\pmod9,
\tag{3.12}
$$




$$
(1-y)^H\equiv1-y^H\pmod3.
\tag{3.13}
$$



For example, (3.11) follows by starting with


$$
(1-y)^{H/9}\equiv1-y^{H/9}\pmod3
$$


and raising to the ninth power: if $A\equiv B\pmod3$, then $A^9\equiv B^9\pmod{27}$.

These are finite polynomial congruences.

### Theorem 3.1 — Complete four-window HIGH coefficient law

Let


$$
T_i=(\beta+3y)p_i,\qquad
r_a=\frac{aH/9-1}{2}\quad(a=1,3,5,7).
$$


Then


$$
\boxed{
(f_i)_s
\equiv
3[T_i]_{r_1-s}
+7[T_i]_{r_3-s}
+6[T_i]_{r_5-s}
+3[T_i]_{r_7-s}
\pmod9
}
\tag{3.14}
$$


for every $d\le s\le m$ and $0\le i\le I$. Coefficients outside a polynomial's literal support are zero.

#### Proof

Because $x^{A+D}=x^H=-(1-y)^H$, the rational part of $f_i$ is


$$
-3^{h-2}
\sum_v
\frac{[y^{v-s}](1-y)^H T_i}{2v+1}.
\tag{3.15}
$$



Only three denominator layers can survive modulo $9$:

1. $H$, with normalized weight $1/3$;
2. unit multiples of $H/3$, with unit normalized weight;
3. unit multiples of $H/9$, with normalized weight divisible by $3$.

Lower layers already carry $9$.

For the denominator $H$, (3.11) applies. The $j=0$ term is zero by (3.9). The terms $j=1,2,3,4$ have centers $r_7,r_5,r_3,r_1$, respectively. Their coefficients, including the minus sign in (3.15), are


$$
-\frac{(-1)^j\binom9j}{3}.
$$


Modulo $9$, these give


$$
3,\quad6,\quad1,\quad3
$$


at $r_7,r_5,r_3,r_1$.

For the $H/3$ layer, the unit denominators are $H/3,5H/3,7H/3$. By (3.12), the contributions at the one surviving center $r_3$ have total coefficient


$$
-1-\frac35+\frac17=-\frac{51}{35}\equiv6\pmod9.
\tag{3.16}
$$


The potential center $r_H$ is outside the actual HIGH source by (3.9); the other centers are outside the literal HIGH interval. Thus the $r_3$ coefficient becomes $1+6=7$.

For the $H/9$ layer, use (3.13). The only matching pairs are the unit denominators


$$
aH/9,\qquad(a+18)H/9,\qquad a=1,5,7.
$$


Their coefficients are


$$
-\frac3a+\frac3{a+18}\equiv0\pmod9.
\tag{3.17}
$$


Every other center lies outside the original HIGH interval.

All four remaining windows lie wholly inside that interval: their centers are between $H/18$ and $7H/18$, while their widths are at most $\deg T_i<\nu\ll H/18$. Thus neither HIGH boundary has been extended.

The factorial contribution is in $3^{h-2}$, hence is zero at this precision. This proves (3.14). ∎

An equivalent form retaining the $3y$ channel separately is


$$
\begin{aligned}
(f_i)_s\equiv{}&
\beta\bigl(
3[p_i]_{r_1-s}
+7[p_i]_{r_3-s}
+6[p_i]_{r_5-s}
+3[p_i]_{r_7-s}
\bigr)\\
&+3[p_i]_{r_3-s-1}
\pmod9.
\end{aligned}
\tag{3.18}
$$



The twelve $9$-weighted $\Omega_P$ terms are now invisible modulo $9$, **after** the dangerous division has been paid. They remain present in all deeper estimates below.

### 3.4 Leading source and finer support

Modulo $3$,


$$
p_i=(1+y^P+y^{2P})(1-y)^t y^{122P+i}.
$$


Therefore


$$
\boxed{
(f_i)_s
=
\sum_{b=122}^{124}c_{r_3-s-bP-i}
\quad\text{in }\mathbb F_3.
}
\tag{3.19}
$$



In particular,


$$
f_i\bmod3
\text{ is supported at }
s\equiv121-i\pmod{243}.
\tag{3.20}
$$


The full law modulo $9$ also gives


$$
f_i\in
\mathscr V^{(81)}_{40-i}
+3\mathscr V^{(81)}_{39-i}
+9\mathscr V.
\tag{3.21}
$$


For the later return calculations, the weaker consequence


$$
\boxed{
f_i\in\mathscr V_{13-i}+3\mathscr V_{12-i}+9\mathscr V
}
\tag{3.22}
$$


modulo $27$-grades is sufficient.

The finer source support does not, by itself, refine the inherited exceptional **inverse** module.

---

## 4. New uniform bare cancellation and bulk estimates

We now prove the all-interior bare statement. The same argument evaluates substantial parts of the terminal bulk module.

Retain the safe grid


$$
B_\circ=2187P,\qquad C_\circ=\frac{3^{24}-1}{2}.
$$


The terminal-module generators are the weighted HIGH projections of


$$
x^Dy^{vB_\circ+\nu-1+a},\quad
x^Dy^{vB_\circ}P_{d+a},\quad
x^Dy^{vB_\circ+a},
$$


where


$$
0\le v\le C_\circ,\qquad
0\le a\le27
$$


for the terminal family, and $0\le a\le26$ for the other two families.

The exact finite quotient is


$$
P_{d+a}=\sum_{j=0}^{\nu+a}
b_jy^{\nu+a-j},
\qquad
b_j=\binom{D+j-1}{j}.
\tag{4.1}
$$



### 4.1 A common high-indicator exclusion

For the interior terminal, quotient, and ordinary families, the beta top is


$$
N=H+D+t+\Delta=H+268P+\Pi+\Delta,
\qquad v_3(N)=S-1.
\tag{4.2}
$$



Writing $q=vB_\circ+q_{\rm lo}$, all the actual arguments below satisfy


$$
N-H+q_{\rm lo}<540P<B_\circ/2.
\tag{4.3}
$$


For $S+7\le e\le S+31$, the modulus is an odd multiple of $B_\circ$. Its relevant half-residue has distance from $q_{\rm lo}$ greater than $N-H$. At modulus $3H$,


$$
q\le\frac{H-B_\circ}{2}+q_{\rm lo}
$$


gives the same exclusion. Higher indicators are absent as well.

Thus only levels $1,\ldots,S+6$ can contribute.

The actual degree bound is


$$
N+q<
H+\frac{H-B_\circ}{2}+540P
<\frac{3H}{2}<K_{\rm phys}.
\tag{4.4}
$$


No beta evaluation extends the physical cutoff.

### 4.2 Terminal-type contractions

For a terminal-type seed,


$$
q=vB_\circ+(134+b)P+q_0,
\qquad q_0=\chi+i-2+a+\delta.
\tag{4.5}
$$


Uniformly on the admitted ranges,


$$
\frac{2P}{9}<2q_0+1<\frac P3.
\tag{4.6}
$$


The lower inequality uses $\chi>3P/25$; the upper uses


$$
\chi+i\le4\chi-\Pi-2<\frac P6-\frac P{250}-2
$$


and the bounded offsets $a+\delta\le28$.

There is no multiple of $P/9$ strictly between the two endpoints in (4.6). Hence


$$
v_3(2q+1)\le S-3.
\tag{4.7}
$$



At level $S$, the top residue is $\Pi$, whereas


$$
j_S(q)=\frac{P-1}{2}-q_0>\Pi.
\tag{4.8}
$$


That indicator is absent.

For the two $\Delta=2P$ sources, $134+b\equiv1\pmod3$, while


$$
N\bmod3P=\Pi.
$$


Consequently the level-$S+1$ indicator is also absent: its least half-residue is again the number in (4.8).

The normalized pairing with $f_i$ has scale $3^{S+30}$. For the two $\Delta=2P$ terms, at most


$$
(S-3)+5=S+2
$$


indicators remain, giving valuation at least $28$, before adding the source and channel valuations.

For each $\Delta=0$ term, the absence of level $S$ gives a bound of at least $27$; its coefficient supplies two additional powers of $3$.

Therefore every unweighted interior terminal seed has its whole contraction in $3^{28}$.

### Theorem 4.1 — Uniform bare cancellation

For every original $0\le i\le I$,


$$
\boxed{
G_c(x^Dy^{\nu-1},x^Dp_i)\in3^{30}\mathbb Z_3.
}
\tag{4.9}
$$



#### Proof

Take $v=0,a=0$ in (4.5), before HIGH projection. The preceding argument gives valuation at least $28$ after division by $9$. Restoring that factor gives $3^{30}$.

Every one of the fourteen source terms and both channels was included. The factorial part after division by $9$ lies in $3^{S+30}$. The physical cutoff was verified in (4.4). ∎

Thus the endpoint bare cancellation now has an independently derived uniform extension.

### 4.3 Ordinary-type contractions

For an ordinary seed,


$$
q=vB_\circ+bP+q_0,\qquad q_0=i+a+\delta.
$$


Here


$$
0<2q_0+1<P/9,
$$


so again $v_3(2q+1)\le S-3$.

The level-$S$ indicator is absent because


$$
(P-1)/2-q_0>\Pi.
$$


For the two $\Delta=2P$ sources, $b\equiv2\pmod3$; the level-$S+1$ half-residue is then


$$
\frac{5P-1}{2}-q_0>\Pi,
$$


so it too is absent.

The same counting proves


$$
\boxed{
\text{every unweighted ordinary bulk seed pairs with }f_i
\text{ in }3^{28}.
}
\tag{4.10}
$$



### 4.4 The literal lower HIGH mask

For a lower-edge monomial $y^{d+a}$,


$$
N=H+t+\Delta,
$$




$$
q=(402+b)P+q_E,\qquad q_E=3\chi+i-1+a+\delta.
\tag{4.11}
$$


Set


$$
j_P=\frac{P-1}{2}-q_E.
$$


The original subwindow gives


$$
j_P-t
=
\frac P6-\chi-i+\frac12-a-\delta
>
\frac P{250}+\frac52-a-\delta>0.
\tag{4.12}
$$



For $\Delta=0$, every indicator at level $S$ or above is absent because its half-residue is congruent to $j_P\pmod P$ and is therefore at least $j_P>t$.

For $\Delta=2P$, let


$$
J_a(B)=\left(\frac{3^a-1}{2}-B\right)\bmod3^a.
$$


The two actual values $B=402+b$ are $524$ and $443$, and


$$
\begin{array}{c|rrrrrr}
a&1&2&3&4&5&6\\ \hline
J_a(524)&2&2&2&2&83&569\\
J_a(443)&2&2&2&2&164&650.
\end{array}
\tag{4.13}
$$


Each is at least $2$. Thus the corresponding half-residue is at least


$$
2P+j_P>2P+t.
$$


All indicators at levels $S,\ldots,S+6$ are absent, and the higher ones are excluded by the same safe-grid bound.

There are at most $S-1$ indicators in total. Hence


$$
\boxed{
G_c(y^{d+a},x^Dp_i)/9\in3^{31}\mathbb Z_3
\qquad(0\le a\le27).
}
\tag{4.14}
$$



The literal lower masks


$$
\mathsf Q_{a,0}=3^ay^{d+a},\qquad
\mathsf O_{a,0}=0,
$$


and


$$
\mathsf T_{a,0}
=
3^{a-1}\sum_{b=0}^{a-1}
(-1)^{a-1-b}\binom D{a-1-b}y^{d+b}
\quad(a\ge1)
$$


therefore satisfy the required estimates. No masked polynomial has been replaced by an unmasked interior continuation.

### 4.5 Finite-quotient contractions

For a coefficient $b_j$ of $P_{d+a}$,


$$
q=vB_\circ+\nu+a-j+bP+i+\delta.
$$


Put


$$
u=a+\delta,\qquad
\omega_i(u)=2\chi+2i+2u-1.
\tag{4.15}
$$



Without any special residue assumption, there are at most $S+6$ indicators. Therefore each weighted quotient term has valuation at least


$$
24+u+v_3(c)+v_3(b_j).
\tag{4.16}
$$


In particular, every unweighted quotient contraction is in $3^{24}$.

Suppose now


$$
i\bmod27\notin\{12,13,14,15\}.
\tag{4.17}
$$


If $u\ge3$, (4.16) is already at least $27$.

If $u=0,1,2$, then


$$
\lambda=v_3(\omega_i(u))\le2,
$$


because the possible congruences $\omega_i(u)\equiv0\pmod{27}$ require $i\equiv14,13,12$, respectively.

If $v_3(j)\ne\lambda$, the first $S-1$ indicators number at most $\lambda$, and the term is much deeper than $3^{27}$.

If $v_3(j)=\lambda$, use the exact identity


$$
b_j=\frac Dj\binom{D+j-1}{j-1}.
$$


It gives


$$
v_3(b_j)\ge5-\lambda.
$$


Even allowing all $S+6$ indicators, the valuation is at least


$$
29+u+v_3(c)-\lambda\ge27.
\tag{4.18}
$$



This evaluates every coefficient of the actual finite quotient, without omitting its tail.

Combining the terminal, ordinary, quotient, and lower-mask estimates gives:

### Theorem 4.2 — Interior bulk annihilation away from four residue classes

For the unchanged Turn 18 weighted bulk module $\mathscr B$,


$$
\boxed{
\mathscr B^Tf_i\subseteq3^{27}\mathbb Z_3
\quad\text{if}\quad
i\bmod27\notin\{12,13,14,15\}.
}
\tag{4.19}
$$



---

## 5. Complete LOW/HIGH elimination and the evaluated interior coordinates

Set


$$
v_T=M_H\upsilon_T,\qquad
d_T=\mathcal X^TM_L\alpha_T,\qquad
d_i=\mathcal X^TM_L\alpha_i.
\tag{5.1}
$$



### 5.1 Exact Schur pairing

The exact finite block identity is


$$
\begin{aligned}
g_T^TE_c^{-1}b_i={}&
27v_T^Tf_i
+3\alpha_T^TM_L\alpha_i\\
&-9v_T^Td_i
-27d_T^TM_Hf_i
+9d_T^TM_Hd_i.
\end{aligned}
\tag{5.2}
$$


It follows by using the physical LOW inverse $3^{-1}M_L$ and the true Schur matrix (2.5).

Uniformly,


$$
\alpha_T,\alpha_i,d_T,d_i\in3^{25}.
$$


Thus


$$
3\alpha_T^TM_L\alpha_i\in3^{51},\qquad
9d_T^TM_Hd_i\in3^{52}.
\tag{5.3}
$$


The two mixed LOW terms still require their own payments.

### 5.2 Source-side mixed LOW term

The finite matrix gradings imply


$$
v_T\in
\mathscr V_{26}
+3\mathscr V_{25}
+3\mathscr V_0
+9\mathscr V_1
+27\mathscr V,
\tag{5.4}
$$


and, from (3.7),


$$
3^{-25}d_i
\in
\mathscr V_{13-i}
+3\mathscr V_{12-i}
+9\mathscr V_{11-i}
+27\mathscr V.
\tag{5.5}
$$



The possible intersections at total cost less than $3^3$ are exactly:



$$
\begin{array}{c|c}
\text{intersection}&\text{required }i\bmod27\\ \hline
26\text{ with }13-i,\ 12-i,\ 11-i&14,\ 13,\ 12\\
25\text{ with }13-i,\ 12-i&15,\ 14\\
0\text{ with }13-i,\ 12-i&13,\ 12\\
1\text{ with }13-i&12.
\end{array}
\tag{5.6}
$$



Therefore, under (4.17),


$$
\boxed{v_T^Td_i\in3^{28}\mathbb Z_3.}
\tag{5.7}
$$


Its multiplier $9$ in (5.2) places the whole term in $3^{30}$.

### 5.3 Terminal-side mixed LOW term

The terminal LOW source and actual LOW-return grading give


$$
3^{-25}d_T\in
\mathscr V_{15}+3\mathscr V_{14}+9\mathscr V.
\tag{5.8}
$$


From (3.22) and the actual HIGH inverse grading,


$$
M_Hf_i\in
\mathscr V_i+3\mathscr V_{i+1}+9\mathscr V.
\tag{5.9}
$$


A contribution modulo $9$ requires $i\equiv14$ or $15\pmod{27}$. Thus, under (4.17),


$$
\boxed{d_T^TM_Hf_i\in3^{27}\mathbb Z_3.}
\tag{5.10}
$$


Its multiplier $27$ again places the complete term in $3^{30}$.

These are source-return payments. They are separate from the LOW matrix return already present in $\mathcal S_H$.

### 5.4 Actual terminal-module containment

The passed Turn 18 theorem gives


$$
v_T\in\mathscr N,
\qquad
\mathscr N=\mathscr B+3^{25}\mathscr E+3^{27}\mathscr V,
$$


where


$$
\mathscr E=
\mathscr V_{25}+\mathscr V_{26}+\mathscr V_0
+3\mathscr V_1+9\mathscr V.
\tag{5.11}
$$



By (3.22), an element of $\mathscr E$ can pair nontrivially with $f_i$ modulo $9$ only when


$$
i\bmod27\in\{12,13,14,15\}.
$$


Thus under (4.17),


$$
\mathscr E^Tf_i\subseteq9\mathbb Z_3.
$$


Together with Theorem 4.2,


$$
\boxed{v_T^Tf_i\in3^{27}\mathbb Z_3.}
\tag{5.12}
$$



### Theorem 5.1 — Evaluated noncritical interior coordinates

For every original $0\le i\le I$,


$$
\boxed{
i\bmod27\notin\{12,13,14,15\}
\quad\Longrightarrow\quad
\eta_i=0.
}
\tag{5.13}
$$



#### Proof

The bare pairing is in $3^{30}$ by Theorem 4.1. Equations (5.3), (5.7), (5.10), and (5.12) place every term of the complete stationary return in $3^{30}$. Hence


$$
G_c(F_T,F[p_i])\in3^{30}.
$$


Divide the whole pairing by $3^{29}$ in the inherited interface (2.10). Since $a$ is a unit, $\eta_i=0$. ∎

Since $h_i=\eta_i+\eta_{i+1}$, we obtain


$$
\boxed{
h_i=0
\quad\text{if}\quad
i\bmod27\notin\{11,12,13,14,15\},
\qquad 0\le i<I.
}
\tag{5.14}
$$



This is an actual uniform evaluation, not a finite computation. It does not evaluate the remaining five residue classes of $h$.

---

## 6. The leading physical-$6$ matrix has no unknown first-four return

The original monomial complement remains


$$
\mathcal C=
\{0,\ldots,R\}\setminus
\{L,\ldots,L+\chi-2\},
\qquad L=\frac{P-1}{2}.
$$


The Turn 20 certificate is reused:


$$
\overline A_4^{-1}(C_H)_i
=
e_{\rho+i}+2\mathbf1_{i=I}v_\partial,
\qquad
\rho=\frac{\Pi-1}{2},
$$


where $v_\partial$ is the original-coordinate coefficient vector of


$$
y^{L+\chi-1}(1-y)^{2\chi}.
$$


It retains the upper $3y$ corner and proves


$$
R_4=0\pmod3.
$$



Accordingly,


$$
\boxed{
C_6=C^{\rm mom}-(e_I\eta^T+\eta e_I^T),
\qquad
C^{\rm mom}_{ij}=c_{\kappa_2-i-j}.
}
\tag{6.1}
$$



Let $N$ have columns $e_j+e_{j+1}$, $0\le j<I$, and let $e'=e_{I-1}$. At the stated endpoint conclusions $\eta_0=\eta_I=0$,


$$
\boxed{
B_6=N^TC^{\rm mom}N-(e'h^T+he'^T),
}
\tag{6.2}
$$




$$
\boxed{
(w_6)_i=\bar\gamma(c_{\kappa_2-i}+c_{\kappa_2-i-1}),
\qquad
\bar\gamma=(\sigma2^t)^{-1}.
}
\tag{6.3}
$$


Thus


$$
\begin{aligned}
(B_6)_{ij}={}&
c_{\kappa_2-i-j}
+2c_{\kappa_2-i-j-1}
+c_{\kappa_2-i-j-2}\\
&-\mathbf1_{i=I-1}h_j-h_i\mathbf1_{j=I-1}.
\end{aligned}
\tag{6.4}
$$



For


$$
z_{\rm alt}=(1,-1,\ldots,(-1)^{I-1})^T,
$$


one has


$$
Nz_{\rm alt}=e_0+\varepsilon e_I.
$$


The complete directional equation remains


$$
\boxed{
B_6z_{\rm alt}
=
N^TC^{\rm mom}(e_0+\varepsilon e_I)-\varepsilon h.
}
\tag{6.5}
$$



The new zeros in (5.14) are consistent with the proposed right-hand side: the proposed nonzero coefficient positions lie in residues $12,13,14,15\pmod{27}$. They do not prove equality on those residues.

---

## 7. An exact original-index obstruction to extending the endpoint annihilator

This section identifies a concrete missing source component. It does **not** assert that the actual alternating vector fails.

### 7.1 A mandatory nonzero test for the proposed identity

Set


$$
\boxed{i_\star=\frac{P/27-1}{2}.}
\tag{7.1}
$$


The original subwindow gives $0\le i_\star<I$ for all sufficiently large admitted tuples.

Since


$$
\kappa_2-i_\star=P/27,
$$


Lucas's binomial congruence gives


$$
c_{P/27}=1.
\tag{7.2}
$$


Indeed,


$$
2<\frac{t}{P/27}<3,
$$


so the ternary digit of $t$ at position $P/27$ is $2$, and


$$
(-1)^{P/27}\binom{t}{P/27}\equiv-2=1\pmod3.
$$



Also $243\mid t$, while


$$
P/27-1,\qquad P/27-I,\qquad P/27-I-1
$$


have residues $-1,2,1\pmod{243}$, respectively. Their $c$-coefficients are zero.

Therefore the proposed identity requires the definite value


$$
\boxed{h_{i_\star}=\varepsilon.}
\tag{7.3}
$$



This is a nontrivial original-index test, not an endpoint or scalar-zero test.

### 7.2 The exceptional module does not annihilate this source

Define the literal HIGH coordinate


$$
\boxed{s_\star=r_3-122P-i_\star.}
\tag{7.4}
$$


Because $r_3\sim H/6$ and all subtracted quantities are $O(P)$,


$$
d\le s_\star\le m
$$


on the original sufficiently large domain.

Moreover,


$$
s_\star\equiv0\pmod{243},
$$


so $e_{s_\star}\in\mathscr V_0\subseteq\mathscr E$.

The explicit leading source law (3.19) gives


$$
(f_{i_\star})_{s_\star}=1,\qquad
(f_{i_\star+1})_{s_\star}=0
\quad\text{in }\mathbb F_3.
$$


Hence


$$
\boxed{
e_{s_\star}^T(f_{i_\star}+f_{i_\star+1})=1
\quad\text{in }\mathbb F_3.
}
\tag{7.5}
$$



Thus


$$
\mathscr E^T(f_{i_\star}+f_{i_\star+1})
\not\subseteq9\mathbb Z_3.
\tag{7.6}
$$



This proves that the Turn 18 exceptional annihilator argument cannot simply be extended to the required interior direction.

### 7.3 Why the missing digit is mathematically consequential

The perturbation


$$
3^{26}e_{s_\star}
$$


belongs to $3^{25}\mathscr E$. Adding it to a vector satisfying only the inherited module containment and the known low-order terminal certificate preserves those pieces of information. It also preserves their endpoint annihilator consequences.

But its contribution to the HIGH return for $p_{i_\star}(1+y)$ is


$$
27\cdot3^{26}
e_{s_\star}^T(f_{i_\star}+f_{i_\star+1})
\equiv3^{29}\pmod{3^{30}}.
\tag{7.7}
$$


It therefore changes the normalized directional residue.

Such a perturbed vector is **not claimed to solve**
$\mathcal S_Hv=\upsilon_T$. Rather, (7.7) proves that the module and endpoint information alone do not determine the answer. The actual source equation must fix precisely this exceptional digit.

This is the exact obstruction exposed by the present derivation.

---

## 8. The remaining source-specific lemma

The bare part is now paid uniformly. The complete stationary return, however, must still be evaluated on the critical classes.

Let


$$
f_i^+=f_i+f_{i+1},\qquad
d_i^+=d_i+d_{i+1}.
$$


The deep direct and double LOW terms in (5.2) vanish modulo $3^{30}$. Thus the assigned source becomes the exact remaining congruence


$$
\boxed{
a h_i
=
\frac{
27v_T^Tf_i^+
-9v_T^Td_i^+
-27d_T^TM_Hf_i^+
}{3^{29}}
\pmod3.
}
\tag{8.1}
$$


The division is a division of the **whole numerator**. Individual displayed summands need not admit the same division separately.

The known terminal certificate


$$
v_T=V^{(0)}+27w_2,
\qquad
V^{(0)}=e_d+3z_0+9\widehat z_1
$$


allows one new simplification without loss:


$$
9(v_T-V^{(0)})^Td_i^+\in3^{30}.
$$


Hence


$$
\boxed{
a h_i
=
\frac{
27v_T^Tf_i^+
-9(V^{(0)})^Td_i^+
-27d_T^TM_Hf_i^+
}{3^{29}}
\pmod3.
}
\tag{8.2}
$$



The remaining information is now sharply localized:

- In the bulk module, all terminal and ordinary families have been paid at depth $28$.
- The literal lower HIGH masks have been paid at depth $31$.
- Quotient families with weight at least $3^3$ are automatically paid at depth $27$.
- Only the first three weighted quotient families and the two-digit exceptional terminal jets can remain in the HIGH contraction.
- The exceptional source values are supplied by the four-window law (3.14), rather than an original-length source table.
- The source-side LOW term needs the three digits of $3^{-25}d_i^+$.
- The terminal-side LOW term needs the two digits of $3^{-25}d_T$, $M_H\bmod9$, and $f_i^+\bmod9$.

A concrete follow-on lemma is therefore:

> **Critical interior return lemma.**  
> For the actual terminal solution $\mathcal S_Hv_T=\upsilon_T$, evaluate the remaining first-three quotient-family contractions and the actual two-digit exceptional contribution in the four windows $r_1,r_3,r_5,r_7$, together with the two mixed LOW terms in (8.2), for
> 

$$
> i\bmod27\in\{11,12,13,14,15\}.
>
$$


> Prove that their whole numerator is
> 

$$
> 3^{29}a\varepsilon
> \left(
> c_{\kappa_2-i}+c_{\kappa_2-i-1}
> +\varepsilon(c_{\kappa_2-I-i}+c_{\kappa_2-I-i-1})
> \right)
> \pmod{3^{30}},
>
$$


> or exhibit an actual original-index discrepancy.

This is more specific than the original all-$i$ obligation: the bare pairing, all noncritical coordinates, all terminal and ordinary bulk families, both lower-mask effects, and the full two-digit HIGH source have now been evaluated. Nevertheless, the critical return lemma itself remains open.

### 8.1 The alternative $\eta$-target is still conditional

Define


$$
r_i=\varepsilon c_{\kappa_2-i}+c_{\kappa_2-I-i}.
$$


If the desired $h$-identity were proved, then


$$
N^T(\eta-r)=0.
$$


Since $\ker N^T$ is the alternating vector, $\eta-r$ would be a scalar multiple of that vector. The endpoint moment zeros give $r_0=r_I=0$, and $\eta_0=0$ would then force that scalar to vanish.

Thus the endpoint information can remove the scalar freedom **after** the interior identity is proved. It cannot supply the missing critical return.

### 8.2 No rank or paid lift is inferred

Because the complete directional identity is not established, this report derives no leading $B_6$ rank or full kernel theorem.

Even if the alternating direction closes, the allowed equation


$$
B_6x=w_6,\qquad x\in3^{-1}\mathbb Z_3^{I}
$$


requires, on writing $z=3x=\widehat z_0+3z_1$,


$$
\overline B_6z_0=0,
$$


and then


$$
\boxed{
\overline B_6z_1+
\overline{B_6\widehat z_0/3}
=\overline w_6.
}
\tag{8.3}
$$


That is a whole modulo-$9$ equation. A leading kernel vector does not pay it.

---

## 9. Division and precision ledger

| Quantity | Required payment | Status here |
|---|---:|---|
| Complete $W$-projection | Physical LOW inverse $3^{-1}M_L$ | Retained exactly |
| Interior $\alpha_i$ | Raw source divided by $3$ | Uniform depth $25$ proved |
| $3^{-25}\alpha_i\bmod27$ | Raw LOW source through $3^{29}$ | Uniform support law proved |
| Interior $f_i$ | Raw HIGH source divided by $9$ | Integrality proved before reduction |
| $f_i\bmod9$ | Denominator-$H$ numerator modulo $27$ | Four-window law evaluated |
| Bare terminal pairing | Required modulo $3^{30}$ | Uniformly zero |
| Source-side LOW return | $9v_T^Td_i$ | Paid off the four critical $\eta$-classes |
| Terminal-side LOW return | $27d_T^TM_Hf_i$ | Paid off the critical classes |
| Terminal/ordinary bulk contractions | Normalized by $9$ | Uniform depth $28$ |
| Literal lower HIGH masks | Normalized by $9$ | Uniform depth $31$ |
| Weighted quotient bulk | Normalized by $9$ | Depth $27$ off critical classes; remaining low-weight cases open |
| Final $\eta_i,h_i$ | Whole numerator divided by $3^{29}$ | Evaluated only at the stated noncritical classes |
| Allowed $3^{-1}$ solve | Whole $B_6\bmod9$ | Still open |

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
\tag{9.1}
$$


The first-four returned operator being zero does not evaluate this different force contraction. No unit numerator or primitive saving is presumed.

---

## 10. Actual producer, complete forcing, and later physical scope

The actual producer remains


$$
\boxed{Q_{\rm act}=Q_c+3^7\mathscr R.}
\tag{10.1}
$$



Retain the original definitions, including their existence and denominator hypotheses:


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


The correction is still


$$
[x^a](3^7\mathscr R)
=
-\frac{F_{\rm fac}}{a!}
\bigl((t_{\rm force})_a+\xi v_a\bigr),
\qquad0\le a\le n-1,
$$




$$
\mathscr R(-1)=-\frac{\xi F_{\rm fac}^2}{3^7}.
\tag{10.2}
$$



The complete forcing/return identity remains


$$
\boxed{
J^T\boldsymbol\varepsilon+\omega
=
-\boldsymbol\varepsilon
-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
}
\tag{10.3}
$$


Both forcing terms remain.

The complete moment recurrence is


$$
\mu_{r+1}+\mu_r
=
\frac{3^h}{2r+1}
-\frac{3^h}{4}\bigl((2r+2)!+(2r)!\bigr),
\qquad0\le r\le2n-2.
\tag{10.4}
$$


The shifted label


$$
r_*=\frac{3^h-5}{2}
$$


is retained; the displayed denominator pole occurs at $r=r_*+2$.

Nothing in the present core calculation pays:

- actual/core transport at physical $7$;
- the physical-$5$ complementary and kernel-pivot returns;
- next digits of earlier returns, including the first-four return;
- higher endpoint adaptation;
- the stationary contribution at source precision $34$.

The passed higher ternary producer theorem does not replace these obligations.

---

## 11. Actual contents, least simultaneous clearer, primitive denominator, and whole error

No actual integer column content is evaluated here. All contents remain those of the complete original columns.

The least simultaneous clearer remains the actual $\ell_{\rm clr}$, not a chosen convenient multiple or a power of $3$. Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the final gcd over **all primes**


$$
\boxed{G=\gcd(|A_\ell|,|B_\ell|).}
\tag{11.1}
$$


For $B_\ell\ne0$, the actual primitive pair is


$$
\boxed{
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{G},
\qquad
q=\frac{|B_\ell|}{G}.
}
\tag{11.2}
$$



The whole evaluated error remains


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
G\det H_{\rm complete}.
}
\tag{11.3}
$$


When the determinant is nonzero,


$$
\boxed{
|q(e+\pi)-p|
=
\frac{\ell_{\rm clr}^{m+1}}G
|\det H_{\rm complete}|>0.
}
\tag{11.4}
$$



An irrationality proof still requires, at the **same infinite original indices**,


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
\tag{11.5}
$$


Then the nonzero whole errors would tend to zero, contradicting the lower bound $1/b$ for nonzero integer linear errors if $e+\pi=a/b$.

The new local source results prove none of these primitive-normalization, nonvanishing, or real-decay requirements.

---

## 12. Bounded exact arithmetic and final status

No tools or numerical execution were used. No new numerical execution is indispensable.

An optional independent check can be restricted to the **new four-window constants**:

**Fixed inputs**


$$
(-1)^j\binom9j,\quad 1\le j\le4,
$$


the rational numbers


$$
-1-\frac35+\frac17,
$$


and the three pairs


$$
-\frac3a+\frac3{a+18},
\qquad a=1,5,7.
$$



**Expected verifiable outputs**


$$
\left(
-\frac{(-1)^j\binom9j}{3}
\right)_{j=1}^4
=(3,6,1,3)\pmod9,
$$




$$
-1-\frac35+\frac17=6\pmod9,
$$




$$
-\frac3a+\frac3{a+18}=0\pmod9
\quad(a=1,5,7),
$$


and therefore the ordered window coefficients


$$
\boxed{(3,7,6,3)\quad\text{at }(r_1,r_3,r_5,r_7).}
$$



This check has fixed degree $9$ and denominators at most $25$. It is not an original-length source calculation, vector solve, or rerun of any closed LOW or $729$-position calculation. It would verify only these constants, not the uniform theorems or the unresolved critical return.

### Consolidated status

| Item | Status |
|---|---|
| Whole leading $R_4$ | Reused as zero; no unknown $R_4$ left |
| Uniform bare terminal pairing | Newly proved zero modulo $3^{30}$ |
| Complete interior HIGH source modulo $9$ | Newly evaluated by four-window coefficient law |
| Terminal and ordinary bulk families | Newly paid uniformly at depth $28$ |
| Literal lower HIGH masks | Newly paid uniformly at depth $31$ |
| Complete LOW source information | Uniform depth and three-digit grading proved |
| Noncritical $\eta_i$ | Newly evaluated as zero |
| Noncritical $h_i$ | Newly evaluated as zero |
| Critical interior terminal return | Open |
| Actual alternating kernel membership | Not proved or disproved |
| Leading $B_6$ rank/kernel and force compatibility | Not inferred |
| Whole allowed modulo-$9$ lift | Open |
| Actual physical $7$/source $34$ | Open |
| Actual contents, least clearer, all-prime $G$, primitive $q$ | Unevaluated |
| Same-index nonzero whole error and decay | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

---

## Conclusion

The new proved results are


$$
\boxed{
G_c(x^Dy^{\nu-1},x^Dp_i)\in3^{30}
\quad(0\le i\le I),
}
$$


the complete four-window HIGH source law


$$
\boxed{
(f_i)_s
\equiv
3[T_i]_{r_1-s}+7[T_i]_{r_3-s}
+6[T_i]_{r_5-s}+3[T_i]_{r_7-s}
\pmod9,
}
$$


and the actual uniform zero law


$$
\boxed{
\eta_i=0\ \text{off } \{12,13,14,15\}\pmod{27},
\qquad
h_i=0\ \text{off } \{11,12,13,14,15\}\pmod{27}.
}
$$



The primary all-interior defect is **not fully evaluated**. Its remaining obstruction is not an unknown first-four return and not a missing endpoint scalar. It is the actual critical terminal jet, together with its complete mixed LOW source payments.

At the explicit original index


$$
i_\star=(P/27-1)/2,
$$


the desired equation requires $h_{i_\star}=\varepsilon$, while the inherited exceptional module contains a literal HIGH coordinate that pairs to $1$ with that source. The actual source equation must determine its depth-$26$ coefficient; the endpoint/module information does not.

No original-size numerical solve is proposed to bypass that obligation. The concrete next task is the critical interior return lemma of Section 8, followed—only if it closes—by the whole modulo-$9$ directional lift.



$$
\boxed{\text{No unconditional rationality or irrationality proof for }e+\pi\text{ follows.}}
$$


