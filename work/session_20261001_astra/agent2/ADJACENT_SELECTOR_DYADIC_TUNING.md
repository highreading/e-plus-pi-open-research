> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Adjacent selectors: exact dyadic tuning and its height cost

Status: new author deductions, not independently reviewed. This document preserves PHASE_CROSSING_ARITHMETIC_BYPASS.md and its complete-companion, determinant, and primitive-height formulas. It extends their exceptional dyadic case. No phase-continuation proof, generic cancellation construction, numerical scan, or independent review is repeated.

The conclusions concern the dyadic part of the ACTUAL reduced denominator. They do not give a geometric bound for its odd part, a small complete error, or an irrationality result.

## 1. Preserved exact data

Fix rho>0, let n=2^s tend to infinity, and take m~rho n log n such that m,m+1 are both parity-eligible. Write

    r=n/2, J=n+4m, N=2n+4m,
    t0=N/2-v2(n!)-v2(J!),
    d=v2(J+4)-1>=1, t1=t0-d,
    B=r-t0=3n/2+2m-s2(n)-s2(J).

Here B is the reduced dyadic denominator exponent of selector m. Eligibility and the preserved complete-companion arithmetic give

    U_j=2^r u_j, u_j odd integers,
    X_j=U_j alpha_j, Y_j=U_j beta_j, Z_j=X_j+Y_j,
    v2(X_j)=v2(Z_j)=t_j, v2(Y_j)>=1, j=0,1.

The symbols X and Y retain the complete exponential and logarithmic rational numerators. For clarity their exact definitions are

    B_j(t)=(1-2t+2t^2)^n(1-4t+2t^2)^(2(m+j))
          =sum_l b_(j,l)t^l,
    N_j=2n+4(m+j),
    K_j=t^n B_j^(n)/n!, U_j=K_j(1),
    X_j=sum_(l=n)^N_j binom(l,n)b_(j,l) sum_(h=0)^l 1/h!,
    Y_j=calL((K_j-U_j)/(t-1)),
    calL(f)=integral_-1^1 f((1+iu)/2)du.

Put S=e+pi and R_j=Z_j-S U_j. These are COMPLETE residual numerators.

For coprime integers a,b, let

    U_ab=aU_0+bU_1,
    Z_ab=aZ_0+bZ_1,
    h=max(|a|,|b|).

A rational center is defined only if U_ab!=0. Its two companions and complete center are exactly

    alpha_ab=(aX_0+bX_1)/U_ab,
    beta_ab=(aY_0+bY_1)/U_ab,
    c_ab=Z_ab/U_ab,
    c_ab-S=(aR_0+bR_1)/U_ab.

The selector is L_m(a+b L_1), where L_1=(2t^2-4t+1)^2. Its polynomial content and primitive coefficient height are the preserved formulas

    c_pol=gcd(a+b,4),
    exp(-4)7^(2m)h/[3c_pol(m+1)] <= H_sel
                                    <=50 7^(2m)h/c_pol,
    log H_sel=2m log 7+log h-log c_pol+O(log(m+1)).

The primitive selector forcing is U_ab/c_pol; the common factor cancels from both rational companions and the center.

For final reduction retain

    O=O_(N+4)=lcm{odd positive integers <=N+4},
    D=n!(J+4)! O,
    A_j=D Z_j in Z,
    g=gcd(aA_0+bA_1,D U_ab)>0.

Then

    q=D|U_ab|/g,
    q|c_ab-S|=D|aR_0+bR_1|/g,                    (1.1)
    H_end=max(|aA_0+bA_1|,D|U_ab|)/g.

Here q is the actual positive reduced denominator, including the convention q=1 for center zero. The preserved determinant is

    Delta=U_0 Z_1-U_1 Z_0 !=0,
    v2(Delta)=r+t1,
    g divides |D^2 Delta|.                          (1.2)

No denominator clearer is substituted for q.

## 2. Integral dyadic coordinates and the complete valuation formula

The rational numbers 2^(-t0)Z_0 and 2^(-t1)Z_1 are dyadic units. Clearing their odd denominators and dividing their integer gcd gives coprime odd integers v0,v1 and a rational dyadic unit gamma such that

    Z_0=2^t0 gamma v0,
    Z_1=2^t1 gamma v1.                              (2.1)

Signs of v0,v1 are allowed. The common scaling gamma has valuation zero, so it does not affect any congruence below. These v_j encode Z=X+Y, not a truncation of either companion.

Define integral linear forms

    L(a,b)=u0 a+u1 b,
    M(a,b)=2^d v0 a+v1 b.

Then U_ab=2^r L and Z_ab=2^t1 gamma M. Thus, for L!=0,

    v2(q)=[B+d+v2(L)-v2(M)]_+,                    (2.2)

where [x]_+=max(x,0), and M=0 is interpreted as v2(q)=0. Formula (2.2) is after complete rational reduction.

In particular, a larger forcing valuation increases the denominator exponent. It does not create denominator savings. For possibly nonprimitive coefficients and 1<=k<=B, the condition v2(q)<=B-k is exactly

    v2(M)>=d+k+v2(L).                               (2.3)

One cannot impose only a fixed numerator congruence while ignoring v2(L), nor multiply a coefficient pair by a power of two to improve its final denominator: both valuations increase equally.

For primitive coefficients, all possibilities simplify as follows, excluding L=0:

* a even, b odd: v2(q)=B+d.
* a,b odd: v2(q)=B+d+v2(L)>B+d.
* a odd, 0<v2(b)<d: v2(q)=B+d-v2(b).
* a odd, v2(b)>d, including b=0: v2(q)=B.
* a odd, b=2^d c with c odd:

      v2(q)=[B-v2(v0 a+v1 c)]_+.                  (2.4)

To prove this table, if b is odd then M is odd. If b is even, primitivity forces a odd and L is odd. Comparing the two terms of M gives its smaller valuation unless v2(b)=d, which is exactly the last case.

All savings occur in this last case. There the actual forcing has valuation r, and c_pol=1 because a+b is odd. Neither increased forcing valuation nor removal of polynomial content explains the saving.

## 3. Exact saving lattice and its index

For 1<=k<=B define

    Lambda_k={(a,b) in Z^2:
               2^d v0 a+v1 b=0 mod 2^(d+k)}.       (3.1)

THEOREM 1. Among primitive integer pairs with nonzero forcing, v2(q)<=B-k holds if and only if (a,b) belongs to Lambda_k. Every primitive member of Lambda_k automatically has nonzero forcing.

Proof. By the table, saving forces a odd and b=2^d c with c odd; equation (2.4) then gives precisely (3.1). Conversely, reducing (3.1) modulo 2^d shows 2^d divides b. Primitivity makes a odd. After division by 2^d, reduction modulo two makes c=b/2^d odd. Therefore L is odd, and (2.4) proves the assertion. This also proves forcing nonvanishing.

Since v1 is odd, the homomorphism M modulo 2^(d+k) is onto. Consequently

    [Z^2:Lambda_k]=2^(d+k).                         (3.2)

In coordinates (a,c), b=2^d c, the lattice is

    v0 a+v1 c=0 mod 2^k,

with index 2^k in Z^2. The extra factor 2^d in (3.2) comes from the coordinate change and must be retained for the original coefficient height.

Put K=2^k and choose an integer representative

    r_k=-v0 v1^(-1) mod K.

It is odd. An explicit basis of Lambda_k in the original coordinates is

    (1,2^d r_k), (0,2^(d+k)).                       (3.3)

A vector has the unique parametrization

    b=2^d c, c=r_k a+K l.

It is primitive if and only if

    a is odd and gcd(a,l)=1.                        (3.4)

Indeed gcd(a,b)=gcd(a,c)=gcd(a,K l)=gcd(a,l) when a is odd.

For a primitive saving vector, write ell=v2(v0 a+v1 c). For ell<B its exact denominator exponent is B-ell, and exact depth ell means membership in Lambda_ell but not Lambda_(ell+1). Membership in Lambda_B makes q odd. The lattices Lambda_k can still be defined for k>B, but those stricter numerator conditions yield no additional dyadic denominator reduction.

The determinant in these coordinates is

    u0 v1-2^d u1 v0,

which is odd and therefore nonzero. This is consistent with, and gives a direct coordinate explanation of, the preserved complete determinant (1.2).

## 4. Exact-annihilator directions

There are distinct exceptional directions, whose roles must not be conflated.

FORCING. Let g_u=gcd(u0,u1)>0. The only primitive forcing-annihilator directions are

    +/- (u1/g_u,-u0/g_u).                            (4.1)

Both entries are odd. They belong to none of the saving lattices and do not define a rational center.

COMPLETE RATIONAL NUMERATOR. Since v0,v1 are coprime and odd, the only primitive directions with Z_ab=0 are

    +/- (v1,-2^d v0).                               (4.2)

They belong to every Lambda_k. Their forcing is nonzero because u0 v1-2^d u1 v0 is odd. They give c_ab=0, q=1, and primitive error |S|. Their height is

    h_ann=max(|v1|,2^d|v0|).                        (4.3)

Thus the exact rational-numerator annihilator is an exception to any assertion that arbitrarily deep numerator cancellation must force the shortest coefficient height to grow without bound.

SEPARATE COMPANIONS. For either rational row (X_0,X_1) or (Y_0,Y_1), clear denominators and divide the integer row gcd to obtain a primitive row (p0,p1), whenever the row is not identically zero. Its primitive annihilator directions are +/- (p1,-p0). If a row is identically zero every vector annihilates it. These separate annihilators need not annihilate Z. In particular, cancellation of X alone is insufficient for the complete saving condition.

FULL ERROR. If S=P/Q is rational in lowest terms, define

    a0=Q A_1-P D U_1,
    b0=P D U_0-Q A_0.                               (4.4)

This is a nonzero vector by (1.2); divide by gcd(a0,b0) to obtain its primitive direction. It is exactly the full-error annihilator direction, has nonzero forcing, and gives center P/Q. By Theorem 1 it belongs to Lambda_k exactly when v2(Q)<=B-k. If S is irrational, there is no nonzero integer full-error annihilator. This is a conditional classification, not an assertion that S is rational or irrational.

## 5. When the logarithmic rational numerator affects the congruence

In saving coordinates the exact numerator is

    2^(-t0) Z_ab
       =a 2^(-t0)Z_0+c 2^(-t1)Z_1.

The corresponding contribution from Y has valuation at least

    1-t0,

because a,c are odd, v2(Y_0)>=1, and the second contribution has valuation at least 1-t1>=1-t0.

Therefore replacing Z by X in a divisibility test through modulus 2^k is automatically justified for

    k<=1-t0.                                       (5.1)

For larger k the actual Y contribution must be retained unless an additional divisibility statement is proved. Condition (5.1) is a guaranteed range, not a claim that the first omitted term has exactly that valuation.

Since B=r-t0, tuning to a remaining exponent E=B-k enters the range potentially sensitive to Y when E<r-1. Thus very deep tuning, in particular all the way to an odd reduced denominator, cannot generally use the exponential numerator alone.

## 6. Exact finite height criterion and bounds

The saving question is a weighted primitive-vector problem. It is not determined by the index.

THEOREM 2. For H>=1 and k>=1, a primitive vector of Lambda_k with h<=H exists if and only if there are integers a,c satisfying

    1<=a<=H, a odd,
    |c|<=H/2^d,
    c=r_k a mod 2^k,
    gcd(a,c)=1.                                    (6.1)

A nonannihilating vector additionally requires v0 a+v1 c!=0. This is an exact finite criterion. It does not prescribe or perform a numerical scan.

Proof. A primitive lattice vector has a odd and nonzero, so multiplying by -1 makes a positive. Equation (6.1) is precisely its congruence, height, and primitivity in the coordinates b=2^d c. Conversely these conditions reconstruct such a vector.

There are elementary uniform sufficient bounds. Choose a=1 and a balanced representative c of r_k modulo K=2^k, so |c|<=K/2. This gives

    h<=2^(d+k-1).                                  (6.2)

If it happens to annihilate Z, replace c by c-sign(c)K. Then |c|<=K, the vector stays primitive and in the same lattice, and the numerator is no longer zero. Consequently a nonannihilating saving vector always exists with

    h<=2^(d+k).                                    (6.3)

For lower bounds set

    C_v=2^d|v0|+|v1|.

If M is nonzero and divisible by 2^(d+k), then

    2^(d+k)<=|M|<=C_v h.

Every primitive saving vector also has |b|>=2^d. Thus every nonannihilating saving vector satisfies

    h>=max(2^d,2^(d+k)/C_v).                        (6.4)

Equivalently, at height H its cancellation depth cannot exceed

    log2(C_v H)-d.                                 (6.5)

The actual coefficients v0,v1 matter in this bound. Present estimates do not convert (6.4) into a matching asymptotic lower height for this selector family.

Let lambda_prim(k) denote the shortest primitive height in Lambda_k, allowing Z annihilation. Equations (4.3) and (6.2) imply

    lambda_prim(k)<=min(h_ann,2^(d+k-1)).

Moreover,

    2^(d+k)>C_v h_ann
       implies lambda_prim(k)=h_ann,                (6.6)

and the only primitive shortest directions are (4.2). Indeed every nonannihilating vector then has height strictly greater than h_ann. This proves eventual saturation of the primitive shortest height for the nested congruence lattices. It can occur beyond B, where further depth has no denominator benefit.

### Why index and ordinary short vectors are insufficient

For a general congruence lattice take K=2^k with k>=2 and residue r_k=K/2+1. For odd a,c satisfying c=r_k a mod K,

    c-a=K/2 mod K,
    |c-a|>=K/2.

Hence

    h=max(|a|,2^d|c|)>=K/[2(1+2^(-d))].             (6.7)

But the same lattice contains (a,c)=(2,2), hence the short original-coordinate vector (2,2^(d+1)). It is nonprimitive, and dividing by two destroys the depth condition. Such a residue can be encoded by coprime odd v0,v1, for example v1=1 and v0=-(K/2+1).

This example concerns the general congruence problem. It does not assert that these residues occur for the adjacent selectors. It explains why a geometry-of-numbers bound for an unrestricted shortest vector cannot simply be divided to give a primitive solution at unchanged depth. Likewise, residue-class counts furnish no lower bound for a shortest vector.

## 7. Geometric dyadic denominator: sufficient and necessary height statements

A geometric dyadic denominator means

    q_2=2^v2(q)<=exp(C n)

for some fixed C. Prescribe an integer target exponent 0<=E_n=O(n). Eventually E_n<B; set

    k=B-E_n.

By (6.3), there is a primitive, nonzero-center vector attaining v2(q)<=E_n with

    log h<=(d+B-E_n)log 2
          =2m log 2+O(n).                          (7.1)

Here d=O(log n) because J~4rho n log n. In the saving case c_pol=1, so the preserved primitive polynomial-height formula gives

    log H_sel<=2m log 14+O(n).                      (7.2)

Thus the coefficient cost for dyadic tuning alone is bounded on the n log n scale, far below the n(log n)^2 scale of the preceding generic full-error construction. Neither estimate supplies an approximation to S. Even the exact center-zero vector has q_2=1 and no small primitive error.

For a nonzero-center candidate a necessary bound is exactly

    h>=max(2^d,2^(d+B-E_n)/C_v),                    (7.3)

together with the finite primitive criterion (6.1). Without actual control of v0,v1 or the residues r_k, a universal matching asymptotic necessity does not follow. The exact-numerator-annihilator alternative must be included if center zero is allowed.

No claim that q itself is geometric is made: its odd reduced denominator has not been bounded here.

## 8. Exact dyadic content of the final endpoint gcd

Let F=v2(D). Directly from the four factorial factors,

    F+t0=N/2+d+2.                                  (8.1)

For a primitive saving vector with finite depth ell=v2(v0 a+v1 c), the two integer endpoint valuations in (1.1) are

    v2(aA_0+bA_1)=F+t0+ell,
    v2(D U_ab)=F+r.

Consequently

    v2(g)=F+t0+min(ell,B).                          (8.2)

This also holds for the numerator annihilator with min(infinity,B)=B.

For 1<=k<=B, every primitive vector in Lambda_k therefore has the genuine endpoint-gcd divisor

    g_k=2^(F+t0+k)=2^(N/2+d+2+k).                  (8.3)

In particular,

    q|c_ab-S|<= (D/g_k)|aR_0+bR_1|.                (8.4)

This is a valid bound for the COMPLETE primitive error using the known dyadic part of its actual gcd. Its use does not bound the odd part of q, and it does not omit either residual component. Any further cancellation at odd primes remains encoded in the actual g of (1.1).

## 9. Exact simultaneous congruence and full-error approximation problem

Retain the original selector ordering used for t0,t1. Suppose first that R_1!=0. Define

    x=-R_0/(2^d R_1),
    y=(x-r_k)/K, K=2^k.

For c=r_k a+K l, the complete residual is exactly

    aR_0+2^d cR_1=2^(d+k)R_1(l-a y).               (9.1)

Thus, at a coefficient-height budget H and desired primitive error epsilon, the exact remaining problem is to find integers a,l satisfying

    a>0 odd, gcd(a,l)=1,
    max(a,2^d|r_k a+K l|)<=H,                       (9.2)
    0< D 2^(d+k)|R_1| |l-a y|/g <epsilon.          (9.3)

Here g is evaluated on a,b=2^d(r_k a+K l). Membership in Lambda_k and nonzero forcing then follow automatically. The strict positivity in (9.3) is the separate nonvanishing obligation. If it is omitted, an exact full-error annihilator is permitted.

A sufficient version that uses only the established dyadic gcd is

    0<|l-a y|<epsilon/(C_2|R_1|),
    C_2=D/2^(N/2+2).                               (9.4)

Indeed (8.1)-(8.3) give the useful exact cancellation

    (D/g_k)2^(d+k)=C_2.                            (9.5)

The depth modulus cancels in this error multiplier because the same modulus guarantees endpoint gcd. It remains present in the weighted height constraint. This is a sharper accounting than charging the modulus without the genuine dyadic gcd saving.

If R_1=0, the complete determinant implies R_0!=0. Every primitive saving vector has |a|>=1 and residual aR_0. The exact criterion is then 0<D|aR_0|/g<epsilon with the lattice and height conditions unchanged. Division by R_1 is unavailable. No satisfactory error estimate is asserted for this special case.

## 10. Conditional restricted approximation and the preceding height budget

Let

    C_R=max(1,|R_0/R_1|), M_k=2^(d+k).

Suppose l/a is a continued-fraction convergent to y, in lowest terms, with a odd and

    |l-a y|<1/a.

Then (9.1) and the exact identity

    2^d c=-(R_0/R_1)a+M_k(l-a y)

give

    h<=C_R a+M_k/a,
    q|c_ab-S|<C_2|R_1|/a.                          (10.1)

Consequently an odd-denominator convergent with nonzero error and

    a>C_2|R_1|/epsilon,
    a<=H/(2C_R),
    a>=2M_k/H                                      (10.2)

is sufficient for the same coefficient-height and complete-error budgets.

This is a conditional certificate, not an assertion that such a convergent occurs in the interval. It uses the entire R_j, with no saddle truncation or neglect of the exponential residual.

The preceding paper supplied an unrestricted full-error height budget of order

    H_0=D W/epsilon,
    W>=max(|R_0|,|R_1|),
    log W=rho log 2 n log n+o(n log n),
    log D=4rho n(log n)^2(1+o(1)).                  (10.3)

Its generic construction is not repeated. At this budget, the first and second bounds in (10.2) have ample room algebraically: since C_R|R_1|<=W,

    [H_0/(2C_R)]/[C_2|R_1|/epsilon]
       >=2^(N/2+1).                                (10.4)

For geometric dyadic tuning log M_k=O(n log n), whereas log H_0 has the larger n(log n)^2 scale. Thus coefficient room for the congruence modulus is not itself the obstacle. The unknown is whether an appropriate reduced fraction with ODD denominator occurs in the required interval with the required error. The earlier unrestricted construction does not establish it.

Multiplying unrestricted coefficients into a lattice cannot repair the omission: reducing them back to primitive coefficients restores their original rational center and denominator. Applying homogeneous lattice approximation can similarly yield an even vector; primitive division can destroy the prescribed depth. Section 6 supplies an explicit illustration of that failure.

### Why no unconditional restricted guarantee has been obtained

If y=P/Q is rational in lowest terms with Q even, then for every odd a and every integer l,

    |l-a y|=|Q l-aP|/Q>=1/Q.                       (10.5)

For a prescribed finite height H, irrational numbers sufficiently close to this rational retain a corresponding positive gap for all odd a<=H. For example, if |y-P/Q|<1/(2QH), then |l-a y|>=1/(2Q) throughout that range. Therefore there is no uniform unrestricted-style assertion that arbitrarily accurate approximation with odd a is available within every preassigned finite budget.

If y is irrational, infinitely many convergents have odd denominators: consecutive convergent denominators are coprime and cannot both be even. This yields no bound on the first such denominator satisfying all of (10.2); partial quotients can create arbitrarily large gaps. If y is rational with odd denominator, its reduced exact fraction satisfies (3.4), but can produce a zero complete form rather than a nonzero approximation.

Because Delta!=0, x and y are nonconstant rational fractional-linear transforms of S wherever R_1!=0. Thus

    y rational if and only if S rational.           (10.6)

No arithmetic estimate specific to this y, sufficient for (9.2)-(9.3) or (10.2), has been proved here. Equations (10.5)-(10.6) are explanations of the missing input, not claims that the adverse cases occur for S.

For completeness, in the rational case the exact full-error vector belongs to the saving lattice precisely under the denominator condition stated after (4.4). Thus the classification is also compatible with a rational S whose exact direction is excluded by the chosen dyadic target.

If an approximate value y_hat is used, its certified error delta_y adds at most C_2|R_1|a delta_y to the sufficient primitive-error bound (9.4). For example allocating half the error tolerance requires

    delta_y<=epsilon/(2C_2|R_1|a).

An uncontrolled leading saddle phase cannot replace this full-error precision requirement.

## 11. Scope and stopping result

The exact depth theorem is proved in Sections 2-3. Saving k<=B powers relative to the single-selector exponent B is exactly primitive membership in an explicitly based lattice of index 2^(d+k); forcing valuation stays r throughout that locus. The complete numerator is essential at deep precision.

The exact finite primitive-height criterion, constructive upper bounds, actual-row lower bounds, and exact-annihilator saturation are proved in Section 6. A nonzero-center geometric DYADIC denominator is attainable with log h<=2m log 2+O(n), and primitive polynomial height log H_sel<=2m log 14+O(n). These are sufficient tuning costs, not approximation results or necessary asymptotic heights.

Compatibility with the preceding full-error budget reduces to the explicit simultaneous conditions (9.2)-(9.3), with the useful sufficient odd-convergent criterion (10.2). The dyadic gcd has been counted exactly and offsets the error-side modulus. The existing unrestricted approximation argument does not produce the required odd-denominator solution within its claimed finite height budget. Additional restricted approximation arithmetic, or a sharper argument using the actual odd gcd, is still needed.

Finally, arbitrarily small bounds that allow a zero primitive form do not prove irrationality. If S=P/Q were rational, every nonzero primitive form |p-qS| would be at least 1/Q. Neither dyadic tuning nor the conditional certificate establishes nonvanishing independently of S.

All results above are author deductions. The preserved predecessor and its formulas remain unchanged. No numerical evidence is asserted. Actual saving and read-back receipts are recorded separately by the application.
