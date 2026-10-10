> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 213: the actual beta Hensel digit is a carry-minus-slope phase

Date: 2026-08-31 (Beijing time)

## 1. Verdict

Retain the actual beta denominator and companion



$$
q_0=q_1=1,\qquad q_N=(4N-2)q_{N-1}+q_{N-2},
$$





$$
P_0=1,\quad P_1=3,\qquad
P_N=(4N-2)P_{N-1}+P_{N-2}.
$$



Introduce the monic integer polynomial



$$
\boxed{
\mathscr C_N(X)=\sum_{j=0}^N{N\choose j}X^{\underline j},
\qquad
X^{\underline j}=X(X-1)\cdots(X-j+1).}                 \tag{1.1}
$$



It is a Charlier-type polynomial with the exact actual-seed
specialization



$$
\boxed{\mathscr C_N(-N-1)=(-1)^Nq_N.}                  \tag{1.2}
$$



Now let



$$
p>2N+1,\qquad p\mid q_N,\qquad s=p-1-N>N,
$$



and define the legitimate integer carry and slope



$$
\kappa_{p,N}:={\mathscr C_N(s)\over p}\pmod p,
\qquad
d^-_{p,N}:=\mathscr C_N'(s)\pmod p.                    \tag{1.3}
$$



The first divided value and the actual reverse-Bessel Hensel digit have
the exact formulas



$$
\boxed{
{q_N\over p}\equiv(-1)^N(\kappa_{p,N}-d^-_{p,N})\pmod p,} \tag{1.4}
$$





$$
\boxed{
\tau_{p,N}\equiv
P_N(\kappa_{p,N}-d^-_{p,N})\pmod p.}                   \tag{1.5}
$$



Here $\tau_{p,N}=(-1)^NP_N(q_N/p)$ is exactly the actual-seed
coordinate of Item 207.  Since $P_N$ is a unit at every root of
$q_N$, (1.5) gives the all-prime phase criterion



$$
\boxed{
p^2\mid q_N
\iff \kappa_{p,N}=d^-_{p,N}\pmod p.}                  \tag{1.6}
$$



The slope is completely explicit in binomial and harmonic terms:



$$
\boxed{
d^-_{p,N}=\sum_{j=1}^N{N\choose j}s^{\underline j}
       (H_s-H_{s-j})\pmod p.}                          \tag{1.7}
$$



All denominators in (1.7) are nonzero modulo $p$.

There is a useful two-sided refinement.  Since



$$
\mathscr C_N(s)=\mathscr C_s(N),
$$



the lower and reflected upper values share the same carry.  Put



$$
d^+_{p,N}:=\mathscr C_s'(N)\pmod p.
$$



Then, with $\epsilon=(-1)^N=(-1)^s$,



$$
\boxed{
\lambda_N={q_N\over p}=\epsilon(\kappa-d^-),\qquad
\lambda_s={q_s\over p}=\epsilon(\kappa-d^+)\pmod p.} \tag{1.8}
$$



If $D_h$ is the symmetric-continuant derivative of Item 165, where



$$
h={p-3\over2}-N,
$$



the exact adjacent/resultant factorization of the slope gap is



$$
\boxed{
d^+_{p,N}-d^-_{p,N}
=-2(-1)^ND_hq_{N-1}\pmod p.}                           \tag{1.9}
$$



Thus the three actual phases have the exact interpretation



$$
\boxed{
\begin{array}{c|c}
\text{condition}&\text{phase collision}\\
\hline
p^2\mid q_N&\kappa=d^-\\
p^2\mid q_s&\kappa=d^+\\
p\mid D_h&d^-=d^+\\
p^2\mid q_N\text{ and }p^2\mid q_s&\kappa=d^-=d^+.
\end{array}}                                           \tag{1.10}
$$



Equations (1.4)--(1.10) are proved for the actual normalization; no
formal seed or freely assigned local digit is used.

The result does **not** prove that the lower phase is nonzero.  In fact,
the sharp obstruction is now transparent:



$$
\kappa_{p,N}-d^-_{p,N}=(-1)^N{q_N\over p}\pmod p.     \tag{1.11}
$$



Consequently an all-prime nonvanishing theorem for this phase is exactly
the still-open large-prime squarefreeness theorem for the actual $q_N$.
The complementary-factorial calculation below shows that neither a
Wilson quotient nor a separate harmonic residue survives as an
additional first-Witt coordinate: both rewrites reduce to (1.11).

The adjacent factorization (1.9) also does not rule out the triple
collision.  The factor $q_{N-1}$ is a unit, but $D_h$ is a moving
resultant and can itself vanish modulo a prime in the target geometry.
Its height is too large to give a useful product bound.  Thus this item
produces an exact actual-family phase description and a precise scoped
obstruction, but no nonzero criterion, density theorem, or rate gain.

## 2. The Charlier realization -- PROVED

The exponential generating function of (1.1) is



$$
\boxed{
\sum_{N\ge0}\mathscr C_N(X){t^N\over N!}
=e^t(1+t)^X.}                                         \tag{2.1}
$$



Indeed, after interchanging the finite sums, the contribution of the
falling factorial of order $j$ is



$$
{X^{\underline j}t^j\over j!}e^t.
$$



It follows either from (2.1), or directly from falling-factorial
identities, that



$$
\mathscr C_0=1,\qquad \mathscr C_1=X+1,
$$





$$
\boxed{
\mathscr C_{N+1}(X)
=(X-N+1)\mathscr C_N(X)+N\mathscr C_{N-1}(X).}         \tag{2.2}
$$



For the actual specialization, use



$$
(-N-1)^{\underline j}
=(-1)^j{(N+j)!\over N!}.
$$



Then



$$
\begin{aligned}
\mathscr C_N(-N-1)
&=\sum_{j=0}^N(-1)^j{(N+j)!\over j!(N-j)!}\\
&=(-1)^N\sum_{k=0}^N(-1)^k
          {(2N-k)!\over k!(N-k)!}\\
&=(-1)^Nq_N.
\end{aligned}                                         \tag{2.3}
$$



The last sum is the reverse-Bessel formula for the actual denominator
from Item 204.  Thus (1.2) is not a modified-seed representation: its
special value is exactly the denominator with $(q_0,q_1)=(1,1)$.

## 3. Exact Taylor phase and Hensel digit -- PROVED

Because $s-p=-N-1$, equations (1.2) and the exact finite Taylor
expansion give



$$
(-1)^Nq_N
=\mathscr C_N(s-p)
=\sum_{r=0}^N{(-p)^r\over r!}\mathscr C_N^{(r)}(s).
                                                               \tag{3.1}
$$



Every Taylor coefficient in (3.1) is an integer: $\mathscr C_N$ has
integer coefficients and is expanded between integer arguments.  Hence



$$
(-1)^Nq_N
\equiv\mathscr C_N(s)-p\mathscr C_N'(s)\pmod {p^2}.   \tag{3.2}
$$



The root condition $p\mid q_N$ makes $\mathscr C_N(s)/p$ an
integer.  Divide (3.2) by $p$ to obtain (1.4).

The actual Wronskian is



$$
P_Nq_{N-1}-P_{N-1}q_N=2(-1)^{N-1}.                    \tag{3.3}
$$



At an odd root prime, (3.3) shows that $P_N$ and $q_{N-1}$ are
units.  Multiplying (1.4) by $(-1)^NP_N$ proves (1.5), and unitness
of $P_N$ proves (1.6).

This is also a direct evaluation of the unique reverse-Bessel Hensel
lift from Item 204.  It does not appeal to separability or to the
reverse-Bessel discriminant: it computes the missing divided value in an
actual binomial coordinate.

## 4. Harmonic form and Wilson cancellation -- PROVED

Since $s>N$, every factor in $s^{\underline j}$, $j\le N$, is a
positive integer below $p$.  Ordinary logarithmic differentiation of
a falling factorial gives



$$
{d\over dX}X^{\underline j}\bigg|_{X=s}
=s^{\underline j}\sum_{r=0}^{j-1}{1\over s-r}
=s^{\underline j}(H_s-H_{s-j}).                       \tag{4.1}
$$



Substitution in (1.1) proves (1.7).  Although (1.7) is written with
harmonic numbers, it is the residue of an ordinary integer derivative.

One can also derive the same result by complementing every factorial in
the reverse-Bessel sum.  Put



$$
r=p-1-2N>0,
$$



so $r$ is even.  For $0\le a<p$, define the Wilson quotient



$$
W_p={(p-1)!+1\over p}.
$$



The exact first-Witt complement formula is



$$
\boxed{
(p-1-a)!\equiv{(-1)^{a+1}\over a!}
\{1+p(H_a-W_p)\}\pmod {p^2}.}                         \tag{4.2}
$$



Apply (4.2) to $a=r+k$ in the reverse-Bessel sum and put
$j=N-k$.  Because $r$ is even, all signs coalesce, and one obtains



$$
q_N\equiv-{1\over N!s!}
\left[
\mathscr C_N(s)
+p\{(H_s-W_p)\mathscr C_N(s)-\mathscr C_N'(s)\}
\right]\pmod {p^2}.                                   \tag{4.3}
$$



At a root, $\mathscr C_N(s)\equiv0\pmod p$.  Thus the Wilson term
in (4.3) vanishes after division by $p$, and the harmonic term reduces
to $-\mathscr C_N'(s)$.  Finally,



$$
N!s!=N!(p-1-N)!\equiv(-1)^{N+1}\pmod p.               \tag{4.4}
$$



Dividing (4.3) by $p$ and using (4.4) reproduces (1.4) exactly.

This is a useful negative conclusion.  The most direct attempt to expose
a Wilson/Fermat-type nonzero phase does not yield a second arithmetic
coordinate.  The Wilson quotient is killed by the root equation, and the
remaining harmonic sum is precisely the ordinary slope already present
in the Taylor formula.  This statement is restricted to the displayed
first-Witt complement calculation; it does not say that no deeper or
different identity can use Wilson-type arithmetic.

## 5. The mirrored carry and the exact phase triangle -- PROVED

For positive integers $N<s$,



$$
\begin{aligned}
\mathscr C_N(s)
&=\sum_{j=0}^N{N^{\underline j}s^{\underline j}\over j!}\\
&=\mathscr C_s(N).
\end{aligned}                                         \tag{5.1}
$$



Terms with $j>N$ in the last polynomial vanish at the integer
argument $N$.  Thus both orientations have the same integer value and
the same carry $\kappa$, but their derivatives need not agree.

The upper derivative has the explicit form



$$
\begin{aligned}
d^+={}&\sum_{j=1}^N{s\choose j}N^{\underline j}
                      (H_N-H_{N-j})\\
&+N!\sum_{j=N+1}^{s}(-1)^{j-N-1}(j-N-1)!{s\choose j}
\pmod p.                                               \tag{5.2}
\end{aligned}
$$



The second line is the derivative of the terms which vanish at $N$:



$$
{d\over dX}X^{\underline j}\bigg|_{X=N}
=N!(-1)^{j-N-1}(j-N-1)!,\qquad j>N.                   \tag{5.3}
$$



Since $N-p=-s-1$, apply the same Taylor proof to
$\mathscr C_s(N-p)=(-1)^sq_s$.  The equality
$N+s=p-1$ makes $(-1)^s=(-1)^N$, proving (1.8).

Subtracting the two identities in (1.8) gives



$$
d^+-d^-=(-1)^N(\lambda_N-\lambda_s).                  \tag{5.4}
$$



The exact reflected divided-value identity of Items 165 and 207 is



$$
\lambda_N-\lambda_s=-2D_hq_{N-1}\pmod p.              \tag{5.5}
$$



Equations (5.4)--(5.5) prove (1.9).  Adjacent coprimality makes
$q_{N-1}$ a unit, so



$$
d^+=d^-\iff p\mid D_h.                                 \tag{5.6}
$$



The first two rows of (1.10) follow from (1.8), the third from (5.6),
and the fourth by combining them.  The coupled square is therefore a
literal collision of one actual carry with both actual complementary
slopes.

## 6. Adjacent/resultant factorization test -- exact, but not an exclusion

Equation (1.9) is the strongest natural adjacent factorization of the
derivative difference.  It removes $q_{N-1}$, which is a unit, but
leaves $D_h$.  Item 165 identifies



$$
D_h=\operatorname {Res}_X(X,\mathcal L_h(X^2)),
$$



where the odd symmetric continuant is



$$
\mathcal K_h(X)=X\mathcal L_h(X^2).
$$



The target inequality alone does not make this resultant a unit.  The
exact structural row



$$
h=2,\qquad D_2=963=3^2\cdot107,\qquad
N={107-2\cdot2-3\over2}=50                             \tag{6.1}
$$



has $107>2N+1$ and $107\mid D_2$.  It is **not** an actual beta
root: $107\nmid q_{50}$.  Thus (6.1) is not a square or coupled
example.  Its legitimate conclusion is narrower: there can be no
all-prime unit proof for the slope gap based only on the target range and
the continuant factor.

Moreover,



$$
\log|D_h|=2h\log h+O(h),                               \tag{6.2}
$$



and $h=(p-3)/2-N$ moves with $p$.  At the large-prime saddle scale,
this is a moving integer of height $\Theta(p\log p)$, not one fixed
small eliminant collecting all participating primes.  Therefore the
adjacent/resultant factorization neither proves $d^-\ne d^+$ for the
actual root family nor yields a useful product bound.

This is not a claim that the derivative equality merely restates the
lower square condition.  They are separate: $\kappa=d^-$ is the lower
square, while $d^-=d^+$ is the singular/continuant condition.  The
proved conclusion is that the available factorization does not exclude
their simultaneous triple collision.

## 7. Precise actual-family obstruction

The phase reduction is stronger than a formal local-data model in one
respect: every quantity in it is fixed by the actual integer polynomial
$\mathscr C_N$, the actual prime $p$, and the actual seed.  The carry
$\kappa$ cannot be assigned freely.

It is also exactly sharp.  Equation (1.11) says that the carry-minus-slope
phase is not a new necessary condition on a square prime; it is the
divided denominator itself in a different coordinate.  Therefore:

> Any proof that $\kappa_{p,N}\ne\mathscr C_N'(p-1-N)\pmod p$ at every
> prescribed actual root is already a proof that no prescribed actual
> square divisor exists.  Taylor expansion, harmonic differentiation,
> and the first complementary-factorial/Wilson expansion alone do not
> supply an independent residue with which to prove that inequality.

There is also no fixed-height collection hidden in (1.6).  Different
prime divisors of one $q_N$ evaluate $\mathscr C_N$ at the different
integers $p-1-N$, and the quotient by $p$ is part of the phase.  A
root-count estimate for the polynomial modulo $p$ does not control
which one of its $p$-adic lifts is selected by the distinguished
integer translate.

The obstruction is scoped.  It closes the direct first-order
Charlier/Taylor/complement route only.  A new theorem about the actual
carry sequence, cross-prime correlations, higher Witt digits, or a
different global eliminant could still succeed.

## 8. Radical and rate ledger

Define the full prescribed large-prime squarefull radical by



$$
S_N=\prod_{\substack{p>2N+1\\p\mid q_N\\
\kappa_{p,N}=\mathscr C_N'(p-1-N)}}p.                  \tag{8.1}
$$



Equation (1.6) proves that (8.1) is exactly



$$
S_N=\prod_{\substack{p>2N+1\\p^2\mid q_N}}p.
$$



Consequently the only unconditional product statement remains



$$
\boxed{S_N^2\mid q_N.}                                 \tag{8.2}
$$



For the paired/coupled radical, (1.10) gives



$$
R_N=\prod_{\substack{p>2N+1\\p\mid q_N\\
\kappa_{p,N}=d^-_{p,N}=d^+_{p,N}}}p,
\qquad R_N\mid S_N,                                    \tag{8.3}
$$



and again only



$$
R_N^2\mid q_N                                           \tag{8.4}
$$



is obtained.  The phase repackaging adds no third copy of a prime and no
new fixed divisor.  Its new bookable divisibility exponent and logarithmic
rate are both exactly zero.

At the archived balanced beta saddle, an $R_N^2$ gain would still need



$$
\log R_N>0.05889895100829538164\ldots\,m.               \tag{8.5}
$$



Nothing in (1.4)--(1.10) proves a positive lower bound, an $o(m)$
upper bound, or any bound below (8.5).  The exact selector (8.3) improves
the description of the candidate set, not its mass estimate.

## 9. Deterministic finite evidence

The standard-library checker performs four independent finite tests.

1. It constructs $\mathscr C_N$ over $\mathbb Z$ through $N=14$,
   checks (2.2), and verifies the exact specialization (1.2).
2. It checks the complementary-factorial congruence (4.2) for every odd
   prime through $251$, and directly compares the harmonic and ordinary
   derivatives at every prescribed root in that range.
3. For every prime $p\le20000$, it reconstructs $q_n\bmod p^2$ and
   $P_n\bmod p$, checks (1.4)--(1.10) at every prescribed lower root,
   and directly reconstructs both complementary polynomials through
   $p\le251$.
4. It replays the known actual square rows $(p,N)=(13,8),(7,79),(31,79)$.
   In all three, $\kappa=d^-$ exactly.  Every row violates
   $p>2N+1$, so none is a target-range example.

The prescribed census has 1,133 lower-root rows.  It finds:

- no lower square, hence no $\kappa=d^-$ collision;
- no derivative collision $d^-=d^+$, hence no singular row;
- no coupled triple collision;
- no zero lower derivative and no zero carry;
- the known upper square $(p,N,s)=(13,4,8)$;
- one zero upper derivative, at $(p,N)=(7,2)$, without a square.

All nonoccurrence and uniqueness assertions in this census are
**EXPERIMENTAL FINITE**.  They prove no all-prime nonvanishing, density,
finiteness, or radical theorem.

Several exact phase fixtures are



$$
\begin{array}{c|c|c|c|c|c|c}
p&N&\kappa&d^-&d^+&q_N/p&\tau\\ \hline
7&2&3&2&0&1&5\\
13&4&1&2&1&12&9\\
71&3&49&50&11&1&20\\
2879&48&1138&1769&1695&2248&766.
\end{array}                                             \tag{9.1}
$$



The last row is the actual target-range root used in Item 204's
coefficient-shift comparison.  Its nonzero phase confirms
$2879^2\nmid q_{48}$; it is not an all-prime argument.

## 10. Status ledger

### PROVED

- The Charlier-type realization (1.1)--(1.2), generating function, and
  recurrence.
- The exact actual-seed divided-value and Hensel phase (1.4)--(1.6).
- The explicit harmonic slope (1.7).
- The complementary-factorial expansion and first-Witt Wilson
  cancellation (4.2)--(4.4).
- The common carry, mirrored phase identities, and exact phase triangle
  (1.8)--(1.10).
- The adjacent/resultant factorization (1.9), including the conclusion
  that it leaves the moving $D_h$ obstruction.
- The exact radical selectors (8.1), (8.3), and the rate-neutral ledger:
  no new exponent and no new bookable logarithmic rate.

### EXPERIMENTAL FINITE

- The actual prescribed-root census through $p\le20000$.
- Direct two-orientation and continuant-gap checks through $p\le251$.
- Finite absence of lower-square, singular, and triple-collision rows in
  that range.
- The three known out-of-range square fixtures.

### OPEN

- Whether $\kappa_{p,N}-d^-_{p,N}$ is nonzero at every prescribed
  actual root.
- Whether any prescribed lower square or actual coupled square exists.
- Any all-prime theorem controlling the actual carries, slopes, or their
  cross-prime correlations.
- Any proper all-index upper bound for $S_N$ or $R_N$ below the
  square-capacity bound.
- All downstream mixed-coefficient, divided matching, saddle, and
  moving-CRT requirements.
- Irrationality, rationality, or transcendence of the target constant.

## 11. Portable artifacts

The source, checker, canonical result, replay result, and manifest archive
as

```text
sources/item213_beta_hensel_phase_report.md
scripts/item213_beta_hensel_phase_certificate.py
results/item213_beta_hensel_phase_certificate.json
results/item213_beta_hensel_phase_certificate.replay.json
results/item213_beta_hensel_phase_hashes.sha256
```

From the archive root, replay with

```text
python scripts/item213_beta_hensel_phase_certificate.py \
  --prime-limit 20000 \
  --output results/item213_beta_hensel_phase_certificate.replay.json
```

Canonical and replay JSON must be byte-identical.  The proof uses these
frozen inputs:

```text
d7b4475d2adfeff9a5f1c70a9c6b318d0c2b140bf90b194aa9acb6fdddcc2650  sources/item165_noncentral_singular_report.md
abbc68e283f16871798be0c6da8af5df55ba6bf865a5864eefc0f8e19fe88f62  sources/item202_actual_squarefull_filter_report.md
45ad273d407323902745095bd7abbc1fe5d17cf4d8da35737276eb3e6c7fc665  sources/item204_squarefull_discriminant_report.md
854a6b7fefc75e06913641a9e31e875e6b06ea31b2b6f7000da3b011b07be0a9  sources/item207_coupled_hensel_euler_report.md
```
