> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Varying powers of $1+x^2$: coordinates and a matching barrier

Date: 2026-08-26

## 1. Result and a correction to the premise

For positive integers $n,k$, put



$$
J_{n,k}=
 \int_0^1
 \frac{x^n(1-x)^n}{(1+x^2)^k}\,dx.             \tag{1}
$$



These moments do **not** always lie in
$\mathbb Q+\mathbb Q\pi$.  In general,



$$
J_{n,k}\in
 \mathbb Q+\mathbb Q\log2+\mathbb Q\pi.         \tag{2}
$$



For example,



$$
\frac{x^2(1-x)^2}{1+x^2}
 =x^2-2x+\frac{2x}{1+x^2},
$$



and hence



$$
J_{2,1}=\log2-\frac23.                         \tag{3}
$$



The following theorem settles every legitimate $\pi$-form in this
family below the $n\log n$ denominator-growth scale.

**Theorem.**  Let $n$ run through an infinite set of positive even
integers, and let $k=k_n\geq1$.  Suppose that the $\log2$-coordinate of
$J_{n,k}$ vanishes and its $\pi$-coordinate is nonzero.  If



$$
k_n=o(n\log n),                                \tag{4}
$$



then the absolute values of the fully primitive, minimally
coefficient-matched $e+\pi$ forms tend to infinity.

In particular, no finite slope



$$
\frac{k_n}{n}\longrightarrow\alpha<\infty      \tag{5}
$$



can escape whenever the moment is actually a nontrivial rational
$\pi$-form.  If $\alpha>1$, the log-free and nonzero-$\pi$
hypotheses hold automatically for all sufficiently large $n$, and the
$\pi$-coordinate is positive.  For slopes at most $1$, a logarithmic
coordinate generally occurs; every exceptional log-free index is still
covered by the theorem.

The proof gives the quantitative primitive-coefficient bound



$$
B_{n,k}\leq\exp(C(n+k)),                        \tag{6}
$$



where $B_{n,k}$ is the magnitude of the $\pi$-coefficient in the
primitive integer normalization and $C$ is absolute.  The final matched
form satisfies, for all sufficiently large relevant indices,



$$
|\Lambda_{n,k}^{\rm prim}|
 \geq\frac{c_\pi}{2}\frac{q_n}{B_{n,k}^9}.      \tag{7}
$$



Here $q_n\geq n^n$ is the primitive $e$-coefficient and
$c_\pi>0$ is fixed.

This is a family-specific obstruction, not an arithmetic result about
$e+\pi$.

## 2. Exact Gaussian partial fractions

Set



$$
P_n(x)=x^n(1-x)^n,\qquad
 F_{n,k}(x)=\frac{P_n(x)}{(1+x^2)^k}.
$$



Let $S_{n,k}(x)$ be the polynomial part of $F_{n,k}$ at infinity.  The
expansions



$$
P_n(x)=\sum_{h=0}^n(-1)^h\binom nhx^{n+h},
$$



and



$$
(1+x^2)^{-k}
 =x^{-2k}\sum_{r=0}^{\infty}
   (-1)^r\binom{k+r-1}{r}x^{-2r}
$$



give the exact formula



$$
S_{n,k}(x)=
 \sum_{\substack{0\leq h\leq n,\ r\geq0\\
                  n+h-2k-2r\geq0}}
 (-1)^{h+r}\binom nh\binom{k+r-1}{r}
 x^{n+h-2k-2r}.                                \tag{8}
$$



For $1\leq j\leq k$, define the Gaussian rational number



$$
a_{n,k,j}
 =
 [z^{\,k-j}]
 \frac{(i+z)^n(1-i-z)^n}{(2i+z)^k}.             \tag{9}
$$



This is exactly the coefficient of $(x-i)^{-j}$ in the Laurent
expansion at $i$.  Since $F_{n,k}$ has real rational coefficients, its
coefficient at the conjugate pole is the complex conjugate.  Therefore



$$
F_{n,k}(x)
 =
 S_{n,k}(x)
 +\sum_{j=1}^k
 \left(
  \frac{a_{n,k,j}}{(x-i)^j}
  +\frac{\overline{a_{n,k,j}}}{(x+i)^j}
 \right).                                      \tag{10}
$$



Write



$$
a_{n,k,1}=u_{n,k}+iv_{n,k},
\qquad u_{n,k},v_{n,k}\in\mathbb Q.             \tag{11}
$$



The simple-pole pair in (10) is



$$
\frac{2u_{n,k}x-2v_{n,k}}{1+x^2}.
$$



For $j\geq2$, integrate the two conjugate terms algebraically.  This
gives the exact coordinate formula



$$
J_{n,k}
 =R_{n,k}+u_{n,k}\log2-\frac{v_{n,k}}2\pi,      \tag{12}
$$



where



$$
\begin{aligned}
 R_{n,k}
 &=
 \int_0^1S_{n,k}(x)\,dx\\
 &\quad+
 \sum_{j=2}^k
 2\operatorname{Re}\left[
 a_{n,k,j}
 \frac{(1-i)^{1-j}-(-i)^{1-j}}{1-j}
 \right]\in\mathbb Q.                           \tag{13}
 \end{aligned}
$$



Equations (8)--(13) are finite exact formulas for all three coordinates.
Baker's theorem on linear forms in logarithms implies that



$$
1,\quad\log2,\quad\pi
$$



are linearly independent over $\mathbb Q$.  Indeed,
$\log2$ and $i\pi=\log(-1)$ are linearly independent over
$\mathbb Q$.  Baker's theorem makes them linearly independent over the
algebraic numbers and makes every nonzero algebraic linear form in them
transcendental.  A rational relation
$A+B\log2+C\pi=0$ would make such a form equal to the algebraic number
$-A$, forcing $B=C=0$, and then $A=0$.

Consequently,



$$
J_{n,k}\in\mathbb Q+\mathbb Q\pi
 \quad\Longleftrightarrow\quad
 u_{n,k}=0,                                     \tag{14}
$$



and the $\pi$-coordinate is nonzero exactly when
$v_{n,k}\ne0$.

The simple-pole residue can also be written directly as



$$
a_{n,k,1}
 =
 \operatorname*{Res}_{x=i}
 \frac{x^n(1-x)^n}{(1+x^2)^k}.                  \tag{15}
$$



Thus (14) is an exact, effectively checkable classification criterion
even when no simple congruence description is available.

References for this step: A. Baker, “Linear forms in the logarithms of
algebraic numbers,” Mathematika 13 (1966), 204–216,
[DOI 10.1112/S0025579300003971](https://doi.org/10.1112/S0025579300003971),
for algebraic-coefficient linear independence; and A. Baker, “Linear forms
in the logarithms of algebraic numbers (III),” Mathematika 14 (1967),
220–228,
[DOI 10.1112/S0025579300003843](https://doi.org/10.1112/S0025579300003843),
for the transcendence of a nonzero such form used to exclude a nonzero
algebraic constant term.

## 3. Simultaneous coordinate height

### Lemma 3.1

There is an absolute constant $C>0$ such that the three rational
coordinates in (12) can be put on one positive integer denominator
$D_{n,k}$ satisfying



$$
D_{n,k}\leq\exp(C(n+k)),
$$



with



$$
|D_{n,k}R_{n,k}|,
 \quad |D_{n,k}u_{n,k}|,
 \quad |D_{n,k}v_{n,k}|
 \leq\exp(C(n+k)).                              \tag{16}
$$



### Proof

The numerator of the local expression in (9) has coefficient
$\ell^1$-norm at most



$$
2^n(1+\sqrt2)^n.
$$



Also



$$
(2i+z)^{-k}
 =(2i)^{-k}
 \sum_{s=0}^{\infty}
 (-1)^s\binom{k+s-1}{s}
 \left(\frac{z}{2i}\right)^s.                  \tag{17}
$$



Only $s\leq k-1$ is needed in (9).  It follows that



$$
2^{2k}a_{n,k,j}\in\mathbb Z[i]
$$



for every $j$, and the real and imaginary parts of these Gaussian
integers have absolute value at most $\exp(C_1(n+k))$.

The polynomial in (8) has integer coefficients.  Whenever a term occurs,
$r\leq n-k$, and all its binomial factors and coefficient sums are
bounded by $\exp(C_2n)$.  Integrating it introduces only a divisor of



$$
\operatorname{lcm}(1,2,\ldots,2n+1).
$$



For the terms in (13), division by $j-1$ introduces a divisor of
$\operatorname{lcm}(1,\ldots,k-1)$.  Moreover,



$$
(1-i)^{1-j}
 =\frac{(1+i)^{j-1}}{2^{j-1}},
$$



while $(-i)^{1-j}$ is a Gaussian unit.  Thus all remaining endpoint
denominators are powers of $2$ of size $\exp(O(k))$.

The elementary estimate



$$
\operatorname{lcm}(1,2,\ldots,m)\leq16^m
$$



now gives a common denominator and numerator bounds of the form (16).
$\square$

### Corollary 3.2

Suppose $u_{n,k}=0$ and $v_{n,k}\ne0$.  Primitive-normalize (12) as



$$
L_{n,k}=A_{n,k}+\varepsilon_{n,k}B_{n,k}\pi
 =\mu_{n,k}J_{n,k},
$$



where $B_{n,k},\mu_{n,k}>0$ and
$\gcd(A_{n,k},B_{n,k})=1$.  Then



$$
B_{n,k}\leq\exp(C_3(n+k)).                     \tag{18}
$$



Indeed, clearing the rational coordinates in (12) by the common
denominator from Lemma 3.1 produces an integer pair of exponential size,
and primitive reduction can only decrease the $\pi$-coefficient.

## 4. The automatically log-free region $k>n$

The substitution $x=\tan t$ transforms (1) into



$$
J_{n,k}
 =
 \int_0^{\pi/4}
 \sin^nt\,(\cos t-\sin t)^n
 \cos^{\,2(k-n-1)}t\,dt.                       \tag{19}
$$



If $n$ is even and $k>n$, the integrand in (19) is a nonnegative
trigonometric polynomial of even total degree $2k-2$.  Its Fourier
frequencies are even, its Fourier coefficients are rational, and all
nonconstant terms have rational integrals from $0$ to $\pi/4$.
Therefore



$$
J_{n,k}=r_{n,k}+\frac{A_{n,k}^{(0)}}4\pi,
\qquad r_{n,k}\in\mathbb Q,                    \tag{20}
$$



where $A_{n,k}^{(0)}$ is its constant Fourier coefficient.

The integrand is nonnegative and not identically zero on a full period, so



$$
A_{n,k}^{(0)}>0.                               \tag{21}
$$



Thus every even pair $k>n$ is log-free and has a positive nonzero
$\pi$-coordinate.

For completeness, if $\ell=k-n-1$, the coefficient in (20) has the
finite extraction formula



$$
\begin{aligned}
 A_{n,k}^{(0)}
 &=
 2^{-(2k-2)}i^{-n}
 [z^{\,2k-2}]
 (z^2-1)^n\\
 &\qquad\cdot
 \bigl((1+i)z^2+1-i\bigr)^n
 (z^2+1)^{2\ell}.
                                                               \tag{22}
 \end{aligned}
$$



Although written in Gaussian notation, (22) is a positive rational
number by the Fourier interpretation.

## 5. Uniform Laplace asymptotics for finite slopes

Put



$$
a=\frac kn,\qquad
 f_a(x)=\log x+\log(1-x)-a\log(1+x^2).
$$



For $a\geq0$, the second derivative is



$$
f_a''(x)
 =
 -\frac1{x^2}
 -\frac1{(1-x)^2}
 -\frac{2a(1-x^2)}{(1+x^2)^2}<0
 \qquad(0<x<1).                                \tag{23}
$$



Hence $f_a$ has a unique maximizer $\xi(a)\in(0,1)$.  It is the unique
root in that interval of



$$
1-2x+(1-2a)x^2+2(a-1)x^3=0.                  \tag{24}
$$



For $a>0$, $\xi(a)<1/2$, while $\xi(0)=1/2$.  Define



$$
\Delta(a)=-f_a''(\xi(a))>0,\qquad
 \Phi(a)=
 \frac{\xi(a)(1-\xi(a))}
      {(1+\xi(a)^2)^a}.                         \tag{25}
$$



### Lemma 5.1

For each fixed $A<\infty$, uniformly for integers
$0\leq k\leq An$,



$$
J_{n,k}
 =
 \Phi(k/n)^n
 \sqrt{\frac{2\pi}{n\Delta(k/n)}}
 \left(1+O_A(n^{-1})\right).                   \tag{26}
$$



### Proof

Equation (1) is exactly



$$
J_{n,k}=\int_0^1\exp\!\left(nf_{k/n}(x)\right)\,dx.
$$



For $a\in[0,A]$, strict concavity gives one nondegenerate saddle, and
$\xi(a)$ remains in a compact subinterval of $(0,1)$.  The derivatives
of $f_a$ through the required order are uniformly bounded on a fixed
neighborhood of these saddles, while strict concavity supplies a uniform
exponential gap outside that neighborhood.  Taylor expansion at the
saddle and the Gaussian integral give (26), with a uniform
$O_A(n^{-1})$ relative remainder. $\square$

In particular, if $k_n/n\to\alpha<\infty$, then



$$
\frac1n\log J_{n,k_n}\longrightarrow\log\Phi(\alpha).         \tag{27}
$$



Thus all finite slopes have ordinary exponential analytic size.  The
factorial scale relevant to matching arises from the $e$-coefficient,
not from the Laplace integral.

## 6. Fully primitive matching

For even $n$, let



$$
E_n=\frac1{n!}\int_0^1x^n(1-x)^ne^x\,dx
 =q_ne-p_n>0
$$



be the primitive exponential form.  It satisfies



$$
\gcd(p_n,q_n)=1,\qquad
 q_n\geq n^n,\qquad
 \frac{E_n}{q_n}\leq e\,n^{-2n-1}.             \tag{28}
$$



Salikhov's finite irrationality measure for $\pi$, weakened to exponent
$8$, gives a fixed $c_\pi>0$ such that



$$
|A+\delta B\pi|\geq c_\pi B^{-7}              \tag{29}
$$



for all integers $A$, positive integers $B$, and
$\delta\in\{1,-1\}$.

At a log-free, nonzero-$\pi$ index, orient the primitive form by its
value:



$$
\widetilde L=sL=\widetilde A+\delta B\pi>0.
$$



Put



$$
d=\gcd(q_n,B),\qquad q_n=dq_0,\qquad B=dB_0.
$$



The minimal coefficient multipliers are $B_0,q_0$.  The matched constant
coefficient is



$$
-B_0p_n\mathbin{\pm}q_0\widetilde A.
$$



It is coprime to $q_0B_0$, so the final content $g$ satisfies



$$
g\mid d.                                       \tag{30}
$$



If $\delta=1$, the positive raw matched form is



$$
W^+=B_0E_n+q_0\widetilde L,
$$



and



$$
\left|\frac{W^+}{g}\right|
 \geq\frac{q_n|L|}{B^2}
 \geq c_\pi\frac{q_n}{B^9}.                    \tag{31}
$$



If $\delta=-1$, use



$$
W^-=B_0E_n-q_0\widetilde L
 =\frac{q_nB}{d}
  \left(\frac{E_n}{q_n}-\frac{|L|}{B}\right).
$$



The possible-cancellation ratio satisfies



$$
\frac{E_n/q_n}{|L|/B}
 \leq c_\pi^{-1}e\,B^8n^{-2n-1}.               \tag{32}
$$



By (18) and $k=o(n\log n)$, the logarithm of $B$ is
$o(n\log n)$, so (32) tends to zero.  For all sufficiently large
indices it is at most $1/2$, and the content bound gives



$$
\left|\frac{W^-}{g}\right|
 \geq\frac{q_n|L|}{2B^2}
 \geq\frac{c_\pi}{2}\frac{q_n}{B^9}.           \tag{33}
$$



Finally, (18), (28), (31), and (33) imply



$$
|\Lambda_{n,k}^{\rm prim}|
 \geq
 \exp\!\left(
 n\log n-O(n+k)
 \right)
 \longrightarrow\infty                         \tag{34}
$$



whenever $k=o(n\log n)$.  This proves the theorem.

In the automatic region $k>n$, equations (20)--(21) show that the
primitive form already has positive value and positive $\pi$-coefficient.
Only the same-sign form (31) occurs.

Reference for (29): V. Kh. Salikhov, “On the irrationality measure of
$\pi$,” Russian Mathematical Surveys 63:3 (2008), 570–572,
[DOI 10.1070/RM2008v063n03ABEH004543](https://doi.org/10.1070/RM2008v063n03ABEH004543).

## 7. What varying denominator growth costs

The denominator $(1+x^2)^k$ has degree $2k$, but its repeated poles
remain at the fixed separated points $\pm i$.  This special geometry
explains why its arithmetic cost is only $\exp(O(n+k))$:

1. local Laurent coefficients have only powers of $2$ in their
   denominators;
2. the pole-order antiderivatives divide by $1,\ldots,k-1$, whose common
   cost is their least common multiple, not $k!$;
3. endpoint evaluation adds only further powers of $2$;
4. the polynomial part has integral coefficients of exponential size.

Consequently every $k=O(n)$, and indeed every
$k=o(n\log n)$, remains below the factorial matching scale.  This
includes all finite slopes and all automatically log-free pairs $k>n$
with $k=o(n\log n)$.

At $k\asymp n\log n$, the bound (18) reaches
$\exp(O(n\log n))$, so the present argument no longer forces
divergence.  This is only a boundary of the proof, not evidence that such
orders succeed.  Repeated quadratics at that scale, moving poles, or
denominators with more complicated arithmetic remain possible
direct-integral directions.
