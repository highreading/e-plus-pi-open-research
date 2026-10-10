> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Cubic power kernels: an exact field obstruction and a mixed-period branch

Date: 2026-08-27.

## 1. Scope and conclusions

This note treats two degree-three denominators.  The conclusions are quite
different.

1.  For

    

$$
J^{(3)}_{n,k}=\int_0^1 {x^n(1-x)^n\over(1+x^3)^k}\,dx,              \tag{1}
$$



    exact Hermite reduction gives

    

$$
J^{(3)}_{n,k}=R_{n,k}+{L_{n,k}\over3}\log2
             +{E_{n,k}\over3\sqrt3}\pi,qquad R_{n,k},L_{n,k},E_{n,k}\in\mathbb Q.
                                                                         \tag{2}
$$



    Therefore a rational combination which cancels `log 2` lies in
    `Q+Q pi/sqrt(3)`, not in `Q+Q pi`.  It cannot have a nonzero rational
    `pi` coefficient.  Allowing coefficients in `Q(sqrt(3))` does not
    rescue the natural three-power construction: its common three-by-three
    determinant factors out of both rational coordinates and disappears
    on primitive reduction.  This is an exact, all-slope obstruction.

2.  For the mixed denominator

    

$$
Q(x)=(1+x)(1+x^2)=1+x+x^2+x^3                         \tag{3}
$$



    the periods are genuinely rational:

    

$$
H_{n,k}=\int_0^1{x^n(1-x)^n\over Q(x)^k}\,dx
       =R_{n,k}+{L_{n,k}\over4}\log2+{E_{n,k}\over8}\pi.  \tag{4}
$$



    Two adjacent powers now give an exact rational `1,pi` form.  We give
    its exact primitive-content invariant and a coarse proved universal
    clearing.  Exact boundary scans show shrinking primitive forms through
    `n=60`, but this is not promoted to an asymptotic theorem: the log
    residue is oscillatory and the endpoint determinant gcd is not yet
    controlled.  Inversion gives a favorable raw integral balance below
    slope one, but a surviving rational half-line boundary term prevents
    one from identifying that balance with the `pi` coordinate.

Nothing here proves or disproves the transcendence of `e+pi`.

## 2. Exact reduction for `1+x^3`

For integers `m>=0` and `j>=2`, direct differentiation gives



$$
{x^m\over(1+x^3)^j}
 ={1\over3(j-1)}{d\over dx}{x^{m+1}\over(1+x^3)^{j-1}}
 +{3j-m-4\over3(j-1)}{x^m\over(1+x^3)^{j-1}}.             \tag{5}
$$



On `[0,1]` the derivative contributes the rational number



$$
{1\over3(j-1)2^{j-1}}.                                   \tag{6}
$$



After `k-1` lowering steps, the coefficient of the final simple-pole
integral is



$$
A^{(3)}_{m,k}
 =\prod_{s=1}^{k-1}{3s-m-1\over3s}
 =[z^{k-1}](1-z)^{(m-2)/3}.                               \tag{7}
$$



The coefficient identity follows from the generalized binomial theorem.
Writing `m=3q+r`, `0<=r<3`, polynomial division gives



$$
{x^m\over1+x^3}
 =\sum_{h=0}^{q-1}(-1)^h x^{3(q-1-h)+r}
   +(-1)^q{x^r\over1+x^3}.                                \tag{8}
$$



Thus every term in the expansion of `x^n(1-x)^n` has a completely
explicit rational endpoint part and one of only three base periods.  Those
periods are



$$
\begin{aligned}
 I_0&=\int_0^1{dx\over1+x^3}={\log2\over3}+{\pi\over3\sqrt3},\\
 I_1&=\int_0^1{x\,dx\over1+x^3}=-{\log2\over3}+{\pi\over3\sqrt3},\\
 I_2&=\int_0^1{x^2\,dx\over1+x^3}={\log2\over3}.          \tag{9}
 \end{aligned}
$$



If `a_0,a_1,a_2` are the three rational coefficients left by (5)--(8),
then



$$
L=a_0-a_1+a_2,qquad E=a_0+a_1,                           \tag{10}
$$



which proves (2).  The companion certificate implements (5)--(10) with
`fractions.Fraction` and checks the result against direct quadrature.

## 3. The coefficient-field obstruction

Take any finite rational coefficient vector `C=(C_s)` and put



$$
R_C=C\mathbin\cdot R,quad L_C=C\mathbin\cdot L,quad
 E_C=C\mathbin\cdot E.                                    \tag{11}
$$



If `L_C=0`, then



$$
C\mathbin\cdot J^{(3)}=R_C+{E_C\over3\sqrt3}\pi.        \tag{12}
$$



Suppose (12) also equals `A+B pi` with `A,B in Q`.  Since `pi` is
transcendental,



$$
R_C=A,qquad {E_C\over3\sqrt3}=B.                         \tag{13}
$$



The second equality has rational left numerator and rational right side;
it forces `E_C=B=0`.  Hence:

**Theorem 3.1.**  No rational log-cancelling combination of any number of
the integrals (1) produces a `Q+Q pi` form with nonzero rational `pi`
coefficient.  In particular, two adjacent powers cancel `log 2` by



$$
(C_0,C_1)=(L_{k+1},-L_k),                                \tag{14}
$$



but the result is a rational form in `1,pi/sqrt(3)`, not in `1,pi`.
Three adjacent powers merely give the rank-two rational lattice
`C dot L=0`; every vector in it has the same field obstruction.

There is a tempting quadratic-field workaround, but it is algebraically
empty.  For three adjacent powers write



$$
L=(L_0,L_1,L_2),\quad E=(E_0,E_1,E_2),\quad R=(R_0,R_1,R_2),
$$



and let



$$
D=\det\begin{pmatrix}L\\E\\R\end{pmatrix}.              \tag{15}
$$



Take coefficients `C=u+sqrt(3)v`, with `u,v in Q^3`.  Requiring the
Hermite coordinates of `C dot J` to belong to `Q+Q pi` imposes



$$
u\mathbin\cdot L=v\mathbin\cdot L=0,qquad
 u\mathbin\cdot E=0,qquad v\mathbin\cdot R=0.            \tag{16}
$$



If `D` is nonzero, (16) has exactly



$$
u=\alpha(L\times E),qquad v=\beta(L\times R),qquad
 \alpha,\beta\in\mathbb Q.                               \tag{17}
$$



The scalar triple-product identities give



$$
(L\times E)\mathbin\cdot R=D,qquad
 (L\times R)\mathbin\cdot E=-D,                          \tag{18}
$$



and hence



$$
\boxed{C\mathbin\cdot J^{(3)}=D\left(\alpha-\frac{\beta}{3}\pi\right).}
                                                                         \tag{19}
$$



The determinant `D` is common content.  After primitive scaling, the pair
is simply proportional to `(3 alpha,-beta)`; `alpha` and `beta` were free
external choices.  Thus the kernel supplies no rational approximation in
this construction.  If `D=0`, (17) need not describe the entire kernel,
but (12) still proves the rational-coefficient obstruction.  The
certificate verifies (18)--(19) exactly at several nonzero determinants;
the displayed finite checks are not used to prove the vector identity.

## 4. Exact Hermite coordinates for the mixed denominator

Let `P` be a rational polynomial and `j>=2`.  Since `Q` is square-free,
write



$$
{P\over Q^j}={d\over dx}\left({U\over Q^{j-1}}\right)
                   +{V\over Q^{j-1}}.                    \tag{20}
$$



Modulo `Q`, this is solved by



$$
U\equiv-{P\over j-1}(Q')^{-1}\pmod Q,qquad
 (Q')^{-1}\equiv{x^2-x\over4}\pmod Q.                   \tag{21}
$$



Choosing `deg U<3` determines `V` by exact monic polynomial division.
The boundary contribution is



$$
{U(1)\over Q(1)^{j-1}}-{U(0)\over Q(0)^{j-1}}
 ={U(1)\over4^{j-1}}-U(0).                               \tag{22}
$$



The factor in (22) is `4`, not `8`.

After the final lowering and polynomial division, let the remainder be
`S=a+bx+cx^2`.  Its partial fractions are



$$
{S\over Q}={A\over x+1}+{Bx+C\over x^2+1},               \tag{23}
$$



where



$$
A={a-b+c\over2},\quad B={-a+b+c\over2},\quad
 C={a+b-c\over2}.                                        \tag{24}
$$



Integration over `[0,1]` gives



$$
\int_0^1{S\over Q}\,dx
 ={a-b+3c\over4}\log2+{a+b-c\over8}\pi.                 \tag{25}
$$



Equations (20)--(25) prove (4), with



$$
L=a-b+3c,qquad E=a+b-c.                                 \tag{26}
$$



There is also a useful residue description.  If `3k>2n+1`, the rational
function is `O(x^{-2})` at infinity, so the sum of its finite residues is
zero.  Put



$$
\begin{aligned}
 r_{-1}&=[t^{k-1}]{P_n(-1+t)\over(t^2-2t+2)^k},\\
 r_i&=[t^{k-1}]{P_n(i+t)\over[(1+i+t)(2i+t)]^k}.           \tag{27}
 \end{aligned}
$$



Comparing (23)--(24) with the residues at `-1,i,-i` yields the exact
proper-range identities



$$
L=2r_{-1},qquad E=-4\operatorname {Im}r_i.               \tag{28}
$$



Thus the mixed branch has one real coefficient saddle and one genuinely
complex, potentially oscillatory coefficient saddle.

## 5. Two and three adjacent mixed powers

For two adjacent powers abbreviate `H_s=H_(n,k+s)` and similarly for the
coordinates.  The vector



$$
(C_0,C_1)=(L_1,-L_0)                                    \tag{29}
$$



cancels `log 2` exactly and gives



$$
\Lambda=L_1H_0-L_0H_1=A+B\pi,                            \tag{30}
$$



where



$$
A=L_1R_0-L_0R_1,qquad B={L_1E_0-L_0E_1\over8}.          \tag{31}
$$



Unlike Theorem 3.1, both coordinates in (31) are rational.  Three
adjacent powers give the rank-two rational lattice `C dot L=0`; the two
distinguished directions `L cross E` and `L cross R` respectively cancel
the `pi` and rational coordinates.  There is no coefficient-field
collapse: the arithmetic of the resulting two-dimensional image lattice
is genuine.

Here is an exact clearing and content statement.  Put



$$
M_N=\operatorname {lcm}(1,2,\ldots,N),qquad
 \Delta_{n,k}=4^k(k-1)!M_{2n+1}.                          \tag{32}
$$



Then `Delta_(n,k)` clears `R_(n,k),L_(n,k),E_(n,k)`.  Indeed,
each use of (21) introduces only `4(j-1)`; the endpoint at one introduces
`4^(j-1)`; monic division introduces nothing; and integration of the
terminal polynomial is cleared by `M_(2n+1)`.  More explicitly, the
numerator at level `j` is cleared by



$$
4^{k-j}{(k-1)!\over(j-1)!},                              \tag{33}
$$



which makes (32) immediate.

Choose any simultaneous column clearings `Delta_0,Delta_1` and write



$$
(\lambda_s,\rho_s,\epsilon_s)=Delta_s(L_s,R_s,E_s)\in\mathbb Z^3.
                                                                         \tag{34}
$$



Define



$$
U=\lambda_1\rho_0-\lambda_0\rho_1,qquad
 V=\lambda_1\epsilon_0-\lambda_0\epsilon_1.              \tag{35}
$$



Then



$$
\boxed{8\Delta_0\Delta_1\Lambda=8U+V\pi.}              \tag{36}
$$



Consequently, with `g=gcd(8U,V)`, the primitive integer pair is



$$
(p,q)=\left({8U\over g},{V\over g}\right).              \tag{37}
$$



This is invariant under the choice of the column clearings.  Formula
(37), not the coarse size of (32), is the correct arithmetic object.  A
proof that the primitive forms tend to zero must control the determinant
gcd `g`; a universal denominator alone cannot settle the branch.

## 6. Inversion and the saddle boundary

For even `n`, reciprocity `Q(1/x)=x^{-3}Q(x)` gives the exact identity



$$
\int_1^\infty {P_n(x)\over Q(x)^k}\,dx
 =\int_0^1 t^{3k-3n-2}{P_n(t)\over Q(t)^k}\,dt.           \tag{38}
$$



The properness boundary is `3k>2n+1`, hence `k/n` approaches `2/3` at
the lowest admissible powers.  The inversion balance is instead at slope
one.  If `k/n -> kappa`, the raw `[0,1]` and inverted-tail Laplace phases
are



$$
\begin{aligned}
 \phi_0(x)&=\log x+\log(1-x)-\kappa\log Q(x),\\
 \phi_\infty(x)&=(3\kappa-2)\log x+\log(1-x)-\kappa\log Q(x).
                                                                    \tag{39}
 \end{aligned}
$$



For `2/3<kappa<1`,



$$
\phi_\infty(x)-\phi_0(x)=3(\kappa-1)\log x>0
 \quad(0<x<1),                                           \tag{40}
$$



so the positive raw tail has a strictly larger exponential rate.  At
`kappa=2/3` its maximum is the endpoint `x=0` with rate zero; at
`kappa=1` the two phases coincide.  Standard Laplace upper and lower
bounds make these statements rigorous for the positive raw integrals.
For example, at the properness boundary,



$$
\max_{0<x<1}\phi_0(x)=-1.7498296312071695\ldots,          \tag{41}
$$



where the maximizer is the unique root in `(0,1)` of



$$
5x^3+5x^2+5x-3=0.                                       \tag{42}
$$



However, (38)--(41) are **not** yet an asymptotic theorem for (30).
The rational derivative boundary at zero generally survives on
`[0,infinity)`.  In particular, the smallest proper example is



$$
H_{2,2}={3\over4}-{1\over2}\log2-{1\over8}\pi,qquad
 \int_0^\infty {x^2(1-x)^2\over Q(x)^2}\,dx=1-{\pi\over4}. \tag{43}
$$



Thus the half-line integral is not simply a constant times the `pi`
coordinate; its large rational endpoint part can cancel that coordinate.
Any argument which replaces `B` in (31) by a positive half-line integral
is invalid.

The actual period saddles come from (27).  Their formal phase functions
are



$$
\begin{aligned}
 \psi_{-1}(t)&=\log(t-1)+\log(2-t)
   -\kappa\log(t^2-2t+2)-\kappa\log t,\\
 \psi_i(t)&=\log(i+t)+\log(1-i-t)
   -\kappa\log(1+i+t)-\kappa\log(2i+t)-\kappa\log t.
                                                                  \tag{44}
 \end{aligned}
$$



Their stationary equations are obtained by differentiating (44).  The
`i` equation, for example, is



$$
{1\over i+t}-{1\over1-i-t}-{\kappa\over1+i+t}
 -{\kappa\over2i+t}-{\kappa\over t}=0.                   \tag{45}
$$



A proof of primitive convergence must identify the accessible saddles in
(44), control their real projections uniformly, and combine that with
the exact gcd (37).  This contour-and-content step is open in this note.

## 7. Exact diagnostics and theorem boundary

The companion script performs exact rational Hermite reduction, followed
by high-precision evaluation only after the primitive integers have been
formed.  On the boundary ray



$$
n=6m,qquad k=4m+1,                                      \tag{46}
$$



selected results are



$$
\begin{array}{c|c|c|c|c}
n&k&n^{-1}\log|p+q\pi|&n^{-1}\log|\pi+p/q|&n^{-1}\log|q|\\ \hline
6&5&-0.779020&-2.029660&1.250640\\
12&9&-0.534862&-2.183139&1.648276\\
24&17&-0.503546&-2.273682&1.770136\\
36&25&-0.591425&-2.331069&1.739644\\
48&33&-0.353000&-2.317774&1.964775\\
60&41&-0.317169&-2.308740&1.991571
\end{array}                                               \tag{47}
$$



The exact integer pairs and the pre-primitive denominator/content are in
the JSON certificate.  Every scanned form in (46), through `n=60`, is
smaller than one.  This is strong evidence that the mixed kernel deserves
further study, but (47) is a finite diagnostic, not a proof of an
asymptotic.  In particular:

* (5)--(19) are exact theorems and close the original `1+x^3` rational
  `1,pi` route;
* (20)--(38) and (43) are exact identities;
* (39)--(42) describe the raw positive-integral saddle balance;
* (44)--(47) isolate, but do not solve, the oscillatory saddle and
  primitive-content problem for the mixed kernel.

