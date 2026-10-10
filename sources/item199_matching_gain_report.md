> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 199 — a two-index transfer barrier for recycled sequential matching

Date: 2026-08-30 (Beijing time)

## 1. Verdict

This item revisits the sequential matching branch of Items 163--169.  It
does not construct the missing positive-rate family.  It proves a sharply
scoped no-go for one natural remaining mechanism: **recycling the same
matched prime-power block at two nearby beta indices**.

Let



$$
p_0=1,\quad p_1=3,\qquad q_0=q_1=1,
$$





$$
x_n=(4n-2)x_{n-1}+x_{n-2}\qquad(n\ge2)
$$



be the actual beta numerator and denominator sequences.  For a fixed
primitive mixed-cubic form



$$
L=a+\varepsilon b\pi>0,\qquad (a,b)=1,\quad b>0,
$$



write, at a parity-compatible beta index $N$,



$$
\Delta_N=(b,q_N),\quad b=\Delta_Nb_{0,N},\quad
 q_N=\Delta_Nq_{0,N},
$$





$$
P_N^*=b_{0,N}p_N-\varepsilon q_{0,N}a,\qquad
 g_N=(P_N^*,\Delta_N).
$$



For $h\ge1$, define the beta transfer continuant



$$
C_0(N)=0,\qquad C_1(N)=1,
$$





$$
C_{j+1}(N)=(4N+4j+2)C_j(N)+C_{j-1}(N).                 \tag{1.1}
$$



The main theorem is



$$
\boxed{
 (\Delta_Ng_N,\Delta_{N+h}g_{N+h})
 =(\Delta_N,\Delta_{N+h})(g_N,g_{N+h})
 \mid C_h(N).}                                           \tag{1.2}
$$



There is a complete three-index consequence at the nearest allowed gaps:



$$
\boxed{
 (\Delta_Ng_N,\Delta_{N+2}g_{N+2},
  \Delta_{N+4}g_{N+4})=1.}                              \tag{1.3}
$$



For the actual matching construction, $N$ and $N+h$ have the same
required parity, so $h$ is even.  Formula (1.2) includes ordinary and
singular beta roots and every prime-power valuation; it does not assume a
squarefree denominator.  Formula (1.3) says more than zero rate: no odd
prime can be recycled across three consecutive indices of the required
parity.

Moreover,



$$
C_h(N)\le(4N+4h-1)^{h-1}.                               \tag{1.4}
$$



At the beta saddle



$$
\frac{N_m\log N_m}{6m}\longrightarrow
 \theta:=\frac d2
 =1.168531187179486497926964890273\ldots,                 \tag{1.5}
$$



equations (1.2) and (1.4) give the theorem-level conclusion



$$
h_m=o(N_m)\quad\Longrightarrow\quad
 \frac1{6m}\log
 (\Delta_{N_m}g_{N_m},\Delta_{N_m+h_m}g_{N_m+h_m})
 \longrightarrow0.                                      \tag{1.6}
$$



Thus a fixed-width or sublinear-width portfolio of beta indices cannot
recover positive linear matching mass by repeatedly using one common
prime-power block.  If a booked rank-one/denominator-clearing divisor is
removed first, the genuinely unbooked common factor is a divisor of the
left side of (1.2), so (1.6) still applies.  This is the precise Route-1
relevance: the theorem controls only matching gain independent of the
already exhausted reservoir, rather than counting reservoir overlap again.

Comparable gaps remain open.  If $h_m/N_m\to\alpha$, the present bound is
only



$$
\limsup\frac1{6m}\log
 (\Delta_{N_m}g_{N_m},\Delta_{N_m+h_m}g_{N_m+h_m})
 \le \alpha\theta.                                      \tag{1.7}
$$



For comparison, the gap left after the optimistic doubled clearing
reservoir is



$$
G=0.019632983669431793880306401240\ldots.
$$



Consequently, this two-index reuse mechanism could carry rate $G$ only
if the gap were at least comparable on the scale



$$
\limsup\frac{h_m}{N_m}\ge
 \frac G\theta
 =0.0168014203513219247791020171\ldots.                  \tag{1.8}
$$



Equation (1.8) is a necessary capacity condition, not an existence result.
The theorem leaves a shift of order $N_m$, a single-index match, and
disjoint prime sets at different indices unresolved.

## 2. The exact beta transfer determinant

The adjacent Wronskian of the two beta solutions is



$$
p_nq_{n-1}-p_{n-1}q_n=2(-1)^{n-1}.                       \tag{2.1}
$$



Indeed, it is $2$ at $n=1$, and the determinant of one recurrence
step is $-1$.

Induction in (1.1) gives, for either $x=p$ or $x=q$,



$$
x_{N+h}=C_h(N)x_{N+1}+C_{h-1}(N+1)x_N.                   \tag{2.2}
$$



The second term cancels from the two-index determinant.  Using (2.1),



$$
\boxed{
 p_Nq_{N+h}-p_{N+h}q_N
 =2(-1)^{N+1}C_h(N).}                                    \tag{2.3}
$$



This identity is over the integers and contains no finite-data or modular
assumption.

For $N\ge0$, the positive continuants are increasing from $C_1=1$.
For $1\le j<h$,



$$
C_{j+1}(N)
 \le(4N+4j+3)C_j(N)
 \le(4N+4h-1)C_j(N),
$$



which proves (1.4).  In the smallest parity-compatible case,



$$
C_2(N)=4N+6=2(2N+3).                                    \tag{2.4}
$$



Since every $q_N$, and therefore every $\Delta_Ng_N$, is odd, (1.2)
and (2.4) sharpen to



$$
(\Delta_Ng_N,\Delta_{N+2}g_{N+2})\mid 2N+3.             \tag{2.5}
$$



Thus two nearest allowed beta indices can share only polynomial-size
sequential content.

Apply (2.5) first to $N,N+2$, and then with $N$ replaced by $N+2$.
Any prime power common to all three exact sequential factors at
$N,N+2,N+4$ must divide both



$$
2N+3\qquad\hbox{and}\qquad 2N+7.
$$



Their gcd divides $4$, while all sequential factors are odd.  Hence their
common gcd is $1$, proving (1.3).  This proof uses the exact
parity-compatible spacing.  It makes no assertion about a nonconsecutive
triple or about gaps comparable with $N$.

## 3. Primewise proof of the common-factor theorem

Fix an odd prime $p$, and set



$$
B=v_p(b),\qquad Q_N=v_p(q_N),\qquad
 D_N=v_p(\Delta_N)=\min(B,Q_N),
$$





$$
J_N=v_p(g_N).
$$



The frozen equal-valuation lemma says



$$
J_N>0\quad\Longrightarrow\quad B=Q_N>0.                 \tag{3.1}
$$



Apply the same notation at $M=N+h$.  Primewise, (3.1) gives



$$
\min(D_N+J_N,D_M+J_M)
 =\min(D_N,D_M)+\min(J_N,J_M).                            \tag{3.2}
$$



If at least one of $J_N,J_M$ is zero, the common exponent in (3.2) is
$\min(D_N,D_M)$, which is at most $\min(Q_N,Q_M)$.  It therefore
divides both $q_N$ and $q_M$, and hence divides the determinant in
(2.3).

It remains to treat



$$
j:=\min(J_N,J_M)>0.
$$



Then (3.1) forces one exact common valuation



$$
B=Q_N=Q_M=:e.
$$



Write



$$
b=p^e\beta,\qquad q_N=p^ex,\qquad q_M=p^ey,
$$



where $\beta,x,y$ are $p$-adic units.  The two final matching
congruences are



$$
\beta p_N-\varepsilon xa\equiv0\pmod {p^j},
$$





$$
\beta p_M-\varepsilon ya\equiv0\pmod {p^j}.              \tag{3.3}
$$



Multiplying the first congruence by $y$, the second by $x$, and
subtracting eliminates the mixed-cubic coordinate:



$$
\beta(p_Ny-p_Mx)\equiv0\pmod {p^j}.
$$



Since $\beta$ is a unit,



$$
p^{e+j}\mid p_Nq_M-p_Mq_N.                               \tag{3.4}
$$



The exponent $e+j$ is exactly the common exponent in (3.2).  Multiplying
over all odd primes proves that the common sequential factor divides the
determinant (2.3).  The common factor is odd, so the factor $2$ in (2.3)
can be removed, proving (1.2).

This argument is why the exact valuation diagonal matters.  Merely knowing
$p\mid b,q_N,q_M$ would give only the first $e$ determinant digits.
The equality $v_p(b)=v_p(q_N)=v_p(q_M)$, together with both normalized
matching congruences, gives the additional $j$ digits corresponding to
the final factors $g_N,g_M$.

## 4. Saddle and modulus-cost consequence

Let



$$
S_m=(\Delta_{N_m}g_{N_m},
       \Delta_{N_m+h_m}g_{N_m+h_m}).
$$



From (1.2), (1.4), and (1.5), when $h_m=o(N_m)$,



$$
\frac{\log S_m}{6m}
 \le
 \frac{(h_m-1)\log(4N_m+4h_m-1)}{6m}
 =\left(\theta+o(1)\right)\frac{h_m}{N_m}
 =o(1).
$$



This can also be read as an exact modulus-cost theorem.  On ordinary root
branches, Item 163 identifies $\Delta_Ng_N$ with the local CRT modulus
spent by the index.  Formula (1.2) says that a modulus block reused at a
second index is not free: it must already divide the transfer continuant
connecting the two indices.  Singular branches do not evade this
two-index determinant argument.

To separate old and new mass, let $\mathcal B_m$ be any integer whose
prime-power digits have already been booked from the rank-one and
denominator-clearing reservoirs, and put



$$
S_m^{\rm new}=\frac{S_m}{(S_m,\mathcal B_m)}.
$$



Then $S_m^{\rm new}\mid S_m\mid C_{h_m}(N_m)$.  Hence every genuinely
independent common gain has zero rate for $h_m=o(N_m)$.  The theorem does
not assert that all of $S_m$ is new, and it does not add $S_m$ to the
already booked reservoir ceiling.

## 5. Exact finite replay

The companion certificate performs two independent deterministic checks.

1. It verifies (2.2), (2.3), and (1.4) for every
   $0\le N\le240$, $1\le h\le60$: 14,460 exact checks of each
   identity or inequality, with no failure.
2. It reads the frozen actual mixed-cubic rows for $1\le m\le100$,
   reconstructs all 15,150 parity-compatible local matching data, and
   checks (3.1), (3.2), and (1.2) on 175,550 exact two-index pairs.  All
   pairs are checked for $m\le30$; for larger $m$, every even gap at
   most 20 is checked.  It additionally checks every 14,950 available
   consecutive parity triple $N,N+2,N+4$ and finds common gcd exactly
   one in every case.  There are no failures.

The final matching part is nonvacuous in the replay.  There are 32 pairs
with $(g_N,g_M)>1$.  For example, the actual row



$$
(m,N,M)=(12,23,25)
$$



has



$$
(\Delta_{23},g_{23})=(7,7),\qquad
 (\Delta_{25},g_{25})=(287,7).
$$



Therefore



$$
(\Delta_{23}g_{23},\Delta_{25}g_{25})=49,
$$



while



$$
C_2(23)=98,\qquad 2N+3=49.
$$



This is an exact illustration of (2.5), not an asymptotic existence claim.
The largest common $g$ in the replay is 13, at
$(m,N,M)=(24,34,134)$.  These finite counts are diagnostics only.

## 6. Route-1 boundary

### PROVED

- The all-index beta transfer identities (2.2)--(2.3).
- The exact common sequential-factor decomposition (3.2).
- The divisibility theorem (1.2), including all prime powers and singular
  beta branches.
- The continuant height bound (1.4), the fixed-gap specialization (2.5),
  the three-index gcd-one theorem (1.3), and the saddle zero-rate theorem
  (1.6).
- The fact that removing overlap with any already booked reservoir cannot
  increase the common gain, so genuinely independent sublinear-gap reuse is
  also zero-rate.

### EXPERIMENTAL FINITE

- The exact replay counts and examples in Section 5.  They are not used to
  prove the general theorem.

### OPEN

- A positive-rate lower bound for $\Delta_Ng_N$ at one actual saddle
  index.
- Reuse across a comparable gap $h\asymp N$; (1.7) leaves formal
  capacity.
- Prime factors that match at only one index, or disjoint matching supports
  at several indices.
- Existence of the required actual primes in $b_m$, exact
  $b_m$-divisibility, the normalized final congruence, and an
  exceptionally small moving CRT representative.  These remain distinct
  conditions.
- Any conclusion about irrationality, rationality, or transcendence of
  $e+\pi$.

This is therefore a genuine Route-1 pruning theorem, not a route-wide
impossibility theorem.

## 7. Replay and path-stable manifest

After integration at the archive root, run

```text
python -m py_compile scripts/item199_matching_gain_certificate.py
python scripts/item199_matching_gain_certificate.py \
  --archive . \
  --output results/item199_matching_gain_certificate.replay.json
```

The canonical and replay JSON files are byte-identical.  The result stores
the input path relative to the archive and its SHA-256, not the machine's
absolute path.  The checker resolves its default archive from its own
installed location; it contains no host-specific path.  The companion
manifest uses archive-relative paths.  The final canonical/replay pair was
also regenerated with the Codex bundled Python runtime.  No timestamp,
Python version, platform string, absolute output path, or floating diagnostic
is serialized, so those fields cannot perturb the replay hash.
