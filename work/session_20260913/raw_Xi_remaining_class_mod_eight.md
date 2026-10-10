> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The remaining infinity cross-minor: a uniform residue modulo eight

Date: 2026-09-13. Original continuation by audit_sources. Dedicated
independent review passed with no correction; see
raw_Xi_remaining_class_independent_review.md.

For the actual raw canonical normalization B_n(1)=1, C_n(1)=4,
assume n>=5, n=1 modulo4, and put a=v_2(n-1)>=2. The theorem is

    v_2(Xi_n)=-2n-2phi(n-1)+2,
    Xi_n=a_n c_(n-1)-(a_(n-1)-c_n)c_n,              (1)

where phi(j)=v_2(j!). The other residue classes were proved in the
prior notes. This is a cubic-degree result, not an Archimedean
estimate or a result about the irrationality of e+pi.

## 1. A common effective cofactor vector and the actual error bound

Use the n+1-column interpolation matrix M and eight row sets in
raw_Xi_eight_row_set_reduction.md, independently checked by root.
Keep the exact entries M_(d,i) for d=1,2 and i=0,1,2,3, and set all
other replacement entries to zero. Eliminating the exponential rows
then modifies only two lower C-moment rows. The effective equations,
in reversed polynomial coordinates, are

    L(t^j C)=0, 0<=j<=n-4,
    L(t^(n-3) C)-sum_(i=0)^3 M_(2,i)L(t^(n+i-1) C)=0,
    L(t^(n-2) C)-sum_(i=0)^3 M_(1,i)L(t^(n+i-1) C)=0,
    C(1)=0.                                         (2)

The minus signs follow directly from solving the top exponential
rows for B: E_low B+C_low=-M C_top+C_low.

Take the cofactor vector of (2), retaining the common top exponential
determinant and the common original endpoint denominator. Call its
polynomial C_eff; do not normalize its coefficients separately.
For S_C(t)=L_s[(C(t)-C(s))/(t-s)], its associated entries are exactly

    A_eff=-S_Ceff(0),
    H_eff=-S_Ceff'(0)-C_eff(0),
    C_eff,0=C_eff(0), D_eff=C_eff'(0).                (3)

This common-scale statement is cofactor linearity: the retained
exponential sets never contain either appended reconstruction row,
so those rows contribute only their C entries. The same holds after
one or two retained lower-row replacements.

The cofactor expansion of (2) includes the base, its eight singles,
and its six doubles. The interpolation valuation table proves that
the terms beyond the designated eight-set list are divisible by
2^(a+2) relative to the top exponential determinant. In particular
the essential upper-left two-by-two double has been retained.

Put alpha=-n and chi=-n-2phi(n-1). The established actual valuations
in the current class are v_2(a_n)=v_2(a_(n-1)-c_n)=alpha and
v_2(c_n)=v_2(c_(n-1))=chi. The eight-set reduction, with its global
Cauchy bounds and the original common denominator, therefore gives

    v_2(a_n-A_eff), v_2(a_(n-1)-c_n-H_eff)>=alpha+a+2,
    v_2(c_n-C_eff,0), v_2(c_(n-1)-D_eff)>=chi+a+2.   (4)

The -4 endpoint assignment and cases where either appended row is
assigned to the exponential block are included in (4), by the strict
gaps in that reduction. For Xi_eff=A_eff D_eff-H_eff C_eff,0, this
implies

    v_2(Xi_n-Xi_eff)>=alpha+chi+a+2.                 (5)

## 2. Four orthogonal coefficients and exact moment equations

Let Q_j be the raw monic Legendre polynomials, h_j=L(Q_j^2), and
beta_j=j^2/(4j^2-1). Put

    b=beta_(n-1), c=beta_(n-2), d=beta_n,
    s_j=j(j-1)/(2(2j-1)),
    r_j=j(j-1)(j-2)(j-3)/[8(2j-5)(2j-3)].           (6)

The lower n-3 moment equations force

    C_eff=kappa [u Q_n+v Q_(n-1)+b w Q_(n-2)+b x Q_(n-3)].

The nonzero scale and the choice u=1 will be justified below. The
needed monomial expansion is

    t^j=Q_j-s_j Q_(j-2)+r_j Q_(j-4)+lower degrees.   (7)

For the third coefficient, subtract the t^(j-4) coefficient of Q_j,
namely j(j-1)(j-2)(j-3)/[8(2j-1)(2j-3)], from s_j s_(j-2).
This gives exactly r_j.

Divide the relevant moments by b h_(n-3). Since
h_(n-2)=-c h_(n-3), h_(n-1)=bc h_(n-3), and
h_n=-bcd h_(n-3), the two lower moments become x and -cw, while
the four top moments become

    m_0=c v-s_(n-1)x,
    m_1=-cd u+s_n c w,
    m_2=-s_(n+1)c v+r_(n+1)x,
    m_3=s_(n+2)cd u-r_(n+2)c w.                      (8)

Thus the remaining equations are exactly

    x-sum_(i=0)^3 M_(2,i)m_i=0,
    -cw-sum_(i=0)^3 M_(1,i)m_i=0.                    (9)

Every entry of the two-by-four block is retained in these equations.

## 3. A dyadic unit system and a justified common scale

The parameter valuations are

    v_2(b)=2a, c,d are units,
    v_2(s_n)=v_2(s_(n-1))=a-1,
    s_(n+1),s_(n+2) are units,
    v_2(r_(n+1))=v_2(r_(n+2))=a-2.                  (10)

Collect (9) into a system Z(w,x)^T=(R_w,R_x)^T. Its entries are

    Z_ww=1+M_(1,1)s_n-M_(1,3)r_(n+2),
    Z_wx=[-M_(1,0)s_(n-1)+M_(1,2)r_(n+1)]/c,
    Z_xw=c[-M_(2,1)s_n+M_(2,3)r_(n+2)],
    Z_xx=1+M_(2,0)s_(n-1)-M_(2,2)r_(n+1),          (11)

and its right sides are

    R_w=[-M_(1,0)+M_(1,2)s_(n+1)]v
                    +[M_(1,1)d-M_(1,3)s_(n+2)d]u,
    R_x=c{[M_(2,0)-M_(2,2)s_(n+1)]v
                    +[-M_(2,1)d+M_(2,3)s_(n+2)d]u}. (12)

The exact interpolation valuations are

    v_2(M_(1,0),M_(1,1),M_(1,2),M_(1,3))=(2,1,a+3,a+1),
    v_2(M_(2,0),M_(2,1),M_(2,2),M_(2,3))=(1,2,a+1,a+3).

Equations (10)-(12) show that Z is the identity modulo two over
Z_(2), and that both coefficients of u,v in its right side are even.
Hence w,x are integral linear functions of u,v with even coefficients.

Set q_j=Q_j(1), lambda=q_n/q_(n-1), eta=q_(n-2)/q_(n-1), and
zeta=q_(n-3)/q_(n-1). The established parity estimates give
v_2(lambda-1)>=2a+1, eta in 2 Z_(2), and zeta a unit. The endpoint is

    u lambda+v+b(w eta+x zeta)=0.                    (13)

After substituting the linear functions w,x, its v coefficient is
one plus a multiple of 2^(2a+1). Thus u=0 forces v=w=x=0, while u=1
gives a unique solution with

    v in Z_(2), v+1 in 2^(2a+1) Z_(2),
    w,x in 2 Z_(2).                                 (14)

The first n-3 orthogonality rows have independent pivots h_0 through
h_(n-4); the last three equations have rank three on their
four-dimensional complement by the argument just given. Thus (2)
has rank n and a nonzero cofactor vector. It is kappa times the
solution with u=1, for one nonzero kappa common to all four entries
in (3). Its valuation will be determined from (4), not guessed.

## 4. All residues modulo eight

Put rho=(n-1)/4 modulo2. In Z_(2) modulo eight,

    c=d=3,
    M_(1,0)=4, M_(1,1)=2+4rho,
    M_(2,0)=6+4rho, M_(2,1)=4.                      (15)

For example use the exact formulas

    M_(1,0)=2n(n+1),
    M_(1,1)=-n^2(n+1)(2n+1),
    M_(2,0)=n(n+1)(2n-1)(n+2),
    M_(2,1)=M_(1,1)(2n-1)(n+2)*2/3.

The exceptional entries M_(1,3),M_(2,2) have valuation a+1>=3;
their coefficients in (11)-(12) are integral by (10), so they vanish
modulo eight. The same holds for M_(1,2),M_(2,3). They have been
retained and proved irrelevant at this precision, rather than
discarded without justification.

Both off-diagonal entries of Z vanish modulo eight. Each diagonal
is 1+4rho: for a=2 the relevant product has valuation two; for a>=3
it is divisible by eight. By (14), v=-1 modulo eight. Substituting
in (12) gives

    R_w=4+3(2+4rho)=2+4rho mod8,
    R_x=3[-(6+4rho)-12]=2+4rho mod8.

The inverse of 1+4rho is itself modulo eight, and its product with
2+4rho has the same residue. Consequently

    w=x=2+4rho mod8.                                (16)

The inverse system includes its determinant; the essential double
replacement has not been lost in this calculation.

## 5. The exact cross-minor and its scale valuation

Put H=h_(n-1), q=Q_(n-1)(0), k=n^2/(2n-1), and
k_-=(n-2)^2/(2n-5). The Legendre and second-kind identities proved
in raw_Xi_top_block_factorization.md give

    Q_(n-3)(0)=q/c,
    S_n(0)=H/q, S_(n-2)(0)=H/(bq),
    Q_n'(0)=kq, Q_(n-2)'(0)=k_- q/c,
    Q_(n-1)(0)+S_(n-1)'(0)=(2n-1)H/q,
    Q_(n-3)(0)+S_(n-3)'(0)=(2n-5)H/(bq).

Separate the even and odd parts of the four-term polynomial in (3).
The exact resulting quadratic identity is

    Xi_eff/(kappa^2 H)
      =(v+b x/c)[(2n-1)v+(2n-5)x]
                     -(1+w)[k+b k_- w/c].           (17)

All terms involving b w or b x vanish modulo eight by (10),(14).
Also v=-1 modulo eight, 2n-1=k=1 modulo eight, and 2n-5=5 modulo
eight. Hence (16)-(17) give

    Xi_eff/(kappa^2 H)=-5x-w
                     =-6(2+4rho)=4 mod8.            (18)

The common scale is determined exactly, rather than from the separate
top terms. The same two-jet formulas give

    A_eff D_eff=-kappa^2 H (1+w)[k+b k_- w/c].        (19)

Both bracketed factors are units by (14). Meanwhile (4) and the
established actual coefficient valuations imply v_2(A_eff)=alpha
and v_2(D_eff)=chi. Thus

    v_2(kappa^2 H)=alpha+chi=-2n-2phi(n-1).           (20)

Equations (18),(20) put Xi_eff exactly two powers above this
baseline. The error (5) is at least a+2>=4 powers above baseline,
so it cannot cancel the term. This proves (1).

## 6. Scope and verification

Together with the other independently checked parity theorems, the
resulting complete formula is

    v_2(Xi_n)=-2n-2phi(n-1)+2, n=1 mod4;
    v_2(Xi_n)=-2n-2phi(n-1)-2, n=2 mod4;
    v_2(Xi_n)=-2n-2phi(n-1),   n=0 or3 mod4.

The first line includes n=1 only by its separate exact value Xi_1=-29.
With b_n!=0 and [z^3]Q_n=b_n Xi_n, this proves cubic degree at every
n>=1. The dedicated independent review checked the common-scale
bridge and the actual error precision as well as the final congruence.

The script derive_Xi_residue_rational.py expanded the fixed two-by-two
equations as rational functions of a symbolic n and helped identify
the constant residue. The proof uses the short uniform congruences
instead of a numerical scan or a large polynomial factorization.
No absolute-value bound for a transfer coefficient or shrinking
primitive linear form follows. The rationality of e+pi remains open.
