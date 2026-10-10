> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## Normalization result, conditional on the fixed-depth support theorem

The normalization closes, but it requires distinguishing two integer coefficient pairs:

1. the pair obtained by multiplying the determinant by $\ell^k$; and
2. the pair obtained using the **least actual two-coefficient denominator clearer**.

These pairs have the same primitive reduction, but generally do **not** have the same gcd. The bound $d+r\nu$ below is justified for the first pair. It does not, without an additional denominator calculation, give that bound for the gcd of the second pair.

Throughout, the turn-25 support theorem is a **claimed input under independent audit**, not a theorem reproved here. The block-integrality and primitive-normalization facts quoted below are also retained dependencies.

### 1. Domain and complete actual scale

Fix an integer $r\ge6$, and impose precisely


$$
j>0,\qquad v_3(j)\ge r-2,\qquad n=4^j+1,
$$




$$
h=\lfloor\log_3(4n-3)\rfloor,\qquad H=3^{h-1},
\qquad 0<D=H-(n-2)<H/C_r,\qquad h\ge r+2,
$$


where


$$
C_r=512(r+1)^2 3^{r-1}.
$$


Retain


$$
A=n-2=H-D,\quad m=\frac{A+1}{2},\quad k=m+1,
\quad d=\frac{3D}{2}-1,\quad \nu=\frac D2-1.
$$


Thus $d=D+\nu$, and $D\ge6$ is an even multiple of $3$.

The primitive polynomial is


$$
Q=\lambda Q^{\rm loc},\qquad \lambda=L_n/3\in\mathbb Z_3^\times.
$$


Its actual endpoint is not replaced by the core endpoint:


$$
Q(-1)\ne0,\qquad e_Q=v_3(Q(-1)).
$$


The supplied endpoint theorem gives $e_Q=2v_3((n-1)!)$; the content argument below only needs $e_Q\ge0$.

Let


$$
\ell=\operatorname{lcm}(1,3,\ldots,4n-3),\qquad
u_\ell=\frac{4\ell}{3^h}\in\mathbb Z_3^\times.
$$


For the actual monomial columns $y^a$, $0\le a\le m$, define


$$
G_{ab}=\mathcal M(Q^{\rm loc}y^{a+b}),
$$


where the complete functional is


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+\sum_{\substack{0\le t\le h\\c\ge1\ {\rm odd},\,3\nmid c\\
c3^t\le4n-3}}
3^{h-t}c^{-1}
[y^{(c3^t-1)/2}]
\frac{F-F(-1)}{y+1},
\qquad \mathfrak f(y^s)=(2s)!.
$$


This retains the factorial force, every admissible pole, its exact rational unit, and endpoint subtraction.

If $R_{\rm rat}$ is the actual rational constant matrix formed with $Q$, then


$$
T:=\ell R_{\rm rat}=\omega G,\qquad
\boxed{\omega=u_\ell\lambda\in\mathbb Z_3^\times.}
\tag{1}
$$



The endpoint basis


$$
1,\ (y+1),\ (y+1)y,\ldots,(y+1)y^{m-1}
$$


is unimodular. In monomial coordinates its distinguished cofactor is


$$
\mathcal C_T=v^T\operatorname{adj}(T)v,\qquad
v=(1,-1,\ldots,(-1)^m)^T.
$$


In the endpoint basis it is exactly the cofactor of the first diagonal entry.

---

## 2. Exact block scales and transported endpoint

Use HIGH $y^d,\ldots,y^m$, LOW unit columns


$$
U=(1,y,\ldots,y^{D-1}),
$$


and the actual remaining LOW columns


$$
Z=(y^i(y-1)^D)_{0\le i<\nu}.
$$


The change from LOW monomials to $(U,Z)$ has determinant $1$.

In the original scale the LOW block and LOW–HIGH block are respectively $3L$ and $3X$, while HIGH is $E$. The first HIGH block is a unit block: its residue is the anti-triangular matrix $E_0$ with unit anti-diagonal. HIGH-first elimination therefore gives $3$ times the first normalized LOW form.

For the exact formulas it is convenient to perform the equivalent LOW-first elimination. Put


$$
B_U=U^TLZ,\qquad C=L_U^{-1}B_U,
$$




$$
\widetilde V=Z^TX-C^TX_U,\qquad
\widehat E=E-3X_U^TL_U^{-1}X_U.
$$


The $D\times D$ matrix $L_U$ and the HIGH matrix $\widehat E$ are units over $\mathbb Z_3$. Integral determinant-one Schur transformations yield


$$
\boxed{
P^TGP=\operatorname{diag}(3L_U,\widehat E,3\mathcal R),
}
\tag{2}
$$


where


$$
\mathcal R
=Z^TLZ-B_U^TL_U^{-1}B_U
-3\widetilde V\widehat E^{-1}\widetilde V^T.
\tag{3}
$$


Here $\mathcal R$ is precisely the first-LOW-normalized radical form in turn 25.

The corresponding exact radical columns are


$$
W=Z-UC-
\bigl(Y-UL_U^{-1}X_U\bigr)\widehat E^{-1}(3\widetilde V^T),
\tag{4}
$$


where $Y$ denotes the original HIGH columns. Thus their endpoint is $W(-1)$, including both corrections. The retained support input gives


$$
e_R:=W(-1)\equiv((-1)^i)_{i<\nu}\ne0\pmod3.
\tag{5}
$$


Write $e_U,e_H,e_R=P^Tv$ for the full transported endpoint, and set


$$
a_U=e_U^TL_U^{-1}e_U,\qquad
a_H=e_H^T\widehat E^{-1}e_H,\qquad
u_0=\det L_U\det\widehat E\in\mathbb Z_3^\times.
$$



---

## 3. Determinant and distinguished cofactor: exact identities

From (2),


$$
\boxed{\det G=3^d u_0\det\mathcal R.}
\tag{6}
$$


More importantly, the distinguished cofactor is


$$
\boxed{
v^T\operatorname{adj}(G)v
=
3^{d-1}u_0
\left[
(a_U+3a_H)\det\mathcal R
+e_R^T\operatorname{adj}(\mathcal R)e_R
\right].
}
\tag{7}
$$


For nonsingular $\mathcal R$, this follows by multiplying the endpoint inverse contraction of (2) by its determinant. The identity extends to singular $\mathcal R$ by the polynomial adjugate identity; no radical inverse is required in (7).

Restoring every scalar unit gives


$$
\boxed{
\det T=\omega^k3^du_0\det\mathcal R,
}
\tag{8}
$$




$$
\boxed{
\mathcal C_T=\omega^{k-1}3^{d-1}u_0
\left[
(a_U+3a_H)\det\mathcal R
+e_R^T\operatorname{adj}(\mathcal R)e_R
\right].
}
\tag{9}
$$



Now invoke the **claimed turn-25 input**


$$
\mathcal R=3^rJ,\qquad J\in\operatorname{Mat}_\nu(\mathbb Z_3).
$$


Equations (8)–(9) become


$$
\det T=\omega^ku_0\,3^{d+r\nu}\det J,
\tag{10}
$$




$$
\mathcal C_T
=\omega^{k-1}u_0\,3^{d-1+r(\nu-1)}
\left[
e_R^T\operatorname{adj}(J)e_R
+3^r(a_U+3a_H)\det J
\right].
\tag{11}
$$


These give exact valuation interfaces, including possible cancellation:


$$
v_3(\det T)=d+r\nu+v_3(\det J),
\tag{12}
$$




$$
v_3(\mathcal C_T)=d-1+r(\nu-1)+
v_3\!\left(
e_R^T\operatorname{adj}(J)e_R+
3^r(a_U+3a_H)\det J
\right).
\tag{13}
$$


As usual $v_3(0)=+\infty$.

In particular,


$$
\boxed{
v_3(\det T)\ge d+r\nu,\qquad
v_3(\mathcal C_T)\ge d-1+r(\nu-1).
}
\tag{14}
$$


The cofactor loses **one full original-scale radical factor**, of depth $r+1$. The nonzero endpoint residue (5) does not by itself eliminate this loss or prove equality in (13).

---

## 4. Actual coefficient-pair content and the least clearer

Write the rational determinant polynomial as


$$
\det H_{\rm complete}=\beta_0+\beta_1S,\qquad S=e+\pi.
$$


The $\ell^k$-cleared integer pair is exactly


$$
A_\ell=\det T,\qquad
B_\ell=\ell Q(-1)\mathcal C_T,
\tag{15}
$$


so that


$$
A_\ell+B_\ell S=\ell^k\det H_{\rm complete}.
$$



The response has the additional depth


$$
v_3(B_\ell)=h+e_Q+v_3(\mathcal C_T).
$$


Consequently,


$$
v_3(B_\ell)\ge d+r\nu+(h+e_Q-r-1).
\tag{16}
$$


Since $h\ge r+2$ and $e_Q\ge0$, the last parenthesis is positive. Thus, for


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|),
$$


we have the justified conclusion


$$
\boxed{v_3(g_\ell)\ge L_r:=d+r\nu.}
\tag{17}
$$


This is a comparison of both actual coefficients, not an extrapolation from the cofactor bound alone.

### Conversion to the least actual two-coefficient clearer

Let


$$
\delta=\operatorname{lcm}\bigl(\operatorname{den}(\beta_0),
\operatorname{den}(\beta_1)\bigr),
\qquad
g_*=\gcd(|\delta\beta_0|,|\delta\beta_1|).
$$


Because $\ell^k$ clears both coefficients,


$$
t_0=\ell^k/\delta\in\mathbb Z_{>0},\qquad
g_\ell=t_0g_*.
\tag{18}
$$


Put


$$
a=v_3(A_\ell),\quad b=v_3(B_\ell),\quad M=\min(a,b).
$$


Then exactly


$$
\boxed{
v_3(\delta)=\max(0,kh-M),\qquad
v_3(g_*)=\max(0,M-kh).
}
\tag{19}
$$


Therefore (17) supplies only


$$
\boxed{v_3(g_*)\ge\max(0,L_r-kh).}
\tag{20}
$$


On the present domain $L_r<kh$, so this particular lower bound for the **least-cleared pair gcd is zero**. This is not a contradiction: much of the $\ell^k$-pair content can simply cancel a nonminimal clearer.

The two normalizations nevertheless give exactly the same primitive multiplier:


$$
\boxed{\frac{\delta}{g_*}=\frac{\ell^k}{g_\ell}.}
\tag{21}
$$



---

## 5. Uniform exponential-scale limitation

Since $n=H-D+2$ and $D<H/C_r$,


$$
\frac Dn<\frac1{C_r-1}.
$$


Hence


$$
\boxed{\frac{rD}{n}<\frac{r}{512(r+1)^2 3^{r-1}-1}.}
\tag{22}
$$


The right side decreases for integers $r\ge6$. At $r=6$,


$$
C_6=6\,096\,384,
$$


and therefore the uniform bound is


$$
\boxed{\frac{rD}{n}<\frac6{6\,096\,383}<9.85\times10^{-7}.}
\tag{23}
$$



The additional radical contribution $r\nu$ satisfies


$$
\frac{r\nu\log3}{n}
<\frac{3\log3}{6\,096\,383}<5.41\times10^{-7}.
\tag{24}
$$


Including the first LOW factor,


$$
L_r=d+r\nu=\frac{r+3}{2}D-(r+1),
$$


so


$$
\boxed{
\frac{L_r\log3}{n}
<
\frac{(r+3)\log3}{2(C_r-1)}
\le
\frac{9\log3}{2(6\,096\,383)}
<8.12\times10^{-7}.
}
\tag{25}
$$


These quantify the guaranteed divisor furnished by this theorem; they are **not upper bounds on the actual gcd**.

Moreover, if one lets admissible depths $r$ grow, then


$$
\frac{L_r}{n}\longrightarrow0
$$


under these explicit restrictions. Increasing the depth therefore does not produce an unbounded exponential-rate gain; its guaranteed contribution becomes subexponential along such a growing-depth selection.

The divisibility condition independently requires


$$
j\ge3^{r-2},\qquad r\le2+\log_3j,
$$


and thus, since $n-1=4^j$, permits at most logarithmic growth in $\log n$. It does not compensate for the exponentially shrinking allowed ratio $D/H$.

Accordingly, this contribution alone cannot overcome any fixed positive exponential deficit by taking $r\to\infty$. At a fixed depth it might help an argument already within the very small rate in (25), but no requisite analytic comparison is supplied here.

---

## 6. Primitive denominator, whole error, and unresolved endpoint digit

Where $B_\ell\ne0$, retain


$$
q=\frac{|B_\ell|}{g_\ell}
=\frac{|\delta\beta_1|}{g_*},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The actual denominator valuation is


$$
\boxed{v_3(q)=\max(0,b-a).}
\tag{26}
$$


Lower bounds for $a$ and $b$ cannot be subtracted to evaluate this quantity.

The whole real error is exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
\det H_{\rm complete}
=
\frac{\operatorname{sgn}(B_\ell)\delta}{g_*}
\det H_{\rm complete}.
}
\tag{27}
$$


Neither actual response nonvanishing nor whole-error nonvanishing follows from the claimed support theorem. Polynomial endpoint nonvanishing is a separate retained fact.

I do not claim an evaluated first post-core perturbation. The newly normalized, precise missing quantities are


$$
\det J,\qquad
e_R^T\operatorname{adj}(J)e_R+
3^r(a_U+3a_H)\det J,
\qquad J=3^{-r}\mathcal R,
$$


with the **actual** endpoint (4), not its residue alone. Their relative valuations determine the arithmetic obstruction in (26). The supplied fixed-depth theorem does not evaluate them.

### Closing ledger

1. **New result and proof status.** Conditional on the audited block interfaces and claimed turn-25 divisibility, equations (10)–(13) give the fully scaled determinant and distinguished-cofactor identities. They prove $v_3(g_\ell)\ge d+r\nu$, but give only the bound (20) for the gcd using the least actual clearer. Equations (22)–(25) uniformly quantify the small, decreasing exponential-rate contribution.

2. **Exact remaining bottleneck.** Evaluate the actual divided radical determinant and transported endpoint contraction, including cancellation in (13), and compare the resulting primitive multiplier with a nonzero whole determinant error. These results do not decide irrationality of $e+\pi$.

3. **Computation request.** None. No finite computation is needed for this normalization, and finite valuations would not evaluate its remaining infinite assertions.
