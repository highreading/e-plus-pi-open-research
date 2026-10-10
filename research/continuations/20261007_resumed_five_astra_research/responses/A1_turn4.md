> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete next-digit cancellation on the original index family

## Abstract

The coordinator’s degree exclusion is valid. In particular, the complete sensitivity introduced in A1 turn3 vanishes for every integral perturbation


$$
\mathscr R\longmapsto\mathscr R+27P,\qquad \deg P\le A+2.
$$


Thus the previously requested fourth divided-producer jet is unnecessary.

The next layer, $\mathscr R\mapsto\mathscr R+9P$, also cancels for the higher jet of the **actual producer**. This second assertion uses more than degree alone: it uses factorial saturation, endpoint divisibility, the complete corrected columns modulo $9$, and the actual LOW projection. The possible physical-terminal source is retained and cancels by the stated terminal isotropy and $B_d\equiv0\pmod3$.

Finally, a short multiplier argument using the already audited precision-$6$ **core-only** support theorem evaluates the remaining digit without computing the unknown lower producer coefficients. It proves


$$
\boxed{\mathcal Q\in3^6M_\nu(\mathbb Z_3),\qquad K_{18}=0.}
$$


Consequently, the radical of $K_{18}$ is the entire original residual space, and its nondegenerate complement has dimension zero.

These conclusions do not use the stronger width-$20$ or depth-$18$ assertions under review. They do not settle the determinant/cofactor problem, primitive arithmetic, or irrationality of $e+\pi$.

---

## 1. Domain, exact objects, and retained hypotheses

Throughout, the original domain is unchanged:


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1,\qquad A=n-2=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


with


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$


All uniform assertions below concern the sufficiently large retained tuples. In particular,


$$
v_3(A)=v_3(D)=5,\qquad D\ge486.
$$



The original finite coordinates are


$$
U_u=x^u\quad(0\le u<D),\qquad x=y-1,
$$




$$
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m),
$$


where


$$
d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1,\qquad d=D+\nu.
$$


Thus


$$
\deg z_i\le d-1,\qquad i+j\le D-4.
$$



The complete functional is


$$
\mathcal M(G)=
-\frac{3^h}{4}\mathfrak f(G)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](G-G(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^s)=(2s)!.
$$


Put


$$
\mathcal D(G)=\frac{G-G(-1)}{y+1}.
$$


This is an integral polynomial whenever $G$ is integral.

The complete core objects remain


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A,
$$




$$
W=[U\ Y],\qquad F=Z-WE_c^{-1}C_c.
$$


Write


$$
E_c=
\begin{pmatrix}
3L&3X\\
3X^T&E_{Y,c}
\end{pmatrix},
\qquad
\widehat E_c=E_{Y,c}-3X^TL^{-1}X.
$$


In this report, $L,X$ denote the **core** blocks. Their substitution for the actual blocks in $K_{18}$ is justified by A1 turn3’s inverse-replacement argument.

The audited results reused below are:

1. $L$ is integral and unimodular, and $E_c^{-1}\in3^{-1}M$.
2. The complete columns satisfy
   

$$
F_i\equiv z_i\pmod3.
$$


3. At the next precision,
   

$$
F_i\equiv z_i-3\pi(y^d)\tau_i\pmod9,
   \qquad \tau=e_{\nu-1},
$$


   where $\pi(y^d)$ is the complete lower-edge projected polynomial; in particular, its representative modulo $3$ has degree at most $d$.
4. The audited core support theorem applies at $p=r=6$, since $C_6<C_{16}$ and $h\ge8$ eventually.
5. The established complete quadratic theorem gives $\mathcal Q\in243M$, so $K_{18}=\mathcal Q/243\bmod3$ is already defined.
6. The stronger width-$20$ and depth-$18$ assertions are not assumed.

No closed producer calculation is repeated.

---

## 2. Audit of the complete functional at the first two precisions

The exact cutoff is


$$
4n-3=4H-4D+5.
$$


On the retained window,


$$
3H<4H-4D+5<9H.
$$


Among the retained odd denominators, the only one with valuation $h$ is $3H=3^h$. Its coefficient index is


$$
r_*=\frac{3H-1}{2}.
$$


The only denominator with valuation $h-1$ is $H$, with index


$$
r_1=\frac{H-1}{2}.
$$



The factorial contribution has valuation at least $h$ on integral polynomials. Therefore, eventually,


$$
\boxed{\mathcal M(G)\equiv[y^{r_*}]\mathcal D(G)\pmod3,}
\tag{2.1}
$$


and


$$
\boxed{
\mathcal M(G)\equiv
[y^{r_*}]\mathcal D(G)+3[y^{r_1}]\mathcal D(G)
\pmod9.}
\tag{2.2}
$$



These formulas result from reducing the **whole retained functional**, not from selecting poles before reduction.

Endpoint subtraction matters to the definition, but does not invalidate degree exclusion:


$$
\deg G\le r_*
\quad\Longrightarrow\quad
\deg\mathcal D(G)<r_*.
$$


Thus such a polynomial has $\mathcal M(G)\equiv0\pmod3$.

The functional is also integral on integral polynomial inputs: every retained denominator has valuation at most $h$. This integrality will preserve all polynomial congruences used below.

---

## 3. The $27P$ sensitivity vanishes

A1 turn3 defines


$$
O_i=
UL^{-1}a_i-\kappa\tau_i\bigl(Y_d-UL^{-1}X_d\bigr)
$$


and proves


$$
(\delta K_{18})_{ij}
=
\mathcal M\!\left(P(F_jO_i+F_iO_j)\right)\pmod3
\tag{3.1}
$$


under $\mathscr R\mapsto\mathscr R+27P$.

Every coefficient in $O_i$ is integral, and


$$
\deg O_i\le d,
$$


not merely $m$: the LOW part has degree at most $D-1$, and the only displayed HIGH polynomial is $Y_d$.

Using the complete-column congruence $F_i\equiv z_i\pmod3$, for $\deg P\le A+2$,


$$
\deg\!\left(P(F_jO_i+F_iO_j)\bmod3\right)
\le A+2+(d-1)+d
=H+2D-1.
$$


Moreover,


$$
H+2D-1<r_*
\quad\Longleftrightarrow\quad
4D-1<H,
$$


which follows amply from the original window. Equations (2.1) and (3.1) therefore give


$$
\boxed{\delta K_{18}=0.}
\tag{3.2}
$$



### Actual producer degree

The safe degree bound required here is $\deg\mathscr R\le A+2$. The supplied exact reset actually records cancellation of the $A+2$ coefficient of $R_{\rm prod}$: in A4 turn1,


$$
R_{\rm prod}=3\gamma Q_c+9J_2,\qquad
[y^{A+2}]J_2=-\gamma,
$$


while $[y^{A+2}]Q_c=3$. Hence that coefficient of $R_{\rm prod}$ is zero. The weaker bound $\le A+2$ is nevertheless retained throughout, so no subsequent argument depends on exploiting this extra cancellation.

Coefficientwise lifts of the lower producer digits can be chosen within the same degree bound.

### Conclusion



$$
\boxed{\text{Producer precision modulo }27\text{ is sufficient for }K_{18}.}
$$



The fourth-jet obligation in A1 turn3 is closed. No extra corrected-column support lemma is needed for that sensitivity.

---

## 4. The actual $9P$ layer: complete joint sensitivity

We now consider


$$
\mathscr R'=\mathscr R+9P.
$$


Define the complete sources


$$
t_U=\bigl(\mathcal M(PU_uF_i)\bigr)_{u,i},
\qquad
t_Y=\bigl(\mathcal M(PY_bF_i)\bigr)_{b,i},
$$


and


$$
c=t_Y-X^TL^{-1}t_U.
\tag{4.1}
$$


The source normalizations give exactly


$$
a'=a+t_U,\qquad B'=B+c.
\tag{4.2}
$$



### 4.1 Leading source and the physical terminal

Modulo $3$, degree exclusion gives $t_U=0$. In the HIGH source, the maximum possible degree of $PY_bz_i$ is $r_*+1$, attained only at


$$
b=m,\qquad i=\nu-1,\qquad \deg P=A+2.
$$


Thus


$$
t_Y\equiv\lambda e_m\tau^T\pmod3,
\qquad
\lambda=[y^{A+2}]P\bmod3.
\tag{4.3}
$$


Consequently,


$$
t_U=3s,\qquad c\equiv\lambda e_m\tau^T\pmod3.
\tag{4.4}
$$



The terminal charge is not deleted. Its contribution to the HIGH quadratic term is


$$
\delta(B^TRB)
=
\lambda\operatorname{Sym}_{\tau}(B_d)
+\lambda^2R_{mm}\tau\tau^T
=0\pmod3,
\tag{4.5}
$$


using precisely


$$
Re_m=e_d,\qquad R_{mm}=0,\qquad B_d\equiv0\pmod3.
$$


These statements concern the physical terminal $m$, not an extended HIGH space.

Also,


$$
\delta B_{d+1}=c_{d+1}=0\pmod3.
$$


Therefore the full surviving sensitivity is


$$
\boxed{
\delta K_{18}
=
s^TL^{-1}a+a^TL^{-1}s
-\kappa\operatorname{Sym}_{\tau}(c_d/3)
\pmod3.}
\tag{4.6}
$$


The core scalar $V_{c,dd}/3$ is unchanged. Actual-inverse changes remain beyond the precision, by the already proved replacement result.

Equation (4.6) retains both the lower pole and complete LOW feedback. Neither has yet been set to zero.

---

## 5. Why that third jet cancels for the actual producer

### 5.1 A sufficient actual third-jet support bound

The exact coefficient formulas and factorial saturation give


$$
[x^a]\mathscr R\equiv0\pmod{27}
\qquad(a\le A-13).
\tag{5.1}
$$


Indeed,


$$
v_3\!\left(\frac{(A+1)!}{(A-13)!}\right)
=5+v_3(12!)=5+5=10,
$$


and division by $3^7$ leaves valuation at least $3$.

Choose an integral lift of the established modulo-$9$ expression


$$
\mathscr R_0=(y+1)x^{A-6}
\left(\kappa x^6+3J(x)\right),
\qquad \deg J\le6.
$$


Then


$$
P=\frac{\mathscr R-\mathscr R_0}{9}
$$


is integral. The exact endpoint identity implies $P(-1)=0\pmod3$ eventually. Together with (5.1), this yields


$$
P\equiv(y+1)x^{A-12}p(x)\pmod3,
\qquad \deg p\le13.
\tag{5.2}
$$



By the already proved $27P$ invariance, changing the lift of $P\bmod3$ does not change $K_{18}$. We may therefore use the exact polynomial representative on the right of (5.2).

### 5.2 Evaluation of the LOW source divided by $3$

For LOW rows, the top extraction in (2.2) vanishes even after the complete modulo-$9$ correction to $F_i$. Its degree is at most


$$
A+2+(D-1)+d=H+d+1<r_*.
$$


At the lower pole only $F_i\bmod3=z_i$ is needed. Therefore


$$
\boxed{
s_{ui}=
[y^{r_1}]x^{H-12+u}p(x)y^i
\pmod3.}
\tag{5.3}
$$



If $u\ge12$, use


$$
x^H=(y-1)^H\equiv y^H-1\pmod3.
$$


The remaining factor has degree at most


$$
u-12+13+i\le d-1<r_1.
$$


Hence


$$
\boxed{s_{ui}=0\pmod3\qquad(u\ge12).}
\tag{5.4}
$$



The established source $a\bmod3$ is supported in rows $0,\ldots,5$. Since


$$
(L^{-1})_{uv}=0\pmod3\qquad(u+v<D-1),
$$


and


$$
11+5<D-1,
$$


we obtain


$$
\boxed{s^TL^{-1}a+a^TL^{-1}s=0\pmod3.}
\tag{5.5}
$$



### 5.3 Evaluation of the complete lower-edge feedback

Let


$$
y^d=r_d+x^Dq_d,\qquad \deg r_d<D,\qquad \deg q_d=\nu.
$$


The audited finite core projection gives


$$
UL^{-1}X_d\equiv r_d\pmod3.
\tag{5.6}
$$



At row $d$, the top extraction modulo $9$ again vanishes by degree, including the corrected-column term. Using (5.3) and (5.6),


$$
\frac{c_{di}}3
=
[y^{r_1}]
x^{H-12}p(x)y^i\bigl(y^d-r_d\bigr)
\pmod3.
$$


Thus


$$
\frac{c_{di}}3
=
[y^{r_1}]x^{H+D-12}p(x)y^iq_d
\pmod3.
\tag{5.7}
$$


After extracting $x^H$, the remaining polynomial has degree at most


$$
D-12+13+(\nu-1)+\nu=2D-2<r_1.
$$


The same $x^H\equiv y^H-1$ argument gives


$$
\boxed{c_d/3=0\pmod3.}
\tag{5.8}
$$



Combining (4.6), (5.5), and (5.8),


$$
\boxed{\delta K_{18}=0}
$$


for the actual third producer jet.

### Precision conclusion

For the actual producer family,


$$
\boxed{\mathscr R\bmod9\text{ is sufficient for }K_{18}.}
\tag{5.9}
$$


This is not an assertion about arbitrary degree-$(A+2)$ perturbations $9P$: the actual factorial and endpoint support in (5.2) is part of its hypothesis.

---

## 6. Direct evaluation of $V_{c,dd}/3$

This scalar can be evaluated independently of the producer.

Define the complete LOW-orthogonal boundary polynomial


$$
g_d=Y_d-UL^{-1}X_d.
$$


The exact Schur boundary identity is


$$
(\widehat E_c)_{dd}
=\mathcal M(Q_cg_d^2).
\tag{6.1}
$$



The finite monic-projection theorem gives, modulo $27$,


$$
g_d\equiv x^Dq_d,
\qquad \deg q_d=\nu.
$$


Consequently,


$$
(\widehat E_c)_{dd}
\equiv
\mathcal M\!\left((y+1)x^{H+D}(\beta+3y)q_d^2\right)
\pmod{27}.
\tag{6.2}
$$



Endpoint subtraction is exact here because the displayed polynomial contains $y+1$.

The quotient polynomial has degree at most


$$
H+D+1+2\nu=H+2D-1<r_*,
$$


so its top-pole contribution is zero.

For the remaining poles modulo $27$, $x^H\bmod27$ is supported on multiples of $H/9$. The other factor


$$
x^D(\beta+3y)q_d^2
$$


has degree at most $2D-1$. Every relevant lower pole lies on an odd half-grid relative to $H/9$, at distance at least


$$
\frac{H/9-1}{2}>2D-1
$$


from an integer-grid point. Hence every remaining extraction is zero.

It follows that


$$
(\widehat E_c)_{dd}\equiv0\pmod{27}.
\tag{6.3}
$$



The finite anti-triangular lift has $(K_0)_{dd}=0$. Since


$$
V_c=\frac{\widehat E_c-K_0}{3},
$$


we obtain the evaluated scalar


$$
\boxed{\frac{V_{c,dd}}3=0\pmod3.}
\tag{6.4}
$$



This is a complete boundary calculation. In particular, the lower-pole term and LOW projection have not been omitted.

---

## 7. Evaluation of the remaining digit without a producer calculation

The preceding sensitivity calculations reduce the necessary producer precision. They do not, by themselves, evaluate the lower-jet Gram term. The following argument does.

### 7.1 A short precision-$6$ producer representative

For $a\le A-19$,


$$
v_3\!\left(\frac{(A+1)!}{a!}\right)
\ge5+v_3(18!)=5+8=13.
$$


After the actual division by $3^7$,


$$
[x^a]\mathscr R\equiv0\pmod{3^6}.
$$


The exact endpoint identity is also zero modulo $3^6$ eventually. Therefore


$$
\boxed{
\mathscr R\equiv(y+1)x^{A-18}B(x)\pmod{3^6},
\qquad \deg B\le19.}
\tag{7.1}
$$


The degree $19$ deliberately allows the safe producer degree $A+2$.

No coefficient of $B$ needs to be computed.

### 7.2 Apply the audited core theorem only at precision $6$

Set


$$
\Omega=\frac H{3^5}.
$$


The established core theorem supplies integral representatives


$$
F_i\equiv x^D\psi_i\pmod{3^6},
$$


with


$$
\operatorname{supp}_y\psi_i\subseteq I_\Omega(3D),
\qquad
\deg\psi_i\le m-D.
\tag{7.2}
$$



The same two-neighbor interval argument from A4 turn1 gives


$$
\deg(x^D\psi_i)\le m-g_6,
\qquad
g_6=\frac{\Omega-9D+1}{2}.
$$


Since


$$
\Omega>512\cdot7^2D,
$$


we have $g_6>6$.

Put $b=\beta+3$, a $3$-adic unit, and


$$
T_6(x)=\sum_{a=0}^{5}\frac{(-3x)^a}{b^{a+1}}.
$$


Then


$$
(\beta+3y)T_6\equiv1\pmod{3^6}.
$$



Define


$$
H_i=x^{D-18}B(x)T_6(x)\psi_i(y).
\tag{7.3}
$$


These are integral polynomials because $D\ge486$. Their degrees satisfy


$$
\deg H_i\le m-g_6-18+19+5\le m.
$$


Thus they belong to the unchanged original polynomial space.

Equations (7.1)–(7.3) give


$$
\boxed{Q_cH_i-\mathscr RF_i\in3^6\mathbb Z_3[y].}
\tag{7.4}
$$



### 7.3 Convert the eliminated contraction into a core Gram

Let


$$
T=\bigl(\mathcal M(\mathscr R\,wF_i)\bigr)_{w,i}.
$$


Decompose the integral polynomials $H_i$ in the integral basis $[W,F]$:


$$
H=WC+FD.
$$


Complete orthogonality and (7.4) give


$$
T=E_cC+\Delta,\qquad \Delta\in3^6M.
$$


Therefore


$$
T^TE_c^{-1}T
=
C^TE_cC+C^T\Delta+\Delta^TC+\Delta^TE_c^{-1}\Delta.
$$


The final term has valuation at least $11$, including the paid inverse loss. Hence


$$
T^TE_c^{-1}T\equiv C^TE_cC\pmod{3^6}.
$$


Also,


$$
G_c(H,H)=C^TE_cC+D^TS_cD.
$$


The retained core divisibility makes the second term invisible here. Thus


$$
\boxed{
T^TE_c^{-1}T\equiv G_c(H,H)\pmod{3^6}.}
\tag{7.5}
$$



This is a finite-basis identity, not an infinite inverse approximation.

### 7.4 Every relevant pole of this Gram vanishes

Modulo $3^6$,


$$
Q_cH_iH_j
\equiv
(y+1)x^{H+D-36}B(x)^2T_6(x)\psi_i(y)\psi_j(y).
\tag{7.6}
$$


After removing $y+1$, write the quotient as


$$
x^H\,C(x)\,\psi_i(y)\psi_j(y),
\qquad
C(x)=x^{D-36}B(x)^2T_6(x).
$$


It is a polynomial, and


$$
\deg C\le D-36+38+5=D+7.
\tag{7.7}
$$



For evaluation modulo $3^5$:

* $x^H$ is supported on the $\Omega$-grid, since its modulo-$3^5$ support is on the coarser $H/3^4$-grid;
* $\psi_i\psi_j$ is supported within distance $6D$ of that grid;
* multiplication by $C$ enlarges the distance to at most $7D+7$.

Thus the quotient in (7.6) is supported in


$$
I_\Omega(7D+7)\pmod{3^5}.
\tag{7.8}
$$



Every retained denominator contributing modulo $3^5$ has the form


$$
2v+1=\alpha3^{h-k},\qquad 0\le k\le4,
$$


with $\alpha$ odd and prime to $3$. Because $H=3^5\Omega$,


$$
v=\frac{\alpha3^{6-k}\Omega-1}{2}.
$$


It is therefore an odd half-grid index relative to $\Omega$, whose distance from the integer grid is at least


$$
\frac{\Omega-1}{2}>7D+7.
\tag{7.9}
$$


Every extraction is zero. The factorial contribution is zero modulo $3^5$ because $h$ is sufficiently large.

Consequently,


$$
\boxed{G_c(H,H)\in3^5M.}
\tag{7.10}
$$


Equations (7.5) and (7.10) prove


$$
T^TE_c^{-1}T\in3^5M.
\tag{7.11}
$$



### 7.5 Return to the actual inverse and the original normalization

The perturbation satisfies


$$
E_{\rm act}-E_c\in3^7M,
$$


so


$$
E_{\rm act}^{-1}-E_c^{-1}\in3^5M.
$$


Moreover, the established source normalization gives $T\in3M$. Hence


$$
T^T(E_{\rm act}^{-1}-E_c^{-1})T\in3^7M.
$$


Thus (7.11) also holds with the actual inverse.

From


$$
T=3\binom{3a}{\beta_s},
$$


block elimination gives


$$
3T^TE_{\rm act}^{-1}T
=
81a^TL_{\rm act}^{-1}a+
27\widetilde\beta_s^{\,T}\widehat E_{\rm act}^{-1}\widetilde\beta_s
=\mathcal Q.
$$


All normalizing factors are therefore accounted for. We conclude


$$
\boxed{\mathcal Q\in3^6M_\nu(\mathbb Z_3).}
\tag{7.12}
$$



---

## 8. Evaluated digit, radical, and complement

The complete next digit is


$$
\boxed{K_{18}=\mathcal Q/243\bmod3=0.}
$$



Together with (6.4), this evaluates the assembled observation:


$$
\frac{a^TL^{-1}a}{3}+B^TRB
-\kappa\operatorname{Sym}_\tau
\left(\frac{B_d}{3}-B_{d+1}\right)
=0\pmod3.
$$


It does not assert that its separate summands vanish.

Since $K_{18}$ is the zero form on the original residual space,


$$
\boxed{\operatorname{rad}(K_{18})=\mathbb F_3^\nu.}
$$


Its nondegenerate complement is


$$
\boxed{\{0\},\qquad\text{dimension }0.}
$$



No new producer residues, including $\kappa$ or the $J_t$, are needed for this conclusion.

This result does **not** by itself establish a depth-$18$ normalization of the whole residual matrix: that normalization also depends on the separate core and linear terms.

---

## 9. What remains unchanged in the global construction

The complete actual columns remain


$$
\widehat Z^{\,\rm act}
=
\widehat Z^{\,c}-3^6WE_{\rm act}^{-1}T_R.
$$


Both exponential boundary columns, logarithmic forcing, exterior constants, and all finite returns remain present. In particular, the physical terminal closure is still


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$



The endpoint and diagonal observations remain


$$
e_{\rm act}=Z(-1)^T-C_{\rm act}^TE_{\rm act}^{-1}w,
\qquad
d_{\rm act}=w^TE_{\rm act}^{-1}w,
\qquad w=W(-1)^T,
$$


including the possible loss


$$
d_{\rm act}\in3^{-1}\mathbb Z_3.
$$



If the separately reviewed hypotheses justify


$$
\Upsilon_{18}=-S_{\rm act}/3^{18},
$$


the distinguished pair is still


$$
\mathcal D_0=\det\Upsilon_{18},
$$




$$
\mathcal D_1=
e_{\rm act}^T\operatorname{adj}(\Upsilon_{18})e_{\rm act}
-3^{18}d_{\rm act}\det\Upsilon_{18}.
$$


The vanishing of $K_{18}$ does not evaluate either member or establish their nonvanishing.

After the **actual** contents, actual multiplier, and least simultaneous clearer,


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


the final gcd is


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over **all primes**. For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole same-index error remains


$$
\boxed{
q(e+\pi)-p=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.}
$$



None of these actual contents, gcds, primitive denominators, or whole errors has been evaluated here.

---

## 10. Proof status and exact-arithmetic requirements

| Statement | Status |
|---|---|
| Complete $27P$ sensitivity vanishes for every $\deg P\le A+2$ | Proved |
| Producer precision modulo $27$ suffices | Proved |
| Actual third jet has the required width-$12$ representative | Proved from saturation and endpoint divisibility |
| Actual $9P$ sensitivity cancels, including terminal and LOW feedback | Proved |
| Actual producer precision modulo $9$ suffices for this digit | Proved |
| $V_{c,dd}/3=0\pmod3$ | Evaluated by complete boundary support |
| $\mathcal Q\in3^6M$, hence $K_{18}=0$ | Proved using audited precision-$6$ core support |
| Full radical and complement of $K_{18}$ | Evaluated: whole residual space and zero complement |
| Stronger width-$20$/depth-$18$ assumptions | Not used; remain separately reviewed |
| Distinguished determinant/cofactor nonvanishing | Open |
| Actual contents, least clearer, all-prime gcd, primitive denominator | Unevaluated |
| Whole nonzero error tending to zero at the same infinite original indices | Open |

### Bounded arithmetic

No new producer computation is needed. In particular, neither closed receipt nor the optional $452$-coordinate interface is requested.

The only small arithmetic checks used by the proof have bounded inputs


$$
12,\quad18,\quad C_6,\quad C_{16},
$$


and expected outputs


$$
v_3(12!)=5,\qquad v_3(18!)=8,\qquad C_6<C_{16},
$$


together with


$$
\Omega>512\cdot7^2D>14D+15.
$$


These are directly verifiable integer identities and inequalities; they are not finite experimental evidence for an infinite-family claim.

---

## Conclusion

The local next-digit obligation is closed:


$$
\boxed{
\begin{gathered}
\text{the fourth and higher producer layers are invisible;}\\
\text{the actual third producer layer cancels jointly;}\\
V_{c,dd}/3=0\pmod3;\\
\mathcal Q\in3^6M,\qquad K_{18}=0.
\end{gathered}}
$$



The decisive final step is not an unevaluated source pairing. It is an explicit finite multiplier construction followed by exclusion of **every** pole relevant to the required precision, using only the already audited precision-$6$ complete-core theorem.

The remaining bottleneck is now the next complete residual operator and its distinguished endpoint/diagonal pair, with a justified normalization and an actual relative nonvanishing argument. Beyond that remain the final all-prime primitive arithmetic and a proof, on the same infinite original indices, that


$$
0<|q(e+\pi)-p|\longrightarrow0.
$$





$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ is obtained.}}
$$


