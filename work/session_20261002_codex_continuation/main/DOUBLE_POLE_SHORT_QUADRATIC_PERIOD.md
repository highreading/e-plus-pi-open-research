> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# M30. A fixed double pole and primitive quadratic e+pi forms

Original Root construction, English author note, 2026-10-02. Fresh archive/primary gate: DOUBLE_POLE_QUADRATIC_PERIOD_GATE.md. Agent3 separately owns complete signed integral and root-scale analysis. This note establishes the exact arithmetic interface; it does not decide e+pi or assert infinite smallness.

## Exact moments and derivative response

Let S=e+pi and let D_n be the derangement integers, D_0=1, D_n=nD_(n-1)+(-1)^n. For r>=0,

    integral_0^1 x^(2r)e^x dx=eD_(2r)-(2r)!,
    8 integral_0^1 x^(2r)/(1+x^2)^2 dx=a_r+nu_r pi,
    nu_r=(-1)^r(1-2r).

Here a_0=2,a_1=-2 and

    a_(r+2)+2a_(r+1)+a_r=8/(2r+1).             (1)

Proof: multiply the integrand by (1+x^2)^2. The two initial integrals follow from the antiderivative x/[2(1+x^2)]+arctan(x)/2. The response recurrence has characteristic (z+1)^2, giving nu_r. Thus the purely EVEN system has no log2 coordinate. Equivalently, on polynomials in y,

    mu(y^r)=D_(2r),
    nu(P)=P(-1)+2P'(-1),
    rho=mu-nu.

The response bilinear form on endpoint value/derivative jets has matrix J=[[1,2],[2,0]], of signature (1,1). Its Hankel rank is two. Its indefiniteness must not be replaced by a positive mass.

## Full matching kernel, with the small-degree exception

For k>=2 set, 0<=i<k,0<=j<2k,

    C_ij=D_(2i+2j)-nu_(i+j),
    R_ij=a_(i+j)-(2i+2j)!,
    V_ij=nu_(i+j).

The physical rectangular moment block for the positive compact weight e^x+8/(1+x^2)^2 is ENTRYWISE

    H=eC+R+S V.                               (2)

C has row rank k for every k>=2. If a nonzero row polynomial p, degp<=k-1, annihilated every column, take q=(y+1)^2p. Its degree is <=k+1<=2k-1, so it is a valid column test. Both the value and first derivative of pq vanish at -1, hence

    rho(pq)=mu((y+1)^2p^2)>0,

a contradiction. Positivity here is the genuine exponential-tail measure representing mu; no positivity of rho is claimed.

At k=1, C=[0,0] because D_0=D_2=nu_0=nu_1=1. Thus the fixed-width stacked determinant vanishes. The two automatically matched right polynomials instead yield (a+b)S+a-4b. Every rational direction is encoded by taking a=4q-p,b=p+q, giving 5(qS-p). This freedom alone supplies no controlled approximation. It is excluded explicitly from the nonzero rank-k stack theorem.

## Basis-independent primitive polynomial

Define the full 2k-square stack

    Delta_k(T)=det[C;R+T V]=beta_0+beta_1 T+beta_2 T^2.       (3)

Its degree is <=2 because V has rank two. For any basis Q of kerC, choose a complementary X with CX invertible. Multiplication by [X,Q] makes the upper-right block zero, giving

    det[(R+T V)Q]=Delta_k(T) det[X,Q]/det(CX).               (4)

Thus changing a rational or integral kernel basis only multiplies ALL polynomial coefficients by one nonzero rational scalar. Clearing denominators and dividing the FULL three-coefficient gcd produces the same primitive integer polynomial up to sign. A smaller kernel basis does not automatically improve it.

Let L=lcm(1,3,...,6k-7). Equation (1) gives denominators of every R entry dividing L. Then I_j=L^k beta_j are integers. Let g=gcd(I_0,I_1,I_2), remove any zero top coefficients, and orient the highest nonzero coefficient positively. The actual primitive polynomial is

    P_k(T)=sum_j (I_j/g)T^j.                              (5)

At the actual S, its full value is ±L^k Delta_k(S)/g. This is a quadratic polynomial value, not a rational-center linear form. If beta_2!=0 with roots c_-,c_+, its exact error identity is

    P_k(S)=(I_2/g)(S-c_-)(S-c_+),                          (6)

up to the stated global orientation. Approximating one root while ignoring the other root or the complete gcd does not establish smallness. If S were rational with denominator v, every nonzero P_k(S) would have absolute value >=v^-2. A rationality contradiction therefore requires genuinely nonzero primitive evaluations tending to zero.

## Forced content retained in all three coefficients

The earlier original Gamma factor proof is credited, not replaced by a larger guessed gcd. Make the unimodular binomial changes from y^i to (y-1)^i in both row blocks and columns. Let

    m_r=mu((y-1)^r)=integral_0^infinity e^-t[t(t-2)]^r dt,
    U_r=m_r/(2^r r!).

The exact integration recurrence gives U_0=1,U_1=0 and U_(r+1)=(2r+1)U_r+U_(r-1) for r>=1. Hence U_r is integer. In this basis the upper Gamma entries are

    2^(i+j)(i+j)! U_(i+j),

and the period entries are 2^(i+j)(1-i-j), still rank two. Every upper k-row minor supplies 2^(sum_i i+sum_selected_j j), hence at least 2^(k(k-1)). After those powers are extracted, an m-row Gamma minor has the factorial divisor F_m^2, F_m=product_(r=0)^(m-1)r!, by factoring i! from each selected row and j! from each selected column.

In the coefficient beta_j, exactly j lower period rows are used. Any term using more than 2-j upper period rows is identically zero: the ENTIRE chosen period row family lies in the same two-dimensional row space. The surviving terms therefore have at least k-2+j upper Gamma rows. Expanding their minors gives the simultaneous, full-coefficient divisibilities

    2^(k(k-1)) F_(k-2+j)^2 divides I_j, j=0,1,2.           (7)

In particular the complete gcd g contains 2^(k(k-1))F_(k-2)^2. These are guaranteed divisors, not exact values of g. Determinant coefficient bounds give log(height(P_k))=O(k^2logk), and (7) removes a substantial forced factorial content, but no sufficient actual primitive-value estimate follows from this upper bound.

## Bounded reproducibility receipt and open step

DOUBLE_POLE_SHORT_STACK_CERTIFICATE.json records seven NEW exact cases k=2,...,8: 24 independent polynomial-division moment checks, full row rank, quadratic coefficient interpolation, matching-kernel polynomial equality, a nonunimodular basis scaling, complete denominator clearing and final gcd. The primitive heights have bits 20,85,178,322,496,707,972. At k=2 the actual polynomial is

    129760 T^2-758873 T-138458.

Finite high-precision diagnostics show one root approaching S rapidly, while log|P_k(S)| is positive and increases through these examples. These diagnostics do not prove an infinite obstruction or main-problem result.

## Completed original analytic continuation

Agent3 has now saved DOUBLE_POLE_SHORT_COMPLETE_QUADRATIC_ERROR.md. For every k>=100, beta has exact degree two, beta(S) has sign (-1)^k, and beta'(S) and beta_2 have sign (-1)^(k+1). The two distinct real roots straddle S. For the ACTUAL compact exterior Christoffel minimum Lambda_k,

    c_+-S is comparable to Lambda_k/k,
    S-c_- is comparable to k Lambda_k,
    |beta(S)/beta_2| is comparable to Lambda_k^2.

The proof keeps both upper derivative-evaluation terms, the full single insertion and the double confluent factor -4. Direct adjacent-Jacobi-weight and interlacing arguments control the inverse two-jet determinant without an assumed indefinite Sobolev positivity theorem. Therefore, with H_k the ACTUAL primitive height in (5),

    log|P_k(S)|=logH_k-8k log(1+sqrt(2))+O(logk),
    H_k/|I_2/g| -> S^2.

This doubles the linear-stack exponential error rate at the polynomial-value level. Actual height control remains the arithmetic issue. Permutationwise sum of moment indices is 3k^2-2k; hence logmax|I_j|<=6k^2logk+O(k^2). The guaranteed F_(k-2)^2 content in (7) improves the ceiling to logH_k<=5k^2logk+O(k^2). This is an upper bound, not a proof that H_k actually grows at that rate, and it does not establish smallness or a no-go theorem for the entire quadratic family.
