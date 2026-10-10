> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The high Smith exponent is bounded by the extremal content exponent

Date: 2026-09-13. Original root derivation; independent review requested.

Independent review now passes in
`raw_high_content_extremal_valuation_independent_review.md`.

Let H_n be the actual integer high matrix, with rows k=n+1,...,3n
and B,C columns of degrees at most n. Let X_n be the actual extremal
matrix, with rows k=n,...,3n and B,C columns of degrees at most n-1.
In either matrix the entries are

    (k)_j and k! tau_(k-j).

Write D_n for the positive maximal-minor gcd of H_n and F_n for
the positive maximal-minor gcd of X_n. The latter matrix is
(2n+1)-by-(2n). Its full characteristic-zero column rank is proved
below, so F_n is well defined and nonzero. For every n>=1 and
every prime p>3n, this note proves

    v_p(D_n) <= v_p(F_n).                              (1)

This includes the full prime-power exponent, rather than just the
implication between defective ranks modulo p. It gives no upper
bound on F_n itself and does not assert the converse divisibility.

## 1. No lower-degree extremal triple exists in characteristic zero

The established actual endpoint determinant Delta_B is nonzero:
see `sources/raw_arctan_endpoint_arithmetic.md`, Theorem 2.1, and
the explicitly retained determinant normalization in
`raw_B_coefficient_dyadic_divisibility.md`. Its square system
consists of the high rows H_n and the two rows

    B(1), C(1)-4B(1).

Equivalently it consists of H_n and B(1),C(1), by an invertible
constant row operation. Thus the only degree-at-most-n triple
with order 3n+1 and B(1)=C(1)=0 is the zero triple. The low
polynomial A is uniquely reconstructed from B,C in this assertion.

Suppose X_n had a nonzero rational kernel vector. Reconstruct A
through degree n-1. The row k=n, which has been retained in X_n,
and all subsequent rows through 3n give a nonzero triple T of
degree at most n-1 with remainder order at least 3n+1. The triple
(z-1)T has degree at most n, the same required order at the origin,
and both B,C endpoints zero. It is nonzero, contradicting the
endpoint determinant. Hence X_n has full column rank over Q.

This also shows that the characteristic-zero reduced module degrees
in `raw_shared_core_large_prime_saturation.md` are exactly
(n,n,n+1): its degree-at-most-n-1 slice is zero, so every reduced
basis row has degree at least n and their sum is 3n+1. The other
two listed profiles remain possible after reduction at a prime;
the characteristic-zero argument does not assert that Delta_B is
a unit at every such prime.

## 2. A primitive left annihilator at the full Smith depth

Fix p>3n and put e=v_p(D_n). If e=0, (1) is immediate. Assume
e>=1 and work over Z_p and its quotient R_e=Z_p/p^e Z_p.

All k! in the row range are units. Replace the integer matrices
by their unscaled Taylor matrices without changing any local
determinantal ideal. The entries in the B column j are
1/(k-j)! and those in the C column j are tau_(k-j). Every
subscript is positive in the respective ranges.

The reviewed high-rank theorem says that H_n has at most one
nonunit Smith invariant at p. Its local Smith form therefore has
an identity block of size 2n-1 and a final invariant p^e, with
two extra zero columns. Invertible row operations giving that
form supply a row vector

    w=(w_(n+1),...,w_(3n)) in Z_p^(2n)

such that

    w H_n=0 mod p^e,

and at least one coordinate of w is a unit. Indeed the last row
of a unimodular row transformation is primitive, and multiplication
by the invertible column transformation preserves the annihilation
congruence. This uses the full exponent e, not only the existence
of a left null vector modulo p.

## 3. The two shifted annihilators of the extremal matrix

Index the 2n+1 rows of X_n by n,...,3n. The two vectors

    u=(0,w_(n+1),...,w_(3n)),
    v=(w_(n+1),...,w_(3n),0)                           (2)

both annihilate the unscaled X_n modulo p^e.

For u, restrict the H_n equations to its B,C columns j=0,...,n-1.
Those columns coincide with X_n on the overlapping rows, and the
coefficient of its extra first row is zero.

For v, instead use columns j+1 of H_n, again for 0<=j<=n-1.
The Taylor coefficient of z times either basis function in row k
is its original Taylor coefficient in row k-1. Thus these H_n
columns on rows n+1,...,3n are exactly the X_n columns on rows
n,...,3n-1. This proves the second assertion without inserting
row-dependent factorial factors: those factors were already
removed by unit operations in Section 2.

The rows u,v have a unit 2-by-2 minor. To see this, reduce modulo
p and let r be the earliest nonzero coordinate of w, using indices
0,...,2n-1 for w. The two columns r,r+1 of the rows (u,v) have
matrix, modulo p,

    [[0,w_r],[w_r,w_(r+1)]],

with the absent final coordinate interpreted as zero if necessary.
Its determinant is -w_r^2, a unit. Earlier coordinates of w need
only vanish modulo p, which is enough to prove this minor is a
unit in Z_p.

Consequently u,v can be extended to the rows of an invertible
(2n+1)-by-(2n+1) matrix over Z_p. One direct construction keeps
the two pivot columns of their unit minor and appends coordinate
rows for all other columns; after a column permutation the
determinant is that unit minor up to sign.

## 4. Every extremal maximal minor has the required divisibility

Apply this row transformation to X_n. Its first two rows are
entrywise divisible by p^e, because of (2). Any selection of 2n
rows out of 2n+1 must include at least one of those first two
rows. Every maximal minor of the transformed X_n is therefore
divisible by p^e. Unimodular row operations preserve its maximal
determinantal ideal, so every maximal minor of X_n has that
divisibility as well. This gives v_p(F_n)>=e and proves (1).

No implication from the number of nonunit factors to their sizes
was used. The size e was carried explicitly through the two
annihilator congruences and the unit-minor completion.

## 5. Relation to the smaller integer matrices and the remaining target

The independently reviewed finite-difference reduction gives,
at p>3n,

    v_p(D_n)=v_p(eta_n),

where eta_n is the maximal-minor content of the (n-1)-by-(n+1)
matrix G_n, with eta_1=1 for the empty 0-by-2 matrix G_1.
The corresponding extremal reduction with m=n
gives an identity block I_n and the (n+1)-by-n integer matrix
mathcal G^(n) in that note. Let theta_n be its positive
maximal-minor content; characteristic-zero full rank follows
from Section 1 and the reduction. Thus the equivalent smaller
content statement is

    v_p(eta_n)<=v_p(theta_n), p>3n,                    (3)

or (eta_n)_(>3n) divides (theta_n)_(>3n).

The earlier argument only forced a nonzero extremal solution
when H_n lost rank modulo p. Equation (3) now retains arbitrary
prime-power depth. It makes any future bound on the actual
extremal content sufficient for the unbordered high content.
The reverse implication or reverse inequality is not proved.

The all-index saturation of the augmented shared core remains a
separate theorem: its content zeta_n has no prime factors above
3n, whereas theta_n and eta_n may still have such factors. The
new result does not estimate their total logarithmic size, the
endpoint restriction content, or the primitive mixed remainder.
