> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 164: singular equal-valuation matching and its support-scale barrier

Date: 2026-08-29 (Beijing time)

## 1. Verdict

The singular branch has an exact first-level matching law that differs sharply
from the ordinary branch.

If a root $r\bmod p$ is singular but dies modulo $p^2$, and
$v_p(b_m)=v_p(q_N)=1$, then the last matching digit is **all or none on the
entire root fibre**. When its one coefficient congruence holds, every
parity-compatible lift of $r\bmod p$ contributes



$$
p^2\mid\Delta_{m,N}g_{m,N}
$$



while imposing only a class modulo $2p$, rather than the ordinary modulus
$2p^2$. Thus dead singular primes offer a genuine “free doubling” mechanism.

Two rigorous restrictions substantially narrow that mechanism.

1. Every central singular prime used at one index divides $2N+1$. Hence the
   product of all distinct central singular primes divides $2N+1$, and even
   perfect first-level doubling has zero exponential rate when
   $N=O(m/\log m)$.
2. More generally, even if **every** prime $p\le3m$ were singular, divided
   $b_m$, and passed the final congruence, its fully doubled radical would
   have rate at most $1$ per $6m$. After the proved rank-one divisor this
   remains

   

$$
0.01963298366943179388\ldots
$$



   below the route target. A rank-one-plus-first-level-singular completion
   must therefore use positive logarithmic mass above $3m$, or use deeper
   powers or another arithmetic source.

The remaining first-level escape is precise but open: a positive-mass family
of **noncentral dead singular primes**, including primes above $3m$, must
simultaneously divide the actual $b_m$ and $q_N$ and satisfy one normalized
coefficient congruence at the same saddle-compatible index. No such theorem is
known.

## 2. Signed root-fibre coordinates

Let



$$
q_0=q_1=1,\qquad q_N=(4N-2)q_{N-1}+q_{N-2},
$$



and let $p_N$ denote the companion beta numerator. Fix an odd prime $p$
and a root $r\in\{0,\ldots,p-1\}$ of $q_r\bmod p$. Put



$$
\lambda_p(r)=\frac{q_r}{p}\pmod p,
 \qquad
 \delta_p(r)=\frac{-q_{r+p}-q_r}{p}\pmod p.
\tag{2.1}
$$



For $N=r+tp$, the exact affine lift law is



$$
\boxed{
 \frac{(-1)^tq_N}{p}
 \equiv\lambda_p(r)+t\delta_p(r)\pmod p.}
\tag{2.2}
$$



A root is ordinary when $\delta_p(r)\ne0$, and singular when
$\delta_p(r)=0$. Equation (2.2) gives the complete first-level trichotomy.

- Ordinary: exactly one $t\bmod p$ lifts the root to $p^2$.
- Singular dead fibre: $\lambda_p(r)\ne0$, so every lift has exact
  $p$-adic valuation one and none lifts to $p^2$.
- Singular all-lift fibre: $\lambda_p(r)=0$, so all $p$ lifts are roots
  modulo $p^2$.

The last case is the separate all-lift/Wieferich obstruction. It must not be
identified with the dead singular branch.

## 3. Exact singular matching theorem

Write the primitive positive form as



$$
L=a+\varepsilon b\pi>0,
 \qquad\gcd(a,b)=1,
 \qquad\varepsilon=(-1)^N,
$$



and define



$$
\Delta=\gcd(b,q_N),\qquad
 P^*=\frac b\Delta p_N-\varepsilon\frac{q_N}{\Delta}a,
 \qquad g=\gcd(P^*,\Delta).
$$



Assume



$$
v_p(b)=v_p(q_N)=1.
\tag{3.1}
$$



Multiplication of $P^*$ by the $p$-unit $\Delta/p$ shows that
$p\mid P^*$ is equivalent to



$$
\frac bp p_N-\varepsilon\frac{q_N}{p}a\equiv0\pmod p.
\tag{3.2}
$$



Let $s=(-1)^r$. The beta numerator period gives
$p_N\equiv p_r\pmod p$, while
$\varepsilon=s(-1)^t$. Substitution of (2.2) into (3.2) yields



$$
\boxed{
 \frac bp p_r-sa\bigl(\lambda_p(r)+t\delta_p(r)\bigr)
 \equiv0\pmod p.}
\tag{3.3}
$$



This gives two exact alternatives.

### Ordinary root

The slope in (3.3) is a unit, so exactly one $t\bmod p$ matches. At that
solution the normalized $q_N/p$ is a unit, so (3.1) remains exact. The root
and matching digit together select one parity-compatible class modulo
$2p^2$, matching the archived transverse theorem.

### Singular root

Equation (3.3) is independent of $t$. If $\lambda_p(r)\ne0$, every lift
has exact $v_p(q_N)=1$, and



$$
\boxed{
 p\mid g
 \quad\Longleftrightarrow\quad
 \frac bp p_r-sa\lambda_p(r)\equiv0\pmod p.}
\tag{3.4}
$$



When (3.4) holds, every parity-compatible lift matches; otherwise none does.
Thus $p^2\mid\Delta g$ costs only the base root class modulo $p$.

If instead $\lambda_p(r)=0$, every lift has $v_p(q_N)\ge2$. With
$v_p(b)=1$, equal valuation fails and $p\nmid g$. Matching at level two
or higher requires new divided data on the all-lift fibre and remains open.

## 4. Simultaneous dead singular primes: the possible mechanism

Let $\mathcal S_m$ be distinct dead singular primes satisfying (3.1),
(3.4), and their root congruences at one $N$. Put



$$
R_m=\prod_{p\in\mathcal S_m}p.
$$



Coprimality gives



$$
\boxed{R_m^2\mid\Delta_{m,N}g_{m,N}.}
\tag{4.1}
$$



The root classes use only one class modulo $R_m$; parity changes this to
one class modulo $2R_m$. This is the singular modulus compression: ordinary
matching would use modulus $2R_m^2$.

It does not by itself produce a small index. The actual
$N=O(m/\log m)$ must still be an exceptionally small representative of the
moving class modulo $R_m$, and the same primes must divide the moving
coefficient $b_m$ and satisfy (3.4).

At the balanced beta scale,



$$
\frac{\log q_N}{6m}\longrightarrow
 \theta=1.1685311871794864979\ldots.
$$



After the rank-one divisor the missing rate is



$$
T_1=1.0196329836694317939\ldots.
$$



If fully doubled dead singular radicals alone supply it, necessarily



$$
\frac{\log R_m}{6m}>\frac{T_1}{2}
 =0.5098164918347158969\ldots,
\tag{4.2}
$$



or equivalently they must capture more than



$$
\frac{T_1}{2\theta}
 =0.4362883057193132808\ldots
\tag{4.3}
$$



of the entire logarithmic height of $q_N$. These are necessary capacity
conditions, not evidence that the family exists.

## 5. Two support-scale no-go theorems

### 5.1 Central singular primes

If $r=(p-1)/2$ and $N\equiv r\pmod p$, then



$$
p\mid2N+1.
$$



Consequently, for any set of distinct central singular primes occurring at
one index,



$$
\boxed{
 R_m^{\mathrm{cent}}\mid2N+1.}
\tag{5.1}
$$



Even if every one is dead and passes (3.4),



$$
\log\bigl((R_m^{\mathrm{cent}})^2\bigr)
 \le2\log(2N+1)=o(m)
\tag{5.2}
$$



for $N=O(m/\log m)$. Thus central first-level singular matching has zero
exponential rate. Central all-lift higher powers are not covered by (5.2).

### 5.2 Bounded support, including the $3m$ ceiling

For any distinct-prime family supported on $p\le x_m$, the prime number
theorem gives



$$
\log R_m\le\sum_{p\le x_m}\log p=x_m+o(x_m).
\tag{5.3}
$$



Hence $x_m=o(m)$ gives zero rate even after doubling. More sharply, if
$x_m=\alpha m$, the most optimistic doubled rate is at most



$$
\frac{2\log R_m}{6m}\le\frac\alpha3+o(1).
\tag{5.4}
$$



For $\alpha=3$, this ceiling is $1$, below $T_1$ by



$$
T_1-1=0.01963298366943179388\ldots.
\tag{5.5}
$$



More generally, a support cutoff below



$$
\alpha_{\rm crit}=3T_1
 =3.0588989510082953816\ldots
\tag{5.6}
$$



cannot close a rank-one-plus-fully-doubled-radical proof. This is deliberately
optimistic: it counts every prime below the cutoff as singular, present in
$b_m$, and successfully matched.

## 6. Exact finite diagnostics

The new Python certificate independently scanned every root of every odd
prime $p\le20000$:

- 2,261 primes and 2,267 roots;
- 2,266 ordinary roots;
- exactly one singular root, $(p,r)=(79,39)$;
- that root is central and dead, with
  $q_{39}/79\equiv12\pmod{79}$;
- all 79 standard lifts were checked and have exact valuation one.

The pinned C++ scan through $p\le200000$ independently contains 17,983
odd primes and 18,013 roots. It likewise finds only $(79,39)$, and no
all-lift branch. Both statements are **EXPERIMENTAL FINITE**, not all-prime
classification.

The exact full matching replay for $m\le100, N\le6m$ found:

- 15,150 candidates and 15,426 $\Delta$-prime slots;
- 190 singular $\Delta$-prime events, all from the dead central prime 79;
- those events occur in 84 rows, always with
  $v_{79}(b)=v_{79}(q_N)=1$;
- exactly one singular final-content hit, at $(m,N,p)=(33,118,79)$;
- the coefficient test (3.4) vanishes exactly in the row $m=33$;
- every central radical check divides $2N+1$, as (5.1) requires.

The single hit is outside the 20%-wide saddle window for $m=33$, whose
target is $N=57$. Neither pinned saddle scan has a singular prime in its
best actual candidate. At $m=64,N=118$, the equal-level upper candidate
contains $p=79$, but its actual $g$ is one.

These frequencies diagnose the transverse coefficient condition; they do not
prove it is asymptotically rare.

## 7. Status ledger

### PROVED

- The signed affine law (2.2) and the dead/all-lift trichotomy.
- The singular all-or-none matching theorem (3.4) at equal valuation one.
- The simultaneous modulus compression (4.1): gain $R_m^2$, index modulus
  $2R_m$.
- The central radical no-go (5.1)--(5.2).
- The support-scale ceilings (5.3)--(5.6), scoped to distinct first-level
  singular primes booked in addition to rank one.

### EXPERIMENTAL

- All finite root-scan and matching-event counts in Section 6.
- Absence of noncentral singular roots through $p=200000$.
- Absence of a singular prime from every best actual saddle candidate tested.

### OPEN

- An all-prime exclusion or logarithmic-mass bound for noncentral singular
  roots.
- A positive-mass family of noncentral dead singular primes above the
  support ceiling, simultaneously dividing $b_m,q_N$ and satisfying (3.4)
  at one saddle-compatible $N$.
- Any higher-power contribution from all-lift singular branches.
- Any combination with deeper internal Cartier digits that fills the residual
  weighted target.

Nothing here proves irrationality, rationality, or transcendence of
$e+\pi$.

## 8. Replay

Run

```text
python scripts/item164_matching_singular_certificate.py --archive . --prime-limit 20000 --output results/item164_matching_singular_certificate.json
```

The certificate and script hashes pinned by the companion manifest are:

```text
190412c5979aeeddcaf16cd6e2be5c042a6379bb6d0b8647b46a19fad491f81a  scripts/item164_matching_singular_certificate.py
8dee60c71a5b3c1f7826c8134fa2602d2e2a5d3c8953c1ecbdaa4a708d012ce3  results/item164_matching_singular_certificate.json
```
