> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact projection, complete remainder, and error transfer for each fixed exponential degree

Status: UNVERIFIED CANDIDATE
Author: worker_2
Content SHA256: b8c2e619d3f2287876530b229be959d872aadf8b04c5df3b3cef4ee8ec7c8245

Status: unverified candidate submitted by worker_2 for independent review. This is a theorem about the matched approximation family, not a proof concerning the rationality of e+pi.

Fix an integer b≥1. Put F(z)=4 arctan(z/(2−z)), using its analytic branch at zero. For n≥b, seek polynomials A,B,C with degree bounds n,b,n, respectively, such that

R(z)=B(z)e^z+C(z)F(z)−A(z)=O(z^(2n+b+1)),
B(1)=C(1)=Y.

This explicitly fixes the sign convention for A. For all sufficiently large n, the solution space is one-dimensional, has a rational representative, and its nonzero representatives have Y≠0. With rho=1+sqrt(2), kappa=1/rho, and epsilon_n the ordinary logarithmic Padé error normalized below, the conclusion is

(-1)^n R(1)/(Y epsilon_n) → kappa^b.

In particular, R(1)/Y is eventually nonzero and has sign (-1)^n. Using the published ordinary asymptotic gives

R(1)/Y = (-1)^n [4pi/rho^(b+1)] rho^(−2n)(1+o(1)).

All limits here keep b fixed.

The only asymptotic source input is the unconditional ordinary Padé assertion in work/astra_review_registry/verified/worker3-ordinary-pade-prefactor-v1.md, payload SHA-256 e2b926b3f2d184f5cd501ef88d3031968ab3a8fb0bbce0fd456292ef52991aa3: in the normalization specified below, epsilon_n~(4pi/rho)rho^(−2n). In particular, epsilon_(n+1)/epsilon_n→kappa². The conditional matched-family assertion in that publication is not used. The proof below supplies that transfer separately.

Define the bilinear moment functional

L(g)=integral from −1 to 1 of g((1+ix)/2) dx.

There is no complex conjugation in this functional. Near z=0,

F(z)=z L(1/(1−zt)).

Let P_k be the usual Legendre polynomial with P_k(1)=1, put c_k=binomial(2k,k), and define

p_k(t)=i^k P_k((2t−1)/i)/c_k.

These polynomials are monic. Legendre orthogonality gives

L(p_k p_l)=0 for k≠l,
h_k:=L(p_k²)=2(-1)^k/((2k+1)c_k²)≠0.

The recurrence is

p_0=1, p_1=t−1/2,
p_(k+1)=(t−1/2)p_k+beta_k p_(k−1),
beta_k=k²/(4(4k²−1)),  k≥1.

Thus beta_k≤1/12 and beta_k→1/16. These formulas follow directly from the Legendre Rodrigues formula and its three-term recurrence. They also show that the p_k have rational coefficients and p_k(0)=(-1)^k p_k(1). At t=1 the recurrence has positive coefficients, so p_k(1)>0 and both endpoints are nonzero.

Define

K_n(t,s)=sum_(k=0)^n p_k(t)p_k(s)/h_k,
H_n(t)=L_s(K_n(t,s)/(1−s)),
V(t)=K_n(t,1),
W(t)=1/(1−t)−H_n(t).

Here H_n denotes the projection polynomial, not the unrelated integer auxiliary sequence with the same historical name. For a germ g(t)=sum_(m≥0)g_m t^m analytic on some disk of positive radius, define

ell_j(g)=sum_(m≥0) g_m/(n+m+1−j)!,  0≤j≤b.

These sums converge absolutely. If B(z)=sum_(j=0)^b B_j z^j, write ell_B=sum_j B_j ell_j and C*(t)=t^n C(1/t).

For k=n+m+1, the coefficient of z^k in B e^z+C F is exactly

ell_B(t^m)+L(C*(t)t^m).

Consequently, the required high Taylor equations are

L(C* q)=−ell_B(q),  q in the polynomial space of degree at most n+b−1.

Since every h_k is nonzero, their restriction to degree at most n reconstructs C* uniquely:

C*(t)=−ell_B^s K_n(t,s).                                           (1)

The remaining equations, expressed in the orthogonal basis, are precisely

ell_B(p_(n+l))=0,  1≤l≤b−1.                                      (2)

Evaluation of (1) at t=1 shows that matching B(1)=C(1) is precisely

sum_(j=0)^b B_j(1+ell_j(V))=0.                                  (3).

A is then uniquely the Taylor polynomial of B e^z+C F through degree n. Thus (1)–(3) are equivalent to the original approximation and matching conditions; there are no omitted moment equations.

The complete evaluated remainder is

R(1)=ell_B(W).                                                    (4)

Indeed, after subtracting A, the entire exponential tail is ell_B(1/(1−t)). The entire logarithmic tail is L(C*/(1−t))=−ell_B(H_n), by (1). Their difference gives (4). These interchanges are legitimate: on the integration segment |t|≤1/sqrt(2), the geometric series converges absolutely, while the exponential tail and every factorial functional above converge absolutely. Equation (4) uses both complete tails, not only the first nonzero Taylor coefficient.

To identify all reference normalizations, put

v_k=L(p_k/(1−t)),
U=p_(n+1),
b_n=p_(n+1)(1)/p_n(1)=−U(0)/p_n(0)>0,
alpha_n=v_(n+1)/v_n.

Orthogonality gives v_k p_k(1)=L(p_k²/(1−t)). After parameterizing the integration segment, its real integral shows

epsilon_k:=(-1)^k v_k/p_k(1)
=2 integral_(−1)^1 P_k(x)²/(1+x²) dx /(c_k² p_k(1)²)>0.           (5)

This is the ordinary Padé normalization to which the published input applies. In particular, every v_k is nonzero. The exact relation

alpha_n/b_n=−epsilon_(n+1)/epsilon_n                              (6)

follows from (5).

The Christoffel–Darboux identity and the recurrence give

V(t)=p_n(1)[U(t)−b_n p_n(t)]/[h_n(t−1)],
V(0)=−2U(0)p_n(1)/h_n≠0.                                       (7)

Also,

W(t)=[v_n U(t)−v_(n+1)p_n(t)]/[h_n(1−t)].                       (8)

For completeness, (1−t)W is a polynomial of degree at most n+1 orthogonal to all polynomials of degree at most n−1. Its coefficient of U is v_n/h_n, from the leading term of H_n. Its coefficient of p_n is −v_(n+1)/h_n, obtained by pairing with p_n and using L(Wq)=0 for degree(q)≤n. This proves (8), including its sign.

Equations (7)–(8) imply

W(0)/V(0)=(-1)^(n+1)epsilon_n(1+alpha_n/b_n)/2
          =(-1)^(n+1)(epsilon_n−epsilon_(n+1))/2.                 (9)

Write s=kappa². The ordinary input and (6) give alpha_n/b_n→−s, so 1+alpha_n/b_n→1−s>0. Hence W(0)≠0 for all sufficiently large n. This is sufficient for every normalization below; no claim of nonvanishing of the matched Y has yet been used.

We next prove the local polynomial limits needed for the determinant argument. On |t|≤1/20, set r_k(t)=p_(k+1)(t)/p_k(t). Starting with r_0=t−1/2, induction in the recurrence gives

Re r_k(t)≤−9/20,
|r_k(t)|≤11/20+(1/12)/(9/20).

The induction simultaneously proves that these ratios are analytic and nonzero there. The maps z↦t−1/2+beta_k/z contract on the half-plane Re z≤−9/20 with Lipschitz constant at most 100/243<1. Since beta_k→1/16, comparison with the fixed-point map proves uniform convergence, on this disk or any smaller fixed disk, to

lambda(t)=(t−1/2−sqrt((t−1/2)²+1/4))/2,
lambda(0)=−a,  a=(1+sqrt(2))/4.

The square-root branch is the one positive at t=0. It is also obtained by the same contracting iteration with beta_k replaced by 1/16. Cauchy's formula gives convergence of each fixed derivative.

Let f(t)=lambda(t)/lambda(0). Then f(0)=1 and f'(0)=−sqrt(2). For each fixed l≥1,

[p_(n+l)(t)/p_(n+l)(0)]/[U(t)/U(0)] → f(t)^(l−1)               (10)

locally uniformly, by multiplying the finitely many consecutive ratios.

The ratios also prove the scaled limit

U(z/n)/U(0)→exp(−sqrt(2)z)                                     (11)

locally uniformly in z. Indeed, uniformly for bounded z,

log(U(z/n)/U(0))
=(z/n) sum_(k=0)^n r_k'(0)/r_k(0)+O(1/n).

The summands converge to lambda'(0)/lambda(0)=−sqrt(2), so the assertion follows by averaging. The logarithmic expansion is uniform because the ratios and their reciprocals and fixed derivatives are uniformly bounded on a smaller disk. Moreover, the zero-free disk gives a uniform bound 20 for the reciprocal roots of U; this suffices for the coefficient bounds used below.

For any reference function P with P(0)≠0, define G_P,n=(P/P(0))/(U/U(0)). Equations (7)–(8) give the exact identities

G_V,n=[1−b_n p_n/U]/[2(1−t)],
G_W,n=[1−alpha_n p_n/U]/[(1+alpha_n/b_n)(1−t)].                 (12)

Here b_n=−r_n(0)→a and alpha_n→−a s. All denominators in (12) are uniformly nonzero on a sufficiently small fixed disk for sufficiently large n. Thus these functions are uniformly analytic and bounded there, and their limits are

G_V=(1−s)/(f−s),
G_W=2/(f+1).                                                   (13)

To check the simplification, the equation for lambda gives

1−t=a(f+1)(f−s)/f,
a(1−s)=1/2.

Finally, |V(0)|=exp(O(n)). An explicit sufficient bound follows from 1/2≤b_k≤2/3 and (7):

|V(0)|≤(2n+1)(2/3)(64/9)^n.                                   (14)

No asymptotic estimate for W(0) is needed to control the additional determinant after normalization by W(0)/V(0).

Here is the factorial determinant lemma, with its cancellation scale justified. Fix d≥1 and put S=d(d−1)/2. Suppose U_n has degree n+1, U_n(0)≠0, uniformly bounded reciprocal roots, and U_n(z/n)/U_n(0)→exp(−c z) locally uniformly. Suppose

P_i,n=a_i,n [U_n/U_n(0)]G_i,n,  1≤i≤d,

where a_i,n≠0 and the G_i,n are uniformly analytic and bounded on a fixed disk and converge locally uniformly to G_i. Define D_j=ell_(j+1)−ell_j for 0≤j≤d−1. Then

(n!)^d n^S det[D_j(P_i,n)]/(product_i a_i,n)
→exp(−dc)(product_(j=0)^(d−1) j!) det[[t^j]G_i]_(i,j).          (15)

To prove it, write U_n/U_n(0)=sum_k u_k,n t^k. If L bounds the reciprocal roots, then

|u_k,n|≤binomial(n+1,k)L^k,
u_k,n/n^k→(−c)^k/k!.

For a monomial shift t^r U_n/U_n(0), the functional D_j is the sum of

u_k,n T_j(n+k+r+1)/(n+k+r+1)!,
T_j(X)=(X)_(j+1)−(X)_j,

where falling factorials are used. Each T_j is monic of degree j+1. Consequently,

det[T_j(X_i)]=Vandermonde(X_i)(product_i X_i+Q(X)),

where Q has total degree at most d−1 and Vandermonde(X)=product_(i<l)(X_l−X_i). For fixed nonnegative r_i, expansion in the k_i therefore gives

(n!)^d n^(sum_i r_i) det[D_j(t^r_i U_n/U_n(0))]
→sum_(k_i≥0) product_i[(−c)^k_i/k_i!] Vandermonde(k_i+r_i)
=exp(−dc) Vandermonde(r_i).                                    (16)

The final sum is an alternating polynomial in the r_i of total degree at most S. Its top-degree coefficient is exp(−dc), proving the equality.

For domination, use n!/(n+k+r+1)!≤n^(−k−r−1) and |u_k,n|/n^k≤(2L)^k/k!. After division by n^d the polynomial determinant is bounded by a fixed polynomial in the k_i+r_i+1. Summing the factorial weights yields, uniformly in n and nonnegative r_i,

|(n!)^d n^(sum_i r_i) det[D_j(t^r_i U_n/U_n(0))]|
≤C product_i(1+r_i)^M                                         (17)

for fixed C,M. Identical shifts give identical rows and hence zero determinant exactly.

Expand each G_i,n in its uniformly Cauchy-bounded Taylor series. The smallest sum of distinct nonnegative shifts is S, attained only by permutations of 0,...,d−1. Formula (16) for these terms gives (15), including product_j j!. All other nonzero terms have sum of shifts at least S+1. Bound (17) and the geometric Cauchy bounds make their total, after normalization by n^S, O(1/n). This justifies the infinite expansions and the determinant cancellation scale. Constants may depend on d; no uniformity in growing d is asserted.

Apply this lemma to the exact reduced system. Let u_l=(ell_j(p_(n+l)))_(j=0)^b for 1≤l≤b−1, and let Urows denote their list. Put

e=(1,...,1), v=(ell_j(V))_(j=0)^b, w=(ell_j(W))_(j=0)^b,
M=[Urows;e+v].

For a row x, choose the signed maximal-cofactor vector B of M so that B dot x=det[M;x]. Set

D=det[Urows;e;v],
E=det[Urows;e;w],
T=det[Urows;v;w].

The exact identities are

Y=B dot e=−D,
R(1)=B dot w=E+T.                                             (18)

Subtract each column from its successor, retaining the first column. This linear column transformation has determinant one and sends e to (1,0,...,0). Expansion along e leaves the d=b determinant in (15), with functions p_(n+1),...,p_(n+b−1),V or W. The expansion sign is the same in both cases.

By (10) and (13), the limiting Taylor-jet rows are

1,f,...,f^(b−2),G_V,

or the same list with G_W. For b=1 the polynomial list is empty. Put m=b−1. Changing from t to x=f−1 multiplies both coefficient determinants by the same nonzero factor f'(0)^S. In the x coordinate the preceding polynomial rows have a triangular coefficient matrix with diagonal one. The last coefficients are

[x^m]G_V=(−1)^m/(1−s)^m,
[x^m]G_W=(−1)^m/2^m.

Both determinants are nonzero and their ratio is

((1−s)/2)^(b−1)=kappa^(b−1).                                  (19)

It follows from (15) that D≠0 for all sufficiently large n and

E/D=(W(0)/V(0))(kappa^(b−1)+o(1)).                             (20)

This also proves rank and matching nonvanishing immediately: det[M;e]=−D≠0 implies rank(M)=b. Its kernel is therefore one-dimensional, its cofactor vector is nonzero, and its matching value Y is nonzero. Every B solution is proportional to that vector. Equations (1) and Taylor reconstruction then give uniqueness of the complete triple. Since M has rational entries, it has a rational cofactor vector, and reconstruction preserves rationality.

It remains to control T; its smallness is not inferred from a first Taylor coefficient. For every normalized function used here, the same coefficient estimates give

|ell_j(P)|≤C|P(0)|n^j/n!,  0≤j≤b.

The nonzero limit in (15) bounds |D| below by a positive constant times

(product_(l=1)^(b−1)|p_(n+l)(0)|)|V(0)|/((n!)^b n^S).

Expansion of the determinant T then gives

|T/D|≤C|W(0)|n^(b²)/n!,
|(T/D)/(W(0)/V(0))|≤C|V(0)|n^(b²)/n!→0,                     (21)

using (14). Every normalization factor is retained in this estimate; no positivity of the bilinear moment functional or cancellation in T is assumed.

Combining (18), (20), and (21),

R(1)/Y=−(W(0)/V(0))(kappa^(b−1)+o(1)).

Equation (9) and epsilon_(n+1)/epsilon_n→s yield

(-1)^n R(1)/(Y epsilon_n)→((1−s)/2)kappa^(b−1)=kappa^b,

which proves the stated transfer and eventual sign.

The inverted quantities and their status are explicit: h_k, p_k(0), p_k(1), v_k, and V(0) are nonzero at every relevant index; the reference ratios p_(k+1)/p_k are uniformly nonzero on a fixed disk; 1−t is nonzero there; 1+alpha_n/b_n and W(0) are nonzero for sufficiently large n; and the matched endpoint Y is proved eventually nonzero by the determinant, rather than assumed.

Evidence and source identification: the original family and historical transfer statement occur in work/session_20260927/fixed_exponential_degree_error_theorem.md, whole-file SHA-256 74e1c05c04c4d6d100484630898c69c53e31afc178583ce66b3cdd7d0e38b5e4. Original projection and reference formulas were read in work/session_20260913/unequal_degree_hp_attempt.md and work/session_20260913/hp_b2_endpoint_attempt.md. Earlier independent derivations are recorded in work/astra_20260929/worker_2/note_000049.md, note_000050.md, and note_000052.md. Their historical verification labels are not premises of this proof.

Self-audit and scope: the factorial index is n+m+1−j; C* is reversed at degree n; the full exponential and logarithmic tails are both retained; the cofactor sign gives Y=−D; and the reference sign is fixed by (5) and (9). The only imported asymptotic is the published ordinary Padé conclusion specified above. This candidate requires independent review before publication. It proves no bound for q_(n,b)=den(A(1)/Y), no estimate uniform in growing b, and no irrationality conclusion.