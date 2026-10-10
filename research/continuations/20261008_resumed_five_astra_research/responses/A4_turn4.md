> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A coefficient-adapted terminal dual and the next ternary arithmetic evaluation

## Abstract

The rationality or irrationality of $e+\pi$ remains unresolved. The present report does, however, evaluate the specific original-index coefficient requested in the assignment.

On the unchanged sufficiently large original family, let


$$
\Psi_a=x^{D+b}y^{k_0+a}(y^{3Q}+3),
\qquad
k_0=\frac{3Q+1}{2},
\qquad 0\le a\le b/2,
$$


and let $\mathcal F_a$ be its **actual complete-core LOW/HIGH correction**. Then


$$
\boxed{
[y^m]\mathcal F_a
\equiv -3^{27}\delta_{a,b/2}\pmod{3^{28}}.
}
\tag{A}
$$


In particular,


$$
v_3([y^m]\mathcal F_{b/2})=27,
\qquad
[y^m]\mathcal F_a\in3^{28}\mathbb Z_3\quad(a<b/2).
$$


Thus the physical-terminal coefficient has not been suppressed: its last prescribed amplitude is nonzero at the evaluated scale.

Combining (A) with the previously proved, fully normalized identity


$$
(\gamma_c)_a
=-\delta_{a,b/2}
-\frac{[y^m]\mathcal F_a}{3^{27}}\pmod3
$$


gives the new evaluation


$$
\boxed{\gamma_c=0.}
\tag{B}
$$



The proof does **not** extend the old $p\le25$ disjoint-support argument without modification. It uses:

1. a three-column, coefficient-adapted construction **inside the actual $W$**, giving an explicit physical-terminal inverse row modulo $9$;
2. a $p=26$ filter whose terms above $Y_m$ are removed;
3. an explicit evaluation of the return of that removed tail;
4. separate treatment of the collision $2s+1=L=27Q$;
5. the original finite pole cutoff throughout.

The two coordinator interfaces—the full inverse dual to the actual omitted monomial window, and the normalized lacunary Schur/Selberg minor—are independently validated below as exact rational identities. Neither interface, by itself, supplies a ternary valuation estimate.

No tool computation was performed. The supplied auxiliary certificate is not recomputed and is not used as an original ternary index.

---

## 1. Original domain, finite objects, and proof inputs

All uniform assertions concern sufficiently large indices satisfying exactly


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


with the original global window


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15},
$$


and the fixed subwindow


$$
\frac{103}{1000}<\rho:=\frac{N_0}{P_0}<\frac{104}{1000}.
$$



The original parameters remain


$$
P_0=243P=3^{h-27},\qquad N_0=243r,\qquad D=P_0+N_0,
$$




$$
P=3^{h-32},\qquad r\equiv2\pmod9,\qquad r\text{ odd},
$$


and


$$
\boxed{4^j=243(3^{26}-1)P-243r+1.}
$$


No independent auxiliary choice of $P,r$ is substituted for an original index.

Put


$$
x=y-1,\qquad Q=3^{h-29},\qquad b=Q-N_0.
$$


Then


$$
D=10Q-b,\qquad .064<\frac bQ<.073,
$$


with $D,b$ even and $Q$ odd. Also


$$
m=\frac{H-D+1}{2},\qquad
\nu=\frac D2-1,\qquad d=D+\nu.
$$



The finite coordinates are exactly


$$
U_s=x^s\quad(0\le s<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_t=y^t\quad(d\le t\le m),
\qquad W=[U\ Y].
$$


The omitted monomial degrees are


$$
I=\{D,\ldots,d-1\}.
$$


The physical HIGH terminal is $Y_m$. It is not the last middle direction $z_{\nu-1}$.

### 1.1 Complete functional and physical pole functional

The complete functional is retained:


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!.
$$


The complete core is


$$
G_c(f,g)=\mathcal M(Q_cfg),
\qquad
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A.
$$



For clarity, write


$$
K_{\rm phys}=2n-2=2H-2D+2
$$


and define the finite coefficient functional


$$
\Lambda_h(P)=
3^h\sum_{v=0}^{K_{\rm phys}}\frac{[y^v]P}{2v+1}.
\tag{1.1}
$$


Then


$$
\mathcal P(f,g)=\Lambda_h\bigl(x^A(\beta+3y)fg\bigr).
$$



The largest original denominator is


$$
\boxed{2K_{\rm phys}+1=4n-3=4H-4D+5<3^{h+1}.}
\tag{1.2}
$$


Consequently $\Lambda_h$ is integral on integral coefficient polynomials, with the displayed truncation.

Later, a polynomial temporarily exceeding degree $m$ is used only as bookkeeping. Whenever that occurs, (1.1) remains truncated at $K_{\rm phys}$. No successor moment or enlarged Gram matrix is introduced.

Let


$$
E_{\mathcal P}=\mathcal P(W,W),\qquad
E_c=G_c(W,W).
$$


The actual complete-core corrected columns are


$$
F_i=z_i-WE_c^{-1}G_c(W,z_i).
$$



### 1.2 Established results reused at their proved scope

The following closed inputs are reused; their expensive original calculations are not repeated:

- integral unimodularity of the original corrected basis;
- $E_c^{-1},E_{\rm act}^{-1}\in3^{-1}M$;
- the paid pole comparison
  

$$
E_{\mathcal P}^{-1}\in3^{-1}M,\qquad
  F_{\mathcal P}-F_c\in3^{h-1}WM,\qquad
  S_{\mathcal P}-S_c\in3^hM;
$$


- $S_c\in3^{26}M$;
- the finite prefix identities, H2, complete producer comparison, and paid rank-$b$ elimination;
- the alternative pole proof of the nonterminal coupling strip;
- $\Pi=0$, $T\in81M$, and the Turn 3 terminal bootstrap;
- the previously proved formula
  

$$
(\gamma_c)_a
  =-\delta_{a,b/2}
  -3^{-27}[y^m]\mathcal F_a\pmod3.
  \tag{1.3}
$$



The older unquantified support-layer extension is not used in place of the closed alternative strip proof.

The density statement is used only at its supplied scope: there are infinitely many original indices in the same fixed subwindow.

---

## 2. Audit of the full inverse dual interface

The coordinator’s first note is correct as an exact finite rational interface.

### 2.1 Sign and linear weight

Since $A=2m-1$ is odd,


$$
\mathcal P(f,g)
=\frac{3^h}{2}\int_0^1
y^{-1/2}(1-y)^A(A+71-3y)f(y)g(y)\,dy.
$$


Set


$$
z=\frac{A+71}{3}>1,\qquad c=\frac{3^{h+1}}2,
\qquad d\mu_0=y^{-1/2}(1-y)^A\,dy.
$$


Then


$$
d\mu_{\mathcal P}=c(z-y)\,d\mu_0.
\tag{2.1}
$$


The sign is therefore positive on $0<y<1$.

For


$$
I_A(u)=\frac12B(u+\tfrac12,A+1)
=\frac{2^AA!}{\prod_{v=0}^{A}(2u+2v+1)},
$$


the full monomial Gram matrix


$$
B=(\mathcal P(y^r,y^s))_{0\le r,s\le m}
$$


has entries


$$
B_{rs}=3^h(-1)^A
\bigl(\beta I_A(r+s)+3I_A(r+s+1)\bigr).
\tag{2.2}
$$


At $r+s=2m$, the second product ends at


$$
2(2m+1+A)+1=8m+1=4n-3.
$$


Thus (2.2) respects the exact original cutoff.

### 2.2 Jacobi leading coefficient and norm

For the base weight $d\mu_0$, define


$$
\ell_r=\binom{2r+A-\tfrac12}{r},
$$




$$
p_r(y)=\ell_r^{-1}
\sum_{j=0}^r
\binom{r+A}{j}\binom{r-\tfrac12}{r-j}
(y-1)^{r-j}y^j.
\tag{2.3}
$$


Vandermonde convolution gives the coefficient of $y^r$ in the numerator as $\ell_r$, so $p_r$ is monic.

These are the shifted Jacobi parameters $(A,-1/2)$, both greater than $-1$. Their monic norms are


$$
h_r=
\frac{(r+1)_A}
{(r+\tfrac12)_A(2r+A+\tfrac12)\ell_r^2}.
\tag{2.4}
$$


Indeed, the unnormalized Jacobi norm is


$$
\frac{\Gamma(r+A+1)\Gamma(r+\tfrac12)}
{(2r+A+\tfrac12)\,r!\,\Gamma(r+A+\tfrac12)},
$$


and division by $\ell_r^2$ gives (2.4).

Every $\ell_r$, Pochhammer factor, and norm denominator is retained. None is automatically a ternary unit.

### 2.3 Christoffel modification and its divisors

All zeros of $p_r$ lie in $(0,1)$, so $p_r(z)>0$. Put


$$
a_r=\frac{p_{r+1}(z)}{p_r(z)},
\qquad
q_r(y)=\frac{p_{r+1}(y)-a_rp_r(y)}{y-z}.
\tag{2.5}
$$


The numerator vanishes at $z$, and $q_r$ is monic of degree $r$.

Since


$$
(z-y)q_r=-p_{r+1}+a_rp_r,
$$


base orthogonality gives orthogonality of $q_r$ for $d\mu_{\mathcal P}$. Its norm is


$$
H_r=c\,a_rh_r>0.
\tag{2.6}
$$


The sign in (2.6) is correct.

If $v_r$ is the coefficient column of $q_r$ in degrees $0,\ldots,m$, then


$$
\boxed{B^{-1}=\sum_{r=0}^m\frac{v_rv_r^T}{H_r}.}
\tag{2.7}
$$


This follows from the exact diagonalization by the monic coefficient matrix.

The temporary use of $p_{m+1}$ in defining $q_m$ requires base-weight polynomial degrees at most $2m+1$. Its largest beta pole is still


$$
2(A+2m+1)+1=8m+1.
$$


It does not introduce a complete-core moment beyond degree $2n-1$.

### 2.4 The actual omitted window and the upper-triangular change

Let


$$
J=\{0,\ldots,D-1\}\cup\{d,\ldots,m\},
\qquad
M=E_I^TB^{-1}E_I.
$$


The LOW $x$-basis and LOW monomial basis differ by an integral unitriangular matrix. Thus $J$ is exactly the coefficient subspace of the actual $W$.

The $I$-coefficients of $z_i=x^Dy^i$ are


$$
T_{ri}=
\begin{cases}
(-1)^{i-r}\binom D{i-r},&r\le i,\\
0,&r>i.
\end{cases}
\tag{2.8}
$$


This is upper unitriangular, with inverse


$$
(T^{-1})_{ri}=
\begin{cases}
\binom{D+i-r-1}{i-r},&r\le i,\\
0,&r>i.
\end{cases}
$$


There is no fractional middle-basis change.

If $X$ is the full coefficient matrix of the actual pole-corrected columns, then $X_I=T$ and $(BX)_J=0$. Hence


$$
\boxed{
X=B^{-1}E_IM^{-1}T,\qquad
S_{\mathcal P}=T^TM^{-1}T.
}
\tag{2.9}
$$


This proves the identity for the selected LOW/HIGH projection, not a projection onto consecutive Jacobi degrees.

The determinant identity is consequently


$$
\boxed{
\det S_{\mathcal P}
=\frac1{\det M}
=\frac{\det B}{\det B_{JJ}}.
}
\tag{2.10}
$$



### 2.5 Physical terminal and complete rank-one divisor

Only the monic $q_m$ contributes to the $y^m$ row of (2.7). If $v=(v_m)_I$, then


$$
[y^m]F_{\mathcal P}
=\frac{v^TM^{-1}T}{H_m}.
\tag{2.11}
$$



Write


$$
M_< =\sum_{r=0}^{m-1}\frac{(v_r)_I(v_r)_I^T}{H_r},
\qquad
\theta=v^TM_<^{-1}v.
$$


Because $d-1<m$, restriction of polynomials of degree at most $m-1$ spans all $I$-coefficient directions. Therefore $M_<$ is positive definite. Sherman–Morrison gives, for $a=Tu$,


$$
\boxed{
[y^m]F_{\mathcal P}u
=\frac{v^TM_<^{-1}a}{H_m+\theta}.
}
\tag{2.12}
$$


The denominator is $H_m+\theta$, not merely $H_m$.

Real positivity proves that this denominator is nonzero over $\mathbb R$. It gives no bound on its $3$-adic valuation. Likewise, the real estimate


$$
|[y^m]F_{\mathcal P}u|^2
\le \frac{\mathcal P(F_{\mathcal P}u,F_{\mathcal P}u)}{H_m}
$$


is not an arithmetic divisibility theorem.

**Audit conclusion.** All displayed exact identities in this interface are valid, with their stated rational factors. Their arithmetic application remains separate.

---

## 3. Audit of the lacunary Schur/Selberg interface

The second coordinator note is also correct at its stated exact-identity scope.

To avoid confusion with the original integer $b$, use $a_{\rm J},b_{\rm J}$ for the beta parameters in this section.

### 3.1 Direct proof of the single-Schur identity

For $a_{\rm J},b_{\rm J}>0$, let


$$
J_w=\det\bigl(B(a_{\rm J}+i+j,b_{\rm J})\bigr)_{0\le i,j<w}.
$$


For a partition $\kappa$ of length at most $w$, put


$$
t_i=i-1+\kappa_{w+1-i}.
$$


Bialternants and Andréief give


$$
\mathbb E s_\kappa
=
\frac{
\det\bigl(B(a_{\rm J}+t_i+j,b_{\rm J})\bigr)_
{1\le i\le w,\ 0\le j<w}}
{J_w}.
\tag{3.1}
$$



After removing the row factors


$$
\Gamma(b_{\rm J})
\frac{\Gamma(a_{\rm J}+t_i)}
{\Gamma(a_{\rm J}+b_{\rm J}+t_i+w-1)},
$$


the $j$-th remaining polynomial is


$$
(a_{\rm J}+t)_j
(a_{\rm J}+b_{\rm J}+t+j)_{w-1-j}.
$$


Its degree is at most $w-1$. Their alternating determinant is a constant times $V(t)$.

Evaluation at $t=-a_{\rm J}-r$, $0\le r<w$, makes the matrix triangular. The diagonal is


$$
(-1)^r r!(b_{\rm J})_{w-1-r},
$$


while the Vandermonde is


$$
(-1)^{w(w-1)/2}\prod_{r=0}^{w-1}r!.
$$


Therefore


$$
\begin{aligned}
&\det\bigl(B(a_{\rm J}+t_i+j,b_{\rm J})\bigr)\\
&\quad=
\Gamma(b_{\rm J})^w
\prod_i
\frac{\Gamma(a_{\rm J}+t_i)}
{\Gamma(a_{\rm J}+b_{\rm J}+t_i+w-1)}
V(t)\prod_{j=0}^{w-1}(b_{\rm J})_j.
\end{aligned}
\tag{3.2}
$$


The out-of-domain test points are used only after passage to a polynomial identity.

Setting $t_i=i-1$ gives


$$
J_w=\prod_{j=0}^{w-1}
\frac{j!\,\Gamma(a_{\rm J}+j)\Gamma(b_{\rm J}+j)}
{\Gamma(a_{\rm J}+b_{\rm J}+w+j-1)}.
\tag{3.3}
$$


Dividing (3.2) by (3.3), with the Weyl dimension formula, proves


$$
\boxed{
\mathbb E s_\kappa
=s_\kappa(1^w)
\prod_{i=1}^w
\frac{(a_{\rm J}+w-i)_{\kappa_i}}
{(a_{\rm J}+b_{\rm J}+2w-i-1)_{\kappa_i}}.
}
\tag{3.4}
$$



Thus the required $\gamma=1$ single-Schur beta identity has a complete direct proof. No unverified two-factor or plethystic-shift simplification is needed.

### 3.2 The actual exponent-gap partition

Here


$$
a_{\rm J}=\frac12,\qquad b_{\rm J}=A+1,\qquad
w=m+1-\nu,
$$


and


$$
\lambda=(\nu^{\,m-d+1},0^D).
\tag{3.5}
$$


Indeed, for increasing exponents $e_i\in J$,


$$
e_i=i-1
$$


on LOW and


$$
e_i=i-1+\nu
$$


on HIGH. Hence the actual alternant is $V(y)s_\lambda(y)$.

The linear pole factor is retained:


$$
\boxed{
\det B_{JJ}
=c^wJ_w\,
\mathbb E\!\left[s_\lambda(y)^2\prod_{i=1}^w(z-y_i)\right].
}
\tag{3.6}
$$


This is the actual lacunary minor.

Expanding $s_\lambda^2$ by Littlewood–Richardson coefficients and the elementary symmetric factors by Pieri gives exactly the finite rational sum in the coordinator note. The signs $(-1)^j z^{w-j}$, vertical-strip condition, and length restriction are correct.

The application has $b_{\rm J}=A+1$, not the parameter required for the proposed unshifted two-factor specialization. Thus importing that specialization would be unjustified.

### 3.3 Boundary and denominator audit

For every partition $\mu$ occurring in the LR/Pieri expansion,


$$
\mu_1\le2\nu+1.
$$


After multiplication by $V(y)^2$, the largest power of any variable is at most


$$
\mu_1+2(w-1)\le2m+1.
$$


Consequently the largest beta pole is


$$
2(A+2m+1)+1=8m+1=4n-3.
$$


There is no enlarged physical cutoff.

The full determinant satisfies


$$
\det B=c^{m+1}J_{m+1}p_{m+1}(z),
$$


by telescoping the monic Christoffel norm product. Therefore


$$
\boxed{
\det S_{\mathcal P}
=
\frac{c^\nu J_{m+1}p_{m+1}(z)}
{J_w\,C_J(z)}.
}
\tag{3.7}
$$


All factors in this quotient remain present.

In the original subwindow,


$$
v_3(z)=-1.
$$


Nevertheless, the leading power of $z$ cannot be declared dominant without controlling the other rational coefficients and their cancellations. The gamma products, Pochhammer divisors, Christoffel values, and the full $C_J(z)$ are not automatically ternary units.

**Audit conclusion.** The normalized identity is sound. It is not an evaluated original-index valuation theorem.

The supplied auxiliary receipt remains a certificate only for its stated finite auxiliary identity. Its parameters are not an original ternary tuple, and no original valuation is inferred from it.

---

## 4. A new coefficient-adapted inverse row inside the actual $W$

The following construction is the key arithmetic addition.

Define


$$
g_r=\binom{D+r-1}{r}\quad(r\ge0),\qquad g_r=0\quad(r<0),
$$


and, for $k=0,1,2$,


$$
\Omega_k(y)
=
y^{d+k}
-\sum_{u=0}^{D-1}\binom{d+k}{u}x^u.
\tag{4.1}
$$


These polynomials belong to the actual $W$: they contain one actual HIGH monomial and LOW $x$-coordinates only. They are also divisible by $x^D$:


$$
\Omega_k=x^Ds_k,
\qquad
s_k(y)=\sum_{\ell=0}^{\nu+k}g_\ell y^{\nu+k-\ell}.
\tag{4.2}
$$


The quotient formula follows from polynomial division of $y^{d+k}$ by $(y-1)^D$.

Let


$$
R^{[25]}(y)=R_{3^{24}}(y^{81Q}),
$$


where the already proved Jacobi normalization gives


$$
R^{[25]}\in\mathbb Z_3[y],
\qquad R^{[25]}\equiv1\pmod9.
$$



### 4.1 Actual degree and LOW/HIGH checks

For $k\le2$,


$$
m-\deg(\Omega_kR^{[25]})
=
\frac{81Q-4D+3-2k}{2}>0.
\tag{4.3}
$$


Every nonconstant filter term begins at monomial degree at least $81Q>d+2$. Thus


$$
\Omega_kR^{[25]}\in W,
$$


with no omitted middle coefficient introduced and no term crossing $Y_m$.

For LOW rows, the residual low-band degree is at most $d+k$, below $(81Q-1)/2$. For HIGH rows, the only macro moment outside the Jacobi orthogonality range is $q=M_{25}$. It occurs at physical rows $Y_{m-r}$, $0\le r\le k+1$.

The largest macro denominator thereby completed is


$$
4H-81Q<4H-4D+5.
$$


Hence the exceptional moment is still wholly physical.

Using the retained exact exceptional scalar $\mathfrak t_{25}\in\mathbb Z_3^\times$, one obtains


$$
\boxed{
\mathcal P(W,\Omega_kR^{[25]})
\equiv
\mathfrak t_{25}
\sum_{r=0}^{k+1}
\bigl(\beta g_{k-r}+3g_{k-r+1}\bigr)e_{Y_{m-r}}
\pmod{3^{25}}.
}
\tag{4.4}
$$


This keeps the exceptional physical-terminal moment rather than declaring it negligible.

### 4.2 A three-column paid certificate

Put


$$
\chi=-\frac3\beta,
\qquad
\mathscr D_{\rm tr}
=
\frac{R^{[25]}}{\beta\mathfrak t_{25}}
\left(\Omega_0+\chi\Omega_1+\chi^2\Omega_2\right).
\tag{4.5}
$$


Both $\beta$ and $\mathfrak t_{25}$ are ternary units, so all coefficients are integral over $\mathbb Z_3$.

The finite convolution in (4.4) telescopes. For $0\le r\le3$,


$$
\sum_{k=0}^2
\chi^k\bigl(\beta g_{k-r}+3g_{k-r+1}\bigr)
=
\beta\delta_{r0}-\beta\chi^3g_{3-r}.
$$


Therefore


$$
\mathcal P(W,\mathscr D_{\rm tr})
\equiv
e_{Y_m}
-\chi^3\sum_{r=0}^3g_{3-r}e_{Y_{m-r}}
\pmod{3^{25}}.
\tag{4.6}
$$


The whole residual is in $3^3M$.

Let


$$
\mathscr D=WE_{\mathcal P}^{-1}e_{Y_m}.
$$


The established inverse loses one digit, so (4.6) proves


$$
\boxed{
\mathscr D\in W\mathbb Z_3,\qquad
\mathscr D\equiv
\frac{\Omega_0-(3/\beta)\Omega_1}
{\beta\mathfrak t_{25}}
\pmod{9W\mathbb Z_3}.
}
\tag{4.7}
$$


This is an actual physical-terminal inverse row of the actual finite $W$.

The payment is explicit:


$$
\text{residual }3^3
\quad\xrightarrow{\,E_{\mathcal P}^{-1}\in3^{-1}M\,}\quad
\text{row error }3^2.
$$



### 4.3 Optional normalization of the row

The unit in (4.7) can also be evaluated without a new large calculation:


$$
\beta\equiv1\pmod9,\qquad \mathfrak t_{25}\equiv7\pmod9.
$$


Thus


$$
\boxed{\mathscr D\equiv4\Omega_0+6\Omega_1\pmod9.}
\tag{4.8}
$$



Here is a check of the new unit evaluation. For $N=3^{24}$, $M=(N-1)/2$, let $r_M$ be the leading coefficient of $R_N$. The exact coefficient formula gives


$$
\frac{r_M}{3^{25}}
\equiv
\frac{(-1)^M2^{2M-1}}
{M\binom{2M}{M}}
\pmod9,
$$


because every omitted factor $1+3N/(2a)$ lies in $1+9\mathbb Z_3$.
The already established binomial recurrence gives


$$
\binom{N-1}{M}\equiv7\pmod9.
$$


Since $M\equiv4\pmod9$, $M$ is even, and $2^{2M-1}\equiv2\pmod9$, the displayed quotient is $2$.

The exact Jacobi norm identities give


$$
\mathfrak t_{25}
=\frac{3^{25}K_N}{(4N-1)r_M}.
$$


The closed binomial recurrence in the formula for $K_N$ gives $K_N\equiv4\pmod9$. Hence


$$
\mathfrak t_{25}\equiv\frac4{(-1)\cdot2}\equiv7\pmod9.
$$


All denominators used in this reduction are proved units.

The subsequent cancellation needs only (4.7), not the numerical form (4.8).

---

## 5. The paid $p=26$ trial and its exact physical truncation

Now put


$$
N=3^{25},\qquad M=\frac{N-1}{2},\qquad
L=27Q,\qquad R(y)=R_N(y^L).
$$


For the prescribed original column, write


$$
\Psi_a=x^Dp_a,
\qquad
p_a=x^by^{k_0+a}(y^{3Q}+3).
$$


The fixed window gives


$$
\deg p_a\le\nu-3.
\tag{5.1}
$$



Set


$$
t=b/2-a,\qquad 0\le t\le b/2.
$$


The virtual filtered polynomial


$$
V_a=\Psi_aR
$$


has degree


$$
\deg V_a=m+6Q-t.
\tag{5.2}
$$


Thus it is not an admissible original column.

Only the top filter term can exceed $m$, because the next term has degree


$$
m+6Q-t-L=m-21Q-t<m.
$$


Let $r_M=[Y^M]R_N(Y)$, and define


$$
O_a=[y^{>m}]\bigl(y^{ML}\Psi_a\bigr).
$$


The actual trial is


$$
\boxed{\widehat V_a=V_a-r_MO_a=[y^{\le m}]V_a.}
\tag{5.3}
$$


It has degree at most $m$, and


$$
\widehat V_a-\Psi_a\in\operatorname{span}Y.
\tag{5.4}
$$


Indeed, every nonconstant filter term begins above $d$.

The Jacobi coefficient valuation is


$$
v_3(r_M)=26.
\tag{5.5}
$$


Removing the tail is therefore not free at the requested precision. Its return will be evaluated explicitly in Section 7.

---

## 6. Full virtual residual and a coefficient-adapted collision calculation

### 6.1 The full virtual residual is in $3^{27}$

We first prove


$$
\boxed{\mathcal P(W,V_a)\in3^{27}M,}
\tag{6.1}
$$


where the notation uses the fixed truncated functional (1.1).

This assertion does not say that $V_a$ is an original column.

Let


$$
Z=y^{9Q},\qquad Y=y^{27Q}.
$$


The coefficientwise Frobenius congruence at the next scale gives


$$
x^H
\equiv
(Y-1)^N+3^{26}E_1(y)
\pmod{3^{27}},
\tag{6.2}
$$


where


$$
E_1=Z(1-Z)(Y-1)^{N-1}.
$$


Indeed,


$$
(Z-1)^3=Y-1+3Z(1-Z),
$$


and raising to $N=3^{25}$ leaves exactly the displayed linear term modulo $3^{27}$. Every term of order at least two has valuation at least $27$.

For the first term of (6.2), a denominator surviving modulo $3^{27}$ must be divisible by $L$. Expanding the remaining LOW or HIGH polynomial into monomials, its exponent must therefore be


$$
qL+\frac{L-1}{2}.
$$



- LOW bands may now cross $(L-1)/2$. They are **not** discarded by the old disjoint-support argument. Their possible $q=0$ contribution is instead annihilated by the exact Jacobi moment.
- For every HIGH row, including $Y_m$, (5.1) gives $q\le M-1$. Those complete macro moments are also zero.

The largest denominator in any completed macro moment is


$$
(4N-3)L=4H-81Q<4H-4D+5.
\tag{6.3}
$$


Thus no completion passes the physical cutoff.

For the error in (6.2), reduce $R$ modulo $3$, where $R\equiv1$. The polynomial $E_1$ has degree $H-9Q$. Multiplication by $p_a$ and any actual $W$-row still leaves the degree strictly below


$$
\frac{3H-1}{2},
$$


the index of the only pole with denominator valuation $h$. Hence that error gains one further digit from the pole weights. This proves (6.1).

### 6.2 A whole pairing needed for the physical row

We now prove


$$
\boxed{\mathcal P(\Omega_0,V_a)\in3^{28}\mathbb Z_3.}
\tag{6.4}
$$


This is an evaluated pairing, not an unevaluated inverse expression.

Since $\Omega_0=x^Ds_0$,


$$
\mathcal P(\Omega_0,V_a)
=\Lambda_h\bigl(x^H B_a(y)R(y)\bigr),
$$


where


$$
B_a=x^{10Q}s_0(y)(\beta+3y)y^{k_0+a}(y^{3Q}+3).
\tag{6.5}
$$


Its degree is


$$
\deg B_a=\frac{39Q+1}{2}-t<2D<L.
\tag{6.6}
$$



#### The term without the Frobenius error

Write


$$
A_1(Y)=(Y-1)^NR_N(Y)=\sum_q a_qY^q.
$$


For $B_{a,s}$, put $c_s=2s+1$. Since $c_s<4D<40Q$, there are three cases.

1. **The collision $c_s=L=27Q$.**  
   Its entire contribution is
   

$$
3^{26}\sum_q\frac{a_q}{2q+1}=0
$$


   by the $q=0$ Jacobi moment. This is the actual macro-denominator collision; it is not treated by an invalid expansion in $L/c_s$.

2. **The case $c_s=9Q$.**  
   The contribution is
   

$$
3^{27}\sum_q\frac{a_q}{1+6q}.
$$


   Modulo $3^{28}$, the normalized sum is
   

$$
\sum_q a_q=A_1(1)=0.
$$



3. **Every other $c_s$.**  
   Its denominator valuation is at most $h-28$, so every term is already in $3^{28}$.

All terms of this pairing lie within the original cutoff. In particular, the collision case uses no pole beyond $3H$, and the whole polynomial has degree


$$
H+ML+\deg B_a<K_{\rm phys}.
$$



Thus the non-error term is zero modulo $3^{28}$.

#### The Frobenius error, including the finite partial coefficient

Write the exact difference as


$$
x^H=(Y-1)^N+3^{26}E_1+3^{27}E_2,
$$


with $E_2\in\mathbb Z_3[y]$, $\deg E_2\le H$.

Because $R\equiv1\pmod9$, replacing $R$ by $1$ in the $3^{26}E_1$-term changes the answer only by $3^{28}$. The $3^{27}E_2$-term is also in $3^{28}$: after replacing $R$ by $1$, its degree misses the unit-weight pole.

Only the denominator $H$, of weight $3$, can contribute from $3^{26}E_1B_a$ modulo $3^{28}$. Let


$$
n_*=\frac{H-1}{2}.
$$


Modulo $3$,


$$
E_1=(Z-Z^2)\sum_{q=0}^{N-1}Y^q.
$$


Since $\deg B_a<2D<20Q$, direct coefficient extraction gives


$$
[y^{n_*}]E_1B_a
=[y^{(9Q-1)/2}]B_a.
\tag{6.7}
$$


The potential contribution from $Z^2$ would require the coefficient at


$$
\frac{45Q-1}{2}> \deg B_a,
$$


so it is absent. This explicitly evaluates the finite partial coefficient.

Modulo $3$, the low term $3y^{k_0+a}$ in (6.5) disappears. The remaining term begins at


$$
\frac{9Q+1}{2}+a>\frac{9Q-1}{2}.
$$


Therefore the right side of (6.7) is zero modulo $3$. This proves (6.4).

No logarithmic compression theorem beyond its established range has been invoked.

---

## 7. Evaluation of the overflow return

It remains to prove that the removed part in (5.3) contributes no physical-terminal correction modulo $3^{28}$.

### 7.1 A finite pole reduction for $\Omega_k$ against the tail

For $k=0,1$, set


$$
C_k=(\beta+3y)s_kO_a.
$$


Its support lies in a fixed-width band around $n_*=(H-1)/2$, far from the other relevant macro positions.

Modulo $9$,


$$
x^H\equiv
y^H-3y^{2H/3}+3y^{H/3}-1.
$$


Only the poles with denominators $3H$ and $H$ contribute. Their weights are $1$ and $3$, respectively. The middle macro shifts miss the support of $C_k$. Hence


$$
\boxed{
\mathcal P(\Omega_k,O_a)
\equiv -2[y^{n_*}]C_k\pmod9.
}
\tag{7.1}
$$


These particular pairings lie wholly within the original physical cutoff.

### 7.2 The relevant binomial coefficients, with their payments

Write


$$
c_j=[y^j]x^{10Q}.
$$


The closed valuation identity implies that, for $4Q<j<9Q$, every non-multiple of $Q$ has valuation at least $2$. At multiples of $Q$,


$$
\binom{10Q}{uQ}\equiv\binom{10}{u}\pmod9.
\tag{7.2}
$$


For completeness, (7.2) follows by stripping multiples of $3$: the product of the two units in a block is


$$
(3r-2)(3r-1)\equiv2\pmod9,
$$


so the unit quotient in
$\binom{3a}{3b}/\binom ab$ is $1\pmod9$. Iteration proves (7.2).

Thus, in the open interval $4Q<j<9Q$, the only nonzero coefficients modulo $9$ are


$$
c_{6Q}\equiv3,\qquad c_{7Q}\equiv-3.
\tag{7.3}
$$


Also,


$$
x^{10Q}\equiv y^{10Q}-y^{9Q}-y^Q+1\pmod3.
\tag{7.4}
$$



### 7.3 The complete $k=0$ coefficient cancels modulo $9$

The high and low pieces of $O_a$ are truncated at the respective binomial indices


$$
j>4Q+t,\qquad j>7Q+t.
$$


Using $s_0=\sum_{\ell=0}^{\nu}g_\ell y^{\nu-\ell}$, the entire coefficient in (7.1) is, modulo $9$,


$$
\begin{aligned}
[y^{n_*}]C_0
\equiv{}&
\beta\sum_{\ell=1}^{\nu}g_\ell c_{4Q+t+\ell}\\
&+3\sum_{\ell=2}^{\nu}g_\ell c_{4Q+t-1+\ell}\\
&+3\beta\sum_{\ell=1}^{\nu}g_\ell c_{7Q+t+\ell}.
\end{aligned}
\tag{7.5}
$$


The omitted fourth term has its explicit factor $9$.

The first sum, by (7.3), equals


$$
3\beta g_{2Q-t}-3\beta g_{3Q-t}\pmod9.
$$


The second sum is zero modulo $9$, because its coefficients are multiplied by $3$ and its index range contains none of the nonzero positions in (7.4).

The third sum, by (7.4), equals


$$
3\beta(-g_{2Q-t}+g_{3Q-t})\pmod9.
$$


The indices $2Q-t$ and $3Q-t$ lie inside the actual summation ranges, by the fixed window.

The two displayed contributions cancel exactly. Therefore


$$
\boxed{\mathcal P(\Omega_0,O_a)\in9\mathbb Z_3.}
\tag{7.6}
$$



### 7.4 The $k=1$ coefficient is zero modulo $3$

Modulo $3$, the overflow is


$$
O_a\equiv
-y^{m+5Q-t}+y^{m+6Q-t}.
$$


Both exponents exceed $n_*=m+\nu$, since


$$
5Q-t-\nu=a+1>0.
$$


Consequently


$$
[y^{n_*}](\beta+3y)s_1O_a\equiv0\pmod3,
$$


and


$$
\boxed{\mathcal P(\Omega_1,O_a)\in3\mathbb Z_3.}
\tag{7.7}
$$



### 7.5 Return through the actual inverse row

By (4.7), (7.6), and (7.7),


$$
\mathcal P(\mathscr D,O_a)\in9\mathbb Z_3.
$$


The error term $9W\mathbb Z_3$ in (4.7) is harmless because the original truncated pole functional is integral.

Since $v_3(r_M)=26$,


$$
\boxed{
r_M\,e_{Y_m}^TE_{\mathcal P}^{-1}\mathcal P(W,O_a)
=r_M\mathcal P(\mathscr D,O_a)
\in3^{28}\mathbb Z_3.
}
\tag{7.8}
$$


This is the explicitly paid return of the part removed above $Y_m$.

---

## 8. Evaluation of the actual physical coefficient

The exact pole correction of $\Psi_a$ can now be written using the admissible trial:


$$
\mathcal F_{\mathcal P,a}
=
\widehat V_a
-WE_{\mathcal P}^{-1}\mathcal P(W,\widehat V_a).
\tag{8.1}
$$


This is exact because of (5.4).

The full virtual residual is in $3^{27}M$. By (4.7), modulo $3^{28}$ its contraction with the actual physical row is a unit multiple of
$\mathcal P(\Omega_0,V_a)$, which is zero by (6.4). The overflow contraction is zero by (7.8). Therefore


$$
[y^m]\mathcal F_{\mathcal P,a}
\equiv[y^m]\widehat V_a\pmod{3^{28}}.
\tag{8.2}
$$



Only the top filter coefficient contributes:


$$
[y^m]\widehat V_a
=
r_M\bigl(c_{4Q+t}+3c_{7Q+t}\bigr).
\tag{8.3}
$$



### 8.1 Leading unit of $r_M$

For $N=3^{25}$, the exact Jacobi coefficient formula gives


$$
\frac{r_M}{3^{26}}
\equiv
\frac{(-1)^M2^{2M-1}}
{M\binom{2M}{M}}
\pmod3.
$$


Here $M\equiv1\pmod3$, and Lucas’ theorem gives


$$
\binom{2M}{M}\equiv(-1)^{25}\pmod3.
$$


Since $M\equiv25\pmod2$,


$$
\boxed{\frac{r_M}{3^{26}}\equiv-1\pmod3.}
\tag{8.4}
$$



### 8.2 The terminal binomial factor

If $t>0$, then $t<Q/27$. The established valuation identity gives


$$
v_3\binom{10Q}{4Q+t}\ge6,
\qquad
v_3\binom{10Q}{7Q+t}\ge6.
$$


If $t=0$, (7.2) gives


$$
c_{4Q}\equiv210\equiv3\pmod9,
\qquad
3c_{7Q}\equiv0\pmod9.
$$


Thus


$$
c_{4Q+t}+3c_{7Q+t}
\equiv3\delta_{t,0}\pmod9.
\tag{8.5}
$$



Combining (8.2)–(8.5),


$$
[y^m]\mathcal F_{\mathcal P,a}
\equiv-3^{27}\delta_{a,b/2}\pmod{3^{28}}.
$$


Finally, the accepted pole/complete-core column comparison is in $3^{h-1}W$, and $h-1\ge28$ on the sufficiently large original family. Therefore:

> **New original-index theorem.**
> 

$$
> \boxed{
> [y^m]\mathcal F_a
> \equiv-3^{27}\delta_{a,b/2}\pmod{3^{28}}.
> }
> \tag{8.6}
>
$$



The whole correction vector in (8.1) has only the general $26\to25$ inverse guarantee. The stronger statement (8.6) concerns its **evaluated physical row**, whose additional cancellation has been proved explicitly.

---

## 9. Consequences for the middle-terminal coupling and first $J$-return

The previously paid identity (1.3) now gives


$$
\boxed{\gamma_c=0.}
\tag{9.1}
$$



The Turn 3 bootstrap already gave $\bar t_K=\bar t_J=0$, so the retained producer comparison implies


$$
\bar L_{\rm act}=\bar L_c.
$$


Together with the closed nonterminal strip, (9.1) yields


$$
\boxed{
G^T\bar L_c=G^T\bar L_{\rm act}=0.
}
\tag{9.2}
$$



Because $B_\alpha^{-1}$ is integral in the normalization
$\mathcal R_{\alpha,JJ}=3B_\alpha$, one obtains the stronger, fully paid matrix-return estimate


$$
\boxed{
27G^TL_\alpha B_\alpha^{-1}L_\alpha^TG
\in3^5M
\qquad(\alpha=c,\mathrm{act}).
}
\tag{9.3}
$$


Indeed, each contracted coupling has gained one factor of $3$, so the quadratic return gains two.

The corresponding finite $J$-displacement satisfies


$$
\boxed{
3B_\alpha^{-1}L_\alpha^TG\in9M.
}
\tag{9.4}
$$


The endpoint contraction now obeys


$$
\boxed{
G^Tf_\alpha^{(2)}
\equiv G^Tf_{\alpha,K}\pmod9.
}
\tag{9.5}
$$



These are new evaluated consequences. They do not cancel the complete diagonal channel, nor the subsequent rank-$b$ endpoint and diagonal returns.

---

## 10. Complete forcing and the remaining returned operator

The producer and its complete forcing are unchanged:


$$
Q_{\rm act}=3P_n=Q_c+3^7\mathscr R,
$$




$$
3^7\mathscr R=\sum_{a=0}^{A+1}e_ax^a,
\qquad
e_a=-\frac{(A+1)!}{a!}(t_a+\xi v_a),
$$




$$
t=3nh_{\rm vec}
+(b_{\rm force}+6)e_{n-1}
+\frac{2b_{\rm force}}{n-1}e_{n-2},
\qquad b_{\rm force}=-n-66.
$$


The signed $\xi$, including its paid normalization, remains intact, as do


$$
\mathscr R(-1)
=-\frac{\xi((A+1)!)^2}{3^7},
$$




$$
J^T\varepsilon+\omega
=-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$



The exact first-radical returns remain


$$
\mathcal S_\alpha^{(2)}
=\mathcal R_{\alpha,KK}
-27L_\alpha B_\alpha^{-1}L_\alpha^T,
$$




$$
f_\alpha^{(2)}
=f_{\alpha,K}-3L_\alpha B_\alpha^{-1}f_{\alpha,J},
$$




$$
\lambda_\alpha^{(2)}
=\lambda_\alpha-\frac13f_{\alpha,J}^TB_\alpha^{-1}f_{\alpha,J}.
\tag{10.1}
$$


Their inverse cost is $3^{-1}$.

The new theorem evaluates the contracted matrix return more deeply and removes the $\gamma_c$-term from (9.5). It does not authorize deletion of (10.1) as exact formulas.

The second prefix lift is still present:


$$
-\frac{G_c(\mathcal F,\mathcal F)}{3^{26}}
=
G^T\mathcal R_{c,KK}G+81Z^T\mathsf AZ.
\tag{10.2}
$$


Using (9.3), its next core digit is now localized as


$$
\boxed{
\frac{G^T\mathcal S_c^{(2)}G}{81}
\equiv
-\frac{G_c(\mathcal F,\mathcal F)}{3^{30}}
-Z^T\mathsf AZ
\pmod3.
}
\tag{10.3}
$$


The divisions in (10.3) are paid by the established whole pairing in $3^{30}$. Its right side is **not evaluated here**.

The rank-$b$ returns remain exactly


$$
T_{\rm new}=T_{RR}-81M_b^TA_b^{-1}M_b,
$$




$$
f_{\rm new}=f_R-3M_b^TA_b^{-1}f_b,
$$




$$
\lambda_{\rm new}
=\lambda^{(2)}-\frac19f_b^TA_b^{-1}f_b.
\tag{10.4}
$$


Their inverse cost is $3^{-2}$.

Thus the next operator still requires the second prefix, producer, rank-$b$, endpoint, and diagonal contributions. The new $J$-return estimate does not turn that operator into a core-only matrix.

---

## 11. Exact remaining local bottleneck

After all retained returns and actual endpoint adaptation,


$$
T=
\begin{pmatrix}a&z^T\\z&C\end{pmatrix}\in81M,
\qquad
\lambda=\eta/3,\quad \eta\in\mathbb Z_3^\times.
$$


Write


$$
a=81\alpha,\qquad z=81w,\qquad C=81B,
$$




$$
u=1-\lambda a=1-27\eta\alpha\in1+27\mathbb Z_3.
$$


The already proved paid two-coordinate elimination gives


$$
C^\sharp
=C+\frac{\lambda}{u}zz^T
=81B^\sharp,
$$




$$
\boxed{
B^\sharp=B+\frac{27\eta}{u}ww^T.
}
\tag{11.1}
$$


This is the **fully returned** object.

A concrete next lemma is:

> **Fully returned directional lemma.**  
> On the same infinite original subwindow, prove that the actual $B^\sharp$ is nonsingular and construct
> 

$$
> B^\sharp v=w,\qquad v\in3^{-1}\mathbb Z_3^{b/2},
>
$$


> with the second prefix, producer, endpoint, diagonal, and rank-$b$ terms in (10.2)–(10.4) retained.

Its conditional implication remains rigorous. If such $v$ exists, then


$$
\epsilon=1-\frac{27\eta}{u}w^Tv\in1+9\mathbb Z_3,
$$


and Sherman–Morrison gives


$$
B^{-1}w=v/\epsilon\in3^{-1}\mathbb Z_3^{b/2}.
$$


If the resulting Schur scalar is nonzero, this supplies a fixed relative gain of at least $3$; an integral directional solution supplies at least $4$.

Neither is a growing saving. The previously exhibited obstruction to inferring a favorable inverse merely from $T\in81M$ and $v_3(\lambda)=-1$ remains applicable to that bare inference.

The present coefficient theorem closes the $\gamma_c$ obligation. It does not close the directional lemma or the growth obligation.

---

## 12. Division, boundary, and arithmetic ledgers

### 12.1 New and retained payments

| Operation | Payment or exact scope |
|---|---|
| Original poles | $3^h$, with cutoff $4n-3$ |
| Factorial removal | Only the established local pole/complete congruence |
| Full Jacobi/Christoffel interface | All $\ell_r,h_r,p_r(z),H_r$ factors retained |
| Lacunary Schur/Selberg interface | Full beta products, LR/Pieri sum, $C_J(z)$, and $z$-powers retained |
| $p=25$ coefficient-adapted dual | Actual $W$-polynomials of degree below $m$ |
| Dual normalization | Division by the proved units $\beta\mathfrak t_{25}$ |
| Three-column residual | $3^3\to3^2$ after the one-digit inverse loss |
| $p=26$ full virtual residual | Evaluated in $3^{27}M$; not an admissible column by itself |
| Physical truncation | Only the top filter term removed; $v_3(r_M)=26$ |
| Collision $2s+1=27Q$ | Complete finite $q=0$ Jacobi moment, evaluated as zero |
| Remaining $9Q$-denominator layer | $3^{27}$ times a unit-denominator sum, evaluated as zero modulo $3$ |
| Frobenius correction | $3^{26}$, then the extra pole-weight digit and an evaluated coefficient zero |
| Overflow return | Explicitly evaluated in $3^{28}$ |
| Actual projection | General $26\to25$ loss retained; only the physical row gains the proved cancellation |
| Terminal coefficient observation | $r_M/3^{26}\equiv-1$, binomial factor $3\delta\pmod9$ |
| Complete-core transfer | Error $3^{h-1}$, sufficient for modulus $3^{28}$ |
| Middle-terminal observation | Whole coefficient divided by $3^{27}$, now evaluated |
| First-radical inverse | $3^{-1}$; contracted matrix return now in $3^5M$ |
| Rank-$b$ inverse | $3^{-2}$, still retained |
| Eventual $B^\sharp$ solve | Open |
| Complete forward resonance | Genuine $3^h$ divisor retained |

No new content division has been made.

The complete moment recurrence is still


$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\qquad0\le t\le2n-2.
$$


Its forward resonance at


$$
t_*=\frac{3^h-5}{2}
$$


is not removed by the new filter. Its highest moment remains physical because


$$
H-4D+5\ge0.
$$



### 12.2 Actual contents, least clearer, all-prime gcd, and whole error

All helper constructions above are local certificates. Their rational coefficients do not replace the actual original column contents or the actual least simultaneous clearer $\ell_{\rm clr}$.

Retain the original distinguished integers


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the gcd over **all primes**


$$
\boxed{g_\ell=\gcd(|A_\ell|,|B_\ell|).}
$$


For $B_\ell\ne0$, the actual primitive denominator and numerator are


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole evaluated error remains


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{12.1}
$$



An irrationality proof still requires, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\boxed{
\log g_\ell-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|
\longrightarrow+\infty.
}
\tag{12.2}
$$


The new fixed-depth coefficient evaluation does not prove (12.2).

---

## 13. Bounded exact-arithmetic receipt, if desired

No arithmetic calculation is outstanding in the analytic proof above. No original dense computation is proposed, and the supplied auxiliary kernel receipt is not reopened.

A coordinator may optionally record the following small certificate for the new overflow constants.

### Inputs

- the polynomial $(Z-1)^{10}$;
- modulus $9$;
- integers $0,\ldots,10$.

### Expected verifiable output

The coefficient vector in increasing degree is


$$
(1,-10,45,-120,210,-252,210,-120,45,-10,1),
$$


and modulo $9$,


$$
\boxed{(1,8,0,6,3,0,3,6,0,8,1).}
$$


Modulo $3$,


$$
\boxed{(Z-1)^{10}=Z^{10}-Z^9-Z+1.}
$$



The associated scaling identity is proved analytically by


$$
(3r-2)(3r-1)=9r(r-1)+2\equiv2\pmod9;
$$


no large factorial is required.

These bounded outputs certify only the displayed universal constants. The original-index theorem follows from the valuation, finite-boundary, inverse-payment, and tail-return proofs—not from extrapolation of a finite auxiliary computation.

---

## 14. Proof status and conclusion

| Statement | Status |
|---|---|
| Exact full Jacobi/Christoffel inverse | Independently validated |
| Upper-triangular change for the actual omitted window | Independently validated |
| Physical terminal row and denominator $H_m+\theta$ | Independently validated; no valuation inferred from positivity |
| Single-Schur beta identity | Direct proof validated |
| Actual lacunary partition and full linear pole factor | Independently validated |
| Normalized LR/Pieri–Selberg product-sum | Exact identity validated; arithmetic cancellation not inferred |
| Supplied auxiliary receipt | Closed finite identity only; not recomputed or used as an original index |
| Actual physical inverse row modulo $9$ | **New proved coefficient-adapted certificate** |
| $p=26$ macro collision and physical truncation | **Explicitly accounted for** |
| Overflow return modulo $3^{28}$ | **Evaluated: zero** |
| $[y^m]\mathcal F_a\pmod{3^{28}}$ | **Evaluated: $-3^{27}\delta_{a,b/2}$** |
| $\gamma_c$ | **Evaluated: zero** |
| Contracted first $J$-matrix return | **Strengthened to $3^5M$** |
| Fully returned $B^\sharp$ directional solve | Open |
| Growing relative-cofactor saving | Open |
| All-prime primitive whole-error decay | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

### Final conclusion

The requested coefficient obligation is closed:


$$
\boxed{
[y^m]\mathcal F_a
\equiv-3^{27}\delta_{a,b/2}\pmod{3^{28}},
\qquad
\gamma_c=0.
}
$$



The proof uses the exceptional Jacobi moment to construct an actual finite-$W$ dual to $Y_m$. At the next filter scale it explicitly handles the denominator collision, the finite macro sums, the terms above $Y_m$, their returned correction, and the inverse’s one-digit loss.

The exact remaining local bottleneck is the **fully returned** $B^\sharp$ directional solve, now with the middle-terminal residue evaluated but with the second prefix, producer, endpoint, diagonal, and rank-$b$ returns still present. Beyond that lies the essential growing arithmetic improvement and the same-index comparison of the actual all-prime gcd with the nonzero whole complete error.

Accordingly,


$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ is obtained.}}
$$


