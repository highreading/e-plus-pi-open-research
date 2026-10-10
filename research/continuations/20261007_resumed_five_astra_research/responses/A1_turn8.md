> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact sector ranks and endpoint restrictions in the adjacent depth-$26$ window

## Abstract

The selected-degree graded-algebra realization proposed in the assignment is correct. Its specialization to the **original** ternary word gives exact ranks, not merely a singularity criterion.

Retain the original indices and put


$$
s=\frac D{486},\qquad P=3^{h-32},\qquad r=2s-P.
$$


In the adjacent window


$$
\frac{147968}{59049}<\frac{\Omega}{D}<3,
\qquad \Omega=\frac H{3^{25}},
$$


the original congruences imply, for sufficiently large retained tuples,


$$
0<r<\frac P5,\qquad r\equiv2\pmod9,\qquad r\ \text{odd};
$$


in particular, $r\ge11$.

For the two equal-sector blocks, the exact syzygy gaps and nullities are


$$
\begin{array}{c|c|c}
T&\text{syzygy gap}&\dim\ker B_s(T)\\ \hline
c'&r-1&(r-1)/2\\
c'-1&r+1&(r+1)/2.
\end{array}
$$


The unequal $s\times(s-1)$ block has rank $(P-1)/2$, right nullity $(r-1)/2$, and left nullity $(r+1)/2$.

These evaluations assemble particularly simply in the **unchanged original residual coordinates**. Define


$$
R_*=\frac{243P+1}{2}
     =\frac{\Omega/3+1}{2}.
$$


For the explicit candidate matrix


$$
K_{ij}=-[y^{c-i-j}](y-1)^D,\qquad 0\le i,j<\nu,
$$


one obtains


$$
\boxed{\operatorname{rank}_{\mathbb F_3}K=R_*},
$$


and


$$
\boxed{
\ker K=\operatorname{span}_{\mathbb F_3}
\{e_{R_*},e_{R_*+1},\ldots,e_{\nu-1}\}.
}
$$


Thus


$$
\boxed{
\dim\ker K=\tau=\frac{243r-3}{2}
=\frac{D-\Omega/3-3}{2}.
}
$$


The prescribed endpoint $\bar e_i=(-1)^i$ is nonzero on this radical, and its kernel there is described explicitly below.

The growth conclusion is more precise than either alternative in a simple “linear or bounded” dichotomy. Nullities are linear in $s$ on every fixed closed subwindow below $3$. There is no uniform positive linear lower bound throughout the entire open window, because original indices can approach its upper edge. Nevertheless, a standard fixed-logarithm lower bound rules out an infinite original subfamily with bounded nullity.

All these are unconditional statements about the explicit candidate $K$. Their application to the actual normalized residual remains conditional on the depth-$26$ transport hypotheses being independently audited. The next actual Schur digit, the relative cofactor valuation, and the nonzero whole-error comparison remain open.

---

## 1. Original objects and proof scope

Retain exactly


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1,\qquad A=4^j-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


and


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



The finite coordinates remain


$$
U_u=(y-1)^u\quad(0\le u<D),
$$




$$
z_i=(y-1)^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m),
$$


where


$$
\nu=\frac D2-1,\qquad d=D+\nu.
$$


The physical terminal is still $Y_m$.

The complete functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!,
$$


with the unchanged cutoff


$$
2v+1\le4H-4D+5.
$$



Write


$$
\Omega=\frac H{3^{25}},\qquad c=\frac{\Omega-1}{2}.
$$


The matrix evaluated in this report is the explicit finite matrix


$$
K_{ij}=-[y^{c-i-j}](y-1)^D,\qquad 0\le i,j<\nu,
\tag{1.1}
$$


over $\mathbb F_3$.

### What is reused, and what remains conditional

The following established parts of A1 turn7 are reused without repeating its determinant-product calculation:

* $D=486s$, with $s\equiv1\pmod9$ on the original progression;
* $c'=(3^{h-31}-1)/2\equiv4\pmod9$ for sufficiently large $h$;
* the exact $243$-sector decomposition, including the shortened sector $242$;
* infinite original scope of every fixed open subinterval of the adjacent real window.

The actual-block receipt supplies


$$
E_{\rm act}-E_c=3^7J.
$$


It does **not** by itself establish the stronger linear perturbation estimate needed to identify the actual depth-$26$ digit. Accordingly, the implication


$$
U=-S_{\rm act}/3^{26}\in M_\nu(\mathbb Z_3),
\qquad \bar U=K
\tag{1.2}
$$


is retained only at its stated conditional scope. The independent review of the corrected-column support theorem and of


$$
\Phi_R\in3^{21}M
$$


is not pre-empted here.

The general syzygy-gap method is established mathematics. The new work below is the selected-map identification, its original-word specialization, and the exact endpoint application.

---

## 2. The original high ternary digit

Set


$$
\kappa_0=\frac{147968}{59049},\qquad
\rho=\frac{\Omega}{D},
$$


and restrict only to the assigned adjacent subwindow


$$
\kappa_0<\rho<3.
\tag{2.1}
$$



Define


$$
P=3^{h-32},\qquad r=2s-P.
\tag{2.2}
$$


Then


$$
\Omega=729P,\qquad D=486s=243(P+r),
$$


so


$$
\rho=\frac{3P}{P+r},
\qquad
\frac rP=\frac3\rho-1.
\tag{2.3}
$$



Since $\kappa_0>5/2$, equation (2.3) gives


$$
0<r<\frac P5.
\tag{2.4}
$$


For sufficiently large $h$, $P\equiv0\pmod9$. Therefore the retained original congruence $s\equiv1\pmod9$ gives


$$
r=2s-P\equiv2\pmod9.
\tag{2.5}
$$


Moreover, $P$ is odd, so $r$ is odd. The least positive odd integer congruent to $2\pmod9$ is $11$. Hence


$$
\boxed{r\ge11.}
\tag{2.6}
$$



These are constraints on the original integer $r$, not freely selectable ternary digits. Its exact defining relation is


$$
\boxed{
4^j=243(3^{26}-1)P-243r+1.
}
\tag{2.7}
$$


All lower ternary digits of $r$ remain those imposed by this equation and by the original progression.

Finally,


$$
c'=\frac{3P-1}{2}.
\tag{2.8}
$$


Thus the two selected values of $T$ are most conveniently parameterized by


$$
T_\epsilon=\frac{3P+\epsilon}{2}-1,
\qquad \epsilon\in\{1,-1\},
\tag{2.9}
$$


where $T_1=c'$ and $T_{-1}=c'-1$. Put


$$
u_\epsilon=\frac{P+\epsilon}{2},
\qquad
k_\epsilon=s-u_\epsilon=\frac{r-\epsilon}{2}.
\tag{2.10}
$$



The important point is that the window fixes the leading ternary digit


$$
2s=P+r,\qquad 0<r<P/5.
$$


The lower digits affect some entries, but, as proved below, they cannot change the unit antidiagonal that determines the rank.

---

## 3. The equal block as a specific graded multiplication map

Let


$$
B_s(T)_{ij}=\binom{2s}{T-i-j},
\qquad 0\le i,j<s,
\tag{3.1}
$$


with out-of-range binomial coefficients defined to be zero.

### 3.1 Row reversal and exact degrees

Reverse the rows, replacing the old row index by $s-1-i$. The resulting matrix has entries


$$
\binom{2s}{T-(s-1-i)-j}
=
\binom{2s}{L+i-j},
\qquad L=T-s+1.
\tag{3.2}
$$



Use auxiliary homogeneous variables $X,Y$, distinct from the original variable $y$. Set


$$
a=T+1=L+s,\qquad
b=4s-T-1=4s-a,
$$


and


$$
\mathcal A=\mathbb F_3[X,Y]/(X^a,Y^b).
$$



Consider the **specific** map


$$
\mu:\mathcal A_{s-1}\longrightarrow\mathcal A_{3s-1},
\qquad F\longmapsto(X+Y)^{2s}F.
\tag{3.3}
$$



For the present parameters, $a,b\ge s$. Consequently the source has basis


$$
X^jY^{s-1-j},\qquad 0\le j<s.
\tag{3.4}
$$



A target monomial $X^qY^{3s-1-q}$ survives precisely when


$$
q<a,\qquad 3s-1-q<b.
$$


Equivalently,


$$
L=a-s\le q\le a-1=L+s-1.
$$


Thus the target basis is exactly


$$
X^{L+i}Y^{3s-1-L-i},\qquad 0\le i<s.
\tag{3.5}
$$



The coefficient of the $i$-th target monomial in the image of the $j$-th source monomial is


$$
\binom{2s}{L+i-j}.
$$


This proves the proposed identification, with both finite boundaries retained.

### 3.2 Signs and the endpoint

For a sector pair with $T=c'-\epsilon_{ab}$, the original signed block is


$$
-(-1)^T D_sB_s(T)D_s,
\qquad
D_s=\operatorname{diag}((-1)^j)_{0\le j<s}.
\tag{3.6}
$$


Both the diagonal changes and row reversal are invertible over $\mathbb F_3$. They introduce no division by $3$.

If $\xi_j$ are the original signed column coordinates, put


$$
w_j=(-1)^j\xi_j,
\qquad
F(X,Y)=\sum_{j=0}^{s-1}w_jX^jY^{s-1-j}.
$$


The prescribed endpoint in residue sector $a_0$ is


$$
\sum_j(-1)^{a_0+j}\xi_j
=
(-1)^{a_0}\sum_jw_j
=
\boxed{(-1)^{a_0}F(1,1).}
\tag{3.7}
$$


Thus the endpoint is an explicit evaluation functional. Row reversal does not alter this source-side observation.

---

## 4. Syzygy degrees give the selected-map nullity

Let $\mathcal S$ be the homogeneous syzygy module of


$$
X^a,\qquad Y^b,\qquad (X+Y)^{2s}.
$$


It is free of rank two over $\mathbb F_3[X,Y]$. Write its homogeneous generator degrees as


$$
d_1\le d_2.
$$



The usual graded resolution has Hilbert numerator


$$
1-t^a-t^b-t^{2s}+t^{d_1}+t^{d_2}.
$$


The quotient has finite length, so this numerator has a double zero at $t=1$. Its first derivative gives


$$
d_1+d_2=a+b+2s=6s.
\tag{4.1}
$$



A kernel element of (3.3) lifts to a syzygy of total degree $3s-1$, by taking its coefficient of $(X+Y)^{2s}$. Conversely, every such syzygy gives a kernel element.

This correspondence is injective at that degree: a syzygy involving only $X^a,Y^b$ is a multiple of


$$
(Y^b,-X^a,0)
$$


and has total degree at least


$$
a+b=4s>3s-1.
$$


Therefore


$$
\dim\ker\mu
=
\max(0,3s-d_1)+\max(0,3s-d_2).
\tag{4.2}
$$


Since $d_1+d_2=6s$, this simplifies to


$$
\boxed{
\dim\ker B_s(T)=\frac{d_2-d_1}{2}.
}
\tag{4.3}
$$



Thus the proposed formula is correct for these equal blocks. It is a statement about the selected map (3.3), not a broad failure-of-Lefschetz assertion.

---

## 5. Exact Han–Monsky gap evaluation on the original word

We use the standard taxicab-distance form of the positive-characteristic syzygy-gap theorem underlying the supplied Nicklasson gate.

### Established syzygy-gap theorem, in the form used here

Let $p$ be the characteristic and let $v=(a,b,N)$ be a positive integer triple satisfying the strict triangle inequalities. Let


$$
L_{\rm odd}=\{z\in\mathbb Z^3:z_1+z_2+z_3\text{ is odd}\}.
$$


If $q=p^e$ is the largest power scale for which


$$
\operatorname{dist}_1(v/q,L_{\rm odd})<1,
$$


then the syzygy gap is


$$
\delta(v)
=
q\left(1-\operatorname{dist}_1(v/q,L_{\rm odd})\right).
\tag{5.1}
$$


If no such scale exists, the gap is zero.

Only this exact gap theorem is used. No ungraded Jordan-type or general SLP classification is substituted for the selected-degree calculation.

### 5.1 Verification of the hypotheses

For $T=T_\epsilon$,


$$
a=P+u_\epsilon=\frac{3P+\epsilon}{2},
$$




$$
b=4s-a=P+2r-u_\epsilon,
\qquad
N=2s=P+r.
\tag{5.2}
$$


The inequalities $r<P/5$, $r\ge11$, and sufficiently large $P$ imply


$$
P<a<2P,\qquad 0<b<P,\qquad P<N<\frac65P.
\tag{5.3}
$$


They also give $a,b\ge s$, as required in §3.

Because $a+b+N=6s$, the triangle inequalities are equivalent to


$$
a<3s,\qquad b<3s,\qquad N<3s.
$$


Here


$$
3s-a=\frac{3r-\epsilon}{2}>0,
$$




$$
3s-b=\frac{2P-r+\epsilon}{2}>0,
$$


and $N=2s<3s$. Thus all hypotheses hold in the original objects.

### 5.2 The first relevant lattice scale

At scale $P$, use the odd lattice point $(1,1,1)$. By (5.3),


$$
\begin{aligned}
\left\|\frac{(a,b,N)}P-(1,1,1)\right\|_1
&=\frac{a-P}{P}+\frac{P-b}{P}+\frac{N-P}{P}\\
&=1-\frac{r-\epsilon}{P}.
\end{aligned}
\tag{5.4}
$$


This is strictly less than $1$.

There is no admissible larger scale. Indeed, for every $q\ge3P$, the normalized coordinates lie strictly between $0$ and $1$, retain the triangle inequalities, and have sum


$$
\frac{6s}{q}\le1+\frac rP<\frac65<2.
$$


An odd lattice point at distance less than $1$ would then have to be one of


$$
(1,0,0),\quad(0,1,0),\quad(0,0,1),\quad(1,1,1).
$$


The distances to the first three are


$$
1+\frac{a+b+N-2a}{q},\quad
1+\frac{a+b+N-2b}{q},\quad
1+\frac{a+b+N-2N}{q},
$$


all greater than $1$ by the strict triangle inequalities. The distance to $(1,1,1)$ is


$$
3-\frac{a+b+N}{q}>1.
$$


Lattice points outside this unit cube are farther away.

Therefore $P$ is exactly the largest scale required in (5.1). Equations (5.1) and (5.4) give


$$
\boxed{\delta_\epsilon=r-\epsilon.}
\tag{5.5}
$$



Combining with §4,


$$
\boxed{
\dim\ker B_s(T_\epsilon)=k_\epsilon=\frac{r-\epsilon}{2},
\qquad
\operatorname{rank}B_s(T_\epsilon)=u_\epsilon=\frac{P+\epsilon}{2}.
}
\tag{5.6}
$$



In particular,


$$
\boxed{
\operatorname{rank}B_s(c')=\frac{P+1}{2},\qquad
\operatorname{rank}B_s(c'-1)=\frac{P-1}{2}.
}
\tag{5.7}
$$



---

## 6. Explicit kernels and their endpoint restrictions

The gap evaluation determines the dimension. A Frobenius syzygy identifies the kernel itself.

Write $Z=X+Y$. Since $P$ is a power of $3$,


$$
Z^P=X^P+Y^P.
$$


For either sign $\epsilon$,


$$
X^{u_\epsilon}Z^{P+r}
=
X^{P+u_\epsilon}Z^r
+
X^{u_\epsilon}Y^PZ^r.
$$


As $a=P+u_\epsilon$ and $b<P$, this is a syzygy with coefficient $X^{u_\epsilon}$ on $Z^{2s}$:


$$
-Z^rX^a
-
X^{u_\epsilon}Y^{P-b}Z^rY^b
+
X^{u_\epsilon}Z^{2s}=0.
\tag{6.1}
$$


Its total degree is


$$
2s+u_\epsilon
=
3s-k_\epsilon
=
d_1.
$$


The evaluated gap shows that this is a minimal-degree generator. At total degree $3s-1$, the second syzygy generator contributes nothing. Hence


$$
\boxed{
\ker\mu
=
X^{u_\epsilon}\mathbb F_3[X,Y]_{k_\epsilon-1}.
}
\tag{6.2}
$$



In matrix coordinates this says


$$
\boxed{
\ker B_s(T_\epsilon)
=
\operatorname{span}\{e_{u_\epsilon},\ldots,e_{s-1}\}.
}
\tag{6.3}
$$



The endpoint from (3.7) restricts to


$$
X^{u_\epsilon}G\longmapsto(-1)^{a_0}G(1,1).
\tag{6.4}
$$


It is nonzero: a monomial $G$ evaluates to $1$. Its kernel is exactly


$$
\boxed{
X^{u_\epsilon}(X-Y)\mathbb F_3[X,Y]_{k_\epsilon-2},
}
\tag{6.5}
$$


with a negative-degree homogeneous space interpreted as zero.

This supplies the actual endpoint restriction, not a generic vector chosen after knowing the rank.

### Independent finite-matrix check

The same kernel follows directly from the high ternary digit. In characteristic $3$,


$$
(1+z)^{2s}=(1+z^P)(1+z)^r.
$$


For every selected matrix entry, the exponent


$$
T_\epsilon-i-j
$$


is greater than $r$. Thus only the upper coefficient band beginning at $P$ can contribute.

Because


$$
T_\epsilon=P+u_\epsilon-1,
$$


entries with $i+j>u_\epsilon-1$ vanish, while entries with


$$
i+j=u_\epsilon-1
$$


equal


$$
\binom{P+r}{P}=1\quad\text{in }\mathbb F_3.
$$


The leading $u_\epsilon\times u_\epsilon$ block is therefore anti-triangular with unit antidiagonal, and all remaining rows and columns are zero.

This is an independent verification of (5.6)–(6.3). It also explains why no lower-digit choice can alter the rank.

---

## 7. The unequal rectangular pair

The unequal pair is exactly


$$
122\longleftrightarrow242.
$$


Its off-diagonal unsigned block has $s$ rows, $s-1$ columns, and


$$
T=c'-1.
$$



Put


$$
u=u_{-1}=\frac{P-1}{2},\qquad
a=T+1=P+u,
$$


and now set


$$
b_{\rm rec}=4s-a-1.
\tag{7.1}
$$


The subtraction of $1$ is essential.

### 7.1 The right-kernel map

After reversing its $s$ rows, the rectangular block is the map


$$
\mathbb F_3[X,Y]/(X^a,Y^{b_{\rm rec}})
\;:\;
\text{degree }s-2
\longrightarrow
\text{degree }3s-2
\tag{7.2}
$$


given by multiplication by $(X+Y)^{2s}$.

The source dimension is $s-1$. The target surviving $X$-exponents are


$$
L=T-s+1,\ldots,T,
$$


so the target dimension is $s$.

### 7.2 The left-kernel map

The transpose, after reversing its $s-1$ rows, is the map in the **same quotient**


$$
\text{degree }s-1
\longrightarrow
\text{degree }3s-1.
\tag{7.3}
$$


Its target surviving $X$-exponents are


$$
L+1,\ldots,T,
$$


so its dimensions are $s\to s-1$.

### 7.3 Gap and nullities

The syzygy-degree sum is now


$$
a+b_{\rm rec}+2s=6s-1.
$$


At scale $P$, the distance to $(1,1,1)$ is


$$
1-\frac rP.
$$


The same larger-scale exclusion as in §5 applies, with strict triangle inequalities still valid. Therefore


$$
\boxed{\delta_{\rm rec}=r.}
\tag{7.4}
$$



The minimal syzygy degree remains


$$
d_1=2s+u.
$$


There is again no relation involving only $X^a,Y^{b_{\rm rec}}$ at either selected target degree, since its least possible total degree is $4s-1$.

Consequently,


$$
\boxed{
\dim\ker_{\rm right}=\frac{r-1}{2},
\qquad
\dim\ker_{\rm left}=\frac{r+1}{2},
}
\tag{7.5}
$$


and


$$
\boxed{\operatorname{rank}B_{\rm rec}=\frac{P-1}{2}.}
\tag{7.6}
$$



The right and left kernels are respectively the coordinate tails


$$
j=u,\ldots,s-2,
\qquad
i=u,\ldots,s-1.
$$


Their endpoint restrictions are again evaluation at $(1,1)$, with the prescribed sector signs. In particular, both restrictions are nonzero.

The full symmetric unequal pair therefore contributes nullity


$$
(s+s-1)-2u=\boxed r.
\tag{7.7}
$$



---

## 8. Assembly in the original residual coordinates

There are:

* $122$ equal sectors with $a+b=121$, hence $T=c'$;
* $119$ equal sectors with $a+b=364$, after removing the unequal pair;
* the unequal pair itself.

Thus the total rank is


$$
122\frac{P+1}{2}
+
119\frac{P-1}{2}
+
2\frac{P-1}{2}
=
\boxed{\frac{243P+1}{2}}.
\tag{8.1}
$$


The total nullity is


$$
122\frac{r-1}{2}
+
119\frac{r+1}{2}
+r
=
\boxed{\frac{243r-3}{2}}.
\tag{8.2}
$$



More is true: these sector tails assemble into a single contiguous tail in the original ordering.

Let


$$
R_*=\frac{243P+1}{2}
=243\frac{P-1}{2}+122.
\tag{8.3}
$$


For residue sectors $0,\ldots,121$, the radical begins at sector coordinate $(P+1)/2$. For residue sectors $122,\ldots,242$, it begins at $(P-1)/2$. These are exactly the original indices


$$
R_*,R_*+1,\ldots,\nu-1.
$$



### Theorem 8.1 — Exact original-coordinate radical

For every sufficiently large original tuple in the adjacent window,


$$
\boxed{
\operatorname{rank}K=R_*,
\qquad
\ker K=\operatorname{span}\{e_{R_*},\ldots,e_{\nu-1}\}.
}
\tag{8.4}
$$



#### Direct sign and boundary verification

Put


$$
P_0=243P,\qquad N_0=243r.
$$


Then


$$
D=P_0+N_0,\qquad c=\frac{3P_0-1}{2},
$$


and in characteristic $3$,


$$
(y-1)^D=(y^{P_0}-1)(y-1)^{N_0}.
\tag{8.5}
$$


Every extraction index $c-i-j$ in the original finite matrix is greater than $N_0$, because


$$
c-2(\nu-1)=\frac{P_0-2N_0+7}{2}>N_0
$$


by $N_0<P_0/5$.

Hence entries with $i+j>R_*-1$ vanish. On the antidiagonal


$$
i+j=R_*-1,
$$


the extraction index is $P_0$. Since $N_0$ is odd,


$$
[y^{P_0}](y-1)^D=(-1)^{N_0}=-1,
$$


and therefore


$$
K_{ij}=1.
$$


The leading $R_*\times R_*$ block is anti-triangular with unit antidiagonal. This proves (8.4), including the original sign. ∎

The old lower bound $242$ has not been used as an upper bound. The new equality follows from the evaluated selected maps and the explicit unit antidiagonal.

Since $r\ge11$,


$$
\boxed{\tau=\dim\ker K\ge1335.}
\tag{8.6}
$$



### 8.1 Exact endpoint restriction on the full radical

For


$$
v=\sum_{j=0}^{\tau-1}\xi_j e_{R_*+j},
$$


the prescribed endpoint is


$$
\boxed{
\bar e^Tv=(-1)^{R_*}\sum_{j=0}^{\tau-1}(-1)^j\xi_j.
}
\tag{8.7}
$$


It is nonzero.

Equivalently, identify $v$ with


$$
t^{R_*}G(t),\qquad \deg G<\tau.
$$


Then its endpoint is


$$
(-1)^{R_*}G(-1).
$$


Thus the endpoint-annihilating radical is exactly


$$
\boxed{
t^{R_*}(t+1)\mathbb F_3[t]_{<\tau-1}.
}
\tag{8.8}
$$


A concrete basis is


$$
e_{R_*+j-1}+e_{R_*+j},
\qquad 1\le j<\tau.
\tag{8.9}
$$



Consequently the prescribed first bordered reduction has rank


$$
R_*+2.
$$


Its determinant still vanishes, because $\tau\ge1335$. This does not say that the corresponding actual $3$-adic determinant is zero; it says that its next digits must be evaluated.

The residual terminal direction $e_{\nu-1}$ belongs to this radical and has nonzero endpoint observation. This fact does not remove any other term in the complete forcing.

---

## 9. Growth: linear on fixed subwindows, unbounded on every infinite original subfamily

The exact equal-sector nullities are


$$
k_\epsilon
=s\left(1-\frac\rho3\right)-\frac\epsilon2,
\tag{9.1}
$$


and


$$
\tau
=
243s\left(1-\frac\rho3\right)-\frac32.
\tag{9.2}
$$



### 9.1 Fixed closed subwindows

If


$$
\kappa_0<\rho_-\le\rho\le\rho_+<3,
$$


then


$$
k_\epsilon\ge
s\left(1-\frac{\rho_+}{3}\right)-\frac12.
$$


Thus all these nullities grow linearly with $s$ on every fixed closed subwindow.

### 9.2 No uniform linear lower bound on the entire open window

The established density theorem concerns the original progression and every fixed open real interval. Applying it successively to intervals approaching $3$ from below produces an increasing sequence of **original** indices with


$$
\rho\longrightarrow3^-.
$$


No ternary digit is prescribed in this selection.

Along that sequence,


$$
\frac{k_\epsilon}{s}\longrightarrow0,
\qquad
\frac{\tau}{s}\longrightarrow0.
$$


Therefore there is no uniform bound $k_\epsilon\ge c s$, with $c>0$, throughout the entire open window.

### 9.3 Bounded nullity cannot persist on an infinite original subfamily

For this conclusion, reuse the standard fixed-logarithm consequence of the theorem on linear forms in logarithms:

> For fixed positive algebraic numbers $\alpha_1,\ldots,\alpha_t$, there are positive effective constants $c,M$ such that every nonzero real linear form
> 

$$
> \Lambda=b_1\log\alpha_1+\cdots+b_t\log\alpha_t
>
$$


> with integer coefficients satisfies
> 

$$
> |\Lambda|\ge cB^{-M},
> \qquad B=\max(3,|b_1|,\ldots,|b_t|).
>
$$



Let


$$
C_*=3^{26}-1,\qquad n_*=h-27.
$$


Equation (2.7) becomes


$$
4^j=C_*3^{n_*}-(243r-1).
$$


Set


$$
x=\frac{243r-1}{C_*3^{n_*}}
=\frac{r-1/243}{C_*P}.
$$


By $0<r<P/5$,


$$
0<x<\frac1{5C_*}<\frac12.
$$


Thus


$$
\Lambda=n_*\log3+\log C_*-j\log4
=-\log(1-x)
$$


is nonzero and satisfies


$$
0<\Lambda<2x<\frac{2r}{C_*P}.
\tag{9.3}
$$


The fixed-logarithm theorem applies to the fixed algebraic numbers $3,C_*,4$. Since


$$
j=O(\log P),\qquad n_*=O(\log P),
$$


it follows that there are constants $c_1,M>0$, independent of the original tuple, such that


$$
\boxed{
r\ge c_1\frac{P}{(\log P)^M}
}
\tag{9.4}
$$


for all sufficiently large retained tuples.

Therefore $r\to\infty$, and hence every sector nullity and $\tau$ tend to infinity, along every infinite original subfamily in this window.

The precise conclusion is therefore:

* linear growth on fixed interior subwindows;
* possible $o(s)$ growth along original indices approaching the upper edge;
* no bounded-nullity infinite original subfamily.

In particular, no fixed number of added border coordinates can eventually produce a unit mod-$3$ bordered certificate along such an infinite family.

---

## 10. A concrete next actual Schur step

The macroscopic radical is now explicit. The next step should address the **relative cofactor**, not merely accumulate common divisibility.

Everything in this section is conditional on the actual identification (1.2), the prescribed endpoint transport, and the stated integrality:


$$
e_{\rm act}\in\mathbb Z_3^\nu,\qquad
\bar e_{{\rm act},i}=(-1)^i,\qquad
d_{\rm act}\in3^{-1}\mathbb Z_3.
$$



Order coordinates as the prefix $0,\ldots,R_*-1$, followed by the radical tail. Write


$$
U=
\begin{pmatrix}
\mathsf A&\mathsf B\\
\mathsf B^T&\mathsf C
\end{pmatrix},
\qquad
e_{\rm act}=\binom{e_C}{e_R}.
$$


The proved candidate structure gives


$$
\det\mathsf A\in\mathbb Z_3^\times,\qquad
\mathsf B\in3M,\qquad
\mathsf C\in3M.
$$


Define


$$
\mathcal R=\mathsf C-\mathsf B^T\mathsf A^{-1}\mathsf B,
$$




$$
f=e_R-\mathsf B^T\mathsf A^{-1}e_C,
$$


and retain the complete bordered diagonal


$$
\lambda=3^{26}d_{\rm act}-e_C^T\mathsf A^{-1}e_C\in\mathbb Z_3.
\tag{10.1}
$$



Because $\mathsf B\in3M$, the first radical digit simplifies to


$$
\boxed{
\overline{\mathcal R/3}
=
\overline{\mathsf C/3}.
}
\tag{10.2}
$$


This is a useful consequence of the newly proved coordinate radical. It does **not** evaluate that digit.

### 10.1 Precisely which producer information is still required

Under the retained perturbation formula


$$
S_{\rm act}=S_c+3^6\Phi_R-3^{13}\mathcal Q,
$$


and the stronger bounds


$$
\Phi_R\in3^{21}M,\qquad \mathcal Q\in3^{21}M,
$$


equation (10.2) gives, on the explicit tail,


$$
\boxed{
\overline{\mathcal R/3}
=
-\overline{\frac{(S_c)_{RR}}{3^{27}}}
-\overline{\frac{(\Phi_R)_{RR}}{3^{21}}}.
}
\tag{10.3}
$$


The $\mathcal Q$-term vanishes at this precision.

Thus the needed new information is:

* the core tail block modulo $3^{28}$;
* the stronger producer digit $(\Phi_R)_{RR}/3^{21}\pmod3$.

Even $\Phi_R\in3^{21}M$ does not make its contribution disappear from $U\bmod9$. The weaker bound $\Phi_R\in3^{20}M$ does not even justify the preceding actual depth-$26$ identification.

No actual mod-$9$ conclusion is inferred from $K\bmod3$.

### 10.2 Endpoint-annihilator relative-cofactor lemma

Every component of $f$ is a unit, since


$$
\bar f_j=(-1)^{R_*+j}.
$$


Use the unimodular tail basis


$$
t_0=e_0,\qquad
t_j=e_j-\frac{f_j}{f_{j-1}}e_{j-1},
\quad 1\le j<\tau.
\tag{10.4}
$$


The divisions here are by units. This basis has determinant $1$, and


$$
f^Tt_0=f_0,\qquad f^Tt_j=0\quad(j\ge1).
$$


Modulo $3$, its endpoint-annihilating columns are exactly the adjacent sums in (8.9).

In this basis write


$$
\mathcal R'=
\begin{pmatrix}
a_0&w^T\\
w&M
\end{pmatrix}.
\tag{10.5}
$$



### Lemma 10.1 — A relative valuation from the endpoint-annihilating block

Assume


$$
M=3\mathsf W,\qquad \det\mathsf W\in\mathbb Z_3^\times,
$$


and define


$$
\sigma=a_0-w^TM^{-1}w.
\tag{10.6}
$$


If $\sigma\ne0$, then, with


$$
\kappa_\sigma=v_3(\sigma)\ge1,
$$


the complete distinguished pair satisfies


$$
\boxed{
v_3D_0=\tau-1+\kappa_\sigma,\qquad
v_3D_1=\tau-1,
}
\tag{10.7}
$$


and hence


$$
\boxed{v_3D_1-v_3D_0=-\kappa_\sigma.}
\tag{10.8}
$$



#### Proof

The inverse is


$$
M^{-1}=3^{-1}\mathsf W^{-1}.
$$


This is a new, independently paid division. Since $a_0,w\in3\mathbb Z_3$, equation (10.6) gives $\sigma\in3\mathbb Z_3$.

The determinant identities are


$$
D_0=\det\mathsf A\,\det M\,\sigma,
$$


and, because the transformed endpoint is $(f_0,0,\ldots,0)$,


$$
D_1
=
\det\mathsf A\,\det M\,(f_0^2-\lambda\sigma).
\tag{10.9}
$$


Here $\lambda$ is the complete diagonal (10.1), not a discarded term.

Now $f_0$ is a unit, $\lambda$ is integral, and $\sigma\in3\mathbb Z_3$. Therefore $f_0^2-\lambda\sigma$ is a unit. Also


$$
v_3(\det M)=\tau-1.
$$


Equations (10.7)–(10.8) follow. ∎

This criterion can work even when the full once-normalized radical matrix is singular modulo $3$. It isolates the endpoint-observed scalar instead of requiring every radical direction to be lifted after one division.

### 10.3 An explicit next lemma to prove or disprove

Let


$$
\bar V=\overline{\mathcal R/3},
$$


and let $H_{\rm end}$ have columns


$$
e_{j-1}+e_j,\qquad 1\le j<\tau.
$$


Then


$$
\overline{\mathsf W}=H_{\rm end}^T\bar V H_{\rm end},
$$


whose entries are explicitly


$$
\overline{\mathsf W}_{ij}
=
\bar V_{i-1,j-1}+\bar V_{i-1,j}
+\bar V_{i,j-1}+\bar V_{i,j}.
\tag{10.10}
$$


If this matrix is invertible, put


$$
z_i=\bar V_{i-1,0}+\bar V_{i,0}.
$$


Then


$$
\frac{\sigma}{3}\pmod3
=
\bar V_{00}-z^T\overline{\mathsf W}^{-1}z.
\tag{10.11}
$$



A concrete follow-on obligation is therefore:

> Evaluate the actual matrix digit (10.3) on the original tail, and prove or disprove, on a specified infinite original subfamily, the invertibility in (10.10) and the nonvanishing of (10.11).

If both hold, then $\kappa_\sigma=1$ and the relative valuation is exactly $-1$. If (10.11) vanishes, further actual precision is required to distinguish a higher finite valuation from $\sigma=0$.

This remains an open producer-aware lemma. No full original-matrix computation is requested here.

---

## 11. Primitive arithmetic and the complete same-index error

At normalization $26$, retain


$$
D_0=\det U,
$$




$$
D_1=e_{\rm act}^T\operatorname{adj}(U)e_{\rm act}
-3^{26}d_{\rm act}D_0.
$$



At the stated scope of the retained exact primitive-ratio identity,


$$
\boxed{
v_3(q)=
\max\!\left(
0,\,
h-26+v_3Q_{\rm loc}(-1)+v_3D_1-v_3D_0
\right).
}
\tag{11.1}
$$


If Lemma 10.1 is eventually proved applicable, this becomes


$$
v_3(q)=
\max\!\left(
0,\,
h-26+v_3Q_{\rm loc}(-1)-\kappa_\sigma
\right).
\tag{11.2}
$$


At present, its hypotheses have not been verified. The exact candidate rank supplies no actual value of $\kappa_\sigma$.

The complete corrected columns remain


$$
F_{\rm act}=Z-WE_{\rm act}^{-1}C_{\rm act},
$$


and the complete closure remains


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
\tag{11.3}
$$


No logarithmic forcing, exponential boundary charge, finite return, exterior constant, or physical terminal contribution has been removed.

Likewise, the actual column contents, multiplier, previously paid divisions, and **least simultaneous clearer** are unchanged. The new auxiliary graded rings do not replace any of these original objects.

Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over **all primes**. For $B_\ell\ne0$, the actual primitive quantities are


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole error is exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{11.4}
$$



An irrationality proof still requires, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\log g_\ell-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|\longrightarrow+\infty.
\tag{11.5}
$$


A ternary relative-cofactor result alone does not establish this all-prime comparison.

---

## 12. A bounded new arithmetic audit

No producer calculation, multiplier chain, or full original matrix needs to be repeated.

The following optional finite check tests only the newly proposed map, gap, and endpoint formulas.

### Bounded inputs

Take


$$
P=81,\qquad r=11,\qquad s=46,\qquad c'=121.
$$


These satisfy


$$
s\equiv1\pmod9,\qquad c'\equiv4\pmod9,
\qquad 0<r<P/5,
$$


and


$$
\kappa_0<\frac{3P}{P+r}=\frac{243}{92}<3.
$$



This is an **auxiliary finite instance**, not a claim that these small parameters arise from an original $j,h$.

### Expected verifiable outputs



$$
\begin{array}{c|c|c|c|c}
\text{block}&(a,b,2s)&\text{gap}&(d_1,d_2)&\text{rank}\\ \hline
B_{46}(121)&(122,62,92)&10&(133,143)&41\\
B_{46}(120)&(121,63,92)&12&(132,144)&40\\
46\times45,\ T=120&(121,62,92)&11&(132,143)&40
\end{array}
$$



More specifically:

1. Row reversal gives the coefficient matrices of the selected degree maps proved in §§3 and 7.
2. The distances at scale $81$ to $(1,1,1)$ are respectively
   

$$
\frac{71}{81},\qquad \frac{69}{81},\qquad \frac{70}{81}.
$$


3. The equal-block kernels are the coordinate tails
   

$$
41,\ldots,45,\qquad 40,\ldots,45.
$$


4. The rectangular right and left kernels are
   

$$
40,\ldots,44,\qquad 40,\ldots,45.
$$


5. After the stated sign change, the endpoint is evaluation at $(1,1)$, is nonzero on each kernel, and its kernel is obtained by the factor $X-Y$.
6. Every relevant leading block has the asserted unit antidiagonal.

The largest matrix in this audit is $46\times46$. No such calculation has been executed here. Its output would verify only this bounded instance; the infinite-scope conclusions above rest on the symbolic proofs.

---

## 13. Proof-status ledger

| Statement | Status |
|---|---|
| Exact equal-block selected-degree realization | Proved |
| Equal-block kernel dimension equals half the syzygy gap | Proved with the degree-bound hypothesis checked |
| Original-word gaps $r-1,r+1$ | Proved by the established lattice-distance theorem, with all hypotheses verified |
| Explicit equal-sector kernels and endpoint restrictions | Proved |
| Correct rectangular degree maps, gap, ranks, and endpoints | Proved |
| Exact candidate rank $R_*=(243P+1)/2$ | Proved |
| Original-coordinate radical is the terminal coordinate tail | Proved |
| Linear nullity growth on fixed closed subwindows | Proved |
| No uniform positive linear bound on the entire open window | Proved using original-index density |
| No bounded-nullity infinite original subfamily | Proved using the standard fixed-logarithm lower bound |
| Identification of actual $U\bmod3$ with $K$ | Conditional on retained depth-$26$ transport hypotheses |
| Actual radical digit $U_{RR}/3\bmod3$ | Open; requires stronger producer information |
| Endpoint-annihilator relative-cofactor criterion | Proved conditional implication |
| Its hypotheses on an infinite original subfamily | Open |
| Actual primitive denominator and all-prime whole-error comparison | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

## Conclusion

The selected-degree syzygy method closes the previously open candidate-sector rank problem in this adjacent window. The new exact result is


$$
\boxed{
\operatorname{rank}K_{26}
=\frac{\Omega/3+1}{2},
\qquad
\operatorname{rad}K_{26}
=
\operatorname{span}\{e_{R_*},\ldots,e_{\nu-1}\},
}
$$


with


$$
\boxed{
\dim\operatorname{rad}K_{26}
=\frac{D-\Omega/3-3}{2}.
}
$$


The endpoint restriction is the explicit alternating evaluation on that tail; its annihilator is generated by adjacent coordinate sums.

There is no infinite original bounded-nullity escape from this obstruction. Approaching the upper edge can make the radical small **relative** to $s$, but not bounded in absolute dimension.

The exact remaining local bottleneck is now the actual, producer-aware digit


$$
-\frac{(S_c)_{RR}}{3^{27}}
-\frac{(\Phi_R)_{RR}}{3^{21}}
\pmod3,
$$


followed by its restriction to the explicitly identified endpoint-annihilating radical and the observed scalar Schur complement. Every inverse used in that step requires its own payment.

The global bottleneck remains transport to the actual primitive ratio, through all actual contents and the least simultaneous clearer, and then comparison of the **all-prime final gcd** with the **nonzero whole evaluated error at the same infinite original indices**.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ has been obtained.}}
$$


