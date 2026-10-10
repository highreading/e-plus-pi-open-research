> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 214 — joint stable-phase eliminants and their gcd

Date: 2026-08-31

## 1. Scope and verdict

Item 212 associated to every stable Frobenius phase



$$
b\le k+2,\qquad r\equiv k=3s+2\pmod4                \tag{1.1}
$$



two reduced integer numerators $N_{g_1}(b,r),N_{g_0}(b,r)$.  Outside the
already classified support gaps,



$$
p\mid g_0(s),g_1(s)
 \iff p\mid N_{g_1}(b,r),N_{g_0}(b,r).                \tag{1.2}
$$



This item studies the gcd of those two numerators as $b$ moves.

**PROVED — exact common-term recurrence.**  The two Item 212 sums can be
rewritten as weighted sums of one hypergeometric term $T_h$, plus at most one
explicit endpoint.  The ratio $T_{h+1}/T_h$ is a rational product of six
linear factors.  This gives a second, independent construction of the joint
eliminants for every $b$ and residue $r$.

**PROVED — exact phase-feasibility congruence.**  If
$\sigma_r\in\{0,1,2,3\}$ is determined by $3\sigma_r+2\equiv r\pmod4$, then
every actual phase prime satisfies



$$
qp\equiv b+4+5\sigma_r\pmod {20}. \tag{1.3}
$$



This removes many prime divisors of the abstract eliminant gcd before any
cell calculation.

**PROVED — complete factorization at the mandatory exception.**  At
$(b,r)=(900,3)$,



$$
\begin{aligned}
 \gcd(N_{g_1},N_{g_0})={}&2^{449}\cdot911\cdot971\cdot991\cdot1031
 \cdot1051\cdot1091\\
 &\cdot1151\cdot1171\cdot1231\cdot1291\cdot2399.    \tag{1.4}
\end{aligned}
$$



The ten odd factors from $911$ through $1291$ are all $11\pmod {20}$ and
are phase-infeasible.  The phase requires $p\equiv19\pmod {20}$, leaving
exactly $p=2399$, which gives the required node



$$
(s,p,q,b,r,k)=(299,2399,1,900,3,899). \tag{1.5}
$$



**FINITE — complete factorization through $b=900$.**  For every
$0\le b\le900$ and all four residues, every eliminant-gcd factor is removed
by exact division by the primes at most $4b+100$; the residual is exactly
one.  Applying all phase inequalities and (1.3), the only feasible odd factor
in this bounded box is (1.5).  This is explicitly not extrapolated.

**PROVED — height remains globally inadequate.**  A direct denominator
clearing gives



$$
\log|N_a(b,r)|
 \le \log(b+2)+(b+1)\log2+{b+2\over2}\log(10(b+3)).  \tag{1.6}
$$



This is $O(b\log b)$ per phase.  Summed over $b$ comparable to $m$, it costs
$O(m^2\log m)$ and yields no linear coefficient.  It therefore neither
supplies nor excludes the missing
$0.1177979020165907632818384072\ldots$ per $m$.

**OPEN.**  No all-$b$ factorization or prime-localization theorem is proved.
The far phase region may still carry positive mass.  No Route-1 exponent and
no conclusion about $e+\pi$ is claimed.

## 2. Common-term form

Recall Item 212's stable normalized sums.  Put



$$
\alpha={3b+2+5r\over20},\qquad
 \delta={r-b-2\over4}.                               \tag{2.1}
$$



Using $(z)^{\downarrow h}=(-1)^h(-z)_h$ in Item 212's formula gives



$$
\Phi_{g_1}=
 \sum_h {b+1\choose r+4h}{(\alpha)_h\over(\delta)_h}, \tag{2.2}
$$





$$
\Phi_{g_0}=
 \sum_h {b\choose r+4h}{(\alpha)_h\over(\delta+1)_h}. \tag{2.3}
$$



Both sums stop at the largest nonnegative $h$ allowed by the binomial.  The
formal simultaneous support gaps remain $(b,r)=(0,2),(0,3),(1,3)$ and are
handled separately.

For $r\le b$, define



$$
T_h={b\choose r+4h}{(\alpha)_h\over(\delta)_h}. \tag{2.4}
$$



Then



$$
\boxed{
 {T_{h+1}\over T_h}=
 \left(\prod_{u=0}^{3}{b-r-4h-u\over r+4h+u+1}\right)
 {\alpha+h\over\delta+h}.}                           \tag{2.5}
$$



Furthermore,



$$
\Phi_{g_0}=\sum_h T_h{\delta\over\delta+h},          \tag{2.6}
$$



and, apart from a possible endpoint,



$$
\Phi_{g_1}=\sum_h T_h{b+1\over b+1-r-4h}.           \tag{2.7}
$$



The endpoint occurs exactly when $b+1-r$ is divisible by four.  It is the
term with $r+4h=b+1$ in (2.2), for which ${b+1\choose b+1}=1$ but the
corresponding ${b\choose b+1}$ in $T_h$ is zero.  Its exact value is



$$
{ (\alpha)_{(b+1-r)/4}\over
   (\delta)_{(b+1-r)/4}}.                             \tag{2.8}
$$



Equations (2.4)--(2.8) are the promised joint recurrence.  They are exact
rational identities, not a finite guess.  The checker reconstructs both
Item 212 fractions from this independent form.

The recurrence does not itself telescope to a proved small boundary
resultant.  In particular, the factor ceiling observed in the bounded scan
below is not promoted to an all-$b$ statement.

## 3. Phase feasibility modulo 20

The residue $r$ determines $s$ modulo four because three is invertible modulo
four:



$$
\sigma_r\equiv3(r-2)\pmod4,
 \qquad
 (\sigma_0,\sigma_1,\sigma_2,\sigma_3)=(2,1,0,3).     \tag{3.1}
$$



By definition of the Frobenius phase,



$$
qp=b+4+5s.                   \tag{3.2}
$$



Reducing (3.2) modulo twenty and using (3.1) proves



$$
\boxed{qp\equiv b+4+5\sigma_r\pmod {20}.}           \tag{3.3}
$$



For $q=1$, this gives one required residue class for $p$ modulo twenty.  For
$q=2$, it gives a class modulo ten; if the right side of (3.3) is odd, the
$q=2$ phase is impossible.  The congruence is necessary.  Positivity of
$s=(qp-b-4)/5$, $p>3s+2$, the definition of $q$, and stability (1.1) must
still be checked.

At $(b,r)=(900,3)$, $\sigma_3=3$, and the right side is



$$
900+4+15\equiv19\pmod {20}.  \tag{3.4}
$$



It is odd, so $q=2$ is impossible, while $q=1$ requires
$p\equiv19\pmod {20}$.  This proves the feasibility filtering used in (1.4).

## 4. Exact factorization at $b=900$

The two reduced numerators have 581 and 578 decimal digits for $g_1$ and
$g_0$, respectively.  Their 169-digit gcd is



$$
\begin{split}
7741269879124174381610291595774708181269272361968769193256374992372688347484605694656473900070056575078240654598768797841493748568433330077102389694794120351022242070528.
\end{split}                                           \tag{4.1}
$$



Repeated exact division gives (1.4), with residual one.  No probable-prime or
floating-point factorization is used; primality of the displayed factors is
checked by deterministic trial division.

The phase filter (3.4) removes



$$
911,971,991,1031,1051,1091,1151,1171,1231,1291,     \tag{4.2}
$$



all of which are $11\pmod {20}$.  The factor $2399$ is $19\pmod {20}$, and



$$
s={2399-900-4\over5}=299,\qquad k=899,\qquad b=k+1. \tag{4.3}
$$



The actual coefficient recurrence independently returns



$$
(g_0,g_1)=(0,0),\qquad
 (A_{k-3},A_{k-2},A_{k-1},A_k)=(7,-7,0,0)\pmod{2399}. \tag{4.4}
$$



Thus the mandatory cancellation is retained exactly.

## 5. Bounded complete factorization

For each of the 3,601 non-gap phase pairs with



$$
0\le b\le900,\qquad0\le r<4, \tag{5.1}
$$



the certificate computes the two reduced numerators, their exact integer gcd,
and divides that gcd by every prime at most $4b+100$, including full
multiplicity.  In every case the final residual is one.  Across the scan there
are 13,867 distinct phase-factor occurrences and 626,022 occurrences with
multiplicity.

Every odd factor is then subjected to the exact reconstruction



$$
s={qp-b-4\over5},\qquad q\in\{1,2\}, \tag{5.2}
$$



followed by all inequalities, the residue check, stability, and an independent
coefficient recurrence.  The complete feasible list is



$$
(b,r,p,q,s)=(900,3,2399,1,299). \tag{5.3}
$$



The largest factor-to-$b$ ratio in the scan is $2399/900$, attained at this
same node.

This section is a **FINITE theorem only through $b=900$**.  Neither the
ceiling $4b+100$ nor uniqueness (5.3) is asserted for $b>900$.

## 6. Height ledger and scoped no-go

The factors in each Pochhammer ratio in (2.2)--(2.3), after multiplying by
twenty, have absolute value at most $10(b+3)$ over the summation range.  There
are at most $(b+2)/4$ factors and at most $b+2$ summands.  Also



$$
{B\choose n}\le2^B\le2^{b+1}. \tag{6.1}
$$



Clearing by the product of all denominator factors and then reducing the
fraction can only decrease the numerator.  The deliberately loose bound with
twice the needed product length is



$$
|N_a(b,r)|
 \le(b+2)2^{b+1}[10(b+3)]^{(b+2)/2}.                \tag{6.2}
$$



Taking logarithms proves (1.6).  Consequently, on one fixed phase,



$$
\sum_{p\mid\gcd(N_{g_1},N_{g_0})}\log p=O(b\log b). \tag{6.3}
$$



This looks nontrivial locally but is unusable at the required global scale.
Summing (6.3) over $O(m)$ phases with $b\asymp m$ gives
$O(m^2\log m)$, much larger than the available linear exponent ledger.  It
does not bound the coefficient below the missing



$$
0.1177979020165907632818384072\ldots\quad\text{per }m. \tag{6.4}
$$



This is a scoped no-go for the eliminant height alone.  It does not show that
the actual common-prime set has positive mass, nor does it rule out a sharper
gcd factorization, congruence sieve, or recurrence invariant.

The fixed finite range $b\le900$, including the isolated factor $2399$, has
zero asymptotic rate by Item 212's identity



$$
10m+1-b=(5j+5-q)p.           \tag{6.5}
$$



No positive Route-1 coefficient is gained by the finite scan.

## 7. Certificate and status

The standard-library checker

    work/item214_stable_eliminant_gcd_certificate.py

performs these exact tasks:

1. reconstructs the stable sums from the common-term recurrence;
2. verifies the phase-feasibility congruence;
3. completely factors every eliminant gcd through $b=900$ by exact division,
   checking residual one;
4. applies all phase conditions and independently verifies the sole feasible
   node;
5. reproduces the full factorization (1.4);
6. checks the explicit height bound at declared checkpoints.

Canonical and replay JSON files are byte-identical.  The portable artifacts
are

    work/item214_stable_eliminant_gcd_report.md
    work/item214_stable_eliminant_gcd_certificate.py
    work/item214_stable_eliminant_gcd_certificate.json
    work/item214_stable_eliminant_gcd_certificate_replay.json
    work/item214_stable_eliminant_gcd_manifest.json
    work/item214_stable_eliminant_gcd_hashes.sha256

Status summary:

* **PROVED:** common-term recurrence (2.2)--(2.8).
* **PROVED:** phase-feasibility congruence (3.3).
* **PROVED:** full mandatory gcd factorization and feasibility filter.
* **FINITE:** complete factorization and unique feasible node through $b=900$.
* **PROVED:** $O(b\log b)$ height bound and its global inadequacy.
* **OPEN:** an all-$b$ factorization or prime-localization theorem, a
  sufficient linear-rate bound, the far phases, primitive contractions,
  $A_1$, the joint gate, a Route-1 exponent improvement, and $e+\pi$.
