> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Total cancellation deficit for the canonical b=3 Gram center

Original author research, offline; not independently reviewed. This saves the retained derivation from the interrupted assignment and incorporates the newly reported joint denominator budget. No seed calculation, modulo-121 transfer, old read-back, or completed control is repeated. All constructions concern the SAME factorial B-only Gram center with b=3,m=1.

The target log(delta)=o(n log n) remains unproved. The principal result is an exact separation into a factorial-truncated cancellation gcd and an exceptional factor constrained by explicit contents and a strictly positive binary-form resultant. The final numerator includes the endpoint correction and logarithmic companion.

## 1. Domain and retained fraction-free data

The algebraic identities apply at integer n>=3 whenever the actual contact matrix T is nonsingular. The eventual analytic conclusions use even n in the retained fixed-b slow-growth domain

    n>=16, n>=512*3^4 log n.

This is an unbounded normality regime under the retained author theorem. The previously proved sequence n=11^h+3, h>=6, is also available, but its transfer and seed are not repeated here. No coordinate-center or full-coefficient-center result is substituted for this Gram center.

Use the retained data

    F=(n!)^2, d0=(n+1)(n+2),
    Drow=diag(1,n+1,(n+1)(n+2)),
    M=2^n n! Drow T, Delta=det M!=0,
    J=(2^n/n!)fP,
    Krec=Z(I+D)^(-n),
    C=Krec adj(M)Drow,
    x=CJ,
    Omega=diag(((n+2)_j)^2), 0<=j<=3,
    Dg=x^T Omega x>0,
    z=C^T Omega x.

Here Z multiplies polynomials by t-1, D differentiates, and (n+2)_j is a falling factorial. The matrix C has size 4 by 3. All displayed fraction-free matrices and vectors are integral.

Let

    Ecal_i=2^n(n+2)! sum_s a_s(n) Dcal_(2n+i-s)/(n+i-s)!,
    a_s(n)=[t^s](1-t+t^2/2)^n,
    Dcal_k=k! sum_(j=0)^k 1/j!,
    0<=s<=min(2n,n+i), 0<=i<=2,
    Acal=z^T Ecal,
    Rcal=Delta x_0.

This is the previously derived exact exponential integer vector. Its definition is retained without recomputation. The endpoint correction is kappa=Rcal/(F Dg).

For a uniform moment clearer, use

    L=2^(2n+1) lcm(1,...,2n+2).

The actual primitive selector has degree at most two, so this is a valid multiple of its previous degree-dependent clearer. Define every moment numerator in this note with this L. Changing the clearer in this documented way does not change any rational companion or reduced denominator.

For i=0,1,2 put

    K_i(t)=(2^n/n!) t^n D_t^n((t^2-t+1/2)^n t^i),
    K_i(1)=J_i,
    theta_i=L calL((K_i-J_i)/(t-1)),
    calL(P)=integral_-1^1 P((1+iu)/2)du.

Each K_i is integral and theta_i is an integer. Indeed the quotient is an integer polynomial of degree at most 2n+1, and the displayed L clears its segment moments. One can see this directly from

    calL(t^m)=2^(-m) sum_(j even,0<=j<=m)
                         2 binom(m,j)(-1)^(j/2)/(j+1).

Write theta=(theta_0,theta_1,theta_2) and Tlog=theta z. The exact companions are

    alpha=Acal/(F d0 Dg),
    kappa=Rcal/(F Dg),
    beta=Tlog/(L Dg),
    gamma=kappa+beta,
    c=alpha+gamma.

All final arithmetic below retains these exact companions.

## 2. Original final gcd formula

Set

    Dorig=F d0 L Dg,
    Uorig=L Acal,
    Vorig=d0(L Rcal+F Tlog),
    Psi=Uorig+Vorig=L(Acal+d0 Rcal)+F d0 Tlog.

Then the positive reduced denominators are

    Q=Dorig/gcd(Dorig,|Uorig|),
    B=Dorig/gcd(Dorig,|Vorig|),
    q=Dorig/gcd(Dorig,|Psi|).

For the requested total deficit

    delta=B/gcd(q,B),

the retained exact identity is

    delta=gcd(Dorig,|Psi|)
                 /gcd(Dorig,|Uorig|,|Vorig|).             (1)

The convention gcd(a,0)=a applies throughout. Formula (1) includes zero rational companions and does not require a nonzero center. The term L d0 Delta x_0 in Psi is indispensable.

Also, exactly,

    lcm(q,B)=lcm(Q,B)=q delta,
    delta divides gcd(Q,B).                              (2)

These identities do not imply B divides q. The previously established one-power loss at 11 remains a retained example of equal-depth cancellation; it supplies no global deficit bound.

## 3. Perturbation by the logarithmic companion

Let delta0 be the analogous deficit for alpha+kappa, with kappa as the second companion. It has the exact formula

    delta0=gcd(F d0 Dg,|Acal+d0 Rcal|)
                /gcd(F d0 Dg,|Acal|,|d0 Rcal|).          (3)

Put Bbeta=den(beta). For every prime p,

    |v_p(delta)-v_p(delta0)|<=v_p(Bbeta).                 (4)

Consequently both delta/gcd(delta,delta0) and delta0/gcd(delta,delta0) divide Bbeta.

Proof. For a rational y define its denominator depth d_p(y)=max(0,-v_p(y)), taking d_p(0)=0. If t=d_p(beta), adding beta preserves every depth greater than t, and takes a depth at most t to a depth at most t. Now

    v_p(delta)=max(d_p(kappa+beta)-d_p(alpha+kappa+beta),0),
    v_p(delta0)=max(d_p(kappa)-d_p(alpha+kappa),0).

If both original depths exceed t, both remain unchanged. If just one exceeds t, its value remains fixed while the other ranges inside [0,t]; the positive difference therefore changes by at most t. If both are at most t, both positive differences lie in [0,t]. This proves (4).

Since Bbeta divides L Dg, it follows that

    sum_(p not dividing Dg)
       |v_p(delta)-v_p(delta0)| log p <=log L=O(n).      (5)

Thus outside Gram-contraction primes the logarithmic companion costs at most O(n) in the total comparison. The focused numerator there is Acal+d0 Delta x_0. At primes dividing Dg, the companion denominator can have much larger depth, so (5) does not license dropping Tlog from the global problem.

## 4. Exact reduction to a positive binary quadratic form

The retained positive-forcing identities are

    J_0=P_n,
    J_1=P_n/2+P_(n+1)/4,
    J_2=P_(n+2)/8.

Use the endpoint recurrence

    (n+2)P_(n+2)=2(2n+3)P_(n+1)+4(n+1)P_n.

Define

    e=4(n+2),
    j0=(4(n+2),2(n+2),2(n+1))^T,
    j1=(0,n+2,2n+3)^T,
    Rmat=C[j0 j1],
    Zmat=C^T Omega Rmat.

Then

    eJ=j0 P_n+j1 P_(n+1).

The columns j0,j1 are independent. Since Krec is injective and adj(M)Drow is invertible, C has column rank three. Hence Rmat has rank two. The integral binary quadratic form

    Bform(X,Y)=(X,Y)Rmat^T Omega Rmat(X,Y)^T            (6)

is positive definite over the reals. This is a genuine quadratic-form consequence of the actual Gram construction, not an entrywise positivity claim.

Let

    t0=gcd(P_n,P_(n+1)),
    w=(P_n/t0,P_(n+1)/t0)^T.

The integer pair w is primitive. Define integer rows of length two by

    avec=Ecal^T Zmat,
    rvec=Delta e0^T Rmat,
    bvec=theta Zmat,
    urow=L avec,
    vrow=d0(L rvec+F bvec).

The row rvec retains the exact endpoint correction. Direct substitution gives

    x=(t0/e)Rmat w,
    z=(t0/e)Zmat w,
    Dg=(t0/e)^2 Bform(w),
    Acal=(t0/e)avec w,
    Rcal=(t0/e)rvec w,
    Tlog=(t0/e)bvec w.

Therefore, with the positive integer

    Dstar=F d0 L t0 Bform(w),

the ORIGINAL companions satisfy

    alpha=e urow w/Dstar,
    gamma=e vrow w/Dstar.                              (7)

No different selector or coordinate center has been introduced.

## 5. Remove common normalizations before measuring cancellation

Assume first that urow,vrow are not both zero. Let s be the positive gcd of their four integer entries and put

    u0=urow/s, v0=vrow/s,
    gstar=gcd(Dstar,e s),
    D1=Dstar/gstar,
    kstar=e s/gstar.

Then gcd(kstar,D1)=1. Thus this residual common multiplier does not affect the reduced denominator of either companion or their sum.

Retain the FINAL evaluated common gcd

    h0=gcd(D1,|u0 w|,|v0 w|),
    D2=D1/h0,
    U=(u0 w)/h0,
    V=(v0 w)/h0,
    Wcancel=U+V.

These are integers and

    alpha=kstar U/D2,
    gamma=kstar V/D2,
    gcd(D2,U,V)=1,
    gcd(kstar,D2)=1.

Consequently the exact final denominator formulas become

    Q=D2/gcd(D2,|U|),
    B=D2/gcd(D2,|V|),
    q=D2/gcd(D2,|Wcancel|),
    delta=gcd(D2,|Wcancel|).                           (8)

In particular

    Wcancel=((u0+v0)w)/h0                              (9)

is the precise normalized equal-depth numerator. The definitions retain every common normalization and the last evaluated gcd before asserting cancellation.

For every prime dividing delta, both U and V are p-adic units. Indeed p dividing U+V and either U or V would divide both, contradicting gcd(D2,U,V)=1. Thus every lost prime power is genuinely an equal-depth cancellation, with exact exponent

    v_p(delta)=min(v_p(D2),v_p(Wcancel)).               (10)

If urow=vrow=0, both companions vanish and their denominators and delta are one; formula (1) handles that case directly. Other zero cases also remain covered by (1) and (8). The resultant construction below needs the nonzero row u0+v0. On the eventual even normality regime, the retained canonical convergence c->e+pi>0 implies c!=0, and hence this row and Wcancel are nonzero. No new sign or finite-sample inference is required for that restriction.

## 6. A positive resultant bounds the exceptional part

Let a_B be the positive coefficient content of the binary form (6), and write

    Bform=a_B Bprim.

Here coefficient content means the gcd of the coefficients of X^2, XY, and Y^2, including the factor two in the mixed coefficient when the form is written from its symmetric matrix. The integral form Bprim is primitive and positive definite.

For the nonzero row u0+v0 write

    u0+v0=c_H(H0,H1),
    c_H>0, gcd(H0,H1)=1.

Define the explicit integer

    Rres=Bprim(-H1,H0)>0.                              (11)

This is, up to the harmless resultant sign convention, the homogeneous resultant of the quadratic form and primitive linear form H0 X+H1 Y. Positivity proves Rres is nonzero at every admitted index. It is not an assumed generic resultant.

For every primitive integer pair w,

    gcd(Bprim(w),|H0 w_0+H1 w_1|) divides Rres.         (12)

Proof. Extend (H0,H1) to the first row of a unimodular integer matrix and use its coordinates (y,z). Then y=H0 w_0+H1 w_1 and gcd(y,z)=1. At y=0 the inverse transformation gives w=plus or minus z(-H1,H0), so

    Bprim(w)=Rres z^2 modulo y.

For any prime power dividing y, z is a unit. Comparing valuations proves (12), including all prime powers rather than only prime support.

Now split the EXACT deficit as

    delta_F=gcd(F,delta)=gcd(F,D2,|Wcancel|),
    delta_exc=delta/delta_F.                            (13)

The factors need not be coprime. Since D2 divides Dstar=F d0 L t0 Bform(w), comparison at each prime gives

    delta_exc divides d0 L t0 Bform(w).

It also divides Wcancel, hence divides c_H(H0 w_0+H1 w_1) by (9). Applying (12) therefore proves

    delta_exc divides d0 L t0 a_B c_H Rres.            (14)

To see that no coprimality has been presumed, put A0=d0 L t0 a_B. At each prime,

    min(v_p(A0)+v_p(Bprim(w)),
        v_p(c_H)+v_p(H0 w_0+H1 w_1))
    <=v_p(A0)+v_p(c_H)
         +min(v_p(Bprim(w)),v_p(H0 w_0+H1 w_1)).

Then apply (12). This proves the full divisibility in (14).

The additional exact restriction delta_exc|Wcancel yields the stronger combined statement

    delta_exc divides
       gcd(d0 L t0 a_B c_H Rres,|Wcancel|).            (15)

In particular

    max(v_p(delta)-2v_p(n!),0)
       <=v_p(d0 L t0 a_B c_H Rres)                    (16)

for every prime. Thus excess loss beyond the factorial multiplicities has explicitly constrained support and depth.

The bound P_n<=[2(1+sqrt(2))]^n follows from its retained circle representation by taking absolute values. Since t0<=P_n, log t0=O(n). Also log d0=O(log n) and log L=O(n). Consequently

    log delta<=log gcd(F,D2,|Wcancel|)
                         +log(a_B c_H Rres)+O(n).     (17)

The stronger version keeps the gcd in (15) instead of bounding it by the whole product. No estimate is asserted that the contents or resultant attain their full possible size, or that they are subfactorial.

## 7. Exact remaining global conditions

The factorial-truncated contribution is

    delta_F=product_p
       p^min(2v_p(n!),v_p(D2),v_p(Wcancel)).           (18)

The target is equivalent to controlling the sum of the logarithms of the two exact factors in (13). A sufficient deterministic route, using the proved upper bound, is

    log gcd(F,D2,|Wcancel|)=o(n log n),
    log gcd(d0 L t0 a_B c_H Rres,|Wcancel|)=o(n log n). (19)

A stronger but simpler sufficient second condition is

    log(a_B c_H Rres)=o(n log n).                     (20)

Neither (19) nor (20) is established for this canonical family. The first condition is not a routine consequence of a factorial clearer: it requires controlling the actual normalized numerator Wcancel at primes carrying factorial depth. The second condition concerns explicit per-index integer contents and a resultant formed from the actual recurrence data. Rres is not a fixed polynomial in n, and its positivity alone gives no useful height or prime-power bound.

Equivalently, the exact total sum to control is

    log delta=sum_p min(v_p(D2),v_p(Wcancel)) log p,  (21)

where every contributing prime has the unit-numerator cancellation U+V=0 modulo the relevant prime power. Formula (18) truncates that sum at 2v_p(n!); equations (14)-(16) constrain the excess.

The perturbation lemma supplies a complementary reduction outside primes dividing Dg: there one can use the endpoint-corrected exponential numerator Acal+d0 Delta x_0, with only O(n) total logarithmic disturbance. At Gram primes the complete Wcancel must remain. Separate estimates for the numerator terms, or support bounds for their individual contents, do not decide their sum after the final gcd h0.

The retained exact lost factor at 11 is consistent with these formulas and with a subfactorial total deficit. It provides no global conclusion about (19) or (21).

## 8. Joint denominator budget without a complete-error premise

The main has now reported the joint budget in JOINT_COMPANION_OVERLAP_BUDGET_DRAFT.md. Its elementary consequence can be incorporated directly from (2), without rereading completed notes or invoking a complete-error lower bound.

Retain the established canonical exponential approximation

    |alpha-e|<=E,
    -log E~X, X=n log n

on the even slow-growth regime. For every fixed epsilon>0, the retained rational-approximation theorem for e gives

    |alpha-e|>=C_epsilon Q^(-nu), nu=2+epsilon.

Since Q divides lcm(Q,B)=q delta,

    q delta>=Q>=(C_epsilon/E)^(1/nu).

Taking logarithms and then letting epsilon decrease to zero proves

    liminf (log q+log delta)/(n log n)>=1/2.           (22)

This statement requires neither a pi irrationality-measure input nor a premise about the complete error c-(e+pi).

If log delta=o(n log n) were proved on an unbounded admitted sequence, it would follow that

    liminf log q/(n log n)>=1/2.

In particular geometric denominators, meaning log q=O(n), would be excluded there. Conversely, on any such sequence with log q=O(n), (22) forces

    liminf log delta/(n log n)>=1/2.

These are conditional implications. The new factorization does not establish either subfactorial delta or geometric q for the actual family.

## 9. Consequence for the complete overlap threshold

Let R=q|c-e-pi|. The retained complete overlap inequality, with a valid uniform pi exponent mu and nu=2+epsilon, is

    C_pi<=E B^mu
        +R C_epsilon^(-1/nu) E^(1/nu) B^mu delta.     (23)

For finite rates

    beta_rate=limsup log B/(n log n),
    eta_rate=limsup log delta/(n log n),

the strict condition

    mu beta_rate+eta_rate<1/2                         (24)

is sufficient for primitive-error divergence, with the limiting lower rate

    1/2-mu beta_rate-eta_rate>0.

The main has confirmed the published pi measure bound 36/5. Use a uniform exponent strictly above that bound unless the source supplies the boundary inequality itself. Approaching it through admissible exponents shows that

    beta_rate<5/72 and log delta=o(n log n)

suffice. Exact B|q is unnecessary. The present result does not establish the deficit condition or a sufficient B-rate condition. The joint lower bound (22) is separate and already follows without (23).

## 10. Outcome and preservation

The strongest proved structural result is the exact factorization (13), with the explicit prime-power restrictions (14)-(16), after the common row normalization and final evaluated gcd have been removed. Its resultant is strictly positive because the binary form is the actual positive Gram form. Every companion normalization, endpoint correction, and final numerator gcd is retained.

The target log delta=o(n log n) remains open. Equations (18)-(21) specify the remaining arithmetic. The newer joint denominator budget (22) explains why proving that target would already exclude geometric q, independently of complete-error analysis.

All retained prior derivations and calculations are preserved. No modulo-121 transfer, seed evaluation, old read-back, independent review, broad scan, or coordinate-to-Gram transfer was performed in this closeout. The deliverables are this note and CANONICAL_OVERLAP_DEFICIT_REPORT.md under work/session_20261001_astra/agent3/. Their successful saving and subsequent read-back must be confirmed by the application before operational completion is reported.
