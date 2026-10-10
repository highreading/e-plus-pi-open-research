> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Double-pole short kernel: complete quadratic sign and two-root error

Author theorem: Agent 3 / analysis, 2026-10-02. Fresh gate: DOUBLE_POLE_SHORT_RECTANGULAR_GATE.md. Root owns the exact compact moments, full matching-kernel rank, rational coefficient clearers, primitive polynomial content, and polynomial-transcendence transfer. This note proves original analytic coercivity and COMPLETE determinant/root scales; it is not an audit or a rational-center assertion.

## 1. Actual determinant and the result

Let mu be the probability pushforward of exp(-t)dt, t>=0, under y=(1-t)^2. Define the value/derivative functional

    nu(f)=f(-1)+2f'(-1),
    nu_r=nu(y^r)=(-1)^r(1-2r),
    rho=mu-nu,
    dsigma_2(y)=[exp(sqrt(y))+8/(1+y)^2]dy/[2sqrt(y)], 0<y<1.

Thus mu(y^r)=D_(2r). For 0<=i<k, 0<=j<2k, the exact equal-response upper block is C_ij=rho(y^(i+j)). Root's exact compact moment formula is

    L_ij=sigma_2(y^(i+j))=e C_ij+R_ij+S V_ij,
    S=e+pi,  V_ij=nu_(i+j).

The actual determinant is therefore

    beta_k(s)=det[C;R+sV]=beta_0+beta_1 s+beta_2 s^2,            (1)
    beta_k(S)=det[C;L].

The last equality is the determinant-preserving upper-row subtraction of eC. It does not omit eC entrywise. The response's jet matrix is

    nu(fg)=[f(-1),f'(-1)] [[1,2],[2,0]] [g(-1),g'(-1)]^T,

with determinant -4 and rank two. Hence degree<=2 in (1) is exact algebra; positivity is not assumed from this indefinite matrix.

Root records the exceptional k=1: D_0=D_2=nu_0=nu_1=1, so C=[0,0] and the fixed 1-by-2 stacked determinant vanishes identically. The theorem below begins at k>=100; it uses no claim about k=1. Root proves full row rank for every k>=2 separately.

**Complete analytic theorem.** For EVERY k>=100, beta_k has degree EXACTLY two, and

    sign beta_k(S)=(-1)^k,
    sign beta_k'(S)=sign beta_2=(-1)^(k+1).                    (2)

There are two distinct REAL roots s_(k,-)<S<s_(k,+). Let Lambda_k be the positive exterior Christoffel minimum at y=-1 for the ACTUAL compact measure sigma_2 and degrees <k. Then, with absolute positive comparison constants independent of k,

    s_(k,+)-S is comparable to Lambda_k/k,
    S-s_(k,-) is comparable to k Lambda_k,
    -beta_k(S)/beta_2 is comparable to Lambda_k^2.             (3)

In particular BOTH roots converge to S, with full signed errors, and

    log(s_(k,+)-S)=-4k log(1+sqrt(2))+O(log k),
    log(S-s_(k,-))=-4k log(1+sqrt(2))+O(log k),
    log|beta_k(S)/beta_2|
                          =-8k log(1+sqrt(2))+O(log k).        (4)

Their error ratio has order k^2. These are algebraic approximants, not automatically rational centers.

If Pi_k(s)=A_0+A_1s+A_2s^2 is Root's FINAL PRIMITIVE integer polynomial proportional to beta_k, then Pi_k(S)!=0 and

    log|Pi_k(S)|=log|A_2|-8k log(1+sqrt(2))+O(log k).            (5)

This retains all actual coefficient clearers and evaluated common content in A_2. No growth law for A_2, favorable gcd, or rationality theorem is inferred.

## 2. Finite tail coercivity retaining BOTH jet terms

Fix ANY k-1 nodes x_i in [-1,1], put Q(y)=product_i(y-x_i), and consider eta=Q rho on polynomials of degree <k. The inherited positive tail interval is I=[k^2,4k^2]. With

    L(p)=sup_[-1,1]|p|^2,
    C_k=3exp(-2k-1)(k^2-1)^(k-1)/[4k16^(k-1)],

the exterior Legendre evaluation estimate gives the positive tail at least C_k L(p), exactly as in the preceding short-family proof. It is valid on all of [-1,1], not just its right half. The compact continuous loss is at most 2^(k-1)L.

Markov's inequality on [-1,1] gives |p'(-1)|<=(k-1)^2 sqrt(L). Also

    |Q(-1)|<=2^(k-1),  |Q'(-1)|<=(k-1)2^(k-2).

The COMPLETE discrete modification is

    nu(Qp^2)=[Q(-1)+2Q'(-1)]p(-1)^2
                                  +4Q(-1)p(-1)p'(-1).        (6)

Its absolute value is at most 2^(k-1)[k+4(k-1)^2]L. Together with the compact loss, the total negative bound is at most 2^(k+1)k^2 L. For k>=100,

    C_k/2^k >4(3/2)^k/[k(k^2-1)]>2k^2.                      (7)

The stronger inequality 2(3/2)^k>k^5 holds at 100 by the integer inequality 2·3^100>2^100·100^5; its ratio for successive indices exceeds one because (3/2)(k/(k+1))^5>1 for k>=100. It implies the second inequality in (7). Thus eta(p^2)>0 for every nonzero deg p<k, uniformly in ALL node configurations.

For conditional roots, set a=1/(48e^4), A=ak^2>=2, and L_A=sup_[-1,A]|p|^2. Markov on this longer interval gives

    |p'(-1)|<=2(k-1)^2 sqrt(L_A)/(A+1).

For w=(y-A)Qp^2, BOTH jet terms obey

    |nu(w)|<=2^(k-1)[(A+1)k+2+8(k-1)^2]L_A.                 (8)

This is no greater than 11k^2 times the old value-atom bound (A+1)2^(k-1)L_A. The negative continuous contribution is at most A(A+1)^(k-1)L_A. Let

    N_0=[A(A+1)^(k-1)+(A+1)2^(k-1)]L_A,
    T_0=(k^2-A)C_k L_A.

The complete negative bound is at most 11k^2 N_0. The established elementary tail calculation gives

    T_0/(11k^2 N_0)
      >=(1-a)exp(2k-4)/(44e a k^3)
       >2^(2k-4)/(3k^3)>1, k>=100.                          (9)

The last inequality holds at 100 and increases with k. Therefore eta((y-A)p^2)>0. The positive truncated Gram's symmetric multiplication compression has all k eigenvalues z_i>A. The derivative correction has not been discarded or replaced by positive separate squared derivative masses.

## 3. Exact full determinant and inverse normalization

For k nodes x define

    F_k(x)=det M_[rho product_i(y-x_i),k].

The finite characteristic identity for the final node u is

    F_k(x_1,...,x_(k-1),u)=det M_(eta,k) product_i(z_i-u).

Consequently F_k(x)>0 on [-1,1]^k, and each insertion obeys

    exp(-4k/A)<=F_k(x,u)/F_k(x,-1)<=1.

The all-minus-one reference is

    F_k^*=F_k(-1,...,-1)=det M_[mu(y+1)^k,k]>0,

because k>=2 annihilates BOTH value and derivative evaluation. Replacing the nodes successively gives

    L0<=F_k(x)/F_k^*<=1,
    L0=exp(-4/a),  x in [-1,1]^k.                            (10)

All integral identities below are finite polynomial moment identities. The derivative-evaluation functional may be applied directly to their polynomial integrands; no measure representation of its indefinite jet matrix is required. Double Andreief gives

    beta_k(S)=(-1)^k/k! integral_[0,1]^k
                   Vandermonde(x)^2 F_k(x) d sigma_2^k.       (11)

The strict positive integral proves its full sign and nonzero value, with both actual endpoint densities retained.

## 4. Single and DOUBLE confluent response coefficients

Write t=s-S and differentiate the lower functional sigma_2+t nu. For k-1 compact nodes x, let

    H_x(u)=product_i(u-x_i)^2 F_k(x,u).

The first response is EXACTLY

    beta_k'(S)=(-1)^k/(k-1)! integral Vandermonde(x)^2
                                      nu_u(H_x(u)) d sigma_2^(k-1).

The full derivative factor is

    nu_u(H_x)=H_x(-1)[1-4sum_i1/(1+x_i)-2sum_j1/(1+z_j)].     (12)

The last sum is over the exact conditional roots from Section 2. Thus for k>=100, putting d_x equal to the NEGATIVE of the bracket,

    k<=2k-3<=d_x<=4k-5+2/(ak)<=5k.                           (13)

This establishes sign beta_k'(S)=(-1)^(k+1), and controls the derivative response normalization without ignoring either value or derivative evaluation.

For two inserted lower nodes u,v, the integrand contains (v-u)^2. At u=v=-1, value and single-derivative terms vanish, but

    nu_u nu_v[(v-u)^2 H(u,v)]|_(u=v=-1)=-8H(-1,-1).

The expansion coefficient has the combinatorial factor 1/[2!(k-2)!], so the coefficient of t^2, equivalently beta_2, is

    beta_2=(-1)^(k+1)4/(k-2)! integral_[0,1]^(k-2)
        Vandermonde(x)^2 product_i(1+x_i)^4
                       F_k(x,-1,-1) d sigma_2^(k-2).         (14)

Its integrand is strictly positive, and

    F_k(x,-1,-1)=det M_[mu(y+1)^2 product_i(y-x_i),k].

The factor (y+1)^2 kills BOTH upper jet terms. In contrast, a SINGLE factor leaves

    (y+1)rho=(y+1)mu-2delta_-1,

which is kept in (12). Formula (14) includes the negative determinant of the jet matrix and the exact factor 4; it is not two ordinary positive atoms.

Define positive normalized coefficients

    D=(-1)^k beta_k(S),
    B=(-1)^(k+1) beta_k'(S),
    C=(-1)^(k+1) beta_2.

Equations (11)--(14) prove D,B,C>0 and

    (-1)^k beta_k(S+t)=D-Bt-Ct^2.                            (15)

Hence the discriminant is strictly positive and there are two distinct real roots on opposite sides of S.

## 5. Reference jet determinant and its uniform conditioning

Let G be the k-dimensional positive sigma_2 moment Gram, v_i=(-1)^i, u_i=i(-1)^(i-1), and

    K=[[v^T G^(-1)v, v^T G^(-1)u],
       [u^T G^(-1)v, u^T G^(-1)u]].

Its determinant is positive for k>=2. The exact ordinary positive insertion integrals satisfy

    D_sigma=det G,
    B_sigma=det G·K_00,
    C_sigma=det G·det K
       =1/(k-2)! integral Vandermonde^2 product_i(1+x_i)^4 d sigma_2^(k-2).

Put Lambda_k=1/K_00. The actual complete coefficient bounds from (10), (13), and (14) are

    L0 F_k^* D_sigma<=D<=F_k^* D_sigma,
    L0 k F_k^* B_sigma<=B<=5k F_k^* B_sigma,
    4L0 F_k^* C_sigma<=C<=4F_k^* C_sigma.                     (16)

The necessary uniform jet conditioning is

    det K is comparable to K_00^2.                          (17)

Here is an elementary proof, avoiding an assumed confluent asymptotic. Compare sigma_2 to dgamma=y^(-1/2)dy:

    m dgamma<=d sigma_2<=M dgamma,
    m=3/2,  M=(e+8)/2.

The full 2-by-2 kernel matrices obey M^(-1)K_gamma<=K<=m^(-1)K_gamma in the Loewner order. It suffices to prove (17) for gamma.

For gamma, let p_l be its shifted Jacobi polynomials, a_l=(2l+1/2)[P_l^(-1/2,0)(3)]^2, and d_l=p_l'(-1)/p_l(-1). Then

    K_(gamma),00=sum_l a_l,
    det K_gamma/K_(gamma),00^2
            =variance of d_l under probabilities a_l/sum a_l.

The exact positive binomial sum and three-term Jacobi recurrence give, for every l>=1,

    1/7<=P_(l-1)^(-1/2,0)(3)/P_l^(-1/2,0)(3)<=2/3.

For the upper ratio, term comparison gives l/[2(l-1/2)]<=2/3 for l>=2, while l=1 has exact ratio 1/2. For the lower ratio, the standard recurrence has 0<A_n<2, 0<B_n<1, C_n>0 at n>=1, so P_l(3)<7P_(l-1)(3); l=1 is again explicit. It follows that

    1/245<=a_(l-1)/a_l<=4/9.                                (18)

The positive compact Jacobi zeros interlace in (0,1). Writing d_l as minus the sum of 1/(1+zero), this interlacing gives EXACTLY

    1/2<=d_(l-1)-d_l<=1.

Thus the probabilities of the top degree j=k-1 and degree j-1 have product at least (5/9)^2/245, while a degree j-r has probability at most (4/9)^r. The variance is consequently bounded by

    25/79380 <=det K_gamma/K_(gamma),00^2
                                   <=sum_(r>=0) r^2(4/9)^r=468/125.  (19)

Loewner comparison proves (17) for the ACTUAL compact weight, with lower constant (m/M)^2·25/79380 and upper constant (M/m)^2·468/125. This retains both jet channels and prevents an unproved confluent inverse-conditioning loss.

## 6. Complete root scales and primitive polynomial interface

From (16)--(19),

    D/B is comparable to Lambda_k/k,
    B/C is comparable to k Lambda_k,
    D/C is comparable to Lambda_k^2,
    eta_k=CD/B^2 is comparable to 1/k^2.                      (20)

The exact roots of (15) therefore satisfy

    s_(k,+)-S=2D/[B+sqrt(B^2+4CD)]
                 =(D/B)[1+O(k^(-2))]>0,
    S-s_(k,-)=[B+sqrt(B^2+4CD)]/(2C)
                 =(B/C)[1+O(k^(-2))]>0.                     (21)

The implicit constants are absolute and may be large because L0 was deliberately coarse. This proves the genuine k^2 directional separation in (3). Their distance product is exactly D/C=-beta_k(S)/beta_2.

The actual compact Christoffel minimum compares to the Jacobi reference, whose exact sum is

    Lambda_gamma=1/sum_(l=0)^(k-1)
                          (2l+1/2)[P_l^(-1/2,0)(3)]^2.

Its established fixed-exterior scale gives

    log Lambda_k=-4k log(1+sqrt(2))+O(log k).

Alternatively, that rate follows directly from the same positive binomial sum by Stirling maximum-term bounds. Combining with (20)--(21) proves (4) and the complete primitive formula (5).

As both actual roots tend to S, the primitive polynomial's normalized coefficients additionally satisfy

    A_1/A_2 -> -2S,  A_0/A_2 -> S^2.

Thus its coefficient height H(Pi_k) is comparable to |A_2| (indeed H/|A_2| tends to S^2), so (5) can equivalently use log H(Pi_k)+O(1). This is a normalized analytic statement, not a growth estimate for that final primitive height. Root's exact coefficient content and arithmetic transfer remain necessary.

The theorem excludes neither the whole construction family nor the rationality of e+pi. It supplies a strictly nonzero complete quadratic at S, two controlled signed algebraic approximants, and the exact arithmetic quantity the primitive polynomial method must price.

Bounded reference sanity receipt: double_pole_reference_jet_checks.py saved DOUBLE_POLE_REFERENCE_JET_RECEIPT.json. Thirty exact adjacent Jacobi weight/slope checks and thirty exact variance bounds passed. They concern the classical reference only, and do not recheck Root's full-stack certificates or certify excluded small k. The all-index assertions are proved above.
