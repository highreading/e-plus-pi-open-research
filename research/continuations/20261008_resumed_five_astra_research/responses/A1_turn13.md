> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A precision-sized reduction of the actual terminal coordinate, and a boundary-safe directional equation

## Abstract and proof status

The rationality or irrationality of $e+\pi$ remains unresolved.

The principal unevaluated object in this report is still the **actual finite terminal vector**


$$
\eta=(\eta_0,\ldots,\eta_{k-1})^T
$$


from A1 Turn 12. In particular, I do not infer its value from the vanishing of the $J$-quadratic, from an endpoint congruence modulo $9$, or from a unit assertion about a different scalar.

The new results are the following.

1. **A uniform ten-response reduction.** For each original coordinate $i$, the contraction defining $\eta_i$ is reduced to:
   - three complete terminal responses modulo $9$;
   - seven complete terminal responses modulo $3$;
   - the actual unit $a=B_{\ell,\tau-1}\bmod3$.

   Only fourteen ternary digits are required. The relevant source columns lie in an explicitly proved, twelve-dimensional subspace of the original completely corrected finite space. The reduction retains the true terminal, every $W$- and prefix correction, and the original divisions by $3^{27}$, $3^{28}$, and $3^{29}$.

   This replaces the $3k(t+1)$ coefficient contraction by a fixed-size **source-measurement problem for one coordinate**. It does not, by itself, supply the missing source measurements or make their production by an original large matrix feasible.

2. **An explicit complete-source residual polynomial.** A second formula expresses $\eta_i$ as one terminal response to a factored polynomial $\Omega_P(y)(1-y)^t y^i$. The leading prefix inverse image is incorporated explicitly, rather than omitted.

3. **Two new exact source values.** For $i=0$ and $i=k-1$, the corresponding **unprojected** complete-source pairing is proved to vanish modulo $3^{30}$. Consequently, at these two coordinates the entire remaining value is an explicitly identified $W$-projection return. This is not a proof that either $\eta_0$ or $\eta_{k-1}$ vanishes.

4. **A complete-matrix consequence of the rank-two support.** I prove what can and cannot be concluded by removing the terminal perturbation from bulk tests. In particular, an exact Schur equation retains the unknown last column and the allowed $3^{-1}\mathbb Z_3$ directional payment. Deleting the last row is not a valid substitute.

The outstanding local obligation is now especially concrete: evaluate the ten terminal responses below, or prove the stated complete $W$-return cancellation at one of the two endpoint coordinates. No original factorial matrix, original moment matrix, or $P$-sized coefficient array is proposed for execution.

---

## 1. Original domain and exact finite objects

### 1.1 The original indices

All assertions concern sufficiently large indices in exactly the original family:


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


The retained arithmetic parameters are


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
N_0=25P+2\chi,\qquad D=268P+2\chi,\qquad D+b=10Q.
$$



The subwindow is unchanged:


$$
\boxed{\frac3{25}<\frac{\chi}{P}<\frac{31}{250}.}
\tag{1.1}
$$


Its certified infinitude in the original progression is reused. No independent choice of $P$ and $\chi$ is made.

Put


$$
\Pi=P/3,\qquad c=2\chi,\qquad t=\Pi-c,
$$




$$
\delta=\chi-1,\qquad k=\delta-t=3\chi-\Pi-1.
$$


After removing a finite initial segment, $k\ge2$. Also


$$
v_3(\chi)=5,
\qquad
\chi/243\equiv1\pmod9.
\tag{1.2}
$$



The literal second-kernel amplitudes are


$$
H_i=(1-y)^\Pi y^{L_*+i},
\qquad
L_*=\frac{P-1}{2},
\qquad 0\le i<k.
\tag{1.3}
$$


It will be useful to write


$$
z_i(y)=(1-y)^t y^i,
\qquad
V(y)=1+y^P+y^{2P}.
\tag{1.4}
$$


Then


$$
H_i=(1-y)^c y^{L_*}z_i,
\qquad
\deg z_i=t+i\le\chi-2.
\tag{1.5}
$$


Since $\Pi$ is odd and $c$ is even, $t$ is odd.

### 1.2 Complete corrected columns

Retain


$$
U_s=x^s\quad(0\le s<D),
$$




$$
z^{\rm mid}_i=x^Dy^i\quad(0\le i<\nu),\qquad \nu=D/2-1,
$$




$$
Y_s=y^s\quad(d\le s\le m),\qquad d=D+\nu,
\qquad W=[U\ Y].
$$


The physical HIGH terminal is $Y_m$. It is not the last middle column.

The complete functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^a)=(2a)!.
\tag{1.6}
$$


The physical cutoff is exactly


$$
K_{\rm phys}=2n-2=2H-2D+2,
$$


and


$$
2K_{\rm phys}+1=4H-4D+5<3^{h+1}.
\tag{1.7}
$$



For the complete core,


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A,
$$




$$
G(f,g)=G_c(f,g)=\mathcal M(Q_cfg),
\qquad E=G(W,W),
$$




$$
F[p]=x^Dp-WE^{-1}G(W,x^Dp).
\tag{1.8}
$$


Thus $F[p]$ is the actual complete $W$-corrected column.

The terminal vector in A1 Turn 12 is defined from this complete core block. “Actual terminal” below means the true finite terminal of that block. No separate assertion that the individual core and actual-producer terminal vectors coincide is needed or made.

### 1.3 Prefix and tail boundaries

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
\tag{1.9}
$$


Write $T=\tau-1$ for the last $J$-label and


$$
F_T=F[y^{\nu-1}].
$$


This column is never placed under the ordinary-column compression theorem.

---

## 2. Accepted results reused, and what they do not establish

I reuse the following at their stated scopes:

- the complete corrected-pairing compression through source precision $33$, only on admitted ordinary inputs;
- the accepted finite prefix inverse and the evaluated leading prefix inverse images;
- the accepted finite interior $J$-inverse;
- the closed prefix-$6$ and terminal-aware $J6$ vanishing;
- the source-$33$ second-kernel moment;
- the common second-kernel-pivot frame and its complete payment;
- A1 Turn 12’s source-specific reduction
  

$$
R_b=e_{k-1}\eta^T+\eta e_{k-1}^T.
  \tag{2.1}
$$



The two-antidiagonal source calculation, the mixed-prefix zero, the mixed-interior-$J$ zero, and the rank-$b$ quotient inverse images are not recalculated here.

The accepted endpoint theorem gives


$$
f_{\alpha,\mathrm{new}}(a)
\equiv-2(-1)^{R_*}a(-1)\pmod9.
\tag{2.2}
$$


It does **not** evaluate the terminal coordinate considered here. Section 8 proves the precise reason: the relevant endpoint returns first see that coordinate with an explicit factor $9$.

---

## 3. Exact prefix correction and the actual bordered inverse

### 3.1 Prefix notation and signs

Let $F_{\rm pref}$ be the matrix of columns $F[y^p]$, $0\le p\le a_0$, and put


$$
\mathsf A=-\frac{G(F_{\rm pref},F_{\rm pref})}{3^{26}}.
\tag{3.1}
$$


This is the original unit normalized prefix block.

For a tail polynomial $p$, define


$$
q[p]=-\frac{G(F_{\rm pref},F[p])}{3^{27}}.
$$


On the admitted tail columns, including the true last middle column, the original normalized construction makes $q[p]$ integral. Its exact prefix correction is


$$
\widehat F[p]=F[p]-3F_{\rm pref}\mathsf A^{-1}q[p].
\tag{3.2}
$$


In particular,


$$
G(F_{\rm pref},\widehat F[p])=0.
$$



For the one-lift associated with $H_i$, write


$$
d_i=\frac{G(F_{\rm pref},\mathcal F[H_i])}{3^{28}},
\qquad Z_i=\mathsf A^{-1}d_i.
$$


Then its exact prefix-corrected column is


$$
K_i=\mathcal F[H_i]+9F[Z_i].
\tag{3.3}
$$


The factor $9$ is not optional:


$$
G(F_{\rm pref},K_i)
=3^{28}d_i-9\cdot3^{26}\mathsf A Z_i=0.
$$



The complete $J$-block and coupling are


$$
B_{vw}=-\frac{G(\widehat F_v,\widehat F_w)}{3^{27}},
\qquad
(l_H)_{vi}=-\frac{G(\widehat F_v,K_i)}{3^{29}},
\tag{3.4}
$$


where $\widehat F_v=\widehat F[y^{R_*+v}]$.

### 3.2 The actual terminal remains in the inverse problem

Modulo $3$, the complete block has the form


$$
\overline B=
\begin{pmatrix}
0&0&a\\
0&B_I&w\\
a&w^T&c_\partial
\end{pmatrix},
\qquad a\ne0.
\tag{3.5}
$$


Here:

- $a=\overline B_{\ell,T}$ is the true unit;
- $w_v=\overline B_{T,v}$ is the true last row on the interior;
- $c_\partial=\overline B_{T,T}$ is the true terminal diagonal;
- $\theta_i=\overline{(l_H)_{T,i}}$ is the true terminal coupling.

For the leading inverse image, the first row of (3.5) forces the last inverse coordinate to be zero. The last row then determines the first inverse coordinate. Thus the last row is not deleted.

The accepted interior calculation gives


$$
(B^{-1}l_H)_{vi}
=
-\sum_{q=0}^2c_{J_i-v-qP},
\qquad
c_d=[y^d](1-y)^t,
\tag{3.6}
$$


with


$$
J_i=\frac{23P-1}{2}+t+i.
$$


The resulting first coordinate is precisely


$$
\boxed{
\eta_i=a^{-1}\left(
\theta_i+
\sum_{q=0}^2\sum_{d=0}^t
w_{J_i-qP-d}c_d
\right).
}
\tag{3.7}
$$



Equation (3.7) is retained as the definition to be evaluated, not as an evaluation.

---

## 4. A new ten-response formula

This section gives a fixed-size source reduction of (3.7).

### 4.1 The interior inverse image as one literal polynomial

The complete finite support in (3.6) permits its coefficient vector to be represented by a polynomial without extending an interior sum.

Indeed,


$$
\begin{aligned}
&\sum_{v=\ell+1}^{T-1}
\left(-\sum_{q=0}^2c_{J_i-v-qP}\right)y^{R_*+v}\\
&\qquad
=-y^{R_*+J_i}(1-y^{-1})^t
       (1+y^{-P}+y^{-2P}).
\end{aligned}
$$


Since $t$ is odd,


$$
(1-y^{-1})^t(1+y^{-P}+y^{-2P})
=-y^{-t-2P}(1-y)^tV(y).
$$


Also


$$
R_*+J_i-t-2P=131P+i.
$$


Consequently the actual leading interior inverse image is represented by


$$
\boxed{
\mathcal T_i(y)=y^{131P}V(y)z_i(y).
}
\tag{4.1}
$$



This is a polynomial representation of the accepted finite inverse image, not a virtual continuation of the terminal row.

### 4.2 The one-lift simplifies after exact prefix correction

The ordinary polynomial part of the one-lift is


$$
x^by^{k_0}(y^{3Q}+3)H_i,
\qquad k_0=\frac{3Q+1}{2}.
$$


Using $b+\Pi=2P+t$ and $k_0+L_*=41P$, it is exactly


$$
z_i(y)(1-y)^{2P}\bigl(y^{122P}+3y^{41P}\bigr).
\tag{4.2}
$$



The low summand is entirely inside the prefix:


$$
\deg\!\left(y^{41P}(1-y)^{2P}z_i\right)
\le43P+\chi-2<a_0.
\tag{4.3}
$$


It therefore pairs to zero with $\widehat F_T$ **by exact prefix orthogonality**, not by discarding its coefficient $3$.

Combining (3.4), (3.7), and (4.1), one obtains


$$
\boxed{
a\eta_i
=
-\frac{
G\!\left(
\widehat F_T,\,
F\!\left[
z_i\bigl(y^{122P}(1-y)^{2P}-9y^{131P}V\bigr)
\right]\right)
}{3^{29}}
\pmod3.
}
\tag{4.4}
$$


All prefix corrections remain present: they are incorporated in $\widehat F_T$, and their exact orthogonality is what justifies (4.3).

### 4.3 A stronger normalization on the seven $K$-columns

For $0\le r\le6$, put


$$
M_{r,i}(y)=y^{122P+r\Pi}z_i(y).
\tag{4.5}
$$


Every coefficient of each $M_{r,i}$ lies in the original $K$-tail.

The lower boundary follows from $122P\ge R_*$. For the upper boundary,


$$
\deg M_{r,i}\le124P+\chi-2,
$$


whereas


$$
R_*+3R=\frac{249P+1}{2}-3\chi.
$$


Their difference is


$$
R_*+3R-(124P+\chi-2)
=\frac{P+5}{2}-4\chi>0
\tag{4.6}
$$


on (1.1).

Therefore the original $K/J$ normalization gives


$$
G(\widehat F_T,\widehat F[M_{r,i}])
\in3^{28}\mathbb Z_3.
\tag{4.7}
$$



This extra source digit is the reason a modulo-$9$, rather than modulo-$27$, polynomial replacement is sufficient.

Repeated cubing gives


$$
(1-y)^{2P}\equiv(1-y^\Pi)^6\pmod9.
\tag{4.8}
$$


The error in the first term of (4.4) is thus $9$ times an admitted $K$-polynomial. By (4.7), its terminal pairing belongs to $3^{30}\mathbb Z_3$.

For $q=0,1,2$, put


$$
N_{q,i}(y)=y^{(131+q)P}z_i(y).
\tag{4.9}
$$


These are wholly inside the original $J$-interior. In particular,


$$
\deg N_{q,i}\le133P+\chi-2
<\nu-2=134P+\chi-3
$$


for sufficiently large $P$. Their source normalization is


$$
G(\widehat F_T,\widehat F[N_{q,i}])
\in3^{27}\mathbb Z_3.
\tag{4.10}
$$



### 4.4 Definition of the ten complete responses

Define the actual complete responses


$$
\mathsf t_{r,i}
=
\frac{G(\widehat F_T,\widehat F[M_{r,i}])}{3^{28}},
\qquad 0\le r\le6,
\tag{4.11}
$$


and


$$
\mathsf u_{q,i}
=
\frac{G(\widehat F_T,\widehat F[N_{q,i}])}{3^{27}},
\qquad 0\le q\le2.
\tag{4.12}
$$


These are integral in the original normalization.

Since


$$
(1-X)^6
=1-6X+15X^2-20X^3+15X^4-6X^5+X^6,
$$


equation (4.4) becomes


$$
\boxed{
a\eta_i
=
-\frac{
\mathsf t_{0,i}-6\mathsf t_{1,i}
+15\mathsf t_{2,i}-20\mathsf t_{3,i}
+15\mathsf t_{4,i}-6\mathsf t_{5,i}
+\mathsf t_{6,i}
}{3}
+\sum_{q=0}^2\mathsf u_{q,i}
\pmod3.
}
\tag{4.13}
$$



The numerator divided by $3$ is integral. This follows from the original integrality of $l_H$, together with the paid error estimate following (4.8). In particular,


$$
\mathsf t_{0,i}+\mathsf t_{3,i}+\mathsf t_{6,i}
\equiv0\pmod3.
\tag{4.14}
$$



Set


$$
\kappa_i=
\frac{\mathsf t_{0,i}+\mathsf t_{3,i}+\mathsf t_{6,i}}3
\pmod3.
\tag{4.15}
$$


Then the ten-response formula simplifies to


$$
\boxed{
a\eta_i=
-\kappa_i
+\overline{\mathsf t}_{3,i}
-\overline{\mathsf t}_{1,i}
+\overline{\mathsf t}_{2,i}
+\overline{\mathsf t}_{4,i}
-\overline{\mathsf t}_{5,i}
+\overline{\mathsf u}_{0,i}
+\overline{\mathsf u}_{1,i}
+\overline{\mathsf u}_{2,i}.
}
\tag{4.16}
$$



Thus only the following data are needed:

| Data | Required modulus | Complete pairing precision |
|---|---:|---:|
| $a$ | $3$ | $3^{28}$ |
| $\mathsf t_{0,i},\mathsf t_{3,i},\mathsf t_{6,i}$ | $9$ | $3^{30}$ |
| $\mathsf t_{1,i},\mathsf t_{2,i},\mathsf t_{4,i},\mathsf t_{5,i}$ | $3$ | $3^{29}$ |
| $\mathsf u_{0,i},\mathsf u_{1,i},\mathsf u_{2,i}$ | $3$ | $3^{28}$ |

There are fourteen ternary digits in total.

These are **complete corrected-pairing precisions**. They do not permit an unprojected source to be truncated at the same modulus before paying an inverse. In particular, the $3^{-1}$ allowance for $E^{-1}$ must still be paid by any producer of these source digits.

### 4.5 The explicit finite embedding, and its limitation

For a fixed $i$, all required measurements occur in the restriction of the complete prefix-returned form to the twelve columns


$$
\widehat F_T,\quad
\widehat F_\ell,\quad
\widehat F[M_{0,i}],\ldots,\widehat F[M_{6,i}],\quad
\widehat F[N_{0,i}],\ldots,\widehat F[N_{2,i}].
\tag{4.17}
$$



The boundary estimates above prove that these are original admitted columns or literal combinations of them. Their distinct leading degrees prove independence in the original tail quotient:

- the seven $M$-columns have leading-degree gaps $\Pi>\deg z_i$;
- their highest degree is below the first $J$-column;
- the three $N$-columns lie strictly in the $J$-interior and have leading-degree gaps $P$;
- the true last column lies above all three.

Thus (4.17) is a genuine twelve-dimensional finite embedding.

There is, however, an important limitation:

> A twelve-column restriction is not automatically a twelve-dimensional algorithm for constructing its complete entries.

The $W$-projection and prefix projection in (4.17) remain the original ones. Replacing them by projections in a newly constructed $12\times12$ moment matrix would be invalid. Formula (4.16) is a rigorously paid fixed-size **measurement reduction**; the source-specific production of its missing measurements remains an open part of the primary task.

---

## 5. A second new reduction: one explicit residual polynomial

A useful alternative puts the prefix correction into the polynomial input and leaves only the complete $W$-projection on the terminal side.

The accepted leading prefix inverse image, specialized to $z_i$, is


$$
\overline Z_i
=
2(y^{14P}+y^{41P}+y^{95P})V(y)z_i(y).
\tag{5.1}
$$


All its coefficients lie in the actual prefix. This evaluated inverse image is reused; its source table is not repeated.

Define


$$
\boxed{
\begin{aligned}
\Omega_P(y)={}&
(1-y)^{2P}\bigl(y^{122P}+3y^{41P}\bigr)\\
&+9V(y)
\bigl(2y^{14P}+2y^{41P}+2y^{95P}-y^{131P}\bigr).
\end{aligned}
}
\tag{5.2}
$$



### Proposition 5.1 — complete residual identity

For every original $0\le i<k$,


$$
\boxed{
a\eta_i
=
-\frac{G(F_T,F[\Omega_Pz_i])}{3^{29}}
\pmod3.
}
\tag{5.3}
$$



#### Proof

The leading interior inverse image is represented by $\mathcal T_i$ in (4.1). Therefore


$$
a\eta_i
=
-\frac{
G(\widehat F_T,K_i-9\widehat F[\mathcal T_i])
}{3^{29}}
\pmod3.
\tag{5.4}
$$



Both columns in the second argument are exactly prefix-orthogonal, so $\widehat F_T$ can be replaced by $F_T$ in this pairing.

For a $J$-interior polynomial $\mathcal T_i$,


$$
\widehat F[\mathcal T_i]
=
F[\mathcal T_i]
-3F_{\rm pref}\mathsf A^{-1}q[\mathcal T_i].
$$


After multiplication by $9$, the additional prefix column has coefficient $27$. Since


$$
G(F_T,F_{\rm pref})\in3^{27}M,
$$


its pairing contributes only in $3^{30}\mathbb Z_3$.

Similarly, replacing $Z_i$ in $9F[Z_i]$ by the lift displayed in (5.1) changes that pairing only in $3^{30}\mathbb Z_3$. Substitution of (4.2), (4.1), and (5.1) now gives exactly (5.2)–(5.3). ∎

This proof pays both the finite prefix-return correction and the error in replacing an integral inverse image by its leading residue.

### 5.1 Complete stationary form

Since $F_T$ is $W$-orthogonal,


$$
G(F_T,F[\Omega_Pz_i])
=
\mathcal M(Q_cF_Tx^D\Omega_Pz_i).
\tag{5.5}
$$



Put


$$
g_T=G(W,x^Dy^{\nu-1}),
\qquad
b_i=G(W,x^D\Omega_Pz_i).
\tag{5.6}
$$


Then the exact complete stationary identity is


$$
\boxed{
G(F_T,F[\Omega_Pz_i])
=
G(x^Dy^{\nu-1},x^D\Omega_Pz_i)
-g_T^TE^{-1}b_i.
}
\tag{5.7}
$$


The whole $W$-return is present. In particular, it includes the physical HIGH terminal $Y_m$.

---

## 6. Two evaluated source values: the bare responses at $i=0$ and $i=k-1$

The following vanishing is new. Its scope is deliberately stated narrowly.

### Theorem 6.1

For sufficiently large original indices in (1.1),


$$
\boxed{
G(x^Dy^{\nu-1},x^D\Omega_Pz_i)
\equiv0\pmod{3^{30}},
\qquad i=0,\ k-1.
}
\tag{6.1}
$$



This is an unprojected pairing. It is not a value of the complete pairing in (5.3).

### 6.1 Physical support

Because $Q_c(-1)=0$, the rational part of this bare pairing is obtained from the polynomial


$$
x^{A+2D}(\beta+3y)y^{\nu-1}\Omega_Pz_i.
\tag{6.2}
$$


Its degree is at most


$$
H+535P+4\chi-3.
$$


Since $H=3^{31}P$, this is below


$$
K_{\rm phys}=2H-536P-4\chi+2.
$$


Its largest denominator is also below


$$
3H=3^h.
\tag{6.3}
$$


Thus the actual cutoff is respected, and every active pole weight has valuation at least $1$.

The factorial term in (1.6) is divisible by $3^h$, since its polynomial input has integral coefficients. It is therefore invisible modulo $3^{30}$ for the original sufficiently large $h$.

### 6.2 Cancellation of the $\chi$-dependence in the binomial tops

There are two types of binomial factors in (6.2). After including $z_i=(1-y)^t y^i$, their exponents are


$$
H+D+t=H+268P+\Pi
$$


and


$$
H+D+t+2P=H+270P+\Pi.
$$


Equivalently,


$$
H+268P+\Pi=(3^{32}+805)\Pi,
$$




$$
H+270P+\Pi=(3^{32}+811)\Pi.
\tag{6.4}
$$


Both have exact valuation


$$
h-33.
\tag{6.5}
$$



This cancellation uses the original identity $t=\Pi-2\chi$. It would be lost if $P,\chi,t$ were replaced by independently chosen experimental parameters.

### 6.3 Active coefficient indices

A pole visible modulo $3^{30}$ has odd denominator $d$ satisfying


$$
v_3(d)\ge h-29.
$$


For a macro-shift $y^{aP}$ in $\Omega_P$, and for the term $\beta$ or $3y$, write $\epsilon=0$ or $1$. The binomial coefficient index is


$$
r=
\frac{d-(268+2a)P+3}{2}
-\chi-i-\epsilon.
\tag{6.6}
$$



For $i=0$, this gives


$$
v_3(r)=
\begin{cases}
1,&\epsilon=0,\\
0,&\epsilon=1.
\end{cases}
\tag{6.7}
$$


Indeed, modulo a sufficiently high power of $3$,


$$
r\equiv\frac32-\chi-\epsilon,
$$


and $v_3(\chi)=5$.

For $i=k-1=3\chi-\Pi-2$,


$$
r\equiv\frac72-4\chi-\epsilon\pmod{\Pi},
$$


so


$$
v_3(r)=0
\qquad(\epsilon=0,1).
\tag{6.8}
$$



If an extraction lies outside the coefficient interval, it is zero. Otherwise, for either binomial top $N$ in (6.4),


$$
\binom Nr=\frac Nr\binom{N-1}{r-1}
$$


implies


$$
v_3\binom Nr\ge h-33-v_3(r).
\tag{6.9}
$$



The weakest case is $i=0,\epsilon=0$, where the coefficient valuation is at least $h-34$. The pole weight adds at least one digit by (6.3), giving valuation at least $h-33$. For $h\ge63$, this is at least $30$. The $3y$ term and the terms already multiplied by $3$ or $9$ are no weaker.

All active poles therefore vanish modulo $3^{30}$. Inactive poles and the factorial contribution do as well. This proves (6.1). ∎

### 6.4 What remains at these two coordinates

Combining (5.3), (5.7), and (6.1) yields


$$
\boxed{
\eta_i
=
a^{-1}\frac{g_T^TE^{-1}b_i}{3^{29}}
\pmod3,
\qquad i=0,\ k-1.
}
\tag{6.10}
$$


The quotient is integral: that follows from (5.3) and the proved bare vanishing.

Equation (6.10) identifies the exact obstruction at these coordinates. The entire value is a complete $W$-return. Neither $\eta_0$ nor $\eta_{k-1}$ has been evaluated until that return is evaluated.

---

## 7. A concrete follow-on terminal lemma

There are now two precise routes to closing a first coordinate.

### 7.1 Ten-response cancellation lemma

For $i=0$, or separately for $i=k-1$, prove the complete-source identity


$$
\boxed{
\kappa_i=
\overline{\mathsf t}_{3,i}
-\overline{\mathsf t}_{1,i}
+\overline{\mathsf t}_{2,i}
+\overline{\mathsf t}_{4,i}
-\overline{\mathsf t}_{5,i}
+\overline{\mathsf u}_{0,i}
+\overline{\mathsf u}_{1,i}
+\overline{\mathsf u}_{2,i}.
}
\tag{7.1}
$$


By (4.16), this is exactly sufficient for the corresponding $\eta_i=0$.

The hypotheses of this lemma are not unspecified matrix data: all ten columns, their finite positions, and their required complete source precisions are given in (4.5), (4.9), and the table following (4.16).

Uniform vanishing of $\eta$ would require (7.1) for every original $0\le i<k$. Checking it at one coordinate or one tuple would not prove that uniform statement.

### 7.2 Complete $W$-return cancellation lemma

At either endpoint coordinate, the new bare-source theorem gives the more focused sufficient statement


$$
\boxed{
g_T^TE^{-1}b_i\in3^{30}\mathbb Z_3,
\qquad i=0\ \text{or}\ k-1.
}
\tag{7.2}
$$


Here $b_i$ is defined using the explicit polynomial $\Omega_Pz_i$, not an unnamed arbitrary source.

A possible proof certificate for (7.2), with the inverse loss fully paid, is the following:

> Construct a compactly described integral $W$-coordinate vector $\zeta_i$ for which
> 

$$
> b_i-E\zeta_i\in3^{31}M
>
$$


> and
> 

$$
> g_T^T\zeta_i\in3^{30}\mathbb Z_3.
>
$$


> Since $E^{-1}\in3^{-1}M(\mathbb Z_3)$ and $g_T$ is integral, these two statements imply (7.2).

No such $\zeta_i$ is supplied here. This is a concrete next proof obligation, not a proposed large linear solve. Its verification must come from a source-specific symbolic or independently validated precision-local representation.

---

## 8. Why the accepted endpoint and $J6$ results do not determine $\eta$

### 8.1 The endpoint congruence is one digit too shallow

The exact endpoint returns are


$$
f^{(2)}=f_K-3LB^{-1}f_J,
$$




$$
f_{\mathrm{new}}
=G_0^Tf^{(2)}-3M_b^TA_b^{-1}f_b.
\tag{8.1}
$$


On $H_i$,


$$
L^TG_0H_i=3l_H{}_i.
$$


Thus the $J$-endpoint return is


$$
-9\,l_H{}_i^TB^{-1}f_J.
\tag{8.2}
$$


Its leading inverse image contains


$$
\eta_i e_\ell+\text{the evaluated interior vector}.
$$


Hence any dependence on $\eta_i$ in (8.2) has an explicit factor $9$.

Similarly, $M_bH_i\in3M$, so the rank-$b$ endpoint return on $H_i$ also begins with a factor $9$.

Therefore the accepted congruence


$$
f_{\mathrm{new}}(H_i)\pmod9
$$


is insensitive to these values. An identification of $\eta_i$ with a zero endpoint jet modulo $9$ would be invalid. A stronger endpoint identity, in the same frame and with both returns paid, would be necessary.

### 8.2 The $J$-quadratic can conceal every first inverse coordinate

The leading bordered solve is


$$
\overline{B^{-1}l_H{}_i}
=
\eta_i e_\ell+X_i,
$$


where the terminal coordinate of $X_i$ is zero.

The accepted terminal-aware $J6$ proof shows that every coefficient of the first inverse coordinate in the relevant quadratic vanishes modulo $9$. This is precisely why that theorem does not evaluate the coordinate itself.

An algebraic diagnostic makes the obstruction explicit. Keep the ordinary block, $a,w,c_\partial$, and all ordinary couplings fixed, and replace only


$$
\theta_i\longmapsto\theta_i+a\lambda_i.
$$


Then


$$
\eta_i\longmapsto\eta_i+\lambda_i.
\tag{8.3}
$$


The leading finite border remains a unit border. The already proved ordinary contractions and their terminal-parameter cancellation in the $J$-quadratic are unchanged. The endpoint conclusions modulo $9$ are also unchanged, by (8.2).

This is not asserted to be an available perturbation of the actual producer. It proves a narrower and relevant point:

> The accepted finite-border, $J6$, and modulo-$9$ endpoint identities do not logically determine the missing terminal response.

The complete source, specifically the return in (6.10) or the measurements in (4.16), must supply the additional information.

---

## 9. Consequences for the complete physical-$6$ matrix

### 9.1 Assembly in the accepted common frame

Retain the accepted moment contribution


$$
C^{\rm mom}_{ij}
=[y^{\kappa_2-i-j}](1-y)^t,
\qquad
\kappa_2=\frac{P/9-1}{2}.
\tag{9.1}
$$


Let


$$
R_4=C_H^TA_4^{-1}C_H
$$


be the actual first physical-$4$ complementary return. It remains unevaluated.

The complete physical-$6$ matrix is


$$
\boxed{
C_6=C^{\rm mom}
-\bigl(e_{k-1}\eta^T+\eta e_{k-1}^T\bigr)
-R_4
\pmod3.
}
\tag{9.2}
$$


The closed prefix-$6$ and $J6$ results are used here only to remove their sixth-digit contributions.

Use the accepted common second-kernel pivot


$$
\gamma H_0,\qquad
\gamma=(\sigma2^t)^{-1},
\qquad
\sigma=(-1)^{R_*+L_*},
$$


and the adjacent-annihilator matrix $N$, whose columns are $e_i+e_{i+1}$. Then


$$
a_6=\bar\gamma^2(C_6)_{00},
\qquad
w_6=\bar\gamma N^TC_6e_0,
\qquad
B_6=N^TC_6N.
\tag{9.3}
$$



No other pivot from a differently returned frame is substituted.

### 9.2 The first-$4$ term is still present

For clarity, the unevaluated first-$4$ term retains


$$
P_{ui}
=\frac{d_u^T\mathsf A^{-1}d_i}{3}\pmod3.
\tag{9.4}
$$


Writing $r_{ui}=P-1-u-i$, its cross column remains


$$
\boxed{
(C_H)_{ui}
=
-c_{r_{ui}-\Pi}
+c_{r_{ui}-2\Pi}
-2\,\mathbf1_{u=R,\ i=k-1}
-P_{ui}
\pmod3.
}
\tag{9.5}
$$


The upper-corner $3y$ term is retained.

The inverse in $R_4$ is the original finite $A_4^{-1}$ on the original monomial complement. No auxiliary inverse is substituted, and no $P$-sized calculation of it is proposed here.

---

## 10. What survives a bulk removal of the rank-two perturbation

The following is a new consequence for the **complete equation**, not merely for a principal submatrix.

Put


$$
C^0=C^{\rm mom}-R_4,
$$




$$
B^0=N^TC^0N,\qquad
w^0=\bar\gamma N^TC^0e_0,
$$


and set


$$
e=e_{k-2}\in\mathbb F_3^{k-1},
\qquad h=N^T\eta.
$$


Then


$$
\boxed{
\overline B_6=B^0-eh^T-he^T,
\qquad
\overline w_6=w^0-\bar\gamma\eta_0e.
}
\tag{10.1}
$$



### 10.1 Restricting the quadratic form is not enough

Partition the annihilator coordinates into the first $k-2$ bulk coordinates and the last coordinate. Write


$$
B^0=
\begin{pmatrix}
D&q^0\\
(q^0)^T&d^0
\end{pmatrix},
\qquad
w^0=\binom r{s^0},
\qquad
h=\binom{h_U}{h_T}.
$$


Then the complete leading equation is


$$
\begin{pmatrix}
D&q^0-h_U\\
(q^0-h_U)^T&d^0-2h_T
\end{pmatrix}
\binom{x_U}{x_T}
=
\binom r{s^0-\bar\gamma\eta_0}.
\tag{10.2}
$$



The bulk principal matrix $D$ and the bulk force $r$ are independent of $\eta$. But the bulk equation is


$$
Dx_U+(q^0-h_U)x_T=r.
\tag{10.3}
$$


The unknown last variable enters it. Solving $Dx_U=r$ after deleting the last column is not justified.

### 10.2 A subspace that removes the perturbation from full left tests

Define


$$
\mathcal U=
\left\{
u\in\mathbb F_3^{k-1}:
u_T=0,\quad h_U^Tu_U=0
\right\}.
\tag{10.4}
$$


Then


$$
\dim\mathcal U\ge k-3.
$$


For every $u\in\mathcal U$,


$$
u^T(eh^T+he^T)=0,
\qquad
u^T(\bar\gamma\eta_0e)=0.
$$


Consequently a solution of the full leading equation must satisfy


$$
\boxed{
u^TB^0x=u^Tw^0
\qquad(u\in\mathcal U).
}
\tag{10.5}
$$


This statement retains every component of $x$, including $x_T$.

The subspace $\mathcal U$ depends on the still unknown $h$; it is not an explicit evaluated bulk basis. Nevertheless, the consequence is rigorous. Likewise,


$$
\operatorname{rank}(\overline B_6-B^0)\le2,
$$


so


$$
\operatorname{nullity}\overline B_6
\ge\operatorname{nullity}B^0-2.
\tag{10.6}
$$


These are leading finite-matrix facts, not content or denominator theorems.

### 10.3 Exact bulk elimination with the allowed $3^{-1}$-direction

Now use the actual integral $3$-adic matrix and vector in the accepted frame, not just their reductions:


$$
B_6=
\begin{pmatrix}
D_{\rm ex}&q_{\rm ex}\\
q_{\rm ex}^T&d_{\rm ex}
\end{pmatrix},
\qquad
w_6=\binom{r_{\rm ex}}{s_{\rm ex}}.
\tag{10.7}
$$


Assume, as an explicit hypothesis for this paragraph, that


$$
\overline{D_{\rm ex}}\ \text{is nonsingular}.
$$


Then $D_{\rm ex}^{-1}$ is integral, and the full equation


$$
B_6x=w_6,\qquad x\in3^{-1}\mathbb Z_3^{k-1},
$$


is equivalent to


$$
x_U=D_{\rm ex}^{-1}(r_{\rm ex}-q_{\rm ex}x_T),
$$




$$
\boxed{
\Delta x_T=\rho,
}
\tag{10.8}
$$


where


$$
\Delta=d_{\rm ex}-q_{\rm ex}^TD_{\rm ex}^{-1}q_{\rm ex},
$$




$$
\rho=s_{\rm ex}-q_{\rm ex}^TD_{\rm ex}^{-1}r_{\rm ex}.
\tag{10.9}
$$


The allowance is exactly


$$
x_T\in3^{-1}\mathbb Z_3.
$$


Therefore:

- if $\Delta\ne0$, a solution exists exactly when
  

$$
v_3(\rho)\ge v_3(\Delta)-1;
$$


- if $\Delta=0$, a solution exists exactly when $\rho=0$.

The unknown last column is retained in both $\Delta$ and $\rho$.

The unit-bulk hypothesis has not been established for the present complete $D_{\rm ex}$, because $R_4$ is still open. Thus (10.8) is a conditional implication, not a completed directional solve.

### 10.4 A small diagnostic showing why deletion can change the answer

Even with the same unit bulk $D=1$ and bulk force $r=0$, consider


$$
B(q)=
\begin{pmatrix}
1&q\\q&0
\end{pmatrix},
\qquad
w=\binom01.
$$


For $q=0$, the full equation has no solution. For $q=1$, it has the integral solution


$$
x=\binom1{-1}.
$$


Thus the same bulk restriction can coexist with opposite full solvability conclusions.

This example is an algebraic diagnostic only. It is not an original-index computation.

---

## 11. The next digit and all inverse payments remain necessary

The allowed direction is still


$$
B_6x=w_6,\qquad x\in3^{-1}\mathbb Z_3^{k-1}.
$$


Writing $z=3x$ gives


$$
B_6z=3w_6.
$$


For $z=z_0+3z_1$, the first two equations are


$$
\overline B_6\overline z_0=0,
$$




$$
\overline B_6\overline z_1
+\overline{B_6z_0/3}
=\overline w_6.
\tag{11.1}
$$


Hence even a complete evaluation of $B_6,w_6\bmod3$ would not settle the directional allowance.

At physical $7$, the whole calculation must retain:

- the actual/core difference;
- the physical-$5$ complementary matrix return;
- the physical-$5$ kernel-pivot directional return;
- higher exact endpoint adaptation;
- the next digits of all earlier returns;
- the stationary term active at source precision $34$.

Source precision $33$ is not a whole source-$34$ theorem.

The two diagonal payments also remain distinct:


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
\tag{11.2}
$$


No unit numerator is assumed.

---

## 12. Bounded exact arithmetic: what is and is not proposed

No tools were used. No accepted source table, closed prefix audit, or closed $J$-quadratic calculation is requested again.

### 12.1 A genuinely fixed-size arithmetic receipt

Once certified complete source digits are available for a specified original coordinate $i$, the arithmetic in (4.16) has the following bounded inputs:

1. $a\in\{1,2\}$;
2. $\mathsf t_{0,i},\mathsf t_{3,i},\mathsf t_{6,i}\in\mathbb Z/9\mathbb Z$;
3. $\mathsf t_{1,i},\mathsf t_{2,i},\mathsf t_{4,i},\mathsf t_{5,i}\in\mathbb F_3$;
4. $\mathsf u_{0,i},\mathsf u_{1,i},\mathsf u_{2,i}\in\mathbb F_3$.

The expected verifiable output is:

- the divisibility certificate
  

$$
\mathsf t_{0,i}+\mathsf t_{3,i}+\mathsf t_{6,i}\equiv0\pmod3;
$$


- the carry $\kappa_i$ from (4.15);
- the single residue $\eta_i\in\{0,1,2\}$ from (4.16).

The universal coefficient input is only


$$
(1-X)^6\bmod9
=
1+3X+6X^2+7X^3+6X^4+3X^5+X^6,
$$


which is directly checkable from the seven ordinary binomial coefficients.

The result $\eta_i=0$ is an output to be determined, not an expected value imposed on the calculation.

### 12.2 Required provenance of those inputs

The source digits must be certified as the complete pairings in (4.11)–(4.12), within the original twelve-column embedding (4.17). In particular:

- the true terminal must be used;
- the physical $Y_m$ must remain in $W$;
- the complete $W$-return and prefix return must be included;
- the stated source divisions must be paid.

The report does not provide a validated precision-local producer for these eleven measured entries. Therefore I do **not** advertise their construction as an already feasible original-index experiment, and I do not propose computing them from a large original inverse.

A receipt for one coordinate at one tuple has exactly that finite scope. A uniform theorem still requires a symbolic evaluation on the same infinite original family.

---

## 13. Complete forcing and unchanged global normalization

The complete producer remains


$$
Q_{\rm act}=Q_c+3^7\mathscr R.
$$


Retain


$$
F_{\rm fac}=(n-1)!,
$$




$$
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},
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


The complete signed coefficients and endpoint are


$$
[x^a](3^7\mathscr R)
=
-\frac{F_{\rm fac}}{a!}
\bigl((t_{\rm force})_a+\xi v_a\bigr),
\qquad 0\le a\le n-1,
$$




$$
\mathscr R(-1)=-\frac{\xi F_{\rm fac}^2}{3^7}.
\tag{13.1}
$$


These formulas are retained as definitions of the actual source; no computation of the original $T_n$ is proposed.

The complete forcing identity is still


$$
\boxed{
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
}
\tag{13.2}
$$


Neither forcing term nor the terminal coordinate is removed.

The complete moment recurrence remains


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
\tag{13.3}
$$



All actual integer column contents and the actual least simultaneous clearer $\ell_{\rm clr}$ remain unchanged. The local ternary reductions in this report do not replace either by a convenient power of $3$.

Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,
\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the final gcd over **all primes**


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


For $B_\ell\ne0$, the actual primitive pair is


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
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
\tag{13.4}
$$



An irrationality proof would require, at the same infinite original indices,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\log g_\ell-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|
\longrightarrow+\infty.
\tag{13.5}
$$


These conditions make the nonzero whole errors tend to zero. If $e+\pi$ were rational with denominator $d$, every such nonzero error would have absolute value at least $1/d$, a contradiction.

No condition in (13.5) is established by a local rank or terminal-coordinate calculation.

---

## 14. Conclusion

### New proved statements

On the certified infinite original Range III subwindow:

1. The target coordinate has the fixed-size, fully normalized formula
   

$$
\boxed{
   a\eta_i=
   -\kappa_i+\overline{\mathsf t}_{3,i}
   -\overline{\mathsf t}_{1,i}
   +\overline{\mathsf t}_{2,i}
   +\overline{\mathsf t}_{4,i}
   -\overline{\mathsf t}_{5,i}
   +\sum_{q=0}^2\overline{\mathsf u}_{q,i}.
   }
$$


   Its fourteen required ternary digits are measurements in an explicitly validated twelve-column restriction of the original complete finite form.

2. The complete residual polynomial $\Omega_P$ in (5.2) gives
   

$$
\boxed{
   a\eta_i=-G(F_T,F[\Omega_Pz_i])/3^{29}\pmod3.
   }
$$


   Its derivation pays the original prefix inverse image and every finite return used in the reduction.

3. At $i=0$ and $i=k-1$, the bare complete-source response is exactly zero modulo $3^{30}$. The remaining actual value is
   

$$
\boxed{
   \eta_i=a^{-1}g_T^TE^{-1}b_i/3^{29}\pmod3.
   }
$$


   Thus the unresolved contribution at these coordinates is specifically the whole $W$-return, including the physical terminal.

4. The rank-two terminal perturbation can be removed from suitable full left tests, but not by deleting a row. Under a unit-bulk hypothesis, the complete allowed directional equation reduces to the exact scalar condition (10.8)–(10.9), retaining the unknown last column.

### Exact remaining local bottleneck

The actual values of the ten terminal responses have not yet been supplied or uniformly proved. In particular, neither $\eta_0$ nor $\eta_{k-1}$ is closed.

The next concrete lemma is the complete-source cancellation (7.1), or, at either endpoint coordinate, the more focused $W$-return bound (7.2). The accepted endpoint and $J6$ theorems cannot replace that lemma: their insensitivity to $\eta$ is proved in Section 8.

After $\eta$ is evaluated, the first physical-$4$ mixed prefix digit and the actual finite $A_4$-inverse application remain necessary. The complete directional payment then still requires the whole physical-$7$ data, including source $34$.

### Global proof status

The actual contents, least simultaneous clearer, all-prime final gcd, actual primitive denominator, same-index nonvanishing, and decay of the nonzero whole error remain open.



$$
\boxed{
\text{The new result is a paid constant-size terminal-measurement reduction,}
\quad
\text{not an unconditional proof of rationality or irrationality of }e+\pi.
}
$$


