> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item-162 adversary: what an eta-zero theorem can and cannot buy

Date: 2026-08-28

## 1. Verdict

Let $\mathcal H_m$ be the item-149 rank-one prime set and
$\mathcal Z_m$ the item-151 rank-two determinant-zero set.  For every
$p\in\mathcal H_m\cup\mathcal Z_m$, item 161 gives the exact lifted digit



$$
\eta_{m,p}\equiv {q_pA_m\over p^{1+\delta_{m,p}}}\pmod p,
$$



and



$$
\eta_{m,p}=0\quad\Longleftrightarrow\quad p^2\mid c_m.          \tag{1.1}
$$



The conclusions are:

- **PROVED:** there is an exact weighted eta-plus-matching statement that
  would suffice; it is formula (3.4) below.  Its matching factors must be
  recomputed after the full actual $c_m$-division.
- **PROVED NO-GO:** no theorem about zeros of this first lifted digit on
  $\mathcal H_m\cup\mathcal Z_m$ can by itself close the internal-content
  route.  Even if every possible forced prime had two surviving digits, the
  absolute optimistic rate would be only
  

$$
0.5698162598434433286409096558\ldots
$$


  per $6m$, below the required
  $1.1561471519642446123307302239\ldots$.
- **PROVED:** fixed primes, primes confined to $p\le m^\alpha$ with
  $\alpha<1$, finitely many exact affine rays, and finitely many fixed
  polynomial-divisor rays have zero logarithmic rate.
- **EXPERIMENTAL:** the 45 zeros in the $m\le30$ certificate occur at only
  six primes, $3,5,7,11,19,31$.  Their counts cannot imply a positive
  asymptotic rate.
- **OPEN:** a positive-mass eta-zero theorem in linear-scale prime bands;
  higher lifted digits; or enough sequential matching mass to cross the
  remaining threshold.

## 2. Exact eta-zero ledger

Put



$$
R_{H,m}=\sum_{p\in\mathcal H_m}\log p,
\qquad
R_{Z,m}=\sum_{p\in\mathcal Z_m}\log p.                         \tag{2.1}
$$



The two sets are disjoint in the item-151 classification.  Define



$$
\mathcal H_m^0=\{p\in\mathcal H_m:\eta_{m,p}=0\},
\qquad
\mathcal Z_m^0=\{p\in\mathcal Z_m:\eta_{m,p}=0\},              \tag{2.2}
$$



and the extra second-digit weight



$$
E_{\eta,m}=
\sum_{p\in\mathcal H_m^0\cup\mathcal Z_m^0}\log p.            \tag{2.3}
$$



Items 149 and 151 supply one copy of every prime in
$\mathcal H_m\cup\mathcal Z_m$; equation (1.1) supplies exactly one
additional certified copy at every eta zero.  Hence



$$
\boxed{
\log c_m\ge R_{H,m}+R_{Z,m}+E_{\eta,m}.}                       \tag{2.4}
$$



This is a lower bound, not an equality: actual $c_m$ may contain other
primes or deeper powers.

The proved rank-one rate is



$$
{R_{H,m}\over6m}\longrightarrow
r_1=0.1365141682948128184504238226\ldots .                     \tag{2.5}
$$



The rank-two radical currently has only the upper ceiling



$$
\limsup {R_{Z,m}\over m}\le
C_2=0.8903637697614530752201860316\ldots .                     \tag{2.6}
$$



Nothing in the finite eta certificate improves (2.5) or turns (2.6) into a
positive lower bound.

## 3. The weighted theorem that would actually suffice

At the optimal beta scale, the frozen matching criterion is



$$
\liminf {\log(c_m\Delta_{m,N_m}g_{m,N_m})\over6m}
>T,
$$



where



$$
T=h-d/2=1.1561471519642446123307302239\ldots .                 \tag{3.1}
$$



After booking the proved rank-one rate, the exact deficit is



$$
D=T-r_1
=1.0196329836694317938803064012\ldots .                       \tag{3.2}
$$



Combining (2.4) with the matching criterion gives the clean sufficient
statement



$$
\boxed{
\liminf_{m\to\infty}
{R_{Z,m}+E_{\eta,m}
 +\log\Delta_{m,N_m}+\log g_{m,N_m}\over6m}>D.}                \tag{3.3}
$$



If a proposed theorem controls only eta-zero sets and not all of
$\mathcal Z_m$, the still more explicit sufficient condition is



$$
\boxed{
\liminf {\displaystyle
 \sum_{p\in\mathcal H_m^0}\log p
+2\sum_{p\in\mathcal Z_m^0}\log p
+\log\Delta_{m,N_m}+\log g_{m,N_m}
\over6m}>D.}                                                  \tag{3.4}
$$



Indeed, a zero in $\mathcal Z_m$ supplies both the previously unbooked
rank-two radical and the new second digit.

Equations (3.3)--(3.4) require the **sequential** definitions



$$
\Delta_{m,N}=\gcd(b_m,q_N),\qquad b_m=|V_m|/c_m,
$$



followed by the primitive final content $g_{m,N}$.  It is invalid to
compute either matching factor from $V_m$, or from a pair divided only by
the eta-certified lower divisor rather than the full actual $c_m$.

Thus an eta-zero theorem can be sufficient only as one component of a
larger sequential mass theorem.  It is not sufficient in isolation.

## 4. Absolute ceiling for the first two forced digits

Since



$$
E_{\eta,m}\le R_{H,m}+R_{Z,m},                                 \tag{4.1}
$$



the entire mass certified by the radical layer and the eta layer is at most



$$
R_{H,m}+R_{Z,m}+E_{\eta,m}
\le2(R_{H,m}+R_{Z,m}).                                         \tag{4.2}
$$



Using (2.5)--(2.6),



$$
\limsup {R_{H,m}+R_{Z,m}+E_{\eta,m}\over6m}
\le2\left(r_1+{C_2\over6}\right)
=0.5698162598434433286409096558\ldots .                       \tag{4.3}
$$



This misses $T$ by at least



$$
\boxed{
0.5863308921208012836898205681\ldots\quad\text{per }6m.}      \tag{4.4}
$$



Equations (4.3)--(4.4) are a ceiling on what the **current two-layer proof
mechanism** can certify.  They are not upper bounds on actual $c_m$.

There is an even simpler support ceiling.  Every forced prime satisfies
$p<2m$, so one additional eta layer has weight at most



$$
\sum_{p<2m}\log p=2m+o(m),                                    \tag{4.5}
$$



or $1/3+o(1)$ per $6m$.  The sharper (4.3) uses the exact rank-one mass
and the item-151 rank-two interval ceiling.

More generally, if one somehow certified $j$ complete surviving digits at
every item-149/item-151 forced prime, their absolute optimistic rate would
be at most



$$
j\left(r_1+{C_2\over6}\right).
$$



Even $j=4$ gives only



$$
1.1396325196868866572818193115\ldots<T,                       \tag{4.6}
$$



still short by $0.0165146322773579550489109123\ldots$.  Five
complete digits are the first layer count not excluded by this radical
ceiling.  This is only a capacity calculation; no such uniform higher lift
is proved.

## 5. Why the 45 finite zeros have no positive-rate consequence

The exact $m\le30$ certificate has 45 eta-zero rows:



$$
33\text{ rank-one rows},\qquad12\text{ rank-two rows}.
$$



Their distinct primes are exactly



$$
\{3,5,7,11,19,31\}.                                           \tag{5.1}
$$



The largest observed eta-zero weight is at $m=17$, where it is



$$
0.07449411107180356\ldots\quad\text{per }6m.                  \tag{5.2}
$$



These are finite diagnostics only.  Even the hypothetical uniform
continuation “every prime in (5.1) is an eta zero whenever eligible” would
give, for each $m$, at most



$$
\log(3\cdot5\cdot7\cdot11\cdot19\cdot31)=13.4302818\ldots,    \tag{5.3}
$$



and hence zero after division by $6m$.  Repetition in $m$ does not add
weight within a single approximant.  Positive rate requires a growing set
of distinct primes at each $m$.

The data therefore do not even suggest the type of mass theorem needed in
(3.3): almost all observed zeros are at small fixed primes, whereas positive
logarithmic mass must come from a growing linear-scale population.

## 6. Rigorous no-go classes for thin zero patterns

The following conclusions use only elementary prime support and apply to
either the once-weighted eta layer or the twice-weighted zero-only expression
in (3.4).

### 6.1 Fixed primes

For every fixed finite set of primes $S$,



$$
\sum_{p\in S,\ \eta_{m,p}=0}\log p\le\sum_{p\in S}\log p=O(1).
$$



Thus any fixed-prime pattern has rate zero, even if it holds for every
large $m$.

### 6.2 Sublinear prime support

If all eta-zero primes lie below $m^\alpha$ for a fixed $\alpha<1$,
Chebyshev's bound gives



$$
\sum_{p\le m^\alpha}\log p=O(m^\alpha)=o(m).                  \tag{6.1}
$$



More generally, support below $\varepsilon_m m$ with
$\varepsilon_m\to0$ has weight $o(m)$.  Hence the visible small-prime
clusters cannot close the route without a separate theorem on growing
valuations, which eta alone does not provide.

### 6.3 Finitely many exact affine rays

An exact ray $p=a m+b$ contains at most one candidate prime for each
$m$, of weight $O(\log m)$.  Any fixed finite collection of such rays
therefore has rate zero.

### 6.4 Fixed polynomial-divisor rays

Suppose every prime in a proposed family divides one of finitely many fixed
nonzero polynomials $F_1(m),\ldots,F_J(m)\in\mathbb Z[m]$.  The product of
the distinct primes divides



$$
\prod_{j=1}^J|F_j(m)|
$$



apart from finitely many exceptional zero values.  Therefore its logarithm
is $O(\log m)$, again rate zero.  This covers the familiar thin moving rays
that become divisors of fixed linear integers in $m$.

These no-go statements do **not** apply to a whole linear-scale interval
$\alpha m<p<\beta m$, or to a positive-density subset of primes in such
intervals.  That is precisely the scale on which a useful eta-zero theorem
would have to operate.  Since every $p<2m$ has $\log p=O(\log m)$, a
positive constant rate also requires on the order of $m/\log m$ distinct
zero primes at a typical large index.

## 7. Replay and status

Run

```text
python scripts/eta_zero_mass_adversary_check.py
```

The checker pins
`results/lifted_endpoint_hasse_certificate_m30.json` at SHA-256
`54025499d507749259d7d52a231f5594a77885bf0bf1ee0df747d94d86afde3c`,
recomputes the finite zero counts and support, and evaluates the exact
capacity constants in (4.3)--(4.4).

Final classification:

- **PROVED:** (2.4), sufficient sequential criteria (3.3)--(3.4), the
  two-digit capacity ceiling (4.3), and all thin-pattern no-go bounds.
- **EXPERIMENTAL:** the 45-row zero census and observed finite rates.
- **OPEN:** positive linear-scale eta-zero mass, deeper lifted digits, and
  any matching lower bound after full sequential normalization.

This item does not prove the irrationality or transcendence of $e+\pi$.
