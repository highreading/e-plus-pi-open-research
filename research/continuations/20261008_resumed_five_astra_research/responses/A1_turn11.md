> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the terminal-aware $J$-return and the next boundary digit

## Abstract and verdict

The rationality or irrationality of $e+\pi$ remains unresolved.

The principal conclusion of this report is:



$$
\boxed{\textbf{PASS: the complete terminal-aware \(J\)-quadratic theorem in A4 Turn 12 is valid.}}
$$



More precisely, on the **whole literal first-radical lattice**, at the original retained indices, the complete core and actual finite blocks satisfy


$$
\boxed{
l_{\alpha,z}^{T}B_\alpha^{-1}l_{\alpha,v}\in9\mathbb Z_3,
\qquad
\alpha=c,\mathrm{act}.
}
\tag{0.1}
$$


The last middle column is retained throughout. Its leading contribution is the actual scalar $\theta_{\alpha,z}$; it is not set to zero. Every coefficient of that scalar in the quadratic modulo $9$ is proved to vanish.

The audit below supplies explicit derivations of the raw-source support, the complete prefix contribution, the finite inverse images, all first-coordinate contractions, and the symmetric lift identity. In particular, it does not rely on A4 Turn 13’s new source-$81$ or forcing-unit assertions.

For the secondary assignment:

* the parent’s two-coordinate boundary reduction **passes**;
* a further source-specific value is proved:
  

$$
\boxed{\sigma_c=0;}
  \tag{0.2}
$$


* an explicit, finite-supported formula for the **actual/core transport of all three next coefficients** is proved below.

However, I do **not** obtain an evaluated value of the complete next quadratic


$$
l_{\mathrm{act},z}^{T}B_{\mathrm{act}}^{-1}l_{\mathrm{act},v}/9\pmod3.
$$


The remaining quantities are identified precisely. Neither their values nor the actual leading terminal combination follow from the accepted comparison bounds. Thus the secondary evaluation is **not closed**.

The already closed analytic audit, prefix-$27$ theorem, and later exact-$3$ result are not repeated.

---

## 1. Original domain, complete objects, and the permitted reuse

### 1.1 Original indices

All assertions concern sufficiently large indices in exactly the original family:


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$




$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15},
$$


and


$$
\frac{103}{1000}<\frac{N_0}{P_0}<\frac{104}{1000}.
$$



The derived parameters remain


$$
P_0=243P=3^{h-27},\qquad N_0=243r,\qquad D=P_0+N_0,
$$




$$
P=3^{h-32},\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$




$$
4^j=243(3^{26}-1)P-243r+1.
$$


Set


$$
Q=27P,\qquad b=Q-N_0=2R,\qquad \chi=P-R,\qquad c=2\chi.
$$


Then


$$
N_0=25P+c,\qquad D=268P+c,\qquad D+b=10Q,
$$


and, for sufficiently large original indices,


$$
v_3(\chi)=5,\qquad \chi/243\equiv1\pmod9.
\tag{1.1}
$$



No independently selected $P,\chi$, or scaled experimental tuple, is substituted for these data.

### 1.2 Complete finite spaces and physical terminal

Write $x=y-1$. The spaces are


$$
U_s=x^s\quad(0\le s<D),
$$




$$
z_i=x^Dy^i\quad(0\le i<\nu),\qquad \nu=D/2-1,
$$




$$
Y_t=y^t\quad(d\le t\le m),\qquad d=D+\nu,\qquad W=[U\ Y].
$$


The physical HIGH terminal remains $Y_m$.

The complete functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!.
\tag{1.2}
$$


Its cutoff is exactly $2n-2$, with largest denominator


$$
4H-4D+5<3^{h+1}.
$$



For $\alpha=c,\mathrm{act}$,


$$
G_\alpha(f,g)=\mathcal M(Q_\alpha fg),\qquad
E_\alpha=G_\alpha(W,W),
$$




$$
F_\alpha[p]
=x^Dp-WE_\alpha^{-1}G_\alpha(W,x^Dp).
\tag{1.3}
$$


The core producer is


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A.
$$



The one-lift polynomial is


$$
\Psi[a]=x^{D+b}y^{k_0}(y^{3Q}+3)a(y),
\qquad k_0=\frac{3Q+1}{2},
$$


and $\mathcal F_\alpha[a]$ is its complete correction against the same $W$.

The finite prefix and tail boundaries are


$$
R_*=\frac{9Q+1}{2},\qquad a_0=R_*-1,
$$




$$
\tau=\frac{N_0-3}{2},\qquad \ell=3R+1,
$$




$$
J=\{\ell,\ldots,\tau-1\},
$$




$$
N=|J|=\frac{19P+8\chi-5}{2}.
\tag{1.4}
$$


Number the $J$-coordinates by $i=0,\ldots,N-1$, so their ordinary labels are $R_*+\ell+i$. The coordinate $i=N-1$ is the actual last middle column $F_\alpha[y^{\nu-1}]$.

### 1.3 Literal first-radical domain

Put


$$
L_*=\frac{P-1}{2},\qquad
\delta=\min\left\{\chi-1,\frac{P+3}{2}-3\chi\right\}.
$$


For every


$$
z\in\mathbb Z_3[y]_{<\delta},
$$


define


$$
C_z=(1-y)^cz,\qquad
\mathcal G[z]=y^{L_*}C_z.
\tag{1.5}
$$



The established inequalities used below are


$$
\delta\le\chi-1,\qquad
3\chi+\delta\le\frac{P+3}{2},
$$




$$
\deg C_z\le c+\delta-1,
$$


and


$$
\boxed{
\deg\bigl((1-y)^czv\bigr)\le c+2\delta-2\le L_*-120.
}
\tag{1.6}
$$



These are the hypotheses for the **whole first radical**, not merely the second kernel.

### 1.4 Reused results and their scope

I reuse the established:

1. complete $W$-projection and terminal payment, including the $3^{-1}$ projection-inverse allowance;
2. complete-core compression modulo $3^{32}$, only for admitted ordinary inputs of degree at most $\nu-2$;
3. finite prefix inverse, paid identity $X=3P_G+9Z$, and integrality of the normalized couplings;
4. finite unit property of the complete $J$-block;
5. complete actual/core comparisons
   

$$
\delta S(p,q)\in3^{29}\mathbb Z_3,\qquad
   \delta S(p,\Psi[a])\in3^{32}\mathbb Z_3
   \tag{1.7}
$$


   at their admitted ordinary/general-one scopes;
6. the independently passed prefix-$27$ theorem, including its finite-boundary clarification.

Only the already closed part of A4 Turn 13 is used. Its new source-$81$, forcing-unit, and conditional short-producer claims are not premises of this audit.

The degree admissions needed here are explicit:


$$
\deg\mathcal G[z]\le R,
$$




$$
\deg\!\left(x^by^{k_0}(y^{3Q}+3)\mathcal G[z]\right)
\le R_*+3R<\nu-2.
\tag{1.8}
$$


For $0\le i\le N-2$,


$$
R_*+\ell+i\le\nu-2.
$$


Thus every compressed input below is ordinary. The last coordinate $N-1$ is never covered by these compression formulas.

---

## 2. Exact normalization: the raw moment and the complete prefix return

It is useful to expose the complete Schur construction rather than treat the second term of A4’s formula as an optional correction.

For the core, define


$$
\mathsf A_{pq}
=-\frac{G_c(F_c[y^p],F_c[y^q])}{3^{26}},
\qquad 0\le p,q\le a_0,
$$


and let $\mathsf B_i$ be the prefix-to-$J$ column with label $\ell+i$. Put


$$
\mathbf q_i=\mathsf B_i/3,
$$




$$
T_{ij}
=-\frac{G_c(F_c[y^{R_*+\ell+i}],
             F_c[y^{R_*+\ell+j}])}{3^{27}}.
$$


Then the exact complete prefix-returned block is


$$
\boxed{
B_{ij}=T_{ij}-3\mathbf q_i^T\mathsf A^{-1}\mathbf q_j.
}
\tag{2.1}
$$



For a radical amplitude $z$, put


$$
(d_z)_p
=\frac{G_c(F_c[y^p],\mathcal F_c[\mathcal G[z]])}{3^{28}},
\qquad Z_z=\mathsf A^{-1}d_z.
\tag{2.2}
$$


The corrected column


$$
K_z=\mathcal F_c[\mathcal G[z]]+9F_c[Z_z]
$$


is exactly orthogonal to the prefix, since


$$
G_c(F_{\rm pref},K_z)
=3^{28}d_z-9\cdot3^{26}\mathsf A Z_z=0.
$$


Consequently the normalized coupling is exactly


$$
\boxed{
(l_z)_i
=
-\frac{G_c(F_c[y^{R_*+\ell+i}],
                 \mathcal F_c[\mathcal G[z]])}{3^{29}}
+\mathbf q_i^TZ_z.
}
\tag{2.3}
$$


This confirms the sign, division, and full prefix return in A4 Turn 12, equation (4.2).

The same definitions and identities hold for the actual producer. In particular, (2.3) remains an exact identity at the last coordinate; only its subsequent ordinary-column compression is restricted.

### Precision ledger



$$
\begin{array}{c|c|c}
\text{required quantity}&\text{division}&\text{sufficient source precision}\\ \hline
T\bmod9&3^{27}&3^{29}\\
\mathbf q\bmod9&3^{27}&3^{29}\\
d\bmod9&3^{28}&3^{30}\\
\text{raw part of }l\bmod9&3^{29}&3^{31}\\
T\bmod27&3^{27}&3^{30}\\
d\bmod27&3^{28}&3^{31}\\
\text{raw part of }l\bmod27&3^{29}&3^{32}
\end{array}
\tag{2.4}
$$



Thus source $32$ is sufficient for the primary audit and for the ordinary source data needed by the next $J$-digit. This does not establish the separate source-$34$ theorem needed by a whole physical-$7$ moment calculation.

---

## 3. Independent derivation of the interior $B$-bands modulo $9$

Let


$$
U(y)=(1-y)^{N_0},\qquad U_r=[y^r]U,
$$


with $U_r=0$ outside $0\le r\le N_0$, and put


$$
S=N_0+N-1.
$$



Because $D=9Q+N_0$,


$$
(1-y)^D=(1-y)^{9Q}U(y),
\qquad
(1-y)^{9Q}\equiv(1-y^Q)^9\pmod{27}.
$$



### 3.1 The raw $27Q$-pole

For two ordinary $J$-coordinates, the extraction interval admits precisely the $3Q$ and $4Q$ bands of $(1-y^Q)^9$. Their coefficients are


$$
-84,\qquad126.
$$


The normalization at this pole is $-1/3$. Including $\beta+3y$, the raw contribution is therefore


$$
\begin{aligned}
K_N\bigl(
28\beta U_{S-i-j}
-42\beta U_{S-Q-i-j}
+84U_{S-1-i-j}
-126U_{S-Q-1-i-j}
\bigr).
\end{aligned}
$$


Since $K_N\beta\equiv1\pmod3$, this is


$$
K_N\beta U_{S-i-j}
+3U_{S-Q-i-j}
+3U_{S-1-i-j}\pmod9.
\tag{3.1}
$$



### 3.2 The remaining active poles

The $9Q$-extraction is negative. At the unit-$3Q$ layer the only admitted leading contributions are at $21Q$ and $39Q$. They are opposite copies of $U_{S-i-j}$, and the reciprocal denominator units agree modulo $3$. Their sum is zero modulo $9$.

Lower layers have normalized weight divisible by $9$.

These finite admissions agree with the actual compact support. In particular, the maximal tail-tail denominator is below $41Q$, so no unlisted higher pole with a more negative normalization occurs.

### 3.3 The prefix Schur term

Let


$$
s_v=k_0+v,\qquad v=\ell+i.
$$


The leading prefix selector is


$$
\mathsf A^{-1}\mathbf q_i\equiv\tfrac12e_{s_v}\pmod3,
\qquad
\overline{\mathsf A}=T_0,
$$


where


$$
(T_0)_{pq}=U_{a_0-p-q}.
$$


Since


$$
a_0-s_{\ell+i}-s_{\ell+j}=S-i-j,
$$


the prefix term in (2.1) is


$$
-3U_{S-i-j}\pmod9.
$$



Thus the claimed complete formula is correct:


$$
\boxed{
B_{ij}\equiv
\rho U_{S-i-j}
+3U_{S-Q-i-j}
+3U_{S-1-i-j}\pmod9,
\quad 0\le i,j\le N-2,
}
\tag{3.2}
$$


where


$$
\rho=K_N\beta-3,\qquad \rho\equiv1\pmod3.
$$



No entry involving coordinate $N-1$ has been assigned by (3.2).

---

## 4. The complete prefix contribution to $l$

This section verifies the new source-specific part of A4’s proof. It does not repeat the closed prefix-$27$ quadratic audit.

### 4.1 Leading residual constants

For a monomial amplitude $y^u$, the leading complete residual is


$$
\boxed{
\overline d_{p,u}
=
2\,\mathbf1_{p+u+1=Q}
+\mathbf1_{p+u+1=2Q}
+2\,\mathbf1_{p+u+1=4Q}.
}
\tag{4.1}
$$



Here is an independent recovery of its bounded constants.

Set


$$
c_k=(-1)^k\binom{30}{k},\qquad c_k=0\quad(k<0).
$$


At $p+u+1=j(9P)$, the combined high and $3$-weighted low highest-pole terms, together with the lower-pole correction, give


$$
\frac{c_{j+3}+3c_{j-6}}9+\mathbf1_{j=9}-\mathbf1_{j=6}\pmod3.
\tag{4.2}
$$


The needed residues $c_0,\ldots,c_{16}\pmod{27}$ are


$$
(1,24,3,17,0,0,18,0,0,15,9,18,21,0,0,18,0).
$$


Substitution gives


$$
(0,0,2,0,0,1,0,0,0,0,0,2,0),
\qquad 1\le j\le13.
\tag{4.3}
$$


The shifted $3y$-coefficients


$$
c_{j+3}/3+c_{j-6}
$$


are all zero modulo $3$.

The grid restriction is also paid. If $p+u+\sigma$ is not a multiple of $9P=Q/3$, the high coefficient at the $27Q$-pole has valuation at least $3$, before its division by $9$. The low coefficient has valuation at least $2$, before its division by $3$. Both disappear modulo $3$. The lower-pole leading coefficients require the coarser $Q$-grid and cancel as in (4.2).

The reduction from the scaled coefficients to the $30$-row is uniform: stripping powers of $3$ preserves normalized units modulo $3$, and the required unnormalized modulo-$27$ replacement is valid along the divisible-top ternary scaling. Thus (4.3) is a bounded verification of universal constants, not an experiment on a surrogate original tuple.

### 4.2 Applying the actual finite prefix inverse

The exact leading finite inverse is


$$
(T_0^{-1})_{pq}=[y^{p+q-a_0}]U^{-1}.
\tag{4.4}
$$


For a coefficient $y^{L_*+u}$ of $\mathcal G[z]$, all three selectors in (4.1) are inside $0,\ldots,a_0$. Applying (4.4) gives the finite truncation of


$$
(2y^{95P}+y^{68P}+2y^{14P})(1-y)^{-25P}z.
$$


Over $\mathbb F_3$,


$$
(1-y)^{-25P}
=\frac{1+y^P+y^{2P}}{1-y^{27P}}.
$$


Writing


$$
V(y)=1+y^P+y^{2P},
$$


and collecting the admitted bands yields


$$
\boxed{
\overline{Z_z}
=
2(y^{14P}+y^{41P}+y^{95P})V(y)z.
}
\tag{4.5}
$$


The next omitted band starts at $122P>a_0$. Each displayed band, including its full $z$-support, lies in the actual prefix.

### 4.3 The next prefix selector and its finite virtual term

For $v=\ell+i$, set


$$
(b_{k,v})_p=U_{kQ-1-p-v}.
$$


A direct pole extraction gives


$$
\mathbf q_i\equiv
K_N\left(
-b_{3,v}-3b_{3,v}^{(-1)}
+3(-b_{1,v}+b_{2,v}+2b_{4,v}+b_{5,v})
\right)\pmod9,
\tag{4.6}
$$


where $b_{3,v}^{(-1)}$ denotes the additional one-step coefficient shift.

The reused prefix matrix modulo $9$ is


$$
K_N^{-1}\mathsf A
\equiv7T_0-6T_{-1}-3T_{3Q}\pmod9.
$$


Since $T_{3Q}e_{s_v}=0$ in the actual finite prefix, solving (4.6) gives


$$
\boxed{
\begin{aligned}
\mathsf A^{-1}\mathbf q_i\equiv{}&
\tfrac12e_{s_v}\\
&+\tfrac32\left(
2T_0^{-1}b_{5,v}
+e_{s_v-Q}+2e_{s_v+Q}+e_{s_v+2Q}
\right)\pmod9.
\end{aligned}}
\tag{4.7}
$$



All displayed ordinary selectors are inside the prefix. The virtual label $s_v-2Q$ is negative; its contribution is exactly $T_0^{-1}b_{5,v}$, not an infinite Toeplitz substitution.

For every admitted monomial coefficient $y^u$, put


$$
r=\frac{Q-3}{2}-(v+u).
\tag{4.8}
$$


On all interior rows,


$$
2\le r<Q/2.
\tag{4.9}
$$


The shifted selectors in (4.7) vanish modulo $3$, because their residual anti-diagonal labels are integral multiples of $Q$ minus the strictly positive $r<Q/2$.

The unshifted selector satisfies


$$
d_{s_v,\bullet}\mathcal G[z]
\equiv3[y^{t-i}]C_z\pmod9,
\qquad t=P+3\chi-2.
\tag{4.10}
$$


Indeed, its sole surviving coefficient is the $198P=22(9P)$ coefficient of $(1-y)^{270P}$, whose normalized unit is


$$
\frac{\binom{30}{22}}{27}
=216775\equiv1\pmod3.
$$



For the virtual selector, (4.5) gives


$$
U\overline Z_z
=
2(y^{14P}-y^{68P}+y^{95P}-y^{122P})C_z.
\tag{4.11}
$$


It is observed at index $132P+3\chi-2-i$. Even after the largest shift $122P$, the residual exceeds $\deg C_z$ by at least


$$
\frac{P+7}{2}-3\chi-\delta\ge2.
$$


Thus the **complete finite** virtual-selector contraction vanishes modulo $3$.

It follows that the complete prefix contribution in (2.3), modulo $9$, is supported only in the old band $t-i$. The finite inverse and its virtual correction have both been retained.

---

## 5. Independent raw-moment audit modulo $9$

For an interior row and a monomial amplitude coefficient $y^u$, use $r$ from (4.8). At a pole $dQ$, the high extraction has the form


$$
\frac{d-19}{2}Q+r,
$$


and the $3$-weighted low extraction is three $Q$-bands higher.

The exact valuation identity


$$
v_3\binom{10Q}{aQ+r}
=v_3(Q)-v_3(r)+v_3\binom9a,
\qquad 0<r<Q,
\tag{5.1}
$$


controls the non-grid terms. It follows from extracting $10Q/(aQ+r)$ and applying Legendre’s formula to the remaining binomial coefficient.

### 5.1 Highest pole

At $27Q$, the high extraction is $4Q+r$, the low extraction is $7Q+r$, and the normalization in the raw term of $l$ costs $3^{-3}$.

Because


$$
v_3\binom94=v_3\binom97=2,
$$


the only high bands visible modulo $9$ are


$$
117P,\quad114P,\quad111P.
$$


The latter two carry one extra factor $3$. The weighted low term admits only $198P$ at this precision. The $3y$-term supplies the one-step-shifted old band.

### 5.2 Other pole layers

* At $9Q$, both extractions are negative.
* At the unit-$3Q$ layer, (5.1) puts every admitted coefficient too deep.
* At the unit-$Q$ layer, the only possible high contributions come from coarse bands $0$ and $9Q$. Their coefficients are opposite modulo $9$, after their common factor $3$; the reciprocal units agree modulo $3$.
* At the unit-$Q/3$ layer, the four leading coefficients are
  

$$
1,-1,-1,1.
$$


  The corresponding denominator units agree modulo $3$, so their sum is zero.
* Lower layers have normalized weight divisible by $9$.

The strict $r\ge2$ is essential: it keeps both $r$ and $r-1$ away from the boundary extraction. This is why the argument is not extended to the last middle column.

### 5.3 Explicit surviving bands

One can sharpen A4’s unnamed-band presentation slightly. Define the actual integral unit


$$
a_P=\frac{(-1)^{117P}\binom{270P}{117P}}{27}.
$$


Then $a_P\equiv1\pmod3$. The two finer high coefficients have normalized units


$$
\frac{\binom{90}{38}}{81}\equiv2,\qquad
\frac{-\binom{90}{37}}{81}\equiv1\pmod3.
$$


Combining the raw calculation with the complete prefix contribution gives


$$
\boxed{
\begin{aligned}
(l_z)_i\equiv{}&
u_0[y^{t-i}]C_z
-3[y^{t-1-i}]C_z\\
&+3[y^{t+3P-i}]C_z
-3[y^{t+6P-i}]C_z
\pmod9,
\end{aligned}}
\tag{5.2}
$$


where


$$
u_0\equiv-K_N\beta a_P+3\pmod9,
\qquad u_0\equiv-1\pmod3.
$$


No higher digit of $K_N$ has been replaced by $1$.

For the primary quadratic, the value of $u_0\bmod9$ is immaterial for a proved reason: every contraction of its band below is individually zero.

---

## 6. The finite inverse image and the actual terminal parameter

The leading ordinary coupling is


$$
\overline{(l_z)_i}=-[y^{t-i}]C_z.
\tag{6.1}
$$


Its support lies in


$$
P\le i\le t<N-2,
$$


so its first coordinate is zero.

Because $N_0$ is odd, coefficient reversal gives the finite leading interior inverse


$$
(C_0^{-1})_{ij}
=-[y^{N-1-i-j}]U^{-1},
\qquad 1\le i,j\le N-2.
\tag{6.2}
$$



Put


$$
a=\frac{13P+6\chi-3}{2},
\qquad
X_z(y)=y^aV(y)z(y).
\tag{6.3}
$$


Applying (6.2) to (6.1), reversing the even-degree factor $(1-y)^c$, gives


$$
(C_0^{-1}\overline l_{I,z})_i
=
\sum_u z_u
[y^{s-i+u}](1-y)^{-25P},
\qquad
s=a+2P.
$$


The observed coefficient indices are below $9P$. Therefore


$$
(1-y)^{-25P}
\equiv\frac{1+y^P+y^{2P}}{1-y^{27P}}\pmod3
$$


contributes only its coefficients at $0,P,2P$, proving


$$
\boxed{
C_0^{-1}\overline l_{I,z}=\overline X_{I,z}.
}
\tag{6.4}
$$



The finite support is


$$
a>0,\qquad
a+2P+\delta-1\le9P-1<N-2.
\tag{6.5}
$$


No convolution crosses an interior endpoint.

Write the complete leading block, with its actual terminal entries, as


$$
\overline B=
\begin{pmatrix}
0&0&a_\partial\\
0&C_0&w\\
a_\partial&w^T&c_\partial
\end{pmatrix}.
\tag{6.6}
$$


The finite unit property implies $a_\partial\ne0$. Solving this exact leading bordered system gives


$$
\boxed{
\overline{B^{-1}l_z}
=\theta_z e_0+\overline X_z,
}
\tag{6.7}
$$


where the last coordinate is zero and


$$
\boxed{
\theta_z
=a_\partial^{-1}
\bigl(\overline{(l_z)_{N-1}}-w^T\overline X_z\bigr).
}
\tag{6.8}
$$



This is the **actual** leading terminal combination. It has not been evaluated numerically and is not assumed to vanish.

---

## 7. Every contraction needed to remove $\theta$ at the current digit

### 7.1 Coupling contractions

At $i=0$, all four extraction indices in (5.2) exceed $\deg C_z$. Hence


$$
(l_z)_0\equiv0\pmod9.
\tag{7.1}
$$



For $X_v=y^aVv$, the first three bands of (5.2) have negative resulting extraction index. The last has


$$
t+6P-a=L_*.
$$


Its contraction is


$$
[y^{L_*}]V(y)(1-y)^czv.
$$


Since $L_*<P$, only the constant band of $V$ can contribute, and (1.6) makes that coefficient zero. Thus


$$
\boxed{l_z^TX_v\equiv0\pmod9.}
\tag{7.2}
$$



### 7.2 First corner of $B$

In (3.2), the unshifted and one-step-shifted coefficients at $B_{00}$ are outside the coefficient interval. The remaining coefficient reverses to


$$
U_{Q-N+1},
\qquad
Q-N+1=\frac{35P-8\chi+7}{2}\equiv125\pmod{243}.
$$


But $U\bmod3$ has support only at multiples of $243$. Therefore


$$
\boxed{B_{00}\equiv0\pmod9.}
\tag{7.3}
$$



### 7.3 First row against $X_z$

The unshifted and one-step-shifted terms are out of range on the support of $X_z$. After reversal, the remaining term is an explicit factor $3$ times a sum of


$$
U_{(24+k)P-\chi+2+u},
\qquad k=0,1,2.
$$


Here $0\le u<\delta$, so $-\chi+2+u\le0$.

If it is negative, its residue modulo $P$ is greater than $c$, and the coefficient vanishes modulo $3$. If it is zero, the three coarse coefficients sum to


$$
[y^{24}](1-y)^{25}
+[y^{25}](1-y)^{25}
+[y^{26}](1-y)^{25}
=1-1+0.
$$


Thus


$$
\boxed{e_0^TBX_z\equiv0\pmod9.}
\tag{7.4}
$$



### 7.4 Two interior inverse images

Let


$$
C=(1-y)^czv,\qquad D_*=21P+L_*.
$$


The three bands in (3.2), contracted against $X_z,X_v$, give


$$
\rho[y^{D_*}]UV^2zv,\qquad
3[y^{D_*-Q}]UV^2zv,\qquad
3[y^{D_*-1}]UV^2zv.
\tag{7.5}
$$


The middle index is negative. The last term is zero by the modulo-$3$ $P$-grid and the gap (1.6).

For the first term, put $\Pi=P/3$. Repeated cubing gives


$$
(1-y)^P
\equiv1-y^P+3(-y^\Pi+y^{2\Pi})\pmod9,
$$


and hence


$$
(1-y)^{25P}
\equiv
(1-y^P)^{25}
+3(1-y^P)^{24}(-y^\Pi+y^{2\Pi})\pmod9.
$$


The unshifted part observes $C_{L_*}=0$.

In the extra part,


$$
V^2\equiv(1-y^P)^4\pmod3.
$$


The $2\Pi$-shift observes a residue above $\deg C$. The $\Pi$-shift could observe $C_{\kappa_1}$, where $\kappa_1=(\Pi-1)/2$, but its coarse coefficient is


$$
[t^{21}](1-t)^{28}=0
$$


because $28=27+1$. Therefore


$$
\boxed{X_z^TBX_v\equiv0\pmod9.}
\tag{7.6}
$$



---

## 8. Exact symmetric lift, terminal cancellation, and actual/core transfer

Choose any integral lifts of the actual leading values $\theta_z$, and put


$$
x_z=\theta_z e_0+X_z.
$$


By (6.7),


$$
Bx_z\equiv l_z\pmod3.
$$


Thus


$$
r_z=(l_z-Bx_z)/3
$$


is integral. Direct expansion gives the exact symmetric identity


$$
\boxed{
l_z^TB^{-1}l_v
=
l_z^Tx_v+x_z^Tl_v-x_z^TBx_v
+9r_z^TB^{-1}r_v.
}
\tag{8.1}
$$



Both cross terms are present. The identity also contains the inverse change through its final quadratic term.

Equations (7.1)–(7.6) show that the first three terms on the right belong to $9\mathbb Z_3$. The last does too, because $B^{-1}$ is integral. Hence


$$
l_z^TB^{-1}l_v\in9\mathbb Z_3.
$$



### 8.1 Explicit coefficients of the actual terminal parameter

In (8.1), every term involving $\theta_z$ or $\theta_v$ is a multiple of one of


$$
(l_z)_0,\qquad (l_v)_0,\qquad
e_0^TBX_z,\qquad e_0^TBX_v,\qquad B_{00}.
$$


All five quantities are zero modulo $9$.

Therefore the entire terminal contribution to this digit is zero **for the actual boundary values**, not because the boundary values were deleted.

The same argument also gives


$$
(B^{-1}l_z)_{N-1}\in9\mathbb Z_3.
\tag{8.2}
$$


Indeed, the first component of $l_z-Bx_z$ lies in $9\mathbb Z_3$, and the leading bordered solve forces the last component of its inverse image to acquire the additional factor $3$.

### 8.2 Actual/core transfer

The accepted comparisons imply, on the ordinary first/interior part,


$$
B_{\mathrm{act}}-B_c\in9M.
$$


Also


$$
\mathsf A_{\mathrm{act}}-\mathsf A_c\in27M,\qquad
d_{\mathrm{act}}-d_c\in81M,
$$


so


$$
Z_{\mathrm{act}}-Z_c\in27M
$$


there; the weaker $9M$ comparison used in A4 Turn 12 would already suffice.

The general/one comparison in (1.7), after division by $3^{29}$, and the comparison of $\mathbf q_i$, give


$$
(l_{\mathrm{act},z})_i-(l_{c,z})_i\in9\mathbb Z_3,
\qquad 0\le i\le N-2.
$$


Thus every ordinary contraction proved above transfers.

The actual terminal integrality and complete finite unit border remain retained inputs. Since the proof permits arbitrary actual terminal values compatible with that border, no terminal compression or terminal congruence beyond those inputs is required.

### Audited theorem

> **Complete terminal-aware $J$-theorem.**  
> At every sufficiently large original retained index, for every
> $z,v\in\mathbb Z_3[y]_{<\delta}$, and for both complete producers,
> 

$$
> \boxed{
> l_{\alpha,z}^{T}B_\alpha^{-1}l_{\alpha,v}\in9\mathbb Z_3,
> \qquad \alpha=c,\mathrm{act}.
> }
>
$$


> Equivalently,
> 

$$
> \mathscr L_\alpha^TB_\alpha^{-1}\mathscr L_\alpha\in9M,
> \qquad
> \frac{\mathscr L_\alpha^TB_\alpha^{-1}\mathscr L_\alpha}{3}
> \equiv0\pmod3.
>
$$


> The whole literal first radical is the domain. The actual last middle column and its leading terminal combination are retained.

### Audit table

| Item | Verdict |
|---|---|
| Exact raw moment divided by $3^{29}$, plus complete prefix source | **PASS** |
| Literal whole first-radical domain | **PASS** |
| Ordinary/last-middle distinction | **PASS** |
| Interior $B\bmod9$, including prefix Schur correction | **PASS** |
| Complete interior $l\bmod9$, including virtual prefix selector | **PASS** |
| Finite-supported $X_z=y^aVz$ | **PASS** |
| First-coordinate and mixed contractions | **PASS** |
| Both cross terms in the exact symmetric lift | **PASS** |
| Every current-digit coefficient of actual $\theta$ | **PASS: zero** |
| Actual/core transfer | **PASS** |

---

## 9. The parent’s next boundary reduction: verification and paid hypotheses

Write the exact finite block as


$$
B=
\begin{pmatrix}
b_{00}&e^T&a\\
e&C&w\\
a&w^T&b_{TT}
\end{pmatrix},
\qquad
l_z=(l_{0,z},l_{I,z},l_{T,z}),
$$


where $C$ is the actual finite interior unit block.

Eliminating $C$, define


$$
s=b_{00}-e^TC^{-1}e,
$$




$$
a'=a-e^TC^{-1}w,\qquad
c'=b_{TT}-w^TC^{-1}w,
$$




$$
t_z=l_{0,z}-e^TC^{-1}l_{I,z},
$$




$$
u_z=l_{T,z}-w^TC^{-1}l_{I,z},
\qquad
\kappa_{zv}=l_{I,z}^TC^{-1}l_{I,v}.
\tag{9.1}
$$



The hypotheses are now proved at the required scopes:

* $e\in3M$;
* $b_{00}\in9\mathbb Z_3$;
* $a'$ is a unit;
* $C^{-1}l_{I,z}-X_z\in3M$;
* $e^TX_z\in9\mathbb Z_3$;
* $l_{0,z}\in9\mathbb Z_3$.

Hence


$$
s,t_z\in9\mathbb Z_3.
$$


The exact two-dimensional inverse gives


$$
l_z^TB^{-1}l_v
=
\kappa_{zv}
+
\frac{
c't_zt_v-a'(t_zu_v+u_zt_v)+su_zu_v
}{
sc'-(a')^2
}.
\tag{9.2}
$$


The border term is in $9\mathbb Z_3$; the audited theorem therefore also gives $\kappa_{zv}\in9\mathbb Z_3$.

Define


$$
\sigma=s/9,\qquad
\tau_z=t_z/9,\qquad
\theta_z=u_z/a',\qquad
\kappa_{7,zv}=\kappa_{zv}/9
\pmod3.
$$


Since $t_zt_v\in81\mathbb Z_3$, (9.2) reduces to


$$
\boxed{
\frac{l_z^TB^{-1}l_v}{9}
\equiv
\kappa_{7,zv}
+\tau_z\theta_v+\theta_z\tau_v
-\sigma\theta_z\theta_v
\pmod3.
}
\tag{9.3}
$$



Thus the parent reduction **passes**. Higher terminal digits are unnecessary for this particular quotient, but the leading actual $\theta$ remains necessary unless its coefficients are separately proved zero.

---

## 10. A new evaluated next coefficient: $\sigma_c=0$

The old displayed $B_{00}$-bands alone do not establish this statement. The following argument includes the complete ordinary raw source and the finite prefix return.

### 10.1 Complete raw first corner modulo $27$

Let


$$
d_J=R_*+\ell=\frac{249P-6\chi+3}{2}.
$$


The compact raw first-corner polynomial is


$$
(1-y)^D(\beta+3y)y^{2d_J}.
$$


Its maximal denominator is below $41Q$, so the largest possible pole valuation gives normalization cost only $3^{-1}$.

Every pole relevant modulo $27$ is divisible by $Q$, hence by $243$ for sufficiently large original indices. At such a pole denominator $d$, put


$$
k=\frac{d-1}{2}-2d_J.
$$


Then


$$
k\equiv-\frac72\pmod{243},\qquad
k-1\equiv-\frac92\pmod{243}.
$$


Consequently


$$
v_3(k)=0,\qquad v_3(k-1)=2.
$$


Also $v_3(D)=5$. The elementary identity


$$
\binom Dk=\frac Dk\binom{D-1}{k-1}
$$


therefore gives


$$
v_3\binom Dk\ge5,\qquad
v_3\binom D{k-1}\ge3.
$$


After including the explicit factor $3$ on the second term and the worst pole cost $3^{-1}$, both contributions vanish modulo $27$.

Poles with normalized weight divisible by $27$ are already inactive. Thus the complete raw corner $T_{00}$ is zero modulo $27$.

Notice that the $3y$-term has been paid separately. The argument does not claim the stronger raw divisibility by $81$.

### 10.2 Complete finite prefix corner

Let $s_\circ=k_0+\ell$. From (4.7), equivalently,


$$
\mathsf A^{-1}\mathbf q_0
\equiv\tfrac12e_{s_\circ}+3h\pmod9,
$$


where


$$
h=T_0^{-1}b_{5,\ell}
-e_{s_\circ+2Q}+e_{s_\circ+Q}+2e_{s_\circ-Q}.
$$


Then


$$
\mathbf q_0^T\mathsf A^{-1}\mathbf q_0
\equiv
\tfrac14\mathsf A_{s_\circ s_\circ}
+3e_{s_\circ}^TT_0h
\pmod9.
$$



The first term is zero modulo $9$, by the actual coefficient bounds in the prefix matrix. The second involves


$$
U_{S+2Q}-U_{S-2Q}+U_{S-Q}+2U_{S+Q}.
$$


All but $U_{S-Q}$ are out of range. The latter has a $3$-unit index and vanishes modulo $3$, since $U\bmod3$ is supported on $243\mathbb Z$.

Therefore


$$
\mathbf q_0^T\mathsf A^{-1}\mathbf q_0\in9\mathbb Z_3,
$$


and its prefactor $3$ in (2.1) gives


$$
\boxed{(B_c)_{00}\equiv0\pmod{27}.}
\tag{10.1}
$$



### 10.3 The interior Schur correction to $s$

Put


$$
\widehat R=S-Q.
$$


From (3.2), for $1\le i\le N-2$,


$$
(e/3)_i
\equiv U_{\widehat R-i}-\mathbf1_{i=N-2}\pmod3.
\tag{10.2}
$$


The first term is supported only on


$$
i\equiv\widehat R\equiv118\pmod{243};
$$


the final basis vector has


$$
N-2\equiv117\pmod{243}.
$$


Meanwhile, (6.2) can be nonzero only when


$$
N-1-i-j\equiv0\pmod{243},
\qquad N-1\equiv118\pmod{243}.
$$


For the three possible support pairings, the residues are $125,126,127$, none zero modulo $243$. Hence


$$
(e/3)^TC_0^{-1}(e/3)=0\pmod3.
$$


Together with (10.1), this proves


$$
\boxed{
\sigma_c
=\frac{(B_c)_{00}-e_c^TC_c^{-1}e_c}{9}
\equiv0\pmod3.
}
\tag{10.3}
$$



This is a source-specific next-digit value, not an inference from the old modulo-$9$ formula.

---

## 11. Explicit actual/core transport at the next $J$-digit

The next actual coefficient is not determined by $\sigma_c=0$. It is useful to isolate precisely the original source values that remain.

For ordinary inputs $p,q$, define the paid complete comparison form


$$
\mathcal E(p,q)
=
\frac{
G_{\mathrm{act}}(F_{\mathrm{act}}[p],F_{\mathrm{act}}[q])
-G_c(F_c[p],F_c[q])
}{3^{29}}
\pmod3.
\tag{11.1}
$$


This is integral by the established comparison. Its source-specific, complete stationary expression is


$$
\boxed{
\mathcal E(p,q)=
\frac{
\mathcal M(\delta Q\,F_c[p]F_c[q])
-
b_p^TE_{\mathrm{act}}^{-1}b_q
}{3^{29}}
\pmod3,
}
\tag{11.2}
$$


where


$$
\delta Q=Q_{\mathrm{act}}-Q_c,\qquad
b_p=\mathcal M(\delta Q\,W\,F_c[p]).
$$


Both terms are retained. Formula (11.2) follows by correcting $F_c[p]$ against the actual $W$-matrix; the core $W$-cross is exactly zero.

Define the following explicit ordinary polynomials:


$$
p_\circ=y^{d_J},
$$




$$
P_z=2(y^{14P}+y^{41P}+y^{95P})V(y)z,
$$




$$
T_z=y^{131P}V(y)z.
\tag{11.3}
$$


Here $P_z$ is the evaluated leading prefix inverse image. The last identity is not a new coordinate guess:


$$
y^{R_*+\ell}X_z
=y^{R_*+\ell+a}Vz
=y^{131P}Vz.
$$


All these polynomials are inside the ordinary degree cutoff. In particular,


$$
\deg T_z\le133P+\delta-1<\nu-2.
$$



### Proposition — finite-supported actual next-jet transport

At the original indices,


$$
\boxed{\sigma_{\mathrm{act}}=-\mathcal E(p_\circ,p_\circ),}
\tag{11.4}
$$




$$
\boxed{
\tau_{\mathrm{act},z}-\tau_{c,z}
=
\mathcal E(p_\circ,T_z-P_z),
}
\tag{11.5}
$$


and


$$
\boxed{
\begin{aligned}
\kappa_{7,\mathrm{act},zv}-\kappa_{7,c,zv}
={}&\mathcal E(T_z,T_v)
-\mathcal E(P_z,T_v)
-\mathcal E(T_z,P_v).
\end{aligned}}
\tag{11.6}
$$



#### Proof

The prefix comparisons give


$$
\delta\mathsf A\in27M,\qquad
\delta d\in81M,\qquad
\delta Z\in27M.
$$


Also


$$
\delta\mathbf q_i/9
=-\mathcal E(y^{R_*+\ell+i},F_{\rm pref}\text{-input})\pmod3.
$$


The prefix Schur correction in $B$ has an additional factor $3$. Thus, on the ordinary first/interior block,


$$
\delta B_{ij}/9
=-\mathcal E(y^{R_*+\ell+i},y^{R_*+\ell+j})\pmod3.
\tag{11.7}
$$


The raw general/one difference in $l$ is in $27M$. Consequently


$$
\delta(l_z)_i/9
=-\mathcal E(y^{R_*+\ell+i},P_z)\pmod3.
\tag{11.8}
$$



For $s=b_{00}-e^TC^{-1}e$, changing $e$ by $9M$ or $C$ by $9M$ changes the latter quadratic only in $27M$, since $e\in3M$. Equations (10.3) and (11.7) give (11.4).

For $t_z=l_{0,z}-e^TC^{-1}l_{I,z}$, the term involving the change of $C^{-1}l_I$ is in $27M$. Using its leading inverse image $X_z$, (11.7)–(11.8) give (11.5).

Finally, the first-order inverse variation of


$$
l_{I,z}^TC^{-1}l_{I,v}
$$


modulo $27$ gives both coupling variations and the inverse variation. Substituting (11.7)–(11.8) and the leading inverse images $X_z,X_v$ proves (11.6). ∎

These formulas involve the explicit three tail bands $131,132,133$, the nine prefix bands


$$
14,15,16,\ 41,42,43,\ 95,96,97,
$$


and the one first-coordinate input $p_\circ$. They do not make A4’s separate actual prefix-$\Delta_A$ calculation a prerequisite: no prefix-prefix value $\mathcal E(P_z,P_v)$ occurs in (11.6).

### What is still not evaluated

The remaining next-$J$ data are:

1. the core values $\tau_{c,z}$ and $\kappa_{7,c,zv}$, requiring the omitted $9$-weighted source and finite inverse layers;
2. the complete source contractions (11.4)–(11.6), with the actual forcing coefficients and the $W$-return in (11.2);
3. the leading **actual** terminal value
   

$$
\theta_{\mathrm{act},z}
   =
   a_{\partial,\mathrm{act}}^{-1}
   \bigl(\overline{l_{\mathrm{act},T,z}}
          -w_{\mathrm{act}}^T\overline X_z\bigr).
$$



These are open evaluations, not values established by naming the forms.

The obstruction is precise. For example, the abstract perturbation


$$
B\longmapsto B+9e_0e_0^T
$$


preserves every proved modulo-$9$ contraction and the finite unit border, but changes $\sigma$ by $1$. Similarly, a perturbation $l_z\mapsto l_z+9\lambda_z e_0$ changes $\tau_z$. These are not claimed to be actual producer perturbations; they show why the accepted depth bounds cannot determine the next source digits.

Thus (9.3) is a valid reduction, and (10.3), (11.4)–(11.6) are concrete advances, but the requested complete secondary value remains unproved.

---

## 12. Original Range III subwindow and complete-return consequences

The accepted density theorem supplies infinitely many original indices in


$$
\frac3{25}<\frac{\chi}{P}<\frac{31}{250}.
\tag{12.1}
$$


On this subwindow,


$$
\delta=\chi-1,\qquad
t_{\rm ker}=\Pi-c,\qquad
k=\delta-t_{\rm ker}=3\chi-\Pi-1>0.
$$


The literal integer second-kernel amplitudes are


$$
H_i=(1-y)^\Pi y^{L_*+i},
\qquad 0\le i<k.
\tag{12.2}
$$


They are obtained by taking $z=(1-y)^{t_{\rm ker}}y^i$ in the whole-radical theorem. No reduction of their higher binomial digits is used to replace the literal columns.

The audited $J$-quadratic has physical multiplier $-3^5$. Therefore (0.1) places its physical return in $3^7M$, and its physical-$6$ contribution is zero. The next physical-$7$ contribution has the sign


$$
-\frac{l_z^TB^{-1}l_v}{9}\pmod3.
$$



The independently passed prefix theorem likewise puts its physical return in $3^7M$ on the stated complete second kernels. Consequently the local physical-$6$ ledger now retains the established moment contribution and the still-assigned rank-$b$ and first physical-$4$ returns. This report does not evaluate their sum or certify a complete matrix/force normalization owned by another assignment.

The two diagonal frames remain distinct:


$$
\lambda_{\rm new}
=\lambda^{\rm pref}
-\frac13f_J^TB^{-1}f_J
-\frac19f_b^TA_b^{-1}f_b
\in3^{-2}\mathbb Z_3,
$$


whereas


$$
\lambda_4
=\lambda_{\rm new}
-\frac1{3^4}f_C^TA_4^{-1}f_C
\in3^{-4}\mathbb Z_3.
$$


No unit numerator is assumed.

The new physical-$5$ complement has inverse cost $3^{-5}$; both its matrix and kernel-pivot directional returns begin at physical $7$. They must be present in every eventual whole-$7$ assembly.

| Operation or return | Retained payment/status |
|---|---|
| Complete $W$-projection | $3^{-1}$ inverse allowance |
| Prefix normalization | $3^{26}$, unit normalized inverse |
| Residual $d$ | division by $3^{28}$ |
| Raw $l$-source | division by $3^{29}$ |
| Finite $J$-block | source normalization $3^{27}$; relative inverse cost $3^{-1}$ |
| Complete $J$-quadratic | now proved in $9M$ |
| Rank-$b$ return | full $3^{-2}$ payment retained |
| First physical-$4$ complement | full $3^{-4}$ payment and return retained |
| New physical-$5$ complement | return active at $7$ |
| Whole physical-$7$ moment | source $34$ not supplied by source $33$ |
| Original contents and primitive normalization | unchanged |

---

## 13. Complete forcing and unchanged global normalization

The actual producer remains


$$
Q_{\mathrm{act}}=Q_c+3^7\mathscr R.
$$


Retain


$$
F_{\rm fac}=(n-1)!,
$$




$$
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},
\qquad
\gamma_0=1,\quad\gamma_1=0,\quad
\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1},
$$




$$
h_{\rm vec}
=T_n^{-1}\left(\binom{n+a}{a}\gamma_{n+a}\right)_{a=0}^{n-1},
$$




$$
u_a=\frac{F_{\rm fac}(-2)^a}{a!},\qquad v=T_n^{-1}u,
$$




$$
b_{\rm force}=-n-66,
$$




$$
\mathbf t
=
3nh_{\rm vec}
+(b_{\rm force}+6)e_{n-1}
+\frac{2b_{\rm force}}{n-1}e_{n-2},
$$




$$
\xi=\frac{u^T\mathbf t}{F_{\rm fac}^2-u^Tv}.
$$


The actual signed coefficients are


$$
[x^a](3^7\mathscr R)
=-\frac{F_{\rm fac}}{a!}(t_a+\xi v_a),
\qquad0\le a\le n-1,
$$


and


$$
\mathscr R(-1)=-\frac{\xi F_{\rm fac}^2}{3^7}.
\tag{13.1}
$$


No new integrality or unit assertion about the scalar denominator is used here.

The full forcing identity remains


$$
\boxed{
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
}
\tag{13.2}
$$


Both terms, including the terminal coordinate, remain present.

The complete source recurrence is unchanged:


$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\qquad0\le t\le2n-2,
$$


with genuine resonance


$$
t_*=\frac{3^h-5}{2}.
$$



No local basis change or paid ternary division changes the actual integer column contents or the actual least simultaneous clearer $\ell_{\rm clr}$. Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the final gcd over **all primes**


$$
G=\gcd(|A_\ell|,|B_\ell|).
$$


For $B_\ell\ne0$, the actual primitive pair is


$$
q=\frac{|B_\ell|}{G},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{G}.
$$


The whole error is exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{G}\det H_{\rm complete}.
}
\tag{13.3}
$$



An irrationality proof would require, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\log G-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|\longrightarrow+\infty.
\tag{13.4}
$$


Then the nonzero whole errors would tend to zero, contradicting rationality. No such same-index whole-error theorem or actual all-prime primitive-denominator bound is established here.

---

## 14. Bounded exact-arithmetic receipt

No tools were used. No old $122$-constant receipt, sector matrix, nine-block receipt, or analytic calculation is requested again.

The small universal arithmetic used in the new audit can be independently checked with the following bounded inputs.

### Inputs

1. $0\le k\le16$, $c_k=(-1)^k\binom{30}{k}$, modulus $27$;
2. $1\le j\le13$, with $c_k=0$ for $k<0$;
3. factorial inputs
   

$$
90,\ 37,\ 53,\ 38,\ 52,
$$


   or directly $\binom{90}{37},\binom{90}{38}$, modulus $243$.

### Expected verifiable output



$$
(c_0,\ldots,c_{16})\equiv
(1,24,3,17,0,0,18,0,0,15,9,18,21,0,0,18,0)\pmod{27},
$$




$$
\left(
\frac{c_{j+3}+3c_{j-6}}9
+\mathbf1_{j=9}-\mathbf1_{j=6}
\right)_{j=1}^{13}
=
(0,0,2,0,0,1,0,0,0,0,0,2,0)
$$


in $\mathbb F_3^{13}$, and


$$
\left(c_{j+3}/3+c_{j-6}\right)_{j=1}^{13}=0
\quad\text{in }\mathbb F_3^{13}.
$$


Also,


$$
v_3\binom{90}{37}
=v_3\binom{90}{38}=4,
$$




$$
\boxed{
\binom{90}{37}\equiv
\binom{90}{38}\equiv162\pmod{243}.
}
$$



These are finite checks of universal constants. The infinite-original-family result is established by the symbolic degree, valuation, support, and finite-boundary proof—not by those finite checks alone.

No original dense-matrix computation is proposed without a separately supplied and validated original index.

---

## Conclusion

### Newly proved or independently certified

1. **A4 Turn 12’s entire new terminal-aware $J$-proof passes independent audit.**
   

$$
\boxed{
   \mathscr L_\alpha^TB_\alpha^{-1}\mathscr L_\alpha\in9M,
   \qquad \alpha=c,\mathrm{act}.
   }
$$


   It holds on the whole literal first radical. Every coefficient of the actual leading terminal parameter vanishes at the current digit.

2. **The parent’s next two-coordinate boundary reduction passes**, with all divisions and finite unit hypotheses paid.

3. **A further complete-core next coefficient is evaluated:**
   

$$
\boxed{\sigma_c=0.}
$$



4. **The actual next-jet transport is reduced to explicit ordinary source tests** in (11.4)–(11.6), using the evaluated nine prefix bands, three tail bands, and first-coordinate input, with the complete $W$-return retained.

### Exact remaining local bottleneck

The complete physical-$7$ $J$-value still requires the evaluated core quantities


$$
\tau_{c,z},\qquad \kappa_{7,c,zv},
$$


the actual source contractions in (11.4)–(11.6), and the leading actual terminal combination whenever its coefficients survive. The omitted $9$-weighted source and finite inverse terms cannot be inferred from their preceding digits.

The secondary complete evaluation is therefore **open**, not replaced by the polynomial reduction (9.3).

### Exact remaining global bottleneck

The actual contents, least simultaneous clearer, all-prime final gcd, actual primitive denominator, same-index nonvanishing, and decay of the **nonzero whole error** remain necessary. Neither this successful local audit nor the new value $\sigma_c=0$ supplies them.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi\text{ is obtained.}}
$$


