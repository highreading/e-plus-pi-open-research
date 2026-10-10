> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A primitive dual quadratic and large-prime endpoint separation

Date: 2026-09-13. Original bounded continuation by audit_sources.
Independent review passed: raw_dual_quadratic_independent_review.md.

The actual normalized endpoint gcd is


$$
G_{4,n}=\gcd(|Z_n|,|N_n|),\qquad
N_n=P_n(1)+4T_n(1),
$$


where throughout this note


$$
Q_n=\widehat Q_n,\quad
P_n=\widehat P_{e,n},\quad
T_n=\widehat P_{a,n}
$$


are the actual **simultaneous** integer polynomials of degree at most $2n$.
They are not the selected type-I cubic or the raw monic Legendre polynomials.

This note constructs a different quadratic Wronskian and proves


$$
\boxed{
\gcd\bigl(|Q_n(1)|,|P_n(1)|,|T_n(1)|\bigr)_{>2n}=1.
}
\tag{1}
$$


Thus a large prime dividing the remaining actual gcd $G_{4,n}$ is never explained by a common factor of all three simultaneous endpoint values. Both $P_n(1)$ and $T_n(1)$ are units at that prime. The resulting single endpoint-ratio condition is exact at every prime-power depth, but its size at the fixed coefficient 4 remains unresolved.

## 1. Audit of the earlier gates and the available finite records

The inspected dependencies are raw_actual_endpoint_integral_dual_numerators.md, raw_extremal_dual_polynomial_and_content_identity.md, raw_large_prime_endpoint_gcd_carrier.md, raw_large_prime_endpoint_local_classification.md, and raw_large_prime_nullity_and_smith.md. The earlier carrier and its full sufficient classification concern the **primitive integral selected type-I triple** and its cubic Wronskian.

Their endpoint cancellation valuation is
$h_p=\min(v_p(A_{\rm prim}(1)),v_p(B_{\rm prim}(1)))$.
It is not the same quantity as
$g_p=v_p(G_{4,n})$. If $\delta_n$ is the maximal-minor content of the matched high matrix $J_n$ and $F_n$ is the extremal content, the exact previously proved scales and the new endpoint identity give


$$
\boxed{g_p=v_p(\delta_n)-v_p(F_n)+h_p,\qquad p>3n.}
\tag{2}
$$


Therefore simply substituting the new endpoint gcd into the old four-integer cubic gate would omit a cofactor-content contribution.

The original results/raw_arctan_endpoint_arithmetic_n30.json stores endpoint-gcd digit counts, valuations at 2, and hashes, rather than exact raw gcd integers. Those fields do not certify a large-prime counterexample for $G_{4,n}$. The already archived exact degrees $n=1,2$ have $G_{4,n}=1$. No absence of large-prime cancellation is inferred at other degrees, and no new degree or prime scan is run here.

## 2. A universal polynomial Wronskian of the simultaneous triple

Let $D=1+z^2$. For any polynomials $Q,P,T$, define the integer differential polynomial


$$
\mathcal W(Q,P,T)=
\det\begin{pmatrix}
Q&P&D^2T\\
Q'&P'-P&D^2T'-DQ\\
Q''&P''-2P'+P&D^2T''-2DQ'+D'Q
\end{pmatrix}.
\tag{3}
$$


Over characteristic zero this is exactly


$$
\mathcal W(Q,P,T)
=D^2e^z W\bigl(Q,Pe^{-z},T-Q\arctan z\bigr).
\tag{4}
$$


To verify (4), multiply the exponential column by $e^z$ after differentiation, and add $\arctan z$ times the first column to the third. The three entries left in that column are
$T,\ T'-Q/D,\ T''-2Q'/D+QD'/D^2$.
Multiplication of that entire column by $D^2$ gives (3).
Equation (3), not an unrestricted exponential series, defines the object over a finite field.

If all three input degrees are at most $m$, then


$$
\boxed{\deg\mathcal W(Q,P,T)\le3m+2.}
\tag{5}
$$


Here are explicit cancellations proving the bound. The portion in which the third column consists of $D^2(T,T',T'')^T$, divided by $D^2$, is


$$
W(Q,P,T)-P(QT''-Q''T)-(P-2P')(QT'-Q'T).
$$


The ordinary Wronskian has degree at most $3m-3$;
$QT'-Q'T$ has degree at most $2m-2$, because the top degree cancels when both inputs have degree $m$; and $QT''-Q''T$ has degree at most $2m-2$.
The displayed expression has degree at most $3m-2$.
The two remaining contributions are


$$
\begin{aligned}
&DQ\{Q(P''-2P'+P)-Q''P\},\\
&(-2DQ'+D'Q)\{Q(P'-P)-Q'P\}.
\end{aligned}
$$


Their degrees are at most $3m+2$ and $3m+1$, respectively. This proves (5); zero polynomials cause no exception.

For any polynomial $f$, the universal common-factor identity is


$$
\boxed{\mathcal W(fQ,fP,fT)=f^3\mathcal W(Q,P,T).}
\tag{6}
$$


It follows from the three-function Wronskian product rule in (4), or directly from triangular row operations in (3). Both sides are polynomials with integer coefficients in the coefficients of $f,Q,P,T$, so the identity is valid in every characteristic.

## 3. The actual origin factor leaves only a quadratic

Put $M=3n+1$. The reviewed simultaneous equations say


$$
Q_ne^z-P_n=O(z^M),\qquad
Q_n\arctan z-T_n=O(z^M).
$$


Consequently, after subtracting the first column from the second in (4), its last two function columns have order at least $M$.

For any analytic or formal characteristic-zero functions $q,g,h$, with $g,h=O(z^M)$, one has


$$
W(q,g,h)=O(z^{2M-2}).
\tag{7}
$$


Indeed the terms containing $q'$ or $q''$ have that order or higher. The only potential lower-order term is $q(g'h''-g''h')$, of candidate order $2M-3$. Its leading coefficients cancel: both are $M^2(M-1)[z^M]g\,[z^M]h$. This remains valid if either leading coefficient vanishes.

Equations (4) and (7), with $m=2n$ in (5), prove the exact integer identity


$$
\boxed{
\mathcal W(Q_n,P_n,T_n)=z^{6n}\mathcal K_n(z),\qquad
\mathcal K_n\in\mathbb Z[z],\quad\deg\mathcal K_n\le2.
}
\tag{8}
$$


Division by a monomial merely removes zero coefficients and introduces no denominator. The proof of origin divisibility is in characteristic zero for the actual rationally defined family. The resulting integer identity is then reduced modulo primes; no undefined characteristic-$p$ exponential coefficient is used.

## 4. A nonvanishing lemma over every odd characteristic

Let $K$ be any field of characteristic different from 2, with $Q,P\ne0$. Put in $K(z)$


$$
a=P/Q,\qquad b=T/Q,\qquad L=a'-a,\qquad H=b'-1/D.
$$


A direct rational simplification of (3) gives


$$
\boxed{\mathcal W(Q,P,T)
=D^2Q^3\{LH'-L'H+LH\}.}
\tag{9}
$$


This can first be checked from (4) and the Wronskian of
$1,ae^{-z},b-\arctan z$; it is a rational identity with integer coefficients, so it remains valid over every field in the stated range.

The rational function $L$ is nonzero: otherwise a nonzero rational $a$ would have $a'/a=1$, impossible since a rational logarithmic derivative is $O(1/z)$ at infinity. The function $H$ is nonzero as well. Over an algebraic closure, $1/D$ has nonzero simple-pole residues at $i$ and $-i$, whereas a derivative of a rational function has zero residue at every finite point. These assertions remain true in positive characteristic.

If the brace in (9) were zero, then


$$
\frac{(H/L)'}{H/L}=-1,
$$


again impossible for a nonzero rational function. We have proved


$$
\boxed{Q,P\ne0\quad\Longrightarrow\quad
\mathcal W(Q,P,T)\ne0.}
\tag{10}
$$


No assumption that $T$ is nonzero is needed.

For the actual integer family, the globally reviewed cofactor-content identity in raw_endpoint_scalar_cauchy_restriction.md (8) gives


$$
c_n^Q=R_n\Theta_n/h_n,\qquad h_n/\Theta_n\mid R_n,
\qquad R_n=(2n)!/n!.
$$


Thus $c_n^Q\mid R_n$, so $Q_n$ is $p$-primitive for every $p>2n$. This is stronger than the earlier direct factorial-weight argument, which by itself only gives the cutoff $3n$. Moreover $P_n$ cannot reduce to zero: the low relation


$$
P_n\equiv Q_n\sum_{j=0}^{2n}z^j/j!\pmod{z^{2n+1}}
$$


would then force $Q_n=0$, since the exponential Taylor polynomial has unit constant coefficient. All denominators here are units at $p>2n$.
Using (8) and (10), we obtain


$$
\boxed{\mathcal K_n\ \text{is \(p\)-primitive for every }p>2n.}
\tag{11}
$$


In particular the quadratic is nonzero over $\mathbb Q$. Its content has only primes at most $2n$; its actual integral scale is retained.

## 5. No common nonzero root of the simultaneous triple

**Theorem.** For any $p>2n$, the reductions of $Q_n,P_n,T_n$ have no common root in $\overline{\mathbb F}_p^\times$.

Suppose they vanished at $a\ne0$. Each would be divisible by $z-a$. Identity (6) would make $(z-a)^3$ divide $\mathcal W(Q_n,P_n,T_n)$. Since $a\ne0$, equation (8) would make $(z-a)^3$ divide $\mathcal K_n$. This contradicts both its degree at most 2 and its nonzero reduction from (11). This proves the theorem.

Taking $a=1$ gives (1). It is stronger than merely bounding the common endpoint valuation by $v_p(F_n)$. It also covers $a=\pm i$, when defined over the algebraic closure: the polynomial identity (6) is valid at those points despite the rational denominators used for the explanatory formula (4).

There is a global prime-power strengthening which retains small primes:


$$
\boxed{
\gcd(|Z_n|,|P_n(1)|,|T_n(1)|)
\mid \operatorname{content}(\mathcal K_n).
}
\tag{11a}
$$


To prove it, reduce modulo any positive integer $d$ dividing the three endpoint values. Monic division shows that all three input polynomials are divisible by $z-1$ over $(\mathbb Z/d\mathbb Z)[z]$. The universal identity (6) therefore makes their Wronskian divisible by $(z-1)^3$. In the quotient by $(z-1)^3$, $z^{6n}$ is a unit, with an integer-coefficient truncated binomial inverse. Hence (8) makes $\mathcal K_n$ divisible by $(z-1)^3$ modulo $d$. A polynomial of degree at most 2 with that property is zero, so $d$ divides each coefficient of $\mathcal K_n$. This argument uses neither a field nor division by $2$ or $3$, and thus preserves every prime-power exponent in (11a). Equation (11) then proves the large-prime exclusion.

A second immediate consequence is that the degree-$2n$ coefficient vector of the triple is $p$-primitive for $p>2n$. If all three coefficients vanished, all input degrees after reduction would be at most $2n-1$, and (5) would give degree at most $6n-1$. But (8) and (11) give a nonzero polynomial divisible by $z^{6n}$, a contradiction. Neither consequence proves that $Q_n$ individually has full degree or has a nonzero constant coefficient at every prime.

## 6. Exact separation of the endpoint combinations

For any integer $\lambda$, define


$$
G_{\lambda,n}=\gcd\bigl(|Z_n|,
 |P_n(1)+\lambda T_n(1)|\bigr).
\tag{12}
$$


The actual $e+\pi$ endpoint uses $\lambda=4$. Fix $p>2n$. If $p\mid G_{\lambda,n}$, then $T_n(1)$ is a $p$-adic unit: otherwise both $P_n(1)$ and $Q_n(1)=Z_n$ would also vanish modulo $p$, contradicting (1). If $\lambda$ is a $p$-unit, then $P_n(1)$ is a unit as well.

Thus at any actual cancellation prime above $2n$,


$$
\boxed{
v_p(G_{4,n})
=\min\left\{v_p(Z_n),
 v_p\!\left(4+\frac{P_n(1)}{T_n(1)}\right)\right\},
\quad
P_n(1),T_n(1)\in\mathbb Z_p^\times.
}
\tag{13}
$$


The displayed equality is asserted where $p\mid G_{4,n}$, so division by $T_n(1)$ is justified by the theorem, not assumed.

For distinct integers $\lambda,\mu$, every such prime satisfies


$$
\boxed{
\min\{v_p(G_{\lambda,n}),v_p(G_{\mu,n})\}
\le v_p(\lambda-\mu).
}
\tag{14}
$$


If the minimum is zero there is nothing to prove. Otherwise $T_n(1)$ is a unit, and subtracting the two endpoint combinations gives
$(\lambda-\mu)T_n(1)$; its valuation bounds the common gcd. In particular, for any set of integer parameters lying in an interval of length at most $2n$, their $G_{\lambda,n,>2n}$ are pairwise coprime, and


$$
\boxed{
\prod_{\lambda\in S}(G_{\lambda,n})_{>2n}
\mid (Z_n)_{>2n}
\qquad
(\max S-\min S\le2n).
}
\tag{15}
$$


At a fixed prime at most one factor is nontrivial, and its exponent is at most $v_p(Z_n)$, proving the full prime-power assertion.

At all primes, (11a) gives the global version


$$
\boxed{
\gcd(G_{\lambda,n},G_{\mu,n})
\mid |\lambda-\mu|\,\operatorname{content}(\mathcal K_n).
}
\tag{15a}
$$


Indeed, writing $g$ for the valuation of the left side and $a=v_p(\lambda-\mu)$, subtraction forces $v_p(T_n(1))\ge g-a$. Since the parameters are integers, $v_p(P_n(1))\ge g-a$ as well, while $v_p(Z_n)\ge g$. Thus $g-a$ is at most the triple endpoint content valuation, which is at most $v_p(\operatorname{content}\mathcal K_n)$. This also covers $g<a$.

For $2n+1$ consecutive parameters, (15) bounds the sum of their large-prime logarithmic cancellations by $\log |(Z_n)_{>2n}|$. This is a distribution statement over changing endpoint combinations. It cannot be used to bound the single fixed parameter 4. The actual values represented by other parameters are $e+\lambda\pi/4$, not the target $e+\pi$.

## 7. Exact controls using only the already saved degrees

Using the previously archived $Q_n,P_n,T_n$, without solving any new high system, formula (3) gives


$$
\begin{aligned}
\mathcal K_1(z)&=-20z^2+88z-44,\\
\mathcal K_2(z)&=-6623355200z^2+10006152832z+2216151616.
\end{aligned}
\tag{16}
$$


Their contents are respectively 4 and 64. The origin orders in (8) are exactly 6 and 12 in these controls. Both endpoint triple gcds in (1) equal 1 over the integers. These checks verify the chosen signs and scales; they are not the proof of (8), (11), or the all-index saturation theorem.

## 8. Remaining fixed-parameter obstruction

The normalized simultaneous triple is basepoint-free at every nonzero algebraic point modulo a prime above $2n$. Nevertheless, its image at the specific endpoint 1 can lie on the line


$$
Q_n(1)=0,\qquad P_n(1)+4T_n(1)=0
$$


modulo such a prime power, with $T_n(1)$ a unit. The primitive dual quadratic does not exclude this line: only a common zero of all three coordinates would force its impossible cube factor.

Therefore the exact missing arithmetic lemma is a height or congruence bound for the single unit ratio in (13), at those primes that divide $Z_n$. The pairwise separation theorem prevents the same large prime from contributing deeply at nearby distinct integer parameters, but it gives no bound for the parameter 4 alone. Endpoint data $(Z,P,T)=(a,-4+a,1)$ with arbitrary nonzero integer $a$ illustrate this limitation of the endpoint algebra: their triple gcd is 1 but $G_4=|a|$. These are not claimed actual HP data or counterexamples to an unproved actual theorem.

The new degree-2 object is smaller than the older primitive type-I cubic and proves a distinct all-index saturation theorem. Its coefficient size has not been bounded sharply, and no quantitative advantage for the actual fixed-parameter $G_{4,n}$ follows merely from that degree reduction. Establishing such an advantage requires a new relation between the actual unit ratio, the endpoint $Z_n$, and the differential or adjacent-index structure.
