> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# All-index shifted coefficient positivity for the two spectral branches

Date: 2026-09-13. Original bounded continuation by audit_results.

This note proves that both rationally normalized spectral branches have
nonnegative coefficients in the shifted variable xi−1. It follows that
their logarithmic derivatives and their ratios at adjacent large
prolate eigenvalues have explicit uniform bounds. Positivity in xi
itself, and real negative zeros, remain conjectural beyond the closed
diagnostic k<=12. The proved shifted result already gives the ratio
control sought from the stronger coefficient conjecture. It gives no
relative cofactor or mixed-moment determinant bound.

## 1. Definitions and the closed diagnostic

Use the branches in raw_spectral_branch_generating_function.md:



$$
r_k^{(0)}=p_k^{(0)}/\sqrt{2k+1},\qquad
r_k^{(1)}=\sqrt3\,p_k^{(1)}/\sqrt{2k+1}.
$$



Their seeds are respectively (r_0,r_1)=(1,1/2) and (0,1).
Their degree caps are floor(k/2) and floor((k−1)/2), respectively;
the zero branch r_0^(1) is excluded whenever a logarithm is used.
These are the plus-convention branches of F_k(x). Reflection of the
actual unknown polynomial introduces the previously recorded minus
sign in the odd high equations and does not change these branches.

The one predeclared exact diagnostic was k=0,...,12 in both branches.
The saved checker and JSON are
check_raw_branch_positive_coefficients.py and
raw_branch_positive_coefficients_checks.json. On this closed set:

- all25 nonzero branch polynomials have strictly positive coefficients
  in xi;
- all21 nonconstant polynomials have all roots real and strictly
  negative, certified by exact rational root isolation.

No larger index was computed. These finite observations are not the
proof below and do not establish the stronger all-index statements.

## 2. A first-difference recurrence with a positive shifted parameter

Suppress the branch superscript. For every k>=0, the exact normalized
row recurrence is



$$
U_k r_{k+2}=(\xi-d_k)r_k+u_k r_{k+1}
             +v_k r_{k-1}-w_k r_{k-2},                 \tag{1}
$$



where negative-index terms are omitted and



$$
\begin{aligned}
U_k&=\frac{(k+1)^2(k+2)^2}{(2k+1)(2k+3)},&
u_k&=\frac{(k+1)^2}{2k+1},\\
v_k&=\frac{k^2}{2k+1},&
w_k&=\frac{k^2(k-1)^2}{(2k+1)(2k-1)},\\
d_k&=\frac{(k+1)^4}{(2k+1)(2k+3)}
      +\frac{k^4}{(2k+1)(2k-1)}-k(k+1).
\end{aligned}
$$



Set D_0=0, D_1=r_1 and, for k>=2,



$$
D_k=k r_k-(k-1)r_{k-2}.
\tag{2}
$$



Then the following identity holds for every k>=0, with r_(-1)=0:



$$
\boxed{
D_{k+2}=A_kD_{k+1}+B_kD_k
       +C_k\bigl[(\xi-1)r_k+k r_{k-1}\bigr],}
\tag{3}
$$



where



$$
A_k=\frac{2k+3}{(k+1)(k+2)},\quad
B_k=\frac{k^2(k-1)(2k+3)}{(k+1)^2(k+2)(2k-1)},\quad
C_k=\frac{(2k+1)(2k+3)}{(k+1)^2(k+2)}.
\tag{4}
$$



Here B_0=B_1=0. For k>=2, B_k>0; A_k,C_k>0 for all k>=0.

For completeness, substitute
r_(k+1)=(D_(k+1)+k r_(k−1))/(k+1) and
r_(k−2)=(k r_k−D_k)/(k−1) in (1), for k>=2.
The two scalar simplifications are exactly



$$
d_k+\frac{k w_k}{k-1}+\frac{(k+1)U_k}{k+2}=1,
\qquad \frac{k u_k}{k+1}+v_k=k.
\tag{5}
$$



The remaining multipliers are
A_k=(k+2)u_k/((k+1)U_k),
B_k=(k+2)w_k/((k−1)U_k), C_k=(k+2)/U_k,
which give (3). At k=0, (1) gives
D_2=3r_1/2+3(xi−1)r_0/2, exactly (3).
At k=1 the w term is zero, and direct substitution of
r_2=(D_2+r_0)/2 gives (3) without any division by k−1.
Thus no exceptional small-index identity is assumed.

## 3. The unconditional positivity theorem

**Theorem.** For sigma=0,1 and every k>=0,
r_k^(sigma)(1+y) has nonnegative rational coefficients in y.
Every one of these polynomials except r_0^(1)=0 is nonzero and
strictly positive for real y>=0. The same coefficient nonnegativity
holds for D_k(1+y).

**Proof.** The seeds r_0,r_1,D_0,D_1 have the stated nonnegative
coefficients. Suppose the polynomials through the indices needed on
the right side of (3) have nonnegative coefficients. Formula (3),
with xi−1=y, has only nonnegative rational multipliers and the
additional nonnegative factor y. It gives the same property for
D_(k+2). Recover



$$
r_{k+2}=\frac{D_{k+2}+(k+1)r_k}{k+2}.              \tag{6}
$$



This gives nonnegative coefficients for r_(k+2), and induction closes.
Both branches have D_1=r_1>0 as a constant. Since A_k>0, (3) shows
successively that every D_k for k>=1 has a positive constant
coefficient. Formula (6) then gives a positive constant coefficient
for every r_k with k>=1; r_0^(0)=1 separately. This proves strict
positivity for y>=0 and completes the proof. □

The theorem does not assert positivity of every individual coefficient
in xi itself. For example the proof uses D_2^(0)=3xi/2−3/4,
whose constant coefficient in xi is negative. The shift is an actual
part of the proved invariant cone, not a suppressed sign assumption.

## 4. Logarithmic derivatives and adjacent spectral-node ratios

Let r be any nonzero branch above, of degree d. For real xi>1,
write r(xi)=sum_(j=0)^d a_j(xi−1)^j with a_j>=0. Then



$$
\boxed{0\le\frac{r'(\xi)}{r(\xi)}
             \le\frac{d}{\xi-1}.}
\tag{7}
$$



Indeed (xi−1)r'/r is the weighted mean of the integers j with
nonnegative weights a_j(xi−1)^j. Integrating (7) gives, for 1<x<=y,



$$
\boxed{1\le\frac{r(y)}{r(x)}
             \le\left(\frac{y-1}{x-1}\right)^d.}
\tag{8}
$$



Use the proved spectral enclosures
l(l+1)+3/4<=xi_l<=l(l+1)+1. For every l>=1 and integer h>=1,



$$
1\le\frac{r_k^{(\sigma)}(\xi_{l+h})}
               {r_k^{(\sigma)}(\xi_l)}
\le
\left(
\frac{(l+h)(l+h+1)}{l(l+1)-1/4}
\right)^{d_{k,\sigma}},
\tag{9}
$$



where d_(k,0)=floor(k/2), d_(k,1)=floor((k−1)/2) are safe upper
bounds; again omit k=0,sigma=1. This estimate holds at both parities
of the nodes for either polynomial branch, not only at its matching
physical parity. No analytic continuation estimate is being used:
the theorem applies to the polynomial at every xi>1.

For fixed h and k/l bounded, (9) supplies a uniform positive upper
and lower ratio bound as l grows. More precisely, if k/l->tau,



$$
\limsup_{l\to\infty}
\frac{r_k^{(\sigma)}(\xi_{l+h})}
     {r_k^{(\sigma)}(\xi_l)}\le e^{h\tau}.
\tag{10}
$$



If k/l->0, these ratios tend to1. For fixed h and k<=Cl,
the logarithmic derivative throughout the corresponding spectral
interval is O(1/l). This is the intended uniform growing-index
consequence, proved without the stronger unshifted conjecture.

There is also a useful complex consequence with an elementary proof.
For d>=1, R>0 and |theta|<pi/d,



$$
\left|r(1+Re^{i\theta})\right|
 \ge \cos(d|\theta|/2)\,r(1+R)>0.
\tag{11}
$$



Multiply the sum by exp(−id theta/2). Each resulting term has argument
(j−d/2)theta in [−d|theta|/2,d|theta|/2], so its real part is at
least its modulus times the cosine in(11). This proves both the lower
bound and the claimed zero-free sector. It makes no claim about all
complex zeros outside this sector.

In particular, for every real x>1 and
|z−x|<=(x−1)/(4d), write z−1=Re^(i theta). Then
R/(x−1) lies in[1−1/(4d),1+1/(4d)] and
|theta|<=arcsin(1/(4d))<=1/(2d). Monotonicity and(8), or directly
the positive coefficients, give



$$
\frac34\cos(1/4)\,r(x)
 \le |r(z)|\le e^{1/4}r(x).
\tag{12}
$$



For the lower comparison use
r(1+R)/r(x)>=(1−1/(4d))^d>=3/4 when R<=x−1;
if R>=x−1, monotonicity is stronger. The upper comparison is the
reverse argument and (1+1/(4d))^d<=exp(1/4). Thus, when x is of
order n² and d of order n, individual branches have a zero-free
complex neighborhood of radius of order n with uniform relative
upper and lower bounds. This remains an individual-branch statement,
not a noncancellation theorem for their mixed determinants.

## 5. Why a scalar orthogonality shortcut has not been established

The even subsequence of the even branch begins, in monic form,



$$
q_0=1,\quad q_1=\xi+1/6,\quad
q_2=\xi^2+\frac{30}{7}\xi+\frac{99}{70}.
$$



If these three polynomials obeyed the positive scalar Favard recurrence
q_2=(xi+alpha)q_1−beta q_0, coefficient comparison would require
alpha=173/42 and beta=−131/180<0. Thus these actual subsequences are
not automatically the scalar orthogonal polynomials of a positive
measure; those are the different polynomials pi_j^sigma in the
two-measure note. The finite negative-root observations therefore do
not come with an inferred scalar Favard proof.

The imaginary zeros of F_k also imply real interlacing for its centered
real and imaginary parts after the usual Hermite–Biehler change of
variables. Transporting that root statement through the polynomial
map f(T)v_sigma would need a separate root-preservation theorem; the
present proof does not assume one. It is unnecessary for (7)–(10).

## 6. Scope for the actual high-row problem

The positive shifted recurrence supplies an exact invariant cone and
uniform scalar branch-ratio bounds. It does not bound the relative
cancellation in determinants made from both branches at many nodes.
The high constraints still couple two positive spectral measures,
and the canonical endpoint rows still select a particular vector in
their two-dimensional high kernel. A useful next quantitative target
is to combine (9) with the proved spectral-amplitude ratios while
retaining the actual alternating cofactor expansion. No conditioning,
top-two concentration, primitive-height bound, or irrationality claim
is deduced merely from the scalar positivity theorem.
