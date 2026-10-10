> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The next core digit, its rank-$b$ return, and a new finite-radical obstruction

## Abstract

The rationality or irrationality of $e+\pi$ remains unresolved.

This report evaluates the next **complete-core** contraction that was left open in A4 Turn 4. Put


$$
r_b=\frac b2,\qquad P=\frac Q{27}=3^{h-32},\qquad
\kappa=\frac{3P-3}{2}=\frac{Q/9-3}{2}.
$$


On the unchanged sufficiently large original indices, define the finite matrix


$$
(\mathsf H_\kappa)_{ac}
=[y^{\kappa-a-c}](1-y)^b,
\qquad 0\le a,c\le r_b.
$$


Its entries are evaluated explicitly below by ternary digits; this notation is not left as an unevaluated coefficient sum.

The new complete-core conclusions are


$$
\boxed{
\frac{G_c(\mathcal F_a,\mathcal F_c)}{3^{30}}
\equiv(\mathsf H_\kappa)_{ac}\pmod3,
}
\tag{A}
$$


and


$$
\boxed{Z^T\mathsf A Z\equiv0\pmod3.}
\tag{B}
$$


Consequently, the requested right-hand side of Turn 4’s equation (10.3) is


$$
\boxed{
-\frac{G_c(\mathcal F,\mathcal F)}{3^{30}}
-Z^T\mathsf A Z
\equiv-\mathsf H_\kappa\pmod3.
}
\tag{C}
$$



This digit is **not zero**. For example,


$$
(\mathsf H_\kappa)_{r_b,\kappa-r_b}=1.
$$


Thus the whole complete-core pairing does not acquire another uniform ternary digit on these prescribed amplitudes.

Conditional on the Turn 4 terminal evaluation $\gamma_c=0$, pending its stated independent review, the subsequent **core** rank-$b$ coupling satisfies


$$
\boxed{\overline{M}_{b,c}=0,}
\tag{D}
$$


so its matrix return is actually in $3^6M$, rather than merely $81M$. Therefore, after the first $J$-return and the core rank-$b$ elimination,


$$
\boxed{\frac{T_{c,\mathrm{red}}}{81}\equiv-\mathsf H_\kappa\pmod3.}
\tag{E}
$$



There is a further obstruction. The matrix $\mathsf H_\kappa$ has an explicitly constructed radical of dimension at least


$$
\delta=
\min\!\left\{
P-r_b-1,\;
3r_b-\frac{5P-3}{2}
\right\},
\tag{F}
$$


which grows with the original indices. Its intersection with **any** endpoint-annihilator hyperplane has dimension at least $\delta-1$. Thus, even if the outstanding producer digits vanished, the new core digit would not provide a nonsingular endpoint-annihilator block.

The actual producer, endpoint, and diagonal contributions are retained below. They have not been evaluated at the precision needed to turn (E) into an evaluation of the fully returned $B^\sharp$. In particular, no actual solution


$$
B^\sharp v=w,\qquad v\in3^{-1}\mathbb Z_3^{\,b/2},
$$


is claimed.

---

## 1. Original objects and proof status

### 1.1 The original index domain is unchanged

All uniform assertions concern sufficiently large indices satisfying exactly


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


and the same fixed subwindow


$$
\frac{103}{1000}<\rho=\frac{N_0}{P_0}<\frac{104}{1000}.
$$



The original arithmetic relation is retained:


$$
P_0=243P=3^{h-27},\qquad N_0=243r,\qquad D=P_0+N_0,
$$




$$
P=3^{h-32},\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$




$$
\boxed{4^j=243(3^{26}-1)P-243r+1.}
$$



Put


$$
x=y-1,\qquad Q=3^{h-29}=27P,\qquad b=Q-N_0.
$$


Then


$$
D=10Q-b,\qquad .064<\frac bQ<.073,
$$


and $D,b$ are even.

No independent choice of $P,r$ is substituted for an original index. The supplied density theorem is used only to retain infinitely many original indices in this fixed subwindow.

### 1.2 Finite coordinates and the physical boundary

The finite coordinates remain


$$
U_s=x^s\quad(0\le s<D),
$$




$$
z_i=x^Dy^i\quad(0\le i<\nu),
\qquad
\nu=\frac D2-1,
$$




$$
Y_t=y^t\quad(d\le t\le m),
\qquad d=D+\nu,
$$


and


$$
W=[U\ Y].
$$



The physical HIGH terminal is $Y_m$. It is not the last middle direction $z_{\nu-1}$.

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
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A.
$$



The pole functional is always physically truncated:


$$
\Lambda_h(P)=
3^h\sum_{v=0}^{K_{\rm phys}}\frac{[y^v]P}{2v+1},
\qquad
K_{\rm phys}=2n-2=2H-2D+2,
$$




$$
\mathcal P(f,g)=\Lambda_h\!\left(x^A(\beta+3y)fg\right).
$$


Its largest denominator is exactly


$$
\boxed{2K_{\rm phys}+1=4n-3=4H-4D+5<3^{h+1}.}
\tag{1.1}
$$


Thus $\Lambda_h$ is integral on integral coefficient polynomials, with this cutoff.

Write


$$
E_c=G_c(W,W),\qquad
F_i=z_i-WE_c^{-1}G_c(W,z_i).
$$


These are the actual complete-core corrected columns.

The prescribed one-lift polynomials and their complete corrections are


$$
\Psi_a=x^{D+b}y^{k_0+a}(y^{3Q}+3),
\qquad
k_0=\frac{3Q+1}{2},
\qquad 0\le a\le r_b=\frac b2,
$$




$$
\mathcal F_a=\text{the actual complete-core correction of }\Psi_a.
$$



### 1.3 Reused inputs and the conditional terminal input

The following are reused at their stated, original-object scope:

- the paid pole/complete-core comparison;
- the one-digit bound for the actual LOW/HIGH inverse;
- the mixed-projection filter for $16\le p\le25$;
- the integral unit-prefix inverse and the paid first prefix lift;
- H2, including its rank-$b$ block and radical;
- the complete first producer-return comparisons;
- the exact first $J$- and rank-$b$-return formulas.

The older unquantified support-layer extension is not needed.

The Turn 4 terminal input is


$$
[y^m]\mathcal F_a
\equiv-3^{27}\delta_{a,r_b}\pmod{3^{28}},
\qquad
\gamma_c=0.
\tag{T4}
$$


Its finite-$W$ dual, physical truncation, collision, and overflow arguments are not repeated. The coordinator has checked them locally, and independent review is pending. Every conclusion below using (T4) is identified as conditional on that input.

The new evaluations (A)–(C) do **not** use (T4).

---

## 2. A paid extension of the corrected-pairing formula through $3^{31}$

The earlier compression theorem was stated through $3^{30}$. One additional digit is needed here. It can be obtained without a $p=26$ or higher filter.

### Lemma 2.1 — Complete corrected-pairing compression modulo $3^{31}$

Let $p_1,p_2\in\mathbb Z_3[y]$ have degrees at most $\nu-2$, and let $F[p_i]$ be the actual complete-core correction of $x^Dp_i$. Put


$$
B(y)=x^D(\beta+3y)p_1(y)p_2(y).
$$


Then


$$
\boxed{
G_c(F[p_1],F[p_2])
\equiv K_N\mathcal J_h(B)\pmod{3^{31}},
}
\tag{2.1}
$$


where


$$
\mathcal J_h(B)=3^h\sum_{s=0}^{\deg B}\frac{B_s}{2s+1},
$$




$$
N=3^{16},
\qquad
K_N=
-\frac{4^{2N-1}}
{\displaystyle
\binom{N-1}{(N-1)/2}
\binom{3N-1}{(3N-1)/2}},
\qquad
K_N\equiv1\pmod3.
\tag{2.2}
$$



#### Proof

Use the already proved filter with


$$
p=17,\qquad L=3^{h-17},\qquad Y=y^L.
$$


Its trial columns are


$$
\widetilde F[p_i]=x^Dp_iR_N(y^L).
$$



The established actual-$W$ residual is in $3^{17}M$. The inverse loses one digit, so the correction displacement is in $3^{16}W$. More precisely, if $r_i$ is the residual,


$$
r_i^TE_{\mathcal P}^{-1}r_j\in3^{33}\mathbb Z_3.
\tag{2.3}
$$


This is the stationary error payment $17+16=33$, not an unpaid substitution into a mixed pairing.

The existing degree check gives


$$
m-\deg\widetilde F[p_i]\ge\frac{L-4D+7}{2}>0.
$$


Every trial is therefore an original finite polynomial below $Y_m$, and its nonconstant filter terms remain in the actual HIGH span. No overflow is introduced.

It remains to check the extra digit in the scalar compression. We have


$$
\deg B\le2D-5,
\qquad
v_3(2s+1)\le h-26.
\tag{2.4}
$$


The exact formal identity is


$$
(1-y)^H
=(1-y^L)^N
\exp\!\left(
-H\sum_{\substack{k\ge1\\L\nmid k}}\frac{y^k}{k}
\right).
$$


Every coefficient in the exponent has valuation at least $17$. The quadratic exponential error is therefore in $3^{34}$.

Set


$$
A_0(Y)=(Y-1)^NR_N(Y)^2=\sum_q a_qY^q.
$$


Then


$$
\deg A_0=2N-1,\qquad A_0(1)=0.
$$



For $c=2s+1$, the uncorrected macro denominators satisfy


$$
v_3\!\left[
3^h\left(\frac1{c+2qL}-\frac1c\right)
\right]
\ge h+(h-17)-2(h-26)=35.
$$


Their contribution is thus zero modulo $3^{31}$, using $A_0(1)=0$.

For a logarithmic term put


$$
k=v-qL-s,\qquad d_v=2v+1.
$$


Its scalar valuation is


$$
2h-1-v_3(k)-v_3(d_v).
$$



If $v_3(k)<v_3(c)$, this is at least $53$. If $v_3(k)>v_3(c)$, it is at least $43$. Thus only


$$
v_3(k)=v_3(c)
$$


can matter. A contribution below $3^{31}$ then requires


$$
v_3(d_v)\ge h-5.
\tag{2.5}
$$


Such a denominator is a multiple of $L$.

For these terms,


$$
\frac1k\equiv-\frac2c
$$


at the needed precision. Indeed,


$$
\frac1k+\frac2c=\frac{d_v-2qL}{kc},
$$


and, after multiplication by $3^hH/d_v$, the error has valuation at least


$$
3h-18-v_3(d_v)-2v_3(c)\ge34.
$$



Write


$$
d_v=(2q_0+1)L.
$$


Because $\deg B<(L-1)/2$, the condition $k>0$ is exactly $q\le q_0$. Hence the actual finite partial sum is


$$
\sum_{q\le q_0}a_q
=
-[Y^{q_0}](1-Y)^{N-1}R_N(Y)^2.
\tag{2.6}
$$



The physical macro position $q_0=2N-1$, if present, gives the complete sum $A_0(1)=0$. All nonzero completed terms therefore have


$$
q_0\le2N-2,
$$


and their largest denominator is


$$
(4N-3)L=4H-3L<4H-4D+5.
\tag{2.7}
$$


This is an explicit physical-cutoff check.

Adding the inactive macro denominators changes the result only by $3^{31}$: if $v_3(d_v)\le h-6$, then


$$
2h-1-v_3(c)-v_3(d_v)\ge31.
$$


The resulting scalar is exactly the already established $K_N$. Its Jacobi norm identity is reused, not reproved.

Finally, Lucas’ theorem gives


$$
\binom{N-1}{(N-1)/2}\equiv2^{16}=1,
\qquad
\binom{3N-1}{(3N-1)/2}\equiv2^{17}=2
\pmod3,
$$


so $K_N\equiv1\pmod3$.

The complete-core transfer error is in $3^hM$, beyond the modulus used here. This proves (2.1). ∎

**Scope.** This is a paid fixed-precision extension using $p=17$. It is not an extension of the old disjoint-support argument to $p\ge26$.

---

## 3. Evaluation of the next complete-core pairing

The needed arithmetic reduces to a single nonzero coefficient of $(y-1)^{10Q}$, not to a large unevaluated sum.

Put


$$
X(y)=(y-1)^{10Q},\qquad X_k=[y^k]X(y),
$$


and retain


$$
\kappa=\frac{Q/9-3}{2}.
$$



For sufficiently large original indices,


$$
2b+4<\frac Q6.
\tag{3.1}
$$


This follows uniformly from $2b/Q<.146<1/6$.

### Lemma 3.1 — An evaluated next-digit delta

For every integer $0\le w\le2b$,


$$
\boxed{
\mathcal J_h\!\left(
x^{10Q}(\beta+3y)y^{9Q+1+w}
\right)
\equiv3^{30}\delta_{w,\kappa}\pmod{3^{31}},
}
\tag{3.2}
$$


while


$$
\boxed{
3\mathcal J_h\!\left(
x^{10Q}(\beta+3y)y^{6Q+1+w}
\right)\in3^{31}\mathbb Z_3,
}
\tag{3.3}
$$


and


$$
\boxed{
9\mathcal J_h\!\left(
x^{10Q}(\beta+3y)y^{3Q+1+w}
\right)\in3^{31}\mathbb Z_3.
}
\tag{3.4}
$$



#### Proof

Let


$$
L_0=\frac Q3.
$$


All relevant polynomial degrees are below $2D$. Consequently, every pole that can survive modulo $3^{31}$ has the form


$$
2s+1=dL_0,
\qquad
d\in\{1,3,\ldots,119\},
$$


and its weight is


$$
\frac{3^{30}}d.
\tag{3.5}
$$



After the $y$-shift, an extraction index in $X$ has the form


$$
k=uL_0+\frac{L_0-3}{2}-w-\epsilon,
\qquad \epsilon\in\{0,1\}.
$$


By (3.1), its residue between consecutive multiples of $L_0$ is strictly positive and strictly below $L_0$. Thus every interior extraction is a nonmultiple of $Q/3$.

Write $Q=3^q$. For $k=uQ+r$, $0<r<Q$, reuse the established exact valuation


$$
v_3\binom{10Q}{k}
=q-v_3(r)+v_3\binom9u.
\tag{3.6}
$$


Since $Q/3\nmid k$, the first term $q-v_3(r)$ is at least $2$.

The complete surviving-layer check is as follows.

| $v_3(d)$ in (3.5) | Pole weight | Possible contribution below $3^{31}$ |
|---:|---:|---|
| $0$ | $3^{30}$ times a unit | None: every interior coefficient has valuation at least $2$ |
| $1$ | $3^{29}$ times a unit | None: every interior coefficient has valuation at least $2$ |
| $2$ | $3^{28}$ times a unit | Valid bands have $u=1,4,7$, hence coefficient valuation at least $4$ |
| $3$ | $3^{27}$ times a unit | The physical denominator is $9Q$; only the $9$-weighted low term can be in range, and its coefficient has valuation at least $4$ |
| $4$ | $3^{26}$ | The physical denominator is $27Q$; only the high term without its extra $3y$ factor can contribute |

For clarity, the $v_3(d)=2$ denominators are


$$
3Q,\ 15Q,\ 21Q,\ 33Q,\ 39Q.
$$


The high term has valid interior bands only at $21Q,33Q$, with integer parts $Q,7Q$. The middle term has integer parts $Q,4Q$, and the low term has integer parts $4Q,7Q$. All other extractions are below support or above degree. Thus the table retains every component and both terms of $\beta+3y$.

At the only remaining pole, $27Q$, the high extraction is


$$
k=\frac{9Q-3}{2}-w.
$$


It lies strictly between $4Q+Q/3$ and $4Q+2Q/3$. Its coefficient can have valuation exactly $4$ only when


$$
k=4Q+\frac{4Q}{9}=\frac{40Q}{9}.
$$


Equivalently,


$$
w=\kappa.
\tag{3.7}
$$


Every other coefficient in this band has valuation at least $5$.

It remains to evaluate the unit


$$
\frac{X_{40Q/9}}{3^4}\pmod3.
$$


The extraction index $40Q/9$ is even, so there is no negative coefficient sign. Stripping common powers of $3$ reduces the normalized unit to that of


$$
\binom{90}{40}.
$$


Legendre’s formula gives


$$
v_3(90!)=44,\qquad v_3(40!)=18,\qquad v_3(50!)=22,
$$


hence


$$
v_3\binom{90}{40}=4.
$$



For the unit calculation, if $n=\sum n_i3^i$, then


$$
\frac{n!}{3^{v_3(n!)}}
\equiv
(-1)^{v_3(n!)}\prod_i n_i!\pmod3.
$$


The ternary expansions are


$$
90=(10100)_3,\qquad
40=(1111)_3,\qquad
50=(1212)_3.
$$


All three factorial units are $1\pmod3$. Therefore


$$
\boxed{\frac{X_{40Q/9}}{3^4}\equiv1\pmod3.}
\tag{3.8}
$$


Also $\beta\equiv1\pmod3$. Equations (3.5)–(3.8) prove (3.2)–(3.4). ∎

### Theorem 3.2 — The next whole complete-core pairing

For all $0\le a,c\le r_b$,


$$
\boxed{
\frac{G_c(\mathcal F_a,\mathcal F_c)}{3^{30}}
\equiv
[y^{\kappa-a-c}](1-y)^b
\pmod3.
}
\tag{3.9}
$$



#### Proof

The polynomial in Lemma 2.1 is


$$
B_{ac}
=
x^{10Q+b}(\beta+3y)
y^{3Q+1+a+c}(y^{3Q}+3)^2.
$$


Write $t=a+c$. Expanding only the actual finite factor $x^b$, the high, middle, and low terms are finite sums of the expressions in Lemma 3.1 with


$$
w=t+i,\qquad 0\le i\le b.
$$


Thus $0\le w\le2b$.

The middle term has coefficient $6$, and the low term coefficient $9$. Equations (3.3)–(3.4) remove them modulo $3^{31}$. The high term contributes only at $t+i=\kappa$. Hence


$$
\mathcal J_h(B_{ac})
\equiv
3^{30}[y^{\kappa-t}]x^b
\pmod{3^{31}}.
$$


Since $b$ is even, $x^b=(1-y)^b$. Lemma 2.1 and $K_N\equiv1\pmod3$ complete the proof. ∎

### 3.1 Explicit evaluation of every matrix entry

Let


$$
s=\kappa-a-c.
$$


If $s<0$ or $s>b$, then $(\mathsf H_\kappa)_{ac}=0$.

Otherwise write


$$
b=\sum_i b_i3^i,\qquad s=\sum_i s_i3^i,
\qquad b_i,s_i\in\{0,1,2\}.
$$


Then


$$
\boxed{
(\mathsf H_\kappa)_{ac}
=
(-1)^s\prod_i\binom{b_i}{s_i}
\quad\text{in }\mathbb F_3.
}
\tag{3.10}
$$


In particular:

- the entry is zero if any $s_i>b_i$;
- otherwise it is
  

$$
(-1)^s2^{\,\#\{i:b_i=2,\ s_i=1\}}\pmod3.
$$



This is a direct ternary-digit evaluation on the original integer $b$.

Moreover, the fixed window gives


$$
r_b<\kappa<b
$$


for sufficiently large original indices. Thus


$$
a=r_b,\qquad c=\kappa-r_b
$$


are actual allowed amplitudes, and


$$
\boxed{
(\mathsf H_\kappa)_{r_b,\kappa-r_b}=1.
}
\tag{3.11}
$$


The new whole pairing has valuation exactly $30$ at this entry.

---

## 4. Evaluation of the second-prefix contraction

The second prefix cannot be omitted. It can, however, be evaluated at this digit.

Let


$$
a_0=R_*-1=\frac{9Q-1}{2},
\qquad R_*=\frac{9Q+1}{2}.
$$


Partition the normalized complete-core Schur matrix


$$
\mathsf U=-\frac{S_c}{3^{26}}
$$


into the original finite prefix $0,\ldots,a_0$ and its original tail:


$$
\mathsf U=
\begin{pmatrix}
\mathsf A&\mathsf B\\
\mathsf B^T&\mathsf U_{TT}
\end{pmatrix}.
$$



The columns of $P_G$ are the prefix polynomials


$$
x^by^{k_0+a}.
$$


Their degrees are below $R_*$, so they belong to this actual prefix.

Fix the sign convention


$$
X=-\mathsf A^{-1}\mathsf B_KG
=3P_G+9Z.
\tag{4.1}
$$


This is the paid first-prefix lift. It gives exactly the retained stationary identity


$$
-\frac{G_c(\mathcal F,\mathcal F)}{3^{26}}
=
G^T\mathcal R_{c,KK}G+81Z^T\mathsf A Z.
\tag{4.2}
$$



### 4.1 The actual finite prefix inverse

The leading prefix matrix is


$$
\boxed{
\overline{\mathsf A}_{pq}
=[y^{a_0-p-q}](1-y)^{N_0},
\qquad 0\le p,q\le a_0.
}
\tag{4.3}
$$


This follows from the corrected-pairing formula at the $27Q$ pole. In this prefix range, the low band of


$$
x^D\equiv(y^{9Q}-1)x^{N_0}\pmod3
$$


is absent from the extraction, and the sign from $\mathsf U=-S_c/3^{26}$ changes $x^{N_0}$ to $(1-y)^{N_0}$, since $N_0$ is odd.

The inverse is the finite anti-triangular convolution


$$
\boxed{
(\overline{\mathsf A}^{-1})_{pq}
=[y^{p+q-a_0}](1-y)^{-N_0}.
}
\tag{4.4}
$$


All negative coefficient indices are zero. The finite bounds make the usual convolution exact; no infinite prefix is used.

Define the integral prefix residual matrix


$$
d_{pa}=\frac{G_c(F_p,\mathcal F_a)}{3^{28}}.
$$


Equation (4.1) gives


$$
\boxed{\mathsf A Z=d.}
\tag{4.5}
$$


Thus the displayed division by $3^{28}$ is paid by the already established $9Z$ lift.

### 4.2 A support statement at precisely the required digit

Put $L_0=Q/3$. Then


$$
\boxed{
\overline d_{pa}=0
\quad\text{unless}\quad
p+a+1\in L_0\mathbb Z
\ \text{or}\
p+a+2\in L_0\mathbb Z.
}
\tag{4.6}
$$



To verify this in the actual corrected pairing, its compressed polynomial is


$$
x^{10Q}(\beta+3y)y^{p+k_0+a}(y^{3Q}+3).
$$


Modulo $3^{29}$, the only relevant denominators are the $dQ$ layers with $3\mid d$.

Outside the two congruence classes in (4.6), all extraction indices are nonmultiples of $Q/3$.

- At the $27Q$ pole, the high extraction lies strictly between $4Q$ and $9Q$. Its binomial valuation is at least $3$, paying $3^{26}$ through $3^{29}$.
- The low extraction at that pole has its explicit factor $3$, and its coefficient valuation is at least $2$, again paying $3^{29}$.
- The high extraction at $9Q$ is negative.
- The remaining layers have weights at least $3^{28}$, and their nonmultiple coefficients have at least two further digits.

This proves (4.6), including the one-step shift from $3y$.

### Theorem 4.1 — The second-prefix quadratic term vanishes modulo $3$



$$
\boxed{Z^T\mathsf A Z\equiv0\pmod3.}
\tag{4.7}
$$



#### Proof

By (4.4)–(4.5),


$$
\overline{Z^T\mathsf A Z}
=\overline d^{\,T}\overline{\mathsf A}^{-1}\overline d.
$$



A potentially nonzero summand has


$$
p+a+\sigma=uL_0,\qquad
q+c+\tau=vL_0,
\qquad \sigma,\tau\in\{1,2\}.
$$


Since


$$
a_0=13L_0+\frac{L_0-1}{2},
$$


the inverse coefficient index


$$
n=p+q-a_0
$$


has residue modulo $L_0$


$$
\frac{L_0+1}{2}-(a+c)-(\sigma+\tau).
\tag{4.8}
$$


By $0\le a+c\le b$ and (3.1), this residue lies strictly between $b$ and $L_0$.

On the other hand,


$$
(1-y)^{-N_0}
=(1-y)^{b-Q}
\equiv\frac{(1-y)^b}{1-y^Q}\pmod3.
\tag{4.9}
$$


Every nonzero coefficient on the right has residue modulo $L_0$ in $[0,b]$, because $Q=3L_0$ and $b<L_0$.

Thus the coefficient in (4.4) is zero for every potentially contributing pair. Negative indices are already zero. The whole finite contraction vanishes. ∎

Combining Theorems 3.2 and 4.1 yields the requested evaluation


$$
\boxed{
-\frac{G_c(\mathcal F,\mathcal F)}{3^{30}}
-Z^T\mathsf A Z
\equiv-\mathsf H_\kappa\pmod3.
}
\tag{4.10}
$$



This is an evaluated matrix with the explicit entry rule (3.10), including the nonzero original entry (3.11).

---

## 5. The first $J$-return and the subsequent core rank-$b$ return

This section uses (T4), and is therefore conditional on the pending independent review of that input.

The exact first return remains


$$
\mathcal S_c^{(2)}
=\mathcal R_{c,KK}-27L_cB_c^{-1}L_c^T.
\tag{5.1}
$$


The inverse cost is $3^{-1}$.

Under (T4),


$$
G^T\overline L_c=0.
$$


Hence


$$
27G^TL_cB_c^{-1}L_c^TG\in3^5M.
\tag{5.2}
$$


Equation (4.10) therefore gives


$$
\boxed{
\frac{G^T\mathcal S_c^{(2)}G}{81}
\equiv-\mathsf H_\kappa\pmod3.
}
\tag{5.3}
$$



### 5.1 Use of the actual rank-$b$ quotient

Let $E_b$ consist of the first $b$ coordinate columns in the original $K$-window. The columns of $G$ are $x^by^a$, $0\le a\le r_b$. Since these polynomials are monic in their highest degrees,


$$
[E_b\ G]
$$


is integral unimodular on the original $K$-space.

H2 identifies the radical of the leading $9$-normalized form with $\overline G$. Therefore this finite complement is a valid rank-$b$ block. Write


$$
A_{b,c}=\frac{E_b^T\mathcal S_c^{(2)}E_b}{9},
\qquad
M_{b,c}=\frac{E_b^T\mathcal S_c^{(2)}G}{27}.
\tag{5.4}
$$


The established rank-$b$ inverse payment is


$$
(9A_{b,c})^{-1}=3^{-2}A_{b,c}^{-1},
\qquad A_{b,c}^{-1}\in M_b(\mathbb Z_3).
$$



### Theorem 5.1 — The core rank-$b$ coupling has one additional digit

Conditional on (T4),


$$
\boxed{M_{b,c}\in3M.}
\tag{5.5}
$$



#### Proof

First examine the cross pairing between a complementary tail column and a prescribed radical column. For $0\le u<b$,


$$
G_c(F_{R_*+u},\mathcal F_a)
$$


compresses to


$$
x^{10Q}(\beta+3y)y^{6Q+1+u+a}(y^{3Q}+3).
$$


Here $0\le u+a<3b/2\le2b$. Lemma 3.1 gives, in fact,


$$
\boxed{
\frac{G_c(F_{R_*+u},\mathcal F_a)}{3^{30}}
\equiv\delta_{u+a,\kappa}\pmod3.
}
\tag{5.6}
$$


In particular, the whole cross pairing is in $3^{30}$.

Let $\mathsf B_E$ be the prefix-to-$E_b$ block. The exact first-prefix identity gives


$$
\frac{E_b^T\mathcal R_{c,KK}G}{27}
=
-\frac{G_c(F_{R_*+\cdot},\mathcal F)}{3^{29}}
+\left(\frac{\mathsf B_E}{3}\right)^TZ.
\tag{5.7}
$$


The first term is zero modulo $3$.

The leading divided cross block is


$$
\left(\overline{\mathsf B_E/3}\right)_{p,u}
=[y^{3Q-1-p-u}]x^{N_0}.
\tag{5.8}
$$


This is the same finite prefix selector at its stated precision. In this particular range it also follows directly from


$$
x^{9Q}\equiv y^{9Q}-3y^{6Q}+3y^{3Q}-1\pmod9:
$$


only the band starting at $6Q$ survives.

Combining (5.8) with the finite inverse (4.4) gives


$$
\boxed{
\left(\overline{\mathsf B_E/3}^{\,T}
\overline{\mathsf A}^{-1}\right)_{u,p}
=-\delta_{p,k_0+u}.
}
\tag{5.9}
$$


Indeed, the finite convolution multiplies $x^{N_0}$ by $(1-y)^{-N_0}$, giving $-1$, since $N_0$ is odd. Nonnegative coefficient indices keep every contributing summand within the original prefix.

Using $\mathsf A Z=d$,


$$
\left(\overline{\mathsf B_E/3}^{\,T}\overline Z\right)_{u,a}
=-\overline d_{k_0+u,a}.
$$


But


$$
k_0+u+a+\sigma
=
4L_0+\frac{L_0+1}{2}+u+a+\sigma,
\qquad \sigma\in\{1,2\}.
$$


By the fixed-window bounds, its residue lies strictly between $0$ and $L_0$. Neither congruence in (4.6) holds. Thus


$$
\overline d_{k_0+u,a}=0.
$$


Equation (5.7) is therefore zero modulo $3$.

Finally, the $J$-return in this cross block is


$$
27E_b^TL_cB_c^{-1}L_c^TG.
$$


Under (T4), its right contracted coupling is divisible by $3$. The return is in $81M$, so after division by $27$ it is zero modulo $3$. This proves (5.5). ∎

### 5.2 The returned matrix and the paid displacement

The exact rank-$b$ matrix return is retained:


$$
T_{c,\mathrm{red}}
=
G^T\mathcal S_c^{(2)}G
-81M_{b,c}^TA_{b,c}^{-1}M_{b,c}.
\tag{5.10}
$$


Theorem 5.1 gives


$$
\boxed{
81M_{b,c}^TA_{b,c}^{-1}M_{b,c}\in3^6M.
}
\tag{5.11}
$$


The actual core displacement through this block is


$$
3A_{b,c}^{-1}M_{b,c}\in9M.
\tag{5.12}
$$



Thus, conditional on (T4),


$$
\boxed{
\frac{T_{c,\mathrm{red}}}{81}
\equiv-\mathsf H_\kappa\pmod3.
}
\tag{5.13}
$$



The endpoint and diagonal returns are not deleted:


$$
f_{c,\mathrm{new}}
=f_{c,R}-3M_{b,c}^TA_{b,c}^{-1}f_{c,b},
$$




$$
\lambda_{c,\mathrm{new}}
=\lambda_c^{(2)}
-\frac19f_{c,b}^TA_{b,c}^{-1}f_{c,b}.
\tag{5.14}
$$


The extra matrix-coupling digit does not evaluate the $1/9$ diagonal return.

---

## 6. A new obstruction: the evaluated digit has a large finite radical

The nonzero matrix $\mathsf H_\kappa$ is nevertheless highly singular.

### Theorem 6.1 — Explicit radical in the original amplitude window

Put


$$
L_*=\frac{P-1}{2},
\qquad
U_*=
\min\!\left\{
\kappa-r_b-1,\;
3r_b-2P
\right\}.
$$


For each integer $L_*\le s\le U_*$, define the amplitude polynomial


$$
g_s(y)=(1-y)^{2P-b}y^s.
\tag{6.1}
$$


Its degree is at most $r_b$, and its coefficient vector belongs to the radical of $\mathsf H_\kappa$ over $\mathbb F_3$.

These vectors are linearly independent. Consequently,


$$
\boxed{
\dim\ker\mathsf H_\kappa\ge
\delta=
\min\!\left\{
P-r_b-1,\;
3r_b-\frac{5P-3}{2}
\right\}.
}
\tag{6.2}
$$



#### Proof

The degree bound follows from


$$
2P-b+s\le r_b
\iff s\le3r_b-2P.
$$



For a row $0\le u\le r_b$,


$$
(\mathsf H_\kappa g_s)_u
=
[y^{\kappa-u}](1-y)^bg_s(y).
$$


Since $P$ is a power of $3$,


$$
(1-y)^bg_s(y)
=y^s(1-y)^{2P}
\equiv y^s(1+y^P+y^{2P})\pmod3.
\tag{6.3}
$$



The coefficient interval observed by the rows is exactly


$$
[\kappa-r_b,\kappa].
$$


The bound $s\le\kappa-r_b-1$ places the first exponent $s$ below that interval. The lower bound $s\ge(P-1)/2$ gives


$$
s+P\ge\frac{3P-1}{2}=\kappa+1,
$$


so the other two exponents are above the interval. Every row is zero.

The polynomials are a common nonzero factor times distinct monomials, hence are linearly independent. Counting the allowed integers $s$ gives (6.2). ∎

The original window gives


$$
.864<\frac{r_b}{P}<.9855.
$$


In particular,


$$
\delta>\frac{29}{2000}P-1
$$


for sufficiently large original indices.

This is growing **nullity**, not growing ternary saving.

### 6.1 Endpoint adaptation does not cure this core degeneracy

For the original evaluation endpoint,


$$
g_s(-1)=(-1)^s(2)^{2P-b}=(-1)^s\ne0
\quad\text{in }\mathbb F_3.
$$


Thus the adjacent combinations


$$
g_s+g_{s+1}=(1+y)(1-y)^{2P-b}y^s
$$


give at least $\delta-1$ independent endpoint-annihilating radical vectors.

More generally, let $f$ be **any** endpoint functional on the amplitude space. Then


$$
\dim(\ker\mathsf H_\kappa\cap\ker f)\ge\delta-1.
\tag{6.4}
$$


This statement does not assume that the actual returned endpoint is still the unmodified evaluation at $-1$.

Therefore:

> If the outstanding actual producer and rank-$b$ corrections vanish at this digit, the leading endpoint-annihilator block is singular after every integral unimodular endpoint adaptation.

The new digit cannot support a proof based on its nonsingularity modulo $3$. This does **not** disprove the directional equation $B^\sharp v=w$; a singular leading digit can still admit a suitably paid directional lift. Such a lift now requires arithmetic on an explicit, large radical.

### 6.2 The whole-core deepening route is sharply obstructed

At the original allowed entry from (3.11),


$$
v_3G_c(\mathcal F_{r_b},\mathcal F_{\kappa-r_b})=30.
$$


The second-prefix contraction does not cancel this digit. Conditional on (T4), neither the first $J$-return nor the core rank-$b$ matrix return cancels it.

Thus the assertion


$$
T_{c,\mathrm{red}}\in243M
$$


would be false. Further progress must isolate and return the radical directions; it cannot be obtained by claiming one more uniform digit for the entire core matrix.

---

## 7. What remains in the fully actual returned operator

The foregoing computations evaluate the complete core and its core rank-$b$ return. They do not identify the complete producer with the core at this new digit.

### 7.1 The complete producer forcing remains unchanged

Retain exactly


$$
Q_{\rm act}=3P_n=Q_c+3^7\mathscr R,
$$




$$
3^7\mathscr R=\sum_{a=0}^{A+1}e_ax^a,
\qquad
e_a=-\frac{(A+1)!}{a!}(t_a+\xi v_a),
$$


with


$$
t=3nh_{\rm vec}
+(b_{\rm force}+6)e_{n-1}
+\frac{2b_{\rm force}}{n-1}e_{n-2},
\qquad
b_{\rm force}=-n-66.
\tag{7.1}
$$


The signed $\xi$ and its paid normalization are retained, as are


$$
\mathscr R(-1)
=-\frac{\xi((A+1)!)^2}{3^7},
$$




$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
\tag{7.2}
$$



Neither the new moment calculation nor the terminal evaluation authorizes dropping any term of this force.

### 7.2 All three return channels are retained

For $\alpha=c,\mathrm{act}$, the first return is


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
\tag{7.3}
$$


Its inverse cost is $3^{-1}$.

The rank-$b$ return is


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
\tag{7.4}
$$


Its inverse cost is $3^{-2}$.

Theorem 5.1 concerns $M_{b,c}$. It does not establish $M_{b,\mathrm{act}}\in3M$.

### 7.3 The precise producer digits still needed

On the actual original complement, define the integral differences


$$
\Delta_{GG}
=
\frac{
G^T(\mathcal S_{\rm act}^{(2)}-\mathcal S_c^{(2)})G
}{81},
\tag{7.5}
$$




$$
\Delta_{bG}
=
\frac{
E_b^T(\mathcal S_{\rm act}^{(2)}-\mathcal S_c^{(2)})G
}{27}.
\tag{7.6}
$$


The stated earlier bounds pay these divisions. They do not evaluate their residues.

Conditional on (T4), the newly evaluated core gives the exact remaining leading-digit formula


$$
\boxed{
\frac{T_{\rm act,\mathrm{red}}}{81}
\equiv
-\mathsf H_\kappa
+\overline{\Delta}_{GG}
-\overline{\Delta}_{bG}^{\,T}
\overline A_{b,\rm act}^{-1}
\overline{\Delta}_{bG}
\pmod3.
}
\tag{7.7}
$$



Equation (7.7) is a ledger for what remains, not a claim that its producer terms have been evaluated.

The precise valuation obstruction is now clear:

- a difference known to be in $81M$ is only **integral** after division by $81$;
- a cross difference known to be in $27M$ is only **integral** after division by $27$;
- the $1/9$ diagonal return can expose digits not visible in the earlier endpoint congruences.

Thus the earlier producer comparisons do not justify setting either residue in (7.7) to zero.

### 7.4 Actual endpoint adaptation and $B^\sharp$

Let the actual returned endpoint determine its original integral unimodular adaptation. It must be formed from the complete $f_{\rm act,new}$ in (7.4), not from an unreturned core endpoint.

After that adaptation, retain


$$
T=
\begin{pmatrix}a&z^T\\z&C\end{pmatrix}\in81M,
\qquad
\lambda=\eta/3,\quad\eta\in\mathbb Z_3^\times.
$$


Write


$$
a=81\alpha,\qquad z=81w,\qquad C=81B,
\qquad
u=1-27\eta\alpha.
$$


The paid two-coordinate return remains


$$
\boxed{
B^\sharp=B+\frac{27\eta}{u}ww^T,
\qquad u\in1+27\mathbb Z_3.
}
\tag{7.8}
$$



In particular, $B^\sharp\equiv B\pmod3$. But its actual leading $B$ is obtained by adapting the **whole** matrix in (7.7), not merely $-\mathsf H_\kappa$.

Accordingly, no favorable actual direction has yet been proved to survive all returns. The core calculation gives a sharper obstruction and an explicit radical on which the outstanding producer and endpoint arithmetic must now be tested.

---

## 8. A concrete follow-on lemma

The next target is no longer the unnamed right-hand side of Turn 4’s equation (10.3). That contraction has been evaluated.

A concrete next lemma is the following.

> **Actual producer-on-radical return lemma.**  
> On the same original fixed subwindow, substitute the complete coefficients (7.1)–(7.2) into the actual corrected columns and the exact returns (7.3)–(7.4), and evaluate
> 

$$
> \overline{\Delta}_{GG},\qquad
> \overline{\Delta}_{bG},
>
$$


> at least on the explicitly given vectors
> 

$$
> (1-y)^{2P-b}y^s,\qquad L_*\le s\le U_*.
>
$$


> Simultaneously evaluate the actual returned endpoint on these vectors.
>
> This must determine whether the producer fills the radical in (6.2), preserves it, or cancels part of the nonzero matrix $\mathsf H_\kappa$.

Two particularly concrete possible outcomes are:

1. Prove the stronger actual estimates
   

$$
G^T(\mathcal S_{\rm act}^{(2)}-\mathcal S_c^{(2)})G\in3^5M,
$$


   

$$
E_b^T(\mathcal S_{\rm act}^{(2)}-\mathcal S_c^{(2)})G\in3^4M.
$$


   Then (7.7) reduces to $-\mathsf H_\kappa$, and Theorem 6.1 rigorously rules out the nonsingular-next-digit route after actual endpoint adaptation.

2. If either residue is nonzero, evaluate its action on the displayed radical and carry that action through the actual endpoint and diagonal returns. A favorable directional solve would have to be proved from those returned data.

Neither outcome is assumed here. In particular, a statement that the producer correction has “higher order” without these exact normalized estimates would be insufficient.

---

## 9. Fixed depth versus a saving growing with the original index

The new pairing digit is fixed:


$$
3^{30}\quad\text{for the whole complete-core pairing},
$$


or


$$
81\quad\text{after the original core normalization}.
$$


Its sharp nonzero entry shows that the whole core matrix does not simply keep gaining uniform digits.

The growing radical dimension in Theorem 6.1 is also not a growing primitive-denominator saving. Large common determinant factors from a radical elimination can occur in both distinguished cofactors and disappear in the final primitive quotient.

A mechanism for a genuinely growing saving would require an original-index induction through an unbounded number of further ternary layers, with all of the following proved at each layer:

1. the actual finite radical or directional subspace;
2. a paid inverse on its actual complement;
3. the complete producer, endpoint, and diagonal returns;
4. preservation of the physical LOW/HIGH boundaries;
5. a nonzero final Schur scalar with a valuation advantage growing with $j$;
6. survival of that advantage after the actual all-prime gcd and least clearer are used.

The current $p\le25$ mixed filters do not supply such an induction. Their admissible range is fixed. Any later use of $p\ge26$ must again pay collisions, truncation, and all returns; the checked Turn 4 calculation at one such scale is not an unbounded extension theorem.

The complete-source recurrence remains


$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\qquad0\le t\le2n-2.
$$


Its forward resonance at


$$
t_*=\frac{3^h-5}{2}
$$


retains its genuine $3^h$ divisor. The highest moment remains physical because


$$
H-4D+5\ge0.
$$


No local core calculation here removes that divisor.

---

## 10. Division and boundary ledger

| Operation | Exact payment or boundary |
|---|---|
| Original pole functional | Cutoff $K_{\rm phys}=2n-2$, largest denominator $4n-3$ |
| $p=17$ trial | Actual finite LOW/HIGH trial; degree strictly below $m$ |
| Mixed residual | $3^{17}$ |
| LOW/HIGH inverse | One-digit loss, giving displacement $3^{16}$ |
| Stationary pairing error | $3^{17+16}=3^{33}$ |
| Logarithmic quadratic error | $3^{34}$ |
| Bare macro-denominator approximation | Error at least $3^{35}$ |
| Completed logarithmic macro sum | Last nonzero denominator $(4N-3)L<4n-3$ |
| Physical $q_0=2N-1$ macro position | Its complete partial sum is $A_0(1)=0$ |
| Complete-core transfer | Error $3^h$, beyond $3^{31}$ |
| New small binomial division | $v_3\binom{90}{40}=4$, normalized unit $1$ |
| Whole core observation | Division by $3^{30}$, explicitly evaluated |
| Original core normalization | Division by $3^{26}$ |
| Unit prefix | Integral inverse; the $9Z$ lift is retained |
| Second-prefix return | Evaluated $Z^T\mathsf A Z\equiv0\pmod3$ |
| First $J$-inverse | $3^{-1}$; conditional contracted matrix return in $3^5M$ |
| Core rank-$b$ inverse | $3^{-2}$; new $M_{b,c}\in3M$, return in $3^6M$ |
| Actual rank-$b$ inverse | Same $3^{-2}$ cost; its producer contribution is not discarded |
| Endpoint/diagonal return | Full $3$ and $1/9$ formulas retained |
| Two-coordinate bordered return | Actual $u,\eta,w$ retained in $B^\sharp$ |
| Content division | No new content division is made |

All new amplitude polynomials are vectors inside an original finite subspace at a fixed original $j$. They are not auxiliary dense tuples or new original indices.

---

## 11. Actual contents, least clearer, all-prime gcd, and whole error

The local Jacobi coefficients, the unit $K_N$, and the finite-field amplitude calculations do not redefine the actual original column contents.

Retain the actual least simultaneous clearer $\ell_{\rm clr}$, with only the previously paid original content divisions. The distinguished integers remain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,
\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and


$$
\boxed{g_\ell=\gcd(|A_\ell|,|B_\ell|)}
$$


is the gcd over **all primes**.

For $B_\ell\ne0$, the actual primitive denominator and numerator are


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole evaluated error is still


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{11.1}
$$



An irrationality proof requires, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\boxed{
\log g_\ell-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|
\longrightarrow+\infty.
}
\tag{11.2}
$$



The new core digit and growing radical dimension establish none of these final inequalities or nonvanishing conditions.

---

## 12. Bounded exact-arithmetic receipt

No tool computation was performed. No dense original matrix computation is requested, and no closed auxiliary receipt, Jacobi/Selberg identity, or fixed-digit table is reopened.

The only optional new arithmetic receipt is small.

### Inputs

- $n=90$, $k=40$;
- modulus $243=3^5$;
- Pascal’s recurrence for rows $0,\ldots,90$, computed by integer addition modulo $243$.

This requires fewer than $4200$ stored residues and fewer than $4200$ additions.

### Expected verifiable outputs



$$
\boxed{\binom{90}{40}\equiv81\pmod{243},}
$$


and


$$
v_3(90!)=44,\qquad
v_3(40!)=18,\qquad
v_3(50!)=22.
$$


Thus


$$
\boxed{
v_3\binom{90}{40}=4,
\qquad
\frac1{81}\binom{90}{40}\equiv1\pmod3.
}
$$



These outputs verify only the displayed universal constant. The original-index theorem follows from the paid projection, full pole-layer analysis, finite prefix contraction, and return calculations above—not from extrapolating a finite auxiliary instance.

---

## 13. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Original mixed $W$-projection and $p\le25$ filters | Reused at their established scope |
| Turn 4 physical-terminal evaluation and $\gamma_c=0$ | Locally checked; independent review pending |
| Corrected-pairing compression through $3^{31}$ | **New paid proof** |
| Next low-degree moment delta, Lemma 3.1 | **Explicitly evaluated** |
| $G_c(\mathcal F,\mathcal F)/3^{30}\pmod3$ | **Evaluated as $\mathsf H_\kappa$** |
| Second-prefix contraction $Z^T\mathsf A Z\pmod3$ | **Evaluated: zero** |
| Requested next core contraction | **Evaluated as $-\mathsf H_\kappa$** |
| Core rank-$b$ coupling $M_{b,c}\pmod3$ | **Evaluated: zero, conditional on (T4)** |
| Core rank-$b$ matrix return | **Strengthened to $3^6M$, conditional on (T4)** |
| Uniform extra digit for the whole core residual | **Disproved by an original allowed nonzero entry** |
| Explicit large radical of the next core digit | **New proved finite-window theorem** |
| Nonsingular leading endpoint-annihilator route for the core digit | **Obstructed after every endpoint adaptation** |
| Actual producer residues in (7.7) | Open |
| Fully returned $B^\sharp v=w$ with $v\in3^{-1}\mathbb Z_3^{b/2}$ | Open |
| Growing relative-cofactor saving | Open |
| Same-index all-prime primitive whole-error decay | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

### Final conclusion

The previously unevaluated next core contraction is now determined:


$$
\boxed{
-\frac{G_c(\mathcal F,\mathcal F)}{3^{30}}
-Z^T\mathsf A Z
\equiv-\mathsf H_\kappa\pmod3,
\qquad
\kappa=\frac{3P-3}{2}.
}
$$



It is a nonzero matrix with explicitly evaluated ternary-digit entries. Conditional on the reviewed Turn 4 terminal input, the subsequent core rank-$b$ return does not alter this digit.

The advance also exposes a concrete obstruction: the next core digit has a large explicit radical, and that radical meets every endpoint-annihilator hyperplane. Consequently, another fixed-depth nonsingular-digit argument cannot supply the desired actual directional inverse.

The exact remaining local bottleneck is the action of the **complete returned producer** on this explicit radical, together with the actual endpoint and diagonal channels. Beyond that remains the unbounded arithmetic improvement and the same-index comparison involving the actual contents, least clearer, all-prime gcd, primitive denominator, and nonzero whole complete determinant.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ is obtained.}}
$$


