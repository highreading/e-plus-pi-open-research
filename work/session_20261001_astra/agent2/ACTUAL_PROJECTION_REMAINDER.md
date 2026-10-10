> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual projection remainder: uniform scalar-preserving bounds

Status: paper proofs of reference-function identities, uniform disk estimates, and complete determinant upper bounds. No growing-degree endpoint or evaluated-remainder nonvanishing theorem is asserted. No numerical computation or scan is used.

The completed domain correction and content-obstruction review remain valid in their stated scopes. The obstruction B_W>4B_V concerned particular coefficient majorants. Here those majorants are replaced by bounds derived from the actual projection remainder.

## 1. Objects and exact dependencies

Let

L(P)=integral_{-1}^1 P((1+iu)/2) du,
p_k(t)=i^k P_k(-i(2t-1))/binom(2k,k),
h_k=L(p_k^2)=2(-1)^k/((2k+1)binom(2k,k)^2),
K_n(t,s)=sum_{k=0}^n p_k(t)p_k(s)/h_k.

Here P_k is the ordinary Legendre polynomial. Write

U(t)=p_(n+1)(t), A_n=p_n(1)>0,
v_n=L(p_n(t)/(1-t)),
V(t)=K_n(t,1),
H_n(t)=L_s(K_n(t,s)/(1-s)),
W(t)=1/(1-t)-H_n(t).

H_n here is a projection polynomial, not the integer auxiliary polynomial in the arithmetic notes. The scalar v_n is distinct from the functional row later denoted v.

Sources read for this continuation:

- work/session_20260913/unequal_degree_hp_attempt.md, Sections 3 and 4.1: monic polynomials, norms, recurrence, and the Legendre-square second-kind identity.
- work/session_20260913/hp_b1_endpoint_attempt.md, Sections 1 and 4: Christoffel–Darboux and the exact projection remainder.
- work/session_20260913/hp_b2_endpoint_attempt.md, Sections 2 and 4: reference quotients and second-kind ratio bounds.
- work/session_20260927/fixed_exponential_degree_error_theorem.md, Sections 1 and 3: complete determinant identities and reference normalization. Its fixed-size determinant limit is not used.
- work/session_20261001_astra/agent3/GAUSSIAN_VANDERMONDE_BOUND.md, Sections 2–4: Gaussian integral and absolute contour estimates, previously checked in GROWING_CONTENT_CRITERION_REVIEW.md.

The reference identities and bounds needed below are proved explicitly, so their dependence is separate from any fixed-b error theorem.

## 2. Christoffel–Darboux retains the cancelling scalar

The exact kernel formula is

K_n(t,s)=[U(t)p_n(s)-p_n(t)U(s)]/[h_n(t-s)].

Because L_s K_n(t,s)=1, subtract the two rational functions inside the projection:

W(t)=L_s(K_n(t,s)[1/(1-t)-1/(1-s)]).

Their difference is (t-s)/((1-t)(1-s)). The factor t-s cancels before integration, giving

W(t)=[v_n U(t)-v_(n+1)p_n(t)]/[h_n(1-t)].                 (1)

This is the actual projection remainder, with all terms retained. It avoids estimating 1/(1-t) and H_n separately.

Define

r_n(t)=p_n(t)/U(t),
beta_k=k^2/[4(4k^2-1)],
b_n=A_(n+1)/A_n,
alpha_n=v_(n+1)/v_n.

Once v_n is shown nonzero below, (1) and the kernel formula at s=1 become

W(t)/U(t)=(v_n/h_n)[1-alpha_n r_n(t)]/(1-t),             (2)
V(t)/U(t)=-(A_n/h_n)[1-b_n r_n(t)]/(1-t).               (3)

Both signs agree with the reference identities. The scalar v_n/h_n must remain attached to the complete W expression.

To identify its magnitude, orthogonality gives

A_n v_n=L(p_n(t)^2/(1-t))
 =2(-1)^n/binom(2n,n)^2 * integral_{-1}^1 P_n(u)^2/(1+u^2) du.

Indeed the difference of the two integrands before the last equality is p_n times a polynomial of degree at most n-1. Define

theta_n=(2n+1) integral_{-1}^1 P_n(u)^2/(1+u^2) du.

The Legendre norm and 1/2<=1/(1+u^2)<=1 prove

1<=theta_n<=2,
v_n A_n/h_n=theta_n.                                   (4)

In particular v_n has strict sign (-1)^n and is nonzero. Introduce the positive scalars

mu_n=v_n/h_n=theta_n/A_n,
nu_n=A_n/|h_n|,
epsilon_n=|v_n|/A_n=theta_n |h_n|/A_n^2.

Then exactly

mu_n/nu_n=epsilon_n.                                    (5)

The small scalar is relative: mu_n itself need not decay. In fact it grows exponentially, whereas nu_n grows much faster. Equivalently W(0) stays bounded while V(0) grows exponentially. Treating W/U as absolutely exponentially decaying would be a normalization error.

## 3. Quantitative uniform disk bounds

Use the fixed disk |t|<=rho=1/20, and set m=1/2-rho=9/20.

The recurrence

p_(k+1)=(t-1/2)p_k+beta_k p_(k-1)

implies that every ratio p_(k+1)/p_k is analytic on the disk and has real part at most -m. This starts with p_1/p_0=t-1/2; the reciprocal of a number with negative real part has negative real part, so induction applies. In particular

Re r_n(t)<0, |r_n(t)|<=20/9.                             (6)

The endpoint recurrence gives

1/2<=b_n<=2/3.

For k>=1, orthogonality also gives v_(k+1)=v_k/2+beta_k v_(k-1). Since the signs alternate, application at k=n+1 gives

|alpha_n|=beta_(n+1)/(1/2+|alpha_(n+1)|)<1/6,
alpha_n<0.                                               (7)

This proof is valid for n>=0 and does not use a limiting second-kind formula.

Put

F_W,n(t)=[1-alpha_n r_n(t)]/(1-t),
F_V,n(t)=[1-b_n r_n(t)]/(1-t).

Equations (6)–(7) imply the explicit bounds

340/567 <= |F_W,n(t)| <= c_W:=740/513,
20/21 <= |F_V,n(t)| <= c_V:=1340/513.                    (8)

For W, use 1-|alpha_n r_n|>=1-10/27=17/27. For V, Re(1-b_n r_n)>=1 supplies the lower bound; its numerator is at most 1+40/27=67/27. The bounds for |1-t| are 19/20 and 21/20.

Therefore valid uniform analytic row bounds are

M_W^sharp=c_W mu_n=c_W theta_n/A_n,
M_V^sharp=c_V nu_n=c_V A_n/|h_n|.                        (9)

Their ratio is exactly

M_W^sharp/M_V^sharp=(37/67)epsilon_n.                   (10)

These are bounds on the actual functions W/U and V/U, with their scalar normalization preserved. They replace the earlier bounds obtained by estimating projection coefficients separately.

There is also a direct comparison of the actual reference functions, stronger than a comparison of majorants. Let c=-alpha_n, so 0<c<b_n. For Re r<=0,

|1+c r|^2-|1-b_n r|^2
 =2(c+b_n)Re r+(c^2-b_n^2)|r|^2<=0.

Since the denominator has positive real part, equations (2)–(3) give

(17/67)epsilon_n <= |W(t)/V(t)| <= epsilon_n             (11)

throughout the disk. The lower bound uses |1+c r|>=17/27 and |1-b_n r|<=67/27. This division is justified by a proved lower bound for the actual denominator function, not by dividing upper bounds.

The same formulas prove U,V,W are nonzero on this disk. They do not prove nonvanishing of any factorial determinant.

At t=0, r_n(0)=-1/b_n. Thus the normalized shapes in the fixed-degree source are recovered exactly:

[V(t)/V(0)]/[U(t)/U(0)]=F_V,n(t)/2,
[W(t)/W(0)]/[U(t)/U(0)]=F_W,n(t)/(1+alpha_n/b_n).

Their uniform upper bounds are c_V/2 and 3c_W/2, respectively. Moreover

W(0)/V(0)=(-1)^(n+1)epsilon_n(1+alpha_n/b_n)/2,
epsilon_n/3 <= |W(0)|/V(0) <= epsilon_n/2.              (12)

Using (4), one can check the absolute normalization directly:

W(0)=(-1)^(n+1)theta_n(b_n+alpha_n),
1/3<=|W(0)|<=4/3.                                      (13)

Thus retaining W's cancellation does not amount to claiming that W(0) tends to zero.

## 4. Explicit exponential bounds for the scalar ratio

Set

a=(1+sqrt(2))/4,
s=(sqrt(2)-1)^2,
tau=-log s=2log(1+sqrt(2)).

Then 16a^2=1/s and 1/(2a)+s=1. We prove bounds uniform in n rather than invoking a fixed-b asymptotic.

Since beta_k>=1/16, comparison with the positive constant-coefficient recurrence with initial values 1,1/2 yields

A_n >= a^n[1-(-s)^(n+1)]/(1+s) >= (1-s)a^n.

For an upper bound put x_n=A_n/a^n. The recurrence becomes

x_(k+1)=(1/(2a))x_k+s[1+1/(4k^2-1)]x_(k-1).

The two constant coefficients sum to one. Since x_0=1 and x_1=1-s<1, induction on the running maximum gives

x_n<=product_{k=1}^{n-1}[1+s/(4k^2-1)]<=exp(s/2),

where sum_{k>=1}1/(4k^2-1)=1/2 telescopes. Consequently

(1-s)a^n <= A_n <= exp(s/2)a^n.                         (14)

For n>=1, the elementary central-binomial bounds

4^n/(2sqrt(n)) <= binom(2n,n) <= 4^n/sqrt(3n+1)

follow by induction from the ratio 4(2n+1)/(2n+2). The lower inequality starts at n=1. For the upper inequality, the required squared comparison is

(2n+1)^2(3n+4)<=4(n+1)^2(3n+1),

whose right side minus left side is n. These bounds imply

2*16^(-n) <= |h_n| <= 4*16^(-n).

Combining this with (4) and (14) proves the explicit scalar estimates

2 exp(-s) s^n <= epsilon_n <= [8/(1-s)^2]s^n, n>=1.     (15)

In particular log epsilon_n=-tau n+O(1), with absolute, dimension-independent constants. This is a statement about the ordinary scalar reference error, not about a growing determinant quotient.

For clarity, the separate row amplitudes satisfy

exp(-s/2)a^(-n) <= mu_n <= [2/(1-s)]a^(-n),
[(1-s)/4](16a)^n <= nu_n <= [exp(s/2)/2](16a)^n.         (16)

The latter inequalities follow directly from the central-binomial bounds. All row factors remain exp(O(n)), but their ratio now carries the genuine saving s^n.

## 5. Applying the bound to both complete remainder determinants

For 1<=b<=n retain the exact monic cofactor system

ell_j(t^k)=1/(n+k+1-j)!, 0<=j<=b,
U_lj=ell_j(p_(n+l)), 1<=l<=b-1,
e=(1,...,1), v=(ell_j(V)), w=(ell_j(W)).

The complete endpoint identities are

Y=-D_V, D_V=det[U_lj;e;v],
R(1)=D_W+T,
D_W=det[U_lj;e;w], T=det[U_lj;v;w].                   (17)

They use both full tails, not a first omitted Taylor coefficient. Adjacent column differences reduce D_V,D_W to b-column difference determinants, with the same sign (-1)^(b+1). The companion T is an ordinary (b+1)-column determinant. Both use largest functional index b, preserving the completed domain correction.

For any R>20 set

S_d=d(d-1)/2,
C_d(R)=d^(d/2)rho^(-S_d)(1-1/(rho R))^(-(d+S_d)),
J_d(R)=(2pi)^(-d/2)(4R/pi^2)^(-d^2/2) product_{j=1}^d j!,
E_n(R)=exp(R)(R+1)R^(-n-1)|U(0)|(1+2/R)^(n+1),
H_b=(3/4)^((b-1)(b-2)/2),
K_b(R)=C_b(R)H_b E_n(R)^b J_b(R)/b!.

The high-row bounds entering H_b follow from

|p_(k+1)/p_k|<=11/20+(1/12)/(9/20)=397/540<3/4.

The Gaussian Vandermonde bound now gives the explicit positive expressions

B_V^sharp=K_b(R) M_V^sharp,
B_W^sharp=K_b(R) M_W^sharp,
B_T^sharp=C_(b+1)(R)H_b M_V^sharp M_W^sharp
          [E_n(R)/(R+1)]^(b+1)J_(b+1)(R)/(b+1)!,       (18)

satisfying |D_V|<=B_V^sharp, |D_W|<=B_W^sharp, |T|<=B_T^sharp. In particular

B_W^sharp/B_V^sharp=(37/67)epsilon_n.                  (19)

Equation (19) compares explicitly defined bounding expressions. It is not a bound for D_W/D_V. The direct reference-function comparison (11) likewise cannot be passed through signed factorial functionals or determinant contractions without a new argument.

The complete companion bound admits a useful exact comparison. Put

Xi_(n,b)(R)=B_T^sharp/B_W^sharp.

Using J_(b+1)/J_b and C_(b+1)/C_b explicitly gives

Xi_(n,b)(R)
 =[(b+1)^((b+1)/2)/b^(b/2)]
  rho^(-b)(1-1/(rho R))^(-(b+1))
  * M_V^sharp E_n(R)/(R+1)^(b+1)
  * b!/[sqrt(2pi)(4R/pi^2)^(b+1/2)].                   (20)

No outside integration factorial is omitted. Therefore the rigorous full-remainder bound is

|D_W+T| <= B_V^sharp (37/67)epsilon_n[1+Xi_(n,b)(R)].   (21)

The companion has been retained explicitly.

## 6. Quantitative companion estimate when b=floor(n/2)

Fix lambda>0 and R=lambda n, eventually R>20. In (20), the ratio of divided-difference factors has logarithm O_lambda(n), while M_V^sharp and |U(0)| have logarithms O(n). Also

log(b!)-(b+1/2)log R=O_lambda(n)

for b=floor(n/2). It follows from the exact positive expression that

log Xi_(n,b)(lambda n)=-(n+b)log n+O_lambda(n)
 =-(3/2)n log n+O_lambda(n).                           (22)

This statement concerns the bound ratio, not T/D_W or T/D_V.

An entirely explicit upper inequality is available with R=n. For n>=40 and b=floor(n/2),

Xi_(n,b)(n)
 <= [exp(26)/n] [e/(s n)]^n [5pi^2/(2n)]^b.            (23)

To verify it, use the following inequalities in (20):

- (b+1)^((b+1)/2)/b^(b/2)<=exp(1/2)sqrt(b+1).
- (1-20/n)^(-(b+1))<=exp(21), using -log(1-x)<=2x for x<=1/2.
- b!<=b^b and b/n<=1/2, so the last factor in (20) is at most sqrt(pi/(8n))(pi^2/8)^b.
- M_V^sharp |U(0)|<=c_V exp(s)a s^(-n)/2, from (14) and (16).
- (1+2/n)^(n+1)<=exp(41/20) and (n+1)^(-b)<=n^(-b).

After multiplication, the constant is below exp(26), and rho^(-b)(pi^2/8)^b=(5pi^2/2)^b. This proves (23) without degree samples.

Thus Xi tends to zero rapidly, and the full ratio of bounding expressions in (21) satisfies

log[(B_W^sharp+B_T^sharp)/B_V^sharp]=-tau n+O(1).        (24)

Unlike the old ratio exceeding 4, this ratio tends to zero. This removes that particular pointwise obstruction to the certification method. It does not establish that the endpoint-normalized upper bound tends to zero.

The leading cofactor-scale bounds remain

log B_V^sharp=-n^2 log n/2+O_lambda(n^2),
log B_W^sharp=-n^2 log n/2+O_lambda(n^2),
log B_T^sharp=-n^2 log n/2+O_lambda(n^2).

Their ratios retain the finer information in (22)–(24), which the O(n^2) notation hides. There is only one W row in each remainder determinant, so the demonstrated relative saving is s^n once, not s^(nb). No additional factor (sqrt(2)-1)^b is inferred from the fixed-b determinant theorem.

Even though B_T^sharp/B_W^sharp tends to zero, D_W might itself be much smaller than its bound or zero. Consequently this does not prove that the actual companion is negligible relative to D_W, nor that D_W+T is nonzero.

## 7. Actual primitive normalization and the remaining quantitative gap

On D_V!=0, let q be the positive denominator of X/Y=A(1)/Y in lowest terms. It includes full polynomial content cancellation and the final endpoint gcd. Then

|L|=|qR(1)/Y|=q|D_W+T|/|D_V|.

Define the loss relative to the improved endpoint bound by

delta_n^sharp=log(q B_V^sharp/|D_V|)
 =log q+log(B_V^sharp/|D_V|)>=log q>=0.                 (25)

Use (21) to obtain the valid inequality

|L|<=exp(delta_n^sharp)(37/67)epsilon_n[1+Xi_(n,b)(R)].  (26)

This does not divide two upper bounds to estimate an actual quotient: the actual endpoint remains explicitly in delta_n^sharp.

For fixed lambda and b=floor(n/2), the logarithm of the positive expression on the right of (26) is

delta_n^sharp-tau n+O(1).                              (27)

Thus this particular upper-bound method certifies shrinking precisely when its bounding expression tends to zero, equivalently

delta_n^sharp-tau n -> -infinity.                      (28)

A convenient sufficient quantitative hypothesis is delta_n^sharp<=(tau-eta)n on an unbounded set, for a fixed eta>0. To obtain nonzero shrinking forms, that same set must also satisfy D_V!=0 and D_W+T!=0.

No estimate delta_n^sharp=O(n), much less one below tau n, is proved here. It contains both the actual reduced denominator and potentially large cancellation loss in the growing endpoint determinant. A bound on q alone would not control the second term in (25). This is the remaining quantitative gap.

For comparison with the corrected arithmetic review, retain its monic endpoint clearer

M=2^(2n+3)((2n+1)!)^2 product_{l=1}^{b-1}(2n+2l)!,
g=gcd(|MX|,|MY|).

The previously verified exact identity q/|D_V|=M/g gives

delta_n^sharp=log(M B_V^sharp/g).

Criterion (28) therefore asks for

log(M B_V^sharp)-log g <= tau n-omega(1),               (29)

with the same nonvanishing qualifications. It concerns an additive scale of order n, not a strict improvement of the leading n^2 log n coefficient. Since g<=M|D_V|<=M B_V^sharp, the earlier ceiling remains

limsup log g/(n^2 log n)<=3/4

on every unbounded nonzero-endpoint set. The strict content-rate target above 3/4 is still impossible and is not revived by the new row estimate.

The arithmetic identity is used here with the exact cofactor scale audited in GROWING_CONTENT_CRITERION_REVIEW.md. Removed row, minor, and contraction contents are already included in g through that review's scalar ledger. They must not be added again as independent gains.

## 8. Proven outcome and limitations

The new result is a scalar-preserving uniform bound for the actual W/U, including explicit constants, a direct reference-function comparison, and a quantitative scalar rate epsilon_n comparable to exp(-tau n). Both complete remainder determinants have been bounded, with an explicit companion ratio.

The old B_W>4B_V obstruction does not apply to these newly defined bounds. Their relative numerator bound is exponentially small. The remaining obstacle is now explicitly delta_n^sharp versus tau n, together with growing-degree endpoint and full-remainder nonvanishing at the same indices.

Reference-function nonvanishing on a fixed disk is proved; determinant and evaluated-remainder nonvanishing are not. No positivity of the original complex determinant integrand is assumed. No fixed-b determinant limit, finite-degree extrapolation, numerical evidence, or first-tail approximation enters these proofs. Neither shrinking nor divergence of the actual primitive forms is established.

All files written for this continuation stay in work/session_20261001_astra/agent2/. The completed domain correction, combined correction review, and finite certificates are preserved. This note and its report require read-back verification after saving.
