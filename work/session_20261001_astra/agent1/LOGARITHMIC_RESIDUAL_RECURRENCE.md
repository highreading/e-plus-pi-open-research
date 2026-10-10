> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Logarithmic residual: recurrence, consecutive content, and strip cancellation

Original author research, English and offline, 2026-10-01. The completed LOGARITHMIC_COLLECTED_COEFFICIENT_RELATIONS.md and its successful symbolic checks are preserved. No previous check, support scan, or independent review is repeated. The preceding author note is developed here into proofs; it is not treated as a verification verdict.

## 1. The actual strip and auxiliary sequences

Retain

    P(x)=1+2x+2x^2, C(x)=1-2x^2,
    n=4k, k>=1,
    p prime, p>n, p>=11,
    m=2p-1,
    J=n+4m=n+8p-4,
    F(x)=P(x)^n C(x)^(2m)=sum c_h x^h,
    U=c_n!=0,
    T=calL((K-U)/(t-1)), Bbeta=den(T/U).

These conditions give exactly

    floor(2m/p)=3, r=2m-3p=p-2,
    t=p-r=2,
    floor((n+2r)/p)=2,
    floor(J/p)=8,
    8p<=J<9p<p^2.

Thus the original leading-prime condition p>max(n,sqrt(J)) is satisfied. For an asymptotic allocation m~rho n log n, the prime must additionally satisfy p~(rho/2)n log n. This is a restriction on parameters, not a prime-supply assertion.

For recurrence purposes extend the following auxiliary sequences to every integer n>=0:

    A_n=[x^n]P(x)^n/C(x)^2,
    Pell_0=0, Pell_1=1,
    Pell_(n+2)=2Pell_(n+1)+Pell_n,
    B_n=2^(n+1)Pell_n,
    R_n^(epsilon)=35A_n-6epsilon B_n, epsilon=+1 or -1.

The identification of B_n with the actual collected coefficient is used only on the retained even-index domain, in particular n=4k. Extending these auxiliary sequences to odd indices does not extend the original parameter strip.

Write chi_p=(-1)^((p-1)/2) and epsilon_p=(2/p). The retained collected-coefficient theorem supplies

    pT=(16chi_p/105)R_n^(epsilon_p) modulo p,
    U=A_n modulo p.                                      (1)

The prefactor is a unit throughout the strip. Hence a nonzero residual proves

    v_p(T)=-1,
    v_p(Bbeta)=1+v_p(U).                                 (2)

The present task is to understand the residual in (1), without confusing its integer content with the higher valuation of pT.

## 2. Exact generating functions

Put

    Q(z)=1-4z-4z^2, s(z)=sqrt(Q(z)), s(0)=1.

The exact generating functions are

    sum_(n>=0) A_n z^n
      =(1-4z)/(2Q(z)^(3/2))+(1-2z)/(2Q(z)),
    sum_(n>=0) B_n z^n=4z/Q(z).                         (3)

Here is a derivation of the first identity. Since

    A_n=CT_x (x^(-1)+2+2x)^n/(1-2x^2)^2,

sum the geometric series in z. The small root of

    2z x^2-(1-2z)x+z=0

is

    eta=(1-2z-s)/(4z), eta=z+O(z^2).

Formal residue extraction, equivalently Cauchy extraction on a fixed small x-circle followed by expansion for sufficiently small z, gives

    sum A_n z^n=1/[s(1-2eta^2)^2].

The other quadratic root lies outside that circle and the poles of (1-2x^2)^(-2) can also be kept outside. The identities

    1-2eta^2=s eta/z,
    1/eta=(1-2z+s)/(2z)

reduce the last expression to

    (1-2z+s)^2/(4s^3),

which is (3). Apparent divisions by z in this derivation are removable formal Laurent manipulations, not modular inversions of an integer index.

The second identity follows directly from the Pell recurrence. In particular

    B_(n+2)=4B_(n+1)+4B_n,
    B_0=0, B_1=4.                                     (4)

Introduce the integral auxiliary coefficients

    C_n=[z^n]Q(z)^(-1/2), C_(-1)=0,
    Z_n=C_n-4C_(n-1).

The integrality of C_n also follows from

    C_n=[x^n]P(x)^n.

Multiplying the residual generating function by Q gives, at every index l>=2,

    R_l-4R_(l-1)-4R_(l-2)=(35/2)Z_l.                 (5)

This holds for either sign. The sign-dependent part is annihilated by Q.

## 3. A fourth-order integer recurrence

The generating function of Z is

    Z(z)=(1-4z)/sqrt(Q(z)).

Direct differentiation gives the polynomial differential equation

    zQ(z) Z''+(6z-3)Z'-6Z=0.

For example it can be verified by substituting the displayed algebraic expression and multiplying by Q^(5/2); it is an identity of polynomials, not an empirical recurrence fit. Coefficient comparison yields

    (j^2-4)Z_(j+2)
      =2j(2j-1)Z_(j+1)+4j(j-1)Z_j, j>=0.           (6)

Substitute (5) into (6) with j=n+2. Both residual signs satisfy

    n(n+4)R_(n+4)
    -2(4n^2+15n+6)R_(n+3)
    +4(2n^2+7n+10)R_(n+2)
    +8(n+2)(4n+5)R_(n+1)
    +16(n+1)(n+2)R_n=0, n>=0.                       (7)

This is an integer identity valid also where one of its coefficients vanishes. Its derivation proves it at the exceptional indices without division.

The initial values are

    R_0=35,
    R_1=70-24epsilon,
    R_2=420-96epsilon,
    R_3=1960-480epsilon,
    R_4=9660-2304epsilon.                            (8)

They follow from coefficient extraction in (3), or directly from the defining finite sums. The equation at n=0 relates R_0,R_1,R_2,R_3 and contains no R_4. Consequently R_4 is indispensable initial data for forward propagation from the origin.

For practical reduction at an admissible prime, initialize R_1 through R_4 from (8). For every target index n<p, all forward steps required to reach that target have unit leading coefficient. Thus (7) is a finite, division-safe procedure for the exact residue in (1), and indeed for R_n modulo any power of that prime.

## 4. Complete division ledger

All recurrences are first stated as integer identities. The following list identifies the nonunit divisions if one elects to solve them in a particular direction.

1. In (7), forward propagation divides by j(j+4). For an odd prime p it fails precisely at j=0 or -4 modulo p. At the integer index j=0 the coefficient is exactly zero, so no increase in precision can recover R_4 from that equation.

2. Backward propagation in (7) divides by 16(j+1)(j+2). For odd p its exceptional indices are j=-1 or -2 modulo p. At p=2 this coefficient is always a nonunit.

3. In (6), forward propagation divides by j^2-4, with exceptional classes j=+2 or -2 modulo an odd prime. At the integer index j=2 this coefficient is zero. Backward propagation divides by 4j(j-1), exceptional at p=2 or j=0,1 modulo an odd prime. The algebraic definition of Z fixes the data that this degenerate recurrence alone does not fix.

4. The auxiliary central coefficients obey

       (j+1)C_(j+1)=2(2j+1)C_j+4j C_(j-1).

   Forward use divides by j+1, exceptional at j=-1 modulo p. The direct coefficient definition remains integral at that index.

5. Equation (4) needs no forward division; backward use divides by 4 and is unavailable at p=2.

6. Recovering Z from (5) divides by 35/2, requiring p different from 2,5,7. Recovering A and B from both residual signs uses

       A=(R^(+)+R^(-))/70,
       B=(R^(-)-R^(+))/12,

   requiring p different from 2,3,5,7. The actual normalization 16chi_p/105 in (1) has exactly the same excluded prime set. Every one of these primes is outside the actual strip p>=11.

7. The generating-function square roots are formal roots with constant term one. Their coefficient recursion divides by 2 only. No factorial-series reduction modulo p is used.

For an integer step j>0 with a=v_p(j(j+4))>0, solving (7) for R_(j+4) modulo p^h generally requires the right side modulo p^(h+a), followed by exact division by p^a over the integers and inversion of the remaining unit. Reducing the equation merely modulo p^h loses the needed information. The analogous backward precision loss is v_p(16(j+1)(j+2)).

In particular, for a target n<p the loop j=1,...,n-4 has both j and j+4 below p, so no such precision loss occurs. The recurrence determines each requested residual from four explicit initial residues; it does not by itself prove that the result is nonzero.

## 5. Four consecutive zeros and an all-size gcd restriction

Fix either sign and put

    g_l=gcd(|R_l|,|R_(l+1)|,|R_(l+2)|,|R_(l+3)|), l>=1.

Then

    g_l divides 16^(l-1) l! (l+1)!.                  (9)

Proof. The values in (8) give

    gcd(R_1,R_2)=2

for both signs; all R_1 through R_4 are even, so g_1=2. Starting with a block at l, apply (7) backwards. At the step recovering R_j, multiplication by

    b_j=16(j+1)(j+2)

makes that earlier value an integer linear combination of the subsequent four values. Consequently, after all steps j=l-1,...,1, the product

    D_l=product_(j=1)^(l-1)b_j
       =16^(l-1) l!(l+1)!/2

multiplies each of R_1,...,R_4 into a multiple of g_l. Bezout applied to their gcd 2 gives g_l|2D_l, proving (9). For l=1 the empty product gives the same formula.

A direct consequence is

    p>l+1, p odd  ==>  R_l,...,R_(l+3)
                            cannot all vanish modulo p. (10)

In particular, no four consecutive residual values wholly within indices 1,...,p-1 vanish simultaneously. This concerns consecutive integer indices of the auxiliary sequence. It does not claim that four successive admissible indices 4k,4k+4,4k+8,4k+12 obey the same restriction.

There is a precise reason why this recurrence restriction cannot become an individual unit theorem merely by inspecting its coefficients. On any interval where both extreme coefficients in (7) are units, its four-state transition is invertible over F_p. Arbitrary four-state initial data are therefore possible for solutions of the homogeneous recurrence, including data with a specified coordinate zero. Such data need not be the actual residual data (8). The actual initial residues and their propagation remain essential. No claim that the actual residual always vanishes or always survives is inferred from this observation.

## 6. Positivity and a parameter-uniform residual-content bound

Set

    alpha=2+2sqrt(2), beta=2-2sqrt(2).

For every even n>=2 and both signs,

    0<R_n^(epsilon)<=C(n)alpha^n,
    C(n)=35(n/2+1)+3sqrt(2).                         (11)

Here the nonzero lower bound is important: it makes the residual content a finite integer rather than a zero-gcd convention.

To prove positivity, decompose the generating function in (3) as

    A_n=(H_n+L_n)/2,
    H_n=[z^n](1-4z)Q^(-3/2),
    L_n=(alpha^n+beta^n)/2.

Differentiating Q^(-1/2), or comparing generating functions, gives

    H_n=(n+2)C_n/2-n C_(n-1).

The displayed recurrence for C_n and its positive coefficients give C_n>=2C_(n-1) for n>=1. Hence H_n>=C_n>0. For even n, beta^n>0, so

    A_n>=alpha^n/4.

The Pell closed formula gives, at even n,

    B_n=(alpha^n-beta^n)/sqrt(2),
    0<B_n<=alpha^n/sqrt(2).

Therefore

    R_n^(+) >=(35/4-3sqrt(2))alpha^n>0,
    R_n^(-)>0.

For the upper bound, the positive coefficient formula is

    A_n=sum_(u=0)^(n/2)(u+1)2^u [x^(n-2u)]P(x)^n.

Evaluate the positive polynomial P(x)^n at x=1/sqrt(2). The selected terms imply

    A_n<=(n/2+1)2^(n/2)P(1/sqrt(2))^n
        =(n/2+1)alpha^n.

Together with the bound for B_n this proves (11).

Define the positive integer

    Delta_n=R_n^(+)R_n^(-)
           =1225A_n^2-36B_n^2, n even, n>=2.

It satisfies

    log Delta_n<=2n log alpha+2log C(n).              (12)

Now fix one admissible n=4k. Let P_n be any finite set of distinct admissible primes on the t=2 strip for which the actual character-selected residual vanishes. Thus each p in P_n has its own m=2p-1, satisfies p>n, p>=11 and U(n,m)!=0, and obeys

    R_n^((2/p))=0 modulo p.

Then

    product_(p in P_n) p divides Delta_n,
    sum_(p in P_n) log p<=2n log alpha+2log C(n).     (13)

More strongly,

    sum_(p in P_n) v_p(R_n^((2/p))) log p
       <=log Delta_n.                              (14)

Indeed each selected residual is one of the two integer factors of Delta_n; its local valuation is no greater than the valuation of their product. Unique factorization proves (13)-(14).

Consequently the number of such distinct primes is at most

    [2n log alpha+2log C(n)]/log(n+1).               (15)

This is a parameter-uniform content bound within the actual strip, not a statement about densities. It applies in particular after restricting the primes to any moving range consistent with m~rho n log n. It needs no assumption that such a range contains primes.

The scope of the aggregate statement is a fixed-n fiber, with m varying as 2p-1. At fixed n,m the t=2 condition specifies at most one p. The bound is not a sum over every possible M,t strip and is not an all-family denominator-rate theorem.

Equation (14) concerns valuations of the integer residuals. Beyond first order they are not known to equal valuations of pT. Thus (14) does not bound the higher-depth cancellation of the actual rational numerator by replacing v_p(pT) with v_p(R_n).

## 7. Endpoint consequences of a residual zero

Within the actual strip, all of 35,6,2 are p-units. Equation (1) and U=A_n modulo p show that, whenever the residual vanishes,

    U=0 modulo p  if and only if  Pell_n=0 modulo p. (16)

Indeed the residual relation is 35A_n=6epsilon_p B_n, and B_n=2^(n+1)Pell_n.

Thus the local alternatives are sharper than an unevaluated zero test:

* If R_n^(epsilon_p) is nonzero, the exact pole and companion law are (2).
* If R_n^(epsilon_p)=0 and Pell_n is nonzero modulo p, then U is a p-unit and T is p-integral. Therefore v_p(Bbeta)=0: this prime disappears from the actual companion denominator.
* If both R_n^(epsilon_p) and Pell_n vanish, then p divides both A_n and U. Moment cancellation has occurred, but the actual companion denominator requires higher depth.

For either of the first two alternatives the recurrence (7), initialized by (8), and the Pell recurrence (4) give a finite division-safe calculation at every target n<p. This is a deterministic procedure, not a claimed execution or a uniform unit assertion.

The residual content bound (13) bounds all first-layer moment-canceling primes on the strip, including the third alternative. It does not establish that any of those alternatives occurs infinitely often.

## 8. The exact higher-depth quantities

The endpoint itself has a short first lift. Define the p-integral rational coefficient

    E_n=[x^n]P(x)^n C(x)^(-2)log C(x),
    log C(x)=-sum_(h>=1)2^h x^(2h)/h.

Since n<p, only h<=n/2<p occurs. Expanding the actual exponent 2m=4p-2 in the finite coefficient extraction gives

    U=A_n+4p E_n modulo p^2.                         (17)

This is a Taylor identity in the exponent, with coefficient denominators dividing powers of two and factorials below p. It is not an assertion about infinite p-adic analytic convergence.

If p divides A_n and

    A_n/p+4E_n !=0 modulo p,

then v_p(U)=1. The division A_n/p is taken in the integers before reduction. If that expression vanishes, U must be lifted further; the nonzero-endpoint hypothesis ensures its valuation is finite.

For T retain the exact Laurent identity, with the actual coefficients c_h of F=P^n C^(4p-2). Since floor(J/p)=8 and n<p, splitting out all positive multiples of p gives exactly

    pT=sum_(a=1)^8 c_(n+ap) tau_(ap)/a
       +p sum_(-n<=d<=J, d!=0, p does not divide d)
                   c_(n+d) tau_d/d.                 (18)

Every denominator left in (18) is a p-unit. The terms a=4,8 have tau_(ap)=0 exactly, but retaining them is harmless. The second sum includes negative Laurent indices, as required by the exact numerator. They have no highest-layer pole but reappear at the next order.

Let u=v_p(U). The precise final condition is

    v_p(Bbeta)=max(0,1+u-v_p(pT)),
    p absent from Bbeta iff pT=0 modulo p^(1+u).      (19)

If T=0, Bbeta=1 with the usual zero-numerator convention. To determine survival it suffices to know u and (18) modulo p^(1+u). To determine an exact positive surviving exponent, the first nonzero order below 1+u suffices. Higher valuations beyond that threshold are unnecessary for the denominator question.

The recurrence for the residual can compute R_n modulo any p-power from its explicit initial values while n<p. It does not identify that lift with (18). The retained relation (1) was proved modulo p only. At the next order, (18) also contains regular Laurent terms, corrections to tau_(ap), and corrections to the actual coefficients with exponent 4p-2. These are not specified by lifting the congruence (1) alone. In general adding p times an arbitrary p-integral quantity preserves (1) while changing the next digit. Accordingly (18), not an unsupported extension of (1), is the deciding complete lift.

This states both remaining pieces explicitly: an endpoint lift beginning with (17), and the full rational numerator at precision p^(1+u).

## 9. An explicit asymptotic congruence family

The content theorem already applies to every nonzero node in the strip. If the retained binary allocation is desired to guarantee U!=0, it remains an additional requirement

    m=-k modulo P2, k<P2<=2k,

where P2 is a power of two. On m=2p-1 this becomes

    2p=1-k modulo P2.                              (20)

For example choose an integer a>=2 and put

    P2=2^a, k=P2-1, n=4(P2-1), H=P2/2.

For a fixed rho>0 define the odd candidate

    p_candidate=1+H ceil(((rho/2)n log n-1)/H),
    m_candidate=2p_candidate-1.

For all sufficiently large a,

    p_candidate>n, p_candidate>=11,
    p_candidate=1 modulo H,
    m_candidate=-k modulo P2,
    m_candidate=rho n log n+O(n).

Whenever this candidate is prime, it is an actual member of the t=2 strip; the binary allocation supplies U!=0. The recurrence, content bound, and denominator alternatives all apply.

This construction gives infinitely many integer parameter congruences. It does not establish infinitely many prime candidates, nor infinitely many surviving or canceling prime members. It is included solely to make compatibility of the strip, n=4k, the optional endpoint allocation, and the asymptotic size explicit.

## 10. Completed stage and limitations

The new proved stage consists of:

* exact generating functions and the fourth-order integer recurrence (7);
* an explicit ledger of every nonunit division in its forward, backward, and auxiliary propagation;
* the consecutive-block gcd bound (9) and the no-four-zero consequence (10);
* positivity and the O(n) residual-content bound (13)-(14) on the actual fixed-n strip;
* the endpoint/Pell dichotomy (16), which turns many first-layer zeros into complete removal from den(T/U);
* explicit endpoint and complete numerator lifting requirements (17)-(19).

The no-four-zero statement is not asserted for consecutive multiples of four. The content bound is not a claim about all strips or about prime density. It controls integer residual valuations and first-layer moment cancellation, not arbitrary higher cancellation of pT. No leading-rate improvement below the actual companion threshold 5/82 is claimed.

The four previously resolved unit-multiple-of-U regions and the gap-one surviving pole are unchanged and are not new tasks in this note. No new numerical result or symbolic-check receipt is claimed. All new conclusions here rest on their written derivations. The completed source paper and its successful certificate remain preserved.
