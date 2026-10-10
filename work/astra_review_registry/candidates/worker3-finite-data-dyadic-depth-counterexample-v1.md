> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Finite polynomial data and quantitative convergence do not bound dyadic root approximation depth

Status: UNVERIFIED CANDIDATE
Author: worker_3
Content SHA256: 27d6f36815f7b3e87c21e6b1367375d8fa6666ae1d391fe867d02dd887bb27a6

UNVERIFIED CANDIDATE — submitted for independent review.

Statement.
Let N≥1 and D≥1 be integers. Let P∈Z[Y] have degree at most D and satisfy P≡Y−1 coefficientwise modulo 2. Fix a positive odd integer M and a residue c modulo M. There exist an integer-coefficient restricted power series G∈Z_2⟨Y⟩, a transcendental β∈1+2Z_2, and strictly increasing positive integers n_j such that:

(1) G agrees exactly with P in every degree at most D, and G≡P coefficientwise modulo 2^N.
(2) For every integer L≥D, the tail of G beyond degree L has Gauss valuation at least N+L−D. For every r>D, its ordinary integer coefficient satisfies |[Y^r]G|≤2^{N+r−D−1}.
(3) G(Y)=(Y−β)U(Y), where U∈1+2Z_2⟨Y⟩. Consequently β is the unique zero of G in Z_2, G′(y)≡1 modulo 2 for every y∈Z_2, and v_2(G(y))=v_2(y−β) for every y≠β in Z_2.
(4) Every n_j≡c modulo M, and v_2(n_j−β)=v_2(G(n_j))=n_j²+j+N.

Here the Gauss valuation of a restricted series is the infimum of the valuations of its coefficients. Restricted means its coefficients tend to zero dyadically.

Proof.
Since P≡Y−1 modulo 2, its unique root modulo 2 is odd, and P′ is congruent to 1 modulo 2. A root a_k modulo 2^k has a unique lift a_k+ε2^k modulo 2^{k+1}: polynomial expansion gives P(a_k+ε2^k)≡P(a_k)+ε2^kP′(a_k) modulo 2^{k+1}, and the two choices of ε give opposite parities after division by 2^k. Thus P has a unique root residue a modulo 2^N.

By the Chinese remainder theorem choose a positive integer n_1 satisfying n_1≡a modulo 2^N and n_1≡c modulo M. Define, for j≥1,
B_j=n_j²+j+N,
n_{j+1}=n_j+M·2^{B_j}.
The n_j and B_j increase strictly, and B_j tends to infinity. Hence n_j converges in Z_2 to
β=n_1+Σ_{j≥1}M·2^{B_j}.
It is odd and congruent to a modulo 2^N. For each j,
β−n_j=M·2^{B_j}(1+Σ_{k>j}2^{B_k−B_j}).
The parenthesis is an odd dyadic integer, giving v_2(β−n_j)=B_j. Each increment is divisible by M, so every n_j has the required ordinary congruence. Also P(β)∈2^NZ_2.

Put F_0=P. Suppose F_t(β)∈2^{N+t}Z_2. Because β is odd, there is a unique d_t∈{0,1} satisfying
F_t(β)/2^{N+t}+d_tβ^{D+1+t}≡0 modulo 2.
Set
F_{t+1}(Y)=F_t(Y)+d_t2^{N+t}Y^{D+1+t}.
Then F_{t+1}(β)∈2^{N+t+1}Z_2. The sequence F_t converges in the Gauss norm to
G(Y)=P(Y)+Σ_{t≥0}d_t2^{N+t}Y^{D+1+t}.
Evaluation at β is continuous for that norm, so G(β)=0. Each coefficient is an ordinary integer. The displayed formula proves exact agreement through degree D and congruence modulo 2^N. In degree r>D its coefficient is d_{r−D−1}2^{N+r−D−1}; therefore the ordinary coefficient bound holds. Beyond degree L≥D, the first possible added term has t=L−D and valuation at least N+L−D. This proves the asserted tail estimate.

For every integer r≥1,
(Y^r−β^r)/(Y−β)=Σ_{k=0}^{r−1}Y^{r−1−k}β^k,
whose coefficients lie in Z_2. Consequently the series of quotients
U(Y)=(P(Y)−P(β))/(Y−β)+Σ_{t≥0}d_t2^{N+t}Σ_{k=0}^{D+t}Y^{D+t−k}β^k
converges in the Gauss norm: the t-th added polynomial has Gauss valuation at least N+t. Termwise multiplication gives (Y−β)U=G(Y)−G(β)=G(Y).

The polynomial quotient is congruent to 1 modulo 2. Indeed, reducing P(Y)−P(β) modulo 2 gives Y−1, while Y−β reduces to Y−1; polynomial division gives quotient 1. Every added quotient is divisible by 2. Thus U∈1+2Z_2⟨Y⟩, so U(y) is a unit for every y∈Z_2. This proves uniqueness and the valuation identity. Differentiation is legitimate for restricted series, since multiplying coefficients by nonnegative integers does not decrease their dyadic valuations. Alternatively G≡Y−1 modulo 2 immediately gives G′≡1 modulo 2. Applying the valuation identity at n_j proves (4).

Finally β is transcendental over Q. Suppose A(β)=0 for a nonzero polynomial A∈Z[Y] of degree d. Polynomial division by Y−β yields A(Y)=(Y−β)V(Y) with V∈Z_2[Y], because β∈Z_2. Hence v_2(A(n_j))≥B_j whenever A(n_j)≠0. The strictly increasing positive n_j eventually avoid all integer roots of A. Let C be the sum of the absolute values of its coefficients. For these sufficiently large j,
2^{B_j}≤|A(n_j)|≤C n_j^d.
Thus n_j²+j+N≤log_2 C+d log_2 n_j, contradicting n_j→∞. This proves transcendence and completes the argument.

Scope and self-audit.
The construction shows that the stated finite polynomial data, coefficientwise finite precision, exponential ordinary coefficient bound, explicit dyadic convergence rate, simple-root factorization, and fixed odd-modulus restriction can coexist with quadratic approximation depth. Its hypotheses include P≡Y−1 modulo 2; it makes no assertion for arbitrary prescribed polynomial data. It does not preserve an arbitrary preassigned infinite coefficient sequence, recurrence, determinant identity, or endpoint normalization. It therefore neither classifies the project's exceptional root nor supplies or refutes a denominator estimate for that family. No conclusion about the rationality of e+π follows.

Evidence and dependencies.
The original constructions are recorded in work/astra_20260929/worker_3/note_000018.md (complete-file SHA-256 80bdc94f3eeb2ae439f0efe791a14278c899a80397e5bc857de656e5dbfdb72c) and work/astra_20260929/worker_3/note_000021.md (complete-file SHA-256 09b602f48f7735e954624e05c96fa162f3ddeddd63b3f7600da9987be6efa6b8). Both originals were read completely. The proof above is self-contained apart from elementary properties of Z_2, its complete Gauss-norm algebra, and the Chinese remainder theorem. No numerical evidence or project-specific arithmetic theorem is used. Independent registry review remains outstanding.