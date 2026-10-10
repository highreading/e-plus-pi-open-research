> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 311 OPEN checkpoint — the actual-seed multiplier reduction

Checked: 2026-08-31 (Beijing time)

## 1. Strict verdict

Let



$$
q_0=q_1=1,\qquad p_0=1,\quad p_1=3,
$$



and, for $n\ge2$,



$$
q_n=(4n-2)q_{n-1}+q_{n-2},\qquad
p_n=(4n-2)p_{n-1}+p_{n-2}.                    \tag{1.1}
$$



Put



$$
A=4n-2,\qquad a=q_{n-1},\quad b=q_n,\quad c=q_{n-2},
\qquad b=Aa+c,                                      \tag{1.2}
$$



and let



$$
\kappa=\operatorname{nint}(a^2/b),\qquad
r=a^2-\kappa b,\qquad R=|r|.                       \tag{1.3}
$$



This checkpoint proves an exact reduction but **does not** prove the
centered half-bound $R\ge a/2$, the smaller bound $R\ge a/(2c)$,
or a counterexample.

For $n\ge5$, the actual small-window event is equivalent to one explicit
continuant divisibility condition:



$$
\boxed{
R<\frac{a}{2c}
\iff
\exists\,1\le k<n-2:\quad
\widehat D_k\mid a
\quad\hbox{and}\quad
\widehat D_k>2cQ_k.}                               \tag{1.4}
$$



Every divisor branch in (1.4) would have



$$
n+k\equiv0\pmod2,\qquad r>0,\qquad R\ \hbox{odd},
\qquad \kappa\ \hbox{even}.                       \tag{1.5}
$$



The exact missing lemma is



$$
\boxed{
\widehat D_k>2cQ_k
\Longrightarrow
\widehat D_k\nmid a.}                              \tag{1.6}
$$



It remains **OPEN**.  Therefore Item 311 is an OPEN checkpoint, not a
theorem-level beta closure.  Booking is zero:



$$
\boxed{
\text{new Route-1 rate}=0,\qquad
\text{new beta capacity reduction}=0.}              \tag{1.7}
$$



## 2. Independent Padé/continuant identity

Use



$$
K(\varnothing)=1,\qquad
K(z_1,\ldots,z_j)
=z_jK(z_1,\ldots,z_{j-1})+K(z_1,\ldots,z_{j-2}).    \tag{2.1}
$$



For $n\ge2$, define



$$
S_n=K(10,14,\ldots,4n-2),                           \tag{2.2}
$$



where the word is empty at $n=2$.  Thus



$$
S_2=1,\qquad S_3=10,
$$



and appending the terminal coefficient gives



$$
S_n=(4n-2)S_{n-1}+S_{n-2}\qquad(n\ge4).            \tag{2.3}
$$



The sequence



$$
L_n=\frac{3q_n-p_n}{2}                              \tag{2.4}
$$



has the same recurrence, and $L_2=1,L_3=10$.  Hence, independently
of a finite fit,



$$
\boxed{S_n=\frac{3q_n-p_n}{2}\qquad(n\ge2).}        \tag{2.5}
$$



In particular, the Item-292 Padé numerator is not extra numerical data:
it is exactly the complementary-tail coordinate



$$
p_n=3q_n-2S_n.                                      \tag{2.6}
$$



The adjacent Wronskian from Item 292 becomes



$$
\boxed{q_{n-1}S_n-q_nS_{n-1}=(-1)^n.}               \tag{2.7}
$$



This proves both the sign and the modular-inverse orientation used below.

## 3. Exact indices and tails

For $n\ge5$, put



$$
m=n-2,\qquad
w_1=7,\qquad w_j=4j+2\quad(2\le j\le m).            \tag{3.1}
$$



Then



$$
a=K(w_1,\ldots,w_m),\qquad
c=K(w_1,\ldots,w_{m-1}),                            \tag{3.2}
$$



and $b=K(w_1,\ldots,w_m,A)$.  For $1\le k<m$, set



$$
Q_k=K(w_1,\ldots,w_k),\qquad
P_k=K(w_2,\ldots,w_k),                              \tag{3.3}
$$





$$
D_k=K(w_{k+2},\ldots,w_m),\qquad
\widehat D_k=K(w_{k+2},\ldots,w_m,A).               \tag{3.4}
$$



The empty word in $D_{m-1}$ has value $1$.  Every displayed
continuant is positive.  The index range excludes the terminal convergent
and contains no negative-index convention.

Euler's identity for the word ending at $a$ is



$$
Q_kS_{n-1}-P_ka=(-1)^kD_k.                          \tag{3.5}
$$



For the word with $A$ appended, it is



$$
Q_kS_n-P_kb=(-1)^k\widehat D_k.                     \tag{3.6}
$$



Since $Q_k=q_{k+1}$ and, by (2.5),



$$
P_k=\frac{3q_{k+1}-p_{k+1}}2,
$$



equation (3.6) is the exact Padé cross-determinant



$$
\boxed{
p_{k+1}b-q_{k+1}p_n
=2(-1)^k\widehat D_k.}                              \tag{3.7}
$$



Thus the actual Bessel/Padé pair and the complementary continuant give
the same arithmetic coordinate; (3.7) is not a fitted identity.

## 4. The appended-tail bridge

Taking the determinant of the two continuant products, or combining
(2.7), (3.5), and (3.6), gives



$$
\boxed{
bD_k+(-1)^{n+k}Q_k=a\widehat D_k.}                  \tag{4.1}
$$



This is the valid identity that retains the actual terminal coefficient
$A$.  It is the key new coordinate for the multiplier branch.

There are no sign ambiguities in (4.1): the Item-305 compatible sign is
$(-1)^k$, while the signed centered residue has sign
$(-1)^{n+k}$.

## 5. Necessity in the small window

For $n\ge5$, $a,b,c$ are odd and adjacent terms are coprime.
Consequently nearest integers are unique and $r\ne0$.  Direct recurrence
inequalities give



$$
0<\kappa<c.                                         \tag{5.1}
$$



Indeed, with $d=q_{n-3}$ one has
$a=(A-4)c+d$, $0<d<c$, and



$$
\frac{a^2}{b}<\frac aA
=c-\frac{4c-d}{A}<c-\frac12.
$$



The last inequality follows from $4c-d>3c$ and $6c>A$ for
$n\ge5$.  Also $b<(A+1)a$ and $a>A+1$, so
$a^2/b>a/(A+1)>1/2$.  Unique rounding now proves (5.1).

Suppose



$$
R<\frac a{2c}.                                      \tag{5.2}
$$



Reducing $r=a^2-\kappa b$ modulo $a$, and using



$$
cS_{n-1}\equiv(-1)^{n-1}\pmod a,
$$



gives



$$
\kappa\equiv(-1)^n rS_{n-1}\pmod a.               \tag{5.3}
$$



Item 305's exact Legendre classification therefore supplies a unique
$k$ and an integer $g\ge1$ such that



$$
R=gQ_k,\qquad
\kappa=gD_k,\qquad
\operatorname{sgn}(r)=(-1)^{n+k}.                  \tag{5.4}
$$



Substituting (5.4) into the actual square equation and using (4.1),



$$
\begin{aligned}
a^2
&=\kappa b+r\\
&=g\bigl(bD_k+(-1)^{n+k}Q_k\bigr)\\
&=ga\widehat D_k.
\end{aligned}                                       \tag{5.5}
$$



Since $a>0$,



$$
\boxed{a=g\widehat D_k.}                            \tag{5.6}
$$



In particular, $\widehat D_k\mid a$.  Also, (5.2), (5.4), and
(5.6) give



$$
gQ_k<\frac{g\widehat D_k}{2c},
$$



so



$$
\boxed{\widehat D_k>2cQ_k.}                         \tag{5.7}
$$



This proves the forward implication in (1.4).

## 6. Sufficiency and exact parity consequences

Conversely, suppose that some $k$ satisfies



$$
\widehat D_k\mid a,qquad
\widehat D_k>2cQ_k.                                 \tag{6.1}
$$



Write $g=a/\widehat D_k$.  Multiplying (4.1) by $g$ yields



$$
a^2=gD_kb+(-1)^{n+k}gQ_k.                           \tag{6.2}
$$



The size condition gives



$$
0<gQ_k<\frac a{2c}<\frac b2.                        \tag{6.3}
$$



Therefore the last term of (6.2) is already the unique centered
representative modulo $b$.  Thus



$$
\kappa=gD_k,qquad
r=(-1)^{n+k}gQ_k,qquad
R=gQ_k<\frac a{2c}.                                 \tag{6.4}
$$



This proves the reverse implication in (1.4).

All coefficients in $\widehat D_k$ are even.  Its word length is
$m-k$.  A continuant of even entries is odd exactly when its length is
even.  Since $a$ is odd and $\widehat D_k\mid a$, one must have



$$
m-k\equiv0\pmod2,qquad n+k\equiv0\pmod2.          \tag{6.5}
$$



Hence the sign in (6.4) is positive.  The tail $D_k$ has the opposite
parity length and is even, whereas $g,Q_k$ are odd.  This proves (1.5).

These parity constraints are exact, but they do not prove (1.6).

## 7. Quarantine of the false split

The following tempting identity is **false**:



$$
a-Q_k\widehat D_k
\stackrel{\rm false}{=}
(Q_{k+1}-AQ_k)D_k.                                  \tag{7.1}
$$



The error is a first-tail/last-tail substitution.  The correct split of
$a$ uses



$$
F_k=K(w_{k+3},\ldots,w_m)
$$



through



$$
a=Q_{k+1}D_k+Q_kF_k,                                \tag{7.2}
$$



whereas appending $A$ uses



$$
E_k=K(w_{k+2},\ldots,w_{m-1})
$$



through



$$
\widehat D_k=AD_k+E_k.                              \tag{7.3}
$$



At the boundary $k=m-1$, both $F_k$ and $E_k$ in these two-step
recurrences are $0$; this is the standard one-step-past-empty
continuant boundary, not a negative-index lookup.  For $k=m-2$, the
corresponding empty continuants have value $1$.

In general $F_k\ne E_k$.

An exact counterexample to (7.1) is $n=9,k=1$:



$$
\begin{gathered}
a=312129649,\quad Q_1=7,\quad Q_2=71,\\
D_1=4365570,\quad \widehat D_1=148574713,
\end{gathered}
$$



for which



$$
a-Q_1\widehat D_1=-727893342
$$



but



$$
(Q_2-34Q_1)D_1=-729050190.                          \tag{7.4}
$$



No divisibility conclusion in this checkpoint uses (7.1).

## 8. Denominator, sign, and base audit

There are no analytic or meromorphic poles in this argument.  Every
division has a positive integer denominator:

* $a,b,c,Q_k,D_k,\widehat D_k>0$;
* $R>0$, because $b\mid a^2$ is impossible when $b>1$ and
  $\gcd(a,b)=1$;
* the nearest integer in (1.3) is unique because $b$ is odd;
* division by $\widehat D_k$ occurs only under the explicit hypothesis
  $\widehat D_k\mid a$;
* the Item-305 range is exactly $n\ge5$, $m=n-2$,
  $1\le k<m$.

The smaller indices are exact:



$$
\begin{array}{c|ccccc}
n&a&b&c&\kappa&r\\ \hline
2&1&7&1&0&1\\
3&7&71&1&1&-22\\
4&71&1001&7&5&36
\end{array}                                         \tag{8.1}
$$



They contain no exceptional denominator or half-integer tie.

## 9. Exact scope of what remains open

The smallest missing lemma for the **Item-305 Legendre window** is (1.6):



$$
\widehat D_k>2cQ_k\Longrightarrow\widehat D_k\nmid a.
$$



Proving it would establish only



$$
R\ge\frac a{2c},                                    \tag{9.1}
$$



not the desired



$$
R\ge\frac a2.                                       \tag{9.2}
$$



The exact intermediate region



$$
\boxed{
\frac a{2c}\le R<\frac a2}                         \tag{9.3}
$$



is outside the Legendre classification used here.  Therefore even a future
proof of (1.6) would need an additional modular-square or Ostrowski bridge to
settle the centered half-bound.

No global no-go for every multiplier/nearest-quotient method is proved.
No proper de-overlapped target theorem follows, and the Item-282 product
baseline remains separate.

## 10. Strict labels

### PROVED

* The all-$n$ companion-tail identity (2.5), by recurrence and exact
  initial values.
* The Padé cross-determinant (3.7).
* The appended-tail bridge (4.1), with exact sign and index orientation.
* The exact small-window divisor equivalence (1.4).
* The parity consequences (1.5).
* The exact small bases (8.1).
* The counterexample (7.4) to the quarantined false split.

### EXACT FINITE ONLY

* The deterministic checker replays bounded instances of the recurrence,
  continuant, Padé, centering, parity, and quarantine identities.
* It performs no half-bound scan, divisibility search, counterexample search,
  or finite-fit extrapolation.

### OPEN

* The divisibility implication (1.6).
* The lower bound $R\ge a/(2c)$.
* The centered half-bound $R\ge a/2$.
* The intermediate region (9.3).
* A seed-specific modular-square or Ostrowski invariant beyond the
  Legendre window.
* Proper-target transfer, the Item-282 product baseline, Route 1, and every
  conclusion about $e+\pi$.

### BOOKING



$$
\boxed{
\text{new Route-1 rate}=0,\qquad
\text{new beta capacity reduction}=0.}              \tag{10.1}
$$



## 11. Deterministic replay

From the archive root:

~~~text
python scripts/item311_beta_seed_multiplier_open_checkpoint.py ^
  --output results/item311_beta_seed_multiplier_open_checkpoint_replay.json
~~~

The checker uses only the Python standard library and exact integer
arithmetic.  Its bounded rows are control rows only and are never promoted.
