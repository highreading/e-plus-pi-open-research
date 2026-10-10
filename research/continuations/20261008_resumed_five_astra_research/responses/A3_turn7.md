> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent ternary audit and one further paid producer digit

## Abstract

The rationality or irrationality of $e+\pi$ remains unresolved.

The principal claims of A4 Turn 8, Sections 3–8, pass this audit at their stated scope. In particular:

- the extended $p=22$ dual is a dual to the **physical coordinate $Y_m$**;
- the last middle column has the residual $3\mathfrak t_{22}e_{Y_m}$, which must be corrected;
- the compact filtered norms, shortened multiplier, actual inverse-image criterion, and exact Schur difference are valid;
- the natural $p=26$ physical representative generally has precision exactly $25$, not $26$;
- after all stated prefix, $J$- and rank-$b$ inverse payments, the reported comparison
  

$$
T_{\mathrm{act},\mathrm{red}}-T_{c,\mathrm{red}}\in3^6\operatorname{Mat}(\mathbb Z_3)
$$


  follows.

The coordinator’s $p=25$ bulk transport also passes. Its proposed last-middle extension is valid: the exceptional residual is indeed


$$
3\mathfrak t_{25}e_{Y_m}\pmod{3^{25}},
$$


and the associated stationary correction is sufficiently divisible. This gives a shorter, nonoverflowing route to the selected-input part of A4’s comparison, though not by itself to the whole eliminated $J$-block.

There is one further evaluated original-family refinement. Paying one additional admissible $p=25$ Frobenius digit, and using a mixed observation already available in the original finite objects, gives


$$
\boxed{
T_{\mathrm{act},\mathrm{red}}-T_{c,\mathrm{red}}
\in3^7\operatorname{Mat}(\mathbb Z_3).
}
$$


More precisely,


$$
\boxed{\Delta_{GG}\in27\operatorname{Mat}(\mathbb Z_3),
\qquad
\Delta_{bG}\in9\operatorname{Mat}(\mathbb Z_3).}
$$


This is a local matrix result on the entire retained amplitude space. It does not evaluate the actual returned endpoint or the $1/9$ diagonal return, and it implies no primitive-denominator gain.

---

## 1. Original domain, finite objects, and retained inputs

### 1.1 The original indices are unchanged

Every uniform assertion below concerns sufficiently large members of exactly the original family


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


with


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15},
$$


and


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


and the exact relation


$$
4^j=243(3^{26}-1)P-243r+1.
$$



Write


$$
x=y-1,\qquad Q=27P=3^{h-29},\qquad b=Q-N_0,\qquad R=\frac b2.
$$


Then


$$
D=10Q-b,\qquad .064<\frac bQ<.073.
$$


Also set


$$
\chi=P-R,\qquad .0145<\frac{\chi}{P}<.136.
$$



No independently selected $P,r$, or $R$ is used. The retained density theorem supplies infinitely many indices in this same original subwindow; it is not used to authorize any other parameter family.

### 1.2 The finite basis and physical cutoff

The coordinates are


$$
U_s=x^s\quad(0\le s<D),
$$




$$
z_i=x^Dy^i\quad(0\le i<\nu),
\qquad \nu=\frac D2-1,
$$




$$
Y_t=y^t\quad(d\le t\le m),
\qquad d=D+\nu,
$$


and $W=[U\ Y]$.

There is one monic polynomial of each degree $0,\ldots,m$ in $[U,z,Y]$. Thus this basis is integral unimodular relative to the monomial basis. In particular, coefficientwise divisibility and divisibility in this actual finite basis are equivalent for polynomials of degree at most $m$.

The physical terminal is $Y_m$. The last middle direction $z_{\nu-1}$ is a different coordinate.

The complete functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{K_{\mathrm{phys}}}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad \mathfrak f(y^t)=(2t)!,
$$


where


$$
K_{\mathrm{phys}}=2n-2=2H-2D+2.
$$


Its largest pole denominator is


$$
2K_{\mathrm{phys}}+1=4H-4D+5<3^{h+1}.
\tag{1.1}
$$



Consequently the fixed, truncated functional is integral:


$$
\mathcal M(\mathbb Z_3[y])\subseteq\mathbb Z_3.
\tag{1.2}
$$


Indeed, monic division by $y+1$ preserves integral coefficients, every displayed pole weight is integral, and the factorial contribution is in $3^h\mathbb Z_3$.

For reference, put


$$
\Lambda_h(P)=3^h\sum_{v=0}^{K_{\mathrm{phys}}}\frac{[y^v]P}{2v+1}.
$$


The only physical pole of valuation $h$ is $3H=3^h$, at coefficient index


$$
n_3=\frac{3H-1}{2}.
\tag{1.3}
$$


This observation will be used only with the fixed cutoff (1.1).

### 1.3 The complete producer remains unchanged

Let


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A\in1+9\mathbb Z_3,
$$


and


$$
G_c(f,g)=\mathcal M(Q_cfg).
$$


Write


$$
E_c=G_c(W,W),\qquad
F[p]=x^Dp-WE_c^{-1}G_c(W,x^Dp),\qquad \deg p<\nu.
$$



The actual producer is


$$
Q_{\mathrm{act}}=Q_c+c\mathscr R,\qquad c=3^7.
$$


Its coefficients retain the entire signed force:


$$
[x^a](3^7\mathscr R)
=-\frac{F_{\mathrm{fac}}}{a!}(t_a+\xi v_a),
\qquad F_{\mathrm{fac}}=(n-1)!,
\tag{1.4}
$$


where


$$
t=3nh_{\mathrm{vec}}+(b_{\mathrm{force}}+6)e_{n-1}
+\frac{2b_{\mathrm{force}}}{n-1}e_{n-2},
\qquad b_{\mathrm{force}}=-n-66,
$$




$$
u_a=\frac{F_{\mathrm{fac}}(-2)^a}{a!},\qquad v=T_n^{-1}u,
$$




$$
h_{\mathrm{vec}}
=T_n^{-1}\left(\binom{n+a}{a}\gamma_{n+a}\right)_{a=0}^{n-1},
$$




$$
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},\qquad
\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1},
\quad \gamma_0=1,\ \gamma_1=0.
$$


The archived signed normalization of $\xi$, including its ternary-unit property, is reused, not recalculated. In particular,


$$
\mathscr R(-1)=-\frac{\xi F_{\mathrm{fac}}^2}{3^7}
$$


is retained.

The paid precision-$31$ support theorem gives


$$
\mathscr R=(y+1)x^{A-72}q_{31}(x)\pmod{3^{31}},
\qquad \deg q_{31}\le72.
\tag{1.5}
$$


The entire reciprocal is


$$
r_{31}(y)=\beta^{-1}\sum_{k=0}^{30}
\left(-\frac{3y}{\beta}\right)^k,
\qquad
(\beta+3y)r_{31}\equiv1\pmod{3^{31}}.
\tag{1.6}
$$


No coefficient of $q_{31}$, no term of $r_{31}$, and no part of $\xi v$ is suppressed.

Set


$$
\mathcal B(f,g)=\mathcal M(\mathscr Rfg).
$$



### 1.4 Closed results used at their original scope

The following are retained established inputs:

1. $E_c^{-1}\in3^{-1}\operatorname{Mat}(\mathbb Z_3)$.
2. The admitted mixed filters for $16\le p\le25$.
3. The finite Jacobi moment identities and unit exceptional moment.
4. Integral original corrected columns and the normalization $S_c/3^{26}$.
5. A4 Turn 5’s complete corrected-pairing compression through $3^{31}$, **only for input degrees at most $\nu-2$**.
6. The integral unit-prefix inverse and the exact lift $X_G=3P_G+9Z$.
7. H2 and its original rank-$b$ unit block.
8. The audited physical-terminal theorem
   

$$
[y^m]\mathcal F_a\equiv-3^{27}\delta_{a,R}\pmod{3^{28}},
   \qquad \gamma_c=0.
   \tag{1.7}
$$


9. A1 Turn 5’s exact radical, saturated basis, and complete-core unit complement.

No new general filter theorem or unbounded-precision assertion is being imported.

---

## 2. Audit of the physical $p=22$ certificate

For a filter parameter $s$, use


$$
N_s=3^{s-1},\qquad M_s=\frac{N_s-1}{2},\qquad
L_s=3^{h-s},
$$




$$
\rho_s(y)=R_{N_s}(y^{L_s}).
$$


The retained finite filter facts are


$$
R_N\in\mathbb Z_3[Y],\qquad R_N\equiv1\pmod9,
$$


and, if


$$
(Y-1)^NR_N(Y)=\sum_j a_jY^j,
$$


then


$$
\sum_j\frac{a_j}{2(j+q)+1}=0\qquad(0\le q<M),
\tag{2.1}
$$


while


$$
\mathfrak t_s=3^s\sum_j\frac{a_j}{2(j+M)+1}\in\mathbb Z_3^\times.
\tag{2.2}
$$


No numerical reevaluation of $\mathfrak t_s$ is needed.

For $s=22$,


$$
L_{22}=3^7Q.
$$



### 2.1 Extended terminal dual

Define


$$
\Omega_k
=y^{d+k}-\sum_{u=0}^{D-1}\binom{d+k}{u}x^u
=x^Ds_k,
$$


where


$$
s_k(y)=\sum_{\ell=0}^{\nu+k}g_\ell y^{\nu+k-\ell},
\qquad
g_\ell=\binom{D+\ell-1}{\ell},
$$


and $g_\ell=0$ for $\ell<0$.

This quotient follows either by monic division by $x^D$, or by taking the polynomial part of


$$
y^{\nu+k}(1-y^{-1})^{-D}.
$$



For $0\le k\le21$,


$$
\Omega_k\rho_{22}\in W\mathbb Z_3.
$$


The constant filter term is already in $W$; every nonconstant term starts above $d+21$. Its top degree satisfies


$$
m-\deg(\Omega_k\rho_{22})
=\frac{L_{22}-4D+3-2k}{2}>0.
\tag{2.3}
$$



The residual asserted in A4 is correct:


$$
G_c(W,\Omega_k\rho_{22})
\equiv
\mathfrak t_{22}
\sum_{r=0}^{k+1}
(\beta g_{k-r}+3g_{k-r+1})e_{Y_{m-r}}
\pmod{3^{22}}.
\tag{2.4}
$$



Here are the necessary scope checks.

- For a LOW row, the nonsparse factor has degree at most
  

$$
d+k\le d+21<\frac{L_{22}-1}{2},
$$


  so it misses every pole residue that can survive this modulus.
- For a HIGH row, its degree is at most
  

$$
\frac{H-1}{2}+22.
$$


  Since $22<L_{22}$, no macro moment after the first exceptional moment is reached.
- The exceptional completed moment ends at
  

$$
(4N_{22}-1)L_{22}=4H-L_{22}<4H-4D+5.
$$


- All $Y_{m-r}$, $0\le r\le22$, are actual HIGH rows.
- The factorial part is in $3^h$, beyond the modulus.

Put


$$
\vartheta=-\frac3\beta,\qquad
D^\vee_{22}
=\frac{\rho_{22}}{\beta\mathfrak t_{22}}
\sum_{k=0}^{21}\vartheta^k\Omega_k.
$$


The finite convolution is


$$
\begin{aligned}
\sum_{k=0}^{21}\vartheta^k
(\beta g_{k-r}+3g_{k-r+1})
&=\beta\sum_{k=0}^{21}\vartheta^k
(g_{k-r}-\vartheta g_{k-r+1})\\
&=\beta g_{-r}-\beta\vartheta^{22}g_{22-r}.
\end{aligned}
$$


Therefore


$$
G_c(W,D^\vee_{22})-e_{Y_m}\in3^{22}M.
\tag{2.5}
$$



The exact complete-core terminal dual


$$
D^\vee=WE_c^{-1}e_{Y_m}
$$


satisfies


$$
D^\vee-D^\vee_{22}\in3^{21}W.
\tag{2.6}
$$


Thus the one-digit inverse payment is explicit, and this is a dual to the actual physical coefficient $Y_m$.

### 2.2 The last middle residual is not zero

For $\deg p<\nu$, let


$$
\tau(p)=[y^{\nu-1}]p.
$$


The same finite moment calculation gives


$$
G_c(W,x^Dp\rho_{22})
\equiv3\mathfrak t_{22}\tau(p)e_{Y_m}
\pmod{3^{22}}.
\tag{2.7}
$$



Indeed, only the $3y$ part of $\beta+3y$, the top coefficient of $p$, and the row $Y_m$ can reach exponent


$$
m+\nu=\frac{H-1}{2}.
$$


The $\beta$-term remains one degree short.

Consequently


$$
\widetilde F[p]
=x^Dp\rho_{22}
-3\mathfrak t_{22}\tau(p)D^\vee_{22}
=x^D\pi_p\rho_{22},
$$


where


$$
\pi_p=p-\frac{3\tau(p)}{\beta}
\sum_{k=0}^{21}\vartheta^ks_k,
\qquad \deg\pi_p\le\nu+21,
\tag{2.8}
$$


has residual in $3^{22}$, and


$$
\boxed{\widetilde F[p]-F[p]\in3^{21}W.}
\tag{2.9}
$$



Both polynomials lie below $m$, and their difference from the original middle input belongs to the actual $W$. Thus A4’s extension includes the last middle column without confusing it with $Y_m$.

---

## 3. Audit of the compact norms, inverse image, and shortened multiplier

### 3.1 Compact filtered norm

Let $B\in\mathbb Z_3[y]$ have


$$
\deg B\le2D+101.
$$


Then


$$
\boxed{\Lambda_h(x^HB\rho_{22}^2)\in3^{22}\mathbb Z_3.}
\tag{3.1}
$$



To verify this, use


$$
x^H\equiv(y^{L_{22}}-1)^{N_{22}}\pmod{3^{22}}.
$$


Write


$$
A_0(Y)=(Y-1)^{N_{22}}R_{N_{22}}(Y)^2
=\sum_q a_qY^q.
$$


Then


$$
A_0(1)=0,\qquad \deg A_0=2N_{22}-1.
$$



Every macro term is physical:


$$
(2N_{22}-1)L_{22}+\deg B
\le2H-L_{22}+2D+101
\le K_{\mathrm{phys}}.
\tag{3.2}
$$



For $c_s=2s+1$, the original large-index inequalities give


$$
c_s\le4D+203<81Q=3^{h-25},
\qquad v_3(c_s)\le h-26.
$$


Since $v_3(L_{22})=h-22$,


$$
v_3\!\left(
3^h\left(\frac1{c_s+2qL_{22}}-\frac1{c_s}\right)
\right)\ge30.
\tag{3.3}
$$


Replacing each denominator by $c_s$ therefore changes the macro sum by a multiple of $3^{30}$; the remaining sum is zero because $\sum_q a_q=0$. The Frobenius error limits the asserted conclusion to $3^{22}$. This proves (3.1) with the finite cutoff intact.

### 3.2 Actual inverse-image criterion

Modulo $3$, every LOW row of $E_c$ vanishes. For $\deg u<D$ and $\deg w\le m$, the relevant numerator degree is at most


$$
A+(D-1)+m=H+m-1<n_3.
$$


Thus it misses the only unit-weight physical pole.

For HIGH coordinates,


$$
G_c(y^i,y^j)
\equiv[y^{n_3-i-j}]x^A\pmod3.
$$


The entries vanish if $i+j<m+d$, and the anti-diagonal $i+j=m+d$ has coefficient $1$. Reversing columns produces a triangular unit matrix.

Now


$$
E_{\mathrm{act}}=E_c+c\mathcal B(W,W).
$$


Because $cE_c^{-1}\mathcal B(W,W)\in3^6M$,


$$
E_{\mathrm{act}}^{-1}\in3^{-1}M,
\qquad
E_{\mathrm{act}}^{-1}E_c,\ E_cE_{\mathrm{act}}^{-1}\in M.
\tag{3.4}
$$


Also $E_{\mathrm{act}}\equiv E_c\pmod3$.

It follows that an integral vector $a$ with LOW coordinates divisible by $3$ satisfies


$$
\boxed{E_{\mathrm{act}}^{-1}a\in M.}
\tag{3.5}
$$


Indeed, choose an integral HIGH vector $z$ with
$E_{\mathrm{act}}z\equiv a\pmod3$, and write


$$
E_{\mathrm{act}}^{-1}a
=z+E_{\mathrm{act}}^{-1}(a-E_{\mathrm{act}}z).
$$


The second term is integral by (3.4). This criterion does not assert that every integral vector has an integral inverse image.

### 3.3 Shortened multiplier and its actual $W$-part

For the representative (2.8), put


$$
H_p=x^{D-72}q_{31}r_{31}\pi_p.
$$


Then


$$
\deg H_p\le d+51,\qquad x^{D-72}\mid H_p.
$$



There is an exact integral decomposition


$$
H_p=B_p+x^Db_p,
\qquad \deg b_p<\nu,
\tag{3.6}
$$


with $B_p$ in the span of LOW coordinates and $y^d,\ldots,y^{d+51}$, and $x^{D-72}\mid B_p$.

A concrete construction is:

1. subtract the high coefficients using $\Omega_0,\ldots,\Omega_{51}$;
2. divide the remaining polynomial monically by $x^D$;
3. place the remainder in $B_p$.

Every subtraction and division is integral. Multiplication by $\rho_{22}$ preserves $B_p\in W$, because the nonconstant terms start above $d+51$, and


$$
m-\deg(B_p\rho_{22})\ge\frac{L_{22}-4D-99}{2}>0.
$$



Using the terminal correction for $b_p$, one obtains $U_p\in W$ such that


$$
\mathcal B(W,F[p])=E_cu_p+3^{21}e_p,
\tag{3.7}
$$


where $u_p$ is the coordinate vector of $U_p$, $e_p$ is integral, and


$$
U_p=x^{D-72}a_p(y)\rho_{22}(y),
\qquad \deg a_p\le\nu+123.
\tag{3.8}
$$



The coefficient relation underlying (3.7) is


$$
\mathscr R\,\widetilde F[p]\equiv Q_cH_p\rho_{22}\pmod{3^{31}}.
$$


The $3^{21}$ error in (3.7) records the replacement (2.9); it is not hidden inside the support congruence.

### 3.4 Exact Schur difference and A4’s original payment

Let $\mathbf h_p=\mathcal B(W,F[p])$. Since the $F[p]$ are exactly core-orthogonal to $W$, the actual-minus-core middle Schur difference is exactly


$$
\delta S(p,q)
=c\mathcal B(F[p],F[q])
-c^2\mathbf h_p^TE_{\mathrm{act}}^{-1}\mathbf h_q.
\tag{3.9}
$$



The compact lemma gives the raw filtered bounds needed in A4. In particular,


$$
G_c(U_p,U_q)\in3^{22}\mathbb Z_3,
\qquad
\mathcal B(U_p,U_q)\in3^{22}\mathbb Z_3,
\tag{3.10}
$$


because their compact factors have degrees at most


$$
2D+101,\qquad 2D+100,
$$


respectively.

The identity


$$
E_cE_{\mathrm{act}}^{-1}E_c
=
E_c-c\mathcal B(W,W)
+c^2\mathcal B(W,W)E_{\mathrm{act}}^{-1}\mathcal B(W,W)
\tag{3.11}
$$


is exact. A4’s LOW inverse-image argument makes the last contraction integral. Therefore its contribution, including the outer $c^2$ in (3.9), is in $3^{28}$. The cross errors from (3.7) are in $3^{35}$, and the error-error term is in $3^{55}$.

Together with A4’s bound


$$
\mathcal B(F[p],F[q])\in3^{21}\mathbb Z_3,
$$


this proves its reported


$$
\boxed{S_{\mathrm{act}}-S_c\in3^{28}M}
\tag{3.12}
$$


on the entire original middle space.

Thus Sections 3–4 of A4 pass. Section 7 below will extract one additional digit from the same construction.

---

## 4. Audit of the $p=26$ transport and its genuine overflow loss

### 4.1 Virtual residual and physical representative

For $p=26$,


$$
L_{26}=27Q,\qquad N_{26}=3^{25}.
$$


For every integral input with $\deg p\le\nu-3$, let


$$
V[p]=x^Dp\rho_{26}.
$$



The A1 residual proof extends to these inputs with exactly this degree hypothesis.

- A LOW nonsparse factor has degree at most $d-3<L_{26}$; its only possible active macro moment is $q=0$, which vanishes exactly.
- A HIGH nonsparse factor has degree at most
  

$$
m+\nu-2=\frac{H-1}{2}-2,
$$


  so the exceptional moment is missed.
- Every completed ordinary moment ends by
  

$$
(4N_{26}-3)L_{26}=4H-81Q,
$$


  inside the physical cutoff.
- The first Frobenius correction, after replacing the filter by $1$ at cost $3^{28}$, has degree at most
  

$$
n_3-9Q-2.
$$


  It misses the unit-weight pole and gains the required digit.

Hence


$$
G_c(W,V[p])\in3^{27}M.
\tag{4.1}
$$



Only the top filter term can cross $m$. Its coefficient $r_{\mathrm{top}}$ has valuation $26$. If


$$
O[p]=[y^{>m}](y^{M_{26}L_{26}}x^Dp),
\qquad
\widehat V[p]=V[p]-r_{\mathrm{top}}O[p],
$$


then


$$
\widehat V[p]-x^Dp\in W,\qquad \deg\widehat V[p]\le m,
$$


but the residual is guaranteed only in $3^{26}$. Therefore


$$
\boxed{\widehat V[p]-F[p]\in3^{25}W.}
\tag{4.2}
$$



This is the correct inverse payment.

### 4.2 The degree-$m+30$ multiplier is paid before observation

For


$$
p_a=x^ba(y)y^{k_0}(y^{3Q}+3),
\qquad k_0=\frac{3Q+1}{2},
\qquad \deg a\le R,
$$


one has


$$
\deg p_a\le p_{\max}=\frac{9Q+3b+1}{2},
$$


and


$$
\nu-3-(p_{\max}+30)=\frac{Q-4b-69}{2}>0.
\tag{4.3}
$$



A4’s monic remainder subtraction from $\widehat V[p_a]$ is legitimate. The resulting $F^*[a]$ satisfies


$$
\deg F^*[a]\le m,\qquad x^{D+b}\mid F^*[a],
$$




$$
F^*[a]-\mathcal F[a]\in3^{25}\mathbb Z_3[y]_{\le m}.
\tag{4.4}
$$


The subtracted remainder need not be LOW: its degree is below $D+b$. What is valid, and sufficient, is its coefficientwise divisibility by $3^{26}$ in the whole actual finite basis.

Now


$$
L^*[a]=x^{-72}q_{31}r_{31}F^*[a]
$$


is a polynomial because $b\ge72$, and $\deg L^*[a]\le m+30$.

The crucial assertion is not this degree bound but


$$
[y^{>m}]L^*[a]\in3^{26}\mathbb Z_3[y].
\tag{4.5}
$$


It follows because $F^*[a]$ differs from its divisible virtual trial by $3^{26}$, monic division by $x^{72}$ preserves that divisibility, and the corresponding virtual multiplier is $x^Dp'_a\rho_{26}$ with $\deg p'_a\le\nu-3$. Its overflow again comes only from the top filter coefficient.

After clipping above $m$,


$$
\widehat L^*[a]-F[p'_a]\in3^{25}\mathbb Z_3[y]_{\le m}.
\tag{4.6}
$$



Thus A4 never needs to apply an original finite-space mixed observation to an unpaid degree-$>m$ vector.

The complete coefficient identity


$$
\mathscr R F^*[a]\equiv Q_cL^*[a]\pmod{3^{31}}
$$


then gives


$$
\mathcal B(W,\mathcal F[a])\in3^{25}M,
$$




$$
\mathcal B(F[p],\mathcal F[a])\in3^{25}\mathbb Z_3
\quad(\deg p<\nu).
\tag{4.7}
$$


For a two-sided replacement, both linear errors are in $3^{25}$, and the quadratic error is in $3^{50}$. Multiplication by the actual producer factor $3^7$ is retained.

Substitution in (3.9) proves


$$
\boxed{\delta S(p,\Psi[a])\in3^{32}\mathbb Z_3.}
\tag{4.8}
$$



### 4.3 The lost $p=26$ digit is genuinely detected in the original LOW space

For the exact radical generators


$$
g_s=(1-y)^{2\chi}y^s,
$$


the top-filter overflow has, modulo $3$, the form


$$
O_s\equiv
y^{m+5Q-R+s}x^{2\chi}(y^Q-1).
\tag{4.9}
$$


Indeed,


$$
x^{10Q}\equiv y^{10Q}-y^{9Q}-y^Q+1\pmod3,
$$


and $s+2\chi\le R$ places precisely the $9Q$- and $10Q$-bands above $m$.

Choose the original LOW row


$$
u_s=241P-s-1.
$$


It is admissible, since $s<P$ and


$$
D-u_s=27P+2\chi+s+1>0.
$$


Using $R+\chi=P$,


$$
A+2\chi+Q=H-241P,
$$


and


$$
n_3-(m+5Q-R+s)=H-s-1.
$$


Thus the extraction at the unit-weight pole is the leading coefficient of $x^{H-s-1}$, namely $1$:


$$
G_c(x^{u_s},O_s)\equiv1\pmod3.
$$



The closed top-filter unit is retained:


$$
r_{\mathrm{top}}/3^{26}\equiv-1\pmod3.
$$


Consequently


$$
\frac{G_c(x^{u_s},\widehat V[g_s])}{3^{26}}
\equiv1\pmod3.
\tag{4.10}
$$



Every pairing of an original LOW row with an integral polynomial of degree at most $m$ is divisible by $3$. Since the corrected column is LOW-orthogonal, (4.10) proves


$$
\widehat V[g_s]-\mathcal F[g_s]\notin3^{26}\mathbb Z_3[y]_{\le m}.
$$


Together with (4.2), its precision is exactly $25$.

A4’s corrected claim passes. An assertion of physical precision $26$ would fail at these explicit original rows.

---

## 5. Audit of the coordinator’s $p=25$ bulk transport

### 5.1 The mixed observation is valid in the original objects

The retained observation is


$$
\mathcal B(F[p],w)\in3\mathbb Z_3
\qquad(w\in W\mathbb Z_3,\ \deg p<\nu).
\tag{5.1}
$$



It can also be checked directly from the audited $p=22$ representative:


$$
F[p]\equiv x^Dp\pmod3.
$$


Modulo $3$, the numerator for $\mathcal B(W,F[p])$ has degree at most


$$
A-72+72+D+m+(\nu-1)
=H+m+\nu-1=n_3-1.
$$


It therefore misses the only unit-weight physical pole. This validates (5.1) for the complete producer, including the last middle input.

### 5.2 One-sided substitution and monic transport

Let


$$
L=L_{25}=81Q,\qquad V[p]=x^Dp\rho_{25},
\qquad \deg p\le\nu-32.
$$


The admitted $p=25$ residual gives


$$
V[p]-F[p]\in3^{24}W.
$$


Therefore, for any corrected $F[q]$,


$$
\mathcal B(F[p],F[q])
\equiv\mathcal B(V[p],F[q])\pmod{3^{25}},
\tag{5.2}
$$


using (5.1). Only one argument has been replaced.

The physical gap is


$$
m-\deg V[p]\ge\frac{L-4D+7}{2}>20Q,
$$


so multiplication by the full degree-$30$ reciprocal remains below $m$.

Put


$$
L[p]=x^{D-72}q_{31}r_{31}p\,\rho_{25}.
$$


Then


$$
\mathscr R V[p]\equiv Q_cL[p]\pmod{3^{31}},
\qquad \deg L[p]\le m.
$$


Both complete products paired with $F[q]$ have degree at most $2n-1$.

Now divide monically by $x^D$:


$$
x^{D-72}q_{31}r_{31}p=x^Dp'+u,
$$




$$
\deg p'\le\deg p+30\le\nu-2,\qquad \deg u<D.
\tag{5.3}
$$


The remainder is an actual LOW polynomial. Moreover,


$$
u\rho_{25}\in W,
$$


because nonconstant terms start at $L>d$, and


$$
m-\deg(u\rho_{25})
\ge\frac{L-3D+3}{2}>25Q.
\tag{5.4}
$$


Likewise, $x^Dp'\rho_{25}-x^Dp'\in W$. Hence


$$
L[p]-x^Dp'\in W
$$


and, exactly,


$$
G_c(L[p],F[q])=G_c(F[p'],F[q]).
\tag{5.5}
$$



This is a finite monic quotient-and-remainder argument. It does not apply compression to an inadmissible $x^{D-72}$ input.

For $\deg q\le\nu-2$, the retained compression theorem applies. Its small polynomial


$$
B=x^D(\beta+3y)p'q
$$


has degree at most $2D-5$. Every denominator $2s+1<40Q$ has valuation at most $h-26$; hence every coefficient term is in $3^{26}$. Thus


$$
G_c(F[p'],F[q])\in3^{26}\mathbb Z_3.
$$


Combining this with (5.2)–(5.5) proves the reported bulk theorem


$$
\boxed{
\mathcal B(F[p],F[q])\in3^{25}\mathbb Z_3,
\quad
\deg p\le\nu-32,\quad \deg q\le\nu-2.
}
\tag{5.6}
$$



### 5.3 The candidate last-middle extension passes

Let $q=y^{\nu-1}$. Its trial is still physical:


$$
m-\deg V[q]=\frac{L-4D+5}{2}>0.
$$


The actual residual is


$$
\boxed{
r_q:=G_c(W,V[q])
\equiv3\mathfrak t_{25}e_{Y_m}\pmod{3^{25}}.
}
\tag{5.7}
$$



The verification is the $p=25$ version of Section 2:

- the LOW nonsparse degree is $d-1<(L-1)/2$;
- the largest HIGH exponent is $m+\nu=(H-1)/2$;
- only $3y\cdot y^{\nu-1}$ at $Y_m$ reaches that exponent;
- the exceptional completed moment ends at
  

$$
4H-L=4H-81Q<4H-4D+5;
$$


- the complete factorial term is beyond the stated precision.

Because $\mathfrak t_{25}$ is a unit, this residual has valuation exactly $1$ at $Y_m$. It is not an ordinary residual in $3^{25}$.

For an ordinary $p'$, the exact stationary identity is


$$
G_c(F[p'],F[q])
=
G_c(V[p'],V[q])-r_{p'}^TE_c^{-1}r_q.
\tag{5.8}
$$


The inverse payment is


$$
25-1+1=25.
$$



More explicitly, the original terminal counterterm is


$$
3\mathfrak t_{25}\,r_{p'}^TE_c^{-1}e_{Y_m}.
\tag{5.9}
$$


It is retained in (5.8), not set to zero.

The raw filtered pairing has pole polynomial


$$
x^HB\rho_{25}^2,
\qquad
B=x^D(\beta+3y)p'q,
\qquad \deg B\le2D-4<\frac{L-1}{2}.
$$


Modulo $3^{25}$, its sparse part is a polynomial in $y^L$. Every surviving pole requires coefficient residue $(L-1)/2$ modulo $L$, which the support of $B$ misses. Its maximum macro degree is


$$
2H-L+2D-4\le K_{\mathrm{phys}}.
$$


Thus the raw pairing is in $3^{25}$, and (5.8) proves the same bound for the corrected pairing.

Therefore (5.6) extends to **all** original $q$ with $\deg q<\nu$.

This does not extend the compression formula through $3^{31}$ to the last middle column. It establishes only the stated weaker divisibility, with its terminal counterterm paid.

### 5.4 What this simplifies in A4’s proof

For the prescribed one-lift inputs,


$$
p_a=x^by^{k_0+a}(y^{3Q}+3),
$$




$$
\nu-32-\max_a\deg p_a=\frac{Q-4b-67}{2}>0.
$$


Thus the bulk theorem applies to every amplitude, every exact radical combination, and every saturated complement combination.

Because $b\ge72$, their multiplier has no LOW remainder:


$$
x^{D-72}q_{31}r_{31}p_a=x^Dp'_a.
$$


The admitted $p=25$ residual then gives


$$
\mathcal B(W,\mathcal F[a])\in3^{24}M.
$$


Together with the direct source bound $3^{25}$, the exact Schur formula gives


$$
\delta S(p,\Psi[a])\in3^{32}.
$$



Hence the $p=25$ argument, after its last-middle extension is verified, is a shorter valid substitute for the selected-input estimate (4.8). It avoids the $p=26$ overflow construction entirely for that purpose.

It still needs the whole-middle estimate from Sections 2–3 to control changes in the eliminated $J$-block.

---

## 6. One additional admissible $p=25$ digit

The preceding audit proves the coordinator’s stated result. A further fixed digit is available without introducing a new filter or crossing the physical boundary.

### 6.1 Two-term Frobenius expansion at $p=25$

Put


$$
N=3^{24},\qquad L=81Q,\qquad Z=y^{L/3}=y^{27Q},\qquad Y=y^L.
$$


There is an integral polynomial $E_2$, of degree at most $H$, such that


$$
\boxed{
x^H=(Y-1)^N+3^{25}E_1+3^{26}E_2,
\qquad
E_1=Z(1-Z)(Y-1)^{N-1}.
}
\tag{6.1}
$$


Also


$$
\deg E_1=H-27Q.
$$



Here is the coefficient payment. Since


$$
x^{L/3}=Z-1+3A(y)
$$


for an integral polynomial $A$, raising to $3N=3^{25}$ changes $(Z-1)^{3N}$ only by $3^{26}$. This follows from


$$
v_3\binom{3^{25}}k=25-v_3(k),
\qquad k-v_3(k)\ge1.
$$


Next,


$$
(Z-1)^3=Y-1+3Z(1-Z).
$$


In its $N$-th power, the linear perturbation is $3N E_1=3^{25}E_1$. For every $k\ge2$,


$$
v_3\!\left(\binom Nk3^k\right)
=24-v_3(k)+k\ge26.
$$


This proves (6.1) coefficientwise.

### 6.2 The ordinary physical residual is in $3^{26}$

For $\deg p\le\nu-2$, the same physical trial $V[p]=x^Dp\rho_{25}$ satisfies


$$
\boxed{G_c(W,V[p])\in3^{26}M.}
\tag{6.2}
$$



For the main term of (6.1), every pole surviving modulo $3^{26}$ has denominator divisible by $L$. A LOW factor misses the required residue. A HIGH factor has degree at most


$$
m+\nu-1=\frac{H-1}{2}-1,
$$


so only the vanishing moments $0\le q<M$ occur. Their largest completed denominator is


$$
(4N-3)L=4H-243Q,
$$


inside the original cutoff.

In the $3^{25}E_1$-term, replacing $\rho_{25}$ by $1$ costs $3^{27}$. The remaining polynomial has degree at most


$$
(H-27Q)+m+(\nu-2)+1=n_3-27Q-1<n_3.
$$


It therefore has one additional factor $3$ after $\Lambda_h$. The $E_2$-term is already in $3^{26}$, and the complete factorial contribution is in $3^h$.

The last middle residual correspondingly refines to


$$
G_c(W,V[y^{\nu-1}])
\equiv3\mathfrak t_{25}e_{Y_m}\pmod{3^{26}}.
\tag{6.3}
$$


The exceptional term remains; only its error has improved.

Applying the actual inverse to (6.2) gives


$$
\boxed{V[p]-F[p]\in3^{25}W
\qquad(\deg p\le\nu-2).}
\tag{6.4}
$$



This is an admissible $p=25$ precision statement. It does not contradict the genuine $p=26$ overflow obstruction.

### 6.3 Last-middle pairing at precision $26$

The raw pairing in Section 5.3 is also in $3^{26}$.

Its sparse main term misses the pole residue modulo $L$, because $\deg B<(L-1)/2$. For the first correction in (6.1), replace $\rho_{25}^2$ by $1$ at cost $3^{27}$. Its remaining degree is at most


$$
H-27Q+2D-4<n_3,
$$


so its pole value acquires an additional factor $3$.

In the stationary correction (5.8), the valuations are now


$$
26-1+1=26.
$$


Therefore


$$
G_c(F[p'],F[y^{\nu-1}])\in3^{26}\mathbb Z_3
\qquad(\deg p'\le\nu-2).
\tag{6.5}
$$


No last-middle compression identity through $3^{31}$ has been asserted.

### 6.4 Strengthened bulk and selected-input source bounds

Use (6.4) in the one-sided transport of Section 5. The mixed observation contributes one further digit:


$$
3^{25}W
\quad\overset{\mathcal B(\,\cdot\,,F[q])}{\longrightarrow}\quad
3^{26}\mathbb Z_3.
$$


The monic transport and physical degree checks are unchanged. Ordinary corrected pairings are in $3^{26}$ by the retained compression, and the last-middle pairing is in $3^{26}$ by (6.5).

Thus


$$
\boxed{
\mathcal B(F[p],F[q])\in3^{26}\mathbb Z_3,
\qquad
\deg p\le\nu-32,\quad \deg q<\nu.
}
\tag{6.6}
$$



For one-lift inputs, the multiplier is exactly $x^Dp'_a\rho_{25}$, with no LOW remainder and no overflow. Equation (6.2) and the error (6.4) give


$$
\boxed{\mathcal B(W,\mathcal F[a])\in3^{25}M.}
\tag{6.7}
$$



The exact quadratic Schur term is retained. Using (5.1) for the other mixed vector, its valuation is at least


$$
14+1+25-1=39.
$$


The direct term has valuation $7+26=33$. Hence


$$
\boxed{
\delta S(p,\Psi[a])\in3^{33}\mathbb Z_3
\qquad(\deg p<\nu,\ \deg a\le R).
}
\tag{6.8}
$$



---

## 7. One additional whole-middle digit from the existing $p=22$ certificate

No new terminal dual is needed for this step.

### 7.1 Both linear replacement errors gain a digit

Write


$$
\widetilde F[p]=F[p]+w_p,\qquad w_p\in3^{21}W.
$$


The compact lemma gives


$$
\mathcal B(\widetilde F[p],\widetilde F[q])\in3^{22}\mathbb Z_3.
$$


Expand exactly:


$$
\begin{aligned}
\mathcal B(\widetilde F[p],\widetilde F[q])
={}&\mathcal B(F[p],F[q])
+\mathcal B(w_p,F[q])\\
&+\mathcal B(F[p],w_q)
+\mathcal B(w_p,w_q).
\end{aligned}
$$


By the actual mixed observation, both linear errors are in $3^{22}$; the quadratic error is in $3^{42}$. Consequently


$$
\boxed{\mathcal B(F[p],F[q])\in3^{22}\mathbb Z_3}
\tag{7.1}
$$


for every original middle pair, including the last one.

### 7.2 The shortened $W$-part is LOW modulo $3$

The construction of $U_p$ in Section 3 has an additional useful property.

From (2.8) and (1.6),


$$
\pi_p\equiv p\pmod3,\qquad r_{31}\equiv\beta^{-1}\pmod3.
$$


Hence


$$
H_p\equiv x^{D-72}q_{31}\beta^{-1}p\pmod3
$$


has degree at most $d-1$. All coefficients removed using $\Omega_0,\ldots,\Omega_{51}$ are therefore divisible by $3$. The terminal correction is also divisible by $3$. Since $\rho_{22}\equiv1\pmod3$,


$$
\boxed{U_p\pmod3\ \text{is an actual LOW polynomial}.}
\tag{7.2}
$$



For every actual $W$-row, pairing $\mathscr R$ with this LOW polynomial has numerator degree at most


$$
A+(D-1)+m=H+m-1<n_3.
$$


Therefore


$$
\boxed{\mathcal B(W,U_p)\in3M.}
\tag{7.3}
$$


This strengthens A4’s LOW-coordinate divisibility to divisibility of the entire mixed vector.

Let $d_p=\mathcal B(W,U_p)$. Then


$$
d_p^TE_{\mathrm{act}}^{-1}d_q\in3\mathbb Z_3,
$$


because $d_p,d_q\in3M$ and $E_{\mathrm{act}}^{-1}\in3^{-1}M$.

In the contraction of (3.11), the three terms consequently have valuations at least


$$
22,\qquad 7+22=29,\qquad 14+1=15.
$$


After the outer $c^2=3^{14}$, the last term is in $3^{29}$. The cross and error-error terms remain in $3^{35}$ and $3^{55}$. The direct term is in $3^{7+22}=3^{29}$ by (7.1).

Thus


$$
\boxed{
S_{\mathrm{act}}-S_c\in3^{29}\operatorname{Mat}(\mathbb Z_3)
}
\tag{7.4}
$$


on the entire original middle space.

Equations (6.8) and (7.4) are the two strengthened inputs needed for the returned matrix.

---

## 8. All prefix, $J$- and rank-$b$ inverse payments

The following common ledger audits A4’s original bounds and propagates the new ones.

Let $\varepsilon\in\{0,1\}$, and assume


$$
\delta S\in3^{28+\varepsilon}M
$$


on the whole middle space, and


$$
\delta S(p,\Psi[a])\in3^{32+\varepsilon}\mathbb Z_3.
$$


The case $\varepsilon=0$ is A4’s audited proof; the case $\varepsilon=1$ is (6.8), (7.4).

### 8.1 Finite prefix

The prefix is exactly $0,\ldots,R_*-1$, where


$$
R_*=\frac{9Q+1}{2}.
$$


The tail has $\tau=\nu-R_*$ coordinates, partitioned as


$$
K=\{0,\ldots,3R\},\qquad
J=\{3R+1,\ldots,\tau-1\}.
$$


Thus the last original middle coordinate remains in $J$.

Let $G_0$ have columns $x^by^a$, $0\le a\le R$, in the original $K$-coordinates. The exact core-prefix lift is the one-lift column plus $9Z$.

Therefore:

- a $G_0,G_0$ direct perturbation is in $3^{32+\varepsilon}$;
- a general tail-to-$G_0$ perturbation is in $3^{30+\varepsilon}$;
- a prefix-to-$G_0$ perturbation is in $3^{30+\varepsilon}$;
- a general perturbation remains in $3^{28+\varepsilon}$.

The physical prefix inverse costs $3^{-26}$. The normalized prefix perturbation is in $3^{2+\varepsilon}$, so the actual normalized prefix remains a unit block.

The quadratic perturbation payments are


$$
\begin{array}{c|c}
\text{channel}&\text{quadratic valuation}\\ \hline
\text{general}&(28+\varepsilon)+(28+\varepsilon)-26=30+2\varepsilon\\
\text{mixed }G_0&(28+\varepsilon)+(30+\varepsilon)-26=32+2\varepsilon\\
G_0,G_0&(30+\varepsilon)+(30+\varepsilon)-26=34+2\varepsilon.
\end{array}
$$


After division by $3^{26}$, the normalized prefix Schur differences satisfy


$$
\delta\mathcal R\in3^{2+\varepsilon}M,
\tag{8.1}
$$




$$
\delta\mathcal R_{T,K}G_0\in3^{4+\varepsilon}M,
\tag{8.2}
$$




$$
G_0^T\delta\mathcal R_{KK}G_0\in3^{6+\varepsilon}M.
\tag{8.3}
$$



### 8.2 Complete $J$-return

Retain the exact normalizations


$$
\mathcal R_{\alpha,JJ}=3B_\alpha,\qquad
\mathcal R_{\alpha,KJ}=9L_\alpha.
$$


Equations (8.1)–(8.2) give


$$
B_{\mathrm{act}}-B_c\in3^{1+\varepsilon}M,
$$




$$
L_{\mathrm{act}}-L_c\in3^\varepsilon M,
$$




$$
(L_{\mathrm{act}}-L_c)^TG_0\in3^{2+\varepsilon}M.
\tag{8.4}
$$


The actual $J$-inverse costs $3^{-1}$, and


$$
B_{\mathrm{act}}^{-1}-B_c^{-1}\in3^{1+\varepsilon}M.
$$



The physical-terminal theorem gives $L_c^TG_0\in3M$. Hence, with


$$
C_\alpha=\frac{L_\alpha^TG_0}{3},
$$


one has


$$
C_{\mathrm{act}}-C_c\in3^{1+\varepsilon}M.
$$


The complete contracted return is


$$
27G_0^TL_\alpha B_\alpha^{-1}L_\alpha^TG_0
=3^5C_\alpha^TB_\alpha^{-1}C_\alpha.
$$


Its difference is therefore in $3^{6+\varepsilon}M$, including the change in the inverse.

Thus


$$
G_0^T(\mathcal S_{\mathrm{act}}^{(2)}
-\mathcal S_c^{(2)})G_0
\in3^{6+\varepsilon}M.
\tag{8.5}
$$



For the mixed $E_b,G_0$ channel, the least-divisible term in the $J$-return difference has:

- the outside factor $3^3$;
- a left coupling difference in $3^\varepsilon$;
- a right $G_0$-coupling in $3$.

Hence that difference is in $3^{4+\varepsilon}$, exactly matching the direct bound. Therefore


$$
E_b^T(\mathcal S_{\mathrm{act}}^{(2)}
-\mathcal S_c^{(2)})G_0
\in3^{4+\varepsilon}M.
\tag{8.6}
$$



### 8.3 Rank-$b$ return

Define


$$
A_{b,\alpha}
=\frac{E_b^T\mathcal S_\alpha^{(2)}E_b}{9},
\qquad
M_{b,\alpha}
=\frac{E_b^T\mathcal S_\alpha^{(2)}G_0}{27}.
$$


The original H2 block is a unit after its factor $9$, so its physical inverse costs $3^{-2}$.

From the preceding estimates,


$$
M_{b,\mathrm{act}}-M_{b,c}\in3^{1+\varepsilon}M.
$$


The closed core result $M_{b,c}\in3M$ therefore gives $M_{b,\mathrm{act}}\in3M$.

On the whole $K$-block, the $J$-return difference is in $3^{3+\varepsilon}$, while the direct difference is in $3^{2+\varepsilon}$. Consequently


$$
A_{b,\mathrm{act}}-A_{b,c}\in3^\varepsilon M,
$$


and the same bound holds for their inverse difference.

The exact rank-$b$ return is


$$
81M_{b,\alpha}^TA_{b,\alpha}^{-1}M_{b,\alpha}.
$$


In its difference, the cross terms have valuation at least


$$
4+(1+\varepsilon)+1=6+\varepsilon,
$$


and the inverse-change term has valuation at least


$$
4+1+\varepsilon+1=6+\varepsilon.
$$


Thus the entire rank-$b$ return difference is in $3^{6+\varepsilon}$.

Combining all channels proves


$$
\boxed{
T_{\mathrm{act},\mathrm{red}}-T_{c,\mathrm{red}}
\in3^{6+\varepsilon}M.
}
\tag{8.7}
$$



For $\varepsilon=0$, this independently verifies A4’s reported result.

For $\varepsilon=1$, it gives the new evaluated refinement


$$
\boxed{
T_{\mathrm{act},\mathrm{red}}-T_{c,\mathrm{red}}\in3^7M,
\qquad
\Delta_{GG}\in27M,\qquad
\Delta_{bG}\in9M.
}
\tag{8.8}
$$


Equivalently, the previously unpaid next producer digit is explicitly zero:


$$
\boxed{
\frac{T_{\mathrm{act},\mathrm{red}}-T_{c,\mathrm{red}}}{3^6}
\equiv0\pmod3.
}
\tag{8.9}
$$



---

## 9. Exact radical, unit complement, and physical terminal

The retained leading complete-core form is


$$
T_{c,\mathrm{red}}/81\equiv-\mathsf H_\kappa\pmod3,
\qquad \kappa=\frac{3P-3}{2},
$$


where


$$
(\mathsf H_\kappa)_{ac}
=[y^{\kappa-a-c}](1-y)^b.
$$


Its already evaluated entry rule is


$$
(\mathsf H_\kappa)_{ac}
=(-1)^s\prod_i\binom{b_i}{s_i}\pmod3,
\qquad s=\kappa-a-c,
$$


with zero outside $0\le s\le b$, and with $b_i,s_i$ the ternary digits.

The comparison (8.8) gives


$$
T_{\mathrm{act},\mathrm{red}}/81
\equiv-\mathsf H_\kappa\pmod3.
$$


Thus the entire actual leading complement is a unit; this conclusion is not inferred merely from vanishing on a selected radical.

The exact radical is retained:


$$
g_s=(1-y)^{2\chi}y^s,
\qquad
L_*=\frac{P-1}{2}\le s\le L_*+\delta-1,
$$




$$
\delta=\min\left\{\chi-1,\frac{P+3}{2}-3\chi\right\},
$$


with


$$
[E_{\mathcal C}\ \mathscr G]\in\operatorname{GL}_{R+1}(\mathbb Z).
$$



### 9.1 Comparison after the exact unit-complement lifts

The complementary physical inverse costs $3^{-4}$. Its radical coupling is in $3^5$, so the exact displacement is in $3M$.

Let $\widehat{\mathscr G}_\alpha$ denote the respective exact complementary lifts. To compare their returned matrices at the new precision, individual $3^6$ return bounds are not enough; use the exact Schur perturbation formula.

Writing $\delta T=T_{\mathrm{act},\mathrm{red}}-T_{c,\mathrm{red}}$, the direct perturbation on the core-lifted radical is in $3^7$. Its quadratic correction has valuation at least


$$
7+7-4=10.
$$


Therefore


$$
\widehat{\mathscr G}_{\mathrm{act}}^TT_{\mathrm{act},\mathrm{red}}
\widehat{\mathscr G}_{\mathrm{act}}
-
\widehat{\mathscr G}_{c}^TT_{c,\mathrm{red}}
\widehat{\mathscr G}_{c}
\in3^7M.
$$


In particular,


$$
\boxed{
\frac{\widehat{\mathscr G}_{\mathrm{act}}^TT_{\mathrm{act},\mathrm{red}}
\widehat{\mathscr G}_{\mathrm{act}}}{3^5}
\equiv
\frac{\widehat{\mathscr G}_{c}^TT_{c,\mathrm{red}}
\widehat{\mathscr G}_{c}}{3^5}
\pmod9.
}
\tag{9.1}
$$



This is a comparison of matrix Schur complements. It does not evaluate the endpoint or diagonal channels of a bordered complementary elimination.

### 9.2 Physical terminal transfer

From (6.7),


$$
\mathcal F_{\mathrm{act}}[a]-\mathcal F[a]
=-3^7WE_{\mathrm{act}}^{-1}\mathcal B(W,\mathcal F[a])
\in3^{31}W.
$$


Thus A4’s physical-terminal transfer passes:


$$
\boxed{
[y^m]\mathcal F_{\mathrm{act},a}
\equiv-3^{27}\delta_{a,R}\pmod{3^{28}}.
}
\tag{9.2}
$$



For radical inputs,


$$
[y^m]\mathcal F_{\mathrm{act}}[g_s]
\equiv-3^{27}[y^R]g_s\pmod{3^{28}}.
$$



The original arithmetic buffer is relevant to the branch statement. For sufficiently large original indices,


$$
\chi=\frac{243r-25P}{2},
$$


so $v_3(\chi)=5$, and $P-8\chi$ is a nonzero multiple of $243$. This excludes the small boundary ambiguity in the branch $\delta=\chi-1$; there all displayed $g_s$ have degree below $R$. In the other branch, the final generator has degree $R$ and leading coefficient $1$.

None of these statements identifies the subsequently returned endpoint functional.

---

## 10. What passes, what needs qualification, and what remains open

| Claim | Audit result |
|---|---|
| Extended physical $p=22$ terminal dual | **Passes**, with residual $3^{22}$ and inverse error $3^{21}$ |
| Last middle $p=22$ representative | **Passes**, only after retaining $3\mathfrak t_{22}\tau(p)e_{Y_m}$ |
| Compact norm and finite macro cutoff | **Passes** |
| Actual inverse-image criterion | **Passes**, only for vectors with LOW coordinates divisible by $3$ |
| Shortened multiplier and $W$-membership | **Passes**, with the stated monic decomposition and degree bounds |
| Natural physical $p=26$ precision $25$ | **Passes and is sharp** on the displayed radical generators |
| Natural physical $p=26$ precision $26$ | **False**; the explicit LOW rows in Section 4.3 detect the loss |
| A4’s complete $3^6$ returned comparison | **Passes**, including all stated inverses |
| Coordinator’s $p=25$ bulk theorem | **Passes** |
| Coordinator’s last-middle candidate | **Passes** after evaluating its actual residual; ordinary compression through $3^{31}$ is still not extended there |
| New complete $3^7$ comparison | **Proved above** |
| Actual unit complement and common divided radical matrix | **Proved at the stated precisions** |
| Actual radical endpoint pivot | **Open** |
| Evaluated $1/9$ diagonal return | **Open** |
| Paid directional solve through further singular layers | **Open** |
| Primitive-denominator gain and whole-error decay | **Open** |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

No reported A4 $3^6$ digit is invalidated by an additional inverse loss in this audit. The only false stronger substitution is the already identified $p=26$ physical precision-$26$ assertion.

---

## 11. Exact remaining bordered bottleneck

All complete forcing and return terms remain present. In particular,


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\mathrm{ret}}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right)
\tag{11.1}
$$


is unchanged.

For $\alpha=c,\mathrm{act}$, retain


$$
f_\alpha^{(2)}
=f_{\alpha,K}-3L_\alpha B_\alpha^{-1}f_{\alpha,J},
$$




$$
\lambda_\alpha^{(2)}
=\lambda_\alpha-\frac13f_{\alpha,J}^TB_\alpha^{-1}f_{\alpha,J},
\tag{11.2}
$$


and


$$
f_{\alpha,\mathrm{new}}
=f_{\alpha,R}-3M_{b,\alpha}^TA_{b,\alpha}^{-1}f_{\alpha,b},
$$




$$
\lambda_{\alpha,\mathrm{new}}
=\lambda_\alpha^{(2)}
-\frac19f_{\alpha,b}^TA_{b,\alpha}^{-1}f_{\alpha,b}.
\tag{11.3}
$$



The matrix comparison does not delete either endpoint return or either diagonal division.

### 11.1 Actual endpoint samples

The proved divisibilities imply


$$
f_{\mathrm{act},\mathrm{new}}
\equiv G_0^Tf_{\mathrm{act},K}\pmod9.
$$


For a radical generator,


$$
G_0g_s=x^bg_s=x^{2P}y^s
\equiv(1+y^P+y^{2P})y^s\pmod3.
$$


Therefore


$$
\boxed{
f_{\mathrm{act},\mathrm{new}}(g_s)
\equiv
(f_{\mathrm{act},K})_s
+(f_{\mathrm{act},K})_{s+P}
+(f_{\mathrm{act},K})_{s+2P}
\pmod3.
}
\tag{11.4}
$$


All three indices are physical $K$-indices, because $s+2P\le3R$. Their original middle indices are


$$
R_*+s,\qquad R_*+s+P,\qquad R_*+s+2P.
$$



The exact open endpoint quantities are thus


$$
\epsilon_s=
(f_{\mathrm{act},K})_s
+(f_{\mathrm{act},K})_{s+P}
+(f_{\mathrm{act},K})_{s+2P}\in\mathbb F_3,
\tag{11.5}
$$


with $f_{\mathrm{act},K}$ formed from the complete signed force and actual prefix return.

A unit radical endpoint pivot exists precisely when at least one allowed $\epsilon_s$ is nonzero. Neither generic primitivity nor $g_s(-1)\ne0$ establishes this. In a saturated complement-radical basis, a primitive functional may be supported entirely on the complement.

### 11.2 The diagonal numerator must actually be evaluated

Put


$$
Q_b=f_{\mathrm{act},b}^TA_{b,\mathrm{act}}^{-1}f_{\mathrm{act},b}.
$$


The exact return remains


$$
\lambda_{\mathrm{act},\mathrm{new}}
=\lambda_{\mathrm{act}}^{(2)}-\frac{Q_b}{9}.
$$


An endpoint congruence modulo $3$ does not determine it. Replacing $f_b$ by $f_b+3z$ changes $Q_b/9$ by


$$
\frac23z^TA_b^{-1}f_b+z^TA_b^{-1}z,
$$


whose first term can have valuation $-1$.

The concrete next certificate must evaluate


$$
Q_b\pmod{27},
\qquad
9\lambda_{\mathrm{act}}^{(2)}\pmod{27},
\tag{11.6}
$$


together with (11.5), from the actual returned data. The retained normalization


$$
\lambda_{\mathrm{act},\mathrm{new}}=\eta/3,
\qquad \eta\in\mathbb Z_3^\times,
$$


requires their difference to be $3\eta\pmod{27}$, but does not supply its value.

Only after these evaluations can the actual endpoint-annihilating direction be formed and tested in the retained operator


$$
B^\sharp=B+\frac{27\eta}{u}ww^T,
\qquad
u=1-27\eta\alpha\in1+27\mathbb Z_3.
$$


The solve


$$
B^\sharp v=w,\qquad v\in3^{-1}\mathbb Z_3^{\,R},
$$


still requires actual Smith-direction divisibility through the singular layers. The enlarged matrix agreement proved here does not supply that direction.

---

## 12. Contents, least clearer, all-prime gcd, and the whole error

No original column content has been changed. All previously paid original content divisions remain exactly as constructed. The $3$-adic filtered certificates are not replacements for the actual least simultaneous clearer $\ell_{\mathrm{clr}}$.

The complete source recurrence remains


$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\qquad 0\le t\le2n-2.
$$


Its resonance


$$
t_*=\frac{3^h-5}{2}
$$


retains the genuine $3^h$ division. The highest required moment remains physical because $H-4D+5\ge0$. No local comparison here removes this division or replaces the complete determinant by a pole determinant.

Retain the actual integers


$$
A_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_0,
\qquad
B_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_1,
$$


and the gcd over **all primes**


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


For $B_\ell\ne0$, the actual primitive numerator and denominator are


$$
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
\qquad
q=\frac{|B_\ell|}{g_\ell}.
$$



The whole evaluated error is exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\mathrm{clr}}^{m+1}}
{g_\ell}\det H_{\mathrm{complete}}.
}
\tag{12.1}
$$



An irrationality proof would follow if, at the **same infinite original indices**, one established


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
\tag{12.2}
$$


These conditions make the nonzero whole errors tend to zero; if $e+\pi=a/b$ were rational, every such nonzero error would have absolute value at least $1/b$.

This is a conditional implication, not a conclusion of the local matrix audit. Common local determinant factors can occur in both distinguished cofactors and disappear in the actual primitive quotient.

---

## 13. Bounded arithmetic receipt and conclusion

No tool computation was performed. No dense original matrix, signed-source jet, old terminal constant, full syzygy, or closed prime table needs to be rerun for the proof above.

No new numerical calculation is necessary for the $3^7$ comparison. An optional small diagnostic for the binomial payment in (6.1) is:

- **Inputs:** formal variables $A,C$, exponent $9$, modulus $81$.
- **Calculation:** expand $(A+3C)^9$ by its ten binomial coefficients.
- **Expected verifiable output:**
  

$$
(A+3C)^9\equiv A^9+27A^8C\pmod{81},
$$


  namely the coefficient vector
  

$$
(1,27,0,0,0,0,0,0,0,0)
$$


  for $A^{9-k}C^k$, $0\le k\le9$.

This finite diagnostic verifies only that finite polynomial identity. The uniform $N=3^{24}$ statement is proved by the valuation inequalities in Section 6, not by extrapolation from the check.

### Final result and proof status

The independent audit confirms A4’s claimed full producer comparison. The coordinator’s nonoverflowing $p=25$ transport is valid, including its properly charged last-middle extension, and supplies a simpler selected-input route.

The new evaluated finite original-family refinement is


$$
\boxed{
\Delta_{GG}\in27M,\qquad
\Delta_{bG}\in9M,\qquad
T_{\mathrm{act},\mathrm{red}}-T_{c,\mathrm{red}}\in3^7M.
}
$$


After the paid unit-complement lifts, the corresponding divided radical matrices agree modulo $9$.

The exact remaining local bottleneck is bordered: evaluate the actual three-entry endpoint samples (11.5), the actual residues (11.6), and then the required directional divisibility through the remaining singular layers. The exact remaining global bottleneck is nonvanishing and decay of the whole error (12.1), after the actual contents, least simultaneous clearer, all-prime gcd, and primitive denominator are used at the same infinite original indices.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ is obtained.}}
$$


