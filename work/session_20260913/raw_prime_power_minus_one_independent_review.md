> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the odd-prime-power-minus-one extension

Date: 2026-09-13. Reviewer: audit_sources.

**PASS.** The complete note
raw_prime_power_minus_one_denominator_extension.md correctly extends
the independently reviewed ternary proof to every odd prime:


$$
\boxed{n=p^\nu-1\quad\Longrightarrow\quad
 v_p(q_n)=\frac{p^\nu-1}{p-1}-\nu,\qquad \nu\ge1.}
$$


No repair, new canonical computation, or prime scan is needed.
The subsequently added Section 6 also **PASSES**: it supplies a wholly
all-index proof and removes the frozen $n=8$ case as a dependency.
This review checks the changes from the full detailed audit in
raw_ternary_factorial_denominator_independent_review.md; its exact
integral identities and signs apply unchanged.

## 1. Unit pole, triangular block and cofactor normalization

Set $T=p^\nu=n+1$. The inequalities
$T\le3n<3T\le pT$ prove $v_p(L)=\nu$, also for $p=3,\nu=1$.
The only positive odd multiple of $T$ below $3n$ is $T$.
Thus $\lambda=L\tau_T$ is the sole unit Taylor value.

In the original $\mathsf Z$, lengths $s\ge p$ have a rising
factor divisible by $p$. For $s<p$, the coefficient reduces to
$(r)_s^{\rm rise}$, because
$\binom{T-1}s=(-1)^s\pmod p$. This gives the claimed support
$j=r+s-1$. Row zero vanishes. The block of rows $1,\ldots,n$
is upper triangular with unit diagonal. When $\nu=1$, the final
retained index $s=p-1=n$ is still within the original summation,
so the formula has no missing boundary term.

It follows that $\delta_0,\Theta$ are units, all $\delta_r$,
$r>0$, vanish modulo $p$, and the scalar endpoint sum has
row-zero value one. Therefore $K$ is a unit. Both $n$ and
$2n$ have base-$p$ digit sum $\nu(p-1)$, proving
$v_p(R)=n/(p-1)\ge1$. All weighted minors have a factor $p$,
so $d_p=v_p(h)\ge1$ in the original primitive normalization.

## 2. Cauchy determinant and full lift precision

The exact integer identities $Y=H\mathsf Z=C+TE$ and
$\det Y=hV(1)$ use no special property of three. In the additional-row
pure Cauchy matrix the deleting-row-zero minor is again a unit.
The same signed cofactor ratio is $1/Q_n(0)$, with


$$
Q_n(0)=\frac{\binom n{n/2}}{\binom{2n}n}.
$$


The numerator has valuation zero: $n/2$ has all digits
$(p-1)/2$. The denominator has exactly $\nu$ carries.
Hence $v_p(\det C)=\nu$.

The adjugate modulo $p$ is supported solely at $(n-1,0)$.
The exact correction entry is the same integer sum as in the
ternary proof. For $1\le s<p$,


$$
v_p\binom{T-1+s}s=\nu:
$$


the numerator contains $T$ once and its remaining factors, and
the denominator $s!$, are units. Whenever $\tau_{s+1}\ne0$,
$v_p(L\tau_{s+1})\ge\nu-1$. Thus every such correction
term has valuation at least $2\nu-1\ge1$. At $s=p$ the
Taylor coefficient is zero because $p+1$ is even. At $s>p$,
$(s-1)!$ supplies a factor $p$, with $L\tau_{s+1}$
integral. This handles the complete summation through $s=T$.

Consequently the linear determinant correction vanishes modulo
$p^{\nu+1}$; all higher terms contain $p^{2\nu}$, which
suffices even for $\nu=1$. The conclusion


$$
v_p(hV(1))=\nu,\qquad 1\le d_p\le\nu
$$


is exact. No field-rank statement is silently promoted to full
prime-power depth.

## 3. Numerator and every boundary case

The identity $D_{n,r}\equiv1\pmod{n+1}$, with primitive integer
$V_r$, gives


$$
\widehat P_e(1)\equiv V(1)\pmod{p^\nu}.
$$


Because $v_p(V(1))=\nu-d_p<\nu$, it follows that
$e_p=\nu-d_p$. Thus the full gate
$\kappa_p=0,\ d_p+e_p=\nu$ holds at every stated $p,\nu$.

One has $\lfloor\log_p(2n)\rfloor=\nu$, since
$T\le2(T-1)<pT$. The retained arctangent loss is therefore
exactly $\nu$. If $n/(p-1)>2\nu$, that term is strictly
deeper than the exponential numerator, and four is a unit.
Actual endpoint reduction then subtracts $\nu-d_p$ from
$n/(p-1)-d_p$, proving the displayed formula.

The inequality holds for $p\ge5,\nu\ge2$ and
$p\ge3,\nu\ge3$: its initial sums are respectively
$1+p\ge6>4$ and $1+3+9=13>6$, and the inequality persists
on increasing $\nu$. For $\nu=1$, $d_p=1$ is forced by
the determinant, and $v_p(Z_n)=0$. Thus the denominator
valuation is zero regardless of possible numerator cancellation,
exactly the asserted answer. The single remaining case
$(p,\nu)=(3,2)$ is the frozen $n=8$ case, independently
re-reduced in raw_ternary_prefix_independent_checks.json.

For a given $n$, $n+1$ cannot be a power of two different primes.
The note correctly forbids combining these separate families into
a many-prime bound at one index. It also retains that no estimate
for all even indices follows.

## 4. Extra arctangent power: independently checked addendum

The actual cofactor polynomial and its scale are exactly


$$
\mathscr P(z)=\sum_{r,s=0}^n(-1)^{r+s}\binom ns\delta_r
 (n+r+1)^{\overline s}z^{2n-r-s},\qquad
 h\widehat Q=R\mathscr P.
$$


I checked this against equations (6)--(7) of
raw_endpoint_scalar_cauchy_restriction.md; no common factor or sign
has changed. Every exponent is nonnegative. All terms with $r>0$
vanish modulo $p$, and every term with $r=0,s>0$ contains
$n+1=T$ in the rising factorial. Hence
$\mathscr P\equiv\delta_0z^{2n}\pmod p$ as an integer polynomial.

Let $\mathcal T_a(P)=[P\arctan z]_{\le2n}(1)$. Its value on a
monomial of degree $j$ is a sum of arctangent coefficients of
indices at most $2n-j$. Thus all its denominators have $p$-depth
at most $\nu$, and $p^\nu\mathcal T_a$ is an integral linear
functional on the entire $\mathbb Z_p$-coefficient module, not
merely on the actual polynomial. It annihilates $z^{2n}$ exactly.
Writing $\mathscr P=\delta_0z^{2n}+pJ$, $J$ integral, proves


$$
v_p(\mathcal T_a(\mathscr P))\ge1-\nu,\qquad
 v_p(\widehat P_a(1))
 \ge\frac n{p-1}-d_p-\nu+1.
$$


The extra power therefore survives the exact $R/h$ scaling.
For every odd $p$ and $\nu\ge2$,
$1+p+\cdots+p^{\nu-1}\ge2\nu$; the right side is now strictly
greater than $e_p=\nu-d_p$, including the equality case
$(p,\nu)=(3,2)$. For $\nu=1$, the unit-$Z$ argument already
applies. Thus all indices are proved algebraically. The frozen
prefix remains a correct optional normalization check only.
