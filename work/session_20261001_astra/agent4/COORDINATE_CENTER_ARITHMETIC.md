> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Coordinate centers of the actual relaxed B lift

Status: exact paper results, with an unconditional rational coordinate-selection rule on the reviewed slow-growth domain. Useful denominator asymptotics remain open. The approximation estimate uses precisely the limited inverse/log(2) review saved in LOG_TWO_INVERSE_REVIEW.md. No old audit, checker, prime table, or contact solve is repeated.

Use integers n>=16, 3<=b<=n, n>=512 b^4 log n and 1<=m<=floor((b-1)/2). The coordinate arithmetic itself applies whenever the rational endpoint lift exists. All logarithms are natural.

Let Phi be the full rational endpoint-to-coefficient lift and Psi its B block. Put

    u=Psi(1,0), v=Psi(0,1), S=e+pi,
    lambda=n+m+1,
    omega_j=(lambda)_j, omega_0=1,
    tau=(lambda-b)!/lambda!, w_j=tau omega_j.

Then sum_j u_j=0 and sum_j v_j=1. The weights are exactly those of the multi-row complete-bound paper, not a full A/B/C norm. Psi is injective. In particular u is nonzero.

For every u_j!=0 the rational coordinate center is

    t_j=v_j/u_j.

This center is independent of the choice of weights or subtraction depth m at fixed n,b. Its analytic eligibility can depend on m. The weighted Gram center generally changes with m and is a different rational number.

## 1. Exact weighted-vector comparison and a rational selection rule

Define

    a_j=w_j u_j,
    r_j_an=w_j(v_j-Su_j),
    U=sum_j a_j^2>0,
    epsilon_vec=||r_an||_2/sqrt(U).

For u_j!=0 set C_j=sqrt(U)/|a_j|. Then, exactly,

    |t_j-S|=|r_j_an|/|a_j|<=C_j epsilon_vec.            (1)

The limited inverse review proves epsilon_vec<=delta_n, where

    delta_n=n^(10b)[2^(-n)+2(M/2)^n/n!],
    M=1+sqrt(2),
    log delta_n=-n log 2+o(n)

uniformly on the stated domain. This is an upper envelope only.

A maximum of a_j^2 over all coordinates has C_j<=sqrt(b+1). There is a stronger actual-family rule that avoids coordinate zero. From sum_j u_j=0,

    a_0=-sum_(j=1)^b a_j/omega_j.

Put the positive rational number

    c_lambda=sum_(j=1)^b omega_j^(-2)<=b/lambda^2.

Cauchy-Schwarz gives a_0^2<=c_lambda sum_(j=1)^b a_j^2. Therefore a maximum of a_j^2 over j=1,...,b satisfies

    C_j<=Csel:=sqrt(b(1+c_lambda))<sqrt(b+1).          (2)

The strict inequality follows from lambda>b. In particular the rationally defined eligible set

    Jelig={j in {1,...,b}: b(1+c_lambda)a_j^2>=U}       (3)

is nonempty, and every member has u_j!=0. No value of S is used to construct it. Among its members one may choose the smallest actual reduced denominator, resolving ties by the smallest coordinate index. Equations (1)-(3) still apply to that choice.

The resulting complete scalar error bound is

    |t_j-S|<=delta_coord,n:=Csel delta_n.               (4)

The selection cost is retained. Since log Csel=o(n), the explicit coordinate envelope has the same exponential rate log 2. This is a proved estimate for an actual-family eligible coordinate; it supplies no useful denominator growth estimate by itself.

## 2. Smaller Toeplitz adjugate and actual denominators

Use the b by b Toeplitz matrix T and both actual endpoint forcing columns fP,fQ from the retained exact contact inverse. Let

    Aop=D_B(D+1)^(-n),

where D_B multiplies a degree-less-than-b polynomial by z-1. The finite inverse differential operator has integer ascending-coefficient entries

    [(D+1)^(-n)]_(j,j+l)
      =(-1)^l binom(n+l-1,l)(j+l)!/j!.

Thus Aop is an integer (b+1) by b matrix. Exact reconstruction is

    Psi=Aop T^(-1)[fP fQ]+e0 e2^T.                    (5)

Choose positive integer row clearers making T_hat and both columns of F_hat integral. Set

    Delta=det T_hat!=0,
    N=Aop adj(T_hat)F_hat+Delta e0 e2^T.

Then

    Psi=N/Delta,
    sum_j N_(j,1)=0, sum_j N_(j,2)=Delta.              (6)

For N_(j,1)!=0 define hN_j=gcd(|N_(j,1)|,|N_(j,2)|). The fully reduced coordinate fraction is

    p_j=sgn(N_(j,1)) N_(j,2)/hN_j,
    q_j=|N_(j,1)|/hN_j>0.                             (7)

The common inverse denominator Delta cancels. The weights also cancel from t_j and q_j. Enlarging the row clearers multiplies N and Delta by the same integer, and both numerator and gcd in (7) scale together. No saving is credited to this enlargement.

The selection rule can be evaluated directly from N: compare omega_j^2 N_(j,1)^2, using the rational threshold from (3). All common factors tau^2/Delta^2 cancel from eligibility.

For the guaranteed eligible coordinates j>=1 there is no additive endpoint term in the second numerator. Let aop_j be row j of Aop. Then

    N_(j,s)=aop_j adj(T_hat) f_hat_s, s=1,2.           (8)

Each is exactly the integer bordered determinant with top block [T_hat,f_hat_s] and bottom row [-aop_j,0]. This reduces q_j to a gcd of two LINEAR bordered contractions. It contains no sum of squared lift entries.

For i,j>=1 let B_ij be the determinant of the (b+2) by (b+2) integer matrix with top block [T_hat,F_hat] and bottom rows [-aop_i,0,0],[-aop_j,0,0]. Schur complementation gives

    det N_[i,j]=Delta B_ij.                            (9)

Thus Delta divides every such two-row minor. The sign in (9) corresponds to the displayed negative bottom rows. The identity is an actual-family fraction-free divisibility relation, not an assertion of coprimality.

## 3. Saturated basis and coordinate slices

Retain the proved saturated factorization from RATIONAL_CENTER_ARITHMETIC.md:

    Phi=(1/d)K R0,
    K=[x,z],
    R0=[[g1,g2 t],[0,g2 c]],
    chi=g1 g2 c, chi|d.

Here d is the intrinsic full-lift denominator, g1,g2,c are positive integers, t is an integer, and K is an integral basis of the saturated coefficient kernel. The integer t here is not a rational center. Its full two-column maximal-minor gcd is one. Let xi,nu be the B blocks of x,z. Then

    u_j=g1 xi_j/d,
    v_j=g2(t xi_j+c nu_j)/d.                           (10)

For xi_j!=0 put

    h_j=gcd(g1|xi_j|, |g2(t xi_j+c nu_j)|),
    r_j=gcd(|xi_j|,|nu_j|)>0.

Then

    q_j=g1|xi_j|/h_j,
    p_j=sgn(xi_j)g2(t xi_j+c nu_j)/h_j.                (11)

There is an exact separation of the content:

    h_j=r_j e_j, e_j|chi.                              (12)

Indeed (xi_j/r_j,nu_j/r_j) is a primitive integer row. Multiplication by R0 gives a row whose coordinate gcd is e_j. Applying adj(R0), and using primitivity, shows that e_j divides det R0=chi. Thus, outside primes dividing chi,

    v_p(q_j)=max(0,v_p(xi_j)-v_p(nu_j)),               (13)

with v_p(0)=infinity. This involves two actual linear coordinates, not weighted quadratic contractions. At primes dividing chi, (11)-(12) retain the full extra cancellation.

The coordinate center has a direct interpretation in the coefficient lattice. The unique primitive coefficient vector in the slice B_j=0 is, up to sign,

    K(-nu_j/r_j,xi_j/r_j)^T.                           (14)

Its primitive endpoint direction is (-p_j,q_j). The minimal positive radial factor making the rational lift of that direction integral, and hence the endpoint gcd of the primitive coefficient triple, is

    mu_j=d h_j/(chi r_j)=d e_j/chi.                    (15)

For sign precision, Phi(-p_j,q_j)^T equals sgn(xi_j)chi/(d h_j) times K(-nu_j,xi_j)^T. Equation (15) follows because K is saturated and preserves the gcd of an integer two-vector. It is integral since chi|d. Its multiplication of the full remainder cancels against the same endpoint gcd. In particular mu_j is not q_j.

For the Bezout companion (x2,y2), q_j x2+p_j y2=1, its separate radial factor is

    mu2=d/gcd(g1 x2+g2 t y2, g2 c y2).

This can differ from mu_j. The primitive endpoint determinant is -1, regardless of the two radial factors; the integral coefficient lifts need not form a lattice basis.

The adjugate and saturated constructions agree exactly:

    hN_j=|Delta|h_j/d.                                 (16)

This follows by factoring a primitive integer row from the two coordinates in (10). Although its right side is an integer, |Delta|/d need not be integral. That rational scale must not be discarded before cancellation.

## 4. Projected minors and a sharper exceptional-prime set

Define

    m_ij=xi_i nu_j-xi_j nu_i,
    betaB=gcd_(i<j)|m_ij|>0,
    M_j=gcd_i |m_ji|>0 for xi_j!=0.

Positivity of betaB and M_j follows from rank two of the B projection and nonzero row j. Full coefficient saturation does not assert betaB=1.

There is an exact divisor

    ell_j=M_j/r_j, ell_j|betaB.                        (17)

Proof: the rows (xi_i,nu_i) generate a full-rank sublattice L_B of Z^2 of index betaB. The primitive row (xi_j/r_j,nu_j/r_j) defines a surjective determinant functional Z^2 to Z. Its image on L_B is ell_j Z. Hence the group Z^2/L_B surjects onto Z/ell_j Z, so ell_j divides betaB.

Combining (11), (12), and (17) gives

    q_j=g1|xi_j| ell_j/(e_j M_j),
    e_j|chi, ell_j|betaB.                              (18)

For example this implies the genuine bounds

    |xi_j|/(g2 c M_j) <= q_j <= g1 betaB |xi_j|/M_j.

Outside primes dividing chi betaB, the local formula is exact:

    v_p(q_j)=v_p(xi_j)-v_p(M_j).                       (19)

The actual endpoint rows further restrict betaB. From E Phi=I and the saturated factorization,

    EK=[[d/g1,-dt/(g1 c)],[0,d/(g2 c)]].

Consequently

    sum_i xi_i=0,
    sum_i nu_i=s0=d/(g2 c), an integer.

Let hxi=gcd_i |xi_i|>0. Every projected minor is divisible by hxi. Conversely, summing m_ij over j gives s0 xi_i. Taking gcds proves

    hxi|betaB|s0 hxi,
    betaB=hxi beta0, beta0|s0.                         (20)

Since s0 divides d and chi divides d, all exceptional primes in (19) are confined to d hxi. In particular, for EVERY prime p not dividing d hxi,

    v_p(q_j)=v_p(xi_j)-v_p(M_j).                       (21)

This is an actual-family restriction using the exact endpoint sums. It preserves the possible additional B-projection content hxi instead of assuming its absence. No random-coprimality hypothesis is used.

Equations (18)-(21) make the residual arithmetic question more concrete: estimate one eligible linear coordinate and the gcd of the unsquared projected minors involving its row, with any extra local factors supported on the stated set. They do not yet bound these quantities as n,b grow.

## 5. Pairwise separation and denominator restrictions

For any two coordinates with nonzero first-column entries,

    h_i h_j divides chi m_ij.                          (22)

Indeed the two rows (g1 xi_i,g2(t xi_i+c nu_i)) and their j counterparts have determinant chi m_ij; dividing each by its row gcd leaves an integer determinant. If m_ij!=0, then

    q_i q_j |t_i-t_j|=chi|m_ij|/(h_i h_j)              (23)

is a positive integer. Thus distinct eligible coordinates obey

    q_i q_j >=1/[(C_i+C_j)delta_n].                    (24)

This is conditional on their being distinct, equivalently on m_ij!=0. Rank two of Psi does not imply that a given eligible set contains two distinct coordinate quotients. An index with a zero minor is not assigned a positive separation.

For varying approximation indices, the same elementary rational-separation argument applies whenever the selected centers differ. It is a constraint on possible simultaneous denominator bounds, not a proof of denominator growth or nonstabilization.

## 6. Exact comparison with the Gram center

Let W=diag(w_j^2), Sigma=Psi^T W Psi, and theta_G=Sigma12/Sigma11. With U=sum_j(w_j u_j)^2 and

    alpha_j=(w_j u_j)^2/U for u_j!=0,

the exact identity is

    theta_G=sum_(u_j!=0) alpha_j t_j,
    alpha_j>0, sum alpha_j=1.                          (25)

Thus the Gram center is a rational convex combination of the coordinate quotients. It need not equal any one of them, and (25) does not transfer their denominators to the Gram denominator.

There is also the exact defect decomposition

    det(Sigma)/U^2
      =sum_(u_j!=0) alpha_j(t_j-theta_G)^2
        +sum_(u_j=0)(w_j v_j)^2/U.                    (26)

It follows by expanding the norm squared of W^(1/2)(v-theta_G u). The last term is essential when some first-column entries vanish. In particular,

    |t_j-theta_G|<=C_j sqrt(det(Sigma)/U^2).            (27)

The multi-row COMPLETE Gram matrix is G=2[e2 e2^T+zeta Sigma]. It has the same rational center as Sigma, but its normalized defect is

    det(G)/G11^2=1/(zeta U)+det(Sigma)/U^2.

The extra term is not removed in a complete quadratic certificate. The direct envelope in (4) instead bounds the signed complete forcing residual before evaluating the rational direction. Necessary conditions derived for a separated-tail quadratic majorant must not be transferred to (4) without proof.

The full-coefficient Gram matrix in CONTACT_INVERSE_RESEARCH.md contains additional A/C terms and generally has a further different center. No norm comparison alone makes these centers equal.

## 7. The separately mentioned direct forcing quotient

The direct forcing ratio tF=fQ_0/fP_0 is a third rational object. The retained positive forcing lower bound gives fP_0>0. Its relationship to an eligible Psi-coordinate quotient follows from (5), without reading or reviewing another proof.

For j>=1 put ellrow_j=aop_j T^(-1). Then

    t_j=(ellrow_j fQ)/(ellrow_j fP),

and

    t_j-tF
      =ellrow_j(fP_0 fQ-fQ_0 fP)
           /[fP_0(ellrow_j fP)].                      (28)

The denominator is nonzero for the selected coordinate. Equality would require the numerator in (28) to vanish; it is not automatic. At coordinate zero, the additive constant in (5) must also be included.

For tF itself, clearing the two scalar entries fP_0,fQ_0 by a common positive integer gives its own denominator |A_F|/gcd(|A_F|,|B_F|). This elementary reduction does not identify it with (7) or (11). No result from SCALAR_FORCING_CENTER_DRAFT.md is imported or independently reviewed here. Equation (28) is solely a comparison derived from the already assigned forcing/reconstruction identities.

## 8. Precisely remaining arithmetic and primitive-form conditions

For any selected eligible center t_j=p_j/q_j, q_j>0, choose q_j x2+p_j y2=1 with |y2|<=q_j/2. The two primitive independent endpoint directions obey the complete bounds

    |-p_j+q_j S|<=q_j delta_coord,n,
    |x2+y2 S|<=1/q_j+q_j delta_coord,n/2.              (29)

Their determinant is -1. Their separate polynomial lifting factors cancel against their separate endpoint gcds as described in Section 3. No individual nonzero-remainder theorem is required for the paired rationality contradiction.

Sufficient same-index conditions are

    q_j -> infinity,
    q_j delta_coord,n ->0.                            (30)

A strict upper exponential rate limsup log(q_j)/n<log 2 together with divergence suffices. In saturated coordinates the exact window is

    g1|xi_j| delta_coord,n=o(h_j),
    h_j=o(g1|xi_j|).                                   (31)

For the rational selection minimizing q_j over Jelig, the unresolved upper estimate concerns exactly

    min_(j in Jelig) |N_(j,1)|/
           gcd(|N_(j,1)|,|N_(j,2)|),

or equivalently (18) on that same eligible set. Divergence is a separate requirement; choosing the minimum does not establish it.

What is proved for the actual family is the nonempty rational eligibility rule with cost (2), the complete error bound (4), the actual smaller-adjugate and saturated denominator formulas, the coordinate-slice endpoint-gcd formula, and the unsquared projected-minor restrictions including (20)-(21). The linear contraction sizes, their local gcds on an eligible sequence, and the limits (30) remain unresolved. These precise open conditions replace a claimed denominator theorem.

The completed Gram-center arithmetic and its 21 checks are preserved and not rerun. The older 907-check quotient audit is also closed. The current new results are paper deductions; no new actual contact-family numerical evidence is asserted. A failed sufficient bound is not an exclusion of small actual forms, and no conclusion about the rationality or irrationality of e+pi is obtained.
