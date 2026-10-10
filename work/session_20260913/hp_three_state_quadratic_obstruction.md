> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A determinant obstruction to rational quadratic invariants

Date: 2026-09-13. Original bounded continuation of the exact h,E
three-state recurrence. The main theorem below is unconditional and
uses only rational-function degree. The separate symbolic search has
a deliberately restricted scope. No prime scan was performed.

## 1. Exact system and the class of invariants considered

Let S_n=(h_n,h_(n-1),E_n)^T. The preceding arithmetic note proves

    S_(n+1)=T(n)S_n,
    T(n)=1/2 [[-3n,n^2,n^2],
              [2,0,0],
              [2-n,n^2,-n(n+2)]],
    det T(n)=n^3(n+1)/2.                              (1)

We investigate a rational bilinear similitude matrix: a matrix
Q(n) in Mat_3(K(n)), not identically zero, and a nonzero rational
multiplier rho(n) such that

    T(n)^T Q(n+1) T(n)=rho(n) Q(n).                    (2)

Here K is a field of characteristic different from two, and n is an
indeterminate. Symmetric Q gives a homogeneous quadratic relation.
Equation (2) is an identity of rational functions and holds for all
state vectors. It is stronger than an identity imposed only on the
particular arithmetic orbit. That distinction matters below.

## 2. No nondegenerate rational bilinear similitude exists

**Theorem.** Every Q satisfying (2) is singular. This holds without a
degree bound, without specifying rho in advance, and without assuming
symmetry.

**Proof.** Suppose det Q is nonzero. Taking determinants in (2) gives

    (det T(n))^2 det Q(n+1)=rho(n)^3 det Q(n).          (3)

For a nonzero rational function f, define deg f as the degree of its
numerator minus the degree of its denominator. Translation preserves
this degree: deg f(n+1)=deg f(n). Since deg det T=4, comparing degrees
in (3) gives

    8=3 deg rho.

This is impossible because deg rho is an integer. Q must be singular.
No asymptotic expansion, difference-Galois theorem, or finite
computation is used. The argument remains valid over F_p for every
odd p, as an identity in the rational function field F_p(n). QED.

In particular, this is not a statement about identities required only
at the finitely many residue indices. An identity modulo X^p-X, or a
quadratic certificate defined solely on the finite orbit, need not be
an identity of rational functions in an indeterminate and can evade
the degree argument. Such finite-orbit certificates remain possible.

In characteristic zero an additional independent divisor check gives
the same obstruction. Sum finite valuations over the integer shift
orbit n in Z. The quotient det Q(n+1)/det Q(n) has total zero, while
(det T)^2 has total eight. A cube has total divisible by three.
The degree proof is shorter and also covers positive characteristic.

Thus a preserved nondegenerate rational conic cannot be used to
exclude the projective common-root state [0:1:n]. Searching for such
a conic with higher rational degrees cannot overcome this obstruction.

## 3. Rational gauges and factorial normalizations do not fix it

Consider any transformed transition

    T_tilde(n)=sigma(n) R(n+1)T(n)R(n)^(-1),            (4)

where R is an invertible rational matrix and sigma is a nonzero
rational function. Since translation preserves the degree of det R,

    deg det T_tilde=4+3 deg sigma.

A nondegenerate rational bilinear similitude for this transition
would require

    2(4+3 deg sigma)=3 deg rho,

again impossible modulo three.

This covers a common scalar normalization of all state coordinates
whose successive ratio is rational, including ordinary factorial and
hypergeometric scalar normalizations, together with arbitrary rational
changes of coordinates. The natural exponential-generating-function
state

    (h_n/n!, h_(n-1)/(n-1)!, E_n/n!)

is included: its gauge is (1/n!) diag(1,n,1). The new determinant is
n^2/(2(n+1)), of degree one, and the same contradiction becomes
2=3 deg rho.

This statement does not cover arbitrary different factorial powers
assigned independently to the three coordinates. Such transformations
need not be a rational matrix times a common scalar; a rational
invariant in those coordinates can correspond to nonrational entries
in the original coordinates. No nonexistence statement for that larger
class is made.

## 4. The remaining degenerate possibilities

For a symmetric matrix Q of rank two satisfying (2), its one-dimensional
radical is an invariant rational line: if Q(n)v(n)=0, then

    Q(n+1) T(n)v(n)=0.

Indeed multiply (2) by v and use invertibility of T(n)^T. Thus a
rank-two quadratic form would require a rational line of the original
three-dimensional difference module.

A symmetric rank-one rational matrix can be written c(n)w(n)w(n)^T
with rational c,w: choose a nonzero diagonal entry and use vanishing
of its two-by-two minors. Equation (2) then forces

    T(n)^T w(n+1)=alpha(n)w(n)

for a nonzero rational alpha. Thus this case requires a rational line
of the dual system. A rank-two skew form also has an invariant radical
line. These observations reduce the remaining search but do not prove
that such lines are absent.

An exploratory hypergeometric-solution routine applied to the exact
third-order scalar recurrence returned no solution. No independently
verified completeness certificate was extracted from that routine;
therefore no irreducibility or absence-of-rational-lines theorem is
claimed from its output.

The determinant argument also does not rule out an affine quadratic
identity with lower-degree terms, an inhomogeneous pairing, or a
relation valid only on the particular initial-state orbit. For an
affine quadratic similitude, however, the highest homogeneous matrix
still satisfies (2) and therefore has to be singular.

## 5. A completed bounded symbolic search

Before execution, the following finite ansatz was fixed:

* Q is symmetric or skew-symmetric, with polynomial entries of degree
  at most six;
* rho is one of

      1;
      -n^a(n+1)^(2-a),                 a=0,1,2;
      n^a(n+1)^(4-a)/4,                a=0,1,2,3,4.

For each choice the polynomial identity

    (2T)^T Q(n+1)(2T)-4rho Q(n)=0

was expanded and every coefficient through degree ten was equated.
These are exact rational linear systems with 42 symmetric or 21
skew unknown coefficients. All eighteen systems have nullity zero.
Degree ten includes every possible coefficient because both sides
have degree at most 6+4.

The full specification and result are saved in
`check_hp_three_state_invariant_ansatz.py` and
`hp_three_state_invariant_ansatz_checks.json`. This is a proof of
nonexistence within those eighteen explicit polynomial ansatz classes
only. It does not extend the theorem to arbitrary degenerate rational
forms: clearing a general denominator changes the multiplier by a
shift quotient, which was not included automatically in this finite
list.

## 6. Return to the actual arithmetic gate

For 1<=r<=p-2 the already proved necessary and sufficient common-root
condition is

    [h_r:h_(r-1):E_r]=[0:1:r].                         (5)

The present theorem removes a specific proposed method: no
nondegenerate rational bilinear similitude of the entire three-state
system can exclude this state, even after the natural factorial
normalization. It does not establish whether the actual orbit reaches
the state at any additional index.

The exact outstanding finite-field certificate therefore remains

    gcd((X^p-X)/(X^2-1),
        H_p(X), H_p(X+1)+E_p(X+1))=1,

with the explicit H_p,E_p defined in the preceding note. A useful
continuation would be a proved degenerate or orbit-specific relation,
or a direct Bezout/nonvanishing argument for these particular
polynomials. Neither the failed finite ansatz nor the proved
nondegenerate-form obstruction supplies that missing certificate.

The two-branch conjecture, the odd auxiliary-gcd divisibility, and the
original large-prime endpoint-gcd exclusion remain unproved.
