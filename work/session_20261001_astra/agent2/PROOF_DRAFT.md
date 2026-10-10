> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Growing exponential degree: exact reduction and a uniform determinant bound

Status: proved identities and absolute bounds, with unresolved endpoint and arithmetic gaps. Throughout n>=2 and b=floor(n/2). No fixed-b asymptotic is used.

## Sources and scope

Read: work/session_20260913/unequal_degree_hp_attempt.md; work/session_20260927/fixed_exponential_degree_error_theorem.md and fixed_exponential_degree_error_independent_review.md; E_PI_RESEARCH_REPORT_20260913.md. The antecedent was located in the bounded listing of session_20260913. No EQUIVALENT-named file appeared in that listing; none was assumed or read.

The inherited raw exclusion concerns its particular raw endpoint polynomials, not all independent triples with caps (n,b,n). The b=0 exclusion is also specific to that allocation. Consequently neither theorem excludes the present allocation. Conversely the fixed-b error theorem explicitly supplies no uniform growing-b conclusion. The degree-one rational companion error theorem does not transfer to a growing determinant.

## 1. Exact system, without a normality assumption

Use L(P)=integral_{-1}^1 P((1+iu)/2)du, monic p_k=i^k P_k(-i(2t-1))/binom(2k,k), and h_k=2(-1)^k/((2k+1)binom(2k,k)^2). Put

ell_j(t^k)=1/(n+k+1-j)!, 0<=j<=b,
K_n(t,s)=sum_{k=0}^n p_k(t)p_k(s)/h_k,
V(t)=K_n(t,1),
H(t)=sum_{k=0}^n L(p_k/(1-t))p_k(t)/h_k,
W(t)=1/(1-t)-H(t).

The factorial arguments are positive for every k>=0 because b<=n. The first n+1 moment equations reconstruct

C*(t)=-sum_{k=0}^n ell_B(p_k)p_k(t)/h_k,
ell_B=sum B_j ell_j.

There are exactly b-1 remaining moment tests ell_B(p_{n+l})=0, 1<=l<=b-1, and the endpoint row ell_B(V)+sum B_j=0. This follows from the nonzero displayed bilinear norms; positivity of the complex moment functional is neither assumed nor needed. Taylor reconstruction gives A uniquely. Thus the actual reduced matrix is M=[U;e+v], where U_lj=ell_j(p_{n+l}), e=(1,...,1), and v_j=ell_j(V).

The full evaluated remainder is ell_B(W). Indeed the exponential tail after degree n is sum_j B_j sum_{k>=0}1/(n+k+1-j)!, and the logarithmic tail is L(C*/(1-t))=-ell_B(H). Both series converge absolutely. This proves the identity for growing b as well as fixed b.

Choose B as the cofactor vector characterized by B dot x=det[M;x]. Write w_j=ell_j(W). Then

Y=B(1)=-D_V, D_V=det[U;e;v],
R(1)=D_W+T, D_W=det[U;e;w], T=det[U;v;w].

These identities hold even if the cofactor vector vanishes. To obtain a unique normalized approximant it suffices to prove D_V!=0: this also proves rank M=b. Rank M=b alone does not imply Y!=0. Nonzero value of the integer form requires the separate condition D_W+T!=0.

## 2. Exact growing-size contour formula

For 0<=j<=b, any P analytic on |t|<r0 with factorially summable Taylor coefficients, and any R>1/r0,

ell_j(P)=(1/(2 pi i)) integral_{|z|=R} e^z z^{j-n-2}P(1/z) dz.

Termwise integration proves this formula; on the contour the Taylor expansion is absolutely convergent. For the polynomials and W here, any R>1 works. Set D_j=ell_{j+1}-ell_j for 0<=j<=b-1. For 1<=d<=b and d functions P_i,

 det[D_j(P_i)]_{i=1..d,j=0..d-1}
 =1/(d!(2 pi i)^d) integral ... integral
 det[P_i(1/z_k)]_{i,k} Delta(z_1,...,z_d)
 product_{k=1}^d [e^{z_k}(z_k-1)z_k^{-n-2} dz_k].

Here Delta(z)=product_{k<l}(z_l-z_k). Expanding the two determinants and permuting integration variables proves the identity directly. All contour integrals are compact, so no limiting interchange is needed.

Subtracting original adjacent columns in D_V and D_W leaves a d=b determinant of D_j applied to p_{n+1},...,p_{n+b-1},V or W, up to the same expansion sign. Thus the formula applies to the actual endpoint determinants, not just to a model matrix.

For T use the same contour identity with ell_j instead of D_j, d=b+1 and functions p_{n+1},...,p_{n+b-1},V,W: simply omit every factor z_k-1. This retains the complete companion contribution.

## 3. Explicit uniform bound retaining determinant cancellation

The following lemma has no fixed-d constants. Let U0(t)=p_{n+1}(t), let rho=1/20, and suppose P_i=U0 G_i with G_i analytic on a neighborhood of |t|<=rho. Let M_i bound |G_i| there. Choose R>20, set

S=d(d-1)/2, a=2R/pi^2,
C_G=d^(d/2) (product M_i) rho^d/(rho-1/R)^(d+S),
J_d(R)=2^S a^(-S-d/2) pi^(d/2) Gamma(S+d/2)/((2pi)^d Gamma(d/2)),
E_n(R)=exp(R)(R+1)R^(-n-1)|U0(0)|(1+2/R)^(n+1).

Then, with the original functionals ell_0 through ell_b, for 1<=d<=b,

|det[D_j(P_i)]| <= C_G E_n(R)^d J_d(R)/d!.

For 1<=d<=b+1, the ordinary determinant det[ell_j(P_i)] with columns j=0,...,d-1 satisfies the same bound with E_n(R)/(R+1) in place of E_n(R).

Domain correction: the difference determinant needs ell_0 through ell_d, whereas the ordinary determinant needs ell_0 through ell_(d-1). Both intended applications, d=b for D_V and D_W after column differences and d=b+1 for T with ordinary functionals, therefore use no index beyond b. Every factorial argument is at least n+1-b>=1. All displayed bounds remain unchanged. See GROWING_DOMAIN_CORRECTION.md for the correction record.

Proof. The roots of U0 are (1+iu_k)/2 with real |u_k|<1, so their reciprocal moduli are at most 2. Hence |U0(1/z)|<=|U0(0)|(1+2/R)^(n+1). Divided-difference column elimination gives

det[G_i(t_k)]=Delta(t) det[G_i[t_1,...,t_{j+1}]]_{i,j}.

The Cauchy integral formula bounds the entry in column j by M_i rho/(rho-1/R)^(j+1). Hadamard's inequality, after extracting the row and column bounds, gives |det G|<=C_G |Delta(t)|. The formula extends to coincident nodes by continuity.

Write z_k=R exp(i theta_k), -pi<=theta_k<=pi. The product |Delta(z)Delta(1/z)| equals product_{k<l}|exp(i theta_l)-exp(i theta_k)|^2. It is at most product_{k<l}(theta_l-theta_k)^2, which is at most (2 sum theta_k^2)^S. Moreover cos theta<=1-2theta^2/pi^2 on this interval. In the contour formula, extract E_n(R)^d and integrate the remaining Gaussian majorant over all R^d. Polar coordinates give

(2pi)^(-d) integral_{R^d} exp(-a||theta||^2)(2||theta||^2)^S dtheta = J_d(R).

This proves the bound with every dimension-dependent factor displayed. The ell_j version follows by omitting z-1. QED.

All required M_i exist explicitly. On |t|<=rho, the recurrence ratios p_{k+1}/p_k have real part <=-(1/2-rho), by induction in p_{k+1}/p_k=t-1/2+beta_k/(p_k/p_{k-1}). Consequently |U0(t)|>=(9/20)^(n+1). For a polynomial P=sum c_k t^k one may take M(P)=(20/9)^(n+1)sum |c_k|rho^k. For W one may take M(W)=(20/9)^(n+1)[1/(1-rho)+sum |[t^k]H|rho^k]. These are coarse but fully explicit growing-n bounds, not unspecified constants. H is the finite projection defined above; its coefficients are well-defined real numbers. No rationality claim is made for H.

The high-row bounds can be sharpened without limits: for k>=1, |p_{k+1}/p_k|<=11/20+(1/12)/(9/20)=397/540<3/4 on this disk. Thus for P_i=p_{n+l}, G_i=p_{n+l}/p_{n+1}, one may take M_i=(3/4)^(l-1).

Taking, for example, R=n+21 makes the bound an explicit inequality solely in n and the finite projection data. Its Gaussian factor contains R^(-S), in addition to R^(-d/2). The cancellation order S=b(b-1)/2 is quadratic in n: S=n^2/8+O(n). The remaining Gamma, C_G and dimension factors must be retained; they cannot be hidden in a constant independent of b.

There is also an exact formal explanation of S: expand each G_i(t)=sum_r g_ir t^r and use determinant multilinearity. Repeated monomial shifts give equal rows and vanish. Every surviving tuple of distinct nonnegative shifts has sum at least S. This is an algebraic cancellation statement, not proof that the normalized determinant has a nonzero leading term at growing b. The uniform contour bound and the formal cancellation are consistent, but neither is a determinant lower bound.

## 4. Primitive normalization and a quantitative conditional route

Let X=A(1), Y=B(1)!=0. Clear all polynomial denominators, divide the full coefficient content, and write the resulting integer endpoint pair as (X_int,Y_int). Set g=gcd(|X_int|,|Y_int|), q=|Y_int|/g and p=sign(Y_int)X_int/g. Then exactly

L=p+q(e+pi)=q R(1)/Y,
|L|=q |D_W+T|/|D_V|.

Thus the final endpoint gcd is indispensable. A full-coefficient clearer, cofactor height, or real coefficient amplification does not substitute for q.

The contour lemma supplies explicit upper bounds B_W and B_T for |D_W| and |T|, with d=b and b+1 respectively. A precise sufficient route on an unbounded index set is:

D_V!=0, D_W+T!=0, and q(B_W+B_T)/|D_V| ->0.

For an exponential target it suffices that q(B_W+B_T)<=exp(-eta n)|D_V| for some eta>0. This is a testable sufficient inequality, not a proved rate. It requires an actual denominator estimate and a lower bound on D_V; nonvanishing of D_W+T is an additional gate. No estimate proved here establishes those gates, and the coarse upper bounds may be far from sharp.

In particular, the fixed-b constant (sqrt(2)-1)^b cannot be inserted into the fixed-b limit to predict an established growing-b rate. No saddle equation or asymptotic error theorem is asserted here. The additional factorial row in T is controlled absolutely by the lemma, but its ratio to D_V is not controlled until a denominator-determinant lower bound is proved.

## 5. Finite certificates and stopping boundary

The only newly computed indices are n=4,6,8,10, b=2,3,4,5. check_growing_regime.py verifies all original high Taylor rows, the exact projection, endpoint matching, cofactor endpoint identity, and rational decomposition of both complete tails. It clears the full triple, removes its content, and separately removes the endpoint gcd. Exact Taylor/Machin intervals certify the nonzero evaluated forms. The certificate contains full reduced endpoints and primitive triples.

The respective reduced q digit counts are 10,23,43,68, and endpoint gcds after primitive polynomial normalization are 3,20,140,28224. The integer-form magnitudes are approximately 7.6361e5, 2.8318e17, 2.0202e35, 8.8562e58. These are finite evidence only and prove no obstruction for the growing regime.

There is no decisive all-index obstruction here, so no replacement construction is proposed under a false claim of exclusion. The exact system, complete-tail contour representation, and explicit uniform absolute determinant bound are the proved deliverables. Growing-degree endpoint lower bounds, signed whole-error estimates, and actual primitive arithmetic remain open. This branch stops before substituting fixed-size constants, first omitted Taylor terms, or unreduced coefficient heights for those missing estimates.
