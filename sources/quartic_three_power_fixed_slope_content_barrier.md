> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The rational three-power cross product at fixed slope

Date: 2026-08-27.

## 1. Scope and outcome

For even `n`, put



$$
Q(x)=1+x^4,\qquad P_n(x)=x^n(1-x)^n,\qquad
 J_s=\int_0^1\frac{P_n(x)}{Q(x)^{k+s}}\,dx\quad(0\leq s\leq2).
                                                                    \tag{1}
$$



For `k>n/2`, write the quartic Hermite reduction as



$$
J_s=R_s+\frac{L_s}{2\sqrt2}\log(1+\sqrt2)
 +\left(\frac{E_s}{4\sqrt2}+\frac{b_s}{8}\right)\pi.       \tag{2}
$$



All four displayed coordinates in (2) are rational.  The cross product



$$
C=L\times E
 =(L_1E_2-L_2E_1,L_2E_0-L_0E_2,L_0E_1-L_1E_0)             \tag{3}
$$



cancels both irrational quadratic-field coordinates and leaves the
genuinely rational form



$$
\Lambda=C\mathbin\cdot J=A+B\pi,\qquad
 A=C\mathbin\cdot R,\quad B=\frac{C\mathbin\cdot b}{8}.     \tag{4}
$$



This note proves three things and isolates one remaining arithmetic gap.

1.  At every fixed slope with the stated one-saddle geometry, the
    scale-invariant rational approximation has exponential rate

    

$$
\left|\pi+\frac AB\right|
      =\exp\{-n a(\kappa)+o(n)\},\qquad
      a(\kappa)=\ell(\kappa)-j(\kappa)>0,                  \tag{5}
$$



    apart from a possible subexponential real-phase factor.  Here `j` is
    the real integral saddle rate and `ell` the accessible complex saddle
    rate.  The same assertion, with an upper bound and no phase
    qualification, holds unconditionally once the saddle expansions hold.

2.  At the transition `k=n/2+O(1)`,

    

$$
a(1/2)=1.388912660352581880\ldots .                  \tag{6}
$$



    Thus a nonzero primitive form can tend to zero only if its primitive
    integer `pi` coefficient has exponential rate at most (6), or if the
    real saddle projection has an additional exponential cancellation.

3.  There is an exact determinantal description of the fully cleared
    pair and of all its primitive content.  With the published universal
    endpoint clearing, the unreduced integer form has a strictly positive
    exponential rate throughout the admissible fixed-slope branch.  Any
    primitive escape must therefore occur in one explicit gcd of two
    integer determinants.

At the boundary `n=4m,k=2m+1`, the complete two-primary law of the
primitive cross-product coefficient vector is proved below.  The
remaining endpoint valuation reduces to one explicit terminating
hypergeometric congruence.  That congruence, the odd rational-endpoint
denominator, and the final determinantal gcd remain uncontrolled.
Consequently this branch does not yet prove that the *primitive* forms
cannot tend to zero.  It also does not prove that they do tend to zero,
and it does not classify `e+pi`.

## 2. Exact clearing and exact content

For a rational number `x`, let `den(x)` denote its positive denominator.
Choose any positive integers `Delta_s` which simultaneously clear
`L_s,E_s,R_s,b_s`.  Define the integer columns



$$
(\lambda_s,\epsilon_s,\rho_s,\beta_s)
 =\Delta_s(L_s,E_s,R_s,b_s).                               \tag{7}
$$



Put



$$
U=\det\begin{pmatrix}
 \lambda_0&\lambda_1&\lambda_2\\
 \epsilon_0&\epsilon_1&\epsilon_2\\
 \rho_0&\rho_1&\rho_2
 \end{pmatrix},\qquad
 V=\det\begin{pmatrix}
 \lambda_0&\lambda_1&\lambda_2\\
 \epsilon_0&\epsilon_1&\epsilon_2\\
 \beta_0&\beta_1&\beta_2
 \end{pmatrix}.                                           \tag{8}
$$



Multilinearity gives the exact identity



$$
\boxed{
 8\Delta_0\Delta_1\Delta_2\Lambda=8U+V\pi.}              \tag{9}
$$



In particular, if



$$
g=\gcd(8U,V),\qquad p=8U/g,\qquad q=V/g,                 \tag{10}
$$



then `p,q` are the fully primitive rational coordinates and



$$
\boxed{\Phi=p+q\pi=\frac{8\Delta_0\Delta_1\Delta_2}{g}\Lambda.}
                                                                    \tag{11}
$$



Equations (8)--(11) are independent of the chosen column clearing:
changing `Delta_s` multiplies both determinants by the same factor, which
is removed in (10).  They also show exactly where primitive content can
enter.  No estimate for the coefficient height which omits `g` can settle
the branch.

There is an equivalent saturated-kernel description.  Let `A_LE` be the
first two rows of the integer matrix in (7), and let `delta_2(A_LE)` be
the gcd of its `2 by 2` minors.  Then the primitive coefficient vector is



$$
c_{\rm prim}=\frac{\lambda\times\epsilon}{\delta_2(A_{LE})},
 \qquad
 \|c_{\rm prim}\|_2
 =\frac{\sqrt{\det(A_{LE}A_{LE}^T)}}{\delta_2(A_{LE})}.     \tag{12}
$$



The endpoint pair before its final gcd is `(U,V)/delta_2(A_LE)`; the
factor `delta_2(A_LE)` cancels from the primitive pair (10).  Thus the
two separate arithmetic quantities are the kernel-minor content, which
controls coefficient height, and `g`, which controls the final rational
endpoint content.

## 3. Fixed-slope saddle rates

Let `k/n -> kappa>1/2`.  Introduce



$$
\begin{aligned}
 \phi_-(x)&=\log x+\log(1-x)-\kappa\log(1+x^4),\\
 \phi_+(y)&=\log y+\log(1+y)-\kappa\log(1+y^4),\\
 \phi_i(z)&=\log z+\log(1+iz)-\kappa\log(1+z^4).
 \end{aligned}                                             \tag{13}
$$



Let `x_-` be the unique real maximum in `(0,1)`, `y_+` the unique positive
maximum, and `z_i` the accessible complex saddle obtained by continuation
from the small positive saddle as `kappa -> infinity`.  Put



$$
j(\kappa)=\phi_-(x_-),\qquad
 e(\kappa)=\phi_+(y_+),\qquad
 \ell(\kappa)=\Re\phi_i(z_i),                              \tag{14}
$$



and



$$
m=(1+x_-^4)^{-1},\qquad p=(1+y_+^4)^{-1},\qquad
 z_i^*=(1+z_i^4)^{-1}.                                     \tag{15}
$$



The following statement is deliberately phrased with its projected-contour
hypothesis.  It applies on any compact `kappa` interval on which the three
saddles above are nondegenerate and the two coordinate projections `L` and
`b+E/sqrt(2)` have one conjugate saddle pair at `z_i`, with every other
term separated by a fixed real-action gap.  This is slightly weaker than
asserting that the *full* complex integral `I` is saddle dominated.  The
distinction matters at `k=n/2+O(1)`, where `I` has an algebraic endpoint
expansion that disappears from both projected coordinates.  The hypothesis
holds in the large-`kappa` regime proved in the neighboring-saddle note.
Section 4 explains the transition cancellation.  A global no-Stokes proof
for every `kappa>1/2` is not claimed here.

Put



$$
H_s=b_s+\frac{E_s}{\sqrt2}.
$$



**Theorem 3.1 (fixed-slope normalized rate).**  On such an admissible
compact interval, there is one nonzero complex amplitude `Z` and fixed
nonzero real normalizing constants such that



$$
\begin{aligned}
 E_s&=a_+n^{-1/2}e^{ne}\{p^s+O(n^{-1})\},\\
 L_s&=a_Ln^{-1/2}e^{n\ell}
       \{\Re(Z(z_i^*)^s)+O(n^{-1})\},\\
 H_s&=a_Hn^{-1/2}e^{n\ell}
       \{\Im(Z(z_i^*)^s)+O(n^{-1})\},\\
 J_s&=a_-n^{-1/2}e^{nj}\{m^s+O(n^{-1})\},                 \tag{16}
 \end{aligned}
$$



with nonzero analytic amplitudes; the bounded factor `Z` carries the real
phase.  Since `C dot E=0`, one may replace `b` by `H` in the determinant.
Consequently



$$
C\mathbin\cdot b
 =K_b n^{-3/2}e^{n(e+2\ell)}
 \left\{(-\Im z_i^*)|p-z_i^*|^2+O(n^{-1})\right\},         \tag{17}
$$



where `K_b` has a fixed nonzero sign, whereas



$$
C\mathbin\cdot J
 =K_J n^{-3/2}e^{n(e+\ell+j)}
 \left\{\Re\big(
 e^{i(n\theta+\theta_0)}
 (p-z_i^*)(m-z_i^*)(m-p)\big)+O(n^{-1})\right\}.           \tag{18}
$$



In particular, if `Im(z_i^*)` and the two displayed differences do not
vanish, then `C dot b` has a fixed sign and



$$
\boxed{
 \left|\pi+\frac AB\right|
 \leq \exp\{n(j(\kappa)-\ell(\kappa))+o(n)\}.}             \tag{19}
$$



Along any sequence on which the real projection in (18) is
`exp(o(n))` rather than exponentially small, equality holds at the
exponential-rate level.

The determinant identities behind (17)--(18) are purely algebraic:



$$
\det\begin{pmatrix}
 \Re Z&\Re Zg&\Re Zg^2\\1&p&p^2\\
 \Im Z&\Im Zg&\Im Zg^2
 \end{pmatrix}
 =(-\Im g)|Z|^2|p-g|^2,                                   \tag{20}
$$



and



$$
\det\begin{pmatrix}
 \Re Z&\Re Zg&\Re Zg^2\\1&p&p^2\\1&m&m^2
 \end{pmatrix}
 =\Re\{Z(p-g)(m-g)(m-p)\}.                               \tag{21}
$$



Thus the denominator coordinate is phase-independent while the value is
not.  This distinction remains at fixed slope; it is not a peculiarity of
`k/n -> infinity`.

## 4. The transition `k=n/2+O(1)`

At `kappa=1/2`, stationarity simplifies.  The real saddle is the positive
root



$$
x_0^4+2x_0-1=0,\qquad x_0=0.474626617562605550\ldots,     \tag{22}
$$



and the positive saddle is the positive root



$$
y_0^4-2y_0-1=0,\qquad y_0=1.395336994467073019\ldots.     \tag{23}
$$



The accessible complex saddle `z_0=a_0+i b_0` is characterized without
numerical root selection by



$$
16b_0^6+4b_0^2-1=0,\quad b_0>0,\qquad
 a_0=\sqrt{b_0^2+\frac1{2b_0}}>0,                          \tag{24}
$$



so



$$
z_0=1.139317680301922564+0.460355188452233734i\ldots .    \tag{25}
$$



Using `1+x_0^4=2(1-x_0)` and
`1+z_0^4=2(1+iz_0)`, the two relevant rates are



$$
\begin{aligned}
 j_0&=\log x_0+\frac12\log(1-x_0)-\frac12\log2\\
 &=-1.413623474897413433\ldots,\\
 \ell_0&=\log|z_0|+\frac12\log|1+iz_0|-\frac12\log2\\
 &=-0.024710814544831553\ldots .                           \tag{26}
 \end{aligned}
$$



Therefore



$$
\boxed{a_0=\ell_0-j_0
 =1.388912660352581880\ldots>0.}                           \tag{27}
$$



There is a transition subtlety.  For `k=n/2+h` with fixed positive `h`,
the full integral `I_s` has an endpoint-at-infinity expansion.  Setting
`y=n/t` gives, with `H=h+s`,



$$
I_s=i^n n^{1-4H}\int_0^\infty t^{4H-2}
 (1-it/n)^n(1+t^4/n^4)^{-n/2-H}\,dt.                      \tag{27a}
$$



Its leading oscillatory Watson term is
`i^(n+1) Gamma(4H-1)n^(1-4H)`, so it is purely imaginary for even `n`
and does not enter `L_s`.  The corresponding expansion of `A_-` is the
rotation of the same Watson series.  In the exact identity



$$
H_s=\frac2\pi\{A_{-,s}-(-1)^{n/2}\Im I_s\},              \tag{27b}
$$



these endpoint series cancel term by term.  Hence the projected rows
`L,H`, rather than the full `I`, are governed by the conjugate saddle at
the exponential-rate level.  The algebraic saddles are simple and stay
away from the quartic poles; under the projected-contour hypothesis of
Theorem 3.1, (27) is therefore the limiting normalized rate for
`k=n/2+o(n)`.  In the opposite slowly growing regime `kappa -> infinity`,
the already
proved saddle expansions give



$$
a(\kappa)=(4\kappa)^{-1/4}+O(\kappa^{-1/2}).              \tag{28}
$$



Thus changing the slope never supplies analytic primitive height.  It
only changes the height threshold which arithmetic content must beat.

## 5. The primitive-height criterion

Let `(p_n,q_n)` be the primitive pair (10), oriented arbitrarily.  The
exact identity



$$
\boxed{
 |p_n+q_n\pi|=|q_n|\left|\pi+\frac{A_n}{B_n}\right|}       \tag{29}
$$



is invariant under every scaling or content removal.  Combining it with
(19) gives the sharp division of labor:

* if
  $\liminf n^{-1}\log|q_n|>a(\kappa)$ and the phase in
  (18) has no exponential loss, then the primitive forms grow
  exponentially and this branch is a no-go;
* if a nonzero primitive form tends to zero, then either
  $\liminf n^{-1}\log|q_n|\leq a(\kappa)$, or the exact value has an
  additional exponential phase cancellation not detected by the leading
  fixed-slope determinant.

For `kappa -> infinity`, replace the fixed-slope threshold by



$$
\log|q_n|>n(4\kappa)^{-1/4}(1+o(1)).                      \tag{30}
$$



At `kappa=c log n`, this is `log|q_n|` larger than a constant multiple of
`n/(log n)^(1/4)`.  The expected endpoint height `exp(Theta(k))` is vastly
larger, but no proved lower bound survives the determinant content (10).

## 6. A rigorous pre-primitive no-go

A universal clearing denominator from the exact Hermite reduction is



$$
\Delta_{n,k}=
 2^{3(k-1)-s_2(k-1)+k}
 \operatorname {lcm}(1,\ldots,k-1)
 \operatorname {lcm}(1,\ldots,2n+1).                       \tag{31}
$$



Take `Delta_s=Delta_(n,k+s)` in Section 2.  If `k/n -> kappa` is fixed,
the prime number theorem in its equivalent Chebyshev form gives



$$
\frac1n\log\Delta_{n,k+s}
 =\delta(\kappa)+o(1),\qquad
 \delta(\kappa)=4\kappa\log2+\kappa+2.                    \tag{32}
$$



Under the non-exponential phase condition in Theorem 3.1, the completely
cleared value (9) has rate



$$
\boxed{
 G(\kappa)=3\delta(\kappa)+e(\kappa)+\ell(\kappa)+j(\kappa).}
                                                                    \tag{33}
$$



On the dominant branch `ell>=j`, this rate is strictly positive.  Indeed,
evaluation at `y=1` and `x=1/2` gives



$$
e\geq(1-\kappa)\log2,\qquad
 j\geq-2\log2-\kappa\log(17/16),                           \tag{34}
$$



and hence



$$
G(\kappa)\geq
 (11\kappa-3)\log2+3\kappa+6
 -2\kappa\log(17/16)>0\qquad(\kappa\geq1/2).              \tag{35}
$$



At the transition,



$$
e_0=0.423324333147158574\ldots,\qquad
 G(1/2)=10.643873127064585\ldots .                          \tag{36}
$$



Thus the published fully cleared integer form is very far from zero.  If
`g_n` is the exact content (10), a primitive form tending to zero would
require



$$
\frac1n\log g_n\geq G(\kappa)-o(1)                        \tag{37}
$$



along every phase-separated subsequence.  This is a precise no-go before
primitive reduction and a precise description of the only possible
primitive escape.  It is not an upper bound on `g_n`.

## 7. A proved boundary dyadic theorem

The dyadic law of the `L cross E` coefficient vector can be proved for
every `m`; it is not a finite-scan inference.  The useful statement is
slightly more general.

Let



$$
F_m(x)=x^{4m}(1-x)^{4m},\qquad D=x\frac d{dx},\qquad
 P_K(T)=\prod_{r=1}^K(4r-1-T),                              \tag{38}
$$



and reduce `P_K(D)F_m` modulo `x^4+1`:



$$
P_K(D)F_m\equiv a_K+b_Kx+c_Kx^2+d_Kx^3.
$$



Put `v_K=(a_K-c_K,a_K+c_K)`.  Thus `v_K` is exactly the raw
integer `(L,E)` pair before division by `4^K K!`.

**Lemma 7.1 (raw two-adic Wronskians).**  For every `m>=1` and `K>=0`,



$$
\begin{aligned}
 v_2(a_K-c_K)=v_2(a_K+c_K)&=m,\\
 v_2\det(v_K,v_{K+1})&=2m+2+v_2(m),\\
 v_2\det(v_K,v_{K+2})&=2m+3+v_2(m).                       \tag{39}
 \end{aligned}
$$



Here is a direct proof, included to make clear that (39) is not being
extrapolated from the certificate.  Work in
`R=Z[x]/(x^4+1)` and let `rho(a+bx+cx^2+dx^3)=(a-c,a+c)`.
For `g=x^4(1-x)^4`, reduction after the dilation `x -> exp(t)x` gives



$$
[g(e^t x)]=e^{8t}-e^{4t}+4e^{5t}x-6e^{6t}x^2+4e^{7t}x^3
             =2h_t.                                      \tag{40}
$$



All ordinary derivatives of `h_t` at zero lie in `R`.  Explicitly,



$$
h_r:=\left.\frac{d^r h_t}{dt^r}\right|_{t=0}
 =\frac{8^r-4^r}{2}+2\,5^r x-3\,6^r x^2+2\,7^r x^3,       \tag{41}
$$



where the constant in (41) is zero for `r=0`.  Since `F_m=g^m`,



$$
[D^rF_m]=2^m\left.\frac{d^r}{dt^r}h_t^m\right|_{t=0}.     \tag{42}
$$



Modulo two, `h_0=x^2`; hence
`2^{-m}[F_m]=x^{2m} (mod 2)`.  This proves the first line of
(39): exactly one of `a_K/2^m,c_K/2^m` is odd, according as `m` is
even or odd, and the constant term of `P_K` is odd.  Terms containing
`D` do not change this residue.  For completeness, the extra precision
needed for the two determinants follows by substituting (41) in the
ordinary Bell-polynomial expansion of the right side of (42).  If



$$
Q_K(T)=\frac{P_K(T)}{P_K(0)}\in\mathbb Z_2[T],
$$



write `q_1=[T]Q_K` and put



$$
u=(1,1),\qquad
 \epsilon_m=\begin{cases}(1,0),&m\text{ odd},\\(0,1),&m\text{ even}.
 \end{cases}
$$



Here are the details of the reduction.  Formula (41) gives `h_r in 2R`
for every `r>=1`, and direct multiplication gives



$$
h_0^4\equiv1\pmod8,\qquad
 B_{r,2}(h_1,h_2,\ldots)\equiv0\pmod8,                   \tag{42a}
$$



where `B_(r,2)` is the partial Bell polynomial.  In the Bell expansion
of the derivative of `h_t^m`, every term with at least three
differentiated factors lies in `8R`; after division by `m`, (42a) therefore
leaves



$$
\frac1m\left.\frac{d^r}{dt^r}h_t^m\right|_{t=0}
 \equiv h_0^{m-1}h_r\pmod8.                              \tag{42b}
$$



Using (41) and the four possible powers of `h_0` in (42b) gives



$$
\rho(h_0^{m-1}h_r)\equiv
 \begin{cases}
 4\epsilon_m,&r=1,\\
 4u,&r=2,\\
 (0,0),&r\ge3
 \end{cases}\pmod8.                                    \tag{42c}
$$



Equations (42b)--(42c), applied termwise to `Q_K`, give the explicit
congruences



$$
\begin{aligned}
 2^{-m}\rho(Q_K(D)F_m)&\equiv u,\\
 (4m\,2^m)^{-1}\rho(Q_K(D)DF_m)&\equiv\epsilon_m+q_1u,\\
 (4m\,2^m)^{-1}\rho(Q_K(D)D^2F_m)&\equiv u
 \end{aligned}\qquad(\bmod 2).                           \tag{43a}
$$



Here is the promised extra bit explicitly.  Define



$$
A_{m,K}=2^{-m}\rho(Q_K(D)F_m),\qquad
 B_{m,K}=(4m\,2^m)^{-1}\rho(Q_K(D)D^2F_m).               \tag{43e}
$$



There is a small but important precision point here: because the second
quantity in (43e) is divided by `4m`, its residue modulo eight must be
computed *before that division modulo 32*, not merely modulo eight.  We
give that computation explicitly.  Let `\mathfrak B_{s,p}` be the
ordinary partial Bell polynomial, so that, exactly in `R`,



$$
{1\over m}{d^s\over dt^s}h_t^m\bigg|_{t=0}
 =\sum_{p=1}^{\min(s,m)}(m-1)_{p-1}h_0^{m-p}
       \mathfrak B_{s,p}(h_1,h_2,\ldots).                 \tag{43e1}
$$



If `Q_K(T)=sum_(r=0)^K q_rT^r`, (43e1) gives the exact formula



$$
B_{m,K}={1\over4}\rho\sum_{r=0}^Kq_r
 \sum_{p=1}^{\min(r+2,m)}(m-1)_{p-1}h_0^{m-p}
       \mathfrak B_{r+2,p}(h_1,h_2,\ldots).              \tag{43e2}
$$



Formula (41) says `h_s in 2R` for every `s>=1`; consequently
`\mathfrak B_(s,p) in 2^pR`.  After the division by four in
(43e2), every term with `p>=5` is zero modulo eight.  Thus the raw
calculation really is a modulo-32 calculation, but only the four cases
`p=1,2,3,4` can survive.  There is no unbounded Bell tail hidden in the
table below.

For reference, the periodic reductions used in that finite calculation
are



$$
\begin{gathered}
 h_0^4=1+8w,\qquad w=72-51x+51x^3,\\
 \mathfrak B_{s,2}\equiv0\pmod8,\qquad
 \rho\{h_0^a(h_0^4-1)h_s\}\equiv(0,0)\pmod{32}
       \quad(a\ge0,\ s\ge1),                             \tag{43e3}\\
 \prod_{j=1}^4\left(1-{\lambda\over4(K+j)-1}\right)
       \equiv1\pmod {16}\quad(\lambda\in2\mathbb Z).  \tag{43e4}
 \end{gathered}
$$



All congruences in (43e3)--(43e4) are in the indicated free
`2`-adic module.  Here is a short verification.  The first equality is
ordinary multiplication in `R`.  For the last congruence in (43e3),
divide the two factors by `8` and `2`, respectively, and work modulo
two.  One has



$$
w\equiv x+x^3,\quad h_0\equiv x^2,\quad
 h_1/2\equiv1+x+x^2+x^3,\quad
 h_s/2\equiv x+x^3\ (s\ge2),
$$



and `(x+x^3)^2=(x+x^3)(1+x+x^2+x^3)=0` in
`F_2[x]/(x^4+1)`.  The middle congruence in (43e3) follows by pairing
the two symmetric terms in `\mathfrak B_(s,2)`; its possible central
term is also zero modulo eight by the same displayed residues.  Finally,
(43e4) follows by putting `lambda=2u`, reducing the four odd inverses
modulo 16, and multiplying the four factors; the four denominators are
`4K+3,4K+7,4K+11,4K+15` modulo 16.

Equations (43e2)--(43e3) also prove `B_(m+4,K)=B_(m,K)` modulo
eight.  Indeed, for `p=2,3,4` the changes in
`(m-1)_(p-1)` are respectively divisible by `4,4,2`, while
`\mathfrak B_(s,p)/4` is respectively divisible by `2,2,4`; the
change in the power of `h_0` is killed by `h_0^4-1`.  The `p=1`
case is exactly the last congruence in (43e3).  The cases `m<4`, where
a terminal Bell term is absent, follow by direct substitution in
(43e2).  Equation (43e4) proves `K`-period four: `rho` retains only
the even dilation eigenvalues, and a `p`-factor Bell term already
contains `2^p`, so the factor `16` in (43e4) remains zero modulo eight
after division by four.  The identical, easier argument modulo eight
applies to `A_(m,K)`.

It remains only to evaluate the sixteen representatives.  Substitution
of (41) into (43e2), using



$$
Q_0=1,\quad Q_1=1-T/3,\quad
 Q_2=(1-T/3)(1-T/7),\quad
 Q_3=Q_2(1-T/11),
$$



in `R/32R` gives the following complete component calculation.  Each
entry is `A_(m,K);B_(m,K)` modulo eight; this is a finite residue
calculation justified by (43e1)--(43e4), rather than a finite scan in
`m` or `K`.



$$
\begin{array}{c|cccc}
m\backslash K&0&1&2&3\\ \hline
1&(3,5);(1,3)&(7,5);(3,1)&(7,1);(1,3)&(3,1);(3,1)\\
2&(7,7);(3,3)&(7,7);(5,1)&(7,7);(7,7)&(7,7);(1,5)\\
3&(5,3);(3,1)&(1,3);(1,3)&(1,7);(3,1)&(5,7);(1,3)\\
0&(1,1);(1,1)&(1,1);(7,3)&(1,1);(5,5)&(1,1);(3,7)
\end{array}                                               \tag{43f}
$$



Taking the two-by-two determinant in every cell gives the single formula



$$
\boxed{\det(A_{m,K},B_{m,K})\equiv4(m+K)\pmod8.}         \tag{43g}
$$



In particular the determinant is always zero modulo four.  Thus (43g),
rather than an unrecorded higher-precision assertion, supplies the second
line below.

Together, (43a) and (43g) give the determinant statements



$$
\begin{aligned}
 v_2\det\{\rho(Q_K(D)F_m),\rho(Q_K(D)DF_m)\}
     &=2m+2+v_2(m),\\
 v_2\det\{\rho(Q_K(D)F_m),\rho(Q_K(D)D^2F_m)\}
     &\ge 2m+4+v_2(m).                                   \tag{43}
 \end{aligned}
$$



Thus the first determinant in (43), divided by `2^(2m)4m`, is odd,
while the second is divisible by four after the same division.  All the
congruences above take place in the free rank-four ring `R`, so no
root-of-unity division or numerical inference is involved.

Now



$$
\frac{Q_{K+1}(T)}{Q_K(T)}=1-\frac{T}{4K+3}.               \tag{44}
$$



The first formula in (43) and (44) prove the adjacent-minor assertion.
For a two-step jump,



$$
\frac{Q_{K+2}(T)}{Q_K(T)}-1
 =-\left(\frac1{4K+3}+\frac1{4K+7}\right)T
   +\frac{T^2}{(4K+3)(4K+7)}.                             \tag{45}
$$



The coefficient of `T` in (45) has valuation exactly one.  The second
line of (43) shows that the `T^2` contribution has at least one additional
power of two and therefore cannot cancel it.  This proves the last line of
(39).

We now specialize to `K=2m`.  Since



$$
v_2(4^K K!)=3K-s_2(K),                                  \tag{46}
$$



the exact reduced denominator exponents of each of `L_s,E_s` are



$$
d_0=5m-s_2(m),\quad d_1=d_0+2,\quad
 d_2=d_0+5+v_2(m+1).                                     \tag{47}
$$



Apply (39) to the three minors and then clear their powers of two.
Odd common content cannot alter a two-adic valuation, so the primitive
integer representative `C=L cross E` satisfies the proved identity



$$
\boxed{(v_2(C_0),v_2(C_1),v_2(C_2))
       =(0,3,5+v_2(m+1)).}                                \tag{48}
$$



Put `n=4m,k=2m+1`.  For the first odd coordinate one obtains an exact
terminating sum.  Substituting `j=4h+1` in the Hermite residue formula and
using the half-integer gamma values gives



$$
\boxed{
 b_{4m,2m+1}=-\frac1{4^{2m}}
 \sum_{h=0}^{m-1}\binom{4m}{4h+1}
 \frac{(2m-2h)!(2m+2h)!}
 {(m-h)!(m+h)!(2m)!}.}                                    \tag{49}
$$



For every `h`, the factor `4^(-2m)` times the factorial ratio in (49)
has the same 2-adic valuation `-4m+s_2(m)`.  If `S_m` denotes the sum in
(49), the observed denominator law



$$
v_2(\operatorname {den}b_{4m,2m+1})
 =3m-s_2(m)-v_2(m)-1                                     \tag{50}
$$



is equivalent to the single exact assertion



$$
v_2(S_m)=m+s_2(m)+v_2(m)+1,                             \tag{50a}
$$



an explicit weighted Fleck-type congruence.
Equation (49) is proved; (50) has been checked through `m=30` in the
attached certificate but is not
proved here.

For the rational endpoint pair, the exact scan further finds



$$
\begin{aligned}
 v_2(\operatorname {den}A)&=m+1+s_2(m),\\
 v_2(\operatorname {den}B)&=3m-s_2(m)+2-v_2(m).            \tag{51}
\end{aligned}
$$



In the diagnostic data, the first term `C_0b_0/8` has uniquely smallest
2-adic valuation in `B`.  Thus (50), the corresponding inequalities for
`b_1,b_2`, and the proved formula (48) would prove the second line above.
These endpoint assertions, unlike (48), remain conjectural.
If they hold, the power of two needed for the primitive rational pair is



$$
2^{3m-s_2(m)+2-v_2(m)}
 =\exp\{(3\log2/4+o(1))n\}.                                \tag{52}
$$



This is the missing kind of lower-denominator statement, but by itself it
is not enough: `3 log(2)/4=0.519860385...` is below the transition
approximation exponent (27).  The odd denominator of `A`, the size of the
odd numerator of `B`, and their gcd in (10) decide the outcome.  The
certificate finds positive primitive-value exponents at every tested
fixed and boundary slope, but those computations are diagnostics only.

## 8. Conclusion

The rational cross product is analytically stronger than the quadratic-
field positive kernel: it gives genuine rational approximations to `pi`,
with the exact fixed-slope exponent (5).  It is nevertheless not a proved
primitive construction.  Fixed or slowly varying `kappa` changes the
required primitive-height threshold from the positive constant (27) to
the smaller critical value (28); it does not control the determinant gcd.

The strongest rigorous no-go presently available is therefore:

*the universally denominator-cleared form grows exponentially throughout
the admissible fixed-slope branch, and any primitive counterexample must
remove that growth through the exact content `gcd(8U,V)`.*

Proving (50) and the two endpoint laws following it, and then controlling
the odd part of that gcd, is the remaining arithmetic problem.  Until
those steps are completed, no
`kappa` can honestly be declared to produce vanishing primitive forms, but
neither can all `kappa` be ruled out.
