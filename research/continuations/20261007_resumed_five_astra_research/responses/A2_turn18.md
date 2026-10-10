> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 Turn 18: an evaluated all-prime obstruction on the entire original domain

## Abstract

The rationality or irrationality of $e+\pi$ remains unresolved. This report proves a new obstruction for the specific original matrix family, including its surviving progression.

The principal new estimate is


$$
\boxed{
\frac{|F|}{R}
\le
\frac{1}{4e}\frac{(5/4)_d}{(3/4)_d}
+2001+\frac1{4b}
\le
\frac{\sqrt{2b-1}}{4e}+2001+\frac1{4b}.
}
\tag{A}
$$


It holds for the actual primitive polynomial and unchanged charges at every original index


$$
n=2001b,\qquad d=b-1,\qquad h=2000b+1.
$$



Since every original index has $b\ge10^9$, this gives


$$
\boxed{|F|<\sqrt b\,R.}
\tag{B}
$$


Combining it with the established restriction $h\mid q$, for the actual primitive denominator $q=|F|/g$, yields the all-prime bound


$$
\boxed{
\frac gR<\frac{\sqrt b}{h}<\frac1{2000\sqrt b}.
}
\tag{C}
$$


Consequently the complete primitive error satisfies


$$
\boxed{
q(e+\pi)-p>1000\sqrt b.
}
\tag{D}
$$


Thus it diverges along every unbounded collection of admissible original indices. In particular, the surviving progression does not supply a vanishing primitive-error subsequence.

The proof does **not** retry pointwise positivity of the reciprocal kernel. Instead, it combines:

1. monotonicity of the zeros under an auxiliary contact deformation;
2. an exactly evaluated Laguerre comparison charge;
3. a projection comparison with orthogonality restricted to $x>1$;
4. a monotonicity theorem for an exterior Christoffel modification.

These arguments control the entire polynomial and its $x>1$ contribution.

The proposed tail margin (9.4) from Turn 17 is also proved, with the fixed choice $C=1$. All new comparisons are analytic normalizations of the existing objects; none changes the primitive integer form, its clearers, or its final gcd.

---

## 1. Original objects, boundaries, and retained arithmetic payments

### 1.1 Domain

Throughout,


$$
b=3^{249005515+574312172u},\qquad
n=2001b,\qquad d=b-1,\qquad h=n-d=2000b+1,
$$


with


$$
u\equiv2\pmod{29^9}
$$


and every other original admissibility condition retained.

In particular, $d$ is even and $h,n$ are odd. The results below apply pointwise throughout this domain, hence also on


$$
u=2+29^9(1+6068205v),\qquad v\ge0,
$$


whenever the original admissibility conditions hold.

No assertion about an unspecified additional admissibility condition is needed: every inequality is proved separately at each admissible index.

### 1.2 The finite matrix and its complete columns

The matrix remains


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


Its physical row window is exactly $n,\ldots,n+d$, with physical terminal $n+d$; its columns are exactly $0,\ldots,d$. Every rational summand of every $B_j$ is retained.

Write


$$
\mathsf A_{rj}=A_{n+r,j}+B_j,\qquad
\mathsf W_{rj}=(n+r)!\mathsf A_{rj}.
$$


The actual contents and clearers remain


$$
\kappa_r=\gcd\bigl((n+r)!,\mathsf W_{r0},\ldots,\mathsf W_{rd}\bigr),
\qquad C_r=\frac{(n+r)!}{\kappa_r},
$$




$$
Y_{rj}=C_r\mathsf A_{rj},\qquad
c_j=\gcd_{0\le r\le d}(C_r,Y_{rj}),
$$




$$
\mathcal L_n=\operatorname{lcm}_{0\le r\le d}C_r,\qquad
P_n=\frac{\prod_{r=0}^dC_r}{\prod_{j=0}^dc_j}.
$$


Thus


$$
D_n(X)=
\det\left[\frac{C_rX-Y_{rj}}{c_j}\right]_{r,j=0}^d
=P_n\det H(X)=U_nX-V_n.
$$


The established paid reduction is


$$
D_n(X)=\frac{P_n\tau_n}{aK_n}(FX-E-T),
\qquad
K_n=
\frac{\prod_{r=0}^d(n+r)!}
{\prod_{j=0}^d j!(n-j)!}.
\tag{1.1}
$$


Here $\tau_n$ is the unchanged cofactor normalization. In the supplied notation,


$$
\tau_n=
\frac{(-1)^n}{n!}
\frac{\prod_{s=0}^{d-1}s!}{\prod_{j=h}^{n-1}j!}
\frac{\Delta_h}{\Delta_h^{(0)}},
\qquad
\Delta_h^{(0)}=\prod_{i=0}^{h-1}i!(i+b)!.
$$



None of these divisions is removed below.

The separate earlier producer, with its own corrected forcing, returns, and physical terminal, is not identified with this matrix. Its formulas are absent from the packet. No conclusion below transfers an arithmetic gain to that separate producer.

### 1.3 The actual primitive scalar objects

Let $p_h$ be the monic degree-$h$ orthogonal polynomial for


$$
d\mu(x)=x^b(x-1)^d e^{-x}\,dx,\qquad x>0.
$$


Let $a>0$ be its actual least coefficient clearer, so that


$$
r(x)=a(x-1)^dp_h(x)=\sum_{k=0}^nr_kx^k
$$


is the actual primitive integer polynomial.

Retain


$$
F=\sum_{k=0}^nr_kk!,
\qquad
E=\sum_{k=0}^nr_k\sum_{v=0}^k\frac{k!}{v!},
$$




$$
\gamma_j=(-1)^{n-j}(n-j)!r_{n-j}
-\sum_{i<j}\binom{n+1}{j-i}\gamma_i,
$$




$$
w_j=\binom nj\gamma_j,\qquad
W(y)=\sum_{j=0}^dw_jy^j,\qquad
T=\sum_{j=0}^dw_jB_j.
$$


The established original-domain clearing result is


$$
\ell=1,\qquad T\in\mathbb Z.
$$



The unchanged positive integer charge is


$$
R=\sum_{k=0}^n|r_k|c_{n,k},
\qquad
c_{n,k}=
\frac{k!(3/4)_k}{(n-k+1/4)_{k+1}},
\tag{1.2}
$$


with


$$
R=-4\sum_{j=0}^d\frac{w_j}{4j+1}\in\mathbb Z_{>0}.
$$



The actual all-prime reduction is


$$
g=\gcd(|F|,|E+T|),\qquad
q=-\frac Fg>0,\qquad
p=-\frac{E+T}{g}.
\tag{1.3}
$$


The determinant’s final gcd remains


$$
G_n=\gcd(U_n,|V_n|)=U_n\frac g{|F|}.
\tag{1.4}
$$



I reuse the accepted results


$$
\mathcal D_h\mid q,\qquad h\mid q,
\qquad
\mathcal D_h=
\prod_{\mathfrak p\mid h}
\mathfrak p^{v_{\mathfrak p}(h!)-v_{\mathfrak p}(d!)}.
\tag{1.5}
$$


Their arithmetic proofs were independently audited in the supplied A4 excerpt.

Finally, the complete error is unchanged:


$$
M=F(e+\pi)-E-T
=e\int_0^1e^{-x}r(x)\,dx
+4\int_0^1\frac{W(s^4)}{1+s^2}\,ds<0,
$$


and the established whole-error bounds are


$$
\boxed{
\frac{R}{2g}<q(e+\pi)-p<6005\frac Rg.
}
\tag{1.6}
$$


Neither channel nor any endpoint term is discarded.

---

## 2. A sign lemma for orthogonal-polynomial integrals

The following elementary fact will be used repeatedly.

### Lemma 2.1

Let $\sigma$ be a positive measure with sufficiently many moments, and let $\pi_m$ be its monic orthogonal polynomial of degree $m$, with zeros $\xi_1,\ldots,\xi_m$. Suppose $f$ is integrable in the expressions below and


$$
(-1)^m f[\xi_1,\ldots,\xi_m,x]>0
$$


on the support, apart from a set of measure zero. Then


$$
(-1)^m\int \pi_m(x)f(x)\,d\sigma(x)>0.
\tag{2.1}
$$



In particular this applies to


$$
f(x)=(x+s)^{-j},\qquad j\ge1,
$$


when the support lies to the right of $-s$.

#### Proof

Let $I_{m-1}f$ interpolate $f$ at the zeros of $\pi_m$. The interpolation remainder is


$$
f(x)-I_{m-1}f(x)
=\pi_m(x)f[\xi_1,\ldots,\xi_m,x].
$$


Orthogonality therefore gives


$$
\int\pi_m f\,d\sigma
=
\int\pi_m^2
f[\xi_1,\ldots,\xi_m,x]\,d\sigma.
$$


This proves the assertion.

For reciprocal powers, the divided difference has the required sign. Explicitly, for positive $t_0,\ldots,t_m$,


$$
(-1)^m(t^{-j})[t_0,\ldots,t_m]
=
\left(\prod_{i=0}^m t_i^{-1}\right)
h_{j-1}(t_0^{-1},\ldots,t_m^{-1})>0.
$$


Translation by $s$ gives the stated case. ∎

This lemma is a sign statement about an integrated orthogonal-polynomial functional. It does not assert positivity of the signed reciprocal comparison kernel from Turn 17.

---

## 3. A contact deformation makes the beta charge larger

Introduce an auxiliary real parameter $0\le t\le1$. Let $p_{h,t}$ be the monic degree-$h$ orthogonal polynomial for


$$
x^b(x-t)^d e^{-x}\,dx,\qquad x>0,
$$


and define the auxiliary monic polynomial


$$
r^{[t]}(x)=(x-t)^dp_{h,t}(x).
$$


Thus


$$
r=a\,r^{[1]}.
$$


These are analytic comparison objects only. They do not replace the primitive integer polynomial or its clearer.

### Lemma 3.1 — Monotonicity of the deformed zeros

Each ordered zero of $p_{h,t}$ is nondecreasing as $t$ runs from $0$ to $1$.

#### Proof

Use the established Gaussian quadrature for the base measure $x^be^{-x}\,dx$, with


$$
N=h+\frac d2.
$$


It is exact through degree $2N-1$. Its nodes $\lambda_i$ satisfy the established bound


$$
\lambda_i\ge L_b:=\frac{b^2}{8004b+2}>1.
\tag{3.1}
$$


The orthogonality equations for $p_{h,t}$ require degrees at most


$$
d+2h-1=2N-1.
$$


Consequently they are exactly the orthogonality equations for the finite positive measure


$$
\sum_{i=1}^N\omega_i(\lambda_i-t)^d\delta_{\lambda_i}.
\tag{3.2}
$$


All these weights are positive for $0\le t\le1$. In particular, all zeros of $p_{h,t}$ lie above $1$.

For completeness, the zero-monotonicity calculation is as follows. Let $\xi(t)$ be one zero and put


$$
\ell(x)=\frac{p_{h,t}(x)}{x-\xi(t)}.
$$


For the discrete measure in (3.2), its logarithmic weight derivative is


$$
s_t(x)=-\frac d{x-t}.
$$


Differentiating orthogonality gives


$$
\xi'(t)=
\frac{\int (x-\xi)\ell(x)^2s_t(x)\,d\sigma_t(x)}
{\int \ell(x)^2\,d\sigma_t(x)}.
\tag{3.3}
$$


One way to verify this formula is to subtract from $\partial_t p_{h,t}$ its interpolation value at $\xi$; the remaining polynomial is divisible by $x-\xi$, and its contribution vanishes by orthogonality.

Also


$$
\int(x-\xi)\ell(x)^2\,d\sigma_t(x)=0.
$$


Thus the numerator in (3.3) equals


$$
\int (x-\xi)\ell(x)^2
\bigl(s_t(x)-s_t(\xi)\bigr)\,d\sigma_t(x).
$$


Since $s_t$ is increasing on $x>t$, every integrand is nonnegative. Hence $\xi'(t)\ge0$. ∎

### Corollary 3.2 — Coefficientwise beta-charge comparison

Define


$$
R^{[0]}=\sum_{k=0}^n
\left|[x^k]r^{[0]}(x)\right|c_{n,k}.
$$


Then


$$
\boxed{R\ge aR^{[0]}.}
\tag{3.4}
$$



#### Proof

The zeros of $r^{[t]}$ consist of $d$ copies of $t$ and the $h$ zeros of $p_{h,t}$. All are nonnegative and each is nondecreasing with $t$.

The absolute coefficients of a monic polynomial with nonnegative zeros are the elementary symmetric functions of those zeros. They are nondecreasing in every zero. Therefore


$$
\left|[x^k]r^{[1]}(x)\right|
\ge
\left|[x^k]r^{[0]}(x)\right|
$$


for every $k$. All $c_{n,k}$ are positive, proving (3.4). ∎

This is a comparison of finite coefficient charges, not a pointwise comparison between the parent’s double-beta measure and the Turn 17 measure.

---

## 4. Exact evaluation of the comparison charge

At $t=0$, the orthogonality measure is


$$
x^{b+d}e^{-x}\,dx=x^{2d+1}e^{-x}\,dx.
$$


Write


$$
\alpha=2d+1.
$$


Then


$$
p_{h,0}(x)=(-1)^hh!L_h^{(\alpha)}(x),
\qquad
r^{[0]}(x)=x^dp_{h,0}(x).
$$



### Proposition 4.1

For $b=d+1$ and $n=h+d$,


$$
\boxed{
\int_0^\infty e^{-x}r^{[0]}(x)\,dx=(-1)^hn!,
}
\tag{4.1}
$$


and


$$
\boxed{
R^{[0]}=
4n!\frac{(3/4)_d}{(5/4)_d}.
}
\tag{4.2}
$$



#### Evaluation of the factorial functional

The finite Laguerre expansion, followed by the terminating Vandermonde identity, gives


$$
\int_0^\infty x^de^{-x}L_h^{(\alpha)}(x)\,dx
=
\frac{d!}{h!}(\alpha-d)_h.
$$


Here $\alpha-d=d+1=b$, so


$$
\int e^{-x}r^{[0]}(x)\,dx
=(-1)^hd!(b)_h.
$$


Since


$$
d!(b)_h=d!(d+1)_h=(d+h)!=n!,
$$


equation (4.1) follows.

#### Evaluation of the beta charge

The coefficient expansion is


$$
\left|[x^{d+j}]r^{[0]}(x)\right|
=
h!\binom{h+2d+1}{h-j}\frac1{j!},
\qquad 0\le j\le h.
$$


Put $l=h-j$. Direct substitution in the exact weights (1.2) gives


$$
R^{[0]}
=
\frac{n!(3/4)_n\Gamma(1/4)}{\Gamma(n+5/4)}
\sum_{l=0}^h
\frac{(-h)_l(-h-2d-1)_l(1/4)_l}
{(-n)_l(1/4-n)_l\,l!}.
\tag{4.3}
$$



The finite sum is balanced. Its exact evaluation is


$$
\sum_{l=0}^h
\frac{(-h)_l(-h-2d-1)_l(1/4)_l}
{(-n)_l(1/4-n)_l\,l!}
=
\frac{(d+1)_h(-n-1/4)_h}
{(-n)_h(d+3/4)_h}.
\tag{4.4}
$$



Here is a derivation sufficient to check that evaluation rather than treating it as an unevaluated special-function invocation. The terminating identity


$$
\sum_{k=0}^m
\frac{(-m)_k(A)_k(B)_k}
{k!(C)_k(1+A+B-C-m)_k}
=
\frac{(C-A)_m(C-B)_m}
{(C)_m(C-A-B)_m}
\tag{4.5}
$$


follows by integrating the polynomial transformation


$$
{}_2F_1(-m,A;C;t)
=
\frac{(C-A)_m}{(C)_m}
{}_2F_1(-m,A;1+A-C-m;1-t)
$$


against the normalized beta density with parameters


$$
B,\quad 1+A-C-m.
$$


Termwise integration cancels the second denominator on the transformed side, leaving the terminating Vandermonde evaluation. This first proves (4.5) where the beta parameters are positive; clearing denominators extends it as a rational identity to every nonsingular parameter choice.

Taking


$$
m=h,\quad A=-h-2d-1,\quad B=\frac14,\quad C=-n
$$


gives (4.4). None of its denominators vanishes in the finite range $0\le l\le h$.

Finally,


$$
\frac{(3/4)_n}{(d+3/4)_h}=(3/4)_d
$$


and


$$
\frac{(-n-1/4)_h}{(-n)_h}
=
\frac{\Gamma(n+5/4)}{\Gamma(d+5/4)}
\frac{d!}{n!}.
$$


Substituting into (4.3), and using $d!(d+1)_h=n!$, yields


$$
R^{[0]}
=
n!(3/4)_d\frac{\Gamma(1/4)}{\Gamma(d+5/4)}
=
4n!\frac{(3/4)_d}{(5/4)_d}.
$$


This proves (4.2). ∎

Thus Corollary 3.2 has the fully evaluated form


$$
\boxed{
R\ge4a n!\frac{(3/4)_d}{(5/4)_d}.
}
\tag{4.6}
$$



---

## 5. Exterior Christoffel monotonicity

The next lemma controls the complete contribution from $x>1$.

### Lemma 5.1

Fix integers $b\ge1,d\ge0$. For $s\ge0$, let $\pi_{m,s}$ be the monic orthogonal polynomial for


$$
d\sigma_s(y)=(y+s)^b y^d e^{-y}\,dy,\qquad y>0.
$$


Define


$$
C_m(s)=\int_0^\infty \pi_{m,s}(y)y^de^{-y}\,dy.
$$


For $m\ge1$, the quantity $(-1)^mC_m(s)$ is positive and nonincreasing in $s$.

#### Proof

For $s>0$,


$$
C_m(s)=\int \pi_{m,s}(y)(y+s)^{-b}\,d\sigma_s(y).
$$


Lemma 2.1 gives


$$
(-1)^mC_m(s)>0.
\tag{5.1}
$$



Let


$$
J_m(s)=\int\frac{\pi_{m,s}(y)}{y+s}\,d\sigma_s(y),
$$


so that


$$
(-1)^mJ_m(s)>0.
\tag{5.2}
$$


Let $K_{m-1,s}$ be the reproducing kernel for polynomials of degree at most $m-1$ in $L^2(\sigma_s)$.

Differentiating orthogonality gives the exact identity


$$
\partial_s\pi_{m,s}(y)
=
-bJ_m(s)K_{m-1,s}(y,-s).
\tag{5.3}
$$


Indeed, for $k<m$,


$$
\int\frac{\pi_{m,s}(y)\pi_{k,s}(y)}{y+s}\,d\sigma_s(y)
=
\pi_{k,s}(-s)J_m(s),
$$


because


$$
\frac{\pi_{k,s}(y)-\pi_{k,s}(-s)}{y+s}
$$


has degree $k-1$, and its product with $\pi_{m,s}$ integrates to zero.

Integrating (5.3) against $y^de^{-y}\,dy$ gives


$$
C_m'(s)
=
-bJ_m(s)
\sum_{k=0}^{m-1}
\frac{\pi_{k,s}(-s)C_k(s)}
{\|\pi_{k,s}\|_{\sigma_s}^2}.
\tag{5.4}
$$


All zeros of $\pi_{k,s}$ are positive. Hence $\pi_{k,s}(-s)$ has sign $(-1)^k$, the same sign as $C_k(s)$. Every summand in (5.4) is positive, including $k=0$.

Equations (5.2) and (5.4) therefore imply


$$
(-1)^mC_m'(s)<0\qquad(s>0).
$$


The moments, orthogonal-polynomial coefficients, and the displayed integrals are continuous at $s=0$, where the measure is $y^{b+d}e^{-y}\,dy$. Taking the limit proves the assertion on $s\ge0$. ∎

This is a structural monotonicity theorem. Its proof uses the complete kernel projection; no large-$y$ or low-degree part is omitted.

---

## 6. Comparing the actual polynomial with orthogonality on $x>1$

Let $\pi_h^*$ be the monic degree-$h$ orthogonal polynomial for the restricted measure


$$
d\mu^*(x)=x^b(x-1)^de^{-x}\mathbf1_{(1,\infty)}(x)\,dx.
$$


Write


$$
d\nu(x)=(x-1)^de^{-x}\,dx.
$$



### Proposition 6.1 — A full-tail bound

For the actual monic $p_h$,


$$
\boxed{
\frac{|F|}{a}
\le
e^{-1}n!+\frac{|p_h(0)|}{b}.
}
\tag{6.1}
$$


Equivalently,


$$
\boxed{
|F|\le e^{-1}a n!+\frac{|r_0|}{b}.
}
\tag{6.2}
$$



#### Proof

Let $K^*_{h-1}$ be the reproducing kernel for degree at most $h-1$ in $L^2(\mu^*)$. Since $p_h-\pi_h^*$ has degree at most $h-1$, the original orthogonality equations give the exact projection identity


$$
p_h(x)
=
\pi_h^*(x)
-\int_0^1p_h(y)K^*_{h-1}(x,y)\,d\mu(y).
\tag{6.3}
$$



Put


$$
L^*(y)=\int_1^\infty K^*_{h-1}(x,y)\,d\nu(x).
$$


If $\pi_k^*$ denotes the corresponding monic polynomial of degree $k$, then


$$
L^*(y)=
\sum_{k=0}^{h-1}
\frac{\pi_k^*(y)\int_1^\infty\pi_k^*(x)x^{-b}\,d\mu^*(x)}
{\|\pi_k^*\|_{\mu^*}^2}.
\tag{6.4}
$$


For $0\le y\le1$, every $\pi_k^*(y)$ has sign $(-1)^k$, because all its zeros exceed $1$. By Lemma 2.1, its accompanying integral has the same sign. Therefore


$$
L^*(y)>0\qquad(0\le y\le1).
\tag{6.5}
$$



The actual $p_h$ has all zeros above $1$, and $h$ is odd, so


$$
p_h(y)<0\qquad(0\le y\le1).
$$


Integrating (6.3) over $x>1$ against $\nu$ consequently gives


$$
\int_1^\infty p_h(x)\,d\nu(x)
\ge
\int_1^\infty \pi_h^*(x)\,d\nu(x).
\tag{6.6}
$$



After the change of variable $x=y+1$, the polynomial


$$
\pi_h^*(y+1)
$$


is the monic orthogonal polynomial for


$$
(y+1)^b y^de^{-y}\,dy.
$$


Lemma 5.1, together with Proposition 4.1, therefore gives


$$
\left|
\int_1^\infty\pi_h^*(x)\,d\nu(x)
\right|
=
e^{-1}|C_h(1)|
\le e^{-1}|C_h(0)|
=e^{-1}n!.
\tag{6.7}
$$


The integral in (6.7) is negative.

On the remaining interval, write the zeros of the actual $p_h$ as $\rho_i>1$. Then


$$
\frac{|p_h(y)|}{|p_h(0)|}
=
\prod_{i=1}^h\left(1-\frac y{\rho_i}\right)\le1
\qquad(0\le y\le1).
$$


Hence


$$
\left|\int_0^1p_h(y)\,d\nu(y)\right|
\le
|p_h(0)|\int_0^1(1-y)^d\,dy
=\frac{|p_h(0)|}{b}.
\tag{6.8}
$$



Combining (6.6)–(6.8) with the established $F<0$ proves (6.1). Since $|r_0|=a|p_h(0)|$, equation (6.2) follows. ∎

The tail $x>1$ has thus been controlled by an exact projection and a monotone full integral, not by extrapolating a small-$x$ estimate.

---

## 7. The evaluated comparison and its all-prime consequence

The $k=0$ term of the unchanged positive charge gives


$$
R\ge\frac{|r_0|}{n+1/4}.
\tag{7.1}
$$


Combining (6.2), (4.6), and (7.1) gives


$$
\frac{|F|}{R}
\le
\frac1{4e}\frac{(5/4)_d}{(3/4)_d}
+\frac{n+1/4}{b}.
\tag{7.2}
$$



The remaining product has an elementary square-root bound. For every integer $j\ge0$,


$$
\left(\frac{4j+5}{4j+3}\right)^2
<
\frac{2j+3}{2j+1},
$$


because


$$
(4j+3)^2(2j+3)-(4j+5)^2(2j+1)=2.
$$


Multiplication over $0\le j<d$ yields


$$
\frac{(5/4)_d}{(3/4)_d}\le\sqrt{2d+1}.
\tag{7.3}
$$


Thus, with


$$
B_b:=\frac{\sqrt{2b-1}}{4e}+2001+\frac1{4b},
$$


we have proved


$$
\boxed{\frac{|F|}{R}\le B_b.}
\tag{7.4}
$$



For $b\ge10^9$,


$$
\frac{\sqrt{2b-1}}{4e}<\frac{\sqrt b}{2},
\qquad
2001+\frac1{4b}<2002<\frac{\sqrt b}{2}.
$$


Therefore


$$
\boxed{|F|<\sqrt b\,R.}
\tag{7.5}
$$



### Theorem 7.1 — Actual all-prime decay of $g/R$

At every original index,


$$
\boxed{
\frac gR
=\frac{|F|}{qR}
\le\frac{B_b}{\mathcal D_h}
\le\frac{B_b}{h}
<\frac1{2000\sqrt b}.
}
\tag{7.6}
$$



This includes all prime factors of $g$. No restricted-prime gcd has been substituted.

By the unchanged whole-error lower bound,


$$
q(e+\pi)-p
>
\frac{h}{2B_b}
>
\frac{h}{2\sqrt b}
>
1000\sqrt b.
\tag{7.7}
$$



In particular, the actual primitive whole error tends to $+\infty$ along every unbounded collection of admissible original indices, including any such collection in the surviving progression.

This excludes vanishing primitive errors for this matrix family. It does not exclude other constructions for $e+\pi$.

---

## 8. The proposed tail margin is true, with $C=1$

This section verifies the particular outstanding obligation from Turn 17.

### 8.1 Exact normalization of the signed tail

Retain


$$
P(x)=\frac{p_h(x)}{p_h(0)}
=\prod_{i=1}^h\left(1-\frac{x}{\rho_i}\right),
$$




$$
H_j=h_j(\rho_1^{-1},\ldots,\rho_h^{-1}),
\qquad
A_d(x)=\sum_{j=0}^dH_jx^j,
$$


and


$$
K_d(x)=\sum_{k=0}^d
\frac{(-1)^k\binom nk}{(1/4)_{k+1}}x^k,
\qquad
Q_d=[K_dA_d]_{\le d}.
$$


The exact identities are


$$
\frac{|F|}{|r_0|}
=
\int_0^\infty P(x)^2(x-1)^de^{-x}A_d(x)\,dx,
\tag{8.1}
$$




$$
\frac R{|r_0|}
=
\int_0^\infty P(x)^2(x-1)^de^{-x}Q_d(x)\,dx.
\tag{8.2}
$$



Their normalization can be checked directly. The supplied Laguerre identity gives


$$
R=-\int_0^\infty e^{-x}r(x)K_d(x)\,dx.
$$


Interpolation at the zeros of $p_h$, followed by orthogonality, replaces $x^{-b}$ and $x^{-b}K_d(x)$ by their divided differences. Lemma 2.1’s explicit reciprocal-power formula gives respectively


$$
\frac{(-1)^h x^{-b}A_d(x)}{\prod_i\rho_i},
\qquad
\frac{(-1)^h x^{-b}Q_d(x)}{\prod_i\rho_i}.
$$


Since $h$ is odd and $|r_0|=a\prod_i\rho_i$, this gives (8.1)–(8.2).

Thus the signed tail is the actual normalized $R$-functional. It is not the parent’s different positive double-beta measure.

### 8.2 The controlled interval

For $0\le x\le4/n$,


$$
\left|\frac{Q_d(x)}{A_d(x)}\right|
\le
4\sum_{k=0}^\infty\frac{4^k}{k!(5/4)_k}
<324.
$$


Also


$$
P(x)^2A_d(x)\le P(x)\le1,
\qquad
(1-x)^de^{-x}\le1.
$$


Consequently


$$
\left|
\int_0^{4/n}
P(x)^2(x-1)^de^{-x}Q_d(x)\,dx
\right|
\le\frac{1296}{n}.
\tag{8.3}
$$



No sign is assigned to this small-interval integral.

### 8.3 A lower bound large enough to pay the explicit margin

The normalized coefficient polynomial is


$$
\sum_{k=0}^n\frac{|r_k|}{|r_0|}z^k
=(1+z)^dP(-z).
$$


Its coefficient of $z^d$ is at least $1$. Therefore


$$
\frac R{|r_0|}\ge c_{n,d}.
\tag{8.4}
$$


Now


$$
c_{n,d}
\ge
\frac{d!(3/4)_d}{(n+1/4)^{d+1}}
\ge
\frac1{n+1/4}
\left(\frac{d^2}{12(n+1/4)}\right)^d.
\tag{8.5}
$$


Here we used


$$
(3/4)_d\ge(3/4)^dd!,
\qquad d!\ge(d/e)^d>(d/3)^d.
$$



For $b\ge10^9$,


$$
d\ge\frac b2,\qquad n+\frac14<2002b,
$$


so


$$
\frac{d^2}{12(n+1/4)}
>
\frac b{96096}>2.
$$


Since $d\ge13$, equations (8.4)–(8.5) imply


$$
\boxed{\frac R{|r_0|}>\frac{5184}{n}.}
\tag{8.6}
$$



### 8.4 Fully evaluated tail inequality

Put


$$
Z_\beta(x)=P(x)^2(x-1)^dQ_d(x)
=\sum_{j=0}^{2n}z_jx^j,
$$


and


$$
\mathcal T_\beta(t)=
\sum_{j=0}^{2n}z_jj!\sum_{s=0}^j\frac{t^s}{s!}.
$$


The complete endpoint evaluation is


$$
\int_t^\infty e^{-x}Z_\beta(x)\,dx
=e^{-t}\mathcal T_\beta(t).
\tag{8.7}
$$



Let this tail at $t=4/n$ be $J$. From (8.2)–(8.3),


$$
J\ge\frac R{|r_0|}-\frac{1296}{n}.
$$


Meanwhile, (7.5) gives


$$
\frac{|F|}{h|r_0|}
<
\frac{\sqrt b}{h}\frac R{|r_0|}
<
\frac12\frac R{|r_0|}.
$$


Using (8.6),


$$
\begin{aligned}
J
&>
\frac{|F|}{h|r_0|}
+\frac12\frac R{|r_0|}
-\frac{1296}{n}\\
&>
\frac{|F|}{h|r_0|}
+\frac{2592}{n}-\frac{1296}{n}.
\end{aligned}
$$


Hence


$$
\boxed{
e^{-4/n}\mathcal T_\beta(4/n)
>
\frac{1296}{n}
+\frac{|F|}{h|r_0|}.
}
\tag{8.8}
$$



This proves the proposed margin (9.4), with $C=1$, at every original index.

The proof is not merely the naming of a factorial sum: the exact sum in (8.7) has now been bounded by the explicit right side of (8.8). The full polynomial and the complete tail are included.

---

## 9. Boundaries, source assessment, and verification scope

### 9.1 No enlarged original construction

The auxiliary arguments do not add a physical matrix row or column.

The quadrature used in Section 3 has precisely the previously permitted degree


$$
2N-1=d+2h-1.
$$


The moments of the shifted or restricted weights used in Sections 5–6 require factorials at most


$$
(b+d)+(2h-1)=2n.
$$


The tail polynomial in Section 8 has degree at most $2n$. Thus the new derivation does not exceed the already established $(2n)!$ factorial boundary.

Auxiliary divisions by $a$, $|r_0|$, or monic norms are analytic comparisons. They do not claim additional integer content or alter the least simultaneous clearer.

### 9.2 Assessment of the supplied claims

* The exact-content theorem, $h$-supported denominator theorem, and all-prime interpretation of $g=|F|/q$ are reused at their audited scope.
* The whole-error theorem is used only with its complete two-channel error and original hypotheses.
* The fixed base-quadrature node bound is used at its stated node count and exactness degree.
* Turn 17’s negative-kernel result is not contradicted. The present proof does not require that kernel to be nonnegative.
* The parent’s double-beta identity has correct coefficient normalization:
  

$$
c_{n,k}=(3/4)_kB(k+1,n-k+1/4).
$$


  Its positive measure is different from (8.1). This report does not identify them. The positive consequences used here are the unchanged finite coefficient charge and its coefficientwise monotonicity.
* No finite modular receipt is promoted to an infinite covering theorem.
* No conclusion is imported from the unrelated determinant families or almost-everywhere literature packets.

### 9.3 Bounded exact arithmetic

No new matrix, modular, root-bracketing, or series computation is needed for the proof.

If an independently authored transcription receipt is desired, its bounded inputs can be only:

1. the two degree-three polynomials
   

$$
(4X+3)^2(2X+3),\qquad (4X+5)^2(2X+1);
$$


2. the integers $4004,96096,10^9$.

Expected verifiable outputs are


$$
(4X+3)^2(2X+3)-(4X+5)^2(2X+1)=2,
$$




$$
4004^2=16032016<10^9,
\qquad
2\cdot96096=192192<10^9.
$$



These are finite transcription checks only. The uniform conclusions rest on the proofs above, not on such a receipt. No completed $n=13,b=3$ calculation or earlier finite series check needs repetition.

---

## 10. Conclusion and proof-status ledger

| Statement | Status |
|---|---|
| Original domain, finite matrix, complete $B_j$, and paid determinant normalization | Retained |
| Actual primitive $r$, least clearer $a$, contents, $\mathcal L_n$, and all paid divisions | Retained |
| $R\in\mathbb Z_{>0}$, $\ell=1$, actual all-prime $g$, actual primitive $q$ | Established and unchanged |
| Complete nonzero error and its two-sided bounds | Established and reused |
| Contact-deformation zero monotonicity | **New proved structural statement** |
| Exact comparison charge $R^{[0]}=4n!(3/4)_d/(5/4)_d$ | **New evaluated identity** |
| Exterior Christoffel monotonicity | **New proved structural statement** |
| Full-tail comparison $|F|\le e^{-1}an!+|r_0|/b$ | **New proved comparison** |
| $|F|/R\le \sqrt{2b-1}/(4e)+2001+1/(4b)$ | **New proved quantitative bound** |
| $g/R<1/(2000\sqrt b)$ on the entire original domain | **New proved all-prime theorem** |
| Tail margin (9.4) with $C=1$ | **Proved here** |
| Primitive whole-error divergence on every unbounded admissible original collection | **Proved here** |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

The outstanding comparison obligation for this family is closed by (7.4), and the stronger sufficient tail margin is closed by (8.8). These results show that the previously surviving progression does not evade the obstruction: its actual all-prime gcd is too small relative to $R$, and its complete primitive error grows rather than tends to zero.

The global research bottleneck is therefore no longer an unproved signed-average estimate for this matrix. An unconditional theorem about $e+\pi$ requires a different successful arithmetic mechanism or a materially different family with a proved infinite sequence of nonzero primitive errors tending to zero—or an independent proof of rationality. The present result is a rigorous obstruction at the stated family scope, not a universal impossibility theorem and not a resolution of the global problem.
