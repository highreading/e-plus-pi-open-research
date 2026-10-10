> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The hard odd-frequency family at endpoint degree three

## A strict covariance proof of the corrected next-border sign

Checked: 2026-08-27 UTC

## 1. Scope and theorem

This note treats exactly the degree-three subfamily of the parity-forced
odd-frequency case:



$$
m=2k+1\geq3,\qquad n\geq4\text{ even},\qquad
 h=n+1,\qquad D=3.                                        \tag{1}
$$



It uses the notation of
`sources/root_unity_gamma_forced_odd_m_next_coefficient_audit.md`, with the
phase correction derived directly below.  Put



$$
V(x)=\prod_{r=1}^{k}(x+r^2)^h,\qquad
 \mathcal E=2x\frac d{dx}+h+1.                            \tag{2}
$$



The symmetric centered partial fractions give the natural positive
Stieltjes function



$$
\rho_+(x)=\frac{w_0}{x}
       +2\sum_{r=1}^{k}\frac{w_r}{x+r^2},\qquad w_r>0.     \tag{3}
$$



If $R(U)=\Lambda_n(k+U)/\Phi(k+U)$, direct substitution gives



$$
R(it)=-it\,\rho_+(t^2),\qquad
 \Lambda_n(k+it)=-A_\Phi i\,t^{h+1}V(t^2)\rho_+(t^2).     \tag{4}
$$



Since $d/dX=-i\,d/dt$ on $X=k+it$,



$$
\Lambda_n'(k+it)=-A_\Phi t^h\mathcal E(V\rho_+)(t^2).
                                                               \tag{4a}
$$



Thus $F=\Lambda_{n-1}-\Lambda_n'$ and $F/\Phi=\psi$ give



$$
V\sigma=V\psi-\mathcal E(V\rho_+).                       \tag{4b}
$$



Direct removal of the common column factors gives opposite prefactors for
the even and odd bordered ratios.  Equivalently, the exact endpoint identity
then has normalized target



$$
\mathcal T=
 \operatorname {NB}_A(V\psi)
 -\left\{
 \operatorname {NB}_A(\mathcal E(V\rho_+))
 -\operatorname {NB}_G(\mathcal E(V\rho_+))
 \right\}.                                                \tag{5}
$$



Equivalently, define the signed real-row function



$$
\rho_-=-\rho_+
 =-\frac{w_0}{x}-2\sum_{r=1}^{k}\frac{w_r}{x+r^2}.        \tag{6}
$$



Then $\Lambda_n(k+it)=A_\Phi i\,t^{h+1}V\rho_-$, and (5) is



$$
\boxed{
 \mathcal T=
 \operatorname {NB}_A(V\psi)
 +\left\{
 \operatorname {NB}_A(\mathcal E(V\rho_-))
 -\operatorname {NB}_G(\mathcal E(V\rho_-))
 \right\}.}                                               \tag{7}
$$



Here $A$ has its sole ordinary row $V$, while $G$ has its sole
ordinary row $\mathcal EV$.  The simple-pole cancellation theorem gives



$$
\boxed{
 \psi(x)=\sum_{r=1}^{k}\frac{c_r}{x+r^2},
 \qquad c_r>0.}                                           \tag{8}
$$



The result is the strict sign



$$
\boxed{\mathcal T>0.}                                    \tag{9}
$$



Consequently the normalized coefficient corresponding to
$[z^{n+D-1}]\Gamma=[z^{n+2}]\Gamma$ is nonzero in (1).  This closes the
hard parity comparison for $D=3$, but makes no assertion for $D\geq5$,
about primitive content or height, or about the arithmetic nature of
$e+\pi$.

The replayable files are

* `scripts/root_unity_forced_odd_m_D3_covariance_certificate.py`;
* `results/root_unity_forced_odd_m_D3_covariance_certificate.json`;
* `results/root_unity_forced_odd_m_D3_covariance_hashes.sha256`.

## 2. The probability normalization

Write



$$
Y(x)=\coth^2(\pi\sqrt x),\qquad
 q(x)=Q_1(Y(x)).                                         \tag{10}
$$



If



$$
\frac{d^{\ell}}{du^{\ell}}\frac1{\sinh u}
 =\frac{H_\ell(\coth u)}{\sinh u},                       \tag{11}
$$



then



$$
H_0=1,\qquad H_1(y)=-y,\qquad H_2(y)=2y^2-1.
$$



Therefore



$$
q(x)=2\coth^2(\pi\sqrt x)-1
     =1+2\operatorname {csch}^2(\pi\sqrt x),            \tag{12}
$$



which is strictly decreasing on $(0,\infty)$.

For the pairing



$$
\langle f,Q\rangle
 =2\int_0^\infty f(t^2)Q(Y(t^2))
       \frac{t^h}{\sinh(\pi t)}\,dt,                    \tag{13}
$$



put



$$
M=\langle V,1\rangle,
 \qquad
 d\mathbb P(t)=
 \frac{2V(t^2)t^h}{M\sinh(\pi t)}\,dt.                  \tag{14}
$$



This is a probability measure with a strictly positive density on
$(0,\infty)$.  Finally set



$$
a(x)=\frac{\mathcal EV(x)}{V(x)}
 =h+1+2h\sum_{r=1}^{k}\frac{x}{x+r^2}.                  \tag{15}
$$



Its derivative is



$$
a'(x)=2h\sum_{r=1}^{k}\frac{r^2}{(x+r^2)^2}>0.         \tag{16}
$$



Thus $a$ is strictly increasing, while $q$ is strictly decreasing.

## 3. Exact determinant algebra

At $d=1$, the two moment rows are



$$
M_A=(\langle V,1\rangle,\langle V,q\rangle),\qquad
 M_G=(\langle\mathcal EV,1\rangle,
                  \langle\mathcal EV,q\rangle).         \tag{17}
$$



Appending $e_1^T=(0,1)$ shows directly, with no phase convention left,



$$
\begin{aligned}
 \operatorname {NB}_A(f)
 &=\langle f,q\rangle-
   \frac{\langle V,q\rangle}{\langle V,1\rangle}
   \langle f,1\rangle,\\
 \operatorname {NB}_G(f)
 &=\langle f,q\rangle-
   \frac{\langle\mathcal EV,q\rangle}
        {\langle\mathcal EV,1\rangle}
   \langle f,1\rangle.                                  \tag{18}
 \end{aligned}
$$



Using (14)--(15), subtraction gives the exact identity



$$
\boxed{
 \operatorname {NB}_A(f)-\operatorname {NB}_G(f)
 =\langle f,1\rangle
   \frac{\operatorname {Cov}_{\mathbb P}(a,q)}
        {\mathbb E_{\mathbb P}a}.}                      \tag{19}
$$



The denominator is positive.  The covariance has the symmetrized form



$$
\operatorname {Cov}_{\mathbb P}(a,q)
 =\frac12\iint
   (a(x)-a(y))(q(x)-q(y))\,d\mathbb P(x)d\mathbb P(y)<0. \tag{20}
$$



Here $x=t^2$ and $y=s^2$.  Strictness follows from the opposite strict
monotonicity and the positive continuous density.

## 4. The signed Euler border

For completeness, the weights in (3) are



$$
w_r=\frac1{n![(k+r)!(k-r)!]^h}\quad(0\leq r\leq k).    \tag{21}
$$



Every coefficient of $V$, $V/x$, and $V/(x+r^2)$ in its Laurent or
ordinary monomial basis is positive.  Hence every coefficient of
$V\rho_-$ in (6) is negative.  On a monomial $x^j$,



$$
[x^j]\mathcal Ef=(2j+h+1)[x^j]f.                       \tag{22}
$$



The smallest exponent in $V\rho_-$ is $j=-1$, and its multiplier is
$h-1=n>0$.  It follows that



$$
f_-:=\mathcal E(V\rho_-)<0\quad(x>0),\qquad
 \langle f_-,1\rangle<0.                                \tag{23}
$$



The central term behaves like $x^{-1}$ at zero.  In (13) its integrand is
$O(t^{h-3})=O(t^{n-2})$, so it is integrable for (1); exponential decay
handles infinity.  Combining (19), (20), and (23) proves



$$
\operatorname {NB}_A(f_-)-\operatorname {NB}_G(f_-)>0. \tag{24}
$$



Equivalently, for $f_+=\mathcal E(V\rho_+)=-f_-$,



$$
\operatorname {NB}_A(f_+)-\operatorname {NB}_G(f_+)<0. \tag{25}
$$



This agrees with the minus sign in the raw target (5).

## 5. The positive simple-pole border

From (8), both $\psi$ and $q$ are strictly decreasing.  Equation (18)
with $f=V\psi$ yields



$$
\begin{aligned}
 \operatorname {NB}_A(V\psi)
 &=M\left(
   \mathbb E_{\mathbb P}(\psi q)
   -\mathbb E_{\mathbb P}\psi\,
    \mathbb E_{\mathbb P}q\right)\\
 &=M\operatorname {Cov}_{\mathbb P}(\psi,q)>0.          \tag{26}
 \end{aligned}
$$



Indeed



$$
\operatorname {Cov}_{\mathbb P}(\psi,q)
 =\frac12\iint
  (\psi(x)-\psi(y))(q(x)-q(y))\,
  d\mathbb P(x)d\mathbb P(y)>0.                         \tag{27}
$$



Adding (24) and (26) proves (9) in the equivalent form (7); equivalently,
subtracting (25) from (26) proves the raw form (5).

## 6. Exact replay and logical scope

The certificate reconstructs
$V,\rho_\pm,\psi,\mathcal E(V\rho_\pm)$ over
$\mathbb Q$, checks all coefficient signs, and evaluates the two normalized
borders using exact Bernoulli moments on a finite grid.  It also checks the
symbolic $2\times2$ determinant identity, the phase
$R(it)=-it\rho_+(t^2)$, and the polynomial recurrence giving
$Q_1=2Y-1$.

As a phase anchor, for $k=1,n=4$, after the positive
$\pi^2$-scaling of the $Q_1$ column, the exact replay gives



$$
\operatorname {NB}_A(V\psi)=\frac{2025}{9698},\qquad
 \operatorname {NB}_A(f_+)-\operatorname {NB}_G(f_+)
 =\frac{16323}{38792}-\frac37
 =-\frac{2115}{271544},
$$



and hence



$$
\mathcal T=\frac{58815}{271544}>0.
$$



The finite grid is only a replay of the formulas.  Universality of (9) comes
from the strict covariance proof in Sections 2--5, not from extrapolation.
