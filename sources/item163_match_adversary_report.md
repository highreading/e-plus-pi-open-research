> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 163 adversarial audit: sequential matching capacity and thin-pattern traps

Date: 2026-08-29 (Beijing time)

## 1. Verdict

This note audits the matching product



$$
c_m\Delta_{m,N}g_{m,N}
$$



after all primitive reductions.  It does not find a positive-density prime
family that forces either matching factor at exponential scale.  It does
prove a useful capacity envelope and a corresponding small-index no-go:



$$
\boxed{\Delta g\mid \gcd(b,q_N)^2,
 \qquad
 \log(\Delta g)\leq
 2\min\{\log b,\log q_N\}.}
 \tag{1}
$$



Consequently, if $N_m\log N_m=o(m)$, then



$$
\boxed{\log(\Delta_{m,N_m}g_{m,N_m})=o(m).}
 \tag{2}
$$



Thus a bounded beta index, a fixed finite collection of indices, or any
sub-$m/\log m$ index regime cannot contribute positive exponential
matching mass.  This formally disqualifies the fixed-index plateaus that
dominate much of the current finite scan.

The envelope (1) is sharp for abstract primitive positive forms.  Therefore
no better universal bound can be obtained from positivity and primitivity
alone.  Any improvement must use arithmetic special to the actual
mixed-cubic coordinates.

At the balanced beta scale, a one-copy squarefree matching mechanism would
have to capture more than



$$
0.872576611438626561637682081243\ldots
 \tag{3}
$$



of the entire logarithmic height of $q_N$ if it alone supplied the exact
post-rank-one deficit.  Even the idealized case in which every such digit is
doubled by $g$ still requires more than



$$
0.436288305719313280818841040621\ldots .
 \tag{4}
$$



These are necessary capacity fractions, not impossibility theorems.

## 2. Exact sequential algebra

Write the primitive positive mixed-cubic form as



$$
L=a+\varepsilon b\pi>0,
 \qquad \gcd(a,b)=1,\quad b>0,
$$



and let $p_N,q_N$ be the primitive beta pair.  Define



$$
\Delta=\gcd(b,q_N),\qquad
 b=\Delta b_0,\qquad q_N=\Delta q_0,
$$





$$
P^*=b_0p_N-\varepsilon q_0a,\qquad
 g=\gcd(P^*,\Delta).
 \tag{5}
$$



The already-frozen exact ledger gives $g\mid\Delta$.  Hence



$$
\Delta g\mid\Delta^2
 =\gcd(b,q_N)^2.
 \tag{6}
$$



Since $\Delta\mid b,q_N$, equation (6) separately implies



$$
\Delta g\mid b^2,\qquad \Delta g\mid q_N^2.
 \tag{7}
$$



If $|V|=cb$, it also recovers the sequential safeguard



$$
c\Delta g\mid |V|q_N.
 \tag{8}
$$



The separate bounds in (7), rather than only (8), make the beta-index
capacity explicit.

For $N\ge 2$, the recurrence



$$
q_0=q_1=1,\qquad
 q_N=(4N-2)q_{N-1}+q_{N-2}
$$



gives



$$
q_N<4^{N-1}N!,
 \qquad
 \log q_N=N\log N+O(N).
 \tag{9}
$$



Combining (7) and (9) proves (2).  More generally, if a squarefree prime
family $\mathcal S_m$ is forced into $\Delta$, then



$$
\prod_{p\in\mathcal S_m}p\mid q_N,\qquad
 \sum_{p\in\mathcal S_m}\log p\leq\log q_N
 \leq N\log(4N).
 \tag{10}
$$



Therefore any family with positive prime-number-theorem mass on the
$m$-scale forces $N\gg m/\log m$.  Divisibility of $b_m$ by a
positive-density prime family does not by itself force matching: the same
primes must also be Bessel roots at the single chosen index $N$.

### 2.1 Multi-index antiperiod stacking also has zero forced rate

There is a second possible synchronization attempt: replace one beta index
by a finite positive or signed aggregate of shifted beta forms.  Let $S$
be the forward shift in the beta index.  For a finite set of **distinct** odd
primes choose integers



$$
1\leq k_p<{p\over2},
$$



and form



$$
T=\prod_p(1+S^p)^{2k_p},\qquad Q_N=(Tq)_N.
 \tag{11}
$$



The archived all-even antiperiod theorem proves, uniformly in the base
index,



$$
p^{k_p}\mid(1+S^p)^{2k_p}q.
$$



All shift operators commute, and applying the remaining integer-coefficient
operators preserves this divisibility.  Coprimality across the distinct
primes therefore gives the forced raw-coefficient divisor



$$
D=\prod_pp^{k_p}\mid Q_N.
 \tag{12}
$$



The forward shift span is



$$
W=\sum_p2k_pp.
 \tag{13}
$$



For every odd prime $p\geq3$, the function $\log x/x$ is decreasing,
so



$$
{k_p\log p\over2k_pp}
 ={\log p\over2p}
 \leq{\log3\over6}.
$$



Summing proves the sharp method-level capacity bound



$$
\boxed{
  \log D\leq{\log3\over6}W
  =0.183102048111\ldots W.}
 \tag{14}
$$



If every beta index used by the aggregate must remain in the
saddle-compatible range $O(m/\log m)$, then necessarily
$W=O(m/\log m)$.  Equation (14) gives



$$
\log D=o(m).
 \tag{15}
$$



Even granting, optimistically, that the entire raw divisor survives
primitive reduction and that final matching doubles every one of its
digits, its contribution is at most $2\log D=o(m)$.  Thus stacking these
certified antiperiod blocks cannot supply positive exponential matching
mass at saddle-compatible span.

No positivity assertion is needed for this no-go.  In fact, the literal
Hausdorff moment is $N!E_N$, not $E_N$ itself, so invoking positivity of
an unweighted finite-difference aggregate without a separate proof would be
unsafe.  The divisor theorem above holds for the raw coefficient regardless
of the aggregate's sign.

Repeated blocks at the same prime are deliberately excluded from (12): the
archived theorem does not, by itself, authorize adding their certified
valuations.  Even if additive divisibility for repetitions is granted as an
optimistic ceiling, every repeated block has the same ratio
$\log p/(2p)$, so (14)--(15) remain unchanged.  Any common content of the
aggregate beta pair can only remove part of $D$ upon primitive reduction,
which strengthens the obstruction.

## 3. Rate accounting at the balanced scale

The frozen constants are



$$
\theta={d\over2}
 =1.168531187179486497926964890273\ldots,
$$





$$
r_1=0.136514168294812818450423822617\ldots,
$$



and the exact sequential weight still required after the rank-one divisor is



$$
T_1=1.019632983669431793880306401240\ldots
 \quad\hbox{per }6m.
 \tag{16}
$$



At a saddle-compatible beta index,



$$
{\log q_N\over6m}\longrightarrow\theta.
$$



If the whole deficit (16) came from $\Delta$ alone, equations (10) and (16)
would require a captured fraction greater than



$$
{T_1\over\theta}
 =0.872576611438626561637682081243\ldots .
$$



If every captured digit also contributed through $g$, the formal
two-copy floor would be $T_1/(2\theta)$, giving (4).  The latter is only a
capacity ceiling: the final copy has an additional congruence condition.
Extra digits of $c_m$ would reduce the fraction matching must supply, so
neither ratio is an unconditional lower bound for the full route.

## 4. Why the final factor is a transverse, thin condition

For one prime put



$$
B=v_p(b),\qquad Q=v_p(q_N),\qquad D=\min(B,Q),
 \qquad J=v_p(g).
$$



Exact primitive reduction gives



$$
J>0\Longrightarrow B=Q>0,
 \tag{17}
$$



and then



$$
J=\min\{B,v_p(P^*)\}.
 \tag{18}
$$



If $B\ne Q$, the two terms of $P^*$ have unequal valuations, so
$P^*$ is a unit and $J=0$.  Thus an ordinary common prime does not
automatically produce the final copy: it first has to lie on the
equal-valuation diagonal, and then has to satisfy the normalized residue
condition (18).

This restriction is real but cannot be upgraded to a generic upper bound.
At $N=2$, the beta pair is $(p_2,q_2)=(19,7)$.  With
$\varepsilon=1$, both



$$
(a,b)=(19,7),\qquad (a,b)=(20,7)
$$



are primitive and give positive forms.  The first has



$$
(\Delta,g)=(7,7),\qquad\Delta g=q_2^2,
$$



while the second has



$$
(\Delta,g)=(7,1).
$$



Hence (1) is attained, while the same $b,q_N,\Delta$ data need not force
any final content.

On ordinary Bessel root branches, the frozen affine-lift theorem refines
this further: prescribed local data for $\Delta g$, including parity,
place $N$ in residue classes modulo $2\Delta g$.  An exponential
matching product at the saddle scale therefore makes the actual
$N=O(m/\log m)$ an exponentially small representative of its moving CRT
class.  CRT guarantees a representative below the modulus; it does not
guarantee this exceptional small representative.  Distinct first-level
singular primes escape the ordinary theorem and could in principle accumulate
without any all-lift hypothesis.  Repeated deeper lifts at a fixed singular
prime, however, require the unresolved all-lift/Wieferich mechanism.  Both
the abundance and synchronization of first-level singular primes, and the
deeper lifting problem, remain open.

## 5. Exact finite replay

The checker independently replayed all 15,150 parity-compatible candidates
with



$$
1\leq m\leq100,\qquad1\leq N\leq6m.
$$



It reconstructed the beta recurrence, checked all 600 consecutive
Wronskians, recomputed $\Delta,g$, verified (6)--(8) candidate by
candidate, verified the equal-valuation condition prime by prime, and
reproduced every stored row maximum.

The exact finite diagnostics are:

- 6,057 candidates had a nontrivial equal-valuation ceiling;
- 234 candidates had $g>1$, or
  $3.863298662704\ldots\%$ of those candidates;
- among 7,393 equal-valuation prime slots, 236 entered $g$, or
  $3.192208846206\ldots\%$;
- the largest $\Delta$ was
  $596038519=31\cdot97\cdot379\cdot523$, at $(m,N)=(92,544)$,
  with $g=1$;
- the largest $g$ was $1133=11\cdot103$, at
  $(m,N)=(91,455)$, where $\Delta=12463$;
- only ten candidate-prime events with $p>6m$ entered $\Delta$; their
  primes were $31,97,173,691,797$, and none entered $g$.

The last point is especially relevant because the actual primitive
coefficient $b_m$ has a large cofactor after removing primes at most
$6m$.  In this finite window that large cofactor almost never synchronized
with $q_N$.  This is **EXPERIMENTAL**, not an all-$m$ support theorem.

For $81\leq m\leq100$, the mean best rates per $6m$ were



$$
\begin{array}{c|ccccc}
 &\log c&\log\Delta&\log g&\log(\Delta g)&\log(c\Delta g)\\ \hline
\text{mean}
&0.1845733550&0.0303135500&0.0017099311
&0.0320234811&0.2165968361.
\end{array}
\tag{19}
$$



The best-matching rate by consecutive ten-row blocks decreased as follows:



$$
\begin{array}{c|cc}
m&\text{mean best }\log(\Delta g)/(6m)&\text{block maximum}\\ \hline
1\!:\!10&0.203901&0.466491\\
21\!:\!30&0.077996&0.092122\\
41\!:\!50&0.052677&0.057202\\
61\!:\!70&0.041794&0.047990\\
81\!:\!90&0.032223&0.033787\\
91\!:\!100&0.031824&0.036605.
\end{array}
\tag{20}
$$



No asymptotic inference is made from (19)--(20).

## 6. Fixed-index plateau trap

Many late row maxima reuse exactly the same beta index and matching product:



$$
\begin{array}{c|c|c|c}
N&\Delta&g&\text{number of maximizing rows}\\ \hline
41&16572763&1&19\\
312&5149067&1&10\\
121&5088629&1&8\\
138&416273&1&8\\
37&1292137&1&7\\
544&596038519&1&4.
\end{array}
\tag{21}
$$



For every fixed $N$, equation (7) bounds $\Delta g$ by the fixed integer
$q_N^2$, independently of $m$.  Thus every individual plateau in (21)
has zero asymptotic matching rate.  A successful theorem must produce
genuinely growing indices and genuinely growing synchronized prime mass;
repetition of a visually prominent finite factor cannot do so.

## 7. Thin-pattern traps to reject

1. **Raw-coordinate reuse.**  The matching gcd is
   $\gcd(b_m,q_N)$ after division by $c_m$, not
   $\gcd(|V_m|,q_N)$.
2. **Common-prime implies final-content.**  False: $g$ requires equal
   positive valuations and (18).
3. **Fixed-index recurrence.**  Any bounded collection of beta indices has
   zero exponential matching capacity by (2).
4. **Average root sparsity implies a selected-index bound.**  The archived
   zero-gap theorem controls averages and root-class capacity; it does not
   bound the maximum smooth divisor of one adversarially selected $q_N$.
5. **CRT produces the saddle index.**  CRT gives a representative below its
   modulus, not one of size $O(m/\log m)$ when the modulus is exponential.
6. **Observed absence is a theorem.**  The rarity of outside primes and of
   final-content hits in the finite replay is diagnostic only.
7. **Antiperiod divisors add exponential mass.**  Their certified logarithmic
   divisor is at most $(\log3/6)$ times the forward span, hence is
   subexponential at saddle-compatible span.

## 8. Status ledger

### PROVED

- The capacity envelope (1), the separate divisibilities (7), and the
  small-index no-go (2).
- The mass constraint (10) for every squarefree family forced into
  $\Delta$.
- The equal-valuation necessity (17), and sharpness of the abstract
  $q_N^2$ envelope.
- The multi-index antiperiod stacking bound (14)--(15), for distinct prime
  blocks; repeated blocks obey the same bound if additive valuations are
  granted optimistically.
- Exact replay of all 15,150 frozen finite candidates and all stored row
  maxima.

### EXPERIMENTAL

- The decreasing block rates in (20).
- The 234 nontrivial final-content candidates, the prime-slot frequencies,
  the ten outside-prime events, and the repeated plateaus in (21).
- The apparent failure of the large cofactor of $b_m$ to synchronize in
  the tested range.

### OPEN

- Any positive asymptotic lower bound for
  $\log(\Delta_mg_m)/(6m)$ in the actual family, or any nontrivial upper
  bound below the universal $2\log q_N$ capacity.
- A positive-density actual prime family simultaneously dividing $b_m$
  and $q_{N_m}$ at saddle-compatible indices.
- Existence or exclusion of the exponentially small ordinary CRT
  representatives required by an exponential matching product.
- Abundance and synchronization of first-level singular primes; separately,
  an exponential contribution from deeper all-lift/Wieferich branches.

Nothing here proves irrationality, rationality, or transcendence of
$e+\pi$.

## 9. Replay

Run

```text
python work/item163_match_adversary_check.py
```

The result is

```text
work/item163_match_adversary_certificate.json
```

The authoritative hashes are collected in
`work/item163_match_adversary_hashes.sha256`.
