> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the actual type-I endpoint bridge

Date: 2026-09-13. Reviewer: audit_results.

Target: raw_actual_endpoint_integral_dual_numerators.md, Sections 1–8,
including the added partial-sum functional (9a) and archive
determinant identities (11a).
The exact primitive dual normalization, endpoint-scalar restriction
and saturated Cauchy-block theorem were checked against their
previously reviewed source notes.

**Verdict: FULL PASS.** The global integral numerator construction
proves $q_n\mid|Z_n|$ for the actual canonical endpoint. The
primitive cofactor residue and the ensuing exact saturated-family
denominator valuations are also correct. The exceptional cancellation
at $n=p=7$ is proved without solving that degree.

One wording clarification has been applied by the author: the
linear-in-$n$ contribution statement concerns the explicit families
with known $e=0$ or $1$; the formula with unknown $e_{n,p}$
does not bound its growth. No substantive repair or new degree/prime
scan was needed.

## 1. The actual denominator and polynomial normalization

The archive's $q_n$ is the positive reduced denominator of
$A(1)/B(1)$ under $C(1)=4B(1)$. Since $B(1)\ne0$ in
every relevant degree, normalizing $B(1)=1$ gives precisely
the canonical value used in the target.

The integer primitive cofactor vector $w_k$ and the factors
$k!/n!$ in $\widehat Q_n$ agree exactly with the original
dual note. Neither an unscaled Taylor cofactor nor an arbitrary
scalar multiple has been substituted.

For a coefficient of degree $t\le2n$ in either numerator, set
$j=3n-t$. Then $j\ge n$, and the exponential term is


$$
\frac{k!}{n!(k-j)!}w_k
=\frac{j!}{n!}\binom kjw_k.
$$


Every factor on the right is integral. The arctangent term occurs
only when $k-j>0$ is odd, and it equals the same integer times
$(k-j-1)!(-1)^{(k-j-1)/2}$. The case $k=j$ is absent in that
sum, so no negative factorial is used.

Thus both entire truncated numerator polynomials are integral.
The lower bound $j\ge n$ is the essential reason the factor
$n!$ does not remain in their denominators.

## 2. Cross-product signs and the global endpoint divisor

The reviewed cross product has first coordinate
$S_0=\widehat Q_n/Z_n$ and degree at most $2n$.
Its other two coordinates agree with $S_0e^z$ and
$S_0\arctan z$ through degree $3n$.
Since they are polynomials of degree at most $2n$, their low
Taylor truncations determine them exactly. Hence (8) follows
with $\widehat P_e,\widehat P_a$, not merely up to a scalar.

At the two chosen endpoint pairs, the second cross coordinate is
$-A_E(1)$ and the third is $-A_F(1)$.
The selected triple is $T_E+4T_F$, so its endpoint is


$$
A_n(1)=-\frac{\widehat P_{e,n}(1)+4\widehat P_{a,n}(1)}{Z_n}.
$$


The numerator is integral, $Z_n\ne0$, and elementary rational
reduction gives exactly


$$
q_n=\frac{|Z_n|}{\gcd(|Z_n|,|N_n|)}.
$$


This remains true if $N_n=0$. The same linearity proves (11)
for any prescribed integer endpoint pair.

The added formula (9a) also checks. For fixed $k$, the permitted
Taylor index is $0\le s\le k-n$, and
$k!/n!=\binom kn(k-n)!$. Interchanging the two finite sums
gives exactly (9a); both factorial partial sums are integers.
Replacing their cutoff $k-n$ by $k$ changes the exponential
sum by


$$
\frac1{n!}\sum_{j=0}^{n-1}\sum_k(k)_jw_k=0,
$$


and the arctangent sum by


$$
\frac1{n!}\sum_{j=0}^{n-1}\sum_k k!\tau_{k-j}w_k=0.
$$


These are precisely the original columns of $X_n$, so the
alternative telescoping form has the same exact normalization.

For $p>3n$, all factorial multipliers in $\widehat Q_n$
are $p$-units. Primitivity of $w$ then makes its coefficient
content a $p$-unit, giving the stated local comparison with
$d_n^{II}$. Globally $q_n\mid d_n^{II}$ need not hold:
the target correctly claims only $q_n\mid|Z_n|$.

## 3. Exact archive determinant and gcd factors

The archive appends the endpoint row $C(1)-4B(1)$ followed
by $B(1)$. Replacing the first of those rows by $C(1)$
does not change the determinant, and reversing their order gives
$\Delta_B=-\mathcal E_n$. Therefore


$$
\Delta_B=(-1)^{n+1}F_nZ_n.
$$


The other appended functional is $n!A(1)$, so the ratio
$\Delta_A/\Delta_B$ is $n!A(1)/B(1)$.
Using the proved endpoint formula gives


$$
\Delta_A=(-1)^n n!F_nN_n.
$$


Taking positive gcds proves


$$
\gcd(\Delta_A,n!\Delta_B)
=n!F_n\gcd(N_n,Z_n).
$$


These are exact global identities; the factor $n!$ in the
appended $A$-row and the sign convention are both retained.

## 4. Primitive cofactor residue on the saturated family

For $r<n$, the ratio


$$
c_r=\frac{(2n)!}{(n+r)!}
$$


contains the factor $2n$, so it is divisible by $p$.
The final weight is $c_n=1$.
The saturated Cauchy theorem makes both $\delta_n$ and $h_n$
units. Thus the exact cofactor transport reduces to


$$
w_{2n+s}\equiv
(-1)^{n+s}\binom ns\,\eta_n,\qquad
\eta_n=\delta_n/h_n,
$$


with earlier coefficients zero modulo $p$.
This proves


$$
W_n(z)\equiv\eta_n z^{2n}(z-1)^n\pmod p.
$$


The factor $h_n$ is essential to the displayed primitive
normalization, and the target explicitly retains it.

Because $p\mid n$, the polynomial on the right has only
exponents divisible by $p$. This establishes both facts
needed below: surviving $k$ satisfy $k\ge2n$ and $p\mid k$.

## 5. Endpoint residues and the $n=p$ exception

In either numerator endpoint sum, $j!/n!$ is divisible by $p$
if $j\ge n+p$, since its product contains $n+p$.
For $j=n+a$, $1\le a<p$, Lucas's lowest-digit formula
annihilates $\binom{k}{j}$ whenever the coefficient $w_k$
survives modulo $p$: the lowest digit of $k$ is zero and
that of $j$ is $a$. All additional factors in the arctangent
sum are integers, so they cannot undo this vanishing.

The only remaining index is $j=n$. For the exponential endpoint,


$$
\sum_k\binom knw_k=[y^n]W_n(1+y)
\equiv[y^n]\eta_n(1+y)^{2n}y^n=\eta_n.
$$


This is a coefficient identity over $\mathbb Z$, valid in
characteristic $p$ without division by $n!$.

For the arctangent endpoint and $n>p$, every surviving
$k-n\ge n>p$, so $(k-n-1)!$ contains $p$.
Thus that endpoint is zero modulo $p$, and
$N_n\equiv\eta_n$ is a unit. It follows that none of the
$p$-part of $Z_n$ cancels in the actual endpoint rational.

When $n=p$, only $k=2p$ can remain: higher differences have
a factorial divisible by $p$, and earlier coefficients vanish.
Here $w_{2p}\equiv-\eta_p$, $\binom{2p}{p}\equiv2$,
and $(p-1)!\equiv-1$. Their two minus signs cancel; the
arctangent coefficient contributes
$\chi_p=(-1)^{(p-1)/2}$. Hence


$$
\widehat P_{a,p}(1)\equiv2\chi_p\eta_p,\qquad
N_p\equiv(1+8\chi_p)\eta_p.
$$


For $p>3$, this coefficient is a unit except at $p=7$:
when $\chi_p=1$, it is $9$; when $\chi_p=-1$, it is
$-7$. The excluded prime $3$ is not saturated for $m=1$.

## 6. Exact valuations and archived controls

For saturated $n>p$, the unit numerator and the reviewed
endpoint-scalar identity give exactly


$$
v_p(q_n)=v_p(Z_n)
=\frac{n-m}{p-1}+v_p(d_n^{II}).
$$


This formula does not require knowing the last valuation.
The previously proved cases $e=0$ and $e=1$ therefore
transfer to the actual type-I endpoint with no new loss.

For $n=p$, $v_p(Z_p)=1$. Thus the unit numerator gives
$v_p(q_p)=1$ except at $p=7$, where $v_7(N_7)\ge1$
forces $v_7(q_7)=0$. No higher numerator precision or
degree-seven construction is needed.

The displayed $n=1,2$ polynomial controls agree with the saved
primitive vectors. In particular at $n=2$,


$$
\widehat P_e(1)=44641,\quad
\widehat P_a(1)=12852,\quad N_2=96049.
$$


This numerator is coprime to $Z_2=16432$, giving
$q_2=16432$, as already recorded in
raw_rational_transfer_checks.json.
The simultaneous coefficient denominator is $4108$.
This confirms both sharpness of $q_n\mid|Z_n|$ at this degree
and the failure of a global $q_n\mid d_n^{II}$ claim.
It is a normalization check using existing data, not an
infinite-family argument.

## 7. What has now been transferred, and what remains

The exact selected endpoint denominator is now controlled by the
two explicit integers $N_n,Z_n$. Whole coefficient recovery
of the type-I triple is unnecessary for this endpoint identity.
On the saturated families with $n>p$, its local numerator
coprimality is proved.

For other primes, the remaining cancellation is still
$\gcd(N_n,Z_n)$. No statement here bounds all those prime
contributions, reconstructs denominators of every type-I
coefficient, proves primitive shrinking, or settles the main
rationality problem. The final scope of the target correctly
preserves these distinctions.
