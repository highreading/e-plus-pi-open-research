> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Every integer Bessel jet contains the same Euler factorial constant

Checked: 2026-08-27 UTC.

## 1. Verdict

Let



$$
q_0=q_1=1,
 \qquad q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\geq2),
\tag{1}
$$



and let $f_p$ be the canonical interpolation of



$$
f(n)=(-1)^nq_n.
\tag{2}
$$



The already proved hypergeometric representation is



$$
f_p(x)=\sum_{k\geq0}\frac{(-x)_k(x+1)_k}{k!}.
\tag{3}
$$



Define the companion Padé numerator sequence



$$
p_0=1,\qquad p_1=3,\qquad
 p_n=(4n-2)p_{n-1}+p_{n-2},
\tag{4}
$$



and the integer sequence



$$
b_0=0,\qquad b_1=4,\qquad
 b_{n+2}=(4n+6)b_{n+1}+b_n+4q_{n+1}.
\tag{5}
$$



For every prime $p$, put



$$
\mathcal K_p=\sum_{m=0}^{\infty}m!\in\mathbb Z_p.
\tag{6}
$$



Then every integer first jet has the exact form



$$
\boxed{
 f_p'(n)=(-1)^{n+1}\bigl(p_n\mathcal K_p-b_n\bigr)
 \qquad(n\geq0).}
\tag{7}
$$



Consequently, for every fixed $n$,



$$
f_p'(n)\in\mathbb Q
 \quad\Longleftrightarrow\quad
 \mathcal K_p\in\mathbb Q,
\tag{8}
$$



where $\mathbb Q$ is embedded in $\mathbb Q_p$.  Thus passing from
finite parameter shifts to Taylor jets does not produce rational
coefficient data of controlled height: already the first jet at **every**
integer contains Euler's factorial constant.  Irrationality of
$\mathcal K_p$ for any specified prime remains open.

There is also an exact digit consequence.  Suppose $p$ is odd, $n$
lies on an ordinary root branch, and



$$
a=v_p(q_n)\geq1,
 \qquad
 u_n=p_n\mathcal K_p-b_n\in\mathbb Z_p^\times.
\tag{9}
$$



If the compatible root has the next lift



$$
\rho\equiv n+t p^a\pmod {p^{a+1}},
 \qquad 0\leq t<p,
\tag{10}
$$



then



$$
\boxed{
 t\equiv\frac{q_n}{p^a}\,u_n^{-1}\pmod p.}
\tag{11}
$$



Formula (11) determines the first nonzero digit after the exact valuation;
it does **not** bound how many zero digits occurred between the ordinary
base-$p$ size of $n$ and the exponent $a$.  Hence (7)--(11) are a
rigorous obstruction to a rational Taylor-jet shortcut, not the missing
uniform estimate



$$
v_p(q_n)\log p=o(n\log n).
\tag{12}
$$



## 2. The two initial derivatives

Write



$$
T_k(x)=\frac{(-x)_k(x+1)_k}{k!}
 =\frac{(-1)^k}{k!}\prod_{h=-k+1}^{k}(x+h).
\tag{13}
$$



We first justify differentiation of (3), rather than only checking that
the resulting numerical series converges.  Fix an integer center $n$.
For odd $p$, expand on the disk $x=n+py$, $y\in\mathbb Z_p$.  In
each product obtained by differentiating $T_k$, one factor has been
removed from the $2k$ consecutive factors



$$
n-k+1+py,\ldots,n+k+py.
$$



At least $\lfloor2k/p\rfloor$ of their constant terms are divisible by
$p$.  Hence the Gauss valuation on $\mathbb Q_p\langle y\rangle$
satisfies, uniformly in the removed factor,



$$
v_{\rm G}\bigl(T_k'(n+py)\bigr)
 \geq
 \left\lfloor\frac{2k}{p}\right\rfloor-1-v_p(k!)
 \geq
 \frac{p-2}{p(p-1)}k-2.
\tag{13a}
$$



For $p=2$, use the analytic disk $x=n+4y$.  Counting once the even
constant terms and once more those divisible by $4$, and allowing for
the removed factor, gives



$$
v_{\rm G}\bigl(T_k'(n+4y)\bigr)
 \geq k+\left\lfloor\frac k2\right\rfloor-2-v_2(k!)
 \geq\left\lfloor\frac k2\right\rfloor-1.
\tag{13b}
$$



The same bounds without the losses $1$ and $2$ apply to $T_k$
itself.  Both the original series and its derivative series therefore
converge in the corresponding local Tate algebra.  Differentiation is a
continuous operator there (after the fixed change of variable
$x=n+py$, or $x=n+4y$), so (3) may be differentiated term by term at
every integer center.

At an integer $n\geq0$, every term with $k\geq n+1$ has the simple
factor $x-n$.  Removing that factor gives



$$
\boxed{
 T_k'(n)=(-1)^{n+1}
 \frac{(k-n-1)!(n+k)!}{k!}
 \qquad(k\geq n+1).}
\tag{14}
$$



The factorials make the differentiated tail converge in every
$\mathbb Q_p$.  At $n=0$, (14) gives



$$
f_p'(0)=-\sum_{m\geq0}m!=-\mathcal K_p.
\tag{15}
$$



At $n=1$, the terminating part consists of $T_0'(1)=0$ and
$T_1'(1)=-3$.  In the tail put $m=k-2$.  Equation (14) gives



$$
\sum_{k\geq2}T_k'(1)
 =\sum_{m\geq0}m!(m+3).
\tag{16}
$$



The elementary telescoping identity



$$
\sum_{m=0}^{N}m\,m!=(N+1)!-1
\tag{17}
$$



has limit $-1$ in every $\mathbb Q_p$.  Therefore



$$
f_p'(1)=-3+(3\mathcal K_p-1)
 =3\mathcal K_p-4.
\tag{18}
$$



Equations (15) and (18) are exactly (7) at $n=0,1$.

## 3. Propagation to every integer

The interpolation satisfies



$$
f_p(x+2)+(4x+6)f_p(x+1)-f_p(x)=0.
\tag{19}
$$



Differentiate and specialize at $x=n$:



$$
f_p'(n+2)+(4n+6)f_p'(n+1)-f_p'(n)
 =-4f_p(n+1).
\tag{20}
$$



Since $f_p(n+1)=(-1)^{n+1}q_{n+1}$, substitution of



$$
D_n=(-1)^{n+1}(p_n\mathcal K_p-b_n)
\tag{21}
$$



into (20) separates the coefficient of $\mathcal K_p$ and the rational
part.  The former is exactly recurrence (4), while the latter is exactly
recurrence (5).  The two initial values were proved in Section 2, so
induction proves (7) for all $n\geq0$.

This proof also shows that $b_n$ is an integer without assigning a
rational height to $\mathcal K_p$.  Positivity and a coarse useful
height bound follow directly from the recurrences:



$$
0\leq b_n\leq4(n+1)p_n,
 \qquad
 \log\max\{1,b_n\}=n\log n+O(n).
\tag{22}
$$



For the upper bound, use $0<q_n<p_n$ for $n\geq1$, the initial
values, and induction in (5).  For the matching logarithmic lower bound,
positivity in (5) gives



$$
b_n\geq4\prod_{j=2}^{n}(4j-2)\qquad(n\geq1),
$$



with the empty product interpreted as $1$.  The elementary product
bounds for (4) now prove the logarithmic estimate in (22).  Thus even
after formally adjoining $\mathcal K_p$, the integer multipliers in (7)
already live on the Bessel main-height scale.

## 4. Exact next-digit formula

Let $n$ be as in (9), and put $M=p^a$.  The proved affine lift law
on an ordinary branch says that the unique child $n+tM$ modulo
$p^{a+1}$ satisfies



$$
\frac{q_n}{M}+t\,\delta_M(n)\equiv0\pmod p,
\tag{23}
$$



where



$$
\delta_M(n)=\frac{-q_{n+M}-q_n}{M}.
\tag{24}
$$



For $a=1$ this is the definition of $\delta_p$; for $a\geq2$, the
prime-power slope theorem and the fact $p\mid q_n$ give



$$
\delta_M(n)\equiv\delta_p(n)\pmod p.
\tag{25}
$$



On a root disk, the derivative/slope identity is



$$
f_p'(n)\equiv(-1)^n\delta_p(n)\pmod p.
\tag{26}
$$



Combining (7) and (26) gives



$$
\delta_M(n)\equiv-u_n\pmod p.
\tag{27}
$$



Substitution in (23) proves (11).  In particular, ordinary-root
simplicity is equivalently



$$
p_n\mathcal K_p-b_n\not\equiv0\pmod p.
\tag{28}
$$



The formula is valid at the exact one-exponent lift.  No unproved
quadratic Taylor remainder or modulus-$p^{2a}$ Newton formula is used.

## 5. Arithmetic meaning and limitation

The value $\mathcal K_p$ is Euler's factorial series at $-1$ in the
usual convention



$$
E_p(z)=\sum_{m\geq0}m!(-z)^m.
\tag{29}
$$



Matala-aho and Zudilin construct Padé approximants and prove global
alternatives across sets of primes, but not irrationality for any one
specified $\mathcal K_p$:

T. Matala-aho and W. Zudilin,
[*Euler's factorial series and global relations*](https://arxiv.org/abs/1703.02633),
*J. Number Theory* **186** (2018), 202--210.

The relevance here is exact rather than heuristic.  By (8), rationality
of one integer derivative $f_p'(n)$ is equivalent to rationality of
$\mathcal K_p$.  A local Hermite--Padé construction over $\mathbb Q_p$
may freely use these jets, but it has no rational coefficient height until
additional arithmetic information about $\mathcal K_p$ is supplied.
Replacing the jets with finite rational truncations returns to the already
proved factorial order-versus-height barrier.

This does not prove that a different global auxiliary is impossible.  It
proves that the most direct Taylor-jet refinement of the finite-shift
method introduces a fixed-prime open constant at its first new datum.

## 6. Certificate

The companion script

    scripts/bessel_padic_all_integer_jet_euler_obstruction_certificate.py

checks with exact integer arithmetic:

1. the tail derivative formula (14) on a finite grid;
2. recurrences (4)--(5) and the linear-form propagation (20)--(21);
3. positivity and the explicit bound in (22); and
4. formula (11) on several certified ordinary branches, using only
   $\mathcal K_p\bmod p=\sum_{m=0}^{p-1}m!\bmod p$.

The all-parameter proof is Sections 2--4.  The finite checks are regression
tests, not extrapolation.  Nothing in this note proves (12), irrationality
of $\mathcal K_p$, or irrationality or transcendence of $e+\pi$.
