> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Preserve pairwise logarithmic convexity in the relative spread gain

Coordinator deduction, 9 October2026. A DIFFERENT full audit is pending.
This is a conditional algebraic corollary of the already supplied
Laguerre relative-factor and moment proof, not a new moment computation.
The earlier base comparison has now passed its DIFFERENT A1turn10 audit.
The first spread argument remains under A2's different audit. No current
admitted or staged prompt is changed to include this later note.

## Reuse and overlap

Before this deduction the archive main mathematical files, ALL Desktop
continuations, current controls and reports were searched for85/77,
77/85, log(85), and pairwise Jensen terms. The specific relative constant
was not recovered. The important broader proportional-Jensen overlap,
PROPORTIONAL_REVIEW_AND_QUANTITATIVE_STAGE6.md, was read in full. Its
weighted bounded-interval determinant is different; its accepted energy
and entropy normalization is REUSE as a method, not a theorem about the
present factorial determinant. The classical complex normalization is
already covered by the reopened primary Cunden--Dahlqvist--O'Connell
paper, https://arxiv.org/pdf/1809.10033 , Section1.2. Only that selected
section and initial discussion were inspected. No literature novelty
claim or new probabilistic theorem is made here. The elementary convex
inequality below is derived explicitly.

## Exact finite statement

Retain the SAME positive nodes, probability law and exact relative factor
of COORDINATOR_COMPACT_LAGUERRE_JENSEN_REFINEMENT_CANDIDATE.md. For k>=2
put p=k(k-1)/2 and

    r_ij=(z_i-z_j)/(z_i+z_j),
    X=sum_(i<j) r_ij^2,
    f(t)=-log(1-t), 0<=t<1.

The reused deterministic/probabilistic Cauchy argument gives

    EX >= R_k=k(4k-1)(k^2-1)/(85k^2-37k+6).

Because f''(t)=1/(1-t)^2>0, Jensen over the FINITE pair list gives

    sum_(i<j) log g_ij = sum_(i<j) f(r_ij^2)
                           >= p*f(X/p).

Each r_ij^2<1, so X/p<1 pointwise. Integrability follows from the
reused bound0<=sum log g<=product g and the finite relative expectation.
The continuous Laguerre law has unequal nodes almost surely, but the
inequality remains valid at repeated nodes as well. Jensen in probability
and monotonicity of f now give

    E sum log g >= p*f(EX/p) >= p*f(R_k/p).

Here EX/p<1 because the positive variable1-X/p has positive expectation.
The proposed lower ratio is also strictly below1. Directly,

    R_k/p=2(4k-1)(k+1)/(85k^2-37k+6),

and the denominator minus its numerator is77k^2-43k+8>0 for k>=2
(it is increasing there and equals230 at k2). Therefore the same outer
Jensen step in the exact relative determinant identity yields

    det D_k >= B_k*exp(R_star,k),

    R_star,k=(k(k-1)/2)*log[(85k^2-37k+6)/(77k^2-43k+8)].

The limit is

    R_star,k/k^2 -> (1/2)*log(85/77) > 4/85.

The strict improvement follows from-log(1-x)>x at x=8/85. No new
Wick enumeration, integration receipt, reference determinant or original
source computation is needed. This keeps a convexity step that the first
spread proof relaxed to its tangent f(t)>=t.

## Original-source implication and limit

Conditional on the complete first spread proof, the SAME original H,
highest factorial(6k-4)!, source corrections and contact atom give

    (-1)^k H_k(e+pi) >= (3Lambda_k/64)^k h_k B_k exp(R_star,k)>0

for the unchanged cutoff k>=512 and original index family. Its lower
constant becomes15log2-(9/2)log3+(1/2)log(85/77). The leading4k^2logk
term is unchanged. The existing arithmetic implication would replace
4/85 by this larger constant in its CONDITIONAL binary threshold only.
The direct final v2(G), other odd contents and all-prime upper budget
remain open. A stronger analytic lower bound can retire this producer
only after those hypotheses are proved; it does not prove e+pi rational
or irrational. A DIFFERENT full audit of this later corollary is pending.
