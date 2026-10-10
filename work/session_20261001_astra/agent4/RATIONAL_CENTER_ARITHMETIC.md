> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rational-center arithmetic for the relaxed contact lift

New research by Agent 4. Work is offline. No completed quotient audit, old checker, approximation control, or prime scan is repeated.

The limited normality review is complete: SLOW_GROWTH_NORMALITY_REVIEW.md was saved and read back. Its verdict is PASS for det J_(n,b)>0 when n>=16, 2<=b<=n, and n>=512 b^4 log n, with the stated column order. No defect was found in the reviewed exact reduction, contour argument, constants, or unbounded allocation. This does not extend to b=floor(n/2). The review does not certify the quantitative inverse estimates in CONTACT_INVERSE_RESEARCH.md.

For the arithmetic below use b>=3 within that normality domain, and choose

    1<=m<=floor((b-1)/2), k=n+m, lambda=k+1, r=lambda-b.

All asymptotic assertions below are explicitly conditional. The new unconditional conclusions on this domain are exact arithmetic identities, divisibility restrictions, and recurrences in the weight parameter with n,b fixed.

## 1. The selected norm and the exact distinction between the papers

Let Phi be the full rational coefficient lift from endpoint data u=(P,Q)^T to the triple (A,B,C). Let Psi be its B-coefficient block, of size (b+1) by 2. Child 2 calls this B block Phi in MULTIROW_REMAINDER_RESEARCH.md; throughout this note it is Psi. Thus

    sum_j Psi_(j,.)=(0,1),
    B=Psi u,
    A(1)=P, B(1)=C(1)=Q.

The B block is injective: B=0 forces C=0 through the moment reconstruction and then A=0. This fact supplies positive definiteness of its weighted Gram matrix.

Use precisely the weights and complete bound from ../agent2/MULTIROW_REMAINDER_RESEARCH.md:

    A_k=p_k(1), L_k=||p_k||_1,
    d_k=2|h_k|/A_k^2,
    w_j=r!/(lambda-j)!, 0<=j<=b,
    gamma=3 L_k/(A_k r!),
    Sigma=Psi^T diag(w_j^2) Psi=[[U,V],[V,W]],
    Delta=UW-V^2>0,
    zeta=(b+1)(gamma/d_k)^2.

The reference envelope d_k is distinct from every coefficient-lift denominator used below. All these quantities are rational and use no numerical approximation to e+pi.

The justified COMPLETE quadratic bound is

    |P+Q(e+pi)| <= eta sqrt(u^T G u),
    eta=d_k,
    G=2[e2 e2^T+zeta Sigma], e2=(0,1)^T.                 (1)

For context, its derivation retains the exact identity

    R(1)=Q v_k/A_k+ell_(Psi u)(t^m p_k/(1-t))/A_k.

The subtraction uses only retained rows because t^s p_k lies in the span of p_(k-s),...,p_(k+s), which is annihilated for 0<=s<m. The complete factorial tail is bounded by 3 L_k/(n+m+1-j)!, and |v_k|/A_k<=d_k. Weighted Cauchy-Schwarz, followed by (a+b)^2<=2(a^2+b^2), gives (1). Both the pi term and the complete exponential term are present.

Writing G=[[a,h],[h,c]], its exact conversion from Sigma is

    a=2 zeta U, h=2 zeta V, c=2+2 zeta W,
    det G=4 zeta(U+zeta Delta),
    h/a=V/U,
    rho_G:=det G/a^2=1/(zeta U)+Delta/U^2.              (2)

The first term in rho_G cannot be removed.

The full-coefficient norm in ../agent3/CONTACT_INVERSE_RESEARCH.md is different. With that paper's positive reconstruction constants a0,c0 and wmin=min_j w_j, its Gram matrix is exactly

    Gfull=Sigma+(wmin/a0)^2 Phi_A^T Phi_A
               +(wmin/c0)^2 Phi_C^T Phi_C.             (3)

Its reported inequalities Sigma<=Gfull<=3Sigma do not identify rational centers or reduced denominators. For example, with theta=V/U and the extra summands in (3) denoted J_extra,

    Gfull_12/Gfull_11-theta
      =(J_extra_12-theta J_extra_11)/(U+J_extra_11).

There is no reason for this rational expression to vanish. This note selects G in (1), not Gfull. The exact forcing and reconstruction identities from the inverse paper are used below; its localization, coercivity, and exponential relative-error estimates remain named author results outside the limited review. None is needed to prove the arithmetic identities here. Section 9 of that paper supersedes its earlier internal pending-status paragraphs, but that author completion is not an independent review by this note.

## 2. Actual contact construction of the arithmetic input

The inverse paper reduces the primed B lift to the rational b by b Toeplitz matrix

    T_ij=[z^(n+i-j)] exp(z)Q0(z)^n,
    Q0(z)=1-z+z^2/2, 0<=i,j<b.

Its actual two forcing columns are

    fP_i=[z^(n+i)] Q0^n D^n(1/(1-z)),
    fQ_i=[z^(n+i)] Q0^n D^n((exp(z)+F(z))/(1-z)).

Let Fforce=[fP fQ]. With S_n=(D+1)^(-n) on polynomials of degree less than b and D_B multiplication by z-1 on coefficient vectors,

    Psi=D_B S_n T^(-1)Fforce+e0 e2^T.                  (4)

In ascending monomial coordinates S_n is an INTEGER matrix:

    (S_n)_(j,j+l)=(-1)^l binom(n+l-1,l)(j+l)!/j!,
    0<=l<=b-1-j.

Choose positive integer row clearers making both T_hat=D_rows T and F_hat=D_rows Fforce integral. Put delta=det T_hat, which is nonzero on the reviewed domain, and

    N=D_B S_n adj(T_hat)F_hat+delta e0 e2^T.

Then

    Psi=N/delta, N integral,
    sum_j N_(j,1)=0, sum_j N_(j,2)=delta.               (5)

This is a construction of the actual B lift through a b by b adjugate, with the constant endpoint term retained. It avoids reconstructing A and C merely to determine the center.

There is also an exact removal of the common factorial weight denominator. Set

    tau=r!/lambda!, v_j(lambda)=(lambda)_j,
    (lambda)_0=1,
    (lambda)_j=lambda(lambda-1)...(lambda-j+1).

Then w_j=tau v_j, and all v_j are positive integers at the actual indices. Define

    A_N=sum_j v_j^2 N_(j,1)^2,
    H_N=sum_j v_j^2 N_(j,1)N_(j,2).

The ACTUAL reduced denominator of h/a is therefore

    q=A_N/gcd(A_N,|H_N|).                              (6)

Both tau^2 and delta^2 cancel from the ratio before its final rational reduction. Formula (6) is not an estimate for delta. Enlarging the Taylor row clearers by an integer diagonal matrix R multiplies delta and N by det R, since adj(R T_hat)R=det(R)adj(T_hat). It consequently multiplies A_N and H_N by the same square and leaves q unchanged. No gain is credited to a larger clearer.

The remainder of the note resolves the common factors in (6) further using the saturated full lift.

## 3. Full-lift content and an explicit saturated basis

Retain the established primed lift Vprim=J^(-1)F0 from ENDPOINT_LATTICE_RESEARCH.md. Let d>=1 be its least common denominator, Wprim=d Vprim, and

    chi=gcd(d,t2(Wprim)),

where t2 is the gcd of all two-row determinants and gcd of an all-zero list is zero. This d is also the least denominator of the full lift Phi.

Put Z=d Phi. The integral coordinate change obtained by componentwise division by z-1 sends Z to the stack

    [Wprim; d I2; 0].

The final zero row is the matching coordinate. This coordinate change is unimodular. Minimality of d gives gcd(d,entries Wprim)=1. Therefore the first and second determinantal contents of Z are exactly

    Delta1(Z)=1,
    Delta2(Z)=gcd(t2(Wprim),d entries Wprim,d^2)=chi.    (7)

In particular chi divides d. This proves a content identity for the full lift, stronger than its endpoint index alone.

Write its two columns as

    Z_1=g1 x, Z_2=g2 y,

where g1,g2>0 are their coefficient gcds and x,y are primitive integer columns. Equation (7) implies

    gcd(g1,g2)=1,
    g1 g2 divides chi,
    c_perp:=chi/(g1 g2)=t2([x,y])>0.

Choose an integer row r0 with r0 x=1. Put t=r0 y and

    z_perp=(y-tx)/c_perp.

Then z_perp is integral, gcd(t,c_perp)=1, and

    K=[x,z_perp], Delta2(K)=1.                         (8)

Proof: extend x to an integer unimodular basis whose remaining columns lie in ker r0. In these coordinates x is the first coordinate vector and y has first coordinate t. The gcd of its remaining coordinates is precisely t2([x,y])=c_perp. Division of those coordinates by c_perp gives (8); primitivity of y gives gcd(t,c_perp)=1.

Thus K is a basis of the SATURATED coefficient kernel, not merely a pair obtained by clearing rational kernel columns. The exact factorization is

    Phi=(1/d) K R,
    R=[[g1,g2 t],[0,g2 c_perp]], det R=chi.             (9)

If E denotes the endpoint map, E Phi=I2 gives

    EK=d R^(-1)
      =[[d/g1,-d t/(g1 c_perp)],
        [0,d/(g2 c_perp)]].                            (10)

All entries in (10) are integers. Its determinant is d^2/chi, the established endpoint-lattice index.

Changing the auxiliary row r0 changes t to t+c_perp l and z_perp to z_perp-l x for an integer l. The formulas below are invariant under this shear; no favorable basis choice is concealed.

## 4. Integer weighted contractions and every factor in q

Let xi and nu be the B-coefficient blocks of x and z_perp. For the integer weights v_j=(lambda)_j define

    A_*=sum_j v_j^2 xi_j^2>0,
    H_*=sum_j v_j^2 xi_j nu_j,
    C_*=sum_j v_j^2 nu_j^2,
    D_*=A_* C_*-H_*^2>0.                               (11)

These are integers. Positivity follows from injectivity of the B reconstruction on the saturated two-dimensional plane. In particular, ambient coefficient saturation does NOT imply that the B-projected minors have gcd one.

Substituting (9) into Sigma gives the exact formulas

    U=tau^2 g1^2 A_*/d^2,
    V=tau^2 g1 g2(t A_*+c_perp H_*)/d^2,
    Delta=tau^4 chi^2 D_*/d^4.                         (12)

Hence, with

    kappa=gcd(g1 A_*, |g2(t A_*+c_perp H_*)|),

one has the fully reduced center

    p=g2(t A_*+c_perp H_*)/kappa,
    q=g1 A_*/kappa>0.                                  (13)

If the mixed contraction is zero, kappa=g1 A_* and q=1. All formulas include this case. Neither d, chi, nor either separate column content is substituted for q.

There are two useful exact ways to separate the cancellations.

First put

    s=gcd(A_*,g2 c_perp), A0=A_*/s,
    v=gcd(A0,|H_*|), R0=s v,
    B0=g2(t A_*+c_perp H_*)/R0.

Then B0 is integral, gcd(A_*/R0,B0)=1, and

    kappa=R0 gcd(g1,|B0|),
    q=(A0/v) g1/gcd(g1,|B0|).                          (14)

Indeed gcd(A_*,g2(t A_*+c_perp H_*))=gcd(A_*,g2 c_perp H_*)=s v. In the important special case g1=1,

    q=A0/gcd(A0,|H_*|).

Here s is forced by the lift contents, while the remaining contraction gcd depends on the actual rational weights. There is no random-coprimality assumption.

Second, put r_*=gcd(A_*,|H_*|). Then

    r_* divides kappa, kappa divides chi r_*,
    e_*=kappa/r_* divides chi,
    q=g1(A_*/r_*)/e_*.                                 (15)

To prove the upper divisibility, divide A_*,H_* by r_* to obtain a primitive pair. The two arguments defining kappa/r_* are its image under the integer matrix

    [[g1,0],[g2 t,g2 c_perp]],

whose determinant is chi. The adjugate identity shows that the gcd of the image coordinates divides chi. Thus (15) retains both the metric gcd r_* and the additional lattice factor e_* exactly.

Under the shear after (10), H_* changes to H_*-l A_* and C_* to C_*-2l H_*+l^2 A_*. Both D_* and t A_*+c_perp H_* remain unchanged. Equations (13)-(15) are consequently independent of the choice of r0.

## 5. The center direction's own endpoint gcd

The explicit center vector is u1=(-p,q), a primitive integer pair. Equations (9) and (13) give

    Phi u1=chi/(d kappa) K(-H_*,A_*)^T.                (16)

Because K is saturated, the coefficient gcd of K times an integer vector equals the gcd of that vector's coordinates. Thus its minimal primitive integral coefficient lift is exactly

    K(-H_*/r_*, A_*/r_*)^T.

The minimal radial lifting factor and its endpoint gcd are

    mu1=d kappa/(chi r_*)=d e_*/chi.                   (17)

They are integers because chi divides d and e_* divides chi. This is a formula for an endpoint gcd, not the center denominator q. Multiplication by mu1 multiplies the full remainder and its endpoint gcd equally; it contributes no additional primitive smallness.

More generally, for any primitive integer direction u, let s(u)=gcd of the two coordinates of Ru. The adjugate identity gives s(u)|chi|d, and

    mu(u)=d/s(u).

This agrees with the previously established congruence formula using Wprim. For the Bezout companion u2=(x2,y2), q x2+p y2=1, its own factor is

    mu2=d/gcd(g1 x2+g2 t y2, g2 c_perp y2).

It need not equal mu1. Their minimally lifted triples need not be a lattice basis. Their primitive endpoint determinant is nevertheless -1, and their coefficient-sublattice index is mu1 mu2 chi/d^2, a positive integer. This accounts separately for both endpoint gcds.

## 6. Divisibility restrictions from the transverse Gram determinant

In (14), v divides both A_* and H_*, and hence v divides D_*. Consequently

    A0/gcd(A0,D_*) <= q <= g1 A0.                      (18)

For g1=1 and gcd(A0,D_*)=1, this yields the exact formula q=A0. Coprimality here is a stated sufficient condition, not an assumed property of the contact family.

There is a sharper local restriction, valid at EVERY prime, including 2. Write

    alpha=v_p(A_*), beta=v_p(H_*),
    cval=v_p(g2 c_perp), delta=v_p(D_*),

with v_p(0)=infinity. Put q0=A0/gcd(A0,|H_*|). Formula (14) gives

    v_p(q0)=max(0,alpha-cval-beta),
    v_p(q0)<=v_p(q)<=v_p(q0)+v_p(g1).                  (19)

The identity D_*=A_* C_*-H_*^2, with C_* integral, implies:

* If delta<alpha, then delta is even and beta=delta/2. Thus v_p(q0)=max(0,alpha-cval-delta/2).
* If delta>=alpha, then beta>=ceil(alpha/2). Thus 0<=v_p(q0)<=max(0,floor(alpha/2)-cval).

Proof: v_p(A_* C_*)>=alpha. If 2 beta<alpha, the term -H_*^2 is uniquely least and determines delta=2 beta. Otherwise both terms have valuation at least alpha. This argument also covers H_*=0 through the infinity convention.

Primes dividing chi retain the exact final factor in (14). Outside chi, g1,g2,c_perp are units and (15) simplifies to

    v_p(q)=alpha-min(alpha,beta).

No large-prime hypothesis or transfer from an old fixed-b family is used.

The B-projected content must also be retained. Set

    m_ij=xi_i nu_j-xi_j nu_i,
    tB(lambda)=gcd_(i<j)|v_i(lambda)v_j(lambda)m_ij|.

Then Cauchy-Binet gives the exact integer decomposition

    D_*=sum_(i<j) v_i^2 v_j^2 m_ij^2
       =tB(lambda)^2 Dprim(lambda),
    Dprim(lambda) a positive integer.                 (20)

Neither tB nor Dprim is set to one. Full coefficient saturation in (8) does not remove projection content in (20).

## 7. Direct connection to the COMPLETE directional defect

The B-only defect and the complete defect are, exactly,

    rho_Sigma=Delta/U^2
             =(g2 c_perp/g1)^2 D_*/A_*^2,
    rho_G=rho_Sigma+1/(zeta U).

Combining these with the ACTUAL reduced denominator (13) yields

    q^2 rho_Sigma=(g2 c_perp)^2 D_*/kappa^2,

    q^2 rho_G=[(g2 c_perp)^2 D_*
                  +d^2 A_*/(zeta tau^2)]/kappa^2.      (21)

This is the requested structural relation between denominator cancellation and directional defect. It retains the complete pi contribution as the second positive term. A small B-only defect cannot silently replace rho_G.

The complete inequality in direction (1,0) gives a useful consistency condition stronger than the generic one. Its endpoint is one and Y=0, so

    1<=gamma sum_j |w_j Psi_(j,1)|
      <=sqrt(b+1) gamma sqrt(U).

Therefore

    eta^2 a=2(b+1)gamma^2 U>=2.                        (22)

In particular, if the center-pair quantity F=eta^2 a rho_G q^2 tends to zero, (21)-(22) force

    kappa/[(g2 c_perp)sqrt(D_*)] -> infinity.           (23)

For example, if kappa<=C (g2 c_perp)sqrt(D_*) along a subsequence, then F>=2/C^2 there and the selected center certificate cannot shrink on that subsequence. Equation (20) makes the necessary cancellation in (23) at least as strong as cancellation against the full weighted minor content. By (15), another necessary consequence is

    g1^2 r_*^2/D_* -> infinity.

These are proved necessary conditions, not assertions that the actual family meets them. They identify a concrete large-gcd requirement that entrywise inverse-denominator estimates cannot supply.

## 8. Actual weight recurrence and congruences

Fix n,b and therefore the rational lift, K, g1,g2,c_perp,t. Only m and lambda=n+m+1 vary in this section. The exact identity

    v_j(lambda+1)=v_j(lambda)+j v_(j-1)(lambda)

constructs all integer weights. The contractions A_*(lambda),H_*(lambda),C_*(lambda) are integer polynomials of degree at most 2b. The determinant has the more precise expansion (20), so its degree is at most 4b-2. Consequently forward differences satisfy

    Delta_lambda^(2b+1) A_*=0,
    Delta_lambda^(2b+1) H_*=0,
    Delta_lambda^(2b+1) C_*=0,
    Delta_lambda^(4b-1) D_*=0.                          (24)

These are all-size structural recurrences for the exact arithmetic that enters q, rather than a recurrence for an arbitrary inverse clearer. The denominator is recovered after every update by the gcd in (13); the gcd itself is not claimed to obey a linear recurrence.

For any prime p and s>=1, integer-polynomial evaluation also gives

    A_*(lambda+p^s)=A_*(lambda) mod p^s,
    H_*(lambda+p^s)=H_*(lambda) mod p^s.

It follows that the capped gcd valuation obeys

    min(s,v_p(kappa(lambda+p^s)))
      =min(s,v_p(kappa(lambda))).                      (25)

No valuation beyond the cap follows merely from (25).

There is additional explicit factorial-weight content. Every v_j for j>=1 is divisible by lambda, so

    A_*=xi_0^2 mod lambda^2,
    H_*=xi_0 nu_0 mod lambda^2,
    C_*=nu_0^2 mod lambda^2,
    lambda^2 divides D_*.                              (26)

If delta_B is the gcd of the unweighted m_ij, each weighted minor is directly divisible by lambda delta_B. Hence (lambda delta_B)^2 divides D_*. This product follows from its termwise factorization, not from multiplying overlapping divisor assertions.

In particular, if p|lambda and p does not divide xi_0, then v_p(A_*)=0 and (19) gives v_p(q)<=v_p(g1). The nonvanishing condition on xi_0 modulo p is essential.

For an optional exact bound across the same fixed-lift weight family, factor a common integer polynomial P0 from A_* and H_* so their quotient polynomials are relatively prime over Q. Integer polynomial Bezout gives a nonzero integer R with U0(A_*/P0)+V0(H_*/P0)=R. At integer lambda, the residual value gcd divides R. Thus

    r_*(lambda)=|P0(lambda)| r_res(lambda),
    r_res(lambda)|R.

This is available after retaining any actual common polynomial factor. No claim of polynomial coprimality, small R, or uniformity in n,b is made.

The analytic bound is used only for the admissible m range. Although (24)-(26) are polynomial identities for a fixed lift, they do not prove normality or a smallness estimate at other m, and they do not close a recurrence as n,b themselves grow.

## 9. Exact remaining center-pair budget

Define the positive rational scale

    Lambda0=2(b+1)(gamma tau/d)^2
           =18(b+1)L_k^2/[A_k^2 (k+1)!^2 d^2].         (27)

The equality uses gamma tau=3 L_k/[A_k(k+1)!]; all factorial common factors are accounted for exactly.

The main criterion's two quantities become

    E=eta^2 a/q^2=Lambda0 kappa^2/A_*,

    F=eta^2 det(G)q^2/a
      =[2 d_k^2 g1^2 A_*^2
         +Lambda0 chi^2 A_* D_*]/kappa^2.              (28)

The first numerator term in F is the complete pi-error contribution. The exact product is

    E F=2 Lambda0 d_k^2 g1^2 A_*
           +Lambda0^2 chi^2 D_*.                      (29)

Thus the necessary and sufficient same-index conditions for THESE TWO MAJORANTS to vanish are

    2 d_k^2 g1^2 A_*^2+Lambda0 chi^2 A_* D_*
         =o(kappa^2),
    kappa^2=o(A_*/Lambda0).                            (30)

Neither condition has been established on an unbounded contact-family sequence. The product condition from (29) alone is insufficient.

With n,b fixed, the reference recurrences also give

    Lambda0(k+1)/Lambda0(k)
      =(L_(k+1)/L_k)^2 (A_k/A_(k+1))^2/(k+2)^2,
    d_(k+1)/d_k=beta_(k+1)(A_k/A_(k+1))^2.

Together with (24) and the exact gcd update, these determine the full budget as the admissible subtraction depth changes. A decrease in the quadratic bound does not imply monotonicity of q or of its two center-pair quantities.

Any common rescaling of integer weights multiplies A_*,H_*,C_*,kappa by its square and D_* by its fourth power, with tau changed inversely when the same norm is represented. Equations (13), (21), and (28) remain unchanged. No clearance or rescaling creates an arithmetic saving.

## 10. Evidence, scope, and open arithmetic

The newly saved and inspected check_rational_center_structure.py executed successfully with exit code 0. Its real result is PASS_NEW_SYMBOLIC_IDENTITIES, with 21 checks and all six specified input hashes unchanged. It verifies formal Gram conversions, determinant and center-vector identities, E/F substitutions, shear invariance, and one abstract weight-polynomial Cauchy-Binet/finite-difference example. It computes no actual contact index or prime table. The divisibility results in this note are established by the paper proofs above, not inferred from those symbolic controls.

Supporting artifacts are rational_center_structure_checks.json and rational_center_structure_stdout.txt. The previously completed 907-check quotient audit was not executed or reopened. SLOW_GROWTH_NORMALITY_REVIEW.md and both earlier endpoint-lattice documents remain preserved.

Substantive new results are: the actual smaller adjugate construction of the center arithmetic; exact removal of common factorial scales; a saturated full-coefficient basis with all endpoint scales; formulas (13)-(17) separating the center denominator and its own radial endpoint gcd; primewise determinant restrictions; the complete defect identity (21) and necessary large-gcd condition (23); and the fixed-lift weight recurrences and congruences (24)-(26).

What remains open is control of the actual weighted contractions and their gcd on an unbounded normal sequence, sufficient to prove both limits in (30). Neither random coprimality, a lift clearer, lattice covolume, nor the inverse paper's orientation estimate resolves that question. No conclusion about the rationality or irrationality of e+pi is claimed.
