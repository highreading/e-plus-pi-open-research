> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The next logarithmic quotient sector: M=4

Child 1 author result, 2026-10-02. English, offline, finish-only closeout of the accepted task. This paper completes the existing sector calculation; it starts no further research stage. The written all-index arguments below are author proofs, not independently reviewed theorems. The existing symbolic certificate has narrower scope, specified in Section 9.

## 1. Scope and retained definitions

Retain n=4k, k>=1, m>=0,

    P(x)=1+2x+2x^2, C(x)=1-2x^2,
    F(x)=P(x)^n C(x)^(2m)=sum_h c_h x^h,
    J=n+4m, U=c_n != 0,
    Bbeta=den(T/U).

The actual logarithmic numerator has the retained rational identity

    T=sum_{-n<=a<=J, a!=0} c_(n+a) tau_a/a,
    tau_a=(2/i)(((-1+i)/2)^a-((-1-i)/2)^a).

Negative indices are part of this exact identity. This paper uses its first residue at primes p>max(n,sqrt(J)), p<=J. These inequalities remove negative multiples of p from the first residue, not negative terms from the exact lift.

The prior files LOGARITHMIC_COLLECTED_COEFFICIENT_RELATIONS.md and LOGARITHMIC_RESIDUAL_RECURRENCE.md are retained unchanged. In particular, the latter's M=3 fourth-order recurrence, nonunit-index ledger, and fixed-n cancellation-mass theorem are neither replaced nor rechecked here.

The outcome is a new fixed-t M=4 sector theorem, with an explicit O(n+t) height bound and a concrete obstruction to applying the same residual construction uniformly over unbounded t. It is not an all-t O(n) theorem.

## 2. Exact M=4 domain and all three sectors

Write

    2m=4p+r=5p-t, r=p-t,
    m=(5p-t)/2, 1<=t<=p.

Because p is odd and m is integral, t must be odd. Conversely odd t in this interval gives the exact quotient M=4 and a nonnegative integral m.

The leading-prime domain is equivalently

    n=4k, p prime, p>n, p>=11,
    t odd, 1<=t<=p, m=(5p-t)/2, U!=0.

Indeed J=n+10p-2t satisfies 8p<J<11p<=p^2 under these conditions. Conversely floor(J/p)>=8 and p>sqrt(J) force the prime p to be at least 11.

Put

    d=floor((n+2r)/p), floor(J/p)=8+d.

The exact sectors are

    d=2: 1<=t<=n/2, t odd;
    d=1: n/2<t<=(p+n)/2, t odd;
    d=0: (p+n)/2<t<=p, t odd.

Since n/2 is even, the largest allowed t in d=2 is n/2-1 and the smallest in d=1 is n/2+1. Since p+n is odd, the other displayed boundary is a half-integer; the inequalities are to be interpreted exactly, not rounded outward.

All three sectors actually occur. For n=4 and any p>=11, t=1,3,p give d=2,1,0 respectively. The endpoint condition does not invalidate these examples: direct coefficient expansion gives

    U=8m^2-132m+136=4(2m^2-33m+34).

Its quadratic discriminant is 817, strictly between 28^2 and 29^2, so it has no integral root. This is an algebraic realization of the sectors, not a prime scan or density assertion. For general n, U!=0 remains a separate hypothesis; no binary allocation is inferred merely from M=4.

## 3. Residue from the actual coefficients and its units

Let Y=P^n C^r and ell_v=[x^(n+vp)]Y for 0<=v<=d. Frobenius applied to the actual polynomial gives

    F=Y C(x^p)^4 modulo p.

Collecting the first Laurent residue therefore gives

    pT=chi_p sum_{v=0}^d ell_v Phi_v(4) modulo p,
    chi_p=(-1)^((p-1)/2),

where

    Phi_v(4)=sum_{0<=h<=4, v+2h!=0}
                 binom(4,h)(-2)^h tau_(v+2h)/(v+2h).

Every denominator index actually used is at most 8+d<p. The retained weight relations, or direct evaluation of these finite sums, give

    (Phi_0(4),Phi_1(4),Phi_2(4))
       =(16/3,-536/315,4/5).

Thus none of the three weights vanishes identically over Q. In particular the third weight is 4/5, not zero.

For explicit coefficient formulas put a_j=[x^j]P^n, with a_j=0 outside 0<=j<=2n, and define

    A=A_(n,t)=sum_{u=0}^{n/2}
                    2^u a_(n-2u) binom(t+u-1,u),

    B=B_(n,t)=sum_{1<=j<=2n-1, j odd}
                    a_j 2^((n+1-j)/2)
                    binom(t-1+(n-j)/2,t-1),

    D=D_(n,t)=2(-1)^(t-1) sum_{u=t}^{n/2}
                    2^u a_(n-2u) binom(u-1,t-1).

Generalized binomial coefficients are rational numbers before reduction. The last sum is zero when empty. The actual complementary-power identity

    Y=C(x^p)P(x)^n/C(x)^t modulo p

and coefficient extraction give

    ell_0=A, ell_1=epsilon_p B, ell_2=D modulo p,
    epsilon_p=(2/p),

where only present blocks are used. This is the retained coefficient argument, specialized to the present domain: reduction of the high binomial coefficients is allowed because t-1<p; reciprocity a_(n+2u)=2^(2u)a_(n-2u) gives the last formula. Also U=A modulo p because n<p and the other Frobenius blocks cannot contribute to c_n.

Consequently

    d=2: pT=(4chi_p/315)(420A-134epsilon_p B+63D) mod p;
    d=1: pT=(4chi_p/315)(420A-134epsilon_p B) mod p;
    d=0: pT=(16chi_p/3)U mod p.

For odd t, D>=0; it is strictly positive in d=2, since t<=n/2-1 and all coefficients in its nonempty sum are positive. It is identically zero for t>n/2. An absent odd block in d=0 must not be treated as an additional independent coefficient.

All primes 2,3,5,7 are excluded by the domain. Thus 315 and the displayed prefactors are units. The integer weights 420 and 63 are units at every allowed prime. The middle weight has the additional numerator prime 67: Phi_1(4) vanishes modulo 67. This prime is allowed and must not be silently excluded. At p=67 in d=1 the residue is again (16chi_p/3)U, so its zero is equivalent to p|U. In d=2 the D term still remains at p=67. The two-sign residual theorem below includes p=67 without division by 67.

The d=0 unit-multiple-of-U result is the already established region retained here for completeness. At fixed n,m, its pole-removing primes have one-factor logarithmic mass at most log|U|. No other universal unit-multiple-of-U reduction is claimed for the remaining sectors.

## 4. Positivity of the residuals

For each n=4k and odd t>=1 define the rational residuals

    R_(n,t)^epsilon=420A_(n,t)-134epsilon B_(n,t)+63D_(n,t),
    epsilon in {+1,-1}.

For t>n/2 the last term is zero, exactly as required in d=1. The following proof does not need p.

Set

    b_j=2^(-j/2)a_j,
    f(s)=binom(s+t-1,t-1)=product_{l=1}^{t-1}(s+l)/l,
    g(s)=(f(s)+f(-s))/2.

For t=1 the empty product is one. All coefficients of f are nonnegative. Therefore g is an even polynomial with nonnegative coefficients, g(0)=1, and f(u)>=g(u) for u>=0. Reciprocity gives b_j=b_(2n-j).

Use the two weighted sums

    E_g=sum_{j even} b_j g((n-j)/2),
    O_g=sum_{j odd}  b_j g((n-j)/2).

They satisfy E_g>=O_g>0. To prove the first inequality without an asymptotic approximation, observe the exact generating identity

    sum_j (-1)^j b_j exp((j-n)y)
       =(2 cosh(y)-sqrt(2))^n.

The series 2 cosh(y)-sqrt(2) has positive constant term and nonnegative even coefficients. Every even derivative of its nth power at zero is nonnegative. It follows that, for every h>=0,

    sum_j (-1)^j b_j ((n-j)/2)^(2h)>=0.

Multiply these inequalities by the nonnegative coefficients of g and sum. This yields E_g-O_g>=0. Positivity of O_g follows from g>=1 on the real line and the positive odd coefficients of P^n.

Pairing j with 2n-j in the definition of B now gives

    B=sqrt(2) 2^(n/2) O_g >0.

For A, the same pairing and f(u)>=g(u) show

    A=2^(n/2) sum_{j even, j<=n} b_j f((n-j)/2)
      >=2^(n/2-1) E_g.

Hence

    0<B<=2sqrt(2) A.

In fact the central term makes the final comparison strict, but strictness is unnecessary below. Since t is odd, the formula for D also gives

    0<=D<=2A:

term by term, binom(u-1,t-1)<=binom(t+u-1,t-1) for u>=t. Therefore, with

    delta=420-268sqrt(2)>0,
    C0=546+268sqrt(2),

both signs satisfy

    0<delta A<=R_(n,t)^epsilon<=C0 A.                 (1)

The positivity of delta follows, for example, from 420^2>2*268^2 and 420>0. Thus neither sign residual vanishes identically or at an allowed integer pair n,t. This is an all-index author proof; the earlier finite certificate alone did not prove it.

## 5. Integer residuals and their explicit heights

These rational residuals admit a denominator clearer containing no odd prime. For any half-integer q and integer L>=0,

    4^L binom(q,L) is an integer.

One justification is to write (1+z)^q=(1+z)^a(1+z)^(1/2) for an integer a. Integer powers, including negative ones, have integral Taylor coefficients, while 4^h binom(1/2,h) is integral; the coefficient convolution proves the assertion.

In B the smallest displayed power of 2 is 2^(1-n/2), and L=t-1. Thus the common clearer

    H_(n,t)=2^(n/2+2t-2)

makes B, A, and D integral after multiplication. Define two positive integers

    Z_(n,t)^epsilon=H_(n,t) R_(n,t)^epsilon,
    Delta_(n,t)=Z_(n,t)^+ Z_(n,t)^- >0.

H is a unit at every allowed prime. These integers depend on n,t but not on p or m. On d=1 or d=2,

    pT=0 modulo p iff p divides Z_(n,t)^(epsilon_p).  (2)

For a quantitative bound put alpha=2+2sqrt(2). Positivity of the coefficients gives

    A<=alpha^n binom(t+n/2-1,n/2).

Indeed the binomial weight is increasing with u, and

    sum_{u=0}^{n/2} 2^u a_(n-2u)
       <=2^(n/2) P(1/sqrt(2))^n=alpha^n.

Combining this with (1) gives the explicit bound

    log Delta_(n,t)
      <=2(n/2+2t-2)log 2+2n log alpha
        +2log binom(t+n/2-1,n/2)+2log C0.            (3)

In particular log Delta=O(n+t), since binom(t+n/2-1,n/2)<=2^(t+n/2-1). This proves O(n) for every fixed odd t, and uniformly on any separately specified range t<=C n, with the constant depending on C. It does not prove O(n) uniformly over arbitrary t<=p when p/n is unbounded.

## 6. Precise cancellation-mass consequence

Fix n=4k and an odd t. Consider distinct primes p satisfying the domain in Section 2, lying in d=1 or d=2, and take m=(5p-t)/2 for each prime. Retain only primes for which the first residue vanishes. By (2),

    sum_p log p
       <=sum_p v_p(Z_(n,t)^(epsilon_p)) log p
       <=log Delta_(n,t).                           (4)

The second inequality holds because the selected prime powers divide the product of the two fixed positive integers Z^+ and Z^-. Consequently the number of such primes is at most log Delta/log(n+1).

Thus each fixed-t fiber has cancellation mass O(n); more generally each fiber with t<=C n has the uniform bound O_C(n). Here n and t are held fixed when the prime sum is formed, and m varies with p. No assertion about the number or supply of primes on that fiber is needed.

This is the new sector theorem beyond the M=3,t=2 result. Its valuation-weighted statement concerns the integer residuals, not higher-order valuations of the actual rational pT.

There are two limits to aggregation. First, even d=2 has n/4 possible odd t values. Applying (3) independently to all of them gives only an O(n^2) product-height bound, not O(n). Second, d=1 permits t unbounded relative to n. A finite set of t values can be handled by multiplying the corresponding Delta values, but this construction does not furnish a bounded number of O(n)-height residuals covering all M=4 primes.

## 7. A specific obstruction for the natural all-t residual construction

The existing symbolic calculation gives the exact n=4 expressions

    A_(4,t)=2t^2+66t+136,
    B_(4,t)=c_t * 128t(2t^2+12t-23)/(3(2t-3)),
    c_t=binom(2t-2,t-1)/4^(t-1).

For odd t>=7, D_(4,t)=0. Let s_2(a) denote the number of ones in the binary expansion of a. Legendre's factorial valuation formula gives

    v_2(binomial(2a,a))=s_2(a).

All of t, 2t^2+12t-23, and 3(2t-3) are odd. Hence

    v_2(B_(4,t))=9+s_2(t-1)-2t,
    v_2(134B_(4,t))=10+s_2(t-1)-2t<0.

The last inequality holds for all odd t>=7: it holds at t=7, and the elementary bound s_2(t-1)<=log_2(t-1)+1 suffices for all t>=9. Since 420A is integral, adding it cannot change this negative valuation. For either sign,

    v_2(R_(4,t)^epsilon)=10+s_2(t-1)-2t.

The residual is dyadic by Section 5. Its reduced denominator is therefore exactly

    2^(2t-10-s_2(t-1)).                              (5)

Moreover R>=delta A>1 here. Its positive reduced numerator consequently has logarithmic height at least

    (2t-10-s_2(t-1))log 2=Omega(t).

This proves that merely clearing and reducing the natural two sign residuals cannot yield an O(n) bound uniform in all t: already n=4 has linear growth in t. Whenever p>=11 and p>2t with t odd>=7, this calculation lies in the actual d=1 sector. The endpoint U is nonzero by the n=4 polynomial in Section 2. No assertion of prime density or a special prime-producing family is used.

This is a precise obstruction to the present construction, not a theorem that every alternative elimination of the prime parameter is impossible. A different normalization or relation might reduce the height, but none is established here. The O(n+t) upper bound and (5) are consistent: the t-dependence is real for these natural reduced residuals.

## 8. Endpoint content and complete denominator disappearance

Let u=v_p(U) and let R_actual=pT in Z_(p). Throughout the domain,

    v_p(Bbeta)=max(0,1+u-v_p(R_actual)).              (6)

If the selected residual in (2) is nonzero modulo p, then v_p(T)=-1 and v_p(Bbeta)=1+u. If it is zero, T is p-integral. This removes the first moment pole only.

Since U=A modulo p, a zero residue with p not dividing A has u=0 and removes p from Bbeta. If p divides A, the endpoint is not a unit and removal requires the complete condition

    pT=0 modulo p^(1+u).

The exact expression to lift is

    pT=sum_{-n<=a<=J, a!=0} c_(n+a) p tau_a/a.

All its terms are p-integral. The regular terms, including negative Laurent indices, must be restored for higher precision. The congruence involving Z^epsilon is a first-order statement; no equality of its higher valuations with those of pT has been proved. The power-of-two clearer H introduces no additional odd-prime valuation, but that fact does not upgrade a modulo-p identity to a higher congruence.

If T=0, use v_p(0)=infinity and Bbeta=1. The separate denominator of the complete center alpha+T/U is not determined by this logarithmic calculation.

## 9. Evidence, provenance reconciliation, and closeout

The existing artifact

    work/session_20261001_astra/agent1/logarithmic_next_sector_checks.json

has controller-confirmed status PASS_NEW_M4_WEIGHT_AND_SYMBOLIC_OBSTRUCTION_IDENTITIES. It was substantively read back during closeout. It records Phi(4)=(16/3,-536/315,4/5), the normalized weights (420,-134,63), the two n=4 formulas used in Section 7, and delta>0. Its scope expressly excludes an all-index sector or mass proof. It has not been rerun or replaced. No separate saved checker script or independent review is claimed.

The following preserved author notes were substantively read during closeout:

* Source [session identifier removed], recorded 2026-10-02T14:45:10+0800. It announced all three odd-t sectors, the normalized residue, and intended fixed-t bounds. Its mathematical statements and promised coherent-paper disposition are now supplied by Sections 2-7. A promised save in that note was not treated as a write receipt.
* Source [session identifier removed], recorded 2026-10-02T15:19:57+0800. It announced finish-only reconciliation and saving; it contained no additional proof. This paper and its companion report discharge that documentation task once genuine readbacks are obtained.

Their exact preserved paths are

    .astra-notes/[session identifier removed]/[session identifier removed]/notes/62/[session identifier removed].001.json
    .astra-notes/[session identifier removed]/[session identifier removed]/notes/79/[session identifier removed].001.json

These are author-note provenance records, not verification verdicts. The present parity-moment positivity proof, explicit dyadic clearer, mass bound, and reduced-denominator obstruction are the bounded written completion of the accepted task. They have not received independent review. No assertion that all historical messages were audited by Child 1 is made; the main closeout owns the wider record audit and file index.

Unproved at termination: a bounded collection of O(n)-height residuals covering every M=4 t sector at once; an O(n) all-t cancellation-mass theorem; any growing-M uniform extension; higher endpoint cancellation depths; a leading improvement for the actual companion denominator; and the global e+pi problem. The actual e+pi problem remains OPEN.

The stage ends at the user's request. There is no new assignment or continuation loop. Original files, evidence, and references are preserved in place. The companion handoff is LOGARITHMIC_NEXT_QUOTIENT_SECTOR_REPORT.md.
