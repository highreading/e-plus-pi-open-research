> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 10 — A finite adjoint telescope and a fixed-variable rational representation of the actual head-to-source kernel

## Executive assessment

The supplied work does not prove or disprove the irrationality of $e+\pi$. The local norm-relative congruence also remains unresolved.

There is, however, a concrete advance on the assigned output-kernel problem:

> **The actual finite contact inverse can be expressed as a fixed-length operator product plus its complete finite-end correction. Its interior inverse is an explicitly truncated divided-power operator, not a recurrence of original length. Combining this with the bounded first-force support gives a fixed-variable rational coefficient representation of the actual head-to-source contraction.**

The principal conclusions are:

1. **A sharper interior contact inverse.**  
   If
   

$$
c_s(n)=s![z^s]\phi(z)^{-n},
   \qquad \phi(z)=1-z+\frac{z^2}{2},
$$


   then the inverse of the lower contact factor is
   

$$
(H^{-1})_{jk}
   =c_{j-k}(n)\binom jk.
$$


   Modulo $29^K$, only $j-k<29K$ can contribute. This is a direct divided-power identity.

2. **An actual finite adjoint telescope.**  
   For
   

$$
w=A^{-T}LA^{-1}f^0,
$$


   the kernel $\Psi_\ell$ is the terminal-zero solution of a backward adjoint recurrence. The resulting summation identity has exactly two initial charges, the complete source contraction, and the separate exterior charge. No recurrence row is added beyond $b-2$.

3. **An explicit finite-end formula.**  
   Writing the finite inverse as
   

$$
A^{-1}\equiv \mathsf B-\mathsf U\mathsf S_{\rm end}^{-1}\mathsf V
   \pmod{29^K},
$$


   the complete correction to every required weighted contraction is displayed below. In particular, the exterior $+1$ contributes
   

$$
bW_b^2\,(A^{-1}f^0)_{b-1},
$$


   not a block-end surrogate.

4. **A fixed-variable rational coefficient target.**  
   Every scalar needed for
   

$$
\sum_{\ell=1}^{b-2}\mathcal H_\ell\Psi_\ell
$$


   is reduced to coefficients of explicitly specified rational functions. The number of variables is bounded independently of both $b$ and $K$; a safe bound is $32$. Parameter exponents remain the actual $n,b$, as extraction indices, rather than being replaced by residues.

5. **A quantified limitation.**  
   The representation is an algebraic reduction, not a practical original-index computation. An explicit dense prime-power Cartier implementation is possible, but its conservative cost is prohibitive. No claim that a recent automaticity or state-complexity theorem makes this particular kernel feasible is made.

The remaining local target is still


$$
\boxed{
\mathcal C-29\rho_n\mathcal N
\equiv0\pmod{29^{v_{29}(\mathcal N)+2}}.
}
$$


The new formulas specify its high-index coefficient content more concretely; they do not establish its vanishing.

No tools were executed. No external literature, archive, credential, or endpoint was accessed. The supplied Markdown sources and receipts are evaluated only as mathematical data.

---

## 1. Domain and reused results

Retain the original family


$$
a=432827+682892t,\qquad
t=364+841u,\quad u\ge0,
$$




$$
\boxed{
b=3^{249005515+574312172u},\qquad n=2001b.
}
$$



The finite domains remain:

- contact coordinates: $0\le i,j<b$;
- recurrence rows: $1\le i\le b-2$;
- reconstructed coordinates: $0\le j\le b$.

Write


$$
W_j=\binom{n+2}{j},
\qquad
(\mathcal Rx)_j=W_j(jx_{j-1}-x_j),
$$


with the actual first and last rows, and


$$
A\theta=f^0,\qquad A\psi=\mathbf r,
$$




$$
Z_w=\mathcal R\theta,\qquad
Y=\mathcal R\psi+W_be_b.
$$


Thus


$$
\mathcal N=Z_w^TZ_w=29^4D,\qquad
\mathcal C=Z_w^TY=29^5M.
$$



The actual tridiagonal weight matrix is


$$
L=\mathcal R^T\mathcal R,
$$


where


$$
L_{jj}=W_j^2+(j+1)^2W_{j+1}^2,
$$




$$
L_{j,j+1}=L_{j+1,j}=-(j+1)W_{j+1}^2.
$$


In particular, $L_{b-1,b-1}$ includes $b^2W_b^2$.

### 1.1 Reused memory and support bounds

As requested, I reuse Turn 9’s symbolic monodromy calculation, without repeating a generic Fitting argument or another finite-prefix check. Its consequences are


$$
H_K=58K+1
$$


for arbitrary actual propagation intervals, and


$$
h_j^{(0)}\equiv h_j^{(1)}\equiv0\pmod{29^K}
\qquad(j\ge58K+2).
$$


The first force has the stronger bound


$$
f_j^0\equiv0\pmod{29^K}\qquad(j\ge29K),
$$


because


$$
f_j^0=\frac{(n+j)!}{n!}J_j,\qquad J_j\in\mathbb Z.
$$



Consequently, at precision $29^K$, the first-force and homogeneous input polynomials may be taken to have lengths


$$
m_f=\min(b,29K),\qquad
m_h=\min(b,58K+2).
$$


This truncation applies to the **inputs**. It does not assert that their contact inverses or weighted outputs have short coordinate support.

The coordinator’s supplied $59K$ receipt is consistent with, and weaker than, the reused symbolic bound. Its higher-precision cases remain finite corroboration, not original-family Gram calculations.

---

## 2. The interior contact inverse is a divided-power operator

Fix $K\ge1$ and work modulo $29^K$. Set


$$
M_K=29K-1,\qquad m=\min(2n,M_K),\qquad t_0=\min(m,b).
$$



Use Turn 7’s finite factorization


$$
A\equiv \mathsf P\,T\,(H+F\overline K E)\,T,
\tag{2.1}
$$


where


$$
\mathsf P_{ij}=\binom ij,\qquad
T_{ij}=\binom n{j-i},
$$


and $E$ selects the last $t_0$ contact coordinates.

The complete finite-end data are


$$
F_{jr}
=-\sum_{u=0}^{r}
\binom{-n}{b+u-j}\binom n{r-u},
\qquad 0\le r<m,
\tag{2.2}
$$


and


$$
\overline K_{rv}
=
\begin{cases}
a_{b+r-j_v}(n)\dfrac{(b+r)!}{j_v!},
&1\le b+r-j_v\le m,\\[1mm]
0,&\text{otherwise},
\end{cases}
\quad
j_v=b-t_0+v.
\tag{2.3}
$$


Here $a_s(n)=[z^s]\phi(z)^n$.

These are exactly the terms crossing the finite contact boundary. They are not optional corrections to an infinite inverse.

### Proposition 2.1 — Explicit inverse of the lower factor

Define


$$
b_s(n)=[z^s]\phi(z)^{-n},
\qquad c_s(n)=s!b_s(n).
$$


Then the exact finite lower-triangular inverse of the untruncated lower factor is


$$
\boxed{
(H^{-1})_{jk}
=b_{j-k}(n)\frac{j!}{k!}
=c_{j-k}(n)\binom jk
\qquad(k\le j).
}
\tag{2.4}
$$



Moreover,


$$
\boxed{
H^{-1}\equiv \mathsf D,\qquad
\mathsf D_{jk}
=
\begin{cases}
c_{j-k}(n)\binom jk,&0\le j-k\le M_K,\\
0,&\text{otherwise},
\end{cases}
\pmod{29^K}.
}
\tag{2.5}
$$



#### Proof

For a finite vector $v$, use its exponential generating polynomial


$$
V(z)=\sum_{j=0}^{b-1}v_j\frac{z^j}{j!}.
$$


The lower factor $H$ acts by multiplication by $\phi(z)^n$, followed by truncation below degree $b$. Since $\phi(0)=1$, its inverse on this finite lower-triangular system is multiplication by $\phi(z)^{-n}$, with the same truncation. This proves (2.4).

Every $b_s(n)$ is $29$-integral: the only coefficient denominators come from powers of $2$. Hence


$$
v_{29}(c_s(n))\ge v_{29}(s!)\ge\lfloor s/29\rfloor.
$$


Thus $c_s(n)\equiv0\pmod{29^K}$ for $s\ge29K$, proving (2.5). ∎

This inverse does not require solving a long lower recurrence.

The coefficients can be generated without nonunit modular division:


$$
b_s(n)=(-1)^s
\sum_{v=0}^{\lfloor s/2\rfloor}
2^{-v}\binom{-n}{s-v}\binom{s-v}{v}.
\tag{2.6}
$$


Generalized binomial coefficients here are evaluated as integers before reduction.

### 2.1 The complete finite inverse

Put


$$
\mathsf R=T^{-1},\qquad \mathsf P_-=\mathsf P^{-1},
$$




$$
\mathsf S_{\rm end}=I_{t_0}+E\mathsf D F\overline K,
$$




$$
\mathsf B=\mathsf R\mathsf D\mathsf R\mathsf P_-,
\qquad
\mathsf U=\mathsf R\mathsf D F\overline K,
\qquad
\mathsf V=E\mathsf D\mathsf R\mathsf P_-.
$$


Then


$$
\boxed{
A^{-1}\equiv
\mathsf B-\mathsf U\mathsf S_{\rm end}^{-1}\mathsf V
\pmod{29^K}.
}
\tag{2.7}
$$



This follows by the finite rank-update identity applied to (2.1).

Because $29\mid n$, the accepted factorization gives


$$
F\overline K\equiv0\pmod{29},
$$


and therefore


$$
\mathsf S_{\rm end}\equiv I\pmod{29}.
$$


Its inverse is the demonstrated unit inverse


$$
\boxed{
\mathsf S_{\rm end}^{-1}
\equiv
\sum_{q=0}^{K-1}
\bigl(-E\mathsf D F\overline K\bigr)^q
\pmod{29^K}.
}
\tag{2.8}
$$



Equations (2.5)–(2.8) replace the interior contact inverse by a precision-sized divided-power operator while preserving the whole finite boundary.

---

## 3. What bounded head support actually buys

For any input $h$, define


$$
c_h=\mathsf S_{\rm end}^{-1}\mathsf Vh.
$$


Then


$$
\boxed{
\theta_h:=A^{-1}h
\equiv \mathsf Bh-\mathsf Uc_h.
}
\tag{3.1}
$$



If $h$ is supported in $0\le i<L$, its first finite binomial transform is


$$
(\mathsf P_-h)_k
=\sum_{i=0}^{\min(k,L-1)}
(-1)^{k-i}\binom ki h_i.
\tag{3.2}
$$



There is also a closed formula for the next transform:


$$
\boxed{
\begin{aligned}
(\mathsf R\mathsf P_-h)_j
={}&(-1)^j
\sum_{i=0}^{L-1}(-1)^i h_i
\sum_{t=0}^{i}
\binom j{i-t}\binom{n+t-1}{t}\\
&\hspace{24mm}\times
\binom{n+b-1-j}{b-1-j-t}.
\end{aligned}
}
\tag{3.3}
$$


Invalid binomial ranges are zero.

#### Derivation

Starting from the actual finite range,


$$
(\mathsf R\mathsf P_-h)_j
=
\sum_{r=0}^{b-1-j}\binom{-n}{r}
\sum_i(-1)^{j+r-i}\binom{j+r}{i}h_i,
$$


use


$$
\binom{-n}{r}=(-1)^r\binom{n+r-1}{r},
\qquad
\binom{j+r}{i}
=\sum_t\binom j{i-t}\binom rt.
$$


Then


$$
\binom{n+r-1}{r}\binom rt
=
\binom{n+t-1}{t}
\binom{n+r-1}{r-t},
$$


and the finite hockey-stick sum gives (3.3).

The upper limit $b-1-j$ is responsible for the last binomial in (3.3). It has not been replaced by an infinite convolution.

### 3.1 Endpoint coefficients of head inputs are genuinely small calculations

To form


$$
E\mathsf D\mathsf R\mathsf P_-h,
$$


only indices within distance at most $t_0+M_K$ of $b$ are required before the last transform. For head inputs of length $O(K)$, formulas (3.2) and the finite upper transform then involve:

- $O(K)$ input coefficients;
- binomial lower indices $O(K)$;
- $O(K)$ near-terminal coordinates.

Thus $c_{f^0},c_{h^{(0)}},c_{h^{(1)}}$ and the corresponding terminal contact coordinates have bounded polynomial-size arithmetic descriptions once the actual head coefficients are supplied.

This does **not** make the whole output local. The high-index binomials in the interior of (3.3) remain.

Also,


$$
W_b=\binom{n+2}{b}
$$


is still a genuine high-index binomial. It is not covered by a small-lower-index simplification.

---

## 4. An actual terminal-zero adjoint telescope

Let


$$
\Gamma=A^{-T}LA^{-1},
\qquad
w=\Gamma f^0.
$$


Since $\Gamma$ is symmetric,


$$
(f^0)^T\Gamma h=w^Th.
$$



The original recurrence operator is


$$
(\mathcal Dh)_i
=h_{i+1}-\alpha_i h_i+\beta_i h_{i-1}+\gamma_i h_{i-2},
\qquad 1\le i\le b-2,
$$


with $\gamma_1=0$.

Define $\lambda_i$ only on the actual source rows $1\le i\le b-2$, by backward substitution:


$$
\boxed{
\lambda_{j-1}
=
w_j+\alpha_j\lambda_j
-\beta_{j+1}\lambda_{j+1}
-\gamma_{j+2}\lambda_{j+2},
\qquad j=b-1,b-2,\ldots,2,
}
\tag{4.1}
$$


where absent terminal $\lambda$-coordinates are zero. These zeros are boundary conventions for the adjoint, not additional forward recurrence rows.

Set


$$
a_0=w_0-\beta_1\lambda_1-\gamma_2\lambda_2,
$$




$$
a_1=w_1+\alpha_1\lambda_1-\beta_2\lambda_2-\gamma_3\lambda_3.
\tag{4.2}
$$



### Proposition 4.1 — Finite adjoint summation identity

For every actual contact vector $h$,


$$
\boxed{
w^Th
=
a_0h_0+a_1h_1
+\sum_{\ell=1}^{b-2}\lambda_\ell(\mathcal Dh)_\ell.
}
\tag{4.3}
$$



#### Proof

Expanding the last sum, the coefficient of $h_j$, $j\ge2$, is


$$
\lambda_{j-1}
-\alpha_j\lambda_j
+\beta_{j+1}\lambda_{j+1}
+\gamma_{j+2}\lambda_{j+2},
$$


which equals $w_j$ by (4.1).

The coefficients of $h_0,h_1$ are respectively


$$
\beta_1\lambda_1+\gamma_2\lambda_2,
$$




$$
-\alpha_1\lambda_1+\beta_2\lambda_2+\gamma_3\lambda_3.
$$


Adding (4.2) supplies exactly $w_0,w_1$. There are no other boundary terms. ∎

Applying this identity to $h^{(0)},h^{(1)}$ shows


$$
a_0=A_0,\qquad a_1=A_1,
$$


with the notation of Turn 9.

### 4.1 Identification with the assigned kernel

The terminal-zero adjoint Green formula is


$$
\lambda_\ell
=
\sum_{j=\ell+1}^{b-1}
q_{j-\ell-1}(j)\,w_j.
$$


By the reused memory bound,


$$
\boxed{
\lambda_\ell
\equiv
\sum_{d=0}^{\min(H_K-1,b-\ell-2)}
q_d(\ell+d+1)\,w_{\ell+d+1}
=\Psi_\ell
\pmod{29^K}.
}
\tag{4.4}
$$



The head truncation of $f^0$ is valid because $A^{-1}$ and $L$ are integral at $29$. Thus $w_j$ in (4.4) is exactly the head contraction used in Turn 9(11.2), modulo the requested precision.

This is an actual adjoint telescoping identity for that kernel. Its right side still contains a potentially nonzero source contraction.

---

## 5. The two source impulses give an output difference, not a block-end zero

Write


$$
n=29m_0,\qquad b=29B+27.
$$


The supplied source calculation gives


$$
\mathcal H_{29q+26}
\equiv\mathcal H_{29q+27}
\equiv\kappa_q
:=\binom{2m_0+q}{B}\pmod{29},
$$


and zero on the other residue classes.

The original source rows stop at


$$
b-2=29B+25.
$$


Hence the complete impulse pairs occur for exactly


$$
0\le q<B.
$$



The source-only response to one equal pair has precisely


$$
\tau_{29q+27}=\kappa_q,\qquad
\tau_{29q+28}=-2\kappa_q
\pmod{29},
$$


and vanishes thereafter for that pair.

Consequently, for an arbitrary integral output vector $w$,


$$
\boxed{
\sum_{\ell=1}^{b-2}\mathcal H_\ell\lambda_\ell
\equiv
\sum_{q=0}^{B-1}
\kappa_q
\bigl(w_{29q+27}-2w_{29q+28}\bigr)
\pmod{29}.
}
\tag{5.1}
$$



Equivalently,


$$
\lambda_{29q+26}+\lambda_{29q+27}
\equiv w_{29q+27}-2w_{29q+28}\pmod{29}
$$


for those actual complete pairs.

This identifies the relevant output test. A vanishing phase-$2$ block-end state says nothing about the displayed weighted difference.

For the actual $w=\Gamma f^0$, common $29$-adic content can make its reduction zero. Equation (5.1) therefore does **not** prove an actual nonzero defect. It proves the operator-level obstruction to using block-end cancellation as a replacement for the source contraction. At the true norm depth, higher source digits and higher output digits must still be retained.

---

## 6. The complete finite-end contribution to the weighted contractions

For inputs $h,k$, define


$$
J(h,k)=(\mathsf Bh)^TL(\mathsf Bk),
$$




$$
v_h=\mathsf U^TL\mathsf Bh,
\qquad
G_{\rm end}=\mathsf U^TL\mathsf U.
$$


Using (3.1),


$$
\boxed{
\begin{aligned}
\mathcal Q(h,k)
&:=(A^{-1}h)^TL(A^{-1}k)\\
&\equiv
J(h,k)-c_h^Tv_k-v_h^Tc_k
+c_h^TG_{\rm end}c_k
\pmod{29^K}.
\end{aligned}
}
\tag{6.1}
$$



Thus the complete finite contact-end correction is


$$
\boxed{
-c_h^Tv_k-v_h^Tc_k+c_h^TG_{\rm end}c_k.
}
\tag{6.2}
$$


Its rank is bounded in terms of $K$, but its weighted contractions are not assumed to vanish.

For the actual first force, the exterior $+1$ contributes


$$
\boxed{
E_{\rm out}
=bW_b^2
\left((\mathsf Bf^0)_{b-1}-(\mathsf Uc_{f^0})_{b-1}\right).
}
\tag{6.3}
$$


This follows from


$$
\mathcal R^T(W_be_b)=bW_b^2e_{b-1}.
$$



Set


$$
A_a=\mathcal Q(f^0,h^{(a)}),\qquad a=0,1.
$$


Then the actual contractions are


$$
\boxed{
\mathcal N=f_0^0A_0+f_1^0A_1,
}
\tag{6.4}
$$




$$
\boxed{
\mathcal C
=r_0A_0+r_1A_1+\mathcal Q(f^0,\tau)+E_{\rm out}.
}
\tag{6.5}
$$



In particular, the complete source-plus-end contribution is


$$
\boxed{
\begin{aligned}
\mathcal Q(f^0,\tau)+E_{\rm out}
={}&J(f^0,\tau)
-c_{f^0}^Tv_\tau
-v_{f^0}^Tc_\tau\\
&+c_{f^0}^TG_{\rm end}c_\tau
+E_{\rm out}
\pmod{29^K}.
\end{aligned}
}
\tag{6.6}
$$



These formulas include both kinds of finite end:

- the contact-inverse correction caused by crossing $b-1$;
- the reconstructed exterior coordinate $j=b$.

They must not be merged into a fictitious extra recurrence step.

---

## 7. Explicit rational kernels for the finite operator products

The next reduction removes unevaluated original-length matrix products. It does not replace $\Gamma$ by a local matrix.

For a matrix $M$, use its bivariate kernel


$$
\mathscr K_M(x,y)=\sum_{i,j\ge0}M_{ij}x^iy^j.
$$


Finite bounds will be imposed by coefficient extraction, not by assuming an infinite inverse commutes with truncation.

### 7.1 The upper binomial transform

For $\mathsf R_{ij}=\binom{-n}{j-i}$,


$$
\boxed{
\mathscr K_{\mathsf R}(x,y)
=\frac{(1+y)^{-n}}{1-xy}
=
[u^{n-1}]
\frac1{(1-xy)(1-u+y)}.
}
\tag{7.1}
$$


This applies because the original $n$ is positive.

The exponent $n-1$ is an actual coefficient index. No expansion into a polynomial of degree $n$, and no replacement $n\mapsto n\bmod29^K$, is made.

### 7.2 The finite-difference transform

For $(\mathsf P_-)_{ij}=(-1)^{i-j}\binom ij$,


$$
\boxed{
\mathscr K_{\mathsf P_-}(x,y)
=\frac1{1+x-xy}.
}
\tag{7.2}
$$



### 7.3 The divided-power inverse

Equation (2.5) gives


$$
\boxed{
\mathscr K_{\mathsf D}(x,y)
=
\sum_{s=0}^{M_K}
c_s(n)\frac{x^s}{(1-xy)^{s+1}}.
}
\tag{7.3}
$$


Terms exceeding the finite matrix dimension are harmless because the finite coefficient gluing below rejects them.

### 7.4 The exact squared-weight tridiagonal kernel

Let


$$
\Delta=(1-u)(1-v)-xyuv.
$$


The generating function of $W_j^2$ is


$$
\sum_{j\ge0}W_j^2z^j
=
[u^{n+2}v^{n+2}]
\frac1{(1-u)(1-v)-zuv}.
$$


Differentiating with respect to $z$ gives the full tridiagonal kernel:


$$
\boxed{
\mathscr K_L(x,y)
=
[u^{n+2}v^{n+2}]
\left(
\frac1{\Delta}
+\frac{(1-x-y)uv}{\Delta^2}
+\frac{2xyu^2v^2}{\Delta^3}
\right).
}
\tag{7.4}
$$



This formula retains $W_j^2$, adjacent-coordinate weights, and the last diagonal contribution $b^2W_b^2$ after finite truncation.

### 7.5 The finite-end columns

For each $r<m$, (2.2) has the univariate kernel


$$
\boxed{
\sum_{j\ge0}F_{jr}z^j
=
-\sum_{u=0}^{r}\binom n{r-u}
[t^{b+u}v^{n-1}]
\frac1{(1-v+t)(1-zt)}.
}
\tag{7.5}
$$


The contact restriction $j<b$ is imposed separately. Thus the extraction index $b+u$ preserves the actual crossed endpoint.

All these rational functions have denominator nonzero at the origin.

---

## 8. Finite coefficient gluing: no hidden original-length sum

The following elementary identity is the finite boundary mechanism used throughout.

Suppose $F,G$ are vector generating functions and $K_1,\ldots,K_r$ are matrix kernels. Introduce variables $x_j,y_j$, $0\le j\le r$. Then


$$
\boxed{
\begin{aligned}
F^TK_1\cdots K_rG
={}&
\left[\prod_{j=0}^{r}x_j^{b-1}y_j^{b-1}\right]
F(x_0)G(y_r)\\
&\times
\prod_{a=1}^{r}K_a(y_{a-1},x_a)
\prod_{j=0}^{r}\frac1{1-x_jy_j},
\end{aligned}
}
\tag{8.1}
$$


where the left side means that **every** contracted index ranges over $0,\ldots,b-1$.

Indeed, at any node,


$$
[x^{b-1}y^{b-1}]
x^iy^j\frac1{1-xy}
=
\begin{cases}
1,&i=j<b,\\
0,&\text{otherwise}.
\end{cases}
$$


This proves (8.1) directly.

A fixed endpoint coordinate is extracted directly, for example by $[z^{b-1}]$, rather than represented by a high-degree monomial in a numerator. Transposition exchanges the two kernel variables.

### 8.1 Application to the main source contraction

The core term


$$
J(f^0,\tau)
=(f^0)^T\mathsf B^TL\mathsf B\tau
$$


uses exactly nine matrix factors:


$$
\mathsf P_-^T,\ \mathsf R^T,\ \mathsf D^T,\ \mathsf R^T,\
L,\
\mathsf R,\ \mathsf D,\ \mathsf R,\ \mathsf P_-.
\tag{8.2}
$$



Thus its finite matrix indices require $20$ gluing variables. The four $\mathsf R$ kernels add four parameter-extraction variables, and $L$ adds two. The source representation below adds at most two more.

Therefore $J(f^0,\tau)$ has a rational coefficient representation in at most $28$ variables.

The other terms in (6.6) have shorter matrix paths. Allowing all endpoint variants and separate bookkeeping, the uniform safe bound


$$
\boxed{V\le32}
\tag{8.3}
$$


is sufficient for every primitive coefficient extraction used here.

The finite endpoint inverse is first evaluated as the $t_0\times t_0$ unit matrix problem (2.8); its powers do not introduce a growing number of coefficient variables.

This is the distinction from a contact-word expansion whose number of summation variables increases with the word length.

---

## 9. The complete source and the remaining high-index coefficient target

Define


$$
R_s(t)=\sum_{k=0}^s
\binom n{s-k}\frac{t^k}{(1-t)^{k+1}}.
$$


Then


$$
\sum_{i\ge0}\binom{n+i}{s}t^i=R_s(t).
$$



Let


$$
s_{\max}=\min(2n+2,M_K).
$$


The complete source generating function is


$$
\mathscr H(z)
\equiv
[X^b]\sum_{s=0}^{s_{\max}}
a_s(n+1)s!(1+X)^{2n+1-s}
R_s(z(1+X))
\pmod{29^K}.
\tag{9.1}
$$


The source rows used in the actual problem remain $1,\ldots,b-2$.

Put


$$
\Theta=z\frac{d}{dz},
\qquad
\mathscr H_+(z)=\mathscr H(z)-\mathscr H(0).
$$


The reused finite-memory law gives


$$
\boxed{
\mathscr T(z)
=
\sum_{d=0}^{H_K-1}
z^{d+1}q_d(\Theta+d+1)\mathscr H_+(z),
}
\tag{9.2}
$$


whose coefficients below degree $b$ are the actual $\tau_j$ modulo $29^K$.

Because $\mathscr H_+$ has no constant term,


$$
\tau_0=\tau_1=0.
$$


When $\tau_j$ with $j<b$ is extracted, only source rows $\ell<j\le b-1$ occur. Hence no source row after $b-2$ is inserted.

### 9.1 Keeping parameter exponents exact

For $2n+1-s\ge0$, replace


$$
(1+X)^{2n+1-s}
$$


by


$$
\boxed{
[v^{2n+1-s}]
\frac1{1-v(1+X)}.
}
\tag{9.3}
$$



There is one possible exceptional exponent: if $s=2n+2$ lies within the truncation, retain the factor


$$
(1+X)^{-1}
$$


directly. It is a rational function with unit constant denominator, not a coefficient extraction at a negative index.

Thus each source atom has genuine extraction indices


$$
X^b,\qquad v^{2n+1-s},
$$


or the explicitly handled exceptional rational factor.

The pole order in $1-z(1+X)$ is at most


$$
s+1+(H_K-1)\le87K.
$$


After multiplication by $z^{d+1}$, a safe bound for the numerator degree in $z$ is $145K$.

### 9.2 The actual high-index target

Let


$$
\mathfrak C_K(h,k)
$$


denote the explicitly constructed coefficient expression (6.1), with its scalar terms evaluated using (7.1)–(9.3) and finite gluing (8.1).

This is no longer an unspecified $A^{-1}$, adjoint solution, or original-length sum: its rational factors and extraction indices have been given.

Then the local target is exactly


$$
\boxed{
\begin{aligned}
&\mathfrak C_K(f^0,\tau)+E_{\rm out}\\
&\quad +(r_0-29\rho_nf_0^0)\,
\mathfrak C_K(f^0,h^{(0)})\\
&\quad +(r_1-29\rho_nf_1^0)\,
\mathfrak C_K(f^0,h^{(1)})
\equiv0\pmod{29^K},
\end{aligned}
}
\tag{9.4}
$$


at


$$
\boxed{K=v_{29}(\mathcal N)+2.}
\tag{9.5}
$$



For the main core source term, the coefficient targets consist of:

- $20$ finite-index gluing exponents equal to $b-1$;
- four exponents $n-1$ from the upper transforms;
- two exponents $n+2$ from the squared weights;
- the actual source exponents $b$ and $2n+1-s$.

Endpoint terms use the corresponding actual indices $b+u$ and $b-t_0+v$, not completed blocks.

Equation (9.4) is the concrete follow-on coefficient lemma. Its vanishing is not proved here.

---

## 10. Construction size and an explicit Cartier cost bound

The representation above has a genuine fixed number of variables, but fixed-variable rationality alone is not a practical complexity theorem.

### 10.1 Rational-function construction bounds

One can put each divided-power kernel over a common denominator $(1-xy)^{M_K+1}$, and group the source’s $d$-sum at each $s$. Direct degree bookkeeping gives the following deliberately loose bounds for each primitive rational coefficient problem:


$$
\boxed{
V\le32,\qquad
\deg_{x_j}P,\deg_{x_j}Q\le D_K:=256K+16,
\qquad Q(0)=1.
}
\tag{10.1}
$$



The largest variable degree comes from the source numerator, bounded above by $145K$, plus its gluing factor. The bound $D_K$ also covers the endpoint atoms and the tridiagonal kernel.

Expanding endpoint-column choices externally, rather than increasing the number of variables, gives a safe polynomial bound


$$
\boxed{
T_K\le100(29K+2)^4
}
\tag{10.2}
$$


for the number of primitive coefficient problems required for the norm, the two initial charges, the source contraction, and the exterior term.

These bounds treat the actual head coefficients and the finite small-index symbol coefficients as supplied arithmetic inputs. Their generation is a separate, accepted digit/binomial task and is not silently charged zero.

### 10.2 A transparent prime-power section construction

The following is the elementary rational-section mechanism underlying the prime-power rational/diagonal methods represented by Rowland–Yassawi. It is stated explicitly here to avoid importing an unstated feasible-state conclusion.

For a rational function $P/Q$ over $\mathbb Z/29^K\mathbb Z$, put


$$
E_K=29^{K-1}.
$$


Then


$$
\frac P Q=\frac{PQ^{E_K-1}}{Q^{E_K}}.
$$


The congruence


$$
Q(\mathbf x)^{29E_K}
\equiv Q(\mathbf x^{29})^{E_K}\pmod{29^K}
$$


follows by lifting the Frobenius congruence.

Therefore a multivariate Cartier section $\Lambda_{\mathbf d}$ acts by


$$
\boxed{
\frac{S}{Q^{E_K}}
\longmapsto
\frac{\Lambda_{\mathbf d}
\!\left(SQ^{28E_K}\right)}
{Q^{E_K}}.
}
\tag{10.3}
$$


A coordinatewise numerator degree bound $E_KD_K$ is stable under these transitions.

Thus a dense numerator representation needs at most


$$
\boxed{
\mathcal M_K=(D_K29^{K-1}+1)^{32}
}
\tag{10.4}
$$


coefficient slots.

Let


$$
L_{\rm par}
=
1+\left\lfloor
\log_{29}(2n+b+M_K+3)
\right\rfloor.
$$


A conservative dense arithmetic implementation of all the required coefficient extractions has ring-operation cost bounded by


$$
\boxed{
O\!\left(
T_K(K+L_{\rm par})\,29^{64}\mathcal M_K^2
\right),
}
\tag{10.5}
$$


with storage bounded by


$$
O(29^{32}\mathcal M_K)
$$


when tasks are processed sequentially.

These are explicit bounds, not a bare $29^{\operatorname{poly}(K)}$ existence claim.

They are also plainly unsuitable as a practical implementation. Already


$$
\mathcal M_2=15313^{32},
$$


roughly $10^{134}$ dense coefficient slots.

The established rational/Cartier literature, including the supplied Rowland–Yassawi, Bostan–Christol–Dumas, and newer prime-power state-complexity references, is relevant background for improving this representation. None is being asserted to prove that this parameter-dependent weighted/contact kernel has a small reachable module.

### 10.3 What has and has not been achieved

The advance is the **explicit fixed-variable representation and the elimination of a variable count growing with inverse-word length**.

What remains unavailable is a small closed module adapted to these particular rational factors, or an algebraic cancellation proving (9.4) without evaluating the large coefficient targets.

---

## 11. Complete initial force, logarithmic protection, and the true norm digit

The complete initial values remain


$$
\boxed{
r_i=
\sum_s a_s(n)(n+i)_{\underline s}
\left(
T_{2n+i-s}+\frac{L_{2n+i-s}}{b!}
\right),
\qquad i=0,1,
}
\tag{11.1}
$$


where


$$
T_m=\frac1{b!}\sum_{q=b}^m(m)_{\underline q},
$$




$$
L_0=0,\qquad
L_m=mL_{m-1}+2(m-1)!u_{m-1},
$$


and $u_r=[z^r]\phi(z)^{-1}$.

The source telescope does not remove these initial logarithmic terms.

Retain


$$
N_{\log}
=
2v_{29}(n!)-v_{29}(b!)
-\lfloor\log_{29}(2n+b-1)\rfloor.
$$


For


$$
P=29^cx,\qquad x\ \text{primitive},\qquad
\nu=v_{29}(x^Tx),
$$


the accepted relative protection estimate is


$$
v_{29}\!\left(
\frac MD-\frac{M^{(e)}}D
\right)
\ge N_{\log}-c-3-\nu.
$$


Thus omission in the normalized ratio modulo $29$ requires


$$
\boxed{N_{\log}\ge c+4+\nu.}
\tag{11.2}
$$



The whole primitive-norm loss $\nu$ is retained.

### 11.1 Nonvanishing and precision

The first force is nonzero, $A$ is invertible, and the finite reconstruction is injective. Hence


$$
\mathcal N=Z_w^TZ_w>0
$$


over the reals. In particular,


$$
d:=v_{29}(\mathcal N)<\infty.
$$



This does not give a useful bound on $d$. The appropriate test remains


$$
\mathcal N\bmod29^{d+1},
\qquad
\mathcal C\bmod29^{d+2}.
$$



If $v_{29}(\mathcal C)<d+1$, the local alignment fails. Otherwise,


$$
\boxed{
\delta_{\rm act}
=
\left(\frac{\mathcal C}{29^{d+1}}\right)
\left(\frac{\mathcal N}{29^d}\right)^{-1}
-\rho_n
\pmod{29}.
}
\tag{11.3}
$$


Only the demonstrated unit $\mathcal N/29^d$ is inverted.

The independent $\rho_n=(6C_n)^{-1}$ must be supplied from its original definition. The attached material does not reproduce a complete evaluator for $C_n$. It is not permissible to define $\rho_n$ from $M/D$.

---

## 12. The precise obstruction and a follow-on lemma

The finite adjoint telescope is valid, but it does not force its source term to vanish. The contact factorization is complete, but its finite-end correction is not orthogonal to the source by construction. The rational representation is explicit, but rationality does not imply the high coefficient in (9.4) is zero.

The outstanding issue is therefore not another recurrence memory bound.

### Concrete follow-on lemma

> **Boundary-aware rational coefficient alignment lemma.**  
> On the original orbit
> 

$$
> b=3^{249005515+574312172u},\qquad n=2001b,\qquad u\ge0,
>
$$


> prove that the explicit coefficient combination (9.4), constructed from kernels (7.1)–(7.5), source (9.1)–(9.3), and the complete endpoint correction (6.1)–(6.3), vanishes at
> 

$$
> K=v_{29}(\mathcal N)+2;
>
$$


> or evaluate one original input at that precision and obtain a nonzero certificate (11.3), or a lower-valuation failure.

A potentially useful structural refinement would be a small invariant module for the rational sections of these **specific factors**, including the endpoint atoms and squared-weight kernel. To count as a completed compression, such a result must give actual reduction identities and dimensions, not merely rename each transformed function as another kernel.

Even a proof of this follow-on lemma would establish only the local $29$-adic law.

---

## 13. Bounded exact arithmetic proposed for personal inspection

No finite calculation is needed to justify the symbolic identities above. The following bounded calculation would audit their implementation.

### Auxiliary full-boundary test

Use


$$
\boxed{
n=203,\qquad b=143=29\cdot4+27,\qquad K=2.
}
$$


This is **not** an original-family index.

Here:

- contact coordinates are $0,\ldots,142$;
- source rows are $1,\ldots,141$;
- reconstructed coordinates are $0,\ldots,143$;
- $M_K=m=t_0=57$;
- homogeneous head support is bounded by $118<143$;
- the last source block ends at phase $25$, so the final impulse pair is not artificially inserted.

#### Inputs

1. The exact contact entries
   

$$
A_{ij}
   =\sum_s a_s(n)(n+i)_{\underline s}
   \binom{2n+i-s}{j}.
$$


2. The two homogeneous inputs and the complete particular source.
3. The actual weights $W_j=\binom{205}{j}$.
4. The finite matrices and coefficients in Sections 2–7.

#### Expected verifiable outputs

1. **Divided-power inverse**
   

$$
H\mathsf D-I=0\pmod{841}.
$$



2. **Complete contact inverse**
   

$$
A\left(
   \mathsf B-\mathsf U\mathsf S_{\rm end}^{-1}\mathsf V
   \right)-I=0\pmod{841}.
$$



3. **Actual adjoint kernel**  
   Agreement, for every $1\le\ell\le141$, between:
   - backward recurrence (4.1);
   - the finite-lag kernel (4.4);
   - direct contraction using the finite inverse.

4. **Finite-end accounting**  
   Agreement of the direct weighted contractions with (6.1), with the three contact-end terms and the exterior term reported separately.

5. **Rational coefficient audit**  
   Agreement between direct finite sums and coefficient formulas for:
   - the $\mathsf R,\mathsf P_-,\mathsf D,L$ kernels;
   - each finite-end column $F_r$;
   - $J(f^0,\tau)$ and its complete correction (6.6).

6. **Impulse/output identity**  
   Verification modulo $29$ of (5.1), using exactly $q=0,1,2,3$, not a completed fifth pair.

For an optional complete-force audit in this auxiliary system, generate the logarithmic and factorial data exactly through source index


$$
2n+b-1=548.
$$


Do not invoke an original-family logarithmic omission bound for this auxiliary input.

Expected outputs are zero discrepancies in these identities, not a predicted normalized defect.

### Original-index calculation

A genuine local-law certificate still requires an actual original $u$, exact parameter digits, complete initial force or a certified logarithmic budget, the independent $\rho_n$, and a nonzero norm digit.

At bounded precision $K_{\max}$, an output


$$
\mathcal N\equiv0\pmod{29^{K_{\max}}}
$$


certifies only


$$
v_{29}(\mathcal N)\ge K_{\max}.
$$


The present report does not provide a feasible original-index implementation, and does not disguise the dense bound in Section 10 as one.

---

## 14. Full gcd, primitive denominator, and whole evaluated error

The least actual two-column clearer remains $d_B$. Retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


The final reduction is


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad
q_n=\frac{A_B}{g_B}>0.
}
\tag{14.1}
$$


The primitive multiplier remains $d_B^2/g_B$.

With


$$
F_m=v_{29}(m!),\qquad
\delta=v_{29}(D),\qquad
\mu=v_{29}(M),
$$


retain


$$
v_{29}(g_B)
=
\min\{4F_n+4+\delta,\ 2F_n+F_b+5+\mu\},
$$




$$
\boxed{
v_{29}(q_n)
=
\max\{0,\ 2F_n-F_b-1+\delta-\mu\}.
}
\tag{14.2}
$$



An affirmative local law would give $\delta=\mu$, since $\rho_n$ is a unit. It would settle only this local contribution.

The actual primitive denominator still requires


$$
\boxed{
\log q_n
=
\sum_{\ell}
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
}
\tag{14.3}
$$



For


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the whole evaluated error remains


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
\tag{14.4}
$$


At the retained scope of the complete signed-error theorem,


$$
\epsilon_n>0\quad\text{eventually},
$$


and


$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$



No componentwise error replaces this whole same-index expression. No all-prime denominator estimate sufficient to make the whole nonzero evaluated form tend to zero is obtained.

---

## Proof-status ledger

| Statement | Status |
|---|---|
| Turn 9 symbolic monodromy and $58K+1$ memory | Reused at the requested scope |
| Homogeneous and actual first-force head support | Reused with exact precision bounds |
| Divided-power interior contact inverse | Proved here |
| Complete finite inverse with endpoint correction | Derived from the accepted finite factorization |
| Terminal-zero adjoint telescope for the actual $\Psi_\ell$ | Proved here |
| Equal source impulses produce an output difference, not block-end cancellation | Proved as a finite operator identity |
| Complete weighted contact-end and exterior contributions | Explicit identities |
| Fixed-variable rational coefficient representation | Constructed here |
| Parameter exponents retained exactly | Yes |
| Dense Cartier implementation cost | Explicit, but impractical |
| Small usable section module for this kernel | Open |
| Original-family norm-relative congruence at the true norm digit | Open |
| Original normalized defect | Not computed |
| Full gcd/primitive-denominator/whole-error comparison | Open |

## Conclusion

The new result is an **actual finite adjoint telescope together with a complete finite-boundary, fixed-variable rational coefficient representation of the head-to-source output contraction**.

The essential new simplification is


$$
(H^{-1})_{jk}
=
(j-k)![z^{j-k}]\phi(z)^{-n}\binom jk,
$$


which makes the interior inverse precision-sized and leaves the finite contact boundary as an explicit unit rank correction. The actual squared weights and the exterior $+1$ remain present throughout.

The exact remaining local bottleneck is the vanishing of the concrete high-index coefficient combination (9.4) at


$$
K=v_{29}(\mathcal N)+2.
$$


Neither short input memory nor the finite adjoint telescope proves that vanishing. The proposed bounded auxiliary calculation can audit the formulas, but cannot establish the original-family law.

Even an affirmative resolution would leave the full all-prime gcd, actual primitive denominator, and whole nonzero evaluated error to be compared.



$$
\boxed{
\text{An unconditional proof or disproof of the irrationality of }e+\pi
\text{ remains unresolved.}
}
$$


