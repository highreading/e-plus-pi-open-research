> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Growing-degree endpoint nonvanishing: exact representation and remaining lemma

Author: Agent 3. Status: recovered analysis, with proved identities, a sufficient unproved coefficient lemma, exact obstructions to stronger sign arguments, and one frozen exact control. No unbounded endpoint-nonvanishing theorem is established.

This completes the previously unsaved endpoint assignment. The existing endpoint_wronskian_control.json is preserved. The completed prime certificate, growing-degree audit, and Gaussian refinement are not modified. No new degree sweep, prime scan, or Gaussian optimization is undertaken.

## 1. Scope, notation, and factorial domains

Let n>=2 and 1<=b<=n; the intended growing regime is b=floor(n/2). Use the monic polynomials

    p_k(t)=k!/(2k)! * D_t^k (t^2-t+1/2)^k,
    h_k=2(-1)^k/[(2k+1) binom(2k,k)^2],
    V(t)=sum_(k=0)^n p_k(1)p_k(t)/h_k.

The underlying moment functional is the complex-segment functional

    L(P)=integral_(-1)^1 P((1+iu)/2) du.

Its bilinear norms h_k are nonzero and alternate in sign. No positive real moment interpretation is assumed.

For a polynomial P, define

    Phi_n(P;x)=sum_(m>=0) [t^m]P(t) x^(n+m+1)/(n+m+1)!.

The sum is finite. For 0<=j<=b,

    D_x^j Phi_n(P;1)=ell_j(P),
    ell_j(t^m)=1/(n+m+1-j)!.

Every factorial argument is at least n+1-b>=1. In the full endpoint Wronskian the derivative columns run from 0 through b, so they stay in this domain. A d-column difference determinant uses ell_0 through ell_d and requires d<=b; an ordinary determinant uses ell_0 through ell_(d-1) and requires d<=b+1. These are precisely the domains recorded in ../agent2/GROWING_DOMAIN_CORRECTION.md. No reciprocal-Gamma extension or convention for negative factorials is introduced.

Write U for the b-1 rows ell_j(p_(n+l)), l=1,...,b-1, and write

    e=(1,...,1), v=(ell_j(V))_(j=0)^b,
    M=[U;e+v], D_V=det[U;e;v].

The empty high-row list is allowed when b=1. The cofactor convention throughout is

    B_j=(-1)^(b+j) det(M with column j removed), j=0,...,b,
    B dot a=det[M;a].

Thus the cofactor representative has endpoint

    Y=B(1)=det[U;e+v;e]=-D_V.

A nonzero D_V proves rank M=b and a nonzero endpoint. Rank alone does not prove endpoint nonvanishing. These facts concern the actual reduced system and its Taylor reconstruction, not a surrogate matrix.

## 2. Exact high-function identity

Set

    a_s(k)=[z^s](1-z+z^2/2)^k,
    H_k(x)=k![z^k] exp(xz)(1-z+z^2/2)^k.

Here H_k(x) is the auxiliary polynomial, not the projection polynomial H(t) used later. Explicitly,

    H_k(x)=k! sum_(m=0)^k a_(k-m)(k) x^m/m!.

Rodrigues gives, for 0<=m<=k,

    [t^m]p_k(t)=k! a_(k-m)(k)(k+m)!/[(2k)!m!].

Indeed, the coefficient of t^(k+m) in (t^2-t+1/2)^k is a_(k-m)(k), and differentiation contributes (k+m)!/m!.

For k=n+l with 1<=l<=b-1, substitute this coefficient formula into Phi. Termwise differentiation proves

    Phi_n(p_(n+l);x)
      =D_x^(l-1)[x^(n+l) H_(n+l)(x)]/(2n+2l)!.

The differentiated exponent is k+m-l+1=n+m+1. Its factorial is positive; the derivative order l-1 is at most b-2. All factorials (2k)!, (k+m)!, m!, and (n+m+1)! occur only at nonnegative integer arguments. This identity is exact for all allowed n,l, without an asymptotic qualification.

Define a row-oriented Wronskian by

    Wr(f_1,...,f_d)(x)=det[D_x^j f_i(x)]_(i=1,...,d; j=0,...,d-1).

Let

    f_l=Phi_n(p_(n+l);x), E(x)=exp(x-1), F_V=Phi_n(V;x).

Since E^(j)(1)=1, the endpoint determinant is exactly

    D_V=Wr(f_1,...,f_(b-1),E,F_V)(1).

Both the order of functions and the derivative-column order are essential to the sign.

## 3. Real Volterra representation and recurrence

For P(t)=sum c_m t^m put

    P_hat(u)=sum c_m u^m/m!.

For x>=0, the elementary beta integral gives

    Phi_n(P;x)=1/n! integral_0^x (x-u)^n P_hat(u) du.

To check it, integrate each monomial: the coefficient of c_m is x^(n+m+1)/(n+m+1)!. This is a valid real integral representation. Its kernel is nonnegative for 0<=u<=x, but P_hat need not have a fixed sign.

Define the polynomial transform and Volterra operator

    T_n(P;x)=n! sum_(m>=0) [t^m]P(t) x^m/(n+m)!,
    J_n A(x)=x^(-n) integral_0^x u^n A(u) du.

For A(x)=sum a_m x^m,

    J_n A(x)=sum a_m x^(m+1)/(n+m+1).

Thus the apparent singularity at zero is removable. All factorials in T_n have arguments n+m>=n, and all denominators in J_n are positive integers. Coefficient comparison proves

    T_n(tP)=J_n T_n(P).

Set

    A_k=T_n(p_k), r_k=(I-J_n)A_k=T_n((1-t)p_k),
    r_V=T_n((1-t)V).

The same fixed parameter n is used in every A_k and r_k. With

    beta_k=k^2/[4(4k^2-1)],

the monic recurrence gives

    A_(k+1)=(J_n-1/2)A_k+beta_k A_(k-1), k>=1,
    A_0=1, A_1=x/(n+1)-1/2.

Since I-J_n commutes with J_n, the r_k obey the same recurrence, starting from

    r_0=1-x/(n+1),
    r_1=-1/2+3x/[2(n+1)]-x^2/[(n+1)(n+2)].

The exact Christoffel-Darboux identity also gives

    (1-t)V(t)
      =[p_(n+1)(1)p_n(t)-p_n(1)p_(n+1)(t)]/h_n,

hence

    r_V=[p_(n+1)(1)A_n-p_n(1)A_(n+1)]/h_n.

Alternatively, with w_k=p_k(1)/h_k,

    r_V=sum_(k=0)^n w_k r_k.

These are explicit real polynomial constructions for the actual endpoint functions.

## 4. Removing the exponential row with its exact sign

For every polynomial P,

    (D_x-1)Phi_n(P;x)=x^n T_n((1-t)P;x)/n!.

In the full Wronskian replace derivative column j by original column j minus original column j-1 for j=1,...,b, retaining column zero. This simultaneous triangular column transformation has determinant one. The E row becomes (E,0,...,0). Its row position is b in one-based numbering, so expansion along its first entry contributes (-1)^(b+1).

The remaining columns are derivatives of (D_x-1)f_l and (D_x-1)F_V. For any common factor g, Leibniz's rule gives

    Wr(g r_1,...,g r_b)=g^b Wr(r_1,...,r_b).

Apply this with g=x^n/n!. Define

    Z_(n,b)(x)=Wr(r_(n+1),...,r_(n+b-1),r_V)(x).

Then, as an identity of analytic functions,

    Wr(f_1,...,f_(b-1),E,F_V)(x)
      =(-1)^(b+1) exp(x-1) x^(nb) Z_(n,b)(x)/(n!)^b.

In particular,

    D_V=(-1)^(b+1) Z_(n,b)(1)/(n!)^b,
    Y=(-1)^b Z_(n,b)(1)/(n!)^b.

These equalities fix the endpoint interpretation and cofactor orientation completely. They do not identify the full remainder with Z_(n,b).

## 5. A concrete sufficient coefficient lemma

Use the kernel expansion of r_V to write

    P_(n,k)(x)=w_k Wr(r_(n+1),...,r_(n+b-1),r_k)(x),
       0<=k<=n,
    Z_(n,b)=sum_(k=0)^n P_(n,k).

The r_k have degree k+1 and leading coefficient -n!/(n+k+1)!. The degrees in each mixed Wronskian are distinct: n+2,...,n+b,k+1. Consequently

    degree P_(n,k)=L_(n,k)=(b-1)n+b+k.

This is an equality, not merely an upper bound. The leading Wronskian coefficient is the product of the nonzero row-leading coefficients and the Vandermonde of these row degrees.

All coefficients can be generated without an HP nullspace. Put c_(k,m)=[t^m]p_k, with out-of-range coefficients zero, and

    C_(k,m)=n![c_(k,m)-c_(k,m-1)]/(n+m)!.

Thus r_k=sum_m C_(k,m)x^m. For the row-index list

    nu=(n+1,...,n+b-1,k), S=b(b-1)/2,

Cauchy-Binet and the monomial Wronskian formula give

    [x^u]P_(n,k)
      =w_k sum det[C_(nu_i,m_j)] product_(i<j)(m_j-m_i),

where the sum is over

    0<=m_1<...<m_b<=n+b, sum_j m_j=u+S.

The monomial determinant uses (m_i)_j in derivative column j and has Vandermonde product product_(i<j)(m_j-m_i). Distinct nonnegative m_j have sum at least S, so no negative power of x occurs. Every coefficient is rational and explicitly specified.

If P_(n,k)=sum_u q_u x^u has degree L=L_(n,k), its Bernstein coefficients on [0,1] are

    beta_(n,k,j)=sum_(u=0)^j q_u binom(j,u)/binom(L,u),
      0<=j<=L.

They satisfy

    P_(n,k)(x)=sum_(j=0)^L beta_(n,k,j) binom(L,j)x^j(1-x)^(L-j).

Sufficient lemma, not proved uniformly: on an explicitly specified unbounded index set, find sigma_n in {+1,-1} and numbers epsilon_(n,k)>=0 such that

    sigma_n beta_(n,k,j)>=epsilon_(n,k) for every k,j,
    sum_(k=0)^n epsilon_(n,k)>0.

The Bernstein basis is nonnegative on [0,1] and sums to one. Therefore this lemma would imply

    sigma_n Z_(n,b)(x)>=sum_k epsilon_(n,k)>0 on [0,1],
    |D_V|>=sum_k epsilon_(n,k)/(n!)^b>0.

This is a quantitative sufficient criterion in explicit coefficient inequalities, stronger than simply restating D_V!=0.

A concrete unresolved target is the set of all even n>=4 with b=n/2 and sigma_n=(-1)^(b-1). If these inequalities hold there, they imply D_V>0 and Y<0 in the stipulated cofactor orientation. This is a proposed lemma to prove or refute, not an established sign law. The single interval control below supplies no induction or growing-degree theorem.

One modest zero-count fact does follow algebraically: Z_(n,b) is a nonzero polynomial of degree b(n+1), because the k=n summand has strictly larger degree than the other mixed summands. This says that for each fixed n,b its zeros are finite. It does not exclude x=1 as a zero, and is not an unbounded endpoint-nonvanishing result.

## 6. Exact frozen control and its limits

The saved endpoint_wronskian_control.json contains the prior computation at n=4,b=2. It verifies the high-function identity, Volterra recurrence, Christoffel-Darboux transform, Wronskian orientation, and agreement with the existing endpoint certificate. No new control is introduced here.

The high auxiliary polynomial is

    H_5(x)=x^5-25x^4+250x^3-1200x^2+2700x-2220.

The reduced polynomial is

    Z_(4,2)(x)=-(17x^10-950x^9+23190x^8-325440x^7
      +2912400x^6-17394480x^5+70236000x^4-189172800x^3
      +325306800x^2-323676000x+143056800)/14515200.

Its endpoint agrees exactly with

    D_V=135377/103219200,
    Z_(4,2)(1)=-135377/179200.

All 45 stored Bernstein coefficients of the five weighted mixed Wronskians are strictly negative. Therefore this fixed control establishes their common negative sign on the entire closed interval [0,1]. It verifies the sufficient lemma at one existing index only.

The exact weighted endpoint values are:

| k | P_(4,k)(1) | Number of Bernstein coefficients | Stored root count on [0,1] |
|---:|---|---:|---:|
| 0 | -3067/302400 | 7 | 0 |
| 1 | -767/54000 | 8 | 0 |
| 2 | -2461/33075 | 9 | 0 |
| 3 | -871937/4536000 | 10 | 0 |
| 4 | -47193479/101606400 | 11 | 0 |

The saved positive-real-root counts for these five mixed polynomials are respectively 4,3,2,3,2. Those counts are finite diagnostic data; the counterexample below needs only a displayed endpoint value and leading coefficient.

The prior growing-degree audit used the frozen set n=4,6,8,10. Only n=4 was used for this new interval-sign control. No Bernstein-sign result at the other three indices is asserted.

## 7. Genuine obstructions to stronger analytic routes

### 7.1 A positive real measure cannot represent the difference functional

At x=1, the monomial moments of ell_1-ell_0 are

    mu_m=(n+m)/(n+m+1)!.

Their second-order Hankel determinant satisfies exactly

    ((n+2)!)^2 (mu_0 mu_2-mu_1^2)
      =n(n+2)^2/(n+3)-(n+1)^2
      =-(n^2+3n+3)/(n+3)<0.

For a nonnegative real measure with these moments, the matrix of moments of 1 and t would be positive semidefinite, forcing this determinant to be nonnegative. Thus such a measure representation is impossible. This is a proved obstruction, not a failed numerical search. The valid Volterra integral in Section 3 does not contradict it: that integral acts on transformed polynomial data and does not provide the prohibited positive moment representation.

### 7.2 Common sign on the whole positive half-line fails

Every r_k has a negative leading coefficient. In the ordered mixed Wronskian, the low degree k+1 is last, giving b-1 negative factors in the degree Vandermonde. The product of b negative leading coefficients contributes (-1)^b. Thus the unweighted mixed Wronskian always has negative leading coefficient.

Since p_k(1)>0 and sign(h_k)=(-1)^k, multiplication by w_k gives

    sign(leading coefficient of P_(n,k))=(-1)^(k+1).

Adjacent k have opposite signs for sufficiently large positive x. A common-sign assertion for all these actual polynomials on the whole positive half-line is therefore false.

There is also a concrete fixed-control counterexample to a zero-free positive half-line. At n=4,k=1,

    P_(4,1)(1)=-767/54000<0,
    leading coefficient of P_(4,1)=1/378000>0.

Hence P_(4,1) has a real zero strictly greater than one by the intermediate value theorem. This is a genuine counterexample to that stronger sign/zero-free claim. It is not a counterexample to endpoint nonvanishing or to the interval [0,1] coefficient lemma. This global-sign sub-branch is closed.

### 7.3 The signed Volterra recurrence does not preserve the positive cone

After alternating signs in the recurrence, its principal operator becomes 1/2-J_n. It does not preserve nonnegative functions on [0,1]. Take h(x)=1-x>=0. Then

    [(1/2-J_n)h](1)=-1/[(n+1)(n+2)]<0.

This is an exact counterexample to an unrestricted positivity-preservation argument. It does not assert that the actual recurrence polynomials behave like arbitrary nonnegative functions. A successful recurrence proof would need additional inequalities specific to those polynomials or their minors; no controlled-pivot theorem has been established here.

No Chebyshev property or disconjugacy theorem has been assumed. Positivity of the auxiliary Gaussian integral from the earlier task is irrelevant to these sign questions.

## 8. Updated obstruction to the chosen shrinking criterion

Read: ../GROWING_BOUND_OBSTRUCTION_DRAFT.md. Its Section 1 elementary comparison is correct for the explicit choices in GAUSSIAN_VANDERMONDE_BOUND.md.

To avoid confusing the special-row scale with A_k(x), call that scale a_n=(20/9)^(n+1). The chosen bounds are

    M_V=a_n (n+1)^2 64^n/2,
    M_W=a_n [20/19+2(n+1)^2 64^n]
       =4M_V+(20/19)a_n>4M_V.

The remaining positive factors in B_V and B_W are identical, so

    B_W/B_V=M_W/M_V>4.

On the nonzero-endpoint domain, |D_V|<=B_V and the actual reduced denominator is an integer q>=1. Thus

    q(B_W+B_T)/|D_V|>=q B_W/B_V>4q>=4.

The earlier sufficient shrinking expression cannot tend to zero for these chosen bounds. Neither a better endpoint nonvanishing proof nor a larger endpoint gcd can overcome this comparison. This deduction does not require the proposed integer clearer or any content estimate. The separate clearing and divisibility claims in the obstruction draft are not independently certified by this note.

A lower bound on this upper-bound expression is not a lower bound on the actual primitive form. Therefore the comparison does not prove failure of the actual growing-degree construction. It does require abandoning the chosen absolute-bound criterion as a viable shrinking target.

For clarity, the actual projection remainder remains

    W(t)=1/(1-t)-H(t),
    H(t)=sum_(k=0)^n L(p_k/(1-t))p_k(t)/h_k,
    R(1)=ell_B(W)=D_W+T.

When D_V!=0, the exact primitive identity is

    |L_integer|=q |D_W+T|/|D_V|.

Endpoint nonvanishing supplies the domain for this identity and normality of the cofactor construction. It neither establishes full-remainder nonvanishing nor controls the ratio. A shrinking argument now needs genuinely sharper information about the actual projection remainder or cancellation between its two complete determinants, together with actual arithmetic normalization.

## 9. Outcome and the most useful next lemma

Proved: the Phi identity, high-function derivative formula, exact row-oriented Wronskian representation, polynomial reduction with its cofactor sign, real Volterra representation and recurrence, explicit mixed-minor coefficient formula, and the implication of the Bernstein coefficient lemma.

Finite exact evidence: the saved n=4 control verifies the identities and all 45 strict negative Bernstein coefficients. It proves an interval sign statement only at that index.

Genuine counterexamples/obstructions: the negative moment Hankel determinant, the positive-half-line sign failure of actual mixed Wronskians, and the failure of 1/2-J_n to preserve nonnegative functions. None is a counterexample to the original endpoint at x=1.

Unproved: the coefficient inequalities on an unbounded set, endpoint nonvanishing for b=floor(n/2) on an explicitly described unbounded set, and full-remainder nonvanishing. No unbounded endpoint-nonvanishing theorem is claimed.

The most useful next lemma for this branch is the explicit uniform Bernstein-sign inequality in Section 5 on even n>=4, preferably with a quantitative positive sum of coefficient margins. Its inputs are recurrence-defined rational coefficients and finite Cauchy-Binet sums, so it is independently checkable and can be attacked symbolically without a degree sweep. A proof would give an actual endpoint lower bound and normality on that set. If a coefficient obstruction is found, it should be recorded as a failure of this sufficient condition rather than of endpoint nonvanishing itself.

For an eventual shrinking result, that endpoint lemma must be paired with new control of the actual projection remainder; the superseded bound ratio cannot be repaired by endpoint arithmetic alone. No further Gaussian optimization is proposed.

Related saved files: endpoint_wronskian_control.json; GROWING_DEGREE_INDEPENDENT_REVIEW.md; growing_degree_independent_certificate.json; GAUSSIAN_VANDERMONDE_BOUND.md; ENDPOINT_NONVANISHING_REPORT.md.
