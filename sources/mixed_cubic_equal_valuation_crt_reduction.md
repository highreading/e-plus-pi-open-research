> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Mixed-cubic/beta matching after the equal-valuation lemma

Date: 2026-08-28.

## 1. Verdict

This note studies only the synchronization factor in item 137.  Let



$$
L=a+\varepsilon b\pi>0,\qquad \gcd(a,b)=1,\quad b>0,
$$



and choose the beta index (N) with ((-1)^N=\varepsilon).  Write



$$
E_N=\varepsilon(q_Ne-p_N)>0,
 \qquad
 \Delta=\gcd(b,q_N),
 \qquad
 b=\Delta b_0,quad q_N=\Delta q_0,
$$



and



$$
P^*=b_0p_N-\varepsilon q_0a,
 \qquad g=\gcd(P^*,\Delta).
$$



Two new exact reductions are obtained.

1. A prime can enter (g) only at an **equal positive valuation**:

   

$$
v_p(g)>0\quad\Longrightarrow\quad
   v_p(b)=v_p(q_N)>0.
   \tag{1}
$$



2. On every ordinary Bessel root branch, the full local gain
   (p^{v_p(\Delta g)}) is exactly a congruence modulus in the index.
   More precisely, after the base root modulo (p) is chosen, the
   conditions defining (v_p(\Delta)) and (v_p(g)) select one residue
   class modulo (p^{v_p(\Delta g)}).  The last matching digit is
   transverse to the next root digit of (q_N).

Consequently, if all primes contributing to (\Delta) lie on ordinary
branches, then (N) belongs to at most



$$
\prod_{p\mid\Delta}R_p
 \tag{2}
$$



parity-compatible residue classes modulo (2\Delta g), where (R_p) is
the number of roots of (q_r\) modulo (p).  The proved bound



$$
R_p\leq 2p^{2/3}
 \tag{3}
$$



therefore applies directly.

This does **not** prove an asymptotic upper bound for the actual
(\Delta_mg_m).  If that product has positive exponential rate while
(N\sim (d/2)n/\log n), then the actual index is an exponentially small
representative of one of the residue classes modulo (\Delta_mg_m).
CRT alone gives only a representative below the modulus and cannot put it
in the saddle window.  Proving that the required exceptional small
representatives occur is a new arithmetic theorem, not a consequence of
the Bessel congruences.

The alternative is that an exponential part comes from singular branches.
That runs into the already isolated all-lift/Wieferich obstruction.  Thus
the calculation yields a rigorous CRT obstruction and a sharp dichotomy,
but it neither closes the irrationality proof nor proves that the actual
synchronization rate is too small.

## 2. Exact local equal-valuation ledger

Fix an odd prime (p), and put



$$
B=v_p(b),\qquad Q=v_p(q_N),\qquad D=\min(B,Q)=v_p(\Delta).
$$



If (B>Q), then (p\mid b_0), (p\nmid q_0a), and hence



$$
P^*\equiv-\varepsilon q_0a\not\equiv0\pmod p.
$$



If (Q>B), then (p\mid q_0), (p\nmid b_0p_N), because
(\gcd(p_N,q_N)=1), and hence



$$
P^*\equiv b_0p_N\not\equiv0\pmod p.
$$



This proves (1).  In the only remaining case (B=Q>0), both (b_0)
and (q_0) are (p)-adic units, and



$$
v_p(g)=\min\{B,v_p(P^*)\}.
 \tag{4}
$$



Equivalently, if



$$
E_{=}(b,q_N)=
 \prod_{v_p(b)=v_p(q_N)>0}p^{v_p(q_N)},
 \tag{5}
$$



then



$$
\boxed{g\mid E_{=}(b,q_N)\mid\Delta.}
 \tag{6}
$$



Prime by prime, the complete synchronization ledger is



$$
v_p(\Delta g)=
 \begin{cases}
   \min(B,Q),&B\ne Q,\\[2mm]
   B+\min\{B,v_p(P^*)\},&B=Q>0.
 \end{cases}
 \tag{7}
$$



Thus the final content can double only an equal valuation level.  It
cannot amplify any unequal part of the coefficient gcd.

## 3. The two beta congruences needed below

The archived period theorem gives, for every integer (M\geq1),



$$
p_{n+M}\equiv p_n\pmod M,
 \qquad
 q_{n+M}\equiv(-1)^M q_n\pmod M.
 \tag{8}
$$



For completeness, the first congruence follows immediately from the
terminating formula



$$
p_n=\sum_{j=0}^n\frac{(n+j)!}{j!(n-j)!}.
$$



Modulo (M), the values at (M,M+1) are (1,3), because all terms
except (j=0), and also (j=1) at (M+1), contain (M) in their
falling product.  The recurrence coefficient (4n-2) is periodic modulo
(M), so the congruence follows for all (n).

The archived prime-power second-antiperiod theorem gives, for (p) odd,
(A\geq1), (M=p^A),



$$
q_{n+2M}+2q_{n+M}+q_n
 \equiv2p^{2A-1}q_n\pmod {p^{2A}}.
 \tag{9}
$$



Suppose (M\mid q_r), and define



$$
\delta_M(r)=\frac{-q_{r+M}-q_r}{M}\pmod M.
 \tag{10}
$$



Repeated use of (9), with
(A_t=(-1)^tq_{r+tM}), gives the exact affine law



$$
\boxed{
 \frac{(-1)^tq_{r+tM}}{M}
 \equiv \frac{q_r}{M}+t\delta_M(r)\pmod M.}
 \tag{11}
$$



The branch is ordinary precisely when (\delta_M(r)\) is a (p)-adic
unit.  The inherited-slope theorem says that this is equivalent to the
base root modulo (p) being ordinary.

## 4. Transverse matching-digit theorem

**Theorem 4.1.**  Let (p) be odd and suppose



$$
v_p(b)=B\geq1.
$$



Fix an ordinary descendant (r\pmod {p^B}) of a Bessel root, so that
(p^B\mid q_r), and fix the required parity
((-1)^N=\varepsilon).  For every (1\leq j\leq B), among the indices



$$
N=r+t p^B
$$



there is exactly one class of (t\pmod {p^j}), and hence exactly one
class of (N\pmod {2p^{B+j}}) after parity is imposed, for which



$$
v_p(q_N)=B,
 \qquad p^j\mid g.
 \tag{12}
$$



**Proof.**  Put (M=p^B), (s=(-1)^r), and



$$
\beta=b/M.
$$



The integer (\beta) and the primitive coordinate (a) are (p)-adic
units.  From (8),



$$
p_{r+tM}\equiv p_r\pmod M.
 \tag{13}
$$



On the imposed parity class,



$$
\varepsilon\frac{q_N}{M}
 =s\frac{(-1)^tq_{r+tM}}{M}.
$$



Multiplication of (P^*) by the (p)-adic unit
(\Delta/M) shows that (p^j\mid P^*) is equivalent to



$$
p^j\mid
 H(t):=\beta p_N-\varepsilon\frac{q_N}{M}a.
 \tag{14}
$$



Using (11) and (13),



$$
H(t)\equiv
 \beta p_r-sa\left(\frac{q_r}{M}+t\delta_M(r)\right)
 \pmod {p^B}.
 \tag{15}
$$



This is affine in (t), with unit slope
(-sa\delta_M(r)).  Hence (14) selects exactly one (t\pmod {p^j})
for every (j\leq B).  At that class modulo (p), equation (15) gives



$$
s\frac{(-1)^tq_N}{M}
 \equiv \beta p_r a^{-1}\not\equiv0\pmod p.
$$



Thus (v_p(q_N)=B), rather than (>B).  Finally, the condition on
(t\pmod {p^j}) and the parity condition on (t\pmod2) combine uniquely
because (p) is odd.  Equation (4) completes the proof. $\square$

The last displayed nonzero residue is important: the matching digit is
not the digit which lifts (q_N) to valuation (B+1).  It is a distinct,
transverse digit.

If the root is singular, the slope in (15) vanishes modulo (p).  The
condition then has either no child or every child at the first level.
This is exactly where the theorem stops, and it matches the archived
singular all-lift obstruction.

## 5. Simultaneous ordinary primes and the exact CRT modulus

Let (\mathcal S) be the primes dividing (\Delta), and suppose the
root branch followed by (N) is ordinary for every (p\in\mathcal S).
For each (p), put



$$
D_p=v_p(\Delta),\qquad J_p=v_p(g).
$$



If (J_p>0), (1) gives



$$
D_p=v_p(b)=v_p(q_N),\qquad 0<J_p\leq D_p,
$$



and Theorem 4.1 selects one class modulo (p^{D_p+J_p}) over each base
root modulo (p).  If (J_p=0), ordinary Hensel inheritance selects one
class modulo (p^{D_p}) over each base root.  CRT therefore proves:

**Theorem 5.1 (ordinary synchronization modulus).**  Under the ordinary
branch hypothesis, all parity-compatible indices having the prescribed
local synchronization data lie in at most



$$
\boxed{\prod_{p\mid\Delta}R_p}
 \tag{16}
$$



residue classes modulo



$$
\boxed{2\prod_{p\mid\Delta}p^{D_p+J_p}=2\Delta g.}
 \tag{17}
$$



Consequently, an interval of length (H) contains at most



$$
\boxed{
 \left(\prod_{p\mid\Delta}R_p\right)
 \left(\frac{H}{\Delta g}+1\right)}
 \tag{18}
$$



such indices.  Inserting (3) gives



$$
\prod_{p\mid\Delta}R_p
 \leq 2^{\omega(\Delta)}\operatorname{rad}(\Delta)^{2/3}.
 \tag{19}
$$



The modulus in (17) is exactly the synchronization gain, not merely its
radical.  This is the main benefit of combining the equal-valuation lemma
with the prime-power affine law.

## 6. Consequence at the saddle scale, and why it is not a no-go theorem

For item 137, (n=6m) and a saddle-compatible beta index satisfies



$$
\frac{N\log N}{n}\longrightarrow\frac d2,
 \qquad
 N=\left(\frac d2+o(1)\right)\frac n{\log n}.
 \tag{20}
$$



Suppose on an ordinary subsequence that



$$
\frac1n\log(\Delta_mg_m)\longrightarrow\kappa>0.
 \tag{21}
$$



Then Theorem 5.1 puts (N_m) in one of the explicit classes modulo



$$
M_m=\Delta_mg_m=\exp((\kappa+o(1))n),
$$



while



$$
\frac{N_m}{M_m}=\exp(-\kappa n+o(n)).
 \tag{22}
$$



Thus a successful synchronization theorem must prove that the actual CRT
class has an exponentially small positive representative, simultaneously
with the moving mixed-cubic coefficient (b_m).  Ordinary CRT provides a
representative (<M_m); it gives nothing like (22).  The local Bessel
congruences therefore account for all of the apparent determinant gain and
do not by themselves choose a saddle-compatible index.

This is a rigorous obstruction to a generic CRT construction, not an
upper bound on the actual (\Delta_mg_m).  Root classes can in principle
have exceptional small representatives.  Proving or excluding that
phenomenon for the actual (b_m) remains open.

If (21) is instead carried by singular branches, the ordinary modulus
theorem does not apply.  The first singular central example is the root
((p,r)=(79,39)); the archived exact scan finds no other singular root for
(p\leq200000), but there is no all-prime theorem.  An exponential
singular contribution would require precisely the unresolved
truncated-hypergeometric all-lift phenomenon.

Hence every possible completion through (\Delta g) falls into one of
two genuinely new tasks:

1. prove exponentially small representatives of the actual ordinary CRT
   classes coupled to (b_m); or
2. prove an exponential singular-branch contribution, first overcoming
   the all-prime Wieferich obstruction.

Neither task is solved here.

## 7. Exact finite diagnostics for the actual mixed-cubic coefficient

The script

```text
scripts/mixed_cubic_equal_valuation_scan.py
```

recomputes the actual item-133 pair, removes its exact post-Cartier
content, forms the primitive (b_m), and checks (6) prime by prime.  It
then scans every parity-compatible index in a relative (20\%\) window
around the solution of (N\log N/(6m)=d/2).

The run

```text
m=1,...,100
output: results/mixed_cubic_equal_valuation_m1_100_w20.json
```

gave the following exact finite ledger.

* For every tested pair, (g\mid E_{=}(b_m,q_N)).
* For (m\geq20), the largest observed rate

  

$$
\frac1{6m}\log(c_m\Delta_mg_m)
$$



  was (0.415869\ldots), at (m=21).  This is far below the item-137
  irrationality threshold (1.156147\ldots).
* Over (81\leq m\leq100), the mean rates of (c_m,\Delta_m,g_m) at
  the best actual candidate were respectively

  

$$
0.184573\ldots,qquad0.026424\ldots,qquad0.002046\ldots.
$$



  The largest total rate in those twenty rows was (0.257895\ldots).
* Even replacing the actual (g_m) by the full equal-level ceiling
  (E_{=}(b_m,q_N)), the largest rate over those last twenty rows was
  only (0.277062\ldots).
* The equal-level primes encountered at the optimizing candidates were

  

$$
7,11,13,31,41,71,79,97,101,103,107,157,173,199,227,
  233,281,283,293,337,367.
$$



  All corresponding base roots were ordinary except (p=79).  The
  singular (79)-case appeared once, at (m=64,N=118\equiv39\pmod{79}),
  in the equal-level upper candidate, and its actual final content was
  (g=1).

A second exact run sampled every fifth value



$$
m=105,110,\ldots,200
$$



in the same relative saddle window.  Across those twenty rows, the mean
rates of (c_m,\Delta_m,g_m) at the best actual candidate were



$$
0.174655\ldots,\qquad0.017133\ldots,\qquad0.000513\ldots.
$$



The largest actual total rate was (0.213268\ldots), and the largest
equal-level ceiling was (0.234010\ldots).  The output is

```text
results/mixed_cubic_equal_valuation_m105_200_step5_w20.json
```

These are exact finite statements, not asymptotic estimates.  They support
the structural conclusion that the final content is a thin transverse
condition, but they cannot prove that its rate tends to zero.

The independent finite congruence replay is
`scripts/mixed_cubic_equal_valuation_crt_replay.py`, with output
`results/mixed_cubic_equal_valuation_crt_replay.json`.  It checks ordinary
branches at levels one and two and the singular $(p,r)=(79,39)$ branch.

There is also no finite indication that the primitive coefficient (b_m)
is supported only on primes of size (O(m)).  The exact probe

```text
scripts/mixed_cubic_primitive_b_support_probe.py
results/mixed_cubic_primitive_b_support_probe_selected.json
```

removed every prime at most (6m) from the actual primitive (b_m) at
(m=10,20,30,40,50,60,80,100).  A nontrivial cofactor survived in every
case.  Its logarithmic rate ranged from (1.08817\ldots) to
(1.15479\ldots); at (m=100) it had 987 bits and rate
(1.13996\ldots).  Thus the existing Bessel estimates for a smooth part
cannot simply be applied to all of (\gcd(b_m,q_N)).  A theorem coupling
the large cofactor of the actual (b_m) to the Bessel root classes would
still be needed.

## 8. Final status

The equal-valuation lemma and the prime-power affine law now give an exact
ordinary-branch CRT accounting of the whole factor (\Delta g).  They do
not supply the positive exponential lower bound required by item 137, and
they do not supply an unconditional upper bound excluding such a lower
bound for the actual mixed-cubic coefficients.

In particular, this note does **not** prove irrationality of (e+\pi).
