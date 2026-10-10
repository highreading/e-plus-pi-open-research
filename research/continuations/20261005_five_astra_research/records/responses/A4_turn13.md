> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## A4 — the third saturation is again zero on a smaller infinite subclass

The modulo-$27$ core suffices. On the infinite subclass


$$
\boxed{\mathcal J^{(3)}
=\{j\in\mathcal J^{\ddagger}:D<H/36\},}
$$


the third actual saturation has rank zero. The potentially surviving mixed-block quadratic correction is **not** separately zero: it cancels the contribution inherited from the large HIGH Schur complement.

This calculation uses the supplied modulo-$27$ core and the established first-residue identification. It does not require a modulo-$81$ lift.

Throughout, put


$$
A=4^j-1,\quad H=3^{h-1},\quad D=H-A,\quad
d=\frac{3D}{2}-1,\quad \nu=\frac D2-1,\quad
m=\frac{A+1}{2},
$$


and use


$$
z_i=y^i(y-1)^D,\qquad 0\le i<\nu.
$$


The actual primitive scalar is denoted by


$$
\lambda=L_n/3\in\mathbb Z_3^\times.
$$


For the derivation I first remove $\lambda$, restoring it at the end.

### 1. The necessary modulo-$27$ Frobenius expansion

For $H=3^s$, $s\ge2$, write $K=H/9$. Then


$$
\boxed{
\begin{aligned}
(y-1)^H\equiv {}&
y^H-1
+9y^K-9y^{2K}+3y^{3K}+9y^{4K}\\
&-9y^{5K}-3y^{6K}+9y^{7K}-9y^{8K}
\pmod{27}.
\end{aligned}}
\tag{1}
$$



Here is a justification that includes the support restriction. For $0<r<H$,


$$
v_3\binom Hr=s-v_3(r),
$$


because


$$
\binom Hr=\frac Hr\binom{H-1}{r-1},
$$


and the second factor is a $3$-adic unit. Consequently only multiples of $H/9$ can survive modulo $27$. At those multiples, repeated use of the supplied prime-power binomial congruence reduces their coefficients to those of $(x-1)^9$ modulo $27$. Expanding that degree-nine polynomial gives (1).

Thus (1) is not merely the modulo-$9$ formula with another presumed cancellation appended.

### 2. Exact finite all-pole matrices

Let


$$
r_*=\frac{3H-1}{2},\qquad r_1=\frac{H-1}{2},
$$


and define the exact coefficient functional


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+\sum_{r=0}^{h}
\ \sum_{\substack{a\ge1\ {\rm odd}\\3\nmid a\\a3^r\le4n-3}}
3^{h-r}a^{-1}
[y^{(a3^r-1)/2}]
\frac{F(y)-F(-1)}{y+1}.
\tag{2}
$$


This retains the factorial term, endpoint subtraction, every admissible pole unit, and the complete cutoff.

Partition the exact matrix


$$
\bigl(\mathcal M(Q^{\rm loc}y^{a+b})\bigr)_{0\le a,b\le m}
=
\begin{pmatrix}
3L&3X\\
3X^T&E
\end{pmatrix}
\tag{3}
$$


at LOW indices $0,\ldots,d-1$ and HIGH indices $d,\ldots,m$. The actual first LOW Schur matrix, with $\lambda$ removed, is


$$
S=L-3XE^{-1}X^T.
\tag{4}
$$



For explicit computation modulo $27$, the LOW block is


$$
\begin{aligned}
L_{ab}\equiv {}&
[y^{r_1}]P(y)y^{a+b}\\
&+3\sum_{\substack{c\ {\rm odd},\,3\nmid c\\cH/3\le4n-3}}
c^{-1}[y^{(cH/3-1)/2}]P(y)y^{a+b}\\
&+9\sum_{\substack{c\ {\rm odd},\,3\nmid c\\cH/9\le4n-3}}
c^{-1}[y^{(cH/9-1)/2}]P(y)y^{a+b}
\pmod{27},
\end{aligned}
\tag{5}
$$


where


$$
P(y)=(y-1)^A(3y+10-9u),\qquad j=3u.
\tag{6}
$$


In the second and third lines only $P\bmod9$ and $P\bmod3$, respectively, are needed.

Formula (5) includes **all** $h-3$ units, rather than selecting only a few nearest poles. Lower pole depths carry a factor $27$. The factorial term also disappears at this precision on the stated large-index domain. There is no top-pole contribution to the LOW–LOW block, by degree.

The endpoint subtraction has not been replaced by an independently truncated expression: it is present in (2). Since


$$
Q^{\rm loc}-(y+1)P\in27\mathbb Z_3[y],
$$


division of the corresponding endpoint-subtracted difference by $y+1$ preserves divisibility by $27$.

### 3. The direct pole form annihilates the lifted radical modulo $27$

Let $Z$ have columns the coefficient vectors of the $z_i$. On $D<H/36$,


$$
\boxed{Z^TL\equiv0\pmod{27}.}
\tag{7}
$$



To prove this, multiply a radical vector by an arbitrary LOW monomial. Its contribution to (5) contains


$$
(y-1)^Az_i y^a
=y^{i+a}(y-1)^H,
\qquad
0\le i+a\le \nu+d-2=2D-4.
\tag{8}
$$



For the first pole, (1) has support on the $H/9$ grid. The index $r_1$ lies halfway between $4H/9$ and $5H/9$, apart from its $-1/2$ offset. Since


$$
2D-3<H/18,
$$


neither the shifts in (8) nor the extra factor $y$ in (6) can reach that index.

For the $h-2$ poles, the required expansion modulo $9$ has support on the $H/3$ grid. Each index


$$
(cH/3-1)/2
$$


with odd $c$ is halfway between consecutive grid points. The same degree bound excludes every such contribution.

For the $h-3$ poles, only $y^H-1$ remains modulo $3$. An index


$$
(cH/9-1)/2
$$


with odd $c$ is at least $(H/9-1)/2$ away from any potentially relevant multiple of $H$. Again (8) cannot reach it.

These arguments apply to every admissible pole unit. In particular,


$$
Z^TLZ\equiv0\pmod{27}.
\tag{9}
$$



The third saturation therefore comes entirely from the inherited unit eliminations.

### 4. The large HIGH correction to the required precision

Write


$$
V=Z^TX.
$$


Let $e$ denote the last standard vector in the $\nu$-dimensional radical coordinates, and let $e_m,e_d$ denote the indicated HIGH coordinate vectors. Put


$$
r_2=\frac{H/3-1}{2},\qquad
K_{ib}=\mathbf1_{i+b=r_2}
\quad(0\le i<\nu,\ d\le b\le m).
$$


Then


$$
\boxed{V\equiv-2ee_m^T+3K\pmod9.}
\tag{10}
$$



Indeed:

* the top pole contributes exactly $ee_m^T$, using the actual leading coefficient $3$ of $Q^{\rm loc}$;
* the first lower pole contributes $3K-3ee_m^T$;
* at the next pole depth, the $c=1$ and $c=7$ contributions cancel modulo $3$, and the other units cannot meet the coefficient range.

Thus the inherited top-pole corner has been retained.

Use the integral top-pole representative


$$
(E_0)_{ab}=[y^{r_*}](y-1)^Ay^{a+b},
\qquad d\le a,b\le m.
\tag{11}
$$


It is anti-triangular with anti-diagonal entries $1$, and, exactly,


$$
E_0^{-1}e_m=e_d,\qquad (E_0^{-1})_{mm}=0.
\tag{12}
$$


Write $E=E_0+3E_1$. Its first perturbation satisfies


$$
(E_1)_{dd}\equiv L_{dd}\pmod3.
\tag{13}
$$


The top-pole lift contributes nothing to this entry by degree; the $h-1$ pole supplies the displayed $L_{dd}$.

Expanding the inverse gives


$$
\frac{(E^{-1})_{mm}}3\equiv-L_{dd}\pmod3.
\tag{14}
$$


Furthermore,


$$
Ke_d=0,
\tag{15}
$$


because $i+d\le2D-3<r_2$. Equations (10)–(15) therefore yield


$$
\boxed{
-\frac{VE^{-1}V^T}{3}
\equiv L_{dd}\,ee^T\pmod3.
}
\tag{16}
$$



This is the contribution of the **actual large HIGH Schur correction** to $Z^TSZ/9$. It need not vanish separately.

### 5. The mixed-block correction cancels it exactly

Let $U$ consist of the LOW monomials $1,y,\ldots,y^{D-1}$, and put


$$
G=U^TSU,\qquad B=U^TSZ,\qquad C=Z^TSZ.
$$


The first residue-unit block $G$ has size $D$. The third actual saturation is


$$
T_3=\frac{C-B^TG^{-1}B}{9}\pmod3.
\tag{17}
$$



Define the finite coefficient vector


$$
l_a=\overline{L}_{a,d},\qquad 0\le a<D,
$$


and write


$$
G_0=(\overline L_{ab})_{0\le a,b<D}.
$$


By (7), (10), and (12),


$$
\frac B3\equiv-le^T\pmod3.
\tag{18}
$$


Combining (9), (16), and (18) gives the requested finite coefficient-matrix formula:


$$
\boxed{
T_3=
\left(\overline L_{dd}-l^TG_0^{-1}l\right)ee^T.
}
\tag{19}
$$



The scalar in (19) can be evaluated without leaving an unresolved inverse criterion. The first residue Hankel form $\overline L$ has rank $D$, and $G_0$ is its invertible $D$-square leading block. Its extension to the coordinate $y^d$ must therefore have zero Schur complement:


$$
\overline L_{dd}-l^TG_0^{-1}l=0.
\tag{20}
$$


Equivalently, the recurrence radical makes the coordinate $y^d$ congruent, for this bilinear form, to a polynomial of degree below $D$; pairing that identity with itself gives (20).

Consequently,


$$
\boxed{\operatorname{rank}_{\mathbb F_3}T_3=0
\qquad(j\in\mathcal J^{(3)}).}
\tag{21}
$$



For the actual primitive polynomial, every Schur form above is multiplied by $\lambda$. In particular, the actual expression in (19) is $\lambda$ times its right-hand side. The rank-zero conclusion is unchanged.

### 6. Actual endpoint image and infinitude

The transformations eliminating HIGH and then the first LOW unit block change a radical endpoint vector only by terms divisible by $3$. Hence its actual residue is still


$$
\boxed{
\overline e_{\rm rad}
=\bigl((-1)^i(-2)^D\bigr)_{0\le i<\nu}
=\bigl((-1)^i\bigr)_{0\le i<\nu}\ne0.
}
\tag{22}
$$


Since $T_3=0$,


$$
\boxed{\overline e_{\rm rad}\notin\operatorname{im}T_3.}
\tag{23}
$$



The subclass is infinite: choose a closed ratio interval strictly inside


$$
1<H/A<36/35.
$$


Irrational rotation by $\log_3 4$, also on any fixed progression $j\bmod9$ with $3\mid j$, gives infinitely many admissible indices in this interval. No particular value of $u\bmod3$ was needed for the cancellation.

### 7. Smith, gcd, and full-error consequences

After eliminating the first $D$ LOW unit coordinates, all $\nu$ remaining Smith factors are now divisible by $27$. Thus


$$
\boxed{
v_3(\det S)\ge3\nu,\qquad
v_3\!\left(\operatorname{adj}(S)_{00}\right)\ge3\nu-3.
}
\tag{24}
$$


Using the inherited complete-determinant normalization relation, the final-gcd bound strengthens to


$$
\boxed{
v_3(g)\ge d+3\nu=3D-4.
}
\tag{25}
$$


The identification of this $g$ with the complete coefficient-pair gcd remains the normalization dependency already used in the supplied source; (24) is the direct matrix consequence.

These are lower bounds, not exact valuations of the reduced denominator.

For the complete integer coefficient pair, retain


$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|),\quad
q=\frac{|B_{\rm det}|}{g},\quad
p=-\frac{\operatorname{sgn}(B_{\rm det})A_{\rm det}}g.
$$


On indices with $B_{\rm det}\ne0$, the whole evaluated error remains


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_{\rm det})}{g}
\bigl(A_{\rm det}+B_{\rm det}(e+\pi)\bigr)
=\frac{\operatorname{sgn}(B_{\rm det})\ell^k}{g}
\det H_{\rm complete}.
}
\tag{26}
$$


Endpoint nonvanishing in (22) does not independently prove $B_{\rm det}\ne0$, nor nonvanishing or decay of (26).

## Closing ledger

**(1) New result and proof status.**  
Using the supplied modulo-$27$ core and established first-residue structure, the third actual saturation is proved to have rank zero on the infinite subclass $D<H/36$. Its actual endpoint vector is nonzero and outside its image. The key new identity is (19): the HIGH correction and mixed LOW correction cancel by the already identified rank-$D$ recurrence form. This gives actual Smith bounds (24), and the stronger gcd bound (25) under the inherited normalization identity.

**(2) Exact remaining bottleneck.**  
A fourth saturation needs another actual digit and its inherited unit corrections. The cancellation proved here does **not** establish a recurrence in pole depth or justify geometric extrapolation. More globally, exact reduced-denominator control and nonzero whole primitive errors tending to zero remain unavailable; irrationality of $e+\pi$ is not decided.

**(3) Computation request.**  
None. The third-saturation rank and endpoint image above are evaluated symbolically; no finite rank scan or additional modulo-$81$ input is required for this result.
