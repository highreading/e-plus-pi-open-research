> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A zero-free reconstruction insertion at proportional size

Author: Codex continuation Agent 3, 2026-10-02. Original author lemma; not independently reviewed. It controls the exact reconstruction insertion BEFORE its complex ensemble average. The latter remains a separate step and is not inferred from positivity of this insertion.

The exact gamma insertion R_j is defined in PROPORTIONAL_B_EXACT_SELBERG_PROGRESS.md. Let d=b-1<=n-1, let every |z_l|<=1, and put

    s_0=(-1)^(d+1), s_j=(-1)^(d-j+1), 1<=j<=d,
    s_b=1,
    B_j=|K_(j,d)| sigma^(-d)>0,
    S_j(z)=s_j R_j(z)/B_j.

There is an absolute n_0 such that for ALL n>=n_0, all d<=n-1, all coordinates 0<=j<=b, and all such z,

    Re S_j(z)>=1/100, |S_j(z)|<=5.                      (1)

Thus every actual reconstruction insertion is zero-free throughout the closed unit polydisk, with constants uniform up to proportional size. These are not coordinate-center or actual Toeplitz-expectation nonvanishing statements.

## 1. Checks and primary-source overlap

Before this lemma, archive queries included gamma reconstruction, sector K, sector reconstruction, Gamma(n), positive real polynomial, pointwise K and top-column constant in the October 1 agent3 sources and the current analytic notes. The archived B_CENTER_ADJOINT_NONVANISHING.md warns correctly that Toeplitz accretivity does not establish positivity of mixed reconstructed adjoints. The present pointwise gamma lemma does not make that inference.

Primary queries:
- site:arxiv.org gamma integral inverse differential operator polynomial stability preservation Laguerre
- site:arxiv.org Borcea Branden linear operators stable polynomials Laguerre gamma

Opened [Borcea and Branden, stability-preserving linear operators](https://arxiv.org/abs/0809.0401) and [their stable-polynomial theory/applications](https://arxiv.org/abs/0809.3087). Their broad zero-free operator framework is established. No classification theorem is imported here; (1) follows from the actual elementary gamma-integral argument below.

## 2. Gamma integrands have a fixed sector on their main mass

For a selected set I of k variables, write

    product_(l in I)(sigma z_l-u)=(-u)^k
                                  product_(l in I)(1-sigma z_l/u).

For u>sigma, every factor lies in the disk centered at one of radius sigma/u. Therefore the product's argument has modulus at most k arcsin(sigma/u), and its modulus is at least (1-sigma/u)^k.

Fix alpha=19/20. If u>=alpha n and k<=d<=n-1, then, for all sufficiently large n,

    k arcsin(sigma/u)<=3/2<pi/2,
    (1-sigma/u)^k>=exp(-3/2).

Consequently the real part of every normalized selected product is at least

    cos(3/2)exp(-3/2)>0.015.                             (2)

The normalized elementary polynomial is the average of these products, so (2) holds for it too.

For 1<=j<=d, put k=d-j. After multiplication by its known sign, the gamma integrand is the POSITIVE combination

    u^(k+1)binom(d,k+1) average_(|I|=k+1) product_(l in I)(1-sigma z_l/u)
      +u^k binom(d,k) average_(|I|=k) product_(l in I)(1-sigma z_l/u).

The j=0 case contains only the k=d term; the j=b case is the exact constant. Its reference gamma integral is exactly B_j:

    B_j=sigma^(-d)/Gamma(n)
       [binom(d,k+1)Gamma(n+k+1)+binom(d,k)Gamma(n+k)]

for the middle coordinates, with the corresponding single term at j=0. This agrees with the exact top K column; it is not an asymptotic replacement.

## 3. Uniform small-tail and upper estimates

For an individual degree k term,

    |e_k(sigma z-u)|<=binom(d,k)(u+sigma)^k.

Substitute v=u+sigma. Since u^(n-1)<=v^(n-1),

    integral_0^infinity u^(n-1)e^(-u)(u+sigma)^k du
        <=exp(sigma)Gamma(n+k).                          (3)

Thus every normalized term, and their positive combination, has absolute upper bound exp(sigma)<5. This proves the upper estimate in (1), without any large-n qualification.

The same substitution restricts the small tail u<alpha n to v<alpha n+sigma. Its absolute size divided by Gamma(n+k) is at most

    exp(sigma) Prob[Gamma(n+k,1)<alpha n+sigma].

Uniformly in 0<=k<=d, this is O(exp(-gamma n)) for some absolute gamma>0: its largest lower-tail probability is at the smallest shape n, and alpha n+sigma remains a fixed fraction below n for large n. The ordinary reference gamma mass below alpha n has the same bound.

Therefore the main gamma mass contributes at least the positive constant in (2), times 1-O(exp(-gamma n)), while the whole small tail can subtract only O(exp(-gamma n)). Every middle-coordinate reference is a positive weighted combination of those gamma shapes, so the bounds are uniform in j. For sufficiently large n their difference exceeds 1/100. This proves (1).

## 4. Consequence and limitation

The exact K reconstruction has no exponential-in-n loss as a function of the unit-circle particles, even when d~cn: after its explicit top-column scale and sign are removed, its insertion remains bounded and in the right half-plane. It also has no zero anywhere in the unit polydisk.

The original complex symbol and the characteristic forcing product still multiply this insertion. Integrating them can introduce cancellation. The next step is a variance/concentration estimate for that phase, together with a same-index bound on the odd outer sectors. No positivity of the full actual coordinate or its Gram average is claimed from (1) alone.
