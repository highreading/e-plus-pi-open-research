> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Multiplication displacement and trailing-pairing review, stage 9

Status: limited independent review of the new conditional implications in Main Stages 11–12; separate original author proofs of actual multiplication displacement and filtered boundary identities. No occurrence theorem, infinite-family nonvanishing theorem, or irrationality conclusion is established.

## Sources and scope

Read in full in the controller receipts: main/SMITH_PIVOT_ROOTS_AND_CENTERED_INVARIANT_STAGE11.md, main/TRAILING_PAIRING_PARTIAL_SURVIVAL_STAGE12.md, main/DIAGONAL_LOCAL_CONTENT_REDUCTION_STAGE10.md under work/parallel_batch_01/, and work/parallel_batch_01/agents/c1e91660/a551144b/DIAGONAL_LOCAL_REVIEW_AND_PAIRING_STAGE8.md. Stage 10 is a starting input, not reviewed again. The earlier differential identities and nullity-one coefficient calculation are not repeated.

Work with k>=2, h=y+1, and the actual matrices M,G,J,C=M-J,B,D of those sources. Fix p>6k when making modular statements. All these matrices are p-integral and J has unit determinant. The specified complete physical clearer delta is a p-unit. These inherited unit hypotheses are retained throughout.

## 1. Limited review: Newton polygon and Smith depths

First minimum index: VALID. If d is the coefficient-content valuation, multiplication by a unit integral formal series preserves the first index t attaining d. The negative-slope portion of the Newton polygon of chi/p^d ends at (t,0), begins at (0,a-d), and has horizontal length t. Thus exactly t reciprocal roots have positive valuation, with total valuation a-d. Reciprocation gives precisely t negative-valuation roots of beta. Missing high coefficients of chi correspond to zero roots of beta and do not affect that group. Algebraic multiplicities are counted throughout, so each repeated root lies in a single valuation group. The bound max(t,k-t), and its stated pure-power and half-degree consequences, follow.

Smith-depth majorization: VALID. The coefficient of degree j uses at most j columns from zQ, leaving an E-minor of size at least r-j. Its valuation is at least H_(r-j). Earlier coefficients have stronger divisibility, so the bound survives the integral unit multiplier. When Q(0) is invertible, the endpoints (0,a) and (r,0) are attained. The convex polygon with ordinates H_(r-j) lies below the actual Newton polygon. At abscissa r-j the actual ordinate equals the sum of the j smallest positive reciprocal-root valuations. This establishes the stated direction of majorization, including equality of total sums. Equal Smith depths consequently force equal positive reciprocal-root valuations. The singleton group when r=1 is simple and defined over Q_p; this does not imply rationality over Q.

Trailing vertex residues: VALID. At a strict gap alpha_i<alpha_(i+1), in degree r-i the unique minimum-depth set of retained E entries is the first i diagonal entries. Terms selecting fewer Q columns have strictly larger valuation; terms selecting exactly r-i columns use only Q(0). This gives the stated signed trailing determinant. The exact coefficient of chi includes the additional unit u(0); this does not change whether the vertex is attained or its valuation.

Depth-face reductions: VALID. Substitution z=p^b w and row division by p^min(alpha_i,b) is integral. Since b>0, Q(p^b w) reduces to Q(0) and u(p^b w) reduces to its nonzero constant. The shallow rows reduce to their diagonal units, the deep rows to -wQ blocks, and elimination of the deepest invertible block yields w^|H| times the displayed F_b, up to a nonzero scalar. Its constant coefficient is a product of units; its leading coefficient is nonzero by the two consecutive trailing-block determinants. Nonzero residual roots describe exactly the depth-b group. Squarefree residual factors lift to simple roots, and an irreducible residual factor lifts to an irreducible local factor of the corresponding degree. The possible factor w^|H| does not interfere with the nonzero factors. No symmetry of Q is needed.

## 2. Limited review: deepest line and Stage 12

Unique deepest pivot: VALID. If b=alpha_r is unique and Q(0)_rr is a unit, the linear coefficient has the unique minimum valuation a-b. The earlier constant coefficient multiplied by the linear term of u has valuation at least a and cannot cancel it. Thus v_p(I_(k-1))=a-b and d<=a-b.

Centered invariant: VALID. For r>=2, the second-leading coefficient bound gives v_p(I_k I_(k-2))>=2a-b-alpha_(r-1)>2(a-b). For r=1, a=b and integrality yields the needed strict inequality directly. Since k-1 is a p-unit, the square term alone gives valuation 2(a-b). Removing the complete gcd subtracts 2d. The resulting invariant is nonzero, excluding a pure linear power without assuming real roots or positivity of squared complex differences.

Deepest simple root: VALID. In p^(-a)chi(p^b w), the constant and linear coefficients are units and every higher coefficient is divisible by p. The strict inequalities use uniqueness of the largest depth for j<=r and integrality for j>r. Its nonzero linear residual root lifts to a simple unit root over Q_p. The horizontal Newton segment has length one; no root of chi can have valuation greater than b because the constant term would strictly dominate. The local root of beta has valuation -b and is unique in that group. A globally rational root with that denominator valuation would therefore be simple.

Single trailing-block theorem: VALID. With s=r-i and b>c as in Stage 12, the selected coefficient has exact valuation H_i. The left and right supporting lines through (s,H_i) have slopes -b and -c. Every coefficient lies above the resulting convex broken line, and the point at s is attained; hence it is a Newton vertex. Exactly s reciprocal roots have valuations at least b, summing to a-H_i, and every remaining reciprocal root has valuation at most c. Zero roots of beta belong to the latter group under the stated denominator convention. This argument does not require d=0 and permits additional shallower negative roots. The content bound and multiplicity consequences follow with the stated directions.

Intrinsic formulation: VALID. Under a unit congruence G'=W^T G W, the condition Gx in p^b Z_p^k is equivalent, for x=Wv, to G'v in p^b Z_p^k because W^T is invertible over Z_p. Its mod-p image is exactly the span of directions of depth at least b. Restricting x^T C J^(-1)D y to this subspace changes by congruence under a basis change, even if the form is nonsymmetric. Its determinant is multiplied by a nonzero square. Thus nonsingularity is intrinsic. Counting each successful prime once by its largest proved survival weight gives the conditional global lower bound, not a favorable-content construction.

No correction to these assigned conditional conclusions is required. Their actual residue hypotheses and any quantitative weight of successful primes remain unproved.

## 3. Original multiplication identities with complete boundary vectors

Let S be the k-by-k truncated multiplication-by-h matrix: S e_j=e_(j+1) for j<k-1 and S e_(k-1)=0. Let e=e_(k-1) be the terminal coordinate and e0=e_0 the constant coordinate. Thus for a coefficient vector x, Sx represents h x(h)-(e^T x)h^k.

For any Hankel matrix A_ij=a_(i+j), define its boundary vector v_A by (v_A)_i=a_(k+i), 0<=i<k. Direct entry comparison gives

 A S-S^T A=e v_A^T-v_A e^T.                         (1)

Indeed the two shifted entries agree away from the terminal row and column. In the terminal row only the first term remains; in the terminal column only its negative remains. At the terminal corner they cancel. The final entry of v_A cancels from (1), but retaining it provides a uniform moment-vector convention.

For the actual matrices define

 c_i=mu(h^(k+i)),
 g_i=mu(h^(2k+i)),
 d_i=R_k(h^(2k+i)).

The full jet annihilates every h power of degree at least k, so its boundary vector is zero. The low matching block C therefore has boundary vector c. In particular c=G e0 exactly. Equation (1) gives

 G S-S^T G=e g^T-g e^T,
 C S-S^T C=e c^T-c e^T,
 J S=S^T J,
 D S-S^T D=e d^T-d e^T.                             (2)

Since J is invertible,

 S J^(-1)=J^(-1)S^T.                                (3)

All identities hold over Q for every k>=2, and over Z_p under the inherited unit assumptions. No nonunit pivot of G is inverted.

The boundary vectors contain the actual moments, including both rational endpoints. Explicitly, for 0<=i<k and N=2k+i,

 g_i=sum_(t=0)^N binom(N,t)D_(2t),
 d_i=-sum_(t=0)^N binom(N,t)(2t)!
       +c_k sum_(t=0)^(k+i) binom(k+i,t)/(2t+1).

Here D_(2t) denotes the derangement number, whereas the matrix D is the high rational block. The scalar c_k is the normalized pole coefficient from the construction. These expressions follow from the high-degree endpoint formula, since N>=k. The largest added moment index is 3k-1. The rational integral denominators in d_i are at most 4k-1, and c_k is p-integral for p>6k. Thus these added boundary vectors are also p-integral. This formula is not used for the low block B.

## 4. Actual effective-matrix displacement

Put H=C J^(-1)D. By adding and subtracting C S J^(-1)D and using (3), equations (2) give the exact identity

 H S-S^T H
 =e c^T J^(-1)D-c e^T J^(-1)D
    +C J^(-1)e d^T-C J^(-1)d e^T.                   (4)

This establishes rank at most four for THIS displacement, over Q and after reduction modulo p. It does not establish symmetry of H, low rank of H itself, or a comparable displacement bound after arbitrary Schur elimination.

For clarity, introduce the vectors and rows

 a=C J^(-1)e,  t=C J^(-1)d,
 u^T=c^T J^(-1)D,  v^T=e^T J^(-1)D.

Then (4) is e u^T-c v^T+a d^T-t e^T. The order of all factors matters because H need not be symmetric.

There is also an exact formal identity retaining the complete low block. Let L(z)=J+zB and let beta_i=R_k(h^(k+i)), so beta=D e0. From the Hankel identity,

 L(z)S-S^T L(z)=z(e beta^T-beta e^T).

Consequently H(z)=C L(z)^(-1)D satisfies

 H(z)S-S^T H(z)
 =(e c^T-c e^T)L(z)^(-1)D
  +C L(z)^(-1)(e d^T-d e^T)
  -z C L(z)^(-1)(e beta^T-beta e^T)L(z)^(-1)D.        (5)

To verify the last sign, multiply the commutator identity for L on both sides by L^(-1), obtaining S L^(-1)-L^(-1)S^T=L^(-1)(L S-S^T L)L^(-1), and substitute it when moving S through the product. All inverse coefficients are p-integral because L(0)=J is a unit matrix. Formula (5) explicitly retains B at every higher order. It has displacement rank at most six over Q(z), but no bound for the final reduced Q(z) is asserted.

## 5. Restriction to a proper trailing filtered subspace

Fix a positive depth break b and let L_b={x:Gx in p^b Z_p^k}, V_b its mod-p image. The main case is a proper trailing subspace within the nonunit directions, with unequal positive depths on the two sides of the break. Nothing below assumes its restricted H-form is nonsingular.

Because b>=1, every x in V_b lies in ker(G mod p). Since c=G e0 and G is symmetric,

 x^T c=0 mod p for x in V_b.                         (6)

Restricting (4) therefore gives the boundary identity

 H(x,Sy)-H(Sx,y)
 =(e^T x)(u^T y)+(x^T a)(d^T y)-(x^T t)(e^T y)
                                                        mod p,       (7)

for x,y in V_b, where H(x,y)=x^T H y. The omitted fourth term is exactly -(x^T c)(v^T y), which vanishes by (6). Neither u nor a nor t is asserted to vanish on V_b: the relation c=G e0 cannot be moved through J^(-1)D or C without additional information.

Equation (7) is a boundary expression for the multiplication defect of the restricted pairing. It is not an expression for the pairing values themselves, and S need not preserve V_b. Both limitations are substantive.

The G identity supplies an additional exact restriction. For x,y in L_b,

 (e^T x)(g^T y)-(g^T x)(e^T y)=0 mod p^b.            (8)

Indeed its left side is x^T(GS-S^T G)y; both terms are divisible by p^b. In particular the two boundary functionals e^T and g^T are linearly dependent on V_b whenever e^T is nonzero there.

More precisely, suppose x0 in L_b has e^T x0 a unit and set lambda=(g^T x0)/(e^T x0) in Z_p. Then (8) gives

 g^T x=lambda e^T x mod p^b, x in L_b,
 G Sx=(lambda e-g)(e^T x) mod p^b.                  (9)

These formulas retain depth b, rather than merely the mod-p radical. They follow from actual multiplication, not from a Schur restatement.

There is a useful partial closure consequence. Under this same unit-boundary hypothesis,

 S(V_b intersect ker e^T) is contained in V_b.        (10)

To prove it, lift v in that intersection to x in L_b. Its terminal coefficient lies in pZ_p. Subtract [(e^T x)/(e^T x0)]x0, a p-multiple of x0, to obtain a lift with terminal coefficient exactly zero and the same residue. By (9), its shifted vector lies in L_b. This proves (10). Without the unit-boundary hypothesis this adjustment is unavailable and (10) is not claimed.

If V_b is proper and e^T is nonzero on it, S cannot preserve ALL of V_b. Otherwise V_b would be invariant under the single nilpotent shift and contain a vector with nonzero terminal coefficient; this alone does not force the whole space, so no contradiction follows from that observation. Accordingly we make no general noninvariance assertion: (9), rather than a blanket statement, is the exact criterion to use.

## 6. Deepest line and limits of these restrictions

When V_b is the unique deepest line, (7) remains valid, but it involves H(z,Sz)-H(Sz,z), not H(z,z). Its right side is

 (e^T z)(u^T z)+(z^T a)(d^T z)-(z^T t)(e^T z).

There is no symmetry assumption allowing the left side to be set to zero. Even if additional information made Sz a scalar multiple of z modulo p, the resulting identity would constrain these boundary quantities, not force z^T H z to be nonzero.

For a higher-dimensional trailing subspace, (7) and (10) give relations on shifts of vectors with vanishing terminal coordinate. They do not determine a seed pairing matrix or its determinant. A small displacement rank bounds a commutator; it does not imply nondegeneracy of the original form. No such implication is used here.

The precise remaining arithmetic premise is a proof that the ACTUAL matrix Z_b^T C J^(-1)D Z_b is nonsingular modulo p for a useful set of pairs (k,p), where Z_b consists of lifts of a basis of V_b. The new identities reduce some shift relations to the displayed boundary forms, but do not evaluate their initial values or preclude cancellation. Neither an infinite supply of eligible primes with a strict positive-depth break nor successful pairing residues on such a supply is established.

## 7. Primitive interpretation and stopping point

If that restricted determinant is a unit at the break indexed i, the reviewed Stage 12 theorem gives v_p(I_(k-s))=H_i, v_p(g)<=H_i, and v_p(A)>=a-H_i. The complete physical clearer remains a p-unit here; all nonunit pivots remain in G. Failure of the constant restricted pairing is not evidence that the complete gcd is divisible by p: higher coefficients involve the full B and the additional formal boundary term in (5), together with the unit-block Schur corrections.

The original results of this stage are the exact all-degree identities (2), (4), (5), the filtered boundary congruence (8), and the conditional depth-preserving shift statement (10). They establish no actual nonvanishing theorem and no centered-invariant conclusion beyond Main's reviewed conditional theorem. The branch stops at this explicit arithmetic premise, as requested.

No prime atlas, abstract example presented as actual-family evidence, numerical computation, network access, or irrationality claim is made. The original identities are author proofs; the limited review is confined to the new conditional implications in Stages 11–12.
