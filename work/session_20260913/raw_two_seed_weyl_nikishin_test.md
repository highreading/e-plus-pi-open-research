> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The actual two-seed Weyl matrix: exact continued fractions and a Markov-ratio obstruction

Date: 2026-09-13. Original bounded continuation by audit_results.
Independent root review in raw_two_seed_weyl_root_review.md passes the
full algebra, exact certificates, and stated scope.

This investigates the actual left-seed measure, rather than importing scalar total positivity from a five-diagonal matrix. It gives exact all-index scalar and block Schur representations. It also gives an exact counterexample at the actual size N=4 to the simplest constant-sign Markov-ratio/Nikishin identification. That finite obstruction is not promoted to an eventual theorem or to a counterexample for the large-index mixed Schur matrix.

Prior notes read first: `matrix_orthogonal_ratio_literature.md` and `raw_borel_legendre_literature.md`. Their matrix-orthogonality and scalar-Favard limitations remain in force.

## 1. What the Nikishin condition would actually require

Fidalgo Prieto and López Lagomasino, [*Nikishin systems are perfect*](https://arxiv.org/pdf/1001.0554), pp. 2-5, Definition 1.2 and Theorems 1.1-1.2, construct the second measure by multiplying a root measure by the Cauchy transform of a constant-sign measure on a disjoint interval. They prove the corresponding AT and mixed-perfectness results. Their stated measures have infinite support; a finite matrix requires a bounded-degree, finite-atomic analogue rather than literal all-index perfectness. I read these definitions and theorem statements, not merely the abstract.

The specific scalar identification tested below would have, on the support interval I of the actual first-seed measure,

    dSigma_01(t)=phi(t)dSigma_00(t),
    phi(t)=c_0+integral d tau(s)/(t-s),              (1)

where tau has constant sign and its support interval is disjoint from I. A harmless constant or nonzero scalar change of the second seed is allowed in (1). Positive semidefiniteness of the matrix measure does not imply (1).

A general AT property is weaker/different than this particular representation. Failure of (1) will not be called a proof that every restricted AT statement fails.

## 2. Gauge and an exact scalar Schur factorization

Let K=K_N be the actual symmetric matrix, N=2n, with

    a_j=j^2/sqrt(4j^2-1),
    d_j=a_j^2+a_(j+1)^2-j(j+1),
    K_(j,j+1)=-a_(j+1),
    K_(j,j+2)=a_(j+1)a_(j+2).

Here a_0=0. Set D_alt=diag((-1)^j) and Kplus=D_alt K D_alt. Both first and second off-diagonals of Kplus are strictly positive. The actual seeds become

    D_alt v_0=e_0,
    D_alt v_1=-e_1-c e_0,
    c=sqrt(3)/2.

For N>=4 split off the first coordinate:

    Kplus=[[d_0,h^T],[h,A]],
    d_0=1/3,
    h=a_1(e+a_2 f),

where A is the tail on original indices 1,...,N-1 and e,f are its first two coordinate vectors. Put

    G(z)=(zI-A)^(-1),
    r(z)=h^T G(z)e,
    g(z)=e^T G(z)e,
    m(z)=[z-d_0-h^T G(z)h]^(-1).

The actual seed Weyl matrix M_N(z)=V^T(zI-K)^(-1)V is exactly

    M_N(z)=[[m, -(c+r)m],
            [-(c+r)m, g+(c+r)^2 m]].               (2)

This is an identity of rational functions. It follows from the ordinary block inverse, including the original offset seed; no seed is replaced by an orthogonal coordinate without keeping the change.

In particular,

    -M_01/M_00-c=r(z),
    M_11-M_01^2/M_00=g(z).                         (3)

Both m and g are Cauchy transforms of positive scalar spectral measures. The remaining coefficient r is a CROSS resolvent. Its spectral residues on the tail are

    r(z)=sum_lambda [h^T Pi_lambda e]/(z-lambda),   (4)

and the products h^T Pi_lambda e have no automatic sign. Formula (2) is a spectral-parameter-dependent triangular factorization; it is not a constant change that turns the original two-channel system into two independent scalar systems.

## 3. Exact two-by-two continued fraction and genuine exterior positivity

Group Kplus into blocks indexed j=0,...,n-1. Its diagonal and forward blocks are

    A_j=[[d_(2j),a_(2j+1)],
         [a_(2j+1),d_(2j+1)]],

    B_j=[[a_(2j+1)a_(2j+2),0],
         [a_(2j+2),a_(2j+2)a_(2j+3)]].

Let W_j(z) be the top two-by-two resolvent block of the tail beginning at scalar index 2j. Then

    W_(n-1)=(zI-A_(n-1))^(-1),
    W_j=[zI-A_j-B_j W_(j+1)B_j^T]^(-1).           (5)

All B_j are invertible. This is the actual matrix continued fraction, with the multiplication order fixed. The formula holds wherever its displayed inverses exist, and elsewhere as a meromorphic identity.

The seed conversion at the first block is

    M_N=S^T W_0 S,
    S=[[1,-c],[0,-1]].                             (6)

For real x above the row spectrum, every principal-tail resolvent is positive definite and entrywise strictly positive. For example, add a scalar shift to make its underlying irreducible matrix entrywise nonnegative and sum its convergent resolvent Neumann series. Thus r(x)>0, and in fact

    (-1)^k r^(k)(x)=k! h^T(xI-A)^(-k-1)e>0        (7)

for every k>=0. Both h and e are nonnegative and the inverse is entrywise positive. These statements are valid for all N in scope. They do not imply constant-sign spectral residues in (4).

Equivalently, if Sigma=B_0 W_1 B_0^T, the first-block inversion gives

    r(z)=[a_1+Sigma_01(z)]/[z-d_1-Sigma_11(z)].     (8)

The numerator and denominator are positive on the exterior real interval. The self-energy Sigma_01 is still a cross-resolvent entry, so (8) is not a scalar positive Jacobi continued fraction.

## 4. An actual N=4 symbolic obstruction

For N=4, divide r by the positive a_1 and write psi=r/a_1. Direct exact three-by-three inversion of the actual tail gives

    psi(z)=q(z)/p(z),

    p(z)=(1323z^3+11697z^2+18284z-13168)/1323,
    q(z)=(315z^2+2932z+6576)/315.                   (9)

The denominator has exactly one root in each of

    (-7,-6), (-3,-2), (0,1),

and the numerator has exactly one root in each of

    (-6,-5), (-4,-3).

These are certified by exact endpoint signs and degree counts; the three-by-three tail is symmetric. The polynomials are coprime. Both numerator zeros are in the FIRST pole gap. Therefore the residues of psi at its three increasing poles have signs

    +, -, +.                                     (10)

For example q is positive at all three poles, while the derivative of the monic cubic has signs +,-,+. The ratio cannot be the Cauchy transform of a constant-sign measure. A constant shift has no effect on these residues.

An independent moment certificate gives the same conclusion. Expanding psi at infinity, its first five moments are

    1, 7/15, 923/315, -148193/6615, 4506871/27783.

Their three-by-three Hankel determinant is

    -400592896/2701125 <0.                         (11)

A positive measure would make this Gram determinant nonnegative. Its total mass is positive, so a constant negative measure cannot represent it either. Formula (7) nevertheless remains valid for this ratio on the exterior interval. This is a concrete example of the distinction between exterior resolvent positivity and the Markov spectral-residue condition in the actual family.

The exact control is `two_seed_markov_ratio_checks.py`, with saved output of the same stem ending in `.json`. It constructs only the stated N=4 matrix for the counterexample. A separate fixed formal-moment stabilization check was also done, specifically to avoid extrapolating (11): through order four, all paths stay below scalar index 6, and for N>=6 the stabilized moments are

    1, 7/15, 923/315, -11059/4725, 16421477/155925.

Their Hankel determinant is instead 117256192/471625>0. Hence the particular negative determinant (11) does NOT prove eventual failure. No larger sequence of moment or eigenvalue tests was performed.

## 5. Why the obstruction excludes the standard first-row Nikishin identification

Here is an elementary necessary condition for (1), avoiding reliance on a formal analogy. Suppose a positive finite root measure sigma has simple support points lambda_j and all weights w_j>0. Let

    f_0(z)=sum_j w_j/(z-lambda_j),
    f_1(z)=sum_j w_j phi(lambda_j)/(z-lambda_j).

Every zero nu of f_0 lies strictly between consecutive support points, is simple, and has f_0'(nu)<0. If (1) holds with positive tau outside the convex support interval, then

    f_1(nu)
      =sum_j w_j [phi(lambda_j)-phi(nu)]/(nu-lambda_j)
      =sum_j w_j integral d tau(s)/[(lambda_j-s)(nu-s)]>0.

Thus every pole residue of f_1/f_0 is negative. Negative tau reverses every sign, and adding a constant to phi does not change any residue. All such residues must have the same sign.

For the actual N=4 first-row pair, M_00 has four positive spectral weights and its three zeros are exactly the roots of p in (9). One can verify this directly from the coprimality of the full characteristic polynomial and the tail characteristic polynomial. This coprimality was checked exactly; it also follows because every cross residue in (10) is nonzero, hence no tail eigenvector is orthogonal to the coupling h. By (3), the residues of M_01/M_00 are -a_1 times those in (10), so their signs are -,+,-. This contradicts the necessary condition just proved.

Consequently the actual first-row measure pair at N=4 is not of the form (1), even with the allowed constant shift or scalar sign convention. This refutes an all-N claim of that standard Nikishin structure. It does not classify arbitrary nonlinear or full two-seed changes, and it does not disprove a restricted or eventual AT property on a specified interval.

## 6. An all-index obstruction to a simpler scalar Jacobi seed identification

For every N>=4, let E=span(e_0,e_1), the same subspace as the actual two seeds. The block carrying Kplus E into coordinates 2,3 is B_0^T, and

    det B_0=a_1 a_2^2 a_3 !=0.

Hence no nonzero u in E satisfies Kplus u in E. It follows that no constant invertible change of these two seeds can make them the degree-zero and degree-one vectors of one scalar Jacobi/Krylov chain: that would require the second vector to be a nonzero affine function of Kplus applied to the first, and therefore Kplus u in E.

This is specific to the actual invertible two-channel boundary coupling. It does not contradict the existence of a scalar orthogonal-polynomial measure for each individual seed, and it does not rule out a more elaborate Nikishin representation. It excludes the direct scalar three-term-chain shortcut for the unchanged two-seed span.

## 7. Consequence for the mixed Schur task

The valid all-index structures are the positive matrix continued fraction (5), the exact scalar Schur factorization (2), and exterior positivity (7). The cross coefficient r can carry signed spectral residues, and the actual N=4 example shows that a same-sign Markov-ratio claim requires more than the gauge and positive resolvent entries. The usual scalar Nikishin perfectness theorem therefore does not currently establish invertibility of the actual mixed Schur S.

The precise unresolved route would need an actual large-index or data-restricted theorem about the signed cross function in (4), or a different measure transformation together with an exact translation of the true node factors, degree caps, and mixed test map. A change of seeds alone cannot be treated as preserving the two diagonal node-polynomial factors. No mixed rank improvement, quantitative inverse, or irrationality conclusion is proved here.
