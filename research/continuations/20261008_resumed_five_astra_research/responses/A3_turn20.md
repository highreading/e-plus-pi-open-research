> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3 Turn 20 — Full audit of the higher ternary block theorem and its original-family consequences

## Executive verdict

The full higher-precision finite block theorem in A4 Turn 14 **passes** this audit. Its proof works for every finite matrix size, not merely for the first coefficient or for the original sizes modulo $243$. In particular, it applies simultaneously to the literal finite matrices


$$
T_{n-1},\qquad T_n,\qquad T_{n+1},
$$


with their different, actual terminal boundaries.

The decisive assertions are


$$
\widehat T_d
\equiv
\operatorname{diag}
\bigl(\widehat T_{3^E},\ldots,\widehat T_{3^E},
\widehat T_{d\bmod 3^E}\bigr)
\pmod{3^E},
$$


and the corresponding assertion for the inverse. The latter follows from the former by a paid finite inverse identity; it is not an assumed periodicity of inverses.

Consequently, the higher-block dependency left explicit in the independently passed LOCAL and weighted-period audit of A4 Turn 17 is now discharged. There is **no additional loss of precision** in its $E33$ conclusion:



$$
\boxed{
\begin{gathered}
j=84645+3^{32}s,\qquad s\ge0,\\
(q_{n-72},\ldots,q_{n-1})\pmod{3^{32}}
\quad\text{and}\quad
V_{70}\pmod{3^{32}}
\end{gathered}
}
$$


are constant when the coefficients are compared at their corresponding terminal offsets. The physical exponents, columns, matrices, and returns are not thereby frozen.

The uniform scalar conclusions in Turn 14 also pass, by the symbolic derivation below:


$$
\boxed{
\Xi\equiv120\pmod{243},\qquad
\chi_{\rm prod}:=u^T\mathbf t\equiv-168\pmod{729},\qquad
\xi\equiv31\pmod{81}.
}
$$


These conclusions do not rely on treating the cached scalar receipts as a uniform theorem.

Two minor presentational repairs are appropriate:

* In the $617$-coordinate window argument, the minimum coordinate distance is $420$, not $421$. The latter counts positions inclusively. Since $420>418$, the mathematical conclusion is unchanged.
* The retained index $(3^h-5)/2$ is not a denominator pole of the displayed recurrence with denominator $2t+1$. Its separate designated role must not be confused with such a pole.

Neither repair affects the higher block law.

The complete physical-seventh correction remains unevaluated. The core $\eta _0$ theorem from Turn 19 remains an established parent-reviewed result at its separate core scope; it is not transported here to the actual producer or relabelled as a different-passed theorem.

No new arithmetic execution is needed for the present audit.

---

## 1. Scope, original indices, and established inputs

Throughout, $v_3(0)=+\infty$. Integrality without further qualification means integrality over $\mathbb Z_3$.

The original family is retained:


$$
j>0,\qquad j\equiv84645\pmod{3^{12}},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad
N=n-1=4^j,\qquad A=n-2=N-1.
$$


The physical parameters remain


$$
H=3^{h-1},\qquad D=H-A,
$$




$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15},
$$


and


$$
P=3^{h-32},\qquad P_0=243P,\qquad
N_0=243r,\qquad D=P_0+N_0,
$$


with


$$
r\equiv2\pmod9,\qquad r\ \text{odd}.
$$


The exact size relation is


$$
N=243(3^{26}-1)P-243r+1.
$$



To avoid a collision of notation, write


$$
\chi_{\rm range}=P-R,\qquad c=2\chi_{\rm range},
$$


where


$$
Q=27P,\qquad Q-N_0=2R.
$$


Thus


$$
N_0=25P+c,\qquad D=268P+c.
$$



The additional retained Range III condition, where required for the physical application, is


$$
\frac3{25}<\frac{\chi_{\rm range}}P<\frac{31}{250}.
$$


It is not a condition on $\chi_{\rm prod}=u^T\mathbf t$.

Since


$$
84645=3^4\cdot1045,\qquad 3\nmid1045,
$$


every original $j$ has $v_3(j)=4$. LTE therefore gives


$$
\boxed{v_3(N-1)=v_3(4^j-1)=5.}
\tag{1.1}
$$


In particular,


$$
N\equiv1\pmod{243},\qquad n\equiv2\pmod{243}.
$$



### Established results reused at their stated scope

The following are not reopened:

1. The independently passed LOCAL theorem and the checked weighted-period deduction in A4 Turn 17, with their previously explicit higher-block dependency.
2. The original physical inverse allowances
   

$$
E_c^{-1},E_{\rm act}^{-1}\in3^{-1}\operatorname{Mat}(\mathbb Z_3).
$$


3. The passed finite prefix comparison and normalization results used in the physical correction.
4. The established nine leading inverse-image bands.
5. The original density argument on the retained arithmetic progressions.
6. The separately passed A1 Turn 18 annihilator and A1 Turn 13 prefix/bare interface audits.
7. The parent-reviewed Turn 19 core $\eta _0$ result, only at its own core scope.

The proof below independently audits the higher finite block theorem and all producer-level deductions in Turn 14. It does not repeat an old matrix solve, compatibility scan, or LOW-return calculation.

---

# Part I. Literal finite gamma objects and all coefficient payments

## 2. The three finite matrices and their gamma ranges

For every finite size $d\ge1$, define


$$
T_d[a,b]=\binom{a+b}{a}\gamma_{a+b},
\qquad 0\le a,b<d,
$$


where


$$
\gamma_0=1,\qquad \gamma_1=0,\qquad
\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1}.
$$


Let


$$
P_d[a,b]=\binom ab,\qquad
\widehat T_d=P_d^{-1}T_dP_d^{-T}.
$$



The exact gamma ranges are:

| Finite object | Row/column range | Largest gamma index |
|---|---|---:|
| $T_{n-1}=T_N$ | $0,\ldots,n-2$ | $2n-4=2N-2$ |
| $T_n$ | $0,\ldots,n-1$ | $2n-2=2N$ |
| Full $T_{n+1}$ | $0,\ldots,n$ | $2n$ |
| Actual next column used by the $n$-solve | $a=0,\ldots,n-1,\ b=n$ | $2n-1$ |

No one of these matrices is substituted for another.

### 2.1 Finite divided gamma jets

It is important to distinguish the ordinary and divided jets:


$$
\Gamma_K(z)=\sum_{r=0}^K\gamma_r z^r,\qquad
F_K(z)=\sum_{r=0}^K\gamma_r\frac{z^r}{r!}.
$$


For $K\ge a+b$,


$$
T_d[a,b]
=[X^aY^b]\Gamma_K(X+Y)
=(a+b)!\,[X^aY^b]F_K(X+Y).
\tag{2.1}
$$


Thus the coefficient of the divided jet by itself is
$\gamma_{a+b}/(a!b!)$, not $T_d[a,b]$.

Equivalently,


$$
T_d[a,b]
=\frac1{a!\,b!}
\left.\frac{d^{a+b}}{dz^{a+b}}\Gamma_K(z)\right|_{z=0}.
$$


The factorial cancellation is exact and yields the integer binomial coefficient. It is not a modular division by a nonunit factorial.

The finite differential boundary is also explicit. For $K\ge2$,


$$
\begin{aligned}
(1-4z)F_K''-6F_K'-4F_K
={}&-\frac{(4K+2)\gamma_K+4\gamma_{K-1}}{(K-1)!}z^{K-1}\\
&-\frac{4\gamma_K}{K!}z^K.
\end{aligned}
\tag{2.2}
$$


Therefore the homogeneous differential equation is valid for the finite jet only through degree $K-2$. It must not be imposed past that boundary. The formal infinite generating-function calculation in Turn 17 is compatible with this identity, but no infinite inverse is involved here.

---

## 3. Audit of the explicit gamma formula

Define


$$
B_r(z)=
\sum_{k=0}^r
\frac{(r+k)!}{(r-k)!\,k!}\left(\frac z2\right)^k.
$$


For $r\ge1$,


$$
B_{r+1}(z)=(2r+1)zB_r(z)+B_{r-1}(z).
\tag{3.1}
$$



For $k\ge1$, clearing the displayed factorial factors reduces the coefficient identity to


$$
(r+k)(r+k+1)
=(r-k)(r-k+1)+2k(2r+1).
$$


The constant coefficient and the endpoint coefficients agree, with out-of-range coefficients zero.

Now $B_0=1$, $B_1=1+z$. Hence


$$
(-2)^rB_r(-1)
$$


has initial values $1,0$ and satisfies the given gamma recurrence. Consequently


$$
\boxed{
\gamma_r=(-2)^r
\sum_{k=0}^r A_k\binom{r+k}{2k},
\qquad
A_k=(-1)^k\frac{(2k)!}{2^k k!}.
}
\tag{3.2}
$$


Here


$$
A_k=(-1)^k(2k-1)!!
$$


is an integer. The factorial division in (3.2) has therefore been paid exactly.

**Verdict: PASS.**

---

## 4. Every-degree Newton bounds

Write the finite Newton expansion


$$
\gamma_r=\sum_{\ell=0}^r c_\ell\binom r\ell,
\qquad
c_\ell=\sum_{a=0}^{\ell}(-1)^{\ell-a}\binom{\ell}{a}\gamma_a.
\tag{4.1}
$$


There is no division by $\ell!$ in this definition.

### 4.1 Bounds for $A_k$

For $k\ge1$,


$$
v_3(A_k)=v_3((2k)!)-v_3(k!).
$$


Let $q$ be the largest power of $3$ not exceeding $2k$.

* If $q>k$, the interval $(k,2k]$ contains $q$.
* If $q\le k$, it contains $2q$, since $q>2k/3$.

Therefore


$$
v_3(A_k)\ge\lfloor\log_3(2k)\rfloor.
\tag{4.2}
$$


The same interval contains at least $\lfloor k/3\rfloor$ multiples of $3$, giving


$$
v_3(A_k)\ge\lfloor k/3\rfloor.
\tag{4.3}
$$



By Vandermonde,


$$
\binom{r+k}{2k}
=\sum_{t=k}^{2k}\binom rt\binom k{2k-t}.
$$


If


$$
B_r(-1)=\sum_{t=0}^r d_t\binom rt,
$$


then


$$
d_t=\sum_{k=\lceil t/2\rceil}^{t}
A_k\binom k{2k-t}.
$$


Thus


$$
v_3(d_t)\ge\lfloor\log_3t\rfloor\quad(t\ge1),
\qquad
v_3(d_t)\ge\lfloor t/6\rfloor.
\tag{4.4}
$$



### 4.2 Multiplication by $(-2)^r$

Use


$$
(-2)^r=(1-3)^r=\sum_{h=0}^r(-3)^h\binom rh
$$


and the exact integer identity


$$
\binom rh\binom rt
=
\sum_{\ell=\max(h,t)}^{h+t}
\frac{\ell!}
{(\ell-h)!(\ell-t)!(h+t-\ell)!}
\binom r\ell.
\tag{4.5}
$$



For $h,t\ge1$, a contribution to $c_\ell$ has valuation at least


$$
h+\lfloor\log_3t\rfloor.
$$


Since


$$
3^h t\ge h+t\ge\ell,
$$


this is at least $\lfloor\log_3\ell\rfloor$. If $h=0$, then $t=\ell$; if $t=0$, then $h=\ell$. Those cases satisfy the same bound.

Likewise,


$$
h+\lfloor t/6\rfloor
\ge\lfloor(h+t)/6\rfloor
\ge\lfloor\ell/6\rfloor.
$$


Therefore


$$
\boxed{
v_3(c_\ell)\ge\lfloor\log_3\ell\rfloor\quad(\ell\ge1),
\qquad
v_3(c_\ell)\ge\lfloor\ell/6\rfloor\quad(\ell\ge0).
}
\tag{4.6}
$$



These are all-degree theorems, not consequences of a checked finite list.

They imply, respectively,

* modulo $3^E$, only $\ell<3^E$ can contribute;
* modulo $3^M$, only $\ell\le6M-1$ can contribute.

**Verdict: PASS, including both coefficient floors.**

---

## 5. Exact finite Pascal conjugation, every entry, and the full bivariate kernel

For $r\ge0$, set


$$
D_r=\operatorname{diag}\left(\binom ar\right)_{a=0}^{d-1},
\qquad C_r=P_d^{-1}D_rP_d.
$$


A literal finite calculation gives


$$
\begin{aligned}
(C_r)_{a,i}
&=\sum_{b=i}^a(-1)^{a-b}\binom ab\binom br\binom bi\\
&=\binom ai\binom i{r-a+i}\\
&=\boxed{\binom ar\binom r{a-i}}.
\end{aligned}
\tag{5.1}
$$



All indices are in $0,\ldots,d-1$. In particular, $C_r=0$ for $r\ge d$.

Since


$$
\left(\binom{a+b}{a}\right)_{a,b=0}^{d-1}=P_dP_d^T,
$$


the exact finite matrix identity is


$$
\boxed{
\widehat T_d
=\sum_{\ell=0}^{2d-2}c_\ell
\sum_{\substack{r+s=\ell\\0\le r,s<d}}C_rC_s^T.
}
\tag{5.2}
$$


No row or column outside the finite matrix occurs.

The entry form is


$$
\boxed{
\widehat T_d[a,b]
=
\sum_{\ell=0}^{a+b}c_\ell
\sum_{r=0}^{\ell}
\binom ar\binom b{\ell-r}
\binom{\ell}{r+b-a}.
}
\tag{5.3}
$$


The nonzero inner range is contained in


$$
\max(0,\ell-b,a-b)
\le r\le
\min(\ell,a,\ell+a-b).
\tag{5.4}
$$


Using the zero convention outside the binomial ranges is equivalent to these explicit bounds.

To check the finite product, one uses


$$
\sum_i\binom r{a-i}\binom s{b-i}
=\binom{r+s}{r+b-a}.
$$


The factors $\binom ar,\binom bs$ guarantee that all admitted terms have $i\ge0$, while lower triangularity gives $i\le\min(a,b)$. No hidden negative index is used.

### 5.1 Full bivariate identity

Let $G(z)=\sum_{\ell\ge0}c_\ell z^\ell$. Applying the two inverse Pascal transforms gives, coefficientwise,


$$
\boxed{
\sum_{a,b\ge0}\widehat T[a,b]X^aY^b
=
\sum_{\ell\ge0}
c_\ell\frac{(X+Y+2XY)^\ell}{(1-XY)^{\ell+1}}.
}
\tag{5.5}
$$


For the finite matrix $T_d$, this identity is read modulo the ideal
$(X^d,Y^d)$. Only gamma indices through $2d-2$, and only
$\ell\le2d-2$, are then relevant.

Expanding the entire numerator and denominator gives


$$
\boxed{
\widehat T[a,b]
=
\sum_{\ell=0}^{a+b}c_\ell
\sum_{\substack{p,q,c\ge0\\p+q+c=\ell\\p-q=a-b}}
\frac{\ell!}{p!\,q!\,c!}\,2^c
\binom{a+q}{\ell}.
}
\tag{5.6}
$$


The condition $a+q\ge\ell$ is exactly the condition that the denominator expansion contributes a nonnegative power of $XY$.

Thus the full bivariate kernel—not merely its first nontrivial coefficient—is accounted for. In particular,


$$
\ell\ge |a-b|
$$


in every contribution, so


$$
\boxed{
v_3(\widehat T[a,b])\ge\lfloor |a-b|/6\rfloor.
}
\tag{5.7}
$$



**Verdict: PASS, with all finite ranges and the whole bivariate expression retained.**

---

## 6. Continuity, derivatives, and divided differences: the exact bill

For integers $z,t$, $E\ge1$, and $1\le r<3^E$,


$$
\binom{z+3^Et}{r}-\binom zr
=
\sum_{i=1}^r\binom{3^Et}{i}\binom z{r-i}.
$$


Because


$$
\binom{3^Et}{i}
=\frac{3^Et}{i}\binom{3^Et-1}{i-1},
$$


all terms are integral and


$$
\boxed{
\binom{z+3^Et}{r}-\binom zr
\in3^{E-\lfloor\log_3r\rfloor}\mathbb Z.
}
\tag{6.1}
$$


For $r=0$, the difference is exactly zero.

This is the precise divided-difference cost. Dividing the difference by $3^E$ can lose as many as $\lfloor\log_3r\rfloor$ ternary digits.

A derivative formulation confirms that no higher coefficient is being overlooked. For $i\ge1$,


$$
\binom hi
=\frac{(-1)^{i-1}h}{i}
\prod_{j=1}^{i-1}\left(1-\frac hj\right).
$$


Hence, for $k\ge1$,


$$
v_3\!\left([h^k]\binom hi\right)
\ge-k\lfloor\log_3i\rfloor.
$$


Using Vandermonde as a polynomial identity in $h$, for integer $z$,


$$
\boxed{
v_3\!\left(\frac1{k!}\frac{d^k}{dz^k}\binom zr\right)
\ge-k\lfloor\log_3r\rfloor.
}
\tag{6.2}
$$


The left side is the divided derivative; the $k!$ payment is already included.

For a fixed displacement $b-a$, a summand in (5.3) is a polynomial of total degree at most $\ell$ in the common translation of $a,b$. Put


$$
e_\ell=\lfloor\log_3\ell\rfloor.
$$


After multiplication by $c_\ell$, the $k$-th translated coefficient at a step $3^Et$ has valuation at least


$$
e_\ell+k(E-e_\ell)\ge E
\qquad
(1\le k\le\ell<3^E).
\tag{6.3}
$$


This pays every derivative order, not just $k=1$.

Equivalently, if


$$
A=\binom ar,\quad B=\binom b{\ell-r},
$$


and $\Delta A,\Delta B$ are their translated differences, the complete change is


$$
(A+\Delta A)(B+\Delta B)-AB
=(\Delta A)B+A(\Delta B)+(\Delta A)(\Delta B).
\tag{6.4}
$$


The quadratic cross term is present. Multiplication by $c_\ell$ pays both linear terms modulo $3^E$, and pays the cross term at least as strongly.

These observations are not needed to replace the finite matrix proof below, but they explicitly validate the derivative and divided-difference precision implicit in the entry formulas.

---

# Part II. The full higher block theorem

## 7. Proof for every finite size, including incomplete final blocks

### Theorem 7.1 — Full finite ternary block law

Let $E\ge1$, $q_E=3^E$, and let


$$
d=kq_E+r,\qquad 0\le r<q_E.
$$


Then


$$
\boxed{
\widehat T_d
\equiv
\operatorname{diag}
\bigl(
\underbrace{\widehat T_{q_E},\ldots,\widehat T_{q_E}}_{k\text{ copies}},
\widehat T_r
\bigr)
\pmod{3^E},
}
\tag{7.1}
$$


where the final block is omitted if $r=0$.

#### Proof

By (4.6), terms $\ell\ge q_E$ in (5.2) vanish modulo $3^E$. Fix


$$
1\le\ell<q_E,\qquad e=\lfloor\log_3\ell\rfloor,
$$


and $r+s=\ell$.

For $r\le\ell$, formula (5.1) and (6.1) show the following.

**Inside a block.** Write $a=kq_E+a_0$, $i=kq_E+i_0$. Then


$$
a-i=a_0-i_0,
$$


and


$$
\binom ar\equiv\binom{a_0}r\pmod{3^{E-e}}.
$$


Thus the entry agrees with its first-block counterpart modulo $3^{E-e}$.

**Across a block boundary.** A nonzero lower-triangular entry must have
$a-i\le r<q_E$. If $i$ lies in an earlier block, then


$$
a-i>a_0.
$$


Consequently $r>a_0$, so $\binom{a_0}r=0$. Formula (6.1) therefore makes the crossing entry divisible by $3^{E-e}$.

The case $r=0$ is simply $C_0=I$. Thus each $C_r$ agrees modulo
$3^{E-e}$ with the asserted repeated block matrix. The same is true of $C_s$. Multiplying the two matrices introduces no denominator. Multiplication by


$$
c_\ell\in3^e\mathbb Z_3
$$


makes the entire discrepancy vanish modulo $3^E$.

Finally, the incomplete final block is the literal finite one. In


$$
(C_rC_s^T)[a,b]=\sum_iC_r[a,i]C_s[b,i],
$$


lower triangularity forces $i\le\min(a,b)$. A leading principal product therefore does not require a column beyond that principal block. There is no artificial completion of the last block.

The $\ell=0$ term is the identity. Summing proves (7.1). ∎

### Audit conclusion

The proof covers:

* every Newton coefficient $\ell$;
* every split $r+s=\ell$;
* every row and column;
* crossings between full blocks;
* the actual last incomplete block;
* every precision $3^E$;
* every finite matrix size.

It is not a first-coefficient argument, an observed pattern, or a dimension-residue substitution.



$$
\boxed{\text{FULL HIGHER TERNARY BLOCK THEOREM: PASS.}}
$$



---

## 8. Units, inverses, and the original $T_{n-1}$

The exact small transformed matrices are


$$
\widehat T_1=(1),
$$




$$
\widehat T_2=
\begin{pmatrix}1&-1\\-1&9\end{pmatrix},
\qquad
\widehat T_2^{-1}
=\frac18\begin{pmatrix}9&1\\1&1\end{pmatrix},
\tag{8.1}
$$


and


$$
\widehat T_3=
\begin{pmatrix}
1&-1&5\\
-1&9&99\\
5&99&3017
\end{pmatrix}.
\tag{8.2}
$$



Modulo $3$, the block lifts used in Turn 17 are


$$
B_1=(1),\qquad
B_2=\begin{pmatrix}1&2\\2&0\end{pmatrix},\qquad
B_3=\begin{pmatrix}1&2&2\\2&0&0\\2&0&2\end{pmatrix}.
$$


Their determinants are $1,-4,-8$, respectively. Theorem 7.1 at $E=1$ therefore proves


$$
\boxed{T_d,\widehat T_d\in\operatorname{GL}_d(\mathbb Z_3)
\quad(d\ge1).}
\tag{8.3}
$$



### 8.1 The inverse block law is proved, not imported

Let $D$ be the block matrix on the right of (7.1). Both $D$ and
$\widehat T_d$ are units. The exact finite identity


$$
\widehat T_d^{-1}-D^{-1}
=\widehat T_d^{-1}(D-\widehat T_d)D^{-1}
$$


gives


$$
\boxed{
\widehat T_d^{-1}
\equiv
\operatorname{diag}
\bigl(\widehat T_{q_E}^{-1},\ldots,\widehat T_{q_E}^{-1},
\widehat T_r^{-1}\bigr)
\pmod{3^E}.
}
\tag{8.4}
$$


There is no loss of precision in this inversion.

### 8.2 The original one-smaller matrix and its Schur scalar

At the original indices,


$$
n\equiv2,\qquad n-1=N\equiv1,\qquad n+1\equiv3\pmod{243}.
$$


Thus the respective actual terminal blocks have sizes $2,1,3$.

Retain the literal bordering


$$
T_n=
\begin{pmatrix}
T_N&k^-\\
(k^-)^T&d_N
\end{pmatrix},
$$


where


$$
k^-_a=\binom{N+a}{a}\gamma_{N+a},
\quad 0\le a<N,
\qquad
d_N=\binom{2N}{N}\gamma_{2N}.
$$


Its Schur scalar is


$$
\sigma_N=d_N-(k^-)^TT_N^{-1}k^-.
\tag{8.5}
$$



The finite Pascal bordering is a unit triangular congruence. If the corresponding transformed border is $(w,\widehat d_N)$, direct expansion gives


$$
\sigma_N=\widehat d_N-w^T\widehat T_N^{-1}w.
$$


The terminal $1$-by-$1$ block of $\widehat T_N$ is $1$, the transformed border is $-1$, and $\widehat d_N\equiv9\pmod{243}$. Therefore


$$
\boxed{\sigma_N\equiv8\pmod{243}.}
\tag{8.6}
$$


It is a unit.

The entire inverse, including the rank-one correction in every entry, is


$$
T_n^{-1}=
\begin{pmatrix}
T_N^{-1}+T_N^{-1}k^-\sigma_N^{-1}(k^-)^TT_N^{-1}
&-T_N^{-1}k^-\sigma_N^{-1}\\
-\sigma_N^{-1}(k^-)^TT_N^{-1}&\sigma_N^{-1}
\end{pmatrix}.
\tag{8.7}
$$



This unit scalar $\sigma_N$ is **not** the producer scalar $\Xi$. Confusing them would incorrectly erase the latter’s one-digit division.

---

# Part III. Complete producer, scalar normalization, and signed endpoint

## 9. The full force and the true next column

Set


$$
F_{\rm fac}=N!,
\qquad
u_a=\frac{N!(-2)^a}{a!},
\qquad
v=T_n^{-1}u.
$$


The next-column force is


$$
k_a=\binom{n+a}{a}\gamma_{n+a},
\qquad
h_{\rm vec}=T_n^{-1}k.
$$


It is the column $n$ of the actual $T_{n+1}$, restricted to rows
$0,\ldots,n-1$.

Retain


$$
b_{\rm force}=-n-66
$$


and the complete force


$$
\boxed{
\mathbf t
=3nh_{\rm vec}
+(b_{\rm force}+6)e_N
+\frac{2b_{\rm force}}N e_{N-1}.
}
\tag{9.1}
$$


The denominator $N$ is a ternary unit.

Write


$$
P_{n+1}=
\begin{pmatrix}P_n&0\\p^T&1\end{pmatrix},
\qquad p_a=\binom na,
$$


and let $\widehat k$ be the first $n$ entries of column $n$ of
$\widehat T_{n+1}$. Exact finite block multiplication gives


$$
\boxed{
h_{\rm vec}=P_n^{-T}\bigl(p+\widehat T_n^{-1}\widehat k\bigr).
}
\tag{9.2}
$$


The dense known term is retained:


$$
(P_n^{-T}p)_a=(-1)^{n-a-1}\binom na.
\tag{9.3}
$$



---

## 10. Uniform evaluation of $\Xi,\chi_{\rm prod},\xi$

Define


$$
\Xi=F_{\rm fac}^2-u^TT_n^{-1}u,
\qquad
\chi_{\rm prod}=u^T\mathbf t,
\qquad
\xi=\frac{\chi_{\rm prod}}{\Xi}.
$$



### 10.1 The transformed factorial force

For $a\le N-2$, $N!/a!$ contains the factor $N-1$, whose valuation is $5$. Hence


$$
u_a\equiv0\pmod{243}.
$$


The remaining entries are


$$
u_{N-1}=N(-2)^{N-1},\qquad u_N=(-2)^N.
$$


LTE gives


$$
v_3\bigl((-2)^{N-1}-1\bigr)=1+v_3(N-1)=6.
$$


Consequently


$$
\widehat u:=P_n^{-1}u
\equiv e_{N-1}-3e_N\pmod{243}.
\tag{10.1}
$$



The original $N$ is far beyond the finite threshold needed for
$(N!)^2\equiv0\pmod{243}$. This is a modular payment, not deletion of the exact factorial term.

### 10.2 The scalar $\Xi$

Using the actual terminal $2$-block,


$$
\begin{aligned}
u^TT_n^{-1}u
&\equiv
(1,-3)\frac18
\begin{pmatrix}9&1\\1&1\end{pmatrix}
\binom1{-3}\\
&=\frac32
\pmod{243}.
\end{aligned}
$$


Therefore


$$
\boxed{
\Xi\equiv-\frac32\equiv120\pmod{243}.
}
\tag{10.2}
$$


In particular,


$$
\boxed{
v_3(\Xi)=1,\qquad
\Xi/3\equiv40\pmod{81}.
}
\tag{10.3}
$$



The transformed diagonal assertion also follows:


$$
\boxed{\widehat T_n[N,N]\equiv9\pmod{243}.}
\tag{10.4}
$$


This is an assertion about the transformed diagonal, not the raw diagonal
$\binom{2N}{N}\gamma_{2N}$.

### 10.3 The complete numerator

From the actual final $3$-block of $\widehat T_{n+1}$,


$$
\widehat k_{\{N-1,N\}}\equiv\binom5{99}\pmod{243}.
$$


Also


$$
p_{\{N-1,N\}}
=
\binom{\binom n2}{n}
\equiv\binom12\pmod{243}.
$$


Since


$$
\widehat T_2^{-1}\binom5{99}=\binom{18}{13},
$$


we obtain


$$
\boxed{
u^Th_{\rm vec}
\equiv
(1,-3)\binom{19}{15}
=-26\pmod{243}.
}
\tag{10.5}
$$



Both affine terminal forces must now be included:


$$
\begin{aligned}
u^T\mathbf t
={}&3n\,u^Th_{\rm vec}
 +(b_{\rm force}+6)(-2)^N
 +\frac{2b_{\rm force}}N N(-2)^{N-1}\\
={}&3n\,u^Th_{\rm vec}+6(-2)^N.
\end{aligned}
\tag{10.6}
$$


The cancellation is exact. It is not permission to omit either term from an individual coefficient.

Thus


$$
\boxed{
\chi_{\rm prod}\equiv
3\cdot2\cdot(-26)+6(-2)
=-168\pmod{729}.
}
\tag{10.7}
$$


So $v_3(\chi_{\rm prod})=1$.

After dividing both scalars by $3$, the common available precision is modulo $81$:


$$
\boxed{
\xi
=\frac{\chi_{\rm prod}/3}{\Xi/3}
\equiv\frac{-56}{-1/2}
=112\equiv31\pmod{81}.
}
\tag{10.8}
$$


This proves $v_3(\xi)=0$. It does not prove the exact equality $\xi=112$.

**Verdict: PASS. The cached scalar residues are consistent receipts, but are not used as the uniform proof.**

---

## 11. The full Schur correction and all producer coefficients

The producer scalar is the Schur complement of the literal augmented matrix


$$
\mathcal A_{\rm prod}
=
\begin{pmatrix}
T_n&u\\
u^T&F_{\rm fac}^2
\end{pmatrix}.
$$


Its entire inverse is


$$
\boxed{
\mathcal A_{\rm prod}^{-1}
=
\begin{pmatrix}
T_n^{-1}+vv^T/\Xi&-v/\Xi\\
-v^T/\Xi&1/\Xi
\end{pmatrix}.
}
\tag{11.1}
$$


Thus the whole bivariate rank-one correction is present; it is not replaced by one entry.

The sole nonunit division here is by $\Xi$, of depth one. Indeed, finite block elimination gives


$$
\det\mathcal A_{\rm prod}=\det T_n\,\Xi,
$$


so the augmented producer matrix has determinant valuation exactly one. Over $\mathbb Z_3$, its elementary-divisor valuations are $0,\ldots,0,1$.

The special forcing pays that division:


$$
\boxed{
\mathcal A_{\rm prod}
\binom{\mathbf t+\xi v}{-\xi}
=
\binom{T_n\mathbf t}{0}.
}
\tag{11.2}
$$


Here


$$
T_n\mathbf t
=3nk+(b_{\rm force}+6)T_ne_N
+\frac{2b_{\rm force}}N T_ne_{N-1},
$$


so every original row of the force is retained.

The actual coefficient formula remains


$$
\boxed{
q_a=[x^a]\delta Q
=-\frac{N!}{a!}\bigl(t_a+\xi v_a\bigr),
\qquad 0\le a\le N.
}
\tag{11.3}
$$


Since $T_n^{-1}$, $v$, $h_{\rm vec}$, $\mathbf t$, and $\xi$ are integral at $3$,


$$
v_3(q_a)\ge v_3(N!/a!).
\tag{11.4}
$$


For $a=n-r$, $1\le r\le n$, write


$$
A_r(n)=\prod_{j=1}^{r-1}(n-j)=\frac{N!}{(n-r)!}.
$$


Because $n\equiv2\pmod3$,


$$
\boxed{v_3(A_r(n))\ge\lfloor r/3\rfloor.}
\tag{11.5}
$$



At $y=-1$, equivalently $x=-2$,


$$
\begin{aligned}
\delta Q(-1)
&=-u^T\mathbf t-\xi u^Tv\\
&=-\xi(\Xi+u^Tv)\\
&=\boxed{-\xi F_{\rm fac}^2}.
\end{aligned}
\tag{11.6}
$$


This endpoint is nonzero. It remains part of the exact actual producer.

---

# Part IV. Uniform translation and the Turn 17 dependency

## 12. What $n'=n+3^Et$ means on the original family

The block theorem is valid for all positive finite sizes. Consequently, if


$$
d'=d+3^Et>0,
$$


corresponding right-offset entries of $\widehat T_d$ and
$\widehat T_{d'}$, and of their inverses, agree modulo $3^E$, whenever both coordinates exist.

For the inverse, this follows from (8.4). The within-block positions are the same, and the block numbers are shifted by $t$. Cross-block entries are zero on both sides. The final incomplete block has the same size.

The same argument applies separately at sizes


$$
n-1,\ n,\ n+1
\quad\text{and}\quad
n'-1,\ n',\ n'+1.
$$


In particular, the genuine next-column force is covered even when $n+1$ is a full-block boundary.

For original sizes, however, $t$ is not free. If


$$
n=4^j+1,\qquad n'=4^{j'}+1,
$$


then for $j'\ne j$,


$$
\boxed{
v_3(n'-n)=1+v_3(j'-j).
}
\tag{12.1}
$$


Thus


$$
n'\equiv n\pmod{3^E}
\quad\Longleftrightarrow\quad
j'\equiv j\pmod{3^{E-1}}.
\tag{12.2}
$$


The size shift is specifically


$$
t=\frac{4^j(4^{j'-j}-1)}{3^E},
$$


not an independently chosen integer. Both $j,j'$ must still lie in the original progression, and physical applications additionally require their actual real-window admission.

This validates the original-family hypothesis without changing the family.

---

## 13. Exact status of LOCAL and weighted $E33$

The LOCAL proof in Turn 17 already passed independently. Its matrix estimate


$$
v_3(\widehat T[a,b])\ge\lfloor|a-b|/6\rfloor
$$


is now also established directly in (5.7).

Its weighted Neumann paths have total excursion at most


$$
w_M=13(M-1)+2
$$


modulo $3^M$. For


$$
M\ge4,\qquad 1\le L\le3M,
$$


one may take


$$
R_{\rm loc}\ge 6M+w_M+2=19M-9,
$$


increased by at most two so that


$$
R_{\rm loc}\equiv n\pmod3.
$$


The explicit size hypothesis is


$$
n,n'\ge R_{\rm loc}.
\tag{13.1}
$$


All original sizes used here exceed this bound at $M=33,L=72$.

The weighted-period deduction in Turn 17 required the block law for **all finite sizes**, including $n+1$. Theorem 7.1 supplies exactly that hypothesis.

For completeness, the precision-critical features of that deduction are:

1. $\widehat u$ is supported within the last $3M$ coordinates modulo $3^M$.
2. The actual transformed next column is supported within the last $6M-1$ coordinates.
3. The known part
   

$$
(h_{\rm known})_{n-r}=(-1)^{r-1}\binom nr
$$


   is retained.
4. For $r\le3M<3^M$,
   

$$
v_3(A_r(n))\ge\lfloor r/3\rfloor
   \ge\lfloor\log_3r\rfloor.
   \tag{13.2}
$$


   Hence the factorial weight pays every Pascal continuity loss in the raw reconstruction.
5. The weight is never cancelled out of a congruence.
6. Both affine terms, $b_{\rm force}+6$ and $2b_{\rm force}/N$, remain present.
7. $\Xi$ and $\chi_{\rm prod}$ are first computed modulo $3^M$, then both divided by $3$. This gives $\xi$ only modulo $3^{M-1}$.

Therefore the previously conditional conclusion is now available unconditionally, within the established scalar and size hypotheses:


$$
\boxed{
\begin{aligned}
\Xi(n')&\equiv\Xi(n)\pmod{3^M},\\
\chi_{\rm prod}(n')&\equiv\chi_{\rm prod}(n)\pmod{3^M},\\
\xi(n')&\equiv\xi(n)\pmod{3^{M-1}},\\
q_{n'-r}(n')&\equiv q_{n-r}(n)\pmod{3^{M-1}},
\qquad 1\le r\le L.
\end{aligned}
}
\tag{13.3}
$$



The accompanying weighted assertions remain


$$
A_r(n')v_{n'-r}(n')\equiv A_r(n)v_{n-r}(n)\pmod{3^M},
$$


and the analogous statement for the complete $h_{\rm vec}$.

There is no reason to restore the conservative input moduli $3^{37}$ or $3^{39}$ once this stronger theorem is used. Conversely, there is no permission to promote the full output jet from $3^{M-1}$ to $3^M$.

### 13.1 The original $E33$ progression

At $M=33,L=72$,


$$
R_{\rm loc}=620.
$$


For


$$
\boxed{j=84645+3^{32}s,\qquad s\ge0,}
\tag{13.4}
$$


LTE gives


$$
4^j+1\equiv4^{84645}+1\pmod{3^{33}}.
$$


This progression lies inside the original class modulo $3^{12}$. Therefore


$$
\boxed{
(q_{n-72},\ldots,q_{n-1})\pmod{3^{32}}
\quad\text{and}\quad
V_{70}\pmod{3^{32}}
}
\tag{13.5}
$$


are constant along it.

The saved array is still a finite arithmetic record for its reference input. The new theorem justifies transporting a verified reference array to the corresponding original terminal offsets. It does not independently authenticate the execution history of that array.

The separate irrational-rotation argument applies to the step $3^{32}$, since


$$
3^{32}\log_3 4
$$


is irrational. Thus the established real-window selection remains available on this progression. No claim is made that the base producer index itself satisfies the real Range III window.

### Verdict



$$
\boxed{\text{LOCAL: reused PASS.}}
$$




$$
\boxed{\text{Weighted complete-source period: former dependency fully discharged.}}
$$




$$
\boxed{\text{Original }E33\text{ conclusion: PASS, with output precision }3^{32}.}
$$



The already identified general-domain implementation allocation repair in Turn 17 remains exactly that repair. It is unrelated to the block theorem, and the saved $M=33,L=72$ case is not rerun.

---

# Part V. Audit of the $72$-coefficient reduction and bounded reconstruction

## 14. Exact tail and endpoint payment

For the original $N$, (1.1) gives


$$
\begin{aligned}
v_3\!\left(\frac{N!}{(N-72)!}\right)
&=v_3(N-1)+\sum_{r=2}^{71}v_3(N-r)\\
&=5+v_3(70!)\\
&=5+23+7+2\\
&=\boxed{37}.
\end{aligned}
\tag{14.1}
$$


The equality


$$
v_3(N-r)=v_3(r-1),\qquad2\le r\le71,
$$


is valid because $v_3(r-1)<5$.

It follows that


$$
q_a\in3^{37}\mathbb Z_3
\qquad(a\le n-73).
$$


Retain all $72$ top coefficients:


$$
P_{71}(x)=\sum_{r=0}^{71}q_{n-72+r}x^r.
$$


Then


$$
\delta Q=x^{n-72}P_{71}(x)+L_{\rm tail}(x),
\qquad L_{\rm tail}\in3^{37}\mathbb Z_3[x].
$$



The exact nonzero endpoint (11.6), together with the sufficiently deep factorial square, gives


$$
P_{71}(-2)\in3^{37}\mathbb Z_3.
$$


Monic division yields


$$
P_{71}(x)=(x+2)V_{70}(x)+P_{71}(-2),
$$


with


$$
\boxed{
[x^b]V_{70}
=
\sum_{r=b+1}^{71}(-2)^{r-b-1}q_{n-72+r},
\qquad0\le b\le70.
}
\tag{14.2}
$$


There is no division by a ternary nonunit.

Since $n-72=A-70$,


$$
\boxed{
\delta Q-(y+1)x^{A-70}V_{70}
\in3^{37}\mathbb Z_3[x].
}
\tag{14.3}
$$



**Verdict: PASS.** The endpoint-zero short polynomial is only a paid finite-precision replacement of an actual polynomial with a nonzero endpoint.

---

## 15. The $617$-coordinate reconstruction

At precision $3^M$, the matrix half-bandwidth is at most $6M-1$. Let $B$ be the literal modulo-$3$ block lift, including the actual short final block. Its inverse has half-bandwidth $2$.

A correction entry of valuation $\nu\ge1$ has jump at most $6\nu+5$. A Neumann path with correction valuations summing to $W<M$ therefore has total absolute length at most


$$
6W+7r+2\le13W+2\le13(M-1)+2.
\tag{15.1}
$$


This bounds every intermediate excursion, not just endpoint displacement.

For $M=33$,


$$
6M-1=197,\qquad13(M-1)+2=418.
$$


The $617$-coordinate window begins at $n-617$, which is divisible by $3$. The earliest relevant next-column coordinate is $n-197$, whose distance from the left edge is


$$
(n-197)-(n-617)=420>418.
$$


Thus every relevant path remains inside the window.

The source’s number $421$ is the inclusive count of positions. Replacing it by the actual distance $420$ repairs the wording without changing the conclusion.

The complete reconstruction uses:

* $c_0,\ldots,c_{197}$;
* the actual entry formula (5.3);
* the last $99$ raw $u$-coordinates, with exact factorial quotient and power;
* the last $197$ transformed next-column coordinates;
* the dense known part of $h_{\rm vec}$;
* the exact top Pascal reconstruction;
* the full scalar contraction before division by $3$.

For $r\le197$,


$$
\lfloor\log_3r\rfloor\le4.
$$


Therefore upper binomial arguments modulo $3^{37}$ determine these binomial values modulo $3^{33}$. The power $(-2)^a$ needs no stronger modulus, and $N^{-1}$ is a unit. Hence the Turn 14 input


$$
N\bmod3^{37}
$$


is sufficient for its reconstruction.

Computing $\Xi,\chi_{\rm prod}\pmod{3^{33}}$ gives
$\xi\pmod{3^{32}}$, and then every actual top coefficient and every coefficient of $V_{70}$ modulo $3^{32}$.

**Verdict: PASS, with the harmless distance wording repaired.**

This certifies the reduction method. It is not a new execution of the optional $617$-coordinate calculation.

---

# Part VI. Complete physical columns, bivariate Schur correction, and limits

## 16. All physical boundaries remain literal

Retain


$$
U_s=x^s,\quad0\le s<D,
$$




$$
z_i=x^Dy^i,\quad0\le i<\nu,\qquad \nu=D/2-1,
$$




$$
Y_t=y^t,\quad d\le t\le m,\qquad d=D+\nu,
$$


and


$$
W=[U\ Y].
$$


The highest HIGH column is $Y_m$, inclusively.

The functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!.
\tag{16.1}
$$


The cutoff is


$$
K_{\rm phys}=2n-2,\qquad
2K_{\rm phys}+1=4H-4D+5<3^{h+1}.
$$


Thus every retained denominator has ternary valuation at most $h$.

The core and actual forms are


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A,
$$




$$
Q_{\rm act}=Q_c+\delta Q,
$$




$$
G_\alpha(f,g)=\mathcal M(Q_\alpha fg),\qquad
E_\alpha=G_\alpha(W,W),
$$




$$
F_\alpha[p]
=x^Dp-WE_\alpha^{-1}G_\alpha(W,x^Dp).
\tag{16.2}
$$



The finite prefix boundaries remain


$$
R_*=\frac{9Q+1}{2},\qquad
a_0=R_*-1=121P+\frac{P-1}{2},
$$




$$
\tau=\frac{N_0-3}{2},\qquad
\ell=3R+1,
$$




$$
K=\{0,\ldots,\ell-1\},\qquad
J=\{\ell,\ldots,\tau-1\},\qquad
R_*+\tau=\nu.
$$


No last middle coordinate is removed.

The degree conditions are adequate. The original bound $D/H<1/C_{16}$ gives $d<m$ with a large margin. Admitted uncorrected columns and all columns in $W$ have degree at most $m$, so their corrected columns do too. Since $\deg Q_{\rm act}\le n$,


$$
\deg(Q_{\rm act}fg)\le n+2m=2n-1.
$$


After endpoint subtraction and division by $y+1$, the degree is at most the actual cutoff $2n-2$.

Therefore $\mathcal M$ is integral on the admitted integral polynomials. The reused physical inverse bound gives


$$
F_\alpha[p]\in3^{-1}\mathbb Z_3[y].
\tag{16.3}
$$



---

## 17. The whole bivariate correction and every return term

For a source $Q$, denote the returned form by $S_Q(p,q)$. If


$$
Q'=Q+\epsilon,
$$


the exact stationary identity is


$$
\boxed{
S_{Q'}(p,q)-S_Q(p,q)
=
\mathcal M(\epsilon F_Q[p]F_Q[q])
-c_p^TE_{Q'}^{-1}c_q,
}
\tag{17.1}
$$


where


$$
c_p=\mathcal M(\epsilon W F_Q[p]).
$$


This is a complete bivariate identity in the two admitted inputs.

For $\epsilon\in3^{37}\mathbb Z_3[x]$,

* the direct term is in $3^{35}$;
* $c_p,c_q\in3^{36}$;
* $E_{Q'}^{-1}\in3^{-1}\operatorname{Mat}(\mathbb Z_3)$, by the finite perturbation identity;
* the return is in $3^{71}$.

Thus


$$
S_{Q'}-S_Q\in3^{35}M.
$$


After the original division by $3^{26}$,


$$
\boxed{\mathsf A_{\rm short}-\mathsf A_{\rm act}\in3^9M.}
\tag{17.2}
$$



### 17.1 Keeping $E_{\rm act}^{-1}$ unchanged

Define


$$
\alpha_\alpha[p]=E_\alpha^{-1}G_\alpha(W,x^Dp)
$$


and


$$
b_p^\delta=\mathcal M(\delta Q\,W F_c[p]).
$$


Exact finite orthogonality gives


$$
\boxed{
E_{\rm act}^{-1}b_p^\delta
=\alpha_{\rm act}[p]-\alpha_c[p]\in3^{-1}M.
}
\tag{17.3}
$$



Now change $\delta Q$ to $\delta Q+\epsilon$, keeping the original
$E_{\rm act}^{-1}$ literal. Put


$$
c_p=\mathcal M(\epsilon W F_c[p]).
$$


The entire change in the direct-minus-return expression is


$$
\begin{aligned}
&\mathcal M(\epsilon F_c[p]F_c[q])\\
&\quad-c_p^TE_{\rm act}^{-1}b_q^\delta
-(b_p^\delta)^TE_{\rm act}^{-1}c_q
-c_p^TE_{\rm act}^{-1}c_q.
\end{aligned}
\tag{17.4}
$$


All four terms are present.

If $\epsilon\in3^s$, the first three terms are in $3^{s-2}$, while the last is in $3^{2s-3}$. Therefore, for $s\ge2$, the complete change is in $3^{s-2}$.

Consequently:

* the exact tail replacement at $s=37$ changes the whole expression by $3^{35}$;
* a lift of $V_{70}\pmod{3^{32}}$ changes it by $3^{30}$;
* after division by $3^{29}$, the latter change is zero modulo $3$.

This verifies the projection payment without deleting the $W$-return.

---

## 18. What the full block PASS does not evaluate

Retain


$$
\mathcal S=\{14,15,16,41,42,43,95,96,97\}.
$$


For the admitted indices, let


$$
g_i(y)=2y^i(1-y)^\eta\sum_{r\in\mathcal S}y^{rP},
\qquad
\widehat F_i=F_c[g_i].
$$


The established gaps


$$
w+2k-2\le\kappa_1-120,\qquad
i+\eta+1\le\delta_{\rm idx}<\kappa_1
$$


imply


$$
\deg g_i=97P+\eta+i<a_0.
$$


Thus these are admitted original inputs, not freely selected tests.

The complete comparison uses


$$
\mathsf A_{\rm act}-\mathsf A_c\in27M,\qquad
d_{\rm act}-d_c\in81M,
$$


with the actual prefix unit inverses and normalization
$\mathsf A=-S/3^{26}$. Finite inverse variation then gives


$$
\mathcal P_{7,\rm act}-\mathcal P_{7,c}
=
\frac{
\mathcal M(\delta Q\,\widehat F_i\widehat F_j)
-(b_i^\delta)^TE_{\rm act}^{-1}b_j^\delta
}{3^{29}}
\pmod3.
\tag{18.1}
$$


The sign follows from the minus sign in $\mathsf A=-S/3^{26}$. The changes in $d$ carry $81$, so after division by $27$ they vanish modulo $3$. The inverse variation contributes the stated normalized Schur difference.

The source reduction makes (18.1) equal to


$$
\boxed{
\begin{aligned}
\frac{\mathcal N_{ij}}{3^{29}}\pmod3,\qquad
\mathcal N_{ij}={}&
\mathcal M\!\left(
(y+1)x^{A-70}V_{70}\widehat F_i\widehat F_j
\right)\\
&-\mathcal M\!\left(
(y+1)x^{A-70}V_{70}W\widehat F_i
\right)^T
E_{\rm act}^{-1}
\mathcal M\!\left(
(y+1)x^{A-70}V_{70}W\widehat F_j
\right).
\end{aligned}
}
\tag{18.2}
$$



All $9\times9$ band pairs remain. Only their complete aggregate has the established $3^{29}$ divisibility. It is not legitimate to divide each band-pair summand separately without an additional proof.

The physical component


$$
\mathcal M\!\left(
(y+1)x^{A-70}V_{70}Y_m\widehat F_i
\right)
$$


remains in the return vector.

### Exact obstruction

The producer block theorem controls $\widehat T_n$. It supplies no locality theorem for the different physical matrix $E_{\rm act}^{-1}$.

In particular, it does not prove that


$$
\widehat F_i
=x^Dg_i-WE_c^{-1}G_c(W,x^Dg_i)
$$


has short support. Complete LOW feedback, finite HIGH inverse contributions, lower truncation, and the physical terminal $Y_m$ can all contribute.

Therefore the now-unconditional frozen producer jet is not an evaluation of $\mathcal N_{00}$, much less of the whole physical-seventh matrix.



$$
\boxed{\mathcal N_{ij}/3^{29}\pmod3\text{ remains OPEN.}}
$$



---

## 19. Concrete next lemma, with its already paid precision target

The residual-certificate lemma in Turn 17 remains a valid, concrete target, not a completed evaluation.

Let $\widetilde V_{70}$ lift the actual quotient modulo $3^{32}$, and set


$$
Q_s=(y+1)x^{A-70}\widetilde V_{70},\qquad
\Phi_i=3\widehat F_i.
$$


Define the actual complete objects


$$
B_i=\mathcal M(Q_sW\Phi_i),\qquad
D_{ij}=\mathcal M(Q_s\Phi_i\Phi_j),\qquad E=E_{\rm act}.
$$


Then


$$
9\mathcal N_{ij}^{\,s}=D_{ij}-B_i^TE^{-1}B_j.
$$



If integral vectors $z_i$ satisfy every finite residual coordinate


$$
\rho_i=B_i-Ez_i\in3^{17}\mathbb Z_3^{\dim W},
$$


then


$$
\Theta_{ij}
=D_{ij}-B_i^Tz_j-z_i^TB_j+z_i^TEz_j
$$


satisfies


$$
\Theta_{ij}\equiv9\mathcal N_{ij}^{\,s}\pmod{3^{32}},
$$


because


$$
\rho_i^TE^{-1}\rho_j\in3^{17+17-1}=3^{33}.
$$


Accordingly,


$$
\frac{\mathcal N_{ij}}{3^{29}}
\equiv\frac{\Theta_{ij}}{3^{31}}\pmod3,
$$


after the complete aggregate is formed.

The next source-specific lemma must construct or evaluate these complete observations in a precision-sized way, including every LOW coordinate and $Y_m$. Merely displaying $B_i,D_{ij}$, or the formal sum (18.2), does not accomplish that task.

No original-sized residual vector or solve is proposed here.

---

# Part VII. Consolidated precision and status audit

## 20. Division and precision bill

| Operation | Exact payment or loss |
|---|---|
| Gamma formula $A_k=(2k)!/(2^kk!)$ | Integer; valuation $v_3((2k)!)-v_3(k!)$ retained |
| Finite divided gamma jets | Factorials retained; matrix entries recovered by exact cancellation |
| Newton coefficients $c_\ell$ | No $\ell!$-division; integer finite differences |
| Binomial translation of lower index $r$ | Loss at most $\lfloor\log_3r\rfloor$ |
| $k$-th divided derivative | Bound (6.2); every order paid in (6.3) |
| Pascal conjugation | Integral unimodular matrices; no ternary loss |
| $T_d^{-1}$ | Integral for every finite $d$ |
| Original bordering scalar $\sigma_N^{-1}$ | Unit, $\sigma_N\equiv8\pmod{243}$ |
| Producer scalar $\Xi^{-1}$ | Costs one ternary digit |
| $\Xi/3$ from $\Xi\bmod243$ | Available modulo $81$ |
| $\chi_{\rm prod}/3$ from numerator modulo $729$ | Available modulo $243$ |
| $\xi$ from both normalized scalars | Common precision modulo $81$ |
| General scalar reconstruction modulo $3^M$ | $\xi$ and full top output modulo $3^{M-1}$ |
| Force denominator $N$ | Actual ternary unit |
| Coefficient factor $N!/a!$ | Exact integer, not cancelled from congruences |
| Division by $x+2$ | Monic; no loss; remainder retained |
| Physical corrected column $F_\alpha[p]$ | Allowance $3^{-1}$ |
| Two corrected columns | Total possible loss $3^{-2}$ |
| Complete $3^{37}$ source replacement | Whole Schur error $3^{35}$ |
| Prefix normalization | Division by $3^{26}$, leaving error $3^9$ |
| Physical-seventh comparison | Complete numerator divided by $3^{29}$ |
| $V_{70}\bmod3^{32}$ lift | Whole error $3^{30}$, sufficient after $3^{29}$ division |
| Complete-return residual certificate | Residual $3^{17}$, aggregate modulo $3^{32}$, final division $3^{31}$ |

All statements here concern ternary precision. They do not evaluate denominators or contents at other primes.

---

## 21. PASS / REPAIR / OPEN ledger

| Claim or obligation | Verdict |
|---|---|
| Gamma polynomial formula and recurrence | **PASS** |
| Logarithmic and linear Newton coefficient floors | **PASS** |
| Literal finite Pascal conjugation | **PASS** |
| Every entry and all binomial ranges | **PASS** |
| Whole bivariate kernel | **PASS** |
| Derivative and divided-difference payment | **PASS** |
| Full higher block law for every finite size and precision | **PASS** |
| Actual final incomplete blocks | **PASS** |
| Finite inverse block law | **PASS**, derived by a unit inverse identity |
| Simultaneous treatment of $T_{n-1},T_n,T_{n+1}$ | **PASS** |
| Original-family admissibility of $n'=n+3^Et$ | **PASS**, with the LTE restriction on $j'-j$ |
| Uniform $\Xi,\chi_{\rm prod},\xi$ scalar conclusions | **PASS** |
| Complete force and all correction coefficients | **PASS** |
| Nonzero signed endpoint | **PASS** |
| Exact $72$-coefficient $3^{37}$ tail reduction | **PASS** |
| Complete physical projection payment | **PASS**, using the established physical inverse bounds |
| $617$-coordinate reconstruction | **PASS**; distance wording repaired to $420$ |
| Turn 17 LOCAL theorem | **REUSE: PASS** |
| Turn 17 weighted period | **Dependency discharged; unconditional at its stated scope** |
| Original $E33$ frozen terminal jet | **PASS**, modulo $3^{32}$, not $3^{33}$ |
| Cached arrays and scalar receipts | **Finite arithmetic records only** |
| Complete $\mathcal N_{00}$ evaluation | **OPEN** |
| Whole physical-seventh/source-$34$ work | **OPEN and distinct** |
| First-$4$ return | **Separate obligation; not evaluated here** |
| Uniform56 | **Separate item; no implication from this audit** |
| Core $\eta_0$ | **Established parent-reviewed result at its separate scope** |
| Transport of core $\eta_0$ to actual $Q_{\rm act}$ | **Not proved here** |
| Actual contents, least clearer, all-prime gcd | **OPEN** |
| Primitive denominator and same-index nonzero whole-error decay | **OPEN** |
| Rationality or irrationality of $e+\pi$ | **UNRESOLVED** |

### Retained forcing and frame boundaries

The full forcing identity remains


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$


Both terms remain.

The moment recurrence remains


$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\qquad0\le t\le2n-2.
$$


The designated index


$$
t_*=\frac{3^h-5}{2}
$$


is retained, but


$$
2t_*+1=3^h-4
$$


is a ternary unit. Thus it is not the denominator pole of this displayed recurrence. The denominator-$3^h$ pole is at
$(3^h-1)/2$. Any separate shifted resonance at $t_*$ needs its own stated identity.

The diagonal frames remain distinct:


$$
\lambda_{\rm new}
=
\lambda^{\rm pref}
-\frac13f_J^TB^{-1}f_J
-\frac19f_b^TA_b^{-1}f_b
\in3^{-2}\mathbb Z_3,
$$




$$
\lambda_4
=
\lambda_{\rm new}
-\frac1{81}f_C^TA_4^{-1}f_C
\in3^{-4}\mathbb Z_3.
$$


The physical-$5$ complementary returns are not retired by the present block theorem.

---

# Part VIII. Global arithmetic and the research objective

## 22. Actual contents, least clearer, all-prime gcd, and whole error

No producer basis change redefines an original column content. Even an integral unimodular change of coordinates does not identify the content of each transformed column with the content of each original column.

Retain the actual least simultaneous clearer $\ell_{\rm clr}$, and


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1.
$$


The final gcd is over **all primes**:


$$
\boxed{G=\gcd(|A_\ell|,|B_\ell|).}
$$


For $B_\ell\ne0$, the actual primitive pair is


$$
q_{\rm prim}=\frac{|B_\ell|}{G}>0,\qquad
p_{\rm prim}
=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{G}.
$$



The whole signed error is


$$
\boxed{
q_{\rm prim}(e+\pi)-p_{\rm prim}
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{G}
\det H_{\rm complete}.
}
\tag{22.1}
$$


Its positive magnitude is obtained by taking the absolute value of this whole expression, not of one local summand.

An irrationality proof still requires, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\boxed{
\log G-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|
\longrightarrow+\infty.
}
\tag{22.2}
$$


These would imply


$$
0<
\left|q_{\rm prim}(e+\pi)-p_{\rm prim}\right|
\longrightarrow0.
$$


If $e+\pi=a/b$ were rational, every such nonzero integer linear form would have magnitude at least $1/|b|$.

The result $\Xi\ne0$ is not the result
$\det H_{\rm complete}\ne0$. The valuation $v_3(\Xi)=1$ is not an all-prime gcd estimate or a primitive-denominator estimate.

---

## 23. Bounded arithmetic docket

**No new bounded arithmetic calculation is indispensable for this audit.** The higher block theorem, the scalar evaluations, the original-family period implication, and the precision bills above are symbolic proofs.

In particular, this report does not request:

* an old LOW48 or $729$-position check;
* an M33/L72 inverse calculation;
* the $4950/1964$ compatibility scan;
* the optional $617$-coordinate calculation;
* an original-sized vector, table, or solve.

The existing finite receipts remain at their stated finite scope.

For the remaining physical correction, the exact verifiable target is already specified:

* complete residuals $B_i-E_{\rm act}z_i$ in $3^{17}$;
* the complete aggregate $\Theta_{ij}$ modulo $3^{32}$;
* the resulting quotient $\Theta_{ij}/3^{31}\pmod3$.

But a precision-sized construction of those observations has not yet been proved. Therefore no new bounded computation purporting to evaluate $\mathcal N_{00}$ is authorized mathematically by this packet alone.

---

# Conclusion

The principal new outcome is a complete independent **PASS** of the A4 Turn 14 higher ternary block theorem, including its finite boundaries, coefficient floors, all rows and columns, full bivariate identities, derivative and divided-difference costs, and finite inverse consequences.

The strongest paid original producer conclusions now include


$$
\boxed{
v_3(\Xi)=v_3(\chi_{\rm prod})=1,\qquad v_3(\xi)=0,
}
$$




$$
\boxed{
\Xi\equiv120\pmod{243},\quad
\chi_{\rm prod}\equiv-168\pmod{729},\quad
\xi\equiv31\pmod{81},
}
$$




$$
\boxed{
\delta Q-(y+1)x^{A-70}V_{70}\in3^{37}\mathbb Z_3[x],
}
$$


and the now-unconditional terminal coefficient period


$$
\boxed{
j=84645+3^{32}s
\quad\Longrightarrow\quad
V_{70}\pmod{3^{32}}
\text{ is fixed at corresponding original terminal offsets}.
}
$$



This fully discharges the higher-block dependency retained by the passed LOCAL and weighted $E33$ theorem. It does not require a stronger input modulus, and it does not recover the digit spent in division by $\Xi$.

The exact remaining local bottleneck is the complete original physical contraction


$$
\mathcal N_{ij}/3^{29}\pmod3,
$$


including the corrected columns, LOW feedback, the complete $E_{\rm act}^{-1}$ return, and the physical $Y_m$ component. The core $\eta _0$ theorem does not supply that actual transport.

The global bottleneck remains the actual contents and least clearer, the all-prime final gcd, the actual primitive denominator, and a nonzero whole error tending to zero at the same infinite original indices.



$$
\boxed{\text{The full higher-block obligation is now proved.}}
$$




$$
\boxed{\text{The complete actual physical return and the global arithmetic remain open.}}
$$




$$
\boxed{\text{No unconditional proof or disproof of irrationality of }e+\pi\text{ is obtained.}}
$$


