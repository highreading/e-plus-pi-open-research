> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 206 — moving-prime determinant collisions and global capacity

## 1. Scope and outcome

This is a new Route-1 branch from archived Items 189, 195, 196, and 203 and
the current Route-1 ledger.  It studies only the first two $\kappa=1$
gates $A_0,B_0$.  It does not use the forced $F_m=G_m$ mechanism, does
not reuse Item 149's digit, and makes no assertion about $A_1$.

The main outcome is a structural no-go for the proposed cross-row collision
strategy, together with an exact reduction on its regular locus.

**PROVED — universal all-$j$ kernel.**  The two rational pole-weight rows
for $A_0,B_0$, for every $j\geq1$, annihilate the same line



$$
\mathcal L=\langle(2,-1,-1)\rangle                 \tag{1.1}
$$



in the real coordinates
$(V(-1),\operatorname{Re}V(i),\operatorname{Im}V(i))$.  Therefore
every $3\times3$ eliminant made from one $A/B$ row pair and any row at
another $j$ is identically zero over $\mathbb{Q}$.  This is an exact
identity, not a finite coincidence.

**PROVED — regular-rank joint gates are exactly common moving content.**
Let the two weight rows have rank two modulo an admissible odd prime $p$.
Then, for every $s\geq0$,



$$
A_0=B_0=0\pmod p
 \quad\Longleftrightarrow\quad
 g_0(s)=g_1(s)=0\pmod p.                               \tag{1.2}
$$



For odd $s$, $j=1$ is always a regular same-parity anchor; for even
$s\geq2$, $j=2$ is always regular.  At $s=0$, the only boundary is
$(j,p)=(2,7)$, which belongs to the automatic rank-zero interval below;
all $p\geq11$ have the regular $j=2$ anchor.

**PROVED — an automatic rank-zero interval has zero Route-1 rate.**  If



$$
2j+3\leq p\leq3j+2,              \tag{1.3}
$$



then both complete weight rows vanish modulo $p$, independently of the
moving vector.  On a $\kappa=1$ row this forces $p^2\leq6m$; hence all
such rows together have log-prime weight $O(\sqrt m)$, which is zero
after normalization by $m$.

**PROVED — maximal cross-row collisions really occur.**  For
$(p,s)=(19,3)$, the common content vanishes and every admissible
same-parity row



$$
j=1,3,5,7\qquad(m=17,36,55,74)          \tag{1.4}
$$



has $A_0=B_0=0$.  In general a common-content root occupies



$$
N_p(s)=\#\{1\leq j\leq(p-3)/2:j\equiv s\pmod2\}
       ={p\over4}+O(1)                                  \tag{1.5}
$$



rows.  Thus the $j$-direction can have linear, rather than Sidon-sized,
collision fibres.

**OPEN.**  Rank-one primes above $3j+2$ genuinely occur.  On those rows
the two gates collapse to one condition and (1.2) need not follow.  No
uniform rate bound is proved for that moving determinant-divisor family,
and no uniform zero count is proved for the common-content sequence
$\gcd(g_0(s),g_1(s))$.  Consequently Item 206 proves no positive missing
rate and no new mass.  The $A_1$ gate remains wholly separate.

## 2. Exact moving and fixed data

Use the archive convention



$$
u=x(1-x),\qquad Q=(x+1)(x^2+1),\qquad
 F_j={u^{3j+2}\over Q^{2j+2}}.                          \tag{2.1}
$$



On the rank-one cell,



$$
2m+1=(j+1)p-s,\qquad
 0\leq s\leq{p-3\over3},\qquad
 s\equiv j\pmod2,                                     \tag{2.2}
$$



and $k=3s+2<p$.  Item 196's normalized primitive is
$G_s=B_s/u^k$, with



$$
L_kB_s:=uB_s'-ku'B_s
   =Q^{2s}\bigl(g_1(s)Q-g_0(s)\bigr),\qquad
 \deg B_s=2k-2.                                        \tag{2.3}
$$



For $\rho=p\bmod4\in\{1,3\}$, put



$$
V_{s,\rho}(a)=u(a)G_s(a^\rho),\qquad a\in\{-1,i,-i\}. \tag{2.4}
$$



Conjugation writes this as the real vector



$$
X_{s,\rho}=
 \bigl(V(-1),\operatorname{Re}V(i),\operatorname{Im}V(i)\bigr)
 \in\mathbb{F}_p^3.                                    \tag{2.5}
$$



Let $r^A_j,r^B_j\in\mathbb{Q}^3$ be the two Item 196 weight rows after
this real conversion.  The gates differ from
$r^A_jX_{s,\rho}$ and $r^B_jX_{s,\rho}$ only by displayed units.  All
their denominators are $p$-units when $p\geq2j+3$.

## 3. The universal cohomological direction

At the three roots of $Q$, the partial fractions are



$$
\sum_{a\in\{-1,i,-i\}}{-u(a)\over x-a}
 ={2\over x+1}+{-1-i\over x-i}+{-1+i\over x+i}
 ={4\over Q(x)}.                                       \tag{3.1}
$$



Write $A=3j+2$ and $K=2j+2$.  Direct logarithmic differentiation,
using



$$
3u'Q-2uQ'-8+5Q=0,                       \tag{3.2}
$$



gives the relative differential identity



$$
{4F_j\over Q}\,dx
  ={5\over2}F_j\,dx
   +d\!\left({uF_j\over2j+2}\right).                  \tag{3.3}
$$



The primitive in (3.3) vanishes at both endpoints $0,1$.  Hence the
relative endpoint-coordinate vector of $4F_j/Q$ is exactly
$5/2$ times that of $F_j$.  Taking either of the defining wedges for
$A_0$ or $B_0$ kills this vector.  In the real coordinates (2.5), the
pole vector in (3.1) is precisely



$$
v_\star=(2,-1,-1).             \tag{3.4}
$$



Therefore



$$
r^A_jv_\star=r^B_jv_\star=0,\qquad
r^A_j\times r^B_j=\Delta_j(2,-1,-1)                  \tag{3.5}
$$



for one rational $\Delta_j$.  A rationally degenerate row
$\Delta_j=0$ is allowed here and is singular at every prime; the
deterministic finite audit finds no such row through $j=12$.  Equation
(3.5) immediately yields, for all $j,h\geq1$,



$$
\det(r^A_j,r^B_j,r^A_h)
 =\det(r^A_j,r^B_j,r^B_h)=0.                           \tag{3.6}
$$



Thus an exact cross-row polynomial $G_p(S)$ formed from these
determinants is the zero polynomial.  Two-point monodromy in $j$ sees no
new direction: every regular row cuts out the same line.

The two minimal-parity minors are explicitly



$$
\Delta_1={5^3\over2^{11}3},\qquad
 \Delta_2=-{7^3\over2^{11}3\cdot5}.                   \tag{3.7}
$$



If $s$ is odd, then $p>3s+2\geq5$, so $p\neq5$; if $s\geq2$
is even, then $p>3s+2\geq8$, so $p\neq7$.  This proves the regular
anchor assertions in Section 1 without an extrapolation from finite data.

## 4. Rank two: the joint gate is common content

Assume $\Delta_j$ is a $p$-unit.  By (3.5), the common kernel of the
two rows is exactly $\mathcal L$.  Membership in that line says



$$
V(-1):V(i):V(-i)=2:(-1-i):(-1+i),                    \tag{4.1}
$$



or equivalently that $G_s$ is constant on the three roots of $Q$.
This equivalence is unchanged when $\rho=3$, because
$a\mapsto a^3$ merely permutes those roots.  Thus, for some $d$,



$$
Q\mid B_s-du^k.               \tag{4.2}
$$



Set $P=B_s-du^k$.  Since $L_k(u^k)=0$, equation (2.3) gives



$$
L_kP=Q^{2s}(g_1Q-g_0).                                \tag{4.3}
$$



The cancellation-aware step is the exact congruence



$$
uQ'\equiv-4\pmod Q,            \tag{4.4}
$$



because $uQ'+4=(4-3x)Q$.  If $Q^r\mid P$, write $P=Q^rT$.  For
$1\leq r\leq2s$, reduction of $L_kP/Q^{r-1}$ modulo $Q$ gives
$-4rT$.  The right side of (4.3) is divisible by $Q^{2s}$, and
$p>3s+2>2s$, so $r$ is a unit.  Starting with (4.2) and iterating
proves



$$
Q^{2s+1}\mid P.               \tag{4.5}
$$



Degree now gives



$$
P=Q^{2s+1}(Ax+B).              \tag{4.6}
$$



After substituting (4.6) into (4.3) and cancelling $Q^{2s}$, the
coefficients from $x^0$ through $x^4$ are



$$
\begin{split}
 &-(3s+2)B,\\
 &-(3s+1)A+(5s+3)B,\\
 &(5s+3)(A+B),\\
 &(5s+3)(A+B),\\
 &(5s+3)A+B.
\end{split}                                             \tag{4.7}
$$



The right side is $g_1Q-g_0$, whose $x^4$ coefficient vanishes and
whose $x,x^2$ coefficients agree.  Hence



$$
B=-(5s+3)A,\qquad 4(2s+1)A=0.                        \tag{4.8}
$$



Since $p>3s+2$, equation (4.8) forces $A=B=0$.  Then $P=0$; the
strict degree inequality $\deg B_s<\deg u^k$ forces $d=0$ and
$B_s=0$, and (2.3) forces $g_0=g_1=0$.  Conversely, if
$g_0=g_1=0$, Item 196's coefficient construction (whose denominators
are $p$-units) gives $B_s=0$, so both gates vanish.  This proves
(1.2) for $s\geq1$.

For $s=0$, the two cleared moving vectors for $\rho=1,3$ are



$$
(-6,2,6),\qquad(-6,6,2).       \tag{4.9}
$$



Neither is on $\mathcal L$ modulo an odd prime, while
$\gcd(g_0(0),g_1(0))=\gcd(10,6)=2$.  Thus both sides of (1.2) are false
on every rank-two odd-prime row, completing the boundary case.

## 5. The automatic rank-zero interval

Suppose (1.3) holds.  Put $r=3j+2-p\geq0$ and $K=2j+2<p$.  In
characteristic $p$, Frobenius and Cartier semilinearity give



$$
F_j\,dx
 =u^p{u^r\over Q^K}\,dx,\qquad
 {u^r\over Q^K}={u^rQ^{p-K}\over Q^p}.                \tag{5.1}
$$



The numerator on the right has degree



$$
2r+3(p-K)=p-2<p-1.                  \tag{5.2}
$$



Therefore its Cartier extraction has no coefficient in a degree
congruent to $p-1\pmod p$, so the differential is exact.  After one
extra divisor $x-a$, with $a$ a root of $Q$, the polynomial
numerator is



$$
{u^rQ^{p-K}\over x-a},               \tag{5.3}
$$



of degree $p-3$, so that differential is exact as well.  The boundary
$p=K+1$ is included because $Q^{p-K}/(x-a)=Q/(x-a)$ is still a
polynomial.  All logarithmic and circular coordinates vanish, and hence
both wedge rows vanish.  This proves (1.3).

For rate, (2.2), $j\geq(p-2)/3$, and
$s\leq(p-3)/3$ give



$$
2m+1=(j+1)p-s
 \geq{(p+1)p-(p-3)\over3}
 ={p^2+3\over3},
 \qquad p^2\leq6m.                                    \tag{5.4}
$$



Thus the total log-prime weight is at most
$\sum_{p\leq\sqrt{6m}}\log p=O(\sqrt m)$.

Two boundary controls show why rank must be kept explicit:



$$
(j,p,s,m)=(2,7,0,10),\qquad A_0=B_0=0\pmod7,          \tag{5.5}
$$



and the primitive-content counterexample



$$
\begin{gathered}
 (j,p,s,m)=(3,11,1,21),\\
 C^A=-{150464985\over256}\equiv0\pmod{11},\qquad
 C^B=-{191577969\over128}\equiv0\pmod{11},\\
 (g_0(1),g_1(1))\equiv(6,6)\pmod{11}.
\end{gathered}                                         \tag{5.6}
$$



So (1.2) cannot be extended through rank zero.

## 6. Rank-one exceptions and the exact information barrier

For $p>3j+2$, define the singular determinant family by



$$
\Delta_j=0\quad\text{or}\quad
 p\mid\operatorname{num}(\Delta_j).                   \tag{6.1}
$$



At such a prime the two rows can have rank one.  This is not hypothetical.
The deterministic **FINITE** ledger through $j=12$ finds, above the
automatic interval,



$$
\begin{array}{c|c|c}
j&p&\text{rank-one type}\\ \hline
3&19&B\text{-row zero}\\
6&29&\text{two nonzero parallel rows}\\
7&79&\text{two nonzero parallel rows}\\
9&1291&\text{two nonzero parallel rows}\\
11&59&B\text{-row zero}\\
11&8123&\text{two nonzero parallel rows}\\
12&1597&\text{two nonzero parallel rows}.
\end{array}                                             \tag{6.2}
$$



This table is a finite diagnostic, not an all-$j$ distribution theorem.
On rank one, the joint gate is only one moving linear equation, so the
$Q$-adic implication in Section 4 is unavailable.  No bounded-height
formula for the primitive part of $\Delta_j$, and no uniform count of
the prime divisors in (6.1), is presently proved.

More fundamentally, (3.6) means that adding a second regular $j$-point
cannot repair this: its row space is the same plane and its common kernel
is again $\mathcal L$.  Common-content roots then occupy the full fibre
(1.5).  Therefore the present determinant-collision mechanism supplies no
codimension in the moving $j$-direction.  Any positive missing-rate
argument must instead control both



$$
p\mid\gcd(g_0(s),g_1(s))\qquad\text{and}\qquad
 p\mid\operatorname{num}(\Delta_j)                    \tag{6.3}
$$



on their moving ranges, or introduce information outside the first
$A_0/B_0$ pole-weight plane.  Items 189's Sidon heuristic and 195's
two-point eliminant cannot by themselves provide that missing input.

## 7. Deterministic certificate and portability

The standard-library checker

`scripts/item206_moving_prime_collision_certificate.py`

performs the following tasks.

1. It verifies (3.1)--(3.5) in exact rational/Gaussian arithmetic and
   checks every cross-$j$ determinant through $j=12$.
2. It verifies the exact anchor minors (3.7).
3. It replays the coefficient identity (4.7) through $s=12$.
4. It verifies the Cartier rank-zero interval for every row through
   $j=12$, and records all rank-one determinant primes in that range.
5. It checks 512 regular-anchor triples with $0\leq s\leq12$ and
   $p\leq211$, explicitly labelled **FINITE**.
6. It reproduces (1.4), (4.9), and the exact witness (5.6).

The canonical and replay JSON files must be byte-identical.  The checker
resolves its pinned Item 175, Item 178, and Item 196 helpers either beside
it in `work/` or beside it in an archive-layout `scripts/` directory.  Its
JSON contains archive-relative dependency keys and hashes only.  The
portable bundle is

```text
sources/item206_moving_prime_collision_report.md
scripts/item206_moving_prime_collision_certificate.py
results/item206_moving_prime_collision_certificate.json
results/item206_moving_prime_collision_certificate_replay.json
scripts/item175_fixed_band_certificate.py
scripts/item178_minimal_parity_certificate.py
scripts/item196_rankone_moving_gate_certificate.py
```

The SHA-256 manifest is
`item206_moving_prime_collision_hashes.sha256`.

Status summary:

- **PROVED:** universal fixed kernel and identically zero cross-row
  eliminants.
- **PROVED:** rank-two joint-gate equivalence with common moving content,
  including $s=0$.
- **PROVED:** the automatic rank-zero interval and its zero-rate bound.
- **FINITE:** rank-drop ledger through $j=12$ and regular-anchor replay
  through $s=12,p\leq211$.
- **OPEN:** moving common-content zeros and rank-one determinant divisors.
- **OPEN/SEPARATE:** $A_1$, any third-copy synchronization, and every
  positive missing-rate or mass conclusion.
