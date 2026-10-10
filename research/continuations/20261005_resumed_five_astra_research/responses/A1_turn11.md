> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1, Turn 11 — An actual unit-resultant Hankel transfer for the full displacement-relative pair

## Executive conclusion

The actual displacement can be normalized **without a residual determinant denominator**. The decisive facts are stronger than cyclicity alone:

1. The Krylov matrix of
   

$$
\mathscr D=\mathscr C-e_0\ell^T
$$


   from $e_0$ has determinant **exactly $1$**.

2. On the retained original domain, the actual second displacement generator satisfies
   

$$
r_{\rm act}\equiv e_{\nu-1}\pmod3.
$$


   After the determinant-one Krylov change of basis, its associated generating polynomial $\mathsf R(X)$ satisfies
   

$$
\boxed{\mathsf R(X)\equiv1\pmod3.}
$$


   Consequently the actual resultant
   

$$
\boxed{\mathfrak u=\operatorname{Res}(f,\mathsf R)\in1+3\mathbb Z_3}
$$


   is a unit throughout the original domain. This is an actual, unconditional nonvanishing statement for the **normalizing resultant**, not for the residual determinant.

3. On the accepted depth-$16$ window, these two transformations convert the full normalized residual form $\Psi$ into an **integral Hankel matrix**
   

$$
\mathsf H=(\mu_{i+j})_{0\le i,j<\nu}.
$$


   No inverse of $\Psi$, no generic coprimality assumption, and no division by a residual pivot is used.

4. The actual transported endpoint becomes a vector
   

$$
\varepsilon_i\equiv(-1)^i\pmod3.
$$


   Thus **every endpoint coordinate is a unit**. Its complete distinguished cofactor is the determinant of an explicitly evaluated endpoint-kernel Gram matrix, followed by the indispensable eliminated-space subtraction:
   

$$
\boxed{
   \begin{aligned}
   \delta_0&=\mathfrak u^2\det\mathsf H,\\
   \delta_1&=\mathfrak u^2\left(
      \varepsilon_0^2\det\mathsf H_{\partial}
      -3^{16}d_{\rm act}\det\mathsf H
   \right).
   \end{aligned}}
$$


   Here $\mathsf H_{\partial}$ is specified entrywise below. The common factor is a proved $3$-adic unit.

5. The required Hankel data have a prescribed evaluation from the complete functional and a fixed number of eliminated-space right-hand sides. A sufficient budget for all normalized data modulo $3^p$ is
   

$$
\boxed{R\bmod3^{p+10},}
$$


   hence, using the accepted Turn 9 producer theorem,
   

$$
\boxed{\text{producer input precision }3^{p+17}.}
$$


   The remaining determinants can still have growing order and unknown cancellation. This is not advertised as a constant-state algorithm in $n$.

The actual pair has therefore been reduced to a unit-sensitive Hankel/endpoint-kernel pair, with its full endpoint block retained and its normalization losses paid. The residual nonvanishing and relative valuation problem is **not solved**.

The irrationality or rationality of $e+\pi$ remains unresolved.

No tools were used.

---

## 1. Scope, accepted premises, and complete data

### 1.1 Original indices and finite boundaries

Retain


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$


and


$$
A=n-2=H-D,\qquad H=3^{h-1},\qquad0<D<H/972,
$$


with


$$
t=v_3(A)=1+v_3(j)\ge5.
$$



The spaces remain


$$
m=\frac{A+1}{2},\qquad
d=\frac{3D}{2}-1,\qquad
\nu=\frac D2-1,
$$




$$
U_a=(y-1)^a\quad(0\le a<D),
$$




$$
z_i=(y-1)^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m).
$$


Write $W=[U\ Y]$.

In particular,


$$
d=D+\nu,\qquad \deg z_i\le d-1.
$$


No coordinate beyond HIGH endpoint $m$ is introduced.

The depth-$16$ normalization is used only on the accepted sufficiently large original-index window


$$
j\equiv81\pmod{243},
\qquad
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad
C_{16}=512\cdot17^2\,3^{15}.
\tag{1.1}
$$


On this window $t=5$, and the accepted reduction is


$$
S_{\rm act}=-3^{16}\Psi,\qquad \Psi\in M_\nu(\mathbb Z_3).
\tag{1.2}
$$



### 1.2 Complete functional and actual producer

The functional is unchanged:


$$
\boxed{
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h
\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^r)=(2r)!.
}
\tag{1.3}
$$



The producer is


$$
Q_n^{\rm loc}=Q_c+3^6R,
\qquad
Q_c=(y+1)(y-1)^A(\beta+3y),
\qquad
\beta=-71-A,
$$


with


$$
R\in\mathbb Z_3[y],\qquad \deg R\le A+1.
$$



Set


$$
G_{\rm act}(f,g)=\mathcal M(Q_n^{\rm loc}fg).
$$



All constructions below use (1.3), including the factorial term, endpoint subtraction, and finite cutoff.

### 1.3 Source status

I reuse:

- Turn 8’s accepted finite propagation and eliminated-block results;
- its actual corrected-column congruence;
- its complete twenty-feature decomposition;
- its depth-$16$ reduction at (1.1);
- Turn 9’s scalar and producer-precision theorem, now accepted by A4 Turn 17.

In particular, with $F=(n-1)!$,


$$
\eta_n\equiv\chi_n\equiv3\pmod9,
\qquad
\xi_n=\chi_n/\eta_n\in1+3\mathbb Z_3,
$$


and


$$
\boxed{Q_n^{\rm loc}(-1)=-F^2\xi_n\ne0.}
\tag{1.4}
$$



The displacement and terminal formulas from Turn 10 were pending audit. The algebra needed here is verified explicitly below. The supplied finite receipts are not used to establish an original-family residual theorem.

The general companion, Bezoutian, and Hankel mechanisms used below are classical structured linear algebra. The contribution claimed here is the evaluation of their **actual arithmetic hypotheses and normalization** for the supplied residual pair.

---

## 2. The actual displacement and its finite endpoint

Let


$$
E=G_{\rm act}(W,W),\qquad
C=G_{\rm act}(W,Z),\qquad
K_{\rm elim}=E^{-1}C,
$$


and


$$
\widehat Z=Z-WK_{\rm elim}.
$$


Then


$$
S_{\rm act}=G_{\rm act}(\widehat Z,\widehat Z).
$$



The accepted block structure is


$$
E=
\begin{pmatrix}
3L&3X\\
3X^T&E_Y
\end{pmatrix},
\qquad
L,\quad \widehat E=E_Y-3X^TL^{-1}X
\in\operatorname{GL}(\mathbb Z_3).
\tag{2.1}
$$


The LOW part of $C$ is divisible by $3$, and indeed the complete mixed block $C$ is divisible by $3$ at the stated degree bounds. Thus $K_{\rm elim}$ is integral.

Define truncated multiplication on the actual polynomial space:


$$
\mathscr T f=yf-[y^m]f\,y^{m+1}.
$$


Put


$$
t(f)=[y^m]f,
$$


and


$$
\mathfrak r(f)=
\mathcal M\!\left(
Q_n^{\rm loc}y^{m+1}\bigl(f-t(f)y^m\bigr)
\right).
\tag{2.2}
$$



The argument of $\mathcal M$ has degree at most $2n-1$; hence (2.2) uses no moment beyond the original cutoff.

Expanding $\mathscr T$ proves


$$
G_{\rm act}(f,\mathscr Tg)-G_{\rm act}(\mathscr Tf,g)
=
t(f)\mathfrak r(g)-\mathfrak r(f)t(g).
\tag{2.3}
$$


The exterior highest moment cancels in this identity.

Let


$$
t_{\rm act}=t(\widehat Z),\qquad
r_{\rm act}=\mathfrak r(\widehat Z).
$$


In the original residual coordinates,


$$
\mathscr D=\mathscr C-e_0\ell^T,
\qquad
\ell^T=e_{U_{D-1}}^TK_{\rm elim}.
\tag{2.4}
$$


The row correction is exactly the last LOW return, because


$$
yU_{D-1}=U_{D-1}+z_0.
$$



Orthogonality to $W$ in (2.3) gives


$$
\boxed{
S_{\rm act}\mathscr D-\mathscr D^TS_{\rm act}
=
t_{\rm act}r_{\rm act}^T-r_{\rm act}t_{\rm act}^T.
}
\tag{2.5}
$$



This proof does not assume residual nonsingularity.

### 2.1 The complete endpoint block

Let $T_{WW},T_{WZ},T_{ZW},T_{ZZ}$ be the blocks of $\mathscr T$ in the original $[W,Z]$ basis. The eliminated-space block acting on corrected residual columns is


$$
\boxed{
B_{WZ}=T_{WZ}-T_{WW}K_{\rm elim}+K_{\rm elim}\mathscr D.
}
\tag{2.6}
$$



With


$$
w_-=W(-1),\qquad e_{\rm act}=\widehat Z(-1),
\qquad s=(-1)^{m+1},
$$


the exact endpoint identity is


$$
\boxed{
\mathscr D^Te_{\rm act}+B_{WZ}^Tw_-
=-e_{\rm act}-s\,t_{\rm act}.
}
\tag{2.7}
$$



The block $B_{WZ}$ will be transported, not deleted.

---

## 3. Actual first residues: the normalizing channel is a unit

This section supplies the arithmetic information that generic rank-two displacement does not provide.

### Lemma 3.1 — Actual LOW row and terminal residues

On the retained original domain,


$$
\boxed{
\ell_i\equiv
-3\binom d{D-1}\mathbf1_{i=\nu-1}\pmod9,
}
\tag{3.1}
$$




$$
\boxed{t_{\rm act}\equiv0\pmod9,}
\tag{3.2}
$$


and


$$
\boxed{r_{\rm act}\equiv e_{\nu-1}\pmod3.}
\tag{3.3}
$$



#### Proof

The accepted corrected-column formula is


$$
\widehat z_i^{\,c}
\equiv z_i-3\pi(y^d)\mathbf1_{i=\nu-1}\pmod9,
$$


where


$$
\pi(y^d)=y^d-\operatorname{rem}_{(y-1)^D}y^d.
$$


The actual correction to $K_{\rm elim}$ is divisible by $3^6$, so this remains valid for $\widehat z_i$ modulo $9$.

Writing


$$
\operatorname{rem}_{(y-1)^D}y^d
=\sum_{a=0}^{D-1}\binom da(y-1)^a
$$


gives (3.1). Since $d<m$, neither $z_i$ nor $\pi(y^d)$ has a $y^m$ term. This gives (3.2).

For (3.3), first note that $\mathfrak r$ is integral on the full bounded-degree coefficient space in question. At the original cutoff, the only denominator producing valuation zero in $\mathcal M$ is $3^h=3H$. The factorial term and every other pole vanish modulo $3$.

Also


$$
\widehat z_i\equiv z_i\pmod3.
$$


Thus it suffices to evaluate $\mathfrak r(z_i)$ modulo $3$. Put


$$
r_*=\frac{3H-1}{2}.
$$


Since $t(z_i)=0$, the top coefficient is


$$
[y^{r_*}](y-1)^H(\beta+3y)y^{m+1+i}.
$$


Modulo $3$, $\beta\equiv1$, and the required coefficient of $(y-1)^H$ is at index


$$
r_*-(m+1+i)=H+\nu-1-i.
$$


It is zero for $i<\nu-1$ and equals $1$ for $i=\nu-1$. This proves (3.3). ∎

The last coordinate of $r_{\rm act}$ is therefore a **proved actual unit**.

---

## 4. Determinant-one Krylov coordinates and the actual companion polynomial

Write


$$
\pi(y^d)=(y-1)^Dq_d(y),
\qquad
q_d(X)=X^\nu+\sum_{i=0}^{\nu-1}q_iX^i.
$$



Polynomial division at infinity gives the explicit coefficients


$$
\boxed{
q_i=\binom{D+\nu-i-1}{\nu-i}
\qquad(0\le i<\nu).
}
\tag{4.1}
$$



The companion action is


$$
\mathscr C e_i=e_{i+1}\quad(i<\nu-1),
\qquad
\mathscr C e_{\nu-1}=-\sum_{i=0}^{\nu-1}q_i e_i.
$$



Define


$$
p_0(X)=1,\qquad
p_{i+1}(X)=Xp_i(X)+\ell_i.
\tag{4.2}
$$


Then


$$
p_i(\mathscr D)e_0=e_i
\qquad(0\le i<\nu).
$$



The **actual final companion equation** is


$$
\mathscr D e_{\nu-1}
=-\sum_{i=0}^{\nu-1}q_i e_i-\ell_{\nu-1}e_0.
$$


Consequently define


$$
\boxed{
f(X)=p_\nu(X)+\sum_{i=0}^{\nu-1}q_i p_i(X).
}
\tag{4.3}
$$


It is monic of degree $\nu$, and


$$
f(\mathscr D)e_0=0.
$$



### Theorem 4.1 — Exact unit Krylov basis

Let


$$
\mathsf K=[e_0,\mathscr De_0,\ldots,\mathscr D^{\nu-1}e_0].
$$


Then


$$
\boxed{\det\mathsf K=1.}
\tag{4.4}
$$


Moreover, if $J$ is the companion matrix of $f$,


$$
\boxed{\mathscr D\mathsf K=\mathsf KJ.}
\tag{4.5}
$$



#### Proof

Each $p_i$ is monic of degree $i$. If $\mathsf P$ is the coefficient matrix whose $i$-th column is $p_i$, then $\mathsf P$ is upper triangular with diagonal entries $1$, and


$$
I=\mathsf K\mathsf P.
$$


Hence $\mathsf K=\mathsf P^{-1}$ and $\det\mathsf K=1$.

Equation (4.5) follows from the first $\nu-1$ Krylov shifts and the final relation (4.3). ∎

This is stronger than merely knowing that $e_0$ is cyclic: it incurs **no determinant normalization factor at all**.

By (3.1),


$$
\boxed{\mathsf K\equiv I\pmod9,}
\tag{4.6}
$$


and


$$
\boxed{
f(X)\equiv q_d(X)-3\binom d{D-1}\pmod9.
}
\tag{4.7}
$$



### 4.1 A genuine obstruction to a simple-root argument

Let $L=3^t$, and write


$$
D=2La_0,\qquad \nu=La_0-1.
$$


Then modulo $3$,


$$
\boxed{
f(X)\equiv
X^{L-1}
\left(
\sum_{r=0}^{a_0-1}
\binom{2a_0+r-1}{r}X^{a_0-1-r}
\right)^L.
}
\tag{4.8}
$$



Indeed, the coefficients of


$$
(1-z)^{-D}=(1-z)^{-2La_0}
$$


modulo $3$ occur only at exponents divisible by $L$, and Frobenius gives (4.8).

On the depth-$16$ window, $L=243$. Thus the actual companion polynomial has, modulo $3$, a zero root of multiplicity at least $242$, as well as the displayed Frobenius multiplicities.

So an argument requiring an étale companion algebra, distinct roots modulo $3$, or a unit discriminant is unavailable. Cyclicity does not repair this obstruction.

---

## 5. Division-safe normalization of the displacement

Work now on the accepted depth-$16$ window. Since $r_{\nu-1}$ is a unit, define


$$
\theta=\frac{(t_{\rm act})_{\nu-1}}{(r_{\rm act})_{\nu-1}},
$$


and


$$
\boxed{
a=\frac{t_{\rm act}-\theta r_{\rm act}}{3^{16}}.
}
\tag{5.1}
$$



### Lemma 5.1

The vector $a$ is integral, and $a_{\nu-1}=0$. Moreover,


$$
\boxed{
\Psi\mathscr D-\mathscr D^T\Psi
=
r_{\rm act}a^T-a r_{\rm act}^T.
}
\tag{5.2}
$$



#### Proof

The $(i,\nu-1)$ entry of (2.5), together with $S_{\rm act}=-3^{16}\Psi$, shows


$$
(t_{\rm act})_i(r_{\rm act})_{\nu-1}
-(r_{\rm act})_i(t_{\rm act})_{\nu-1}
\in3^{16}\mathbb Z_3.
$$


Division by the unit $(r_{\rm act})_{\nu-1}$ proves the integrality in (5.1).

Substitute


$$
t_{\rm act}=\theta r_{\rm act}+3^{16}a
$$


into (2.5), and cancel the common factor with its sign. ∎

The division by $3^{16}$ is justified for the **whole sheared vector**. No separate divisibility of the original outer products is asserted.

Also, (3.2) gives


$$
\theta\in9\mathbb Z_3.
\tag{5.3}
$$



---

## 6. The actual normalizing resultant is a unit

Put


$$
H_0=\mathsf K^T\Psi\mathsf K,\qquad
r_0=\mathsf K^Tr_{\rm act},\qquad
a_0=\mathsf K^Ta.
$$


Then


$$
H_0J-J^TH_0=r_0a_0^T-a_0r_0^T.
\tag{6.1}
$$



Let $\mathsf B_f$ be the coefficient matrix of


$$
\frac{f(X)-f(Y)}{X-Y}.
$$


Thus


$$
\frac{f(X)-f(Y)}{X-Y}
=\sum_{i,j=0}^{\nu-1}(\mathsf B_f)_{ij}X^iY^j.
$$



Direct coefficient comparison gives


$$
J\mathsf B_f=\mathsf B_fJ^T,
\tag{6.2}
$$




$$
\det\mathsf B_f=(-1)^{\nu(\nu-1)/2},
\qquad
\mathsf B_fe_{\nu-1}=e_0.
\tag{6.3}
$$



Define the **actual generating polynomial**


$$
\boxed{
\mathsf R(X)=
\sum_{i=0}^{\nu-1}(\mathsf B_fr_0)_iX^i.
}
\tag{6.4}
$$


This $\mathsf R$ is not the producer correction $R(y)$.

### Theorem 6.1 — Actual unit-resultant theorem

Throughout the retained original domain,


$$
\boxed{\mathsf R(X)\equiv1\pmod3,}
\tag{6.5}
$$


and hence


$$
\boxed{
\mathfrak u=\operatorname{Res}(f,\mathsf R)
=\det\mathsf R(J)\in1+3\mathbb Z_3.
}
\tag{6.6}
$$



#### Proof

By (3.3) and (4.6),


$$
r_0\equiv e_{\nu-1}\pmod3.
$$


Equation (6.3) therefore gives


$$
\mathsf B_fr_0\equiv e_0\pmod3,
$$


which is precisely (6.5).

Thus $\mathsf R(J)\equiv I\pmod3$. Its determinant is a unit congruent to $1$. For monic $f$, this determinant is the displayed resultant. ∎

This proves the needed coprimality for the **actual normalizer**, rather than assuming it.

It does **not** prove that $\Psi$ is invertible.

---

## 7. An integral Hankel transfer of the whole residual pair

Define


$$
\mathsf U=\mathsf R(J)^{-1},
\qquad
\mathsf V=\mathsf K\mathsf U.
\tag{7.1}
$$


Then


$$
\mathsf V\in\operatorname{GL}_\nu(\mathbb Z_3),
\qquad
\mathsf V\equiv I\pmod3,
\qquad
\det\mathsf V=\mathfrak u^{-1}.
\tag{7.2}
$$



No unproved inverse occurs: $\mathsf R(J)\equiv I\pmod3$.

The identity


$$
r_0=\mathsf R(J^T)e_{\nu-1}
$$


follows from (6.2)–(6.4). Therefore


$$
\mathsf U^Tr_0=e_{\nu-1}.
$$



Set


$$
\boxed{
\mathsf H=\mathsf V^T\Psi\mathsf V,\qquad
b=\mathsf V^Ta.
}
\tag{7.3}
$$


Then


$$
\boxed{
\mathsf HJ-J^T\mathsf H
=e_{\nu-1}b^T-be_{\nu-1}^T.
}
\tag{7.4}
$$



### Theorem 7.1 — Actual integral Hankel law

The matrix $\mathsf H$ is Hankel:


$$
\boxed{
\mathsf H_{ij}=\mu_{i+j}
\qquad(0\le i,j<\nu)
}
\tag{7.5}
$$


for integral moments


$$
\mu_0,\ldots,\mu_{2\nu-2}.
$$



#### Proof

For $0\le i,j\le\nu-2$, the right side of (7.4) is zero. The first $\nu-1$ companion columns give


$$
\mathsf H_{i,j+1}=\mathsf H_{i+1,j}.
$$


These are all adjacent equalities along the anti-diagonals of a square symmetric matrix. Hence (7.5). Integrality follows from (7.2) and $\Psi\in M_\nu(\mathbb Z_3)$. ∎

### 7.1 The actual last-column equations

Write


$$
f(X)=X^\nu+\sum_{k=0}^{\nu-1}f_kX^k.
$$


The $(i,\nu-1)$ entries of (7.4) give


$$
\boxed{
\mu_{i+\nu}
+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}
=b_i,
\qquad 0\le i\le\nu-2.
}
\tag{7.6}
$$



The final equation, at $i=\nu-2$, determines $\mu_{2\nu-2}$. The diagonal entry $(\nu-1,\nu-1)$ is the required identity $0=0$; it does not furnish an additional moment.

No $\mu_{2\nu-1}$ is being declared an actual exterior moment. In particular, (7.6) does not extend HIGH beyond $m$.

Thus the full Hankel matrix is determined by:

- the actual monic polynomial $f$;
- the first $\nu$ moments $\mu_0,\ldots,\mu_{\nu-1}$;
- the actual forcing entries $b_0,\ldots,b_{\nu-2}$.

The forcing is not dropped.

---

## 8. Complete endpoint transport and an endpoint-kernel Gram law

Define


$$
\varepsilon=\mathsf V^Te_{\rm act},
\qquad
\omega=(B_{WZ}\mathsf V)^Tw_-.
\tag{8.1}
$$



Since $\mathsf V$ intertwines $\mathscr D$ and $J$, equation (2.7) becomes


$$
\boxed{
J^T\varepsilon+\omega
=-\varepsilon-s\bigl(\theta e_{\nu-1}+3^{16}b\bigr).
}
\tag{8.2}
$$



Here


$$
\mathsf V^Tt_{\rm act}
=\theta e_{\nu-1}+3^{16}b
$$


was used exactly.

### 8.1 Interior recurrence and final companion equation

For $0\le i<\nu-1$,


$$
\boxed{
\varepsilon_{i+1}
=-\varepsilon_i-\omega_i-s\,3^{16}b_i.
}
\tag{8.3}
$$



At the actual last companion column,


$$
\boxed{
-\sum_{i=0}^{\nu-1}f_i\varepsilon_i
=
-\varepsilon_{\nu-1}
-\omega_{\nu-1}
-s\bigl(\theta+3^{16}b_{\nu-1}\bigr).
}
\tag{8.4}
$$



Both $\omega_{\nu-1}$ and the terminal charge $\theta$ remain present.

For a polynomial form of the closure, put


$$
h_i=\omega_i+s\,3^{16}b_i+s\theta\mathbf1_{i=\nu-1},
\qquad f_\nu=1.
$$


Then


$$
\boxed{
f(-1)\varepsilon_0
=
\sum_{k=0}^{\nu-1}
\left(
\sum_{i=k+1}^{\nu}f_i(-1)^{i-1-k}
\right)h_k.
}
\tag{8.5}
$$


This is an identity, not a license to divide by $f(-1)$.

### 8.2 Every transformed endpoint coordinate is a unit

Because $K_{\rm elim}\equiv0\pmod3$,


$$
(e_{\rm act})_i
\equiv z_i(-1)
=(-2)^D(-1)^i
\equiv(-1)^i\pmod3.
$$


Since $\mathsf V\equiv I\pmod3$,


$$
\boxed{\varepsilon_i\equiv(-1)^i\pmod3.}
\tag{8.6}
$$



Thus define, without any nonunit division,


$$
\lambda_i=\frac{\varepsilon_{i+1}}{\varepsilon_i}
\in-1+3\mathbb Z_3,
\qquad 0\le i\le\nu-2.
\tag{8.7}
$$



Let


$$
\phi_i(X)=X^{i+1}-\lambda_iX^i.
$$


The endpoint functional with values $\varepsilon_j$ annihilates every $\phi_i$.

Define the $(\nu-1)\times(\nu-1)$ matrix


$$
\boxed{
(\mathsf H_{\partial})_{ij}
=
\mu_{i+j+2}
-(\lambda_i+\lambda_j)\mu_{i+j+1}
+\lambda_i\lambda_j\mu_{i+j},
}
\tag{8.8}
$$


for $0\le i,j\le\nu-2$.

### Theorem 8.1 — Complete distinguished-cofactor transfer

Put


$$
c_{\partial}=3^{16}d_{\rm act}.
$$


Then


$$
\boxed{
\begin{aligned}
\delta_0
&=\mathfrak u^2\det\mathsf H,\\
\delta_1
&=\mathfrak u^2
\left(
\varepsilon_0^2\det\mathsf H_{\partial}
-c_{\partial}\det\mathsf H
\right).
\end{aligned}}
\tag{8.9}
$$



These identities hold whether or not either matrix is singular.

#### Proof

The first follows from $\mathsf H=\mathsf V^T\Psi\mathsf V$ and $\det\mathsf V=\mathfrak u^{-1}$.

The basis


$$
1,\phi_0,\ldots,\phi_{\nu-2}
$$


has triangular coefficient matrix with diagonal $1$, hence determinant $1$. In this basis the endpoint vector is


$$
(\varepsilon_0,0,\ldots,0)^T,
$$


and the lower-right Gram block is $\mathsf H_{\partial}$. Therefore


$$
\varepsilon^T\operatorname{adj}(\mathsf H)\varepsilon
=\varepsilon_0^2\det\mathsf H_{\partial}.
$$


Congruence transformation of the adjugate contraction, or the corresponding bordered determinant identity, gives (8.9). No inverse of $\mathsf H$ is required. ∎

### 8.3 An evaluated actual relative residue law

The block inverse bound gives


$$
d_{\rm act}\in3^{-1}\mathbb Z_3,
\qquad c_{\partial}\in3^{15}\mathbb Z_3.
$$


Using $\mathfrak u\equiv1$, $\varepsilon_0\equiv1$, and $\lambda_i\equiv-1$, equation (8.9) yields


$$
\boxed{
\delta_0\equiv
\det(\mu_{i+j})_{0\le i,j<\nu}\pmod3,
}
\tag{8.10}
$$




$$
\boxed{
\delta_1\equiv
\det\bigl(
\mu_{i+j+2}-\mu_{i+j+1}+\mu_{i+j}
\bigr)_{0\le i,j<\nu-1}
\pmod3.
}
\tag{8.11}
$$



This is a uniform theorem on the original window. It does not assert that either displayed determinant is nonzero.

At higher precision, the varying units $\lambda_i$ and the entire subtraction $c_{\partial}\det\mathsf H$ must be retained. Replacing them permanently by their first residues would lose the actual pair.

---

## 9. Evaluation of the additional actual data

The new theorem requires more than the terminal $g,k$ from Turn 10. The necessary extra objects are:

- the full last-LOW return row $\ell$;
- the complete generator $r_{\rm act}$;
- the endpoint return $e_{\rm act},d_{\rm act}$;
- one residual seed pairing for the first Hankel row;
- the normalized sheared generator $a$.

They can be evaluated without a residual inverse.

### 9.1 Complete evaluation of $r_{\rm act}$

Form the finite vectors


$$
r_W=\mathfrak r(W),\qquad r_Z=\mathfrak r(Z).
$$


The LOW part of $r_W$ is divisible by $3$: its top pole is absent by the original degree bound. Hence


$$
s_r=E^{-1}r_W
$$


is integral and is computed by the normalized LOW/HIGH solve.

Then


$$
\boxed{r_{\rm act}=r_Z-C^Ts_r.}
\tag{9.1}
$$



This uses one actual adjoint return. It includes the factorial functional and the complete finite pole sum.

### 9.2 Last-LOW return

Let $e_L$ select the actual last LOW coordinate $U_{D-1}$. Compute the integral vector


$$
\sigma_L=3E^{-1}e_L.
$$


Since $C/3$ is integral,


$$
\boxed{\ell=(C/3)^T\sigma_L.}
\tag{9.2}
$$


There is no loss from an unnormalized LOW inverse in this formula.

### 9.3 Endpoint and eliminated contraction

Compute


$$
\sigma_-=3E^{-1}w_-.
$$


Then


$$
\boxed{
e_{\rm act}=Z(-1)-(C/3)^T\sigma_-,
}
\tag{9.3}
$$


and


$$
\boxed{
c_{\partial}
=3^{15}w_-^T\sigma_-.
}
\tag{9.4}
$$



Equation (9.4), rather than a premature division followed by cancellation, is the integral form of the full eliminated contribution.

### 9.4 First Hankel row from one residual seed

Let


$$
v_0=\mathsf V e_0.
$$


Compute


$$
\varphi_0=Zv_0-WE^{-1}Cv_0.
\tag{9.5}
$$


This requires one more actual eliminated-space right-hand side.

For $0\le i<\nu$,


$$
\mathsf V e_i=\mathscr D^iv_0,
$$


because $\mathsf VJ=\mathscr D\mathsf V$ and $J^ie_0=e_i$. Orthogonality of $\varphi_0$ to $W$ therefore gives


$$
\boxed{
\mu_i
=
-\frac1{3^{16}}\,
G_{\rm act}\!\left(
\varphi_0,\,
Z\mathscr D^iv_0
\right),
\qquad0\le i<\nu.
}
\tag{9.6}
$$



One may first evaluate the single row $G_{\rm act}(\varphi_0,Z)$, and then apply the structured coordinate transforms. It is unnecessary to construct every corrected residual polynomial.

The whole numerator in (9.6) is divisible by $3^{16}$, by the accepted residual theorem. The remaining moments follow from the monic recurrence (7.6), with no further precision loss.

### 9.5 Terminal input used in the shearing precision

For completeness, the Turn 10 terminal identities needed for the precision budget follow from the actual terminal representer


$$
\rho=Y\widehat E^{-1}e_m-U L^{-1}X\widehat E^{-1}e_m.
$$


It satisfies


$$
G_{\rm act}(U,\rho)=0,\qquad
G_{\rm act}(Y_b,\rho)=\mathbf1_{b=m}.
$$



Using the accepted terminal cancellations gives


$$
g=\frac{(\widehat E^{-1})_{mm}}9\in\mathbb Z_3,
\qquad
k=\frac{K(\widehat Z^{\,c},\rho)}{27}\in\mathbb Z_3^\nu,
$$


and exactly


$$
\boxed{t_{\rm act}=t_c-3^9k.}
\tag{9.7}
$$



The division-safe form is


$$
\boxed{
k=\frac19\left(
\frac{K(Z,\rho)}3
-(C_c/3)^TE_c^{-1}K(W,\rho)
\right).
}
\tag{9.8}
$$


The maps inside parentheses are integral on their full bounded-degree spaces. Thus $k\bmod3^q$ requires $R\bmod3^{q+2}$, as asserted in Turn 10.

The terminal boundary features remain


$$
\tau=c_R^2g,\qquad
\gamma=-c_Rk-\tau e_{\nu-1},
\qquad c_R=[y^{A+1}]R.
\tag{9.9}
$$



---

## 10. Precision theorem and retention of all twenty features

### Theorem 10.1 — Sufficient normalized-data precision

Fix $p\ge1$. On the accepted depth-$16$ window, the data


$$
f,\ \mathsf R,\ \mathfrak u,\ b,\ 
\mu_0,\ldots,\mu_{2\nu-2},\
\varepsilon,\ \lambda_i,\ c_{\partial}
$$


are determined modulo $3^p$ from


$$
\boxed{R\bmod3^{p+10}}
\tag{10.1}
$$


and exact core data evaluated to the indicated finite working precision.

A sufficient producer-input modulus is


$$
\boxed{3^{p+17}.}
\tag{10.2}
$$



#### Precision proof

There are three distinct losses.

**1. Integral actual block data.**  
The normalized LOW maps, the ordinary HIGH maps, $C/3$, and the return formulas (9.1)–(9.4) use integral operations. A change


$$
R\mapsto R+3^q\Delta R
$$


changes their actual producer-dependent data by at least $3^{q+6}$. This uses the complete normalized degree bounds, not an omitted-pole approximation.

**2. The sheared generator.**  
To compute $a\bmod3^p$, its whole numerator in (5.1) is needed modulo $3^{p+16}$.

By (9.7), the producer-dependent part of $t_{\rm act}$ is $3^9k$. Thus $k\bmod3^{p+7}$, and hence


$$
R\bmod3^{p+9},
$$


suffices for $t_{\rm act}\bmod3^{p+16}$.

Because $t_{\rm act}\in9\mathbb Z_3^\nu$, computing


$$
t_i-t_{\nu-1}\frac{r_i}{r_{\nu-1}}
$$


only requires $r_{\rm act}\bmod3^{p+14}$. Formula (9.1) obtains this from $R\bmod3^{p+8}$. Thus the shearing requires at most $p+9$ digits of $R$.

**3. The normalized seed row.**  
Formula (9.6) divides a whole residual pairing by $3^{16}$. Its raw value must therefore be known modulo $3^{p+16}$. Actual normalized block data and raw residual Schur pairings depend on $R$ with the factor $3^6$, so


$$
R\bmod3^{p+10}
$$


suffices.

The remaining steps use only:

- determinant-one triangular transformations;
- inversion of $\mathsf R(J)\equiv I\pmod3$;
- unit divisions by endpoint coordinates;
- the monic recurrence (7.6).

They lose no further digits. Finally, the accepted producer theorem supplies $R\bmod3^{p+10}$ from input precision $3^{p+17}$. ∎

For $\mathsf R(J)^{-1}\bmod3^P$, the explicitly bounded expansion


$$
\sum_{j=0}^{P-1}\bigl(I-\mathsf R(J)\bigr)^j
$$


suffices. The LOW and HIGH inverse returns likewise use the finite reference convolutions and $P$-term expansions supplied in Turn 10. All output HIGH indices remain $d,\ldots,m$.

The theorem does not assert that a fixed $p$ detects the first nonzero determinant digit.

### 10.1 All twenty boundary features remain present

On window (1.1), $\kappa_3=9$, so the accepted feature list has twenty slots:


$$
\mathcal F=
\begin{pmatrix}
\alpha\\
\zeta\\
v^T\\
\gamma^T
\end{pmatrix},
\qquad
\mathcal J=
\begin{pmatrix}
J_{\rm low}&I_9&0&0\\
I_9&0&0&0\\
0&0&\tau&1\\
0&0&1&0
\end{pmatrix}.
$$


The exact identity


$$
\Psi=\mathcal A+\mathcal F^T\mathcal J\mathcal F
$$


becomes


$$
\boxed{
\mathsf H
=
\mathsf V^T\mathcal A\mathsf V
+
(\mathcal F\mathsf V)^T\mathcal J(\mathcal F\mathsf V).
}
\tag{10.3}
$$



Thus the transfer retains every boundary feature, the HIGH bulk, the LOW tail, and the complete core and linear-force terms. Hankel structure is proved for their **whole sum**. No feature is discarded because of its rank or its first residue.

---

## 11. Structured determinant recurrence and the exact remaining radical problem

The preceding result is more than a formal determinant ratio: it proves that the actual normalizer is a unit, identifies the actual Hankel moments and forcing, and proves every endpoint coordinate is a unit. It does not evaluate all growing Hankel determinants.

### 11.1 A structured Schur recurrence when its pivots exist

Let $\mathcal L(X^k)=\mu_k$. Suppose, for a given initial range, the monic orthogonal polynomials $P_i$ exist with nonzero norms


$$
h_i=\mathcal L(P_i^2).
$$


They are generated by the standard three-term recurrence, using the actual moments. Define the actual endpoint charges


$$
E_i=\varepsilon(P_i).
$$



For


$$
\Delta_i=\det(\mu_{a+b})_{0\le a,b<i},
$$


and


$$
\Gamma_i=
\varepsilon_{<i}^T
\operatorname{adj}(\mathsf H_i)
\varepsilon_{<i}
-c_{\partial}\Delta_i,
$$


the exact recurrence is


$$
\boxed{
\begin{aligned}
\Delta_0&=1,&\Gamma_0&=-c_{\partial},\\
\Delta_{i+1}&=h_i\Delta_i,&
\Gamma_{i+1}&=h_i\Gamma_i+E_i^2\Delta_i.
\end{aligned}}
\tag{11.1}
$$



This recurrence propagates the **complete** bordered quantity, including its original subtraction. It does not replace its valuation by the minimum of the valuations of separate summands.

Zero pivots require look-ahead blocks or fraction-free determinant calculations. There is no theorem here that the scalar pivots are all nonzero. Accordingly, (11.1) is an evaluation recurrence at its stated pivot scope, not a nonvanishing proof.

### 11.2 An unconditional finite radical description

Let


$$
M_\mu(X)=\sum_{k=0}^{2\nu-2}\mu_kX^k.
$$


For $x=(x_0,\ldots,x_{\nu-1})^T$, define


$$
x^\vee(X)=\sum_{j=0}^{\nu-1}x_jX^{\nu-1-j}.
$$


Then


$$
\boxed{
x\in\ker\mathsf H
\iff
[X^{\nu-1+i}]\,M_\mu(X)x^\vee(X)=0
\quad(0\le i<\nu).
}
\tag{11.2}
$$



The actual endpoint on this radical is


$$
\varepsilon(x)=\sum_{j=0}^{\nu-1}\varepsilon_jx_j.
$$



Consequently:

- if $\operatorname{corank}\mathsf H\ge2$, both $\delta_0$ and $\delta_1$ vanish;
- if $\operatorname{corank}\mathsf H=1$, then $\delta_0=0$, and $\delta_1\ne0$ exactly when the endpoint does not annihilate the one-dimensional radical;
- if $\mathsf H$ is nonsingular, the remaining distinguished scalar is the whole expression in (8.9).

These are exact classifications after the actual moment kernel is evaluated. They do not evaluate that kernel on the infinite original window.

### 11.3 Why the present normalizer theorem cannot imply residual nonvanishing

Every Hankel matrix, including singular ones, satisfies a displacement of the form


$$
HJ-J^TH=e_{\nu-1}b^T-be_{\nu-1}^T
$$


for suitable final-column forcing whenever the relevant recurrence is imposed. Thus a unit generator and a cyclic companion do not force its determinant to be nonzero.

For the present problem, the actual missing arithmetic is concentrated in


$$
\boxed{
\det\mathsf H,\qquad
\varepsilon_0^2\det\mathsf H_{\partial}
-c_{\partial}\det\mathsf H.
}
\tag{11.3}
$$



Neither the repeated-root companion factorization (4.8) nor the unit normalizer determines this pair.

### Concrete follow-on lemma

The next useful obligation is:

> **Actual Hankel–endpoint relative-minor lemma.**  
> Evaluate the finite moment sequence defined by (9.6) and (7.6), with the actual $f,b,\varepsilon,\omega$, and prove either:
> 
> 1. nonvanishing and a sufficiently strong uniform law for
>    

$$
>    v_3\!\left(
>      \varepsilon_0^2\det\mathsf H_{\partial}
>      -c_{\partial}\det\mathsf H
>    \right)-v_3(\det\mathsf H);
>
$$


>    or
> 2. an exact radical theorem through (11.2), including the endpoint action on that radical.
>
> The proof must use the actual initial moments and forcing. The companion polynomial and its unit normalizer alone are insufficient.

The new result makes this a normalized moment problem with **no hidden resultant loss**.

---

## 12. Same archived approximant, full primitive normalization, and whole error

The transformations above do not construct a new rational approximant. They preserve exactly the A1 Turn 8/Turn 9 determinant approximant. Their purpose is to expose its unresolved arithmetic in a better normalized form.

When $\delta_0\ne0$, the accepted ratio remains


$$
\frac{\beta_1}{\beta_0}
=
\frac{3^{h-16}F^2\xi_n}{4}
\frac{\delta_1}{\delta_0}.
$$


Using (8.9),


$$
\boxed{
\frac{\beta_1}{\beta_0}
=
\frac{3^{h-16}F^2\xi_n}{4}
\frac{
\varepsilon_0^2\det\mathsf H_{\partial}
-c_{\partial}\det\mathsf H
}{
\det\mathsf H
}.
}
\tag{12.1}
$$



The common resultant factor cancels exactly. It supplies no artificial denominator gain.

If both members of the actual pair are nonzero,


$$
\boxed{
v_3(q)=
\max\!\left\{
0,\,
h-16+2v_3(F)
+
v_3\!\left(
\varepsilon_0^2\det\mathsf H_{\partial}
-c_{\partial}\det\mathsf H
\right)
-v_3(\det\mathsf H)
\right\}.
}
\tag{12.2}
$$



The valuation in the middle is of the **whole difference**.

Restore


$$
Q_n=\lambda Q_n^{\rm loc},
\qquad
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



Let $\ell_{\rm clr}$ be the least actual clearing integer required by the original normalization, and let $k_0=m+1$. Put


$$
A_{\ell}=\ell_{\rm clr}^{k_0}\beta_0,\qquad
B_{\ell}=\ell_{\rm clr}^{k_0}\beta_1,
$$


and preserve the all-prime gcd


$$
\boxed{g_{\ell}=\gcd(|A_{\ell}|,|B_{\ell}|).}
\tag{12.3}
$$



When $B_{\ell}\ne0$,


$$
q=\frac{|B_{\ell}|}{g_{\ell}},
\qquad
p=-\frac{\operatorname{sgn}(B_{\ell})A_{\ell}}{g_{\ell}}.
$$


The whole evaluated error is


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_{\ell})
      \ell_{\rm clr}^{k_0}}{g_{\ell}}
\det H_{\rm complete}.
}
\tag{12.4}
$$



The resultant $\mathfrak u$ is proved to be a unit at $3$, not at every prime. Nothing in the Hankel transfer determines the least clearer, the full gcd, or the nonvanishing and decay of (12.4).

The supplied archive contains no proved global denominator/error estimate for this A1 approximant that closes those obligations. I therefore do not replace them by an unverified obstruction from another construction.

---

## 13. Bounded exact arithmetic for personal inspection

No finite calculation is required for the symbolic theorems above. A small synthetic calculation can inspect the new Krylov, resultant, Hankel, and complete-cofactor algebra.

It must not be represented as evidence for actual original-family divisibility.

### 13.1 Explicit synthetic inputs

Take residual order $3$, with


$$
q(X)=X^3+8X^2+36X+120,
\qquad
\ell=(9,18,-3)^T,
$$


and


$$
\mathscr D=\mathscr C_q-e_0\ell^T.
$$



Equations (4.2)–(4.3) give


$$
p_0=1,\quad p_1=X+9,\quad p_2=X^2+9X+18,
$$




$$
\boxed{f(X)=X^3+17X^2+126X+585.}
$$



The exact Krylov matrix is


$$
\boxed{
\mathsf K=
\begin{pmatrix}
1&-9&63\\
0&1&-9\\
0&0&1
\end{pmatrix}.
}
$$



Choose


$$
\mathsf R(X)=1+3X,
\qquad
\mathsf U=(I+3J)^{-1},
\qquad
\mathsf V=\mathsf K\mathsf U.
$$



Use the Hankel moments


$$
(\mu_0,\mu_1,\mu_2,\mu_3,\mu_4)=(1,2,5,14,42),
$$


so


$$
\mathsf H=
\begin{pmatrix}
1&2&5\\
2&5&14\\
5&14&42
\end{pmatrix}.
$$


Set


$$
\varepsilon=(1,-1,1)^T,\qquad
c_{\partial}=3^{15}.
$$



Construct


$$
\Psi=\mathsf V^{-T}\mathsf H\mathsf V^{-1},
\qquad
e=\mathsf V^{-T}\varepsilon.
$$



### 13.2 Expected verifiable output

The exact calculation should report:

1. $\det\mathsf K=1$ and
   

$$
\mathscr D\mathsf K-\mathsf KJ=0.
$$



2. The actual resultant for this synthetic input:
   

$$
\boxed{
   \operatorname{Res}(f,1+3X)=-14711\equiv1\pmod3.
   }
$$



3. $\det\mathsf H=1$.

4. Since both endpoint ratios are $-1$,
   

$$
\mathsf H_{\partial}
   =
   \begin{pmatrix}
   10&26\\
   26&75
   \end{pmatrix},
   \qquad
   \boxed{\det\mathsf H_{\partial}=74.}
$$



5. Exact agreement of the complete pair:
   

$$
\boxed{\det\Psi=14711^2,}
$$


   

$$
\boxed{
   e^T\operatorname{adj}(\Psi)e
   -3^{15}\det\Psi
   =
   14711^2(74-3^{15}).
   }
$$



6. The final-column forcing for the Hankel displacement can be taken as
   

$$
b=(936,2080,0)^T,
$$


   and the zero matrix
   

$$
\mathsf HJ-J^T\mathsf H
   -e_2b^T+be_2^T
$$


   should be reported.

This is a bounded exact check of the new algebra and signs. It does not test the actual producer, the original index cylinder, the depth-$16$ divisibility, or the original endpoint block $B_{WZ}$. Those remain governed by the symbolic arguments and accepted original-family hypotheses.

---

## 14. Proof-status ledger and closing bottleneck

| Statement | Status |
|---|---|
| Turn 9 $\eta/\chi$, endpoint, and producer-precision theorem | Accepted by A4 Turn 17 |
| Full finite displacement and endpoint block | Verified algebraically here |
| Actual $r_{\rm act}\equiv e_{\nu-1}\pmod3$ | Proved here from the complete functional |
| Actual LOW-row residue and $t_{\rm act}\in9\mathbb Z_3^\nu$ | Derived from accepted corrected columns |
| Krylov determinant exactly $1$ | Proved here |
| Actual companion polynomial, including final equation | Explicitly derived |
| Repeated-root factorization of $f\bmod3$ | Proved here |
| Actual normalizing resultant in $1+3\mathbb Z_3$ | Proved here |
| Integral Hankel transfer of the whole $\Psi$ | Proved here |
| Complete endpoint transport with $B_{WZ}$ | Retained and transformed exactly |
| Every transformed endpoint coordinate is a unit | Proved here |
| Complete endpoint-kernel cofactor identity | Proved without nonsingularity assumptions |
| All twenty boundary features | Retained under the exact congruence |
| $R\bmod3^{p+10}$ sufficient for normalized data modulo $3^p$ | Proved sufficient budget |
| Residual determinant/cofactor nonvanishing | Unresolved |
| Uniform relative valuation on the infinite original window | Unresolved |
| Least clearer, full gcd, and whole-error decay | Unresolved |

### New result

The actual residual pair now has a normalization with **proved unit arithmetic**:


$$
\boxed{
\Psi
\ \xrightarrow[\det=1]{\text{actual Krylov}}
\ H_0
\ \xrightarrow[\operatorname{Res}(f,\mathsf R)\in1+3\mathbb Z_3]
{\text{actual generator normalization}}
\ \mathsf H\ \text{Hankel}.
}
$$



Its distinguished endpoint is not replaced by a terminal coefficient channel. It is transported through the complete block $B_{WZ}$, and its unit coordinates yield the exact endpoint-kernel Gram matrix (8.8).

### Exact remaining bottleneck

What is still needed is an arithmetic theorem for the **actual evaluated Hankel moments and complete forcing** that determines


$$
\det\mathsf H
\quad\text{and}\quad
\varepsilon_0^2\det\mathsf H_{\partial}
-c_{\partial}\det\mathsf H,
$$


including their nonvanishing and relative valuation on the infinite original window.

The normalizing resultant is no longer an unknown denominator. The residual Hankel determinants still are.

After that local problem, the full all-prime primitive normalization and the whole same-index error (12.4) remain indispensable global obligations.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


