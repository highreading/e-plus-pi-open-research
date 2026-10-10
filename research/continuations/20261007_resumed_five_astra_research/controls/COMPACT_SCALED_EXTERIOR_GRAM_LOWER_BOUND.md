> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Retaining the exterior Gram matrix sharpens the whole determinant lower bound

Coordinator derivation, 7 October2026. Research ACTIVE. This is a refinement
of A3turn13, awaiting independent review; it is not an irrationality theorem.
The complete mixed block identity and A5's compression/upper bound have already
been independently accepted by A4turn17. The new A3 global sign proof is under
A4turn18 review. No finite numerical sign grid or remote code is used here.

## Overlap and classical ingredients

The scoped archive search of A3turn13, A5turn12, A4turn16 and the parent's contact
note finds the exterior extrapolation lemma and a Hilbert comparison on[0,1],
but no retained exterior Gram determinant. The refinement below is an immediate
consequence of that existing lemma. It does not claim a new classical determinant
identity. Cauchy's double alternant and its Hilbert specialization are reused
from Krattenthaler, *Advanced Determinant Calculus*, section2.1, equation(2.7),
personally inspected on 7 October2026:
https://arxiv.org/html/math/9902004v3 .
The scoped search supplies no assertion of absence from all literature.

## Exact finite-degree estimate

Retain L=mu-delta_(-1), the original compact nu, and for y in[0,1]^k set
Q_y(x)=product_j(x-y_j). Put I_k=[k^2,4k^2], and for deg p<=k-1 define



$$
E(p)=\int_{I_k}p(x)^2\,dx,\qquad
 M(p)=\max_{[-1,1]}|p|.
$$



The Legendre expansion in A3turn13 proves



$$
M(p)^2\le K_k E(p),\qquad K_k=16^{k-1}/3.
$$



On I_k, Q_y>=(k^2-1)^k and the exact density of mu is
e^(-1-sqrt(x))/(2sqrt(x))>=e^(-1-2k)/(4k). Thus its positive contribution is
at least c_k E(p), where



$$
c_k=\frac{(k^2-1)^k}{4k e^{1+2k}}
 >\frac1{12k}\left(\frac{k^2-1}{9}\right)^k=:c'_k.
$$



This uses e<3. The remaining x>1 contribution is nonnegative. On[0,1],
|Q_y|<=1 and mu has mass at most1; the negative atom has magnitude at most
2^k M(p)^2. Consequently the SAME complete signed functional satisfies



$$
L(p^2Q_y)\ge[c'_k-(1+2^k)K_k]E(p)=\alpha_k E(p),
$$



where



$$
\alpha_k=K_k\gamma_k,\qquad
 \gamma_k=\frac4k\left(\frac{k^2-1}{144}\right)^k-1-2^k.
$$



A3's exact all-k argument gives gamma_k>0 for every k>=32: since
(k^2-1)/288>3, the positive term exceeds (4/k)2^k 3^k>=4*2^k.
The improvement is to keep E(p) itself, instead of replacing it by the much
smaller compact norm integral_0^1 p^2.

## The exterior determinant pays its entire affine scaling

Let B_k(I)=(integral_I x^(a+b) dx)_(0<=a,b<k) and
M_y=(L(x^(a+b)Q_y))_(0<=a,b<k). The preceding inequality gives
M_y>=alpha_k B_k(I_k) in positive-semidefinite order. Since alpha_k>0,



$$
\det M_y\ge\alpha_k^k\det B_k(I_k).
$$



For an interval[A,A+ell], substituting x=A+ell t changes the monomial frame
by a triangular matrix with diagonal1,ell,...,ell^(k-1), and the integration
measure contributes ell to each matrix entry. Therefore



$$
\det B_k([A,A+\ell])=\ell^{k^2}\mathfrak h_k,
 \quad \mathfrak h_k=\det(1/(a+b+1))
 =\frac{\prod_{j=0}^{k-1}(j!)^4}{\prod_{j=0}^{2k-1}j!}.
$$



This also follows immediately from the classical Cauchy identity. With ell=3k^2,



$$
\boxed{\det M_y\ge
 (K_k\gamma_k)^k(3k^2)^{k^2}\mathfrak h_k.}
$$



Integrate the exact signed conditional determinant identity, with all moments
through3k-2 retained. The result for the EXISTING integer affine block is



$$
\boxed{(-1)^kH_k(e+\pi)\ge
 \Lambda_k^kJ_k^\nu(K_k\gamma_k)^k
 (3k^2)^{k^2}\mathfrak h_k>0\qquad(k\ge32).}
$$



Its ratio to A3turn13's stated lower bound is exactly
K_k^k(3k^2)^(k^2), a genuine determinant-scale improvement. It is not a
denominator charge or an integer basis change.

## Matching the leading raw growth and sharpening the remaining target

The complete compact density is
(e^(sqrt(x))+4/(1+x))/(2sqrt(x))>=3/2 on(0,1). Thus
J_k^nu>=(3/2)^k mathfrak h_k. Standard factorial sums in the displayed Hilbert
formula give log mathfrak h_k=-2(log2)k^2+O(k log k). Also
log gamma_k=2k log k-(log144)k+O(log k) and
log K_k=(log16)k+O(1). Since Lambda_k>=1, the new lower bound implies



$$
\log|H_k(e+\pi)|\ge4k^2\log k-O(k^2).
$$



Together with the already accepted A5turn12 upper bound
log F_k^perp=4k^2 log k+O(k^2), this establishes the matching leading raw scale



$$
\boxed{\log|H_k(e+\pi)|=4k^2\log k+O(k^2).}
$$



It does NOT establish primitive divergence. For the actual final
G_k=gcd(|H_0|,|H_1|), the error is |H_k(e+pi)|/G_k. Primitive decay would
necessarily require log G_k>=4k^2 log k-O(k^2) on that same infinite set.
An evaluated upper bound log G_k<=(4-epsilon)k^2 log k+O(k^2), with fixed
epsilon>0, would now prove actual primitive divergence for this family. No such
upper bound is claimed. The known D_(k-1) lower divisor, whose logarithm has
leading coefficient1, is not the final G and cannot be substituted for it.

This refinement leaves the original producer families and their distinct actual
primitive pairs unchanged. Its applicability is all compact integers k>=32.
