> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Adjacent selectors: restricted approximation after dyadic tuning

Status: new author deductions, not independently reviewed. ADJACENT_SELECTOR_DYADIC_TUNING.md, its lattice, height criterion, annihilator directions, and completed operations remain unchanged. This note proves an exact odd-denominator approximation theorem, an exact criterion retaining the original weighted height, and conditional complete-error certificates. No numerical scan, generic Dirichlet construction, or independent review is repeated.

The complete residual slope is not assumed irrational. Its rationality is equivalent to that of S=e+pi. Rational cases and exact annihilators are therefore part of the statements, not excluded exceptions.

## 1. Preserved coordinates and exact primitive error

Use the notation of ADJACENT_SELECTOR_DYADIC_TUNING.md for a parity-eligible adjacent pair. In particular,

    r=n/2, J=n+4m, N=2n+4m,
    t0=N/2-v2(n!)-v2(J!),
    d=v2(J+4)-1>=1, B=r-t0,
    U_j=2^r u_j, u_j odd,
    X_j=U_j alpha_j, Y_j=U_j beta_j, Z_j=X_j+Y_j,
    R_j=Z_j-S U_j.

Both X and Y are the COMPLETE rational companion numerators. The nonzero complete endpoint determinant is

    Delta=U_0 Z_1-U_1 Z_0.

Write Z_0=2^t0 gamma v0 and Z_1=2^(t0-d) gamma v1, where v0,v1 are coprime odd integers and gamma is a rational dyadic unit. Fix 1<=k<=B, and put

    K=2^k, M=2^(d+k),
    r_k=-v0 v1^(-1) modulo K.

The preserved saving lattice is

    Lambda_k={2^d v0 a+v1 b=0 modulo M}.

Use its actual coordinates

    b=2^d(r_k a+K l).

Primitive members, after changing overall sign if necessary, are exactly

    a>0 odd, gcd(a,l)=1.                             (1.1)

Their forcing is nonzero and has valuation r. Their polynomial content is one. Their original coefficient height is exactly

    h(a,l)=max(a,2^d|r_k a+K l|).                    (1.2)

The primitive selector polynomial height retains the preserved bounds

    exp(-4)7^(2m)h/[3(m+1)] <= H_sel <=50 7^(2m)h,
    log H_sel=2m log 7+log h+O(log(m+1)).             (1.3)

Let

    D=n!(J+4)! O_(N+4), A_j=D Z_j,
    g=gcd(aA_0+bA_1,D(aU_0+bU_1)),
    g_k=2^(N/2+d+2+k),
    C_2=D/2^(N/2+2).

The established dyadic theorem gives g_k|g. Define the positive integer

    chi(a,l)=g/g_k.

Then, with q_red the actual positive reduced center denominator,

    q_red=D|aU_0+bU_1|/g,
    q_red|c-S|=D|aR_0+bR_1|/g.                     (1.4)

Assume initially R_1!=0, and define the COMPLETE slope and its normalization

    z=R_0/R_1,
    y=(-R_0/(2^d R_1)-r_k)/K,
    C=max(1,|z|).

For e=l-a y, the exact identities are

    b=-z a+M e,
    aR_0+bR_1=M R_1 e,
    h=max(a,|-z a+M e|),                            (1.5)
    q_red|c-S|=C_2 |R_1| |e|/chi(a,l).              (1.6)

Thus the modulus M is offset on the error side by the guaranteed endpoint gcd: (D/g_k)M=C_2. It remains explicitly in the coefficient height. Additional odd and dyadic reduction is retained in chi, not assumed absent or favorable.

For target epsilon>0, define

    delta=epsilon/(C_2|R_1|).                       (1.7)

The condition 0<|e|<delta is a sufficient complete primitive-error certificate using only the known gcd divisor. The exact condition is 0<|e|<delta chi(a,l).

Changing r_k to r_k+K t changes y to y-t and l to l-t a. It changes none of the height, residual, parity, or primitivity conditions.

## 2. Continued-fraction conventions

For a real y, use its ordinary simple continued fraction, with floor as the first partial quotient, including negative y. Write

    y=[a0;a1,a2,...],
    p_-1=1, q_-1=0, p_0=a0, q_0=a0_den=1,
    p_(j+1)=a_(j+1)p_j+p_(j-1),
    q_(j+1)=a_(j+1)q_j+q_(j-1).

Here a0_den is only a reminder that q_0=1; it is not a further partial quotient. In all formulas below the denominator is denoted q_j. Consecutive columns (p_j,q_j),(p_(j-1),q_(j-1)) have determinant +/-1.

For rational y choose the finite expansion with last partial quotient at least two, except for integer y. If j is nonterminal, define the complete quotient

    alpha=[a_(j+1);a_(j+2),...],
    E_j=p_j-q_j y.

Then

    E_(j-1)=-alpha E_j,
    |E_j|=1/(q_j alpha+q_(j-1)).                    (2.1)

These follow by substituting

    y=(p_j alpha+p_(j-1))/(q_j alpha+q_(j-1)).

For a denominator cap Q>=1, choose the largest j with q_j<=Q. When a next denominator exists and Q<q_(j+1), this removes the harmless initial equality q_0=q_1=1. An index with q_j even necessarily has j>=1 and q_(j-1)>0.

## 3. Exact best approximation with odd denominator

Define the unweighted odd-denominator error envelope

    mu_odd(y,Q)=min{|p-q y|:
                    1<=q<=Q, q odd, p in Z, gcd(p,q)=1}.

Zero is permitted in this definition. The following theorem identifies a minimizer; no claim of uniqueness is needed.

THEOREM 1. Suppose j is nonterminal and

    q_j<=Q<q_(j+1).

Put A=a_(j+1) and alpha as in Section 2.

(a) If q_j is odd, then

    mu_odd(y,Q)=|E_j|=1/(q_j alpha+q_(j-1)),         (3.1)

attained by p_j/q_j.

(b) If q_j is even, then q_(j-1) is odd. Define

    t=floor((Q-q_(j-1))/q_j), 0<=t<=A-1.

Then

    mu_odd(y,Q)=(alpha-t)/(q_j alpha+q_(j-1)),       (3.2)

attained by the reduced intermediate fraction

    (p_(j-1)+t p_j)/(q_(j-1)+t q_j).                (3.3)

In particular, the theorem includes coprimality rather than imposing it after obtaining a nonprimitive vector.

Proof. Every integer pair (p,q) has unique coordinates

    (p,q)=u(p_j,q_j)+v(p_(j-1),q_(j-1)).

Its error equals (u-v alpha)E_j. The coordinate change is unimodular.

First disregard parity. If v=0 and q>0, then u>=1, so the error modulus is at least |E_j|. If v>=1 and q<q_(j+1)=A q_j+q_(j-1), then u<=A-1. Since alpha>=A, v alpha-u>=1. If v<=-1, q>0 forces u>=1, and u-v alpha>=1. Thus every positive denominator below q_(j+1) has error at least |E_j|. This proves (a), because its proposed minimizer is reduced and has odd denominator.

For (b), odd q forces v odd, because q_j is even and q_(j-1) is odd. If v>=1, q<=Q implies

    u<=floor((Q-v q_(j-1))/q_j)<=t,

and hence v alpha-u>=alpha-t. If v<=-1, positivity of q forces u>=1, giving u-v alpha>=1+alpha>alpha-t. The choice (u,v)=(t,1) has the required denominator and attains equality. Its coordinates are coprime, so the fraction is reduced. This proves (b).

This proof also works for rational y before its terminal denominator: alpha can be an integer at the last step.

## 4. Exact parity obstruction and quantified loss

For a nonterminal interval in Theorem 1 define

    L(y,Q)=Q mu_odd(y,Q).

This is the exact loss relative to the reference error scale 1/Q.

If q_j is odd, (3.1) gives L<1. If q_j is even, put beta=q_(j-1)/q_j. Then

    L=(Q/q_j)(alpha-t)/(alpha+beta),
    t=floor(Q/q_j-beta).                            (4.1)

In particular,

    L<A+1.                                         (4.2)

Indeed mu_odd<=alpha/(q_j alpha+q_(j-1))<1/q_j and Q/q_j<A+beta<A+1.

The EXACT obstruction to a positive-error odd reduced fraction with denominator at most Q and error less than delta, in a nonterminal interval, is

    q_j odd: 1/(q_j alpha+q_(j-1)) >=delta;

    q_j even: (alpha-t)/(q_j alpha+q_(j-1)) >=delta. (4.3)

Conversely, reversing the corresponding inequality supplies the explicit fraction in Theorem 1. Large partial quotients matter here precisely when the current convergent denominator is even.

The loss can be arbitrarily large for irrational slopes. If q_j is even and A=a_(j+1)>=4, take

    t=floor(A/2), Q=q_(j-1)+t q_j.

Then (4.1), alpha in [A,A+1), and 0<beta<1 imply

    L=(t+beta)(alpha-t)/(alpha+beta)
      >= (A/2-1)(A/2)/(A+2)
      >= A/12.                                     (4.4)

Thus a large next partial quotient following an even denominator produces a proved interval of poor restricted approximation. Intermediate fractions do not eliminate the obstruction: (3.2) already optimizes over every odd denominator below Q.

For an explicit family showing the obstruction among irrational numbers, one may take the exact continued fractions [0;2,A,1,1,1,...]. Their q_1=2 is even, and (4.4) applies as A increases. This is an analytic family, not a numerical experiment and not a claim about the actual residual slope.

COROLLARY 1. For a fixed irrational y, a finite constant L_* such that

    mu_odd(y,Q)<=L_*/Q for every integer Q>=1        (4.5)

exists if and only if the partial quotients a_(j+1) at indices with q_j even are bounded.

For sufficiency, use (3.1) and (4.2). For necessity, apply (4.4) to any unbounded sequence of those partial quotients. Large partial quotients following odd denominators cause no such loss, since the excellent odd convergent remains available throughout the interval.

This is a restricted approximation theorem with an explicit loss and a precise obstruction to a uniform loss. It makes no assertion that the required partial-quotient condition holds for the complete selector slope.

## 5. Rational slopes, positive errors, and exact annihilators

Let y=P/Q0 in lowest terms, Q0>0. Every candidate has

    e=l-a y=j/Q0,
    j=Q0 l-P a in Z.                               (5.1)

This is a complete arithmetic description, including zero.

If Q0 is even, P is odd. For odd a the integer j is odd and nonzero, so

    |e|>=1/Q0.                                     (5.2)

The lower bound is attained by a Bezout pair with 1<=a<=Q0-1 odd. For example, solve P a=-1 modulo Q0, take that odd representative, and put l=(P a+1)/Q0. The determinant j=1 ensures gcd(a,l)=1. Consequently mu_odd(y,Q)=1/Q0 for every Q>=Q0. There is no arbitrarily small odd-denominator error at any height.

If Q0 is odd, the unique reduced positive-denominator zero-error pair is

    (l,a)=(P,Q0).

It is a primitive saving vector. Its original height is

    h_zero=max(Q0,2^d|r_k Q0+K P|)=C Q0.            (5.3)

It gives an exact COMPLETE error annihilator, not a nonzero small form. If zero is excluded, every error again satisfies |e|>=1/Q0. A Bezout solution with j=1 can be chosen with a odd and 1<=a<=2Q0-1: its solutions are periodic modulo Q0, and adding Q0 changes parity. This includes integer y, where one can take a=1 and l=P+1.

Thus nonzero error 1/Q0 is attained at height at most

    C(Q0-1)+M/Q0,       Q0 even,
    C(2Q0-1)+M/Q0,      Q0 odd.                      (5.4)

These are sufficient bounds; the exact signed height can be smaller.

For arbitrary rational y, height H, and error tolerance delta, an EXACT finite criterion for a nonzero solution is: there exist integers a,j such that

    1<=a<=H, a odd,
    j!=0, |j|<Q0 delta,
    P a+j=0 modulo Q0,
    gcd(a,(P a+j)/Q0)=1,
    |-z a+(M/Q0)j|<=H.                             (5.5)

For the actual-gcd criterion replace |j|<Q0 delta by |j|<Q0 delta chi. This does not discard a possible favorable odd gcd.

The rational cases are logically necessary. Since Delta!=0, the maps S to z and then y are nonconstant rational fractional-linear maps when R_1!=0. Therefore

    y rational if and only if S rational.           (5.6)

We do not assume either side is irrational. The exact slope pair with odd Q0 is the same full-error annihilator classified in the preserved dyadic paper. Its lattice membership corresponds to that paper's reduced-denominator condition on a rational S. If Q0 is even, no full-error annihilator is present in the saving lattice.

The complete rational-NUMERATOR annihilator remains the different direction (a,b) proportional to (v1,-2^d v0), normalized to a>0. It belongs to every saving lattice, has center zero, and gives primitive error |S|. It must not be identified with e=0. The forcing annihilator has no primitive member in these saving lattices.

## 6. Exact continued-fraction criterion retaining the weighted height

Theorem 1 solves the denominator-capped error problem. The original weighted height depends also on the sign of the error, so its exact criterion must retain that sign.

THEOREM 2. Fix any nonterminal convergent index j of y, with alpha and E_j as in Section 2. Put

    a=u q_j+v q_(j-1),
    e=(u-v alpha)E_j.                               (6.1)

There is a primitive saving vector with h<=H and 0<|e|<delta if and only if there are integers u,v satisfying

    1<=u q_j+v q_(j-1)<=H,
    u q_j+v q_(j-1) odd,
    gcd(u,v)=1,
    0<|(u-v alpha)E_j|<delta,
    |-z(u q_j+v q_(j-1))+M(u-v alpha)E_j|<=H.       (6.2)

The reconstructed numerator is l=u p_j+v p_(j-1). The search coordinates in (6.2) are necessarily bounded by

    |v|<=H|E_j|+q_j delta,
    |u|<=H|E_(j-1)|+q_(j-1)delta.                  (6.3)

Hence (6.2)-(6.3) are an exact finite arithmetic criterion, not an unweighted proxy.

Proof. The consecutive convergent basis is unimodular, so gcd(l,a)=gcd(u,v). Equation (2.1) proves the error expression. Substitution into (1.5) gives the exact height. Finally, determinant inversion gives, up to signs,

    v=p_j a-q_j l=E_j a-q_j e,
    u=q_(j-1)l-p_(j-1)a=q_(j-1)e-E_(j-1)a.

These prove (6.3). Every reconstruction satisfying (6.2) gives (1.1), so forcing nonvanishing follows from the preserved lattice theorem.

One can choose j with q_j<=H<q_(j+1) to make the bounds particularly useful. This theorem does not claim that checking only convergents suffices at the exact weighted boundary. Arbitrary primitive basis combinations in (6.2) retain any possible boundary solutions.

There is also an exact criterion for the ACTUAL primitive-error inequality. In (6.2) replace delta by delta chi(u,v), evaluated on its reconstructed integer endpoint pair. To keep a fixed finite preliminary box, use

    G_max=|D^2 Delta|/g_k,
    chi<=G_max,                                    (6.4)

from the preserved determinant divisibility g| |D^2 Delta|. The quantity G_max is an integer: g_k divides the determinant, as follows either from its explicit dyadic valuation or by completing any primitive lattice member to a unimodular coefficient pair. Thus (6.3) with delta G_max contains every possible actual-error solution; the final test uses its own chi. This is an exact reduction, not a useful upper estimate for the odd denominator by itself.

For rational integer y, where there is no nonterminal convergent, use the exact determinant criterion (5.5) directly.

## 7. A useful weighted sufficient theorem and exclusion test

Here is a simpler consequence that needs only Theorem 1's explicit best fraction.

THEOREM 3. Let Q>=1. Let l/a be an odd reduced minimizer for mu=mu_odd(y,Q), and suppose mu>0. Then its original coefficients satisfy

    h<=C Q+M mu,
    0<q_red|c-S|<=C_2|R_1| mu.                     (7.1)

In particular,

    C Q+M mu<=H, mu<delta                           (7.2)

is a sufficient condition for the original height-H and error-epsilon target, with nonzero complete form. The minimizer is explicitly provided by Theorem 1 in its nonterminal range, and by Section 5 after an even terminal denominator.

Proof. Use a<=Q and (1.5)-(1.6), with chi>=1. The form is nonzero because mu>0 and R_1!=0. This proves nonvanishing only under this theorem's explicit positive-error hypothesis; it does not establish that such a hypothesis holds for the actual family indefinitely.

For a target tolerance delta with H>M delta, put

    Q_minus=floor((H-M delta)/C),
    Q_plus=floor(min(H,(H+M delta)/C)).              (7.3)

Every candidate with h<=H and |e|<delta has a<=Q_plus. Conversely, every odd reduced pair with a<=Q_minus and |e|<delta has h<=H. Therefore:

* If Q_minus>=1 and 0<mu_odd(y,Q_minus)<delta, there is a valid nonzero complete-error certificate at height H.
* If Q_plus<1, no height-H candidate can satisfy |e|<delta.
* If Q_plus>=1 and mu_odd(y,Q_plus)>=delta, there is no candidate satisfying that error tolerance and height.

The first test must treat a zero minimum separately using Section 5. The exclusion tests concern the given slope-error tolerance, and hence the certificate using g_k. They do not rule out a small actual primitive form obtained through chi>1. The exact criterion in Section 6 retains that possibility.

These tests differ only in an explicit weighted boundary region. Inside that region, Theorem 2 supplies the exact criterion. There is no substitution of an unweighted denominator bound for the original coefficient constraint.

## 8. Restricted approximation with a quantified finite loss

Suppose the active nonterminal convergent at cap Q has odd denominator, or has even denominator with next partial quotient at most A. Set L=1 in the first case and L=A+1 in the second. Theorem 1 gives an odd reduced pair with

    0<|l-a y|<L/Q.

Consequently the following explicit conditions suffice:

    C Q+M L/Q<=H,
    Q>L C_2|R_1|/epsilon.                           (8.1)

The conclusions are the original coefficient-height bound and a NONZERO complete primitive error below epsilon. For irrational y the positive-error condition is automatic. For rational y it holds in a nonterminal interval; terminal cases are handled in Section 5.

This is the requested replacement theorem in a clearly stated scope. It is stronger than the preceding paper's requirement that an odd convergent itself land in a specified interval: when the last convergent is even, the correct intermediate fraction (3.3) is used and is optimal among all odd denominators below the cap. Its loss is exactly (4.1), bounded by the local next partial quotient plus one.

There is no unconditional fixed-loss replacement valid for all irrational slopes. Equation (4.4) proves the obstruction, and (5.2) gives a permanent obstruction for rational slopes with even denominator. Neither follows from a lattice-index argument.

## 9. Application to the preceding complete-error height budget

Retain a bound W>=max(|R_0|,|R_1|) from the complete residual estimates and consider the previous coefficient budget

    H0=D W/epsilon.

This is only a named budget; its unrestricted construction is not repeated. Suppose

    H0/(2C)>=2,
    Q=floor(H0/(2C)).

Then Q>=H0/(4C), and by C|R_1|<=W,

    Q delta>=H0 epsilon/(4C C_2|R_1|)
             >=2^(N/2).                            (9.1)

Let the local active parity/partial-quotient data at this Q provide the positive-error bound mu_odd(y,Q)<L/Q. For example take L=1 for odd active denominator, or L=A+1 for even active denominator and a_(j+1)<=A. If

    L<2^(N/2),
    8 C M L<=H0^2,                                 (9.2)

then the height and complete-error targets at H0 are both attained.

Indeed C Q<=H0/2 and

    M L/Q<=4C M L/H0<=H0/2,

while (9.1) makes L/Q<delta. Theorem 3 or (8.1) completes the proof.

Thus a finite, explicitly quantified local partial-quotient condition is sufficient within the old coefficient budget. Only partial quotients following even denominators require control. A global bounded-partial-quotient hypothesis is unnecessary.

The second inequality in (9.2) retains the actual slope ratio C. If R_1 is extremely small, C can be large; it must not be suppressed merely because log M=O(n log n) and log D has the larger n(log n)^2 scale. When C and L have logarithms O(n log n), the preserved scale of D makes that inequality eventually hold, but this is a stated additional condition, not an automatic fact about every adjacent pair.

The original selector polynomial height then satisfies

    log H_sel<=2m log 7+log H0+O(log(m+1)).           (9.3)

The full denominator still obeys its exact expression in (1.4). The complete-error certificate does not require pretending that q_red is geometric, and it does not settle the odd-prime reduction problem.

The particular y varies with n,m,k and the actual full residuals. No bound for its relevant partial quotients has been proved in this note. Conditions (9.1)-(9.2) make the new sufficient theorem applicable and checkable; they do not silently assume it applies to every selector pair.

## 10. Strong obstruction near an even-denominator convergent

Equation (3.2) is the exact obstruction in terms of the actual continued fraction. There is a complementary finite-height interpretation.

Suppose P/Q0 is reduced with Q0 even. For every odd a<=H and integer l,

    |l-a y|>=1/Q0-H|y-P/Q0|.                       (10.1)

This follows because Q0 l-P a is a nonzero odd integer. Thus if

    H|y-P/Q0|+delta<=1/Q0,

no candidate of original height at most H can have error less than delta. This includes coprime candidates, since the inequality holds even without primitivity.

For an even convergent P/Q0=p_j/q_j, its exact distance to y is

    |y-P/Q0|=1/[Q0(Q0 alpha+q_(j-1))].

Substitution relates (10.1) directly to its next complete quotient. A large next partial quotient creates a long finite-height obstruction. The exact optimum, including its intermediate fractions, remains (3.2); (10.1) is a convenient weaker test.

As before, this excludes the specified slope-error tolerance. If one seeks to defeat it using extra endpoint reduction, the exact necessary compensation is visible from (1.6): chi must exceed C_2|R_1||e|/epsilon. That is an additional arithmetic gcd obligation, not a consequence of rational approximation alone.

## 11. The case R_1=0 and precision of slope input

If R_1=0, the nonzero endpoint determinant gives R_0!=0. Moreover U_1!=0, so S=Z_1/U_1 is rational in this case. The full-error annihilator has coefficient direction (a,b)=(0,1), which belongs to no primitive saving lattice.

For a primitive saving vector, a is positive odd and the residual is aR_0. Its exact nonzero primitive error is

    D a|R_0|/g.

The height remains (1.2), and the exact gcd must be retained. If S=P_S/Q_S in lowest terms, every such nonzero primitive form is at least 1/Q_S. No division by R_1, assertion about a continued fraction of y, or arbitrarily small nonzero-error conclusion is legitimate here.

When R_1!=0 and a certified approximation y_hat satisfies |y-y_hat|<=eta, a tested coefficient pair incurs at most a eta additional slope error. Equation (1.6) bounds the corresponding extra primitive error by

    C_2|R_1| a eta,

using only g_k. Thus a finite continued-fraction prefix or a strict interval test used to certify the theorem must be justified by sufficiently accurate FULL residual data. An uncontrolled leading saddle term cannot establish the needed prefix, partial quotient, or strict error margin. No such numerical certification was performed here.

## 12. New results and remaining arithmetic

The new sharp result is Theorem 1: the best reduced odd-denominator error is either the current odd convergent or a specified intermediate fraction adjacent to an even convergent. It yields the exact finite obstruction (4.3), and Corollary 1 characterizes precisely when a uniform loss relative to 1/Q exists for an irrational slope.

Theorem 2 retains parity, coprimality, signed residual, original weighted coefficient height, and, if desired, the actual endpoint gcd in an exact finite criterion. Theorems 3 and (8.1) give usable sufficient certificates. Section 9 supplies explicit local conditions sufficient inside the preceding height budget, with the modulus and guaranteed gcd counted together.

Rational slopes have a separate complete classification. Even denominator prevents errors below 1/Q0. Odd denominator permits one reduced exact annihilator; excluding that zero form restores the same positive spacing. These cases cannot be removed by assuming the full slope irrational.

For the actual adjacent-selector family, the remaining needed input is now precise: a suitable bound on the particular next partial quotient following an even denominator at the relevant cap, or satisfaction of the exact weighted criterion, or enough additional actual gcd to compensate for its error. No such arithmetic bound for this y is established here. Odd-prime denominator reduction and a family-wide complete-form nonvanishing argument remain separate obligations.

All conclusions are author proofs, not independent review verdicts. No rationality or irrationality conclusion about e+pi follows. The preserved dyadic and earlier analytic files have not been changed.
