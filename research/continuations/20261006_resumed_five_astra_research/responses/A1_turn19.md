> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1 turn19 — The complete mixed source has a seven-coordinate terminal obstruction

## Executive conclusion

The new modulo-$81$ receipt is accepted at its stated finite scope: forty characteristic-zero endpoint comparisons at $m=221,\ldots,240$, and 121 middle words of lengths $0,\ldots,4$. Its three named outputs agree with the turn17 formula. No original real-window index was evaluated, and I do not request that calculation again. The separately announced full-content checks at $m=241,\ldots,260$ remain pending; no output from them is assumed.

The main new result concerns the **actual complete mixed force**, not another raw-content bound.

On the retained sufficiently large original window, write the first producer jet as


$$
R_{\rm prod}(y)\equiv
(y+1)(y-1)^{A-6}\mathcal B(y-1)\pmod3,
\qquad
\mathcal B(x)=\sum_{r=0}^{6}a_rx^r.
$$


This is the precision-one terminal jet supplied by the accepted saturation theorem on $t=v_3(A)=5$.

Let


$$
T_R=K(W,\widehat Z^{\,c}),
\qquad
K(f,g)=\mathcal M(R_{\rm prod}fg),
$$


with the **complete** finite functional $\mathcal M$. Then $T_R\in3M(\mathbb Z_3)$, and seven entries of its actual terminal column satisfy


$$
\boxed{
\begin{pmatrix}
(T_R/3)_{U_5,\nu-1}\\
(T_R/3)_{U_4,\nu-1}\\
(T_R/3)_{U_3,\nu-1}\\
(T_R/3)_{U_2,\nu-1}\\
(T_R/3)_{U_1,\nu-1}\\
(T_R/3)_{U_0,\nu-1}\\
(T_R/3)_{Y_m,\nu-1}
\end{pmatrix}
\equiv
\begin{pmatrix}
1&0&0&0&0&0&0\\
2&1&0&0&0&0&0\\
1&2&1&0&0&0&0\\
0&1&2&1&0&0&0\\
0&0&1&2&1&0&0\\
0&0&0&1&2&1&0\\
0&2&2&0&1&1&2
\end{pmatrix}
\begin{pmatrix}a_0\\a_1\\a_2\\a_3\\a_4\\a_5\\a_6\end{pmatrix}
\pmod3.
}
\tag{E.1}
$$


The matrix has determinant $2$ in $\mathbb F_3$. Consequently,


$$
\boxed{
T_R\in9M(\mathbb Z_3)
\iff
R_{\rm prod}\in3\mathbb Z_3[y].
}
\tag{E.2}
$$


In fact, the terminal column alone detects the right-hand condition.

The last row of (E.1) contains the indispensable boundary contribution


$$
\boxed{-a_6.}
$$


It comes from the corrected terminal column and the highest permitted pole. Removing that return would destroy the injectivity of this first-layer source test.

This gives a sharp obstruction to the proposed $3^g$-factor for the **retained monic residual columns**:

* on the fixed-tail family $g\ge3$;
* therefore $T_R=3^g\widetilde T_R$, with integral $\widetilde T_R$, necessarily implies $R_{\rm prod}\equiv0\pmod3$;
* if the actual seven-coordinate jet $\mathcal B$ is nonzero, then
  

$$
\min v_3(T_R)=1,
$$


  so that proposed factorization fails.

The actual values of these seven jet coefficients are not supplied in the attached reports. Thus (E.2) is an evaluated source criterion, not a claim that the actual jet is nonzero.

There is also a separate, unconditional normalization obstruction. The actual residual polynomials and their transported endpoints satisfy


$$
\widehat z_i^{\,c}\equiv z_i\pmod3,\qquad
\widehat z_i^{\,\rm act}(-1)\equiv(-1)^i\pmod3.
$$


They are primitive. They cannot be identified integrally with the raw Jacobi pair, whose full polynomial content is at least $3$. Homogeneous $3^g$ and $3^{2g}$ factorizations do hold for **projected Jacobi channels**, but those channels are $3^g$-divisible combinations of the retained primitive residual columns, not the original columns themselves.

The exact remaining local task is therefore concrete:

> Evaluate the actual terminal producer jet in (E.1). If it vanishes, continue with the complete higher-layer source and actual inverse; if it does not, retain the resulting inhomogeneous correction rather than dividing the actual source by $3^g$.

The four-digit Christoffel loss, the actual eliminated-inverse bill, the original terminal return, the all-prime gcd, and the whole nonzero same-index error all remain in force.

---

## 1. Domain and source status

Retain


$$
j>0,\qquad j\equiv81\pmod{243},\qquad
m=2^{2j-1},\qquad n=2m+1,\qquad A=2m-1,
$$


and the exact window


$$
H=3^{h-1},\qquad D=H-A,\qquad
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\quad C_{16}=147968\,3^{15}.
\tag{1.1}
$$


For the deeper fixed-tail conclusions, retain


$$
j\equiv84645\pmod{531441}.
\tag{1.2}
$$


No real-window correction is replaced by an asymptotic surrogate.

The finite spaces are unchanged:


$$
U_u=x^u\quad(0\le u<D),\qquad x=y-1,
$$




$$
z_i=x^Dy^i\quad(0\le i<\nu),\qquad
Y_b=y^b\quad(d\le b\le m),
$$




$$
d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
\tag{1.3}
$$


In particular,


$$
d=D+\nu,\qquad \deg z_i\le d-1.
$$



The following turn18 results are reused rather than rederived:

* the trailing-residue exception counts;
* the pattern-$20$ full-polynomial lower bound;
* equality of monomial and Bernstein contents;
* the exact eight-state content evaluator;
* the sixteen-state endpoint-at-full-content evaluator.

Their finite independent checks are distinct from their symbolic proofs.

The paid modulo-$81$ receipt now corroborates the turn17 formula on its stated finite inputs. In particular,


$$
H=\varnothing,\ 0,\ 20
\quad\longmapsto\quad
(27,54),\ (54,27),\ (0,0)\pmod{81}.
$$


It establishes neither an original-window primitive endpoint nor actual-source divisibility.

---

## 2. Two core conventions must not be conflated

This distinction matters when the whole factorial term is retained.

Define


$$
\mathcal D(F)=\frac{F(y)-F(-1)}{y+1},
\qquad
\mathfrak f(y^r)=(2r)!,
$$


and


$$
\boxed{
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v]\mathcal D(F)}{2v+1}.
}
\tag{2.1}
$$


Thus the cutoff is exactly


$$
2v+1\le4n-3.
$$



Write


$$
Q_{\rm act}=Q_c+3^6R_{\rm prod},
\qquad
R_{\rm prod}=R_{25}+3^{25}\Delta_{25},
$$




$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A.
\tag{2.2}
$$



For the **complete core**


$$
G_c(f,g)=\mathcal M(Q_cfg),
$$


one has exactly


$$
\boxed{
G_{\rm act}-G_c=3^6K,\qquad
K(f,g)=\mathcal M(R_{\rm prod}fg).
}
\tag{2.3}
$$



By contrast, the turn18 displayed perturbation


$$
-\frac{3^h}{4}\mathfrak f(Q_{\rm act}fg)
+
3^{h+6}\sum_{v=0}^{2n-2}
\frac{[y^v]\mathcal D(R_{\rm prod}fg)}{2v+1}
\tag{2.4}
$$


is the difference from the **pole-only core**. Relative to the complete core it equals


$$
\boxed{
-\frac{3^h}{4}\mathfrak f(Q_cfg)+3^6K(f,g).
}
\tag{2.5}
$$



Both conventions are legitimate. They are not interchangeable. In particular, the complete-core corrected-column formula must use (2.3); if a Jacobi identification was made for a pole-only reference, the extra core factorial form in (2.5) remains part of its actual residual.

Below, $E_c,\widehat Z^{\,c}$ refer to the complete-core definitions explicitly supplied in turn7.

---

## 3. Both complete mixed columns and the quadratic source

Put


$$
W=[U\ Y],\qquad
E_c=G_c(W,W),\qquad C_c=G_c(W,Z),
$$




$$
\widehat Z^{\,c}=Z-WE_c^{-1}C_c.
\tag{3.1}
$$


Write its columns as $F_i=\widehat z_i^{\,c}$.

For any two original residual indices $i_0,i_1$, the two columns of the complete mixed source are explicitly


$$
\boxed{
\begin{aligned}
(T_R)_{w,i_\alpha}
={}&-\frac{3^h}{4}\mathfrak f(R_{\rm prod}wF_{i_\alpha})\\
&+3^h\sum_{v=0}^{2n-2}
\frac{
[y^v]\displaystyle
\frac{R_{\rm prod}(y)w(y)F_{i_\alpha}(y)
-R_{\rm prod}(-1)w(-1)F_{i_\alpha}(-1)}
{y+1}
}{2v+1},
\end{aligned}
}
\tag{3.2}
$$


for $\alpha=0,1$ and every retained LOW or HIGH row $w$.

Likewise,


$$
\boxed{
\begin{aligned}
(K_Z)_{ij}
={}&-\frac{3^h}{4}\mathfrak f(R_{\rm prod}F_iF_j)\\
&+3^h\sum_{v=0}^{2n-2}
\frac{
[y^v]\displaystyle
\frac{R_{\rm prod}(y)F_i(y)F_j(y)
-R_{\rm prod}(-1)F_i(-1)F_j(-1)}
{y+1}
}{2v+1}.
\end{aligned}
}
\tag{3.3}
$$



These are complete expressions: factorial, LOW subtraction, all allowed poles, $R_{25}$, and $\Delta_{25}$ are retained.

Set


$$
E_{\rm act}=E_c+3^6K(W,W).
$$


Then


$$
\boxed{
\widehat Z^{\,\rm act}
=
\widehat Z^{\,c}-3^6WE_{\rm act}^{-1}T_R,
}
\tag{3.4}
$$




$$
\boxed{
S_{\rm act}-S_c
=
3^6K_Z-3^{12}T_R^TE_{\rm act}^{-1}T_R.
}
\tag{3.5}
$$


The formulas apply to both selected columns and their entire $2\times2$ Schur subblock, or to the full residual block. No higher perturbation terms have been omitted: they are contained in the actual inverse.

---

## 4. What full-content-normalized Jacobi coordinates actually normalize

Let the paid content evaluator give


$$
r_+=\operatorname{cont}_3J_m^{[A]},
\qquad
r_-=\operatorname{cont}_3J_{m-1}^{[A]},
\qquad
g=\min(r_+,r_-).
$$


Use only this actual common polynomial content:


$$
J_m^{[A]}=3^gP,\qquad
J_{m-1}^{[A]}=3^gQ.
\tag{4.1}
$$


At least one of $P,Q$ is primitive as a polynomial.

On the stated integral scalar branch,


$$
Z_{\rm src}=3^g\widetilde Z_{\rm src},
$$


and


$$
\boxed{
(3y-\eta)\widetilde Z_{\rm src}
=
(y-\beta_m-\chi_m)P-\rho_mQ.
}
\tag{4.2}
$$


This is the accepted homogeneous Christoffel normalization. It does not make the Christoffel coordinate change unimodular.

### 4.1 Exact projection into the retained finite producer

Because the ordered columns


$$
U_0,\ldots,U_{D-1},\ z_0,\ldots,z_{\nu-1},\
Y_d,\ldots,Y_m
$$


have successive degrees and leading coefficient $1$, they form an integral unimodular basis of $\mathbb Z_3[y]_{\le m}$.

Let


$$
\Lambda:\mathbb Z_3[y]_{\le m}\longrightarrow\mathbb Z_3^\nu
$$


extract the $Z$-coordinates in this basis. The complete-core orthogonal projection is


$$
\Pi_c F=F-WE_c^{-1}G_c(W,F).
$$


Since it kills $W$,


$$
\boxed{
\Pi_cF=\widehat Z^{\,c}\Lambda(F).
}
\tag{4.3}
$$


It is integral in the retained normalization.

For the two Jacobi/Christoffel channels, set


$$
C_{\rm JC}=
\bigl[\Lambda(P)\ \ \Lambda(\widetilde Z_{\rm src})\bigr].
$$


Then


$$
\boxed{
\bigl[\Pi_cJ_m^{[A]}\ \ \Pi_cZ_{\rm src}\bigr]
=
3^g\widehat Z^{\,c}C_{\rm JC}.
}
\tag{4.4}
$$



Consequently their complete projected mixed and quadratic sources are


$$
\boxed{
T_{\rm JC}=3^gT_RC_{\rm JC},
}
\tag{4.5}
$$




$$
\boxed{
K_{\rm JC}=3^{2g}C_{\rm JC}^TK_ZC_{\rm JC}.
}
\tag{4.6}
$$


These factorizations include the full functional (2.1), not merely its leading pole.

The actual projected channels satisfy


$$
\boxed{
3^{-g}
\bigl[\Pi_{\rm act}J_m^{[A]}\ \ \Pi_{\rm act}Z_{\rm src}\bigr]
=
\widehat Z^{\,c}C_{\rm JC}
-3^6WE_{\rm act}^{-1}T_RC_{\rm JC}.
}
\tag{4.7}
$$



This is a genuine complete-source normalization theorem for the projected channels.

### 4.2 Why this does not divide the original corrected columns

For the original columns,


$$
\Lambda(F_i)=e_i.
$$


Moreover,


$$
F_i\equiv z_i\pmod3.
\tag{4.8}
$$


Thus every $F_i$ is primitive.

If $g>0$, no original $F_i$ can be an integral combination of the two raw projected channels in (4.4): the latter have all residual coordinates divisible by $3^g$, whereas $e_i$ is primitive.

Equivalently, if one writes an affine decomposition


$$
[F_{i_0}\ F_{i_1}]
=
3^g\widehat Z^{\,c}C_{\rm JC}A
+\widehat Z^{\,c}H,
\qquad
H=[e_{i_0}\ e_{i_1}]-3^gC_{\rm JC}A,
\tag{4.9}
$$


with integral $A$, then


$$
\boxed{H\equiv[e_{i_0}\ e_{i_1}]\pmod3.}
\tag{4.10}
$$


The inhomogeneous residual term cannot disappear.

Its mixed source is exactly


$$
T_R[e_{i_0}\ e_{i_1}]
=
3^gT_RC_{\rm JC}A+T_RH,
\tag{4.11}
$$


and its quadratic source includes all three additional terms


$$
3^gA^TC_{\rm JC}^TK_ZH,\quad
3^gH^TK_ZC_{\rm JC}A,\quad
H^TK_ZH.
\tag{4.12}
$$



This identifies the missing hypothesis in a purported direct use of turn18 §13: **linearity normalizes the projected Jacobi channels, not the primitive affine residual coordinates left in (4.9).**

---

## 5. The complete first mixed-force layer

We now evaluate that actual source layer, including the terminal correction.

### 5.1 Exact pole accounting modulo $9$

On the original window,


$$
4n-3=4A+5=4H-4D+5.
$$


For sufficiently large eligible indices, it lies strictly between $3H$ and $4H$. Among the permitted odd denominators:

* the only denominator of valuation $h$ is $3H$;
* the only denominator of valuation $h-1$ is $H$.

Put


$$
r_*=\frac{3H-1}{2},\qquad r_1=\frac{H-1}{2}.
$$


For an integral polynomial of the relevant degree,


$$
\boxed{
\mathcal M(F)
\equiv
[y^{r_*}]\mathcal D(F)
+
3[y^{r_1}]\mathcal D(F)
\pmod9.
}
\tag{5.1}
$$



This is a consequence of the **original finite cutoff**. All lower poles have coefficients divisible by $9$. The complete factorial term is divisible by $9$, since $h\ge2$ and $\mathfrak f(F)$ is integral. It has been evaluated at this layer, not removed from the exact source.

### 5.2 The actual corrected terminal column

The accepted complete-core formula is


$$
\boxed{
F_i\equiv z_i-3\pi(y^d)\mathbf1_{i=\nu-1}\pmod9,
}
\tag{5.2}
$$


where


$$
\pi(y^d)=y^d-\operatorname{rem}_{x^D}y^d.
$$


The polynomial $\pi(y^d)$ is monic of degree $d$.

For every retained $w\in W$,


$$
\deg(R_{\rm prod}wz_i)\le A+m+d,
$$


so its endpoint-subtracted quotient has degree at most $r_*-1$. Hence the top-pole coefficient is absent for the uncorrected $z_i$.

For the correction in (5.2), a top-pole coefficient can occur only when


$$
w=Y_m,\qquad i=\nu-1.
$$


In that case,


$$
[y^{r_*}]\mathcal D(R_{\rm prod}y^m\pi(y^d))
=[y^{A+1}]R_{\rm prod}.
\tag{5.3}
$$



Let


$$
c_R=[y^{A+1}]R_{\rm prod}.
$$


Combining (5.1)–(5.3) gives the complete identity


$$
\boxed{
\frac{(T_R)_{w,i}}3
\equiv
[y^{r_1}]\mathcal D(R_{\rm prod}wz_i)
-c_R\,\mathbf1_{w=Y_m}\mathbf1_{i=\nu-1}
\pmod3.
}
\tag{5.4}
$$



In particular, $T_R\in3M(\mathbb Z_3)$.

The second term in (5.4) is the original terminal HIGH return. It is not a dispensable boundary error.

### 5.3 Substituting the paid producer jet

On $t=5$, the precision-one terminal width is $6$. Thus


$$
R_{\rm prod}\equiv(y+1)x^{A-6}\mathcal B(x)\pmod3,
\qquad \deg\mathcal B\le6.
\tag{5.5}
$$


Since $A+D=H$, formula (5.4) becomes


$$
\boxed{
\frac{(T_R)_{w,i}}3
\equiv
[y^{r_1}]x^{H-6}\mathcal B(x)w(y)y^i
-a_6\,\mathbf1_{w=Y_m}\mathbf1_{i=\nu-1}
\pmod3.
}
\tag{5.6}
$$


Here $c_R\equiv a_6\pmod3$.

Although (5.5) is only modulo $3$, that is enough for (5.6). Indeed, replacing $R_{\rm prod}$ by $R_{\rm prod}+3R'$ changes the divided mixed force by $K_{R'}(W,F_i)$, which is zero modulo $3$ by the same top-degree argument. No unpaid extra producer digit has been used.

---

## 6. The seven-coordinate terminal detector

### 6.1 LOW rows

For $w=U_u=x^u$, equation (5.6) is


$$
\frac{(T_R)_{U_u,i}}3
\equiv
[y^{r_1-i}]x^{H-6+u}\mathcal B(x)\pmod3.
\tag{6.1}
$$


It vanishes for $u\ge6$.

For $0\le u\le5$, use


$$
x^H\equiv y^H-1\pmod3.
$$


At coefficient indices strictly between $0$ and $H$,


$$
[y^N]x^{H-\ell}
=
(-1)^{\ell+1}\binom{N+\ell-1}{\ell-1}
\pmod3.
$$


Therefore


$$
\boxed{
\frac{(T_R)_{U_u,i}}3
\equiv
\sum_{b=0}^{5-u}
a_b(-1)^{7-u-b}
\binom{r_1-i+5-u-b}{5-u-b}
\pmod3.
}
\tag{6.2}
$$



At the terminal index $i=\nu-1$,


$$
r_1-i=m+1.
$$


The original parameterization gives $m\equiv5\pmod9$, so


$$
m+1\equiv6\pmod9.
$$


Lucas reduction of the six binomial factors in (6.2) gives the weights


$$
1,\ 2,\ 1,\ 0,\ 0,\ 0.
$$


Thus


$$
\begin{aligned}
(T_R/3)_{U_5,\nu-1}&=a_0,\\
(T_R/3)_{U_4,\nu-1}&=2a_0+a_1,\\
(T_R/3)_{U_3,\nu-1}&=a_0+2a_1+a_2,\\
(T_R/3)_{U_2,\nu-1}&=a_1+2a_2+a_3,\\
(T_R/3)_{U_1,\nu-1}&=a_2+2a_3+a_4,\\
(T_R/3)_{U_0,\nu-1}&=a_3+2a_4+a_5
\end{aligned}
\pmod3.
\tag{6.3}
$$



### 6.2 The actual terminal HIGH row

For $w=Y_m$ and $i=\nu-1$,


$$
r_1-m-i=1.
$$


Hence


$$
\frac{(T_R)_{Y_m,\nu-1}}3
\equiv
[y]x^{H-6}\mathcal B(x)-a_6.
$$


In characteristic $3$, the constant and linear coefficients of $x^{-6}=(1-y)^{-6}$ are $1,0$. Therefore


$$
[y]x^{H-6}\mathcal B(x)=-\mathcal B'(-1),
$$


and


$$
\boxed{
\frac{(T_R)_{Y_m,\nu-1}}3
\equiv-\mathcal B'(-1)-a_6
=
2a_1+2a_2+a_4+a_5+2a_6
\pmod3.
}
\tag{6.4}
$$



Equations (6.3)–(6.4) prove (E.1).

### Theorem 6.1 — Complete terminal mixed-force detection

Under the retained original-window hypotheses,


$$
\boxed{
T_R\in9M(\mathbb Z_3)
\iff
R_{\rm prod}\in3\mathbb Z_3[y].
}
\tag{6.5}
$$


It suffices to test the seven entries in (E.1).

**Proof.** The matrix in (E.1) has a unit lower-triangular $6\times6$ upper-left block and last diagonal entry $2$, so its determinant is $2$. The seven entries vanish exactly when $\mathcal B=0$.

By (5.5), $\mathcal B=0$ is equivalent to $R_{\rm prod}\equiv0\pmod3$. Conversely, if $R_{\rm prod}=3R'$, the complete mixed-force divisibility argument gives


$$
T_R=3K_{R'}(W,\widehat Z^{\,c})\in9M.
$$


∎

### Consequence for the proposed $g$-factor

On the fixed-tail progression, $g\ge3$. Therefore


$$
\boxed{
T_R\in3^gM
\ \Longrightarrow\
R_{\rm prod}\equiv0\pmod3.
}
\tag{6.6}
$$


If the actual $\mathcal B\ne0$, the stronger statement is


$$
\boxed{\min v_3(T_R)=1.}
\tag{6.7}
$$



This is not merely an example showing that linearity is insufficient. It is an exact criterion for the first divided layer of the actual retained source.

It does **not** yet decide which side of the criterion the actual producer occupies.

---

## 7. The quadratic source at the same layer

The same complete calculation gives


$$
\boxed{K_Z\in9M(\mathbb Z_3).}
\tag{7.1}
$$



Indeed, the top coefficient is absent for $R_{\rm prod}z_iz_j$ and for the first corrected-column terms. The remaining possible contribution modulo $9$ is


$$
3[y^{r_1}]x^{H+D-6}\mathcal B(x)y^{i+j}.
$$


Modulo $3$, this is an extraction from


$$
(y^H-1)x^{D-6}\mathcal B(x)y^{i+j}.
$$


Its lower factor has degree at most


$$
D+i+j\le2D-4<r_1,
$$


so the extraction is zero.

On the stated window, the stronger accepted turn7 support theorem gives


$$
K_Z\in3^9M
\tag{7.2}
$$


at its displayed hypotheses. I reuse that result only at that precision.

Neither (7.1) nor (7.2) gives $K_Z\in3^{2g}M$ for unbounded $g$. The complete expression remains (3.3), and the actual nonlinear term remains


$$
3^{12}T_R^TE_{\rm act}^{-1}T_R.
$$



In particular, if $\mathcal B\ne0$, the mixed force starts at order $3$, regardless of how deep the Jacobi polynomial content has become. Increasing $g$ does not remove this actual source.

---

## 8. The complete endpoint return is an additional inhomogeneous obstruction

Let


$$
w_-=W(-1),\qquad e_c=\widehat Z^{\,c}(-1),
$$


and retain the actual endpoint


$$
\boxed{
e_{\rm act}=e_c-3^6T_R^TE_{\rm act}^{-1}w_-.
}
\tag{8.1}
$$


In the original coordinates,


$$
e_c=Z(-1)-C_c^TE_c^{-1}w_-.
$$


The forcing term $Z(-1)$ is


$$
Z(-1)_i=(-2)^D(-1)^i.
$$


The accepted integral elimination gives


$$
\boxed{
(e_{\rm act})_i\equiv(-1)^i\pmod3.
}
\tag{8.2}
$$



Therefore dividing the original endpoint vector by the Jacobi content gives


$$
\boxed{
v_3(3^{-g}(e_{\rm act})_i)=-g.
}
\tag{8.3}
$$


Its lowest normalized layer is explicitly $(-1)^i$, at exponent $-g$.

This is an unconditional obstruction to treating the actual retained endpoint as a $3^g$-divisible Jacobi endpoint pair. The physical endpoint and the Jacobi observation are different coordinate objects until an exact identification, with its denominators, is proved.

### 8.1 Original terminal closure

In the retained normalized Hankel coordinates, keep


$$
\mu_{i+\nu}^{\langle26\rangle}
+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}^{\langle26\rangle}
=b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2,
\tag{8.4}
$$


and


$$
\boxed{
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
}
\tag{8.5}
$$


Thus the interior equations are


$$
\varepsilon_{i+1}
=-\varepsilon_i-\omega_i
-s_{\rm ret}3^{26}b_i^{\langle26\rangle},
\qquad i<\nu-1,
\tag{8.6}
$$


while the actual last equation is


$$
\boxed{
-\sum_{i=0}^{\nu-1}f_i\varepsilon_i
=
-\varepsilon_{\nu-1}-\omega_{\nu-1}
-s_{\rm ret}
\left(\theta+3^{26}b_{\nu-1}^{\langle26\rangle}\right).
}
\tag{8.7}
$$



No moment beyond $2\nu-2=D-4$ appears.

The unit coordinate transformations from turn11 preserve


$$
\varepsilon_i\equiv(-1)^i\pmod3.
\tag{8.8}
$$


Consequently, replacing $\varepsilon$ by $3^g\widetilde\varepsilon$ with integral $\widetilde\varepsilon$ is impossible for $g>0$.

For completeness, modulo $3$ the whole endpoint-return vector is


$$
\omega_i=0\quad(i<\nu-1),\qquad
\boxed{\omega_{\nu-1}=q_d(-1)\pmod3,}
\tag{8.9}
$$


where


$$
q_d(X)=X^\nu+\sum_{i=0}^{\nu-1}
\binom{D+\nu-i-1}{\nu-i}X^i.
$$


The terminal charge is therefore retained even when its particular residue happens to vanish.

---

## 9. Surviving precision losses

Removing the actual polynomial content does not remove the Christoffel Smith loss.

At the endpoint,


$$
\widetilde Z_{\rm src}(-1)
=\lambda_mP(-1)+\mu_mQ(-1),
\qquad v_3(\mu_m)=4,
$$


with $\lambda_m$ a unit on the stated branch. Recovering $Q(-1)\bmod3^K$ from these transformed data still requires the appropriate numerator modulo $3^{K+4}$.

For actual inverse transport, define


$$
\iota_E=\max\left\{0,-\min_{a,b}v_3((E_{\rm act}^{-1})_{ab})\right\}.
$$


In the retained LOW/HIGH normalization, the accepted block structure gives $\iota_E=1$. This value must not be transplanted to a differently row-scaled matrix without checking that scaling.

For an unscaled actual source, the sufficient bill for


$$
3^{6-g}WE_{\rm act}^{-1}T_R
$$


modulo $3^K$ is


$$
\boxed{
T_R\pmod{3^{g+K+\iota_E-6}},
}
\tag{9.1}
$$


when that exponent is positive. If subsequent Christoffel inversion is required, the sufficient exponent becomes


$$
\boxed{g+K+4+\iota_E-6.}
\tag{9.2}
$$



For the genuinely homogeneous projected channels in (4.5), one may first divide their source by the proved $3^g$. That removes $g$ from the bill. It does not remove either $4$ or $\iota_E$.

If the actual jet in (E.1) is nonzero, no such integral division is available for the original terminal mixed column.

---

## 10. A paid refinement beyond the first vanished endpoint residue

A finite-precision extension of the signed-minimum evaluator is available. It does not establish an infinite original-window realization.

Let


$$
U(N)=3^{-v_3(N!)}N!.
$$


For precision $3^K$, define


$$
G_K(a)=\prod_{\substack{1\le t\le a\\3\nmid t}}t
\pmod{3^K},
\qquad0\le a<3^K.
$$


The product of all units in a complete block of length $3^K$ is $-1$, so


$$
\boxed{
U(N)\equiv
\prod_{j\ge0}
(-1)^{\lfloor N/3^{j+K}\rfloor}
G_K\!\left(\lfloor N/3^j\rfloor\bmod3^K\right)
\pmod{3^K}.
}
\tag{10.1}
$$


This follows directly by removing the multiples of $3$ recursively from $N!$.

For an endpoint summand with $r=s-k$, the exact expression is


$$
(-1)^s3^{e_s(k)}
\frac{U(n)U(2s)}
{U(n-k)U(2k)U(s)U(r)}
\,2^{-r}.
\tag{10.2}
$$



### 10.1 State bound

Start with the sixteen carry/borrow states from turn18. Retain, in addition, the last $K-1$ digits of each of


$$
n-k,\qquad 2k,\qquad r.
$$


These buffers evaluate the length-$K$ windows in (10.1). Thus a sufficient combinatorial state bound is


$$
\boxed{16\,3^{3(K-1)}.}
\tag{10.3}
$$



For each state retain the minimum path cost and the next $K-1$ cost layers, with unit sums modulo $3^K$. A path more than $K-1$ above the minimum reaching the same state cannot contribute to the final result modulo $3^{r_s+K}$: every admissible suffix is also available to the lower-cost path.

All original terminal carries are imposed before flushing the final $K-1$ zero digits of the buffers. No extra Bernstein index is admitted.

This gives an exact evaluator for


$$
\boxed{3^{-r_s}J_s^{[A]}(-1)\pmod{3^K}.}
\tag{10.4}
$$


At $K=1$ it reduces to the accepted signed-minimum interface.

For the pair, restore the common content $g=\min(r_+,r_-)$. If the two outputs after division by $3^g$ first become nonzero at valuation $t<K$, then


$$
c_m=g+t
$$


and the primitive direction is determined modulo $3^{K-t}$.

If both outputs vanish modulo $3^K$, the conclusion is only $c_m\ge g+K$. No uniform precision bound follows.

This construction evaluates the actual original parameterization $m=2^{2j-1}$ when such an $m$ is supplied. It does not infer that an arbitrary finite-middle input occurs at infinitely many original window indices.

---

## 11. Concrete next lemma and the remaining bounded arithmetic

The immediate complete-source task is now smaller than an unspecified inverse contraction.

### Actual terminal-jet lemma

Determine


$$
\mathcal B(x)=\sum_{r=0}^{6}a_rx^r\pmod3
$$


for the actual $R_{\rm prod}$ on the retained original family.

* If $\mathcal B\ne0$, Theorem 6.1 proves that the original terminal mixed source has valuation exactly $1$; its $3^g$-normalization fails for $g\ge3$.
* If $\mathcal B=0$, the first obstruction vanishes, but only the conclusion $T_R\in9M$ has been obtained. One must evaluate the next **complete** layer, retaining the factorial term, all newly relevant lower poles, the terminal correction, and the actual inverse.

In the latter case, proving $T_R\in3^gM$ still requires enough layers for the actual, potentially growing $g$.

### Minimal new arithmetic input

No accepted endpoint computation, and no planned $m=241,\ldots,260$ content check, needs to be repeated.

For any specified actual producer instance, write


$$
R_{\rm prod}(x+1)=\sum_j r_jx^j.
$$


Only the eight residues


$$
\boxed{
r_{A-6},r_{A-5},\ldots,r_{A+1}\pmod3
}
\tag{11.1}
$$


are needed for the new first-layer test. Since


$$
R_{\rm prod}=R_{25}+3^{25}\Delta_{25},
$$


they may be read from the actual $R_{25}$ data; this use of $R_{25}$ is valid only for this first-layer test.

The reconstruction is


$$
r_{A-6+r}=2a_r+a_{r-1}\pmod3
\quad(0\le r\le6),\qquad a_{-1}=0,
$$


with the consistency check


$$
r_{A+1}=a_6.
\tag{11.2}
$$



**Expected verifiable output:**

1. the eight actual input residues;
2. the seven reconstructed $a_r$;
3. the seven mixed-force residues obtained from (E.1);
4. a declaration of whether $\mathcal B=0$;
5. if nonzero, a displayed actual source entry with valuation exactly $1$.

This is a bounded eight-coefficient extraction specification. Its cost depends on how the actual producer data are represented; I do not claim that an original-window producer has already been evaluated or that extracting these coefficients from an unspecified producer is free.

No finite computation is required to prove the matrix identity (E.1) or its invertibility.

---

## 12. Final primitive normalization and the whole error

None of the source normalizations above substitutes for actual row contents.

After the actual row contents, actual multiplier, and least actual clearer, retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the gcd over all primes


$$
\boxed{g_\ell=\gcd(|A_\ell|,|B_\ell|).}
$$


For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The exact same-index error remains


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
\tag{12.1}
$$



For the weighted producer, likewise retain


$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B,
$$


and


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
\tag{12.2}
$$



Selected-prime content and source divisibility determine neither final gcd. They also do not prove nonvanishing or decay of the whole error.

An irrationality proof would still require, for an infinite original sequence, a conclusion such as


$$
0<|q(e+\pi)-p|\longrightarrow0
$$


for the actual primitive integer pairs.

---

## 13. Proof-status ledger

| Statement | Status |
|---|---|
| Paid modulo-$81$ receipt | Accepted finite corroboration: 40 direct comparisons and 121 words |
| New full-content checks at $m=241,\ldots,260$ | Pending; no output assumed |
| Turn18 content and density theorems | Reused at their proved scopes |
| Complete-core versus pole-only-core distinction | Exact algebraic identity, §2 |
| Homogeneous normalization of projected Jacobi/Christoffel channels | Proved, §§4.1 |
| Identification of those channels with original primitive residual columns | False without additional nonintegral/affine transport; obstruction proved |
| Complete first mixed-force formula, including terminal HIGH correction | Proved, §5 |
| Seven-coordinate terminal detector and determinant $2$ | Proved, §6 |
| $T_R\in9M\iff R_{\rm prod}\in3\mathbb Z_3[y]$ | Proved on the stated original-window hypotheses |
| Actual value of the seven producer-jet coefficients | Not evaluated in the supplied data |
| $K_Z\in9M$ | Derived here |
| Stronger $K_Z\in3^9M$ | Reused at turn7’s stated window scope |
| Integral $3^g$-normalization of the original endpoint return | Ruled out by its unit residues |
| Higher paid endpoint evaluator with state bound $16\,3^{3(K-1)}$ | Derived; no finite run claimed |
| Actual primitive endpoint direction on an infinite original-window family | Unresolved |
| Actual all-prime denominator and whole nonzero error comparison | Unresolved |

## Conclusion

The complete-source question now has a concrete first obstruction, rather than only a warning about linearity:



$$
\boxed{
\text{the actual terminal mixed column detects the entire first producer jet by an invertible }7\times7\text{ map}.
}
$$



Its last coordinate depends on the original terminal HIGH return. The complete factorial and finite pole sum justify the calculation; neither was silently replaced by a leading-pole model.

Full Jacobi content does cancel from genuinely projected homogeneous Jacobi/Christoffel channels. It does **not** cancel from the original primitive affine residual columns or their unit endpoint forcing. If the actual first producer jet is nonzero, the proposed $3^g$-factor of the original mixed source fails decisively.

The next mathematical bottleneck is the actual eight-coefficient extraction (11.1), followed—if that layer vanishes—by complete higher-source evaluation at the precision demanded by $g$, the four-digit Christoffel loss, and the actual eliminated inverse.

Even after that local work, the actual all-prime primitive denominator must still be compared with the whole nonzero same-index error.



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$


