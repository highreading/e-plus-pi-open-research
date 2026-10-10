> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## A1: the first radical lift is uniform, and the primitive leading coefficient has exact $3$-depth one

I obtain the requested first nonzero radical lift on the **entire** regular class:


$$
\boxed{\delta_n/3\equiv1\pmod3,\qquad
\xi_{\rm last}-(b/a)\xi_{\rm const}\equiv2\pmod3,
\quad n=4^j+1,\ j\ge1.}
$$


In fact these congruences hold in the larger domain $n=3M+2$, $M\ge1$, with the divided basis and Schur partition of A1 turn 4.

The lift does not require a growing finite-state machine. The decisive simplification is the uniform identity


$$
\boxed{e_{3r}\equiv3\pmod9\qquad(r\ge0).}
$$


It converts the first perturbation of the radical norm into the ordinary Pascal Schur complement, which is exactly $1$.

For the actual primitive polynomial on the regular class, this proves


$$
\boxed{v_3(\operatorname{lc}Q_n)=1.}
$$


I also obtain an exact endpoint-content relation below. I do **not** obtain a uniform valuation of the actual final denominator $q$: the remaining endpoint cancellation and the full rational-arctangent determinant gcd are not determined by this first lift.

---

# 1. Moment precision: an explicit uniform calculation modulo $9$

Reuse the established integers


$$
b_s=\frac{\mu((y-1)^s)}{s!},
\qquad
e_s=\frac{\mu((y+1)^2(y-1)^s)}{s!}.
$$


Their exact formulas are


$$
b_s=\sum_{\ell=0}^s
 \binom{s}{\ell}(-2)^{s-\ell}
 \frac{(s+\ell)!}{s!},
\tag{1}
$$


and


$$
e_s=4b_s+4(s+1)b_{s+1}+(s+1)(s+2)b_{s+2}.
\tag{2}
$$



Every term of (1) with $\ell\ge6$ is divisible by $9$: the product of any six consecutive integers contains at least two multiples of $3$. Thus only $0\le\ell<6$ is needed, uniformly in $s$.

Terms with $\ell>s$ may be included as zero. In the following residue calculations, a negative exponent of $-2$ in such a zero term is interpreted in $\mathbb Z_3^\times$; it causes no boundary exception.

The direct six-term calculation gives


$$
\boxed{
\begin{aligned}
b_{3r}&\equiv1+6r(r+1),\\
b_{3r+1}&\equiv0,\\
b_{3r+2}&\equiv4+6r(r+1)
\end{aligned}\pmod9
\qquad(r\ge0).
}
\tag{3}
$$



Here are the details, including the divisions in the binomial coefficients.

### 1.1 The branch $s=3r$

Since


$$
(-2)^u=(1-3)^u\equiv1-3u\pmod9,
$$


the $\ell=0$ term is $1$. The $\ell=1,2$ terms are respectively


$$
3r,\qquad -3r\pmod9.
$$


For $\ell=3$, its factorial-binomial product is


$$
\frac{(3r)(3r-1)(3r-2)(3r+1)(3r+2)(3r+3)}6.
$$


After extracting one factor $3$, its residue is


$$
6r(r+1)\pmod9.
$$


For $\ell=4,5$, the binomial coefficient is divisible by $3$, and the rising factorial also is divisible by $3$. Those terms vanish modulo $9$. This proves the first branch.

### 1.2 The branch $s=3r+1$

The first two terms are $7$ and $2$, summing to zero modulo $9$, because


$$
(3r+1)(3r+2)\equiv2\pmod9.
$$


The $\ell=2$ term has two factors $3$: one in $\binom{s}{2}$, the other in the rising factorial.

For $\ell=3,4$, Lucas reduction gives


$$
\binom{3r+1}{3}\equiv r,\qquad
\binom{3r+1}{4}\equiv r\pmod3.
$$


Their rising factorials, divided by $3$, have residues $2(r+1)$ and $r+1$. Hence these two terms contribute


$$
6r(r+1)+3r(r+1)=0\pmod9.
$$


The $\ell=5$ rising factorial has two factors $3$. This proves the second branch.

### 1.3 The branch $s=3r+2$

The first term is $4$. The $\ell=1,2$ terms contribute


$$
6(r+1),\qquad3(r+1),
$$


and cancel modulo $9$. For $\ell=3$,


$$
\binom{3r+2}{3}\equiv r\pmod3,
$$


and the rising factorial divided by $3$ is $2(r+1)$ modulo $3$. Its contribution is $6r(r+1)$. The $\ell=4,5$ rising factorials contain two multiples of $3$.

This completes (3).

### 1.4 The norm branch collapses

Putting $s=3r$ in (2), use


$$
(3r+1)(3r+2)\equiv2\pmod9
$$


and (3). Then


$$
\begin{aligned}
e_{3r}
&\equiv4\bigl(1+6r(r+1)\bigr)
 +2\bigl(4+6r(r+1)\bigr)\\
&\equiv12+36r(r+1)
\equiv3\pmod9.
\end{aligned}
$$


Thus


$$
\boxed{e_{3r}\equiv3\pmod9\quad\text{at every }r\ge0.}
\tag{4}
$$



There is no dependence on a bounded list of observed indices in this proof.

---

# 2. Explicit radical coordinates and their first perturbation

Take $n=3M+2$, $M\ge1$. The established unit block $E$ consists of nonconstant divided coordinates


$$
d=0,\ldots,3M-1,
$$


and the last nonconstant coordinate is $d=3M$. Its reduction is


$$
\bar E=B_M\otimes A,
\qquad
B_M(D,E)=\binom{D+E}{D},
$$


where


$$
A=
\begin{pmatrix}
0&2&1\\
2&2&0\\
1&0&0
\end{pmatrix}
\quad\text{over }\mathbb F_3.
$$



Write


$$
v_D=\binom MD,\qquad
z_D=(-1)^{M-1-D}\binom MD,\qquad 0\le D<M.
\tag{5}
$$


These are exact integers, not just residue representatives.

If $P_M(D,a)=\binom Da$, then


$$
B_M=P_MP_M^T,\qquad
b_D=\binom{M+D}{D}=(P_Mv)_D.
$$


The binomial inverse formula gives


$$
(P_M^{-T}v)_D
=\sum_{a=D}^{M-1}(-1)^{a-D}\binom aD\binom Ma
=(-1)^{M-1-D}\binom MD=z_D.
$$


Therefore


$$
B_M^{-1}b=z
\tag{6}
$$


holds over $\mathbb Q$, not merely modulo $3$.

Let $r$ be the divided-coordinate vector with:

* constant coordinate $0$;
* last coordinate $1$;
* coordinate $d=3D$ equal to $-z_D$, $0\le D<M$;
* every other coordinate equal to $0$.

This is an integral lift of the established radical.

### Why its norm computes the first Schur perturbation

Let $x$ be the actual cross-vector from $E$ to the last coordinate, and let


$$
z^*=E^{-1}x\in\mathbb Z_3^{3M}.
$$


The residue theorem and (6) show that $z^*$ differs from the vector supported on $d=3D$ with coefficients $z_D$ by a vector in $3\mathbb Z_3^{3M}$.

Consequently,


$$
r^TG_nr
=
c+(z-z^*)^TE(z-z^*)
\equiv c\pmod9.
\tag{7}
$$


Here $c$ is the actual last-last entry after eliminating $E$. Since $b\in3\mathbb Z_3$ and $a$ is a unit,


$$
\delta=c-b^2/a\equiv c\pmod9.
\tag{8}
$$



Equations (7)–(8) apply the first inverse perturbation without introducing an unevaluated inverse correction: its quadratic contribution starts at $9$.

---

# 3. Evaluation of the radical norm: $\delta/3=1$

Set


$$
t_D=-z_D\quad(0\le D<M),\qquad t_M=1.
$$


The support of $r$ consists entirely of coordinates $d=3D$. Hence


$$
r^TG_nr
=
\sum_{D,E=0}^{M}
t_Dt_E
\binom{3(D+E)}{3D}e_{3(D+E)}.
$$


By (4), this is divisible by $3$, and Lucas reduction yields


$$
\frac{r^TG_nr}{3}
\equiv
\sum_{D,E=0}^{M}
t_Dt_E\binom{D+E}{D}
\pmod3.
\tag{9}
$$



The expression on the right is the last Schur norm in the ordinary Pascal matrix $B_{M+1}$. More explicitly, by (6),


$$
\begin{aligned}
\sum_{D,E=0}^{M}t_Dt_E\binom{D+E}{D}
&=\binom{2M}{M}-b^TB_M^{-1}b\\
&=\binom{2M}{M}
  -\sum_{a=0}^{M-1}\binom Ma^2\\
&=1.
\end{aligned}
\tag{10}
$$


The second equality uses $b=P_Mv$, and the third is Vandermonde’s identity, retaining the omitted $a=M$ term.

Combining (7)–(10) proves


$$
\boxed{\delta\equiv3\pmod9,\qquad v_3(\delta)=1}
\tag{11}
$$


for every $M\ge1$.

This proves the first nonzero radical lift on every regular index $n=4^j+1$, not just on a subsequence.

---

# 4. The mixed numerator is uniformly a unit

The degree-$n$ divided polynomial has nonconstant index


$$
d=n-1=3M+1.
$$


Modulo $3$, it is the next tensor coordinate $(M,1)$, whereas the radical’s last coordinate is $(M,0)$.

After eliminating the first $3M$ coordinates, the mixed pairing is


$$
A_{01}
\left(\binom{2M}{M}-b^TB_M^{-1}b\right)
=2
\pmod3
$$


by (10). Thus


$$
\xi_{\rm last}\equiv2\pmod3.
\tag{12}
$$



For the constant component, the direct coupling is $2$. The eliminated contribution is also $2$: it uses


$$
\mathbf1^TB_M^{-1}b=1,\qquad
\mathbf1^TA^{-1}Ae_1=1.
$$


Therefore


$$
\xi_{\rm const}\equiv0\pmod3.
\tag{13}
$$



Since $b/a\in3\mathbb Z_3$,


$$
\boxed{
\xi_{\rm last}-(b/a)\xi_{\rm const}\equiv2\pmod3.
}
\tag{14}
$$


Equations (11) and (14) give


$$
\boxed{v_3(\eta_{\rm last})=-1,\qquad
3\eta_{\rm last}\equiv2\pmod3.}
\tag{15}
$$


All entries of $\eta$ lie in $3^{-1}\mathbb Z_3$, and


$$
\eta_{\rm const}=(\xi_{\rm const}-b\eta_{\rm last})/a
\in\mathbb Z_3.
\tag{16}
$$



---

# 5. Propagation to actual primitive content

Now restrict to the assigned domain


$$
n=4^j+1,\quad j\ge1,\qquad N=n-1=4^j=3M+1.
$$


Let $P_n$ be the monic orthogonal polynomial. In the established basis,


$$
P_n
=h_n-N!\eta_{\rm const}
-\sum_{d=0}^{N-1}\frac{N!}{d!}\eta_{d+1}h_{d+1}.
\tag{17}
$$



Every factorial ratio is an integer, and all $\eta_i$ have valuation at least $-1$. Thus $3P_n$ has $3$-integral coefficients.

The coefficient of $y^{n-1}$ in $P_n$ is


$$
[y^{n-1}]h_n-N\eta_{\rm last}.
$$


The first term is integral. The second has valuation exactly $-1$, because $N=4^j$ is a $3$-adic unit. Consequently


$$
\min_a v_3([y^a]P_n)=-1.
\tag{18}
$$



Write the actual primitive integer polynomial as


$$
Q_n=L_nP_n,\qquad L_n=\operatorname{lc}Q_n>0.
$$


Primitivity and (18) imply


$$
\boxed{v_3(L_n)=1.}
\tag{19}
$$


This is the actual polynomial content calculation; no endpoint gcd has yet been taken.

There is also an explicit primitive-ray reduction. For $d\le N-2$, the factorial ratio $N!/d!$ contains the multiple $N-1=3M$, so all such terms vanish in $3P_n\bmod3$. Using (15),


$$
3P_n\equiv-2N h_{n-1}
\equiv h_{n-1}\pmod3.
$$


Therefore, for a unit $u_j\in\mathbb F_3^\times$,


$$
\boxed{
\bar Q_n(y)=u_j(y+1)(y-1)^{\,n-2}.
}
\tag{20}
$$



---

# 6. The exact endpoint-content relation—and its unresolved cancellation

The endpoint is


$$
P_n(-1)=-N!\eta_{\rm const}.
$$


Inverting the actual two-by-two Schur block gives


$$
\eta_{\rm const}
=\frac{c\,\xi_{\rm const}-b\,\xi_{\rm last}}{a\delta}.
$$


Since $v_3(L_n)=v_3(\delta)=1$ and $a$ is a unit, the primitive endpoint satisfies the exact identity


$$
\boxed{
v_3(Q_n(-1))
=
v_3(N!)
+
v_3\!\left(c\,\xi_{\rm const}-b\,\xi_{\rm last}\right).
}
\tag{21}
$$


The numerator in (21) is nonzero: the established negative-mass orthogonal-polynomial identity gives $P_n(-1)\ne0$.

Our congruences show


$$
c\in3\mathbb Z_3,\quad
\xi_{\rm const}\in3\mathbb Z_3,\quad
b\in3\mathbb Z_3,\quad
\xi_{\rm last}\in\mathbb Z_3^\times.
$$


Hence


$$
\boxed{
v_3(Q_n(-1))\ge v_3(N!)+1.
}
\tag{22}
$$


More precisely:

* if $v_3(b)=1$, equality holds in (22);
* if $v_3(b)\ge2$, the endpoint has depth at least $v_3(N!)+2$, but its exact depth requires the coupled numerator in (21).

For the supplied $n=17$ control, $v_3(c\xi_{\rm const})=7$ and $v_3(b\xi_{\rm last})=6$. Thus (21) gives $6+6=12$, agreeing with the native primitive endpoint. This agreement is a normalization check, not an infinite law for that deeper numerator.

The first radical lift therefore explains the uniform primitive leading depth. It does **not** explain the observed growing endpoint depth by itself.

---

# 7. Full rational-arctangent endpoint and actual denominator

No change is made to the complete endpoint construction. For primitive $Q_n$, retain


$$
R_{ij}=\sum_{t=0}^nQ_{n,t}
\left(-(2(i+j+t))!+
4\sum_{a=1}^{i+j+t}\frac{(-1)^{i+j+t-a}}{2a-1}\right).
$$


In the endpoint basis write


$$
R_{\rm end}=
\begin{pmatrix}a_R&b_R^T\\ b_R&H\end{pmatrix},
\qquad
\ell=\operatorname{lcm}(1,3,\ldots,4n-3),
$$


and set


$$
t=\ell a_R,\quad z=\ell b_R,\quad K=\ell H,
$$




$$
A=t\det K-z^T\operatorname{adj}(K)z,\qquad
B=\ell Q_n(-1)\det K.
$$


The actual final normalization is


$$
g=\gcd(|A|,|B|),\qquad
q=\frac{|B|}{g},\qquad
p=-\frac{\operatorname{sgn}(B)A}{g}.
\tag{23}
$$


In particular,


$$
v_3(q)=\max\{0,v_3(B)-v_3(A)\}.
\tag{24}
$$



The new content relation enters this expression as


$$
v_3(B)=v_3(\ell)+v_3(N!)
+v_3(c\xi_{\rm const}-b\xi_{\rm last})
+v_3(\det K).
\tag{25}
$$


This is an exact propagation to the full endpoint pair. I have not evaluated the last determinant or $A$ uniformly; replacing either by a polynomial coefficient content would be invalid.

The whole evaluated error remains


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B)}g\bigl(A+B(e+\pi)\bigr)
=\frac{\operatorname{sgn}(B)\ell^k}{g}\det H_{\rm complete}.
}
\tag{26}
$$


Both periods and every arctangent rational term are included. On the regular domain, the supplied dyadic theorem gives $B\ne0$, pairwise distinct centers, and hence nonzero whole errors apart from at most one index. Nothing proved here gives decay of (26).

---

## (1) New result and proof status

**Proved uniformly, with explicit derivations:**

* $e_{3r}\equiv3\pmod9$ for all $r\ge0$;
* $\delta/3\equiv1\pmod3$ and mixed numerator $\equiv2\pmod3$ for every $n=3M+2$, $M\ge1$;
* on $n=4^j+1$, exact primitive leading depth $v_3(\operatorname{lc}Q_n)=1$;
* the primitive-ray reduction (20);
* the exact, nonzero endpoint-content relation (21), propagated to the full endpoint coefficient $B$ in (25).

No decision on irrationality of $e+\pi$, and no uniform actual odd-denominator law, is proved.

## (2) Exact remaining bottleneck

The next lift is no longer the radical determinant: its depth is now settled exactly.

The unresolved polynomial endpoint scalar is specifically


$$
c\xi_{\rm const}-b\xi_{\rm last}.
$$


Its growing-depth behavior requires deeper coupled information about $b$ and $\xi_{\rm const}$. Even after that scalar is evaluated, the actual denominator still requires the full rational-arctangent quantities


$$
v_3(\det K),\qquad v_3(A),
$$


and their final gcd contribution. These are the precise obstructions to turning the new primitive-content theorem into an improvement of A4’s whole-error balance.

## (3) Bounded computation request

**Input:** the single next regular degree $n=65$, $p=3$, using the divided moments and the $63\times63$ unit block $E$.

**Requested output:** compute the four Schur entries/responses


$$
b,\quad c,\quad\xi_{\rm const},\quad\xi_{\rm last}
$$


modulo $3^{32}$, reporting certified valuations when below $32$, and report the valuation and first nonzero unit of


$$
c\xi_{\rm const}-b\xi_{\rm last}.
$$


Verify $\delta\equiv3\pmod9$ and the mixed numerator $\equiv2\pmod3$ as normalization checks.

This is one bounded modular unit-block computation, not a degree scan or a request to reconstruct a huge exact center. Its purpose is to distinguish the next coupled endpoint cancellation from the now-proved first radical lift. If a requested scalar is zero modulo $3^{32}$, report only the corresponding lower bound; do not infer exact depth or an infinite law.
