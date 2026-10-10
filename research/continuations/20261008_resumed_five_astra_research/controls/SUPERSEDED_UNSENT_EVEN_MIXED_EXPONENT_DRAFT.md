> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Both parities and equality ties at the first mixed transition

Coordinator proof, 9 October 2026. NEW; DIFFERENT review is PENDING.
This extends, without replacing its historical text, the earlier ODD-p
nonmembership and mixed-cost note. The full higher mixed kernel,
including its ODD auxiliary derivative, also awaits DIFFERENT review.
FULL A4turn22 independently PASSES the source/factorial-adjugate,
rectangular physical-rank and multiple-return quarter-window premises.
The new conclusions below are not included in that completed audit.

Before this derivation, scoped English MD/TEX searches in the current,
previous and Desktop research find the earlier ODD-p note but no proved
both-parity exclusion from R_(p+1) or complete equality-tie attainment.
Primary web searches for this mixed Cauchy/Newton source problem return
no matching theorem in the inspected result scope. The previously
studied OpenAI Catalan transfer and all classical finite-field root,
Newton-product and irrational-rotation tools are REUSE. No unread
external theorem or exhaustive literature-novelty claim is imported.

## 1. Original objects and the stronger target

Keep ORIGINAL d=9^(18+32u)-1, its v2(d)=4, actual returns r<d,
complete corrected common columns and their full odd scalars. Let
L be dyadic and write d=2L+rho. Assume

    rho even, rho>=4, p>=rho+1, rho+p<=L, 2L<=d.       (1)

These are conditions on the ORIGINAL d and an ACTUAL mixed product
column count p. They do not introduce a changed research index.
The final application has rho divisible by16 and hence rho>=16.

On the first2L original return columns define U_j=U_d(j,bullet).
For the minimizing atom-containing source cofactor, its binary row
space after all actual integer divisions is

    R_q = span(U_0,...,U_(q-2))                 if q is odd,
    R_q = span(U_0,...,U_(q-3),U_(q-2)+U_(q-1)) if q is even.

Thus dim R_q=q-1 under the independently passed rectangular criterion.
The full actual mixed bottom row is S_p=U_p(0,bullet). The NEW claim is

    S_p is NOT in R_(p+1), for BOTH parities of p.       (2)

Since R_p is a subspace of R_(p+1), this is stronger than the previous
ODD-p exclusion from R_p and also covers EVEN p. All row-space claims
below concern finite normalized PARITY matrices. The binary column
convolution is not an integer operation on the whole pencil.

## 2. A shared exact degree reduction

Work over F4, omega^2+omega+1=0, with coefficientwise conjugation sigma
and trace. Put a=1+omega Y, b=1+omega^2 Y, and C_d=(ab)^d. This is a
unit triangular convolution on the first2L binary columns. The full
mixed kernel gives

    S_p(Y)=Tr(omega^(2p)*b^(p-1)/a^p)       if p is odd,
    S_p(Y)=Tr(omega^(2p+1)*b^(p+1)/a^(p+2)) if p is even.  (3)

The ODD-p derivative is essential to the first formula. The already
proved EVEN-d top rows, after the SAME convolution, are

    C_d U_(2h)   =Tr(omega^(2d+2h+1)*b^(2d+1)/a^(2h+2)),
    C_d U_(2h+1) =Tr(omega^(2d+2h)*b^(2d)/a^(2h+2)).     (4)

Modulo Y^(2L), a^(2L)=b^(2L)=1, so b^(2d)=b^(2rho).
Every top combination from R_(p+1) below takes the form

    Tr(b^(2rho)*Q/a^p), deg Q<=p-1.                    (5)

In either parity, a hypothetical equality with C_d S_p leads, after
clearing BOTH unit denominators, to

    b^p N+a^p N^sigma=0 mod Y^(2L),
    N=b^(2rho)Q+c*a^e*b^(rho+p-1),                    (6)

where (e,c)=(rho,omega^(2p)) at odd p and
(rho+2,omega^(2p+1)) at even p. The degree of(6) is at most
2rho+2p-1<=2L-1 by(1). Hence(6) is the EXACT zero polynomial.
At the root of a, b is a unit, so a^p divides N. The unique possible
Q of degree at most p-1 is consequently

    Q_0=c*a^e*b^(p-rho-1).                            (7)

Indeed(7) makes N zero, and Q-Q_0 otherwise has to be divisible by
a^p with smaller degree. All exponents in(7) are nonnegative by(1).
This is a finite degree argument, not an infinite rational-function
identity deduced without a truncation bound.

## 3. ODD p: the new tied source row cannot repair the obstruction

Write p=2m_c+1. The paired rows U_0,...,U_(p-2) have common-denominator
numerator

    Q_old=omega^(2d)*sum_(h=0)^(m_c-1)
        omega^(2h)*(c_odd,h+c_even,h*omega*b)
                           a^(2(m_c-h-1)),
    deg Q_old<=p-2, c_odd,h,c_even,h in F2.

The extra tied source row for q=p+1 EVEN is U_(p-1)+U_p. Formula(4)
and omega*b+1=omega^2*a evaluate it as

    C_d(U_(p-1)+U_p)=Tr(omega^(2d+p+1)*b^(2d)/a^p).

Thus the numerator in(5) is

    Q=a*Q_old+c_new*omega^(2d+p+1), c_new in F2.        (8)

The unique candidate(7) is Q_0=omega^(2p)*a^rho*b^(p-rho-1).
At the root of a it vanishes, so(8) forces c_new=0. Dividing by a
reduces the candidate to

    Q_old,0=omega^(2p)*a^(rho-1)*b^(p-rho-1).

For completeness, put A=a^2 and B=b^2=omega*(1+omega A),
s=(rho-2)/2, t=(p-rho-1)/2=m_c-rho/2. Then

    Q_old,0=omega^(2p+t)*a*A^s*(1+omega A)^t.

Its coefficient of Y*A^s is omega^(2p+1+t). In the allowed Q_old
space this coefficient must be omega^(2d+2t)*c_even,t: the relevant
paired row is h=t, since m_c-h-1=s. Their ratio is

    omega^(2p+1-2d-t)=omega^(rho/2-2d)=omega^(-L).

The equalities are exponent congruences modulo3, using p=2m_c+1 and
d=2L+rho. Since dyadic L is nonzero modulo3, omega^(-L) is not in F2.
This contradicts the binary coefficient. It proves(2) at ODD p,
including the extra source row that was absent from the earlier lemma.

## 4. EVEN p: retain both minimizing atom positions

Write p=2m_c. Now q=p+1 is ODD, so R_q consists of all first p contact
rows. Formula(4) gives the numerator in(5) as

    Q=omega^(2d)*sum_(h=0)^(m_c-1)
       omega^(2h)*(c_odd,h+c_even,h*omega*b)
                               a^(p-2h-2).           (9)

The unique candidate(7) is

    Q_0=omega^(2p+1)*a^(rho+2)*b^(p-rho-1).

Put s=(rho+2)/2, t=(p-rho-2)/2=m_c-rho/2-1. These are nonnegative:
p even and p>=rho+1 imply p>=rho+2. Then

    Q_0=omega^(2p+1+t)*b*A^s*(1+omega A)^t.

Its Y*A^s coefficient is omega^(2p+t). The allowed coefficient in(9)
is omega^(2d+2t)*c_even,t, since again m_c-t-1=s. Here t may be zero;
rho>=4 ensures t<=m_c-3, so the indicated paired row is in range.
The ratio is

    omega^(2p-2d-t)=omega^(rho/2-2d)=omega^(-L),       (10)

again outside F2. This proves(2) at EVEN p. No odd-parameter shortcut
or deletion of one tied atom position is used.

For the rank premise, at odd p the q=p+1 EVEN source requires the
first p+1 contact rows. Since rho+p is odd and L is even, (1) implies
rho+p+1<=L. At even p the q ODD source requires the first p contact
rows and rho+p<=L suffices. Thus in BOTH cases the rectangular proof
pays dim R_q=p; it also pays dim R_p=p-1. These finite integer cutoffs
are retained, rather than rounding a parity-dependent condition away.

## 5. Strict and tied first mixed attainment

Reuse the exact cost quantities and increasing digit formula from the
previous note:

    F_q(p)=q L_d+S_q+T_p-p L_d,
    D_p=T_p-T_(p-1), D_(p+1)-D_p>=4.

Define s=min{r>=2:D_r>=L_d}, p=s-1, q=s. At sufficiently large original
indices p>=2 and q<=d. Then

    D_p<L_d<=D_q.

Keep the strict exclusions alpha-2>4q and d-2q+1-2m>0. These exclude
all factorial corrections, atom-in-W patterns and p=0 at the minimum.

If D_q>L_d, there is exactly one minimum product count p, and exactly
ONE W return. The source atom is in the p product columns, with its
actual unique odd-p position or tied EVEN-p positions. Its complete
leading contact cofactor is R_p. The normalized first unused bottom
jet is S_p, by the full mixed kernel at the actual Cauchy count p.
Summing over WHICH selected return belongs to W is the Laplace
expansion of det[R_p;S_p]. Equation(2), with dim R_p=p-1, makes this
stack rank p. Some p ORIGINAL return columns therefore attain the
complete q-common-column depth F_q(p).

If D_q=L_d, only TWO product counts minimize: p (one W) and q (pure).
Let v_new complete R_p to R_q as follows:

    v_new=U_(p-1)+U_p if p is ODD;
    v_new=U_(p-1)     if p is EVEN.

In the EVEN case R_p already contains U_(p-2)+U_(p-1), so adding
U_(p-1) gives exactly R_q. The binary determinant of these row-basis
changes is one. After their full integer divisions, the unique
minimal N_d minors, complementary K_d determinants, normalized
Cauchy Vandermondes, actual atom coefficients and gamma all have
ODD scalar values, hence value ONE in F2. Consequently the SUM of
the two complete leading contributions, for the SAME selected
original columns and residual rows, is precisely

    det[R_p;v_new]+det[R_p;S_p]=det[R_p;v_new+S_p].     (11)

There is no omitted relative unit at binary precision; all odd factors
are retained before this reduction. The equality of costs gives
F_q(p)=F_q(q)=Theta_q. Nonminimal N_d/source terms and every other
correction pattern have at least one extra binary power. Since
S_p is NOT in R_q, v_new+S_p is NOT in R_p. Thus(11) has rank p and
some p ORIGINAL columns attain this tied full depth. A rank statement
about either summand alone would not have paid this cancellation.

These leading-compound identifications, including EVERY relative
scalar, are explicit DIFFERENT audit obligations. The previous
multiple-return theorem supplied lower payments only; attainment
here uses the new source-space argument and the full parity expansion.

## 6. Infinitely many ORIGINAL indices, without a parity filter

Keep k=d+1=9^(18+32u), a=floor(log2 k), L=2^(a-1), and choose the SAME
nonempty original interval as the independently passed quarter flag:

    (9/8)2^a<k<(7/6)2^a.

Then d=2L+rho, L/4-1<rho<L/3-1, and rho is divisible by16 at all
sufficiently large indices. The exact digit formula gives
p=s-1=d/4+O(log d). Hence p>=rho+1 and rho+p<=L hold with linear slack;
the sharper rank cutoff rho+p+1<=L also holds when it is required.
The other two strict exclusions hold with linear slack because
alpha=2d+O(log d) and m=O(log d). All returns stay below2L<=d.

Irrationality of log2 9 follows from prime factorization. Therefore
the established irrational-rotation density for fractional parts
of (18+32u)log2 9 hits this interval infinitely often. Since Sections
3--5 now cover BOTH parities and BOTH equality cases, no unproved
parity/equality distribution assertion is needed. This supplies an
INFINITE ORIGINAL subfamily of the proposed first mixed attainment.

The already completed original u=0 digit receipt has an EVEN p and a
strict cost crossing. It previously fell outside the ODD-only lemma.
It now fits the extended symbolic conditions, conditional on this
NEW DIFFERENT review. No digit calculation, source table, determinant
or original vector solve is repeated, and one tuple is not used to
prove the infinite subfamily.

## 7. Scope and remaining obligations

This is a proposed first surviving complete mixed common-column
cofactor, including equality cancellation, at the actual quarter
transition. It does not evaluate either coefficient border, their
joint final gcd or a terminal coefficient upper. A full two-border
bound, odd-prime control, least clearer, actual primitive denominator
and nonzero whole-error decay remain OPEN. It does not retire this
producer or decide rationality of e+pi. Independent proof review
must precede adoption of the new attainment theorem.
