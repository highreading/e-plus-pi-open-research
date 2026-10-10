> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Diagonal Padé forms for the nested-exponential consequence

Checked: 2026-08-26 UTC

## Scope

Assume temporarily that



$$
s=e+\pi\in\overline{\mathbb Q}.
$$



Then Euler's identity gives



$$
e^{ie}=-e^{is}.                                             \tag{1}
$$



The research log previously approximated the left side of (1) by its Taylor
polynomial.  Multiplying that Taylor form by the common denominator makes its
upper bound grow.  This note tests the substantially sharper diagonal Padé
approximants to the exponential.  They do produce Gaussian-integer
coefficient linear forms that are provably nonzero under the algebraicity
hypothesis and tend to zero.  They still do **not** give a contradiction:
their values are not nonzero algebraic integers, and qualitative
Lindemann--Weierstrass supplies no discrete lower bound for a varying family
with a growing number of exponential terms.

Nothing in this note proves or assumes the desired conclusion.

## 1. An integral Padé identity with integral coefficients

For $n\geq0$, define



$$
P_n(z)=\sum_{k=0}^n
 \frac{(2n-k)!}{k!(n-k)!}z^k,
 \qquad Q_n(z)=P_n(-z).                                    \tag{2}
$$



Both polynomials lie in $\mathbb Z[z]$, and the following identity is
exact:



$$
Q_n(z)e^z-P_n(z)
 =\frac{(-1)^nz^{2n+1}}{n!}
   \int_0^1t^n(1-t)^ne^{tz}\,dt.                           \tag{3}
$$



One direct verification is to expand the integral.  Its right side is



$$
(-1)^n\sum_{r=0}^{\infty}
 \frac{(n+r)!}{r!(2n+r+1)!}z^{2n+r+1}.                     \tag{4}
$$



On the left, multiplication of $Q_n$ by the exponential and the elementary
finite-difference identity



$$
\sum_{k=0}^n(-1)^k
 \frac{(2n-k)!}{k!(n-k)!(m-k)!}
 =\begin{cases}
 0,&n<m\leq2n,\\[3pt]
 \displaystyle
 (-1)^n\frac{(m-n-1)!}{(m-2n-1)!m!},&m\geq2n+1
 \end{cases}                                               \tag{5}
$$



gives exactly (4); the coefficients through degree $n$ are canceled by
$P_n$.  For completeness, after multiplication by $m!/n!$, the sum in
(5) is



$$
\sum_{k=0}^n(-1)^k\binom{m}{k}\binom{2n-k}{n-k}.
$$



It is the coefficient of $x^n$ in



$$
(1+x)^{2n}\sum_{k=0}^m\binom{m}{k}
 \left(\frac{-x}{1+x}\right)^k=(1+x)^{2n-m};
$$



terms with $k>n$ cannot contribute to that coefficient.  Hence the sum is
$\binom{2n-m}{n}=(-1)^n\binom{m-n-1}{n}$, which is zero for
$n<m\leq2n$ and simplifies to the second line of (5) for
$m\geq2n+1$.  This proves (3) without an asymptotic or numerical step.

For example, $P_1(z)=2+z$, $Q_1(z)=2-z$, and the first term of
$Q_1e^z-P_1$ is $-z^3/6$, in agreement with (3).

## 2. The conditional small nonzero forms

Evaluate (3) at $z=ie$ and put



$$
\Lambda_n=Q_n(ie)e^{ie}-P_n(ie).                            \tag{6}
$$



Since $|e^{iet}|=1$ for real $t$, the beta integral gives



$$
|\Lambda_n|
 \leq \frac{e^{2n+1}}{n!}\int_0^1t^n(1-t)^n\,dt
 =\frac{e^{2n+1}n!}{(2n+1)!}.                               \tag{7}
$$



The ratio of consecutive upper bounds is



$$
\frac{e^2(n+1)}{(2n+3)(2n+2)}\longrightarrow0,             \tag{8}
$$



so $\Lambda_n\to0$.

There is no hidden cancellation in this estimate.  The beta weight is
symmetric about $1/2$, so



$$
\left|\int_0^1t^n(1-t)^ne^{iet}\,dt\right|
 =\int_0^1t^n(1-t)^n
   \cos\!\left(e\left(t-\tfrac12\right)\right)dt.
$$



Indeed, after extracting $e^{ie/2}$, the sine part cancels under
$t\mapsto1-t$.  Elementary bounds $e<3<\pi$ give
$0\leq e|t-1/2|<\pi/2$, and hence



$$
\cos(e/2)\frac{(n!)^2}{(2n+1)!}
 \leq
 \left|\int_0^1t^n(1-t)^ne^{iet}\,dt\right|
 \leq\frac{(n!)^2}{(2n+1)!}.                         \tag{8a}
$$



Thus $\Lambda_n\neq0$ even without the algebraicity hypothesis, and its
magnitude is within the fixed positive factor $\cos(e/2)$ of the upper
bound (7).

Under the temporary hypothesis $s\in\overline{\mathbb Q}$, equation (1)
rewrites (6) as



$$
\Lambda_n=-Q_n(ie)e^{is}-P_n(ie).                           \tag{9}
$$



After expanding the two polynomials, this is an algebraic linear combination
of the exponentials with exponents



$$
0,1,\ldots,n,qquad is,1+is,\ldots,n+is.                    \tag{10}
$$



All exponents in (10) are distinct algebraic numbers: $s$ is real and
positive, so no number in the second row is real.  The coefficients are
Gaussian integers and are not all zero.  The Lindemann--Weierstrass theorem
therefore gives an independent conditional proof that



$$
\Lambda_n\neq0                       \tag{11}
$$



for every $n$.  Thus algebraicity of $e+\pi$ would place the already
nonzero Padé remainders into the rigorous conditional sequence



$$
0<|\Lambda_n|\leq
             \frac{e^{2n+1}n!}{(2n+1)!}\longrightarrow0.     \tag{12}
$$



This is stronger than the Taylor construction in the sense that no rational
denominator remains to be cleared.

## 3. Why smallness is not an arithmetic contradiction

Define the Gaussian-integer polynomial



$$
F_n(X,Y)=-Q_n(iX)Y-P_n(iX).                                  \tag{13}
$$



Then $F_n(e,e^{is})=\Lambda_n$, its degree in $X$ is $n$, and its
degree in $Y$ is one.  The coefficients in (2) decrease in absolute value
with $k$, so its height is exactly



$$
H_n=\frac{(2n)!}{n!}.                                       \tag{14}
$$



Stirling's formula gives



$$
\log H_n=n\log n+(2\log2-1)n+O(\log n),                     \tag{15}
$$



whereas the logarithm of the upper bound in (7) is



$$
-n\log n+(3-2\log2)n+O(\log n).                             \tag{16}
$$



The two-sided estimate (8a) shows that the height exponent is exactly one:



$$
\lim_{n\to\infty}
 \frac{-\log|\Lambda_n|}{\log H_n}=1.                       \tag{17}
$$



Indeed, the product of the coefficient height and either side of the
two-sided estimate is $\exp(2n+O(\log n))$, not a quantity tending to zero.

More importantly, (9) is not a rational integer or a nonzero algebraic
number.  Under the same algebraicity hypothesis, $e=e^1$ and $e^{is}$
are themselves algebraically independent: any polynomial relation expands
into a forbidden algebraic linear relation among exponentials of distinct
algebraic numbers $m+nis$.  Algebraic independence proves only that
$F_n(e,e^{is})\neq0$; it does not impose $|F_n(e,e^{is})|\geq1$, or any
other height-free discreteness bound.  Varying small polynomial values at an
algebraically independent point are entirely compatible with the qualitative
theorem.

Accordingly, (12) cannot be inserted into the elementary integer-linear-form
criterion for irrationality of $e+\pi$.  Closing this route would require a
quantitative algebraic-independence measure for the specific pair
$(e,e^{is})$ that beats the simultaneous growth in (15), the degree $n$,
and the $2n+2$ exponentials in (10).  No such estimate is established in
this note.

## Conclusion

Diagonal Padé approximation repairs the denominator-growth defect of the
naive Taylor near-relation and yields an exact family of small nonzero forms
under the algebraicity hypothesis.  It does not repair the decisive
arithmetic defect: the forms take values in a transcendental field and have
no discrete nonzero lower bound.  The construction is therefore a sharper
research reduction, not a proof that $e+\pi$ is algebraic or
transcendental.
