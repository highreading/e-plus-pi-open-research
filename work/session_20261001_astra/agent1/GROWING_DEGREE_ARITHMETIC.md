> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact arithmetic after high-row cancellation for 1<=b<=n

Status: paper proof with successful formal identity checks; independent review pending. This applies in particular to b=floor(n/2), n>=2. No fixed-b asymptotic or growing-degree nonvanishing theorem is assumed.

## 1. Actual reduced system and Rodrigues row factors

Use Agent 2's reduced system M=[U;e+t], where e=(1,...,1), columns j=0,...,b, high rows l=1,...,b-1, and

    ell_j(y^m)=1/(n+m+1-j)!,
    U_lj=ell_j(p_(n+l)),
    t_j=ell_j(K_n(y,1)).

Here p_k is monic. Distinguish the row t from the integer tau=n+1 below. The endpoint cofactor convention is Y=det[U;e+t;e], X=det[U;e+t;x], with x_j the reconstructed elementary A endpoint. These expressions include the actual numerator.

Let L_k=2^k binom(2k,k) p_k and

    H_k(x)=k![z^k] exp(xz)(1-z+z^2/2)^k,
    E_(k,r)=(d/dx)^r[x^k H_k(x)] at x=1,
    f_k=2^k/(k!)^2.

Rodrigues gives

    sum_m [y^m]L_k(y) x^(k+m)/(k+m)! = f_k x^k H_k(x).

Taking r=l+j-1 derivatives with k=n+l proves exactly

    ell_j(L_(n+l))=f_(n+l) E_(n+l,l+j-1).

All resulting factorial arguments are positive: their minimum is n+1-b>=1. No negative-factorial convention is needed. Since the leading coefficient of L_k is 2^k(2k)!/(k!)^2, the monic formula simplifies to

    ell_j(p_(n+l))=E_(n+l,l+j-1)/(2n+2l)!.

Set R_lj=E_(n+l,l+j-1) and rho=product_(l=1)^(b-1) 1/(2n+2l)!. Thus every endpoint determinant has the same high-row factor rho. In the integer-L convention the common factor is instead product f_(n+l). Neither factor survives in X/Y.

## 2. Integrality and additional row divisibility

Write a_s(k)=[z^s](1-z+z^2/2)^k. The coefficient of x^(k-s) in H_k is (k)_s a_s(k). A term containing c quadratic selections has denominator dividing 2^c and s>=2c. A consecutive product of length s contains at least floor(s/2)>=c even factors. Thus H_k belongs to Z[x], and all E_(k,r) are integers.

There is a further useful exact divisibility:

    k divides E_(k,r) for every k>=1 and r>=1.

Indeed H'_k/k has coefficient (k-1)_s a_s(k) at x^(k-s-1), for 0<=s<=k-1. The same even-factor argument proves this coefficient integral. Hence H'_k/k is an integer polynomial, as are all its derivatives. In the Leibniz expansion of (x^k H_k)^(r), the term with no derivative on x^k is divisible by k; every other nonzero term contains (k)_a for some a>=1 and is likewise divisible by k. This proves the claim without dividing modulo a prime.

Consequently every row l>=2 of R has the forced common divisor n+l, since its smallest derivative order is l-1>=1. Row l=1 includes order zero and is not covered by that assertion.

For an exact content removal define

    c_l=gcd_j |R_lj|.

If any c_l=0, that row is zero and all endpoint cofactors vanish. The quotient domain is then empty. Otherwise set R0_lj=R_lj/c_l and Crows=product c_l. For b=1 these are empty products and an empty high block.

## 3. Elementary endpoints for every j<=b<=n

Put P=L_n, Uadj=L_(n+1), A=P(1), B=Uadj(1), and

    w_P=calL((P(y)-A)/(y-1)),
    w_U=calL((Uadj(y)-B)/(y-1)),
    G=A w_U-B w_P=(-1)^n 2^(2n+3)/(n+1).

These second-kind quantities and the Wronskian are exactly those of the September 13 endpoint source. Define the rational partial-exponential rows

    T_j(Q)=sum_m [y^m]Q Epartial_(n+m-j),
    Epartial_d=sum_(a=0)^d 1/a!.

The smallest partial-sum index is n-j>=0 throughout the present domain. Absolutely convergent factorial sums give, for every polynomial Q,

    ell_j(Q/(1-y))=exp(1) Q(1)-T_j(Q).

To verify, each monomial y^m contributes the factorial tail starting at n+m+1-j. Thus this formula holds for every permitted j, independently of b.

Let D(y)=(w_U P(y)-w_P Uadj(y))/G, so D(1)=1. The Christoffel--Darboux formula is

    K_n(1,y)=(B P(y)-A Uadj(y))/(G(1-y)).

Applying the factorial identity cancels the exp(1) terms and gives

    t_j=(A T_j(Uadj)-B T_j(P))/G.

The projection remainder identity used in the source is polynomial-kernel data depending only on n, not on the number of elementary columns. Taylor reconstruction gives

    x_j=ell_j((D-1)/(1-y))-Epartial_(n-j)
       =(w_P T_j(Uadj)-w_U T_j(P))/G.

For clarity, the first equality also follows by writing the projection remainder as D/(1-y)-pi K_n(1,y). Subtracting the elementary contribution exp(1)+pi t_j leaves the displayed rational x_j. Thus it is the reconstructed A endpoint, not merely a factorial tail. All index and convergence requirements remain valid at j=n. These two endpoint formulas therefore extend to every 0<=j<=b<=n.

## 4. Integer derivative minors and their content

For vectors v,w of length b+1 define

    B0(v,w)=det[R0;v;w].

It is convenient to specify this entirely through integer high-row minors. For 0<=i<j<=b, let

    m_ij=(-1)^(i+j+1) det(R0 with columns i,j deleted).

The remaining columns retain their natural order. Then

    B0(v,w)=sum_(i<j) m_ij(v_i w_j-v_j w_i).

For b=1 the empty minor is 1, so m_01=1. Set mu=gcd_(i<j)|m_ij|. If mu=0 the high block has deficient row rank and both endpoint determinants vanish. Otherwise put mbar_ij=m_ij/mu and

    Bbar(v,w)=sum_(i<j) mbar_ij(v_i w_j-v_j w_i).

This removes the full maximal-minor content before endpoint contraction, not merely a selection of individual row divisors. Exactly,

    det[U;v;w]=rho Crows mu Bbar(v,w).

This identity is valid for arbitrary rational endpoint rows. Its factors therefore cancel in every ratio of endpoint determinants.

## 5. Adjacent rows and a complete three-integer contraction

Put tau=n+1, f=f_n, and define integer rows indexed by j=0,...,b:

    p_0=u_0=0,
    p_j=sum_(i=1)^j E_(n,i-1),
    u_j=sum_(i=1)^j E_(n+1,i)/(n+1).

The last row is integral by Section 2; its definition involves exact integer division, not a local inverse. The elementary differences satisfy

    T_(i-1)(Q)-T_i(Q)=ell_i(Q).

Rodrigues consequently gives, writing TP=T_0(P), TU=T_0(Uadj),

    T(P)=TP e-f p,
    T(Uadj)=TU e-(2f/tau) u.

Define three integer contractions of the primitive derivative-minor vector:

    sigma=-Bbar(e,u),
    c=-Bbar(e,p),
    kappa=Bbar(u,p).

The letter c here is a scalar contraction, not a row content c_l. Let

    D=tau B c-2A sigma,
    Q=2w_P sigma-tau w_U c,
    V=sigma Acal_n-c Bcal_n-kappa.

Acal_n and Bcal_n are exactly the earlier adjacent Rodrigues contractions, with TP=f Acal_n and TU=2f Bcal_n/tau. In particular these contractions retain their partial-exponential sums. They belong to Z[1/2].

Bilinearity and the Wronskian give the exact endpoints

    Y=rho Crows mu * f/(tau G) * D,
    X=rho Crows mu * f/(tau G) * (Q+2f V).

One way to check the signs is to use Bbar(e,u)=-sigma, Bbar(e,p)=-c, Bbar(u,p)=kappa. The coefficient determinant expressing (t,x) in the two T rows is -1/G. Expansion then gives

    Q+2f V
      =2(w_P+TP)sigma-tau(w_U+TU)c-2f kappa.

Thus the quotient, on D!=0, is exactly

    X/Y=(Q+2^(n+1)V/(n!)^2)/D.

The high-row scalars rho, individual row contents, maximal-minor content, and the additional common endpoint scalar f/(tau G) have all cancelled explicitly. The division by tau in the derivative row u is justified by an exact identity. None of these cancelled factors is a lower bound for the reduced denominator.

There is one further computable common factor: d=gcd(|sigma|,|c|,|kappa|). On D!=0 this is positive. Replace the three contractions by sigma*=sigma/d, c*=c/d, kappa*=kappa/d, and define D*,Q*,V* by the same displayed formulas. Both complete endpoint expressions acquire the common factor d, which cancels over Q. All subsequent formulas use these starred quantities. This cancellation does not discard the partial-exponential or second-kind terms.

## 6. Exact final gcd and unresolved arithmetic

Choose, for example, the deliberately conservative positive integer

    Lambda=2^(n+1)(n+2)!(2n+1)!(n!)^2.

Then N=Lambda(Q*+2f V*) and Z=Lambda D* are integers. To see this directly without a claim of minimality, use

    Q*+2f V*
      =2(w_P+TP)sigma*-tau(w_U+TU)c*-2f kappa*.

The T denominators divide (2n+1)!. The moment denominators through degree n divide 2^n(n+1)!, so the stated Lambda clears both w values. It also clears f. Every remaining coefficient is an integer. Therefore, on D*!=0,

    q=|Z|/gcd(|Z|,|N|).

This is the actual reduced endpoint denominator. It includes full coefficient-content cancellation automatically because X/Y is unchanged by any scale of the complete triple. The final endpoint gcd is not identified with high-row content or discarded.

Equivalently, at every prime p, with v_p(0)=infinity,

    v_p(q)=v_p(Z)-min(v_p(Z),v_p(N)).

If N=0 this gives q=1. If the numerator is nonzero, the equivalent rational valuation formula is

    v_p(q)=max(0,v_p(D*)-v_p(Q*+2f V*)).

The precise unresolved content is gcd(|Lambda D*|,|Lambda(Q*+2f V*)|), after all the proved cancellations above. A smaller rational clearer could change the two integers but not their reduced quotient or q. Naming Lambda alone does not solve this content problem.

For an odd p a useful equivalent gate, still containing all numerator cancellation, is obtained by setting

    F=v_p(n!),
    R*=V*+(n!)^2 Q*/2^(n+1).

For R*!=0,

    v_p(q)=max(0,2F+v_p(D*)-v_p(R*)).

Since sigma*,c* are integers, the moment proof gives v_p(Q*)>=-floor(log_p(n+1)). If a proved bound places v_p(V*) strictly below 2F-floor(log_p(n+1)), then v_p(R*)=v_p(V*). No such bound or seed transfer for growing-size minors is asserted here. Near or above that threshold, the full R* must be retained.

The remaining tasks are both endpoint nonvanishing D*!=0 and quantitative control of this final gcd or its valuation gate. For b=floor(n/2), no fixed-b nonvanishing or asymptotic constant supplies either assertion. Deficient high-row rank, D*=0, and a zero complete numerator are distinct cases.

## 7. Compatibility with the completed b=2 normalization

To compare conventions, temporarily omit row/minor/scalar content divisions. For b=2 the integer high row is

    (a,tau k,tau ell),

where a=H_(n+1), J_(n+1)=tau k, K_(n+1)=tau ell. The two integer cumulative rows are

    p=(0,h,h+J_n), u=(0,k,k+ell).

Direct determinants give

    sigma=tau k^2-a ell,
    c=(tau k-a)J_n-tau(ell-k)h=C,
    kappa=a(kJ_n-ell h)=a omega.

Consequently V=sigma Acal_n-C Bcal_n-a omega is precisely the completed b=2 Vtilde. The original b=2 scalar is V_original=tau Vtilde, and its original Dcal and Xcal are tau times the present D and complete numerator. Thus the earlier n+1 cancellation is recovered exactly, including the second-kind terms and a omega contribution. Additional content divisions in Sections 4–5 simply remove further common scales from these same expressions.

For b=1 the high block is empty. The convention gives sigma=-k, c=-H_n, kappa=0; both numerator and denominator differ by the same sign from the familiar b=1 formula. The quotient agrees. These are formal compatibility checks, not fresh degree computations.

## 8. Evidence and scope

check_growing_degree_arithmetic.py completed successfully with exit code 0 and sandboxed=true. growing_degree_arithmetic_certificate.json records PASS_FORMAL_IDENTITIES for 18 symbolic checks: Rodrigues coefficients and indices, the monic row scalar, endpoint determinant signs with the Wronskian, complete contractions, content factors, signed minors, and b=1/b=2 compatibility. There were no new numerical degree evaluations, seed scans, or prime computations.

The finite symbolic checks supplement the paper arguments for the unrestricted derivative divisibility, elementary endpoint extension, and exact gcd formula. They do not establish growing-degree rank, endpoint nonvanishing, or any growth estimate. Independent review remains pending.

Sources used: agent2/PROOF_DRAFT.md for the actual reduced system; the previously read September 13 contiguous endpoint source and independent review for Rodrigues, projection, and Wronskian identities; the completed common-factor and normalized b=2 records for compatibility. No shared or historical record was modified. Completed seeds and the correction remain preserved.
