> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 Turn 14: a sign theorem and two-sided paid bounds for the complete mixed error

## 1. Result and proof status

The global objective—an unconditional proof of rationality or irrationality of $e+\pi$—remains unresolved. This report does, however, settle the **whole-error nonvanishing obligation for the turn-13 matrix on every original index**.

The new ingredient is a sign-preserving identity for the **integrated arctangent channel**. It does not assert that its polynomial $W$ is pointwise positive or negative. Rather, it shows that integration against the actual arctangent weight converts the alternating coefficients of $r$ into contributions of one sign.

The conclusions are:

1. The complete arctangent integral has sign $(-1)^n$, throughout the explicit odd-$b$ construction.
2. At the original $n=2001b$ indices, an explicit Gaussian-quadrature argument places every zero of the modified orthogonal polynomial above $1$.
3. Consequently, at every original index, **both complete integrals in the mixed error are strictly negative**. They do not cancel each other.
4. An explicitly evaluated positive rational charge $\mathscr R_n$, constructed from the already computed coefficients of $r$, gives
   

$$
\boxed{
   \frac{\ell\mathscr R_n}{2g}
   <
   q_n(e+\pi)-p_n
   <
   \left(6004+\frac{3}{4b}\right)\frac{\ell\mathscr R_n}{g}.
   }
   \tag{1.1}
$$


   All quantities here use the actual turn-13 normalization, reduced arctangent charge, and final ALL-prime gcd.

Thus coefficient nonvanishing and whole-error nonvanishing are now both established for this matrix. The unresolved issue is quantitative scalar saturation: whether the actual gcd $g$ can make the positive quantity in (1.1) tend to zero.

No tool computation was performed. The proofs below are symbolic.

---

## 2. Original objects and payments retained

### 2.1 Exact index domain and finite matrix

Retain precisely


$$
b=3^{249005515+574312172u},\qquad
n=2001b,\qquad
u\equiv2\pmod{29^9},
$$


with $u$ in its original allowed domain. Put


$$
d=b-1,\qquad h=n-d=2000b+1,\qquad \alpha=b.
$$


Then $d$ is even and $n,h$ are odd.

The matrix remains


$$
H_{rj}(X)=X-A_{n+r,j}-B_j,
\qquad 0\le r,j\le d,
$$


where


$$
A_{m,j}
=j!\sum_{v=0}^{m-j}
(-1)^v\binom{m-j}{v}\frac1{(j+v)!},
$$


and


$$
B_j=4\sum_{v=0}^{2j-1}\frac{(-1)^v}{2v+1},
\qquad B_0=0.
$$



The physical finite matrix window remains


$$
m=n,n+1,\ldots,n+d,
$$


with columns $0,\ldots,d$. No additional row or column is introduced into this matrix.

In particular, the complete rational arctangent correction $B_j$ is retained.

### 2.2 Actual contents and simultaneous clearing

Write


$$
R_{rj}=A_{n+r,j}+B_j,\qquad
\mathsf W_{rj}=(n+r)!R_{rj}.
$$


Retain the actual contents


$$
\kappa_r
=\gcd\bigl((n+r)!,\mathsf W_{r0},\ldots,\mathsf W_{rd}\bigr),
\qquad
C_r=\frac{(n+r)!}{\kappa_r},
$$




$$
Y_{rj}=C_rR_{rj},
\qquad
c_j=\gcd_{0\le r\le d}(C_r,Y_{rj}),
$$


the least simultaneous clearer


$$
\mathcal L_n=\operatorname{lcm}_{0\le r\le d}C_r,
$$


and the complete row-and-column payment


$$
P_n=\frac{\prod_{r=0}^d C_r}{\prod_{j=0}^d c_j}.
$$


Thus


$$
D_n(X)
=
\det\left[\frac{C_rX-Y_{rj}}{c_j}\right]_{r,j=0}^d
=
P_n\det H(X)
=
U_nX-V_n
$$


has integer coefficients.

The turn-13 evaluated coefficient identity


$$
U_n=P_n\mathfrak c_{n,d}Z_{n,d}>0
\tag{2.1}
$$


is reused at its proved scope. Its positive-moment proof is not repeated here, and none of its factorial divisions is discarded.

The earlier A2 producer, with its separate corrected forcing, returns and physical terminal, is not identified with this matrix. Its complete formulas are not supplied in the packet. No gain, division, or cancellation from that producer is transferred into the present argument.

---

## 3. Reused scalar reduction

Let $p_h$ be the monic orthogonal polynomial of degree $h$ for


$$
w_d(x)\,dx=x^b(x-1)^d e^{-x}\,dx,\qquad x>0.
\tag{3.1}
$$


Because $d$ is even, this is a positive measure apart from isolated zeros, with infinite support and all moments.

Let $a$ be the actual least coefficient clearer of $p_h$, and retain the primitive integer polynomial


$$
r(x)=a(x-1)^dp_h(x)=\sum_{k=0}^n r_kx^k,
\qquad r_n=a>0.
\tag{3.2}
$$



The polynomial is evaluated by the nonsingular rational recurrence in turn 13, using


$$
\mu_j
=
\sum_{v=0}^d(-1)^{d-v}\binom dv(j+b+v)!.
$$


Only moments through $\mu_{2h-1}$ are required, and the largest factorial is $(2n)!$.

Retain the integer charges


$$
F=\sum_{k=0}^n r_kk!,
\qquad
E=\sum_{k=0}^n r_k\sum_{v=0}^k\frac{k!}{v!}.
\tag{3.3}
$$


Their exact endpoint meanings are


$$
F=\int_0^\infty e^{-x}r(x)\,dx,
\qquad
E=e\int_1^\infty e^{-x}r(x)\,dx.
\tag{3.4}
$$


The established reciprocal-moment argument gives $F<0$ at every original index.

The complete arctangent charge is still evaluated by


$$
\gamma_j
=
(-1)^{n-j}(n-j)!\,r_{n-j}
-\sum_{i=0}^{j-1}\binom{n+1}{j-i}\gamma_i,
\qquad 0\le j\le d,
$$




$$
w_j=\binom nj\gamma_j,\qquad
W(y)=\sum_{j=0}^dw_jy^j,
$$




$$
\mathcal B=\sum_{j=0}^dw_jB_j=\frac{T}{\ell},
\qquad
\gcd(\ell,T)=1,
\qquad \ell>0.
\tag{3.5}
$$


Here $\ell$ is the actual reduced denominator of the combined charge, not an oversized common denominator.

The final scalar gcd and actual primitive pair are


$$
g=\gcd\bigl(|F|,\ |\ell E+T|\bigr),
\tag{3.6}
$$




$$
q_n=-\frac{\ell F}{g}>0,\qquad
p_n=-\frac{\ell E+T}{g}.
\tag{3.7}
$$


The gcd in (3.6) includes every prime. In particular, no restriction to $p\le b$ is imposed.

The corresponding final gcd of the paid determinant coefficients remains exactly


$$
G_n=\gcd(U_n,|V_n|)
=
U_n\frac{g}{\ell|F|}.
\tag{3.8}
$$



Finally, retain the whole error identity


$$
M_n:=F(e+\pi)-E-\frac{T}{\ell}
=
e\int_0^1e^{-x}r(x)\,dx
+
4\int_0^1\frac{W(s^4)}{1+s^2}\,ds,
\tag{3.9}
$$


and hence


$$
q_n(e+\pi)-p_n=-\frac{\ell}{g}M_n.
\tag{3.10}
$$



Both endpoints and every rational arctangent correction remain present in these equations.

---

## 4. New bridge: the arctangent functional preserves the alternating coefficient sign

The turn-13 kernel identity is


$$
W(y)=\int_0^\infty e^{-x}r(x)L_n^{(0)}((1-y)x)\,dx.
\tag{4.1}
$$


We now evaluate its action on each monomial. This is the missing bridge between positive orthogonal zeros and the **integrated** arctangent channel.

### 4.1 A monomial Rodrigues identity

For $0\le k\le n$, define


$$
\mathcal W_{n,k}(y)
=
\int_0^\infty e^{-x}x^kL_n^{(0)}((1-y)x)\,dx.
$$


The finite Laguerre expansion gives


$$
\mathcal W_{n,k}(y)
=
\sum_{v=0}^n
\binom nv\frac{(k+v)!}{v!}(y-1)^v.
$$


But expanding $y^n=(1+(y-1))^n$ also gives


$$
\frac{d^k}{dy^k}\bigl[y^n(y-1)^k\bigr]
=
\sum_{v=0}^n
\binom nv\frac{(k+v)!}{v!}(y-1)^v.
$$


Therefore


$$
\boxed{
\mathcal W_{n,k}(y)
=
\frac{d^k}{dy^k}\bigl[y^n(y-1)^k\bigr].
}
\tag{4.2}
$$



Consequently,


$$
W(y)=\sum_{k=0}^n r_k\mathcal W_{n,k}(y).
\tag{4.3}
$$



The individual auxiliary polynomials $\mathcal W_{n,k}$ may have degree $n$. Their combination in (4.3) is the actual degree-at-most-$d$ polynomial $W$, because the higher terms cancel by the already established orthogonality. Equation (4.3) does not enlarge the matrix’s column domain.

### 4.2 The actual arctangent density is completely monotone

The substitution $y=s^4$ gives exactly


$$
4\int_0^1\frac{W(s^4)}{1+s^2}\,ds
=
\int_0^1v(y)W(y)\,dy,
\qquad
v(y)=\frac{y^{-3/4}}{1+\sqrt y}.
\tag{4.4}
$$



We require derivative signs for this particular density, not an unrelated positive weight.

Put


$$
g_0(y)=\frac1{1+\sqrt y}.
$$


It satisfies


$$
g_0'(y)=-\frac12y^{-1/2}g_0(y)^2.
\tag{4.5}
$$


An induction using the Leibniz rule proves


$$
(-1)^j g_0^{(j)}(y)\ge0
\qquad(j\ge0,\ y>0).
$$


Indeed, after differentiating (4.5) $j$ times, every term has the required sign if the assertion holds through order $j$.

Since


$$
(-1)^j\frac{d^j}{dy^j}y^{-c}
=(c)_j y^{-c-j}>0
\qquad(c>0),
$$


products preserve these alternating derivative signs. Thus both


$$
v(y)=y^{-3/4}g_0(y)
\quad\text{and}\quad
y^{-1/4}g_0(y)
$$


are completely monotone.

The identity


$$
y^{-3/4}-v(y)=y^{-1/4}g_0(y)
\tag{4.6}
$$


therefore gives the upper derivative bound


$$
(-1)^k v^{(k)}(y)
\le
(3/4)_k y^{-k-3/4}.
$$


For $0<y\le1$, the term in the Leibniz expansion in which all derivatives fall on $y^{-3/4}$, together with $g_0(y)\ge1/2$, gives the lower bound. Hence


$$
\boxed{
\frac12(3/4)_k y^{-k-3/4}
\le
(-1)^k v^{(k)}(y)
\le
(3/4)_k y^{-k-3/4}
\qquad(0<y\le1).
}
\tag{4.7}
$$



These are explicit derivative bounds for the complete arctangent density.

### 4.3 Integration by parts, including both boundary checks

Define


$$
C_{n,k}
=
(-1)^k\int_0^1v(y)\mathcal W_{n,k}(y)\,dy.
\tag{4.8}
$$


Using (4.2) and integrating by parts $k$ times gives


$$
\boxed{
C_{n,k}
=
\int_0^1
y^n(1-y)^k(-1)^k v^{(k)}(y)\,dy>0.
}
\tag{4.9}
$$



Here the endpoints require checking.

* At $y=1$, $y^n(y-1)^k$ has a zero of order $k$, so every boundary term vanishes.
* At $y=0$, a boundary product after any of the integrations is
  

$$
O\!\left(y^{\,n-k+1/4}\right),
$$


  which tends to zero because $k\le n$.
* The final integrand is
  

$$
O\!\left(y^{\,n-k-3/4}\right)
$$


  near zero and is integrable for every $k\le n$.

Thus no endpoint term has been suppressed.

### 4.4 A sign theorem for the complete arctangent integral

Every zero of $p_h$ is positive, by ordinary positive-measure orthogonality. The remaining zeros of $r$ are the $d$ copies of $1$. Since the leading coefficient is $a>0$, all elementary symmetric functions of these roots are strictly positive. Therefore


$$
\boxed{
(-1)^{n-k}r_k>0
\qquad(0\le k\le n).
}
\tag{4.10}
$$



Equations (4.3), (4.8) and (4.10) now yield


$$
\begin{aligned}
\int_0^1v(y)W(y)\,dy
&=\sum_{k=0}^n r_k(-1)^k C_{n,k}\\
&=(-1)^n\sum_{k=0}^n |r_k|C_{n,k}.
\end{aligned}
$$


Hence:

> **Theorem 4.1 — Integrated arctangent sign.**  
> For the explicit construction with odd $b$ and $n\ge b-1$,
> 

$$
> \boxed{
> (-1)^n\,4\int_0^1\frac{W(s^4)}{1+s^2}\,ds>0.
> }
> \tag{4.11}
>
$$


> This statement uses the actual polynomial $W$, including its complete rational arctangent charge.

The theorem does not claim that $W$ has constant sign. The known $n=3$ diagnostic is therefore fully compatible with it.

At every original index, $n$ is odd, and the complete arctangent integral is strictly negative.

---

## 5. Evaluated rational bounds for the arctangent channel

Equation (4.7) makes the sign theorem quantitative.

Define the positive rational numbers


$$
c_{n,k}
=
(3/4)_k
\int_0^1y^{n-k-3/4}(1-y)^k\,dy.
$$


The beta integral evaluates them:


$$
\boxed{
c_{n,k}
=
\frac{k!(3/4)_k}{(n-k+1/4)_{k+1}}.
}
\tag{5.1}
$$


All parameters differ by integers, so these numbers are rational.

They can be evaluated without gamma functions or numerical integration by


$$
\boxed{
c_{n,0}=\frac4{4n+1},
\qquad
c_{n,k+1}
=
c_{n,k}
\frac{(k+1)(4k+3)}{4n-4k-3},
\quad 0\le k<n.
}
\tag{5.2}
$$


Every denominator in this recurrence is positive.

From (4.7) and (4.9),


$$
\frac12c_{n,k}\le C_{n,k}\le c_{n,k}.
\tag{5.3}
$$



Now define the evaluated positive rational charge


$$
\boxed{
\mathscr R_n=\sum_{k=0}^n|r_k|c_{n,k}.
}
\tag{5.4}
$$


This is a finite positive arithmetic evaluation from the already generated integer coefficients of $r$. Explicitly, start with


$$
\mathscr R^{(0)}=|r_0|c_{n,0},
$$


and apply


$$
\mathscr R^{(k+1)}
=
\mathscr R^{(k)}+|r_{k+1}|c_{n,k+1}
$$


alongside (5.2).

No division by $c_{n,k}$ or $\mathscr R_n$ is used to redefine the integer form. These are auxiliary real-bound charges; the integer payment remains exactly $\ell/g$.

The complete arctangent channel satisfies


$$
\boxed{
\frac12\mathscr R_n
\le
\left|4\int_0^1\frac{W(s^4)}{1+s^2}\,ds\right|
\le
\mathscr R_n.
}
\tag{5.5}
$$



This is an evaluated bound, not merely a new name for the original oscillatory integral.

---

## 6. Original geometry: all modified orthogonal zeros lie above $1$

The arctangent sign did not require a lower bound exceeding $1$. The exponential channel does. We now validate that bound in the original objects.

### 6.1 Exact base Gaussian quadrature size

Use the base positive measure


$$
d\mu_0(x)=x^b e^{-x}\,dx.
$$


Set


$$
N=h+\frac d2=\frac{4001b+1}{2}.
\tag{6.1}
$$


The $N$-point positive Gaussian quadrature for $\mu_0$ is exact through degree $2N-1$.

For polynomials involved in the modified orthogonality,


$$
\deg\bigl((x-1)^dp_h(x)t(x)\bigr)
\le d+2h-1=2N-1
$$


whenever $\deg t<h$. Thus this quadrature exactly represents all the required orthogonality equations.

It also uses no factorial moment beyond the existing budget:


$$
(2N-1)+b=2n.
\tag{6.2}
$$


The largest base moment required is again $(2n)!$.

### 6.2 An explicit lower bound for the base Gaussian nodes

The Gaussian nodes are the zeros of $L_N^{(b)}$, equivalently the eigenvalues of the symmetric Laguerre Jacobi matrix with diagonal


$$
2i+b+1,\qquad 0\le i<N,
$$


and neighboring off-diagonal entries


$$
\sqrt{i(i+b)},\qquad 1\le i<N.
$$



For $t\ge0$,


$$
\sqrt{t(t+b)}
=
\left(t+\frac b2\right)
\sqrt{1-\frac{b^2}{4(t+b/2)^2}}
\le
t+\frac b2-\frac{b^2}{8(t+b/2)}.
\tag{6.3}
$$


The elementary inequality used here is $\sqrt{1-z}\le1-z/2$.

For row $i$, allowing a nonexistent terminal off-diagonal entry only weakens a lower bound. Equation (6.3) therefore gives


$$
\begin{aligned}
&(2i+b+1)
-\sqrt{i(i+b)}
-\sqrt{(i+1)(i+b+1)}
\\
&\hspace{1cm}\ge
\frac{b^2}{8}
\left(
\frac1{i+b/2}+\frac1{i+1+b/2}
\right)
\ge
\frac{b^2}{4N+2b}.
\end{aligned}
$$


The symmetric-matrix row bound consequently proves that every Gaussian node is at least


$$
\boxed{
L_b=\frac{b^2}{4N+2b}
=\frac{b^2}{8004b+2}.
}
\tag{6.4}
$$



For $b\ge8005$,


$$
L_b>1.
$$


Every original index satisfies this elementary size requirement.

### 6.3 Transfer to the modified orthogonal polynomial

Let the base Gaussian nodes and positive weights be $\lambda_i,\omega_i$. Exactness gives


$$
\int_0^\infty p_h(x)t(x)x^b(x-1)^de^{-x}\,dx
=
\sum_{i=1}^N
\omega_i(\lambda_i-1)^dp_h(\lambda_i)t(\lambda_i)
=0
$$


for $\deg t<h$.

Since $\lambda_i>1$, all modified weights


$$
\omega_i(\lambda_i-1)^d
$$


are strictly positive. Moreover $N>h$, since $d\ge2$.

Thus $p_h$ is also the degree-$h$ monic orthogonal polynomial for this finite positive measure. The ordinary zero-location theorem for positive measures, or the Rayleigh-quotient description of the compressed multiplication operator, puts its zeros inside the convex hull of the $\lambda_i$. In particular,


$$
\boxed{
\rho_i\ge L_b>1
\qquad(1\le i\le h)
}
\tag{6.5}
$$


for every original index.

This is the requested original-geometry validation. It is an exact quadrature argument, not a numerical root estimate.

---

## 7. Sign and size of the complete mixed error

Write


$$
p_h(x)=\prod_{i=1}^h(x-\rho_i).
$$


At the original indices, $h$ is odd and every $\rho_i>1$. Therefore, for $0\le x<1$,


$$
r(x)
=
a(1-x)^d\prod_{i=1}^h(x-\rho_i)<0.
\tag{7.1}
$$


It follows that


$$
e\int_0^1e^{-x}r(x)\,dx<0.
\tag{7.2}
$$



By Theorem 4.1, the arctangent integral is also strictly negative. Consequently,


$$
\boxed{
M_n<0
}
\tag{7.3}
$$


at every original index.

This proves nonvanishing of the **whole** evaluated determinant, not merely of one channel:


$$
q_n(e+\pi)-p_n>0.
\tag{7.4}
$$



### 7.1 An explicit bound for the exponential channel

On $0\le x\le1$,


$$
|r(x)|
=
|r_0|(1-x)^d
\prod_{i=1}^h\left(1-\frac{x}{\rho_i}\right)
\le
|r_0|(1-x)^d.
$$


Since $e<3$,


$$
0<
-e\int_0^1e^{-x}r(x)\,dx
<
\frac{3|r_0|}{d+1}
=
\frac{3|r_0|}{b}.
\tag{7.5}
$$



Combining this with (5.5) gives


$$
\boxed{
\frac12\mathscr R_n
<
|M_n|
<
\mathscr R_n+\frac{3|r_0|}{b}.
}
\tag{7.6}
$$



The $k=0$ term of $\mathscr R_n$ yields


$$
\mathscr R_n\ge\frac{|r_0|}{n+1/4}.
$$


Since $n=2001b$, (7.6) becomes


$$
\boxed{
\frac12\mathscr R_n
<
|M_n|
<
\left(6004+\frac{3}{4b}\right)\mathscr R_n
<
6005\,\mathscr R_n.
}
\tag{7.7}
$$



Thus the whole mixed error is comparable, with explicit uniform constants, to a positive rational quantity evaluated from $r$.

### 7.2 The bound after the actual final payment

Multiplying by the exact $\ell/g$ in (3.10) proves


$$
\boxed{
\frac{\ell\mathscr R_n}{2g}
<
q_n(e+\pi)-p_n
<
\left(6004+\frac{3}{4b}\right)
\frac{\ell\mathscr R_n}{g}
<
6005\frac{\ell\mathscr R_n}{g}.
}
\tag{7.8}
$$



This is the main new theorem.

In particular, all primitive rational values supplied by this matrix satisfy


$$
\frac{p_n}{q_n}<e+\pi.
$$


That one-sided statement does not imply irrationality.

---

## 8. An actual factorial lower bound—and what it does not prove

The leading coefficient $r_n=a$ contributes a positive term to $\mathscr R_n$. Therefore


$$
\mathscr R_n
\ge
a\,c_{n,n}
=
a\,n!\frac{(3/4)_n}{(1/4)_{n+1}}.
\tag{8.1}
$$


Consequently,


$$
\boxed{
q_n(e+\pi)-p_n
>
\frac{\ell a\,n!}{2g}
\frac{(3/4)_n}{(1/4)_{n+1}}.
}
\tag{8.2}
$$



The exact factor has the standard asymptotic


$$
\frac{(3/4)_n}{(1/4)_{n+1}}
=
\frac{\Gamma(1/4)}{\Gamma(3/4)}
n^{-1/2}\bigl(1+O(n^{-1})\bigr).
\tag{8.3}
$$


Thus the unpaid whole mixed error has a genuine factorial-size lower bound:


$$
|M_n|
>
\frac{a\,n!}{2}
\frac{(3/4)_n}{(1/4)_{n+1}}.
\tag{8.4}
$$



Unlike the old inadequate upper bound, this is a lower bound on the actual whole error. Nevertheless, it is **not** a primitive-error divergence theorem, because the actual factor $\ell/g$ remains present.

A necessary condition for primitive errors to tend to zero is now


$$
\frac{g}{\ell a\,n!/\sqrt n}\longrightarrow\infty.
\tag{8.5}
$$


The stronger exact characterization follows directly from (7.8):


$$
\boxed{
q_n(e+\pi)-p_n\longrightarrow0
\quad\Longleftrightarrow\quad
\frac{\ell\mathscr R_n}{g}\longrightarrow0
}
\tag{8.6}
$$


on any infinite subset of the original indices.

This is a substantive reduction: there is no longer an unresolved mixed-sign or mixed-cancellation issue for this family. What remains is an ALL-prime saturation comparison against the explicitly evaluated positive charge $\mathscr R_n$.

---

## 9. The precise remaining arithmetic obligation

### 9.1 A sufficient irrationality lemma

A sufficient next lemma is:

> On an infinite subset of the original index set, prove
> 

$$
> \boxed{
> g\ge6005\,b\,\ell\mathscr R_n.
> }
> \tag{9.1}
>
$$



Then (7.8) would give


$$
0<q_n(e+\pi)-p_n<\frac1b\longrightarrow0.
$$


Since $p_n,q_n$ are the actual primitive integers, this would prove irrationality of $e+\pi$.

No such gcd estimate is established here.

### 9.2 A concrete alternative: an obstruction lemma for this matrix

The new lower bound also makes an obstruction route precise.

For example, if one could prove, for a fixed constant $C$,


$$
|F|\le C\mathscr R_n
\tag{9.2}
$$


on an infinite original subset, then $g\le|F|$ and $\ell\ge1$ would give


$$
q_n(e+\pi)-p_n>\frac1{2C}
$$


there. This would obstruct decay along that subset.

An eventual version of (9.2) would rule out this matrix as a vanishing-error sequence. It would not rule out other constructions and would not establish rationality of $e+\pi$.

Equation (9.2) is not asserted. Its point is that it is now a concrete comparison between two fully evaluated coefficient functionals:


$$
F=\sum_{k=0}^nr_kk!,
\qquad
\mathscr R_n
=
\sum_{k=0}^n|r_k|
\frac{k!(3/4)_k}{(n-k+1/4)_{k+1}}.
$$


The first is alternating; the second is positive. Orthogonality may give a useful comparison, but no such comparison has yet been proved at the required scope.

---

## 10. Scope and source assessment

The new proof uses the supplied work at the following precise scope.

* The finite matrix reduction, recurrence for $r$, complete charge evaluation, and primitive-pair formulas are reused.
* Positive-weight orthogonality applies because $d$ is even. It establishes positive zeros of $p_h$, which is exactly what the arctangent sign proof needs.
* The stronger location above $1$ is proved separately and only then used for the exponential integral.
* The known sign changes of $W$ do not obstruct the new proof: the sign is obtained **after integration**, by (4.2)–(4.10).
* The Gaussian quadrature is auxiliary positive-measure mathematics. It neither changes the finite matrix boundaries nor imports an arithmetic gain.
* The parent’s compact contact lattice and A5’s finite determinant remain different constructions. Their saturation indices and final gcds are not transferred.
* No Family005 calculation, original-producer gain, or literature claim is used to establish the new mixed-error theorem.

The basic mixed-integral construction and standard orthogonal-polynomial tools are not claimed as novel. The advance here is the evaluated sign bridge for the complete arctangent functional, its combination with the original geometry, and the resulting two-sided bound after the actual scalar payment.

---

## 11. Bounded exact arithmetic check

No computation is needed for the proofs above. A small, independently authored transcription check would nevertheless be useful for the new Rodrigues and arctangent-functional normalization.

### Inputs

Take only


$$
n=2,\qquad k=0,1,2,
$$


with


$$
B_0=0,\qquad B_1=\frac83,\qquad B_2=\frac{304}{105}.
$$


Use


$$
I_j=\int_0^1v(y)y^j\,dy=\pi-B_j.
$$



### Expected exact outputs

The monomial kernels should be


$$
\mathcal W_{2,0}=y^2,
$$




$$
\mathcal W_{2,1}=3y^2-2y,
$$




$$
\mathcal W_{2,2}=12y^2-12y+2.
$$



The signed arctangent moments in (4.8) should be


$$
C_{2,0}=\pi-\frac{304}{105},
$$




$$
C_{2,1}=\frac{352}{105}-\pi,
$$




$$
C_{2,2}=2\pi-\frac{96}{35}.
$$



The rational comparison recurrence should return


$$
c_{2,0}=\frac49,\qquad
c_{2,1}=\frac4{15},\qquad
c_{2,2}=\frac{56}{15}.
$$



Finally, a rational enclosure for $\pi$ should verify


$$
\frac12c_{2,k}<C_{2,k}<c_{2,k}
\qquad(k=0,1,2).
$$


For example, a bounded Machin-formula check using the alternating arctangent series suffices.

This check has only the stated finite auxiliary scope. It is not an original-index computation and does not certify an infinite gcd estimate.

---

## 12. Conclusion

The new proved result is that, for the complete turn-13 mixed matrix at **every original**


$$
n=2001b
$$


index,

* the exponential contribution is strictly negative;
* the complete arctangent contribution is strictly negative despite possible sign changes of $W$;
* the whole mixed error is nonzero;
* the actual primitive error is strictly positive and satisfies the explicit paid bounds
  

$$
\frac{\ell\mathscr R_n}{2g}
  <
  q_n(e+\pi)-p_n
  <
  6005\frac{\ell\mathscr R_n}{g}.
$$



The exact remaining bottleneck is therefore


$$
\boxed{
\text{the ALL-prime comparison of }
g=\gcd(|F|,|\ell E+T|)
\text{ with }\ell\mathscr R_n
\text{ on the same infinite original indices.}
}
$$



There is now no missing whole-error nonvanishing premise for this matrix. There is still no proved vanishing primitive-error sequence, no proved primitive-error obstruction for the entire original family, and no unconditional rationality or irrationality theorem for $e+\pi$.
