> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Turn 20 — Evaluation of the first-four mixed-prefix return and its actual finite inverse

## Abstract

The global rationality or irrationality of $e+\pi$ remains unresolved.

The local obligation isolated in Turn 19 can, however, be evaluated at its stated leading core precision. The calculation below does **not** use the closed second-kernel prefix quadratic to supply the missing mixed digit.

Write


$$
I=k-1,\qquad \varepsilon_{\rm alt}=(-1)^{k-2},
\qquad c=2\chi,\qquad
\rho=\frac{\Pi-1}{2},\qquad
M=L_*+\chi-1.
$$


All matrices and coordinates below retain their original finite boundaries.

The new results are:

1. For every original amplitude $0\le u\le R$, and every $0\le i\le I$,
   

$$
\boxed{
   d_u^T\mathsf A^{-1}d_H{}_i\in9\mathbb Z_3.
   }
$$


   Consequently, the actual normalized mixed-prefix digit is
   

$$
\boxed{
   P_{ui}=\frac{d_u^T\mathsf A^{-1}d_H{}_i}{3}=0
   \quad\text{in }\mathbb F_3.
   }
$$


   In particular, this evaluates both requested endpoint columns $P_{u,0}$ and $P_{u,I}$.

2. Let $v_\partial$ be the coefficient vector, on the **original monomial complement**, of
   

$$
y^M(1-y)^c.
$$


   The actual leading finite inverse application is
   

$$
\boxed{
   \overline{A_4}^{\, -1}(C_H)_i
   =
   e_{\rho+i}+2\mathbf1_{i=I}v_\partial.
   }
$$


   This is certified directly by multiplication by the original finite $\overline A_4$. No auxiliary inverse replaces it.

3. The complete first-four returned operator is evaluated:
   

$$
\boxed{
   R_4=C_H^T\overline{A_4}^{\, -1}C_H=0
   \quad\text{over }\mathbb F_3.
   }
$$


   Therefore, for
   

$$
g_4=C_H(e_0+\varepsilon_{\rm alt}e_I),
$$


   one has the explicit inverse image
   

$$
\boxed{
   \overline{A_4}^{\, -1}g_4
   =
   e_\rho+\varepsilon_{\rm alt}e_{\rho+I}
   +2\varepsilon_{\rm alt}v_\partial,
   }
$$


   and the scalar isolated in Turn 19, equation (10.6), is
   

$$
\boxed{
   g_4^T\overline{A_4}^{\, -1}g_4=0.
   }
$$



These are leading core residue statements. They do not assert that the corresponding entire $3$-adic return is identically zero.

The first-four term can now be removed from the leading physical-$6$ assembly. The unknown interior terminal coordinates remain in


$$
h=N^T\eta.
$$


Even with the two endpoint residues zero, the alternating vector need not lie in the kernel of $B_6$. Moreover, the permitted equation


$$
B_6x=w_6,\qquad x\in3^{-1}\mathbb Z_3^{k-1},
$$


still requires the next whole digit and its complete source returns.

---

## 1. Scope, inherited results, and review status

### 1.1 What is reused

The proof uses the following established results at their stated scope:

- complete corrected-pairing compression through source precision $33$, for polynomial parts of degree at most $\nu-2$;
- the original finite prefix inverse formula;
- the normalized prefix matrix modulo $9$;
- the actual leading first-four form and its original finite complement/unit theorem;
- the evaluated direct first-four mixed moment and its leading $J$-correction;
- the common second-kernel-pivot frame.

The closed prefix-$6$ quadratic and closed terminal-aware $J6$ quadratic are used only in the later physical-$6$ assembly. They are **not** used to prove the new mixed-prefix digit.

### 1.2 Updated endpoint status

The supplied coordinator update changes the dependency ledger as follows.

- The A1 Turn 18 terminal-module/annihilator theorem and the A1 Turn 13 prefix/bare endpoint interface are now DIFFERENT-passed through A3 Turn 19.
- The complementary-source proof in A1 Turn 19, including its new LOW payments and the conclusion $\eta_I=0$, has favorable parent review; its separate DIFFERENT review remains pending.
- A3 Turn 19’s additional complete LOW-return lemma for $\eta_0=0$ has favorable parent review and is under the stated A4 Turn 24 audit.
- Neither of those new source-return proofs is relabelled here as independently passed.

The new prefix and first-four calculations below do not depend on either endpoint value. Endpoint-dependent consequences are identified explicitly in Section 8.

---

## 2. Original domain and complete finite objects

All uniform assertions concern sufficiently large members of exactly the original family


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
Q=27P,\qquad Q-N_0=b=2R,\qquad \chi=P-R,
$$


so that


$$
N_0=25P+2\chi,\qquad D=268P+2\chi.
$$



The subwindow remains


$$
\boxed{\frac3{25}<\frac{\chi}{P}<\frac{31}{250}.}
\tag{2.1}
$$


No independent choices of $P,\chi$, or $I$ are made.

Put


$$
S=h-32,\qquad P=3^S,\qquad S\ge31,
$$




$$
\Pi=P/3,\qquad c=2\chi,\qquad t=\Pi-c,
$$




$$
k=3\chi-\Pi-1,\qquad I=k-1=3\chi-\Pi-2,
\qquad L=L_*=\frac{P-1}{2}.
$$


The original arithmetic gives


$$
v_3(\chi)=5,\qquad \chi/243\equiv1\pmod9,
\qquad v_3(D)=v_3(t)=5.
$$


In particular,


$$
\beta=D-H-71\equiv1\pmod9.
\tag{2.2}
$$



The useful exact relations are


$$
t+I=\chi-2,\qquad b+\Pi=2P+t.
\tag{2.3}
$$


The retained subwindow gives $0<t<\Pi$, $k\ge2$, and


$$
R-\deg H_I
=\frac{P+5}{2}-4\chi>0,
\tag{2.4}
$$


where


$$
H_i=(1-y)^\Pi y^{L+i},\qquad 0\le i\le I.
$$


Thus every literal coefficient of every $H_i$ is an admitted amplitude coordinate $0\le u\le R$.

### 2.1 The complete functional and projection

Set $x=y-1$. The original finite spaces are


$$
U_u=x^u,\qquad 0\le u<D,
$$




$$
z_i^{\rm mid}=x^Dy^i,\qquad 0\le i<\nu,
\qquad \nu=D/2-1,
$$




$$
Y_s=y^s,\qquad d\le s\le m,\qquad d=D+\nu.
$$



The physical HIGH terminal is $Y_m$. The last middle polynomial is $y^{\nu-1}$. They are not interchanged.

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


For


$$
Q_c=(y+1)x^A(\beta+3y),
\qquad G_c(f,g)=\mathcal M(Q_cfg),
$$


write


$$
W=[U\ Y],\qquad E_c=G_c(W,W).
$$


Every column used below is the complete corrected column


$$
\boxed{
F[p]=x^Dp-WE_c^{-1}G_c(W,x^Dp).
}
\tag{2.5}
$$



The actual finite LOW/HIGH decomposition remains


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
$$


The physical LOW inverse is $3^{-1}M_L$, not $M_L$.

### 2.2 Prefix and terminal boundaries

Retain


$$
R_*=\frac{9Q+1}{2},\qquad a_0=R_*-1,
$$




$$
\tau=\frac{N_0-3}{2},\qquad \ell=3R+1,
$$




$$
K=\{0,\ldots,3R\},\qquad
J=\{\ell,\ldots,\tau-1\},
\qquad R_*+\tau=\nu.
$$



Define the ordinary amplitude lift


$$
\mathcal F[y^u]
=
F\!\left[(1-y)^b y^{k_0+u}(y^{3Q}+3)\right],
\qquad k_0=\frac{3Q+1}{2}.
\tag{2.6}
$$


Its polynomial part has degree at most $R_*+3R<\nu-1$. Hence it, and every prefix polynomial $y^p$, $0\le p\le a_0$, lies in the admitted compression scope. No compression is applied here to $F[y^{\nu-1}]$.

---

## 3. The actual prefix quantities and their precision

Let


$$
\mathsf A=-\frac{G_c(F_{\rm pref},F_{\rm pref})}{3^{26}},
$$


and


$$
d_u=\frac{G_c(F_{\rm pref},\mathcal F[y^u])}{3^{28}},
\qquad 0\le u\le R.
\tag{3.1}
$$


The literal integer coefficient matrix of the $H_i$ is denoted by $\mathscr H$. Thus


$$
d_H{}_i=\sum_{u=0}^R [y^u]H_i\,d_u.
\tag{3.2}
$$


This contraction is over the integers before reduction.

The target is


$$
P_{ui}
=
\frac{d_u^T\mathsf A^{-1}d_H{}_i}{3}\pmod3.
\tag{3.3}
$$


Therefore the undivided contraction must be known modulo $9$.

Put


$$
U(y)=(1-y)^{N_0}.
$$


For $\Delta\in\mathbb Z$, define the original-size finite matrices


$$
(A_\Delta)_{pq}=U_{a_0+\Delta-p-q},
\qquad 0\le p,q\le a_0.
\tag{3.4}
$$


In particular, $A_0$ is the established leading prefix matrix, and its exact finite inverse is


$$
(A_0^{-1})_{pq}
=
[y^{p+q-a_0}]U^{-1}.
\tag{3.5}
$$



The supplied prefix formula, with its shifts made explicit, is


$$
\mathsf A
\equiv
K_N\bigl(-2\beta A_0+3A_{-1}-3\beta A_{3Q}\bigr)
\pmod9.
\tag{3.6}
$$


The shifts in (3.6) are genuine finite shifts, not periodic identifications. For example, the $3y$ term lowers the coefficient index by one and hence gives $A_{-1}$.

Using (2.2), write


$$
\mathsf A
\equiv
K_N\{A_0+3(-A_0+A_{-1}-A_{3Q})\}\pmod9.
$$


Consequently,


$$
\boxed{
\mathsf A^{-1}
\equiv K_N^{-1}
\left[
A_0^{-1}
+
3A_0^{-1}(A_0-A_{-1}+A_{3Q})A_0^{-1}
\right]\pmod9.
}
\tag{3.7}
$$



The source digits needed in (3.1) require the complete pairings modulo $3^{30}$. The prefix matrix modulo $9$ requires its complete pairing modulo $3^{28}$. Both are inside the established compression precision $33$.

---

## 4. New evaluation of the two source digits of $d_u$

This section supplies the previously missing source-specific information.

### 4.1 Complete compact source and all visible pole layers

In the accepted complete corrected-pairing formula, the compact polynomial for $d_u$ is


$$
(1-y)^{D+b}(\beta+3y)y^{k_0+p+u}(y^{3Q}+3).
$$


Since $D+b=10Q$, put


$$
T(y)=(1-y)^{10Q},\qquad T_a=[y^a]T,
\qquad z=p+u+1.
$$



The compact degree satisfies


$$
2\deg+1\le38Q+3+2R<39Q.
\tag{4.1}
$$


After division by $3^{28}$, the only pole layers visible modulo $9$ are:

- denominator $27Q$;
- denominator $9Q$;
- unit multiples of $3Q$;
- unit multiples of $Q$.

The complete physical cutoff is much larger than (4.1), so none of these coefficient extractions extends the original functional.

The unit-$Q$ layer is zero modulo $9$. Indeed, it is already multiplied by $3$, so only $T\bmod3$ matters:


$$
T(y)\equiv(1-y^Q)^{10}
=1-y^Q-y^{9Q}+y^{10Q}.
$$


A nonzero observation requires $z=sQ$, $1\le s\le4$. Its divided unit coefficient is


$$
\frac1{2s+9}-\frac1{2s+11}
-\frac1{2s+27}+\frac1{2s+29}\pmod3,
\tag{4.2}
$$


with terms divisible by $3$ omitted because they belong to higher pole layers. The first and third denominators have the same residue modulo $3$, as do the second and fourth; their inclusion conditions also agree. Thus (4.2) is zero. The weighted low term and $3y$ term in this layer are already in $9$.

The remaining complete normalized scalar source is


$$
\begin{aligned}
D(z)={}&
\frac{T_{9Q-z}+3T_{12Q-z}}9
+T_{3Q-z}\\
&+\frac{T_{3Q-z}+3T_{6Q-z}}5
+\frac{T_{6Q-z}+3T_{9Q-z}}7
+\frac{T_{12Q-z}}{11}
\pmod9.
\end{aligned}
\tag{4.3}
$$


Here:

- the first fraction is the whole $27Q$ numerator;
- the denominator-$9Q$ high extraction is outside support, while its low extraction gives $T_{3Q-z}$;
- the unit-$3Q$ denominators are $5,7,11$;
- the denominator-$3Q$ unit $1$, and the $11$-channel low extraction, are outside the actual support.

The complete source, including the $3y$ channel, is therefore


$$
\boxed{
(d_u)_p\equiv K_N\{\beta D(z)+3D(z+1)\}\pmod9.
}
\tag{4.4}
$$



The division by $9$ in (4.3) will now be paid using the whole numerator modulo $81$.

### 4.2 The required integer-binomial carry identity

Let


$$
A(y)=(1-y)^Q,\qquad A_{\rm mac}(y)=1-y^Q.
$$


Because $Q$ is a power of $3$,


$$
A(y)\equiv
1-y^Q+3(-y^{Q/3}+y^{2Q/3})\pmod9.
\tag{4.5}
$$


This follows from


$$
v_3\binom Qr=v_3(Q)-v_3(r)
$$


and the two normalized units at $r=Q/3,2Q/3$.

Write $A=A_{\rm mac}+3E$, so


$$
E\equiv-y^{Q/3}+y^{2Q/3}\pmod3.
$$


Expanding the ninth power gives


$$
A^9\equiv A_{\rm mac}^9+27A_{\rm mac}^8E\pmod{81}.
$$


Multiplication by $A$ yields the finite algebraic identity


$$
\boxed{
T=A^{10}
\equiv
A A_{\rm mac}^{\,9}
+27A_{\rm mac}^{\,9}E
\pmod{81}.
}
\tag{4.6}
$$



In particular,


$$
T_{aQ}\equiv(-1)^a\binom{10}{a}\pmod{81}.
\tag{4.7}
$$


For $0<l<Q$, the first term in (4.6) contributes


$$
(-1)^a\binom9a A_l
$$


at $aQ+l$. The second term, modulo $81$, occurs only in the $a=0$ and $a=9$ bands.

Since $10Q$ is even, reciprocity gives


$$
T_{9Q-z}=T_{Q+z},
\qquad T_{12Q-z}=T_{z-2Q}.
$$


Thus (4.3) becomes


$$
\begin{aligned}
D(z)={}&
\frac{T_{Q+z}+3T_{z-2Q}}9
+\frac65T_{7Q+z}
+\frac{26}{35}T_{4Q+z}\\
&+\frac37T_{Q+z}
+\frac1{11}T_{z-2Q}
\pmod9.
\end{aligned}
\tag{4.8}
$$



For $z=sQ+l$, $0<l<Q$, $0\le s\le4$, the whole numerator in the first fraction is, modulo $81$,


$$
b_sA_l,
$$


where


$$
\begin{array}{c|rrrrr}
s&0&1&2&3&4\\ \hline
b_s&-9&36&-81&99&-18\\
b_s/9&-1&4&-9&11&-2.
\end{array}
\tag{4.9}
$$


Every $b_s$ is divisible by $9$. This explicitly pays the division; it is not inferred from the leading zero of the final contraction.

Modulo $9$, the additional terms in (4.8) contribute off the macro grid only through


$$
\frac1{11}\mathbf1_{s=2}A_l.
$$


Hence, with


$$
(e_0,e_1,e_2,e_3,e_4)=(2,1,2,2,1)\in\mathbb F_3^5,
$$


one obtains


$$
\boxed{
D(sQ+l)
\equiv
3e_s\bigl(
-\mathbf1_{l=Q/3}
+\mathbf1_{l=2Q/3}
\bigr)\pmod9.
}
\tag{4.10}
$$



At the four macro positions, the full calculation is


$$
\begin{array}{c|rrrr}
s&1&2&3&4\\ \hline
(T_{Q+sQ}+3T_{sQ-2Q})/9
&5&-13&20&-13\\
\text{remaining terms modulo }9
&0&5&4&0\\ \hline
D(sQ)\bmod9&5&1&6&5.
\end{array}
\tag{4.11}
$$



Equations (4.10)–(4.11) evaluate the needed source digits uniformly. No $P$-length table is involved.

### 4.3 A fixed finite source description

For an integer $M_0$, define the finite prefix column


$$
(E_{M_0}(u))_p=\mathbf1_{p+u+1=M_0},
\qquad 0\le p\le a_0.
$$


Then


$$
d_u\equiv K_N(d_u^{[0]}+3d_u^{[1]})\pmod9,
\tag{4.12}
$$


where


$$
\boxed{
d_u^{[0]}=2E_Q(u)+E_{2Q}(u)+2E_{4Q}(u),
}
\tag{4.13}
$$


and


$$
\begin{aligned}
d_u^{[1]}={}&
E_Q(u)+2E_{3Q}(u)+E_{4Q}(u)\\
&+\sum_{s=0}^{4}e_s
\{-E_{sQ+Q/3}(u)+E_{sQ+2Q/3}(u)\}\\
&+2E_{Q-1}(u)+E_{2Q-1}(u)+2E_{4Q-1}(u).
\end{aligned}
\tag{4.14}
$$



The last line is precisely the retained $3y$ source correction.

These are literal finite columns. The location $14Q/3=126P$ is outside the prefix for every admitted amplitude and is zero. Every other displayed active location lies between $9P$ and $117P$, or is one of the three displayed one-step shifts. Thus its row $M_0-1-u$ lies inside $0,\ldots,a_0$ for every $0\le u\le R$.

Contracting (4.12) with the **integer** coefficients of $H_i$ gives


$$
d_H{}_i
\equiv K_N(d_{H,i}^{[0]}+3d_{H,i}^{[1]})\pmod9.
\tag{4.15}
$$


No reduction of $(1-y)^\Pi$ has been made before the precision in (4.12) was paid.

---

## 5. Evaluation of the complete mixed-prefix quotient

Put


$$
r=r_{ui}=P-1-u-i.
$$


For the full original ranges,


$$
\boxed{t+1\le r\le P-1.}
\tag{5.1}
$$



Let


$$
f(y)=U^{-1}(1-y)^\Pi=(1-y)^{t-25P}.
\tag{5.2}
$$



Combining (3.7), (4.12), and (4.15), the undivided contraction modulo $9$ is $K_N$ times


$$
\begin{aligned}
&S_{00}
+3S_{01}+3S_{10}\\
&\qquad+
3(Z_u^{[0]})^T(A_0-A_{-1}+A_{3Q})Z_{H,i}^{[0]},
\end{aligned}
\tag{5.3}
$$


where


$$
S_{ab}=(d_u^{[a]})^TA_0^{-1}d_{H,i}^{[b]},
\qquad
Z_u^{[0]}=A_0^{-1}d_u^{[0]},
\quad
Z_{H,i}^{[0]}=A_0^{-1}d_{H,i}^{[0]}.
$$



All terms in (5.3) will be evaluated.

### 5.1 The leading-source contraction through its next digit

The exact finite inverse formula (3.5), applied to the three locations in (4.13), gives


$$
\boxed{
S_{00}
=
8f_{12P+r}+4f_{39P+r}+4f_{93P+r}.
}
\tag{5.4}
$$


The other location sums have negative coefficient indices and are exactly zero. Formula (5.4) is an identity for the actual finite inverse application.

It remains to evaluate these coefficients modulo $9$, not merely modulo $3$.

Since $P=3\Pi$,


$$
(1-y)^{-25P}\equiv(1-y^\Pi)^{-75}\pmod9.
\tag{5.5}
$$


Put $z=y^\Pi$. The finite carry identity


$$
(1-z)^3=(1-z^3)+3(-z+z^2)
$$


gives


$$
\boxed{
(1-z)^{-75}
\equiv
(1-z^3)^{-25}
+3(z-z^2)(1-z^3)^{-26}
\pmod9.
}
\tag{5.6}
$$


Thus, for $e=1,2$,


$$
\frac{[z^{3B+e}](1-z)^{-75}}3
\equiv
(-1)^{e-1}[z^B](1-z)^{-26}\pmod3.
\tag{5.7}
$$



But


$$
(1-z)^{-26}\equiv\frac{1-z}{1-z^{27}}\pmod3,
$$


so its coefficient is zero at every $B\equiv12\pmod{27}$. In particular it is zero for


$$
B=12,\ 39,\ 93.
\tag{5.8}
$$



Now write $r=e\Pi+d$, $0\le d<\Pi$. Because $t<\Pi$, a coefficient in


$$
(1-y)^t(1-y^\Pi)^{-75}
$$


can survive only when $d\le t$. The possibility $e=0$ is excluded by $r>t$. Therefore only $e=1,2$ could contribute, and both are zero modulo $9$ by (5.7)–(5.8). Hence


$$
\boxed{
f_{12P+r}\equiv f_{39P+r}\equiv f_{93P+r}\equiv0\pmod9,
\qquad S_{00}\in9\mathbb Z_3.
}
\tag{5.9}
$$



This is the missing next-digit payment for the leading-source term.

### 5.2 Both first-order source corrections

Modulo $3$,


$$
\boxed{
f(y)=
\frac{(1-y)^t(1+y^P+y^{2P})}{1-y^Q}.
}
\tag{5.10}
$$


Thus its support, in each $Q$-period, lies only in


$$
[0,t],\qquad [P,P+t],\qquad [2P,2P+t].
\tag{5.11}
$$



For a location $M_0$ in $d_u^{[0]}$ and a location $N_0'$ in $d_u^{[1]}$, the exact finite inverse contraction, after the literal $H_i$ contraction, is the coefficient


$$
f_{M_0+N_0'-123P+r}.
\tag{5.12}
$$


All displayed source locations have already been checked to lie inside the actual prefix.

The possible residue positions of (5.12) modulo $Q=27P$ are


$$
\begin{array}{c|c}
\text{type of first-order location}&\text{coefficient position modulo }Q\\ \hline
sQ&12P+r\\
sQ+Q/3&21P+r\\
sQ+2Q/3&3P+r\\
jQ-1&12P+r-1.
\end{array}
\tag{5.13}
$$


Every position in (5.13) is outside all three intervals in (5.11), using (5.1). Therefore


$$
\boxed{S_{01}=S_{10}=0\pmod3.}
\tag{5.14}
$$



This includes the complete $3y$ source correction in the last line of (4.14).

### 5.3 The actual finite prefix inverse correction

Here it is useful to exhibit the finite inverse images themselves.

Over $\mathbb F_3$,


$$
U^{-1}=\frac{(1-y)^b}{1-y^Q}.
$$


For each of the three source locations $jQ$, $j=1,2,4$, exactly the translates $0,\ldots,j-1$ fit in the prefix. The next translate begins at $R_*+u>a_0$; the preceding translates fit completely because


$$
u+b\le3R<Q-1.
$$


Consequently, with


$$
\Phi(y)=1+y^Q+y^{3Q},
\qquad q_0=R_*-4Q=\frac{Q+1}{2},
$$


the actual finite inverse images are


$$
\boxed{
Z_u^{[0]}(y)
=
2y^{q_0+u}(1-y)^b\Phi(y),
}
\tag{5.15}
$$




$$
\boxed{
Z_{H,i}^{[0]}(y)
=
2y^{14P+i}(1-y)^t(1+y^P+y^{2P})\Phi(y).
}
\tag{5.16}
$$



These are finite polynomial identities on the original prefix interval. No infinite inverse has replaced that interval.

For $\Delta=0,-1,3Q$, the original matrix definition (3.4) gives


$$
(Z_u^{[0]})^TA_\Delta Z_{H,i}^{[0]}
=
[y^{a_0+\Delta}]\,U Z_u^{[0]}Z_{H,i}^{[0]}.
$$


Substituting (5.15)–(5.16) yields the finite identity


$$
\boxed{
\begin{aligned}
&(Z_u^{[0]})^TA_\Delta Z_{H,i}^{[0]}\\
&\quad=
[y^{93P+r+\Delta}]
(1-y^Q)(1+y^Q+y^{3Q})^2
(1+y^P+y^{2P})(1-y)^t.
\end{aligned}
}
\tag{5.17}
$$


The first factor is a finite polynomial in $y^Q$. Explicitly, in $\mathbb F_3[Z]$,


$$
(1-Z)(1+Z+Z^3)^2
=
1+Z+2Z^2+Z^3+Z^5+Z^6+2Z^7.
\tag{5.18}
$$


The remaining factor has only the three bands (5.11).

For $\Delta=0,3Q$, the requested coefficient has residue $12P+r$ modulo $Q$; for $\Delta=-1$, it has residue $12P+r-1$. All are outside (5.11). Thus


$$
\boxed{
(Z_u^{[0]})^TA_0Z_{H,i}^{[0]}
=
(Z_u^{[0]})^TA_{-1}Z_{H,i}^{[0]}
=
(Z_u^{[0]})^TA_{3Q}Z_{H,i}^{[0]}
=0
}
\tag{5.19}
$$


in $\mathbb F_3$.

This pays the entire finite inverse correction in (3.7), including its shifted finite boundary term.

### Theorem 5.1 — The actual mixed-prefix digit

For every original $0\le u\le R$ and $0\le i\le I$,


$$
\boxed{
d_u^T\mathsf A^{-1}d_H{}_i\in9\mathbb Z_3,
\qquad P_{ui}=0\in\mathbb F_3.
}
\tag{5.20}
$$



#### Proof

In the complete expansion (5.3), the first term is in $9$ by (5.9). Both source corrections vanish after their explicit factor $3$, by (5.14). The full inverse correction vanishes after its explicit factor $3$, by (5.19). Multiplication by the unit $K_N$ preserves divisibility by $9$. ∎

In particular,


$$
\boxed{P_{u,0}=P_{u,I}=0.}
\tag{5.21}
$$



The proof did not invoke the closed second-kernel prefix quadratic.

---

## 6. The original finite first-four inverse: an explicit certificate

The original monomial complement is


$$
\mathcal C
=
\{0,\ldots,R\}\setminus
\{L,\ldots,L+\chi-2\}.
$$


It is the disjoint union


$$
\mathcal C_-=\{0,\ldots,L-1\},
\qquad
\mathcal C_+=\{M,\ldots,R\},
\qquad M=L+\chi-1.
\tag{6.1}
$$



The actual leading normalized block is


$$
\boxed{
(\overline A_4)_{uv}
=
-[y^{\kappa-u-v}](1-y)^b,
\qquad
\kappa=\frac{3P-3}{2}=3L,
\quad u,v\in\mathcal C.
}
\tag{6.2}
$$


Its unit property is the established original finite complement theorem.

Put


$$
c_d=[y^d](1-y)^t,
\qquad c_d=0\quad(d<0\text{ or }d>t).
$$


The already evaluated direct moment, the leading $J$-payment, and Theorem 5.1 give the complete cross


$$
\boxed{
(C_H)_{ui}
=
-c_{2\Pi-1-u-i}
+c_{\,\Pi-1-u-i}
-2\mathbf1_{u=R,\ i=I}.
}
\tag{6.3}
$$


Both distinct moment supports remain, and so does the upper $3y$ corner.

### 6.1 The inverse of the two moment supports

Define


$$
\rho=\frac{\Pi-1}{2}.
$$


For all $0\le i\le I$,


$$
0\le\rho+i<L,
$$


so $e_{\rho+i}$ is a literal coordinate of the original lower complement.

Since


$$
b=5\Pi+t,
$$


one has over $\mathbb F_3$


$$
(1-y)^b
=
(1-y^\Pi)^5(1-y)^t.
$$


The six macro coefficients of $(1-z)^5$ are


$$
(1,1,1,-1,-1,-1).
\tag{6.4}
$$



For $r=P-1-u-i$, the coefficient in (6.2), with $v=\rho+i$, has index


$$
\kappa-u-\rho-i=4\Pi-1-u-i=r+\Pi.
$$


Using $t<r<P$, the first two and last two macro observations in (6.4) are outside support. The two surviving observations give


$$
\boxed{
(\overline A_4e_{\rho+i})_u
=
-c_{r-\Pi}+c_{r-2\Pi}
=
-c_{2\Pi-1-u-i}+c_{\Pi-1-u-i}.
}
\tag{6.5}
$$



This is a direct multiplication certificate in the actual finite matrix.

### 6.2 The inverse of the upper $3y$ corner

Let $v_\partial$ be the coefficient vector of


$$
V_\partial(y)=y^M(1-y)^c,
\qquad c=2\chi.
\tag{6.6}
$$


Its support is wholly in the original upper complement. Indeed,


$$
M+c=L+3\chi-1<R,
$$


because


$$
R-(M+c)=L+2-4\chi>0
\tag{6.7}
$$


on the retained subwindow.

Since $b+c=2P$ and $\kappa-M=R$, equation (6.2) gives


$$
\begin{aligned}
(\overline A_4v_\partial)_u
&=-[y^{R-u}](1-y)^{2P}\\
&=-[y^{R-u}](1-y^P)^2.
\end{aligned}
$$


For $0\le u\le R<P$, the only possible surviving coefficient is $R-u=0$. Therefore


$$
\boxed{\overline A_4v_\partial=-e_R.}
\tag{6.8}
$$



The corner has not been discarded. It has a nontrivial, explicitly evaluated inverse image.

### Theorem 6.1 — Actual finite inverse application

For every $0\le i\le I$,


$$
\boxed{
\overline A_4^{-1}(C_H)_i
=
e_{\rho+i}+2\mathbf1_{i=I}v_\partial.
}
\tag{6.9}
$$



#### Proof

Equations (6.5) and (6.8) show that multiplication by the actual finite $\overline A_4$ gives exactly (6.3). The original unit theorem makes this inverse image unique. ∎

In coordinates, the certificate is


$$
\boxed{
X_{ui}
=
\mathbf1_{u=\rho+i}
+
2\mathbf1_{i=I}
(-1)^{u-M}\binom{2\chi}{u-M},
}
\tag{6.10}
$$


where the binomial term is zero outside $M\le u\le M+2\chi$. All these coordinates belong to $\mathcal C$.

Equation (6.10) is a symbolic finite certificate. No original-length vector is proposed for construction or execution.

---

## 7. Evaluation of the returned operator and alternating scalar

### 7.1 Moment–moment products

Using (6.3),


$$
(C_H)_j^Te_{\rho+i}
=
-c_{L-i-j}+c_{\rho-i-j}.
\tag{7.1}
$$


The upper corner contributes nothing because $\rho+i<R$.

For every $0\le i,j\le I$,


$$
\rho-i-j-t
\ge \rho-2I-t
=\frac{P+7}{2}-4\chi>0.
\tag{7.2}
$$


Hence both coefficient indices in (7.1) are greater than $t$. Thus


$$
\boxed{(C_H)_j^Te_{\rho+i}=0.}
\tag{7.3}
$$



This is a support evaluation in the actual source, not an appeal to generic isotropy.

### 7.2 Every product with the boundary inverse image

Because


$$
(1-y)^t(1-y)^c=(1-y)^\Pi=1-y^\Pi
$$


over $\mathbb F_3$, the moment part of $(C_H)_j^Tv_\partial$ is


$$
2\mathbf1_{M=\Pi-1-j}
-\mathbf1_{M=2\Pi-1-j}.
\tag{7.4}
$$


The first equality is impossible because


$$
M-(\Pi-1-j)=\rho+\chi+j>0.
$$


The second is impossible because


$$
2\Pi-1-j-M
\ge 2\Pi-1-I-M
=L+3-4\chi>0.
\tag{7.5}
$$


Finally, the corner term is


$$
-2\mathbf1_{j=I}[y^R]V_\partial=0
$$


by the strict degree bound (6.7). Therefore


$$
\boxed{(C_H)_j^Tv_\partial=0.}
\tag{7.6}
$$



### Theorem 7.1 — The full leading first-four return

The actual returned operator is


$$
\boxed{
R_4=C_H^T\overline A_4^{-1}C_H=0
\quad\text{in }\mathbb F_3^{k\times k}.
}
\tag{7.7}
$$



#### Proof

Substitute the evaluated inverse image (6.9). Every resulting moment–moment contraction is zero by (7.3), and every contraction with the retained boundary inverse image is zero by (7.6). ∎

### 7.3 The requested alternating direction

Keep exactly


$$
\varepsilon_{\rm alt}=(-1)^{k-2}.
$$


The actual endpoint cross is


$$
\begin{aligned}
(g_4)_u={}&
-c_{2\Pi-1-u}+c_{\Pi-1-u}\\
&+\varepsilon_{\rm alt}
\left(
-c_{2\Pi-1-u-I}+c_{\Pi-1-u-I}
-2\mathbf1_{u=R}
\right).
\end{aligned}
\tag{7.8}
$$


Its actual finite inverse image is


$$
\boxed{
\overline A_4^{-1}g_4
=
e_\rho+\varepsilon_{\rm alt}e_{\rho+I}
+2\varepsilon_{\rm alt}v_\partial.
}
\tag{7.9}
$$


Equations (7.3) and (7.6) evaluate every contraction in the resulting scalar, giving


$$
\boxed{g_4^T\overline A_4^{-1}g_4=0.}
\tag{7.10}
$$



The two moment supports and upper $3y$ corner have remained throughout the calculation. In particular, the corner is responsible for the final term in (7.9), even though its completed return is zero.

---

## 8. Physical-$6$ assembly in the unchanged common pivot frame

The new result removes $R_4$ from the leading core assembly:


$$
\boxed{
C_6=C^{\rm mom}-(e_I\eta^T+\eta e_I^T)
\pmod3,
}
\tag{8.1}
$$


where


$$
C^{\rm mom}_{ij}=c_{\kappa_2-i-j},
\qquad
\kappa_2=\frac{P/9-1}{2}.
$$



The physical first-four return is obtained from cross scale $3^5$ and inverse scale $3^{-4}$, hence has multiplier $3^6$. Equation (7.7) proves that this physical-$6$ contribution vanishes. It does not evaluate its physical-$7$ digit.

Let


$$
\bar\gamma=(\sigma2^t)^{-1}\in\mathbb F_3,
\qquad \sigma=(-1)^{R_*+L},
$$


and let $N$ have columns $e_j+e_{j+1}$, $0\le j\le k-2$. Retain


$$
h=N^T\eta,\qquad e'=e_{k-2}.
$$



At the two parent-reviewed endpoint conclusions,


$$
\eta_0=\eta_I=0,
\tag{8.2}
$$


with the separate review statuses stated in Section 1, one obtains


$$
\boxed{
a_6=0,\qquad
w_6=\bar\gamma N^TC^{\rm mom}e_0,
}
\tag{8.3}
$$




$$
\boxed{
B_6=N^TC^{\rm mom}N-(e'h^T+he'^T).
}
\tag{8.4}
$$


In coordinates,


$$
(w_6)_i
=
\bar\gamma(c_{\kappa_2-i}+c_{\kappa_2-i-1}),
\tag{8.5}
$$




$$
\boxed{
\begin{aligned}
(B_6)_{ij}
={}&c_{\kappa_2-i-j}
+2c_{\kappa_2-i-j-1}
+c_{\kappa_2-i-j-2}\\
&-\mathbf1_{i=k-2}h_j-h_i\mathbf1_{j=k-2}.
\end{aligned}
}
\tag{8.6}
$$



These formulas retain the unknown interior terminal coordinates.

### 8.1 The alternating scalar is now actually paid

Let


$$
z_{\rm alt}=(1,-1,\ldots,(-1)^{k-2})^T.
$$


Then


$$
Nz_{\rm alt}=e_0+\varepsilon_{\rm alt}e_I,
\qquad z_{\rm alt}^Th=0.
\tag{8.7}
$$



Since $243\mid t$, the polynomial $(1-y)^t$ over $\mathbb F_3$ is supported on exponents divisible by $243$. Meanwhile,


$$
\kappa_2\equiv121,\quad
\kappa_2-I\equiv123,\quad
\kappa_2-2I\equiv125\pmod{243}.
$$


Thus the endpoint moment block is zero.

Turn 19’s unevaluated scalar therefore becomes the evaluated statement


$$
\boxed{
z_{\rm alt}^TB_6z_{\rm alt}=0,
\qquad
z_{\rm alt}^Tw_6=0
}
\tag{8.8}
$$


at the leading core precision and the endpoint status (8.2).

### 8.2 The whole directional equation still contains $h$

The full directional law is


$$
\boxed{
B_6z_{\rm alt}
=
N^TC^{\rm mom}(e_0+\varepsilon_{\rm alt}e_I)
-\varepsilon_{\rm alt}h.
}
\tag{8.9}
$$


The quadratic zero in (8.8) does not make the right-hand side zero.

In particular,


$$
z_{\rm alt}\in\ker\overline B_6
$$


would require the additional source-specific identity


$$
\boxed{
h=
\varepsilon_{\rm alt}
N^TC^{\rm mom}(e_0+\varepsilon_{\rm alt}e_I).
}
\tag{8.10}
$$


Equation $z_{\rm alt}^Th=0$ is only one scalar constraint and does not imply (8.10).

Even if (8.10) were proved, the allowed equation


$$
B_6x=w_6,\qquad x\in3^{-1}\mathbb Z_3^{k-1},
$$


would still need a next-digit payment. Writing $z=3x=z_0+3z_1$, one needs


$$
\overline B_6\overline z_0=0,
$$


and then


$$
\overline B_6\overline z_1
+
\overline{B_6\widehat z_0/3}
=
\overline w_6.
\tag{8.11}
$$


The second equation depends on the actual whole $B_6\bmod9$. That information is not supplied by the leading return evaluation.

---

## 9. A concrete follow-on terminal-direction lemma

The new first-four obstruction is closed. The next alternating-direction obstruction can now be stated without an unknown first-four term.

Retain the complete polynomial


$$
\begin{aligned}
\Omega_P(y)={}&
(1-y)^{2P}(y^{122P}+3y^{41P})\\
&+9(1+y^P+y^{2P})
(2y^{14P}+2y^{41P}+2y^{95P}-y^{131P}).
\end{aligned}
\tag{9.1}
$$


It retains all fourteen terms and both source channels.

Let


$$
F_T=F[y^{\nu-1}],
\qquad a=\overline B_{\ell,\tau-1}\ne0.
$$


The independently validated residual interface, applied linearly, gives


$$
\boxed{
a h_i
=
-\frac{
G_c\!\left(
F_T,\,
F[\Omega_P(1-y)^t y^i(1+y)]
\right)
}{3^{29}}
\pmod3,
\quad 0\le i\le I-1.
}
\tag{9.2}
$$


The whole numerator is integral at the displayed normalization by the inherited interface. The physical terminal and complete $W$-projection remain in (9.2).

A concrete next lemma is therefore:

> **Terminal-direction defect lemma.**  
> Evaluate, on the same original indices,
> 

$$
> h_i-\varepsilon_{\rm alt}
> \left(
> c_{\kappa_2-i}+c_{\kappa_2-i-1}
> +\varepsilon_{\rm alt}
> (c_{\kappa_2-I-i}+c_{\kappa_2-I-i-1})
> \right)
>
$$


> using the complete source (9.2), modulo $3$.

Its vanishing would prove (8.10). Its nonvanishing would identify precisely why this alternating vector fails even the leading kernel condition.

No bare interior cancellation is assumed in proposing this lemma. In particular, the endpoint bare theorem is not extended to all interior indices merely by changing an exponent.

A subsequent paid lift would still require the actual next digit, including actual/core transport, all newly active complementary returns, the higher endpoint adaptation, and source precision $34$.

---

## 10. Exact division and precision ledger

| Quantity | Division or inverse payment | Information used or required |
|---|---:|---|
| Complete $W$-projection | $E_c^{-1}\in3^{-1}M(\mathbb Z_3)$ | Retained in $F[p]$; covered by admitted complete compression only at its stated scope |
| Prefix $\mathsf A\bmod9$ | Raw pairing divided by $3^{26}$ | Whole raw pairing modulo $3^{28}$ |
| $d_u,d_H\bmod9$ | Raw pairing divided by $3^{28}$ | Whole raw source modulo $3^{30}$ |
| Dominant source term in (4.3) | Division by $9$ | Whole numerator modulo $81$, paid by (4.6)–(4.11) |
| Mixed-prefix digit $P_{ui}$ | Further division by $3$ | Entire contraction modulo $9$, evaluated as zero |
| Leading-source contribution $S_{00}$ | Its next digit cannot be inferred from its leading zero | Each of the three coefficients in (5.4) proved zero modulo $9$ |
| Source corrections $S_{01},S_{10}$ | Each has explicit factor $3$ | Complete finite coefficient contractions evaluated modulo $3$ |
| Prefix inverse correction | Explicit factor $3$ in (3.7) | All three actual finite shifted contractions evaluated in (5.19) |
| Direct first-four mixed moment | Raw source divided by $3^{31}$ | Reused whole-source formula at its stated precision |
| Physical first-four inverse | $3^{-4}\overline A_4^{-1}$ | Actual finite complement retained |
| Physical first-four return | $3^5\cdot3^{-4}\cdot3^5=3^6$ | Its leading normalized operator is zero; physical-$7$ digit not evaluated |
| Endpoint residue | Division by $3^{29}$ | Complete numerator modulo $3^{30}$, reused at stated review scope |
| Allowed directional $3^{-1}$ | $z=3x$ | Requires the whole next equation (8.11), not only $\overline B_6$ |

The diagonal force payments remain separate:


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
\tag{10.1}
$$


The evaluated $C_H$-return does not evaluate the different force contraction involving $f_C$. No unit numerator is assumed.

---

## 11. Actual producer, complete forcing, and later source precision

The new theorem concerns the complete core. The actual producer remains


$$
\boxed{Q_{\rm act}=Q_c+3^7\mathscr R.}
\tag{11.1}
$$



Retain the original definitions, with their original existence and denominator hypotheses:


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
\xi=
\frac{u^Tt_{\rm force}}{F_{\rm fac}^2-u^Tv}.
$$


The complete correction is still


$$
[x^a](3^7\mathscr R)
=
-\frac{F_{\rm fac}}{a!}
\bigl((t_{\rm force})_a+\xi v_a\bigr),
\qquad 0\le a\le n-1,
$$




$$
\mathscr R(-1)=-\frac{\xi F_{\rm fac}^2}{3^7}.
\tag{11.2}
$$



The full forcing/return identity remains


$$
\boxed{
J^T\boldsymbol\varepsilon+\omega
=
-\boldsymbol\varepsilon
-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
}
\tag{11.3}
$$


Neither forcing term is removed.

The complete moment recurrence remains


$$
\mu_{r+1}+\mu_r
=
\frac{3^h}{2r+1}
-\frac{3^h}{4}\bigl((2r+2)!+(2r)!\bigr),
\qquad 0\le r\le2n-2.
\tag{11.4}
$$


The designated shifted index


$$
r_*=\frac{3^h-5}{2}
$$


is retained. In the recurrence as printed, the pole $2r+1=3^h$ occurs at $r=r_*+2$, not at $r_*$.

The factorial part was handled only through the admitted local complete-source precision. It has not been removed from the actual producer, forcing, determinant, or real error.

The following remain separate:

- actual/core transport at physical $7$;
- physical-$5$ complementary and kernel-pivot directional returns;
- the next digits of earlier returns, now including the first-four return;
- higher endpoint adaptation;
- the stationary contribution at source precision $34$;
- the separate higher ternary theorem assigned under A3 Turn 20.

No status for that separate higher theorem is inferred from the present calculation.

---

## 12. Actual contents, least simultaneous clearer, final gcd, and whole error

No actual integer column content is evaluated by the new local zero. The original complete columns and their original contents are unchanged.

The least simultaneous clearer remains the actual $\ell_{\rm clr}$, not a convenient common multiple and not a power of $3$. Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,
\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the final gcd over **all primes**


$$
\boxed{G=\gcd(|A_\ell|,|B_\ell|).}
\tag{12.1}
$$


For $B_\ell\ne0$, the actual primitive pair is


$$
\boxed{
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{G},
\qquad
q=\frac{|B_\ell|}{G}.
}
\tag{12.2}
$$



The whole evaluated error remains exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
G\det H_{\rm complete}.
}
\tag{12.3}
$$


Its positive magnitude, when the determinant is nonzero, is


$$
\boxed{
|q(e+\pi)-p|
=
\frac{\ell_{\rm clr}^{m+1}}G
|\det H_{\rm complete}|>0.
}
\tag{12.4}
$$



An irrationality proof would still require, at the **same infinite original indices**,


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
\tag{12.5}
$$


These conditions would make the nonzero whole errors tend to zero. If $e+\pi=a/b$ were rational, every nonzero integer linear error would have absolute value at least $1/b$.

The local matrix identity $R_4=0\pmod3$ proves none of the nonvanishing, actual-content, least-clearer, all-prime gcd, or real-decay requirements in (12.5). It yields no primitive denominator saving by itself.

---

## 13. Bounded exact-arithmetic verification

No tools or numerical execution were used. No new arithmetic execution is indispensable to the proof.

A coordinator-authored **auxiliary check of the new carry constants only** can have the following fixed inputs:

1. The integers
   

$$
\binom9a\quad(0\le a\le9),\qquad
   (-1)^a\binom{10}{a}\quad(0\le a\le10).
$$


2. The offsets $s=0,\ldots,4$, and the unit denominators $5,7,11,35$, in $\mathbb Z/9\mathbb Z$.
3. For $s=1,\ldots,4$, the four denominators
   

$$
2s+9,\quad2s+11,\quad2s+27,\quad2s+29,
$$


   omitting multiples of $3$.
4. The six fixed binomial coefficients
   

$$
\binom{74+v}{v},
   \qquad
   v\in\{37,38,118,119,280,281\},
$$


   reduced modulo $9$.
5. The two fixed polynomials
   

$$
(1-Z)^5,\qquad (1-Z)(1+Z+Z^3)^2
$$


   over $\mathbb F_3$.

The expected verifiable outputs are:

- the whole-numerator coefficients
  

$$
(-9,36,-81,99,-18);
$$


- the macro source digits
  

$$
(D(Q),D(2Q),D(3Q),D(4Q))=(5,1,6,5)\pmod9;
$$


- the off-macro coefficients
  

$$
(e_0,e_1,e_2,e_3,e_4)=(2,1,2,2,1)\pmod3;
$$


- four zero values for the unit-$Q$ cancellation;
- six zero binomial residues modulo $9$;
- the coefficient lists
  

$$
(1,1,1,2,2,2)
$$


  for $(1-Z)^5$, and
  

$$
(1,1,2,1,0,1,1,2)
$$


  for $(1-Z)(1+Z+Z^3)^2$.

These inputs are bounded by fixed small degrees and fixed binomial tops at most $355$. They contain no original $P$- or $H$-length matrix, vector, inverse, solve, source table, or generic first-four scan.

Such a finite check verifies only these constants. The uniform theorem rests on the symbolic finite-boundary and carry proofs above.

---

## 14. Consolidated proof-status ledger

| Item | Status |
|---|---|
| Original progression and certified subwindow infinitude | Reused unchanged |
| Complete corrected-pairing compression through source $33$ | Reused only for admitted ordinary polynomial parts |
| Original prefix inverse and normalized prefix matrix modulo $9$ | Reused with their literal finite boundaries |
| A1 Turn 18 terminal module and A1 Turn 13 endpoint interface | DIFFERENT-passed through supplied A3 Turn 19 |
| A1 Turn 19 complementary source return, $\eta_I=0$ | Favorable parent review; separate DIFFERENT review pending |
| A3 Turn 19 new complete $\eta_0$ LOW-return lemma | Favorable parent review; stated A4 Turn 24 audit pending |
| New two-digit amplitude source formula | Proved here |
| New mixed-prefix numerator modulo $9$ | Evaluated as zero here |
| Actual $P_{u,0},P_{u,I}$ | Evaluated as zero here |
| Stronger $P_{ui}$ for all original $u,i$ | Evaluated as zero here |
| Actual finite $A_4^{-1}C_H$ | Explicit original-coordinate certificate proved here |
| Whole leading $R_4$ | Evaluated as zero here |
| Alternating first-four scalar | Evaluated as zero here |
| Leading physical-$6$ assembly | Given with the full unknown $h=N^T\eta$ retained |
| Interior terminal-direction defect | Open, with source-specific follow-on lemma (9.2) |
| Paid $3^{-1}$ directional lift | Open; actual next digit required |
| Actual physical $7$/source $34$ | Open in this report |
| Separate A3 Turn 20 higher ternary theorem | Outside this proof and its status claims |
| Actual contents, least clearer, all-prime $G$, primitive $q$ | Not evaluated |
| Same-index nonzero whole error and decay | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

---

## Conclusion

The actual first-four mixed-prefix obligation is now evaluated, rather than replaced by a leading zero or by the already closed second-kernel quadratic.

The new complete payment is


$$
\boxed{
d_u^T\mathsf A^{-1}d_H{}_i\in9\mathbb Z_3,
\qquad P_{ui}=0.
}
$$


Its proof includes:

- the complete corrected columns;
- all visible pole layers at the needed precision;
- the $3y$ source correction;
- the whole dominant numerator modulo $81$ before division by $9$;
- the next digit of the leading-source contraction;
- both first-order source corrections;
- the actual finite shifted prefix inverse correction.

The actual first-four inverse is then certified directly:


$$
\boxed{
\overline A_4^{-1}(C_H)_i
=
e_{\rho+i}+2\mathbf1_{i=I}v_\partial,
\qquad
V_\partial(y)=y^{L+\chi-1}(1-y)^{2\chi}.
}
$$


This retains the upper $3y$ corner in its inverse image and proves the stronger operator law


$$
\boxed{R_4=0\pmod3.}
$$



Accordingly, the alternating scalar from Turn 19 is zero at its required leading scope. But the full direction remains


$$
B_6z_{\rm alt}
=
N^TC^{\rm mom}(e_0+\varepsilon_{\rm alt}e_I)
-\varepsilon_{\rm alt}h,
$$


with the interior terminal coordinates still present. The precise next local bottleneck is the source-specific evaluation of this terminal-direction defect, followed by the complete next-digit payment for the allowed $3^{-1}$ lift.

The global bottleneck remains the actual all-prime primitive normalization and a nonzero whole error tending to zero at the same infinite original indices.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi\text{ follows.}}
$$


