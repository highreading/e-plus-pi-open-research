> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The complete finite-prefix return on the second kernel

## Abstract and proof status

The rationality or irrationality of $e+\pi$ remains unresolved.

The new result of this report is an evaluation of the prefix contribution assigned in Turn 9. It is stronger than the previously established divisibility by $9$.

Let $\mathscr H$ denote the literal integer amplitude matrix of the **complete second kernel** in any of the already established Ranges I–III. In Range III its columns are exactly


$$
H_i(y)=(1-y)^\Pi y^{L_*+i},
\qquad 0\le i<\varepsilon.
$$


For the original complete prefix, with its original finite boundaries and normalization,


$$
\boxed{
\mathscr H^T Z_\alpha^T\mathsf A_\alpha Z_\alpha\mathscr H
\in 27\,\operatorname{Mat}(\mathbb Z_3),
\qquad \alpha=c,\mathrm{act}.
}
\tag{0.1}
$$


Consequently,


$$
\boxed{
\frac{\mathscr H^T Z_\alpha^T\mathsf A_\alpha Z_\alpha\mathscr H}{9}
\equiv0\pmod3.
}
\tag{0.2}
$$



Thus the prefix contribution to the physical sixth-digit matrix, pivot entry, mixed column, and endpoint-annihilator matrix is **zero** in the accepted second-kernel-pivot frame.

This is a uniform original-object proof, not an inference from a finite sample. Its ingredients are:

* the actual prefix matrix through modulus $27$, including all its shifted Hankel terms;
* an explicit, signed coefficient formula for the prefix residual through modulus $27$;
* the finer $P$-grid and its amplitude-dependent outer admission, checked on the literal amplitudes;
* the finite inverse and its boundary corrections, rather than an infinite-matrix inverse;
* the higher integer binomial digits of the amplitudes.

The parent’s reused density theorem supplies infinitely many **original** Range III indices in


$$
\frac3{25}<\frac{\chi}{P}<\frac{31}{250}.
$$


Therefore (0.1)–(0.2) apply at infinitely many original indices in that subwindow.

The other physical-sixth-digit returns are not erased. The terminal-aware $J$-return, rank-$b$ return, and first physical-$4$ complementary return must still be inserted at their evaluated values. The physical-$5$ complementary returns remain active at order $7$. No conclusion about the primitive denominator or the nonzero whole error follows from the prefix theorem.

---

## 1. Original objects and the exact scope of reuse

### 1.1 Original indices

All uniform assertions below concern sufficiently large original indices satisfying


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=2m-1=4^j-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


and


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$


The retained original subwindow is


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


Put


$$
Q=27P,\qquad b=Q-N_0=2R,\qquad \chi=P-R.
$$


Then


$$
N_0=25P+2\chi,\qquad D=9Q+N_0=10Q-b.
$$



No freely selected $P,\chi,r$, or rounded tuple replaces these original parameters.

We use


$$
\Pi=\frac P3,\qquad
L_*=\frac{P-1}{2},\qquad
\kappa_1=\frac{\Pi-1}{2},
$$


and


$$
\delta=\min\left\{\chi-1,\frac{P+3}{2}-3\chi\right\}.
$$


For sufficiently large original indices,


$$
243\mid P,\chi,\qquad \frac{\chi}{243}\equiv1\pmod9.
$$



### 1.2 Complete columns and physical boundary

Retain


$$
U_s=x^s\quad(0\le s<D),\qquad x=y-1,
$$




$$
z_i=x^Dy^i\quad(0\le i<\nu),\qquad \nu=D/2-1,
$$




$$
Y_t=y^t\quad(d\le t\le m),\qquad d=D+\nu,
\qquad W=[U\ Y].
$$


The physical HIGH terminal is $Y_m$.

The complete functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!.
$$


Its fixed physical cutoff is


$$
K_{\rm phys}=2n-2,
\qquad
2K_{\rm phys}+1=4H-4D+5<3^{h+1}.
$$



For the core,


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A,
$$




$$
G_c(f,g)=\mathcal M(Q_cfg),
$$




$$
E_c=G_c(W,W),\qquad
F_c[p]=x^Dp-WE_c^{-1}G_c(W,x^Dp).
$$


The actual corrected columns use the same physical $W$ and the complete actual producer.

The one-lift input associated with an amplitude $a$ is


$$
\Psi[a]
=x^{D+b}y^{k_0}(y^{3Q}+3)a(y),
\qquad k_0=\frac{3Q+1}{2}.
$$


Its complete correction against $W$ is denoted by $\mathcal F_\alpha[a]$.

The finite prefix boundary remains


$$
R_*=\frac{9Q+1}{2},\qquad
a_0=R_*-1=\frac{9Q-1}{2}.
$$


In particular,


$$
a_0=121P+L_*.
\tag{1.1}
$$


The remaining original boundaries are


$$
\tau=\frac{N_0-3}{2},\qquad
\ell=3R+1,
$$




$$
K=\{0,\ldots,\ell-1\},\qquad
J=\{\ell,\ldots,\tau-1\},
\qquad R_*+\tau=\nu.
$$


No last middle column is removed.

### 1.3 Closed inputs reused

The following are reused at their stated scope.

1. The complete $p=17$ compression, through modulus $3^{33}$, on admitted input degrees:
   

$$
G_c(F_c[p_1],F_c[p_2])
   \equiv
   K_N\mathcal J_h\!\left(x^D(\beta+3y)p_1p_2\right)
   \pmod{3^{33}},
   \tag{1.2}
$$


   where
   

$$
\mathcal J_h(B)=3^h\sum_v\frac{[y^v]B}{2v+1},
   \qquad K_N\in\mathbb Z_3^\times,\quad K_N\equiv1\pmod3.
$$



2. The original first-prefix lifting identity and its paid integrality.

3. The finite inverse of the leading prefix matrix.

4. The previous contraction theorem
   

$$
\mathscr G^TZ_c^T\mathsf A_cZ_c\mathscr G\in9M
   \tag{1.3}
$$


   on the full first radical.

5. The complete second kernels in Ranges I–III and the accepted second-kernel-pivot transport.

6. The corrected-column comparisons
   

$$
S_{\rm act}-S_c\in3^{29}M,
   \qquad
   \delta S(p,\Psi[a])\in3^{32}.
   \tag{1.4}
$$



The source-$33$ moment calculation is closed and is not rederived here.

---

## 2. The complete second-kernel amplitudes and their finite gaps

Put


$$
c=2\chi.
$$



In Ranges I–II, write


$$
k=
\begin{cases}
\delta,&\text{Range I},\\
\delta-B_1,&\text{Range II},
\end{cases}
\qquad
B_1=c+2\delta-1-\kappa_1.
$$


The complete second kernel has literal integer amplitude columns


$$
H_i=(1-y)^c y^{L_*+i},
\qquad 0\le i<k.
\tag{2.1}
$$



In Range III, put


$$
t=\Pi-c,\qquad k=\varepsilon=\delta-t>0.
$$


Then the complete second-kernel amplitudes are exactly


$$
H_i=(1-y)^\Pi y^{L_*+i}
=(1-y)^c y^{L_*}(1-y)^t y^i,
\qquad 0\le i<k.
\tag{2.2}
$$



The following already established strengthened gaps are essential:


$$
\begin{array}{ll}
\text{Ranges I–II:}&c+2k-2\le\kappa_1-120,\\[1mm]
\text{Range III:}&t+2k-2\le\kappa_1-120.
\end{array}
\tag{2.3}
$$


Also, in Range III,


$$
0<t<\Pi/3.
$$



For uniform notation, set


$$
(e,\eta,w)=
\begin{cases}
(c,0,c),&\text{Ranges I–II},\\
(\Pi,t,t),&\text{Range III}.
\end{cases}
\tag{2.4}
$$


Thus


$$
H_i=(1-y)^e y^{L_*+i},
\qquad e=c+\eta,
$$


and


$$
w+2k-2\le\kappa_1-120.
\tag{2.5}
$$



Every literal amplitude is admitted:


$$
\deg H_i\le L_*+c+\delta-1\le R.
\tag{2.6}
$$


The last inequality follows directly from the defining upper bound on $\delta$.

For sufficiently large original indices,


$$
i+\eta+1\le\delta<\kappa_1.
\tag{2.7}
$$


This inequality, not an infinite-support convention, will pay the finite convolution boundaries.

### Infinite original Range III scope

The supplied density reuse proves infinitely many original tuples in


$$
\frac3{25}<\frac{\chi}{P}<\frac{31}{250}.
$$


On this interval,


$$
\delta=\chi-1,
\qquad
\varepsilon=3\chi-\frac P3-1>\frac{2P}{75}-1,
$$


and


$$
\frac{32P}{375}<t<\frac{7P}{75}.
$$


Thus the Range III theorem below has an infinite original-index scope. This uses the supplied rotation theorem; it does not substitute a scaled auxiliary family.

---

## 3. Exact prefix normalization and the precision payment

With the sign fixed by the original prefix audit,


$$
(\mathsf A_\alpha)_{pq}
=-\frac{G_\alpha(F_{\alpha,p},F_{\alpha,q})}{3^{26}},
\qquad 0\le p,q\le a_0.
\tag{3.1}
$$



The exact first-prefix lift is


$$
X_\alpha=3P_G+9Z_\alpha.
$$


Here $P_Ga$ is the prefix coefficient vector of $x^by^{k_0}a$. This polynomial is inside the actual prefix because


$$
k_0+b+R=k_0+3R<a_0.
$$



The polynomial identity


$$
y^{R_*}x^ba+3x^by^{k_0}a
=x^by^{k_0}(y^{3Q}+3)a
$$


and linearity of complete correction give


$$
\boxed{
\mathsf A_\alpha Z_\alpha=d_\alpha,
\qquad
(d_\alpha)_{pa}
=\frac{G_\alpha(F_{\alpha,p},\mathcal F_\alpha[y^a])}{3^{28}}.
}
\tag{3.2}
$$


Thus the $3^{28}$ division is the original paid division, not a newly imposed normalization.

The source comparisons imply


$$
\mathsf A_{\rm act}-\mathsf A_c\in27M,
\qquad
d_{\rm act}-d_c\in81M.
\tag{3.3}
$$


Since the prefix inverse is a unit inverse,


$$
d_{\rm act}^T\mathsf A_{\rm act}^{-1}d_{\rm act}
\equiv
d_c^T\mathsf A_c^{-1}d_c\pmod{27}.
\tag{3.4}
$$


It therefore suffices to evaluate the core expression modulo $27$, after which the actual prefix follows at exactly the required precision.

### Why source $33$ is sufficient here

For this prefix calculation:

* $\mathsf A\bmod27$ needs the ordinary pairing modulo $3^{29}$;
* $d\bmod27$ needs the prefix/one-lift pairing modulo $3^{31}$.

The available source-$33$ compression is stronger than both requirements. Its stationary error becomes an error in $3^7$ for $\mathsf A$ and in $3^5$ for $d$. Neither can affect the numerator modulo $27$, hence neither can affect its paid division by $9$ modulo $3$.

All prefix and one-lift input degrees satisfy the admitted degree bound. The largest compact degrees in this calculation are below $19Q+R+1$, so every relevant compact pole is below $39Q$ and remains inside the previously proved physical cutoff. The complete correction against $W$, including $Y_m$, is still present.

No source-$34$ assertion is required for the theorem proved here.

---

## 4. The actual finite prefix matrix through modulus $27$

Let


$$
U(y)=(1-y)^{N_0}.
$$


For every integer $s$, define the finite matrix


$$
(T_s)_{pq}=U_{a_0+s-p-q},
\qquad 0\le p,q\le a_0,
\tag{4.1}
$$


with coefficients outside $0,\ldots,N_0$ equal to zero.

Thus


$$
T_0=A_0,\qquad T_{-1}=A_-,
\qquad T_{3Q}=A_+.
$$



Since the original arithmetic gives $A\equiv0\pmod{243}$,


$$
\beta=-71-A\equiv10\pmod{27}.
\tag{4.2}
$$



We first derive the matrix before inserting this numerical residue.

Because $N_0$ and $9Q$ are odd,


$$
x^D=(1-y)^{9Q}U(y).
$$


At the required precision,


$$
(1-y)^{9Q}\equiv(1-y^Q)^9\pmod{27}.
\tag{4.3}
$$



At the $27Q$ pole, the finite prefix admits only the bands with exponents $kQ$, $4\le k\le9$. Their coefficients are


$$
\begin{array}{c|rrrrrr}
k&4&5&6&7&8&9\\ \hline
(-1)^k\binom9k&126&-126&84&-36&9&-1.
\end{array}
$$


After the negative prefix normalization in (3.1), this gives


$$
\begin{aligned}
&\beta T_0+3T_{-1}
-9\beta T_Q+9\beta T_{2Q}-3\beta T_{3Q}\\
&\hspace{17mm}
+18\beta T_{4Q}+9\beta T_{5Q}
-9T_{3Q-1}
\pmod{27}.
\end{aligned}
\tag{4.4}
$$



At the $9Q$ pole, the complete contribution is


$$
-3\beta T_0-9T_{-1}+9\beta T_{-3Q}\pmod{27}.
\tag{4.5}
$$



The unit-$3Q$ poles that can occur are


$$
3Q,\quad15Q,\quad21Q,\quad33Q.
$$


Their finite coefficient matrices occur in two matching pairs. The first and third have denominator units equal modulo $3$, as do the second and fourth; the signs from $1-y^{9Q}$ are opposite. Their complete sum is therefore zero modulo $27$. No outer pole is added or deleted.

Combining (4.4)–(4.5),


$$
\begin{aligned}
K_N^{-1}\mathsf A_c\equiv{}&
-2\beta T_0-6T_{-1}-3\beta T_{3Q}\\
&+9\bigl(
\beta T_{-3Q}-\beta T_Q+\beta T_{2Q}
+2\beta T_{4Q}+\beta T_{5Q}-T_{3Q-1}
\bigr)
\pmod{27}.
\end{aligned}
\tag{4.6}
$$



Inserting $\beta\equiv10\pmod{27}$, define


$$
E=-2T_{-1}-T_{3Q},
\tag{4.7}
$$




$$
F=T_{-3Q}-T_Q+T_{2Q}+2T_{4Q}+T_{5Q}-T_{3Q-1}.
\tag{4.8}
$$


Then the fully numerical normalized formula is


$$
\boxed{
K_N^{-1}\mathsf A_c\equiv7T_0+3E+9F\pmod{27}.
}
\tag{4.9}
$$



This retains, in particular, the two shifted $3y$-terms that distinguish the modulus-$27$ calculation from the old modulus-$9$ formula.

The common scalar $K_N$ has not been silently replaced by $1$ modulo $27$. It is restored in the returned quadratic expression below. Only $K_N\bmod3$ can matter after a previously paid division by $9$.

---

## 5. The residual $d$ through modulus $27$: coefficients and edge admission

### 5.1 The source polynomial

For $0\le p\le a_0$ and $0\le a\le R$, the compressed prefix/one-lift polynomial is


$$
(1-y)^{10Q}(\beta+3y)y^{k_0+p+a}(y^{3Q}+3).
\tag{5.1}
$$


It depends on $p,a$ only through $p+a$. This proves the needed anti-diagonal constancy at the present precision.

Both the $3y$ term and the $3$-weighted low term remain in (5.1).

### 5.2 A bounded explicit coefficient formula

For $1\le j\le122$, define the following **explicit rational number**:


$$
\boxed{
D_j=
81\,2^{270}270!
\left(
\frac1{\displaystyle\prod_{a=0}^{270}(243+2j+2a)}
+
\frac3{\displaystyle\prod_{a=0}^{270}(81+2j+2a)}
\right).
}
\tag{5.2}
$$


All factors are specified positive odd integers, at most $1027$. The two summands must be combined before asserting integrality; individual summands can have negative ternary valuation.

These constants give the actual residual:


$$
\boxed{
K_N^{-1}d_{pa}
\equiv
\sum_{j=1}^{122}D_j
\left(
10\,\mathbf1_{p+a+1=jP}
+
3\,\mathbf1_{p+a+2=jP}
\right)
\pmod{27}.
}
\tag{5.3}
$$



Here and below $d=d_c$; by (3.3), the same formula gives $d_{\rm act}\bmod27$.

This is not an unnamed source sum. Formula (5.2) specifies every anti-diagonal constant by two bounded products, with the signs and both weights already evaluated.

#### Derivation of (5.2)

Put $M=p+a+\sigma$, with $\sigma=1$ for $\beta$ and $\sigma=2$ for $3y$. When $M=jP$, all relevant observations of $(1-y)^{270P}$ occur at exponents $aP$.

For $0\le a\le270$,


$$
\binom{270P}{aP}\equiv\binom{270}{a}\pmod{243}.
\tag{5.4}
$$


A direct proof is available without an external binomial-congruence theorem. For $3\mid n$ and $a>0$,


$$
\frac{\binom{3n}{3a}}{\binom na}
=
\prod_{\substack{1\le i\le3a-1\\3\nmid i}}
\left(1-\frac{3n}{i}\right).
$$


If $27\mid n$, then $3n\in81\mathbb Z_3$. Pairing $i=3r+1,3r+2$ makes the linear reciprocal sum divisible by $3$; terms of degree at least two are still deeper. Thus this ratio is $1\pmod{243}$. Iterating proves (5.4).

The normalized pole weight is $81/d$, where $d$ is the odd denominator after removing $P$. The largest such $d$ is at most $1027$, and $v_3(d)\le6$. Therefore the modulus $243$ in (5.4) pays even the possible inverse cost $3^{-2}$.

The resulting high and low sums are evaluated by the exact identity


$$
\sum_{a=0}^{N}\frac{(-1)^a\binom Na}{c+2a}
=
\frac{2^NN!}{\prod_{a=0}^{N}(c+2a)}.
\tag{5.5}
$$


For example, equality follows by comparing the simple-pole residues of the two rational functions in $c$. Applying it with $N=270$, $c=243+2j$ and $c=81+2j$, gives (5.2).

#### Why there is no other residue class modulo $P$

At the $27Q$ pole, the high extraction lies in $4Q<k<9Q$. If $P\nmid M$, then $v_3(k)<v_3(P)$. The exact binomial valuation formula gives at least five coefficient digits on this high interval. The low extraction has at least four coefficient digits and its additional explicit factor $3$. After division by $3^{28}$, both vanish modulo $27$.

At the $9Q$ pole the high extraction is negative; the admitted low extraction is also too deep. All remaining active pole layers have still larger normalized weights. Thus (5.3) has no omitted non-$P$ residue.

### 5.3 Integrality and the old paid grids

The original first lift already proves $d$ integral.

For every $1\le j\le122$, take the admitted original amplitude index


$$
a=L_*,
\qquad
p=jP-L_*-1.
$$


Then $0\le p\le a_0$, and the second indicator in (5.3) is absent. Hence $D_j\in\mathbb Z_3$.

The previously proved residual grids now imply


$$
\boxed{
D_j\in3\mathbb Z_3\quad(9\nmid j),
\qquad
D_j\in9\mathbb Z_3\quad(3\nmid j).
}
\tag{5.6}
$$


No new division is inferred from an unproved cancellation.

Write


$$
D_j\equiv a_j+3b_j+9c_j\pmod{27},
\qquad a_j,b_j,c_j\in\{0,1,2\}.
\tag{5.7}
$$


Then


$$
a_j=0\quad(9\nmid j),\qquad
b_j=0\quad(3\nmid j).
\tag{5.8}
$$



With


$$
\widetilde d=K_N^{-1}d,
$$


one may therefore write


$$
\widetilde d=d_0+3d_1+9d_2\pmod{27},
\tag{5.9}
$$


where, explicitly,

* $d_0$ has weights $a_j$ on $p+a+1=jP$;
* $d_1$ has weights $b_j$ on $p+a+1=jP$, and $a_j$ on $p+a+2=jP$;
* $d_2$ has weights $c_j+a_j$ on $p+a+1=jP$, and $b_j$ on $p+a+2=jP$.

Thus $d_0,d_1,d_2$ have grid spacings $9P,3P,P$, respectively. The $a_j$ in the first part of $d_2$ is the higher digit of $\beta\equiv10$, and has not been dropped.

### 5.4 The newly finer outer grid point

For a general amplitude coefficient indexed by $a$,


$$
p=jP-a-\sigma,\qquad \sigma\in\{1,2\}.
$$


The finite admission is:

* $1\le j\le121$: admitted for every $0\le a\le R$;
* $j=122$: admitted exactly when
  

$$
a\ge L_*+1-\sigma;
  \tag{5.10}
$$


* $j\ge123$: not admitted.

Every literal $H_i$ has support in $L_*,\ldots,R$. Therefore **both** shifts at $j=122$ are fully admitted for every coefficient of every $H_i$. No binomial convolution is truncated at that edge.

For reference, the actual constants happen to satisfy


$$
D_{121}\equiv D_{122}\equiv0\pmod{27};
\tag{5.11}
$$


a new bounded certificate for this is given in Section 11. The proof below does not assume (5.11): it retains the admitted $j=122$ term in the $P$-grid.

### 5.5 Every coefficient of $dH_i$

Combining (5.3) with the literal integer amplitude gives


$$
\begin{aligned}
K_N^{-1}(dH_i)_p\equiv
\sum_{j=1}^{122}D_j\Bigl(&
10(-1)^{jP-p-1-L_*-i}
\binom e{jP-p-1-L_*-i}\\
&+
3(-1)^{jP-p-2-L_*-i}
\binom e{jP-p-2-L_*-i}
\Bigr)\pmod{27},
\end{aligned}
\tag{5.12}
$$


where a binomial coefficient is zero outside $0,\ldots,e$.

This formula retains the entire integer binomial polynomial. Replacing it by its reduction modulo $3$ would not justify the subsequent modulus-$27$ calculation.

---

## 6. The finite inverse and the coefficient lemmas

### 6.1 Finite inverse identities

Put


$$
V=T_0^{-1}.
$$


The accepted inverse is


$$
V_{pq}=[y^{p+q-a_0}]U^{-1}.
\tag{6.1}
$$


It is genuinely finite: if $J$ reverses $0,\ldots,a_0$ and $L_U$ is the finite lower-triangular Toeplitz matrix of $U$, then


$$
T_0=JL_U,\qquad V=L_U^{-1}J.
$$


Only coefficient indices at most $a_0$ are used.

Let $S$ be the finite forward shift,


$$
S_{r,q}=\mathbf1_{r=q+1}.
$$


Then


$$
T_{-1}=T_0S=S^TT_0,
$$


so


$$
VT_{-1}=S,\qquad T_{-1}V=S^T,
\tag{6.2}
$$


and


$$
(VT_{-1}V)_{pq}=[y^{p+q-a_0-1}]U^{-1}.
\tag{6.3}
$$



Using (4.9), the finite inverse expansion is


$$
\boxed{
(K_N^{-1}\mathsf A_c)^{-1}
\equiv
4V+6VEV+9VEVEV-9VFV
\pmod{27}.
}
\tag{6.4}
$$


Indeed, $7^{-1}\equiv4\pmod{27}$, and expansion of
$(7T_0+3E+9F)^{-1}$ through the second power of the $3$-divisible part gives exactly (6.4).

No infinite matrix is inverted.

### 6.2 Frobenius congruences used below

For $q=3^s$, $q\ge3^{r-1}$, and an integer $u$,


$$
(1-y)^{uq}
\equiv
\left(1-y^{q/3^{r-1}}\right)^{u3^{r-1}}
\pmod{3^r}.
\tag{6.5}
$$


For negative $u$, this is a congruence of power series with constant term $1$, so inversion preserves it. The congruence follows by repeated cubing, using that cubing improves an already positive ternary congruence by at least one digit.

We also need the following exact coefficient valuations. For $q=3^s$, $0<b<q$,


$$
v_3\binom{Mq}{Aq+b}
=s+v_3(M)-v_3(b)+v_3\binom{M-1}{A},
\tag{6.6}
$$


when the coefficient is in range, and


$$
v_3\binom{Mq+Aq+b-1}{Aq+b}
=s+v_3(M)-v_3(b)+v_3\binom{M+A}{A}.
\tag{6.7}
$$


For (6.6), use


$$
\binom{Mq}{Aq+b}
=\frac{Mq}{Aq+b}\binom{Mq-1}{Aq+b-1};
$$


the lower $s$ digits of $Mq-1$ are all $2$. For (6.7), use the analogous identity with numerator $Mq$; the lower $s$ digits of the remaining upper and lower arguments agree. Legendre’s formula then gives the displayed valuations.

---

## 7. Evaluation of all finite inverse paths

Let


$$
f_i=\widetilde dH_i,
\qquad
f_i=f_{0i}+3f_{1i}+9f_{2i}\pmod{27},
$$


where $f_{ri}=d_rH_i$.

We will prove


$$
\begin{array}{ll}
\text{(i)}& f_i^TVf_j\equiv0\pmod{27},\\
\text{(ii)}&(Vf_i)^TE(Vf_j)\equiv0\pmod9,\\
\text{(iii)}&(Vf_{0i})^TF(Vf_{0j})\equiv0\pmod3,\\
\text{(iv)}&(Vf_{0i})^TEVE(Vf_{0j})\equiv0\pmod3.
\end{array}
\tag{7.1}
$$


Together with (6.4), these evaluate the complete prefix contraction.

### 7.1 The base inverse path

For grid positions $rP,sP$ and shifts $\sigma,\tau\in\{1,2\}$, the exact finite convolution after absorbing the two literal amplitudes is a coefficient of


$$
U^{-1}(1-y)^{2e}
$$


at


$$
(r+s-123)P+L_*-i-j-(\sigma+\tau-2).
\tag{7.2}
$$


The admission proof in Section 5.4 justifies absorbing the **whole** binomial factors.

In terms of $\Pi$, write (7.2) as


$$
A\Pi+\kappa_1-i-j-b,
\qquad
A=3r+3s-368,\qquad b=\sigma+\tau-2.
\tag{7.3}
$$


The small residue remains above $w$, even after the additional shifts used below.

The generating functions are


$$
U^{-1}(1-y)^{2e}
=
\begin{cases}
(1-y)^c/(1-y)^{75\Pi},&\text{Ranges I–II},\\[1mm]
(1-y)^t/(1-y)^{74\Pi},&\text{Range III}.
\end{cases}
\tag{7.4}
$$



#### The $f_0$-$f_0$ term modulo $27$

Both grids are $9P$, so


$$
A\equiv10\pmod{27}.
\tag{7.5}
$$



In Range III, use


$$
(1-y)^{-74\Pi}
\equiv(1-y^{\Pi/9})^{-666}\pmod{27}.
$$


Because the small residue is above $t$ and below $\Pi/2$, only bands $9A+b'$, $1\le b'\le4$, can contribute. Formula (6.7) gives their valuations as


$$
2-v_3(b')+v_3\binom{74+A}{A}.
$$


The ternary digits $74=(2202)_3$ and $A\equiv(101)_3\pmod{27}$ force two carries. Hence every possible coefficient has valuation at least $3$.

In Ranges I–II,


$$
(1-y)^{-75\Pi}
\equiv(1-y^{\Pi/3})^{-225}\pmod{27}.
$$


Only band $3A+1$ can meet the small residue. Its valuation is


$$
2+v_3\binom{75+A}{A}\ge3,
$$


because $75=(2210)_3$ and $A\equiv10\pmod{27}$ force a carry at the $9$-digit.

Thus the $f_0$-$f_0$ term is zero modulo $27$.

#### The $f_0$-$f_1$ terms modulo $9$

Here


$$
A\equiv1\pmod9.
$$



In Range III,


$$
(1-y)^{-74\Pi}
\equiv(1-y^{\Pi/3})^{-222}\pmod9.
$$


The only possible nontrivial band has valuation


$$
1+v_3\binom{74+A}{A}\ge2,
$$


because the units digits already force a carry.

In Ranges I–II, the denominator modulo $9$ is a series in $y^\Pi$. The remaining small residue is above $c$, so the coefficient is zero.

These cross terms therefore vanish modulo $9$.

#### The terms carrying an explicit $9$

These are $f_1$-$f_1$, $f_0$-$f_2$, and $f_2$-$f_0$. Modulo $3$, the denominator in (7.4) is a series in $y^\Pi$, while the observed small residue is above the remaining numerator degree. Every coefficient is zero.

This proves (7.1)(i). The same argument tolerates an additional downward coefficient shift of at most three, by the gap $120$. In particular it proves the $T_{-1}$ part needed in (ii).

### 7.2 Finite support of the leading inverse images

Put


$$
z_{0i}=Vf_{0i}.
$$


The exact one-sided convolution uses


$$
U^{-1}(1-y)^e=(1-y)^\eta(1-y)^{-25P}.
\tag{7.6}
$$



Modulo $3$, there are constants $C_r$, determined by the actual anti-diagonal weights, such that


$$
\boxed{
(z_{0i})_{rP+i+a}
=C_r(-1)^a\binom{\eta}{a},
\quad
0\le r\le121,\quad 0\le a\le\eta,
}
\tag{7.7}
$$


and all other rows are zero. Explicitly,


$$
C_r=
\sum_{j=1}^{13}
a_{9j}\,[Y^{r+9j-122}](1-Y)^{-25}.
\tag{7.8}
$$


Only coefficient indices $0,\ldots,116$ can occur in (7.8).

The ranges in (7.7) are exact. By (2.7), the small block $i,\ldots,i+\eta$ is strictly inside both the $P$-grid and the last admitted prefix block. In particular,


$$
(z_{0i})_{a_0}=0.
\tag{7.9}
$$



Modulo $9$, the corresponding full inverse image $Vf_i$ has the form


$$
y^i(1-y)^\eta
\left(
C(y^P)+3D(y^\Pi)+3yE_1(y^P)
\right),
\tag{7.10}
$$


with the actual finite truncations


$$
0\le r\le121\quad\text{on the \(P\)-grid},
\qquad
0\le r\le364\quad\text{on the \(\Pi\)-grid}.
$$


Indeed,


$$
(1-y)^{-25P}\equiv(1-y^\Pi)^{-75}\pmod9,
$$


and its reduction modulo $3$ is a series in $y^P$. Inequality (2.7), including the possible shift by $y$, makes these finite truncations independent of the small binomial index.

### 7.3 The first $T_{3Q}$ return

Using the finite supports in (7.10), absorption of the small factors changes the observed polynomial to


$$
U(1-y)^{2\eta}
=
\begin{cases}
(1-y)^{75\Pi+c},&\text{Ranges I–II},\\
(1-y)^{76\Pi+t},&\text{Range III}.
\end{cases}
\tag{7.11}
$$



For the leading $P$-grid pair, the large coefficient index for $T_{3Q}$ is


$$
A=607-3r-3s\equiv1\pmod3.
$$



In Ranges I–II, the large factor in (7.11) is a series in $y^\Pi$ modulo $9$, and the small residue exceeds $c$.

In Range III,


$$
(1-y)^{76\Pi}
\equiv(1-y^{\Pi/3})^{228}\pmod9.
$$


The only possible band is $3A+1$. Formula (6.6) gives


$$
v_3\binom{228}{3A+1}
=1+v_3\binom{75}{A}\ge2,
$$


since $A\equiv1\pmod3$ and the units digit of $75$ is zero. Out-of-range coefficients are, of course, zero.

Terms in (7.10) carrying an explicit $3$ require only (7.11) modulo $3$. Their small residues remain above $c$, respectively $t$, so they vanish termwise.

Therefore


$$
(Vf_i)^TT_{3Q}(Vf_j)\equiv0\pmod9.
$$


Together with the shifted base-inverse identity, this proves (7.1)(ii).

### 7.4 Every $F$-term

Each matrix in $F$ is $T_s$, where $s$ is a multiple of $Q$, possibly followed by a shift of $-1$. On the exact finite support (7.7), absorption again gives (7.11).

Modulo $3$, its large factor is a series in $y^\Pi$, and the remaining residue exceeds the small numerator degree, including the one-step shift. Therefore


$$
z_{0i}^TFz_{0j}=0\quad\text{in }\mathbb F_3.
\tag{7.12}
$$


This proves (7.1)(iii), with all six matrices in (4.8) retained.

### 7.5 The second inverse correction and its finite boundary

Expand $EVE$ using $T_{-1}$ and $T_{3Q}$.

First,


$$
T_{-1}VT_{-1}=T_{-2},
$$


so this part is covered by the same shifted coefficient gap.

For the mixed terms,


$$
T_{-1}VT_{3Q}=S^TT_{3Q},
\qquad
T_{3Q}VT_{-1}=T_{3Q}S.
$$


These agree with the corresponding shifted Hankel matrix except in the last row or last column. Those are the actual finite boundary corrections. They disappear in the present contraction because of (7.9), not because an infinite shift has been substituted.

It remains to evaluate


$$
u_i^TVu_j,\qquad u_i=T_{3Q}z_{0i}.
$$



#### Range III

Here


$$
U(1-y)^t=(1-y)^{76\Pi}\equiv(1-y^\Pi)^{76}\pmod3.
$$


Consequently the complete finite support of $u_i$ is


$$
p=r\Pi+\kappa_1-i,\qquad 0\le r\le364.
\tag{7.13}
$$


The last admitted row is retained; it can be $a_0$ when $i=0$.

For two such rows,


$$
p+q-a_0=(r+s-364)\Pi+\kappa_1-i-j.
$$


But


$$
U^{-1}\equiv\frac{(1-y)^t}{(1-y^\Pi)^{76}}\pmod3,
$$


and


$$
\kappa_1-i-j>t.
$$


Every observed entry of $V$ is therefore zero. Thus $u_i^TVu_j=0$.

#### Ranges I–II

Here the exact finite support is


$$
p=rP+L_*-i-a,
\qquad 0\le r\le121,\quad 0\le a\le c,
\tag{7.14}
$$


with coefficients proportional to $(-1)^a\binom ca$. The gap in (2.3) guarantees that the whole interval in $a$ is admitted, including its finite upper endpoint.

Absorbing the two small binomial factors into $V$ gives


$$
U^{-1}(1-y)^{2c}
=\frac{(1-y)^c}{(1-y)^ {25P}}.
$$


Its observed residue modulo $P$ is $L_*-i-j$, strictly above $c$ and below $P$. Hence this coefficient is zero modulo $3$.

This proves (7.1)(iv).

---

## 8. The evaluated prefix theorem and its mixed contractions

By (6.4) and all four evaluations in (7.1),


$$
f_i^T(K_N^{-1}\mathsf A_c)^{-1}f_j\equiv0\pmod{27}.
$$


Restoring the common scalar,


$$
(dH_i)^T\mathsf A_c^{-1}(dH_j)
=
K_N f_i^T(K_N^{-1}\mathsf A_c)^{-1}f_j
\equiv0\pmod{27}.
$$


Since $\mathsf A_cZ_c=d_c$,


$$
\boxed{
\mathscr H^TZ_c^T\mathsf A_cZ_c\mathscr H\in27M.
}
\tag{8.1}
$$


Equation (3.4) gives the same assertion for the actual prefix.

The previous divisibility by $9$ was already paid on the entire first radical. The present argument evaluates the next digit of that paid expression:


$$
\boxed{
\mathcal P_6
:=
\frac{\mathscr H^TZ_\alpha^T\mathsf A_\alpha Z_\alpha\mathscr H}{9}
=0
\quad\text{in }\operatorname{Mat}(\mathbb F_3).
}
\tag{8.2}
$$



### Actual kernel-pivot contractions

In Range III, retain


$$
\gamma=(\sigma2^t)^{-1},
\qquad \sigma=(-1)^{R_*+L_*}.
$$


The leading pivot is $\gamma H_0$, and the leading endpoint-annihilating columns are


$$
H_i+H_{i+1},\qquad 0\le i<\varepsilon-1.
$$



Therefore the prefix contributions are explicitly


$$
\boxed{
a_6^{\rm pref}=0,\qquad
(w_6^{\rm pref})_i=0,\qquad
(B_6^{\rm pref})_{ij}=0.
}
\tag{8.3}
$$


The same conclusion holds in Ranges I–II with their accepted kernel pivot and adjacent-sum basis.

Because the form is zero on the **complete** second kernel, it is also zero on any correctly returned kernel direction, including the nontrivial $w_*$ appearing in A4’s different first-pivot frame. This does not identify those frames; it states that this particular bilinear contribution vanishes on the whole space in either set of kernel coordinates.

### What the theorem does not remove

The physical prefix term is multiplied by $-81$. Equation (8.1) places it in $3^7M$, not in every higher power. It can therefore contribute to the physical seventh digit.

The theorem also does not remove the first physical-$4$ complementary return. The raw literal amplitudes used above are exactly the amplitudes prescribed in the decomposition of the complete returned matrix; the separate complementary correction remains a separate term.

---

## 9. Complete sixth-digit assembly and the next precise obligation

In Range III, reuse the closed moment coefficient


$$
c_r=[y^r](1-y)^t.
$$


The complete sixth-digit matrix in the accepted common monomial-first labels now reduces to


$$
\boxed{
\begin{aligned}
(C_6)_{ij}={}&c_{\kappa_2-i-j}\\
&-\left(\frac{\mathscr L_H^TB_c^{-1}\mathscr L_H}{3}\right)_{ij}\\
&-\left(\mathscr M_H^TA_{b,c}^{-1}\mathscr M_H\right)_{ij}\\
&-\left(\mathscr C_H^TA_4^{-1}\mathscr C_H\right)_{ij}
\pmod3,
\end{aligned}
}
\tag{9.1}
$$


where


$$
\kappa_2=\frac{P/9-1}{2},
$$


and


$$
\mathscr L_H=\frac{L_c^TG\mathscr H}{3},\qquad
\mathscr M_H=\frac{M_{b,c}\mathscr H}{3},\qquad
\mathscr C_H=\frac{E_4^TT_{c,\rm red}\mathscr H}{3^5}.
$$


The prefix term has been evaluated and removed from (9.1); the other three terms have **not** been assigned zero.

Their actual mixed and annihilator contractions remain


$$
(w_6)_i=\bar\gamma\bigl((C_6)_{i0}+(C_6)_{i+1,0}\bigr),
$$




$$
(B_6)_{ij}
=(C_6)_{ij}+(C_6)_{i+1,j}
+(C_6)_{i,j+1}+(C_6)_{i+1,j+1}.
\tag{9.2}
$$



The terminal-aware $J$-calculation and the rank-$b$/first-complement calculation are separate assigned tasks. Their unavailable next residues are not inferred from their previous paid vanishings.

### 9.1 The complete diagonal and the $3^{-1}$ allowance remain unchanged

Retain exactly


$$
\lambda_{\rm new}
=\lambda^{\rm pref}
-\frac13f_J^TB^{-1}f_J
-\frac19f_b^TA_b^{-1}f_b
\in3^{-2}\mathbb Z_3.
\tag{9.3}
$$


In the different monomial-first frame,


$$
\lambda_4
=\lambda_{\rm new}
-\frac1{81}f_C^TA_4^{-1}f_C
\in3^{-4}\mathbb Z_3.
\tag{9.4}
$$


The $1/3$, $1/9$, and $1/81$ returns are all present.

The physical-$5$ complementary matrix and directional returns remain in $3^7$. They cannot alter (8.3), but they can alter $B_6\bmod9$ and $w_6\bmod9$.

The exact directional equation still permits


$$
B_6x=w_6,\qquad x\in3^{-1}\mathbb Z_3^s.
\tag{9.5}
$$


Putting $z=3x$, its necessary modulo-$9$ test depends on


$$
B_6z=3w_6\pmod9,
$$


not merely on $B_6,w_6\bmod3$. Thus the new prefix theorem is not an exact-solvability theorem for (9.5).

### 9.2 A concrete follow-on prefix jet

The new theorem makes the next prefix quantity integral:


$$
\mathcal P_{7,\alpha}
=
\frac{\mathscr H^Td_\alpha^T\mathsf A_\alpha^{-1}d_\alpha\mathscr H}{27}
\pmod3.
\tag{9.6}
$$



For the **core**, its evaluation requires


$$
\mathsf A_c\bmod81,\qquad d_c\mathscr H\bmod81.
$$


These require source precisions $30$ and $32$, respectively, and are still within the supplied source-$33$ compression. Thus there is no stationary-precision obstruction to this particular next core prefix calculation.

For the actual/core difference, define the specific original prefix jet


$$
\Delta_A=
\frac{\mathsf A_{\rm act}-\mathsf A_c}{27}\pmod3.
\tag{9.7}
$$


Let


$$
Z_{0,H}=\overline{\mathsf A_c^{-1}d_c\mathscr H}.
$$


Its columns are exactly the finite polynomials in (7.7), since the leading scalar $7$ is $1$ modulo $3$.

From (3.3), finite inverse expansion gives the proved transport law


$$
\boxed{
\mathcal P_{7,\rm act}-\mathcal P_{7,c}
=
-Z_{0,H}^T\Delta_A Z_{0,H}
\quad\text{in }\operatorname{Mat}(\mathbb F_3).
}
\tag{9.8}
$$


The $d$-difference is in $81M$, so after division by $27$ it contributes zero modulo $3$. Terms quadratic in the prefix-matrix difference are also too deep.

A concrete next prefix lemma is therefore:

> Evaluate the core expression (9.6) using the modulus-$81$ finite prefix inverse, and evaluate the complete actual producer jet (9.7) on the explicitly supported columns (7.7).

This is a source-specific next jet, not a generic claim that an unspecified higher error might matter. It remains separate from the other physical-seventh-digit contributions and from the source-$34$ moment obligation.

---

## 10. Complete producer, forcing, and primitive whole error

No part of the prefix calculation changes the actual producer


$$
Q_{\rm act}=Q_c+3^7\mathscr R.
$$



Retain


$$
F_{\rm fac}=(n-1)!,
\qquad
\gamma_0=1,\quad\gamma_1=0,
$$




$$
\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1},
$$




$$
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},
$$




$$
h_{\rm vec}
=T_n^{-1}
\left(\binom{n+a}{a}\gamma_{n+a}\right)_{a=0}^{n-1},
$$




$$
u_a=\frac{F_{\rm fac}(-2)^a}{a!},\qquad v=T_n^{-1}u,
\qquad b_{\rm force}=-n-66,
$$




$$
t=
3nh_{\rm vec}
+(b_{\rm force}+6)e_{n-1}
+\frac{2b_{\rm force}}{n-1}e_{n-2},
$$




$$
\xi=\frac{u^Tt}{F_{\rm fac}^2-u^Tv}.
$$


The signed coefficients remain


$$
[x^a](3^7\mathscr R)
=-\frac{F_{\rm fac}}{a!}(t_a+\xi v_a),
\qquad 0\le a\le n-1,
$$


and


$$
\mathscr R(-1)=-\frac{\xi F_{\rm fac}^2}{3^7}.
$$



The complete forcing identity is still


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
\tag{10.1}
$$


Neither the terminal force nor the second displayed forcing term is discarded.

The complete source recurrence remains


$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\qquad 0\le t\le2n-2,
$$


with its genuine resonance


$$
t_*=\frac{3^h-5}{2}.
$$



### Actual contents and final primitive normalization

The actual original column contents and the least simultaneous clearer
$\ell_{\rm clr}$ are unchanged. A local ternary-unit normalization, including the temporary division by $K_N$, does not redefine any global integer content or clearer.

Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,
\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the final gcd over **all primes**


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


For $B_\ell\ne0$, the actual primitive pair is


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
\tag{10.2}
$$



An irrationality proof would require, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\log g_\ell-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|
\longrightarrow+\infty.
\tag{10.3}
$$


These conditions would give nonzero integer linear forms tending to zero. If $e+\pi=a/b$ were rational, every such nonzero form would have absolute value at least $1/|b|$, giving a contradiction.

Neither (10.3) nor the required nonvanishing follows from a fixed local prefix digit. They remain open.

---

## 11. A new bounded exact-arithmetic certificate

No tool computation was performed. No old sector array, endpoint table, or source-moment constant is requested again.

The only proposed auxiliary calculation is a small certificate for the two newly exposed outer $P$-grid coefficients.

### Inputs

Use the four explicitly bounded odd products


$$
\prod_{a=0}^{270}(485+2a),\qquad
\prod_{a=0}^{270}(323+2a),
$$




$$
\prod_{a=0}^{270}(487+2a),\qquad
\prod_{a=0}^{270}(325+2a).
$$


Their largest factor is $1027$. Reuse the already established value


$$
v_3(270!)=134;
$$


there is no need to recompute the old factorial-unit table.

### Expected verifiable outputs

Each of the four odd products has valuation


$$
\boxed{135.}
\tag{11.1}
$$


For example, the first valuation is


$$
v_3(1026!)-v_3(513!)-v_3(484!)+v_3(242!)
=511-255-237+116=135.
$$


The other three use the same finite factorial-ratio identity.

Consequently, in (5.2), the high summand has valuation $3$ and the low summand has valuation $4$, for both $j=121$ and $j=122$. The expected residue output is


$$
\boxed{D_{121}\equiv D_{122}\equiv0\pmod{27}.}
\tag{11.2}
$$



This finite certificate verifies only those two universal prefix constants. The uniform theorem (8.1) is proved symbolically and does not rest on this finite check.

---

## 12. Conclusion

### New proved statement

On every sufficiently large original index in the established Ranges I–III,


$$
\boxed{
\mathscr H^TZ_\alpha^T\mathsf A_\alpha Z_\alpha\mathscr H\in27M,
\qquad \alpha=c,\mathrm{act}.
}
$$


Hence the assigned physical-sixth-digit prefix return is evaluated:


$$
\boxed{
\frac{\mathscr H^TZ_\alpha^T\mathsf A_\alpha Z_\alpha\mathscr H}{9}
\equiv0\pmod3.
}
$$


Its actual pivot, mixed, and annihilator contractions are all zero.

The proof retains the actual anti-diagonal constants, both weighted low terms, the full integer amplitudes, the finer $P$-grid edge admission, every finite inverse boundary, the complete corrected columns, and the original source cutoff.

The supplied density reuse makes the Range III conclusion valid at infinitely many original indices in the exact interval


$$
3/25<\chi/P<31/250.
$$



### Exact remaining local bottleneck

At physical order $6$, the remaining complete assembly is (9.1): the evaluated moment plus the terminal-aware $J$, rank-$b$, and first physical-$4$ complementary returns. Their previous divisibility does not determine their new residues.

If the assembled equation remains singular, its $3^{-1}$-solvability requires actual higher data, including physical-$5$ returns at $7$, actual/core corrections, and higher endpoint adaptation. The prefix’s own next actual/core jet is precisely (9.8).

### Global proof status

The actual contents, least simultaneous clearer, all-prime final gcd, primitive denominator, and same-index nonzero whole error have not been evaluated sufficiently to prove irrationality. No rationality proof is obtained either.



$$
\boxed{
\text{The prefix obligation at physical order }6\text{ is closed.}
\quad
\text{The rationality or irrationality of }e+\pi\text{ remains open.}
}
$$


