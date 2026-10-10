> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rational Stieltjes approximation and displacement bounds: actual applicability

Date: 2026-09-13. Focused primary-source review following the project's
independent dyadic rational-surrogate derivation. These sources provide
context and possible constant improvements; the new rank proof does not
depend on importing an unverified singular-value lower bound from them.

## Primary results read

**Beckermann–Townsend (2017).** Theorem 2.1, pp.3–4 of the
[primary manuscript](https://arxiv.org/pdf/1609.09494), proves
sigma_(j+nu k)(X)<=Z_k(E,F)sigma_j(X) when A,B are normal,
AX-XB has rank at most nu, and their spectra lie in E,F. The proof
constructs a rank-nu k rational displacement correction. Corollary 2.2
replaces normality by controlled spectral sets. These are upper bounds
on later singular values; they do not give a least-singular-value lower
bound or prove an otherwise unknown rank. For the full reflection
commutator, the same K occurs on both sides, so the two spectral sets
coincide and this theorem alone supplies no decay. For separated
spectral blocks it can give useful upper bounds, still with the actual
block norm present. The author-hosted Cornell URL returned404; the
arXiv primary manuscript was read instead.

**Massei–Robol (2020).** Theorem 3.4 (p.6), Corollary 3.14 (p.10),
and Corollary 3.18 (p.11) in the
[primary manuscript](https://arxiv.org/pdf/1908.02032) treat rational
Krylov approximation of resolvents and Cauchy–Stieltjes functions of
Hermitian positive definite matrices. With their prescribed poles,
Corollary 3.18 bounds the vector approximation error by
8 f(a)||v|| rho_[a,4b]^ell, where
rho_[alpha,beta]=exp(-pi^2/log(4beta/alpha)).
The selected theorem and its dependency definitions were read, not the
whole paper independently reproved. The theorem concerns a rational
Krylov approximation to a vector. Its numerator/space can depend on
that vector, so it cannot silently replace a common scalar rational
function for every polynomial multiplier in the present proof.

**Braess–Hackbusch (2026 issue, published December29,2025).**
Theorem 4.6 and Section4.3.1 of
[the primary article](https://link.springer.com/article/10.1007/s00211-025-01523-1)
give a common rational approximant to a Cauchy–Stieltjes function on a
positive interval, with error at most2 sigma_(2r) f(0), under the
explicit hypothesis f(0)<infinity. The coefficient sigma is expressed
through the rational relative-approximation error defined in (4.7).
The preceding interpolation discussion keeps positive pole parameters.
This is a relevant scalar alternative; the displayed theorem and local
definitions were inspected. Its result still controls approximation
error, rather than the residual determinant or arithmetic denominator.

## Independent specialization to the actual family

Let M=2n+1, H=M I-K_(2n), and use the original cutoff
ceil(2sqrt(n)). The actual positive partial fractions show that

    f(y)=1-R(M-y)=sum_i c_i/(beta_i-M+y)

is Cauchy–Stieltjes with a finite positive discrete measure. Its pole
parameters beta_i-M are positive. The reviewed spectral enclosure gives

    spec H subset [1/4,7n^2],
    f(1/4)=1-R(2n+3/4)<1,
    f(0)<=2

for all sufficiently large n. For the last bound use
beta_i-(2n+3/4)>=2n and the normalized residue weights summing below1;
shifting that denominator down by1/4 multiplies the sum by at most
(1-1/(8n))^(-1)<=2.

Thus the positive-matrix and measure hypotheses in the cited Stieltjes
theorems really hold after this shift. Their logarithmic spectral-ratio
dependence is compatible with approximation degree
O(sqrt(n)log(n)) at error exp(-c sqrt(n)). This is an applicability
observation, not an assertion that the same rate controls any inverse.

The project's [rational-surrogate proof](raw_rational_surrogate_rank_improvement.md)
uses an elementary common denominator instead: group the actual pole
distances dyadically, expand about each bin center, and retain nu terms.
Each normalized resolvent has exact error at most3^(-nu), and the
positive weights preserve that bound. The common denominator has
degree O(nu log(n)). Restricting one multiplier to its multiples costs
exactly that many directions, and restores a polynomial surrogate with
the correct support. Choosing nu of order sqrt(n) permits the reviewed
positive-weight argument and gives the actual high-rank conclusion.

That support/divisibility step is part of the project's independent
derivation. None of the cited approximation theorems by itself supplies
it, the physical endpoint map, or an arithmetic content estimate. The
next use of more optimal rational functions would be to improve the
explicit constants or the selected exceptional subspace, with the
common numerator/denominator and all original multipliers retained.
