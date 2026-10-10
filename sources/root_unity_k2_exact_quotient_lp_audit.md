> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The exact rational quotient--LP principle for the saturated $k=2$ image

## A fixed-endpoint certificate, an exact nonoptimality witness, and the clearing-denominator obstruction

Checked: 2026-08-27 UTC

## 1. Scope and verdict

Let $V\subseteq\mathbb Q^P$ be the intrinsically saturated rational space
of complete global coefficient vectors in the root-of-unity exterior-square
construction, and let



$$
E:V\longrightarrow\mathbb Q^q                 \tag{1}
$$



be the retained endpoint map.  For a prescribed primitive endpoint
$p\in\mathbb Z^q$, choosing a rational right inverse of $E$ identifies
the full fixed-endpoint fiber with an affine translate of $\ker E$.  At an
integer circle radius, replacing $e$ and $\pi$ by elementary strict
rational upper bounds turns the coefficientwise circle estimate into a
finite linear program over $\mathbb Q$.

The exact principle is:



$$
\boxed{
 \inf_{Ex=p/H}\sum_{j=1}^Pw_j|x_j|
 =\inf_{t\in\mathbb R^s}
   \sum_{j=1}^Pw_j|b_j+(tK)_j|,}                         \tag{2}
$$



where $H=H(p)$, $b=(p/H)\Lambda$, $\Lambda$ is any rational right
inverse, and the rows of $K$ form a rational basis of $\ker E$.  The
rational points of the affine fiber have the same infimum as the real
points.  Any rational primal feasible point gives a rigorous rational upper
bound.  It is an **optimum** only if optimality is separately proved, for
example by a matching exact dual certificate.

The deterministic replay treats



$$
(m,n,D,d,R)=(2,8,7,2,13),\qquad
 p=(5441060864,0,551294727).                             \tag{3}
$$



It reconstructs a rank-$11$ saturated global image in $85$ coefficient
slots.  The retained endpoint map has rank $3$, and its endpoint-zero
kernel has rank $8$.  A fixed exact rational primal gives



$$
\log B=15.887454239720596\ldots,       \tag{4}
$$



where $B$ is a rigorous rational coefficientwise upper bound for
$|p_0-p_2\pi^2|$.

The important audit finding is that this primal is **not optimal**.  There
is an exact endpoint-zero direction whose one-sided weighted
$\ell^1$-derivative is



$$
-\frac{39710900240730900314101}
                    {17036837675827200}<0.               \tag{5}
$$



An explicit rational step strictly lowers the objective.  Thus the word
“optimum” in the temporary probe must not be carried into a theorem.  The
improved primal is also recorded only as feasible, because no exact dual
certificate is known.

The improved bound still has



$$
\log B_{\mathrm{imp}}=15.8874542397205888\ldots,\qquad
 -\log B_{\mathrm{imp}}-2\log H(p)
       =-60.72193402085388\ldots.                        \tag{6}
$$



It is therefore arithmetically far from the degree-two measure threshold.

There is also an exact normalization warning.  Clearing the first rational
global vector to a primitive integral coefficient vector multiplies its
primitive endpoint by



$$
6518378303365776642144000,       \tag{7}
$$



and the descended vector requires the still larger multiplier



$$
645319452033211887572256000.     \tag{8}
$$



Both cleared global vectors have content one.  Consequently neither
multiplier is removed by global primitive division.  This is an exact finite
example of a cheap rational quotient direction acquiring an enormous
integer clearing cost.  It is not a universal denominator lower bound.

No floating linear-program output is used anywhere in the certificate.  No
conclusion about the irrationality or transcendence of $e+\pi$ follows.

## 2. The affine quotient

Let $V$ be a finite-dimensional rational subspace of $\mathbb Q^P$, and
suppose (1) is surjective.  Choose a rational right inverse



$$
\Lambda\in\mathbb Q^{q\times P},
 \qquad \Lambda E^t=I_q.                                \tag{9}
$$



Use row-vector convention.  Let



$$
W=\ker(E|_V),qquad\dim W=s,      \tag{10}
$$



and let $K\in\mathbb Q^{s\times P}$ have rows forming a basis of $W$.
For $y\in\mathbb Q^q$, put



$$
b_y=y\Lambda.                   \tag{11}
$$



Then $E(b_y)=y$.  If $x\in V$ also satisfies $E(x)=y$, then
$x-b_y\in W$.  Conversely, adding any element of $W$ preserves the
endpoint.  Therefore



$$
\boxed{
       \{x\in V_{\mathbb R}:E(x)=y\}
       =\{b_y+tK:t\in\mathbb R^s\}.}                    \tag{12}
$$



The identical statement with $\mathbb Q$ in place of $\mathbb R$
holds for rational points.

The choice of $\Lambda$ and $K$ does not affect the affine set or the
infimum of any function on it.  Scaling individual kernel rows by nonzero
rational numbers merely changes the coordinates $t$.  The replay uses
such row scaling to keep the exact fractions smaller; it never changes the
rational kernel.

## 3. The weighted quotient LP and its dual audit

Fix positive rational weights $w_1,\ldots,w_P$.  Put $b=b_y$.  The
weighted quotient seminorm of the endpoint $y$ is the optimum of



$$
\begin{array}{ll}
 \text{minimize}&\displaystyle\sum_{j=1}^Pw_ju_j\\[2mm]
 \text{subject to}&-u_j\leq b_j+(tK)_j\leq u_j,
                    \qquad u_j\geq0.                    \tag{13}
 \end{array}
$$



Indeed, for fixed $t$, the least admissible $u_j$ is
$|b_j+(tK)_j|$, proving (2).  Because the rows of $K$ are independent,
the weighted $\ell^1$ objective is coercive in $t$; hence the real
minimum exists.  Rational points are dense in $\mathbb R^s$, so continuity
gives



$$
\inf_{t\in\mathbb Q^s}\sum_jw_j|b_j+(tK)_j|
 =\min_{t\in\mathbb R^s}\sum_jw_j|b_j+(tK)_j|.           \tag{14}
$$



Equation (14) does not bound the denominator of a rational near-minimizer.

The natural dual is



$$
\begin{array}{ll}
 \text{maximize}& b\,v^t\\
 \text{subject to}&Kv^t=0,qquad |v_j|\leq w_j.           \tag{15}
 \end{array}
$$



Weak duality is immediate: for every primal vector $g=b+tK$ and every
dual-feasible $v$,



$$
b\,v^t=g\,v^t
 \leq\sum_j|g_j||v_j|
 \leq\sum_jw_j|g_j|.                                    \tag{16}
$$



Thus equality between an exact primal and exact dual objective certifies
optimality.  Merely receiving a rational vector from a simplex routine does
not.

There is an equally elementary exact nonoptimality test.  Let
$\Phi(g)=\sum_jw_j|g_j|$, take a kernel direction $v$, and suppose
$0<\epsilon<\min_{g_jv_j\ne0}|g_j/v_j|$.  No initially nonzero coordinate
changes sign, so



$$
\Phi(g+\epsilon v)-\Phi(g)=\epsilon D_g(v),             \tag{17}
$$



where the one-sided derivative is



$$
D_g(v)=
 \sum_{g_j\ne0}w_j\operatorname {sgn}(g_j)v_j
 +\sum_{g_j=0}w_j|v_j|.                                 \tag{18}
$$



If (18) is negative, (17) is an exact strict descent certificate.

## 4. A completely rational circle bound

Flatten a centered global exponential polynomial as



$$
F_x(z)=\sum_{q=0}^{2m}\sum_{a=0}^{2n}
               x_{q,a}z^ae^{(q-m)z}.                    \tag{19}
$$



At an integer radius $R$, define



$$
w_{q,a}
 =\left(\frac{11}{4}\right)^{|q-m|R}R^a.                \tag{20}
$$



These weights are rational.  The elementary estimate $e<11/4$ follows,
for example, from



$$
e=\sum_{k=0}^\infty\frac1{k!}
 <\frac83+\frac1{24}\sum_{j=0}^\infty4^{-j}
 =\frac{49}{18}<\frac{11}{4}.                            \tag{21}
$$



Hence on $|z|=R$,



$$
|F_x(z)|
 \leq\sum_{q,a}|x_{q,a}|R^ae^{|q-m|R}
 \leq\sum_{q,a}w_{q,a}|x_{q,a}|.                        \tag{22}
$$



The classical rational upper bound for $\pi$ can be proved without any
decimal approximation by



$$
0<\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx
   =\frac{22}{7}-\pi.                                    \tag{23}
$$



Suppose $F_x$ has a zero of order at least $L$ at the origin.  Schwarz's
lemma, (22), and (23) give the fully rational estimate



$$
\boxed{
 |F_x(i\pi)|
 \leq\left(\frac{22}{7R}\right)^L
   \sum_{q,a}w_{q,a}|x_{q,a}|.}                          \tag{24}
$$



For (3), $L=2m(n+1)=36$, and $e^{-mi\pi}=e^{-2i\pi}=1$.  If
$E(x)=p/H$, then $F_x(i\pi)=P(i\pi)/H$, where



$$
P(z)=\sum_{a=0}^dp_az^a.         \tag{25}
$$



Multiplying (24) by $H$ therefore yields the exact rational endpoint bound



$$
|P(i\pi)|
 \leq H\left(\frac{22}{7R}\right)^{36}
   \sum_{q,a}w_{q,a}|x_{q,a}|.                           \tag{26}
$$



## 5. Exact finite construction at $(2,8,7,2,13)$

The replay reconstructs the cleared remainders, corrected endpoint-tail
kernel, complete Wronskian coefficient map, and intrinsic rational
saturation from the two frozen dependencies listed in Section 9.  It obtains



$$
\begin{array}{c|c}
 \text{quantity}&\text{exact value}\\ \hline
 P&(2m+1)(2n+1)=85\\
 \dim V&11\\
 \operatorname {rank}E&3\\
 \dim\ker(E|_V)&8\\
 L&36.
 \end{array}                                               \tag{27}
$$



Rows $4,7,10$ of the deterministic saturated LLL basis have independent
endpoint images.  If $S$ is the resulting $3$-by-$3$ endpoint matrix
and $G$ the corresponding global rows, the replay forms



$$
\Lambda=S^{-1}G                 \tag{28}
$$



and verifies (9) over $\mathbb Q$.  It independently saturates the
endpoint-zero global row space and obtains eight kernel rows.  Their
row-normalizing heights are



$$
\begin{split}
&288495043200, 760828723200, 1558311955200,\\
&12875563008000, 152575421644800, 167382319104000,\\
&133100294342400, 794739097152000.                       \tag{29}
\end{split}
$$



All endpoint coefficients above degree two and every origin derivative of
orders $0,\ldots,35$ are verified to vanish exactly for both rational
primal vectors.

The endpoint in (3) is primitive and has height



$$
H=5441060864.                    \tag{30}
$$



Its numerical value, used only as a diagnostic, is



$$
|p_0-p_2\pi^2|=0.1034435376245422260\ldots.              \tag{31}
$$



## 6. The feasible primal and the exact descent

For reproducibility the eight rational parameters of the first primal are
embedded directly in the replay.  Their global vector has seven zero
coordinates and SHA-256

```text
05ee0e24029a23b98943df2efe2914b5f95cc57a060d0bdbb91ead43b928af59
```

under the canonical comma-separated rational encoding.  Its exact weighted
objective is



$$
J_0=
 \frac{102212534483868087453404545818076700280569125554185793217865588198917}
 {4436907957595689369959657450411102340881842176000}.     \tag{32}
$$



Equations (12), (20), and the exact endpoint checks make this a valid primal
certificate independently of how it was found.

Take minus normalized kernel row $6$ as the direction in (18).  The replay
obtains exactly (5).  The first possible sign break is avoided by choosing



$$
\epsilon=
 \frac{1655947907}{22954475520}.                          \tag{33}
$$



It verifies (17) exactly and obtains



$$
J_1=
 \frac{91071368225125801171257449603880567839798794312328234796186781437463399}
 {3953284990217759228634054788316292185725721378816000}
 <J_0.                                                     \tag{34}
$$



The descended global rational vector has canonical SHA-256

```text
2a2a83be6e44744f73625a43e899cc95347ddfd8fb67dc5e1dd8631f21fba0b5
```

and the same normalized endpoint.  Neither (32) nor (34) is called the LP
optimum.  The exact strict inequality in (34) in fact disproves optimality of
the first point, while no exact dual is available for the second.

Substitution of (34) into (26) gives



$$
B_1=HJ_1\left(\frac{22}{91}\right)^{36},       \tag{35}
$$



an explicit positive rational number whose numerator and denominator are
stored in full in the result JSON.  Its logarithm is the value in (6), and
$B_1>1$ is checked exactly by integer comparison.

The finite relative exponent supplied by this upper bound is



$$
1-\frac{\log B_1}{\log H}
       =0.2912841046766798\ldots<3.                       \tag{36}
$$



The actual-value diagnostic from (31) gives exponent
$1.1012046691\ldots$, also below the strict threshold.

## 7. Exact clearing cost

Let $x\in\mathbb Q^P$ be either rational primal, and let



$$
L_x=\operatorname {lcm}_j
                                  \operatorname {den}(x_j).             \tag{37}
$$



Then $L_xx\in\mathbb Z^P$.  Because $E(x)=p/H$,



$$
E(L_xx)=\frac{L_x}{H}p.          \tag{38}
$$



Primitivity of $p$ and integrality of the endpoint imply $H\mid L_x$.
If $c_x$ is the global content of $L_xx$, primitive division leaves
endpoint multiplier



$$
\mu_x=\frac{L_x}{Hc_x}.          \tag{39}
$$



For (32), the exact data are



$$
\begin{aligned}
L_0&=35466893083190246764535051452416000,\\
c_0&=1,\\
\mu_0&=6518378303365776642144000.                         \tag{40}
\end{aligned}
$$



For the strictly improved point (34),



$$
\begin{aligned}
L_1&=3511222415235834429688970093789184000,\\
c_1&=1,\\
\mu_1&=645319452033211887572256000.                       \tag{41}
\end{aligned}
$$



Thus a rational function normalized to primitive endpoint $p$ becomes,
after integral clearing, a primitive global vector with endpoint
$\mu_xp$.  The global content is already one, so there is no cross-content
available to restore endpoint $p$.  This is precisely why a small
continuous or rational quotient norm is not by itself an integer linear-form
certificate.

The conclusion is finite and directional.  Equations (40)--(41) do not prove
that every rational point in the fiber has a large denominator, nor do they
give an asymptotic denominator lower bound.

## 8. Why the normalized-face claim is not frozen

One can enlarge (13) by allowing the endpoint coordinates themselves to vary
in the cube $[-1,1]^q$ while fixing one coordinate to $\pm1$.  This gives
an exact rational LP for each normalized face.  A real or floating solution,
however cheap, is not an arithmetic certificate.  To freeze such a face one
would need either an explicit exact rational primal, or preferably matching
exact primal and dual data, followed by the clearing audit (37)--(39).

No such normalized-face optimum is claimed here.  The available floating
face calculations are discarded, and a direct exact face solve did not
produce a bounded replay certificate.  The fixed-endpoint data (40)--(41)
already give a rigorous example of the denominator phenomenon, without
promoting an unreliable floating direction to a theorem.

## 9. Replay, hashes, and logical scope

The package consists of:

* `sources/root_unity_k2_exact_quotient_lp_audit.md`;
* `scripts/root_unity_k2_exact_quotient_lp_certificate.py`;
* `results/root_unity_k2_exact_quotient_lp_certificate.json`; and
* `results/root_unity_k2_exact_quotient_lp_hashes.sha256`.

Replay from the archive root with

    python3 scripts/root_unity_k2_exact_quotient_lp_certificate.py

The replay verifies the following frozen dependencies by SHA-256 before
import:

* `scripts/root_unity_nondecomposable_exterior_sum_certificate.py`;
* `scripts/root_unity_k2_global_image_saturation_certificate.py`.

It reconstructs the saturated image, right inverse, and endpoint-zero kernel;
checks all endpoint and origin identities over $\mathbb Q$; evaluates both
weighted objectives exactly; proves the strict descent identity; checks the
rational Schwarz bounds by numerator comparison; and computes both primitive
clearings over $\mathbb Z$.  Decimal logarithms and the value in (31) are
diagnostics only.

The package proves an exact affine quotient principle and one finite rational
upper-bound/denominator audit.  It proves neither an exact optimum for (13)
nor a uniform denominator obstruction.  It does not classify $e+\pi$.
