> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the original-index terminal coefficient theorem

## Abstract and audit verdict

The new coefficient theorem in A4 Turn 4 survives an independent audit of its arithmetic, inverse payments, and finite boundaries. On the unchanged sufficiently large original family, the actual complete-core corrected columns satisfy


$$
\boxed{
[y^m]\mathcal F_a\equiv-3^{27}\delta_{a,b/2}\pmod{3^{28}},
\qquad 0\le a\le b/2.
}
$$


Consequently, the previously established normalized coupling identity gives


$$
\boxed{\gamma_c=0.}
$$



The proof below independently checks the points on which this conclusion depends:

- the three auxiliary polynomials belong to the **actual finite LOW/HIGH space**;
- the exceptional $p=25$ moment has the stated normalization;
- three columns, rather than two, pay the inverse loss needed for a terminal dual modulo $9$;
- the $p=26$ virtual residual includes the Frobenius error and uses only completed moments inside the original pole cutoff;
- the collision $2s+1=27Q$ is evaluated by an exact moment, not by an invalid denominator expansion;
- the $9Q$-denominator layer and the finite Frobenius coefficient are evaluated;
- the part above $Y_m$ is removed, and its returned correction is proved to vanish modulo $3^{28}$;
- the remaining physical coefficient has the claimed sign and leading unit.

The optional value $\mathfrak t_{25}\equiv7\pmod9$ also checks out. It is not essential: the principal argument uses only the exact symbolic normalization and the fact that $\mathfrak t_{25}$ is a ternary unit.

No closed digit table, dense original matrix calculation, or auxiliary kernel certificate is reopened. The result is a fixed-precision theorem, not a growing cofactor saving. The fully returned directional problem and the same-index comparison involving the actual all-prime gcd and nonzero whole error remain open. In particular, this report does not decide the rationality or irrationality of $e+\pi$.

---

## 1. Original objects and the scope of the audit

All congruences are over $\mathbb Z_3$, with $v_3(3)=1$. A congruence modulo $3^rW\mathbb Z_3$ refers to coordinates in the displayed actual LOW/HIGH basis.

### 1.1 The original index family is unchanged

We retain


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


together with


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15},
$$


and


$$
\frac{103}{1000}<\frac{N_0}{P_0}<\frac{104}{1000}.
$$



The original arithmetic relations remain


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
x=y-1,\qquad Q=3^{h-29},\qquad b=Q-N_0.
$$


Thus


$$
P_0=9Q,\qquad H=3^{28}Q,\qquad D=10Q-b,
$$


and


$$
\frac{64}{1000}<\frac bQ<\frac{73}{1000}.
$$


Here $Q$ is odd and $D,b$ are even. We also retain


$$
m=\frac{H-D+1}{2},\qquad
\nu=\frac D2-1=5Q-\frac b2-1,\qquad d=D+\nu.
$$


An especially useful exact identity is


$$
\boxed{m+\nu=\frac{H-1}{2}.}
\tag{1.1}
$$



Only sufficiently large indices from this original family are used. No auxiliary choice of $P,r$, or of a smaller ternary tuple, is substituted. The supplied density result is reused only for its stated conclusion that infinitely many original indices lie in this same subwindow.

### 1.2 The finite spaces and complete corrections

The actual finite coordinates are


$$
U_s=x^s\quad(0\le s<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_t=y^t\quad(d\le t\le m),\qquad W=[U\ Y].
$$


The omitted monomial window is


$$
\{D,\ldots,d-1\}.
$$


The physical HIGH terminal is $Y_m$, not $z_{\nu-1}$.

The complete functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad \mathfrak f(y^t)=(2t)!.
$$


The complete core is


$$
G_c(f,g)=\mathcal M(Q_cfg),
\qquad
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A.
$$


Its actual corrected columns are


$$
F_i=z_i-WE_c^{-1}G_c(W,z_i),
\qquad E_c=G_c(W,W).
$$



For the pole calculations, define the fixed truncated functional


$$
\Lambda_h(P)=
3^h\sum_{v=0}^{K_{\rm phys}}\frac{[y^v]P}{2v+1},
\qquad
K_{\rm phys}=2n-2=2H-2D+2,
\tag{1.2}
$$


and


$$
\mathcal P(f,g)=\Lambda_h\!\left(x^A(\beta+3y)fg\right),
\qquad E_{\mathcal P}=\mathcal P(W,W).
$$



The largest original denominator is exactly


$$
2K_{\rm phys}+1=4n-3=4H-4D+5<3^{h+1}.
\tag{1.3}
$$


Consequently $\Lambda_h$ maps every polynomial in $\mathbb Z_3[y]$ to $\mathbb Z_3$, even when that polynomial has terms above $K_{\rm phys}$: those terms are simply not included.

This last distinction is important. For a virtual polynomial of degree above $m$, an untruncated beta integral need not equal the prescribed functional. All virtual calculations below use (1.2). A macro moment is completed only after its full support has been checked against (1.3).

### 1.3 Closed inputs reused

The audit uses the following established results at their stated original-object scope:

1. the original corrected-basis integrality and unimodularity;
2. the paid inverse estimate
   

$$
E_{\mathcal P}^{-1}\in3^{-1}\operatorname{Mat}(\mathbb Z_3);
$$


3. the actual pole/complete-core column comparison
   

$$
F_{\mathcal P}-F_c\in3^{h-1}W\operatorname{Mat}(\mathbb Z_3);
$$


4. the sparse Jacobi coefficient valuations, finite macro orthogonality, and exceptional unit moment recalled below;
5. the closed nonterminal coupling strip and the terminal bootstrap;
6. the fully normalized identity
   

$$
(\gamma_c)_a
   =-\delta_{a,b/2}-3^{-27}[y^m]\mathcal F_a\pmod3;
   \tag{1.4}
$$


7. the finite prefix identities and the already paid producer and rank-$b$ returns.

The previously audited full Jacobi inverse and Schur/Selberg interfaces are not recomputed. No valuation conclusion from real positivity or from an unevaluated determinant quotient is used here.

---

## 2. The macro-polynomial facts needed in this audit

For $p\ge2$, put


$$
N=3^{p-1},\qquad M=\frac{N-1}{2},
$$


and


$$
R_N(Y)={}_2F_1\!\left(-M,\frac{3N}{2};\frac12;Y\right)
=\sum_{k=0}^M r_kY^k.
$$


The closed coefficient formula is


$$
r_k=(-1)^k\binom Mk
\frac{\prod_{a=0}^{k-1}(3N+2a)}
{\prod_{a=0}^{k-1}(2a+1)}.
$$


Its paid valuation statement is


$$
v_3(r_k)=p-v_3(k)\ge2\qquad(1\le k\le M).
\tag{2.1}
$$


In particular,


$$
R_N\in\mathbb Z_3[Y],\qquad R_N\equiv1\pmod9.
\tag{2.2}
$$



If


$$
(Y-1)^NR_N(Y)=\sum_j a_jY^j,
$$


the finite macro moments satisfy


$$
\sum_j\frac{a_j}{2(j+q)+1}=0
\qquad(0\le q<M).
\tag{2.3}
$$


The first exceptional moment is normalized by


$$
\mathfrak t_p
=
3^p\sum_j\frac{a_j}{2(j+M)+1}.
\tag{2.4}
$$


Its exact closed value is


$$
\mathfrak t_p
=
(-1)^{N+M}3^p2^{4N-1}
\frac{M!(N+M)!(2N)!}{(4N)!},
\qquad v_3(\mathfrak t_p)=0.
\tag{2.5}
$$



Thus (2.4) includes the factor $3^p$, while the corresponding integral contains the usual factor $1/2$. There is no missing factor of $2$ or $3$ in the exceptional scalar used below.

---

## 3. Independent construction of the actual physical-terminal dual

### 3.1 Exact divisibility of the three polynomials

Define


$$
g_r=\binom{D+r-1}{r}\quad(r\ge0),\qquad g_r=0\quad(r<0),
$$


and


$$
\Omega_k
=
y^{d+k}-\sum_{u=0}^{D-1}\binom{d+k}{u}x^u,
\qquad k=0,1,2.
\tag{3.1}
$$



The subtracted expression is precisely the Taylor polynomial of $y^{d+k}=(1+x)^{d+k}$ through degree $D-1$ in $x$. Hence $\Omega_k$ is divisible by $x^D$.

Its quotient is


$$
\boxed{
\Omega_k=x^Ds_k,\qquad
s_k(y)=\sum_{\ell=0}^{\nu+k}g_\ell y^{\nu+k-\ell}.
}
\tag{3.2}
$$


To verify the quotient independently, expand at infinity:


$$
\frac{y^{d+k}}{(y-1)^D}
=y^{\nu+k}(1-y^{-1})^{-D}
=\sum_{\ell\ge0}g_\ell y^{\nu+k-\ell}.
$$


The polynomial part is exactly $s_k$. Its remainder has degree below $D$, so it is the same remainder as the Taylor subtraction in (3.1).

Thus no quotient factor or sign is missing.

Moreover, (3.1) expresses $\Omega_k$ directly in the actual $W$: it uses one HIGH monomial $y^{d+k}$ and actual LOW coordinates $x^u$.

### 3.2 Filtering does not leave the actual $W$

For this section put


$$
N_{25}=3^{24},\qquad
M_{25}=\frac{N_{25}-1}{2},\qquad
L_{25}=81Q,
$$


and


$$
R^{[25]}(y)=R_{N_{25}}(y^{L_{25}}).
$$


Then


$$
\deg R^{[25]}=\frac{H-L_{25}}2.
$$


A direct calculation gives


$$
m-\deg(\Omega_kR^{[25]})
=\frac{81Q-4D+3-2k}{2}>0
\qquad(k=0,1,2).
\tag{3.3}
$$


Every nonconstant filter term starts at monomial degree at least $81Q>d+2$. Hence it introduces no omitted-window coefficient. Therefore


$$
\boxed{\Omega_kR^{[25]}\in W\mathbb Z_3,\qquad k=0,1,2.}
\tag{3.4}
$$



This is a finite-$W$ construction. It is not a replacement of $W$ by a consecutive orthogonal-polynomial space.

### 3.3 Residual against every actual row

Modulo $3^{25}$,


$$
x^H\equiv(y^{L_{25}}-1)^{N_{25}}.
\tag{3.5}
$$



For a LOW row $x^u$, the nonsparse factor in


$$
\mathcal P(x^u,\Omega_kR^{[25]})
$$


is


$$
x^us_k(\beta+3y),
$$


whose degree is at most $d+k<(L_{25}-1)/2$. It therefore misses the residue class of every pole which can survive modulo $3^{25}$.

For a HIGH row $Y_{m-r}$, an exceptional macro moment occurs only when the exponent in


$$
y^{m-r}s_k(\beta+3y)
$$


equals


$$
m+\nu=\frac{H-1}{2}.
$$


Using (3.2), its coefficient is exactly


$$
\beta g_{k-r}+3g_{k-r+1}.
\tag{3.6}
$$


Only $0\le r\le k+1$ can occur. All other active macro moments have $q<M_{25}$ and vanish by (2.3).

The largest denominator in the exceptional completed moment is


$$
(4N_{25}-1)L_{25}=4H-81Q,
$$


which is strictly below $4H-4D+5$. Thus this is an entirely physical moment.

It follows that


$$
\boxed{
\mathcal P(W,\Omega_kR^{[25]})
\equiv
\mathfrak t_{25}
\sum_{r=0}^{k+1}
(\beta g_{k-r}+3g_{k-r+1})e_{Y_{m-r}}
\pmod{3^{25}}.
}
\tag{3.7}
$$


For sufficiently large original indices, $m-3\ge d$, so every HIGH coordinate displayed here is an actual row.

### 3.4 The three-column convolution and the paid inverse loss

Since


$$
\beta=D-H-71\equiv1\pmod9,
$$


$\beta$ is a unit. Put


$$
\chi=-\frac3\beta
$$


and


$$
\mathscr D_{\rm tr}
=
\frac{R^{[25]}}{\beta\mathfrak t_{25}}
(\Omega_0+\chi\Omega_1+\chi^2\Omega_2).
\tag{3.8}
$$


This lies in $W\mathbb Z_3$.

For $0\le r\le3$, the exact finite convolution is


$$
\begin{aligned}
\sum_{k=0}^2
\chi^k(\beta g_{k-r}+3g_{k-r+1})
&=
\beta\sum_{k=0}^2
\chi^k(g_{k-r}-\chi g_{k-r+1})\\
&=\beta g_{-r}-\beta\chi^3g_{3-r}\\
&=\beta\delta_{r0}-\beta\chi^3g_{3-r}.
\end{aligned}
$$


Therefore


$$
\mathcal P(W,\mathscr D_{\rm tr})
\equiv
e_{Y_m}
-\chi^3\sum_{r=0}^3g_{3-r}e_{Y_{m-r}}
\pmod{3^{25}}.
\tag{3.9}
$$


The whole residual is divisible by $3^3$.

Now define the exact terminal dual


$$
\mathscr D=WE_{\mathcal P}^{-1}e_{Y_m}.
\tag{3.10}
$$


Applying the established inverse bound loses one digit:


$$
\mathscr D-\mathscr D_{\rm tr}\in9W\mathbb Z_3.
$$


Consequently


$$
\boxed{
\mathscr D\in W\mathbb Z_3,\qquad
\mathscr D\equiv
\frac{\Omega_0-(3/\beta)\Omega_1}
{\beta\mathfrak t_{25}}
\pmod{9W\mathbb Z_3}.
}
\tag{3.11}
$$



The payment is exactly


$$
3^3\text{ residual}\quad\longrightarrow\quad
3^2\text{ dual-row error}.
$$



The third column is essential to this justification. Although its coefficient $\chi^2$ disappears in the final display modulo $9$, deleting it before inversion would generally leave only a $3^2$ residual, which after the inverse loss would justify a row only modulo $3$.

Finally, because $E_{\mathcal P}$ is symmetric and only the $Y_m$-coordinate of $W$ has a $y^m$ coefficient,


$$
e_{Y_m}^TE_{\mathcal P}^{-1}\mathcal P(W,P)
=\mathcal P(\mathscr D,P).
\tag{3.12}
$$


Thus (3.11) is a dual to the actual physical coefficient, not to a middle coordinate.

### 3.5 Optional normalization: the reported unit is correct

From the coefficient formula,


$$
\frac{r_M}{3^p}
=
\frac{(-1)^M2^{2M-1}}{M\binom{2M}{M}}
\prod_{a=1}^{M-1}\left(1+\frac{3N}{2a}\right).
\tag{3.13}
$$


Every factor in the product lies in $1+9\mathbb Z_3$.

For $p=25$, the closed binomial recurrence gives


$$
\binom{3^{24}-1}{(3^{24}-1)/2}\equiv7\pmod9,
\qquad
\binom{3^{25}-1}{(3^{25}-1)/2}\equiv2\pmod9.
$$


Also


$$
M_{25}\equiv4\pmod9,\qquad
(-1)^{M_{25}}=1,\qquad
2^{2M_{25}-1}\equiv2\pmod9.
$$


Hence


$$
r_{M_{25}}/3^{25}\equiv2\pmod9.
$$



The retained exact norm relation is


$$
\mathfrak t_{25}
=\frac{3^{25}K_{N_{25}}}{(4N_{25}-1)r_{M_{25}}},
$$


with


$$
K_N=
-\frac{4^{2N-1}}
{\binom{N-1}{(N-1)/2}\binom{3N-1}{(3N-1)/2}}.
$$


The displayed residues give $K_{N_{25}}\equiv4\pmod9$, and therefore


$$
\mathfrak t_{25}\equiv\frac4{(-1)\cdot2}\equiv7\pmod9.
$$


Thus


$$
\boxed{\mathscr D\equiv4\Omega_0+6\Omega_1\pmod9.}
\tag{3.14}
$$



All denominators reduced here are units. More importantly, none of the following proof depends on (3.14); the symbolic formula (3.11) is sufficient.

---

## 4. The $p=26$ trial and its finite physical truncation

Let


$$
N=3^{25},\qquad M=\frac{N-1}{2},\qquad L=27Q,
\qquad R(y)=R_N(y^L).
$$


For the prescribed input, write


$$
\Psi_a=x^Dp_a
=x^{10Q}y^{k_0+a}(y^{3Q}+3),
\qquad
k_0=\frac{3Q+1}{2}.
$$


Set


$$
t=\frac b2-a,\qquad 0\le t\le b/2.
\tag{4.1}
$$



The degree bound needed for the original middle coordinates is


$$
\deg p_a=b+\frac{9Q+1}{2}+a\le\nu-3
\tag{4.2}
$$


for sufficiently large original indices. Indeed, the difference at the largest $a$ is at least


$$
\frac{Q-4b-9}{2}>0.
$$



The virtual filtered polynomial


$$
V_a=\Psi_aR
$$


has degree


$$
\deg V_a=m+6Q-t.
\tag{4.3}
$$


It is therefore not an admissible original column.

Only the top filter term can cross $m$, since the next term has degree at most


$$
m+6Q-t-L=m-21Q-t<m.
$$


Writing $r_M=[Y^M]R_N(Y)$, define


$$
O_a=[y^{>m}](y^{ML}\Psi_a),
$$


and


$$
\boxed{
\widehat V_a=V_a-r_MO_a=[y^{\le m}]V_a.
}
\tag{4.4}
$$


Then


$$
\deg\widehat V_a\le m,\qquad
\widehat V_a-\Psi_a\in\operatorname{span}Y.
\tag{4.5}
$$


The latter assertion follows because every nonconstant filter term starts above $d$.

By (2.1),


$$
\boxed{v_3(r_M)=26.}
\tag{4.6}
$$


Thus the removal in (4.4) is visible at the precision under audit and must be returned through the actual inverse.

---

## 5. The complete virtual residual, including Frobenius error

### 5.1 Derivation of the next-scale Frobenius term

Put


$$
Z=y^{9Q},\qquad Y=y^{27Q}.
$$


Since $9Q$ is a power of $3$,


$$
x^{9Q}=Z-1+3B(y)
$$


for an integral polynomial $B$. Raising to $3N=3^{26}$ gives


$$
x^H\equiv(Z-1)^{3N}\pmod{3^{27}}.
$$


For example, the identity


$$
v_3\binom{3^s}{k}=s-v_3(k)
$$


shows that every nonconstant term in this binomial expansion has valuation at least $27$.

Next,


$$
(Z-1)^3=Y-1+3Z(1-Z).
$$


Raising to $N=3^{25}$, the linear perturbation has coefficient $3N=3^{26}$. Every term of order at least two has valuation at least $27$. Consequently


$$
\boxed{
x^H=(Y-1)^N+3^{26}E_1+3^{27}E_2,
}
\tag{5.1}
$$


where


$$
E_1=Z(1-Z)(Y-1)^{N-1},
\qquad
E_2\in\mathbb Z_3[y],
$$


and


$$
\deg E_1=H-9Q,\qquad \deg E_2\le H.
\tag{5.2}
$$



Thus the stated first Frobenius correction is correct; no contribution of the same order has been omitted.

### 5.2 Main term: all actual LOW and HIGH rows

We prove


$$
\boxed{\mathcal P(W,V_a)\in3^{27}\mathbb Z_3^{\dim W}.}
\tag{5.3}
$$



For the $(Y-1)^N$ term in (5.1), a pole surviving modulo $3^{27}$ must have denominator divisible by


$$
L=3^{h-26}.
$$


A monomial exponent $s$ in the nonsparse factor must therefore have the form


$$
s=qL+\frac{L-1}{2}.
\tag{5.4}
$$



For a LOW row, the nonsparse factor is


$$
x^up_a(\beta+3y),
$$


of degree at most $d-3<L$. Thus the only possible value is $q=0$. This contribution is not discarded by support separation: it is annihilated by the exact $q=0$ moment.

For a HIGH row $y^v$, $v\le m$, the degree bound (4.2) gives


$$
s\le m+\nu-2=\frac{H-1}{2}-2.
$$


The exponent corresponding to $q=M$ is exactly $(H-1)/2$. Therefore every possible active HIGH moment has


$$
0\le q\le M-1
$$


and vanishes by (2.3).

The largest denominator in any such completed moment is


$$
(4N-3)L=4H-81Q<4H-4D+5.
\tag{5.5}
$$


Hence these are complete moments inside the original cutoff. No moment past the physical boundary has been inserted.

### 5.3 Frobenius error: why it gains the required digit

In the $3^{26}E_1$-term, replace $R$ by $1$, using $R\equiv1\pmod9$. The resulting change is already divisible by $3^{28}$.

For every actual $W$-row, the degree of the remaining polynomial is at most


$$
(H-9Q)+m+(\nu-3)+1
=\frac{3H-1}{2}-9Q-2.
\tag{5.6}
$$


The only physical denominator of valuation $h$ is $3H=3^h$, whose coefficient index is


$$
\frac{3H-1}{2}.
$$


The degree in (5.6) misses it. Therefore every pole weight in this error term contains an additional factor $3$, giving divisibility by $3^{27}$.

The $3^{27}E_2$-term is already harmless by the integrality of the fixed truncated functional. This proves (5.3).

Notice the precise scope: $V_a$ remains virtual. Equation (5.3) is a residual certificate for the fixed truncated functional, not a declaration that $V_a$ is an original column.

---

## 6. The distinguished virtual pairing through $3^{28}$

The terminal dual needs one stronger pairing:


$$
\boxed{\mathcal P(\Omega_0,V_a)\in3^{28}\mathbb Z_3.}
\tag{6.1}
$$



Using $\Omega_0=x^Ds_0$,


$$
\mathcal P(\Omega_0,V_a)
=\Lambda_h(x^H B_aR),
$$


where


$$
B_a=
x^{10Q}s_0(\beta+3y)y^{k_0+a}(y^{3Q}+3).
\tag{6.2}
$$


Its degree is exactly


$$
\deg B_a=\frac{39Q+1}{2}-t<2D<L.
\tag{6.3}
$$



The complete product in this pairing has degree


$$
H+ML+\deg B_a
=\frac{3H+12Q+1}{2}-t<K_{\rm phys}.
\tag{6.4}
$$


Thus, unlike some general virtual-row pairings, this entire pairing lies inside the original cutoff.

### 6.1 The two exceptional denominator layers

Write


$$
A_1(Y)=(Y-1)^NR_N(Y)=\sum_q a_qY^q.
$$


For a coefficient $B_{a,s}$, put $c_s=2s+1$. By (6.3),


$$
0<c_s<4D<40Q.
$$



There are exactly two possibilities with $v_3(c_s)\ge h-27$:

| Value of $c_s$ | Pole contribution before multiplying by $B_{a,s}$ | Evaluation |
|---|---|---|
| $27Q=L$ | $\displaystyle 3^{26}\sum_q\frac{a_q}{2q+1}$ | Exactly $0$, by the $q=0$ macro moment |
| $9Q$ | $\displaystyle 3^{27}\sum_q\frac{a_q}{1+6q}$ | $0\pmod{3^{28}}$, since the normalized sum is $\sum_q a_q=A_1(1)=0\pmod3$ |

Every other $c_s$ has valuation at most $h-28$. Since the added quantity $2qL$ has larger valuation, the denominator $c_s+2qL$ has the same valuation as $c_s$, and each corresponding pole term is in $3^{28}$.

In particular, at $c_s=L$ one must not expand in $L/c_s$. The exact collision has instead been evaluated by a complete finite moment. Its largest denominator is $3H$, which is physical.

### 6.2 The finite Frobenius coefficient

Insert (5.1). In the $3^{26}E_1$-term, replacing $R$ by $1$ changes the pairing only by $3^{28}$.

In the $3^{27}E_2$-term, replace $R$ by $1$. Its remaining degree is at most


$$
H+\deg B_a<\frac{3H-1}{2},
$$


so it misses the unit-weight pole and gains one further digit. It is therefore in $3^{28}$.

It remains to examine $3^{26}\Lambda_h(E_1B_a)$. Below modulus $3^{28}$, only the pole with denominator $H$, of weight $3$, can contribute. Set


$$
n_*=\frac{H-1}{2}=m+\nu.
$$


Modulo $3$,


$$
E_1=(Z-Z^2)\sum_{q=0}^{N-1}Y^q.
$$


Because $\deg B_a<20Q<L$, the finite coefficient extraction has only the following possibilities:

- the $Z$-term at $q=M$ asks for $B_a$ at degree $(9Q-1)/2$;
- the nearest $Z^2$-term asks for degree $(45Q-1)/2$, which is above $\deg B_a$;
- every other shift asks for a negative degree or a degree above $\deg B_a$.

Therefore, with the modulus made explicit,


$$
[y^{n_*}]E_1B_a
\equiv [y^{(9Q-1)/2}]B_a\pmod3.
\tag{6.5}
$$


Modulo $3$, the low term $3y^{k_0+a}$ in (6.2) disappears. The remaining polynomial starts at degree at least


$$
k_0+a+3Q=\frac{9Q+1}{2}+a,
$$


strictly above $(9Q-1)/2$. Hence (6.5) is zero.

The $3^{26}$ Frobenius factor, the pole weight $3$, and this final coefficient zero give divisibility by $3^{28}$. This proves (6.1).

---

## 7. Explicit audit of the overflow and its returned correction

### 7.1 The overflow with its exact strict cutoffs

Let


$$
c_j=[y^j]x^{10Q};
$$


as coefficients of a polynomial, $c_j=0$ outside $0\le j\le10Q$.

The two starting exponents in $y^{ML}\Psi_a$ are


$$
m-4Q-t,\qquad m-7Q-t.
$$


Consequently


$$
\boxed{
O_a=
y^{m-4Q-t}\sum_{j>4Q+t}c_jy^j
+
3y^{m-7Q-t}\sum_{j>7Q+t}c_jy^j.
}
\tag{7.1}
$$


Both upper bounds are $10Q$.

The strict inequalities are essential. The coefficient at $j=4Q+t$ belongs to $Y_m$, not to the removed tail.

### 7.2 Reduction of the two tail pairings to one coefficient

For $k=0,1$, put


$$
C_k=(\beta+3y)s_kO_a.
$$


Its support is contained in a band around $n_*=m+\nu$:


$$
m+1\le\deg_{\min}C_k,\qquad
\deg C_k\le n_*+6Q-t+k+1.
\tag{7.2}
$$


This band misses $n_*\pm H/3$ and the other relevant macro translates, because $H=3^{28}Q$.

Modulo $9$,


$$
x^H\equiv y^H-3y^{2H/3}+3y^{H/3}-1.
\tag{7.3}
$$


Within the original cutoff, the only pole weights not divisible by $9$ are:

- denominator $H$, index $n_*$, weight $3$;
- denominator $3H$, index $n_*+H$, weight $1$.

The support check in (7.2) makes the two middle shifts in (7.3) irrelevant. At the denominator $H$, the contribution is $-3[y^{n_*}]C_k$; at $3H$, it is $+[y^{n_*}]C_k$. Hence


$$
\boxed{
\mathcal P(\Omega_k,O_a)
\equiv-2[y^{n_*}]C_k\pmod9,
\qquad k=0,1.
}
\tag{7.4}
$$



These particular pairings lie wholly inside the physical cutoff. The general pairing $\mathcal P(W,O_a)$ need not do so, but later only its integrality under the fixed truncation will be used.

### 7.3 Binomial stripping and nonmultiple-$Q$ valuations

Because $10Q$ is even,


$$
c_j=(-1)^j\binom{10Q}{j}.
\tag{7.5}
$$



For $j=uQ+r$, $0<r<Q$, the closed valuation formula gives


$$
v_3\binom{10Q}{uQ+r}
=v_3(Q)-v_3(r)+v_3\binom9u.
\tag{7.6}
$$


When $4Q<j<9Q$, one has $u=4,\ldots,8$. The minimum value of $v_3\binom9u$ in this range is $1$, and $v_3(Q)-v_3(r)\ge1$. Thus every nonmultiple of $Q$ in this interval is zero modulo $9$.

At multiples of $Q$,


$$
\binom{10Q}{uQ}\equiv\binom{10}{u}\pmod9.
\tag{7.7}
$$


Here is the exact unit-stripping justification. Write


$$
(3a)!=3^aa!\prod_{\substack{1\le v\le3a\\3\nmid v}}v.
$$


The product of the two units in each block satisfies


$$
(3r-2)(3r-1)=9r(r-1)+2\equiv2\pmod9.
$$


The unit quotient in


$$
\frac{\binom{3a}{3b}}{\binom ab}
$$


is therefore $1\pmod9$. Iterating proves (7.7), including cases where the binomial coefficient itself is divisible by $3$.

It follows that in the open interval $4Q<j<9Q$, the only nonzero $c_j$ modulo $9$ are


$$
\boxed{c_{6Q}\equiv3,\qquad c_{7Q}\equiv-3\pmod9.}
\tag{7.8}
$$


Also


$$
\boxed{x^{10Q}\equiv y^{10Q}-y^{9Q}-y^Q+1\pmod3.}
\tag{7.9}
$$



### 7.4 The entire $\Omega_0$-tail coefficient cancels modulo $9$

Using


$$
s_0=\sum_{\ell=0}^{\nu}g_\ell y^{\nu-\ell},
$$


the four channels in $[y^{n_*}]C_0$ are as follows:

| Part of $O_a$ | Factor from $\beta+3y$ | Required index $j$ | Lower bound on $\ell$ | Multiplier |
|---|---|---|---|---|
| high | $\beta$ | $4Q+t+\ell$ | $\ell\ge1$ | $\beta$ |
| high | $3y$ | $4Q+t-1+\ell$ | $\ell\ge2$ | $3$ |
| low | $\beta$ | $7Q+t+\ell$ | $\ell\ge1$ | $3\beta$ |
| low | $3y$ | $7Q+t-1+\ell$ | $\ell\ge2$ | $9$ |

The last channel is zero modulo $9$, with its factor retained explicitly. Thus


$$
\begin{aligned}
[y^{n_*}]C_0\equiv{}&
\beta\sum_{\ell=1}^{\nu}g_\ell c_{4Q+t+\ell}\\
&+3\sum_{\ell=2}^{\nu}g_\ell c_{4Q+t-1+\ell}\\
&+3\beta\sum_{\ell=1}^{\nu}g_\ell c_{7Q+t+\ell}
\pmod9.
\end{aligned}
\tag{7.10}
$$



The upper index of the first sum is exactly


$$
4Q+t+\nu=9Q-a-1<9Q.
$$


By (7.8), that sum is


$$
3\beta(g_{2Q-t}-g_{3Q-t})\pmod9.
\tag{7.11}
$$



The second sum has indices strictly between $4Q$ and $9Q$; its largest index is $9Q-a-2$. None is a nonzero position in (7.9), so the factor $3$ makes the whole sum zero modulo $9$.

In the third sum, (7.9) leaves precisely the positions $9Q$ and $10Q$, giving


$$
3\beta(-g_{2Q-t}+g_{3Q-t})\pmod9.
\tag{7.12}
$$


The required indices are inside the actual finite quotient:


$$
1\le2Q-t<3Q-t\le\nu,
$$


since, for example,


$$
\nu-(3Q-t)=2Q-a-1>0.
$$



Equations (7.11) and (7.12) cancel exactly. Therefore


$$
\boxed{\mathcal P(\Omega_0,O_a)\in9\mathbb Z_3.}
\tag{7.13}
$$



No coefficient of $s_0$ was replaced by an infinite-series surrogate; its finite range was used in the cancellation.

### 7.5 The $\Omega_1$-tail coefficient modulo $3$

Modulo $3$, (7.1) and (7.9) give


$$
O_a\equiv
-y^{m+5Q-t}+y^{m+6Q-t}.
$$


The smaller of these exponents already exceeds $n_*=m+\nu$, because


$$
5Q-t-\nu=a+1>0.
$$


Multiplication by the polynomial $(\beta+3y)s_1$ cannot lower the exponent. Hence


$$
[y^{n_*}]C_1\equiv0\pmod3,
$$


and (7.4) gives


$$
\boxed{\mathcal P(\Omega_1,O_a)\in3\mathbb Z_3.}
\tag{7.14}
$$



### 7.6 Return through the actual terminal inverse row

Apply the actual dual formula (3.11). Equations (7.13) and (7.14) imply


$$
\mathcal P(\mathscr D,O_a)\in9\mathbb Z_3.
\tag{7.15}
$$


The error in (3.11) lies in $9W\mathbb Z_3$. Its pairing with $O_a$ is still in $9\mathbb Z_3$, because the original truncated functional is integral. This does not require an untruncated integral representation for $\mathcal P(W,O_a)$.

Using $v_3(r_M)=26$,


$$
\boxed{
r_M\,e_{Y_m}^TE_{\mathcal P}^{-1}\mathcal P(W,O_a)
=r_M\mathcal P(\mathscr D,O_a)
\in3^{28}\mathbb Z_3.
}
\tag{7.16}
$$



This is the full paid return of the removed physical overflow.

---

## 8. Independent derivation of the terminal amplitude

### 8.1 Exact projection using the admissible trial

By (4.5), the actual pole correction of $\Psi_a$ is exactly


$$
\mathcal F_{\mathcal P,a}
=
\widehat V_a-WE_{\mathcal P}^{-1}\mathcal P(W,\widehat V_a).
$$


Taking the physical coefficient and using $\widehat V_a=V_a-r_MO_a$,


$$
[y^m]\mathcal F_{\mathcal P,a}
=
[y^m]\widehat V_a
-\mathcal P(\mathscr D,V_a)
+r_M\mathcal P(\mathscr D,O_a).
\tag{8.1}
$$



The sign of the overflow return is positive in (8.1).

By (3.11),


$$
\mathcal P(\mathscr D,V_a)
\equiv
\frac{\mathcal P(\Omega_0,V_a)}
{\beta\mathfrak t_{25}}
-\frac{3\mathcal P(\Omega_1,V_a)}
{\beta^2\mathfrak t_{25}}
\pmod{3^{29}},
$$


where the error uses $\mathcal P(W,V_a)\in3^{27}$ and the dual-row error in $9W$.

The first term is in $3^{28}$ by (6.1). The second is in $3^{28}$ because $\Omega_1\in W\mathbb Z_3$ and the full virtual residual is in $3^{27}$. The overflow term is in $3^{28}$ by (7.16). Thus


$$
\boxed{
[y^m]\mathcal F_{\mathcal P,a}
\equiv[y^m]\widehat V_a\pmod{3^{28}}.
}
\tag{8.2}
$$



This is a statement about the evaluated physical row. The general residual of $\widehat V_a$ has only the $3^{26}$ guarantee, and a general inverse application may lose a digit.

### 8.2 The exact terminal binomial factor

Only the top filter term contributes to $y^m$, so


$$
[y^m]\widehat V_a
=r_M(c_{4Q+t}+3c_{7Q+t}).
\tag{8.3}
$$



For $t>0$,


$$
t\le b/2<\frac{73}{2000}Q<\frac Q{27}.
$$


Writing $Q=3^q$, this implies $q-v_3(t)\ge4$. The valuation formula (7.6), with $u=4,7$, then gives


$$
v_3\binom{10Q}{4Q+t}\ge6,\qquad
v_3\binom{10Q}{7Q+t}\ge6.
\tag{8.4}
$$



For $t=0$, binomial stripping and the signs in (7.5) give


$$
c_{4Q}\equiv\binom{10}{4}=210\equiv3\pmod9,
$$




$$
c_{7Q}\equiv-\binom{10}{7}=-120\equiv-3\pmod9.
$$


Therefore


$$
\boxed{
c_{4Q+t}+3c_{7Q+t}\equiv3\delta_{t,0}\pmod9.
}
\tag{8.5}
$$



The stronger valuation in (8.4) belongs to the trial coefficient. The returned correction has only been controlled modulo $3^{28}$, so no stronger claim for the actual off-terminal columns is inferred.

### 8.3 The leading unit of the top filter coefficient

Use (3.13) with $p=26$, $N=3^{25}$, $M=(N-1)/2$. Modulo $3$, the product is $1$. Moreover,


$$
M\equiv1\pmod3,\qquad M\ \text{is odd},
$$




$$
2^{2M-1}\equiv-1\pmod3,
$$


and Lucas’ theorem gives


$$
\binom{2M}{M}
=\binom{3^{25}-1}{(3^{25}-1)/2}
\equiv(-1)^{25}=-1\pmod3.
$$


Thus


$$
\boxed{\frac{r_M}{3^{26}}\equiv-1\pmod3.}
\tag{8.6}
$$



Combining (8.2), (8.3), (8.5), and (8.6),


$$
[y^m]\mathcal F_{\mathcal P,a}
\equiv-3^{27}\delta_{t,0}
=-3^{27}\delta_{a,b/2}
\pmod{3^{28}}.
\tag{8.7}
$$



### 8.4 Transfer to the complete core

The coefficients of $p_a$ are integral, and $\deg p_a\le\nu-3$. Therefore the established original-column comparison extends to this actual linear combination without any additional division:


$$
\mathcal F_{\mathcal P,a}-\mathcal F_a
\in3^{h-1}W\mathbb Z_3.
$$


Since $h-1\ge28$ on the sufficiently large original family, (8.7) proves:

> **Audited original-index theorem.**
> 

$$
> \boxed{
> [y^m]\mathcal F_a
> \equiv-3^{27}\delta_{a,b/2}\pmod{3^{28}}.
> }
> \tag{8.8}
>
$$


> In particular,
> 

$$
> v_3([y^m]\mathcal F_{b/2})=27,
> \qquad
> [y^m]\mathcal F_a\in3^{28}\mathbb Z_3\quad(a<b/2).
>
$$



The physical terminal has not been set to zero. Its last prescribed amplitude is provably nonzero.

---

## 9. The coupling and contracted $J$-return consequences

### 9.1 Evaluation of $\gamma_c$

Substitution of (8.8) into the closed normalized identity (1.4) gives


$$
(\gamma_c)_a
=-\delta_{a,b/2}-(-\delta_{a,b/2})=0
\quad\text{in }\mathbb F_3.
$$


Therefore


$$
\boxed{\gamma_c=0.}
\tag{9.1}
$$



This vanishing is a cancellation between the boundary delta term and a nonzero physical-terminal amplitude. It is not a consequence of suppressing $Y_m$.

### 9.2 Contracted first-radical returns

In the retained residual notation, let


$$
\ell=\frac{3b}{2}+1,\qquad K=\{0,\ldots,\ell-1\},
$$


and let $G$ have columns given by the coefficients of


$$
x^by^a,\qquad 0\le a\le b/2,
$$


in these $K$-coordinates.

The closed nonterminal strip gives


$$
G^T\bar L_c=\gamma_c\delta_J^T.
$$


The terminal bootstrap gives $\bar t_K=\bar t_J=0$, and the retained producer comparison gives


$$
\bar L_{\rm act}=\bar L_c.
$$


Thus


$$
\boxed{G^T\bar L_c=G^T\bar L_{\rm act}=0.}
\tag{9.2}
$$



In the normalization $\mathcal R_{\alpha,JJ}=3B_\alpha$, the matrices $B_\alpha^{-1}$ are integral. Each contracted coupling in


$$
27G^TL_\alpha B_\alpha^{-1}L_\alpha^TG
$$


now has a factor $3$. Consequently


$$
\boxed{
27G^TL_\alpha B_\alpha^{-1}L_\alpha^TG
\in3^5\operatorname{Mat}(\mathbb Z_3),
\qquad \alpha=c,\mathrm{act}.
}
\tag{9.3}
$$


The associated finite displacement satisfies


$$
\boxed{
3B_\alpha^{-1}L_\alpha^TG\in9\operatorname{Mat}(\mathbb Z_3).
}
\tag{9.4}
$$


The closed endpoint-return identity correspondingly reduces to


$$
\boxed{
G^Tf_\alpha^{(2)}
\equiv G^Tf_{\alpha,K}\pmod9.
}
\tag{9.5}
$$



These consequences are valid at the first $J$-return stage. They do not justify deleting the exact return formulas or propagating a congruence through a later $1/9$ division without further work.

### 9.3 One additional evaluated consequence

The prescribed endpoint-annihilating inputs are


$$
\Psi_a+\Psi_{a+1}
=(y+1)x^{10Q}y^{k_0+a}(y^{3Q}+3),
\qquad 0\le a<b/2.
$$


By linearity of the actual correction,


$$
\boxed{
[y^m](\mathcal F_a+\mathcal F_{a+1})
\equiv-3^{27}\delta_{a,b/2-1}\pmod{3^{28}}.
}
\tag{9.6}
$$


Thus even in these prescribed endpoint-annihilating combinations, the last physical coefficient survives at valuation $27$. This corollary concerns the stated corrected inputs only, not the subsequently fully returned endpoint-adapted operator.

---

## 10. Complete forcing and returns that remain present

The successful coefficient audit does not alter the producer:


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


The original signed $\xi$ and its paid normalization remain intact, as do


$$
\mathscr R(-1)
=-\frac{\xi((A+1)!)^2}{3^7},
$$


and


$$
J^T\varepsilon+\omega
=-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$



The exact first-radical returns are still


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
\tag{10.1}
$$


Their inverse payment remains $3^{-1}$.

The second prefix lift also remains:


$$
-\frac{G_c(\mathcal F,\mathcal F)}{3^{26}}
=
G^T\mathcal R_{c,KK}G+81Z^T\mathsf AZ.
\tag{10.2}
$$


Combining the closed whole pairing in $3^{30}$ with (9.3) yields the correctly paid localization


$$
\boxed{
\frac{G^T\mathcal S_c^{(2)}G}{81}
\equiv
-\frac{G_c(\mathcal F,\mathcal F)}{3^{30}}
-Z^T\mathsf AZ
\pmod3.
}
\tag{10.3}
$$


The right side is not evaluated by the present audit. In particular, $Z^T\mathsf AZ$ is not removed.

The rank-$b$ returns remain


$$
T_{\rm new}=T_{RR}-81M_b^TA_b^{-1}M_b,
$$




$$
f_{\rm new}=f_R-3M_b^TA_b^{-1}f_b,
$$




$$
\lambda_{\rm new}
=\lambda^{(2)}-\frac19f_b^TA_b^{-1}f_b.
\tag{10.4}
$$


Their inverse payment remains $3^{-2}$.

Thus the next operator still requires the complete second prefix, producer, rank-$b$, endpoint, and diagonal evaluations. The coefficient theorem does not turn it into a core-only object.

The complete factorial channel is likewise retained. For $\mu_t=\mathcal M(y^t)$,


$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\qquad0\le t\le2n-2.
$$


Nothing proved here removes the previously retained forward $3^h$ division or replaces the whole complete determinant by a pole determinant. Its relevant highest moment remains physical because $H-4D+5\ge0$.

---

## 11. The exact remaining local and global bottlenecks

### 11.1 The fully returned directional problem

After all retained returns and actual endpoint adaptation, the closed result is


$$
T=\begin{pmatrix}a&z^T\\z&C\end{pmatrix}\in81\operatorname{Mat}(\mathbb Z_3),
\qquad \lambda=\eta/3,\quad \eta\in\mathbb Z_3^\times.
$$


Write


$$
a=81\alpha,\qquad z=81w,\qquad C=81B,
$$


and


$$
u=1-\lambda a=1-27\eta\alpha\in1+27\mathbb Z_3.
$$


The paid two-coordinate elimination gives


$$
C^\sharp=81B^\sharp,\qquad
\boxed{
B^\sharp=B+\frac{27\eta}{u}ww^T.
}
\tag{11.1}
$$



The concrete remaining local obligation is:

> **Fully returned directional lemma, still open.**  
> On the same infinite original subwindow, with every contribution in (10.1)–(10.4) retained, prove that the actual $B^\sharp$ is nonsingular and solve
> 

$$
> B^\sharp v=w,\qquad
> v\in3^{-1}\mathbb Z_3^{\,b/2}.
> \tag{11.2}
>
$$



Its conditional implication is rigorous. If (11.2) holds, then


$$
\epsilon=1-\frac{27\eta}{u}w^Tv\in1+9\mathbb Z_3,
$$


and


$$
B^{-1}w=v/\epsilon\in3^{-1}\mathbb Z_3^{\,b/2}.
$$


Thus, if the resulting Schur scalar is nonzero, the local relative ternary gain is at least $3$; an integral directional solution would give at least $4$.

These are fixed gains. Neither the existence of the directional solution nor a growing gain follows from $T\in81M$ alone.

### 11.2 Actual contents, least clearer, all-prime gcd, and whole error

No new global content division has been made. The local rational certificates $R_N$, $\mathfrak t_{25}^{-1}$, and $\beta^{-1}$ do not replace the actual original column contents or the actual least simultaneous clearer $\ell_{\rm clr}$.

Retain the distinguished integers


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the gcd over **all primes**


$$
\boxed{g_\ell=\gcd(|A_\ell|,|B_\ell|).}
$$


For $B_\ell\ne0$, the actual primitive numerator and denominator are


$$
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
\qquad
q=\frac{|B_\ell|}{g_\ell}.
$$


The whole evaluated error is


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{11.3}
$$



An irrationality proof still requires, at the same infinite original indices,


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
\tag{11.4}
$$


Under these conditions, the nonzero whole errors in (11.3) tend to zero, contradicting rationality. None of these global growth or nonvanishing obligations is established by the fixed-digit coefficient theorem.

---

## 12. Division and boundary ledger

| Step | Exact payment or boundary |
|---|---|
| Original pole functional | Cutoff $K_{\rm phys}=2H-2D+2$; largest denominator $4H-4D+5$ |
| $\Omega_k/x^D$ | Exact polynomial division; finite quotient through $\nu+k$ |
| Filtered $\Omega_k$ | Actual $W$; degree strictly below $m$ |
| Exceptional $p=25$ moment | Full denominator range ends at $4H-81Q$ |
| Dual normalization | Only unit divisions by $\beta\mathfrak t_{25}$ |
| Three-column certificate | Residual $3^3$, then inverse loss $3^{-1}$, giving row error $3^2$ |
| $p=26$ virtual residual | Full LOW/HIGH residual in $3^{27}$, with Frobenius error included |
| Completed $p=26$ moments | Largest denominator $4H-81Q$, still physical |
| Collision $2s+1=27Q$ | Exact finite $q=0$ moment, evaluated as zero |
| $9Q$ layer | $3^{27}$ times a sum zero modulo $3$ |
| Frobenius coefficient | Evaluated at $n_*=(H-1)/2$; the finite coefficient is zero modulo $3$ |
| Physical overflow | Removed only from the top filter term; $v_3(r_M)=26$ |
| Overflow return | Actual terminal contraction in $9$, hence returned term in $3^{28}$ |
| General trial projection | Possible $26\to25$ loss retained |
| Physical coefficient | Separately evaluated through $3^{28}$ |
| Pole-to-core transfer | Error $3^{h-1}$, sufficient for modulus $3^{28}$ |
| $\gamma_c$ normalization | Whole physical coefficient divided by $3^{27}$ |
| First $J$-inverse | $3^{-1}$; contracted matrix return now in $3^5M$ |
| Rank-$b$ inverse | $3^{-2}$, unchanged |
| Global content and clearer | No alteration or new division |

---

## 13. Bounded exact-arithmetic receipt

No new numerical computation is required to complete the analytic audit above. No tool-assisted calculation was performed.

If the coordinator wishes to record a small independent arithmetic receipt, it can be confined to the constants used in the overflow calculation.

### Inputs

- the polynomial $(Z-1)^{10}$;
- the integers $0,\ldots,10$;
- moduli $9$ and $3$.

### Expected verifiable outputs

In increasing degree,


$$
(1,-10,45,-120,210,-252,210,-120,45,-10,1),
$$


and modulo $9$,


$$
\boxed{(1,8,0,6,3,0,3,6,0,8,1).}
$$


Modulo $3$,


$$
\boxed{(Z-1)^{10}=Z^{10}-Z^9-Z+1.}
$$



The scaling from these constants to $Q=3^{h-29}$ is not inferred from a finite experiment. It is proved by the unit-stripping identity in §7.3 together with the closed nonmultiple-$Q$ valuation formula.

This finite receipt certifies only these fixed polynomial constants. It does not certify an original ternary index, an inverse bound, the existence of infinitely many indices, a final gcd, or whole-error decay.

---

## 14. Proof status and conclusion

| Statement | Status after this audit |
|---|---|
| Actual finite-$W$ terminal dual modulo $9$ | Independently proved |
| Optional normalization $\mathfrak t_{25}\equiv7\pmod9$ | Verified; not essential |
| Full $p=26$ virtual residual in $3^{27}$ | Independently proved with original cutoff |
| $27Q$ collision and $9Q$ layer | Explicitly evaluated |
| Finite Frobenius coefficient at $(H-1)/2$ | Explicitly evaluated as zero modulo $3$ |
| Physical overflow and its inverse return | Explicitly retained and evaluated |
| Terminal coefficient modulo $3^{28}$ | Verified: $-3^{27}\delta_{a,b/2}$ |
| $\gamma_c$ | Verified: $0$ |
| Contracted first $J$-matrix return | Verified in $3^5M$ |
| Complete next prefix/producer/rank-$b$/endpoint/diagonal evaluation | Open |
| Fully returned directional solve | Open |
| Growing relative-cofactor saving | Open |
| Actual all-prime primitive whole-error decay | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

### Final assessment

There is no mathematical gap in the new coefficient argument identified by this audit. Its decisive features are valid only because they are handled together:

1. the dual is constructed inside the actual finite $W$;
2. the exceptional physical moment is retained;
3. the inverse’s one-digit loss is paid before reducing the dual modulo $9$;
4. the $p=26$ collision is evaluated exactly;
5. the finite Frobenius coefficient is checked at its actual index;
6. the overflow above $Y_m$ is removed and its returned correction is evaluated.

The resulting new original-index statement is


$$
\boxed{
[y^m]\mathcal F_a
\equiv-3^{27}\delta_{a,b/2}\pmod{3^{28}},
\qquad \gamma_c=0.
}
$$



The exact next local bottleneck is the fully returned directional problem (11.2), after the complete second prefix, producer, rank-$b$, endpoint, and diagonal terms have been evaluated and retained. Beyond it remains the essential same-index growth comparison (11.4), involving the actual least clearer, all-prime final gcd, actual primitive denominator, and nonzero whole complete error.

Accordingly,


$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ is obtained.}}
$$


