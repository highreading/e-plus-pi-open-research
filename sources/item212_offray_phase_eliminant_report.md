> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 212 — off-ray Frobenius phases and the stable-band eliminant

Date: 2026-08-31

## 1. Scope and verdict

This item continues Item 208's exact common-content problem.  Put



$$
k=3s+2,\qquad p>k,
$$



and, for an odd prime $p$, define



$$
q=\begin{cases}1,&p\ge 5s+4,\\2,&p<5s+4,\end{cases}
 \qquad b=qp-5s-4,\qquad r\equiv k\pmod4,\qquad0\le r<4.   \tag{1.1}
$$



Item 208 reduced the common-content condition to two coefficients of



$$
P_{s,b}(x)=(1-x^4)^{2s}(1-x)^{b+1}.                 \tag{1.2}
$$



The conclusions here are:

**PROVED — exact all-prime normalized phase formula.**  Both coefficients
are a nonzero binomial base times an explicit finite rational sum.  This is
valid for every $p>k$ and in both $q$ phases; see (2.5).

**PROVED — the only prime-feasible forced support gap is the old ray.**  The
only actual simultaneous support gap is



$$
b=0,\qquad r=3,\qquad q=1,
$$



or equivalently $s\equiv3\pmod4$ and $p=5s+4$.  Every other common-content
prime is a genuine cancellation.

**PROVED — a $b$-only integer eliminant in the stable band.**  If



$$
b\le k+2,                    \tag{1.3}
$$



then the two normalized sums reduce modulo $p$ to rational numbers depending
only on $(b,r)$.  After reducing those rationals, a common-content prime must
divide both explicit integer numerators $N_0(b,r),N_1(b,r)$.  Conversely,
divisibility of both numerators is equivalent to the two coefficient zeros.

The mandatory off-ray example lies inside this theorem:



$$
(s,p,k,q,b,r)=(299,2399,899,1,900,3),\qquad b=k+1.  \tag{1.4}
$$



Both eliminant numerators are divisible by $2399$, and the actual terminal
state is $(7,-7,0,0)$ modulo $2399$.

**PROVED — all slowly growing phase layers have zero Route-1 rate.**  On a
cell row,



$$
10m+1-b=(5j+5-q)p.           \tag{1.5}
$$



Consequently all layers $0\le b\le B(m)$ have total log-prime weight
$O((B+1)\log m)$.  In particular $B=o(m/\log m)$ contributes $o(m)$, hence
coefficient zero per $m$.

**PROVED — a scoped first-singularity no-go.**  Propagating the universal
terminal survivor to the first Frobenius singularity gives an exact necessary
scalar.  It is not sufficient: $(s,p,q,b)=(13,53,2,37)$ passes that scalar but
has $(g_0,g_1)=(4,5)$ modulo $53$.  Thus the terminal line plus the first
singular compatibility cannot classify the actual fixed initial orbit.

**OPEN.**  The far moving-$b$ cancellations are not bounded.  This item does
not prove a sublinear all-phase zero count, improve the Route-1 exponent, or
settle the arithmetic nature of $e+\pi$.

## 2. Exact coefficient normalization

For $a\in\{0,1\}$ define



$$
E_a=2s+a,\qquad B_a=b+1-a,
$$





$$
D_a=[x^k](1-x^4)^{E_a}(1-x)^{B_a}.                 \tag{2.1}
$$



Thus Item 208's two coefficients are



$$
D_0=g_1,\qquad D_1=g_0      \pmod p. \tag{2.2}
$$



Write



$$
t={k-r\over4}.               \tag{2.3}
$$



If $r>B_a$, then $D_a=0$ by support.  Otherwise set



$$
H_a=\min\left(t,\left\lfloor{B_a-r\over4}\right\rfloor\right). \tag{2.4}
$$



Expanding both factors in (2.1), putting the linear-factor degree equal to
$r+4h$, and dividing by the $h=0$ fourth-power binomial gives the exact
identity



$$
\boxed{
 D_a=(-1)^{t+r}{E_a\choose t}\Phi_a(s,b,r),
 }
$$





$$
\boxed{
 \Phi_a(s,b,r)=
 \sum_{h=0}^{H_a}(-1)^h{B_a\choose r+4h}
 {t(t-1)\cdots(t-h+1)\over
  (E_a-t+1)(E_a-t+2)\cdots(E_a-t+h)}.}               \tag{2.5}
$$



All displayed denominators are nonzero integers below $p$ on their actual
summation range, and $0\le t\le E_a<p$.  Hence the binomial base and every
denominator are $p$-units.  Therefore $D_a=0\pmod p$ exactly when
$\Phi_a=0\pmod p$.

This is more than a scan: it is a term-by-term identity for every admissible
$(s,p)$.

## 3. The complete support-gap classification

Both coefficients vanish by support exactly when



$$
r>b+1.                       \tag{3.1}
$$



Since $0\le r<4$ and $b\ge0$, the only formal pairs are



$$
(b,r)=(0,2),(0,3),(1,3).     \tag{3.2}
$$



They can be checked arithmetically without any asymptotics.

* If $(b,r)=(0,2)$, then $s\equiv0\pmod4$.  In the $q=1$ phase,
  $p=5s+4$ is even; in the $q=2$ phase, $p=(5s+4)/2$ is even.  Neither is an
  admissible odd prime.
* If $(b,r)=(1,3)$, then $s\equiv3\pmod4$.  The $q=1$ value is
  $p=5(s+1)$ and the $q=2$ value is $p=5(s+1)/2$; both are composite.
* If $(b,r)=(0,3)$, parity excludes $q=2$, while $q=1$ gives exactly
  $p=5s+4$ with $s\equiv3\pmod4$.

Thus the old structural ray is the unique prime-feasible simultaneous support
gap.  In particular, every off-ray common-content prime must arise through
cancellation in (2.5).

## 4. Stable-band elimination

Assume $b\le k+2$.  Then for both $a=0,1$,



$$
H_a=\left\lfloor{B_a-r\over4}\right\rfloor.         \tag{4.1}
$$



The summation range now depends only on $(b,r)$.  From (1.1), in
$\mathbb F_p$,



$$
5s=-(b+4).                   \tag{4.2}
$$



For $p>5$, substitute the rational number



$$
S_b=-{b+4\over5}                                    \tag{4.3}
$$



into the right side of (2.5), and write the reduced fraction as



$$
\Phi_a(S_b,b,r)={N_a(b,r)\over M_a(b,r)}. \tag{4.4}
$$



The denominator $M_a$ is a $p$-unit because it is congruent to the product of
the actual unit denominators in (2.5), up to powers of $4$ and $5$.  It follows
that, outside the already classified support gaps,



$$
\boxed{
 p\mid g_0(s),g_1(s)
 \iff p\mid N_0(b,r),N_1(b,r),\qquad b\le k+2.}      \tag{4.5}
$$



The isolated case $p=5$ is checked directly and is not a common zero.

This is a concrete eliminant, not a height surrogate.  For fixed $(b,r)$ it
replaces two coefficients whose original sizes grow with $s$ by two fixed
integers.  It does not, however, bound how often their prime divisors line up
with the moving relation $qp=5s+4+b$ as $b$ itself grows.

## 5. The off-ray example is a cancellation root of the eliminant

For (1.4), the cutoff in both sums is $224$.  Exact reduced-fraction
arithmetic gives



$$
N_0(900,3)\equiv N_1(900,3)\equiv0\pmod{2399},      \tag{5.1}
$$



while both denominators are nonzero modulo $2399$.  Independently, the exact
coefficient recurrence gives



$$
(g_0,g_1)\equiv(0,0),\qquad
 (A_{k-3},A_{k-2},A_{k-1},A_k)\equiv(7,-7,0,0).      \tag{5.2}
$$



The reduced eliminant numerators have 578 and 581 decimal digits (the ordering
is $g_0,g_1$).  Their gcd has 169 digits and is divisible by $2399$.  The
certificate records hashes rather than printing those large integers in the
report.

This mandatory example is therefore fully retained.  It is not mislabeled as
a support gap or discarded as an exceptional computation.

## 6. First-Frobenius compatibility is not enough

Use Item 205's recurrence



$$
(n+1)A_{n+1}=(5s+3)(A_n+A_{n-1}+A_{n-2})+(n-3s)A_{n-3}. \tag{6.1}
$$



A common zero forces



$$
(A_{k-4},A_{k-3},A_{k-2},A_{k-1},A_k)
 =T(0,1,-1,0,0).                                    \tag{6.2}
$$



Normalize $T=1$ and propagate (6.1) from $n=k$ through $n=p-2$.  At
$n=p-1$ division by $n+1=p$ is unavailable.  Hence a necessary compatibility
condition is



$$
\mathcal H_{s,p}:=(5s+3)(W_{p-1}+W_{p-2}+W_{p-3})
 +(p-1-3s)W_{p-4}=0\pmod p.                          \tag{6.3}
$$



The pair $(299,2399)$ passes (6.3).  But (6.3) is not sufficient.  At



$$
(s,p,q,b,r)=(13,53,2,37,1), \tag{6.4}
$$



the propagated survivor also has $\mathcal H_{s,p}=0$, whereas the actual
fixed-initial-state orbit has



$$
(g_0,g_1)=(4,5)\pmod{53}.    \tag{6.5}
$$



This is an actual-family false positive: it uses the exact recurrence and its
actual parameters, not a mock height sequence.  It proves a precise scoped
no-go.  An argument based only on the terminal line and first singular
solvability cannot classify common content.  A global invariant retaining the
initial state $A_0=1$ is not excluded.

## 7. Phase overlap and Route-1 rate

The cell equation is



$$
2m+1=(j+1)p-s.               \tag{7.1}
$$



Multiplying by $5$ and using $qp=5s+4+b$ yields



$$
\boxed{10m+1-b=(5j+5-q)p.}                          \tag{7.2}
$$



Thus the quotient is $5j+4$ for $q=1$ and $5j+3$ for $q=2$.  For fixed $m$
and fixed $b$, the product of all distinct phase primes divides
$|10m+1-b|$.  Therefore, if $0\le B\le5m$,



$$
\sum_{0\le b\le B}\ \sum_{p\text{ in phase }b}\log p
 \le (B+1)\log(10m+1).                               \tag{7.3}
$$



In particular,



$$
B=o(m/\log m)\Longrightarrow (7.3)=o(m). \tag{7.4}
$$



These near phases contribute coefficient **zero per $m$**.  The currently
missing coefficient is



$$
0.1177979020165907632818384072\ldots\quad\text{per }m,
$$



while the full $\kappa=1$ cell coefficient is



$$
0.4820375017701112\ldots\quad\text{per }m.
$$



Hence the near-phase theorem does not fill the gap; it removes a thin region
from consideration.  The far moving-$b$ region could still carry more than
the missing coefficient, and no contrary bound is proved here.

For the mandatory row $(m,p,j,s)=(2249,2399,1,299)$, (7.2) reads



$$
10m+1-900=9\cdot2399.        \tag{7.5}
$$



## 8. Certificate and status

The standard-library checker

    work/item212_offray_phase_eliminant_certificate.py

performs the following exact tasks:

1. reproduces the recurrence and phase coefficients independently;
2. evaluates the stable-band rational eliminants;
3. verifies the eliminant equivalence on 2,310 finite nodes in both $q$ phases;
4. reproduces $(299,2399,900)$ and its two eliminant divisibilities;
5. verifies the exact $(13,53)$ compatibility false positive;
6. checks the row identities in both phases;
7. audits the rational eliminants through $b=400$, with all bounded claims
   explicitly labeled **FINITE**.

Canonical and replay JSON outputs are byte-identical.  The portable artifacts
are

    work/item212_offray_phase_eliminant_report.md
    work/item212_offray_phase_eliminant_certificate.py
    work/item212_offray_phase_eliminant_certificate.json
    work/item212_offray_phase_eliminant_certificate_replay.json
    work/item212_offray_phase_eliminant_manifest.json
    work/item212_offray_phase_eliminant_hashes.sha256

Status summary:

* **PROVED:** exact all-prime normalization (2.5).
* **PROVED:** complete forced-support classification.
* **PROVED:** the stable-band $b$-only eliminant (4.5), including the mandatory
  off-ray root.
* **PROVED:** the phase overlap identity and zero rate for
  $b=o(m/\log m)$.
* **PROVED:** first-singularity compatibility alone is insufficient.
* **FINITE:** the declared equivalence and rational-eliminant audits.
* **OPEN:** a sublinear count or adequate log-weight bound for far moving-$b$
  cancellations, primitive contractions, $A_1$, the joint gate, a Route-1
  exponent improvement, and $e+\pi$.
