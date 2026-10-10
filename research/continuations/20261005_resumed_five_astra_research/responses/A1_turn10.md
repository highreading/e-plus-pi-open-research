> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1, Turn 10 — Evaluation of the actual terminal channel and displacement of the full residual form

## Executive conclusion

The determinant/cofactor nonvanishing problem is **not resolved** in this report. I do obtain a narrower result that evaluates the actual terminal channel, including its LOW return, without assuming that the growing residual bulk is invertible.

The principal new results are:

1. **An exact terminal-channel reduction.**  
   A single actual terminal dual polynomial $\rho$, defined in the original eliminated space $W=[U\ Y]$, determines both terminal features in the accepted twenty-feature decomposition. Put
   

$$
g=\frac{(\widehat E_{\rm act}^{-1})_{mm}}9,
   \qquad
   k=\frac{K(\widehat Z^{\,c},\rho)}{27}.
$$


   Then $g\in\mathbb Z_3$, $k\in\mathbb Z_3^\nu$, and the old terminal features satisfy the exact identities
   

$$
\boxed{\tau=c^2g,\qquad \gamma=-ck-\tau v,}
$$


   where $c=[y^{A+1}]R$ and $v=e_{\nu-1}$.

   Thus the previous combination of a next HIGH force, an inverse correction, and a lower-boundary return can be evaluated through **one true terminal representer and one core adjoint return**. No inverse of the residual bulk occurs.

2. **A certified two-digit terminal precision bound.**  
   To compute $g,k,\tau,\gamma\bmod3^p$, it suffices to know the actual producer correction
   

$$
R\bmod3^{p+2}.
$$


   With the supplied Turn 9 producer formula, a sufficient producer-input precision is therefore
   

$$
\boxed{3^{p+9}.}
$$


   This bound is independent of any cancellation in the residual determinant. The computation uses explicitly specified finite LOW and HIGH convolution returns and terminates after a prescribed number of terms.

3. **A full-residual displacement identity.**  
   On the original residual space—not an enlarged space and not a selected subspace—the actual Schur complement satisfies
   

$$
\boxed{
   S_{\rm act}\mathscr D-\mathscr D^TS_{\rm act}
   =t_{\rm act}r_{\rm act}^T-r_{\rm act}t_{\rm act}^T,
   }
$$


   where
   

$$
\mathscr D=\mathscr C-e_0\ell^T
$$


   is a concrete companion matrix with one actual LOW-return row correction. Moreover,
   

$$
\boxed{t_{\rm act}=t_c-3^9k.}
$$


   The newly evaluable vector $k$ is therefore not merely an auxiliary border feature: it is the exact actual correction to a displacement generator of the whole residual form.

These results advance the actual nonlinear structure. They do **not** establish


$$
\delta_0\ne0,\qquad \delta_1\ne0,
$$


or a uniform law for


$$
v_3(\delta_1)-v_3(\delta_0).
$$



The remaining local bottleneck is now precise: the full residual displacement data must be converted into a nonvanishing and relative-cofactor theorem, with its actual endpoint retained. A bounded-precision terminal-channel calculation does not, by itself, supply that theorem.

No tools were used.

---

# 1. Scope and source status

Retain the original family


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$


and


$$
A=n-2=H-D,\qquad H=3^{h-1},\qquad 0<D<H/972,
$$


with


$$
t=v_3(A)=1+v_3(j)\ge5.
$$



The finite dimensions and coordinates are unchanged:


$$
m=\frac{A+1}{2},\qquad
d=\frac{3D}{2}-1,\qquad
\nu=\frac D2-1,
$$




$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),\qquad
Y_b=y^b\quad(d\le b\le m),
$$


where $x=y-1$.

In particular,


$$
\deg z_i\le d-1,\qquad i+j\le D-4.
$$



The complete functional remains


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
\tag{1.1}
$$



The actual producer and correction are


$$
Q_n^{\rm loc}=Q_c+3^6R,
\qquad
Q_c=(y+1)x^A(\beta+3y),
\qquad
\beta=-71-A,
$$




$$
R\in\mathbb Z_3[y],\qquad \deg R\le A+1.
$$



Write


$$
G_c(f,g)=\mathcal M(Q_cfg),\qquad
K(f,g)=\mathcal M(Rfg),
$$




$$
G_{\rm act}=G_c+3^6K.
$$



## 1.1 Results reused

A4 Turn 15 accepts, at the scopes stated in Turn 8:

- the refined complete propagation;
- the actual LOW inverse zeros;
- the terminal corrected-column formula;
- $\mathcal Q\in27M$;
- the twenty-feature decomposition;
- the depth-$16$ determinant-pair reduction on the specified sufficiently large original-index window.

Those results are reused, not reproved here.

Turn 9’s symbolic argument gives


$$
v_3(\eta_n)=v_3(\chi_n)=1,\qquad
\xi_n=\chi_n/\eta_n\in1+3\mathbb Z_3
\tag{1.2}
$$


for $n\ge5,\ n\equiv2\pmod3$. Its proof uses the actual finite Pascal vector, the complete-force cancellation, and the quadratic contraction identity. I use that supplied proof, rather than promoting the modulo-$729$ receipt into an infinite theorem. Independent audit of Turn 9 remains a separate status item.

Consequently, on the original family,


$$
\boxed{
Q_n^{\rm loc}(-1)=-((n-1)!)^2\xi_n,\qquad
v_3(Q_n^{\rm loc}(-1))=2v_3((n-1)!).
}
\tag{1.3}
$$



The two supplied certificates remain finite:

- thirty-one signed-denominator probes modulo $729$;
- the auxiliary $18$-coordinate LOW calculation and its $6400$ pairings modulo $27$.

Neither establishes an original-family residual determinant law.

---

# 2. Actual eliminated blocks and the terminal dual polynomial

Let $W=[U\ Y]$. Use the actual eliminated block


$$
E_{\rm act}
=
\begin{pmatrix}
3L_{\rm act}&3X_{\rm act}\\
3X_{\rm act}^T&E_{Y,\rm act}
\end{pmatrix},
$$


and put


$$
M=L_{\rm act}^{-1},
\qquad
\widehat E_{\rm act}
=
E_{Y,\rm act}-3X_{\rm act}^TMX_{\rm act},
\qquad
H_{\rm inv}=\widehat E_{\rm act}^{-1}.
$$



Both $L_{\rm act}$ and $\widehat E_{\rm act}$ are unit matrices over $\mathbb Z_3$. This is a statement about the eliminated block. It makes no assertion about the residual bulk.

Let


$$
u=e_m
$$


in the original HIGH coordinates $d,\ldots,m$. Define


$$
a_\rho=H_{\rm inv}u
$$


and the polynomial


$$
\boxed{
\rho
=
Y a_\rho-U M X_{\rm act}a_\rho.
}
\tag{2.1}
$$



This polynomial belongs to the original space $W$, has degree at most $m$, and has integral coefficients.

It is characterized by the exact equations


$$
\boxed{
G_{\rm act}(U,\rho)=0,\qquad
G_{\rm act}(Y_b,\rho)=\mathbf1_{b=m}.
}
\tag{2.2}
$$



Thus $\rho$ is the **actual terminal HIGH dual polynomial after the full LOW return**. It is not $y^d$, not its monic remainder correction, and not a core substitute.

Let


$$
h_{\rm term}=u^TH_{\rm inv}u.
$$


The accepted terminal inverse calculation gives


$$
h_{\rm term}\in9\mathbb Z_3.
$$


Define


$$
\boxed{g=h_{\rm term}/9\in\mathbb Z_3.}
\tag{2.3}
$$



No claim of nonvanishing is implicit in this definition.

---

# 3. Exact evaluation of the terminal features

Retain the accepted actual mixed-force notation


$$
T=K(W,\widehat Z^{\,c})=3\binom ab,
$$




$$
\widetilde b=b-X_{\rm act}^TMa,
$$




$$
\widetilde b=-cuv^T+3\mathcal B,
\qquad
c=[y^{A+1}]R,\qquad v=e_{\nu-1}.
\tag{3.1}
$$



Also retain


$$
R_H=E_0^{-1},\qquad
\mathcal C=\frac{H_{\rm inv}-R_H}{3},
\qquad
w=\mathcal B^Te_d.
$$


The accepted finite-boundary identities are


$$
R_Hu=e_d,\qquad u^TR_Hu=0,
$$




$$
\mathcal C_{mm}\in3\mathbb Z_3,\qquad w\in3\mathbb Z_3^\nu.
\tag{3.2}
$$



## Theorem 3.1 — Terminal representer reduction

Define


$$
\boxed{
k=\frac{K(\widehat Z^{\,c},\rho)}{27}.
}
\tag{3.3}
$$


Then $k\in\mathbb Z_3^\nu$, and the terminal features in Turn 8 satisfy


$$
\boxed{
\tau=c^2g,\qquad
\gamma=-ck-c^2gv.
}
\tag{3.4}
$$



Equivalently,


$$
\boxed{\gamma=-ck-\tau v.}
$$



### Proof

By (2.1) and the definition of $\widetilde b$,


$$
K(\widehat Z^{\,c},\rho)
=
3\widetilde b^TH_{\rm inv}u.
\tag{3.5}
$$



Write


$$
\widehat E_{\rm act}=E_0+3F_{\rm act},
\qquad
f=F_{\rm act}e_d.
$$


Since $E_0e_d=u$,


$$
\widehat E_{\rm act}e_d=u+3f,
$$


and hence


$$
\boxed{
H_{\rm inv}u=e_d-3H_{\rm inv}f.
}
\tag{3.6}
$$



Substituting (3.1) and (3.6) into (3.5) gives


$$
\begin{aligned}
K(\widehat Z^{\,c},\rho)
&=
3(-cvu^T+3\mathcal B^T)
(e_d-3H_{\rm inv}f)\\
&=
-3c\,h_{\rm term}v
+9w-27\mathcal B^TH_{\rm inv}f.
\end{aligned}
$$


Therefore


$$
\boxed{
k=-cgv+\frac w3-\mathcal B^TH_{\rm inv}f.
}
\tag{3.7}
$$


Every term on the right is integral, by (2.3) and (3.2). This proves the asserted integrality of $k$.

Equation (3.6) also gives


$$
\mathcal Cu
=
\frac{H_{\rm inv}u-e_d}{3}
=
-H_{\rm inv}f.
$$


Thus Turn 8’s feature


$$
\gamma=-c\left(\frac w3+\mathcal B^T\mathcal Cu\right)
$$


becomes


$$
\gamma=-c\left(\frac w3-\mathcal B^TH_{\rm inv}f\right)
=-ck-c^2gv.
$$



Finally,


$$
\mathcal C_{mm}
=
\frac{(H_{\rm inv})_{mm}}3
=
3g,
$$


because $(R_H)_{mm}=0$. Therefore


$$
\tau=\frac{c^2\mathcal C_{mm}}3=c^2g.
$$


This proves (3.4). ∎

## 3.1 What has been reduced

The old expression for $\gamma$ involved

- the next HIGH mixed-force bulk $\mathcal B$;
- the lower-boundary return $w$;
- the actual inverse correction $\mathcal Cu$.

Theorem 3.1 combines these **exactly**, rather than discarding one of them. The output requires only:

1. the true terminal representer $\rho$;
2. its scalar terminal coefficient $g$;
3. one complete mixed-force vector $k$.

No residual inverse is used.

The terminal contribution to $\mathcal Q/27$ can consequently be written


$$
\boxed{
-c^2g\,vv^T-c(vk^T+kv^T).
}
\tag{3.8}
$$


Thus the accepted nonlinear identity becomes


$$
\boxed{
\frac{\mathcal Q}{27}
=
\frac{a^TMa}{27}
+\mathcal B^TH_{\rm inv}\mathcal B
-c^2g\,vv^T-c(vk^T+kv^T).
}
\tag{3.9}
$$



This is an exact rearrangement of the whole terminal contribution. It does not remove the growing HIGH bulk.

---

# 4. A division-safe computation of $k$

Formula (3.3), used naively, appears to require three extra digits. The actual degree bounds save one digit.

Let


$$
C_c=G_c(W,Z),\qquad E_c=G_c(W,W).
$$


The original degree endpoints give


$$
C_c\in3M.
$$


Put


$$
C_1=C_c/3.
$$



For a polynomial $f$ of degree at most $m$,


$$
\deg(Rz_if)\le A+d+m=r_*,
\qquad r_*=\frac{3H-1}{2}.
$$


Therefore its endpoint-subtracted quotient has degree at most $r_*-1$. The unique pole of valuation zero is absent identically.

Consequently,


$$
\boxed{
R,f\longmapsto \frac{\mathcal M(Rz_if)}3
}
\tag{4.1}
$$


is an integral bilinear map on the entire relevant bounded-degree spaces. This is the residual analogue of the normalized LOW integrality used in A4 Turn 15.

Now define the complete core adjoint return


$$
s=E_c^{-1}K(W,\rho).
\tag{4.2}
$$



This vector is integral. Indeed, its LOW right-hand side is divisible by $3$, by the same normalized LOW degree argument used in the audit. The block solve therefore uses no division by a nonunit after that normalization.

Since


$$
\widehat Z^{\,c}=Z-WE_c^{-1}C_c,
$$


we obtain


$$
K(\widehat Z^{\,c},\rho)
=
K(Z,\rho)-C_c^Ts.
$$


Hence


$$
\boxed{
k=
\frac1{9}
\left(
\frac{K(Z,\rho)}3-C_1^Ts
\right).
}
\tag{4.3}
$$



The whole numerator in parentheses belongs to $9\mathbb Z_3^\nu$, by Theorem 3.1.

This formula is important computationally:

- it does not require constructing all corrected columns $\widehat z_i^{\,c}$;
- it does not require solving against every column of $\mathcal B$;
- it uses one core adjoint return;
- its evaluated maps are integral before the final division by $9$.

Thus $k\bmod3^p$ requires only $p+2$ digits of the actual producer correction and of the integral intermediate quantities.

---

# 5. Explicit finite LOW and HIGH return operations

The precision theorem below does not rely on an unspecified matrix inverse. Here are the base operations and stopping rules.

## 5.1 An explicit LOW reference inverse

Put


$$
r_1=\frac{H-1}{2}.
$$



Modulo $3$, the actual LOW matrix has moments


$$
(L_{\rm act})_{uv}
\equiv [y^{r_1}]x^{A+u+v}.
$$


For $u+v\ge D$, this is zero. For $0\le j<D$,


$$
[y^{r_1}]x^{H-1-j}
\equiv
(-1)^j\binom{r_1+j}{j}\pmod3.
\tag{5.1}
$$



To see (5.1), use


$$
x^{H-1-j}
\equiv
(y^H-1)(y-1)^{-j-1}\pmod3.
$$


At degree $r_1<H$, only the lower term contributes.

Define an exact integral reference matrix $L_*$ by


$$
(L_*)_{uv}
=
\begin{cases}
(-1)^{D-1-u-v}
\displaystyle\binom{r_1+D-1-u-v}{D-1-u-v},
&u+v<D,\\[2mm]
0,&u+v\ge D.
\end{cases}
\tag{5.2}
$$


Then


$$
L_{\rm act}\equiv L_*\pmod3,
\qquad
\det L_*=\pm1.
$$



Let $J_D$ reverse $D$ coordinates. The matrix $L_*J_D$ is upper triangular Toeplitz, generated by


$$
(1+z)^{-r_1-1}\pmod{z^D}.
$$


Its inverse is therefore generated by


$$
(1+z)^{r_1+1}\pmod{z^D}.
$$



For a LOW vector $b=(b_0,\ldots,b_{D-1})^T$,


$$
\boxed{
(L_*^{-1}b)_i
=
[z^i](1+z)^{r_1+1}
\sum_{j=0}^{D-1}b_{D-1-j}z^j,
\qquad 0\le i<D.
}
\tag{5.3}
$$



This is an explicit finite convolution.

Let


$$
\Delta_L=L_{\rm act}-L_*\in3M.
$$


For a target modulus $3^P$, define


$$
\boxed{
\mathscr L_P(b)
=
\sum_{j=0}^{P-1}
(-L_*^{-1}\Delta_L)^jL_*^{-1}b
\pmod{3^P}.
}
\tag{5.4}
$$


Then


$$
\mathscr L_P(b)\equiv L_{\rm act}^{-1}b\pmod{3^P}.
$$



The stopping criterion is exactly $P$ terms. Each omitted term contains at least $P$ factors of $3$.

The same construction applies to the core LOW matrix.

## 5.2 The finite HIGH reference inverse

Let


$$
L_H=m-d+1.
$$


Write a HIGH vector as $b_0,\ldots,b_{L_H-1}$, corresponding to $Y_d,\ldots,Y_m$. The accepted finite inverse formula gives


$$
\boxed{
(R_Hb)_i
=
[z^{L_H-1-i}]
(1-z)^{-A}
\sum_{j=0}^{L_H-1}b_jz^j,
\qquad 0\le i<L_H.
}
\tag{5.5}
$$



This formula preserves both boundaries:

- coefficients with negative index are zero;
- the output indices remain exactly $d,\ldots,m$;
- no HIGH coordinate beyond $m$ is introduced.

Let


$$
\Delta_H=\widehat E_{\rm act}-E_0\in3M.
$$


Then


$$
\boxed{
\mathscr H_P(b)
=
\sum_{j=0}^{P-1}
(-R_H\Delta_H)^jR_Hb
\pmod{3^P}
}
\tag{5.6}
$$


satisfies


$$
\mathscr H_P(b)\equiv H_{\rm inv}b\pmod{3^P}.
$$



Again the stopping criterion is exactly $P$ terms.

## 5.3 Complete actual return action

The action of $\widehat E_{\rm act}$ used in (5.6) is


$$
\boxed{
q\longmapsto
E_{Y,\rm act}q
-
3X_{\rm act}^T
\mathscr L_P(X_{\rm act}q)
\pmod{3^P}.
}
\tag{5.7}
$$



Every matrix action in (5.7) is a finite moment convolution or a finite polynomial-basis conversion:

- $L_{\rm act}$ is Hankel in the $x$-basis;
- $E_{Y,\rm act}$ is Hankel in the original $y$-indices;
- $X_{\rm act}$ is the finite mixed-basis moment map.

The moments are evaluated from (1.1), with the original endpoint subtraction, factorial term, and cutoff. The computation does not replace $X_{\rm act}$ by a remainder map at unproved precision.

These formulas still manipulate polynomials whose lengths grow with the original index. They are **not** a constant-state algorithm in $n$. Their reduction is different: the decisive terminal contractions require only a fixed number of actual right-hand sides and prescribed convolution returns, not a solve against the growing residual bulk or against all its mixed-force columns.

---

# 6. A fixed-precision terminal-channel algorithm

## Theorem 6.1 — Two-digit terminal evaluation

Fix $p\ge1$. On the original domain, suppose the actual correction $R$ is supplied modulo


$$
3^{p+2}.
$$



Then the actual quantities


$$
g,\qquad k,\qquad\tau,\qquad\gamma
$$


are determined modulo $3^p$ by the following finite computation. Its precision loss is at most two digits and is independent of any residual determinant cancellation.

### Inputs

1. The original integers $n,H,D,h$, with the original finite endpoints.
2. The exact core $Q_c$.
3. The actual $R\bmod3^{p+2}$.
4. The complete functional (1.1), not a selected pole truncation unless omitted terms have been separately proved divisible by the working modulus.

### Working precision

Set


$$
P=p+2.
$$



### Step 1: construct actual eliminated-block actions

Construct


$$
L_{\rm act},\quad X_{\rm act},\quad E_{Y,\rm act}
\pmod{3^P}
$$


using the complete normalized LOW evaluations and the ordinary integral HIGH evaluations.

Use (5.3)–(5.7) for the LOW and HIGH return maps.

### Step 2: compute the true terminal dual polynomial

Compute


$$
a_\rho=\mathscr H_P(u),
$$




$$
\rho=Ya_\rho-U\mathscr L_P(X_{\rm act}a_\rho)
\pmod{3^P}.
$$



### Step 3: evaluate the scalar terminal channel

Form


$$
h_{\rm term}=u^Ta_\rho\pmod{3^P}.
$$


The accepted terminal theorem makes it divisible by $9$. Set


$$
\boxed{g=h_{\rm term}/9\pmod{3^p}.}
$$



### Step 4: perform one core adjoint return

Form


$$
f_U=\frac{K(U,\rho)}3,\qquad f_Y=K(Y,\rho)
\pmod{3^P}.
$$


The first map is integral on the full relevant bounded-degree space.

Using the core blocks $L_c,X_c,\widehat E_c$, compute


$$
s_Y
=
\widehat E_c^{-1}
\bigl(f_Y-3X_c^TL_c^{-1}f_U\bigr),
$$




$$
s_U=L_c^{-1}(f_U-X_cs_Y)
\pmod{3^P}.
\tag{6.1}
$$


All inverses in (6.1) are evaluated by the explicit finite return rules above.

Then $s=(s_U,s_Y)^T$ is exactly the integral vector


$$
E_c^{-1}K(W,\rho)
$$


to the prescribed precision.

### Step 5: evaluate the whole mixed numerator before division

Compute


$$
N_k=\frac{K(Z,\rho)}3-C_1^Ts
\pmod{3^P}.
$$


Theorem 3.1 proves $N_k\in9\mathbb Z_3^\nu$. Set


$$
\boxed{k=N_k/9\pmod{3^p}.}
$$



### Step 6: recover the terminal features

With $c=[y^{A+1}]R$,


$$
\boxed{
\tau=c^2g,\qquad
\gamma=-ck-\tau v
\pmod{3^p}.
}
$$



### Stopping criterion

Every LOW or HIGH inverse return uses $P$ terms. After Steps 1–6, stop. There is no determinant-dependent stopping test.

### Proof

The LOW and HIGH return formulas are valid because their respective perturbations lie in $3M$, while the displayed reference inverses are integral. Thus their errors after $P$ terms lie in $3^P$.

All polynomial coefficients involved in $\rho$ and $s$ are integral. The normalized LOW and residual mixed-force maps are integral on the complete degree-bounded spaces, so replacing their inputs modulo $3^P$ changes their outputs by a multiple of $3^P$.

The only final nonunit divisions are


$$
h_{\rm term}/9,\qquad N_k/9.
$$


Their legitimacy follows from the actual terminal identities, and they consume two digits. No inverse of $\Psi$, $\mathcal A$, or $S_{\rm act}$ occurs. ∎

## 6.1 Producer-input precision

Turn 9 supplies $R\bmod3^q$ from producer input precision $3^{q+7}$. Taking $q=p+2$ gives the sufficient bound


$$
\boxed{\text{producer input modulus }3^{p+9}.}
\tag{6.2}
$$



If the terminal-jet representation is used, its exact hypotheses must still hold:


$$
R\equiv(y+1)x^{A-\kappa_{p+2}}B_{p+2}(x)
\pmod{3^{p+2}},
$$


with the actual factorial-tail length and endpoint condition, in particular


$$
2v_3((n-1)!)\ge p+8.
$$


No arbitrary-depth approximation to $Q_c$ has been introduced.

## 6.2 What the algorithm does not compute

It computes the true terminal features and their complete LOW returns. It does not compute


$$
e_{\rm act}^T\Psi^{-1}e_{\rm act},
$$


and it does not certify $\det\Psi\ne0$.

The two-digit loss above belongs to the terminal eliminated-block channel. It is not a bound for the inverse loss of the residual form.

---

# 7. An exact scalar return formula

The preceding algorithm can also be expressed as scalar return contractions.

With


$$
F_{\rm act}=\frac{\widehat E_{\rm act}-E_0}{3},
\qquad
f=F_{\rm act}e_d,
$$


the resolvent identity gives


$$
H_{\rm inv}
=
R_H-3R_HF_{\rm act}R_H
+9R_HF_{\rm act}H_{\rm inv}F_{\rm act}R_H.
$$


Contracting with $u$, and using $R_Hu=e_d$, yields


$$
\boxed{
g
=
-\frac{(F_{\rm act})_{dd}}3
+
f^TH_{\rm inv}f.
}
\tag{7.1}
$$



This is the whole scalar, not a valuation estimate on its separate terms.

For fixed $p$,


$$
\boxed{
g\equiv
-\frac{(F_{\rm act})_{dd}}3
+
\sum_{j=0}^{p-1}
(-3)^j
f^T(R_HF_{\rm act})^jR_Hf
\pmod{3^p}.
}
\tag{7.2}
$$



The actual first-return vector $f$ itself has an explicit LOW-return expression. Let


$$
q=\pi(y^d)=y^d-\operatorname{rem}_{x^D}y^d,
$$


and put


$$
\lambda=\frac{G_{\rm act}(U,q)}3.
$$


Then


$$
\boxed{
f_b
=
\frac{G_{\rm act}(Y_b,q)-\mathbf1_{b=m}}3
-
(X_{\rm act}^TM\lambda)_b.
}
\tag{7.3}
$$



The subtraction of $\mathbf1_{b=m}$ is the finite top-pole cancellation. The final term is the actual LOW return. Neither is omitted.

Equations (7.2)–(7.3) explicitly reduce the terminal scalar to finitely many complete evaluated returns. They also make clear why its nonvanishing does not follow from the integrality of its summands: cancellation between the whole scalar terms remains possible.

---

# 8. Displacement on the whole original residual space

The terminal vector $k$ has a direct role in the full residual operator.

Let


$$
C_{\rm act}=G_{\rm act}(W,Z),
\qquad
K_{\rm elim}=E_{\rm act}^{-1}C_{\rm act},
$$


and define the actual orthogonal residual columns


$$
\widehat Z^{\,\rm act}=Z-WK_{\rm elim}.
$$


Then


$$
S_{\rm act}
=
G_{\rm act}(\widehat Z^{\,\rm act},\widehat Z^{\,\rm act}).
$$



The matrix $K_{\rm elim}$ is integral: the LOW part of $C_{\rm act}$ is divisible by $3$, and the actual block solve has the normalized form used above.

## 8.1 The finite multiplication operator

On $\mathbb Q_3[y]_{\le m}$, define


$$
\mathscr T f
=
yf-[y^m]f\,y^{m+1}.
\tag{8.1}
$$


Thus multiplication by $y$ is truncated at the **actual endpoint $m$**.

Let


$$
t(f)=[y^m]f.
$$


Define a second functional without extending the original moment cutoff:


$$
\mathfrak r(f)
=
\mathcal M\!\left(
Q_n^{\rm loc}y^{m+1}
\bigl(f-t(f)y^m\bigr)
\right).
\tag{8.2}
$$


The polynomial in (8.2) has degree at most $2n-1$. Thus every evaluation remains inside the original complete functional range.

For all $f,g\in\mathbb Q_3[y]_{\le m}$,


$$
\boxed{
G_{\rm act}(f,\mathscr Tg)
-
G_{\rm act}(\mathscr Tf,g)
=
t(f)\mathfrak r(g)-\mathfrak r(f)t(g).
}
\tag{8.3}
$$



This follows by expanding (8.1). The potentially exterior highest moment cancels; it is not supplied by enlarging the cutoff.

## 8.2 The residual multiplication matrix

Write


$$
\pi(y^d)=x^Dq_d(y),
$$


where


$$
q_d(y)=y^\nu+\sum_{i=0}^{\nu-1}q_i y^i.
$$



Let $\mathscr C$ be the $\nu\times\nu$ companion matrix with


$$
\mathscr C e_i=e_{i+1}\quad(0\le i<\nu-1),
\qquad
\mathscr C e_{\nu-1}=-\sum_{i=0}^{\nu-1}q_i e_i.
\tag{8.4}
$$



Multiplication of a LOW column by $y$ leaves LOW except at its true last coordinate:


$$
yU_{D-1}=U_{D-1}+z_0.
$$


No HIGH column creates a residual coordinate under the truncated multiplication (8.1).

Consequently, the residual block of multiplication in the actual orthogonal coordinates is


$$
\boxed{
\mathscr D
=
\mathscr C-e_0\ell^T,
\qquad
\ell^T=e_{U_{D-1}}^TK_{\rm elim}.
}
\tag{8.5}
$$



This is the promised companion matrix with one actual LOW-return row correction.

## Theorem 8.1 — Full-residual displacement

Put


$$
t_{\rm act}=t(\widehat Z^{\,\rm act}),
\qquad
r_{\rm act}=\mathfrak r(\widehat Z^{\,\rm act}).
$$


Then, on the whole original $\nu$-dimensional residual space,


$$
\boxed{
S_{\rm act}\mathscr D-\mathscr D^TS_{\rm act}
=
t_{\rm act}r_{\rm act}^T-r_{\rm act}t_{\rm act}^T.
}
\tag{8.6}
$$



### Proof

Apply (8.3) to two actual orthogonal residual columns. Their pairings with every column of $W$ vanish. Therefore only the residual block $\mathscr D$ of the truncated multiplication contributes on the left, giving exactly (8.6). ∎

This identity does not assume that $S_{\rm act}$ is nonsingular.

## 8.3 The terminal mixed vector is an actual displacement generator correction

Define


$$
t_c=t(\widehat Z^{\,c}).
$$



The exact correction identity


$$
C_{\rm act}-E_{\rm act}E_c^{-1}C_c
=
3^6K(W,\widehat Z^{\,c})
$$


gives


$$
K_{\rm elim}-E_c^{-1}C_c
=
3^6E_{\rm act}^{-1}K(W,\widehat Z^{\,c}).
$$


Taking its terminal HIGH row and using the defining property of $\rho$,


$$
e_m^T
\left(K_{\rm elim}-E_c^{-1}C_c\right)
=
3^6K(\rho,\widehat Z^{\,c})
=
3^9k.
$$


Since the residual columns themselves have degree below $m$,


$$
\boxed{
t_{\rm act}=t_c-3^9k.
}
\tag{8.7}
$$



Thus the terminal calculation in §§3–6 evaluates the exact actual change in a generator of the full-residual displacement law.

This is a structural link to the growing bulk, not an isolated common zero digit.

---

# 9. The actual endpoint is not the terminal coefficient channel

The endpoint vector remains


$$
e_{\rm act}=\widehat Z^{\,\rm act}(-1),
$$


and


$$
d_{\rm act}=W(-1)^TE_{\rm act}^{-1}W(-1).
$$



These are not replaced by $t_{\rm act}$, $v=e_{\nu-1}$, or the terminal HIGH dual polynomial.

The finite multiplication has the endpoint identity


$$
(\mathscr Tf)(-1)
=
-f(-1)-(-1)^{m+1}t(f).
\tag{9.1}
$$


Accordingly, in actual orthogonal coordinates, the endpoint transport includes both the residual multiplication and its eliminated-space boundary block. It is not legitimate to infer an endpoint recurrence from $\mathscr D$ alone while omitting that block.

For completeness, if $\mathscr T$ has blocks $T_{WW},T_{WZ},T_{ZW},T_{ZZ}$ in the original $[W,Z]$ basis, then the eliminated-space block acting on the corrected residual columns is exactly


$$
\boxed{
B_{WZ}
=
T_{WZ}-T_{WW}K_{\rm elim}+K_{\rm elim}\mathscr D.
}
\tag{9.2}
$$


Thus


$$
\boxed{
\mathscr D^Te_{\rm act}
+B_{WZ}^TW(-1)
=
-e_{\rm act}-(-1)^{m+1}t_{\rm act}.
}
\tag{9.3}
$$



Equation (9.3) preserves the complete finite endpoint boundary. It also identifies the obstruction to treating the newly evaluated terminal coefficient channel as though it were already the desired endpoint inverse contraction.

---

# 10. Consequences for the accepted bulk–boundary pair

On the accepted sufficiently large original-index window


$$
j\equiv81\pmod{243},
\qquad
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad
C_{16}=512\cdot17^2\,3^{15},
$$


retain


$$
S_{\rm act}=-3^{16}\Psi,
$$


and


$$
\delta_0=\det\Psi,
$$




$$
\boxed{
\delta_1
=
e_{\rm act}^T\operatorname{adj}(\Psi)e_{\rm act}
-
3^{16}d_{\rm act}\det\Psi.
}
\tag{10.1}
$$



The accepted twenty-feature representation remains exact. The new result evaluates its terminal features by


$$
\tau=c^2g,\qquad \gamma=-ck-\tau v.
$$



The full displacement law becomes


$$
-3^{16}
\bigl(\Psi\mathscr D-\mathscr D^T\Psi\bigr)
=
t_{\rm act}r_{\rm act}^T-r_{\rm act}t_{\rm act}^T.
\tag{10.2}
$$


The right side is divisible by $3^{16}$ as a **whole matrix**. No separate divisibility of its two outer products is assumed.

## 10.1 What has not followed

Neither a rank-two displacement nor a finite-rank border implies invertibility.

In particular, the present results do not prove:

- that $\mathcal A$ is nonsingular;
- that $\Psi$ is nonsingular;
- that the complete distinguished cofactor $\delta_1$ is nonzero;
- that the endpoint contraction has a uniform inverse-loss bound.

The growing bulk still carries information not determined by its terminal border.

## 10.2 The precise follow-on lemma

A useful next obligation is now the following.

> **Actual displacement-relative-pair lemma.**  
> Use the exact data
> 

$$
> \mathscr D=\mathscr C-e_0\ell^T,\qquad
> t_{\rm act}=t_c-3^9k,\qquad
> r_{\rm act},\qquad
> e_{\rm act},\qquad
> B_{WZ},
>
$$


> with (8.6) and (9.3), to obtain either:
> 
> 1. a nonvanishing theorem and a relative valuation law for the actual pair $(\delta_0,\delta_1)$; or
> 2. an exact radical theorem for the full original residual space that determines both members of that pair.
>
> Any recurrence must retain its last companion equation and the endpoint boundary block $B_{WZ}$. A recurrence using only interior displacement equations is insufficient.

The terminal inputs $g,k,\tau,\gamma$ are no longer unspecified contractions: §§5–6 give a prescribed computation and stopping precision for them.

What remains unproved is the conversion from these complete displacement data to the relative determinant/cofactor law.

---

# 11. Endpoint valuation and primitive normalization

Let


$$
F=(n-1)!.
$$


The true endpoint law is


$$
Q_n^{\rm loc}(-1)=-F^2\xi_n,
\qquad \xi_n\in1+3\mathbb Z_3.
$$



When $\delta_0\ne0$, the accepted exact ratio therefore becomes


$$
\boxed{
\frac{\beta_1}{\beta_0}
=
\frac{3^{h-16}F^2\xi_n}{4}
\frac{\delta_1}{\delta_0}.
}
\tag{11.1}
$$



If $\delta_0\delta_1\ne0$,


$$
\boxed{
v_3(q)
=
\max\left\{
0,\,
h-16+2v_3(F)
+v_3(\delta_1)-v_3(\delta_0)
\right\}.
}
\tag{11.2}
$$



The new terminal precision theorem does not remove the final relative valuation in (11.2).

Restore


$$
Q_n=\lambda Q_n^{\rm loc},
\qquad
R_{\rm rat}=\frac{4\lambda}{3^h}G_{\rm act},
$$




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



Let $\ell$ be the least positive clearing integer required by the original rational-matrix normalization. Its minimality is not established by a local $3$-adic calculation, and it is not replaced here by a convenient larger clearer.

With $k_0=m+1$, put


$$
A_\ell=\ell^{k_0}\beta_0,\qquad
B_\ell=\ell^{k_0}\beta_1,
$$


and preserve the complete all-prime gcd


$$
\boxed{
g_\ell=\gcd(|A_\ell|,|B_\ell|).
}
\tag{11.3}
$$



When $B_\ell\ne0$, the primitive integers are


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
\frac{\operatorname{sgn}(B_\ell)\ell^{k_0}}{g_\ell}
\det H_{\rm complete}.
}
\tag{11.4}
$$



Neither the factorial contribution in (1.1), the endpoint subtraction, the least clearer, nor any prime in the gcd has been removed.

---

# 12. Bounded exact arithmetic for implementation inspection

No finite computation is needed for the symbolic terminal identities or the displacement proof.

A small auxiliary calculation can inspect the new convolution implementation and all finite-boundary signs. It must not be presented as an original-producer test.

## 12.1 Auxiliary inputs

Take


$$
H=81,\qquad h=5,\qquad D=6,
$$




$$
A=75,\qquad n=77,\qquad m=38,\qquad d=8,\qquad \nu=2.
$$


Thus the full polynomial space has dimension $39$, LOW has dimension $6$, and HIGH has dimension $31$.

Use


$$
\beta=-71-A=-146,
$$




$$
Q_c=(y+1)x^{75}(\beta+3y),
$$


and the explicitly selected test perturbation


$$
R_{\rm test}=(y+1)x^{73}(1+2x+x^2).
$$


Set


$$
Q_{\rm test}=Q_c+3^6R_{\rm test}.
$$



This is a **synthetic perturbation**, not the actual producer $Q_n^{\rm loc}$. These parameters do not satisfy the original index or narrow-window hypotheses.

Use the complete functional with its exact cutoff


$$
4n-3=305,
$$


and working modulus


$$
3^8.
$$



The factorial term must be evaluated, not automatically discarded: its displayed coefficient is only $3^5/4$.

## 12.2 Expected verifiable output

The calculation should report:

1. Agreement of the explicit LOW reference inverse (5.3) with direct inversion of $L_*$.
2. Agreement of the finite HIGH convolution (5.5) with direct inversion of $E_0$.
3. Agreement modulo $3^8$ between the finite return algorithms and direct modular inversion of the corresponding unit LOW and HIGH Schur blocks.
4. Agreement of the directly constructed terminal dual polynomial with (2.2).
5. Agreement, whenever the stated divisions are valid, between the direct terminal scalar and the complete scalar return formula (7.1).
6. Exact rational agreement of Theorem 3.1’s algebraic feature identities, without presuming the original-family divisibility assertions for this synthetic input.
7. Agreement of the full $2\times2$ residual displacement with (8.6), using the actual last LOW coordinate, last residual equation, and HIGH cutoff.
8. Agreement of the endpoint transport with (9.3).

The verifiable output should include the actual residues and the zero matrices obtained by subtracting the two sides of each identity. A failure of a divisibility hypothesis on this auxiliary input must be reported as such, not overridden.

This bounded calculation checks the implementation and finite-boundary algebra only. It cannot prove original-family nonvanishing or a relative valuation law.

---

# 13. Proof-status ledger

| Statement | Status |
|---|---|
| Turn 8 refined propagation, $\mathcal Q\in27M$, depth $16$, twenty-feature decomposition | Reused at A4 Turn 15’s accepted scopes |
| Turn 9 $\eta/\chi$ law and sharp endpoint valuation | Reused from its supplied symbolic proof; independent audit remains separate |
| Supplied modulo-$729$ and LOW modulo-$27$ receipts | Finite corroboration only |
| Actual terminal dual polynomial with complete LOW return | Defined and characterized exactly |
| $g\in\mathbb Z_3$, $k\in\mathbb Z_3^\nu$ | Proved using accepted terminal cancellations |
| $\tau=c^2g,\ \gamma=-ck-\tau v$ | Newly proved exact reduction |
| One-core-adjoint evaluation of $k$ | Newly proved |
| Explicit finite LOW reference convolution | Newly derived for the actual residue matrix |
| Two-digit terminal precision bound and stopping rule | Newly proved |
| Producer input $3^{p+9}$ sufficient for terminal features modulo $3^p$ | Derived with the stated producer-jet hypotheses |
| Full original-residual displacement identity | Newly proved |
| $t_{\rm act}=t_c-3^9k$ | Newly proved |
| Complete endpoint boundary transport | Newly derived |
| Actual $\delta_0,\delta_1$ nonvanishing | Unresolved |
| Relative cofactor valuation law | Unresolved |
| Least clearer, full gcd, and whole nonzero error tending to zero | Unresolved |

## Closing conclusion

The new result is an **actual terminal-channel evaluation theorem**, not another common residual zero digit.

The complete terminal border can now be computed from one actual terminal dual polynomial and one core adjoint return:


$$
\boxed{
g=\frac{(\widehat E_{\rm act}^{-1})_{mm}}9,\qquad
k=\frac{K(\widehat Z^{\,c},\rho)}{27},\qquad
\tau=c^2g,\qquad
\gamma=-ck-\tau v.
}
$$


The computation has a certified two-digit loss, explicit finite convolution inputs, and a fixed stopping rule independent of unknown residual determinant cancellation.

Moreover, $k$ controls the exact actual change in a displacement generator of the whole original residual form:


$$
\boxed{t_{\rm act}=t_c-3^9k.}
$$



The decisive remaining mathematical bottleneck is still the nonvanishing and relative valuation of


$$
\boxed{
\det\Psi,\qquad
e_{\rm act}^T\operatorname{adj}(\Psi)e_{\rm act}
-3^{16}d_{\rm act}\det\Psi,
}
$$


now with explicitly evaluable terminal data and a complete finite displacement law. No proof has yet converted that structure into the required relative-pair theorem.

The least clearer, full all-prime gcd, actual primitive denominator, and whole same-index nonzero error remain additional global obligations.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


