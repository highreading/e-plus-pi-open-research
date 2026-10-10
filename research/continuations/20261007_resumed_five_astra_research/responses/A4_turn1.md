> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Reconciliation of the complete-core support theorem and the ten-digit edge obligation

## Executive conclusion

The archived **core-only** support theorem applies to the retained progression


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$


despite $v_3(j)=4$. The older hypothesis $v_3(j)\ge r-2$ is not used by any of the five finite core operations. It belonged to the attempted transfer from the core polynomial to the actual producer, whose arbitrary-depth approximation is not used here.

Consequently, the coordinator’s proposed implication is valid:



$$
\boxed{
[x^a]F_i\equiv0\pmod{3^{10}}\quad(0\le a<27),
\qquad
[y^{m-k}]F_i\equiv0\pmod{3^{10}}\quad(0\le k<9).
}
$$



The proof uses the **complete** core columns, the actual LOW projection, the finite HIGH inverse, and both finite HIGH boundaries. In particular, it does not substitute producer locality for corrected-column locality.

Applying A1turn22’s multiplier lemma then proves, uniformly over the sufficiently large retained original indices,


$$
\boxed{\Phi_R\in3^{11}M,\qquad S_{\rm act}\in3^{17}M.}
$$



There is also a stronger linear consequence. The same core support at precision $3^{16}$, combined with the already established integral source reset


$$
R_{\rm prod}=3\gamma Q_c+9J_2,
$$


gives


$$
\boxed{\Phi_R\in3^{18}M.}
$$


A complete derivation is given below. It uses factorial saturation at its stated scope, not an arbitrary-depth approximation of the actual producer by $Q_c$.

This stronger linear result does **not** establish deeper whole-matrix divisibility, inverse alignment, a nonzero distinguished cofactor, the all-prime primitive denominator, or decay of the whole nonzero error. At the independently reviewed nonlinear scope supplied by A4turn19, the unconditional whole-matrix conclusion remains


$$
\boxed{S_{\rm act}\in3^{17}M.}
$$



The rationality or irrationality of $e+\pi$ remains unresolved.

---

## 1. Original domain and exact objects

Throughout, retain


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$


and


$$
m=2^{2j-1},\qquad n=4^j+1,\qquad A=n-2=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


subject to


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad
C_{16}=147968\,3^{15}=512\cdot17^2\,3^{15}.
\tag{1.1}
$$



All uniform conclusions concern sufficiently large indices in this same retained window. No additional residue condition is imposed.

The finite polynomial spaces remain


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
d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
\tag{1.2}
$$


In particular,


$$
d=D+\nu,\qquad \deg z_i\le d-1,\qquad i+j\le D-4.
$$



Put


$$
W=[U\ Y],\qquad
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A,
$$


and use the complete functional


$$
\mathcal M(G)=
-\frac{3^h}{4}\mathfrak f(G)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](G-G(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^r)=(2r)!.
\tag{1.3}
$$



Thus


$$
G_c(f,g)=\mathcal M(Q_cfg),
$$




$$
E_c=G_c(W,W),\qquad C_c=G_c(W,Z),
$$


and the complete corrected columns are


$$
F_i=\widehat z_i^{\,c},\qquad
\widehat Z^{\,c}=Z-WE_c^{-1}C_c.
\tag{1.4}
$$



No HIGH coordinate beyond $m$, no residual coordinate beyond $\nu-1$, and no replacement terminal condition is introduced.

### 1.1 Elementary domain checks

Because


$$
84645=81\cdot1045,\qquad 1045\equiv1\pmod3,
$$


and $531441=3^{12}$, every retained $j$ satisfies


$$
v_3(j)=4.
$$


The lifting-the-exponent identity gives


$$
v_3(A)=v_3(4^j-1)=1+v_3(j)=5.
\tag{1.5}
$$



For sufficiently large retained indices, $h-1>5$, so


$$
v_3(D)=v_3(H-A)=5.
$$


Also $H$ and $A$ are odd, so $D$ is even. Hence


$$
D\ge 2\cdot3^5=486.
\tag{1.6}
$$



In particular, the core requirements “$D$ even and divisible by $3$” hold, as do


$$
\beta\equiv1\pmod3,\qquad \beta+3\in\mathbb Z_3^\times.
$$



The retained fixed real window implies $H,D,h\to\infty$ along its infinite original-index subfamily. Thus all fixed lower bounds on $h$, $D$, and factorial valuations used below hold eventually.

---

## 2. The apparent LOW-basis discrepancy is harmless—but must be handled correctly

A4turn26 writes the LOW basis as


$$
U_y=(1,y,\ldots,y^{D-1}),
$$


whereas the retained construction uses


$$
U_x=(1,x,\ldots,x^{D-1}).
$$



These are not identical coordinate arrays. They are, however, integral unimodular bases of the same polynomial space.

Let


$$
T_{au}=
\begin{cases}
(-1)^{u-a}\binom ua,&a\le u,\\
0,&a>u.
\end{cases}
$$


Then


$$
U_x=U_yT,\qquad \det T=1.
\tag{2.1}
$$



If $L_y,X_y$ are the normalized LOW and LOW/HIGH matrices in the $y$-basis, then


$$
L_x=T^TL_yT,\qquad X_x=T^TX_y.
$$


Consequently,


$$
U_xL_x^{-1}X_x
=
U_yL_y^{-1}X_y.
\tag{2.2}
$$



Thus the **polynomial LOW projection**, the complete HIGH feedback operator, and the complete corrected columns are unchanged.

This is the correct way to transport the archive argument. One must not transfer a coordinatewise statement in one LOW basis to the other without the Pascal transformation. In the present audit, the needed statements concern the projection polynomial and complete columns, and (2.2) proves their invariance.

Moreover, $[U,Z,Y]$, ordered by polynomial degree, is an integral unitriangular basis of the polynomials of degree at most $m$. Complete correction is an integral column shear. Therefore $[W,F]$ is also an integral basis of that space. This validates the integral basis decomposition used later in the multiplier argument.

---

## 3. Audit of all five finite core operations

For $r\ge6$, define


$$
\Omega_r=\frac H{3^{r-1}},
\qquad
C_r=512(r+1)^2\,3^{r-1},
$$


and


$$
W_r=4(r+1)(D+2).
\tag{3.1}
$$



The archive’s sufficient conditions are


$$
h\ge r+2,\qquad C_rD<H.
\tag{3.2}
$$


They imply


$$
W_r+2D+2<\frac{\Omega_r}{8}.
\tag{3.3}
$$



The five operations use only the following arithmetic properties:

- $H$ is a power of $3$;
- $D$ is even and divisible by $3$;
- $\beta\equiv1\pmod3$;
- the stated finite endpoints;
- the coefficient support of $x^H$ and $(1-z)^{-H}$;
- the separation inequality (3.3);
- sufficient factorial precision after the one displayed normalization by $3$.

None requires $v_3(A)\ge r-1$, and hence none requires $v_3(j)\ge r-2$.

The individual checks follow.

### 3.1 Coefficient support and precision

For $0<k<H$,


$$
v_3\binom Hk=h-1-v_3(k).
\tag{3.4}
$$


Indeed,


$$
\binom Hk=\frac Hk\binom{H-1}{k-1},
$$


and the second factor is a $3$-adic unit.

Likewise, for


$$
a_k=[z^k](1-z)^{-H}=\binom{H+k-1}{k},
$$




$$
v_3(a_k)\ge h-1-v_3(k).
\tag{3.5}
$$



Therefore, below degree $H$, both arrays modulo $3^q$ are supported on multiples of


$$
H/3^{q-1}.
$$


For $q\le r$, those multiples belong to the $\Omega_r$-grid.

Every pole retained at the normalized precision occurs on an odd half-grid. Its unit denominator changes its coefficient, not its support. This applies to every pole in the original finite cutoff; it does not rely on pairing selected poles.

### 3.2 Operation 1: the complete mixed source $V$

Write


$$
r_1=\frac{H-1}{2},\qquad r_*=\frac{3H-1}{2}.
$$


The exact finite endpoints give


$$
i+b\le \nu-1+m=r_1-1.
\tag{3.6}
$$



In the top contribution, the $\beta x^H$ term cannot reach $r_*$. The $3yx^H$ term reaches it only at


$$
i=\nu-1,\qquad b=m.
$$


Thus the original last-residual/last-HIGH corner is present, with its stated normalized coefficient.

All lower contributions place the HIGH row on an odd half-grid with local shift $-i-\epsilon$, where $\epsilon\in\{0,1\}$. The width is at most


$$
\nu+1=D/2.
$$



For rows


$$
d\le b\le d+W_r,
$$


the local shift is bounded by $W_r+2D-2$. Inequality (3.3) excludes a surviving extraction. Hence the lower-edge zero is entrywise, not a cancellation against omitted rows.

No valuation of $j$ beyond the elementary domain properties enters this argument.

### 3.3 Operation 2: the finite HIGH inverse

The inverse coefficient formula is


$$
R_{ab}
=
[z^{D+r_1-a-b}](1-z)^D(1-z)^{-H},
\qquad d\le a,b\le m.
\tag{3.7}
$$


Every nonnegative selected degree is below $H$:


$$
D+r_1-a-b\le D+r_1-2d<H.
\tag{3.8}
$$


Thus the proven inverse-series support is sufficient; no unrestricted infinite inverse is substituted for the finite one.

For a half-grid input at $b$, a supported inverse-series coefficient produces a polynomial copy


$$
y^{r_1-b-k\Omega_r}(y-1)^D.
\tag{3.9}
$$


The sign is correct because $D$ is even.

There are exactly two finite-boundary possibilities:

1. **Upper boundary $m$.**  
   Integer-grid copies of the allowed width cannot straddle this half-grid boundary. They are wholly retained or wholly excluded.

2. **Lower boundary $d$.**  
   Only a copy near the integer-grid origin can be cut. Its retained part lies in the stated lower-edge interval.

This produces complete internal copies plus a lower-edge vector, without a width increase and without a new division.

### 3.4 Operation 3: the actual feedback operator on an internal copy

For a wholly internal copy


$$
p=y^{k\Omega_r+s}x^D,
$$


one has


$$
x^Ap=x^Hy^{k\Omega_r+s}.
\tag{3.10}
$$



Before using support separation, the LOW top-pole contribution vanishes by degree:


$$
\deg\bigl(x^A(\beta+3y)p\,y^u\bigr)
\le H+m<r_*
\qquad(u<D).
\tag{3.11}
$$


The last strict inequality is equivalent to $D>2$.

All lower LOW extractions have shifts within the established gap. Thus the actual LOW force is zero at the required precision. Because the normalized LOW inverse is integral, its feedback is zero at that precision as well.

The remaining feedback terms have half-grid support, with local width increased by at most one. The coefficient


$$
(\beta-1)/3=-24-A/3
$$


need only be integral. No stronger valuation is used.

### 3.5 Operation 4: the actual lower-edge LOW projection

For $0\le s\le w$, monic division gives


$$
y^{d+s}=r_s+x^Dq_s,\qquad \deg r_s<D,
$$


where


$$
q_s=\sum_{a=0}^{\nu+s}
\binom{D+a-1}{a}y^{\nu+s-a}.
\tag{3.12}
$$


This is an integral polynomial quotient of degree $\nu+s$.

The difference between the LOW forces of $y^{d+s}$ and $r_s$ involves


$$
x^H(\beta+3y)q_sy^u.
$$


Its lower shifts lie inside the proved gap. Its degree is at most


$$
H+\nu+s+D<r_*.
\tag{3.13}
$$


Thus


$$
L_U^{-1}X_Ue_{d+s}\equiv r_s\pmod{3^r}.
\tag{3.14}
$$



This is the essential identification: the **actual orthogonal LOW projection**, not an informal truncation, is the monic remainder at the required precision.

For the top terms,


$$
r_*-A-d=m.
\tag{3.15}
$$


The resulting upper-edge contribution has the stated finite width. The lower terms have shifts in


$$
[-(\nu+s+1),0].
$$


The total width increase is therefore at most $\nu+1=D/2$.

### 3.6 Operation 5: exact upper-to-lower transport

For the actual upper row $b=m-s$,


$$
D+r_1-a-b=d+s-a.
$$


Equation (3.7) therefore gives


$$
R_{a,m-s}=0\qquad(a>d+s).
\tag{3.16}
$$


Thus upper-edge width $w$ returns to lower-edge width $w$, exactly within the finite matrix.

This check includes the physical HIGH terminal $Y_m$. It does not append a coordinate beyond it.

### 3.7 Normalization and factorial accounting

The eliminated block has the form


$$
E_c=
\begin{pmatrix}
3L&3X\\
3X^T&E_Y
\end{pmatrix},
$$


with $L$ integral and unimodular. The HIGH Schur operator is


$$
E_0+3\mathcal F,
$$


where $\mathcal F$ includes the complete LOW feedback.

The LOW normalization divides by $3$ once. The factorial term then has valuation at least


$$
h-1\ge r+1.
$$


All subsequent normalized LOW and HIGH inversions are unit inversions. There is no additional unpaid division hidden in the finite Neumann walks.

The resulting archived conclusions are therefore valid for the present core:


$$
\boxed{S_c\in3^{r+1}M,}
\tag{3.17}
$$


and the corrected-column support statement derived next.

The unsupported arbitrary-depth actual-producer approximation plays no part in this audit.

---

## 4. Complete corrected-column support

Fix $p\ge1$, and set $r=\max(6,p)$. Under (3.2), the complete core columns satisfy


$$
F_i\equiv x^D\psi_i(y)\pmod{3^p},
\tag{4.1}
$$


with


$$
\deg\psi_i\le m-D,\qquad
\operatorname{supp}_y\psi_i\subseteq I_{\Omega_r}(pD/2),
\tag{4.2}
$$


where


$$
I_\Omega(w)=\{a\Omega+u:a\in\mathbb Z,\ |u|\le w\}.
$$



Here is the width accounting.

The HIGH correction has an initial factor $3$. For $p\ge2$, only $p-2$ feedback occurrences are needed modulo $3^p$. Starting from width


$$
w_0=\nu+1=D/2,
$$


the retained walks have width at most


$$
(p-1)D/2.
$$


The final lower-edge monic quotient adds at most $\nu=D/2-1$, giving width at most


$$
pD/2-1.
$$


The stated $pD/2$ is therefore a safe bound. For $p=1$, $F_i\equiv z_i\pmod3$ gives the assertion directly.

The direct normalized LOW source is zero at the required precision by the same degree and grid-gap argument. Thus the final LOW subtraction is precisely the one needed to complete the $x^D$-divisible polynomial copies.

This establishes support for the complete eliminated columns—not merely for a producer source or an unprojected HIGH response.

---

## 5. Verification of the coordinator’s ten-digit implication

Take


$$
p=r=10,\qquad \Omega=\frac H{3^9}.
$$



### 5.1 Numerical hypotheses

The constants satisfy


$$
C_{10}=512\cdot11^2\,3^9<C_{16},
$$


since


$$
\frac{C_{16}}{C_{10}}
=\frac{17^2}{11^2}\,3^6>1.
$$


The retained window gives


$$
C_{10}D<C_{16}D<H.
$$


Also $h\ge12$ eventually.

Hence


$$
F_i\equiv x^D\psi_i\pmod{3^{10}},
$$




$$
\deg\psi_i\le \frac{H-3D+1}{2},
\qquad
\operatorname{supp}\psi_i\subseteq I_\Omega(5D).
\tag{5.1}
$$



### 5.2 Lower edge

Since $D\ge486>27$ for sufficiently large retained indices,


$$
[x^a]F_i\equiv0\pmod{3^{10}}
\qquad(0\le a<27).
\tag{5.2}
$$



### 5.3 Upper edge: both neighboring intervals must be checked

The integer


$$
H/\Omega=3^9
$$


is odd. The two grid centers neighboring $H/2$ are


$$
c_-=\frac{H-\Omega}{2},
\qquad
c_+=\frac{H+\Omega}{2}.
$$



The upper endpoint of the lower interval is


$$
c_-+5D,
$$


and the lower endpoint of the next interval is


$$
c_+-5D.
$$



Let


$$
L=m-D=\frac{H-3D+1}{2}.
$$


Then


$$
L-(c_-+5D)=\frac{\Omega-13D+1}{2},
\tag{5.3}
$$


whereas


$$
(c_+-5D)-L=\frac{\Omega-7D-1}{2}.
\tag{5.4}
$$



The core window gives


$$
\Omega>512\cdot11^2D=61952D.
$$


Both differences are positive. Thus the next support interval lies entirely above the degree cutoff, while the preceding interval lies entirely below it. Therefore


$$
\deg\psi_i\le \frac{H-\Omega}{2}+5D.
$$


Multiplication by $x^D$, a degree-$D$ polynomial, yields


$$
\deg(F_i\bmod3^{10})
\le\frac{H-\Omega}{2}+6D.
\tag{5.5}
$$



The gap from $m$ is exactly


$$
m-\left(\frac{H-\Omega}{2}+6D\right)
=
\frac{\Omega-13D+1}{2}>9.
\tag{5.6}
$$



Consequently,


$$
\deg(F_i\bmod3^{10})\le m-9,
$$


and in particular


$$
[y^{m-k}]F_i\equiv0\pmod{3^{10}}
\qquad(0\le k<9).
\tag{5.7}
$$



Every equality and inequality in the coordinator’s proposed edge argument is therefore valid.

---

## 6. Closing $\Phi_R\in3^{11}M$ and $S_{\rm act}\in3^{17}M$

Reuse the established actual-producer statement


$$
R_{\rm prod}=3\mathscr R,
$$




$$
\mathscr R\equiv(y+1)x^{A-27}q(x)\pmod{3^{10}},
\qquad \deg q\le27.
\tag{6.1}
$$



Put $b=\beta+3\in\mathbb Z_3^\times$, and define


$$
T_{10}(x)=\sum_{r=0}^{9}\frac{(-3x)^r}{b^{r+1}}.
$$


Then


$$
(b+3x)T_{10}\equiv1\pmod{3^{10}}.
\tag{6.2}
$$



By the two proved edges,


$$
H_i=x^{-27}qF_iT_{10}\pmod{3^{10}}
$$


has an integral polynomial representative of degree at most


$$
-27+27+(m-9)+9=m.
$$


Thus


$$
\mathscr RF_i-Q_cH_i\in3^{10}\mathbb Z_3[y].
\tag{6.3}
$$



The complete functional preserves this congruence. Indeed, its cutoff satisfies


$$
4n-3=4H-4D+5<9H=3^{h+1},
$$


so every retained denominator has $3$-adic valuation at most $h$. Monic endpoint subtraction is integral, and the factorial summand is integral.

Decomposing $H_i$ in the integral basis $[W,F]$, complete-core orthogonality kills its $W$-part, while its residual part pairs through


$$
S_c\in3^{17}M.
$$


Hence


$$
\mathcal M(\mathscr RF_iF_j)\in3^{10}\mathbb Z_3.
$$


Therefore


$$
\boxed{\Phi_R\in3^{11}M.}
\tag{6.4}
$$



For the whole actual residual block, retain the exact identity


$$
S_{\rm act}=S_c+3^6\Phi_R-3^{13}\mathcal Q.
\tag{6.5}
$$



The independently reviewed A4turn19 result is


$$
\mathcal Q\in3^4M.
$$


That is already sufficient: all three terms of (6.5) belong to $3^{17}M$. Thus


$$
\boxed{S_{\rm act}\in3^{17}M.}
\tag{6.6}
$$



A1turn22’s stronger assertion $\mathcal Q\in3^5M$ is not needed for this conclusion. In particular, the present reconciliation does not silently enlarge the scope of the supplied review of the nonlinear calculation.

---

## 7. Stronger linear protection and its certified ceiling

### 7.1 The degree budget does not fail at precision $16$

For general $p$ in the archived scope, the same interval calculation gives


$$
\deg(F_i\bmod3^p)\le m-g_p,
$$


where


$$
g_p=\frac{\Omega_r-(p+3)D+1}{2},
\qquad r=\max(6,p).
\tag{7.1}
$$



The constant $C_r$ makes $g_p$ much larger than the degree $p-1$ of the reciprocal multiplier


$$
T_p(x)=\sum_{a=0}^{p-1}\frac{(-3x)^a}{(\beta+3)^{a+1}}.
$$


Thus polynomial-degree growth does not obstruct the multiplier argument at any $p\le16$.

In particular, at $p=r=16$,


$$
\Omega_{16}>147968D,
$$


and


$$
g_{16}=\frac{\Omega_{16}-19D+1}{2}>16.
\tag{7.2}
$$



### 7.2 Direct divided-producer reuse already gives $\Phi_R\in3^{17}M$

Let $\mathcal A=(A+1)!$. The established saturation bound for the coefficients $e_a$ of $3P_n-Q_c$ is


$$
v_3(e_a)\ge v_3(\mathcal A/a!).
$$



At $t=v_3(A)=5$,


$$
v_3\!\left(\frac{(A+1)!}{(A-k-1)!}\right)
=5+v_3(k!)
\qquad(k<243).
\tag{7.3}
$$


Since


$$
v_3(39!)=18,
$$


the coefficients of $\mathscr R=(3P_n-Q_c)/3^7$ below $x^{A-39}$ vanish modulo $3^{16}$. Its actual endpoint is also zero modulo $3^{16}$ eventually. Hence


$$
\mathscr R\equiv(y+1)x^{A-39}B(x)\pmod{3^{16}},
\qquad \deg B\le39.
\tag{7.4}
$$



Because $D\ge486$ and $g_{16}>15$, the same multiplier proof gives


$$
\Phi_{\mathscr R}\in3^{16}M,
\qquad
\Phi_R\in3^{17}M.
$$



### 7.3 The reviewed source reset improves this to $\Phi_R\in3^{18}M$

A4turn19 establishes


$$
R_{\rm prod}\equiv3\gamma(y+1)x^A\pmod9
$$


for an integral lift $\gamma$ of the unevaluated scalar $g_3$. Since


$$
Q_c\bmod3=(y+1)x^A,
$$


the polynomial


$$
J_2=\frac{R_{\rm prod}-3\gamma Q_c}{9}
\tag{7.5}
$$


is integral. This is an exact source reset, not a claim that $J_2$ is another signed producer.

Its degree and leading coefficient are


$$
\deg J_2\le A+2,\qquad [y^{A+2}]J_2=-\gamma.
\tag{7.6}
$$


That extra degree must be retained.

For $a<A$, the subtracted $Q_c$-term has no $x^a$-coefficient, so


$$
[x^a]J_2=e_a/3^8.
$$


Now


$$
v_3(42!)=14+4+1=19,
$$


and therefore


$$
v_3\!\left(\frac{(A+1)!}{(A-43)!}\right)=24.
$$


It follows that


$$
[x^a]J_2\equiv0\pmod{3^{16}}
\qquad(a\le A-43).
\tag{7.7}
$$



Its exact endpoint is


$$
J_2(-1)=-\frac{\xi_n\mathcal A^2}{3^8},
$$


which is zero modulo $3^{16}$ for sufficiently large retained indices. Since $x=-2$ is a unit at $y=-1$, monic division gives


$$
J_2\equiv(y+1)x^{A-42}B_2(x)\pmod{3^{16}},
\qquad \deg B_2\le43.
\tag{7.8}
$$



The extra degree in (7.6) accounts for the bound $43$, rather than $42$.

Using the precision-$16$ complete columns, define


$$
H_i=x^{-42}B_2F_iT_{16}\pmod{3^{16}}.
$$


This has an integral representative because $D\ge42$, and


$$
\deg H_i
\le -42+43+(m-g_{16})+15
=m-g_{16}+16
\le m.
$$


Therefore the complete multiplier argument proves


$$
\Phi_{J_2}\in3^{16}M.
\tag{7.9}
$$



Finally, (7.5) gives the exact pairing identity


$$
\Phi_R=3\gamma S_c+9\Phi_{J_2}.
$$


Since $S_c\in3^{17}M$,


$$
\boxed{\Phi_R\in3^{18}M.}
\tag{7.10}
$$



No value of $\gamma$ is needed. No producer computation has been rerun.

### 7.4 What “ceiling” means here

For the **stated $C_r$-based archive reuse**, the largest uniformly available precision on the retained window is $r=16$. Indeed,


$$
\frac{C_{17}}{C_{16}}
=3\frac{18^2}{17^2}
=\frac{972}{289}>2.
$$


But the window gives $H/D<2C_{16}$. Hence


$$
C_{17}D>H
$$


throughout that window.

Accordingly:

- the archived support certificate is uniformly available through precision $3^{16}$;
- direct divided-producer multiplication gives linear protection through $3^{17}$;
- the reviewed two-factor source reset gives $\Phi_R\in3^{18}M$;
- the available core bound $S_c\in3^{17}M$ also caps this reset argument at $3^{18}$, because of $3\gamma S_c$.

This is a **ceiling of the present certified argument**, not a theorem that a coefficient becomes nonzero at the next precision. The $C_r$ constants are sufficient, not necessary. A sharper use of the raw width inequalities would be a separate extension requiring its own proof.

At the reviewed nonlinear scope,


$$
S_{\rm act}-S_c
=3^6\Phi_R-3^{13}\mathcal Q\in3^{17}M.
$$


If A1turn22’s stronger $\mathcal Q\in3^5M$ is separately accepted at its full original-domain scope, then


$$
S_{\rm act}-S_c\in3^{18}M.
$$


Even that would leave the absolute conclusion $S_{\rm act}\in3^{17}M$ unless the core’s next digit were also controlled.

---

## 8. Reconciliation ledger

| Claim or earlier label | Reconciled status |
|---|---|
| Core operations require $v_3(j)\ge r-2$ | **False as a necessity for these operations.** The five proofs require only the weaker arithmetic and width hypotheses audited above. |
| Arbitrary-depth actual approximation $Q_n^{\rm loc}-Q_c\in3^{v_3(j)+2}\mathbb Z_3[y]$ | **Not established and not used.** Its earlier conditional label remains substantive. |
| $U=y^u$ versus $U=x^u$ invalidates the support argument | **No.** The integral Pascal change of basis preserves the actual projection polynomial and complete columns. |
| Ten-digit complete-core edge lemma unavailable in A1turn0 and A1turn22 | **A missing-source limitation, now resolved.** The full archived core support supplies both edges. |
| Producer locality by itself proves complete-column locality | **Still invalid.** The proof here uses complete core elimination. |
| $\Phi_R\in3^{11}M$ | **Now proved on the retained original family.** |
| $S_{\rm act}\in3^{17}M$ | **Now proved**, using the reviewed $\mathcal Q\in3^4M$. |
| Stronger linear protection | **Proved:** $\Phi_R\in3^{18}M$, using precision-$16$ core support and the reviewed integral source reset. |
| A1turn22’s $\mathcal Q\in3^5M$ | Not required here; its stronger reviewed scope must not be inferred from the supplied A4turn19 excerpt. |
| Unbounded precision on this fixed window | **Not established.** The stated $C_r$-certificate stops at $r=16$. |
| Core inverse loss, actual relative inverse alignment | **Genuine open mathematics.** |
| Distinguished cofactor nonvanishing | **Genuine open mathematics.** |
| Actual contents, least simultaneous clearer, final all-prime gcd, primitive denominator, whole-error decay | **Genuine open mathematics.** |

Classical sparse coefficient support and finite Neumann inversion are the established methods being reused. The new result is their original-domain reconciliation and the explicit consequences above, not a claim of a new general inversion method.

---

## 9. The next mathematical bottleneck

The local ten-digit edge obligation is closed. The inverse and relative-arithmetic obligations are not.

At the reviewed nonlinear scope, define the exact integral residual operator


$$
\Upsilon_{17}
=
\frac{\mathcal Q}{81}
-\frac{\Phi_R}{3^{11}}
-\frac{S_c}{3^{17}},
\qquad
S_{\rm act}=-3^{17}\Upsilon_{17}.
\tag{9.1}
$$


All three terms are retained. The new linear result implies


$$
\Upsilon_{17}
\equiv
\frac{\mathcal Q}{81}-\frac{S_c}{3^{17}}
\pmod3,
$$


but does not evaluate either remaining term.

A concrete follow-on lemma should address the actual pair


$$
\mathcal D_{0,17}=\det\Upsilon_{17},
$$




$$
\mathcal D_{1,17}
=
e_{\rm act}^T\operatorname{adj}(\Upsilon_{17})e_{\rm act}
-3^{17}d_{\rm act}\det\Upsilon_{17}.
\tag{9.2}
$$



> **Follow-on relative-pair lemma.**  
> On the same retained original indices, prove nonvanishing of the required determinants and distinguished bordered expression, and obtain a uniform law or bound for
> 

$$
> v_3(\mathcal D_{1,17})-v_3(\mathcal D_{0,17}).
>
$$


> Any core comparison must use an actual upper inverse-loss bound and the whole transported scalar, including cancellation with $d_{\rm act}$.

This is an open target, not an evaluated determinant formula.

The known implication


$$
S_c\in3^{17}M\quad\Longrightarrow\quad s_c\ge17
$$


is only a lower bound on inverse loss. It cannot pay an inverse division or establish


$$
S_c^{-1}(S_{\rm act}-S_c)\in3M.
$$



---

## 10. Primitive normalization and whole same-index error remain unchanged

The complete actual columns remain


$$
\widehat Z^{\,\rm act}
=
\widehat Z^{\,c}-3^6WE_{\rm act}^{-1}T_R.
$$


The terminal closure is not altered:


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$



Both exponential boundary columns, the logarithmic forcing $F/(1-z)$, every exterior $+1$, and the physical terminal remain part of the complete construction. None is discarded by the support proof.

After retaining the actual row contents, actual multiplier, and least simultaneous clearer, write


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over **all primes**. For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{10.1}
$$



No local depth improvement changes this normalization or evaluates its right-hand side.

An irrationality proof by this route still requires, at the **same infinite original indices**,


$$
0<|q(e+\pi)-p|\longrightarrow0,
$$


with $q$ the actual primitive denominator after the final all-prime gcd.

---

## 11. Exact-arithmetic requirements

**No new computation is needed for the results proved in this report.** In particular:

- neither completed producer receipt is reopened;
- the optional $452$-coordinate endpoint computation is not needed;
- no finite core-column scan is needed to certify the ten-digit edges;
- no inverse or cofactor value is claimed to have been computed.

The small arithmetic used in the proof is explicitly checkable:


$$
v_3(39!)=18,\qquad v_3(42!)=19,
$$




$$
C_{10}<C_{16},\qquad C_{17}>2C_{16}.
$$


These are symbolic valuation and integer comparisons, not new original-family computational evidence.

Any later finite evaluation of (9.2) must specify a concrete original $(j,h)$, the complete finite matrices, transported endpoint, diagonal term, and precision before every nonunit division. Its verifiable outputs would concern that finite tuple only. Uniform conclusions would still require a proved structural reduction.

---

## Final result and proof status

The supplied full core audit resolves the apparent contradiction between the archived support theorem and the later ten-digit “unproved” labels.



$$
\boxed{
\begin{gathered}
\text{The core-only theorem applies when }v_3(j)=4;\\
\text{the complete ten-digit lower and upper edges hold;}\\
\Phi_R\in3^{11}M,\qquad S_{\rm act}\in3^{17}M.
\end{gathered}
}
$$



A further explicit use of precision-$16$ core support and the reviewed integral source reset proves


$$
\boxed{\Phi_R\in3^{18}M.}
$$



The true remaining bottleneck is no longer the ten-digit edge lemma. It is the relative arithmetic and nonvanishing of the complete residual determinant/cofactor pair, followed by the actual all-prime primitive denominator and the whole nonzero same-index error.



$$
\boxed{\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$


