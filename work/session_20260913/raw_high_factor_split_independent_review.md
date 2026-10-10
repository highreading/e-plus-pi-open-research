> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: high-factor split and individual parity rank

Date: 2026-09-13. Reviewer: audit_sources.

**Result: pass.** I checked `raw_high_factor_split_and_parity_rank.md`
against the actual Krylov construction and parity-domain dimensions
in `raw_high_multipoint_complementary_reduction.md`. Its rank bounds,
cross-cut rank identities, and polynomial Loewner comparison are
correct. None gives the still-missing combined-channel rank or
angle estimate.

## 1. Actual split and support test

The chosen j_n is the largest integer with j_n(j_n+1)<=2n.
For l>j_n the positive difference l(l+1)-2n is an even integer,
so it is at least two. The actual node bounds therefore give
xi_l-(2n+3/4)>=2. Each factor xi_l I-K_(2n) is positive
definite, and their commuting product F_sigma(K) is positive
definite, including the empty product.

The actual domains have dimensions d_sigma=n-m_sigma. Their
columns are indeed the low-coordinate projections of
F_sigma(K)L_sigma(K)u(K)v_sigma, up to one harmless column
sign. The seed v_1=e_1-(sqrt(3)/2)e_0 must be retained; the
note does so. No spectral amplitude is absorbed in this
factorization.

For a polynomial p of degree k, the highest possible coordinate
of p(K)v_sigma is 2k+sigma. If that index is at most n, it
lies inside the retained block and the leading contribution is
nonzero: the length-k path using only the outer +2 band has
nonzero product, lower powers cannot reach that index, and
the e_0 part of v_1 cannot reach 2k+1. This also gives a direct
proof of the needed triangular injectivity without an additional
rank assumption.

Thus if deg(L_sigma u)<=q_sigma, its vector w is supported in
the low coordinates and is nonzero whenever u is nonzero.
The equation P_L F_sigma(K)w=0 would imply w^T F_sigma(K)w=0,
contradicting positivity. This proves injectivity on precisely
the restricted polynomial subspace used in the note.

## 2. The offset counts

That subspace has dimension
max(0,min(d_sigma,q_sigma-ell_sigma+1)). Subtracting from the
full domain dimension gives exactly (10), with its outer cap.
The four offsets in (11) check as follows:

    n=2r:   (d_0,d_1)=(r-1,r), (q_0,q_1)=(r,r-1),
    n=2r+1: (d_0,d_1)=(r,r),   (q_0,q_1)=(r,r).

Consequently the losses are ell_0-2 and ell_1 in even degree,
and ell_0-1,ell_1-1 in odd degree, each floored at zero and
capped at its actual domain dimension. The n=2 empty zero-channel
domain is included correctly. These are bounds on the individual
maps, not a bound on their juxtaposition.

The support lemma in Section 3 is also correct: the positive
principal a-by-a block makes the first a rows restricted to the
first a+r columns surjective, leaving kernel dimension r. For
literal completeness its proof can assume a+r<=N; if a+r>N,
replace r by N-a<=r and the conclusion is immediate. The
author has incorporated this statement clarification. It does
not change any application here.

## 3. Exact cross-cut rank

For a polynomial f of degree h with 2h<=n+1, the proposed
minor uses rows starting at n+1-2h and columns starting at n+1.
All selected indices lie in the appropriate low and high blocks.
For row/column offsets i,j, their separation is 2h+j-i, so
entries above the diagonal vanish by bandwidth. The diagonal
entry is the leading coefficient of f times the unique all-+2
path product in (15). It is nonzero and remains within the
finite compression throughout the path. Lower-degree terms
cannot reach that distance.

This proves a minor of size min(2h,n-1) is nonsingular. The
matching upper bound follows because only the last 2h low
rows can couple across the cut and there are n-1 high columns.
The h=0 case is a zero cross block. The actual high factors
satisfy the degree hypothesis because both zero and one were
included in the exceptional low set.

For a positive definite F, its principal block and Schur
complement are invertible, so the block-inverse formula
preserves the rank of F_LH exactly. This proves the same
cross-cut rank for the inverse factors.

These are statements about the full polynomial operators and
their inverses. They do not show that a particular restricted
Krylov family realizes that rank. The note explicitly preserves
this limitation, so its large-rank obstruction does not become
an unsupported assertion about the actual combined Z_L.

## 4. Interlacing and polynomial comparison

The high nodes form a consecutive alternating list of actual
parities. Their strict ordering follows already from the given
upper and lower node bounds. If their counts differ, deleting
the final node of the longer list leaves equal alternating
lists. Moving that root into the corresponding low factor
preserves its full node polynomial, with the already specified
overall sign, and raises one low degree by one.

For the resulting order alpha_1<beta_1<...<alpha_h<beta_h
and t<=M_n, every factor is positive. The upper product bound
is termwise. The lower product bound cancels the inequalities
alpha_i-t>=beta_(i-1)-t for i>=2, leaving
(alpha_1-t)/(beta_h-t). This ratio decreases with t, so its
minimum over the row spectrum occurs no earlier than M_n.
The numerator there is at least two and the denominator is
at most n^2. This proves the scalar ratio bounds in (19)-(20).

Both positive factors are polynomials in the same symmetric K,
so they commute. Functional calculus therefore gives both the
ratio Loewner inequality and the inequality between the factors
themselves. It does not rely on multiplying arbitrary Loewner
inequalities by a noncommuting matrix. The empty equal-degree
case is the identity and satisfies the same bound for n>=2.

The two-dimensional example in (21) checks exactly: the original
vectors are independent, the two factors are positive definite,
and their images coincide. It correctly disproves a general
inference from factor comparability to independence of the
two transformed image spaces. It is not presented as an actual
counterexample to the research matrix.

## 5. Retained research obstruction

The proved progress is an O(sqrt n) individual rank loss, a
polynomial comparison of the two high factors, and an exact
n-O(sqrt n) full-operator cross-cut rank. The unresolved task
is still the intersection or angle of the two actual projected
image spaces, with the original amplitude-weighted cardinal
vectors retained. A positive inverse for the full Z_L Gram
matrix, the desired near-one cardinal determinant, and an
irrationality conclusion have not been inferred from these
separate results.

No new degree, node, or numerical root scan was used in this
review.
