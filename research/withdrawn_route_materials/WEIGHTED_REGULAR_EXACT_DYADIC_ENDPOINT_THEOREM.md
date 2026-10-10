> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# L24 complete author theorem: exact regular endpoint and actual dyadic denominator

2026-10-02. This completes the currently planned L24 arithmetic route. The proof is authored mathematics with exact finite algebra/state certificates; it has not been independently audited. No further extension of an archive/public-literature route is opened. This result concerns the full weighted paired center and its final endpoint gcd, not a coefficient clearer. It proves no unconditional conclusion about e+pi and no odd-prime growth statement.

## 1. Exact statement, including the primitive denominator

Let n=4^j+1,j≥1, m=(n−1)/2=2^(2j−1), k=m+1, sigma=m+v2(m!)=n−2. Let

    A(P)=integral_0^infinity e^(−t)P(1−t)dt,
    C_s=A(x^(2s))−(−1)^s,

and let q_n(y) be the primitive integer polynomial of degree n, with positive leading coefficient, satisfying

    Σ_(a=0)^n (q_n)_a C_(a+s)=0, 0≤s<n.

Use the COMPLETE rational matrix and response

    R_(i,l)=−Σ_a(q_n)_a(2(i+l+a))!+Σ_a(q_n)_a L_(i+l+a),
    L_s=4Σ_(r=0)^(s−1)(−1)^r/(2s−1−2r), L0=0,
    w=q_n(−1), v_i=(−1)^i, 0≤i,l<k,
    det(R+S w vv^T)=alpha+beta S, S=e+pi,
    alpha=det R, beta=w v^T adj(R)v.

Take ANY positive ODD D clearing alpha,beta and set

    p_center=−D alpha/g,
    q_center=|D beta|/g,
    g=gcd(D alpha,D beta),

with signs chosen so q_center>0. The theorem is

    v2(q_n(−1))=3n−2,
    v2(q_center)=n+2.                                    (1)

Equivalently, for the monic normalized polynomial P_n defined by

    q_n(2z−1)=lambda 2^n P_n(z), lambda an ODD integer,

one has

    v2(P_n(0))=2n−2,
    v2(eta0)=n,
    P_n(0)/[2^m m!]^2=4 mod8.                             (2)

Here eta0 is the divided-basis endpoint response specified below. All rational-arctan endpoint contributions are retained in R. In particular (1) is an ACTUAL reduced-denominator identity after the final gcd.

## 2. Prior all-degree normalization and the precise remaining scalar

The exact all-degree basis conversions and arctan gate are proved in `WEIGHTED_REGULAR_DYADIC_SUBFAMILY.md`; their full primitive-pair transfer is `WEIGHTED_REGULAR_ENDPOINT_DYADIC_RATE.md`. The necessary interface is recalled here.

Set z=(x²+1)/2 and b_r=A(z^r). The moments obey

    b0=b1=1,
    b_(r+1)=(r+1)(2r+1)b_r−r(r+1)b_(r−1)−r.

Every b_r is odd. Put the signed functional L(P)=A_z(P)−P(0), and the monic divided basis

    h0=1,
    h_(2d+1)=z(z²−1)^d,
    h_(2d+2)=z²(z²−1)^d,
    D_d=2^d d!, psi_(dP)=h_(2d+1)/D_d,
    psi_(dE)=h_(2d+2)/D_d.

Its signed normalized Gram G is integral and a dyadic unit for every m=2^odd. Its nonconstant complete-pair block B is also a unit. If

    omega_i=L(h_n h_i)/(D_m D_i), eta=G^−1 omega,
    P_n=h_n−Σ_(i<n)(D_m/D_i)eta_i h_i,

then P_n has integral coefficients in Z2[z], and the primitive q_n has q_n(0) odd and lambda odd. The SAME-basis arctan rational contraction has the depth needed for the full R pair. Hence, with

    gamma=k(k−1)+2Σ_(i=0)^(k−1)v2(i!),

the COMPLETE determinant pair satisfies

    v2(alpha)=gamma,
    v2(beta)=gamma+v2(w)−2sigma,
    v2(q_center)=max(0,v2(w)−2sigma).                       (3)

The preceding L24 bound proves v2(P_n(0))≥2sigma+1. Set

    U=P_n(0)/D_m²,

so U is integral and even. Its full transfer is

    v2(q_center)=n+v2(U).                                 (4)

It remains to prove U=4 modulo8, rather than assume the apparent equality from n5,17,65.

## 3. Exact residue inverse and complete coupled quotient

The integral ordinary moment branches O,E have modulo2 rational functions

    Ebar=(1+u²+u³)/(1+u+u⁴),
    Obar=(1+u+u³)/(1+u+u⁴).

Write e_r,o_r for their residues and a_r=e_r+o_r. These are15-periodic at all indices; a_(m−1)=1 for every m=2^odd. For the Frobenius matrices

    H_f(d,l)=binom(d+l,d)f_(d+l) mod2,

Bbar has blocks[[H_e,H_o],[H_o,H_e]]. Boolean monomial Frobenius algebra proves

    Bbar^−1=R Bbar R,

where R reverses BOTH member indices d→m−1−d. Let C be the resulting exact0/1 binary lift. C commutes with the member swap T EXACTLY. With Ecarry=(BC−I)/2,

    B^−1=C−2C Ecarry+4C Ecarry² mod8.

The complete scalar formula is

    U=−t^T C omega+2t^T C Ecarry omega
                         −4tbar^T Cbar Ecarry² omegabar mod8. (5)

The leading term is identically0. The constant-coordinate coupling is zero modulo8 by the preceding all-degree eta0 bound, and the multiplying factor1−A_z((1−z²)^m) equals1 modulo8. Those two facts justify (5); neither is silently discarded.

Retain the ACTUAL member difference BEE−BPP=2H. The commutator identity gives a binary v such that

    tbar^T Cbar Ecarry² omegabar=v^T Ecarry omegabar.

The proof and complete formula are in `WEIGHTED_ENDPOINT_CARRY_TRANSFER.md` §§7–8. This reduces U to one internal binomial layer.

## 4. Exact four-mode polynomial moments and three-periodic response

Work in R8=(Z/8)[x]/(x⁴+x+1). It is unramified of rank4, and zeta=7+5x³ has exact order15. Finite algebraic partial fractions prove at EVERY r≥0 and j1,2,3,4

    rho_r(b_j)=Delta_2^r b_j/(2^r r!)
       =Σ_(nu=1,2,4,8) zeta^(nu r)
                       Σ_(s=0)^4 c_(j,nu,s)binom(r,s).       (6)

The integer-valued degree4 statement follows by first proving a safe degree10 representation from D^5 partial fractions, then certifying that coefficients5,…,10 vanish IDENTICALLY in R8. Thus a finite coefficient calculation proves the assertion at all orders. The actual order0 defect is zero in all four branches. All exact coefficients are in `WEIGHTED_ENDPOINT_MOMENT_POLYNOMIAL_RECEIPT.json`.

The canonical binary response x0 of x=C omega is UNIVERSALLY

    (x0_(dP),x0_(dE))=(1,1),(0,0),(1,0), d=0,1,2 mod3.    (7)

The subset/F16 proof uses sums of distinct roots of x⁴+x+1; those sums have orders1 or3. The possible exceptional d0 term cancels. Put

    N=(TB+BT)/2, ell=Nbar x0+delta0,
    k=(T omega−t)/2 mod4, b=Cbar kbar,
    x1=(x−x0)/2 mod2,
    q0=x0^T TB x0.

Expanding the full quadratic form and retaining its half-symmetric cross term gives

    U=q0−2S1−2ell^T x0+2(ell−k)^T C omega
                 −2(b+v)^T(B C omega−omega) mod8,           (8)
    S1=t^T C omega.

The integer k correction is kept modulo4. The full binary last response is

    (b+v)_P=0, (b+v)_E=1_(d=1 or3 mod6),
    then add1 at BOTH last coordinates d=m−1 modulo2.     (9)

An additive integer lift of (9) may be used: any2-shift of that lift changes its term in (8) by a multiple8 because BC omega−omega is even. All these identities are proved in `WEIGHTED_ENDPOINT_PERIODIC_NORM_REDUCTION.md` and checked at the existing states, rather than inferred from them.

## 5. The principal norm has an exactly closed rational-Cartier state

Let p_d=(1,0,1), r_d=(1,0,0) have period3, eta=zeta^5, with their period3 Fourier coefficients p_hat,r_hat. Write F_j(Z)=Σ_s rho_s(b_j)Z^s. Then q0 is the exact coefficient of the FIXED rational function

    [X^(m−1)Y^(m−1)] 1/[(1−X)(1−Y)]
      Σ_(a,b=0)^2 {
        p_hat_a r_hat_b(F2+F4)(eta^a X+eta^b Y)
        +(p_hat_a p_hat_b+r_hat_a r_hat_b)
                                  F3(eta^a X+eta^b Y)}.   (10)

Equation(6) decomposes each F_j into four conjugate single-root poles of order at most5. Taking the unramified trace reduces (10) to SIX unordered(a,b) rational terms for the nu1 root. Each has

    Q=(1−X)(1−Y)(1−zeta(eta^a X+eta^b Y))^5,
    F=N/Q=P/Q^4, P=N Q^3.

The numerator box degree is at most24 in each variable. If sigma denotes the unramified Frobenius, then

    Q^8= sigma(Q)(X²,Y²)^4 mod8.

Indeed Q²−sigma(Q)(X²,Y²) is2-divisible, and its fourth-power expansion has all correction terms8-divisible. Therefore the EXACT one-digit transition on the all-ones word m−1 is

    P_next=Lambda_(1,1)(P Q^4),
    Q_next=sigma(Q),                                      (11)

with the degree box preserved. The four denominator phases are explicit zeta→zeta^(2^phase), eta→eta^(2^phase). Output is the trace of the constant numerator; trace(a0+a1x+a2x²+a3x³)=4a0−3a3 modulo8.

`weighted_endpoint_rational_norm_machine.py` saves every coefficient of all six polynomial states and certifies ENTIRE STATE equality, including the phase, at h7=h3. Hence the state has preperiod3 and period4. It follows at ALL odd h≥3 that

    q0=6 if h=1 mod4,
    q0=4 if h=3 mod4.                                     (12)

The independently retained h1,h3,h5 principal norms are2,4,6. This is a finite-state proof of (12), not a scalar pattern guessed from degrees.

## 6. The two linear terms require only finite quarter-residue transfers

At m=2^h,h≥3,

    binom(m+d,m)=kappa_(floor(4d/m)) mod8,
    kappa=(1,5,7,3), 0≤d<m.                              (13)

All factors1+m/r with depth at least3 are1 modulo8; the only remaining r are the first three multiples of m/4, with successive factors5,3,5. This proves (13).

The vector ell is a30-periodic binary vector plus its canonical d0 adjustment. Its F16 proof follows from the explicit subset sum for even d

    (Hbar T x0)_d=Σ_(q=1,2,4,8)Σ_(a=0)^2
       e_hat_q f_hat_a zeta^(q(d+1))
                          (1+zeta^q eta^a)^(m−d−2).

Every1+zeta^q eta^a is nonzero in F16. Thus the expression depends only on dmod15 and the even/odd condition, with mmod15=2 or8. It supplies the two complete period30 tables; delta0 is converted to its correct integer signs1−2ellper(0), not added as though XOR were ordinary addition.

The actual k has only the P member:

    k_P=(d+1)binom(m+d+1,m)rho_(m+d+1)(b1), k_E=0 mod4.

The quarter crossing at d+1 has zero contribution modulo4 because d+1 is then divisible by m/4. Hence k is a480-periodic function within each quarter, with its phase and kappa factor recorded.

For the last term in (8), use the additive lift w=b+v of (9). Its E-periodic part has

    2wper_d=a_d(1−(−1)^d), a=(1,1,0), period3.

Put rho in the rising integer-valued basis. The coefficients of orders3,4 are4-divisible, and orders1,2 are2-divisible. The exact identity

    binom(d+e,d)binom(d+e+s,s)
       =binom(e+s,s)binom(d+e+s,d)

reduces its row contraction to the finite negative-binomial sum

    K_r(z)=Σ_(d=0)^(m−1)binom(d+r,d)z^d
      =(1−z)^−(r+1)[1−z^m Σ_(a=0)^r
                              binom(m+a−1,a)(1−z)^a].     (14)

The arguments are z=plus/minus zeta^nu eta^a;1−z is a unit because nu is1,2,4,8. Thus (14) is legal in R8. Below m the tail coefficients only survive at a0,m/4,m/2,3m/4, with values1,4,2,4 modulo8. The coefficient at a=m is3 and the next is0 modulo8. Quarter crossings from r=e+s carry binom(a m/4,s), which kills them at the required precision for h≥7. Therefore the PERIODIC row2wper^T B is a480-periodic function in each quarter, with no hidden shifted-boundary term. The member q_s3,q_s4 contributions vanish because K_r(z)−K_r(−z) is even.

The BOTH-last-coordinate addition from w is retained. Its row2w_last^T B is supported only at e0 and e=m/2 modulo8:

    R0_u=2[rho_(m−1)(b_(2+u))+rho_(m−1)(b_(3+u))],
    Rhalf_u=4[rho_(3m/2−1)(b_(2+u))+rho_(3m/2−1)(b_(3+u))].

The required point responses C omega at those two indices are finite one/two-term sums because their binary support forces the other OR index to m−1 or to m/2−1,m−1. These exact point responses and both boundary rows are saved. The half-minus-one residue is0 or3 modulo15; it is not the quarter-minus-one residue.

Now both linear pairings contain only ONE binary C kernel. Split indices as d=32D+ell,e=32E+u. Their OR condition gives ell OR u=31 and D OR E=2^(h−5)−1. The terminal tables depend on D,Emod15, lower five digits, the fixed phase and the LEFT quarter. The common225-coordinate transfer is

    (a,b)→(2a+x,2b+y) mod15,
    (x,y)=(0,1),(1,0),(1,1).

Use FOUR initial vectors indexed by the left quarter q:

    Vq(a,b)=kappa_b if a=q,0≤b<4,q OR b=3,
             0 otherwise.

The number of bulk steps is h−7. `weighted_endpoint_complete_linear_transfer.py` saves all four complete vector orbits, all terminal/quarter tables, ell/k signs, point responses and constants. ENTIRE STATE closure is certified at step11=step3: preperiod3, period8. The last constant2w^T omega is4 or6 in its two phases; for h7,9 it is separately evaluated, and equals the same phase value. Its uniform phase reduction for odd h≥11 follows from the480 period and m modulo3840, not an asymptotic approximation.

## 7. Complete residue table and all-degree conclusion

The corrected first-contraction theorem is

    S1=2,0,2,4 for h=1,3,5,7 mod8, odd h≥7.              (15)

Combining the norm closure, all four linear-transfer states, BOTH boundary rows, ell's integer d0 signs, k modulo4 and the full last constant yields

| h | S1 | q0 | left base | right base | 2w^T omega | U mod8 |
|---:|---:|---:|---:|---:|---:|---:|
|7|4|4|6|0|4|4|
|9|2|6|1|2|6|4|
|11|0|4|0|4|4|4|
|13|2|6|3|6|6|4|
|15|4|4|6|0|4|4|
|17|2|6|1|2|6|4|

The row entries are finite TRANSFER outputs. They are not fresh complete Gram determinant nodes. Steps4,6,8,10 represent all odd h≥11 by the exact full-state period8. Steps0,2 cover h7,9. The previously retained complete h1,h3,h5 residues are4 from `WEIGHTED_ENDPOINT_BINARY_INVERSE_RECEIPT.json`. Therefore U=4 modulo8 for EVERY positive odd h.

A direct new representation check at h7 verifies all256 coefficients of EACH linear row against the actual normalized B/t/omega inputs and both point responses. It computes no new full center determinant. This check is a normalization receipt, while the identities and state closures provide the all-degree proof.

Now v2U=2. Since sigma=n−2,

    v2P_n(0)=2sigma+2=2n−2,
    v2eta0=sigma+2=n,
    v2q_n(−1)=n+v2P_n(0)=3n−2.

Finally (3) gives v2alpha=gamma and v2beta=gamma+n+2. Their full cleared endpoint gcd has dyadic depth gamma. Thus the ACTUAL reduced q has depth n+2, proving (1). No odd denominator factor is estimated or assumed to survive.

## 8. Correction record, scope and reproducibility

The initially written S1 classes6,0,6,4 are WITHDRAWN. A helper in the NEW spectral/linear-terminal scripts used(start−1)//2 at even moment starts; the correct branch coordinate is start//2. The original L23/L24 denominator theorem, binary inverse and coupled-member identities explicitly used the correct c1,c2 and were unaffected. All affected spectral, polynomial and transfer receipts were regenerated. The correct classes are (15). A second point-normalization check corrected the half-minus-one residue to0/3; all final full-row and point checks pass. No withdrawn residue is used in this theorem.

Run these exact scripts in this directory in order:

1. `weighted_branch_mod8_lift.py`
2. `weighted_endpoint_binary_inverse.py`
3. `weighted_endpoint_first_transfer.py`
4. `weighted_endpoint_spectral.py`
5. `weighted_endpoint_moment_polynomial.py`
6. `weighted_endpoint_coupled_symmetry.py`
7. `weighted_endpoint_periodic_norm.py`
8. `weighted_endpoint_rational_norm_machine.py --max-depth 32`
9. `weighted_endpoint_complete_linear_transfer.py`

They write only this agent directory. The full orbit states, fixed polynomial identities and coefficients are retained in the correspondingly named JSON receipts. Numerical approximation is not used. Earlier files saying exact q2=n+2 remained conjectural describe intermediate states; this file supersedes that limitation for the regular subfamily only.

No all-n theorem, odd-content growth, total q upper bound, shrinking primitive form or irrationality conclusion is inferred. The archive/public overlap of finite-state arithmetic and rational Cartier extraction is explicitly recorded in the L24 novelty gate. This closes the currently planned route. The agent is ready for the root-directed Genesis stage and will not open another old-route extension.
