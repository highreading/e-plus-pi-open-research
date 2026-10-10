> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete compact diagonalization and exact rectangular content indices

Original author reduction: Agent 2, 2026-10-02. Fresh archive/primary gate: `SHORT_STACK_COMPACT_DIAGONAL_GATE.md`. The Legendre identities and the general finite-index lattice principle are classical. The actual N/W reductions and their full coefficient normalization are retained below. This note supplies a proved structural reduction, not an all-degree odd-content upper bound.

## 1. Integer basis and its full index

Let P_n be the classical Legendre polynomial with P_n(1)=1. Define

    ell_i(y)=2^(2i)P_(2i)(sqrt(y))
       =sum_(r=0)^i(-1)^(i-r)binom(2i,i-r)binom(2i+2r,2i)y^r.

All coefficients are integers. Its leading coefficient is

    c_i=binom(4i,2i).

Write T_n for the lower triangular coefficient matrix of ell_0,...,ell_(n-1), and

    Delta_n=det T_n=product_(i=0)^(n-1)c_i>0.

This is NOT an integer unimodular change. Its exact determinant is counted. The elementary central-binomial bound gives log Delta_n<=2(log2)n(n-1), so its total cost is O(n^2). Also no prime greater than 4n-4 divides Delta_n.

## 2. The actual reciprocal companion becomes diagonal

Keep f(y^r)=(2r)! and mu(y^r)=D_(2r), as in the preceding author notes. The complete functional K is

    K(P)=-f((y+1)P)+4 integral_0^1 P(x^2)dx.

Classical even-Legendre orthogonality gives EXACTLY

    4 integral_0^1 ell_i(x^2)ell_j(x^2)dx
       =delta_ij 4·16^i/(4i+1)=:Omega_ij.                (1)

For N, the highest nonzero diagonal index is i=k-1, so its denominator 4k-3 is within L=lcm(1,3,...,6k-5). For W the highest index is k-2. All transformed entries thus remain integers after their original L multiplier. No new denominator or period is introduced.

Apply T_k separately to the two row blocks of N and T_(2k-1)^t to its columns. The resulting ACTUAL integer matrix is

    N'=[ mathcal G ; L(-mathcal F+Omega) ],
    mathcal G_ij=mu((y+1)ell_i ell_j),
    mathcal F_ij=f((y+1)ell_i ell_j).

The compact term is zero for every column j>=k, so these k-1 rightmost columns contain only the two Gamma projections.

Similarly apply T_k,T_(k-1) to W's two row blocks and T_(2k)^t to its columns. Its full top block is

    mu(ell_i ell_j)-ell_i(-1)ell_j(-1),

and its lower block is L(-mathcal F+Omega). Its last k+1 columns j>=k-1 have no compact contribution. The TOP endpoint evaluation remains rank one and is not omitted. This basis changes neither the number of columns nor the right-family matching space.

## 3. Exact finite-index transfer of the two contents

Assume the actual beta1 is nonzero, so the two rectangles have full rational rank. Let h_N,h_W and h'_N,h'_W be their respective positive maximal-minor contents. Then there are positive integers theta_N,theta_W satisfying

    h'_N=Delta_(2k-1) h_N theta_N,
    theta_N | Delta_k^2,

    h'_W=Delta_k Delta_(k-1) h_W theta_W,
    theta_W | Delta_(2k).                               (2)

These are exact index identities, not a row-clearer estimate.

For a direct cofactor proof, write w for the primitive integer left nullvector of N, so its signed maximal-minor vector is h_N w. If A=diag(T_k,T_k), the vector for A N is h_N adj(A)^t w. Therefore

    theta_N=gcd(components of adj(A)^t w).

Since A^t adj(A)^t w=(det A)w and w is primitive, theta_N divides det A=Delta_k^2. The full square column transformation supplies the additional determinant Delta_(2k-1).

For W, let z be its primitive integer right nullvector, with signed maximal-minor vector h_W z. If B=T_(2k)^t is its column transformation, the cofactor vector becomes h_W adj(B)z. Thus

    theta_W=gcd(components of adj(B)z) | det B=Delta_(2k).

Its full square row transformation supplies Delta_k Delta_(k-1). Zero entries in either primitive kernel vector cause no difficulty; their gcd still equals 1 and the transformed vector is nonzero. This proves (2) at every prime depth.

Equivalently,

    h'_N/(Delta_(2k-1)Delta_k^2) <= h_N <= h'_N/Delta_(2k-1),
    h'_W/(Delta_kDelta_(k-1)Delta_(2k)) <= h_W
       <= h'_W/(Delta_kDelta_(k-1)).                     (3)

The logarithmic transfer loss is O(k^2). At EVERY prime p>8k-4 all the index factors in (2) are p-units, so

    v_p(h'_N)=v_p(h_N), v_p(h'_W)=v_p(h_W).              (4)

This preserves, rather than solves, any large-prime common content of the complete Gamma-plus-diagonal matrices. A diagonal compact summand does not imply that the full matrix has maximal rank modulo p.

## 4. Full primitive pair and the remaining arithmetic problem

For completeness one may apply the full T_k to BOTH row blocks and full T_(2k)^t to all columns of the original physical pencil M+tuv^t. Its determinant multiplies by

    D_pair=Delta_k^2 Delta_(2k),

and the two ACTUAL physical coefficients become D_pair I0,D_pair I1. Their gcd becomes D_pair gcd(I0,I1), so the final primitive center and denominator are exactly unchanged. This counts the nonmonic basis cost in BOTH entries and makes no favorable cancellation assumption.

The exact actual interface from the preceding note still is

    lcm(h_N,h_W) | G_actual | L h_N h_W,
    q_actual=L|J1|/G_actual.

By (2)--(3), any uniform leading-scale upper or lower law for h'_N,h'_W transfers to h_N,h_W with only O(k^2) logarithmic loss. Our actual response theorem has log|J1|=4k^2logk+O(k^2), and primitive-smallness requires liminf log(h_N h_W)/(k^2logk)>=4. The same necessary leading threshold holds for h'_N h'_W because all displayed basis indices cost only O(k^2).

The unproved step is a sharp content bound or unit-minor construction for the ACTUAL two Gamma projections plus the explicit diagonal (1). Pure Gamma saturation, classical Hilbert diagonalization, and the finite-index formulas do not themselves settle that step. This reduction is saved so future work cannot mistake a convenient orthogonal basis for a primitive output gain.

A single existing k5 pair checks the new nonmonic normalization and index multipliers in `SHORT_STACK_COMPACT_DIAGONAL_RECEIPT.json`. All225 complete entry/compact identities, both primitive cofactor vectors, both theta divisor identities, both transformed rectangular contents, and both FULL physical coefficient determinants pass. It gives theta_N=1384500237120000 and theta_W=20056979222973914434866740652364800000; these large basis-induced factors are counted rather than treated as new favorable actual output content. The actual final q remains308bits exactly. No new degree or prime atlas was run.
