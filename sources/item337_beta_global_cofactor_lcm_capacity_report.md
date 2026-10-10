> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 337 — the global beta cofactor tower and its primitive LCM capacity

Checked: 2026-09-01 (Beijing time)

## 1. Strict verdict

Retain



$$
q_0=q_1=1,
\qquad
q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\ge2),
\tag{1.1}
$$



and, for $n\ge5$, put



$$
A=4n-2,
\qquad
a=q_{n-1},\quad b=q_n,\quad c=q_{n-2},
\qquad m=n-2.
\tag{1.2}
$$



For an Item-316 canonical word, let



$$
\epsilon=(-1)^n\operatorname{sgn}(E_m),
\tag{1.3}
$$



and retain Item 335's exact adjacent load cofactors



$$
\boxed{
\mathfrak z_j
=(1+w_jw_{j-1})J_{j-2}-w_jJ_{j-3}-J_j
=\epsilon(\delta_j-w_j\delta_{j-1})
\quad(3\le j\le m).}
\tag{1.4}
$$



Item 335 proves that every fixed number of these cofactors has zero beta
rate.  Item 337 makes the requested growing-depth decision.

The depthwise product is not the overlap-normalized reservoir.  The exact
primitive tower is



$$
\boxed{
\Lambda(\delta)
=\operatorname{lcm}_{\substack{3\le j\le m\\
\mathfrak z_j\ne0}}
|\mathfrak z_j|,}
\tag{1.5}
$$



with the empty lcm declared to be one.  For every declared de-overlapped
target $Q\mid b$, the total prime-power mass available from the tower is
exactly



$$
\boxed{
\Gamma_Q(\delta)
=\log\gcd(Q,\Lambda(\delta))
=\sum_p
\min\!\left{
v_p(Q),
\max_{3\le j\le m}v_p(\mathfrak z_j)
\right}\log p.}
\tag{1.6}
$$



Equation (1.6) removes both compulsory sources of overcounting:

1. repeated occurrences of the same prime power at different depths are
   replaced by one maximum valuation; and
2. already-booked denominator content can be removed before the calculation
   by choosing the corresponding de-overlapped divisor $Q$.

The global height theorem is



$$
\boxed{
\log\Lambda(\delta)
\le(2+o(1))\log b,}
\tag{1.7}
$$



for every canonical word, while the actual captured mass satisfies the
stronger one-target ceiling



$$
\boxed{
0\le\Gamma_Q(\delta)
\le\log Q\le\log b.}
\tag{1.8}
$$



Thus the entire tower can never create more than one fresh copy of a single
declared target.  Counting the product as two independent beta copies is
invalid.

The tower is nevertheless **not** globally low-height after cross-depth
overlap is removed.  There is an explicit canonical family in the exact
intermediate half-window for which



$$
\boxed{
\log\Lambda(\delta)
\ge\left(\frac12+o(1)\right)\log b.}
\tag{1.9}
$$



The proof uses the irreducible quadratic subsequence



$$
|\mathfrak z_{2r}|=32r^2-3
\tag{1.10}
$$



and the published quadratic-LCM theorem of Javier Cilleruelo.  That theorem
states that for every irreducible quadratic $f\in\mathbb Z[x]$,



$$
\log\operatorname{lcm}\{f(1),\ldots,f(N)\}
=N\log N+O_f(N).
\tag{1.11}
$$



See [Cilleruelo, *The least common multiple of a quadratic sequence*](https://arxiv.org/abs/1001.3438).

Consequently the global cofactor tower survives the raw capacity screen with
positive linear beta-scale height.  Item 335's fixed-complexity no-go cannot
be extrapolated to growing depth.

The family proving (1.9) is **not** promoted to an actual Item-316 target: it
is canonical and lies in the exact intermediate $R$-window, but no
small-error condition or $\Delta=0$ equality is asserted.  Therefore the
actual target-specific overlap



$$
\Gamma_Q(\delta_{\rm target})
\tag{1.12}
$$



remains open and unbooked.  The first genuinely bulk invariant has been
isolated, but no positive mass for the actual collision is proved.

## 2. Exact removal of cross-depth overlap

For a prime $p$, the depthwise product would contain the valuation



$$
\sum_{j=3}^{m}v_p(\mathfrak z_j).
\tag{2.1}
$$



This counts the same available $p$-power repeatedly.  A single target
$Q$ can use at most



$$
\min\!\left{v_p(Q),\max_jv_p(\mathfrak z_j)\right}.
\tag{2.2}
$$



By the defining prime factorization of an lcm,



$$
v_p(\Lambda)=\max_jv_p(\mathfrak z_j),
\tag{2.3}
$$



where zero rows are omitted.  Summing (2.2) over the primes proves (1.6).
No coprimality assumption between depths is made.

If the current ledger has already removed a deterministic reservoir
$D\mid b$, take



$$
Q\mid\frac{b}{\gcd(b,D)}.
\tag{2.4}
$$



Then (1.6) measures only overlap with the declared remainder.  Any further
compulsory factor removed from the cofactor side can only replace
$\Lambda$ by a divisor and decrease $\Gamma_Q$.

For an actual Item-316 target, Item 335 proves that at least one cofactor is
nonzero.  Hence its $\Lambda$ is a positive integer.  No convention about
the lcm of an empty set enters the actual-family theorem.

## 3. Universal product and continuant upper bound

Every canonical digit satisfies



$$
0\le\delta_j\le w_j.
\tag{3.1}
$$



For $j\ge3$, one has $w_{j-1}\ge10$.  If
$\delta_{j-1}=0$, then



$$
|\mathfrak z_j|=\delta_j\le w_j\le w_jw_{j-1}.
\tag{3.2}
$$



If $\delta_{j-1}\ge1$, the Markov condition excludes
$\delta_j=w_j$ unless $\delta_{j-1}=0$, and directly



$$
|\mathfrak z_j|
=w_j\delta_{j-1}-\delta_j
\le w_jw_{j-1}.
\tag{3.3}
$$



Therefore



$$
\Lambda
\le\prod_{\substack{3\le j\le m\\\mathfrak z_j\ne0}}
|\mathfrak z_j|
\le\prod_{j=3}^{m}w_jw_{j-1}.
\tag{3.4}
$$



Put



$$
W_m=\prod_{j=1}^{m}w_j.
\tag{3.5}
$$



The last product in (3.4) is exact:



$$
\prod_{j=3}^{m}w_jw_{j-1}
=\frac{W_m^2}{w_1^2w_2w_m}.
\tag{3.6}
$$



The continuant $Q_m=a$ differs from $W_m$ by only a bounded factor.
Indeed,



$$
\frac{Q_j}{w_jQ_{j-1}}
=1+\frac{Q_{j-2}}{w_jQ_{j-1}}
<1+\frac1{w_jw_{j-1}},
\tag{3.7}
$$



and



$$
\sum_{j=2}^{\infty}\frac1{w_jw_{j-1}}
<\sum_{j=2}^{\infty}\frac1{8j^2}
<\frac18.
\tag{3.8}
$$



Iterating (3.7) gives



$$
\boxed{W_m\le a<e^{1/8}W_m.}
\tag{3.9}
$$



Since



$$
Aa<b<(A+1)a,
\tag{3.10}
$$



one has



$$
\log b=\log a+\log A+O(1/A).
\tag{3.11}
$$



Combining (3.4), (3.6), (3.9), and $w_m=A-4$,



$$
\log\Lambda
\le2\log a-\log w_m+O(1)
=2\log b-3\log A+O(1).
\tag{3.12}
$$



This proves (1.7).  Equation (1.8) then follows directly from
$\gcd(Q,\Lambda)\mid Q$.

The distinction is important:



$$
\begin{array}{c|c}
\text{quantity}&\text{universal beta-scale ceiling}\\ \hline
\log\prod_j|\mathfrak z_j|&2\log b+o(\log b)\\
\log\Lambda&2\log b+o(\log b)\\
\Gamma_Q&\log Q\le\log b.
\end{array}
\tag{3.13}
$$



Only the final row is a capacity for one de-overlapped target.

## 4. A canonical family with linear primitive LCM height

For each $m\ge3$, define a canonical digit word as follows:



$$
\delta_1=3,
\tag{4.1}
$$



and, for $2\le j\le m$, initially put



$$
\delta_j=
\begin{cases}
1,&j\text{ even},\\
w_j/2,&j\text{ odd}.
\end{cases}
\tag{4.2}
$$



If $m$ is odd, replace only the top digit by



$$
\delta_m=w_m/2-1.
\tag{4.3}
$$



Every digit lies strictly below its maximum, so the Markov implications are
vacuous.  The top digit is strictly below $w_m/2$, and hence the exact
half-language gives



$$
R<\frac a2.
\tag{4.4}
$$



Also $\delta_m\ge1$, so $R\ge c$.  Since



$$
a<Ac,
\qquad
c>A/2\quad(n\ge5),
\tag{4.5}
$$



one has



$$
R\ge c>\frac{a}{2c}.
\tag{4.6}
$$



Thus the family lies in the exact intermediate $R$-window of Item 316.

Take $\epsilon=1$; absolute values make this choice immaterial.  For every
even $j=2r$ with $4\le j\le m$, (4.2) gives



$$
\begin{aligned}
|\mathfrak z_j|
&=w_j\frac{w_{j-1}}2-1\\
&=8j^2-3\\
&=32r^2-3.
\end{aligned}
\tag{4.7}
$$



The top correction (4.3) occurs only when $m$ is odd and therefore never
changes the even-index subsequence in (4.7).

Let



$$
N=\left\lfloor\frac m2\right\rfloor.
\tag{4.8}
$$



The polynomial



$$
f(r)=32r^2-3
\tag{4.9}
$$



is irreducible over $\mathbb Z$, because its discriminant $384$ is not a
square.  Cilleruelo's theorem gives



$$
\log\operatorname{lcm}_{2\le r\le N}(32r^2-3)
=N\log N+O(N).
\tag{4.10}
$$



This lcm divides $\Lambda(\delta)$.  Since $m=n-2$ and
$\log b=n\log n+O(n)$,



$$
\log\Lambda(\delta)
\ge\left(\frac12+o(1)\right)\log b.
\tag{4.11}
$$



This lower bound already uses an lcm, not a product.  Repeated primes and
prime powers across the quadratic values have been removed by the theorem
itself.

The polynomial $32r^2-3$ is primitive and has no fixed prime divisor.
Hence (4.11) is not produced by one compulsory scalar common to every depth.

## 5. Actual target versus ambient capacity

The exact actual-family implication remains



$$
\text{half-bound failure}
\Longrightarrow
\text{Item-316 canonical word with }\Delta=0
\Longrightarrow
\Lambda(\delta_{\rm target}).
\tag{5.1}
$$



For that word and every declared de-overlapped $Q\mid b$, (1.6) is an exact
identity.  No ambient polynomial space is used in defining the actual
candidate.

The witness family in Section 4 has a different logical role.  It proves



$$
\boxed{
\text{canonicality + the exact intermediate }R\text{-window}
\not\Longrightarrow
\log\Lambda=o(\log b).}
\tag{5.2}
$$



It does **not** prove that the Item-316 small-error condition, the exact
appended equality, or an actual beta collision is compatible with (4.11).
Those are precisely the remaining orbit-specific inputs.

Accordingly, Item 337 makes the following capacity decision.

> **PROVED — FIRST BULK INVARIANT SURVIVES RAW ADMISSION.**  The
> overlap-normalized growing-depth lcm $\Lambda$ can have positive linear
> beta-scale height even on canonical words in the exact intermediate
> window.  Therefore no global zero-rate theorem follows from digit height,
> Markov admissibility, half-language, or cross-depth overlap alone.

> **OPEN — ACTUAL OVERLAP.**  For the hypothetical Item-316 target word,
> determine
>
> 

$$
> \Gamma_Q
> =\log\gcd(Q,\Lambda(\delta_{\rm target})).
> \tag{5.3}
>
$$


>
> No positive lower bound, strict fractional upper bound below $\log Q$,
> or little-oh theorem is proved here.

Thus $\Lambda$, not one more local $\mathfrak z_j$, is the next admitted
cofactor object.  Any continuation must attack its target-specific shared
prime distribution.

## 6. Builder and Closer thresholds

The Closer target is



$$
\boxed{
\Gamma_Q(\delta_{\rm target})=o(\log b).}
\tag{6.1}
$$



A strict fractional theorem



$$
\Gamma_Q\le(1-\eta)\log Q+o(\log b)
\tag{6.2}
$$



for some fixed $\eta>0$ would also be meaningful if the master ledger
shows that the removed fraction changes the Route-1 decision.

The Builder target is an actual-family lower bound



$$
\boxed{
\Gamma_Q(\delta_{\rm target})\ge\eta\log b}
\tag{6.3}
$$



for a declared $\eta>0$, after every old denominator factor has been
removed.  Ambient lower bounds for $\Lambda$ do not satisfy (6.3).

Potential tools must therefore couple the actual target equation to the
prime divisors of the lcm.  Examples include a moving-depth resultant,
large-sieve control of the digit-transition values, or a canonical
redigitization only if it is forced by the actual collision.  Increasing the
number of independently booked local cofactors is forbidden by (1.6).

## 7. Strict labels

### PROVED

* The exact overlap-normalized tower $\Lambda$ and captured-mass identity
  (1.6).
* Exact removal of repeated cross-depth prime powers by maximum valuation.
* The universal continuant/product upper bound (3.12).
* The one-target ceiling $\Gamma_Q\le\log Q$.
* The explicit canonical intermediate-window family (4.1)-(4.6).
* The exact quadratic subsequence $|\mathfrak z_{2r}|=32r^2-3$.
* Using Cilleruelo's published theorem, the positive-linear lcm lower bound
  (4.11).
* The actual-family and admission distinctions in Section 5.

### PROVED CAPACITY DECISION

* The full growing-depth cofactor tower is not zero rate by canonical height
  or cross-depth overlap alone.
* The primitive lcm $\Lambda$ is the first bulk invariant that survives raw
  capacity admission.
* A single target can use at most one copy, measured exactly by $\Gamma_Q$;
  the apparent two-copy product ceiling cannot be booked.

### EXACT FINITE ONLY

* The deterministic replay's declared canonical witness rows, lcm/product
  identities, quadratic subsequences, and finite ratios.
* The replay checks the input to Cilleruelo's theorem; it does not claim to
  re-prove that asymptotic theorem from bounded data.

### OPEN

* The original all-digit exclusion and centered half-bound.
* The size of $\Lambda$ under the full Item-316 small-error and
  $\Delta=0$ conditions.
* The actual shared mass $\Gamma_Q$, including any little-oh, strict
  fraction, or positive lower bound.
* Removal of every declared old reservoir from an actual target family.
* A proper-target residue lower bound, weighted zero-density theorem, or beta
  capacity reduction.
* Route 1 and every conclusion about $e+\pi$.

### BOOKING



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new Route-1 rate}=0.}
\tag{7.1}
$$



The raw invariant passes admission, but actual-family mass is unproved and
cannot be booked.

No canonical, master, status, checkpoint, or research-log file is edited by
this work package.

## 8. Deterministic replay

From the archive root:

~~~text
python work/item337_beta_global_cofactor_lcm_capacity_certificate.py ^
  --output work/item337_beta_global_cofactor_lcm_capacity_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer
arithmetic.  It performs no actual-target scan and promotes no bounded row.
