> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Moving Möbius parameter: an actual cancellation transition

Date: 2026-09-13. Continuation of `hp_mobius_parameter_dependence.md`.
This note concerns the degree-(n,1,n) anchored HP family. It does not prove
the rationality or irrationality of e+pi.

## Result and overlap check

Write rho=1+sqrt(2). For real b_n with b_n/n->kappa>0, the exact matched
family is normal with nonzero endpoint for all sufficiently large n.
Outside the critical slope



$$
\kappa_*=(2e\rho)^{-1},
$$



its normalized evaluated error has the rigorous exponential rate



$$
\frac1n\log|R_n(1)/Y_n|
 \longrightarrow -2\log\rho+
 \max\{0,\log(2e\rho\kappa)\}.
 \tag{1}
$$



Thus moving linearly in n offers no improved analytic exponent away
from the critical slope. At the critical slope, a genuine cancellation
window exists. In fact the continuous real parameter has exact zeros of
the evaluated remainder near



$$
b_n^*=\kappa_*n+\frac72\kappa_*\log n+O(1).
 \tag{2}
$$



This is an intermediate-value theorem about **real parameters**, not a
rational construction. At such a parameter, the identity X_b/Y_b=-(e+pi)
itself holds, so it does not supply a known rational coefficient. The
arithmetic task is to obtain adequate rational approximation to a moving
zero while controlling the **reduced** endpoint denominator. The verified
ledger remains D=H^2 L_n s^(2n+1) for b=r/s, H=4^(n+1)(2n+1)!.

Before deriving this, I searched the relevant archive parameter/pullback
notes and read the scopes and constructions in
`sources/high_radius_composed_integral_jet_pullback.md`,
`sources/improved_composed_integral_jet_pullback.md`, and
`sources/universal_pullback_radius_bound.md`, as well as the already read
real Möbius-radius section of `sources/pi_g_function_pullback_route.md`.
Those results concern fixed polynomial compositions, their integral jets,
or a universal radius ceiling; they do not give the moving degree-one
factorial endpoint determinant below. No all-archive semantic rereading
is asserted. The moving Möbius Taylor radius actually tends to one; pure
pi Padé endpoint covariance, not a growing Taylor radius, controls its
logarithmic approximation here.

## 1. Exact identity retaining the large endpoint term

Use all objects from the parameter note, but let b=b_n. Put



$$
V=K_{n,b}(t,1),\quad W=\Psi_{n,b},\quad
 t_j=\ell_j(V),\quad w_j=\ell_j(W),\quad
 \Delta=\ell_1-\ell_0.
$$



For B(0)=1, Y=Delta(V)/(1+t_1). The whole-remainder identity is exactly



$$
\frac{R(1)}Y
 =-\frac{\Delta(W)}{\Delta(V)}
 +\frac{t_1w_0-t_0w_1}{\Delta(V)}.
 \tag{3}
$$



Indeed R(1)/Y=-(1+t_1)Delta(W)/Delta(V)+w_1, and the last two terms
combine into the displayed numerator. Its sign is essential: the
numerator is the **negative** of det((t_0,t_1),(w_0,w_1)).

Set a=1+b and



$$
U=p_{n+1,b},\quad
 \mu_n=-p_{n+1,b}(0)/p_{n,b}(0),\quad
 \lambda_n=p_{n+1,b}(1)/p_{n,b}(1),\quad
 \alpha_n^*=v_{n+1,b}/v_{n,b}.
$$



For b/n bounded above and below by positive constants,



$$
\mu_n\to1,\quad
 a\lambda_n\to\rho/2,\quad
 a\alpha_n^*\to(1-\sqrt2)/2.
 \tag{4}
$$



The first follows directly from
b/a<=mu_n<=b/a+1/(3ab). The latter two use the exact affine scaling from
the fixed-map quantities and their already proved limits. Let



$$
q_n(t)=p_{n,b}(t)/p_{n+1,b}(t),\quad
 c_n=\frac{\lambda_n-\alpha_n^*}
 {(1+\lambda_n/\mu_n)(1+\alpha_n^*/\mu_n)}
 \sim\frac{\sqrt2}{b}.
 \tag{5}
$$



The normalized quotients G_V=(V/V(0))/(U/U(0)) and G_W=(W/W(0))/(U/U(0))
from the fixed-parameter note satisfy the exact difference identity



$$
G_W-G_V=c_n H_n(t),\qquad
 H_n(t)=\frac{q_n(t)+1/\mu_n}{1-t},\qquad H_n(0)=0.
 \tag{6}
$$



These quantities have uniform analytic bounds on any fixed disk
|t|<=r<1, for all sufficiently large n. Indeed the Jacobi matrix for U
has diagonal b/a and off-diagonal norm at most 2/(sqrt(3)a), so its
operator-norm distance from the identity tends to zero. The corner
resolvent therefore gives, locally uniformly on |t|<1,



$$
q_n(t)\to\frac1{t-1},\quad
 G_V(t)\to\frac1{1-t},\quad
 H_n(t)\to-\frac{t}{(1-t)^2},\quad H_n'(0)\to-1.
 \tag{7}
$$



Every root of U equals (b+iu_j)/a for a real Legendre zero |u_j|<1.
All reciprocal roots tend uniformly to 1. Factoring U shows



$$
U(z/n)/U(0)\to e^{-z}
 \tag{8}
$$



locally uniformly, with a fixed reciprocal-root bound (for example 2).
All these convergences are uniform when b/n ranges in a fixed compact
subset of (0,infinity).

## 2. A two-functional determinant with its cancellation fully controlled

For functions P,Q analytic near zero, define



$$
\mathcal D_n(P,Q)=\ell_0(P)\ell_1(Q)-\ell_1(P)\ell_0(Q).
$$



If P=sum P_k t^k and Q=sum Q_l t^l, direct subtraction gives the exact
kernel



$$
\mathcal D_n(P,Q)=\sum_{k,l\ge0}
 \frac{(l-k)P_kQ_l}{(n+k+1)!(n+l+1)!}.
 \tag{9}
$$



Suppose U has degree n+1, a fixed reciprocal-root bound, and normalized
limit (8). Suppose G_n,H_n are uniformly analytic and bounded on a fixed
disk, with G_n(0)=1, H_n(0)=0, and H_n'(0)->h. Then



$$
\boxed{\mathcal D_n(UG_n,UH_n)
 \sim \frac{h\,U(0)^2e^{-2}}{(n!)^2 n^3}}
 \quad\text{if }h\ne0.
 \tag{10}
$$



Here is a direct domination proof at the required cancellation order.
Write U/U(0)=sum u_(n,k)t^k. The root bound L gives
|u_(n,k)|<=binom(n+1,k)L^k, while (8) gives
u_(n,k)/n^k->(-1)^k/k!. For the leading term G=1,H=h t, substitute l=j+1
in (9). After multiplying by (n!)^2n^3/U(0)^2, each term tends to
h(j+1-k)(-1)^(j+k)/(j!k!). Its double sum is h e^(-2): the j-k terms
cancel by symmetry, leaving the product of two exponential series.
The summands are dominated by constants times
(j+k+1)(2L)^(j+k)/(j!k!), which is summable.

For the remaining Taylor terms write G=sum g_r t^r and H=sum h_s t^s,
where s>=1. Cauchy's estimate bounds |g_r|,|h_s| by constants times a
fixed inverse radius to the respective powers. The same kernel estimate
for the pair t^rU,t^sU gains a factor n^(1-r-s) after the displayed
normalization, multiplied by a constant times r+s+1. Thus every r+s>=2
term contributes O(1/n) in total. The only r+s=1 term is r=0,s=1.
This proves (10), including the double Taylor interchanges. The proof is
uniform under the uniform bounds just verified in (7)–(8).

Taking G=G_V, H=H_n, h=-1 in (10) and using (6) yields



$$
t_0w_1-t_1w_0
 \sim-\frac{c_n V(0)W(0)e^{-2}}{(n!)^2 n^3}.
 \tag{11}
$$



In particular this retains the small factor c_n~sqrt(2)/b even though
b grows with n. A generic O(1/n) error before factoring (6) would not
justify that conclusion.

The leading factorial lemma likewise gives



$$
\Delta(V)\sim t_1\sim V(0)e^{-1}/n!,\quad
 \Delta(W)\sim W(0)e^{-1}/n!,\quad t_0/t_1\sim1/n.
 \tag{12}
$$



The kernel V(0)>0, so t_1 and Delta(V) are positive eventually. Thus the
matching row is nonzero, B(0)=1 is available, and
Y~t_1/(1+t_1)>0, regardless of whether t_1 is small or large.

Combining (3), (11), and (12), with independent relative errors on the
two nonzero terms, proves



$$
\frac{R(1)}Y=-\frac{W(0)}{V(0)}
 \left\{(1+o(1))-\frac{c_n t_1}{n^3}(1+o(1))\right\}.
 \tag{13}
$$



The errors here are uniform in the specified compact slope intervals.
This formula is not used to claim a relative error at a zero of the
braced expression; precisely there the cancellation must be retained.
The exact endpoint identity gives



$$
\frac{W(0)}{V(0)}=(-1)^{n+1}\epsilon_n
 \frac{\mu_n+\alpha_n^*}{\mu_n+\lambda_n}
 =(-1)^{n+1}\epsilon_n(1+o(1)).
 \tag{14}
$$



## 3. Kernel growth and the two different transitions

Let p_(n,1)(1) denote the fixed-map monic endpoint. Its positive
recurrence, whose coefficients differ from their limits by O(1/n^2),
implies



$$
p_{n,1}(1)\sim C_P(\rho/4)^n\quad\text{for some }C_P>0.
 \tag{15}
$$



To justify the constant, the endpoint ratio recurrence is uniformly
contractive (derivative bound 1/3); subtracting its positive fixed root
gives ratio error O(1/n^2). The logarithms of the ratio divided by its
limit are summable, so their product converges to a finite positive
constant. No numerical asymptotic fit is used.

Let P=p_(n,b)(1), U_0=|p_(n,b)(0)|, and let C_n=binom(2n,n). Uniformly
for b/n in a fixed compact subset of (0,infinity),



$$
P\sim C_P(\rho/(2a))^n,\qquad
 U_0=(b/a)^n(1+O(n/b^2)),\qquad
 |h_{n,b}|\sim\frac{2\pi}{a}(1/(4a^2))^n.
 \tag{16}
$$



The middle estimate is especially simple: pair the real Legendre zeros
u and -u in the product for p_(n,b)(0); the residual product is
prod(1+u^2/b^2), whose logarithm is between zero and n/(2b^2).
The last estimate is the explicit norm (3) of the parameter note and
Stirling's formula C_n~4^n/sqrt(pi n).

Christoffel–Darboux gives V(0)=P U_0(mu_n+lambda_n)/|h_(n,b)|. Since the
last parenthesis tends to one, (12) and (16) imply



$$
t_1\sim C_*\frac{a}{\sqrt n}
 \left(\frac{2e\rho b}{n}\right)^n,\qquad
 C_*:=\frac{e^{-1}C_P}{2\pi\sqrt{2\pi}}>0.
 \tag{17}
$$



This is uniform in the stated compact slope intervals. Consequently
log(t_1)/n->log(2e rho kappa). The slope where t_1 changes from
exponentially small to exponentially large is kappa_*.

The actual cancellation in (13) occurs later in its polynomial scale:



$$
c_n t_1/n^3\asymp1,\qquad
 t_1\asymp b n^3/\sqrt2,
 \tag{18}
$$



not at t_1 of order one. If kappa<kappa_*, the second term in (13)
vanishes. If kappa>kappa_*, it dominates and reverses the sign. These
alternatives and (14), with log epsilon_n/n->-2log rho, prove (1).
For example, if kappa>rho/(2e), even the normalized error grows
exponentially, so multiplying by a positive integer denominator cannot
yield a shrinking form in that regime.

## 4. An exact real-parameter zero and what rational approximation costs

For a bounded real x set



$$
b=\kappa_*n+\frac72\kappa_*\log n+x.
$$



Equation (17), expanded uniformly for bounded x, gives



$$
\frac{c_n t_1}{n^3}\longrightarrow
 C_*\sqrt2\exp(x/\kappa_*).
 \tag{19}
$$



Indeed the n-th power in (17) contributes
n^(7/2) exp(x/kappa_*)(1+o(1)), its factor a/sqrt(n) contributes
kappa_*sqrt(n)(1+o(1)), and c_n/n^3 contributes
sqrt(2)/(kappa_*n^4)(1+o(1)).

Let x_*=-kappa_*log(C_*sqrt(2)). For every fixed eta>0, the braced
expression in (13) has opposite signs at x=x_*-eta and x=x_*+eta,
for all sufficiently large n. The HP endpoint is nonzero throughout
this real interval by the uniform positivity in (12). Its coefficients
are continuous functions of b. The intermediate value theorem therefore
gives an exact real zero of R(1) in this interval. Choosing zeros in the
nested shrinking brackets proves that zeros can be selected with



$$
b_n^*=\kappa_*n+\frac72\kappa_*\log n+x_*+o(1).
 \tag{20}
$$



No uniqueness is asserted. This is a genuine cancellation, not a
first-coefficient diagnostic. At every such zero,
X_(n,b*)+(e+pi)Y_(n,b*)=0. We have not shown that any b* is rational,
nor that any suitable rational approximation has low primitive endpoint
height.

For rational b=r/s the exact integer ledger and degree theorem from the
parameter note say



$$
D=H^2L_n s^{2n+1},\quad H=4^{n+1}(2n+1)!,\quad
 q_{n,b}=\frac{|DY_{n,b}|}{\gcd(|DX_{n,b}|,|DY_{n,b}|)}.
 \tag{21}
$$



The parameter denominator enters to a power growing with n, and H^2 has
logarithm 4n log n+O(n). In the transition window the raw endpoint
Y_b=Delta(V) in the projective normalization (13) of the parameter note
has only polynomial size (asymptotic to t_1 of order n^4). Thus the
available common-clearer upper bound for the primitive q is of size
exp(4n log n+O(n)) s^(2n+1), up to polynomial factors. This is an upper
bound and a ledger, **not a proved lower bound on the reduced q**.

The analytic result alone does not defeat that arithmetic cost. A
generic rational approximation to a real zero with error of order
1/s^2 cannot simply be combined with a degree-(2n+1) denominator cost
to deduce shrinking integer forms; and (13) is only an o(1)-precision
asymptotic in the braced factor, so it does not itself quantify
exponentially close tuning. A valid next theorem would need an actual
quantitative approximation to the relevant real zero, an evaluated
remainder estimate at that precision, and control of the gcd in (21).
None is proved here.

There is therefore a concrete new analytic intermediate problem—the
critical real-parameter cancellation window—but no demonstrated favorable
primitive arithmetic window. Treating the real zero as an available
rational parameter would assume precisely the missing arithmetic fact.
