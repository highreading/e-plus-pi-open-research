> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1 turn20 — The actual first producer jet collapses to one scalar, with a bounded, precision-paid evaluator

## Executive conclusion

The newly supplied actual producer representation permits a substantial reduction beyond the seven-coordinate criterion of turn19.

On the retained sufficiently large original family, I prove


$$
\boxed{
R_{\rm prod}(y)\equiv c\,(y+1)(y-1)^A\pmod3
}
\tag{E.1}
$$


for one scalar $c\in\mathbb F_3$. Thus six of the seven previously undetermined jet coordinates vanish **for the actual signed producer**, not merely for a model supported in the same interval.

Equivalently, the eight requested shifted coefficients are


$$
\boxed{
\bigl(r_{A-6},r_{A-5},\ldots,r_{A+1}\bigr)
=
(0,0,0,0,0,0,2c,c)\pmod3.
}
\tag{E.2}
$$



The remaining scalar is no longer an unspecified coefficient of an enormous inverse. I derive an explicit evaluator using:

* normalized moments only through index $41$;
* a $350$-coordinate **terminal arithmetic interface**, with bandwidth $41$;
* two right-hand sides and eight terms of a finite Neumann expansion;
* inverses only of fixed $3\times3$ and $2\times2$ unit blocks;
* the actual signed rank-one denominator, proved here to satisfy
  

$$
\boxed{\eta_n\equiv3\pmod9,\qquad v_3(\eta_n)=1;}
  \tag{E.3}
$$


* modulus $3^8$ before that scalar division, followed by modulus $3^7$ before division by $3^6$.

This is not an $n$-dimensional solve. On the fixed progression


$$
j\equiv84645\pmod{531441},
$$


the evaluator has the single fixed input


$$
\boxed{n_0=86996\pmod{3^{11}}.}
\tag{E.4}
$$


Consequently **no unread high ternary digits remain in this first-jet question on that progression**.

I have not executed this new arithmetic. Accordingly, I do not report a numerical value of $c$, or claim to have selected its zero/nonzero branch. The evaluator below is an explicit, bounded arithmetic construction with no free producer coefficients.

There is nevertheless a further unconditional consequence for the complete correction. Formula (E.1), including the terminal return, gives


$$
\boxed{
T_R/3\equiv
-c\,e_{Y_m}e_{\nu-1}^{T}\pmod3.
}
\tag{E.5}
$$


The initial LOW force vanishes completely. The remaining terminal HIGH force is isotropic for the actual leading HIGH inverse. Therefore


$$
\boxed{\mathcal Q\in9M_\nu(\mathbb Z_3),}
\tag{E.6}
$$


improving turn7’s $\mathcal Q\in3M$. On the retained window this yields


$$
\boxed{S_{\rm act}\in3^{15}M_\nu(\mathbb Z_3)}
\tag{E.7}
$$


and


$$
\boxed{e_{\rm act}-e_c\in3^7\mathbb Z_3^\nu.}
\tag{E.8}
$$



Neither conclusion determines the actual residual inverse or the primitive denominator. The complete next contraction, actual endpoint scalar, all-prime gcd, and whole nonzero same-index error remain outstanding.

---

## 1. Domain, finite boundaries, and accepted computation

Throughout,


$$
j>0,\qquad j\equiv81\pmod{243},
$$




$$
m=2^{2j-1},\qquad n=2m+1=4^j+1,\qquad A=n-2=2m-1,
$$


and


$$
H=3^{h-1},\qquad D=H-A,
$$


with the exact window


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
\tag{1.1}
$$


In particular,


$$
v_3(A)=5.
$$



For the fixed-input evaluation of the first jet, retain


$$
j\equiv84645\pmod{531441}.
\tag{1.2}
$$



The original finite spaces remain


$$
U_u=x^u\quad(0\le u<D),\qquad x=y-1,
$$




$$
z_i=x^Dy^i\quad(0\le i<\nu),\qquad
Y_b=y^b\quad(d\le b\le m),
$$


where


$$
d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
\tag{1.3}
$$



The NEW40 receipt is accepted at its stated finite scope:

* forty full-content/sign comparisons at $m=241,\ldots,260$;
* agreement of Bernstein, monomial and min-plus contents;
* agreement of the signed residue with the exact endpoint at full content;
* six further endpoint cancellations.

It evaluates no original-window producer or inverse. No accepted endpoint, Cartier, or content calculation is requested again.

---

# Part I. Evaluation of six actual jet coordinates

## 2. Simplifying the complete producer force before inversion

Use turn5’s exact normalization


$$
F=(n-1)!,
\qquad
\mathsf T_n=
\left(\binom{a+b}{a}\gamma_{a+b}\right)_{0\le a,b<n},
$$




$$
u_a=\frac{F(-2)^a}{a!},
\qquad
\eta_n=F^2-u^T\mathsf T_n^{-1}u.
\tag{2.1}
$$



The normalized moments satisfy


$$
\gamma_0=1,\qquad \gamma_1=0,\qquad
\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1}.
\tag{2.2}
$$



Let


$$
h=\mathsf T_n^{-1}
\left(\binom{n+a}{a}\gamma_{n+a}\right)_{0\le a<n},
\qquad
v=\mathsf T_n^{-1}u.
\tag{2.3}
$$


Here $h$ is a vector; it is unrelated to the window exponent.

Write $b=-68-A=-n-66$. The complete force in turn5 simplifies exactly to


$$
\boxed{
t=3nh+(b+6)e_{n-1}+\frac{2b}{n-1}e_{n-2}.
}
\tag{2.4}
$$


This follows because the last two terms in the force are actual columns of $\mathsf T_n$.

Moreover,


$$
\chi_n=u^Tt
=3n\,u^Th-12(-2)^{n-2}.
$$


Thus


$$
\boxed{
\chi_n=3\left(nu^Th-4(-2)^{n-2}\right),
\qquad
\xi_n=\frac{\chi_n}{\eta_n}.
}
\tag{2.5}
$$



For


$$
3P_n-Q_c=\sum_{a=0}^{n-1}e_ax^a=3^6R_{\rm prod},
$$


the exact coefficient identity remains


$$
\boxed{
e_a=-\frac{F}{a!}(t_a+\xi_n v_a).
}
\tag{2.6}
$$


No part of the signed rank-one subtraction has been removed.

---

## 3. The actual unit-matrix inverse modulo $9$

Put


$$
n=3N+2,\qquad A=3N.
$$


On our family, $v_3(N)=4$.

### 3.1 The normalized moments modulo $9$

An induction in (2.2) gives


$$
\boxed{
\begin{aligned}
\gamma_{3k}&\equiv1+3f(k),\\
\gamma_{3k+1}&\equiv0,\\
\gamma_{3k+2}&\equiv4+3f(k),
\end{aligned}
\qquad
f(k)=\frac{k(k+1)}2
\pmod9.
}
\tag{3.1}
$$



Let


$$
Z_{ij}=\binom{i+j}{i}.
$$


Group indices by their residues modulo $3$, retaining the sizes


$$
N+1,\quad N+1,\quad N.
$$



Choose the exact integral lift


$$
\mathsf T_0=
\begin{pmatrix}
Z_{N+1}&0&Z_{N+1,N}\\
0&2Z_{N+1}&0\\
Z_{N,N+1}&0&0
\end{pmatrix}.
\tag{3.2}
$$


It is a unit matrix over $\mathbb Z_3$.

Writing


$$
\mathsf T_n=\mathsf T_0+3\mathsf E\pmod9,
$$


the nonzero blocks of $\mathsf E\bmod3$, with $k=i+j$, are


$$
\boxed{
\begin{array}{c|c}
\text{block}&\mathsf E_{ij}\\ \hline
00&f(k)Z_{ij}\\
02,\ 20&(1+f(k))Z_{ij}\\
11&(2+2f(k)+k)Z_{ij}\\
12,\ 21&(k+1)Z_{ij}.
\end{array}}
\tag{3.3}
$$



These are exact modulo-$9$ formulas, not a Lucas-only approximation. For example,


$$
\binom{3k}{3i}\equiv\binom{k}{i}\pmod9
$$


follows by expanding


$$
(1+z)^{3k}=\bigl(1+z^3+3z(1+z)\bigr)^k:
$$


the term linear in $3$ has no exponent divisible by $3$. The other residue blocks follow from the same expansion with the original small offsets.

### 3.2 A finite-difference identity

Set


$$
z_i=(-1)^{N+i}\binom Ni,\qquad 0\le i\le N.
\tag{3.4}
$$


Then


$$
Z_{N+1}z=e_N.
\tag{3.5}
$$



For every polynomial $P$ of degree at most $2$, with coefficients in $\mathbb Z_3$,


$$
\boxed{
\sum_{j=0}^{N}
P(i+j)\binom{i+j}{i}z_j
\equiv
P(i)\binom iN\pmod3.
}
\tag{3.6}
$$


To verify it, use


$$
\sum_{j=0}^{N}z_jX^j=(X-1)^N.
$$


The sums with a factor $j$ or $j(j-1)$ acquire respectively factors $N$ and $N(N-1)$, both zero modulo $3$. The constant-weight sum is $\binom iN$.

This identity retains the finite endpoint $j=N$.

### 3.3 Evaluation of $v=\mathsf T_n^{-1}u$

Modulo $9$, the factorial saturation of $u$ leaves only


$$
u_{3N}=1,\qquad u_{3N+1}=-2.
\tag{3.7}
$$


Indeed, $A$ is divisible by $243$, so every earlier $u_a$ is divisible by $9$, and $(-2)^A\equiv1\pmod9$.

The exact solution of the lifted system is


$$
\mathsf T_0^{-1}u=(z,-z,0)\pmod9.
\tag{3.8}
$$


Equations (3.3) and (3.6) give


$$
\mathsf E(z,-z,0)\equiv(0,e_N,0)\pmod3.
$$


Consequently


$$
\boxed{
v\equiv(z,\,2z,\,0)\pmod9.
}
\tag{3.9}
$$



In particular,


$$
v_{A}=1,\qquad v_{A+1}=2\pmod9,
\tag{3.10}
$$


and


$$
\boxed{
v_{A-1}=v_{A-2}=v_{A-3}=0\pmod9.
}
\tag{3.11}
$$


For the latter, use $N\equiv0\pmod9$ and $z_{N-1}=-N$.

### 3.4 The actual scalar denominator is paid

Since $F^2\equiv0\pmod9$,


$$
\eta_n
\equiv-\bigl(1\cdot1+(-2)\cdot2\bigr)
=3\pmod9.
$$


Therefore


$$
\boxed{v_3(\eta_n)=1.}
\tag{3.12}
$$



Equation (2.5) proves $\chi_n\in3\mathbb Z_3$, hence $\xi_n\in\mathbb Z_3$. The accepted order-six top-coefficient congruence further gives


$$
1+2\xi_n\equiv0\pmod3,
$$


so


$$
\boxed{\xi_n\equiv1\pmod3.}
\tag{3.13}
$$



This proves the actual scalar loss. It does not replace $\eta_n$ by a unit before division.

---

## 4. The first producer jet is actually one-dimensional

Modulo $3$, the vector $h$ in (2.3) is


$$
\boxed{
h\equiv(z,\,0,\,-z_{<N})\pmod3.
}
\tag{4.1}
$$


This follows by multiplying by (3.2): its image is exactly the next normalized moment column, whose residue-$0$ block is $Z_{N+1}e_N$.

Thus


$$
h_{A-1}=h_{A-2}=h_{A-3}=0\pmod3.
\tag{4.2}
$$



Now apply the exact coefficient formula (2.6).

* For $a=A-1,A-2,A-3$,
  

$$
v_3(F/a!)=5.
$$


  At these indices, $t_a=3nh_a\in9\mathbb Z_3$, and $v_a\in9\mathbb Z_3$. Hence
  

$$
e_a\in3^7\mathbb Z_3.
$$



* For $a=A-4,A-5,A-6$,
  

$$
v_3(F/a!)=6.
$$


  Here $t_a\equiv0\pmod3$, and (3.9), together with
  

$$
z_{N-2}=\binom N2\equiv0\pmod3,
$$


  gives $v_a\equiv0\pmod3$. Again $e_a\in3^7\mathbb Z_3$.

* For $a<A-6$, turn5’s proved factorial saturation already gives $e_a\in3^7\mathbb Z_3$.

Therefore


$$
R_{\rm prod}(x+1)\equiv r_Ax^A+r_{A+1}x^{A+1}\pmod3.
\tag{4.3}
$$


The actual endpoint divisibility gives $R_{\rm prod}(-1)\equiv0\pmod3$. Since $x=-2$ is a unit,


$$
r_A-2r_{A+1}=0\pmod3.
$$



### Theorem 4.1 — Actual first-jet collapse

On the retained original family,


$$
\boxed{
R_{\rm prod}(y)\equiv c(y+1)(y-1)^A\pmod3,
\qquad
c=[x^{A+1}]R_{\rm prod}(x+1).
}
\tag{4.4}
$$


In turn19’s notation,


$$
\boxed{(a_0,\ldots,a_6)=(0,0,0,0,0,0,c).}
\tag{4.5}
$$



This is a coefficient-value theorem for the actual producer. It is stronger than its terminal support bound.

---

# Part II. A bounded evaluator for the remaining actual scalar

## 5. Why naive top-degree truncation fails—and how to repair it

The original normalized inverse is not terminal-local. Already modulo $3$, its terminal residue-$1$ row contains


$$
2(-1)^{N+i}\binom Ni,\qquad 0\le i\le N.
$$


Its entry at $i=0$ is a unit. Thus truncating the original matrix $\mathsf T_n$ to a short terminal principal block is not justified.

The repair is an exact finite Pascal congruence, followed by a precision-dependent band theorem.

Let


$$
\mathsf P_{ij}=\binom ij,\qquad
\mathsf B_n=\mathsf P_n^{-1}\mathsf T_n\mathsf P_n^{-T}.
\tag{5.1}
$$


All these Pascal transformations are integral unimodular.

### 5.1 A polynomial moment approximation with an explicit degree

The exact factorial formula is


$$
\gamma_r
=
\sum_{k=0}^{r}
k!\binom rk\binom{r+k}{k}(-2)^{r-k}.
\tag{5.2}
$$



At modulus $3^K$, terms with $v_3(k!)\ge K$ vanish. Also


$$
(-2)^r=(1-3)^r
\equiv\sum_{\ell=0}^{K-1}\binom r\ell(-3)^\ell
\pmod{3^K}.
$$


Hence $\gamma_r\bmod3^K$ agrees, for every nonnegative integer $r$, with an integer-valued polynomial of degree at most


$$
d_K=2(\ell_K-1)+K-1,
$$


where $\ell_K$ is the least integer with $v_3(\ell_K!)\ge K$.

For $K=8$,


$$
\ell_8=18,\qquad d_8=41.
\tag{5.3}
$$



Define


$$
c_k=\sum_{r=0}^{k}(-1)^{k-r}\binom kr\gamma_r
\pmod{3^8},
\qquad 0\le k\le41.
\tag{5.4}
$$


Then


$$
\boxed{
\gamma_r\equiv\sum_{k=0}^{41}c_k\binom rk\pmod{3^8}
\quad(r\ge0).
}
\tag{5.5}
$$


The $c_k$ can be obtained from the integer recurrence (2.2). No division by $3$ is involved.

### 5.2 The transformed matrix is banded

The bivariate generating kernel for
$\binom{a+b}{a}\binom{a+b}{k}$ is


$$
\frac{(z+w)^k}{(1-z-w)^{k+1}}.
$$


The inverse Pascal transform sends this to


$$
\frac{(z+w+2zw)^k}{(1-zw)^{k+1}}.
$$


Consequently


$$
\boxed{
(\mathsf B_n)_{ij}\equiv
[z^iw^j]
\sum_{k=0}^{41}
c_k\frac{(z+w+2zw)^k}{(1-zw)^{k+1}}
\pmod{3^8}.
}
\tag{5.6}
$$


In particular,


$$
\boxed{(\mathsf B_n)_{ij}=0\pmod{3^8}\quad\text{if }|i-j|>41.}
\tag{5.7}
$$



Modulo $3$, $\mathsf B_n$ is block diagonal in consecutive triples. Its complete block is


$$
J_3=
\begin{pmatrix}
1&2&2\\
2&0&0\\
2&0&2
\end{pmatrix},
\tag{5.8}
$$


and, because $n\equiv2\pmod3$, its terminal block is


$$
J_2=
\begin{pmatrix}1&2\\2&0\end{pmatrix}.
\tag{5.9}
$$


Both have unit determinant.

Let $\mathsf C$ be this fixed block-diagonal lift and


$$
\Delta=\mathsf B_n-\mathsf C.
$$


Then


$$
\boxed{
\mathsf B_n^{-1}
\equiv
\sum_{r=0}^{7}
(-\mathsf C^{-1}\Delta)^r\mathsf C^{-1}
\pmod{3^8}.
}
\tag{5.10}
$$


Each additional factor can enlarge support by at most $41+2=43$.

This establishes actual fixed-precision locality. It is not inferred from producer support alone.

---

## 6. Retaining the signed inverse within that local interface

Set


$$
\widehat u=\mathsf P_n^{-1}u.
\tag{6.1}
$$


Because every product of $18$ consecutive integers is divisible by $3^8$,


$$
u_a=0\pmod{3^8}\qquad(a<n-18).
$$


The lower-triangular inverse Pascal transform preserves this terminal support:


$$
\widehat u_i=0\pmod{3^8}\qquad(i<n-18).
\tag{6.2}
$$



Let


$$
b_i=(\mathsf B_{n+1})_{i,n},\qquad0\le i<n,
\tag{6.3}
$$


so $b$ is supported in the last $41$ coordinates modulo $3^8$. Put


$$
z_u=\mathsf B_n^{-1}\widehat u,\qquad
z_b=\mathsf B_n^{-1}b.
\tag{6.4}
$$



The exact Pascal block identity gives


$$
h=\mathsf P_n^{-T}(p+z_b),
\qquad
p_i=\binom ni.
\tag{6.5}
$$


In particular,


$$
h_{n-1}=n+(z_b)_{n-1},
\tag{6.6}
$$


and


$$
u^Th=\widehat u^T(p+z_b).
\tag{6.7}
$$



Likewise,


$$
v_{n-1}=(z_u)_{n-1},
\qquad
u^T\mathsf T_n^{-1}u=\widehat u^Tz_u.
\tag{6.8}
$$



The largest required propagation distance in (5.10) is bounded by


$$
41+7\cdot43+2=344.
$$


A suffix of length $350$, whose left endpoint is divisible by $3$, therefore suffices. This suffix is an arithmetic consequence of the full finite matrix identity; it is not a replacement of the original matrix boundary.

### 6.1 Explicit scalar extraction

At the required modulus, $F^2\equiv0\pmod{3^8}$, so calculate


$$
\eta=-\widehat u^Tz_u\pmod{3^8},
$$




$$
\chi=
3\left(n\widehat u^T(p+z_b)-4(-2)^{n-2}\right)
\pmod{3^8}.
\tag{6.9}
$$



Then perform the paid division


$$
\boxed{
\xi=
(\chi/3)(\eta/3)^{-1}\pmod{3^7}.
}
\tag{6.10}
$$


This is legitimate because $\eta/3\equiv1\pmod3$.

The top coefficient of $3P_n-Q_c$ is


$$
\boxed{
e_{n-1}
=
n+60-3n\bigl(n+(z_b)_{n-1}\bigr)
-\xi(z_u)_{n-1}
\pmod{3^7}.
}
\tag{6.11}
$$


Finally,


$$
\boxed{c=e_{n-1}/3^6\pmod3.}
\tag{6.12}
$$



The order of operations matters:

1. compute the rank-one numerator and denominator modulo $3^8$;
2. divide both by $3$, then invert the unit denominator modulo $3^7$;
3. assemble the **whole** top coefficient modulo $3^7$;
4. only then divide by $3^6$.

No scalar loss is hidden.

---

## 7. Original-power dependence and the fixed original progression

Every binomial coefficient in (5.6) has lower index at most $41$. By Vandermonde’s identity,


$$
\binom{x+3^{11}}k\equiv\binom xk\pmod{3^8},
\qquad 0\le k\le41.
\tag{7.1}
$$


Indeed, every nonconstant Vandermonde term has valuation at least


$$
11-\lfloor\log_3 41\rfloor=8.
$$



All other terminal factors have the same or smaller residue requirement:

* factorial ratios are products of at most $17$ consecutive integers;
* the relevant inverse-Pascal coefficients have bounded lower index;
* $(-2)^a=(1-3)^a\bmod3^8$ depends only on $a\bmod3^7$.

Thus the evaluator depends only on


$$
\boxed{n\bmod3^{11},}
\tag{7.2}
$$


once $n$ is beyond its fixed terminal width.

For original powers,


$$
n=4^j+1,
$$


so this is determined by $j\bmod3^{10}$. On (1.2), the accepted fixed tail


$$
m\equiv1194953\pmod{3^{13}}
$$


gives


$$
n\equiv795584\pmod{3^{13}},
$$


hence


$$
\boxed{n\equiv86996\pmod{3^{11}}.}
\tag{7.3}
$$



Therefore the first jet is constant on the entire sufficiently large fixed-tail original family.

This also settles the compatibility issue: the evaluator is attached to the existing original arithmetic progression, whose exact real-window intersection has positive density. No arbitrary auxiliary order is being promoted to an infinite original-power instance. Nor is an additional condition on unexamined high digits required.

### What is evaluated, and what is not

The proof evaluates six coordinates as zero and reduces the last one to the fixed arithmetic construction (5.4)–(6.12), with input $n_0=86996$.

The numerical execution of that construction is still outstanding. Thus I do **not** yet assert


$$
c=0,\quad c=1,\quad\text{or}\quad c=2.
$$



---

# Part III. Consequences for the actual complete correction

## 8. The full first mixed source is a terminal HIGH charge

Retain the complete functional


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^r)=(2r)!.
\tag{8.1}
$$


The cutoff remains $2v+1\le4n-3$.

Let


$$
W=[U\ Y],\qquad
F_i=\widehat z_i^{\,c},
$$


where the reference is the **complete core**. For either selected original residual column $i=i_0,i_1$,


$$
\begin{aligned}
(T_R)_{w,i}
={}&-\frac{3^h}{4}\mathfrak f(R_{\rm prod}wF_i)\\
&+3^h\sum_{v=0}^{2n-2}
\frac{
[y^v]\bigl(R_{\rm prod}wF_i
-R_{\rm prod}(-1)w(-1)F_i(-1)\bigr)/(y+1)
}{2v+1}.
\end{aligned}
\tag{8.2}
$$


Both columns and every retained row use this whole expression.

Turn19’s complete first-layer formula gives


$$
\frac{(T_R)_{w,i}}3
\equiv
c[y^{r_1}]x^H w(y)y^i
-c\,\mathbf1_{w=Y_m}\mathbf1_{i=\nu-1}
\pmod3,
\tag{8.3}
$$


where $r_1=(H-1)/2$.

For LOW rows, $x^H=y^H-1$, and the lower factor has degree below $r_1$. For HIGH rows,


$$
b+i\le m+\nu-1=r_1-1.
$$


Thus the coefficient extraction vanishes for every retained row and column.

### Theorem 8.1 — Actual terminal-charge form



$$
\boxed{
T_R/3\equiv-c\,e_{Y_m}e_{\nu-1}^{T}\pmod3.
}
\tag{8.4}
$$



The seven-coordinate detector consequently equals


$$
\boxed{(0,0,0,0,0,0,2c)^T.}
\tag{8.5}
$$



This is precisely the original terminal HIGH return. Without that return the complete first source would incorrectly appear to vanish for every $c$.

Conditional on the bounded scalar evaluation:

* if $c\ne0$, then $\min v_3(T_R)=1$, and the proposed $3^g$-factor for the original columns fails;
* if $c=0$, then $T_R\in9M$, but no arbitrary-depth factor follows.

---

## 9. A new cancellation in the actual inverse contraction

Write, as in turn7,


$$
T_R=3T_1,\qquad
T_1=\binom a b,
$$


and


$$
E_{\rm act}=
\begin{pmatrix}
3L_{\rm act}&3X_{\rm act}\\
3X_{\rm act}^T&E_{Y,\rm act}
\end{pmatrix},
$$




$$
\widehat E_{\rm act}
=
E_{Y,\rm act}
-3X_{\rm act}^TL_{\rm act}^{-1}X_{\rm act}.
\tag{9.1}
$$


All displayed unit inverses exist at the retained scope.

The exact nonlinear term is


$$
\mathcal Q
=
a^TL_{\rm act}^{-1}a
+
3\widetilde b^T\widehat E_{\rm act}^{-1}\widetilde b,
\qquad
\widetilde b=b-X_{\rm act}^TL_{\rm act}^{-1}a.
\tag{9.2}
$$



Theorem 8.1 gives


$$
a\in3M,\qquad
\widetilde b\equiv-c\,e_{Y_m}e_{\nu-1}^{T}\pmod3.
\tag{9.3}
$$



### 9.1 The terminal HIGH coordinate is isotropic

Modulo $3$, the complete HIGH block is


$$
(E_Y)_{bc}
=
[y^{r_*-b-c}]x^A,
\qquad
d\le b,c\le m,
\tag{9.4}
$$


where $r_*=(3H-1)/2$. The factorial term is zero at this evaluated layer; it remains in the exact block.

Since


$$
r_*-A=m+d,
$$


we obtain


$$
(E_Y)_{bc}=0\quad(b+c<m+d),
$$


and


$$
(E_Y)_{b,m+d-b}=1.
\tag{9.5}
$$


Thus $E_Y$ is anti-triangular with unit anti-diagonal. Its inverse satisfies


$$
(E_Y^{-1})_{bc}=0\quad(b+c>m+d).
\tag{9.6}
$$


In particular, because $m>d$,


$$
\boxed{(E_Y^{-1})_{mm}=0\pmod3.}
\tag{9.7}
$$



Also


$$
\widehat E_{\rm act}\equiv E_Y\pmod3.
$$


Equations (9.3) and (9.7) imply


$$
\widetilde b^T\widehat E_{\rm act}^{-1}\widetilde b\in3M.
$$


The first term of (9.2) lies in $9M$, since $a\in3M$.

### Theorem 9.1 — Improved complete nonlinear divisibility



$$
\boxed{\mathcal Q\in9M_\nu(\mathbb Z_3).}
\tag{9.8}
$$



This is a statement about the actual inverse contraction, not a deduction from the seven-coordinate map alone.

### 9.2 The next complete contraction

Write $a=3a'$. Then the exact integral next object is


$$
\boxed{
\frac{\mathcal Q}{9}
=
a'^TL_{\rm act}^{-1}a'
+
\frac{\widetilde b^T\widehat E_{\rm act}^{-1}\widetilde b}{3}.
}
\tag{9.9}
$$


The second numerator must be summed completely before division by $3$. Its next digit includes the actual HIGH inverse, the complete LOW/HIGH transport, and the higher producer-force layers.

Equation (9.9), rather than the isolated scalar $c^2$, is the next nonlinear bottleneck.

---

## 10. Depth $15$, both corrected columns, and endpoint transport

The exact complete identities remain


$$
\boxed{
\widehat Z^{\,\rm act}
=
\widehat Z^{\,c}-3^6WE_{\rm act}^{-1}T_R,
}
\tag{10.1}
$$




$$
\boxed{
S_{\rm act}-S_c
=
3^6\Phi_R-3^{13}\mathcal Q.
}
\tag{10.2}
$$


They apply to both selected original columns, their $2\times2$ contraction, and the full residual block.

On the retained window, turn7’s precision theorem applies at $p=10$:

* $C_{10}<C_{16}$;
* $h$ is sufficiently large;
* $\kappa_{10}=27<D$;
* the endpoint and finite-return inequalities hold.

Thus


$$
\Phi_R\in3^{10}M.
\tag{10.3}
$$


Together with


$$
S_c\in3^{17}M,\qquad \mathcal Q\in9M,
$$


this proves


$$
\boxed{S_{\rm act}\in3^{15}M.}
\tag{10.4}
$$



Define the exact integral operator


$$
\boxed{
\Upsilon_{15}
=
\frac{\mathcal Q}{9}
-\frac{\Phi_R}{3^9}
-\frac{S_c}{3^{15}}.
}
\tag{10.5}
$$


Then


$$
\boxed{S_{\rm act}=-3^{15}\Upsilon_{15}.}
\tag{10.6}
$$


All three complete terms are retained. In particular, this is not a pole-only-core substitution.

### 10.1 Endpoint transport

Let $w_-=W(-1)$. The exact endpoint is


$$
e_{\rm act}
=
e_c-3^6T_1^T(3E_{\rm act}^{-1})w_-.
\tag{10.7}
$$


Since $a\in3M$ and the HIGH part of $3E_{\rm act}^{-1}$ carries a factor $3$,


$$
\boxed{e_{\rm act}-e_c\in3^7\mathbb Z_3^\nu.}
\tag{10.8}
$$



More explicitly, with


$$
\widetilde w_Y=w_Y-X_{\rm act}^TL_{\rm act}^{-1}w_U,
$$




$$
\boxed{
\frac{e_{\rm act}-e_c}{3^7}
=
-\left(
a'^TL_{\rm act}^{-1}w_U
+
\widetilde b^T\widehat E_{\rm act}^{-1}\widetilde w_Y
\right).
}
\tag{10.9}
$$


This is the next complete endpoint numerator. It has not been evaluated.

The unit obstruction remains:


$$
(e_{\rm act})_i\equiv(-1)^i\pmod3.
$$


Thus the original endpoint cannot be divided integrally by the growing Jacobi content.

The original terminal closure also remains unchanged:


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right),
\tag{10.10}
$$


including its last equation and $\omega_{\nu-1}$. No moment beyond $D-4$ is introduced.

---

# Part IV. Primitive normalization and remaining arithmetic

## 11. The actual determinant pair at depth $15$

Set


$$
\mathcal D_{0,15}=\det\Upsilon_{15},
$$




$$
\boxed{
\mathcal D_{1,15}
=
e_{\rm act}^T\operatorname{adj}(\Upsilon_{15})e_{\rm act}
-3^{15}d_{\rm act}\det\Upsilon_{15},
}
\tag{11.1}
$$


where


$$
d_{\rm act}=w_-^TE_{\rm act}^{-1}w_-.
$$



Exactly as in turn7,


$$
\det G_{\rm act}
=
\det E_{\rm act}(-3^{15})^\nu\mathcal D_{0,15},
$$




$$
v^T\operatorname{adj}(G_{\rm act})v
=
\det E_{\rm act}(-3^{15})^{\nu-1}\mathcal D_{1,15}.
\tag{11.2}
$$



When the relevant determinants are nonzero,


$$
\boxed{
\frac{\beta_1}{\beta_0}
=
-\frac{3^{h-15}Q_n^{\rm loc}(-1)}4
\frac{\mathcal D_{1,15}}{\mathcal D_{0,15}}.
}
\tag{11.3}
$$


Consequently,


$$
\boxed{
v_3(q)=
\max\!\left\{
0,\,
h-15+v_3(Q_n^{\rm loc}(-1))
+v_3(\mathcal D_{1,15})
-v_3(\mathcal D_{0,15})
\right\}.
}
\tag{11.4}
$$



The depth contributes one factor in the determinant ratio—not $15\nu$.

Nor does the new depth protect the core inverse. The known core loss still satisfies $s_c\ge17$, while the guaranteed actual-core precision is now $15$, not greater than $s_c$.

The actual eliminated-inverse bill remains $1$, and Christoffel inversion still loses $4$ digits. Projected Jacobi channels are not original unit residual columns.

The common content of the two Jacobi polynomials remains $O(\log m)$. No degree-$m$ amplification is inferred without its exact multiplicity.

---

## 12. Final all-prime gcd and whole same-index error

After the actual row contents, actual multiplier and least actual clearer, retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and


$$
\boxed{g_\ell=\gcd(|A_\ell|,|B_\ell|)}
$$


over all primes.

For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and the whole evaluated error is still


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
\tag{12.1}
$$



For the weighted producer, likewise,


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B,
$$




$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
\tag{12.2}
$$



Nothing above evaluates either all-prime gcd, proves the necessary distinguished-cofactor nonvanishing, or supplies decay of the whole nonzero primitive error.

---

## 13. The genuinely new bounded calculation

No accepted calculation should be rerun.

### Inputs

Use


$$
M=3^8=6561,\qquad n_0=86996,\qquad L=350.
$$


The suffix indices are


$$
86646,\ldots,86995,
$$


with $86646\equiv0\pmod3$.

1. Generate $\gamma_0,\ldots,\gamma_{41}\bmod6561$ by (2.2).
2. Form $c_0,\ldots,c_{41}$ by (5.4).
3. Construct the bandwidth-$41$ suffix matrix by (5.6), and its next-column vector $b$.
4. Construct the last $18$ entries of $u$, then $\widehat u$.
5. Apply the eight-term formula (5.10) to $\widehat u$ and $b$, using only the fixed unit blocks $J_3,J_2$.
6. Evaluate (6.9)–(6.12), paying both displayed divisions.

A direct coefficient formula for step 3 is


$$
\sum_{k=0}^{41}c_k
\sum_{\substack{\alpha+\beta+\gamma=k\\
i-\alpha-\gamma=j-\beta-\gamma=\ell\ge0}}
\frac{k!}{\alpha!\beta!\gamma!}\,2^\gamma
\binom{\ell+k}{k}.
\tag{13.1}
$$


All binomial and multinomial coefficients can be evaluated as exact integers before reduction. No nonunit factorial is inverted modulo $6561$.

This requires storage only for a bounded band and bounded modular matrix-vector products. It never constructs $C_n$, $\mathsf T_n$, or an original-window polynomial of degree $n$.

### Expected verifiable output

The new certificate should display:

1. $\eta\bmod9=3$;
2. $\chi\bmod9=3$;
3. $\xi\bmod3=1$;
4. the assembled $e_{n-1}\bmod2187$, necessarily one of
   

$$
0,\ 729,\ 1458;
$$


5. the resulting $c\in\{0,1,2\}$;
6. the eight residues
   

$$
(0,0,0,0,0,0,2c,c);
$$


7. the seven detector residues
   

$$
(0,0,0,0,0,0,2c);
$$


8. the selected conclusion:
   * $c\ne0$: actual terminal mixed-source valuation exactly $1$;
   * $c=0$: $T_R\in9M$, without an arbitrary-depth claim.

Because the residue-dependence theorem has been proved, this single fixed arithmetic evaluation would select the first-jet branch on the entire sufficiently large original progression (1.2), including its exact real-window subsequence. Its scope is not merely an auxiliary-$n$ comparison.

No output from this calculation is assumed here.

---

## 14. Proof-status ledger

| Statement | Status |
|---|---|
| NEW40 content/sign receipt, including six cancellations | Accepted finite corroboration |
| Actual normalized inverse formula modulo $9$, §3 | Proved |
| Actual scalar denominator $v_3(\eta_n)=1$ | Proved |
| Six vanishing first-jet coordinates | Proved for the actual producer |
| $R_{\rm prod}\equiv c(y+1)x^A\pmod3$ | Proved |
| Naive truncation of the original unit matrix | Not valid; dense inverse obstruction displayed |
| Pascal-transformed bandwidth $41$ modulo $3^8$ | Proved |
| $350$-coordinate, precision-paid evaluator | Derived explicitly; not executed |
| Dependence only on $n\bmod3^{11}$ | Proved |
| Fixed input $n_0=86996$ on the original fixed-tail progression | Derived from the accepted original tail |
| Numerical value of $c$ | Outstanding bounded calculation |
| Complete first source is terminal HIGH charge only | Proved |
| $\mathcal Q\in9M$ through the actual HIGH inverse | Proved |
| $S_{\rm act}\in3^{15}M$ and $e_{\rm act}-e_c\in3^7$ | Proved on the stated window |
| Next complete contraction $\mathcal Q/9$ | Exact formula supplied; not evaluated |
| Actual relative determinant-pair arithmetic | Unresolved |
| All-prime primitive denominator and whole nonzero error | Unresolved |

## Conclusion

The actual producer analysis now goes beyond terminal support and beyond a detector with seven free coefficients:



$$
\boxed{
R_{\rm prod}(y)\equiv c(y+1)(y-1)^A\pmod3,
}
$$


with six coordinates proved zero and the remaining scalar given by an explicit, realistic, precision-paid terminal evaluator.

Top-degree locality does survive the signed rank-one inverse **after** the correct Pascal congruence and after paying its actual one-digit scalar loss. It does not survive as a naive truncation of the original normalized matrix.

The resulting complete mixed force is only the original terminal HIGH charge. Its isotropy for the leading actual HIGH inverse proves the new unconditional cancellation


$$
\boxed{\mathcal Q\in9M,\qquad S_{\rm act}\in3^{15}M.}
$$



The immediate bounded task is to execute the fixed evaluator and report $c$. The next mathematical bottleneck is the whole contraction (9.9), together with the endpoint numerator (10.9), and ultimately the relative arithmetic of the exact determinant pair—not another support bound or a presumed Jacobi-content division.

The global obligation remains an infinite original sequence with the actual all-prime primitive denominator and


$$
0<|q(e+\pi)-p|\longrightarrow0
$$


for the whole same-index error.



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$


