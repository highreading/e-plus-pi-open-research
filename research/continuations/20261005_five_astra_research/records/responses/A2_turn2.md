> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Matched $b=4$: an exact $2n+5$ factor, integral normalization, and the first genuine $7$-adic root disk

The proposed factor is real:



$$
\boxed{2n+5\ \text{divides all three raw matched-}b=4\text{ contractions}.}
$$



More strongly, it comes from an exact row identity, not from cancellation that is visible only on the scalar sequence. After removing this factor, a second, universal factor $12$ follows from a factorial-column normalization. Both divisions can be performed over the integers before any modular reduction.

I also obtain two concrete arithmetic consequences:

1. **At $7$, the complete raw contraction content is now identified exactly:**
   

$$
\boxed{v_7\!\left(\gcd(\sigma_n,\chi_n,\kappa_n)\right)
          =v_7(2n+5)\qquad(n\ge0).}
$$


   In particular, the apparent joint root $n\equiv1\pmod7$ disappears completely after the correct normalization.

2. **The remaining $7$-adic numerator root is genuine.** It is the disk
   

$$
n\equiv4\pmod7,
$$


   where no contraction content removes the zero. An exact calculation gives
   

$$
\boxed{v_7(V_n^*)=1\qquad(n\equiv4\pmod{49}),}
$$


   with $V_n^*$ formed from the actual primitive contraction triple.

These results also yield a certificate-backed exclusion of shrinking primitive forms on an explicit positive-density set of matched-$b=4$ indices. They do **not** yet exclude the entire matched-$b=4$ family.

The actual approximation domain throughout is $n\ge4$. Nonnegative indices below $4$ are used only as scalar congruence seeds.

---

## 1. A polynomial construction of the raw contractions

Write


$$
\mathscr F_n(x)=x^nH_n(x),\qquad
H_n(x)=n![z^n]e^{xz}\left(1-z+\frac{z^2}{2}\right)^n.
$$


The five scalar coordinates are


$$
(h,u,v,\mathcal A,\mathcal M)
=(H_n(1),H_n'(1),H_n''(1),\mathcal A_n,\mathcal M_n),
$$


and


$$
\mathcal B=\mathcal M+h-u.
$$



The raw determinant contractions use the three high rows


$$
R_1=(\mathscr F_{n+1}^{(j)}(1))_{j=0}^4,
$$




$$
R_2=\left(\frac{\mathscr F_{n+2}^{(j+1)}(1)}{n+2}\right)_{j=0}^4,
\qquad
R_3=\left(\frac{\mathscr F_{n+3}^{(j+2)}(1)}{n+3}\right)_{j=0}^4.
$$


The lower rows are


$$
e=(1,1,1,1,1),
$$




$$
p_j=\sum_{i=1}^j\mathscr F_n^{(i-1)}(1),
\qquad
u_j=\sum_{i=1}^j\frac{\mathscr F_{n+1}^{(i)}(1)}{n+1},
\qquad 0\le j\le4.
$$


Thus


$$
\sigma=-\det[R_1;R_2;R_3;e;u],
$$




$$
\chi=-\det[R_1;R_2;R_3;e;p],
\qquad
\kappa=\det[R_1;R_2;R_3;u;p].
\tag{1.1}
$$



Here and below, row divisions by their degree parameters are exact integer divisions.

### 1.1 Explicit finite polynomial formulas

The following gives an arithmetic-circuit specification of these polynomials over $\mathbb Z[1/2]$, without a growing determinant or a division by $n+1$.

Put $k=n+1$ and


$$
a=-nh+nu+\frac v2,\qquad
\alpha=h-u+\frac v2,\qquad
\beta=nh+u-\frac{n+2}{2}v.
$$


Then


$$
H_k(1)=a,\qquad H_k'(1)=k\alpha,\qquad H_k''(1)=k\beta.
$$



Define jets $g_d$, through the orders needed below, by


$$
g_0=a,\qquad g_1=k\alpha,\qquad g_2=k\beta,
$$




$$
g_{d+3}=-(k+d)g_{d+2}+2d\,g_{d+1}+2(k-d)g_d.
\tag{1.2}
$$


Set


$$
y_j=\sum_{a=0}^j\binom ja(k)_a g_{j-a},
\qquad 0\le j\le6.
\tag{1.3}
$$


Thus $y_j=\mathscr F_k^{(j)}(1)$.

For normalized derivatives, set


$$
\eta_1=\alpha,\qquad \eta_2=\beta,\qquad
\eta_3=2a-k\beta,
$$


and use, for $d\ge1$,


$$
\eta_{d+3}=-(k+d)\eta_{d+2}
             +2d\,\eta_{d+1}+2(k-d)\eta_d.
$$


Then, for $j\ge1$,


$$
\frac{y_j}{k}
=
\eta_j+
\sum_{a=1}^j\binom ja(k-1)_{a-1}g_{j-a}.
\tag{1.4}
$$


The right side is polynomial over $\mathbb Z[1/2]$.

The $p$-row is obtained analogously from the jets of $H_n$, starting with $h,u,v$; only derivatives through order $3$ of $\mathscr F_n$ are required. Consequently every entry of (1.1), and hence all three raw contractions, is polynomial over $\mathbb Z[1/2]$ in


$$
n,h,u,v.
$$


The complete factorial numerator contraction


$$
V=\sigma\mathcal A-\chi(\mathcal M+h-u)-\kappa
\tag{1.5}
$$


is polynomial over the same ring in all five coordinates.

The new row identity below gives substantially smaller formulas for $R_2,R_3$, and proves the common factor.

---

## 2. The exact contiguous row identity

Define differential operators


$$
T_k=
\frac{x^2}{2}D^2+x(1-x)D+x^2-x-\frac{k(k+1)}2
$$


and


$$
B_k=xD^2+(1-k-2x)D+(k-1+2x).
$$


The polynomial transition is


$$
\mathscr F_{k+1}=T_k\mathscr F_k.
\tag{2.1}
$$



The differential equation for $\mathscr F_k$ is


$$
\begin{aligned}
0={}&x^2\mathscr F_k'''
+\bigl((2-2k)x-2x^2\bigr)\mathscr F_k''\\
&+\bigl(k(k-1)+(4k-2)x+2x^2\bigr)\mathscr F_k'
-(2k^2+4kx)\mathscr F_k.
\end{aligned}
\tag{2.2}
$$


Differentiating (2.1) and using (2.2) gives


$$
\boxed{\frac{\mathscr F_{k+1}'}{k+1}=B_k\mathscr F_k.}
\tag{2.3}
$$


For example, after substituting (2.2), the coefficients of
$\mathscr F_k'',\mathscr F_k',\mathscr F_k$ in
$(T_k\mathscr F_k)'$ become respectively


$$
(k+1)x,\qquad (k+1)(1-k-2x),\qquad
(k+1)(k-1+2x).
$$



Now define


$$
\begin{aligned}
C_k={}&x(x-k-1)D^2\\
&+\bigl(k^2-1+2(k+2)x-2x^2\bigr)D\\
&-(k+1)(2k-1)-2(k+2)x+2x^2.
\end{aligned}
\tag{2.4}
$$



### Proposition 2.1 — universal row factor

For every nonnegative integer $k$,


$$
\boxed{
\frac{\mathscr F_{k+2}''}{k+2}
=(k+1)^3\mathscr F_k+(2k+3)C_k\mathscr F_k.
}
\tag{2.5}
$$



The same identity holds formally for the jet construction (1.2)–(1.3), with arbitrary initial coordinates.

### Derivation

Put $F=\mathscr F_k$, $z=B_kF$. From (2.3),


$$
\mathscr F_{k+1}'=(k+1)z.
$$


Applying (2.3) at $k+1$ and differentiating,


$$
\frac{\mathscr F_{k+2}''}{k+2}
=(k+1)(B_k^2-B_k)F+2T_kF.
\tag{2.6}
$$



Reduction of $B_k^2F-B_kF$ by (2.2) gives the three coefficients


$$
2x^2-(2k+3)x,
$$




$$
(k-1)(2k+3)+(4k+10)x-4x^2,
$$




$$
-3k^2-k+4-(4k+10)x+4x^2
$$


in front of $F'',F',F$, respectively. Substituting these into (2.6), the $F''$ and $F'$ coefficients factor immediately by $2k+3$. The constant part of the $F$-coefficient uses


$$
(k+1)(-3k^2-2k+4)
=(k+1)^3-(2k+3)(k+1)(2k-1).
$$


This is exactly (2.5).

All the reductions are polynomial identities in the parameter and the initial three jets. No evaluation at a modular root is used. ∎

### 2.1 Application to matched $b=4$

Take $k=n+1$, and write


$$
F=\mathscr F_k,\qquad z=B_kF,\qquad w=C_kF.
$$


Then


$$
R_1=(F^{(j)}(1))_{j=0}^4,\qquad
R_2=(z^{(j)}(1))_{j=0}^4,
$$


and


$$
\boxed{
R_3=(n+2)^3R_1+(2n+5)(w^{(j)}(1))_{j=0}^4.
}
\tag{2.7}
$$



Consequently,


$$
\begin{aligned}
\sigma&=(2n+5)\sigma^{[1]},\\
\chi&=(2n+5)\chi^{[1]},\\
\kappa&=(2n+5)\kappa^{[1]},
\end{aligned}
\tag{2.8}
$$


where the superscript-$[1]$ contractions are formed by replacing the third high row with the jets of $w$.

Since $F\in\mathbb Z[x]$ and $C_k$ has integer polynomial coefficients at integer $k$, $w\in\mathbb Z[x]$. Thus all three quotients in (2.8) are integers.

This proves more than divisibility inferred from the oddness of $2n+5$: it supplies an **integral replacement row**.

### 2.2 Explicit jet formulas for the replacement rows

With $y_j=F^{(j)}(1)$, and negative-index $y_j$ interpreted as zero,


$$
z_j
=y_{j+2}+(j-k-1)y_{j+1}
 +(k+1-2j)y_j+2j\,y_{j-1},
\tag{2.9}
$$


and


$$
\begin{aligned}
w_j={}&-k\,y_{j+2}
 +\bigl(j(1-k)+(k+1)^2\bigr)y_{j+1}\\
&+\bigl(j(j-1)+2kj-(k+1)(2k+1)\bigr)y_j\\
&-2j(j+k-1)y_{j-1}
 +2j(j-1)y_{j-2}.
\end{aligned}
\tag{2.10}
$$


These formulas, for $0\le j\le4$, complete the promised finite polynomial specification of the raw contractions.

A useful equivalent identity is


$$
\boxed{w=(x-1)z-xz'+(k+1)xF.}
\tag{2.11}
$$



---

## 3. A further universal factor $12$

There is another exact contraction factor, arising from all the rows together rather than from a single high row.

For a polynomial $P$, define


$$
\mathcal J(P)=
\left(
P(1),\
[t^0](P'-P)(1+t),\
[t^1](P'-P)(1+t),\
[t^2](P'-P)(1+t),\
[t^3](P'-P)(1+t)
\right).
$$


Also define


$$
\mathcal P=
\left(0,[t^0]\mathscr F_n(1+t),\ldots,[t^3]\mathscr F_n(1+t)\right),
$$




$$
\mathcal U=
\left(0,[t^0]\frac{F'(1+t)}k,\ldots,
          [t^3]\frac{F'(1+t)}k\right),
\qquad
\mathcal E=(1,0,0,0,0).
$$


Every entry is integral. In particular $F'/k\in\mathbb Z[x]$, by the derivative divisibility already supplied in the cofactor source.

Set


$$
\begin{aligned}
\widehat\sigma&=-\det[\mathcal J(F);\mathcal J(z);\mathcal J(w);
                       \mathcal E;\mathcal U],\\
\widehat\chi&=-\det[\mathcal J(F);\mathcal J(z);\mathcal J(w);
                       \mathcal E;\mathcal P],\\
\widehat\kappa&=\det[\mathcal J(F);\mathcal J(z);\mathcal J(w);
                       \mathcal U;\mathcal P].
\end{aligned}
\tag{3.1}
$$



### Proposition 3.1 — integral double normalization

For every $n\ge0$,


$$
\boxed{
(\sigma,\chi,\kappa)
=12(2n+5)(\widehat\sigma,\widehat\chi,\widehat\kappa),
}
\tag{3.2}
$$


with all three hatted contractions integral.

### Proof

After using (2.7), subtract each original column from its successor, retaining the first column. The transformation has determinant $1$.

For the last four columns, indexed by $j=0,1,2,3$, the high-row entries become


$$
(P'-P)^{(j)}(1),
$$


while the cumulative-row entries become


$$
\mathscr F_n^{(j)}(1),\qquad
(F'/k)^{(j)}(1).
$$


Every entry in such a column is divisible by $j!$. Dividing those four columns by their factorials contributes


$$
0!\,1!\,2!\,3!=12.
$$


The resulting rows are precisely those in (3.1). ∎

I do **not** assert that $12(2n+5)$ is the complete universal integer-valued content. The exact remaining contraction content is retained:


$$
d_n=\gcd(|\widehat\sigma_n|,|\widehat\chi_n|,|\widehat\kappa_n|).
\tag{3.3}
$$


Whenever the triple is nonzero,


$$
\boxed{
\gcd(|\sigma_n|,|\chi_n|,|\kappa_n|)
=12(2n+5)d_n.
}
\tag{3.4}
$$


Thus any further row, maximal-minor, or contraction content is removed by dividing the hatted triple by $d_n$. Nothing is assumed about its exhaustion by the factors already displayed.

At $n=0$, the supplied seed becomes


$$
(\widehat\sigma_0,\widehat\chi_0,\widehat\kappa_0)
=(16,-56,-8),\qquad
\widehat V_0=192.
$$


Here $d_0=8$, recovering the actual primitive seed


$$
(2,-7,-1),\qquad V_0^*=24.
$$



---

## 4. All-depth transfer after the normalization

Define


$$
\widehat V
=\widehat\sigma\mathcal A
-\widehat\chi(\mathcal M+h-u)-\widehat\kappa.
\tag{4.1}
$$



The row-factor quotient in Section 2 is polynomial over
$\mathbb Z[1/2]$ in $n$ and the scalar coordinates. The additional division by $12$ introduces at most one factor $3$ into the coefficient denominators.

Using the proved scalar transfer, one therefore obtains:

### Proposition 4.1 — normalized transfer

For every prime $p\ge5$, every $a\ge1$, and every $m,n\ge0$,


$$
m\equiv n\pmod{p^a}
\quad\Longrightarrow\quad
\begin{cases}
\widehat\sigma_m\equiv\widehat\sigma_n\pmod{p^a},\\
\widehat\chi_m\equiv\widehat\chi_n\pmod{p^a},\\
\widehat\kappa_m\equiv\widehat\kappa_n\pmod{p^a},\\
\widehat V_m\equiv\widehat V_n\pmod{p^a}.
\end{cases}
\tag{4.2}
$$



At $p=3$, a valid all-depth version is


$$
m\equiv n\pmod{3^{a+1}}
\quad\Longrightarrow\quad
(\widehat\sigma,\widehat\chi,\widehat\kappa,\widehat V)_m
\equiv
(\widehat\sigma,\widehat\chi,\widehat\kappa,\widehat V)_n
\pmod{3^a}.
\tag{4.3}
$$


No loss depending on $v_p(2n+5)$ occurs.

In particular, (4.2) is valid on the previously problematic disk


$$
n\equiv\frac{p-5}{2}\pmod p.
$$


One evaluates the polynomial replacement row there; one does not divide a zero residue by $2n+5$.

### 4.1 What transfers for the actual primitive contractions

The globally primitive triple is


$$
(\sigma_n^*,\chi_n^*,\kappa_n^*)
=d_n^{-1}(\widehat\sigma_n,\widehat\chi_n,\widehat\kappa_n).
\tag{4.4}
$$


Its exact residues need not be periodic: the prime-to-$p$ part of the global gcd can vary.

The correct invariant is local projective normalization. Put


$$
c_p(n)=\min\bigl(
v_p(\widehat\sigma_n),
v_p(\widehat\chi_n),
v_p(\widehat\kappa_n)\bigr).
$$


If $c_p(n)=c<\infty$, then sufficiently close indices have the same $c_p$, and


$$
p^{-c}
(\widehat\sigma,\widehat\chi,\widehat\kappa)
$$


transfers to the corresponding precision. The actual primitive triple differs from this by a $p$-adic unit.

In particular,


$$
\boxed{v_p(V_n^*)=v_p(\widehat V_n)-c_p(n).}
\tag{4.5}
$$


This is the content-sensitive valuation statement needed for the actual denominator.

---

## 5. The $7$-adic normalization is now complete

The joint raw root is $n\equiv1\pmod7$. We must evaluate the normalized contraction there independently of division by $2n+5$.

### 5.1 Exact calculation at the removed root

At the scalar seed $n=1$, $k=2$, the first four transformed high-row entries after the leading column are


$$
\begin{pmatrix}
-1&-4&2&4\\
11&18&-26&-16\\
-29&12&132&-4
\end{pmatrix}.
$$


The corresponding lower coefficient rows are


$$
\mathcal U_{\rm tail}=(0,-2,0,2),\qquad
\mathcal P_{\rm tail}=(0,1,1,0).
$$


The leading high entries are $1,-1,-7$. These determinants give


$$
\boxed{
(\widehat\sigma_1,\widehat\chi_1,\widehat\kappa_1)
=(-360,1128,888).
}
\tag{5.1}
$$


Since $\mathcal A_1=3$, $\mathcal B_1=10$,


$$
\boxed{\widehat V_1=-13248\equiv3\pmod7.}
\tag{5.2}
$$


Thus the apparent raw numerator root at $1\pmod7$ is entirely a common-factor artifact.

Using (5.2) at $r=1$, and dividing the supplied raw residues by the units $12(2r+5)$ at the other six residues, gives


$$
\boxed{
(\widehat V_0,\ldots,\widehat V_6)
\equiv(3,3,4,6,0,4,6)\pmod7.
}
\tag{5.3}
$$


The normalized contraction triple has no joint zero modulo $7$: outside $r=1$ this follows from the supplied raw joint-zero set, and at $r=1$ it follows from (5.1).

Therefore, by normalized transfer,


$$
\boxed{c_7(n)=0\qquad(n\ge0).}
\tag{5.4}
$$


Combining (3.4) and (5.4),


$$
\boxed{
v_7\!\left(\gcd(|\sigma_n|,|\chi_n|,|\kappa_n|)\right)
=v_7(2n+5).
}
\tag{5.5}
$$



This also proves that the three high rows have rank $3$ over $\mathbb Q$ at every scalar index $n\ge0$: a nonzero contraction determinant exists at every index. It does not by itself prove that the matched endpoint $D_n^*$ is nonzero.

### 5.2 The surviving numerator-root disk

At $r=4$, the normalized triple is


$$
(\widehat\sigma,\widehat\chi,\widehat\kappa)
\equiv(6,6,6)\pmod7,
\qquad \widehat V\equiv0\pmod7.
\tag{5.6}
$$


Thus the zero cannot disappear under contraction-content removal.

We can go one depth further exactly.

At $n=4$,


$$
\mathcal A_4=13293,\qquad
\mathcal M_4=144818,\qquad
\mathcal B_4=144955,
$$


so


$$
\mathcal A_4\equiv14,\qquad
\mathcal B_4\equiv13\pmod{49}.
$$



The transformed high rows modulo $49$, including their leading entries, are


$$
\begin{pmatrix}
45&8&5&41&42\\
10&44&8&21&27\\
20&21&39&20&20
\end{pmatrix}.
$$


The lower rows are


$$
\mathcal U=(0,40,41,14,0),\qquad
\mathcal P=(0,45,39,5,28).
$$


Direct determinants give


$$
\boxed{
(\widehat\sigma_4,\widehat\chi_4,\widehat\kappa_4)
\equiv(41,20,48)\pmod{49}.
}
\tag{5.7}
$$


For example, the last-row cofactor vector of the four tail columns is


$$
(44,39,43,43)\pmod{49};
$$


its scalar products with the two lower tail rows give $41$ and $20$.

Consequently,


$$
\widehat V_4
\equiv41\cdot14-20\cdot13-48
\equiv21\pmod{49}.
\tag{5.8}
$$


Normalized transfer and (5.4) now prove


$$
\boxed{
v_7(V_n^*)=1
\qquad\text{for every }n\ge0\text{ with }n\equiv4\pmod{49}.
}
\tag{5.9}
$$



This characterizes one entire depth-two subdisk of the first genuine root disk. The other six lifts


$$
11,18,25,32,39,46\pmod{49}
$$


have not been evaluated here.

---

## 6. The complete endpoint quotient and the final gcd

Let $\mathsf P_j=L_j(1)$ and $w_j$ denote the integer-L endpoint and rational second-kind endpoint from the supplied cofactor reduction.

Using the **primitive** contractions (4.4), define


$$
D_n^*=(n+1)\mathsf P_{n+1}\chi_n^*
          -2\mathsf P_n\sigma_n^*,
$$




$$
Q_n^*=2w_n\sigma_n^*
          -(n+1)w_{n+1}\chi_n^*,
$$




$$
V_n^*=\sigma_n^*\mathcal A_n
          -\chi_n^*\mathcal B_n-\kappa_n^*.
\tag{6.1}
$$


The exact endpoint quotient is


$$
\boxed{
\frac{X_n}{Y_n}
=
\frac{Q_n^*+\dfrac{2^{n+1}}{(n!)^2}V_n^*}{D_n^*},
\qquad n\ge4,\quad D_n^*\ne0.
}
\tag{6.2}
$$


Both $Q_n^*$ and the $-\kappa_n^*$ term are retained.

For example, take the valid clearer


$$
\lambda_n=
\operatorname{lcm}\!\left(
(n!)^2,\,
2^n\operatorname{lcm}(1,\ldots,n+1)
\right).
$$


Set


$$
N_n=\lambda_n\left(
Q_n^*+\frac{2^{n+1}}{(n!)^2}V_n^*
\right),\qquad
Z_n=\lambda_nD_n^*,
$$




$$
g_n=\gcd(|N_n|,|Z_n|).
\tag{6.3}
$$


Then the actual primitive rational center is


$$
c_n=-\frac{X_n}{Y_n}=\frac{p_n}{q_n},
$$


with


$$
\boxed{
q_n=\frac{|Z_n|}{g_n},\qquad
p_n=-\operatorname{sign}(Z_n)\frac{N_n}{g_n}.
}
\tag{6.4}
$$


The endpoint gcd $g_n$ is distinct from the contraction gcd $d_n$.

At an odd prime $p$, put


$$
F_p=v_p(n!),\qquad \ell_p=\lfloor\log_p(n+1)\rfloor.
$$


The moment denominator bound gives


$$
v_p(Q_n^*)\ge-\ell_p.
$$


If $b=v_p(V_n^*)<\infty$ and


$$
2F_p-b>\ell_p,
\tag{6.5}
$$


then the two terms in the **whole** numerator of (6.2) have distinct valuations:


$$
v_p\!\left(
Q_n^*+\frac{2^{n+1}}{(n!)^2}V_n^*
\right)=b-2F_p.
$$


In particular, that numerator is nonzero, and actual reduction yields


$$
\boxed{
v_p(q_n)=2F_p+v_p(D_n^*)-b
\ge2F_p-b.
}
\tag{6.6}
$$



Where (6.5) is not proved, the exact gate remains


$$
\mathcal R_{n,p}^*
=V_n^*+\frac{(n!)^2}{2^{n+1}}Q_n^*,
$$




$$
\boxed{
v_p(q_n)=
\max\{0,\;2F_p+v_p(D_n^*)-v_p(\mathcal R_{n,p}^*)\},
}
\tag{6.7}
$$


provided the complete numerator is nonzero. No assertion about a factorial clearer replaces this final-gcd calculation.

---

## 7. A scoped matched-$b=4$ exclusion

The normalization already allows a nontrivial all-index conclusion on a specified set of residue classes.

Let $\mathcal T$ be the set of nonnegative integers satisfying:

- at $7$,
  

$$
n\not\equiv4\pmod7
  \quad\text{or}\quad
  n\equiv4\pmod{49};
$$


- at the other seven primes, avoid the following supplied raw $V$-zero sets:
  

$$
\begin{array}{c|l}
  p&\text{excluded residues}\\ \hline
  19&4,7\\
  31&13,20\\
  61&7,17,28,57\\
  71&33\\
  73&22,34,47\\
  83&39\\
  101&38,48,77.
  \end{array}
  \tag{7.1}
$$



At $7$, Sections 5.1–5.2 prove $v_7(V_n^*)\le1$ on this set. At every other listed prime, a raw unit is necessarily also a primitive unit.

For $n\in\mathcal T$, $n\ge101$, and $D_n^*\ne0$, the complete-numerator separation therefore gives


$$
q_n\ge
7^{\,2v_7(n!)-1}
\prod_{p\in\{19,31,61,71,73,83,101\}}
p^{\,2v_p(n!)}.
\tag{7.2}
$$


Thus


$$
\log q_n\ge W_8n-O(\log n)
\qquad(n\in\mathcal T).
\tag{7.3}
$$



The set $\mathcal T$ has the explicit positive natural density


$$
\boxed{
\frac{43}{49}\,
\frac{17}{19}\,
\frac{29}{31}\,
\frac{57}{61}\,
\frac{70}{71}\,
\frac{70}{73}\,
\frac{82}{83}\,
\frac{98}{101}.
}
\tag{7.4}
$$


Here $43/49$ counts the $42$ classes not equal to $4\pmod7$, plus the certified class $4\pmod{49}$.

The inherited fixed-$b$ theorem, used now at $b=4$, gives eventual $D_n^*\ne0$ and the nonzero whole evaluated error


$$
e+\pi-c_n
=(-1)^n\epsilon_n(\sqrt2-1)^4(1+o(1)),
\qquad
\log\epsilon_n=-\tau n+o(n).
\tag{7.5}
$$


Therefore the actual primitive form


$$
L_n=q_n(e+\pi)-p_n
$$


satisfies


$$
\boxed{
\liminf_{\substack{n\to\infty\\n\in\mathcal T}}
\frac{\log|L_n|}{n}
\ge W_8-\tau>0.02.
}
\tag{7.6}
$$



This is a **scoped matched-$b=4$ exclusion**: shrinking primitive forms cannot occur along an unbounded-index subsequence contained in $\mathcal T$. It is not an exclusion of all matched-$b=4$ indices.

Its dependencies are explicit: the newly proved normalization and transfer, the supplied finite $b=4$ residue table outside the hand-checked $7$-adic repairs, and the inherited fixed-$b=4$ whole-error theorem. I have not independently regenerated the entire supplied $b=4$ table.

---

# Required concluding ledger

## (1) New result and proof status

**Paper-level proved here:**

- The exact differential row identity
  

$$
R_3=(n+2)^3R_1+(2n+5)R_{\mathrm{new}},
$$


  with an integral replacement row.
- Consequently, exact polynomial divisibility of all three raw contractions by $2n+5$.
- A further universal integral contraction factor $12$, with an explicit factorial-column normalization.
- All-depth transfer for these normalized quantities at every $p\ge5$, including the modular root $n=(p-5)/2$; a safe one-digit-loss version at $3$.
- The correct local-projective transfer statement for the actual primitive contractions, rather than an unjustified periodicity claim for the global gcd normalization.
- At $7$, exact raw contraction-content depth
  

$$
v_7(\gcd(\sigma_n,\chi_n,\kappa_n))=v_7(2n+5).
$$


- The genuine normalized numerator-root disk $n\equiv4\pmod7$, and the exact valuation
  

$$
v_7(V_n^*)=1\quad(n\equiv4\pmod{49}).
$$



**Certificate-backed consequence with inherited analytic dependency:**

- The positive-density scoped matched-$b=4$ exclusion (7.6), retaining the actual primitive denominator, final endpoint gcd, complete numerator, whole evaluated error, index domain, and eventual nonvanishing.

The factor $12(2n+5)$ is proved universal; it is **not claimed maximal**. All further evaluated contraction content remains in $d_n$.

## (2) Exact remaining bottleneck

For a full matched-$b=4$ exclusion, the unresolved arithmetic is now narrower:

1. Evaluate the normalized contractions at the seven remaining common-factor roots
   

$$
r_p=(p-5)/2,\qquad
   p\in\{19,31,61,71,73,83,101\}.
$$


   These must be evaluated through the replacement row, not by dividing raw zero residues.

2. Resolve the surviving primitive numerator-root disks. In particular, the $7$-adic disk $4+7\mathbb Z_7$ is not a content artifact.

3. If a root disk persists at arbitrarily high depth, one still needs a quantitative bound on
   

$$
v_p(V_n^*)-v_p(D_n^*)
$$


   along ordinary integer indices—or, when separation fails, on the complete expression (6.7). A persistent $p$-adic root alone supplies neither a favorable denominator bound nor an exclusion.

No main irrationality decision has been obtained.

## (3) Bounded exact computation request

I request the following fixed computations for the coordinator’s consideration; no execution is presumed.

### A. Symbolic common-factor check

**Inputs:** the polynomial circuit (1.2)–(1.4), (2.9)–(2.10), and determinants (3.1).

**Expected output:**

- The gcd over $\mathbb Q[n,h,u,v]$ of
  

$$
\widehat\sigma,\widehat\chi,\widehat\kappa,
$$


  with exact factor/recomposition checks.
- Any further common polynomial factor, kept separate from numerical coefficient content and from integer-valued content along the actual scalar sequence.

This is a bounded factorization of three fixed polynomials, not a degree or prime search.

### B. Targeted prime-square root-disk certificate

For exactly


$$
\{7,19,31,61,71,73,83,101\},
$$


and for each raw $V$-zero residue $r$ in the supplied table, evaluate


$$
(\widehat\sigma_n,\widehat\chi_n,\widehat\kappa_n,\widehat V_n)
\pmod{p^2}
$$


at


$$
n=r+pj,\qquad 0\le j<p.
$$



This is exactly


$$
14+38+62+244+71+219+83+303
=\boxed{1034}
$$


targeted residue rows. No additional primes or residue disks are requested.

**Expected verifiable output:**

- All normalized rows, obtained using the integral replacement-row construction.
- Each normalized joint-zero set and numerator-zero set, separately.
- The normalized value at every common-factor root $r_p$.
- For the $7$-adic control, confirmation of
  

$$
(\widehat\sigma_4,\widehat\chi_4,\widehat\kappa_4,\widehat V_4)
  \equiv(41,20,48,21)\pmod{49}.
$$


- For every disk, either a bounded primitive valuation certificate or the exact list of surviving depth-two root disks.

An empty surviving numerator-zero set modulo $p^2$, together with control of normalized contraction content, would prove an all-index bounded-valuation lemma through the transfer above. A surviving disk would instead identify the precise next local obligation; it would not be extrapolated into an infinite valuation assertion.
