> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 166: the actual-seed Euler-residual bridge for noncentral singular primes

Date: 2026-08-29 (Beijing time)

## 1. Verdict

Let



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2},
$$



and define the companion and jet-correction sequences



$$
P_0=1,\quad P_1=3,\quad
P_n=(4n-2)P_{n-1}+P_{n-2},
\tag{1.1}
$$





$$
b_0=0,\quad b_1=4,\quad
b_n=(4n-2)b_{n-1}+b_{n-2}+4q_{n-1}\quad(n\ge2).
\tag{1.2}
$$



For an odd prime $p$, write



$$
!p:=\sum_{j=0}^{p-1}j!\pmod p
\tag{1.3}
$$



for its left-factorial residue.  Let



$$
p=2r+2h+3,\qquad r\ge1,\quad h\ge0,
\tag{1.4}
$$



and let $D_h$ be the symmetric-continuant derivative from item 165:



$$
\mathcal K_h(X)=[X-4h,X-4h+4,\ldots,X+4h]
                =X\mathcal L_h(X^2),
\qquad D_h=\mathcal K_h'(0).
\tag{1.5}
$$



The fixed initial pair $(q_0,q_1)=(1,1)$ supplies an exact extra identity.
If $p\mid q_r$, then



$$
\boxed{
E_{p,r}:=P_r(!p)-b_r
\equiv 2D_hq_{r-1}\pmod p.}
\tag{1.6}
$$



The Wronskian is



$$
\boxed{
P_rq_{r-1}-P_{r-1}q_r=2(-1)^{r-1}.}
\tag{1.7}
$$



Consequently $P_r$ and $q_{r-1}$ are units modulo a root prime, and



$$
\boxed{
P_rE_{p,r}\equiv4(-1)^{r-1}D_h\pmod p.}
\tag{1.8}
$$



Since item 165 proved
$D_h=\operatorname {Res}_X(X,\mathcal L_h(X^2))$, equations
(1.6)--(1.8) give the requested exact fixed-seed gcd/resultant bridge:



$$
\boxed{
\gcd\!\left(p,q_r,
 \operatorname {Res}_X(X,\mathcal L_h(X^2))\right)
=\gcd\!\left(p,q_r,
 \det\!\begin{pmatrix}P_r&b_r\\1&!p\end{pmatrix}\right).}
\tag{1.9}
$$



Each side is either $1$ or $p$.  Thus an actual noncentral root is singular
exactly when



$$
\boxed{!p\equiv b_rP_r^{-1}\pmod p.}
\tag{1.10}
$$



This is a useful exact reduction, but it is not an avoidance theorem.  It
replaces the apparently independent condition $p\mid D_h$ by a
prime-dependent, prescribed-residue condition for the left factorial.
No product estimate for primes satisfying (1.10) is presently obtained.

The new exact finite search finds no actual noncentral singular prime in its
tested sets.  It checks the bridge at all 344 noncentral roots for
$p\le5000$, and checks five certified factors $p\mid q_r$ reaching



$$
p=3{,}092{,}690{,}659,
$$



which is $47.0894\ldots$ times the previous item-165 maximum.  Every tested
$D_h$ is nonzero modulo $p$.  This is sparse finite evidence, not an
all-prime theorem.

## 2. Wronskian and determinant bridge -- PROVED

Put



$$
W_n=P_nq_{n-1}-P_{n-1}q_n.
$$



Using the common recurrence in (1.1) gives



$$
W_n=P_{n-2}q_{n-1}-P_{n-1}q_{n-2}=-W_{n-1}.
$$



Since $W_1=3\cdot1-1\cdot1=2$, induction proves (1.7).  In
particular, if an odd prime divides $q_r$, it divides neither $P_r$ nor
$q_{r-1}$.

For completeness, recall the exact first-jet identity for the canonical
$p$-adic interpolation $f_p(n)=(-1)^nq_n$:



$$
f_p'(n)=(-1)^{n+1}\bigl(P_n\mathcal E_p-b_n\bigr),
\qquad
\mathcal E_p=\sum_{j\ge0}j!\in\mathbb Z_p.
\tag{2.1}
$$



Its two initial values are



$$
f_p'(0)=-\mathcal E_p,
\qquad f_p'(1)=3\mathcal E_p-4.
$$



Differentiating the interpolation recurrence and propagating these two
values gives exactly (1.1)--(1.2), hence (2.1).  This is the archived
all-integer Euler-jet theorem; no numerical interpolation is used here.
The exact archive dependency is
`sources/bessel_padic_all_integer_jet_euler_obstruction.md`, pinned at
SHA-256
`fb68cec8ec01ca9dcfa39eb86af61f76a9bba07f18a6e955668ef2e90f89696e`.
Since $j!\equiv0\pmod p$ for $j\ge p$,



$$
\mathcal E_p\equiv !p\pmod p.
\tag{2.2}
$$



On a root disk, the exact derivative/index-slope identity is



$$
f_p'(r)\equiv(-1)^r\delta_p(r)\pmod p.
\tag{2.3}
$$



Item 165 proved, for the tied value $h=(p-3)/2-r$,



$$
\delta_p(r)\equiv-2D_hq_{r-1}\pmod p.
\tag{2.4}
$$



Substitution of (2.1)--(2.2) into (2.3) first gives



$$
E_{p,r}\equiv-\delta_p(r)\pmod p,
$$



and then (2.4) proves (1.6).  Multiplication by $P_r$ and (1.7)
prove (1.8).  Finally



$$
E_{p,r}=\det\!\begin{pmatrix}P_r&b_r\\1&!p\end{pmatrix},
$$



so (1.5), (1.8), and the fact that $P_r$ is a unit prove the exact gcd
identity (1.9) and the prescribed-residue criterion (1.10).

## 3. What the reduction supplies; the product bound remains OPEN

At one saddle index $N$, let $\mathcal S_N$ be any set of actual
noncentral dead singular primes $p>3m$.  For large $m$, $p>2N+1$, so
$r=N$ and



$$
p\mid q_N,
\qquad
!p\equiv b_NP_N^{-1}\pmod p.
\tag{3.1}
$$



The target in (3.1) is the reduction of one fixed rational number for that
$N$, but the left-factorial residue is a different arithmetic datum for
every prime.  The bridge does not itself collect these conditions as
divisors of a single new integer of controlled height.  The unconditional
product divisibility furnished directly by the current argument remains



$$
R_N:=\prod_{p\in\mathcal S_N}p\mid q_N,
\qquad
\log R_N\le N\log N+O(N).
\tag{3.2}
$$



Item 165 showed quantitatively that filling the residual doubled-rate gap
$0.0196329836694\ldots$ requires merely



$$
\log R_N>0.0588989510083\ldots,m,
\tag{3.3}
$$



only $0.0084007101\ldots$ of the available asymptotic $\log q_N$ budget.
Equation (1.10) filters the divisors in (3.2), but no all-prime counting or
product theorem for that prescribed residue has been proved here.  Thus no
quantitative improvement to (3.2) follows from the present identities.  This
is a statement about what the reduction presently proves, not an
impossibility claim about every future use of left-factorial arithmetic.

The ordinary Kurepa conjecture concerns only the zero target $!p\equiv0$.
Andreji\'c, Bostan, and Tatarevic state that conjecture remains open and
report a computation excluding zero residues for every odd prime
$p<2^{40}$; they also give fast algorithms for computing individual or
batched residues:

V. Andreji\'c, A. Bostan, and M. Tatarevic,
[*Improved algorithms for left factorial residues*](https://arxiv.org/abs/1904.09196),
arXiv:1904.09196v3 (2020), later published in *Information Processing
Letters*.

That published computation settles zero-target cases only in its finite
range.  Most targets $b_NP_N^{-1}$ are nonzero, so neither the Kurepa
conjecture nor its verification to $2^{40}$ implies (1.10) is avoided.
Calling (1.10) a **Kurepa-type reformulation** is accurate; calling it an
equivalence to Kurepa, an impossibility theorem, or a product bound would be
an overclaim.

## 4. Primality is essential -- PROVED counterexample to an unscoped claim

An initially tempting strengthening was



$$
\gcd(q_r,D_h,2r+2h+3)=1
\quad\hbox{for all }r,h.
\tag{4.1}
$$



It is false.  Exact integer arithmetic gives



$$
79\mid q_{39},\qquad79\mid D_{78},\qquad
2\cdot39+2\cdot78+3=237=3\cdot79.
\tag{4.2}
$$



The finite grid finds the same periodic factor in further composite tied
integers.  This does not produce a singular prime, because the tied integer
in (4.2) is composite and the singular theorem requires it itself to be the
prime $p$.  It does prove that no proof may silently replace the prime-tied
statement by the unscoped coprimality assertion (4.1).

There is also no recurrence-only exclusion.  Item 165 constructed a
modified-initial-data dead singular example at $p=107,h=2,r=50$ by replacing
the initial pair $(1,1)$.  That comparison is **not** an example for the
actual Bessel seed.  The new determinant $E_{p,r}$ is precisely where the
actual seed enters.

## 5. Exact finite diagnostics -- EXPERIMENTAL FINITE

### 5.1 Direct bridge census

For every odd prime $p\le5000$, the certificate reconstructs the recurrence
modulo $p^2$, evaluates $!p$, $P_r$, $b_r$, and $D_h$, and checks at every
noncentral root



$$
\delta_p(r)=-2D_hq_{r-1},\qquad
E_{p,r}=-\delta_p(r)=2D_hq_{r-1},
$$



as well as the Wronskian.  It finds 344 noncentral roots, 344 successful
bridge checks, and zero singular roots.

Three actual roots have zero target $b_r\equiv0\pmod p$ in the displayed
diagnostics:



$$
(p,r,h)=(7,2,0),\ (13,4,1),\ (2879,48,1390).
$$



Direct left-factorial evaluation gives respectively



$$
!p\equiv6,\ 10,\ 142\pmod p,
$$



so all three are ordinary.  These examples illustrate the zero-target
Kurepa subcase; they do not show all actual targets vanish.

### 5.2 Tied gcd grid

The certificate checks all 250,500 pairs



$$
1\le r\le500,\qquad0\le h\le500.
$$



There is no pair for which the tied integer $2r+2h+3$ is prime and divides
both $q_r$ and $D_h$.  The same grid supplies the composite failure (4.2).
This finite grid reaches tied primes only up to 2003 and is subordinate to
the direct $p\le5000$ census; its main value is falsifying (4.1).

### 5.3 Sparse billion-scale search

Five independently certified prime factors $p\mid q_r$ were tested:

| $p$ | $r$ | $h=(p-3)/2-r$ | $D_h\bmod p$ | result |
|---:|---:|---:|---:|:---|
| 105,220,393 | 74 | 52,610,121 | 31,155,715 | ordinary |
| 515,574,659 | 18 | 257,787,310 | 191,377,629 | ordinary |
| 1,331,511,677 | 45 | 665,755,792 | 1,328,938,593 | ordinary |
| 2,452,487,773 | 42 | 1,226,243,843 | 1,097,291,826 | ordinary |
| 3,092,690,659 | 16 | 1,546,345,312 | 2,217,484,827 | ordinary |

The last computation evaluates over 1.5 billion exact continuant steps.
The modular multiplication splits an input at $B=2^{18}$ and checks



$$
2Bp\le1{,}621{,}460{,}600{,}225{,}792
<2^{53}-1.
$$



Thus every integer product and sum used by the split formula is exactly
represented.  The quotient used in the final modular reduction is below
$2B=524{,}288$; even the conservative binary64 division-error bound
$2B\,2^{-52}$ is smaller than $1/p$ at the largest tested prime.  The
intermediate split quotient has the still smaller bound $p/B$.  Hence a
nonintegral quotient cannot round across an integer boundary, while an exact
integral quotient is representable.  The remainders are therefore the exact
integer remainders.  The certificate also cross-checks representative split
products against `BigInt` arithmetic.  This is not a probabilistic or
approximate floating-point test.

The five factors are sparse.  The result does not claim a complete
factorization of all $q_r$, an exhaustive scan below the maximum, density
zero, or finite absence.

## 6. Status ledger

### PROVED

- The Wronskian (1.7).
- The fixed-seed Euler-residual bridge (1.6) and determinant form (1.8).
- The exact gcd/resultant identity (1.9).
- The prescribed left-factorial criterion (1.10).
- The product divisibility $R_N\mid q_N$ for the selected dead singular
  primes, and the exact additional filter (3.1).
- The composite tied counterexample (4.2) to the unscoped coprimality claim.

### EXPERIMENTAL FINITE

- No singular root among 344 direct noncentral roots for $p\le5000$.
- No prime-tied common divisor on the $r,h\le500$ grid.
- No singular root among five sparse certified factors through
  $p=3{,}092{,}690{,}659$.
- The cited published zero-target search through $2^{40}$ is computational
  evidence about ordinary Kurepa residues, not a prescribed-target theorem.

### OPEN

- Whether the actual Bessel seed has any noncentral singular prime.
- Any all-prime bound making the product of such primes $o(m)$, or merely
  smaller than the threshold in (3.3), at saddle-compatible $N$.
- An actual singular counterexample or a positive-logarithmic-mass family.
- Simultaneous synchronization with the separate coefficient divisibility
  and small common-root conditions needed by the full matching branch.

Nothing here proves irrationality, rationality, or transcendence of
$e+\pi$.

## 7. Replay

From the research archive root, run the eventual archived copy as one line:

```text
node scripts/item166_actual_singular_certificate.js --output results/item166_actual_singular_certificate.json
```

For a byte-identical replay, direct `--output` to a temporary file and
compare it with the pinned JSON.  The companion SHA-256 manifest pins the
report, script, and JSON, and records the pinned archived Euler-jet source
dependency.
