> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the varying quadratic-power kernel barrier

Date: 2026-08-26

## Verdict

**ACCEPT.**  The Gaussian partial fractions, simultaneous coordinate-height
bound, Baker-theorem uniqueness step, automatically log-free region
$k>n$, uniform finite-slope Laplace estimate, and fully primitive matching
argument all rederive correctly.  The proof is pointwise and therefore
remains valid on an arbitrary sparse infinite set of positive even indices.

One source gap found during the audit was corrected before the final hash
was frozen.  The first version cited only Baker's 1966 Part I while invoking
the stronger theorem that a nonzero algebraic-coefficient linear form in
logarithms of algebraic numbers cannot itself be algebraic.  The final
source retains Part I for algebraic-coefficient linear independence and
adds Baker's 1967 Part III, where the required transcendence statement is
explicit.

The accepted source is
`sources/varying_quadratic_power_kernel_barrier.md`, with SHA-256

`36e3809081c6e2052a31312ffece0edd16590d50558c7522545d45d282ce38e4`.

## 1. Exact Gaussian coordinates

Write

$$
F_{n,k}(x)=\frac{x^n(1-x)^n}{(1+x^2)^k}.
$$

At infinity,

$$
x^n(1-x)^n
=\sum_{h=0}^n(-1)^h\binom nhx^{n+h}
$$

and

$$
(1+x^2)^{-k}
=x^{-2k}\sum_{r\ge0}(-1)^r
  \binom{k+r-1}{r}x^{-2r}.
$$

Their nonnegative powers give exactly the polynomial part in (8).  Every
term has integer coefficient.  If such a term occurs, then
$2n-2k-2r\ge0$, so $r\le n-k$; this observation is also the key to the
uniform coefficient-height estimate below.

At $x=i+z$,

$$
F_{n,k}(i+z)
=z^{-k}\frac{(i+z)^n(1-i-z)^n}{(2i+z)^k}.
$$

Consequently the coefficient of $(x-i)^{-j}$ is precisely

$$
a_{n,k,j}
=[z^{k-j}]
\frac{(i+z)^n(1-i-z)^n}{(2i+z)^k}.
$$

The conjugate-pole coefficient is its complex conjugate because the
original rational function has real coefficients.  Subtracting all the
principal parts leaves an entire rational function with polynomial growth,
hence the polynomial part at infinity.  This proves the full decomposition
(10), including all Laurent indices.

If $a_{n,k,1}=u+iv$, then

$$
\frac{a_{n,k,1}}{x-i}
+\frac{\overline{a_{n,k,1}}}{x+i}
=\frac{2ux-2v}{1+x^2}.
$$

Its integral on $[0,1]$ is

$$
u\log2-\frac v2\pi.
$$

For $j\ge2$, direct antiderivation gives

$$
2\operatorname{Re}\left[
a_{n,k,j}
\frac{(1-i)^{1-j}-(-i)^{1-j}}{1-j}
\right].
$$

All quantities inside the real part belong to $\mathbb Q(i)$, so these
higher-pole contributions are rational.  Integrating the integer
polynomial part is rational as well.  Thus

$$
J_{n,k}=R_{n,k}+u_{n,k}\log2-\frac{v_{n,k}}2\pi
$$

with exactly the signs claimed in the source.  In particular, the residue
$a_{n,k,1}$ is an exact finite criterion for the logarithmic and
$\pi$-coordinates.  The example
$J_{2,1}=\log2-2/3$ follows from ordinary polynomial division and is
correct.

## 2. Baker's theorem and coordinate uniqueness

Choose

$$
\lambda_1=\log2,
\qquad
\lambda_2=i\pi=\log(-1).
$$

They are linearly independent over $\mathbb Q$ because the first is a
nonzero real number and the second a nonzero purely imaginary number.
Baker Part I upgrades the relevant logarithmic independence to algebraic
coefficients.  Baker Part III states that a nonzero algebraic-coefficient
linear form in logarithms of algebraic numbers is transcendental and hence
cannot equal a nonzero algebraic constant.

Indeed, a rational relation

$$
A+B\log2+C\pi=0
$$

can be rewritten as

$$
B\lambda_1-iC\lambda_2=-A.
$$

If $(B,C)\ne(0,0)$, the left side is a nonzero algebraic-coefficient
logarithmic form and is transcendental, while the right side is algebraic.
This is impossible.  Thus $B=C=0$, followed by $A=0$.  Therefore
$1,\log2,\pi$ are rationally independent, so the three rational
coordinates in the displayed decomposition are unique.  It follows
exactly that

$$
J_{n,k}\in\mathbb Q+\mathbb Q\pi
\quad\Longleftrightarrow\quad u_{n,k}=0,
$$

and that the remaining $\pi$-coordinate is nonzero precisely when
$v_{n,k}\ne0$.

This step genuinely needs the theorem excluding a nonzero algebraic
constant, not merely nonvanishing of a logarithmic form; the final source's
two references now distinguish those roles correctly.

## 3. Simultaneous coordinate height

The numerator in the local expansion has coefficient $\ell^1$ norm at
most

$$
\|(i+z)^n\|_1\,\|(1-i-z)^n\|_1
\le2^n(1+\sqrt2)^n.
$$

Also,

$$
(2i+z)^{-k}
=(2i)^{-k}\sum_{s\ge0}(-1)^s
\binom{k+s-1}{s}\frac{z^s}{(2i)^s}.
$$

To compute any $a_{n,k,j}$ one needs only $s\le k-j\le k-1$.
Every denominator therefore divides a Gaussian unit times
$2^{k+s}$ with $k+s\le2k-1$.  Hence

$$
2^{2k}a_{n,k,j}\in\mathbb Z[i].
$$

The numerator norm, the binomial coefficients with $s<k$, and the number
of contributing convolutions are all bounded by $\exp(C(n+k))$.  This
proves both the denominator assertion and the real/imaginary numerator
bounds for all local coefficients.

The polynomial part has integer coefficients.  Since a contributing
$r$ satisfies $r\le n-k$, it exists only when $k\le n$, and then
$k+r-1\le n-1$.  Both binomial factors and the total number of summands
are therefore $\exp(O(n))$.  Integrating a monomial introduces a divisor
at most $2n+1$, and a common denominator is
$\operatorname{lcm}(1,\ldots,2n+1)$.

For the higher-pole terms, division by $j-1$ costs only
$\operatorname{lcm}(1,\ldots,k-1)$, while

$$
(1-i)^{1-j}=\frac{(1+i)^{j-1}}{2^{j-1}}
$$

and $(-i)^{1-j}$ is a unit.  Thus endpoint evaluation adds powers of two
of size $\exp(O(k))$ and no uncontrolled odd denominator.  The elementary
bound

$$
\operatorname{lcm}(1,\ldots,m)\le16^m
$$

then gives one denominator $D_{n,k}$ and all three numerator bounds of
size $\exp(C(n+k))$.  When $k=1$, the higher-pole sum and its LCM are empty
and are interpreted with denominator one, so no edge case is lost.

At a log-free index,

$$
J_{n,k}=R_{n,k}-\frac{v_{n,k}}2\pi.
$$

Multiplication by $2D_{n,k}$ gives the integer pair

$$
(2D_{n,k}R_{n,k},-D_{n,k}v_{n,k}).
$$

If $v_{n,k}\ne0$, primitive reduction can only decrease the magnitude of
its second coordinate.  This proves

$$
B_{n,k}\le\exp(C(n+k))
$$

without any hidden rational-coordinate denominator.

## 4. The automatic region $k>n$

The change of variables $x=\tan t$ gives exactly

$$
J_{n,k}=\int_0^{\pi/4}
\sin^nt\,(\cos t-\sin t)^n
\cos^{2(k-n-1)}t\,dt.
$$

If $n$ is even and $k>n$, every exponent is a nonnegative even integer.
The integrand is therefore a nonnegative, nonzero trigonometric polynomial
on every full period.  Its total homogeneous degree in $\sin t,\cos t$ is
$2k-2$, which is even.

With $z=e^{it}$, a rational homogeneous polynomial of even degree has only
even Fourier frequencies.  Its Laurent coefficients lie in $\mathbb Q(i)$;
pairing conjugate frequencies gives rational coefficients of
$\cos(2rt)$ and $\sin(2rt)$.  For $r\ne0$,

$$
\int_0^{\pi/4}\cos(2rt)\,dt
=\frac{\sin(r\pi/2)}{2r}\in\mathbb Q,
$$

and

$$
\int_0^{\pi/4}\sin(2rt)\,dt
=\frac{1-\cos(r\pi/2)}{2r}\in\mathbb Q.
$$

Only the constant Fourier coefficient contributes a multiple of $\pi$.
If it is denoted $A_{n,k}^{(0)}$, then

$$
J_{n,k}=r_{n,k}+\frac{A_{n,k}^{(0)}}4\pi,
\qquad r_{n,k}\in\mathbb Q.
$$

The constant coefficient is the full-period average of a nonnegative,
nonzero function, so it is strictly positive.  This proves both automatic
log-freeness and the positive nonzero $\pi$-coordinate, with no appeal to
observed cancellations.

For the extraction formula, use

$$
\sin t=\frac{z^2-1}{2iz},\quad
\cos t-\sin t=
\frac{(1+i)z^2+1-i}{2z},\quad
\cos t=\frac{z^2+1}{2z}.
$$

The total denominator is
$2^{2k-2}i^nz^{2k-2}$.  The constant Laurent term is consequently the
coefficient of $z^{2k-2}$ in the numerator, proving every power and index
in (22).  Since $n$ is even, $i^{-n}=\pm1$; the Fourier interpretation
proves that the displayed Gaussian extraction is in fact a positive
rational number.

## 5. Uniform finite-slope Laplace estimate

For $a=k/n$, write

$$
f_a(x)=\log x+\log(1-x)-a\log(1+x^2).
$$

Direct differentiation gives

$$
f_a''(x)
=-\frac1{x^2}-\frac1{(1-x)^2}
-\frac{2a(1-x^2)}{(1+x^2)^2}<0
$$

on $0<x<1$.  Since $f_a$ tends to $-\infty$ at both endpoints, it has a
unique interior maximizer.  Clearing the positive denominator from
$f_a'(x)=0$ gives

$$
1-2x+(1-2a)x^2+2(a-1)x^3=0,
$$

so the saddle equation is correct.  At $a=0$ the root is $1/2$, and for
$a>0$ the derivative at $1/2$ is negative, so strict concavity places the
root to its left.

For $a\in[0,A]$, the root depends continuously on $a$ and stays in one
compact subinterval of $(0,1)$.  The negative second derivative is bounded
away from zero there, the required higher derivatives are uniformly
bounded, and compactness supplies a uniform gap outside a fixed saddle
neighborhood.  Taylor expansion and the Gaussian integral therefore give,
uniformly for all integers $0\le k\le An$,

$$
J_{n,k}
=\Phi(k/n)^n
\sqrt{\frac{2\pi}{n\Delta(k/n)}}
\left(1+O_A(n^{-1})\right).
$$

There is no omitted amplitude factor because the original integral is
exactly $\int_0^1e^{nf_{k/n}(x)}dx$.  Continuity of the saddle data then
proves
$n^{-1}\log J_{n,k_n}\to\log\Phi(\alpha)$ whenever
$k_n/n\to\alpha<\infty$.

## 6. Primitive matching and divergence

At a log-free nonzero-$\pi$ index, let
$L=A+\varepsilon B\pi$ be the primitive coordinate pair, with $B>0$.
The integral is strictly positive, but orienting by value also covers the
matching algebra without relying on that observation.  Let
$\widetilde L=\widetilde A+\delta B\pi=|L|$.

For the primitive exponential pair $q_ne-p_n$, put

$$
d=\gcd(q_n,B),\qquad q_n=dq_0,\qquad B=dB_0.
$$

The minimal target multipliers are $B_0,q_0$.  The matched constant is
$-B_0p_n\mathbin\pm q_0\widetilde A$.  A prime dividing $q_0$ cannot divide
this constant because it divides neither $B_0$ nor $p_n$; a prime dividing
$B_0$ cannot divide it because it divides neither $q_0$ nor
$\widetilde A$.  Therefore the final content satisfies the full
prime-power bound $g\mid d$.  If the matched constant is zero, these
congruences force $q_0=B_0=1$, and again $g=d$.

The uniform irrationality bound for $\pi$ gives

$$
|A+\delta B\pi|\ge c_\pi B^{-7}.
$$

In the same-sign case, positivity and $dg\le B^2$ yield

$$
\left|\frac{W^+}{g}\right|
\ge c_\pi\frac{q_n}{B^9}.
$$

In the opposite-sign case the possible-cancellation ratio is at most

$$
c_\pi^{-1}eB^8n^{-2n-1}.
$$

The coordinate-height bound and $k=o(n\log n)$ imply
$\log B=O(n+k)=o(n\log n)$, so this ratio tends to zero and is eventually
at most $1/2$.  Hence

$$
\left|\frac{W^-}{g}\right|
\ge\frac{c_\pi}{2}\frac{q_n}{B^9}.
$$

Finally, $q_n\ge n^n$ and $B\le\exp(C(n+k))$ give

$$
\log|\Lambda_{n,k}^{\mathrm{prim}}|
\ge n\log n-O(n+k)\longrightarrow+\infty.
$$

This remains true on any infinite index set because such a set is
unbounded.  In the automatic region $k>n$, both the value and the
$\pi$-coefficient are positive, so only the same-sign branch occurs.

## 7. Independent exact checks and file validation

The acceptance above rests on the symbolic arguments.  As separate guards
against Laurent-index and Fourier-sign mistakes, I also performed the
following exact finite checks with independently written Gaussian-rational
arithmetic.

* For every $1\le n,k\le12$, all local coefficients satisfied
  $2^{2k}a_{n,k,j}\in\mathbb Z[i]$.  At each of three rational evaluation
  points, the polynomial part plus every conjugate principal part
  reconstructed $F_{n,k}$ exactly, giving 432 exact reconstruction checks.
* For every even $2\le n\le40$ and
  $n+1\le k\le n+10$, the independent Fourier extraction was a positive
  rational number and agreed with the residue coordinates through
  $u_{n,k}=0$ and $A_{n,k}^{(0)}=-2v_{n,k}$.  All 200 cases passed.
* Independent symbolic differentiation reproduced both the cubic saddle
  equation and the displayed second derivative.

The final source is 14,108 bytes, strict UTF-8 and LF-only, with no
forbidden C0 controls or replacement characters.  It has 55 ordered
display pairs, 122 ordered inline pairs, and the complete sequential tag
list 1 through 34.  A Pandoc render check exits successfully.

The accepted theorem is a barrier for the specific family
$(1+x^2)^{-k}$ below the $n\log n$ growth scale.  It does not assert that
the critical scale succeeds, and it makes no unconditional arithmetic
claim about $e+\pi$.
