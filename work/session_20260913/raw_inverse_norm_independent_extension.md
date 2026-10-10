> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent inverse-norm audit and the actual mixed-parity determinant obstruction

Date: 2026-09-13. Reviewer/continuation: audit_results.
Dependencies: `raw_arctan_inverse_norm_attempt.md`, the independently
checked dual mass theorem, and the exact raw Delta_B normalization.

## Outcome

The inverse-norm note's exact formulas and the constant



$$
\|Z_n\|_2\sim\sqrt{2/\pi}\,e^{-1/2}4^n n!
$$



pass independent review. I did not obtain the missing estimate
delta_n>=exp(-O(n))/n!.

The constructive continuation proves three precise facts.

1. In every degree n>=3, two explicit maximal coefficient minors of
   the actual high block F_(n+1),...,F_(2n-1) have opposite signs.
   Consequently the Cauchy--Binet expansion of its actual mixed moment
   minors against increasing monomials has positive and negative terms
   in every degree. Positivity of the separated-parity minors cannot
   be used to drop the other terms.
2. The natural first-minor contribution has logarithm
   -(1/2)n^2 log n+O(n^2) after normalization of the individual rows.
   Retaining this one term while bounding competing volumes by rowwise
   Hadamard estimates therefore loses a quadratic-logarithmic scale.
   This is a limitation of that specific estimate, not a theorem that
   all coherent determinant-quotient methods must lose that scale.
3. An exact determinant identity connects the residual problem directly
   to the actual Delta_B. The known dyadic lower bound alone gives only
   a -(7/2)n^2 log n+O(n^2) lower bound for the relevant functional
   determinant, far short of the needed comparison with its cofactors.

These results identify why the proposed fixed-positive-minor shortcut
does not complete the desired norm bound. They do not rule out a
quantitative estimate that retains cancellation and common volume factors.

## 1. Independent check of the factorial endpoint representer

For J_k(x)=P_k(2x-1),



$$
J_k^{(j)}(1)=\frac{(k+j)!}{(k-j)!j!}.
$$



Therefore the coefficient b_k=beta_n(J_k) and the Riesz representer
Z_n=sum_(k<=n)(2k+1)b_k J_k in the source note are exact. The identity
beta_n(x^j)=(-1)^j D_j also follows directly by reversing the finite
derivative sum; the endpoint functional is not point evaluation.

Put A_k=(2k)!/k!. The reversed alternating expression for b_k has
summand magnitudes



$$
\frac1{r!}\frac{(k)_{\underline r}}{(2k)_{\underline r}}.
$$



Their consecutive ratio is (k-r)/((r+1)(2k-r)), at most
1/(2(r+1)). The alternating sum lies between1/2 and1, and domination
by 2^(-r)/r! gives its limit e^(-1/2). Since
A_(k-1)/A_k=1/[2(2k-1)], the sum of all lower squared Legendre
coefficients is O(n^(-2)) relative to the final one. Combining



$$
A_n=\binom{2n}{n}n!\sim4^n n!/\sqrt{\pi n}
$$



with sqrt(2n+1) verifies the exact constant sqrt(2/pi)e^(-1/2).
No additional factor n!, n, or2 is missing.

## 2. Independent check of the projection and norm identities

The actual equations are the n-1 high moments, the T_n moment equal
to-4, and beta_n(P)=1. Their established independence implies that
S_n=span(projected high F_k,T_n+4Z_n) has dimension n in P_n and that
Z_n is outside S_n. Orthogonal projection is necessary because the high
F_k have degree greater than n.

The complement of S_n is one-dimensional, so the exact normalized
solution is



$$
P_n=Z_n^\perp/\|Z_n^\perp\|_2^2.
$$



The Schur-complement quotient and the two-dimensional area formula in
the source note follow with the displayed order of numerator and
denominator. In the latter, replacing t by t+4z leaves its squared
area with z unchanged. The norm comparison
||P||_1<=||P||_2<=(n+1)||P||_1 is also correct: the shifted Legendre
kernel bounds ||P||_infinity by(n+1)||P||_2.

Thus the requested factorial upper bound for M_n is equivalent, within
exponential factors, to delta_n>=exp(-O(n))/n!. The earlier factorial
mass lower bound implies the opposite inequality for delta_n and does
not settle this target.

## 3. Two opposite maximal coefficient minors in every degree

Let m_sigma count the high indices k in[n+1,2n-1] of parity sigma.
For each parity list these indices increasingly as h_0,...,h_(m-1),
write lambda_j=h_j(h_j+1), and put



$$
\mu_a=(2a+\sigma)(2a+\sigma+1),\qquad
 p_r(X)=\prod_{a=0}^{r-1}(X-\mu_a).
$$



After dividing each row F_(h_j) by its positive lowest coefficient
q_(h_j,sigma), its coefficient at x^(2r+sigma) is



$$
\frac{p_r(\lambda_j)}{((2r+\sigma)!)^2}.                  \tag{1}
$$



For the first m columns r=0,...,m-1, the determinant is exactly



$$
D_\sigma=
 \frac{\prod_{0\le j<a<m}(\lambda_a-\lambda_j)}
      {\prod_{r=0}^{m-1}((2r+\sigma)!)^2}>0.              \tag{2}
$$



This is the ordinary Vandermonde determinant after unitriangular
column changes between monic polynomial bases.

Now replace only the final column r=m-1 by r=m. The determinant of
the polynomial numerators becomes



$$
\prod_{j<a}(\lambda_a-\lambda_j)
 \left(\sum_{j=0}^{m-1}\lambda_j-
                  \sum_{a=0}^{m-1}\mu_a\right).         \tag{3}
$$



To verify(3), first change the initial columns to1,X,...,X^(m-2).
The last polynomial has top terms X^m-(sum mu_a)X^(m-1).
The two resulting alternants are Vandermonde times sum lambda_j and
Vandermonde respectively. All lower-degree terms contribute zero.
This includes m=1. The parenthesized factor is strictly positive:
every high node lambda_j is greater than every mu_a appearing here.
The factorial denominators and the removed row normalizations are
positive, so the changed separated-parity minor remains positive.

Consider the full coefficient matrix with rows F_(n+1),...,F_(2n-1)
in increasing degree order. Let I_0 consist of the first m_0 even powers
and the first m_1 odd powers, in increasing order. Let I_1 be obtained
by increasing its largest even power by2, with every other power fixed.
Both selected maximal minors are nonzero by(2)--(3).

For odd n=2r+1, m_0=m_1=r. The changed even power moves from2r-2
to2r and crosses exactly the odd power2r-1. For even n=2r>=4,
m_0=r-1 and m_1=r; the changed even power moves from2r-4 to2r-2
and crosses exactly the odd power2r-3. These cases cover every n>=3.

Permute rows and columns into parity blocks. The row permutation is
the same for both minors. The within-parity determinants are positive,
while the two column permutations differ by one transposition. Hence



$$
\boxed{\det A_{I_0}\,\det A_{I_1}<0\qquad(n\ge3),}       \tag{4}
$$



where A is the coefficient matrix of the actual high block. In both
cases the selected columns have degree at most n-1, so the example
does not depend on selecting remote tail columns.

This is an all-index coefficient-minor theorem. It does not assert that
the full collocation determinant changes sign in every degree, and it
does not upgrade the earlier finite Chebyshev counterexamples into an
all-index Chebyshev failure theorem.

## 4. Consequence for the actual moment Cauchy--Binet expansion

Let J be any increasing list of n-1 nonnegative integer monomial
degrees, and form the mixed moment matrix



$$
C_{k,j}=\int_0^1F_k(x)x^j\,dx,
 \qquad n+1\le k\le2n-1,\quad j\in J.
$$



It is A times the monomial moment matrix with entries1/(d+j+1).
For increasing lists I,J, its Cauchy minor is strictly positive:



$$
\det\left(\frac1{i+j+1}\right)_{i\in I,j\in J}
 =\frac{\prod_{i<i'}(i'-i)\prod_{j<j'}(j'-j)}
        {\prod_{i\in I,j\in J}(i+j+1)}>0.                \tag{5}
$$



The two terms indexed by I_0 and I_1 in the exact Cauchy--Binet sum
for det C therefore have opposite signs, by(4). This applies in
particular to monomial test degrees drawn from0,...,n, the actual
projection target. Consequently this determinant expansion is not a
sum of nonnegative spectral contributions in any of the degrees n>=3.

A Gram determinant is positive, and a Cauchy--Binet expansion after
orthonormalization is a sum of squares. But those squares contain the
mixed moment determinants, hence the cancellation just identified.
One cannot replace such a squared mixed determinant by the square of
one of its positive summands as a lower bound. The separate parity
positivity is real; this final inference is the invalid step.

## 5. Quantified loss in retaining the first coefficient minor alone

For the individually normalized rows f_k=F_k/q_(k,k mod2), the magnitude
of the I_0 coefficient minor is exactly D_0D_1 from(2). Since all high
indices are between n+1 and2n-1,



$$
\lambda_a-\lambda_j=2(a-j)(h_a+h_j+1),
$$



and h_a+h_j+1 is between constant multiples of n. Stirling summation
in(2) gives, for m=m_sigma=n/2+O(1),



$$
\log D_\sigma=-m^2\log n+O(n^2).
$$



For completeness, the Vandermonde numerator has logarithm
m^2 log n+O(n^2): its two contributions are
(m(m-1)/2)log n and sum_(a=1)^(m-1)log(a!). The squared factorial
denominator has logarithm2m^2 log n+O(n^2). Therefore



$$
\boxed{\log|\det A^{\rm normalized}_{I_0}|
       =-\tfrac12n^2\log n+O(n^2).}                     \tag{6}
$$



Each normalized even row is at least1 on[0,1], and each odd row is at
least x. Its positive coefficients and(1) also give



$$
\|f_k\|_2\le f_k(1)
 \le\sum_{d\ge0}\frac{(k+1)^d}{(d!)^2}
 \le e^{2\sqrt{k+1}}.
$$



The last inequality follows by including the diagonal terms in
(sum_(d>=0)(sqrt(k+1))^d/d!)^2. The same bounds hold for the Euclidean
coefficient-row norm, with a constant lower bound. Thus a rowwise
Hadamard product has logarithm O(n^(3/2)), whereas the fixed first
minor has the quadratic-logarithmic loss in(6).

For the Euclidean coefficient Gram A A^T, Cauchy--Binet really is a
positive sum of squared minors. Keeping just I_0 is a valid lower
bound there, but comparing that one term with a rowwise Hadamard upper
bound loses exp(-(1+o(1))n^2 log n) at the squared-volume level.
This rigorously quantifies the weakness of that fixed-term estimate.
It is not yet a bound for the projected endpoint residual.

The shared small high-row volume could cancel in a carefully controlled
quotient. Nothing here rules out that possibility. An estimate that
preserves such cancellation, together with the two actual endpoint
directions, is exactly what remains to be proved.

## 6. Exact return to the actual endpoint determinant

Let L_n be the (n+1)-by-(n+1) functional matrix on the monomial basis
1,x,...,x^n. Its rows are the n-1 high pairings, the T_n pairing, and
beta_n, in that order. Put D_n=det L_n. This D_n is not the dyadic
valuation quantity denoted D_n in the archived arithmetic note.

Let Delta_(B,n) be the original integral high-jet augmented determinant
from that note. With the raw norms h_j, the exact relation is



$$
\boxed{|D_n|=
 \frac{|\Delta_{B,n}|\prod_{j=0}^n j!}
 {\left(\prod_{k=n+1}^{3n}k!\right)
             \left(\prod_{j=0}^n|h_j|\right)}.}          \tag{7}
$$



To prove this, first divide the integral high rows by k! and reverse
the C columns. Their moment block is L(t^(r+j)), 0<=r,j<=n.
Unitriangular changes to the monic Q_r basis diagonalize this block,
with determinant product h_j. Elimination of C leaves exactly the
high ell_B(Q_k) rows, the negative row ell_B(K_n(1,t))+4B(1), and
B(1). Removing the multiple4 of the last row and ignoring its sign
leaves the high rows, the T_n pairing, and beta_n.

Finally the coefficient change B->P_B has determinant
1/product_(j=0)^n j!. Its reversal sign and the product of the leading
signs (-1)^j cancel. This gives(7), including its factorial factors.

The known all-degree valuation implies |Delta_(B,n)|>=2^(d_n), where
d_n=3n^2+O(n log n). The explicit norm product contributes only O(n^2)
to the logarithm. Hence (7) gives only



$$
\log|D_n|\ge-\tfrac72 n^2\log n+O(n^2).                 \tag{8}
$$



This is a valid, very weak Archimedean bound. The exact dyadic
nonvanishing statement does not supply the larger value needed for a
factorial-scale inverse estimate.

## 7. The coherent cofactor quotient that avoids artificial Gram losses

Let H be the (n+1)-dimensional monomial Hilbert matrix. Replace the T
row of L by T+4 beta and let A consist of all rows except beta. Let a
be the signed vector of its maximal cofactors, with signs chosen so
that beta*a=det L=D_n. Then the actual monomial coefficient vector is



$$
P_n=a/D_n,
 \qquad \boxed{\delta_n=\frac{|D_n|}{\sqrt{a^T H a}}.}    \tag{9}
$$



Indeed A a=0, and beta(P_n)=1. This is the same normalization and
residual as in the source Gram formula. The full representer Gram
determinant is D_n^2/det H, because the functional row matrix is the
coefficient row matrix multiplied by H. Thus its apparent large
Hilbert-determinant factor must cancel coherently; estimating the two
Gram determinants independently can introduce a spurious quadratic
loss.

Since lambda_max(H)<=n+1, one sufficient quantitative target is



$$
\frac{|D_n|}{\|a\|_2}\ge\frac{e^{-Cn}}{n!}.
$$



The polynomial factor sqrt(n+1) is immaterial at this scale. Neither
(7) nor a positive coefficient-Gram summand proves this cofactor
comparison. The missing work concerns the actual bordered determinant
relative to its cofactors, or equivalently the projected endpoint
angle; it is not removed by rewriting that quantity as a positive Gram
quotient.

## 8. Independent controls and scope

`check_raw_inverse_extension.py` constructs all objects by exact
rational arithmetic at the predeclared n=1,3,5. It checks the Riesz
identity against every monomial, its exact norm, the source Gram
quotient, the cofactor formula(9), and the factorial/Delta_B bridge(7)
against a separately assembled original integral high-jet matrix.
At n=3,5 it also verifies both explicit opposite maximal minors.
All controls pass; results are in `raw_inverse_extension_checks.json`.

The all-index proofs of(4), (6), (7), and(9) do not depend on those
finite controls. No factorial upper bound for M_n, lower bound for
the actual cancellation ratio, or primitive shrinking theorem was
obtained in this continuation.

Audit_computations independently reviewed the all-index opposite-minor
proof and the Delta_B bridge. It accepted the exact Vandermonde factor,
the one-column crossing in both parities, all factorial normalization
factors, and the -(7/2)n^2 log n scale. No gap was found.
