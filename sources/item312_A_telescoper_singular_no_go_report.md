> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 312 — exact $A_s$ telescoper, singular-pivot localization, and a bounded-operator no-go

Date: 2026-08-31

## 1. Outcome and capacity

Retain Item 310's exact fixed-$j=1$ rational aggregate



$$
A_s=-[x^{2s+5}]
 \frac{(1+x)^{3s+1/2}N_s(1+x)}{(1+x^2)^{2s+1}},
 \qquad s\geq1.                                           \tag{1.1}
$$



This item proves the following all-$s$ recurrence:



$$
\boxed{\sum_{j=0}^{3}P_j(s)A_{s+j}=0\qquad(s\geq1),}     \tag{1.2}
$$



where every $P_j\in\mathbb Z[s]$ has degree seven and is displayed
explicitly in Section 3.  The proof is an exact rational telescoping
certificate, including all finite-support endpoint terms.  Thus the
previously guessed order-three, degree-seven operator is promoted from
discovery to **PROVED**.  No minimality beyond this explicit bound is
claimed.

The leading and trailing coefficients factor completely over
$\mathbb Q$.  On the actual fixed-$M$ indexing, every prime which
makes either pivot singular divides one of two explicit nonzero
degree-seven integers $R_0(M),R_3(M)$.  Consequently their total
logarithmic mass is $O(\log M)=o(M)$.  This is an exact
**singular-pivot localization theorem**.

It is not a localization theorem for the collision primes
$p_s\mid D_{s,\epsilon}$.  Away from the thin pivot set, (1.2) merely
transports a three-dimensional state modulo a changing prime; it does not
prevent one coordinate, or Item 308's quadratic norm container, from
vanishing.

Finally, the positive integral sequence



$$
C_s={7s\choose s}                 \tag{1.3}
$$



has an order-one recurrence whose two coefficients have degree seven, yet
retains tied-prime mass $M/38+o(M)$ on the actual fixed-$M$ indexing.
This is strictly an information-class no-go: order at most three,
coefficient degree at most seven, integrality, nonvanishing, and
exponential height alone cannot prove moving-prime $o(M)$.  It is not a
counterexample to the exact operator (1.2) or to the actual $A_s,B_s$, or
$D_{s,\epsilon}$ sequences.

Therefore



$$
\boxed{\text{new linear log rate}=0,\qquad
       \text{new fixed-}j=1\text{ capacity reduction}=0.} \tag{1.4}
$$



The fixed-$j=1$ ceiling remains $1/36$ per $6M$.

## 2. Exact finite hypergeometric representation

Item 310 writes $N_s(t)=N_0(t)+sN_1(t)$, with



$$
\begin{aligned}
N_0(t)&=4-\frac43t-\frac83t^2+\frac{16}3t^3-3t^4+t^5,\\
N_1(t)&=\frac{80}3t-\frac{224}3t^2+\frac{256}3t^3
                         -46t^4+10t^5.                   \tag{2.1}
\end{aligned}
$$



Put



$$
N_s(1+x)=\sum_{d=0}^{5}\mu_d(s)x^d.                     \tag{2.2}
$$



Direct expansion gives, from $d=0$ to $5$,



$$
\left(
\frac{4s+10}{3},\
\frac{7-2s}{3},\
\frac{16s+16}{3},\
\frac{4s+10}{3},\
4s+2,\
10s+1
\right).                                                  \tag{2.3}
$$



Expanding



$$
(1+x^2)^{-2s-1}
 =\sum_{m\geq0}(-1)^m{2s+m\choose m}x^{2m}               \tag{2.4}
$$



turns (1.1) into



$$
A_s=\sum_{m=0}^{s+2}T_{s,m},                             \tag{2.5}
$$



where



$$
T_{s,m}=-(-1)^m{2s+m\choose m}
 \sum_{d=0}^{5}\mu_d(s)
 {3s+\frac12\choose 2s+5-2m-d}.                           \tag{2.6}
$$



Let



$$
\alpha=3s+\frac12,\qquad k=2s+5-2m.                     \tag{2.7}
$$



The contiguous-binomial identity



$$
\frac{{\alpha\choose k-d}}{{\alpha\choose k}}
=\frac{k^{\underline d}}{(\alpha-k+1)^{\overline d}}      \tag{2.8}
$$



gives



$$
T_{s,m}=-(-1)^m{2s+m\choose m}{\alpha\choose k}R(s,m),  \tag{2.9}
$$



with



$$
R(s,m)=
\frac{4Q(s,m)}
{\prod_{\nu\in\{-7,-5,-3,-1,1\}}(4m+2s+\nu)},            \tag{2.10}
$$



and



$$
\begin{aligned}
Q(s,m)={}&1024m^5
+(10240s^2+7168s-4096)m^4\\
&+(-22528s^3-67584s^2-37376s+4352)m^3\\
&+(24576s^4+110336s^3+160128s^2+70464s+1056)m^2\\
&+(-13024s^5-78064s^4-167888s^3-155432s^2
                                  -53982s-3111)m\\
&+3328s^6+24960s^5+71552s^4+98496s^3
                                  +66704s^2+19896s+1840.
                                                               \tag{2.11}
\end{aligned}
$$



Every denominator in (2.10) is an odd nonzero integer when $s,m$ are
integers.  Since $k=1$ at $m=s+2$ and $k=-1$ at $m=s+3$, the
standard convention ${\alpha\choose r}=0$ for negative integral $r$
proves the exact support in (2.5).

## 3. The explicit order-three, degree-seven operator

The four coefficients in (1.2) are



$$
\begin{aligned}
P_0(s)={}&9(2s+1)(6s+5)(6s+7)(6s+11)(6s+13)\\
&\hspace{34mm}\cdot(660s^2+2920s+3039),                   \tag{3.1}\\
P_1(s)={}&24s(6s+11)(6s+13)\\
&\quad\cdot(1697520s^4+10905280s^3+24360488s^2
                              +22368528s+7001703),         \tag{3.2}\\
P_2(s)={}&768s(s+1)(2s+3)(6s+13)\\
&\quad\cdot(3960s^3+20820s^2+33034s+14047),               \tag{3.3}\\
P_3(s)={}&4096s(s+1)(s+2)(2s+3)(2s+5)\\
&\hspace{34mm}\cdot(660s^2+1600s+779).                    \tag{3.4}
\end{aligned}
$$



Each displayed product has total degree seven.  Section 4 supplies an
all-$s$ certificate, so these coefficients are not inferred from a
bounded recurrence fit.

## 4. Exact telescoping certificate and endpoint closure

Let $J(s,m)\in\mathbb Z[s,m]$ be the bidegree-$(18,11)$ polynomial
defined by the twelve exact coefficients, descending in $m$, in
work/item312_A_telescoper_data.json under the key
certificate_J_coefficients_descending_m.  That file also stores the
expanded certificate as an independent exact representation.  It is part
of this sealed package and has SHA-256
64cdd3c400c0472fef2e6b7949ccff2a15478ba7a96eb232ab05f2c547cd993c.

Define



$$
\begin{aligned}
C(s,m)=
-\frac{9m(6s+5)(6s+7)(6s+11)(6s+13)J(s,m)}
{2(s+1)(s+2)(s+3)Q(s,m)}\qquad\qquad\qquad\\
\cdot\frac1{
(-2m+2s+7)(-2m+2s+9)(-2m+2s+11)
(-m+s+3)(-m+s+4)(-m+s+5)(4m+2s+3)}.       \tag{4.1}
\end{aligned}
$$



Set $G_{s,m}=T_{s,m}C(s,m)$, interpreted by removable continuation at
the three points identified below.  The exact identity is



$$
\boxed{
G_{s,m+1}-G_{s,m}
=\sum_{j=0}^{3}P_j(s)T_{s+j,m}.}                           \tag{4.2}
$$



Here is a compact symbolic replay of (4.2).  For $j=0,1,2,3$,



$$
\frac{T_{s+j,m}}{T_{s,m}}
=
\frac{(2s+m+1)_{2j}}{(2s+1)_{2j}}
\frac{(3s+\frac32)_{3j}}
{(2s+6-2m)_{2j}(s+2m-\frac72)_j}
\frac{R(s+j,m)}{R(s,m)},                                  \tag{4.3}
$$



and



$$
\frac{T_{s,m+1}}{T_{s,m}}
=-\frac{2s+m+1}{m+1}
\frac{k(k-1)}
{(s+2m-\frac72)(s+2m-\frac52)}
\frac{R(s,m+1)}{R(s,m)}.                                  \tag{4.4}
$$



Substitution of (3.1)--(3.4) and (4.1) into



$$
C(s,m+1)\frac{T_{s,m+1}}{T_{s,m}}-C(s,m)
-\sum_{j=0}^{3}P_j(s)\frac{T_{s+j,m}}{T_{s,m}}             \tag{4.5}
$$



has zero numerator in $\mathbb Q[s,m]$.  The deterministic replay checks
this cleared polynomial identity exactly.

It remains to justify summation at the finite-support boundary.  In
$G=T\,C$, the factor $Q(s,m)$ cancels.  Thus:

1. The explicit factor $m$ in (4.1) gives $G_{s,0}=0$.

2. The only apparent poles at integral $m$ above the support of
   $T_{s,m}$ are

   

$$
m=s+3,\quad s+4,\quad s+5.                 \tag{4.6}
$$



   They come respectively from the three simple factors
   $-m+s+3,-m+s+4,-m+s+5$.  At these points $k=-1,-3,-5$.
   In

   

$$
{\alpha\choose k}
   =\frac{\Gamma(\alpha+1)}
          {\Gamma(k+1)\Gamma(\alpha-k+1)},                 \tag{4.7}
$$



   $1/\Gamma(k+1)$ has a simple zero, while the other gamma factor is
   finite because $\alpha$ is half-integral.  Each apparent simple pole
   is therefore removable.  Identity (4.2), first proved off these
   points, extends to them by taking limits.

3. At $m=s+6$, $k=-7$, so the same binomial factor is zero.  No
   denominator vanishes there; an explicit common denominator specializes
   to

   

$$
\begin{aligned}
   90&(s+1)(s+2)(s+3)(6s+17)(6s+19)(6s+21)\\
     &\hspace{27mm}\cdot(6s+23)(6s+25)(6s+27),             \tag{4.8}
   \end{aligned}
$$



   which is positive for $s\geq1$.  Hence $G_{s,s+6}=0$.

Summing (4.2) for $0\leq m\leq s+5$ captures the complete support of
every $T_{s+j,m}$, $0\leq j\leq3$, and gives



$$
\sum_{j=0}^{3}P_j(s)A_{s+j}
=G_{s,s+6}-G_{s,0}=0.                                    \tag{4.9}
$$



This proves (1.2) for every integer $s\geq1$.

## 5. Complete pivot factorization

The trailing and leading recurrence polynomials are already fully
factored in (3.1) and (3.4).  Their two quadratic factors have the common
discriminant



$$
2920^2-4(660)(3039)
=1600^2-4(660)(779)
=503440=16\cdot31465,                                     \tag{5.1}
$$



which is not a square.  Hence both quadratics are irreducible over
$\mathbb Q$.  All factors of $P_0(s)$ and $P_3(s)$ are positive for
$s\geq1$, so the characteristic-zero recurrence has no positive-index
singularity.

The constants $9$ and $4096$ are units at every actual prime because
Item 308 gives $p\geq6s+7\geq13$.

## 6. Exact fixed-$M$ localization of recurrence singularities

The actual indexing is



$$
\mathcal S_M=
\{s\geq1:4s\leq M-5,\ s\equiv M+1\pmod3\},
\qquad
p_s=\frac{4M+2s+1}{3}.                                    \tag{6.1}
$$



Whenever this cell is nonempty, $M\geq9$.  Modulo $p_s$,



$$
2s\equiv-(4M+1)\pmod {p_s}.       \tag{6.2}
$$



Apply (6.2) to every irreducible factor of $P_0,P_3$, clearing only
powers of two.  After discarding those $p_s$-unit contents, the exact
fixed-$M$ residues are



$$
\begin{array}{c|c}
\text{factor of }P_0(s)&\text{primitive fixed-\(M\) residue}\\ \hline
2s+1&-M\\
6s+5&1-6M\\
6s+7&1-3M\\
6s+11&2-3M\\
6s+13&5-6M\\
660s^2+2920s+3039&330M^2-565M+218
\end{array}                                                \tag{6.3}
$$



and



$$
\begin{array}{c|c}
\text{factor of }P_3(s)&\text{primitive fixed-\(M\) residue}\\ \hline
s&-4M-1\\
s+1&1-4M\\
s+2&3-4M\\
2s+3&1-2M\\
2s+5&1-M\\
660s^2+1600s+779&330M^2-235M+18.
\end{array}                                                \tag{6.4}
$$



Thus define



$$
\begin{aligned}
R_0(M)={}&-M(3M-2)(3M-1)(6M-5)(6M-1)\\
         &\hspace{24mm}\cdot(330M^2-565M+218),             \tag{6.5}\\
R_3(M)={}&-(M-1)(2M-1)(4M-3)(4M-1)(4M+1)\\
         &\hspace{24mm}\cdot(330M^2-235M+18).              \tag{6.6}
\end{aligned}
$$



Both are nonzero for $M\geq9$, and both have degree seven.  Equations
(6.2)--(6.4) prove



$$
\begin{aligned}
p_s\mid P_0(s)&\Longrightarrow p_s\mid R_0(M),\\
p_s\mid P_3(s)&\Longrightarrow p_s\mid R_3(M).             \tag{6.7}
\end{aligned}
$$



The map $s\mapsto p_s$ is injective on $\mathcal S_M$:
increasing $s$ by three increases $p_s$ by two.  Therefore distinct
singular rows contribute distinct prime divisors, and



$$
\begin{aligned}
\sum_{\substack{s\in\mathcal S_M,\ p_s\ {\rm prime}\\
                 p_s\mid P_0(s)P_3(s)}}\log p_s
&\leq\log|R_0(M)R_3(M)|\\
&=O(\log M)=o(M).                                         \tag{6.8}
\end{aligned}
$$



This rules out positive-linear mass caused by failure to invert a
recurrence pivot.  It does **not** say that a collision prime dividing
$D_{s,\epsilon}$ must divide a pivot, and therefore gives no direct
collision-prime saving.

## 7. Scoped no-go for bounded order and degree

Let $C_s={7s\choose s}$.  Exact factorial cancellation gives



$$
(s+1)\prod_{r=1}^{6}(6s+r)C_{s+1}
-\prod_{r=1}^{7}(7s+r)C_s=0.                              \tag{7.1}
$$



This recurrence has order one and both coefficients have degree seven.
Also



$$
\log C_s=s(7\log7-6\log6)+O(\log s)=O(s),                 \tag{7.2}
$$



and $C_s>0$.

If $p$ is prime and



$$
6s<p\leq7s,                 \tag{7.3}
$$



then $7s<2p$, $p>s$, and



$$
v_p{7s\choose s}
=\left\lfloor\frac{7s}{p}\right\rfloor
-\left\lfloor\frac{s}{p}\right\rfloor
-\left\lfloor\frac{6s}{p}\right\rfloor
=1.                                                        \tag{7.4}
$$



On the actual indexing (6.1), the condition $p_s\leq7s$ is



$$
s\geq\frac{4M+1}{19}.        \tag{7.5}
$$



The bijection $s\mapsto p_s$ takes this slice, up to bounded endpoints,
to



$$
\frac{28}{19}M\leq p\leq\frac32M.
                                                               \tag{7.6}
$$



Consequently the prime number theorem gives



$$
\sum_{\substack{s\in\mathcal S_M,\ p_s\ {\rm prime}\\
                 s\geq(4M+1)/19}}\log p_s
=\left(\frac32-\frac{28}{19}\right)M+o(M)
=\frac1{38}M+o(M).                                        \tag{7.7}
$$



This is $1/228$ after normalization by $6M$, a positive rate.
Therefore no theorem using only the information class



$$
\begin{gathered}
\text{nonzero integral sequence},\quad \log|u_s|=O(s),\\
\text{recurrence order}\leq3,\quad
\text{recurrence coefficient degree}\leq7
\end{gathered}                                             \tag{7.8}
$$



can force tied-prime weighted mass $o(M)$.

This comparison deliberately does not use the exact coefficients
(3.1)--(3.4), the Gaussian coordinate, or the Item 308 norm shape.  It is
only a no-go for the bounded recurrence information class.  Any
sequence-specific invariant of the exact operator remains admissible.

## 8. Capacity, strict labels, and the smallest remaining lemma

The exact recurrence and singular localization make the rational
coordinate effectively computable modulo every actual prime outside
weighted $o(M)$ pivot support.  They do not bound the zero set of the
regular transported state, and they do not control the Gaussian
coordinate needed by $D_{s,\epsilon}$.

The sufficient off-ray target remains



$$
\boxed{
\mathcal W_D(M)=
\sum_{\substack{s\in\mathcal S_M\setminus\{2,4,6\}\\
                 p_s\ {\rm prime}\\
                 p_s\mid D_{s,h_s\bmod2}}}\log p_s=o(M),
\qquad h_s=\frac{M-4s-2}{3}.}                              \tag{8.1}
$$



The smallest remaining lemma exposed by this item is a
sequence-specific moving-prime theorem for the exact paired state
$(a_s,b_{s,\epsilon})$, or an exact annihilator/invariant for
$B_s$ or $D_{s,\epsilon}$, proving that regular collision zeros in
(8.1) have weighted $o(M)$ support.  A moving-prime gcd bound followed
by control of the nondegenerate norm factors would also suffice.

- **PROVED:** the exact summand (2.5)--(2.11), the all-$s$ telescoper
  (3.1)--(4.9), endpoint removability, the complete pivot factorization,
  and the fixed-$M$ singular localization (6.7)--(6.8).

- **SCOPED INFORMATION-CLASS NO-GO:** order at most three, coefficient
  degree at most seven, integrality, nonvanishing, and exponential height
  alone cannot imply moving-prime $o(M)$, by (7.1)--(7.7).

- **EXACT FINITE ONLY:** none is used to prove the recurrence or any
  density statement.

- **OPEN:** absolute minimality of the displayed operator, a useful exact
  operator for $B_s$ or $D_{s,\epsilon}$, regular-state prime
  localization, (8.1), the fixed-$j=1$ closer, Route 1, and every
  conclusion about $e+\pi$.

- **NOT CLAIMED:** a prime scan, a factor census, that pivot divisibility
  is necessary for collision, that the comparison sequence is the actual
  sequence, or positive capacity.

The ledger remains



$$
\boxed{\text{capacity booked}=0,\qquad
       \text{fixed-}j=1\text{ ceiling}=\frac1{36}
       \text{ per }6M.}                                   \tag{8.2}
$$



Canonical integration changes no booked rate, retained ceiling, or route
status.

## 9. Deterministic replay

From the archive root, run

~~~text
python scripts/item312_A_telescoper_singular_no_go_certificate.py --output results/item312_A_telescoper_singular_no_go_certificate_replay.json
~~~

The checker pins the canonical Item 310 source, script, results, manifest,
hash list, and root audit.  It pins the exact telescoper-data appendix;
reconstructs $R,Q,J,C$; clears and verifies the rational telescoping
identity in $\mathbb Q[s,m]$; audits the removable and terminal
endpoints; factors both recurrence pivots; derives the two fixed-$M$
singularity containers; and checks the degree-seven comparison,
valuation, and mass normalization.  It uses exact symbolic arithmetic,
performs no prime scan, and factors no $D_{s,\epsilon}$.
