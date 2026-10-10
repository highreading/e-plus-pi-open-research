> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the uniform second-digit obstruction and the raw endpoint modulo $9$

## Abstract and decisions

Both parent candidates **PASS at their stated local scope**.

The first candidate proves, on every sufficiently large index in the **original retained family**, that


$$
\dim_{\mathbb F_3}\ker\mathsf D\ge242,
$$


and consequently that the actual first endpoint-annihilator operator has nullity at least $241$. The formerly unclassified range is covered by a valid finite, ninth-power syzygy construction. Its selected source and target spaces, signs, shortened sector, and $241+1$ count are all correct.

The second candidate proves the stronger endpoint congruence


$$
\boxed{
f_{\alpha,\mathrm{new}}(a)
\equiv-2(-1)^{R_*}a(-1)\pmod9,
\qquad \deg a\le R,\quad \alpha=c,\mathrm{act}.
}
$$


This is a statement about the **actual corrected-column endpoint and its complete returns**, not a replacement by bare evaluation. It follows after paying the physical mixed inverse, the finite prefix lift, and both the $J$- and rank-$b$ endpoint returns.

In the specified same-label exact endpoint-adapted frames, it follows that


$$
f_{\alpha,\mathrm{new}}(g_s+g_{s+1})\in9\mathbb Z_3
$$


and


$$
\boxed{
T_{\mathrm{act},\mathrm{ann}}
-
T_{c,\mathrm{ann}}
\in3^7\operatorname{Mat}(\mathbb Z_3).
}
$$


Thus the higher-endpoint vector that was potentially active in Turn 8 is **zero modulo $3$ in these frames**. This does not evaluate the corresponding endpoint return in the different, unadapted monomial-complement frame.

There are also new directional consequences:

1. In all three already classified ranges, the leading endpoint-annihilator forcing is in the image of the leading annihilator matrix. I give explicit finite kernels, unit complements, and a particular solution.
2. In the formerly gray range, the leading directional question reduces sharply to one actual rectangular sector map. A finite proof gives a dichotomy:
   - either an endpoint-unit vector exists in the full second kernel and the leading directional equation is solvable;
   - or an explicitly constructible second-radical vector observes a **nonzero** leading forcing.
   
   The second alternative is proved using an exact $243$-sector signed cancellation, not an assumption about $W(-1)$.
3. In the classified ranges, the next physical $3^6$ matrix and the **paid next direction** reduce to specified core bilinear contractions. All four active core returns remain in those contractions.

These are local results. They prove neither final cofactor nonvanishing nor a gain in the actual primitive denominator. The rationality or irrationality of $e+\pi$ remains unresolved.

---

## 1. Scope, original indices, and finite objects

### 1.1 The original family is unchanged

All uniform assertions below concern sufficiently large members of exactly


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


subject to


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15},
$$


and the retained fixed subwindow


$$
\frac{103}{1000}<\frac{N_0}{P_0}<\frac{104}{1000}.
$$



Retain


$$
P_0=243P=3^{h-27},\qquad N_0=243r,\qquad D=P_0+N_0,
$$




$$
P=3^{h-32},\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$


and


$$
4^j=243(3^{26}-1)P-243r+1.
$$



Write


$$
x=y-1,\quad Q=27P,\quad b=Q-N_0,\quad R=\frac b2,\quad \chi=P-R.
$$


Then


$$
D+b=10Q,\qquad N_0=25P+2\chi,
$$


and the retained inequalities give


$$
.064<\frac bQ<.073,\qquad
.0145<\frac{\chi}{P}<.136.
\tag{1.1}
$$



No independent choice of $P,\chi,c,T$, or $r$ is used to establish a statement about this family.

### 1.2 Finite coordinates and the physical terminal

The coordinates remain


$$
U_s=x^s\quad(0\le s<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
\nu=\frac D2-1,\qquad
Y_t=y^t\quad(d\le t\le m),\qquad d=D+\nu,
$$


with $W=[U\ Y]$.

The physical HIGH terminal is $Y_m$, not $z_{\nu-1}$.

The prefix and tail boundaries are


$$
R_*=\frac{9Q+1}{2},\qquad a_0=R_*-1,\qquad
\tau=\frac{N_0-3}{2},
$$




$$
\ell=3R+1,\qquad
K=\{0,\ldots,\ell-1\},\qquad
J=\{\ell,\ldots,\tau-1\},
$$




$$
n_J=\frac{Q-4b-5}{2},\qquad R_*+\tau=\nu.
\tag{1.2}
$$


In particular, the actual last middle column remains in $J$.

The complete functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{K_{\mathrm{phys}}}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!,
$$


where


$$
K_{\mathrm{phys}}=2n-2=2H-2D+2
$$


and


$$
2K_{\mathrm{phys}}+1=4H-4D+5<3^{h+1}.
\tag{1.3}
$$


Thus $\mathcal M$ preserves coefficientwise $3$-adic integrality. No infinite pole sum is substituted for this finite functional.

### 1.3 Established inputs reused

The assignment accepts Turn 8’s physical matrix audit, including its finite-prefix proof completion and its actual finite $J$-border. I reuse that theorem, rather than repeat its pole-unit calculations.

The additional reused inputs, at their stated scope, are:

- integral corrected middle columns and
  

$$
E_\alpha^{-1}\in3^{-1}\operatorname{Mat}(\mathbb Z_3),
  \qquad \alpha=c,\mathrm{act};
$$


- the admitted finite $p=25$ filter and its coefficientwise congruence $R_N\equiv1\pmod9$;
- the complete whole-middle perturbation
  

$$
\delta S\in3^{29}\operatorname{Mat}(\mathbb Z_3);
$$


- the selected one-lift perturbation
  

$$
\delta S(p,\Psi[a])\in3^{33}\mathbb Z_3,
  \qquad \deg p<\nu,\quad\deg a\le R;
$$


- the selected mixed observation
  

$$
\mathcal B(W,\mathcal F[a])\in3^{25}M;
$$


- the exact core prefix lift
  

$$
X_c=3P_G+9Z;
$$


- the unit $J$- and rank-$b$ blocks, with
  

$$
L_c^TG_0\in3M,\qquad M_{b,c}\in3M;
$$


- the actual versions of these divisibilities proved by the complete producer comparison;
- the exact leading radical and saturated complement;
- the common-label raw comparison
  

$$
T_{\mathrm{act},\mathrm{red}}-T_{c,\mathrm{red}}\in3^7M.
  \tag{1.4}
$$



These inputs include the original terminal correction at $Y_m$. No compression theorem is newly extended to the last middle column.

---

# Part I. Audit of Candidate 1

## 2. Original arithmetic and the classified branches

Set


$$
\Pi=\frac P3,\qquad
\kappa=\frac{\Pi-1}{2},
$$




$$
\delta=\min\left\{\chi-1,\frac{P+3}{2}-3\chi\right\},
$$


and


$$
\mathsf D_{uv}
=[y^{\kappa-u-v}](1-y)^{2\chi},
\qquad 0\le u,v<\delta.
\tag{2.1}
$$



Here and throughout this report,


$$
\boxed{\chi=243c;}
$$


thus $c$ is not the differently named quotient of $2\chi$ appearing in one entry formula in Turn 8.

For sufficiently large original indices,


$$
\Pi=243T,\qquad T=3^{h-38},\qquad 9\mid T.
$$


Moreover


$$
c=\frac{r-75T}{2}.
$$


Since $r\equiv2\pmod9$, this proves


$$
\boxed{c\equiv1\pmod9.}
\tag{2.2}
$$


Also $T$ is odd and $T\equiv9\pmod{18}$.

Define


$$
B_1=2\chi+2\delta-1-\kappa,\qquad
\varepsilon=2\chi+\delta-\Pi.
\tag{2.3}
$$



### 2.1 Range I

If $B_1\le0$, the accepted finite anti-triangular analysis gives $\mathsf D=0$.

Both possible values of $\delta$ grow:


$$
\chi-1>\frac{29P}{2000}-1,
$$




$$
\frac{P+3}{2}-3\chi>\frac{23P}{250}+\frac32.
$$


Consequently $\delta\ge242$ eventually.

**Verdict: PASS.**

### 2.2 Range II

Suppose $0<B_1\le\delta$.

The upper branch for $\delta$ would give


$$
\varepsilon=\frac{\Pi+3}{2}-\chi
>\frac{23P}{750}+\frac32>0.
$$


But


$$
B_1-\delta=\varepsilon+\kappa,
$$


so this upper branch is impossible in Range II. Therefore


$$
\delta=\chi-1.
$$



The accepted rank formula then gives


$$
\operatorname{nullity}\mathsf D
=\delta-B_1
=\frac{\Pi-6\chi+3}{2}
=\frac{243(T-6c)+3}{2}.
\tag{2.4}
$$


Now


$$
T-6c\equiv3\pmod{18}.
$$


Nonnegativity of (2.4) excludes a negative value of $T-6c$. Hence $T-6c\ge3$, and


$$
\boxed{\operatorname{nullity}\mathsf D\ge366.}
$$



The potential equality $B_1=\delta$ is indeed excluded by the original low digits.

**Verdict: PASS.**

### 2.3 Range III

Suppose $\varepsilon>0$. The accepted complete kernel theorem gives


$$
\operatorname{nullity}\mathsf D=\varepsilon.
$$



On the lower branch,


$$
\varepsilon=243(3c-T)-1.
$$


Here $3c-T>0$ and $3c-T\equiv3\pmod9$, so


$$
\boxed{\varepsilon\ge728.}
$$



On the upper branch,


$$
\varepsilon=\frac{\Pi+3}{2}-\chi
>\frac{23P}{750}+\frac32,
$$


which exceeds $242$ for sufficiently large original indices.

**Verdict: PASS.**

These uses import the accepted ranks for the **current matrix** from Turn 8. They do not import an old rank formula for a different coefficient polynomial.

---

## 3. The gray range: a finite ninth-power syzygy

Assume


$$
B_1>\delta,\qquad \varepsilon\le0.
\tag{3.1}
$$


The upper branch is impossible by the preceding positive bound for $\varepsilon$. Thus


$$
\delta=\chi-1=243c-1.
\tag{3.2}
$$



The two inequalities in (3.1) imply


$$
6c>T,\qquad T\ge3c.
$$


Since


$$
6c-T\equiv15\pmod{18},
$$


we obtain the sharper original-arithmetic gap


$$
\boxed{6c-T\ge15.}
\tag{3.3}
$$



Write $c=9s+1$. Eventually $s\ge1$. Define


$$
A_s=\frac{T+9}{18},\qquad
B_s=\frac{8c-T+1}{18},\qquad
C_s=2s,\qquad d_0=3s.
\tag{3.4}
$$


These are integers, and


$$
A_s+B_s=4s+1,\qquad A_s+B_s+C_s=6s+1.
\tag{3.5}
$$



The required inequalities are exact:

- (3.3) gives $T\le54s-9$, hence $A_s\le3s$;
- $T\ge3c\ge2c+7$, since $c\ge10$, gives $B_s\le3s$;
- $C_s=2s\le3s$;
- all three exponents are positive.

Consider the finite homogeneous coefficient map in degree $d_0$,


$$
(U,V,W)\longmapsto
UX^{A_s}+VY^{B_s}+W(Y-X)^{C_s}.
\tag{3.6}
$$


Its source dimension is


$$
(d_0-A_s+1)+(d_0-B_s+1)+(d_0-C_s+1)
=d_0+2,
$$


whereas its target dimension is $d_0+1$. A nonzero syzygy therefore exists.

Its third component cannot vanish. Indeed, a nonzero relation between $X^{A_s}$ and $Y^{B_s}$ alone has total degree at least


$$
A_s+B_s=4s+1>d_0.
$$


Thus $W\ne0$, with homogeneous degree $s$.

Raise (3.6) to the ninth power in characteristic $3$, and multiply by $(Y-X)^2$. The resulting third coefficient is


$$
F=W^9\ne0,
\qquad \deg_{\mathrm{hom}}F=9s=c-1.
\tag{3.7}
$$


The total degree is


$$
9d_0+2=3c-1.
$$



The two required truncation pairs are


$$
a_{\mathrm{low}}=\frac{T+1}{2}=9A_s-4,
\qquad
b_{\mathrm{low}}=4c-a_{\mathrm{low}}=9B_s-1,
$$




$$
a_{\mathrm{high}}=\frac{T-1}{2}=9A_s-5,
\qquad
b_{\mathrm{high}}=4c-a_{\mathrm{high}}=9B_s,
\tag{3.8}
$$


and


$$
2c=9C_s+2.
$$


The first two terms of the powered syzygy are divisible by each respective pair $X^a,Y^b$. Therefore


$$
F(Y-X)^{2c}=0
$$


in both selected quotients.

### 3.1 Exact finite-map correspondence

For either pair in (3.8), the map is


$$
\left(\mathbb F_3[X,Y]/(X^a,Y^b)\right)_{c-1}
\xrightarrow{\;\cdot(Y-X)^{2c}\;}
\left(\mathbb F_3[X,Y]/(X^a,Y^b)\right)_{3c-1}.
\tag{3.9}
$$



Both $a,b$ exceed $c-1$. Thus the source is the full degree-$(c-1)$ homogeneous space; the nonzero polynomial $F$ is not killed by a source truncation.

If $S=a-1$, the surviving target $X$-exponents are exactly


$$
S-c+1,\ldots,S.
$$


Using source monomials $X^jY^{c-1-j}$ and target rows in descending exponent order, the matrix is


$$
[z^{S-i-j}](1-z)^{2c},\qquad 0\le i,j<c.
\tag{3.10}
$$


Thus the low block has $S=(T-1)/2$, and the high block has the one-step-lower index.

This verifies the selected finite boundaries directly.

No sign ambiguity is needed with the multiplier $Y-X$. If one instead traces the old unsigned-binomial convention, the relation is


$$
[z^{S-i-j}](1-z)^{2c}
=(-1)^S(-1)^i(-1)^j
\binom{2c}{S-i-j}.
$$


The row and column sign matrices are units. They preserve nonzero kernel dimension.

**Verdicts for Candidate 1’s displays (1) and (2): PASS.**

The degree equality in (3.7) is homogeneous. After dehomogenization, the degree can be smaller than $c-1$; that does not affect membership in the finite source space.

---

## 4. Exact sector lengths and the $241+1$ count

By Frobenius,


$$
(1-y)^{2\chi}=(1-y^{243})^{2c}
\quad\text{in }\mathbb F_3[y],
$$


and


$$
\kappa=243\frac{T-1}{2}+121.
\tag{4.1}
$$



Write $u=243i+\alpha$, $0\le\alpha<243$. Since the matrix dimension is $243c-1$, the sector lengths are


$$
n_\alpha=
\begin{cases}
c,&0\le\alpha\le241,\\
c-1,&\alpha=242.
\end{cases}
\tag{4.2}
$$



Only $\alpha+\beta=121$ or $364$ can occur.

- For $\alpha+\beta=121$, there are $122$ residue sectors, all of length $c$, with the low block (3.10).
- For $\alpha+\beta=364$, the residues $123,\ldots,241$ give $119$ equal sectors of length $c$, with the high block.
- The remaining pair is
  

$$
122\longleftrightarrow242,
$$


  of dimensions $c$ and $c-1$.

The common nonzero kernel vector from Section 3 can be placed independently in each of the $122+119=241$ equal source sectors. Their disjoint supports make the resulting vectors linearly independent.

The unequal pair has the exact form


$$
\begin{pmatrix}
0&C\\
C^T&0
\end{pmatrix},
\qquad C\in M_{c,c-1}(\mathbb F_3).
$$


Its rank is $2\operatorname{rank}C\le2(c-1)$, while its dimension is $2c-1$. It supplies at least one additional independent kernel vector.

Therefore, in the gray range,


$$
\boxed{\dim\ker\mathsf D\ge241+1=242.}
\tag{4.3}
$$



Together with Section 2, this proves the uniform assertion on **all sufficiently large original indices**.

For the actual endpoint hyperplane $H$, any $242$-dimensional subspace of $\ker\mathsf D$ meets $H$ in dimension at least $241$. Those vectors are in the radical of the restricted form. Hence


$$
\boxed{
\operatorname{nullity}
\left(\mathsf D|_H\right)\ge241.
}
\tag{4.4}
$$



The accepted actual endpoint and Turn 8’s physical transfer identify this restriction with the actual operator


$$
-\left(
[y^{\kappa-u-v}](1-y)^{2\chi}(1+y)^2
\right)_{0\le u,v\le\delta-2}.
$$



**Verdict for Candidate 1’s display (3), uniform conclusion, and endpoint conclusion: PASS.**

These are nullities over $\mathbb F_3$ of the indicated divided digit. They are not assertions that the complete $3$-adic matrix has an exact kernel of that dimension.

---

# Part II. Audit of Candidate 2

## 5. Why the exact endpoint is corrected-column evaluation

This normalization should be justified, not inferred merely from an alternating reduction.

Let $\mathcal L(y^t)=\mu_t$ be the original complete moment functional. Its recurrence is


$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\quad 0\le t\le2n-2.
\tag{5.1}
$$



For $\deg P\le2n-1$, write the exact finite division


$$
P=P(-1)+(y+1)Q.
$$


Then (5.1) gives


$$
\begin{aligned}
\mathcal L(P)
&=\mu_0P(-1)
+3^h\sum_{v=0}^{2n-2}\frac{[y^v]Q}{2v+1}
-\frac{3^h}{4}\mathfrak f((y+1)Q)\\
&=\left(\mu_0+\frac{3^h}{4}\right)P(-1)+\mathcal M(P).
\end{aligned}
\tag{5.2}
$$


The quotient has degree at most $2n-2$, exactly the physical cutoff.

Thus the distinguished rank-one functional in the complete moment decomposition is evaluation at $-1$. Eliminating $W$ in the core or actual Gram form transforms that functional by the same finite column correction. Consequently


$$
\boxed{
e_{\alpha,i}=F_{\alpha,i}(-1).
}
\tag{5.3}
$$



This also explains why the endpoint scaling cannot be changed independently of the complete border.

### 5.1 Conversion of the old producer notation

The old convention was


$$
Q_{\mathrm{act}}-Q_c=3^6R_{\mathrm{prod}},
$$


whereas the current convention is


$$
Q_{\mathrm{act}}-Q_c=3^7\mathscr R.
$$


Therefore


$$
\boxed{R_{\mathrm{prod}}=3\mathscr R.}
\tag{5.4}
$$



If


$$
\mathbf h_p=\mathcal B(W,F_c[p])
=\mathcal M(\mathscr R\,W F_c[p]),
$$


then the old mixed source is $T_R=3\mathbf h_p$. With the old divided first-source normalization $T_1=T_R/3$, the old formula


$$
-3^6T_1^T(3E_{\mathrm{act}}^{-1})W(-1)
$$


is exactly


$$
-3^7\mathbf h_p^TE_{\mathrm{act}}^{-1}W(-1).
$$



Independently of that notation, the current exact corrected-column identity is


$$
\boxed{
F_{\mathrm{act}}[p]-F_c[p]
=-3^7WE_{\mathrm{act}}^{-1}\mathcal B(W,F_c[p]).
}
\tag{5.5}
$$


It follows because $F_c[p]$ is exactly core-orthogonal to $W$.

The current all-middle mixed observation gives $\mathcal B(W,F_c[p])\in3M$. Together with the physical inverse cost $3^{-1}$, this yields an all-middle column difference in $3^7W$. For a selected one-lift input, the stronger mixed bound $3^{25}$ gives


$$
F_{\mathrm{act}}[\Psi]-F_c[\Psi]\in3^{31}W.
\tag{5.6}
$$



All coordinates of $W(-1)$ are integral:


$$
U_s(-1)=(-2)^s,\qquad Y_t(-1)=(-1)^t.
$$


Thus endpoint observation loses no further digit.

The old selected-source formula is not extrapolated to unselected columns. The all-middle statement used here comes from the current complete mixed observation.

---

## 6. The raw actual prefix lift

Let


$$
G_0a=x^ba,\qquad
P_Ga=x^by^{k_0}a,\qquad k_0=\frac{3Q+1}{2}.
$$


The exact normalized prefix lift is


$$
X_\alpha=-\mathsf A_\alpha^{-1}\mathsf B_{\alpha,K}G_0.
\tag{6.1}
$$


The source equality


$$
X_c=3P_G+9Z
\tag{6.2}
$$


has the correct sign.

The identity


$$
y^{R_*}x^ba+3x^by^{k_0}a
=x^by^{k_0}a(y^{3Q}+3)
\tag{6.3}
$$


is exact, since $R_*-k_0=3Q$.

Both components on the left are in their claimed finite spaces:

- $x^ba$ has degree at most $b+R=3R$, so it lies in the retained $K$-tail;
- $x^by^{k_0}a$ has degree at most
  

$$
\frac{3Q+3b+1}{2}<a_0,
$$


  so it is a genuine prefix vector.

The whole-middle perturbation gives


$$
\delta\mathsf A\in3^3M.
$$


By (6.3), the prefix-to-raw-tail perturbation is the selected one-lift perturbation, in $3^{33}$, minus $3$ times an ordinary perturbation, in $3^{29}$. It is therefore in $3^{30}$ before normalization, so


$$
\delta(\mathsf B_KG_0)\in3^4M.
$$



The exact difference identity is


$$
X_{\mathrm{act}}-X_c
=-\mathsf A_{\mathrm{act}}^{-1}
\left(\delta(\mathsf B_KG_0)+\delta\mathsf A\,X_c\right).
\tag{6.4}
$$


The normalized actual inverse is integral, and $X_c\in3M$. Hence


$$
X_{\mathrm{act}}-X_c\in3^4M.
$$


In particular,


$$
\boxed{
X_{\mathrm{act}}=3P_G+9Z_{\mathrm{act}},
\qquad Z_{\mathrm{act}}\in M.
}
\tag{6.5}
$$


In fact $Z_{\mathrm{act}}-Z\in9M$, though that stronger fact is unnecessary for the modulo-$9$ endpoint.

**Verdicts for Candidate 2’s (1) and (2): PASS.**

---

## 7. Physical one-lift endpoint evaluation

For $\deg a\le R$, put


$$
\Psi[a]=x^{D+b}y^{k_0}a(y)(y^{3Q}+3).
$$


Its middle input has maximum degree


$$
p_{\max}=\frac{9Q+3b+1}{2},
$$


and


$$
\nu-32-p_{\max}=\frac{Q-4b-67}{2}>0
$$


for sufficiently large original indices.

Therefore the admitted $p=25$ certificate applies with


$$
N=3^{24},\qquad L=81Q.
$$


It gives


$$
F_c[\Psi]-\Psi R_N(y^L)\in3^{25}W.
\tag{7.1}
$$


The trial has the paid positive physical gap below $m$; no clipping or overflow term is used here.

The filter fact is coefficientwise:


$$
R_N(Y)\equiv1\pmod9.
$$


Since $R_N$ is a finite integral polynomial, substitution $Y=(-1)^L=-1$ is legitimate and preserves that modulus. This is not evaluation of an infinite formal series at a unit.

At $y=-1$,


$$
(-1)^{3Q}+3=2,
$$


and


$$
(-2)^{D+b}=(-2)^{10Q}\equiv1\pmod9,
$$


because $10Q$ is divisible by $6$. Also $R_*-k_0=3Q$ is odd, so


$$
(-1)^{k_0}=-(-1)^{R_*}.
$$


Thus (7.1), (5.6), and integral endpoint observation prove


$$
\boxed{
F_\alpha[\Psi[a]](-1)
\equiv-2(-1)^{R_*}a(-1)\pmod9,
\quad \alpha=c,\mathrm{act}.
}
\tag{7.2}
$$



The actual producer has not been replaced by its core at unproved precision: the actual/core column difference was paid at $31$ digits before evaluation.

**Verdict for Candidate 2’s (3): PASS.**

---

## 8. Complete prefix, $J$, and rank-$b$ endpoint returns

The exact first-prefix endpoint is


$$
f_{\alpha,K}
=e_{\alpha,\mathrm{tail}}
-\mathsf B_{\alpha,K}^T\mathsf A_\alpha^{-1}
e_{\alpha,\mathrm{prefix}}.
$$


Using $X_\alpha$ and corrected-column linearity,


$$
\begin{aligned}
G_0^Tf_{\alpha,K}
&=G_0^Te_{\alpha,\mathrm{tail}}+
X_\alpha^Te_{\alpha,\mathrm{prefix}}\\
&=F_\alpha[\Psi](-1)+9Z_\alpha^Te_{\alpha,\mathrm{prefix}}.
\end{aligned}
\tag{8.1}
$$


This confirms the **plus** sign in the lifted endpoint.

Next retain the entire $J$-return:


$$
f_\alpha^{(2)}
=f_{\alpha,K}-3L_\alpha B_{\alpha}^{-1}f_{\alpha,J}.
\tag{8.2}
$$


The established original terminal theorem and its paid actual transfer give


$$
L_\alpha^TG_0\in3M.
$$


The normalized $J$-inverse and $f_{\alpha,J}$ are integral. Therefore the contracted correction in (8.2) belongs to $9M$.

This reasoning retains the whole finite $J$-block, including its last middle column. It does not evaluate that last endpoint coupling or set the $J$-return equal to zero.

Finally,


$$
f_{\alpha,\mathrm{new}}
=G_0^Tf_\alpha^{(2)}
-3M_{b,\alpha}^TA_{b,\alpha}^{-1}f_{\alpha,b}.
\tag{8.3}
$$


The actual and core matrices $M_{b,\alpha}$ lie in $3M$, and the normalized rank-$b$ inverse and $f_{\alpha,b}$ are integral. This last endpoint correction also belongs to $9M$.

Combining (7.2), (8.1), (8.2), and (8.3) proves


$$
\boxed{
f_{\alpha,\mathrm{new}}(a)
\equiv-2(-1)^{R_*}a(-1)\pmod9
}
\tag{8.4}
$$


for every amplitude $a\in\mathbb Z_3[y]$ of degree at most $R$.

**Verdict for Candidate 2’s (4): PASS.**

For


$$
g_s=(1-y)^{2\chi}y^s,\qquad
h_s=g_s+g_{s+1},
$$


the polynomial $h_s$ has an exact factor $1+y$. Hence


$$
\boxed{f_{\alpha,\mathrm{new}}(h_s)\in9\mathbb Z_3.}
\tag{8.5}
$$



**Verdict for Candidate 2’s (5): PASS.**

---

## 9. Exact endpoint adaptation and synchronized frames

Write


$$
T_\alpha=T_{\alpha,\mathrm{red}},\qquad
K_\alpha=T_\alpha/81,
$$


and let $\mathscr G$ be the fixed integer matrix with columns


$$
g_{L_*+u},\qquad L_*=\frac{P-1}{2},\qquad 0\le u<\delta.
$$



Let $E=E_{\mathcal C}$ be the same original monomial leading complement for both matrices. Fix the same integer pivot $g_{L_*}$, and put


$$
u_\alpha=f_{\alpha,\mathrm{new}}(g_{L_*}),\qquad
v_\alpha=\frac{g_{L_*}}{u_\alpha}.
$$


These are unit normalizations. Indeed, since $2\chi$ is divisible by $6$,


$$
2^{2\chi}\equiv1\pmod9,
$$


and therefore


$$
u_\alpha\equiv-2(-1)^{R_*+L_*}\pmod9.
\tag{9.1}
$$



Adapt only the complementary and annihilator columns, retaining the normalized pivot:


$$
V_{\alpha,i}
=E_i-v_\alpha f_{\alpha,\mathrm{new}}(E_i),
$$




$$
h_{\alpha,u}^{\,f}
=h_u-v_\alpha f_{\alpha,\mathrm{new}}(h_u).
\tag{9.2}
$$


Then


$$
f_\alpha(V_{\alpha,i})=0,\qquad
f_\alpha(h_{\alpha,u}^{\,f})=0.
$$



The complement remains unit at physical order $3^4$, since the subtracted pivot lies in its leading radical. Its cross with the retained radical is in $3^5M$. Thus its physical inverse costs $3^{-4}$, its displacement is in $3M$, and its matrix return begins in $3^6M$.

Because its endpoint is **exactly zero**, this complement makes no new endpoint or complete-diagonal return.

By (8.5),


$$
h_{\alpha,u}^{\,f}-h_u\in9\,\mathbb Z_3v_\alpha.
$$


The retained radical matrix begins at $3^5$. Hence this adjacent-sum endpoint correction changes it only in $3^7M$. Both physical digits $3^5$ and $3^6$ are protected from this correction.

### 9.1 Actual/core comparison

Equation (8.4) holds on the entire amplitude lattice. Therefore the two raw endpoint functionals, their pivot endpoints, and their normalized pivot coefficients agree modulo $9$. The two adapted complements differ by $9$ times the same leading-radical pivot.

Pairing such a difference with any original amplitude costs at least $3^5$, so:

- the complementary physical blocks differ in $3^7M$;
- the complementary-to-radical cross blocks differ in $3^7M$;
- the direct retained blocks differ in $3^7M$.

For their Schur returns:

- a cross change contributes at least $7-4+5=8$ digits;
- an inverse change has valuation at least $-4+7-4=-1$, and contributes at least $5-1+5=9$ digits.

The direct difference remains in $3^7M$. The subsequent adjacent-sum endpoint adaptations also alter the matrices only in $3^7M$. Thus


$$
\boxed{
T_{\mathrm{act},\mathrm{ann}}-T_{c,\mathrm{ann}}\in3^7M.
}
\tag{9.3}
$$



**Verdict for Candidate 2’s (6): PASS.**

This comparison concerns the specified same-label adapted matrices. It does not synchronize arbitrary monomial and endpoint-adapted frames, and it does not assert a comparison of their complete diagonal parameters.

### 9.2 The monomial-frame endpoint is a different quantity

In the unadapted monomial frame, write


$$
A=E^TK_\alpha E,\qquad
C_1=\frac{E^TK_\alpha\mathscr G}{3},\qquad
e=f_\alpha(E).
$$


Eliminating $E$ changes the radical endpoint by


$$
f_{\mathrm{mon}}
=f_\alpha(\mathscr G)-3C_1^TA^{-1}e.
$$


Consequently


$$
\boxed{
\frac{f_{\mathrm{mon}}(\mathsf N)}3
\equiv-\mathsf N^T\overline C_1^{\,T}\overline A^{-1}\overline e
\pmod3,
}
\tag{9.4}
$$


where $\mathsf N$ is the adjacent-sum matrix.

The right side has not been evaluated and need not vanish. Candidate 2 correctly avoids claiming otherwise. Equation (9.4) is the precise return that would invalidate an attempt to carry (8.5) into the different monomial-complement frame without transformation.

---

# Part III. New directional consequences

## 10. The actual $3^6$ formula after the endpoint synchronization

Work first in either raw amplitude frame. Put


$$
M=\frac{\mathscr G^TT\mathscr G}{3^5},\qquad
M_0=\overline M=-\mathsf D.
$$


Let $p$ be the coordinate vector of the normalized pivot:


$$
p=\frac{e_0}{f(g_{L_*})}.
$$


The new endpoint theorem determines $p\bmod9$. If


$$
\sigma=(-1)^{R_*+L_*}\in\{1,-1\},
$$


then


$$
p\equiv4\sigma e_0\pmod9,
\qquad \overline p=\sigma^{-1}e_0.
\tag{10.1}
$$



The higher endpoint vector from Turn 8 is now evaluated:


$$
t=\frac{f(\mathscr G\mathsf N)}3\equiv0\pmod3.
\tag{10.2}
$$



Define


$$
Q_f=(\overline C_1-\overline e\,\overline p^{\,T}M_0)\mathsf N,
\qquad
q_f=(\overline C_1-\overline e\,\overline p^{\,T}M_0)\overline p.
$$


Then the complete endpoint-adapted complement calculation gives


$$
\boxed{
\frac{S_{\mathrm{ann}}}{3^5}
\equiv
\mathsf N^TM\mathsf N
-3Q_f^T\overline A^{-1}Q_f
\pmod9,
}
\tag{10.3}
$$


and its actual pivot direction is


$$
\boxed{
\frac{r^\circ}{3^5}
\equiv
\mathsf N^TMp
-3Q_f^T\overline A^{-1}q_f
\pmod9.
}
\tag{10.4}
$$



The formerly open $t$-term is absent for a proved reason. The complementary matrix and directional returns remain.

There is also an original-source zero:


$$
\mathsf D_{00}=0.
\tag{10.5}
$$


Indeed, the coefficient polynomial is supported only at multiples of $243$, whereas $\kappa\equiv121\pmod{243}$. Hence


$$
\overline p^{\,T}M_0\overline p=0,
\qquad q_f=\overline C_1\overline p.
\tag{10.6}
$$


In particular,


$$
\boxed{a^\circ\in3^6\mathbb Z_3.}
\tag{10.7}
$$



The leading direction is


$$
r_0=-\sigma^{-1}\mathsf N^T\mathsf D e_0.
\tag{10.8}
$$


Its entries are explicitly the coefficients of $(1-y)^{2\chi}(1+y)$ at $\kappa-u$, multiplied by $-\sigma^{-1}$. They can be nonzero only for


$$
u\equiv120,\ 121\pmod{243}.
$$


Their values are given by the finite ternary-digit binomial rule. This is the actual direction in the specified frame.

---

## 11. A solved leading directional equation in Ranges I–III

Let


$$
B_0=-\mathsf N^T\mathsf D\mathsf N.
\tag{11.1}
$$


The leading equation is


$$
B_0z=r_0.
\tag{11.2}
$$



The polynomial-coordinate map $\mathsf N$ is multiplication by $1+y$:


$$
\mathbb F_3[y]_{\le\delta-2}
\longrightarrow
\mathbb F_3[y]_{\le\delta-1}.
$$


It is injective and its image is precisely the evaluation hyperplane at $-1$. No last coefficient is discarded.

### 11.1 Range I

Here $\mathsf D=0$. Thus


$$
B_0=0,\qquad r_0=0.
$$


Its complete kernel has dimension $\delta-1$, and $z=0$ solves (11.2).

### 11.2 Range II

Put


$$
k=\delta-B_1\ge366.
$$


The complete kernel of $\mathsf D$ is


$$
\operatorname{span}\{e_0,\ldots,e_{k-1}\}.
$$


In particular $e_0\in\ker\mathsf D$, so


$$
r_0=0.
$$



The complete annihilator kernel, in adjacent-sum coordinates, is


$$
\boxed{
\ker B_0=\operatorname{span}\{e_0,\ldots,e_{k-2}\}.
}
\tag{11.3}
$$


The remaining monomials are a unit complement. Thus


$$
\operatorname{nullity}B_0=k-1,\qquad
\operatorname{rank}B_0=B_1,
$$


and $z=0$ again solves (11.2).

### 11.3 Range III

Put


$$
d_1=\Pi-2\chi,\qquad w(y)=(1-y)^{d_1}.
$$


The accepted full kernel is


$$
\ker\mathsf D
=w(y)\,\mathbb F_3[y]_{\le\varepsilon-1}.
$$


Here $d_1>0$, and


$$
w(-1)=2^{d_1}\ne0.
$$


Therefore evaluation at $-1$ is nonzero on this kernel.

It follows that


$$
\boxed{
\ker B_0
=w(y)\,\mathbb F_3[y]_{\le\varepsilon-2}.
}
\tag{11.4}
$$


The displayed basis $w(y)y^v$, $0\le v\le\varepsilon-2$, has a triangular initial coefficient block with diagonal $1$. It is saturated. Monomials of degrees


$$
\varepsilon-1,\ldots,\delta-2
$$


form a unit complement. In particular,


$$
\operatorname{nullity}B_0=\varepsilon-1,\qquad
\operatorname{rank}B_0=d_1.
$$



An explicit particular solution of (11.2) is


$$
\boxed{
z_0(y)=
\frac{1-w(y)/w(-1)}{\sigma(1+y)}.
}
\tag{11.5}
$$


The numerator vanishes at $-1$, so this is an actual finite polynomial. Moreover


$$
\mathsf N z_0
=\sigma^{-1}\left(e_0-\frac{w}{w(-1)}\right),
$$


and $\mathsf D w=0$, which proves $B_0z_0=r_0$.

For a particular solution in the stated monomial unit complement, define


$$
z_C
=z_0-w\left[\frac{z_0}{w}\right]_{<\varepsilon-1}.
\tag{11.6}
$$


The bracket means only the finite initial coefficient truncation. It is not an evaluation of $w^{-1}$ at $-1$. The first $\varepsilon-1$ coefficients of $z_C$ vanish, and the subtracted term belongs to $\ker B_0$. Thus $z_C$ lies in the specified complement and still solves (11.2).

This closes the leading directional equation throughout Ranges I–III, with exact finite representatives.

---

## 12. A sharper gray-range directional lemma

The nullity construction alone does not determine the direction in the gray range. Nevertheless, the actual sector structure gives a useful exact reduction that does **not** require $W(-1)\ne0$.

Put


$$
S=\frac{T-1}{2},
$$


and define the two actual equal-sector matrices


$$
(H_0)_{ij}=[z^{S-i-j}](1-z)^{2c},
$$




$$
(H_1)_{ij}=[z^{S-1-i-j}](1-z)^{2c},
\qquad 0\le i,j<c.
$$


Let


$$
\boxed{
C_{\mathrm{rect}}=(H_1)_{\{0,\ldots,c-1\},\{0,\ldots,c-2\}}.
}
\tag{12.1}
$$


This is exactly the $c$-by-$(c-1)$ block of the unequal pair $122\leftrightarrow242$.

Let


$$
a_c=(1,-1,\ldots,(-1)^{c-1})^T,
\qquad
a_{c-1}=(1,-1,\ldots,(-1)^{c-2})^T.
$$



### Theorem 12.1 — Exact gray-range direction dichotomy

On every original gray-range index:

1. If
   

$$
a_c\notin\operatorname{im}C_{\mathrm{rect}},
   \tag{12.2}
$$


   then evaluation is nonzero on $\ker\mathsf D$, and $B_0z=r_0$ is solvable.
2. If
   

$$
C_{\mathrm{rect}}t=a_c
   \tag{12.3}
$$


   is solvable, then there is an explicitly constructible $w_*$ such that
   

$$
\mathsf D w_*=e,\qquad e^Tw_*=0,
$$


   where $e_u=(-1)^u$. Its adjacent-sum preimage is in $\ker B_0$ and observes the forcing by the nonzero value $-\sigma^{-1}$. Consequently $r_0\notin\operatorname{im}B_0$.

#### Proof

First suppose (12.3) holds. Put


$$
q=(t_0,\ldots,t_{c-2},0)^T,\qquad
v=(0,t_0,\ldots,t_{c-2})^T.
$$


The exact one-step shift gives


$$
H_1q=a_c,\qquad H_0v=a_c.
\tag{12.4}
$$


Also, by symmetry of $H_1$,


$$
C_{\mathrm{rect}}^Tq=a_{c-1}.
\tag{12.5}
$$



Set


$$
\beta=a_{c-1}^Tt.
$$


Then


$$
a_c^Tq=\beta,\qquad a_c^Tv=-\beta.
\tag{12.6}
$$



In sector $\alpha$, evaluation is $(-1)^\alpha a_{n_\alpha}$, because $243$ is odd. Use (12.4) to solve all equal-sector equations for $\mathsf D w_*=e$, and use $q,t$ for the unequal pair.

For every low sector, the partner residue sum is $121$, which is odd. Its evaluation contribution is therefore


$$
(-1)^{121}a_c^Tv=\beta.
$$


There are $122$ such sectors.

For every equal high sector, the residue sum is $364$, which is even, so its contribution is $\beta$. There are $119$ such sectors.

The unequal pair contributes $2\beta$. Hence


$$
e^Tw_*=(122+119+2)\beta=243\beta=0
\quad\text{in }\mathbb F_3.
\tag{12.7}
$$



This proves the asserted construction.

Conversely, if $e\in\operatorname{im}\mathsf D$, its equation in the length-$c$ sector $122$ is necessarily $C_{\mathrm{rect}}t=a_c$. Thus


$$
\boxed{
e\in\operatorname{im}\mathsf D
\quad\Longleftrightarrow\quad
a_c\in\operatorname{im}C_{\mathrm{rect}}.
}
\tag{12.8}
$$



If (12.2) holds, finite linear algebra supplies $\ell$ with


$$
C_{\mathrm{rect}}^T\ell=0,\qquad a_c^T\ell=1.
$$


Placing $\ell$ in sector $122$ and zero elsewhere gives $k\in\ker\mathsf D$ with $e^Tk=1$. Then


$$
z=\frac{e_0-k}{\sigma(1+y)}
$$


is a finite polynomial solution of $B_0z=r_0$.

If (12.3) holds, (12.7) gives $w_*=\mathsf N z_*$ for a unique finite $z_*$. Since $\mathsf D w_*=e$ and $\mathsf N^Te=0$,


$$
B_0z_*=0.
$$


But


$$
z_*^Tr_0
=-\sigma^{-1}w_*^T\mathsf D e_0
=-\sigma^{-1}e^Te_0
=-\sigma^{-1}\ne0.
$$


Thus $r_0$ cannot lie in $\operatorname{im}B_0$. ∎

### 12.1 Consequences and exact open part

Writing $k_D=\dim\ker\mathsf D$, the theorem also proves:

- under (12.2),
  

$$
\dim\ker B_0=k_D-1;
$$


- under (12.3),
  

$$
\dim\ker B_0=k_D+1.
$$



Thus, in the second case, the candidate’s lower bound strengthens to


$$
\dim\ker B_0\ge243,
$$


and the leading forcing on that kernel is nonzero.

What is **not** proved is which alternative holds uniformly on the original gray-range indices. The exact remaining premise for such a claim is a proof of membership or nonmembership in (12.3) for the original $c,T$. A finite diagnostic at one pair does not establish that premise.

The second alternative does not rule out a later paid solve allowing an additional factor $3^{-1}$. It is not a disproof of eventual directional or primitive-denominator success.

---

## 13. The next physical $3^6$ obligation, including its direction

This section gives a concrete continuation beyond the previous unknown list.

In Ranges I–III, Section 11 supplies the **complete** leading annihilator kernel. Let $Z_2$ be its stated integer lift and $V_2$ the stated monomial unit complement. Set


$$
S=S_{\mathrm{ann}},\qquad r=r^\circ.
$$


Then


$$
A_2=\frac{V_2^TSV_2}{3^5}
$$


is a unit matrix, and


$$
C_2=\frac{V_2^TSZ_2}{3^6}
$$


is integral.

Because the leading direction kills the complete second radical,


$$
\frac{Z_2^Tr}{3^6}
$$


is integral. The exact next directional return is


$$
\boxed{
\rho_2
=
Z_2^Tr
-
3^6C_2^TA_2^{-1}
\left(\frac{V_2^Tr}{3^5}\right).
}
\tag{13.1}
$$


It is active at physical order $3^6$ in general.

By contrast, the corresponding matrix return is


$$
3^7C_2^TA_2^{-1}C_2,
\tag{13.2}
$$


and is invisible at physical $3^6$.

In Ranges I and II, the leading direction is identically zero. Therefore the return in (13.1) is itself invisible at $3^6$. In Range III it must be retained.

### 13.1 All four active core returns

Define the complete contracted core pairing


$$
\mathcal P
=\mathscr G^T G_c(\mathcal F,\mathcal F)\mathscr G.
$$


Retain the four integral return matrices


$$
R_{\mathrm{pref}}
=\frac{\mathscr G^TZ^T\mathsf A Z\mathscr G}{9},
$$




$$
R_J
=\frac{\mathscr L^TB_c^{-1}\mathscr L}{3},
\qquad
\mathscr L=\frac{L_c^TG_0\mathscr G}{3},
$$




$$
R_b
=
\left(\frac{M_{b,c}\mathscr G}{3}\right)^T
A_{b,c}^{-1}
\left(\frac{M_{b,c}\mathscr G}{3}\right),
$$




$$
R_C=C_1^TA_c^{-1}C_1.
\tag{13.3}
$$


Their integrality is precisely what the preceding audits paid. Their reductions modulo $3$ have not all been evaluated.

The exact matrix after the first **monomial matrix** complement has divided radical form


$$
\boxed{
\widehat M_c
=
-\frac{\mathcal P}{3^{31}}
-3(R_{\mathrm{pref}}+R_J+R_b+R_C).
}
\tag{13.4}
$$


This use of the monomial Schur matrix does not use its different endpoint or diagonal.

### 13.2 A concrete core bilinear reduction for the actual next direction

Take the complement-supported solution $z_C$ from Section 11; in Ranges I and II take $z_C=0$. Choose any integral lift in that same finite complement. Let


$$
K_2=\mathsf N Z_2,\qquad
k=p-\mathsf N z_C.
\tag{13.5}
$$


Modulo $3$,


$$
\mathsf D K_2=0,\qquad \mathsf D k=0.
$$


The endpoint of $k$ is the normalized unit endpoint.

On these vectors, the endpoint-adapted complementary cross reduces to the ordinary $C_1$-cross: the extra term contains $M_0K_2$ or $M_0k$, both zero. Equations (10.3)–(10.4), together with the exact directional return (13.1), therefore give


$$
\boxed{
\frac{Z_2^TSZ_2}{3^6}
\equiv
\frac{K_2^T\widehat M_cK_2}{3}
\pmod3,
}
\tag{13.6}
$$


and


$$
\boxed{
\frac{\rho_2}{3^6}
\equiv
\frac{K_2^T\widehat M_ck}{3}
\pmod3.
}
\tag{13.7}
$$



The division in (13.7) is paid by $\mathsf Dk=0$ and the leading directional solve. It incorporates the physical $3^{-5}$ complementary directional return; it is not merely the unreturned vector $Z_2^Tr/3^6$.

Substituting (13.4), the two exact next targets are


$$
\boxed{
-\frac{K_2^T\mathcal P K_2}{3^{32}}
-K_2^T(R_{\mathrm{pref}}+R_J+R_b+R_C)K_2
\pmod3,
}
\tag{13.8}
$$


and


$$
\boxed{
-\frac{K_2^T\mathcal P k}{3^{32}}
-K_2^T(R_{\mathrm{pref}}+R_J+R_b+R_C)k
\pmod3.
}
\tag{13.9}
$$



These formulas specify a narrower original obligation than an unrestricted next matrix calculation:

- the raw higher endpoint is already evaluated and disappears;
- the different monomial endpoint return is avoidable by exact adaptation;
- the core matrix return $R_C$ is **not** avoidable;
- the next directional return is retained through the explicit solution $z_C$;
- only the indicated bilinear contractions are needed for this next layer in the classified ranges.

The remaining evaluations in (13.8)–(13.9) are open. In particular, the moment pairing must be controlled through modulus $3^{33}$, and the four integral returns in (13.3) must be evaluated at their now-active residues. A name for these expressions is not a proof that they vanish.

---

## 14. The complete bordered diagonal remains present

For the actual objects, retain


$$
\lambda^{\mathrm{pref}}
=3^{26}d_{\mathrm{act}}
-e_C^T\mathsf A^{-1}e_C,
$$




$$
\lambda^{(2)}
=\lambda^{\mathrm{pref}}
-\frac13 f_J^TB_{\mathrm{act}}^{-1}f_J,
$$


and


$$
\boxed{
\lambda_{\mathrm{new}}
=\lambda^{(2)}
-\frac19 f_b^TA_{b,\mathrm{act}}^{-1}f_b.
}
\tag{14.1}
$$


The associated endpoint returns are exactly those in (8.2)–(8.3).

The admitted integrality of $\lambda^{\mathrm{pref}}$, and integral normalized observations and inverses, give


$$
\lambda_{\mathrm{new}}\in3^{-2}\mathbb Z_3.
\tag{14.2}
$$


No unit residue for $\lambda_{\mathrm{new}}$ is inferred.

The endpoint-adapted first complement has endpoint zero, so it makes **no new** diagonal return. The complete remaining border is


$$
\begin{pmatrix}
\lambda_{\mathrm{new}}&1&0\\
1&a^\circ&(r^\circ)^T\\
0&r^\circ&S_{\mathrm{ann}}
\end{pmatrix}.
$$


Its exact two-coordinate Schur return is


$$
\boxed{
S^\sharp
=
S_{\mathrm{ann}}
+
\frac{\lambda_{\mathrm{new}}}
{1-\lambda_{\mathrm{new}}a^\circ}
r^\circ(r^\circ)^T.
}
\tag{14.3}
$$



By (10.7) and (14.2),


$$
1-\lambda_{\mathrm{new}}a^\circ\in1+3^4\mathbb Z_3,
$$


and the correction in (14.3) is in $3^8M$. Hence it cannot affect either physical digit $3^5$ or $3^6$.

This is why the exact value of the prior diagonal numerator can be deferred at this layer. It has not been erased.

By contrast, the unadapted monomial complement would make the additional return


$$
-\frac1{81}e^TA^{-1}e.
$$


That diagonal belongs to a different frame and cannot be inserted into (14.3) without the corresponding exact transformations.

---

## 15. Assertion-by-assertion audit ledger

### Candidate 1

| Assertion | Verdict | Reason |
|---|---|---|
| Section 1: original $\chi=243c$, $c\equiv1\pmod9$, $\Pi=243T$ and physical transfer | **PASS** | Derived from the original arithmetic; Turn 8’s accepted physical theorem discharges the candidate’s former audit condition |
| Section 2: Range I bound | **PASS** | Both branches of $\delta$ grow |
| Section 2: Range II bound $366$ | **PASS** | Exact nullity and $T-6c\equiv3\pmod{18}$ |
| Section 2: Range III bounds | **PASS** | Lower bound $728$ on the lower branch; positive linear growth on the upper branch |
| Display (1): $6c-T\ge15$ | **PASS** | Exact gray-range inequalities and original low digits |
| Display (2): common ninth-power kernel coefficient | **PASS** | Finite dimension count, nonzero third component, exact source degree and truncations |
| Section 3: selected maps and signs | **PASS** | Both target intervals verified; signed multiplier gives the actual blocks directly |
| Section 4: sector lengths and $241+1$ count | **PASS** | Includes the shortened sector $242$ and the unequal pair |
| Display (3): uniform nullity at least $242$ | **PASS** | Uniform finite proof, not finite extrapolation |
| Endpoint-annihilator nullity at least $241$ | **PASS** | Intersection bound; no assumption about $W(-1)$ |
| Section 5: only immediate unitness is excluded | **PASS** | No directional or primitive-$q$ conclusion follows from nullity alone |

### Candidate 2

| Numbered assertion | Verdict | Reason |
|---|---|---|
| (1) $X_c=3P_G+9Z$ | **PASS** | Exact accepted finite prefix identity, with the correct sign |
| (2) $X_{\mathrm{act}}=3P_G+9Z_{\mathrm{act}}$ | **PASS** | Selected $3^{33}$, ordinary $3^{29}$, and unit-prefix inverse payments |
| (3) one-lift corrected endpoint modulo $9$ | **PASS** | Physical $p=25$ representative, coefficientwise filter reduction, $31$-digit actual transport, and exact signs |
| (4) full raw endpoint on every amplitude modulo $9$ | **PASS** | Complete prefix, $J$, and rank-$b$ returns retained and paid |
| (5) $f_{\alpha,\mathrm{new}}(h_s)\in9$ | **PASS** | Exact $1+y$ factor; remains valid after endpoint-kernel complement elimination |
| (6) separately adapted actual/core matrices agree in $3^7$ | **PASS** | Same-label adaptations differ by $9$ times a radical pivot; all physical inverse costs included |

The following stronger statements remain **CONDITIONAL**, with precise missing premises:

- A uniform answer to the gray-range leading directional question requires a uniform original-index determination of
  

$$
a_c\in\operatorname{im}C_{\mathrm{rect}}.
$$


- An evaluated next physical $3^6$ matrix and direction require the core residues in (13.8)–(13.9).
- A normalization $\lambda_{\mathrm{new}}=\eta/3$ with specified unit $\eta$ requires the actual quadratic numerator from (14.1); matrix synchronization does not supply it.
- Primitive-denominator saving and irrationality require the same-index global nonvanishing and whole-error estimates stated below.

---

## 16. Complete producer, forcing, and arithmetic normalization

The producer remains


$$
Q_{\mathrm{act}}=3P_n=Q_c+3^7\mathscr R,
\qquad
Q_c=(y+1)x^A(\beta+3y),\quad \beta=-71-A.
$$


Its complete coefficients are


$$
[x^a](3^7\mathscr R)
=-\frac{(n-1)!}{a!}(t_a+\xi v_a),
\qquad 0\le a\le n-1,
$$


with


$$
t=
3nh_{\mathrm{vec}}
+(b_{\mathrm{force}}+6)e_{n-1}
+\frac{2b_{\mathrm{force}}}{n-1}e_{n-2},
\qquad b_{\mathrm{force}}=-n-66.
\tag{16.1}
$$


Here the original definitions


$$
u_a=\frac{(n-1)!(-2)^a}{a!},\qquad v=T_n^{-1}u,
$$




$$
h_{\mathrm{vec}}
=T_n^{-1}\left(\binom{n+a}{a}\gamma_{n+a}\right)_{a=0}^{n-1},
$$




$$
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},
\quad
\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1},
\quad \gamma_0=1,\ \gamma_1=0
$$


and the complete signed normalization of $\xi$ are unchanged.

In particular,


$$
\mathscr R(-1)
=-\frac{\xi((n-1)!)^2}{3^7}
$$


is not set to zero. Neither terminal coordinate of $t$, nor any term of $\xi v$, is suppressed.

The complete original return remains


$$
\boxed{
J^T\varepsilon+\omega
=
-\varepsilon-s_{\mathrm{ret}}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
}
\tag{16.2}
$$


The recurrence (5.1) retains its genuine resonance division at


$$
t_*=\frac{3^h-5}{2}.
$$



All local adaptations used in this report are $3$-adic operations inside the original finite spaces. They do not redefine the actual integer column contents or the least simultaneous clearer $\ell_{\mathrm{clr}}$.

Retain the original integers


$$
A_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_1,
$$


and the gcd over **all primes**


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


For $B_\ell\ne0$, the actual primitive pair is


$$
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
\qquad
q=\frac{|B_\ell|}{g_\ell}.
$$



The whole evaluated error remains exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\mathrm{clr}}^{m+1}}
{g_\ell}\det H_{\mathrm{complete}}.
}
\tag{16.3}
$$



An irrationality proof would follow from, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad \det H_{\mathrm{complete}}\ne0,
$$


and


$$
\boxed{
\log g_\ell-(m+1)\log\ell_{\mathrm{clr}}
-\log|\det H_{\mathrm{complete}}|
\longrightarrow+\infty.
}
\tag{16.4}
$$


Indeed, these hypotheses make the nonzero whole errors tend to zero, whereas rationality $e+\pi=a/b$ would make every nonzero such error have absolute value at least $1/b$.

This is a conditional implication. None of the local nullity or endpoint results proves its hypotheses.

---

## 17. Exact follow-on lemma and bounded certificates

### 17.1 Next original proof obligation

A concrete continuation is now:

> **Original second-radical core-and-direction lemma.**  
> On the original indices, evaluate the bilinear residues (13.8) and (13.9), using the complete corrected pairing through modulus $3^{33}$, all four returns in (13.3), and the stated finite second-radical basis and unit complement.  
> In the gray range, first determine the exact rectangular alternative (12.2)–(12.3), and retain the resulting nonzero forcing when the second alternative occurs. Then establish the required actual directional divisibility through the remaining singular layers.

This obligation no longer includes an unevaluated raw endpoint modulo $9$. It still includes the original direction and the complete physical returns.

### 17.2 Bounded exact arithmetic

No tool computation was performed. The already run $T=81,\ c=10,19,28$ receipt is not repeated and is not used as a uniform proof.

No new numerical computation is needed for either PASS verdict.

If a coordinator wishes to inspect the new directional sign cancellation separately, a fully bounded optional receipt has:

- **Inputs:** residues $\alpha=0,\ldots,242$, partner
  

$$
\pi(\alpha)\equiv121-\alpha\pmod{243},
$$


  the special shortened residue $242$, and arithmetic modulo $3$.
- **Expected verifiable output:** $122$ low equal sectors, $119$ high equal sectors, the two orientations of $122\leftrightarrow242$, the low sign $(-1)^{121}=-1$, the high sign $(-1)^{364}=1$, and
  

$$
122+119+2=243\equiv0\pmod3.
$$


  
This verifies only the finite routing and scalar count used in (12.7).

For a **separately certified single original tuple**, the gray-range directional test also has an exact finite certificate format:

- **Inputs:** its actual $c,T$, the matrix $C_{\mathrm{rect}}$ of size $c\times(c-1)$ from (12.1), and $a_c$. Each entry is obtained by the finite ternary-digit rule for the specified coefficient.
- **Expected output, exactly one of two alternatives:**
  

$$
t\in\mathbb F_3^{c-1},\qquad C_{\mathrm{rect}}t=a_c,
$$


  or
  

$$
\ell\in\mathbb F_3^c,\qquad
  C_{\mathrm{rect}}^T\ell=0,\qquad a_c^T\ell=1.
$$


- **Verification bound:** the displayed finite matrix and vector products, with all entries in $\{0,1,2\}$.

No new original tuple is selected here. Such a certificate would decide only that supplied tuple; it would not establish a uniform original-index theorem.

---

## Conclusion

Both candidates survive independent audit.

The new proved local conclusions are:



$$
\boxed{
\dim\ker\mathsf D\ge242,\qquad
\dim\ker B_0\ge241
}
$$


on all sufficiently large original retained indices, and


$$
\boxed{
f_{\alpha,\mathrm{new}}(a)
\equiv-2(-1)^{R_*}a(-1)\pmod9
}
$$


for every original amplitude, for both core and actual objects. In the specified exact endpoint-adapted frames,


$$
\boxed{
T_{\mathrm{act},\mathrm{ann}}-T_{c,\mathrm{ann}}\in3^7M.
}
$$



The stronger directional advance is an explicit leading solve in Ranges I–III and an exact rectangular-map dichotomy in the gray range. The latter supplies a concrete nonzero forcing certificate when its membership alternative holds, without assuming a value of $W(-1)$.

The remaining local bottleneck is the evaluated physical $3^6$ core matrix **and its paid original direction**, with all four active returns retained. The remaining global bottleneck is same-index nonvanishing and decay of the **whole** error after the actual contents, least simultaneous clearer, all-prime gcd, and primitive denominator.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ is obtained.}}
$$


