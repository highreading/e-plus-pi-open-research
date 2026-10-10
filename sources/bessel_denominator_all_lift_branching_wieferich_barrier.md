> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Prime-square branching for the Bessel denominator: exact law and a central Wieferich barrier

Checked: 2026-08-27 UTC.

## 1. Verdict

Let



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\ge2).
\tag{1}
$$



The first lift from a root modulo an odd prime to roots modulo its square is
completely explicit.  A root has either one lift, no lifts, or all $p$
lifts.  Reflection pairs every noncentral singular root with another singular
root and forces the central root $r=(p-1)/2$, whenever it exists, to be
singular.

There is no rigorous all-prime exclusion of the all-$p$ alternative here.
For a central root that alternative is exactly the supercongruence



$$
\sum_{j=0}^{(p-1)/2}\frac{(1/2)_j^2}{j!}\equiv0\pmod {p^2}.
\tag{2}
$$



Thus the attempted exclusion reaches a concrete truncated-hypergeometric
Wieferich-type question rather than a contradiction.  The sum in (2) is the
central specialization of the terminating ${}_2F_0$ representation of the
Bessel polynomial; calling the divisibility “Wieferich-type” describes the
extra lift from $p$ to $p^2$, not a claim that it is a classical
base-$a$ Wieferich congruence.

An exact exhaustive scan of every root for every odd prime $p\le200000$
finds no all-$p$ branch.  Its only singular root is the already known central
root $(p,r)=(79,39)$, and that root dies modulo $79^2$.  This is finite
evidence only.

The strongest immediate unconditional prime-power root-count estimate is



$$
\boxed{R_{p^a}\le p^{a-1}R_p\le2p^{a-1/3}},
\tag{3}
$$



where $R_{p^a}=|\{0\le r<p^a:p^a\mid q_r\}|$.  The factor $p^{a-1}$
cannot be removed from this argument while an all-$p$ branch remains
unexcluded.  Section 6 records exactly what (3) does and does not give for
excess valuations.

## 2. Exact first-lift trichotomy

Two previously proved congruences are the inputs.  For every odd prime $p$,



$$
q_{n+p}\equiv-q_n\pmod p
\tag{4}
$$



and



$$
q_{n+2p}+2q_{n+p}+q_n\equiv2p q_n\pmod {p^2}.
\tag{5}
$$



Let $r\in\{0,\ldots,p-1\}$ satisfy $p\mid q_r$, and define



$$
\delta_p(r)=\frac{-q_{r+p}-q_r}{p}\pmod p.
\tag{6}
$$



This is integral by (4).  Put



$$
a_t=(-1)^tq_{r+tp}.
$$



Equation (4) gives $p\mid a_t$.  After substituting in (5), its right side
is divisible by $p^2$, and hence



$$
a_{t+2}-2a_{t+1}+a_t\equiv0\pmod {p^2}.
$$



The initial values at $t=0,1$ therefore give



$$
\boxed{(-1)^tq_{r+tp}\equiv q_r+tp\delta_p(r)\pmod {p^2}.}
\tag{7}
$$



Consequently $r+tp$ is a root modulo $p^2$ precisely when



$$
\frac{q_r}{p}+t\delta_p(r)\equiv0\pmod p.
\tag{8}
$$



There is one solution when $\delta_p(r)\ne0$.  When
$\delta_p(r)=0$, there are no solutions if $p^2\nmid q_r$, and all
$p$ solutions if $p^2\mid q_r$.

For an exact root-count identity, define



$$
\begin{aligned}
 S_p&=|\{r:p\mid q_r,\ \delta_p(r)=0\}|,\\
 A_p&=|\{r:p^2\mid q_r,\ \delta_p(r)=0\}|,
 \end{aligned}
\tag{9}
$$



with $0\le r<p$.  Summing the three possible numbers of children gives



$$
\boxed{R_{p^2}=R_p-S_p+pA_p.}
\tag{10}
$$



Thus proving $A_p=0$ for all $p$ would imply
$R_{p^2}\le R_p$, but (10) itself does not prove that premise.

## 3. Reflection, pairing, and the forced central singularity

For every odd $M$, the exact reflection congruence is



$$
q_{M-1-s}\equiv q_s\pmod M.
\tag{11}
$$



Apply it with $M=p^2$.  If $r'=p-1-r$, reflection sends



$$
r+tp\longmapsto r'+(p-1-t)p.
$$



Because $p-1$ is even, the normalizing parity is unchanged.  Formula (7)
on the two fibers and (11) give



$$
q_r+tp\delta_p(r)
 \equiv q_{r'}+(p-1-t)p\delta_p(r')\pmod {p^2}.
\tag{12}
$$



Comparison of the coefficient of $t$, followed by the constant term,
gives



$$
\delta_p(r')\equiv-\delta_p(r)\pmod p,
\qquad
 q_r\equiv q_{r'}-p\delta_p(r')\pmod {p^2}.
\tag{13}
$$



In particular, singular roots occur in reflection pairs, with identical base
value modulo $p^2$, except possibly at the fixed point.  At
$r=r'=(p-1)/2$, (13) forces



$$
\boxed{\delta_p((p-1)/2)=0}
\tag{14}
$$



whenever the central class is a root modulo $p$.  It follows that a central
root necessarily dies at the first lift or produces all $p$ lifts.  This is
why an argument asserting that every root is Hensel-simple cannot work.

## 4. Exact central obstruction modulo $p^2$

Put $m=(p-1)/2$.  The explicit Bessel-denominator formula is



$$
q_m=(-1)^m\sum_{j=0}^m(-1)^j
       \frac{(m+j)!}{j!(m-j)!}.
\tag{15}
$$



For $1\le t\le j$, pair the two factors equidistant from the center:



$$
2(m+t)=p+(2t-1),\qquad
 2(m+1-t)=p-(2t-1).
\tag{16}
$$



Their product is



$$
(m+t)(m+1-t)=\frac{p^2-(2t-1)^2}{4}
 \equiv-\frac{(2t-1)^2}{4}\pmod {p^2}.
\tag{17}
$$



Since $j!$ is a unit modulo $p^2$, multiplication of the $j$ pairs
gives



$$
\frac{(m+j)!}{j!(m-j)!}
 \equiv(-1)^j\frac{((2j-1)!!)^2}{4^j j!}
 =(-1)^j\frac{(1/2)_j^2}{j!}\pmod {p^2}.
\tag{18}
$$



Substitution in (15) proves the exact congruence



$$
\boxed{
 q_{(p-1)/2}\equiv(-1)^{(p-1)/2}
 \sum_{j=0}^{(p-1)/2}\frac{(1/2)_j^2}{j!}\pmod {p^2}.}
\tag{19}
$$



Thus a central root occurs when the truncated ${}_2F_0$ sum vanishes
modulo $p$, and it has the all-$p$ branch exactly when the same sum
vanishes modulo $p^2$.  For the first central root,



$$
p=79,\quad m=39,\quad q_{39}\equiv948=12\cdot79\pmod {79^2},
\tag{20}
$$



so it dies.  Equation (19) exposes the obstruction exactly; it does not
exclude the possibility that another prime satisfies (2).

## 5. Unconditional root counts at all prime powers

The prime-power period theorem gives



$$
p^a\mid q_n\quad\Longleftrightarrow\quad
 p^a\mid q_{n\bmod p^a}.
\tag{21}
$$



If a class modulo $p^a$ is a root, its reduction modulo $p$ is a root
modulo $p$.  Every class modulo $p$ has exactly $p^{a-1}$ preimages
modulo $p^a$.  Therefore



$$
R_{p^a}\le p^{a-1}R_p.
\tag{22}
$$



The all-prime zero-gap theorem $R_p\le2p^{2/3}$ now proves (3).  This
argument is insensitive to whether the preimages actually arise by ordinary
lifting or by full branching; consequently it cannot improve the factor
$p^{a-1}$.

## 6. What this yields for excess valuations

There is a useful uniform estimate for the levels whose periods fit inside the
averaging interval.  On $[N,2N)$, define



$$
\mathcal E^{\rm low}_X(n)
 =\sum_{p\le X}\ \sum_{\substack{a\ge2\\p^a\le N}}
   {\bf1}_{p^a\mid q_n}\log p.
\tag{23}
$$



For $p^a\le N$, any interval of length $N$ meets at most



$$
\left(\frac N{p^a}+1\right)R_{p^a}
 \le\frac{2N R_{p^a}}{p^a}
 \le4N p^{-1/3}
$$



root classes.  For a fixed $p$, the number of exponents $a\ge2$ with
$p^a\le N$ is at most $\log N/\log p$.  Therefore



$$
\begin{aligned}
 \frac1N\sum_{n=N}^{2N-1}\mathcal E^{\rm low}_X(n)
 &\le4\log N\sum_{p\le\min(X,\sqrt N)}p^{-1/3}\\
 &\le \boxed{6N^{1/3}\log N}.
 \end{aligned}
\tag{24}
$$



This is $o(N\log N)$, uniformly in $X$.  It includes **all** exponents
with $p^a\le N$, not merely a fixed exponent cutoff.

The complementary tail is



$$
\mathcal E^{\rm high}_X(n)
 =\sum_{p\le X}\ \sum_{\substack{a\ge2\\p^a>N}}
   {\bf1}_{p^a\mid q_n}\log p.
\tag{25}
$$



Equivalently, with the same restriction $p\le X$, its $p$-summand is



$$
\left(v_p(q_n)-\max\{1,\lfloor\log N/\log p\rfloor\}\right)_+\log p.
$$



Here each residue class modulo the period occurs at most once in $[N,2N)$,
so the root-density argument loses its averaging gain.  This tail includes every square
$p^2>N$ and the high powers of the smaller primes.  Possible full branching
is precisely one mechanism by which the bound (3) fails to decay with $a$.
The size estimate $\mathcal E^{\rm high}_X(n)\le\log q_n=O(n\log n)$
only recovers an $O(N\log N)$ mean and is not the required little-oh bound.
Thus (24) isolates the moving high-level tail (25), rather than solving it.

For completeness, a fixed-cutoff density statement can also be made exact.
For fixed $X\ge3$ and integer $A\ge2$, put



$$
\mathcal E_{X,A}(n)
 =\sum_{p\le X}\min\{(v_p(q_n)-1)_+,A-1\}\log p
 =\sum_{p\le X}\sum_{a=2}^{A}{\bf1}_{p^a\mid q_n}\log p.
\tag{26}
$$



Periodicity makes the limiting mean exact:



$$
\lim_{L\to\infty}\frac1L\sum_{n=0}^{L-1}\mathcal E_{X,A}(n)
 =\sum_{p\le X}\log p\sum_{a=2}^{A}\frac{R_{p^a}}{p^a}.
\tag{27}
$$



By (3), every summand $R_{p^a}/p^a\le2p^{-1/3}$, so



$$
\boxed{
 \lim_{L\to\infty}\frac1L\sum_{n<L}\mathcal E_{X,A}(n)
 \le3(A-1)X^{2/3}\log X.}
\tag{28}
$$



Here we only enlarged the prime sum to the integers and used
$\sum_{m\le X}m^{-1/3}\le(3/2)X^{2/3}$.

For a finite interval of length $L$, the same residue-class count gives the
fully uniform but generally much weaker inequality



$$
\frac1L\sum_{n=N}^{N+L-1}\mathcal E_{X,A}(n)
 \le3(A-1)X^{2/3}\log X
 +\frac{2}{L}\sum_{a=2}^{A}\sum_{p\le X}p^{a-1/3}\log p.
\tag{29}
$$



The last term may, for example, be bounded by
$2(A-1)X^{A+2/3}\log X/L$.  This displays the lack of uniformity rather
than concealing it.

If one informally inserts $X\asymp N\log N$ only into the main term of
(28), that term is $o(N\log N)$ when



$$
A=o\!\left(\frac{N^{1/3}}{(\log N)^{2/3}}\right).
$$



But (28) takes $X,A$ fixed before $L\to\infty$, and the boundary term in
(29) is not useful in that moving range.  More importantly, the full excess
valuation has no cutoff in $a$.  Because (3) gives a density bound
independent of $a$, summing it over all exponents diverges.  Hence neither
(28) nor (29) proves the needed
$o(N\log N)$ mean bound for the full smooth prime-power content.  The
uniform low-level estimate (24) shows exactly that any remaining failure must
come from (25).

## 7. Exact finite certificate

The companion program

`scripts/bessel_denominator_all_lift_branching_certificate.cpp`

does the following with exact modular arithmetic:

1. sieves every odd prime through a selectable limit;
2. computes every $q_r\pmod {p^2}$ for $0\le r<p$ and retains every
   root modulo $p$;
3. computes $q_{r+p}\pmod {p^2}$, hence $\delta_p(r)$, for every root;
4. records every singular root and every all-$p$ branch;
5. checks that each central root has zero slope and checks (19) independently
   using the hypergeometric term ratio
   $T_j/T_{j-1}=(2j-1)^2/(4j)$.

The frozen run uses $p\le200000$.  It is an exhaustive statement only in
that finite range and is not used as a substitute for any all-prime proof.
Its frozen SHA-256 hashes are



$$
\begin{array}{c|c}
\text{certificate implementation}&
\mathtt{849e86b3bb26628261b8bb0bb9b457e1c9cec0a6823b94ebf3cfe94f9af02f92}\\
\text{result JSON}&
\mathtt{09a3622c5a4362127bddede30793b378765040da397d2e0dd50ca4cc50fdddf4}
\end{array}
$$



Compile and rerun with

    g++ -std=c++17 -O3 -march=native -Wall -Wextra -pedantic \
      scripts/bessel_denominator_all_lift_branching_certificate.cpp \
      -o /tmp/bessel_denominator_all_lift_branching_certificate
    /tmp/bessel_denominator_all_lift_branching_certificate \
      --prime-limit 200000 \
      --output /tmp/bessel_denominator_all_lift_branching_certificate.json
    cmp results/bessel_denominator_all_lift_branching_certificate.json \
      /tmp/bessel_denominator_all_lift_branching_certificate.json

Nothing in this note classifies $e+\pi$, and the all-prime all-lift question
remains open.
