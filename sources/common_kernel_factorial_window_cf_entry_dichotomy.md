> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Factorial-window continued-fraction entry dichotomy and the finite-scaling barrier

Checked: 2026-08-27 UTC.

## 1. Verdict

This note isolates the strongest conclusion that the native
factorial-window mechanism supplies from *misses*, as opposed to hits.
Let $x$ be irrational.  The symbols $p_k/q_k$ retain their original
indices in the full principal-convergent sequence; conditions
$p_k/q_k<x$ select the below-side subsequence without reindexing it.  Put



$$
{\cal A}=\{N\geq2:N\bmod8\in\{0,1,2,3,4\}\}.          \tag{1}
$$



For a fixed $0\leq\delta<1/2$, set



$$
\tau=\frac{2}{1-2\delta},\qquad
 N_\delta(q)=\min\{N\in{\cal A}:q^\tau\leq N!\}.       \tag{2}
$$



At $N=N_\delta(q_k)$, define



$$
\Lambda_k=\frac{N!}{q_k^\tau},\qquad
 \lambda_k=\frac{N!}{q_k^2}
            =\Lambda_kq_k^{\tau-2},                   \tag{3}
$$



and



$$
Z_k=N\,N!\left(x-\frac{p_k}{q_k}\right).             \tag{4}
$$



The native interval has exact normalized endpoints



$$
A_N=N{\cal L}^{\min}_N,\qquad B_N=N{\cal L}^{0}_N,
 \qquad 1<A_N<B_N<5.                                  \tag{5}
$$



Call $A_N<Z_k<B_N$ a native-shaped factorial-window hit.  When
$x=e+\pi$, this is exactly the native hit criterion.  If only finitely
many hits obeying the power cutoff $q_k\leq(N!)^{1/2-\delta}$ occur, then the
entry pair of every sufficiently large below convergent is either



$$
\begin{array}{ll}
 \textbf{low:}&Z_k\leq A_N,\\
 \textbf{high:}&Z_k\geq B_N.
 \end{array}                                          \tag{6}
$$



The exact consequences are:

* every low entry satisfies
  

$$
a_{k+1}>\frac{N\lambda_k}{5}-2,\qquad
   0<x-\frac{p_k}{q_k}
      <\frac5{N\lambda_kq_k^2};                       \tag{7}
$$


* every high entry satisfies
  

$$
a_{k+1}<N\lambda_k.         \tag{8}
$$



The admissible set has maximum gap four.  Minimality in (2) therefore
gives the exact entry ledger



$$
1\leq\Lambda_k<N^4,          \tag{9}
$$



and hence



$$
\lambda_k=q_k^{\tau-2+o(1)},\qquad
 N\Lambda_k=q_k^{o(1)}.                               \tag{10}
$$



Let



$$
\mu_-(x)=\sup\left\{\nu:
 0<x-\frac pq<q^{-\nu}\ \hbox{for infinitely many reduced }p/q
 \right\}
$$



be the below-side irrationality exponent.  Equations
(6)--(10) prove the following dichotomy.

1. If low entries occur infinitely often and $\delta>0$, then
   

$$
\mu_-(x)\geq\tau>2.      \tag{11}
$$


   In particular, an algebraic irrational cannot have infinitely many
   such low entries, by Roth's theorem.
2. If low entries occur only finitely often, then entries are eventually
   high and
   

$$
\mu_-(x)\leq\tau.        \tag{12}
$$


3. At the original square-root cutoff $\delta=0$, eventual high entries
   force $\mu_-(x)=2$.  Infinite low entries force only
   

$$
a_{k+1}>
     \left(\frac25+o(1)\right)\frac{\log q_k}{\log\log q_k},
   \qquad
   x-\frac{p_k}{q_k}
   <\left(\frac52+o(1)\right)
     \frac{\log\log q_k}{q_k^2\log q_k}.              \tag{13}
$$


   This is a logarithmic improvement over exponent two, not a fixed
   Roth improvement.

There is no unconditional lower bound on next partial quotients from
finitely many hits.  The golden ratio gives an exact countermodel:
for every sufficiently large $N$, no rational $p/q<\phi$ with
$q^2\leq N!$ lies in the native interval, even if every residue class
of $N$ is allowed.  Nevertheless every partial quotient of $\phi$
equals one and $\mu(\phi)=2$.

The same countermodel survives every fixed finite collection of scaled
native windows.  More generally, if $x$ is badly approximable, so that


$$
\left|x-\frac pq\right|\geq\frac{c(x)}{q^2}
 \quad\hbox{for every reduced }p/q                    \tag{13a}
$$


with $c(x)>0$, then scales $s_N=o(N)$ cannot catch $x$ at the
square-root cutoff.  Catching such bounded-type entries forces the largest
scale to be $\Omega(N)$, and this consumes the entire factor $1/N$ in
the approximation error.  Separately, a multiplicative
covering argument also shows that bridging the factorial jump


$$
{Z_{N+1}\over Z_N}={(N+1)^2\over N}\sim N            \tag{14}
$$


with copies of one fixed-ratio interval requires $\Omega(\log N)$
different scales.  Thus residue completion or finitely many fixed scales
cannot turn misses into Roth-violating approximations.

These are abstract all-parameter theorems.  They do not assert that
$e+\pi$ is irrational or transcendental.

## 2. The exact entry ledger

The consecutive gaps in ${\cal A}$ are $1,1,1,1,4$.  Let $M$ be
the element of ${\cal A}$ immediately before
$N=N_\delta(q)$.  Then $1\leq N-M\leq4$.  By minimality,



$$
M!<q^\tau\leq N!.            \tag{15}
$$



Consequently



$$
1\leq\Lambda=\frac{N!}{q^\tau}
 <\frac{N!}{M!}
 =\prod_{j=M+1}^{N}j
 \leq N^{N-M}\leq N^4,                               \tag{16}
$$



which proves (9).  Stirling's formula and (15) give



$$
\tau\log q=\log N!+O(\log N)
            =N\log N-N+O(\log N),                    \tag{17}
$$



where the implied constant is absolute for this fixed gap-four set.
In particular,



$$
\log N=o(\log q),\qquad
 N\Lambda=q^{o(1)},\qquad
 \lambda=\Lambda q^{\tau-2}=q^{\tau-2+o(1)}.          \tag{18}
$$



If every residue class is made available, the maximum gap is one and
(16) improves from $\Lambda<N^4$ to $\Lambda<N$.  This changes only
a fixed power of $N$, hence only a $q^{o(1)}$ factor.

At $\delta=0$, equation (17) specializes to



$$
N=\left(2+o(1)\right)\frac{\log q}{\log\log q}.      \tag{19}
$$



## 3. Continued-fraction coordinate and the low/high split

Write



$$
\alpha_{k+1}=[a_{k+1};a_{k+2},\ldots],\qquad
 D_k=\alpha_{k+1}+\frac{q_{k-1}}{q_k}.                \tag{20}
$$



The exact convergent-error formula is



$$
q_k^2\left(x-\frac{p_k}{q_k}\right)=\frac1{D_k},
 \qquad
                         a_{k+1}<D_k<a_{k+1}+2.       \tag{21}
$$



Equations (3)--(4) give



$$
Z_k=\frac{N\lambda_k}{D_k}.
                                                               \tag{22}
$$



For a low entry, $Z_k\leq A_N<5$, so



$$
D_k\geq\frac{N\lambda_k}{A_N}
       >\frac{N\lambda_k}{5}.
$$



Using $D_k<a_{k+1}+2$ and then (21) proves both inequalities in (7).
For a high entry, $Z_k\geq B_N>1$, hence



$$
a_{k+1}<D_k\leq\frac{N\lambda_k}{B_N}<N\lambda_k,
$$



which proves (8).

For completeness, the below-side irrationality exponent satisfies



$$
\boxed{
 \mu_-(x)=2+\limsup_{\substack{k\to\infty\\p_k/q_k<x}}
 \frac{\log a_{k+1}}{\log q_k}.}                     \tag{23}
$$



Indeed, (21) proves the lower direction.  Conversely, every sufficiently
strong one-sided approximation of exponent $>2$ is a principal
convergent by Legendre's criterion, so it is included in the limsup.

If low entries occur infinitely often and $\tau>2$, equations (7),
(10), and (23) give (11).  If low entries are finite, (8), (10), and
(23) give (12).  When $\tau=2$, below convergents always give
$\mu_-(x)\geq2$, so eventual high entries give equality.  For infinite
low entries, substitute (19) into (7) and use $\lambda\geq1$ to obtain
(13).

This is the complete entry dichotomy.  A low miss has useful arithmetic
meaning; a high miss supplies an upper bound, not a lower bound, for the
next partial quotient.

## 4. Fixed power saving and the Roth boundary

Suppose $\delta>0$.  A hit or a low entry satisfies



$$
0<x-\frac pq<\frac5{N\,N!}
 \leq\frac5Nq^{-\tau}.                               \tag{24}
$$



If this occurs infinitely often for distinct reduced fractions, then for
every fixed $2<\nu<\tau$, the right side is eventually smaller than
$q^{-\nu}$.  Hence $\mu_-(x)\geq\tau$, and Roth excludes algebraic
irrational $x$.

It follows that, under the additional hypothesis that $x$ is algebraic
irrational, every fixed-power-saving entry is eventually high.  This is
not an independent transcendence argument: it is exactly the Roth boundary
expressed in factorial coordinates.

At $\delta=0$, (24) has exponent two and only the additional factor
$1/N$.  By (19), this is the logarithmic factor in (13).  No fixed
positive exponent can be extracted:



$$
\frac{\log N}{\log q}\longrightarrow0.              \tag{25}
$$



Even the largest entry-phase factor allowed by (16) is



$$
N\lambda<N^5
 =\left(\frac{\log q}{\log\log q}\right)^{5+o(1)}
 =q^{o(1)}.                                          \tag{26}
$$



With every residue shift available, $N^5$ improves to $N^2$, still
$q^{o(1)}$.

## 5. An exact bounded-type countermodel

Let



$$
\phi=\frac{1+\sqrt5}{2},\qquad
 \phi'=\frac{1-\sqrt5}{2}.
$$



For any rational $0\leq p/q<\phi$,



$$
\left|\left(\frac pq\right)^2-\frac pq-1\right|
 =\left|\frac pq-\phi\right|
  \left|\frac pq-\phi'\right|
 =\frac{|p^2-pq-q^2|}{q^2}\geq\frac1{q^2}.           \tag{27}
$$



Since $0\leq p/q<\phi$,



$$
\left|\frac pq-\phi'\right|<\phi-\phi'=\sqrt5.
$$



Therefore



$$
\phi-\frac pq>\frac1{\sqrt5\,q^2}.
                                                               \tag{28}
$$



If $q^2\leq N!$, equations (5) and (28) give



$$
\phi-\frac pq>\frac1{\sqrt5\,N!}
 >\frac5{N\,N!}\qquad(N>5\sqrt5).                    \tag{29}
$$



Any putative hit in (29) has $p/q>0$ once $N\geq12$, so the preceding
norm bound applies.  Thus no native-shaped hit exists for $\phi$ once
$N\geq12$, even if all
integer indices are declared admissible.  Yet



$$
\phi=[1;1,1,1,\ldots],
$$



so all next partial quotients equal one.  Equation (28), together with
the convergents, also gives $\mu(\phi)=2$.

This refutes any abstract implication



$$
\text{finitely many factorial-window hits}
 \quad\Longrightarrow\quad
 \text{large next partial quotients or }\mu(x)>2.     \tag{30}
$$



It does not say that $e+\pi$ behaves like $\phi$; it proves that the
window mechanism alone cannot exclude that behavior.

## 6. Scaled windows and multiplicative coverage

Consider a finite family of positive fixed scales $s_1,\ldots,s_m$.
A scaled native window has normalized upper endpoint at most $5s_j$.
Put $S=\max_js_j$.  Any hit for $\phi$ would satisfy



$$
\phi-\frac pq<\frac{5S}{N\,N!}.
$$



Combining this with (28) and $q^2\leq N!$ forces



$$
S>\frac{N}{5\sqrt5}.    \tag{31}
$$



No fixed finite family satisfies (31) for unbounded $N$.  The argument
generalizes without using the quadratic norm.
If $x$ satisfies (13a), a scaled window with normalized upper endpoint
at most $CS_N$ and $q^2\leq N!$ can contain a rational only if



$$
\frac{c(x)}{N!}\leq\frac{CS_N}{N\,N!},
 \qquad\hbox{hence}\qquad
 S_N\geq\frac{c(x)}C N.                              \tag{31a}
$$



Thus $S_N=o(N)$ is impossible for every badly approximable $x$, while
scales of order $N$ change the ceiling to $O(1/N!)$ and remove the
factor $1/N$.

There is a complementary, but logically independent, covering count.  Let
a base normalized interval have fixed ratio



$$
\rho=\frac BA>1.
$$



Suppose $m$ scaled copies are ordered and overlap consecutively so that
their union covers one connected multiplicative range.  Then



$$
s_{j+1}A\leq s_jB
 \quad\Longrightarrow\quad
 \frac{s_mB}{s_1A}\leq\rho^m.                        \tag{32}
$$



The normalized error of one fixed rational changes at consecutive
factorial indices by the exact factor



$$
\frac{(N+1)(N+1)!}{N\,N!}
 =\frac{(N+1)^2}{N}.                                 \tag{33}
$$



Bridging this jump with fixed-ratio scaled copies requires



$$
m\geq
 \frac{\log((N+1)^2/N)}{\log\rho}
 =\Omega(\log N).                                    \tag{34}
$$



Thus no fixed number of scales can remove the growing multiplicative
holes between factorial levels.  This argument controls only the number
and relative span of the scales: the same span could be placed, for example,
between $1/N$ and $1$.  It does **not** by itself force an absolute scale
of order $N$.  That separate absolute lower bound comes from the
badly-approximable inequality (31a), not from multiplicative coverage.

## 7. Scope and replay

The theorem is abstract and all-parameter.  The only native inputs are the
exact interval criterion, the admissible residue set, and the uniform
endpoint bounds (5).  Finite continued-fraction data for $e+\pi$ are not
used.

Run

    python3 scripts/common_kernel_factorial_window_cf_entry_dichotomy_certificate.py

from the research directory.  The replay checks the entry-gap inequalities,
the exact continued-fraction identities on rational quadratic-field pairs,
the golden-ratio norm obstruction, and the multiplicative covering ledger.
Finite rows are diagnostics for the symbolic proofs and are not
extrapolated.

Pinned upstream manifest:

    45c9253a4d4572806c0650345f2e47e4d8953618daf5c87512a1d62e0e1cd958  results/common_kernel_native_cf_window_scan_hashes.sha256
