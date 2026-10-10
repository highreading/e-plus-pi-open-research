> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Phase crossings: endpoint arithmetic and adjacent-selector bypass

Status: new author deductions, not independently reviewed. This note preserves LARGE_SELECTOR_PHASE_CROSSINGS.md, its derivative-controlled continuation, and all earlier saddle results. Those arguments are used in their saved scopes and are not repeated. No numerical phase scan, independent review, or new computation is claimed. The result is a qualitative exclusion of exact integer crossings and a precise obstruction/budget for quantitative separation and adjacent-selector cancellation. It does not resolve the rationality of e+pi.

## 1. Starting point and notation

Fix rho,C>0 and let n=2^s>=4 tend to infinity. Set T=n log n and a_rho=rho log 2. The selector index lies in

    |m-rho n log n| <= C n log n/log log n.

For the combination discussion, take m,m+1 both eligible in the preserved dyadic allocation. Such adjacent pairs exist by the saved block theorem. This note does not repeat their construction. For each member of the pair, U_j!=0 and v2(U_j)=n/2.

The exact slow parity crossing sets are

    r_(epsilon,k)=psi_n^(-1)(epsilon*pi/2+k*pi).

At an eligible integer m, bounded complete primitive error requires distance to its matching parity crossing set at most

    exp(-kappa_rho T+o(T)),
    kappa_rho=min(3a_rho,1+a_rho).

Both terms are essential: the second allows cancellation against the complete exponential residual. Monotonicity, curvature, and truncated phase expansions do not establish avoidance at this scale.

We use S=e+pi. The complete rational companions of selector j=0,1, meaning index m+j, are denoted alpha_j and beta_j. Their forcing and rational numerators are

    U_j,
    X_j=U_j alpha_j,
    Y_j=U_j beta_j,
    Z_j=X_j+Y_j.

Define complete residual numerators

    E_j=X_j-e U_j,
    F_j=Y_j-pi U_j,
    R_j=Z_j-S U_j=E_j+F_j.

These symbols are local to this note; Z_j is not the earlier truncated endpoint enclosure.

## 2. Exact endpoint arithmetic excludes exact integer coincidences

For an integer index m, put

    alpha=(1+i)/2,
    V(w)=w^2-w+1/2,
    A(w)=(2w^2-1)^2,
    P(w)=V(w)^n A(w)^m=sum_(j=0)^N p_j w^j,
    N=2n+4m.

All p_j are rational. Since n is even, the saved coefficient formula for U gives

    p_n=2^(-n) U.

Indeed P(w)=2^(-n)(1-2w+2w^2)^n(1-2w^2)^(2m), and changing w to -w does not change the coefficient of degree n.

Integrating this finite Laurent polynomial along the preserved segment gives the exact identity

    J_n(m)=R_complex+2^(-n)U Log(1+i),

    R_complex=sum_(j!=n) p_j
       [alpha^(j-n)-(1/2)^(j-n)]/(j-n) in Q(i).

The logarithm is the continuation on that segment, hence

    Log(1+i)=(log 2)/2+i*pi/4.

Thus, for r=Im R_complex in Q,

    Im J_n(m)=r+U*pi/2^(n+2).                         (2.1)

The exact logarithmic companion identity is

    F=U(beta-pi)=-2^(n+2) Im J_n(m),
    beta=-2^(n+2)r/U in Q.                            (2.2)

The sign in (2.2) includes both conjugate paths: the moment integral equals the difference of the upper path and its conjugate. Equivalently, apply n integrations by parts to the saved complete moment identity; n is even here.

Since pi is irrational and U!=0, (2.1) proves

    Im J_n(m)!=0.                                    (2.3)

At integer m, a matching parity crossing is equivalent to Im J_n(m)=0. Consequently there are no exact eligible integer coincidences with the crossing sets. This improves the previous qualitative status. It gives no uniform lower bound on their positive distances.

The real part of the same identity involves log 2, but no independent arithmetic relation between the two rational endpoint expressions is supplied. Treating the complex integral as a Gaussian rational would incorrectly discard its logarithmic term.

## 3. What quantitative arithmetic would actually suffice

Write B_m=den(beta_m). The saved moment arithmetic gives

    B_m divides O_N |U_m|/2,
    O_N=lcm{odd positive integers <=N},
    O_N<=4^N.

Hence, in this block,

    log B_m <= 4rho log 4 T+o(T)=8a_rho T+o(T).       (3.1)

Suppose one separately proves a quantitative estimate

    |pi-p/q| >= C q^(-mu)                            (3.2)

for all relevant rationals, with fixed mu and C>0. No numerical value of mu or unexamined external theorem is being asserted here. If the ACTUAL B_m obeyed log B_m<=b T+o(T), then (2.2), the saved saddle magnitude, and log|U_m|=o(T) would imply

    sin(delta_n(m)) >= exp(-(a_rho+mu b)T+o(T)).      (3.3)

The slope conversion changes this exponent only by o(T). Thus this route would close the earlier avoidance gap provided

    mu b < min(2a_rho,1).                            (3.4)

The existing bound b=8a_rho does not meet (3.4), even for an optimistic exponent mu>=1. The endpoint rationality identity and its present denominator upper bound therefore do not supply the required separation. This is a failure of the available quantitative budget, not a proof that stronger arithmetic is impossible.

A potentially sufficient new input is a much smaller actual logarithmic denominator, together with a suitable approximation bound for pi. Another is a direct lower bound for these particular endpoint linear forms stronger than a denominator-only estimate. Qualitative irrationality supplies (2.3), but not (3.4).

## 4. Exact adjacent-selector combination and primitive polynomial height

Every nonzero rational combination can be rescaled to coprime integers a,b. Put h=max(|a|,|b|)>=1 and

    L=L_m(a+b L_1),
    L_1=(2t^2-4t+1)^2
       =4t^4-16t^3+20t^2-8t+1.

Its polynomial coefficient content is exactly

    c=gcd(a+b,4), in {1,2,4}.                        (4.1)

Indeed L_m is primitive, so Gauss's content identity reduces the question to a+b L_1. The gcd of its nonconstant coefficients is 4|b|, and gcd(a+b,b)=1. The same formula covers b=0. The primitive selector is L/c.

Let H_sel be its coefficient l1 height. For m>=1,

    e^(-4) 7^(2m)h/[3c(m+1)]
        <= H_sel <= 50 7^(2m)h/c.                    (4.2)

The upper estimate follows from ||L_m||_1=7^(2m) and ||L_1||_1=49. To prove the lower estimate, evaluate at -1 and at -r, r=m/(m+1). Put p(r)=2r^2+4r+1. Then

    L_m(-1)=7^(2m),
    L_m(-r)=p(r)^(2m)>=e^(-4)7^(2m),
    49-p(r)^2>=70/(m+1).

For the middle inequality, on [1/2,1], p'/p<=12/7, so integration gives an exponent loss at most 24/7. The last inequality follows from 7-p(r)=8/(m+1)-2/(m+1)^2 and 7+p(r)>=21/2. If Q0=a+49b and Q1=a+p(r)^2 b, these bounds give h<=3(m+1)max(|Q0|,|Q1|). Evaluation inside the unit disk is bounded by coefficient l1 height, proving (4.2).

In particular,

    log H_sel=2m log 7+log h-log c+O(log(m+1)).       (4.3)

Large cancellation coefficients do not disappear when the selector is made primitive: polynomial content removes at most a factor four.

## 5. Complete companions and nonzero forcing

For each j, expand

    B_j(t)=(1-2t+2t^2)^n(1-4t+2t^2)^(2(m+j))
           =sum_l b_(j,l)t^l,
    N_j=2n+4(m+j),
    K_j=t^n B_j^(n)/n!,
    U_j=K_j(1).

The exact complete companions are

    X_j=sum_(l=n)^N_j binom(l,n)b_(j,l)
                       sum_(r=0)^l 1/r!,
    Y_j=calL((K_j-U_j)/(t-1)),
    calL(g)=integral_-1^1 g((1+iu)/2)du.              (5.1)

For the pair define

    U_ab=aU_0+bU_1.

The necessary and sufficient forcing condition is U_ab!=0. The only forbidden primitive coefficient direction is

    (a,b)=+/- (U_1/g_U,-U_0/g_U),
    g_U=gcd(U_0,U_1).                                (5.2)

If a,b have opposite parity, then v2(U_ab)=n/2, so forcing is automatically nonzero. When both are odd, their actual sum must be checked.

When U_ab!=0, the primitive selector L/c has forcing U_ab/c and EXACT rational companions

    alpha_ab=(aX_0+bX_1)/U_ab,
    beta_ab=(aY_0+bY_1)/U_ab,
    c_ab=(aZ_0+bZ_1)/U_ab,
    c_ab-S=(aR_0+bR_1)/U_ab.                         (5.3)

The factor c cancels. No rational endpoint correction is present for these direct selectors.

Set Lambda_j=2n+8(m+j). The saved entire exponential-tail bound gives

    |E_j| < Ebar_j,
    Ebar_j=3 Lambda_j^n exp(Lambda_j/(n+1))
                  /[(n+1)(n!)^2].                  (5.4)

Thus |aE_0+bE_1|<=h E_*, where E_*=Ebar_0+Ebar_1. No exponential term is dropped when combining the selectors.

## 6. Complete-companion determinant and the dyadic exception

Put Jfac=n+4m and N=2n+4m. The saved unique-lowest-term calculation, before division by U, states

    v2(X_0)=t_0=N/2-v2(n!)-v2(Jfac!),
    v2(Y_j)>=1.

Here t_0<0. At the adjacent index,

    t_1=v2(X_1)=t_0-d,
    d=v2(Jfac+4)-1>=1.                              (6.1)

Indeed the four new factorial factors have total valuation 1+v2(Jfac+4), whereas the numerator gains two powers of two. Consequently v2(Z_j)=t_j. On an eligible adjacent pair,

    Delta=U_0Z_1-U_1Z_0!=0,
    v2(Delta)=n/2+t_1.                              (6.2)

The two terms in Delta have different valuations. This proves noncollinearity of the COMPLETE rational companions, not of their logarithmic components alone.

For any nonzero-forcing combination, its actual denominator obeys exactly

    v2(q_ab)=[v2(U_ab)-v2(aZ_0+bZ_1)]_+.            (6.3)

If the two numerator valuations differ, the smaller is the valuation of their sum. With primitive a,b, equality is possible only in the case

    a odd, v2(b)=d.                                 (6.4)

Outside (6.4),

    v2(aZ_0+bZ_1)<=t_0,
    v2(q_ab)>=n/2-t_0
       =3n/2+2m-s2(n)-s2(n+4m).                    (6.5)

This includes zero coefficients, with the usual infinite valuation convention. Thus the earlier dyadic denominator floor persists for every primitive coefficient direction except the explicitly identified tie.

In the tie write b=2^d b0, where b0 is odd, and

    w0=2^(-t_0) Z_0,
    w1=2^(-t_1) Z_1.

Both w0,w1 are rational dyadic units. Let zeta=v2(a w0+b0 w1)>=1, allowing infinity if the sum is zero. Then U_ab has valuation n/2 and

    v2(q_ab)=[n/2-t_0-zeta]_+.                       (6.6)

After clearing a common odd denominator, zeta>=k is precisely one congruence

    a v0+b0 v1=0 modulo 2^k,

with v0,v1 odd integers. This congruence lattice has index 2^k. Its index alone does not lower-bound the height of its shortest primitive solution; exceptional small solutions can exist. To obtain substantial denominator savings, the same coefficients must satisfy this congruence and the required real cancellation. No simultaneous approximation theorem accomplishing that is supplied here.

## 7. Exact final reduction, endpoint height, and rational surjectivity

Let

    O=O_(N+4),
    D=n!(Jfac+4)! O,
    A_j=D Z_j in Z.

Integrality follows from (5.1): the exponential numerator denominator divides n!(n+4(m+j))!, while the logarithmic numerator has only odd denominator dividing O. The latter fact uses the saved moment valuation v2(Y_j)>=1.

For primitive a,b with U_ab!=0 put

    g=gcd(aA_0+bA_1, D U_ab)>0.

Then, after complete rational reduction,

    q_ab=D|U_ab|/g,
    q_ab |c_ab-S|=D|aR_0+bR_1|/g.                   (7.1)

The height of the primitive rational endpoint pair is exactly

    H_end=max(|aA_0+bA_1|,D|U_ab|)/g.                (7.2)

When c_ab stays bounded, H_end and q_ab differ by a bounded factor. In general,

    H_end <= D h max(|Z_0|+|Z_1|,|U_0|+|U_1|)/g.

Neither D nor U_ab is the reduced denominator. Dividing the selector by its content c divides the raw endpoint pair and its gcd by the same factor, leaving (7.1) unchanged.

The integer endpoint matrix with columns (A_j,D U_j) has determinant

    -D^2 Delta !=0.

Because (a,b) is primitive, it can be completed to a unimodular matrix. Therefore

    g divides |D^2 Delta|.                           (7.3)

This is an exact restriction, not a favorable estimate on g for chosen coefficients.

There is also an explicit inverse. For any reduced rational p/q, q>0, take

    a=q A_1-pD U_1,
    b=pD U_0-q A_0,                                 (7.4)

and divide these two integers by their gcd. Before that division, the resulting endpoint pair is (pD^2 Delta,qD^2 Delta), so U_ab!=0 and c_ab=p/q exactly.

Thus this two-selector family parametrizes every rational center after unrestricted rational combination. This fact does not supply good approximants to S. It shows why arbitrary coefficient cancellation alone cannot carry an irrationality argument: the needed reduced rational approximation quality has to be proved, not inferred from the representation.

The available common clearer is expensive:

    log D=4rho n(log n)^2(1+o(1)).                   (7.5)

Its factorial part dominates. No claim that q_ab has this size is made. Any improvement over it requires the actual gcd or a sharper direct denominator calculation.

## 8. Complete asymptotic budget with normalization retained

Define

    G=2^(n+2)(|J_n(m)|+|J_n(m+1)|),
    U_*=|U_0|+|U_1|,
    E_*=Ebar_0+Ebar_1.

The preserved saddle magnitude, adjacent rotation, forcing bound, and complete exponential bound imply

    log G=a_rho T+o(T),
    log U_*=o(T),
    log E_*=-T+o(T),
    max(|F_0|,|F_1|)>=c0 G                         (8.1)

for some fixed c0>0 and all sufficiently large n. The last statement is the saved adjacent rotation consequence, not a new phase scan.

For coefficients a,b, put

    eta=|U_ab|/(h U_*),  0<eta<=1,
    tau=|aF_0+bF_1|/(h G).

From the COMPLETE identity (5.3), bounded primitive magnitude at most H necessarily implies

    tau <= H eta U_*/(q_ab G)+E_*/G.                 (8.2)

Outside the dyadic tie, (6.5) and eta<=1 imply

    tau <= exp(-min(3a_rho,1+a_rho)T+o(T)).          (8.3)

This is the same required precision as the isolated-crossing problem. Rational coefficients change the variable being tuned; they do not remove the precision requirement.

For a sufficient triangle-bound certificate, suppose actual information gives

    q_ab<=exp(d_q T+o(T)),
    eta>=exp(-ell T+o(T)),
    tau<=exp(-t T+o(T)).

Then both complete contributions tend to zero if

    t>d_q+ell+a_rho,
    d_q+ell<1.                                     (8.4)

If the second condition is unavailable, the entire residual R must be cancelled, including E. Absolute factorial accuracy of the exponential companion alone is insufficient.

An equivalent coefficient/gcd version is useful. Set h=exp(sT+o(T)) and D/g=exp(rT+o(T)) when these rates are finite. Then (7.1) gives the sufficient conditions

    t>r+s+a_rho,
    r+s<1.                                         (8.5)

Here r need not be positive. For an approximation estimate supplying tau<=h^(-2), the budget becomes

    s>r+a_rho,
    s<1-r.                                         (8.6)

A nonempty interval in (8.6) requires 2r+a_rho<1. These are sufficient bounds using the stated estimates, not universal necessary coefficient lower bounds. An exceptionally good rational approximation can beat h^(-2), and exceptionally favorable endpoint gcds can change r.

## 9. Logarithmic cancellation: its arithmetic direction and coefficient cost

Define the rational determinant

    Delta_F=U_0Y_1-U_1Y_0.

If Delta_F=0, both logarithmic companions beta_j are equal. Every nonzero-forcing combination has this same beta. In particular, cancelling its logarithmic numerator exactly also cancels forcing. No logarithmic improvement is available in this case.

If Delta_F!=0, choose the ordering so that |F_1|=max(|F_0|,|F_1|), and put x=-F_0/F_1. Then |x|<=1. The number x is a nonconstant rational fractional-linear transform of pi, hence irrational. Its continued-fraction convergents b/a, a>0, satisfy

    |a x-b|<1/a,
    |aF_0+bF_1|<|F_1|/a,
    tau=O(h^(-2)), h comparable to a.               (9.1)

This is a legitimate coefficient-accuracy tradeoff. It is not a lower bound on the coefficients needed by every possible cancellation.

The forcing direction must also be controlled. Exactly,

    U_0+xU_1=Delta_F/F_1.

Since O Y_j are integers, O Delta_F is integral. Therefore, if Delta_F!=0,

    |Delta_F|>=1/O.

For a convergent satisfying a^2>=2|U_1F_1|/|Delta_F|, the forcing obeys

    |U_ab|>=a |Delta_F|/(2|F_1|).

Thus one obtains a coarse bound

    eta>=exp(-(9a_rho)T+o(T)).                       (9.2)

Here log O<=8a_rho T+o(T) and log G=a_rho T+o(T). Formula (9.2) is only a worst-case transversality guarantee. It can be far too weak for (8.4). It is not a determination of the actual eta.

There is a transparent obstruction using the available clearer without any favorable gcd information. Dirichlet's theorem, for every integer Q>=1, supplies a nonzero pair with |a|<=Q, |b|<=Q+1 and

    |aF_0+bF_1|<=G/Q.

Whenever its forcing is nonzero, the resulting generic certificate is

    q_ab|c_ab-S| <= D[G/Q+(Q+1)E_*].                 (9.3)

The right side is at least 2D sqrt(G E_*). Its logarithm has positive leading term 4rho n(log n)^2, for every rho>0. Hence no choice of Q makes this particular certificate small. This does NOT lower-bound the actual error. It identifies the inadequacy of combining this generic cancellation bound, this full exponential-error majorant, and no gcd savings.

To beat the logarithmic contribution alone through (9.3) would require Q much larger than DG. At that scale the available exponential bound DQ E_* is enormous. Alternatively, a known gcd lower bound would replace D by D/g, leading precisely to (8.5)-(8.6). Extra cancellation of E, extraordinary rational approximation, or substantial arithmetic reduction is indispensable for this route.

There is also an exact limiting description. Let

    Delta_X=U_0X_1-U_1X_0,
    C_XY=X_0Y_1-X_1Y_0.

As b/a tends to x and Delta_F!=0, the normalized complete error tends to

    (C_XY+pi Delta_X)/Delta_F-e.                     (9.4)

Thus arbitrarily accurate logarithmic cancellation alone leaves a specific full residual. Its vanishing would itself be a rational affine relation between e and pi; it cannot be silently assumed. Formula (9.4) is consistent with the complete exponential bound and explains why cancellation of only the logarithmic saddle does not establish primitive smallness.

## 10. Full-error cancellation and the remaining nonvanishing obligation

By (8.1) and the negligible E_*, at least one R_j has magnitude comparable to G. Choose it as R_1 and put

    x_S=-R_0/R_1.

Since Delta!=0, x_S is a nonconstant rational fractional-linear transform of S. Accordingly,

    x_S is rational if and only if S is rational.   (10.1)

This equivalence concerns this full slope, not the logarithmic-only slope. If a nonzero integer pair cancels R exactly, then its forcing is nonzero by Delta!=0, and c_ab=S is rational. Conversely, if S is rational, such an exact integer cancellation pair exists by (7.4).

For completeness, a rigorous but generic full-error construction is available. Let W=G+E_*; then |R_j|<=W. Given 0<epsilon<1, choose an integer Q>DW/epsilon. Dirichlet applied to x_S gives a nonzero pair with |a|<=Q, |b|<=Q+1 and

    |aR_0+bR_1|<=W/Q,
    D|aR_0+bR_1|<epsilon.                           (10.2)

The forcing cannot vanish: if U_ab=0, then D(aR_0+bR_1)=aA_0+bA_1 is a nonzero integer, by the nonzero endpoint determinant, contradicting (10.2). After making the pair primitive, (7.1) gives

    q_ab|c_ab-S|<epsilon.

This statement allows the value zero. It is the general Dirichlet approximation mechanism expressed in the adjacent-selector coordinates. It does not prove that these forms are nonzero, or prove irrationality of S.

For fixed epsilon, the guaranteed coefficient budget is

    log h <= log D+log G+O(1)
           =4rho n(log n)^2(1+o(1)),
    log q_ab <= 2log D+log G+o(T).

For epsilon depending on n, add log(1/epsilon) to the first bound and to the corresponding second bound. The selector's primitive polynomial height must additionally include 2m log 7 from (4.3). This quantifies a valid full-error construction while exposing its lack of new nonvanishing information and its high coefficient cost.

Any use of a numerically or analytically approximated slope must also retain its certified error. If |x_hat-x_S|<=epsilon_x, the extra raw residual is at most h W epsilon_x. Without favorable gcd information, a primitive-error certificate of size epsilon therefore needs

    epsilon_x <= epsilon/(D h W).

At the generic h of order DW/epsilon, this is precision of order epsilon^2/(D^2 W^2). The saved leading relative saddle error O(1/n), even with derivative control, is vastly too large. No cancellation of just that leading term certifies (10.2).

## 11. Precise stopping conclusion

The new qualitative separation theorem is (2.3): exact eligible integer crossings do not occur. Exponentially close crossings remain unexcluded.

The adjacent-selector alternative is now completely reduced to explicit quantities: primitive polynomial content (4.1), coefficient height (4.2), nonzero forcing (5.2), full companions (5.3), exact reduced denominator/gcd (7.1), and complete cancellation budgets (8.4)-(8.6). The complete endpoint determinant is nonzero, while the logarithmic-only determinant has not been proved nonzero and is treated by cases.

The indispensable additional arithmetic can take one of these concrete forms:

1. A lower bound for the specific pi endpoint forms beating (3.4), with their actual logarithmic denominators controlled.
2. Coefficients satisfying sufficiently accurate complete cancellation together with an actual gcd/denominator estimate meeting (8.4) or (8.5), and a nonzero complete primitive form.
3. In the dyadic tie, a simultaneous real approximation and high-order dyadic congruence calculation; the single-selector denominator law cannot simply be transferred through this exception.

None of these is supplied by monotonicity, curvature, a finite saddle expansion, polynomial content, or the existence of rational combinations. The generic full-error construction in Section 10 is valid but permits zero and is equivalent in scope to ordinary rational approximation. No conclusion about the rationality or irrationality of e+pi follows.

## 12. Sources and preservation

Exact complete endpoint and height inputs: ../DIRECT_SELECTOR_HEIGHT_OBSTRUCTION_DRAFT.md; ../LARGE_SELECTOR_EXPONENTIAL_REMAINDER_DRAFT.md; ../LARGE_SELECTOR_DYADIC_DENOMINATOR_DRAFT.md. These were read as research sources, not independently reviewed in this assignment.

Preserved analytic inputs: LARGE_SELECTOR_RELATIVE_SADDLE.md; LARGE_SELECTOR_PHASE_CROSSINGS.md; LARGE_SELECTOR_BLOCK_NONCANCELLATION.md. No continuation proof, saddle proof, counting argument, or numerical control was replayed.

The earlier PHASE_CROSSING_ARITHMETIC_BYPASS_WORKING.md remains a preliminary ledger. This final note supplies its proofs, qualifications, and completed coefficient budget. Saving and read-back are recorded by the application separately; mathematical status remains author deductions.
