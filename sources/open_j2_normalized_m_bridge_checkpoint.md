> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# OPEN checkpoint — normalized ordinary-$j=2$ $M$-bridge

Date: 2026-08-31

This is an **unnumbered OPEN checkpoint**, not a sealed item or theorem
package.  It records the correct reduction that survived the Item 299/303
work and explicitly retracts one invalid intermediate route.  It proves no
all-$n$ bridge, recurrence, prime-density estimate, or capacity saving.

## Exact beta-functional reversal

Let $r\geq1$ be odd with $3\nmid r$, and put



$$
K_0=(1-z)^r(1+z),\qquad K_1=(1-z)^r(1+z)^4.
$$



For $\nu=0,1$, define the parity polynomials



$$
V_\nu(t)=\sum_{j\geq0}(-1)^j[z^{2j}]K_\nu\,t^j,
 \qquad
 O_\nu(t)=\sum_{j\geq0}(-1)^j[z^{2j+1}]K_\nu\,t^j,
$$



and the normalized beta functional



$$
\mathfrak B_{a,b}(t^j)=\frac{(a)_j}{(a+b)_j}.
$$



Set



$$
H=\frac{r+1}{2},\qquad b_0=-\frac{2r}{3},\qquad
 b_1=b_0-1,\qquad \rho=\frac{r}{2(2r+3)},
$$





$$
C_0=-\frac{r!}{(-2r/3)_{r+1}},\qquad
 C_1=\frac{(r+1)!}{(-2r/3-1)_{r+2}},
$$



and



$$
\kappa_0=-(-1)^H\frac{(-r/3)_H}{(-r)_H},\qquad
 \kappa_1=-(-1)^{H+1}
                 \frac{(-r/3)_{H+1}}{(-r-1)_{H+1}}.
$$



The Item 291 upper coordinates $f_0,f_1$ and affine constants
$d_0,d_1$ satisfy the exact identities



$$
\begin{aligned}
 f_0&=\mathfrak B_{H+1/2,b_0}(O_0),\\
 f_1&=\rho\,\mathfrak B_{H+1/2,b_1}(O_1),\\
 d_0&=\frac{C_0\kappa_0}{2}\,
          \mathfrak B_{H,b_0}(V_0),\\
 d_1&=\frac{C_1\kappa_1}{2}\,
          \mathfrak B_{H,b_1}(V_1).
\end{aligned} \tag{A}
$$



Here $d_\nu$ is the affine constant from Item 250/291; the complete
lower tail is $2d_\nu$.  Formula (A) follows by reversing coefficients
with



$$
[z^\ell]K_0=-[z^{r+1-\ell}]K_0,
 \qquad
 [z^\ell]K_1=-[z^{r+4-\ell}]K_1,
$$



and using



$$
(a)_{N-j}=(a)_N\frac{(-1)^j}{(1-a-N)_j}.
$$



The scalar factors also obey



$$
rC_1\kappa_1=(r+3)\rho C_0\kappa_0. \tag{B}
$$



All displayed Pochhammer denominators are nonzero for
$r\equiv1,5\pmod6$.  The identities (A)--(B) were independently replayed
with exact rational arithmetic for all 67 admissible odd $r\leq199$;
the row-stream SHA-256 is

~~~text
9f0841ccf918e04c53c4d42ee98ac1fdf7c7a621a82e0f3fad0fb25329934b50
~~~

The replay is an implementation check; coefficient reversal is the
all-$r$ proof.

## Correct first-shift Hermite reduction

Keeping $1-u^2$ unchanged, define the plus-chart weight and its
six-step multiplier by



$$
w_r(u)=u^r(1-u^2)^{-2r/3-1}(1-iu)^r,
 \qquad
 \psi(u)=\frac{u^6(1-iu)^6}{(1-u^2)^4}.
$$



Let



$$
\mathcal D_r=\frac{d}{du}+\frac{w_r'(u)}{w_r(u)}.
$$



Exact polynomial reduction over $\mathbb Q(i,r)$ gives



$$
(1+iu)\psi(u)=a_0(r)+a_1(r)u+a_2(r)u^2+\mathcal D_rS_r(u), \tag{C}
$$



where



$$
a_0=-\frac{27(r+1)(r+5)(71r^2+411r+648)}
 {32(r+3)(r+6)(2r+3)(2r+9)},
$$





$$
a_1=\frac{27i(r+5)(289r^3+2173r^2+5316r+4032)}
 {32(r+3)(r+6)(2r+3)(2r+9)},
$$





$$
a_2=\frac{135(r+4)(r+5)(29r+69)}
 {32(r+3)(r+6)(2r+9)}.
$$



One compact exact certificate for (C) is



$$
S_r(u)=\frac{u(1-iu)N_r(u)}{(1-u^2)^3},
 \qquad \deg_uN_r\leq10,
$$



where $N_r$ is the unique solution over $\mathbb Q(i,r)$ of



$$
(1+iu)u^6(1-iu)^6
 =(a_0+a_1u+a_2u^2)(1-u^2)^4+\mathcal L_{r,3}N_r, \tag{D}
$$



with the sparse operator specified on monomials by



$$
\begin{aligned}
 \mathcal L_{r,3}(u^k)={}&(k+r+1)u^k
 -i(k+2r+2)u^{k+1}\\
 &+\left(-k+7+\frac r3\right)u^{k+2}
 +i\left(k-6+\frac{2r}{3}\right)u^{k+3}.
\end{aligned}
$$



Thus (C) is a cleared polynomial identity, not a numerical fit.  It is
only the first shift in one chart.  No claim is made here that integrating
the exact term has no endpoint contribution in every desired
continuation; that issue belongs to the missing complete certificate.

## Exact finite checks beyond the original fit

Using the original Item 250 tail definitions and the independently
certified Item 237 Lagrange coefficient, without using the fitted
recurrence to generate either side, the proposed bridge



$$
\frac{16^nM_n}{g_n}=\lambda_e[x^{6n+e}]C(x),
 \qquad
 \lambda_1=-\frac{891}{100},\quad
 \lambda_5=\frac{3897234}{41405},
$$



continues to agree exactly for both rays on the new range
$12\leq n\leq29$.  The 36 new rows have SHA-256

~~~text
00a89bfef87b35a59c82d7a69aac05023e43cf48c6d551df00a5b5b76dce24ef
~~~

The candidate recurrence also has exact zero residual for both rays at
all new starts $12\leq n\leq26$, with residual-row SHA-256

~~~text
06532454f6d2bf4838757591a4333887c9313009bccdbb437e8cf73e160b7547
~~~

These checks are **EXACT FINITE ONLY** and are not theorem evidence.

## Discarded route and remaining gap

An intermediate complex-period argument incorrectly replaced



$$
1-u^2
$$



by $(1-iu)(1+iu)$.  In fact
$(1-iu)(1+iu)=1+u^2$.  Every reduction based on that false
factorization was discarded before packaging and supports no claim.

The following remain missing:

* the second- and third-shift Hermite reductions in both real charts;
* the exact tensor/determinant cancellation for the known order-three
  operator;
* a complete endpoint and normalization audit for the combined
  certificate;
* an all-$n$ proof of the normalized-$M$ bridge or of recurrence
  membership.

Accordingly, the bridge is **OPEN**, this checkpoint proves no new
collision condition, and



$$
\boxed{\text{new booking}=0.}
$$



The raw ordinary-$j=2$ ceiling remains $1/105$ per $6M$.
