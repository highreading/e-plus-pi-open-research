> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A $p$-adic ${}_2F_0$ representation of the Bessel index zero and its truncation barrier

Checked: 2026-08-27 UTC.

## 1. Verdict

Let $f_p:\mathbb Z_p\to\mathbb Z_p$ be the canonical interpolation of



$$
f(n)=(-1)^nq_n,
\tag{1}
$$



constructed in

    sources/bessel_padic_index_interpolation_analytic_height_barrier.md

For every prime $p$, it has the uniformly convergent
parameter-hypergeometric representation



$$
\boxed{
 f_p(x)=\sum_{k=0}^{\infty}
 \frac{(-x)_k(x+1)_k}{k!}.}
\tag{2}
$$



Thus an ordinary Bessel index zero $\rho_{p,r}$ is exactly a zero of the
special $p$-adic parameter series



$$
{}_2F_0(-x,x+1;\,\,;1).
\tag{3}
$$



For comparison with the classical name, define the Bessel polynomial by



$$
y_n(z):={}_2F_0\left(-n,n+1;\,\,;-\frac z2\right)
 \qquad(n\in\mathbb Z_{\geq0}),
\tag{3a}
$$



where the series terminates.  Then



$$
f(n)=y_n(-2).
\tag{3b}
$$



Consequently (2) is a canonical $p$-adic continuation in the *degree*
of the fixed-argument Bessel-polynomial values $y_n(-2)$.  This is a
precise Bessel identification, but it is not a claim that (2) is a
previously defined argument-variable $p$-adic Bessel function.

Formula (2) is meant as the explicitly convergent series proved below.  It
is not an identification with a finite-field or Dwork
${}_nG_n(t)_p$, where parameters are fixed and the argument varies.

The $k$-th term has the uniform valuation bound



$$
\boxed{
 v_p\left(\frac{(-x)_k(x+1)_k}{k!}\right)
 \geq\Lambda_p(k):=v_p((2k)!)-v_p(k!)
 \quad(x\in\mathbb Z_p).}
\tag{4}
$$



Since $\Lambda_p(k)\to\infty$, this proves uniform convergence and gives
an exact tail estimate.

The representation does not presently yield the required
rational-integer approximation bound for $\rho_{p,r}$.  There is a
precise reason the direct truncation method stalls.  If
$n\equiv\rho_{p,r}\pmod {p^a}$, the factor $x-n$ first appears in the
hypergeometric term with $k=n+1$.  Every truncation with $k\leq n$
is blind, at the factor level, to the high valuation of $x-n$.  At the
first relevant threshold, the preceding exact integer sum is already



$$
\sum_{k=0}^{n}\frac{(-n)_k(n+1)_k}{k!}
 =f(n)=(-1)^nq_n,
\tag{5}
$$



whose logarithmic height is $n\log n+O(n)$.

A quantitative auxiliary-integer calculation makes the same barrier
explicit.  It is rigorous for the natural truncations (2); it is not a
claim that every possible new Padé construction must fail.  The functional
difference equation likewise produces transfer matrices whose direct
height already contains $q_n$.  Neither route proves



$$
v_p(n-\rho_{p,r})\log p=o(n\log n).
\tag{6}
$$



The exact survivor is therefore an arithmetic irrationality measure for
the parameter zero in (2), requiring an auxiliary construction that gains
more $p$-adic order per archimedean height than the raw truncations or
recurrence transfer.

## 2. Uniform convergence of the parameter ${}_2F_0$

For $x\in\mathbb Z_p$, write



$$
\begin{aligned}
 T_k(x)
 &:=\frac{(-x)_k(x+1)_k}{k!}\\
 &=\frac{(-1)^k}{k!}
   \prod_{h=-k+1}^{k}(x+h).
\end{aligned}
\tag{7}
$$



Fix $b\geq1$.  Among any $2k$ consecutive shifts $x+h$, at least
$\lfloor2k/p^b\rfloor$ are divisible by $p^b$: modulo $p^b$, the
condition $x+h\equiv0$ selects one residue class of $h$.  Summing over
$b$ gives



$$
v_p\left(\prod_{h=-k+1}^{k}(x+h)\right)
 \geq\sum_{b\geq1}\left\lfloor\frac{2k}{p^b}\right\rfloor
 =v_p((2k)!).
\tag{8}
$$



After division by $k!$, equation (8) is (4).  Moreover,



$$
\Lambda_p(k+1)-\Lambda_p(k)
 =v_p\bigl(2(2k+1)\bigr)\geq0,
\tag{9}
$$



so the bound is nondecreasing.  Legendre's formula gives



$$
\Lambda_p(k)=\frac{k}{p-1}+O(\log k)
\quad(p\text{ odd}),\qquad
 \Lambda_2(k)=k.
\tag{10}
$$



Consequently the series in (2) converges uniformly on $\mathbb Z_p$,
as a series of integer-valued polynomials.  Uniform convergence here is in
the supremum norm on $\mathbb Z_p$; it does not assert convergence in
the coefficient Gauss norm on the whole unit disk.  This distinction is
consistent with the exact local, but nonglobal, analyticity proved in the
companion note.

If $x=n\geq0$, then $(-n)_k=0$ for $k>n$, and for $k\leq n$



$$
T_k(n)=(-1)^k\frac{(n+k)!}{k!(n-k)!}.
\tag{11}
$$



The terminating sum is exactly the Bessel formula for
$(-1)^nq_n$.  Therefore (2) agrees with $f(n)$ on the nonnegative
integers.  Both sides are continuous, and those integers are dense in
$\mathbb Z_p$, proving (2).

For



$$
H_K(x)=\sum_{k=0}^{K}T_k(x),
\tag{12}
$$



the uniform tail estimate is



$$
\boxed{
 v_p(f_p(x)-H_K(x))\geq\Lambda_p(K+1)
 \quad(x\in\mathbb Z_p).}
\tag{13}
$$



### 2.1 Reflection symmetry and the quadratic index coordinate

The paired parameters in (2) give a further exact structure:



$$
\begin{aligned}
 T_k(x)
 &=\frac{(-1)^k}{k!}
   \prod_{j=0}^{k-1}(x-j)(x+j+1)\\
 &=\frac{(-1)^k}{k!}
   \prod_{j=0}^{k-1}\bigl(x(x+1)-j(j+1)\bigr).
\end{aligned}
\tag{Q1}
$$



In particular,



$$
\boxed{f_p(-x-1)=f_p(x).}
\tag{Q2}
$$



Thus (2) is a Newton series in the quadratic coordinate
$t=x(x+1)$, with interpolation nodes $j(j+1)$.  This statement is
made on the quadratic image of $\mathbb Z_p$; no convergence on every
unrelated $t\in\mathbb Z_p$ is being asserted.

There is also an exact consequence for ordinary roots.  If $p$ is odd
and an ordinary root lay in the residue class
$r=-1/2\pmod p$, its reflected root would lie in the same residue
class.  Uniqueness of the ordinary Hensel lift would force
$\rho=-\rho-1=-1/2$, while differentiating (Q2) there gives
$f_p'(-1/2)=0$, a contradiction.  For $p=2$, $2\rho+1$ is
automatically a unit.  Hence every ordinary root satisfies



$$
\boxed{2\rho_{p,r}+1\in\mathbb Z_p^\times.}
\tag{Q3}
$$



If $n\equiv\rho_{p,r}\pmod p$, it follows that



$$
\begin{aligned}
 v_p\bigl(n(n+1)-\rho_{p,r}(\rho_{p,r}+1)\bigr)
 &=v_p(n-\rho_{p,r})+v_p(n+\rho_{p,r}+1)\\
 &=v_p(n-\rho_{p,r}).
\end{aligned}
\tag{Q4}
$$



The quadratic Bessel coordinate therefore preserves, rather than
weakens, the exact digit-depth problem on every ordinary branch.

## 3. Natural auxiliary integers

Let $0\leq K\leq n$.  Every $T_k(n)$ is an integer, so
$H_K(n)\in\mathbb Z$.  The absolute values of successive terms obey



$$
\frac{|T_{k+1}(n)|}{|T_k(n)|}
 =\frac{(n-k)(n+k+1)}{k+1}\geq2
 \qquad(0\leq k<n).
\tag{14}
$$



The last inequality is minimized at $n=k+1$.  Hence the alternating
partial sum is nonzero, has the sign of its final term, and satisfies



$$
0<|H_K(n)|<2|T_K(n)|
 \leq2(n+K)^{2K}.
\tag{15}
$$



Now suppose $f_p(\rho)=0$ and



$$
a=v_p(n-\rho).
\tag{16}
$$



The numerator of $T_k(x)$ is an integral polynomial.  Therefore



$$
v_p(T_k(n)-T_k(\rho))
 \geq a-v_p(k!).
\tag{17}
$$



Summing through $K$ gives



$$
v_p(H_K(n)-H_K(\rho))
 \geq a-v_p(K!).
\tag{18}
$$



On the other hand, $f_p(\rho)=0$ and (13) give



$$
v_p(H_K(\rho))\geq\Lambda_p(K+1).
\tag{19}
$$



Combining (18) and (19),



$$
\boxed{
 v_p(H_K(n))
 \geq
 \min\{\Lambda_p(K+1),\,a-v_p(K!)\}.}
\tag{20}
$$



Although this subsection began with $K\leq n$ in order to obtain the
small-height bound (15), the valuation estimate (20) itself is valid for
every $K\geq0$: its proof used only (17)--(19).

Since $H_K(n)$ is a nonzero integer, the ordinary product estimate and
(15) give the fully explicit auxiliary inequality



$$
\boxed{
 \min\{\Lambda_p(K+1),\,a-v_p(K!)\}\log p
 \leq\log2+2K\log(n+K).}
\tag{21}
$$



Equation (21) is the direct estimate obtained from the uniform tail and
termwise polynomial-difference bounds for the raw hypergeometric
truncation.  No optimality among all estimates for the same partial sums
is asserted.

It does not bound a very large $a$.  Once



$$
a>v_p(K!)+\Lambda_p(K+1),
\tag{22}
$$



the left side of (21) is capped by $\Lambda_p(K+1)$, and further
increases in $a$ are invisible.  To remain in the $a$-dependent
alternative, it is necessary that



$$
\begin{aligned}
 a
 &\leq v_p(K!)+\Lambda_p(K+1)\\
 &=v_p((2K+2)!)-v_p(K+1)\\
 &\leq\frac{2K+2}{p-1}.
\end{aligned}
\tag{23}
$$



Thus, uniformly for odd $p$, one needs
$K\geq (p-1)a/2-1$.  The archimedean term in (21) is then already on
at least the $((p-1)a-2)\log n$ scale.  In the asymptotic range this
dominates the desired $a\log p$ left-hand scale instead of constraining
it.  Thus (21) cannot be rearranged into the required upper bound.  This
is a scale audit, not an assumption about cancellation.

For completeness, taking $K>n$ cannot evade the barrier.  Termination
at the integer argument gives



$$
H_K(n)=H_n(n)=(-1)^nq_n
 \qquad(K\geq n).
\tag{P1}
$$



Thus every truncation at or beyond the threshold already has the full
main-scale integer value.  Moreover, the amount of the depth $a$ that
the termwise estimate (20) can certify has an exact half-depth ceiling.
Put



$$
L_K=\Lambda_p(K+1),\qquad V_K=v_p(K!),\qquad
 D_K=L_K-V_K.
\tag{P2}
$$



Then



$$
D_K
 =v_p\left((K+1)\binom{2K+2}{K+1}\right)\geq0.
\tag{P3}
$$



For any real $a$, the elementary two-case comparison at
$V_K=(a-D_K)/2$ gives



$$
\min\{L_K,a-V_K\}
 \leq\frac{a+D_K}{2}.
\tag{P4}
$$



Kummer's carry interpretation of the valuation of a binomial coefficient,
together with $v_p(K+1)\leq\log_p(K+1)$, gives the convenient uniform
bound



$$
D_K\leq2\bigl(1+\log_p(K+1)\bigr).
\tag{P5}
$$



Consequently (20), using only the raw termwise tail and polynomial
difference estimates, certifies no more than



$$
\frac a2+1+\log_p(K+1)
\tag{P6}
$$



digits.  When $K\geq n$, the corresponding product estimate has
right side $\log q_n=n\log n+O(n)$ by (P1).  Even in the deep regime
where the logarithmic error in (P6) is negligible, this route would at
best return a factor-two main-scale estimate, weaker than the exact
identity $a\log p=v_p(q_n)\log p\leq\log q_n$ already known.  Equations
(P1)--(P6) are an all-truncation audit of these particular termwise
estimates, not an optimality theorem for other Padé combinations or for
possible cancellation inside $H_K$.

## 4. The exact visibility threshold

There is an even more concrete way to see why low truncations lose the
depth $a$.  In (7), the small factor $\rho-n$ occurs precisely when
the offset $h=-n$ lies in



$$
-k+1\leq h\leq k.
\tag{24}
$$



For $n\geq0$, this first happens at



$$
\boxed{k=n+1.}
\tag{25}
$$



Thus no individual term $T_k(\rho)$ with $k\leq n$ contains the
factor $\rho-n$.  All terms with $k\geq n+1$ do.  The truncation just
before this threshold is $H_n$, and its integer evaluation is exactly
(5).  Therefore the first raw hypergeometric auxiliary that sees the full
approximation depth also pays the full Bessel-denominator height.

This does not logically rule out a new linear combination that cancels
many terms while keeping small height.  It identifies the exact feature
such a Padé construction must overcome: it must import the
$\rho-n$ factor from the tail beginning at $k=n+1$ without inheriting
the $n\log n$ height of $H_n(n)=(-1)^nq_n$.

## 5. Difference equation and continued-fraction audit

The interpolation satisfies



$$
f_p(x+1)+(4x+2)f_p(x)-f_p(x-1)=0.
\tag{26}
$$



Direct propagation uses the transfer matrices



$$
\binom{f_p(x+j+1)}{f_p(x+j)}
 =
 \begin{pmatrix}
  -(4x+4j+2)&1\\
  1&0
 \end{pmatrix}
 \binom{f_p(x+j)}{f_p(x+j-1)}.
\tag{27}
$$



Each matrix has determinant $-1$.  Iterating from $x=0$ sends the
initial state $(f_p(1),f_p(0))=(-1,1)$ to states containing
$f_p(n)=(-1)^nq_n$.  Thus the direct transfer matrix already has an
integer evaluation of size



$$
\log q_n=n\log n+O(n).
\tag{28}
$$



Where the ratios are defined, (26) gives the formal continued-fraction
recursion



$$
\frac{f_p(x+1)}{f_p(x)}
 =-(4x+2)+
 \left(\frac{f_p(x)}{f_p(x-1)}\right)^{-1}.
\tag{29}
$$



At a zero $x=\rho$, this relation propagates the still-undetermined
nonzero value $f_p(\rho+1)=f_p(\rho-1)$; it does not close to an
algebraic equation for $\rho$.  Iterating (29) reproduces the same
transfer products and their main-scale height.

Accordingly, the functional equation gives an exact structural
description but no rational-integer approximation measure.  A successful
new method would need an additional arithmetic boundary condition or a
small-height Padé determinant not present in the raw transfer.

## 6. Applicability of standard $p$-adic hypergeometric methods

The series (2) differs from the common $p$-adic hypergeometric setting
in two important ways:

1. the variable $x$ appears in both upper parameters, $-x$ and
   $x+1$, rather than as the hypergeometric argument; and
2. the desired number is a zero in this parameter, not a special value at
   a known algebraic parameter.

The literature is broader than fixed-parameter theory, so the relevant
distinction must be stated carefully.  Dwork developed generalized
$p$-adic hypergeometric functions as analytic functions of the
hypergeometric argument while allowing $p$-integral parameters.
Koblitz and Diamond also studied continuity in $p$-adic parameters and
values or ratios at hypergeometric argument $1$.  In particular,
Diamond's paper explicitly treats ${}_2F_1(a,b;c;1)$, Dwork ratios,
and certain convergent ${}_3F_2(1)$ identities with $p$-adic
parameters.

Those results do not directly evaluate (2).  Here there is no lower
parameter: it is the irregular ${}_2F_0$ series at $1$, and its
convergence comes from the special correlated pair $(-x,x+1)$ and the
consecutive-factor estimate (8).  More importantly, the desired object
is a zero as the correlated parameter varies, whereas the cited formulas
give special values or ratios under their stated continuation,
digit, or distance hypotheses.  They neither imply that
$\rho_{p,r}$ is algebraic nor supply a rational-integer irrationality
measure for it.  Likewise, classical Padé irrationality methods for
hypergeometric *values* begin with a specified algebraic argument and
construct linear forms in the resulting values; here the number to be
measured is the unknown parameter zero itself.

Primary sources checked for this applicability audit are:

* B. Dwork, [*On $p$-adic differential equations IV: generalized
  hypergeometric functions as $p$-adic analytic functions in one
  variable*](https://www.numdam.org/articles/10.24033/asens.1249/),
  *Ann. Sci. École Norm. Sup.* **6** (1973), 295--316;
* J. Diamond, [*Hypergeometric series with a $p$-adic
  variable*](https://msp.org/pjm/1981/94-2/pjm-v94-n2-p03-s.pdf),
  *Pacific J. Math.* **94** (1981), 265--276; and
* N. Koblitz, *The hypergeometric function with $p$-adic parameters*,
  Proceedings of the Queen's Number Theory Conference 1979 (1980),
  319--328, bibliographic entry on the
  [author's publication page](https://sites.math.washington.edu/~koblitz/pbl.html).

The search did not locate a theorem in these sources giving an arithmetic
height or irrationality measure for a zero of the correlated parameter
series (2).  This is a bounded applicability statement about the cited
results, not an exhaustive claim about all literature.

The rigorous conclusions of this note are therefore (2), (4), (13),
(Q1)--(Q4), (21), and the visibility threshold (25).  The literature
comparison is an applicability audit, not a theorem that no future
hypergeometric method can work.

The exact remaining lemma is:

> For every ordinary zero $\rho_{p,r}$ arising from the Bessel index
> interpolation, prove uniformly in the relevant $p,r,n$ that
> $v_p(n-\rho_{p,r})\log p=o(n\log n)$.

Neither the hypergeometric identity nor the direct functional-equation
transfer proves this lemma.  Nothing here proves irrationality or
transcendence of $e+\pi$.

## 7. Exact certificate

The companion script

    scripts/bessel_padic_hypergeometric_zero_pade_certificate.py

checks the terminating identity (5), the quadratic Newton identity (Q1),
the uniform factorial valuation bound (4) on finite residue systems,
monotonicity of $\Lambda_p(k)$, the dominance and nonvanishing statement
(14)--(15), the polynomial difference estimate (17), and the auxiliary
inequality (21) on certified ordinary branches.  It also checks the
post-termination freezing (P1), the exact imbalance identity (P3), and
the half-depth ceiling (P4)--(P5) over finite ranges.

Run

    python -m py_compile scripts/bessel_padic_hypergeometric_zero_pade_certificate.py
    python scripts/bessel_padic_hypergeometric_zero_pade_certificate.py

For a byte-identical replay, use

    python scripts/bessel_padic_hypergeometric_zero_pade_certificate.py \
      --output /tmp/bessel_padic_hypergeometric_zero_pade_certificate.json
    cmp results/bessel_padic_hypergeometric_zero_pade_certificate.json \
      /tmp/bessel_padic_hypergeometric_zero_pade_certificate.json

The finite calculation is diagnostic.  The general proofs are in
Sections 2--6.
