> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Reciprocal-factorial kernel and the actual endpoint sums

Status: exact kernel sign theorem and actual-endpoint integral representation proved; uniform endpoint signs remain unresolved. The pending Bernstein verifier has now executed successfully, with its saved output read back. No new HP index, prime, or Bernstein scan was introduced.

## 1. Completed pending verification

The existing check_bernstein_difference_identities.py was inspected and executed unchanged against its three saved inputs. It passed 126 signed-difference identities, 95 shift identities, both endpoint sums, and the original n=6 endpoint comparison. All input bytes were preserved. No assertion or mathematical statement needed repair.

The output bernstein_difference_identity_verification.json and actual stdout were read back; stderr is empty. The verified endpoint is

    D_V=19532105792367929/2149019034696302985216000000.

The two positive saved sums are

    E_6=1355870278086451/73150524144312975360000,
    E_7=181648924564193/70441245472301383680000.

The earlier unexecuted-verifier qualification is therefore superseded by an actual successful execution. An initial mistyped input path was corrected to the confirmed session path; no access boundary was bypassed.

## 2. Exact signed-minor theorem

Let d>=1 and let

    0<=a_1<...<a_d, 0<=c_1<...<c_d

be integers. Set S=d(d-1)/2, A=a_d, e_i=A-a_(d+1-i), and X_j=A+c_j. Then e_1<...<e_d are nonnegative integers and X_1<...<X_d, with X_j>=A>=e_d. Define

    N(e,X)=det[binom(X_j,e_i)]_(i,j=1..d).

The exact formula is

    det[1/(a_i+c_j)!]
      =(-1)^S [product_i e_i! / product_j X_j!] N(e,X).       (1)

Indeed, multiply column j by (A+c_j)! and reverse the row order. The resulting entry is

    (A+c_j)!/(a_(d+1-i)+c_j)!
      =(X_j)_(e_i)=e_i! binom(X_j,e_i).

This proves (1) without any negative factorial convention. Every factorial argument in the original matrix and factorization is nonnegative.

For completeness, N(e,X) is a strictly positive integer. Interpret binom(X_j,e_i) as the number of north/east lattice paths from S_i=(-e_i,e_i) to T_j=(0,X_j). Each path has e_i east steps and X_j-e_i north steps. Expand the determinant into signed families of paths. For intersecting families, exchanging tails at the first intersection is a sign-reversing involution. The planar order of the sources on x+y=0 and sinks on x=0 forces a vertex-disjoint family to connect S_i to T_i in increasing order: crossed endpoint assignments must intersect. Thus the determinant counts the disjoint identity families with positive sign.

At least one such family exists. For each i, go north from (-e_i,e_i) to (-e_i,X_i), then east to (0,X_i). These paths are disjoint: later vertical portions lie strictly to the left, and later horizontal portions lie strictly above earlier endpoints. This also covers e_1=0. Consequently N(e,X)>0, proving

    sign det[1/(a_i+c_j)!]=(-1)^S.                       (2)

Nondecreasing offsets with a repeated row or column give determinant zero. A different ordering requires its corresponding permutation signs. The theorem concerns finite minors and does not assert a positive representing measure.

A useful consecutive-column specialization is

    det[1/(n+m_i-j)!]_(i=1..d,j=0..d-1)
      =Delta(m_1,...,m_d)/product_i(n+m_i)!,             (3)

for increasing nonnegative m_i and n>=d-1. Multiply row i by (n+m_i)!; its entries become the monic falling-factorial polynomials (n+m_i)_j. Their determinant is Delta(m). The reversed column order removes the sign in (2). In our application d=b<=n, all factorial arguments in (3) are at least n-b+1>=1.

## 3. Passing to the actual functions: every signed coefficient remains

Fix even n>=4 and b=n/2. For k=n or n+1 use the following b actual polynomial rows:

    q_l(t)=(1-t)p_(n+l)(t), l=1,...,b-1,
    q_b(t)=p_k(t).

Write q_(i,m)=[t^m]q_i. All degrees are at most n+b. Let

    T_n(q;x)=n! sum_m q_m x^m/(n+m)!,
    eta_k=(-1)^(k+b-1).

The endpoint sums from the earlier continuation are exactly

    E_k=eta_k Wr(T_n(q_1),...,T_n(q_b))(1).              (4)

The high rows are r_(n+l), and the last row is A_k. This preserves their order.

There is a triangular derivative-column change of determinant one that replaces (m)_j by (n+m)_j: both polynomial families are monic of degree j. Applying it to the endpoint jets gives

    E_k=eta_k (n!)^b det[J_ij],
    J_ij=sum_m q_(i,m)/(n+m-j)!, j=0,...,b-1.           (5)

Cauchy–Binet followed by (3) proves the exact positive-kernel expansion

    E_k=eta_k (n!)^b sum_(M)
          det[q_(i,m)]_(i=1..b,m in M)
          Delta(M)/product_(m in M)(n+m)!,              (6)

where M ranges over increasing b-element subsets of {0,...,n+b}.

The factor Delta(M)/product(n+m)! is strictly positive. The coefficient minor is not. Formula (6) retains the multiplication by (1-t), the monic Legendre coefficients, their row order, and eta_k. No coefficient minor may be discarded or replaced by its absolute value when proving a lower bound.

This identifies exactly what sign regularity provides: explicit positive weights for a signed sum of actual coefficient minors. It does not prove the sign of the sum.

## 4. A new real integral representation for the actual sums

Define the ordinary Borel polynomial of each actual row by

    f_i(t)=sum_m q_(i,m)t^m/m!.

For j=0,...,b-1, elementary beta integration yields

    J_ij=1/(n-j-1)! integral_0^1 f_i(t)(1-t)^(n-j-1) dt. (7)

The smallest factorial here is (n-b)!, so every argument is nonnegative. In particular the formula is valid throughout 1<=b<=n; the exponent n-b of the eventual weight is nonnegative.

Factor out the common weight w(t)=(1-t)^(n-b). The remaining column polynomial is (1-t)^(b-1-j). Its degree is b-1-j. Their evaluation determinant, with node rows and j increasing, is +Delta(t): reversal of the polynomial degrees contributes (-1)^S and the leading coefficients contribute the same sign.

Expanding two determinants and integrating term by term gives the determinant integration identity. Its b! factor cancels upon restricting the symmetric product integrand to the ordered simplex. Thus (5)-(7) prove

    E_k=eta_k C_(n,b) integral_(0<t_1<...<t_b<1)
            det[f_i(t_l)] Delta(t)
            product_l(1-t_l)^(n-b) dt_1...dt_b,         (8)

where

    C_(n,b)=(n!)^b/product_(j=0)^(b-1)(n-j-1)! >0.

There is no extra b! in (8). The formula is exact for the actual Legendre-weighted endpoint sums; it is not a renamed determinant nonvanishing condition. It converts the reciprocal-factorial kernel to an ordinary real polynomial determinant integrated against an explicit positive weight.

However, the signed polynomial determinant eta_k det[f_i(t_l)] need not be nonnegative. This is the precise limit of the real integral route.

## 5. Exact fixed-control checks and failed shortcuts

The new checker uses only saved n=6,b=3 polynomial coefficients and the two saved endpoint contractions. It does not rebuild the completed Bernstein control. Its execution passed, preserving every input.

It checked the 120 relevant three-row kernel minors, with increasing column offsets 4,5,6, against (1), and their reversed-column versions against (3). It then checked (6), (7), and (8) against both saved E values. The normalizer in (8) is C_(6,3)=21600.

The coefficient weights actually have both signs:

| Last row | Positive terms in (6) | Negative terms | Zero terms |
|---|---:|---:|---:|
| p_6 | 60 | 59 | 1 |
| p_7 | 60 | 60 | 0 |

For k=6 the first positive term, M=(0,1,2), is

    41005067/63994677626880,

while M=(0,1,3) contributes

    -29371/14108174080.

For k=7 the corresponding terms are

    24068347/237694516899840,
    -36815/107797966848.

Thus even the first two terms refute termwise positivity after the actual signed transform. The full signed sums remain positive and equal the saved E_6,E_7. This closes the shortcut that bare-kernel sign regularity automatically controls the transformed determinant.

The stronger pointwise-integrand route also fails for these actual rows. At the ordered nodes (1/4,1/2,3/4), exact arithmetic gives

    eta_6 det[f_i(t_l)]
      =-77269228521898938600167/1169106515997749128892252160000,

    eta_7 det[f_i(t_l)]
      =-1085990845347560281179719/98789500601809801391395307520000.

Both are strictly negative. At (1/8,1/4,3/8), both signed determinants are strictly positive, as recorded exactly in the certificate. By continuity, these are open regions of both signs inside the simplex, whose weight in (8) is positive. The signed integrand therefore genuinely changes sign; it is not merely zero on an exceptional boundary.

This disproves a pointwise Chebyshev/sign claim for these particular Borel-transformed rows on (0,1). It does not disprove the positive integral or endpoint nonvanishing. That pointwise-sign subroute is stopped.

For reference, direct beta-moment determinants give the unsigned ordered-simplex integrals

    k=6: 1355870278086451/1580051321517160267776000000,
    k=7: -181648924564193/1521530902201709887488000000.

Multiplication by eta_k*21600 gives exactly E_6 and E_7. All these are finite exact statements at the existing control, not uniform evidence promoted to a theorem.

## 6. A concrete signed-integral inequality and the remaining problem

Formula (8) suggests a cancellation-aware sufficient inequality. Let Omega be the ordered simplex and

    F_k(t)=eta_k det[f_i(t_l)],
    W(t)=Delta(t) product_l(1-t_l)^(n-b)>=0.

Suppose one constructs a measurable region U in Omega, a nonnegative lower bound g on U, and a nonnegative upper bound h on Omega minus U such that

    F_k>=g on U,
    F_k>=-h on Omega minus U,
    integral_U g W > integral_(Omega minus U) h W.       (9)

Then (8) proves E_k>0, with the explicit lower bound C_(n,b) times the difference in (9). Polynomial/rational enclosures on a suitable decomposition could make this an independently checkable determinant inequality. In contrast to pointwise positivity, it permits the negative regions already proved to exist.

No uniform decomposition or dominance estimate (9) has been proved here. Replacing its integrals by the exact positive and negative parts without estimating them would only restate E_k>0; that is not claimed as progress. The new progress is the explicit kernel factorization, positive weights, actual polynomial integral, and exact identification of two invalid shortcuts.

The discrete version is equally explicit. Put

    d_(k,M)=eta_k det[q_(i,m)]_(m in M),
    v_M=Delta(M)/product_(m in M)(n+m)!.

Then the residual sign question is whether, uniformly on a specified unbounded even-index set,

    sum_(d_(k,M)>0) d_(k,M)v_M
       >= sum_(d_(k,M)<0) |d_(k,M)|v_M, k=n,n+1,        (10)

with at least one strict inequality. The signs of individual d_(k,M) are not uniformly nonnegative, as the fixed-control witnesses show. A useful proof must derive an actual pairing, determinant cancellation, or integral dominance estimate for these Legendre minors; simply asserting (10) is not a new nonvanishing theorem.

If both signs in (10) are established, the already proved endpoint identity for even n gives

    D_V=[p_(n+1)(1)E_n+p_n(1)E_(n+1)]/[h_n(n!)^b]>0,
    Y=-D_V<0,

provided E_n,E_(n+1)>=0 and they are not both zero. This conditional implication remains valid, but its uniform hypotheses remain open.

## 7. Scope of the moment obstruction and final status

The earlier negative moment-Hankel determinant excludes a nonnegative real representing measure for that difference functional. It does not exclude the oriented sign regularity proved in (1)-(2). In particular the increasing-order reciprocal-factorial two-by-two minors are negative; a Hankel positivity argument and this sign-regular kernel are different assertions.

Proved: the exact signed-minor theorem and its strict sign; the consecutive-column Vandermonde formula; the full signed Cauchy–Binet expansion for the actual endpoint sums; and the real beta-integral representation with exact normalization.

Finite evidence: the pending verifier passed and was read back; the new checker passed all 120 relevant bare-kernel checks and both actual endpoint formulas using saved n=6 data. No input certificate was changed.

Failed shortcuts: positive kernel minors do not force positive coefficient-transformed minors; the actual signed Borel determinant is not pointwise nonnegative on the ordered simplex. Both failures have exact frozen-control witnesses.

Open: uniform aggregate signs of the two endpoint sums, an effective cancellation-aware inequality such as (9), unbounded endpoint nonvanishing, full-remainder nonvanishing, and actual reduced-denominator control. The chosen absolute-bound shrinking obstruction remains unaffected; endpoint gcd improvements cannot rescue that bound ratio.

Agent 2 retains companion conditioning and Agent 4 the quotient audit. Neither is duplicated here.

Files: check_endpoint_factorial_kernel.py; endpoint_factorial_kernel_checks.json; endpoint_factorial_kernel_stdout.txt; endpoint_factorial_kernel_stderr.txt; bernstein_difference_identity_verification.json; bernstein_difference_verifier_stdout.txt; bernstein_difference_verifier_stderr.txt; ENDPOINT_FACTORIAL_KERNEL_REPORT.md.
