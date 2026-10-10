> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The even endpoint inverse-corner limit and its exact error constant

Date: 2026-09-13. Original bounded continuation by audit_results.
Independent review: PASS by audit_sources, including an identical interval postprocessing rerun; see raw_even_inverse_corner_independent_review.md.

This identifies the actual even inverse-corner limit using the same fixed half-line exponential operator as in the independently proved odd limit. The even geometry has one component of degree m and another of degree m-1; it is not the full two-component odd space.

The exact limit is a positive scalar g_+. The already certified odd witness vectors give, without a new solve,

    0.91149<g_+<0.91150.                                  (1)

Consequently the even exponential-error comparison sharpens to the limit

    lim_(n even) n beta^(-n) Re_n(1)/[t^n]V_n
       =sqrt(3e)/(4g_+) in (0.783,0.784),
    beta=3sqrt(3)/4.                                     (2)

No new canonical degree, quadrature, or linear system was solved.

## 1. Actual even positive-symbol normalization

Let n=2m, m>=1, and retain

    A_ij=[z^(n+i-j)]e^z(1+z^2)^n,       0<=i,j<=n,
    c_m=((2m)!)^2/[m!(3m)!],
    g_m=(A^(-1))_00/c_m.

The positive circle weight is |1+z^2|^(2m). Writing

    p(z)=u(t)+z h(t),       t=z^2,

gives degree u<=m and degree h<=m-1. Under this parity decomposition the normalized matrix is the compression of

    F(t)=exp[0 t;1 0]
         =[c(t) t s(t);s(t) c(t)]

to those two polynomial spaces in the common scalar weight |1+t|^(2m). There is no rational odd factor a0 in this even symbol.

The endpoint coordinate acts on u(0) alone. Its normalized Riesz vector gives g_m as the corresponding inverse quadratic form. In particular the known even bounds make g_m real and uniformly positive.

## 2. The common Cayley space has one exact codimension-one constraint

Use t=(1+iy)/(1-iy) and a common denominator exponent m in both components:

    U(y)=(1-iy)^m u(t),
    H(y)=(1-iy)^m h(t).

The scalar measure is a positive constant times

    (1+y^2)^(-beta_m)dy,       beta_m=2m+1.                (3)

The first component U ranges over all polynomials of degree at most m. The second component has the exact form

    H=(1-iy)P,       degree P<=m-1.

Equivalently H has degree at most m and H(-i)=0. Thus, inside the common two-component degree-m polynomial space, the actual even space is

    S_m=w_m-perpendicular,

where w_m is the unit Riesz vector for evaluation at -i in the second component. This is an orthogonal codimension-one condition in the positive metric. Replacing it by deletion of a top monomial would be incorrect.

Let v_m be the unit Riesz vector for evaluation at i in the first component. Evaluation at the original t=0 equals evaluation at y=i times 2^(-m); this positive factor cancels when the vector is normalized. Hence v_m is exactly the normalized original endpoint vector and v_m is orthogonal to w_m.

If E_m is the full common degree-m compression of F(t(y)) and Pi_m=I-w_mw_m*, then

    g_m=<v_m,(Pi_m E_m Pi_m|_(w_m-perp))^(-1)v_m>.        (4)

This is the precise coordinate interface to the actual even corner.

## 3. Right limit and the two endpoint vectors

Let q_j^(m) be the scalar orthonormal polynomials for (3), with positive leading coefficient. Their zero-diagonal Jacobi recurrence has

    a_(j,m)^2=
       j(2beta_m-j)/[(2beta_m-2j)^2-1].

For each fixed k, a_(m+k,m)->sqrt(3)/2. The fixed-degree moment approximation argument in raw_odd_boundary_operator_limit.md applies verbatim to beta_m=2m+1: each required fixed neighborhood and moment exists for sufficiently large m, and its limit is the same bilateral constant Jacobi operator J. In particular

    E_m -> E_+:=P_+F(J)P_+

strongly after reversing the polynomial indices and extending by identities outside the finite space.

Rodrigues gives the same exact evaluation ratio with the changed beta:

    q_j(i)/q_(j-1)(i)
       =i sqrt[(2beta_m-j)(2beta_m-2j-1)/
                    (j(2beta_m-2j+1))].                  (5)

For j<=m its magnitude is at least sqrt(2), since both positive factors decrease with j and at j=m their product is

    (3m+2)(2m+1)/(m(2m+3))>2.

This supplies a uniform geometric tail. For each fixed distance from the top, (5) has limiting magnitude sqrt(3). After harmless independent phases for the two unit vectors, their norm limits are therefore

    v_m -> v,       v_r=sqrt(2/3)(i/sqrt(3))^r [1;0],
    w_m -> w,       w_r=sqrt(2/3)(-i/sqrt(3))^r [0;1].
                                                               (6)

The phase for v_m can be i^m, and that for w_m can be (-i)^m. Neither changes (4): the first cancels in the quadratic form and the second leaves its orthogonal projection unchanged.

The two geometric series in (6) are unit vectors and are orthogonal because they occupy different components.

## 4. Coercivity proves inverse convergence without a new exceptional gate

Every E_m and E_+ has Hermitian part at least c_*I, with c_*=e^(-1)cos(1)>0, and norm at most e. Form the full-space extension

    B_m=Pi_m E_m Pi_m+w_mw_m*.

It is uniformly strictly accretive, as is its adjoint, and therefore has a uniformly bounded inverse. Since w_m->w in norm, Pi_m->Pi=I-ww* in operator norm. Thus B_m converges strongly to

    B_+=Pi E_+ Pi+ww*.

The limit is strictly accretive and invertible. The inverse identity with the uniform bound proves B_m^(-1)->B_+^(-1) strongly. Equation (4) and (6) give

    g_m -> g_+:=<v,B_+^(-1)v>.                            (7)

Its real part is positive by accretivity; its reality also follows from the exact real even corners. Hence g_+>0. This positivity does not require the numerical certificate.

Equivalently, the inverse-compression identity gives the explicit scalar

    g_+=v*E_+^(-1)v
       -(v*E_+^(-1)w)(w*E_+^(-1)v)/(w*E_+^(-1)w).        (8)

The denominator has positive real part and cannot vanish. Formula (8) uses the same fixed E_+ as the odd certificate, retaining the missing second-component constraint.

## 5. The certified odd witnesses already give all four scalar entries

Let Y=P_+JP_+ and let e_0 denote the first scalar position. Direct substitution in the half-line recurrence proves

    (I+/-iY)^(-1)e_0
       =(2/3)(-/+i/sqrt(3))^r.                           (9)

At r=0 the factor 2/3 follows from 1+1/2=3/2; at r>=1 the geometric sequence satisfies the homogeneous equation. The vector is square summable, and invertibility makes it the unique solution.

The same A0_+ and U_+=(sqrt(3)/4)e_0 used in the odd certificate consequently satisfy

    A0_+^(-1)U_+e_1=w/sqrt(2),
    A0_+^(-1)U_+e_2=v/sqrt(2).                            (10)

Thus its first two exact solved vectors are

    f_0=Q_+U_+e_1=E_+^(-1)w/sqrt(2),
    f_1=Q_+U_+e_2=E_+^(-1)v/sqrt(2).

Equation (8) becomes

    g_+=sqrt(2)[v*f_1-(v*f_0)(w*f_1)/(w*f_0)].             (11)

The unchanged exact dyadic approximate vectors from
raw_odd_limit_certificate_vectors.json have independently certified errors
less than 3.508e-13 and 2.827e-12. Pairing them against the unit vectors v,w therefore has errors below the same numbers. No tail is omitted: the approximants have finite support and the error is measured against the full true solved vectors.

The separate outward-interval checker
check_raw_even_limit_from_odd_witnesses.py uses the conservative bounds
4e-13 and 3e-12 and evaluates (11). Its output
raw_even_limit_from_odd_witnesses.json is PASS and implies (1). The narrower enclosure is approximately

    g_+=0.911492005669...,
    1/g_+=1.09710232649....

These decimals are descriptive; (1) is the asserted rational enclosure. The checker makes no new linear solve, quadrature, or canonical-degree construction.

## 6. Exact endpoint and exponential-error limits

The actual joint equation gives

    (A^(-1))_00=(2n)![t^n]V_n/(n!V_n(1)).

Using the exact c_m and n=2m therefore yields

    V_n(1)/[t^n]V_n = B_m/g_m,
    B_m=(4m)!m!(3m)!/((2m)!)^3.                           (12)

Hence its previous two-sided comparison improves to

    V_n(1)/([t^n]V_n B_m) ->1/g_+>0.                      (13)

The independently proved even flatness/error theorem already gives

    Re_n(1)=sqrt(e)V_n(1)n!/(2n+1)!(1+O(1/n)).

The exact remaining factorial ratio is

    B_m n!/(2n+1)!
       =m!(3m)!/[(2m)!^2(4m+1)]
       ~sqrt(3)/(4n) beta^n.

Equations (7) and (12) prove (2). The interval checker also verifies its displayed enclosure (0.783,0.784); its numerical center is approximately 0.7832402782.

The even and odd leading-coefficient-normalized exponential errors now have exact positive limits after multiplication by n beta^(-n):

    even: sqrt(3e)/(4g_+);
    odd:  -(3/4)sqrt(e)s_infty.

These two constants are different. Both parities retain the same exponential rate beta.

## 7. Scope

The new result is the actual even inverse-corner limit, with its exact positive boundary formula and a certified enclosure reusing old witnesses. It strengthens comparison to a genuine asymptotic equivalence.

It does not estimate the signed arctangent contribution, the endpoint gcd, or a combined primitive irrationality form. No orthogonality has been transferred through the Borel map and no degree scan has been performed.
