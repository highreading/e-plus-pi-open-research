> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Reflection and reciprocity for centered exterior Wronskian sums

## Hyperbolic coefficient pairing, refined origin order, and the surviving type-$m$ barrier

Checked: 2026-08-27 UTC

## 1. Verdict

Let $R_C$ be a root-of-unity Hermite--Padé remainder attached to an
endpoint polynomial $C$, and suppose



$$
R_C(z)=O(z^L).                       \tag{1}
$$



If $C(-z)=\sigma_C C(z)$, $\sigma_C\in\{\pm1\}$, then the exact
all-parameter reflection law is



$$
\boxed{
 e^{mz}R_C(-z)=(-1)^m\sigma_C R_C(z).}                     \tag{2}
$$



Thus the half-centered remainder



$$
S_C(z)=e^{-mz/2}R_C(z)                                    \tag{3}
$$



has ordinary parity



$$
S_C(-z)=(-1)^m\sigma_C S_C(z).       \tag{4}
$$



For an exterior sum



$$
F_p(z)=\sum_{a<b}p_{ab}W(R_{C_a},R_{C_b})(z),\qquad
 G_p(z)=e^{-mz}F_p(z),                                    \tag{5}
$$



assume that $p$ is parity-homogeneous: every nonzero coordinate has
$\sigma_a\sigma_b=\tau$, or, basis-freely,
$(J\wedge J)p=\tau p$.  Then



$$
\boxed{G_p(-z)=-\tau G_p(z).}                             \tag{6}
$$



This yields two rigorous improvements over a symmetry-blind centered
circle estimate.

1. Opposite frequencies pair into exact $\cosh$ or $\sinh$ terms.
   The resulting coefficient-wise circle majorant is strictly smaller
   whenever a noncentral frequency occurs.
2. If $\tau=+1$, then $G_p$ is odd and has the uniform stronger origin
   order

   

$$
\operatorname {ord}_0G_p\ge2L+1.    \tag{7}
$$



   For a single same-parity endpoint block there is a refinement to
   $2(L+\delta_\sigma)+1$, where
   $\delta_\sigma\in\{0,1\}$ is defined below.

Reflection does **not** reduce the exponential type below $m$.  The
hyperbolic coarse factor is



$$
D_m(R)=1+2\sum_{r=1}^m\cosh(rR)
 =\frac{\sinh((m+\tfrac12)R)}{\sinh(R/2)}
 =e^{mR}\frac{1-e^{-(2m+1)R}}{1-e^{-R}},                  \tag{8}
$$



which still has type $m$.  Nor does antipodal symmetry reduce a circle
maximum: it only says that the same modulus is repeated on the opposite
semicircle.

Consequently, reflection improves finite prefactors and can add one or
three origin zeros in special parity blocks, but it cannot improve the
leading $n\log n$ analytic ledger.  No rank-gap, classification,
primitive-content, irrationality, or transcendence conclusion follows.

## 2. Exact remainder reflection

Retain a free frequency variable $y$ and write



$$
R_C(z,y)=C(z)+(1+y)T_C(z,y).                              \tag{9}
$$



Reflection followed by the common shift that restores the frequencies
$0,\ldots,m-1$ gives



$$
\begin{aligned}
 y^mR_C(-z,y^{-1})
  ={}&(-1)^mC(-z)\\
   &+(1+y)\left\{
      y^{m-1}T_C(-z,y^{-1})
      +\frac{y^m-(-1)^m}{y+1}C(-z)
     \right\}.                                             \tag{10}
\end{aligned}
$$



If $C(-z)=\sigma_C C(z)$, uniqueness of the order-$L$ interpolation
says that the reflected pair in (10) is
$(-1)^m\sigma_C$ times the original pair.  Setting $y=e^z$ proves
(2), and multiplying by $e^{mz/2}$ at $-z$ proves (4).

For a common scalar factor $h$,



$$
W(hf,hg)=h^2W(f,g).               \tag{11}
$$



Therefore



$$
e^{-mz}W(R_C,R_D)=W(S_C,S_D).                             \tag{12}
$$



If $S_C(-z)=\eta_CS_C(z)$ and
$S_D(-z)=\eta_DS_D(z)$, differentiation reverses parity, and direct
substitution gives



$$
W(S_C,S_D)(-z)=-\eta_C\eta_DW(S_C,S_D)(z)
                =-\sigma_C\sigma_DW(S_C,S_D)(z).           \tag{13}
$$



Summing (13) over a parity-homogeneous $p$ proves (6).  No Plücker or
decomposability relation was used.

The equivalent raw reciprocity is



$$
e^{2mz}F_p(-z)=-\tau F_p(z).       \tag{14}
$$



## 3. Exact coefficient reciprocity

Write the centered exponential polynomial uniquely as



$$
G_p(z)=\sum_{r=-m}^{m}P_r(z)e^{rz}
       =\sum_{r=-m}^{m}\sum_{k=0}^{2n}a_{r,k}z^ke^{rz}.    \tag{15}
$$



Put



$$
\epsilon=-\tau.               \tag{16}
$$



Uniqueness of exponential-polynomial expansion and (6) give



$$
\boxed{
 P_{-r}(z)=\epsilon P_r(-z),\qquad
 a_{-r,k}=\epsilon(-1)^ka_{r,k}.}                          \tag{17}
$$



At the middle frequency,



$$
a_{0,k}=0\quad\text{unless}\quad(-1)^k=\epsilon.          \tag{18}
$$



In terms of the raw coefficient polynomials
$F_p=\sum_{q=0}^{2m}F_qe^{qz}$, equation (17) is



$$
F_{2m-q}(-z)=\epsilon F_q(z).      \tag{19}
$$



## 4. Refined origin factors

For a parity block $\sigma$, set



$$
\eta_\sigma=(-1)^m\sigma,\qquad
 \delta_\sigma=
 \begin{cases}
 0,&\eta_\sigma=(-1)^L,\\
 1,&\eta_\sigma=-(-1)^L.
 \end{cases}                                               \tag{20}
$$



Equations (1) and (4) imply the exact factorization



$$
S_C(z)=z^{L+\delta_\sigma}f_C(z^2) \tag{21}
$$



for some entire $f_C$.  If $C,D$ lie in the same parity block, put
$\ell=L+\delta_\sigma$.  Then



$$
\begin{aligned}
 W(S_C,S_D)
  &=2z^{2\ell+1}
    \{f_C(z^2)f_D'(z^2)-f_D(z^2)f_C'(z^2)\}.
                                                               \tag{22}
\end{aligned}
$$



Consequently



$$
\boxed{
 \operatorname {ord}_0W(S_C,S_D)
 \ge2(L+\delta_\sigma)+1.}                                 \tag{23}
$$



The two endpoint-parity blocks have opposite $\eta_\sigma$, hence one
has $\delta_\sigma=0$ and the other has $\delta_\sigma=1$.  An arbitrary
same-parity exterior sum can combine both blocks, so its uniform common
factor is only



$$
z^{2L+1}.                     \tag{24}
$$



If it is supported entirely in the $\delta_\sigma=1$ block, the common
factor improves to $z^{2L+3}$.

For a mixed-parity wedge, the two base factors in (21) are
$z^L$ and $z^{L+1}$ in some order.  Its Wronskian therefore has the
common factor $z^{2L}$, but reflection alone supplies no additional
zero.  This explains why $G_p$ is even for $\tau=-1$ and odd for
$\tau=+1$, while reproducing the original universal order $2L$ in the
mixed case.

If the extra common order is denoted by $s\in\{0,1,3\}$, the corresponding
coarse stationary calculation replaces



$$
A=L-n\quad\text{by}\quad B=A+\frac{s}{2},                 \tag{25}
$$



and has radius and per-column gain



$$
\rho_s=\frac{2B}{m},\qquad
 \mathcal G_s
 =B\log\frac{2B}{e\pi m}-n\log\pi.                        \tag{26}
$$



Since $s$ is bounded, this refinement is $O(\log n)$ for fixed $m$,
not a change in the leading $n\log n$ term.

## 5. The paired hyperbolic circle majorant

Let $|z|=R$, $R>0$.  By (17), the two terms associated with
$(r,k)$, $r>0$, are



$$
a_{r,k}z^k
 \{e^{rz}+\epsilon(-1)^ke^{-rz}\}.                         \tag{27}
$$



For $z=x+iy$, one has



$$
\begin{aligned}
 |\cosh(rz)|^2&=\sinh^2(rx)+\cos^2(ry)\le\cosh^2(rR),\\
 |\sinh(rz)|^2&=\sinh^2(rx)+\sin^2(ry)\le\sinh^2(rR).
                                                               \tag{28}
\end{aligned}
$$



The second inequality follows from
$\sin^2(ry)\le r^2y^2$ and



$$
\sinh^2(rR)-\sinh^2(r|x|)
 \ge r^2(R^2-x^2)=r^2y^2;                                 \tag{29}
$$



the latter is a consequence of the monotonicity of
$\sinh^2u-u^2$.

Define



$$
H_+(t)=\cosh t,\qquad H_-(t)=\sinh t.                     \tag{30}
$$



Equations (27)--(30) give the coefficient-wise bound



$$
\boxed{
\begin{aligned}
 \max_{|z|=R}|G_p(z)|
 \le{}&
 \sum_{\substack{0\le k\le2n\\(-1)^k=\epsilon}}
     |a_{0,k}|R^k\\
 &+2\sum_{r=1}^{m}\sum_{k=0}^{2n}
   |a_{r,k}|R^kH_{\epsilon(-1)^k}(rR).
\end{aligned}}                                             \tag{31}
$$



The symmetry-blind coefficient-wise bound for the same paired
coefficients replaces every $2H_{\pm}(rR)$ by $2e^{rR}$.  For $rR>0$,



$$
2\cosh(rR)=e^{rR}+e^{-rR}<2e^{rR},\qquad
 2\sinh(rR)=e^{rR}-e^{-rR}<2e^{rR}.                        \tag{32}
$$



Thus (31) is rigorously and strictly smaller whenever at least one
noncentral coefficient is nonzero.  There is no uniform relative gain:
reflection permits all noncentral coefficients to vanish, in which case
the two bounds coincide.

### 5.1 A uniform coefficient-height form

Let



$$
H=\max_{r,k}|a_{r,k}|,\qquad R\ge1,
 \qquad
 N_\epsilon=
 \begin{cases}
 n+1,&\epsilon=+1,\\
 n,&\epsilon=-1.
 \end{cases}                                               \tag{33}
$$



Since $\sinh t\le\cosh t$, equation (31) implies



$$
\begin{aligned}
 \max_{|z|=R}|G_p(z)|
 &\le HR^{2n}
 \left\{N_\epsilon+2(2n+1)\sum_{r=1}^{m}\cosh(rR)\right\}\\
 &=HR^{2n}
 \left\{N_\epsilon+(2n+1)(D_m(R)-1)\right\}\\
 &\le(2n+1)HR^{2n}D_m(R),                                 \tag{34}
\end{aligned}
$$



where $D_m$ is (8).  The geometric-series form in (8) follows by putting
$q=e^{-R}$:



$$
\frac{D_m(R)}{e^{mR}}
 =1+q+\cdots+q^{2m}
 =\frac{1-q^{2m+1}}{1-q}.                                 \tag{35}
$$



Compared with the earlier centered coarse bound



$$
(2m+1)(2n+1)HR^{2n}e^{mR},                               \tag{36}
$$



the multiplicative ratio is at most



$$
\frac{1-e^{-(2m+1)R}}
 {(2m+1)(1-e^{-R})}<1.                                    \tag{37}
$$



At the root-of-unity stationary radii $R\ge4$, the residual factor
$D_m(R)/e^{mR}$ lies between $1$ and
$(1-e^{-4})^{-1}$.  Hence reflection can replace a substantial coarse
slot-count prefactor, but the logarithm of the remaining correction is
less than



$$
-\log(1-e^{-4})<0.019.             \tag{38}
$$



Most importantly,



$$
D_m(R)\sim e^{mR}\quad(R\to\infty). \tag{39}
$$



The exponential type remains exactly $m$.

## 6. Why no further uniform gain follows from reflection

### 6.1 Antipodal and maximum-modulus symmetry

Equation (6) gives $|G_p(-z)|=|G_p(z)|$.  It follows that the maximum on
a full circle equals the maximum on either closed semicircle containing
one point from every antipodal pair.  It does not make that maximum
smaller.  Applying the maximum-modulus principle to a half-disk introduces
the diameter as an additional boundary and supplies no new uniform bound.

### 6.2 Even/odd common factors

When $\epsilon=-1$, $G_p$ is odd and hence divisible by $z$; the
stronger version of this fact is already fully accounted for by (23)--(26).
When $\epsilon=+1$, $G_p$ is an even entire function and can be written
as a function of $z^2$, but this reformulation does not remove the
$e^{mR}$ radial growth in (39).

### 6.3 Extreme frequencies are not killed

The reciprocity law relates the $+m$ and $-m$ coefficient polynomials;
it does not force either to vanish.  Abstractly, both
$2\cosh(mz)$ and $2\sinh(mz)$ obey the required even/odd reflection and
have exact type $m$.

More significantly, the deterministic replay constructs the actual
full-endpoint Hermite--Padé remainders for



$$
m\in\{2,3\},\qquad n\in\{2,3,4\}.                         \tag{40}
$$



All $38$ monomial endpoint pairs have nonzero frequencies $+m$ and
$-m$ after centering.  Every one also attains exactly the lower origin
order predicted in Section 4.  These are exact rational computations, not
floating-point samples.  They are finite sharpness diagnostics, not an
all-parameter theorem, but they provide concrete counterexamples to any
claim that reflection by itself forces smaller type or an additional
uniform origin factor.

Thus any further improvement would have to use special arithmetic
cancellation, a rank restriction on the selected exterior vector, or
additional Hermite--Padé structure beyond reflection reciprocity.

## 7. Deterministic replay

The package consists of

* the present source note;
* scripts/root_unity_centered_exterior_reflection_certificate.py;
* results/root_unity_centered_exterior_reflection_certificate.json; and
* results/root_unity_centered_exterior_reflection_hashes.sha256.

Replay from the archive root with

    python3 scripts/root_unity_centered_exterior_reflection_certificate.py

The replay:

1. builds the actual full-endpoint interpolation map exactly over
   $\mathbb Q$;
2. verifies (2), (6), and (17) coefficient by coefficient;
3. computes exact Taylor orders and verifies that all $38$ pair rows
   attain the refined bounds (7) and (23);
4. checks four parity-homogeneous exterior sums and certifies each is
   genuinely nondecomposable by computing rank (4) for its exact skew
   coefficient matrix (a nonzero decomposable bivector has skew rank (2));
5. verifies that all diagnostic rows retain both extreme frequencies; and
6. checks the finite geometric-series identities and records bounded
   hyperbolic-prefactor diagnostics.

The all-parameter results are proved in Sections 2--6, not inferred from
the finite table.  No randomized computation is used.
