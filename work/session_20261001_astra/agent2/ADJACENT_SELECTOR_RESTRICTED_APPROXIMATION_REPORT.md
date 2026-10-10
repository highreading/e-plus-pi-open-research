> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Restricted approximation report

Status: new author deductions, not independently reviewed. Main proof: ADJACENT_SELECTOR_RESTRICTED_APPROXIMATION.md. The preceding ADJACENT_SELECTOR_DYADIC_TUNING.md and its completed operations are preserved. No numerical scan or generic Dirichlet construction was repeated.

The actual saving coordinates remain

    b=2^d(r_k a+2^k l), a>0 odd, gcd(a,l)=1,
    h=max(a,2^d|r_k a+2^k l|).

For R_1!=0 put

    y=(-R_0/(2^d R_1)-r_k)/2^k,
    z=R_0/R_1, C=max(1,|z|), M=2^(d+k),
    e=l-a y.

The COMPLETE identities are

    b=-z a+M e,
    q_red|c-S|=C_2|R_1||e|/chi,
    C_2=D/2^(N/2+2), chi=g/g_k>=1,
    g_k=2^(N/2+d+2+k).

Thus the modulus is offset by the guaranteed endpoint gcd on the error side, while it remains in the original weighted height. The actual extra gcd chi, including odd-prime reduction, remains explicit.

NEW SHARP ODD-DENOMINATOR THEOREM. Let p_j/q_j be the last convergent with q_j<=Q<q_(j+1), let alpha be its next complete quotient, and define the minimum of |p-qy| over reduced fractions with odd 1<=q<=Q. If q_j is odd, the minimum is

    1/(q_j alpha+q_(j-1)).

If q_j is even, put t=floor((Q-q_(j-1))/q_j). The minimum is exactly

    (alpha-t)/(q_j alpha+q_(j-1)),

attained by the reduced odd intermediate fraction

    (p_(j-1)+t p_j)/(q_(j-1)+t q_j).

This optimizes over all odd denominators, not just convergents. It follows by expressing every integer pair in the unimodular basis of consecutive convergents.

QUANTIFIED LOSS AND PRECISE OBSTRUCTION. The loss Q times this minimum is less than one when the active denominator is odd, and less than a_(j+1)+1 when it is even. If an even denominator is followed by a partial quotient A>=4, a suitable cap has loss at least A/12. Consequently, for an irrational slope, a uniform finite loss relative to 1/Q exists exactly when the partial quotients following even convergent denominators are bounded. No uniform fixed-loss theorem applies to all irrational slopes.

EXACT WEIGHTED CRITERION. Write

    (l,a)=u(p_j,q_j)+v(p_(j-1),q_(j-1)).

Then primitivity is gcd(u,v)=1, oddness is u q_j+v q_(j-1) odd, and the residual is (u-v alpha)(p_j-q_j y). Retaining the exact inequalities a<=H and |-z a+M e|<=H gives an exact finite criterion. The coordinates are bounded by

    |v|<=H|p_j-q_j y|+q_j delta,
    |u|<=H|p_(j-1)-q_(j-1)y|+q_(j-1)delta,

for |e|<delta. The paper also gives its exact actual-gcd version and inner/outer denominator caps that handle the weighted boundary without replacing it by an unweighted assumption.

NEW SUFFICIENT CERTIFICATE. Let mu be the positive odd-denominator minimum at cap Q. If

    C Q+M mu<=H,
    C_2|R_1| mu<epsilon,

the explicit minimizing fraction yields original height at most H and a nonzero complete primitive error below epsilon. A local next-partial-quotient bound supplies mu<L/Q with L=1 or A+1 as above.

At the preceding budget H0=DW/epsilon, W>=max(|R_0|,|R_1|), choose Q=floor(H0/(2C)) and assume H0/(2C)>=2. The explicit sufficient conditions

    L<2^(N/2), 8 C M L<=H0^2

then meet both budgets. These are conditional, finite arithmetic criteria. No bound for the actual slope's relevant partial quotient or the potentially large ratio C has been asserted.

RATIONAL CASES. If y=P/Q0 is reduced with Q0 even, all odd denominators have error at least 1/Q0, attained by a primitive Bezout pair. If Q0 is odd, the sole reduced zero-error pair is (l,a)=(P,Q0), with height C Q0; every nonzero error is at least 1/Q0. The paper provides exact determinant/congruence criteria with the weighted height for all rational cases. The zero pair is the full-error annihilator, distinct from the complete rational-numerator annihilator giving center zero. If R_1=0, the residual is aR_0 and must be handled directly.

Since the endpoint determinant is nonzero, y is rational exactly when e+pi is rational. The paper does not assume its irrationality. Positive-error conclusions are proved only under the displayed sufficient hypotheses; they do not supply a family-wide nonvanishing theorem.

The remaining arithmetic is sharply identified: control the actual relevant parity/partial-quotient data, satisfy the exact weighted criterion, or establish enough extra endpoint gcd to compensate. Odd-prime denominator reduction and complete-form nonvanishing remain separate obligations. No conclusion about rationality or irrationality of e+pi follows.
