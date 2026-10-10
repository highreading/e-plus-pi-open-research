> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact native output moment and the congruence-isolation barrier

Checked: 2026-08-27 UTC.

## 1. Verdict

Let



$$
u=1+x^2,\qquad t=1-x,\qquad
 {\cal T}P=(1-x)P'-xP,
$$



and, for $N\geq2$, write



$$
(1-i)^N=R_N+iI_N,\qquad
 a=-I_N,\qquad b=\frac{N!-R_N}{2},\qquad A=a+b.        \tag{1}
$$



This note concerns the sign-possible classes $I_N\leq0$, so
$a\geq0$, $b>0$, and $A>0$.  The native correction is



$$
K(x)=I_N-b(1-x).               \tag{2}
$$



Every admissible localizer has the form



$$
h(x)=1+u^2q(x),\qquad q(0)=-1.                         \tag{3}
$$



Put $Q(t)=q(1-t)$.  The first theorem below reduces the entire variable
rational output to one moment:



$$
\boxed{
 \rho_{N,h}=C_N-4\int_0^1
 (a+bt)t(2-t)^2Q(t)\,dt,}                              \tag{4}
$$



where $C_N\in\mathbb Q$ is fixed once $N$ is fixed.  More precisely,
relative to the base localizer $h=1$, one has $C_N=\rho_{N,1}-5A$.

For a nearest-integer Bernstein expansion



$$
Q(t)=P(t)+\sum_{k=0}^n z_k t^k(1-t)^{n-k},\qquad
 P\in\mathbb Z[t],\ z_k\in\mathbb Z,                  \tag{5}
$$



the response of each $z_k$ is an explicit sum of four beta moments.
After multiplication by $L_{n+5}=\operatorname {lcm}(1,\ldots,n+5)$,
all responses are integers.  Thus denominator/content control is an exact
linear congruence problem in the $z_k$, followed by one nonlinear gcd.

Two rigorous barriers delimit what this observation supplies.

1. If every Bernstein coefficient is rounded to an independently prescribed
   residue class modulo $m_n$, the standard all-channel construction
   preserves $C^3$ approximation whenever $m_n=o(n)$.  This scale is sharp
   for a guarantee uniform over arbitrary residue patterns.  Since
   $\log L_{n+5}\sim n$, taking $m_n=L_{n+5}$ is far outside that theorem.
   This is a no-go for coefficientwise full-modulus rounding, not for every
   adaptive sparse or multichannel congruence construction.

2. More intrinsically, every sign-controlled primitive output gives a reduced
   rational $p/q$ in an interval of length

   

$$
\frac{5e-1}{(N+1)N!}.
$$



   For $N\geq14$, that interval contains at most one reduced rational with
   $q\leq\sqrt{N!}$.  Equivalently, among all sign-controlled outputs there
   is at most one rational approximant satisfying

   

$$
\frac{g_{N,h}}{D_{N,h}}\geq\sqrt{N!}.               \tag{6}
$$



   The stronger Roth-scale target is a subset of this isolated set.  Hence a
   continuum of real sign profiles and a high-dimensional coefficient lattice
   do not create a dense supply of Roth-scale candidates: a successful
   construction must hit the unique candidate, if it exists.

No such candidate is constructed or excluded here.  In particular, this note
does not prove an arithmetic classification of $e+\pi$.

## 2. Exact integration by parts

Let $P_N^{(0)}$ be the integral Taylor polynomial satisfying



$$
N!+{\cal T}P_N^{(0)}=(1-x)^N.
$$



The base polynomial $P_N^{(0)}+K$ is Robin.  The choice $h=1$ does not
satisfy $h(0)=0$; it is used here only as an algebraic reference coordinate.
Write that coordinate as



$$
\rho_{N,1}=-N!-(P_N^{(0)}+K)(0)
 +4\int_0^1\frac{(1-x)^N+{\cal T}K-N!}{u}\,dx.         \tag{7}
$$



The quotient in (7) is an integer polynomial of degree at most $N-2$, so
the reduced denominator of $\rho_{N,1}$ divides
$\operatorname {lcm}(1,\ldots,N-1)$.

Now put



$$
Y=u^2qK.                       \tag{8}
$$



Since $q(0)=-1$,



$$
Y(0)=-K(0),\qquad K(0)=-A.     \tag{9}
$$



The exponential part is a boundary term:



$$
\int_0^1e^x{\cal T}Y\,dx
 =[e^x(1-x)Y]_0^1=-Y(0)=K(0).                         \tag{10}
$$



For the rational part, integration by parts gives



$$
\begin{aligned}
 \int_0^1\frac{{\cal T}Y}{u}\,dx
 &=-Y(0)+\int_0^1(1-x)(1+x)^2q(x)K(x)\,dx\\
 &=K(0)+\int_0^1(1-x)(1+x)^2q(x)K(x)\,dx.             \tag{11}
\end{aligned}
$$



Indeed, if $f=(1-x)/u$, then



$$
\int fY'=[fY]_0^1-\int f'Y,
 \qquad
 -f'-\frac xu=\frac{(1-x)(1+x)^2}{u^2},
$$



and (11) follows from $Y=u^2qK$.  Combining (10)--(11), then substituting
$x=1-t$ and $K(1-t)=-(a+bt)$, yields



$$
\rho_{N,h}-\rho_{N,1}
 =5K(0)-4\int_0^1(a+bt)t(2-t)^2Q(t)\,dt.              \tag{12}
$$



Here the coefficient $5K(0)$ consists of the one exponential boundary term
in (10) and the four rational-kernel boundary terms obtained by multiplying
(11) by $4$.  This proves (4).

## 3. Exact Bernstein response ledger

Set



$$
W(t)=(a+bt)t(2-t)^2
 =\sum_{j=1}^4w_jt^j,                                 \tag{13}
$$



where



$$
(w_1,w_2,w_3,w_4)
 =(4a,\ 4b-4a,\ a-4b,\ b).                            \tag{14}
$$



For the raw Bernstein channel



$$
B_{n,k}^{\rm raw}=t^k(1-t)^{n-k},
$$



define its output response



$$
\boxed{
 R_{n,k}=4\int_0^1WB_{n,k}^{\rm raw}\,dt
 =4\sum_{j=1}^4w_j
 \frac{(k+j)!(n-k)!}{(n+j+1)!}.}                      \tag{15}
$$



Thus (4)--(5) become



$$
\rho_{N,h}=C_{N,P}-\sum_{k=0}^nR_{n,k}z_k,\qquad
 C_{N,P}=\rho_{N,1}-5A-4\int_0^1WP.                   \tag{16}
$$



The polynomial $WB_{n,k}^{\rm raw}$ has integer coefficients and degree at
most $n+4$.  Consequently



$$
M_{n,k}:=L_{n+5}R_{n,k}\in\mathbb Z.           \tag{17}
$$



If $n\geq\max(N,\deg P)$, the same $L_{n+5}$ clears $C_{N,P}$.  Put



$$
Z=L_{n+5}C_{N,P}-\sum_{k=0}^nM_{n,k}z_k\in\mathbb Z. \tag{18}
$$



Then



$$
d_0=\gcd(Z,L_{n+5}),\qquad
 c=Z/d_0,\qquad D=L_{n+5}/d_0,
 \qquad g=\gcd(N!,c).                                  \tag{19}
$$



Equations (18)--(19) are a replayable exact ledger for the reduced denominator
and primitive content.  They also show why a denominator congruence and a
content congruence cannot be conflated: cancellation against $L_{n+5}$ occurs
before the gcd with $N!$.

## 4. Congruence-constrained coefficientwise rounding

Let $r\in C^3[0,1]$ have zero jets through order three at both endpoints.
For each $n$, fix a modulus $m_n\geq1$ and arbitrary residue classes
$\eta_{n,k}\pmod {m_n}$ for $4\leq k\leq n-4$.  Choose



$$
z_{n,k}\equiv\eta_{n,k}\pmod {m_n},\qquad
 \left|z_{n,k}-r(k/n){n\choose k}\right|\leq\frac{m_n}{2},            \tag{20}
$$



and set the first and last four $z_{n,k}$ equal to zero.  Define



$$
\mathcal B_{n,m}r
 =\sum_{k=0}^nz_{n,k}t^k(1-t)^{n-k}\in\mathbb Z[t].    \tag{21}
$$



**Residue-rounding theorem.**  If



$$
m_n=o(n),                      \tag{22}
$$



then



$$
\|{\cal B}_{n,m}r-r\|_{C^3[0,1]}\longrightarrow0   \tag{23}
$$



uniformly over every choice of the residue pattern.  Conversely, the scale
(22) is necessary for a guarantee uniform over arbitrary residue patterns:
if $m_n/n\not\to0$, there are patterns for which even the zero function is
not approximated in $C^3$.

To prove the upper bound, compare (21) with the ordinary Bernstein polynomial.
Let



$$
e_k=z_{n,k}-r(k/n){n\choose k}.
$$



For $4\leq k\leq n-4$, $|e_k|\leq m_n/2$.  Three differentiations and
the identity



$$
\frac{(k)_j(n-k)_{3-j}}{{n-3\choose k-j}}
 =\frac{n(n-1)(n-2)}{{n\choose k}}                     \tag{24}
$$



give



$$
\left\|\left(\sum_{k=4}^{n-4}e_kB_{n,k}^{\rm raw}\right)'''\right\|_\infty
 \leq
 \frac{4m_n n(n-1)(n-2)}{{n\choose4}}
 =O\!\left(\frac{m_n}{n}\right).                      \tag{25}
$$



The zeroth, first, and second derivatives have smaller bounds.  The omitted
endpoint channels tend to zero in $C^3$ because $r$ has four zero jets.
Ordinary Bernstein polynomials approximate $r$ simultaneously through its
third derivative.  Equations (22)--(25) prove (23).

For sharpness, take $r=0$, set every residue to zero except at $k=4$, and
choose that class at distance at least $m_n/3$ from zero.  The resulting
error contains



$$
z_{n,4}t^4(1-t)^{n-4}.
$$



At $t=1/n$, direct scaling gives



$$
n\left\{t^4(1-t)^{n-4}\right\}'''_{t=1/n}
 \longrightarrow
 \left(y^4e^{-y}\right)'''_{y=1}=-e^{-1}.              \tag{26}
$$



Hence its $C^3$ norm is bounded below by a positive constant times
$m_n/n$.  This proves the uniform sharpness assertion.

The all-response clearing modulus satisfies



$$
\log L_{n+5}\sim n             \tag{27}
$$



by the prime number theorem in its Chebyshev-function form.  Therefore the
simple plan “prescribe every coefficient modulo $L_{n+5}$, then round to the
nearest representative” is not covered by (23), and the sharpness example
shows that no guarantee uniform over arbitrary such patterns is possible.
Adaptive use of a few central channels can have exponentially more local
capacity and is expressly outside this restricted no-go.

## 5. Roth-scale candidates are isolated

Let $s=e+\pi$.  For a sign-controlled output, write



$$
L_{N,h}=N!s+\frac cD,\qquad (c,D)=1,\quad D>0,\qquad
 g=\gcd(N!,c).                                         \tag{28}
$$



Set



$$
p=-c/g,\qquad q=N!D/g.          \tag{29}
$$



Then $(p,q)=1$, and the exact raw bounds give



$$
\frac1{(N+1)N!}
 \leq s-\frac pq
 \leq\frac{5e}{(N+1)N!}.                              \tag{30}
$$



Thus every such $p/q$ belongs to an interval of length



$$
\Delta_N=\frac{5e-1}{(N+1)N!}.                \tag{31}
$$



Two distinct reduced rationals with denominators at most $Q$ are separated
by at least $1/Q^2$.  Since $e<3$, for $N\geq14$,



$$
\Delta_N<\frac{14}{(N+1)N!}<\frac1{N!}.              \tag{32}
$$



Taking $Q=\sqrt{N!}$, equations (31)--(32) prove:



$$
\boxed{
 \text{for }N\geq14\text{, at most one reduced }p/q
 \text{ from a sign output has }q\leq\sqrt{N!}.}       \tag{33}
$$



By (29), the denominator condition in (33) is exactly (6).  In particular,
for every fixed $\delta>0$, the Roth target



$$
q\leq(N!)^{1/2-\delta}
 \quad\Longleftrightarrow\quad
 \frac gD\geq(N!)^{1/2+\delta}                         \tag{34}
$$



lies in this isolated regime.

This theorem is an arithmetic sparsity statement, not an impossibility
theorem.  The interval may contain one such rational.  Proving that it does for
infinitely many $N$ would already give the Roth contradiction from the
preceding package; proving that it never does would be a new Diophantine result
about $e+\pi$.

## 6. Scope and replay

The sound conclusions are:

* the exact single-moment output formula (4);
* the exact beta-response and reduction ledger (15)--(19);
* the sharp $m_n=o(n)$ scale for uniform arbitrary coefficientwise residue
  rounding;
* the isolation theorem (33) for every $N\geq14$.

The note does **not** rule out adaptive central-channel congruences, correlated
rounding, or a construction tailored to the unique rational in (33).  It also
does not establish the primitive-decay threshold $D/g=o(N)$, the Roth
threshold (34), or any arithmetic classification of $e+\pi$.

The exact replay verifies (10)--(18), the factorial response identity (24),
the sharpness limit (26), reduced-coordinate normalization in representative
native cases, and the rational constants in the isolation theorem.  Finite
response-gcd tables are labeled diagnostic and are not extrapolated.

From the research directory run

    python3 scripts/common_kernel_native_output_bernstein_congruence_certificate.py
    sha256sum -c results/common_kernel_native_output_bernstein_congruence_hashes.sha256

The replay uses exact symbolic, integer, and rational CPU arithmetic.  No
hardware accelerator is useful, and RAM use remains negligible relative to the
available $50$ GiB.
