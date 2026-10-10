> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Mixed finite-jet arithmetic for the compact construction

## 1. Summary and proof status

The attached work does not decide whether $e+\pi$ is rational or irrational. This report also does not decide that question.

The specific uniform arithmetic requested in this turn remains open:



$$
\operatorname{rank}_{\mathbb F_p}Z_k=2k-1,
\qquad
\operatorname{rank}_{\mathbb F_p}Y_k=2k-1
\qquad(p>6k-4),
\tag{1.1}
$$


or, alternatively, an evaluated bound


$$
\log\mathscr R_k+\log\mathscr L_k
\le (4-\eta)k^2\log k+O(k^2)
\tag{1.2}
$$


with some fixed $\eta>0$, at the original indices


$$
k=K_u=9^{18+32u}.
$$



There are nevertheless three new, proved developments.

1. **A complete finite-jet differential reduction.**  
   The actual mixed arrays are transformed, using explicitly paid triangular operations, into integer coefficient arrays of rational functions. The construction retains the contact atom, factorial forcing, arctangent forcing, and every product-rule commutator. It uses no characteristic-$p$ arctangent series beyond the paid original prefix.

2. **An evaluated mixed pole obstruction.**  
   A nonzero mixed relation in $Z_k$ necessarily produces a nonzero polynomial of explicitly bounded degree. If the first nonzero return coefficient is $v_t$, an explicitly evaluated principal-part coefficient is
   

$$
-v_t(2t+1)!(6k-7-2t)!,
   \tag{1.3}
$$


   which is a unit times $v_t$ at every $p>6k-4$. This is a genuine obstruction involving the complete mixed system, not just $U_k$ or $[T,V]$.

   The obstruction does **not** yet rule out the relation: the polynomial degree left after imposing the physical finite prefix is still large. The exact remaining degree gap is identified below.

3. **An exact all-prime height-payment theorem.**  
   Let $\mathscr C_{Z,k},\mathscr C_{Y,k}$ be the actual maximal-minor contents of the two new integer coefficient arrays. Then
   

$$
\boxed{
   \log\mathscr R_k+\log\mathscr L_k
   =
   \log\mathscr C_{Z,k}+\log\mathscr C_{Y,k}
   -8k^2\log k+O(k^2).
   }
   \tag{1.4}
$$


   More importantly, Section 7 gives exact identities before taking logarithms, including the actual simultaneous clearer of the transformed primitive cofactor vector and the remaining all-prime column-content correction.

Thus a quantitatively sufficient follow-on statement is now explicit: a proved bound


$$
\log\mathscr C_{Z,k}+\log\mathscr C_{Y,k}
\le (12-\eta)k^2\log k+O(k^2)
\tag{1.5}
$$


would imply the requested bound (1.2). No such estimate is proved here.

A small new exact calculation also shows why an apparently innocuous interpolation step cannot be treated as a unit operation: a relevant even-factorial interpolation determinant has the large prime factor $149$. At the same auxiliary $k=3,p=149$, however, the **actual mixed** arrays have explicitly exhibited unit maximal minors. This is a finite check, not a uniform theorem.

---

## 2. Original objects and normalization

Throughout,


$$
k\ge2,\qquad 0\le m<2k,\qquad 0\le j<k.
$$



Retain


$$
a_0=1,\qquad a_d=1-da_{d-1},
$$




$$
u_n=a_{2n},\qquad f_n=(2n)!,\qquad w_n=(-1)^n,
$$




$$
c_n=u_n-w_n,
$$


and


$$
\rho_0=0,\qquad
\rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad
r_n=-f_n+4\rho_n.
$$



The complete returns are


$$
\sigma_n=c_{n+1}+c_n=u_{n+1}+u_n,
$$




$$
\boxed{
\tau_n=r_{n+1}+r_n
=-(2n+2)!-(2n)!+\frac4{2n+1}.
}
\tag{2.1}
$$



Put


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5).
$$


The original affine determinant is


$$
H_k(s)=
\det\left[
(c_{m+j})\ \middle|\
\bigl(\Lambda_k(r_{m+j}+s(-1)^{m+j})\bigr)
\right]
=H_{0,k}+H_{1,k}s.
\tag{2.2}
$$



Its physical terminal remains


$$
m+j=3k-2,\qquad (6k-4)!,\qquad 6k-5.
\tag{2.3}
$$



Whenever $H_{1,k}\ne0$, the actual normalization is


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
$$




$$
q_k=\frac{|H_{1,k}|}{G_k},
\qquad
p_k=-\frac{\operatorname{sgn}(H_{1,k})H_{0,k}}{G_k}.
\tag{2.4}
$$



In particular,


$$
\boxed{
\ell_k=q_k(e+\pi)-p_k
=\frac{|H_k(e+\pi)|}{G_k}.
}
\tag{2.5}
$$



No known lower divisor of $G_k$ is substituted for $G_k$.

The two actual rectangles are


$$
Z_k=
\left[
(c_{m+j})_{\substack{m<2k\\j<k}}
\ \middle|\
(\Lambda_k\tau_{m+j})_{\substack{m<2k\\j<k-1}}
\right],
$$




$$
Y_k=
\left[
(\sigma_{m+j})_{\substack{m<2k-1\\j<k}}
\ \middle|\
(\Lambda_k\tau_{m+j})_{\substack{m<2k-1\\j<k}}
\right],
\tag{2.6}
$$


with


$$
\mathscr R_k=\delta_{2k-1}(Z_k),
\qquad
\mathscr L_k=\delta_{2k-1}(Y_k).
$$



The established bordered-content theorem is reused at its stated nonvanishing scope:


$$
\boxed{
\operatorname{lcm}(\mathscr R_k,\mathscr L_k)
\mid G_k
\mid\Lambda_k\mathscr R_k\mathscr L_k.
}
\tag{2.7}
$$


Consequently, for $p>6k-4$,


$$
p\nmid G_k
\iff
Z_k,\ Y_k
\text{ both have their full possible rank modulo }p.
\tag{2.8}
$$



The original infinite set remains


$$
\mathcal O=\{9^{18+32u}:u\ge0\}.
\tag{2.9}
$$



---

## 3. What the new receipts establish—and what they do not

### 3.1 Closed $11\to12$ scalar splitting

The two new Bézout-certified gcds are both $1$. Applying the already proved paid-transfer splitting theorem therefore gives


$$
C_{11}\mid q_{11},
\qquad
A_{11}\mid q_{12},
\tag{3.1}
$$


where $C_{11}$ is the complete 566-digit residual factor of $\chi_{11}$, and $A_{11}$ is the complete 691-digit residual factor of $\alpha_{11}$.

These conclusions concern the actual primitive denominators. Neither residual is assumed prime.

The scope is exactly auxiliary $k=11,12$. The calculations exclude these particular residuals from the corresponding actual final contents. They do not exclude every large prime from $G_{11}$ or $G_{12}$, and they imply no growing-index estimate.

No determinant or Smith calculation from that receipt is repeated.

### 3.2 Closed two-rectangle receipt at $k=5$

The supplied maximal minors and Bézout certificates give the all-prime contents


$$
\mathscr R_5=2^{40}3^2 5^3 23^2,
$$




$$
\mathscr L_5=2^{46}3^2 5^3 23^2=64\mathscr R_5,
$$




$$
G_5=2^{50}3^3 5^4\,19\,23^3.
\tag{3.2}
$$



Thus both mixed arrays are saturated at every prime $p>26$, at this one index.

The sign and scalar agree with the original ordering:


$$
H_{1,5}=-\Lambda_5D,
\qquad
H_{0,5}=\Lambda_5D+\text{cross\_L}.
\tag{3.3}
$$


The actual primitive denominator is still $|H_{1,5}|/G_5$.

One further finite normalization deduction is immediate without any new determinant. Since


$$
\Lambda_5=3^3 5^2\,7\,11\,13\,17\,19\,23,
$$


the actual common divisor used to clear $H_5/\Lambda_5^5$ is


$$
d_{H,5}
=\gcd(\Lambda_5^5,H_{0,5},H_{1,5})
=3^3 5^4\,19\,23^3.
$$


Hence its actual least simultaneous coefficient clearer is


$$
\boxed{
\frac{\Lambda_5^5}{3^3 5^4\,19\,23^3},
}
\tag{3.4}
$$


and the remaining coefficient content is $2^{50}$.

The old $C_5$ Smith table and its actual monic-row clearer


$$
15285836938599813
$$


are reused, not recomputed. That nonunit frame clearer is not silently removed.

### 3.3 Other established payments

The following remain in force:

- the actual individual right-column clearer
  

$$
\Lambda_{k,j}
  =\operatorname{lcm}(1,3,\ldots,4k+2j-3);
$$


- the complete return array’s actual least clearer $\Lambda_k$;
- the transformed contact-column contents $2^{\max(1,j)}$;
- the actual denominator $n!$ in $b_n/n!$;
- the known product divisor
  

$$
E_k\,2^{k(k-1)}
  \prod_{r=0}^{k-2}(r!)^2\mid G_k.
$$



These are payments and lower divisors, not substitutes for the final gcd.

---

## 4. A finite Laurent interface with complete forcing

It is convenient to replace the variable $z$ by $x^{-2}$. Work first over $\mathbb Q$, and write


$$
\mathfrak f(x)=\sum_{n\ge0}f_nx^{-2n-1},
\qquad
\mathfrak u(x)=\sum_{n\ge0}u_nx^{-2n-1},
$$




$$
\mathfrak b(x)=\sum_{n\ge0}\frac{x^{-2n-1}}{2n+1}.
$$



Let $D=d/dx$ and $L_0=D^2-1$. The exact equations are


$$
\boxed{
L_0\mathfrak f=-\frac1x,
\qquad
L_0\mathfrak u=\frac{x(3-x^2)}{(x^2-1)^2},
\qquad
D\mathfrak b=-\frac1{x^2-1}.
}
\tag{4.1}
$$



For example,


$$
u_n=(2n)(2n-1)u_{n-1}-(2n-1)
$$


gives


$$
L_0\mathfrak u
=-\frac1x+\sum_{n\ge1}(2n-1)x^{-2n-1}
=\frac{x(3-x^2)}{(x^2-1)^2}.
$$



The complete contact and return functions are


$$
\boxed{
\mathfrak c=\mathfrak u-\frac{x}{x^2+1},
}
$$




$$
\boxed{
\mathfrak t=-(x^2+1)\mathfrak f+x+4\mathfrak b,
\qquad
\mathfrak s=(x^2+1)\mathfrak u-x.
}
\tag{4.2}
$$



Their coefficients are respectively $c_n,\tau_n,\sigma_n$. In particular, the atom at $x^2=-1$ is visible in $\mathfrak c$, and the arctangent contribution is visible in $\mathfrak t$.

### 4.1 Characteristic-$p$ scope

Equations (4.1) are used over $\mathbb Q$ to produce rational functions. Only the required finite coefficient jets are then reduced modulo $p$.

This is essential. There is no assertion that


$$
\sum_{n\ge0}\frac{x^{-2n-1}}{2n+1}
$$


is a full Laurent series over $\mathbb F_p$. Its coefficient at $2n+1=p$ is undefined.

For the actual mixed arrays, the largest arctangent denominator used is $6k-5$. All relevant coefficients can therefore be reduced at $p>6k-4$. The high differential orders used below do not introduce new moments: differentiation only moves existing Laurent coefficients farther toward negative powers.

---

## 5. New mixed pole obstruction for $Z_k$

### 5.1 The complete rational reduction

Let


$$
X(t)=\sum_{j=0}^{k-1}x_jt^j,
\qquad
V(t)=\sum_{j=0}^{k-2}v_jt^j.
$$


Define


$$
\Phi_Z(x)=X(x^2)\mathfrak c(x)+V(x^2)\mathfrak t(x).
\tag{5.1}
$$



The negative Laurent coefficient at $x^{-2m-1}$ is


$$
a_m=\sum_{j<k}x_jc_{m+j}
+\sum_{j<k-1}v_j\tau_{m+j}.
\tag{5.2}
$$


Thus a right relation in the raw version of $Z_k$ is exactly


$$
a_0=\cdots=a_{2k-1}=0.
$$



Put


$$
d=2k-2,\qquad e=2k-4,\qquad h=2k-3,\qquad N=6k-5,
$$


and


$$
K_Z=D^hL_0^{d+1}.
\tag{5.3}
$$



For $0\le a\le d$, define the explicitly known polynomial


$$
P_{d,a}(T)=
\frac{1}{T^2-1}
\frac{d^a}{dT^a}(T^2-1)^{d+1}\in\mathbb Z[T].
\tag{5.4}
$$


The divisibility follows because the numerator still contains
$(T^2-1)^{d+1-a}$.

For a polynomial $A$ of degree at most $d$, the full product rule gives


$$
L_0^{d+1}(A\mathfrak u)
=
\sum_{a=0}^{d}
\frac{A^{(a)}}{a!}\,
P_{d,a}(D)
\frac{x(3-x^2)}{(x^2-1)^2}.
\tag{5.5}
$$


There is an identical formula for $A\mathfrak f$, with forcing $-1/x$.

Every $a\ge1$ term in (5.5) is a product-rule commutator. None is omitted. Also, $A^{(a)}/a!$ is an integral polynomial when $A$ is integral; this notation does not conceal a nonintegral normalization.

Set


$$
A=X(x^2),\qquad
D_0=-(x^2+1)V(x^2),\qquad
\xi=X(-1).
$$


Write


$$
Q_X(t)=\frac{X(t)-X(-1)}{t+1}.
$$


Then


$$
\Phi_Z
=A\mathfrak u+D_0\mathfrak f+4V(x^2)\mathfrak b
+xV(x^2)-xQ_X(x^2)-\xi\frac{x}{x^2+1}.
$$



Consequently $K_Z\Phi_Z$ is the following completely specified rational function:


$$
\begin{aligned}
\mathcal R_Z={}&
D^h\sum_{a=0}^{d}
\left[
\frac{A^{(a)}}{a!}P_{d,a}(D)
 \frac{x(3-x^2)}{(x^2-1)^2}
+
\frac{D_0^{(a)}}{a!}P_{d,a}(D)
 \left(-\frac1x\right)
\right]\\
&+
4L_0^{d+1}
\sum_{a=0}^{e}
\binom ha
\bigl(V(x^2)\bigr)^{(a)}
D^{h-a-1}\left(-\frac1{x^2-1}\right)\\
&-\xi K_Z\left(\frac{x}{x^2+1}\right)
+h!\,(x_{k-1}-v_{k-2}).
\end{aligned}
\tag{5.6}
$$



The last constant is the evaluated polynomial contribution. It follows from


$$
D^h\bigl(xV(x^2)-xQ_X(x^2)\bigr)
=h!(v_{k-2}-x_{k-1})
$$


and the fact that $d+1$ is odd.

Thus (5.6) retains:

- the factorial endpoint forcing $-1/x$;
- the complete arctangent forcing $-1/(x^2-1)$;
- the contact atom at $x^2=-1$;
- all commutators;
- the polynomial endpoint contribution.

### 5.2 Evaluated pole and degree bounds

The poles of $\mathcal R_Z$ have orders at most

- $N-1$ at $x=0$;
- $N$ at $x=1,-1$;
- $N+1$ at the roots of $x^2+1$.

Hence


$$
Q_Z(x)=x^{N-1}(x^2-1)^N(x^2+1)^{N+1}
\tag{5.7}
$$


clears the denominator. Its degree is $30k-24$.

Because $c_0=0$, $c_1=2$, and $\tau_0=1$, the polynomial part of $\Phi_Z$ has degree at most $2k-5<h$. It is killed by $K_Z$. The resulting rational function is even and begins at order $x^{-(2k-2)}$.

There is therefore an integer polynomial


$$
\mathcal P_{Z,k}(t;X,V)
$$


such that


$$
Q_Z(x)\mathcal R_Z(x)=\mathcal P_{Z,k}(x^2;X,V),
$$


with


$$
\boxed{\deg_t\mathcal P_{Z,k}\le14k-11.}
\tag{5.8}
$$



If the actual $2k$ mixed relations (5.2) hold, then


$$
\mathcal R_Z=O(x^{-(6k-2)}),
$$


and hence


$$
\boxed{\deg_t\mathcal P_{Z,k}\le12k-11.}
\tag{5.9}
$$



### 5.3 A nonzero evaluated coefficient

Assume $V\ne0$, and let $v_t$ be its first nonzero coefficient.

Near $x=0$, a local solution of


$$
L_0\mathfrak f=-1/x
$$


has logarithmic part


$$
-x\log x+O(x^3\log x).
$$


The homogeneous ambiguity is analytic and is annihilated after multiplication by $D_0$ and application of $K_Z$.

Since


$$
D_0=-v_tx^{2t}+O(x^{2t+2}),
$$


the leading logarithmic term in $D_0\mathfrak f$ is


$$
v_tx^{2t+1}\log x.
$$


The highest derivative in $K_Z$ is $D^N$. Using


$$
D^N(x^a\log x)
=(-1)^{N-a-1}a!(N-a-1)!\,x^{a-N}
\qquad(N>a),
$$


the coefficient of the pole of order $N-2t-1$ is


$$
\boxed{
-v_t(2t+1)!(N-2t-2)!
=-v_t(2t+1)!(6k-7-2t)!.
}
\tag{5.10}
$$



All other parts of (5.6) are regular at $0$. Thus this pole cannot cancel.

At $p>6k-4$, both factorials in (5.10) are units. Therefore $V\ne0$ implies $\mathcal R_Z\ne0$ modulo $p$.

If $V=0$ and $X\ne0$, use the pole at $x=1$. The local logarithmic coefficient of $\mathfrak u$ is


$$
-\frac12e^{x-1}.
$$


If $A=X(x^2)$ has zero order $v$ at $1$, then the highest remaining pole has a nonzero coefficient proportional to


$$
\frac12 A_v\,v!(N-v-1)!.
$$


Here $A_v\ne0$, $v\le d$, and all displayed divisors and factorials are units at $p>6k-4$. The atom is regular at $x=1$.

We have proved:

> **Mixed pole-obstruction theorem.**  
> For $p>6k-4$, every nonzero pair $(X,V)$ produces a nonzero rational function $\mathcal R_Z$, and hence a nonzero polynomial $\mathcal P_{Z,k}$. If it is an actual relation in $Z_k$, that nonzero polynomial must have degree at most $12k-11$, rather than its a priori bound $14k-11$.

The theorem is uniform and uses the actual mixed forcing. It is not a saturation theorem: the degree bound $12k-11$ is still positive and large.

---

## 6. Exact finite-jet equivalence, including $Y_k$

### 6.1 The triangular jet matrix

Expanding $K_Z$ at infinity gives an explicit formula for the first $2k$ output coefficients:


$$
b_m
=
\sum_{j=0}^{\min(2k-1,m)}
(-1)^j\binom{2k-1}{j}
(2m-2j+1)_{h+2j}\,a_{m-j},
\tag{6.1}
$$


where $h=2k-3$ and $(a)_r=a(a+1)\cdots(a+r-1)$.

Factor


$$
(2m-2j+1)_{h+2j}
=
(2m+1)_h\,\frac{(2m)!}{(2m-2j)!}.
$$


Thus


$$
T_Z=D_ZS_Z,
\tag{6.2}
$$


where


$$
(D_Z)_{mm}=A^Z_m=(2m+1)_{2k-3},
$$


and $S_Z$ is an integer unit lower-triangular matrix.

The largest factor in any $A^Z_m$, for $m<2k$, is $6k-5$. Therefore every diagonal entry is a unit at $p>6k-4$, and


$$
a_0=\cdots=a_{2k-1}=0
\iff
b_0=\cdots=b_{2k-1}=0.
\tag{6.3}
$$



This proves finite-jet equivalence without extending $\mathfrak b$ modulo $p$.

The corresponding coefficient array, denoted $\mathbf J_{Z,k}$, is an integer $2k$ by $2k-1$ matrix. Its columns are obtained by taking the standard coefficient pairs $(X,V)$ in (5.6).

Integrality also follows directly from (6.1): each odd denominator in a shifted $\tau$-entry lies among the factors already present in the displayed rising factorial.

### 6.2 The $Y_k$ interface

For


$$
X(t),V(t)\quad\text{of degree at most }k-1,
$$


put


$$
\Phi_Y=X(x^2)\mathfrak s+V(x^2)\mathfrak t.
$$


Here


$$
\Phi_Y
=(x^2+1)X(x^2)\mathfrak u
-(x^2+1)V(x^2)\mathfrak f
+4V(x^2)\mathfrak b+x(V-X)(x^2).
\tag{6.4}
$$



The atom cancels here for the legitimate reason
$\sigma_n=c_{n+1}+c_n$; it has not been deleted from the original contact system.

Take


$$
d_Y=2k,\qquad h_Y=2k-1,\qquad N_Y=6k+1,
\qquad K_Y=D^{h_Y}L_0^{d_Y+1}.
$$


The same full product-rule construction makes $K_Y\Phi_Y$ rational. A denominator is


$$
Q_Y=x^{N_Y-1}(x^2-1)^{N_Y}.
$$


The numerator is even, and its polynomial in $t=x^2$ has degree at most


$$
8k+1.
$$


A right relation in the actual $Y_k$ forces its degree down to at most


$$
6k+2.
\tag{6.5}
$$



The physical jet transformation is


$$
T_Y=D_YS_Y,
$$


with $S_Y$ integer unit lower triangular and


$$
(D_Y)_{mm}=A^Y_m=(2m+1)_{2k-1},
\qquad 0\le m<2k-1.
\tag{6.6}
$$


Again, every factor is at most $6k-5$. Thus the jet transformation is a $p$-adic unit transformation at every original prime $p>6k-4$.

It produces an integer $(2k-1)$ by $2k$ array $\mathbf J_{Y,k}$.

### 6.3 A real characteristic-$p$ boundary issue

For the *full rational-function injectivity proof* for $Y_k$, the largest factorial appearing in a pole coefficient can reach $(6k-1)!$. Thus the proof is immediately valid for $p>6k$, but not automatically at the possible prime $p=6k-1$.

That exception cannot be discarded.

There is a paid way to retain a nonzero obstruction in the rank-deficient case. If $Y_k$ has rank below $2k-1$, its right kernel has dimension at least two. One may choose a nonzero relation with


$$
v_{k-1}=0.
$$


For that relation use


$$
h_-=2k-3,\qquad
K_-=D^{h_-}L_0^{2k+1},
\qquad N_-=6k-1.
$$


The polynomial part of $\Phi_Y$ contributes exactly


$$
-2h_-!x_{k-1}
$$


after applying $K_-$. Therefore


$$
K_-\Phi_Y+2h_-!x_{k-1}
\tag{6.7}
$$


is the proper rational obstruction to use.

Its pole coefficients require factorials only through $(6k-2)!$, which are units even at $p=6k-1$. The same pole argument proves it nonzero for a nonzero chosen pair. Its numerator polynomial has a priori degree at most $8k-1$, and the physical relations force degree at most $6k$.

This handles the boundary prime honestly. It does not prove that the necessary low-degree obstruction is impossible.

---

## 7. New exact all-prime content-payment theorem

The finite-jet arrays give an arithmetic reduction, not merely a field-rank reformulation.

Define their actual contents


$$
\mathscr C_{Z,k}=\delta_{2k-1}(\mathbf J_{Z,k}),
\qquad
\mathscr C_{Y,k}=\delta_{2k-1}(\mathbf J_{Y,k}).
$$



Put


$$
t_Z=\prod_{m=0}^{2k-1}(2m+1)_{2k-3},
\qquad
t_Y=\prod_{m=0}^{2k-2}(2m+1)_{2k-1}.
\tag{7.1}
$$



All prime factors of these two payments are at most $6k-5$.

### 7.1 The actual cofactor clearer for $Z_k$

Let $\mathbf v\in\mathbb Z^{2k}$ be the primitive signed cofactor vector of


$$
S_ZZ_k.
$$


It exists because $H_{1,k}\ne0$ implies that $Z_k$ has full column rank over $\mathbb Q$.

Define


$$
\boxed{
\zeta_{Z,k}
=
\operatorname{lcm}_{0\le m<2k}
\frac{A^Z_m}{\gcd(A^Z_m,|v_m|)}.
}
\tag{7.2}
$$


This is the **actual least simultaneous clearer** of


$$
\left(\frac{v_m}{A^Z_m}\right)_{m<2k}.
$$



After this clearing, the vector has content $1$. To verify that assertion prime by prime:

- if a prime divides $\zeta_{Z,k}$, minimality of the clearer leaves at least one unit coordinate;
- if it does not divide $\zeta_{Z,k}$ but divided every cleared coordinate, it would divide every $v_m$, contradicting primitivity.

Multiplication by $D_Z$ sends the signed cofactor vector to


$$
t_Z\left(\frac{v_m}{A^Z_m}\right)_m.
$$


Since every maximal minor of $Z_k$ uses all $k-1$ return columns, restoring their $\Lambda_k$-scalings yields the exact identity


$$
\boxed{
\mathscr R_k
=
\frac{\Lambda_k^{k-1}\mathscr C_{Z,k}\,\zeta_{Z,k}}{t_Z}.
}
\tag{7.3}
$$



Moreover,


$$
\gcd_m A^Z_m\mid\zeta_{Z,k}\mid\operatorname{lcm}_m A^Z_m,
$$


and each $A^Z_m$ divides $(6k-5)!$. Hence


$$
\log\zeta_{Z,k}=O(k\log k).
\tag{7.4}
$$



No guessed value of this actual clearer has been inserted.

### 7.2 The remaining column-content correction for $Y_k$

For $\mathbf J_{Y,k}$, let

- $a_Y$ be the gcd of the maximal minors omitting a contact column;
- $b_Y$ be the gcd of the maximal minors omitting a return column.

Thus


$$
\mathscr C_{Y,k}=\gcd(a_Y,b_Y).
$$


Define the actual correction


$$
\chi_{Y,k}
=
\frac{\gcd(\Lambda_ka_Y,b_Y)}{\gcd(a_Y,b_Y)}.
\tag{7.5}
$$


The elementary gcd lemma gives


$$
\chi_{Y,k}\mid\Lambda_k.
$$



Every maximal minor is multiplied by $t_Y$ under the square row transformation $T_Y$. The return-column scalings are $\Lambda_k^k$ or $\Lambda_k^{k-1}$, according to the omitted column. Consequently,


$$
\boxed{
\mathscr L_k
=
\frac{\Lambda_k^{k-1}\mathscr C_{Y,k}\,\chi_{Y,k}}{t_Y},
\qquad
\chi_{Y,k}\mid\Lambda_k.
}
\tag{7.6}
$$



This retains the all-prime content correction. In particular, $\chi_{Y,k}$ is not presumed to be $1$.

### 7.3 Evaluated leading payment

Stirling’s formula, or summation of logarithms of the displayed consecutive products, gives


$$
\log t_Z=4k^2\log k+O(k^2),
\qquad
\log t_Y=4k^2\log k+O(k^2).
\tag{7.7}
$$


Also,


$$
\log\Lambda_k=O(k),\qquad
\log\zeta_{Z,k}=O(k\log k),\qquad
\log\chi_{Y,k}=O(k).
$$



Combining the exact identities (7.3) and (7.6) proves


$$
\boxed{
\log\mathscr R_k+\log\mathscr L_k
=
\log\mathscr C_{Z,k}+\log\mathscr C_{Y,k}
-8k^2\log k+O(k^2).
}
\tag{7.8}
$$



This is an unconditional arithmetic statement on the nonvanishing domain. It is not yet the desired upper bound, because the two new actual contents remain unevaluated.

At large primes, all displayed payments are units, so


$$
p\mid\mathscr R_k\iff p\mid\mathscr C_{Z,k},
\qquad
p\mid\mathscr L_k\iff p\mid\mathscr C_{Y,k}.
\tag{7.9}
$$



---

## 8. Why the new obstruction does not yet prove saturation

The positive-contact ODE argument succeeded because its polynomial numerator had degree **strictly below** the forced order of vanishing.

That inequality does not occur here.

For $Z_k$, the complete mixed reduction produces a nonzero polynomial of degree at most $14k-11$. The original finite relations kill its top $2k$ coefficients, leaving the possible degree range


$$
0,\ldots,12k-11.
$$


There is no contradiction.

For $Y_k$, one must show that the finite-jet kernel has dimension at most one. Injectivity of the full rational-function map is not enough. Its projection to the physical $2k-1$ coefficients can still have a larger kernel.

These are precise obstructions:

- full rational-function injectivity does not imply injectivity of the retained jet projection;
- a full confluent interpolation matrix need not make its selected, parity-restricted submatrix a unit;
- the factorial and arctangent rational forcings cannot be separated in a mixed relation;
- product-rule commutators cannot be discarded;
- the possible prime $6k-1$ in the $Y$-operator cannot be silently treated as a unit.

### Concrete follow-on lemma

The remaining finite-tail problem can now be stated with explicit coefficient arrays, rather than unspecified Schur cofactors.

A sufficient next lemma would prove either:

1. **Large-prime finite-tail normality:**  
   the top $2k$ coefficient map of $\mathcal P_{Z,k}$ is injective, and the corresponding $Y$-jet map has kernel dimension exactly one, over every $\mathbb F_p$ with $p>6k-4$; or

2. **An evaluated finite-tail content estimate:**  
   for the integer coefficient arrays explicitly constructed above,
   

$$
\log\mathscr C_{Z,k}+\log\mathscr C_{Y,k}
   \le(12-\eta)k^2\log k+O(k^2)
$$


   on the original indices.

The second statement is quantitatively sufficient by the proved all-prime payment theorem. Neither statement follows merely from the nonzero principal part (5.10).

This is an open follow-on lemma, not a claim that a reformulation has closed the original obligation.

---

## 9. A concrete interpolation obstruction and a new actual mixed finite check

### 9.1 A paid interpolation divisor can contain a large prime

Consider the normalized even-factorial shift polynomials


$$
A_j(m)=\frac{(2m+2j)!}{(2m)!}.
$$


For $m,j=0,1,2$, their interpolation matrix is


$$
\begin{pmatrix}
1&2&24\\
1&12&360\\
1&30&1680
\end{pmatrix}.
$$


Subtracting the first row from the other two gives


$$
\det
=10\cdot1656-28\cdot336
=7152
=2^4\cdot3\cdot149.
\tag{9.1}
$$



Thus at $p=149$, this interpolation pivot is not a unit, although every factorial used to form it is a unit.

This is not a counterexample to mixed saturation. It is a concrete counterexample to the proposed shortcut “all interpolation divisions are paid by the factorial boundary.”

### 9.2 Actual mixed unit minors at $k=3,p=149$

Here


$$
\Lambda_3=45045\equiv47\pmod{149},
\qquad
6k-4=14.
$$


The complete raw mixed arrays modulo $149$ are


$$
Z_3^{\rm raw}=
\begin{pmatrix}
0&2&8&1&25\\
2&8&117&25&121\\
8&117&81&121&42\\
117&81&71&42&22\\
81&71&139&22&11\\
71&139&138&11&14
\end{pmatrix},
\tag{9.2}
$$


and


$$
Y_3^{\rm raw}=
\begin{pmatrix}
2&10&125&1&25&121\\
10&125&49&25&121&42\\
125&49&3&121&42&22\\
49&3&61&42&22&11\\
3&61&128&22&11&14
\end{pmatrix}.
\tag{9.3}
$$



These entries use the complete recurrence


$$
\tau_n=-f_{n+1}-f_n+\frac4{2n+1},
$$


not the factorial term alone.

For the first five rows of $Z_3^{\rm raw}$, moving the first return column to the front and eliminating it reduces the determinant, after a pivot $2$, to


$$
\det
\begin{pmatrix}
43&41&76\\
70&46&146\\
89&121&56
\end{pmatrix}
=14\pmod{149}.
$$


The column permutation has negative sign. Therefore the raw determinant is


$$
-2\cdot14=121\pmod{149}.
$$


Restoring both return-column scalings gives


$$
\boxed{\det Z_3[\text{rows }0,\ldots,4]=132\pmod{149}.}
\tag{9.4}
$$



For the first five columns of $Y_3^{\rm raw}$, the analogous elimination has pivot $109$ and final determinant


$$
\det
\begin{pmatrix}
80&29&11\\
9&110&9\\
25&69&67
\end{pmatrix}
=131\pmod{149}.
$$


Including the column-permutation sign gives raw determinant $25$, and restoring both return-column scalings gives


$$
\boxed{\det Y_3[\text{columns }0,\ldots,4]=95\pmod{149}.}
\tag{9.5}
$$



Both are units. Hence the actual mixed arrays are saturated at this auxiliary pair $(k,p)=(3,149)$.

This calculation establishes exactly that finite claim. In particular:

- the interpolation divisor $149$ is real;
- its occurrence in one interpolation pivot does not force mixed rank failure;
- a different, genuinely mixed unit minor can avoid it;
- no all-$k$, all-prime conclusion follows.

---

## 10. Consequences for the original whole error

The accepted analytic results are reused only at their stated scope. At the original indices,


$$
0<\ell_{K_u}
=\frac{|H_{K_u}(e+\pi)|}{G_{K_u}},
$$


and


$$
\log|H_k(e+\pi)|=4k^2\log k+O(k^2).
$$



If the outstanding estimate (1.2) were proved, then (2.7) would imply


$$
\log\ell_{K_u}
\ge
\eta K_u^2\log K_u-O(K_u^2).
\tag{10.1}
$$


Thus the primitive whole errors would diverge along the original indices.

That would show that this particular family does not supply primitive whole-error decay. It would **not** prove that $e+\pi$ is rational.

Conversely, a proved nonzero whole-error decay statement at the same original indices would prove irrationality. No such decay is established here.

Large-prime saturation alone is also insufficient for (10.1): small-prime depths, especially the binary depth already shown to exceed the old finite envelope at $32,33$, must still be bounded. The closed $32/33$ computations are not reopened and do not justify a larger guessed envelope.

The separate binary producer remains separate. Its original domain, physical terminal $z_b=0$, complete corrected columns, paid return estimate, norm $Q$, and all-prime final gcd are not replaced by compact-producer quantities. Its known $3$-adic denominator valuation is not transferred to $q_k$.

---

## 11. Final status and bounded verification request

### New proved results

- The complete finite-jet rational reductions for the actual mixed arrays.
- The explicitly evaluated factorial pole obstruction (5.10).
- The contact-pole nonvanishing argument, with its exact prime restrictions.
- The boundary-prime treatment for a necessary $Y_k$ rank-deficiency obstruction.
- The exact all-prime identities (7.3) and (7.6), including:
  - the actual primitive cofactor vector;
  - its actual least simultaneous clearer $\zeta_{Z,k}$;
  - the complete remaining column-content correction $\chi_{Y,k}$;
  - every factorial row payment.
- The leading payment identity (7.8).
- The finite actual mixed unit-minor certificate at $k=3,p=149$.

### Conditional implication

An evaluated bound (1.5) for the new coefficient-array contents would imply the requested strictly-below-$4$ bound for the original mixed contents, and hence primitive whole-error divergence at the same original indices.

### Exact remaining bottleneck

The missing step is **finite-tail normality or a sufficiently small all-prime content bound for the explicit forced coefficient arrays**.

The full rational-function map is injective in the proved ranges, but the original producer retains only a short, parity-restricted jet. The pole certificate does not yet control the arithmetic of that projection. The interpolation example (9.1) shows why its pivots cannot simply be assumed to be units.

### Bounded exact arithmetic available for coordinator inspection

No closed determinant or Smith computation needs to be repeated.

The only new small certificate requiring arithmetic inspection is Section 9:

- inputs: the displayed $6\times5$ and $5\times6$ matrices modulo the prime $149$, with right-column scalar $47$;
- physical source boundary: $k=3$, moments through $7$, factorials through $14!$, last odd denominator $13$;
- expected outputs:
  

$$
7152=2^4\cdot3\cdot149,
  \qquad
  \det Z_3[\text{rows }0,\ldots,4]\equiv132,
  \qquad
  \det Y_3[\text{columns }0,\ldots,4]\equiv95
  \pmod{149}.
$$



Those outputs verify a finite interpolation obstruction and two actual mixed unit minors. They do not settle the growing arithmetic problem.

**Final conclusion.** The new uniform result is the fully paid finite-jet reduction and its evaluated mixed pole obstruction, together with an exact leading-height transfer of $8k^2\log k$. The requested saturation theorem or strictly-below-$4$ original content estimate remains unproved. The rationality or irrationality of $e+\pi$ remains unresolved.
