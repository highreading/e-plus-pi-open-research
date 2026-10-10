> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Paired polynomial moments with an exact determinant linear in e+pi

Root original target M22, 2026-10-02. Author construction and new exact finite receipts. Analytic and arithmetic continuations remain ACTIVE.

## Archive and primary gate

Fresh archive searches checked paired polynomial moments, biorthogonal families, asymmetric Gram matrices, Uvarov modifications, and even-derangement Hankel determinants. Earlier root-unity biorthogonal Markov transforms and finite common-kernel moment interpolation are retained as prior results. They do not give the present even-derangement-minus-evaluation determinant. Agent1's new L22 unweighted exponential/logarithmic Gram transplant is also prior within this session; its symmetric coefficient-matching obstruction is respected.

Fresh primary literature was opened and read: Brown, Mellin transforms, transfinite diameter and rational approximations of integrals, https://arxiv.org/pdf/2604.20741 , §3.2–3.4 and §7.4–7.5; Krattenthaler, A determinant identity for moments of orthogonal polynomials, https://arxiv.org/pdf/2103.03969 , Theorem1/Corollary2 and formal-functional scope; Bertola–Gekhtman–Szmigielski, Cauchy Biorthogonal Polynomials, https://arxiv.org/pdf/0904.2602 ; and the primary exponential/logarithm simultaneous-approximation paper https://rivoal.perso.math.cnrs.fr/articles/explog.pdf . Generic determinant identities and orthogonal modifications are established methods, not claimed new. Brown's algebraic-period hypotheses are NOT asserted for e; only elementary integral and determinant identities are used here.

## The matching moment functional

Let D_j be the integer derangement sequence D_0=1, D_j=jD_(j-1)+(-1)^j. Define on Q[y]

    mu(y^r)=D_(2r), rho(y^r)=D_(2r)-(-1)^r.

The positive functional mu has the concrete representation

    mu(F)=integral_0^infinity exp(-t)F((1-t)^2)dt,
    rho(F)=mu(F)-F(-1).                             (1)

Every nonzero real polynomial has strictly positive mu(F^2). For each n>=2 there is a unique MONIC rational q_n of degree n satisfying rho(y^j q_n)=0 for j=0,...,n-1. The n-by-n moment matrix C_n=(rho(y^(i+j))) is nonsingular: it is the positive matrix M_n=(mu(y^(i+j))) minus vv^T with v_i=(-1)^i. The evaluation norm v^T M_n^-1v is at least3/2. Indeed the orthogonal directions1 and y-1 have mu norms1 and8 and evaluations1 and-2. The determinant lemma gives det C_n=det M_n(1-v^T M_n^-1v)<0.

In particular q_n exists rationally by finite linear algebra. The constant moment rho(1)=0 explains why the monic degree-one construction fails. To see q_n(-1)!=0 without a numerical check, let p_n be the monic mu-orthogonal polynomial and K_n the reproducing kernel for degree<n. Orthogonality implies q_n=p_n+q_n(-1)K_n(-1,y), and thus

    q_n(-1)=p_n(-1)/(1-K_n(-1,-1)).                (2)

All zeros of p_n lie on the positive support, so p_n(-1)!=0; the denominator in(2) is negative. These are direct classical rank-one orthogonal-modification identities. Agent3 continues their analytic consequences separately.

Clear q_n's rational coefficients and remove their common integer content to choose its primitive integer normalization, with positive leading coefficient. This changes neither its constraints nor the resulting rational center.

## All entries depend on S alone

Fix k>=2, n=2k-1, S=e+pi. Use different left and right polynomial families

    P_i(x)=x^(2i), Q_j(x)=x^(2j)q_n(x^2), 0<=i,j<k.

Define the COMPLETE moment matrix

    H_ij=integral_0^1 P_i(x)Q_j(x)[exp(x)+4/(1+x^2)]dx.   (3)

For an even monomial x^(2r), the exponential endpoint coefficient is D_(2r), the exponential constant is -(2r)!, and the arctangent coefficient is(-1)^r. Its rational arctangent part is

    4 sum_(a=1)^r (-1)^(r-a)/(2a-1).

Since i+j<=2k-2=n-1, rho(y^(i+j)q_n)=0 makes the two period coefficients equal. Therefore the EXACT full matrix is

    H=R+S q_n(-1)vv^T, v_i=(-1)^i,                (4)
    R_ij=sum_(t=0)^n q_(n,t)[-(2(i+j+t))!
             +4 sum_(a=1)^(i+j+t) (-1)^(i+j+t-a)/(2a-1)].

There is no log2 term because every product is even. This is a product constraint for the whole matrix, not an approximation to response equality. The right family differs from the left; rewriting it as a weighted symmetric matrix introduces q_n into the measure. L22's positive unweighted coefficient form consequently cannot be substituted for this weighted form.

## Exact linear determinant and actual primitive pair

The rank-one update gives

    det H=beta_0+beta_1 S,
    beta_0=det R,
    beta_1=q_n(-1) v^T adj(R)v.                    (5)

This is valid even if R is singular. The degree in S is AT MOST one; beta_1 is not assumed nonzero at every degree merely from rank1. When beta_1!=0, let d be the least common multiple of the denominators of beta_0,beta_1, and g=gcd(d beta_0,d beta_1). The exact primitive output is

    (b,a)=(d beta_0/g,d beta_1/g),
    c=-b/a, q=|a|, a S+b=(d/g)det H.              (6)

Equation(6) uses the full determinant coefficient pair AFTER all common content. A row-clear product is not its actual rational denominator. The multiplier d/g can itself be rational; both final coefficients remain integers. Scaling the polynomial by a nonzero rational factor scales det H by its kth power but leaves c and its reduced denominator unchanged.

The unimodular basis1,(y+1),(y+1)y,...,(y+1)y^(k-2) confines the S response to the first entry. Hence beta_1 also equals q_n(-1) times the determinant of the rational lower block. Selector develops this exact projected-block arithmetic separately, and agent1 treats dyadic normalization. These interfaces count common content rather than assuming it favorable.

## Full analytic identity and remaining work

Finite permutation expansion of(3) gives the exact integral

    det H=(1/k!)integral_[0,1]^k
       product_(i<j)(x_j^2-x_i^2)^2
       product_j q_n(x_j^2)[exp(x_j)+4/(1+x_j^2)] dx_j.   (7)

This is the ordinary Andréief/Heine determinant identity applied to the present different families. The weight q_n can change sign. Positivity or nonvanishing in ALL degrees is not silently inherited from the positive base measure. Even a sharp determinant bound must be multiplied by d/g in(6) to prove a small integer linear form. These are the separate original analytic and arithmetic targets currently under study by the three children.

## New finite receipt, not an asymptotic proof

PAIRED_DERANGEMENT_LINEAR_S_CERTIFICATE.json computes the NEW primitive integer polynomials and complete rational moment matrices for k=2,...,8. It verifies every matching condition, beta_1!=0 in these seven cases, and det(R+tW)=beta_0+t beta_1 independently at t=-1,2,3. It stores the actual formal coefficient clearer, the full pair content, and the final primitive pair. Every exact assertion passed.

At k=2 the primitive polynomial is

    q_3(y)=1789763+102231y-38891y^2+401y^3,
    q_3(-1)=1648240.

The COMPLETE primitive determinant is

    222654453739525500 S-1247691741707449037.

Its actual rational center denominator is222654453739525500. The rational determinant clearer is33075 and full output content4; using only the clearer would miss that final reduction.

The real diagnostics suggest centers approaching S from below: errors at k=2,3,4,8 are approximately -.2561611,-.0084863,-.0002652464,-2.26205e-10. The actual q bit lengths are58,283,792,1723,3233,5484,8592; the diagnostic absolute primitive forms grow very rapidly. These1000-digit evaluations are labeled diagnostics, not interval certificates, sign proofs, rate theorems, or an irrationality proof. Research on the all-degree mechanism continues.
