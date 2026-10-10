> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Prime-power carry cancellation on the actual denominator-zero cells

Root original research,2026-10-02. Author theorem; no global denominator rate or main irrationality decision.

## Target and prior-work boundary

M11 proves the good-prime first-digit carry and universal r=1 final-q unit. M14 proves the twisted Cartier law. This new target lifts the carry cancellation itself to EVERY prime-power depth, including common-zero first-digit cells. It reduces the actual evaluated common content to one p^k-residue variable rather than the larger off-zero numerator period.

Archive searches covered derangement/Mahler interpolation, prime-power pullback transfer, and mixed endpoint arrays. No completed theorem for these B_N,D_N cells was found. Fresh primary searches/readings included O'Desky and Richman, Derangements and the p-Adic Incomplete Gamma Function, Sections1,2 (https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2022/81.pdf), and Wang–Miska–Mezo, The r-derangement numbers, Section5 (https://arxiv.org/html/1803.04529v1). The normalized derangement interpolation and its congruence preservation are established prior work. The new endpoint numerator transform, its derivative/carry law and denominator-cell reduction below are specific to the actual gauged pullback center.

## Exact Mahler interface

Let P have integral derivative jets, P(0)=0,P(1)=1, and let p be an odd prime outside its monomial coefficient denominator support. Put G=F composed with P, g_j=G^(j)(0), and a_j=[z^j]G'. Then g_j=(j-1)!a_(j-1), all a_j are p-integral, and g_0=0.

Retain M11's D_N,B_N and ACTUAL q_N=|D_N|/gcd(D_N,B_N). Define

    D*(N)=(-1)^N D_N,
    C*(N)=(-1)^N(B_N-N!),
    T_j=sum_(l=1)^j g_l/l!, T_0=0.

For EVERY nonnegative integer N,

    D*(N)=sum_(j>=0)(-1)^j (N)_j,
    C*(N)=sum_(j>=0)(-1)^j (N)_j T_j.              (1)

Terms with j>N vanish. The second formula follows by expanding the exact original convolution B_N=N!+sum binom(N,l)g_lD_(N-l), then setting j=l+k in the derangement expansion. Thus it includes the complete numerator, not just a logarithmic component.

The Mahler coefficients of C* are the INTEGERS

    c_j=(-1)^j j! T_j,
    c_0=0, c_j=-j c_(j-1)+(-1)^j g_j.             (2)

Since v_p(T_j)>=-floor(log_p j), one has

    v_p(c_j)>=v_p(j!)-floor(log_p j).              (3)

These coefficients tend to0 p-adically, so(1) extends C* continuously to Z_p. D* has the classical continuous extension with integer polynomial coefficients. No claim that the factorial function N! itself extends continuously is made; subtracting it before interpolation is essential.

## Uniform finite truncation at arbitrary depth

Let tau_p(j)=v_p(j!)-floor(log_p j) for j>=1. This is nondecreasing: at j=p^s its jump is s-1, and elsewhere the logarithm does not jump. Let J_k be its first index with tau_p(J_k)>=k. Then

    C*(N)=sum_(j<J_k)(-1)^j T_j (N)_j mod p^k    (4)

uniformly for ALL nonnegative N and, by continuity, all x in Z_p. The cutoff obeys J_k<=2p(k+1). For k=1, J_1=2p. For k>=2, J_k<=p^k, since v_p((p^k)!)>=2k.

D* admits the shorter cutoff at the first j with v_p(j!)>=k. For N>=J_k, N! vanishes mod p^k, so

    (-1)^N B_N=C*(N) mod p^k.                     (5)

Thus(4),(5) determine the full evaluated numerator at depth k using O(pk) factorial terms, independently of how large N is.

## The complete all-depth carry formula

Set chi=(-1|p), g_1=2P'(0). At EVERY k>=1, nonnegative N and integer t for which N+p^k t>=0,

    C*(N+p^k t)-C*(N)
          =p^(k-1)t chi g_1 D*(N) mod p^k.       (6)

This is a prime-power-depth congruence of the complete interpolated numerator. It is not merely a replay of the modulo-p Lucas gate.

### Proof of the derivative residue

The derivative of binom(x,j) at integer x has valuation at least-floor(log_p j). This follows by differentiating the Vandermonde expansion binom(x+z,j)=sum binom(x,j-l)binom(z,l), using [z]binom(z,l)=(-1)^(l-1)/l. Therefore the derivative series for C* converges uniformly.

For j>=2p, (3) implies v_p(c_j binom(x,j)')>=v_p(j!)-2floor(log_p j)>=0. These high terms cannot contribute to p C*'(x) mod p. Terms j<p have p-integral ordinary polynomial coefficients and also contribute0 after multiplication by p.

For p<=j<2p, exactly one denominator in T_j has a p factor. M14 gives

    p T_j = a_(p-1)=chi g_1 mod p.

Over F_p, (x)_(p+r)=(x^p-x)(x)_r for0<=r<p. Its derivative evaluated on F_p is-(x)_r. Consequently

    p C*'(N)=chi g_1 sum_(r=0)^(p-1)(-1)^r(N)_r
             =chi g_1 D*(N) mod p.                (7)

All signs here are retained; in particular(-1)^(p+r) combines with the derivative's minus sign.

### From the derivative to every depth

Use the finite polynomial(4). For k=1 its coefficients have denominator p-exponent at most1, so all quadratic-and-higher terms in a shift p t vanish mod p. For k>=2, J_k<=p^k makes every retained coefficient denominator exponent at most k-1. All quadratic-and-higher terms in a shift p^k t vanish mod p^k. The derivative contributions at j>=2p are p-integral. The remaining linear term is exactly p^(k-1)t times(7), proving(6) at every depth. Continuity extends the same law to p-adic arguments.

## The numerator loses exactly one digit off the zero locus

Formula(6) implies that C* is globally p-Lipschitz:

    v_p(C*(x)-C*(y))>=v_p(x-y)-1.

Its values modulo p^k therefore have period p^(k+1). If p does not divide g_1, the modulus-p period is EXACTLY p^2, since at N=0 and shift p the difference is chi g_1, a unit. The normalized derangement D* has modulus-p period p, so it would be incorrect to impose the smaller period on the numerator everywhere.

On the denominator-zero residue classes D*(N)=0 mod p, (6) improves to

    C*(N+p^k t)=C*(N) mod p^k for every k>=1.     (8)

Thus C* is1-Lipschitz within each such residue class, and all-depth extra carry is killed on the actual denominator-zero locus.

## Actual common content depends on only ONE depth-k residue

For N>=J_k,

    p^k divides gcd(D_N,B_N)
       iff D*(N)=C*(N)=0 mod p^k.                 (9)

If one such zero occurs then its first digit lies on D*=0 mod p. Both D* and C* restricted to that class have period p^k by(8). Therefore the condition in(9) depends only on N mod p^k, even though the full numerator off that class needs p^(k+1). This supplies a finite all-depth common-content lifting problem on p^k cells, without discarding a nonzero carry or using a raw coefficient clearer as q.

By compactness, unbounded common valuations along large nonnegative indices occur if and only if D* and C* have a COMMON p-adic zero in Z_p. If no common zero exists, their joint valuation has a uniform finite bound. This is a conditional local criterion, not a theorem that common zeros are absent. At the universal root x=1, D*(1)=0 and C*(1)=-g_1, so p-unit g_1 excludes that common zero exactly.

## New exact receipt and remaining obligations

GAUGED_PRIME_POWER_TRANSFER_CERTIFICATE.json tests linear/cubic pullbacks at p3,11 through four depths, and the degree81 pullback at good p83 through two depths. It compares the new Mahler numerator with an INDEPENDENT original binomial convolution using the classical derangement polynomial, including very large indices, and checks every shift carry and denominator-root improvement at the indicated witnesses. This is finite evidence for normalization/signs; the all-depth theorem is the proof above.

No distribution theorem for the remaining p-adic common zeros is proved. Fixed small primes do not automatically supply exponential denominator mass, and prime factors larger than N remain outside any fixed finite atlas. Thus this result resolves the local digit-transfer interface while leaving the global actual-q growth question and e+pi irrationality open.
