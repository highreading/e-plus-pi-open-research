> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Coupled h1 numerator roots and the necessary Gram carry correction

Author result L18,2026-10-02. The complete b4/b5 h1 polynomials are retained. This proves the coupled moment model's exact isometry and common-content formula, then a concrete obstruction to transferring that isometry to the ACTUAL normalized Gram center. The uncorrected model does not agree with the Gram scalar even modulo p throughout the boundary cell. A necessary carry compensation restores the first digit and removes the isometry. Its agreement modulo p does not give a higher-precision bridge.

The archive/current-primary gate is recorded in TARGET_LEDGER.md. Standard Mahler and local root methods are overlapping background, as is root's separately authored gauged pullback M15; no root endpoint or correction target is repeated here. No new prime atlas is run.

## 1. Keep all coupled responses

Fix an odd p,chi=(-1|p), and use the interpolated integer sequences S,D,T from L16/L17. They are functions on Z_p. S,D and their integral shifts are1-Lipschitz; T is p-Lipschitz with the proved all-depth carry. Put

    C(x)=D(x), U(x)=S(x), W(x)=S(x)+S(x−1)/2,
    Lambda(x)=−T(x)−chi D(x).

The exact complete polynomial expressions from L13 therefore yield the following COUPLED moment functions:

    Phi4(x)=−85T(x)+(156−194D(x))S(x)
              +(163−97D(x))S(x−1)+(12−85chi)D(x)−78,

    Phi5(x)=−93T(x)+(24D(x)+90)S(x)
              +(155−31D(x))S(x−1)−(148+93chi)D(x)−28,       (1)

    Delta4(x)=4(2S(x)+S(x−1)−1),
    Delta5(x)=48(1−S(x)).                                  (2)

No C response has been frozen. At the actual prime-index reference x=p−1 the known normalized h1 quotient has nu4=4Phi4(p−1) or nu5=384Phi5(p−1) modulo p, and its residual contact determinant is Delta4/Delta5 modulo p. These reference statements do not identify the functions at higher precision with the actual Gram center.

## 2. Exact isometry of the coupled model

Set a4=85,a5=93. For every depth k>=1,

    Phi_b(x+p^k t)−Phi_b(x)
       =a_b chi p^(k−1)t D(x) mod p^k.                    (3)

Indeed every term in(1) except its T term is a polynomial in1-Lipschitz integral companions, so its change is0 mod p^k. The T carry supplies(3). Coupled changes in C,S,S(x−1) are retained and cannot cancel this leading digit.

If p does not divide a_b and D(r) is a unit, then on r+pZ_p,

    v_p(Phi_b(x)−Phi_b(y))=v_p(x−y)−1.                    (4)

Thus z↦Phi_b(r+pz) is an isometric bijection Z_p→Z_p. Every target value, including0, has a unique preimage zeta in this cell. The proof of bijectivity uses the exact residue-level isometry and equal finite cardinalities, then compactness; it does not assume that a1-Lipschitz map is automatically surjective.

The determinant responses are slower:

    v_p(Delta_b(x)−Delta_b(y))>=v_p(x−y).                  (5)

This yields a complete common-content classification FOR THIS COUPLED MODEL. Let zeta be its unique Phi_b zero and c=v_p(Delta_b(zeta)), allowing c=infinity. For x!=zeta, put v=v_p(Phi_b(x)). Equations(4),(5) give

    v_p(x−zeta)=v+1,
    Delta_b(x)=Delta_b(zeta) mod p^(v+1),
    min(v_p(Phi_b(x)),v_p(Delta_b(x)))=min(v,c).            (6)

The same minimum formula at x=zeta is understood with v=infinity. Shared content is uniformly bounded on the cell precisely when Delta_b(zeta) is nonzero. Arbitrarily deep shared content occurs precisely when the two MODEL functions have a common p-adic zero. If Delta_b(r) is a unit, c=0 at once. If it vanishes, a lifted Phi root modulo p^k determines Delta(zeta) modulo p^(k+1), rather than merely modulo p^k.

One new bounded example illustrates(6), without making a claim about primes. At p11,b5 on the cell0+11Z_11, D0=1 and Delta5=0 mod11. The model root representative77 satisfies Phi5(77)=0 mod11 and Delta5(77)=88 mod121. Consequently Delta5(zeta) has valuation exactly1. Formula(6) proves that the model's simultaneous content is capped at ONE digit throughout this entire cell. Root representatives through three precisions,77,803,10120, are saved as supporting evidence; only the first representative and the exact Lipschitz theorem are needed for the cap.

## 3. Why this isometry does not transfer to the actual Gram boundary

Let n be a normal actual Gram index, u=n+1,k=v_p(u)>=1, and assume the endpoint digits are units. In the established all-depth h1 chart, define the genuine normalized quantities

    N_G(n)=V_Gram(n)/(u² P_n),
    D_G(n)=D_Gram(n)/(u² P_n²).

They are p-integral at the boundary. The previous theorem states

    N_G(n)=nu_b(p) mod p,
    D_G(n)=340 (b4) or35712 (b5) mod p,                   (7)

throughout n=−1 mod p, including every depth and the first-depth endpoint carry. The residue nu_b(p) is the SAME scalar obtained from Phi_b(p−1) in§1. This is an actual normalized Gram statement, with the full correction already inside V_Gram.

On the other hand, if C_p=D_(p−1) is a unit and p does not divide a_b, then(3) makes

    Phi_b(n+p)−Phi_b(n)=a_b chi C_p mod p

a unit on that boundary cell. Choose two neighboring normal indices with both k=1 and unit endpoint digits; for a prime whose endpoint digits are all units this is immediate. Equation(7) keeps the actual first digit constant, whereas the coupled Phi first digit changes. Therefore

    N_G(n) != scale_b Phi_b(n) as a boundary-cell identity,
    scale4=4,scale5=384.                                  (8)

This obstruction is structural and uses the all-depth chart, not finite-depth extrapolation. The integer index p−1 in the finite reverse-factorial representation is a reference length for the local moment, not permission to replace it with the arbitrary actual Gram depth index n. The missing carry is substantive.

In particular, the unique model root and formula(6) cannot be treated as roots or shared-content bounds for the actual normalized Gram scalar and its contact determinant. The candidate isometry fails before such an inference.

## 4. The exact necessary carry compensation

For each residue cell r+pZ_p put

    q_r(x)=(x−r)/p in Z_p,
    Ttilde_r(x)=T(x)+chi q_r(x)D(x).                      (9)

This is1-Lipschitz in x on that cell. For delta=p^k t,

    q_r(x+delta)D(x+delta)−q_r(x)D(x)
      =(delta/p)D(x)+q_r(x+delta)(D(x+delta)−D(x)).

The second term is0 mod p^k, and the first exactly cancels T's one-digit carry. Therefore

    Ttilde_r(x+delta)−Ttilde_r(x)=0 mod p^k               (10)

at EVERY depth, not only modulo p. Define Phitilde_b,r by replacing T in(1) with Ttilde_r. All its terms are then1-Lipschitz. The exact uncorrected isometry has disappeared through a coupled factorial correction, rather than through freezing C.

At r=p−1 and x=n in the actual boundary,

    Ttilde_(p−1)(n)=T_(p−1) mod p,
    S(n)=S_(p−1),D(n)=C_p,S(n−1)=S_(p−2) mod p.

Thus the compensated model now has the CORRECT first digit:

    scale_b Phitilde_b,p−1(n)=N_G(n) mod p.               (11)

The contact model Delta_b is also constant modulo p on this cell and equals the known reference determinant. If both compensated numerator and contact determinant vanish modulo p, the entire cell shares this first digit; no simple isometry forces a unique next digit. Higher-content classification now requires the actual higher-precision Gram bridge. A different correction could agree modulo p as well; equation(11) alone does not make(9) the full higher-precision response.

## 5. Exact evidence that the first correction is insufficient at p²

The script h1_coupled_scalar_bridge.py evaluates only TWO new normal b5,m1 Gram states at p11, using the exact contact/endpoint definitions modulo11^4. This is an exact finite calculation, not a scan. Dividing their forced u² content and retaining the full V correction gives:

| n | actual N_G mod121 | uncorrected384Phi5 mod121 | compensated384Phitilde5 mod121 | actual detN mod121 | coupled Delta5 mod121 |
|---:|---:|---:|---:|---:|---:|
|32|85|14|63|39|72|
|43|96|94|96|50|105|

Both actual N_G first digits are8 mod11. The uncorrected model first digits differ; both compensated first digits are8, as proved. At n32 the compensated scalar differs from the actual value by22 mod121, disproving a universal p² bridge with this compensation alone. The contact determinant also differs at p² in both rows. Equality of the compensated scalar at n43 is one finite coincidence and supplies no further theorem.

Actual D_G residues modulo121 are116 and72; both are6 mod11, the correct35712 residue. The actual D,V valuations are2 at these indices. The existing COMPLETE beta comparison therefore gives the final reduced q valuations4 and6, respectively, since2v_11(32!)=4 and2v_11(43!)=6. These q conclusions use the established full beta/kappa and evaluated-gcd theorem, not a model-root content calculation; the script itself does not calculate a new complete q.

H1_COUPLED_SCALAR_BRIDGE_RECEIPT.json saves all normalized scalar/determinant values, the model root and12 compensation checks through three depths. No old atlas was rerun, and no independent audit is undertaken.

## 6. Exact remaining arithmetic target

The authored outcome is a negative transfer theorem plus the necessary compensator: the full coupled h1 scalar has an auxiliary isometry, but the ACTUAL normalized Gram chart cancels its first digit, and this specific first correction still fails at p². Consequently a general common-zero lifting theorem for the actual scalar and contact determinant is not yet established. It requires an exact higher-order boundary response, including the Frobenius endpoint quotient and the finite backward-factorial sources. The already proved metric-kernel elimination handles first-order sources; it does not authorize omitting the next ones.

No extra final-q gain, prime distribution, shrinking primitive family or irrationality statement follows from the coupled model's root theorem.
