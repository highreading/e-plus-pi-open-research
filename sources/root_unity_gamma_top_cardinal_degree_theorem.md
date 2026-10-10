> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The top Hermite-cardinal coefficient of the corrected root-of-unity determinant

## A completely monotone simple-pole theorem, exact parity, and the remaining next-coefficient problem

Checked: 2026-08-27 UTC

## 1. Verdict

Put



$$
h=n+1,\qquad
 \Phi(X)=\prod_{j=0}^{m-1}(X-j)^h,\qquad
 c=\frac{m-1}{2},                                             \tag{1}
$$



and use the centered endpoint matrix



$$
K_{q,a}=\mathcal L\!\left(\bigl((X-c)^q\Phi\bigr)^{(a)}\right),
 \quad 0\le q\le D-2,\quad0\le a\le D.                    \tag{2}
$$



The frozen logistic-minor audit proves that $K$ has rank $D-1$ for
every $m\ge1$ and $n\ge D\ge2$.  Let $\Lambda_b$ be the Hermite
cardinal polynomial



$$
\Lambda_b^{(a)}(j)=(-1)^j\delta_{a,b},\qquad
 0\le j<m,\quad0\le a,b\le n,                              \tag{3}
$$



and put



$$
E_{b,a}=-\mathcal L(\Lambda_b^{(a)}).                       \tag{4}
$$



For any oriented basis $(C,D)$ of $\ker K$, the earlier complementary-
minor identity gives, with one fixed nonzero Pluecker scalar independent of
$\ell$,



$$
[z^\ell]\Gamma_{C,D}\ \doteq\!
 \sum_{a+b=\ell}
 \det\!\begin{pmatrix}K\\e_a^T\\E_b\end{pmatrix}.          \tag{5}
$$



This note proves the following all-parameter high-coefficient theorem.

> **Top-cardinal degree theorem.**  Let $m\ge2$ and
> $n\ge D\ge2$.  Then
> 

$$
> [z^{n+D}]\Gamma\ne0                                      \tag{6}
>
$$


> if and only if parity does not force it to vanish.  Explicitly, (6) holds
> exactly when
> 

$$
> \boxed{\ n+D\text{ is even}\quad\text{or}\quad
>         m,n\text{ are odd and }D\text{ is even}.\ }       \tag{7}
>
$$


> Equivalently, the top coefficient is forced to be zero exactly in the two
> disjoint families
> 

$$
> \boxed{
> \begin{array}{ll}
> \mathrm{A}:&n\text{ even},\ D\text{ odd},\quad m\text{ arbitrary},\\
> \mathrm{B}:&m\text{ even},\ n\text{ odd},\ D\text{ even}.
> \end{array}}                                               \tag{8}
>
$$



The nonvanishing direction is not a finite-grid extrapolation.  Its key new
input is that the centered top-cardinal quotient is, up to one global sign,
a **strictly completely monotone** rational function.  For even $n$, this
is a positive simple-pole expansion.  For odd $n$, all coefficients in a
nonconfluent ordered Newton expansion are positive; explicit centered
binomial-power Fourier sums prove that positivity for every $m,n$.

The corrected determinant identity and sign are



$$
\boxed{\Delta=W(C,D)-\Gamma_{C,D}.}                         \tag{9}
$$



Since $\deg W\le2D-2$, while $n+D\ge2D$, theorem (6) yields



$$
\boxed{\deg\Delta=\deg\Gamma=n+D}                          \tag{10}
$$



throughout (7), and the leading coefficients satisfy



$$
[z^{n+D}]\Delta=-[z^{n+D}]\Gamma.                          \tag{11}
$$



In the forced families (8), the next coefficient is exactly a sum of two
bordered minors.  It is nonzero in every exact grid tested for $m\ge2$, but
the two minors need not have the same sign.  No universal claim about that
sum is made here.  Thus (10) is proved in (7); the degree in (8) remains a
separate two-border comparison problem.

No conclusion about the arithmetic nature of $e+\pi$ is claimed here.

The replayable files are

* `scripts/root_unity_gamma_top_cardinal_degree_certificate.py`;
* `results/root_unity_gamma_top_cardinal_degree_certificate.json`.

## 2. The exact top border and its parity

At $\ell=n+D$, the sum in (5) has only the pair $(a,b)=(D,n)$.  Hence



$$
[z^{n+D}]\Gamma\ \doteq\
 B_{m,n,D}:=\det\!\begin{pmatrix}K\\e_D^T\\E_n\end{pmatrix}.
                                                                    \tag{12}
$$



There is a useful exact sign when the coordinate row is expanded.  The row
$e_D^T$ is row $D$ and column $D+1$ in the $(D+1)$-square matrix in
(12), using one-based numbering.  Therefore



$$
\boxed{
 B_{m,n,D}=-\det\!\begin{pmatrix}
 K_{*,0}&K_{*,1}&\cdots&K_{*,D-1}\\
 E_{n,0}&E_{n,1}&\cdots&E_{n,D-1}
 \end{pmatrix}.}                                             \tag{13}
$$



The centered checkerboard rule from the logistic audit is



$$
K_{q,a}=0\quad\text{unless}\quad a\equiv q+mn\pmod2.      \tag{14}
$$



The parity-reversing gauge is



$$
\widehat E_{b,a}=E_{b,a}+\frac m2\delta_{a,b},             \tag{15}
$$



and satisfies



$$
\widehat E_{b,a}=0\quad\text{unless}\quad b\equiv a+1\pmod2.
                                                                    \tag{16}
$$



Every column in (13) has $a\le D-1\le n-1$, so the diagonal correction in
(15) is absent.  Consequently



$$
E_{n,a}=0\quad(0\le a<D)\quad\text{unless}\quad
 a\equiv n+1\pmod2.                                        \tag{17}
$$



This exclusion of column $a=n$ is important: the ungauged entry
$E_{n,n}=-m/2$ can be nonzero, but it never occurs after the top coordinate
row has been expanded.

Counting the rows assigned to the two column parities now proves the
necessity in (7).  If $D=2d+1$, the columns $0,\ldots,D-1$ have counts
$(d+1,d)$, whereas the ordinary $K$-rows contribute $(d,d)$ after any
checkerboard offset.  The extra row must be even, which by (17) is equivalent
to $n$ odd.  If $D=2d$, both column counts are $d$.  The $K$-rows
contribute $d$ to parity $mn$ and $d-1$ to the other parity.  Thus the
extra row must have parity $1-mn$, or



$$
n+1\equiv1-mn\pmod2
 \quad\Longleftrightarrow\quad n(m-1)\equiv0\pmod2.          \tag{18}
$$



These are exactly (7)--(8).  In a forbidden case, one checkerboard block is
rectangular in the wrong direction, so (13) is identically zero.

## 3. The top cardinal quotient

The top cardinal has a zero of order at least $n$ at every node.  Direct
Hermite interpolation gives the simple-pole identity



$$
\boxed{
 \frac{\Lambda_n(X)}{\Phi(X)}
 =\frac1{n!}\sum_{j=0}^{m-1}
 \frac{(-1)^{j+h(m-1-j)}}
 {[j!(m-1-j)!]^h}\frac1{X-j}.}                              \tag{19}
$$



For completeness, if the residue in (19) is denoted by $\omega_j$, then



$$
\omega_j=\frac{(-1)^j}{n!\prod_{r\ne j}(j-r)^h},           \tag{20}
$$



which is exactly the coefficient required for the $n$-th derivative of
$\Phi(X)\omega_j/(X-j)$ at $j$ to be $(-1)^j$.  At every other node
that summand has a zero of order $h$; uniqueness below degree $mh$ proves
(19).

Set



$$
R(U)=\frac{\Lambda_n(c+U)}{\Phi(c+U)},\qquad
 \varepsilon\equiv(m-1)n+1\pmod2,quad\varepsilon\in\{0,1\}.
                                                                    \tag{21}
$$



Reflection of (19) gives



$$
\omega_{m-1-j}=(-1)^{n(m-1)}\omega_j,qquad
 R(-U)=(-1)^\varepsilon R(U).                               \tag{22}
$$



There is therefore a unique rational function $\rho_{m,n}$ such that



$$
\boxed{R(U)=U^\varepsilon\rho_{m,n}(-U^2).}                \tag{23}
$$



Its denominator has only the following simple rates:



$$
\begin{array}{ll}
 m=2k:&\lambda_r=(r-\tfrac12)^2,\quad1\le r\le k,\\[2mm]
 m=2k+1:&\lambda_r=r^2,\quad0\le r\le k.
 \end{array}                                                 \tag{24}
$$



Thus, in lowest terms,



$$
\rho_{m,n}(x)=\frac{N_{m,n}(x)}{\prod_r(x+\lambda_r)},
 \qquad \deg N_{m,n}=\#\{\lambda_r\}-1.                   \tag{25}
$$



The rate $\lambda_0=0$ for odd $m$ records the central simple pole; it
is not discarded.

## 4. A centered binomial-power positivity lemma

The universal positivity needed below is elementary apart from one standard
Schur--Szego closure theorem.

> **Lemma 1.**  For integers $N\ge0$ and $r\ge1$, put
> 

$$
> \mathcal B_{N,r}(\theta)=
> \sum_{j=0}^N\binom Nj^r e^{i(j-N/2)\theta}.                \tag{26}
>
$$


> Then
> 

$$
> \mathcal B_{N,r}(\theta)>0\quad(-\pi<\theta<\pi),         \tag{27}
>
$$


> and its endpoint values are nonnegative.

**Proof.**  Let



$$
F_{N,r}(z)=\sum_{j=0}^N\binom Nj^r z^j.                    \tag{28}
$$



First,



$$
F_{N,2}(z)=(1-z)^N
 P_N\!\left(\frac{1+z}{1-z}\right),                        \tag{29}
$$



where $P_N$ is the Legendre polynomial.  Its $N$ roots are simple and
lie in $(-1,1)$: this follows directly from orthogonality against every
polynomial of degree below $N$, by multiplying $P_N$ by the product of
its interior sign-change factors.  The fractional-linear map in (29) sends
those roots to negative real numbers.  Hence every root of $F_{N,2}$ is
negative.

Write a degree-$N$ polynomial in binomial coordinates as



$$
P(z)=\sum_j\binom Nj a_jz^j,
$$



and define Schur--Szego composition by coefficientwise multiplication of the
$a_j$.  Then



$$
F_{N,r}*F_{N,s}=F_{N,r+s-1}.                               \tag{30}
$$



Proposition 5 of V. Kostov and B. Shapiro, *On Schur-Szego composition of
polynomials* (arXiv:math/0605377v1, 2006), states in particular that the
degree-$N$ hyperbolic polynomials whose roots are all negative form a
semigroup under this composition.  Applying it repeatedly to $F_{N,2}$
proves that every $F_{N,r}$, $r\ge2$, has only negative roots; $r=1$
is $(1+z)^N$.  This is the only external theorem used in Lemma 1.

The polynomial (28) is palindromic.  Its negative roots therefore consist of
reciprocal pairs $-a,-a^{-1}$, together with possible roots at $-1$.
On $|z|=1$, after centering the powers, a reciprocal pair contributes



$$
a+a^{-1}+2\cos\theta>0\qquad(-\pi<\theta<\pi),             \tag{31}
$$



and a factor $-1$ contributes $2\cos(\theta/2)>0$.  Their products give
(27); continuity gives nonnegativity at the endpoints.  $\square$

Primary source for the composition statement:

* V. Kostov and B. Shapiro, [*On Schur-Szego composition of polynomials*](https://arxiv.org/abs/math/0605377), Proposition 5.

## 5. Even $n$: positive Stieltjes residues

Suppose $n$ is even.  Then $h$ is odd and (19) shows that all
$\omega_j$ have one sign, because



$$
j+h(m-1-j)\equiv m-1\pmod2.                               \tag{32}
$$



Also $\varepsilon=1$.  Pairing the poles at $U=\pm s$ in (19) gives



$$
\frac{\omega}{U-s}+\frac{\omega}{U+s}
 =\frac{2U\omega}{U^2-s^2}.                                \tag{33}
$$



Consequently, after multiplying by one global sign,



$$
\boxed{
 \rho_{m,n}(x)=\sum_r\frac{c_r}{x+\lambda_r},\qquad c_r>0.} \tag{34}
$$



For odd $m$, the central term is $c_0/x$, with the same sign as all
paired terms.  Formula (34) proves strict complete monotonicity immediately.

## 6. Odd $n$: explicit positive ordered Newton coefficients

Now suppose $n$ is odd.  Since $h$ is even, (19), up to one common
nonzero factor, has residues



$$
\omega_j\ \doteq\ (-1)^j\binom{m-1}{j}^{h}.               \tag{35}
$$



Although these residues alternate, the numerator in (25) has a positive
ordered Newton expansion.

### 6.1 Odd $m=2k+1$

Order the rates as $0,1,4,\ldots,k^2$.  Then, after one global sign,



$$
N_{m,n}(x)=\sum_{d=0}^{k}\gamma_d
             \prod_{r=0}^{d-1}(x+r^2),                     \tag{36}
$$



where the empty product is one.  Multiplying $\rho$ and $N$ by the
single global sign $(-1)^{k+1}$, one has



$$
\boxed{
 \gamma_d=\kappa_{m,n}\frac1{(2d)!}
 \sum_{r=-d}^{d}(-1)^r
 \binom{2d}{d+r}\binom{2k}{k+r}^{n},qquad
 \kappa_{m,n}=\frac1{n!\,[(2k)!]^n}>0.}                     \tag{37}
$$



Here and below $\kappa_{m,n}$ is independent of $d$.

To derive (37), let $c_r$ be the partial-fraction residue of $\rho$ at
$-r^2$.  Newton interpolation of the numerator at the first $d+1$ poles
gives



$$
\gamma_d=\sum_{r=0}^{d}c_r
              \prod_{t=d+1}^{k}(t^2-r^2).                  \tag{38}
$$



Unfold the symmetric residues to $-d\le r\le d$ and use



$$
\binom{2k}{k+r}^{h}\prod_{t=d+1}^{k}(t^2-r^2)
 =\binom{2k}{k+r}^{n}
   \frac{(2k)!}{(2d)!}\binom{2d}{d+r}.                     \tag{39}
$$



Indeed, (35) is exact with the common factor
$1/(n![(2k)!]^h)$; the unfolded partial-fraction coefficient contributes
the sign $(-1)^{k+1}$.  Thus all omitted factors in (38)--(39) are common
in $d$, and the displayed normalization gives exactly the value of
$\kappa_{m,n}$ in (37).

The sum in (37) is strictly positive.  Indeed, define



$$
A(\theta)=\mathcal B_{2k,n}(\theta)>0\quad(|\theta|<\pi)  \tag{40}
$$



by Lemma 1, and



$$
K_d(\theta)=\sum_{r=-d}^{d}(-1)^r\binom{2d}{d+r}e^{ir\theta}
 =4^d\sin^{2d}(\theta/2)\ge0.                              \tag{41}
$$



Parseval's coefficient identity says that the sum in (37) is



$$
\frac1{2\pi}\int_{-\pi}^{\pi}A(\theta)K_d(\theta)\,d\theta>0.
                                                                    \tag{42}
$$



### 6.2 Even $m=2k$

Put $a_r=r-\tfrac12$.  With the rates ordered as
$a_1^2,\ldots,a_k^2$, and again multiplying $\rho,N$ by the single
global sign $(-1)^{k+1}$, one has



$$
N_{m,n}(x)=\sum_{d=0}^{k-1}\gamma_d
             \prod_{r=1}^{d}(x+a_r^2),                     \tag{43}
$$



and



$$
\boxed{
 \gamma_d=\kappa_{m,n}\frac1{(2d+1)!}
 \sum_{j=0}^{2d+1}(-1)^{d+1+j}
 \left(j-d-\frac12\right)\binom{2d+1}{j}
 \binom{2k-1}{k-d-1+j}^{n},\quad
 \kappa_{m,n}=\frac1{n!\,[(2k-1)!]^n}>0.}                  \tag{44}
$$



The residue-to-Newton identity is again (38), with half-square rates.  For
$s=j-d-\tfrac12$, the factorial cancellation is



$$
\binom{2k-1}{k-d-1+j}^{h}
 \prod_{r=d+2}^{k}(a_r^2-s^2)
 =\binom{2k-1}{k-d-1+j}^{n}
  \frac{(2k-1)!}{(2d+1)!}\binom{2d+1}{j}.                  \tag{45}
$$



Before global normalization, unfolding the two half-integer poles gives the
factor $(-1)^{k-d}$.  The kernel in (44) contributes
$(-1)^{d+1}$, so their product is the $d$-independent sign
$(-1)^{k+1}$.  Together with (45), this gives the exact value of
$\kappa_{m,n}$ in (44).

For strict positivity, use $A(\theta)=\mathcal B_{2k-1,n}(\theta)$ and



$$
\begin{aligned}
 L_d(\theta)
 &=\sum_{j=0}^{2d+1}(-1)^{d+1+j}
 \left(j-d-\frac12\right)\binom{2d+1}{j}
 e^{i(j-d-1/2)\theta}\\
 &=2^{2d}(2d+1)\sin^{2d}(\theta/2)\cos(\theta/2)\ge0
 \qquad(-\pi\le\theta\le\pi).                            \tag{46}
 \end{aligned}
$$



Again Parseval identifies the sum in (44) with
$(2\pi)^{-1}\int A L_d$, which is strictly positive.  Thus every
$\gamma_d$ in (36) or (43) is positive.

## 7. The Coxian form and strict complete monotonicity

Divide (36) or (43) by the full denominator in (25).  In the odd case,



$$
\rho(x)=\sum_{d=0}^{k}
 \frac{\gamma_d}{\prod_{r=d}^{k}(x+r^2)},                  \tag{47}
$$



and in the even case,



$$
\rho(x)=\sum_{d=0}^{k-1}
 \frac{\gamma_d}{\prod_{r=d+1}^{k}(x+a_r^2)}.              \tag{48}
$$



Every $\gamma_d$ is positive.  Each reciprocal factor
$(x+\lambda)^{-1}$ is the Laplace transform of $e^{-\lambda t}$, and a
product is the Laplace transform of the convolution of those kernels.  The
zero rate in (47) is harmless: its kernel is the positive function one, and
the Laplace integral still converges for $x>0$.  Therefore (34), (47), and
(48) prove the all-parameter statement



$$
\boxed{(-1)^r\rho_{m,n}^{(r)}(x)>0
        \quad(x>0,\ r=0,1,2,\ldots)}                        \tag{49}
$$



after one global sign normalization.

## 8. Strict complete monotonicity proves every parity-allowed top border

Assume the parity balance (7).  Permute the rows and columns of (13) by
parity.  One block contains only ordinary rows of $K$; it is an initial
square parity minor and is nonzero by the all-parameter logistic normality
theorem.  The other block consists of $E_n$ and one fewer ordinary rows.

Let $p\equiv n+1\pmod2$.  For even $m$, the ordinary rows in the
augmented block are



$$
(X-c)^{p+2u}\Phi(X),\qquad u=0,1,\ldots,                  \tag{50}
$$



and $\varepsilon=p$.  For odd $m$, they are



$$
(X-c)^{1+2u}\Phi(X),\qquad u=0,1,\ldots,                  \tag{51}
$$



and $\varepsilon=1$.  Hence in either case, by (23), the cardinal row
divided by the first ordinary row is $\rho(-U^2)$.

Apply the positive contour representation and integrate the selected
derivatives by parts exactly as in the logistic-minor theorem.  On
$U=it$, after common nonzero row and column factors are removed, the row
collocation system for a block of size $r\ge2$ is



$$
\rho(t^2),\ 1,\ t^2,\ldots,t^{2r-4}.                      \tag{52}
$$



For $r=1$, the system consists only of $\rho(t^2)$; the same argument
below applies with a zeroth-order divided difference.

The column system is degree graded in
$\tanh^2(\pi t)$ for even $m$, and in
$\coth^2(\pi t)$ for odd $m$.  Its determinant is a nonzero leading-
coefficient factor times a Vandermonde.  The contour measure is strictly
positive on $t>0$.

There is no suppressed central term in the odd-$m$ case.  All columns in
(13) satisfy $a\le D-1\le n-1$, so the central point mass is zero by the
cardinal conditions



$$
\Lambda_n^{(a)}(c)=0\qquad(a<n).                            \tag{53}
$$



Moreover, $\Lambda_n(c+it)=O(t^n)$.  Every boundary term produced while
integrating $a$ times against $1/\sinh(\pi t)$ is



$$
O(t^{n-a}),                                                 \tag{54}
$$



which tends to zero because $a\le n-1$.  The final integrand is locally
integrable.  Thus (52) is an exact boundary-free representation.

For $0<x_1<\cdots<x_r$, the row determinant in (52) is a Vandermonde times
the divided difference



$$
\rho[x_1,\ldots,x_r].                                      \tag{55}
$$



The Hermite--Genocchi formula and (49) give it the strict sign
$(-1)^{r-1}$.  Andreief's identity now represents the augmented block as
an integral whose row and column determinants each have one fixed strict
sign.  The augmented block is nonzero.  Multiplying it by the ordinary
initial block proves $B_{m,n,D}\ne0$, and hence (6), in every regime (7).

Together with the parity count in Section 2, this completes the proof of the
top-cardinal degree theorem.

## 9. Consequence for the corrected determinant

The exterior correction has the exact sign



$$
\Gamma=C\beta_D-D\beta_C,                                  \tag{56}
$$



whereas the corrected endpoint Wronskian is



$$
\Delta=W(C,D)-\Gamma.                                      \tag{57}
$$



The Wronskian satisfies $\deg W\le2D-2$: the possible degree
$2D-1$ cancels between $CD'$ and $DC'$.  Since $n\ge D$,



$$
n+D\ge2D>2D-2.                                             \tag{58}
$$



Thus the nonzero coefficient from Section 8 cannot be cancelled by $W$,
and (10)--(11) follow.  This proves $\Delta\ne0$ and its exact degree in
all parity-allowed top regimes, without any assumption on an unknown
algebraic degree or height elsewhere in the project.

## 10. The parity-forced next coefficient

In either family (8), formula (5) gives the exact next coefficient



$$
\boxed{
 [z^{n+D-1}]\Gamma\ \doteq\
 \det\!\begin{pmatrix}K\\e_D^T\\E_{n-1}\end{pmatrix}
 +\det\!\begin{pmatrix}K\\e_{D-1}^T\\E_n\end{pmatrix}.}  \tag{59}
$$



Its degree is still safely above the Wronskian range:



$$
n+D-1\ge2D-1>2D-2.                                        \tag{60}
$$



The new cardinal row has a useful exact double-pole expansion.  With
$H_0=0$ and $H_j=1+\cdots+1/j$,



$$
\boxed{
 \frac{\Lambda_{n-1}(X)}{\Phi(X)}
 =\sum_{j=0}^{m-1}\left[
 \frac{n\omega_j}{(X-j)^2}
 -\frac{n(n+1)(H_j-H_{m-1-j})\omega_j}{X-j}
 \right].}                                                  \tag{61}
$$



The double coefficient enforces the $(n-1)$-st cardinal derivative; the
simple coefficient cancels the next Taylor coefficient of $\Phi/(X-j)^h$,
so (61) follows directly from the Hermite conditions.

Equation (59), not either summand separately, is the target.  On the exact
grid



$$
2\le m\le6,\qquad2\le n\le7,\qquad
 2\le D\le\min(6,n),                                       \tag{62}
$$



the sum is nonzero in every forced-top-zero tuple.  For even $m$, the two
terms have compatible signs in the tested cases.  For odd $m$, even $n$,
and odd $D$, they can have opposite signs; at $m=1$ the analogous terms
cancel in the known polynomial-multiple degeneracy.  This makes a universal
claim from (62) unsafe.  A proof of (59) for $m\ge2$ requires a genuine
two-border sign comparison, or a new combined determinant representation.

Accordingly, the first all-parameter guaranteed coefficient above
$2D-2$ is $n+D$ in (7).  No coefficient above $2D-2$ is claimed here
for the two families (8).

## 11. Exact replay and logical scope

The certificate performs the following exact operations over $\mathbb Q$.

1. It reconstructs (19), verifies (22)--(25), and checks every top-cardinal
   jet exactly.
2. For
   

$$
2\le m\le12,\qquad2\le n\le9,                            \tag{63}
$$


   it verifies the one-sign Stieltjes residues for even $n$, and for odd
   $n$ verifies every ordered Newton coefficient, every Fourier sum in
   (37) or (44), and the common-in-$d$ proportionality exactly.
3. On (62), it builds $K,E_n,E_{n-1}$ directly, verifies the top border is
   nonzero exactly in (7), and records the next sum (59).
4. The finite calculations replay the formulas and provide regression tests.
   The all-parameter proof is Sections 3--8, not an inference from the grids.
5. The next-coefficient observation in Section 10 is explicitly diagnostic
   and is not promoted to a theorem.

The deterministic exact-row digest for (63) is

    40f45cf25fa2a6fe73b91d3923eba146ffb955d360de7639b7551aa6c00da3b2
