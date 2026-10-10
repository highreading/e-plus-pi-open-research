> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete 5-adic factorial survival in the reflected rational center

Original author result L19,2026-10-02. The theorem concerns the ACTUAL reduced denominator after projection, both primitive endpoints and the final gcd. It does not infer q from a raw coefficient clearer. The exact reflected-family interface and dyadic theorem belong to agent2_selector; complete errors and critical rounding belong to agent3_analysis. No independent audit is undertaken and no new prime atlas is run.

The archive/current-primary gate and overlap boundary are in TARGET_LEDGER.md. Falling-factorial congruences, exact rational residue reduction, and separation of primitive pole content from final endpoint content are classical/archived background. The new statement is the projected E unit at5 on n divisible20 and its strict comparison with the COMPLETE rational primitive.

## 1. The actual arithmetic statement

Let n be a positive multiple of20,h>=6,N=n+h,L=h−1,epsilon=(−1)^h, and use the exact reflected kernels

    F0=(1−2w+2w²)^N/[w^(N+1)(1−w)^h], F1=wF0.

Retain selector's definitions

    Ri=Res0 Fi−Res1 Fi,
    Ai=Res1(e^(w−1)Fi), Mi=L! Ai, mi=Mi−L! Ri,
    F=m1F0−m0F1,
    U=M1R0−M0R1>0,
    E=N!Res0(e^w F), Pi=4 Im P((1+i)/2),

where F=P′+r0/w+r1/(w−1). The actual rational center is

    c=−(E/N!+Pi)/U=p_c/q, gcd(p_c,q)=1,q>0.

Then the following EXACT identities hold for every parameter pair in this domain:

    E=epsilon(1−2N²) mod5,                            (1)
    v5(E)=0,
    v5(E/N!+Pi)=−v5(N!),
    v5(q)=v5(N!)+v5(U).                               (2)

In particular

    v5(q)>=(N−s5(N))/4
          >=N/4−floor(log5N)−1,                        (3)

where s5 is the base5 digit sum. The addition of v5(U) in(2) comes AFTER complete numerator cancellation has been excluded. It is not a guess that U is a unit.

## 2. A finite residue proof of the projected E unit

Write the two exact regular factors as

    d(w)=(1−2w+2w²)^N/(1−w)^h=Σ d_j w^j,
    c(u)=(1+2u+2u²)^N/(1+u)^(N+1)=Σ c_j u^j,
    c_(−1)=0.

The complete coefficient interface gives

    M0=epsilon Σ_(j=0)^L c_j(L)_j,
    M1=epsilon Σ_(j=0)^L(c_j+c_(j−1))(L)_j,

    E0=N!B0=Σ_(j=0)^N d_j(N)_j,
    E1=N!B1=Σ_(j=1)^N d_(j−1)(N)_j,
    E=m1E0−m0E1.                                      (4)

Every falling factorial with j>=5 is0 modulo5. Since h>=6,5 divides L!, so mi=Mi mod5. Consequently(4) is determined entirely by the FIRST FIVE ordinary coefficients at the two poles, with the pole-one sign retained.

For ordinary coefficients of degree<5, Frobenius shows that the exponents in these two rational regular factors can be reduced modulo5: every fifth power has no nonconstant coefficient of degree<5. The finite falling factorials also depend only on their upper argument modulo5. Since n=0 mod5, h=N mod5 and L=N−1 mod5. Thus exactly FIVE possible cases remain, R=N mod5, not infinitely many numerical samples.

The complete finite determinant in(4), divided by its sign epsilon, is:

|R|L mod5|M0/epsilon mod5|M1/epsilon mod5|E0 mod5|E1 mod5|E/epsilon mod5|
|---:|---:|---:|---:|---:|---:|---:|
|0|4|4|1|1|0|1|
|1|0|1|1|0|1|4|
|2|1|2|3|3|3|3|
|3|2|3|4|4|1|3|
|4|3|2|0|1|3|4|

Each entry is an exact operation in F5 on coefficients of degree<=4; the certificate retains those coefficients as well as the displayed response values. The last column is1−2R² in every case. Squares in F5 are0,1,4, so1−2R² is never0. This proves(1) for ALL stated parameters. The finite proof is valid because the prior Frobenius/falling-factorial reduction exhausts every possible input residue; it is not an extrapolation from bounded n,h.

For example, at R0 the low regular factors are d=1 and c=(1+u)^−1 mod u5, and E0=1,E1=0,M1/epsilon=1. At R1, L=0,M0/epsilon=M1/epsilon=1,E0=0,E1=1. The remaining rows follow from the same two degree4 polynomial products. No primality distribution or all-prime seed claim is involved.

## 3. Retain the complete primitive and the final gcd

Every partial-fraction and polynomial coefficient of F is integral, by the selector's exact interface. At a=(1+i)/2, both a^−1=1−i and(a−1)^−1=−1−i are Gaussian integers. At5, a itself is also an algebraic unit: its norm is1/2. Hence every endpoint power used in the primitive is5-integral.

The only possible5 denominators in Pi come from division by the primitive exponent. Pole0 contributes exponents1,...,N; pole1 contributes1,...,h−1; and the polynomial part contributes1,...,n+1, since F has degree at infinity at most n. All are at most N. Therefore

    v5(Pi)>=−floor(log5N).                              (5)

This bound retains BOTH principal-part endpoints and the polynomial primitive. It does not discard the pole-one output or claim that Pi is integral at5.

For N>=10,

    v5(N!)>=floor(N/5)>floor(log5N).

Our stated parameters have N>=26. Equation(1) makes v5(E/N!)=−v5(N!), strictly below the bound in(5). The nonarchimedean valuation of the COMPLETE sum is therefore exactly−v5(N!), proving the third identity in(2). Since U is a nonzero integer, division by U gives

    v5(c)=−v5(N!)−v5(U)<0.

The ACTUAL reduced denominator of c has valuation−v5(c), proving the final identity in(2). Equivalently, with O_N=odd(lcm(1,...,N)), the exact pair

    denominator=N! O_N U,
    numerator=O_N E+N! O_N Pi

has precisely the same surviving5 valuation AFTER their gcd. The primitive bound and unit numerator are what make this final statement valid; N! alone would not suffice.

## 4. Power-of-two nodes price the selector's norm5 correction

Now additionally take N=2^s,n a positive20-multiple,N>n,h=N−n>=6. Then n,h are divisible by4, and the selector's binary eligibility holds because h−1<N and binom(N+h−1,N) is odd. Its exact dyadic theorem gives

    v2(U)=1,
    tau=v2(q)=v2(N!)+1=N.                              (6)

The old reduced q can therefore be written2^N B with B odd, and(2),(3) give

    b5=v5(B)=v5(N!)+v5(U)>=N/4−floor(log5N)−1.          (7)

This answers the selector's surviving norm5 arithmetic condition. Its complete-denominator threshold is

    b5>(1/2−log2/log5)tau,

and the coefficient on the right is approximately0.0693234419, strictly below1/4. Thus(7) exceeds that threshold eventually on these nodes, without assuming anything about v5(U).

For orientation, if the selector takes an admissible odd correction order r=N/2+O(1),d=r+1, its exact shared-prime formula bounds the new/old denominator ratio by

    q_new/q_old<=5^max(d−b5,0)/2^N
                 =exp[−(log2−log5/4)N+O(logN)].          (8)

The positive exponent is log2−log5/4≈0.2907877025. Equation(8) is an attributed consequence of the selector's full correction/content formula, not a new proof of its norm/error estimates here. Its equal-depth tie requires the selector's retained tie calculation or a neighboring admissible order. Other odd factors of B and the total growth of q still matter; an exponential denominator reduction does not prove a shrinking primitive form.

## 5. Compatibility with the COMPLETE analytic critical window

The designated analysis agent's authored POWER_TWO_INVERSE_CRITICAL_SUBSEQUENCE.md proves the following inverse critical rounding: for fixed N=2^s choose the large positive real t solving

    Psi(t,N)=t^(3/2)/sqrtN−2sqrtN/sqrtt
                    +log(sqrtN/(4t^(3/2)))=0,

then take n as the nearest20-multiple and h=N−n. Its large solution has t~sqrt(2N); bounded n rounding gives an O(n^−1/2)=O(N^−1/4) complete error, with alpha→e and beta→pi retained. That source is ../agent3_analysis/POWER_TWO_INVERSE_CRITICAL_SUBSEQUENCE.md. This analytic result is attributed to that agent; it is not proven by the arithmetic experiments below. The initially communicated simplified curve also converges, but its rate has an additional logarithm; the sharper Psi curve is the quantitative interface.

Whenever that attributed critical subsequence is used, all arithmetic hypotheses above hold eventually. The actual q5 survival and tau=N are therefore compatible with a convergent full-center sequence. The correction's full error and height remain the selector's separate work. No irrationality criterion is claimed from convergence or from(8).

## 6. Complete exact receipts

reflected_actual_five_denominator.py and REFLECTED_ACTUAL_FIVE_DENOMINATOR_RECEIPT.json preserve the five exhaustive degree4 residue rows and three NEW bounded complete centers. The latter construct E,U,ALL Pi principal/polynomial terms, the rational center and the FINAL cleared gcd independently from the supplied coefficient formulas:

|n|N|h|v5(N!)|v5(U)|v5(Pi)|actual v5(q)|actual v2(q)|
|---:|---:|---:|---:|---:|---:|---:|---:|
|20|64|44|14|0|−1|14|64|
|20|128|108|31|3|−3|34|128|
|40|512|472|126|0|−2|126|512|

The N128 case explicitly shows that U's surviving content ADDS three5 digits after final cancellation; it is not silently canceled. Rational primitive poles remain visible in every row. Array values and hashes are retained without large integer output. These are supporting exact examples, not evidence substituted for the infinite proof or an independent audit of the selector's theorem.

The author theorem(1)–(3), the power-of-two arithmetic interface(6),(7), and the attributed correction opportunity(8) are the outcome. There is still no unconditional conclusion about e+pi.
