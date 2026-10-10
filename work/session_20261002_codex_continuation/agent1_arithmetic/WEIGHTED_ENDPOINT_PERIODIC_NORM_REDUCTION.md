> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# L24 periodic response and fixed rational norm reduction

Author continuation of the fresh-gated L24 carry target, 2026-10-02. All normalization and final-gcd formulas are inherited exactly from `WEIGHTED_REGULAR_ENDPOINT_DYADIC_RATE.md` and `WEIGHTED_ENDPOINT_CARRY_TRANSFER.md`; this note does not replace actual q by a row clearer. This intermediate reduction is now completed by `WEIGHTED_REGULAR_EXACT_DYADIC_ENDPOINT_THEOREM.md`, which proves exact actualq2=n+2 on every regular degree. Its final corrected certificates supersede the initial even-start helper and previously conjectural status.

## 1. Four exponential polynomials, now degree4 and including order0

The rank-four spectral chart can be sharpened to

    rho_r(b_j)=Σ_(nu=1,2,4,8) zeta^(nu r)
                    Σ_(s=0)^4 c_(j,nu,s) binom(r,s) mod8,
    j=1,2,3,4, EVERY r≥0.                                  (1)

Here R=(Z/8)[x]/(x⁴+x+1), zeta=7+5x³, as before. The coefficients are exact and are saved in `WEIGHTED_ENDPOINT_MOMENT_POLYNOMIAL_RECEIPT.json`.

This assertion has a finite ALGEBRAIC certificate, not an extrapolated list of rho values. The exact proper rational O/E numerators from the branch receipt have denominator D^5. D's reciprocal polynomial has four distinct unit roots lambda_nu, each congruent to zeta^nu. Confluent partial fraction solving is integral because all root differences are units. The solution is

    t_r=Σ_(nu)Σ_(a=1)^5 d_(nu,a)
                    binom(r+a−1,a−1)lambda_nu^r.

Write lambda_nu=zeta^nu(1+2u_nu). Exactly modulo8,

    (1+2u)^r=1+2ru+4binom(r,2)u².

Thus each proper branch mode is an integer-valued polynomial of degree at most6. The complete three-term finite-difference formula supplies a safe degree bound10. The script constructs these polynomials symbolically by their Newton coefficients, then finds that coefficients5,…,10 are ZERO in R for all16(j,nu) combinations. Because the degree bound is proved in advance, these coefficient cancellations prove degree4 at ALL r. Its constant-order comparison is zero for all four j, so the previous order0 exception is also eliminated for the actual fixed modulo8 chart. The640 bounded rho comparisons only check normalization.

In the rising basis this becomes

    rho_r(b_j)=Σnu zeta^(nu r)Σ_(s=0)^4 a_(j,nu,s)
                                     binom(r+s,s),          (2)
    a_s=Σ_(t=s)^4 (−1)^(t−s)binom(t,s)c_t.

Both bases are integral. Multiplication with the internal binomial kernel gives the exact identity

    binom(d+e,d)binom(d+e+s,s)
       =binom(e+s,s)binom(d+e+s,d).                         (3)

This opens a finite negative-binomial summation mechanism instead of a general factorial-carry state.

## 2. The binary inverse response is UNIVERSALLY three-periodic

Put x=C omega, with C the exact binary lift, and take x0 to be the canonical0/1 lift of x modulo2. At EVERY regular m=2^odd,

    (x0_(dP),x0_(dE))=(1,1),(0,0),(1,0)
                              for d=0,1,2 modulo3.           (4)

Proof. For any d<m, the OR kernel writes the other index as M−d+s, s subset d. The resulting binary response is

    xP_d=Σ_(s subset d)[e_(M−s)e_(2m−1−d+s)
                       +o_(M−s)o_(2m−1−d+s)],
    xE_d=Σ_(s subset d)[e_(M−s)o_(2m−1−d+s)
                       +o_(M−s)e_(2m−1−d+s)].

Use the same four F16 modes as the previous correction-vector proof. For unequal frequency pairs the dependence on d is a power of the sum of two roots of x⁴+x+1. Those sums have order1 or3. Equal frequencies contribute only at d0. Fixed field evaluations at d0,1,2,3 for the two possible mmod15 values2,8 prove (4); the d0 value agrees with its three-periodic continuation, so the possible diagonal-frequency exception cancels. This is an all-degree binary identity.

## 3. Quadratic versus linear corrections

Define T to swap members and H by BEE−BPP=2H. Let N be the symmetric half-sum

    N=(TB+BT)/2,
    Nbar=[[H_o,H_e+Hbar],[H_e+Hbar,H_o]].

The diagonal of TBbar is delta0, supported at BOTH coordinates d0. Define

    ell=Nbar x0+delta0,
    k=(T omega−t)/2 mod4,
    b=Cbar kbar,
    x1=(x−x0)/2 mod2,
    E omega=(B C omega−omega)/2 mod4.

All quotients are integral. The exact principal periodic quadratic norm is

    q0=x0^T TB x0 mod8.

Expanding x=x0+2x1, while retaining the half-symmetric cross term, gives

    S2=q0+4ell^T x1−2k^T x−4b^T E omega mod8.             (5)

The reason only x modulo4 is needed here is that TB+BT=2N; a4-shift of x changes its quadratic norm by a multiple8. Substituting the full U formula gives

    U=q0−2S1−2ell^T x0+2(ell−k)^T C omega
                       −2(b+v)^T(B C omega−omega) mod8.    (6)

Equation(6) preserves every correction. In particular the integer k term cannot be replaced by only its binary residue in its first contraction.

The final left response b+v has a particularly small all-degree form:

    (b+v)_(dP)=0,
    (b+v)_(dE)=1_(d=1 or3 mod6),
    followed by adding1 at BOTH last coordinates d=M.      (7)

Proof: kbar is supported on the P member and on even d, with entry o_(m+d+1). The OR kernel gives, for odd d,

    bP_d=Σ_(s subset d−1)e_(M−s)o_(2m−d+s),
    bE_d=Σ_(s subset d−1)o_(M−s)o_(2m−d+s).

Unequal Fourier pair sums again have orders1 or3; the possible d1 correction cancels the previous v's d1 term. Fixed field tables give (7) for both mmod15 values. On even d both vanish. The last-coordinate delta from v is retained. The existing m2,8,32 full vectors and the scalar reconstruction(5)–(6) are saved in `WEIGHTED_ENDPOINT_PERIODIC_NORM_RECEIPT.json`.

## 4. The principal norm is a coefficient of one FIXED rational function

Let p_d=(1,0,1) and r_d=(1,0,0), both period3, denote the P/E components of x0. Let eta=zeta^5, and use their exact period3 Fourier coefficients p_hat_a,r_hat_a in R. Let

    F_j(Z)=Σ_(s≥0)rho_s(b_j)Z^s,

which is a fixed rational function by (2), with denominator dividing Πnu(1−zeta^nu Z)^5. The full principal norm is EXACTLY

    q0(m)=[X^(m−1)Y^(m−1)] 1/[(1−X)(1−Y)]
      Σ_(a,b=0)^2 {
        p_hat_a r_hat_b(F2+F4)(eta^a X+eta^b Y)
        +(p_hat_a p_hat_b+r_hat_a r_hat_b)
                              F3(eta^a X+eta^b Y)} mod8.   (8)

Indeed the coefficient of X^dY^e in F_j(X+Y) is binom(d+e,d)rho_(d+e)(b_j), and the two cumulative denominators impose the exact rectangle0≤d,e<m. The expression combines both off-member blocks: their rational moment starts are2 and4, while same-member terms have start3 after swapping T. No altered Gram or diagonal approximation is used.

Thus the principal TWO-INDEX factorial carry problem has become a fixed rational diagonal evaluated on the all-ones binary word m−1. The remaining terms in (6) are LINEAR contractions; (7) permits a finite negative-binomial summation through (3), with its quarter thresholds and boundary terms retained. An explicit evaluation of (8) and those linear corrections is still required to prove U=4. The actual q2=n+v2U formula and the proved q2≥n+1 remain in force.
