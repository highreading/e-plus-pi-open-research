> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A source-specific reduction of the rank-$b$ return to one finite terminal vector

## Abstract and proof status

The rationality or irrationality of $e+\pi$ remains unresolved.

This report reuses, without repeating their calculations:

- the accepted complete $J6$ audit from Turn 11;
- the independently passed prefix-$6$ vanishing;
- the complete-core moment formula through source precision $33$;
- the second-kernel-pivot synchronization and payment;
- the certified infinitude of the original indices in
  

$$
\frac3{25}<\frac{\chi}{P}<\frac{31}{250}.
$$



The main new result is an explicit evaluation of the **nonterminal part of the actual normalized rank-$b$ coupling**, together with its actual finite inverse images. It reduces the entire rank-$b$ return to a single, precisely specified terminal vector.

Put


$$
\Pi=P/3,\qquad c=2\chi,\qquad t=\Pi-c,\qquad
k=3\chi-\Pi-1,
$$


and let


$$
H_i=(1-y)^\Pi y^{L_*+i},\qquad L_*=(P-1)/2,\qquad 0\le i<k.
$$


There is a definite vector


$$
\eta=(\eta_0,\ldots,\eta_{k-1})^T\in\mathbb F_3^k,
$$


defined below from the **actual finite last row of the original normalized $J$-block**, for which


$$
\boxed{
\left(\frac{M_b\mathscr H}{3}\right)^T
A_b^{-1}
\left(\frac{M_b\mathscr H}{3}\right)
=
e_{k-1}\eta^T+\eta e_{k-1}^T
\quad\text{in }\mathbb F_3.
}
\tag{0.1}
$$


Here $\mathscr H$ is the literal integer coefficient matrix of the $H_i$, and $A_b$ is the original unit normalized block, with its physical $3^{-2}$ inverse payment retained.

This is substantially more specific than an unevaluated Schur contraction:

1. the direct complete-source coupling consists of two evaluated anti-diagonals;
2. its mixed prefix correction is proved zero;
3. its mixed interior $J$-correction is proved zero;
4. its finite inverse images are explicitly computed;
5. their mutual quadratic products are proved zero;
6. the only remaining contribution is the displayed terminal vector, and
   

$$
\boxed{\text{the rank-\(b\) return vanishes if and only if }\eta=0.}
   \tag{0.2}
$$



However, the supplied excerpts do not evaluate this particular terminal inverse-coordinate vector. I do **not** infer its vanishing from the already closed $J$-quadratic. Consequently, the primary return is reduced sharply but is not declared completely evaluated.

For the first physical-$4$ complement, I also identify the remaining source-specific mixed-prefix digit after evaluating its direct moment coupling and disposing of its leading $J$-coupling. Its quadratic return remains open.

No computation was performed. Section 10 specifies a new bounded terminal-vector calculation, using only already formed finite boundary data, which would decide (0.1) at one certified original index without rerunning a prefix or $J$ audit.

---

## 1. Original domain, finite objects, and accepted reuse

### 1.1 The original indices

All assertions below concern sufficiently large original indices satisfying


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




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


The original arithmetic parameters remain


$$
P_0=243P=3^{h-27},\qquad N_0=243r,\qquad D=P_0+N_0,
$$




$$
P=3^{h-32},\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$




$$
4^j=243(3^{26}-1)P-243r+1.
$$


Set


$$
x=y-1,\qquad Q=27P,\qquad b=Q-N_0=2R,\qquad \chi=P-R.
$$


Thus


$$
N_0=25P+2\chi,\qquad D=10Q-b.
$$



The subwindow used here is exactly


$$
\boxed{\frac3{25}<\frac{\chi}{P}<\frac{31}{250}.}
\tag{1.1}
$$


The supplied density deduction, based on the earlier original-progression rotation theorem, proves that this contains infinitely many original tuples. It does not authorize choosing $P,\chi$ independently.

On this subwindow,


$$
\delta=\chi-1,\qquad
t=\Pi-2\chi,\qquad
k=\delta-t=3\chi-\Pi-1>0.
$$


In particular,


$$
\frac{32P}{375}<t<\frac{7P}{75}.
$$


After removing a finite initial segment, $k\ge2$.

The literal amplitudes satisfy


$$
\deg H_i=L_*+\Pi+i.
$$


At the upper index,


$$
R-\deg H_{k-1}
=\frac{P+5}{2}-4\chi>0.
\tag{1.2}
$$


Thus every $H_i$ is an admitted amplitude of degree at most $R$.

The amplitude parameter $\chi=(243r-25P)/2$ retains its established valuation $5$. The separately closed scalar-unit receipt mentioned in the coordinator update is not used to change this amplitude arithmetic or to supply a missing matrix residue.

### 1.2 Complete finite columns and the physical terminal

Retain


$$
U_s=x^s\quad(0\le s<D),
$$




$$
z_i=x^Dy^i\quad(0\le i<\nu),\qquad \nu=D/2-1,
$$




$$
Y_t=y^t\quad(d\le t\le m),\qquad d=D+\nu,\qquad W=[U\ Y].
$$


The physical HIGH terminal is $Y_m$.

The complete functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad \mathfrak f(y^a)=(2a)!.
$$


Its physical cutoff is


$$
K_{\rm phys}=2n-2=2H-2D+2,
$$


and


$$
2K_{\rm phys}+1=4H-4D+5<3^{h+1}.
$$



For


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A,
$$


write


$$
G_c(f,g)=\mathcal M(Q_cfg),
$$




$$
E_c=G_c(W,W),\qquad
F[p]=x^Dp-WE_c^{-1}G_c(W,x^Dp).
$$


These are the complete corrected columns.

The finite prefix and tail boundaries remain


$$
R_*=\frac{9Q+1}{2},\qquad a_0=R_*-1,
$$




$$
\tau=\frac{N_0-3}{2},\qquad \ell=3R+1,
$$




$$
K=\{0,\ldots,3R\},\qquad
J=\{\ell,\ldots,\tau-1\},
$$




$$
N_J=\tau-\ell,\qquad R_*+\tau=\nu.
\tag{1.3}
$$



The last $J$-column is the actual column $F[y^{\nu-1}]$. It is not brought into the ordinary compression theorem.

### 1.3 Accepted inputs, at their exact scope

The following are reused.

1. **Complete corrected-pairing compression.** For admitted polynomial parts of degree at most $\nu-2$,
   

$$
G_c(F[p_1],F[p_2])
   \equiv
   K_N\mathcal J_h\!\left(x^D(\beta+3y)p_1p_2\right)
   \pmod{3^{33}},
   \tag{1.4}
$$


   with $K_N\equiv\beta\equiv1\pmod3$, and the original physical support retained.

2. **Finite prefix inverse.** With
   

$$
U(y)=(1-y)^{N_0},\qquad
   (A_0)_{pq}=U_{a_0-p-q},
$$


   one has
   

$$
(A_0^{-1})_{pq}=[y^{p+q-a_0}]U^{-1},
   \qquad 0\le p,q\le a_0.
   \tag{1.5}
$$


   Also $\overline{\mathsf A}=\overline{A_0}$.

3. **Leading interior $J$-coupling and finite inverse.** These are used below with their actual interior bounds. No extrapolation to the last row is made.

4. **Closed sixth-digit returns.**
   

$$
\text{prefix contribution at physical \(6\)}=0,
$$


   

$$
\text{terminal-aware \(J\)-quadratic contribution at physical \(6\)}=0.
   \tag{1.6}
$$


   Neither calculation is repeated.

5. **Moment contribution on the second kernel.**
   

$$
C^{\rm mom}_{ij}
   =[y^{\kappa_2-i-j}](1-y)^t,
   \qquad
   \kappa_2=\frac{P/9-1}{2}.
   \tag{1.7}
$$


   The residues $2$ and $-1$ in the two independently matched source derivations are the same element of $\mathbb F_3$.

6. **Frame and payment results.** The specified common second-kernel-pivot frames agree for actual and core matrices, including the mixed pivot column, modulo $3^7$. The physical-$5$ complement returns begin at $7$ in both the matrix and kernel-pivot directional channels.

No characteristic-zero determinant result, one-sided dilated determinant, or reopened abstract supplies any of the finite ternary residues calculated here.

---

## 2. The original normalized rank-$b$ coupling

Introduce ordinary one-lift columns


$$
V_u
=
F\!\left[y^{k_0+u}(y^{3Q}+3)\right],
\qquad
k_0=\frac{3Q+1}{2},
\qquad 0\le u\le3R.
\tag{2.1}
$$


If $G_0$ denotes multiplication by $x^b=(1-y)^b$, then


$$
V[G_0a]=\mathcal F[a].
$$



Define the ordinary residual matrix


$$
(D_0)_{pu}=\frac{G_c(F[y^p],V_u)}{3^{28}},
\qquad
0\le p\le a_0,\quad 0\le u\le3R.
\tag{2.2}
$$


Its integrality follows from the original first-prefix lift. Put


$$
d_H=D_0G_0\mathscr H,\qquad Z_H=\mathsf A^{-1}d_H.
$$



Let $\mathcal S^{(2)}$ be the original $K$-matrix after the prefix and $J$ returns. With $E_b$ denoting the **prescribed original rank-$b$ complement**, its normalized blocks are


$$
A_b=\frac{E_b^T\mathcal S^{(2)}E_b}{9},
\qquad
M_b=\frac{E_b^T\mathcal S^{(2)}G_0}{27}.
\tag{2.3}
$$


These definitions retain the original physical block $9A_b$, whose inverse costs $3^{-2}$.

The exact coupling identity gives, after the paid division by $81$,


$$
\begin{aligned}
\frac{M_b\mathscr H}{3}
={}&
-E_b^T\frac{G_c(V,\mathcal F[\mathscr H])}{3^{30}}\\
&-E_b^TD_0^T\mathsf A^{-1}d_H
-E_b^TL\,B^{-1}l_H,
\end{aligned}
\tag{2.4}
$$


where


$$
l_H=\frac{L^TG_0\mathscr H}{3}.
\tag{2.5}
$$


The following sections evaluate the three terms in (2.4), except for one exact finite terminal coordinate.

---

## 3. New complete-source evaluation: two anti-diagonals

### Theorem 3.1

For every $0\le u\le3R$ and $0\le i<k$,


$$
\boxed{
\frac{G_c(V_u,\mathcal F[H_i])}{3^{30}}
=
\mathbf1_{u+i=P-1}
-
\mathbf1_{u+i=2\Pi-1}
\pmod3.
}
\tag{3.1}
$$



This assertion includes the literal integer binomial coefficients of $H_i$, the complete correction against $W$, both weighted low terms, and the physical cutoff.

### 3.1 The complete compact polynomial

The polynomial in (1.4) is


$$
\begin{aligned}
B_{ui}(y)
={}&(1-y)^{10Q+\Pi}(\beta+3y)y^{L_*+u+i}\\
&\qquad\cdot
\left(y^{9Q+1}+6y^{6Q+1}+9y^{3Q+1}\right).
\end{aligned}
\tag{3.2}
$$


Since $Q=81\Pi$,


$$
10Q+\Pi=811\Pi.
$$


No replacement of $(1-y)^\Pi$ by $1-y^\Pi$ has been made in (3.2).

Moreover,


$$
u+i\le3R+k-1=8\Pi-2.
\tag{3.3}
$$


The compact degree therefore gives


$$
2\deg B_{ui}+1\le3099\Pi.
$$


For a contribution visible modulo $3^{31}$, the pole denominator must be a multiple of


$$
9P=27\Pi.
$$


Writing it as $27d\Pi$, the complete outer range is


$$
1\le d\le113,\qquad d\ \text{odd}.
\tag{3.4}
$$


An extraction outside the actual coefficient support is zero.

### 3.2 Integer-binomial valuation control

Write $\Pi=3^q$. For $0<l<\Pi$,


$$
\boxed{
v_3\binom{811\Pi}{a\Pi+l}
=
q-v_3(l)+v_3\binom{810}{a}.
}
\tag{3.5}
$$


Indeed,


$$
\binom{811\Pi}{a\Pi+l}
=
\frac{811\Pi}{a\Pi+l}
\binom{811\Pi-1}{a\Pi+l-1},
$$


and the lower $q$ ternary digits of $811\Pi-1$ are all $2$. The remaining carries are exactly those of $\binom{810}{a}$.

At a macro index $a\Pi$, both the valuation and normalized unit modulo $3$ are those of $\binom{811}{a}$. This follows by repeatedly stripping the nonmultiples of $3$ from the factorials; their unit factors cancel in the binomial quotient.

The relevant ternary digits are


$$
811=(1010001)_3,\qquad 810=(1010000)_3.
$$



### 3.3 Exhaustion of the pole layers

At the $27Q$ pole, the high extraction is


$$
363\Pi-1-u-i.
$$


Thus its macro index lies in $355,\ldots,362$. In this interval:

- $\binom{811}{a}$ has valuation at least $4$;
- valuation $4$ occurs only at $a=360,361$;
- $\binom{810}{a}$ has valuation at least $4$.

Consequently all nonmacro coefficients have valuation at least $5$, by (3.5).

The other layers are exhausted as follows.

| Pole layer | Pole weight | Coefficient requirement for order at most $30$ | Actual bound or support |
|---|---:|---:|---|
| $27Q$, high | $3^{26}$ | valuation at most $4$ | only $360\Pi,361\Pi$ |
| $27Q$, middle | $3^{26}\cdot6$ | valuation at most $3$ | macro interval $598,\ldots,605$, valuation at least $4$ |
| $27Q$, low | $3^{26}\cdot9$ | — | outside degree $811\Pi$ |
| $9Q$, low | $3^{27}\cdot9$ | valuation at most $1$ | macro interval $112,\ldots,119$, valuation at least $4$ |
| unit multiples of $3Q$ | $3^{28}$ | valuation at most $2$ | the same intervals, or $355,\ldots,362$, all at least $4$ |
| unit multiples of $Q$ | $3^{29}$ | valuation at most $1$ | macro residue $31,\ldots,38\pmod{81}$, forcing at least two carries |
| unit multiples of $Q/3$ | $3^{30}$ | unit coefficient | macro residue $4,\ldots,11\pmod{27}$, incompatible with the unit digits of $811$ |

The $3y$ term adds a further digit and cannot survive. The middle and low weights have been included in the table rather than discarded in advance.

For the unit-$Q$ row, the lower four ternary digits of $811$ are $0001$, whereas a residue from $31,\ldots,38$ forces at least two borrows. For the final row, a unit coefficient of $(1-y)^{811\Pi}$ must have macro residue $0$ or $1\pmod{27}$, not $4,\ldots,11$.

### 3.4 The two surviving units

The established old high coefficient of


$$
(1-y)^{810\Pi}=(1-y)^{10Q}
$$


at $360\Pi=120P$, divided by $3^4$, is $1\pmod3$. This closed scalar receipt is reused.

Pascal’s identity gives


$$
\binom{811}{360}
=\binom{810}{360}+\binom{810}{359},
$$


where the second term has valuation at least $5$. Similarly,


$$
\binom{811}{361}
=\binom{810}{361}+\binom{810}{360}.
$$


Thus both unsigned normalized units are $1$. Their coefficient signs are opposite because $360\Pi$ is even and $361\Pi$ is odd.

The two conditions are respectively


$$
363\Pi-1-u-i=360\Pi
\quad\Longleftrightarrow\quad u+i=P-1,
$$


and


$$
363\Pi-1-u-i=361\Pi
\quad\Longleftrightarrow\quad u+i=2\Pi-1.
$$


This proves (3.1).

---

## 4. New mixed-prefix calculation: the rank-$b$ correction is zero

This section concerns the **ordinary/second-kernel mixed contraction in (2.4)**. It does not repeat the closed second-kernel quadratic prefix-$6$ audit.

### 4.1 The necessary ordinary residual coefficients

A direct compression at source precision $29$, on the admitted ordinary columns, gives


$$
\boxed{
(D_0)_{pu}
=
\sum_{r=1}^{5}a_r\,U_{rQ-1-p-u}\pmod3,
\qquad
(a_1,\ldots,a_5)=(1,2,1,1,2).
}
\tag{4.1}
$$



Here is the source evaluation.

In the $27Q$ extraction, expand


$$
(1-y)^{9Q}\equiv(1-y^Q)^9\pmod{27}.
$$


The only potentially contributing high bands are $4Q,\ldots,8Q$. Their relevant coefficients, after division by $9$, are


$$
14,\ -14,\ \frac{84-3}{9},\ -4,\ 1.
$$


The subtraction $84-3$ includes the weighted low term at the same extraction. Its quotient is $9$, hence zero modulo $3$.

The $9Q$ pole adds the coefficient $1$ at $3Q-1-p-u$. The unit-$3Q$ contributions at the matching $3Q$ observation cancel between the two physical poles with denominator units $5$ and $11$. The remaining observations are outside the support of $U$. The $3y$ terms are one digit deeper.

This gives exactly (4.1), in the order $Q,2Q,\ldots,5Q$. All exclusions use


$$
0\le p\le a_0,\qquad 0\le u\le3R;
$$


no infinite prefix has been substituted.

### 4.2 The literal contracted residual and its finite inverse image

Since


$$
U(1-y)^b=(1-y)^Q,
$$


contracting (4.1) with $G_0H_i$, only after the source division has been paid, gives


$$
\boxed{
(d_H)_{p i}
=
\sum_{j\in\{1,2,4\}}\alpha_j
\left(
\mathbf1_{p+L_*+i+1=jQ}
-
\mathbf1_{p+L_*+i+\Pi+1=jQ}
\right)
}
\tag{4.2}
$$


in $\mathbb F_3$, where


$$
(\alpha_1,\alpha_2,\alpha_4)=(2,1,2).
$$


The possible $0Q$ and $5Q$ observations are outside the actual prefix interval.

Define


$$
f(y)=U^{-1}(1-y)^\Pi=(1-y)^{t-25P}.
$$


Modulo $3$,


$$
\boxed{
f(y)=
\frac{(1-y)^t(1+y^P+y^{2P})}{1-y^Q}.
}
\tag{4.3}
$$


The exact finite inverse (1.5) therefore gives


$$
\boxed{
(Z_H)_{p i}
=
\sum_{j\in\{1,2,4\}}\alpha_j
[y^{p+jQ-122P-i}]f(y)
\pmod3.
}
\tag{4.4}
$$



This is an evaluated finite inverse image. In particular, its support satisfies


$$
\boxed{
(Z_H)_{p i}=0\qquad\text{for }p>97P+i+t.
}
\tag{4.5}
$$


To check the upper boundary explicitly:

- for $j=1$, only the $0,P,2P$ bands of $f$ fit;
- for $j=2$, only those bands and their $Q$-translate fit;
- for $j=4$, only their translates by $0,Q,2Q,3Q$ fit.

All give the same largest possible row $97P+i+t$. The next translate is beyond $a_0$.

### 4.3 Evaluation of the mixed contraction

For $r=1,\ldots,4$, set


$$
q_r(u)=a_0-rQ+1+u.
$$


These indices lie in the actual prefix. Consequently


$$
\sum_{p=0}^{a_0}U_{rQ-1-p-u}(Z_H)_{pi}
=(d_H)_{q_r(u),i}.
$$


This is zero. Indeed, a nonzero term would require a multiple of $Q=27P$ to lie strictly between $122P$ and $125P$, which is impossible.

For the fifth term in (4.1), a nonzero $U$-coefficient requires


$$
p\ge5Q-1-u-N_0
\ge107P+\chi-1.
$$


But (4.5), together with $i+t\le\chi-2$, gives


$$
p\le97P+\chi-2.
$$


The two finite supports are separated by more than $10P$.

Thus every term is zero, and


$$
\boxed{
D_0^T\mathsf A^{-1}d_H=0\pmod3.
}
\tag{4.6}
$$


This closes the mixed-prefix term in the normalized rank-$b$ coupling.

---

## 5. The actual finite $J$-inverse image and its one remaining coordinate

Put


$$
\kappa_b=\frac{Q-3}{2},\qquad
S_J=\tau+\ell-1=\kappa_b+b.
$$



### 5.1 Evaluated interior coupling and inverse image

The accepted interior source formula specializes to


$$
(l_H)_{v i}
=
-\mathbf1_{v+i=4P-1}
+\mathbf1_{v+i=4P-\Pi-1},
\qquad \ell\le v\le\tau-2.
\tag{5.1}
$$


In particular, its first $J$-coordinate $v=\ell$ is zero.

In absolute $J$-indices, the finite interior inverse is


$$
(B_I^{-1})_{vw}
=
-[y^{S_J-v-w}]U^{-1},
\qquad \ell+1\le v,w\le\tau-2.
$$


Define


$$
J_i=\frac{23P-1}{2}+t+i.
$$


Then the interior inverse image is exactly


$$
\boxed{
(B^{-1}l_H)_{v i}
=
-[y^{J_i-v}]f(y),
\qquad \ell+1\le v\le\tau-2,
}
\tag{5.2}
$$


where $f$ is (4.3).

Because all these coefficient indices are below $Q$, (5.2) becomes


$$
\boxed{
(B^{-1}l_H)_{v i}
=
-\sum_{q=0}^{2}c_{J_i-v-qP},
\qquad
c_d=[y^d](1-y)^t.
}
\tag{5.3}
$$


Every coefficient $c_d$ is zero outside $0\le d\le t$, and inside that interval is evaluated by Lucas’s rule.

The support is therefore


$$
\boxed{
\frac{19P-1}{2}+i
\le v\le
\frac{23P-1}{2}+t+i,
}
\tag{5.4}
$$


which lies strictly inside the actual $J$-interior.

### 5.2 The actual border is retained

Write the actual leading finite block, ordered as first, interior, last, as


$$
\overline B=
\begin{pmatrix}
0&0&a\\
0&B_I&w\\
a&w^T&c_\partial
\end{pmatrix},
\qquad a\ne0.
\tag{5.5}
$$


Let


$$
\theta_i=(\overline{l_H})_{\tau-1,i}.
$$


Then the complete inverse image is


$$
\boxed{
\overline B^{-1}\overline{l_H{}_i}
=
\begin{pmatrix}
\eta_i\\[1mm]
-\bigl([y^{J_i-v}]f\bigr)_{\ell+1\le v\le\tau-2}\\[1mm]
0
\end{pmatrix},
}
\tag{5.6}
$$


where the exact remaining coordinate is


$$
\boxed{
\eta_i
=
a^{-1}\left(
\theta_i+
\sum_{v=\ell+1}^{\tau-2}
w_v[y^{J_i-v}]f(y)
\right).
}
\tag{5.7}
$$



Only the three finite bands in (5.3) contribute to this sum. Formula (5.7) does not replace the actual last row by a compressed or virtual row.

### 5.3 The mixed interior $J$-return is zero

A source calculation at the original normalization gives, for all $u\in K$ and all admitted interior $v$,


$$
\overline L_{uv}=U_{\kappa_b-u-v}.
\tag{5.8}
$$


The sign is important: the complete source pairing divided by $3^{28}$ is $2U_{\kappa_b-u-v}$, and the normalized matrix has the negative Gram sign, so $-2=1$.

Using $U_a=-U_{N_0-a}$, the interior mixed contraction is a full coefficient convolution:


$$
\begin{aligned}
&\sum_{v=\ell+1}^{\tau-2}
U_{\kappa_b-u-v}\left(-[y^{J_i-v}]f\right)\\
&\qquad=
[y^{N_0-\kappa_b+u+J_i}]\,U(y)f(y).
\end{aligned}
$$


The finite support (5.4) validates this completion. Its coefficient index is


$$
N_0-\kappa_b+u+J_i
=23P+\Pi+1+u+i.
$$


It lies strictly between $\Pi$ and $Q$, whereas


$$
Uf=(1-y)^\Pi.
$$


Hence the coefficient is zero.

Therefore


$$
\boxed{
\overline{LB^{-1}l_H{}_i}
=
\eta_i\,v_\ell,
\qquad
(v_\ell)_u=U_{\kappa_b-u-\ell}.
}
\tag{5.9}
$$



Combining Sections 3–5 gives the actual normalized coupling:


$$
\boxed{
\frac{M_b\mathscr H_i}{3}
=
-E_b^T(v_i+\eta_i v_\ell)\pmod3,
}
\tag{5.10}
$$


where


$$
\boxed{
(v_i)_u
=
\mathbf1_{u+i=P-1}
-
\mathbf1_{u+i=2\Pi-1}.
}
\tag{5.11}
$$



Everything in (5.10) has now been evaluated except the actual terminal vector (5.7).

---

## 6. Actual rank-$b$ inverse images and the returned bilinear form

### 6.1 Validation of the original normalized block

The same complete-source calculation at physical order $2$ gives


$$
\boxed{
\overline{\mathcal S^{(2)}/9}(f,g)
=
[y^{\kappa_b}](1-y)^{Q-b}f(y)g(y)
}
\tag{6.1}
$$


on the original $K$-space.

The prefix return begins at $4$, and the $J$-return begins at $3$, so neither changes this leading normalized block. Its kernel is the accepted original subspace


$$
(1-y)^b\mathbb F_3[y]_{\le R}.
$$


Thus the original $A_b$ is precisely the restriction of (6.1) to its prescribed finite complement.

The following quotient calculation computes the inverse action of that same form. It is not a substitution of a differently adapted physical inverse.

### 6.2 A finite quotient model with an explicit coordinate certificate

Put $X=y-1$ and work in


$$
\mathcal Q_b=\mathbb F_3[X]/(X^b).
$$


For representatives of degree below $b$, (6.1) is


$$
\boxed{
\mathcal A(f,g)
=
[X^{b-1}]
\left(-(1+X)^{-\kappa_b-1}\right)f(X)g(X).
}
\tag{6.2}
$$


To verify it, test $f=X^r,g=X^s$. For $r+s\ge b$, both sides vanish. Otherwise the coefficient is


$$
(-1)^{r+s}
\binom{\kappa_b+b-r-s-1}{b-r-s-1},
$$


which is exactly the coefficient supplied by (6.2), since $b$ is even.

The weight in (6.2) has unit constant coefficient $-1$, so this is a nondegenerate finite form.

To express an inverse image in the original $A_b$-coordinates, take its displayed class in $\mathcal Q_b$, and express that class in the images of the original columns of $E_b$. Equivalently, solve the finite decomposition


$$
q=E_bx+G_0z.
\tag{6.3}
$$


The original complement theorem makes this decomposition unique. Then $x$ is the actual normalized inverse image. This provides a matrix-times-vector certificate in the original block without altering its physical normalization.

### 6.3 Inverse image of the two-anti-diagonal coupling

Let


$$
d_i=P-1-i.
$$


The covector $v_i$ acts by


$$
v_i(f)=[y^{d_i}](1-y^\Pi)f(y).
\tag{6.4}
$$


It annihilates the original radical: for $\deg a\le R$,


$$
v_i((1-y)^ba)
=[y^{d_i}](1-y)^{2P+t}a=0\pmod3,
$$


because $d_i<P$ and


$$
\deg((1-y)^ta)\le R+t=P-k-1<d_i.
$$



Its coefficient-dual polynomial in $\mathcal Q_b$ is


$$
\nu_i(X)=X^t(1+X)^{-P+i}.
\tag{6.5}
$$


For completeness, this follows from the finite identity


$$
\sum_{r=0}^{b-1}(y-1)^rX^{b-1-r}
=\frac{(y-1)^b-X^b}{y-1-X}.
$$


After multiplying by $1-y^\Pi$, extracting $y^{d_i}$, and reducing modulo $X^b$, the numerator becomes $(1-y)^t$ in the relevant range $d_i<P$. Since $t$ is odd, the result is (6.5).

Multiplication by the inverse weight in (6.2) gives


$$
\boxed{
q_i(X)
=
-X^t(1+X)^{(25P-1)/2+i}\pmod{X^b}.
}
\tag{6.6}
$$


Thus its literal finite coefficients are


$$
-[X^{t+r}]q_i
=
\binom{(25P-1)/2+i}{r},
\qquad 0\le r<b-t,
$$


with the sign interpreted as in (6.6). These binomial residues are individually Lucas-evaluable.

The inverse image of $v_\ell$ is


$$
\boxed{
q_\ell(X)=(1+X)^\ell\pmod{X^b}.
}
\tag{6.7}
$$


Consequently, the inverse image of the actual coupling in (5.10), before conversion by (6.3), is


$$
\boxed{
X^t(1+X)^{(25P-1)/2+i}
-\eta_i(1+X)^\ell
\pmod{X^b}.
}
\tag{6.8}
$$



### 6.4 Evaluation of every required bilinear product

First,


$$
\begin{aligned}
v_i^T\mathcal A^{-1}v_j
&=
-[X^{b-1-2t}]
(1+X)^{(23P-1)/2+i+j}\\
&=
-\binom{(23P-1)/2+i+j}{4\Pi+c-1}.
\end{aligned}
\tag{6.9}
$$


The lower $\Pi$-block of the upper argument is


$$
\frac{\Pi-1}{2}+i+j.
$$


For $0\le i,j<k$,


$$
\frac{\Pi-1}{2}+i+j-(c-1)
\le4\chi-\frac{P+7}{2}<0.
$$


Both compared lower blocks lie between $0$ and $\Pi-1$. Lucas’s rule therefore forces


$$
\boxed{v_i^T\mathcal A^{-1}v_j=0.}
\tag{6.10}
$$



Next,


$$
v_i^T\mathcal A^{-1}v_\ell
=
\binom{\ell-P+i}{5\Pi-1}.
$$


But


$$
\ell-P+i=(5\Pi-1)-(k-1-i).
$$


Hence


$$
\boxed{
v_i^T\mathcal A^{-1}v_\ell
=\mathbf1_{i=k-1}.
}
\tag{6.11}
$$



Finally,


$$
v_\ell^T\mathcal A^{-1}v_\ell
=U_{\kappa_b-2\ell}.
$$


Its index is


$$
\kappa_b-2\ell
=8P+\left(3c-\frac{P+7}{2}\right),
$$


where the parenthesized residue lies in $[0,c]$ for sufficiently large original indices in (1.1). Since


$$
U=(1-y^P)^{25}(1-y)^c\pmod3
$$


and


$$
\binom{25}{8}=0\pmod3
$$


(the units ternary digit of $8$ exceeds that of $25$),


$$
\boxed{v_\ell^T\mathcal A^{-1}v_\ell=0.}
\tag{6.12}
$$



Equations (5.10) and (6.10)–(6.12) prove the announced result:


$$
\boxed{
R_b:=
\left(\frac{M_b\mathscr H}{3}\right)^T
A_b^{-1}
\left(\frac{M_b\mathscr H}{3}\right)
=
e_{k-1}\eta^T+\eta e_{k-1}^T.
}
\tag{6.13}
$$



Because $2\ne0$ in $\mathbb F_3$, this matrix determines $\eta$: its last off-diagonal row gives $\eta_0,\ldots,\eta_{k-2}$, and its last diagonal entry is $2\eta_{k-1}$. In particular, (0.2) follows.

### 6.5 What is still not evaluated

The exact remaining rank-$b$ obligation is now the following source-specific lemma.

> **Terminal inverse-coordinate lemma.**  
> Evaluate the vector $\eta$ in (5.7), using the actual complete last $J$-row and the actual complete terminal couplings. In particular, prove or disprove
> 

$$
> \eta_i=0\qquad(0\le i<k)
>
$$


> on the certified infinite original subwindow.

The closed $J6$ theorem evaluates a quadratic contraction. Formula (5.6) shows that the first inverse coordinate can remain invisible to its leading quadratic contraction. No supplied statement identifies that coordinate with zero.

This is not a claim that the original objects are undefined: the complete functional determines $\eta$ exactly. It is a claim that its needed value has not been established in the supplied evaluated results or in the derivations above.

---

## 7. The first physical-$4$ complement: a precise remaining mixed digit

The original monomial complement is


$$
\mathcal C
=
\{0,\ldots,R\}\setminus\{L_*,\ldots,L_*+\delta-1\}.
$$


It remains


$$
A_4=E_4^T(T_{c,\rm red}/81)E_4,
\qquad
C_H=\frac{E_4^TT_{c,\rm red}\mathscr H}{3^5}.
\tag{7.1}
$$


Its physical inverse is $3^{-4}A_4^{-1}$.

The accepted leading first form gives the actual leading complementary matrix


$$
\boxed{
(\overline A_4)_{ab}
=
-[y^{\kappa-a-b}](1-y)^b,
\qquad
\kappa=\frac{3P-3}{2},
\qquad a,b\in\mathcal C.
}
\tag{7.2}
$$


Its unit property is the original complete-radical/complement theorem, not a characteristic-zero substitute.

### 7.1 Evaluated direct mixed moment

For $a\in\mathcal C$, put


$$
r_{ai}=P-1-a-i.
$$


The finite bounds give


$$
t+1\le r_{ai}\le P-1.
$$


Using the already established source-$31$ pole decomposition and the integer congruence


$$
(1-y)^{2P}
\equiv
(1-y^P)^2+
6(1-y^P)(-y^\Pi+y^{2\Pi})
\pmod9,
$$


the direct mixed moment is


$$
\boxed{
\frac{G_c(\mathcal F[y^a],\mathcal F[H_i])}{3^{31}}
=
c_{r_{ai}-\Pi}-c_{r_{ai}-2\Pi}
+2\,\mathbf1_{a=R,\ i=k-1}
\pmod3.
}
\tag{7.3}
$$


The last term is the surviving $3y$ observation. Indeed, $r_{ai}-1=t$ occurs only at the displayed upper corner. It must not be removed by the stronger gap available in a double-radical contraction.

The higher integer digits have been used in the division by $3$; only afterward is the residue reduced.

### 7.2 The leading $J$-part of this cross is zero

For a bare amplitude $y^a$, the leading interior $l_a$ is supported at


$$
v=\kappa_0-a,\qquad \kappa_0=(9P-3)/2.
$$


This lies below $9P/2$. The inverse image (5.4) starts above $19P/2-1$. The first $J$-coupling is zero and the last inverse coordinate is zero. Thus


$$
\boxed{l_a^TB^{-1}l_H{}_i=0\pmod3.}
\tag{7.4}
$$



The rank-$b$ return itself begins at physical $6$, so it cannot enter $C_H\bmod3$, whose numerator is divided by $3^5$.

### 7.3 The remaining first-$4$ cross coefficient

Define, with the original complete prefix data,


$$
d_a=\frac{G_c(F_{\rm prefix},\mathcal F[y^a])}{3^{28}},
$$


and


$$
\boxed{
P_{ai}
=
\frac{d_a^T\mathsf A^{-1}d_H{}_i}{3}\pmod3.
}
\tag{7.5}
$$


The preceding leading support gives a numerator in $3\mathbb Z_3$. Its next residue is not supplied by the closed second-kernel quadratic prefix theorem.

Combining the evaluated terms,


$$
\boxed{
(C_H)_{ai}
=
-c_{r_{ai}-\Pi}+c_{r_{ai}-2\Pi}
-2\,\mathbf1_{a=R,\ i=k-1}
-P_{ai}
\pmod3.
}
\tag{7.6}
$$



Thus the first physical-$4$ return remains


$$
R_4=C_H^TA_4^{-1}C_H\pmod3,
\tag{7.7}
$$


with the actual mixed-prefix digit (7.5) and the actual finite inverse application still to be evaluated.

I do not label (7.7) a completed return. The present primary effort has instead reduced the rank-$b$ return to the much smaller terminal-vector obligation (5.7).

---

## 8. Physical-$6$ assembly in the same second-kernel-pivot frame

Let


$$
\gamma=(\sigma2^t)^{-1},\qquad
\sigma=(-1)^{R_*+L_*}.
$$


Use the accepted leading pivot $\gamma H_0$ and adjacent annihilators


$$
H_i+H_{i+1},\qquad 0\le i<k-1.
$$


Let $N$ be the corresponding adjacent-sum matrix.

The closed prefix-$6$ and $J6$ results remove their contributions at this digit, but not their exact higher returns. Therefore


$$
\boxed{
C_6=C^{\rm mom}
-\bigl(e_{k-1}\eta^T+\eta e_{k-1}^T\bigr)
-R_4
\pmod3.
}
\tag{8.1}
$$


The physical multiplier of each displayed rank-$b$ return is $-3^6$.

The complete leading data in this same frame are


$$
\boxed{
a_6=\bar\gamma^2(C_6)_{00},\qquad
w_6=\bar\gamma N^TC_6e_0,\qquad
B_6=N^TC_6N.
}
\tag{8.2}
$$



The moment parts are the already evaluated expressions


$$
(w_6^{\rm mom})_i
=
\bar\gamma[y^{\kappa_2-i}](1-y)^t(1+y),
$$




$$
(B_6^{\rm mom})_{ij}
=
[y^{\kappa_2-i-j}](1-y)^t(1+y)^2.
\tag{8.3}
$$



Let $e'=e_{k-2}\in\mathbb F_3^{k-1}$. The new rank-$b$ reduction gives the especially simple contributions


$$
\boxed{
a_6^{(b)}=0,
\qquad
w_6^{(b)}=-\bar\gamma\,\eta_0e',
}
\tag{8.4}
$$




$$
\boxed{
B_6^{(b)}
=
-\left(e'(N^T\eta)^T+(N^T\eta)e'^T\right).
}
\tag{8.5}
$$


Thus the rank-$b$ contribution can affect only the last row and column of the adjacent-annihilator matrix, and only the last coordinate of its mixed force. This support conclusion is proved; the values still require $\eta$.

### 8.1 Complete diagonal payment

The two frames remain distinct:


$$
\lambda_{\rm new}
=
\lambda^{\rm pref}
-\frac13f_J^TB^{-1}f_J
-\frac19f_b^TA_b^{-1}f_b
\in3^{-2}\mathbb Z_3,
$$


whereas


$$
\lambda_4
=
\lambda_{\rm new}
-\frac1{3^4}f_C^TA_4^{-1}f_C
\in3^{-4}\mathbb Z_3.
\tag{8.6}
$$


No unit numerator is assumed.

In the monomial-first second-kernel frame, the endpoint-pivot correction begins at physical $8$. In the endpoint-first frame, the established $\lambda_{\rm new}$ bound gives the corrected thresholds $8$ at level $5$ and $10$ at level $6$. These facts do not supply either missing return.

### 8.2 Why this does not solve the directional equation

The exact equation remains


$$
B_6x=w_6,\qquad x\in3^{-1}\mathbb Z_3^{k-1}.
\tag{8.7}
$$


Even a complete evaluation of (8.2) modulo $3$ would not settle this allowance.

Writing $z=3x$, one needs


$$
B_6z=3w_6.
$$


At the next digit, for $z=z_0+3z_1$,


$$
\overline B_6\overline z_0=0,
$$




$$
\overline B_6\overline z_1+
\overline{B_6z_0/3}
=\overline w_6.
\tag{8.8}
$$


The second equation depends on $B_6\bmod9$, not merely on $\overline B_6$.

At physical $7$, one must retain:

- the actual/core difference;
- the physical-$5$ complementary matrix and directional returns;
- higher exact endpoint adaptation;
- the next digits of all earlier returns;
- the stationary projection term that becomes active when attempting source precision $34$.

Source precision $33$ is not a whole physical-$7$ moment theorem. No part of the next-$J$ audit is claimed here.

---

## 9. Complete producer, forcing, and global primitive normalization

The complete producer remains


$$
Q_{\rm act}=Q_c+3^7\mathscr R.
$$


With $F_{\rm fac}=(n-1)!$, retain


$$
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},
$$




$$
\gamma_0=1,\quad\gamma_1=0,\quad
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
=
3nh_{\rm vec}
+(b_{\rm force}+6)e_{n-1}
+\frac{2b_{\rm force}}{n-1}e_{n-2},
$$




$$
\xi=
\frac{u^Tt_{\rm force}}{F_{\rm fac}^2-u^Tv}.
$$


The actual coefficients and endpoint remain


$$
[x^a](3^7\mathscr R)
=
-\frac{F_{\rm fac}}{a!}
\bigl((t_{\rm force})_a+\xi v_a\bigr),
\qquad 0\le a\le n-1,
$$




$$
\mathscr R(-1)=-\frac{\xi F_{\rm fac}^2}{3^7}.
\tag{9.1}
$$



The complete return/forcing identity is still


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
\tag{9.2}
$$


Neither term is discarded.

Likewise,


$$
\mu_{r+1}+\mu_r
=
\frac{3^h}{2r+1}
-\frac{3^h}{4}\bigl((2r+2)!+(2r)!\bigr),
\qquad 0\le r\le2n-2,
$$


retains its genuine resonant division at


$$
r_*=(3^h-5)/2.
$$



All actual integer column contents and the least simultaneous clearer $\ell_{\rm clr}$ are unchanged. No local quotient calculation above redefines them.

Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the final gcd over **all primes**


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole evaluated error is exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{9.3}
$$



An irrationality proof would require, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\log g_\ell-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|
\longrightarrow+\infty.
\tag{9.4}
$$


These conditions would produce nonzero integer linear-form errors tending to zero, contradicting rationality. They are not proved here.

---

## 10. New bounded exact-arithmetic calculations

No tools were used, and none of the following calculations is represented as completed.

### 10.1 Primary calculation: the terminal inverse-coordinate vector

This calculation is **not** another $J$-quadratic audit. It asks for a previously unevaluated inverse coordinate that the quadratic can conceal.

#### Bounded inputs

Fix one certified original tuple $(j,h)$ in (1.1), with all derived parameters fixed. Use the already formed complete finite boundary data:

1. the unit
   

$$
a=\overline B_{\ell,\tau-1};
$$


2. the actual last-row entries
   

$$
w_v=\overline B_{\tau-1,v}
$$


   only for
   

$$
\frac{19P-1}{2}
   \le v\le
   \frac{23P-1}{2}+t+k-1;
$$


3. the $k$ actual terminal couplings
   

$$
\theta_i=\overline{(l_H)_{\tau-1,i}};
$$


4. the coefficients $c_d=(-1)^d\binom td\bmod3$, $0\le d\le t$.

The source expressions for the indispensable data can be stated without any virtual terminal. Let $\widehat F_v$ denote the exact correction of $F[y^{R_*+v}]$ against the original finite prefix, and let $\widehat{\mathcal F}[H_i]$ be the corresponding prefix-corrected one-lift. Then


$$
B_{\tau-1,v}
=
-\frac{G_c(\widehat F_{\tau-1},\widehat F_v)}{3^{27}},
$$




$$
(l_H)_{\tau-1,i}
=
-\frac{G_c(\widehat F_{\tau-1},
\widehat{\mathcal F}[H_i])}{3^{29}}.
\tag{10.1}
$$


Thus the required numerator precisions are respectively modulo $3^{28}$ and $3^{30}$. The divisions are the original paid block and coupling divisions.

The complete $W$-projection, prefix correction, and actual last middle column are part of (10.1).

#### Calculation and expected verifiable output

Compute


$$
\boxed{
\eta_i=a^{-1}
\left(
\theta_i+
\sum_{q=0}^{2}\sum_{d=0}^{t}
w_{J_i-qP-d}\,c_d
\right).
}
\tag{10.2}
$$


Every row index in this formula is explicitly within the finite interior. There are at most $3k(t+1)$ multiply-add terms.

The output should contain:

- the $k$ values $\eta_i\in\{0,1,2\}$;
- the inverse-image certificate
  

$$
\overline B\,x_i=\overline{l_H{}_i}
$$


  for the vector $x_i$ in (5.6);
- the rank-$b$ return
  

$$
e_{k-1}\eta^T+\eta e_{k-1}^T;
$$


- the actual $A_b$-coordinate inverse images obtained from (6.3), with
  

$$
\overline A_b\,\overline X_i
  =\overline{M_bH_i/3}.
$$



The output “$\eta=0$” or “$\eta\ne0$” is to be determined, not assumed. A receipt for one tuple establishes only that tuple. A uniform theorem on the infinite original subwindow still requires a uniform evaluation of (10.2).

### 10.2 Secondary calculation, after the primary one: the first-$4$ mixed prefix digit

The new data needed for (7.5) are


$$
\mathsf A\bmod9,\qquad d_a\bmod9,\qquad d_H\bmod9,
\qquad a\in\mathcal C.
$$


The matrix $\mathsf A\bmod9$ is already the established finite


$$
K_N(-2\beta A_0+3A_- -3\beta A_+)\pmod9.
$$


No old prefix-$27$ quadratic is to be recomputed.

The new requested outputs are:

1. the paid mixed quotients
   

$$
P_{ai}=d_a^T\mathsf A^{-1}d_H{}_i/3\pmod3;
$$


2. $C_H$ from (7.6);
3. actual finite solve certificates
   

$$
\overline A_4X=C_H;
$$


4. the return
   

$$
R_4=C_H^TX.
$$



The dimensions are exactly $|\mathcal C|\times k$ and $|\mathcal C|\times|\mathcal C|$, with the original monomial boundary. No differently adapted inverse is an acceptable substitute.

---

## 11. Conclusion

### New proved statements

On the certified infinite original Range III subwindow:

1. The direct complete rank-$b$ source coupling is evaluated:
   

$$
G_c(V_u,\mathcal F[H_i])/3^{30}
   =
   \mathbf1_{u+i=P-1}-\mathbf1_{u+i=2\Pi-1}
   \pmod3.
$$



2. Its ordinary/second-kernel mixed prefix correction is zero.

3. Its mixed interior $J$-correction is zero, with the actual finite inverse image explicitly given by (5.3).

4. The actual normalized rank-$b$ inverse images are given by the finite polynomials (6.8), converted to the prescribed original complement by (6.3).

5. The full rank-$b$ return is proved to be
   

$$
\boxed{R_b=e_{k-1}\eta^T+\eta e_{k-1}^T.}
$$


   It is zero exactly when the explicitly defined actual terminal vector $\eta$ is zero.

6. The first physical-$4$ cross has the evaluated decomposition (7.6), including its indispensable upper-corner $3y$ term.

### Exact remaining local bottleneck

The rank-$b$ return is not yet numerically or uniformly closed: its remaining datum is the actual terminal vector (10.2). This is now a bounded contraction of one finite boundary row with three explicit binomial bands, not an unevaluated full Schur quadratic.

The first physical-$4$ return still requires the mixed-prefix digit (7.5) and its actual finite $A_4$-inverse application.

After those are evaluated, the whole $B_6,w_6$ equation still needs the actual physical-$7$ information to decide the permitted $3^{-1}$-directional lift. Source $34$, not merely source $33$, is needed for that next whole moment layer.

### Global proof status

No same-index nonvanishing theorem, all-prime primitive-denominator saving theorem, or decay theorem for the nonzero whole error has been established.



$$
\boxed{
\text{The report gives a new source-specific finite-return reduction,}
\quad
\text{but no unconditional proof of rationality or irrationality of }e+\pi.
}
$$


