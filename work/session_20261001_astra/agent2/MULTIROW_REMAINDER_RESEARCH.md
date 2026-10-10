> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Normalized multi-row subtraction and a complete quadratic remainder bound

Status: new author paper deductions, not an independent review. The earlier TWO_DIMENSIONAL_REMAINDER_RESEARCH.md and its reported factor 101/[9(n+3-b)] are preserved. That factor is not a premise of the argument below. No controls, approximation systems, or numerical scans were recomputed.

The new scheme trades two additional available high rows for each additional guaranteed factorial cancellation. Its subtraction coefficients have an explicit recurrence and an exponential upper bound, but its combined residual numerator has exactly the norm of one reference polynomial. After including the changing reference polynomial and its endpoint normalization, there is a net improvement of the entire positive full-remainder majorant. The endpoint inverse remains a separate, explicitly identified conditioning problem.

## 1. Domain and exact setup

Let n>=b>=3 be integers. The relaxed balanced construction has caps (n,b,n), contact order M=2n+b, and B(1)=C(1). Write

    B(z)=sum_(j=0)^b x_j z^j,
    Y=B(1), X=A(1),
    R(z)=A(z)+B(z)exp(z)+C(z)F(z),
    F(z)=4 arctan(z/(2-z)).

Use the established monic polynomials and functional

    p_l(t)=i^l LegendreP_l(-i(2t-1))/binom(2l,l),
    L(P)=integral_-1^1 P((1+iu)/2) du,
    h_l=L(p_l^2)=2(-1)^l/[(2l+1)binom(2l,l)^2],
    ell_j(t^a)=1/(n+a+1-j)!,
    ell_x=sum_j x_j ell_j.

The recurrence and endpoint values used below are

    p_(l+1)=(t-1/2)p_l+beta_l p_(l-1),
    beta_l=l^2/[4(4l^2-1)],
    A_l=p_l(1)>0,
    1/2<=A_(l+1)/A_l<=2/3,
    0<beta_l<=1/12  for l>=1.

All factorial arguments are positive. Factorial-weighted Taylor series define ell_j on the rational functions below and converge absolutely; these functions need not be regular at t=1.

The actual retained high constraints are

    ell_x(p_(n+l))=0, 1<=l<=b-2.                         (1)

The endpoint matching row is ell_x(V_n)=-Y, where

    V_d=sum_(l=0)^d A_l p_l/h_l.

As in the relaxed projection reconstruction,

    Cstar(t)=t^n C(1/t)=-sum_(l=0)^n ell_x(p_l)p_l/h_l,
    A=-[B exp+C F]_(degree<=n).

These formulas identify x with a solution triple. They follow from the first n+1 moment equations and do not require normality.

The subtraction results hold throughout the stated domain. For a rational endpoint inverse, additionally assume that the actual normality matrix J in Section 8 is nonsingular. The intended slow-growth setting is

    n>=512 b^4 log n,                                     (2)

with natural logarithm and n>1, subject to all hypotheses of Child 3's provisional normality statement. This note does not establish or independently accept that normality theorem. Every use of its consequence is explicitly conditional on J being nonsingular.

## 2. The complete remainder and both errors

Put

    v_l=L(p_l/(1-t)),
    H_d=sum_(l=0)^d v_l p_l/h_l,
    W_d=1/(1-t)-H_d.

The complete Taylor tails give R(1)=ell_x(W_n). Constraint (1) implies, for n<=d<=n+b-2,

    ell_x(W_d)=R(1), ell_x(V_d)=-Y.

The Christoffel-Darboux identities are

    V_d=[A_(d+1)p_d-A_d p_(d+1)]/[h_d(1-t)],
    W_d=[v_d p_(d+1)-v_(d+1)p_d]/[h_d(1-t)],
    A_(d+1)v_d-A_d v_(d+1)=h_d.

Define a_k(x)=ell_x(p_k/(1-t)). Eliminating a_(k-1) from these two identities gives the complete linear-form identity

    R(1)=a_k(x)/A_k+(v_k/A_k)Y,
    n+1<=k<=n+b-1.                                      (3)

For clarity, the eliminated equations are

    A_k a_(k-1)-A_(k-1)a_k=-h_(k-1)Y,
    R(1)=[v_(k-1)a_k-v_k a_(k-1)]/h_(k-1).

Thus no one-dimensional cofactor formula is being imported into a space of dimension two.

For a polynomial P=sum_a P_a t^a, define the rational row

    T_j(P)=sum_a P_a sum_(r=0)^(n+a-j) 1/r!.

The full factorial tail, with its exact starting index, gives

    a_k(x)/A_k=eY-T(p_k) dot x/A_k.

Also set

    w_k=L((p_k-A_k)/(t-1)), r_(pi,k)=w_k/A_k.

Then w_k and r_(pi,k) are rational and v_k/A_k=pi-r_(pi,k). Consequently (3) retains the two complete errors:

    R(1)=[eY-T(p_k) dot x/A_k]+[pi-r_(pi,k)]Y.           (4)

Their sum equals X+Y(e+pi). When Y!=0, write E_k=a_k/(A_k Y) and epsilon_k=|v_k|/A_k. The established reference identity

    v_k A_k/h_k=theta_k, 1<=theta_k<=2,

gives

    R(1)/Y=E_k+(-1)^k epsilon_k,
    E_k=R(1)/Y-(-1)^k epsilon_k.                         (5)

Small full remainders can therefore involve cancellation. None of the bounds below proves separate full-remainder nonvanishing or asserts that the two errors have the same sign.

## 3. A symmetric multi-row subtraction

Choose an integer m satisfying

    1<=m<=floor((b-1)/2), and put k=n+m.                  (6)

For this fixed k, define successive residual functions

    F_r(t)=t^r p_k(t)/(1-t), 0<=r<=m.

Their exact difference is

    F_r-F_(r+1)=t^r p_k.

Multiplication by t in the orthogonal basis obeys

    t p_l=p_(l+1)+(1/2)p_l-beta_l p_(l-1).              (7)

Thus t^r p_k belongs to the span of p_(k-r),...,p_(k+r). For 0<=r<m these indices lie between n+1 and n+2m-1, and

    n+2m-1<=n+b-2.

Every polynomial subtracted is therefore in the actual annihilated high-row span. In particular,

    ell_x(F_0)=ell_x(F_1)=...=ell_x(F_m).

Equivalently, with

    Q_m(t)=p_k(t)(1+t+...+t^(m-1)),

one has the exact polynomial and functional identities

    p_k-(1-t)Q_m=t^m p_k,
    p_k/(1-t)-Q_m=t^m p_k/(1-t),
    a_k(x)=ell_x(t^m p_k/(1-t)).                       (8)

The scheme uses 2m-1 available consecutive high rows to guarantee m subtractions. It does not claim that the first m high rows alone suffice. It is a controlled alternative to growing jet interpolation, rather than an iteration of the earlier two-row coefficients. For b>=5 it permits m>=2. At the largest allowed m, at most one of the b-2 retained high rows is unused.

The change k=n+m is deliberate: centering the multiplication band at k prevents a low, unannihilated row from appearing before the m-th subtraction. Keeping k=n+1 while iterating (7) would immediately introduce p_n and would not justify this argument.

## 4. Explicit coefficients and their entire norm budget

Write

    t^r p_k=sum_l c_(r,l) p_l.

The rational coefficients are specified by the finite recurrence

    c_(0,l)=1 if l=k, otherwise 0,
    c_(r+1,l)=c_(r,l-1)+(1/2)c_(r,l)
                         -beta_(l+1)c_(r,l+1).          (9)

All omitted indices have coefficient zero. Only the finite band k-r<=l<=k+r is used. The subtraction coefficient of p_l in Q_m is

    alpha_(m,l)=sum_(r=0)^(m-1)c_(r,l).

The three transition weights in (7) have total absolute value at most 19/12. Therefore

    sum_l |c_(r,l)|<=(19/12)^r,
    sum_l |alpha_(m,l)|
        <=(12/7)[(19/12)^m-1].                         (10)

These estimates display the high-basis coefficient amplification explicitly. There is no inverse jet matrix or unbounded pivot denominator hidden in the definition of alpha.

Let L_l=||p_l||_1 be the sum of the absolute ordinary coefficients. The coefficients of (-1)^l p_l(-t) are nonnegative: its recurrence is

    f_(l+1)=(t+1/2)f_l+beta_l f_(l-1),
    f_0=1, f_1=t+1/2.

Hence

    L_(l+1)=(3/2)L_l+beta_l L_(l-1),
    3/2<=L_(l+1)/L_l<=14/9.                            (11)

The upper bound follows from beta_l<=1/12 and L_l/L_(l-1)>=3/2; the initial ratio is 3/2.

The combined subtraction and exact residual satisfy the stronger ordinary-coefficient statements

    ||Q_m||_1<=m L_k,
    ||p_k-(1-t)Q_m||_1=||t^m p_k||_1=L_k.              (12)

Thus (10) is not multiplied into the residual estimate. This is justified by the exact combined identity (8), before applying any absolute values. Bounding separately all high-basis summands would discard a proved algebraic cancellation. Equations (10)-(12) account for both the basis coefficients and the actual residual norm.

The change of reference degree also has an explicit cost:

    L_(n+m)/L_(n+1)<=(14/9)^(m-1),
    [L_(n+m)/A_(n+m)]/[L_(n+1)/A_(n+1)]
        <=(28/9)^(m-1).                               (13)

The factorial gain in Section 6 is compared only after this endpoint normalization cost is included.

## 5. Exact boundary terms and the stopping point

The residual numerator t^m p_k has a zero of exactly order m at zero because

    p_k(0)=(-1)^k A_k!=0.

More explicitly,

    (t^m p_k)^(r)(0)=0 for 0<=r<m,
    (t^m p_k)^(m)(0)=m!(-1)^k A_k.

At the other endpoint,

    Q_m(1)=m A_k,
    [p_k-(1-t)Q_m]_(t=1)=A_k.

The pole of the rational residual at t=1 has not been removed: its residue, with respect to t-1, is -A_k. Formula (8) concerns its absolutely convergent factorial-weighted Taylor functional, not a finite value of this rational function at one.

There is also an exact high-span boundary obstruction to one further automatic subtraction. At r=m, the multiplication band reaches p_n and p_(n+2m). The unique all-down and all-up walks in (7) give

    ell_x(t^m p_k)
      =(-1)^m [product_(l=n+1)^(n+m) beta_l] ell_x(p_n)
       +1_(2m=b-1) ell_x(p_(n+2m)).                    (14)

Every interior row vanishes by (1). If 2m<=b-2, the upper boundary also vanishes; if 2m=b-1, it is the omitted last high row. Thus attempting one extra step yields the exact remainder identity

    a_k(x)=ell_x(t^(m+1)p_k/(1-t))
      +(-1)^m [product_(l=n+1)^(n+m) beta_l] ell_x(p_n)
      +1_(2m=b-1) ell_x(p_(n+2m)).                    (15)

No control of these boundary functionals is assumed. The guaranteed subtraction branch stops at (6). They are not set to zero by a normality statement.

## 6. A quantitative full-remainder bound

For a polynomial P and integer s=n+m+1-j>=1,

    |ell_j(t^m P/(1-t))|
       <=||P||_1 sum_(a>=0) 1/(s+a)!
       <=e ||P||_1/s!<3||P||_1/s!.

Indeed each ordinary coefficient of P introduces only an additional nonnegative factorial shift. Combining this complete-tail estimate with (8) gives

    |a_k(x)|<=3 L_k sum_(j=0)^b |x_j|/(n+m+1-j)!.     (16)

Define the positive rational reference envelope

    d_k=2|h_k|/A_k^2.

The reference identity in Section 2 gives epsilon_k<=d_k. Therefore the complete bound, valid also when Y=0, is

    |R(1)|<=B_m(x),
    B_m(x)=d_k |Y|
       +3(L_k/A_k) sum_j |x_j|/(n+m+1-j)!,
    k=n+m.                                            (17)

Its first term bounds the full pi error in (4); its second bounds the full exponential companion. The exact signed expression (4) remains available when a triangle bound is too costly.

There is an explicit net gain in (17). Since |h_(k+1)|/|h_k|=beta_(k+1),

    d_(k+1)/d_k=beta_(k+1)/(A_(k+1)/A_k)^2<=1/3.       (18)

Use the same n,b,x, and compare against m=1, k=n+1. From (13) and the factorials, the exponential term in B_m is at most

    [28/(9(n+3-b))]^(m-1)

 times the exponential term in B_1. The pi term is at most 3^(-(m-1)) times the pi term in B_1. Thus

    B_m(x)<=c_m B_1(x),
    c_m=max{3^(-(m-1)),
            [28/(9(n+3-b))]^(m-1)}.                  (19)

In particular, if n-b>=7,

    B_m(x)<=3^(-(m-1)) B_1(x).                        (20)

This comparison includes every reference-polynomial and endpoint-normalization factor. It is a direct comparison of explicit positive coefficient weights on the same x. It does not estimate a quotient of actual remainders by dividing upper bounds. No product of separate high-row norm bounds is used, so the saved quadratic high-row-slack expression is not the mechanism behind (19).

The result is a relative improvement, not a shrinking-form theorem. The actual coefficient vector may already have enormous norm, especially when it is the rational lift of a prescribed endpoint direction.

## 7. An unbounded subtraction range

For all sufficiently large n, the choice

    b=floor((n/(1024 log n))^(1/4)),
    m=floor((b-1)/2)

has b>=3, satisfies n>=512 b^4 log n, and has n-b>=7. Moreover m tends to infinity. Thus (20) supplies a relative full-majorant saving

    3^(-(m-1))=exp(-(log 3)b/2+O(1)).

The exponential-companion part has the stronger relative factor

    exp(-(m-1)log n+O(m)),

because b=o(n). This includes (13), rather than quoting the factorial shift alone. The slow-growth choice supplies a domain compatible with the provisional normality research; it is not a proof of normality or of adequate conditioning there.

## 8. The actual rational endpoint inverse

Assume now that J is nonsingular. The notation here specifies the inverse exactly while leaving its quantitative development to Child 3.

Let f_h=[z^h]F(z), with f_h=0 for h<0. The square matrix J has rows r=0,...,M-1 and columns corresponding to

    z^j,          0<=j<n;
    z^j exp(z),   0<=j<b;
    z^j F(z),     0<=j<n.

Define an M by 2 rational matrix F0 by

    F0_(r,1)=1,
    F0_(r,2)=sum_(h=0)^r (1/h!+f_h).

Writing A=(z-1)A'+P, B=(z-1)B'+Q, C=(z-1)C'+Q gives the primed lift

    V=J^(-1)F0.

Let V_B be its b rows for B'. Define the (b+1) by b matrix

    (D_B)_(j,l)=1_(j=l+1)-1_(j=l),
    0<=j<=b, 0<=l<b.

With e_0 the first coordinate vector in Q^(b+1), and e_2=(0,1)^T, the actual B-coefficient lift is

    Phi=D_B V_B+e_0 e_2^T,
    x=Phi u, u=(P,Q)^T.                               (21)

All entries are rational. Equivalently,

    Phi_(j,a)=sum_l (D_B)_(j,l)
       [adj(J)F0]_(B'_l,a)/det J
       +1_(j=0)1_(a=2).

This records the exact inverse dependence, including numerators and denominators. No estimate for det J alone is substituted for an estimate of Phi. Also sum_j Phi_(j,.)=e_2^T, as required by B(1)=Q.

The map Phi is injective. If Phi u=0, then B=0; the first n+1 moment equations give Cstar=0, and the Taylor reconstruction gives A=0. Its endpoint u is therefore zero. This is a consequence of the already stated reconstruction and the assumed endpoint lift, not a separate normality proof.

## 9. A rational positive definite quadratic bound

For the same m and k=n+m, define

    r=n+m+1-b,
    w_j=r!/(n+m+1-j)!, 0<=j<=b,
    gamma=3 L_k/(A_k r!),
    Sigma=Phi^T diag(w_j^2) Phi
         =[[U,V0],[V0,W]],
    Delta=UW-V0^2,
    Z=(b+1)(gamma/d_k)^2.                              (22)

Every quantity in (22) is rational. All w_j are positive, and Phi is injective, so Sigma is positive definite, U>0 and Delta>0. The factorial normalization w_b=1 makes the coefficient scale explicit.

Pull (17) through (21). Cauchy-Schwarz gives

    |P+Q(e+pi)|
       <=d_k |Q|+gamma sum_j |w_j(Phi u)_j|
       <=d_k |Q|+sqrt(b+1) gamma sqrt(u^T Sigma u).

Using (a+b)^2<=2(a^2+b^2), set

    eta=d_k,
    G=2[e_2 e_2^T+Z Sigma].                            (23)

Then G is rational positive definite and

    |P+Q(e+pi)|<=eta sqrt(u^T G u).                    (24)

The proof applies to every real u after extending the rational lift linearly; in particular it applies to all integer pairs. The term 2 e_2 e_2^T bounds the full pi error. Removing it would leave only a companion estimate and would invalidate (24) as a complete-form claim.

The exact inverse-conditioning quantities are

    U=sum_j w_j^2 Phi_(j,1)^2,
    V0=sum_j w_j^2 Phi_(j,1)Phi_(j,2),
    Delta=sum_(i<j) w_i^2 w_j^2
                      det(Phi_[i,j])^2.               (25)

Here Phi_[i,j] is the two by two submatrix on rows i,j. The last formula is Cauchy-Binet, with every minor retained. These are actual rational inverse data; their growth is not bounded merely by defining them.

The net improvement survives the quadratic conversion. Write H_m=eta_m^2 G_m, with n,b and Phi fixed while m varies over (6). Then

    H_m=2 d_(n+m)^2 e_2 e_2^T
       +2(b+1) sum_j
          [3 L_(n+m)/(A_(n+m)(n+m+1-j)!)]^2
                         Phi_(j,.)^T Phi_(j,.).

The coefficient comparisons used in (19) give

    H_m <= c_m^2 H_1                                  (26)

in the positive-semidefinite ordering. In particular H_m<=3^(-2(m-1))H_1 when n-b>=7. This is a comparison of the complete quadratic bounds, rather than an artificial rescaling of eta and G. It does not imply that the two center-pair targets are monotone, since their reduced rational center denominators can change with m.

## 10. Exact interface with the rational-center criterion

The main RATIONAL_CENTER_PAIR_CRITERION.md was read as a new conditional criterion, not as an attained estimate. For (23),

    G11=2 Z U,
    G12=2 Z V0,
    det G=4 Z(U+Z Delta).

Consequently its rational center is exactly

    t=G12/G11=V0/U=p/q,
    q>0, gcd(|p|,q)=1.                                 (27)

The scalars gamma and d_k cancel from the center. The weights w_j and the actual inverse Phi do not cancel. If a positive integer L clears U and V0, the exact denominator is

    q=(L U)/gcd(L U,|L V0|).                           (28)

Increasing L does not alter q. Formula (28) is the arithmetic input for Child 4; a lift denominator or lattice index is not a substitute for this gcd.

The two sufficient quantities in the main criterion are, in this normalization, precisely

    E=eta^2 G11/q^2
      =2(b+1) gamma^2 U/q^2,

    F=eta^2 det(G) q^2/G11
      =[2 d_k^2+2(b+1) gamma^2 Delta/U]q^2.            (29)

Their product, also exactly,

    E F=eta^4 det G
       =4(b+1) gamma^2 d_k^2 U
          +4(b+1)^2 gamma^4 Delta.                    (30)

The full pi error contributes the indispensable term 2 d_k^2 q^2 in F. No favorable cancellation between e and pi is presumed in (29).

If both E and F tend to zero on an unbounded normal sequence, the main criterion constructs the primitive independent pair

    u_1=(-p,q), u_2=(x,y), qx+py=1, |y|<=q/2,

and bounds their full forms by sqrt(F) and sqrt(E+F/4). These are conditional implications. Neither limit in (29) is established here.

## 11. A necessary inverse-conditioning check

The rational lift of u=(1,0) has full remainder exactly one and Y=0. Equations (3) and (16) therefore imply

    1<=gamma sum_j |w_j Phi_(j,1)|
       <=sqrt(b+1) gamma sqrt(U).

Hence

    (b+1) gamma^2 U>=1.                               (31)

The inverse must compensate at least this much for the small factorial coefficient. In particular U cannot be bounded independently of gamma in a way contradicting (31), and E->0 requires q->infinity. Normality by itself supplies none of the directional estimates needed to make (29) small.

Equation (31) does not refute (19) or (26): the one-row bound for this direction can be very large. It prevents promoting a relative saving, or a small scalar gamma, to a shrinking primitive-form theorem without the actual inverse data.

The exact outstanding quantities are gamma^2 U, gamma^2 Delta/U, and the reduced denominator q of V0/U, together with the retained d_k^2 q^2 term. This identifies an actual coefficient amplification and its directional minors, rather than renaming an unspecified combined-polynomial norm.

## 12. Each endpoint gcd and the rational lift

Let an integer triple have a nonzero endpoint pair (X,Y). Define separately for that triple

    g=gcd(|X|,|Y|), P=X/g, Q=Y/g.

By uniqueness of the rational endpoint lift,

    x/g=Phi(P,Q)^T,
    R(1)/g=P+Q(e+pi).

Substituting these identities into (17) gives exactly (24), with the same rational G. When Y!=0 the positive reduced denominator is |Q|=|Y|/g. No polynomial coefficient clearer has been identified with it. The case Q=0 is covered without division by Q; a nonzero primitive pair then has form +1 or -1.

For comparison with Child 4's ENDPOINT_LATTICE_RESEARCH.md, let mu(u) be the minimal positive radial factor making the rational lift of a primitive integer direction u integral. The integer endpoint is mu(u)u, and its endpoint gcd is exactly mu(u). The coefficients, full remainder, and endpoint gcd all acquire the same factor. It cancels term by term from (17), (24), and (29).

For two different primitive directions, use their respective radial factors and respective endpoint gcds. They need not lift to a lattice basis. The center pair in Section 10 has primitive determinant -1 regardless of those radial factors. This is the exact arithmetic interface; no new saving is credited to denominator clearing.

## 13. What has and has not been obtained

The new author deductions are the normalized multi-row recurrence (9), its coefficient budget (10)-(13), the exact boundary terms (14)-(15), the net complete-majorant gain (19)-(20), and the rational positive definite full-form bound (23)-(24). The explicit center and the two exact remaining targets are (27)-(29).

The subtraction branch is productive within (6): its coefficient amplification does not cancel the relative saving. It stops at the displayed low/high boundary terms rather than assigning them zero. No saved high-row-slack estimate, ratio of upper bounds for actual determinants, or frozen-control computation is used.

No useful asymptotic control of the actual inverse entries or minors, no reduced-center denominator estimate, and no shrinking primitive endpoint pair is proved. The quadratic form is an explicit valid certificate conditional on the endpoint inverse, but its usefulness for the main paired-form limits remains unresolved. No conclusion about the rationality of e+pi follows.

The current note and MULTIROW_REMAINDER_REPORT.md are separate coordination artifacts. Other agents' files and the earlier two-row author results are not edited. Final completion requires actual read-back of these two saved outputs.
