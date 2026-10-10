> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An exact local cofactor test for large-prime endpoint cancellation

Date: 2026-09-13. Original arithmetic continuation by audit_results.

The translated-cubic condition is necessary but does not by itself
distinguish a common endpoint zero from another apparent singularity.
This note supplies the missing sufficient local condition and proves
an exact valuation formula, including prime powers. The extra test
is whether one actual homogeneous-equation cofactor is a p-unit.
No bound for the resulting integer carrier is proved.

## 1. Archive and normalization

Inputs inspected: raw_large_prime_endpoint_gcd_carrier.md,
raw_hp_homogeneous_ode.md, and the local exponent discussion there.
The first proves the primitive cubic and the necessary endpoint
carrier, including arbitrary nonzero high-kernel solutions over
F_p for p>3n. The second supplies the actual Wronskian cofactors.
Neither inspected result made the carrier sufficient or separated
the three possible local vanishing sequences below. The present
proof uses the actual HP jets rather than assigning arbitrary
solutions to a scalar equation with the same Wronskian.

Fix the primitive integral actual triple
(A,B,C)=(Ahat,Bhat,Chat), with degree at most n, Taylor order3n+1,
C(1)=4B(1), and B(1)!=0 over Q. Set D=1+z². Keep exactly the
primitive integral cubic from the carrier note:



$$
Q(z)=\frac{\mathcal N(A,B,C)}{z^{3n-1}}
      =q_3z^3+q_2z^2+q_1z+q_0.
\tag{1}
$$



It is p-primitive for every p>3n. No monic scaling of Q is made.
Let



$$
G=\gcd(|Q(1)|,|Q'(1)|,|Q''(1)/2|),
\qquad h_p=\min(v_p(A(1)),v_p(B(1))).              \tag{2}
$$



The conventions are gcd(0,0,0)=0 and v_p(0)=infinity.

Use local t=z−1, choose the primitive F_loc of1/D with F_loc(1)=0,
and normalize the local exponential to exp(t), with value1 at t=0.
In characteristic zero, consider the ordered local functions



$$
(A+CF_{\rm loc},\ B e^t,\ C).
\tag{3}
$$



Subtracting constant multiples of the exponential and C columns from
the original R column is exactly the previously used gauge change.
The exponential rescaling merely removes its value at z=1.
For r>=0, let J_r be the derivative row of(3) at t=0, and write
W_ijk=det(J_i,J_j,J_k).

For reduction modulo p^h, these jets are defined algebraically:



$$
J_r=\left(
A^{(r)}(1)+\sum_{j=1}^r\binom rj C^{(r-j)}(1)F^{(j)}(1),
\ \sum_{j=0}^r\binom rj B^{(j)}(1),\ C^{(r)}(1)
\right),                                                     \tag{4}
$$



where F'=1/D. Every F^(j)(1) lies in Z[1/2]. The identities used
below are proved first in characteristic zero and are polynomial
identities in the integral jets with powers of2 as denominators;
they can therefore be reduced modulo every odd prime power.
No formal solution of e'=e over an entire characteristic-p power
series ring is assumed.

## 2. The one extra actual cofactor

Define the integer



$$
\boxed{E=-8W_{123}.}                              \tag{5}
$$



This is exactly A_(0,n)(1), where A_(0,n) is the coefficient of y
in the homogeneous third-order equation from
raw_hp_homogeneous_ode.md. Its formula there is
−D³ exp(−z)W123/z^(3n−2); the local exponential normalization
makes exp(−t)=1 at the endpoint, and D(1)³=8. Thus (5) retains
the actual primitive triple's cubic scale.

Explicitly, all evaluations below are at z=1:



$$
\begin{aligned}
J_1&=(A'+C/2,\ B+B',\ C'),\\
J_2&=(A''+C'-C/2,\ B+2B'+B'',\ C''),\\
J_3&=(A'''+3C''/2-3C'/2+C/2,
                 \ B+3B'+3B''+B''',\ C''').
\end{aligned}                                                     \tag{6}
$$



The first columns have denominator at most2, so E is indeed an
integer (in fact a multiple of4). It is not an arbitrarily
normalized scalar-ODE coefficient. Multiplying the triple by a
common scalar multiplies Q and E by the same third power; the
primitive integral normalization is retained in the arithmetic
conclusions.

## 3. Exact jet identities at a cubic endpoint root

Let W(t) be the Wronskian W012 of the local functions(3). The
Wronskian identity defining Q is



$$
W(t)=\frac{e^t(1+t)^{3n-1}}{[1+(1+t)^2]^2}\,Q(1+t).
\tag{7}
$$



When reducing(7), only its derivatives through order3 are used;
the requisite exponential Taylor coefficients have unit denominators
for p>3. No reduction of an unrestricted exponential power series
is intended.

Differentiating a determinant, terms with repeated rows vanish.
At t=0 this gives the exact identities



$$
\begin{aligned}
W(0)&=W_{012},\\
W'(0)&=W_{013},\\
W''(0)&=W_{023}+W_{014},\\
W'''(0)&=W_{123}+2W_{024}+W_{015}.
\end{aligned}                                                     \tag{8}
$$



All identities extend modulo odd prime powers by(4). Suppose



$$
Q(z)\equiv q_3(z-1)^3\pmod{p^h}.                  \tag{9}
$$



Then (7), or its derivatives through order3, gives



$$
W_{012}=W_{013}=W_{023}+W_{014}=0\pmod{p^h},
\qquad W'''(0)\equiv\tfrac32 q_3\pmod{p^h}.
\tag{10}
$$



Here the factor3/2 is 3!/D(1)². If p>3n and(9) holds with h>=1,
p-primitivity of Q forces q_3 to be a p-unit: otherwise every
coefficient of Q would vanish modulo p.

## 4. Necessary and sufficient criterion, including every prime power

**Theorem.** For every p>3n and every h>=1, the actual primitive
triple satisfies



$$
\boxed{
A(1)\equiv B(1)\equiv0\pmod{p^h}
\ \Longleftrightarrow\
\left\{
\begin{array}{l}
Q(z)\equiv q_3(z-1)^3\pmod{p^h},\\
p\nmid E.
\end{array}\right.}
\tag{11}
$$



Whenever these conditions hold, there is also the exact congruence



$$
\boxed{E\equiv-12q_3\pmod{p^h}.}                 \tag{12}
$$



**Necessity.** The endpoint relation gives C(1)=0 modulo p^h, so
J_0=0. The carrier theorem proves(9) and the unit property of q_3.
In(8), W024 and W015 vanish because they contain J_0. Equations
(8)–(10) therefore imply W123=3q_3/2 modulo p^h, which gives
(12). Since p>3n>=3, the multiplier12 is a unit. Thus p does not
divide E.

**Sufficiency.** Work over the local ring R=Z/p^h Z. By(5), p does
not divide E exactly when W123 is a unit. Consequently the three
rows J_1,J_2,J_3 form an R-basis of R³. Write uniquely



$$
J_0=aJ_1+bJ_2+cJ_3.
$$



The first two zero determinants in(10) give c=0 and b=0: their
coefficients are respectively W123 and −W123, both units.
Therefore J_0=aJ_1. Now



$$
W_{023}+W_{014}
=aW_{123}+\det(aJ_1,J_1,J_4)=aW_{123}.
$$



The third vanishing in(10) forces a=0. Hence J_0=0 modulo p^h,
which says exactly A(1)=B(1)=C(1)=0. This proves sufficiency.
It also proves (12) from(8) as before. □

No diagonalization, Hensel analytic dependence, or division by a
nonunit has been used. The proof works over every odd-prime local
ring with the stated cofactor unit; p>3n enters through the actual
primitive-cubic input and p>3. It applies as well to arbitrary
nonzero finite-field high-kernel triples with endpoint matching.

An equivalent four-congruence form replaces the unit test in(11) by
E+12q_3=0 modulo p^h: the carrier already makes q_3 a unit, so that
extra congruence supplies the unit test automatically.

## 5. Exact valuation refinement of the previous carrier

**Corollary.** For every p>3n,



$$
\boxed{
h_p=
\begin{cases}
0,&p\mid E,\\
v_p(G),&p\nmid E.
\end{cases}}
\tag{13}
$$



For p dividing E, any positive endpoint valuation would contradict
the necessary unit condition. For p not dividing E, apply(11) for
every h: the carrier congruence is equivalent to h<=v_p(G),
by the translation identities in the carrier note. Thus all
prime-power thresholds agree exactly, proving(13).

This turns the necessary carrier into an exact endpoint-gcd
description after excluding the prime support of one additional
integer E. If G!=0, the large-prime part of the endpoint gcd is
obtained from G by removing every prime factor that divides E,
then retaining only primes above3n. This includes the full
valuation at every prime that remains.

If G=0, then E=0. To prove this assertion without a valuation
convention ambiguity, repeat the sufficiency proof over Q. The
identity Q=q_3(z−1)³ and E!=0 would force J_0=0 over Q, contradicting
the actual B(1)!=0. Hence G=0 implies E=0, and (13) says that in
this exceptional case there is no endpoint cancellation at any
prime above3n. If E=0 but G!=0, the same absence of large-prime
cancellation follows directly from(13).

Keep U_n=|Delta_B|/delta_n from the primitive-cofactor carrier note.
Its proved normalization gives v_p(U_n)=v_p(B(1)) for p>3n.
For the actual reduced endpoint denominator q_n, the previous
divisor statement sharpens to the exact formula



$$
\boxed{
v_p(q_n)=v_p(U_n)
-\begin{cases}
0,&p\mid E,\\
v_p(G),&p\nmid E,
\end{cases}
\qquad p>3n.}                                    \tag{14}
$$



No full maximal-minor content delta_n has been reintroduced into
the endpoint carrier. Its removal remains essential.

### 5.1. A nonzero four-integer carrier with exact valuations

The following sharpening was proposed by root during independent
review. Define



$$
\boxed{\mathfrak F=
\gcd\bigl(|Q(1)|,|Q'(1)|,|Q''(1)/2|,|E+12q_3|\bigr).}
\tag{17}
$$



Then mathfrak F is a positive, nonzero integer and



$$
\boxed{v_p(\mathfrak F)=h_p\quad\text{for every }p>3n.}
\tag{18}
$$



Indeed the four-congruence version of(11) holds for every prime
power, proving(18). To prove nonzero without choosing a prime,
if all four integers vanished then G=0, hence E=0 by the preceding
argument over Q. The fourth integer would then be12q_3!=0,
contradicting the proved all-index nonzero cubic coefficient.

Thus the large-prime primitive denominator has the exact identity



$$
\boxed{(q_n)_{>3n}=(U_n)_{>3n}/(\mathfrak F)_{>3n}.}
\tag{19}
$$



The denominator on the right divides the numerator, by the same
valuation identities. Formula(17) avoids both prime-support
saturation and the zero-G convention. It still requires a bound
on the size of this actual four-integer gcd to produce an
asymptotic arithmetic estimate.

## 6. Finite-field local ranks and why the cubic alone is insufficient

For n>=2, p>3n implies p>=7. The local functions(3) therefore have
well-defined Taylor polynomials through degree5 over F_p: all
factorials up to5 are units. Under(9) modulo p, W has order exactly3
and nonzero cubic coefficient q_3/4.

The derivative rows J_0,...,J_5 have rank3, since the nonzero third
Wronskian derivative in(8) is a sum of their3-by-3 minors. Put
the three truncated local functions into a constant echelon basis
with distinct initial orders d_0<d_1<d_2<=5. The leading Wronskian
coefficient is their leading-coefficient product times the
Vandermonde product of the d_i. Every nonzero difference between
these orders is a unit because p>=7. The exact order relation is
therefore



$$
d_0+d_1+d_2-3=3.
$$



There are precisely three possibilities:



$$
\boxed{(d_0,d_1,d_2)=(0,1,5),\quad(0,2,4),\quad(1,2,3).}
\tag{15}
$$



In the first case the ranks of J_0,...,J_j reach1,2,3 at
j=0,1,5. In the second they reach those ranks at j=0,2,4.
In the third they reach them at j=1,2,3. Only the third case has
J_0=0; it is exactly the endpoint-cancellation case. Equivalently,
only the third has W123!=0, or E!=0. Thus the cofactor test in(11)
selects the actual correct local rank type.

This classification does not assert that all three types occur in
the actual global HP kernel. Simple local examples show why
Wronskian order or absence of logarithms alone cannot select one:
the analytic spans {1,t,t^5}, {1,t²,t^4}, and {t,t²,t³} have the
respective order types in(15) and Wronskians with order3, but only
the last span vanishes at the endpoint. These are local examples,
not claimed HP counterexamples.

For n=1 the criterion and valuation proof already work for every
p>3. To dispose of the characteristic5 exception in the order-type
argument, the actual high equations **together with endpoint matching**
can be solved once symbolically. They give the line spanned by



$$
A=14-19z,\quad B=-14+16z,\quad C=17-9z
\tag{16}
$$



over every field of characteristic greater than3. Indeed the two
high rows give c_1=−b_0/2−b_1 and c_0=(b_0+3b_1)/2; the endpoint
row then gives8b_0+7b_1=0, with8 a unit. The high rows alone have a
two-dimensional kernel; no one-dimensional claim is made for them
without the endpoint row. This triple has B(1)=2. Its cubic is



$$
Q=-1856z^3-6984z^2-10788z+5612,
$$



and its translated carrier entries are −14016,−30324,−12552,
with gcd12. Therefore the cubic endpoint condition never occurs
for this degree at a prime above3, including p=5. No finite-field
rank type relevant to the carrier is omitted.

## 7. Remaining arithmetic problem

The exact large-prime cancellation is now determined by two concrete
objects: the translated-cubic gcd G and the prime support of the
actual cofactor E=A_(0,n)(1). This is stronger than the previous
necessary cubic degeneration test and is uniform over every
prime power. It does not bound either integer's size, factorization,
or their joint prime support as n grows.

A useful next arithmetic target is the part of G supported on
primes p>3n for which E is a unit; equivalently it is the exact
large-prime endpoint gcd in(13), or the nonzero four-integer carrier
in(17). Bounds on Q's raw coefficient
denominators, nonvanishing of q_3, or generic no-log conditions
do not provide that estimate. No shrinking integer form or
irrationality conclusion follows from the local classification
alone.

## 8. A universal bounded-jet Bezout identity and the false-carrier factor

There is an additional algebraic identity giving a finite bound on
the prime powers discarded from G. In this section use
V=W123, w_0=W012, w_1=W013, and w_2=W023+W014=W''(0).
These lower-case symbols are scalars, not the polynomial coefficients
of Q. Cofactor expansion of J_0 in the rows J_1,J_2,J_3 gives the
unconditional vector identity



$$
VJ_0=W_{023}J_1-W_{013}J_2+W_{012}J_3.             \tag{20}
$$



No determinant is divided out in(20). Taking its determinant with
J_1,J_4 gives the Plucker identity



$$
VW_{014}=W_{013}W_{124}-W_{012}W_{134}.
$$



Since W023=w_2−W014, substitution in(20) proves



$$
\boxed{
V^2J_0=
(Vw_2-w_1W_{124}+w_0W_{134})J_1
       -Vw_1J_2+Vw_0J_3.}                        \tag{21}
$$



All coefficients are explicit polynomials in the local rows through
order4, over Z[1/2]. This is a fixed-size identity valid for every
actual triple and every n; it is not a resultant with a growing
polynomial degree. Differentiating(7) through order2 shows that
(w_0,w_1,w_2) and (Q(1),Q'(1),Q''(1)/2) generate the same ideal
over Z_p for every odd p, because the change-of-generators matrix
is triangular with unit diagonal entries1/4,1/4,1/2.

For every p>3n, (21) therefore gives



$$
\boxed{v_p(G)\le h_p+2v_p(E),}                   \tag{22}
$$



whenever the right side is finite; the identity itself also covers
zero determinants. To see the valuation assertion, choose a
coordinate of J_0 having valuation h_p. This is possible because
J_0=(A(1),B(1),4B(1)). The corresponding left side has valuation
h_p+2v_p(V)=h_p+2v_p(E), whereas every term on the right is divisible
by p^(v_p(G)).

Combining(22) with(13), every false-carrier prime p>3n dividing E
satisfies v_p(G)<=2v_p(E). For G!=0, the exact endpoint-gcd formula
can consequently be written using only ordinary integer gcds:



$$
\boxed{
(\gcd(|A(1)|,|B(1)|))_{>3n}
=\frac{G_{>3n}}{\gcd(G,E^2)_{>3n}}.}             \tag{23}
$$



If E=0 and G!=0, the denominator equals the numerator and the
quotient is1, as already proved. If G=0, the always-nonzero
carrier(17) remains the appropriate formulation.

There is also a direct Bezout certificate for the four-integer
ideal I generated in(17). Multiplying(21) by64 shows
E²J_0 is in the ideal generated by the first three carrier entries,
over Z[1/2]. The identity



$$
144q_3^2J_0
=E^2J_0-(E-12q_3)(E+12q_3)J_0                  \tag{24}
$$



therefore places every coordinate of144q_3²J_0 in I.
At any prime p>3n dividing I, the first three entries force q_3
to be a unit;144 is also a unit. Thus this is an explicit bounded-jet
Bezout certificate for the sufficient endpoint ideal, consistent
with the exact prime-power proof above.

Equations(21)–(24) control local divisibility and show that false
carrier valuations are absorbed by E². They do not provide an
Archimedean bound for the Bezout coefficients, which still depend
on the actual polynomial jets, or an asymptotic upper bound for
mathfrak F. No such size estimate follows merely from the fixed
number of rows in this identity.

Verification artifact: check_raw_endpoint_local_classification.py
checks the universal Cramer, Plucker and quadratic vector identities
in15 algebraically independent jet coordinates, and the single
n=1 endpoint-matched boundary case. Its saved output
raw_endpoint_local_classification_checks.json reports all checks
passed. The n=1 cofactor is E=−89640, and its four-entry carrier
still has gcd12. No additional prime or degree was sampled.
