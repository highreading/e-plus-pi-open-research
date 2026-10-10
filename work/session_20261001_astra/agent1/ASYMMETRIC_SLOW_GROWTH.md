> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Asymmetric allocation with slowly growing exponential degree

Status: new proved identities and uniform inequalities, with explicit conditional domains. Weighted normality, useful endpoint conditioning, and favorable actual reduced-denominator estimates remain open. The existing verification register is accepted within its documented scope; no previous audit is resumed or repeated.

Take integers n>=1 and

    a=2n, c=n, b=max(1,floor(log n)), M=3n+b,

where log is natural. The algebra below is valid more generally for 1<=b<=n. Let

    R(z)=A(z)+B(z)exp(z)+C(z)F(z),
    F(z)=4 arctan(z/(2-z)),
    deg A<=2n, deg B<=b, deg C<=n,
    B(1)=C(1), R(z)=O(z^M).

All rational solution directions are retained until an explicitly stated optional selection. In particular, the contact condition does not define a unique approximant.

## 1. Moments and the changing orthogonality weight

Put

    t(u)=(1+iu)/2, -1<=u<=1,
    L(P)=integral_(-1)^1 P(t(u)) du,
    mu_m=L(t^m), rho=1/sqrt(2).

The exact representation is

    F(z)=z L(1/(1-tz)), |z|<sqrt(2).

Differentiating the right side gives 4/(z^2-2z+2), and both sides vanish at zero. This also fixes the branch and integration constant. In particular F(1)=pi and L(1/(1-t))=pi. The moments are rational:

    mu_m=((1+i)^(m+1)-(1-i)^(m+1))/(i 2^m(m+1)),
    |mu_m|<=2 rho^m,
    2^m(m+1)mu_m is an integer.

Define sigma_0=0 and sigma_k=sum_(h=0)^(k-1) mu_h. Then

    L(t^k/(1-t))=pi-sigma_k.                         (1)

Write

    B(z)=sum_(j=0)^b beta_j z^j,
    Cstar(t)=t^n C(1/t)=sum_(i=0)^n gamma_i t^i.

Thus gamma_i=[z^(n-i)]C and Cstar(1)=C(1). At Taylor degree k=2n+1+r,

    [z^k](B exp(z))=sum_j beta_j/(2n+1+r-j)!,
    [z^k](C F)=L(t^(n+r) Cstar(t)).

The new functional and factorial functionals are therefore

    L_n(P)=L(t^n P),
    ell_j(t^r)=1/(2n+1+r-j)!, 0<=j<=b.              (2)

On the real u segment the weight is ((1+iu)/2)^n. It is complex and depends on n. The bilinear pairing L_n(PQ) is not a positive inner product. Ordinary Legendre norms, ratio bounds and normality conclusions for weight 1 do not automatically apply. For example, the explicit moment formula gives mu_n=0 when n=3 modulo 4, so even the first leading Gram minor can vanish. This observation does not determine the larger Gram determinant used below.

## 2. Unconditional rational system, endpoints and full remainder

Eliminate A by Taylor truncation. The remaining exact equations are

    ell_beta(t^r)+L_n(t^r Cstar)=0,
        0<=r<=n+b-2,
    sum_j beta_j-sum_i gamma_i=0,                  (3)

where ell_beta=sum_j beta_j ell_j. There are n+b-1 high Taylor equations and one matching equation, in n+b+2 rational unknowns. Consequently the rational solution space has dimension at least two. This statement does not require a Gram determinant or a normality assumption.

Explicitly, the high block has entries

    E_rj=1/(2n+1+r-j)!,
    Grect_ri=mu_(n+r+i).

The full reduced matrix is [E Grect] followed by the matching row [ones,-ones]. All factorial arguments are positive in the stated domain.

For 0<=k<=2n, Taylor reconstruction is

    [z^k]A=-sum_(j<=min(b,k)) beta_j/(k-j)!
             -sum_(l<=min(n,k-1)) [z^l]C * mu_(k-l-1).

Let Epartial_m=sum_(h=0)^m 1/h!. The actual rational endpoints are

    Y=B(1)=C(1)=sum beta_j=sum gamma_i,
    X=A(1)=-sum_j beta_j Epartial_(2n-j)
             -sum_i gamma_i sigma_(n+i).             (4)

In particular R(1)=X+Y(e+pi), where e=exp(1). These are the actual endpoints, before any clearing or gcd removal.

Define Tail_m=sum_(h=m)^infinity 1/h! for m>=1. Contact through degree M-1 gives the complete evaluated remainder

    R(1)=sum_j beta_j Tail_(M-j)
           +L(t^(2n+b-1) Cstar(t)/(1-t)).             (5)

Both full tails are present. Absolute convergence follows from |t|<=rho<1 and the factorial series. No first omitted Taylor coefficient is substituted for either tail.

If contact is increased to M+1, equation (3) gains exactly the row r=n+b-1. Its rational solution space has dimension at least one. In (5), the exponential starting indices increase by one and the power 2n+b-1 becomes 2n+b. This is a different contact subspace, not an automatic choice of a nonzero-endpoint direction.

The endpoint map is another rank question. For the full matrix K in (3), a direction with Y!=0 exists exactly when appending the row [ones,0] increases its row rank. Two rational solution directions alone do not prove this. There is always at least one nonzero direction in the kernel of Y. If the endpoint map to (X,Y) has rank two, it is surjective over Q; useful approximation then still requires a height-controlled choice of direction.

## 3. Projection reduction, with its normality hypothesis exposed

For b>=2, the first n+1 high rows are present. Define the symmetric rational matrix

    G_n=(mu_(n+i+r))_(i,r=0)^n,
    v(t)=(1,t,...,t^n)^T.

Assume det G_n!=0 for this section. Put eta_beta=(ell_beta(t^r))_(r=0)^n. Then

    gamma=-G_n^(-1) eta_beta.                         (6)

For any polynomial P define its weighted projection

    Pi_n P=v(t)^T G_n^(-1) L_n(v P).

For r=n+1,...,n+b-2 set Q_r=t^r-Pi_n(t^r). These polynomials are orthogonal to every polynomial of degree at most n for the bilinear functional L_n. The remaining high equations become exactly

    ell_beta(Q_r)=0, n+1<=r<=n+b-2.                  (7)

There are b-2 such equations, with the empty range understood when b=2. Mutual orthogonality among the Q_r is unnecessary.

Define the reproducing kernel and two projected functions by

    K_n(t,s)=v(t)^T G_n^(-1) v(s),
    V(t)=K_n(t,1),
    H(t)=L_n,s(K_n(t,s)/(1-s)),
    W(t)=1/(1-t)-H(t).

The vector in the integral defining H has coordinates pi-sigma_(n+i). Thus, with

    J(t)=v(t)^T G_n^(-1)(sigma_n,...,sigma_(2n))^T,

one has the exact decomposition

    H=pi V-J, W=1/(1-t)-pi V+J.

Put u_j=ell_j(V), w_j=ell_j(W), and

    x_j=-Epartial_(2n-j)+ell_j(J).

Then Cstar(1)=-sum beta_j u_j, so matching is

    sum_j beta_j(1+u_j)=0.                            (8)

The reduced matrix in beta consists of the b-2 rows in (7) and the matching row (8): b-1 rows in b+1 columns. Its kernel still has dimension at least two. Moreover

    X=sum beta_j x_j,
    Y=sum beta_j,
    R(1)=ell_beta(W),
    w_j=x_j+e-pi u_j.                                (9)

This derives the complete evaluated remainder from the weighted projection and agrees with the direct rational endpoint formula (4).

If G_n is singular, equations (3)--(5) remain valid and must be used directly; an inverse or a positive norm cannot be silently assigned to it.

The b=1 edge case has only n high equations. If the n-by-n matrix (mu_(n+i+r))_(i,r=0)^(n-1) is invertible, projection onto degree at most n-1 gives

    Cstar=Cpart+zeta P_n,

where P_n is the monic degree-n polynomial orthogonal to that lower-degree space and zeta is free. Matching supplies one equation in beta_0,beta_1,zeta. The complete remainder is ell_beta(W_(n-1))+zeta L_n(P_n/(1-t)). Equations (3)--(5) cover this case without the auxiliary invertibility assumption. The formula (6), which uses n+1 high rows, is not asserted for contact M with b=1.

## 4. Weighted CD normalization and the necessary rational endpoint shift

This section provides an optional adjacent-polynomial form. It is conditional on both G_n and its leading n-by-n submatrix being nonsingular. No all-index claim about these determinants is made.

For the fixed functional L_n, let P and Q be its monic orthogonal polynomials of degrees n and n+1, respectively, and let h=L_n(P^2)!=0. Write

    Aend=P(1), Bend=Q(1),
    wP=L_n((P-Aend)/(t-1)),
    wQ=L_n((Q-Bend)/(t-1)).

These second-kind polynomial contractions are rational. The finite-dimensional CD and reproduction identities give

    K_n(t,1)=(Bend P(t)-Aend Q(t))/(h(1-t)),
    Aend wQ-Bend wP=h.

Neither h nor the endpoint values are identified with the ordinary Legendre quantities from the equal-degree allocation.

Set

    D(t)=(wQ P(t)-wP Q(t))/h, D(1)=1,
    m_n=L_n(1/(1-t))=pi-sigma_n.

Integrating the CD subtraction gives exactly

    W(t)=D(t)/(1-t)-m_n V(t).                         (10)

For every polynomial T define

    T_j(T)=sum_m [t^m]T(t) Epartial_(2n+m-j).

Absolutely convergent factorial sums prove

    ell_j(T/(1-t))=e T(1)-T_j(T).

All partial-sum indices are nonnegative for j<=b<=n. Therefore

    u_j=(Aend T_j(Q)-Bend T_j(P))/h,
    x_j=(wP T_j(Q)-wQ T_j(P))/h+sigma_n u_j.           (11)

The rational shift sigma_n is essential. The weighted mass is pi-sigma_n, while the target at z=1 remains e+pi. Omitting the last term in x_j would change the actual numerator.

For a matched vector beta with Y!=0, write T_beta=sum beta_j T_j. Then

    X/Y=-sigma_n
       +(wP T_beta(Q)-wQ T_beta(P))
         /(Bend T_beta(P)-Aend T_beta(Q)).             (12)

The denominator in (12) is hY. This identity retains both partial-exponential contractions and both rational second-kind contractions, including their endpoint cancellation. The rational shift also participates in final denominator reduction.

## 5. A first uniform complete-tail estimate

For any solution of (3), including singular-Gram cases, define

    ||beta||_1=sum_j |beta_j|,
    ||gamma||_rho=sum_i |gamma_i|rho^i.

Since Tail_m<=e/m! and |1-t|>=1/2 on the integration segment, (5) gives the unconditional inequality

    |R(1)|<=e ||beta||_1/(3n)!
                +4 rho^(2n+b-1)||gamma||_rho.         (13)

At contact M+1, replace (3n)! by (3n+1)! and multiply the logarithmic term by rho. Thus the additional contact improves these particular tail factors by 1/(3n+1) and rho; it does not by itself alter their leading factorial/geometric scales.

For b>=2 and det G_n!=0, define the explicit inverse-conditioning quantity

    Kappa_n=sum_(i=0)^n rho^i sum_(r=0)^n |(G_n^(-1))_ir|,
    d0=2n+1-b.

Equation (6) implies

    ||gamma||_rho<=Kappa_n ||beta||_1/d0!,

because every component of eta_beta is at most ||beta||_1/d0! in modulus. Hence the new projected uniform estimate is

    |R(1)|<=||beta||_1 [e/(3n)!
                    +4 rho^(2n+b-1)Kappa_n/d0!].      (14)

This is an all-size inequality, not a fixed-b asymptotic. Its dependence on the changing weighted inverse is explicit. It supplies no favorable estimate for Kappa_n merely by defining that quantity.

There is also a completely explicit, conservative bound for Kappa_n on the same nonsingular domain. Let

    Lcm_n=lcm(1,2,...,3n+1).

The matrix S_ir=Lcm_n 2^(n+i+r)mu_(n+i+r) is integral, and

    det G_n=det S/[2^(2n(n+1)) Lcm_n^(n+1)].

Thus |det G_n|>=2^(-2n(n+1))Lcm_n^(-(n+1)) when it is nonzero. Using |mu_(n+i+r)|<=2rho^(n+i+r), diagonal extraction and Hadamard's inequality bound an n-by-n cofactor, deleting row r and column i, by

    2^n n^(n/2)rho^(2n^2+n-r-i).

Multiplying by rho^i, summing the (n+1)^2 inverse entries, and using r<=n proves

    Kappa_n<=Khat_n,
    Khat_n=(n+1)^2 n^(n/2)2^(n^2+3n)Lcm_n^(n+1).      (15)

Every dimension factor is retained. For example Lcm(1,...,N)<=16^N follows by bounding the lcm increment on each dyadic interval by the central binomial coefficient. Consequently log Khat_n=O(n^2). This is a coarse rigorous ceiling, not evidence that the actual conditioning has that size.

## 6. Optional cofactor selection and uniform determinant bounds

The two-dimensional freedom must be specified before referring to a single cofactor sequence. For b>=2, append a rational selector row to (7), and call the resulting b-1 rows Hhigh. Then append the matching row evec+u. If this b-by-(b+1) matrix has rank b, define beta by

    beta dot z=det[Hhigh;evec+u;z].

Set

    D_V=det[Hhigh;evec;u],
    D_W=det[Hhigh;evec;w],
    Tcomp=det[Hhigh;u;w].

Exactly,

    Y=-D_V, R(1)=D_W+Tcomp.                           (16)

The cofactor representative is useful only when D_V!=0. If the augmented rank is smaller, its cofactors vanish; this does not eliminate the larger underlying solution space. At contact M+1 the additional high row can replace the selector, subject to the same rank and endpoint qualifications.

For completeness, any rational selector can be represented as (ell_j(Sel))_(j=0)^b for a rational polynomial Sel of degree at most b. Multiplying column i of the matrix 1/(2n+1+i-j)! by (2n+1+i)! turns its rows into monic falling-factorial polynomials evaluated at consecutive points. Its determinant is

    product_(j=1)^b j! / product_(i=0)^b (2n+1+i)!,

which is nonzero. This representation does not bound the selector's polynomial coefficients.

Here is a direct uniform contour estimate with no assumption about zeros of weighted orthogonal polynomials. Choose the analytic disk radius eta=1/4 and contour radius T>4, and use the constant reference function 1. The factorial contour identity is

    ell_j(P)=(1/(2pi i)) integral_(|z|=T)
                  exp(z) z^(j-2n-2) P(1/z) dz.

For d functions analytic near |t|<=eta, bounded there by M_i, put

    S_d=d(d-1)/2,
    C_d(T)=d^(d/2) eta^(-S_d)
                 (1-1/(eta T))^(-(d+S_d)),
    J_d(T)=(2pi)^(-d/2)(4T/pi^2)^(-d^2/2)
                 product_(j=1)^d j!,
    E_2n(T)=exp(T)(T+1)T^(-2n-1).

The determinant integration identity, Cauchy divided differences and the Gaussian Vandermonde integral give

    |det[(ell_(j+1)-ell_j)(P_i)]|
       <=C_d(T)(product M_i)E_2n(T)^d J_d(T)/d!,

and for ordinary ell_j replace E_2n(T) by E_2n(T)/(T+1). The difference determinant uses d<=b and the ordinary determinant d<=b+1. Both applications therefore remain within j<=b<=n. The Gaussian identity is used in its all-dimension scope; it asserts no positivity of the original complex moment problem.

One can take fully specified analytic row bounds

    M_V=Kappa_n,
    M_W=1/(1-eta)+4rho^n Kappa_n,
    M_Qr=eta^r+2rho^(n+r)Kappa_n,
    M_Sel=sum_i |[t^i]Sel|eta^i.

Indeed the projection coefficients are obtained with G_n^(-1), and the relevant weighted moments have bounds 2rho^(n+r) and 4rho^n. Since eta<=rho, the coefficient estimates are controlled by Kappa_n. Let

    Hprod=M_Sel product_(r=n+1)^(n+b-2) M_Qr.

Then valid complete cofactor bounds are

    B_V=C_b Hprod M_V E_2n^b J_b/b!,
    B_W=C_b Hprod M_W E_2n^b J_b/b!,
    B_T=C_(b+1) Hprod M_V M_W
              [E_2n/(T+1)]^(b+1)J_(b+1)/(b+1)!.

They satisfy |D_V|<=B_V, |D_W|<=B_W and |Tcomp|<=B_T. All selector, weighted-inverse and dimension factors remain visible. On D_V!=0 the actual primitive estimate is

    |L_int|<=q(B_W+B_T)/|D_V|.                        (17)

Dividing B_W or B_T by B_V does not bound an actual determinant quotient.

For T=2n+5, log E_2n=-2n log n+O(n). With b of order log n the bare contour contribution is -2nb log n+O(nb); the dimension factors have logarithms O(b^2(log n+log(b+1))). The row amplitudes and actual endpoint can change the outcome completely. The small cofactor scale is shared with the endpoint and cannot be treated as a proved normalized error rate.

## 7. Coefficient clearing and the actual endpoint gcd

Choose a nonzero rational solution and scale its pair (B,C) to a primitive integral coefficient vector. This fixes a convenient arithmetic representative; it is not a claim that small integral coefficients exist.

Let D_m=F^(m)(0). The differential equation

    (1-z+z^2/2)F'(z)=2

gives D_0=0, D_1=2 and

    D_(m+1)=m D_m-binom(m,2)D_(m-1), m>=1.

Thus every D_m is an integer. Taylor reconstruction consequently proves that

    Delta_clear=(2n)!

clears every coefficient of A. It also clears the integral B,C. This is a proved, possibly nonminimal coefficient clearer.

Define the two integers and their final gcd by

    Xint=Delta_clear X,
    Yint=Delta_clear Y,
    g_ep=gcd(|Xint|,|Yint|), assuming Y!=0.

Then exactly

    q=|Yint|/g_ep,
    p=sign(Yint)Xint/g_ep,
    p/q=X/Y,
    |p+q(e+pi)|=q|R(1)|/|Y|
                 =Delta_clear |R(1)|/g_ep.            (18)

This includes any full polynomial content and the final endpoint cancellation. Neither Delta_clear nor a determinant denominator is substituted for q. If X=0 the formula gives q=1; Y=0 is outside the quotient domain.

Combining (14) with (18) gives the explicit arithmetic budget

    |L_int|<=||beta||_1/g_ep *
      [e(2n)!/(3n)!
       +4Kappa_n 2^(-n)(sqrt(2)n)^(b-1)].             (19)

Here (2n)!/(2n+1-b)!<=(2n)^(b-1) was used in the second term. In particular,

    log((2n)!/(3n)!)=-n log n+O(n),
    2^(-n)(sqrt(2)n)^(b-1)
          =exp(-n log 2+O((log n)^2)).

These are proved tail/clearing scales. Their multipliers ||beta||_1/g_ep and Kappa_n are not controlled by this calculation. Integral scaling of a projected rational solution can enlarge beta substantially, and endpoint matching can make Y very small in a rational normalization.

For example, matching and (6) imply

    |Y|<=rho^(-n)Kappa_n ||beta||_1/d0!.

Thus the positive normalized expression obtained directly from (14) has the lower bound

    q||beta||_1/|Y| *
       [e/(3n)!+4rho^(2n+b-1)Kappa_n/d0!]
       >=4q rho^(3n+b-1).                             (20)

This lower bound still decays for q=1. No new-family q lower bound making it diverge has been established. It illustrates why raw factorial decay is not itself a normalized approximation theorem.

A provisional sufficient route, not a proved estimate, would require on the same unbounded set: the necessary nonsingularity and nonzero endpoint; a direction with log(||beta||_1/g_ep)=o(n log n); and

    log(Kappa_n ||beta||_1/g_ep)<=(log 2-eta0)n

for some fixed eta0>0. Equation (19) would then tend to zero. Full-remainder nonvanishing would still be needed for nonzero shrinking integer forms. No such direction, conditioning estimate, arithmetic estimate or nonvanishing theorem is claimed.

## 8. Stopped coarse certificate and a concrete alternative allocation

The bound (15) is useful as a rigorous absolute estimate but cannot serve as a shrinking certificate after it replaces Kappa_n in (14). Indeed q||beta||_1/|Y|>=1. Since Lcm_n>=1 and d0!<=(2n)!<=(2n)^(2n), the logarithm of that substituted positive expression is at least

    n^2 log 2-(3/2)n log n
       -((b-1)/2)log 2+2log(n+1)+log 4.

For b=max(1,floor(log n)) this tends to positive infinity. Therefore the inverse-by-integer-denominator subroute is stopped here. This is a proved obstruction to that particular coarse certificate, not divergence or exclusion of the actual family and not a lower bound for its true error.

A concrete different allocation for a follow-up is

    a=n+1, c=n, b=max(1,floor(log n)),
    contact M=2n+b+1.

Its moment weight is the fixed polynomial t rather than t^n, so it removes the linearly growing modification of the moment functional while retaining growing b and at least two rational directions. This is a proposed parameter choice, not a claimed successful certificate; no indices for it were evaluated. The original (2n,b,n) family can instead be revisited through a genuinely sharper bound for its actual weighted inverse or a direct normalized quotient.

There is no established exact equivalence between the requested family and an excluded fixed-b construction. Here both the offset 2n in ell_j and the nonconstant weight t^n differ from the equal-allocation system, and b grows. The existing exclusions cannot be imported by relabeling n.

The previous quadratic high-row slack proof also cannot be imported. It used ordinary Legendre ratios on a fixed disk and a specific retained product (3/4)^N for b of order n. The weighted residual polynomials here have no proved version of those ratio bounds. Even a constant loss accumulated over O(b^2) factors would have logarithm only O((log n)^2) in the present regime. Conversely, that smaller count alone supplies neither weighted conditioning nor an endpoint quotient bound.

## 9. Established results, remaining gaps and evidence

New proved results in this note are the unconditional rational system and dimension count, both full endpoint/tail formulas, the conditional weighted projection and CD normalizations, complete uniform tail and determinant inequalities with dimensions retained, the coefficient clearer (2n)!, the exact final reduced-q formula, and the obstruction to the explicitly identified coarse inverse certificate.

The remaining questions are precise:

- Whether the relevant weighted Gram matrices are nonsingular on a useful unbounded set, or how to work efficiently with the full system when they are singular.
- Whether its solution space contains a nonzero matched endpoint and admits a quantitatively controlled choice of rational direction.
- Bounds on the actual Kappa_n or on a direct normalized determinant quotient, together with the actual endpoint gcd g_ep or reduced q.
- Nonvanishing of the complete R(1) at the same selected indices.

No fixed-b asymptotic, new degree sweep, prime search, or old audit was performed. The first symbolic execution saved asymmetric_formal_evidence.json and verified the integral derivative, weight exponent and equation counts. The second execution saved asymmetric_slow_growth_checks.json and passed all 15 controls in check_asymmetric_slow_growth.py. These cover indexing, the derivative recurrence, weighted rational endpoint shift, selector determinant, Gram scaling and the clearing-budget factors. They do not establish the open analytic or rank assertions.

The second checker also verified unchanged bytes for the generated companion-audit checker, its successful certificate and stdout, and the initial asymmetric evidence. Those previous artifacts are preserved without further companion-audit calculations or paperwork. The unrestricted inequalities above are paper proofs; no numerical evidence is presented as a substitute for them.
