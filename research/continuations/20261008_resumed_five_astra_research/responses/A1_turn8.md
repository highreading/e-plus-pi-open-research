> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The second-kernel pivot and a new sixth-digit moment calculation

## Abstract and proof status

The rationality or irrationality of $e+\pi$ remains unresolved.

This report makes two rigorous local advances, but **does not complete the requested evaluation of the entire physical $3^6$ matrix and mixed force**.

1. **The parent’s second-kernel-pivot argument passes its valuation audit in Ranges I–III.** In the specified common monomial-complement frame, a pivot in the complete second kernel with unit endpoint protects the actual/core comparison at physical order $3^6$. The new physical-$5$ complement has both its matrix return and its directional return in $3^7$. No endpoint modulo $9$ theorem is needed for this conclusion.

2. **The complete-core moment contribution at physical order $3^6$ is explicitly evaluated in Range III.** Put
   

$$
t=\Pi-2\chi,\qquad \Omega=\frac{\Pi}{3}=\frac P9,\qquad
   \kappa_2=\frac{\Omega-1}{2}.
$$


   For the literal integer second-kernel amplitudes
   

$$
H_i(y)=(1-y)^\Pi y^{L_*+i},
   \qquad 0\le i<\varepsilon,
$$


   the new calculation gives
   

$$
\boxed{
   \frac{G_c(\mathcal F[H_i],\mathcal F[H_j])}{3^{32}}
   \equiv
   -[y^{\kappa_2-i-j}](1-y)^t
   \pmod3.
   }
   \tag{A}
$$


   Consequently the moment term in the physical-$6$ returned matrix has the **positive** coefficient matrix
   

$$
\boxed{
   \left([y^{\kappa_2-i-j}](1-y)^t\right)_{0\le i,j<\varepsilon}.
   }
   \tag{B}
$$


   This is a calculation with the complete-core corrected columns. It is not a calculation with bare monomials or merely their reductions modulo $3$.

The other four potentially active terms—the second-prefix return, the finite $J$-return, the rank-$b$ return, and the first physical-$4$ complementary return—are retained below. They have **not** all been evaluated at this digit. Thus (B) is not asserted to be the entire actual physical-$6$ matrix.

The diagonal correction is also repaired:

- in the endpoint-first adapted frame, only
  

$$
\lambda_{\rm new}\in3^{-2}\mathbb Z_3
$$


  is used, giving border thresholds $8$ and $10$, not $9$ and $11$;
- in the parent’s monomial-first frame, the complete additional $3^{-4}$ diagonal return remains present, and only
  

$$
\lambda_4\in3^{-4}\mathbb Z_3
$$


  is used.

No local calculation here changes the actual contents, least simultaneous clearer, all-prime final gcd, primitive denominator, or whole error.

---

## 1. Original objects and exact scope

### 1.1 The original index domain

Every original-family assertion concerns sufficiently large indices satisfying


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
\qquad C_{16}=147968\,3^{15},
$$


and


$$
\frac{103}{1000}<\frac{N_0}{P_0}<\frac{104}{1000}.
$$



The parameters remain


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
x=y-1,\qquad Q=27P,\qquad b=Q-N_0,\qquad R=b/2,\qquad \chi=P-R.
$$


Then


$$
D+b=10Q,\qquad
\chi=\frac{243r-25P}{2},
\qquad .0145<\frac{\chi}{P}<.136.
$$


For sufficiently large original indices,


$$
v_3(\chi)=5,\qquad \frac{\chi}{243}\equiv1\pmod9.
\tag{1.1}
$$



In particular, none of $P,\chi,t,\varepsilon$ below is a free experimental parameter.

The new coefficient calculation is scoped to original indices in **Range III**, namely $\varepsilon>0$. No new assertion that this narrowed range occurs infinitely often is needed or made here.

### 1.2 Finite spaces and the physical terminal

Retain exactly


$$
U_s=x^s\quad(0\le s<D),
$$




$$
z_i=x^Dy^i\quad(0\le i<\nu),\qquad \nu=D/2-1,
$$




$$
Y_t=y^t\quad(d\le t\le m),\qquad d=D+\nu,\qquad W=[U\ Y].
$$


The physical HIGH terminal is $Y_m$, not $z_{\nu-1}$.

The finite prefix and tail boundaries are


$$
R_*=\frac{9Q+1}{2},\qquad a_0=R_*-1,
$$




$$
\tau=\frac{N_0-3}{2},\qquad \ell=3R+1,
$$




$$
K=\{0,\ldots,\ell-1\},\qquad
J=\{\ell,\ldots,\tau-1\},
$$




$$
n_J=\frac{Q-4b-5}{2},\qquad R_*+\tau=\nu.
\tag{1.2}
$$


The last middle column remains in this actual finite $J$-block.

### 1.3 Complete columns, producer, and forcing

The complete functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!.
$$


The largest physical pole denominator remains


$$
4H-4D+5<3^{h+1}.
$$



The complete core is


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A,
$$




$$
G_c(f,g)=\mathcal M(Q_cfg).
$$


Its corrected columns are


$$
E_c=G_c(W,W),\qquad
F_i=z_i-WE_c^{-1}G_c(W,z_i).
$$


The one-lift input associated with an amplitude $a(y)$ is


$$
\Psi[a]
=x^{D+b}y^{k_0}(y^{3Q}+3)a(y),
\qquad k_0=\frac{3Q+1}{2},
$$


and $\mathcal F[a]$ denotes its complete-core correction against the same $W$.

The actual producer is retained in full:


$$
Q_{\rm act}=Q_c+3^7\mathscr R,
$$




$$
[x^a](3^7\mathscr R)
=-\frac{(n-1)!}{a!}(t_a+\xi v_a),
\qquad 0\le a\le n-1,
$$


where


$$
t=
3nh_{\rm vec}
+(b_{\rm force}+6)e_{n-1}
+\frac{2b_{\rm force}}{n-1}e_{n-2},
\qquad b_{\rm force}=-n-66.
\tag{1.3}
$$


Also


$$
v=T_n^{-1}u,\qquad
u_a=\frac{(n-1)!(-2)^a}{a!},
$$




$$
h_{\rm vec}
=T_n^{-1}
\left(\binom{n+a}{a}\gamma_{n+a}\right)_{a=0}^{n-1},
$$




$$
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},
$$




$$
\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1},
\qquad \gamma_0=1,\quad\gamma_1=0.
$$


The signed, paid $\xi$ is unchanged, including


$$
\mathscr R(-1)=-\frac{\xi((n-1)!)^2}{3^7}.
$$



Likewise, the complete source-return identity is retained:


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
\tag{1.4}
$$



---

## 2. Audit of the second-kernel-pivot candidate

The relevant accepted inputs are:

1. on the common original amplitude lattice,
   

$$
T_{\rm act,red}-T_{c,\rm red}\in3^7M;
   \tag{2.1}
$$


2. the first radical has integer coefficient matrix $\mathscr G$, with columns
   

$$
g_{L_*+u}=(1-y)^{2\chi}y^{L_*+u},
   \qquad
   L_*=\frac{P-1}{2},\qquad 0\le u<\delta;
$$


3. after the paid common monomial complement, the leading retained matrix is
   

$$
M_\alpha/3^5\equiv-\mathsf D\pmod3,
   \qquad
   \mathsf D_{uv}
   =[y^{\kappa_1-u-v}](1-y)^{2\chi},
$$


   where
   

$$
\Pi=P/3,\qquad \kappa_1=(\Pi-1)/2;
$$


4. in these same coordinate labels, the leading endpoint is
   

$$
\overline F_\alpha(p)=\sigma p(-1),
   \qquad \sigma=(-1)^{R_*+L_*}.
   \tag{2.2}
$$



The comparison (2.1) is a matrix comparison. Its use for the separately adapted frames must still be paid.

### 2.1 The first monomial complement and its complete diagonal

Let $E_4$ be the common monomial complement. Write


$$
A_{4,\alpha}
=E_4^T(T_{\alpha,\rm red}/81)E_4,
$$




$$
C_{4,\alpha}
=E_4^T(T_{\alpha,\rm red}/81)\mathscr G\in3M.
$$


Then


$$
\widehat{\mathscr G}_\alpha
=
\mathscr G-E_4A_{4,\alpha}^{-1}C_{4,\alpha}.
$$


The retained endpoint and diagonal are exactly


$$
F_\alpha
=
\mathscr G^Tf_{\alpha,\rm new}
-C_{4,\alpha}^TA_{4,\alpha}^{-1}f_{\alpha,C},
\tag{2.3}
$$




$$
\boxed{
\lambda_{4,\alpha}
=
\lambda_{\alpha,\rm new}
-\frac1{81}
f_{\alpha,C}^TA_{4,\alpha}^{-1}f_{\alpha,C}.
}
\tag{2.4}
$$



The entire earlier diagonal is


$$
\lambda_{\alpha,\rm new}
=
\lambda_\alpha^{(2)}
-\frac19 f_{\alpha,b}^TA_{b,\alpha}^{-1}f_{\alpha,b},
$$




$$
\lambda_\alpha^{(2)}
=
\lambda_\alpha^{\rm pref}
-\frac13 f_{\alpha,J}^TB_\alpha^{-1}f_{\alpha,J}.
\tag{2.5}
$$


Only


$$
\lambda_{\alpha,\rm new}\in3^{-2}\mathbb Z_3
$$


is justified by the supplied independent audit. Therefore


$$
\boxed{\lambda_{4,\alpha}\in3^{-4}\mathbb Z_3.}
\tag{2.6}
$$



The $1/3$, $1/9$, and $1/81$ terms have not been removed.

The common-frame matrix transport also checks directly. The normalized complementary block changes in $3^3$, the normalized cross changes in $3^3$, and the original cross is in $3$. Hence:

- the direct retained difference is in $3^7$;
- a changed-cross return begins at $3^{4+1+3}=3^8$;
- a changed-inverse return begins at $3^{4+1+3+1}=3^9$.

Thus


$$
M_{\rm act}-M_c\in3^7M
\tag{2.7}
$$


in the common first-radical labels.

### 2.2 Valid kernel pivots

Let


$$
\mathcal K=\ker\mathsf D.
$$



In the already classified ranges:

- **Range I:** $\mathcal K=\mathbb F_3[y]_{<\delta}$, so $z_0=1$;
- **Range II:** $\mathcal K=\mathbb F_3[y]_{<\delta-B_1}$, so again $z_0=1$;
- **Range III:**
  

$$
\mathcal K=(1-y)^t\mathbb F_3[y]_{<\varepsilon},
  \qquad t=\Pi-2\chi,\qquad \varepsilon=\delta-t>0,
$$


  so
  

$$
z_0=(1-y)^t.
  \tag{2.8}
$$



These pivots lie inside the original finite space. Their endpoints are respectively


$$
\sigma,\qquad \sigma,\qquad \sigma2^t,
$$


all ternary units.

The Range II nullity is genuinely positive on the original parameters:


$$
\delta-B_1=\frac{\Pi-6\chi+3}{2}.
$$


Writing $\Pi=243T$, $\chi=243c$, with $c\equiv1\pmod9$, gives


$$
T-6c\equiv3\pmod{18}.
$$


Its nonnegative nullity therefore forces $T-6c\ge3$, and the nullity is at least $366$.

For the gray range, the same payment applies to the integer $W_2$ constructed in Turn 7 **if that complete-kernel theorem is admitted after its separate audit**. The additional hypotheses needed here are exactly


$$
\mathcal K=W_2\mathbb F_3[y]_{<k_2},
\qquad W_2(-1)\ne0.
$$


The saturated lift follows from the triangular coefficient block at the first nonzero coefficient of $W_2$. No extra higher-endpoint hypothesis is introduced by the pivot payment.

The Range III calculation below does not depend on the pending independent gray-range audit.

### 2.3 An evaluated leading directional solution

In the old first-pivot frame, let $\mathsf N$ be the adjacent-sum map. The leading matrix and actual leading mixed direction are


$$
B_0=-\mathsf N^T\mathsf D\mathsf N,
\qquad
r_0=-\sigma^{-1}\mathsf N^T\mathsf D e_0.
$$



In Ranges I–II, $\mathsf D e_0=0$, so $r_0=0$.

In Range III, the literal dyadic polynomial


$$
\boxed{
w_0(y)=
\sigma^{-1}
\frac{1-2^{-t}(1-y)^t}{1+y}
}
\tag{2.9}
$$


has degree $t-1\le\delta-2$. Its numerator vanishes exactly at $-1$. Moreover,


$$
\mathsf Nw_0
=
\sigma^{-1}(e_0-2^{-t}z_0),
$$


and $\mathsf Dz_0=0$ modulo $3$. Hence


$$
\boxed{B_0w_0=r_0\pmod3.}
\tag{2.10}
$$



This is an evaluated compatibility statement for the original leading mixed force. It is not a freely chosen force.

The dyadic division in (2.9) is a ternary-unit operation only. It makes no claim about the original global integer contents or clearer.

### 2.4 The new physical-$5$ return starts at $7$, in both channels

Choose


$$
v_{2,\alpha}=\frac{z_0}{F_\alpha(z_0)}.
$$


Choose a complement $E_5$ to the complete kernel and replace every complementary column $u$ by


$$
u-v_{2,\alpha}F_\alpha(u).
$$


Similarly lift the remaining kernel columns into the exact endpoint kernel.

All retained columns reduce to $\mathcal K$. Since


$$
M_\alpha/3^5\equiv-\mathsf D,
$$


their pairings with every integral column belong to $3^6$.

Consequently the physical-$5$ complement has


$$
A_5=3^5A_{5,0},\qquad A_{5,0}\in\mathrm{GL}(\mathbb Z_3),
$$


and both its retained cross block and its pivot-direction cross block are in $3^6$. Thus


$$
A_5^{-1}=3^{-5}A_{5,0}^{-1},
$$




$$
\boxed{
X_5^TA_5^{-1}X_5\in3^7M,
\qquad
X_5^TA_5^{-1}c_5\in3^7M.
}
\tag{2.11}
$$


Its endpoint coordinates are exactly zero, so it makes no new endpoint or diagonal return.

This verifies the parent’s important frame distinction: in the old first-pivot frame the complementary direction could begin at $5$; in the present second-kernel-pivot frame it begins at $6$.

### 2.5 Actual/core synchronization at physical order $6$

The actual and core endpoints have the same reduction. Their corresponding normalized pivots and exact endpoint-annihilating kernel columns therefore differ by $3$ times kernel lifts.

A pairing involving any such kernel lift begins at $6$. Hence the direct change caused by these order-$3$ coordinate changes begins at $7$, not $6$.

The complementary cross blocks begin at $6$, and their differences begin at $7$. Therefore the changed-cross return begins at


$$
7-5+6=8.
$$


The inverse difference has valuation at least


$$
-5+7-5=-3,
$$


so its quadratic contribution begins at


$$
6-3+6=9.
$$


Together with (2.7), this proves:

> **Second-kernel synchronization theorem.**  
> In the specified same-label second-kernel-pivot frames, the actual and core retained matrices, including their mixed pivot columns, agree modulo $3^7$.

This does not assert synchronization of arbitrary separately adapted first-annihilator frames.

### 2.6 Correct border payment

After the new complement, the complete border has the form


$$
\begin{pmatrix}
\lambda_4&1&0\\
1&a&r^T\\
0&r&S
\end{pmatrix},
\qquad a,r,S\in3^6M.
$$


Its exact endpoint-pivot return is


$$
S^\sharp
=
S+\frac{\lambda_4}{1-\lambda_4a}rr^T.
\tag{2.12}
$$


By (2.6),


$$
\lambda_4a\in3^2\mathbb Z_3,
$$


so the denominator is a unit and


$$
S^\sharp-S\in3^8M.
\tag{2.13}
$$



Writing $r=3^6w$, $S=3^6B$, the normalized rank-one coefficient has valuation at least $2$. Thus, for $x\in3^{-1}\mathbb Z_3^s$, the scalar


$$
1+\frac{3^6\lambda_4}{1-\lambda_4a}w^Tx
$$


is a unit. The usual exact rank-one conversion therefore preserves the $3^{-1}$ allowance.

Separately, in the endpoint-first frame with $\lambda_{\rm new}\in3^{-2}\mathbb Z_3$, the border corrections at $k=5,6$ begin at $8,10$. These are different frames, and their diagonals must not be interchanged.

---

## 3. Extension of the corrected-pairing compression to source precision $33$

The new physical-$6$ moment requires source precision $33$, because the retained moment term is divided by $3^{26}$.

The Turn 6 compression proof already supplies the following error bounds:



$$
\begin{array}{c|c}
\text{error}&\text{valuation lower bound}\\ \hline
\text{stationary projection error}&33\\
\text{exponential terms of order at least two}&34\\
\text{bare macro-denominator replacement}&35\\
\text{logarithmic reciprocal replacement}&34\\
\text{complete-core transfer}&h
\end{array}
$$



For precision $33$, retain the logarithmic denominators with


$$
v_3(d_v)\ge h-7.
$$


The newly inactive terms satisfy


$$
2h-1-(h-26)-(h-8)=33.
$$


They therefore vanish modulo $3^{33}$. The retained denominators are still multiples of the same macro length $L=3^{h-17}$, and none of the old physical-support inequalities changes.

Thus the existing proof extends to


$$
\boxed{
G_c(F[p_1],F[p_2])
\equiv
K_N\mathcal J_h\!\left(x^D(\beta+3y)p_1p_2\right)
\pmod{3^{33}},
}
\tag{3.1}
$$


where


$$
\mathcal J_h(B)=3^h\sum_v\frac{[y^v]B}{2v+1},
\qquad K_N\equiv1\pmod3,
$$


with the same finite physical support as in the accepted compression.

This extension uses the existing $p=17$ filter. It does **not** justify source precision $34$: the stationary error at valuation $33$ would then be active.

All amplitudes used below remain in the admitted degree range. Indeed,


$$
\deg H_i=L_*+\Pi+i
\le L_*+2\chi+\delta-1\le R,
$$


and therefore


$$
\deg\bigl(x^by^{k_0}(y^{3Q}+3)H_i\bigr)
\le b+k_0+3Q+R<\nu-2.
\tag{3.2}
$$



---

## 4. New evaluated sixth-digit moment in Range III

### 4.1 Literal amplitudes and the strengthened gap

Assume $\varepsilon>0$. Put


$$
t=\Pi-2\chi,\qquad \varepsilon=\delta-t.
$$


The complete second-kernel amplitudes before the first physical-$4$ complementary correction are exactly


$$
H_i(y)=(1-y)^\Pi y^{L_*+i},
\qquad 0\le i<\varepsilon.
\tag{4.1}
$$



Here


$$
0<t<\Pi/3.
$$


For $0\le i,j<\varepsilon$, define


$$
r_{ij}=\kappa_1-i-j.
$$


Then


$$
r_{ij}\le\kappa_1<\Pi/2.
$$


More importantly,


$$
\boxed{r_{ij}-t\ge120.}
\tag{4.2}
$$



To check this, the minimum is:

- if $\delta=\chi-1$,
  

$$
\min(r_{ij}-t)=\frac{P+7}{2}-4\chi;
$$


- if $\delta=(P+3)/2-3\chi$,
  

$$
\min(r_{ij}-t)=4\chi-\frac{P+3}{2}.
$$



Both are positive by the defining minimum for $\delta$. By the original divisibility $243\mid P,\chi$, their residues modulo $243$ are respectively $125$ and $120$. This proves (4.2).

In particular, the same gap survives the one-step shift from the $3y$ term.

### 4.2 The complete compressed polynomial

For $s=i+j$, direct multiplication gives


$$
\boxed{
B_{ij}(y)
=
(1-y)^{817\Pi+t}(\beta+3y)y^s
\left(y^{732\Pi}+6y^{489\Pi}+9y^{246\Pi}\right).
}
\tag{4.3}
$$


Indeed,


$$
D+2b+2\Pi=817\Pi+t,
$$


and the three shifts come from the full square


$$
(y^{3Q}+3)^2=y^{6Q}+6y^{3Q}+9.
$$


Neither weighted term has been dropped in deriving (4.3).

By (3.1),


$$
G_c(\mathcal F[H_i],\mathcal F[H_j])
\equiv K_N\mathcal J_h(B_{ij})\pmod{3^{33}}.
\tag{4.4}
$$



### 4.3 A coefficient valuation lemma

Let $\Pi=3^q$. For


$$
0\le a\le816,\qquad 0<l<\Pi,
$$


one has


$$
\boxed{
v_3\binom{817\Pi}{a\Pi+l}
=
q-v_3(l)+v_3\binom{816}{a}.
}
\tag{4.5}
$$



Proof: use


$$
\binom{817\Pi}{a\Pi+l}
=
\frac{817\Pi}{a\Pi+l}
\binom{817\Pi-1}{a\Pi+l-1}.
$$


The lower $q$ ternary digits of $817\Pi-1$ are all $2$. They introduce no carry in the second binomial; its valuation is exactly that of $\binom{816}{a}$. Since $817$ is a unit and $0<l<\Pi$,


$$
v_3(a\Pi+l)=v_3(l).
$$


This proves (4.5).

Now consider a coefficient of


$$
(1-y)^{817\Pi+t}
$$


at an index $a\Pi+r'$, where


$$
t<r'<\Pi/2.
$$


Every contributing convolution index $l$ lies in


$$
r'-t\le l\le r',
$$


hence in $(0,\Pi/2)$. Therefore every term has valuation at least


$$
1+v_3\binom{816}{a}.
\tag{4.6}
$$



This is where the higher integer binomial digits of $H_i$ are retained. Replacing $H_i$ by its two-term reduction would not establish (4.5)–(4.6).

### 4.4 Complete pole-layer audit

A pole not divisible by $P=3^{h-32}$ has weight divisible by $3^{33}$, and is invisible at the required source precision. Write the remaining pole denominator as


$$
dP,\qquad d>0\ \text{odd}.
$$


The exact coefficient support in (4.3), still below the original physical cutoff, bounds the relevant $d$’s by $1035$. This is only an outer bound for the audit: a term is retained only when its actual coefficient index lies in the support of (4.3).

Number the low, middle, and high terms by $\ell=1,2,3$. Their shifts are


$$
(3+243\ell)\Pi,
$$


and their explicit weights are $9,6,1$.

For either the $\beta$ term or the $3y$ term, the extracted index has the form


$$
a\Pi+r',
$$


where


$$
a=\frac{3d-7}{2}-243\ell,
\qquad
r'=r_{ij}\ \text{or}\ r_{ij}-1.
\tag{4.7}
$$


If $a<0$ or $a>816$, the coefficient is zero, by the gap $r'>t$.

Put


$$
c_a=v_3\binom{816}{a}.
$$


The ternary digits


$$
816=(1010020)_3
$$


give the following lower bounds:



$$
\begin{array}{c|c|c}
v_3(d)&\text{forced low digits of }a&c_a\text{ at least}\\ \hline
0,1&a\equiv1\pmod3&1\\
2,3&a\equiv10\pmod{27}&3\\
4,5,6&a\equiv118\pmod{243}&5
\end{array}
\tag{4.8}
$$



For example, $a\equiv10=(101)_3\pmod{27}$ forces the units borrow and the borrows through the two zero digits in positions $2,3$ of $816$. The stronger residue $118=(11101)_3$ forces two further borrows.

The pole weight is $3^{32-v_3(d)}$ times a unit. Combining it with (4.6) shows that all layers except $v_3(d)=6$ vanish modulo $3^{33}$:



$$
\begin{array}{c|c}
v_3(d)&\text{minimum total valuation before explicit }6,9,3y\\ \hline
0&34\\
1&33\\
2&34\\
3&33\\
4&34\\
5&33\\
6&32
\end{array}
\tag{4.9}
$$



Within the finite support, the sole pole with $v_3(d)=6$ is


$$
d=729,\qquad dP=27Q.
$$


At that pole:

- the high term has $a=361$;
- the middle term has $a=604$, but its explicit factor $6$ moves it to valuation at least $33$;
- the low term has $a=847$, outside the support;
- the $3y$ contribution also moves to valuation at least $33$.

Thus only the high $\beta$-term remains.

### 4.5 Evaluation of its normalized unit

For $a=361$,


$$
v_3\binom{816}{361}=5.
$$


By (4.5), a coefficient can have valuation exactly $6$ only when


$$
v_3(l)=q-1.
$$


Since $0<l<\Pi/2$, the only possibility is


$$
l=\Pi/3.
$$



The relevant signed coefficient is therefore that at


$$
361\Pi+\Pi/3=1084\,\Pi/3.
$$


Scaling both binomial arguments by a power of $3$ preserves the normalized unit modulo $3$, so it is enough to evaluate


$$
\binom{2451}{1084}.
$$


Its factorial valuations are


$$
v_3(2451!)=1223,\qquad
v_3(1084!)=539,\qquad
v_3(1367!)=678.
$$


Hence its valuation is $6$. The normalized factorial units modulo $3$ are $1,2,1$, respectively, giving


$$
\frac{\binom{2451}{1084}}{3^6}\equiv2\pmod3.
\tag{4.10}
$$


The coefficient sign is positive because $1084\,\Pi/3$ is even.

Finally, $\beta\equiv1\pmod3$ and $K_N\equiv1\pmod3$. Therefore


$$
\frac{G_c(\mathcal F[H_i],\mathcal F[H_j])}{3^{32}}
\equiv
2[y^{r_{ij}-\Pi/3}](1-y)^t
\pmod3.
$$


Since


$$
r_{ij}-\Pi/3=\kappa_2-i-j,
$$


this proves (A).

### Theorem 4.1 — Evaluated Range III moment contribution

On every sufficiently large original index in Range III,


$$
\boxed{
\frac{G_c(\mathcal F[H_i],\mathcal F[H_j])}{3^{32}}
\equiv
-[y^{\kappa_2-i-j}](1-y)^t
\pmod3.
}
\tag{4.11}
$$


The division by $3^{32}$ is paid by the complete pole audit above.

This result includes the full integer amplitudes, the complete-core corrections against $W$, the source precision $33$, and the original finite physical cutoff.

---

## 5. The literal sixth-digit moment matrix and mixed column

Define


$$
c_k=
\begin{cases}
(-1)^k\binom tk,&0\le k\le t,\\
0,&\text{otherwise}.
\end{cases}
$$


Then the moment contribution to the unadapted second-kernel physical-$6$ matrix is


$$
\boxed{C^{\rm mom}_{ij}=c_{\kappa_2-i-j}\pmod3.}
\tag{5.1}
$$



Every entry is explicitly evaluated by Lucas’s rule:


$$
c_k\equiv
(-1)^k\prod_\nu\binom{t_\nu}{k_\nu}\pmod3.
\tag{5.2}
$$



Let


$$
\gamma=(\sigma2^t)^{-1}\in\mathbb Z_3^\times.
$$


The leading pivot is $\gamma H_0$, and the leading endpoint-annihilating columns are


$$
H_i+H_{i+1},\qquad 0\le i<\varepsilon-1.
$$


Higher exact endpoint corrections do not affect physical digit $6$, by Section 2.

Thus the moment contributions in the required pivot frame are


$$
a_6^{\rm mom}=\gamma^2c_{\kappa_2},
$$




$$
\boxed{
(w_6^{\rm mom})_i
=
\gamma[y^{\kappa_2-i}](1-y)^t(1+y),
}
\tag{5.3}
$$




$$
\boxed{
(B_6^{\rm mom})_{ij}
=
[y^{\kappa_2-i-j}](1-y)^t(1+y)^2.
}
\tag{5.4}
$$



These formulas evaluate the mixed contribution as well as the quadratic contribution.

For sufficiently large original indices,


$$
243\mid t,\qquad \kappa_2\equiv121\pmod{243}.
$$


Consequently


$$
a_6^{\rm mom}=0,
$$




$$
(w_6^{\rm mom})_i=0
\quad\text{unless}\quad i\equiv120,121\pmod{243},
$$




$$
(B_6^{\rm mom})_{ij}=0
\quad\text{unless}\quad i+j\equiv119,120,121\pmod{243}.
\tag{5.5}
$$



These are statements about the evaluated moment contribution. The unevaluated returns can alter these support statements for the complete matrix and force.

---

## 6. The entire physical-$6$ matrix: exact assembly and the remaining obstruction

Let $\mathscr H$ be the integer coefficient matrix of the amplitudes $H_i$. The complete core identity remains


$$
\begin{aligned}
T_{c,\rm red}
={}&-\frac{G_c(\mathcal F,\mathcal F)}{3^{26}}
-81Z^T\mathsf A Z\\
&-27G^TL_cB_c^{-1}L_c^TG
-81M_{b,c}^TA_{b,c}^{-1}M_{b,c}.
\end{aligned}
\tag{6.1}
$$



Define the paid integral contracted couplings


$$
\mathscr L_H=\frac{L_c^TG\mathscr H}{3},
\qquad
\mathscr M_H=\frac{M_{b,c}\mathscr H}{3},
$$


and


$$
\mathscr C_H
=
\frac{E_4^TT_{c,\rm red}\mathscr H}{3^5}.
$$


Let


$$
A_4=E_4^T(T_{c,\rm red}/81)E_4.
$$



The full second-kernel sixth digit in the common monomial-first frame is therefore


$$
\boxed{
\begin{aligned}
(C_6)_{ij}
={}&c_{\kappa_2-i-j}\\
&-\left(\frac{\mathscr H^TZ^T\mathsf A Z\mathscr H}{9}\right)_{ij}\\
&-\left(\frac{\mathscr L_H^TB_c^{-1}\mathscr L_H}{3}\right)_{ij}\\
&-\left(\mathscr M_H^TA_{b,c}^{-1}\mathscr M_H\right)_{ij}\\
&-\left(\mathscr C_H^TA_4^{-1}\mathscr C_H\right)_{ij}
\pmod3.
\end{aligned}
}
\tag{6.2}
$$



All displayed divisions are paid:

- the prefix contraction is in $9M$;
- the $J$-quadratic contraction is in $3M$;
- $M_{b,c}\mathscr H\in3M$;
- the first physical-$4$ cross is in $3^5M$.

The physical rank-$b$ inverse cost $3^{-2}$ is already present in (6.1); it is not replaced by a unit physical inverse.

The actual matrix has the same $C_6$ modulo $3$, by the audited synchronization theorem.

However, **only the first line of (6.2) is newly evaluated here**. Equation (6.2) is an exact decomposition, not a claim that the complete matrix has been evaluated.

Once its entries are known, the actual leading mixed data are literally


$$
\boxed{
(w_6)_i=\bar\gamma\bigl((C_6)_{i0}+(C_6)_{i+1,0}\bigr),
}
\tag{6.3}
$$




$$
\boxed{
(B_6)_{ij}
=
(C_6)_{ij}+(C_6)_{i+1,j}
+(C_6)_{i,j+1}+(C_6)_{i+1,j+1}.
}
\tag{6.4}
$$


No unspecified endpoint jet occurs in these sixth-digit formulas.

### 6.1 Why the prefix is not closed by support alone

Write


$$
\mathsf A Z=d.
$$


Then the prefix term in (6.2) is


$$
\frac{(d\mathscr H)^T\mathsf A^{-1}(d\mathscr H)}9.
\tag{6.5}
$$


Its evaluation needs $\mathsf A$ and the contracted $d$-columns through modulo $27$, not merely their old support modulo $3$ or $9$.

The finite convolution also needs its anti-diagonal constants. A support statement does not determine those constants and therefore does not determine (6.5). In particular, at the finer $P$-grid, the outer finite-prefix grid position changes its admission behavior; it cannot be included or excluded uniformly for arbitrary amplitudes without a boundary check.

For the present literal amplitudes, that check must use their exact coefficient support, not just


$$
H_i\bmod3=y^{L_*+i}-y^{L_*+\Pi+i}.
$$



### 6.2 A precise finite-$J$ obstruction at the next digit

The leading finite $J$-block has the form


$$
\overline B_c=
\begin{pmatrix}
0&0&a\\
0&B_I&w\\
a&w^T&c
\end{pmatrix},
\qquad a\ne0.
\tag{6.6}
$$


For a leading contracted column


$$
l_0=(0,l_I,l_\partial),
$$


its inverse image is


$$
(\overline B_c^{-1}l_0)_\partial=0,
$$




$$
(\overline B_c^{-1}l_0)_I=B_I^{-1}l_I,
$$




$$
\boxed{
(\overline B_c^{-1}l_0)_0
=
a^{-1}\bigl(l_\partial-w^TB_I^{-1}l_I\bigr).
}
\tag{6.7}
$$



At the preceding digit, the quadratic expression was independent of $l_\partial$. That does not persist automatically after division by another $3$.

For example, changing the next digit of the first coupling coordinate by


$$
l\longmapsto l+3u\,e_0
$$


changes the divided quadratic return, modulo $3$, by


$$
\boxed{
u\,x_0^T+x_0u^T,
\qquad
x_0=a^{-1}\bigl(l_\partial-w^TB_I^{-1}l_I\bigr).
}
\tag{6.8}
$$


Similarly, a next-digit change $B\mapsto B+3s\,e_0e_0^T$ changes that divided return by


$$
-s\,x_0x_0^T.
\tag{6.9}
$$



Thus the actual last coupling, the actual border entries, and their next digits can enter physical order $6$, even though the leading quadratic return vanished. This is a concrete obstruction to deleting the uncompressed last middle boundary.

It is not an assertion that (6.8) is nonzero on every original index. It identifies the exact source-specific data that must be evaluated before declaring the $J$-return zero.

---

## 7. The paid directional equation and the next actual layer

After the physical-$5$ complement, write the exact retained equation as


$$
B_6x=w_6,\qquad x\in3^{-1}\mathbb Z_3^{\varepsilon-1}.
\tag{7.1}
$$


Here $B_6,w_6$ are the actual normalized returned quantities, including all earlier returns.

The new complement preserves the allowance. If its eliminated block is


$$
A_5=3^5A_{5,0},
$$


and its cross and directional columns are in $3^6$, then


$$
x_C=A_5^{-1}(c_C-Xx_R)
$$


is integral whenever $x_R\in3^{-1}\mathbb Z_3$. Both retained Schur terms are included in (7.1).

### 7.1 Necessary modulo-$9$ test

Put $z=3x$. Then


$$
B_6z=3w_6,\qquad z\in\mathbb Z_3^{\varepsilon-1}.
$$


Writing $z=z_0+3z_1$ modulo $9$, one needs


$$
\overline B_6\,\overline z_0=0,
$$




$$
\boxed{
\overline B_6\,\overline z_1
+
\overline{\frac{B_6z_0}{3}}
=
\overline w_6.
}
\tag{7.2}
$$


The division is paid by the first congruence.

Equivalently, the cokernel class of $\overline w_6$ must lie in the image of


$$
\ker\overline B_6
\longrightarrow \operatorname{coker}\overline B_6,
\qquad
\overline z_0\longmapsto
\left[\overline{B_6z_0/3}\right].
\tag{7.3}
$$


This map depends on $B_6\bmod9$, not only on its leading matrix.

Passing this test is not full $3^{-1}$-solvability. For example,


$$
B=[27],\qquad w=[3]
$$


passes $Bz=3w\pmod9$, but its exact solution is $x=1/9$, outside $3^{-1}\mathbb Z_3$.

### 7.2 What becomes active at physical order $7$

The synchronization proved in Section 2 is only modulo $3^7$. After division by $3^6$, it identifies $B_6,w_6$ modulo $3$, not modulo $9$.

At physical order $7$, the following are active:

1. the leading actual/core difference in (2.1);
2. the new physical-$5$ matrix and directional returns;
3. the next exact endpoint-adaptation terms;
4. the next digits of all returns in (6.2);
5. the source-$33$ stationary projection error if one attempts source precision $34$.

The monomial-frame border correction still starts at physical order $8$, so it does not supply these missing seventh-digit data.

Therefore the necessary test (7.2) cannot be decided from the sixth-digit moment formula or from source precision $33$ alone. A source-$34$ argument must explicitly evaluate or improve the stationary error, rather than silently reuse the source-$33$ compression.

---

## 8. Audit of the other newly supplied candidates

### 8.1 Raw endpoint modulo $9$

The algebraic part of the raw-endpoint candidate is consistent:

- the sign in
  

$$
G_0^Tf_{\alpha,K}
  =\mathcal F_\alpha[\Psi](-1)+9Z_\alpha^Te_{\alpha,\rm prefix}
$$


  follows from $X_\alpha=-A_\alpha^{-1}B_{\alpha,K}G_0$;
- the $J$- and rank-$b$ endpoint corrections are in $9M$ under the quoted contracted-coupling divisibilities;
- at $-1$,
  

$$
(-1)^{3Q}+3=2,\qquad (-2)^{10Q}\equiv1\pmod9,
$$


  and $R_*-k_0=3Q$ is odd.

Thus the proposed residue


$$
f_{\alpha,\rm new}(a)
\equiv-2(-1)^{R_*}a(-1)\pmod9
$$


does follow **if** its quoted physical $p25$ representative, coefficientwise filter congruence, and complete-column perturbation bounds are available at exactly the stated scope.

Those physical certificates are quoted rather than proved in the supplied candidate. This report does not upgrade that stronger endpoint theorem to an independently verified input. It is unnecessary for Sections 2–6.

### 8.2 Uniform second-divided obstruction

The new sector candidate gives a valid independent lower-bound argument, without requiring the gray-range endpoint unit.

Its essential finite-degree check is:


$$
A+B+C=6s+1,\qquad d_0=3s,\qquad A+B>d_0.
$$


The coefficient-triple space has dimension $d_0+2$, whereas the target has dimension $d_0+1$. Hence a nonzero syzygy exists, and its third component cannot vanish.

After the ninth power and multiplication by $(Y-X)^2$, the resulting third coefficient has degree


$$
9s=c-1,
$$


and lies in both specified finite sector kernels. The exponent comparisons in the candidate put it in the actual selected-degree maps, not in an ungraded substitute.

The $243$-sector decomposition then supplies:

- $122$ equal low sectors;
- $119$ equal high sectors;
- one unequal symmetric pair of dimensions $c,c-1$.

This yields


$$
\operatorname{nullity}\mathsf D\ge242,
$$


and hence at least $241$ dimensions in the radical of the endpoint restriction.

This is an obstruction to an immediately nonsingular second-divided annihilator. It is not a physical-$6$ force evaluation or a primitive-denominator estimate.

### 8.3 Saved finite receipts

The supplied $T=243$, $c=46,55,64,73$ receipt remains finite auxiliary evidence. Its matrices have not been rerun. Its agreement with the Turn 7 formula does not establish original-index membership, a higher physical digit, or an infinite-family directional statement.

---

## 9. Global normalization is unchanged

No new global content division is asserted.

The actual column contents and the least simultaneous clearer $\ell_{\rm clr}$ remain those of the original complete construction. Ternary-unit basis changes, including dyadic units, do not redefine them.

The complete source recurrence also remains


$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\qquad 0\le t\le2n-2,
$$


with the genuine resonance


$$
t_*=\frac{3^h-5}{2}.
$$


Its $3^h$ division is not removed by any local Smith calculation.

Retain the actual integers


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the gcd over **all primes**


$$
\boxed{g_\ell=\gcd(|A_\ell|,|B_\ell|).}
$$


For $B_\ell\ne0$, the actual primitive pair is


$$
\boxed{
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
}
\tag{9.1}
$$


The whole error is exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{9.2}
$$



An irrationality proof would follow from


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\log g_\ell-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|\longrightarrow+\infty
\tag{9.3}
$$


at the **same infinite original indices**.

This remains conditional. A fixed local Smith improvement need not survive the final all-prime primitive normalization, and it supplies neither same-index nonvanishing nor decay of the whole error.

---

## 10. Bounded new exact-arithmetic checks

No tool computation was performed.

### 10.1 Universal constant receipt for the new moment calculation

This check is new and does not repeat the saved sector matrices or the closed older pole tables.

**Inputs**


$$
2451,\qquad1084,\qquad1367.
$$



**Expected verifiable outputs**


$$
\begin{array}{c|r|c}
n&v_3(n!)&n!/3^{v_3(n!)}\pmod3\\ \hline
2451&1223&1\\
1084&539&2\\
1367&678&1
\end{array}
$$


and hence


$$
\boxed{
v_3\binom{2451}{1084}=6,\qquad
\binom{2451}{1084}\equiv1458\pmod{2187}.
}
$$



An optional bounded digit check uses


$$
1\le d\le1035,\quad d\ \text{odd},\qquad \ell\in\{1,2,3\},
$$




$$
a=(3d-7)/2-243\ell,
$$


retaining only $0\le a\le816$. It should verify the valuation bounds (4.8), and at $d=729$ return


$$
(\ell,a)=(3,361),(2,604),
$$


with valuation $5$ for both $\binom{816}{a}$; the low case $a=847$ is outside the support.

These bounded checks verify universal constants used in the proof. They are not original-index computations.

### 10.2 Exact inputs needed for a complete sixth-digit receipt

For one **certified original Range III index**, no free scaled replacement, a bounded complete receipt can be specified by the following contracted data:

1. $\mathsf A\bmod27$ and $d\mathscr H\bmod27$, with the complete finite prefix and its anti-diagonal constants;
2. $B_c\bmod9$ and $\mathscr L_H\bmod9$, including the actual last $J$-row and column;
3. $A_{b,c}\bmod3$ and $\mathscr M_H\bmod3$;
4. $A_4\bmod3$ and $\mathscr C_H\bmod3$.

The expected outputs are the four returned matrices in the last four lines of (6.2), the literal complete $C_6$, and then the actual $B_6\bmod3,w_6\bmod3$ from (6.3)–(6.4), with certificates for every unit inverse and paid division.

This is a finite input/output specification, not a claim that those data have been supplied or computed. In particular, it does not yet produce the modulo-$9$ test (7.2); that requires the next actual physical layer.

---

## 11. Conclusion

### New proved statements

1. The parent’s second-kernel-pivot payment is valid in Ranges I–III:
   

$$
\text{physical inverse }3^{-5},\qquad
   \text{matrix and directional returns in }3^7.
$$


   The actual/core sixth digit agrees in the specified same-label frames using only the established endpoint modulo $3$.

2. The diagonal correction is repaired without evaluating an unproved rank-$b$ quadratic unit:
   

$$
\lambda_{\rm new}\in3^{-2}\mathbb Z_3,
   \qquad
   \lambda_4\in3^{-4}\mathbb Z_3
$$


   in their respective exact frames.

3. The corrected-pairing compression extends to source precision $33$, with the newly active logarithmic layer retained.

4. In Range III, the complete-core moment contribution at physical order $6$ is explicitly
   

$$
\boxed{
   C^{\rm mom}_{ij}
   =[y^{(P/9-1)/2-i-j}](1-y)^{P/3-2\chi}\pmod3.
   }
$$


   Its pivot mixed column and endpoint-annihilator matrix are explicitly (5.3)–(5.4).

### Exact remaining local bottleneck

The complete actual physical-$6$ matrix and force still require the **evaluated sum of the four remaining returns in (6.2)**. Their valuation bounds alone do not determine them. The finite $J$-boundary dependence in (6.7)–(6.9) explains precisely why an earlier zero quadratic digit cannot simply be reused one digit later.

If the resulting sixth-digit equation remains singular, the next bottleneck is the actual physical-$7$ matrix and force, including the new physical-$5$ return, actual/core difference, higher endpoint adaptation, and the source-$33$ stationary correction needed for a source-$34$ calculation.

### Global proof status

No same-index nonvanishing theorem, unbounded primitive-denominator saving, or decay theorem for the whole error has been proved.



$$
\boxed{
\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ is obtained.}
}
$$


