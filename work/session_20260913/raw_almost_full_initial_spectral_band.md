> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Uniform approximation of an almost full initial prolate band by the actual high rows

Date: 2026-09-13. Original root continuation. Independent review
raw_almost_full_initial_spectral_band_independent_review.md passes the
complete proof without a mathematical correction.

This applies the already proved high-row approximation of low polynomials
to actual prolate eigenfunctions, using a new uniform factorial bound on
their Legendre tails. It gives a specified consecutive set of
n−O(n/log n) independent actual spectral columns and exponential
concentration outside that initial band for every actual high kernel.
It is separate from the stronger overall n−O(sqrt(n)log n) rank count,
which does not identify this consecutive set of columns. It does not
give concentration onto the last two nodes or the missing physical
endpoint angle.

## 1. A uniform Legendre tail estimate for the true eigenfunctions

Let phi_j be the normalized shifted Legendre basis, E_j=j(j+1), and
T=L₀+3/4+W with W=(x−1/2)². Multiplication by W has bandwidth two in
this basis and preserves reflection parity. Its norm is at most 1/4.
Let psi_l be an actual normalized eigenfunction at xi_l. Use the
reviewed enclosure xi_l−3/4∈[E_l,E_l+1/4].

For h≥0 let Q_h project onto the parity-l coordinates with indices
l+2h,l+2h+2,..., and write t_h=||Q_h psi_l||. Thus t_0≤1.
For h≥1 the compression of L₀+W−(xi_l−3/4) onto this tail is
positive and bounded below by

    E_(l+2h)−E_l−1/4
       =2h(2l+2h+1)−1/4 ≥(15/4)h².

Its coupling to the omitted coordinates is a single matrix entry,
between indices l+2h−2 and l+2h, of absolute value at most 1/4.
The eigenvalue equation on the tail therefore implies

    t_h≤[1/(15h²)] |<psi_l,phi_(l+2h−2)>|
        ≤[1/(15h²)]t_(h−1).

The positive inverse exists on the compressed self-adjoint domain;
this is a bounded perturbation of the diagonal Legendre tail with
compact resolvent. Iterating gives the exact, uniform estimate

    ||Q_h psi_l||≤15^(−h)/(h!)²,      l≥0, h≥1.       (1)

In particular, if K≥l+2h−2, the orthogonal polynomial truncation
P_≤K obeys

    ||(I−P_≤K)psi_l||≤15^(−h)/(h!)².                 (2)

The condition in (2) is deliberately conservative: all degrees above K
in this parity are contained in Q_h. No phase or endpoint value is
divided out. The estimate remains uniform when both l and h grow.

## 2. Retain the proved high-row approximation constants

Let H_n=span(E_(n+1),...,E_(2n−1)) in L²[0,1]. Scaling E_k by its
nonzero constants does not change this span. The already reviewed
inverse-Borel construction in
`raw_high_orthogonality_spectral_concentration.md`, equations (4)–(9),
gives for every 0≤j≤K≤n an element A_(n,j) in H_n such that

    ||phi_j−A_(n,j)||≤epsilon_(n,K),
    epsilon_(n,K)=4n² (2e³)^n/n!
                 ·(K+1)³ sqrt(2K+1) 8^K K!.         (3)

For any polynomial v of degree at most K, write it in the orthonormal
Legendre basis and combine the approximants. Cauchy–Schwarz on its
K+1 coefficients proves

    dist(v,H_n)≤sqrt(K+1)epsilon_(n,K)||v||.           (4)

Now take v=P_≤K psi_l with l≤M≤K−2h+2. Equations (2) and (4) give

    dist(psi_l,H_n)≤b_(n,K,h),
    b_(n,K,h)=15^(−h)/(h!)²
                      +sqrt(K+1)epsilon_(n,K).        (5)

All factors in (3) are retained before choosing a growing degree.

## 3. A concrete growing consecutive band

Put c₀=log(16e³)=log16+3, and set, for all sufficiently large n,

    w=ceil(8n/log(n+1)),
    K=n−w,
    h=ceil(2n/log(n+1)),
    M=K−2h,
    r=M+1=n−12n/log n+o(n/log n).                     (6)

Then M≥0 and r≤n−1 eventually. The standard elementary factorial
estimate for w=o(n), used in the previous concentration theorem, gives

    log epsilon_(n,K)≤−(8−c₀+o(1))n.

For (1), Stirling's elementary logarithmic bounds give

    log[15^(−h)/(h!)²]=−4n+o(n).

Thus b_(n,K,h)≤exp(−(8−c₀+o(1))n). Let Psi_r be the isometry with
columns psi_0,...,psi_M and let P_H be the orthogonal projection onto
the actual high-row span. Summing the individual squared defects in
(5) gives the operator-norm bound

    ||(I−P_H)Psi_r||≤sqrt(r)b_(n,K,h)
                   =exp(−(8−c₀+o(1))n).             (7)

More explicitly, the left side is at most its Frobenius norm, and each
column defect is bounded by (5). There is no assumption that the
individual best approximants are linearly independent. Since Psi_r is
an isometry,

    Psi_r*P_H Psi_r≥[1−r b_(n,K,h)²]I_r.             (8)

For sufficiently large n this is positive definite. Therefore the
actual matrix (<E_k,psi_l>)_(n+1≤k≤2n−1,0≤l≤M) has full column
rank r. In particular at least one r-by-r minor made from those
specified consecutive columns and actual high rows is nonzero.

This theorem does not select a predetermined row grid. It proves an
existence statement among the prescribed high rows, and the canonical
projection estimate (8), rather than a Vandermonde asymptotic for one
fixed minor. It complements the earlier explicitly selected small-low
and sparse-bulk minors without replacing their more specific formulas.

## 4. Exact high-kernel concentration in these spectral coordinates

Every v in H_n-perp, with no polynomial restriction, obeys

    ||Psi_r* v||=||Psi_r*(I−P_H)v||
        ≤sqrt(r)b_(n,K,h)||v||.                      (9)

This applies both to the original high-orthogonal polynomial and to a
finite spectral combination v=sum_(l=0)^n a_l psi_l satisfying the
actual high-row equations. In the latter case it gives

    sum_(l=0)^M |a_l|²
        ≤r b_(n,K,h)² sum_(l=0)^n |a_l|².            (10)

These are actual orthonormal spectral coefficients, with no discarded
amplitude factors g_l or unsigned endpoint reweighting. Reflection only
changes their parity signs and preserves the inequalities.

One can express (8) through the original high-row synthesis map
U:c↦sum_(k=n+1)^(2n−1)c_k E_k and its exact positive Gram G_H=U*U:
the preconditioned matrix
G_H^(−1/2)U*Psi_r has Gram Psi_r*P_H Psi_r. This uses the actual
linearly independent polynomial rows E_k. No unweighted singular-value
bound for U, or conditioning estimate for G_H, is being inferred.

The band left uncontrolled in (10) still has order n/log n, far more
than two coordinates. Further localization or an endpoint cancellation
estimate is necessary for the irrationality route. Numerical data and
fixed-size Taylor asymptotics are not inputs to (1)–(10).
