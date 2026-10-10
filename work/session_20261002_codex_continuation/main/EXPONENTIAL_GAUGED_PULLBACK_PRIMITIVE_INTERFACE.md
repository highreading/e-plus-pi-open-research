> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exponential-gauged pullback centers: a new primitive arithmetic interface

Date:2026-10-02. Author derivation; main e+pi question remains open.

## Archive and primary-paper gate

The archive already studies derangement factorial transforms, mixed E/G systems, ordinary Taylor pullbacks and primitive content. Read `sources/positive_derivative_kernel_divergence.md`, `common_kernel_lattice_identity_and_capacity_audit.md`, `cyclotomic_unit_linear_ray_padic_reduction.md`, and the composed integral-jet pullback sources. The target here is the specifically normalized exponential-gauged endpoint ray for F∘P, its complete gcd, a carry-cancelled mod-p formula, and a uniform three-even-index nonvanishing block. No completed theorem in that domain was found in the archive searches. The generic use of derangements is not claimed new.

Fresh searches concerned inverse-Apéry pullbacks, derangement/arctangent arithmetic, rational logarithmic derivatives and divided-power p-curvature. Read the exact Taylor constraint of the July2026 inverse-Apéry paper and Bostan–Caruso–Roques, *Algebraic solutions of linear differential equations: an arithmetic approach*, §§4.2,5.1 (Hurwitz series and denominators), primary full text https://arxiv.org/html/2304.05061v2 . Its general characteristic-p background is established; it does not provide the endpoint formulas below. Also opened the new Sept2026 cancelled digit-transfer paper https://arxiv.org/html/2609.23355v1 ; its two-step hypergeometric result is not transferred to this family without proof.

## Exact target-preserving ray

Let P be a rational polynomial with integer derivative jets, P(0)=0,P(1)=1. Put G=F∘P, F(w)=4atan(w/(2-w)) on the germ with F(0)=0. Its continuation on the real path has G(1)=pi. All derivative jets g_j=G^(j)(0) are EVEN integers, by the recurrence for the F jets and the integer Bell polynomials. Assume G is analytic on |z|<R, with R>1.

Define

u_k=(exp(-z)G(z))^(k)(0)=sum_{j=0}^k binom(k,j)(-1)^(k-j)g_j,
E_N=sum_{k=0}^N(-1)^k/k!,
V_N=sum_{k=0}^N u_k/k!,
D_N=N!E_N,
B_N=N!(1+V_N).

The new normalized center and its ACTUAL primitive denominator are

c_N=(1+V_N)/E_N=B_N/D_N,
q_N=D_N/gcd(D_N,B_N),     N>=2.                   (1)

They target S=e+pi because exp(-1)G(1)=pi/e. The exact recurrences are

D_0=B_0=1,
D_N=N D_(N-1)+(-1)^N,
B_N=N B_(N-1)+u_N.                               (2)

The full numerator can also be written without u:

B_N=N!+sum_{j=0}^N binom(N,j) g_j D_(N-j).       (3)

The Taylor polynomial R_N of exp(-z)(c_N-G(z)) has endpoint R_N(1)=1 and R_N(0)=c_N. Its complete kernel is K_N=(R_N+R_N')exp(z)+G'(z), whose integral is EXACTLY e-c_N+pi=S-c_N. It has Taylor-zero order N at0. Multiplying by q_N gives the primitive integer endpoint form q_N S-p_N even though R_N itself has rational monomial coefficients. Thus this is the normalized version of the maximal-order restart for the improved G pullback; the e and pi coefficients are both exactly1 before primitive scaling.

## The dyadic obstruction changes

For even N, D_N is odd, since the derangement recurrence modulo2 gives D_N=1 for even N and0 for odd N. Since u_j are even and N! is even, B_N is even for every N>=2. Therefore at even N

q_N is ODD, and the primitive numerator is EVEN.             (4)

The ordinary Taylor e+G law v2(q)=v2(N!) does not apply to this gauged family. The dyadic factorial has been removed automatically by the endpoint normalization. This does not bound the many odd factors of D_N or imply favorable q-growth.

## Full analytic error retains the pullback radius

For every1<r<R, Cauchy's remainder bound for exp(-z)G(z) and the factorial remainder for exp(-z) give

c_N-S=O_r(r^(-N)).                                  (5)

E_N is bounded away from0 for N>=2. In a family of endpoint-fixed omitted-puncture pullbacks with one common radius R, the cover/Schwarz normalization (or Schottky theorem) supplies uniform bounds on any smaller disk. Thus (5) can be uniform over independently varying P_N in that class. Formula(1), not a coefficient clearer, must be paired with this error.

A sufficient primitive-form condition would be a subsequence/short-block bound q_N<=C exp(sigma N), sigma<log R, together with nonvanishing. No such gcd estimate is proved here.

## Uniform nonvanishing in a block of THREE even centers

For ONE fixed G, there cannot be three consecutive even orders N,N+2,N+4 with c_N=c_(N+2)=c_(N+4)=S. Indeed, using (2), if c_m=c_(m-2)=S at even m, then

m u_(m-1)+u_m=(1-m)S.                             (6)

The left side is an integer. Applying this to m=N+2,N+4 shows (N+1)S and(N+3)S are integers. These two odd integers have gcd1, so S would be an integer. But5<S<6. Hence at least one complete primitive form among every such three-center block is NONZERO, without a transcendence assumption, a moving saddle, or an all-axis sign analysis.

This is an actual fixed-length nonzero selector, not a zero-free claim for every index. It requires a common G across the three centers. It is not automatically valid for three independently modified P_N, whose u arrays need not match.

## Good-prime carry cancellation at ALL indices

Let p be an odd prime outside the denominator support of the monomial coefficients of P. Then G'=2P'/q0(P), q0(w)=1-w+w²/2, has p-integral ordinary Taylor coefficients because q0(P(0))=1. Therefore

g_j=(j-1)![z^(j-1)]G' =0 mod p for j>=p+1.         (7)

Write N=pa+r,0<=r<p. Lucas' theorem and (7) imply

u_(pa+s)=(-1)^a u_s+a(-1)^(a-1+s)g_p mod p, 0<=s<p. (8)

Only terms k>=pa survive in B_N=N!+sum u_k N!/k! once N>=p. The factorial ratios reduce to r!/s!, while D_N=(-1)^aD_r mod p. Thus

B_N=(-1)^a(B_r-r!)+a(-1)^(a-1)g_p D_r mod p.       (9)

In particular, if p divides D_N, equivalently D_r=0 mod p, then the endpoint carry involving a and g_p disappears:

p divides gcd(D_N,B_N)
  iff D_r=0 and B_r-r!=0 mod p.                    (10)

This gives a finite first-digit common-zero gate for every depth/index; it is not a valuation or prime-supply theorem. The carry is killed on the actual denominator-zero locus, rather than discarded in the full expression.

The universal seed r=1 satisfies D_1=0 and B_1-1=g_1=2 P'(0). For the new P with P'(0)=1 this is2, so at every good odd prime and every N=1 mod p,

v_p(q_N)=v_p(D_N).                                 (11)

All p powers in D_N survive the FINAL evaluated gcd because B_N is a p-unit. The first-digit gate is sufficient for this all-depth valuation equality.

## New bounded exact receipt and unresolved arithmetic

`gauged_pullback_endpoint.py` computes this new transform on root's frozen degree61 P, without rereading or auditing its analytic certificate. Rational/integer checks cover N1..420 and every good prime61..199. They verify(3),(4),(7),(9),(10)'s congruence, and the r1 unit. `GAUGED_PULLBACK_ENDPOINT_CERTIFICATE.json` retains the actual q and gcd at nine orders and every derangement-root seed/residue.

The observed q has119digits at N80 and469digits at N240; these values are consistent with very large odd denominators but prove no asymptotic bound. The needed favorable gcd would have to remove almost all of log D_N=N log N-O(N), leaving less than N log R. The forced raw factorial content from M10 is already removed before this question is asked.

This family genuinely changes the dyadic arithmetic and supplies a simple complete nonvanishing block. It leaves a hard derangement/mixed numerator gcd problem, including prime powers and primes larger than N. No shrinking primitive sequence, main rationality decision, or global no-go follows from the finite data.
