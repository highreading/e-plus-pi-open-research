> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Polynomial-weight dual tests remove the first-channel mismatch

Date: 2026-09-13. Original bounded continuation by audit_results.
The coefficient normalization and improved norm inequality were independently checked by audit_computations in-session. A separate full review is pending.

This proves an exact way to handle the first-channel R-versus-R^2 weight mismatch in `raw_single_channel_denominator_extremizers.md`. No scalar approximation is used. The resulting tests satisfy all first-channel zero-data constraints and a retained lower bound on D-O(sqrt(n)) data directions. Pairings with the other good channel remain unresolved, so this does not improve the mixed retained rank.

## 1. The two actual positive scalar weights

Use the fixed square-root cutoff and all actual definitions from the reviewed single-channel note. Put

    F=F_b,   R=F_a/F_b,   2/n<=R<=1

on the finite row spectrum. The actual first-channel energy measure and a new measure are

    dmu=F_b R^2 L_a^2 dSigma_aa,
    dchi=(1/R)dmu=F_a L_a^2 dSigma_aa.

Thus chi is a positive POLYNOMIAL modification of the actual scalar left-seed measure: its modifying polynomial is F_a L_a^2. The high denominator F_b has canceled exactly. No spectral weights or low roots are removed.

Let V_a be the polynomial space of degree <d_a. The Gram H_a of mu is positive definite on V_a, and the Gram H_tilde of chi satisfies

    H_a<=H_tilde<=(n/2)H_a.                         (1)

The first inequality uses 1/R>=1, and the second uses 1/R<=n/2. In the mu Hilbert space define the selfadjoint compression

    C_a=Proj_(V_a) M_(1/R)|_(V_a).

It obeys I<=C_a<=(n/2)I. In any fixed coefficient basis its matrix is H_a^(-1)H_tilde; selfadjointness is with respect to H_a, not necessarily the Euclidean coefficient inner product.

## 2. Exact first-channel dual interpolation

Retain the ORIGINAL artificial jet map J_a, including Q_a(x_j)/d_j, the local radii, and their higher derivatives. Write

    G_a=J_a H_a^(-1)J_a^T,
    G_tilde=J_a H_tilde^(-1)J_a^T.

By (1),

    (2/n)G_a<=G_tilde<=G_a.                        (2)

For data h, the original mu-extremizer is

    u_h=H_a^(-1)J_a^T G_a^(-1)h,
    E_a(h)=h^T G_a^(-1)h.

Define a new polynomial and its same-channel test function by

    w_h=C_a^(-1)u_h
       =H_tilde^(-1)J_a^T G_a^(-1)h,
    p_h=(-1)^(h_a)L_a w_h.                         (3)

The fixed sign matches r_a=(-1)^(h_a)R L_a. The new w_h is a dual test polynomial; generally J_a w_h is NOT h. In fact

    J_a w_h=G_tilde G_a^(-1)h.                     (4)

Equivalently w_h is the chi-minimum-energy interpolant for the explicitly relabeled data in (4). The eigenvalues of the data-change matrix, after the appropriate G_a normalization, lie in [2/n,1].

For every v in V_a with J_a v=0,

    <p_h,r_a v>_F
       =integral w_h v dchi
       =<C_a w_h,v>_mu
       =<u_h,v>_mu=0.                             (5)

This includes every first-channel good multiplier Qv in the actual good space, with its precise degree cap. More generally, for all data h',

    <p_h,f_(h')^a>_F=h^T G_a^(-1)h'.              (6)

Indeed the left side is <w_h,u_(h')>_chi=<u_h,u_(h')>_mu. Equations (5)-(6) remove the first-channel mismatch exactly; no approximate orthogonality is asserted.

## 3. A stronger retained lower bound on a growing data band

First compute the chi norm from the exact coefficient formula:

    ||w_h||_chi^2
      =h^T G_a^(-1)G_tilde G_a^(-1)h
      <=E_a(h).                                  (7)

The F norm of the test has just one additional factor 1/R:

    ||p_h||_F^2
      =integral F_b L_a^2 w_h^2 dSigma_aa
      =integral (1/R)w_h^2 dchi
      <=(n/2)E_a(h).                              (8)

This improves the coarser bound obtained by using two powers of 1/R relative to mu. It follows from the polynomial-weight energy, not from a bound on monomial coefficient norms.

Impose the top coefficient conditions

    deg(L_a w_h)<=q_a,
    q_a=floor((n-a)/2).

The map h -> w_h is linear and injective. The conditions have rank at most

    t_a=max(0,ell_a+d_a-1-q_a)=O(sqrt(n)).

They define a data subspace H_tilde_band of dimension at least D-t_a. On that subspace p_h belongs to the exact retained prefix. Using p_h as a test and (6) with h'=h gives

    ||Pi_L f_h^a||_F
       >=sqrt(2/n)||f_h^a||_F.                    (9)

The tests giving (9) simultaneously satisfy (5). The bound concerns the original single-channel extremizers f_h^a, not the relabeled chi-extremizers as outputs. No conclusion about the full mixed Schur map is implicit.

Intersecting H_tilde_band with the already proved data space H_0, on which f_h^a-f_h is good, retains dimension at least D-t_a-k_0. This intersection is still D-O(sqrt(n)). Equation (5) removes the first-channel part of that good difference. Its other-channel part is the remaining obstruction.

## 4. The cross-channel pairing is now a concrete polynomial-weight operator

For a second-channel good multiplier v_b, the unremoved pairing is, up to the fixed channel signs,

    <p_h,L_b v_b>_F
       =integral F_b L_a L_b w_h v_b dSigma_ab.     (10)

There is no reason for (10) to vanish. It is not bounded below or made small by (1)-(9).

Here is an exact operator-specific next target. Let W_a contain all original vectors L_a(K)K^j v_a, j<d_a, and let W_(b,g) contain precisely the good second-channel vectors L_b(K)K^j v_b, j<=q_b-ell_b. In the original coefficient bases, the map of test data into all second-channel good pairings is

    B_cross=G_a^(-1)J_a H_tilde^(-1)
               W_a^T F_b(K) W_(b,g).              (11)

All entries are now scalar or matrix moments with polynomial weights; the only rational operations are the displayed finite Gram inverses. No artificial-node amplitude has disappeared.

The difference between this cross moment matrix and the one weighted by F_a is exactly

    W_a^T [F_b(K)-F_a(K)] W_(b,g).                 (12)

The equal-degree interlacing gives a useful extra structure for this particular difference. With alpha_i<beta_i as in the reviewed split,

    F_b(t)-F_a(t)
      =sum_(i=1)^h (beta_i-alpha_i)
          product_(j<i)(beta_j-t)
          product_(j>i)(alpha_j-t).               (13)

This is an exact telescoping product identity. It has degree h-1 when h>0, and has positive coefficients in H0=(2n+1)-t, since every high-root offset is positive. For h=0 it is zero. Thus the remaining change is a specific positive polynomial of one lower degree, rather than an arbitrary off-diagonal perturbation. Neither its degree nor positivity alone supplies a small-rank or small-norm bound.

A bounded next task is to use (11)-(13), the exact finite K_N boundary intertwiner, and the stated good multiplier caps to derive a boundary or Christoffel-Darboux formula for the remaining cross-pairing map after first-channel constraints are imposed. The desired estimate concerns this actual projected cross map. It would address the remaining weight mismatch directly, without demanding that an approximation error be nearly zero. Until such a bound is proved, projecting the test away from the other good channel can destroy the positive pairing in (6).

## 5. Scope

The new proved statements are the positive compression, the exact dual identities, the polynomial-weight formula, and the sqrt(2/n) retained bound with exact first-channel good orthogonality on D-O(sqrt(n)) data directions. Cross-channel elimination, mixed retained rank, and physical endpoint estimates remain open. No numerical scan or new canonical degree solve was used.
