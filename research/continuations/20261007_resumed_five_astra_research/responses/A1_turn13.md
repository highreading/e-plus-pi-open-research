> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Endpoint-controlled elimination beyond the second radical

## Abstract

The supplied work does not establish that $e+\pi$ is rational or irrational. The precision-$29$ second-radical calculation in A1 turn12 remains subject to the stated independent review of its original-object hypotheses. The coordinator’s auxiliary certificate supports its finite coefficient algebra, not those hypotheses or an infinite-index conclusion.

This report proves an obstruction to one precise proposed continuation:

> **The rational-Hankel second digit, its full radical, a primitive endpoint on that radical, and the complete diagonal valuation $-1$ do not, by themselves, imply any bound on the relative cofactor valuation.**

Even fixing the endpoint and the full diagonal exactly, completions of the displayed matrix digit can have


$$
v_3D_0-v_3D_1
$$


arbitrarily positive or arbitrarily negative. Both cofactors can remain nonzero. These completions are not asserted to be original matrices; they disprove an inference from the displayed local data alone.

There is nevertheless a useful exact endpoint-controlled reduction. Granting the proposed second-layer statement, one can choose an actual endpoint-adapted integral basis, eliminate its rank-$b$ block with precisely a $3^{-2}$ inverse, and preserve the complete diagonal exactly. The remaining matrix $T$ lies in $27M$, has endpoint $e_0$, and has complete diagonal $\lambda$ with $v_3(\lambda)=-1$. Writing


$$
T=\begin{pmatrix}a&z^T\\ z&C\end{pmatrix},
$$


the bordered cofactor is exactly


$$
\boxed{
D_1=(1-\lambda a)
\det\!\left(C+\frac{\lambda}{1-\lambda a}zz^T\right)
}
$$


after removal of the common eliminated determinant factor. The perturbation of $C$ lies in $3^5M$, but this does **not** ensure determinant stability: an inverse direction of valuation $-2$ can already cause arbitrarily deep cancellation.

A concrete alternative scalar obligation is therefore identified: control the **actual directional solve**


$$
Cw=z,
$$


using the complete source, rather than extrapolating the characteristic-$3$ rational denominator. An exact complete-source moment recurrence and its finite determinant transfer are derived below to specify that route without replacing the factorial functional by a pole-only model.

---

## 1. Original objects and the scope of this report

Throughout, the original domain is retained:


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1,\qquad A=4^j-1=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


and


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



With $x=y-1$, the finite coordinates remain


$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_a=y^a\quad(d\le a\le m),
\qquad
\nu=\frac D2-1,\qquad d=D+\nu.
$$


The physical HIGH terminal is $Y_m$.

The functional is the complete finite functional


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad \mathfrak f(y^t)=(2t)!.
$$


Its denominator cutoff is


$$
2v+1\le 4H-4D+5=4n-3.
$$



The complete core is


$$
G_c(f,g)=\mathcal M(Q_cfg),\qquad
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A.
$$


The actual polynomial is


$$
Q_{\rm act}=3P_n=Q_c+3^7\mathscr R.
$$



The distinction between this complete core and a pole-only reference is essential. Relative to the complete core,


$$
G_{\rm act}-G_c=3^7\mathcal M(\mathscr R\,\cdot\,\cdot).
$$


A pole-only reference would leave the additional core factorial form in the perturbation. Nothing below removes it.

### 1.1 Results reused at their accepted scope

The independently accepted producer statement is


$$
\boxed{
\frac{S_{\rm act}-S_c}{3^{28}}
\equiv-\kappa(\delta t^T+t\delta^T)\pmod3,
\qquad
t_i=\frac{[y^m]F_i}{3^{20}},
}
$$


where $F_i$ are the exact complete-core corrected columns and


$$
\delta_i=\mathbf 1_{\{i=\nu-1\}}.
$$


The vector $t$ is not assumed to vanish.

Also reused are the finite corrected-column definitions, the original inverse bounds, and the complete first two jets at their stated sufficiently-large original scope. No old producer, dense original matrix, or closed rank calculation is recomputed.

### 1.2 The pending second-layer hypothesis

Choose a fixed open original subwindow contained in


$$
\frac1{10}<\frac{N_0}{P_0}<\frac{19}{180},
$$


where


$$
P_0=243P,\qquad N_0=243r,\qquad
P=3^{h-32},\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$


and retain


$$
4^j=243(3^{26}-1)P-243r+1.
$$



Set


$$
Q=\frac{P_0}{9},\qquad b=Q-N_0,\qquad
\ell=\frac{3b}{2}+1,\qquad E=\frac{Q-3}{2}.
$$



For clarity, denote by **H2** the following original-object conclusion proposed in A1 turn12:



$$
\mathcal S^{(2)}\in9M_\ell(\mathbb Z_3),\qquad
\overline{\mathcal S^{(2)}/9}_{uv}
=[y^{E-u-v}](1-y)^{-b},
$$




$$
\ker\overline{\mathcal S^{(2)}/9}
=(y-1)^b\mathbb F_3[y]_{\le b/2},
$$


together with the exact endpoint and complete diagonal satisfying


$$
\overline{f^{(2)}_u}=(-1)^{R_*+u},
\qquad
v_3(\lambda^{(2)})=-1.
$$



The characteristic-$3$ algebra of this displayed operator is supported by the supplied certificate. Its identification with the complete original reduction is still under the specified independent audit. Applications below to $\mathcal S^{(2)}$ are explicitly conditional on H2.

The obstruction proved below is stronger in one respect: **even granting H2 in full, the proposed infinite conclusion does not follow from it.**

---

## 2. An endpoint-adapted elimination that preserves the complete diagonal

The following is an exact finite-matrix result, not an asymptotic assertion.

### Theorem 2.1 — Endpoint-adapted elimination

Let $M$ be a symmetric $s\times s$ matrix over $\mathbb Z_3$, let $f\in\mathbb Z_3^s$, and suppose


$$
M\in3^kM_s(\mathbb Z_3),\qquad k\ge1.
$$


Let


$$
H=\overline{M/3^k}
$$


have rank $b$, with radical $N$. Assume that the reduction of $f$ is nonzero on $N$.

Then there is a basis over $\mathbb Z_3$, using only unit divisions, in which


$$
f=(0_b,1,0,\ldots,0)^T
$$


and


$$
M=
\begin{pmatrix}
A&X\\
X^T&V
\end{pmatrix},
$$


with


$$
A=3^kA_0,\qquad A_0\in\operatorname{GL}_b(\mathbb Z_3),
$$




$$
X\in3^{k+1}M,\qquad V\in3^{k+1}M.
$$



Eliminating $A$ gives


$$
T=V-X^TA^{-1}X\in3^{k+1}M,
$$


where the inverse payment is exactly


$$
A^{-1}=3^{-k}A_0^{-1}.
$$


The correction satisfies


$$
X^TA^{-1}X\in3^{k+2}M.
$$



For a bordered pair with complete diagonal $\lambda$, this elimination leaves both the retained endpoint $e_0$ and the complete diagonal $\lambda$ unchanged.

#### Proof

Choose $\bar v\in N$ with $\bar f^T\bar v=1$. Lift it to $v_0\in\mathbb Z_3^s$, and put


$$
v=\frac{v_0}{f^Tv_0}.
$$


The denominator is a unit.

Choose any complement $\bar B$ to $N$. Replace each of its vectors $\bar u$ by


$$
\bar u-(\bar f^T\bar u)\bar v.
$$


This puts the complement in $\ker\bar f$, without changing its pairings under $H$, because $\bar v\in N$. Hence the restriction of $H$ to that complement remains nondegenerate.

Lift its basis and a basis of $N\cap\ker\bar f$. For every such lift $u$, replace it by


$$
u-v(f^Tu).
$$


This annihilates the **exact** endpoint. It preserves the required reduction modulo $3$.

The resulting basis is invertible over $\mathbb Z_3$. Its first $b$ coordinates form a nondegenerate complement; its remaining coordinates reduce to $N$. Therefore


$$
A/3^k\in\operatorname{GL}_b(\mathbb Z_3),\qquad
X,V\in3^{k+1}M.
$$


The inverse and correction bounds follow:


$$
v_3(X^TA^{-1}X)\ge(k+1)+(k+1)-k=k+2.
$$



The endpoint on the eliminated coordinates is exactly zero. Consequently the endpoint Schur correction and the diagonal Schur correction are exactly zero, not merely zero modulo a power of $3$. ∎

### 2.2 Application to the proposed second radical

Under H2, take $k=2$, $s=\ell$, and $M=\mathcal S^{(2)}$. The remaining dimension is


$$
r=\ell-b=\frac b2+1.
$$



An explicit choice of radical lifts is


$$
r_0=(y-1)^b,
$$


and


$$
g_a=(y+1)(y-1)^b y^a,\qquad 0\le a<\frac b2.
$$


Every degree is at most


$$
b+\frac b2=\ell-1,
$$


so these are vectors in the actual finite $K$-space, not exterior coordinates.

The endpoint of $r_0$ is a unit modulo $3$. Normalize it using that unit, and correct the $g_a$ by multiples of the normalized vector to annihilate the exact $f^{(2)}$.

For a complement one may start with


$$
1,y,\ldots,y^{b-1}
$$


and perform the same exact endpoint correction. These vectors are independent modulo the radical because every nonzero radical polynomial has degree at least $b$.

Thus the new elimination has the precise form


$$
A=9A_0,\qquad A_0\in\operatorname{GL}_b(\mathbb Z_3),
$$




$$
X\in27M,\qquad V\in27M,
$$




$$
\boxed{
T=V-\frac19X^TA_0^{-1}X\in27M.
}
$$


The new matrix correction belongs to $81M$.

Most importantly,


$$
\boxed{
f_T=e_0,\qquad \lambda_T=\lambda^{(2)}
}
$$


exactly. In this basis the valuation $-1$ diagonal does not acquire an uncomputed correction from the rank-$b$ elimination.

This improves the bookkeeping of an iteration. It does not establish that the endpoint survives every later radical.

---

## 3. The complete producer returns at the next unprotected digit

The accepted rank-two producer correction vanishes on $K\times K$ at its displayed digit. It must not therefore be deleted from subsequent reductions.

Write the exact first-radical reduction in the finite partition $K\sqcup J$:


$$
\mathcal R=
\begin{pmatrix}
\mathcal R_{KK}&\mathcal R_{KJ}\\
\mathcal R_{JK}&\mathcal R_{JJ}
\end{pmatrix},
$$


with


$$
\mathcal R_{JJ}=3B,\qquad B\in\operatorname{GL}_{|J|}(\mathbb Z_3),
\qquad
\mathcal R_{KJ}=9L.
$$


Then the exact formulas are


$$
\boxed{
\mathcal S^{(2)}=\mathcal R_{KK}-27LB^{-1}L^T,
}
\tag{3.1}
$$




$$
\boxed{
f^{(2)}=f_K-3LB^{-1}f_J,
}
\tag{3.2}
$$




$$
\boxed{
\lambda^{(2)}
=\lambda-\frac13f_J^TB^{-1}f_J.
}
\tag{3.3}
$$



These retain the complete matrix return, endpoint lift, and diagonal.

### 3.1 The first returning rank-two contribution

In the normalization $U=-S_{\rm act}/3^{26}$, the accepted producer correction has sign


$$
U_{\rm act}-U_c
\equiv9\kappa(\delta t^T+t\delta^T)\pmod{27}.
$$



The terminal vector has $\delta_K=0$ but $\delta_J\ne0$. After the unit-prefix elimination, its leading effect on the cross block is therefore of the form


$$
\overline L_{\rm act}
=
\overline L_c+\bar\kappa\,\bar t_K\bar\delta_J^T.
\tag{3.4}
$$


Prefix corrections to the effective $t_K$ are divisible by $3$, so they do not alter this displayed reduction.

Substitution into the complete return in (3.1) produces, at order $27$, all of


$$
-\bar\kappa\,\bar t_K\bar\delta_J^T\bar B^{-1}\bar L_c^T,
$$




$$
-\bar\kappa\,\bar L_c\bar B^{-1}\bar\delta_J\bar t_K^T,
$$


and


$$
-\bar\kappa^2
\bigl(\bar\delta_J^T\bar B^{-1}\bar\delta_J\bigr)
\bar t_K\bar t_K^T.
\tag{3.5}
$$


There is also the next, not yet evaluated, direct actual contribution in $\mathcal R_{KK}$. Formula (3.5) is not a replacement for it.

Thus the first surviving producer return need not be linear in the displayed rank-two correction: the quadratic term in $t_K$ is at the same next Schur order.

### 3.2 Exact next-radical formula

Let $G$ be the integral matrix with columns


$$
(y-1)^by^a,\qquad 0\le a\le b/2.
$$


Under H2,


$$
G^T\mathcal R_{KK}G\in27M.
$$


Equation (3.1) gives the paid next digit


$$
\boxed{
\frac{G^T\mathcal S^{(2)}G}{27}
=
\frac{G^T\mathcal R_{KK}G}{27}
-
G^TLB^{-1}L^TG.
}
\tag{3.6}
$$



This identity specifies the actual return that any next-digit calculation must include. The new rank-$b$ elimination of §2 changes this restriction only in $81M$, so it does not alter its normalized digit modulo $3$.

But the first term in (3.6) is not evaluated by the supplied precision-$29$ result. Therefore (3.6) is an exact obligation, not a completed next-digit calculation.

### 3.3 The original forcing has not changed

The source defining these terms remains


$$
3P_n-Q_c
=\sum_{a=0}^{A+1}e_ax^a
=3^7\mathscr R,
$$




$$
e_a=-\frac{(A+1)!}{a!}(t_a+\xi v_a),
$$


with


$$
t=3nh_{\rm vec}
+(b_{\rm force}+6)e_{n-1}
+\frac{2b_{\rm force}}{n-1}e_{n-2},
\qquad b_{\rm force}=-n-66.
$$


The signed scalar $\xi$, including its previously paid common division, is retained.

So is the full return


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$


No exponential boundary charge, logarithmic force, physical-terminal term, or finite return has been discarded.

---

## 4. Exact endpoint reduction and a sharp determinant-stability threshold

Remove the common determinant factors from the previously eliminated blocks. Under H2 and §2, the retained pair is represented by


$$
T=
\begin{pmatrix}
a&z^T\\
z&C
\end{pmatrix}\in27M_r(\mathbb Z_3),
\qquad f_T=e_0,
\qquad v_3(\lambda)=-1.
$$


Define


$$
D_0=\det T,\qquad
D_1=e_0^T\operatorname{adj}(T)e_0-\lambda\det T.
$$



Since the endpoint cofactor is $\det C$,


$$
D_1=\det C-\lambda\det T.
\tag{4.1}
$$



### Theorem 4.1 — Exact endpoint perturbation identity

Put


$$
d=1-\lambda a.
$$


Then $d\in\mathbb Z_3^\times$, and


$$
\boxed{
D_1=d\det\left(C+\frac{\lambda}{d}zz^T\right).
}
\tag{4.2}
$$


Moreover,


$$
\frac{\lambda}{d}zz^T\in3^5M.
\tag{4.3}
$$



#### Proof

Because $a\in27\mathbb Z_3$ and $v_3(\lambda)=-1$,


$$
\lambda a\in9\mathbb Z_3,
$$


so $d$ is a unit.

The determinant identity


$$
\det T=a\det C-z^T\operatorname{adj}(C)z
$$


holds even if $C$ is singular. Hence


$$
D_1=d\det C+\lambda z^T\operatorname{adj}(C)z.
$$


The rank-one determinant formula gives (4.2), also without requiring $C^{-1}$.

Finally,


$$
v_3\!\left(\frac{\lambda}{d}z_iz_j\right)\ge-1+3+3=5.
$$


∎

### 4.2 Every new inverse payment

One may realize (4.2) by two scalar pivots:

1. The complete diagonal pivot $\lambda$ has inverse of valuation $+1$, so this is not a denominator loss.
2. The resulting endpoint pivot is
   

$$
a-\lambda^{-1},
$$


   of exact valuation $1$, because $a\in27\mathbb Z_3$ and $v_3(\lambda^{-1})=1$. Its inverse costs $3^{-1}$.

Together with earlier reductions, the bills are:

| Operation | Inverse valuation bound |
|---|---:|
| Original LOW/HIGH block | $-1$, at the supplied scope |
| Original unit prefix | $0$ |
| First-radical nondegenerate block | $-1$ |
| New rank-$b$ block | $-2$ |
| Exact endpoint normalization | $0$ |
| Complete diagonal pivot $\lambda$ | $+1$ |
| Subsequent endpoint pivot $a-\lambda^{-1}$ | $-1$ |

No inverse of $C$ has been assumed in (4.2).

### 4.3 A concrete directional noncancellation lemma

The $3^5$ perturbation in (4.3) is two digits deeper than $C\in27M$. That is useful only if the relevant inverse direction is controlled.

**Lemma 4.2.** Suppose $C$ is invertible and its actual solution


$$
w=C^{-1}z
$$


satisfies


$$
w\in3^{-1}\mathbb Z_3^{r-1}.
$$


Then


$$
v_3D_1=v_3\det C.
$$


If $D_0\ne0$, then


$$
\boxed{
v_3D_0-v_3D_1
=v_3(a-z^Tw)\ge2.
}
\tag{4.4}
$$


If $w$ is integral, the lower bound improves to $3$.

**Proof.** Since $z\in27\mathbb Z_3^{r-1}$,


$$
z^Tw\in9\mathbb Z_3.
$$


Thus


$$
d+\lambda z^Tw\equiv1\pmod3,
$$


and


$$
D_1=\det C\,(d+\lambda z^Tw)
$$


has exactly the valuation of $\det C$. Also


$$
D_0=\det C\,(a-z^Tw).
$$


The stated bounds follow. ∎

This is a genuine conditional noncancellation result. Its hypothesis is an **actual directional inverse bound**, not a consequence of the rational-Hankel leading digit.

---

## 5. A rigorous obstruction to a precision-growing conclusion from the displayed data

The next theorem explains why the missing directional bound cannot be supplied by the leading rational denominator alone.

### Theorem 5.1 — Unbounded relative cofactors among indistinguishable leading completions

Fix an exact $\lambda\in\mathbb Q_3$ with


$$
v_3(\lambda)=-1,
$$


and let $r\ge2$.

Among symmetric matrices $T\in27M_r(\mathbb Z_3)$, all with exact endpoint $e_0$ and exact complete diagonal $\lambda$, the quantity


$$
v_3D_0-v_3D_1
$$


is unbounded above and below, even when $D_0D_1\ne0$.

Consequently, fixing the second-layer leading form, its radical, the endpoint on that radical, and the exact complete diagonal does not bound this relative valuation.

#### Proof

It suffices to use a two-dimensional residual and append diagonal $27$-blocks. Appended blocks contribute the same determinant factor to both cofactors.

Write $\lambda=u/3$, with $u\in\mathbb Z_3^\times$.

**Arbitrarily positive values.** For $M\ge0$, take


$$
T_M=27
\begin{pmatrix}
3^M&0\\
0&1
\end{pmatrix}.
$$


Then


$$
D_0=3^{6+M},
$$


and


$$
D_1=27-\frac u3\,3^{6+M}
=27(1-u3^{M+2}).
$$


The last factor is a unit, so


$$
v_3D_0-v_3D_1=M+3.
$$



**Arbitrarily negative values.** For $N\ge3$, take


$$
T_N=27
\begin{pmatrix}
0&1\\
1&-9u+3^N
\end{pmatrix}.
$$


Then


$$
D_0=-3^6,
$$


while


$$
D_1=27(-9u+3^N)+\frac u3\,3^6
=3^{N+3}.
$$


Thus


$$
v_3D_0-v_3D_1=3-N.
$$



Both determinants are nonzero in both constructions. ∎

### 5.2 Matching the displayed second-layer form

Let $H$, $f$, and $\lambda$ be the data in H2. Apply the endpoint-adapted basis construction of §2. In that basis, choose the rank-$b$ block to be any lift of the required nonsingular block, multiplied by $9$; set its cross block with the radical to zero; and choose either residual family above.

After transforming back, every resulting matrix has


$$
M/9\equiv H\pmod3,
$$


the same exact endpoint $f$, and the same exact $\lambda$. The same finite dimension and coordinate boundaries are used.

These are **not** asserted to satisfy the complete original moment equations or producer identity. Their purpose is precise:

> They disprove a universal elimination theorem whose hypotheses consist only of the displayed rational-Hankel digit, its radical, the endpoint, and the diagonal valuation—even if the endpoint and diagonal are fixed exactly.

A theorem on the actual original matrices must use additional complete-source information that excludes these completions.

### 5.3 Sharpness of the directional threshold

In the negative family,


$$
C=27(-9u+3^N),\qquad z=27.
$$


For $N>2$,


$$
v_3(C)=5,\qquad v_3(C^{-1}z)=-2.
$$


Thus failure by just one digit of the hypothesis


$$
C^{-1}z\in3^{-1}\mathbb Z_3
$$


permits arbitrarily deep cancellation.

This is the precise arithmetic obstruction behind the phrase “the $3^5$ perturbation is small.” Small entries do not imply a small determinant perturbation without a paid inverse-direction estimate.

---

## 6. Why the existing support-separation mechanism cannot grow indefinitely

There is also a separate obstruction to extending the existing producer separation argument to unbounded precision without a new support theorem.

On the retained original subwindow,


$$
P_0=3^{h-27},\qquad D=P_0(1+\rho),
\qquad \rho=\frac{N_0}{P_0}.
$$


Therefore


$$
\frac HD=\frac{3^{26}}{1+\rho}.
$$



A precision-$p$ grid of the type used in the supplied producer estimate has


$$
\Lambda_p=\frac H{3^{p-1}},
\qquad
\frac{\Lambda_p}{D}=\frac{3^{27-p}}{1+\rho}.
\tag{6.1}
$$



The retained precision-$20$ representative gives the product support width $21D$. The half-grid exclusion requires


$$
21D<\frac{\Lambda_p-1}{2}.
\tag{6.2}
$$


Ignoring the harmless $-1$, a necessary condition is


$$
42(1+\rho)<3^{27-p}.
$$



At $p=23$, the right side is $81$, so this particular margin still holds. At $p=24$, it is $27$, whereas


$$
42(1+\rho)>46.
$$


Thus the same support-envelope proof cannot establish precision $24$, much less precision tending to infinity.

Even an envelope of width only $D$ fails by $p=27$, since then


$$
\Lambda_p/D=(1+\rho)^{-1}<1.
$$



This does not prove a moment is nonzero at those precisions. It proves that the stated grid-and-width exclusion mechanism has exhausted its certification range. A continuation would need new exact cancellations or a substantially different support description.

In addition:

* corrected-column support is presently supplied only through precision $20$;
* the direct higher producer coefficients in (3.6) are not evaluated;
* returns such as (3.5) enter the first unprotected digit;
* future inverse accuracy must be paid.

For example, if


$$
A^{-1}\in3^{-k}M,\qquad
A'-A\in3^NM,\qquad N>k,
$$


then


$$
A'^{-1}-A^{-1}
=-A^{-1}(A'-A)A'^{-1}\in3^{N-2k}M.
$$


An inverse congruence cannot be propagated at its input precision without this loss.

---

## 7. A different scalar strategy using the complete source

The obstruction above does not show that the actual relative cofactor is uncontrolled. It identifies what must now be used: the complete moment equations.

Here is an exact scalar source identity with the original finite boundary.

### 7.1 Complete moments, including the factorial part

Define


$$
\mu_t=\mathcal M(y^t),\qquad 0\le t\le2n-1.
$$


Then


$$
\mu_0=-\frac{3^h}{4},
$$


and, for $0\le t\le2n-2$,


$$
\boxed{
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr).
}
\tag{7.1}
$$



#### Derivation

The polynomial identity


$$
\frac{y^{t+1}-(-1)^{t+1}}{y+1}
+
\frac{y^t-(-1)^t}{y+1}
=y^t
$$


shows that the sum of the two pole contributions is $3^h/(2t+1)$. The factorial contribution is exactly the second term in (7.1).

The largest required pole occurs at $t=2n-2$, with denominator $4n-3$, precisely the original cutoff. No infinite extension of the functional is being used.

Every division by $2t+1$ is explicit. On this range,


$$
v_3(2t+1)\le h,
$$


so the prefactor $3^h$ pays it. Division by $4$ is a ternary unit division.

### 7.2 A division-free polynomial recurrence

Put


$$
q_t=(2t+2)(2t+1)
$$


and


$$
L_t=(2t+3)\mu_{t+2}+2\mu_{t+1}-(2t+1)\mu_t.
$$


Directly from (7.1),


$$
L_t=-\frac{3^h}{4}C_t(2t)!,
$$


where


$$
C_t=(2t+3)q_tq_{t+1}+2q_t-(2t+1).
$$


Hence


$$
\boxed{
C_tL_{t+1}-q_tC_{t+1}L_t=0,
\qquad 0\le t\le2n-4.
}
\tag{7.2}
$$



This is a complete-source polynomial recurrence. It includes the factorial component rather than invoking a Jacobi or beta replacement. Equation (7.2) itself performs no division. Any algorithm that solves it for its highest-index moment must separately pay the resulting coefficient divisor.

### 7.3 Exact transfer to the two distinguished complete determinants

Write the actual polynomial in monomials,


$$
Q_{\rm act}(y)=\sum_{s=0}^{n}q_sy^s,
$$


where the coefficients are those defined by the full producer, including its force and returns. Put


$$
\zeta_t=\mathcal M(Q_{\rm act}y^t)
=\sum_{s=0}^{n}q_s\mu_{s+t},
\qquad 0\le t\le2m.
$$


The largest moment index is


$$
n+2m=2n-1,
$$


so the finite recurrence range is sufficient.

Define the complete monomial Gram determinant


$$
\Delta=\det(\zeta_{i+j})_{0\le i,j\le m},
$$


and the complete endpoint-kernel determinant


$$
K=
\det\bigl(
\zeta_{i+j+2}+2\zeta_{i+j+1}+\zeta_{i+j}
\bigr)_{0\le i,j<m}.
\tag{7.3}
$$



The latter is the Gram determinant on the exact finite endpoint kernel


$$
(y+1)\mathbb Q[y]_{\le m-1}.
$$


It is not a projected Jacobi channel.

Let $E_{\rm act}$ be the original eliminated LOW/HIGH block, and let


$$
U=-S_{\rm act}/3^{26}.
$$


With the original distinguished pair


$$
\mathcal D_0=\det U,\qquad
\mathcal D_1=e_{\rm act}^T\operatorname{adj}(U)e_{\rm act}
-3^{26}d_{\rm act}\det U,
$$


one has the exact identities


$$
\boxed{
\Delta
=\det(E_{\rm act})(-3^{26})^\nu\mathcal D_0,
}
\tag{7.4}
$$




$$
\boxed{
K
=\det(E_{\rm act})(-3^{26})^{\nu-1}\mathcal D_1.
}
\tag{7.5}
$$



To check (7.5), first use the unimodular polynomial basis


$$
1,\ (y+1),\ y(y+1),\ldots,y^{m-1}(y+1).
$$


Evaluation at $-1$ is its first coordinate, so its endpoint cofactor is exactly (7.3). Then apply the exact LOW/HIGH Schur decomposition, retaining


$$
d_{\rm act}=w^TE_{\rm act}^{-1}w.
$$


The sign and factor in (7.5) follow from


$$
\operatorname{adj}(-3^{26}U)
=(-3^{26})^{\nu-1}\operatorname{adj}(U).
$$



Consequently, whenever the quantities are nonzero,


$$
\boxed{
v_3\mathcal D_0-v_3\mathcal D_1
=v_3\Delta-v_3K-26.
}
\tag{7.6}
$$



The determinant transfer is standard finite linear algebra; the relevant source-specific input here is the complete recurrence (7.1)–(7.2), the actual $q_s$, and the exact boundary $2n-1$.

### 7.4 Concrete follow-on lemma

A useful next original-object theorem would be:

> **Complete directional inverse lemma.** On a specified infinite original subfamily in the retained fixed subwindow, form the exact endpoint-adapted residual $T$ of §2, including (3.1)–(3.3). Prove that its endpoint-annihilator block $C$ is nonsingular and that the actual solution of
> 

$$
> Cw=z
>
$$


> satisfies $w\in3^{-1}\mathbb Z_3^{b/2}$, using the complete recurrence (7.1), the actual producer coefficients, and finite boundary equations.

This would close a real noncancellation obligation by Lemma 4.2. It is more specific than merely defining a Schur scalar.

For a growing saving, one must go further: obtain a growing controlled valuation of $a-z^Tw$, or evaluate the complete determinant pair in (7.6) with an arithmetic-scale estimate. Neither assertion is proved here.

The supplied Jacobi facts remain useful only at their established scope. In particular, Jacobi polynomial content cannot be divided out of primitive affine residual columns or the unit physical endpoint. Classical norms do not prove the directional lemma above.

---

## 8. Arithmetic scale and the unchanged global objective

The already eliminated determinant factors contribute the common valuation


$$
n_J+2b.
$$


They appear in both distinguished cofactors and cancel from their relative valuation. Thus the size of $b$, by itself, supplies no primitive saving of size $3^b$.

At the retained scope of the primitive-ratio identity,


$$
v_3(q)=
\max\!\left(
0,\,
h-26+v_3Q_{\rm loc}(-1)
+v_3\mathcal D_1-v_3\mathcal D_0
\right).
$$


Only a bound on the **relative** cofactor can change this exponent.

A saving of $s$ ternary digits changes a logarithmic denominator estimate by at most $s\log3$, before saturation at exponent zero. Therefore:

* a bounded number of additional digits gives only $O(1)$ logarithmic gain;
* even an $O(h)$ digit bound gives only $O(\log H)$ gain;
* a claim that this meets the whole-error requirement needs the actual quantitative whole-error estimate, not a large radical dimension.

No gain from the separate binary family, a prime-$29$ family, or an unrelated endpoint construction is imported.

### 8.1 Actual contents, clearer, gcd, denominator, and whole error

The local basis transformations over $\mathbb Z_3$ do not determine all-prime contents. They must not replace the actual column contents or the least simultaneous clearer.

Retain exactly


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|),
$$


where the gcd is over **all primes**.

For $B_\ell\ne0$, the actual primitive quantities are


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
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
\tag{8.1}
$$



An irrationality proof requires, at the **same infinite original indices**,


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
\tag{8.2}
$$


Then the nonzero integer linear forms in $e+\pi$ would tend to zero, excluding rationality.

Neither (8.2) nor its negation follows from this report.

---

## 9. Bounded exact-arithmetic audit

No computation was executed here. The coordinator’s supplied $P=2187,r=227$ certificate is accepted only as its stated finite evidence and should not be rerun for this report.

The new obstruction has a small optional audit independent of that certificate.

### Inputs

Use $\lambda=1/3$, endpoint


$$
f=(0,0,1,0)^T,
$$


and the $4\times4$ matrices


$$
M=\operatorname{diag}(9I_2,T).
$$


Check the following nine cases:

1. For $M_0=0,1,2,3$,
   

$$
T=27\operatorname{diag}(3^{M_0},1).
$$



2. For $N=4,5,6,7,8$,
   

$$
T=27
   \begin{pmatrix}
   0&1\\
   1&-9+3^N
   \end{pmatrix}.
$$



For each, calculate exactly


$$
D_0=\det M,\qquad
D_1=f^T\operatorname{adj}(M)f-\frac13\det M.
$$



### Expected verifiable outputs

All nine matrices satisfy


$$
M\equiv\operatorname{diag}(9I_2,0_2)\pmod{27},
$$


with the same exact endpoint and diagonal.

For the first four cases:


$$
v_3D_0=10+M_0,\qquad v_3D_1=7,
$$


so the relative valuations are


$$
3,4,5,6.
$$



For the remaining five:


$$
v_3D_0=10,\qquad v_3D_1=N+7,
$$


so the relative valuations are


$$
-1,-2,-3,-4,-5.
$$



Every $D_0,D_1$ is nonzero. These are auxiliary matrices only. The calculation verifies the new finite algebra, not an original tuple or an infinite statement.

No original-size calculation is required to prove the obstruction theorem. Conversely, no bounded collection of such examples can establish the outstanding infinite original directional-inverse lemma.

---

## 10. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Complete next-producer rank-two formula | Reused as independently accepted |
| Producer cancellation on the leading second-level radical at its displayed digit | Reused as accepted |
| Original precision-$29$ identification, cross calculation, and diagonal valuation in H2 | Pending the specified original-hypothesis audit |
| Auxiliary coefficient/rational-series certificate | Supplied finite evidence only |
| Endpoint-adapted rank-block elimination, with exact diagonal preservation | Proved here |
| New $3^{-2}$ inverse bill and $81M$ correction | Proved here, conditional application to H2 |
| Complete return formulas and the returning producer terms | Derived exactly |
| Endpoint rank-one determinant identity and $3^5$ perturbation | Proved here |
| Directional inverse noncancellation lemma | Proved as a conditional theorem |
| Unbounded positive and negative relative valuations among leading-data completions | Proved here |
| Precision-growing conclusion from the displayed rational-Hankel data alone | Ruled out |
| Existing fixed-width grid argument at unbounded precision | Ruled out as a certification mechanism |
| Complete finite moment recurrence and determinant transfer | Proved here |
| Actual directional inverse bound on an infinite original subfamily | Open |
| Growing actual relative-cofactor saving | Open |
| All-prime gcd versus same-index nonzero whole error | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

### Final conclusion

The new result is not another fixed-digit rank assertion. It is a precise obstruction and a paid endpoint reduction.

Even if the proposed second-radical theorem is fully validated, its rational-Hankel structure and the complete diagonal valuation $-1$ do not control the final relative cofactor. The missing arithmetic information is sharply localized: after exact endpoint adaptation, a directional inverse of valuation $-2$ can turn the apparently two-digits-smaller rank-one perturbation into arbitrarily deep cofactor cancellation.

A viable continuation must therefore prove a **complete-source directional inverse or determinant-pair theorem on the original matrices**, with the returning producer terms, finite boundaries, physical terminal, and every inverse payment retained. The complete recurrence in §7 supplies a concrete source-level starting point; it is not yet the required bound.

The global bottleneck remains the comparison of the **actual all-prime gcd and primitive denominator** with the **nonzero whole evaluated error at the same infinite original indices**.



$$
\boxed{\text{The supplied work still does not prove that }e+\pi
\text{ is rational or irrational.}}
$$


