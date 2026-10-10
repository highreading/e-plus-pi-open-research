> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 169: the second divided-index law on a singular all-lift beta orbit

Date: 2026-08-29 (Beijing time)

## 1. Verdict

Let



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2},
$$



let $p\ge 7$ be prime, and let $r$ be a noncentral root modulo $p$.
Write



$$
\lambda_p(r)={q_r\over p}\pmod p,
\qquad
\delta_p(r)={-q_{r+p}-q_r\over p}\pmod p.
$$



This note treats the conditional all-lift case



$$
\boxed{\lambda_p(r)=\delta_p(r)=0.}
\tag{1.1}
$$



Condition (1.1) makes every first-level representative $r+tp$ a root
modulo $p^2$.  The next lift is governed by one explicit cubic
$P_r\in\mathbf F_p[T]$:



$$
\boxed{
p^3\mid q_{r+tp+up^2}
\quad\Longleftrightarrow\quad
P_r(t)=0.}
\tag{1.2}
$$



The right side is independent of $u$.  Therefore each residue class
modulo $p^2$ is exactly one of the following:

- **dead:** $P_r(t)\ne0$, so none of its $p$ children modulo $p^3$
  survives;
- **all-lift:** $P_r(t)=0$, so all $p$ children survive.

There is also an exact fourth-digit law.  At a root $P_r(t)=0$, define
$\kappa_t$ and $\tau_t=P_r'(t)$ as in Section 3.  Then



$$
\boxed{
{(-1)^{t+u+v}q_{r+tp+up^2+vp^3}\over p^3}
\equiv \kappa_t+u\tau_t\pmod p.}
\tag{1.3}
$$



Thus a simple root of $P_r$ selects exactly one second digit $u$,
and every one of the $p$ third digits $v$ above it survives to
$p^4$.  At a multiple root, the branch is dead when $\kappa_t\ne0$
and all $p^2$ pairs $(u,v)$ survive when $\kappa_t=0$.

This is a theorem for the **actual Bessel seed** $(q_0,q_1)=(1,1)$,
conditional only on the local hypothesis (1.1).  It is not inferred from
a finite scan.  No actual-seed noncentral singular orbit, let alone one
satisfying (1.1), is currently known.  Hence Item 169 supplies an exact
local mechanism and a product ceiling, but it does **not** establish a
positive asymptotic matching rate.

## 2. Frozen inputs and hypotheses

For



$$
a_x=(-1)^xq_{r+xp},\qquad D_j=\Delta_x^ja_0,
\tag{2.1}
$$



the archived first-lift law gives



$$
a_x\equiv q_r+xp d_r\pmod {p^2},
\qquad
d_r={-q_{r+p}-q_r\over p}.
\tag{2.2}
$$



The archived all-even anti-period theorem, at order $k=3$, gives



$$
\boxed{
a_x\equiv\sum_{j=0}^{5}D_j\binom xj\pmod {p^4}}
\qquad(x\ge0),
\tag{2.3}
$$



and the valuation facts



$$
p^3\mid D_4,\qquad p^3\mid D_5,\qquad p^4\mid D_6.
\tag{2.4}
$$



The restriction $p\ge7$ is exactly what is needed for $p>2k=6$
and for $1!,\ldots,5!$ to be units in $\mathbf Z_p$.  No assertion in
this note applies the order-three theorem to $p=3$ or $p=5$.

All divided quantities in this report are quotients of integers before
reduction.  For example, $D_j/p^2$ is formed only after (3.1) proves its
integrality, and $B_r(t)/p$ is formed only when $P_r(t)=0$.  A
congruence divided by $p^e$ always loses exactly $e$ powers from its
modulus.  No quotient of a residue-class representative is being used.

The frozen archive dependencies are:

```text
f02b4b936c2ca810299f037e158e7406214e89ef77e8ca98dcd67b2a9bd00911  sources/bessel_denominator_all_lift_branching_wieferich_barrier.md
7fe7bd5b2cef3dcb2a12f49c0c620d8d173d818774701a06f1527d80d574a6be  sources/bessel_prime_cube_fourth_antiperiod_exclusivity.md
95f68e65b3a7458b869cdf610a28e77a9062e1467d78747dc2809563e84a2ee1  sources/bessel_prime_power_second_antiperiod_double_lift.md
c0c834ca8851ddc8dba9edbc9ec74461c0d3aa1b553f79c2320b3d083a0c37de  sources/bessel_all_even_antiperiod_higher_threshold_exclusivity.md
1c0045cf28e78aa6685c2f1337f993f9aa0aa4eeab02851b8cb7c86cf46ff54a  sources/item163_match_adversary_report.md
4c708e21e66a65c41f925ef24cfabe17d231590977691d8b6c6e5c6c51ad8b83  sources/item164_matching_singular_report.md
```

For the noncentral reflection pair we choose



$$
1\le r<s=p-1-r.
\tag{2.5}
$$



Noncentrality is not needed for the local divided law.  It matters for the
matching application because the central support bound
$\prod p\mid 2N+1$ from Item 164 would otherwise force zero exponential
rate.

## 3. Exact second- and third-level theorem — PROVED

### 3.1 Construction of the cubic

Under (1.1), equation (2.2) shows that $p^2\mid a_x$ for every integer
$x\ge0$.  In particular,



$$
p^2\mid D_j\qquad(0\le j\le5).
\tag{3.1}
$$



Define the $p$-integral polynomial



$$
B_r(T)=\sum_{j=0}^{5}{D_j\over p^2}\binom Tj
\quad\hbox{in }\mathbf Z_{(p)}[T],
\tag{3.2}
$$



and reduce it modulo $p$.  By (2.4), its last two terms disappear, so



$$
\boxed{
P_r(T)=B_r(T)\pmod p
=\sum_{j=0}^{3}{D_j\over p^2}\binom Tj
\quad\hbox{in }\mathbf F_p[T].}
\tag{3.3}
$$



The four displayed divided differences are completely explicit:



$$
\begin{aligned}
D_0={}&q_r,\\
D_1={}&-q_{r+p}-q_r,\\
D_2={}&q_{r+2p}+2q_{r+p}+q_r,\\
D_3={}&-q_{r+3p}-3q_{r+2p}-3q_{r+p}-q_r.
\end{aligned}
\tag{3.4}
$$



Divide (2.3) by $p^2$.  The change of modulus is legitimate and gives



$$
{a_x\over p^2}\equiv B_r(x)\pmod {p^2}.
\tag{3.5}
$$



Put



$$
x=t+pu+p^2v,\qquad 0\le t,u,v<p.
\tag{3.6}
$$



Since every denominator through degree five is a $p$-unit, the ordinary
polynomial Taylor identity in $\mathbf Z_p$ gives



$$
B_r(t+pu+p^2v)
\equiv B_r(t)+puB_r'(t)\pmod {p^2}.
\tag{3.7}
$$



Reducing (3.5)--(3.7) modulo $p$ proves (1.2), including its independence
of both higher digits.

### 3.2 The fourth digit

Assume $P_r(t)=0$.  Then $p\mid B_r(t)$, so define



$$
\kappa_t={B_r(t)\over p}\pmod p,
\qquad
\tau_t=P_r'(t)=B_r'(t)\pmod p.
\tag{3.8}
$$



Equation (3.7), divided by $p$, is exactly (1.3).  Consequently:



$$
\begin{array}{c|c|c}
\text{condition}&\text{allowed }u\pmod p&\text{allowed }v\pmod p\\ \hline
\tau_t\ne0&\text{one: }u=-\kappa_t\tau_t^{-1}&\text{all }p\\
\tau_t=0,\ \kappa_t\ne0&\text{none}&\text{none}\\
\tau_t=0,\ \kappa_t=0&\text{all }p&\text{all }p
\end{array}
\tag{3.9}
$$



This also identifies the inherited prime-power slope.  For
$n_t=r+tp$,



$$
\delta_{p^2}(n_t)={-q_{n_t+p^2}-q_{n_t}\over p^2}.
$$



Using $a_{t+p}-a_t=(-1)^tp^2\delta_{p^2}(n_t)$ in (3.7) gives



$$
\boxed{
{\delta_{p^2}(n_t)\over p}
\equiv(-1)^tP_r'(t)\pmod p.}
\tag{3.10}
$$



Thus the derivative in (1.3) is the exact next divided index slope; it is
not an analogy with polynomial-argument Hensel lifting.

There is also a continuant form of the derivative obstruction.  Suppose



$$
n_t=r+tp<{p^2-1\over2},\qquad
H_t={p^2-3\over2}-n_t,
\tag{3.11}
$$



and let



$$
{\cal K}_{H_t}(X)=X{\cal L}_{H_t}(X^2),
\qquad {\cal D}_{H_t}={\cal K}_{H_t}'(0)
$$



be the odd symmetric continuant and its distinguished derivative from
Item 165.  Applying the exact transfer at the odd modulus $p^2$ gives



$$
\delta_{p^2}(n_t)
\equiv-2{\cal D}_{H_t}q_{n_t-1}\pmod {p^2}.
\tag{3.12}
$$



Adjacent beta denominators are coprime, so $q_{n_t-1}$ is a $p$-unit.
Equations (3.10)--(3.12) imply



$$
\boxed{
P_r'(t)
\equiv-2(-1)^t{{\cal D}_{H_t}\over p}q_{n_t-1}\pmod p.}
\tag{3.13}
$$



In particular, $p\mid{\cal D}_{H_t}$, and a multiple root of $P_r$
is equivalent to the deeper condition $p^2\mid{\cal D}_{H_t}$.  Since
$H_t$ is generally of order $p^2$ and
$\log|{\cal D}_{H_t}|=2H_t\log H_t+O(H_t)$, bounding $p$ by this
moving integer is even less effective than the prime-level Item 165
resultant bound.  Different primes again use different continuants.  This
is a rigorous scoped no-go for the direct continuant-height route, not an
exclusion of multiple roots.

### 3.3 Root counts and the zero-polynomial cascade

If $P_r\ne0$, at most three of the $p$ values of $t$ survive to
$p^3$.  Each surviving $t$ has all $p$ values of $u$, so the orbit
has at most $3p$ root classes modulo $p^3$.

If $P_r=0$, all $D_0,\ldots,D_5$ are divisible by $p^3$.  Define



$$
Q_r(T)=\sum_{j=0}^{5}{D_j\over p^3}\binom Tj
\quad\hbox{in }\mathbf F_p[T].
\tag{3.14}
$$



Now $\tau_t=0$ and $\kappa_t=Q_r(t)$.  Hence either $Q_r\ne0$,
in which case at most five values of $t$ have all $p^2$ pairs
$(u,v)$ surviving to $p^4$, or $Q_r=0$, in which case every one of
the $p^3$ triples $(t,u,v)$ survives.  This is the order-three
full-fibre alternative, stated here in the digit coordinates needed by the
matching route.

For the reflected fibre $s=p-1-r$, the archived cube theorem gives



$$
P_s(T)=P_r(-1-T).
\tag{3.15}
$$



Thus a nonzero paired cubic permits at most six first digits and therefore
at most $6p$ root classes modulo $p^3$ across the pair.  If the cubic
vanishes, both fibres are full at that level.

The fourth-digit constants are coupled as well.  If
$t'=-1-t$ and $u'=-1-u$, exact reflection modulo $p^4$, divided by
$p^3$, gives



$$
\boxed{
\kappa_s(t')=\kappa_r(t)-P_r'(t),
\qquad P_s'(t')=-P_r'(t).}
\tag{3.16}
$$



Substitution in (1.3) shows that the paired branches have identical
fourth-power status.  This is the independent reflection check on the sign
of the affine $u$-term.

## 4. Level-two singular matching theorem — PROVED

Let



$$
L=a+\varepsilon b\pi>0,\qquad \gcd(a,b)=1,
\qquad \varepsilon=(-1)^N,
$$



and let $p_N,q_N$ be the primitive beta pair.  Put



$$
\Delta=\gcd(b,q_N),\qquad
P^*={b\over\Delta}p_N-\varepsilon{q_N\over\Delta}a,
\qquad g=\gcd(P^*,\Delta).
\tag{4.1}
$$



Assume (1.1), write



$$
N=r+xp,\qquad x\equiv t\pmod p,
\tag{4.2}
$$



and assume $v_p(b)=2$.  Put



$$
\beta={b\over p^2}\pmod p,
\qquad \sigma=(-1)^r.
\tag{4.3}
$$



The numerator period is $p_N\equiv p_r\pmod p$, while (3.5) gives



$$
{q_N\over p^2}\equiv(-1)^xP_r(t)\pmod p.
\tag{4.4}
$$



Multiplying $P^*$ by the $p$-unit $\Delta/p^2$ shows that its first
normalized matching digit is



$$
\boxed{
p\mid g
\quad\Longleftrightarrow\quad
M_p(t):=\beta p_r-\sigma aP_r(t)=0\pmod p.}
\tag{4.5}
$$



Both $a$ and $p_r$ are $p$-units.  Therefore every root of
$M_p$ has $P_r(t)\ne0$, and hence automatically



$$
v_p(q_N)=v_p(b)=2.
\tag{4.6}
$$



There are two exact alternatives.

1. If $M_p\ne0$, it has at most three roots $t\pmod p$.  Each root
   gives one index class modulo $p^2$; after imposing parity it gives one
   class modulo $2p^2$.  On that class,
   $p^3\mid\Delta g$.
2. If $M_p=0$, then $P_r$ is the nonzero constant
   $\sigma\beta p_r/a$.  Every first digit matches with exact denominator
   valuation two.  Only the root class modulo $p$ remains; parity changes
   it to one class modulo $2p$, and again $p^3\mid\Delta g$.

For distinct simultaneous primes, partition them into the identity set
$I$ and the nonidentity set $J$, and write



$$
R_I=\prod_{p\in I}p,\qquad R_J=\prod_{p\in J}p.
$$



The Chinese remainder theorem gives at most



$$
\boxed{3^{|J|}\text{ parity-compatible classes modulo }
2R_IR_J^2,}
\tag{4.7}
$$



and every such class satisfies



$$
\boxed{(R_IR_J)^3\mid\Delta g.}
\tag{4.8}
$$



The factor two in (4.7) is the exact parity cost.  It has zero normalized
logarithmic rate, but it cannot be omitted from the finite congruence class.

There is a complementary exact law at valuation three.  Assume
$v_p(b)=3$, choose a first digit satisfying $P_r(t)=0$, and put



$$
\beta_3={b\over p^3}\pmod p.
$$



For $N=r+tp+up^2$, equation (1.3) gives



$$
\boxed{
p\mid g
\quad\Longleftrightarrow\quad
M_{p,3}(t,u):=
\beta_3p_r-\sigma a\{\kappa_t+uP_r'(t)\}=0\pmod p.}
\tag{4.9}
$$



Again every matching solution has exact equal valuation three, because the
braced expression in (4.9) is then the nonzero unit
$\sigma\beta_3p_r/a$.  In particular:

- if $P_r'(t)\ne0$, exactly one $u$ matches, and it is different from
  the unique $u$ that raises $q_N$ to $p^4$;
- if $P_r'(t)=0$ and $\kappa_t\ne0$, matching is all or none in $u$;
- if $P_r'(t)=\kappa_t=0$, every child has denominator valuation at
  least four, so equal valuation with $p^3\parallel b$ fails.

When $P_r\ne0$ and all its relevant roots are simple, there are at most
three parity-compatible matched classes modulo $2p^3$, and each has



$$
\boxed{p^4\mid\Delta g.}
\tag{4.10}
$$



For simultaneous distinct primes this generic branch gives at most
$3^{\omega(R)}$ classes modulo $2R^3$, with
$R^4\mid\Delta g$ and $R^3\mid b,q_N$.  A multiple-root all-or-none
case can compress the modulus from $p^3$ to $p^2$, but its existence is
an additional unproved arithmetic condition.

## 5. Gain, modulus cost, and product ceiling — PROVED

Let $R$ be a product of distinct primes satisfying the exact level-two
hypotheses at one index.  Necessarily



$$
\boxed{R^2\mid b,\qquad R^2\mid q_N.}
\tag{5.1}
$$



Consequently,



$$
\boxed{
3\log R\le {3\over2}\min\{\log|b|,\log q_N\}.}
\tag{5.2}
$$



Equation (5.2) is the product ceiling for the rigorously obtained first
matching digit $R^3\mid\Delta g$.  Even if the second matching digit were
granted for free, the universal capacity envelope gives only



$$
R^4\mid\Delta g\mid\gcd(b,q_N)^2,
\qquad
4\log R\le2\min\{\log|b|,\log q_N\}.
\tag{5.3}
$$



For the rigorously classified valuation-three branch of (4.9)--(4.10),
the stronger common-power hypothesis gives a different ceiling:



$$
\boxed{
R^3\mid b,q_N,\qquad R^4\mid\Delta g,
\qquad
4\log R\le {4\over3}\min\{\log|b|,\log q_N\}.}
\tag{5.4}
$$



The local gain/cost ledger is:



$$
\begin{array}{c|c|c|c}
\text{booked factor}&\text{log gain per }p&\text{index modulus per }p
&\text{status}\\ \hline
p^2\mid\Delta&2\log p&p\ \text{(then parity }2p)&\text{conditional proved}\\
p^3\mid\Delta g&3\log p&p^2\ \text{with at most 3 classes}
&\text{conditional proved}\\
p^3\mid\Delta g\ (M_p=0)&3\log p&p\ \text{(then parity }2p)
&\text{conditional exceptional}\\
p^4\mid\Delta g\ (v_p(b)=3)&4\log p&p^3\ \text{with at most 3 classes}
&\text{conditional proved}\\
p^4\mid\Delta g\ (v_p(b)=2)&4\log p&\text{not classified here}
&\text{full-}g\text{ ceiling only}
\end{array}
\tag{5.5}
$$



Thus the all-lift orbit gives real modulus compression if it exists.  It
does not, however, manufacture a small representative of an exponentially
large moving CRT class.

At the balanced beta scale, use the frozen constants



$$
{\log q_N\over6m}\longrightarrow
\theta=1.1685311871794864979\ldots,
$$





$$
T_1=1.0196329836694317939\ldots
\tag{5.6}
$$



for the remaining rate after the rank-one divisor.  If one source alone
were to fill $T_1$, the necessary capacities would be



$$
\begin{array}{c|c|c}
\text{factor and common support}&\log R/(6m)&
\text{required fraction of }\log q_N\\ \hline
R^2,\ R^2\mid q_N&T_1/2=0.509816491834715897\ldots
&T_1/\theta=0.872576611438626562\ldots\\
R^3,\ R^2\mid q_N&T_1/3=0.339877661223143931\ldots
&2T_1/(3\theta)=0.581717740959084374\ldots\\
R^4,\ R^3\mid q_N&T_1/4=0.254908245917357948\ldots
&3T_1/(4\theta)=0.654432458578969921\ldots\\
R^4,\ R^2\mid q_N\ \text{(full-}g\text{ ceiling)}
&T_1/4=0.254908245917357948\ldots
&T_1/(2\theta)=0.436288305719313281\ldots
\end{array}
\tag{5.7}
$$



These are necessary capacity fractions, not existence statements.

There is also a scoped support ceiling.  If all participating primes satisfy
$p\le\alpha m$, the prime number theorem gives
$\log R\le\alpha m+o(m)$.  Therefore the optimistic rates of
$R^2,R^3,R^4$, per $6m$, are at most



$$
{\alpha\over3},\qquad {\alpha\over2},\qquad {2\alpha\over3},
\tag{5.8}
$$



respectively.  Closing $T_1$ would require at least



$$
\alpha\ge
3.05889895100829538\ldots,
\quad
2.03926596733886359\ldots,
\quad
1.52944947550414769\ldots
\tag{5.9}
$$



in the three rows.  Equation (5.9) grants that every prime below the cutoff
is all-lift, occurs squared in the actual coefficient, and passes matching;
it is deliberately an optimistic ceiling.

For comparison with the narrow gap left after the optimistic $3m$
first-level support ceiling, put



$$
G=T_1-1=0.01963298366943179388\ldots.
\tag{5.10}
$$



Filling only this gap would require



$$
\begin{array}{c|c|c}
\text{factor}&\log R/(6m)&\text{equivalent lower bound on }\log R\\ \hline
R^2&G/2=0.00981649183471589694\ldots&3Gm=0.0588989510082953816\ldots m\\
R^3&G/3=0.00654432788981059796\ldots&2Gm=0.0392659673388635878\ldots m\\
R^4&G/4=0.00490824591735794847\ldots&{3Gm\over2}=0.0294494755041476908\ldots m
\end{array}
\tag{5.11}
$$



The best denominator-height ceilings are $\theta$ for $R^2$,
$3\theta/2=1.75279678076922975\ldots$ for the level-two $R^3$, and
$4\theta/3=1.55804158290598200\ldots$ for the proved level-three
$R^4$.  Every one is far above $G$.  Therefore the product ceilings
do **not** prove a zero-gain theorem for the residual $0.01963298\ldots$
gap; they leave ample formal capacity.  The obstruction is existence,
coefficient support, and synchronization, not raw height capacity.

The conclusion is sharp in scope: local all-lift matching has a formally
positive gain-to-modulus ratio, so the present bookkeeping does not rule it
out.  But (5.1), the moving CRT constraint, and the complete absence of an
actual-seed example mean that no positive rate can presently be booked.

## 6. Actual seed versus modified seeds

The anti-periods, the degree-five Newton congruence, and the numerator
period used above are arithmetic identities for the fixed seed
$(q_0,q_1)=(1,1)$.  They are not identities for an arbitrary solution of
the same recurrence.

The modified-seed construction in Item 165 proves that the noncentral
transfer/discriminant condition can occur for another initial pair.  Its
explicit $p=107$ example has $\lambda=1$, so it is dead rather than
all-lift.  More importantly, changing that example's local value to a
multiple of $p^2$ would not authorize (2.2)--(2.4).  No modified-seed row
is used as evidence for (1.2) or (1.3).

The certificate's formal polynomial fixtures test only the algebraic
implications of (3.5)--(3.7).  They are labelled as fixtures, not recurrence
or actual-seed examples.

## 7. Exact replay and finite diagnostic

The companion replay performs three separate checks.

1. On every actual-seed root fibre for primes $7\le p\le101$, it verifies
   the degree-five Newton congruence modulo $p^4$ and the valuations of
   $D_4,D_5,D_6$.  This covers 19 root fibres, 323 Newton evaluations,
   and 57 divided-difference checks.
2. Formal fixtures verify (3.7)--(3.9), including simple, multiple-dead,
   multiple-full, and identically-zero cubic cases.  These are algebra
   replays, not Bessel examples.
3. The finite actual-seed scan through $p\le20000$ reconstructs 2,267
   roots for 2,261 odd primes.  Its only singular root is the known central
   dead row $(p,r,\lambda)=(79,39,12)$.  It finds no noncentral singular
   root and no all-lift root.  This third statement is **EXPERIMENTAL
   FINITE**.  The archived scan through $p\le200000$ is likewise finite.
   The $p=79$ row is not an instance of the theorem: it is central, and
   its nonzero $\lambda=12$ makes it dead already at $p^2$.

The independent derivation

```text
sources/item169_child_second_level_transfer.md
```

has SHA-256

```text
9df44afddeacddc2651ce3d191667078190a526d5f67b9a3ce47ca2cfc3cd8d3
```

and separately checks the sign in (1.3), the continuant formula (3.13),
the reflection coupling (3.16), and both matching normalizations.  It also
directly audits the modified $p=107$ comparison and obtains
$u_{157}\equiv92\pmod {107}$, confirming that this modified-seed row is
not an index all-lift orbit.

Run from the archive root after integration:

```text
python -m py_compile scripts/item169_deeper_all_lift_certificate.py
python scripts/item169_deeper_all_lift_certificate.py \
  --prime-limit 20000 \
  --output results/item169_deeper_all_lift_certificate.json
```

A byte-identical replay uses the same prime limit and compares the resulting
JSON with the archived certificate.

## 8. Status ledger

### PROVED

- The cubic second-level law (1.2), with every residue class modulo $p^2$
  classified as dead or all-lift.
- The fourth-digit affine law (1.3), the derivative/slope identity (3.10),
  and the three cases in (3.9).
- The degree-three and degree-five survivor bounds, including reflection
  coupling at the cube threshold.
- The first normalized level-two matching equation (4.5), its at-most-three
  versus identity alternative, the CRT class count (4.7), and the gain
  (4.8).
- The exact valuation-three matching equation (4.9), including the generic
  gain/modulus pair $p^4$ versus $2p^3$ in (4.10).
- The product ceilings (5.1)--(5.4), the support ceilings (5.8)--(5.9),
  and the explicit residual-gap comparison (5.10)--(5.11).

### EXPERIMENTAL FINITE

- No noncentral singular or all-lift actual-seed root through $p=20000$
  in the new replay.
- The archived absence of all-lift roots through $p=200000$.

### OPEN

- Whether the actual Bessel seed has any noncentral singular prime at all.
- Whether any actual-seed singular root satisfies $\lambda=0$.
- A positive-logarithmic-mass family of such primes occurring squared in
  the actual $b_m$ at one saddle-compatible index.
- Simultaneous satisfaction of the cubic matching equation at positive
  rate, and exceptionally small representatives of the resulting moving
  CRT classes.
- The second normalized matching digit $p^2\mid g$ at exact common
  valuation two; the corresponding row of (5.3) is only an optimistic
  product ceiling.

Nothing here proves irrationality, rationality, or transcendence of
$e+\pi$.
