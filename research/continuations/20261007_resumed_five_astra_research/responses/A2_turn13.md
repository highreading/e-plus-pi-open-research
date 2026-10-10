> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact reduction of the turn-11 mixed Laguerre determinant

## 1. Result and scope

The main new result is an **unconditional nonvanishing theorem for the affine coefficient of the exact turn-11 determinant**:

> **Theorem.** Retain the original A2 indices
> 

$$
> b=3^{249005515+574312172u},\qquad n=2001b,\qquad
> u\equiv2\pmod{29^9},
>
$$


> with $u$ in its original allowed domain. For the complete turn-11 matrix
> 

$$
> H_{rj}(X)=X-A_{n+r,j}-B_j,\qquad 0\le r,j<b,
>
$$


> its coefficient of $X$ is strictly positive. Consequently the paid integer determinant
> 

$$
> D_n(X)=P_n\det H(X)=U_nX-V_n
>
$$


> has $U_n>0$ at every such index.

The proof below establishes the exact bridge to a positive moment construction. It does **not** identify the original mixed matrix itself with a positive Gram matrix. The even number $b-1$ is essential to the bridge.

I also obtain:

* a determinant-free rational recurrence evaluating both $U_n$ and $V_n$;
* an exact scalar-cofactor reduction to a primitive integer polynomial and three scalar charges;
* an ALL-prime formula for the final gcd and the actual primitive denominator;
* a complete expression for the whole evaluated error, retaining the rational arctangent source $B_j$;
* a precise failure of the analogous positivity argument for that whole error.

The outstanding issue is now narrower, but remains substantial: **the whole error has not been proved nonzero and sufficiently small on an infinite set of the original indices**. No irrationality theorem follows here.

The Family005 certificates have already been independently reproduced by the parent. I do not repeat that audit, the content calculation from turn 11, or its single-entry obstruction.

---

## 2. Objects and arithmetic normalizations retained

Put


$$
d=b-1,\qquad h=n-d=2000b+1,\qquad \alpha=d+1=b.
$$


Thus


$$
d\ \text{is even},\qquad n,h\ \text{are odd}.
$$



The complete rational entries are


$$
A_{m,j}
=j!\sum_{\ell=0}^{m-j}
(-1)^\ell\binom{m-j}{\ell}\frac1{(j+\ell)!},
$$


and


$$
B_j=4\sum_{k=0}^{2j-1}\frac{(-1)^k}{2k+1},\qquad B_0=0.
$$


The two complete endpoint identities are


$$
\int_0^1 e^t t^j\Lambda_m(t)\,dt=e-A_{m,j},
$$


and


$$
4\int_0^1\frac{s^{4j}}{1+s^2}\,ds=\pi-B_j.
$$


Therefore


$$
H_{rj}(e+\pi)
=(e+\pi)-A_{n+r,j}-B_j
$$


is precisely the mixed matrix under consideration.

Its finite row window remains


$$
m=n,n+1,\ldots,n+d.
$$


No row beyond $n+d$, and no column beyond $d$, is introduced in the finite-difference reduction.

I retain the actual arithmetic objects from turn 11:


$$
R_{rj}=A_{n+r,j}+B_j,\qquad
W_{rj}=(n+r)!R_{rj},
$$




$$
\kappa_r=\gcd\bigl((n+r)!,W_{r0},\ldots,W_{rd}\bigr),
\qquad
C_r=\frac{(n+r)!}{\kappa_r},
$$




$$
Y_{rj}=C_rR_{rj},
\qquad
c_j=\gcd_{0\le r\le d}(C_r,Y_{rj}),
$$


and


$$
\mathcal L_n=\operatorname{lcm}_{0\le r\le d}C_r,
\qquad
P_n=\frac{\prod_{r=0}^{d}C_r}{\prod_{j=0}^{d}c_j}.
$$


These are exact contents, the least simultaneous clearer, and the complete row-and-column payment—not substitutes based on estimated factorial denominators.

Then


$$
D_n(X)=
\det\left[\frac{C_rX-Y_{rj}}{c_j}\right]_{r,j=0}^{d}
=P_n\det H(X)
$$


has integer coefficients.

The calculations below concern this exact matrix. They do not supply a change-of-frame identity to the earlier A2 producer with its separate corrected forcing, returns, and physical terminal. Those complete producer formulas are not present in the supplied material; no cancellation is transferred to them.

---

## 3. An exact finite-difference reduction

### 3.1 The relevant Laguerre formulas

For nonnegative integral parameters, use the finite definition


$$
L_m^{(\beta)}(x)
=\sum_{\ell=0}^{m}
(-1)^\ell\binom{m+\beta}{m-\ell}\frac{x^\ell}{\ell!}.
$$


Direct coefficient comparison gives


$$
\frac{d}{dx}L_m^{(\beta)}(x)
=-L_{m-1}^{(\beta+1)}(x),
$$


and


$$
L_m^{(\beta+1)}(x)
=L_m^{(\beta)}(x)-\frac{d}{dx}L_m^{(\beta)}(x).
\tag{3.1}
$$



The rational entry satisfies


$$
A_{m,j}
=\frac{L_{m-j}^{(j)}(1)}{\binom mj}.
\tag{3.2}
$$



Define, for $0\le j\le d$,


$$
f_j(x)=L_{n-j}^{(j)}(x),
\qquad
g_j(x)=L_{n-j}^{(j+1)}(x).
$$


Thus


$$
g_j=(1-\partial_x)f_j.
\tag{3.3}
$$



The established finite-difference identity becomes


$$
\Delta_m^r A_{n,j}
=(-1)^r\frac{j!(n-j)!}{(n+r)!}
L_{n-j}^{(j+r)}(1).
\tag{3.4}
$$



### 3.2 Reduction of the whole matrix, including $B_j$

Replace row $r$ of $H$ by its $r$-th forward difference. This is a lower-triangular integral operation of determinant $1$.

The first row remains


$$
X-B_j-\frac{f_j(1)}{\binom nj}.
$$


For $r\ge1$, both $X$ and the **whole** $B_j$ term disappear under row differences, leaving


$$
(-1)^{r+1}\frac{j!(n-j)!}{(n+r)!}
(1-\partial_x)^{r-1}g_j(1).
$$



Scale the columns by $1/[j!(n-j)!]$, the first row by $n!$, and row $r\ge1$ by


$$
(-1)^{r+1}(n+r)!.
$$


Finally, use triangular operations among the last $d$ rows to replace


$$
g_j,\ (1-\partial_x)g_j,\ldots,(1-\partial_x)^{d-1}g_j
$$


by


$$
g_j,\ g_j',\ldots,g_j^{(d-1)}.
$$


The signs from these last operations cancel the previous row signs.

Consequently


$$
K_n\det H(X)=
\det
\begin{pmatrix}
\binom n0(X-B_0)-f_0(1)&\cdots&
\binom nd(X-B_d)-f_d(1)\\
g_0(1)&\cdots&g_d(1)\\
g_0'(1)&\cdots&g_d'(1)\\
\vdots&&\vdots\\
g_0^{(d-1)}(1)&\cdots&g_d^{(d-1)}(1)
\end{pmatrix},
\tag{3.5}
$$


where the complete normalization is


$$
\boxed{
K_n=
\frac{\prod_{r=0}^{d}(n+r)!}
     {\prod_{j=0}^{d}j!(n-j)!}
=
\prod_{r=1}^{d}\frac{(n+r)!}{r!(n-r)!}.
}
\tag{3.6}
$$


In particular, $K_n$ is a positive integer.

Equation (3.5) is the finite-boundary reduction needed here. It retains every first-row source term.

---

## 4. The exact positive-moment bridge

### 4.1 The polynomial selected by the contact rows

Let $z_j$ be the signed cofactors of the first row on the right side of (3.5), and put


$$
Q(x)=\sum_{j=0}^{d}z_jg_j(x).
\tag{4.1}
$$


For the moment, this is only a device for proving the structural identity. It will be eliminated from the final evaluation.

The lower rows imply


$$
Q(1)=Q'(1)=\cdots=Q^{(d-1)}(1)=0.
\tag{4.2}
$$



A further contiguous identity gives


$$
g_j(x)
=\sum_{a=0}^{d-j}(-1)^a\binom{d-j}{a}
L_{n-j-a}^{(\alpha)}(x).
\tag{4.3}
$$


Hence


$$
\operatorname{span}(g_0,\ldots,g_d)
=
\operatorname{span}
\bigl(L_h^{(\alpha)},\ldots,L_n^{(\alpha)}\bigr).
\tag{4.4}
$$



For completeness, the finite Laguerre formula gives Rodrigues’ identity


$$
x^\alpha e^{-x}L_m^{(\alpha)}(x)
=\frac1{m!}\frac{d^m}{dx^m}
\left(e^{-x}x^{m+\alpha}\right).
$$


Integration by parts therefore proves orthogonality on $(0,\infty)$ with weight $x^\alpha e^{-x}$. The monic polynomials


$$
\widehat L_m^{(\alpha)}=(-1)^m m!L_m^{(\alpha)}
$$


have squared norms


$$
m!(m+\alpha)!.
\tag{4.5}
$$


All boundary terms vanish because $\alpha\ge0$, and the exponential controls infinity.

It follows from (4.4) that $Q$ is orthogonal, for this weight, to every polynomial of degree less than $h$.

Now introduce the **actual modified positive weight**


$$
w_d(x)=x^\alpha(x-1)^d e^{-x},\qquad x>0.
\tag{4.6}
$$


Because $d$ is even, this is nonnegative and positive except at isolated points. It has infinite support and all moments.

Let $p_h(x)$ be its monic orthogonal polynomial of degree $h$. Equations (4.2)–(4.4) show that


$$
\boxed{
Q(x)=\tau_n(x-1)^d p_h(x).
}
\tag{4.7}
$$



This is the exact bridge. It is not an assertion that $H$ is itself a Gram matrix.

### 4.2 Evaluation and sign of the normalization

Let


$$
\Delta_h^{(0)}
=\prod_{i=0}^{h-1}i!(i+\alpha)!,
$$


and let $\Delta_h$ be the Hankel determinant for $w_d$.

The cofactor $z_0$ is the Wronskian of


$$
g_1,\ldots,g_d.
$$


By (4.3), their transition to


$$
L_{n-1}^{(\alpha)},L_{n-2}^{(\alpha)},\ldots,L_h^{(\alpha)}
$$


is triangular with diagonal $1$. Reversing the order and passing to monic polynomials gives, since $d$ is even,


$$
z_0=
\frac{1}{\prod_{N=h}^{n-1}N!}
W\!\left(
\widehat L_h^{(\alpha)},\ldots,
\widehat L_{h+d-1}^{(\alpha)}
\right)(1).
$$



The confluent characteristic-polynomial identity is


$$
W\!\left(
\widehat L_h^{(\alpha)},\ldots,
\widehat L_{h+d-1}^{(\alpha)}
\right)(1)
=
\left(\prod_{s=0}^{d-1}s!\right)
\frac{\Delta_h}{\Delta_h^{(0)}}.
\tag{4.8}
$$


One elementary derivation starts with the determinant of the monic orthogonal polynomials evaluated at $d$ distinct points. Expanding the moment determinant by Andréief gives the average of


$$
\prod_{i=1}^{h}\prod_{a=1}^{d}(x_a-t_i).
$$


Dividing by the Vandermonde in the $x_a$, and letting every $x_a$ tend to $1$, yields the derivative factorials in (4.8). The remaining integral is exactly the moment determinant for multiplication of the weight by $(1-t)^d$.

Thus


$$
z_0=
\frac{\prod_{s=0}^{d-1}s!}
     {\prod_{N=h}^{n-1}N!}
\frac{\Delta_h}{\Delta_h^{(0)}}>0,
\tag{4.9}
$$


and comparison of leading coefficients in (4.1) gives


$$
\boxed{
\tau_n=\frac{(-1)^n z_0}{n!}.
}
\tag{4.10}
$$


At the original indices, $\tau_n<0$.

This validates all hypotheses of the positivity argument in the original turn-11 objects: the relevant weight is (4.6), the degree block is exactly $h,\ldots,n$, and the contact length is exactly $d=b-1$.

---

## 5. Strict positivity of the affine coefficient

The relation $g=(1-\partial_x)f$ gives, for polynomials,


$$
f(y)=\int_0^\infty e^{-u}g(y+u)\,du.
$$


Hence


$$
f_j(0)=\int_0^\infty e^{-x}g_j(x)\,dx=\binom nj,
\tag{5.1}
$$


and


$$
f_j(1)=e\int_1^\infty e^{-x}g_j(x)\,dx.
\tag{5.2}
$$



Therefore the coefficient of $X$ in (3.5) is


$$
\int_0^\infty e^{-x}Q(x)\,dx
=\tau_n J_{n,d},
$$


where


$$
J_{n,d}
=\int_0^\infty e^{-x}(x-1)^d p_h(x)\,dx.
\tag{5.3}
$$



The crucial sign is not obtained by claiming that $p_h$ is positive.

### Lemma 5.1 — Reciprocal-moment sign

For the positive weight $w_d$,


$$
\boxed{(-1)^hJ_{n,d}>0.}
\tag{5.4}
$$



#### Proof

The $h$ zeros $r_1,\ldots,r_h$ of $p_h$ are distinct and belong to $(0,\infty)$, by the usual sign-change proof for orthogonal polynomials with a positive measure of infinite support.

Set


$$
f(x)=x^{-\alpha}.
$$


Let $I(x)$ be the polynomial of degree at most $h-1$ interpolating $f$ at the $r_i$. Orthogonality gives


$$
J_{n,d}
=\int_0^\infty p_h(x)w_d(x)\bigl(f(x)-I(x)\bigr)\,dx.
$$


The interpolation remainder is


$$
f(x)-I(x)=p_h(x)f[r_1,\ldots,r_h,x].
$$


For positive arguments, the divided difference has strict sign $(-1)^h$. This follows either from the derivative formula


$$
f^{(h)}(x)=(-1)^h(\alpha)_h x^{-\alpha-h},
$$


or directly from the divided-difference formula for reciprocal powers.

Consequently


$$
(-1)^hJ_{n,d}
=\int_0^\infty p_h(x)^2w_d(x)
\left|f[r_1,\ldots,r_h,x]\right|\,dx>0.
$$


The expression is integrable at zero: the factor $x^\alpha$ in $w_d$ cancels the possible reciprocal singularity. ∎

Combining (4.10) and (5.4),


$$
\operatorname{sgn}(\tau_nJ_{n,d})=(-1)^{n+h}=(-1)^d=1.
$$


Thus


$$
\boxed{
[X]\det H(X)=\frac{\tau_nJ_{n,d}}{K_n}>0.
}
\tag{5.5}
$$


Since $P_n>0$, this proves $U_n>0$.

This settles the affine-coefficient nonvanishing obligation on the **entire original index set**, not merely on a finite sample.

---

## 6. An integer positive-moment evaluation of $U_n$

The preceding coefficient can be evaluated without the original cofactor minors.

Define


$$
\nu_\ell
=\int_0^\infty x^\ell(x-1)^d e^{-x}\,dx
=\sum_{a=0}^{d}(-1)^{d-a}\binom da(\ell+a)!.
\tag{6.1}
$$


Let


$$
a_0=0,\qquad a_i=d+i\quad(1\le i\le h),
$$


and define


$$
Z_{n,d}=\det[\nu_{a_i+j}]_{i,j=0}^{h}.
\tag{6.2}
$$



This is not merely a replacement name for the original minor: it has an explicit positive integral and an exact scalar relation to the orthogonal-polynomial charge:


$$
\boxed{
Z_{n,d}=(-1)^hJ_{n,d}\Delta_h\in\mathbb Z_{>0}.
}
\tag{6.3}
$$



To verify both assertions, symmetrize Heine’s integral for $p_h$. The divided difference of $x^{-\alpha}$ contributes


$$
(-1)^h
\left(\prod_{i=0}^{h}x_i^{-1}\right)
h_d(x_0^{-1},\ldots,x_h^{-1}),
$$


where $h_d$ is the complete homogeneous symmetric polynomial of degree $d$. Since $\alpha=d+1$, cancellation against the powers in $w_d$ gives


$$
Z_{n,d}
=\frac1{(h+1)!}
\int_{(0,\infty)^{h+1}}
V(x)^2
s_{(d^h)}(x)
\prod_{i=0}^{h}(x_i-1)^d e^{-x_i}\,dx_i.
\tag{6.4}
$$


Here


$$
s_{(d^h)}(x)
=\left(\prod_{i=0}^{h}x_i\right)^d
h_d(x_0^{-1},\ldots,x_h^{-1})
$$


has nonnegative coefficients and is strictly positive for positive arguments. Thus the integral is strictly positive.

The alternant identity for this Schur polynomial, followed by Andréief, gives exactly (6.2). Its entries are integers by (6.1), proving integrality.

After cancellation of every factorial factor in (5.5), the result is


$$
\boxed{
[X]\det H(X)=\mathfrak c_{n,d}Z_{n,d},
}
\tag{6.5}
$$


where


$$
\boxed{
\mathfrak c_{n,d}
=
\frac{
\left(\prod_{s=0}^{d-1}s!\right)
\left(\prod_{j=0}^{d}j!\right)}
{
\left(\prod_{i=0}^{h-1}i!(i+d+1)!\right)
\left(\prod_{r=0}^{d}(n+r)!\right)
}.
}
\tag{6.6}
$$


Consequently


$$
\boxed{
U_n=P_n\mathfrak c_{n,d}Z_{n,d}>0.
}
\tag{6.7}
$$



All factorial divisions in this formula are displayed. In particular, $Z_{n,d}>0$ does not authorize discarding the denominator of $\mathfrak c_{n,d}$.

---

## 7. Evaluation of the whole determinant by a rational recurrence

The following recurrence evaluates the constant term as well as the affine coefficient. No original cofactor determinant remains.

### 7.1 Explicit moment inputs

The moments of $w_d$ are


$$
\mu_\ell
=\sum_{a=0}^{d}(-1)^{d-a}\binom da
(\ell+d+1+a)!.
\tag{7.1}
$$



Construct the monic orthogonal polynomials by


$$
p_0(x)=1,\qquad p_{-1}(x)=0,
$$




$$
H_i=\langle p_i,p_i\rangle,\qquad
A_i=\frac{\langle xp_i,p_i\rangle}{H_i},
$$




$$
B_i=
\begin{cases}
0,&i=0,\\
H_i/H_{i-1},&i\ge1,
\end{cases}
$$


and


$$
p_{i+1}(x)=(x-A_i)p_i(x)-B_ip_{i-1}(x).
\tag{7.2}
$$


Every inner product is a finite rational sum using (7.1), and every $H_i$ is strictly positive. Thus the recurrence has no singular division.

To construct $p_h$ and $H_0,\ldots,H_{h-1}$, moments through $\mu_{2h-1}$ suffice. The largest factorial in those inputs is $(2n)!$.

Let $a$ be the actual least coefficient clearer of $p_h$, and set


$$
r(x)=a(x-1)^dp_h(x)=\sum_{\ell=0}^{n}r_\ell x^\ell.
\tag{7.3}
$$


Then $r$ is a primitive integer polynomial. Multiplication by the monic integer polynomial $(x-1)^d$ neither reduces nor increases the least scalar clearer: monic polynomial division recovers $ap_h$ from $r$.

Define the two integer charges


$$
\boxed{
F=\sum_{\ell=0}^{n}r_\ell\ell!,
\qquad
E=\sum_{\ell=0}^{n}r_\ell
\sum_{k=0}^{\ell}\frac{\ell!}{k!}.
}
\tag{7.4}
$$


They have the exact integral meanings


$$
F=\int_0^\infty e^{-x}r(x)\,dx=aJ_{n,d},
$$




$$
E=e\int_1^\infty e^{-x}r(x)\,dx.
\tag{7.5}
$$


In particular,


$$
\boxed{F<0}
\tag{7.6}
$$


at every original index.

The moment determinant appearing earlier is also evaluated by the recurrence:


$$
\Delta_h=\prod_{i=0}^{h-1}H_i,
\qquad
Z_{n,d}=(-1)^h\frac{F}{a}\prod_{i=0}^{h-1}H_i.
\tag{7.7}
$$


Thus (6.7) has a complete rational-recursion evaluation.

### 7.2 The complete arctangent charge

Expand


$$
r(x)=\sum_{j=0}^{d}\gamma_jg_j(x).
\tag{7.8}
$$


This expansion exists by the same orthogonality argument used in (4.4)–(4.7).

Its coefficients are obtained from the top $d+1$ coefficients of $r$ by the explicit triangular recurrence


$$
\boxed{
\gamma_j
=(-1)^{n-j}(n-j)!\,r_{n-j}
-\sum_{i=0}^{j-1}\binom{n+1}{j-i}\gamma_i,
\quad 0\le j\le d.
}
\tag{7.9}
$$


In particular, every $\gamma_j$ is an integer.

Put


$$
w_j=\binom nj\gamma_j,\qquad
\mathcal B=\sum_{j=0}^{d}w_jB_j.
\tag{7.10}
$$


No part of $B_j$ is suppressed. Also, by (5.1),


$$
\sum_{j=0}^{d}w_j=F.
\tag{7.11}
$$



Let


$$
\ell=\operatorname{den}(\mathcal B),\qquad
T=\ell\mathcal B.
\tag{7.12}
$$


These are the **actual reduced denominator and numerator of the combined arctangent charge**, not an oversized lcm of all odd denominators. Thus


$$
\gcd(\ell,T)=1.
$$



### 7.3 Fully reduced determinant identity

Equations (3.5), (4.7), and (7.3) now yield


$$
\boxed{
\det H(X)
=\frac{\tau_n}{aK_n}
\left(FX-E-\frac{T}{\ell}\right).
}
\tag{7.13}
$$


Equivalently, using the evaluated coefficient,


$$
\boxed{
D_n(X)
=
P_n\mathfrak c_{n,d}Z_{n,d}
\left(
X-\frac{\ell E+T}{\ell F}
\right).
}
\tag{7.14}
$$



This evaluates the whole affine determinant through explicit factorial moments, a nonsingular rational recurrence, and finite scalar charges. It does not leave its constant term as a named minor.

It is not, by itself, an asymptotic evaluation of the error. That separate obligation is addressed below.

---

## 8. Exact ALL-prime gcd and actual primitive denominator

Define


$$
g=\gcd\bigl(|F|,\ |\ell E+T|\bigr).
\tag{8.1}
$$


Because


$$
\gcd(\ell,\ell E+T)=\gcd(\ell,T)=1,
$$


one has


$$
\gcd\bigl(|\ell F|,\ |\ell E+T|\bigr)=g.
\tag{8.2}
$$



Therefore the actual primitive pair associated with the turn-11 determinant is


$$
\boxed{
q_n=\frac{\ell|F|}{g},
\qquad
p_n=\frac{\operatorname{sgn}(F)(\ell E+T)}{g}.
}
\tag{8.3}
$$


At the original indices $F<0$, so


$$
q_n=-\frac{\ell F}{g},
\qquad
p_n=-\frac{\ell E+T}{g}.
$$



This is an exact scalar-cofactor reduction. In particular:

* $q_n$ includes the **entire actual denominator $\ell$**;
* the only remaining scalar cancellation is the displayed ALL-prime gcd $g$;
* normalization of the orthogonal polynomial has not been treated as free.

Since $U_n>0$, the final gcd of the paid determinant coefficients is


$$
\boxed{
G_n=\gcd(U_n,|V_n|)
=
P_n\mathfrak c_{n,d}Z_{n,d}
\frac{g}{\ell|F|}.
}
\tag{8.4}
$$


This is an equality, not a lower bound.

Prime by prime,


$$
\boxed{
v_p(q_n)
=
v_p(\ell)+v_p(F)
-\min\{v_p(F),v_p(\ell E+T)\}.
}
\tag{8.5}
$$


It holds for every prime, including primes outside the previously controlled range $p\le b$.

The outstanding arithmetic problem is now explicit: estimate the gcd in (8.1), or equivalently the primitive denominator in (8.3), for these specific recurrence-generated charges. No such asymptotic estimate is proved here.

---

## 9. The whole evaluated error—and the precise positivity failure

### 9.1 Complete error identity

At $S=e+\pi$,


$$
\boxed{
q_nS-p_n
=
\frac{\operatorname{sgn}(F)\ell}{g}
\left(FS-E-\frac{T}{\ell}\right).
}
\tag{9.1}
$$



Define the explicit polynomial


$$
W(y)=\sum_{j=0}^{d}w_jy^j.
\tag{9.2}
$$


Using the complete arctangent identity,


$$
\boxed{
FS-E-\frac{T}{\ell}
=
e\int_0^1e^{-x}r(x)\,dx
+
4\int_0^1\frac{W(s^4)}{1+s^2}\,ds.
}
\tag{9.3}
$$


Both terms are necessary. This is the whole error, not only an exponential remainder or an arctangent tail.

### 9.2 An exact kernel identity for the arctangent term

The polynomial $W$ itself admits a useful exact reduction:


$$
\boxed{
W(y)=\int_0^\infty e^{-x}r(x)L_n^{(0)}((1-y)x)\,dx.
}
\tag{9.4}
$$



Here is an elementary verification. The contiguous expansion and dilation formula are


$$
g_j(x)=\sum_{k=0}^{n-j}\binom{n-k}{j}L_k^{(0)}(x),
$$




$$
L_n^{(0)}(cx)
=\sum_{k=0}^{n}\binom nk c^k(1-c)^{n-k}L_k^{(0)}(x).
$$


Orthogonality with weight $e^{-x}$ gives


$$
\begin{aligned}
\int_0^\infty e^{-x}g_j(x)L_n^{(0)}(cx)\,dx
&=\sum_{k=0}^{n-j}\binom{n-k}{j}\binom nk
c^k(1-c)^{n-k}\\
&=\binom nj(1-c)^j.
\end{aligned}
$$


Set $c=1-y$ and use (7.8).

Moreover, orthogonality of $p_h$ eliminates every term of degree at least $d+1$ in the Laguerre kernel:


$$
\boxed{
W(y)=
\sum_{k=0}^{d}
\frac{(-1)^k}{k!}\binom nk(1-y)^k
\int_0^\infty e^{-x}x^kr(x)\,dx.
}
\tag{9.5}
$$


The remaining integrals are explicit integer factorial charges.

For each $0\le k\le d$, the same reciprocal-moment argument as Lemma 5.1 shows that


$$
\int_0^\infty e^{-x}x^kr(x)\,dx
$$


has sign $(-1)^h$. But the coefficients in (9.5) alternate. This is precisely where the coefficient-positivity proof stops applying.

### 9.3 A concrete failure of a positive-integrand claim

The following is a diagnostic finite instance, **not an original A2 index**:


$$
n=3,\qquad b=3,\qquad d=2,\qquad h=1.
$$


The recurrence gives


$$
p_1(x)=x-\frac{84}{13},
$$


and


$$
r(x)=13(x-1)^2p_1(x)
=13x^3-110x^2+181x-84.
$$


Then


$$
F=-45,\qquad E=-64,
$$




$$
(\gamma_0,\gamma_1,\gamma_2)=(-78,92,-81),
$$


and


$$
W(y)=-78+276y-243y^2.
$$


Although $d$ is even,


$$
W(0)=-78,\qquad W(5/9)=\frac13,\qquad W(1)=-45.
$$


Thus the arctangent integrand changes sign.

The same exact calculation gives


$$
\mathcal B=\frac{1136}{35},
$$


and


$$
\boxed{
\det H(X)=\frac{525X-368}{100800}.
}
\tag{9.6}
$$


This verifies the normalizations and exhibits the obstruction in the actual reduced construction, rather than in an unrelated norm example.

It proves neither that the whole error vanishes nor that it changes sign on the original progression. What it proves is narrower and exact:

> Even contact makes the coefficient bridge positive, but does not make the complete mixed-error integrand positive. A positive-Gram theorem for the coefficient cannot be reused as a whole-determinant nonvanishing theorem without an additional identity or sign argument.

Accordingly, (9.1)–(9.5) evaluate and preserve the whole error, but **do not prove it nonzero at the infinite original indices**.

---

## 10. Comparison with the parent’s even-contact lattice

The parent’s specified contact lattice is a different construction.

Its measure is the pushforward of


$$
e^{t-1}\,dt\quad(t\le1)
$$


under $x=t^2$. Explicitly, for $x>0$, its density is


$$
\frac{e^{-1-\sqrt x}
+\mathbf 1_{x\le1}e^{-1+\sqrt x}}
{2\sqrt x}.
$$


Its moments are $a_{2k}$, and its complete contact matrix is


$$
C_k=B_k-vv^T.
$$



By contrast, the bridge proved here uses


$$
x^{d+1}(x-1)^d e^{-x}\,dx.
$$


These measures, degree spaces, and contact functionals are not equal.

The parent’s symbolic claims have the following scope:

1. **Nonsingularity of $C_k$, $k\ge2$.**  
   The supplied proof is valid: positivity of $B_k$, monotonicity of the reproducing-kernel value, and $K_2=3/2$ imply
   

$$
\det C_k=(1-K_k)\det B_k<0.
$$


   The exceptional $k=1$ case is correctly excluded.

2. **Contact rows and saturation index.**  
   The construction using $C_k^{-1}w_m$ satisfies all contact equations. The quotient-map proof gives exactly
   

$$
[\mathbb Z^k:L_k]=\frac{|\det C_k|}{\delta_k}.
$$


   It does not identify this quotient with the final scalar gcd of a compact determinant.

3. **Raw height.**  
   The supplied positive-box lower bound and Hadamard upper bound justify
   

$$
\log|\det C_k|=2k^2\log k+O(k^2).
$$


   This is raw contact height, not a primitive-denominator estimate.

4. **Finite certificate.**  
   The supplied $k=2,\ldots,10$ data have precisely that finite scope. I have not recomputed them here, and they imply no asymptotic saturation law.

Likewise, A5turn10’s finite matching determinant is a separate compact construction. Its displayed primitive form


$$
322314373-55866720(e+\pi)
$$


does not share its gcd or nonvanishing with the turn-11 matrix by virtue of a common exponential charge functional.

The present positive bridge therefore advances the exact Laguerre matrix without transferring unproved conclusions between these three constructions.

---

## 11. The concrete next lemma

The coefficient problem is now closed: $U_n>0$ on every original index.

A substantive next lemma should address the following explicitly generated scalar data:


$$
r,\quad F,\quad E,\quad
W,\quad \ell,\quad T,\quad
g=\gcd(|F|,|\ell E+T|).
$$



There are two coupled obligations.

### 11.1 Mixed-error sign and size

Establish, on one infinite subset of the original progression,


$$
0<
\left|
e\int_0^1e^{-x}r(x)\,dx
+
4\int_0^1\frac{W(s^4)}{1+s^2}\,ds
\right|,
\tag{11.1}
$$


with a bound strong enough after multiplication by $\ell/g$.

The new structural target is specific: use the orthogonality of


$$
r=a(x-1)^dp_h
$$


and the exact truncated kernel (9.5) to control the **sum** in (11.1). Estimating its two components independently may lose the mixed cancellation. Complete monotonicity alone does not apply, because of the alternating kernel coefficients and the cutoff at $x=1$.

### 11.2 Scalar saturation

Obtain an ALL-prime estimate for


$$
g=\gcd(|F|,|\ell E+T|),
$$


or an equivalent upper bound for


$$
q_n=\ell|F|/g.
$$


The exact equality (8.4) connects that scalar problem to the original paid determinant gcd. Thus a future estimate can be checked without confusing row content, Hankel saturation, and final scalar reduction.

For example, the sufficient conclusion


$$
0<
\left|FS-E-\frac{T}{\ell}\right|
\le \frac{g}{\ell b}
\tag{11.2}
$$


on an infinite original subset would give


$$
0<|q_nS-p_n|\le\frac1b\longrightarrow0
$$


and prove irrationality.

No part of (11.2) is claimed here. In particular, the old paid upper-bound shortfall


$$
2000.5\,b^2\log b+O(b^2)
$$


is not a lower bound on the actual error and is not an impossibility theorem.

---

## 12. Bounded exact arithmetic checks

No tool computation was performed. The symbolic proofs above do not require construction of a matrix at the enormous first original index.

### 12.1 Small normalization certificate

A useful independently authored check has bounded input


$$
n=3,\quad b=3,
$$


together with the finite formulas for $A_{m,j}$, $B_j$, and the three moments needed for $p_1$.

Expected exact output:


$$
r=13x^3-110x^2+181x-84,
$$




$$
F=-45,\quad E=-64,\quad
W(y)=-78+276y-243y^2,
$$




$$
\mathcal B=\frac{1136}{35},
$$




$$
\det H(X)=\frac{525X-368}{100800},
$$


and primitive pair


$$
(p,q)=(368,525).
$$


This checks signs, derivative factorials, the arctangent constant, and primitive reduction. It proves only this finite instance.

### 12.2 Optional bounded identity grid

For


$$
b\in\{3,5\},\qquad b-1\le n\le12,
$$


one may compare:

* direct expansion of the exact $b\times b$ matrix;
* the recurrence evaluation (7.1)–(7.14);
* the coefficient formula (6.5);
* the primitive pair formula (8.3).

Expected output is exact equality in $\mathbb Q[X]$, together with a positive coefficient of $X$ in every case.

This is a transcription check, not evidence for an unproved infinite gcd or error estimate. There is no need to repeat the settled Family005 calculations.

---

## 13. Conclusion and proof-status ledger

| Claim | Status |
|---|---|
| Exact reduction of the full finite turn-11 matrix | Proved |
| Retention of every $B_j$ source and both endpoints | Proved |
| Exact bridge to the weight $x^{d+1}(x-1)^de^{-x}$ | Proved |
| Applicability of positivity when $d=b-1$ is even | Proved |
| $U_n>0$ at every original A2 index | **New proved result** |
| Recurrence evaluation of both determinant coefficients | Proved |
| Exact ALL-prime scalar-cofactor and primitive-pair formulas | **New proved result** |
| Whole-error positivity from the same Gram argument | Precisely fails; sign-changing kernel exhibited |
| Whole determinant nonzero on an infinite original subset | Open |
| Sufficient paid whole-error decay on that same subset | Open |
| Transfer to the earlier corrected A2 producer | No identity supplied or claimed |
| Irrationality or rationality of $e+\pi$ | Unresolved |

The main advance is that the affine coefficient is no longer an unexplained minor: its strict positivity follows from an exact contiguous-Laguerre, Wronskian, and reciprocal-moment bridge, with every normalization retained. The whole determinant is reduced to explicitly generated integer charges and its actual primitive denominator.

The remaining bottleneck is **not coefficient nonvanishing**. It is the compatible infinite control of the complete mixed error and the scalar gcd


$$
\gcd(|F|,|\ell E+T|)
$$


on the same original $n=2001b$ progression. Until that is proved, this work establishes neither rationality nor irrationality of $e+\pi$.
