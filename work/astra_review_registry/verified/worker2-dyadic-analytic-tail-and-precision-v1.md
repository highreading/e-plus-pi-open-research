> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Coefficientwise dyadic convergence, truncation, and normalization precision for the odd-disk contractions

Status: Independently reviewed research result (AI review; not formal verification)
Author: worker_2
Reviewer: worker_3
Content SHA256: 3b220a9384536f55319370fb83bde92220ecf1b8ea1e296bd0a6a6662f42d7ab
Review: work/astra_review_registry/reviews/worker2-dyadic-analytic-tail-and-precision-v1-worker_3.md

Status: unverified submission for independent review. This claim concerns the explicitly defined analytic germs and the conversion of separately checked finite polynomial data into congruences for those germs. It does not identify them with endpoint quantities or bound actual reduced denominators.

Definitions. Write (Z)_L=product_{t=0}^{L-1}(Z−t), with (Z)_0=1. For b,c≥0 put R=b+2c, s=b+c, and epsilon=(-1)^b/(2^c b!c!). Define h_{b,c}(X)=epsilon (X)_R(X)_s. For R≥1 define k_{b,c}(X)=epsilon (X)_{R-1}(X+1)_s(2X+2−R); for b=c=0 set k_{0,0}=2. Let D(Z)=sum_{j≥0}(Z)_j, interpreted after the substitutions specified below. Define H=sum h, K=sum k, A=sum h D(2X−R), B=sum k D(2X+1−R), and C=KA−HB. All outer sums run over b,c≥0. Work on X=a+8Y, a in {1,3,5,7}, in the complete Tate algebra Q_2⟨Y⟩. The Gauss valuation v_G is the infimum of the dyadic valuations of the coefficients.

Finite-data premise. For each of these four disks, every h and every nonconstant k with R<55 is coefficientwise 2-integral. This is an explicitly separate premise, established in the author's earlier independent reconstruction by exact division before modular inversion: 400,396 coefficient-divisibility checks. That finite computation is not repeated or independently approved by this analytic claim. The conditional analytic statements below are proved without reliance on historical PASS assertions.

Claims. The four defining sums converge in Q_2⟨Y⟩. Under the finite-data premise they belong to Z_2⟨Y⟩. Replacing each outer sum by R<55 and each occurrence of D by its sum over j<20 changes H,K,A,B, and therefore C, by elements of 2^10 Z_2⟨Y⟩. These are congruences for all coefficients, including arbitrarily high degrees. Forming C loses no precision. Dividing a divisible series by 2^r loses r bits; in particular the subsequent normalizations by 4 and 8 are known modulo 256 and 128. Exact division by Y after an exact zero constant coefficient loses no further dyadic precision.

Proof of the coefficientwise bounds. For any integer u, each factor u−t+8Y has Gauss valuation min(v_2(u−t),3), with v_2(0)=infinity. Multiplicativity of the Gauss valuation and counting multiples of 2,4,8 among L consecutive integers give
v_G((u+8Y)_L)≥floor(L/2)+floor(L/4)+floor(L/8)≥7L/8−3.
This is uniform in u, including negative u. Replacing slope 8 by 16 only improves the bound.

Since v_2(2^c b!c!)≤c+b+c=R and s≥R/2, every h summand satisfies
v_G(h)≥7(R+s)/8−6−R≥5R/16−6.
For R≥1 the extra linear factor of k is integral, so
v_G(k)≥7(R−1+s)/8−6−R≥5R/16−55/8≥5R/16−7.
The exceptional term k_{0,0}=2 is integral and is retained.

For any integer u, D(u+16Y) is an integral restricted series: each falling factorial is an integral polynomial and its Gauss valuation is at least 7j/8−3, tending to infinity. Consequently v_G(D(u+16Y))≥0. The substitutions in A and B have integer intercepts 2a−R and 2a+1−R and slope 16. Multiplication by these D factors therefore preserves the preceding lower bounds. The exceptional B summand is 2D(2X+1).

Convergence. There are only floor(R/2)+1 pairs (b,c) at each R. The lower bounds tend to infinity with R, uniformly over those pairs and over the four disks. The ultrametric inequality introduces no loss depending on the number of summands. Thus the sums of h,k,hD,kD converge in Q_2⟨Y⟩. The D sums converge there as already shown. This proves coefficientwise and Gauss-norm convergence, rather than merely convergence at integer points.

Truncation and integrality. For R≥55, 5R/16−7≥163/16>10; the H,A bound is stronger. Hence every omitted outer summand lies in 2^10 Z_2⟨Y⟩. For j≥20, 7j/8−3≥29/2>10, so each omitted inner summand and their convergent sum lie in 2^10 Z_2⟨Y⟩, uniformly in the intercept. The finite-data premise makes every retained h,k integral. Multiplying the inner truncation error by these kernels therefore preserves precision 2^10. Combining these facts proves that all four germs are integral and agree modulo 1024 with the finite polynomial construction. Without the finite-data premise, the coarse outer lower bounds alone would not justify this inner-error multiplication at the retained indices; the premise is substantive.

If bars denote integral lifts of the finite approximations, then
C−bar C=(K−bar K)A+bar K(A−bar A)−(H−bar H)B−bar H(B−bar B).
Every term belongs to 2^10 Z_2⟨Y⟩. This proves the claimed absence of precision loss in the product difference.

Normalization. If the finite polynomial for C is coefficientwise divisible by 2^r with r≤10, the same is true of the full C, and C/2^r is determined modulo 2^(10−r). Thus the source's divisions by 4 and 8 retain eight and seven bits. On the a=1 disk, division by Y additionally requires C(1)=0 exactly; a constant coefficient merely congruent to zero modulo 1024 would not suffice. This exact identity follows directly from the definitions: H(1)=1−1=0; K(1)=2−6+4=0. Moreover D(1)=2, D(2)=5, D(3)=16, giving A(1)=3 and B(1)=10. All higher outer contributions vanish at X=1 because of their falling-factorial factors. Therefore C(1)=0. If the finite C polynomial on that disk is written with zero constant coefficient, both the true polynomial error and C itself are divisible by Y. Shifting coefficients by division by Y preserves their dyadic valuations and the restricted-series property. Accordingly C(1+8Y)/(8Y) is determined modulo 128 whenever the finite coefficient data give divisibility by 8.

Evidence and dependencies. Original definitions: work/session_20260927/check_hp_b1_odd_dyadic_germs.py, ledger SHA-256 e82d30312ca6dd2eda7ab75d533fc6c9b3c8d2a3cfc9276f32864edefe697b78. Audited historical argument: work/session_20260927/hp_b1_odd_dyadic_germs_independent_review.md, SHA-256 43a17e421a90ec2b0b2a664fa4f62bbde15371bf51b26f15432afd1db2843f64. Independent finite evidence: work/astra_20260929/worker_2/note_000027.md and the separately scoped candidate worker3-dyadic-finite-coefficient-verification-v1, payload SHA-256 95120d1360a13ef505aae42ed923cca030f0b44ceb99489e17c245501c410269. The historical checker was not executed in this audit.

Self-audit and exclusions. The counting argument handles zero and negative integer factors. The K term with R=0 is treated separately, and no division by the nonunit X+1 occurs. Infinite sums are controlled in the coefficient norm. Normalization by powers of two is explicitly distinguished from integral multiplication. The finite arrays and their retained-kernel integrality remain a separate verification dependency. No assertion is made about endpoint interpolation beyond these definitions, algebraicity of a dyadic root, ordinary-integer approximation depth, the actual reduced denominator, or rationality of e+pi.