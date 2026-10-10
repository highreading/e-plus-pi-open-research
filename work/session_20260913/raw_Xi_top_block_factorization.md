> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact factorization of the remaining Xi top-block tie

Continuation status: the full contribution is now handled by
raw_Xi_eight_row_set_reduction.md and
raw_Xi_remaining_class_mod_eight.md, with independent review. The
top-block factorization here remains valid and its Legendre identities
are used in the full proof.

Date: 2026-09-13. Original continuation by audit_sources.

The full Xi determinant remains open at n=1 modulo4, n>=5. This
note factors the contribution formed from the unique factorial-maximal
exponential row set in each of its four coefficient minors. It does
not estimate the remaining row-set products, and therefore is not a
nonvanishing proof for the full Xi_n.

## 1. Common scale and the pure arctangent polynomial

Keep the common exponential block with n+1 rows `{2n,...,3n}` in
each of the coefficient determinants for a_n, h=a_(n-1)-c_n, c_n,
and c_(n-1). Their remaining C rows are built from
`{n+1,...,2n-1}` and the endpoint row C(1)=0. The top contributions
to the C coefficients therefore form, at a common nonzero scale
kappa, the cofactor vector of this fixed C matrix.

In reversed coordinates its polynomial is

    C_top^rev(t)=kappa [Q_n(t)-lambda Q_(n-1)(t)],
    lambda=Q_n(1)/Q_(n-1)(1).                        (1)

Indeed the n-1 ordinary C rows impose orthogonality to degrees zero
through n-2 for the raw moment functional
`L(P)=1/2 integral_(-1)^1 P(iu) du`. Its orthogonal complement in
degree at most n is span(Q_n,Q_(n-1)); the endpoint row then gives
(1). All q_j=Q_j(1) are positive, so the ratio is defined. The top
C_n cofactor is nonzero for odd n, which also proves kappa!=0 in
the case considered below.

The coefficient top contributions a_top and h_top are obtained by
appending the coefficient row at k=n, or its exact modified row at
k=n-1, to this same C matrix. Thus they have precisely the same
scale kappa. They are the pure arctangent reconstruction of (1),
with the exponential part absent from those appended C rows. This
follows either by cofactor linearity or by expanding those appended
rows against the common C cofactor vector. No independent
normalization of these four top terms is permitted.

## 2. Three exact Legendre identities

For a polynomial Q_m define its polynomial second kind by

    S_m(t)=L_s[(Q_m(t)-Q_m(s))/(t-s)],
    h_m=L(Q_m^2).

For n odd the needed identities are

    Q_n'(0)=n^2 Q_(n-1)(0)/(2n-1),                  (2)
    Q_(n-1)(0) S_n(0)=h_(n-1),                     (3)
    Q_(n-1)(0)[Q_(n-1)(0)+S_(n-1)'(0)]
                         =(2n-1)h_(n-1).            (4)

Equation (2) follows from the ordinary Legendre derivative at zero
and the exact monic scaling
`Q_m(t)=2^m i^m P_m(-it)/binom(2m,m)`.

For (3), the monic three-term recurrence and the second-kind
definition give

    Q_n S_(n-1)-Q_(n-1) S_n=-h_(n-1).

Its normalization follows at n=1 from Q_0=1, Q_1=t, S_0=0,
S_1=1, h_0=1; the recurrence multiplies the identity by
`-beta_(n-1)=h_(n-1)/h_(n-2)` in each next step. Evaluating at
zero and using odd parity of Q_n proves (3).

For (4), put `g(t)=L_s(1/(t-s))=arctan(1/t)` for real t>0, and
`R_m(t)=Q_m(t)g(t)-S_m(t)`. Both Q_m and R_m solve

    (1+t^2)y''+2t y'-m(m+1)y=0.                     (5)

For a direct check of the second solution, g'=-1/(1+t^2), and the
polynomial identity

    [(1+t^2)D^2+2tD-m(m+1)] S_m=-2Q_m'

follows by applying the operator to its finite divided-difference
sum. Equivalently compare coefficients using the Q_m equation and
the exact moment recurrence
`(j+3)mu_(j+2)+(j+1)mu_j=0` for j>=0. The same operator applied
to Q_m g is -2Q_m', proving (5) for R_m.

The Wronskian equation then gives

    Q_m R_m'-Q_m' R_m=-(2m+1)h_m/(1+t^2).

Its constant is determined at infinity: `R_m(t)=h_m t^(-m-1)
+O(t^(-m-2))` by orthogonality. At even m, Q_m'(0)=0 and S_m is
odd. Using the analytic branch `g(t)=pi/2-arctan(t)` near zero
therefore proves (4). The branch's constant drops out of its
derivative and Wronskian.

## 3. Factorization and its exact dyadic cancellation depth

Now let n be odd. Parity of Q_n,Q_(n-1) and of their second-kind
polynomials gives, from (1),

    c_top=-kappa lambda Q_(n-1)(0),
    c_prev_top=kappa Q_n'(0),
    a_top=-kappa S_n(0),
    h_top=kappa lambda [S_(n-1)'(0)+Q_(n-1)(0)].      (6)

Consequently (2)–(4) factor the top-block quadratic expression:

    Xi_top=a_top c_prev_top-h_top c_top
      =kappa^2 h_(n-1)/(2n-1)
                        [(2n-1)^2 lambda^2-n^2].     (7)

The first product alone is

    a_top c_prev_top=-kappa^2 n^2 h_(n-1)/(2n-1),

so their relative cancellation factor is exactly

    Xi_top/(a_top c_prev_top)
                    =1-[(2n-1)lambda/n]^2.          (8)

For n=1 modulo4, n>=5, put a=v_2(n-1)>=2. The already proved
q-value parity estimates give

    lambda=1+beta_(n-1)q_(n-2)/q_(n-1),
    v_2(lambda-1)>=2a+1.

Thus

    v_2((2n-1)lambda-n)=a,
    v_2((2n-1)lambda+n)=1.                           (9)

In the first expression n-1 is uniquely least; in the second the
unperturbed value 3n-1 is 2 modulo4. Since n is odd, (8)–(9) prove

    v_2(Xi_top)=v_2(a_top c_prev_top)+a+1.            (10)

At n=1 this particular top-block factor is exactly zero, because
lambda=1. The actual Xi_1=-29 comes from other contributions, so
that endpoint case is not inserted into (10).

## 4. The precise missing control

The actual Xi is a quadratic expression in full bordered-minor sums.
Equation (10) controls only the product combination in which every
coefficient uses the top exponential row set. Other single-set and
mixed-set products may occur at or below the deeper level in (10).
Their bounds must be proved before this factorization can establish
nonvanishing of the full Xi.

The all-index leading-B theorem normalized an n-column exponential
block and controlled its row replacements modulo 2^(a+1). Here
the common block has n+1 columns and the required quadratic residue
level is a+1 above the product baseline. The former lemma does not
automatically furnish this different precision or the mixed-product
cancellations. The next concrete problem is a uniform row-replacement
or Pluecker-identity estimate for this actual n+1-column quadratic
combination, retaining the -4 endpoint assignment as well.
