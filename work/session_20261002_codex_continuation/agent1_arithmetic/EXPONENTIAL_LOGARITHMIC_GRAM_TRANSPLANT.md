> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact exponential/logarithmic determinant transplant and its coefficient-matching limit

Author result L22, 2026-10-02. Fresh archive/primary queries and the overlap boundary are recorded in TARGET_LEDGER.md. Root separately owns paired left/right polynomial families; this note treats real symmetric polynomial-product matrices only. No independent audit is undertaken.

Brown's 2026 paper https://arxiv.org/pdf/2604.20741v1, §§7.4–7.5, distinguishes row/column clearings from the denominator of the determinant's full coefficient polynomial. That arithmetic mechanism has an exact elementary transplant to exponential plus arctangent moments. The exponential response is a positive Gamma Gram matrix and the logarithmic response is a signed finite-rank evaluation matrix. On even polynomial bases the full determinant is linear in the formal pi response; its precise coefficient denominator and primitive content can be computed after all determinant cancellations.

The direct symmetric coefficient-one transplant has a sharp obstruction: a real polynomial space whose EVERY product has equal e and pi responses has dimension at most1. For the standard even monomial matrices, the determinant remains a nonconstant polynomial in e even under a rationality hypothesis for S=e+pi. Thus a determinant-denominator gain by itself does not isolate S.

## 1. Exact endpoint and logarithmic reduction

For a real rational polynomial P define finite endpoint functionals

    A(P)=Σ_(k≥0)(−1)^k P^(k)(1),
    B(P)=Σ_(k≥0)(−1)^k P^(k)(0).

Repeated integration by parts, or differentiating the finite antiderivative, gives

    ∫_0^1 P(x)e^x dx=e A(P)−B(P).              (1)

The SAME exponential endpoint coefficient has the exact real integral representation

    A(P)=∫_0^∞ e^(−t)P(1−t)dt.               (2)

Indeed expand P(1−t)=ΣP^(k)(1)(−t)^k/k! and use ∫e^(−t)t^k dt=k!. This representation is crucial: A(PQ) is a positive definite Gram pairing on any finite-dimensional real polynomial space.

Divide P by the monic polynomial 1+x²:

    P(x)=(1+x²)H_P(x)+a(P)+b(P)x,
    a(P)=Re P(i), b(P)=Im P(i).

Then the complete logarithmic integral is

    4∫_0^1 P(x)/(1+x²) dx
      =4∫_0^1 H_P(x)dx+pi a(P)+2log2 b(P).     (3)

Define R(P)=−B(P)+4∫H_P. For the positive weight rho(x)=e^x+4/(1+x²), equations(1)–(3) yield

    I(P)=∫_0^1 P(x)rho(x)dx
        =R(P)+e A(P)+pi a(P)+2log2 b(P).         (4)

For integer P, A(P),B(P),a(P),b(P) and H_P's coefficients are integers. Only the integration of H_P supplies rational denominators; they divide lcm(1,…,max(1,degP−1)). Thus there is no raw factorial denominator in this unnormalized polynomial moment integral. The factorials occur in its integer endpoint coefficients instead.

This calculation does not assume that e is an ordinary algebraic period, nor that 1,e,pi,log2 are numerically independent. It gives explicit response coordinates. Brown's algebraic Mellin hypotheses are not silently imported. The current irregular-period framework in Snodgrass https://arxiv.org/pdf/2608.06005 is relevant context, but its period pairing supplies no injectivity or mixed numerical nonzero theorem used here.

## 2. Exact finite-rank coefficient matrices

Let P_1,…,P_m be linearly independent real rational polynomials. Write

    G_ij=A(P_i P_j), R_ij=R(P_i P_j),
    a_i=a(P_i), b_i=b(P_i).

The real moment Gram matrix Q_ij=I(P_iP_j) has exact response decomposition

    Q=R+e G+pi(aa^T−bb^T)+2log2(ab^T+ba^T).    (5)

Here G is positive definite by(2). The pi coefficient is a signed rank≤2 matrix, and the log2 coefficient has rank≤2. The signs in(5) are those of the ACTUAL product P_i(i)P_j(i); no complex conjugation is introduced.

If every P_i is even, b=0, put v=a, and

    Q=R+e G+pi vv^T.                           (6)

For formal variables X,Y let F_m(X,Y)=det(R+XG+Yvv^T). The rank-one determinant identity, valid even when R+XG is singular at a particular X, gives the exact polynomial formula

    F_m(X,Y)=f_m(X)+Y g_m(X),
    f_m(X)=det(R+XG),
    g_m(X)=v^T adj(R+XG)v.                      (7)

Thus deg_Y F≤1. If v≠0, deg_X g=m−1 and its leading coefficient is

    det(G) v^T G^(−1)v>0.                      (8)

The determinant also has the exact positive integral representation

    det Q=(1/m!)∫_[0,1]^m det(P_i(x_j))²
                           ∏_(j=1)^m rho(x_j)dx_j.  (9)

This follows directly by expanding the two determinants and integrating each variable; it is the standard Andréief identity. It establishes nonvanishing for independent P_i without an algebraic-period claim. For P_i=x^(2i), indexed i=0,…,m−1, the determinant integrand is ∏_(a<b)(x_a²−x_b²)² times the positive weights. Formula(9) is a precise analytic object on which Brown's determinant-size idea can be tested; no claimed asymptotic or irrationality criterion is needed for the identities here.

## 3. Full formal coefficient denominator and primitive content

For rational polynomial bases, treat X,Y as explicit response symbols rather than presuming any unknown numerical relation. Let Drow be ANY integer product of row clearings that makes the full coefficient polynomial Drow F integral. Let

    C=gcd(all integer coefficients of Drow F).

The exact minimal POSITIVE INTEGER clearing of the full coefficient polynomial is

    Dcoeff=Drow/gcd(Drow,C),                    (10)

and its primitive coefficient multiplier is the positive rational number

    Mprimitive=Drow/C.                         (11)

Proof. Write F as a reduced rational coefficient vector. The minimum integer multiplier is the least common multiple of the coefficient denominators. If c_i=Drow F_i, then p-adically the denominator exponent is max(0,vpDrow−min_i vp c_i), which is(10). Dividing the entire integer coefficient vector by C proves(11). This retains ALL determinant coefficient cancellations rather than multiplying raw row denominators and interpreting that product as primitive cost.

The integer clearing and rational primitive multiplier are distinct. In particular a factor of C coprime to Drow improves primitive coefficient height without reducing the minimum integer clearing. A determinant-only content gain need not be realizable by the separate row/column transformations required to retain an integral matrix of linear forms for Minkowski. Brown §7.5's polynomial determinant mechanism and §7.2's matrix mechanism therefore remain distinct applications.

For the standard even basis P_i=x^(2i), define k=i+j. Its entries are exactly

    I(x^(2k))=!_(2k) e+(−1)^k pi+r_k,
    r_k=−(2k)!+4Σ_(j=0)^(k−1)(−1)^j/(2k−1−2j),  (12)

where !_(2k) is the ordinary derangement integer. The empty sum at k=0 is0. The receipt computes the complete determinant response polynomial using rational arithmetic in dimensions1,…,4:

| m | row-clear product Drow | full coefficient gcd C | minimum integer Dcoeff | primitive multiplier |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 1 |
| 2 | 3 | 1 | 3 | 3 |
| 3 | 4725 | 4 | 4725 | 4725/4 |
| 4 | 1719073125 | 48 | 573024375 | 573024375/16 |

At m=4 an odd factor3 truly disappears from the determinant's integer coefficient denominator; the remaining factor16 in the primitive gain is coefficient content. This is an exact new finite illustration of the transplant, not an all-m content theorem. No primes were scanned.

These are exact denominators/content of the FORMAL response polynomial in the specified coordinates. They are not actual reduced rational denominators of the numerical determinant F(e,pi), which is not known to be rational and may obey unknown numerical relations. If a target hypothesis eliminates a response, it is necessary to perform that elimination and its final gcd separately.

## 4. Sharp dimension bound for symmetric coefficient matching

Define the symmetric real polynomial form

    K(P,Q)=A(PQ)−Re(P(i)Q(i)).                  (13)

By(2),(5), on a finite ambient polynomial space its matrix is

    K=G+bb^T−aa^T.                             (14)

As G+bb^T is positive definite and the last subtraction has rank1, K has at most ONE nonpositive direction (negative directions plus radical dimension), and in particular at most one negative direction. This is stronger than an unsigned rank2 perturbation bound.

**Theorem.** A real polynomial subspace W satisfying A(PQ)=Re(P(i)Q(i)) for EVERY P,Q∈W has dimension at most1. This remains true before imposing the separate removal of log2.

Proof. K vanishes on W×W. If nonzero P∈W had a(P)=0, then

    K(P,P)=∫_0^∞ e^(−t)P(1−t)²dt+b(P)²>0,

contradicting isotropy. Hence the real linear functional a:W→R is injective, which forces dimW≤1. ∎

The even/log2-free case sets b=0 and has the same bound. The conclusion applies to symmetric real polynomial products and their equal e/pi coefficient requirement. It does not apply to separate left/right bases, to indefinite cross pairings, to arbitrary rational kernels, or to a projection that matches only one final linear combination. Root's paired-family target is deliberately separate.

## 5. The determinant still contains a separate e coordinate

Even without requiring every product to match, the determinant(7) does not automatically become a polynomial in S=X+Y alone. Substitution gives

    F_m(X,S−X)=f_m(X)−Xg_m(X)+Sg_m(X).           (15)

For m≥2 and v≠0, (8) makes the coefficient of S contain a nonzero X^(m−1) term. Therefore(15) is not in Q[S]. If v=0, f_m has degree m with leading detG>0 and is again not in Q[S]. This is a formal response obstruction; it does not assert numerical independence of e and pi.

For the standard even monomial bases it is sharper. The leading X^m coefficient after substitution is

    det(G−vv^T)=detG(1−v^T G^(−1)v)<0  (m≥2).  (16)

To prove the strict sign, use the subspace spanned by 1,x², already contained in every m≥2 basis. For P=5−x²,

    P(i)=6,
    A(P²)=25−10A(x²)+A(x⁴)=25−10+9=24.

The evaluation norm v^T G^(−1)v is the maximum of P(i)²/A(P²) over the real even span; it is at least36/24=3/2. The rank-one determinant identity proves(16). Thus the degree remains exactly m for ANY formal value of S.

For example at m=2,

    F_2(X,Y)=8X²+12XY−(119/3)X−(71/3)Y+68/3,
    F_2(X,S−X)=−4X²+(12S−16)X−(71/3)S+68/3.

Consequently, even under a hypothesis S∈Q, these standard determinants remain nonconstant polynomials in the transcendental number e and are not rational lattice values. Brown's rationality contradiction cannot be applied to S by merely shrinking these determinants and clearing their response coefficients. A further matching mechanism or a quantitative small-polynomial argument would be required. This leaves the paired left/right route and other normalized constructions open.

## 6. Evidence and remaining arithmetic target

The exact source exponential_logarithmic_gram_transplant.py and receipt EXPONENTIAL_LOGARITHMIC_GRAM_TRANSPLANT_RECEIPT.json retain every determinant coefficient and the S-substitution in dimensions1–4. No numerical e/pi evaluation, prime atlas, or period-independence assumption is used. Equations(1)–(16) are symbolic author proofs; the finite receipts illustrate content and support sign conventions but are not extrapolated into an infinite arithmetic theorem.

The transplantable arithmetic question is now precise: for a family that DOES remove the separate e response, estimate the minimum determinant coefficient clearing after its complete shared content, then price any remaining evaluated endpoint gcd under the target hypothesis. The symmetric monomial family has a proved coefficient-matching obstruction, so extending its dimension scan would not solve that target. No irrationality conclusion about e+pi is established.
