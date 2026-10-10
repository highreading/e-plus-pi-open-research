> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the actual low-plus-sparse-bulk union theorem

Date: 2026-09-13. Reviewer: audit_results.
Source: raw_low_bulk_union_theorem.md by audit_sources.

The complete proof passes. I checked the exact physical and normalized
columns, the even-cut localization uniformly over every high row,
the growing low-block inverse, the full-prefix Gram subtraction,
the rectangular Schur estimate, the stated conditioning constant,
and the selected square minor with its relative determinant factor.
No substantive correction is required.

This is an actual joint-independence theorem. Its proof uses a new
interaction estimate between the two column families; it does not
infer independence of their union from two separate rank statements.
The selected sizes, row regions, and physical scaling losses are
kept explicitly, so the theorem does not cover the full high matrix.

## 1. Exact columns and inherited quantitative inputs

The physical entry is
H_(k,ell)=g_ell p_k^(ell mod2)(xi_ell)=<E_k,psi_ell>.
For a low node, dividing by psi_ell(1)L_(2n) gives exactly

    V_(k,ell)=(L_k/L_(2n))M_(k,ell).

The endpoint value is nonzero, and any sign is a harmless
orthogonal column sign for singular values. This normalization
does not replace g_ell by an asymptotic amplitude; it uses the
exact moment identity.

For the bulk columns the retained diagonal is exactly the one
in raw_actual_sparse_bulk_matrix_theorem.md: g_(l_i), the scalar
s_(2n)(xi_(l_i)), and the even-cut powers x^(3/2),x. Thus B
is that theorem's normalized feature matrix, and its lower
singular-value and O(sqrt(b)) upper norm bounds apply directly.
The fixed bulk constants remain independent of the growing
number b=floor(kappa log n).

I compared the low input to Section6 of
raw_growing_low_node_minor_theorem.md. Its actual least-singular-
value estimate is precisely the one used in (11), with its
exp(−C m²log(m+1)) prefactor and n^(-(m−1)/2) factor retained.
For m=floor((log n)^(1/3)) the relative determinant error tends
to zero, so the lower bound applies for all sufficiently large n.
The source does not reuse a fixed-m constant as a uniform one.

## 2. Even-cut localization applies uniformly to the whole high interval

For each k in n+1,...,2n−1, the largest even N<=k satisfies
n<=N<=2n−2, and row k is one of the two rows of P_N. This
remains true for either parity of n. The other row in that
two-row matrix need not be selected, which causes no problem.

For every selected bulk parameter x, the actual spectral bounds
give

    alpha²/4 <= x/N² <= (beta+1)².

Thus one fixed positive compact parameter interval controls
all N, k and selected nodes simultaneously. The accepted
even-cut column theorem gives a uniform bound once N>=n
is sufficiently large; no assertion for a fixed cut followed
by a moving-parameter extrapolation is used here.

Both cuts N and2n are even, so their distinct column powers
are the same and cancel exactly. Their scalar-product quotient is

    s_N(x)/s_(2n)(x)
      =sqrt(2n/N) product_(j=N+2,step2)^(2n) q(x/j²).

Every j is at most2n, so x/j²>=alpha²/4 and monotonicity of q
bounds every factor by q(alpha²/4). There are exactly(2n−N)/2
factors. With rho=sqrt(q(alpha²/4)), this gives rho^(2n−N),
which is at most rho^(2n−k) because N<=k. The square-root
prefactor is at most sqrt2. This proves the entry bound (8)
with the actual parity component, not with an artificially
common column power.

Summing squares over the whole prefix gives a geometric series
and a factor sqrt(b). The Hilbert–Schmidt norm bounds the
operator norm, proving (9) for arbitrary bulk coefficient
combinations. In particular the same t_n bounds both B_R and
the full prefix B_[n+1,...,K]. This latter point is the bound
used in the subsequent Gram subtraction; (9) supplies it.

## 3. Growing row sets, row masses and the selected low inverse

The last interior-grid row satisfies exactly

    k_m=floor(2n−n/(m+1))=2n−ceil(n/(m+1)).

For sufficiently large n the grid rows are distinct and lie
strictly inside the high interval. Its top complement T has
d−1 rows with d=ceil(n/(m+1)), so |T|>b eventually. All row
restrictions used by the Schur argument therefore have the
claimed dimensions and are disjoint.

The reviewed row-mass asymptotic is uniform for n<=k<=2n:

    L_k/L_(2n)
      =(2n/k)^(3/4)exp(2sqrt(k)−2sqrt(2n))
         (1+O(n^(-1/2))).

The prefactor lies in a fixed positive interval, and the
exponential is between exp(−a sqrt(n)) and1, where
a=2(sqrt2−1). This proves (12) without assuming that L_k is
monotone. Multiplying the selected low matrix by this exact
positive row diagonal proves sigma_min(A_0)>=a_n.

The uniform endpoint estimate |M_(k,ell)|<=2E_m holds for
every high row, not just the selected ones: M is the expectation
of the endpoint-normalized eigenfunction against the positive
row density E_k/L_k. Its uniform sup bound is the one proved
using the endpoint recurrence and reflection. Combining it
with (12) gives ||V||<=C E_m sqrt(nm)=M_n, as asserted.

For the bulk Gram,

    B_T^T B_T=B^TB−B_prefix^T B_prefix.

The removed positive term has norm at most t_n². Since t_n
decays like exp(−gamma n/(m+1)) up to a logarithmic factor,
it is smaller than the polynomial bulk lower bound. Thus
sigma_min(B_T)>=(c_B/2)n^(-theta/2) holds eventually. This
subtraction is for the full prefix, not merely for R.

## 4. The actual mixed Schur correction and conditioning constant

The restriction to rows R followed by T is the rectangular block
matrix [[A_0,E],[C,B_T]], with A_0 square and invertible. Its
Schur correction has exactly the bound M_n t_n/a_n. Dividing
by b_n gives eta_n as stated in (17).

The logarithm of that bound is at most

    −gamma n/(m+1)+a sqrt(n)+(m−1)log(n)/2
       +C m²log(m+1)+4m+O(log n).

For the stipulated m every positive term is o(n/(m+1)). This
justifies the eventual bound eta_n<=exp(−gamma n/(2(m+1)))
with fixed constants and all rounding errors absorbed. The
rectangular singular-value perturbation inequality then gives
sigma_min(B_T−C A_0^(-1)E)>=b_n/2.

The two block equations prove injectivity exactly as stated.
For the quantitative version, solving them gives

    ||v|| <=(2/b_n)(1+M_n/a_n)||z||,
    ||u|| <=a_n^(-1)||z||+(t_n/a_n)||v||.

Since eta_n<=1 eventually, b_n<=1 and M_n>=1 imply
t_n/a_n<=1. Bounding the Euclidean pair norm by the sum
of the two component norms therefore gives

    ||(u,v)|| <=[1/a_n+4/b_n+4M_n/(a_n b_n)]||z||
               <=9M_n/(a_n b_n)||z||.

This verifies the displayed constant9. Adding back omitted rows
can only increase the least singular value, so (19) holds for
the full normalized union. Its remaining logarithmic losses are
o(sqrt(n)), proving the stated exp(±C sqrt(n)) conditioning
scale in exactly that normalization.

Finally H_union=U times its exact diagonal column scaling. The
least-singular-value loss min|d_i| and condition-number loss
max|d_i|/min|d_i| in (20) are the correct safe inequalities.
The source does not absorb those possibly much larger physical
factors into its normalized constant C.

## 5. Maximum-volume bulk row selection and its inverse

The maximum-volume b-row subset J exists because T is finite.
Since B_T has b singular values at least b_n, finite Cauchy–Binet
gives

    sum_(|J|=b)(det B_J)²=det(B_T^TB_T)>=b_n^(2b).

Therefore the maximizing determinant has magnitude at least
b_n^b/sqrt(binomial(|T|,b)). The estimate binomial(|T|,b)<=n^b
gives (21). This is an existence argument, not a claim to have
performed a numerical maximizing row search.

Because ||B_J||<=C_B sqrt(b), the exact product of its singular
values yields

    sigma_min(B_J)>=|det B_J|/(C_B sqrt(b))^(b−1).

With b=O(log n) and b_n a fixed inverse power of n, its logarithm
is bounded below by −C(log n)². This proves the usable b'_n
bound without assuming a stronger well-conditioned row selection.

The new correction with B_J^(-1) has norm at most
M_n t_n/(a_n b'_n). Its additional O((log n)²) logarithmic
loss is still o(n/(m+1)), so the same eventual exponential
decay in (23) is valid.

## 6. Relative square-minor factorization and the remaining scope

The block determinant formula in the row order [R,J] is exactly

    det U_[R,J]=det A_0 det B_J
      det(I−B_J^(-1)C_J A_0^(-1)E).

All matrices are real. If the correction norm is below1, the
path I−t times that correction, 0<=t<=1, is nonsingular;
its determinant consequently stays positive. Its singular values
lie between1−eta'_n and1+eta'_n. Therefore the absolute value
of the logarithm of its determinant is at most2b eta'_n for
eta'_n<=1/2. This verifies the relative determinant statement
even though the main determinant can be very small.

The exact low row factors in det A_0 and the low column factors
in (2) combine to product_j L_(k_j) times product_(ell<m)psi_ell(1).
The bulk column factors retain g_(l_i), s_(2n), and the two
different powers of xi_(l_i). The displayed factorization does
not replace det B_J by an unproved local scalar approximation.

The theorem thus proves joint independence and quantified normalized
conditioning for these two growing selected families. Intermediate
nodes, a full-density bulk selection, and the full high-row inverse
remain outside the proved range. The amplitude-weighted cardinal
angle and the primitive remainder are not consequences of the
restricted union theorem alone.
