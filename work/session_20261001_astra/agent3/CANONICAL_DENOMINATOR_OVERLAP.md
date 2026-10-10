> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual denominator overlap for the factorial B-only Gram center

Original author research, offline; not independently reviewed. CANONICAL_COMPANION_TRANSFER.md is preserved without calculation replay. All denominators below belong to the SAME canonical factorial B-only center. Neither coordinate-center nor full-coefficient-center arithmetic is transferred.

The new fixed-b theorem proves that eventual B|q fails for b=3,m=1: at every n=11^h+3, h>=6, the 11-part of the overlap loses exactly one power. This follows from a new exact seed evaluation and an all-index congruence proof, not from extrapolation of finite samples. A global overlap-loss rate remains unresolved.

## 1. Retained integer data and the exponential numerator

Use the fraction-free data of the preserved companion-transfer note:

    F2=(n!)^2, d_i=(n+i)!/n!, D0=diag(d_i),
    M=2^n n! D0 T, Delta=det M!=0,
    J=(2^n/n!)fP,
    C=Krec adj(M)D0, x=CJ,
    Omega=diag(((n+m+1)_j)^2),
    Dg=x^T Omega x>0, z=C^T Omega x.

Here Krec=Z(I+D)^(-n), where Z multiplies by t-1, and the falling factorial at j=0 is one. In particular the endpoint numerator is

    Rcal=Delta x_0,
    kappa=Rcal/(F2 Dg).

Let g=gcd_i |z_i|, G(t)=sum_i(z_i/g)t^i, d=deg G<=b-1, and N=2n+d. Retain

    L=L_N=2^(N-1)lcm(1,...,N),
    K_z(t)=(2^n/n!)t^n D_t^n((t^2-t+1/2)^n sum_i z_i t^i),
    T_z=L calL((K_z-Dg)/(t-1)) in Z.

Thus beta=T_z/(L Dg). These are the existing definitions; no estimate for their final gcds is assumed.

We now supply an integer numerator for the exponential companion in the same normalization. Write

    a_s(n)=[t^s](1-t+t^2/2)^n,
    Dcal_j=j! sum_(k=0)^j 1/k!,
    Dcal_0=1, Dcal_j=j Dcal_(j-1)+1,
    dmax=(n+b-1)!/n!.

Define, for 0<=i<b,

    Ecal_i=2^n(n+b-1)!
       sum_(s=0)^min(2n,n+i)
          a_s(n) Dcal_(2n+i-s)/(n+i-s)!,
    Acal=z^T Ecal.

Every Ecal_i is integral: 2^n clears the coefficients a_s, and (n+i-s)! divides (n+b-1)! throughout this sum. All factorial arguments are nonnegative.

The exponential part of fQ_i is the displayed sum before multiplication by 2^n(n+b-1)!. Using the retained normalized adjoint lambda=(2^n/n!)z/Dg therefore gives exactly

    alpha=Acal/(F2 dmax Dg),
    gamma=kappa+beta=(L Rcal+F2 T_z)/(F2 L Dg),
    c=alpha+gamma.                                             (1)

The endpoint contribution Rcal is retained. Primitive selector content has not been assumed to cancel any factorial factor.

## 2. All reduced denominators and the exact overlap defect

Take the common positive integer denominator and integer numerators

    Dcommon=F2 dmax L Dg,
    U=L Acal,
    V=dmax(L Rcal+F2 T_z).

Then alpha=U/Dcommon, gamma=V/Dcommon, and c=(U+V)/Dcommon. Define

    g_e=gcd(Dcommon,|U|),
    g_gamma=gcd(Dcommon,|V|),
    g_c=gcd(Dcommon,|U+V|),
    g_0=gcd(Dcommon,|U|,|V|).

The exact positive reduced denominators are

    Q=den(alpha)=Dcommon/g_e,
    B=den(gamma)=Dcommon/g_gamma,
    q=den(c)=Dcommon/g_c,
    C_overlap=gcd(q,B)=Dcommon/lcm(g_c,g_gamma).                 (2)

Use gcd(Dcommon,0)=Dcommon. The formulas consequently include zero companions or a zero center without a special unjustified nonvanishing assumption.

Since g_0 divides g_c, define the integer overlap defect

    delta=g_c/g_0.                                             (3)

The identities

    gcd(g_e,g_gamma)=g_0,
    gcd(g_c,g_gamma)=g_0

give

    q=lcm(Q,B)/delta,
    C_overlap=B/delta,
    delta divides gcd(Q,B).                                    (4)

The final divisibility in (4) also follows from the primewise description below. In particular

    B|q iff delta=1.                                           (5)

All these quantities are invariant under multiplying Dcommon,U,V by a common positive integer. Thus the use of a convenient common denominator has not replaced a reduced denominator.

## 3. The exact lcm relation and equal-depth congruence

Because c=alpha+gamma, q divides lcm(Q,B). Because alpha=c-gamma, Q divides lcm(q,B). Taking lcm with B proves

    lcm(q,B)=lcm(Q,B),
    q/C_overlap=Q/gcd(Q,B).                                    (6)

This does not imply B|q.

Fix a prime p and put a_p=v_p(Q), b_p=v_p(B). If a_p!=b_p, the summands have unequal denominator depths, so

    v_p(q)=max(a_p,b_p),
    v_p(C_overlap)=b_p,
    v_p(delta)=0.                                              (7)

If a_p=b_p=0, these valuations are all zero. The only possible loss occurs when a_p=b_p=t>0. Write the reduced companions as

    alpha=Ared/(p^t Q0), gamma=Gred/(p^t B0),
    p does not divide Ared Gred Q0 B0.

Then

    v_p(delta)=min(t,v_p(Ared B0+Gred Q0)),
    v_p(q)=v_p(C_overlap)=t-v_p(delta).                         (8)

Here v_p(0)=infinity. Thus loss of at least k powers, 1<=k<=t, is equivalent to the specific unit-numerator congruence

    Ared B0+Gred Q0=0 mod p^k.                                 (9)

There is also a direct version in the fraction-free data. If e=v_p(Dcommon) and

    v_p(U)=v_p(V)=s<e,

then the loss is

    min(e-s, v_p(U/p^s+V/p^s)).                                (10)

This is an exact test after removing their common p-power. Unequal valuations below e give no overlap loss. Equations (8)-(10) isolate the cancellation that must be controlled; equal denominator depths alone do not settle it.

## 4. A single exact b=3 seed

Now fix b=3,m=1. Thus dmax=(n+1)(n+2), and Omega has weights ((n+2)_j)^2, 0<=j<=3. Define

    S_n=Acal_n+dmax_n Rcal_n.

The new controller-backed evaluation at the single seed n=3 produced

    Delta_3=-1169408,
    Dg_3=1960127638514171904,
    x_(3,0)=-94670848,
    dmax_3=20,
    Acal_3=3836499125598452449280,
    Rcal_3=110708847017984,
    S_3=3836501339775392808960.

In particular

    (Delta_3,Dg_3,x_(3,0),dmax_3,Acal_3,Rcal_3)
       =(2,8,3,9,1,6) mod 11,
    S_3=44 mod 121.                                           (11)

The latter congruence also follows directly from the recorded factorization

    S_3=2^23 * 3 * 5 * 11 * 29 * 26539 * 3601463.

The exact record is denominator_overlap_seed3.json in this directory. It contains the seed matrices and vectors as well as these contractions. No second seed, degree scan, or completed checker was used. The infinite theorem below is proved by transfer modulo 121 from this finite exact input.

Notice the endpoint cancellation already in (11): Acal_3 is 1 modulo 11, whereas dmax_3 Rcal_3 is 10. Omitting kappa would remove the cancellation being studied.

## 5. New transfer modulo 121 for this Gram construction

Write n=a+3 with 121|a, and put tau=2^a. We prove the necessary congruences directly, including the exponential vector. No coordinate-selector transfer is invoked.

First, the normalized Toeplitz entries are

    M_ij(n)=2^n sum_s a_s(n)(n+i)_(j+s), 0<=i,j<=2,

where the summation is restricted by n+i-j-s>=0. If j+s>3+i, its falling factorial contains n-3=a, so the term vanishes modulo 121. All coefficients a_s(n) are 11-adically integral, including the discarded terms.

In the surviving terms s<=3+i-j<=5. For these s, a_s(n) is a polynomial in n with denominator dividing a power of 2 times s!, hence with denominator prime to 11. Reducing n to 3 in these short terms proves

    M(n)=tau M(3) mod 121.                                    (12)

For the exponential vector the factorial ratio is

    (n+2)!/(n+i-s)!=(n+2)_(2-i+s).

Terms with 2-i+s>5 contain a and vanish. The survivors have s<=3+i<=5. Their derangement indices have the form

    2n+i-s=2a+(6+i-s), 3<=6+i-s<=8.

The recurrence Dcal_j=j Dcal_(j-1)+1 resets at 2a modulo 121: Dcal_(2a)=1. Induction through the next eight indices gives Dcal_(2a+j)=Dcal_j modulo 121. Consequently

    Ecal(n)=tau Ecal(3) mod 121.                              (13)

It remains to propagate the actual positive forcing, rather than assuming it follows the exponential vector. Let P_k be the integer endpoint sequence with

    P_0=1, P_1=2,
    (k+1)P_(k+1)=2(2k+1)P_k+4kP_(k-1).

The exact forcing-circle coefficient identities for b=3 are

    J_0(n)=P_n,
    J_1(n)=P_n/2+P_(n+1)/4,
    J_2(n)=P_(n+2)/8.                                        (14)

For example, with w(theta)=1+sqrt(2)cos theta, the first three real polynomial factors on the conjugate circle are 1, (1+w)/2, and w^2/2. Integrating against 2^n w^n gives (14). The identities are rational identities, so their powers of two cause no difficulty modulo 121.

At k=a the backward recurrence term 4aP_(a-1) vanishes modulo 121. The next five divisors a+j, 1<=j<=5, are units. Induction therefore proves

    P_(a+j)=P_a P_j mod 121, 0<=j<=5,
    J(n)=P_a J(3) mod 121.                                   (15)

The b=3 reconstruction matrix Krec(n), D0(n), and the factorial metric Omega(n) are polynomial expressions in n with denominators prime to 11, so they agree with their n=3 values modulo 121. Applying the adjugate and contraction definitions to (12)-(15) gives

    C(n)=tau^2 C(3),
    x(n)=tau^2 P_a x(3),
    z(n)=tau^4 P_a z(3),
    Delta_n=tau^3 Delta_3,
    Dg_n=tau^4 P_a^2 Dg_3,
    Acal_n=tau^5 P_a Acal_3,
    Rcal_n=tau^5 P_a Rcal_3,
    S_n=tau^5 P_a S_3                                      mod 121. (16)

Every occurrence of the metric and endpoint term has been retained in these congruences.

## 6. An explicit unbounded normality sequence with exact loss

Take

    n_h=11^h+3, h>=6.

These indices are even. To establish the needed unit condition, use the endpoint generating function

    P(t)=sum_k P_k t^k=(1-4t-4t^2)^(-1/2).

Over F_11 it satisfies

    P(t)=(1-4t-4t^2)^5 P(t^11).

The prefactor has degree ten and constant coefficient one. Comparing coefficients at indices divisible by 11 gives P_(11k)=P_k modulo 11. Hence

    P_(11^h)=P_1=2 mod 11.

Also tau=2^(11^h)=2 modulo 11. From (11),(16), Delta_n,Dg_n,Acal_n,Rcal_n are 11-adic units, and

    S_n=33 mod 121,
    v_11(S_n)=1.                                             (17)

Indeed tau^5 P_a=9 modulo 11, and 9*44=33 modulo 121.

The unit determinant itself proves T is nonsingular at every n_h. Moreover n_h>=11^6+3>2^20. Since n/log n is increasing for n>e, and

    2^20>512*3^4*20 log 2,

these indices lie in the retained fixed-b=3 slow-growth domain. Thus this is a genuinely unbounded admissible normality sequence; it is not selected by a finite normality scan.

Put f=v_11(n!). The base-11 expansion of n_h has digit sum four, so

    f=(11^h-1)/10.

Because d<=2, the moment-clearer index obeys

    11^h <= N=2n_h+d <11^(h+1),
    v_11(L_N)=h.

Since Dg is an 11-adic unit and T_z is integral, beta=T_z/(L_NDg) has denominator depth at most h. On the other hand Acal,Rcal,dmax,Dg are units, and (1) gives

    v_11(Q)=2f,
    v_11(den(kappa))=2f.

Since 2f>h, adding beta cannot cancel the denominator depth of kappa. Thus

    v_11(B)=2f.                                              (18)

To determine the complete center, retain the exact sum

    c=S_n/(F2 dmax Dg)+beta.

Its first term has denominator depth 2f-1 by (17). As 2f-1>h, the entire logarithmic companion is too shallow to cancel that depth. Therefore

    v_11(q)=v_11(C_overlap)=2f-1,
    v_11(delta)=1.                                           (19)

Equivalently, for every h>=6,

    v_11(Q)=v_11(B)=(11^h-1)/5,
    v_11(q)=v_11(C_overlap)=(11^h-1)/5-1.

This proves B does not divide q at every index of this sequence. It rules out eventual B|q for the actual fixed-b=3,m=1 Gram family. It does not rule out divisibility for the different growing-b allocation, or for another subsequence.

There is also the explicit lower divisor

    11^((11^h-1)/5-1) divides C_overlap.

Its logarithm has order n, whereas the transfer scale is n log n. The one-power defect at 11 is therefore compatible with subfactorial TOTAL overlap loss, but does not establish it: all other primes remain to be controlled.

## 7. Use in the complete overlap inequality

Retain the already established canonical bound |alpha-e|<=E, with

    -log E~X_n, X_n=n log n

on the even slow-growth regimes of the companion-transfer note. This rate is an input here, not recalculated.

Write R=q|c-e-pi|. The e approximation theorem with exponent nu=2+epsilon and the lcm identity (6) imply

    Q<=qB/C_overlap,
    q>=C_epsilon^(1/nu) E^(-1/nu) C_overlap/B.

Together with the pi lower bound and the triangle inequality this gives the stated complete inequality

    C_pi <= E B^mu
        + R C_epsilon^(-1/nu) E^(1/nu) B^(mu+1)/C_overlap.

Using the exact defect from (4), it becomes

    C_pi <= E B^mu
        + R C_epsilon^(-1/nu) E^(1/nu) B^mu delta.             (20)

Thus exact divisibility is sufficient but unnecessary for the improved threshold. If

    beta_rate=limsup log B/X_n,
    defect_rate=limsup log delta/X_n,
    mu beta_rate+defect_rate<1/2,                             (21)

then one can choose nu>2 sufficiently close to 2 so that both error separation and primitive-error divergence follow. More precisely,

    liminf log R/X_n >=1/2-mu beta_rate-defect_rate>0.

The main has confirmed the published pi measure bound 36/5. For the uniform approximation inequality use an admissible exponent strictly above that bound unless the source supplies the boundary exponent itself. Taking such exponents arbitrarily close to 36/5 shows that

    beta_rate<5/72, log delta=o(X_n)

is sufficient. The strict threshold 5/72 therefore does not require eventual B|q. Without any overlap control, delta<=B recovers the weaker sufficient threshold 1/[2(mu+1)], tending to 5/82 at the published bound.

The fixed-b theorem prevents treating delta=1 as an established universal property. Its exact one-power loss does not decide the rate condition (21).

## 8. Precise remaining arithmetic

The total overlap loss has the exact prime expansion

    log delta = sum_(p: v_p(Q)=v_p(B)=t_p>0)
       min(t_p,v_p(Ared B0,p+Gred Q0,p)) log p,                (22)

where Q0,p=Q/p^t_p and B0,p=B/p^t_p. The reduced numerators Ared,Gred are those of alpha,gamma, including the endpoint correction inside gamma.

A proof that the sum in (22) is o(n log n), together with a suitable B budget, would establish the improved transfer condition without exact divisibility. Alternatively, excluding (9) for every equal-depth prime on a proposed normality subsequence would prove B|q there. Neither conclusion follows from the current results.

The additional arithmetic needed is specific: determine equal-depth primes and control the precision of their normalized numerator cancellations. For the fixed-b=3 sequence, (12)-(19) decide this calculation at 11 through modulus 121, including the shallow logarithmic term. Higher-depth behavior at other primes, or a uniform weighted sum over primes, requires new congruence/content information for Acal, Delta x_0, T_z and Dg. Bounds on their separate heights, or on possible supports of their contents, do not determine (22).

No denominator-divisibility theorem is claimed for the logarithmically growing b family. No global overlap rate or branch exclusion is proved here. The local nondivisibility theorem is independent of the pi measure input; the analytic consequences in Section 7 explicitly depend on that input and the retained canonical exponential bound.

## 9. Deliverables and status

This note proves exact reduced-denominator formulas, the lcm identity, the equal-depth cancellation criterion, and an explicit unbounded fixed-b countersequence to eventual B|q. Its sole new computation was the exact n=3 seed evaluation; the infinite conclusion has the congruence proof above. No completed control was replayed and no independent audit is asserted.

The existing CANONICAL_COMPANION_TRANSFER.md is unchanged. The new report is CANONICAL_DENOMINATOR_OVERLAP_REPORT.md, and the new exact seed record is denominator_overlap_seed3.json, all in work/session_20261001_astra/agent3/.
