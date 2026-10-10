> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1, Turn 4 — The depth-seven residue-class radical, the actual force, and the next endpoint operator

## Executive conclusion

The main new conclusion is **not** nonsingularity of the depth-seven binomial matrix. It is the opposite:



$$
\boxed{\mathcal C _7\text{ is singular throughout the original domain.}}
$$



The reason is structural. After the correct residue-class decomposition, the true endpoint


$$
\nu=D/2-1
$$


leaves one class shorter than the others. Consequently, the decomposed form contains a rectangular block and its transpose. At least one radical direction is unavoidable.

More precisely, the results below give:

1. A proof of the genuinely broader $D<H/972$ core-return estimate, using the finite-boundary mechanism already established in A1 turn25/A4 turn26, but with a sharper divisible-lift width budget:
   

$$
V\widehat E^{-1}V^T\equiv0\pmod{729}.
$$


   Together with the independently reviewed transfer and force-strip results of A1 turn2/A4 turn5, this gives
   

$$
\boxed{\mathscr R_{\rm act}/3^7\equiv\mathcal C _7+\mathcal F_R\pmod3.}
$$



2. An explicit integral residue-class permutation for $\mathcal C _7$, including its **actual unequal class sizes**, radical, image, and endpoint projection. The remaining coefficient arithmetic is reduced to two binomial Hankel matrices of order
   

$$
s=\frac{D}{2\cdot3^{v_3(j)+1}},
$$


   and one $s\times(s-1)$ truncation.

3. An exact criterion for complete degeneration of the core digit:
   

$$
\boxed{\mathcal C _7=0\quad\Longleftrightarrow\quad D<H/2916.}
$$


   On the larger region $D<H/2187$, its ranks and radical are given explicitly by triangular blocks, and the endpoint is outside its image.

4. A complete residue-block formula for the **actual** $\mathcal F_R$, without supposing that it vanishes.

5. A rigorous Schur compression of a singular actual depth-seven digit to the actual operator on its radical. If the whole digit vanishes, a complete next-digit formula is given, retaining the LOW cross terms, all relevant force poles, and carries.

There is an important unresolved producer issue:

> The supplied sources do not prove from the derangement producer that
> 

$$
> 3P_n-Q_c\in3^7\mathbb Z_3[y]\qquad(v_3(j)\ge5).
>
$$


> A4 turn26 explicitly identified this missing interface. Therefore I do **not** treat the assertion $R\equiv0\pmod3$, and hence $\mathcal F_R=0$, as established merely because it was repeated in later sources.

I give below an exact producer-level formulation of the missing congruence and a weaker, sufficient strip lemma. The core radical results are unconditional algebraic results on the stated parameters. Their identification with the **actual** depth-seven radical on $v_3(j)\ge5$ remains conditional on this producer issue.

No tools were used. No original-index computation is claimed.

---

## 1. Domain, accepted scope, and normalization

Retain the entire original domain


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$




$$
A=n-2=H-D,\qquad H=3^{h-1},\qquad 0<D<H/972.
$$


Also retain


$$
m=\frac{A+1}{2},\qquad
d=\frac{3D}{2}-1,\qquad
\nu=\frac D2-1,
$$




$$
r_1=\frac{H-1}{2},\qquad r_*=\frac{3H-1}{2}.
$$



The actual columns are unchanged:


$$
U_a=(y-1)^a\quad(0\le a<D),\qquad
z_i=y^i(y-1)^D\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m).
$$



The complete functional is


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\!\!\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1}.
\tag{1.1}
$$


Thus the factorial force, endpoint subtraction, and original finite cutoff remain part of every exact definition.

Write


$$
Q_c=(y+1)(y-1)^A(\beta+3y),\qquad \beta=-71-A,
$$


and use the retained order-six approximation


$$
Q_n^{\rm loc}=3P_n=Q_c+729R,\qquad R\in\mathbb Z_3[y].
\tag{1.2}
$$



For the core blocks,


$$
G_c(U,U)=3L,\quad G_c(U,Y)=3X,\quad
G_c(U,Z)=3B,\quad G_c(Z,Y)=3V,
$$




$$
\widehat E=E-3X^TL^{-1}X,\qquad
\widetilde V=V-B^TL^{-1}X.
$$


The exact residual in the **full scaled-matrix normalization** is


$$
\mathscr R_c
=
G_c(Z,Z)-3B^TL^{-1}B
-9\widetilde V\widehat E^{-1}\widetilde V^T.
\tag{1.3}
$$



### What is reused

A1 turn25/A4 turn26 already establish finite-boundary core closure on


$$
D<\frac{H}{512(r+1)^2\,3^{r-1}},
$$


with fixed $r$, and establish the precision-protection argument under its stated polynomial-approximation hypothesis. I do not claim that mechanism as new.

A1 turn2/A4 turn5 independently establish, at the retained order-six interface:

- the actual/core transfer modulo $3^7$;
- $B\in3^6M(\mathbb Z_3)$;
- the next actual-force strip;
- the actual transported endpoint modulo $3$.

What requires a new argument is the substantially broader $H/972$ width budget and the resulting depth-seven core digit.

---

## 2. The broader finite-boundary estimate

This section supplies a proof of the broader assertion rather than accepting turn3 by repetition. The phase tables in turn3 are not needed for this proof.

Set


$$
\omega=H/243.
$$


LTE gives


$$
v_3(A)=1+v_3(j)\ge5.
$$


Since $h\ge9$, both $D$ and $\omega$ are divisible by $27$. Therefore


$$
\boxed{\omega-4D\ge27.}
\tag{2.1}
$$



For $W\ge0$, put


$$
I(W)=\{t\omega+u:t\in\mathbb Z,\ |u|\le W\},
$$




$$
J(W)=
\left\{\frac{(2t+1)\omega-1}{2}+u:
t\in\mathbb Z,\ |u|\le W\right\}.
$$


Their supports are disjoint whenever


$$
W_1+W_2<\frac{\omega-1}{2}.
\tag{2.2}
$$



### 2.1 The input and inverse supports

The reviewed beta valuation, including the exceptional shifted top endpoint, gives


$$
\operatorname{supp}(V_{i,\bullet}\bmod729)\subseteq J(\nu).
\tag{2.3}
$$


This uses the valuation formula only on its valid range


$$
0\le s\le(H-3)/2;
$$


the shifted argument $s=(H-1)/2$ is treated separately.

At the two required precisions,


$$
(1-z)^{-A}\equiv(1-z)^D S(z^\omega)
$$


for a scalar series $S$, modulo $243$ or modulo $729$. The exact finite HIGH inverse remains


$$
(R_H)_{ab}=[z^{d+m-a-b}](1-z)^{-A},
\qquad d\le a,b\le m.
\tag{2.4}
$$



For a HIGH polynomial $p$, define


$$
\pi(p)=p-\operatorname{rem}_{(y-1)^D}p.
$$


Say $p\in\mathcal C(W)$ if


$$
\pi(p)=(y-1)^Dq,\qquad \operatorname{supp}q\subseteq I(W).
$$



If $w$ has support in $J(W)$, $W\ge\nu$, the HIGH coefficients of $R_Hw$ are obtained from


$$
(y-1)^D
\sum_b w_b\sum_{u\ge0}s_u y^{r_1-b-u\omega}.
\tag{2.5}
$$


All surviving quotient exponents lie in $I(W)$.

This calculation respects both finite boundaries:

- negative quotient exponents cannot reach degree $d>D$;
- the upper degree is at most $m$;
- the correction introduced by discarding degrees below $d$, followed by monic division, has quotient degree at most
  

$$
d-1-D=\nu-1.
$$



Hence


$$
\boxed{R_H(J(W))\subseteq\mathcal C(W)}
\tag{2.6}
$$


at either stated precision. This is a statement about the finite matrix (2.4), not an infinite convolution replacement.

### 2.2 The complete projected $F$

Put


$$
F=(\widehat E-E_0)/3.
$$


Suppose $p\in\mathcal C(W)$ and


$$
W+D<(\omega-1)/2.
\tag{2.7}
$$



For $\pi(p)=(y-1)^DQ$, the LOW pairing after division by $3$ extracts coefficients from


$$
(y-1)^H(y-1)^a(\beta+3y)Q.
$$


Using


$$
(y-1)^H\equiv(y^\omega-1)^{243}\pmod{729},
$$


all coefficients capable of meeting a pole modulo $243$ lie in an integer-grid band of width at most $W+D$. Every contributing pole lies on the half-grid. Thus


$$
G_c(U,\pi(p))/3\equiv0\pmod{243}.
\tag{2.8}
$$



If $p-\pi(p)=Ur$, this says


$$
Xp\equiv Lr\pmod{243}.
$$


Consequently,


$$
\widehat Ep\equiv G_c(Y,\pi(p))\pmod{729}.
\tag{2.9}
$$



Equation (2.9) is the essential LOW-correction step: the term


$$
3X^TL^{-1}X
$$


subtracts the actual remainder. It is not deleted.

The same coefficient-gap argument for the HIGH pairings, with the extra linear factor, gives support in $J(W+1)$. The $E_0$ term has support in $J(W)$; it annihilates the remainder exactly by degree. Therefore


$$
\boxed{\operatorname{supp}(Fp\bmod243)\subseteq J(W+1).}
\tag{2.10}
$$



The factorial terms vanish at these precisions because their depth, even after the one division, is at least $h-1\ge8$.

### 2.3 Closing the return words

From (2.3), (2.6), and (2.10),


$$
(R_HF)^\ell R_HV_j^T\in\mathcal C(\nu+\ell)
\qquad(0\le\ell\le5)
\pmod{243}.
$$


The combined support width in the final contraction is at most


$$
\nu+(\nu+\ell+D)=2D-2+\ell.
$$


For $\ell\le5$, (2.1) makes this strictly less than $(\omega-1)/2$. Thus


$$
V(R_HF)^\ell R_HV^T\equiv0\pmod{243},
\qquad0\le\ell\le5.
\tag{2.11}
$$



For $\ell=0$, the same direct inverse argument works modulo $729$. The six-term inverse expansion then gives


$$
\boxed{V\widehat E^{-1}V^T\equiv0\pmod{729}.}
\tag{2.12}
$$



This proves the broader-window assertion. It does not extend the old fixed-depth theorem to a growing depth.

---

## 3. The resulting depth-seven formula

Since $B\in729M$, equation (1.3) and (2.12) give


$$
\mathscr R_c\equiv G_c(Z,Z)\pmod{3^8}.
\tag{3.1}
$$



The direct beta calculation has only one possible contribution after division by $3^7$. Writing


$$
\varrho=\frac{H/729-1}{2},
$$


the relevant shift is $i+j+t=\varrho$. Its normalized unit is $1\pmod3$, while the extra-$3$ beta summand and the factorial term vanish at this digit. Hence


$$
\frac{G_c(z_i,z_j)}{3^7}
\equiv
[y^{\varrho-i-j}](y-1)^D\pmod3.
\tag{3.2}
$$



The already reviewed actual-force result gives


$$
\frac{\mathscr R_{\rm act}-\mathscr R_c}{3^7}
\equiv\mathcal F_R\pmod3,
$$


where


$$
(\mathcal F_R)_{ij}
=[y^{r_1-i-j}]
\frac{R(y)(y-1)^{2D}-R(-1)(-2)^{2D}}{y+1}.
\tag{3.3}
$$



Therefore


$$
\boxed{
\mathscr R_{\rm act}\in3^7M_\nu(\mathbb Z_3),\qquad
\mathscr R_{\rm act}/3^7\equiv\mathcal C_7+\mathcal F_R\pmod3.
}
\tag{3.4}
$$



In particular, the depth-six digit is zero. The genuinely new question is the actual depth-seven sum, not another proof of narrow-window fixed-depth closure.

---

## 4. The stronger producer congruence is not yet justified

The actual producer is


$$
P_n(y)=y^n-\sum_{a=0}^{n-1}(C_n^{-1}f_n)_a y^a,
$$


with


$$
(C_n)_{ab}=D_{2(a+b)}-(-1)^{a+b},
\qquad
(f_n)_a=D_{2(n+a)}-(-1)^{n+a}.
\tag{4.1}
$$



The implication


$$
v_3(j)\ge5
\quad\Longrightarrow\quad
3P_n-Q_c\in3^7\mathbb Z_3[y]
\tag{4.2}
$$


does **not** follow formally from the retained order-six approximation. Increasing $v_3(j)$ supplies additional divisibility of $A$, but it does not by itself prove additional divisibility of the solution of the highly nonunit system (4.1).

A4 turn26 expressly states that the arbitrary-depth approximation was not derived from the producer. That qualification survives in the present task.

### 4.1 An exact producer-level formulation

Let


$$
\Delta_n=\det C_n,\qquad w_n=\operatorname{adj}(C_n)f_n,
$$


and write


$$
Q_c=3y^n+\sum_{a<n}c_a y^a.
$$


Then, exactly,


$$
[y^a](3P_n-Q_c)
=\frac{-3(w_n)_a-\Delta_n c_a}{\Delta_n}.
\tag{4.3}
$$



Thus (4.2) is equivalent to the following coefficientwise statement:


$$
\boxed{
v_3\!\left(-3(w_n)_a-\Delta_n c_a\right)
\ge v_3(\Delta_n)+7
\quad(0\le a<n).
}
\tag{4.4}
$$



The determinant content in (4.4) is essential. A numerator congruence modulo $3^7$ without the additional $v_3(\Delta_n)$ does not prove (4.2).

### 4.2 A weaker sufficient lemma

For the depth-seven application, the full congruence (4.2) is stronger than necessary. It suffices to prove


$$
\boxed{
[y^t]\,
\frac{R(y)(y-1)^{2D}-R(-1)(-2)^{2D}}{y+1}
=0\pmod3
}
\tag{4.5}
$$


for precisely


$$
r_1-(D-4)\le t\le r_1.
$$



Equation (4.5) is a concrete producer-strip lemma. It can be formulated from (4.3) without any arbitrary replacement of $R$.

**Status:** neither (4.4) nor its sufficient strip version (4.5) is proved here. Accordingly, the statement $\mathcal F_R=0$ on $v_3(j)\ge5$ remains conditional. The following evaluation of $\mathcal C_7$ does not depend on that assertion.

---

## 5. Arithmetic parameters for the true residue decomposition

Put


$$
t=v_3(j)+1,\qquad g=3^t.
$$


Because $0<A<H$,


$$
v_3(D)=v_3(A)=t.
$$


Write


$$
D=g\delta=2gs,\qquad 3\nmid\delta,\qquad \delta=2s.
\tag{5.1}
$$


In particular, $3\nmid s$.

Since


$$
H/g>972\delta\ge1944,
$$


we have


$$
H/(729g)=L=3^w,\qquad w\ge1.
$$


Define


$$
a_0=\frac{g-1}{2},\qquad
\eta=\frac{L-1}{2}.
\tag{5.2}
$$


Then


$$
\varrho=g\eta+a_0,\qquad
\nu=gs-1,
\tag{5.3}
$$


and the real window is


$$
2s=\delta<\frac{3L}{4}.
\tag{5.4}
$$



On the specifically requested subfamily $v_3(j)\ge5$, $g\ge729$. The same decomposition already applies on the whole original domain, where $g\ge243$.

---

## 6. Explicit decomposition, radical, image, and endpoint

### 6.1 The integral permutation and its unequal class sizes

Every actual residual index has a unique expression


$$
i=ga+r,\qquad 0\le r<g.
$$


The number of indices in class $r$ is


$$
n_r=
\begin{cases}
s,&0\le r\le g-2,\\
s-1,&r=g-1.
\end{cases}
\tag{6.1}
$$



Grouping indices by $r$ is an integral permutation of the actual $\nu$ coordinates. No coordinate is added.

In $\mathbb F_3[y]$,


$$
(y-1)^D=(y^g-1)^{2s}.
$$


Consequently, a block between classes $r,r'$ can be nonzero only when


$$
r+r'\equiv a_0\pmod g.
\tag{6.2}
$$



Define the involution


$$
\sigma(r)=a_0-r\pmod g.
$$


For $r\le a_0$, $r+\sigma(r)=a_0$; for $r>a_0$, it equals $a_0+g$.

Set


$$
(H_0)_{ab}=[x^{\eta-a-b}](x-1)^{2s},
\qquad0\le a,b<s,
\tag{6.3}
$$




$$
(H_1)_{ab}=[x^{\eta-1-a-b}](x-1)^{2s},
\qquad0\le a,b<s,
\tag{6.4}
$$


and let


$$
J=H_1[:,0,\ldots,s-2],
\tag{6.5}
$$


an $s\times(s-1)$ matrix.

The two exceptional paired classes are


$$
r_+=a_0+1,\qquad r_-=g-1.
\tag{6.6}
$$


They are coupled by $J$ and $J^T$, not by a square copy of $H_1$.

This missing final coordinate is the decisive finite-endpoint effect.

### 6.2 Rank and radical

Let


$$
N_0=\frac{g+1}{2},\qquad N_1=\frac{g-1}{2},
$$


and let


$$
\rho_0=\operatorname{rank}H_0,\qquad
\rho_1=\operatorname{rank}H_1,\qquad
\rho_J=\operatorname{rank}J
$$


over $\mathbb F_3$. Then


$$
\boxed{
\operatorname{rank}\mathcal C_7
=N_0\rho_0+(N_1-2)\rho_1+2\rho_J.
}
\tag{6.7}
$$



The radical is the following direct sum in the permuted coordinates:

- in every class $0\le r\le a_0$: a copy of $\ker H_0$;
- in every class $a_0<r<g$, except $r_+,r_-$: a copy of $\ker H_1$;
- in class $r_+$: $\ker J^T\subseteq\mathbb F_3^s$;
- in class $r_-$: $\ker J\subseteq\mathbb F_3^{s-1}$.

In particular,


$$
\dim\ker J^T\ge1,
$$


so


$$
\boxed{\det\mathcal C_7=0.}
\tag{6.8}
$$



Even if both square matrices are nonsingular, the true matrix $\mathcal C_7$ is not.

### 6.3 Image

The image is equally explicit:

- class $r\le a_0$: $\operatorname{im}H_0$;
- regular class $r>a_0$: $\operatorname{im}H_1$;
- class $r_+$: $\operatorname{im}J$;
- class $r_-$: $\operatorname{im}J^T$.

This statement includes all finite endpoint corrections.

### 6.4 Projection of the actual endpoint

Put


$$
\epsilon_q=(1,-1,\ldots,(-1)^{q-1})^T.
$$


Since $g$ is odd, the actual endpoint in class $r$ is


$$
\overline e_r=(-1)^r\epsilon_{n_r}.
\tag{6.9}
$$



If a radical vector in class $r$ is represented by


$$
f(x)=\sum_a f_a x^a,
$$


its endpoint pairing is exactly


$$
\boxed{\overline e_r^{\,T}f=(-1)^r f(-1).}
\tag{6.10}
$$



Thus the endpoint projection onto the radical is not an unspecified distinguished vector: it is evaluation at $-1$ on each of the listed kernel polynomial spaces.

Equivalently,


$$
\overline e\in\operatorname{im}\mathcal C_7
$$


if and only if


$$
\boxed{
\epsilon_s\in\operatorname{im}H_0,\qquad
\epsilon_s\in\operatorname{im}J,\qquad
\epsilon_{s-1}\in\operatorname{im}J^T.
}
\tag{6.11}
$$


The separate $H_1$ condition is redundant because
$\operatorname{im}J\subseteq\operatorname{im}H_1$.

This reduces endpoint-image membership from the original $(gs-1)$-dimensional matrix to three tests of size at most $s$.

---

## 7. What is explicitly evaluable without a digit-dependent rank calculation

### 7.1 Exact criterion for the entire core digit to vanish

The largest possible coefficient index reached in $H_1$ is controlled by


$$
\eta-1-a-b.
$$


If $L>4\delta$, then $\eta\ge2\delta$, so both $H_0$ and $H_1$ vanish by degree.

Conversely, suppose $L<4\delta$. Then


$$
0\le \eta-1\le2\delta-2.
$$


The $s\times s$ matrix $H_1$ is nonzero:

- if $\eta-1\le\delta-2$, an entry selects coefficient $0$, which is $1$;
- if $\eta-1=\delta-1$, an entry selects coefficient $1$, which is $-\delta\ne0\pmod3$;
- if $\eta-1\ge\delta$, an entry selects coefficient $\delta$, which is $1$.

There are regular full $H_1$ blocks because $g\ge243$. Equality $L=4\delta$ is impossible, since $L$ is odd.

Therefore


$$
\boxed{
\mathcal C_7=0
\iff L>4\delta
\iff D<H/2916.
}
\tag{7.1}
$$



This is an exact criterion, not merely a sufficient degree bound.

### 7.2 Explicit triangular radicals on $D<H/2187$

Suppose


$$
D<H/2187,
\quad\text{equivalently}\quad L>3\delta.
$$


Set


$$
u=\max(0,4s-1-\eta),\qquad
v=\max(0,4s-\eta).
\tag{7.2}
$$



Then:

- $H_0$ has an invertible trailing $u\times u$ anti-triangular block and all preceding rows and columns are zero;
- $H_1$ has the corresponding trailing $v\times v$ block;
- $J$ has an invertible trailing $u\times u$ block, with all other rows and columns zero.

The anti-diagonal coefficient is the leading coefficient of $(x-1)^{2s}$, namely $1$. These assertions therefore hold integrally for the indicated minors, not merely by an inferred determinant valuation.

Hence


$$
\boxed{
\rho_0=u,\qquad \rho_1=v,\qquad \rho_J=u,
}
\tag{7.3}
$$


and


$$
\boxed{
\operatorname{rank}\mathcal C_7
=(N_0+2)u+(N_1-2)v.
}
\tag{7.4}
$$



The kernels are coordinate spaces:



$$
\ker H_0=\langle e_0,\ldots,e_{s-u-1}\rangle,
$$




$$
\ker H_1=\langle e_0,\ldots,e_{s-v-1}\rangle,
$$




$$
\ker J^T=\langle e_0,\ldots,e_{s-u-1}\rangle,
$$




$$
\ker J=\langle e_0,\ldots,e_{s-u-2}\rangle.
\tag{7.5}
$$



Their images are the complementary trailing coordinate spaces. Formula (6.10) gives every endpoint projection coefficient explicitly.

In particular,


$$
\boxed{
D<H/2187
\quad\Longrightarrow\quad
\overline e\notin\operatorname{im}\mathcal C_7.
}
\tag{7.6}
$$



Thus a substantial part of the broader window has a completely evaluated radical and endpoint obstruction.

---

## 8. Lucas–Toeplitz evaluation on the remaining interval

On


$$
H/2187<D<H/972,
$$


the square binomial blocks can have additional characteristic-three radicals. They must not be declared nonsingular from a characteristic-zero Hankel transformation.

### 8.1 Standard determinant test, used only at its valid scope

For


$$
H^{(r)}_{ab}=[x^{r-a-b}](x-1)^{2s},
\qquad0\le a,b<s,
$$


put $q=r-s+1$. The classical binomial Toeplitz determinant gives, for $0\le q\le2s$,


$$
\det H^{(r)}
=
(-1)^{sr+s(s-1)/2}
\prod_{i=0}^{s-1}
\frac{(2s+i)!\,i!}{(q+i)!\,(2s-q+i)!}.
\tag{8.1}
$$


Outside this range the determinant is zero by triangular support.

This is a standard determinant identity of the type treated in *Advanced Determinant Calculus*. It is not claimed as new. In characteristic three it proves nonsingularity only when the valuation of the **whole integer product** is zero:


$$
\sum_{i=0}^{s-1}
\left(
v_3((2s+i)!)+v_3(i!)
-v_3((q+i)!)-v_3((2s-q+i)!)
\right)=0.
\tag{8.2}
$$


One must not reduce the separate factorial quotients when they have nonunit denominators.

The characteristic-zero orthogonal-polynomial transformations mentioned in the overlap gate do not by themselves determine these $\mathbb F_3$ radicals.

### 8.2 Exact kernel and endpoint construction when the determinant vanishes

All entries are obtained directly by Lucas:


$$
[x^k](x-1)^{2s}
=(-1)^k\prod_{\ell\ge0}
\binom{(2s)_\ell}{k_\ell}\pmod3,
\tag{8.3}
$$


with zero for out-of-range $k$. Reversing rows turns each of $H_0,H_1,J$ into a finite Toeplitz coefficient window.

For completeness, the following specifies actual bases rather than leaving “find the kernel” as an undefined operation.

For any one of these smaller matrices $M$, choose the lexicographically first maximal nonzero minor $M_{I,J_0}$, of order $r$. For each nonpivot column $b$, define


$$
k_b=e_b-
\sum_{a\in J_0}
\left(M_{I,J_0}^{-1}M_{I,b}\right)_a e_a.
\tag{8.4}
$$


The inverse here is an inverse of a certified unit minor; equivalently use its adjugate divided by its nonzero determinant in $\mathbb F_3$.

Then:

- the $k_b$ form a basis of $\ker M$;
- the columns $M[:,a]$, $a\in J_0$, form a basis of $\operatorname{im}M$;
- the endpoint projection on $k_b$ is
  

$$
\epsilon^Tk_b
  =
  (-1)^b-
  \epsilon_{J_0}^{\,T}M_{I,J_0}^{-1}M_{I,b}.
  \tag{8.5}
$$



Apply the same construction to $J^T$ for its left kernel. Representatives $0,1,-1$ give integral lifts of all these residue vectors.

Equations (6.1)–(6.11), (8.3)–(8.5) are a complete constructive characterization for every input in the original domain. They do not presume a uniform rank pattern. The only remaining arithmetic is on matrices of size at most


$$
s=\frac{\nu+1}{g},
$$


rather than the original size $\nu$.

### 8.3 A scalar endpoint compression when the endpoint is in the image

Suppose the three conditions (6.11) hold. Define the well-defined quotient contractions


$$
\kappa_0=\epsilon_s^Tx_0,\qquad H_0x_0=\epsilon_s,
$$




$$
\kappa_1=\epsilon_s^Tx_1,\qquad H_1x_1=\epsilon_s,
$$




$$
\kappa_J=\epsilon_{s-1}^Tb,\qquad Jb=\epsilon_s.
$$


They are independent of the chosen solutions precisely because the endpoint annihilates the relevant kernels.

The contraction of the endpoint with the induced nondegenerate quotient form is then


$$
\boxed{
(-1)^{a_0}
\left(
N_0\kappa_0-(N_1-2)\kappa_1-2\kappa_J
\right)
\quad\text{in }\mathbb F_3.
}
\tag{8.6}
$$



This is a quotient-form calculation. Since $\mathcal C_7$ is singular, it is **not** an actual inverse contraction of the full residual matrix and does not establish a primitive-denominator depth.

---

## 9. The actual force in the same residue coordinates

The decomposition above must not be mistaken for a decomposition of the actual sum unless the actual force is included.

The retained endpoint law implies


$$
R(-1)\equiv0\pmod3.
$$


Indeed, $Q_c(-1)=0$, and


$$
v_3(Q_n^{\rm loc}(-1))=2v_3((n-1)!)
$$


is far above $6$ on the original domain.

Thus, over $\mathbb F_3$, write


$$
\overline R(y)=(y+1)S(y),
\qquad
S(y)=\sum_{c=0}^{g-1}y^cS_c(y^g).
\tag{9.1}
$$


Then


$$
W_R(y)
=
\frac{R(y)(y-1)^{2D}-R(-1)(-2)^{2D}}{y+1}
\equiv
\sum_{c=0}^{g-1}y^cS_c(y^g)(y^g-1)^{4s}.
\tag{9.2}
$$



Let


$$
\zeta=\frac{H/g-1}{2},
\qquad r_1=g\zeta+a_0.
$$


For a pair of residue classes $r,r'$, choose the unique $c\in[0,g-1]$ with


$$
c\equiv a_0-r-r'\pmod g,
$$


and put


$$
b_{r,r'}=\frac{a_0-r-r'-c}{g}.
$$


The actual force block is exactly


$$
\boxed{
(\mathcal F_R)_{(r,a),(r',b)}
=
[x^{\zeta+b_{r,r'}-a-b}]
S_c(x)(x-1)^{4s}.
}
\tag{9.3}
$$



This formula preserves the true class sizes $n_r,n_{r'}$ and the actual producer coefficient strip. It also shows the obstruction clearly:

> Unless the relevant $S_c$ strips vanish, the actual force couples residue classes that the core does not couple.

Therefore the core’s forced radical need not survive in $\mathcal C_7+\mathcal F_R$. Conversely, it is not legitimate to fill that radical with an arbitrary model force.

If the missing stronger producer congruence is proved, all $S_c$ vanish, and Sections 6–8 become the actual depth-seven radical and endpoint analysis on $v_3(j)\ge5$.

---

## 10. Compression to the smaller **actual** operator

There is a rigorous way to proceed on any singular actual branch, without assuming that residue symmetries persist at the next digit.

Let


$$
T=\mathscr R_{\rm act}/3^7,\qquad
\overline T=\mathcal C_7+\mathcal F_R.
$$


Let $K$ be a basis matrix for $\ker\overline T$, and choose a complementary basis matrix $N$. Lift them integrally so that


$$
P=[N\ K]\in\operatorname{GL}_\nu(\mathbb Z_3).
$$


Write


$$
P^TTP=
\begin{pmatrix}
A_0&B_0\\
B_0^T&C_0
\end{pmatrix}.
$$


Then


$$
A_0\in\operatorname{GL}(\mathbb Z_3),\qquad
B_0,C_0\in3M(\mathbb Z_3).
$$


The next actual operator is


$$
\boxed{
T_{\rm next}
=
\frac{C_0-B_0^TA_0^{-1}B_0}{3}.
}
\tag{10.1}
$$



Its size is exactly $\dim\ker\overline T$. This is a genuine Schur compression of the actual residual, not a quotient by a symmetry that may fail at higher precision.

For the actual transported endpoint $e_{\rm res}$, the corresponding endpoint is


$$
\boxed{
e_{\rm next}
=
K^Te_{\rm res}-B_0^TA_0^{-1}N^Te_{\rm res},
\qquad
e_{\rm next}\bmod3=K^T\overline e.
}
\tag{10.2}
$$



Thus the endpoint projection computed in Sections 6–8 is exactly the datum needed by the next actual saturation step when $\mathcal F_R=0$.

If $T_{\rm next}\bmod3$ is invertible and its endpoint contraction is nonzero, then—and only under those additional conditions—the full endpoint inverse contraction has depth $-8$. No such condition is established merely from singularity of $\mathcal C_7$.

---

## 11. If the whole depth-seven digit vanishes: the complete next force

If


$$
\mathcal C_7+\mathcal F_R=0,
$$


there is no dimension reduction at depth seven. One must compute the next **whole** digit.

Set


$$
J_B=B/729,
$$


and


$$
\mathcal K_{\rm LOW}
=
J_B^TL^{-1}X\widehat E^{-1}V^T
+
V\widehat E^{-1}X^TL^{-1}J_B.
\tag{11.1}
$$


Let $\widehat Z^{\,c}$ be the exact core-corrected columns, and define


$$
(\Phi_R)_{ij}
=
\mathcal M(R\widehat z_i^{\,c}\widehat z_j^{\,c}).
\tag{11.2}
$$



The loss-one Schur perturbation lemma and the exact expansion of $\widetilde V$ give


$$
\boxed{
\mathscr R_{\rm act}
\equiv
G_c(Z,Z)
-9V\widehat E^{-1}V^T
+3^8\mathcal K_{\rm LOW}
+3^6\Phi_R
\pmod{3^9}.
}
\tag{11.3}
$$


The omitted LOW quadratic term has depth at least $13$; the quadratic polynomial perturbation has depth at least $11$.

Consequently, when the depth-seven digit is zero,


$$
\boxed{
\frac{\mathscr R_{\rm act}}{3^8}
\equiv
\frac{
G_c(Z,Z)-9V\widehat E^{-1}V^T
+3^8\mathcal K_{\rm LOW}+3^6\Phi_R
}{3^8}
\pmod3.
}
\tag{11.4}
$$



The division in (11.4) is taken **after summing the whole numerator**. Separate depth-seven carries must not be discarded.

### 11.1 Every force pole needed modulo $27$

To evaluate $\Phi_R\bmod27$, the complete functional reduces to


$$
\begin{aligned}
\mathcal M(F)\equiv{}&
[y^{r_*}]C_F
+3[y^{r_1}]C_F\\
&+9\sum_{c\in\{1,5,7,11\}}
c^{-1}[y^{(cH/3-1)/2}]C_F
\pmod{27},
\end{aligned}
\tag{11.5}
$$


where $C_F=(F-F(-1))/(y+1)$.

All four units in the last sum are within the original cutoff on $D<H/972$. The factorial term vanishes at this precision by its known depth. The corrected columns are needed modulo $27$; they cannot be replaced everywhere by $Z$.

### 11.2 Conditional simplification if the producer congruence is proved

If the missing congruence gives $R=3S$, and $D<H/2916$, then $\mathcal C_7=0$ and the first possible actual force is


$$
(\mathcal F_S)_{ij}
=
[y^{r_1-i-j}]
\frac{S(y)(y-1)^{2D}-S(-1)(-2)^{2D}}{y+1}.
$$


Equation (11.4) simplifies to


$$
\boxed{
\frac{\mathscr R_{\rm act}}{3^8}
\equiv
\frac{G_c(Z,Z)}{3^8}
-\frac{V\widehat E^{-1}V^T}{729}
+\mathcal K_{\rm LOW}
+\mathcal F_S
\pmod3.
}
\tag{11.6}
$$



This is the first still-unevaluated complete digit. It is **not proved nonzero**. A fixed digit can remain degenerate, and no fixed-depth theorem supplies the first nonzero depth uniformly.

---

## 12. Primitive normalization, full gcd, and whole evaluated error

The primitive unit must still be restored:


$$
Q_n=\lambda Q_n^{\rm loc},\qquad \lambda\in\mathbb Z_3^\times.
$$


For the complete rational matrix,


$$
R_{\rm rat}=\frac{4\lambda}{3^h}G_{\rm act},
$$


and


$$
H_{\rm complete}
=
R_{\rm rat}+(e+\pi)Q_n(-1)vv^T.
$$



Without assuming nonsingularity,


$$
\beta_0=\det R_{\rm rat},\qquad
\beta_1=Q_n(-1)v^T\operatorname{adj}(R_{\rm rat})v.
$$


When $G_{\rm act}$ is nonsingular,


$$
\frac{\beta_1}{\beta_0}
=
\frac{3^hQ_n^{\rm loc}(-1)}4
v^TG_{\rm act}^{-1}v.
\tag{12.1}
$$



The singularity of $\mathcal C_7$ means that the previously proposed invertible depth-seven sufficient branch is unavailable when $\mathcal F_R=0$. It gives no replacement exact denominator law by itself.

For a clearing integer $\ell$, retain


$$
A_\ell=\ell^k\beta_0,\qquad
B_\ell=\ell^k\beta_1,\qquad
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


When $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole evaluated error is exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
\det H_{\rm complete}.
}
\tag{12.2}
$$



None of the residue-radical results determines the all-prime gcd, proves $B_\ell\ne0$, or proves nonvanishing and decay of (12.2).

---

## 13. Bounded exact arithmetic for personal inspection

No computation is needed for the symbolic residue decomposition or the triangular-region theorem. The following small checks would provide useful implementation certificates.

These are **auxiliary algebraic inputs**, not asserted original indices.

### Inputs

Take $g=9$, and the following triples $(L,\delta,s)$:



$$
(9,2,1),\qquad (9,4,2),\qquad (27,8,4).
$$



For each, set


$$
D=g\delta,\qquad
\nu=gs-1,\qquad
\varrho=(gL-1)/2.
$$


Construct


$$
(\mathcal C)_{ij}
=[y^{\varrho-i-j}](y-1)^D\pmod3
$$


on the exact range $0\le i,j<\nu$.

Independently construct the residue blocks (6.3)–(6.6), including the shortened class $r=g-1$.

### Expected verifiable output

| $(g,L,\delta)$ | $\nu$ | $\operatorname{rank}\mathcal C$ | Endpoint |
|---|---:|---:|---|
| $(9,9,2)$ | $8$ | $0$ | outside image |
| $(9,9,4)$ | $17$ | $16$ | outside image |
| $(9,27,8)$ | $35$ | $20$ | outside image |

For the middle case,


$$
\ker\mathcal C=\langle e_{14}\rangle,
$$


and its endpoint pairing is $1$.

For the last case,


$$
\rho_0=2,\qquad \rho_1=3,\qquad \rho_J=2,
$$


so


$$
\dim\ker\mathcal C=15.
$$



The certificate should additionally return:

1. equality of the permuted full matrix and the residue-block assembly;
2. bases for the radical and image;
3. the endpoint projections from (6.10);
4. agreement with the Lucas-entry construction;
5. agreement of unit determinant tests with (8.1)–(8.2).

A separate finite check of (9.3) can use sparse auxiliary polynomials


$$
R=(y+1)y^u
$$


and compare the original quotient extraction with its residue-block expression. Such a check validates the force assembly, **not** the actual producer congruence.

No bounded list of these auxiliary tests proves (4.4) on the infinite original family. That issue requires a producer-level proof.

---

## 14. Closing ledger

### New results and proof status

**Proved from the retained block and order-six interfaces:**

- the broader $H/972$ finite-boundary estimate
  

$$
V\widehat E^{-1}V^T\in729M;
$$


- the actual depth-seven characterization
  

$$
\mathscr R_{\rm act}/3^7\equiv\mathcal C_7+\mathcal F_R;
$$


- the exact residue-class decomposition of $\mathcal C_7$ at
  

$$
\nu=D/2-1;
$$


- unavoidable singularity of $\mathcal C_7$;
- its radical, image, and endpoint projection in terms of two smaller binomial blocks and the true rectangular endpoint block;
- the exact whole-core degeneration criterion
  

$$
\mathcal C_7=0\iff D<H/2916;
$$


- explicit triangular ranks and endpoint exclusion on $D<H/2187$;
- the actual force residue-block formula;
- the actual radical Schur compression and the complete next-digit formula.

**Not proved:**

- the producer congruence $3P_n-Q_c\in3^7\mathbb Z_3[y]$ on $v_3(j)\ge5$;
- consequently, unconditional vanishing of $\mathcal F_R$ on that subfamily;
- a first nonzero actual residual depth or an actual primitive-denominator depth;
- nonzero whole primitive errors tending to zero.

### Exact remaining mathematical bottleneck

The immediate missing lemma is now precise:

> **Actual producer-strip lemma.**  
> Starting from the derangement system (4.1), prove either the coefficientwise bound (4.4), or directly the smaller strip vanishing (4.5), for $v_3(j)\ge5$.

After that lemma, the endpoint problem is not an invertible $C_7$ problem: $C_7$ is always singular. The next obligation is the actual radical operator (10.1), or, on the wholly degenerate branch, the complete digit (11.6), together with its transported endpoint.

The global objective still requires the same original indices to yield the final primitive pair with


$$
0<|q(e+\pi)-p|\longrightarrow0.
$$





$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$


