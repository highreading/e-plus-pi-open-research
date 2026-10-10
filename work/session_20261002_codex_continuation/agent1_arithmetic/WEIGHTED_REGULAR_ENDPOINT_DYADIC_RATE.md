> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# L24: a surviving linear dyadic rate in the FULL regular weighted denominator

Author theorem, 2026-10-02. This is the fresh-gated original endpoint continuation of L23. Definitions and the simultaneous Gram/atan normalization are in `WEIGHTED_REGULAR_DYADIC_SUBFAMILY.md`. Selector's shorter-stack factorial content and root's huge-shift obstructions are different targets and are not audited here.

For EVERY n=4^j+1, j≥1, the actual weighted coefficient-one center has

    v2(q_center)≥n+1.                         (1)

The final evaluated alpha/beta gcd is included through L23's proved identity. This is neither a raw coefficient lattice bound nor a theorem about odd content. The stronger bounded-state pattern v2(q_center)=n+2 remains conjectural.

## 1. Exact notation and the final arithmetic interface

Put m=(n−1)/2=2^(2j−1), k=m+1, z=(x²+1)/2, sigma=m+v2(m!)=2m−1. Let A_z be the positive real Gamma functional A_z(z^r)=b_r, and let

    L(P)=A_z(P)−P(0).

The monic normalized orthogonal polynomial P_n has L(P_n z^s)=0 for0≤s<n. L23 proves its actual primitive integer ray obeys

    q_n(2z−1)=lambda 2^nP_n(z), lambda odd,
    q_n(0) odd,
    v2 V_s≥n+sigma+1 for all s≥0.

Consequently, for the FULL determinant det(R+S q_n(−1)vv^T)=alpha+betaS,

    v2(q_center)=v2q_n(−1)−2sigma
                =n+v2P_n(0)−2sigma.         (2)

Its alpha valuation is gamma=k(k−1)+2Σ_(i<k)v2(i!), and its beta valuation is gamma+v2q_n(−1)−2sigma. Equation(2) follows AFTER the complete final gcd and odd denominator clearing; neither alpha content nor a row scale is being called q.

Use the common monic basis

    h_0=1,
    h_(2d+1)=z(z²−1)^d,
    h_(2d+2)=z²(z²−1)^d,
    D_0=1, D_(2d+1)=D_(2d+2)=D_d=2^d d!.

Here the repeated symbol D_d in the last formula labels the factorial scale of a pair, not the degree index. Write psi_i=h_i/D_i. The signed normalized Gram G_ij=L(psi_i psi_j),0≤i,j<n, is a dyadic unit on this entire family. The mixed vector

    omega_i=L(h_n h_i)/(D_mD_i)

is integral. Put eta=G^−1 omega. The exact polynomial expansion is

    P_n=h_n−Σ_(i<n)(D_m/D_i)eta_i h_i,
    P_n(0)=−D_m eta_0.                       (3)

L23 alone proves v2P_n(0)≥sigma and q2≥2. The additional endpoint argument below proves v2P_n(0)≥2sigma+1, equivalent to(1).

## 2. One exact shifted-Gram Schur scalar contains all endpoint content

The standard orthogonal constant-term determinant identity gives

    P_n(0)=(−1)^n det(b_(i+j+1))_(i,j<n)
                        /det(mu_(i+j))_(i,j<n),

where mu_0=0,mu_r=b_r for r≥1. This can also be proved by expanding the final polynomial row of the defining orthogonal determinant at0; no novel general identity is claimed here.

Apply the SAME monic basis and row scales to its numerator:

    G^+_ij=A_z(z h_i h_j)/(D_iD_j)∈Z_2.

The two determinants have the same exact row-scale square, so

    v2P_n(0)=v2 detG^+.                     (4)

To describe its residue, let e_d,o_d be the coefficients of

    Ebar=(1+u²+u³)/(1+u+u⁴),
    Obar=(1+u+u³)/(1+u+u⁴),
    a_d=e_d+o_d.

These are the exact L23 Taylor/difference residues, not guessed moment residues. On complete pairs, the nonconstant shifted Gram reduces to

    Bbar=[ H_O H_E ]
         [ H_E H_O ],

with H_E(d,e)=binom(d+e,d)e_(d+e) and similarly H_O. The pair sum gives its determinant det(H_A)^2, H_A=H_E+H_O. It is a unit by L23's power-of-two anti-triangular argument. Thus the actual nonconstant block B=(G^+_ij)_(1≤i,j<n) is2-integrally invertible.

Replace the constant basis vector by c=1+z²; its normalized row uses D_0=D_2=1. Modulo2 it is orthogonal to EVERY nonconstant basis member in G^+: adding2 to the starting moment preserves parity and the Taylor coefficient residue. Its norm is0 modulo2. Hence G^+ has exactly one radical direction modulo2, represented by c.

The FULL all-depth scalar is therefore

    s=A_z(z c²)−b^T B^−1 b,
    b_i=A_z(z c psi_i),1≤i<n.               (5)

Both b and the first term are even, and detB is a unit. The exact determinant factorization yields

    v2P_n(0)=v2s,
    v2(q_center)=v2s−n+4.                  (6)

The positive real Gamma form gives B positive definite and s>0, so it is not zero as a rational scalar. This statement does not prescribe its dyadic depth. Formula(5) is a compact normalized lifting target with all endpoint content retained.

## 3. Orthogonality doubles the endpoint depth

Let

    f(z)=(1−z²)^m, deg f=2m=n−1, f(0)=1.

Orthogonality to f gives EXACTLY

    P_n(0)=A_z(P_n f).                      (7)

The analytic moment difference theorem is

    v2 Delta_2^d b_r≥d+v2(d!),
    Delta_2^d b_r/(2^d d!)=e_d or o_d mod2

according as r is even or odd. In particular

    A_z(h_i f)=(−1)^m Delta_2^(m+d_i)b_(a_i)

for i≥1, with a_i=1 on odd members and2 on even members. For i=0 the same formula uses d_i=0,a_i=0. Also

    A_z(h_n f)=(−1)^m Delta_2^(2m)b_1.

For i<n, d_i≤m−1. Because m is a power of2, binom(m+d_i,m) is odd. Thus

    v2 A_z(h_i f)≥sigma+v2(D_i).

The coefficient(D_m/D_i)eta_i in(3) has depth at least sigma−v2(D_i). Every lower-degree term in(7) therefore has depth at least2sigma. The leading term has depth

    v2 Delta_2^(2m)b_1≥2m+v2((2m)!)
                              =2sigma+1.

This already proves v2P_n(0)≥2sigma, with no residue argument.

It is helpful to separate the constant lower term. Since its coefficient in(3) is P_n(0), equation(7) becomes

    P_n(0)[1−A_z(f)]
       =A_z(h_n f)
        −Σ_(1≤i<n)(D_m/D_i)eta_i A_z(h_i f). (8)

A_z(f) has depth at least sigma, so the bracket is a unit. Division by D_m² is exact over Z_2 on the right of(8). The leading term reduces to0 because binom(2m,m) is even.

## 4. The full lower residue also vanishes

We now calculate the remaining normalized residue in(8), retaining the coupled eta vector rather than replacing it with raw moment content.

First eta_0=0 modulo2. Indeed the signed Gram splits off the unit vector1+z². The mixed response to that vector is omega_0+omega_2=o_m+o_m=0 modulo2. The coefficient of the original constant vector equals the coefficient of this replacement, so the conclusion follows. Consequently the complete pair coordinates eta_P,eta_E satisfy modulo2

    B_E eta_rest=omega_rest,
    B_E=[ H_E H_O ]
        [ H_O H_E ].

Since binom(m+d,m) is odd for0≤d<m, their responses are

    omega_P(d)=e_(m+d), omega_E(d)=o_(m+d).

The rational quantity

    (D_m/D_i) A_z(h_i f)/D_m²

reduces to o_(m+d) on P members and e_(m+d) on E members. Therefore the lower sum in(8), divided by D_m², reduces precisely to

    omega_rest^T B_E^−1 T omega_rest,        (9)

where T swaps the two complete pair coordinate blocks.

For clarity, compute this inverse algebra explicitly. H_A=H_E+H_O is an alternating invertible matrix: its diagonal vanishes because a_0=0 and binom(2d,d) is even for d≥1. Set J=H_A^−1 and K=J H_E J. The pair-sum congruence gives

    B_E^−1=[ K   J+K ]
             [ J+K  K ].

The inverse of an alternating invertible form is alternating, so J has zero diagonal. H_E has just one nonzero diagonal element, at d=0, because every other binom(2d,d) is even. Hence

    diag(K)_d=J_(d,0).

Over F_2, all off-diagonal terms in a symmetric quadratic expression cancel. Thus(9) equals

    Σ_d J_(d,0)[e_(m+d)+o_(m+d)]
       =Σ_d J_(0,d)a_(m+d).                 (10)

The anti-triangular H_A has unit anti-diagonal and zero entries when d+e≥m. Its last row is exactly the first coordinate row. Therefore the FIRST row of J is exactly the last coordinate row. Expression(10) is consequently

    a_(2m−1).

Write m=2^h with h odd. Then2m=2^(h+1), and h+1 is even. The fixed period15 coefficient identity from L23 gives a_(2m−1)=0. Both the leading term and the COMPLETE coupled lower sum of(8) vanish modulo2 after division by D_m². Since the bracket of(8) is a unit,

    v2P_n(0)≥2sigma+1.                     (11)

Equations(2),(11) prove the FULL actual denominator bound v2(q_center)≥n+1. The proof uses no unproved valuation pattern and no parent finite determinant reconstruction.

## 5. Exact values remain a separate higher-digit question

The all-degree result(11) is one bit below the bounded pattern

    v2P_n(0)=2sigma+2,
    v2q_n(−1)=3n−2,
    v2(q_center)=n+2.                       (12)

NEW exact moment states n5,n17,n65 give constant depths8,32,128 and actualq2 depths7,19,67 through the PROVED complete-pair identity. These agree with(12), but(12) remains conjectural. The n65 receipt is `WEIGHTED_REGULAR_ENDPOINT_N65_PROBE.json`; it computes the full rational monic moment state, not an unnormalized coefficient depth.

One more depth of the normalized coupled expression(8), or a square-class identity for the exact Schur scalar(5), would settle or refute(12). Neither is supplied by the residue recurrence alone. No large odd-content conclusion, shrinking primitive-form conclusion or irrationality claim follows from this dyadic result.

## 6. Archive and primary-paper gate

The L24 query/URLs are recorded verbatim in TARGET_LEDGER.md. The archive search for weighted endpoint/dyadic Christoffel and signed Gamma constant-term results returned no match. Fresh primary searches included current2026 Hankel/Christoffel and quadratic Laguerre terms. Full Krattenthaler https://arxiv.org/pdf/2101.04225v5 was opened: Theorem1 and the singular-case discussion give the established general shifted-Hankel/orthogonal-value framework. The requested current2026 primary article https://www.sciencedirect.com/science/article/abs/pii/S0196885826000230 could not be opened and supplies no theorem here.

The classical constant-term determinant formula is overlap. The new author arithmetic is the explicit unique normalized radical, the doubled depth by orthogonality against(1−z²)^m, and the coupled Gram-inverse residue cancellation at a_(2m−1), followed by the actual final-q bound(1).

## 7. Integral multiplication operator for the higher-digit target

The common divided basis gives an EXACT multiplication law:

    z psi_0=psi_1,
    z psi_(2d+1)=psi_(2d+2),
    z psi_(2d+2)=psi_(2d+1)+2(d+1)psi_(2d+3).

Thus multiplication by z preserves the infinite integral lattice generated by psi_i. In the first n states its uncorrected matrix Z_n has these entries, with the last out-of-range term removed. Its characteristic polynomial is h_n(z)=z(z²−1)^m. Orthogonal projection of psi_n is the EXACT vector eta in(3), so the actual finite multiplication matrix is

    J_n=Z_n+2m eta e_last^T.                (13)

It is integral and selfadjoint for G, since L(zUV)=L(UzV). Its characteristic polynomial is P_n: over Q_2 these states form the polynomial quotient by P_n, with orthogonal reduction at the one degree-n boundary. In particular

    det J_n=D_m eta_0=−P_n(0).

Expansion of the only possible first-row entry,2m eta_0, has complementary determinant2^(m−1)(m−1)!, giving the full product D_m eta_0. No content is discarded.

The zero eigenvector of Z_n is r_0=1, r_(2d+1)=0, r_(2d+2)=(−1)^(d+1)D_d. As a polynomial it is f(z)=(1−z²)^m. Also f(Z_n)=r e_0^T: it annihilates every complete pair block and maps the constant state to r. These identities give a rank-one perturbation approach to the next digit.

On the current power-of-two family, reduction of(13) yields P_n(z)=z(z+1)^(2m)=z+z^n mod2. This residue is proved ONLY on this subfamily through the integral matrix; it is not the false general-all-n pattern encountered during L23. There is a unique simple2-adic root near0, and every other root is a dyadic unit. Thus v2P_n(0) equals that root's depth. Formula(12) is equivalently one more digit of its normalized depth; this operator identity does not assert that unproved digit.
