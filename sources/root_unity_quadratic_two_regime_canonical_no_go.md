> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The quadratic closer-root two-regime test

## Exact thresholds, the unique two-row pole cancellation, and canonical no-go reductions

Checked: 2026-08-27 UTC

## 1. Scope

Put



$$
A_N=(2N+2)(2N+1),\qquad
 G_N=\gcd\!\left(A_N|E_{2N}|,|E_{2N+2}|\right),
                                                               \tag{1}
$$



and



$$
P_N={|E_{2N+2}|\over G_N},\qquad
 Q_N={A_N|E_{2N}|\over G_N},\qquad
 C_N(T)=4Q_N-P_NT^2.                                         \tag{2}
$$



The integers $P_N,Q_N$ are positive and coprime.  The exact beta-ratio
identity is



$$
{P_N\over Q_N}
  =\alpha\bigl(1+\delta_s\bigr),\qquad
 \alpha={4\over\pi^2},\qquad s=2N+1,
                                                               \tag{3}
$$



where



$$
\delta_s={\beta(s+2)\over\beta(s)}-1
          ={8\over3^{s+2}}-{24\over5^{s+2}}+O(7^{-s}).        \tag{4}
$$



For clarity, the second term in (4) is not a numerical extrapolation.
The alternating series for $\beta(s+2)-\beta(s)$ has first two terms
$8/3^{s+2}$ and $-24/5^{s+2}$, and its remaining tail is bounded in
absolute value by its first omitted term, hence is $O(7^{-s})$.
Furthermore $\beta(s)^{-1}=1+O(3^{-s})$; the resulting denominator
correction is $O(9^{-s})$, which is absorbed by $O(7^{-s})$.

The frozen beta-denominator package proves, in addition, that the ratios in
(3) are strictly decreasing and that



$$
D_N=P_NQ_{N+1}-P_{N+1}Q_N>0,\qquad v_2(D_N)=1,              \tag{5}
$$



as well as



$$
Q_NQ_{N+1}>
 {13\pi^2\over216}\,3^{2N+3}.                                \tag{6}
$$



This note asks whether the alternative “$G_N$ is not large enough, hence
$Q_N$ is large” can itself drive a neighboring auxiliary construction.
The answer for the canonical coefficient-content, determinant, Bezout,
product, and fixed two-row constructions is precise:

1. The original quadratic branch has the exact conditional rate threshold
   (13) below.  “Large $G_N$” must mean within an exponential factor of the
   entire factorial-size raw coefficient.
2. Translating $C_N(\pi)$ to a polynomial in $e$ over a fixed algebraic
   coefficient field creates no unbounded nonarchimedean coefficient
   content.  Thus a product-formula normalization cannot erase a large
   $Q_N$ in this direct construction.
3. Adjacent determinant and Bezout elimination saturate to a monomial or a
   constant.  The adjacent product has relative exponent at most $2+o(1)$,
   far below the degree-four conditional threshold.
4. Among fixed affine combinations of two adjacent rows, the only
   cancellation of the nearest pole is the Richardson combination

   

$$
{9(P_{N+1}/Q_{N+1})-P_N/Q_N\over8}.                  \tag{7}
$$



   Its error has base $5$, but its reduced denominator is small only when a
   new, explicit common-divisor condition between $Q_N$ and $Q_{N+1}$ holds.
   The small-$G_N$ hypothesis alone supplies no such neighboring valuation
   condition.

Thus the proposed two-regime dichotomy does not close by these canonical
operations.  A successful complementary branch would need a new theorem
about the common divisor in (38), a noncanonical combination with its own
height analysis, or a genuinely different auxiliary form.  No finite data
are used to infer an all-parameter arithmetic estimate, and nothing here
classifies $e+\pi$.

## 2. The first branch and its exact conditional threshold

Every secant Euler number is odd.  Therefore $G_N$ and $P_N$ are odd, and
$C_N$ is primitive.  The elementary beta bounds
$1-3^{-s}<\beta(s)<1$, together with $\pi>3$, give explicitly



$$
{P_N\over Q_N}
 <{4\over9}\,{1\over1-3^{-s}}
 \le {4\over9}\,{27\over26}={6\over13}<1
 \qquad(s\ge3).
$$



Thus $P_N<Q_N$ for $N\geq1$, and hence



$$
H(C_N)=4Q_N,\qquad
 {|C_N(\pi)|\over H(C_N)}=\delta_s.                           \tag{8}
$$



The reduced denominators $Q_N$ tend to infinity, as proved in the frozen
beta-denominator package, so the all-sufficiently-large-height clause in
the measure below applies to every infinite subsequence after discarding
finitely many terms.

Assume temporarily that $z=e+\pi$ is algebraic of degree $r$.  For a
primitive integer polynomial of degree two, the fixed-degree conditional
$e$-measure gives, for every $\varepsilon>0$ and all sufficiently large
heights,



$$
|C_N(\pi)|>
 H(C_N)^{-\left(2r^2+r-1+\varepsilon\right)}.                \tag{9}
$$



After division by the height, the relative threshold is



$$
\tau_r=2r^2+r.                              \tag{10}
$$



Since



$$
-\log\delta_s=2N\log3+O(1),                                 \tag{11}
$$



the quadratic family contradicts the degree-$r$ hypothesis along any
infinite subsequence $\mathcal N$ on which



$$
\limsup_{\substack{N\to\infty\\N\in\mathcal N}}
 {\log Q_N\over N}
       <c_{3,r},\qquad
 c_{3,r}={2\log3\over2r^2+r}.                                \tag{12}
$$



Equivalently, in terms of the Euler gcd, the required first-branch
condition is



$$
\boxed{\;
 \log G_N>
 \log\!\left(A_N|E_{2N}|\right)-c_{3,r}N+\Omega(N)
 \quad\hbox{along a subsequence}. \;}                         \tag{13}
$$



Here $\Omega(N)$ means a positive linear margin; it is the strict gap
needed to choose $\varepsilon$ in (9).  At the rational hypothesis $r=1$,



$$
c_{3,1}={2\log3\over3}
                  =0.7324081924\ldots .                      \tag{14}
$$



Thus a gcd which is merely exponential, or even
$\exp(o(N\log N))$, is not the “large gcd” needed by this branch.  It must
remove the whole $2N\log N+O(N)$ Euler height except for a sufficiently
small exponential denominator.

## 3. Fixed-field coefficient content cannot absorb $Q_N$

The following lemma is unconditional and isolates the direct
nonarchimedean route.

**Lemma 3.1 (bounded translation content).**  Let $K$ be a fixed number
field, let $z\in K$, and choose a fixed positive integer $m$ such that
$\theta=mz\in\mathcal O_K$.  For any coprime positive integers $P,Q$, put



$$
F_{P,Q}(X)=m^2\bigl(4Q-P(z-X)^2\bigr)\in\mathcal O_K[X].
                                                               \tag{15}
$$



For every prime ideal $\mathfrak p$ of $\mathcal O_K$,



$$
\min_{0\le j\le2}v_{\mathfrak p}\!\left([X^j]F_{P,Q}\right)
       \le v_{\mathfrak p}(4m^4).                             \tag{16}
$$



In particular, the common coefficient ideal divisor of $F_{P,Q}$ is
bounded by a fixed ideal independent of $P,Q$.

To prove the lemma, write



$$
\begin{aligned}
 a_0&=4m^2Q-P\theta^2,\\
 a_1&=2Pm\theta,\\
 a_2&=-Pm^2.
\end{aligned}                                                 \tag{17}
$$



The integral coefficient combination



$$
m^2a_0-\theta^2a_2=4m^4Q                \tag{18}
$$



shows that the left side of (16) is at most



$$
\min\{v_{\mathfrak p}(Pm^2),v_{\mathfrak p}(4m^4Q)\}.
                                                               \tag{19}
$$



Because $\gcd(P,Q)=1$, at least one of
$v_{\mathfrak p}(P),v_{\mathfrak p}(Q)$ is zero.  The quantity in (19) is
therefore at most $v_{\mathfrak p}(4m^4)$, proving (16).

Apply the lemma with $K=\mathbb Q(z)$, $P=P_N$, and $Q=Q_N$.  Formula (3)
gives $P_N\asymp Q_N$.  To state the height conclusion globally, let



$$
H_K^{\mathrm{proj}}(F)
 =\prod_v\max_{0\le j\le2}|a_j|_v^{\,n_v/[K:\mathbb Q]}
$$



be the absolute projective coefficient height, with the usual normalized
absolute values.  At every archimedean embedding, the rational coefficient
$a_2=-P_Nm^2$ supplies a lower bound $\gg P_N$, while the fixed integral
model (17) gives the upper bound $O_{K,z,m}(Q_N)$.  At every finite place,
(16) bounds the common coefficient valuation by a fixed amount; hence the
entire finite-place factor is bounded above and below by positive constants
depending only on $K,z,m$.  Therefore



$$
H_K^{\mathrm{proj}}(F_{P_N,Q_N})
                    \asymp_{K,z,m}Q_N.
$$



Consequently a large $Q_N$ cannot be turned into a small global coefficient
height by translating to $e$ and invoking finite-place content.  This does
not exclude an unrelated $p$-adic auxiliary construction; it is an exact
no-go for the direct translated quadratic.

## 4. Adjacent determinant, Bezout, and product

Write $P=P_N$, $Q=Q_N$, $P'=P_{N+1}$, $Q'=Q_{N+1}$, and
$U=T^2$.  Direct elimination gives



$$
\begin{aligned}
 Q'C_N-QC_{N+1}&=-D_NU,\\
 P'C_N-PC_{N+1}&=-4D_N.                                   
\end{aligned}                                                 \tag{20}
$$



Thus primitive normalization turns the two coefficient-canceling
combinations into $U$ and $1$.  Equivalently,



$$
\begin{aligned}
 \left|\operatorname {Res}_U(4Q-PU,4Q'-P'U)\right|
      &=4D_N,\\
 \left|\operatorname {Res}_T(C_N,C_{N+1})\right|
      &=16D_N^2.
\end{aligned}                                                 \tag{21}
$$



The determinant and Bezout routes therefore eliminate the small endpoint
at the same time as they eliminate a coefficient.  The nonzero integer
$D_N$ does give the denominator floor (6), but it is not a new small
polynomial value at $\pi$.  It also shows that two adjacent original rows
cannot both satisfy the strict first-branch threshold: (6) forces their
logarithmic denominator sum to be at least $2N\log3+O(1)$, whereas two
instances of (12) would make that sum less than
$2c_{3,r}N+o(N)<2N\log3$.

The symmetric product is also exact.  Gauss's lemma makes
$C_NC_{N+1}$ primitive, and $P_N<Q_N$ implies



$$
\begin{aligned}
 H(C_NC_{N+1})&=16Q_NQ_{N+1},\\
 {|C_N(\pi)C_{N+1}(\pi)|\over H(C_NC_{N+1})}
     &=\delta_s\delta_{s+2}.
\end{aligned}                                                 \tag{22}
$$



Equations (4), (6), and (22) yield



$$
\begin{aligned}
 -\log(\delta_s\delta_{s+2})&=4N\log3+O(1),\\
 \log H(C_NC_{N+1})&\ge2N\log3+O(1).
\end{aligned}                                                 \tag{23}
$$



Hence



$$
\limsup_{N\to\infty}
 {-\log\!\left(|C_N(\pi)C_{N+1}(\pi)|
                    /H(C_NC_{N+1})\right)
  \over\log H(C_NC_{N+1})}
 \le2.                                                        \tag{24}
$$



The conditional relative threshold for degree four is $4r^2+r$, which is
at least $5$.  Thus the adjacent product cannot contradict any algebraic
degree hypothesis through this measure.  This conclusion is
all-parameter; it is not a finite-height extrapolation.

## 5. Classification of fixed two-row affine combinations

For fixed integers $a,b$, align the two rows by their denominators:



$$
L_{a,b,N}(T)
   =aQ_{N+1}C_N(T)+bQ_NC_{N+1}(T).                           \tag{25}
$$



If $a+b=0$, equation (20) says that $L_{a,b,N}$ is a multiple of the
monomial $D_NT^2$.  Suppose $a+b\ne0$.  The ratio of its quadratic and
constant coefficients, after the harmless scalar $a+b$, is



$$
\alpha\left(
 1+{a\delta_s+b\delta_{s+2}\over a+b}\right).                \tag{26}
$$



Using (4),



$$
a\delta_s+b\delta_{s+2}
 ={8\over3^{s+2}}\left(a+{b\over9}\right)
  -{24\over5^{s+2}}\left(a+{b\over25}\right)
  +O_{a,b}(7^{-s}).                                         \tag{27}
$$



Therefore the nearest-pole base $3$ cancels if and only if



$$
a+{b\over9}=0.                       \tag{28}
$$



Up to a nonzero common scalar, the unique fixed solution is
$(a,b)=(-1,9)$.  This proves the claimed uniqueness of (7) among fixed
two-row affine combinations.  The assertion deliberately does not
classify weights which grow with $N$; such weights carry their own height
and content cost and constitute a different Diophantine problem.

## 6. The Richardson branch and its exact denominator

From (4),



$$
9\delta_{s+2}-\delta_s
       ={384\over5^{s+4}}+O(7^{-s}).                         \tag{29}
$$



Define



$$
\begin{aligned}
 R_N&=9P_{N+1}Q_N-P_NQ_{N+1},\\
 S_N&=8Q_NQ_{N+1},\\
 K_N&=\gcd(R_N,S_N),\\
 \widehat P_N&={R_N\over K_N},\qquad
 \widehat Q_N={S_N\over K_N}.
\end{aligned}                                                 \tag{30}
$$



For all $N$, $R_N>0$.  Indeed $P_N/Q_N<1$, while
$P_{N+1}/Q_{N+1}>\alpha>2/5$.  The last elementary inequality follows
from $\pi^2<10$.  Moreover, the exact 2-adic description in the frozen
beta-denominator theorem gives



$$
v_2(Q_N)=1+v_2(N+1).
$$



The two summands in $R_N$ consequently have distinct 2-adic valuations,
so



$$
v_2(R_N)=v_2(K_N)=1.                   \tag{31}
$$



It follows that $\widehat P_N$ is odd and that



$$
\widehat C_N(T)=4\widehat Q_N-\widehat P_NT^2               \tag{32}
$$



is primitive.  Moreover,
$\widehat P_N/\widehat Q_N=(9P_{N+1}/Q_{N+1}-P_N/Q_N)/8$
lies between $0$ and $9/8$, so
$H(\widehat C_N)=4\widehat Q_N$.  Equations (3), (29), and (30) give



$$
{|\widehat C_N(\pi)|\over H(\widehat C_N)}
 =\left|{9\delta_{s+2}-\delta_s\over8}\right|
 ={48\over5^{s+4}}\left(1+O((5/7)^s)\right).                 \tag{33}
$$



Because the reduced rational $\widehat P_N/\widehat Q_N$ converges to the
irrational number $\alpha$, its denominator $\widehat Q_N$ tends to
infinity.

Thus the second branch would contradict the degree-$r$ algebraic
hypothesis along an infinite subsequence $\mathcal N$ if



$$
\limsup_{\substack{N\to\infty\\N\in\mathcal N}}
 {\log\widehat Q_N\over N}
       <c_{5,r},\qquad
 c_{5,r}={2\log5\over2r^2+r}.                                \tag{34}
$$



At $r=1$,



$$
c_{5,1}={2\log5\over3}
                    =1.0729586082\ldots .                    \tag{35}
$$



The improved base is real, but reduction of the raw denominator in (30)
is a new arithmetic issue.

To display it exactly, put



$$
h_N=\gcd(Q_N,Q_{N+1}),\qquad
 Q_N=h_Nu_N,\qquad Q_{N+1}=h_Nv_N,\qquad
 \gcd(u_N,v_N)=1.                                           \tag{36}
$$



Then



$$
\begin{aligned}
 R_N&=h_NX_N,\qquad
 X_N=9P_{N+1}u_N-P_Nv_N,\\
 K_N&=h_NL_N,\qquad
 L_N=\gcd(X_N,8h_Nu_Nv_N).
\end{aligned}                                                 \tag{37}
$$



The coprimality relations imply



$$
\gcd(X_N,u_N)=1,\qquad \gcd(X_N,v_N)\mid9.
$$



Also $v_2(h_N)=1$ and $X_N$ is odd by (31).  Hence
no prime factor contributed by $u_N$ can occur in $L_N$, the contribution
from $v_N$ beyond that from $h_N$ divides $9$, and the factor $2$ in
$h_N$ does not occur.  Prime by prime this gives



$$
L_N\mid 9\,{h_N\over2},
\qquad
 \boxed{\;
 {16Q_NQ_{N+1}\over9h_N^2}
       \le\widehat Q_N
       \le {8Q_NQ_{N+1}\over h_N}. \;}                       \tag{38}
$$



In particular, the denominator condition (34) necessarily requires



$$
2\log h_N\ge
 \log Q_N+\log Q_{N+1}-c_{5,r}N+o(N).                        \tag{39}
$$



Combining this with the unconditional adjacent floor (6) gives the more
transparent necessary condition



$$
\log h_N\ge
 \left(\log3-{\log5\over2r^2+r}\right)N+o(N).
$$



For $r=1$ the coefficient on the right is
$0.5621329845\ldots$.  In particular, a subexponential adjacent gcd can
never power the Richardson branch.

More exactly, (30) says that the Richardson branch succeeds at the rate
level precisely when



$$
\log K_N>
 \log Q_N+\log Q_{N+1}-c_{5,r}N+\Omega(N).                   \tag{40}
$$



Thus the complementary construction needs a nearly maximal adjacent
common divisor, plus the congruence cancellation encoded in $L_N$.  Large
$Q_N$ does not by itself provide either.

## 7. Translation back to Euler valuations

The last point can be made primewise without any heuristic.  For a prime
$p$, set



$$
\begin{aligned}
 x&=v_p(A_N|E_{2N}|),&
 y&=v_p(|E_{2N+2}|),\\
 a&=v_p(A_{N+1}),&
 z&=v_p(|E_{2N+4}|).
\end{aligned}                                                 \tag{41}
$$



The definitions (1)--(2) give the exact identities



$$
\begin{aligned}
 v_p(Q_N)&=(x-y)_+,\\
 v_p(Q_{N+1})&=(a+y-z)_+,\\
 v_p(h_N)&=\min\!\left((x-y)_+,(a+y-z)_+\right).
\end{aligned}                                                 \tag{42}
$$



The first-regime failure “$G_N$ too small” records positive excesses
$x-y$.  The common divisor required by (39) additionally asks that those
same prime powers survive the next comparison $a+y-z$.  Formula (42) is
the precise missing neighboring-Euler condition.  It is not a consequence
of the definition of $G_N$, which involves only the first two entries.

Consequently the canonical two-regime program reduces, rather than solves,
the arithmetic problem:



$$
\begin{array}{c|c}
\text{branch}&\text{strict rate condition}\\ \hline
C_N&
 \log Q_N<c_{3,r}N-\Omega(N)\\
\widehat C_N&
 \log(8Q_NQ_{N+1}/K_N)<c_{5,r}N-\Omega(N).
\end{array}                                                   \tag{43}
$$



Determinants, Bezout elimination, products, and direct fixed-field content
do not fill the gap between these alternatives.  Proving that one row of
(43) always occurs would require a new all-parameter theorem about
$K_N=h_NL_N$, equivalently about the three consecutive Euler valuations in
(42).  No such theorem is asserted here.

## 8. Dependencies and replay

This note uses the frozen exact identities and adjacent determinant theorem
from:

- sources/root_unity_closer_root_sech_pade_audit.md;
- sources/root_unity_quadratic_euler_gcd_kummer_obstruction.md;
- sources/root_unity_quadratic_euler_beta_denominator_floor.md.

The companion deterministic certificate checks every displayed algebraic
identity, the beta-pole cancellation constants, the threshold ledger, the
gcd inequalities on exhaustive bounded symbolic instances, the resultant,
the exact parity statements, dependency hashes, and a strict
control-character scan.  Those finite checks audit the formulas; the
proofs above establish the all-parameter statements.

From the research directory run

    python3 scripts/root_unity_quadratic_two_regime_canonical_certificate.py
    sha256sum -c results/root_unity_quadratic_two_regime_canonical_hashes.sha256

No claim in this package proves or disproves the transcendence of
$e+\pi$.
