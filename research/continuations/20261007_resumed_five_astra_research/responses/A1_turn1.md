> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Core-only support closure, stronger Schur protection, and the remaining actual inverse problem

## Executive conclusions

The coordinator’s proposed two-edge implication is valid. The apparent discrepancy between the archived LOW bases $1,y,\ldots,y^{D-1}$ and $1,x,\ldots,x^{D-1}$, where $x=y-1$, is harmless: it is an integral unimodular change of basis in the same eliminated subspace and leaves the complete corrected columns unchanged.

More importantly, the five core operations can be proved without the old condition


$$
v_3(j)\ge r-2.
$$


That condition belonged to the proposed transfer from the core polynomial to the actual polynomial. It is not needed by the core support argument. Below I give the missing verification directly from the complete finite core blocks, including the LOW projection, finite HIGH inverse, lower-edge returns, and physical upper endpoint $m$.

Consequently, on the retained sufficiently large original indices,


$$
\boxed{
[x^a]F_i\equiv0\pmod{3^{10}}\quad(0\le a<27),
\qquad
[y^{m-k}]F_i\equiv0\pmod{3^{10}}\quad(0\le k<9).
}
$$


Thus the previously outstanding implication closes:


$$
\boxed{\Phi_R\in3^{11}M,\qquad S_{\rm act}\in3^{17}M.}
$$



There is a further consequence of checking the actual inequalities rather than merely quoting the archived sufficient constants. The five-operation proof works under its displayed width inequality, which is substantially weaker than $C_rD<H$. On the present window it works through $r=20$. Together with the already established producer saturation and complete quadratic cancellation, this gives


$$
\boxed{
S_c\in3^{21}M,\qquad
\Phi_R\in3^{20}M,\qquad
S_{\rm act}-S_c\in3^{18}M,\qquad
S_{\rm act}\in3^{18}M.
}
$$


This is a new deduction, not an application of the archived $r=20$ statement at hypotheses it does not satisfy.

For the inverse problem, I construct an explicit, precision-paid, structured approximate inverse of the **actual eliminated block**. It uses a finite triangular LOW inverse and the actual finite HIGH Neumann expansion; it is not merely a restatement of an abstract certificate.

That construction does **not** yet invert the normalized residual block. In fact, normalization at depth $17$ cannot produce a unit residual matrix, since the stronger conclusion above makes that normalized matrix zero modulo $3$. At depth $18$, the first residual digit is exactly


$$
\boxed{
-\frac{S_{\rm act}}{3^{18}}
\equiv \frac{\mathcal Q}{3^5}\pmod3.
}
$$


Its full radical, inverse loss, and distinguished endpoint contraction remain unevaluated. I do not claim to have constructed the requested residual inverse.

No producer computation is rerun or requested. No conclusion about rationality or irrationality of $e+\pi$ follows.

---

## 1. Original domain and exact finite objects

Retain


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$


and


$$
m=2^{2j-1},\qquad n=4^j+1,\qquad A=n-2=2m-1.
$$


Let


$$
H=3^{h-1},\qquad D=H-A,
$$


with the unchanged window


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad
C_{16}=147968\,3^{15}.
$$



Since


$$
84645=81\cdot1045,\qquad 3\nmid1045,
$$


the progression has


$$
v_3(j)=4,\qquad v_3(A)=v_3(4^j-1)=5.
$$


For sufficiently large retained tuples, $h-1>5$, so


$$
v_3(D)=5.
$$


Also $D$ is even. In particular,


$$
D\ge 2\cdot3^5=486.
$$



Put


$$
d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1,
\qquad x=y-1.
$$


The finite columns are exactly


$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m).
$$


No coordinate beyond $Y_m$ or $z_{\nu-1}$ is added.

The complete functional is


$$
\mathcal M(G)=
-\frac{3^h}{4}\mathfrak f(G)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](G-G(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^s)=(2s)!.
\tag{1.1}
$$


Its cutoff is exactly $2v+1\le4n-3$.

The core polynomial is


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A,
$$


and


$$
G_c(f,g)=\mathcal M(Q_cfg).
$$


Writing $W=[U\ Y]$, define


$$
E_c=G_c(W,W),\qquad C_c=G_c(W,Z),
$$




$$
F=Z-WE_c^{-1}C_c.
\tag{1.2}
$$


Thus $F_i$ denotes the **complete** core-orthogonal column, not a truncated producer response.

The actual form is


$$
G_{\rm act}=G_c+3^6K,\qquad
K(f,g)=\mathcal M(R_{\rm prod}fg).
$$


The retained exact identity is


$$
S_{\rm act}=S_c+3^6\Phi_R-3^{13}\mathcal Q,
\tag{1.3}
$$


where


$$
(\Phi_R)_{ij}=\mathcal M(R_{\rm prod}F_iF_j),
$$


and $\mathcal Q$ is the complete contraction through the actual eliminated inverse.

The already closed turn22 result is


$$
\mathcal Q\in3^5M_\nu(\mathbb Z_3).
\tag{1.4}
$$


Its proof retains the six-coordinate LOW source, HIGH feedback, actual HIGH boundary response, and terminal return. Nothing below replaces that complete contraction by an uncorrected source.

---

## 2. The LOW-basis discrepancy does not change the columns

The archive uses


$$
U^{(y)}=(1,y,\ldots,y^{D-1}),
$$


whereas the retained formulation uses


$$
U^{(x)}=(1,x,\ldots,x^{D-1}).
$$



There is an integral triangular matrix $P$, with diagonal entries $1$, such that


$$
U^{(y)}=U^{(x)}P.
$$


Indeed,


$$
y^a=(x+1)^a=\sum_{u=0}^a\binom au x^u.
$$


Hence $P\in\operatorname{GL}_D(\mathbb Z)$.

Let $T=\operatorname{diag}(P,I_{\rm HIGH})$. Then


$$
W^{(y)}=W^{(x)}T,\quad
E_c^{(y)}=T^TE_c^{(x)}T,\quad
C_c^{(y)}=T^TC_c^{(x)}.
$$


Therefore


$$
W^{(y)}(E_c^{(y)})^{-1}C_c^{(y)}
=
W^{(x)}(E_c^{(x)})^{-1}C_c^{(x)}.
\tag{2.1}
$$



Thus the complete columns $F_i$ are identical as polynomials. In particular, the change of LOW basis cannot delete or alter a terminal correction.

The distinction still matters inside a calculation: a remainder modulo $x^D$ must be expressed in whichever LOW basis is being used. Equation (2.1), rather than an identification of the two coordinate vectors, is the correct justification.

---

## 3. A core-only closure theorem with its actual hypotheses

For an integer $r\ge6$, set


$$
\Omega=\frac{H}{3^{r-1}},\qquad
W_r=4(r+1)(D+2).
$$



The following is the scope directly proved by the five operations.

### Theorem 3.1 — Finite core closure

Suppose


$$
D\ge6,\qquad 6\mid D,\qquad \beta\equiv1\pmod3,
\qquad h\ge r+2,
\tag{3.1}
$$


and


$$
\boxed{W_r+2D+2<\Omega/8.}
\tag{3.2}
$$


Then:

1. the complete finite eliminated core block is invertible, with
   

$$
E_c^{-1}\in3^{-1}M(\mathbb Z_3);
$$


2. for $1\le p\le r$, there are integral polynomial representatives
   

$$
F_i\equiv x^D\psi_i(y)\pmod{3^p},
   \tag{3.3}
$$


   satisfying
   

$$
\deg\psi_i\le m-D,\qquad
   \operatorname{supp}_y\psi_i
   \subseteq I_\Omega(pD/2);
   \tag{3.4}
$$


3. the undivided core Schur complement satisfies
   

$$
S_c\in3^{r+1}M_\nu(\mathbb Z_3).
   \tag{3.5}
$$



Here


$$
I_\Omega(w)=
\{a\Omega+u:a\in\mathbb Z,\ |u|\le w\}.
$$



No condition $v_3(j)\ge r-2$ occurs in this theorem.

### 3.1 All poles and the factorial term

Let


$$
r_1=\frac{H-1}{2},\qquad r_*=\frac{3H-1}{2}.
$$


Since $Q_c$ contains $y+1$, the endpoint subtraction is exact:


$$
\frac{Q_cfg-Q_cfg(-1)}{y+1}
=x^A(\beta+3y)fg.
$$



The pole at denominator $3H=3^h$ gives the top extraction at $r_*$. All remaining denominators can be written uniquely as


$$
cH/3^t,\qquad 0\le t\le h-1,
$$


where $c$ is positive, odd, prime to $3$, and satisfies the original cutoff. Their weights are


$$
3^{t+1}c^{-1}.
$$


Thus every normalized lower extraction has its stated $3^t$ weight. No pole is omitted.

The normalized factorial contribution carries $3^{h-1}$. Under $h\ge r+2$, it vanishes modulo $3^r$, including in the blocks divided once by $3$. It remains part of the exact blocks.

### 3.2 Coefficient grids

For $0<k<H$,


$$
v_3\binom Hk=h-1-v_3(k).
\tag{3.6}
$$


Also, for


$$
a_k=[z^k](1-z)^{-H}=\binom{H+k-1}{k},
$$




$$
v_3(a_k)\ge h-1-v_3(k).
\tag{3.7}
$$


Consequently, at precision $3^q$, the relevant coefficient arrays below degree $H$ are supported on multiples of


$$
H/3^{q-1}.
$$


For $q\le r$, these are integer multiples of $\Omega$.

Every pole that can survive at that precision lies on an odd half-grid relative to $\Omega$:


$$
\frac{(2a+1)\Omega-1}{2}.
\tag{3.8}
$$


The unit $c^{-1}$ affects coefficients, not support. This is the prime-power support mechanism used in the archive; no new automaticity theorem is being asserted.

### 3.3 Exact block formulas

Use the notation


$$
E_c=
\begin{pmatrix}
3L&3X\\
3X^T&E_Y
\end{pmatrix},
\qquad
C_c=
\binom{3B}{3V^T}.
\tag{3.9}
$$


Let


$$
(E_0)_{ab}=[y^{r_*}]x^Ay^{a+b},
\qquad d\le a,b\le m.
$$


Define the complete HIGH-return operator


$$
\mathcal F=
\frac{E_Y-E_0}{3}-X^TL^{-1}X.
\tag{3.10}
$$


Then


$$
K_c:=E_Y-3X^TL^{-1}X=E_0+3\mathcal F.
\tag{3.11}
$$



The complete columns are therefore


$$
\boxed{
F
=
Z-UL^{-1}B
-
(Y-UL^{-1}X)\,
3(E_0+3\mathcal F)^{-1}
(V^T-X^TL^{-1}B).
}
\tag{3.12}
$$


This formula exhibits both the LOW projection and every HIGH-to-LOW return.

### 3.4 The finite LOW and HIGH inverses

In the $x$-LOW basis, modulo $3$,


$$
L_{ab}=[y^{r_1}]x^{H-D+a+b}.
$$


Hence


$$
L_{ab}=0\quad(a+b\ge D),\qquad
L_{a,D-1-a}=1.
\tag{3.13}
$$


Thus $L$ is a unit matrix over $\mathbb Z_3$.

The exact finite HIGH inverse is


$$
\boxed{
R_{ab}:=(E_0^{-1})_{ab}
=
[z^{D+r_1-a-b}](1-z)^D(1-z)^{-H}.
}
\tag{3.14}
$$


To check that this is a finite inverse, reverse one coordinate of $E_0$. The resulting triangular Toeplitz matrix has generating polynomial $(1-z)^A$; its finite triangular inverse is obtained from $(1-z)^{-A}$. Since $A=H-D$, this gives (3.14).

Every nonnegative coefficient index used in (3.14) is below $H$:


$$
D+r_1-a-b\le D+r_1-2d<H.
\tag{3.15}
$$


Thus the inverse-series support estimate is used only in its proved range.

### 3.5 Operation 1: complete $V$-support

Since


$$
i+b\le\nu-1+m=r_1-1,
$$


the top $\beta x^H$ contribution to $V_{ib}$ is absent. The extra $3y$ reaches the top pole only at


$$
i=\nu-1,\qquad b=m.
$$


This is the physical terminal corner.

Every lower contribution is an extraction from


$$
x^H(\beta+3y)y^{i+b}.
$$


Its surviving HIGH index is therefore half-grid-supported with width at most $\nu+1=D/2$.

For


$$
d\le b\le d+W_r,
$$


the local shifts are bounded by $W_r+2D-2$, so (3.2) separates them from every retained odd half-grid pole. Hence


$$
V_{ib}\equiv0\pmod{3^r}
\quad(d\le b\le d+W_r).
\tag{3.16}
$$



### 3.6 Operation 2: finite inverse copies

A coefficient $a_{k\Omega}$ in (3.14), acting on a half-grid input $e_b$, contributes before intersection with HIGH a copy


$$
a_{k\Omega}\,y^{r_1-b-k\Omega}x^D.
\tag{3.17}
$$


Its starting exponent is on the integer grid, with the same local width as the input.

The finite interval $[d,m]$ has two effects:

* At the upper boundary, the integer-grid copy cannot straddle $m$, because $m$ lies near an odd half-grid and the width is much smaller than the gap.
* At the lower boundary, only copies near grid point $0$ can be cut. Their surviving parts lie in a lower-edge interval $[d,d+w]$.

Thus the finite inverse produces complete internal polynomial copies plus lower-edge vectors. It introduces no new coordinate above $m$, and no width increase.

### 3.7 Operation 3: the complete return on an internal copy

Let


$$
p=y^{k\Omega+s}x^D
$$


be wholly supported in HIGH. Then $x^Ap=x^Hy^{k\Omega+s}$.

For a LOW index $u<D$, the top contribution to $Xp$ is absent because


$$
\deg\bigl(x^A(\beta+3y)p\,y^u\bigr)
\le H+m<r_*.
\tag{3.18}
$$


Every lower contribution is separated by the integer/half-grid gap. Thus


$$
Xp\equiv0\pmod{3^r}.
\tag{3.19}
$$


The LOW correction in the **complete** operator $\mathcal Fp$ therefore vanishes at that precision.

Writing $c_0=(\beta-1)/3$, the remaining terms in $\mathcal Fp$ are:

* $c_0E_0p$;
* the top extraction with the extra factor $y$;
* all normalized lower-pole extractions;
* the factorial term, already zero at the required precision.

Their support is half-grid support, together with an upper-edge vector, with width increased by at most one.

### 3.8 Operation 4: the actual lower-edge projection

For $0\le s\le w$, divide monically:


$$
y^{d+s}=r_s+x^Dq_s,\qquad \deg r_s<D,
$$


where


$$
q_s=
\sum_{a=0}^{\nu+s}
\binom{D+a-1}{a}y^{\nu+s-a},
\qquad
\deg q_s=\nu+s.
\tag{3.20}
$$



The difference between the LOW forces of $y^{d+s}$ and $r_s$ is obtained from


$$
x^H(\beta+3y)q_sy^u.
$$


Its shifts lie within the proved gap; its top extraction is absent by degree. Therefore


$$
L^{-1}Xe_{d+s}\equiv r_s\pmod{3^r}.
\tag{3.21}
$$



This proves that the actual LOW projection, not an imposed projection, turns a lower-edge monomial into $x^Dq_s$.

In $\mathcal Fe_{d+s}$, the top terms are confined to the last $s+2$ HIGH coordinates. The lower terms have local shifts of width at most $\nu+s+1$. Thus a return increases width by at most


$$
\nu+1=D/2.
\tag{3.22}
$$



### 3.9 Operation 5: the terminal return is finite and exact

For $b=m-s$, formula (3.14) gives


$$
D+r_1-a-b=d+s-a.
$$


Hence


$$
R_{a,m-s}=0\qquad(a>d+s).
\tag{3.23}
$$


Thus an upper-edge vector of width $w$ returns to the actual lower edge of width $w$, exactly.

This is where the physical terminal is retained. An infinite inverse or an enlarged HIGH interval would not be an acceptable substitute.

### 3.10 Corrected-column support and Schur closure

Modulo $3^p$, the HIGH correction in (3.12) uses only


$$
3\sum_{a=0}^{p-2}(-3)^a(R\mathcal F)^aR.
\tag{3.24}
$$


The initial width is $D/2$; each return adds at most $D/2$. After LOW projection, the quotient of a lower-edge term has degree at most its edge width plus $\nu$. Therefore the safe quotient width is


$$
pD/2.
$$


This proves (3.3)–(3.4).

The direct normalized residual block and $B$ vanish modulo $3^r$, by the same coefficient gaps and top-degree bounds. In the residual Schur form, every retained HIGH walk is killed on the left by $V$:

* complete internal copies miss the half-grid support and the upper terminal corner;
* lower-edge vectors are killed by (3.16).

Thus $S_c/3\in3^rM$, proving (3.5).

All inverse operations used above are unit inversions after the single displayed LOW factor $3$. The proof uses no divisibility of $D$ by $3^{r-1}$, and no condition $v_3(j)\ge r-2$. This completes the missing core-only hypothesis audit.

---

## 4. The coordinator’s two-edge implication passes

At $p=r=10$, the archived sufficient constant is


$$
C_{10}=512\cdot11^2\cdot3^9.
$$


Since


$$
\frac{C_{16}}{C_{10}}
=
\frac{17^2}{11^2}3^6>1,
$$


the retained window implies $C_{10}D<H$, and hence the width condition.

For sufficiently large original tuples, $h\ge12$. Theorem 3.1 gives


$$
F_i\equiv x^D\psi_i(y)\pmod{3^{10}},
$$




$$
\deg\psi_i\le m-D,\qquad
\operatorname{supp}_y\psi_i\subseteq I_\Omega(5D),
\qquad
\Omega=H/3^9.
\tag{4.1}
$$



### 4.1 Lower edge

Because $D\ge486>27$,


$$
[x^a]F_i\equiv0\pmod{3^{10}}
\qquad(0\le a<27).
\tag{4.2}
$$



### 4.2 Upper edge: the support variable is $y$

Here the support statement concerns $\psi_i(y)$, not an $x$-coefficient support statement.

Since


$$
H/\Omega=3^9
$$


is odd, the integer-grid center immediately below $H/2$ is


$$
\frac{H-\Omega}{2}.
$$


The next center is $(H+\Omega)/2$. Its interval begins above the allowed degree


$$
m-D=\frac{H-3D+1}{2},
$$


because $\Omega>7D+1$.

Therefore the highest possible support interval for $\psi_i$ ends at


$$
\frac{H-\Omega}{2}+5D.
$$


Multiplication by $x^D=(y-1)^D$ gives


$$
\deg F_i\bmod3^{10}
\le
\frac{H-\Omega}{2}+6D.
\tag{4.3}
$$


The gap from $m$ is


$$
\frac{\Omega-13D+1}{2}.
\tag{4.4}
$$



Numerically, the retained width bound gives


$$
\frac{\Omega}{D}>
\frac{C_{16}}{3^9}
=
147968\cdot3^6
=
107868672.
$$


Thus (4.4) is much larger than $9$. In particular,


$$
[y^{m-k}]F_i\equiv0\pmod{3^{10}}
\qquad(0\le k<9).
\tag{4.5}
$$



### 4.3 Consequence for the actual linear force

Reuse the established producer congruence


$$
\mathscr R:=R_{\rm prod}/3
\equiv(y+1)x^{A-27}q(x)\pmod{3^{10}},
\qquad \deg q\le27.
$$


Let $b=\beta+3$, a unit, and


$$
T(x)=\sum_{s=0}^9\frac{(-3x)^s}{b^{s+1}}.
$$


Then


$$
(b+3x)T(x)\equiv1\pmod{3^{10}}.
$$



By (4.2) and (4.5),


$$
H_i=x^{-27}q(x)F_iT(x)\pmod{3^{10}}
$$


has an integral polynomial representative of degree at most $m$. Hence


$$
\mathscr RF_i\equiv Q_cH_i\pmod{3^{10}}.
$$


The whole functional is integral on the retained cutoff, and complete core orthogonality gives


$$
\mathcal M(Q_cH_iF_j)\in3^{17}\mathbb Z_3.
$$


Therefore


$$
\Phi_{\mathscr R}\in3^{10}M,\qquad
\Phi_R\in3^{11}M.
$$


Using (1.3)–(1.4),


$$
\boxed{S_{\rm act}\in3^{17}M.}
$$



This closes the original two-edge obligation without any producer calculation.

---

## 5. A stronger consequence of the audited width inequality

The preceding proof establishes Theorem 3.1 under (3.2), not merely under the more conservative condition $C_rD<H$.

This distinction permits a further deduction, but it must be made explicitly. I do **not** claim that the retained window satisfies $C_{20}D<H$; it does not do so uniformly.

At $r=20$,


$$
\Omega_{20}=H/3^{19},
$$


and the retained window gives


$$
\frac{\Omega_{20}}D>\frac{147968}{81}.
$$


Meanwhile,


$$
8(W_{20}+2D+2)=688D+1360.
$$


Since


$$
\frac{147968}{81}-688=\frac{92240}{81}
$$


and $D\ge486$,


$$
688D+1360<\Omega_{20}.
$$


For sufficiently large original indices, $h\ge22$. Theorem 3.1 therefore yields


$$
\boxed{S_c\in3^{21}M}
\tag{5.1}
$$


and


$$
F_i\equiv x^D\psi_i(y)\pmod{3^{20}},
\qquad
\operatorname{supp}_y\psi_i\subseteq I_{\Omega_{20}}(10D).
\tag{5.2}
$$



### 5.1 Producer saturation at this precision

This step reuses the established saturation theorem, not an arbitrary-depth approximation $Q_{\rm act}-Q_c\in3^{v_3(j)+2}\mathbb Z_3[y]$.

For $v_3(A)=5$, the terminal width at producer precision $3^{20}$ is


$$
\kappa_{20}
=
\min\{k\ge0:5+v_3(k!)\ge26\}
=45.
$$


Indeed,


$$
v_3(44!)=19,\qquad v_3(45!)=21.
$$


Since $45<3^5$ and $45<D$, the stated factorial-tail formula applies. The endpoint factorial condition also holds for sufficiently large original indices.

Thus


$$
R_{\rm prod}
\equiv(y+1)x^{A-45}B_{20}(x)\pmod{3^{20}},
\qquad \deg B_{20}\le45.
\tag{5.3}
$$



Using (5.2), the endpoint-subtracted product quotient is congruent to


$$
x^H\,x^{D-45}B_{20}(x)\psi_i(y)\psi_j(y).
$$


Its non-$x^H$ factor has support in


$$
I_{\Omega_{20}}(21D).
$$


Since


$$
21D<(\Omega_{20}-1)/2,
$$


it misses every contributing odd half-grid pole. The factorial contribution vanishes at this precision. Hence


$$
\boxed{\Phi_R\in3^{20}M.}
\tag{5.4}
$$



Combining (5.1), (5.4), and the closed theorem $\mathcal Q\in3^5M$ gives


$$
\boxed{
S_{\rm act}-S_c\in3^{18}M,\qquad
S_{\rm act}\in3^{18}M.
}
\tag{5.5}
$$



No additional producer residue was needed.

---

## 6. An actual structured approximate inverse of the eliminated block

This section constructs a genuine approximation to the actual finite eliminated inverse. It does not assume residual nonsingularity.

Write


$$
E_{\rm act}=
\begin{pmatrix}
3L_{\rm act}&3X_{\rm act}\\
3X_{\rm act}^T&E_{Y,\rm act}
\end{pmatrix}.
$$


All three blocks are the complete actual blocks, including factorial and pole contributions.

### 6.1 An explicit triangular LOW model

Let $N_D$ be the $D\times D$ upper shift and $J_D$ the reversal matrix. From the calculation leading to (3.13),


$$
L_{\rm act}
\equiv
(I+N_D)^{-(r_1+1)}J_D\pmod3.
$$


Define the integral unit lift


$$
L_*=(I+N_D)^{-(r_1+1)}J_D.
$$


Because $N_D^D=0$, both powers are finite polynomials in $N_D$, and


$$
L_*^{-1}=J_D(I+N_D)^{r_1+1}.
\tag{6.1}
$$



Put


$$
D_L=L_*^{-1}(L_{\rm act}-L_*)\in3M.
$$


For $a\ge1$, define


$$
P_a=\sum_{t=0}^{a-1}(-D_L)^tL_*^{-1}.
\tag{6.2}
$$


Then


$$
P_a\equiv L_{\rm act}^{-1}\pmod{3^a},
$$


with both left and right residual identities verifiable by multiplying the finite geometric series.

This is an explicit finite LOW approximate inverse, not an unspecified matrix $B$.

### 6.2 The actual finite HIGH approximation

The actual HIGH Schur block is


$$
K_{\rm act}
=
E_{Y,\rm act}
-3X_{\rm act}^TL_{\rm act}^{-1}X_{\rm act}
=
E_0+3\mathcal F_{\rm act},
\tag{6.3}
$$


where


$$
\mathcal F_{\rm act}
=
\frac{E_{Y,\rm act}-E_0}{3}
-X_{\rm act}^TL_{\rm act}^{-1}X_{\rm act}.
$$



For a requested precision parameter $s\ge1$, use $P_{s+1}$ and set


$$
\mathcal F^{[s]}
=
\frac{E_{Y,\rm act}-E_0}{3}
-X_{\rm act}^TP_{s+1}X_{\rm act},
$$




$$
H_s=
\sum_{t=0}^{s-1}
(-3R\mathcal F^{[s]})^tR,
\tag{6.4}
$$


where $R=E_0^{-1}$ is the exact finite matrix (3.14).

Then


$$
H_s\equiv K_{\rm act}^{-1}\pmod{3^s}.
$$


The HIGH interval remains $[d,m]$ throughout every multiplication. In particular, (6.4) includes the actual terminal-to-lower-edge returns.

### 6.3 Assembly and the paid division

Define


$$
\mathscr J_s=
\begin{pmatrix}
P_{s+1}+3P_{s+1}X_{\rm act}H_sX_{\rm act}^TP_{s+1}
&
-3P_{s+1}X_{\rm act}H_s\\[1mm]
-3H_sX_{\rm act}^TP_{s+1}
&
3H_s
\end{pmatrix}.
\tag{6.5}
$$


The exact block inverse formula gives


$$
\boxed{
\mathscr J_s\equiv3E_{\rm act}^{-1}\pmod{3^{s+1}}.
}
\tag{6.6}
$$


Consequently,


$$
\mathscr J_sE_{\rm act}\equiv
E_{\rm act}\mathscr J_s\equiv3I\pmod{3^{s+1}}.
\tag{6.7}
$$



Thus the actual eliminated inverse loss is paid explicitly by one factor $3$. Every other inverse in the construction is a unit inverse, either the finite triangular inverse (6.1) or the finite HIGH inverse (3.14).

### 6.4 Complete columns, endpoint, and diagonal observation

Write the actual mixed block as


$$
C_{\rm act}=3C_1,
\qquad
\mathscr J=3E_{\rm act}^{-1}.
$$


Then


$$
\widehat Z^{\,\rm act}=Z-W\mathscr J C_1,
\tag{6.8}
$$




$$
S_{\rm act}=G_{\rm act}(Z,Z)-3C_1^T\mathscr JC_1.
\tag{6.9}
$$



For $w=W(-1)^T$,


$$
e_{\rm act}=Z(-1)^T-C_1^T\mathscr Jw,
\tag{6.10}
$$




$$
d_{\rm act}=\frac13w^T\mathscr Jw.
\tag{6.11}
$$


The last division is real and must be retained:


$$
d_{\rm act}\in3^{-1}\mathbb Z_3
$$


is sufficient; its integrality is not assumed.

These formulas construct the complete actual transported endpoint from the same actual inverse used in the Schur complement.

---

## 7. The residual inverse and distinguished cofactor remain open

The construction in §6 is not an inverse of the residual matrix. This distinction is essential.

Define the actual depth-$18$ normalized residual operator


$$
\Upsilon_{18}=-\frac{S_{\rm act}}{3^{18}}.
$$


By the exact Schur identity,


$$
\boxed{
\Upsilon_{18}
=
\frac{\mathcal Q}{3^5}
-\frac{\Phi_R}{3^{12}}
-\frac{S_c}{3^{18}}.
}
\tag{7.1}
$$


The divisions are legitimate by (1.4), (5.1), and (5.4). In particular,


$$
\boxed{
\Upsilon_{18}\equiv\frac{\mathcal Q}{3^5}\pmod{27}.
}
\tag{7.2}
$$



This identifies the actual leading residual operator, not merely a sufficient edge condition.

### 7.1 Why the core inverse is not yet available as a substitute

If $S_c$ is nonsingular, (5.1) implies


$$
s_c\ge21.
$$


The proved absolute perturbation bound is only


$$
S_{\rm act}-S_c\in3^{18}M.
$$


It therefore does not pay the core inverse loss in


$$
S_c^{-1}(S_{\rm act}-S_c).
$$



Also,


$$
-S_{\rm act}/3^{17}\in3M.
$$


Thus an attempted unit inverse at normalization depth $17$ necessarily fails. This is an original-family obstruction, not an illustrative external matrix example.

At depth $18$, the precise outstanding object is


$$
K_{18}:=\left(\mathcal Q/3^5\right)\bmod3.
\tag{7.3}
$$


Its rank and full radical have not been determined.

### 7.2 The whole distinguished expression

Put


$$
\mathcal D_0=\det\Upsilon_{18},
$$




$$
\boxed{
\mathcal D_1=
e_{\rm act}^T\operatorname{adj}(\Upsilon_{18})e_{\rm act}
-
3^{18}d_{\rm act}\det\Upsilon_{18}.
}
\tag{7.4}
$$


Since $v_3(d_{\rm act})\ge-1$, the second term is integral.

The exact block identities are


$$
\det G_{\rm act}
=
\det E_{\rm act}\,(-3^{18})^\nu\mathcal D_0,
\tag{7.5}
$$




$$
v^T\operatorname{adj}(G_{\rm act})v
=
\det E_{\rm act}\,(-3^{18})^{\nu-1}\mathcal D_1.
\tag{7.6}
$$


They remain valid even if $\Upsilon_{18}$ is singular.

Modulo $3$, the retained endpoint is


$$
e_0=\bigl((-1)^i\bigr)_{0\le i<\nu},
$$


and therefore


$$
\mathcal D_1\equiv e_0^T\operatorname{adj}(K_{18})e_0\pmod3.
\tag{7.7}
$$


Neither this scalar nor $\det K_{18}$ has been evaluated.

### Concrete follow-on lemma

The next useful lemma is:

> **Complete first residual-digit lemma.** Determine the full matrix $K_{18}$ in (7.3), its radical and a nondegenerate complement, and the transported endpoint on that decomposition. If the radical is nonzero, derive the next exact Schur operator and endpoint using the actual complement inverse. Evaluate the whole bordered expression, including its diagonal term, at a precision exceeding its possible cancellation.

A nonsingular $K_{18}$, together with a nonzero scalar in (7.7), would immediately provide a unit normalized residual inverse and a nonzero distinguished cofactor. A singular $K_{18}$ requires the full radical/complement step; it cannot be inverted formally.

This obligation has not been closed by naming $\mathcal Q$, nor by the structured eliminated inverse in §6.

---

## 8. Primitive arithmetic and the whole same-index error

Restore the actual multiplier and actual rational matrix:


$$
Q_n=\lambda Q_n^{\rm loc},\qquad
R_{\rm rat}=\frac{4\lambda}{3^h}G_{\rm act},
$$




$$
H_{\rm complete}
=
R_{\rm rat}+(e+\pi)Q_n(-1)vv^T.
$$


Retain


$$
\beta_0=\det R_{\rm rat},\qquad
\beta_1=Q_n(-1)v^T\operatorname{adj}(R_{\rm rat})v.
$$



When $\mathcal D_0\ne0$,


$$
\frac{\beta_1}{\beta_0}
=
-\frac{3^{h-18}Q_n^{\rm loc}(-1)}4
\frac{\mathcal D_1}{\mathcal D_0}.
\tag{8.1}
$$


The actual producer endpoint is not replaced by the zero core endpoint.

After the actual row contents, actual multiplier, and least simultaneous clearer $\ell_{\rm clr}$, preserve


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
\boxed{g_\ell=\gcd(|A_\ell|,|B_\ell|)}
$$


over all primes. For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole error remains


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{8.2}
$$



If both local determinants are nonzero, the exact local denominator formula is


$$
v_3(q)=
\max\!\left\{
0,\,
h-18+v_3(Q_n^{\rm loc}(-1))
+v_3(\mathcal D_1)-v_3(\mathcal D_0)
\right\}.
\tag{8.3}
$$


The common depth contributes one factor to the determinant ratio, not $18\nu$ factors to the primitive denominator.

No result here evaluates the actual row contents, replaces the least simultaneous clearer, determines the all-prime gcd, or proves nonvanishing or decay of (8.2).

In particular, neither exponential boundary column, the logarithmic forcing $F/(1-z)$, any exterior $+1$, nor the physical terminal equation is removed. The retained terminal closure


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right)
$$


remains part of the complete construction.

The global requirement is still


$$
0<|q(e+\pi)-p|\longrightarrow0
$$


at the same infinite original indices, with the actual primitive $q$.

---

## 9. Bounded exact arithmetic: what is and is not needed

### 9.1 No computation is needed for the support conclusion

The two-edge theorem, the deletion of the unnecessary core-only valuation hypothesis, and the strengthened bounds in §5 are symbolic consequences of the displayed finite formulas.

Neither closed producer receipt is reopened. The optional higher endpoint producer interface is not requested.

### 9.2 A new finite residual check, if authorized

For one coordinator-selected original tuple $(j,h)$, first verify exactly:

* the progression and retained window;
* $h\ge22$;
* the definitions of $D,d,\nu,m$;
* the complete actual producer coefficients.

The bounded inputs are:

1. those integers and the exact finite polynomial $R_{\rm prod}$;
2. the complete functional (1.1);
3. the core and actual finite blocks on the unchanged coordinate intervals;
4. the explicit inverse constructions (6.1)–(6.5).

To determine $K_{18}$, a safe precision interface is:

* compute the complete core columns $F_i\bmod3^7$;
* compute
  

$$
T_R=\bigl(\mathcal M(R_{\rm prod}wF_i)\bigr)_{w,i}
  \pmod{3^7};
$$


* divide by the proved factor $3$, obtaining $T_1=T_R/3\bmod3^6$;
* compute $\mathscr J=3E_{\rm act}^{-1}\bmod3^6$ using $\mathscr J_5$;
* assemble the whole contraction
  

$$
\mathcal Q=T_1^T\mathscr JT_1\pmod{3^6};
$$


* verify its proved divisibility by $3^5$, then output
  

$$
K_{18}=\mathcal Q/3^5\bmod3.
$$



Expected verifiable outputs are:

1. exact residual checks for the LOW and finite HIGH inverse approximations;
2. the complete matrix $K_{18}$;
3. its rank and a basis of its full radical;
4. a verified nondegenerate complement, if present;
5. the residue
   

$$
e_0^T\operatorname{adj}(K_{18})e_0;
$$


6. all intermediate divisibility checks before division.

No particular rank or nonzero residue is predicted.

This is a finite certificate for that tuple only. It is not a proof of an infinite-family inverse theorem, and it does not determine the final primitive error.

---

## 10. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| LOW $y$-basis versus LOW $x$-basis preserves complete columns | Proved exactly |
| Removal of $v_3(j)\ge r-2$ for core operations only | Proved from the complete finite block formula |
| Finite HIGH inverse, LOW projection, and terminal return | Audited and derived above |
| Strong two-edge theorem modulo $3^{10}$ | Proved on the retained sufficiently large original family |
| $\Phi_R\in3^{11}M$, $S_{\rm act}\in3^{17}M$ | Proved |
| Width-based extension to $r=20$ | New proved deduction; not an illicit use of $C_{20}D<H$ |
| $S_c\in3^{21}M$, $\Phi_R\in3^{20}M$, $S_{\rm act}\in3^{18}M$ | Proved using the closed complete quadratic theorem |
| Structured approximate inverse of the actual eliminated block | Constructed with all divisions displayed |
| Structured inverse of the normalized residual block | Not constructed |
| Full radical of $K_{18}=\mathcal Q/3^5\bmod3$ | Open |
| Nonzero distinguished cofactor | Open |
| Actual all-prime gcd, primitive denominator, and whole nonzero decaying error | Open |

The archived support machinery does resolve the turn0 edge obligation. Its use is legitimate because the five core operations do not require the old high valuation of $j$, and the LOW-basis change preserves the complete polynomial columns exactly.

The inverse problem does not disappear. The stronger support conclusion actually makes its location clearer: depth $17$ is not a unit normalization, and the first presently exposed actual residual operator is the complete quadratic digit


$$
\mathcal Q/3^5\bmod3.
$$


Determining its full radical and whole endpoint contraction is the precise next local bottleneck.

Beyond that local problem, the research objective still requires the actual all-prime primitive denominator and a nonzero whole error tending to zero along the same infinite original indices.



$$
\boxed{\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$


