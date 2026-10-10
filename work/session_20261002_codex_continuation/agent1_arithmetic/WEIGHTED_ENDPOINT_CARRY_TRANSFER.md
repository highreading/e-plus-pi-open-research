> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# L24 exact finite residue transfer and spectral compression

Original arithmetic continuation, 2026-10-02. This note advances the complete regular endpoint quotient from `WEIGHTED_BRANCH_MOD8_LIFT.md` without another determinant-degree atlas. The actual center denominator always includes the final pair gcd. The all-degree theorem remains q2≥n+1 for n=4^j+1; exact q2=n+2 is still unproved.

## 1. Fresh archive and primary gate

Archive query: `automatic.*(dyadic|binomial|carry|endpoint)|finite.state.*(dyadic|endpoint|Gram)|binary.*reversal.*inverse|Granville|Rowland.*Yassawi`. Read the existing September13 `prime_power_automata_applicability.md` completely. It constructs a different slope-four rational diagonal and explicitly leaves its common-zero depth distribution open. It contains no weighted Gram endpoint scalar, reversed residue inverse or all-degree residue4 theorem.

Fresh primary queries: “Rowland Yassawi automatic congruences prime powers binomial coefficients primary paper”; “Granville binomial coefficients modulo prime powers odd factorial modulo8 paper”. Opened the full June25,2026 Rowland–Yassawi primary paper https://arxiv.org/pdf/2408.00750, with Sections1–2/Theorem3 read for scope. Also reopened Granville's primary factorial digit derivation https://www.cecm.sfu.ca/organics/papers/granville/paper/binomial/html/node3.html and node4.html. Automaticity and factorial carries are classical overlap. The particular complete endpoint three-contraction identity, its225-state transfer and the local spectral filtration below are the authored specialization. No general automaticity theorem is presented as new, and automaticity alone does not imply residue4.

## 2. Endpoint binomial weights use only two high digits

For m=2^h,h≥3 and0≤d<m,

    binom(m+d,m) = kappa_(floor(4d/m)) mod8,
    kappa=(1,5,7,3).                                      (1)

Proof: write the binomial as Π_(r=1)^d(1+m/r) in Q2. If v2 r≤h−3 the factor is1 modulo8. The only remaining r are the multiples of m/4, of which at most three occur. Their factors are5,3,5 modulo8, yielding the four successive products1,5,7,3. This proves(1) uniformly, without an exact integer-binomial table as the theorem.

The central binomial satisfies binom(2m,m)=6 modulo8 for every m=2^h,h≥1. One proof uses the odd factorial product O(t)=Π_(j≤t,j odd)j modulo8, with period8 and values1,1,1,3,3,7,7,1. The odd part of m! is Π_(a≥0)O(floor(m/2^a)); it is3 for h≥2 and1 for h1. The central binomial has depth1, and its odd unit is3 modulo4 in both cases.

The existing exact branch representation gives rho_(2m)(b1)=4 modulo8 on the two possible positive residues2m=64,256 modulo480 for odd h≥5. The h1,h3 values are checked by the same fixed branch formula. Hence the leading term L=binom(2m,m)rho_(2m)(b1) is identically0 modulo8 on the regular subfamily. This uses a fixed finite recurrence certificate for all orders, rather than extrapolation from degrees.

## 3. An evaluated225-state transfer for the first contraction

Let S1=t^T C omega, where C is the exact binary lift of the reversed residue inverse. For h≥7 write each index

    d=32D+ell, e=32E+u, 0≤ell,u<32.

The condition d OR e=m−1 separates into ell OR u=31 and D OR E=2^(h−5)−1. The two endpoint rho values only depend on the indices modulo480; the C coefficient only depends on2(m−1)−d−e modulo15. Thus the lower five digits are a fixed terminal table, while the remaining binary digits require only the two residues D,E modulo15.

Define a225-dimensional row-vector transfer over Z/8. Its state is(a,b)∈(Z/15)^2 and one digit column gives the three transitions

    (a,b) → (2a+x,2b+y) mod15,
    (x,y)∈{(0,1),(1,0),(1,1)}.                            (2)

After the first two high columns, initialize

    v0(a,b)=kappa_a kappa_b if0≤a,b<4 and a OR b=3,
             0 otherwise.                                 (3)

These two columns account for(1). The number of further high columns is h−7. For phase p=m modulo480, p32 or128, the terminal table is

    W_p(a,b)=Σ_(ell OR u=31) Σ_(s,t=0,1)
       f_(s,t)(2(p−1)−32a−32b−ell−u)
       rho_(p+32a+ell)(b_(1+s))
       rho_(p+32b+u)(b_(2+t)) mod8,                        (4)

where f_(s,t)=e ifs=t ando otherwise, with its period15. Every rho index is positive and is evaluated in1,…,480 by the proved periodic formula; its exceptional order0 is never conflated with order480. Then EXACTLY

    S1(h)=v0 T^(h−7) W_(2^h mod480) mod8.                   (5)

`weighted_endpoint_first_transfer.py` saves both terminal tables, the full225-coordinate vectors and an ENTIRE STATE closure v9=v1. Therefore the state orbit has preperiod1 and period8; every subsequent vector is certified by(2). This gives the authored all-degree result

    S1(h)=2,0,2,4 modulo8 for h=1,3,5,7 modulo8,
    for every odd h≥7.                                    (6)

The isolated earlier h1,h3,h5 inputs remain separately recorded in the previous receipt. A single independent direct first-contraction check at h7 matches4; it computes no new full center or denominator. Formula(5) and the state closure, not that check, prove(6).

## 4. A rank-four spectral chart for EVERY moment input

Work in the unramified coefficient ring

    R=(Z/8)[x]/(x^4+x+1).

The reduction is the field F16. Hensel lifting x to a primitive order15 root and taking its inverse gives

    zeta=7+5x^3 in R, zeta^15=1.

The exact coefficient receipt verifies this identity and its proper-order conditions. Each starting moment index j=1,2,3,4 has the following complete representation at every POSITIVE difference order r=ell+32a:

    rho_r(b_j)=Σ_(nu∈{1,2,4,8}) c_(j,ell,nu) zeta^(nu a),
    0≤ell<32.                                            (7)

The coefficients are in R and are stored in `WEIGHTED_ENDPOINT_SPECTRAL_RECEIPT.json`. Formula(7) is substantially smaller than retaining all480 residue values independently.

Proof beyond the finite table: the proper O,E branch rational functions have denominator D^5. D modulo2 has four distinct unit roots in F16, so it splits into four factors with pairwise unit root differences in R. Partial fraction coefficients are integral, and the coefficient of each factor power is a unit-root exponential times binom(r+s−1,s−1),1≤s≤5. Those binomials are32-periodic modulo8. A principal unit1+2v has fourth power1 modulo8. Consequently on r=ell+32a the only exponentials are the four Teichmuller modes zeta^(2^i a). The finite-difference conversion multiplies by integer-valued polynomials of degree at most4, also32-periodic, and shifts at most two orders, so it preserves the same four-mode support. The separate order0 polynomial part remains excluded in(7).

## 5. The binary inverse lift has a filtered fourteen-mode chart

For either binary sequence f=e,o, let z_r be ANY lift to R of its characteristic2 four-mode expression:

    z_r=Σ_(nu∈{1,2,4,8}) u_nu zeta^(nu r),
    z_r mod2=f_r∈F2.

Then the actual integer lift f_r∈{0,1} is EXACTLY

    f_r=z_r^4 mod8.                                       (8)

Indeed z_r=2v gives fourth power0, while z_r=1+2v gives fourth power1 modulo8. This prevents treating the binary C entries as arbitrary lifts of their four-mode residues.

Write f_r=Σ_(nu=0)^14 F_nu zeta^(nu r). Multinomial expansion of(8) proves

    F0=0,
    v2(F_nu)≥binary_weight(nu)−1, 1≤nu≤14.                 (9)

For counts c0+…+c3=4, the multinomial coefficient has depth Σ binary_weight(c_i)−1. Cyclic binary carries in the exponent Σ c_i2^i modulo15 can only reduce its positive representative's binary weight. Exponent0 requires all four distinct modes and has coefficient24, hence vanishes modulo8. This gives(9). Exact DFT receipts show the bound is sharp for both e,o: four unit frequencies, six depth1 frequencies, four depth2 frequencies. These are fixed coefficient identities valid at every index.

## 6. Remaining coupled arithmetic

The complete U is

    U=−3 S1+3 S2−S3 mod8,
    S2=t^T C B C omega, S3=t^T C B C B C omega.              (10)

The first contraction is now evaluated at ALL regular large degrees by(6). All moment factors in the longer contractions have the rank-four chart(7), and each binary inverse factor has the explicit filtration(8)–(9). The internal B binomial factors still require their ordinary factorial-unit carries modulo8. Sections7–8 further eliminate the second internal B layer by retaining the coupled-member commutator. The actual denominator theorem q2≥n+1 and the final-gcd formula q2=n+v2U are retained; no odd-content or irrationality claim follows.

## 7. New coupled-member identity removes the second binomial layer

Let T swap P/E members. The binary lift C commutes with T EXACTLY. Write the actual block, in all-P/all-E order,

    B=[[A,D],[D,A+2H]],
    H_(d,e)=(d+e+1)binom(d+e,d)rho_(d+e+1)(b2).

The equality follows from rho_r(b4)−rho_r(b2)=2(r+1)rho_(r+1)(b2). Modulo2, H is supported on EVEN d,e with disjoint binary support. Its entry there is e_(d+e+1). Let H^r reverse both indices of Hbar, and let the same symbol with a block hat mean diag(H^r,H^r).

As before E=(BC−I)/2. Work now modulo2. Boolean monomial multiplication proves

    Cbar diag(Hbar,Hbar) Cbar=diag(H^r,H^r).                (11)

Indeed Cbar has multiplication blocks M_(g_e)R and M_(g_o)R. The diagonal block of the product is M_(g_h)(M_(g_e)^2+M_(g_o)^2)R=M_(g_h)R because e_M+o_M=1; the opposite blocks cancel. This is the same Frobenius algebra as the inverse proof, not an assumption about lift symmetry.

Since [E,T]=diag(Hbar,Hbar) T Cbar modulo2, (11) gives

    Cbar [E,T]=diag(H^r,H^r) T.

Also E^T Cbar=Cbar E. The diagonal of Cbar T is the vector delta supported at BOTH last-member coordinates d=M. The paired responses satisfy tbar=T omegabar. Therefore the exact second-carry scalar is

    Q=tbar^T Cbar E² omegabar
      =(E omegabar)^T Cbar T(E omegabar)
        +omegabar^T diag(H^r,H^r) T E omegabar
      =v^T E omegabar,                                   (12)
    v=delta+T diag(H^r,H^r) omegabar.

The first equality retains the commutator term; omitting it would be false. The quadratic form in characteristic2 is its diagonal, giving the final expression.

Substitute (12) in the full geometric inverse formula. Since L=0, the COMPLETE endpoint reduces to

    U=S2−2S1−2 v^T(B C omega−omega) mod8.                  (13)

Thus ONE internal B binomial layer suffices. The previous six-index S3 contraction is unnecessary. The new left vector v is binary and is completely evaluated in Section8. `weighted_endpoint_coupled_symmetry.py` verifies (11)–(13)'s scalar consequences at the existing m2,8,32 states, retaining the complete U. No further degree or prime atlas is used.

## 8. The correction vector has period6 plus TWO boundary coordinates

For even d the vector v_d is zero. For odd d, its two-member vector has the following all-degree explicit form. Set m modulo15=p, which is2 or8 at every odd h. Define the periodic vector vper(d) by

    p2: d=1,3,5 mod6 → (0,1),(1,0),(1,1),
    p8: d=1,3,5 mod6 → (1,0),(1,1),(1,1).

Then

    v_(dP,dE)=vper(d)+(1,0)1_(d=1)+(1,1)1_(d=M) mod2.    (14)

The two indicators may coincide, as at m2; both are retained.

Proof. For odd d, the reversed H action on either response f=e,o is EXACTLY

    (H^r omega_f)_d=Σ_(s subset d−1) e_(m−1−s)f_(2m−d+s).

Use the four-mode characteristic2 representations of e,f in F16. For frequency pair q,t the subset sum is

    e_q f_t lambda^(q(m−1)+t(2m−d))
       Π_(b in support(d−1))(1+lambda^((t−q)2^b)).

For q=t the product is zero unless d=1. For q≠t it equals (1+lambda^(t−q))^(d−1), so the dependence on d is through (lambda^(−t)+lambda^(−q))^(d−1). Here the four lambda inverse modes are the roots x,x²,x⁴,x⁸ of x⁴+x+1. Their six pair sums are1 and the two roots of z²+z+1. Hence the non-diagonal sum has period3 in d; imposing odd d gives period6. Fixed evaluations at d3,5,7 for p2,p8 determine the six rows above. The diagonal-frequency term contributes exactly(1,0) after the member swap at d1. Finally delta supplies both last coordinates. This proves (14) at every regular degree.

At this intermediate state the remaining target was the TWO-INDEX binomial-carry pairing S2=(Ct)^T B(Comega). It is now completed by `WEIGHTED_REGULAR_EXACT_DYADIC_ENDPOINT_THEOREM.md`, which proves U4 and exact actualq2=n+2 for every regular degree. The initially written S1 classes6,0,6,4 are WITHDRAWN because a new even-start helper used the wrong shift; the corrected fixed-state classes are2,0,2,4 as above. All affected receipts were regenerated. Earlier inverse/full-q proofs explicitly used the correct shifts and were unaffected.
