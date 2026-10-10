> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual wide-block rank and the residual arithmetic interface

Author: Child 2. Status: new author proof, conditional on the explicitly attributed coercivity input below; not independently reviewed. No numerical calculation or networking was used. The rationality of the actual S=e+pi remains unresolved.

## 1. Definitions and inherited input

Historical sources are under work/session_20261002_codex_continuation/:

- agent2_selector/SHORT_STACK_COMPACT_DIAGONAL_INDEX.md, for the actual matrices and all basis indices.
- agent2_selector/SHORT_STACK_RIGHT_BLOCK_SCHUR_CONTENT.md, for the inherited Smith/content formulas.
- agent3_analysis/SHORT_RECTANGULAR_COMPLETE_SIGNED_ERROR.md, Sections 2–3, for signed modified-moment coercivity and conditional roots. These analytic results are used with author attribution, not presented as newly proved here.

Put lambda(P)=integral_0^1 P(x^2)dx, f(y^r)=(2r)!, and mu(y^r)=D_(2r). The measure mu is the pushforward of exp(-t)dt on t>=0 by y=(1-t)^2. Set rho=mu-delta_(-1), and

    K(P)=-f((y+1)P)+4lambda(P).

Let ell_j(y)=2^(2j)P_(2j)(sqrt(y)), with leading coefficient binom(4j,2j). The actual W' has upper entries rho(ell_i ell_j), 0<=i<k, and lower entries L K(ell_i ell_j), 0<=i<k-1, with 0<=j<2k and L=lcm(1,3,...,6k-5). Its right block P_W consists of columns j=k-1,...,2k-1. The compact contribution vanishes in those columns, but the upper term -ell_i(-1)ell_j(-1) remains.

The inherited coercivity statement used here is: for k>=24, every monic R whose k-1 roots belong to [-1,1], and every nonzero real p of degree<k,

    rho(R p^2)>0.

The same source proves rho(R(y)(y-u)p(y)^2)>0 for every u in [-1,1]. Its explicit constant is

    C_k=3 exp(-2k-1)(k^2-1)^(k-1)/(4k 16^(k-1))>2^k.

On I=[k^2,4k^2], the source's evaluation estimate bounds the positive tail below by C_k times max(|p(-1)|^2,sup_[0,1]|p|^2). These precise signed-form assertions, rather than positivity of the underlying signed measure, are the input.

## 2. Exact actual moment conversion, including the atom

For every polynomial P,

    e mu(P)=f(P)+integral_0^1 exp(x)P(x^2)dx.             (1)

Indeed split the defining t-integral for mu at t=1 and substitute x=|1-t| in its two parts. Define the positive compact measure tau by

    tau(P)=integral_0^1 [(1+x^2)exp(x)+4]P(x^2)dx.

Then the exact identity is

    K(P)+e rho((y+1)P)=tau(P).                          (2)

The atom vanishes in the particular factor (y+1)P in (2); it is still present in every condition rho(Qa)=0, especially mu(Q)=Q(-1).

Consequently the polynomial kernel of the full W' is exactly the space of Q of degree<=2k-1 satisfying

    rho(Qa)=0       for deg a<k,
    tau(Qb)=0       for deg b<k-1.                     (3)

This is an equality of real polynomial kernel spaces. It follows from (2), since deg((y+1)b)<k. Because W' is rational, its real and rational ranks agree.

A kernel polynomial of P_W additionally belongs to span(ell_(k-1),...,ell_(2k-1)), equivalently

    lambda(Qb)=0    for deg b<k-1.                     (4)

Equations (1)–(4) describe the actual family, not a generic Gamma stack.

## 3. Sign-change bound for the actual kernel

Write n=k-1. Any nonzero Q satisfying (3) has at least n sign changes in (0,1): otherwise multiplication by the product of its compact sign-change roots would give a polynomial test of degree<n with a nonzero integral against the positive measure tau.

There cannot be m>=k compact sign changes. Let R_m be the monic product of the m distinct sign-change roots, and write Q=R_m H. Then deg H<=2k-1-m<=k-1, so the first condition in (3) gives

    rho(R_m H^2)=0.                                   (5)

But the inherited tail estimate extends directly to this modifier. Let

    M(H)=max(|H(-1)|^2,sup_[0,1]|H|^2)>0.

Its positive tail is at least

    (k^2-1)^(m-k+1) C_k M(H).

All possible negative contributions are confined to [0,1] and the atom at -1. Their absolute sum is at most (1+2^m)M(H), since |R_m|<=1 on [0,1] and |R_m(-1)|<=2^m. As C_k>2^k and k^2-1>2,

    (k^2-1)^(m-k+1) C_k >2^(m+1)>=1+2^m.

Thus rho(R_m H^2)>0, contradicting (5). Every nonzero Q satisfying (3) therefore has exactly n compact sign changes.

There is also no nonzero solution of (3) of degree<=2k-2. Such a solution would factor as Q=R_n H with deg H<=k-1, where R_n is the product of its n compact sign-change roots. The first equation in (3) and the inherited (k-1)-node coercivity give respectively rho(R_n H^2)=0 and >0.

It follows that W' has full row rank 2k-1, and its kernel has a unique monic polynomial Q_k of degree 2k-1. This conclusion uses the signed-form input directly and does not need an additional beta_1 nonvanishing assumption.

## 4. Full rational rank of the ACTUAL wide right block

**Theorem.** For every k>=24, rank_Q P_W=k+1.

Suppose instead that its kernel contains a nonzero Q. Equations (3)–(4) hold. By Section 3, Q has exactly n=k-1 sign changes alpha_1,...,alpha_n in (0,1). Put

    R(y)=product_(i=1)^n(y-alpha_i),  H=Q/R.

The real polynomial H has a fixed nonzero sign away from its finitely many zeros on (0,1): all sign changes of Q have been removed once. Select any alpha_i and put p_i=R/(y-alpha_i), of degree n-1. Define

    w(y)=(1+y)exp(sqrt(y))+4.

This function is strictly increasing on [0,1]. From (3)–(4),

    0=tau(Qp_i)-w(alpha_i)lambda(Qp_i)
     =integral_0^1 H(y)R(y)^2
          [(w(y)-w(alpha_i))/(y-alpha_i)] d lambda(y). (6)

The divided difference in (6) is strictly positive, including its continuous value at alpha_i. All remaining factors have a constant nonzero sign except at finitely many points. The integral is therefore nonzero, a contradiction.

This excludes the inherited rank-k branch throughout the explicit infinite range k>=24. The argument excludes an actual polynomial kernel; it is not a generic full-rank assertion or a numerical rank scan. No assertion is made here for 2<=k<24.

## 5. Additional actual root information

The monic kernel polynomial from Section 3 factors Q_k=R_n H_k, where R_n records its n compact sign-change roots. The equations rho(Q_k a)=0 say that H_k is the monic degree-k orthogonal polynomial for the signed functional nu=R_n rho.

The inherited input makes both nu(p^2) and nu((y-1)p^2) positive for deg p<k. Thus the compressed multiplication matrix for nu is real symmetric with all eigenvalues greater than 1. Its characteristic polynomial is H_k; the positive lower-degree norms make its Jacobi matrix irreducible, so its roots are simple. Hence Q_k has exactly k-1 simple roots in (0,1) and k simple roots in (1,infinity). The stronger inherited conditional root bound gives the latter roots>a k^2 for k>=100, a=1/(48e^4).

This is a consequence for the actual W-kernel of the attributed conditional-form theorem. It gives no p-adic unit conclusion.

## 6. Retained Smith, basis and largest-pivot factors

The full-rank branch now applies for k>=24. Keep the inherited integer Smith reduction

    U P_W V=[D_W;0], D_W=diag(e_1,...,e_(k+1)),
    delta_W=product e_i,
    U X_W=[A_W;S_W].

Here S_W is (k-2) by (k-1), has full row rank, and h_S is the positive gcd of its maximal minors. The exact inherited formula remains

    h'_W=delta_W h_S/zeta_W,
    zeta_W=lcm_i(e_i/gcd(e_i,z_i)),
    z_i=det[A_(W,i);S_W]/h_S,
    zeta_W | e_(k+1).                                 (7)

No conclusion zeta_W=1 follows from the rank theorem.

The original basis transfer is still

    h_W=delta_W h_S /
        [zeta_W Delta_k Delta_(k-1) theta_W],
    theta_W | Delta_(2k).                             (8)

For the tall block it remains

    h_N=delta_N h(S_N)/[Delta_(2k-1)theta_N],
    theta_N | Delta_k^2.                              (9)

Here Delta_j=product_(i<j)binom(4i,2i). All equalities are exact; their factors cannot be dropped because their logarithms are O(k^2).

## 7. A polynomial interpretation of the surviving wide loss

This section is an elementary corollary of the inherited Smith formula, not a claim of a new generic Smith theorem. It makes zeta_W accessible through the actual kernel polynomial without constructing the row multiplier U.

Choose the primitive integer vector z=(z_0,...,z_(2k-1)) in ker W', and let

    Q^prim_k(y)=sum_(j=0)^(2k-1) z_j ell_j(y).

The normalization is primitive in the INTEGER LEGENDRE COORDINATES. It must not be replaced silently by primitiveness in monomial coordinates. Set

    c_low=gcd(z_0,...,z_(k-2))>0.

The rank theorem ensures these entries are not all zero. Then

    zeta_W=c_low.                                     (10)

Proof: let v be the primitive right kernel vector of S_W. In the Smith column coordinates every full kernel vector has x=t v and y_i=-t(A_W v)_i/e_i. Integrality requires t to be an integer divisible by lcm_i e_i/gcd(e_i,(A_Wv)_i), which is zeta_W by cofactor expansion. The vector obtained at the least positive t=zeta_W is primitive: dividing all its coordinates by any common integer would contradict the minimal positive t, because v is primitive. The unimodular transformation of the right columns preserves primitiveness and leaves the left coordinates unchanged. Their gcd is therefore zeta_W.

Compact orthogonality gives the exact extraction formula

    z_j=(4j+1)lambda(Q^prim_k ell_j)/16^j.              (11)

Thus (10) is the common content of the ACTUAL low compact Legendre projection, with the factors 4j+1 and 16^j retained. Equivalently, at every prime p,

    v_p(zeta_W)=min_(0<=j<=k-2) v_p(z_j),

using v_p(0)=infinity. For odd p the power 16 is a unit; the factors 4j+1 are still retained unless their p-unit status has been established.

Combining (8) and (10) gives the exact residual criterion

    v_p h(S_W)
      =v_p h_W+v_p Delta_k+v_p Delta_(k-1)+v_p theta_W
         +min_(j<k-1)v_p(z_j)-v_p delta_W.             (12)

In particular, S_W is p-saturated exactly when the right side is zero. This is an explicit remaining arithmetic criterion, not an estimate for its terms. It can support a direct arithmetic study of the actual compact projection; the real sign argument only proves that projection is nonzero.

## 8. Full primitive output and the remaining gap

The complete pair still obeys

    lcm(h_N,h_W) | G_actual | L h_N h_W.

Writing H_N and H_W for the respective exact right sides of (9) and (8), the all-depth statement is

    max(v_p H_N,v_p H_W)<=v_p G_actual
       <=v_p L+v_p H_N+v_p H_W.

The inherited tall response reduction retains

    D_basis=Delta_k^2 Delta_(2k-1),
    D_basis G_actual=delta_N gcd(A,L B),
    q=L|B|/gcd(A,L B).

The new rank/root theorem neither estimates h(S_N), h(S_W), delta_N, delta_W, zeta_W nor bounds the final coefficient gcd. At p>8k-4, L and the displayed basis factors are units, but neither residual saturation nor favorable final content follows.

## 9. Next useful interface

The rank-k branch is eliminated for k>=24 under the stated inherited analytic input. The next useful arithmetic object is the primitive actual W-kernel polynomial together with its low Legendre projection (10)–(11), not another rational-rank scan. A worthwhile follow-up would prove an actual congruence or divisibility law for that projection and its coupling to delta_W and h(S_W). Such a law must retain the primitive Legendre normalization and the full factors in (8)–(12).

No all-degree odd-content estimate, final primitive denominator law, or irrationality claim has been proved in this stage. Child 1's final-pair estimates and Main's cross-polynomial resultant work are not duplicated.
