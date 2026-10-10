> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# All fresh primes away from the exceptional ray: a two-pole obstruction

Date: 2026-08-28

## 1. Scope

Let $m\ge1$, let $p>6m$ be prime, and put



$$
N=6m,\quad K=4m+2,\quad r=4m,
$$



and in the local coordinate $t=x+1$ put



$$
A=t-R=-2+3t-t^2,\qquad R=2-2t+t^2,
\qquad f(t)=\frac{A(t)^N}{R(t)^K}=\sum_{j\ge0}f_jt^j.
$$



The exact scalar recurrence in the preceding note proves, for every prime
$p>6m$,



$$
L_0=L_1=0\pmod p\quad\Longrightarrow\quad f_r=f_{r+1}=0\pmod p. \tag{1}
$$



If $p\ne10m+3$, the converse also holds.  The two-pole equivalence in this
note excludes the exceptional ray $p=10m+3$.  That separate degree-five
inverse-series problem $y^5-y=z$ is now resolved uniformly in
sources/mixed_cubic_exceptional_ray_coprimality_theorem.md (SHA-256
396011D7C5D019710E91374087008C8AB6CD4272C64B4954B6DF47DD980C80CF).

## 2. Exact reduction from four singularities to two poles

Write



$$
\delta=p-N=p-6m>0,
 \qquad e=p-K=p-4m-2=2m+\delta-2,
$$



and define



$$
h(t)=\frac{R(t)^e}{A(t)^\delta}.
$$



In characteristic $p$,



$$
f(t)=\left(\frac{A(t)}{R(t)}\right)^p h(t).
$$



Since $(A/R)^p=A(t^p)/R(t^p)$ and $A(0)/R(0)=-1$, comparison of
coefficients below degree $p$ gives



$$
\boxed{f_j=-h_j\pmod p\qquad(0\le j<p).}             \tag{2}
$$



Here $r+1<p$.  Combining (1)--(2) gives the exact fresh-prime
obstruction



$$
\boxed{L_0=L_1=0\Longrightarrow h_r=h_{r+1}=0,}      \tag{3}
$$



with equivalence in (3) whenever $p\ne10m+3$.

This is a genuine simplification: $h$ has only the two poles $1,2$,
both of order $\delta$.  Its polynomial part has degree



$$
2e-2\delta=4m-4=r-4,                                \tag{4}
$$



so $h_r,h_{r+1}$ are already in the pure two-pole tail.

## 3. Exact two-pole/Hahn coefficient formula

At the pole $t=1$, set $y=1-t$.  Then



$$
A=-y(1+y),\qquad R=1+y^2,
$$



and, because $\delta$ is odd,



$$
h(t)=-y^{-\delta}C(y),qquad
 C(y)=\frac{(1+y^2)^e}{(1+y)^\delta}.
$$



Let



$$
a_\ell=-[y^{\delta-\ell}]C(y)\qquad(1\le\ell\le\delta). \tag{5}
$$



These are the principal-part coefficients at $t=1$.  The involution
$t\mapsto2/t$ satisfies



$$
h(2/t)=2^{2m-2}t^{-(4m-4)}h(t).                    \tag{6}
$$



Consequently, for every $j>4m-4$, the complete Taylor coefficient is



$$
\boxed{
 h_j=\sum_{\ell=1}^{\delta}a_\ell
 \binom{j+\ell-1}{\ell-1}
 +2^{2m-2-j}\sum_{\ell=1}^{\delta}(-1)^\ell a_\ell
 \binom{j-4m+3}{\ell-1}.}                          \tag{7}
$$



The second sum in (7) truncates sharply at the two target indices:



$$
\begin{split}
 h_r={}&U_r+2^{-2m-2}\sum_{\ell=1}^{4}(-1)^\ell a_\ell
 \binom3{\ell-1},\\
 h_{r+1}={}&U_{r+1}+2^{-2m-3}\sum_{\ell=1}^{5}(-1)^\ell a_\ell
 \binom4{\ell-1},                                  \tag{8}
\end{split}
$$



where the only remaining global quantities are the two terminating Hahn-type
coefficients



$$
\boxed{
 U_j=-[y^{\delta-1}]
 \frac{(1+y^2)^e}{(1+y)^\delta(1-y)^{j+1}}.}         \tag{9}
$$



Equations (8)--(9) are an exact equivalence, not a numerical heuristic.
They isolate the all-prime difficulty in two adjacent Hasse coefficients of
a two-pole rational function.  A generic root-separation statement for
Jacobi polynomials is insufficient: the quantities in (9) are contiguous
Hahn/Heun-type coefficients, and their connection determinant has irregular
large prime divisors.

## 4. Exact hypergeometric tail formulation

There is a complementary formula over $\mathbb Q$, before reduction
modulo any prime.  Put



$$
a=2m-1,qquad q=2m+1,qquad z=\frac tR,
$$



and



$$
P_{N,a}(z)=\sum_{s\ge0}(-1)^s\binom N{a+s}z^s
 =\binom Na\,{}_2F_1(1,a-N;a+1;z).                  \tag{10}
$$



Direct expansion of $A=t-R$ gives



$$
\boxed{L_0=-2[t^q]P_{N,a}(t/R),\qquad
 L_1=-2[t^{q+2}](t/R)P_{N,a}(t/R).}                 \tag{11}
$$



The contiguous identity



$$
P_{N,a-1}(z)=\binom N{a-1}-zP_{N,a}(z)             \tag{12}
$$



explains why both residues are controlled by one hypergeometric polynomial.
It does not by itself supply finite-field root separation for the two
different coefficient functionals in (11).

## 5. A fixed-gap meta-theorem and rigorous infinite subfamilies

Fix an odd positive integer $\delta$ coprime to 6 and restrict to
$p=6m+\delta$.  Let



$$
X=2^{2m+\delta-1}.
$$



The palindromic full-sum/tail decomposition from the width-49 certificate
constructs four explicit rational numbers



$$
C_0(\delta),T_0(\delta),C_1(\delta),T_1(\delta)
$$



such that



$$
\lambda_0=C_0(\delta)X-T_0(\delta),\qquad
 \lambda_1=C_1(\delta)X-T_1(\delta)\pmod p,          \tag{13}
$$



where $\lambda_0=2^{2m}L_0$ and
$\lambda_1=2^{2m+2}L_1$.  Define the exact rational determinant



$$
\mathcal R_\delta=C_0T_1-C_1T_0.                  \tag{14}
$$



The generalized-binomial construction has only $2$- and $3$-power
denominators: for every prime $\ell\ne3$, a parameter in
$\mathbb Z[1/3]$ is $\ell$-adically integral and so are all of its
binomial coefficients; the extra factors in the construction are powers of
$2$.  Hence every denominator in (13)--(14) is a unit modulo the present
prime $p>6m\ge6$, so $p\ge7$.

This gives the following all-parameter statement.

**Fixed-gap meta-theorem.**  If $\mathcal R_\delta\ne0$, simultaneous
vanishing can occur only when $p$ divides the numerator of
$\mathcal R_\delta$; at each such prime, (13) is a final exact
power-of-two check.  Hence every fixed gap with nonzero determinant has at
most finitely many exceptions.

There is also an explicit uniform height bound.  Write $q=\delta\ge5$,
$n=q-1$, $\alpha_0=2q/3-1$, and $\alpha_1=2q/3-2$.  In addition to
the full-sum formulas in the frozen note, the tails have the exact forms



$$
\begin{split}
 T_0(q)&=[z^n]\frac{(1+z)(1+z^2)^{\alpha_0}}{(1-z)^q},\\
 T_1(q)&=[z^n]\frac{(1+z)^4(1+z^2)^{\alpha_1}}{(1-z)^q}.
\end{split}                                                   \tag{H1}
$$



For $0\le k\le n$ and $\alpha\in\{\alpha_0,\alpha_1\}$,



$$
\left|\binom{\alpha}{k}\right|
 \le \binom{q+k-1}{k}<4^q.
$$



Coefficient majorization at $z=1$ in the four exact formulas gives



$$
\begin{split}
 |C_0|&\le3q^2\,24^q,&
 |C_1|&\le\frac{81}{2}q^2\,24^q,\\
 |T_0|&\le2q\,16^q,&
 |T_1|&\le16q\,16^q.
\end{split}                                                   \tag{H2}
$$



Indeed
$\binom{b/3}{k}$ has reduced denominator dividing
$3^{k+v_3(k!)}$, hence dividing $3^{2k}$.  It follows that the
respective denominators divide
$2^n3^{2n},2^{n+1}3^{2n},3^{2n},3^{2n}$.  Therefore



$$
\boxed{\left|\operatorname{num}\mathcal R_q\right|
 \le129q^3\,62208^q.}                              \tag{H3}
$$



Consequently, conditional only on $\mathcal R_q\ne0$, the moving-gap
inequality



$$
p>129q^3\,62208^q                                 \tag{H4}
$$



already excludes simultaneous vanishing without factorization or a
power-of-two check.  This is a genuine height consequence, but it is not an
unconditional moving-gap theorem because nonvanishing of
$\mathcal R_q$ for every admissible $q$ remains unproved.

For



$$
\delta\in\{1,5,7,11,13,17,19,23,25,29,31,35,37,41,43,47\}, \tag{15}
$$



the frozen deterministic certificate factors (14), checks every compatible
prime divisor, and proves that there are no exceptions.  By Dirichlet's
theorem, each residue class $p\equiv\delta\pmod6$ contains infinitely many
primes, so (15) supplies rigorously proved infinite fresh-prime subfamilies,
not merely a finite numerical scan.

The frozen artifacts are
scripts/mixed_cubic_large_prime_log_residue_fixed_gap_certificate.py (SHA-256
272913D09C4A2F7D7D844F78DEE9A900D47F0793C89D4F76B32DA59273054769)
and its byte-stable JSON output
results/mixed_cubic_large_prime_log_residue_fixed_gap_certificate.json (SHA-256
15167998DAEC481A588E76DE91908A33E9AD8B4FB60B37898BFA64A63D6511A5).

For the first ray the formulas are especially transparent:



$$
\delta=1:\qquad
 \lambda_0=2^{2m+1}-1,qquad
 \lambda_1=2^{2m+3}-1\pmod p.                       \tag{16}
$$



If both vanished, subtracting four times the first congruence from the
second would give $p\mid3$, impossible for $p=6m+1\ge7$.

## 6. Sharp remaining obstruction

The desired uniform theorem is now equivalent, away from $p=10m+3$, to
excluding the simultaneous equalities (8), or equivalently the consecutive
zero in (3).  The reduction is only to two poles, but the Hahn coefficient
$U_j$ remains global.  Fixed-gap determinants already acquire compatible
prime factors of size $6819625707194544521$ at $\delta=41$; therefore a
claim that the determinant is supported on primes at most $6m$, or on a
fixed smooth set, is false at the intermediate resultant level.  The final
power-of-two congruence excludes that candidate, but no uniform identity
forcing this exclusion for moving $\delta$ has been found.

Nor does the determinant itself have a fixed sign:
$\mathcal R_1<0,\mathcal R_5>0,\mathcal R_7<0,\mathcal R_{11}<0$, and
$\mathcal R_{13}>0$.  Thus a direct total-positivity claim for
$\mathcal R_q$ is false.  The height estimate (H3) becomes useful only
after a separate proof that $\mathcal R_q\ne0$.

The accompanying deterministic probe supplies finite diagnostics only.  It
checks exactly that $\mathcal R_q\ne0$ for the 60 admissible integers
$1\le q<180$.  On each subsequence $q=6r+1$ and $q=6r+5$, using the
first 28 values, it also finds no rational polynomial-coefficient recurrence
of order at most 6 and coefficient degree at most 5; full column rank is
certified modulo the prime $1000000007$.  This bounded failed search is
not evidence that no higher or longer recurrence exists, and the finite
nonzero range is not extrapolated to all $q$.

The byte-stable probe artifacts are scripts/mixed_cubic_large_prime_two_pole_probe.py
(SHA-256
31B24AFE392722CBA9A328E72AE7C009EFDF092133DC79A216D6350FFA4D1867)
and results/mixed_cubic_large_prime_two_pole_probe.json (SHA-256
80F66787BDBBB42AED508E47256407ACD4B5976CFFC64F6550BE2BB33B8740AD).

Thus the new theorem-grade content is the two-pole equivalence (2)--(9), the
single-polynomial hypergeometric formulation (10)--(12), and the fixed-gap
meta-theorem with the infinite families (15).  They do not prove the full
statement for all $p>6m$.
