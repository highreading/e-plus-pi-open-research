> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Primitive content of the exceptional canonical deficit

Original author research, offline; not independently reviewed. This continues CANONICAL_OVERLAP_DEFICIT.md for the SAME b=3,m=1 factorial B-only Gram center. That note, its exact factorization delta=delta_F delta_exc, and the completed seed and modulo-121 transfer are preserved. No earlier calculation or control is replayed.

The new result removes common matrix scalars before evaluating the binary forms, separates a uniformly O(n) logarithmic factor, and identifies the remaining prime-power condition. A uniform factorial-scale upper bound is proved. The sharper target log delta_exc=o(n log n) remains open. Nothing here controls the separate delta_F.

## 1. Retained data and domain

Use the integer data and conventions of CANONICAL_OVERLAP_DEFICIT.md:

    F=(n!)^2, d0=(n+1)(n+2), e=4(n+2),
    Drow=diag(1,n+1,d0),
    M=2^n n! Drow T, Delta=det M!=0,
    K=Krec=Z(I+D)^(-n),
    C=K adj(M)Drow,
    Omega=diag(((n+2)_j)^2), 0<=j<=3,
    L=2^(2n+1)lcm(1,...,2n+2).

All algebraic statements hold for n>=3 with nonsingular T. For asymptotic conclusions take sufficiently large even n in the retained fixed-b normality domain n>=512*3^4 log n. The retained convergence of the actual center to e+pi>0 permits restriction to its nonzero values; this ensures the sum row used below is nonzero. No new nonvanishing theorem is inferred from finite data.

Keep the two positive-forcing columns

    j0=(4(n+2),2(n+2),2(n+1))^T,
    j1=(0,n+2,2n+3)^T,
    Jpair=[j0 j1],
    Rmat=C Jpair,
    Zmat=C^T Omega Rmat.

The retained exponential integer column is Ecal. The retained integer logarithmic moment row is theta, using the uniform clearer L above. Define

    Bform(X,Y)=(X,Y)Rmat^T Omega Rmat(X,Y)^T,
    urow=L Ecal^T Zmat,
    vrow=d0(L Delta e0^T Rmat+F theta Zmat).

In particular the endpoint correction is present in vrow. We do not investigate the main agent's separate complete-numerator estimates.

For t0=gcd(P_n,P_(n+1)) and the primitive pair

    w=(P_n/t0,P_(n+1)/t0)^T,

let Dstar=F d0 L t0 Bform(w). The original companions are

    alpha=e urow w/Dstar,
    gamma=e vrow w/Dstar.

The preceding note removes common row content and a final evaluated gcd to obtain D2,U,V,Wcancel=U+V, with

    gcd(D2,U,V)=1,
    delta=gcd(D2,|Wcancel|),
    delta_F=gcd(F,delta), delta_exc=delta/delta_F.

Its starting restriction is

    delta_exc divides gcd(d0 L t0 a_B c_H Rresultant,|Wcancel|),

where a_B=content(Bform), u0+v0=c_H(H0,H1), and

    Rresultant=Bprim(-H1,H0)>0.

Coefficient content of a binary quadratic includes its actual XY coefficient, including the factor two from the symmetric Gram matrix.

## 2. Primitive matrices and a stronger integral scalar identity

For a nonzero integer matrix, content means the positive gcd of all its entries. Set

    k_C=content(C), Cbar=C/k_C,
    k_R=content(Cbar Jpair),
    Rbar=Cbar Jpair/k_R,
    Zbar=Cbar^T Omega Rbar,
    Bbar(X,Y)=(X,Y)Rbar^T Omega Rbar(X,Y)^T.

Both Cbar and Rbar have entry content one. They retain ranks three and two respectively. These definitions take place before evaluation at w.

The reconstruction K has an integer left inverse. Indeed division by t-1 on integer coefficient vectors of sum zero is given by integer partial sums, and (I+D)^n is integral and inverts (I+D)^(-n). Consequently

    content(C)=content(adj(M)Drow).

In particular the stronger scalar divisibility

    k_C divides |Delta|                                           (1)

holds: multiply adj(M)Drow by the integer matrix M to obtain Delta Drow, whose first diagonal entry is Delta. Define the integer

    b_Delta=d0 Delta/k_C.

The weaker divisibility k_C|d0 Delta would suffice below, but (1) also constrains the remaining lattice content.

Define the two integer rows

    uhat=L Ecal^T Zbar,
    vhat=L b_Delta e0^T Rbar+F d0 theta Zbar.                     (2)

The first term of vhat is the endpoint correction. Exact scalar factorizations give

    Rmat=k_C k_R Rbar,
    Zmat=k_C^2 k_R Zbar,
    Bform=k_C^2 k_R^2 Bbar,
    urow=k_C^2 k_R uhat,
    vrow=k_C^2 k_R vhat.                                        (3)

No statement about favorable evaluated gcds has been used.

A further divisibility isolates the possible size of k_R. Put

    eta_n=content(Drow Jpair)=(n+2)gcd(4,n+1).

Writing Aint=adj(M)Drow/k_C, one has M Aint=(Delta/k_C)Drow. The integer left inverse of K shows that k_R is also content(Aint Jpair). Therefore

    k_R divides (|Delta|/k_C) eta_n,
    eta_n<=4(n+2).                                              (4)

This is a support and depth restriction, not a smallness assertion for k_R.

## 3. Exact cancellation of the common scalar, including the final gcd

Let shat be the joint positive content of the four entries of uhat,vhat. The old joint row content is exactly

    s=k_C^2 k_R shat,
    u0=uhat/shat, v0=vhat/shat.

Define

    Dtilde=F d0 L t0 k_R Bbar(w),
    g1=gcd(Dtilde,e shat),
    D1=Dtilde/g1, kstar=e shat/g1.

These D1,kstar are exactly the old values: both Dstar and e s contain the common factor k_C^2 k_R. Thus their removal follows from an identity of common factors, not from an assumed coprimality.

Retain the FINAL evaluated common gcd

    h0=gcd(D1,|u0 w|,|v0 w|),
    D2=D1/h0,
    U=(u0 w)/h0, V=(v0 w)/h0,
    Wcancel=((uhat+vhat)w)/(shat h0).                            (5)

All quantities in (5) are integral. They are unchanged from the preceding note, and

    alpha=kstar U/D2, gamma=kstar V/D2,
    gcd(kstar,D2)=1, gcd(D2,U,V)=1,
    delta=gcd(D2,|Wcancel|).

Thus the endpoint term, logarithmic term, and final reduced-denominator gcd have survived the primitive normalization exactly.

Write

    Bbar=abar_B Bprim,
    u0+v0=c_H(H0,H1), gcd(H0,H1)=1.

The primitive form Bprim, primitive row (H0,H1), and positive resultant Rresultant are the SAME as in the preceding note. In particular

    a_B=k_C^2 k_R^2 abar_B.

Since D2 divides F d0 L t0 k_R Bbar(w), the previous primitive-response resultant argument now gives the sharper restriction

    delta_exc divides
      gcd(d0 L t0 k_R abar_B c_H Rresultant,|Wcancel|).           (6)

Compared with the old exceptional product, the explicit factor k_C^2 k_R has disappeared. This improvement is justified by denominator cancellation before evaluation. Dividing a resultant by contents alone would not justify (6).

## 4. Scalar factorization of the resultants

Use the homogeneous convention

    Res(Q,l0 X+l1 Y)=Q(-l1,l0).

For a quadratic Q, scaling it by a multiplies this resultant by a; scaling the linear form by b multiplies it by b^2. Hence the exact factorizations are

    Res(Bbar,uhat+vhat)
       =abar_B shat^2 c_H^2 Rresultant,

    Res(Bform,urow+vrow)
       =k_C^6 k_R^4 abar_B shat^2 c_H^2 Rresultant.              (7)

These identities distinguish matrix content, joint row content, sum-row content, and the genuinely primitive resultant. The residual product in (6) contains only one power of c_H. The raw resultant contains two, because its linear argument is evaluated quadratically. No extra cancellation is inferred from that discrepancy.

Positive definiteness proves Rresultant>=1. It does not bound the gcd of Rresultant with Wcancel.

## 5. Primitive entries versus primitive maximal minors

Define the integer rank-two matrix

    Ybar=adj(M)Drow Jpair/(k_C k_R),
    Rbar=K Ybar.

Its integrality and entry content one follow by applying the integer left inverse of K to Rbar. Let kappa2 be the positive gcd of its three maximal minors. Its Smith invariant factors are therefore 1,kappa2.

Put

    G_K=K^T Omega K.

The content abar_B of Ybar^T G_K Ybar satisfies

    abar_B divides 2 kappa2^2 det(G_K).                          (8)

Proof. Integral Smith basis changes put Ybar into columns e1,kappa2 e2. A unimodular change of the two binary variables preserves coefficient content. A unimodular change of the ambient three variables replaces G_K by an integral matrix G' with the same determinant. The quadratic coefficients become

    g'11, 2 kappa2 g'12, kappa2^2 g'22.

If a is their gcd, then a/gcd(a,2kappa2^2) divides each entry of the upper-left two-by-two block. Every term of a three-by-three determinant contains at least one entry of that block. Thus this quotient divides det(G_K), proving (8) prime by prime, including p=2.

The reconstruction determinant itself is small. The differential matrix is integral unitriangular, and every maximal minor of Z has absolute value one. Cauchy-Binet therefore gives exactly

    det(G_K)=sum_(i=0)^3 product_(j!=i) omega_j^2,
    omega_j=(n+2)_j,
    0<det(G_K)<=4(n+2)^12.                                    (9)

Define the exact factorization

    a_reg=gcd(abar_B,2det(G_K)),
    a_lat=abar_B/a_reg.

Then

    a_reg<=8(n+2)^12,
    a_lat divides kappa2^2.                                   (10)

The factors need not be coprime. Primitive matrix entries alone do not eliminate kappa2; it measures saturation of a rank-two lattice, rather than content of its individual entries.

## 6. Exact formula for the remaining lattice factor

Set

    v_n=(d0/2,-(2n+3),1)^T,
    m_n=content(M^T v_n).

The vector v_n is integral and primitive. The wedge of the two columns of Drow Jpair is

    4(n+2)d0 v_n.

For an invertible three-by-three matrix A, the cross-product identity is

    (Aa) cross (Ab)=det(A) A^(-T)(a cross b).

Taking A=adj(M) gives det(A)A^(-T)=Delta M^T. Dividing the columns by k_C k_R now yields the exact integer identity

    kappa2=4(n+2)d0 |Delta| m_n/(k_C^2 k_R^2).                  (11)

The quotient in (11) is an integer because its left side is the gcd of the actual integral minors. It is not a claim that the factors in its numerator are pairwise coprime.

Also

    m_n divides |Delta|.                                      (12)

Indeed adj(M^T)M^T v_n=Delta v_n, and the primitivity of v_n gives this divisibility. Equations (10)-(12) identify the possible non-polynomial contribution to the primitive Gram-form content: it lies in maximal-minor saturation involving Delta and m_n after the two entry contents have been removed.

Neither (11) nor primitivity proves that kappa2, a_lat, or their relevant gcds are subfactorial. No claim that they actually attain factorial growth is made. The exact identities identify the remaining canonical lattice arithmetic, rather than supplying a counterexample with unrelated polynomials.

## 7. A controlled factor of the exceptional deficit

Define positive integers

    K_reg=d0 L t0 a_reg,
    K_bad=k_R a_lat c_H Rresultant,
    delta_reg=gcd(delta_exc,K_reg),
    delta_res=delta_exc/delta_reg.

Then (6) proves

    delta_exc=delta_reg delta_res,
    delta_reg divides K_reg,
    delta_res divides K_bad,
    delta_res divides Wcancel/delta_reg.                       (13)

There is no coprimality assertion between these factors. The last quotient is integral because delta_reg divides delta_exc, which divides Wcancel.

The first factor has a parameter-uniform logarithmic bound. The retained endpoint bound gives

    t0<=P_n<=[2(1+sqrt(2))]^n,

and lcm(1,...,2n+2)<=4^(2n+2) gives L<=2^(6n+5). By (9),(10),

    K_reg<=8(n+2)^14 2^(6n+5)[2(1+sqrt(2))]^n,
    log delta_reg=O(n).                                       (14)

Thus this part is o(n log n). The residual factor in (13) contains the primitive reconstruction-lattice factor, normalized sum-row content, and primitive resultant. Its cancellation against Wcancel has not been bounded at the desired scale.

## 8. Explicit height ledger and a uniform exceptional ceiling

The following bounds are ceilings only. They do not establish favorable gcd cancellation. They make the distinction between controlled small factors and the remaining arithmetic quantitative.

Put M0=1+sqrt(2), and define

    Mbound=18(2M0)^n(n+2)!,
    Cbound=12(n+3)^2 d0 Mbound^2,
    Omegabound=(n+2)^6.

Cauchy's bound for the Toeplitz entries on |z|=sqrt(2) gives |M_ij|<=Mbound. Two-by-two minors then give |adj(M)_ij|<=2Mbound^2 and |Delta|<=6Mbound^3. The finite reconstruction bound |K_ij|<=2(n+3)^2 gives |C_ij|<=Cbound.

In particular, uniformly for fixed b=3,

    log Cbound=2log(n!)+O(n),
    log|Delta|<=3log(n!)+O(n).

Define bounds for the primitive matrices and form by

    Rbound=12(n+2)Cbound/(k_C k_R),
    Zbound=4 Omegabound(Cbound/k_C)Rbound,
    Bbound=16 Omegabound Rbound^2.

They give respectively

    ||Rbar||_max<=Rbound,
    ||Zbar||_max<=Zbound,
    ||Bbar||_1<=Bbound.

The last norm is the sum of the absolute values of the three binary coefficients. In particular abar_B<=Bbound. The actual primitive response satisfies ||w||_infinity<=(2M0)^(n+1). Thus the denominator divisibility used in (6) gives the entirely explicit bound

    delta_exc<=d0 L k_R Bbound(2M0)^(3n+2).

Consequently

    log delta_exc<=4log(n!)-2log k_C-log k_R+O(n).              (15)

The O(n) constant is independent of n and of the evaluated primitive response. Without estimates for the removed contents or further cancellation this proves only log delta_exc=O(n log n), with leading ceiling four. It proves neither an attained growth rate nor the desired little-o estimate.

For completeness the other remaining factors also have explicit ceilings. Since Dcal_j<=3j!, the retained finite formula for Ecal gives

    ||Ecal||_infinity<=Ebound=3*5^n(2n+2)!.

Indeed each factorial quotient in that formula is bounded by (2n+2)! after including (n+2)!, and the absolute coefficient sum of (2-2t+t^2)^n is at most 5^n. For the moment row, the integer direct polynomials have coefficient norm at most 4*20^n. Dividing their endpoint-subtracted polynomial by t-1 increases this norm by at most 2n+2; each segment monomial moment has absolute value at most two. Hence

    ||theta||_infinity<=Thetabound=8L(2n+2)20^n.

These are scalar size bounds, not a new evaluation of either companion. From (2),

    ||uhat+vhat||_infinity<=Tbound,

where

    Tbound=3L Ebound Zbound
         +L(d0|Delta|/k_C)Rbound
         +3F d0 Thetabound Zbound.

It follows that

    shat c_H<=Tbound,
    max(|H0|,|H1|)<=Tbound/(shat c_H),
    1<=Rresultant
       <=(Bbound/abar_B)[Tbound/(shat c_H)]^2.                  (16)

Also (4),(11),(12) give

    k_R<=4(n+2)|Delta|/k_C,
    kappa2<=4(n+2)d0 |Delta|^2/(k_C^2 k_R^2).

These bounds retain all known common scalars. They can still have factorial-scale logarithms. Even a large ceiling for the primitive resultant says nothing about whether its prime powers survive in Wcancel after the final gcd h0.

## 9. Exact residual prime powers and required precision

For a prime p write

    f_p=2v_p(n!),
    d_p=v_p(D2),
    w_p=v_p(Wcancel),
    k_p=v_p(K_reg).

The definitions, with the original factorial truncation unchanged, give EXACTLY

    v_p(delta_exc)=max(0,min(d_p,w_p)-f_p),
    v_p(delta_res)=max(0,min(d_p,w_p)-f_p-k_p).                 (17)

Therefore p^j divides delta_res, for j>=1, if and only if both

    d_p>=f_p+k_p+j,
    Wcancel=0 mod p^(f_p+k_p+j).                              (18)

In terms of the integer row BEFORE final division, the second test in (18) is

    (uhat+vhat)w=0
      mod p^(f_p+k_p+j+v_p(shat)+v_p(h0)).                     (19)

The required extra precision v_p(shat)+v_p(h0) cannot be discarded. The denominator test is likewise explicit:

    d_p=v_p(Dtilde)
          -min(v_p(Dtilde),v_p(e shat))-v_p(h0),
    Dtilde=F d0 L t0 k_R abar_B Bprim(w).                      (20)

Every prime contributing to (17) has U and V both p-adic units, by the retained final-gcd normalization. Thus (19) is a genuine equal-depth unit-numerator cancellation after division, rather than a first-order vanishing of an unreduced row.

Only primes dividing K_bad can contribute to delta_res. But their allowed support and their available powers do not prove that the congruences fail. Determining the exact contribution at a prime can require precision through d_p in Wcancel, or through d_p+v_p(shat)+v_p(h0) in the undivided integer row.

Because log delta_reg=O(n), the exceptional target is equivalent to

    sum_p max(0,min(d_p,w_p)-f_p-k_p) log p=o(n log n).         (21)

A sufficient, potentially stronger condition is

    log gcd(K_bad,|Wcancel|/delta_reg)=o(n log n).

Neither condition is proved. Replacing it by log K_bad=o(n log n) would be stronger still and is also unproved. Positive definiteness, primitive coefficient content, and the height ceilings do not establish any of these gcd estimates.

## 10. Outcome and separation from the factorial deficit

The exact new structure is

    delta=delta_F delta_exc,
    delta_exc=delta_reg delta_res,
    log delta_reg=O(n),
    delta_res divides k_R a_lat c_H Rresultant,
    a_lat divides kappa2^2,
    kappa2=4(n+2)d0 |Delta|m_n/(k_C^2 k_R^2).

The residual numerator is always the unchanged endpoint-corrected Wcancel with its final evaluated gcd. Equations (18)-(20) specify the precision needed to decide its remaining prime-power cancellations. Equation (15) supplies a uniform factorial-scale ceiling, not a subfactorial conclusion.

The original delta_F is separate and unchanged. Even proving (21) would control only the exceptional factor. A subfactorial TOTAL deficit would additionally require log delta_F=o(n log n). Accordingly no new assertion that the 5/72 complete-overlap threshold applies is made; that application still requires the corresponding total-deficit and companion-denominator budgets.

The unresolved factors are actual canonical quantities: entry-content loss k_R, primitive rank-two lattice saturation measured by kappa2, the sum-row content c_H after joint normalization, and the primitive resultant together with its evaluated cancellation. The results locate these possible factorial-scale contributions but do not assert that any of them is actually large. No coordinate-center argument, denominator-mismatch calculation, high-prime analysis, endpoint-corrected scalar-numerator analysis, seed replay, or independent review is used.

Both this note and CANONICAL_EXCEPTIONAL_DEFICIT_CONTENT_REPORT.md require application-confirmed saving and subsequent read-back before operational completion is reported.
