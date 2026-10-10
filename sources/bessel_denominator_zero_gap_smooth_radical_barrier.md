> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Zero-gap sparsity for the exponential Padé denominator, and the remaining valuation barrier

## 1. Statement

Let



$$
q_0=q_1=1,\qquad q_n=2(2n-1)q_{n-1}+q_{n-2}\quad(n\ge 2).
$$



For an odd prime $p$, put



$$
\mathcal R_p=\{r\in\{0,\ldots,p-1\}:q_r\equiv0\pmod p\},
 \qquad R_p=|\mathcal R_p|.
$$



The period congruence



$$
q_{n+p}\equiv-q_n\pmod p
\tag{1}
$$



is proved independently in `exponential_beta_bessel_period_congruence.md`.

**Theorem 1 (zero-gap capacity).**  For every odd prime $p$ and every integer
$D$ with $1\le D\le p$,



$$
R_p\le {D(D-1)\over2}+{p\over D+1}.
\tag{2}
$$



In particular,



$$
R_p\le 2p^{2/3}.
\tag{3}
$$



This gives a rigorous average bound for the squarefree smooth part.  Define



$$
\operatorname{rad}_{\le X}(q_n)
 =\prod_{\substack{p\le X\\p\mid q_n}}p,
$$



where the product is over odd primes (the sequence is odd, so omitting $2$
does nothing).

**Corollary 2 (average smooth-radical bound).**  For integers $N\ge1$ and
real $X\ge3$,



$$
\sum_{n=N}^{2N-1}\log\operatorname{rad}_{\le X}(q_n)
 \le 3NX^{2/3}\log X+2X^{5/3}\log X.
\tag{4}
$$



Consequently, if $X=C N\log N$, with fixed $C>0$, then



$$
{1\over N}\sum_{n=N}^{2N-1}
 \log\operatorname{rad}_{\le X}(q_n)
 =O_C\!\left(N^{2/3}(\log N)^{8/3}\right)
 =o(N\log N).
\tag{5}
$$



Thus at least one $n\in[N,2N)$ has a squarefree $X$-smooth factor of
logarithmic size $o(N\log N)$.  This is not yet a bound for the full smooth
part: the exact remaining term is the excess valuation sum in Section 5.

## 2. Proof of Theorem 1

No two cyclically adjacent residue classes can belong to $\mathcal R_p$.
Indeed, the recurrence in the shifted form



$$
q_{n+1}=(4n+2)q_n+q_{n-1}
\tag{6}
$$



would propagate two adjacent zeros backwards to $q_0\equiv0\pmod p$, a
contradiction.  Congruence (1) makes the same argument valid across the cyclic
boundary.

Suppose first that $R_p>0$.  List the zero classes cyclically, and let $N_d$
be the number of gaps of length $d$ from one zero class to the next.  Then



$$
N_1=0,\qquad \sum_{d=2}^{p}N_d=R_p,
 \qquad \sum_{d=2}^{p}dN_d=p.
\tag{7}
$$



Introduce polynomials over $\mathbf F_p$ by



$$
P_0(X)=0,\qquad P_1(X)=1,
$$



and, for $j\ge0$,



$$
P_{j+2}(X)=(4X+4j+6)P_{j+1}(X)+P_j(X).
\tag{8}
$$



If $q_r\equiv0\pmod p$, then $q_{r+1}\not\equiv0\pmod p$, and induction
from (6) gives



$$
q_{r+j}\equiv q_{r+1}P_j(r)\pmod p\qquad(j\ge0).
\tag{9}
$$



This remains valid when the indices cross $p$, because both the recurrence
coefficients and the assertion that an index is a zero are compatible with
(1).  Therefore a zero gap of length $d$ starting at $r$ makes $r$ a root
of $P_d$.

For every $d\ge1$, (8) shows inductively that



$$
\deg P_d=d-1,\qquad \operatorname{lc}(P_d)=4^{d-1}.
\tag{10}
$$



In particular, for $1\le d\le p$, $P_d$ is a nonzero polynomial over
$\mathbf F_p$ and has at most $d-1$ roots.  Distinct gaps start at distinct
zero classes, hence



$$
N_d\le d-1\qquad(2\le d\le p).
\tag{11}
$$



For any $1\le D\le p$, equations (7) and (11) now give



$$
\begin{aligned}
 R_p
 &=\sum_{2\le d\le D}N_d+\sum_{d>D}N_d\\
 &\le\sum_{d=2}^{D}(d-1)+{1\over D+1}\sum_{d>D}dN_d\\
 &\le {D(D-1)\over2}+{p\over D+1}.
 \end{aligned}
$$



If $R_p=0$, this is immediate.  Taking $D=\lceil p^{1/3}\rceil$ yields



$$
R_p\le {1\over2}(p^{1/3}+1)p^{1/3}+p^{2/3}
 \le2p^{2/3}
$$



for $p\ge3$, proving (3).

## 3. Proof of Corollary 2

By (1), an interval of $N$ consecutive integers contains at most
$(N/p+1)R_p$ indices for which $p\mid q_n$.  Therefore



$$
\begin{aligned}
 \sum_{n=N}^{2N-1}\log\operatorname{rad}_{\le X}(q_n)
 &\le\sum_{p\le X}\left({N\over p}+1\right)R_p\log p\\
 &\le2N\log X\sum_{m\le X}m^{-1/3}
   +2\log X\sum_{m\le X}m^{2/3}\\
 &\le3NX^{2/3}\log X+2X^{5/3}\log X.
 \end{aligned}
$$



Here enlarging the prime sums to all positive integers only weakens the bound,
and $\sum_{m\le X}m^{-1/3}\le(3/2)X^{2/3}$.  Formula (5) follows by
substitution and division by $N$.

## 4. Exact first-lift law

The root classes have a useful, but nonuniform, first-order lifting law.

**Theorem 3 (second anti-period difference).**  For every odd prime $p$ and
every $n\ge0$,



$$
\boxed{q_{n+2p}+2q_{n+p}+q_n\equiv2p q_n\pmod{p^2}.}
\tag{12}
$$



**Proof.**  Put $c_n=4n-2$, so $q_n=c_nq_{n-1}+q_{n-2}$, and define



$$
u_n={q_{n+p}+q_n\over p}\in\mathbf Z.
\tag{13}
$$



Integrality follows from (1).  Comparing the recurrences at $n+p$ and
$n$ gives, for $n\ge2$,



$$
u_n=c_nu_{n-1}+u_{n-2}+4q_{n+p-1}.
\tag{14}
$$



Modulo $p$, (1) makes the last term $-4q_{n-1}$.  Replacing $n$ by
$n+p$ in (14) makes its last term $+4q_{n-1}$ modulo $p$.  Hence



$$
y_n:=u_{n+p}+u_n
$$



satisfies the original homogeneous recurrence modulo $p$.  It remains to
identify its two initial values.  They are computed here explicitly, to avoid
hiding the arithmetic needed by the lifting law.

Use



$$
a_{n,j}={(n+j)!\over j!(n-j)!}
 =\binom{n+j}{j}n(n-1)\cdots(n-j+1),
 \qquad
 q_n=(-1)^n\sum_{j=0}^n(-1)^ja_{n,j}.
\tag{15}
$$



For $p\ge5$, set, in $\mathbf F_p$,



$$
S=\sum_{h=0}^{p-2}h!,
 \qquad
 T=\sum_{j=2}^{p-2}(j+1)(j-2)!.
$$



Removing the unique factor $p$ from the terms that are nonzero modulo
$p^2$ gives the following elementary reductions.  Entries containing
$a_{n,j}/p$ are congruences modulo $p$; undivided entries are congruences
modulo $p^2$.



$$
\begin{array}{c|c|c}
n&\text{ordinary indices}&\text{exceptional indices}\\ \hline
p& a_{p,j}/p\equiv(-1)^{j-1}(j-1)!\ (1\le j<p)
  &a_{p,p}/p\equiv-2\\
2p&a_{2p,j}/p\equiv2(-1)^{j-1}(j-1)!\ (1\le j<p)
  &a_{2p,p}/p\equiv-6\\
p+1&a_{p+1,1}\equiv2+3p,\quad
 a_{p+1,j}/p\equiv(j+1)(-1)^{j-2}(j-2)!\ (2\le j\le p-2)
  &a_{p+1,p-1}\equiv0,\ a_{p+1,p}/p\equiv-2,\
   a_{p+1,p+1}/p\equiv-4\\
2p+1&a_{2p+1,1}\equiv2+6p,\quad
 a_{2p+1,j}/p\equiv2(j+1)(-1)^{j-2}(j-2)!\ (2\le j\le p-2)
  &a_{2p+1,p-1}\equiv0,\ a_{2p+1,p}/p\equiv-6,\
   a_{2p+1,p+1}/p\equiv-12
\end{array}
$$



In the $2p$ row all $j\ge p+1$, and in the $2p+1$ row all
$j\ge p+2$, are also zero modulo $p^2$.  For example, for
$1\le j<p$,



$$
{a_{p,j}\over p}
 \equiv\binom{p+j}{j}\prod_{h=1}^{j-1}(p-h)
 \equiv(-1)^{j-1}(j-1)!\pmod p.
$$



The other entries follow identically from (15), Lucas's theorem for the
displayed binomial factor, and Wilson's congruence
$(p-1)!\equiv-1\pmod p$.  Substitution, including the signs in (15), yields



$$
\begin{array}{ll}
q_p\equiv-1+p(S-2),&q_{2p}\equiv1+p(-2S+6),\\
q_{p+1}\equiv-1+p(T-5),&q_{2p+1}\equiv1+p(12-2T)
\end{array}
\pmod{p^2}.
\tag{16}
$$



Consequently



$$
y_0={q_{2p}+2q_p+q_0\over p}\equiv2,
 \qquad
 y_1={q_{2p+1}+2q_{p+1}+q_1\over p}\equiv2\pmod p.
$$



For $p=3$, the same two values follow directly from
$(q_0,q_1,q_3,q_4,q_6,q_7)\equiv(1,1,8,2,7,1)\pmod9$.
Since $q_0=q_1=1$, uniqueness in the recurrence gives
$y_n\equiv2q_n\pmod p$.  Multiplication by $p$ is exactly (12).
$\square$

**Corollary 4 (affine anti-period lift).**  If $p\mid q_r$, define



$$
\delta_p(r)={-q_{r+p}-q_r\over p}\pmod p.
$$



Then, for every integer $t\ge0$,



$$
\boxed{(-1)^tq_{r+tp}\equiv q_r+tp\,\delta_p(r)\pmod{p^2}.}
\tag{17}
$$



Indeed, (1) makes every $q_{r+tp}$ divisible by $p$, and (12) says that
the second finite difference of $(-1)^tq_{r+tp}$ is zero modulo $p^2$.
Thus it is affine, and its values at $t=0,1$ give (17).  In particular, the
lifts $r+tp\pmod{p^2}$ are governed by the single linear congruence



$$
{q_r\over p}+t\delta_p(r)\equiv0\pmod p.
\tag{18}
$$



There is exactly one lift if $\delta_p(r)\ne0$.  If
$\delta_p(r)=0$, there are no lifts when $p^2\nmid q_r$, but all $p$
lifts when $p^2\mid q_r$.  The last, fully branching alternative remains
possible in principle: nothing in Theorem 3 bounds or excludes it.

The reflection congruence proved in
`critical_fourier_large_prime_matching_filter.md` gives



$$
q_{M-1-s}\equiv q_s\pmod M\qquad(M\text{ odd}).
\tag{19}
$$



If the central class $r=(p-1)/2$ is a root modulo $p$, reflection with
$M=p^2$ sends its lift parameter $t$ to $p-1-t$.  The parity factor in
(17) is unchanged, because $p-1$ is even.  Comparing the affine values at
$t=0$ and $t=p-1$ forces $\delta_p(r)=0$.  Hence every central root
necessarily lies on the singular branch: it either dies modulo $p^2$, or it
has all $p$ lifts.  Deciding whether



$$
p^2\mid q_{(p-1)/2}
$$



on such a class is a genuine Wieferich-type obstruction left open here.

## 5. Precise unresolved reduction: excess valuations

Write



$$
q_{n,\le X}=\prod_{\substack{p\le X\\p\mid q_n}}p^{v_p(q_n)}.
$$



Then the exact identity



$$
\log q_{n,\le X}
 =\log\operatorname{rad}_{\le X}(q_n)+\mathcal E_X(n),
\qquad
\mathcal E_X(n)=\sum_{p\le X}(v_p(q_n)-1)_+\log p
\tag{20}
$$



isolates what Theorem 1 does not control.  This is a genuine obstruction rather
than a cosmetic distinction.  Direct exact recurrence calculation gives



$$
v_7(q_{18})=3,\qquad v_7(q_{361})=4,
 \qquad v_{11}(q_{1359})=5.
\tag{21}
$$



The period congruence modulo prime powers says that these high valuations recur
on residue classes modulo the corresponding prime power; it does not bound the
valuation.

One must also not assume that every root modulo $p$ has an ordinary simple
Hensel lift.  The first singular example (in increasing odd-prime order) is



$$
p=79,\qquad r=39.
$$



Here $r=(79-1)/2$ is the central class, so Corollary 4 and reflection force
its displacement to vanish.  Exact modular recurrence gives



$$
q_{39}\equiv948=12\cdot79\pmod{79^2},
\qquad
 q_{39+79t}\equiv(-1)^t948\pmod{79^2}
 \quad(0\le t<79).
\tag{22}
$$



Thus $39$ is a root modulo $79$, its first anti-period displacement
vanishes modulo $79^2$, and none of its $79$ lifts is a root modulo
$79^2$.  The certificate exhausts every root for every smaller odd prime and
finds a nonzero first displacement there.  This finite statement does not by
itself classify singular roots at larger primes, but it rigorously rules out a
blanket “all roots are Hensel-simple” argument.

There is some cancellation after passing to the three-adjacent Fourier matching
gcd.  For example, for $n=18$, the exact matching calculations at
$k=1004,1005,1006$ have



$$
v_7(q_{18})=3,\qquad
 (v_7(g_{1004}),v_7(g_{1005}),v_7(g_{1006}))=(3,2,1),
$$



so $v_7(\gcd(g_{1004},g_{1005},g_{1006}))=1$.  This is useful evidence but
not a uniform theorem: the global order-three recurrence has reset pivots at
both moving-band boundaries, so ordinary homogeneous propagation cannot carry
a divisibility constraint through those pivots.

Thus a sufficient next theorem would be either

1. an average bound $\sum_{n=N}^{2N-1}\mathcal E_X(n)=o(N^2\log N)$ for
   $X\asymp N\log N$, or
2. directly, a uniform/average bound on the prime-power content of
   $G_3=\gcd(g_K,g_{K+1},g_{K+2})$ outside the common one-block band.

Neither follows from a largest-prime-factor statement for $q_n$: such a
statement supplies one large prime, while (20) asks for the total multiplicity
of all small primes.  Nor does irreducibility of the Bessel polynomial in its
polynomial variable control prime factors of the fixed specialization
$q_n=(-1)^n y_n(-2)$.

## 6. Scope of identified primary literature

The following primary papers are relevant but do not contain the missing
valuation estimate in (20):

* D. H. Lehmer, [“Arithmetical periodicities of Bessel functions”](https://doi.org/10.2307/1968107),
  *Annals of Mathematics* **33** (1932), 143–150, concerns modular
  periodicities.
* M. Filaseta and O. Trifonov,
  [“The irreducibility of the Bessel polynomials”](https://doi.org/10.1515/crll.2002.069),
  *J. reine angew. Math.* **550** (2002), 125–140, concerns polynomial
  irreducibility/Newton polygons, not the factorization of $y_n(-2)$.
* J. Cullinan and N. Scheel,
  [“On the arithmetic of Padé approximants to the exponential function”](https://arxiv.org/abs/2007.01329),
  studies irreducibility, Galois groups, and Newton polygons of the Padé
  polynomials, not smooth factors of this specialization.
* F. Luca, [“Prime divisors of binary holonomic sequences”](https://doi.org/10.1016/j.aam.2006.12.001),
  *Advances in Applied Mathematics* **40** (2008), 168–179, gives results on
  the set of primes occurring across initial segments of holonomic sequences;
  this is not a termwise or prime-power smooth-part estimate.

The logical non-implications above are important: even an arbitrarily strong
lower bound on the largest prime factor, or a primitive-divisor theorem, leaves
$\mathcal E_X(n)$ unrestricted and hence cannot by itself prove the needed
$o(n\log n)$ bound.

## 7. Certificate

`scripts/bessel_denominator_zero_gap_smooth_radical_barrier_certificate.py`
checks the recurrence period, every gap-capacity inequality for all odd primes
up to a selectable limit, the second anti-period congruence (12) and its four
base residues, the reflection and affine lift law through $p=79$, the
high-power examples in (21), the first singular anti-period lift (22), and the
exact three-adjacent $n=18$ valuation calculation.
