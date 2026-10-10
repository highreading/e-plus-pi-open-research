> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The degree-205 lift in the $n=5$ two-log ideal content

Checked: 2026-08-26 UTC

## Verdict

The residue-class formula observed for $2\leq d\leq200$ is false in
all degrees.  Its first failure is $d=205$.  In the notation of Section 8
of `algebraic_unit_global_norm_rivoal.md`, put



$$
t=\zeta _5+\zeta _5^{-1},\qquad \delta=4-t.
$$



Then



$$
N_{\mathbb Q(\sqrt5)/\mathbb Q}(\delta)=19,
 \qquad
 \boxed{\mathfrak c_{205}=\delta^2\mathcal O_K},
 \qquad
 \boxed{N_{K/\mathbb Q}(\mathfrak c_{205})=19^4=130321}. \tag{1}
$$



The old finite pattern predicts only $19^2=361$, because
$205\equiv15\pmod {19}$.  Thus (1) is a strict counterexample, not a
new interpretation of the degree-200 record.

## Exact lattice certificate

Use the integral basis



$$
1,\quad t,\quad z=i(\zeta _5-\zeta _5^{-1}),\quad tz
 \tag{2}
$$



of $\mathcal O_K$.  Reconstruct the minimally rationally cleared
coefficients $u_{205},v_{205}$ from equations (51)--(53) of the companion
source.  Form the $4$ by $8$ integer matrix



$$
M_{205}=[M(u_{205})\mid M(v_{205})], \tag{3}
$$



where $M(a)$ is multiplication by $a$ in (2).  An exhaustive exact
gcd of all $k$ by $k$ minors of (3) gives the determinantal divisors



$$
\Delta_1=1,\quad \Delta_2=1,\quad
             \Delta_3=361,\quad \Delta_4=130321. \tag{4}
$$



Consequently the Smith invariants are



$$
(1,1,361,361). \tag{5}
$$



There is also a structural identification of the ideal, rather than only
its norm.  Since $t^2+t-1=0$,



$$
\delta^2=(4-t)^2=17-9t. \tag{6}
$$



For $a+bt\in\mathbb Z[t]$, exact division by $m-t$, whose norm is
$p=m^2+m-1$, is



$$
\frac{a+bt}{m-t}
 =\frac{a(m+1)+b}{p}+\frac{a+mb}{p}t. \tag{7}
$$



Applying (7) with $m=4$ to the two
$\mathbb Z[t]$-components in
$\mathcal O_K=\mathbb Z[t]\oplus z\mathbb Z[t]$ gives



$$
v_\delta(u_{205})=2,\qquad
 v_\delta((v_{205})_{\mathbb Z[t]})=12,\qquad
 v_\delta((v_{205})_{z\mathbb Z[t]})=3. \tag{8}
$$



Thus every generator in (3) is divisible by $\delta^2$, so
$\mathfrak c_{205}\subseteq\delta^2\mathcal O_K$.  Multiplication by
$17-9t$ has the same determinantal divisors (4).  The two sublattices
therefore have the same index, proving the ideal equality in (1).

All statements above are checked with integer arithmetic by
`scripts/algebraic_unit_two_log_n5_ideal_content_d205_counterexample.py`;
its result is
`results/algebraic_unit_two_log_n5_ideal_content_d205_counterexample.json`.

## What this changes

An all-degree identity with content bounded by $5^2 19^2$ would have
made the left side of the necessary condition



$$
\limsup_{d\to\infty}d^{-1}\log N(\mathfrak c_d)\geq\log\varphi
 \tag{9}
$$



equal to zero, and would therefore have ruled out cancellation of the
degree-four relative-norm growth by a common algebraic coordinate factor.
The degree-205 lift refutes that proposed identity.  It does **not** show
that (9) can hold: a bounded lift, a logarithmic valuation, or any other
subexponential replacement would still give limsup zero.

Exact scans show no prime other than $5$ and $19$ through $d=500$,
and the $19$-part at $d=205$ is the only failure of the old formula in
that range.  Those are finite diagnostics only.  In particular, neither a
replacement congruence law nor an all-degree subexponential bound is
claimed here.  The recurrence values can acquire prime divisors outside a
finite scan, so excluding later primes requires a proof, not extrapolation.

Nothing in this countercertificate proves either algebraicity or
transcendence of $e+\pi$.
