> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1 turn12 — A rank-four coefficient connection, a two-coordinate recurrence, and explicit endpoint observability

## Executive conclusion

The proposed reciprocal identities are correct on the distinguished branch. They reduce the relevant differential space from the degree-eight parameter field to its four-dimensional anti-invariant part.

The advance is not merely a prescription for symbolic elimination. Below I derive:

1. an explicit polynomial differential system with four coordinates and seed $(1,1,1,1)$;
2. a complete two-coordinate coefficient recurrence, including its initial boundary and its singular reverse step;
3. a certificate that the genuine differential rank of the joint outputs—and already of the first output—is **exactly four**;
4. an explicit same-index endpoint observation matrix and its inverse-lattice bound;
5. a complete cumulative $3$-adic content bound for this particular recurrence.

The observation bound is especially concrete on the retained original branch. If $V_{m-1}$ denotes the two-coordinate recurrence state defined below, then


$$
\boxed{
c(V_{m-1})-6\le c_m\le c(V_{m-1})-4.
}
$$


Thus endpoint projection loses between four and six digits of common content there. It cannot hide an arbitrarily large additional common endpoint factor.

The cumulative transition estimate proved here is **linear**, not logarithmic:


$$
\boxed{
c(V_N)\le N-2+v_3((2N+1)!)-v_3(N)\qquad(N\ge1).
}
$$


In particular, on the original branch,


$$
\boxed{
c_m\le m-7+v_3((2m-1)!).
}
$$


This improves the earlier $c_m<4m$ bound, but does not supply the sought small normalization budget. The remaining coefficient-connection bottleneck is now transition cancellation along the actual seeded solution, rather than an uncontrolled endpoint projection.

No original tuple is evaluated, and no accepted bounded computation is proposed for repetition.

---

## 1. Scope, retained endpoint formulas, and notation

The original domain remains


$$
j>0,\qquad j\equiv81\pmod{243},\qquad
m=2^{2j-1},\qquad A=2m-1,
$$


with the retained real window


$$
H_{\mathrm{win}}=3^{h-1},\qquad D=H_{\mathrm{win}}-A,
$$




$$
\frac1{2C_{16}}<\frac{D}{H_{\mathrm{win}}}<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$


Statements invoking the normalized scalar comparison retain all its additional hypotheses, including


$$
m\equiv851\pmod{6561},\qquad
r=\operatorname{cont}_3(J_m)=\operatorname{cont}_3(J_{m-1}),
$$




$$
s=h-2-2r,\qquad \mathfrak a\equiv25\pmod{27},
\qquad N_m\in\mathbb Z_3^\times.
$$



Write


$$
a_m=J_m(-1),\qquad b_m=J_{m-1}(-1),
$$


where the adjacent polynomial has the same parameter $A=2m-1$ as the degree-$m$ polynomial. For generating functions only, put $a_0=1,b_0=0$.

I retain the exact turn11 endpoint formulas:


$$
\mathcal A(x)=\sum_{m\ge0}a_mx^m
=\frac{(1+Z)^3(1-Z)}{R(Z)},
$$




$$
\mathcal B(x)=\sum_{m\ge0}b_mx^m
=\frac{2Z(1+Z)^5}{(1+Z^2)(1-Z)R(Z)},
$$


where


$$
R(z)=1+8z-10z^2+8z^3+z^4,
$$




$$
2Z(1+Z)^6=x(1+Z^2)^3(1-Z)^2,
\qquad Z=\frac x2+O(x^2).
$$



These are identities for the actual varying-$m$ adjacent pairs. No fixed-$A$ Jacobi recurrence is being applied across $m$.

The turn11 negative result also remains in force at precisely its stated scope: unrestricted characteristic-zero exact linear ternary section rank is infinite. None of the finite differential or coefficient-state ranks below contradicts that result.

---

## 2. Audit of the reciprocal symmetry

Set


$$
w=z+z^{-1},\qquad v=z^{-1}-z.
$$


Then


$$
v^2=w^2-4,
$$


and direct substitution gives


$$
\boxed{
x=\frac{2(w+2)^3}{w^3(w-2)},\qquad
\frac{R(z)}{z^2}=w^2+8w-12,
}
$$




$$
\boxed{
\mathcal A=\frac{v(w+2)}{w^2+8w-12},\qquad
\frac{\mathcal B}{\mathcal A}
=\frac{2(w+2)}{w(w-2)}.
}
$$



For example,


$$
\frac{(1+z)^3(1-z)}{z^2}
=(z^{-1}-z)(z+z^{-1}+2),
$$


which verifies the sign in the first output.

On the distinguished branch,


$$
z=\frac x2+O(x^2),\qquad
w\sim\frac2x,\qquad v\sim\frac2x.
$$


Thus the displayed formula gives $\mathcal A(0)=1$, not $-1$.

### A convenient quartic coordinate

Introduce


$$
t=1+\frac2w,\qquad \sigma=\frac vw.
$$


The distinguished branch satisfies


$$
t(0)=1,\qquad \sigma(0)=1,
$$


and


$$
\boxed{
\sigma^2=t(2-t),\qquad
x=\frac{t^3(t-1)}{2-t}.
}
$$


Consequently


$$
\boxed{
P(x,t):=t^4-t^3+xt-2x=0.
}
\tag{2.1}
$$



Put


$$
d(t)=-3t^2+10t-6.
$$


The outputs become


$$
\boxed{
\mathcal A=\frac{\sigma t}{d(t)},\qquad
\frac{\mathcal B}{\mathcal A}
=\frac{t(t-1)}{2-t}.
}
\tag{2.2}
$$


Also,


$$
\frac{dx}{dt}=\frac{t^2d(t)}{(2-t)^2},
\qquad
P_t=4t^3-3t^2+x=\frac{t^2d(t)}{2-t}.
\tag{2.3}
$$



The rational map $t\mapsto x$ has degree four. Moreover, $t(2-t)$ is not a square in $\mathbb Q(t)$. Therefore


$$
[\mathbb Q(t,\sigma):\mathbb Q(x)]=8,
$$


and the anti-invariant part under $\sigma\mapsto-\sigma$ is


$$
\sigma\,\mathbb Q(t),
$$


of dimension four over $\mathbb Q(x)$. Differentiation preserves this part.

---

## 3. An explicit polynomial differential system

Define the four generating functions


$$
\begin{pmatrix}U\\V\\W\\S\end{pmatrix}
=
\frac{\sigma}{P_t}
\begin{pmatrix}1\\t\\t^2\\t^3\end{pmatrix}.
\tag{3.1}
$$


Here $S$ is a generating-function coordinate, not the scalar exponent $s$ in the normalization hypotheses.

Their seed is


$$
\boxed{(U,V,W,S)(0)=(1,1,1,1).}
\tag{3.2}
$$



### Theorem 3.1 — Concrete polynomial connection

Let


$$
L(x)=L_0+xL_1
=
\begin{pmatrix}
x&0&-3&4\\
8x&-3x&0&1\\
2x&7x&-3x&1\\
2x&x&7x&1-3x
\end{pmatrix},
$$


and


$$
K(x)=
\begin{pmatrix}
-3x&0&-1&1\\
-10x&2x&0&0\\
-4x&-4x&0&0\\
-4x&-2x&0&-2x
\end{pmatrix}.
$$


Then


$$
\boxed{
2xL(x)
\begin{pmatrix}U\\V\\W\\S\end{pmatrix}'
=
K(x)
\begin{pmatrix}U\\V\\W\\S\end{pmatrix}.
}
\tag{3.3}
$$



Its determinant factor is


$$
\boxed{
\det L(x)=-x^2\bigl(27x^2+1264x+108\bigr).
}
\tag{3.4}
$$


Thus an explicitly displayed rational form of the connection is


$$
\begin{pmatrix}U\\V\\W\\S\end{pmatrix}'
=
-\frac{\operatorname{adj}L(x)\,K(x)}
{2x^3(27x^2+1264x+108)}
\begin{pmatrix}U\\V\\W\\S\end{pmatrix}.
\tag{3.5}
$$


This displays all denominator factors of this representation; it is not an assertion that every entry has that denominator after cancellation.

#### Derivation

Let


$$
Y=(\sigma,\sigma t,\sigma t^2,\sigma t^3)^T.
$$


Multiplication by $t$ on these evaluations is represented by


$$
C=
\begin{pmatrix}
0&1&0&0\\
0&0&1&0\\
0&0&0&1\\
2x&-x&0&1
\end{pmatrix},
$$


using $t^4=t^3-xt+2x$. Hence multiplication by $P_t$ is represented by


$$
4C^3-3C^2+xI=L.
$$



Implicit differentiation and $\sigma^2=t(2-t)$ give


$$
t'=\frac{2-t}{P_t},
$$




$$
\frac{d}{dx}(\sigma t^k)
=
\frac{\sigma}{P_t}
\left((2k+1)t^{k-1}-(k+1)t^k\right).
$$


For $k=0$, use


$$
t^{-1}=\frac{t^3-t^2+x}{2x}.
$$


It follows that


$$
Y'=N
\begin{pmatrix}U\\V\\W\\S\end{pmatrix},
\qquad
N=
\begin{pmatrix}
-\tfrac12&0&-\tfrac1{2x}&\tfrac1{2x}\\
3&-2&0&0\\
0&5&-3&0\\
0&0&7&-4
\end{pmatrix}.
$$


Since $Y=L(U,V,W,S)^T$,


$$
2xL(U,V,W,S)'=(2xN-2xL')(U,V,W,S)^T.
$$


The right-hand matrix is exactly $K$.

Finally, direct expansion of $\det L$, equivalently the discriminant of
$t^4-t^3+xt-2x$, gives (3.4). ∎

### Exact output rows

The quartic relation gives the useful reduction


$$
\frac{t^3}{2-t}=t^3+x.
$$


Using (2.2)–(2.3),


$$
\boxed{\mathcal A=S+xU,}
\tag{3.6}
$$




$$
\boxed{
\mathcal B=\frac x4\bigl(S+W+2V+xU\bigr).
}
\tag{3.7}
$$



These are the actual two endpoint outputs, not surrogate observables.

---

## 4. A complete two-coordinate coefficient recurrence

Write


$$
U=\sum_{n\ge0}u_nx^n,\quad
V=\sum_{n\ge0}v_nx^n,\quad
W=\sum_{n\ge0}w_nx^n,\quad
S=\sum_{n\ge0}s_nx^n.
$$


The lower-case $s_n$ here denotes a coefficient of $S$.

Coefficient extraction from (3.3) gives, for $n\ge0$,


$$
\boxed{
(1-6n)w_n+(8n-1)s_n=-(2n+1)u_{n-1},
}
\tag{4.1}
$$


with $u_{-1}=0$, and


$$
\boxed{
2(n+1)s_{n+1}=-(16n+10)u_n+(6n+2)v_n.
}
\tag{4.2}
$$


Subtracting the other two coefficient equations gives


$$
\boxed{
(6n+3)u_n=(10n+3)v_n-3nw_n,
}
\tag{4.3}
$$




$$
\boxed{
(6n+1)v_n=10nw_n-(3n-1)s_n.
}
\tag{4.4}
$$



These equations include the low-index boundary. In particular, at $n=0$,


$$
w_0=s_0,\qquad v_0=s_0,\qquad u_0=v_0,
$$


and the seed fixes all four to $1$.

Define


$$
D_n=(6n+1)(6n+3),
$$




$$
\mathsf U_n(w,s)
=
\frac{n(82n+27)w-(10n+3)(3n-1)s}{D_n}.
\tag{4.5}
$$


Then $u_n=\mathsf U_n(w_n,s_n)$, while $v_n$ is given by (4.4).

### Theorem 4.1 — Forward recurrence with all factors exposed

Let


$$
V_n=\binom{w_n}{s_n},\qquad V_0=\binom11.
$$


For every $n\ge0$, set


$$
\boxed{
s_{n+1}
=
\frac{
-7n(68n^2+68n+15)w_n
+(3n-1)(62n^2+59n+12)s_n
}{
(n+1)(6n+1)(6n+3)
},
}
\tag{4.6}
$$


and


$$
\boxed{
w_{n+1}
=
\frac{(8n+7)s_{n+1}+(2n+3)\mathsf U_n(w_n,s_n)}
{6n+5}.
}
\tag{4.7}
$$



This recurrence uniquely produces the coefficients of (3.1).

A common leading coefficient for the polynomial vector recurrence is


$$
\boxed{
\Lambda(n)=(n+1)(6n+1)(6n+3)(6n+5).
}
\tag{4.8}
$$


Its only integer zero is $n=-1$; in particular, there is **no exceptional nonnegative forward step**.

The transition matrix $T(n)$, defined by (4.6)–(4.7), has determinant


$$
\boxed{
\det T(n)=
\frac{
n(3n-1)(3n+1)(2n+3)
}{
(n+1)(6n+1)(2n+1)(6n+5)
}.
}
\tag{4.9}
$$


Its only nonnegative integer singular step is $n=0$.

That step is explicitly continued by the seed:


$$
\boxed{
V_1=\binom{-5}{-4},\qquad
(u_1,v_1,w_1,s_1)=(-7,-6,-5,-4).
}
\tag{4.10}
$$


No inverse transition at $n=0$ is used.

#### Proof and completeness

Equations (4.3)–(4.4) yield (4.5). Substitution into (4.2) gives (4.6), and (4.1) at index $n+1$ gives (4.7).

Conversely, (4.6)–(4.7), together with (4.3)–(4.4), recover every coefficient equation of (3.3). The initial equation (4.1) is satisfied at $n=0$. All forward denominators are nonzero for $n\ge0$, proving uniqueness.

For the determinant, write


$$
s_{n+1}=p_nw_n+q_ns_n,\qquad
u_n=\alpha_nw_n+\beta_ns_n.
$$


Then


$$
\det T(n)=\frac{2n+3}{6n+5}
(\alpha_nq_n-\beta_np_n).
$$


The numerator reduction uses the exact factorization


$$
\begin{aligned}
&(82n+27)(62n^2+59n+12)\\
&\quad-7(10n+3)(68n^2+68n+15)\\
&=9(3n+1)(6n+1)(2n+1),
\end{aligned}
$$


which proves (4.9). ∎

### Endpoint extraction and the low-index terms

From (3.6)–(3.7),


$$
\boxed{
a_m=s_m+u_{m-1},
}
\tag{4.11}
$$




$$
\boxed{
b_m=\frac14(s_{m-1}+w_{m-1}+2v_{m-1}+u_{m-2}),
}
\tag{4.12}
$$


where coefficients with negative index are zero.

Thus


$$
(a_0,b_0)=(1,0),\qquad
(a_1,b_1)=(-3,1),
$$


and the next step gives the retained check


$$
(a_2,b_2)=\left(\frac{53}{2},-5\right).
$$



The two-coordinate coefficient recurrence is not a differential-rank-two realization. Its rational dependence on the coefficient index and its coefficient shifts encode a differential system of larger rank.

---

## 5. The genuine differential rank is exactly four

The anti-invariant field description proves an upper bound of four. A lower-bound certificate can be obtained locally, without an unevaluated determinant of four derivatives.

### Theorem 5.1 — Minimal differential rank

The smallest differential subspace over $\mathbb Q(x)$ containing $\mathcal A$ has dimension four. Consequently the minimal joint differential rank of $(\mathcal A,\mathcal B)$ is also four.

#### Proof

Near $x=0$, one branch has $t=1+O(x)$. On the chosen sign of $\sigma$, its first output has


$$
\mathcal A=1+O(x).
$$



The other three $t$-branches approach $t=0$. Put


$$
q=(-2x)^{1/3}.
$$


The local parametrization gives


$$
q=t\left(\frac{1-t}{1-t/2}\right)^{1/3}
=t-\frac{t^2}{6}+O(t^3),
$$


so


$$
t=q+\frac{q^2}{6}+O(q^3).
$$



For a nonzero constant $C$, depending only on choices of roots,


$$
\frac{\mathcal A}{\sqrt{x}}
=
C\,
\frac{1-t/2}
{\sqrt{1-t}\,(1-\frac53t+\frac12t^2)}.
$$


Expanding,


$$
\frac{\mathcal A}{\sqrt{x}}
=
C\left(
1+\frac53t+\frac{173}{72}t^2+O(t^3)
\right)
$$


and hence


$$
\boxed{
\mathcal A
=
C\sqrt{x}\left(
1+\frac53q+\frac{193}{72}q^2+O(q^3)
\right).
}
\tag{5.1}
$$


All three displayed coefficients are nonzero.

Choose the three local branches obtained by $q\mapsto\omega^kq$, $k=0,1,2$, with consistent square-root signs. If a constant linear combination of these branches vanishes, comparison of the powers


$$
x^{1/2},\qquad x^{5/6},\qquad x^{7/6}
$$


gives a nonsingular three-by-three Fourier system. Therefore the three branches are linearly independent over $\mathbb C$. The branch with nonzero constant term is independent of them.

These four functions are analytic continuations of the algebraic first output: the degree-eight covering is connected, and away from its branch values its sheets are connected by continuation. Any homogeneous rational-coefficient differential equation annihilating $\mathcal A$ therefore annihilates all four branches. An equation of order less than four cannot have four independent local solutions.

The upper bound is four because all derivatives remain in the four-dimensional anti-invariant subspace. Thus the rank is exactly four. ∎

This is a differential-rank certificate, not a digit-rank certificate. The unrestricted exact ternary digit rank remains infinite.

---

## 6. Same-index endpoint observability

The recurrence now permits an explicit answer to the projection issue.

Use $n=m-1$. Eliminating the previous coefficient $u_{n-1}$ by (4.1), including its valid $n=0$ boundary, gives


$$
\boxed{
\binom{a_{n+1}}{b_{n+1}}=O(n)V_n,
}
\tag{6.1}
$$


where


$$
O(n)=
\begin{pmatrix}
\displaystyle
-\frac{n(394n^2+367n+78)}{(n+1)D_n}
&
\displaystyle
\frac{(3n-1)(52n^2+46n+9)}{(n+1)D_n}
\\[8pt]
\displaystyle
\frac{n(22n+7)}{(2n+1)(6n+1)}
&
\displaystyle
-\frac{(3n-1)(4n+1)}{(2n+1)(6n+1)}
\end{pmatrix}.
\tag{6.2}
$$



Its determinant is


$$
\boxed{
\det O(n)=
\frac{
n(3n-1)(3n+1)(8n+5)
}{
(n+1)(2n+1)^2(6n+1)
}.
}
\tag{6.3}
$$


It is invertible for every integer $n\ge1$. The exceptional observation at $n=0$ is handled by the actual seed and gives $(-3,1)$.

For verification, the nontrivial numerator factorization is


$$
\begin{aligned}
&(394n^2+367n+78)(4n+1)\\
&\quad-(52n^2+46n+9)(22n+7)\\
&=3(6n+1)(3n+1)(8n+5).
\end{aligned}
\tag{6.4}
$$



### Theorem 6.1 — Explicit inverse-lattice observation bound

For a vector over $\mathbb Q_3$, let $c(\cdot)$ be the minimum coordinate valuation. For every integer $n\ge1$, put


$$
d_n=1+v_3(n+1)+v_3(2n+1).
$$


Then, for every $V\in\mathbb Q_3^2$,


$$
\boxed{
c(O(n)V)\ge c(V)-d_n,
}
\tag{6.5}
$$


and


$$
\boxed{
c(O(n)V)
\le c(V)+1+v_3(n)+v_3(8n+5)-v_3(2n+1).
}
\tag{6.6}
$$



In particular these inequalities apply to the actual seeded state $V_n$.

#### Proof

Every entry of $O(n)$ has valuation at least $-d_n$. This proves (6.5).

Also, because $3n\pm1$ and $6n+1$ are units,


$$
v_3(\det O(n))
=
v_3(n)+v_3(8n+5)-v_3(n+1)-2v_3(2n+1).
$$


The entries of the adjugate have valuation at least $-d_n$. Therefore


$$
c(O(n)^{-1}Y)\ge c(Y)-d_n-v_3(\det O(n)).
$$


Apply this to $Y=O(n)V$ and rearrange. This gives (6.6). ∎

This proof uses the entries of the inverse, not merely the determinant. Equivalently, it proves explicit lattice inclusions in both directions.

### Corollary 6.2 — Original-branch observation costs only four to six digits

On the retained original branch, take $n=m-1$. Then


$$
v_3(n)=v_3(n+1)=v_3(8n+5)=0,
\qquad v_3(2n+1)=v_3(A)=5.
$$


Consequently


$$
\boxed{
c(V_{m-1})-6\le c_m\le c(V_{m-1})-4.
}
\tag{6.7}
$$



In fact $O(m-1)$ has local Smith exponents $-6,-4$: its smallest entry valuation is $-6$, while its determinant valuation is $-10$.

Thus the primitive recurrence state and the primitive endpoint pair are linked by a uniformly controlled observation map on the original family. An arbitrarily large projection loss is excluded here.

---

## 7. Integral coefficients and a full cumulative transition bound

The formal equation $P(x,t)=0$, at $t=1,x=0$, has


$$
P_t(0,1)=1.
$$


Hence


$$
t\in\mathbb Z[[x]].
$$


The square root with constant term $1$ satisfies


$$
\sigma\in\mathbb Z[1/2][[x]],
$$


and $P_t(x,t(x))$ is an integral unit series. Therefore


$$
\boxed{
U,V,W,S\in\mathbb Z_3[[x]],\qquad V_n\in\mathbb Z_3^2.
}
\tag{7.1}
$$



This is an actual-solution integrality statement. It does not say that every transition $T(n)$ preserves the full lattice $\mathbb Z_3^2$.

### Theorem 7.1 — Complete cumulative content bound

For every $N\ge1$,


$$
\boxed{
0\le c(V_N)\le
N-2+v_3((2N+1)!)-v_3(N).
}
\tag{7.2}
$$



#### Proof

For $n\ge1$, the displayed transition formulas imply


$$
\min_{i,j}v_3(T(n)_{ij})
\ge -1-v_3(n+1)-v_3(2n+1),
$$


since $6n+1$ and $6n+5$ are units.

From (4.9),


$$
v_3(\det T(n))
=
v_3(n)+v_3(2n+3)-v_3(n+1)-v_3(2n+1).
$$


The adjugate estimate therefore gives


$$
\boxed{
c(V_{n+1})\le
c(V_n)+1+v_3(n)+v_3(2n+3).
}
\tag{7.3}
$$



The seed $V_1=(-5,-4)^T$ has content zero. Summing every step, without dropping the cumulative valuation terms,


$$
c(V_N)
\le
N-1+v_3((N-1)!)
+\sum_{n=1}^{N-1}v_3(2n+3).
$$


The odd product in the last sum is


$$
5\cdot7\cdots(2N+1).
$$


Thus


$$
\sum_{n=1}^{N-1}v_3(2n+3)
=
v_3((2N+1)!)-v_3(N!)-1.
$$


Substitution proves (7.2), including $N=1$. ∎

### Original endpoint consequence

Combine (7.2), with $N=m-1$, and (6.7). Since $m-1$ is a $3$-adic unit on the original branch,


$$
\boxed{
c_m\le m-7+v_3((2m-1)!).
}
\tag{7.4}
$$



This is a rigorous improvement over the previous $4m$ termination budget. It is still of linear size: Legendre’s formula gives


$$
v_3((2m-1)!)=\frac{2m-1-s_3(2m-1)}2.
$$


Nothing in the proof turns the cumulative transition loss into $O(\log m)$.

### What has and has not been resolved

The recurrence now separates two issues:

- **Endpoint observability:** explicitly controlled, with a constant four-to-six-digit relation on the original branch.
- **Actual-state transition content:** still not sharply controlled.

The second is the remaining normalization obstruction. Rational invertibility and a fixed recurrence order do not prevent repeated accumulation of content in the actual solution.

---

## 8. A concrete follow-on lemma

The next target can now be stated for a fully specified recurrence, rather than an unspecified companion system.

> **Seeded transition-content lemma.**  
> For the rational matrices $T(n)$ in (4.6)–(4.7), with
> 

$$
> V_1=(-5,-4)^T,
>
$$


> prove a substantially sublinear bound for
> 

$$
> c\!\left(T(N-1)\cdots T(1)V_1\right)
>
$$


> on $N=m-1$ from the retained original family, or construct a normalized transition scheme with a proved cumulative content budget on that family.

The local estimates show exactly what a crude argument pays:


$$
1+v_3(n)+v_3(2n+3)
$$


at each step. A logarithmic theorem must establish cancellation or compensation across the product, not simply note that the exceptional factors are linear in $n$.

Even such a content theorem would not decide the projective endpoint direction. After normalization, (6.2) gives its exact connection to the state, but one must still prove the required avoidance or approach bound for the actual seeded solution. The already closed split-form classification is not revisited here.

A nonlinear normalization or a construction on the original-power language remains possible. Neither is excluded by the infinite unrestricted characteristic-zero digit-rank theorem.

---

## 9. Narrow, new exact-arithmetic checks

The derivations above are proofs, not reports of executed computer algebra. A coordinator can independently check their algebra with small fixed-degree identities. No original large integer, endpoint expansion, or accepted computation is needed.

### Inputs

Only:


$$
P=t^4-t^3+xt-2x,
$$


the displayed $4\times4$ matrices $L,K$, and the rational $2\times2$ matrices defined in (4.6)–(4.7) and (6.2).

### Expected verifiable outputs

1. **Polynomial system check.**
   Verify
   

$$
L=4C^3-3C^2+xI,\qquad K=2xN-2xL'.
$$


   All matrix entries involved have degree at most one in $x$, apart from the intermediate matrix products.

2. **Connection denominator check.**
   Verify
   

$$
\det L=-x^2(27x^2+1264x+108).
$$


   The adjugate has entries of degree at most three in $x$; the numerator $\operatorname{adj}(L)K$ has degree at most four.

3. **Transition determinant check.**
   Clear
   

$$
(n+1)(6n+1)(6n+3)(6n+5)
$$


   in $T(n)$. Its polynomial numerator entries have degree at most four. Verify (4.9) by polynomial multiplication.

4. **Observation determinant check.**
   Clear
   

$$
(n+1)(6n+1)(6n+3)(2n+1).
$$


   The resulting observation numerator entries have degree at most four. Verify (6.3) and the cubic factorization (6.4).

These checks corroborate fixed algebraic identities. They neither evaluate an original tuple nor prove an infinite-family normalization theorem. They are not prerequisites left in place of the coefficient derivation.

---

## 10. Full-producer and primitive-arithmetic boundaries

The endpoint connection does not modify the original finite spaces:


$$
0\le v\le2n-2,
$$




$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m),\qquad
d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
$$



Both corrected columns and the nonlinear elimination remain


$$
\widehat Z^{\,\mathrm{act}}
=\widehat Z^{\,c}-3^6WE_{\mathrm{act}}^{-1}T_R,
$$




$$
S_{\mathrm{act}}-S_c
=3^6K_Z-3^{12}T_R^TE_{\mathrm{act}}^{-1}T_R,
$$


with


$$
Q_{\mathrm{act}}=Q_c+3^6R_{\mathrm{prod}},
\qquad
R_{\mathrm{prod}}=R_{25}+3^{25}\Delta_{25}.
$$


All $\Delta_H$ layers, unpaired cutoff contributions, exterior terms, both corrected factors, and nonlinear corrections remain required for both full producers.

The complete force retains both leading extractions, every permitted lower pole, factorial forcing, and LOW subtraction. The terminal return remains


$$
\mu_{i+\nu}^{\langle26\rangle}
+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}^{\langle26\rangle}
=b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2,
$$




$$
J^T\varepsilon+\omega
=-\varepsilon-s_{\mathrm{ret}}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$


No moment beyond $D-4$ is introduced, and $\omega_{\nu-1}$ is retained.

All row contents, the actual multiplier, and the least actual clearer precede


$$
A_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over all primes. For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and the same-index whole error is


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\mathrm{clr}}^{m+1}}{g_\ell}
\det H_{\mathrm{complete}}.
}
$$



Likewise, the second producer retains


$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B,
$$


with its whole same-index error


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$



No theorem above evaluates either whole error, proves its nonvanishing, or proves its decay after the actual all-prime reduction.

---

## 11. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Exact turn11 algebraic endpoint formulas | Retained |
| Proposed reciprocal identities and distinguished sign | **Verified here** |
| Quartic parameter and anti-invariant differential subspace | **Derived here** |
| Concrete polynomial differential system and seed | **Proved here** |
| Genuine differential rank exactly four | **Proved here by local branch certificate** |
| Complete two-coordinate coefficient recurrence | **Proved here** |
| Forward leading factors and all nonnegative exceptional steps | **Listed and resolved here** |
| Same-index endpoint observation matrix | **Derived here** |
| Explicit inverse-lattice observability inequality | **Proved here** |
| Original-branch four-to-six-digit observation relation | **Proved here** |
| Full cumulative linear content bound | **Proved here** |
| $O(\log m)$ common-content bound | Not proved |
| Actual primitive endpoint class on an original tuple | Not evaluated |
| Original-family endpoint avoidance or approach bound | Open |
| Infinite unrestricted characteristic-zero digit rank | Retained at its established scope |
| Normalized or original-language digit construction | Not excluded; not constructed |
| Full-producer and all-prime whole-error obligations | Open |

### Final result

The coefficient connection has advanced from algebraic closure to an explicit, seeded recurrence. Its differential rank is exactly four, while its two-coordinate coefficient state has a directly controlled observation map.

The most useful new arithmetic conclusion on the original branch is


$$
\boxed{
4\le c(V_{m-1})-c_m\le6.
}
$$


Endpoint projection is therefore no longer an unspecified source of normalization loss.

The exact remaining local bottleneck is **a sharp cumulative content theorem for the actual seeded product of the displayed matrices $T(n)$, together with control of its normalized direction at the original indices**. The cumulative theorem proved here is linear; it cannot be relabeled logarithmic.

Beyond that bottleneck remain the complete finite producers, forcing and terminal returns, all row contents, the all-prime final gcds, the actual primitive denominators, and the whole same-index errors.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved by this work.}}
$$


