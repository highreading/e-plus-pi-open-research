> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the two global sign theorems and their primitive arithmetic consequences

## 1. Executive conclusion

**Both new global sign arguments survive independent symbolic checking.** They apply to two different, precisely specified determinant families.

1. **A2’s Laguerre family.** At every original admissible index
   

$$
b=3^{249005515+574312172u},\qquad n=2001b,\qquad
   u\equiv2\pmod{29^9},
$$


   with $u$ restricted to its original allowed domain, the complete mixed error satisfies
   

$$
M_n<0.
$$


   Its actual primitive error is therefore positive. After the already established exact simplification $\ell=1$, it satisfies
   

$$
\boxed{\frac{\mathscr R_n}{2g_n}
   <q_n(e+\pi)-p_n
   <6005\,\frac{\mathscr R_n}{g_n}.}
$$


   The coordinator’s short identity is correct:
   

$$
\boxed{\mathscr R_n
   =4(-1)^n\sum_{j=0}^{d}\frac{w_j}{4j+1}.}
$$


   Moreover, $\mathscr R_n$ is a strictly positive integer on the entire original domain. Its integrality follows from actual factorial divisibility of the existing charges, without rescaling the primitive polynomial $r$.

2. **A3’s compact family.** For every integer $k\ge32$,
   

$$
\boxed{\det T^{(k)}>0,\qquad
   (-1)^kH_k(e+\pi)>0,\qquad
   (-1)^kH_{1,k}>0.}
$$


   The proof retains the actual unbounded factorial measure, the full compact measure, and the negative atom at $-1$. The signed double-Andréief formula and its derivative have the asserted orientation. They evaluate the **same integer affine polynomial** originally defined by the complete rational endpoint corrections.

3. **What remains open.** Neither result proves primitive-error decay. The remaining questions are comparisons with the **actual final all-prime gcds**:
   

$$
\frac{\mathscr R_n}{g_n}
   \quad\text{and}\quad
   \frac{|H_k(e+\pi)|}{G_k}.
$$


   In particular, a fixed-$C$ divisibility assertion
   

$$
g_n\mid C\mathscr R_n
$$


   is **not proved**.

The historical nonvanishing obligations recorded in A4 Turn 17 are thus closed for these two displayed families on the domains stated above. They are not closed for a distinct original producer merely by association with one of these matrices.

**The rationality or irrationality of $e+\pi$ remains unresolved.**

---

## 2. Objects, boundaries, and arithmetic payments retained

### 2.1 A2’s finite matrix

Throughout the A2 audit, put


$$
d=b-1,\qquad h=n-d=2000b+1.
$$


On the original domain, $d$ is even and $n,h$ are odd.

The matrix remains exactly


$$
H_{rj}(X)=X-A_{n+r,j}-B_j,\qquad 0\le r,j\le d,
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


Thus the physical row window is $m=n,\ldots,n+d$, and the column range is $0,\ldots,d$. Every rational arctangent correction is retained.

For clarity, write


$$
R_{rj}=A_{n+r,j}+B_j,\qquad
\mathsf W_{rj}=(n+r)!R_{rj}.
$$


The actual row contents, column contents, and clearers remain


$$
\kappa_r=\gcd\bigl((n+r)!,\mathsf W_{r0},\ldots,\mathsf W_{rd}\bigr),
\qquad
C_r=\frac{(n+r)!}{\kappa_r},
$$




$$
Y_{rj}=C_rR_{rj},\qquad
c_j=\gcd_{0\le r\le d}(C_r,Y_{rj}),
$$




$$
\mathcal L_n=\operatorname{lcm}_{0\le r\le d}C_r,\qquad
P_n=\frac{\prod_{r=0}^dC_r}{\prod_{j=0}^dc_j}.
$$


Consequently,


$$
D_n(X)
=\det\left[\frac{C_rX-Y_{rj}}{c_j}\right]
=P_n\det H(X)
=U_nX-V_n
$$


is an integer polynomial.

The established coefficient bridge gives $U_n>0$. I reuse that result at its proved scope; no new sign argument below removes any factor from its normalization.

### 2.2 The actual polynomial and scalar charges

Let $p_h$ be the monic orthogonal polynomial for


$$
x^b(x-1)^d e^{-x}\,dx,\qquad x>0.
$$


Let $a$ be its least coefficient clearer, and retain


$$
r(x)=a(x-1)^dp_h(x)=\sum_{k=0}^nr_kx^k,\qquad r_n=a>0.
$$



This is the actual primitive integer polynomial. Indeed, $ap_h$ is primitive by the minimality of $a$, and multiplication by the primitive polynomial $(x-1)^d$ preserves content $1$. No division by $a$, by a coefficient of $r$, or by an auxiliary bound is made below.

The charges are


$$
F=\sum_{k=0}^nr_kk!,
\qquad
E=\sum_{k=0}^nr_k\sum_{v=0}^k\frac{k!}{v!},
$$


and


$$
\gamma_j=(-1)^{n-j}(n-j)!r_{n-j}
-\sum_{i<j}\binom{n+1}{j-i}\gamma_i,
$$




$$
w_j=\binom nj\gamma_j,\qquad
W(y)=\sum_{j=0}^dw_jy^j,\qquad
\mathcal B=\sum_{j=0}^dw_jB_j.
$$



The previously established exact identities are


$$
F<0,\qquad \sum_{j=0}^dw_j=F,
$$




$$
W(y)=\int_0^\infty e^{-x}r(x)L_n^{(0)}((1-y)x)\,dx,
$$


and


$$
M_n:=F(e+\pi)-E-\mathcal B
=e\int_0^1e^{-x}r(x)\,dx
+4\int_0^1\frac{W(s^4)}{1+s^2}\,ds.
\tag{2.1}
$$



On the original domain, the established charge-divisibility argument gives


$$
\ell=1,\qquad T=\mathcal B\in\mathbb Z.
$$


Hence the actual final reduction is


$$
g_n=\gcd(|F|,|E+T|),
$$




$$
q_n=-\frac F{g_n}>0,\qquad
p_n=-\frac{E+T}{g_n},
\tag{2.2}
$$


and


$$
q_n(e+\pi)-p_n=-\frac{M_n}{g_n}.
\tag{2.3}
$$


The paid determinant’s final gcd remains


$$
G_n=\gcd(U_n,|V_n|)
=U_n\frac{g_n}{|F|}.
\tag{2.4}
$$



These are all-prime gcds.

---

## 3. Audit of A2’s integrated arctangent sign

### 3.1 The exact monomial Rodrigues identity

For $0\le k\le n$, define


$$
\mathcal W_{n,k}(y)
=\int_0^\infty e^{-x}x^kL_n^{(0)}((1-y)x)\,dx.
$$


Using the finite Laguerre expansion,


$$
\mathcal W_{n,k}(y)
=\sum_{v=0}^n\binom nv\frac{(k+v)!}{v!}(y-1)^v.
$$



Now set $z=y-1$. Since


$$
y^n(y-1)^k=(1+z)^nz^k
=\sum_{v=0}^n\binom nv z^{v+k},
$$


differentiating $k$ times proves


$$
\boxed{
\mathcal W_{n,k}(y)
=\frac{d^k}{dy^k}\bigl[y^n(y-1)^k\bigr].
}
\tag{3.1}
$$


Thus


$$
W(y)=\sum_{k=0}^nr_k\mathcal W_{n,k}(y).
\tag{3.2}
$$



This identity does not enlarge the matrix. Individual monomial kernels can have degree $n$; their combination is the already defined polynomial $W$ of degree at most $d$.

**Decision: accepted.**

### 3.2 Complete monotonicity of the actual density

The substitution $y=s^4$ gives


$$
4\int_0^1\frac{W(s^4)}{1+s^2}\,ds
=\int_0^1v(y)W(y)\,dy,
\qquad
v(y)=\frac{y^{-3/4}}{1+\sqrt y}.
\tag{3.3}
$$



Let


$$
g_0(y)=\frac1{1+\sqrt y}.
$$


Then


$$
g_0'(y)=-\frac12y^{-1/2}g_0(y)^2.
$$



Here is the derivative-sign induction explicitly. Suppose


$$
(-1)^jg_0^{(j)}(y)\ge0\qquad(0\le j\le m).
$$


Differentiate the displayed first-order identity $m$ times. A typical Leibniz term has the form


$$
-\frac12\frac{m!}{a!\,b!\,c!}
\left(y^{-1/2}\right)^{(a)}
g_0^{(b)}g_0^{(c)},
\qquad a+b+c=m.
$$


The product after the initial minus sign has sign $(-1)^m$. Every term therefore has sign $(-1)^{m+1}$. This proves the induction.

Because


$$
(-1)^j(y^{-c})^{(j)}=(c)_jy^{-c-j}>0
\qquad(c>0),
$$


both


$$
y^{-3/4}g_0(y)
\quad\text{and}\quad
y^{-1/4}g_0(y)
$$


are completely monotone.

The identity


$$
y^{-3/4}-v(y)=y^{-1/4}g_0(y)
$$


then proves


$$
(-1)^kv^{(k)}(y)\le(3/4)_ky^{-k-3/4}.
$$


For $0<y\le1$, the Leibniz term in which all $k$ derivatives fall on $y^{-3/4}$, together with $g_0(y)\ge1/2$, gives the lower bound. Hence


$$
\boxed{
\frac12(3/4)_ky^{-k-3/4}
\le(-1)^kv^{(k)}(y)
\le(3/4)_ky^{-k-3/4}.
}
\tag{3.4}
$$



These inequalities concern the complete arctangent density, not a surrogate.

**Decision: accepted for every $k\ge0$ and $0<y\le1$.**

### 3.3 Every integration-by-parts boundary term

Put


$$
f_{n,k}(y)=y^n(y-1)^k.
$$


After $k$ integrations by parts, the potential boundary terms are products


$$
v^{(j)}(y)f_{n,k}^{(k-1-j)}(y),
\qquad 0\le j<k.
$$



At $y=1$, the derivative order on $f_{n,k}$ is less than $k$, so its zero of order $k$ makes each product vanish.

At $y=0$, since $k\le n$,


$$
f_{n,k}^{(k-1-j)}(y)
=O\!\left(y^{n-k+1+j}\right).
$$


Equation (3.4) gives


$$
v^{(j)}(y)=O(y^{-j-3/4}),
$$


so every boundary product is


$$
O\!\left(y^{n-k+1/4}\right)\longrightarrow0.
$$



The final integrand is bounded near zero by a constant times


$$
y^{n-k-3/4},
$$


whose exponent is at least $-3/4$. It is integrable.

Therefore


$$
C_{n,k}:=(-1)^k\int_0^1v(y)\mathcal W_{n,k}(y)\,dy
$$


satisfies the exact identity


$$
\boxed{
C_{n,k}
=\int_0^1y^n(1-y)^k(-1)^kv^{(k)}(y)\,dy>0.
}
\tag{3.5}
$$



There is no missing endpoint contribution.

### 3.4 Coefficient signs and the integrated sign

The measure defining $p_h$ is positive because $d$ is even. Its support is infinite in $(0,\infty)$. The usual sign-change proof for orthogonal polynomials therefore puts all zeros of $p_h$ in $(0,\infty)$.

All zeros of $r$ are consequently positive: the zeros of $p_h$, together with the $d$ copies of $1$. Since $r_n=a>0$, every elementary symmetric function of these zeros is strictly positive, and


$$
(-1)^{n-k}r_k>0\qquad(0\le k\le n).
\tag{3.6}
$$



Combining (3.2), (3.5), and (3.6),


$$
\int_0^1v(y)W(y)\,dy
=\sum_{k=0}^nr_k(-1)^kC_{n,k}
=(-1)^n\sum_{k=0}^n|r_k|C_{n,k}.
$$


Thus


$$
\boxed{
(-1)^n\,4\int_0^1\frac{W(s^4)}{1+s^2}\,ds>0.
}
\tag{3.7}
$$



The proof requires neither coefficientwise positivity of $W$ nor a pointwise sign for $W$. It therefore avoids the exact obstruction found in the earlier auxiliary example where $W$ changed sign.

**Decision: A2’s integrated arctangent sign theorem is accepted at its stated odd-$b$, $n\ge b-1$ construction scope. In particular, the integral is strictly negative at every original index.**

---

## 4. Audit of the root bound and the whole mixed error

### 4.1 Quadrature size, exactness degree, and factorial boundary

Use the base measure


$$
d\mu_0(x)=x^be^{-x}\,dx.
$$


Set


$$
N=h+\frac d2=\frac{4001b+1}{2}.
$$


This is an integer because $b$ is odd.

An $N$-node Gaussian quadrature is exact through degree $2N-1$. For $\deg t<h$,


$$
\deg\bigl((x-1)^dp_h(x)t(x)\bigr)
\le d+2h-1=2N-1.
$$


Thus the quadrature is exact for every modified orthogonality equation that is used.

The largest base factorial moment is


$$
(b+2N-1)!=(2n)!.
\tag{4.1}
$$


No moment $(2n+1)!$ is needed: the monic degree-$N$ orthogonality equations and the finite Jacobi matrix use moments through degree $2N-1$.

This agrees with the direct modified-moment construction, whose final required moment is $\mu_{2h-1}$.

**Decision: the quadrature size, exactness degree, and $(2n)!$ boundary are accepted.**

### 4.2 The Gershgorin estimate

The Laguerre Jacobi matrix has diagonal


$$
2i+b+1,\qquad 0\le i<N,
$$


and off-diagonal entries


$$
\sqrt{i(i+b)},\qquad 1\le i<N.
$$


For $t\ge0$,


$$
\sqrt{t(t+b)}
=\left(t+\frac b2\right)
\sqrt{1-\frac{b^2}{4(t+b/2)^2}}
\le
t+\frac b2-\frac{b^2}{8(t+b/2)}.
$$


This follows from $\sqrt{1-z}\le1-z/2$, with $0\le z\le1$.

Subtracting both possible neighboring terms from row $i$'s diagonal gives


$$
\begin{aligned}
&2i+b+1-\sqrt{i(i+b)}-\sqrt{(i+1)(i+b+1)}
\\
&\qquad\ge
\frac{b^2}{8}
\left(\frac1{i+b/2}+\frac1{i+1+b/2}\right)
\\
&\qquad\ge\frac{b^2}{4N+2b}.
\end{aligned}
$$


At the final row, including the nonexistent outward neighbor only decreases the estimate, so it is a legitimate weakening.

Every eigenvalue—and hence every quadrature node—is therefore at least


$$
\boxed{
L_b=\frac{b^2}{4N+2b}
=\frac{b^2}{8004b+2}.
}
\tag{4.2}
$$


For $b\ge8005$, $b^2-8004b-2>0$, so $L_b>1$. Every original admissible index satisfies this size condition.

### 4.3 Transfer to the modified polynomial

Let the quadrature nodes and positive weights be $\lambda_i,\omega_i$. Exactness gives


$$
\sum_{i=1}^N
\omega_i(\lambda_i-1)^dp_h(\lambda_i)t(\lambda_i)=0
\qquad(\deg t<h).
$$



All modified weights are strictly positive because $\lambda_i>1$. Also,


$$
N-h=\frac d2>0
$$


on the original domain.

Thus $p_h$ is the degree-$h$ monic orthogonal polynomial of a positive discrete measure supported on the $N$ nodes. The standard zero-location theorem puts its zeros in their convex hull. Therefore


$$
\boxed{\rho_i\ge L_b>1\qquad(1\le i\le h).}
\tag{4.3}
$$



The finite quadrature is an auxiliary exact representation of existing moments. It does not add rows or contacts to the original matrix.

**Decision: accepted.**

### 4.4 Whole-error sign and uniform paid bounds

Since $h$ is odd and $d$ is even, (4.3) gives


$$
r(x)=a(1-x)^d\prod_{i=1}^h(x-\rho_i)<0
\qquad(0\le x<1).
$$


The exponential channel is therefore strictly negative. The arctangent channel is strictly negative by (3.7). Hence


$$
\boxed{M_n<0}
\tag{4.4}
$$


at every original admissible index.

For the quantitative comparison, define


$$
c_{n,k}
=(3/4)_k\int_0^1y^{n-k-3/4}(1-y)^k\,dy.
$$


The beta integral gives


$$
c_{n,k}
=\frac{k!(3/4)_k}{(n-k+1/4)_{k+1}}.
\tag{4.5}
$$


In particular,


$$
c_{n,0}=\frac4{4n+1},
$$


and direct division of successive expressions gives


$$
c_{n,k+1}
=c_{n,k}\frac{(k+1)(4k+3)}{4n-4k-3}.
\tag{4.6}
$$


For $0\le k<n$, the final denominator is at least $1$.

Let


$$
\mathscr R_n=\sum_{k=0}^n|r_k|c_{n,k}>0.
\tag{4.7}
$$


Equation (3.4) gives


$$
\frac12\mathscr R_n
\le
\left|4\int_0^1\frac{W(s^4)}{1+s^2}\,ds\right|
\le\mathscr R_n.
\tag{4.8}
$$



Furthermore,


$$
|r(x)|
=|r_0|(1-x)^d\prod_i\left(1-\frac{x}{\rho_i}\right)
\le |r_0|(1-x)^d
$$


on $[0,1]$. Therefore


$$
0<-e\int_0^1e^{-x}r(x)\,dx
<\frac{3|r_0|}{b}.
$$


Since the channels have the same sign,


$$
\frac12\mathscr R_n<|M_n|
<\mathscr R_n+\frac{3|r_0|}{b}.
$$


The $k=0$ term gives


$$
\mathscr R_n\ge\frac{|r_0|}{n+1/4}.
$$


Using $n=2001b$,


$$
\boxed{
\frac12\mathscr R_n
<|M_n|
<
\left(6004+\frac{3}{4b}\right)\mathscr R_n
<6005\,\mathscr R_n.
}
\tag{4.9}
$$



Finally, applying the actual payment $1/g_n$, not an invented normalization,


$$
\boxed{
\frac{\mathscr R_n}{2g_n}
<q_n(e+\pi)-p_n
<
\left(6004+\frac{3}{4b}\right)\frac{\mathscr R_n}{g_n}
<6005\,\frac{\mathscr R_n}{g_n}.
}
\tag{4.10}
$$



**Decision: A2’s complete nonvanishing theorem and uniform primitive bounds are accepted.**

---

## 5. Independent audit of the short integer charge, with an additional common-divisor lemma

### 5.1 Derivation of the short identity

Repeat the integration-by-parts calculation with $y^{-3/4}$ in place of $v(y)$. The boundary estimates are identical:


$$
\bigl(y^{-3/4}\bigr)^{(j)}
f_{n,k}^{(k-1-j)}
=O(y^{n-k+1/4})
$$


at zero, and the order-$k$ zero handles the endpoint $1$. Consequently,


$$
\int_0^1y^{-3/4}\mathcal W_{n,k}(y)\,dy
=(-1)^kc_{n,k}.
$$


Using (3.6),


$$
\int_0^1y^{-3/4}W(y)\,dy
=(-1)^n\mathscr R_n.
$$


But $W(y)=\sum_{j=0}^dw_jy^j$, so


$$
\int_0^1y^{-3/4}W(y)\,dy
=4\sum_{j=0}^d\frac{w_j}{4j+1}.
$$


Therefore


$$
\boxed{
\mathscr R_n
=4(-1)^n\sum_{j=0}^d\frac{w_j}{4j+1}.
}
\tag{5.1}
$$



This equality is exact. It neither asserts that the summands on the right are positive nor suppresses the absolute values needed in the positive expression (4.7).

### 5.2 Actual factorial divisors and integrality

The forcing term in the $\gamma_j$ recurrence contains


$$
(n-j)!r_{n-j},
$$


and $n-j\ge h$. Because every $r_k$ is an integer, induction gives


$$
h!\mid\gamma_j,\qquad h!\mid w_j.
\tag{5.2}
$$



Define


$$
\Lambda_B=\operatorname{lcm}(1,3,\ldots,4d-1),
$$


and


$$
\Lambda_R=\operatorname{lcm}(1,5,\ldots,4d+1).
$$


Then


$$
\frac{\Lambda_BB_j}{4}\in\mathbb Z,
\qquad
\frac{\Lambda_R}{4j+1}\in\mathbb Z.
$$


Consequently,


$$
T\in\frac{4h!}{\Lambda_B}\mathbb Z,
\qquad
\mathscr R_n\in\frac{4h!}{\Lambda_R}\mathbb Z.
\tag{5.3}
$$



On the original domain,


$$
h=2000b+1>4d+1.
$$


Both $\Lambda_B$ and $\Lambda_R$ divide $h!$, including all prime powers. Thus


$$
\boxed{T\in\mathbb Z,\qquad \mathscr R_n\in\mathbb Z_{>0}.}
\tag{5.4}
$$



The source’s divisibility by $h!/\Lambda_R$ is correct; (5.3) retains the additional factor $4$.

**Decision: the coordinator’s short identity and original-domain integrality theorem are accepted.**

### 5.3 A further proved common divisor

A useful additional consequence is


$$
\boxed{d!\mid F,\ E,\ T,\ \mathscr R_n}
\tag{5.5}
$$


on every original A2 index.

First, $d!\mid F$ follows from $h!\mid F$ and $h\ge d$.

Next write


$$
r(1+u)=u^d\sum_{j=0}^hs_ju^j,\qquad s_j\in\mathbb Z.
$$


The exact endpoint identity gives


$$
E=e\int_1^\infty e^{-x}r(x)\,dx
=\sum_{j=0}^h(d+j)!s_j,
$$


so $d!\mid E$.

For $T$ and $\mathscr R_n$, put


$$
m=h-d=1999b+2.
$$


Then $m\ge4d+1$, and


$$
\frac{h!}{d!}=m!\binom hd.
$$


Both $\Lambda_B$ and $\Lambda_R$ divide $m!$. Hence


$$
d!\mid\frac{h!}{\Lambda_B},
\qquad
d!\mid\frac{h!}{\Lambda_R}.
$$


Equation (5.3) finishes the proof.

This supplies an exact normalized arithmetic form:


$$
\widehat F=\frac F{d!},\quad
\widehat E=\frac E{d!},\quad
\widehat T=\frac T{d!},\quad
\widehat R=\frac{\mathscr R_n}{d!}\in\mathbb Z_{>0},
$$




$$
g_n=d!\,\widehat g_n,\qquad
\widehat g_n=\gcd(|\widehat F|,|\widehat E+\widehat T|).
$$


The decisive ratio is unchanged:


$$
\frac{\mathscr R_n}{g_n}
=\frac{\widehat R}{\widehat g_n}.
\tag{5.6}
$$



This is a proved common-divisor lemma, **not** an evaluation of the final gcd.

### 5.4 Exact remaining A2 alternatives

Equation (4.10) proves, on any infinite subset of the original indices,


$$
q_n(e+\pi)-p_n\longrightarrow0
\quad\Longleftrightarrow\quad
\frac{\mathscr R_n}{g_n}\longrightarrow0.
\tag{5.7}
$$



A sufficient irrationality lemma is therefore


$$
g_n\ge6005\,b\,\mathscr R_n
$$


on an infinite original subset. It would give positive primitive errors below $1/b$.

An obstruction lemma of a different kind would be


$$
g_n\mid C\mathscr R_n
$$


for one fixed positive integer $C$, throughout an eventual original tail. Then $C\mathscr R_n/g_n$ would be a positive integer, giving


$$
q_n(e+\pi)-p_n>\frac1{2C}.
$$



Neither lemma is proved. In valuation form, the latter requires an upper bound


$$
\min\{v_p(F),v_p(E+T)\}
\le v_p(\mathscr R_n)+v_p(C)
$$


for **every prime**, including primes exceeding $b$. The raw factorial divisors do not supply that upper bound.

The leading coefficient also remains visible:


$$
\mathscr R_n
\ge a\,n!\frac{(3/4)_n}{(1/4)_{n+1}}
\sim
a\,n!\frac{\Gamma(1/4)}{\Gamma(3/4)\sqrt n}.
$$


Thus decay would require


$$
\frac{g_n}{a\,n!/\sqrt n}\longrightarrow\infty.
$$


This is a necessary condition, not a contradiction.

---

## 6. Audit of A3’s measures and domination lemma

### 6.1 The exact compact polynomial

For the compact family, retain


$$
k\ge2,\qquad 0\le m<2k,\qquad 0\le j<k.
$$


Define


$$
a_0=1,\qquad a_d=1-da_{d-1},
\qquad c_n=a_{2n}-(-1)^n,
$$




$$
\rho_0=0,\qquad
\rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad
r_n=-(2n)!+4\rho_n.
$$


Let


$$
C_{mj}=c_{m+j},\qquad
\mathcal R_{mj}=r_{m+j},\qquad
w_m=(-1)^m,\qquad v_j=(-1)^j,
$$


and


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5).
$$


The original polynomial is


$$
\boxed{
H_k(s)=\det[C\mid\Lambda_k\mathcal R+s\Lambda_kwv^T]
=H_{0,k}+H_{1,k}s.
}
\tag{6.1}
$$



It is affine because the $s$-dependent block is rank one. It has integer coefficients: the contact entries are integers, and $\Lambda_k$ clears the complete rational corrections through index $3k-2$.

### 6.2 Checking both measures

Integration by parts gives


$$
a_d=\int_0^\infty(1-t)^de^{-t}\,dt.
$$


Indeed, the integral equals $1-d a_{d-1}$.

Under $x=(1-t)^2$, there are two preimages for $0<x<1$ and one for $x>1$. Their Jacobians give


$$
\frac{d\mu}{dx}
=
\begin{cases}
\displaystyle\frac{e^{-1}\cosh\sqrt x}{\sqrt x},
&0<x<1,\\[6pt]
\displaystyle\frac{e^{-1}e^{-\sqrt x}}{2\sqrt x},
&x>1.
\end{cases}
\tag{6.2}
$$


This is a probability measure, with moments $a_{2n}$.

The compact measure is


$$
\int f\,d\nu
=\int_0^1f(t^2)\left(e^t+\frac4{1+t^2}\right)dt,
$$


so its density in $x$ is


$$
\boxed{
\frac{d\nu}{dx}
=\frac{e^{\sqrt x}+4/(1+x)}{2\sqrt x},
\qquad 0<x<1.
}
\tag{6.3}
$$


The signed contact functional remains


$$
L(f)=\int f\,d\mu-f(-1).
\tag{6.4}
$$



Both densities have integrable singularities at zero. In particular, the density of $\nu$ with respect to $dx$ is **not** bounded by $7$. The accepted upper bound uses


$$
e^t+\frac4{1+t^2}<7
$$


in the $t$-coordinate. This distinction is essential, although it does not invalidate the source’s actual bound.

The endpoint integrals give


$$
\int_0^1t^{2n}e^t\,dt=e\,a_{2n}-(2n)!,
$$


and


$$
4\int_0^1\frac{t^{2n}}{1+t^2}\,dt
=\pi(-1)^n+4\rho_n.
$$


Therefore


$$
\nu_n=e\,c_n+(e+\pi)(-1)^n+r_n.
\tag{6.5}
$$



**Decision: the precise densities and complete moment identity are accepted.**

### 6.3 The failed ratio transfer

On the overlap, with $t=\sqrt x$,


$$
\frac{d\mu}{d\nu}(t^2)
=e^{-1}\frac{e^t+e^{-t}}{e^t+4/(1+t^2)}.
$$


Its derivative at $0$ is $-2/(25e)$. At $1$, the derivative numerator, after removal of a positive factor, is


$$
(e-e^{-1})(e+2)-(e+e^{-1})(e-2)=4e-2>0.
$$


The ratio is therefore nonmonotone. It is not completely monotone as a function of $x$, and $\{1,d\mu/d\nu\}$ does not form a two-function Chebyshev system on the overlap.

**Decision: a transfer requiring those hypotheses is rejected.** A3 correctly replaces it with the following independent estimate.

### 6.4 Legendre extrapolation on the exact interval

Let $\deg p\le k-1$, $k\ge2$, and


$$
M(p)=\max_{[-1,1]}|p|.
$$


An orthonormal polynomial basis on $[k^2,4k^2]$ is


$$
\varphi_j(x)=
\sqrt{\frac{2j+1}{3k^2}}\,
\mathcal P_j\!\left(\frac{2x-5k^2}{3k^2}\right).
$$


For $x\in[-1,1]$,


$$
1<
\left|\frac{2x-5k^2}{3k^2}\right|
\le\frac{11}{6}.
$$


The Legendre integral representation yields


$$
|\mathcal P_j(u)|
\le\bigl(|u|+\sqrt{u^2-1}\bigr)^j
<4^j
$$


in this range, since $(11+\sqrt{85})/6<4$.

Writing $p=\sum_{j<k}\alpha_j\varphi_j$, Cauchy–Schwarz gives


$$
|p(x)|^2
\le
\left(\int_{k^2}^{4k^2}p^2\right)
\frac1{3k^2}
\sum_{j=0}^{k-1}(2j+1)16^j.
$$


Because


$$
\sum_{j=0}^{k-1}(2j+1)=k^2,
$$


the final factor is at most $16^{k-1}/3$. Hence


$$
\boxed{
\int_{k^2}^{4k^2}p(x)^2\,dx
\ge\frac3{16^{k-1}}M(p)^2.
}
\tag{6.6}
$$



Every normalization and degree restriction in this extrapolation is correct.

### 6.5 Domination of the overlap and the negative atom

For $y=(y_1,\ldots,y_k)\in[0,1]^k$, put


$$
Q_y(x)=\prod_{j=1}^k(x-y_j).
$$


On $[k^2,4k^2]$,


$$
Q_y(x)\ge(k^2-1)^k,
\qquad
\frac{d\mu}{dx}\ge\frac{e^{-1-2k}}{4k}.
$$


Together with (6.6), this gives


$$
\int_{k^2}^{4k^2}p^2Q_y\,d\mu
\ge
\frac{12}{ek}
\left(\frac{k^2-1}{16e^2}\right)^kM(p)^2.
$$


Using $e<3$, this is at least $A_kM(p)^2$, where


$$
A_k=\frac4k\left(\frac{k^2-1}{144}\right)^k.
$$



On the overlap,


$$
|Q_y(x)|\le1,\qquad \mu([0,1])\le1,
$$


so its possible negative contribution is at least $-M(p)^2$.

The negative atom is retained:


$$
-p(-1)^2Q_y(-1)\ge-2^kM(p)^2.
$$


All remaining exterior contributions are nonnegative. Therefore


$$
\boxed{
L(p^2Q_y)\ge\gamma_kM(p)^2,
\qquad
\gamma_k=A_k-1-2^k.
}
\tag{6.7}
$$



For every $k\ge32$,


$$
\frac{k^2-1}{288}>3,
$$


and hence


$$
A_k
>\frac4k\,2^k3^k
\ge4\cdot2^k.
$$


Thus


$$
\boxed{\gamma_k>3\cdot2^k-1>0.}
\tag{6.8}
$$



This is an all-size proof. It does not depend on a computation at $k=32$.

**Decision: the domination lemma and its constants are accepted.** Its conclusion is positivity on the specified degree space, not positivity of the signed measure $Q_yL$.

---

## 7. Determinant orientation, whole-error sign, and coefficient sign

### 7.1 The same evaluated integer polynomial

Let $s_0=e+\pi$ and $N_{mj}=\nu_{m+j}$. From (6.5), adding $e\Lambda_k$ times contact column $j$ to right column $j$ gives, for every real $s$,


$$
\boxed{
H_k(s)=\Lambda_k^k
\det[C\mid N+(s-s_0)wv^T].
}
\tag{7.1}
$$


In particular,


$$
H_k(s_0)=\Lambda_k^k\Delta_k,
\qquad
\Delta_k=\det[C\mid N].
$$



This is a real identity evaluating the polynomial (6.1). It does not replace its integer coefficients or alter their gcd.

### 7.2 Signed double Andréief with the original column order

Use


$$
V(x)=\prod_{i<j}(x_j-x_i).
$$


The contact columns come first, followed by the compact columns. Accordingly,


$$
V(x_1,\ldots,x_k,y_1,\ldots,y_k)
=V(x)V(y)\prod_{i,j}(y_j-x_i).
$$


Expanding the moment determinant and symmetrizing independently in the two groups proves


$$
\boxed{
\Delta_k
=\frac1{k!^2}
\int V(x)^2V(y)^2
\prod_{i,j}(y_j-x_i)\,
dL^k(x)\,d\nu^k(y).
}
\tag{7.2}
$$



All integrations are justified by absolute polynomial integrability against the total variations of the measures. The unbounded measure has all polynomial moments, and the compact measure is finite.

For fixed $y$, define


$$
M_y=\bigl(L(x^{a+b}Q_y(x))\bigr)_{0\le a,b<k}.
$$


Since


$$
\prod_{i,j}(y_j-x_i)
=(-1)^{k^2}\prod_iQ_y(x_i),
$$


the ordinary determinant integration identity in the $x$-variables gives


$$
\boxed{
(-1)^{k^2}\Delta_k
=\frac1{k!}\int V(y)^2\det M_y\,d\nu^k(y).
}
\tag{7.3}
$$



The sign is $(-1)^{k^2}=(-1)^k$, with no further reversal.

### 7.3 Conditional positive definiteness and the exact moment range

For $p(x)=\sum_{a<k}v_ax^a$, (6.7) implies


$$
v^TM_yv
\ge\gamma_kM(p)^2
\ge\gamma_k\int_0^1p(x)^2\,dx.
$$


Thus


$$
M_y\succeq\gamma_k\mathcal H_k,
\qquad
\mathcal H_k=\left(\frac1{a+b+1}\right)_{a,b<k}.
$$


For $k\ge32$, both matrices are positive definite, and


$$
\det M_y\ge\gamma_k^k\mathfrak h_k,
$$


where


$$
\mathfrak h_k=\det\mathcal H_k
=\frac{\prod_{j=0}^{k-1}(j!)^4}
{\prod_{j=0}^{2k-1}j!}>0.
$$


Consequently,


$$
\boxed{
(-1)^k\Delta_k
\ge\gamma_k^k\mathfrak h_kJ_k^\nu>0,
}
\tag{7.4}
$$


where


$$
J_k^\nu=\frac1{k!}\int V(y)^2\,d\nu^k(y)>0.
$$



The largest degree in $M_y$ is


$$
(k-1)+(k-1)+k=3k-2.
$$


This is exactly the original maximum $m+j$. It corresponds to factorials through $(6k-4)!$ in the original recurrence, and to the final odd clearer entry $6k-5$. No extra moment is introduced.

### 7.4 Independent compression orientation

Let $P_n$ be the monic orthogonal polynomials for $\nu$, and


$$
T^{(k)}_{rj}=L(x^jP_{k+r}(x)).
$$


Replacing the monomial row basis by $P_0,\ldots,P_{2k-1}$ has determinant $1$. The transformed matrix has block form


$$
\begin{pmatrix}A&B\\T^{(k)}&0\end{pmatrix},
\qquad
\det B=J_k^\nu.
$$


Exchanging the two groups of $k$ columns contributes $(-1)^{k^2}$. Therefore


$$
\Delta_k=(-1)^{k^2}J_k^\nu\det T^{(k)}.
$$


Combining this with (7.4),


$$
\boxed{
\det T^{(k)}
\ge\gamma_k^k\mathfrak h_k>0
\qquad(k\ge32).
}
\tag{7.5}
$$



**Decision: A3’s determinant and evaluated-polynomial sign theorem is accepted.**

### 7.5 The affine derivative: one compact atom and annihilation of the charge atom

Equation (7.1) identifies the right block with the moment block of


$$
\nu+(s-s_0)\delta_{-1}.
$$


Differentiating (7.2) at $s=s_0$ places exactly one compact variable at $-1$. There are $k$ identical placements, changing $1/k!^2$ into $1/(k!(k-1)!)$.

Let the remaining compact variables be $y_1,\ldots,y_{k-1}$. Their Vandermonde factor becomes


$$
V(y)^2\prod_{j=1}^{k-1}(1+y_j)^2.
$$


The cross product becomes


$$
\prod_{i=1}^k
\left((-1-x_i)\prod_{j=1}^{k-1}(y_j-x_i)\right)
=(-1)^{k^2}\prod_i\widetilde Q_y(x_i),
$$


where


$$
\widetilde Q_y(x)=(x+1)\prod_{j=1}^{k-1}(x-y_j).
$$



If an $L$-variable is at its negative atom $-1$, then $\widetilde Q_y(-1)=0$. Hence all such terms vanish exactly. This is why the surviving charge integrations use $\mu$; the negative atom has not been arbitrarily discarded.

Define


$$
\widetilde M_y
=\left(\int x^{a+b}\widetilde Q_y(x)\,d\mu(x)\right)_{a,b<k}.
$$


Integrating the $x$-variables yields


$$
\boxed{
\frac{(-1)^kH_{1,k}}{\Lambda_k^k}
=
\frac1{(k-1)!}
\int
V(y)^2\prod_{j=1}^{k-1}(1+y_j)^2
\det\widetilde M_y\,d\nu^{k-1}(y).
}
\tag{7.6}
$$



On the exterior interval,


$$
\widetilde Q_y(x)
\ge(k^2+1)(k^2-1)^{k-1}
\ge(k^2-1)^k.
$$


On $[0,1]$, $|\widetilde Q_y|\le2$. Repeating the already proved domination estimate gives


$$
\widetilde M_y\succeq(A_k-2)\mathcal H_k.
$$


For $k\ge32$, $A_k-2>0$. Therefore


$$
\boxed{(-1)^kH_{1,k}>0.}
\tag{7.7}
$$



The moments again stop at degree $3k-2$.

**Decision: the affine-coefficient theorem is accepted, including its sign and identification with the original integer coefficient.**

---

## 8. Actual primitive consequences, retained producer boundaries, and open lemmas

### 8.1 Compact arithmetic ledger

The real-variable proof does not evaluate or change the established payments


$$
\prod_{m=k}^{2k-1}e_{k,m}
=\frac{|\det C_k|}{\delta_{k,2k-1}}.
$$


For a saturated integer kernel basis $X$, retain


$$
B_{rj}=\sum_mX_{rm}r_{m+j},
$$




$$
L_X=
\frac{\Lambda_k}
{\gcd\!\left(\Lambda_k,\{\Lambda_kB_{rj}\}_{r,j}\right)}.
$$


If


$$
L_X^k\det\mathcal M_X(s)=A_0+A_1s,
$$


the least simultaneous coefficient clearer remains


$$
\frac{L_X^k}{\gcd(L_X^k,A_0,A_1)},
$$


and the remaining integer content is


$$
\frac{\gcd(A_0,A_1)}
{\gcd(L_X^k,A_0,A_1)}.
$$



The final block-coefficient gcd is


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
$$


over all primes. For $k\ge32$,


$$
q_k=\frac{|H_{1,k}|}{G_k},
\qquad
p_k=-\frac{(-1)^kH_{0,k}}{G_k}.
$$


The new signs imply


$$
\boxed{
q_k(e+\pi)-p_k
=\frac{|H_k(e+\pi)|}{G_k}>0.
}
\tag{8.1}
$$



The established complete upper bound remains


$$
|H_k(e+\pi)|\le F_k^\perp,
$$




$$
F_k^\perp
=\Lambda_k^k21^kk!h_k
\prod_{r=0}^{k-1}(2k+4r)!,
$$


with


$$
h_k=
\frac{2^{k(k-1)}(\prod_{j=1}^{k-1}j!)^2}
{\prod_{r,j=0}^{k-1}(2r+2j+1)}.
$$


Together with the new lower bound,


$$
\boxed{
\frac{\Lambda_k^kJ_k^\nu\gamma_k^k\mathfrak h_k}{G_k}
\le q_k(e+\pi)-p_k
\le\frac{F_k^\perp}{G_k}.
}
\tag{8.2}
$$



Neither bound evaluates $G_k$. The established divisor


$$
D_{k-1}=\prod_{r=0}^{k-2}(r!)^2\mid G_k
$$


remains only a lower divisor. Its use in the upper bound leaves


$$
\log(F_k^\perp/D_{k-1})
=3k^2\log k+O(k^2),
$$


which proves insufficiency of those estimates, not divergence of the actual primitive errors.

### 8.2 Exact infinite domains and the distinct original producers

A3’s theorem holds on all integers $k\ge32$, and therefore on the explicit infinite compact index set


$$
k=9^{18+32u},\qquad u\ge0.
$$



This is not an identification with the original binary producer. That producer retains


$$
b=9^{18+32u},\qquad n=4002b,
$$


contact range $0,\ldots,b-1$, physical reconstruction range $0,\ldots,b$, and


$$
z_b=0.
$$


Its complete corrected columns remain


$$
x=\frac12RA^{-1}f,\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad x=2^ax_0.
$$


Its full return remains


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f,
$$


with the paid consequence


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1}.
$$



No compact sign estimate removes $h^F$, $e_0$, $z_b=0$, or the subtraction of $a$. Nor does it evaluate that producer’s norm $x_0^Tx_0$, actual corrected-column contents, simultaneous clearer, or final gcd. The quoted binary valuation


$$
v_3(q)=n-\frac{b+15}{2}
$$


is not transferred.

Likewise, the older A2 producer is not completely specified in this packet. The audited Laguerre matrix does not settle an undocumented identification with its forcing, returns, or physical terminal. The separate original ternary boundary-column obligation remains separate.

### 8.3 The remaining sufficient lemmas

For A2, a sufficient original-domain lemma is


$$
\frac{\mathscr R_n}{g_n}\longrightarrow0
$$


on an explicitly specified infinite subset of the original admissible progression.

For the compact family, a sufficient lemma on an explicit infinite set of $k\ge32$ is


$$
\frac{F_k^\perp}{G_k}\longrightarrow0.
$$


A weaker and more directly relevant sufficient statement is


$$
\frac{\Lambda_k^kJ_k^\nu\det T^{(k)}}{G_k}
\longrightarrow0.
\tag{8.3}
$$



The required coefficient and whole-error nonvanishing premises are now proved on those same domains. If either decay statement were proved there, rationality $e+\pi=A/B$ would be impossible, because every nonzero integer linear form would satisfy


$$
|q(e+\pi)-p|=\frac{|qA-pB|}{B}\ge\frac1B.
$$



At present, these decay lemmas remain open.

---

## 9. Acceptance ledger and bounded exact-arithmetic receipts

### 9.1 Decisions

| Claim | Independent decision |
|---|---|
| A2 monomial Rodrigues identity | **Accepted** |
| Complete monotonicity and both derivative bounds for $v$ | **Accepted** |
| All integration-by-parts endpoint cancellations | **Accepted** |
| Integrated arctangent sign on the stated construction | **Accepted** |
| Gaussian exactness through $2N-1$, largest factorial $(2n)!$ | **Accepted** |
| Node bound $b^2/(8004b+2)$ and modified-root inclusion | **Accepted** |
| $M_n<0$ at every original A2 index | **Accepted** |
| Paid bounds with $\ell=1$ and the actual $g_n$ | **Accepted** |
| Short identity for $\mathscr R_n$ | **Accepted** |
| Original-domain integrality of $\mathscr R_n$ | **Accepted** |
| Common divisor $d!\mid F,E,T,\mathscr R_n$ | **Proved here** |
| Fixed-$C$ assertion $g_n\mid C\mathscr R_n$ | **Open; not accepted as a theorem** |
| Monotone-ratio/Chebyshev transfer for the actual compact densities | **Rejected: hypotheses fail** |
| A3 exterior Legendre estimate and all-$k\ge32$ domination | **Accepted** |
| Signed double-Andréief orientation | **Accepted** |
| Conditional positive definiteness and moment boundary $3k-2$ | **Accepted** |
| $\det T^{(k)}>0$, $(-1)^kH_k(e+\pi)>0$ | **Accepted for every $k\ge32$** |
| Derivative formula and $(-1)^kH_{1,k}>0$ | **Accepted for every $k\ge32$** |
| Any gcd inference from real row or column operations | **Not justified** |
| Primitive decay in either family | **Open** |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

### 9.2 No finite computation is needed for the accepted global proofs

No closed Smith, Family005, or mixed-normalization calculation needs repetition. The compact sign theorem is independent of the Family090 interval premises.

The following optional receipts would check transcription and orientation only. They are bounded mathematical tasks with explicit expected outputs.

#### Receipt A: monomial normalization

**Inputs**


$$
n=2,\qquad k=0,1,2,
$$




$$
B_0=0,\quad B_1=\frac83,\quad B_2=\frac{304}{105}.
$$



**Expected exact outputs**


$$
\mathcal W_{2,0}=y^2,
$$




$$
\mathcal W_{2,1}=3y^2-2y,
$$




$$
\mathcal W_{2,2}=12y^2-12y+2,
$$


and


$$
c_{2,0}=\frac49,\qquad
c_{2,1}=\frac4{15},\qquad
c_{2,2}=\frac{56}{15}.
$$


Using $\int_0^1v(y)y^j\,dy=\pi-B_j$, the exact signed moments are


$$
C_{2,0}=\pi-\frac{304}{105},
$$




$$
C_{2,1}=\frac{352}{105}-\pi,
$$




$$
C_{2,2}=2\pi-\frac{96}{35}.
$$



These are algebraic normalization checks, not original-index evidence.

#### Receipt B: determinant and derivative orientation

This receipt uses deliberately auxiliary atomic measures; it does not test A3’s $k\ge32$ positivity estimate.

**Inputs**


$$
k=2,\qquad
\mu=\delta_2+\delta_3,\qquad
L=\mu-\delta_{-1},\qquad
\nu=\delta_0+\delta_1.
$$


Their relevant moments are


$$
(L(x^m))_{m=0}^4=(1,6,12,36,96),
$$




$$
(\nu(x^m))_{m=0}^4=(2,1,1,1,1).
$$


Form


$$
\Delta(t)=
\det\bigl[(L(x^{m+j}))\mid
(\nu(x^{m+j})+t(-1)^{m+j})\bigr]_
{\substack{0\le m<4\\0\le j<2}}.
$$



**Expected exact output**


$$
\boxed{\Delta(t)=-216+168t.}
$$



The derivative formula gives $168$ independently:


$$
12(2-0)(3-0)(1+0)^2
+
12(2-1)(3-1)(1+1)^2
=72+96=168.
$$


Here the charge atom vanishes because of the factor $x+1$. The negative value $\Delta(0)$ also illustrates why signed-measure determinant positivity cannot be asserted without the domination hypothesis.

No inference beyond this finite algebraic scope is warranted.

---

## 10. Final research status

The substantive analytic advance is now established:

- In A2’s original Laguerre matrix, the two complete channels have the same strict sign, so the whole error never vanishes on the original admissible indices.
- Its positive beta bound is also an exact short integer charge, with the original polynomial content and all factorial divisors retained.
- In the compact family, exterior polynomial domination controls both the overlapping-support contribution and the negative atom on exactly the degree space required by the determinant. It proves nonvanishing of both the affine coefficient and the whole evaluated polynomial for every $k\ge32$.

The precise remaining bottleneck is no longer a missing global sign proof for these two families. It is


$$
\boxed{
\text{an all-prime arithmetic/asymptotic comparison with the actual final gcd,
on the same infinite indices.}
}
$$



For A2 that comparison is $\mathscr R_n/g_n$; for the compact family it is $|H_k(e+\pi)|/G_k$. The proved raw divisors, the real orthogonal transformations, and the finite receipts do not determine either ratio.

Accordingly, the report establishes the two global nonvanishing theorems and their exact primitive consequences, but establishes **neither a vanishing primitive-error sequence nor an unconditional theorem on the rationality or irrationality of $e+\pi$**.
