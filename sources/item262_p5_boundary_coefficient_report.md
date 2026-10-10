> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 262 - arithmetic of the $p\equiv5\pmod 6$ boundary coefficient

Checked: 2026-08-31 (Beijing time)

## 1. Scope and booking verdict

On an actual Item-260 row, put



$$
p=6q+5,\qquad \delta=\frac{r+2}{3},\qquad
m=q-\delta=s-1. \tag{1.1}
$$



Here $\delta$ is positive and odd. Define



$$
c_0=1,\qquad
c_j=\prod_{i=0}^{j-1}\frac{6i+5}{3i+4}\quad(j\ge1),\qquad
K_\delta=\sum_{j=0}^{\delta-1}c_j. \tag{1.2}
$$



Item 260 proved



$$
H_{q-\delta}=H_q-K_\delta h_q\pmod p. \tag{1.3}
$$



This item determines the recurrence, generating function, local valuations,
height, and numerator-gcd information of $K_\delta=B_\delta^{(5)}$.

> **PROVED - minimal order-two structure.** The exact recurrence is
> 

$$
> (3\delta+4)K_{\delta+2}-9(\delta+1)K_{\delta+1}
> +(6\delta+5)K_\delta=0,\qquad K_0=0,\quad K_1=1. \tag{1.4}
>
$$


> Its generating function is
> 

$$
> \sum_{\delta\ge0}K_\delta z^\delta
> =\frac{z}{1-z}\,{}_2F_1\!\left(1,\frac56;\frac43;2z\right). \tag{1.5}
>
$$


> There is no scalar order-one rational-ratio reduction. The order-two
> recurrence remains minimal after restriction to the actual odd values of
> $\delta$.

> **PROVED - reduced local arithmetic.** Every prime in the reduced
> denominator of $K_\delta$ is at most $3\delta-2$. Thus its denominator
> is a $p$-unit on every actual row, where $p\ge6\delta+5$. For every
> actual odd $\delta$,
> 

$$
> \boxed{K_\delta\equiv1\pmod3,\qquad v_3(K_\delta)=0.} \tag{1.6}
>
$$


> An exact reverse recurrence below gives the complete reduced
> $2$-adic numerator and denominator valuations, including the genuine
> cancellation in the odd section.

> **PROVED - fixed-$\delta$ numerator bound, but not a zero container.**
> If $K_\delta=A_\delta/B_\delta$ in lowest terms, then
> 

$$
> \log |A_\delta|=O(\delta),\qquad \log B_\delta=O(\delta). \tag{1.7}
>
$$


> Hence the log weight of primes dividing $A_\delta$ is $O(\delta)$
> for fixed $\delta$. However,
> 

$$
> H_{q-\delta}=0\quad\Longleftrightarrow\quad
> B_\delta H_q-A_\delta h_q=0\pmod p, \tag{1.8}
>
$$


> not $p\mid A_\delta$. Numerator divisibility of $K_\delta$ is
> neither necessary nor sufficient for the target zero.

> **PROVED - localization inside the full Item-251 affine target.** There
> is a second fixed rational $D_\delta$, defined in Section 6, such that
> 

$$
> A_s=(-1)^m\{\epsilon[H_q-D_\delta h_q]-1\}\pmod p. \tag{1.9}
>
$$


> Thus even after $K_\delta$ is completely localized, the second gate
> remains affine in the moving pair $(H_q,h_q)$, together with the
> row-dependent Item-251 coefficients.

> **POSITIVE-LINEAR-CAPACITY ADMISSION: FAIL.** The $K_\delta$-numerator
> condition misses actual $H_m$-zeros. Even if it were imposed, summing
> its $O(\delta)$ fixed-ray height over the linearly moving $\delta$'s
> gives only an $O(M^2)$ radical bound, whereas the raw ordinary-
> $j=2$ cell has log-prime mass
> 

$$
> \frac{2}{35}M+o(M). \tag{1.10}
>
$$


> No positive linear saving, all-prime exclusion, or full affine-gate
> theorem follows. Item 262 books
> 

$$
> \boxed{\text{new Route-1 rate}=0,\qquad
> \text{new \(j=2\) capacity reduction}=0.} \tag{1.11}
>
$$



Every bounded count and census below is **EXACT FINITE ONLY**.

## 2. Recurrence and generating function

The term is hypergeometric:



$$
c_j=2^j\frac{(5/6)_j}{(4/3)_j},\qquad
\frac{c_{j+1}}{c_j}=\frac{6j+5}{3j+4}. \tag{2.1}
$$



Because $K_{\delta+1}-K_\delta=c_\delta$, elimination of $c_\delta$
gives



$$
K_{\delta+2}-K_{\delta+1}
=\frac{6\delta+5}{3\delta+4}(K_{\delta+1}-K_\delta), \tag{2.2}
$$



which is (1.4). Also,



$$
C(z)=\sum_{j\ge0}c_jz^j
={}_2F_1\!\left(1,\frac56;\frac43;2z\right). \tag{2.3}
$$



Summing the prefixes gives (1.5). Equivalently,



$$
\sum_{\delta\ge1}K_\delta z^{\delta-1}=\frac{C(z)}{1-z}. \tag{2.4}
$$



### 2.1. Why order one is impossible

If $K_\delta$ had rational consecutive ratio, then
$R(\delta)=K_\delta/c_\delta$ would be rational and would satisfy



$$
\frac{6x+5}{3x+4}R(x+1)-R(x)=1. \tag{2.5}
$$



After clearing denominators, a finite pole orbit of $R$ must begin at
$1/6$, one step to the right of the zero of $6x+5$, and end at
$-4/3$, the zero of $3x+4$. Their difference is $-3/2$, not an
integer, so no pole orbit exists. Thus $R$ is a polynomial. A positive
degree gives an uncancelled leading term of degree one higher; a constant
would require simultaneously



$$
a(3x+1)=3x+4, \tag{2.6}
$$



which is impossible. This proves the claimed minimality for the full
sequence.

## 3. The actual odd section is still order two

Put



$$
L_N=K_{2N+1},\qquad N\ge0. \tag{3.1}
$$



Its increment is



$$
e_N=L_N-L_{N-1}=c_{2N-1}\frac{18N}{6N+1}\qquad(N\ge1), \tag{3.2}
$$



and



$$
\frac{e_{N+1}}{e_N}
=\frac{(12N-1)(12N+5)(N+1)}{(6N+4)(6N+7)N}
=\frac{A_N^*}{B_N^*}. \tag{3.3}
$$



Therefore



$$
B_N^*L_{N+1}-(A_N^*+B_N^*)L_N+A_N^*L_{N-1}=0. \tag{3.4}
$$



If $G(z)=zC(z)/(1-z)$, its generating function is the formal odd
section



$$
\sum_{N\ge0}L_Nt^N
=\frac{G(\sqrt t)-G(-\sqrt t)}{2\sqrt t}. \tag{3.5}
$$



An order-one reduction would give a rational solution of



$$
A_x^*R(x+1)-B_x^*R(x)=B_x^*. \tag{3.6}
$$



The possible left pole endpoints are



$$
\frac{13}{12},\quad\frac7{12},\quad0, \tag{3.7}
$$



and the possible right endpoints are



$$
-\frac23,\quad-\frac76,\quad0. \tag{3.8}
$$



The only integral pairing is the isolated point $0$, and its pole can
only be simple. Hence $R=a/x+P(x)$. Degree comparison makes $P=b$
constant. The cubic and constant coefficients force



$$
b=\frac13,\qquad a=-\frac5{99}, \tag{3.9}
$$



but the quadratic coefficient is then $402/11$, not the required
$66=726/11$. Thus (3.6) has no rational solution, proving minimality on
the actual odd section.

## 4. Exact reduced valuations

For any prime $\ell$, write



$$
\mu_{\ell,\delta}=\min_{0\le j<\delta}v_\ell(c_j),\qquad
u_{\ell,j}=\ell^{-v_\ell(c_j)}c_j\in\mathbf Z_{(\ell)}^*. \tag{4.1}
$$



Then the exact valuation, including all tied-minimum cancellation, is



$$
v_\ell(K_\delta)=\mu_{\ell,\delta}
+v_\ell\!\left(\sum_{j<\delta}
\ell^{v_\ell(c_j)-\mu_{\ell,\delta}}u_{\ell,j}\right). \tag{4.2}
$$



The reduced numerator and denominator exponents are respectively the
positive and negative parts of (4.2). This identity also explains why
termwise minimum valuations alone are insufficient when the minimum is
tied.

### 4.1. The prime $3$

Every factor in (1.2) is a $3$-adic unit and



$$
c_j\equiv(-1)^j\pmod3. \tag{4.3}
$$



For odd $\delta$, the alternating prefix is $1\pmod3$. This proves
(1.6), including the statement about the reduced numerator and
denominator.

### 4.2. The prime $2$

For $N\ge0$, put



$$
\mathcal A_N=N+\sum_{u=0}^{N-1}v_2(3u+2). \tag{4.4}
$$



The numerator factors in $c_j$ are odd. If $\delta=2N$, the final
term is the unique term of lowest $2$-adic valuation, and hence



$$
\boxed{v_2(K_{2N})=-\mathcal A_N.} \tag{4.5}
$$



Although even $\delta$ is not an actual row, (4.5) records the exact
interlacing valuation.

For the actual section, define



$$
R_0=1,\qquad
R_{j+1}=1+\frac{3j+4}{6j+5}R_j. \tag{4.6}
$$



Its denominator is odd and



$$
R_j=\frac{K_{j+1}}{c_j}. \tag{4.7}
$$



Consequently the complete exact formula is



$$
\boxed{v_2(K_{2N+1})=-\mathcal A_N+v_2(R_{2N}).} \tag{4.8}
$$



Thus



$$
\begin{aligned}
v_2(\operatorname{num}K_{2N+1})
 &=\max\{v_2(R_{2N})-\mathcal A_N,0\},\\
v_2(\operatorname{den}K_{2N+1})
 &=\max\{\mathcal A_N-v_2(R_{2N}),0\}.
\end{aligned} \tag{4.9}
$$



There are useful exact strata. With $T_N=R_{2N}/2$, the two-step form
of (4.6) is



$$
T_N=
\frac{9N(12N-7)+2(6N+1)(3N-1)T_{N-1}}
{(12N-1)(12N-7)}. \tag{4.10}
$$



Reduction modulo $2$ and $4$ gives



$$
v_2(R_{2N})=
\begin{cases}
1,&N\text{ odd},\\
2,&N>0\text{ and }N\equiv0\pmod4,\\
\ge3,&N\equiv2\pmod4.
\end{cases} \tag{4.11}
$$



The remaining deeper cancellations in the last line are computed exactly
by (4.6); no empirical closed formula is asserted. For example,



$$
K_3=\frac{59}{14},\qquad
K_5=\frac{175}{13},\qquad
K_7=\frac{4857283}{110656}. \tag{4.12}
$$



The cancellation at $K_5$ shows why a lowest-term-only denominator
claim would be false.

## 5. Denominator height and numerator gcds

For an odd prime $\ell\ne3$, each of the progressions $6i+5$ and
$3i+4$ occupies one residue class modulo $\ell^a$. In an interval of
length $j$, the counts in two residue classes differ by at most one.
Therefore



$$
|v_\ell(c_j)|\le\left\lfloor\log_\ell(6j-1)\right\rfloor. \tag{5.1}
$$



Let $\Lambda_n=\operatorname {lcm}(1,2,\ldots,n)$, let
$\Lambda_n^{\mathrm{odd}}$ denote its odd part, and put



$$
\mathcal B_j=\sum_{i=0}^{j-1}v_2(3i+4). \tag{5.2}
$$



A common denominator of $c_0,\ldots,c_{\delta-1}$ divides



$$
2^{\mathcal B_{\delta-1}}\Lambda_{6\delta}^{\mathrm{odd}}. \tag{5.3}
$$



Also $c_j<2^j$, so $K_\delta<2^\delta$. It follows that



$$
\begin{aligned}
\log B_\delta
&\le\mathcal B_{\delta-1}\log2+\psi(6\delta),\\
\log |A_\delta|
&\le(\mathcal B_{\delta-1}+\delta)\log2+\psi(6\delta).
\end{aligned} \tag{5.4}
$$



Counting the one residue class modulo each $2^a$ gives



$$
\mathcal B_{\delta-1}\le\delta-1+O(\log\delta). \tag{5.5}
$$



The standard Chebyshev bound $\psi(x)=O(x)$ proves (1.7).

The recurrence also gives a sharply scoped numerator-gcd theorem. If a
prime $\ell>6\delta+5$ divided both $A_\delta$ and
$A_{\delta+2}$, all coefficients and denominators in (1.4) would be
$\ell$-units. Equation (1.4) would force $K_{\delta+1}=0$, while



$$
K_{\delta+1}-K_\delta=c_\delta \tag{5.6}
$$



is an $\ell$-unit. This is impossible. Hence



$$
\boxed{\ell\mid\gcd(A_\delta,A_{\delta+2})
\quad\Longrightarrow\quad \ell\le6\delta+5.} \tag{5.7}
$$



This prevents two adjacent zeros in the odd $\delta$-section modulo one
large fixed prime. It does not propagate along actual global rows, because
the row prime changes when $\delta$ changes.

Large admissible prime divisors do occur:



$$
A_3=59,\qquad A_7=4857283=521\cdot9323. \tag{5.8}
$$



Thus there is no congruence-class exclusion of all actual primes from the
numerators.

## 6. Why $K_\delta$-divisibility does not control the target

Write $K_\delta=A_\delta/B_\delta$ in lowest terms. Since $B_\delta$
and $h_q$ are $p$-units, (1.3) gives (1.8). In particular,



$$
p\mid A_\delta\quad\Longrightarrow\quad H_{q-\delta}=H_q, \tag{6.1}
$$



not $H_{q-\delta}=0$.

Two exact rows prove independence in both directions:



$$
\begin{array}{c|c|c|c|c|c}
p&r&s&m&\delta&(H_m,K_\delta)\pmod p\\ \hline
47&7&5&4&3&(0,21)\\
59&7&7&6&3&(57,0).
\end{array} \tag{6.2}
$$



Thus $p\mid A_\delta$ is neither necessary nor sufficient for
$H_m=0$. This is a proved counterexample statement, not a density
inference.

### 6.1. Exact insertion into the Item-251 period

Put



$$
\Pi_\delta=
\sum_{k=1}^{3\delta}2^{-k}
\frac{(-\delta-1/3)_k}{(1/2)_k},\qquad
D_\delta=K_\delta+c_\delta\Pi_\delta. \tag{6.3}
$$



On $p=6q+5$, the backward quotient is



$$
h_{q-\delta}=c_\delta h_q. \tag{6.4}
$$



Also $m=q-\delta$, so termwise specialization gives



$$
P_{3\delta}(m)\equiv\Pi_\delta\pmod p. \tag{6.5}
$$



Indeed each factor in the $k$-th summand of $\Pi_\delta$ is



$$
\frac{3t-3\delta-1}{3(2t+1)},\qquad 0\le t<k. \tag{6.6}
$$



All numerator magnitudes and all prime denominator factors are below
$p\ge6\delta+5$, so no unit has been discarded. Combining (1.3),
(6.4), and (6.5) with Item 251 yields



$$
\boxed{
A_s=(-1)^m\{\epsilon[H_q-D_\delta h_q]-1\}\pmod p.} \tag{6.7}
$$



Consequently its exact period is



$$
Z=B_s\left[
\frac{9\kappa_r}{2}(-1)^m
\{\epsilon[H_q-D_\delta h_q]-1\}-\tau_{r,s}
\right]. \tag{6.8}
$$



On the half-binomial zero locus $H_m=0$, one has



$$
H_q=K_\delta h_q,\qquad
A_s=(-1)^m\{-\epsilon c_\delta\Pi_\delta h_q-1\}. \tag{6.9}
$$



The moving unit $h_q$ survives. The full target is still



$$
\mathbf G=\mathbf f Z+\mathbf U, \tag{6.10}
$$



with the separate Item-251 rank-zero branch retained. No valuation or gcd
statement for $K_\delta$ makes (6.10) nonzero.

## 7. Positive-linear-capacity test

For fixed $\delta$, (5.4) gives



$$
\sum_{p\mid A_\delta}\log p\le\log|A_\delta|=O(\delta). \tag{7.1}
$$



This is a valid fixed-ray divisor bound. It fails the Route-1 admission
test for three independent reasons.

1. Equation (6.2) proves that $p\mid A_\delta$ is not a container for
   the target zeros.
2. Even as a hypothetical container, summing (7.1) over
   $\delta\ll M$ gives $O(M^2)$, not $o(M)$ and not a positive
   linear saving against (1.10).
3. The recurrence and gcd theorem compare several $K$-values modulo one
   fixed prime, while neighboring actual global rows have different primes.
   Equation (6.8) also retains $h_q$ and the full affine row data.

Therefore neither the fixed-ray height, the odd-section recurrence, nor
the numerator gcd can be booked. This is a sharply scoped no-go for the
present $K_\delta$-arithmetic package; it is not a proof that every
future arithmetic method for the moving pair $(H_q,h_q)$ must fail.

## 8. Exact finite replay and strict labels

The standard-library checker verifies through $\delta\le127$:

- 127 full recurrence steps and 62 actual odd-section recurrence steps;
- every exact $2$-adic formula and stratum above;
- every actual $3$-adic unit identity;
- the common-denominator height container;
- 126 consecutive and 63 odd-distance-two numerator-gcd instances.

Through $p\le401$, it independently checks 605 actual
$p\equiv5\pmod6$ rows, including 2,420 localization equalities. The
bounded census finds one $H_m$-zero, two $K_\delta$-numerator zeros,
one affine determinant row, and no common gate. These counts and their
absence statements are **EXACT FINITE ONLY**.

### PROVED

- the recurrence, generating functions, and both minimality statements;
- the denominator support and exact valuation formulas;
- the linear height bound and numerator-gcd restriction;
- the fixed localization (6.7)-(6.8);
- the two independence counterexamples;
- the zero booking under the positive-linear-capacity test.

### EXACT FINITE ONLY

- every bounded count, sample list, and digest in the certificate.

### OPEN

- all-prime or weighted control of $H_q/h_q=K_\delta$;
- a positive-density theorem for the simultaneous Item-251 affine gate;
- any new Route-1 capacity or conclusion about $e+\pi$.

## 9. Reproduction

From the portable archive root:

```text
python scripts/item262_p5_boundary_coefficient_certificate.py \
  --output results/item262_p5_boundary_coefficient_certificate.json
python scripts/item262_p5_boundary_coefficient_certificate.py \
  --output results/item262_p5_boundary_coefficient_certificate_replay.json
```

The checker uses only Python's standard library and frozen Item-251 and
Item-260 dependencies. Its output contains no timestamp, random seed,
elapsed time, or host path.
