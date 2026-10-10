> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Primitive denominator depth when n+1 is an odd prime power

Date: 2026-09-13. Original extension by audit_computations of the ternary
row-difference proof. No new degree, matrix solve, or prime scan is used.
Independent audit: **PASS** by audit_sources; see
raw_prime_power_minus_one_independent_review.md.

## 1. Exact statement and scope

For every odd prime $p$ and every integer $\nu\ge1$, the actual
canonical reduced endpoint denominator satisfies



$$
\boxed{n=p^\nu-1\quad\Longrightarrow\quad
 v_p(q_n)=\frac{p^\nu-1}{p-1}-\nu.}
\tag{1}
$$



These indices are even. The notation and integral normalization are
exactly those of raw_ternary_factorial_denominator_subsequence.md and
the independently passed raw_fixed_prime_primitive_denominator_gate.md:



$$
Z_n=\widehat Q_n(1),\quad
 N_n=\widehat P_e(1)+4\widehat P_a(1),\quad
 q_n=|Z_n|/\gcd(|Z_n|,|N_n|),
$$




$$
hZ_n=RK,\quad R=(2n)!/n!,\quad
 V_r=(-1)^{n+r}c_r\delta_r/h,
 \quad c_r=(2n)!/(n+r)!.
\tag{2}
$$



The proof establishes the exact gate



$$
\boxed{v_p(\Theta)=v_p(K)=0,\qquad
 d_p+e_p=\nu,}
\tag{3}
$$



where $d_p=v_p(h/\Theta)$ and
$e_p=v_p(\widehat P_e(1))$. In particular, it controls actual endpoint
reduction. It does not merely exhibit a common cofactor divisor.

For a fixed $n$, the hypothesis $n+1=p^\nu$ cannot hold for two
distinct primes. Thus these individual prime-power-minus-one families
cannot be combined into a simultaneous many-prime lower bound at the
same indices. A general all-even estimate remains unproved.

## 2. Full ordinary cofactor rank at every odd prime

Put $T=p^\nu=n+1$, $L=\operatorname{lcm}(1,\ldots,3n)$, and
use the same integer matrix



$$
\mathsf Z_{rj}=L\sum_{s=0}^n(-1)^s\binom ns
 (n+r+1)_s^{\rm rise}\tau_{n+r+s-j},
 \quad 0\le r\le n,\ 0\le j<n.
\tag{4}
$$



We have $v_p(L)=\nu$, since $T\le3n<3T\le pT$. Among
positive indices at most $3n$, the only odd multiple of $T$ is
$T$. Therefore the only $p$-unit Taylor entry is
$\lambda=L\tau_T$.

For $s\ge p$, the rising factorial in (4) is divisible by $p$.
For $0\le s<p$,
$\binom ns\equiv(-1)^s\pmod p$ and
$(n+r+1)_s^{\rm rise}\equiv(r)_s^{\rm rise}\pmod p$.
Consequently



$$
\lambda^{-1}\mathsf Z_{rj}
 \equiv\sum_{s=0}^{p-1}(r)_s^{\rm rise}
 \mathbf1_{j=r+s-1}\pmod p.
\tag{5}
$$



Row 0 is zero, while rows $1,\ldots,n$ form an upper triangular
square matrix with diagonal one after division by $\lambda$.
Thus $\delta_0$ and $\Theta$ are units and every $\delta_r$,
$r>0$, is divisible by $p$. The endpoint row $v_r$ is the
same finite coefficient sum without the indicator; its row-0 value
is one. Therefore $K\equiv\delta_0\not\equiv0\pmod p$.

Also $c_0=R$ is divisible by $p$, so $d_p=v_p(h)\ge1$.
The base-$p$ digit sums of $n=T-1$ and $2n=2T-2$ are both
$\nu(p-1)$. Hence



$$
v_p(R)=\frac n{p-1}.
\tag{6}
$$



## 3. The row-difference determinant and its single correction

The exact identities (13)--(16) of the ternary proof hold over
$\mathbb Z$, independently of the prime. In the present notation,



$$
Y_{r,:}=\mathsf Z_{r,:}-(n+r+1)\mathsf Z_{r+1,:},
 \quad0\le r<n,
$$




$$
Y=C+TE,\quad C_{rj}=L\tau_{n+r-j},\quad
 E\in\operatorname{Mat}_n(\mathbb Z),\quad
 \det Y=hV(1).
\tag{7}
$$



The pure Cauchy matrix with its additional last row has a unit minor
deleting row 0. Its kernel is the monic imaginary-Legendre polynomial,
whose exact constant term is



$$
Q_n(0)=\binom n{n/2}/\binom{2n}n.
$$



The first binomial is a $p$-unit, because the digits of $n/2$
are all $(p-1)/2$, so adding it to itself has no carries. The second
binomial has valuation $\nu$, by the $\nu$ carries in adding
$n$ to itself. The cofactor ratio therefore gives



$$
v_p(\det C)=\nu.
\tag{8}
$$



The square $C\bmod p$ has only the entries
$\lambda\mathbf1_{j=r-1}$; its adjugate has only one possibly
nonzero entry, at $(n-1,0)$. The relevant correction is exactly



$$
E_{0,n-1}=L\sum_{s=1}^{T}(-1)^s(s-1)!
 \binom{T-1}{s-1}\binom{T-1+s}s\tau_{s+1}.
\tag{9}
$$



For $1\le s<p$, $\binom{T-1+s}s$ has valuation exactly $\nu$:
its numerator contains $T$ once, every other factor and the
denominator are units. Also
$v_p(L\tau_{s+1})\ge\nu-1$ when the Taylor entry is nonzero.
These summands have valuation at least $2\nu-1\ge1$.
The $s=p$ term is zero because $p+1$ is even. Every $s>p$
term is divisible by $p$ through $(s-1)!$, with all other factors
integral. Thus



$$
E_{0,n-1}\equiv0\pmod p.
\tag{10}
$$



The determinant expansion now gives



$$
\det Y\equiv\det C\pmod{p^{\nu+1}}.
\tag{11}
$$



Indeed the linear correction vanishes by the adjugate support and
(10), and all terms of order at least two contain $p^{2\nu}$, which
is divisible by $p^{\nu+1}$. Consequently



$$
\boxed{d_p+v_p(V(1))=\nu.}
\tag{12}
$$



This proves in particular $1\le d_p\le\nu$.

## 4. The endpoint numerator and primitive reduction

The all-integer identity



$$
D_{n,r}-1=(n+1)\sum_{j=1}^{n+r}(j-1)!
 \binom{n+j}{j-1}\binom{n+r}j
\tag{13}
$$



and the proved formula $\widehat P_e(1)=\sum_rV_rD_{n,r}$ give



$$
\widehat P_e(1)\equiv V(1)\pmod T.
$$



Since $v_p(V(1))=\nu-d_p<\nu$, it follows that
$e_p=\nu-d_p$. This proves the complete gate (3).

The unreduced endpoint and arctangent numerator obey



$$
v_p(Z_n)=\frac n{p-1}-d_p,
\quad
 v_p(\widehat P_a(1))\ge\frac n{p-1}-d_p-\nu,
\tag{14}
$$



where the second inequality is the passed denominator bound and uses
$\lfloor\log_p(2n)\rfloor=\nu$.

Whenever



$$
\frac n{p-1}=1+p+\cdots+p^{\nu-1}>2\nu,
\tag{15}
$$



the arctangent term is strictly deeper than the exponential numerator.
Because $p$ is odd, the factor 4 is a unit. Hence



$$
v_p(N_n)=\nu-d_p,
\quad
 v_p(q_n)=\frac n{p-1}-\nu.
\tag{16}
$$



Condition (15) holds for every $p\ge5,\nu\ge2$ and every
$p\ge3,\nu\ge3$. For $\nu=1$, (12) and $d_p\ge1$ force
$d_p=1$, so (14) makes $Z_n$ a $p$-unit; (1) is then zero
on both sides regardless of the numerator. The only remaining case
is $p=3,\nu=2,n=8$, whose already saved exact reduced denominator
has valuation 2, as independently verified in the cached fixed-prime
gate review. This completes (1).

## 5. Relation to the previous obstruction

The visible factorial $R$ does not survive untouched: precisely
$\nu$ powers of $p$ are lost in the actual reduced denominator.
The proof controls this loss through a row-difference determinant and
an exact integer numerator congruence. It does not assume cancellation
is absent in a sum merely because its displayed coefficients are positive.

The result applies when $n+1$ is a single odd prime power. An extension
to $n+1=mp^\nu$ would no longer have a single unit Taylor pole or a
single-coordinate adjugate correction; the associated finite Cauchy
blocks and their endpoint correction would have to be proved explicitly.
No such extension, and no all-even fixed-prime theorem, is claimed here.

## 6. An extra arctangent power removes the finite base input

The theorem also has a wholly all-index proof, without using the frozen
$n=8$ case. Use the actual integer cofactor polynomial



$$
\mathscr P(z)=\sum_{r,s=0}^n(-1)^{r+s}\binom ns\delta_r
 (n+r+1)_s^{\rm rise}z^{2n-r-s},\qquad
 h\widehat Q=R\mathscr P.
\tag{17}
$$



Every term with $r>0$ is divisible by $p$, by Section 2. At
$r=0,s>0$, the rising factorial contains $n+1=T$. Hence



$$
\boxed{\mathscr P(z)\equiv\delta_0z^{2n}\pmod p.}
\tag{18}
$$



Let $\mathcal T_a(P)=[P(z)\arctan z]_{\le2n}(1)$. Because
$\lfloor\log_p(2n)\rfloor=\nu$, the linear functional
$p^\nu\mathcal T_a$ is integral on $\mathbb Z_p[z]_{\le2n}$.
It vanishes on $z^{2n}$, since the arctangent series has zero
constant coefficient. Applying it to (18) proves



$$
v_p(\mathcal T_a(\mathscr P))\ge1-\nu,
\quad
 \boxed{v_p(\widehat P_a(1))\ge
 \frac n{p-1}-d_p-\nu+1.}
\tag{19}
$$



For every odd $p$ and every $\nu\ge2$,
$1+p+\cdots+p^{\nu-1}\ge2\nu$. Thus (19) is strictly larger
than $e_p=\nu-d_p$, including $p=3,\nu=2$. The numerator
reduction (16) follows for all $\nu\ge2$, while the $\nu=1$
unit-$Z$ argument is unchanged. The cached base cases in Section 4
remain correct normalization checks, but are no longer required inputs
to the theorem.
