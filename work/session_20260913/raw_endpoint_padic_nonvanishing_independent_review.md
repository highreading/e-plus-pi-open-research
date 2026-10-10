> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the endpoint limit nonvanishing criterion

Date: 2026-09-13. Reviewer: audit_results.

Target: raw_endpoint_padic_limit_nonvanishing_criterion.md, Sections 1–7.
The preceding integer constant-term representation, Gauss congruences,
limit precision and endpoint transfer have already passed independent
review. The finite-binomial primary references were opened and checked
directly for this audit.

**Verdict: FULL PASS.** The all-$m$ congruence modulo $p^2$,
including primes where the auxiliary quadratic algebra is nonsplit,
is proved without dividing by $A_m$. The nonvanishing criterion
for seed valuation zero or one, the endpoint consequences and the
Witt-coordinate limit representation all hold. The separate scope
of the Dwork analytic function is correct. No correction, new seed
calculation or degree/prime scan was needed.

## 1. Integer sequence and Dwork scope

The asymmetric Laurent polynomial $f(z)=2+z+2z^{-1}$ has the
same constant terms as the symmetric expression. Pairing its
positive and negative powers gives the exact sum (3).
Its generating function is


$$
\operatorname{CT}\frac1{1-tf(z)}
=\bigl((1-2t)^2-8t^2\bigr)^{-1/2}
=(1-4t-4t^2)^{-1/2},
$$


with constant coefficient one.

The Newton interval is exactly $[-1,1]$, with zero its only
interior integral point. Thus the hypotheses of Mellit–Vlasenko's
Theorem 1 hold. Their Lemma 2 applies on the domain where the first
truncation is a unit; near zero its limit agrees with the displayed
ratio of generating functions, with the corresponding formal
square-root branch. The note correctly distinguishes this function
limit from the individual coefficient-ray limit. A unit value of
one does not prove nonvanishing of the other.
[Primary source, Theorem 1 and Lemma 2](https://arxiv.org/pdf/1306.5811).

## 2. Finite-logarithm identity and both quadratic cases

Put $h=(p-1)/2$. The polynomial
$\mathfrak l(\alpha)+\mathfrak l(\beta)$, where
$\alpha+\beta=1,\alpha\beta=X$, belongs to $\mathbb F_p[X]$
and has degree at most $h$, by the recurrence for the symmetric
power sums.

In its function field, differentiate using
$\alpha'=-1/(\alpha-\beta)$, $\beta'=1/(\alpha-\beta)$.
Since
$\mathfrak l'(x)=(1-x^{p-1})/(1-x)$, the derivative is


$$
\frac{\alpha^p-\beta^p-(\alpha-\beta)}
     {X(\alpha-\beta)}
=\frac{(\alpha-\beta)^{p-1}-1}{X}
=\frac{(1-4X)^h-1}{X}.
$$


The numerator is divisible by $X$, so this is a polynomial identity,
including the apparent special points of the function-field calculation.
The coefficient congruence


$$
(-4)^j\binom hj\equiv\binom{2j}{j}\pmod p
$$


shows that it is exactly $S'(X)$. At $X=0$, the other
polynomial has constant term $\mathfrak l(0)+\mathfrak l(1)=0$.
Both degrees are below $p$, so their equal derivatives and
constant terms prove equality. This works also for $p=3$.

At $X=1/2$, one may work in the free étale algebra
$\mathbb Z_p[i]$ with $i^2=-1$, rather than assuming a square
root of $-1$ exists in $\mathbb Z_p$. The polynomial congruence


$$
\mathfrak l(x)\equiv
\frac{1-x^p-(1-x)^p}{p}\pmod p
$$


is obtained by dividing the binomial coefficients by $p$ before
specialization; every resulting coefficient is $p$-integral.

The exact identity


$$
\alpha^p+\beta^p=(2/p)\,2^{-(p-1)/2}
$$


follows by reducing the powers of $1+i$ and $1-i$ in the four
odd residue classes modulo eight. Its value $u$ is rational
and $u\equiv1\pmod p$, by Euler's criterion. Therefore
$u^2=(1+pq_p(2))^{-1}$ gives


$$
u\equiv1-\frac p2q_p(2)\pmod{p^2}.
$$


The residue $u\equiv1$ fixes the square-root choice. Substitution
in the finite-log identity proves (8) with the correct sign.
The omitted central-binomial terms above $h$ vanish modulo $p$;
their denominators $j$ and $2^j$ remain units.

I checked that Belbachir–Otmani Lemma 5, equation (12), states the
specialization for $p\ge5$, and Tauraso Section 3, equation (8),
states the underlying polynomial finite-log identity for $p>3$.
The note's independent proof supplies the additional $p=3$ case.
No unrelated assertions from either paper are required.
[Belbachir–Otmani](https://math.colgate.edu/~integers/x27/x27.pdf),
[Tauraso](https://cs.uwaterloo.ca/journals/JIS/VOL19/Tauraso/taur31.pdf).

## 3. The degree-$p$ correction

For $1\le j\le h$,


$$
\binom p{2j}=\frac p{2j}\binom{p-1}{2j-1}
\equiv-\frac p{2j}\pmod{p^2}.
$$


The integer constant-term sum then gives


$$
A_p\equiv2^p-p2^{p-1}
\sum_{j=1}^{h}\binom{2j}{j}\frac1{j2^j}
\equiv2+pq_p(2)\pmod{p^2}.
$$


This proves (9) and (10). The only divisions are by integers
prime to $p$.

## 4. All $m$, with no division by a vanishing seed

The Frobenius defect
$G=(f(z)^p-f(z^p))/p$ is an integer Laurent polynomial supported
on $[-p,p]$. Its three coefficients at multiples of $p$ are
exactly those in (11): the leading one is zero, the constant one
is $(A_p-2)/p$, and the trailing one is
$(2^p-2)/p=2q_p(2)$.

In the product $Gf(z^p)^{m-1}$, only these three coefficients
can contribute to the constant term. Hence the first-order
binomial expansion gives (12), with the coefficient of $z^1$
in $f^{m-1}$ attached to the trailing term of $G$.
Every higher term contains $p^2$, for arbitrary positive
integer $m$.

The exact symmetry $f(2/z)=f(z)$ gives
$[z^{-1}]f^{m-1}=2[z^1]f^{m-1}$, and multiplication by $f$
therefore yields
$A_m=2A_{m-1}+4B_{m-1}$.
Using the computed constant term of $G$ reduces the correction
to $mpq_p(2)A_m/2$, proving (1).

No step divides by $A_m$, assumes $m<p$, or assumes $p\nmid m$.
In particular the formula remains valid on the exceptional
residue $A_m\equiv0\pmod p$, which is essential for the new
valuation-one conclusion.

## 5. Limit and actual denominator consequences

The previously proved error
$\mathcal A_{m,p}-A_{mp}\in p^2\mathbb Z_p$
combines directly with (1) to give (14).
Its multiplying factor is $1\pmod p$.
Thus seed valuation zero or one is preserved in the limit, and
the limit is nonzero. For a seed of valuation at least two,
the congruence gives only divisibility by $p^2$; no persistence
of its full valuation follows.

For $3m<p$, the reviewed endpoint transfer resolves the
denominator depth whenever that depth is less than $\nu$.
This proves both lines of (15), including the strict threshold
$\nu\ge2$ when the seed valuation is one.
The statement for $A_4=8\cdot17$ therefore follows from the
degree-four seed alone. It agrees with the separate degree-68
certificate and does not rely on it.
The case $\nu=1$ correctly remains unresolved beyond its first
factor of $p$.

## 6. The actual algebraic unit and Witt-coordinate limit

The selected formal root


$$
H=\frac{1-2t+\sqrt{1-4t-4t^2}}2
$$


has constant coefficient one and satisfies
$H^2-(1-2t)H+2t^2=0$.
At every new coefficient, the linear multiplier is
$2H(0)-1=1$, proving integrality recursively without division
by two. Direct differentiation of this equation or of the selected
root gives $F-1=-tH'/H$.

Every formal unit in $1+t\mathbb Z[[t]]$ has the stated unique
Euler factorization, by successively cancelling its next coefficient.
Logarithmic differentiation is coefficientwise finite and gives


$$
A_n=\sum_{d\mid n}d\,b_d^{n/d}.
$$


For $p\nmid m$, all divisors of $mp^r$ are uniquely $ep^j$,
with $e\mid m$ and $0\le j\le r$. For fixed $j$, a unit
integer $b$ has $b^{p^{r-j}}\to\omega_p(b)$; if $p\mid b$,
the same powers tend to zero. Raising to the fixed positive
integer $m/e$ is continuous.

Every omitted term with $j\ge J$ is divisible by $p^J$,
uniformly in $r$, and the outer divisor set is finite.
This justifies taking the limit under the sum and proves (17).
The exact convergent representation is therefore sound.
It does not exclude cancellation among its terms, and the note
correctly avoids using real positivity as a $p$-adic sign
argument.

The proved new result is a uniform first-correction and nonvanishing
theorem for seed valuations at most one. It leaves higher valuations,
varying-prime bounds, and the original irrationality objective open.
