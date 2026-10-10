> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Collected logarithmic coefficients: recurrences and residual congruences

Original author research, 2026-10-01. English and offline. The completed cancellation-range paper is retained unchanged, including its proved limitation that missing monomials alone cannot supply a leading saving. This note studies collected coefficients and their actual weights. No prime scan, prime-supply assumption, or independent review is used.

## 1. Domain and notation

Let n=4k, k>=1, m>=0, J=n+4m, and suppose the actual endpoint U is nonzero. Put

    P(x)=1+2x+2x^2, C(x)=1-2x^2,
    F(x)=P(x)^n C(x)^(2m), U=[x^n]F(x).

Retain the logarithmic numerator T and companion Bbeta=den(T/U) from the preceding papers. Let p be an odd prime satisfying

    max(n,sqrt(J))<p<=J.

Write

    2m=Mp+r, 0<=r<p,
    d=floor((n+2r)/p), 0<=d<=2,
    Y(x)=P(x)^n C(x)^r,
    ell_v=[x^(n+vp)]Y(x), 0<=v<=d.

Then floor(J/p)=2M+d<p. In this domain the highest denominator layer is p itself and there are no negative Laurent indices. Their absence follows from p>n; it is not an omission in the general Laurent formula.

With

    a_plus=(-1+i)/2, a_minus=(-1-i)/2,
    tau_j=(2/i)(a_plus^j-a_minus^j),
    chi_p=(-1)^((p-1)/2),

Section 6 of the retained cancellation-range paper gives

    pT=S_p modulo p,
    S_p=chi_p sum_{v=0}^d ell_v Phi_v(M),              (1)

where

    Phi_v(M)=sum_{h=0}^M, v+2h!=0
               binom(M,h)(-2)^h tau_(v+2h)/(v+2h).

Only weights with v<=d are required. Their positive denominator indices are at most 2M+d<p. All reductions below are made from rational identities with p-integral coefficients.

The new results are explicit recurrences for the weights; a deterministic region where S_p is a unit multiple of U; a differential-equation and rational-function reduction of all three collected coefficients; and a two-scalar residual congruence on the first Phi_2-zero strip. No favorable leading cancellation rate is established.

## 2. Closed relations for the three weights

Define the integer sequence

    V_j=((1+i)^j-(1-i)^j)/(2i),
    V_0=0, V_1=1, V_(j+2)=2V_(j+1)-2V_j.

Its four-step values are

    V_(4a)=0,
    V_(4a+1)=(-4)^a,
    V_(4a+2)=2(-4)^a,
    V_(4a+3)=2(-4)^a.

Thus every nonzero V_j is a signed power of two.

The weights have the rational integral representations

    Phi_0(M)=(2/i) integral_(a_minus)^(a_plus)
                         (C(x)^M-1)/x dx,
    Phi_1(M)=(2/i) integral_(a_minus)^(a_plus) C(x)^M dx,
    Phi_2(M)=(2/i) integral_(a_minus)^(a_plus) x C(x)^M dx.

The first integrand is a polynomial because its numerator vanishes at zero. These are polynomial primitives, so no logarithm branch is introduced.

At the endpoints C(a_plus)=1+i and C(a_minus)=1-i. Direct integration gives

    Phi_2(M)=-V_(M+1)/(M+1).                          (2)

Subtracting the first integral at consecutive M gives

    Phi_0(M+1)-Phi_0(M)=-2Phi_2(M),
    Phi_0(0)=0,
    Phi_0(M)=2 sum_{j=1}^M V_j/j.                     (3)

For the remaining weight use

    D_x[x C(x)^(M+1)]
       =(2M+3)C(x)^(M+1)-2(M+1)C(x)^M.

Its endpoint difference, multiplied by 2/i, is -4V_M. Hence

    (2M+3)Phi_1(M+1)
       =2(M+1)Phi_1(M)-4V_M,
    Phi_1(0)=2.                                      (4)

Equations (2)-(4) are usable recurrences without binomial sums. They determine exactly the weights in (1). An additional recurrence, if desired, is

    (M+2)Phi_2(M+1)
       =2(M+1)Phi_2(M)-2M Phi_2(M-1), M>=1.

All modular divisions needed to reach a required Phi_1(M) involve odd integers at most 2M+1. When d>=1 these are strictly below p. If d=0 and 2M+1=p, Phi_1(M) is not required and equation (4) must not be divided by that p. Equations (2)-(3) use denominators at most M+1<p in the present domain.

In particular, whenever Phi_2 is required,

    Phi_2(M)=0 modulo p if and only if 4 divides M+1. (5)

This is stronger than a sufficient rational zero: if 4 does not divide M+1, its numerator is a power-of-two unit and M+1 is a p-unit.

The constants needed below are

    Phi_0(1)=2, Phi_0(2)=4,
    Phi_0(3)=Phi_0(4)=16/3,
    (Phi_0(3),Phi_1(3),Phi_2(3))=(16/3,-32/35,0).     (6)

They follow directly from (2)-(4). No claim is made that Phi_0 or Phi_1 is always a unit at every allowed prime for arbitrary M.

## 3. An explicit region where cancellation requires endpoint divisibility

Fix an integer a in {1,2,3,4}. Consider every prime in the explicit interval

    max(n,sqrt(J),J/(2a+1))<p<=2m/a.                  (7)

The interval can be empty. No prime existence is assumed. Put r=2m-ap. Its bounds imply

    r>=0, n+2r=J-2ap<p.

In particular r<p, so M=a and d=0. Frobenius gives

    F(x)=Y(x)C(x^p)^a modulo p.

Since n<p, its coefficient at n is unchanged:

    ell_0=U modulo p.                                (8)

Combining (1), (6), and (8) proves the deterministic collected identity

    pT=chi_p c_a U modulo p,
    c_1=2, c_2=4, c_3=c_4=16/3.                     (9)

Every c_a is a p-unit: p>n>=4, and in the cases a=3,4 the further inequality 2a<p is already forced by the domain. Therefore

    S_p=0 if and only if p divides U                 (10)

throughout (7).

This is a genuine restriction on collected cancellation, not a support criterion. In particular:

* If p does not divide U, then v_p(T)=-1 and v_p(Bbeta)=1.
* If p divides U, then T is p-integral. This removes the moment pole, but does not decide whether division by U leaves p in Bbeta.

The pole-removing primes in the union of the four intervals must all divide the same nonzero integer U. Hence, at each fixed n,m,

    sum_{p in these intervals, S_p=0} log p<=log|U|.  (11)

For m~rho n log n, the retained forcing-height bound gives log|U|=o(n log n). Thus cancellation in these explicit regions cannot supply leading removable logarithmic mass. This conclusion needs neither a prime count nor an assumption that U is generically a unit.

For the exceptional primes dividing U, equation (9) specifies the first residue of pT. The complete lift of pT, rather than that residue alone, is needed for endpoint cancellation. This is discussed in Section 8.

The same argument works for any fixed M with a separately proved unit Phi_0(M) in the d=0 region. No such general unit assertion is made here beyond the four explicit values used above.

## 4. Differential equation and the obstruction to naive propagation

The ACTUAL low polynomial Y=P^n C^r satisfies

    (1+2x-4x^3-4x^4)Y'
       =[2n+4(n-r)x-(4n+8r)x^2-8(n+r)x^3]Y.         (12)

Let y_j=[x^j]Y, with negative indices zero. Comparing coefficients gives the all-index recurrence

    (j+1)y_(j+1)
       =2(n-j)y_j+4(n-r)y_(j-1)
        +4(j-n-2r-2)y_(j-2)
        +4(j-2n-2r-3)y_(j-3).                       (13)

This is an integer identity before reduction. Modulo p, it can be solved for y_(j+1) only when j+1 is nonzero modulo p. At j=p-1 and j=2p-1 it is a constraint, not a license to divide by p.

This matters for ell_0, ell_1, ell_2, which occur in different p-blocks. A first-order differential equation in characteristic p does not by itself propagate a constant term uniquely across those blocks: multiplication by a rational function of x^p leaves its logarithmic derivative unchanged. The prescribed polynomial degree and its particular factors still matter and can restrict this ambiguity. They cannot be replaced by the characteristic-zero uniqueness argument.

Thus neither the order of (12) nor the vanishing of Phi_2 permits dropping one of the other collected coefficients. The next section resolves the relevant block coefficients through the actual factors of Y.

## 5. Resolving the coefficient blocks by complementary powers

Put

    t=p-r, 1<=t<=p,
    G(x)=P(x)^n/C(x)^t.

Over F_p[[x]], Frobenius gives

    Y(x)=C(x^p)G(x)=(1-2x^(2p))G(x).               (14)

The rational function G satisfies equation (12) with r replaced by -t, congruent to r modulo p. Thus (14) provides the actual factor-dependent solution across the singular positions of recurrence (13).

Let

    a_j=[x^j]P(x)^n, 0<=j<=2n,
    epsilon_p=(2/p), the quadratic character of 2.

Define the following rational quantities depending on n,t:

    A_(n,t)=sum_{u=0}^{n/2}
              a_(n-2u) 2^u binom(t+u-1,u),

    B_(n,t)=sum_{1<=j<=2n-1, j odd}
              a_j 2^((n+1-j)/2)
              binom(t-1+(n-j)/2,t-1),

    D_(n,t)=2(-1)^(t-1) sum_{u=t}^{n/2}
              2^u a_(n-2u) binom(u-1,t-1).           (15)

An empty final sum is zero. Negative powers of 2 in B are legitimate dyadic units. Generalized binomial coefficients in that formula are evaluated over Q before reduction. Their denominators divide powers of 2 times (t-1)!, hence are p-units. In A, the denominator indices u are below p; the displayed A is in fact a positive integer.

The exact collected-coefficient reduction is

    ell_0=A_(n,t),
    ell_1=epsilon_p B_(n,t),
    ell_2=D_(n,t) modulo p,                          (16)

with only indices present in the original d-range needed.

Proof. Write g_l=[x^l]G. Equation (14) gives

    ell_0=g_n,
    ell_1=g_(n+p),
    ell_2=g_(n+2p)-2g_n modulo p.

The first expression is A by expansion of C^(-t). Because p>n, both high indices exceed deg(P^n), so all same-parity coefficients of P^n enter without truncation. At the odd index n+p,

    2^((n+p-j)/2)
      =epsilon_p 2^((n+1-j)/2) modulo p,

and reducing the polynomial binomial coefficient shifts its argument by p/2 without changing its residue. This proves the formula for B.

At the even high index n+2p, reduction gives twice the corresponding sum with exponents (n-j)/2. Subtracting 2g_n leaves only even j>n. Write j=n+2u. The reciprocal identity

    a_(n+2u)=2^(2u)a_(n-2u)

follows from P(x)=2x^2 P(1/(2x)). Finally,

    binom(t-u-1,t-1)=0 for 1<=u<t,
    binom(t-u-1,t-1)=(-1)^(t-1)binom(u-1,t-1)
                                    for u>=t.

This proves the last formula in (16).

The degree ranges take a particularly simple form:

    d=2 if t<=n/2,
    d=1 if n/2<t<=(p+n)/2,
    d=0 if t>(p+n)/2.                               (17)

In particular D_(n,t)=0 identically when d<2, consistent with (16). When d=0 the high odd coefficient also vanishes modulo p, but an absent Phi_1 with a nonunit denominator must not be introduced to express that fact.

Equations (2)-(4), (15)-(17) replace the three long coefficient extractions in (1) by explicit finite quantities. The new sums have indices bounded by n, rather than by p+n or 2p+n. This reduction uses collected coefficients and reciprocal identities; it is not a monomial-support bound.

## 6. The first Phi_2-zero strip leaves two actual quantities

Consider M=3 and t=p-r with

    p prime, p>n, p>=11,
    2<=t<=n/2, t even,
    m=2p-t/2,
    U!=0.                                          (18)

Then 2m=4p-t=3p+(p-t), so the stated M,r are the actual quotient and remainder. Also

    J=n+8p-2t,
    8p<=J<9p<p^2,
    d=2.

Thus (18) is inside the required leading-prime domain. The parity condition on t is exactly what makes m integral. Any desired binary allocation is an additional restriction, not inferred from (18).

Now Phi_2(3)=0, but the other weights in (6) are nonzero. Equations (1) and (16) give the reduced two-scalar congruence

    S_p=(16chi_p/105)
              [35A_(n,t)-6epsilon_p B_(n,t)] modulo p. (19)

The prefactor is a unit because p>=11. Consequently moment cancellation on this strip is equivalent to the explicit additional congruence

    35A_(n,t)=6epsilon_p B_(n,t) modulo p.            (20)

This is a shorter condition than the original three-coefficient test: all Phi weights have been evaluated, the third term has been eliminated for a proved reason, and both remaining scalars are finite n-index sums from (15). It is not valid to conclude S_p=0 solely from M+1 being divisible by four.

A further reduction is available at t=2. Let Pell_n denote the integer sequence

    Pell_0=0, Pell_1=1,
    Pell_(n+2)=2Pell_(n+1)+Pell_n.

Then for every even n,

    B_(n,2)=B_(n,1)=2^(n+1) Pell_n.                 (21)

To prove this, pair j and 2n-j in the odd sum in (15). The reciprocal identity makes their weights equal; their values of (n-j)/2 are opposite. The linear binomial factor for t=2 therefore contributes the same paired sum as the constant factor for t=1. Evaluating the odd part of P(x)^n at x=1/sqrt(2) yields

    B_(n,1)=2^((n-1)/2)
                 [(2+sqrt(2))^n-(2-sqrt(2))^n]
             =2^(n+1) Pell_n.

The last equality uses even n and the usual closed expression for the displayed integer recurrence. It is a rational identity, so the temporary square root creates no modular extension or new denominator.

Thus, on the exact substrip

    t=2, m=2p-1, p>n, p>=11, U!=0,

put

    A_n=[x^n]P(x)^n/(1-2x^2)^2
       =sum_{u=0}^{n/2}(u+1)2^u a_(n-2u).

The shortest congruence obtained here is

    35A_n-6epsilon_p 2^(n+1)Pell_n=0 modulo p.       (22)

Both quantities are independent of p apart from the single sign epsilon_p. A_n is explicitly determined by the displayed finite sum, and Pell_n by a second-order integer recurrence. No residual Phi sum or high-degree coefficient remains.

For nonzero (22), the logarithmic pole survives and

    v_p(T)=-1, v_p(Bbeta)=1+v_p(U).

If (22) vanishes, T is p-integral; the endpoint valuation still controls whether the prime survives in Bbeta.

## 7. Why the proposed automatic cancellation fails

The actual small-n specialization already separates the two residual scalars. The successful new symbolic certificate records

    A_(4,2)=276,
    B_(4,2)=384,
    D_(4,2)=-8.

Accordingly the bracket in (19) is

    9660-2304epsilon_p.                              (23)

Its two possible rational values are 7356 and 11964, both nonzero. Thus the differential equation and Phi_2(3)=0 do not imply a rational identity annihilating the other two terms. In particular every prime p>11964 on the n=4, m=2p-1 line has a surviving moment pole. This last statement is a deterministic implication for such primes, not a computation or a statement about an n-growing asymptotic sequence.

Here U!=0 follows from the retained binary allocation with k=1 and P=2, because m=2p-1 is odd. The observation is an actual-family obstruction to the proposed automatic cancellation, not an abstract choice of independent ell_v.

The n=4 specialization is not claimed to have m~rho n log n with n tending to infinity. The all-n relations (19)-(22) can be applied to growing parameter choices satisfying that asymptotic allocation, whenever their required primes and nonzero endpoints are present. No supply of those primes is asserted.

There are two distinct reasons that a naive argument fails:

1. The differential recurrence has singular steps at multiples of p. Propagating through them by division would impose a false relation between p-blocks.
2. Phi_2=0 removes only the third contraction. The remaining weights are nonzero and the actual factors produce the separate scalars in (20), or (22) on t=2.

The explicit rational reduction resolves the first issue, but it does not make the second congruence automatic. A proof of many zeros of (20) would be genuinely new arithmetic, not a consequence of the already known weight zero.

## 8. Gap one, endpoint content, and higher depth

The gap-one prime p=J-1 has M=0,d=1. The initial weights remain

    Phi_0(0)=0, Phi_1(0)=2.

The retained translated coefficient is

    ell_1=n 2^((2n+4m)/2),

a p-unit, and chi_p=-1. Hence the present formulas retain exactly

    pT=-2n 2^((2n+4m)/2) modulo p !=0.

Neither the d=0 regions nor the M=3 strip can erase this surviving pole. No earlier gap-one calculation is repeated.

Throughout the present leading-prime domain, put u=v_p(U). The complete local normalization is

    R_p=pT in Z_(p),
    v_p(Bbeta)=max(0,1+u-v_p(R_p)).                  (24)

For T=0 the companion denominator is one and the zero-numerator convention applies. If the collected residue vanishes, then R_p is divisible by p and T is p-integral. This is moment cancellation only. Absence of p from Bbeta requires

    R_p=0 modulo p^(1+u).                           (25)

The exact quantity to lift is the retained rational Laurent expression

    R_p=sum_{a=-n, a!=0}^J c_(n+a) p tau_a/a,
    c_h=[x^h]F(x).

Every summand is p-integral because p^2>J and n<p. Terms suppressed in the first residue, including regular Laurent terms with negative indices, must be restored for (25). The highest-layer sum has no negative multiples of p, but the exact lift still contains those negative Laurent terms.

Equation (9) does not identify moment cancellation with cancellation against U. Similarly (20) or (22) with a zero residue settles removal from Bbeta at once only if U is a p-unit. No root-depth estimate follows from the zero alone.

## 9. Aggregate scope and the actual companion threshold

The d=0 intervals (7) give a new proved limitation stronger than a support statement: all their pole-removing primes divide U, so their removable one-factor mass is o(n log n) under the stated large-selector allocation. On the M=3 strip, the third weight vanishes identically but the new explicit residual (20) remains. No aggregate zero bound for that residual is proved.

Consequently this note establishes neither a leading reduction of the actual companion denominator rate nor a new regime below the confirmed strict threshold 5/82. It also does not prove that all possible collected cancellation is subleading. Regions not covered by (7), and the residual congruences in the other regions, remain genuine arithmetic questions.

The preceding support-only limitation is preserved. The current results go beyond it by evaluating the weights, resolving the differential block coefficients, and isolating two concrete residual quantities on a nontrivial parameter strip. No assertion about primes in moving intervals is needed for any theorem above.

## 10. Evidence and deliverable status

The existing new certificate is

    work/session_20261001_astra/agent1/logarithmic_collected_relations_checks.json.

Its controller-confirmed status is PASS_NEW_COLLECTED_RELATION_ALGEBRA. It verifies the expanded differential polynomials, the new small-M constants, and the actual n=4 complementary-exponent coefficients used above. An initial structural-expression comparison failed before a certificate was saved; replacing it by comparison of expanded polynomial differences resolved that issue without changing the mathematical identity. The successful check has not been repeated.

The unrestricted results in this note rest on their written proofs. The certificate is supporting symbolic evidence, not an independent review or a substitute for all-index arguments. Earlier papers and their readbacks are not repeated. The two new documents require controller-confirmed write and read-back before final handoff.
