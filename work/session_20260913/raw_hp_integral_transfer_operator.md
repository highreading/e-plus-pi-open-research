> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact second-order integral transfer and a factorial norm criterion

Date: 2026-09-13. Continuation by audit_results, with the initial
second-order combination and Volterra inverse observations supplied by
root. All identities below concern the actual normalization B_n(1)=1.
The coefficient and root bounds needed for a uniform norm estimate
remain unproved.

## 1. Scope and notation

Assume the current degree has q=deg Q_n=3. The proof does not require
squarefreeness or avoidance of any finite point. In particular repeated
roots and Q(1)=0 cause no exception to the integral operator.

Write the actual first transfer row as



$$
S=\frac{N_0+N_1\partial_z+N_2\partial_z^2}{Q},\qquad
\deg(N_0,N_1,N_2)\le(5,6,6).
$$



The sharper mixed-row degree bound is available for every actual
transfer, and the cubic infinity degree ledger gives



$$
N_{0,5}+nN_{1,6}=0,\quad N_{1,6}+N_{2,6}=0,
$$




$$
N_{0,5}+N_{1,5}+N_{2,5}
       +nN_{1,6}+2nN_{2,6}=0.
\tag{1}
$$



These infinity conditions only use q=3, not the generic finite-root
hypotheses of the earlier square update.

To avoid confusion with the old polynomial A, define the exponential
numerator coefficients



$$
\mathsf A=N_0+N_1+N_2,\quad
\mathsf B=N_1+2N_2,\quad
\mathsf C=N_2.
$$



Use a_d,b_d,c_d for their coefficients at z^d, and interpret an index
outside0,...,6 as zero. Put



$$
\gamma=c_6,\qquad \delta=c_5,\qquad \beta=b_5.
$$



The three infinity identities imply



$$
a_6=0,\quad b_6=\gamma,\quad a_5=-n\gamma,
\qquad \boxed{\beta=\delta-2n\gamma.}
\tag{2}
$$



The last cancellation uses the Laurent condition in addition to the
two exponential conditions. It is an all-index identity on the cubic
stratum, not an observation inferred from the finite controls.

On [0,1], let



$$
P_n(t)=\sum_{k=0}^n B_{n,k}\frac{t^{n-k}}{(n-k)!},
\quad (Jf)(t)=\int_0^t f(s)\,ds,\quad \theta=t\partial_t.
$$



This is the earlier actual P_B reflected by t=1-x, so all its Lp norms
are unchanged.

## 2. The exact integral identity and its boundary terms

The coefficientwise factorial/reversal transform at common reference
degree n+6 gives



$$
\sum_{d=0}^3Q_dJ^{5-d}P_{n+1}
=\mathcal W_nP_n,
$$




$$
\mathcal W_n=
\sum_{j=0}^2\sum_{d=0}^6
\widetilde N_{j,d}J^{6+j-d}(n-\theta)_{\underline j},
\quad(\widetilde N_0,\widetilde N_1,\widetilde N_2)
=(\mathsf A,\mathsf B,\mathsf C).
\tag{3}
$$



There are no negative integral powers in (3), since 6+j-d>=0.
Moreover a_6=0 removes its sole possible J^0 term, so every remaining
term contains at least one J.

Apply two t-derivatives. The left side becomes



$$
(Q_3I+Q_2J+Q_1J^2+Q_0J^3)P_{n+1}.
\tag{4}
$$



This differentiation loses no boundary data. Every nonzero term on
the right of (3) has at least one J, so W_nP(0)=0. Its first derivative
at0 can receive contributions only from a_5 JP and b_6 J(n-theta)P.
Their sum is (-n gamma+n gamma)P(0)=0. Therefore W_nP and its first
derivative vanish at0 for every polynomial P, and integrating the
differentiated identity twice recovers (3) without additional constants.

The integrations by parts below also produce no hidden P(0) or P'(0)
terms. Their boundary factors contain t or t² and vanish at0.

## 3. The complete second-order and Volterra operator

For r>=1,



$$
J^r(n-\theta)P=(n+r)J^rP-tJ^{r-1}P.
\tag{5}
$$



For r>=2,



$$
J^r(n-\theta)_{\underline2}P
=(n+r)(n+r-1)J^rP
-2(n+r-1)tJ^{r-1}P+t^2J^{r-2}P.
\tag{6}
$$



At r=1 the same formula means



$$
J(n-\theta)_{\underline2}P
=n(n+1)JP-2ntP+t^2P'.
\tag{7}
$$



The only terms that formally acquire J^-1 after two derivatives are
a_5 P' and b_6 partial_t(n-theta)P. By (2) their sum is
-gamma partial_t theta P. Combining with c_6(n-theta)_2 P gives



$$
\gamma\{t(t-1)P''-[(2n-2)t+1]P'+n(n-1)P\}.
$$



Define, for0<=k<=6, the explicitly known quadratic polynomials



$$
\boxed{
V_k(t)=a_{4-k}+(n+k)b_{5-k}
 +(n+k)(n+k-1)c_{6-k}
-t[b_{4-k}+2(n+k)c_{5-k}]+t^2c_{4-k}.}
\tag{8}
$$



Then the full equation is



$$
(Q_3I+Q_2J+Q_1J^2+Q_0J^3)P_{n+1}
=\mathcal D_nP_n,
$$




$$
\boxed{
\mathcal D_nP=
\gamma t(t-1)P''
+[\delta t^2-((2n-2)\gamma+\beta)t-\gamma]P'
+\sum_{k=0}^6V_k(t)J^kP.}
\tag{9}
$$



This displays every coefficient and every integral term.

In fact c_0=N_2(0)=0 for an actual transfer, because the first possible
origin term of N_0R+N_1R'+N_2R'' is
N_2(0)M(M-1)[z^M]R*z^(M-2), and the required raised origin order is
larger. Consequently V_6=(n+6)(n+5)c_0=0. Keeping it in the notation is
harmless; there are at most five nonzero repeated-integral terms.

## 4. Exact cancellation to the shifted Legendre operator

Let



$$
\mathscr L P=-[t(1-t)P']'
=t(t-1)P''+(2t-1)P'.
$$



Using beta=delta-2n gamma in (9) gives the simpler exact identity



$$
\boxed{\mathcal D_nP=
\gamma\mathscr LP+\delta t(t-1)P'
+V_0(t)P+\sum_{k=1}^5V_k(t)J^kP.}
\tag{10}
$$



Thus no unweighted tP' term remains. A naive estimate before using all
three infinity conditions would lose an unnecessary order of n.

Another useful exact arrangement is



$$
\mathcal D_n=
\gamma(\mathscr L-n(n+1)I)
+\delta[t(t-1)\partial_t+n(1-2t)]
+W_0(t)+\sum_{k=1}^5V_k(t)J^k,
\tag{11}
$$




$$
W_0(t)=a_4-b_4t+c_4t^2.
$$



This form separates the constant and linear parts already coupled to
the differential operator.

## 5. Uniform Volterra inverse criteria without root separation

Let alpha_1,alpha_2,alpha_3 be the complex roots of Q, counted with
multiplicity. Then



$$
H_n:=I+(Q_2/Q_3)J+(Q_1/Q_3)J^2+(Q_0/Q_3)J^3
=\prod_{r=1}^3(I-\alpha_rJ).
\tag{12}
$$



Each factor has the explicit inverse



$$
(I-\alpha J)^{-1}f(t)
=f(t)+\alpha\int_0^t e^{\alpha(t-s)}f(s)\,ds.
\tag{13}
$$



Direct differentiation or the absolutely convergent Volterra series
verifies the inverse on L2(0,1). Young's convolution inequality gives



$$
\|(I-\alpha J)^{-1}\|
\le1+|\alpha|\int_0^1e^{\operatorname{Re}\alpha\,s}\,ds.
\tag{14}
$$



For real alpha>=0 this becomes e^alpha. For real alpha<=0 the stronger
bound1 holds. Indeed, writing alpha=-a with a>=0,



$$
\operatorname{Re}\langle g,(I+aJ)g\rangle
=\|g\|_2^2+\frac a2\left|\int_0^1g\right|^2
\ge\|g\|_2^2,
$$



so the everywhere-defined inverse is a contraction.

Define ell(alpha) using these sharper real bounds and (14) otherwise,
and put Lambda_n=product_r ell(alpha_r). Then



$$
\boxed{\|H_n^{-1}\|_{2\to2}\le\Lambda_n.}
\tag{15}
$$



Several concrete sufficient root hypotheses give a uniform Lambda:

- all roots lie in one fixed bounded subset of C;
- all roots are real and sum_r max(alpha_r,0) is uniformly bounded;
- each root lies either in a fixed bounded set or in a fixed left
  sector |alpha|<=K*(-Re alpha).

For the sector condition, (14) is at most1+K. Repeated roots present no
problem. No lower bound on distances between roots, distance from1,
or Q(1) is required. The inverse may remain uniformly controlled even
when roots coalesce at1 or negative real roots have large modulus.

None of these all-index root hypotheses has been established for the
actual orbit.

## 6. A rigorous coefficient criterion for one-step factorial growth

Normalize all coefficients in (10) by Q_3, writing bars. The actual
equation is



$$
P_{n+1}=H_n^{-1}\overline{\mathcal D}_nP_n.
\tag{16}
$$



For P of degree at most n, put N=n(n+1). Shifted Legendre
orthogonality gives the exact spectral bound



$$
\|\mathscr LP\|_2\le N\|P\|_2,
$$



and integration by parts gives



$$
\int_0^1t(1-t)|P'|^2
=\langle P,\mathscr LP\rangle\le N\|P\|_2^2.
$$



Since t(1-t)<=1/4,



$$
\|t(t-1)P'\|_2\le\frac{\sqrt N}{2}\|P\|_2.
\tag{17}
$$



Also ||J^k||<=1/k! by its convolution kernel. A convenient sufficient
operator bound is therefore



$$
\|\overline{\mathcal D}_nP\|_2
\le
\left(
|\bar\gamma|N+\frac{|\bar\delta|\sqrt N}{2}
+\|\bar V_0\|_\infty+
\sum_{k=1}^5\frac{\|\bar V_k\|_\infty}{k!}
\right)\|P\|_2.
\tag{18}
$$



Every supremum here is that of an explicit real quadratic on [0,1].
It can be evaluated using the endpoints and, when it lies in the
interval, the single critical point.

A sharper bound permits the constant part of V0 to cancel the
Legendre spectrum. Let m=min_[0,1] bar V0 and M=max_[0,1] bar V0, and set



$$
G_n=\max\left(
|m+\min(0,\bar\gamma N)|,\,
|M+\max(0,\bar\gamma N)|
\right).
\tag{19}
$$



Then |\bar gamma|N+||bar V0|| in (18) may be replaced by G_n. To prove
this, insert a real constant shift lambda between the two operators:



$$
\bar\gamma\mathscr L+\bar V_0
 =(\bar\gamma\mathscr L-\lambda I)+(\bar V_0+\lambda).
$$



The first norm on P_n is the maximum distance from lambda to the
endpoints of the interval [min(0,bar gamma N),max(0,bar gamma N)].
The second is the maximum distance from -lambda to [m,M]. Minimizing
the sum of these two radii gives exactly (19). This is an operator
triangle bound with an optimized shift, not an assumption that the
differential and multiplication operators commute.

Consequently a fully explicit sufficient condition is



$$
\boxed{
\Lambda_n\left[
G_n+\frac{|\bar\delta|\sqrt{n(n+1)}}2
+\sum_{k=1}^5\frac{\|\bar V_k\|_\infty}{k!}
\right]\le C(n+1)
\quad(n\ge n_0).}
\tag{20}
$$



Under (20), the desired one-step estimate



$$
\|P_{n+1}\|_2\le C(n+1)\|P_n\|_2
\tag{21}
$$



holds for the actual polynomials. The operator estimate is stronger:
it controls every input polynomial of degree at most n.

An easier sufficient collection of bounds, with fixed constants, is



$$
\Lambda_n\le L,\qquad
|\bar\gamma|\le G/(n+1),\qquad |\bar\delta|\le D,
$$




$$
\|\bar V_0\|_\infty+
\sum_{k=1}^5\|\bar V_k\|_\infty/k!\le V(n+1).
\tag{22}
$$



These imply (21) with C=L(G+D/2+V). The combined V_k bounds, rather
than bounds on individual summands before their cancellations, are
the relevant quantities.

Iterating (21) gives ||P_n||2<=n! exp(O(n)), hence the missing upper
bound ||P_n||1<=n! exp(O(n)) and the corresponding lower bound
exp(-O(n))/n! for the inverse-norm residual in the earlier Gram
construction. It still does not estimate the cancellation ratio in
the whole remainder integral or the primitive endpoint denominator.

## 7. Independent exact controls and finite diagnostics

The checker check_raw_integral_transfer_independent.py constructs the
actual pairs of degrees3,4 and5,6 directly from the original Taylor
and endpoint equations. It verifies:

- the full primitive identity and both zero boundary constants;
- the complete second-order/Volterra formula on every monomial of
  the selected input polynomial spaces;
- the exact Legendre cancellation;
- agreement with the actual normalized next polynomial.

All checks pass in raw_integral_transfer_independent_checks.json.

From those same stored exact rows, with no additional indices, the
following rounded values were obtained:

| current n | n*gamma/Q3 | delta/Q3 | combined V coefficient bound divided by n | full conservative numerator bound divided by n |
|---:|---:|---:|---:|---:|
| 3 | -0.0588144381 | -0.2374531754 | 3.8839677406 | 4.1206891083 |
| 5 | -0.0740539204 | -0.2195152836 | 3.6660727387 | 3.8866466133 |

The combined bound in this table is the coefficient absolute-value
bound for V0 plus sum_(k>=1) of the coefficient absolute-value bounds
for Vk divided by k!, all normalized by |Q3|n. The full numerator
column adds the safe weighted differential bounds, replacing
sqrt(n(n+1)) by n+1. It does not include Lambda_n.

These two odd-index cubics each have only one real root and a complex
conjugate pair. Exact real isolations are recorded in the JSON. Thus
the all-real-root version of the inverse lemma cannot be imposed on
the whole actual orbit merely from the separate even-index examples.
The complex-root criteria remain available.

The displayed values are modest and support investigating (20), but
they prove no uniform coefficient or root bound. If parity causes
large one-step factors at other indices, a two-step estimate



$$
\|\mathcal T_{n+1}\mathcal T_nP_n\|_2
\le C^2(n+1)(n+2)\|P_n\|_2
$$



for the exact operators in (16) would be sufficient. Such a product
must be analyzed with its actual intermediate polynomial; multiplying
two loose one-step norm bounds can discard the relevant cancellation.
No claim of a two-step cancellation is made here.
