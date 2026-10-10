> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the high multipoint complementary reduction

Date: 2026-09-13. Reviewer: audit_results.

Reviewed raw_high_multipoint_complementary_reduction.md in full,
focusing on Sections 2--5 and checking the subsequent Green and
Schur formulas. The substantive statements pass. One small scope
clarification was requested: impose 0<=epsilon_n<=1 in the converse
following (18). The intended asymptotic small-error application
already has this property. The displayed projector also has a
typographical 'qquad' to replace by the intended separator.
Both clarifications have now been applied by the author. No
remaining correction is requested.

## 1. Exact vanishing basis and coefficient orientation

For the first 2n branch rows, both component degree caps are n-1.
Distinct nodes within each parity channel make the vanishing space
exactly the pairs whose respective components are divisible by
Q_0 and Q_1. Its dimension is 2n-(n+1)=n-1. I checked the top
interleaved indices for even and odd n; they are exactly n+1
through 2n-1. At n=2 the absent zero-channel range causes no
exception.

Because branch row k has new leading coefficient ell_k>0, a monic
vanishing vector with highest index k has coefficient 1/ell_k on
that row and no coefficients above it. With these vectors as
columns, the high coefficient block is upper triangular, not lower.
Its determinant is h_(n+1)^p/h_(2n)^p. The transpose orientation
then gives

    Y_hi=-Z_H^(-T) Z_L^T Y,
    H=-Z_H^(-T) Z_L^T S.

The finite Krylov coefficient columns are Q_sigma(K_(2n)) K_(2n)^j
v_sigma, with v_0=e_0 and v_1=e_1-(sqrt3/2)e_0. The largest
power involved is n-1; every intermediate path remains below
index 2n. Symmetry of K correctly changes the inverse coefficient
rows to these coefficient columns. Thus there is no finite
compression error in this identity.

## 2. Cardinal normalization and complementary-minor sign

The amplitude-weighted cardinal coefficient vector is a_l=S^(-T)e_l.
Its associated polynomial must therefore have value 1/g_l at its
own channel node and zero at every other selected node. This
confirms the exact factor 1/g_l in (10).

For T=Z_L^T S, appending e_j^T,e_k^T produces the determinant
(-1)^(j+k+1) det T[:,I]. Multiplication of
[Z_L,a_j,a_k]^T by S gives precisely this appended matrix.
The additional factor from H is (-1)^(n-1)/det Z_H. These
combine to the stated sign (-1)^(n+j+k), with the common
factor h_(2n)^p det(S)/h_(n+1)^p. No pair-dependent amplitude
or Vandermonde factor has been discarded.

## 3. The normalized two-dimensional determinant

Assuming rank Z_L=n-1, P_Z is the orthogonal projector onto its
two-dimensional orthogonal complement. The congruence
C=S^(-1)P_ZS^(-T) is positive semidefinite of rank two, with
image exactly ker H. It is not generally an orthogonal projector;
the note correctly uses its second elementary symmetric function
to normalize it.

For orthonormal columns V spanning ker Z_L^T and N=S^(-1)V,
one has C=NN^T and e_2(C)=det(N^T N)>0. This proves the
ratio in (16). The Gram determinant Schur complement also gives
the exact identity (14). Orthonormalizing N shows that the ratio
is the square of the last two-coordinate determinant, hence the
product cos^2(theta_1) cos^2(theta_2).

For 0<=epsilon<=1, a product at least 1-epsilon^2 makes each
factor at least that value, giving the claimed low projection
bound. Conversely, that projection bound gives each factor at
least 1-epsilon^2 and thus the product at least its square.
The explicit interval for epsilon is needed for this converse
as a literal finite statement; otherwise epsilon>1 could give
an impossible lower bound exceeding one.

Cauchy--Binet together with the complementary-minor identity
proves (19). The growing inverse Z_L^T Z_L has not disappeared
from the two-dimensional representation, and its rank is
appropriately left as an assumption rather than a conclusion.

## 4. Boundary-only Gram and Schur reductions

The exact Green identity over rows n+1,...,2n-1 has cuts n+1
and 2n with opposite signs. This gives (20), with the derivative
in the second variable on the diagonal. The identity is polynomial
at apparent poles of rational transfer formulas. Defining the
boundary columns as in the note gives

    GX-XG=C_(2n)^T B_(2n)-B_(2n)^T C_(2n)
          -C_(n+1)^T B_(n+1)+B_(n+1)^T C_(n+1).

Each of the four products has rank at most two, proving the rank
eight displacement bound. Positive semidefiniteness of this
particular difference follows from its actual high Gram definition,
not from subtracting arbitrary positive kernels.

For the parity block partition, A>0 makes the Schur complement
positive semidefinite; its strict positivity is equivalent to
invertibility of the full designated low-node Gram block. Under
that condition the two graph right sides in (24) follow from
block elimination and are exactly the kernel graph. Every
amplitude factor is retained through G=H^T H.

If B>0 as well, the eigenvalues of the normalized Schur matrix
lie in [0,1]. A determinant at least d>0 therefore makes its
least eigenvalue at least d, giving S>=dB. The individual
parity inverses and the projected right sides remain necessary
additional estimates. The empty odd block at n=2 is handled
correctly by the stated convention.

## 5. Scope

This is a sound exact reduction of the prescribed high interval,
with its true node polynomials, channels and amplitudes. It does
not prove the rank of Z_L or a quantitative estimate for its
projected cardinal determinant. The single-parameter branch
conditioning theorem cannot substitute for any of those mixed-node
estimates. The source note preserves this remaining obstruction.
