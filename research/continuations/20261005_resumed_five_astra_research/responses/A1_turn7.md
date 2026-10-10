> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1, Turn 7 — Precision protection, the complete nonlinear correction, and the actual determinant pair

## Executive conclusion

The producer saturation theorem now has a useful precision-parameterized application, but its consequence is **not** that the actual Schur complement may be replaced by the core inside an inverse.

The main results of this report are:

1. **A precision-parameterized theorem for the actual linear force.**  
   At precision $3^p$, the actual producer jet disappears from the complete corrected-column force under explicit factorial-tail, endpoint, grid-separation, and finite-return inequalities. No arbitrary-depth coefficientwise approximation to the original core is assumed.

2. **An exact formula for the complete nonlinear Schur correction.**  
   If $E_c$ is the actual finite core eliminated block and $\widehat Z^{\,c}$ its core-orthogonal residual columns, then
   

$$
\boxed{
   S_{\rm act}
   =
   S_c+3^6\Phi_R-3^{13}\mathcal Q,
   }
$$


   where $\mathcal Q$ is an explicitly defined contraction through the **actual** eliminated inverse. The linear force $\Phi_R$ is not the whole perturbation.

3. **An additional cancellation in that nonlinear term.**  
   The mixed force is divisible by $3$. Moreover, the first possible quadratic correction vanishes because its actual LOW force lies in a small initial-coordinate subspace which is totally isotropic for the finite LOW inverse:
   

$$
\boxed{\mathcal Q\in3M_\nu(\mathbb Z_3).}
$$


   Consequently the unconditional protection supplied by these arguments is
   

$$
\boxed{
   S_{\rm act}-S_c\in3^{\min(6+p,14)}M_\nu(\mathbb Z_3).
   }
$$


   A stronger assertion requires evaluating the complete $\mathcal Q$, not just increasing the precision of the linear support argument.

4. **A specified infinite original-index window and an actual determinant-pair reduction.**  
   On an explicitly specified infinite subfamily with
   

$$
n=4^j+1,\qquad v_3(j)=4,
$$


   the results give
   

$$
S_{\rm act}=-3^{14}\Upsilon,\qquad
   \Upsilon\in M_\nu(\mathbb Z_3),
$$


   with an exact formula for $\Upsilon$. The complete determinant and distinguished cofactor reduce to the exact pair
   

$$
\mathcal D_0=\det\Upsilon,\qquad
   \mathcal D_1
   =
   e_{\rm act}^{T}\operatorname{adj}(\Upsilon)e_{\rm act}
   -3^{14}d_{\rm act}\det\Upsilon.
$$


   This reduction retains the full endpoint and the actual eliminated inverse.

5. **A relative inverse theorem with its losses displayed.**  
   Absolute protection to $3^N$ protects a core inverse only if
   

$$
N>s_c,\qquad
   s_c=-\min_{a,b}v_3((S_c^{-1})_{ab}).
$$


   On the specified window, $S_c\in3^{17}M$, so $s_c\ge17$ whenever $S_c$ is nonsingular. The unconditional protection $N=14$ therefore **does not meet the relative-inverse criterion**. This is a precise obstruction to replacing the actual inverse by the core inverse using the present protection theorem.

The local depth has a transparent but limited denominator effect. When the relevant determinants are nonzero,


$$
\boxed{
v_3(q)
=
\max\!\left\{
0,\,
h-14+v_3(Q_n^{\rm loc}(-1))
+v_3(\mathcal D_1)-v_3(\mathcal D_0)
\right\}.
}
$$


Thus the common residual depth contributes through a **single factor $3^{-14}$** in the determinant ratio, not through a gain of $14\nu$ in the primitive denominator.

The unresolved local object is now the **relative arithmetic of the exact pair $(\mathcal D_0,\mathcal D_1)$**. Another isolated vanishing digit would not resolve it.

No tools were used. Irrationality or rationality of $e+\pi$ remains unresolved.

---

# 1. Scope, notation, and source status

Retain the original family


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$


and


$$
A=n-2=H-D,\qquad H=3^{h-1},\qquad0<D<H/972.
$$


Put


$$
t=v_3(A)=1+v_3(j)\ge5,
$$




$$
m=\frac{A+1}{2},\qquad
d=\frac{3D}{2}-1,\qquad
\nu=\frac D2-1.
$$



The columns remain


$$
U_a=x^a\quad(0\le a<D),\qquad x=y-1,
$$




$$
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m).
$$



In particular,


$$
\deg z_i\le d-1,\qquad i+j\le D-4.
$$


No HIGH coordinate beyond $m$, no residual coordinate beyond $\nu-1$, and no additional terminal residue class will be introduced.

The actual producer is


$$
Q_n^{\rm loc}=3P_n=Q_c+3^6R,
$$


where


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A,
$$




$$
R\in\mathbb Z_3[y],\qquad \deg R\le A+1.
$$



The complete functional is


$$
\boxed{
\mathcal M(F)
=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\!\!\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^s)=(2s)!.
}
\tag{1.1}
$$



Define


$$
G_c(f,g)=\mathcal M(Q_cfg),\qquad
K(f,g)=\mathcal M(Rfg),
$$


so that


$$
G_{\rm act}=G_c+3^6K.
$$



## 1.1 What is accepted, and what is not silently promoted

The following are reused:

- Turn 5’s producer saturation theorem, now reviewed in A4 Turn 10;
- its exact signed scalar denominator and complete normalized producer force;
- the finite LOW/HIGH unit-block structure;
- the finite core support operations reviewed in old A4 Turn 26;
- the previously established original-index irrational-rotation reachability;
- the actual depth-seven identification and its finite radical consequences.

The supplied finite certificate corroborates the stated auxiliary orders. It is not the proof of the general producer theorem and supplies no original-index inverse valuation.

Turn 6’s sharper full-domain corrected-force and depth-eight statements remain pending review. The arguments below do **not** require their constants $972,2916,8748$ to be accepted at new precisions. I use a more conservative window furnished by the reviewed finite core closure.

The old arbitrary-depth transfer


$$
Q_n^{\rm loc}-Q_c\in3^{v_3(j)+2}\mathbb Z_3[y]
$$


is not assumed.

---

# 2. The producer jet at arbitrary stated precision

Let


$$
F=(n-1)!=(A+1)!.
$$


The accepted saturation theorem says that, if


$$
3P_n-Q_c=\sum_{a=0}^{A+1}e_ax^a,
$$


then


$$
v_3(e_a)\ge v_3(F/a!),
\qquad
v_3((3P_n-Q_c)(-1))\ge2v_3(F).
\tag{2.1}
$$



For $p\ge1$, let $\ell_{6+p}$ be the least terminal length satisfying


$$
v_3\!\left(\frac{F}{(A+1-\ell_{6+p})!}\right)\ge6+p.
\tag{2.2}
$$


Assume this factorial is defined, and put


$$
\kappa_p=\ell_{6+p}-2.
$$



If


$$
2v_3(F)\ge6+p,
\tag{2.3}
$$


then the reviewed argument gives


$$
\boxed{
R(y)\equiv
(y+1)x^{A-\kappa_p}B_p(x)\pmod{3^p},
\qquad
\deg B_p\le\kappa_p.
}
\tag{2.4}
$$



Both the terminal exponent and the endpoint factor are essential. The latter follows from the actual endpoint divisibility and the fact that $x=-2$ is a unit.

## 2.1 Explicit dependence on $t$

Write $g=3^t$. For $0\le k<g$,


$$
v_3\!\left(\frac{(A+1)!}{(A-k-1)!}\right)
=
t+v_3(k!).
\tag{2.5}
$$


Indeed, the factors are


$$
A+1,\ A,\ A-1,\ldots,A-k,
$$


and $v_3(A-r)=v_3(r)$ for $0<r<g$.

Consequently, whenever the minimum below is less than $g$,


$$
\boxed{
\kappa_p
=
\min\{k\ge0:t+v_3(k!)\ge6+p\}.
}
\tag{2.6}
$$



For example, on $t=5$,


$$
\kappa_1=6,\qquad
\kappa_3=9,\qquad
\kappa_8=21,\qquad
\kappa_9=24.
\tag{2.7}
$$



A convenient sufficient bound is


$$
\kappa_p\le3\max(0,6+p-t)
\tag{2.8}
$$


when the right-hand side is less than $3^t$. This bound is not substituted for the actual minimal terminal length when an exact threshold is needed.

## 2.2 The exact terminal-length obstruction

The factorization used below needs


$$
\kappa_p\le D.
$$


Equivalently,


$$
\ell_{6+p}\le D+2.
$$


Thus the exact terminal-tail condition is


$$
\boxed{
6+p\le
v_3\!\left(\frac{(A+1)!}{(A-D-1)!}\right).
}
\tag{2.9}
$$



This is one precise point where producer support protection can cease to be available. It is a loss of this certificate, not a claim that the actual force becomes nonzero at that precision.

---

# 3. Reusing the finite core closure at variable precision

For an integer $r\ge6$, put


$$
\Omega_r=\frac H{3^{r-1}},
\qquad
C_r=512(r+1)^2\,3^{r-1}.
\tag{3.1}
$$



The reviewed five core operations have the following sufficient numerical hypotheses:


$$
h\ge r+2,\qquad C_rD<H.
\tag{3.2}
$$



Their working width is


$$
W_r=4(r+1)(D+2),
$$


and the displayed proof uses


$$
\boxed{
W_r+2D+2<\Omega_r/8.
}
\tag{3.3}
$$



The condition $C_rD<H$ implies this inequality on the present domain.

## 3.1 Hypothesis audit of the core argument

The old statement also imposed a large $v_3(j)$ because its proposed *actual transfer* used an arbitrary-depth producer approximation. That approximation is not needed for the **core operations**.

The displayed core proof uses:

- $H$ is a power of $3$;
- $D$ is even and divisible by $3$;
- $\beta\equiv1\pmod3$;
- the finite column endpoints;
- the coefficient support of $x^H$ and $(1-z)^{-H}$;
- the width inequalities;
- $h\ge r+2$, for the factorial term after the stated division.

All these hold here with $t\ge5$. No step in the five core operations uses $t\ge r-1$. Thus the proof itself gives the following core-only lemma at the stated numerical scope:

> **Finite core closure lemma.** Under (3.2), the original finite core Schur complement satisfies
> 

$$
> \boxed{S_c\in3^{r+1}M_\nu(\mathbb Z_3).}
> \tag{3.4}
>
$$


> Here $S_c$ is the un-divided Schur complement; the old normalized radical form was $S_c/3$.

This extracts the scope actually proved by the reviewed operations. It does not restore their conditional arbitrary-depth actual transfer.

## 3.2 Corrected-column support supplied by those operations

Let $W=[U\ Y]$. Write


$$
E_c=G_c(W,W),\qquad C_c=G_c(W,Z),
$$


and


$$
\widehat Z^{\,c}=Z-WE_c^{-1}C_c.
\tag{3.5}
$$


These columns are integral; in particular,


$$
\widehat Z^{\,c}\equiv Z\pmod3.
\tag{3.6}
$$



For support notation, put


$$
I_{\Omega}(w)=\{a\Omega+u:a\in\mathbb Z,\ |u|\le w\}.
$$



Fix $p\ge1$, and take


$$
r=\max(6,p).
$$


At precision $3^p$, the HIGH correction requires at most $p-2$ occurrences of the complete $F$-operator, because of its initial factor $3$. The reviewed operations give:

- no width increase under the finite HIGH inverse;
- increase at most $\nu+1=D/2$ per return;
- after lower-edge monic division, quotient degree at most the edge width plus $\nu$.

A safe resulting width is


$$
\boxed{w_p=pD/2.}
\tag{3.7}
$$



The actual LOW projection is the monic remainder at this precision, by the reviewed coefficient-gap proof. The $B$-correction is zero at the required modulus. Hence


$$
\boxed{
\widehat z_i^{\,c}\equiv x^D\psi_i(y)\pmod{3^p},
}
\tag{3.8}
$$


where


$$
\deg\psi_i\le m-D,\qquad
\operatorname{supp}\psi_i\subseteq I_{\Omega_r}(w_p).
\tag{3.9}
$$



This is a reuse of the finite return mechanism. The lower truncations and upper boundary $m$ remain those in the reviewed proof.

---

# 4. Precision-parameterized protection of the actual linear force

Define


$$
(\Phi_R)_{ij}
=
\mathcal M(R\widehat z_i^{\,c}\widehat z_j^{\,c}).
\tag{4.1}
$$



## Theorem 4.1 — Actual corrected-force protection

Let $p\ge1$, $r=\max(6,p)$. In addition to the original domain, assume


$$
h\ge r+2,\qquad C_rD<H,
\tag{4.2}
$$




$$
2v_3(F)\ge6+p,\qquad \kappa_p\le D,
\tag{4.3}
$$


and


$$
\boxed{
D+2w_p<\frac{\Omega_r-1}{2},
\qquad w_p=pD/2.
}
\tag{4.4}
$$


Then


$$
\boxed{\Phi_R\in3^pM_\nu(\mathbb Z_3).}
\tag{4.5}
$$



The stronger core-width condition in (4.2) already implies (4.4); it is displayed separately because it is the exact final force-separation inequality.

### Proof

Use (2.4) and (3.8). The endpoint-subtracted quotient is congruent modulo $3^p$ to


$$
x^{A-\kappa_p+2D}B_p(x)\psi_i\psi_j
=
x^H\,x^{D-\kappa_p}B_p(x)\psi_i\psi_j.
\tag{4.6}
$$



The endpoint subtraction vanishes at this modulus because $R(-1)\in3^p\mathbb Z_3$. Monic division by $y+1$ preserves the congruence.

Since


$$
\deg(x^{D-\kappa_p}B_p)\le D,
$$


the non-$x^H$ factor in (4.6) has support in


$$
I_{\Omega_r}(D+2w_p).
\tag{4.7}
$$



For $0<k<H$,


$$
v_3\binom Hk=h-1-v_3(k).
$$


Thus $x^H\bmod3^p$ is supported on multiples of


$$
H/3^{p-1},
$$


which are multiples of $\Omega_r$. Multiplication by $x^H$ preserves the support class in (4.7).

Every pole capable of contributing modulo $3^p$ has


$$
v_3(2v+1)\ge h-p+1.
$$


Since $r\ge p$, its coefficient position is on the odd half-grid


$$
J_{\Omega_r}(0)
=
\left\{\frac{(2a+1)\Omega_r-1}{2}:a\in\mathbb Z\right\}.
$$


Condition (4.4) separates this half-grid from (4.7).

This accounts for **every pole satisfying the original finite cutoff**, not merely the first few displayed poles. The factorial term vanishes modulo $3^p$ because $h\ge p$ and the polynomial coefficients are integral.

Therefore every entry of (4.1) is divisible by $3^p$. ∎

## 4.1 Where this support certificate first stops

For fixed $H,D,t$, the theorem applies exactly at the precisions satisfying its displayed conditions. Its potential stopping points are:

1. **factorial endpoint protection**
   

$$
p\le2v_3(F)-6;
$$



2. **terminal exponent protection**
   

$$
p\le
   v_3\!\left(\frac{(A+1)!}{(A-D-1)!}\right)-6;
$$



3. **finite return closure**
   

$$
h\ge r+2,\qquad C_rD<H;
$$



4. **final force separation**
   

$$
\boxed{
   \frac H{3^{r-1}}>2(p+1)D+1.
   }
   \tag{4.8}
$$



The first $p$ violating one of these is the first precision **not certified by this theorem**. It is not automatically the first nonzero force precision.

On a fixed real window


$$
a<D/H<b,\qquad a>0,
$$


the return condition requires


$$
512(r+1)^2\,3^{r-1}a<1.
\tag{4.9}
$$


Hence this support certificate has a precision bound independent of $n$ on that fixed window. Ordinary reachability of the window does not turn it into unbounded precision.

---

# 5. The exact nonlinear Schur correction

Linear force protection alone is insufficient. The following identity isolates the complete outstanding term.

In the core-orthogonal coordinates $[W,\widehat Z^{\,c}]$,


$$
G_c=
\begin{pmatrix}
E_c&0\\
0&S_c
\end{pmatrix}.
$$



Define the actual force blocks


$$
K_{WW}=K(W,W),\qquad
T=K(W,\widehat Z^{\,c}),\qquad
\Phi_R=K(\widehat Z^{\,c},\widehat Z^{\,c}),
$$


and


$$
E_{\rm act}=E_c+3^6K_{WW}.
\tag{5.1}
$$



The retained eliminated-block inverse estimate is


$$
E_c^{-1}\in3^{-1}M(\mathbb Z_3).
$$


Since


$$
3^6E_c^{-1}K_{WW}\in3^5M(\mathbb Z_3),
$$


$E_{\rm act}$ is nonsingular and


$$
E_{\rm act}^{-1}\in3^{-1}M(\mathbb Z_3).
\tag{5.2}
$$



Exact block elimination gives


$$
\boxed{
S_{\rm act}
=
S_c+3^6\Phi_R
-
3^{12}T^TE_{\rm act}^{-1}T.
}
\tag{5.3}
$$



There are no omitted higher perturbation terms in (5.3). They are all contained in $E_{\rm act}^{-1}$.

---

# 6. Two actual cancellations in the mixed-force contraction

## 6.1 The complete mixed force is divisible by $3$

### Lemma 6.1


$$
\boxed{T\in3M(\mathbb Z_3).}
\tag{6.1}
$$



### Proof

By (3.6),


$$
\widehat z_i^{\,c}\equiv z_i\pmod3.
$$


For any column $w$ of $W$,


$$
\deg w\le m,\qquad
\deg R\le A+1,\qquad
\deg z_i\le d-1.
$$


Therefore


$$
\deg(Rwz_i)\le A+d+m=\frac{3H-1}{2}=r_*.
$$


Its endpoint-subtracted quotient has degree at most $r_*-1$.

Modulo $3$, only the top pole at $r_*$ can survive, and that coefficient is absent by this exact degree bound. The factorial term is also zero modulo $3$. ∎

Write


$$
T=3T_1,\qquad J_{\rm act}=3E_{\rm act}^{-1}.
$$


Then (5.3) becomes


$$
\boxed{
S_{\rm act}
=
S_c+3^6\Phi_R-3^{13}\mathcal Q,
\qquad
\mathcal Q=T_1^TJ_{\rm act}T_1.
}
\tag{6.2}
$$



## 6.2 The finite LOW inverse kills the leading contraction

The core eliminated block has the retained form


$$
E_c=
\begin{pmatrix}
3L&3X\\
3X^T&E_Y
\end{pmatrix},
\qquad L\in\operatorname{GL}_D(\mathbb Z_3).
\tag{6.3}
$$


It follows that


$$
J_{\rm act}\equiv
\begin{pmatrix}
L^{-1}&0\\
0&0
\end{pmatrix}\pmod3.
\tag{6.4}
$$



The next lemma uses the actual $x$-basis LOW endpoint.

### Lemma 6.2 — LOW anti-triangularity

Modulo $3$,


$$
L_{ab}=0\quad(a+b\ge D),\qquad
L_{a,D-1-a}=1.
\tag{6.5}
$$


Consequently,


$$
\boxed{
(L^{-1})_{ab}=0\pmod3
\quad(a+b<D-1).
}
\tag{6.6}
$$



### Proof

The top pole is absent in the LOW/LOW block by degree. After its normalization by $3$, its residue is


$$
L_{ab}\equiv
[y^{r_1}]x^{A+a+b},
\qquad r_1=(H-1)/2.
$$



For $a+b\ge D$,


$$
x^{A+a+b}=x^H x^{a+b-D}
\equiv(y^H-1)x^{a+b-D}\pmod3.
$$


The lower factor has degree at most $D-2$, so the coefficient at $r_1$ is zero.

For $a+b=D-1$,


$$
x^{A+a+b}=x^{H-1}
\equiv1+y+\cdots+y^{H-1}\pmod3.
$$


The coefficient is $1$.

Reversal turns $L$ into a unit upper-triangular matrix. Reversing its inverse gives (6.6). ∎

Now split


$$
T_1=\binom a b
$$


into LOW and HIGH rows. Let $\kappa_1$ be the actual terminal width modulo $3$, so


$$
\kappa_1\le6.
$$



### Lemma 6.3 — Actual initial-row localization



$$
\boxed{
a_{ui}=0\pmod3\qquad(u\ge\kappa_1).
}
\tag{6.7}
$$



### Proof

For a LOW column $U_u$, the top pole is absent even with the full corrected column:


$$
\deg(RU_u\widehat z_i^{\,c})
\le A+1+(D-1)+m=H+m<r_*.
$$


Since $\widehat z_i^{\,c}-z_i\in3\mathbb Z_3[y]$, its contribution to $K(RU_u,\widehat z_i^{\,c})$ is zero modulo $9$: after removing that factor $3$, the same top-pole degree argument applies.

Hence


$$
a_{ui}
\equiv
[y^{r_1}]
x^{H-\kappa_1+u}B_1(x)y^i
\pmod3.
\tag{6.8}
$$



If $u\ge\kappa_1$, this is an extraction from


$$
(y^H-1)x^{u-\kappa_1}B_1(x)y^i.
$$


The lower factor has degree at most $u+i<r_1$, so the coefficient is zero. ∎

Because


$$
D\ge2\cdot3^t\ge486,\qquad\kappa_1\le6,
$$


the initial $\kappa_1$-coordinate subspace is totally isotropic for $L^{-1}\bmod3$. Equations (6.4)–(6.7) therefore prove


$$
\boxed{\mathcal Q\equiv a^TL^{-1}a\equiv0\pmod3.}
\tag{6.9}
$$



This is a cancellation for the **actual** mixed force. It is not obtained by declaring the binomial residual digit invertible.

---

# 7. The protection theorem, including the complete next correction

Combining the preceding results gives:

## Theorem 7.1 — Actual Schur protection with nonlinear loss accounted

Under the hypotheses of Theorem 4.1,


$$
\boxed{
S_{\rm act}-S_c
=
3^6\Phi_R-3^{13}\mathcal Q,
\qquad
\Phi_R\in3^pM,\quad \mathcal Q\in3M.
}
\tag{7.1}
$$


Thus


$$
\boxed{
S_{\rm act}-S_c
\in3^{\min(6+p,14)}M_\nu(\mathbb Z_3).
}
\tag{7.2}
$$



More precisely, if


$$
q_{\mathcal Q}=\min_{i,j}v_3(\mathcal Q_{ij}),
$$


then


$$
S_{\rm act}-S_c
\in3^{\min(6+p,13+q_{\mathcal Q})}M,
\qquad q_{\mathcal Q}\ge1.
\tag{7.3}
$$



Possible cancellation between the two complete summands can improve this lower bound. Their valuations must not be subtracted or combined as though equality had been proved.

## 7.1 The complete correction at the first unprotected nonlinear order

Write the actual eliminated block as


$$
E_{\rm act}=
\begin{pmatrix}
3L_{\rm act}&3X_{\rm act}\\
3X_{\rm act}^T&E_{Y,\rm act}
\end{pmatrix},
$$


and


$$
\widehat E_{\rm act}
=
E_{Y,\rm act}
-3X_{\rm act}^TL_{\rm act}^{-1}X_{\rm act}.
$$


All unit inverses here exist.

With


$$
\widetilde b=b-X_{\rm act}^TL_{\rm act}^{-1}a,
$$


the exact quadratic term is


$$
\boxed{
\mathcal Q
=
a^TL_{\rm act}^{-1}a
+
3\widetilde b^T\widehat E_{\rm act}^{-1}\widetilde b.
}
\tag{7.4}
$$



The first term is divisible by $3$, by the preceding LOW argument. Therefore


$$
\boxed{
\frac{\mathcal Q}{3}
=
\frac{a^TL_{\rm act}^{-1}a}{3}
+
\widetilde b^T\widehat E_{\rm act}^{-1}\widetilde b
}
\tag{7.5}
$$


is integral.

This is the complete nonlinear correction which can first enter at order $3^{14}$. It includes:

- the actual LOW perturbation;
- the actual LOW inverse;
- both mixed LOW/HIGH terms through $\widetilde b$;
- the actual finite HIGH inverse;
- all producer-force poles and the factorial force through $a,b$.

If $p=8$, the order-$14$ numerator must also retain $3^{-8}\Phi_R$. If $p\ge9$, that linear contribution is absent modulo $3^{15}$.

I do **not** assert that $\mathcal Q/3$ is nonzero. Order $14$ is the first order not excluded by the theorem after the proved cancellations. Determining an actual first nonzero order requires more information.

The important change of objective is that (7.4), not a sequence of separate guessed digits, is now the exact nonlinear object to be controlled.

---

# 8. Relative inverse and determinant protection

Let $S_c$ be nonsingular and define its inverse loss


$$
s_c=-\min_{i,j}v_3((S_c^{-1})_{ij}).
$$


Let


$$
\Delta=S_{\rm act}-S_c\in3^NM.
$$



## Theorem 8.1 — Relative matrix protection

If


$$
\boxed{N>s_c,}
\tag{8.1}
$$


then $S_{\rm act}$ is nonsingular and


$$
\boxed{
\frac{\det S_{\rm act}}{\det S_c}
\in1+3^{N-s_c}\mathbb Z_3,
}
\tag{8.2}
$$




$$
\boxed{
S_{\rm act}^{-1}-S_c^{-1}
\in3^{N-2s_c}M(\mathbb Z_3).
}
\tag{8.3}
$$



### Proof

The matrix $S_c^{-1}\Delta$ belongs to $3^{N-s_c}M$, which is topologically nilpotent under (8.1). Therefore


$$
S_{\rm act}^{-1}
=
(I+S_c^{-1}\Delta)^{-1}S_c^{-1},
$$


and the convergent Neumann series gives (8.3). Taking determinants gives (8.2). ∎

The two inverse losses in (8.3) are real. An absolute congruence modulo $3^N$ cannot be inserted into an inverse without them.

## 8.1 The endpoint changes as well

Let


$$
w=W(-1)^T,
$$


and let $e_c$ be the endpoint in the core-orthogonal residual coordinates. Exact actual elimination gives


$$
\boxed{
e_{\rm act}
=
e_c-3^6T^TE_{\rm act}^{-1}w
=
e_c-3^6T_1^TJ_{\rm act}w.
}
\tag{8.4}
$$


Hence


$$
e_{\rm act}-e_c\in3^6\mathbb Z_3^\nu.
\tag{8.5}
$$



Define


$$
d_c=w^TE_c^{-1}w,\qquad
d_{\rm act}=w^TE_{\rm act}^{-1}w.
$$


The eliminated inverse perturbation has valuation at least $4$, so


$$
d_{\rm act}-d_c\in3^4\mathbb Z_3.
\tag{8.6}
$$



If (8.1) holds, the whole endpoint contraction consequently satisfies


$$
\boxed{
\begin{aligned}
&\left(d_{\rm act}
+e_{\rm act}^TS_{\rm act}^{-1}e_{\rm act}\right)
-\left(d_c+e_c^TS_c^{-1}e_c\right)\\
&\hspace{15mm}\in
3^{\min(4,\ 6-s_c,\ N-2s_c)}\mathbb Z_3.
\end{aligned}
}
\tag{8.7}
$$



This is an absolute scalar bound. To deduce a **relative** scalar comparison or scalar nonvanishing, its exponent must exceed the valuation of the entire core scalar


$$
d_c+e_c^TS_c^{-1}e_c.
$$


That scalar may itself exhibit cancellation.

The actual producer endpoint $Q_n^{\rm loc}(-1)$ must remain outside this comparison. Replacing it by the core endpoint would replace a nonzero actual quantity by $Q_c(-1)=0$.

---

# 9. A specified infinite original-index window

Set


$$
C_{16}=512\cdot17^2\cdot3^{15}.
$$


Consider the original indices satisfying


$$
\boxed{
j\equiv81\pmod{243},
\qquad
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}}.
}
\tag{9.1}
$$



Then


$$
v_3(j)=4,\qquad t=5.
$$



The retained irrational-rotation reachability applies on this fixed arithmetic progression and fixed open real window. Thus (9.1) contains infinitely many original indices. No restricted higher-digit infinitude is assumed, and no new density proof is needed.

For sufficiently large indices in this window:

- the core closure at $r=16$ gives
  

$$
S_c\in3^{17}M;
$$


- the force theorem at $p=9$ applies;
- $\kappa_9=24<D$;
- the endpoint factorial condition holds;
- therefore
  

$$
\Phi_R\in3^9M,\qquad \mathcal Q\in3M.
$$



It follows that


$$
\boxed{S_{\rm act}\in3^{14}M_\nu(\mathbb Z_3).}
\tag{9.2}
$$



## 9.1 Why this precision does not protect the endpoint inverse

If $S_c$ is nonsingular, $S_c\in3^{17}M$ implies


$$
s_c\ge17.
$$


Indeed, writing $S_c=3^{17}B$, an integral nonsingular $B$ cannot have every entry of $B^{-1}$ divisible by $3$.

The guaranteed actual-core precision is only $N=14$. Hence


$$
N>s_c
$$


fails.

Thus the current theorem does **not** justify


$$
S_{\rm act}^{-1}\approx S_c^{-1}
$$


on this infinite window.

Increasing $p$ in the linear-force theorem does not repair that comparison unless the complete nonlinear contraction $\mathcal Q$ is also controlled. This is the precise inverse bottleneck.

---

# 10. The full radical, complement, and exact determinant pair

On (9.1), the actual depth-seven digit is wholly zero. Its radical is the entire residual space, and there is no nondegenerate depth-seven complement to invert.

The arguments above therefore act on the **full actual radical**. They do not substitute an inverse of a singular binomial digit.

For reference, if a later actual digit $C$ is singular but not zero, one must choose a lifted basis $P=[K\ L]$ for its full radical and a nondegenerate complement. In those coordinates,


$$
M=
\begin{pmatrix}
A&B\\
B^T&C_L
\end{pmatrix},
$$


with $C_L$ a unit matrix and $A,B\in3M$. The next exact operator and endpoint are


$$
A-BC_L^{-1}B^T,
\qquad
e_K-BC_L^{-1}e_L.
\tag{10.1}
$$


Any determinant formula also retains the factor $(\det P)^{-2}$. Ignoring the radical or enlarging the shortened terminal class would change this problem.

## 10.1 An exact integral operator on the whole residual space

On (9.1), define


$$
\boxed{
\Upsilon
=
\frac{\mathcal Q}{3}
-
\frac{\Phi_R}{3^8}
-
\frac{S_c}{3^{14}}.
}
\tag{10.2}
$$


Each term is integral, and (6.2) gives the exact identity


$$
\boxed{S_{\rm act}=-3^{14}\Upsilon.}
\tag{10.3}
$$



This definition retains the entire force and the entire actual nonlinear correction. It is not merely a formula for a residue digit.

Put


$$
\mathcal D_0=\det\Upsilon,
$$




$$
\boxed{
\mathcal D_1
=
e_{\rm act}^T\operatorname{adj}(\Upsilon)e_{\rm act}
-3^{14}d_{\rm act}\det\Upsilon.
}
\tag{10.4}
$$



The adjugate expression is valid whether or not $\Upsilon$ is nonsingular.

## Theorem 10.1 — Actual determinant-pair reduction

On (9.1),


$$
\boxed{
\det G_{\rm act}
=
\det E_{\rm act}\,(-3^{14})^\nu\mathcal D_0,
}
\tag{10.5}
$$


and


$$
\boxed{
v^T\operatorname{adj}(G_{\rm act})v
=
\det E_{\rm act}\,(-3^{14})^{\nu-1}\mathcal D_1.
}
\tag{10.6}
$$



Here $v$ is the original monomial endpoint vector, and $e_{\rm act},d_{\rm act}$ are its actual transported quantities.

### Proof

For every invertible eliminated block,


$$
\det G_{\rm act}=\det E_{\rm act}\det S_{\rm act},
$$


and


$$
v^T\operatorname{adj}(G_{\rm act})v
=
\det E_{\rm act}
\left(
d_{\rm act}\det S_{\rm act}
+
e_{\rm act}^T\operatorname{adj}(S_{\rm act})e_{\rm act}
\right).
$$


These identities hold also when the residual block is singular, either directly by block determinant identities or by polynomial continuation.

Substitute (10.3) and retain the sign and all powers of $3$. ∎

This is the promised actual determinant-pair statement. It moves the denominator question from “how many zero digits have been found?” to the relative arithmetic of one exact pair.

---

# 11. Consequences for the actual primitive denominator

Restore


$$
Q_n=\lambda Q_n^{\rm loc},\qquad \lambda\in\mathbb Z_3^\times,
$$




$$
R_{\rm rat}=\frac{4\lambda}{3^h}G_{\rm act},
$$


and


$$
H_{\rm complete}
=
R_{\rm rat}+(e+\pi)Q_n(-1)vv^T.
$$



Retain


$$
\beta_0=\det R_{\rm rat},
\qquad
\beta_1=Q_n(-1)v^T\operatorname{adj}(R_{\rm rat})v.
$$



When $\mathcal D_0\ne0$, Theorem 10.1 gives


$$
\boxed{
\frac{\beta_1}{\beta_0}
=
-\frac{3^{h-14}Q_n^{\rm loc}(-1)}4
\frac{\mathcal D_1}{\mathcal D_0}.
}
\tag{11.1}
$$



This formula retains the actual producer endpoint. Its nonvanishing does not imply $\mathcal D_1\ne0$.

Let $k=m+1$, and choose a clearing integer $\ell$ so that


$$
A_\ell=\ell^k\beta_0,\qquad B_\ell=\ell^k\beta_1
$$


are integers. Preserve the full gcd


$$
\boxed{g_\ell=\gcd(|A_\ell|,|B_\ell|).}
\tag{11.2}
$$


When $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$



If $\mathcal D_0\mathcal D_1\ne0$, taking the valuation of the exact ratio—not subtracting unrelated determinant lower bounds—gives


$$
\boxed{
v_3(q)
=
\max\!\left(
0,\,
h-14+v_3(Q_n^{\rm loc}(-1))
+v_3(\mathcal D_1)-v_3(\mathcal D_0)
\right).
}
\tag{11.3}
$$



### What local depth actually contributes

The powers in (10.5) and (10.6) differ by one residual factor. Their large common power cancels in the ratio.

Accordingly:

- depth $14$ contributes the explicit term $-14$ in (11.3);
- it does **not** produce a denominator gain of $14\nu$;
- the unknown difference
  

$$
v_3(\mathcal D_1)-v_3(\mathcal D_0)
$$


  can defeat any inference based only on common residual depth;
- no odd-prime part of $g_\ell$ has been determined.

The whole primitive error remains


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
\det H_{\rm complete}.
}
\tag{11.4}
$$



Neither the all-prime gcd nor the whole evaluated determinant error is replaced by the local pair analysis.

---

# 12. The precise obstruction—and its scope

The obstruction established here is to a particular inference:

> **Finite absolute protection plus a nonzero endpoint residue does not determine the endpoint inverse contraction, its nonvanishing, or the primitive denominator.**

This is not merely a lack of a convenient estimate. The missing information is mathematically necessary.

For example, after an integral change of coordinates sending a primitive endpoint to $e_1$, the matrices


$$
S_L=\operatorname{diag}(3^L,3^{14},\ldots,3^{14}),
\qquad L\ge14,
$$


all satisfy the same depth-$14$ zero congruence, but


$$
e_1^TS_L^{-1}e_1=3^{-L}
$$


has arbitrarily large inverse loss.

In dimension at least two, an invertible block


$$
3^L
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}
$$


has a primitive endpoint $e_1$ with zero self-contraction. Thus endpoint nonvanishing does not even guarantee distinguished-cofactor nonvanishing.

These are **not counterexamples involving the actual producer**. They show the exact scope of the obstruction: the supplied absolute congruence data cannot imply the desired inverse or denominator conclusion without additional structural information about the actual contraction.

The exact identities (7.4) and (10.4) specify that additional structure to be studied.

---

# 13. Concrete follow-on lemma

The next task should not be “find one more zero digit.”

A useful follow-on statement is:

> **Actual relative-pair lemma on the window (9.1).**  
> For the exact operator $\Upsilon$ in (10.2) and exact transported endpoint $e_{\rm act}$, determine:
> 

$$
> \mathcal D_0=\det\Upsilon,
> \qquad
> \mathcal D_1
> =
> e_{\rm act}^T\operatorname{adj}(\Upsilon)e_{\rm act}
> -3^{14}d_{\rm act}\det\Upsilon,
>
$$


> including their nonvanishing and a uniform law or bound for
> 

$$
> v_3(\mathcal D_1)-v_3(\mathcal D_0).
>
$$


> Any comparison with a Jacobi/core predictor must include its actual inverse loss and the entire scalar contraction, including cancellation with $d_{\rm act}$.

Two legitimate routes remain:

1. control the full radical and complement of the first nonzero actual digit, using (10.1), until the scalar contraction is determined; or
2. use the retained exact Jacobi inverse to prove a relative scalar comparison satisfying the loss inequalities in §8.

The known Jacobi resonance obstruction must remain in force. Coefficientwise dominance cannot be restored by citing a classical inverse formula, and a fixed polar-residue computation does not by itself control a moving-degree original-index sum.

Globally, even this relative-pair lemma would still need same-index all-prime gcd control and a nonzero whole-error estimate.

---

# 14. Bounded exact arithmetic for personal inspection

No finite computation is needed for the symbolic Schur identity or the support theorem. A small bounded certificate can inspect the new LOW-isotropy mechanism independently.

## Auxiliary inputs

Take


$$
H=2187,\qquad D=18,\qquad
\kappa=6,\qquad
\nu=8,\qquad
r_1=1093.
$$



These are **auxiliary polynomial inputs**, not original indices and not an invocation of the original order-six producer congruence.

Construct over $\mathbb F_3$


$$
L_{ab}
=
[y^{r_1}](y-1)^{H-D+a+b},
\qquad0\le a,b<18.
$$



For


$$
0\le b\le6,\qquad0\le i<8,
$$


construct the $18$-vector


$$
a^{(b,i)}_u
=
[y^{r_1}]
(y-1)^{H-\kappa+u+b}y^i,
\qquad0\le u<18.
$$



All coefficients can be obtained as signed binomial coefficients modulo $3$.

## Expected verifiable output

1. $L$ is invertible.
2. Its entries satisfy
   

$$
L_{ab}=0\quad(a+b\ge18),\qquad
   L_{a,17-a}=1.
$$


3. Its inverse satisfies
   

$$
(L^{-1})_{ab}=0\quad(a+b<17).
$$


4. Every one of the $56$ vectors $a^{(b,i)}$ is supported in coordinates $0,\ldots,5$.
5. All $56^2$ pairings vanish:
   

$$
(a^{(b,i)})^TL^{-1}a^{(c,j)}=0.
$$



This certificate checks the finite algebra underlying the first nonlinear cancellation. It cannot determine the actual $\mathcal Q/3$, the actual pair $(\mathcal D_0,\mathcal D_1)$, or any infinite denominator law.

---

# 15. Final proof ledger

| Statement | Status |
|---|---|
| Turn 5 producer saturation and signed denominator | Accepted after A4 Turn 10 |
| Supplied auxiliary unit/pivot/force certificate | Finite corroboration only |
| Arbitrary-depth approximation to the original core | Not assumed |
| Precision-$p$ actual terminal jet | Reused with exact factorial and endpoint conditions |
| Finite corrected-column support with explicit return widths | Derived from the reviewed core operations |
| Actual complete linear-force protection $\Phi_R\in3^pM$ | Proved under the displayed inequalities |
| Exact nonlinear Schur identity | Proved |
| Mixed-force divisibility $T\in3M$ | Proved by the original degree endpoints |
| LOW inverse isotropy and $\mathcal Q\in3M$ | Proved for the actual force |
| Guaranteed actual-core precision $\min(6+p,14)$ | Proved |
| Infinite original-index window (9.1) | Reuses accepted rotation reachability |
| Actual depth-$14$ factorization on that window | Proved |
| Exact determinant-pair reduction $(\mathcal D_0,\mathcal D_1)$ | Proved, without residual nonsingularity |
| Relative inverse comparison on that window | Not obtained; the required inequality fails for the guaranteed precision |
| Nonvanishing and relative valuation of $\mathcal D_0,\mathcal D_1$ | Unresolved |
| Actual all-prime gcd and whole-error decay | Unresolved |

## Closing conclusion

The new result is a precision-parameterized application of producer saturation to the **actual complete force**, followed by an exact accounting of the nonlinear Schur correction. The first quadratic contribution is shown to cancel through the actual finite LOW inverse, and an infinite original-index window admits an exact depth-$14$ determinant-pair reduction.

The inverse bottleneck is now explicit:



$$
\boxed{
\text{Control the relative arithmetic of }
\mathcal D_0
\text{ and }
\mathcal D_1,
\text{ not merely a common residual depth.}
}
$$



The protection obtained here does not suffice to replace the actual endpoint inverse by the core inverse on the specified window. Its denominator consequence is the exact formula (11.3), which still contains the unresolved relative pair valuation and preserves the full all-prime gcd.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


