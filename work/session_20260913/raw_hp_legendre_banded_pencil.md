> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The exact Legendre pencil, high-mode bounds, and the endpoint concentration target

Date: 2026-09-13. Continuation by audit_results. The cubic-stratum integral
transfer is now written as a banded coefficient relation. The structural
identities and high-mode estimates below are proved. No concentration,
endpoint noncancellation, or coefficient-limit hypothesis is inferred
from the bandwidth.

## 1. Orthonormal coordinates

Let L_l(t)=P_l(2t-1) be the shifted Legendre polynomial, and put



$$
\phi_l(t)=\sqrt{2l+1}\,L_l(t),\qquad
P_n(t)=\sum_{l=0}^n p_{n,l}\phi_l(t).
$$



The phi_l are orthonormal in L2(0,1). Thus ||p_n||_(ell2)=||P_n||2.
Write e_l for the coordinate vector and



$$
\tau_l=\frac1{2\sqrt{(2l+1)(2l+3)}}.
$$



The integration operator J and multiplication by t have the exact
matrices



$$
\mathsf J e_0=\tfrac12e_0+\tau_0e_1,\qquad
\mathsf J e_l=\tau_l e_{l+1}-\tau_{l-1}e_{l-1}\quad(l\ge1),
\tag{1}
$$





$$
\mathsf T e_l=\tfrac12e_l+(l+1)\tau_l e_{l+1}
                    +l\tau_{l-1}e_{l-1}.
\tag{2}
$$



Terms with index -1 are omitted. In particular



$$
\mathsf J+\mathsf J^*=e_0e_0^*,\qquad \mathsf T=\mathsf T^*.
$$



These formulas follow respectively from
J L_l=(L_(l+1)-L_(l-1))/(2(2l+1)) for l>=1,
J L_0=(L_1+L_0)/2, and the ordinary three-term Legendre recurrence.

Let Lambda=diag(l(l+1)). The shifted Legendre differential operator
has matrix Lambda, while



$$
t(t-1)L_l'
=\frac{l(l+1)}{2(2l+1)}(L_{l+1}-L_{l-1}).
$$



Consequently the exact weighted-derivative matrix is



$$
\boxed{\mathsf W=\mathsf J\Lambda.}
\tag{3}
$$



The exceptional diagonal entry of J at index0 causes no problem
because Lambda_00=0.

## 2. Infinite banded relation

Use the notation and actual normalization of
raw_hp_integral_transfer_operator.md, on a current index with deg Q=3.
Divide coefficients by Q3 and write



$$
q_2=Q_2/Q_3,\quad q_1=Q_1/Q_3,\quad q_0=Q_0/Q_3,
\quad g_n=\gamma/Q_3,\quad d_n=\delta/Q_3,
$$



and v_(k,n)(t)=V_(k,n)(t)/Q3. The exact coefficient relation is



$$
\boxed{\mathsf H_n p_{n+1}=\mathsf D_n p_n,}
\tag{4}
$$





$$
\mathsf H_n=I+q_2\mathsf J+q_1\mathsf J^2+q_0\mathsf J^3,
$$




$$
\boxed{
\mathsf D_n=(g_n I+d_n\mathsf J)\Lambda
                 +\sum_{k=0}^5v_{k,n}(\mathsf T)\mathsf J^k.}
\tag{5}
$$



The order of factors in the last sum matters: integrate first, then
multiply by the polynomial. J and T do not commute.

Equation(4) is well defined on finitely supported vectors. H_n is
bounded and invertible on ell2 under the equivalent Volterra
representation. D_n, for fixed n, contains the unbounded diagonal
Lambda; no bounded-operator claim on the whole infinite ell2 space is
made. Its restriction to input degrees at most n is the relevant map.

In the unnormalized L_l basis every entry is rational. The orthonormal
pencil is obtained by the diagonal conjugation with sqrt(2l+1).

## 3. The right bandwidth is five, and three upper rows must be retained

The left matrix has bandwidth3. The apparent right bound7 can be
sharpened using the exact coefficient formula for V_k:

- V6=0 because N2(0)=0;
- V5 is constant;
- V4 has degree at most1;
- V0,V1,V2,V3 have degree at most2.

Since T has bandwidth1, V_k(T)J^k has bandwidth at most5 in every
case. The differential terms have bandwidth at most1. Thus



$$
\boxed{(\mathsf D_n)_{r,l}=0\quad\text{if }|r-l|>5.}
\tag{6}
$$



For an input polynomial of degree at most n, the apparent output
degree n+5 also cancels. It suffices to inspect its coefficient on
the leading input monomial t^n. The three possible contributions are
the constant term of V5*J5, the linear term of V4*J4, and the quadratic
term of V3*J3. At common denominator (n+1)...(n+5), their coefficient is



$$
(n+5)[b_0+(n+4)c_1]
-(n+5)[b_0+2(n+4)c_1]
+(n+5)(n+4)c_1=0.
\tag{7}
$$



Every lower input degree already produces degree at most n+4.
Therefore D_n maps P_n into P_(n+4).

The complete finite equality is consequently



$$
\boxed{
H_n^{\rm fin}p_{n+1}=D_n^{\rm fin}p_n,\quad
H_n^{\rm fin}\in\mathbb R^{(n+5)\times(n+2)},\quad
D_n^{\rm fin}\in\mathbb R^{(n+5)\times(n+1)},}
\tag{8}
$$



using output rows0,...,n+4. H_n^fin has full column rank because H_n
is injective on L2.

Keeping only rows0,...,n+1 loses the three upper compatibility
equations at n+2,n+3,n+4. Those equations help ensure that the
Volterra solution is a polynomial of the required degree. A square
compression of H_n need not inherit the invertibility of the full
Volterra operator. The exact pencil should therefore be kept
rectangular unless these compatibility rows are accounted for
separately.

## 4. Sharp high-index integration estimates

Let E_(>=m) denote projection onto Legendre indices at least m, with
m>=1. The weighted-shift formula(1) gives



$$
\|\mathsf J E_{\ge m}\|
\le \tau_{m-1}+\tau_m
\le \frac1{\sqrt{4m^2-1}}.
\tag{9}
$$



This is asymptotically sharp:



$$
\boxed{\lim_{m\to\infty}2m\,\|\mathsf J E_{\ge m}\|=1.}
\tag{10}
$$



For a lower bound, take a vector supported on l=m,...,m+L-1, with
entries i^l/sqrt(L), where L tends to infinity and L/m tends to zero.
At the interior indices, J acts by -i(tau_(l-1)+tau_l), which is
(1+o(1))*(-i)/(2m) uniformly on that block. Ignoring the two boundary
entries gives the matching lower norm bound. For example L=floor(sqrt m)
suffices. The real and complex operator norms agree for this real
matrix, so complex test coordinates introduce no additional premise.

For fixed k and m>=k, each integration can lower the minimum index
by at most1. Iterating(9) gives



$$
\boxed{
\|\mathsf J^kE_{\ge m}\|
\le\prod_{r=0}^{k-1}(\tau_{m-r-1}+\tau_{m-r})
\le\prod_{r=0}^{k-1}(4(m-r)^2-1)^{-1/2}.}
\tag{11}
$$



Its leading scale is (2m)^(-k). The same interior phase-vector
argument, with a fixed k and k boundary rows omitted, gives the
matching asymptotic constant if needed.

These are estimates on high input modes, not the full norm of J.
They are stronger than the global bound ||J^k||<=1/k!.

## 5. The inverse is almost local on high modes under explicit root bounds

Suppose for the moment that the monic coefficients of Q are uniformly
bounded and that ||H_n^-1|| is uniformly bounded by L. The latter
follows, for example, from the bounded-root criterion already proved.
Then



$$
\|(H_n-I)E_{\ge m}\|=O(m^{-1}),
$$



and the resolvent identity gives



$$
\boxed{\|(H_n^{-1}-I)E_{\ge m}\|=O(m^{-1}).}
\tag{12}
$$



All constants here depend on the stated uniform bounds. An arbitrary
bounded inverse without the coefficient bounds does not give(12).

There is a stronger far-off-diagonal estimate when all three roots
have modulus at most R. Expanding the commuting inverses gives



$$
H_n^{-1}=\sum_{r\ge0}h_{r,n}\mathsf J^r,\qquad
|h_{r,n}|\le\binom{r+2}{2}R^r.
$$



Since J^r has bandwidth r and ||J^r||<=1/r!,



$$
\boxed{
\|E_{\le a}H_n^{-1}E_{\ge b}\|
\le\sum_{r\ge b-a}\binom{r+2}{2}\frac{R^r}{r!}
\quad(b>a).}
\tag{13}
$$



The inverse is generally dense; (13) controls that density instead of
incorrectly treating its bandwidth as three. The same statement holds
with upper and lower modes interchanged. Combining it with the
bandwidth5 of D_n gives a corresponding transport-tail estimate with
the separation reduced by5.

## 6. Conditional separation of bulk transport from the integral corrections

Here is a precise consequence of the coefficient scales already
isolated by the norm criterion. Assume on the indices considered that



$$
|g_n|=O(n^{-1}),\quad |d_n|=O(1),\quad
\|v_{k,n}\|_\infty=O(n)\quad(0\le k\le5),
\tag{14}
$$



and that the inverse and monic coefficient bounds used in(12) hold.
Fix eta>0 and restrict input indices to eta*n<=l<=n.

By(11), the sum of the k>=1 integral terms has operator norm O(1).
The three nonintegral terms have norm O(n). Since D_n lowers indices
by at most5, (12) applies to their output and changes it by O(1).
Consequently



$$
\boxed{
\frac1nH_n^{-1}D_n
=\frac1n\{g_n\Lambda+d_n\mathsf J\Lambda
                         +v_{0,n}(\mathsf T)\}+O(n^{-1})}
\tag{15}
$$



in operator norm on that restricted input space.

If, in addition,



$$
ng_n\to g,\quad d_n\to d,\quad
v_{0,n}(t)/n\to v(t)
$$



coefficientwise, then around an index l/n->x>0 the fixed-offset matrix
entries converge to those of the translation-invariant band operator



$$
g x^2I+\frac{d x}{4}(\mathsf S_+-\mathsf S_-)
 +v\!\left(\tfrac12I+\tfrac14(\mathsf S_++\mathsf S_-)\right).
\tag{16}
$$



Here S_+e_l=e_(l+1), and S_-=S_+^*. On plane waves its symbol is



$$
g x^2-\frac{i d x}{2}\sin\vartheta
  +v\!\left(\frac{1+\cos\vartheta}{2}\right).
\tag{17}
$$



This is a proved conditional bulk limit, with every required bound
listed. It does not supply the coefficient limits or prove stability.
At the upper degree boundary the three compatibility rows from
Section3 remain essential. In particular, a bulk symbol alone need
not select the actual top-mode boundary behavior.

## 7. Exact endpoint quotient and the correct weighted concentration criterion

The reversal transform gives



$$
B_{n,n}=P_n(0),\qquad B_{n,n-1}=P_n'(0).
$$



On the cubic stratum B has full degree n, so P_n(0) is nonzero. Set



$$
a_{n,l}=(-1)^l\sqrt{2l+1}\,p_{n,l},\quad
A_n^{\rm abs}=\sum_l|a_{n,l}|,\quad
\eta_n=\frac{|\sum_la_{n,l}|}{A_n^{\rm abs}}>0.
$$



Using phi_l'(0)=-l(l+1)phi_l(0), the root-sum coefficient is exactly



$$
\boxed{
\beta_{B,n}=\frac{B_{n,n-1}}{B_{n,n}}
=-\frac{\sum_l l(l+1)a_{n,l}}{\sum_l a_{n,l}}.}
\tag{18}
$$



Thus



$$
\beta_{B,n}+n(n+1)
=\frac{\sum_l[n(n+1)-l(l+1)]a_{n,l}}{\sum_l a_{n,l}}.
\tag{19}
$$



Let w_n be an integer between0 and n, and let epsilon_n be the
fraction of absolute endpoint weight below the top window l>=n-w_n.
Then



$$
\frac{|\beta_{B,n}+n(n+1)|}{n^2}
\le
\frac{(2n+1)w_n/n^2+(1+1/n)\epsilon_n}{\eta_n}.
\tag{20}
$$



Consequently



$$
\boxed{
\frac{w_n/n+\epsilon_n}{\eta_n}\longrightarrow0
\quad\Longrightarrow\quad \beta_{B,n}/n^2\longrightarrow-1.}
\tag{21}
$$



This is the required endpoint noncancellation qualification. Small
low-mode L2 mass alone does not bound eta_n.

For comparison with an L2 concentration theorem, if



$$
\|E_{\le n-w_n-1}p_n\|_2\le e_n\|p_n\|_2,
$$



then Cauchy–Schwarz gives epsilon_n<=(n+1)e_n. Indeed,
sum_(l<=N)|a_l|<= (N+1)||p_(<=N)||2, while
A_n^abs>=||p_n||2. Thus a sublinear window and an exponentially small
L2 tail would imply the desired beta limit under a uniform positive
lower bound on eta_n. No such lower bound is established here.

## 8. Top-window concentration must allow normalization cancellation

In the t-variable the actual endpoint normalization is



$$
\mathfrak b(P)=\sum_{j\ge0}P^{(j)}(0)=B_n(1)=1.
$$



For L_l, its value is positive and



$$
\mathfrak b(L_l)
=\frac{(2l)!}{l!}
\left(\sum_{r=0}^l\frac{(-1)^r}{r!}
\frac{(l)_{\underline r}}{(2l)_{\underline r}}
\right)
\sim e^{-1/2}\frac{4^l l!}{\sqrt{\pi l}}.
\tag{22}
$$



This factorial scale is the same one proved in the earlier endpoint
representer calculation.

Accordingly, a large norm together with b(P)=1 requires cancellation
among the Legendre coefficients weighted by b(L_l). It does not
permit an unqualified assumption of pure L_n dominance.

Adjacent coefficients of opposite signs can cancel in b(P), whose
weights are positive, while contributing the same sign to P(0),
whose Legendre weights alternate. Hence endpoint noncancellation is
compatible with the necessary normalization cancellation. A top
window containing n-1 and its neighbors is a legitimate target.

For a finer diagnostic, put h=n-l and define signed endpoint moments
mu_j=sum h^j a_(n,n-h)/sum a_(n,n-h). Then exactly



$$
\beta_{B,n}=-n(n+1)+(2n+1)\mu_1-\mu_2,
$$




$$
\beta_{B,n}+n(n-1)=2n(\mu_1-1)+\mu_1-\mu_2.
\tag{23}
$$



A bounded correction to -n(n-1) therefore requires more than a
sublinear window: for example mu1=1+O(1/n) and bounded mu2 would
suffice. No such signed-moment estimate is claimed.

## 9. A precise unproved dynamical target

The shortest remaining endpoint target, if a separate concentration
theorem supplies the sublinear window, is a sign-cone bound for the
weights a_(n,l). Let S+ and S- be their total positive and negative
masses. A fixed rho<1 such that



$$
\boxed{\min(S_+,S_-)\le\rho\max(S_+,S_-)}
\tag{24}
$$



implies eta_n>=(1-rho)/(1+rho). It permits some coefficients of either
sign; it is weaker than claiming that every endpoint weight has the
same sign.

A stronger dynamical route would propagate a top-index weighted cone.
Reverse the endpoint-weight vector by r_(n,h)=a_(n,n-h), and fix
omega>1. If, from one verified seed onward, the exact projected
transport preserves



$$
\sum_h\omega^h|r_h|\le K\sum_h|r_h|,
\qquad |\sum_hr_h|\ge c\sum_h|r_h|,
\tag{25}
$$



then all absolute endpoint deficit moments are bounded, and (19)
gives beta_B+n(n+1)=O(n).

The projected transport in this statement means the actual
H_n^-1 D_n followed by output projection through degree n+1 and the
explicit endpoint-weight/reversal change of coordinates. On the
actual trajectory its discarded coefficients are zero by the three
compatibility equations. Those equations must still be verified for
any candidate limiting mode.

Coefficient limits could justify this route only with additional
uniform control: convergence of the rescaled transport in the
weighted operator norm, a strict invariant-cone margin for the
limiting operator, a lower bound on its output norm on the cone, and
entry of the actual seed into that cone. Strict margins then survive
small operator perturbations by elementary norm estimates.
Fixed-offset limits such as(16), or a narrow bandwidth by itself,
do not supply these hypotheses.

Thus the proved structural work isolates two concrete next questions:
the actual coefficient/root estimates needed for the bulk transfer,
and the endpoint sign-cone or noncancellation estimate needed for
(21). It does not claim either one has been solved.

## 10. Exact structural controls

check_raw_legendre_pencil.py uses two predeclared synthetic coefficient
rows, at n=3 and n=6, satisfying the exact cubic infinity relations
and N2(0)=0. It checks the orthonormal matrix scaling, bandwidth5,
top-output cancellation, the rectangular row bounds, and equality
with direct polynomial differentiation and integration on every
input Legendre polynomial in those two spaces. It also checks the
endpoint beta quotient on a separate polynomial.

All checks pass in raw_legendre_pencil_checks.json. These rows are
explicitly synthetic structural controls, not additional canonical
raw-family samples and not evidence for orbit stability.

## 11. Interface with the separately proved high-orthogonality concentration

The new result in raw_high_orthogonality_spectral_concentration.md,
independently audited in raw_legendre_concentration_independent_review.md,
supplies a sublinear top window and an exponentially small L2 tail for
the actual high-orthogonal inputs. Its proof is separate from the
banded-pencil argument. It does not supply endpoint noncancellation.

There is also an immediate improvement of the centered norm criterion.
If ||E_(<=n-w-1)P||2<=epsilon*||P||2, then the diagonal spectrum gives



$$
\boxed{
\|(\mathscr L-n(n+1)I)P\|_2
\le[w(2n+1)+n(n+1)\epsilon]\|P\|_2.}
\tag{26}
$$



The top-window multiplier is at most w(2n+1), while the remaining
multiplier is at most n(n+1); orthogonality justifies the separate
bounds. With w=O(n/log n) and exponentially small epsilon, the
W0-centered identity (11) of raw_hp_integral_transfer_operator.md
therefore permits the weaker coefficient requirement



$$
|\gamma/Q_3|=O(\log n/n),
$$



provided delta/Q3 is bounded, the actual combined W0 and remaining
Volterra norms are O(n), and the inverse norm is uniformly bounded.
The resulting estimate remains ||P_(n+1)||2<=C(n+1)||P_n||2.

This relaxation uses the actual high-orthogonality constraints. The
full-polynomial operator criterion still requires its original
stronger estimate. The supplied spectral concentration also makes
(24), or the more flexible eta_n condition in(21), a particularly
direct next target for beta_B/n².
