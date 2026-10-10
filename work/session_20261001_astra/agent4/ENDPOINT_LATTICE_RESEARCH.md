> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Arithmetic of the relaxed endpoint lattice

New research by Agent 4. All statements below concern caps (n,b,n), contact M=2n+b, and B(1)=C(1), with 1<=b<=n. They apply in particular to b=floor(n/2), n>=2. Assume the square normality matrix J defined below is nonsingular. Establishing this assumption on an unbounded set belongs to Child 3. No previous audit or frozen control is rerun.

The main new results are an all-size two-column content formula for the endpoint index, an exact radial lifting formula for every primitive endpoint direction, and a complete-tail bound whose conditioning is explicit. These are exact reductions, not asymptotic estimates.

## 1. Actual rational lift without arbitrary row clearers

Let F(z)=4 arctan(z/(2-z))=sum f_k z^k. Set f_k=0 for k<0, f_0=0. For nonnegative indices use

f_1=2,
(k+1)f_(k+1)=k f_k-(k-1)f_(k-1)/2, k>=1.

This follows from (1-z+z^2/2)F'(z)=2. Thus every matrix below has an exact rational recurrence construction.

Write each endpoint-matched triple uniquely as

A=(z-1)A'+X,
B=(z-1)B'+Y,
C=(z-1)C'+Y,

where the primed caps are (n-1,b-1,n-1). This is an integral coordinate isomorphism on the endpoint-matching submodule: division by the monic polynomial z-1 preserves integral coefficients and has integer remainder equal to evaluation at one.

Let J have rows k=0,...,M-1 and columns A'_j (0<=j<n), B'_j (0<=j<b), C'_j (0<=j<n). Its entries are respectively delta_(k,j), 1/(k-j)! when k>=j and zero otherwise, and f_(k-j). Define the rational M by 2 matrix G by

G_(k,1)=1,
G_(k,2)=E_k+S_k,
E_k=sum_(h=0)^k 1/h!, S_k=sum_(h=0)^k f_h.

Then the unique primed coefficient vector at endpoint u=(X,Y)^t is

v=V u, V=J^(-1)G.

Proof: the inverse of multiplication by z-1 on truncated Taylor coefficients is minus cumulative summation. Contact requires (z-1)R'+X+Y(exp(z)+F(z))=0 modulo z^M, so R'=(X+Y(exp(z)+F(z)))/(1-z) modulo z^M. This gives exactly Jv=Gu, including its positive sign.

A useful size reduction eliminates the A' columns. Solve the square (n+b) by (n+b) system with rows k=n,...,M-1, columns B',C', and the corresponding rows of G. Recover A'_k for 0<=k<n by subtracting the B'exp and C'F coefficients from (Gu)_k. Denominators introduced during this recovery must be retained; the denominator of the B',C' block alone need not clear V.

Define d>=1 as the least common positive denominator of every entry of V, and W=dV in Z^(M by 2). Then

gcd(d, all entries of W)=1.

All following quantities are independent of enlargement of Taylor row clearers. This d is the denominator of the actual rational lift, not an arbitrarily chosen coefficient clearer.

## 2. Saturation becomes a two-column congruence

The endpoint lattice is exactly

Lambda={u in Z^2: Wu=0 modulo d}.

Indeed, an integral original triple has integral endpoints and integral primed coefficients. Conversely integral u and integral Vu reconstruct an integral original triple. This equivalence proves saturation directly; clearing two separate rational nullspace vectors would not suffice.

Consequently Z^2/Lambda is the image of the map u -> Wu modulo d. Its exponent is d. To see the exponent assertion prime by prime, minimality of d supplies, for every p dividing d, an entry of W not divisible by p. One coordinate basis vector therefore has image order divisible by the full p-part of d. The group is killed by d, establishing equality of the exponent.

For any integer two-column matrix W define s_1=gcd of its entries and t_2=gcd of its two-row determinants. Zero determinants are included in the gcd; the gcd of an all-zero list is zero. Integer Smith operations show that the index I=[Z^2:Lambda] is

I=d^2/gcd(d^2, d times all entries of W, all two-row determinants of W).    (A)

This expression covers rank zero and rank one as well as rank two. At d=1 it gives I=1.

Proof: integer unimodular row and column operations preserve both the congruence index and the displayed determinantal gcd. In rank two put W into Smith form diag(s_1,s_2), with s_1|s_2 and s_1*s_2=t_2. The index is the product over i=1,2 of d/gcd(d,s_i). For p with a=v_p(d), x=v_p(s_1)<=y=v_p(s_2), the denominator in (A) has valuation min(2a,a+x,x+y)=min(a,x)+min(a,y). Rank one follows by taking y=infinity, and rank zero directly.

For the least denominator d, gcd(d,s_1)=1. Formula (A) therefore simplifies to the all-size content reduction

I=d^2/c, c=gcd(d,t_2).                                      (B)

In particular d divides I and I divides d^2. This reduces maximal-minor content of the full constraint matrix to gcds of two-row determinants of a rational lifting matrix. It is an exact reduction in dimension and in content, not a bound claiming d is small.

The local formula is especially simple. For a=v_p(d)>0,

v_p(I)=2a-min(a,v_p(t_2)).                                  (C)

Thus a<=v_p(I)<=2a. Rank-one W gives c=d and I=d. No product of overlapping row or column contents has been inserted.

Combining (B) with the main bridge gives an exact expression for the original maximal-minor content:

Delta_(N-2)(T)=abs(det([T;E]))*c/d^2
             =(product Taylor row clearers)*abs(det J)*c/d^2.

The result is an integer by the lattice proof. The rational factors must remain intact when evaluating this identity. Signs of determinants disappear only in the explicitly absolute quantities.

## 3. Individual endpoint gcds and radial lifting

Let u=(P,Q) be a primitive integer pair. The smallest positive integer m with mu in Lambda is

m(u)=d/gcd(d, (Wu)_1,...,(Wu)_M).                           (D)

Proof: d must divide each m(Wu)_i. Taking prime valuations gives v_p(m)=max(0,v_p(d)-min_i v_p((Wu)_i)), which is (D).

The unique integral triple with endpoint m(u)u is primitive as a coefficient vector. If every coefficient had a common divisor h>1, then h would divide both endpoints, hence h|m(u), because u is primitive. Dividing the triple by h would contradict the minimality of m(u). Its endpoint gcd is exactly m(u), even though its coefficient gcd is one.

More generally, every nonzero endpoint vector has a unique expression g u with u primitive and g>0 up to the chosen sign of u. It belongs to Lambda precisely when m(u)|g. Its reduced denominator is |Q| when Q!=0, independently of g. This explicitly separates coefficient saturation, endpoint gcd, and individual reduced denominator.

For two independent primitive directions u_1,u_2, the two minimal integral lifts have endpoint determinant

m(u_1)m(u_2)*abs(det[u_1,u_2]).

Their index as a sublattice of Lambda is therefore

h=m(u_1)m(u_2)*abs(det[u_1,u_2])/I,                          (E)

a positive integer. They form a basis of Lambda exactly when h=1. Requiring a lattice basis can therefore exclude useful independent directions; the paired-form criterion only requires independence.

A significant limitation follows: every primitive direction in Z^2 is available after multiplication by its radial lifting factor. Hence the primitive directions allowed by this relaxed construction are all rational directions. Arithmetic of the endpoint index alone cannot select approximations to e+pi. A useful theorem must control the actual lift in those directions and its complete remainder.

## 4. Exact compatibility with complete remainders

Let H:Q^2 -> Q^N denote the full coefficient lift obtained from V and the reconstruction in Section 1. Let beta_j(u) and gamma_j(u) be its B and C coefficients. Thus beta_j and gamma_j are explicit rational linear forms in (P,Q), computable from J^(-1)G. They refer to the rational triple with endpoint u, before the radial integer scaling.

For M=2n+b, the polynomial A contributes no Taylor coefficient at indices >=M. Contact therefore gives the exact complete-tail functional

R_u(1)=sum_(j=0)^b beta_j(u) T_exp(M-j)
       +sum_(j=0)^n gamma_j(u) T_F(M-j),                    (F)

where

T_exp(k)=sum_(h=k)^infinity 1/h!,
T_F(k)=sum_(h=k)^infinity f_h.

These series converge absolutely. In particular R_u(1)=P+Q(e+pi). Formula (F) retains all cancellation if its two sums are evaluated together. It is not a first-omitted-coefficient approximation.

For the minimal integral lift m(u)H u, both its full remainder and its endpoint gcd acquire exactly the same factor m(u). Therefore

R_(m(u)Hu)(1)/g=R_u(1), g=m(u).                            (G)

This cancellation is essential: a large endpoint gcd obtained solely from denominator clearing does not improve the primitive error bound. It simply brings one back to the rational lift H u.

An explicit rigorous absolute majorant is available without another analytic source. Let rho=1/sqrt(2). Factorization of 1-z+z^2/2, or integration of its partial fractions, gives

f_h=4 rho^h sin(h*pi/4)/h, h>=1.

It follows that, for k>=1,

T_exp(k)<=e/k!,
abs(T_F(k))<=sum_(h=k)^infinity abs(f_h)
            <=4 rho^k/[k(1-rho)].

Define the fully explicit lift-conditioned bound

B_n(u)=sum_(j=0)^b e*abs(beta_j(u))/(M-j)!
       +sum_(j=0)^n 4*rho^(M-j)*abs(gamma_j(u))/[(M-j)(1-rho)].    (H)

Then abs(P+Q(e+pi))<=B_n(u). All starting indices are positive in the stated domain. This majorant can be replaced by Child 2's sharper complete-remainder functional; equations (D), (E), and (G) remain unchanged. The absolute majorant (H) itself makes no claim to exploit the important cancellations of (F).

The relevant conditioning is the action of the actual rational lift on chosen endpoint directions, not the size of a convenient integer kernel basis. For example, define

kappa_n=max over ||u||_infinity<=1 of B_n(u).

Then B_n(u)<=kappa_n||u||_infinity, but this isotropic bound can be much weaker than evaluating (H) on the chosen directions. Its definition keeps the potentially large inverse-J coefficients visible. No uniform estimate for kappa_n is proved here.

## 5. Basis selection with explicit primitive reduction

One safe formulation of the remaining selection problem is the second primitive minimum

lambda_2(n)=inf over independent primitive u_1,u_2 in Z^2
            of max(B_n(u_1),B_n(u_2)).

For fixed n, B_n is a norm on R^2: it is a nonnegative weighted sum of absolute rational linear forms, and simultaneous vanishing of all B,C coefficients forces Y=0; contact then forces A=0 and X=0. Thus bounded B_n balls are compact and the indicated infimum is attained. This is a precise optimization problem, not a hidden favorable basis choice. If sharper estimates are used, their corresponding positivity or compactness conditions must be stated separately.

The exact arithmetic procedure for any selected pair is: compute its two radial orders from (D), lift to primitive integral coefficient triples, and reduce by those same endpoint gcds. Formula (E) then checks their sublattice index. They need not be a basis.

For an already computed saturated endpoint basis L=[l_1,l_2], every candidate is Lz with z in Z^2. Define g(z)=gcd of the two coordinates of Lz. The exact directional objective is

B_n(Lz)/g(z).

Thus independent integer coefficient vectors z_1,z_2 supply two primitive bounds by evaluating this expression separately. Replacing both gcds by a function of det L is invalid. Restricting to det[z_1,z_2]=+-1 is optional and can worsen the optimum.

Even the canonical triangular lattice basis illustrates the danger: if its first vector is (a,0), its primitive reduction is (+-1,0), whose form has absolute value 1. Such a basis cannot itself provide two shrinking primitive forms, regardless of its index.

A useful necessary consistency condition for any pair with max absolute primitive error <=epsilon is

1<=abs(det[u_1,u_2])<=epsilon*(abs(Q_1)+abs(Q_2)).

Consequently at least one reduced denominator is >=1/(2epsilon). This quantifies why two small forms require a growing direction scale; one cannot infer them from small endpoint vectors or lattice covolume alone.

## 6. Precise asymptotic requirements

The arithmetic theorem is conditional only on nonsingularity of J, and is valid at every size in that domain. It establishes formulas (A)-(G), not useful growth rates for their entries.

For b=floor(n/2), an arithmetic analysis can now target the intrinsic lift denominator d_n and the capped minor content c_n=gcd(d_n,t_2(W_n)); the exact local budget is (C). Bounds for these quantities would describe the endpoint lattice but would still not establish small primitive forms.

A sufficient paired-form theorem requires an unbounded set of normal indices and independent primitive directions u_(n,1),u_(n,2) with max_i B_n(u_(n,i))->0, or the same condition for a sharper justified complete-remainder bound retaining cancellation. The radial factors are then given exactly by (D), and no separate individual full-remainder nonvanishing theorem is needed for the paired rationality contradiction.

Open requirements are therefore: normality from Child 3; effective control of the directional rational lift or Child 2's complete functional on a selected independent pair; and a selection argument exhibiting that pair with its own gcds retained. No estimate for the full inverse lift, its primitive second minimum, or its same-index asymptotics is claimed here. The recurrences in Section 1 construct the actual arithmetic input, but do not yet close to a low-order recurrence for d_n or c_n.

The main bridge TWO_DIMENSIONAL_ENDPOINT_BRIDGE.md was read as a source for the setup and determinant/index identity. This document develops it as new research, rather than reopening its review. The completed two-scalar audit and its reported prose correction remain untouched. No numerical controls, prime tables, or previous checks were executed for these deductions.
