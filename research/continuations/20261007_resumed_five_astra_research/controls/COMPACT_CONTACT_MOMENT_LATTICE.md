> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact even-contact moment lattice: sign, size, and saturation

Parent derivation, 7 October 2026. Research remains ACTIVE. This note proves
structural facts about a newly specified compact contact family, not irrationality.
The underlying gamma-integral charge is already derived in A2turn11. Basic
mixed integration-by-parts matching overlaps the archive and arXiv2606.17303.
Hankel moment determinants, reproducing kernels and rank-one mass modifications
are standard orthogonal-polynomial tools; novelty of those tools is not claimed.
The targeted primary check includes https://dlmf.nist.gov/18.2#ix and the
related determinant literature https://arxiv.org/abs/2103.03969. The latter's
rational-density theorem is not being invoked as a point-mass theorem.

## 1. The actual contact matrix

Let a_d=sum_{j=0}^d (-1)^j d!/(d-j)! and A(P)=sum_j(-1)^j P^(j)(1).
The already established identity gives



$$
A(P)=\int_0^\infty e^{-u}P(1-u)\,du.
$$



Push the probability measure e^(t-1)dt on (-infinity,1] through x=t^2.
Call the resulting positive measure mu. It has infinite support in [0,infinity),
all finite moments, and mu_k=a_(2k). For P(t)=p(t^2), the k-contact constraints
from A5turn10 are exactly



$$
\int x^j p(x)\,d\mu(x)=(-1)^j p(-1),\qquad 0\le j<k.
$$



Put c_j=a_(2j)-(-1)^j, B_k=(a_(2i+2j))_(0<=i,j<k),
v=(1,-1,...,(-1)^(k-1))^T, and C_k=(c_(i+j))=B_k-vv^T.
This is the COMPLETE contact functional, not just its factorial summand.

## 2. Nonsingularity at every size k>=2

B_k is positive definite. Its reproducing-kernel value at -1 is
K_k=v^T B_k^(-1)v, equivalently the supremum of |p(-1)|^2/integral p^2 dmu
over nonzero polynomials of degree less than k. The polynomial spaces are nested.
For k=2,



$$
B_2=\begin{pmatrix}1&1\\1&9\end{pmatrix},\qquad K_2=3/2.
$$



Hence K_k>=3/2 for every k>=2. The exact determinant identity is



$$
\det C_k=(1-K_k)\det B_k<0.
$$



Congruence by B_k^(-1/2) also shows that C_k has exactly one negative eigenvalue
and k-1 positive eigenvalues. C_1=(0) is exceptional and is not silently included.
Thus all k contact equations are independent for k>=2.

## 3. An explicit infinite family of contact rows

For every m>=k, let w_m=(c_m,...,c_(m+k-1))^T and define



$$
p_m(x)=x^m-(1,x,...,x^{k-1})C_k^{-1}w_m.
$$



Every p_m obeys ALL k contact equations. The rows m=k,...,2k-1 have distinct
degrees and form a rational basis of the contact space of degree at most 2k-1.
Let d_m be the ACTUAL lcm of the reduced denominators of C_k^(-1)w_m.
Then d_m p_m is a primitive integer polynomial: a common divisor of all its
coefficients would contradict the minimality of d_m. This supplies independent
primitive integer rows, but does not assert that they are a saturated integer
basis. Their finite lattice index must still be paid.

At k=2 these formulas give exactly
p_2=x^2-4x-117 and p_3=x^3-133x-6884, the two previously checked rows.
The compact moment matrix of p_m(t^2)t^(2j) has period part
p_m(-1)(-1)^j(e+pi). This has rank one. Its square determinant is therefore
an AFFINE rational polynomial in e+pi at every size. Nonvanishing of C_k does
not prove nonvanishing of this DIFFERENT evaluated compact determinant.

## 4. Exact saturation payment

Let W=(w_k,...,w_(2k-1)), and let delta_k be the gcd of all k-by-k minors of
[C_k | W]. The image of this integer matrix has index delta_k in Z^k.
The allowed high-coefficient lattice is



$$
L_k=\{h\in\mathbb Z^k:Wh\in C_k\mathbb Z^k\}.
$$



The map h -> Wh mod C_k Z^k is onto im[C_k|W]/C_k Z^k, so



$$
[\mathbb Z^k:L_k]=|\det C_k|/\delta_k.
$$



This ratio retains all primes and is the exact high-coefficient saturation
payment. The raw determinant |det C_k| is NOT the least clearer of every row,
nor the final gcd of the compact determinant's two scalar coefficients.

## 5. Raw contact-determinant height

The raw contact matrix has the precise leading height



$$
\log|\det C_k|=2k^2\log k+O(k^2).
$$



For the lower bound, B_k is the Gram matrix on t<=1. Restricting to t=-s<=0
gives B_k>=e^(-1)E_k in positive-semidefinite order, where E_k=((2i+2j)!).
Andreief expresses det E_k as 1/k! times the nonnegative multiple integral
of exp(-sum s_i) times the squared Vandermonde of s_i^2. Restrict s_i to
[i,i+1/4], i=1,...,k, and use all k! permutations of these disjoint boxes.
The 1/k! cancels. On these boxes,



$$
s_j-s_i\ge\tfrac34(j-i),\qquad s_i+s_j\ge i+j.
$$



Thus the logarithmic lower bound is



$$
2\sum_{j=1}^{k-1}\log(j!)+2\sum_{j=2}^k(j-1)\log j-O(k^2)
=2k^2\log k-O(k^2).
$$



Also |det C_k|=(K_k-1)det B_k>=det B_k/2.
For the upper bound, positivity of adj(B_k) implies
|adj(B_k)_(i,j)|<=sqrt(adj(B_k)_(i,i) adj(B_k)_(j,j)).
Each diagonal cofactor is at most the product of the other diagonal entries
by Hadamard, and all B_(i,i)=a_(4i)>=1. Consequently



$$
|\det C_k|\le(1+k^2)\prod_{i=0}^{k-1}a_{4i}
\le(1+k^2)\prod_{i=0}^{k-1}(4i)!.
$$



Stirling gives the same leading term 2k^2 log k. This proves the statement.
It quantifies raw contact height only. It DOES NOT rule out cancellation in
delta_k, small actual invariant factors, or the final scalar gcd.

## 6. Remaining obligations

The next arithmetic targets are delta_k and the actual contact-row clearers,
followed by nonvanishing and the primitive coefficient-pair gcd of the compact
moment determinant. Its whole evaluated error must be estimated after those
payments. No theorem here supplies 0<|q_k(e+pi)-p_k|->0.
