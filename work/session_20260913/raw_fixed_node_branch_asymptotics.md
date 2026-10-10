> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Sharp fixed-node asymptotics for the actual spectral branches

Date: 2026-09-13. Original bounded continuation by audit_results.

The main new result is an actual coefficient asymptotic, not an inference
from a formal generating-function singularity. At every fixed prolate
node, the branch of matching reflection parity has the nonzero leading
term



$$
p_k^{(\ell\bmod2)}(\xi_\ell)
=\frac{\psi_\ell(1)}{2\pi g_\ell}
 k^{-3/4}e^{2\sqrt k}\bigl(1+O_\ell(k^{-1/2})\bigr).
\tag{1}
$$



The parameter and node are fixed while k tends to infinity. A separate
positivity comparison gives the sharp upper scale, uniformly on every
compact complex parameter set, for both branches. Neither result is a
growing-node cofactor estimate or an irrationality proof.

## 1. Normalizations and reviewed inputs

Use the plus convention of raw_spectral_branch_generating_function.md:
Q_k is the raw monic Legendre polynomial satisfying
Q_0=1, Q_1=x and Q_(k+1)=xQ_k+k²Q_(k−1)/(4k²−1). Let F_k be its
coefficientwise Borel transform, and put



$$
c_k=2^{-k}\binom{2k}{k},\qquad E_k=c_k\sqrt{2k+1}F_k.
$$



For the reviewed self-adjoint prolate operator, normalized eigenfunctions
psi_l and eigenvalues xi_l satisfy



$$
\langle E_k,\psi_\ell\rangle
=g_\ell p_k^{(\ell\bmod2)}(\xi_\ell),\qquad g_\ell\ne0,
\tag{2}
$$



where the two rational normalizations are



$$
r_k^{(0)}=p_k^{(0)}/\sqrt{2k+1},\qquad
r_k^{(1)}=\sqrt3\,p_k^{(1)}/\sqrt{2k+1}.
\tag{3}
$$



The spectral enclosures are
ell(ell+1)+3/4 <= xi_l <= ell(ell+1)+1. The finite-Fourier argument
in raw_boundary_free_moment_intertwiner.md gives entire continuation
of each psi_l. The independent amplitude theorem also gives nonzero
g_l (and fixes a phase with g_l>0). The all-index shifted positivity
theorem proves that r_k^(sigma)(1+y) has nonnegative coefficients in y.
These are the only spectral inputs used below.

Reflection of the actual unknown polynomial introduces the already
recorded minus sign in the odd high equations. It does not alter F_k,
the branch definitions, or (2).

## 2. Exact positive coefficients and their saddle range

The ordinary Legendre coefficient formula, followed by the Borel
transform, gives the exact positive identity



$$
c_kF_k(x)=\sum_{\substack{0\le d\le k\\d\equiv k\pmod2}}
 \frac{A_{k,d}x^d}{(d!)^2},\qquad
A_{k,d}=2^{-k}\frac{(k+d)!}
 {((k-d)/2)!\,((k+d)/2)!}.
\tag{4}
$$



For example k=1 gives x, and k=2 gives 1/2+3x²/4, fixing the
Borel and c_k normalization without a new degree scan. With
sigma=k mod2, consecutive admissible coefficients satisfy



$$
\frac{A_{k,d+2}}{A_{k,d}}=(k-d)(k+d+1)
=k(k+1)-d(d+1).
\tag{5}
$$



The lowest coefficients satisfy, by the central binomial coefficient
estimate (or Stirling's formula with its O(1/k) remainder),



$$
A_{k,0}=\sqrt{\frac2{\pi k}}(1+O(k^{-1}))\quad(k\text{ even}),
\qquad
\frac{A_{k,1}}k=\sqrt{\frac2{\pi k}}(1+O(k^{-1}))
\quad(k\text{ odd}).
\tag{6}
$$



Consequently, for every fixed L, uniformly over admissible d<=L sqrt(k),



$$
A_{k,d}=\sqrt{\frac2{\pi k}}\,k^d
 \bigl(1+O_L(k^{-1/2})\bigr).
\tag{7}
$$



To verify the error explicitly, divide each factor in (5) by k².
The resulting factor is 1+1/k−d(d+1)/k², which differs from1 by
O_L(1/k) in this range. There are O_L(sqrt(k)) factors. Taking their
logarithms proves an O_L(k^(-1/2)) total logarithmic error; (6)
supplies the initial factor. For sufficiently large k all these
factors are positive and bounded away from0, as required by this step.

A global bound follows without logarithmic approximation. With
kappa_k=sqrt(k(k+1)), every factor in (5) is at most kappa_k²;
the two initial bounds in (6) therefore imply



$$
0\le A_{k,d}\le Ck^{-1/2}\kappa_k^d
\quad(k\ge1),\qquad \kappa_k\le k+1.
\tag{8}
$$



For x in any fixed [a,b] with 0<a<=b, choose a fixed
L>4e sqrt(b+1). The part d>L sqrt(k) of the series controlled by
(8) is exponentially small in sqrt(k), even absolutely: use
d! >= (d/e)^d at the first tail index, and then the ratio bound
kappa_k b/(d+1)² < 1/2. The same argument applies to the comparison
series with k^d instead of A_(k,d). Thus truncating to the range of
(7) does not change its relative O_(a,b)(k^(-1/2)) precision.

## 3. The sharp actual Borel–Legendre coefficient estimate

For t>=0, the parity-filtered comparison series is



$$
\sum_{d\equiv\sigma\ (2)}\frac{t^d}{(d!)^2}
=\frac12\left[I_0(2\sqrt t)+(-1)^\sigma J_0(2\sqrt t)\right].
\tag{9}
$$



This follows directly from the Taylor series. The elementary integral
representations give |J_0(u)|<=1 for real u and



$$
I_0(u)=\frac1\pi\int_0^\pi e^{u\cos\theta}\,d\theta
=\frac{e^u}{\sqrt{2\pi u}}(1+O(u^{-1})),\qquad u\longrightarrow+\infty.
\tag{10}
$$



For completeness, the last estimate follows by splitting at a small
fixed positive angle, using a Gaussian upper bound on 1−cos(theta),
and putting theta=v/sqrt(u) near0. Taylor's formula for the cosine
gives a relative error bounded by O(u^(-1)) times the convergent
Gaussian fourth moment. A further split at v=u^(1/8) bounds the
Taylor remainder uniformly, and the complementary Gaussian tail is
smaller than any inverse power. All constants in (10) can therefore
be chosen uniformly for u in the positive rays used here.

The J_0 term in (9) is exponentially smaller than I_0 for t=kx,
x in [a,b]. Combining (7)–(10) proves



$$
\boxed{
c_kF_k(x)=\frac{e^{2\sqrt{kx}}}
 {2\pi\sqrt2\,k^{3/4}x^{1/4}}
 \left(1+O_{a,b}(k^{-1/2})\right),\quad x\in[a,b].}
\tag{11}
$$



This is uniform for both parities of k. It is a direct coefficient
proof, including control of the entire coefficient tail. In addition,
(8) and I_0(u)<=e^u give the useful global estimate



$$
0\le c_kF_k(x)\le Ck^{-1/2}e^{2\sqrt{(k+1)x}},
\qquad 0\le x\le1,\quad k\ge1.
\tag{12}
$$



## 4. Endpoint projection and the nonzero fixed-node constant

For every fixed f in C¹[0,1], (11)–(12) imply



$$
\boxed{
\int_0^1 c_kF_k(x)f(x)\,dx
=\frac{e^{2\sqrt k}}{2\pi\sqrt2\,k^{5/4}}
 \left[f(1)+O\!\left(\|f\|_{C^1}k^{-1/2}\right)\right].}
\tag{13}
$$



Indeed split at a fixed a in (0,1), say a=1/2. Equation (12) makes
the first part exponentially smaller than the scale in (13). On
[a,1], the uniform relative error in (11) is controlled after
integration by the same estimate with |f|. For its main integral,
put u=sqrt(x):



$$
\int_a^1 x^{-1/4}f(x)e^{2\sqrt{kx}}dx
=\int_{\sqrt a}^1 2u^{1/2}f(u^2)e^{2\sqrt k\,u}du
=\frac{e^{2\sqrt k}}{\sqrt k}
 \left[f(1)+O(\|f\|_{C^1}k^{-1/2})\right].
$$



One integration by parts, with the derivative of
2u^(1/2)f(u²) bounded on this interval, proves the last equality.
No sign assumption on f is required.

Apply (13) to f=psi_l and then multiply by sqrt(2k+1)/g_l in (2).
This proves (1), provided psi_l(1) is nonzero. Here is a local proof
of that fact. Set y(u)=psi_l((u+1)/2)/sqrt2. Its entire continuation
satisfies



$$
(1-u^2)y''-2uy'+(\xi_\ell-3/4-u^2/4)y=0.
\tag{14}
$$



If y had a zero of order r>=1 at u=1, the first nonzero coefficient
of the left side, at order r−1, would be −2r² times the leading
coefficient of y. This cannot vanish. An analytic function with
all derivatives zero would be identically zero, also excluded by
normalization. Hence y(1), and therefore psi_l(1), is nonzero.

The ratio psi_l(1)/g_l is phase invariant. In the reviewed phase
g_l>0, shifted positivity further shows psi_l(1)>0 for l>=1:
xi_l>1, all matching branch values are positive, and (1) has a
nonzero limiting constant. No sign claim for the ground-state phase
is needed for (1). The constants in (1) are uniform over nodes in
any fixed compact interval, since the spectral enclosure makes that
a finite set. They are not claimed uniform as l grows with k.

## 5. A sharp upper bound on every compact parameter set

Let K be a compact subset of C and R=max_(xi in K)|xi−1|. For each
sigma choose a fixed matching-parity actual node Lambda_sigma with
Lambda_sigma−1>=R and Lambda_sigma>1. Shifted coefficient positivity
gives, for every xi in K,



$$
|r_k^{(\sigma)}(\xi)|
\le r_k^{(\sigma)}(1+|\xi-1|)
\le r_k^{(\sigma)}(\Lambda_\sigma).
\tag{15}
$$



The right side is controlled by (1) and (3). Absorbing the finitely
many small indices into the constants gives



$$
\boxed{
\sup_{\xi\in K}|p_k^{(\sigma)}(\xi)|
\le C_K(k+1)^{-3/4}e^{2\sqrt{k+1}},\qquad \sigma=0,1,}
\tag{16}
$$



and



$$
\sup_{\xi\in K}|r_k^{(\sigma)}(\xi)|
\le C_K(k+1)^{-5/4}e^{2\sqrt{k+1}}.
\tag{17}
$$



The zero initial odd branch causes no exception. These are uniform
upper bounds for arbitrary complex parameters in a fixed compact
set; (1) supplies matching nonzero lower asymptotics at the actual
nodes. In particular the stretched exponential coefficient2 is sharp
for these nodes. An arbitrary-parameter nonzero leading constant,
or an opposite-parity asymptotic at the same node, is not asserted.

## 6. What the actual generating function does at z=1 and z=−1

This section records real-axis Abelian consequences and fixes the
distinction between the two generating objects. Put h_0=1, h_1=sqrt3.
At a matching node the auxiliary ODE solution is



$$
V_\sigma(w;\xi_\ell)
=\frac{h_\sigma}{g_\ell}\int_0^1 e^{wx}\psi_\ell(x)dx.
\tag{18}
$$



Thus as w tends to positive infinity,
V_sigma(w)=A_l e^w/w (1+O_l(1/w)), where
A_l=h_sigma psi_l(1)/g_l is nonzero. Its Taylor coefficients are
not the branch sequence r_k.

The actual generating function, reviewed in the earlier note, is



$$
\mathcal P_\sigma(z;\xi_\ell)
=\frac{h_\sigma}{g_\ell\sqrt{1-z^2}}
 \int_0^1 e^{x\eta}I_0(x\eta)\psi_\ell(x)dx,
\qquad \eta=\frac z{1-z^2},\quad |z|<1.
\tag{19}
$$



As z tends to1 from below, the same two endpoint Laplace estimates
give, with delta=1−z,



$$
\boxed{
\mathcal P_\sigma(z;\xi_\ell)
\sim\frac{A_\ell}{\sqrt{2\pi}}\,
 \delta\exp(1/\delta-1/2).}
\tag{20}
$$



For an explicit constant check, the right side of (19) is asymptotic
to A_l e^(2eta)/(2eta sqrt(2pi z)); use
2eta=delta^(-1)−1/2+O(delta). Contributions away from x=1 are
exponentially smaller, by I_0(t)<=e^t and (10).

As z tends to−1 from above, write eta=−R. The real integral instead
has the finite limit



$$
\boxed{
\lim_{z\to-1+}\mathcal P_\sigma(z;\xi_\ell)
=\frac{h_\sigma}{g_\ell\sqrt{2\pi}}
 \int_0^1 x^{-1/2}\psi_\ell(x)dx.}
\tag{21}
$$



Indeed e^(-t)I_0(t)<=C/sqrt(1+t) for t>=0, directly from the integral
in (10) and its Gaussian bound. Also
(1−z²)^(-1/2)/sqrt(R)=1/sqrt(−z), bounded near−1. Dominated
convergence with the integrable majorant Cx^(-1/2)|psi_l(x)| proves
(21). This limit may be zero; no nonvanishing assertion is required.

Equations (20)–(21) concern approach along the real axis. They are
not a complex singularity classification or a coefficient-transfer
theorem. The coefficient asymptotic (1) was established independently
in Sections2–4, including the parity term and all coefficient tails.
The matching auxiliary V is entire; for a general parameter or the
opposite branch, the previously specified slit-plane domain remains
the justified one.

## 7. Precise gain and remaining analytic target

This closes the fixed-node upper-growth problem with an actual
nonzero matching asymptotic. It replaces a generic exp(O(k)) bound
by the sharp e^(2sqrt(k)) scale uniformly on compact parameter sets.
It also resolves the leading parity issue for fixed matching nodes:
the bounded J_0 term cannot cancel the exponentially larger I_0 term.

It does not bound an inverse high-row spectral matrix, a determinant
with growing node set, or the final remainder after normalization.
To use this in the current high-row route, the next exact problem is
to control the transition from these fixed-node columns to nodes
growing with n, while retaining relative bounds after the actual
bordered determinant cancellation. The constants in (1) and (16)
must not be treated as uniform on that moving parameter range.

## 8. First node-dependent correction and a fixed two-column minor

The unknown universal correction to the main coefficient in (11)
can be avoided by normalizing with the actual positive row mass
L_k=integral_0^1 E_k(x)dx. For each fixed integer r>=0, the same
proof as (13), retaining the factor (1−x)^r, gives



$$
\frac{\int_0^1(1-x)^r E_k(x)dx}{L_k}
=\frac{r!}{k^{r/2}}\left(1+O_r(k^{-1/2})\right).
\tag{22}
$$



To check the constant and error, put u=sqrt(x) and then
v=2sqrt(k)(1−u) in the endpoint integral. The factor (1−x)^r
becomes (v/sqrt(k))^r(1−v/(4sqrt(k)))^r. The remaining smooth
factor tends to its endpoint value with error O((v+1)/sqrt(k)).
Integrating against e^(-v) gives the leading integral r! and
an O_r(k^(-1/2)) error. The uniform kernel error in (11) gives
the same relative precision; the part outside a fixed endpoint
interval is exponentially small by (12). This proves (22),
including the denominator r=0 estimate used in the quotient.

Taylor's formula and (22), for r=1,2, imply for fixed f in C²[0,1]



$$
\frac{\int_0^1 E_k(x)f(x)dx}{L_k}
=f(1)-\frac{f'(1)}{\sqrt k}
 +O\!\left(\|f\|_{C^2}k^{-1}\right).
\tag{23}
$$



There is no assumed first correction to (11) in this calculation.
For the eigenfunction, evaluating
T psi=[x(x−1)psi']'+(x²−x+1)psi=xi psi at x=1 gives the exact
endpoint identity psi_l'(1)=(xi_l−1)psi_l(1). Consequently



$$
\boxed{
\frac{g_\ell p_k^{(\ell\bmod2)}(\xi_\ell)}
 {\psi_\ell(1)L_k}
=1-\frac{\xi_\ell-1}{\sqrt k}+O_\ell(k^{-1}).}
\tag{24}
$$



Thus a fixed finite collection of actual low-node columns is
rank one to leading order after row normalization; its first
node-dependent separation is of relative order k^(-1/2).

For a precise minor statement choose two fixed distinct nodes
xi_a,xi_b, and let k_n/n tend to t>0 and j_n/n tend to u>0 with
t!=u. In the two-column matrix of actual normalized moments
M_(k,l)=<E_k,psi_l>/L_k, equation (24) gives



$$
\boxed{
\det\begin{pmatrix}M_{k_n,a}&M_{k_n,b}\\
                    M_{j_n,a}&M_{j_n,b}\end{pmatrix}
=\psi_a(1)\psi_b(1)(\xi_b-\xi_a)
 (k_n^{-1/2}-j_n^{-1/2})+O_{a,b,t,u}(n^{-1}).}
\tag{25}
$$



All factors in its n^(-1/2) leading coefficient are nonzero.
It follows that this particular fixed two-column minor is
nonzero for sufficiently large n, with its eventual sign
determined by the displayed coefficient. The statement permits
different node parities because M uses each node's matching branch.
For k_n−j_n bounded, the displayed main difference is smaller
than the proved error and (25) does not establish a sign or
lower bound. A growing number of nodes is also outside its scope.
