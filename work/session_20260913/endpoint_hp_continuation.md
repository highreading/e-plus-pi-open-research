> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Endpoint-matched independent-coefficient Hermite–Padé continuation

Date: 2026-09-13. Bounded mathematical investigation; no bulk degree scan.

## Outcome

I obtained an all-index multiplicity bound and an exact reduction to a
cubic forcing polynomial for the actual Möbius-arctangent family. These
are new deductions in this session, not extrapolations of normality through
a finite degree range. They do not prove full normality, primitive endpoint
decay, or a statement about the arithmetic nature of e+pi.

The main proved statements are:

1. For every nonzero triple of polynomials of degrees at most n,
   
       ord_0(A+B exp(z)+C F(z)) <= 3n+4.

2. Consequently the endpoint-matched order-(3n+1) solution space has
   dimension at most four for every n. This replaces the possibility of
   unbounded rank deficiency with an explicit constant bound; it does not
   establish the expected dimension one.

3. For every nonzero member of that space, an explicitly defined
   polynomial determinant numerator is exactly
   
       N_n(z)=z^(3n-1) Q_n(z),  deg Q_n<=3.

4. Variation of parameters gives an evaluated integral involving Q_n,
   with the endpoint coefficient and its gcd retained explicitly. The
   tempting nonsingular positive-kernel interpretation fails already at
   the archived n=2 row: its two-function Wronskian has a zero inside
   (0,1). Thus the integral requires a path avoiding these zeros or
   correctly matched continuation across them. It cannot be used as an
   ordinary positive real integral for all n.

No new arithmetic lower rate or favorable subsequence was obtained.

## 1. What the archive already established

The underlying family is

    F(z)=4 arctan(z/(2-z)),  D(z)=z^2-2z+2,
    F'(z)=4/D(z),  F(1)=pi,
    R_n=A_n+B_n exp(z)+C_n F(z),
    deg A_n,deg B_n,deg C_n<=n,
    ord_0 R_n>=3n+1,  B_n(1)=C_n(1).

I reviewed Items179,182,184, `pi_g_function_pullback_route.md`,
`endpoint_matched_mobius_hp_rank_and_content.md`, and the relevant
Chebyshev, Machin-rank, and arithmetic-height obstruction notes.

The archive already proves integral derivative jets, an analytic radius
sqrt(2), exact tail identities, and substantial forced cofactor content.
It proves exact normality and endpoint incompatibility for the independent
maximal family only through n=256, and nonshrinking primitive endpoint
values for the matched family through n=45. The all-degree compatibility
determinant identity is proved; its all-degree nonvanishing is not.

The current best generic content-aware estimate, conditional on full row
rank, is

    log H(A,B,C) <= (3/2)n^2 log n+O(n^2).

Raw determinant height and the forced common-cofactor divisor contribute
respectively (7/2)n^2 log n and 2n^2 log n at the displayed leading scale.
The low-coefficient reconstruction and final full-polynomial content must
still be accounted for. These are distinct from the endpoint-pair gcd.

Item184 gives, with q=2n+1 and H_BC=max coefficients of B,C,

    |R_n(1)| <= H_BC * Psi_n,
    Psi_n=(q+1)^2/(q^2 q!)+(16+12sqrt(2))/(q 2^n).

For an integral triple put X=A(1), Y=B(1)=C(1), and
d=gcd(|X|,|Y|). Its primitive endpoint value is R_n(1)/d. Therefore the
actual bound is (H_BC/d)Psi_n. No normalization changes H_BC/d or
H_BC/max(|X|,|Y|). This obstruction is retained throughout the new work.

The known Machin bordered-rank theorem applies to a different logarithmic
kernel and is not an all-degree Möbius rank theorem. The archived whole-
space Chebyshev shortcut fails for the constrained Machin system. In the
Möbius system, actual rows n=6 and8 already show that the first free Taylor
coefficient and the endpoint value can have opposite signs. I did not
repeat those failed first-term or uniform positivity arguments.

## 2. The new all-degree Wronskian lemma

Use W(f,g,h) for the determinant with columns f,g,h and derivative rows
0,1,2. Set

    U=B exp(z),  V=C,
    B1=B'+B,  B2=B''+2B'+B,
    K=B C'-(B'+B)C.

Then W(U,V)=exp(z)K. Define

    N=D^2 exp(-z) W(R,U,V).                              (1)

Although R contains a logarithm and an exponential, N is a polynomial.
Here is its explicit rational-arithmetic-free formula:

    N = D^2 det[[A, B, C],
                 [A', B1, C'],
                 [A'',B2, C'']]
        +4D[-C(B C''-B2 C)+2C'K]-4D' C K.              (2)

To prove (2), subtract the B exp(z) column and F times the C column from
the first Wronskian column. That column becomes

    (A, A'+C F', A''+2C'F'+C F'')^t.

Factor exp(z) from the second column and use F'=4/D and
F''=-4D'/D^2. Expanding the first column gives exactly (2).

### Degree bound

For n>=1,

    deg N <= 3n+2.                                      (3)

Indeed the polynomial determinant in (2) has degree at most 3n-2.
One way to see the only potentially troublesome cancellation is to write
it as the ordinary polynomial Wronskian W(A,B,C), plus

    B(A C''-A''C)-(2B'+B)(A C'-A'C).

The ordinary Wronskian has degree at most 3n-3. Also
deg(A C'-A'C)<=2n-2 because the top equal-degree terms cancel; its
derivative A C''-A''C has degree at most 2n-3. Thus the additional terms
have degree at most 3n-2. Multiplication by D^2 adds four.

In the remaining terms of (2), deg K<=2n, deg B2<=n, and each term has
degree at most 3n+2 directly. For n=0 the polynomial determinant is zero
and (3) still holds by direct inspection of (2).

### N is nonzero when B and C are nonzero

This point cannot be inferred just from a nonzero input triple. Here it
has a short independent proof.

The three analytic functions R, B exp(z), C are linearly independent over
the constants when B,C are nonzero. Suppose a constant relation holds.
Analytic continuation once around the logarithmic singularity 1+i changes
F by a nonzero constant, while all other terms are single-valued. The
coefficient of R must consequently be zero. The remaining relation
between B exp(z) and C is impossible because exp(z) is not a rational
function. For example, their alleged polynomial-ratio equality is
incompatible with growth on the positive real axis after continuation.

For analytic functions, a zero Wronskian identically is equivalent to
constant linear dependence. In this case it can also be checked without
invoking that general statement: on a small domain where C and
(B exp(z)/C)' are nonzero, W(R,B exp(z),C)=0 implies

    ((R/C)' / (B exp(z)/C)')'=0,

up to a nonzero factor. Two integrations give the same prohibited
constant relation. Thus N is a nonzero polynomial.

### Multiplicity bound

If ord_0 R=M>=2, then each term in W(R,U,V) has order at least M-2.
Because D(0)=2 and exp(0)=1,

    M-2 <= ord_0 N <= deg N <=3n+2.

This proves M<=3n+4 when B,C are nonzero.

The omitted cases have a stronger elementary bound. If C=0, the
two-function Wronskian W(R,B exp(z)) is exp(z) times the polynomial
A(B'+B)-A'B, of degree at most2n, unless R itself is a polynomial multiple
of exp(z), which is immediate. If B=0, then

    D W(R,C)=D(A C'-A'C)-4C^2

is a nonzero polynomial of degree at most2n. The same multiplicity
argument gives M<=2n+1. Polynomial-only cases are immediate. Hence

    ord_0 R<=3n+4                                       (4)

for every nonzero triple. No rank or asymptotic hypothesis is used.

### Uniform bound on rank deficiency

For the endpoint-matched space of order at least3n+1, the four Taylor
coefficients of indices3n+1,...,3n+4 determine the remainder injectively.
If all four were zero, (4) would force the triple to be zero. Therefore
that space has dimension at most4 for every n. Equivalently the high
endpoint matrix has rank at least2n-2. The independent family with order
at least3n+2 has dimension at most3.

This is weaker than full normality, but it is an all-index theorem. A
constant multiplicity allowance cannot simply be deleted: at degree0,
the function 2-2exp(z)+F(z) has order exactly4. This also explains the
known endpoint-degenerate n=1 triple after multiplication by1-z.

## 3. A cubic forcing polynomial for every actual high-order form

For n>=1, every nonzero endpoint-matched form of order>=3n+1 has B,C
nonzero, by the stronger two-function bounds just proved. Thus N is
nonzero. Its origin multiplicity is at least3n-1, while (3) bounds its
degree by3n+2. Consequently

    N_n(z)=z^(3n-1) Q_n(z),
    Q_n in Q[z], 0<=deg Q_n<=3.                         (5)

For an integral triple, (2) shows that Q_n has integer coefficients.
This is an exact new fixed-degree reduction, not a fitted recurrence.

The bounded checker `check_endpoint_hp_wronskian.py` verifies formula(2)
against a separate direct rational-function determinant on the archived
rows n=2,3,6,8, and verifies the factorization(5). Those four checks support
the formula's implementation only; the preceding argument proves (5)
for every n.

## 4. Evaluated variation of parameters and its obstruction

Expanding W(R,U,V) in the first column gives

    W(R,U,V)=W(U,V)R''-W(U,V)'R'
             +(U'V''-U''V')R.

On a path from0 toz where K has no zero, and when K(0)!=0, variation of
parameters with R(0)=R'(0)=0 gives

    R(z)=integral_0^z
      [C(z)B(t)-B(z)exp(z-t)C(t)]
      *N(t)/[D(t)^2 K(t)^2] dt.                         (6)

This follows from the usual two-solution Green formula with
U=B exp(z), V=C and W(U,V)=exp(z)K. It can alternatively be verified by
differentiating (6) twice and checking the initial conditions.

If K has no zero on[0,1] and Y=B(1)=C(1)!=0, then (6) specializes to

    R(1)/Y=integral_0^1
       [B(t)-exp(1-t)C(t)] t^(3n-1)Q_n(t)
       /[D(t)^2 K(t)^2] dt.                            (7)

However, the no-zero condition on K fails in the actual family already
at n=2. The archived primitive triple is

    A=1392+2454z-911z^2,
    B=-1392+1020z-130z^2,
    C=-1041+879z-340z^2.

Its K equals twice

    -805410+1480644z-868860z^2+230535z^3-22100z^4.

In particular K(0)=-1610820 and K(1)=29618, so a zero in(0,1) is forced
by the intermediate value theorem. Exact Sturm counts give one such zero.
The same bounded checks find one K zero in each of n=3,6,8 as well, but
no all-n root-count conclusion is drawn. The cubic forcing has respectively
0,1,2,2 roots in(0,1) in these four rows.

Thus (7) is not a globally valid ordinary real integral for all the actual
rows. It may be used on pieces with correctly matched initial data, or on
a complex path avoiding zeros of K and D. Analytic continuation of the
complete expression recovers R, but splitting the individual singular
integrals and treating them as positive would be invalid. This is a
specific obstruction to the newly attempted positive Green-kernel proof,
not merely the older whole-space Chebyshev objection.

## 5. Height, endpoint, and gcd accounting together

Under common scaling (A,B,C)->c(A,B,C), one has

    K->c^2 K, N->c^3 N, Q_n->c^3 Q_n.

Therefore the integral in (7), wherever valid or correctly continued, is
projectively invariant. The exact primitive endpoint form is

    L_n=R_n(1)/d=(Y/d)*(R_n(1)/Y).                       (8)

The endpoint integer Y/d, not the raw polynomial normalization, multiplies
the integral. Neither the cubic degree nor the normality-defect bound
controls that integer.

For example a straightforward coefficient norm estimate from (2), with
H=max coefficient magnitude in the full triple, gives

    H(Q_n)<=400(n+1)^6 H^3,
    ||K||_1<=2(n+1)^3 H^2.

These upper bounds show that fixed forcing degree does not mean fixed
forcing height. Combined with the archive's conditional primitive-height
upper bound, the first gives at best

    log H(Q_n)<=(9/2)n^2 log n+O(n^2),

without the additional endpoint-gcd input. There is also no lower bound
here for |K| on an integration path. Consequently this deduction does not
improve the effective-height estimate (H_BC/d)Psi_n and cannot turn the
observed finite normality into shrinking integer forms.

If Y=0, expression(8) using a ratio is unavailable. Such a row must be
handled directly as its integer endpoint A(1)/d, or as the degenerate pair
(0,0). No all-index theorem excluding that case is claimed.

## 6. Literature hypotheses checked

Fidalgo Prieto and López Lagomasino prove perfectness for Nikishin systems
and an AT property on intervals outside the first support. Their
definitions use constant-sign measures on real intervals and the specific
iterated Cauchy-transform construction. These hypotheses do not follow
from F'(x)>0 or from integral derivative jets. Our logarithmic singularities
are at1±i, and exp(z) supplies no identified measure in that Nikishin
construction. Thus their theorem is not directly applicable to this pair.
[Primary paper, definitions1.2–1.3 and theorems1.1–1.2](https://arxiv.org/pdf/1001.0554).

The July2026 Yu repository manuscript reports a computer-assisted normality
theorem for a mixed exponential–arctangent system. Its abstract explicitly
distinguishes this setting from immediate positivity arguments. This
continuation did not independently replay its large external certificate,
and the archive already distinguishes its ordinary normality claim from
the endpoint-matching and primitive-value obligations needed here.
[University of Alabama manuscript record](https://ir.ua.edu/items/[session identifier removed]).

No external normality theorem was needed for the new Wronskian lemma.

## 7. The narrower remaining mathematical problem

The new four-coefficient forcing reduction makes the next analytic step
more concrete: determine the actual projective cubic Q_n together with
the zeros and connection behavior of K_n=B_n C_n'-(B_n'+B_n)C_n, sufficiently
uniformly to evaluate the continued integral(6) at1. One useful intermediate
target is an all-index description of the real K_n zeros and the transfer
across them, followed by an asymptotic of R_n(1)/Y_n. The bounded checks
suggest one real K zero in the four selected rows, but this is expressly
an unproved target, not a theorem or a proposed zero-free assertion.

Even success at that analytic target must be combined with the independent
primitive-endpoint integer |Y_n|/d_n. A candidate remainder asymptotic must
be tested against that exact height; an exponential bound for a normalized
analytic remainder alone is inadequate when the primitive integer height
can live on an n^2 log n scale.

The diagonal ray remains a low-priority route to positive progress on
irrationality because its certified primitive values grow dramatically.
The all-degree multiplicity and cubic-forcing lemmas are useful structural
information for studying it or a changed degree allocation. They do not
justify another broad diagonal scan, nor do they establish an all-large
nondecay theorem.

Artifacts: `endpoint_hp_continuation.md`,
`check_endpoint_hp_wronskian.py`, and `endpoint_hp_wronskian_checks.json`.
