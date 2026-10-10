> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# First-Witt gate: a new order-three period system and exterior reduction

Status: exact symbolic auxiliary identities derived in this continuation
and independently reviewed, including the corrected Frobenius ambiguity.
The actual nonzero-state issue was subsequently settled in
`witt_actual_exterior_rank.md`, yielding the reviewed support theorem in
`witt_roth_density.md`. The unbounded multiplicity problem remains open.

## Archive context and scope

This attempt reads the complete work-only Items426 and427, and the relevant
canonical Item194 and Item197 arguments. It continues Item426's actual
four-endpoint period construction, not a fitted recurrence. Item427's
valuation identity does not make this recurrence a density theorem.

Use u=x(1-x), Q=(1+x)(1+x^2), and actual rank-zero rows

    p=2r+6s+3,   P_nu(x)=u^r Q^(2s-nu),   nu=0,1.

The zero-constant primitive T_nu is a polynomial over F_p, because
deg P_nu=p-3-3nu. For fixed p and j, increasing s by2 decreases r by6.
Item426 constructs H_nu from the four values T_nu(zeta), zeta^4=1,
and fixed linear maps R_j,L_j, with the exact first-Witt gate

    kappa=L_j(H_1)R_j(H_0)-L_j(H_0)R_j(H_1).

This is a larger and different event from the ordinary common-log
collision support studied in the session's first Roth applications.

## 1. An order-three telescoper, improving Item426's order four

Put e=2s-nu. Modulo p, e+1=-2r/3-nu. Seek

    sum_(k=0)^3 c_k Q^(4k) u^(6(3-k))
      =uQ A' + {(-2r/3-nu)uQ' +(r-17)Qu'}A.       (1)

Allow deg A<=34+3nu. The coefficient of degree deg A+4 on the right
is (34+3nu-deg A) times the leading coefficient of A, so the highest
row vanishes. There are 39+3nu unknowns and at most 38+3nu equations.
This proves existence of a nonzero solution over Q(r), and over each
actual F_p after substitution.

The extra two (nu=0) or five (nu=1) primitive coefficients compared with
the naive degree bound are essential. With the smaller degree32, the
symbolic system has trivial kernel; this failed subattempt was checked
before the correct degree allowance was derived.

The recurrence coefficients cannot all vanish on an actual row with
r>=18. Otherwise (1) gives

    (A u^(r-17) Q^(e+1))'=0.

The polynomial in parentheses has degree at most p, and vanishes at
both0 and1. In characteristic p, a polynomial of degree at most p
with zero derivative is ax^p+b. The two endpoint zeros imply a=b=0,
and therefore A=0. This contradicts a nonzero solution. This replaces
Item426's stronger-than-necessary requirement that the degree be <p.

Multiplying (1) by P_nu/u^18 gives an exact derivative whose primitive
is A u^(r-17)Q^(e+1). It vanishes at0,1,-1,i,-i. **A characteristic-p
integration ambiguity must be retained:** if b is this primitive's
x^p coefficient, the actual degree-below-p primitives obey

    sum_(k=0)^3 c_k(r) T_nu(r-6k;zeta)=-b zeta^p. (2)

on every actual range in which these four rows exist, subject to the
explicit denominator exceptions of the chosen symbolic coefficients.
The rank argument itself remains valid even at an exceptional row; a
single chosen rational operator need not specialize regularly there.
The homogeneous recurrence is valid after projection to R_j,L_j,E_j,
by the exact kernel argument in Section2a below. The first draft omitted
this raw-period forcing term; independent review identified the omission.

`derive_witt_period_operator.py` solves (1) over Q(r) and verifies the
result by expanding every coefficient in Q[r,x] after denominator
clearing. The complete coefficients, including those of A, are saved in
`witt_period_operator_symbolic.json`. The two coefficient lists have
common degree17 (nu=0) and20 (nu=1). This is an exact polynomial
certificate, not interpolation or a finite recurrence fit.

Both limiting characteristic polynomials, up to nonzero rational
factors, are

    f_W(t)=531441t^3-19279798848t^2-1089994752t-16777216. (3)

If f(t)=531441t^3-301246857t^2-266112t-64 is the cubic from the
already reviewed Roth argument, then f_W(t)=64^3 f(t/64).
Thus the same non-root-of-unity eigenvalue-ratio proof applies.

Independently, the critical polynomial of the rational phase u^6/Q^4
is S=3Qu'-2uQ'=-5x^3-5x^2-5x+3, and

    resultant_x(S,t u^6-Q^4)=4096 f_W(t).

This exact agreement explains the limiting cubic; it is not used to
replace the verified telescoping identity.

## 2. A contiguity identity between nu=0 and nu=1

The two period triples need not be treated as independent systems. There
are rational functions a_0,a_1,a_2 and a polynomial A of degree at most25
such that

    u^12 = sum_(k=0)^2 a_k u^(12-6k)Q^(4k+1)
      +uQ A'+{(r-11)Qu'+(-2r/3-1)uQ'}A.          (4)

All coefficients are given in `witt_period_contiguity_symbolic.json`;
`derive_witt_contiguity.py` verifies the entire identity over Q(r)[x].
On actual rows, multiply (4) by u^(r-12)Q^(2s-1). The derivative
primitive is A u^(r-11)Q^(2s). Its degree is at most p and its
endpoint values at0,1,-1,i,-i vanish when r>=12. If b is its x^p
coefficient, the actual raw period identity is therefore

    T_1(r;zeta)=sum_(k=0)^2 a_k(r)T_0(r-6k;zeta)-b zeta^p. (5)

This holds outside the explicitly recorded rational denominator roots
and fixed coefficient primes. It applies to the same four endpoint
values. The additional term disappears under the same linear maps
R_j,L_j,E_j by Section2a. No new endpoints or external periods are
introduced.

The coefficients have

    a_0 -> 5/8,
    r a_1 -> -165139233219/3610112000,
    r a_2 -> 291328083/231047168000.               (6)

In particular, the leading proportional part cancels in kappa. This is
consistent with, and separate from, the archive's saddle cancellation.

### 2a. Why the Frobenius ambiguity disappears after projection

Let a=3j+1,c=2j+1 and F_j=u^a/Q^c. Item426 has
D_j=a u'Q-cQ'u. Its values are -4a at1 and4c at each of -1,i,-i;
thus D_j(zeta)=D_j(zeta^p) on the fourth roots.
For the endpoint vector T(zeta)=zeta^p, the interpolated polynomial H
is the unique degree-at-most-four, zero-constant polynomial with
H(zeta^p)=D_j(zeta)zeta^p. The exact identity uQ=x-x^5 shows that

    H_F=xD_j+uQ=(3j+2)x-(5j+2)(x^2+x^3+x^4).

Its second-Cartier differential is

    u^(3j)H_F/Q^(2j+2) dx = d(xF_j).

Both endpoint values of xF_j are zero, and an exact rational differential
has zero residues. Hence R_j(H_F)=L_j(H_F)=E_j(H_F)=0. This proves the
projected homogeneous recurrence and projected contiguity used below,
without declaring the raw T identities homogeneous. The correction has
been independently checked.

## 3. The gate lies in a three-dimensional exterior-square system

Let f(r)=L_j(H_0(r)), g(r)=R_j(H_0(r)), and put

    S_f=(f(r),f(r-6),f(r-12))^T,
    S_g=(g(r),g(r-6),g(r-12))^T.

They obey the same nu=0 companion transfer T(r). Write
w_01=f_0g_1-f_1g_0, w_02=f_0g_2-f_2g_0,
w_12=f_1g_2-f_2g_1. The vector w obeys the exact transfer
w(r-6)=(exterior^2 T(r))w(r). Equation(5) gives

    kappa(r)=-a_1(r)w_01(r)-a_2(r)w_02(r).       (7)

Thus the determinant problem has dimension three, rather than requiring
an unrestricted product of two order-three systems.

The limiting companion and exterior matrix, in the displayed ordering,
are

    C = [[0,1,0],[0,0,1],
         [16777216/531441,40370176/19683,26446912/729]],

    W = [[0,0,1],
         [-16777216/531441,0,26446912/729],
         [0,-16777216/531441,-40370176/19683]].

For r*kappa, the limiting observation row is

    v=(165139233219/3610112000,-291328083/231047168000,0).

The exact calculation gives

    det(v,vW,vW^2)=243/705100000 !=0.             (8)

The eigenvalues of W are the pairwise products of the three eigenvalues
of C. Their pairwise ratios are ratios of the original eigenvalues, so
they are nonzero and have no root-of-unity quotient. The Vandermonde
argument with the cyclic row (8) therefore makes every fixed-spacing
observation determinant symbolically nonzero. The source of (8) and
the characteristic-polynomial scale check is the exact rational program
`check_witt_exterior_limit.py`, with `witt_exterior_limit_checks.json`.

The functions in these observations are rational functions of r.
Multiplying by their common denominators gives bounded-degree integer
polynomials for each fixed spacing. This addresses the nonidentity part
of a Roth transfer, but not every hypothesis of that transfer.

## 4. Initial obstruction and its subsequent resolution

The following records the precise obstacle at the end of the initial
derivation. It has since been resolved by the actual26-by26 rank
certificate in `witt_actual_exterior_rank.md`: the exterior state is
nonzero except at six sextic roots, with terminal rows counted separately.
This bypasses the need for a separate seed-propagation proof. The
desingularization was also completed in `witt_period_desingularization.json`,
but is not needed for the final density proof. The final support result
and independent review are `witt_roth_density.md` and
`witt_independent_review.md`.

To conclude that the actual kappa-zero rows have density zero at each
fixed prime, it is still necessary to establish that the actual exterior
state w is nonzero modulo p on all but o(p) starts. This cannot be
inferred from the nondegenerate limiting cubic. Both of the following
issues must be settled:

1. The actual endpoint solutions f,g must not become proportional
   throughout a positive-length portion of the fixed-p interval. Their
   initial values depend on p; no fixed rational nonzero seed minor has
   yet been established.
2. Apparent singularities of the chosen companion may allow a state
   loss unless a p-integral propagation or desingularization argument
   excludes it. The nu=0 outer polynomial factors have a shifted sextic
   pattern, suggesting an exact extension of the earlier quintic
   desingularization. It has not yet been completed here.

If these hypotheses are proved, the existing progression argument would
give an averaged first-Witt support estimate. It would still not bound
the full unbounded valuation tower: support rarity is not uniform
integrability of the depths. The present note does not book a positive
gain or change the main irrationality threshold.
