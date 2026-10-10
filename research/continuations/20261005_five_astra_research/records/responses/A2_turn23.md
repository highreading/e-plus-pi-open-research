> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 — explicit $J_{29}$-kernel and a single universal low-contraction table

## Status and scope

The formal $J_{29}$-construction can be evaluated substantially further than turn22 did.

1. **The complete Newton vector $h_B\bmod29$ is given below.** Its reconstructed Laurent polynomial has only the four powers
   

$$
0,\ 1,\ 29,\ 30.
$$


   The contact correction in this formal construction is zero for a valuation reason, not by analogy with the leading column.

2. **The entire $J_{29}$-obstruction reduces to one new scalar**, independent of $d$:
   

$$
\boxed{\Gamma _1(d)=8\zeta\,\mathcal L_d\bigl((3-J)^2\bigr).}
$$


   Here $\zeta$ is an explicitly defined contraction on only $3036$ low coordinates. In particular,
   

$$
\boxed{\Gamma _1(0)=7\zeta.}
$$


   Thus $\Gamma _1$ vanishes identically if and only if this one scalar vanishes. The supplied $\kappa$- and $g$-tables do not, by themselves, determine $\zeta$.

3. **The $R_C$-calculation needs neither 25 reconstructions nor interpolation.** One low-coordinate pass produces a universal table consisting of
   

$$
\boxed{9\text{ residues modulo }29^2
          \quad+\quad18\text{ residues modulo }29.}
$$


   Explicit formulas below reconstruct the ordinary two-variable polynomial $R_C(d,J)$ from that table. Its degree is at most seven. Ordinary derivatives are retained.

I do **not** claim that the new scalar or the universal table has been numerically evaluated here. Consequently this report does not prove third-depth alignment.

### Source and search gate

I checked the supplied bounded archive for the relevant constructions, finite boundaries, contact formulas, off-central recurrence, and finite receipts. No external search facility is available in this interface, so I cannot certify a fresh primary-literature search. The reductions below use directly proved factorial, contiguous-binomial, and finite-polynomial identities; no global novelty claim is made.

The finite receipts $\kappa=(11,18)$, $g=(26,3)$, and support size $9108$ are reused as **supplied finite arithmetic inputs**, not independently recomputed results.

---

## 1. Domain and retained third-defect interface

Keep the original domain


$$
p=29,\qquad b=3^a,\qquad n=2001b,\qquad
a\ge1,\quad a\equiv432827\pmod{682892}.
$$


Coordinates are $0\le j\le b$, and every contact inverse has the original range $0\le i,j<b$.

Write


$$
L=p^4,\quad b_*=687936,\quad b=b_*+Lh,\quad
n=191110+LN,
$$




$$
N=3+pA,\qquad h=pH+d.
$$


The present third-defect locus is


$$
0\le d\le24,\qquad T=0,\qquad D_1=0.
$$



Use the actual falling metric


$$
\omega_j=j!\binom{n+2}{j},\qquad
\Omega=\operatorname{diag}(\omega_j^2),
$$


and the already weighted columns


$$
P=Z_w/p^2,\qquad Q=Y/p^3,\qquad
D=P^TP,\quad M=P^TQ.
$$



The retained reduction from turn22 is


$$
\frac{M-(6C_n)^{-1}D}{p^2}
=
U\bigl(C_n\Gamma _0(d)+J_{29}\Gamma _1(d)\bigr)\pmod p,
\tag{1.1}
$$


where


$$
\Gamma _0(d)=\mathcal L_d(R_C),\qquad
\Gamma _1(d)=\mathcal L_d(R_{29}).
$$


For an ordinary polynomial $V(J)$,


$$
\mathcal L_d(V)=
\sum_{\mathrm{adm}\ t}w_t\bigl(V'(t)+2r_tV(t)\bigr)
-\frac{\beta(d)}{f(d)}
 \sum_{\mathrm{adm}\ t}w_tV(t),
\tag{1.2}
$$


with


$$
0\le t\le3,\quad 0\le v=d-t\le22,
$$




$$
w_t=\binom3t^2\binom{v+6}{6}^2,\qquad
r_t=H_{3-t}-H_t+H_v-H_{v+6}.
$$


All quantities in (1.2) are in $\mathbb F_{29}$.

Put


$$
\ell_0=d+7-J,\qquad \ell_1=3-J.
$$


The known polynomial


$$
K_d=11\ell_0^2+18\ell_1^2
=11(d+4)(d+10-2J)
\tag{1.3}
$$


satisfies


$$
\mathcal L_d(K_d)=0.
\tag{1.4}
$$



No quotient modulo $J^{29}-J$ will be used.

---

# Part I. Complete evaluation of $h_B$

## 2. The contact operator contributes zero to $h_B\bmod29$

In the formal construction defining $h_B$, take


$$
J_0=0,\quad J_{29}=1,\quad
J_t=p\,b_t\quad(1\le t\le28),
$$


where


$$
b_t=\frac{8(20^t-8^t)}{12t}\pmod{29},
\tag{2.1}
$$


and take the remaining relevant formal moments to be zero.

The initial forcing polynomial is


$$
g_B(X)=
\sum_{i=0}^{57}(-1)^i
 \frac{(n+i)!}{n!}
 \left(\sum_{t=0}^i\binom itJ_t\right)\binom Xi
 \pmod{p^2}.
\tag{2.2}
$$


Every coefficient of $g_B$ is divisible by $p$.

The actual contact operator


$$
\mathscr V_{29}=\sum_{s=1}^{29}d_s\mathscr L_{s,b}
$$


has integral Newton coefficients and is divisible by $p$. Consequently


$$
\mathscr V_{29}g_B\equiv0\pmod{p^2}.
$$


Thus the **complete** inverse correction gives


$$
\boxed{h_B=g_B/p\pmod p.}
\tag{2.3}
$$



This conclusion uses the contact operator, including its finite boundary. It does not discard it without checking its action.

---

## 3. Complete Newton coefficient vector

Write


$$
h_B(X)=\sum_{i=0}^{57}\eta_i\binom Xi.
$$



For $0\le i\le28$,


$$
\eta_i=(-1)^ii!\sum_{t=1}^i\binom it b_t.
\tag{3.1}
$$


For $i=29+r$, $0\le r\le28$, the only surviving moment is $J_{29}$. Since $n/p\equiv7$,


$$
\frac{(n+29+r)!}{p\,n!}\equiv-8r!\pmod p,
$$


and hence


$$
\boxed{\eta_{29+r}=8(-1)^rr!.}
\tag{3.2}
$$



The complete vector is therefore:



$$
\boxed{
\begin{aligned}
(\eta_0,\ldots,\eta_{28})={}&
(0,21,24,7,1,14,24,1,21,9,13,9,8,14,10,\\
&\qquad3,10,1,4,16,28,28,20,26,14,16,4,0,0),
\end{aligned}}
\tag{3.3}
$$





$$
\boxed{
\begin{aligned}
(\eta_{29},\ldots,\eta_{57})={}&
(8,21,16,10,18,26,18,19,22,5,8,28,12,18,9,\\
&\qquad10,14,23,21,7,5,11,19,27,19,18,25,21,21).
\end{aligned}}
\tag{3.4}
$$



All higher Newton coefficients are zero modulo $29$.

### A short independent check on the first block

Set


$$
\lambda_i=\eta_i+i\eta_{i-1}\quad(1\le i\le28).
$$


The binomial-transform identity


$$
\sum_{t=1}^i\binom it\frac{a^t}{t}
-
\sum_{t=1}^{i-1}\binom{i-1}t\frac{a^t}{t}
=\frac{(1+a)^i-1}{i}
$$


gives


$$
\boxed{\lambda_i=20(i-1)!(8^i-20^i).}
\tag{3.5}
$$


Numerically,


$$
(\lambda_1,\ldots,\lambda_{28})
=
(21,8,21,0,19,21,24,0,24,16,7,0,2,3,
8,0,26,22,5,0,7,27,22,0,18,14,21,0).
\tag{3.6}
$$


Equations (3.2), (3.5), and $\eta_0=0$ reproduce the entire vector.

---

## 4. Complete reconstructed Laurent polynomial

Let


$$
h_0(X)=\sum_{i=0}^{28}(-1)^ii!\binom Xi.
$$


The reconstruction coefficients


$$
a_t=\binom{2n+t-1}{t}
$$


satisfy, for $0\le t\le57$,


$$
a_0=1,\qquad a_{29}=14,\qquad
a_t=0\quad(t\ne0,29)\pmod p.
$$


Moreover,


$$
\sum_{i=29}^{57}\eta_i\binom X{i-29}=8h_0(X).
$$



It follows directly from the complete reconstruction formula that


$$
\boxed{
\begin{aligned}
\mathcal R_{h_B}(j,r)
={}&j h_B(j-1)\\
&+r\bigl(h_B(j)+j h_B(j-1)\bigr)\\
&+25r^{29}j h_0(j-1)\\
&+25r^{30}.
\end{aligned}}
\tag{4.1}
$$


The last coefficient uses the coefficientwise Newton congruence


$$
h_0(j)+jh_0(j-1)\equiv1\pmod p.
$$



Thus every Laurent coefficient has been specified: only $q=0,1,29,30$ occur.

For additional implementation clarity,


$$
h_B(j)+jh_B(j-1)
=
\sum_{i=1}^{28}\lambda_i\binom ji
+8\binom j{29}\pmod p.
\tag{4.2}
$$


In particular, (4.1) is not a four-point interpolation of a coordinate function.

### Endpoint

There is no exterior forcing for this formal $P$-column. At $j=b$, all positive powers in (4.1) have invalid lower binomial index. The $q=0$ term is multiplied by $W_b\in p^3\mathbb Z_p$, so its contribution after division by $p^2$ is zero modulo $p$.

The endpoint has therefore been retained and evaluated.

---

# Part II. The entire $J_{29}$-contraction reduces to one scalar

## 5. Elimination of two Laurent powers and a contiguous reduction

Write


$$
B_q(j)=\binom{2n+b-j-1}{b-j-q}.
$$


Besides the established $q=0$ bound, the same digit-zero argument gives


$$
W_jB_{29}(j)\in p^3\mathbb Z_p.
\tag{5.1}
$$


Indeed, if the weight has no digit-zero borrow, then $j_0\le2$; the complementary index $2n+28$ has digit $28$, forcing a digit-zero carry in the second binomial. Digits $1$ and $3$ supply the other two factors.

Hence the $q=0,29$ terms of (4.1) disappear from the normalized $B$-column modulo $p$.

For $j\le b-1$, the exact contiguous identity is


$$
B_{30}(j)
=
B_1(j)\,
\frac{(b-j-1)_{\underline{29}}}{(2n)_{29}}.
\tag{5.2}
$$


The denominator has valuation exactly one, and the numerator is always divisible by $p$. Thus the ratio is integral. It also correctly gives zero when $b-j-1<29$.

On the surviving base support, $j_0\le2$, and


$$
\frac{(b-j-1)_{\underline{29}}}{(2n)_{29}}
\equiv\frac{28-j_1}{14}\pmod p.
\tag{5.3}
$$



At $j_0=0,1,2$, the coefficient of $r$ in (4.1) is respectively


$$
8j_1,\qquad21+8j_1,\qquad21+8j_1.
$$


Combining this with $25/14=8$ gives the exact normalized multiplier


$$
\boxed{\theta(0)=21,\qquad\theta(1)=\theta(2)=13.}
\tag{5.4}
$$



Consequently the natural $B$-multiplier is


$$
\boxed{
B_x(J)=
\begin{cases}
\theta(x_0)c(x)\ell_{e(x)}(J),&x\in\mathcal X,\\
0,&x\notin\mathcal X,
\end{cases}}
\tag{5.5}
$$


where $\mathcal X$ is the established $9108$-element low support.

This proves that no new support or omitted Laurent contraction enters $R_{29}$.

---

## 6. Triple structure of the low support

The support is a union of triples


$$
x=29y,\quad29y+1,\quad29y+2.
$$


Within each triple:

* the higher low digits and the shape $e$ are unchanged;
* the low units satisfy
  

$$
c(29y+a)=\binom2a\,c(29y),\qquad a=0,1,2.
  \tag{6.1}
$$



This follows by stripping the first factorial level: both base binomials have no digit-zero carry, and all remaining factorial arguments are identical across the triple. The shape thresholds do not split any such triple.

Therefore there are $3036$ triples, and


$$
\sum_{\substack{x\in\mathcal X\\e(x)=e\\x_0=0}}c(x)^2
=\frac{\kappa_e}{6}.
\tag{6.2}
$$


Using $21+13(4+1)=28=-1$,


$$
\sum_{\substack{x\in\mathcal X\\e(x)=e}}
\theta(x_0)c(x)^2
=-\frac{\kappa_e}{6}=24\kappa_e.
\tag{6.3}
$$



The corresponding mixed contraction is not fixed by (6.1), because no triple formula for $\xi(x)$ has yet been proved.

Define the two fixed constants


$$
\boxed{
\zeta_e=
\sum_{\substack{x\in\mathcal X\\e(x)=e\\x_0=0}}
c(x)\xi(x)\pmod{29},
\qquad
\zeta=\zeta_0+\zeta_1.
}
\tag{6.4}
$$


Then, using the supplied $g_e=\kappa_e/6$,


$$
\begin{aligned}
R_{29}
&=\sum_e
\left(13g_e+8\zeta_e-\frac13\,24\kappa_e\right)\ell_e^2\\
&=\boxed{(8\zeta_0-11)\ell_0^2+
         (8\zeta_1-18)\ell_1^2.}
\end{aligned}
\tag{6.5}
$$



Since $18=-11$,


$$
\boxed{
R_{29}
=
\left(\frac{8\zeta_0}{11}-1\right)K_d
+8\zeta\,\ell_1^2.
}
\tag{6.6}
$$


Thus


$$
\boxed{\Gamma _1(d)=8\zeta\,\mathcal L_d(\ell_1^2).}
\tag{6.7}
$$



For $d\le24$, the two squares $\ell_0^2,\ell_1^2$ are linearly independent. Hence


$$
\boxed{R_{29}\in\operatorname{span}K_d\iff\zeta=0.}
\tag{6.8}
$$



### The first exact obstruction

At $d=0$, only $t=0$ is admissible. Directly,


$$
r_0=25,\qquad f(0)=5,\qquad\beta(0)=17,
$$


and


$$
\mathcal L_0((3-J)^2)=19.
$$


Therefore


$$
\boxed{\Gamma _1(0)=7\zeta.}
\tag{6.9}
$$



This is the precise obstruction to completing the $J_{29}$-part from the existing receipts. Aggregate knowledge of $\kappa_e,g_e$ does not determine the sub-contraction (6.4).

---

## 7. Minimal exact calculation defining $\zeta$

Only one new scalar is needed for the whole $\Gamma _1$-table. Return $\zeta_0,\zeta_1$ as well if the full polynomial $R_{29}$, rather than its class modulo $\operatorname{span}K_d$, is wanted.

Use the fixed odd representative


$$
b^\circ=1395217,\qquad n^\circ=2791829217,
$$


so $h^\circ=1$, $N^\circ=3947$. At $J=0$,


$$
F(0)\equiv7,\qquad \ell_0(0)\equiv8,\qquad\ell_1(0)\equiv3.
$$


Set $s_0=8,s_1=3$.

For $x\in\mathcal X$,


$$
c(x)=
\frac{p^{-2}\binom{n^\circ+2}{x}
 \binom{2n^\circ+b^\circ-x}{b^\circ-x}}
 {7s_{e(x)}}\pmod p.
\tag{7.1}
$$



For $\xi(x)$, retain the complete leading boundary


$$
\mathcal Q_0=(2+r^{-1})(1+x+xr^{-1})
$$


and


$$
\mathcal T_2=
-6\sum_{h=2}^{30}(-1)^h(h-2)!
 (1+r^{-1})^h(1+x+xr^{-1}).
\tag{7.2}
$$


Its coefficient of $r^{-k}$ is explicitly


$$
t_k(x)=
-6\sum_{h=2}^{30}(-1)^h(h-2)!
\left((1+x)\binom hk+x\binom h{k-1}\right),
\quad0\le k\le31.
\tag{7.3}
$$


Then


$$
\boxed{
\xi(x)=\frac{p^{-3}W_x}{7s_{e(x)}}
\left[
2(1+x)B_0+(1+3x)B_{-1}+xB_{-2}
+p^2\sum_{k=0}^{31}t_k(x)B_{-k}
\right]\pmod p.
}
\tag{7.4}
$$



The first contact polynomial is


$$
a(X)=9\left[
\binom{b-X+28}{28}+\binom{b-X+29}{28}
\right],
$$


with reconstructed kernel


$$
r\,a(x)+(1+r)x\,a(x-1).
$$


It is zero modulo $p$ on $\mathcal X$, because $x_0\le2$. Thus its omission from (7.4) is proved; the complete relevant contact is not an unspecified missing input.

**Raw arithmetic requirements:**

* compute the binomials in (7.1) modulo $p^3=24389$;
* compute all binomials and products in (7.4) modulo $p^4=707281$;
* perform the displayed divisions only after verifying divisibility;
* sum only the $3036$ coordinates $x\in\mathcal X$ with $x_0=0$.

This is independent of $d$.

---

# Part III. A universal table for $R_C$

## 8. Fixed complete kernels needed at this layer

The calculation of $R_C$ requires


$$
P\bmod p^2,\qquad Q\bmod p^2.
$$


After the established reconstruction carries, the complete inputs are:

* $h_A\bmod p^2$, degree at most $57$;
* $h_Q\bmod p^3$, degree at most $57$;
* all boundary coefficients through $59$, including every negative power through $-60$.

Here are formulas sufficient to construct these inputs without external code.

### Contact coefficients

For $1\le s\le58$,


$$
\boxed{
d_s=(-1)^ss!
\sum_{u=0}^{\lfloor s/2\rfloor}
\binom n{s-u}\binom{s-u}{u}2^{-u}.
}
\tag{8.1}
$$


Use these modulo $p^3$, or the lower precision required by a particular term.

The signed finite contact operator is


$$
\begin{aligned}
\mathscr L_{s,b}\binom Xr
={}&(-1)^s\binom Xs\binom{X-s}r\\
&+\sum_{v=1}^s(-1)^{s-v}\binom X{s-v}\binom nv
 \sum_{i=0}^r
 \binom{X-s+v}{r-i}\binom{v+i-1}i
 \binom{b-1-X+s}{v+i}.
\end{aligned}
\tag{8.2}
$$


The final binomial retains the actual finite boundary.

### $A$-kernel

Use the formal moments


$$
J_0=1,\quad J_{29}=0,\quad
J_t=p\,\frac{7(8\cdot20^t-20\cdot8^t)}{12t}
\quad(1\le t\le28),
$$


and $J_t=0$ for $30\le t\le57$. Construct $g_A$ by (2.2), with those moments, and set


$$
\boxed{
h_A=\left(I-\sum_{s=1}^{29}d_s\mathscr L_{s,b}\right)g_A
\pmod{p^2}.
}
\tag{8.3}
$$



### Complete $Q$-kernel

Set


$$
F_r=\frac{(b+r)!}{b!},\qquad
c_h=\sum_{r=h}^{59}F_r\binom{2n}{r-h}\pmod{p^4}.
\tag{8.4}
$$


Construct


$$
\begin{aligned}
a_Q(X)=
\sum_{s=1}^{58}d_s\sum_{h=0}^{59}
c_h(-1)^{h+s+1}
\sum_{v=1}^s(-1)^v
\binom X{s-v}\binom nv
\binom{b+h-X+s-1}{v-1}.
\end{aligned}
\tag{8.5}
$$


The sign uses the original odd parity of $b$. Then


$$
\boxed{
h_Q=\left(I-\sum_{s=1}^{29}d_s\mathscr L_{s,b}\right)a_Q
\pmod{p^3}.
}
\tag{8.6}
$$


Terms with two subsequent contacts have valuation at least three and are zero at this precision.

Reconstruct these Newton polynomials by the turn15 formula, and include the entire boundary


$$
\boxed{
\sum_{h=0}^{59}(-1)^hc_h(1+r^{-1})^h(1+x+xr^{-1}).
}
\tag{8.7}
$$


Let the resulting coefficient arrays be


$$
a_q(x)\quad(0\le q\le58),\qquad
y_q(x)\quad(-60\le q\le58).
$$



The safe original force construction is reduced to these ranges only after applying the stated carry bounds. The whole logarithmic force remains absent solely under its retained whole-force valuation bound.

---

## 9. Explicit first low-unit correction

For each $x\in[0,L)$, put


$$
v=b_*-x,\quad
e=\mathbf1_{x>191112},\quad
u=\left\lfloor\frac{382219+v}{L}\right\rfloor,\quad
r_q=\mathbf1_{v-q<0}.
$$


The three possible shapes are


$$
(e,u)=(0,1),(1,1),(1,0).
$$


With formal variables $D,J$, define


$$
G_{eu}(D,J)=(3-J)^e(D+7-J)^u.
\tag{9.1}
$$



The exact high ratio is


$$
F(J)\,G_{eu}(D,J)(D-J)^{r_q}.
\tag{9.2}
$$



### Fully specified stripping factors

Represent a factorial argument as $z=La+t$, $0\le t<L$. For $i=0,1,2,3$, set


$$
s_i(z)=\left\lfloor t/p^i\right\rfloor\bmod p,\qquad
m_i(z)=p^{3-i}a+\left\lfloor t/p^{i+1}\right\rfloor.
$$


At this precision,


$$
U_p(pm+s)\equiv(28!)^m s!(1+pmH_s)\pmod{p^2}.
\tag{9.3}
$$



Apply this to the following two factorial ratios:



$$
\begin{array}{c|c|c}
&\text{high part}&\text{low part}\\ \hline
W\text{ numerator}&3&191112\\
W\text{ first denominator}&J&x\\
W\text{ second denominator}&3-J-e&191112-x+Le\\ \hline
B_q\text{ numerator}&6+D-J+u&382219+v-Lu\\
B_q\text{ first denominator}&D-J-r_q&v-q+Lr_q\\
B_q\text{ second denominator}&6&382219+q
\end{array}
\tag{9.4}
$$



For each stripping level, subtract the two denominator $m_i$'s from the numerator $m_i$. These differences are the fixed low carries. Let their total over both binomials be $c_{xq}$.

Define


$$
u_{xq}=(28!)^{c_{xq}}
 \prod_{i=0}^3
 \frac{s_i(W_{\rm top})!\,s_i(B_{\rm top})!}
 {s_i(W_{\rm bot1})!\,s_i(W_{\rm bot2})!\,
  s_i(B_{\rm bot1})!\,s_i(B_{\rm bot2})!}
 \pmod{p^2},
\tag{9.5}
$$


and


$$
\Lambda_{xq}(D,J)
=\sum_{i=0}^3
 \left(m_iH_{s_i}\right)_{\rm numerators}
-\sum_{i=0}^3
 \left(m_iH_{s_i}\right)_{\rm denominators}
\pmod p.
\tag{9.6}
$$


This is affine:


$$
\Lambda_{xq}=\lambda_{xq,0}
+\lambda_{xq,D}D+\lambda_{xq,J}J.
\tag{9.7}
$$



Equations (9.4)–(9.7) give every harmonic coefficient explicitly. In particular, $28!$ is retained modulo $841$, not replaced by $-1$.

---

## 10. Six scalars per column and low coordinate

Group the Laurent powers by $r_q=0,1$. Define


$$
\begin{aligned}
A_{xr}(D,J)
&=\sum_{q:r_q=r}
p^{c_{xq}-2}a_q(x)u_{xq}
 \bigl(1+p\Lambda_{xq}(D,J)\bigr),\\
Q_{xr}(D,J)
&=\sum_{q:r_q=r}
p^{c_{xq}-3}y_q(x)u_{xq}
 \bigl(1+p\Lambda_{xq}(D,J)\bigr).
\end{aligned}
\tag{10.1}
$$


These expressions are integral after combining the displayed kernel coefficient with its low carry factor. The unit-boundary $q=-2$ term includes its factor $x$.

Write


$$
A_{xr}=a_{xr}+p(b_{xr,D}D+b_{xr,J}J),\qquad
Q_{xr}=q_{xr}+p(c_{xr,D}D+c_{xr,J}J),
\tag{10.2}
$$


where $a_{xr},q_{xr}$ are modulo $841$, and the other coefficients are modulo $29$. The constant part of $\Lambda$ is included in $a_{xr},q_{xr}$.

Then the natural low polynomials are exactly


$$
A_x=G_{eu}\bigl(A_{x0}+(D-J)A_{x1}\bigr),
$$




$$
Q_x=G_{eu}\bigl(Q_{x0}+(D-J)Q_{x1}\bigr)
\pmod{p^2}.
\tag{10.3}
$$



Thus Laurent powers are contracted into six scalars per column **before** the final polynomial multiplication.

Required raw kernel precisions are:

* $a_q\bmod p^2$;
* positive $Q$-coefficients modulo $p^3$;
* general negative coefficients modulo $p^4$;
* unit-boundary $q=0,-1$ coefficients need only modulo $p^2$.

Using the safe precisions in Section 8 is sufficient.

---

## 11. The universal $27$-entry table

For each of the three shapes $(e,u)$, and $v=0,1,2$, define



$$
\boxed{
T^{(0)}_{eu,v}
=
\sum_{\substack{x:\,\mathrm{shape}(x)=(e,u)\\r+s=v}}
\left(a_{xr}q_{xs}-\frac16a_{xr}a_{xs}\right)
\pmod{p^2}.
}
\tag{11.1}
$$



For $Z=D,J$, define


$$
\boxed{
\begin{aligned}
T^{(Z)}_{eu,v}
=\sum_{\substack{x:\,\mathrm{shape}(x)=(e,u)\\r+s=v}}
\bigg[
&a_{xr}c_{xs,Z}+b_{xr,Z}q_{xs}\\
&-\frac16\bigl(a_{xr}b_{xs,Z}+b_{xr,Z}a_{xs}\bigr)
\bigg]\pmod p.
\end{aligned}}
\tag{11.2}
$$



There are exactly:

* nine $T^{(0)}$-entries modulo $841$;
* nine $T^{(D)}$-entries modulo $29$;
* nine $T^{(J)}$-entries modulo $29$.

Define the ordinary polynomials


$$
H_{\rm flat}(D,J)
=
\sum_{eu,v}G_{eu}(D,J)^2(D-J)^vT^{(0)}_{eu,v},
\tag{11.3}
$$




$$
H_{\rm harm}(D,J)
=
\sum_{eu,v}G_{eu}(D,J)^2(D-J)^v
 \bigl(DT^{(D)}_{eu,v}+JT^{(J)}_{eu,v}\bigr).
\tag{11.4}
$$


Then


$$
\boxed{
R_C(D,J)=\frac{H_{\rm flat}(D,J)}p+
H_{\rm harm}(D,J)\pmod p.
}
\tag{11.5}
$$



The division in (11.5) is **coefficientwise after summing** (11.3). Individual table entries need not be divisible by $p$.

The degree bounds are


$$
\deg H_{\rm flat}\le6,\qquad
\deg H_{\rm harm}\le7.
\tag{11.6}
$$


This supplies the requested universal two-variable polynomial. After this one fixed calculation, every $\Gamma _0(d)$ is obtained by the at-most-four-term functional (1.2).

---

## 12. Ordinary lifted cancellation and independence of higher digits

This point is essential.

Before substituting $N=3,h=D$, retain


$$
\ell_0=2N+h+1-J,\qquad\ell_1=N-J
$$


as ordinary polynomials. The leading low representatives satisfy


$$
A_x^{(0)}=
\begin{cases}c(x)\ell_{e(x)},&x\in\mathcal X,\\0,&x\notin\mathcal X,\end{cases}
$$


and, on $\mathcal X$,


$$
Q_x^{(0)}=\xi(x)\ell_{e(x)}.
$$


These are stripping identities, not identities obtained by division by values of $F(J)$.

Choose integral lifts of the low constants. The leading contracted polynomial is


$$
\sum_e
\left(
\sum_{x\in\mathcal X_e}c(x)\xi(x)
-\frac16\sum_{x\in\mathcal X_e}c(x)^2
\right)\ell_e^2.
\tag{12.1}
$$


Each parenthesized coefficient is divisible by $p$, by $g_e=\kappa_e/6$.

Consequently replacing


$$
N\longmapsto N+p\nu,\qquad h\longmapsto h+p\eta
$$


changes (12.1) by a polynomial divisible by $p^2$. The harmonic corrections already carry an explicit $p$; their dependence on $N,h$ is affine modulo $p$, so the same replacement changes them only modulo $p^2$.

This proves that after division by $p$, the residual depends only on


$$
N\bmod p=3,\qquad h\bmod p=d.
$$



The bounded kernel coefficients themselves use only the fixed low parameter residues at these precisions. For example, varying $b$ by $p^4$ changes the relevant $F_r$, $r\ge2$, by multiples of $p^4$; these are killed in $Y\bmod p^5$ by the negative-power reconstruction carry.

**Parity is not interpolated:** the sign in (8.5), (8.7) is fixed from the original odd $b$. Setting $h=D$ in the polynomial multiplier is formal and does not replace that sign by the parity of an auxiliary integer.

Thus the higher-digit assertion is justified as an ordinary lifted-polynomial statement.

---

## 13. Normalization terms versus genuine harmonic contractions

A uniform first-order change


$$
A_x\mapsto A_x+p\alpha A_x^{(0)},\qquad
Q_x\mapsto Q_x+p\beta Q_x^{(0)}
$$


changes $R_C$ by


$$
\frac{\beta-\alpha}{6}K_d.
\tag{13.1}
$$


Such degree-zero normalizations are annihilated by $\mathcal L_d$.

But **not every $J$-independent low correction is a uniform normalization**. A correction depending on $x$, or separately on the two shapes, need not be proportional to $K_d$. It must remain in $T^{(0)}$.

Likewise the first harmonic correction contains weighted sums such as


$$
\sum_{x\in\mathcal X}
c(x)\bigl(\xi(x)-c(x)/6\bigr)
\Lambda_{x,1}(D,J)\ell_{e(x)}^2,
\tag{13.2}
$$


as well as relative harmonic differences between the surviving $Q$-powers and the base $P$-power. Neither $\kappa_e$ nor $g_e$ evaluates these weighted contractions.

Equations (11.1)–(11.5) retain all of them. A leading-constant analogy cannot replace this table.

---

## 14. Finite boundaries and the unfrozen correction

For $x>b_*$, every positive $P$-power has $r_q=1$. Thus $A_x$ contains $h-J$. The actual ranges


$$
0\le J\le h\quad(x\le b_*),\qquad
0\le J\le h-1\quad(x>b_*)
$$


may be extended in the contractions only after exhibiting that factor. Formula (10.3) does so explicitly.

For the third-defect derivation one still needs $P,Q\bmod p^3$, not merely the polynomials defining $R_C$. At that precision the unit-boundary coefficient cannot be frozen. Retain turn22’s explicit correction


$$
\delta Y_{LJ+x}
\equiv(-1)^{j+1}LJ\,W_jB_{-2}(j)\pmod{p^6}.
\tag{14.1}
$$


At $x=0$,


$$
\delta Q_0(J)=23p^2J\ell_0(J),
$$


and its mixed low-polynomial contribution is


$$
3C_np^2J\ell_0(J)^2.
\tag{14.2}
$$


This lies in the second residual polynomial; its leading contraction is killed by $T=0$. It therefore does not enter (11.5), but it remains necessary in the proof of (1.1).

For that precision-three representation, retain the complete boundary through factorial index $88$, all negative powers through $-89$, and the actual endpoint $W_b(1+b\theta^Q_{b-1})$.

---

# 15. Primitive arithmetic and whole error: retained dependencies

No new denominator or real-error theorem is asserted.

Keep the actual least two-column denominator $d_B$, the actual falling metric, and


$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B.
$$


The primitive multiplier is $1/g_B$ on the integer Gram pair, or $d_B^2/g_B$ on the rational pair.

With the supplied arithmetic interface,


$$
v_{29}(g_B)=
\min\{4F_n+4+\delta,\ 2F_n+F_b+5+\mu\},
$$




$$
v_{29}(q_n)=
\max\{0,\ 2F_n-F_b-1+\delta-\mu\}.
$$


The whole evaluated form remains exactly


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$


The supplied signed-error theorem and nonvanishing dependencies retain their source status. No partial forcing or local denominator is substituted for the whole error or the final primitive denominator.

---

# Concluding ledger

## New results proved here

* The full $58$-entry Newton vector $h_B\bmod29$.
* Its complete four-power Laurent reconstruction, with contact and endpoint treatment.
* The normalized $J_{29}$-column multiplier $\theta=(21,13,13)$ on the three digit-zero residues.
* The reduction
  

$$
R_{29}\equiv8\zeta(3-J)^2
  \pmod{\operatorname{span}K_d},
$$


  and hence
  

$$
\Gamma _1(d)=8\zeta\mathcal L_d((3-J)^2),\qquad
  \Gamma _1(0)=7\zeta.
$$


* A universal $27$-entry contraction table for $R_C$, independent of $d$, with an ordinary degree-at-most-seven reconstruction.
* Higher-digit independence after division by $29$, proved using ordinary cancellation at lifted $N,h$, not field-value interpolation.

## Exact remaining bottleneck

The third-defect coefficient evaluation is reduced to:

1. the single scalar $\zeta$;
2. the $27$-entry universal table (11.1)–(11.2).

Neither is evaluated in this report. Thus third-depth alignment, actual-index reachability of a nonzero defect, all-depth relative valuation control, and irrationality of $e+\pi$ remain unresolved.

## Bounded exact arithmetic now requested

**Calculation A — small first.**

Inputs: the fixed representative in Section 7, the $3036$ supported coordinates with $x_0=0$, and formulas (7.1)–(7.4).

Return:

* $\zeta_0,\zeta_1,\zeta$;
* divisibility checks before every normalization;
* optionally the 25 values
  

$$
\Gamma _1(d)=8\zeta\mathcal L_d((3-J)^2).
$$



Expected mandatory check:


$$
\Gamma _1(0)=7\zeta.
$$



**Calculation B — one universal pass, not 25 passes.**

Inputs: the fixed kernels (8.1)–(8.7), the stripping data (9.4), and all $0\le x<29^4$.

Return:

* nine $T^{(0)}$ residues modulo $841$;
* eighteen harmonic residues modulo $29$;
* a coefficientwise receipt
  

$$
H_{\rm flat}(D,J)\equiv0\pmod{29};
$$


* the reconstructed ordinary polynomial $R_C(D,J)$;
* its 25 contractions under (1.2), with ordinary derivatives.

These computations would finish the missing coefficient tables at their stated finite scope. Even vanishing of both tables would establish only the stated third-depth relation—not an all-depth denominator bound or an irrationality proof for $e+\pi$.
