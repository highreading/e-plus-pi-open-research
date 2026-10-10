> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact radical and paid complement of the next complete-core digit

## Abstract

The rationality or irrationality of $e+\pi$ remains unresolved.

The new complete-core claims in A4 Turn 5 survive independent audit. In particular, on the unchanged sufficiently large original indices,


$$
\frac{G_c(\mathcal F_a,\mathcal F_c)}{3^{30}}
\equiv
(\mathsf H_\kappa)_{ac}\pmod3,
\qquad
Z^T\mathsf A Z\equiv0\pmod3,
$$


and


$$
\frac{T_{c,\mathrm{red}}}{81}\equiv-\mathsf H_\kappa\pmod3.
$$


The previously conditional use of the physical-terminal theorem is now unconditional at the accepted complete-core scope: that theorem and $\gamma_c=0$ are closed and are not re-audited here.

The principal new result of this report is that A4's explicit radical is the **entire radical**, not merely a subspace of it. Write


$$
R=\frac b2,\qquad \chi=P-R,\qquad
\kappa=\frac{3P-3}{2},
$$


and


$$
\delta=
\min\left\{
\chi-1,\ \frac{P+3}{2}-3\chi
\right\}.
$$


Then


$$
\boxed{\operatorname{nullity}_{\mathbb F_3}\mathsf H_\kappa=\delta},
\qquad
\boxed{\operatorname{rank}_{\mathbb F_3}\mathsf H_\kappa=R+1-\delta}.
$$


A complete radical basis is


$$
\boxed{
g_s(y)=(1-y)^{2\chi}y^s,\qquad
\frac{P-1}{2}\le s\le \frac{P-1}{2}+\delta-1.
}
$$


Its integer coefficient vectors span a saturated sublattice of the original amplitude lattice. An explicit complementary set of original monomials gives a unit block modulo $3$, and hence a paid, exact complete-core orthogonal lift through that block.

The proof reuses the archived selected graded-map method, but not any old numerical rank or an unreproduced general syzygy-gap theorem. The required specialization is proved directly by an explicit primitive syzygy and a degree argument.

These results close the finite radical/complement calculation for $\mathsf H_\kappa$. They do **not** turn growing nullity into a primitive-denominator saving. The remaining local obstruction is the complete producer and returned endpoint on this now-complete radical, followed by the higher radical Schur digits needed for a paid directional solve. The remaining global obstruction is still the same-index, all-prime primitive whole-error comparison.

---

## 1. Original objects and precise scope

### 1.1 The original index family is unchanged

All assertions about the research family concern sufficiently large indices satisfying exactly


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


and


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$


The fixed subwindow remains


$$
\frac{103}{1000}<\rho=\frac{N_0}{P_0}<\frac{104}{1000}.
$$



The original arithmetic identities are retained:


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
x=y-1,\qquad Q=27P=3^{h-29},\qquad b=Q-N_0,\qquad R=\frac b2.
$$


Then


$$
D=10Q-b,\qquad .064<\frac bQ<.073,
$$


and consequently


$$
.864<\frac RP<.9855.
$$


For the rank calculation it is convenient to use the positive integer


$$
\chi=P-R.
$$


Thus


$$
\boxed{.0145<\frac{\chi}{P}<.136.}
\tag{1.1}
$$



No independent choice of $P,r$, or $R$, is substituted for an original index. The accepted density result is used only to retain infinitely many original indices in this fixed subwindow.

### 1.2 All finite boundaries remain physical

The original coordinates are


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


and


$$
W=[U\ Y].
$$


The physical HIGH terminal is $Y_m$, not $z_{\nu-1}$.

The retained residual boundaries are


$$
R_*=\frac{9Q+1}{2},\qquad
\tau=\frac{N_0-3}{2},\qquad
\ell=\frac{3b}{2}+1=3R+1,
$$




$$
K=\{0,\ldots,\ell-1\},\qquad
J=\{\ell,\ldots,\tau-1\},
$$




$$
n_J=\tau-\ell=\frac{Q-4b-5}{2},
\qquad R_*+\tau=\nu.
$$



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


The complete core is


$$
G_c(f,g)=\mathcal M(Q_cfg),
\qquad
Q_c=(y+1)x^A(\beta+3y),
\qquad \beta=-71-A.
$$


The physically truncated pole functional is


$$
\Lambda_h(P)=3^h\sum_{v=0}^{K_{\mathrm{phys}}}
\frac{[y^v]P}{2v+1},
\qquad
K_{\mathrm{phys}}=2n-2=2H-2D+2.
$$


Its largest denominator is


$$
2K_{\mathrm{phys}}+1=4H-4D+5<3^{h+1}.
\tag{1.2}
$$


Thus $\Lambda_h$ preserves coefficientwise $3$-adic integrality and divisibility.

The corrected columns are the actual complete-core columns


$$
E_c=G_c(W,W),\qquad
F_i=z_i-WE_c^{-1}G_c(W,z_i).
$$


The prescribed one-lift inputs are


$$
\Psi_a=x^{D+b}y^{k_0+a}(y^{3Q}+3),
\qquad k_0=\frac{3Q+1}{2},
\qquad 0\le a\le R,
$$


and $\mathcal F_a$ denotes their actual correction against this same finite $W$.

### 1.3 Closed inputs used without re-audit

The following established results are reused at their stated scope:

* the actual mixed LOW/HIGH projection and its one-digit inverse loss;
* the mixed filters for $16\le p\le25$;
* the paid pole/complete-core comparison;
* the finite unit-prefix inverse and paid first-prefix lift;
* H2 and its original rank-$b$ quotient;
* the exact first $J$-return and rank-$b$-return formulas;
* the complete first producer comparisons.

The physical-terminal theorem and its consequence are now closed:


$$
[y^m]\mathcal F_a
\equiv-3^{27}\delta_{a,R}\pmod{3^{28}},
\qquad
\gamma_c=0.
\tag{1.3}
$$


They are quoted, not re-proved. In particular, their cancellation does not suppress the nonzero physical coefficient at $a=R$.

---

## 2. Audit of the compression through $3^{31}$

The extra digit in A4 Turn 5 is justified using the already admitted $p=17$ filter. No extension to $p\ge26$ is needed.

Let


$$
N=3^{16},\qquad L=3^{h-17},\qquad H=NL,
$$


and let $R_N$ be the established integral normalized Jacobi filter. For


$$
\deg p_i\le\nu-2,
$$


the trial columns are


$$
\widetilde F[p_i]=x^Dp_iR_N(y^L).
$$



### 2.1 Projection and stationary error

The established residual is in $3^{17}M$. Since the actual inverse loses one digit,


$$
r_i^TE_{\mathcal P}^{-1}r_j\in3^{33}\mathbb Z_3.
\tag{2.1}
$$


This is the paid stationary error $17+16$, rather than an unpaid substitution into a mixed pairing.

The trial remains inside the physical polynomial space:


$$
m-\deg\widetilde F[p_i]\ge\frac{L-4D+7}{2}>0.
\tag{2.2}
$$


Every nonconstant filter term has smallest exponent at least $L>d$, so it belongs to the actual HIGH span.

Put


$$
B=x^D(\beta+3y)p_1p_2.
$$


Then


$$
\deg B\le2D-5,\qquad
v_3(2s+1)\le h-26
\quad(0\le s\le\deg B).
\tag{2.3}
$$



### 2.2 The formal expansion is sufficiently precise

The exact formal identity is


$$
(1-y)^H=(1-y^L)^N
\exp\left(
-H\sum_{\substack{k\ge1\\L\nmid k}}\frac{y^k}{k}
\right).
$$


Every coefficient in the exponent has valuation at least $17$. The terms of exponential order at least two lie in $3^{34}\mathbb Z_3[[y]]$. By the physical integrality in (1.2), they remain negligible after applying $\Lambda_h$.

Set


$$
A_0(Y)=(Y-1)^NR_N(Y)^2=\sum_q a_qY^q.
$$


Then


$$
\deg A_0=2N-1,\qquad A_0(1)=0.
$$



For $c=2s+1$, the bare macro denominators satisfy


$$
v_3\left(
3^h\left(\frac1{c+2qL}-\frac1c\right)
\right)
\ge35.
$$


Therefore their complete sum is zero modulo $3^{31}$.

Here “complete” is a genuine physical statement. The largest bare coefficient index is bounded by


$$
(2N-1)L+\deg B
\le2H-L+2D-5
<2H-2D+2=K_{\mathrm{phys}}.
\tag{2.4}
$$


Thus no missing terminal macro term is concealed in the use of $A_0(1)=0$.

### 2.3 Logarithmic terms and macro completion

For a logarithmic term write


$$
k=v-qL-s,\qquad d_v=2v+1.
$$


Before multiplication by integral coefficients, its valuation is


$$
2h-1-v_3(k)-v_3(d_v).
$$



If $v_3(k)<v_3(c)$, this is at least $53$. If $v_3(k)>v_3(c)$, it is at least $43$. Hence a term can survive modulo $3^{31}$ only if


$$
v_3(k)=v_3(c),\qquad v_3(d_v)\ge h-5.
\tag{2.5}
$$


Such $d_v$ is a multiple of $L$.

For these terms,


$$
\frac1k+\frac2c=\frac{d_v-2qL}{kc}.
$$


After multiplication by $3^hH/d_v$, the error has valuation at least


$$
3h-18-v_3(d_v)-2v_3(c)\ge34.
$$


Thus $1/k$ may be replaced by $-2/c$ at the required precision.

Write


$$
d_v=(2q_0+1)L.
$$


Because $s<(L-1)/2$,


$$
k>0\quad\Longleftrightarrow\quad q\le q_0.
$$


The finite partial sum is therefore


$$
\sum_{q\le q_0}a_q
=
-[Y^{q_0}](1-Y)^{N-1}R_N(Y)^2.
\tag{2.6}
$$



The physical macro endpoint deserves explicit attention. In fact, $q_0=2N-1$ is inside the cutoff, because


$$
(4N-1)L=4H-L<4H-4D+5.
$$


At that position the partial sum is the complete sum $A_0(1)=0$. The last potentially nonzero completed term is $q_0=2N-2$, whose denominator is


$$
(4N-3)L=4H-3L<4H-4D+5.
\tag{2.7}
$$


The next macro position is outside the physical cutoff.

Adding the inactive macro denominators is also paid. If


$$
v_3(d_v)\le h-6,
$$


their scalar valuation is at least


$$
2h-1-(h-26)-(h-6)=31.
$$


Consequently the finite physical calculation completes to the established scalar $K_N$, with no boundary debt.

### 2.4 Audited conclusion

The exact Jacobi norm evaluation is reused:


$$
K_N=
-\frac{4^{2N-1}}
{\binom{N-1}{(N-1)/2}\binom{3N-1}{(3N-1)/2}}.
$$


Both denominators are ternary units, and Lucas gives


$$
\binom{N-1}{(N-1)/2}\equiv1,\qquad
\binom{3N-1}{(3N-1)/2}\equiv2\pmod3.
$$


Hence $K_N\equiv1\pmod3$.

The complete-core transfer error is in $3^hM$. Therefore


$$
\boxed{
G_c(F[p_1],F[p_2])
\equiv
K_N\,\mathcal J_h\!\left(x^D(\beta+3y)p_1p_2\right)
\pmod{3^{31}}.
}
\tag{2.8}
$$


The proposed compression survives audit, including physical macro completion.

---

## 3. Audit of every pole layer and the paid binomial unit

Let


$$
X(y)=(y-1)^{10Q},\qquad L_0=\frac Q3,
\qquad
\kappa=\frac{Q/9-3}{2}=\frac{3P-3}{2}.
$$


For sufficiently large original indices,


$$
2b+4<\frac Q6.
\tag{3.1}
$$



All relevant degrees are below $2D$. A pole capable of contributing modulo $3^{31}$ is therefore


$$
2s+1=dL_0,\qquad d\in\{1,3,\ldots,119\},
$$


with weight $3^{30}/d$.

After any of the three prescribed shifts, the extraction index has the form


$$
k=uL_0+\frac{L_0-3}{2}-w-\epsilon,
\qquad
0\le w\le2b,\quad \epsilon\in\{0,1\}.
$$


By (3.1), its residue modulo $L_0$ is strictly between $0$ and $L_0$. Thus every interior extraction is a nonmultiple of $Q/3$.

For $Q=3^q$ and $k=uQ+r$, $0<r<Q$, the established identity


$$
v_3\binom{10Q}{k}
=q-v_3(r)+v_3\binom9u
\tag{3.2}
$$


applies. The first term is at least $2$.

### 3.1 Complete layer audit

| $v_3(d)$ | Pole weight | Audit |
|---:|---:|---|
| $0$ | $3^{30}$ times a unit | Interior coefficients have valuation at least $2$; no contribution. |
| $1$ | $3^{29}$ times a unit | Again at least two coefficient digits; no contribution. |
| $2$ | $3^{28}$ times a unit | Physical poles are $3Q,15Q,21Q,33Q,39Q$. Every valid band has $u=1,4,7$, hence at least four coefficient digits. |
| $3$ | $3^{27}$ times a unit | The pole is $9Q$. Only the explicitly $9$-weighted low term can be in range; its coefficient has at least four digits. |
| $4$ | $3^{26}$ | The pole is $27Q$. Only the high term without its additional $3y$ factor can survive. |

For the $v_3(d)=2$ layer, the actual valid bands are:

* high shift: $u=1,7$, at poles $21Q,33Q$;
* middle shift: $u=1,4$, at poles $15Q,21Q$;
* low shift: $u=4,7$, at poles $15Q,21Q$.

All other extractions are outside the finite support. The extra $3y$ term only increases the valuation; it has not been omitted.

At $27Q$, the high extraction is


$$
k=\frac{9Q-3}{2}-w.
$$


It lies strictly between $4Q+Q/3$ and $4Q+2Q/3$. Since


$$
v_3\binom94=2,
$$


valuation exactly $4$ occurs only when


$$
k=\frac{40Q}{9},
\qquad\text{equivalently}\qquad w=\kappa.
\tag{3.3}
$$


Every other coefficient in this band has valuation at least $5$.

### 3.2 The unit of $\binom{90}{40}$

Removing a common factor $3$ from both indices of a binomial coefficient preserves its normalized unit modulo $3$: the products of the nonmultiples of $3$ cancel modulo $3$. Iteration reduces the normalized unit at $40Q/9$ to that of


$$
\binom{90}{40}.
$$



Legendre's formula gives


$$
v_3(90!)=44,\qquad v_3(40!)=18,\qquad v_3(50!)=22,
$$


so


$$
v_3\binom{90}{40}=4.
$$


For $n=\sum n_i3^i$,


$$
\frac{n!}{3^{v_3(n!)}}
\equiv(-1)^{v_3(n!)}\prod_i n_i!\pmod3.
$$


The ternary expansions are


$$
90=(10100)_3,\qquad
40=(1111)_3,\qquad
50=(1212)_3.
$$


All three factorial units are $1\pmod3$. The extraction index $40Q/9$ is even, so its coefficient sign is positive. Therefore


$$
\boxed{
\frac{[y^{40Q/9}](y-1)^{10Q}}{3^4}\equiv1\pmod3.
}
\tag{3.4}
$$


This division by $3^4$ is fully paid.

Since $\beta\equiv1\pmod3$, the resulting moment identities are


$$
\mathcal J_h\!\left(
x^{10Q}(\beta+3y)y^{9Q+1+w}
\right)
\equiv3^{30}\delta_{w,\kappa}\pmod{3^{31}},
\tag{3.5}
$$




$$
3\mathcal J_h\!\left(
x^{10Q}(\beta+3y)y^{6Q+1+w}
\right)\in3^{31}\mathbb Z_3,
\tag{3.6}
$$




$$
9\mathcal J_h\!\left(
x^{10Q}(\beta+3y)y^{3Q+1+w}
\right)\in3^{31}\mathbb Z_3.
\tag{3.7}
$$



### 3.3 The next complete-core matrix

For the prescribed amplitudes,


$$
B_{ac}
=x^{10Q+b}(\beta+3y)
y^{3Q+1+a+c}(y^{3Q}+3)^2.
$$


Expanding the actual finite factor $x^b$, every shift has $0\le w\le2b$. Equations (3.5)–(3.7) leave only the coefficient with


$$
w=a+c+i=\kappa.
$$


Because $b$ is even,


$$
x^b=(1-y)^b.
$$


Thus


$$
\boxed{
\frac{G_c(\mathcal F_a,\mathcal F_c)}{3^{30}}
\equiv
[y^{\kappa-a-c}](1-y)^b
=(\mathsf H_\kappa)_{ac}
\pmod3.
}
\tag{3.8}
$$



Every entry is explicitly digit-evaluated. If $s=\kappa-a-c$ lies in $[0,b]$, then


$$
(\mathsf H_\kappa)_{ac}
=(-1)^s\prod_i\binom{b_i}{s_i}\quad\text{in }\mathbb F_3;
\tag{3.9}
$$


otherwise it is zero.

Moreover $R<\kappa<2R$ on the sufficiently large original family, so


$$
(\mathsf H_\kappa)_{R,\kappa-R}=1.
\tag{3.10}
$$


The whole complete-core pairing therefore has an actual original entry of valuation exactly $30$.

---

## 4. Audit of the finite prefix and the rank-$b$ return

### 4.1 The finite prefix inverse is correct

Put


$$
a_0=R_*-1=\frac{9Q-1}{2}.
$$


The leading prefix matrix is


$$
\overline{\mathsf A}_{pq}
=[y^{a_0-p-q}](1-y)^{N_0},
\qquad 0\le p,q\le a_0.
$$


Its inverse is


$$
(\overline{\mathsf A}^{-1})_{pq}
=[y^{p+q-a_0}](1-y)^{-N_0}.
\tag{4.1}
$$



To check the finite boundary, in the matrix product a nonzero summand requires


$$
a_0-r\le q\le a_0-p.
$$


When $r\ge p$, this is exactly the finite convolution range for the coefficient of $y^{r-p}$ in


$$
(1-y)^{N_0}(1-y)^{-N_0}=1.
$$


When $r<p$, the range is empty. Thus (4.1) is the inverse of the actual finite prefix, not an infinite-prefix surrogate.

With the paid lift


$$
X=-\mathsf A^{-1}\mathsf B_KG=3P_G+9Z,
$$


the prefix residual satisfies


$$
d_{pa}=\frac{G_c(F_p,\mathcal F_a)}{3^{28}},
\qquad
\mathsf A Z=d.
\tag{4.2}
$$


The division is paid by that exact lift.

### 4.2 The support statement has the required precision

The compressed prefix-to-one-lift polynomial is


$$
x^{10Q}(\beta+3y)y^{p+k_0+a}(y^{3Q}+3).
$$


Modulo $3^{29}$, only poles at odd multiples of $3Q$ need be retained. Outside


$$
p+a+1\in L_0\mathbb Z
\quad\text{or}\quad
p+a+2\in L_0\mathbb Z,
\tag{4.3}
$$


all extraction indices are nonmultiples of $L_0=Q/3$.

At $27Q$, the high extraction lies in $4Q<k<9Q$. In these bands


$$
v_3\binom9u\ge1,
$$


so (3.2) supplies at least three coefficient digits, paying the weight $3^{26}$ through $3^{29}$. The low term has its explicit factor $3$, and at least two coefficient digits. The high extraction at $9Q$ is negative. All remaining layers have weight at least $3^{28}$, with at least two further coefficient digits.

Therefore


$$
\boxed{
\bar d_{pa}=0
\quad\text{unless one of the two conditions in (4.3) holds.}
}
\tag{4.4}
$$



### 4.3 The entire second-prefix contraction vanishes

A potentially nonzero summand of


$$
\bar d^{\,T}\overline{\mathsf A}^{-1}\bar d
$$


has


$$
p+a+\sigma=uL_0,\qquad
q+c+\tau=vL_0,\qquad
\sigma,\tau\in\{1,2\}.
$$


Since


$$
a_0=13L_0+\frac{L_0-1}{2},
$$


the inverse coefficient index $p+q-a_0$ has residue


$$
\frac{L_0+1}{2}-(a+c)-(\sigma+\tau)
\pmod{L_0}.
\tag{4.5}
$$


By $0\le a+c\le b$ and (3.1), this residue is strictly between $b$ and $L_0$.

But


$$
(1-y)^{-N_0}
=(1-y)^{b-Q}
\equiv\frac{(1-y)^b}{1-y^Q}\pmod3.
$$


Every nonzero coefficient has residue modulo $L_0$ in $[0,b]$. Hence every potentially contributing inverse coefficient in (4.5) is zero. It follows that


$$
\boxed{Z^T\mathsf A Z\equiv0\pmod3.}
\tag{4.6}
$$



Thus the next prefix-returned contraction is indeed


$$
-\frac{G_c(\mathcal F,\mathcal F)}{3^{30}}
-Z^T\mathsf A Z
\equiv-\mathsf H_\kappa\pmod3.
\tag{4.7}
$$



### 4.4 The new core rank-$b$ coupling digit is correct

Let $E_b$ be the first $b$ coordinate columns in the original $K$-window. Since the columns of $G$ are $x^by^a$, $0\le a\le R$, the matrix


$$
[E_b\ G]
$$


is integral unimodular: its high-degree triangular block has diagonal $1$.

For $0\le u<b$, compression of the cross pairing gives


$$
G_c(F_{R_*+u},\mathcal F_a)
\longleftrightarrow
x^{10Q}(\beta+3y)y^{6Q+1+u+a}(y^{3Q}+3).
$$


Here $0\le u+a<3b/2\le2b$, so the pole audit yields


$$
\frac{G_c(F_{R_*+u},\mathcal F_a)}{3^{30}}
\equiv\delta_{u+a,\kappa}\pmod3.
\tag{4.8}
$$


In particular this cross pairing is in $3^{30}\mathbb Z_3$.

The exact first-prefix identity is


$$
\frac{E_b^T\mathcal R_{c,KK}G}{27}
=
-\frac{G_c(F_{R_*+\cdot},\mathcal F)}{3^{29}}
+\left(\frac{\mathsf B_E}{3}\right)^TZ.
\tag{4.9}
$$


The first term is zero modulo $3$.

For the second term,


$$
\left(\overline{\mathsf B_E/3}\right)_{p,u}
=[y^{3Q-1-p-u}]x^{N_0}.
\tag{4.10}
$$


This follows at the required precision from


$$
x^{9Q}\equiv
y^{9Q}-3y^{6Q}+3y^{3Q}-1\pmod9;
$$


the finite extraction range excludes every band except the one beginning at $6Q$.

Combining (4.10) with the actual finite inverse (4.1) gives


$$
\left(
\overline{\mathsf B_E/3}^{\,T}
\overline{\mathsf A}^{-1}
\right)_{u,p}
=-\delta_{p,k_0+u}.
\tag{4.11}
$$


The convolution is finite: its nonnegative coefficient indices force every contributing summand to lie in $0,\ldots,a_0$.

At $p=k_0+u$, neither condition in (4.3) holds, because


$$
k_0+u+a+\sigma
=
4L_0+\frac{L_0+1}{2}+u+a+\sigma
$$


has residue strictly between $0$ and $L_0$. Hence the second term of (4.9) is also zero modulo $3$.

Finally, the accepted $\gamma_c=0$ implies


$$
L_c^TG\in3M.
$$


The cross $J$-return


$$
27E_b^TL_cB_c^{-1}L_c^TG
$$


is consequently in $81M$. Therefore


$$
\boxed{M_{b,c}\in3M.}
\tag{4.12}
$$


The exact rank-$b$ return gives


$$
81M_{b,c}^TA_{b,c}^{-1}M_{b,c}\in3^6M,
$$


and its displacement lies in $9M$.

Combining these facts with the contracted $J$-return in $3^5M$,


$$
\boxed{
\frac{T_{c,\mathrm{red}}}{81}
\equiv-\mathsf H_\kappa\pmod3.
}
\tag{4.13}
$$



This is an unconditional **complete-core** conclusion under the now-closed inputs. It is not yet an evaluation of the fully returned producer.

---

## 5. Exact rank: the displayed radical is complete

We now evaluate the outstanding finite rank problem.

### 5.1 Parameters and the candidate radical

Write


$$
L_*=\frac{P-1}{2},
$$


and define


$$
B_*=\frac{P+5}{2}-4\chi,\qquad
B_+=\max(B_*,0),\qquad
B_-=\max(-B_*,0).
$$


Then


$$
\delta=
\min\left\{
\chi-1,\ \frac{P+3}{2}-3\chi
\right\}.
\tag{5.1}
$$


The fixed window gives


$$
\chi-1>.0145P-1,
$$




$$
\frac{P+3}{2}-3\chi>.092P+\frac32.
$$


Thus $\delta>0$ for all sufficiently large original indices.

A4's upper index can be written


$$
U_*=L_*+\delta-1.
\tag{5.2}
$$


Indeed,


$$
U_*=
\min\{\kappa-R-1,\ 3R-2P\}.
$$



The proposed vectors are


$$
g_s(y)=(1-y)^{2\chi}y^s,
\qquad L_*\le s\le U_*.
\tag{5.3}
$$


Their degrees satisfy


$$
2\chi+s\le R.
$$


Since $P$ is a power of $3$,


$$
(1-y)^{2R}g_s(y)
=y^s(1-y)^{2P}
=y^s(1+y^P+y^{2P})
\quad\text{in }\mathbb F_3[y].
\tag{5.4}
$$


The row-observed coefficient interval is exactly


$$
[\kappa-R,\kappa].
$$


The exponent $s$ lies below this interval, while


$$
s+P\ge L_*+P=\kappa+1.
$$


Thus (5.3) does give $\delta$ independent radical vectors.

The remaining question is whether any further radical exists. The following proof excludes it.

### 5.2 Exact selected-map boundaries

Work in $\mathbb F_3[X,Y]$, with auxiliary homogeneous variables distinct from the original $y$. Put


$$
a=\kappa+1=\frac{3P-1}{2},
$$




$$
b'=4R+1-\kappa=\frac{5P+5}{2}-4\chi.
$$


Then


$$
\boxed{a+b'=4R+2.}
\tag{5.5}
$$


Both $a$ and $b'$ exceed $R$ in the original window.

Let


$$
\mathcal A=\mathbb F_3[X,Y]/(X^a,Y^{b'}).
$$


Consider the specific graded map


$$
\mu:\mathcal A_R\longrightarrow\mathcal A_{3R},
\qquad
F\longmapsto(Y-X)^{2R}F.
\tag{5.6}
$$


Using $Y-X$, rather than $X+Y$, keeps the original signed amplitude coordinates unchanged; the two versions are related by an invertible sign substitution.

The source has basis


$$
X^cY^{R-c},\qquad 0\le c\le R.
$$


A target monomial $X^qY^{3R-q}$ survives precisely when


$$
q<a,\qquad 3R-q<b',
$$


that is,


$$
\boxed{\kappa-R\le q\le\kappa.}
\tag{5.7}
$$


There are exactly $R+1$ such target monomials.

After reversing the rows of $\mathsf H_\kappa$, its $(i,c)$-entry is


$$
[y^{\kappa-R+i-c}](1-y)^{2R}.
$$


This is exactly the coefficient of


$$
X^{\kappa-R+i}Y^{3R-\kappa+R-i}
$$


in $(Y-X)^{2R}X^cY^{R-c}$. Thus row reversal identifies $\mathsf H_\kappa$ with (5.6), with the required source degree $R$, multiplier degree $2R$, target degree $3R$, and finite boundaries (5.5)–(5.7).

No old rank has been imported into this new matrix.

### 5.3 An explicit primitive syzygy

The relevant three forms are


$$
X^a,\qquad Y^{b'},\qquad (Y-X)^{2R}.
$$


Since


$$
a=P+L_*,
\qquad
b'=2P+B_*,
$$


the following is a homogeneous syzygy:


$$
\boxed{
S_*=
\left(
-Y^{B_+}(X^P+Y^P),\
-X^{L_*}Y^{B_-},\
X^{L_*}Y^{B_+}(Y-X)^{2\chi}
\right).
}
\tag{5.8}
$$


Its total degree is


$$
d_*=2P+L_*+B_+.
\tag{5.9}
$$



To verify it, use


$$
(Y-X)^{2P}=X^{2P}+X^PY^P+Y^{2P}.
$$


The product of the third component in (5.8) with $(Y-X)^{2R}$ is


$$
X^{L_*}Y^{B_+}
\left(X^{2P}+X^PY^P+Y^{2P}\right).
$$


The first two terms are canceled by the first component times $X^a$, and the last term by the second component times $Y^{b'}$, because


$$
B_-+B_*=B_+.
$$



Crucially, $S_*$ is primitive: its first two components have gcd $1$.

* If $B_+>0$, then $B_-=0$; the second component is a power of $X$, while the first is not divisible by $X$.
* If $B_->0$, then $B_+=0$; the first component is $-(X+Y)^P$, coprime to $X^{L_*}Y^{B_-}$.
* The case $B_*=0$ is included in the same reasoning.

Finally,


$$
\boxed{3R+1-d_*=\delta.}
\tag{5.10}
$$



### 5.4 A direct completeness argument

A kernel vector of (5.6) gives a homogeneous syzygy of total degree $3R$. Conversely, the third component of every such syzygy gives a kernel vector.

This correspondence is injective. A syzygy involving only $X^a,Y^{b'}$ has total degree at least


$$
a+b'=4R+2>3R.
\tag{5.11}
$$


Equivalently, at degree $3R$ no monomial is divisible by both $X^a$ and $Y^{b'}$, so the ideal decomposition is unique.

Let $T$ be any syzygy of total degree $3R$. Over the fraction field, both $S_*$ and $T$ are orthogonal to


$$
(X^a,Y^{b'},(Y-X)^{2R}).
$$


Their cross product must therefore be


$$
S_*\times T
=h\,(X^a,Y^{b'},(Y-X)^{2R})
\tag{5.12}
$$


for a rational function $h$.

In fact $h$ is a polynomial. A denominator of $h$, in reduced form, would have to divide both $X^a$ and $Y^{b'}$, which are coprime.

Its degree would be


$$
\deg h
=d_*+3R-(a+b'+2R)
=d_*-3R-2
=-\delta-1<0.
\tag{5.13}
$$


Therefore $h=0$, and $S_*\times T=0$.

Thus $T=fS_*$ over the fraction field. Since $S_*$ is primitive, the same denominator argument shows that $f$ is a polynomial. Its degree is


$$
\deg f=3R-d_*=\delta-1.
\tag{5.14}
$$


Consequently every degree-$3R$ syzygy is a unique degree-$(\delta-1)$ polynomial multiple of $S_*$.

Taking the third component and dehomogenizing $Y=1$, a basis is


$$
(1-y)^{2\chi}y^{L_*+j},
\qquad 0\le j\le\delta-1.
$$


These are exactly (5.3).

This proves the required specialization without invoking a general Han–Monsky gap formula.

### Theorem 5.1 — Exact original-window radical and rank

On the same sufficiently large original indices,


$$
\boxed{
\ker_{\mathbb F_3}\mathsf H_\kappa
=
\operatorname{span}_{\mathbb F_3}
\left\{
(1-y)^{2\chi}y^{L_*+j}:0\le j<\delta
\right\}.
}
\tag{5.15}
$$


Hence


$$
\boxed{\operatorname{nullity}\mathsf H_\kappa=\delta},
\qquad
\boxed{\operatorname{rank}\mathsf H_\kappa=R+1-\delta}.
\tag{5.16}
$$



Equivalently, the evaluated rank is


$$
\boxed{
\operatorname{rank}\mathsf H_\kappa=
\begin{cases}
2R-P+2,&8\chi\le P+5,\\[2mm]
\dfrac{P-1}{2}+2\chi,&8\chi\ge P+5.
\end{cases}
}
\tag{5.17}
$$


At equality the two formulas agree. The actual original integer $\chi$ determines the branch; no branch is selected by replacing the original family with auxiliary parameters.

---

## 6. Saturated radical basis and an explicit paid complement

### 6.1 The radical lifts are saturated over the integers

Let


$$
I=\{L_*,L_*+1,\ldots,U_*\},
\qquad
\mathcal C=\{0,\ldots,R\}\setminus I.
$$


Let $\mathscr G$ be the matrix of integer coefficient vectors of the polynomials $g_s$, $s\in I$, and let $E_{\mathcal C}$ contain the standard monomial columns $y^i$, $i\in\mathcal C$.

Then


$$
\boxed{[E_{\mathcal C}\ \mathscr G]\in\operatorname{GL}_{R+1}(\mathbb Z).}
\tag{6.1}
$$



Indeed, restricted to rows $I$, the coefficient matrix of $\mathscr G$ is lower triangular:


$$
[y^i]g_s=
\begin{cases}
(-1)^{i-s}\binom{2\chi}{i-s},&i\ge s,\\
0,&i<s,
\end{cases}
$$


with diagonal $1$. After the complementary identity columns are removed, the determinant is $1$, up to the ordering sign.

This also gives an explicit finite inverse for the basis change. If a vector has coefficients $v_i$, its radical-basis coordinates $t_j$, $0\le j<\delta$, are determined by


$$
t_j=
\sum_{i=0}^j
\binom{2\chi+j-i-1}{j-i}\,v_{L_*+i}.
\tag{6.2}
$$


Only coefficients through degree $\delta-1$ are used. The remaining coordinates are obtained by subtracting $\sum_jt_jg_{L_*+j}$ and reading the coefficients in $\mathcal C$.

All coefficients in (6.2) are integers; no division by $3$, or by any other prime, is introduced. Thus the displayed radical lifts span a saturated integer sublattice.

This statement concerns a saturated lift of the **modulo-$3$ radical**. It does not claim that these vectors are killed by the full $3$-adic complete-core matrix.

### 6.2 The complementary form is a unit block

Because the radical has now been proved complete, the form induced by $\mathsf H_\kappa$ on


$$
V/\ker\mathsf H_\kappa
$$


is nondegenerate. The explicitly given subspace spanned by $E_{\mathcal C}$ is a complement to that radical. Therefore


$$
\boxed{
E_{\mathcal C}^T\mathsf H_\kappa E_{\mathcal C}
\ \text{is nonsingular over }\mathbb F_3.
}
\tag{6.3}
$$



This is not a generic nonsingularity assumption. It is a consequence of the exact kernel theorem and the explicit unimodular basis (6.1).

### 6.3 An exact paid complete-core lift

Set


$$
K_c=\frac{T_{c,\mathrm{red}}}{81}\in M_{R+1}(\mathbb Z_3).
$$


The audit established


$$
\bar K_c=-\mathsf H_\kappa.
$$


Define


$$
A_c=E_{\mathcal C}^TK_cE_{\mathcal C},
\qquad
C_c=E_{\mathcal C}^TK_c\mathscr G.
$$


Then


$$
A_c^{-1}\in M(\mathbb Z_3),
\qquad
C_c\in3M.
\tag{6.4}
$$



The exact complementary correction of the radical columns is


$$
\boxed{
\widehat{\mathscr G}
=
\mathscr G-E_{\mathcal C}A_c^{-1}C_c.
}
\tag{6.5}
$$


It satisfies


$$
E_{\mathcal C}^TK_c\widehat{\mathscr G}=0,
\qquad
\widehat{\mathscr G}-\mathscr G\in3\,\operatorname{span}_{\mathbb Z_3}E_{\mathcal C}.
\tag{6.6}
$$


This is an exact original-amplitude core lift, not merely a modulo-$3$ vector.

The physical block is $81A_c$, so its inverse costs


$$
(81A_c)^{-1}=3^{-4}A_c^{-1}.
\tag{6.7}
$$


Its cross block is in $3^5M$, and its displacement is therefore in $3M$, as (6.6) records. The matrix return is


$$
81C_c^TA_c^{-1}C_c\in3^6M.
\tag{6.8}
$$


Thus the returned radical matrix is in $3^5M$, and its first divided digit obeys the paid identity


$$
\boxed{
\frac{\widehat{\mathscr G}^{\,T}T_{c,\mathrm{red}}\widehat{\mathscr G}}{3^5}
\equiv
\frac{\mathscr G^TT_{c,\mathrm{red}}\mathscr G}{3^5}
\pmod3.
}
\tag{6.9}
$$


Both contracted divisions in (6.9) are paid. The right-hand digit is not evaluated here; the point is that the newly proved unit complement does not contaminate it at this precision.

All these lifted vectors remain combinations of amplitudes $0,\ldots,R$. Their lifts through the already retained corrected columns and returns remain in the original finite polynomial spaces. No LOW/HIGH cutoff is extended.

### 6.4 Evaluated first Smith layer of the core

The preceding construction proves:



$$
\boxed{
\text{Exactly }R+1-\delta\text{ elementary divisors of }
T_{c,\mathrm{red}}
\text{ have valuation }4.
}
\tag{6.10}
$$


Every remaining elementary divisor has valuation at least $5$, or is zero.

This is an exact first-layer arithmetic statement about the complete core. It is not a claim that the full core is nonsingular, nor that the common factor contributed by those blocks survives the final primitive quotient.

---

## 7. Endpoint restriction and a sharp directional-lift interface

### 7.1 Exact endpoint-annihilator rank for the evaluation endpoint

For the unreturned evaluation functional


$$
f_0(g)=g(-1),
$$


the radical basis satisfies


$$
g_s(-1)=2^{2\chi}(-1)^s\ne0\quad\text{in }\mathbb F_3.
$$


Therefore


$$
g_s+g_{s+1},\qquad L_*\le s<U_*,
$$


is a basis of


$$
\ker\mathsf H_\kappa\cap\ker f_0.
$$


These adjacent combinations annihilate evaluation at $-1$ even over the integers.

Since $f_0$ is nonzero on the radical, $\ker f_0$ maps onto the full nondegenerate quotient. Hence


$$
\boxed{
\operatorname{nullity}
\left(\mathsf H_\kappa\big|_{\ker f_0}\right)=\delta-1,
}
$$




$$
\boxed{
\operatorname{rank}
\left(\mathsf H_\kappa\big|_{\ker f_0}\right)=R+1-\delta.
}
\tag{7.1}
$$



More generally, these exact conclusions hold for any endpoint functional whose restriction to the radical is nonzero. For an arbitrary endpoint functional one still has the unconditional lower bound $\delta-1$, but equality need not follow if the functional vanishes on the whole radical.

The actual returned endpoint must therefore be tested; it is not replaced by $f_0$.

### 7.2 Minimal hypotheses for transferring the complement to the actual producer

Let $K$ denote a fully returned integral normalized matrix on the original amplitude space; for the complete core $K=K_c$, and for the actual producer


$$
K=\frac{T_{\mathrm{act},\mathrm{red}}}{81}.
$$



The following two matrix hypotheses are sufficient to reuse the exact radical/complement split:


$$
\boxed{
\bar K\,\overline{\mathscr G}=0,
\qquad
E_{\mathcal C}^T\bar K E_{\mathcal C}
\text{ is nonsingular}.
}
\tag{7.2}
$$


They are already proved for $K_c$. They are not yet proved for the actual producer.

The second condition cannot be inferred merely from vanishing of producer residues on the radical: a producer could preserve that radical while changing the quotient. Conversely, if the full actual leading matrix is $-\mathsf H_\kappa$, both conditions follow immediately from the theorem above.

Let $f$ be the complete actual returned endpoint. A useful endpoint hypothesis is


$$
\boxed{f(g_{s_0})\in\mathbb Z_3^\times
\quad\text{for some }s_0\in I.}
\tag{7.3}
$$


A4's producer/endpoint calculation can now test (7.3) on a **complete** radical basis, rather than only a known subspace.

### 7.3 A paid conditional directional theorem

Assume (7.2)–(7.3). Permute the radical basis if necessary and write its unit endpoint pivot as $g_0$. Define


$$
q_0=\frac{g_0}{f(g_0)},
$$




$$
h_j=g_j-f(g_j)q_0,
\qquad
v_i=e_i-f(e_i)q_0\quad(i\in\mathcal C).
\tag{7.4}
$$


These are $3$-adically integral, and the basis change is unimodular over $\mathbb Z_3$. Its only division is by the certified ternary unit $f(g_0)$. It is a local basis change, not a new global content division or a redefinition of the least clearer.

In the ordered basis $[q_0,V,H]$, the endpoint is exactly $(1,0,0)$, and


$$
K=
\begin{pmatrix}
\alpha&w_C^T&w_R^T\\
w_C&A&C\\
w_R&C^T&D_0
\end{pmatrix},
\tag{7.5}
$$


where


$$
A^{-1}\in M(\mathbb Z_3),
\qquad
\alpha,w_C,w_R,C,D_0\in3M.
\tag{7.6}
$$


The endpoint-annihilator matrix and direction are


$$
B=
\begin{pmatrix}A&C\\ C^T&D_0\end{pmatrix},
\qquad
w=\binom{w_C}{w_R}.
$$



Eliminate the proved unit complement:


$$
S=D_0-C^TA^{-1}C,
\qquad
r=w_R-C^TA^{-1}w_C.
\tag{7.7}
$$


Then


$$
S\in3M,\qquad r\in3M,
$$


and


$$
\boxed{
S/3\equiv D_0/3,\qquad
r/3\equiv w_R/3\pmod3.
}
\tag{7.8}
$$


The complement return has two factors of $3$, so it is invisible in these first divided radical digits.

The exact equation $Bv=w$ is equivalent to


$$
Sv_R=r,
\qquad
v_C=A^{-1}(w_C-Cv_R).
\tag{7.9}
$$


Thus the entire remaining inverse loss is concentrated on the explicit $(\delta-1)$-dimensional endpoint-annihilating radical.

In particular:

* If $S/3$ is a unit matrix, then $v_R$ is integral because $r\in3M$; hence $v$ is integral.
* More generally, if every elementary divisor of $S$ is nonzero and has valuation at most $2$, then
  

$$
v_R\in3^{-1}M,\qquad v_C\in M,
$$


  and therefore
  

$$
\boxed{v\in3^{-1}\mathbb Z_3^{\,R}.}
  \tag{7.10}
$$



The exact directional condition is sharper than a nonsingularity condition. If


$$
USV=\operatorname{diag}(3^{e_i})
$$


is a Smith form, with unit factors absorbed, then (7.10) holds exactly when


$$
v_3((Ur)_i)\ge e_i-1
\tag{7.11}
$$


for every nonzero diagonal entry, and $(Ur)_i=0$ for every zero entry. Thus high Smith depth can still be harmless in a suitably divisible direction. Conversely, mere large nullity supplies no such directional divisibility.

The physical inverse costs are explicit:

* the complementary $81A$-block costs $3^{-4}$;
* an $S$-elementary divisor of valuation $e_i$ costs $3^{-(4+e_i)}$;
* the forcing $r\in3M$ returns one digit in the directional solution.

### 7.4 Passage to the retained $B^\sharp$

In the actual original endpoint adaptation retain


$$
B^\sharp=B+\frac{27\eta}{u}ww^T,
\qquad
u=1-27\eta\alpha\in1+27\mathbb Z_3.
$$


Suppose the preceding paid calculation gives $Bv=w$ with $v\in3^{-1}M$. Then


$$
\sigma=w^Tv\in3^{-1}\mathbb Z_3,
$$


and


$$
d=1+\frac{27\eta}{u}\sigma\in1+9\mathbb Z_3
$$


is a unit. Direct multiplication gives


$$
\boxed{
B^\sharp\left(\frac vd\right)=w,
\qquad
\frac vd\in3^{-1}M.
}
\tag{7.12}
$$



The preceding argument is not a bare rank-one inversion assertion: the new exact radical, explicit complement, physical $3^{-4}$ inverse cost, radical forcing, and remaining Smith conditions have all been identified first.

The directional bound for $B$ is invariant under integral endpoint-preserving changes of basis. Replacing an endpoint pivot by that pivot plus an integral endpoint-annihilating vector changes $B^{-1}w$ by an integral vector, up to a unimodular coordinate change. Hence the bound obtained in (7.4) transfers back to the actual retained adaptation, where (7.12) is then applied with its actual $u,\eta,w$.

### Scope of this theorem

The exact core complement and lift in Section 6 are proved. The directional conclusion of this section is conditional on the actual hypotheses (7.2), (7.3), and the stated radical Smith or directional divisibility condition. None of those actual producer/endpoint conditions is silently supplied by the core calculation.

---

## 8. Complete producer, endpoint, diagonal, and boundary obligations

The new radical calculation does not alter the complete producer:


$$
Q_{\mathrm{act}}=3P_n=Q_c+3^7\mathscr R,
$$




$$
3^7\mathscr R=\sum_{a=0}^{A+1}e_ax^a,
\qquad
e_a=-\frac{(A+1)!}{a!}(t_a+\xi v_a),
$$


with the original coefficient-vector force


$$
t=3nh_{\mathrm{vec}}
+(b_{\mathrm{force}}+6)e_{n-1}
+\frac{2b_{\mathrm{force}}}{n-1}e_{n-2},
\qquad
b_{\mathrm{force}}=-n-66.
\tag{8.1}
$$


The signed $\xi$ and its paid normalization remain present, as do


$$
\mathscr R(-1)
=-\frac{\xi((A+1)!)^2}{3^7},
$$




$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\mathrm{ret}}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
\tag{8.2}
$$



For $\alpha=c,\mathrm{act}$, retain all three first-return channels:


$$
\mathcal S_\alpha^{(2)}
=\mathcal R_{\alpha,KK}
-27L_\alpha B_\alpha^{-1}L_\alpha^T,
$$




$$
f_\alpha^{(2)}
=f_{\alpha,K}-3L_\alpha B_\alpha^{-1}f_{\alpha,J},
$$




$$
\lambda_\alpha^{(2)}
=\lambda_\alpha-\frac13
f_{\alpha,J}^TB_\alpha^{-1}f_{\alpha,J}.
\tag{8.3}
$$


The physical inverse cost is $3^{-1}$.

Likewise retain the complete rank-$b$ returns:


$$
T_{\alpha,\mathrm{red}}
=
T_{\alpha,RR}
-81M_{b,\alpha}^TA_{b,\alpha}^{-1}M_{b,\alpha},
$$




$$
f_{\alpha,\mathrm{new}}
=f_{\alpha,R}
-3M_{b,\alpha}^TA_{b,\alpha}^{-1}f_{\alpha,b},
$$




$$
\lambda_{\alpha,\mathrm{new}}
=
\lambda_\alpha^{(2)}
-\frac19f_{\alpha,b}^TA_{b,\alpha}^{-1}f_{\alpha,b}.
\tag{8.4}
$$


The physical inverse cost is $3^{-2}$.

The audit proves $M_{b,c}\in3M$. It does not prove the analogous assertion for $M_{b,\mathrm{act}}$. Nor does it evaluate the $1/9$ diagonal return. The actual endpoint in Section 7 must be formed from the complete $f_{\mathrm{act},\mathrm{new}}$, not an unreturned core evaluation.

The complete-source recurrence also remains


$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\qquad0\le t\le2n-2.
$$


Its resonance at


$$
t_*=\frac{3^h-5}{2}
$$


retains its genuine $3^h$ divisor. The highest moment remains inside the physical boundary because


$$
H-4D+5\ge0.
$$


Nothing in the finite-field radical calculation deletes this complete-source divisor.

### Division and boundary ledger

| Operation | Paid scope |
|---|---|
| Original pole functional | Cutoff $K_{\mathrm{phys}}=2n-2$, largest denominator $4n-3$ |
| $p=17$ filter | Actual LOW/HIGH span; trial degree below $m$ |
| Mixed inverse | One-digit loss |
| Stationary projection error | $3^{33}$ |
| Exponential remainder | $3^{34}$ |
| Bare macro approximation | At least $3^{35}$ |
| Logarithmic reciprocal replacement | At least $3^{34}$ |
| Physical macro completion | Last nonzero denominator $(4N-3)L$; next physical macro sum is zero |
| New small binomial normalization | $v_3\binom{90}{40}=4$, unit $1$ |
| Whole pairing observation | Division by $3^{30}$, evaluated |
| Core normalization | Division by $3^{26}$ |
| Prefix residual | Division by $3^{28}$, paid by $9Z$ |
| Finite prefix inverse | Integral; exact finite convolution |
| First $J$-inverse | Physical $3^{-1}$; contracted core return in $3^5M$ |
| Rank-$b$ inverse | Physical $3^{-2}$; core return in $3^6M$ |
| New radical basis change | Determinant $\pm1$ over $\mathbb Z$ |
| New core quotient inverse | Physical $3^{-4}$; displacement in $3M$ |
| New core radical return | In $3^6M$; contracted radical itself in $3^5M$ |
| Conditional endpoint pivot | Division only by a certified ternary unit |
| Conditional deeper radical inverse | Exact cost recorded by its Smith exponents |
| Endpoint/diagonal returns | Full $3$, $1/3$, and $1/9$ terms retained |
| Global content division | None newly asserted |

---

## 9. What is now closed, and the concrete next lemma

### 9.1 The finite rank obligation is closed

The assignment asked for more than a growing nullity lower bound. The new conclusions are:

1. **Exact nullity:** A4's $\delta$ is the full nullity.
2. **Exact rank:** formulas (5.16)–(5.17).
3. **Complete original-coordinate radical:** formula (5.15).
4. **Saturated integer lift:** the explicit unimodular basis (6.1).
5. **Paid core complement:** an actual unit quotient of dimension $R+1-\delta$.
6. **Exact core orthogonal lift:** formulas (6.5)–(6.9).
7. **Exact endpoint-annihilator rank** whenever the endpoint is nonzero on this radical.

No binomial Toeplitz determinant has been rediscovered, and no old rank has been transplanted. The graded-map method is reused; the new numerical rank is proved by the explicit primitive syzygy.

### 9.2 The precise obstruction to the nonsingular-digit route

The normalized core matrix has exact radical dimension $\delta$, with


$$
\delta>.0145P-1.
$$


Its restriction to any endpoint-annihilator has radical dimension at least $\delta-1$. Thus, for sufficiently large original indices, the next core digit cannot furnish a nonsingular endpoint-annihilator block.

At the same time, the original entry (3.10) is nonzero. Hence neither a nonsingular-next-digit argument nor another uniform whole-core digit is available.

The valid next move is a **radical return with its actual direction**, not a claim that the whole matrix becomes deeper.

### 9.3 Concrete follow-on lemma

A useful next lemma, complementary to A4's producer calculation, is now precise:

> **Actual radical directional-lift lemma.**  
> On the same original indices, use the complete producer and the exact returns (8.3)–(8.4) to verify either:
>
> 1. the actual leading radical/complement hypotheses (7.2), together with a unit returned endpoint value (7.3); or
> 2. an explicitly evaluated alternative in which the producer fills part of the displayed radical.
>
> In the first case, form the endpoint-annihilating vectors (7.4) from the complete returned endpoint. Evaluate the first divided radical matrix and direction in (7.8). If that matrix is singular, evaluate its next paid radical return sufficiently to prove the Smith bound $e_i\le2$, or the sharper directional conditions (7.11).

This is a fixed, original-object target. The amplitude vectors are explicitly known and exhaust the core radical. The new complement inverse has already been paid. What remains cannot be replaced by saying that a producer term is “higher order”: after the specified divisions its actual residues must be evaluated.

Even a successful proof of this local lemma would give only a fixed directional bound unless accompanied by an unbounded mechanism. A growing global saving would still require control through an increasing number of layers, with the complete producer, physical boundaries, endpoint, diagonal, and final nonzero scalar retained at every stage.

---

## 10. Actual contents, least clearer, all-prime gcd, and whole error

The actual original column contents and the actual least simultaneous clearer $\ell_{\mathrm{clr}}$ are unchanged. Local $3$-adic unit inverses do not redefine either object.

Retain


$$
A_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_0,
\qquad
B_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_1,
$$


and the gcd over **all primes**


$$
\boxed{g_\ell=\gcd(|A_\ell|,|B_\ell|).}
$$


For $B_\ell\ne0$, the actual primitive numerator and denominator are


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole evaluated error remains exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\mathrm{clr}}^{m+1}}
{g_\ell}\det H_{\mathrm{complete}}.
}
\tag{10.1}
$$



An irrationality proof still requires, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad
\det H_{\mathrm{complete}}\ne0,
$$


and


$$
\boxed{
\log g_\ell-(m+1)\log\ell_{\mathrm{clr}}
-\log|\det H_{\mathrm{complete}}|
\longrightarrow+\infty.
}
\tag{10.2}
$$


Then the nonzero quantity in (10.1) would tend to zero, contradicting rationality.

The exact radical rank proved here does not establish any of these nonvanishing or decay assertions. Common determinant factors produced by a large radical can occur in both distinguished cofactors and disappear in the final primitive quotient. Growing nullity is therefore not a growing primitive-denominator saving.

---

## 11. Bounded exact-arithmetic receipt

No tool computation was performed. No dense original matrix computation is needed for the exact rank theorem: its proof is symbolic and uniform.

The only optional new arithmetic receipt is the small binomial unit used in the audited next digit.

### Inputs

* integers $n=90$, $k=40$;
* modulus $243=3^5$;
* Pascal recurrence for rows $0,\ldots,90$, with integer addition modulo $243$;
* the finite Legendre sums for $90!,40!,50!$.

There are $4186$ entries in these Pascal rows, and fewer than $4200$ additions are required.

### Expected verifiable outputs



$$
\boxed{\binom{90}{40}\equiv81\pmod{243},}
$$




$$
v_3(90!)=44,\qquad v_3(40!)=18,\qquad v_3(50!)=22.
$$


Hence


$$
\boxed{
v_3\binom{90}{40}=4,
\qquad
\binom{90}{40}/81\equiv1\pmod3.
}
$$



These outputs verify only that universal constant. They do not verify an original index, establish an infinite family by computation, or substitute for the rank and boundary proofs above. No closed terminal constant or expensive earlier calculation is reopened.

---

## 12. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Original mixed projection and admitted $p\le25$ filters | Reused at established scope |
| Physical-terminal theorem and $\gamma_c=0$ | Closed; not re-audited |
| Compression through $3^{31}$, including physical macro completion | Independently audited and valid |
| Every $dQ/3$ pole layer and the $\binom{90}{40}$ unit | Independently audited and valid |
| Next complete-core digit $\mathsf H_\kappa$ | Evaluated |
| Finite second-prefix contraction | Evaluated: zero |
| Core rank-$b$ coupling and return | Evaluated: $M_{b,c}\in3M$, return in $3^6M$ |
| Exact rank and complete radical of $\mathsf H_\kappa$ | **New proved result** |
| Saturated radical lift and explicit original monomial complement | **New proved result** |
| Paid complete-core orthogonal lift through the new quotient | **New proved result** |
| Exact endpoint-annihilator rank when endpoint is nonzero on the radical | **Proved** |
| Fully actual producer preserves/fills the radical | Open |
| Actual returned endpoint on the complete radical | Open |
| Paid directional solution of the fully actual $B^\sharp$ | Conditional interface proved; hypotheses open |
| Growing relative-cofactor saving | Open |
| Same-index all-prime primitive whole-error decay and nonvanishing | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

### Final conclusion

The new A4 complete-core digit and its return calculations survive audit. The complementary finite arithmetic obligation is now advanced from a lower bound to an exact result:


$$
\boxed{
\operatorname{nullity}\mathsf H_\kappa
=
\min\left\{
P-R-1,\ 3R-\frac{5P-3}{2}
\right\}.
}
$$


The displayed Frobenius radical is complete, its integer lifts are saturated, and an explicit original-coordinate complement has a paid unit inverse. This supplies a genuine core quotient and orthogonal lift without a dense original computation or an unverified general syzygy theorem.

The exact remaining local bottleneck is the complete returned producer and endpoint on this radical, followed by the radical Smith/directional digits identified in Section 7. The exact remaining global bottleneck is still the nonzero whole determinant and its comparison with the actual contents, least simultaneous clearer, all-prime gcd, and actual primitive denominator at the same infinite original indices.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ is obtained.}}
$$


