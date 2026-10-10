> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Paired derangement determinant: actual coefficient content

Author research, 2026-10-02. This new target follows root M22. The target is an all-degree denominator/content theorem for the actual rational coefficient pair of the linear form in S=e+pi, after the primitive integer normalization of q_n. Root owns the exact finite coefficients, and the analysis agent owns analytic nonzero/positivity. This note is not an audit.

## Archive and primary-paper gate

Archive queries covered even derangement orthogonality, rho moments, weighted Gram matrices, Hankel determinants and primitive determinant content. Read the current `main/GRAM_RESULTANT_CROSS_PRODUCT_REDUCTION.md` and `agent1_arithmetic/EXPONENTIAL_LOGARITHMIC_GRAM_TRANSPLANT.md`. The former is a different normalized cross-product/resultant identity; the latter derives the complete unweighted exponential/arctangent Gram interface and its formal coefficient content. Neither establishes weighted q_n carry/content at every degree. Earlier Hermite–Pade D_(2r) moment formulas overlap scalar background only.

Fresh online queries were `derangement numbers even moments orthogonal polynomials Hankel determinants` and `site:arxiv.org Hankel determinants derangement numbers Charlier orthogonal polynomial arithmetic`. Opened the primary full texts:

- Guettai–Laissaoui–Rahmani, *The Hankel determinants for the generalized derangement polynomials of order r*, https://arxiv.org/pdf/2402.16160, Theorem4.4 and Remark4.5. The full-index derangement Hankel product is classical; it does not apply unchanged to D_(2r)−(−1)^r.
- Krattenthaler, *Hankel determinants of linear combinations of moments of orthogonal polynomials, II*, https://arxiv.org/pdf/2101.04225, Theorem1 and its condensation proof. The Christoffel determinant identity is established prior work. It does not price the evaluated projected coefficient pair here.

The new boundary is the primitive q_n-weighted even-minus-evaluation moment projection and its full rational determinant coefficient pair. No general Hankel or Christoffel identity is claimed new.

## Exact normalization

Let k>=2 and n=2k−1. Write D_m for the derangement integer and

    rho_r=D_(2r)−(−1)^r,
    beta_r=−(2r)!+4 sum_(a=0)^(r−1) (−1)^a/(2r−2a−1).

The empty sum is0. Root's primitive integer q_n(y)=sum_(t=0)^n q_t y^t satisfies

    sum_t q_t rho_(s+t)=0       (0<=s<n).

Then with Q=q_n(−1), R_ij=sum_t q_t beta_(i+j+t) and u_i=(−1)^i,

    H=R+S Q uu^T,
    det H=A+S B,
    A=det R, B=Q u^T adj(R)u.

All indices in the k-square matrix fall inside the exact orthogonality range. The maximum beta index is2n−1; all entry denominators are odd and divide lcm of the odd integers<=4n−3. The actual primitive coefficient pair is obtained from A,B by their common rational normalization, not from row clearers.

## Exact unimodular response reduction

Replace the monomial basis1,y,...,y^(k−1) by

    1, (1+y), y(1+y), ..., y^(k−2)(1+y).

The triangular change has determinant1 and evaluation at y=−1 is(1,0,...,0). In this basis write

    R'=[ r00  b^T ; b  D ],
    D_ij=beta[y^(i+j)(1+y)^2q_n(y)]       (0<=i,j<k−1).

Here beta is the linear moment functional. Consequently, without division and even if D is singular,

    B=Q det D,
    A=det R'.

The complete rational block entries have the useful scalar relation

    beta_r+beta_(r+1)=−(2r)!−(2r+2)!+4/(2r+1).

Thus multiplying by1+y eliminates the arctangent response exactly. This is an arithmetic reduction of the actual coefficient pair, not a replacement approximation family.

## Next structural question

Modulo an odd prime p, D_(2r) is a polynomial in r of degree p−1, with nonzero leading coefficient, whereas(−1)^r is a separate exponential sequence. An n-row exact orthogonality relation should therefore force q_n modp to contain(y−1)^p(y+1) whenever n>=p+1. That alone forces p|Q but does not prove common output content: beta has denominators divisible byp, and their carried coefficients must be retained. A full carry map and a useful shared-content lower bound are still open here.

The root's finite receipt `main/PAIRED_DERANGEMENT_LINEAR_S_CERTIFICATE.json` is treated as exact normalization data. It is not an all-degree theorem. No new prime atlas or additional degree scan is part of this target.
