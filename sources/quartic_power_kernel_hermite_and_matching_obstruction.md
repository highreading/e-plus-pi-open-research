> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Hermite coordinates for the quartic power kernel

Date: 2026-08-27.

## 1. Scope and outcome

Put



$$
Q(x)=1+x^4,\qquad
 P_n(x)=x^n(1-x)^n,\qquad
 J_{n,k}=\int_0^1\frac{P_n(x)}{Q(x)^k}\,dx                 \tag{1}
$$



for integers $n\geq 0$ and $k\geq 1$.  This note gives an exact
Hermite reduction of every member of this family.  In particular, it gives
finite integer sums for both logarithmic coordinates and proves the two
infinite log-free families which had first appeared experimentally:



$$
k=1,\quad n\equiv6\pmod 8,                              \tag{2}
$$



and



$$
n=4j+2,\quad k=3j+2\quad(j\geq0).                       \tag{3}
$$



There is also the isolated log-free pair $(n,k)=(3,2)$.  An exact scan
over $0\leq n\leq160$, $1\leq k\leq160$ finds no other pair.  The
assertion that (2), (3), and $(3,2)$ are the complete all-parameter list
is recorded here as a conjecture, not as a theorem: the present note does
not contain the required global nonvanishing theorem for two oscillatory
residue sums.

The inversion-balanced family (3) has $k/n\to3/4$, not
$k\asymp n\log n$.  Its primitive coefficient-matched forms with the
exponential beta form diverge in absolute value even after the entire final
algebraic content is removed.  Thus this only known power-family ray is a
rigorous no-go.

Two neighboring powers can always be combined to cancel the remaining
$\log(1+\sqrt2)$ coordinate once $k>n/2$.  This is a genuine escape
from the single-integral classification.  It loses positivity and doubles
the main dyadic denominator.  Exact finite calculations find no vanishing
of its surviving $\pi$-determinant, but this note does **not** prove a
uniform lower bound for the resulting sign-indefinite form.  Consequently
the two-power critical construction remains an open branch, rather than a
proved improvement.

Nothing in this note classifies $e+\pi$.

## 2. Exact monomial Hermite reduction

For $m\geq0$, $k\geq1$, define



$$
A_{m,k}
 =\prod_{s=1}^{k-1}\frac{4s-m-1}{4s}
 =\frac{((3-m)/4)_{k-1}}{(k-1)!},                        \tag{4}
$$



with an empty product equal to one.  For $j\geq2$, put



$$
a_{m,j}=\frac{4j-m-5}{4(j-1)}.                          \tag{5}
$$



The elementary differential identity



$$
\frac{x^m}{Q^j}\,dx
 =a_{m,j}\frac{x^m}{Q^{j-1}}\,dx
 +\frac1{4(j-1)}d\!\left(\frac{x^{m+1}}{Q^{j-1}}\right) \tag{6}
$$



gives, on iteration,



$$
\frac{x^m}{Q^k}\,dx
 =A_{m,k}\frac{x^m}{Q}\,dx+dH_{m,k}(x),                 \tag{7}
$$



where one completely explicit choice is



$$
H_{m,k}(x)=
 \sum_{j=2}^k
 \frac1{4(j-1)}
 \left(\prod_{t=j+1}^k a_{m,t}\right)
 \frac{x^{m+1}}{Q(x)^{j-1}}.                            \tag{8}
$$



If $m=4q+r$, $0\leq r<4$, then



$$
\frac{x^m}{Q}=S_m(x)+(-1)^q\frac{x^r}{Q},              \tag{9}
$$



with



$$
S_m(x)=x^r\sum_{u=0}^{q-1}(-1)^u x^{4(q-1-u)}.          \tag{10}
$$



Equations (7)--(10) are an exact reduction, including its rational endpoint
term; no computer algebra is needed for the proof.

Write the unique reduced numerator as



$$
\omega_{n,k}(x)=a_{n,k}+b_{n,k}x+c_{n,k}x^2+d_{n,k}x^3. \tag{11}
$$



Then (4) and (9) give the closed finite sums



$$
\boxed{
 [x^r]\omega_{n,k}
 =\sum_{\substack{0\leq j\leq n\\n+j\equiv r\ (4)}}
 (-1)^{j+(n+j-r)/4}\binom nj A_{n+j,k}.}                 \tag{12}
$$



The rational coordinate is equally explicit:



$$
R_{n,k}=\sum_{j=0}^n(-1)^j\binom nj
 \left(
 H_{n+j,k}(1)+A_{n+j,k}\int_0^1S_{n+j}(x)\,dx
 \right).                                               \tag{13}
$$



Thus



$$
J_{n,k}=R_{n,k}+\int_0^1\frac{\omega_{n,k}(x)}{Q(x)}\,dx. \tag{14}
$$



## 3. The four period coordinates and the exact log-free criterion

Set $u=1+\sqrt2$.  Direct partial fractions give



$$
\begin{aligned}
 \int_0^1\frac{dx}{1+x^4}
   &=\frac{\pi}{4\sqrt2}+\frac{\log u}{2\sqrt2},\\
 \int_0^1\frac{x\,dx}{1+x^4}&=\frac\pi8,\\
 \int_0^1\frac{x^2\,dx}{1+x^4}
   &=\frac{\pi}{4\sqrt2}-\frac{\log u}{2\sqrt2},\\
 \int_0^1\frac{x^3\,dx}{1+x^4}&=\frac14\log2.
 \end{aligned}                                           \tag{15}
$$



Consequently



$$
\boxed{
 J_{n,k}=R_{n,k}
 +\frac{a_{n,k}-c_{n,k}}{2\sqrt2}\log u
 +\frac{d_{n,k}}4\log2
 +\left(\frac{a_{n,k}+c_{n,k}}{4\sqrt2}
          +\frac{b_{n,k}}8\right)\pi.}                  \tag{16}
$$



In particular, all logarithmic coordinates vanish exactly when



$$
d_{n,k}=0,\qquad a_{n,k}=c_{n,k}.                       \tag{17}
$$



This is also an equality criterion for the actual logarithmic number in
(16), not merely a formal-coordinate statement.  Indeed, $2$ and
$1+\sqrt2$ are multiplicatively independent: after clearing integer
exponents, taking the norm from $\mathbb Q(\sqrt2)$ first forces the
exponent of $2$ to vanish, and then the positive unit has no nonzero
power equal to one.  Baker's linear-independence theorem for logarithms of
algebraic numbers then makes $\log2$ and $\log(1+\sqrt2)$ linearly
independent over $\overline{\mathbb Q}$.

There is also a useful expression for the second logarithmic coordinate.
It is the coefficient of $x^{-1}$ at infinity:



$$
d_{n,k}=(-1)^n
 \sum_{\substack{j+4\ell=2n-4k+1\\0\leq j\leq n}}
 (-1)^{j+\ell}\binom nj\binom{k+\ell-1}{\ell}.           \tag{18}
$$



Thus



$$
k\geq\left\lfloor\frac n2\right\rfloor+1
 \quad\Longrightarrow\quad d_{n,k}=0.                  \tag{19}
$$



At every prospective critical scale $k\asymp n\log n$, only the single
coordinate $a_{n,k}-c_{n,k}$ remains.

## 4. The two proved infinite log-free families

### 4.1 The simple-pole family

For $k=1$, (7) says simply



$$
\omega_{n,1}\equiv[x(1-x)]^n\pmod{x^4+1}.              \tag{20}
$$



Let $\alpha_j=e^{(2j+1)\pi i/4}$.  The four eigenvalues
$\alpha_j(1-\alpha_j)$ have moduli



$$
r_- =\sqrt{2-\sqrt2},\qquad r_+=\sqrt{2+\sqrt2},        \tag{21}
$$



and arguments $\pm\pi/8$ and $\pm5\pi/8$, respectively.  Fourier
inversion at the four roots gives, for example,



$$
d_{n,1}=\frac12\left[
 r_-^n\cos\left(\frac{n\pi}8+\frac{3\pi}4\right)
 +r_+^n\cos\left(\frac{5n\pi}8-\frac\pi4\right)
 \right].                                                \tag{22}
$$



The analogous formula for $a_{n,1}-c_{n,1}$, or a direct sixteen-class
table in the same Fourier inversion, shows



$$
d_{n,1}=0\ \text{and}\ a_{n,1}=c_{n,1}
 \quad\Longleftrightarrow\quad n\equiv6\pmod8.          \tag{23}
$$



For completeness, in checking that no other class vanishes, one uses
$r_+/r_-=1+\sqrt2>1$; outside the classes where both cosines vanish,
the two unequal powers cannot cancel.  The two exceptional zeros of
$d_{n,1}$ at $n=0,1$ have $a_{n,1}-c_{n,1}=1$.

### 4.2 The inversion-balanced power ray

Let $n=2r$.  Under $\iota(x)=1/x$, the rational differential in (1)
satisfies



$$
\iota^*\left(\frac{P_n(x)}{Q(x)^k}\,dx\right)
 =-x^{4k-3n-2}\frac{P_n(x)}{Q(x)^k}\,dx.                \tag{24}
$$



Hence, when



$$
4k-3n-2=0,                                             \tag{25}
$$



it is anti-invariant.  The reciprocal roots of each quadratic factor of
$x^4+1$ form a pair.  Equation (24) makes the two residues in each pair
opposite, so both quadratic logarithmic residues vanish.  Since (25) also
implies (19), condition (17) follows.  Integrality of $k$ in (25) is
equivalent to



$$
n=4j+2,\qquad k=3j+2.                                  \tag{26}
$$



There is a useful equivalent trace computation.  Put $y=x+x^{-1}$ and



$$
h=2k-3r.
$$



The pushforward (trace) of the differential under the two-sheeted map
$x\mapsto y$ is



$$
-\frac{U_{h-2}(y/2)(y-2)^r}{(y^2-2)^k}\,dy,            \tag{27}
$$



where $U_m$ is the Chebyshev polynomial of the second kind, extended by
$U_{-1}=0$ and $U_{-m-2}=-U_m$.  The balanced ray is exactly $h=1$,
so (27) vanishes identically.

Finally, direct use of (12) gives the isolated pair



$$
\omega_{3,2}(x)=-\frac34+\frac32x-\frac34x^2,          \tag{28}
$$



which is log-free as well.

## 5. Exact dyadic coordinate denominators

Let $K=k-1$.  In lowest terms, the monomial multiplier (4) has
denominator



$$
\operatorname{den}(A_{m,k})=
 \begin{cases}
  2^{\,2K+v_2(K!)}=2^{\,3K-s_2(K)},&m\ \text{even},\\
  2^{\,K+v_2(K!)},&m\equiv1\pmod4,\\
  1,&m\equiv3\pmod4.
 \end{cases}                                             \tag{29}
$$



In the last case the Pochhammer symbol is an integer or is zero.  To prove
(29), remove the displayed power of two from every factor
$4s-m-1$.  For every odd prime power $p^a$, the remaining arithmetic
progression has invertible step modulo $p^a$, and among $K$ consecutive
indices it contains at least $\lfloor K/p^a\rfloor$ multiples of
$p^a$.  It therefore contains the entire odd part of $K!$.  No further
factor of two is available, which proves exactness.

Thus the common non-polynomial coordinate denominator in (12) divides



$$
D_k=2^{\,3(k-1)-s_2(k-1)}.                             \tag{30}
$$



This is an exact universal denominator, not an $O$-estimate.  Individual
coordinate sums can of course have additional dyadic content.

Equations (8), (10), and (13) give the exact rational coordinate
denominator.  A convenient uniform clearing denominator is



$$
\Delta_{n,k}=
 2^{\,3(k-1)-s_2(k-1)+k}
 \operatorname{lcm}(1,\ldots,k-1)
 \operatorname{lcm}(1,\ldots,2n+1).                     \tag{31}
$$



Every coordinate in (16), after the displayed factors $1/4$ and
$1/8$ are also cleared, lies in
$\Delta_{n,k}^{-1}\mathbb Z[\sqrt2]$.  Formula (13), rather than (31),
should be used when the minimal denominator is wanted.

To justify that (31) has no hidden factorial, inspect each summand of
(8).  Away from $2$, its numerator and factorial quotient are products
over two arithmetic blocks of the same length, and multiplication by $4$
permutes the residue classes modulo every odd prime power.  Their
$p^a$-divisibility counts can therefore differ by at most one; the
product of all possible deficits is at most the largest power of $p$
not exceeding $k-1$, and hence divides
$\operatorname{lcm}(1,\ldots,k-1)$.  The explicit values
$Q(1)^{j-1}=2^{j-1}$, together with the remaining powers of $4$, are
absorbed by the displayed extra $2^kD_k$.

On the balanced ray (26), Stirling's formula applied to (4), uniformly for
$n\leq m\leq2n$, and the elementary lcm bound show that the primitive
coefficient height is



$$
\exp(O(n)).                                             \tag{32}
$$



The finite calculation suggests the sharper exact denominator of the
$a=c$ coordinate



$$
2^{\,5j+2+v_2((3j+1)!)};                              \tag{33}
$$



it is verified for $0\leq j\leq40$ by the certificate.  Since an
all-$j$ proof of the last residual valuation has not been included,
(33) is diagnostic and is not used in the no-go theorem below.

## 6. Asymptotics and a primitive-matching no-go on the balanced ray

For (26), write



$$
F(x)=\frac{x(1-x)}{(1+x^4)^{3/4}},\qquad
 g(x)=(1+x^4)^{-1/2}.                                   \tag{34}
$$



Then $J_{n,k}=\int_0^1g(x)F(x)^n\,dx$.  There is one maximum in
$(0,1)$, at $x=x_0$, where



$$
x_0+x_0^{-1}=\frac{3+\sqrt5}{2},                       \tag{35}
$$



or equivalently



$$
x_0^4-3x_0^3+3x_0^2-3x_0+1=0.                         \tag{36}
$$



Put $\rho=F(x_0)$.  Laplace's method gives the exact leading form



$$
J_{n,(3n+2)/4}
 \sim
 \frac{g(x_0)\sqrt{2\pi}}{
       \sqrt{n\,| (\log F)''(x_0)|}}
 \rho^n,                                                \tag{37}
$$



where numerically



$$
x_0=0.464312613208127\ldots .                           \tag{38}
$$



Only the exponential nature of (37) is needed below.

Let



$$
E_n=q_ne-p_n=\frac1{n!}\int_0^1P_n(x)e^x\,dx>0         \tag{39}
$$



for even $n$.  The pair $(p_n,q_n)$ is primitive and



$$
q_n\geq\frac{n(2n-1)!}{n!}.                            \tag{40}
$$



The $\pi$-coefficient on this ray is nonzero.  One quick proof is to
integrate the rational differential over the whole real axis.  Its even
part is strictly positive, while its reduced integral is
$\pi(a_{n,k}+c_{n,k})/\sqrt2$; hence
$a_{n,k}+c_{n,k}>0$.  If the coefficient in (16) vanished, rational
independence of $1$ and $\sqrt2$ would force both
$a_{n,k}+c_{n,k}=0$ and $b_{n,k}=0$, a contradiction.

Primitive-normalize (16) over $\mathbb Z[\sqrt2]$, choosing its real
sign so that its value $\Lambda_n=A_n+B_n\pi$ is positive.  Equations
(31)--(32), and the
same bounds after division by algebraic content, give constants
$C_1,C_2>0$ such that



$$
H(A_n,B_n)\leq e^{C_1n},\qquad
 \Lambda_n\geq e^{-C_2n}.                               \tag{41}
$$



The minimally coefficient-matched form is



$$
\Phi_n=B_nE_n+q_n\Lambda_n.                            \tag{42}
$$



Let $\mathfrak g_n$ be its entire final coefficient-content ideal.  A
local valuation argument using $(A_n,B_n)=1$ and $(p_n,q_n)=1$ gives



$$
\mathfrak g_n\mid(B_n)^2.                              \tag{43}
$$



Indeed, away from primes dividing $q_n$ the two matched coefficients
cannot both vanish; at a prime dividing $q_n$, primitivity forces the
content valuation to be at most twice the valuation of $B_n$.  Therefore



$$
N\mathfrak g_n\leq |N(B_n)|^2=e^{O(n)}.                \tag{44}
$$



Choose the generator of the content ideal balanced by a power of the
fundamental unit, so that both real embeddings are within a fixed factor of
the square root of its norm.  This is the standard height-normalized meaning
of full primitive reduction in a real quadratic field.  Finally,



$$
0<E_n\leq\frac{e}{4^n n!}.                              \tag{45}
$$



Thus the first summand in (42) is superfactorially smaller than the second,
irrespective of its sign.  Equations (40)--(45) prove



$$
\left|\frac{\Phi_n}{\mathfrak g_n}\right|
 \longrightarrow+\infty.                               \tag{46}
$$



in the chosen real embedding.  Thus the balanced quartic ray fails after
full primitive normalization, not merely before content removal.

## 7. The critical scale and the neighboring-power escape

If $k\sim c n\log n$, $c>0$, the positive integral itself has saddle
point $x\sim(4c\log n)^{-1/4}$, and



$$
\log J_{n,k}
 =-\frac n4\log\log n
  -\frac n4\bigl(\log(4c)+1\bigr)+o(n).                 \tag{47}
$$



The exact coordinate denominator (30), however, has



$$
\log D_k=(3\log2+o(1))k.                               \tag{48}
$$



Thus the quartic family reaches factorial coefficient scale through its
dyadic arithmetic even though the raw integral has only the
$(\log n)^{-n/4}$ decay in (47).

For every $k>n/2$, let



$$
L_{n,k}=a_{n,k}-c_{n,k}.                               \tag{49}
$$



Whether or not either individual integral is log-free, the determinant



$$
\mathcal K_{n,k}
 =L_{n,k+1}J_{n,k}-L_{n,k}J_{n,k+1}                    \tag{50}
$$



has no logarithm.  Its $\pi$-coordinate is



$$
\frac18\left[
 L_{n,k+1}b_{n,k}-L_{n,k}b_{n,k+1}
 +\sqrt2\bigl(
 L_{n,k+1}(a_{n,k}+c_{n,k})
 -L_{n,k}(a_{n,k+1}+c_{n,k+1})
 \bigr)\right].                                        \tag{51}
$$



The square-root part in (51) is twice the adjacent determinant



$$
a_{n,k+1}c_{n,k}-c_{n,k+1}a_{n,k}.                    \tag{52}
$$



The companion certificate finds (52) nonzero for every even
$2\leq n\leq160$ and
$\lfloor n/2\rfloor+1\leq k\leq160$.  It also records a striking stable
dyadic valuation for the integer-scaled determinant.  These facts show
that the neighboring-power cancellation normally retains a genuine
$\pi$-coordinate and essentially both copies of (30).

But (50) is sign-indefinite: its integrand is proportional to



$$
\frac{P_n(x)}{Q(x)^{k+1}}
 \bigl(L_{n,k+1}Q(x)-L_{n,k}\bigr),                     \tag{53}
$$



and the last factor can vanish inside $[0,1]$.  Therefore the positivity
argument used in Section 6 does not apply.  Neither (47) nor the exact
denominator by itself supplies a lower bound after this cancellation.
The two-power construction is consequently not certified to beat the
quadratic critical-Fourier construction, but it is also not ruled out by
the present analysis.

## 8. Reproducible certificate

Run

    python -m py_compile scripts/quartic_power_kernel_hermite_certificate.py
    python scripts/quartic_power_kernel_hermite_certificate.py

For a byte-identical rerun, use

    python scripts/quartic_power_kernel_hermite_certificate.py \
      --output /tmp/quartic_power_kernel_hermite_certificate.json
    cmp results/quartic_power_kernel_hermite_certificate.json \
      /tmp/quartic_power_kernel_hermite_certificate.json

The script verifies the differential identity symbolically, reconstructs
the exact Hermite coordinates in two independent ways at small parameters,
performs the stated all-pair scan, tests (29), verifies (33) through
$j=40$, and audits the neighboring determinant and its observed dyadic
pattern.  The finite scans are diagnostics; only the identities proved in
the text are used as all-parameter theorems.
