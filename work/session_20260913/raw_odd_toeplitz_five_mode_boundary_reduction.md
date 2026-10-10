> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A five-mode boundary reduction for the odd dual Toeplitz matrix

Date: 2026-09-13. Original bounded continuation by audit_results.
Independent review: FULL PASS by audit_sources; see raw_odd_five_mode_independent_review.md.

This continues the independently passed raw_odd_dual_toeplitz_scalar_obstruction.md. It proves a quantitative result about the actual odd matrix and its actual high compression: all but five singular values of the full matrix, and all but six singular values of the high compression, are uniformly bounded below. The proof uses an explicit Laurent inverse of the actual two-parity symbol and a fixed degree-one truncation. It does not infer invertibility from the indefinite Hermitian gap.

Both matrices are already known to be invertible by the passed added-column theorem and the actual high-row argument. The new result confines the unresolved inverse growth to a fixed number of boundary modes. It does not yet bound those remaining modes.

## 1. The exact two-parity multiplication symbol

Let n=2m+1, m>=0, N=n+1=2m+2. Write polynomials of degree at most n as

    p(z)=u(t)+z v(t),       t=z^2, degree u,degree v<=m.

Use the Hilbert space

    H_m=L^2(circle, |1+t|^(2m+2) dtheta/(2pi); C^2),

and let P be the orthogonal projection onto

    P_m={(u,v): degree u,degree v<=m}, dimension N.

The positive Gram matrix in monomial coordinates is exactly the G from the preceding odd note: two copies of the binomial Toeplitz block C_(m+1).

Define the entire functions

    c(t)=sum_(j>=0) t^j/(2j)! =cosh(sqrt(t)),
    s(t)=sum_(j>=0) t^j/(2j+1)! =sinh(sqrt(t))/sqrt(t).

The power series define their values without choosing a branch. Pairing z and -z in the actual signed symbol gives the following exact matrix-valued symbol in t:

    a(t)=1/(1+t) [ t s(t)   t c(t) ]
                 [ c(t)     t s(t) ].                      (1)

Indeed the paired entries before division by the positive weight are sinh(z), z cosh(z), z^(-1)cosh(z), sinh(z), divided by z+z^(-1). Replacing z^2 by t gives (1). Consequently the compression

    A=P M_a P restricted to P_m

is unitarily equivalent to the actual normalized odd matrix Atilde=G^(-1/2)A_nG^(-1/2). The preceding proved bound therefore gives

    ||A||<=C0=e sqrt(5/4).                                  (2)

The multiplier a has a pole at t=-1 and need not be bounded on the entire Hilbert space. Its action on every finite Laurent polynomial used below is well-defined: the square of its simple pole is integrable against |1+t|^(2m+2), including m=0.

## 2. An explicit bounded Laurent inverse

The elementary identity c(t)^2-t s(t)^2=1 gives the pointwise inverse

    r(t)=(1+t) [ -s(t)   c(t) ]
                [ c(t)/t -s(t) ].                          (3)

This identity is needed only almost everywhere on the unit circle. The apparent issue at t=-1 is removable for r, and t=0 is not on the integration circle.

Use the fixed truncations

    c_1(t)=1+t/2,     s_1(t)=1+t/6,
    r_1(t)=(1+t) [ -s_1(t)   c_1(t) ]
                  [ c_1(t)/t -s_1(t) ].                    (4)

On |t|=1, its row and column absolute sums are at most

    R0=2[(1+1/2)+(1+1/6)]=16/3.

Thus the finite compression R=P M_(r_1) P satisfies ||R||<=R0, uniformly in m.

A direct multiplication gives

    a r_1-I = [ d-1   t h ]
                [ h     d-1 ],
    d=c c_1-t s s_1,    h=s c_1-c s_1.                     (5)

The sum of the two series tails is at most sum_(k>=4)1/k!=e-8/3. Since |c|+|s|<=e, the pointwise matrix norm of (5) is at most

    delta=e(e-8/3)<1/4.                                   (6)

For an elementary bound sufficient for the strict inequality, use e<11/4, which gives delta<11/48<1/4. Multiplication by the error in (5) is a bounded operator on H_m with exactly this norm bound, independent of the weight.

## 3. Only five boundary directions are lost by compression

Every component of r_1 times a vector in P_m has powers between -1 and m+2. More precisely:

* both components may acquire powers m+1 and m+2;
* only the second component may acquire power -1.

The latter coefficient depends only on the constant coefficient of the first input component. Hence r_1 P_m lies in the algebraic extension

    P_m + span(t^(m+1)e_1,t^(m+2)e_1,
               t^(m+1)e_2,t^(m+2)e_2,t^(-1)e_2).

Applying I-P to this space has rank at most five. Orthogonal projection may change the lower coefficients, but cannot increase this quotient-space dimension.

Compression of (5) now gives the exact identity

    A R=I+E-F,
    ||E||<=delta,  rank F<=5,                              (7)

where

    E=P M_(a r_1-I)P,
    F=P M_a(I-P)M_(r_1)P.

All terms are well-defined on the finite space. The multiplier product a r_1 has its pole canceled; the separate Laurent-polynomial terms are integrable as observed after (2). No bound for the full multiplier M_a on H_m is assumed.

The finite-rank correction is also uniformly bounded, although this is not needed for the singular-value count:

    ||F||<=1+delta+C0 R0,

by (7), (2), and ||R||<=R0.

## 4. Uniform singular-value bounds except for five or six modes

Singular values are ordered decreasingly. On ker F, of dimension at least N-5, equation (7) implies

    ||A R x||>=(1-delta)||x||.

The singular-value min-max principle and
s_j(A R)<=||R||s_j(A) therefore prove

    s_(N-5)(A)>=(1-delta)/R0>=sigma_*:=9/64                 (8)

whenever N>5. Equivalently at most five singular values can be smaller than sigma_*. For smaller N the assertion is understood as a count, not a negative index.

Now retain the exact unit vector v and high compression from the previous odd note:

    v=G^(-1/2)e_0/sqrt((G^(-1))_(0,0)),
    Pi=I-vv*,
    B=Pi A restricted to v-perpendicular.

Unitary coordinate transport from P_m is implicit. Define R_B=Pi R restricted to the same subspace. From (7),

    B R_B=I+Pi E Pi-F_B,
    F_B=Pi F Pi+Pi A v v*R Pi,
    rank F_B<=6,    ||R_B||<=R0.                           (9)

Thus at most six singular values of B can be smaller than sigma_*:

    s_(N-7)(B)>=sigma_*       when N>7.                    (10)

Its norm is at most C0. The actual B is already proved invertible; (10) is the new quantitative information. It does not bound its remaining six inverse singular values.

## 5. The odd scalar depends, up to constants, only on those exceptional modes

The passed added-column theorem makes A invertible, and the high-row argument makes B invertible. Let

    a_1>=...>=a_N>0          be the singular values of A,
    b_1>=...>=b_(N-1)>0      be those of B.

The scalar s_m in the preceding note obeys det A=det B s_m in an orthonormal basis starting with v. Hence

    |s_m|=prod_i a_i / prod_j b_j.                         (11)

A codimension-one orthogonal compression has the two inequalities

    a_i>=b_i>=a_(i+2),      1<=i<=N-2.                    (12)

The upper inequality follows from projection and restriction. For the lower one, extend B by zero on v: A-Pi A Pi has rank at most two, and singular-value rank interlacing gives the claim.

For N>=8 set k=N-7. From (12), (8), and ||A||<=C0,

    1 <= prod_(i=1)^k a_i/b_i
       <=a_1a_2/[a_(k+1)a_(k+2)]
       <=(C0/sigma_*)^2.                                  (13)

Therefore (11) is, up to fixed positive factors, the ratio of the seven smallest singular values of A and the six smallest of B. The first two of those seven A values are themselves between sigma_* and C0. Define the ratio of only the potentially small modes by

    T_m=
       [prod_(i=N-4)^N a_i] /
       [prod_(j=N-6)^(N-1) b_j].                           (14)

Equations (11)-(13) give the explicit uniform bounds

    sigma_*^2 T_m <= |s_m| <= (C0^4/sigma_*^2) T_m.         (15)

Thus the odd-degree root-product target is now exactly

    log T_m=o(m).                                          (16)

The equivalence follows from (15) and the previously proved
V_n(1)/[t^n]V_n=B_m^odd s_m. No product of a growing number of uncontrolled comparison constants remains.

## 6. What this closes and what remains

The uniform indefinite Hermitian gap alone did not control the inverse of B. The explicit inverse symbol (3) adds a distinct fact: after a fixed truncation, all possible small singular values lie in at most six boundary modes. This is an operator-specific statement, not an inference from bandwidth, sign, or finite numerical data.

Neither the finite-rank identity nor all-index invertibility excludes exponentially small singular values in those exceptional modes. A new estimate for the fixed tail ratio (14), or a direct stable boundary determinant, is still required. The exact dyadic value of s_m does not supply such an Archimedean estimate.

All identities hold at the fixed exponential parameter 1. No assertion about an interval of deformed exponential parameters is made. No canonical degrees or singular-value samples were constructed; the proof is the exact parity-symbol calculation, the constant truncation, and finite-dimensional singular-value inequalities.
