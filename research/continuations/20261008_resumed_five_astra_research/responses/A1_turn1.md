> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A uniform mixed-projection filter and the next ternary coefficient

## Abstract

The global problem remains open: no unconditional proof that $e+\pi$ is rational or irrational is obtained.

There is, however, a new evaluation of the local coefficient requested in the assignment. On the unchanged sufficiently large original family, the actual LOW/HIGH-plus-prefix coefficient satisfies


$$
\boxed{\Pi=0\quad\text{as a matrix over }\mathbb F_3.}
$$


In particular, its restriction to all the prescribed endpoint-annihilating combinations is zero.

The main new ingredient is a uniform polynomial filter. It does **not** replace the mixed space $W$ by consecutive Jacobi degrees. Instead, a normalized Jacobi polynomial in the sparse variable


$$
Y=y^{3^{h-16}}
$$


produces explicit trial corrected columns. Their residuals are checked against **every actual LOW and HIGH coordinate**, including $Y_m$, and the established one-digit inverse loss is paid. The resulting same-$W$ corrected pairing reduces, through $3^{30}$, to a scalar times a small-degree coefficient functional. That scalar is evaluated:


$$
\boxed{K\equiv13\pmod{81}.}
$$



The same construction also proves


$$
\boxed{[y^m]F_i\in3^{24}\mathbb Z_3\qquad(0\le i\le\nu-2).}
$$


It does not prove the analogous assertion for $F_{\nu-1}$. At that last middle coordinate the filter has an explicit, nonzero physical-$Y_m$ residual. Thus the physical terminal is retained rather than suppressed.

A separate derivation below supplies the corrected-column comparison needed for the full nonterminal strip. This is an alternative proof of that comparison, not a retrospective certification of the older support-layer argument. Using the already established finite prefix and $J$-inverse identities, it gives the first-return cancellation without invoking the unaudited support-layer extension.

Consequently, after the already paid rank-$b$ elimination, the actual residual matrix is in $81M$. This is a fixed additional matrix digit, **not** a growing relative-cofactor saving. The actual directional inverse, the surviving terminal and diagonal returns, and the all-prime primitive whole-error comparison remain unresolved.

---

## 1. Original domain, objects, and reused results

### 1.1 The domain is unchanged

All statements concern sufficiently large indices satisfying


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



Retain the fixed original subwindow


$$
\frac{103}{1000}<\rho:=\frac{N_0}{P_0}<\frac{104}{1000},
$$


where


$$
P_0=243P=3^{h-27},\qquad N_0=243r,\qquad D=P_0+N_0,
$$




$$
P=3^{h-32},\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$


and


$$
\boxed{4^j=243(3^{26}-1)P-243r+1.}
$$



No auxiliary $(P,r)$ is substituted for an original tuple. The accepted density result is used only at its supplied scope: there are infinitely many original indices in this fixed window.

Put


$$
x=y-1,\qquad Q=P_0/9,\qquad b=Q-N_0.
$$


Then


$$
D=10Q-b,\qquad
\frac{64}{1000}<\frac bQ<\frac{73}{1000},
$$


and $D,b$ are even.

The finite spaces remain


$$
U_s=x^s\quad(0\le s<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_t=y^t\quad(d\le t\le m),
\qquad
\nu=D/2-1,\qquad d=D+\nu.
$$


Thus


$$
W=[U\ Y].
$$


The physical HIGH terminal is $Y_m$.

The retained residual indices are


$$
R_*=\frac{P_0+1}{2},\qquad
\tau=\frac{N_0-3}{2},\qquad
\ell=\frac{3b}{2}+1,
$$




$$
K=\{0,\ldots,\ell-1\},\qquad
J=\{\ell,\ldots,\tau-1\},
$$




$$
n_J=\frac{Q-4b-5}{2},\qquad E=\frac{Q-3}{2}.
$$


Since $R_*+\tau=\nu$, the last middle direction is $z_{\nu-1}$, not $Y_m$.

### 1.2 Complete functional and actual corrected columns

The complete finite functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!.
$$


Its physical pole cutoff is


$$
2v+1\le4n-3=4H-4D+5<3^{h+1}.
$$



The complete core is


$$
G_c(f,g)=\mathcal M(Q_cfg),\qquad
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A.
$$


Write


$$
E_c=G_c(W,W),\qquad
F_i=z_i-WE_c^{-1}G_c(W,z_i).
$$


These $F_i$ are the actual complete-core corrected columns.

The paid pole form is


$$
\mathcal P(f,g)
=
3^h\sum_{v=0}^{2n-2}
\frac{[y^v]x^A(\beta+3y)fg}{2v+1}.
$$


Because $A$ is odd,


$$
\mathcal P(f,g)
=
\frac{3^h}{2}
\int_0^1
y^{-1/2}(1-y)^A(-\beta-3y)f(y)g(y)\,dy,
$$


and its weight is positive on $0<y<1$.

This positivity motivates the filter below. It is not used to infer a ternary valuation or a primitive content.

### 1.3 Reused mathematics and review status

The following are reused at their supplied original-object scope:

* integrality and unimodularity of the original corrected basis;
* $E_c^{-1},E_{\rm act}^{-1}\in3^{-1}M$;
* $S_c\in3^{26}M$;
* the paid pole/complete-core Schur congruence
  

$$
S_{\mathcal P}-S_c\in3^hM;
$$


* the finite unit-prefix inverse and first selector;
* H2 and its stated radical and endpoint consequences;
* the complete first producer-return difference;
* the paid $3^{-2}$ rank-$b$ elimination and complete diagonal valuation;
* the raw radical pairing through $3^{30}$.

The parent’s local checks of Turn 0 are not described here as completed external referee review.

The older proof of the full support-layer strip remains unaudited as a proof. Section 5 below gives a different derivation of the particular corrected-strip conclusion needed here; it does not silently invoke the older extension.

---

## 2. An explicit filter for the actual mixed projection

The useful Jacobi polynomial is not a basis replacement for $W$. It is a sparse trial multiplier whose residual can be checked in the original coordinates.

### 2.1 The normalized macro-polynomial

For an integer $p\ge2$, put


$$
N=3^{p-1},\qquad M=\frac{N-1}{2},
$$


and define


$$
R_N(Y)
=
{}_2F_1\!\left(-M,\frac{3N}{2};\frac12;Y\right).
$$


This is a polynomial of degree $M$, normalized by $R_N(0)=1$.

Its coefficient of $Y^k$, $1\le k\le M$, is


$$
r_k
=
(-1)^k\binom Mk
\frac{\prod_{a=0}^{k-1}(3N+2a)}
{\prod_{a=0}^{k-1}(2a+1)}.
$$



#### Lemma 2.1 — Every ternary normalization is paid

For $1\le k\le M$,


$$
\boxed{v_3(r_k)=p-v_3(k)\ge2.}
$$


In particular,


$$
R_N\in\mathbb Z_3[Y],\qquad R_N\equiv1\pmod9.
$$



**Proof.**
Because $2a+1<N$ for $0\le a<k\le M$,


$$
v_3(N-(2a+1))=v_3(2a+1).
$$


Using $M=(N-1)/2$, this gives


$$
v_3\binom Mk=v_3\binom{2k}{k}.
$$


Also,


$$
v_3\prod_{a=0}^{k-1}(3N+2a)
=p+v_3((k-1)!),
$$


whereas


$$
v_3\prod_{a=0}^{k-1}(2a+1)
=v_3((2k)!)-v_3(k!).
$$


Substitution yields


$$
v_3(r_k)=p-v_3(k).
$$


Since $k<N=3^{p-1}$, one has $v_3(k)\le p-2$. ∎

Thus the hypergeometric normalization introduces no unpaid ternary denominator.

The Rodrigues formula is


$$
R_N(Y)=
\frac{Y^{1/2}(1-Y)^{-N}}{(1/2)_M}
\frac{d^M}{dY^M}
\left(Y^{M-1/2}(1-Y)^{N+M}\right).
$$


Integrating by parts $M$ times proves


$$
\boxed{
\int_0^1Y^{q-1/2}(1-Y)^N R_N(Y)\,dY=0
\quad(0\le q<M).
}
\tag{2.1}
$$


All boundary terms vanish: before the last integration, the powers at $0$ and $1$ remain positive.

### 2.2 Embedding the filter at the same original indices

Now set


$$
L=3^{h-p},\qquad Y=y^L.
$$


Then $H=NL$. For $16\le p\le25$,


$$
\frac LD=\frac{3^{27-p}}{1+\rho}
\ge\frac9{1.104}>8.
$$


In particular,


$$
L>4D.
\tag{2.2}
$$



For $0\le i\le\nu-2$, define the trial column


$$
\widetilde F_i^{(p)}
=
x^Dy^iR_N(y^L).
$$



It has the same middle coordinate as $z_i$. Indeed, every nonconstant filter term has smallest monomial exponent at least $L>d$, so


$$
\widetilde F_i^{(p)}-z_i\in\operatorname{span}Y.
\tag{2.3}
$$



Its degree remains strictly below the physical terminal:


$$
\deg\widetilde F_i^{(p)}
\le D+\nu-2+\frac{H-L}{2}
=\frac{H+3D-L-6}{2},
$$


and hence


$$
m-\deg\widetilde F_i^{(p)}
\ge\frac{L-4D+7}{2}>0.
\tag{2.4}
$$



### Theorem 2.2 — Uniform residual certificate in the actual $W$

For $16\le p\le25$ and $0\le i\le\nu-2$,


$$
\boxed{
\mathcal P(W,\widetilde F_i^{(p)})
\in3^p\mathbb Z_3^{\dim W}.
}
\tag{2.5}
$$



Consequently,


$$
\boxed{
F_i-\widetilde F_i^{(p)}\in3^{p-1}W\mathbb Z_3^{\dim W}.
}
\tag{2.6}
$$



**Proof.**

First,


$$
x^H=(y-1)^H
\equiv (y^L-1)^N\pmod{3^p}.
\tag{2.7}
$$


For example, write $(y-1)^L=(y^L-1)+3B(y)$ and raise to $N=3^{p-1}$; every nonleading term is divisible by $3^p$.

Every pole that can survive modulo $3^p$ has


$$
v_3(2v+1)\ge h-p+1,
$$


so its index satisfies


$$
v\equiv\frac{L-1}{2}\pmod L.
\tag{2.8}
$$



For a LOW row $x^u$, the relevant polynomial after (2.7) is


$$
(Y-1)^N R_N(Y)\,x^u y^i(\beta+3y).
$$


Its low residue band has degree at most


$$
u+i+1\le d-2<\frac{L-1}{2}.
$$


It therefore misses every residue class in (2.8).

For a HIGH row $y^t$, consider separately the $\beta$ and $3y$ terms. A possible surviving residue has


$$
t+i+\epsilon=qL+\frac{L-1}{2},
\qquad \epsilon\in\{0,1\}.
$$


The actual bounds $d\le t\le m$, $i\le\nu-2$ imply


$$
0\le q\le M-1.
$$


Indeed,


$$
m+i+1\le m+\nu-1=\frac{H-3}{2}<\frac{H-1}{2},
$$


whereas $q=M$ would give $(H-1)/2$.

The complete contribution in that residue class is therefore a multiple of


$$
3^p\sum_k
\frac{[Y^k](Y-1)^NR_N(Y)Y^q}{2k+1},
$$


which is zero by (2.1).

No macro term lies beyond the physical cutoff. Its largest possible index is at most


$$
2H-\frac{3L+1}{2}
<2H-2D+2=2n-2,
$$


using $L>4D$.

This proves (2.5). The actual pole inverse loses at most one digit, so the exact pole-corrected column differs from the trial by $3^{p-1}W$. The already paid pole/complete-core comparison adds only $3^{h-1}W$, proving (2.6). ∎

This theorem pays the selected mixed-subspace projection. It uses neither a dense inverse nor a replacement of $W$ by consecutive Jacobi degrees.

### 2.3 Two immediate consequences

With $p=16$, stationary error gives


$$
\boxed{
G_c(F_i,F_j)
\equiv
\mathcal P(\widetilde F_i^{(16)},\widetilde F_j^{(16)})
\pmod{3^{30}}
}
\tag{2.9}
$$


for $i,j\le\nu-2$.

Indeed, the two column errors lie in $3^{15}W$, and exact orthogonality leaves only their quadratic pairing, in $3^{30}$.

With $p=25$, (2.4) and (2.6) give the new physical-terminal estimate


$$
\boxed{
[y^m]F_i\in3^{24}\mathbb Z_3
\qquad(0\le i\le\nu-2).
}
\tag{2.10}
$$


Thus, for the retained normalization


$$
t_i=\frac{[y^m]F_i}{3^{20}},
$$


one has


$$
\boxed{t_i\in3^4\mathbb Z_3\quad(i\le\nu-2).}
\tag{2.11}
$$



This is a local divisibility statement, not a content division.

### 2.4 Why the physical terminal cannot be included for free

For $i=\nu-1$, the $3y$-term at $t=m$ has


$$
m+i+1=m+\nu=\frac{H-1}{2}.
$$


It therefore produces $q=M$, outside the orthogonality range in (2.1).

More precisely, modulo $3^p$, the trial terminal column has a residual supported at the actual $Y_m$-row:


$$
\mathcal P(W,\widetilde F_{\nu-1}^{(p)})
\equiv3\mathfrak t_p\,e_{Y_m}\pmod{3^p},
\tag{2.12}
$$


where


$$
\mathfrak t_p
=
(-1)^{N+M}3^p2^{4N-1}
\frac{M!(N+M)!(2N)!}{(4N)!}.
$$


Legendre’s formula gives


$$
v_3(\mathfrak t_p)=0.
\tag{2.13}
$$


For completeness, if $q=p-1$, then


$$
v_3(M!)+v_3((N+M)!)=N-q-1,
$$




$$
v_3((2N)!)=N-1,\qquad v_3((4N)!)=2N-1,
$$


and their total with the prefactor is $p-q-1=0$.

Thus the missing physical boundary is a genuine unit-amplitude residual multiplied by $3$. Neither $t_{\nu-1}$ nor the middle-terminal coupling is set to zero by the filter.

---

## 3. The corrected pairing compresses to an evaluated scalar

For a polynomial $B$ of degree below $2D$, define the finite coefficient functional


$$
\mathcal J_h(B)
=
3^h\sum_{s=0}^{\deg B}\frac{B_s}{2s+1}.
\tag{3.1}
$$


All its denominators lie inside the original physical cutoff.

Hereafter use


$$
p=16,\qquad N=3^{15},\qquad L=3^{h-16},
\qquad M=\frac{N-1}{2}.
$$



### Theorem 3.1 — Same-$W$ compression through $3^{30}$

Let $p_1,p_2\in\mathbb Z_3[y]$ have degrees at most $\nu-2$. Let $F[p_i]$ denote the actual complete-core correction of $x^Dp_i$. Then


$$
\boxed{
G_c(F[p_1],F[p_2])
\equiv
K_N\,\mathcal J_h\!\left(x^D(\beta+3y)p_1p_2\right)
\pmod{3^{30}},
}
\tag{3.2}
$$


where


$$
\boxed{
K_N=
-\frac{4^{\,2N-1}}
{\displaystyle
\binom{N-1}{(N-1)/2}
\binom{3N-1}{(3N-1)/2}}
\equiv13\pmod{81}.
}
\tag{3.3}
$$



The remaining functional in (3.2) is evaluated on the requested combinations in Section 4.

### 3.1 Proof of the compression

Put


$$
B(y)=x^D(\beta+3y)p_1(y)p_2(y).
$$


Then


$$
\deg B\le2D-5.
$$


By Theorem 2.2, it suffices to evaluate


$$
\mathcal P\bigl(x^Dp_1R_N(y^L),x^Dp_2R_N(y^L)\bigr).
$$



In $\mathbb Z_3[[y]]$,


$$
(1-y)^H
=
(1-y^L)^N
\exp\!\left(
-H\sum_{\substack{k\ge1\\L\nmid k}}\frac{y^k}{k}
\right).
\tag{3.4}
$$


Every coefficient of the series in the exponential has valuation at least $16$. Consequently,


$$
x^H
\equiv
(Y-1)^N
\left(
1-H\sum_{\substack{k\ge1\\L\nmid k}}\frac{y^k}{k}
\right)
\pmod{3^{30}}.
\tag{3.5}
$$


The quadratic exponential error starts in $3^{32}$.

Let


$$
A_0(Y)=(Y-1)^NR_N(Y)^2=\sum_q a_qY^q.
$$


Its degree is $2N-1$, and $A_0(1)=0$.

For each coefficient index $s$ of $B$, put $c=2s+1$. Since


$$
c<4D+1<3^{h-25},
$$




$$
v_3(c)\le h-26.
\tag{3.6}
$$



#### The term without the logarithmic correction

Every relevant denominator is $c+2qL$. Since $v_3(L)=h-16$,


$$
3^h\left(\frac1{c+2qL}-\frac1c\right)\in3^{36}\mathbb Z_3.
$$


Thus its contribution modulo $3^{30}$ is


$$
\frac{3^h}{c}\sum_q a_q=0.
\tag{3.7}
$$



All these coefficients are inside the original cutoff because


$$
(2N-1)L+\deg B<2H-2D+2.
$$



#### The logarithmic correction

Consider a term with


$$
k=v-qL-s\ge1,\qquad L\nmid k,\qquad d_v=2v+1.
$$


Its valuation before multiplication by the integral coefficients is


$$
2h-1-v_3(k)-v_3(d_v).
$$



If $v_3(k)<v_3(c)$, then $v_3(d_v)=v_3(k)$, and this valuation is at least $53$.

If $v_3(k)>v_3(c)$, it is at least $42$.

Hence a contribution modulo $3^{30}$ is possible only when


$$
v_3(k)=v_3(c),\qquad v_3(d_v)\ge h-4.
\tag{3.8}
$$



For these terms,


$$
\frac1k\equiv-\frac2c
$$


at the required precision: after multiplication by $3^hH/d_v$, the error lies in $3^{35}\mathbb Z_3$.

Write the active denominator as


$$
d_v=aL,\qquad a\ \text{odd}.
$$


Then


$$
v=q_0L+\frac{L-1}{2},
\qquad q_0=\frac{a-1}{2}.
$$


Since $s<(L-1)/2$, the condition $k>0$ is exactly $q\le q_0$. Therefore


$$
\sum_{q\le q_0}a_q
=
[Y^{q_0}]\frac{A_0(Y)}{1-Y}
=
-[Y^{q_0}](1-Y)^{N-1}R_N(Y)^2.
\tag{3.9}
$$



Adding the inactive macro denominators changes nothing modulo $3^{30}$: their scalar valuation, combined with (3.6), is at least $30$. Every denominator thereby used still corresponds to a physical pole, since


$$
(4N-3)L=4H-3L<4H-4D+5.
$$



Consequently the complete scalar multiplying $3^h/c$ is


$$
K_N
=
-2N\sum_{q=0}^{2N-2}
\frac{[Y^q](1-Y)^{N-1}R_N(Y)^2}{2q+1},
$$


or


$$
K_N
=
-N\int_0^1Y^{-1/2}(1-Y)^{N-1}R_N(Y)^2\,dY.
\tag{3.10}
$$


This proves the compressed pairing once the scalar is evaluated.

### 3.2 Evaluation of the scalar

Let


$$
h_R=\int_0^1Y^{-1/2}(1-Y)^NR_N(Y)^2\,dY.
$$


Integration of the derivative of


$$
Y^{1/2}(1-Y)^NR_N(Y)^2
$$


gives


$$
N\int_0^1Y^{-1/2}(1-Y)^{N-1}R_N(Y)^2\,dY
=
\left(N+2M+\frac12\right)h_R.
\tag{3.11}
$$


Here


$$
\int YR_N'R_N\,Y^{-1/2}(1-Y)^N\,dY=Mh_R,
$$


because $YR_N'-MR_N$ has degree below $M$.

Rodrigues and $M$ integrations by parts give


$$
h_R=
\frac{\Gamma(1/2)^2M!\Gamma(N+M+1)}
{(N+2M+1/2)\Gamma(M+1/2)\Gamma(N+M+1/2)}.
$$


Substitution into (3.10)–(3.11), with $2M=N-1$, yields exactly


$$
K_N=
-\frac{4^{2N-1}}
{\binom{N-1}{M}\binom{3N-1}{N+M}}.
$$



Both binomial denominators are ternary units: their lower indices have only ternary digits $1$, so doubling causes no carries.

To evaluate modulo $81$, put


$$
B_q=\binom{3^q-1}{(3^q-1)/2}.
$$


Stripping multiples of $3$ from the factorials shows that


$$
B_q\equiv-B_{q-1}\pmod{81}\qquad(q\ge4).
\tag{3.12}
$$


Indeed, the product of all units modulo $81$ is $-1$, and the square of the product of the units in $1,\ldots,40$ is $1$.

Since


$$
B_3=\binom{26}{13}=10400600\equiv38\pmod{81},
$$




$$
B_{15}\equiv38,\qquad B_{16}\equiv43,
$$


and their product is $14\pmod{81}$. Also,


$$
4^{2N-1}\equiv4^{-1}\equiv61\pmod{81},
\qquad14^{-1}\equiv29\pmod{81}.
$$


Therefore


$$
\boxed{K_N\equiv-61\cdot29\equiv13\pmod{81}.}
$$


Theorem 3.1 follows. ∎

---

## 4. Evaluation of the requested coefficient

### 4.1 The actual one-lift polynomials remain nonterminal

Retain


$$
k_0=\frac{P_0/3+1}{2}=\frac{3Q+1}{2},
$$


and


$$
\Psi_a
=
x^{D+b}y^{k_0+a}(y^{3Q}+3),
\qquad0\le a\le b/2.
$$


Write $\Psi_a=x^Dp_a$. Then


$$
\deg p_a\le R_*+\frac{3b}{2}
=\nu-(n_J+1)\le\nu-3
$$


for sufficiently large original indices.

Thus Theorem 3.1 applies to every pair $\Psi_a,\Psi_c$, including every endpoint-annihilating combination


$$
\Psi_a+\Psi_{a+1}
=(y+1)x^{D+b}y^{k_0+a}(y^{3Q}+3).
$$



Let $\mathcal F_a$ be the actual complete-core correction of $\Psi_a$. Put $t=a+c$, so $0\le t\le b$. The compressed polynomial is


$$
B_{ac}
=
x^{10Q+b}(\beta+3y)y^{3Q+1+t}(y^{3Q}+3)^2.
$$


Hence


$$
B_{ac}=B_{\rm high}+6B_{\rm mid}+9B_{\rm low},
\tag{4.1}
$$


where the three starting powers of $y$ are respectively


$$
9Q+1+t,\qquad6Q+1+t,\qquad3Q+1+t.
$$



### 4.2 The high term is already closed

The accepted complete raw radical theorem, together with its paid low-degree moment formula, gives


$$
\mathcal J_h(B_{\rm high})\in3^{30}\mathbb Z_3.
\tag{4.2}
$$


This is reused at raw scope only. No old large calculation is repeated.

### 4.3 Evaluation of the two new terms

Since all degrees are below $2D$, the only poles relevant modulo $3^{30}$ have


$$
2s+1=dQ,\qquad d\in\{1,3,\ldots,39\}.
$$


Their weights in $\mathcal J_h$ are $3^{29}/d$.

For $6B_{\rm mid}$, only $3\mid d$ can contribute. The coefficient index in $x^{10Q+b}$ is


$$
k_d=\frac{(d-12)Q-3}{2}-t,
$$


or $k_d-1$ for the $3y$-term.

The indices for $d=3,9$ are negative. Those for $d=33,39$ are above the degree. The remaining values $d=15,21,27$, after expansion of $x^b$, lie respectively in the strict intervals


$$
uQ+\frac Q3<k<uQ+\frac{2Q}{3},
\qquad u=1,4,7.
\tag{4.3}
$$


The margin follows from


$$
2b+\frac52<\frac Q6
$$


at sufficiently large original indices.

Reuse the established binomial valuation identity


$$
v_3\binom{10Q}{uQ+r}
=
v_3(Q)-v_3(r)+v_3\binom9u.
$$


In (4.3), $v_3(Q)-v_3(r)\ge2$, and the three values $u=1,4,7$ have


$$
v_3\binom9u=2.
$$


Thus all these coefficients have valuation at least $4$. Even at $d=27$, the weight including the factor $6$ has valuation $27$. Therefore


$$
\boxed{6\mathcal J_h(B_{\rm mid})\in3^{30}\mathbb Z_3.}
\tag{4.4}
$$



For $9B_{\rm low}$, only $d=9,27$ can contribute below $3^{30}$. The $d=9$ index is in the first interval in (4.3), and its coefficient has valuation at least $4$. The $d=27$ index is above the degree, including the one-step $3y$ shift. Hence


$$
\boxed{9\mathcal J_h(B_{\rm low})\in3^{30}\mathbb Z_3.}
\tag{4.5}
$$



Combining (4.1)–(4.5),


$$
\mathcal J_h(B_{ac})\in3^{30}\mathbb Z_3.
$$


The evaluated scalar $K_N$ is a unit, so Theorem 3.1 proves


$$
\boxed{G_c(\mathcal F_a,\mathcal F_c)\in3^{30}\mathbb Z_3.}
\tag{4.6}
$$



### Theorem 4.1 — The actual next coefficient is zero

The paid one-lift stationary identity from Turn 0 is


$$
\Pi
=
-\frac{G_c(\mathcal F,\mathcal F)}{3^{29}}\pmod3.
$$


Equation (4.6) therefore gives


$$
\boxed{\Pi=0.}
\tag{4.7}
$$



This evaluates the entire matrix indexed by $0\le a,c\le b/2$, not merely one entry. In particular,


$$
\boxed{V^T\Pi V=0}
$$


for the endpoint-annihilating columns $e_a+e_{a+1}$.

Its rank over $\mathbb F_3$ is exactly zero. This is not a claim that the rational corrected Gram matrix itself is zero.

---

## 5. A new proof of the nonterminal strip conclusion

The older support-layer proof is not needed for the following argument.

### 5.1 Actual corrected $K$-to-$J$ entries

For


$$
0\le u<\ell,\qquad \ell\le v\le\tau-2,
$$


both middle indices $R_*+u,R_*+v$ are nonterminal. Theorem 3.1 applies with


$$
B=x^D(\beta+3y)y^{9Q+1+u+v}.
$$



Modulo $3^{29}$, the only surviving principal extraction is the pole $d=27$. Its coefficient index is


$$
k=\frac{9Q-3}{2}-u-v,
$$


and the exact finite bounds give


$$
4Q-b+2\le k<\frac{9Q}{2}.
$$


Thus the band beginning at $3Q$ ends at least two positions before $k$, while the only possible band is the one beginning at $4Q$.

Using


$$
x^D\equiv(y^Q-1)^9x^{N_0}\pmod{27},
$$


the coefficient of that band is


$$
-\binom94=-126\equiv9\pmod{27}.
$$


The $3y$-shift carries one additional factor of $3$. The other surviving poles either have negative extraction index, lie in the characteristic-$3$ gap, or are beyond the degree. Consequently,


$$
\boxed{
\frac{(S_c)_{R_*+u,R_*+v}}{3^{28}}
\equiv[y^{E-u-v}]x^{N_0}\pmod3.
}
\tag{5.1}
$$



This calculation uses the actual corrected pairing theorem, not a raw-to-corrected support assertion.

### 5.2 The finite prefix is also paid

For a prefix index $0\le p\le(P_0-1)/2$, the corresponding principal index is


$$
P_0-1-p-v.
$$


Its minimum is


$$
4Q+\frac b2+3>3Q+N_0,
$$


and it is below $P_0$. The same compressed theorem, now only needed modulo $3^{28}$, gives


$$
(\mathsf B_1)_{p,v}
=
[y^{3Q-1-p-v}]x^{N_0}\pmod3.
\tag{5.2}
$$



The established **finite** prefix inverse then gives


$$
(\mathsf B_1^T\mathsf A_0^{-1}\mathsf B_1)_{u,v}
=
[y^{C-u-v}](1-y)^{N_0},
\qquad C=\frac{3Q-3}{2}.
$$


No infinite prefix is introduced. Moreover,


$$
C-u-v\ge N_0+2,
$$


so this prefix correction is zero throughout the strip.

With the sign $U_c=-S_c/3^{26}$, (5.1) therefore yields


$$
\boxed{
(\bar L_c)_{u,v-\ell}
=[y^{E-u-v}](1-y)^{-b}.
}
\tag{5.3}
$$



This supplies the desired strip conclusion by a new original-object argument. The previous support-layer proof still has its historical audit status; none of its unquantified higher supports has been used here.

### 5.3 The terminal-only contraction and matrix return

For $g_a=x^by^a$,


$$
g_a^T\bar L_{c,\cdot,v-\ell}
=
[y^{E-v}]y^a=0,
$$


because


$$
E-v\ge b/2+2>a.
$$


Thus


$$
G^T\bar L_c=\gamma_c\delta_J^T,
\qquad
\gamma_c=G^T\bar L_c\delta_J.
\tag{5.4}
$$


The amplitude $\gamma_c$ is retained and is not evaluated here.

Using the accepted finite identities


$$
\bar B^{-1}\delta_J=-e_0,\qquad
\delta_J^T\bar B^{-1}\delta_J=0,
$$


one obtains


$$
\boxed{
27G^TL_cB_c^{-1}L_c^TG\in81M.
}
\tag{5.5}
$$



The accepted complete producer-return difference gives the same conclusion for the actual producer. Therefore the actual second-radical digit is zero:


$$
\boxed{
G^T\mathcal S_{\rm act}^{(2)}G\in81M.
}
\tag{5.6}
$$



This application does not rely on silently accepting the old strip proof: equations (5.1)–(5.3) are the replacement derivation.

---

## 6. Complete forcing, physical terminal, and all returns

### 6.1 The producer is unchanged

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
\qquad b_{\rm force}=-n-66.
$$


The signed $\xi$ and its previously paid normalization are retained, as are


$$
\mathscr R(-1)
=-\frac{\xi((A+1)!)^2}{3^7}
$$


and


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$



The filter makes no alteration to this complete force or return.

### 6.2 First-radical returns

For $\alpha=c,\mathrm{act}$, retain


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
=\lambda_\alpha-\frac13f_{\alpha,J}^TB_\alpha^{-1}f_{\alpha,J}.
\tag{6.1}
$$


The inverse payment is $3^{-1}$.

The new physical-terminal estimate gives


$$
\widehat t:=G^T\bar t_K=0,
$$


so the previously established producer formula


$$
\gamma_{\rm act}=\gamma_c+\bar\kappa\,\widehat t
$$


now yields


$$
\gamma_{\rm act}=\gamma_c.
\tag{6.2}
$$



Nevertheless,


$$
G^Tf_\alpha^{(2)}
\equiv G^Tf_{\alpha,K}+3\varepsilon_0\gamma_\alpha\pmod9
\tag{6.3}
$$


still contains the unevaluated middle-terminal amplitude.

The full producer differences remain


$$
f_{\rm act}^{(2)}-f_c^{(2)}
\equiv3\bar\kappa\varepsilon_0\bar t_K\pmod9,
$$




$$
\lambda_{\rm act}^{(2)}-\lambda_c^{(2)}
\equiv
-2\bar\kappa\varepsilon_0(\bar t_J^Tu_0)\pmod3.
\tag{6.4}
$$


The first is now zero modulo $9$. The second need not vanish: only the last component of $\bar t_J$ can remain, and that component has not been evaluated.

### 6.3 Rank-$b$ returns

Retain the exact three-channel formulas


$$
T_{\rm new}=T_{RR}-81M_b^TA_b^{-1}M_b,
$$




$$
f_{\rm new}=f_R-3M_b^TA_b^{-1}f_b,
$$




$$
\lambda_{\rm new}
=\lambda^{(2)}-\frac19f_b^TA_b^{-1}f_b.
\tag{6.5}
$$


The inverse payment is $3^{-2}$.

Equation (5.6) and the matrix return in (6.5) show that, after actual endpoint adaptation,


$$
\boxed{
T=\begin{pmatrix}a&z^T\\z&C\end{pmatrix}\in81M.
}
\tag{6.6}
$$


The complete returned diagonal still satisfies


$$
v_3(\lambda)=-1.
$$



At the next digit, the matrix return


$$
81M_b^TA_b^{-1}M_b
$$


is visible and cannot be discarded. The endpoint and diagonal returns in (6.5) have not been canceled.

---

## 7. What the evaluated zero does—and does not—give

### 7.1 The previous nonsingular-digit route fails at this digit

The proposed criterion


$$
\det(V^T\Pi V)\ne0
$$


is now decisively false:


$$
V^T\Pi V=0.
$$


Thus the order-$27$ digit cannot supply the directional inverse by nonsingularity.

The new conclusion is a deeper residual matrix, not an evaluated inverse of its endpoint-annihilator block.

### 7.2 The actual scalar obstruction remains

Write


$$
a=81\alpha,\qquad z=81w,\qquad C=81B,\qquad\lambda=\eta/3,
\quad \eta\in\mathbb Z_3^\times.
$$


If $B$ is nonsingular, put


$$
\sigma=w^TB^{-1}w.
$$


Then


$$
D_0=\det C\cdot81(\alpha-\sigma),
$$




$$
\boxed{
D_1=\det C\,(1-27\eta\alpha+27\eta\sigma).
}
\tag{7.1}
$$


The critical shell is now


$$
v_3(\sigma)=-3.
$$


The earlier completion obstruction has not disappeared; its threshold has merely shifted by one digit.

For example, an actual bound


$$
C^{-1}z\in3^{-1}\mathbb Z_3^{b/2}
$$


would imply


$$
a-z^TC^{-1}z\in27\mathbb Z_3
$$


and make the multiplier in $D_1/\det C$ a unit. If the Schur scalar is nonzero, the relative cofactor gain would then be at least $3$. An integral directional solution would give a gain of at least $4$.

Neither hypothesis has been proved here.

### 7.3 A concrete next local obligation

The next coefficient must include, simultaneously:

1. the corrected pairing one digit beyond the present whole division by $3^{29}$;
2. the second prefix lift;
3. the next $J$-return, including $\gamma_c$;
4. the order-$81$ producer contribution;
5. the now-visible rank-$b$ matrix return;
6. the exact endpoint and complete diagonal returns.

The second prefix lift is particularly explicit. If


$$
X=3P_G+9Z,
$$


the exact stationary identity is


$$
-\frac{G_c(\mathcal F,\mathcal F)}{3^{26}}
=
G^T\mathcal R_{c,KK}G+81Z^T\mathsf AZ.
$$


Thus $Z^T\mathsf AZ$, previously harmless, enters the next normalized digit. It must be evaluated, not omitted.

A useful follow-on lemma is therefore:

> **Next returned directional lemma.** On the same infinite original subwindow, form the exact endpoint-adapted $T\in81M$, including all six contributions above. Prove that its actual $C$ is nonsingular and that $C^{-1}z\in3^{-1}\mathbb Z_3^{b/2}$, or evaluate the critical-shell multiplier in (7.1) sufficiently to exclude resonance.

A growing saving would still require additional information, such as a controlled nonzero Schur scalar whose valuation tends to infinity.

### 7.4 The complete-source resonance is retained

The complete moments still satisfy


$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\qquad0\le t\le2n-2.
$$


The forward recurrence has its genuine $3^h$ divisor at


$$
t_*=\frac{3^h-5}{2}.
$$


Its highest moment remains inside the original boundary because


$$
\frac{3H+1}{2}\le2n-1
\iff H-4D+5\ge0.
$$



The local filter does not delete this complete-source divisor or replace the final real determinant by a pole determinant.

---

## 8. Division and arithmetic ledgers

### 8.1 Paid divisions

| Operation | Payment |
|---|---|
| Original finite pole denominators | $3^h$, with cutoff $4n-3$ |
| Macro Jacobi normalization | Coefficientwise proof $v_3(r_k)=p-v_3(k)\ge2$ |
| Actual mixed $W$-projection | Established loss of one digit |
| Filter residual $3^{16}$ | Column error $3^{15}$, stationary pairing error $3^{30}$ |
| Filter residual $3^{25}$ | Column error $3^{24}$, yielding the physical-terminal bound |
| Pole/complete-core replacement | Previously proved $3^h$ Schur congruence |
| Core normalization | $S_c/3^{26}$ |
| Unit prefix | Integral unit inverse |
| First prefix lift | Exact $81Z^T\mathsf AZ$ stationary return |
| Projection observation | Whole pairing divided by $3^{29}$ |
| First-radical inverse | $3^{-1}B_\alpha^{-1}$ |
| Rank-$b$ inverse | $3^{-2}A_b^{-1}$ |
| Physical coefficient normalization | Actual coefficient divided by $3^{20}$ |
| Eventual directional inverse | Still unproved |
| Complete forward resonance | Genuine $3^h$ divisor retained |

There is no new content division.

### 8.2 Actual contents, clearer, all-prime gcd, and whole error

The actual original column contents and the actual least simultaneous clearer $\ell_{\rm clr}$ are unchanged. The rational coefficients of $R_N$, or the beta norm in $K_N$, do not define a new global clearer.

Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the gcd over **all primes**


$$
\boxed{g_\ell=\gcd(|A_\ell|,|B_\ell|).}
$$



For $B_\ell\ne0$, the actual primitive quantities are


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole evaluated error is exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{8.1}
$$



An irrationality proof still requires, at the **same infinite original indices**,


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
\tag{8.2}
$$



The new matrix digit does not establish (8.2). Common determinant depths from eliminated blocks remain common to the distinguished cofactors and are not, by themselves, primitive-denominator savings.

---

## 9. Bounded exact-arithmetic verification

No computation was performed, and no dense original matrix calculation is proposed.

The uniform projection theorem is analytic. Its only optional new arithmetic certificate concerns the fixed scalar in (3.3).

### Inputs

* modulus $81$;
* integers $1,\ldots,80$;
* $\binom{26}{13}$;
* the exponents $15,16$, used only in the proved recurrence $B_q\equiv-B_{q-1}$.

### Expected verifiable outputs



$$
\binom{26}{13}=10400600\equiv38\pmod{81},
$$




$$
\prod_{\substack{1\le a\le80\\3\nmid a}}a\equiv-1\pmod{81},
$$




$$
\left(\prod_{\substack{1\le a\le40\\3\nmid a}}a\right)^2
\equiv1\pmod{81},
$$




$$
B_{15}\equiv38,\qquad B_{16}\equiv43,
$$




$$
B_{15}B_{16}\equiv14,\qquad14^{-1}\equiv29,\qquad4^{-1}\equiv61,
$$


and finally


$$
\boxed{K_N\equiv13\pmod{81}.}
$$



This bounded calculation checks fixed constants in the proof. It is not an auxiliary original tuple, and its finite output is not being extrapolated to establish the original-index theorem.

No closed $350$- or $62$-coordinate calculation is reopened.

---

## 10. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Paid pole/complete-core replacement and one-lift identity | Reused at supplied scope; external audit status retained |
| Uniform sparse filter residual against the actual mixed $W$ | **Proved here** |
| Physical degree and all-$Y_m$ boundary checks for nonterminal columns | **Proved here** |
| Explicit nonzero trial defect at the last middle coordinate | **Proved here** |
| Same-$W$ corrected-pairing compression through $3^{30}$ | **Proved here** |
| Scalar $K_N\equiv13\pmod{81}$ | **Evaluated here** |
| Actual coefficient $\Pi$ | **Evaluated: zero** |
| Endpoint-annihilator digit $V^T\Pi V$ | **Evaluated: zero, rank $0$** |
| $[y^m]F_i\in3^{24}$ for $i\le\nu-2$ | **Proved here** |
| Older full support-layer proof | Its independent audit remains incomplete |
| Required nonterminal strip conclusion | **New alternative derivation given here** |
| Actual residual after paid rank-$b$ elimination lies in $81M$ | **Derived here from the retained complete returns** |
| Middle-terminal amplitude and last physical-terminal amplitude | Unevaluated and retained |
| Actual directional inverse / critical-shell nonresonance | Open |
| Growing relative-cofactor saving | Open |
| All-prime primitive denominator versus nonzero whole error | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

### Final conclusion

The requested next coefficient is no longer an unevaluated mixed-subspace inverse:


$$
\boxed{\Pi=0}
$$


uniformly on the same sufficiently large original subwindow.

The proof uses a sparse Jacobi filter only after checking its residual against the actual LOW span and the entire physical HIGH span. The selected inverse loss, finite pole cutoff, one-lift stationary error, and exceptional physical terminal are all paid explicitly.

The evaluated zero advances the matrix depth to $81M$, but it also rules out the proposed nonsingular-digit directional argument at order $27$. The exact remaining local bottleneck is the fully returned endpoint-annihilator solve—or the equivalent critical-shell scalar—with the next prefix, $J$, producer, terminal, endpoint, diagonal, and rank-$b$ returns retained.

Beyond that local obstruction, the decisive global requirement is still (8.2), involving the actual all-prime gcd, actual primitive denominator, and nonzero whole evaluated error at the same infinite original indices.



$$
\boxed{\text{No unconditional rationality or irrationality proof for }e+\pi
\text{ is obtained.}}
$$


