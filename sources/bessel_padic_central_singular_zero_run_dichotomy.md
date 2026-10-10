> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Central singular Bessel paths: bounded death or proportional zero runs

Checked: 2026-08-27 UTC.

## 1. The dichotomy

Let $p$ be an odd prime, and let $f_p:\mathbb Z_p\to\mathbb Z_p$
be the canonical interpolation of



$$
f_p(n)=(-1)^nq_n,
 \qquad
 q_0=q_1=1,
 \qquad
 q_n=(4n-2)q_{n-1}+q_{n-2}.
\tag{1}
$$



It is locally analytic and has the exact reflection symmetry



$$
f_p(-x-1)=f_p(x).
\tag{2}
$$



Put



$$
c=-\frac12,
 \qquad
 n_a=\frac{p^a-1}{2}\quad(a\geq1).
\tag{3}
$$



Then exactly one of the following alternatives holds.

1. **Bounded death.**  If $f_p(c)\ne0$, then

   

$$
\boxed{
   v_p(q_{n_a})=v_p(f_p(c))
   \quad\text{for every sufficiently large }a.}
   \tag{4}
$$



2. **Proportional singular runs.**  If $f_p(c)=0$, then there are an
   even integer $\mu\geq2$, an integer $h$, and $a_0$ such that

   

$$
\boxed{
   v_p(q_{n_a})=\mu a+h
   \quad(a\geq a_0).}
   \tag{5}
$$



The base-$p$ expansion of $n_a$ has exactly $a$ digits, all equal
to $(p-1)/2$.  Thus (5) makes the fixed integer representative $n_a$
a root modulo $p^{\mu a+h}$.  Above its last ordinary digit it has



$$
\boxed{(\mu-1)a+h+O(1)}
\tag{6}
$$



consecutive zero lift digits.  This is a rigorous mechanism for terminal
zero runs comparable to the digit depth.

The theorem is a dichotomy, not a claim that the second alternative
occurs.  The known central residue at $p=79$ dies at its first lift; no
prime is proved here to satisfy $f_p(-1/2)=0$.

## 2. Proof

Write $x=c+y$.  Reflection (2) becomes



$$
f_p(c+y)=f_p(c-y).
\tag{7}
$$



### 2.1 Nonzero central value

If $f_p(c)\ne0$, then $n_a\to c$ in $\mathbb Z_p$.  Hence



$$
f_p(n_a)\longrightarrow f_p(c).
\tag{8}
$$



For a convergent sequence to a nonzero $p$-adic limit, the valuation is
eventually the valuation of that limit.  Since the sign $(-1)^{n_a}$
is a unit, (8) proves (4).

### 2.2 Zero central value

Suppose $f_p(c)=0$.  The restriction of $f_p$ to the central residue
disk is not identically zero: it takes the nonzero integer values
$(-1)^nq_n$ at every nonnegative integer in that residue class.
Local analytic factorization therefore gives a finite multiplicity
$\mu\geq1$ and an analytic unit $U$ near zero such that



$$
f_p(c+y)=y^\mu U(y),
 \qquad U(0)\ne0.
\tag{9}
$$



Equation (7) forces $(-1)^\mu=1$, so $\mu$ is even and
$\mu\geq2$.

Now



$$
n_a-c=\frac{p^a}{2},
 \qquad v_p(n_a-c)=a.
\tag{10}
$$



Because $U(p^a/2)\to U(0)\ne0$, its valuation is eventually the fixed
integer



$$
h=v_p(U(0)).
\tag{11}
$$



Substitution of (10)--(11) in (9), followed by
$|f_p(n_a)|_p=|q_{n_a}|_p$, proves (5).

Finally,



$$
n_a=\frac{p-1}{2}\left(1+p+\cdots+p^{a-1}\right),
\tag{12}
$$



so its last nonzero digit is in position $a-1$.  Divisibility through
exponent $\mu a+h$ proves the run count (6).

## 3. Scope for the uniform Bessel-height problem

The ordinary branch identity



$$
v_p(q_n)=v_p(n-\rho)
\tag{13}
$$



reduces long runs to exceptional rational-integer approximation of a
simple root $\rho$.  The present theorem shows that the singular central
branch has a different possible mechanism: analytic multiplicity alone
would multiply the digit depth.

Even (5) remains far below the forbidden $n_a\log n_a$ scale, because



$$
v_p(q_{n_a})\log p=O(\log n_a)
\tag{14}
$$



for fixed $p$ and fixed multiplicity.  Its importance is narrower: it
rules out every proposed universal bound of the form
$v_p(q_n)\leq\log_p n+O(1)$ unless central multiple zeros are first
excluded, and it characterizes exactly what an infinite central singular
branch would do.

No uniform bound in varying $p$, no exclusion of
$f_p(-1/2)=0$, and no statement about $e+\pi$ is proved.

## 4. Certificate

The companion script

    scripts/bessel_padic_central_singular_zero_run_dichotomy_certificate.py

checks the exact base-$p$ truncation identity (12) and the valuation/run
formula for finite synthetic even-multiplicity local models.  The analytic
dichotomy is proved in Section 2; the models are regression checks rather
than evidence that the Bessel central value vanishes.
