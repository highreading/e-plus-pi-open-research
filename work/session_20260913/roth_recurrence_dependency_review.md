> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: recurrence dependencies and all-spacing observation determinants

Date: 2026-09-13. Scope: the proposed auxiliary zero-density theorem in
`fixed_prime_roth_density.md`; the Item237 differential identity; and the
Item309 extension to the second local branch. Roth's progression theorem
is an imported theorem and is not reproved here. The separate review of
quantifiers and coefficient-height bounds was assigned to the source agent.

**Verdict: ACCEPT the recurrence and all-spacing determinant inputs.**
The upstream recurrence is supported by an independently recomputed exact
zero-polynomial identity, not merely a stored status label. The limiting
cubic and its root-ratio argument are correct. I found no defect in the
argument that every fixed-spacing observation determinant is a nonzero
rational function. With the separately reviewed counting/height estimates
and the preceding nonzero-state theorem, these inputs support Z(p)=o(p)
and the stated auxiliary averaged upper-cap conclusion. They provide no
positive lower bound for Gamma and no proof concerning e+pi.

## 1. What was read and independently recomputed

I inspected the mathematical derivation and actual polynomial-operator
implementation in:

- `sources/item237_j1_algebraic_residual_report.md`, Sections2–5;
- `scripts/item237_j1_algebraic_residual_certificate.py`, particularly
  `RECURRENCE_FACTORS`, `shifted_theta`, and `operator_certificate`;
- `sources/item309_j2_l_second_branch_bridge_report.md`, Sections5–8;
- `scripts/item309_j2_l_second_branch_bridge_certificate.py`, particularly
  `second_branch_global_identities`;
- the full proposed `fixed_prime_roth_density.md`.

I then wrote and ran a separate checker:

    work/session_20260913/check_recurrence_dependency_independent.py

It imports no archived Python module, does not consult the stored zero
flag, and performs its own Fraction polynomial arithmetic. It reads only
the published factor lists from the Item237 JSON and reconstructs the
entire cleared differential numerator coefficient by coefficient.

Its saved result is

    work/session_20260913/recurrence_dependency_independent_checks.json.

The exact result is zero. The independently reconstructed cleared blocks
have degrees131,131,131,127; their sum is the zero polynomial, rather than
a polynomial sampled at finitely many arguments. It also recomputes the
parametric numerator N, the theta change of variable, the branch data,
the four leading coefficients, the cubic discriminant, and the two
integer nonsquare tests.

## 2. Semantic derivation of the Item237 differential operator

Write

    T(y)=y^2+2y+2,
    D(y)=2y^3+7y^2+14y+6,
    x=y(1+y)/(T(y)/2)^(2/3),
    C(x(y))=N(y)/D(y)^3,

where

    N(y)=432+2064y+4440y^2+5376y^3+4044y^4
          +1860y^5+486y^6+48y^7.

The source constructs this C from

    U_A=6(T/2)^2 A/D,
    U_B=6(T/2)^2 B/D,
    A=(20+14y+4y^2)/3, B=2-5y-3y^2,
    C=U_B+(x/2)dU_A/dx.

The independent checker verifies the resulting numerator is exactly N.
Thus it does not silently replace the source's algebraic function by a
different series chosen to fit the recurrence.

Direct differentiation gives

    theta=x d/dx=J(y)/D(y) *d/dy,
    J(y)=3y(1+y)T(y).

The polynomial identity behind this formula,

    3(1+2y)T-2y(1+y)T'=D,

was independently checked. For a rational function H/D^a,

    ((theta-6k)/2)(H/D^a)
      =[J(H'D-aHD')-6k H D^2]/[2D^(a+2)].              (1)

This is exactly the operation encoded by the archived `shifted_theta`.
Its denominator exponent increases by two at each step; beginning with
a=3 and using a degree16 polynomial in the operator gives exponent35.

The four reconstructed recurrence polynomials P_k have degree16. Define

    L=sum_(k=0)^3 x^(18-6k) P_k((theta-6k)/2).          (2)

After the differential operation, the remaining powers of x satisfy

    x^3=4y^3(1+y)^3/T(y)^2.

Writing u=6-2k, the factor x^(18-6k) is consequently

    4^u y^(3u)(1+y)^(3u)/T^(2u).

Here u is6,4,2,0, so all exponents are nonnegative. A common denominator
for (2) applied to C is exactly D^35 T^12. The four numerator blocks
constructed from (1), the full P_k coefficient lists, and these x powers
sum to zero in Q[y]. This was recomputed without invoking the old
`operator_certificate` function.

Therefore LC=0 as an actual rational-parametric differential identity.

## 3. Why the coefficient recurrence applies to odd indices too

Let C(x)=sum_(r>=0)b_r x^r. In the k-th term of (2), the coefficient of
x^(r+18) comes from b_(r+6k); the shifted theta operator acts there by

    P_k(((r+6k)-6k)/2)=P_k(r/2).

Thus the differential identity gives

    sum_(k=0)^3 P_k(r/2)b_(r+6k)=0                    (3)

for every integer r>=0. The original report emphasizes its even-index
interpretation h=r/2, but the derivation does not impose evenness. The
Roth argument's odd rays r=e+6n are therefore legitimate consequences
of the same operator. This is not an extrapolation from the originally
named integer-h sequence.

The order of multiplication in (2) matters: x^(18-6k) is applied after
the polynomial in theta. Both the code and the coefficient extraction
use that order.

## 4. The Item309 second branch is a valid use of the same identity

Put y=z-1 and let alpha^3=4, choosing the positive real alpha for the
following characteristic-zero description. Define

    X=z(1-z)/(1+z^2)^(2/3).

Then

    T(z-1)=1+z^2,
    x=-alpha X,
    D(z-1)=2z^3+z^2+6z-3.

The independent polynomial check also reproduces

    N(z-1)=54-144z+258z^2-240z^3+354z^4-48z^5
            +150z^6+48z^7.

Furthermore

    X'(z)=-D(z-1)/[3(1+z^2)^(5/3)],

so X'(0)=1 and X has a unique formal inverse z(X). Define

    A(X)=N(z(X)-1)/D(z(X)-1)^3=sum a_r X^r,
    C_-(x)=A(-x/alpha).

All local denominators are nonzero: D(-1)=-3 and T(-1)=1. In particular
the cleared differential denominator D^35 T^12 is a unit on this local
branch. The identity from Section2 therefore applies at y=-1 just as at
y=0. Merely satisfying the resultant curve would not by itself prove
this operator extension; the decisive fact is that the operator's
rational numerator is identically zero in y, with valid local
denominators. Item309 uses that correct stronger fact.

For r=e+6n odd,

    [x^r]C_-(x)=(-alpha)^(-r)a_r
               =-alpha^(-e)16^(-n)a_r.

The constant -alpha^(-e) is independent of n and nonzero. Cancelling it
in characteristic zero in (3) proves the same rational recurrence for
16^(-n)a_(e+6n). Since that sequence is rational, reduction modulo p
does not require alpha to exist in F_p or require p to split in its
number field. No such assumption is present or needed in the Roth proof.

The actual fixed-prime phase obeys

    2^(2s)=4^(s0)16^(-n),  s=s0-2n.

Therefore the two summands of u_(p,n) are indeed solutions of one fixed
order-three recurrence with a prime-dependent constant linear
combination. The phase is not a moving coefficient in that recurrence.

## 5. The limiting cubic and nondegenerate powers

Expanding the exact factor lists gives the leading coefficients

    P_0: -64/531441,
    P_1: -9856/19683,
    P_2: -413233/729,
    P_3: 1.

They were independently checked from the factor scalars, the leading
core coefficients, and every linear-factor slope. Thus the limiting
companion characteristic polynomial is exactly the root's polynomial

    f(X)=531441X^3-301246857X^2-266112X-64.

Its mod7 values at0,...,6 are6,5,6,1,3,4,3, and its leading coefficient
is1 modulo7. This proves irreducibility overQ. The exact discriminant is

    -572058527163885303300000000.

It is negative and nonzero, so the irreducible cubic has Galois groupS3.
The independent integer-square tests confirm that neither minus the
discriminant nor minus one third of it is a square. An integer that is
a rational square must be an integer square, so these tests also establish
the required rational nonsquare statements.

The splitting field has a unique quadratic subfield, and it is neither
Q(i) nor Q(sqrt(-3)). Every cyclotomic subfield is a Galois abelian
subextension of an S3 extension, hence lies in that unique quadratic
subfield. It follows that the splitting field contains only the roots
of unity ±1.

Every ratio of two roots lies in the splitting field. A root-of-unity
ratio can therefore only be ±1. Distinctness excludes+1. For-1, writing
the monic cubic as X^3-A X^2-B X-C with A,B,C positive and factoring
roots lambda,-lambda,A gives lambda^2=B and A lambda^2=-C, a
contradiction. Consequently the powers lambda_i^d are pairwise distinct
for every positive integer d. This verifies the all-spacing assertion,
not just a bounded check of d.

## 6. Observation determinants for all fixed spacings

The companion convention in the proposed proof is consistent with the
state S_n=(u_n,u_(n+1),u_(n+2))^t. For the limiting companion matrix C,
the vectors

    v_j=(1,lambda_j,lambda_j^2)^t

are eigenvectors. For fixed d, the transfer products T_d(h),T_(2d)(h)
tend to C^d,C^(2d) as real h tends to infinity because there are finitely
many factors and every P_j has the same degree with nonzero P_3 leading
coefficient. This is an ordinary rational-function limit.

Let V have columns v_j. Multiplying the limiting observation matrix by V
gives rows (lambda_j^(id)) for i=0,1,2. Its determinant is a Vandermonde
in the three distinct lambda_j^d. Division by det V therefore gives a
nonzero limiting observation determinant. The rational function F_d(h)
cannot be identically zero for any d>=1.

No finite-field approximation to the real limit is assumed. The limit
only proves a characteristic-zero rational-function nonidentity. Its
subsequent use modulo p requires denominator clearing and exclusion of
primes where the numerator polynomial vanishes identically; the proposed
proof explicitly does this rather than skipping the issue.

Clearing with integer M=P_3 T gives the stated J_d and denominator
D_d D_(2d). The degree bound48d is correct. The unshifted row e_1 makes
the numerator determinant a difference of two products, consistent with
the coefficient-norm estimate. These checks agree with the scope of the
separate height review.

## 7. State and boundary bookkeeping

When three observations vanish and both the transfer denominator and
observation numerator are nonzero, invertibility forces S_n=0. The
preceding desingularization theorem bounds such zero-state starts by5.
It is necessary to use that theorem: a nonzero rational-function
observation determinant alone would not exclude an identically zero
state modulo a particular prime.

The root's correction of two boundary starts is sufficient. Computing
the full state T_(2d)S_n can require values through index n+2d+2. Among
starts whose last observed zero n+2d is actual, at most two lack those
last two additional actual values. Removing them makes every intermediate
recurrence and p-integrality claim legitimate. The safe bound80d+7
therefore covers these endpoint cases.

The finite exceptional prime sets from coefficient denominators, the
initial branch minors, the quintic leading coefficient, and integer
clearing may all be combined. They are independent of the original
construction index. None of this review treats the growing initial
factor4^(s0) as a bounded-height integer; only its residue and the
uniform independence of the two branch columns are used.

## 8. What the accepted result does and does not establish

The recurrence is now independently verified at the semantic level
needed by the proposed Roth argument. The all-spacing determinant
nonvanishing is valid. Together with the reviewed progression counting
and its fixed or slowly growing spacing cutoff, these inputs establish
zero density for this actual fixed-prime determinant support.

Actual Item334 collisions form a subset of that support on every chart,
so the result concerns an averaged upper bound for that component. It
does not supply pointwise W(M)=o(M), does not control a potentially useful
sparse high-gain subsequence, and does not improve the positive booked
content/matching rate. The main irrationality problem remains separate.

The Item314 actual-phase determinant bridge and its all-row p-unit
normalization were used as the expressly identified upstream bridge
(also used in the preceding independently reviewed bounded-run theorem).
This bounded review rechecked the Item237/309 recurrence dependency in
depth; it did not rerun the entire older Item250–314 period-minor chain.
