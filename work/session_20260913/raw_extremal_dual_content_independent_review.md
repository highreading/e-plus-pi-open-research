> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the extremal dual polynomial and content identity

Date: 2026-09-13. Reviewer: audit_sources.

Reviewed `raw_extremal_dual_polynomial_and_content_identity.md`
against the actual integer matrices, the reviewed full-rank
extremal theorem, the finite-difference Smith reduction, and the
raw Legendre moment normalization.

**Verdict: all mathematical claims pass.** In particular the
global integer identity, with the stated row and cofactor orders,
is exactly

    mathcal E_n=(-1)^n F_n Z_n.

No prime-power factor or sign is missing. The simultaneous
denominator and its large-prime ledger are actual objects of the
given family. The note does not establish their saturation or a
bound on the extremal content.

Two optional clarifications were sent to the author: the integer
coefficient content c_n^Q already divides Z_n, so the denominator
formula may be simplified to |Z_n|/c_n^Q; and the final Legendre
discussion can distinguish the largest possible monic-basis
denominator prime, at most 4n-1, from norm factors reaching 4n+1.
Neither clarification changes the theorem or repairs an error.

## 1. Primitive polynomial and the factorial convention

The signed maximal-minor vector of a full-column-rank
(2n+1)-by-(2n) matrix spans its left nullspace. Dividing by
the positive gcd gives the stated primitive integer vector,
with its sign fixed rather than chosen afterwards.

For the integer exponential column (k)_j, the equation is
sum w_k(k)_j=W_n^(j)(1)=0. Together with support k>=n this
gives z^n(z-1)^n as a factor of W_n. Both monic divisions are
integral, and Gauss's content formula makes V_n primitive.
No exact degree or nonzero endpoint for V_n follows or is used.

Dividing matrix row k by k! changes its left vector to the
coordinate k!w_k. The note keeps this convention consistently:
W_n uses w_k, while T_n and the reversed denominator use the
factorial-multiplied coordinates.

## 2. The raw moment and shifted factorial conditions

The normalization

    L(z^a)=(1/(2i)) integral_(-i)^i z^a dz=tau_(a+1)

is correct: for even a it is (-1)^(a/2)/(a+1), and for odd
a it is zero. For arctangent column j, set s=n-j-1; the
resulting sum is exactly L(z^s T_n), with 0<=s<=n-1.
All indices are nonnegative and all required tau subscripts
are positive.

Over Q the monic raw Legendre polynomials are orthogonal with
nonzero norms, so the first n moment vanishings remove exactly
the Q_0,...,Q_(n-1) components. This proves the stated span
through Q_(2n), without identifying T_n with one basis member.

For exponential column j, s=n-j runs from 1 to n and gives
sum [z^r]T_n/(r+s)!. The beta integral applied to a coefficient
q_r z^r/r! of F_l yields q_r/(r+s)! after division by
(s-1)!, proving (9) with its exact normalization.

## 3. Reversed simultaneous denominator and uniqueness

Every coefficient of Qhat_n is integral because k!/n! is an
integer. At p>3n these multipliers are units, so primitivity
of w implies that at least one coefficient of Qhat_n is a
p-unit. Reversal does not combine coefficients and therefore
cannot introduce cancellation into this assertion.

At degree 3n-j, the reversed exponential coefficient is
(1/n!) sum k!w_k/(k-j)!, exactly an X_n column equation.
The arctangent coefficient uses the same sum with tau_(k-j).
As j runs from 0 to n-1 these are precisely degrees
2n+1,...,3n. Conversely all such degree-at-most-2n denominator
coefficients reverse to a rational left vector of X_n by
undoing nonzero factorials. This is a linear bijection, so the
solution space is exactly one-dimensional over Q.

These are coefficient conditions at the origin, not an
assertion about an approximation value at the endpoint. In
particular nonvanishing of Qhat_n(1) needs the separate
argument supplied next.

## 4. Full global determinant sign and content

For one polynomial, the coefficient change from degree-at-most-n
B to ((z-1)b+beta) has basis determinant (-1)^n in the order
(b_0,...,b_(n-1),beta). Two such blocks have total determinant
one. Moving beta past the n c columns gives the final coordinate
change determinant (-1)^n in the order used in the note.

After unscaling the high rows, the endpoint rows become the
identity on beta,gamma. The remaining high block is exactly
D X_n^0 with rows e_r-e_(r+1). Since D has 2n rows, its minor
omitting column r is (-1)^(2n-r)=(-1)^r. Finite Cauchy-Binet
therefore sums the signed cofactors with no extra alternating
factor.

If P_n=prod_(k=n)^(3n)k!, deleting row k from the unscaled
matrix multiplies its cofactor by k!/P_n. Thus

    det(D X_n^0)=(F_n/P_n) sum k!w_k.

The coordinate sign makes the unscaled endpoint determinant
(-1)^n times this expression. Restoring its original high
row factors multiplies by P_n/n!, leaving exactly
(-1)^n F_n sum(k!/n!)w_k=(-1)^n F_n Z_n.

The archive appends B(1) after C(1)-4B(1). Replacing the latter
by C(1) and then exchanging the two endpoint rows gives its
Delta_B=-mathcal E_n, as stated. No additional determinant
normalization is being inferred from a coordinate cofactor.

Since the actual endpoint determinant is nonzero and F_n>0,
this proves Z_n is a nonzero integer and F_n divides that
endpoint determinant globally. The factorial integral formula
for Z_n follows by integrating each monomial. Its convergence
does not imply a positive integrand and is not used for a
sign or nonvanishing argument.

## 5. Cross product and exact prime-power ledger

The nonzero endpoint determinant gives unique rational type-I
triples for endpoint pairs (1,0) and (0,1). Their cross product
has degree at most 2n. Substituting their two high-order
remainders gives exactly

    S_1-S_0 exp(z)=O(z^(3n+1)),
    S_2-S_0 arctan(z)=O(z^(3n+1)).

The signs in both equations agree with the displayed cross
product. Since S_0(1)=1, it is nonzero; uniqueness of the
simultaneous denominator and the already proved Z_n!=0 give
S_0=Qhat_n/Z_n. Replacing the first triple by the canonical
(1,4) solution does not change this cross product with the
(0,1) triple.

The least coefficient denominator of this rational polynomial
is |Z_n|/gcd(|Z_n|,c_n^Q). In fact c_n^Q divides Z_n because
Z_n is the sum of the coefficients, so this is |Z_n|/c_n^Q.
At every p>3n, c_n^Q is a unit by Section 3. Taking valuations
of the exact global factorization therefore proves

    v_p(mathcal E_n)=v_p(F_n)+v_p(d_n^II)
                    =v_p(theta_n)+v_p(d_n^II).

This preserves arbitrary prime-power depth. The final equality
uses the previously reviewed m=n finite-difference reduction,
which preserves the relevant determinantal ideal at p>3n.
It does not follow merely from equality of ranks modulo p.

The proposed scalar equality with the endpoint exponent is
equivalent to F_n being a unit at that prime. It is a sufficient
condition for the original high content to be a unit through
the separately proved inequality, not a proved converse to
that inequality.

## 6. Small controls and the Legendre localization obstruction

The stated n=1 signed cofactor vector reproduces the three
original rows and yields Z_1=-2 and mathcal E_1=2. The n=2
vector satisfies both exponential equations and both
arctangent equations with the indicated factorial factors.
Its reversed polynomial has content 4, value 16432 at 1,
and coefficient denominator 4108. These checks use only the
recorded degrees and are not an additional scan.

The monic recurrence coefficient at step l has denominator
(2l-1)(2l+1). Building the monic basis through degree 2n
uses steps through l=2n-1 and can already introduce primes
up to 4n-1. For example Q_4 contains the denominator 7,
which lies above 3n when n=2. Norms through degree 2n can
add the factor 4n+1. Thus a full rational orthogonal-basis
and norm transformation is not automatically unimodular at
every p>3n. This is an actual obstruction to an unqualified
large-prime recurrence argument, not a claim that every such
prime divides a particular content.

The polynomial moment equations themselves only use tau
subscripts through 3n, so they do remain valid over Z_p at
the stated prime threshold. Keeping those equations while
declining to assume a p-unit Legendre change of basis is
the correct distinction. No ordinary three-term recurrence
for the combined cofactor solution or for its content has
been established by this identification.
