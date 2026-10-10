> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Adjacent joint-output thin strips and the determinant no-go

Checked: 2026-08-27 UTC.

## 1. Verdict

Let $N<M$ be sign-possible native indices.  Write



$$
(1-i)^j=R_j+iI_j,\qquad
 a_j=-I_j\geq0,\qquad
 b_j=\frac{j!-R_j}{2}>0,\qquad
 \epsilon_j=\frac{a_j}{b_j},                          \tag{1}
$$



and put



$$
\mu_j(t)=t(a_j+b_jt)e^{-t},\qquad
 w_j(t)=e^{-t}t^j,\qquad
 B_j=\int_0^1w_j(t)\,dt.                              \tag{2}
$$



Here a *common sign profile* means one smooth function $H$ for which, for
both indices under consideration,



$$
G_j(0)=G_j(1)=0,\qquad 0<G_j<\mu_j,\qquad
 w_j+G_j'>0\quad(0<t<1),                              \tag{2a}
$$



with the native endpoint germs from the preceding exact-approximation
theorem.  In particular $0<H<1$ on $(0,1)$.  For such a profile define



$$
G_j=\mu_jH,\qquad
 {\cal L}_j(H)={\cal L}_j(0)-\int_0^1R'(t)G_j(t)\,dt, \tag{3}
$$



where



$$
R(t)=e+\frac{4e^t}{t^2-2t+2},\qquad
 R(0)=e+2,\quad R(1)=5e.                              \tag{4}
$$



Let ${\cal O}_{N,M}\subset\mathbb R^2$ be the set of joint output pairs
$({\cal L}_N(H),{\cal L}_M(H))$ over all common sign profiles.  Here
and below ``area'' may be read as Lebesgue outer area; no measurability of
the infinite-dimensional image is needed.

This note proves an all-parameter thin-strip theorem.  Put



$$
q=\frac{b_N}{b_M},\qquad
 T(H)={\cal L}_N(H)-q{\cal L}_M(H),\qquad
 C_0=4e-2,\qquad C_1=16e.                             \tag{5}
$$



For every $0<\tau\leq1$,



$$
\boxed{
 \begin{aligned}
 \operatorname {diam}{\cal L}_M({\cal O}_{N,M})
 &\leq C_0B_M,\\
 \operatorname {diam}T({\cal O}_{N,M})
 &\leq|\epsilon_N-\epsilon_M|
 \left\{
 \frac{C_1}{2}b_N\tau^2+
 \frac{2C_0qB_M}{\tau+\epsilon_M}
 \right\}.
 \end{aligned}}                                      \tag{6}
$$



The linear change



$$
(x,y)\longmapsto(x-qy,y)
$$



has determinant one.  Consequently



$$
\boxed{
 \operatorname {area}({\cal O}_{N,M})
 \leq C_0B_M\,\operatorname {diam}T({\cal O}_{N,M}).} \tag{7}
$$



Moreover the first coordinate itself obeys



$$
\boxed{
 \operatorname {diam}{\cal L}_N({\cal O}_{N,M})
 \le qC_0B_M+\operatorname {diam}T({\cal O}_{N,M}).} \tag{7a}
$$



The strip is also uniformly separated from its zero normal coordinate:



$$
\boxed{
 T(H)>\frac57B_N\geq\frac5{7e(N+1)}
 \qquad(N<M).}                                       \tag{7b}
$$



Thus near-dependence of the two native weights makes the entire joint output
set thinner but does not move it toward zero or enlarge the rational lattice
capacity.

For adjacent indices $M=N+1$, the asymptotic consequence is especially
strong.  Along any sign-possible adjacent subsequence,



$$
\operatorname {diam}T({\cal O}_{N,N+1})
 \ll
 \frac{2^{N/2}}{(N!)^{2/3}N^{4/3}},                   \tag{8}
$$





$$
\boxed{
 \operatorname {area}({\cal O}_{N,N+1})
 \ll
 \frac{2^{N/2}}{(N!)^{2/3}N^{7/3}}.}                 \tag{9}
$$



The hidden obstruction is positional.  For the infinite adjacent classes



$$
N\equiv0,1,2\pmod8,           \tag{10}
$$



one has $\mu_{N+1}\geq\mu_N$, and every common profile satisfies



$$
\boxed{
 {\cal L}_N(H)-{\cal L}_{N+1}(H)>D_N^0,
 \quad
 D_N^0:=\int_0^1R(t)e^{-t}t^N(1-t)\,dt
 \sim\frac5{N^2}.}                                   \tag{11}
$$



Thus $D_N^0$ is the infimum, approached by strict profiles only from the
positive side.  Under a temporary rationality hypothesis, a common
denominator $D$ makes



$$
D\{{\cal L}_N-{\cal L}_{N+1}\}\in\mathbb Z_{>0}.     \tag{12}
$$



Therefore a profile whose adjacent difference is $O(N^{-2})$ necessarily
has $D\gg N^2$, the opposite of the desired $D=o(N)$.

There is also an even more basic conditional denominator floor.  If
$e+\pi\in\mathbb Q$, once its denominator divides $N!$, positivity and
${\cal L}_N<5e/(N+1)$ imply that any $D$ for which
$D{\cal L}_N\in\mathbb Z$ satisfies



$$
\boxed{D>\frac{N+1}{5e}.}                           \tag{12a}
$$



This explains why real output geometry alone cannot select a positive
rational output with $D=o(N)$.  It does **not** rule out an arithmetic
construction forcing such a denominator: under the temporary rationality
hypothesis that would be a contradiction and hence an irrationality proof.

Finally, the unique primitive integer direction that cancels the two
factorial coefficients is centered far from zero.  If $M>N$ and
$r=M!/N!$, then for every $N\geq14$,



$$
\boxed{
 r{\cal L}_N(H)-{\cal L}_{M}(H)
 \geq\frac{e+2}{2e}>0.}                               \tag{13}
$$



For adjacent indices its variation across the entire common output set is
factorially small, but the quantity itself is bounded away from zero.  For
larger gaps the lower bound remains valid.  Multiplying it by a common
denominator produces a large integer, not a primitive contradiction.

Equations (6)--(13) give a scoped convex-geometric no-go: adjacent
near-dependence
creates a very small area and a very thin determinant direction, but the
only $O(N^{-2})$ direction lies in a one-sided Farey gap, while the
factorial-cancel direction misses zero by a fixed amount.  No $o(N)$
denominator or primitive integer tending to zero follows from the two-output
width, area, or these determinant directions.  This is not an impossibility
theorem for every conceivable arithmetic use of two outputs.  This note does
not prove that $e+\pi$ is irrational or transcendental.

## 2. Fixed mass and variation bounds

For every native sign profile,



$$
\nu_j=w_j+G_j'>0,\qquad
 \int_0^1\nu_j=B_j,\qquad
 {\cal L}_j(H)=\int_0^1R(t)\nu_j(t)\,dt.              \tag{14}
$$



Since $R$ is increasing from $e+2$ to $5e$,



$$
(e+2)B_j<{\cal L}_j(H)<5eB_j.                       \tag{15}
$$



Also, (3) gives



$$
0\leq\int_0^1R'G_j
 ={\cal L}_j(0)-{\cal L}_j(H)
 \leq(4e-2)B_j=C_0B_j.                               \tag{16}
$$



If $H_0,H_1$ are two common profiles and
$\delta G_j=\mu_j(H_1-H_0)$, then $G_j\geq0$ gives



$$
\boxed{
 \int_0^1R'|\delta G_j|
 \leq2C_0B_j.}                                       \tag{17}
$$



Finally, direct differentiation of (4) gives



$$
R'(t)=\frac{4e^t(2-t)^2}{(t^2-2t+2)^2},
 \qquad0<R'(t)\leq16e=C_1.                            \tag{18}
$$



We also need a uniform coefficient-ratio bound.  For every $N\geq2$,



$$
b_{N+1}\geq\frac72b_N.        \tag{18a}
$$



The cases $N=2,3$ are $(b_2,b_3,b_4)=(1,4,14)$.  For $N\geq4$,



$$
2\{2b_{N+1}-7b_N\}
 =(2N-5)N!+7R_N-2R_{N+1}>0.
$$



Indeed



$$
|7R_N-2R_{N+1}|
 \leq(7+2\sqrt2)2^{N/2}<10\,2^{N/2}<(2N-5)N!;
$$



the last inequality starts at $N=4$, and the factorial side then grows by
more than the factor $\sqrt2$ of the exponential side.

It follows that for every $M>N$,



$$
q=\frac{b_N}{b_M}\leq\frac27.                       \tag{18b}
$$



Since $B_M<B_N$, equations (15) and (18b), together with $e<3$, give



$$
\begin{aligned}
 T(H)&>(e+2)B_N-5eqB_M\\
 &>\left(2-\frac{3e}{7}\right)B_N
 >\frac57B_N\geq\frac5{7e(N+1)}.
                                                               \tag{18c}
\end{aligned}
$$



This proves (7b) for every pair, without a residue-class restriction.

These are the only global sign-family estimates needed for the strip
theorem.

## 3. Exact thin-coordinate identity

For two common profiles write $\delta H=H_1-H_0$.  From (2),



$$
\begin{aligned}
 \delta G_N-q\delta G_M
 &=t e^{-t}
 \{a_N+b_Nt-q(a_M+b_Mt)\}\delta H\\
 &=b_N(\epsilon_N-\epsilon_M)t e^{-t}\delta H.         \tag{19}
\end{aligned}
$$



Split the integral for $\delta T$ at $\tau$.  Since
$|\delta H|\leq1$, equations (18)--(19) give on $0\leq t\leq\tau$



$$
|\delta T_{\rm early}|
 \leq\frac{C_1}{2}b_N|\epsilon_N-\epsilon_M|\tau^2.   \tag{20}
$$



On $t\geq\tau$, use instead



$$
\delta G_N-q\delta G_M
 =
 q\,\frac{\epsilon_N-\epsilon_M}{t+\epsilon_M}
 \delta G_M.                                         \tag{21}
$$



Equation (17) gives



$$
|\delta T_{\rm late}|
 \leq
 \frac{2C_0q|\epsilon_N-\epsilon_M|B_M}
 {\tau+\epsilon_M}.                                   \tag{22}
$$



Equations (20)--(22) prove the second line of (6).  The first line is (15).
The image of ${\cal O}_{N,M}$ under
$(x,y)\mapsto(x-qy,y)$ lies in a rectangle with precisely these two
diameter bounds, proving (7).

The exact-dependence edge case is worth isolating.  If
$\epsilon_N=\epsilon_M$, then (19) makes $T$ profile-independent and



$$
T(H)=T(0)
 =\int_0^1R(t)e^{-t}\{t^N-qt^M\}\,dt>0.              \tag{22a}
$$



Indeed $b_M>b_N$, hence $0<q<1$, while $0<t<1$ and $M>N$.
Thus the most degenerate joint set has area zero but lies on an affine line
which misses the zero normal coordinate.  In particular, choosing two
indices with $a_N=a_M=0$ does not create a vanishing determinant.

Finally $\delta{\cal L}_N=q\delta{\cal L}_M+\delta T$.  Taking
suprema over pairs of profiles proves (7a).

Dropping $\epsilon_M$ from the denominator and optimizing
$A\tau^2+B/\tau$ gives, whenever the optimizer is at most one,



$$
\operatorname {diam}T
 \ll
 |\epsilon_N-\epsilon_M|\,
 b_N^{1/3}(qB_M)^{2/3}.                               \tag{23}
$$



All implied constants here and below are absolute.

## 4. Adjacent asymptotics and anisotropy

The Gaussian power satisfies



$$
|R_j|,a_j\leq2^{j/2}.
$$



Consequently



$$
b_j=\frac{j!}{2}
 \left\{1+O\left(\frac{2^{j/2}}{j!}\right)\right\},
 \qquad
 \epsilon_j=O\left(\frac{2^{j/2}}{j!}\right).         \tag{24}
$$



For $M=N+1$,



$$
q=\frac1{N+1}\{1+o(1)\},\qquad
 B_M\sim\frac1{e(N+1)},                               \tag{25}
$$



and



$$
|\epsilon_N-\epsilon_M|
 \ll\frac{2^{N/2}}{N!}.                               \tag{26}
$$



Substitution of (24)--(26) into (23) proves (8).  Multiplication by the broad
width $C_0B_M\ll1/N$ proves (9).

It is useful to record the anisotropy explicitly:



$$
\frac{\operatorname {diam}T}
 {C_0B_M}
 \ll
 \frac{2^{N/2}}{(N!)^{2/3}N^{1/3}}.                  \tag{27}
$$



Thus the aspect ratio of the certified enclosing rectangle tends to zero
faster than exponentially.  A
two-dimensional rational-grid or determinant argument has less effective
volume here than in a hypothetical $N^{-1}$-by-$N^{-1}$ box.

Equation (7a) also records the axis anisotropy which the determinant-one
coordinates hide:



$$
\operatorname {diam}{\cal L}_N({\cal O}_{N,N+1})
 \leq \frac{C_0+o(1)}{eN^2}
 +O\left(\frac{2^{N/2}}{(N!)^{2/3}N^{4/3}}\right).   \tag{27a}
$$



Thus the lower-index coordinate has only $O(N^{-2})$ common-profile
freedom, while the upper-index coordinate has $O(N^{-1})$ freedom.

## 5. The one-sided adjacent difference

For the adjacent residue classes in (10), the explicit Gaussian powers give



$$
a_{N+1}\geq a_N.              \tag{28}
$$



Also $b_{N+1}>b_N$ for every $N\geq2$.  Indeed,



$$
2(b_{N+1}-b_N)
 =N\,N!+R_N-R_{N+1}.                                 \tag{29}
$$



For $N=2$, positivity is immediate from $b_2=1,b_3=4$.  For
$N\geq3$,


$$
|R_N-R_{N+1}|
 \leq2^{N/2}+2^{(N+1)/2}<N\,N!.
$$



The last strict inequality starts at $N=3$ and propagates: its left side
is multiplied by $\sqrt2$ when $N$ increases by one, while its right
side is multiplied by $(N+1)^2/N>\sqrt2$.

Thus $\mu_{N+1}\geq\mu_N$.  Subtracting (3) gives



$$
\begin{aligned}
 {\cal L}_N(H)-{\cal L}_{N+1}(H)
 ={}&{\cal L}_N(0)-{\cal L}_{N+1}(0)\\
 &+\int_0^1R'(t)\{\mu_{N+1}(t)-\mu_N(t)\}H(t)\,dt.
                                                               \tag{30}
\end{aligned}
$$



The first difference is



$$
{\cal L}_N(0)-{\cal L}_{N+1}(0)
 =\int_0^1R(t)e^{-t}t^N(1-t)\,dt.                    \tag{31}
$$



Equations (30)--(31) prove the strict inequality in (11).  The looser
elementary bound



$$
D_N^0\geq(e+2)(B_N-B_{N+1})                         \tag{32}
$$



is sometimes useful, but it is not the exact boundary.  The same substitution
$t=1-y/N$, followed by dominated convergence, gives



$$
N^2D_N^0\longrightarrow
 R(1)\int_0^\infty ye^{-y-1}\,dy=5.                 \tag{32a}
$$



The common strict-profile construction can move both endpoint transition
neighborhoods arbitrarily close to the endpoints and make $H$ arbitrarily
small on the intervening compact interval.  Since
$\mu_{N+1}-\mu_N$ is integrable, the second term in (30) can therefore be
made arbitrarily small for each fixed $N$.  Thus $D_N^0$, rather than
the weaker right side of (32), is the true infimum, approached only from
above.

Suppose temporarily that $e+\pi\in\mathbb Q$, and let $D$ clear both
rational output coordinates of one common integer profile.  For all
sufficiently large $N$,



$$
X_j=D{\cal L}_j(H)\in\mathbb Z_{>0}.
$$



Equation (11) gives



$$
X_N-X_{N+1}=D\{{\cal L}_N-{\cal L}_{N+1}\}
 \in\mathbb Z_{>0}.                                   \tag{33}
$$



In particular,



$$
D\geq
 \frac1{{\cal L}_N-{\cal L}_{N+1}}.                   \tag{34}
$$



Profiles within a fixed multiple of the infimum (11) therefore require
$D\gg N^2$.  The tempting $O(N^{-2})$ analytic difference is exactly a
one-sided rational gap, not a small primitive integer.

Independently of monotonicity or adjacency, (15) and $B_N\le1/(N+1)$
give



$$
0<{\cal L}_N(H)<\frac{5e}{N+1}.                     \tag{34a}
$$



If $D{\cal L}_N$ is a positive integer, then it is at least one, and
(34a) proves (12a).  Thus, within the temporary rationality setup, the
conditional floor applies to every pair.  Forcing a smaller denominator by
an independent arithmetic construction would contradict that hypothesis;
the present geometric bounds do not supply such a construction.

## 6. The unique factorial-cancel direction

Let $M>N$, put $r=M!/N!$, and write



$$
C(H)={\cal L}_{M}(H)-r{\cal L}_N(H).        \tag{35}
$$



The universal range (15) and the elementary bounds



$$
B_N\geq\frac1{e(N+1)},\qquad
 B_M\leq\frac1{M+1},\qquad r\geq N+1
$$



give



$$
\begin{aligned}
 r{\cal L}_N-{\cal L}_{M}
 &\geq r(e+2)B_N-5eB_M\\
 &\geq\frac{e+2}{e}-\frac{5e}{M+1}\\
 &\geq\frac{e+2}{e}-\frac{5e}{N+2}
 \geq\frac{e+2}{2e}\qquad(N\geq14).                  \tag{36}
\end{aligned}
$$



This proves (13).  The native rational output has the form



$$
{\cal L}_j=j!s+\rho_j,qquad s=e+\pi,       \tag{36a}
$$



with $\rho_j\in\mathbb Q$ for an integer profile.  If
$u{\cal L}_N+v{\cal L}_M$ cancels $s$, then
$uN!+vM!=0$.  After division by the coefficient gcd, the only choices are
$(u,v)=\pm(r,-1)$.  Equation (36) proves that this unique primitive
cancellation direction is separated from zero for every pair.

For adjacent indices, near-dependence does make the *variation* of $C$
tiny.  From now to (39), set $M=N+1$, so $r=N+1$.  The exact identity



$$
C=(1-rq){\cal L}_{N+1}-rT,\qquad
 1-rq=\frac{b_{N+1}-rb_N}{b_{N+1}}                   \tag{37}
$$



and



$$
b_{N+1}-rb_N
 =\frac{rR_N-R_{N+1}}2                               \tag{38}
$$



give



$$
\operatorname {diam}C
 \leq
 \frac{|rR_N-R_{N+1}|}{2b_{N+1}}\,C_0B_{N+1}
 +r\,\operatorname {diam}T.                          \tag{39}
$$



Equations (8), (24), and (39) show that
$\operatorname {diam}C$ is factorially small.  But (36) shows that this
thin strip is centered a fixed distance from zero.

Under the temporary rationality hypothesis,



$$
D C=X_{N+1}-rX_N\in\mathbb Z.
$$



By (36), its magnitude is at least
$(e+2)D/(2e)$.  This is a large integer, so factorial cancellation does
not produce a primitive small value.

## 7. Common denominators and the convex-lattice limitation

Under the temporary rationality hypothesis, the joint exact-moment theorem
allows rational points in every sufficiently small open patch of the real
output set.  It gives no effective lower bound for the patch widths.  A
naive grid in the determinant-one *real* coordinates of (6) would have to
resolve the thin width, not its broad width, so (8) would worsen its
denominator.  Such a grid is not yet an integer-lattice argument because
$q$ need not be integral; (41)--(42) below make the normalization explicit.

Area alone cannot repair this.  Rational points of common denominator at
most $Q$ have one-sided major gaps next to rational affine lines.  For
coprime integers $p,q$, the strip



$$
0<qx-py<\frac1Q                                      \tag{40}
$$



contains no rational pair $(x,y)=(A/d,B/d)$ with $d\le Q$: its middle
quantity, if nonzero, has magnitude at least $1/d\ge1/Q$.  Yet (40) has
arbitrarily large length in the tangential direction.
Thus no translation-independent denominator upper bound follows from area
or anisotropy alone.

There is also a normalization trap in the analytically thinnest coordinate.
Write



$$
g=\gcd(b_N,b_M),\qquad
 U=\frac{b_M}{g}{\cal L}_N-\frac{b_N}{g}{\cal L}_M
   =\frac{b_M}{g}T.                                  \tag{41}
$$



The vector in (41), not $(1,-q)$, is the primitive integer normal.  Thus
the thin width relevant to an integer determinant is exactly
$(b_M/g)\operatorname {diam}T$, and any gain depends on the arithmetic
content $g$.  In the adjacent case,



$$
g\mid b_{N+1}-(N+1)b_N
   =\frac{(N+1)R_N-R_{N+1}}2,                         \tag{42}
$$



whose right side is nonzero in every residue class modulo eight.  Hence
$g=O(N2^{N/2})$, while $b_{N+1}\asymp(N+1)!$.  Passing to the primitive
integer normal therefore multiplies the analytic thin coordinate by a
factor at least of factorial-over-exponential size.  More decisively, (7b)
gives the all-pair positional bound



$$
U>\frac{5b_M}{7eg(N+1)}.                            \tag{42a}
$$



For adjacent indices the right side grows at factorial-over-exponential
scale, so the primitive analytic normal itself is far from zero.  In
addition, simply
multiplying the upper bound (8) by the required normalization does not yield
an upper bound tending to zero: the resulting right-side scale is at least



$$
\frac{b_{N+1}}g
 \frac{2^{N/2}}{(N!)^{2/3}N^{4/3}}
 \gg\frac{(N!)^{1/3}}{N^{7/3}}.                      \tag{43}
$$



This does not prove that the actual
primitive-coordinate width is large; it proves that the small real width
(8), by itself, is insufficient.

In the actual adjacent set, equations (33)--(34) identify the relevant major
gap exactly: the closest nonzero rational value of
${\cal L}_N-{\cal L}_{N+1}$ with denominator $D$ has magnitude at least
$1/D$.  Meanwhile (36) excludes zero in the factorial direction.  These
two facts dispose of the two natural determinant candidates: the adjacent
difference and the unique factorial-cancel direction.  They do not rule out
an additional arithmetic identity involving numerator content.

The shared polynomial does give a common unreduced harmonic clearing
denominator, but its logarithm is proportional to the very large polynomial
degree.  Nothing in the strip theorem couples that denominator to numerator
content.  Hence the simultaneous-output construction yields no
$D=o(N)$, no useful common gcd, and no primitive contradiction.

## 8. Scope and replay

The all-parameter conclusions are the strip and coordinate bounds
(6)--(7a), the positive invariant line in the exact-dependence case (22a),
the area and anisotropy estimates (8)--(9), the one-sided adjacent theorem
(11), the conditional common-denominator floor (12a), and the
all-pair factorial-direction obstruction (13), with the adjacent variation
ledger (39).  The numerical tables in the replay only illustrate their exact
finite values.

The monotone adjacent theorem is asserted for the residue classes (10);
the transition $N\equiv3\pmod8$ has $a_{N+1}<a_N$ and is not covered by
(11).  The general strip theorem still applies to it.

No effective rational patch, primitive-content estimate, irrationality
proof, or transcendence proof is claimed.

The replay pins the frozen dependencies

    results/common_kernel_native_sign_output_range_sharp_width_hashes.sha256
    results/common_kernel_finite_multimoment_exact_approximation_hashes.sha256

From the research directory run

    python3 scripts/common_kernel_adjacent_joint_output_thin_strip_certificate.py

The replay uses exact symbolic and rational CPU arithmetic, no accelerator,
and a $40$ GiB RAM guard.
