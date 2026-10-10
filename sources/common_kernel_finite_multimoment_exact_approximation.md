> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Finite rational-moment images and simultaneous native approximation

Checked: 2026-08-27 UTC.

## 1. Verdict

For integer polynomial weights $V_1,\ldots,V_m$, define



$$
{\boldsymbol L}(P)=
 \left(\int_0^1V_1(t)P(t)\,dt,\ldots,
       \int_0^1V_m(t)P(t)\,dt\right).                 \tag{1}
$$



This note gives a complete algebraic characterization:



$$
\boxed{
 {\boldsymbol L}(\mathbb Z[t])
 ={\boldsymbol L}(\mathbb Q[t]).}                     \tag{2}
$$



The right side is the rational subspace of $\mathbb Q^m$ determined by
all rational linear relations among the weights.  In particular,



$$
\boxed{
 V_1,\ldots,V_m\text{ linearly independent over }\mathbb Q
 \quad\Longleftrightarrow\quad
 {\boldsymbol L}(\mathbb Z[t])=\mathbb Q^m.}           \tag{3}
$$



The same conclusion holds after restricting $P$ to any prescribed
endpoint-zero ideal



$$
t^d(1-t)^d\mathbb Z[t].       \tag{4}
$$



Thus there is no finite-moment denominator or congruence obstruction hidden
in the use of ordinary integer coefficients.

There is also a simultaneous approximation theorem for two independent
native weights.  Let



$$
V_i(t)=(a_i+b_it)t(2-t)^2,\qquad
 a_i,b_i\in\mathbb Z_{\geq0},\quad a_i+b_i>0
 \quad(i=1,2),                                        \tag{5}
$$



and assume



$$
\Delta=a_1b_2-a_2b_1\ne0.    \tag{6}
$$



If $f\in C^\infty[0,1]$ has integral normalized endpoint jets through
order three and both moments



$$
L_i(f)=4\int_0^1V_i f         \tag{7}
$$



are rational, then there are $P_n\in\mathbb Z[t]$ with exactly the same
endpoint jets, exactly the same two moments, and



$$
\boxed{
 L_i(P_n)=L_i(f)\quad(i=1,2),\qquad
 \|P_n-f\|_{C^3[0,1]}\longrightarrow0.}               \tag{8}
$$



The proof uses the exact double kernel



$$
{\cal D}_V U=2V'U+VU',\qquad
 f={\cal D}_{V_1}{\cal D}_K U,\qquad
 K=V_2V_1'-V_1V_2'
 =-\Delta\,t^2(2-t)^4.                                \tag{9}
$$



For every finite pair of sign-possible native indices, a single smooth real
profile can satisfy both strict sign systems.  Its endpoint shapes can be
chosen on the integral jet lattice.  When the two native weights are
independent, (8) transfers that common real profile to a single integer
polynomial while preserving both rational output coordinates exactly.

This does **not** create a primitive-content gain.  For independent weights,
the two rational moments are locally freely variable; sharing one polynomial
forces no rational relation between them.  A common unreduced clearing
denominator exists, but its size is controlled by the very large polynomial
degree.  Eliminating $e+\pi$ between the two output forms introduces the
factorial ratio and destroys smallness.  No irrationality or transcendence
conclusion follows.

For arbitrary $m$, equation (3) is unconditional.  Simultaneous
moment-preserving approximation is proved here for two native weights, whose
cross-weight (9) has no interior zero.  A general Wronskian can vanish inside
$[0,1]$, making the natural inverse differential equation singular; no
unrestricted $m$-weight approximation theorem is claimed.

## 2. A Wronskian coordinate-isolation operator

We use the scalar fact proved in the preceding package:

> If $A\in\mathbb Z[t]$ is nonzero, then
> 

$$
> \left\{\int_0^1A(t)Q(t)\,dt:Q\in\mathbb Z[t]\right\}
> =\mathbb Q.                                         \tag{10}
>
$$



The conclusion remains true after replacing $Q$ by
$t^s(1-t)^sQ$, because the product weight remains a nonzero integer
polynomial.

Assume first that $V_1,\ldots,V_m$ are linearly independent.  Fix $j$,
list the other $m-1$ weights as $U_1,\ldots,U_{m-1}$, and define the
order-$(m-1)$ differential operator



$$
{\cal A}_j^*y=
 \operatorname {Wr}(U_1,\ldots,U_{m-1},y).             \tag{11}
$$



Expanding the determinant along its final column shows that
${\cal A}_j^*$ has coefficients in $\mathbb Z[t]$.  Let
${\cal A}_j$ be its formal adjoint.  If



$$
{\cal A}_j^*=\sum_{r=0}^{m-1}c_r(t)D^r,
 \qquad
 {\cal A}_j=\sum_{r=0}^{m-1}(-D)^r\circ c_r(t),        \tag{12}
$$



then repeated integration by parts gives



$$
\int_0^1Y\,{\cal A}_jQ
 =\int_0^1({\cal A}_j^*Y)Q                            \tag{13}
$$



whenever $Q$ and its derivatives through order $m-2$ vanish at both
endpoints.  Therefore



$$
\int_0^1V_i{\cal A}_jQ=0\quad(i\ne j),               \tag{14}
$$



whereas



$$
\int_0^1V_j{\cal A}_jQ
 =\int_0^1
 \operatorname {Wr}(U_1,\ldots,U_{m-1},V_j)Q.         \tag{15}
$$



The Wronskian in (15) is nonzero: over characteristic zero, the Wronskian
of linearly independent polynomials is nonzero.  By (10), with $Q$
restricted to an arbitrarily high endpoint-zero ideal, the last coordinate
in (15) takes every rational value.  Equations (14)--(15) isolate every
coordinate axis in $\mathbb Q^m$, proving (3).  Choosing the endpoint
order of $Q$ at least $m-1+d$ makes
${\cal A}_jQ$ divisible by $t^d(1-t)^d$, proving the version (4).

If the weights have rank $r<m$, select $r$ of them as a rational basis.
The independent case realizes every vector in $\mathbb Q^r$, and the
remaining coordinates are their fixed rational linear combinations.
This proves (2) and gives the exact obstruction: rational linear dependence
of the weights, and nothing else.

## 3. Initial simultaneous endpoint and moment correction

For the two-weight approximation theorem, let



$$
B_0=t^4(1-t)^4.               \tag{16}
$$



The endpoint CRT gives an $H\in\mathbb Z[t]$ matching the integral endpoint
jets of $f$ through order three.  By the endpoint-ideal form of (3),



$$
(L_1,L_2)(B_0\mathbb Z[t])=\mathbb Q^2.              \tag{17}
$$



Hence there is $R\in B_0\mathbb Z[t]$ with



$$
L_i(R)=L_i(f-H)\quad(i=1,2).  \tag{18}
$$



Set



$$
P_0=H+R,\qquad g=f-P_0.       \tag{19}
$$



Then



$$
g^{(j)}(0)=g^{(j)}(1)=0\quad(0\leq j\leq3),
 \qquad L_1(g)=L_2(g)=0.                              \tag{20}
$$



It remains to approximate this common kernel exactly.

## 4. The double native differential kernel

For every polynomial $V$, put



$$
{\cal D}_VU=2V'U+VU'.         \tag{21}
$$



Direct integration by parts gives



$$
\int_0^1V\,{\cal D}_VU=[V^2U]_0^1,                  \tag{22}
$$



and, for a second weight $Z$,



$$
\int_0^1Z\,{\cal D}_VU
 =[VZU]_0^1+
 \int_0^1(ZV'-VZ')U.                                  \tag{23}
$$



For the native weights (5), their cross-weight is



$$
K=V_2V_1'-V_1V_2'
 =(a_2b_1-a_1b_2)t^2(2-t)^4
 =-\Delta t^2(2-t)^4.                                \tag{24}
$$



It is nonzero on $0<t\leq1$, and has order two at zero.

Let



$$
\nu=\operatorname {ord}_0V_1=
 \begin{cases}
 1,&a_1>0,\\
 2,&a_1=0.
 \end{cases}                                          \tag{25}
$$



Starting from $g$ in (20), define



$$
S(t)=\frac{\int_0^tV_1(u)g(u)\,du}{V_1(t)^2}.        \tag{26}
$$



Exactly as in the single-moment argument, $S$ is smooth,



$$
{\cal D}_{V_1}S=g,\qquad
 S=t^{5-\nu}s_0=(1-t)^5s_1,                           \tag{27}
$$



and (23), (20), and the endpoint vanishing give



$$
\int_0^1KS=0.                \tag{28}
$$



Define a second inverse:



$$
U(t)=\frac{\int_0^tK(u)S(u)\,du}{K(t)^2}.            \tag{29}
$$



Then $U$ is smooth and



$$
{\cal D}_KU=S,\qquad
 U=t^{4-\nu}u_0=(1-t)^6u_1.                           \tag{30}
$$



Combining (27) and (30) proves the exact factorization in (9).

## 5. Weighted integer Bernstein approximation for the double kernel

Put



$$
r=4-\nu\in\{2,3\}.            \tag{31}
$$



Let



$$
U_n(t)=\sum_{k=0}^n
 \left\langle U(k/n){n\choose k}\right\rangle
 t^k(1-t)^{n-k}\in\mathbb Z[t].                       \tag{32}
$$



The endpoint orders in (30) imply, for all sufficiently large $n$,



$$
t^r(1-t)^6\mid U_n.           \tag{33}
$$



Write $E_n=U_n-U$.  The same normalized Bernstein calculation as in the
single-moment package gives, for $0\leq q\leq5$,



$$
\boxed{
 \left\|t^{\lambda_q}E_n^{(q)}\right\|_\infty
 \longrightarrow0,\qquad
 \lambda_q=\max\{0,\nu+q-3\}.}                        \tag{34}
$$



Here are the details.  Let $R_n$ denote the rounded error supported on
$r\leq k\leq n-6$, with raw Bernstein coefficients of absolute value at
most $1/2$.  Differentiation and normalization in the nonnegative
Bernstein basis give, for $q,\lambda\geq0$,



$$
\begin{aligned}
 \|t^\lambda R_n^{(q)}\|_\infty
 \leq{}&
 \frac{(n)_q}{2(n-q+1)_\lambda}
 \sum_{\alpha=0}^q{q\choose\alpha}\\
 &\times
 \max_{r\leq k\leq n-6}
 \frac{(k-\alpha+1)_\lambda}{{n\choose k}}.
\end{aligned}
$$



As before, invalid falling-factorial terms are absent, the first
$(n)_q$ is falling, and the two $\lambda$-factorials are rising.  For
$\lambda=\lambda_q$, the maximum is $O(n^{-r})$.  Indeed, at the left
endpoint its numerator is bounded and ${n\choose r}\asymp n^r$; at the
right endpoint it is



$$
O\!\left(\frac{n^{\lambda_q}}{{n\choose6}}\right)
 =O(n^{\lambda_q-6})=O(n^{-r}),
$$



because $(r,\lambda_q)$ is either
$(3,\lambda_q\leq3)$ or $(2,\lambda_q\leq4)$.
For a completely uniform interior bound, split the indices into thirds.
On $r\leq k\leq n/3$, the ratio of consecutive terms is less than one
for all sufficiently large $n$, so the left endpoint dominates.  On
$n/3\leq k\leq2n/3$, the binomial coefficient is exponentially large.
On $2n/3\leq k\leq n-6$, symmetry gives
${n\choose k}={n\choose n-k}\geq {n\choose6}$, while the numerator is
$O(n^{\lambda_q})$.  Thus no interior range exceeds the two endpoint
orders.  Therefore the rounded central channels contribute



$$
O\!\left(n^{q-r-\lambda_q}\right)=O(n^{-1}),         \tag{35}
$$



where the exponent is at most $-1$ by the definition of $\lambda_q$.

For completeness, the omitted left channel with fixed $k<r$ has classical
coefficient $O(n^{k-r})$.  Its $q$-th derivative, after multiplication
by $t^{\lambda_q}$, has norm
$O(n^{q-k-\lambda_q})$, so its product is again
$O(n^{q-r-\lambda_q})$.  At the right endpoint, write $k=n-h$ with
$h<6$.  The omitted coefficient is $O(n^{h-6})$, while the derivative
norm is $O(n^{q-h})$; their product is $O(n^{q-6})=O(n^{-1})$.
The classical Bernstein part converges simultaneously through derivative
five.  This proves (34), with no finite-degree extrapolation.

Now set



$$
G_n={\cal D}_{V_1}{\cal D}_KU_n.              \tag{36}
$$



The operator in (36) has the form



$$
{\cal D}_{V_1}{\cal D}_K
 =A_0(t)+A_1(t)D+A_2(t)D^2,                           \tag{37}
$$



where



$$
\begin{aligned}
 A_0&=4V_1'K'+2V_1K'',\\
 A_1&=2V_1'K+3V_1K',\\
 A_2&=V_1K.
\end{aligned}                                         \tag{38}
$$



At zero,



$$
\operatorname {ord}_0A_j\geq\nu+j
 \quad(j=0,1,2).                                      \tag{39}
$$



After three differentiations, the coefficient of $E_n^{(q)}$ therefore
has order at least $\lambda_q$.  Equations (34)--(39) prove



$$
\|G_n-g\|_{C^3[0,1]}\longrightarrow0.        \tag{40}
$$



The endpoint orders in (33) give



$$
t^4(1-t)^4\mid G_n.           \tag{41}
$$



Equations (22)--(24), applied twice, give the exact identities



$$
L_1(G_n)=L_2(G_n)=0.          \tag{42}
$$



Finally $P_n=P_0+G_n$ proves (8).

## 6. A common strict real sign profile

For a sign-possible native index $N_i$, write its parameters as
$a_i\geq0,b_i>0$.  In the $t=1-x$ coordinate, the residual is



$$
\begin{aligned}
 F_i(1-t)
 ={}&t^{N_i}+t(a_i+b_it)H'(t)\\
 &+\{a_i(1-t)+b_it(2-t)\}H(t).                        \tag{43}
\end{aligned}
$$



For $0<t<1$, put



$$
\begin{aligned}
 \alpha_i(t)&=
 \frac{a_i(1-t)+b_it(2-t)}{t(a_i+b_it)},\\
 \beta_i(t)&=\frac{t^{N_i-1}}{a_i+b_it}.
\end{aligned}                                         \tag{44}
$$



Then



$$
F_i(1-t)=t(a_i+b_it)
 \{H'+\alpha_iH+\beta_i\}.                            \tag{45}
$$



For finitely many indices let
$\alpha_*=\min_i\alpha_i$.  One has



$$
\lim_{t\downarrow0}t\alpha_*(t)
 \in\{1,2\}.                                          \tag{46}
$$



This nonintegrable $1/t$ allowance permits a common profile to descend
from one to an arbitrarily small value while obeying



$$
H'\geq-\alpha_*H.             \tag{47}
$$



Here is a precise smooth construction.  Near zero prescribe



$$
H(t)=1-4t^2.                 \tag{48}
$$



Choose $t_0>0$ so small that
$t\alpha_*(t)>\sigma/2$ on $(0,t_0]$, where
$\sigma$ is the limit in (46).  For a parameter
$\varepsilon<t_0/4$, make a smooth transition after (48), and then solve


$$
H'=-c(t)H,\qquad 0<c(t)<\alpha_*(t),
$$


with a smooth $c$ that equals $\sigma/(4t)$ on
$[2\varepsilon,t_0]$.  The transition can remain below $\alpha_*$
because the logarithmic derivative of (48) is $O(\varepsilon)$ at its
left end.  Since



$$
\int_{2\varepsilon}^{t_0}\frac{\sigma}{4t}\,dt
 =\frac{\sigma}{4}\log\frac{t_0}{2\varepsilon}
 \longrightarrow\infty,
$$



moving the transition toward zero makes $H$ arbitrarily small on any
fixed compact subinterval of $(0,1)$.

Now choose a small $\delta>0$.  Arrange that $c$ decreases smoothly to
zero before $1-2\delta$, still with $0\leq c<\alpha_*$.  The middle
solution is then constant, say $h_0$, on a neighborhood to the left of
$1-2\delta$.  By taking $\varepsilon$ sufficiently small, arrange
$0<h_0\leq\delta^2$.  On $[1-\delta,1]$ prescribe



$$
H(t)=(1-t)^2.                \tag{49}
$$



Let $\chi$ be a smooth flat cutoff on $[1-2\delta,1-\delta]$, equal to
zero near the left endpoint and one near the right endpoint, with
$0\leq\chi\leq1$ and $\|\chi'\|_\infty=O(\delta^{-1})$.  Define there



$$
H(t)=(1-\chi(t))h_0+\chi(t)(1-t)^2.
$$



This is a convex blend of positive functions and it glues smoothly to the
constant middle piece and to (49).  Throughout the bridge,



$$
H=O(\delta^2),\qquad H'=O(\delta).
$$



On $[1-2\delta,1]$, every $\beta_i$ has a positive lower bound and every
$\alpha_i$ is bounded.  These two displayed terms are therefore smaller
than the uniform $\beta_i$ margin when $\delta$ is small, so the bridge
preserves



$$
H'+\alpha_iH+\beta_i>0
 \quad\hbox{for every }i.                             \tag{50}
$$



The transition at zero is also strict because (46) dominates the bounded
derivative of (48).  The construction stays between zero and one and can be
made to satisfy



$$
H(0)=1,\quad H(1)=0,\quad0<H<1,\quad
 F_i(1-t)>0\quad(0<t<1).                              \tag{51}
$$



Put $v(t)=t^2-2t+2$ and



$$
q(t)=\frac{H(t)-1}{v(t)^2}.   \tag{52}
$$



The endpoint shapes (48)--(49) give



$$
q(t)=-t^2-2t^3+O(t^4),\qquad
 q(1-s)=-1+3s^2+O(s^4).                              \tag{53}
$$



Thus the normalized endpoint jets of $q$ through order three are integers.
For two independent weights, the ratio $V_1/V_2$ is nonconstant on
$(0,1)$.  Choose two interior points at which the vectors
$(V_1(t),V_2(t))$ are linearly independent.  Small disjoint neighborhoods
of those points support $C^\infty$ bump functions
$\phi_1,\phi_2$ for which the matrix



$$
\left(\int_0^1V_i(t)\phi_j(t)\,dt\right)_{i,j=1}^2
$$



is nonsingular.  The compact supports stay away from both endpoint
degeneracies.  The strict sign and $0<H<1$ inequalities have positive
margins on those supports, so every sufficiently small perturbation
$q+s_1\phi_1+s_2\phi_2$ remains strict and has the identical endpoint
germs.  Its two moments sweep an open neighborhood in $\mathbb R^2$.
Choose a rational pair in that neighborhood, obtaining a strict
$\widetilde q$ with both moments rational.  Apply (8) to
$\widetilde q$.  Because the strict inequalities survive and the endpoint
jets are preserved exactly, every sufficiently close integer approximant
gives one admissible polynomial localizer satisfying both sign systems.

If the two weights are dependent, their moment coordinates carry only one
degree of freedom, exactly as (2) predicts.  Common strict profiles still
exist by the same construction, but there is no two-coordinate arithmetic
problem.

## 7. Why shared denominators do not yet help

At a common strict profile, sufficiently small smooth perturbations with zero
endpoint jets preserve both sign systems.  When $V_1,V_2$ are independent,
the map



$$
\phi\longmapsto(L_1(\phi),L_2(\phi))         \tag{54}
$$



from zero-jet smooth perturbations onto $\mathbb R^2$ is surjective:
the endpoint-ideal version of (3) already supplies two polynomial coordinate
directions.  Hence the real attainable output pairs contain an open
two-dimensional neighborhood.  Rational pairs in that neighborhood can be
preserved exactly by (8), including pairs chosen on a common denominator
grid.

This local freedom is a no-go for any universal rational congruence between
the two outputs based only on sharing the polynomial.  It is not a
quantitative denominator theorem.  The radius of the strict neighborhood may
be extremely small, while every native output coordinate lies in a range of
width $O(1/N_i)$.

For a common reduced denominator $D$, the two positive forms have shape



$$
L_N=N!(e+\pi)+\frac{c_N}{D},\qquad
 L_M=M!(e+\pi)+\frac{c_M}{D}.                         \tag{55}
$$



If $M>N$, eliminating $e+\pi$ gives the integer



$$
D L_M-\frac{M!}{N!}D L_N
 =c_M-\frac{M!}{N!}c_N.                              \tag{56}
$$



But the raw upper bound for the left side contains the factorial multiple
$(M!/N!)L_N$; it is not small.  Conversely, the common monomial-integration
denominator obtained from a shared degree is an LCM growing exponentially in
that degree.  Neither operation gives $D=o(N)$, a large common numerator
gcd, or a primitive integer tending to zero.

Thus simultaneous exact moments remove a qualitative approximation obstacle
and prove common-profile existence.  They do not supply the quantitative
content needed for irrationality or transcendence.

## 8. Scope and replay

The rigorous all-parameter conclusions are:

* the complete finite-moment image characterization (2);
* full image $\mathbb Q^m$ for linearly independent integer weights;
* simultaneous exact-moment integer $C^3$ approximation for two independent
  native weights;
* existence of a common strict real, and then integer, sign profile for every
  sign-possible native pair;
* absence of any universal rational coupling arising solely from a shared
  polynomial.

The source does not claim a general approximation theorem across interior
zeros of arbitrary Wronskians.  It gives no effective degree, neighborhood
radius, denominator, or primitive-content bound, and it makes no arithmetic
classification of $e+\pi$.

From the research directory run

    python3 scripts/common_kernel_finite_multimoment_exact_approximation_certificate.py

The replay uses exact symbolic and rational CPU arithmetic and a $40$ GiB
RAM guard.  No accelerator is useful.
