> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete common-root and evaluation-cost interface for the linear metric

Agent 3, 2026-10-02. Original author deductions on the new metric of RECIPROCAL_COORDINATE_METRIC_LINEAR_CENTER.md. No selected root supply, favorable asymptotic gcd, or irrationality conclusion is asserted.

## 1. New target checks

Archive searches covered common roots, fixed divisors, integer-valued polynomials, negative evaluations and polynomial resultants in the October 1 and current sessions. They located the exact saturated-basis algebra in agent4/RATIONAL_CENTER_ARITHMETIC.md, the generic weight-polynomial resultant observation there, and root's different canonical binary Gram resultant reduction. Those facts are reused within their scopes. The present target is the ACTUAL reciprocal-coordinate linear metric, with negative evaluation costs and its separate column/fixed-divisor/root contents retained.

Primary queries included `site:arxiv.org integer polynomial fixed divisor factorial falling factorial basis`, `site:arxiv.org Hermite Pade denominators factorial reduction common roots polynomials`, `fixed divisor polynomial factorial arxiv`, and `fixed divisors primitive polynomial n! paper`. Opened the full Peruginelli paper https://arxiv.org/pdf/1304.7450, especially Lemma 1.1 (finite determination of a fixed divisor) and its prime-power viewpoint; the full Prasad--Rajkumar--Reddy paper https://arxiv.org/pdf/1803.05780; and the Hermite--Pade primary paper https://arxiv.org/html/1502.06695. The elementary finite-difference and Hensel inputs are established mathematics, not claimed new. No searched source provides favorable content for this actual mixed companion.

## 2. An exact all-parameter height formula

Write d=b-1, sigma=sqrt2. In the proved proportional range the uniform complete coordinate theorem gives

    |u_j|=C_n B_j theta_(j,n),
    log C_n=log n!+O(n),
    0<c1<=theta_(j,n)<=c2<infinity

uniformly over every coordinate. These constants are independent of a subsequent negative evaluation parameter. The reference coefficients B_j have alternating reconstructed signs. Evaluation of their full gamma polynomial gives the EXACT identity

    sum_(j=0)^b B_j t^j
      =(1+t)sigma^(-d) E_(X~Gamma(n,1))(X+t)^d, t>=0.     (1)

There is no highest-coefficient truncation in (1). Jensen's inequality and the rising-factorial expansion imply

    (n+t)^d <= E(X+t)^d <= (n+d+t)^d
                             <=(1+d/n)^d(n+t)^d.        (2)

Thus uniformly for ALL t>=0, including rapidly varying t,

    log|U(-t)|=log d_B+log n!+d log(n+t)
                            +log(1+t)-d log sigma+O(n). (3)

The two bounded theta factors affect this only by O(1); the remaining O(n) is the actual inverse/saddle factor in C_n. The uniform coordinate equivalence and signs ensure that no evaluation cancellation occurs.

For a positive reduced rational t=a/h, use the degree-b homogeneous INTEGER evaluation

    U^h(a,h)=sum_j U_j(-a)^j h^(b-j),
    V^h(a,h)=sum_j V_j(-a)^j h^(b-j).

Equation (3) becomes

    log|U^h(a,h)|=log d_B+log n!+d log(nh+a)
                                +log(h+a)-d log sigma+O(n). (4)

This accounts for the entire h^b evaluation clearer. No gain is credited before reducing the pair. Its exact denominator is |U^h|/gcd(U^h,V^h), and its complete error still has the signed rate tau_c for arbitrary positive a,h.

In particular EVERY integer 1<=a<=K n, with fixed K, has

    log|U(-a)|=log d_B+(n+b-1)log n+O_K(n).              (5)

The useful integer search interval therefore extends to order n without a new factorial height penalty. A large CRT modulus itself does not prove that it has a root representative inside this interval. If h grows, its d log h cost in (4) must be retained; if a>>nh, its d log a cost must be retained. Replacing these costs with zero would invalidate the primitive denominator budget.

## 3. Separate column contents and the actual lattice factor

Let

    alpha=cont(U), beta=cont(V), X=U/alpha, Y=V/beta.

Both X,Y are primitive integer columns, gcd(alpha,beta)=1, and

    chi0=gcd_(i<j)|X_i Y_j-X_j Y_i|>0.                 (6)

Choose an INTEGER row r with r X=1 and put t0=r Y. Define

    Z=(Y-t0 X)/chi0.

This is an integer polynomial column: each coordinate of its numerator is a sum of the two-row minors against r. In an integer unimodular basis extending X, the remaining coordinate gcd is exactly chi0, which proves the normalization. This is the standard saturated-basis construction already used in the archive, now applied to the two linear evaluation polynomials rather than a quadratic Gram contraction. In polynomial notation

    U=alpha X,
    V=beta(t0 X+chi0 Z).                               (7)

Endpoint sums are X(1)=0 and beta chi0 Z(1)=d_B. Hence

    beta chi0 | d_B.                                   (8)

This proves an intrinsic upper divisor relation; equality is not assumed.

For an INTEGER negative argument -a, put A=X(-a), B=Z(-a). With

    s=gcd(|A|,beta chi0), A0=A/s,
    v0=gcd(|A0|,|B|), r0=s v0,
    C0=beta(t0 A+chi0 B)/r0,

the quotient has the EXACT reduction

    q*=alpha |A0|/[v0 gcd(alpha,|C0|)].                  (9)

Indeed gcd(A,beta(t0 A+chi0 B))=gcd(A,beta chi0 B)=r0, and the remaining pair A/r0,C0 is coprime. Formula (9) retains the factorial column content alpha, the response-lattice divisor s, the residual evaluation gcd v0, and the final overlap with alpha. In particular

    gcd(|U(-a)|,|V(-a)|)>=gcd(|X(-a)|,beta chi0).        (10)

Common roots of X modulo the LARGE intrinsic divisor beta chi0 therefore force actual companion cancellation through (7). This is a concrete response-lattice supply, stronger than studying an arbitrary pure logarithmic row. It still requires roots at affordable arguments and does not establish their existence.

The same construction applies to homogeneous evaluations, where the full (a,h) costs in (4) remain. Divisibility by h or a shared artificial homogeneous scale is removed before using (9).

## 4. Automatic content and selected lifting are distinct

Let g_fix be the gcd of U(k),V(k) over ALL integers k. The degree-b Newton expansion determines it from k=0,...,b. Multiplying each expansion coefficient by b! expresses b! times every ordinary coefficient as an integer linear combination of these values. Since the total coefficient gcd of U,V is one,

    g_fix | b!.

Evaluation at k=1 also gives g_fix|d_B, so

    g_fix | gcd(d_B,b!).                               (11)

The same result holds if the common fixed divisor is taken over all NEGATIVE integers: b+1 consecutive negative values determine the Newton coefficients. This universal content has at most c n log n+O(n) logarithmic scale. It cannot alone meet the required log d_B+(n+b-1)log n cancellation, and is not multiplied into a selected gcd a second time.

For a prime p with p|alpha, total coefficient primitivity implies that V has at least one p-unit coefficient. A simple ACTUAL companion root V(zeta)=0 modulo p, with V'(zeta) a p-unit, has a unique Hensel lift modulo p^k for all k. Choosing -a equal to that lift modulo p^A, A=v_p(alpha), forces p^A into gcd(U(-a),V(-a)). For primes dividing beta the roles reverse. At primes dividing neither column content, simultaneous U,V roots must be lifted together; a root of either polynomial alone is insufficient.

Alternatively, the response-lattice factor (10) gives a route through roots of X modulo beta chi0. Hensel lifting of a simple X root supplies the stated forced factor in (10) at every lifted depth, with the actual Z polynomial still retained in (9). A CRT product of such divisors gives a prescribed residue class, but obtaining a small positive integer or rational representative requires a separate argument. The trivial representative a<=M of a modulus M may cost d log M in (3), so it is not automatically favorable.

## 5. Bounded original reconnaissance and next proof need

negative_evaluation_content_probe.py and its JSON reconstruct three complete rational lifts at (n,b)=(12,4),(20,5),(30,7), from exact T, both forcing columns, the finite reconstruction and the endpoint constant. These cases are explicitly OUTSIDE the proved c<1/1000 proportional range. They are new algebraic mechanism probes, not asymptotic evidence or a replay of old normality checks.

All three have g_fix=1. Their separately primitive minor content chi0 equals d_B and beta=1. This equality is an OBSERVATION on those cases, not a theorem. It motivates a precise arithmetic target: identify which actual primes satisfy v_p(chi0)=v_p(d_B), and control the missing factor through the local response matrix rather than through its arbitrary raw determinant.

Several V roots modulo small p are multiple and fail to lift. For example (30,7),p=7 has v_p(V_j)=1 for 0<=j<7 and V_7 a p-unit. Thus v_7(V(-a))=0 when 7 does not divide a and equals 1 when 7 divides a; that residue-zero root never gives a deeper companion factor. This single-case observation does not exclude an unbounded family or determine S.

The substantive remaining selected-content question is whether roots of X modulo beta chi0, together with the alpha overlap in (9), occur at arguments satisfying (3)-(5) often enough to bring the actual q below exp(tau_c n). No favorable root supply or denominator bound is asserted here.
