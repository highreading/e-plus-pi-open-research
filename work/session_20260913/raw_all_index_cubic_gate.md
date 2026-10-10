> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# All-index cubic degree and triple-root exclusion for the canonical raw family

Date: 2026-09-13. Verified theorem summary and dependency index.

For every n>=1, use the unique canonical raw Hermite–Padé triple

    R_n=A_n+B_n exp(z)+C_n arctan(z)=O(z^(3n+1)),
    deg A_n,deg B_n,deg C_n<=n,
    B_n(1)=1, C_n(1)=4.

Write a_j,b_j,c_j for its actual polynomial coefficients. Put
phi(j)=v_2(j!) and

    Xi_n=a_n c_(n-1)-(a_(n-1)-c_n)c_n.

The following exact results are now proved and independently reviewed:

    v_2(a_n)=-n,
    v_2(c_(n-1))=-n-2phi(n-1),                      (all n>=1)

    v_2(b_n)=3                                      (n=1),
    v_2(b_n)=v_2(n-1)                               (n>=5, n=1 mod4),
    v_2(b_n)=0                                      (other n>=2),

    v_2(Xi_n)=-2n-2phi(n-1)+2                      (n=1 mod4),
    v_2(Xi_n)=-2n-2phi(n-1)-2                      (n=2 mod4),
    v_2(Xi_n)=-2n-2phi(n-1)                        (n=0 or3 mod4).

The first Xi branch includes n=1 by the separate exact value Xi_1=-29.
In particular a_n,b_n,c_(n-1),Xi_n are nonzero at every index.

The exact Wronskian polynomial is

    Q_n=(1+z^2)^2 exp(-z) W(R_n,B_n exp(z),C_n)
                                             /z^(3n-1),

with deg Q_n<=3 and

    [z^3]Q_n=b_n Xi_n.

Consequently deg Q_n=3 for every n>=1. The cubic-stratum scalar and
Volterra transfer formulas therefore have their degree hypothesis
at every current index. This statement does not imply distinct roots,
root separation, avoidance of fixed singularities, or any uniform
absolute-value bound on their coefficients.

There is now a further independently reviewed all-index theorem.
Write q_3,q_2,q_1 for the top three coefficients of this same Q_n.
At the canonical scale, the exact Hessian valuation is

    v_2(q_2^2-3q_3q_1)=2v_2(Xi_n),                 (all n>=1).

Thus (q_2^2-3q_3q_1)/Xi_n^2 is a dyadic unit. In particular
Q_n has no triple root over the algebraic closure of Q at any index.
The scale-invariant normalized valuation is

    v_2((q_2^2-3q_3q_1)/q_3^2)=-6                  (n=1),
    v_2((q_2^2-3q_3q_1)/q_3^2)=-2v_2(n-1)         (n>=5, n=1 mod4),
    v_2((q_2^2-3q_3q_1)/q_3^2)=0                  (other n>=2).

Full squarefreeness remains open: a double root is not excluded by
this Hessian theorem. The theorem also implies that Q_n(1),
Q_n'(1),Q_n''(1)/2 cannot all vanish, so their integer gcd after
a common integral scaling is nonzero. No bound for its magnitude
or prime-power factors follows here.

## Proof and review dependencies

1. `raw_leading_B_dyadic_all_indices.md`, reviewed in
   `raw_leading_B_all_indices_independent_review.md`. Its integral
   interpolation lemma includes every multiple row replacement and
   controls the actual appended leading-B coordinate determinant.
2. `raw_leading_A_dyadic_and_Xi_gate.md`, reviewed in
   `raw_leading_A_independent_review.md`. Its appended Taylor row
   retains the correct coefficient versus integer-minor factorial.
3. `raw_penultimate_C_even_dyadic.md` and
   `raw_Xi_even_dyadic.md`, reviewed together in
   `raw_Xi_even_independent_review.md`. These handle the modified
   C-pole sets and the exact cancellation-adapted reconstruction row.
4. `raw_Xi_odd_parity_supplement.md`, reviewed in
   `raw_Xi_odd_independent_review.md`. It extends the penultimate-C
   theorem to all odd degrees and resolves Xi at n=3 modulo4.
5. `raw_Xi_eight_row_set_reduction.md`, reviewed by root in
   `raw_Xi_eight_row_set_root_review.md`. It retains all contributions
   at the required valuation depth with the actual common denominator.
6. `raw_Xi_remaining_class_mod_eight.md`, reviewed in
   `raw_Xi_remaining_class_independent_review.md`. The effective
   four-Legendre cofactor vector retains the double replacement and
   both exceptional singles. Its unit two-by-two system gives a
   nonzero residue four modulo eight; the common scale is recovered
   from actual coefficient approximation, and the discarded terms
   lie strictly beyond the proved leading valuation.
7. `raw_B_coefficient_dyadic_divisibility.md` proves the uniform
   actual coefficient bound v_2(b_j)>=phi(n)-phi(j). It is the
   arithmetic input to the full moment argument in
   `raw_even_P_second_dyadic_gate.md`, proving both even-degree
   P coefficient gates without discarding any cofactor terms.
8. `raw_all_index_triple_root_exclusion.md` extends that moment
   argument using U'(0) at odd degree and compares the two Hessian
   terms separately in each residue class. The all-index proof was
   independently reviewed by audit_sources. Its first coefficient
   gate also has a separate determinant proof in
   `raw_even_P_first_dyadic_gate.md`, reviewed in
   `raw_even_P_first_gate_independent_review.md`.

The last proof uses the exact second-kind identities recorded in
`raw_Xi_top_block_factorization.md`. The cubic coefficient identity
and its original integer-minor normalization were independently
derived in `raw_homogeneous_ode_independent_review.md`.

No all-index assertion above rests on a finite degree scan. The
proofs do not estimate a whole remainder, a primitive denominator,
or the arithmetic nature of e+pi. Those are remaining mathematical
requirements, rather than consequences of this structural theorem.
