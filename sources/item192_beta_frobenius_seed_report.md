> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 192: Frobenius-seed rigidity on beta root fibres

Date: 2026-08-30 (Beijing time)

## 1. Verdict

This note gives a sharply scoped obstruction, not an existence theorem for
useful primes.

Let



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2},
$$



and let the companion solution be



$$
\nu_0=1,\qquad \nu_1=3,\qquad
 \nu_n=(4n-2)\nu_{n-1}+\nu_{n-2}.
$$



The frozen beta identities give, for every prime $p\geq7$,



$$
q_{n+p}\equiv-q_n,\qquad \nu_{n+p}\equiv\nu_n\pmod p.       \tag{1.1}
$$



At an actual root $p\mid q_r$, set



$$
\lambda={q_r\over p},\qquad
 \delta={-q_{r+p}-q_r\over p}\pmod p.                       \tag{1.2}
$$



For every first-Witt seed perturbation



$$
u=q+p(aq+b\nu),\qquad a,b\in\mathbf F_p,                   \tag{1.3}
$$



the new divided coordinates satisfy



$$
\boxed{(\lambda_u,\delta_u)=(\lambda+c,\delta-2c),
        \qquad c=b\nu_r.}                                    \tag{1.4}
$$



Moreover $\nu_r\ne0\pmod p$.  Hence



$$
\boxed{I_p(r):=\delta+2\lambda
       ={q_r-q_{r+p}\over p}\pmod p}                         \tag{1.5}
$$



is the complete obstruction to making that fibre all-lift by a local
first-Witt seed change.  If $I_p(r)=0$, exactly $p$ of the $p^2$
seed lifts in (1.3) have $\lambda_u=\delta_u=0$.  If $I_p(r)\ne0$,
none does.

In particular, a singular dead actual fibre has $\delta=0$ and
$\lambda\ne0$, so $I_p(r)=2\lambda\ne0$.  **No first-Witt seed lift can
turn a singular dead actual beta fibre into an all-lift fibre.**  This is
the main proved no-go.

There is one necessary qualification.  An ordinary root can satisfy
$I_p(r)=0$.  The exact finite census finds the example



$$
(p,r,\lambda,\delta,\nu_r)=(7,2,1,5,5),                    \tag{1.6}
$$



for which seven locally modified seeds become all-lift.  This is a
modified-seed example, not an all-lift root of the actual denominator.
It therefore cannot be booked as arithmetic content for the fixed beta
linear form.

At higher seed digits the two Frobenius branches give a second exact
dichotomy.  The anti-Frobenius branch is invisible on a root fibre and
cannot tune the next divided digit.  A nonzero periodic branch injects the
representative-parity function $(-1)^T$, whose interpolation degree on
$T=0,\ldots,p-1$ is exactly $p-1$.  It therefore exits the fixed-degree
Newton architecture used for the actual seed.  Finally, one fixed integral
seed which reduces to $(1,1)$ at infinitely many primes is necessarily
the actual seed itself.  Prime-dependent local seed engineering is not an
infinite-prime mechanism for the fixed sequence.

No result here rules out actual noncentral singular or all-lift primes.
Their existence, positive logarithmic mass, mixed-coefficient divisibility,
saddle-index synchronization, matching, and a small moving-CRT
representative remain separate open requirements.

## 2. The Frobenius eigenbasis and its unit value — PROVED

Define



$$
W_n=\nu_nq_{n-1}-\nu_{n-1}q_n.
$$



Using the two recurrences once gives $W_n=-W_{n-1}$, while
$W_1=3\cdot1-1\cdot1=2$.  Thus



$$
\boxed{W_n=2(-1)^{n-1}.}                                    \tag{2.1}
$$



If $p\mid q_r$, reduction of (2.1) gives



$$
\nu_rq_{r-1}\equiv2(-1)^{r-1}\not\equiv0\pmod p.           \tag{2.2}
$$



Consequently $\nu_r$ and $q_{r-1}$ are units.  In particular, the
periodic coefficient $b$ in (1.3) ranges $c=b\nu_r$ through all of
$\mathbf F_p$.

Equation (1.1) is an imported frozen identity of the rank-one beta
architecture, including the companion-numerator period used in Items 164
and 169.  Item 192 does not infer (1.1) from its finite computation.  Its
new deductions begin with (1.1), and the manifest pins those sources.

## 3. First-Witt seed classification — PROVED

Every integral seed which reduces to the actual seed modulo $p$ has,
modulo $p^2$, the unique form (1.3).  Indeed $q,\nu$ are a basis modulo
$p$, since their initial-value determinant is $2$, a unit for odd $p$.

At $r$, equation $q_r\equiv0\pmod p$ gives



$$
{u_r\over p}\equiv {q_r\over p}+b\nu_r
 =\lambda+c\pmod p.                                         \tag{3.1}
$$



For the divided anti-period,



$$
\begin{aligned}
 {-u_{r+p}-u_r\over p}
 &\equiv\delta-a(q_{r+p}+q_r)-b(\nu_{r+p}+\nu_r)\\
 &\equiv\delta-2b\nu_r
 =\delta-2c\pmod p,
 \end{aligned}                                               \tag{3.2}
$$



where (1.1) was used in the second line.  This proves (1.4), and then
(1.5) is immediate.  Solving



$$
\lambda+c=0,\qquad\delta-2c=0                               \tag{3.3}
$$



shows that a simultaneous solution exists exactly when
$\delta+2\lambda=0$.  The value of $b$ is then unique and $a$ is
free, giving exactly $p$ solutions.

For a singular fibre, $\delta=0$.  Since $p$ is odd, (3.3) is solvable
if and only if $\lambda=0$ already.  Therefore a singular dead fibre is
rigidly dead under every first-Witt seed lift.  An actual all-lift fibre
remains all-lift for exactly the $p$ lifts with $b=0$.

The invariant criterion can also be read as the first divided periodicity
condition



$$
I_p(r)=0\quad\Longleftrightarrow\quad
 q_{r+p}\equiv q_r\pmod {p^2}.                               \tag{3.4}
$$



This is a new arithmetic condition on the actual seed; the theorem does
not show that it occurs infinitely often.

## 4. Higher seed digits: invisibility or degree $p-1$ — PROVED

Suppose a root fibre is divisible by $p^e$ at the level under study and
write its normalized signed function as



$$
F_q(T)={(-1)^Tq_{r+Tp}\over p^e}\pmod p,
 \qquad T=0,\ldots,p-1.                                      \tag{4.1}
$$



Change the seed at that digit by



$$
u=q+p^e(aq+b\nu).                                           \tag{4.2}
$$



Modulo $p$, the change in (4.1) is



$$
(-1)^T\{a q_{r+Tp}+b\nu_{r+Tp}\}
 \equiv b\nu_r(-1)^T.                                       \tag{4.3}
$$



The $q$-branch vanishes because $q_{r+Tp}\equiv(-1)^Tq_r=0$, while
the $\nu$-branch is periodic.  Thus the anti-Frobenius digit cannot tune
the normalized fibre at all.

For the values $\chi(T)=(-1)^T$, direct finite differencing gives



$$
\Delta^k\chi(0)=(-2)^k,\qquad0\leq k\leq p-1.               \tag{4.4}
$$



The last value is $1\pmod p$, by Fermat, so the unique interpolation
polynomial on $\mathbf F_p$ has degree exactly $p-1$.  Consequently,
if $b\ne0$, (4.3) has degree $p-1$, since $\nu_r$ is a unit.  It
cannot be absorbed into an actual-seed Newton polynomial of any fixed
degree less than $p-1$; in particular it cannot preserve the cubic
second-level law of Item 169 for $p\geq7$.

This is deliberately scoped.  It does not say that arbitrary modified
seeds have no higher roots.  It says that the branch which preserves the
anti-Frobenius architecture cannot tune the divided digit, while the branch
which can tune it destroys the uniform bounded-degree architecture on
which the archived root-count and modulus bookkeeping rely.

## 5. Why local seed choices do not make an infinite-prime mechanism — PROVED

Let $u$ be one fixed integral solution of the recurrence.  To be a lift
of the actual beta seed at a prime $p$, it must satisfy



$$
u_0\equiv1,\qquad u_1\equiv1\pmod p.                        \tag{5.1}
$$



If (5.1) holds for infinitely many primes, then the fixed integers
$u_0-1$ and $u_1-1$ each have infinitely many prime divisors.  Hence
both are zero and $u=q$.  The same statement holds for fixed rational
seeds after excluding the finitely many primes dividing their common
denominator.

The useful $b$ selected by (3.3) is generally prime-dependent, as is the
factor $p$ in (1.3).  Such local choices classify the tangent space of a
single fibre, but they do not alter the actual denominator and cannot
establish an infinite family of primes dividing the actual linear form.

## 6. Exact logarithmic-mass ledger — PROVED NECESSARY CONDITION

After the deliberately optimistic assumption that every eligible prime
at most $3m$ is fully doubled, the frozen normalized ledger still has
the gap



$$
G=0.01963298366943179388\ldots                               \tag{6.1}
$$



per $6m$.  If an additional radical $R_m$ contributes only an
$R_m^2$ gain, then



$$
{2\log R_m\over6m}>G
 \quad\Longleftrightarrow\quad
 \boxed{\log R_m>
 0.05889895100829538164\ldots\,m.}                            \tag{6.2}
$$



For comparison, an $R_m^3$ or $R_m^4$ gain would respectively require



$$
\log R_m>0.03926596733886358776\ldots\,m,
 \qquad
 \log R_m>0.02944947550414769082\ldots\,m.                   \tag{6.3}
$$



These are necessary mass thresholds, not evidence that an eligible
radical exists.

The logical requirements must remain separate.

1. An actual noncentral singular or all-lift root must exist.  A synthetic
   seed example does not imply this.
2. The root must occur at the chosen saddle-compatible index $N$.  Root
   existence at some residue does not imply this synchronization.
3. The actual mixed coefficient $b_m$ must have the required valuation.
   Dead singular equal-level matching uses $v_p(b_m)=v_p(q_N)=1$.
   An all-lift fibre has $v_p(q_N)\geq2$, so the first equal-level case
   requires at least $p^2\mid b_m$ and new divided data.
4. The appropriate divided coefficient congruence must hold at the same
   pair $(m,N)$.
5. The simultaneous moving CRT system must have a representative inside
   the shrinking saddle window.

No step implies the next.  In particular, if $R_N$ is the radical of
distinct actual all-lift primes at one fixed $N$, then



$$
\boxed{R_N^2\mid q_N.}                                      \tag{6.4}
$$



This is only an upper capacity bound
$2\log R_N\leq\log|q_N|$; it supplies no positive lower bound such as
(6.2).

## 7. Exact replay and finite evidence — EXPERIMENTAL FOR EXISTENCE

The deterministic certificate does the following.

1. It verifies the exact Wronskian recurrence through $n=80$.
2. For all primes $7\leq p\leq20000$, it reconstructs the actual
   sequences modulo $p^2$, checks both Frobenius branches, finds every
   actual root in $0\leq r<p$, and directly checks (1.4) on five fixed
   seed perturbations per root.
3. It checks the higher-branch interpolation statement on 64 root fibres
   and independently verifies (4.4) for every prime through $251$.

The finite census has 2,267 actual roots.  It finds:

- no actual all-lift root;
- only the known singular root $(p,r)=(79,39)$, which is central and
  dead, with $(\lambda,\delta,I)=(12,0,24)$;
- exactly one root with $I=0$, the ordinary modified-seed opportunity
  (1.6).

The archived exhaustive census through $p\leq200000$ likewise reports no
actual all-lift root and no noncentral singular root.  All absence
statements in this paragraph are **EXPERIMENTAL FINITE**.  They prove no
all-prime exclusion, finiteness, or density statement.

## 8. Status ledger

### PROVED

- The Wronskian identity (2.1) and the companion-unit property (2.2).
- The complete first-Witt seed law (1.4), invariant (1.5), and exact count
  of qualifying local seed lifts.
- The impossibility of converting a singular dead actual fibre into an
  all-lift fibre by a first-Witt seed perturbation.
- The higher-digit anti-branch invisibility and periodic-branch degree
  $p-1$ obstruction.
- Fixed-seed rigidity across infinitely many primes.
- The necessary mass threshold (6.2), the distinct logical eligibility
  stages, and the all-lift capacity bound (6.4).

### EXPERIMENTAL FINITE

- The exact census through $p\leq20000$, including the unique
  $I=0$ row (1.6).
- The pinned absence of actual all-lift and noncentral singular roots
  through $p\leq200000$.

### OPEN

- Whether the fixed beta seed has any noncentral singular root or any
  actual all-lift root.
- Whether useful actual roots have positive logarithmic radical mass, or
  even enough mass to meet (6.2) in the $R^2$ ledger.
- The necessary $b_m$-valuation, divided matching, saddle-index, and
  small-CRT synchronization at one sequence of pairs $(m,N)$.
- Any Dwork/Witt identity intrinsic to the actual seed which controls its
  higher divided digits without changing the seed.
- Irrationality, rationality, or transcendence of the target constant.

## 9. Artifacts and replay

The source artifact is
sources/item192_beta_frobenius_seed_report.md.  The deterministic replay is
scripts/item192_beta_frobenius_seed_certificate.py, and its canonical
output is
results/item192_beta_frobenius_seed_certificate.json.

From the archive root, run

    python scripts/item192_beta_frobenius_seed_certificate.py --output results/item192_beta_frobenius_seed_certificate.replay.json

The script's no-argument output is portable: beside the script while it is
in work/, and in ../results/ after archival under scripts/.  The manifest
uses archive-relative sources/, scripts/, and results/ keys and pins the
imported Item 164, Item 165, and Item 169 sources used above.

