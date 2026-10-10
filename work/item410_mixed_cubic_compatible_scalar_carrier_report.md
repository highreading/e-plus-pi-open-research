> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 410 — Compatible scalar carrier for the mixed-cubic H branch

Date: 2026-09-01  
Status: **WORK ONLY, UNAUDITED, NO CENTRAL EDIT, NO BOOKING**

## 1. Capacity admission and verdict

Canonical Item 403 writes the actual largest fixed-gap Smith invariant,
away from (6), as



$$
d_3(q)=H_qG_q^{\rm prim}.
$$



Work Item 406 proves that, for a compatible prime



$$
p=6m+q,qquad m\ge1,qquad q\ge5,qquad n=q-1,qquad k=4m+1,
$$



the condition (p\mid H_q) is equivalent to simultaneous vanishing of the
degree-((n-1,n)) coefficient pairs of



$$
R_m(z)=\frac{(1-z)^{6m}}{(1+z^2)^k},
 \qquad
 S_m(z)=\frac{R_m(z)}{(1+z)^k}.
$$



The capacity audit must come first.  Even perfect exclusion of compatible
primes from (H_q) has **zero presently proved numerical ceiling
reduction**: the primitive (G_q^{\rm prim}) stratum can still occupy the
whole combined Item-390 large-prime ceiling



$$
\frac{\log136}{6}=0.8187758142893420014\ldots .
$$



Thus this is admitted only as a structural Closer problem.  It cannot add a
divisor to the booked rate, and it cannot by itself reduce the master
capacity ledger.

The new uniform result is an exact collapse of the moving compatible-prime
condition to four rational scalars depending only on (m) and one of two
phases.  In particular, every compatible (H)-collision prime divides a
single phase-independent integer (W_m).  This yields a rigorous weighted
mass carrier and an explicit (O(m)) height bound (outside a precisely
declared identically-resonant exceptional set).  The resulting constant is
worse than the inherited Item-390 ceiling, so it is not booked.

Finite exact normalization through (m=128) suggests the much stronger
support statement



$$
\operatorname{rad}J_{m,\delta}\mid (6m)!,
 \qquad \delta\in\{0,2\},
$$



which would prove the four-adjacent lemma at once.  This is **finite evidence
only**.  Two tempting multiplicity strengthenings already fail in the same
finite range, so neither is promoted to a conjectural theorem.

## 2. Exact simplification and recurrence for (S_m)

The factorization



$$
(1+z)(1+z^2)=\frac{1-z^4}{1-z}
$$



gives the exact normal forms



$$
\boxed{
 S_m(z)=\frac{(1-z)^{10m+1}}{(1-z^4)^{4m+1}},
 \qquad
 R_m(z)=(1+z)^{4m+1}S_m(z).}
 \tag{2.1}
$$



Write (S_m(z)=\sum_{j\ge0}s_jz^j), with (s_j=0) for (j<0).  Logarithmic
differentiation of (2.1), followed by coefficient extraction, proves



$$
\boxed{
 (j+1)s_{j+1}+(10m+1)(s_j+s_{j-1}+s_{j-2})
 -(j+6m)s_{j-3}=0.}
 \tag{2.2}
$$



Equation (2.2) is an exact all-(m) recurrence for the actual kernel.  It is
not, by itself, a nonvanishing theorem: a pair of terminal zeros leaves a
two-dimensional local state.  Consequently recurrence existence or a
finite initial scan cannot be credited as support exclusion.

## 3. Phase-independent collapse of the (R) pair

Put (N=4m), (t=n/2), and use generalized binomial coefficients over
(\mathbb Q).  Define



$$
\begin{aligned}
 E_m&=\sum_{j=0}^{3m}(-1)^j\binom{6m}{2j}
 \binom{m-\tfrac12-j}{4m},\\
 O_m&=\sum_{j=0}^{3m-1}(-1)^j\binom{6m}{2j+1}
 \binom{m-\tfrac32-j}{4m}.
\end{aligned}
\tag{3.1}
$$



**Theorem 3.1.**  For every compatible prime in Section 1,



$$
\boxed{
 [z^n]R_m\equiv(-1)^tE_m,
 \qquad
 [z^{n-1}]R_m\equiv(-1)^tO_m\pmod p.}
 \tag{3.2}
$$



**Proof.**  Expanding the denominator gives



$$
[z^{2u}](1+z^2)^{-k}=(-1)^u\binom{k+u-1}{k-1}.
$$



For the even coefficient (n=2t), put the numerator degree equal to
(2j).  Since (t=(p-6m-1)/2),



$$
k+t-j-1\equiv m-\tfrac12-j\pmod p.
$$



The lower binomial index is (k-1=4m<p), so the binomial is a polynomial
in its upper argument over (\mathbb F_p).  This gives the first congruence.
For degree (n-1), use numerator degree (2j+1); the same computation gives
upper argument (m-\tfrac32-j) and the second congruence.  All rational
denominators are (p)-units because (p>6m).  $\square$

Let (\nu(x)) denote the numerator of a reduced rational number (x), and
define



$$
\boxed{W_m=\gcd\bigl(|\nu(E_m)|,|\nu(O_m)|\bigr).}
 \tag{3.3}
$$



Whenever ((E_m,O_m)\ne(0,0)), this is a positive integer.  Theorem 3.1
proves the actual-family carrier implication



$$
\boxed{p\mid H_q\Longrightarrow p\mid W_m.}
 \tag{3.4}
$$



No prime or factorization choice enters the definition of (W_m).

## 4. Two phase scalars for the (S) pair

Because (n) is even, put



$$
\delta\equiv n\pmod4,
 \qquad \delta\in\{0,2\}.
$$



Define



$$
\begin{aligned}
 U_{m,\delta}
 &=\sum_{\substack{0\le a\le10m+1\\a\equiv\delta\ (4)}}
 (-1)^a\binom{10m+1}{a}
 \binom{(10m-1-a)/4}{4m},\\
 V_{m,\delta}
 &=\sum_{\substack{0\le a\le10m+1\\a\equiv\delta-1\ (4)}}
 (-1)^a\binom{10m+1}{a}
 \binom{(10m-2-a)/4}{4m}.
\end{aligned}
\tag{4.1}
$$



Expanding ((1-z^4)^{-k}), and again using that a binomial with lower
index (4m<p) is polynomial in its upper argument, proves



$$
\boxed{
 [z^n]S_m\equiv U_{m,\delta},
 \qquad
 [z^{n-1}]S_m\equiv V_{m,\delta}\pmod p.}
 \tag{4.2}
$$



Thus the exact phase carrier is



$$
\boxed{
 J_{m,\delta}=\gcd\bigl(
 |\nu(E_m)|,|\nu(O_m)|,
 |\nu(U_{m,\delta})|,|\nu(V_{m,\delta})|
 \bigr),}
 \tag{4.3}
$$



and the complete Item-406 equivalence becomes



$$
\boxed{p\mid H_q\Longrightarrow p\mid J_{m,\delta}\mid W_m.}
 \tag{4.4}
$$



Equations (3.1) and (4.1) are characteristic-zero rational definitions;
equations (3.2) and (4.2) are uniform compatible-prime theorems.  They are
not extrapolated from the replay rows.

## 5. Rigorous weighted-mass consequence and its limitation

Let



$$
\mathcal P_H(m)=\{p>6m:p\text{ prime and }p\mid H_{p-6m}\}.
$$



For (m) with ((E_m,O_m)\ne(0,0)), (3.4) gives



$$
\boxed{
 \sum_{p\in\mathcal P_H(m)}\log p
 \le\log\operatorname{rad}W_m
 \le\log W_m.}
 \tag{5.1}
$$



This is a genuine weighted-support theorem for the actual family.  It does
not assert that the right side is (o(m)).

There is also an explicit elementary height bound.  Every half-integral
binomial in (3.1) has denominator dividing



$$
2^{N+v_2(N!)}<2^{2N}=2^{8m}.
$$



For every term in (3.1), the (4m) numerator factors have absolute value
below (6m), while the sum of the relevant ordinary binomial coefficients
is at most (2^{6m}).  Therefore



$$
\boxed{
 |\nu(E_m)|,|\nu(O_m)|
 \le
 2^{14m}\frac{(6m)^{4m}}{(4m)!}.}
 \tag{5.2}
$$



Using ((4m)!\ge(4m/e)^{4m}), this gives



$$
\limsup_{m\to\infty}\frac{\log W_m}{6m}
 \le
 \frac{14\log2+4\log(3e/2)}6
 =2.55\ldots .
 \tag{5.3}

The bound is finite and linear, but it is worse than the inherited
((\log136)/6) ceiling.  It neither proves zero weighted density nor
reduces a live capacity.  The exceptional possibility

\[
 \mathcal E_R=\{m:E_m=O_m=0\}
$$



is also not excluded uniformly here.  The replay finds no member through
(m=128), but that is finite evidence only.

The smallest useful arithmetic target exposed by this item is



$$
\boxed{
 \log\operatorname{rad}W_m=o(m),}
 \tag{5.4}
$$



or, more strongly and with the full phase information,



$$
\boxed{
 \operatorname{rad}J_{m,\delta}\mid(6m)!
 \quad(\delta=0,2).}
 \tag{5.5}
$$



Statement (5.5) would make (4.4) impossible because (p>6m), proving the
four-adjacent lemma.  Neither (5.4) nor (5.5) is proved.

## 6. Exact finite evidence and rejected strengthenings

The deterministic replay checks every (1\le m\le128).  In that declared
finite range it finds:

1. (E_m) and (O_m) are not both zero;
2. (J_{m,0}=J_{m,2});
3. after removing every prime at most (6m), both phase carriers have
   residual (1), i.e. the finite analogue of (5.5);
4. selected compatible primes in both phases satisfy all four uniform
   scalar congruences and recurrence (2.2).

The replay also records counterexamples to two stronger finite patterns.

* (W_m\mid\binom{6m}{2m}) already fails at (m=33,34,59,\ldots).
* (J_{m,\delta}\mid\binom{6m}{2m}) fails at (m=109) and (m=122),
  although only excess powers of primes at most (6m) occur there.

These counterexamples are normalization facts, not asymptotic theorems.
They prevent multiplicity claims from being inferred from the surviving
radical-support census.

## 7. Strict labels

### PROVED

* The exact simplification (2.1) and all-(m) recurrence (2.2).
* The uniform compatible-prime scalar collapses (3.2) and (4.2).
* The prime-independent carriers (W_m,J_{m,\delta}) and implication
  (4.4) for the actual family.
* The weighted carrier inequality (5.1), conditional only on the explicitly
  stated non-identically-resonant value of (m).
* The explicit height bound (5.2) and zero booking.

### EXACT FINITE ONLY

* The (m\le128) nonzero census, phase equality, and radical support in
  primes at most (6m).
* The declared counterexamples to the two stronger binomial divisibilities.
* Selected compatible-prime rows used only to normalize the uniform
  formulas.

### OPEN

* Uniform exclusion of (E_m=O_m=0).
* The zero-rate bound (5.4).
* The all-(m) phase support theorem (5.5).
* The four-adjacent lemma, compatible support of (H_q), primitive
  (G_q^{\rm prim}) support, and (H_qG_q^{\rm prim}\mid P_q).
* Any positive Route-1 booking, Route-1 closure, or irrationality conclusion
  for (e+\pi).

### BOOKING



$$
\boxed{
 \Delta r_{\rm booked}=0,
 \qquad
 \Delta C_{\rm total}^{\rm proved}=0.}
$$



No canonical, master, status, checkpoint, or research-log file is edited by
this work package.

## 8. Replay

From the archive root run:

```text
python work/item410_mixed_cubic_compatible_scalar_carrier_certificate.py \
  --output work/item410_mixed_cubic_compatible_scalar_carrier_certificate.replay.json
```

The checker uses only the Python standard library and exact integer/rational
arithmetic.  It verifies the pinned dependencies, the exact scalar formulas,
the recurrence, selected compatible normalization rows, the declared
(m\le128) finite census, and the two finite multiplicity counterexamples.

