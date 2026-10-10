> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 368 — Whipple rectangle, target-line saturation, and the growing-state obstruction for the two (j=1) boundary carriers

Checked: 2026-09-01 (Beijing time)

## 1. Admission, capacity, and verdict

Retain the actual fixed-(j=1) family



$$
p=4h+6s+3,
 \qquad
 M=3h+4s+2,
 \qquad h,s\geq1,
\tag{1.1}
$$



and the two saturation boundaries isolated in Item 364,



$$
\mathcal B_{xy}=\{x=y=0\},
 \qquad
 \mathcal B_{uv}=\{u=v=0\}.
\tag{1.2}
$$



They are subsets of one full collision gate.  They and the nonboundary
chart share the same raw fixed-(j=1) ceiling



$$
{1\over6}\quad\hbox{per }M,
 \qquad
 {1\over36}\quad\hbox{per }6M,
\tag{1.3}
$$



and are not additive.

This item tests the strongest standard completion suggested by the Item
364 phase carriers.  Its outcome is structural, but negative for the
ledger.

> **PROVED — exact target-line saturation.**  Each of the four periods has
> a first-order denominator-clearing recurrence.  After imposing the tied
> line (6s+4h+3=0), the two boundary carriers are precisely the common
> large-prime support of two linear resultants.  Every prime at most
> (4h+3) can be removed once and for all, because an actual tied prime
> satisfies (p\geq4h+9).  Exact-zero phase pairs remain separate strata.

> **PROVED — crossed Whipple completion.**  The pair (X_h,Y_h) is the
> diagonal of a (2\times2) rectangle of terminating very-well-poised
> ${}_4F_3(-1)$ values.  Both crossed entries have exact Whipple product
> evaluations, and both are (p)-units for every actual tied prime.
> However, the actual and matched parameters differ by
> 

$$
> \delta_h={10h+3\over6}\notin\mathbb Z
>
$$


> on every potentially prime ray.  Classical integer-contiguous transfer
> therefore cannot connect a Whipple value to either actual entry.

> **PROVED — linear parameter-state growth.**  The parameter-uniform
> denominator state of the (K_0) family has exact rank (h+1).  For the
> (K_1) even and odd families the corresponding ranks are at least
> (h-3) and (h-4).  Thus a bounded matched-value interpolation or a
> bounded coefficient-state transfer cannot close either boundary.  This
> is a scoped no-go, not a nonvanishing theorem for the two actual moving
> parameter values.

Ordinary fixed-(h) resultants have logarithmic height only bounded by
(O(h^2\log h)), while the already sharper target-line carriers have
pointwise height (O(h\log h)).  A saturated version of Item 364's
order-one comparison still carries (M/8+o(M)) Chebyshev mass.  Hence
fixed-order recurrence, pointwise height, ordinary resultants, and a
generic divisor sieve—even after removing all primes at most (4h+3)—do
not imply weighted zero density.

Consequently



$$
\boxed{\text{new booking}=0},
 \qquad
 \boxed{\text{new capacity reduction}=0},
 \qquad
 \boxed{\text{shared fixed-}j=1\text{ ceiling remains }1/36}.
\tag{1.4}
$$



The first missing arithmetic input is now precise: a target-specific
large-prime average-gcd or weighted-divisibility theorem for the two
actual off-diagonal periods.

## 2. The universal clearing recurrence

For a polynomial (K(z)=\sum_j k_jz^j), parity
(\epsilon\in\{0,1\}), and a terminal index (n), put



$$
\mathcal S_{K,\epsilon,n}(A;B)
 =\sum_{t=0}^{n}(-1)^t{(A)_t\over(B)_t}k_{\epsilon+2t}.
\tag{2.1}
$$



The four Item 364 periods are instances of (2.1).  Define



$$
d_t=(-1)^t(A)_t k_{\epsilon+2t},
 \qquad
 Q_0=d_0,
 \qquad
 Q_t=(B+t-1)Q_{t-1}+d_t.
\tag{2.2}
$$



Induction gives the exact identity



$$
\boxed{
 \mathcal S_{K,\epsilon,n}(A;B)={Q_n(A,B)\over(B)_n}.}
\tag{2.3}
$$



This is the cleanest fixed-(h) recurrence: it is first order in the
summation cutoff, but its cleared polynomial state grows with the cutoff.

Use



$$
K_0=(1-z)^{2h}(1+z),
 \qquad
 K_1=(1-z)^{2h}(1+z)^4.
\tag{2.4}
$$



The four denominator-cleared polynomials in (mathbb Z[s]) are



$$
\begin{aligned}
 \widehat X_h(s)&=Q_{K_0,1,h}(s+1,3s+2),\\
 \widehat Y_h(s)&=Q_{K_0,1,h}(h+1,2s+h+2),\\
 \widehat U_h(s)&=Q_{K_1,0,h+2}(s,3s),\\
 \widehat V_h(s)&=Q_{K_1,1,h+1}(h+1,2s+h+1).
\end{aligned}
\tag{2.5}
$$



They satisfy



$$
\begin{aligned}
 x&={\widehat X_h(s)\over(3s+2)_h},
 &y&={\widehat Y_h(s)\over(2s+h+2)_h},\\
 u&={\widehat U_h(s)\over(3s)_{h+2}},
 &v&={\widehat V_h(s)\over(2s+h+1)_{h+1}}.
\end{aligned}
\tag{2.6}
$$



Every denominator factor in (2.6) is a (p)-unit on an actual positive
row.  The degrees of the four cleared polynomials are at most
(h,h,h+2,h+1), respectively.

## 3. Linear resultants and the primitive large-prime carriers

Put



$$
L_h(s)=6s+4h+3,
 \qquad
 \sigma_h=-{4h+3\over6}.
\tag{3.1}
$$



For any (P\in\mathbb Z[s]), with (d=\deg P), the linear resultant is



$$
\operatorname {Res}_s(L_h,P)=6^dP(\sigma_h).
\tag{3.2}
$$



Thus the four phase values of Item 364 are the corresponding linear
resultants divided only by rational products of linear factors whose
prime divisors are at most (4h+3).

For a nonzero integer (N), define



$$
\operatorname {Sat}_{>B}(N)
 ={N\over\prod_{q\leq B}q^{v_q(N)}},
 \qquad
 \operatorname {Rad}_{>B}(N)
 =\prod_{\substack{q\mid N\\q>B}}q.
\tag{3.3}
$$



If a phase pair is not exactly zero, define the primitive ordinary-gate
carriers



$$
\begin{aligned}
 \mathfrak G_0(h)
 &=\operatorname {Rad}_{>4h+3}
   \gcd\bigl(\operatorname {num}X_h,
             \operatorname {num}Y_h\bigr),\\
 \mathfrak G_1(h)
 &=\operatorname {Rad}_{>4h+3}
   \gcd\bigl(\operatorname {num}U_h,
             \operatorname {num}V_h\bigr).
\end{aligned}
\tag{3.4}
$$



All repeated valuations and every prime too small to equal an actual
tied prime have now been removed.  Equations (2.6)–(3.2) give exact
equality of large-prime support between (3.4) and the gcds of the paired
linear resultants.  In particular,



$$
\boxed{
 \mathcal B_{xy}\Longrightarrow p\mid\mathfrak G_0(h),
 \qquad
 \mathcal B_{uv}\Longrightarrow p\mid\mathfrak G_1(h),}
\tag{3.5}
$$



outside the exact-zero phase strata.

Let



$$
\mathcal Z_0=\{h:X_h=Y_h=0\text{ in }\mathbb Q\},
 \qquad
 \mathcal Z_1=\{h:U_h=V_h=0\text{ in }\mathbb Q\}.
\tag{3.6}
$$



These sets are retained separately; defining a zero integer carrier on
them would hide rather than solve the issue.  The (h=2) identity
(V_2=0) is not an exact-zero pair because (U_2\ne0), and Item 364
already excludes that entire actual ray.

## 4. The (K_0) phase pair is an off-diagonal Whipple rectangle

Set



$$
a_0={1\over2}-h,
 \qquad
 c_0={1-2h\over4}={a_0\over2}.
\tag{4.1}
$$



Direct coefficient extraction gives, for (0\leq t\leq h),



$$
[z^{2t+1}]K_0
 =(1-2h)
 {(-h)_t(\frac12-h)_t(c_0+1)_t
  \over
  (\frac32)_t(c_0)_t,t!}.
\tag{4.2}
$$



Define



$$
\mathcal F_h(A;B)
 ={}_4F_3\!\left(
 \begin{matrix}
 -h,\ \frac12-h,\ c_0+1,\ A\\
 \frac32,\ c_0,\ B
 \end{matrix};-1\right).
\tag{4.3}
$$



At the tied phase, put



$$
A_s={3-4h\over6},
 \qquad A_h=h+1,
 \qquad B_s={1-4h\over2},
 \qquad B_h=1-{h\over3}.
\tag{4.4}
$$



Then



$$
\boxed{
 X_h=(1-2h)\mathcal F_h(A_s;B_s),
 \qquad
 Y_h=(1-2h)\mathcal F_h(A_h;B_h).}
\tag{4.5}
$$



The relevant specialization of Whipple's classical transformation is



$$
{}_4F_3\!\left(
 \begin{matrix}
 a,\ 1+\frac a2,\ c,\ d\\
 \frac a2,\ 1+a-c,\ 1+a-d
 \end{matrix};-1\right)
 ={\Gamma(1+a-c)\Gamma(1+a-d)
   \over
   \Gamma(1+a)\Gamma(1+a-c-d)}.
\tag{4.6}
$$



Our series terminates through ((-h)_t), so (4.6) is an exact finite
identity with no convergence issue.  The matched denominator for (A_s)
is (B_h), whereas the matched denominator for (A_h) is (B_s).
Therefore the two crossed entries evaluate to



$$
\boxed{
 \mathcal F_h(A_s;B_h)
 ={(\frac32-h)_h\over(1-\frac h3)_h},
 \qquad
 \mathcal F_h(A_h;B_s)
 ={(\frac32-h)_h\over(\frac12-2h)_h}.}
\tag{4.7}
$$



This is the complete natural Whipple completion of the (K_0) pair.

If (3\nmid h), none of the product factors in (4.7) vanishes.  After
clearing 2 and 3, their absolute linear factors are bounded respectively
by (2h) and (4h-1).  Since every actual prime satisfies



$$
p=4h+6s+3\geq4h+9,
\tag{4.8}
$$



both values in (4.7), and also their multiples by (1-2h), are
(p)-units.

The obstruction is visible directly in the rectangle:



$$
\boxed{
 A_h-A_s=B_h-B_s={10h+3\over6}=\delta_h.}
\tag{4.9}
$$



When (3\nmid h), the fractional part of (delta_h) is (1/6) or
(5/6).  Classical contiguous relations shift hypergeometric parameters
by integers.  Hence no finite chain of such relations can move
((A_s,B_h)) to ((A_s,B_s)), or ((A_h,B_s)) to ((A_h,B_h)).
The exact Whipple products are genuine (p)-unit companions, but they do
not imply that either actual diagonal entry is nonzero.

## 5. Exact (h+1) denominator-state rank

Write (4.3) as



$$
\mathcal F_h(A;B)
 =\sum_{t=0}^{h}D_{h,t}{(A)_t\over(B)_t},
\tag{5.1}
$$



where every (D_{h,t}\ne0).  As (A) varies, the polynomials
((A)_0,\ldots,(A)_h) form a basis.  Consequently



$$
\operatorname {span}_{A}{B\mapsto\mathcal F_h(A;B)}
 =\operatorname {span}\left\{{1\over(B)_t}:0\leq t\leq h\right\}.
\tag{5.2}
$$



Multiplication by ((B)_h) sends the displayed functions to



$$
{(B)_h\over(B)_t}=(B+t)_{h-t}.
\tag{5.3}
$$



These are monic polynomials of the distinct degrees
(h,h-1,\ldots,0).  Thus they are linearly independent, and



$$
\boxed{
 \dim\operatorname {span}_{A}{\mathcal F_h(A;\cdot)\}=h+1.}
\tag{5.4}
$$



Equation (5.4) closes a precise method class.  Any transfer which treats
the denominator basis coefficient by coefficient, or reconstructs a
parameter-uniform member from a bounded collection of matched scalar
values, encounters a linearly growing state.  It does **not** rule out a
new identity specialized simultaneously to the two actual moving values
(A_s,A_h).  Such target-specific arithmetic remains open.

## 6. The second boundary retains linear state

Let (k^{(1)}_j=[z^j]K_1).  For (0\leq j\leq2h), exact convolution
gives



$$
k^{(1)}_j
 =(-1)^j{2h\choose j}{P_h(j)\over(2h-j+1)_4},
\tag{6.1}
$$



where



$$
\begin{aligned}
 {P_h(j)\over4}={}&
 4h^4-16h^3j+20h^3+24h^2j^2-72h^2j+35h^2\\
 &-16hj^3+84hj^2-112hj+25h\\
 &+4j^4-32j^3+80j^2-64j+6.
\end{aligned}
\tag{6.2}
$$



As a polynomial in (j), (P_h(j)) is a nonzero quartic with leading
coefficient (16).  Hence at most four of the interior coefficients
(k^{(1)}_j), (0\leq j\leq2h), vanish.  The same triangular argument as
in Section 5 gives



$$
\boxed{
 \operatorname {rank}(K_1\text{ even family})\geq h-3,
 \qquad
 \operatorname {rank}(K_1\text{ odd family})\geq h-4.}
\tag{6.3}
$$



Boundary coefficients above (2h) can only increase these ranks.  At
(h=2), the odd family is exactly zero because
(K_1=(1-z^2)^4); this is the already closed exceptional face from Item
364.  Apart from such finite degeneracies, the (U,V) boundary does not
collapse to a bounded universal state.

## 7. Why ordinary resultants and a generic sieve still miss the scale

Before imposing (L_h(s)=0), one may form



$$
R_0(h)=\operatorname {Res}_s(\widehat X_h,\widehat Y_h),
 \qquad
 R_1(h)=\operatorname {Res}_s(\widehat U_h,\widehat V_h).
\tag{7.1}
$$



If nonzero, each is a valid necessary carrier for the corresponding
boundary.  But it is weaker than Section 3: it allows every common root,
not only the tied root (sigma_h).  The coefficient heights of (2.5) are
(O(h\log h)), and their degrees are (O(h)), so the Sylvester
determinant gives only



$$
\log|R_i(h)|=O(h^2\log(h+2)).
\tag{7.2}
$$



The target-line gcds already improve this to the Item 364 pointwise
(O(h\log h)) bound, but at fixed (M) even that sums only to
(O(M^2\log M)), not (o(M)).  Thus an ordinary fixed-(h) resultant
cannot improve the ledger unless it is followed by a new target-specific
factor or average-gcd theorem.

Small-prime saturation also does not make generic height and recurrence
arguments sufficient.  Reuse Item 364's comparison



$$
\mathcal C_h={(18h)!\over(4h)!}=(4h+1)_{14h}
\tag{7.3}
$$



and remove every prime at most (4h+3), obtaining
(operatorname {Sat}_{>4h+3}(\mathcal C_h)).  On the bulk



$$
{M\over12}\leq h\leq{M\over3},
\tag{7.4}
$$



every actual candidate satisfies



$$
4h+3<p={3M-h\over2}<18h.
\tag{7.5}
$$



It therefore divides the saturated comparison carrier.  This bulk is
the prime interval



$$
{4M\over3}\leq p\leq{35M\over24},
\tag{7.6}
$$



and has Chebyshev mass (M/8+o(M)), or (1/48) per (6M).  The parent
carrier (7.3) has an order-one rational recurrence and
(O(h\log h)) pointwise height.  Therefore the pipeline



$$
\text{fixed-order recurrence}
 +\text{ pointwise height}
 +\text{ remove all small primes}
 +\text{ generic divisor sieve}
\tag{7.7}
$$



cannot by itself prove zero rate.  The comparison is not asserted to
share the target-specific arithmetic of (3.4).

## 8. Exact remaining weighted theorem

For a fixed (M), let



$$
h=3M-2p,
 \qquad
 p_h={3M-h\over2},
\tag{8.1}
$$



over the actual integral rows.  Sections 2–7 reduce the boundary question
to the following target and do not prove it:



$$
\boxed{
 \sum_{\substack{h\text{ actual at }M\\p_h\text{ prime}}}
 (\log p_h)
 \left(
  1_{h\in\mathcal Z_0\cup\mathcal Z_1}
  +1_{h\notin\mathcal Z_0\cup\mathcal Z_1}
   1_{p_h\mid\mathfrak G_0(h)\mathfrak G_1(h)}
 \right)
 =o(M).}
\tag{8.2}
$$



A proof of (8.2) would make both saturation boundaries zero rate.  It
would not remove the nonboundary chart and therefore would not by itself
book (1/36).  What is missing is cross-(h), target-specific arithmetic:
an average gcd, a large-prime-factor restriction for the actual
off-diagonal hypergeometric values, or a selector-aware large sieve.

## 9. Strict labels

### PROVED

- the universal clearing recurrence (2.2)–(2.3);
- the four integer cleared polynomials and their linear target-line norms;
- exact large-prime saturation and the boundary implications (3.5);
- the (K_0) hypergeometric rectangle (4.2)–(4.5);
- both crossed Whipple products and their actual-prime unit property;
- the nonintegral contiguity gap (4.9);
- exact (K_0) parameter-state rank (h+1);
- linear lower bounds for both (K_1) parameter-state ranks;
- dominance of the tied linear norms over ordinary fixed-(h) resultants;
- the saturated recurrence-height-divisor-sieve barrier;
- zero booking, zero capacity reduction, and retention of the shared
  (1/36) ceiling.

### EXACT FINITE ONLY

- eight predeclared exact Whipple controls;
- six predeclared (K_0) rank controls;
- six predeclared (K_1) coefficient controls;
- six predeclared target-line saturation controls;
- three predeclared comparison controls;
- no prime scan, boundary census, or extrapolation.

### OPEN

- classification of (mathcal Z_0,mathcal Z_1);
- occurrence or nonoccurrence of either boundary for unbounded (h);
- the weighted theorem (8.2);
- a target-specific identity coupling the two actual moving numerator
  parameters despite the parameter-uniform rank obstruction;
- any strict fixed-(j=1) capacity reduction, Route 1, and every conclusion
  about (e+\pi).

The proved no-go is deliberately scoped.  It closes the natural crossed
Whipple completion, classical integer contiguity, bounded
parameter-uniform state, ordinary resultant height, and generic saturated
divisor-sieve reasoning.  It does not claim that all target-specific
arithmetic methods are impossible.
