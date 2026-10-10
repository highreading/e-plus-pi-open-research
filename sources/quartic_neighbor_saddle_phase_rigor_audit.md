> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Adversarial rigor audit of the quartic neighboring-power saddle argument

Date: 2026-08-27.

## 1. Verdict and hypotheses

This note audits the previously frozen source
`quartic_neighbor_saddle_phase_barrier.md`, concentrating on its Lemma 4.1,
the three-power Hankel minor, the positive integer-kernel construction, and
the whole-line tail estimate.  The audit found and repaired two genuine
proof-presentation gaps.  First, the old power bound at infinity discarded
the factor `2^(-k)` and therefore did not, as written, prove comparison
with the complex saddle; equation (A12) below supplies the required bound.
Second, the later tail argument omitted the permitted case `c=0`, for which
the chosen kernel is simply `P(Q)=1`; Section 5 now treats it separately.
No counterexample or missing asymptotic hypothesis was found.  The
following hypotheses are essential and are now made explicit:



$$
n\longrightarrow\infty,\qquad
 r=(4k/n)^{-1/4}\longrightarrow0,\qquad
 nr^{10}\longrightarrow\infty.                               \tag{A1}
$$



The last condition is needed only for the uniform sign of the three-power
minor and the perturbation of its real roots.  It holds for
`k` in every fixed positive multiple of `n log n`.  The audit does not
promote any bounded scan to an all-parameter theorem, and it does not turn
the symmetric analytic obstruction into a quadratic-field primitive-content
theorem.

## 2. Pole-free homology and the uniform saddle error

After `y=ru`, the complex integral is



$$
I_{n,k}=r^{n+1}\int_0^\infty e^{n\psi_i(u;r)}\,du,
$$



where



$$
\psi_i(u;r)=\log u+\log(1+iru)
 -\frac1{4r^4}\log(1+r^4u^4).                                \tag{A2}
$$



Fix a sufficiently small `epsilon>0` and a rectangle



$$
\mathcal R=\{1/2\leq\operatorname {Re}u\leq2,
                 |\operatorname {Im}u|\leq\epsilon\}.         \tag{A3}
$$



For all sufficiently small `r`, the zero of `1+iru` and all four zeros of
`1+r^4u^4` have modulus `1/r`, and hence lie outside this rectangle.  The
integer-powered integrand is holomorphic on and inside every contour used
below.  A single analytic logarithm may therefore be chosen on the
rectangle for purposes of steepest descent; the final integrand itself has
no branch ambiguity.

At `r=0`,



$$
\psi_0(u)=\log u-u^4/4,
$$



and the only critical point in (A3) is `u=1`, with
`-psi_0''(1)=4`.  Choose `delta>0` so small that the disk
`|u-1|<=2delta` lies in the rectangle.  On the two real compact pieces



$$
[1/2,1-\delta]\cup[1+\delta,2]
$$



there is a constant `gamma_delta>0` such that



$$
\operatorname {Re}\psi_0(u)\leq-1/4-\gamma_\delta.           \tag{A4}
$$



Uniform convergence of the phase and its first four derivatives on the
rectangle preserves half this gap for small `r`.  The analytic implicit
function theorem gives the unique critical point `u_i(r)` in
`|u-1|<delta`.  The analytic Morse lemma supplies a local coordinate `w`,
depending analytically on `r`, in which



$$
\psi_i(u;r)=\psi_i(u_i;r)-w^2/2.                              \tag{A5}
$$



Take the real `w` segment through zero and map it back to the `u` plane.
It is a `C^1`, `O(r)` perturbation of the real segment through one.  Continue
it until it meets the vertical lines through `1-delta` and `1+delta`, and
use the two vertical segments back to the real axis as connectors.  Their
length is `O(r)`.  Together with the unchanged outer compact pieces, this
is homologous relative to its endpoints to `[1/2,2]` in the pole-free
rectangle.  The connectors remain `O(r)`-close to the real endpoints in
the fixed-gap region (A4).  Thus this deformation neither crosses a
quartic pole nor silently rotates an infinite ray.  Notice that this
`O(r)` control is essential: an arbitrary connector in the rectangle need
not lie below the saddle because a harmonic real part has no interior
maximum.

The Gaussian expansion on the real `w` segment has coefficients uniformly
bounded for small `r`, because `-psi_i''(u_i;r)` tends to four and the
required phase derivatives are uniformly bounded.  It follows that



$$
I_{n,k}=r^{n+1}e^{n\psi_i(u_i;r)}
 \sqrt{\frac{2\pi}{-n\psi_i''(u_i;r)}}
 \left(1+O(n^{-1})\right),                                   \tag{A6}
$$



with an absolute constant after `r` is restricted to a fixed sufficiently
small interval.  The same proof works with any of the three fixed analytic
amplitudes `(1+r^4u^4)^(-s)`, `s=0,1,2`.

It remains to check that the infinite tails are small relative to the
complex saddle rather than merely relative to the real-axis maximum.  On
the real ray put



$$
h_r(u)=\log u+\frac12\log(1+r^2u^2)
 -\frac1{4r^4}\log(1+r^4u^4).                                \tag{A7}
$$



Its unique maximum follows from the one-sign-change polynomial



$$
1+2t+(1-4\kappa)t^2+(2-4\kappa)t^3,
 \qquad t=y^2,\quad\kappa=k/n.                              \tag{A8}
$$



More explicitly,



$$
h_0(1/2)=\log(1/2)-1/64<-1/4,
 \qquad h_0(2)=\log2-4<-1/4.                                 \tag{A9}
$$



Meanwhile



$$
\operatorname {Re}\psi_i(u_i;r)=-1/4+3r^2/8+O(r^4).        \tag{A10}
$$



For `2<=u<=1/r`,



$$
u h_r'(u)
 =1+\frac{r^2u^2}{1+r^2u^2}
   -\frac{u^4}{1+r^4u^4}\leq2-u^4/2\leq-6,                  \tag{A11}
$$



For the remaining ray define



$$
H(y)=\log y+\frac12\log(1+y^2)-(k/n)\log(1+y^4).
$$



For `y>=1`,



$$
yH'(y)\leq2-2k/n,
 \qquad
 \int_1^\infty e^{nH(y)}\,dy
 \leq\frac{2^{n/2-k}}{2k-2n-1}.                            \tag{A12}
$$



This retains the indispensable endpoint factor `2^(-k)`; the cruder bound
`2^(n/2)y^(2n-4k)` would not by itself compare correctly with the saddle.
The logarithm of (A12), divided by the saddle magnitude, is at most



$$
-k\log2+\frac{n+1}{4}\log(4k/n)+O(n+\log k).               \tag{A12a}
$$



The right-hand side tends to `-infinity` faster than `-c n` under (A1),
because `k/n -> infinity`.  The lower tail is
bounded by monotonicity up to `u=1/2`.  Equations (A9)--(A12) therefore show
that both tails are `O(exp(-c n))` relative to (A10).  This closes the only
global-contour issue in Lemma 4.1.

## 3. Absolute error in the Hankel minor

Let



$$
Z=M e^{i\theta},\qquad
 g=(1+y_i^4)^{-1}=\rho e^{i\eta}.
$$



Applying (A6) with the three amplitudes gives, with *absolute* errors,



$$
I_{n,k+s}=Z\big(g^s+\varepsilon_s\big),
 \qquad |\varepsilon_s|\leq C/n,
 \qquad s=0,1,2.                                             \tag{A13}
$$



This formulation remains valid when one of the real projections is close
to zero; no relative error in `L_s` is asserted.  Since



$$
\big(\operatorname {Re}(Zg)\big)^2
 -\operatorname {Re}(Z)\operatorname {Re}(Zg^2)
 =M^2\rho^2\sin^2\eta,                                      \tag{A14}
$$



and `|g|` stays bounded above and below, expanding the determinant in
(A13) yields



$$
L_1^2-L_0L_2
 =\frac8{\pi^2}M^2\rho^2
 \left(\sin^2\eta+O(n^{-1})\right).                          \tag{A15}
$$



The exact multiplier expansion gives



$$
\eta=-r^5+O(r^7),
 \qquad
 \sin^2\eta=r^{10}+O(r^{12}).                               \tag{A16}
$$



Thus (A1), and specifically `n r^10 -> infinity`, makes the leading term
strictly dominate the absolute error uniformly in `theta`.  This verifies
the passage from (41) to (43), including the worst phase where one or more
individual `L_s` are small.

## 4. Roots, rational grid, and coefficient height

Before the `O(1/n)` perturbation, scale away the common positive factor and
write



$$
q_s=\rho^s\cos(\theta+s\eta).
$$



The roots of `q_0-2q_1t+q_2t^2` are



$$
t_\pm=
 \frac{\cos(\theta+\eta)\mathbin\pm|\sin\eta|}
      {\rho\cos(\theta+2\eta)}.                              \tag{A17}
$$



Writing `A=theta+2eta` and choosing the sign for which



$$
|\sin A\mathbin\pm1|=1-|\sin A|
 =\frac{\cos^2A}{1+|\sin A|}\leq|\cos A|                    \tag{A18}
$$



shows, including the limiting case by continuity, that one root satisfies



$$
|\rho t_\pm-1|\leq1-\cos\eta+|\sin\eta|\leq2|\eta|.    \tag{A19}
$$



At either pure root the derivative magnitude is exactly
`2 rho |sin eta|`.  The coefficient perturbation in (A13) changes the
polynomial by `O(1/n)` on every fixed bounded interval.  Hence the stable
root moves by



$$
O\big((n|\eta|)^{-1}\big)=o(|\eta|)                         \tag{A20}
$$



under (A1).  If the exact third coefficient is zero, the constant kernel
`P(Q)=1` finishes the construction and no two-root argument is needed.
Assume henceforth in this section that it is nonzero.  Then (A15) and the
uniform upper bound on the three coefficients imply that the exact root
interval has length at least `c |eta|`.

After scaling the exact rational vector to primitive integers `(a,b,c)`,
neither its roots nor their interval changes.  Starting at the bounded
stable root, move into the root interval by distances between fixed small
multiples of `|eta|`.  Because the full separation is at least a fixed
multiple of `|eta|`, this produces an inner interval of length
`c_0|eta|` which stays `c_0|eta|` from both roots and remains in a fixed
bounded set.  Taking one fixed denominator



$$
v=\left\lceil\frac{2}{c_0|\eta|}\right\rceil                \tag{A21}
$$



places a grid point `u/v` in that interval; reducing `gcd(u,v)` only lowers
the denominator.  Therefore



$$
v=O(|\eta|^{-1}),\qquad |u|=O(v).                            \tag{A22}
$$



For



$$
(C_0,C_1,C_2)=\operatorname {sgn}(c)(cv,-2cu,-av+2bu),      \tag{A23}
$$



one has the exact kernel identity and



$$
P(Q)=\operatorname {sgn}(c)v\{c(Q-u/v)^2-f(u/v)\}>0.        \tag{A24}
$$



The two root distances give



$$
\frac{\min P}{|c|v}=-\frac{f(u/v)}c\geq c_1\eta^2,         \tag{A25}
$$



while (A22) gives



$$
\max|C_j|\leq C H|\eta|^{-1}=O(Hr^{-5}).                   \tag{A26}
$$



The omitted `c=0` branch uses `(0,0,1)` as its positive kernel.  These
estimates are unchanged by dividing the coefficient vector by its integer
content.

## 5. Infinite-tail ratio for the symmetric form

If the third primitive logarithmic coordinate is zero, the construction
uses `P(Q)=1`, and all tail comparisons below hold with no loss.  In the
remaining case write the positive quadratic as



$$
P(Q)=A(Q-t)^2+m,qquad A,m>0,qquad |t|\leq C,qquad
 m/A\geq c\eta^2.                                           \tag{A27}
$$



Then, for `Q>=1`,



$$
\frac{P(Q)}m\leq1+C\eta^{-2}(1+Q^2).                       \tag{A28}
$$



The main negative-half interval is bounded from below without invoking a
delicate saddle remainder.  On



$$
r\leq y\leq r(1+1/n),
$$



one has, uniformly in a fixed critical window,



$$
\frac{[y(1+y)]^n}{(1+y^4)^{k+2}}
 \geq r^n e^{-Cn}.                                           \tag{A29}
$$



The interval has length `r/n`, so its logarithm is



$$
-\frac n4\log(4k/n)+O(n).                                  \tag{A30}
$$



For `y>=1`, put



$$
\phi(y)=\log y+\log(1+y)-(k/n)\log(1+y^4).
$$



Then



$$
y\phi'(y)\leq2-2k/n,
$$



and hence



$$
\int_1^\infty e^{n\phi(y)}\,dy
 \leq\frac{2^{n-k}}{2k-2n-1}.                               \tag{A31}
$$



Using (A28) absorbs its `Q^2` into the two spare denominator powers.  The
positive tail is no larger than the negative one because
`(y-1)^n<=(y+1)^n`.  Dividing (A31) by (A29) proves



$$
\frac{\int_{|x|>1}F(x)\,dx}{\int_{-1}^{1}F(x)\,dx}
 \leq \eta^{-2}\exp\left(
 -(k-n)\log2+\frac n4\log(4k/n)+O(n)\right)=o(1).            \tag{A32}
$$



Thus (65) is uniform and does not hide a coefficient-height factor.

## 6. Remaining limitation

The audit confirms the analytic statements and the positive integer-kernel
construction.  It also confirms the limitation already stated in the main
source: the symmetrized coefficient pair lies in `Q(sqrt(2))`.  The
scale-invariant ratio `Lambda/B -> 2 pi` is an analytic same-sign barrier,
not by itself a bound on the final ideal content of a fully primitive
coefficient-matched algebraic integer.  No classification of `e+pi`
follows from this branch.

## 7. Certificate

The companion certificate checks the exact tail derivative identity and
the pure Hankel identity symbolically, and checks the stable-root inequality
on a dense floating-point diagnostic grid, the integer-kernel identities
and negative discriminants, and additional critical-ray Hankel signs.  The
grids and scans are diagnostics only; the uniform arguments are the
inequalities above.
