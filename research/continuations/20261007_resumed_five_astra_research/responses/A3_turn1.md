> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual-seed elimination of the Green prefix and a forced transverse recurrence

## Executive summary

The rationality or irrationality of $e+\pi$ remains unresolved.

This report makes two advances on the actual seeded system, without changing the approximation domain or the finite producer.

1. **The physical exponential source admits an exact symbolic integration.** Its polynomial multiplier factors as
   

$$
(n+1)-nz+\frac{n-1}{2}z^2+\frac12z^3
   =q(z)(n+1+z).
$$


   This eliminates the Green prefix as a Green-kernel sum and gives an explicit generating function for the actual seed-subtracted response.

2. **The complete transverse response satisfies a first-order forced recurrence in the parameter $n$.** Writing
   

$$
\mathcal K_n=\frac{\mathscr K_n^\circ}{L_n}
$$


   at original indices, and defining $\mathcal K_n$ without $L_n$ at auxiliary indices, the recurrence is
   

$$
\boxed{\mathcal K_{n+1}=-(n+1)^2\mathcal K_n+\gamma_nY_n,}
$$


   where $Y_n=(P_n,Q_n,F_n)\otimes(\tau_n,\tau_{n+1})$, the row $\gamma_n$ is explicit below, and
   

$$
\boxed{\mathcal K_2=14.}
$$


   Thus the unresolved transverse correlation can be studied in a seven-dimensional, explicitly seeded polynomial-coefficient system, rather than through an unevaluated Green prefix.

The new recurrence does **not** by itself prove a gcd bound. It does, however, turn a bounded-endpoint elimination into a concrete rational-gauge equation with six unknown rational functions. A bounded exact-arithmetic test for a specified class of such certificates is given at the end.

On the alignment side, the globally valid scalar chart yields an actual-seed congruence for the **whole evaluated telescope**. At terminal alignment depth $a_t>0$, a canonically specified seed charge $\eta_t$ is a $p$-adic unit, and


$$
\boxed{
-\sum_{s=n}^{t-1}
\frac{u_{31,s}x_s+u_{32,s}y_s}{F_{s+1}}
\equiv \eta_t
\pmod{p^{\,a_t-v_p(F_n)}}
}
$$


whenever $v_p(F_n)<a_t$. This is a congruence for the complete sum, not for its summands. It does not yet bound alignment acquisition.

Finally, the separate height of unselected contact collision is rigorously unnecessary for the stated saturation budget:


$$
\boxed{
\mathfrak S_0\mathfrak S_3\mid J_{\rm res}^{\,2}.
}
$$


Consequently the required saturation estimate is exactly an estimate for $J_{\rm res}$, not for all of $C_{\rm sat}$.

No target-specific transverse Bézout certificate against the actual primitive contact reference denominators is established here. No subfactorial acquisition estimate is established. No infinite family of favorable nonzero primitive whole forms is established.

---

## 1. Domain, source scope, and notation

The approximation domain is unchanged:


$$
\boxed{n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2.}
$$


For a multiplicative block,


$$
t=bn,\qquad b\in\{15,105\}.
$$



Consecutive integers below are auxiliary recurrence indices only. In particular, the normalization


$$
L_n=2^{(n+1)/2}
$$


is used as the original integral normalization only at the original odd indices.

Put


$$
q(z)=1-z+\frac{z^2}{2},\qquad
A_n(z)=e^zq(z)^n,
$$


and


$$
a_k(n)=k![z^k]A_n(z).
$$


When the parameter is understood, write $a_k=a_k(n)$.

The actual moment observations are


$$
X_n=(n+1)a_n(n),\qquad
Y_n^{\rm mom}=(n+1)n\,a_{n-1}(n),
$$




$$
Z_n=2a_{n+1}(n)-(n+1)a_n(n),
$$




$$
P_n=nX_n+Y_n^{\rm mom},\qquad
Q_n=nZ_n+2X_n-Y_n^{\rm mom},
$$




$$
F_n=2(n+1)(Z_n-Q_n).
$$


To avoid conflicting uses of $Y$, the tensor state introduced later will be denoted $\mathbf Y_n$.

The supplied proofs establish the natural transfer


$$
z_{n+1}=\mathsf U_nz_n,\qquad z_n=(P_n,Q_n,F_n)^T,
$$


with genuine seed


$$
z_2=(0,10,-66)^T,
$$


and


$$
\mathsf U_n=
\begin{pmatrix}
0&(n+1)(n+2)&(n+2)/2\\
n+2&-(n^2+3n+1)&-\dfrac{n(n+2)}{2(n+1)}\\
-(n+2)(2n+3)&(n+2)(n^2+3n+1)&
\dfrac{(n+2)(n^2-2)}{2(n+1)}
\end{pmatrix}.
\tag{1.1}
$$



The reference pair satisfies


$$
(n+2)\tau_{n+2}=(2n+3)\tau_{n+1}+(n+1)\tau_n,
$$


with


$$
(\tau_2,\tau_3)=(2,4).
$$


Thus, for


$$
y_n=(\tau_n,\tau_{n+1})^T,
$$




$$
y_{n+1}=\mathsf R_ny_n,\qquad
\mathsf R_n=
\begin{pmatrix}
0&1\\
\dfrac{n+1}{n+2}&\dfrac{2n+3}{n+2}
\end{pmatrix}.
\tag{1.2}
$$



The archive already contains actual-seed scalar reduction, evaluated finite Green identities, and saturation identities. Those are reused, not claimed anew. The new derivation below is the parameter recurrence for the complete transverse response obtained from the actual differential equation.

A limitation of the supplied documents must also be explicit: the complete original entries of the finite matrix $T$, its physical return functional, and formulas for the actual primitive contact rows are referenced but not reproduced. Accordingly, the supplied contact and final-normalization theorems can be retained at their stated hypotheses, but a new independently checkable contact resultant cannot be manufactured from the syzygy condition alone.

---

## 2. Exact symbolic elimination of the physical Green prefix

### 2.1 The source factorization

Let


$$
B_n(z)=\sum_{k\ge0}b_k(n)\frac{z^k}{k!}
$$


denote the actual seed-subtracted response appearing in the sources. Its lower seed is


$$
B_n(0)=-1.
$$



The retained differential equation is


$$
(1-z)q(z)B_n'(z)
-\bigl(n(1-z)q'(z)+(n+1)q(z)\bigr)B_n(z)
=\mathfrak f_n(z),
\tag{2.1}
$$


where


$$
\mathfrak f_n(z)=
\left(n+1-nz+\frac{n-1}{2}z^2+\frac12z^3\right)A_n(z).
$$



The crucial actual-source identity is


$$
\boxed{
n+1-nz+\frac{n-1}{2}z^2+\frac12z^3
=q(z)(n+1+z).
}
\tag{2.2}
$$


No source coordinate is varied in this identity.

Since


$$
qA_n'=(q+nq')A_n,
$$


the left-hand operator in (2.1), applied to $A_n$, gives


$$
-(n+z)qA_n.
$$


Consequently


$$
V_n:=B_n+A_n
$$


satisfies


$$
(1-z)qV_n'
-\bigl(n(1-z)q'+(n+1)q\bigr)V_n=qA_n,
\qquad V_n(0)=0.
\tag{2.3}
$$



Divide $V_n$ by the actual factor $q^n$:


$$
V_n=q^nU_n.
$$


Equation (2.3) becomes


$$
\boxed{(1-z)U_n'-(n+1)U_n=e^z,\qquad U_n(0)=0.}
\tag{2.4}
$$



This is the first substantial simplification: the remaining source is exactly $e^z$.

### 2.2 Explicit integration

Define the polynomial


$$
S_n(z)=\sum_{j=0}^n(n)_j(1-z)^{n-j}
      =n!\sum_{k=0}^n\frac{(1-z)^k}{k!},
\tag{2.5}
$$


and the integer seed charge


$$
E_n=S_n(0)=n!\sum_{k=0}^n\frac1{k!}.
\tag{2.6}
$$


Then


$$
S_n'+S_n=(1-z)^n.
$$


Therefore


$$
\boxed{
U_n(z)=\frac{e^zS_n(z)-E_n}{(1-z)^{n+1}},
}
\tag{2.7}
$$


and


$$
\boxed{
B_n(z)
=-A_n(z)
+\frac{q(z)^n}{(1-z)^{n+1}}
       \bigl(e^zS_n(z)-E_n\bigr).
}
\tag{2.8}
$$



This is an exact symbolic elimination of the Green-kernel prefix.

It is not yet a bounded-endpoint formula: $S_n$ has degree $n$. That distinction matters. Formula (2.8) replaces an unevaluated Green sum by an explicit polynomial antiderivative and one fixed seed charge; it does not establish that a bounded number of moment offsets suffice.

### 2.3 Exact coefficient form

Write


$$
U_n(z)=\sum_{k\ge0}u_k(n)\frac{z^k}{k!}.
$$


Equation (2.4) gives


$$
u_0(n)=0,\qquad
u_{k+1}(n)=(n+k+1)u_k(n)+1.
$$


Hence


$$
\boxed{
u_k(n)=(n+k)!\sum_{j=n+1}^{n+k}\frac1{j!}.
}
\tag{2.9}
$$



This formula is integral, as is also immediate from its recurrence. Together with


$$
V_n=q^nU_n,\qquad B_n=V_n-A_n,
$$


it determines the actual response without arbitrary forcing coordinates.

### 2.4 What has and has not been truncated

Equation (2.8) is an identity of formal series. Its use to evaluate $b_n,b_{n+1}$ does not truncate the physical producer.

The original source still runs through


$$
\boxed{K=2n+2,}
$$


and the coefficient of $\mathfrak f_K$ in $b_{K+1}$ remains $1$. The retained physical terminal-return functional is unchanged. Neither the logarithmic forcing nor either exponential boundary column is removed.

---

## 3. A two-coordinate parameter recurrence for the actual response

The antiderivative polynomials satisfy


$$
S_{n+1}=(n+1)S_n+(1-z)^{n+1},
\qquad
E_{n+1}=(n+1)E_n+1.
$$


Substituting into (2.7) yields


$$
(1-z)U_{n+1}
=(n+1)U_n+e^z-\frac1{(1-z)^{n+1}}.
\tag{3.1}
$$



Let


$$
H_n(z)=\frac{q(z)^n}{(1-z)^{n+1}}.
$$


Combining (3.1) with (2.4) gives


$$
\boxed{
V_{n+1}=qV_n'-nq'V_n-H_{n+1}.
}
\tag{3.2}
$$



The last term is the actual homogeneous reference function. Replacing it by $q^{n+1}/(1-z)$ would be incorrect; the full power $(1-z)^{n+2}$ is essential.

Define ordinary endpoint coefficients


$$
v_n=[z^n]V_n,\qquad w_n=[z^{n+1}]V_n,
$$




$$
d_n=[z^n]A_n=\frac{a_n(n)}{n!},\qquad
e_n=[z^{n+1}]A_n=\frac{a_{n+1}(n)}{(n+1)!}.
$$



The known homogeneous endpoint identities are


$$
[z^n]H_n=\tau_n,\qquad
[z^{n+1}]H_n=\frac{\tau_n+\tau_{n+1}}2.
\tag{3.3}
$$



### Proposition 3.1 — Actual two-coordinate forced recurrence

For every auxiliary $n\ge2$,


$$
\boxed{
v_{n+1}
=-(n+1)v_n+2(n+1)w_n+d_{n+1}-\tau_{n+1},
}
\tag{3.4}
$$


and


$$
\boxed{
\begin{aligned}
w_{n+1}
={}&-(n+1)v_n
+\frac{(n+1)(3n+5)}{n+2}w_n\\
&+\frac{2n+3}{n+2}d_{n+1}+e_{n+1}
-\frac{\tau_{n+1}+\tau_{n+2}}2.
\end{aligned}}
\tag{3.5}
$$



The actual seed is


$$
\boxed{(v_2,w_2)=\left(\frac12,\frac43\right).}
\tag{3.6}
$$



#### Derivation

If $v_{n,k}=[z^k]V_n$, equation (2.3) gives


$$
\begin{aligned}
(k+1)v_{n,k+1}
={}&(2k+1)v_{n,k}
+\frac{2n+1-3k}{2}v_{n,k-1}\\
&+\frac{k-n-1}{2}v_{n,k-2}
+[z^k]A_{n+1}.
\end{aligned}
\tag{3.7}
$$


At $k=n+1$,


$$
(n+2)v_{n,n+2}
=(2n+3)w_n-\frac{n+2}{2}v_n+d_{n+1}.
\tag{3.8}
$$



Meanwhile, coefficient extraction from (3.2) gives


$$
[z^k]V_{n+1}
=(k+1)v_{n,k+1}
+(n-k)v_{n,k}
+\left(\frac{k-1}{2}-n\right)v_{n,k-1}
-[z^k]H_{n+1}.
\tag{3.9}
$$


Use $k=n+1$ and (3.8) to obtain (3.4). Use $k=n+2$, then (3.7) at $k=n+2$, followed by (3.8), to obtain (3.5).

For the seed, equation (2.9) at $n=2$ gives


$$
u_1=1,\qquad u_2=5,\qquad u_3=26.
$$


Since


$$
q^2=1-2z+2z^2-z^3+\frac14z^4,
$$


one obtains $v_2=1/2$ and $w_2=4/3$. ∎

The recurrence has only the displayed denominator $2(n+2)$. It is not a constant-coefficient recurrence.

---

## 4. The complete transverse response has a first-order forced recurrence

Define, at every auxiliary index,


$$
\boxed{
\mathcal K_n
=
\tau_n b_{n+1}(n)
-\frac{n+1}{2}(\tau_n+\tau_{n+1})b_n(n).
}
\tag{4.1}
$$


At original indices,


$$
\mathscr K_n^\circ=L_n\mathcal K_n.
$$



Set


$$
g_n=(v_n,\,2w_n-v_n)^T.
$$


Equations (3.4)–(3.5) become


$$
g_{n+1}
=(n+1)\mathsf R_ng_n+
\binom{
d_{n+1}
}{
\dfrac{3n+4}{n+2}d_{n+1}+2e_{n+1}
}
-y_{n+1}.
\tag{4.2}
$$



Because $y_{n+1}=\mathsf R_ny_n$, taking determinants gives


$$
\begin{aligned}
\det(y_{n+1},g_{n+1})
={}&-\frac{(n+1)^2}{n+2}\det(y_n,g_n)\\
&+\det\!\left(
y_{n+1},
\binom{
d_{n+1}
}{
\dfrac{3n+4}{n+2}d_{n+1}+2e_{n+1}
}
\right).
\end{aligned}
\tag{4.3}
$$


The complete homogeneous seed term $-y_{n+1}$ disappears here because its determinant with $y_{n+1}$ is zero.

Now


$$
(d_n,\,2e_n-d_n)^T
=\frac1{(n+1)!}(X_n,Z_n)^T,
$$


and (4.1) is equivalently


$$
\mathcal K_n
=\frac{(n+1)!}{2}
\left[
\det(y_n,g_n)
-\det\bigl(y_n,(d_n,2e_n-d_n)^T\bigr)
\right].
\tag{4.4}
$$



### Theorem 4.1 — Actual seeded transverse recurrence

For every auxiliary $n\ge2$,


$$
\boxed{
\begin{aligned}
\mathcal K_{n+1}
={}&-(n+1)^2\mathcal K_n\\
&+(2n+3)\tau_{n+1}a_{n+1}(n+1)\\
&-\frac{(n+1)^2}{2}
   \bigl(\tau_nZ_n-\tau_{n+1}X_n\bigr).
\end{aligned}}
\tag{4.5}
$$


Its actual initial value is


$$
\boxed{\mathcal K_2=14.}
\tag{4.6}
$$



#### Proof

Substitute (4.3) into (4.4) at $n+1$, and use (4.4) at $n$. The terms involving $e_{n+1}$ cancel. The remaining moment forcing is exactly the last two lines of (4.5).

At $n=2$,


$$
a_2(2)=1,\qquad a_3(2)=1,
$$


so


$$
b_2=2!\left(\frac12-\frac12\right)=0,\qquad
b_3=3!\left(\frac43-\frac16\right)=7.
$$


Hence


$$
\mathcal K_2=2\cdot7-\frac32(2+4)\cdot0=14.
$$


∎

This recurrence retains the whole response. In particular, it has not discarded either final physical source term. Their contributions are incorporated through the exact differential equation used in its derivation.

### 4.1 Explicit tensor forcing

The identity


$$
a_{n+1}(n+1)
=\frac12\bigl(P_n+Z_n-(n+1)X_n\bigr)
\tag{4.7}
$$


follows from the retained diagonal moment identities.

Also,


$$
Z_n=Q_n+\frac{F_n}{2(n+1)},
$$




$$
X_n=\frac{P_n-(n-1)Q_n-\dfrac{nF_n}{2(n+1)}}{n+2}.
\tag{4.8}
$$



Order the six actual tensor coordinates as


$$
\mathbf Y_n=
(P_n\tau_n,\ P_n\tau_{n+1},\
 Q_n\tau_n,\ Q_n\tau_{n+1},\
 F_n\tau_n,\ F_n\tau_{n+1})^T.
$$


Then


$$
\mathbf Y_{n+1}
=(\mathsf U_n\otimes\mathsf R_n)\mathbf Y_n,
\tag{4.9}
$$


and (4.5) is


$$
\boxed{\mathcal K_{n+1}=-(n+1)^2\mathcal K_n+\gamma_n\mathbf Y_n,}
\tag{4.10}
$$


where


$$
\boxed{
\gamma_n=
\left(
0,\frac{n+2}{2},
-\frac{(n+1)^2}{2},
\frac{(n+1)^2+1}{2},
-\frac{n+1}{4},
\frac{n^2+3n+3}{4(n+1)}
\right).
}
\tag{4.11}
$$



The complete seed is


$$
\boxed{
\mathbf Y_2=(0,0,20,40,-132,-264)^T,\qquad
\mathcal K_2=14.
}
\tag{4.12}
$$


As a small hand check,


$$
\gamma_2\mathbf Y_2=-77,\qquad
\mathcal K_3=-9\cdot14-77=-203.
$$



This seven-coordinate system is a concrete reduction of the actual seeded response. No free source parameters occur.

---

## 5. Bounded endpoint elimination: the precise remaining equation

### 5.1 A simple rational generating-function gauge does not exist uniformly

One might try to write $B_n=r(n,z)A_n$, up to the homogeneous seed term, with $r\in\mathbb Q(n,z)$. Such a particular solution would require


$$
(1-z)\frac{\partial r}{\partial z}-(n+z)r=n+1+z.
\tag{5.1}
$$



There is no solution in $\mathbb Q(n,z)$.

Indeed, a pole away from $z=1$ would produce an uncancellable highest-order pole from the derivative. A pole of order $d>0$ at $z=1$ would have leading coefficient multiplied by


$$
d-n-1.
$$


For a rational function over $\mathbb Q(n)$, $d$ is a fixed integer, so this cannot vanish identically in $n$. Thus $r$ would have to be polynomial in $z$. Its highest-degree term in $-(n+z)r$ forces it to be constant; the coefficient of $z$ then forces $r=-1$, which gives $n+z$, not $n+1+z$.

For each fixed integer $n$, the pole of order $n+1$ in (2.8) is possible. What is excluded is a rational generating-function gauge of uniformly bounded complexity.

This does **not** exclude a bounded relation among evaluated endpoint moments. Coefficient evaluation can create identities not represented by such a generating-function gauge.

### 5.2 A target-specific rational-gauge equation

A bounded endpoint formula linear in the six actual moment-reference tensors would have the form


$$
\mathcal K_n=\ell(n)\mathbf Y_n,
\tag{5.2}
$$


for a rational row $\ell(n)\in\mathbb Q(n)^6$.

The exact certificate equation is


$$
\boxed{
\ell(n+1)(\mathsf U_n\otimes\mathsf R_n)
+(n+1)^2\ell(n)=\gamma_n.
}
\tag{5.3}
$$



This is not a generic source-coordinate elimination. Every matrix and every forcing coefficient in it belongs to the actual moment/reference system.

If (5.3) holds, then


$$
\mathcal K_n-\ell(n)\mathbf Y_n
=c\,(-1)^{n-2}\left(\frac{n!}{2}\right)^2
\tag{5.4}
$$


for a fixed seed discrepancy $c$.

For the actual solution, a rational gauge cannot hide a nonzero discrepancy of this size. Here is a direct justification.

Choose a fixed circle $|z|=\rho<1$. From


$$
V_n(z)=H_n(z)\int_0^z e^w(1-w)^n\,dw,
$$


one obtains


$$
\sup_{|z|=\rho}|A_n(z)|+
\sup_{|z|=\rho}|V_n(z)|\le e^{C_\rho n}.
$$


Cauchy coefficient estimates give


$$
|b_n|+|b_{n+1}|\le n!e^{Cn}.
$$


The reference endpoints and actual moments obey the corresponding exponential/factorial bounds, so


$$
|\mathcal K_n|+\|\mathbf Y_n\|\le n!e^{C'n}.
\tag{5.5}
$$


Multiplication by a fixed rational function of $n$ changes this bound only by a polynomial factor. A nonzero right side of (5.4), however, has order $(n!)^2$. Therefore $c=0$.

Thus:

> **Conditional endpoint-elimination statement.**  
> Any rational solution of (5.3), valid for all sufficiently large integers, automatically gives the actual-seed identity (5.2) there. Its seed discrepancy must vanish.

This is a useful restriction on a prospective certificate. It is not a proof that such a rational solution exists.

### 5.3 Denominator payment

Suppose a certificate is found in the form


$$
\ell(n)=\frac{\mathbf A(n)}{\delta D(n)},
\qquad
\mathbf A(n)\in\mathbb Z[n]^6,\quad \delta>0.
$$


Then the paid endpoint identity is


$$
\boxed{
\delta D(n)\mathscr K_n^\circ
=L_n\,\mathbf A(n)\mathbf Y_n.
}
\tag{5.6}
$$



The complete affine scalar would become


$$
\boxed{
\delta D(n)\Theta
=
\delta D(n)CM
+F\left(
\delta D(n)\,2L_n(n!)^2
-L_n\mathbf A(n)\mathbf Y_n
\right).
}
\tag{5.7}
$$



The factor $2L_n(n!)^2$ remains complete. Neither it nor any prime in $\delta D(n)$ may be cancelled without proof.

For the bounded test proposed below,


$$
D(n)=n(n+1)(n+2).
$$


At $p>N=n+2$, this polynomial denominator is a unit. The fixed integer $\delta$ must still be recorded; its prime factors are eventually below the moving threshold, but not automatically below it at every finite index.

No such $\ell$, $\delta$, or endpoint certificate has been computed in this report.

---

## 6. Explicit holonomic upper bounds and the contact limitation

### 6.1 Seven-dimensional transverse system

The system (4.9)–(4.10) has common denominator


$$
4(n+1)(n+2).
$$


After multiplication by this denominator, every matrix entry is a polynomial of degree at most $5$. Hence its coefficient heights are $O(\log n)$ per step.

This is a fixed-size, fully seeded polynomial-coefficient system. It is not a C-finite system.

The transverse coordinate is scalar and first-order once the six actual tensor forcings are retained. I do **not** assert that seven is the minimal holonomic dimension over $\mathbb Q(n)$: deciding whether this extension splits is precisely the rational-gauge problem (5.3).

### 6.2 A closed system containing $F$, $M$, and $\Theta$

Put


$$
k_n=2(n!)^2,\qquad k_{n+1}=(n+1)^2k_n.
$$


At original indices,


$$
\frac{\Theta_n}{L_n}
=(n+1)Z_n\overline M_n+F_nk_n-F_n\mathcal K_n,
$$


where


$$
\overline M_n=Q_n\tau_n-P_n\tau_{n+1}.
\tag{6.1}
$$



A closed homogeneous linear system can therefore be formed from

- $z_n$, dimension $3$, to observe $F_n$;
- $z_n\otimes y_n$, dimension $6$, to observe $\overline M_n$;
- $\operatorname{Sym}^2(z_n)\otimes y_n$, dimension $12$;
- $z_n\mathcal K_n$, dimension $3$;
- $z_nk_n$, dimension $3$.

This gives an explicit upper bound of $27$ coordinates. Its seed is completely determined by


$$
z_2=(0,10,-66),\quad y_2=(2,4),\quad
\mathcal K_2=14,\quad k_2=8.
$$



For example,


$$
(z\mathcal K)_{n+1}
=-(n+1)^2\mathsf U_n(z\mathcal K)_n
+\mathsf U_nz_n\,(\gamma_n\mathbf Y_n),
$$


and the last term is a linear observation of
$\operatorname{Sym}^2(z_n)\otimes y_n$.

A common denominator is


$$
8(n+1)^2(n+2);
$$


after clearing it, degree at most $9$ suffices for all the transition entries. These are explicit degree bounds, not gcd-growth estimates.

### 6.3 Why the actual primitive contacts have not been appended

The actual contact rows are not specified by


$$
c_j\cdot z_n=0
$$


alone. Their construction includes a particular finite matrix, particular corrected columns, and actual content divisions.

Moreover, gcd-based primitive normalization is not automatically a holonomic operation. A recurrence for raw contact coordinates would not, without further work, be a recurrence for the paid primitive coordinates or for


$$
D_j=\frac{|\widehat R_j|}{\gcd(|\widehat R_j|,|F|)}.
$$



Thus the $27$-coordinate system is an explicit upper bound for the moment, reference, and complete transverse observations—not a claimed minimal system for the actual primitive contacts.

To complete the requested contact calculation, one needs the original finite formulas for the actual rows, including their content payments, and then a certificate using those evaluated rows. The supplied syzygy and cross-product identities cannot substitute for that input.

---

## 7. Consequences for seeded resonance

### 7.1 The separate $C_{\rm sat}$-height burden is removable

Retain the established actual-contact hypotheses:

- $c_0,c_3$ are the actual paid primitive contact-coordinate rows;
- their coordinate contents have no prime above $N$;
- they annihilate the actual primitive state;
- their cross product is the stated nonzero contact multiple;
- the retained saturation theorem applies to the complete seeded affine data.

Under these hypotheses,


$$
\mathfrak S_j=\gcd(|T_{\rm aff}|,D_j)_{>N},
$$


and


$$
J_{\rm res}
=\operatorname{lcm}(\mathfrak S_0,\mathfrak S_3).
$$


Therefore


$$
\boxed{
\mathfrak S_0\mathfrak S_3
=J_{\rm res}\gcd(\mathfrak S_0,\mathfrak S_3)
\mid J_{\rm res}^2.
}
\tag{7.1}
$$


Since also $J_{\rm res}\mid\mathfrak S_0\mathfrak S_3$,


$$
\boxed{
\log(\mathfrak S_0\mathfrak S_3)=o(n\log n)
\iff
\log J_{\rm res}=o(n\log n).
}
\tag{7.2}
$$



In particular, the retained budgets can be written


$$
\boxed{
\mathfrak X_0\mathfrak X_3\mid \mathcal I_n^2J_{\rm res}^2,
}
\tag{7.3}
$$


and


$$
\boxed{
\Delta_0\Delta_3
\mid
\mathcal I_n^2\mathcal Z_0\mathcal Z_3J_{\rm res}^2.
}
\tag{7.4}
$$



This rigorously removes any need to bound the unselected height of all of $C_{\rm sat}$ for these budgets. It does not estimate $J_{\rm res}$.

### 7.2 What the new recurrence contributes

The complete numerator remains


$$
T_{\rm aff}
=\frac{CM+F\bigl(2L_n(n!)^2-L_n\mathcal K_n\bigr)}
       {\gcd(|F|,|CM|)}.
\tag{7.5}
$$


The new result is that $\mathcal K_n$ is now an explicitly seeded coordinate of (4.9)–(4.10).

This exposes a concrete route:

1. solve or obstruct the actual rational-gauge equation (5.3);
2. if it splits, substitute the resulting paid endpoint formula into (7.5);
3. compute a Bézout certificate against the **actual** $D_0,D_3$, after all prescribed normalizations.

There is an important target distinction. A resultant involving $F$ alone cannot control all resonance: primes with $v_p(F)=0$ can still contribute to


$$
\gcd(T_{\rm aff},D_j).
$$


Adding $F$ as an extra generator to an elimination ideal can therefore discard precisely the unit-force branch that must be retained.

The needed certificate is against the normalized actual reference denominator:


$$
A_nT_{\rm aff}+B_nH_{\rm ref}=C_n
$$


in the prescribed localized ring, with


$$
\log(C_n)_{>N}=o(n\log n).
\tag{7.6}
$$


Neither (4.10) nor a prospective identity involving $F$ alone proves (7.6).

### 7.3 Geometric indices

The recurrence is valid at every auxiliary step, but evaluating it at


$$
n=15^r\quad\text{or}\quad105^r
$$


does not confer a known gcd theorem.

Products over the $14n$ or $104n$ intervening steps have coefficients of logarithmic height generally bounded only at the $O(n\log n)$ scale by direct multiplication. That is not the required little-$o$ estimate.

No constant-coefficient recurrence gcd theorem applies to (4.9)–(4.10) without a separate proved reduction. No such reduction is supplied here.

---

## 8. An actual-seed congruence for the complete alignment telescope

This section gives a congruence for the whole evaluated telescope, rather than another formula for its pointwise denominator.

Fix an original block $n\le s\le t=bn$, and put


$$
r_s=\mathsf W_{s,t}^{-1}(\tau_t,\tau_{t+1},0)^T.
$$


The chart is globally valid by the supplied proof that $F_s\ne0$.

Let


$$
a_t=\min\{v_p(F_t),v_p(\overline M_t)\},
\qquad p>t+2.
$$



### 8.1 A fixed seed charge

Transport the actual terminal reference all the way to the genuine seed:


$$
r_2=\mathsf W_{2,t}^{-1}(\tau_t,\tau_{t+1},0)^T.
$$


Define


$$
\boxed{\eta_t=\frac{(r_2)_2}{10}.}
\tag{8.1}
$$


This charge uses the actual seed coordinate $Q_2=10$. It is not an adjustable reference-frame coefficient.

Every denominator introduced by (8.1) has prime support at most $t+2$: the inverse transfers have the retained small-prime-supported denominators, the reference coefficients are dyadic, and $10$ is a unit at $p>t+2$.

### Theorem 8.1 — Seeded whole-telescope congruence

If $a_t>0$, then $\eta_t\in\mathbb Z_p^\times$, and for every $2\le s\le t$,


$$
\boxed{r_s\equiv\eta_tz_s\pmod{p^{a_t}}.}
\tag{8.2}
$$



Consequently, if


$$
f_n:=v_p(F_n)<a_t,
$$


then


$$
\boxed{
\lambda_n\equiv\eta_t\pmod{p^{a_t-f_n}},
\qquad v_p(\lambda_n)=0,
}
\tag{8.3}
$$


and hence


$$
\boxed{
-\sum_{s=n}^{t-1}
\frac{u_{31,s}x_s+u_{32,s}y_s}{F_{s+1}}
\equiv\eta_t\pmod{p^{a_t-f_n}}.
}
\tag{8.4}
$$



#### Proof

The actual terminal decomposition is


$$
z_t=\sigma_tv_t+\overline M_tw_t+F_te_3,
\qquad v_t=(\tau_t,\tau_{t+1},0)^T,
$$


with $\sigma_t$ a unit on terminal alignment. Therefore


$$
v_t\equiv\sigma_t^{-1}z_t\pmod{p^{a_t}}.
$$


All backward transfers are in $\operatorname{GL}_3(\mathbb Z_p)$, so


$$
r_s\equiv\sigma_t^{-1}z_s\pmod{p^{a_t}}.
$$


At the seed, $Q_2=10$ is a unit. Taking the second coordinate and dividing by $10$ gives


$$
\eta_t\equiv\sigma_t^{-1}\pmod{p^{a_t}}.
$$


This proves (8.2) and the unit assertion.

Taking the third coordinate at $n$ gives


$$
F_n\lambda_n-\eta_tF_n\in p^{a_t}\mathbb Z_p.
$$


Division by $F_n$ gives (8.3). The exact complete telescope is


$$
\lambda_n
=-\sum_{s=n}^{t-1}
\frac{u_{31,s}x_s+u_{32,s}y_s}{F_{s+1}},
$$


which proves (8.4). ∎

### 8.2 Scope and remaining acquisition problem

The congruence says something genuinely seed-dependent about the evaluated sum: in the specified regime, the whole telescope is a unit with a prescribed residue.

It does not say that its individual summands are integral. All intermediate $F_s$ and scalar off-diagonal divisions remain paid until the complete sum is evaluated.

It also does not cover the complementary regime $v_p(F_n)\ge a_t$, nor does it bound the aggregate depth


$$
\sum_{p>t+2}(a_t-a_n)_+\log p.
$$



The primitive exterior payment remains exactly $\mathcal I_t$. No primitive normalization was made in the proof.

The exact moving-threshold inventory also remains


$$
\mathcal I_t
=
\frac{\mathcal I_n\,c^{\min}_{n,t}}
     {\mathcal M_{n,t}\mathcal L_{n,t}},
$$


with


$$
\mathcal M_{n,t}
=
\prod_{n+2<p\le t+2}
p^{\min(v_p(F_n),v_p(M_n))}
$$


and


$$
\mathcal L_{n,t}
=
\prod_{p>t+2}p^{(a_n-a_t)_+}.
$$


Neither factor is suppressed.

Finally, the reference composition still has two potentially cancelling summands:


$$
\boldsymbol\delta_{n,t}
=
\boldsymbol\delta_{n,u}\alpha_{u,t}
+\mathsf D_{n,u}\boldsymbol\delta_{u,t}.
$$


The new congruence does not turn $\alpha_{u,t}$ into a unit under weaker hypotheses than those already proved.

---

## 9. Original finite construction and final arithmetic

None of the preceding identities changes the producer.

### 9.1 Complete forcing and return

The complete source remains


$$
\mathfrak f_k
=(n+1)a_k-nk\,a_{k-1}
+\frac{(n-1)k(k-1)}2a_{k-2}
+\frac{k(k-1)(k-2)}2a_{k-3},
$$


through $K=2n+2$, with the original terminal return.

The complete endpoint residual remains


$$
\boxed{
C_j^{\rm complete}
=
\mathcal E_j^\circ+
2n!(n+1)!\bigl(\alpha_j\rho_n+\beta_j\rho_{n+1}\bigr).
}
\tag{9.1}
$$


It is not replaced by the transverse response.

### 9.2 Corrected columns and the least eight-entry clearer

Retain


$$
x=T^{-1}(n!t),\qquad y=T^{-1}\widehat w,
$$




$$
S=
\begin{pmatrix}
1&-n&n(n+1)\\
0&1&-2n\\
0&0&1
\end{pmatrix},
\qquad sx=Sx,\quad sy=Sy,
$$




$$
u=(-sx_0,\ sx_0-sx_1,\ sx_1-sx_2,\ sx_2),
$$




$$
v=(1-sy_0,\ sy_0-sy_1,\ sy_1-sy_2,\ sy_2).
$$



The exterior $+1$ is retained.

Explicitly, if $\operatorname{den}(r)$ is the positive reduced denominator of a rational number,


$$
D_8=\operatorname{lcm}_{0\le j\le3}
\bigl(\operatorname{den}(u_j),\operatorname{den}(v_j)\bigr).
$$


The actual row content is


$$
g_j=\gcd(|D_8u_j|,|D_8v_j|),
$$


and the row is divided by this all-prime $g_j$.

The accepted $3375$ contents remain


$$
(113940000,\ 9780750,\ 10125,\ 1).
$$


No new producer calculation is requested.

### 9.3 Actual primitive denominators

The endpoint denominator remains


$$
\boxed{
d_j=
\frac{|n!R_j|}
{\gcd(|n!R_j|,\ |E_nR_j+C_j^{\rm complete}|)}.
}
\tag{9.2}
$$



For the retained reduced weight $\lambda=a/k_{\rm wt}$, retain


$$
J_{\rm wt}=B_{\rm wt}\widetilde v_0-A_{\rm wt}\widetilde v_3,
$$




$$
T_{\rm wt}=aJ_{\rm wt}+k_{\rm wt}A_{\rm wt}\widetilde v_3,
$$




$$
F_{\rm gcd}
=
\gcd(|A_{\rm wt}|,|a|)
\gcd(|B_{\rm wt}|,|a-k_{\rm wt}|),
$$




$$
G_{\rm wt}=\gcd(k_{\rm wt},|J_{\rm wt}|),
$$




$$
H_{\rm gcd}
=
\gcd\!\left(
h_{\rm end},
\frac{|T_{\rm wt}|}{F_{\rm gcd}G_{\rm wt}}
\right).
$$


Then


$$
\boxed{
q_\lambda=
\frac{k_{\rm wt}h_{\rm end}|A_{\rm wt}B_{\rm wt}|}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}},
\qquad
p_\lambda=
\operatorname{sgn}(A_{\rm wt}B_{\rm wt})
\frac{T_{\rm wt}}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}}.
}
\tag{9.3}
$$



Every gcd here is all-prime. Neither the denominator in (5.6) nor the primitive denominator of $\Theta/F$ replaces $q_\lambda$.

### 9.4 Whole same-index error

The whole error remains


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}).
}
\tag{9.4}
$$



A successful irrationality argument must prove that this expression is nonzero and tends to zero on the **same infinite set of original indices** on which the arithmetic estimates are established. None of the new recurrences proves that assertion.

---

## 10. Bounded exact-arithmetic calculation

No computation was executed. No $3375$ or $11025$ producer, alignment, or whole-form computation is requested.

The following bounded symbolic calculation directly tests the newly isolated endpoint-elimination obligation.

### Inputs

Use the explicitly displayed matrices $\mathsf U_n,\mathsf R_n$, the row $\gamma_n$, and the seed $\mathbf Y_2,\mathcal K_2$.

Set


$$
D(n)=n(n+1)(n+2),
$$


and seek


$$
\ell_i(n)=\frac{A_i(n)}{D(n)},\qquad
A_i(n)=\sum_{j=0}^6c_{ij}n^j,\qquad 1\le i\le6.
$$


There are exactly $42$ rational unknowns $c_{ij}$.

Impose


$$
\ell(n+1)(\mathsf U_n\otimes\mathsf R_n)
+(n+1)^2\ell(n)-\gamma_n=0
$$


and


$$
\ell(2)\mathbf Y_2=14.
$$



Multiplication by


$$
4(n+1)(n+2)D(n)D(n+1)
$$


turns the six rational identities into polynomial identities of degree at most $14$. Thus at most $90$ coefficient equations, plus one seed equation, suffice.

### Expected verifiable output

Either:

1. **A rational solution**, reported as six explicit polynomials, together with:
   - their common coefficient denominator $\delta$;
   - six identically zero cleared residual polynomials;
   - the exact seed residual $0$;
   - the paid endpoint identity (5.6);

or:

2. **An exact inconsistency certificate** for this $42$-unknown rational linear system, such as a row-reduction certificate producing $0=1$.

A negative result would exclude only this specified denominator and degree class. It would not prove the nonexistence of every rational gauge or every bounded-endpoint identity.

A positive result would prove the actual endpoint identity, but **not** the desired resonance gcd estimate. The next calculation would then require the complete original formulas for the actual primitive contact rows and their paid reference denominators.

---

## 11. Proof ledger and remaining bottleneck

| Statement | Status |
|---|---|
| Exact physical source factorization (2.2) | **Proved** |
| Explicit actual response (2.8) | **Proved** |
| Actual two-coordinate parameter recurrence | **Proved** |
| Complete transverse recurrence with seed $\mathcal K_2=14$ | **Proved** |
| Seven-dimensional transverse holonomic upper bound | **Proved** |
| Uniform rational generating-function gauge $B=rA+\text{homogeneous}$ | **Excluded in $\mathbb Q(n,z)$** |
| Bounded endpoint tensor formula for $\mathcal K_n$ | **Open; equation (5.3) is explicit** |
| Minimal holonomic system including actual primitive contacts | **Not established** |
| Separate $C_{\rm sat}$-height estimate needed for the stated budget | **No; rigorously unnecessary** |
| Actual-seed congruence for the complete alignment telescope | **Proved under the stated terminal-alignment hypotheses** |
| Subfactorial alignment acquisition | **Open** |
| Target-specific transverse Bézout certificate | **Open** |
| $\log J_{\rm res}=o(n\log n)$ on an infinite original subsequence | **Open** |
| Favorable all-prime primitive whole forms at those same indices | **Open** |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

## Conclusion

The actual Green prefix is no longer only a named finite response. The physical moment equation gives


$$
B_n
=-e^zq^n+
\frac{q^n}{(1-z)^{n+1}}(e^zS_n-E_n),
$$


and the complete transverse scalar satisfies the explicitly seeded recurrence


$$
\boxed{
\mathcal K_{n+1}
=-(n+1)^2\mathcal K_n+\gamma_n\mathbf Y_n,
\qquad
\mathcal K_2=14.
}
$$



This is genuine progress on the actual source correlations. It does not establish a bounded-endpoint closed form, and it does not establish a gcd-growth theorem. The precise next symbolic obligation is the rational-gauge equation (5.3); a bounded certificate test for it has been specified.

On alignment, the new seed charge $\eta_t$ controls the residue of the **whole** telescope in the regime $v_p(F_n)<a_t$. All primitive exterior payments, medium-prime support, and possible reference-composition cancellation remain intact.

The exact remaining arithmetic bottlenecks are:

1. a subfactorial bound for new terminal alignment acquisition on sufficiently controlled original geometric blocks;
2. a paid, actual-contact Bézout or equivalent support theorem proving
   

$$
\log J_{\rm res}=o(n\log n)
$$


   on an infinite original subsequence;
3. the all-prime final primitive denominator and a nonzero whole-error estimate at those same indices.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi\text{ is obtained.}}
$$


