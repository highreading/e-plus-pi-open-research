> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 393 — Small-prime primitive remainder: exact de-overlap, total ceiling, and decisive valuation strata

Date: 2026-09-01  
Status: **CANONICAL, ROOT-AUDITED, NO BOOKING**

## 1. Verdict

Item 390 isolates the complete $p>6m$ common-content component.  This
item treats the complementary actual-family factor at $p\le6m$, after
removing every genuinely available baseline exactly once.

Let



$$
\mathcal B_m=2\prod_{p\in\mathcal H_m}p.
 \tag{1.1}
$$



The dyadic factor is the frozen deterministic common clearing factor, and
the product over $\mathcal H_m$ is the only positive-rate booked Cartier
factor.  Define



$$
c_{m,\le}^{\rm rem}
 =\prod_{p\le6m}
 p^{v_p(c_m)-\mathbf1_{p=2}-\mathbf1_{p\in\mathcal H_m}},
 \tag{1.2}
$$



and retain Item 390's



$$
c_m^>=\prod_{p>6m}p^{v_p(c_m)}.
 \tag{1.3}
$$



Then the actual content has the exact primewise factorization



$$
\boxed{c_m=\mathcal B_m\,c_{m,\le}^{\rm rem}\,c_m^>,}
 \qquad
 \gcd(\mathcal B_mc_{m,\le}^{\rm rem},c_m^>)=1.
 \tag{1.4}
$$



The sharpest currently rigorous general upper bound for the remaining
small-prime factor is



$$
\boxed{
 \limsup_{m\to\infty}
 \frac{\log c_{m,\le}^{\rm rem}}{6m}
 \le
 \left(h-\frac d{\mu_\pi}\right)-r_1
 =1.8591489918666\ldots .}
 \tag{1.5}
$$



Using a rational number strictly above the frozen Zeilberger--Zudilin bound
and certified one-sided intervals for $h,d,r_1$, the completely explicit
safe version is



$$
\boxed{
 \limsup_{m\to\infty}
 \frac{\log c_{m,\le}^{\rm rem}}{6m}
 <1.859148991866686.}
 \tag{1.6}
$$



This does not lower the compatible total-content ceiling: Item 390 supplies
an upper bound, not a positive lower bound, for $c_m^>$, so it cannot be
subtracted from the full-content bound.

The main decision theorem is instead layerwise.

* One complete post-booking residual valuation layer over **all** primes
  $p\le6m$ has capacity at most $1$ per $6m$.  Since
  $T-r_1=1.0196329836694317\ldots$, small-prime success forces the second
  post-booking layer and deeper to carry at least
  

$$
0.01963298366943179388\ldots .
  \tag{1.7}
$$


* In the intrinsic raw valuation tower, the first radical layer has capacity
  at most $1$.  Therefore all raw layers $v_p(c_m)\ge2$ together must
  carry at least
  

$$
T-1=0.15614715196424461233\ldots .
  \tag{1.8}
$$


* On the declared forced Cartier support, four complete raw layers have
  ceiling
  

$$
4C_{\rm rad}=1.13963251968688665728\ldots<T.
$$


  Hence a forced-support-only success requires fifth-and-deeper raw
  valuation mass at least
  

$$
T-4C_{\rm rad}
  =0.01651463227735795505\ldots .
  \tag{1.9}
$$


  Equivalently, the Item-163 fifth gate, or content outside the forced
  support, is indispensable.

Thus the small-prime branch remains live, but the surviving capacity has
been localized to precise deeper strata rather than an undifferentiated
smooth-support reservoir.

## 2. What can actually be removed

The frozen normalization is



$$
U_m=\frac{2\widehat A_m}{T_mG_m},
 \qquad
 V_m=\frac{K_m\widehat B_m}{G_m},
 \qquad
 c_m=\gcd(U_m,V_m).
 \tag{2.1}
$$



Three de-overlap points are essential.

1. The Cartier product $G_m$ has already been divided out in (2.1).  It
   is not a factor of $c_m$ available for a second subtraction.
2. The lcm clearing factors $M,T,K$ do not form one further common scalar.
   Their primewise exponents enter $U_m,V_m$ differently.  Removing a
   whole copy of $M$ or $T$ from $c_m$ would therefore be invalid.
3. The exact guaranteed post-normalization factors are the one dyadic copy
   and the booked rank-one product in (1.1).  Item 149 proves
   $\mathcal B_m\mid c_m$, and
   

$$
\frac{\log\mathcal B_m}{6m}\longrightarrow
   r_1=0.13651416829481281845\ldots .
   \tag{2.2}
$$



The exponents in (1.2) are consequently nonnegative.  The supports in
(1.2) and (1.3) are disjoint, proving (1.4) without any asymptotic
approximation.

## 3. The quantitative total ceiling for the small remainder

The frozen irrationality-measure argument gives



$$
\limsup_{m\to\infty}\frac{\log c_m}{6m}
 \le C_\pi:=h-\frac d{\mu_\pi}
 =1.9956631601614\ldots .
 \tag{3.1}
$$



Since $c_m^>\ge1$, (1.4) implies



$$
\log c_{m,\le}^{\rm rem}
 \le\log c_m-\log\mathcal B_m.
$$



Taking a limsup and using (2.2) proves (1.5).

For an explicit one-sided numerical statement, use



$$
\bar\mu=7.103205334138
 >7.1032053341370017275\ldots,
$$



the certified upper endpoint



$$
h<2.3246783391437311102576951141305620522234564135413822,
$$



and the certified lower endpoint



$$
d>2.3370623743589729958539297805468573066534630858270130.
$$



Exact rational arithmetic gives



$$
h-\frac d{\bar\mu}<1.995663160161498.
$$



The exact expression for $r_1$ gives, conservatively,



$$
r_1>0.1365141682948128.
$$



Subtracting these one-sided bounds proves (1.6).

This is the sharpest rigorous bound presently isolated for the complete
small-prime primitive remainder.  The safe $\tau=36/5$ measure would give
the weaker bound



$$
2.0000863427049848608-r_1
 =1.8635721744101720\ldots .
$$



### Why Item 390 cannot be subtracted

Item 390 proves



$$
\limsup\frac{\log c_m^>}{6m}\le\frac{\log136}{6}.
$$



An upper bound for a disjoint factor cannot be subtracted from an upper
bound for their product.  A subtraction would require a lower bound for
$c_m^>$, and the only proved one is the zero rate $c_m^>\ge1$.  Hence
the compatible total ceiling remains (3.1).  Adding the separate small and
large ceilings would also be weaker than (3.1), so no such sum is entered
in the ledger.

## 4. Exact post-booking layer cake

For $p\le6m$, define the post-booking residual valuation



$$
w_{m,p}=v_p(c_m)-\mathbf1_{p=2}-\mathbf1_{p\in\mathcal H_m}.
 \tag{4.1}
$$



For every $j\ge1$, put



$$
\mathcal S_j^{\rm rem}(m)
 =\{p\le6m:w_{m,p}\ge j\},
 \qquad
 \Theta_j^{\rm rem}(m)
 =\sum_{p\in\mathcal S_j^{\rm rem}(m)}\log p.
 \tag{4.2}
$$



Then the finite layer-cake identity is exact:



$$
\boxed{
 \log c_{m,\le}^{\rm rem}
 =\sum_{j\ge1}\Theta_j^{\rm rem}(m).}
 \tag{4.3}
$$



Each set in (4.2) is a subset of all primes at most $6m$, so the prime
number theorem gives



$$
\limsup\frac{\Theta_j^{\rm rem}(m)}{6m}\le1
 \qquad\text{for every fixed }j.
 \tag{4.4}
$$



Suppose the small-prime internal content alone crosses the analytic
threshold.  Equations (2.2), (4.3), and (4.4) force



$$
\liminf
 \frac1{6m}\sum_{j\ge2}\Theta_j^{\rm rem}(m)
 \ge T-r_1-1
 =0.01963298366943179388\ldots,
 \tag{4.5}
$$



with strict inequality when the threshold is crossed with a fixed positive
margin.  Thus a theorem confined to the first post-booking residual layer
cannot complete the route.

The first residual layer already mixes two logically different events:

* a second valuation at a booked prime $p\in\mathcal H_m$;
* a first valuation at an unbooked prime.

Equation (4.2) counts each exactly once.  Adding separate radical ceilings
for these two events without respecting their disjoint prime supports would
be weaker and risks double counting.

## 5. Intrinsic raw layers

For comparison, define



$$
\mathcal S_k^{\rm raw}(m)
 =\{p\le6m:v_p(c_m)\ge k\},
 \qquad
 \Theta_k^{\rm raw}(m)
 =\sum_{p\in\mathcal S_k^{\rm raw}(m)}\log p.
$$



Then



$$
\log\prod_{p\le6m}p^{v_p(c_m)}
 =\sum_{k\ge1}\Theta_k^{\rm raw}(m).
 \tag{5.1}
$$



The raw radical layer $k=1$ has rate at most $1$.  Therefore a
small-prime internal-content proof of rate exceeding $T$ necessarily
satisfies



$$
\liminf\frac1{6m}
 \sum_{k\ge2}\Theta_k^{\rm raw}(m)
 \ge T-1
 =0.15614715196424461233\ldots .
 \tag{5.2}
$$



This is the cleanest baseline-independent multiplicity target.  It explains
why a support theorem by itself cannot close Route 1: even the impossible
best case in which every prime $p\le6m$ divides $c_m$ still needs a
positive linear mass of second and deeper valuations.

## 6. Forced Cartier/Witt strata

Let



$$
\mathcal F_m=\mathcal H_m\cup\mathcal Z_m
$$



be the actual rank-one plus vanishing rank-two forced support.  Item 151's
rank-two interval envelope and Item 149 give



$$
\limsup\frac1{6m}
 \sum_{p\in\mathcal F_m}\log p
 \le C_{\rm rad}
 =0.28490812992172166432\ldots .
 \tag{6.1}
$$



For every fixed raw depth $k$, the forced stratum



$$
\mathcal F_{m,k}=\{p\in\mathcal F_m:v_p(c_m)\ge k\}
$$



is contained in $\mathcal F_m$.  Hence each complete forced layer has the
same ceiling $C_{\rm rad}$.  The first four layers therefore satisfy



$$
\limsup\frac1{6m}
 \sum_{k=1}^4\sum_{p\in\mathcal F_{m,k}}\log p
 \le4C_{\rm rad}
 =1.13963251968688665728\ldots<T.
 \tag{6.2}
$$



Consequently, if all positive-rate small content is confined to the forced
support, then



$$
\liminf\frac1{6m}
 \sum_{k\ge5}\sum_{p\in\mathcal F_{m,k}}\log p
 \ge T-4C_{\rm rad}
 =0.01651463227735795505\ldots .
 \tag{6.3}
$$



Five complete layers have ceiling



$$
5C_{\rm rad}=1.42454064960860832160\ldots>T,
$$



so the fifth layer is the first forced-support depth not excluded by
capacity.

On the positive-mass $e=1$ bands, Item 163 identifies its exact gate:



$$
p^5\mid c_m
 \Longleftrightarrow
 a_0=a_1=a_2=a_3=b_0=b_1=b_2=0.
 \tag{6.4}
$$



Thus (6.3) is not a vague request for “more digits.”  It identifies the
first raw stratum whose weighted mass can change the forced-support
decision.  Alternatively, an off-forced small-prime theorem may replace
part of (6.3), but its contribution must remain primewise disjoint from
$\mathcal F_m$.

## 7. Resulting branch classification

### Proved quantitative ceilings

* Complete small-prime primitive remainder:
  

$$
\limsup\frac{\log c_{m,\le}^{\rm rem}}{6m}
  <1.859148991866686.
$$


* Any single post-booking residual layer: rate at most $1$.
* Any fixed forced raw layer: rate at most $C_{\rm rad}$.
* First four forced raw layers together: rate at most
  $1.1396325196868867\ldots$.

### Strata that remain capable of mattering

* Post-booking residual layers $j\ge2$, with required aggregate rate at
  least $0.0196329836694318\ldots$ if small content alone succeeds.
* Raw multiplicity layers $k\ge2$, with required aggregate rate at least
  $0.1561471519642446\ldots$.
* On the forced support, raw layers $k\ge5$, with required aggregate rate
  at least $0.0165146322773580\ldots$, unless off-forced content supplies
  the difference.
* Off-forced primes at $p\le6m$, subject to the universal layer ceiling
  and exact primewise separation from $\mathcal F_m$.

### Not proved

* A total small-prime ceiling below $T-r_1$.
* Any positive weighted mass for the fifth Item-163 gate.
* A uniform valuation bound at $p=2$ or at the $p\le\sqrt m$ tower.
* A weighted upper bound for the off-forced small-prime component.
* A lower bound for Item 390's large-prime factor.
* A new Route-1 booking, Route-1 closure, or irrationality of $e+\pi$.

The small-prime branch therefore cannot yet be closed, but it no longer
needs to be described as “arbitrary smooth content.”  Its exact unresolved
load is the deeper layer cake in (4.5), refined by the forced fifth-layer
target (6.3).

## 8. Replay and dependencies

Deterministic replay:

```text
python scripts/item393_mixed_cubic_small_prime_strata_ceiling_certificate.py \
  --output results/item393_mixed_cubic_small_prime_strata_ceiling_certificate_replay.json
```

The replay verifies:

1. the explicit rationalized $h,d,\bar\mu,r_1$ inequalities behind
   (1.6);
2. every capacity difference in (1.7)–(1.9);
3. the first admissible forced depth;
4. an exact primewise baseline/small/large factorization and both layer-cake
   identities on a transparent algebraic test vector.

The test vector is not actual-row data and makes no finite-density claim.

Primary dependencies:

* `ROUTE1_MASTER_CAPACITY.md`;
* `sources/mixed_cubic_coordinates_and_synchronization_audit.md`;
* `sources/mixed_cubic_small_prime_rank_one_cartier_mass.md`;
* `sources/mixed_cubic_rank_two_cartier_determinant.md`;
* `sources/item163_deeper_digits.md`;
* `sources/item390_mixed_cubic_fresh_primitive_saturation_report.md`.

The canonical artifacts are in `sources/`, `scripts/`, `results/`, and
`manifests/`.  No mass is booked.
