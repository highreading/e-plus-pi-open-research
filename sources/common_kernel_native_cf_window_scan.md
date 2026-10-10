> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Native factorial windows and the continued fraction of $e+\pi$

Checked: 2026-08-27 UTC.

## 1. Verdict

Write



$$
s=e+\pi,\qquad X_N=N!,                              \tag{1}
$$



and retain the notation from the fixed-index output-closure theorem:



$$
{\cal L}^{\min}_N<{\cal L}_N(G)<{\cal L}^{0}_N.     \tag{2}
$$



Throughout, $P/Q$ means a reduced fraction with $Q>0$.  A genuine
reduced rational approximation $P/Q$ occurs at index $N$ precisely when



$$
s-\frac{{\cal L}^{0}_N}{X_N}
 <\frac PQ<
 s-\frac{{\cal L}^{\min}_N}{X_N},\qquad
 Q\leq\sqrt{X_N}.                                    \tag{3}
$$



This note gives three rigorous results.

First, along the native admissible indices,



$$
\begin{aligned}
 {\cal L}^{0}_N
 &=\frac5N-\frac4{N^2}-\frac5{N^3}
   +\frac{45}{N^4}+O(N^{-5}),\\
 {\cal L}^{\min}_N
 &=\left(1+\frac2e\right)
   \left(\frac1N-\frac1{N^3}+\frac1{N^4}
   +O(N^{-5})\right),\\
 {\cal L}^{0}_N-{\cal L}^{\min}_N
 &=\frac{4-2/e}{N}-\frac4{N^2}
   +\frac{-4+2/e}{N^3}+O(N^{-4}).                    \tag{4}
 \end{aligned}
$$



Thus both errors in (3) are of exact order $1/(N\,N!)$.

Second, every hit with $N\geq10$ is a *principal continued-fraction
convergent* of $s$; proper semiconvergents are excluded.  Every such hit
must satisfy the sharp universal necessary window



$$
\boxed{
  1<N\,N!\left(s-\frac PQ\right)<5.}                 \tag{5}
$$



Third, an exact fixed-point/continued-fraction exhaustion through $N=2000$
finds only nine convergents in the broad window (5):



$$
25,33,43,86,88,164,331,351,1477.                    \tag{6}
$$



The indices $86,351,1477$ lie respectively in the forbidden native residue
classes $6,7,5\pmod8$, where
$-\operatorname{Im}(1-i)^N<0$.  The remaining six are exactly the six
genuine hits already certified in the hash-pinned fixed-index package:



$$
\boxed{25,33,43,88,164,331.}                         \tag{7}
$$



Consequently there is no new admissible hit for



$$
332\leq N\leq2000.                                  \tag{8}
$$



Statement (8) is a finite theorem, not an extrapolation.  No infinite
recurrence or congruence pattern is proved, and the package proves neither
irrationality nor transcendence of $e+\pi$.

## 2. Sharp endpoint asymptotics

Set $u=1-t$.  Since $v(t)=1+u^2$, the upper output is



$$
{\cal L}^{0}_N
 =\int_0^1t^N\left(e^u+\frac4{1+u^2}\right)dt.       \tag{9}
$$



Put



$$
A_j(N)=\frac{N!}{(N+j+1)!}
 =\int_0^1\frac{t^Nu^j}{j!}\,dt.                    \tag{10}
$$



Taylor expansion at $u=0$, with a uniform remainder on $[0,1]$, gives



$$
\begin{aligned}
 eB_N&=A_0+A_1+A_2+A_3+O(A_4),\\
 {\cal L}^{0}_N&=5A_0+A_1-7A_2+A_3+O(A_4).           \tag{11}
 \end{aligned}
$$



Indeed, the coefficient of $u^2$ in
$e^u+4/(1+u^2)$ is $-7/2$, and
$\int t^Nu^2=2A_2$.  Expanding the four inverse products in (11) yields



$$
\begin{aligned}
 eB_N&=\frac1N-\frac1{N^3}+\frac1{N^4}+O(N^{-5}),\\
 {\cal L}^{0}_N
 &=\frac5N-\frac4{N^2}-\frac5{N^3}
   +\frac{45}{N^4}+O(N^{-5}).                         \tag{12}
 \end{aligned}
$$



For the lower endpoint, recall



$$
E_N(t)=\min\{\mu(t),J(t)\},\qquad
 \mu(\tau_N)=J(\tau_N),                              \tag{13}
$$



and let $\nu_*$ be its limiting density.  It has mass $B_N$ and support
in $[0,\tau_N]$.  The native coefficients satisfy



$$
b=\frac{N!}{2}(1+o(1)),\qquad
 0\leq a\leq2^{N/2}.                                 \tag{14}
$$



The root equation first gives
$\tau_N^2=O(B_N/N!)$.  Hence $\tau_N\to0$, and



$$
\begin{aligned}
 0\leq B_N-J(\tau_N)
 &=\int_0^{\tau_N}e^{-t}t^N\,dt
 \leq\frac{\tau_N^{N+1}}{N+1}=o(B_N),\\
 \frac{a}{\sqrt{bB_N}}&\longrightarrow0.
 \end{aligned}                                       \tag{15}
$$



Thus $J(\tau_N)/B_N\to1$.  On putting
$y_N=\tau_N\sqrt{b/B_N}=O(1)$, the root equation becomes



$$
e^{-\tau_N}\left\{
 \frac{a}{\sqrt{bB_N}}y_N+y_N^2\right\}
 =\frac{J(\tau_N)}{B_N}\longrightarrow1.             \tag{15a}
$$



Since $y_N\geq0$, equation (15a) gives $y_N\to1$.

Substitution back into the root equation proves the sharper formula



$$
\boxed{
 \tau_N\sim\sqrt{\frac{B_N}{b}}
 \sim\sqrt{\frac{2}{eN\,N!}}.}                       \tag{16}
$$



Since $R(0)=e+2$, $R$ is Lipschitz, and $\nu_*$ has mass $B_N$,



$$
0<{\cal L}^{\min}_N-(e+2)B_N=O(B_N\tau_N).          \tag{17}
$$



The right side is smaller than every fixed power of $1/N$.  Combining
(12) and (17) proves (4).  In particular, the two approximation errors in
(3) have the explicit forms



$$
\begin{aligned}
 s-\left(s-\frac{{\cal L}^{0}_N}{N!}\right)
 &=\frac1{N!}\left(\frac5N-\frac4{N^2}
   -\frac5{N^3}+O(N^{-4})\right),\\
 s-\left(s-\frac{{\cal L}^{\min}_N}{N!}\right)
 &=\frac1{N!}\left(1+\frac2e\right)
   \left(\frac1N-\frac1{N^3}+O(N^{-4})\right).
                                                               \tag{18}
 \end{aligned}
$$



## 3. A uniform normalized-error window

The lower comparison from the fixed-index theorem and
$e^{-t}\geq e^{-1}$ give



$$
N{\cal L}^{\min}_N
 >N(e+2)B_N
 \geq\left(1+\frac2e\right)\frac{N}{N+1}>1.          \tag{19}
$$



For the upper endpoint, convexity gives
$e^u\leq1+(e-1)u$ on $[0,1]$, while
$(1+u^2)^{-1}\leq1$.  Therefore



$$
{\cal L}^{0}_N
 \leq\frac5{N+1}
 +\frac{e-1}{(N+1)(N+2)}
 <\frac5N.                                           \tag{20}
$$



Multiplying (3) by $N\,N!$ proves (5).

If the fraction $P/Q$ is reduced and $Q^2\leq N!$, then (20) also gives



$$
0<s-\frac PQ
 <\frac5{N\,N!}
 \leq\frac5{NQ^2}\leq\frac1{2Q^2}\qquad(N\geq10).   \tag{21}
$$



The first inequality in (21) is strict, including when $N=10$.
Legendre's continued-fraction criterion therefore proves that $P/Q$ is a
principal convergent.  This is why a scan over all rationals or all
semiconvergents is unnecessary: the latter cannot meet (3) in this range.

There is another useful rigidity.  Put $Y_N=N\,N!$.  Then



$$
\frac{Y_{N+1}}{Y_N}=\frac{(N+1)^2}{N}>5\qquad(N\geq4). \tag{22}
$$



Consequently a fixed convergent, with fixed positive error
$s-P/Q$, can satisfy the broad window (5) for at most one $N$.

## 4. Exact continued-fraction membership

Assume for this paragraph that $s$ is irrational, and let the reduced
fraction $p_k/q_k<s$ be a below-side principal convergent.  Write



$$
\alpha_{k+1}=[a_{k+1};a_{k+2},\ldots],\qquad
 \theta_k=q_k^2\left(s-\frac{p_k}{q_k}\right),\qquad
 \lambda_{N,k}=\frac{N!}{q_k^2}.                     \tag{23}
$$



The exact convergent-error identity is



$$
\theta_k
 =\frac1{\alpha_{k+1}+q_{k-1}/q_k}.                 \tag{24}
$$



Define



$$
C_N^{\min}=N{\cal L}^{\min}_N,\qquad
 C_N^0=N{\cal L}^{0}_N.                              \tag{25}
$$



Then (3) is exactly equivalent to



$$
q_k^2\leq N!,\qquad
 C_N^{\min}
 <\frac{N\lambda_{N,k}}
 {\alpha_{k+1}+q_{k-1}/q_k}
 <C_N^0.                                              \tag{26}
$$



By (4), the limiting window in (26) is



$$
1+\frac2e+O(N^{-2})
 <N\lambda_{N,k}\theta_k
 <5-\frac4N+O(N^{-2}).                               \tag{27}
$$



Since
$a_{k+1}<\alpha_{k+1}+q_{k-1}/q_k<a_{k+1}+2$, a
necessary integer condition is



$$
\frac{N\lambda_{N,k}}{C_N^0}-2
 <a_{k+1}<
 \frac{N\lambda_{N,k}}{C_N^{\min}}.                 \tag{28}
$$



Thus the phenomenon is a matching problem between factorial scale,
convergent denominator, and the next partial quotient.  Equation (28), not a
simple congruence in $N$, is the structural condition seen in the data.

## 5. Exact exhaustion through $N=2000$

Let



$$
D=\#\operatorname{digits}(2000!)+120=5856,\qquad S=10^D. \tag{29}
$$



The replay constructs integers $L<U$ with



$$
\frac LS<e+\pi<\frac US.                            \tag{30}
$$



For $e$, it uses a Taylor partial sum and the exact tail bound



$$
\sum_{j>K}\frac1{j!}
 \leq\frac{K+2}{(K+1)!(K+1)}.                        \tag{31}
$$



For $\pi$, it uses Machin's identity and alternating rational bounds for
$\arctan(1/5)$ and $\arctan(1/239)$.  Every individual term is rounded
outward at the common scale $S$.  The final enclosure has width only



$$
U-L=71822                                             \tag{32}
$$



units of $10^{-5856}$.

The exact interval continued-fraction algorithm repeatedly checks that the
floors of both endpoints agree, subtracts that common floor, and reciprocates
the interval.  It certifies 5684 common partial quotients, through the first
convergent whose denominator exceeds
$\lfloor\sqrt{2000!}\rfloor$.  Hence every
principal convergent relevant to (3) is certified without assuming that
$e+\pi$ is irrational.

For each $10\leq N\leq2000$, the replay considers every certified
below-side convergent with $Q\leq\lfloor\sqrt{N!}\rfloor$, using outward
integer bounds for



$$
Z_{N,k}=N\,N!\left(s-\frac{p_k}{q_k}\right).        \tag{33}
$$



The complete broad candidate table is:

| $N$ | CF index $k$ | $N\bmod8$ | admissible? | digits $Q$ | $a_{k+1}$ | $Z_{N,k}$, approximately |
|---:|---:|---:|:---:|---:|---:|---:|
| 25 | 30 | 1 | yes | 13 | 8 | 4.0603955549 |
| 33 | 46 | 1 | yes | 19 | 10 | 3.5267265679 |
| 43 | 58 | 3 | yes | 26 | 365 | 2.4949162167 |
| 86 | 134 | 6 | no | 66 | 23 | 3.9992427387 |
| 88 | 138 | 0 | yes | 68 | 54 | 2.6119449336 |
| 164 | 302 | 4 | yes | 147 | 554 | 2.9304572911 |
| 331 | 700 | 3 | yes | 346 | 881 | 2.0872802609 |
| 351 | 740 | 7 | no | 372 | 140 | 3.0970978726 |
| 1477 | 4014 | 5 | no | 2021 | 557 | 4.9611981978 |

The decimals merely render exact rational intervals stored in the JSON.  The
JSON also stores every full numerator and denominator, fraction hashes,
partial quotients, and exact normalized-error interval hashes.

The preceding fixed-index package is pinned by all three artifact hashes and
its manifest hash.  It independently certifies strict membership for the six
admissible candidates.  Combining that membership certificate with the
exhaustive necessary-window scan proves (7)--(8).

## 6. What pattern is, and is not, established

The exact scan gives two genuine structural facts:

1. admissibility itself is the periodic condition
   $N\bmod8\in\{0,1,2,3,4\}$;
2. each fixed convergent can enter the broad factorial window for at most one
   index, by (22).

The candidate indices, CF indices, and next partial quotients do not obey any
proved recurrence in this package.  In particular, the fact that all three
new broad candidates lie in forbidden residue classes is a finite observation
through $2000$, not a congruence theorem.  The next partial quotients



$$
8,10,365,23,54,554,881,140,557                      \tag{34}
$$



also provide no justified extrapolation.  A continued fraction of a generic
nearby real number can realize arbitrary finite extensions, so the certified
prefix alone cannot prove a future hit or a future exclusion.

Here are precise sufficient missing lemmas.

**Irrationality target.**  Prove that (26) holds for infinitely many
admissible pairs $(N,k)$.  The reduced convergents are then infinitely many
distinct strict rational approximants whose errors tend to zero, proving that
$e+\pi$ is irrational.

**Transcendence target.**  Prove the same assertion together with a fixed
$0<\delta<1/2$ such that



$$
q_k\leq(N!)^{1/2-\delta}                             \tag{35}
$$



infinitely often.  Then



$$
0<s-\frac{p_k}{q_k}
 <\frac5{N\,N!}
 \leq\frac5N q_k^{-2/(1-2\delta)}.                  \tag{36}
$$



This beats exponent $2$ by
$4\delta/(1-2\delta)$; Roth's theorem excludes every algebraic irrational,
while the infinite strict approximants exclude rationality.  Such a lemma
would therefore prove transcendence.  No such infinite matching or power
saving is established here.

## 7. Replay and scope

Run

    python3 scripts/common_kernel_native_cf_window_scan_certificate.py

from the research directory.  The replay uses exact integers and rational
arithmetic only, remains below a 2 GiB RAM cap, and writes

    results/common_kernel_native_cf_window_scan_certificate.json

The theorem-facing scan is complete only for $10\leq N\leq2000$.  It does
not classify later indices and makes no claim that the displayed finite
sequence continues or terminates.
