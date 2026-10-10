> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete directional remainders and the rational center

New author research, conditional where indicated on Child 3's CONTACT_INVERSE_RESEARCH.md. That input, including its completion Section 9, and the main RATIONAL_CENTER_PAIR_CRITERION.md have been read. No independent audit, numerical controls, or repeated multirow checks are performed. Earlier outputs remain unchanged.

## 1. Actual lift and a justified rational coefficient norm

Work with the relaxed balanced family, n>=16, b>=3, n>=512 b^4 log n. Assume the actual endpoint lift exists. The quantitative inverse estimates below are provisional dependencies on Child 3, not independently established here.

Let Phi be the full rational coefficient lift and Psi its B-coefficient block. Put

    u=Psi(1,0), v=Psi(0,1), S=e+pi.

Thus B(P,Q)=Pu+Qv. Choose the retained-row weights from the completed multirow construction:

    1<=m<=floor((b-1)/2), k=n+m,
    r0=n+m+1-b,
    w_j=r0!/(n+m+1-j)!, 0<=j<=b,
    W_B=diag(w_j^2), wmin=min_j w_j.

These are positive rational weights, w_b=1, and wmin>=(2n)^(-b). Use inner product <x,y>_w=x^T W_B y. Define

    a=<u,u>_w, h=<u,v>_w, c=<v,v>_w,
    Sigma=[[a,h],[h,c]], D=ac-h^2,
    t=h/a, z=v-tu, s=<z,z>_w=D/a.

The B lift is injective, so Sigma is positive definite. All these quantities, including t,z,s, are rational. The center uses only exact lift coefficients; it is not defined using S.

This norm is justified twice: it is exactly the factorial-weighted coefficient norm in the complete multirow estimate, and Child 3 gives a positive rational full-coefficient extension. With that note's rational reconstruction constants c0,a0, let

    ||(A,B,C)||_full^2
      =(wmin/a0)^2||A||_2^2+||B||_w^2
        +(wmin/c0)^2||C||_2^2.

Its stated reconstruction estimates imply on the solution space

    ||B||_w <= ||(A,B,C)||_full <= sqrt(3)||B||_w.

Consequently the full Gram matrix satisfies

    Sigma <= Gfull <= 3 Sigma.

The B-only norm is positive definite on the solution space; the displayed extension is positive definite on the entire coefficient space.

## 2. Explicit provisional inverse constants

To avoid hiding conditioning, retain Child 3's constants explicitly. Set R=sqrt(2), M0=1+R, d=b-1 and

    Cint=(16 b^2 n)^d binom(2d,d)/(d!)^2,
    K0=2048 b sqrt(n) Cint,
    Fminus=n! 2^n/(2n+1),
    E0=16 sqrt(b) R^d n! (3/2)^n
          +27 sqrt(b) M0^n/(n+1),
    Hplus=(n+1)^d, Hminus=(n+b)^d,
    L=Fminus/[9 b R^d Hplus M0^n],
    E=1+2 Hminus K0 E0/M0^n.

The provisional input supplies

    ||u||_2>=L, ||v-Su||_2<=E,
    2(2n)^b E/L<=exp(-n/8).

These are estimates of actual forcing and reconstruction, not definitions involving the unknown approximation error. The additive 1 in E is retained. This note does not strengthen the claimed exponential rate or reverify its constants.

## 3. Orthogonal separation preserves the complete main term

By construction <u,z>_w=0 and

    Pu+Qv=u(P+tQ)+zQ.

Define delta=v-Su. Its orthogonal decomposition is

    delta=z+(t-S)u.

Therefore the exact identity is

    ||delta||_w^2=s+a(t-S)^2.                         (1)

In particular, since w_j<=1 and ||delta||_2<=E,

    |S-t| <= Bperp := sqrt((E^2-s)/a).               (2)

Under the provisional hypotheses E^2>=s, so the radicand is nonnegative. If exact data contradict that condition, the estimate is inapplicable; a negative radicand must not be silently clipped to zero.

Equation (2) is a new Pythagorean refinement of the inherited orientation estimate E/sqrt(a). It removes the entire rational transverse squared norm s from the error budget. It uses an independently specified upper bound E on forcing and reconstruction, not the unknown ||v-Su|| itself. Thus Bperp is an analytic upper bound, conditional on the inverse theorem. In contrast, replacing E^2 by the exact left side of (1) would merely rewrite |S-t|.

The endpoint coefficient sum gives sum_j u_j=0 and sum_j z_j=1. Hence, with Hw=sum_j w_j^(-2),

    s>=1/Hw>0.

This also yields the weaker fully explicit subtraction

    |S-t|<=sqrt((E^2-1/Hw)/a),

again only under the same valid hypotheses. No uniform positive fraction s/E^2 is proved, so the strict improvement in (2) is not promoted to a new exponential rate.

For arbitrary real P,Q, the COMPLETE form obeys

    |P+QS| <= |P+tQ|+Bperp |Q|.                      (3)

Here A_n=1 exactly. This follows by keeping the exact longitudinal value of the endpoint functional; it does not separately bound exponential and pi contributions in that direction.

The coarser bound

    B0=E/sqrt(a)<=E/(wmin L)<=exp(-n/8)/2             (4)

is inherited from Child 3's provisional inverse estimate, including all its amplification. Thus (3) is an explicit complete directional certificate. The uniform exponential rate in (4) is not a newly proved improvement over that input. The new contributions here are the exact longitudinal normalization and the transverse subtraction in (2).

## 4. Full-tail functional and the exact place where its coarse bound loses cancellation

Let ell_x be the original factorial functional, and retain the completed multirow identities without replaying their checks. Define

    T_m(x)=ell_x(tvar^m p_k(tvar)/(1-tvar))/A_k,
    pi_k=v_k/A_k, A_k=p_k(1),
    gamma=3||p_k||_1/(A_k r0!),
    dk=2|h_k|/A_k^2.

The variable tvar is distinct from the rational center t. For every actual lifted B vector x with endpoint Q,

    P+QS=T_m(x)+pi_k Q.                              (5)

This is the complete factorial-tail functional, with all retained-row subtractions performed before estimates. In particular,

    T_m(u)=1,
    T_m(z)+pi_k=S-t.                                 (6)

Linearity now gives

    T_m(u(P+tQ)+zQ)+pi_k Q
       =(P+tQ)+[T_m(z)+pi_k]Q.                       (7)

Thus (7) preserves the near-rank-one term exactly. Merely defining B=|T_m(z)+pi_k| would restate the desired approximation; it is not a new estimate.

The saved coefficient bound gives

    |T_m(z)|<=sqrt(b+1) gamma sqrt(s), |pi_k|<=dk.

Applying a triangle inequality here produces

    Btail=dk+sqrt(b+1) gamma sqrt(s).                 (8)

Equation (8) is valid, but it discards precisely the cancellation in the bracket in (7). It is the old separated-tail transverse budget in centered coordinates. This branch is stopped as a source of new cancellation-sensitive savings. No favorable sign for that bracket has been proved.

For comparison only, one may use min(Bperp,Btail) as a valid error envelope. The conditional new orientation bound Bperp does not come from claiming that the two terms in (6) are individually small. It comes from the complete forcing residual delta before taking separate absolute values of its e and pi contributions at the endpoint.

The nonzero endpoint (1,0) also gives

    1=T_m(u), (b+1)gamma^2 a>=1.                     (9)

This makes the old longitudinal coefficient sqrt(2(b+1))gamma sqrt(a) at least sqrt(2), whereas (3) has the exact coefficient 1. There is no justified claim that this constant improvement alone makes any primitive pair shrink.

## 5. Exact reconciliation with the previous Gram certificate

The previous multirow notation Um,Vm,Dm is exactly a,h,D here. Its matrix and scalar were

    Z=(b+1)(gamma/dk)^2,
    Gold=2[e2 e2^T+Z Sigma], etaold=dk.

Therefore its center is exactly t=h/a, with no comparison loss, and its centered quadratic expression is

    etaold^2 (P,Q)Gold(P,Q)^T
      =2(b+1)gamma^2 a(P+tQ)^2
         +[2dk^2+2(b+1)gamma^2 s]Q^2.               (10)

The full-coefficient norm from Section 1 generally has a different center tfull. If afull=Gfull_11 and sfull=det(Gfull)/afull, the norm comparison implies

    a<=afull<=3a, s<=sfull<=3s,
    D<=det(Gfull)<=9D.

For an explicit center comparison, apply the full norm to the lifted vectors corresponding to u and z. Then

    |tfull-t|<=sqrt(3s/a).                           (11)

Indeed their full inner product divided by afull equals tfull-t, while their full norms are at most sqrt(3s) for z and at least sqrt(a) for u. Thus one must not identify these two rational centers or their reduced denominators. The certificate (3) consistently uses the B-only center, which is exactly the old multirow center.

If a rational positive definite quadratic certificate is desired for (3), choose any positive rational rho>=Bperp^2. Then

    |P+QS|^2<=2(P+tQ)^2+2rho Q^2,
    Gdir=2[[1,t],[t,t^2+rho]], eta=1.                (12)

Such rho can be enclosed from the explicit constants using rational square-root bounds. No numerical enclosure was computed in this work. Matrix (12) has center t and determinant 4rho. Its certificate targets are 2/q^2 and 2rho q^2. The sharper direct pair bounds below avoid the extra quadratic factor.

## 6. The explicit primitive center pair: both denominator effects retained

Write the exact rational t=p/q in lowest terms, q>0. If a positive integer J0 clears a and h, then

    q=J0 a/gcd(J0 a,|J0 h|).

This is the actual reduced center denominator, not a lift denominator. Choose integers x,y with qx+py=1 and |y|<=q/2. The pair

    u1=(-p,q), u2=(x,y)

is primitive and has determinant -1. Put epsilon=S-t. The exact complete forms are

    L1=q epsilon,
    L2=1/q+y epsilon.                               (13)

Consequently

    |L1|<=q Bperp,
    |L2|<=1/q+(q/2)Bperp.                           (14)

The actual second denominator is |y| when y!=0. The term 1/q in (13)-(14) cannot be suppressed. Neither can the factor q multiplying the directional error. A sufficient condition for this pair is

    q->infinity and q Bperp->0.                     (15)

Using only the inherited uniform envelope (4), sufficient conditions are q->infinity and q exp(-n/8)->0. These are conditional arithmetic requirements, not established properties of the actual center. In particular exponentially small orientation alone does not suffice when the reduced q grows too fast.

For comparison, the old quadratic targets were

    Eold=2(b+1)gamma^2 a/q^2,
    Fold=[2dk^2+2(b+1)gamma^2 s]q^2.

The new direct longitudinal term is exactly 1/q, with no inverse-column amplification. The transverse estimate instead uses (E^2-s)/a. No uniform ordering between this estimate and Fold follows without further information about a,s and the explicit inverse constants.

## 7. Individual endpoint gcds and scope of the gain

For any primitive direction (P,Q), let its minimal integral lift multiply the rational coefficient triple by mu. Its endpoint pair is mu(P,Q), its endpoint gcd is mu, and its full remainder is mu(P+QS). Dividing by that pair's own gcd cancels mu exactly. Apply this separately to the two vectors in (13); their radial factors need not agree. The bounds (14) concern their already primitive forms.

What is newly quantified: the exact coefficient A_n=1; the rational weighted center compatible with the old Gram matrix; the analytic transverse budget sqrt((E^2-s)/a); the explicit coefficient-norm and center comparisons; and both denominator effects in the primitive center pair.

What is not obtained: a uniformly better exponential rate than Child 3's provisional exp(-n/8) orientation, a lower bound on s/E^2 producing a uniform further gain, a favorable reduced q range, or a new signed upper bound for the bracket T_m(z)+pi_k beyond the orientation input. The full-tail-only triangle branch reproduces the old loss (8) and is stopped. The exact formula (6) alone is not offered as progress on approximation.

These results preserve all previous multirow artifacts. No irrationality or shrinking-pair theorem is claimed. This note and DIRECTIONAL_FULL_REMAINDER_REPORT.md must be read back before completion is reported.
