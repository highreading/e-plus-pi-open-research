> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exponential companion and coefficient-height tradeoff

Status: new main-agent paper deductions, previously developed in the conversation and now recorded for continuation. Not independently reviewed. No numerical experiment, new HP sample, or completed-check replay is used. The conclusions concern conditioning and selected positive bounds; they do not decide the rationality of e+pi.

## 1. Actual solution and normalization

Consider any relaxed balanced solution with n>=b>=3, degree caps (n,b,n), contact order 2n+b, and B(1)=C(1)=Y!=0. Put X=A(1). Write X/Y=P/Q in lowest terms, with Q possibly signed, and put q=|Q|. Equivalently, clear the triple and divide its endpoint pair by its own endpoint gcd.

Set

    k=n+1, r=n+2-b,
    K=sum_j |B_j/Y|.

Use the established monic reference polynomial p_k, its endpoint A_k=p_k(1)>0, and its rational pi companion

    r_pi,k=L((p_k-A_k)/(t-1))/A_k.

The complete companion decomposition gives

    E=e+P/Q+r_pi,k.

Since b>=3, the first retained high constraint is ell_B(p_k)=0. Therefore

    ell_B(p_k/(1-t))=ell_B(t p_k/(1-t)).

The complete factorial-tail estimate, with the original n in ell_j, yields

    |E| <= e (||p_k||_1/A_k) K/r!
         < 3*4^k K/r!.                                  (1)

Here ||p_k||_1<=2^k and A_k>=2^(-k) are the established coefficient and endpoint bounds. No contact-normality theorem is needed to apply (1) to an existing solution. K is invariant under common scaling of the triple.

## 2. An elementary uniform rational-approximation bound for e

For m>=0 put

    D_m=(2m+1)!/m!,

so D_0=1. For real V>=1 define

    m(V)=min{m>=1 : D_m>=6V}.

For any integers u,v with 1<=v<=V,

    |e-u/v| > 1/[144*2^m(V)*(2m(V)+1)*V^2].              (2)

Proof. First take V=v and m=m(v). Let

    f_m(x)=x^m(1-x)^m/m!,
    I_m=integral_0^1 e^x f_m(x) dx.

The beta integral gives integral_0^1 f_m=1/D_m, hence

    1/D_m < I_m < 3/D_m.

Repeated integration by parts gives I_m=e a_m-b_m, where

    a_m=sum_{j=0}^{2m} (-1)^j f_m^(j)(1),
    b_m=sum_{j=0}^{2m} (-1)^j f_m^(j)(0).

Both numbers are integers: the nonzero endpoint derivatives have orders m+l, 0<=l<=m, and absolute values binom(m,l)(m+l)!/m!. Symmetry f_m(1-x)=f_m(x) gives the same integrality at one. In particular,

    |a_m| <= 2^m (2m)!/m!
           =2^m D_m/(2m+1).

Also a_m!=0. Otherwise I_m=-b_m would be a positive integer, whereas I_m<3/D_m<=1/2.

Minimality and D_m/D_(m-1)=4m+2 give

    D_m < 6v(4m+2)=12v(2m+1).

This also holds for m=1 because D_0=1<6v. Moreover vI_m<1/2. The integer N=a_m u-b_m v satisfies

    vI_m=a_m v(e-u/v)+N.

If N!=0, then

    |e-u/v| > 1/(2v|a_m|)
             >1/(24*2^m*v^2).

If N=0, then

    |e-u/v|=I_m/|a_m|
             >(2m+1)/(2^m D_m^2)
             >1/[144*2^m*(2m+1)*v^2].

The weaker common lower bound proves (2) for V=v. Since m(v)<=m(V) and all denominator factors increase, it proves the stated uniform version.

There is a useful asymptotic qualification. Since

    D_(m-1)=m(m+1)...(2m-1)>=m^m,

minimality implies m(V) log m(V)<log(6V). Consequently

    2^m(V)*(2m(V)+1)=V^o(1)

as V tends to infinity. This conclusion is proved from the displayed finite formulas, not inferred from numerical approximations.

## 3. A conservative denominator bound for the pi reference

Let P_k be the endpoint of the established integral polynomial

    L_k(t)=2^k i^k LegendreP_k(-i(2t-1)).

Its endpoint recurrence is

    (k+1)P_(k+1)=2(2k+1)P_k+4kP_(k-1),
    P_0=1, P_1=2.

All endpoints are positive, and induction gives P_k<=5^k: both recurrence coefficients are below four, and 4*5^k+4*5^(k-1)<5^(k+1).

The integer polynomial (L_k-P_k)/(t-1) has degree k-1. The moment L(t^j) has denominator dividing 2^j(j+1). Thus the rational second-kind value formed from this polynomial has denominator dividing

    2^(k-1) lcm(1,...,k).

Dividing by P_k gives

    den(r_pi,k)<=2^(k-1) lcm(1,...,k) P_k<=160^k.        (3)

For completeness, the coarse lcm estimate used here is lcm(1,...,k)<=16^k. For m>=1, lcm(1,...,2m)/lcm(1,...,m) divides binom(2m,m): every newly occurring prime power in (m,2m] contributes a prime factor to that binomial coefficient. Iterating at powers of two and using binom(2m,m)<=4^m gives lcm(1,...,2^s)<=4^(2^s-1). Taking the least power of two at least k proves the claimed coarse bound; k=1 is immediate.

The denominator in (3) is only an upper bound. It is not identified with the actual reduced denominator of the pi companion.

## 4. Explicit conditioning inequality

The rational number -P/Q-r_pi,k has positive reduced denominator at most

    V=q*160^k.

Apply (2) to E and combine with (1). With m=m(V),

    K > r!/[432*102400^k*q^2*2^m*(2m+1)].             (4)

The constant 102400 is 4*160^2. Formula (4) concerns the actual reduced endpoint denominator q. Substitution of a polynomial clearer, lattice index, or minimal integral lifting multiplier for q is not justified.

This is an arithmetic lower bound on the coefficient-to-endpoint conditioning of every solution in the stated domain. It does not use either the provisional slow-growth normality theorem or its inverse estimates.

## 5. Consequences in slowly growing degree

Suppose b=o(n) along an unbounded sequence of such solutions.

If log q=O(n), then log V=O(n), and the extra factor 2^m(V)(2m(V)+1) has logarithm o(n). Consequently

    log K >= log((n+2-b)!)-O(n).                         (5)

In particular, when b=O((n/log n)^(1/4)),

    log K >= n log n-O(n).

Conversely, if log K=O(n), then

    liminf log q/(n log n)>=1/2.                        (6)

To justify this even when q grows very rapidly, fix any epsilon>0. The extra factor in (4) is at most a constant times V^epsilon. Taking logarithms gives

    (2+epsilon)log q >= log((n+2-b)!)-O_epsilon(n).

Divide by n log n, use b=o(n), and then let epsilon decrease to zero.

## 6. Implication for the current triangle certificate

The positive full-remainder certificate contains the pi contribution q epsilon_k. The accepted reference bound is

    epsilon_k>=2 exp(-s)s^k,
    s=(sqrt(2)-1)^2.

If log K=O(n), equation (6) forces q epsilon_k to diverge. Thus exponential conditioning cannot accompany shrinking of that positive certificate in the regime b=o(n).

Conversely, if that positive certificate tends to zero, then q epsilon_k tends to zero, which forces log q=O(n). Equation (5) then forces factorial-scale K in the slow-growth range currently under study.

This does not prove that the positive certificate is unattainable for all coefficient directions: factorial-scale conditioning may be balanced by factorial decay. It shows that the inverse amplification must be included when assessing each additional subtraction. The estimate also does not exclude a smaller actual full remainder produced by cancellation between the exponential and pi errors.

## 7. Relation to the ongoing research

The direction-sensitive inverse, rational-center arithmetic, and complete cancellation-preserving estimates remain the active requirements. Their norms must be reconciled before this K bound is transferred to a different conditioning quantity. An ordinary unweighted coefficient norm and a factorially weighted Gram norm are not interchangeable without explicit factors.

This note supplies a new explicit constraint on those estimates. It neither establishes shrinking primitive pairs nor settles e+pi. No new audit assignment is created by saving it.
