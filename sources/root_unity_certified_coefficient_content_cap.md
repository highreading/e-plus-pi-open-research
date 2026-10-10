> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Certified coefficients, saturated content, and a primitive-height lower bound

## A rank-independent refinement of the corrected two-column height ledger

Checked: 2026-08-27 UTC

## 1. Verdict

Assume



$$
m\ge2,\qquad n\ge D\ge2.                 \tag{1}
$$



Let $K$ be the $(D-1)$-by-$(D+1)$ endpoint matrix, let



$$
A_K=2^{M+D-1}K\in\mathbb Z^{(D-1)\times(D+1)},
 \qquad M=m(n+1),                                         \tag{2}
$$



and let $p=(p_{ab})$ be the primitive saturated Pluecker vector of
$\ker K$.  Let $q_E$ be the least common denominator of the cardinal
matrix $E$, put $E^*=q_EE$, and define the integer corrected
coefficient vector



$$
N=q_E\Delta=\mathcal A_\Delta p.          \tag{3}
$$



Write



$$
\mathfrak c_E=\operatorname {cont}(N),\qquad
 P_\Delta=N/\mathfrak c_E,\qquad
 H_N=H(N).                                                 \tag{4}
$$



The earlier primitive-height audit supplied an upper bound for
$H(P_\Delta)$, but no useful lower bound because it did not yet know a
coefficient of $\Delta$ that was universally nonzero.  The new
top-cardinal, forced odd-frequency, and corrected even-frequency theorems
remove that obstruction.

Define the certified index set



$$
\mathcal I_{m,n,D}=
 \begin{cases}
 \{\,2D-1,2D,\ldots,n+D\,\},&m\text{ odd},\\
 \{0\}\cup\{\,2D-1,2D,\ldots,n+D\,\},&m\text{ even},
 \end{cases}                                               \tag{5}
$$



and its exact coefficient gcd



$$
\boxed{
 G_{\rm cert}:=\gcd\{|N_\ell|:\ell\in\mathcal I_{m,n,D}\}.} \tag{6}
$$



Zeros in (6) are harmless.  The cited nonvanishing theorems guarantee that
not every selected coordinate is zero, so $G_{\rm cert}>0$.

The main conclusion is the elementary but previously unavailable
endpoint-specific content theorem



$$
\boxed{\mathfrak c_E\mid G_{\rm cert}.}                   \tag{7}
$$



Consequently,



$$
\boxed{
       H(P_\Delta)=\frac{H_N}{\mathfrak c_E}
       \ge\frac{H_N}{G_{\rm cert}}.}                       \tag{8}
$$



This works whether or not the ambient corrected map
$\mathcal A_\Delta$ has full column rank.  It therefore supplies a
structured cap precisely in the rank-deficient range where the ambient
Smith theorem from the earlier audit is unavailable.

The result is a height/content refinement, not an arithmetic
classification.  In particular, (7)--(8) do not prove that the corrected
endpoint value is small enough to contradict algebraicity of $e+\pi$.

## 2. The exact saturated determinant coordinates

Put



$$
\delta_K=\gcd\{\det(A_K)_{\widehat{a,b}}:0\le a<b\le D\}.
                                                                    \tag{9}
$$



Choose the global sign of $p$ so that complementary-minor orientation
has the following form.  For $0\le a\le D$ and $0\le b\le n$, set



$$
\mathscr B_{a,b}
 =\det\!\begin{pmatrix}
 A_K\\ e_a^T\\ E_b^*
 \end{pmatrix}.                                           \tag{10}
$$



Laplace expansion along $e_a^T$, together with the saturated
complementary-minor formula for $p$, gives the exact identity



$$
\boxed{
 \mathscr B_{a,b}
   =\delta_K\sum_{j=0}^{D}E^*_{b,j}p_{aj}.}                \tag{11}
$$



Here $p_{ja}=-p_{aj}$ and $p_{aa}=0$.  Reversing the orientation of
$p$ changes both sides of every later coefficient identity by one common
sign and changes none of the gcd statements.

The corrected coefficient formula from the primitive-height audit is



$$
N_\ell=q_Ew_\ell(p)
 -\sum_{\substack{0\le a\le D,\ 0\le b\le n\\a+b=\ell}}
      \sum_{j=0}^{D}E^*_{b,j}p_{aj}.                       \tag{12}
$$



Since $\deg W(C,D)\le2D-2$, equations (11)--(12) imply, for every
$\ell\ge2D-1$,



$$
\boxed{
 N_\ell=-\frac1{\delta_K}
 \sum_{\substack{0\le a\le D,\ 0\le b\le n\\a+b=\ell}}
          \mathscr B_{a,b}.}                              \tag{13}
$$



Thus every high coordinate used in (6) is an explicit quotient of a sum
of augmented integer determinants by the exact endpoint saturation
divisor.  The quotient is integral because it is the contraction in
(11), not because of an unsaturated rational nullspace computation.

For even $m$, the additional certified coordinate is equally explicit:



$$
\boxed{
 N_0=q_Ep_{01}-\frac{\mathscr B_{0,0}}{\delta_K}.}          \tag{14}
$$



The first term is the constant coefficient of the bare Wronskian, and the
second is the constant cardinal correction.

Equations (13)--(14) make $G_{\rm cert}$ computable without choosing an
integer basis $C,D$ of the endpoint plane.

## 3. Why the selected gcd is nonzero

For odd $m$, there are two possibilities.

1. If parity permits the top cardinal, the top-cardinal theorem gives

   

$$
N_{n+D}\ne0.                           \tag{15}
$$



2. The only forced odd-$m$ family is

   

$$
m\ge3\text{ odd},\quad n\text{ even},\quad
      D\text{ odd}.
$$



   The external-node reproducing-kernel theorem gives

   

$$
N_{n+D-1}\ne0.                         \tag{16}
$$



Both indices lie in the high tail in (5).  Hence that tail is nonzero for
every odd $m$ in (1).

For even $m$, the corrected constant-border theorem gives



$$
N_0\ne0.                          \tag{17}
$$



This proves $G_{\rm cert}>0$ in all cases.  Notice that no unproved
next-highest coefficient statement is used in an even-frequency
parity-forced family.

## 4. Content and height

By definition, $\mathfrak c_E$ divides every coordinate of $N$.
It therefore divides the gcd of any nonzero subset of those coordinates.
Applying this observation to (5) proves (7), and division of
$H(P_\Delta)=H_N/\mathfrak c_E$ by the upper bound
$\mathfrak c_E\le G_{\rm cert}$ proves (8).

There are two useful refinements.

First, whenever the ambient map has full column rank and largest Smith
invariant $s_R$, the previous theorem and (7) combine to give



$$
\boxed{\mathfrak c_E\mid\gcd(G_{\rm cert},s_R).}           \tag{18}
$$



Second, let $Q=Q_{m,n}$ be the universal interpolation clearing and put



$$
N_Q=Q\Delta,\qquad
 \mathfrak c_Q=\operatorname {cont}(N_Q).
$$



Since $q_E\mid Q$,



$$
N_Q=\frac Q{q_E}N,\qquad
 \mathfrak c_Q=\frac Q{q_E}\mathfrak c_E.                 \tag{19}
$$



Define



$$
G_Q=\frac Q{q_E}G_{\rm cert}.      \tag{20}
$$



Then



$$
\boxed{
 \mathfrak c_Q\mid G_Q,\qquad
 H(P_\Delta)\ge\frac{H(N_Q)}{G_Q}.}                        \tag{21}
$$



The quotient on the right of (21) is the same as the quotient in (8);
the statement is independent of the chosen common clearing.

## 5. The corrected threshold now has a rank-independent necessary test

Retain the notation of item 39:



$$
\begin{aligned}
 C_0&=(2m+1)(2n+1),\\
 \mathcal G_1&=(L-n)\log\frac{L-n}{e\pi m}-n\log\pi,\\
 d&=\deg P_\Delta,\qquad
 \kappa=r^2d+r-1,
 \end{aligned}                                             \tag{22}
$$



under the hypothetical assumption that $e+\pi$ is algebraic of degree
$r$.  The leading corrected-content requirement was



$$
(\kappa+1)\log\mathfrak c_Q>
 \kappa\log H(N_Q)+\log(C_0H_W)
 -2\mathcal G_1-\log Q.                                   \tag{23}
$$



Equation (21) gives a necessary condition for (23):



$$
\boxed{
 (\kappa+1)\log G_Q>
 \kappa\log H(N_Q)+\log(C_0H_W)
 -2\mathcal G_1-\log Q.}                                  \tag{24}
$$



If (24) fails, then the Schwarz/content implementation cannot meet (23),
regardless of the rank of $\mathcal A_\Delta$, the size of its ambient
Smith invariants, or any choice of a saturated integer basis for the
endpoint plane.  Passing (24) is only necessary; it is not sufficient,
because $G_Q$ can strictly exceed the true content.

## 6. Exact obstruction to stronger conclusions from one coefficient

Knowing a nonzero leading coordinate does **not** determine the corrected
content.  The saturated replay already contains sharp counterexamples.

At



$$
(m,n,D)=(3,5,4),
$$



the globally $q_E$-cleared content, leading coordinate, and high-tail gcd
are respectively



$$
\mathfrak c_E=512,\qquad
 |N_9|=5494957056,\qquad
 G_{\rm high}=373248.
$$



After division by the true content, the primitive leading coordinate is
$10732338$, while the selected high-tail gcd is $729$.  Thus the
high-tail cap improves the single-leading-coordinate cap by a factor
$14722$, but still exceeds the true content by a factor $729$.

At



$$
(m,n,D)=(4,6,4),
$$



the corresponding exact global data are



$$
\begin{aligned}
 \mathfrak c_E&=442368,\\
 |N_{10}|&=2049070069153704996300128256,\\
 G_{\rm high}&=41278242816,\\
 G_{\rm cert}&=56623104.
 \end{aligned}
$$



After division by $\mathfrak c_E$, the primitive leading coordinate is
$4632048586592395915392$.  The high-tail cap overestimates the content
by the factor $93312$; adjoining the certified nonzero constant
coefficient reduces that factor to $128$, but still does not determine
the content.

Therefore:

* a leading coefficient supplies a valid content **upper** bound, never a
  content lower bound;
* saturation alone does not make that leading coefficient primitive;
* even the certified multi-coordinate gcd can be strictly larger than the
  true content; and
* any exact content formula still requires arithmetic information from
  coefficients outside the certified subset.

These examples also explain the correct logical use of (8): it is a
rigorous primitive-height lower bound, not an exact height formula.

## 7. Deterministic replay

The companion certificate:

1. constructs $A_K$, $\delta_K$, the saturated primitive Pluecker
   vector, $E^*$, and $N=\mathcal A_\Delta p$;
2. verifies (11) for every $a,b$ on each replay tuple;
3. verifies (13)--(14), the certified nonzero coordinate, and
   $\mathfrak c_E\mid G_{\rm cert}$;
4. checks the clearing-invariance identities (19)--(21);
5. records the single-leading, high-tail, and certified-gcd caps
   separately; and
6. records exact counterexamples where each cap strictly exceeds the full
   content.

All determinant, gcd, divisibility, degree, and height statements in the
certificate are exact.  Decimal endpoint evaluations are neither needed
nor performed.

The replay is finite evidence for the sizes of the caps.  The
all-parameter assertions (7)--(8), (13)--(14), and (18)--(24) follow from
the algebra above and the separately proved nonvanishing theorems, not from
the replay grid.
