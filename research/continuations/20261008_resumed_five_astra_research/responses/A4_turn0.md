> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the complete Laguerre obstruction

## Assignment A4, Turn 0

### Executive verdict

**The obstruction in A2 Turn 18 is correct for the displayed original Laguerre matrix family.** Its essential comparisons, including their signs, finite-degree requirements, and arithmetic transfer to the actual primitive denominator, survive independent derivation.

At every admissible original index


$$
b=3^{249005515+574312172u},\qquad
n=2001b,\qquad d=b-1,\qquad h=2000b+1,
$$


with


$$
u\equiv2\pmod{29^9}
$$


and all other original admissibility conditions retained, one has


$$
\frac{|F|}{R}
\le
B_b:=
\frac{\sqrt{2b-1}}{4e}+2001+\frac1{4b}
<\sqrt b.
$$


For the **actual** all-prime reduction


$$
g=\gcd(|F|,|E+T|),\qquad
q=\frac{|F|}{g},
$$


the established denominator restriction $h\mid q$, independently checked below in the original objects, therefore gives


$$
\frac gR\le\frac{B_b}{h}<\frac1{2000\sqrt b}.
$$


Consequently, the complete primitive error satisfies


$$
\boxed{q(e+\pi)-p>1000\sqrt b.}
$$



This holds pointwise on the original admissible domain. Thus it excludes primitive-error decay on **every unbounded admissible collection from this family**, including any unbounded admissible collection in the previously surviving progression.

The signed-tail margin claimed in A2 Turn 18 is also valid, with $C=1$. Its proof does not require pointwise positivity of the previously problematic signed comparison kernel.

Three scope qualifications are indispensable:

1. The contact-deformation argument works through an **exact positive discrete quadrature representation**. A direct continuous-support Markov shortcut would not have the required hypotheses.
2. The restricted-measure argument proves positivity of an **integrated kernel functional**, not pointwise positivity of the reproducing kernel.
3. The conclusion concerns this Laguerre matrix only. It does **not** retire the compact mixed pencil or the distinct older prime-$29$ producer.

No unconditional proof of rationality or irrationality of $e+\pi$ follows.

---

## 1. Original objects and arithmetic normalization

### 1.1 Exact domain

Throughout this report, $u$ remains in its original admissible domain. No extension of that domain is made. In particular,


$$
b=3^{249005515+574312172u},\quad
n=2001b,\quad d=b-1,\quad h=n-d=2000b+1.
$$


At every original index,


$$
b,n,h\ \text{are odd},\qquad d\ \text{is even},\qquad b\ge10^9.
$$



The argument is pointwise. It does not require a new assertion that any particular intersection with additional admissibility conditions is infinite.

In particular, it applies to


$$
u=2+29^9(1+6068205v),\qquad v\ge0,
$$


whenever those indices satisfy all original admissibility conditions.

### 1.2 The finite matrix and complete corrections

The matrix is exactly


$$
H_{rj}(X)=X-A_{n+r,j}-B_j,\qquad 0\le r,j\le d,
$$


where


$$
A_{m,j}
=j!\sum_{v=0}^{m-j}(-1)^v
\binom{m-j}{v}\frac1{(j+v)!},
$$


and


$$
B_j=4\sum_{v=0}^{2j-1}\frac{(-1)^v}{2v+1},
\qquad B_0=0.
$$



Thus:

- the physical rows are $n,n+1,\ldots,n+d$;
- the physical terminal is $n+d$;
- the columns are $0,1,\ldots,d$;
- every summand in every corrected column $B_j$ is retained.

Write


$$
\mathsf A_{rj}=A_{n+r,j}+B_j,\qquad
\mathsf W_{rj}=(n+r)!\mathsf A_{rj}.
$$


The actual contents and clearers remain


$$
\kappa_r
=\gcd\bigl((n+r)!,\mathsf W_{r0},\ldots,\mathsf W_{rd}\bigr),
\qquad
C_r=\frac{(n+r)!}{\kappa_r},
$$




$$
Y_{rj}=C_r\mathsf A_{rj},\qquad
c_j=\gcd_{0\le r\le d}(C_r,Y_{rj}),
$$




$$
\mathcal L_n=\operatorname{lcm}_{0\le r\le d}C_r,\qquad
P_n=\frac{\prod_{r=0}^d C_r}{\prod_{j=0}^d c_j}.
$$


Hence


$$
D_n(X)
=
\det\left[\frac{C_rX-Y_{rj}}{c_j}\right]_{r,j=0}^d
=P_n\det H(X)=U_nX-V_n.
$$



The previously established paid reduction is


$$
D_n(X)
=
\frac{P_n\tau_n}{aK_n}(FX-E-T),
\tag{1.1}
$$


where


$$
K_n=
\frac{\prod_{r=0}^d(n+r)!}
{\prod_{j=0}^d j!(n-j)!},
$$


and


$$
\tau_n=
\frac{(-1)^n}{n!}
\frac{\prod_{s=0}^{d-1}s!}{\prod_{j=h}^{n-1}j!}
\frac{\Delta_h}{\Delta_h^{(0)}},
\qquad
\Delta_h^{(0)}=\prod_{i=0}^{h-1}i!(i+b)!.
$$


Here $\Delta_h$ is the degree-$h$ Gram determinant for


$$
x^b(x-1)^de^{-x}\,dx.
$$



All factors in (1.1) are retained. In particular, the analytic comparisons below do not supply any new integer division by $a$, a norm, a kernel value, or a comparison charge.

### 1.3 The actual primitive polynomial and charges

Let $p_h$ be the monic degree-$h$ orthogonal polynomial for


$$
d\mu(x)=x^b(x-1)^de^{-x}\,dx,\qquad x>0.
$$


The measure is positive because $d$ is even. Its moments are integers:


$$
\mu_\ell
=
\sum_{j=0}^d(-1)^{d-j}\binom dj(\ell+b+j)!.
$$


Thus $p_h\in\mathbb Q[x]$.

Let $a>0$ be its **least coefficient clearer**, and set


$$
r(x)=a(x-1)^dp_h(x)=\sum_{k=0}^nr_kx^k.
$$


Minimality of $a$ makes $ap_h$ primitive, and Gauss’s lemma makes $r$ primitive.

The retained charges are


$$
F=\sum_{k=0}^nr_kk!,
\qquad
E=\sum_{k=0}^nr_k\sum_{v=0}^k\frac{k!}{v!},
$$


and the complete forced triangular recurrence is


$$
\gamma_j
=
(-1)^{n-j}(n-j)!r_{n-j}
-\sum_{i<j}\binom{n+1}{j-i}\gamma_i,
\qquad 0\le j\le d.
$$


Define


$$
w_j=\binom nj\gamma_j,\qquad
W(y)=\sum_{j=0}^dw_jy^j,\qquad
T=\sum_{j=0}^dw_jB_j.
$$


No forcing term or return summand is removed.

The established identities include


$$
F=\sum_{j=0}^dw_j<0,
$$




$$
R
=
\sum_{k=0}^n|r_k|c_{n,k},
\qquad
c_{n,k}
=
\frac{k!(3/4)_k}{(n-k+1/4)_{k+1}},
\tag{1.2}
$$


and, since $n$ is odd,


$$
R=-4\sum_{j=0}^d\frac{w_j}{4j+1}>0.
\tag{1.3}
$$


Here $(z)_m=z(z+1)\cdots(z+m-1)$, with $(z)_0=1$.

On the original domain,


$$
\ell=1,\qquad T\in\mathbb Z,\qquad R\in\mathbb Z_{>0}.
$$


These are actual combined-charge statements, not replacements of the actual denominators by oversized lcms.

The actual primitive pair is


$$
g=\gcd(|F|,|E+T|),\qquad
q=-\frac Fg>0,\qquad
p=-\frac{E+T}{g}.
\tag{1.4}
$$


The determinant’s final gcd is


$$
G_n=\gcd(U_n,|V_n|)
=U_n\frac g{|F|}.
\tag{1.5}
$$



### 1.4 The whole error being estimated

The complete error is


$$
M=F(e+\pi)-E-T
=
e\int_0^1e^{-x}r(x)\,dx
+
4\int_0^1\frac{W(s^4)}{1+s^2}\,ds.
\tag{1.6}
$$


Both channels and their complete endpoint corrections are present.

I reuse the already proved Laguerre whole-error theorem at exactly this scope:


$$
M<0,
\qquad
\frac R2<|M|<6005R.
\tag{1.7}
$$


Consequently,


$$
\frac{R}{2g}
<
q(e+\pi)-p
<
6005\frac Rg.
\tag{1.8}
$$



For clarity about this dependency: the closed proof uses the complete arctangent density


$$
\frac{y^{-3/4}}{1+\sqrt y},
$$


not the pointwise sign of $W$. It gives an arctangent-channel magnitude between $R/2$ and $R$. The exponential channel has the same strict sign and magnitude less than $3|r_0|/b$. Together with


$$
R\ge\frac{|r_0|}{n+1/4},
$$


this yields (1.7). The root hypothesis needed there is independently validated in Section 3 below.

---

## 2. A reciprocal divided-difference identity

The same elementary identity underlies both exterior comparisons.

Let $\pi_m$ be the monic orthogonal polynomial of degree $m$ for a positive measure $\sigma$, with distinct zeros $\xi_1,\ldots,\xi_m$. Assume the moment matrices needed for these polynomials are positive definite and the following integrals exist.

If $I_{m-1}f$ interpolates $f$ at the zeros, then


$$
f(x)-I_{m-1}f(x)
=
\pi_m(x)f[\xi_1,\ldots,\xi_m,x].
$$


Orthogonality gives the exact identity


$$
\int\pi_m f\,d\sigma
=
\int\pi_m^2
f[\xi_1,\ldots,\xi_m,x]\,d\sigma.
\tag{2.1}
$$



For positive $t_0,\ldots,t_m$ and an integer $j\ge1$,


$$
(-1)^m(t^{-j})[t_0,\ldots,t_m]
=
\left(\prod_{i=0}^m t_i^{-1}\right)
h_{j-1}(t_0^{-1},\ldots,t_m^{-1}),
\tag{2.2}
$$


where $h_r$ denotes the complete homogeneous symmetric polynomial.

One direct verification uses


$$
\sum_{j\ge1}t^{-j}z^{j-1}=\frac1{t-z}.
$$


The divided difference of the right side is


$$
(-1)^m\prod_{i=0}^m(t_i-z)^{-1}.
$$


Expanding this product in $z$ gives (2.2).

It follows that, whenever the support lies to the right of $-s$,


$$
(-1)^m
\int \pi_m(x)(x+s)^{-j}\,d\sigma(x)>0.
\tag{2.3}
$$



All applications below meet the integrability requirements. For $s>0$, there is no singularity on the support. At $s=0$, the reciprocal singularity is canceled by the corresponding power in the weight; the remaining growth is polynomial times an exponential.

**Verdict:** A2’s sign lemma is valid in its applications. It is an integrated orthogonal-polynomial statement, not a positivity assertion about an arbitrary comparison kernel.

---

## 3. Exact contact deformation on the original finite degree range

### 3.1 Quadrature size and node location

Use the base measure


$$
d\mu_0(x)=x^be^{-x}\,dx
$$


and put


$$
N=h+\frac d2=\frac{4001b+1}{2}.
$$


This is an integer, and


$$
2N-1=d+2h-1.
\tag{3.1}
$$



The $N$-node Gaussian rule is exact through degree $2N-1$. Its nodes are the eigenvalues of the finite Laguerre Jacobi matrix with diagonal


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
\le
t+\frac b2-\frac{b^2}{8(t+b/2)}.
$$


Therefore a Gershgorin lower estimate gives


$$
\lambda_i\ge
\frac{b^2}{4N+2b}
=
\frac{b^2}{8004b+2}
=:L_b.
\tag{3.2}
$$


At the last Jacobi row, subtracting a nonexistent outward neighbor only weakens the lower bound; it does not enlarge the finite matrix.

Since every original $b\ge10^9$, in particular $b\ge8005$, and


$$
b(b-8004)>2,
$$


we have


$$
L_b>1.
\tag{3.3}
$$



The largest factorial needed by this quadrature construction is


$$
(b+2N-1)!=(2n)!.
\tag{3.4}
$$


There is no requirement for $(2n+1)!$.

### 3.2 The discrete representation is exact for every contact parameter

For $0\le t\le1$, let $p_{h,t}$ be the monic degree-$h$ orthogonal polynomial for


$$
x^b(x-t)^de^{-x}\,dx.
$$


For every polynomial $v$ with $\deg v<h$,


$$
\deg\bigl((x-t)^dp_{h,t}(x)v(x)\bigr)
\le d+2h-1=2N-1.
$$


Thus its orthogonality equations are exactly those for


$$
d\sigma_t
=
\sum_{i=1}^N\omega_i(\lambda_i-t)^d\delta_{\lambda_i}.
\tag{3.5}
$$


Every weight is strictly positive because $\lambda_i>1\ge t$.

Moreover,


$$
N-h=\frac d2>0.
$$


Hence the finite measure has more support points than the degree of $p_{h,t}$. Its degree-$h$ orthogonal polynomial has simple zeros in the convex hull of those nodes. In particular,


$$
\xi_i(t)\ge L_b>1.
\tag{3.6}
$$



This is the decisive hypothesis validation. On the original continuous support, $-d/(x-t)$ has a pole and jumps across $x=t$; one cannot simply cite a continuous-support monotonicity theorem there.

### 3.3 Independent derivation of zero motion

Fix one zero $\xi(t)$ and write


$$
p(x)=p_{h,t}(x),\qquad
\ell(x)=\frac{p(x)}{x-\xi(t)}.
$$


The finite moment matrix is positive definite and depends analytically on $t$. Thus the coefficients and the simple ordered zeros are differentiable.

The logarithmic derivative of the weights in (3.5) is


$$
s_t(x)=-\frac d{x-t}.
$$


Differentiating


$$
\int p(x)\ell(x)\,d\sigma_t(x)=0
$$


gives


$$
\int (\partial_t p)\ell\,d\sigma_t
+
\int p\ell\,s_t\,d\sigma_t=0.
$$


The term involving $\partial_t\ell$ vanishes by orthogonality.

At $x=\xi$,


$$
\partial_t p(\xi)=-p'(\xi)\xi'=-\ell(\xi)\xi'.
$$


Consequently,


$$
\partial_t p(x)=-\xi'\ell(x)+(x-\xi)v(x)
$$


for some polynomial $v$ of degree at most $h-2$. The contribution of the second term to $\int(\partial_t p)\ell\,d\sigma_t$ is


$$
\int p(x)v(x)\,d\sigma_t(x)=0.
$$


Therefore


$$
\boxed{
\xi'(t)=
\frac{\displaystyle
\int (x-\xi)\ell(x)^2s_t(x)\,d\sigma_t(x)}
{\displaystyle\int\ell(x)^2\,d\sigma_t(x)}.
}
\tag{3.7}
$$



Also,


$$
\int(x-\xi)\ell(x)^2\,d\sigma_t(x)=0.
$$


Subtracting $s_t(\xi)$ in the numerator gives


$$
(x-\xi)\bigl(s_t(x)-s_t(\xi)\bigr)
=
\frac{d(x-\xi)^2}{(x-t)(\xi-t)}.
$$


Thus a more explicit version is


$$
\boxed{
\xi'(t)
=
\frac{d}{\xi-t}
\frac{\displaystyle
\sum_{i=1}^N
\omega_i(\lambda_i-t)^{d-1}p_{h,t}(\lambda_i)^2}
{\displaystyle
\sum_{i=1}^N
\omega_i(\lambda_i-t)^d\ell(\lambda_i)^2}.
}
\tag{3.8}
$$



Every denominator is positive. Since $h<N$, $p_{h,t}$ cannot vanish at every quadrature node. Therefore, on the original domain,


$$
\xi'(t)>0.
\tag{3.9}
$$



A2 only needs nondecreasing zeros; the original hypotheses actually give strict increase.

**Verdict:** the zero-motion formula and its sign are correct. The proof uses the exact finite measure and does not import an inapplicable continuous-support hypothesis.

### 3.4 Coefficient monotonicity with the same original clearer

Define the auxiliary monic polynomial


$$
r^{[t]}(x)=(x-t)^dp_{h,t}(x).
$$


Its zeros consist of $d$ copies of $t$ and the $h$ zeros of $p_{h,t}$. All are nonnegative and nondecreasing with $t$.

For a monic polynomial with nonnegative zeros, the absolute coefficients are elementary symmetric functions of those zeros. They are nondecreasing in every zero. Hence


$$
\left|[x^k]r^{[1]}\right|
\ge
\left|[x^k]r^{[0]}\right|
\qquad(0\le k\le n).
$$


Since every $c_{n,k}>0$,


$$
\boxed{
R\ge aR^{[0]},
\qquad
R^{[0]}=
\sum_{k=0}^n
\left|[x^k]r^{[0]}(x)\right|c_{n,k}.
}
\tag{3.10}
$$



The multiplier is the **same actual $a$** from the original polynomial. There is no replacement by an auxiliary polynomial’s clearer.

---

## 4. Complete evaluation of the Laguerre comparison charge

At $t=0$,


$$
x^b(x-t)^de^{-x}=x^{b+d}e^{-x}
=x^{2d+1}e^{-x}.
$$


Set


$$
\alpha=2d+1.
$$


Then


$$
p_{h,0}(x)=(-1)^hh!L_h^{(\alpha)}(x),
\qquad
r^{[0]}(x)=x^dp_{h,0}(x).
$$



### 4.1 The factorial functional

The finite Laguerre expansion gives


$$
\int_0^\infty x^de^{-x}L_h^{(\alpha)}(x)\,dx
=
\frac{d!(\alpha+1)_h}{h!}
\sum_{j=0}^h
\frac{(-h)_j(d+1)_j}{j!(\alpha+1)_j}.
$$


The terminating Vandermonde evaluation is


$$
\sum_{j=0}^h
\frac{(-h)_j(d+1)_j}{j!(\alpha+1)_j}
=
\frac{(\alpha-d)_h}{(\alpha+1)_h}.
$$


At these parameters it follows directly by integrating


$$
(1-t)^h=\sum_{j=0}^h\frac{(-h)_j}{j!}t^j
$$


against a beta density with positive parameters $d+1$ and $\alpha-d$.

Therefore


$$
\int_0^\infty e^{-x}r^{[0]}(x)\,dx
=
(-1)^h d!(\alpha-d)_h.
$$


Since $\alpha-d=d+1=b$,


$$
d!(d+1)_h=n!,
$$


and hence


$$
\boxed{
\int_0^\infty e^{-x}r^{[0]}(x)\,dx=(-1)^hn!.
}
\tag{4.1}
$$



### 4.2 Reduction of the complete beta charge to a finite balanced sum

The absolute coefficient of $x^{d+j}$ is


$$
h!\binom{h+2d+1}{h-j}\frac1{j!},
\qquad 0\le j\le h.
$$


Putting $l=h-j$, substitution into the actual weights (1.2) gives


$$
R^{[0]}
=
\frac{n!(3/4)_n\Gamma(1/4)}{\Gamma(n+5/4)}
\sum_{l=0}^h
\frac{(-h)_l(-h-2d-1)_l(1/4)_l}
{(-n)_l(1/4-n)_l\,l!}.
\tag{4.2}
$$



This is the entire coefficient charge. No initial or terminal coefficients have been omitted.

### 4.3 Derivation and legitimate specialization of Pfaff–Saalschutz

For a nonnegative integer $m$, the terminating identity is


$$
\sum_{k=0}^m
\frac{(-m)_k(A)_k(B)_k}
{k!(C)_k(1+A+B-C-m)_k}
=
\frac{(C-A)_m(C-B)_m}
{(C)_m(C-A-B)_m}.
\tag{4.3}
$$



For completeness, it can be derived without leaving the finite polynomial setting. Taylor expansion at $t=1$, followed by the terminating Vandermonde identity, gives


$$
{}_2F_1(-m,A;C;t)
=
\frac{(C-A)_m}{(C)_m}
{}_2F_1(-m,A;1+A-C-m;1-t).
\tag{4.4}
$$


For example, the coefficient of $(1-t)^k$ on the left is


$$
\frac{(-1)^k(-m)_k(A)_k(C-A)_{m-k}}
{(C)_m k!}.
$$


Using


$$
(C-A)_{m-k}
=
\frac{(-1)^k(C-A)_m}{(1+A-C-m)_k}
$$


gives (4.4).

Let $D=1+A-C-m$. Where $B,D>0$, integrate (4.4) against the normalized beta density with parameters $B,D$. Termwise integration cancels the denominator $(D)_k$ on the transformed side, leaving a terminating Vandermonde sum. The result is (4.3). Clearing denominators then extends it as a rational identity to every nonsingular specialization.

For (4.2), take


$$
m=h,\qquad
A=-h-2d-1,\qquad
B=\frac14,\qquad
C=-n.
$$


Then


$$
1+A+B-C-m=\frac14-n,
$$


so the balance condition is exact. Also,


$$
C-A=d+1,\qquad
C-B=-n-\frac14,\qquad
C-A-B=d+\frac34.
$$


Therefore


$$
\sum_{l=0}^h
\frac{(-h)_l(-h-2d-1)_l(1/4)_l}
{(-n)_l(1/4-n)_l\,l!}
=
\frac{(d+1)_h(-n-1/4)_h}
{(-n)_h(d+3/4)_h}.
\tag{4.5}
$$



The negative integer $C=-n$ causes no problem:

- the sum stops at $h\le n$;
- $(-n)_l\ne0$ for $0\le l\le h$;
- $(1/4-n)_l\ne0$;
- $(d+3/4)_h>0$.

In particular, the derivation does **not** evaluate a beta integral at negative shape parameters. The actual specialization is made only after obtaining the finite rational identity.

This is the classical terminating Pfaff–Saalschutz identity recorded in the supplied DLMF reference, not a new special-function theorem.

### 4.4 Final simplification

We have


$$
\frac{(3/4)_n}{(d+3/4)_h}=(3/4)_d,
$$


and


$$
\frac{(-n-1/4)_h}{(-n)_h}
=
\frac{\Gamma(n+5/4)}{\Gamma(d+5/4)}
\frac{d!}{n!}.
$$


Using $d!(d+1)_h=n!$ in (4.2)–(4.5) gives


$$
\boxed{
R^{[0]}
=
4n!\frac{(3/4)_d}{(5/4)_d}.
}
\tag{4.6}
$$


Consequently,


$$
\boxed{
R\ge4an!\frac{(3/4)_d}{(5/4)_d}.
}
\tag{4.7}
$$



**Verdict:** the full charge evaluation, including its normalization and terminating denominator conditions, is correct.

---

## 5. Exterior Christoffel monotonicity

Fix integers $b\ge1,d\ge0$. For $s\ge0$, let $\pi_{m,s}$ be monic orthogonal for


$$
d\sigma_s(y)=(y+s)^by^de^{-y}\,dy,\qquad y>0,
$$


and define


$$
C_m(s)=\int_0^\infty\pi_{m,s}(y)y^de^{-y}\,dy.
$$



### 5.1 Signs of the two functionals

For $s>0$,


$$
C_m(s)
=
\int\pi_{m,s}(y)(y+s)^{-b}\,d\sigma_s(y).
$$


The reciprocal sign identity gives


$$
(-1)^mC_m(s)>0.
\tag{5.1}
$$


Similarly, with


$$
J_m(s)
=
\int\frac{\pi_{m,s}(y)}{y+s}\,d\sigma_s(y),
$$


one has


$$
(-1)^mJ_m(s)>0.
\tag{5.2}
$$



### 5.2 The exact derivative formula

Let


$$
K_{m-1,s}(y,z)
=
\sum_{k=0}^{m-1}
\frac{\pi_{k,s}(y)\pi_{k,s}(z)}
{\|\pi_{k,s}\|_{\sigma_s}^2}.
$$


Since $\partial_s\pi_{m,s}$ has degree at most $m-1$, differentiate its orthogonality against $\pi_{k,s}$, $k<m$:


$$
\int(\partial_s\pi_{m,s})\pi_{k,s}\,d\sigma_s
=
-b\int
\frac{\pi_{m,s}(y)\pi_{k,s}(y)}{y+s}\,d\sigma_s(y).
$$


The derivative of $\pi_{k,s}$ contributes zero by orthogonality.

Now


$$
\frac{\pi_{k,s}(y)-\pi_{k,s}(-s)}{y+s}
$$


has degree $k-1<m$. Therefore


$$
\int
\frac{\pi_{m,s}\pi_{k,s}}{y+s}\,d\sigma_s
=
\pi_{k,s}(-s)J_m(s).
$$


Expanding in the orthogonal basis proves


$$
\boxed{
\partial_s\pi_{m,s}(y)
=
-bJ_m(s)K_{m-1,s}(y,-s).
}
\tag{5.3}
$$



Integrating against the fixed measure $y^de^{-y}\,dy$ gives


$$
C_m'(s)
=
-bJ_m(s)
\sum_{k=0}^{m-1}
\frac{\pi_{k,s}(-s)C_k(s)}
{\|\pi_{k,s}\|_{\sigma_s}^2}.
\tag{5.4}
$$



All zeros of $\pi_{k,s}$ are positive, so $\pi_{k,s}(-s)$ has sign $(-1)^k$. By (5.1), $C_k(s)$ has the same sign. Every summand is positive; for $k=0$, this is immediate from $C_0(s)=d!>0$.

Thus


$$
\boxed{(-1)^mC_m'(s)<0\qquad(s>0,\ m\ge1).}
\tag{5.5}
$$



Every kernel term $0\le k<m$ is retained.

### 5.3 The limit at $s=0$

The moments are the polynomials


$$
\int_0^\infty y^\ell\,d\sigma_s(y)
=
\sum_{j=0}^b\binom bj s^{b-j}(d+\ell+j)!.
$$


At $s=0$, the measure is $y^{b+d}e^{-y}\,dy$, whose relevant Gram matrices are positive definite. Hence the coefficients of the monic orthogonal polynomials, their lower-degree norms, and the functionals $C_m(s)$ are continuous at zero.

The same Laguerre calculation as in Section 4 gives the explicit endpoint value


$$
\boxed{
C_m(0)=(-1)^m d!(b)_m.
}
\tag{5.6}
$$


It is nonzero. Therefore


$$
(-1)^mC_m(s)>0
$$


on all $s\ge0$, and its magnitude is nonincreasing.

At the original $m=h$, $b=d+1$,


$$
|C_h(0)|=d!(d+1)_h=n!.
\tag{5.7}
$$



**Verdict:** the derivative identity, its sign, and the $s=0$ passage are valid. The proof pays the full exterior integral and needs no omitted high-degree kernel term.

---

## 6. Restricted-measure projection and the complete $F$-bound

Let $\pi_h^*$ be monic orthogonal for


$$
d\mu^*(x)
=
x^b(x-1)^de^{-x}\mathbf1_{(1,\infty)}(x)\,dx,
$$


and put


$$
d\nu(x)=(x-1)^de^{-x}\,dx.
$$



### 6.1 The projection identity, including its forcing term

Let $K^*_{h-1}$ be the reproducing kernel for degrees at most $h-1$ in $L^2(\mu^*)$. The polynomial $p_h-\pi_h^*$ has degree at most $h-1$. Its coefficient against a lower-degree orthogonal polynomial $\pi_k^*$ is


$$
\frac{\int_1^\infty p_h(x)\pi_k^*(x)\,d\mu(x)}
{\|\pi_k^*\|_{\mu^*}^2}
=
-\frac{\int_0^1p_h(y)\pi_k^*(y)\,d\mu(y)}
{\|\pi_k^*\|_{\mu^*}^2}.
$$


Thus


$$
\boxed{
p_h(x)
=
\pi_h^*(x)
-
\int_0^1p_h(y)K^*_{h-1}(x,y)\,d\mu(y).
}
\tag{6.1}
$$



The integral over $(0,1)$ is the exact projection forcing. It has not been suppressed by replacing the original measure with its restriction.

### 6.2 What is positive

Define


$$
L^*(y)=\int_1^\infty K^*_{h-1}(x,y)\,d\nu(x).
$$


Then


$$
L^*(y)
=
\sum_{k=0}^{h-1}
\frac{
\pi_k^*(y)
\int_1^\infty \pi_k^*(x)x^{-b}\,d\mu^*(x)}
{\|\pi_k^*\|_{\mu^*}^2}.
\tag{6.2}
$$


All zeros of $\pi_k^*$ exceed $1$, so for $0\le y\le1$, its value has sign $(-1)^k$. The accompanying integral has the same sign by (2.3). Hence


$$
\boxed{L^*(y)>0\qquad(0\le y\le1).}
\tag{6.3}
$$



This proves positivity of $L^*$. It does **not** prove, or require,


$$
K^*_{h-1}(x,y)\ge0
$$


for all $x>1$, $0\le y\le1$.

The actual $p_h$ has all zeros above $1$, by Section 3. Since $h$ is odd,


$$
p_h(y)<0\qquad(0\le y\le1).
$$


Integrating (6.1) against $\nu$ on $(1,\infty)$ therefore yields


$$
\int_1^\infty p_h\,d\nu
\ge
\int_1^\infty\pi_h^*\,d\nu.
\tag{6.4}
$$



### 6.3 Paying the entire restricted exterior integral

Under $x=1+y$,


$$
\pi_h^*(1+y)=\pi_{h,1}(y),
$$


because the factor $e^{-1}$ in the shifted measure does not change a monic orthogonal polynomial. Therefore


$$
\int_1^\infty\pi_h^*(x)\,d\nu(x)
=
e^{-1}C_h(1).
$$


It is negative, and Section 5 gives


$$
e^{-1}C_h(1)\ge-e^{-1}n!.
\tag{6.5}
$$



On the other interval, if the zeros of $p_h$ are $\rho_i>1$, then


$$
\frac{|p_h(y)|}{|p_h(0)|}
=
\prod_{i=1}^h\left(1-\frac y{\rho_i}\right)\le1
\qquad(0\le y\le1).
$$


Thus


$$
\left|\int_0^1p_h(y)\,d\nu(y)\right|
\le
|p_h(0)|\int_0^1(1-y)^d\,dy
=
\frac{|p_h(0)|}{b}.
\tag{6.6}
$$



Finally,


$$
\frac Fa=\int_0^\infty p_h\,d\nu<0.
$$


Combining (6.4)–(6.6),


$$
\frac Fa\ge-\frac{n!}{e}-\frac{|p_h(0)|}{b}.
$$


Since $|r_0|=a|p_h(0)|$,


$$
\boxed{
|F|\le\frac{an!}{e}+\frac{|r_0|}{b}.
}
\tag{6.7}
$$



A potentially invalid stronger inference has been avoided: (6.4) alone does not bound the absolute value of the actual exterior tail. The proof instead obtains a lower bound for the **complete** $F/a$ and then uses $F<0$.

**Verdict:** the full-tail comparison is correct, with the right projection sign and no omitted exterior contribution.

---

## 7. The evaluated ratio and the actual all-prime arithmetic transfer

### 7.1 The explicit $F/R$ bound

The $k=0$ term of $R$ is


$$
c_{n,0}|r_0|=\frac{|r_0|}{n+1/4}.
$$


Consequently,


$$
R\ge\frac{|r_0|}{n+1/4}.
\tag{7.1}
$$



Combining (6.7), (4.7), and (7.1),


$$
\frac{|F|}{R}
\le
\frac1{4e}\frac{(5/4)_d}{(3/4)_d}
+
\frac{n+1/4}{b}.
\tag{7.2}
$$



For every integer $j\ge0$,


$$
(4j+3)^2(2j+3)-(4j+5)^2(2j+1)=2.
$$


Hence


$$
\left(\frac{4j+5}{4j+3}\right)^2
<
\frac{2j+3}{2j+1}.
$$


Multiplying,


$$
\frac{(5/4)_d}{(3/4)_d}\le\sqrt{2d+1}.
$$


Since $d=b-1$ and $n=2001b$,


$$
\boxed{
\frac{|F|}{R}
\le
B_b=
\frac{\sqrt{2b-1}}{4e}+2001+\frac1{4b}.
}
\tag{7.3}
$$



For every original $b\ge10^9$,


$$
\frac{\sqrt{2b-1}}{4e}<\frac{\sqrt b}{2},
$$


and


$$
2001+\frac1{4b}<2002<\frac{\sqrt b}{2},
$$


the last inequality following from


$$
4004^2=16032016<10^9.
$$


Thus


$$
\boxed{|F|<\sqrt b\,R.}
\tag{7.4}
$$



### 7.2 Checking the denominator restriction in the actual objects

The previously audited finite Laguerre coefficient identity is


$$
(-1)^kk!r_k
=
\sum_{j=0}^d
\binom{n+1}{n-j-k}\gamma_j.
\tag{7.5}
$$


The complete triangular recurrence gives


$$
h!\mid\gamma_j,
$$


because every forcing factorial $(n-j)!$ is divisible by $h!$. Thus


$$
h!\mid k!r_k\quad(0\le k\le n),
\qquad
h!\mid F.
\tag{7.6}
$$


The stronger exact content theorem $\gcd(\gamma_0,\ldots,\gamma_d)=h!$ remains valid background; only its divisibility part is needed here.

Fix a prime $\varpi\mid h$. For $k<h$,


$$
v_\varpi(k!)<v_\varpi(h!),
$$


so (7.6) gives $\varpi\mid r_k$. Therefore


$$
x^h\mid\bar r(x)
$$


over $\mathbb F_\varpi$. Also $(x-1)^d\mid\bar r(x)$.

Because $r$ is the actual primitive polynomial, $\bar r\ne0$. The two factors are coprime and have total degree $h+d=n$. Hence


$$
\boxed{
r(x)\equiv a\,x^h(x-1)^d\pmod\varpi,
\qquad \varpi\nmid a.
}
\tag{7.7}
$$



Write


$$
r(1+z)=z^dS(z),\qquad S(z)=\sum_{j=0}^hs_jz^j\in\mathbb Z[z].
$$


The complete exponential endpoint is


$$
E=\sum_{j=0}^h(d+j)!s_j,
$$


so


$$
\frac E{d!}=\sum_{j=0}^h(d+1)_j s_j.
\tag{7.8}
$$


By (7.7),


$$
S(z)\equiv a(1+z)^h
=a(1+z^\varpi)^{h/\varpi}\pmod\varpi.
$$


Thus $s_0\equiv a$, and $s_j\equiv0$ for $1\le j<\varpi$. For $j\ge\varpi$, the product $(d+1)_j$ contains $\varpi$ consecutive integers and is divisible by $\varpi$. All nonconstant terms of (7.8) therefore vanish modulo $\varpi$:


$$
\boxed{
E/d!\equiv a\not\equiv0\pmod\varpi.
}
\tag{7.9}
$$



Now retain the entire arctangent correction. Let


$$
\Lambda_B=\operatorname{lcm}(1,3,\ldots,4d-1).
$$


Since $h!\mid w_j$,


$$
T\in\frac{4h!}{\Lambda_B}\mathbb Z.
\tag{7.10}
$$


This lcm is used only for a valuation bound; it does not replace the actual combined denominator $\ell=1$.

Put $L=v_\varpi(\Lambda_B)$. If $L=0$, the factor $h$ in $h!/d!$ gives


$$
v_\varpi(h!/d!)>0.
$$


If $L>0$, then $\varpi^L\le4d-1$. The first two multiples of $\varpi^L$ above $d$ are at most


$$
d+2\varpi^L\le9d-2<h.
$$


They contribute at least $2L>L$ to $v_\varpi(h!/d!)$. In either case,


$$
v_\varpi(h!)-v_\varpi(\Lambda_B)>v_\varpi(d!).
$$


Therefore


$$
v_\varpi(T)>v_\varpi(E)=v_\varpi(d!),
$$


and unequal valuations prevent cancellation:


$$
v_\varpi(E+T)=v_\varpi(d!).
$$


Using $h!\mid F$,


$$
\boxed{
v_\varpi(g)=v_\varpi(d!)\qquad(\varpi\mid h).
}
\tag{7.11}
$$



Consequently, for the actual $q=|F|/g$,


$$
\mathcal D_h
:=
\prod_{\varpi\mid h}
\varpi^{\,v_\varpi(h!)-v_\varpi(d!)}
\mid q.
\tag{7.12}
$$


The product $h!/d!$ contains $h$, so


$$
\boxed{h\mid\mathcal D_h\mid q.}
\tag{7.13}
$$



This derivation retains the actual primitive content, the full exponential endpoint, and the complete $T$.

### 7.3 Why the resulting inequality includes every prime of $g$

No exact valuation assertion has been made at primes not dividing $h$. Nevertheless,


$$
g=\frac{|F|}{q}
$$


is an exact identity involving the final all-prime gcd. Hence


$$
\boxed{
\frac gR
=
\frac{|F|}{qR}
\le
\frac{B_b}{\mathcal D_h}
\le
\frac{B_b}{h}
<
\frac1{2000\sqrt b}.
}
\tag{7.14}
$$


This is not a substitution of an $h$-supported gcd for the final gcd.

The paid determinant reduction is consistent with precisely this primitive pair. If


$$
\lambda_n=\frac{P_n\tau_n}{aK_n},
$$


then $\lambda_n<0$, and


$$
D_n(X)=-\lambda_ng(qX-p).
$$


Because $q,p$ are coprime and $D_n\in\mathbb Z[X]$, the positive multiplier $-\lambda_ng$ is the determinant’s actual content. Therefore


$$
G_n=-\lambda_ng=U_n\frac g{|F|},
$$


as retained in (1.5).

### 7.4 Whole-error conclusion

Using the complete lower bound (1.8),


$$
q(e+\pi)-p
>
\frac{R}{2g}
\ge
\frac{\mathcal D_h}{2B_b}
\ge
\frac h{2B_b}
>
\frac h{2\sqrt b}.
$$


Since $h=2000b+1$,


$$
\boxed{
q(e+\pi)-p>1000\sqrt b.
}
\tag{7.15}
$$



Thus the original family cannot provide a nonzero primitive-error sequence tending to zero.

### 7.5 An additional quantitative corollary

The same proof gives the unscaled lower bound


$$
e+\pi-\frac pq>\frac1{2B_b}.
\tag{7.16}
$$


Also,


$$
\frac{B_b}{\sqrt b}\longrightarrow\frac{\sqrt2}{4e},
\qquad
\frac hb\longrightarrow2000.
$$


Therefore, along any unbounded admissible original collection,


$$
\boxed{
\liminf
\frac{q(e+\pi)-p}{\sqrt b}
\ge2000\sqrt2\,e.
}
\tag{7.17}
$$


This is an additional proved asymptotic consequence; it is not needed for the uniform constant $1000$, and no optimality is asserted.

---

## 8. Audit of every term in the signed-tail margin

The proof in this section concerns the original normalized $R$-functional. It does not replace it by a different positive measure.

### 8.1 Exact normalization

Write


$$
P(x)=\frac{p_h(x)}{p_h(0)}
=\prod_{i=1}^h\left(1-\frac{x}{\rho_i}\right),
$$


and define


$$
H_j=h_j(\rho_1^{-1},\ldots,\rho_h^{-1}),
\qquad
A_d(x)=\sum_{j=0}^dH_jx^j.
$$


Put


$$
K_d(x)=
\sum_{k=0}^d
\frac{(-1)^k\binom nk}{(1/4)_{k+1}}x^k,
\qquad
Q_d=[K_dA_d]_{\le d}.
\tag{8.1}
$$



First check the short functional normalization. The established Laguerre identity gives


$$
W(y)
=
\sum_{k=0}^d
\frac{(-1)^k}{k!}\binom nk(1-y)^k
\int_0^\infty e^{-x}x^kr(x)\,dx.
$$


The terms $d+1\le k\le n$ vanish by the original orthogonality; they are not discarded merely because they are inconvenient.

Since


$$
\int_0^1y^{-3/4}(1-y)^k\,dy
=
\frac{k!}{(1/4)_{k+1}},
$$


equation (1.3) gives


$$
\boxed{
R=-\int_0^\infty e^{-x}r(x)K_d(x)\,dx.
}
\tag{8.2}
$$



Now apply (2.2) to the nodes $\rho_1,\ldots,\rho_h,x$. Since $b=d+1$,


$$
(x^{-b})[\rho_1,\ldots,\rho_h,x]
=
\frac{(-1)^h x^{-b}}{\prod_i\rho_i}A_d(x).
\tag{8.3}
$$


For $x^{-b}K_d(x)$, every reciprocal exponent $b-k$ is at least $1$, and the same calculation gives


$$
(x^{-b}K_d(x))[\rho_1,\ldots,\rho_h,x]
=
\frac{(-1)^h x^{-b}}{\prod_i\rho_i}Q_d(x).
\tag{8.4}
$$


Indeed, the coefficient of $x^k$ from $K_d$ is paired with the truncation $A_{d-k}$, which is exactly the convolution defining $Q_d$.

Using orthogonality, $h$ odd, and


$$
|r_0|=a\prod_i\rho_i,
$$


equations (8.2)–(8.4) yield


$$
\boxed{
\frac{|F|}{|r_0|}
=
\int_0^\infty
P(x)^2(x-1)^de^{-x}A_d(x)\,dx,
}
\tag{8.5}
$$




$$
\boxed{
\frac R{|r_0|}
=
\int_0^\infty
P(x)^2(x-1)^de^{-x}Q_d(x)\,dx.
}
\tag{8.6}
$$



The polynomial $Q_d$ remains signed. No pointwise positivity has been inserted into (8.6).

### 8.2 The small interval is controlled without assigning it a sign

For $0\le x\le4/n$, one has $x<1<\rho_i$. Thus


$$
\frac1{P(x)}=\sum_{j\ge0}H_jx^j,
\qquad
A_d(x)\le\frac1{P(x)}.
$$


Hence


$$
P(x)^2A_d(x)\le P(x)\le1.
\tag{8.7}
$$



Also,


$$
Q_d(x)
=
\sum_{k=0}^d
\frac{(-1)^k\binom nk}{(1/4)_{k+1}}
x^kA_{d-k}(x).
$$


Since $A_{d-k}(x)\le A_d(x)$,


$$
\frac{|Q_d(x)|}{A_d(x)}
\le
4\sum_{k=0}^d
\frac{\binom nkx^k}{(5/4)_k}
\le
4\sum_{k=0}^\infty
\frac{4^k}{k!(5/4)_k}.
$$


A numerical series computation is unnecessary: $(5/4)_k\ge1$, so


$$
4\sum_{k=0}^\infty
\frac{4^k}{k!(5/4)_k}
\le4e^4<324.
$$


Together with (8.7) and $(1-x)^de^{-x}\le1$,


$$
\boxed{
\left|
\int_0^{4/n}
P(x)^2(x-1)^de^{-x}Q_d(x)\,dx
\right|
\le\frac{1296}{n}.
}
\tag{8.8}
$$



### 8.3 A sufficient explicit lower bound for the total charge

The normalized coefficient polynomial is


$$
\sum_{k=0}^n\frac{|r_k|}{|r_0|}z^k
=
(1+z)^dP(-z).
$$


All coefficients on the right are nonnegative, and its coefficient of $z^d$ is at least $1$. Hence


$$
\frac R{|r_0|}\ge c_{n,d}.
\tag{8.9}
$$


Now


$$
c_{n,d}
\ge
\frac{d!(3/4)_d}{(n+1/4)^{d+1}}.
$$


The elementary inequalities


$$
(3/4)_d\ge(3/4)^dd!,
\qquad
d!\ge(d/e)^d>(d/3)^d
$$


give


$$
c_{n,d}
\ge
\frac1{n+1/4}
\left(\frac{d^2}{12(n+1/4)}\right)^d.
\tag{8.10}
$$



At every original index,


$$
d\ge\frac b2,\qquad n+\frac14<2002b,
$$


so


$$
\frac{d^2}{12(n+1/4)}
>
\frac b{96096}>2.
$$


Also $d\ge13$. Therefore


$$
c_{n,d}>\frac{2^{13}}{n+1/4}>\frac{5184}{n}.
$$


The last comparison follows from


$$
(8192-5184)n=3008n>1296.
$$


Thus


$$
\boxed{
\frac R{|r_0|}>\frac{5184}{n}.
}
\tag{8.11}
$$



### 8.4 Complete endpoint evaluation and the claimed margin

Define


$$
Z_\beta(x)
=
P(x)^2(x-1)^dQ_d(x)
=
\sum_{j=0}^{2n}z_jx^j,
$$


where zero coefficients are included if the degree is smaller than $2n$, and


$$
\mathcal T_\beta(t)
=
\sum_{j=0}^{2n}z_jj!\sum_{s=0}^j\frac{t^s}{s!}.
$$


Repeated integration by parts, with all infinity terms vanishing, gives


$$
\boxed{
\int_t^\infty e^{-x}Z_\beta(x)\,dx
=
e^{-t}\mathcal T_\beta(t).
}
\tag{8.12}
$$


This includes every endpoint term for every monomial through degree $2n$.

Let


$$
J=\int_{4/n}^\infty e^{-x}Z_\beta(x)\,dx.
$$


From (8.6) and (8.8),


$$
J\ge\frac R{|r_0|}-\frac{1296}{n}.
\tag{8.13}
$$


Meanwhile, (7.4) gives


$$
\frac{|F|}{h|r_0|}
<
\frac{\sqrt b}{h}\frac R{|r_0|}
<
\frac12\frac R{|r_0|}.
$$


Using (8.11) in (8.13),


$$
J
>
\frac{|F|}{h|r_0|}
+\frac12\frac R{|r_0|}
-\frac{1296}{n}
>
\frac{|F|}{h|r_0|}+\frac{1296}{n}.
$$


Therefore


$$
\boxed{
e^{-4/n}\mathcal T_\beta(4/n)
>
\frac{1296}{n}
+
\frac{|F|}{h|r_0|}.
}
\tag{8.14}
$$



**Verdict:** the full signed-tail margin is proved with $C=1$. The displayed finite factorial sum is not merely named: its complete value is bounded below by the explicit right side of (8.14).

---

## 9. Boundary audit and claim-by-claim decisions

### 9.1 No physical or moment boundary has moved

| Object or operation | Exact retained boundary |
|---|---|
| Original matrix | Rows $n,\ldots,n+d$, columns $0,\ldots,d$ |
| Physical terminal | $n+d$ |
| Modified moments constructing $p_h$ | $\mu_0,\ldots,\mu_{2h-1}$ |
| Largest factorial in those moments | $(b+d+2h-1)!=(2n)!$ |
| Gaussian quadrature | $N=h+d/2$, exact through $2N-1=d+2h-1$ |
| Largest base factorial for quadrature | $(b+2N-1)!=(2n)!$ |
| Kernels used in the derivative and projection | Degrees $0,\ldots,h-1$ |
| Largest factorial in their norms | At most $(2n-1)!$ |
| Shifted/restricted orthogonality construction | At most $(2n)!$ |
| Complete tail polynomial | Degree at most $2n$ |

The new proof does not require the norm of a degree-$h$ polynomial against the full modified weight as an additional moment input. The reciprocal divided-difference cancellations in the relevant integrals keep their polynomial factorial boundary at $2n$.

The quadrature, shifted measures, and restricted measures are analytic representations or comparisons of the existing objects. They do not add a physical row, contact, return, or terminal condition.

### 9.2 Independent decision ledger

| Claim under review | Independent verdict |
|---|---|
| Original domain and finite matrix | Retained exactly |
| Complete $B_j$, triangular forcing, $W$, and $T$ | Retained exactly |
| Actual contents, clearers, $a$, and paid determinant bridge | Established background; unchanged |
| Reciprocal divided-difference sign lemma | Accepted with the stated integrability and positivity hypotheses |
| Fixed-node Gaussian contact representation | Accepted; exact through the required degree |
| Zero-motion formula | Accepted; independently derived |
| Zero monotonicity | Accepted; strict on the original domain |
| Absolute-coefficient monotonicity | Accepted, using the same original $a$ |
| Comparison factorial functional | Accepted: $(-1)^hn!$ |
| Complete Pfaff–Saalschutz beta charge | Accepted: $4n!(3/4)_d/(5/4)_d$ |
| Exterior Christoffel derivative identity | Accepted, with the full kernel sum |
| Sign of its derivative | Accepted |
| $s=0$ limit | Accepted; nonsingular moment matrices and explicit endpoint value |
| Restricted-measure projection | Accepted, including its full forcing integral |
| “Kernel positivity” | Accepted only for $L^*(y)$, exactly as needed |
| Complete bound for $F$ | Accepted; the use of $F<0$ is essential |
| Evaluated $F/R$ estimate | Accepted at every original index |
| Actual $h\mid q$ restriction | Accepted; checked in the primitive original objects |
| Transfer to the all-prime $g/R$ | Accepted; no restricted-prime gcd substitution |
| Complete primitive-error lower bound | Accepted |
| Signed-tail identities and margin | Accepted, with all terms retained |
| Retirement of the displayed Laguerre family | Proved |
| Retirement of the compact matrix or older prime-$29$ producer | Not implied |
| Rationality or irrationality of $e+\pi$ | Unresolved |

No failed equality or inequality was found in A2 Turn 18 at its stated scope. The potentially dangerous stronger readings—continuous-support zero monotonicity, pointwise reproducing-kernel positivity, or an absolute bound for the actual exterior tail—are not needed and should not be substituted for the proved statements.

---

## 10. Research status, remaining bottleneck, and bounded arithmetic

### 10.1 What is now closed

The outstanding Laguerre comparison obligation is closed:


$$
|F|\le ChR
$$


not only holds with a fixed $C$, but is superseded by


$$
|F|<\sqrt b\,R,\qquad h=2000b+1.
$$


Combined with the actual denominator restriction, this proves


$$
\frac Rg>2000\sqrt b
$$


and hence the whole-error obstruction.

Thus the formerly open possibility


$$
R/g\longrightarrow0
$$


on a surviving original Laguerre subsequence is now excluded.

An exact prime-by-prime evaluation of $g$ outside the primes dividing $h$ is **not** supplied. It is also no longer necessary for this family’s retirement: the proved global inequality already controls the actual final gcd sufficiently.

The additional statement (7.17),


$$
\liminf
\frac{q(e+\pi)-p}{\sqrt b}
\ge2000\sqrt2\,e,
$$


is a further quantitative consequence of the audited proof.

### 10.2 What remains genuinely open

The global objective is unchanged. This family’s failure does not decide whether $e+\pi$ is rational or irrational.

The unresolved tasks identified in the coordinator’s ledger remain separate:

- the actual original-domain projection for the distinct producer, retaining its corrected forcing, returns, terminal, and paid relative-cofactor data;
- the final all-prime content of the compact mixed pencil;
- the paid adjacent resultant, retaining both actual neighboring final gcds.

No compact sign theorem or earlier comparison has been repeated here, and no new producer is proposed.

A precise existing follow-on arithmetic target is available for the unretired compact family. With its already defined actual coefficients and final gcd,


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
\qquad
q_k=\frac{|H_{1,k}|}{G_k},
$$


the coordinator’s separately established rational-error bound is


$$
0<e+\pi-\frac{p_k}{q_k}
\le\frac{336}{11^{k-1}}
\qquad(k\ge64).
$$


Therefore the following remains a sufficient, **unproved** arithmetic lemma:

> On an explicitly admissible infinite subset of the original compact indices, prove
> 

$$
> \frac{|H_{1,k}|}{G_k}=o(11^{k-1}).
>
$$



If proved for the same primitive pairs and indices, it would give


$$
0<q_k(e+\pi)-p_k
\le336\,\frac{q_k}{11^{k-1}}\longrightarrow0,
$$


and hence irrationality. This is a conditional implication, not a result established by the present audit. Neither a finite content computation nor the known raw factorial divisors prove this lemma.

### 10.3 Bounded exact arithmetic

**No new finite computation is needed for the obstruction proved here.** In particular, there is no reason to repeat the closed $n=13,b=3$ calculation, the small-prime modular table, or an expensive matrix/content computation.

If a transcription receipt is desired, it can be restricted to the following bounded inputs:

1. The two cubic products
   

$$
(4X+3)^2(2X+3),\qquad
   (4X+5)^2(2X+1).
$$


2. The integers $4004,96096,8192,5184,10^9$.

Expected verifiable outputs are


$$
(4X+3)^2(2X+3)-(4X+5)^2(2X+1)=2,
$$




$$
4004^2=16032016<10^9,
$$




$$
2\cdot96096=192192<10^9,
$$




$$
8192-5184=3008>1296.
$$



These are finite transcription checks only. No execution is claimed, and no infinite conclusion is inferred from their finite scope.

---

## Final conclusion

The independent audit accepts the complete A2 Turn 18 obstruction, including:

- the exact fixed-node contact deformation;
- the zero-motion formula and coefficient comparison;
- the fully evaluated terminating beta charge;
- the exterior Christoffel derivative and its $s=0$ limit;
- the restricted-measure projection with its full forcing;
- the complete signed-tail estimate;
- and the transfer through the **actual primitive denominator and all-prime final gcd**.

The resulting theorem is


$$
\boxed{
q(e+\pi)-p>1000\sqrt b
\quad\text{at every original admissible Laguerre index}.
}
$$



Accordingly, this distinct Laguerre family is rigorously retired as a source of vanishing primitive whole errors. The compact family and the older prime-$29$ producer remain unretired and retain their unresolved arithmetic obligations.

**The rationality or irrationality of $e+\pi$ remains open.**
