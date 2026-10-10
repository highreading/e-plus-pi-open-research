> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the coherent matrix Green/CD estimates

Date: 2026-09-13. Reviewer: audit_results.

Reviewed raw_branch_matrix_christoffel_darboux.md, with particular
attention to Sections4–5. The stated estimates pass. I did not
construct any new HP degree or spectral root. The finite
characteristic identity in its companion boundary-pencil note is
used as an identified input; the conversion to rational branch
normalization is checked below independently.

The three right-cut edges give exactly Gamma_N, with its lower
off-diagonal entry −a_N. Summing KR(y)=yR(y) minus its transposed
counterpart gives the sign(y−x) in(3). Differentiating in y gives
the stated diagonal matrix CD identity. The initial two rows give
the matrix(6), with trace11/4, determinant1, and least eigenvalue
(11−sqrt57)/8>0.

The interior relation is
(K_N−xI)U_N=−iota_N Gamma_N P_N. Thus U_N=(xI−K_N)^(-1)
iota_N Gamma_N P_N, giving the positive-sign resolvent formula(9).
Its divided difference and derivative yield(11)–(12). In particular
the scalar sign is −M_N'>0. The spectral weights and the strict
upper-half-plane imaginary sign are correctly matrix-valued
statements; the note does not infer positivity of mixed scalar
minors or identify this finite row spectrum with the prolate spectrum.

For the uniform estimates, the lower spectral bound follows from
the positive compression of J², the bound ||J_N||<=N−3/8, and
max lambda_k=N(N−1). It is −N²+3/8, with no invalid substitution
of J_N² for the compression of J². The existing upper bound is
N+3/4. The stated N threshold makes
xI−K_N lie between(c0 N²/2)I and((c1+1)N²)I.

The triangular Gamma_N has diagonal entries a_(N−1)a_N and
a_N a_(N+1), and one off-diagonal entry −a_N. The bounds on a_j
give
sigma_min Gamma_N>=(N²−3N−2)/4>=N²/8,
||Gamma_N||<=(N+1)(N+4)/4<=N²/2 for N>=8.
Applying the resolvent and its square gives exactly the constants
in(17)–(18). Congruence by P_N gives(19), which controls every
coherent two-channel vector. The rational normalization is a fixed
right congruence diag(1,1/sqrt3) plus row factors sqrt(2k+1), giving
precisely the weighted matrices in(20).

For(21), the normalized recurrence coefficient satisfies
U_j=a_(j+1)a_(j+2)sqrt((2j+5)/(2j+1)). Its product differs from
the symmetric product by sqrt((2N+1)(2N+3)/3), exactly the factor
between det P_N and det mathcal P_N. Thus the absolute determinant
formula with product U_j has the correct seed and endpoint factors.
Since U_j<=(j+2)², the denominator is at most((N+1)!)². The
inequality(N+1)!<= (N+1)^N<= (2N)^N is valid, so the lower bound
(c0/8)^N follows. The previously reviewed generating-function bound
gives exp(O(N)) upper entries uniformly for x<=c1 N². The identity
sigma_min=|det|/sigma_max for a2-by-2 matrix therefore gives the
claimed exponential conditioning bound, with constants depending
only on the stated fixed parameters.

No correction is needed. These estimates control a single adjacent
branch matrix at a common parameter and a coherent two-channel
Gram matrix. They do not supply an inverse estimate for the growing
matrix that evaluates different rows at many prolate nodes; the
note keeps that distinction.
