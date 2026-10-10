> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# M24. Short paired right families from a full rectangular matching kernel

Status: author theorem for the construction and exact primitive interface; nine new exact instances. This is not a proof of the irrationality of e+pi. The analytic continuation is assigned to the analysis agent and is separate from this algebraic note.

## Fresh target and prior-work gate

The target is a right family of degree at most 2k-1 obtained from the entire kernel of k matching equations. The earlier M22 construction uses a common orthogonal polynomial of degree 2k-1 followed by k shifts, so its largest right degree is 3k-2. The current family is different. Archive searches for paired Gram/Siegel constructions, integer kernels of derangement moments, and short right families did not locate this construction. Existing generic biorthogonal and common-kernel interpolation ideas are credited; no generic kernel method is claimed new.

The fresh literature gate included the primary paper Zhang and Cheng, *An efficient version of the Bombieri–Vaaler theorem*, arXiv:1707.05941, especially Theorems 1.4 and 2.6 and the Hermite-normal-form discussion. Its lattice height theorem does not imply small primitive approximation denominators here. Generic Hermite–Pade and the determinant criterion in Brown, arXiv:2604.20741, remain relevant context. No located paper establishes the particular primitive content or the irrationality conclusion required below.

## Exact construction

Write S=e+pi, and D_m=m! sum_{r=0}^m (-1)^r/r! for the derangement numbers. For r>=0 put

    C_r = D_(2r) - (-1)^r,
    R_r = -(2r)! + 4 sum_{a=1}^r (-1)^(r-a)/(2a-1),
    V_r = (-1)^r.

The exact endpoint integral is

    integral_0^1 x^(2r) [exp(x)+4/(1+x^2)] dx
      = e D_(2r) + pi (-1)^r + R_r.

For k>=1 let C, R, V be k by 2k matrices with entries C_(i+j), R_(i+j), V_(i+j), for 0<=i<k, 0<=j<2k. The matrix C has full row rank. For k>=2 its leading k by k minor is nonsingular: the positive moment form for ((1-t)^2)^r against exp(-t)dt loses a rank-one evaluation at -1, and the evaluation kernel already exceeds 1 on the span of 1 and y-1. For k=1 the row has C_1=2, although C_0=0.

Let Q be any rational 2k by k full-rank basis of ker C. Its columns give polynomials Q_j(y) of degree at most 2k-1. Define the physical k by k matrix

    H_ij = integral_0^1 x^(2i) Q_j(x^2)
                         [exp(x)+4/(1+x^2)] dx.

Then C Q=0 matches the e and pi responses, hence exactly

    H = RQ + S VQ.

Since V is rank one, det H is affine in S. Equivalently define the stacked determinant

    Delta_k(T) = det [ C ; R+T V ] = beta_0 + beta_1 T.

There is no assumption yet that beta_1 is nonzero for every k. It is nonzero in all nine exact instances below.

## Basis invariance and the final gcd

Choose X with CX invertible, and let T=[X,Q]. Then

    det(H) = Delta_k(S) det(T)/det(CX).

The multiplier is a nonzero rational number independent of S. Thus every rational basis of the full matching kernel gives exactly the same center and the same primitive integer coefficient pair. Replacing Q by smaller integer vectors can improve an implementation, but cannot improve this already fixed primitive denominator. The separately primitive columns in the receipt are a rational basis; they are not asserted to be a saturated integer lattice basis.

Let d=lcm(den beta_0, den beta_1), and g=gcd(d beta_0,d beta_1). If beta_1!=0, the reduced integer form and actual denominator are

    b = d beta_0/g,       a = d beta_1/g,
    c = -b/a,            q = abs(a).

The complete error is

    S-c = Delta_k(S)/beta_1,
    abs(q(S-c)) = abs((d/g) Delta_k(S)).

All statements use both endpoint contributions and the full final gcd. No row clearer, kernel vector height, or determinant scale is identified with q.

## An all-degree upper bound on primitive cost

Let L_k=lcm(1,3,...,6k-5), and

    H_k=2(6k-4)!+4(3k-2)+2.

Multiplying all k lower rows by L_k makes the coefficient pair integral, so L_k^k is a valid simultaneous clearer. Expanding the linear coefficient by its k possible replaced lower rows and applying Hadamard gives

    abs(L_k^k beta_1)
       <= k (2k)^k L_k^k H_k^(2k-1).

Consequently, whenever beta_1!=0,

    log q <= O(k^2 log(k+1)).

This is an upper bound only. It neither predicts the actual remaining common content nor supplies the scale needed for a small nonzero integer form. An analytic error estimate must be combined with the actual primitive q, rather than this coarse bound, before an irrationality criterion can be used.

## New exact receipts

The independent exact driver checks C Q=0, affine dependence of the full stacked determinant at T=0,1,2, cross multiplication of the two complete center formulas, invariance under a unimodular basis change, and the final coefficient-pair gcd.

For k=1,...,9 the actual denominator bit lengths are respectively

    1, 26, 85, 179, 308, 476, 689, 937, 1234.

For k=2 the primitive pair is

    (b,a)=(-322314373,55866720),
    c=322314373/55866720.

The 1000-digit diagnostic errors c-S for k=2,...,9 are approximately

    -0.0905296, -0.0068432, -0.000198257, -0.000005995,
    -0.000000179088, -0.00000000532579,
    -0.000000000157943, -0.00000000000467567.

These decimal observations are not all-degree nonvanishing or convergence proofs. The primitive forms in these instances are not small enough to prove irrationality.

Files: SHORT_PAIRED_KERNEL_CERTIFICATE.json and short_paired_kernel_determinant.py.

## Outstanding original questions

1. Prove beta_1!=0 and obtain a complete signed error representation for every sufficiently large k.
2. Determine the asymptotic actual primitive denominator after all common content.
3. Decide whether the complete primitive forms can be nonzero and tend to zero on an explicitly justified infinite sequence.

No answer to question 3 is currently established.
