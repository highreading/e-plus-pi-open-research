> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An evaluated mixed-cost transition and a first-return nonmembership lemma

Parent derivation, 9 October 2026. NEW, UNSENT when written, with
DIFFERENT review PENDING. The full general mixed-jet kernel is a
separate new parent note. The original even-d source kernel and full
rising divisor independently PASS A4turn21. The prior complete
mixed-Cauchy theorem and parent multiple-return payment are being
independently audited in A4turn22. No final coefficient upper follows.

Before deriving this note, scoped current/prior/Desktop English
MD/TEX searches find no proved first mixed-return nonmembership or
evaluated quarter-transition minimizer. Earlier SINGLE S_p(r), exact
source kernel, finite Newton payments and root-multiplicity source
completion are REUSE. This is a new application to the actual mixed
common-column compound. No unread external theorem is imported.

## 1. Exact lower payments and their evaluated minimizer

Keep ORIGINAL d=9^(18+32u)-1. Use all full definitions in A2turn13
and the parent multiple-return note. Set

    lambda_j=j+v2(j!), S_n=sum_(j=0)^(n-1)lambda_j,
    T_p=S_p+2E_p+B_p, S_0=T_0=0.

The exact identity c_p=2S_p follows from the definition of c_p.
Take a q-common-column minor containing the atom. In a term with
p product columns, h=q-p return correction columns, NO factorial
part of R, and the atom in the product, the multiple-return lower
payment becomes

    F_q(p)=(q-p)L_d+c_p+2E_p+B_p+(S_q-S_p)
          =q L_d+S_q+T_p-p L_d, 1<=p<=q.             (1)

For v>0 factorial corrections and a=p-v rational Cauchy columns,
the full lower payment is

    (q-p)L_d+v(alpha-2)+S_a+S_(a+q-p)+2E_p+B_p.

Its difference from(1) is at least v(alpha-2-4q). If instead the
atom is one of the W columns, its full extra scalar2^M_d and the
all-return source payment B_p+e_p remain; e_p=v_(p-1) for p>=1,
e_0=0. Its lower payment exceeds the corresponding formal F_q(p)
by at least d-2q+1-2m. This includes p=0. The formal p0 value is
larger than F_q(1), since T_1=0 and L_d>0.

Consequently, under

    alpha-2>4q, d-2q+1-2m>0, q<=d,                  (2)

the minimum of these LOWER payments over all correction patterns
is exactly min_(1<=p<=q)F_q(p). This is not an attainment claim.

The minimizer is evaluated by a strictly increasing digit expression.
For p>=2, write D_p=T_p-T_(p-1). Then

    D_p=lambda_(p-1)+2e_(d-p)+(p-1)+v_(p-2)
       =8p-9+s2(d)-2s2(d-1)+2s2(d-p)
                        -s2(p-1)-s2(d+p-2).          (3)

All quantities refer to ORIGINAL d, with
e_n=v2((2d-2)!/(2n)!) and v_j=v2((d+1)_j).
For2<=p<d,

    D_(p+1)-D_p
      =1+v2(p)+2(1+v2(d-p))+1+v2(d+p-1)>=4.

Thus T_p-pL_d decreases strictly until D_p reaches L_d and then
increases strictly; only equality D_p=L_d can cause a two-point
tie. Equation(3) permits a finite binary search in O(log d) integer
bit operations, without a growing source or determinant. It gives

    p_star=d/4+O(log d).

The mixed lower bound beyond that transition is the evaluated
qL_d+S_q+T_(p_star)-p_star L_d, with the tie retained if present.
At q=p+1 satisfying

    D_p<L_d<D_(p+1),                                (4)

the ONLY minimum pattern has p product columns and ONE W return
column, with no factorial correction and the atom in the product.
The pure q-product term and every other p count have an extra
positive binary depth. Conditions(2) exclude the other patterns.
This identifies the first strict mixed LOWER-payment transition;
it does not yet say the corresponding actual term is nonzero.

## 2. A first mixed-return row outside the source space

The actual normalized mixed row is

    S_p(r)=U_p(0,r).

Let L be a power of2 and write d=2L+rho. Suppose

    2<=rho<L, rho even,
    p ODD, p>=rho+1, rho+p<=L.                       (5)

Use only original return columns0<=r<2L<=d. Let R_p be the binary
span of top contact rows U_d(j,r), 0<=j<=p-2. Then

    S_p is NOT in R_p on these first2L columns.       (6)

No original index is replaced by p: p is the actual mixed Cauchy
column count. The odd-parameter derivative in the general kernel
is essential to this statement.

Proof. Work over F4 and put a(Y)=1+omega Y, b(Y)=1+omega^2Y.
The full general mixed kernel gives, for odd p,

    sum_(r>=0)S_p(r)Y^r
      =Tr(omega^(2p)b^(p-1)/a^p).                   (7)

To check the simplification, before cancellation its numerator is
omega^(2p+1)b^(p+1)+omega^(2p-1)b^(p-1) over a^(p+2).
The bracket omega^2 b^2+1=omega a^2 cancels exactly. Dropping the
odd-parameter term would give a different row.

Write p=2m_c+1. The even-d top row generating functions, after the
finite binary column convolution C_d(Y)=(ab)^d, are

    C_d U_d(2h,Y)
      =Tr(omega^(2d+2h+1)b^(2d+1)/a^(2h+2)),
    C_d U_d(2h+1,Y)
      =Tr(omega^(2d+2h)b^(2d)/a^(2h+2)),
      0<=h<m_c.

Thus a binary combination of these p-1 top rows is

    Tr(b^(2d)Q(Y)/a^(p-1)),
    Q=omega^(2d) sum_(h=0)^(m_c-1)
           omega^(2h)(c_odd,h+c_even,h*omega*b)
                              a^(2(m_c-h-1)),       (8)

with c_even,h,c_odd,h in F2 and deg Q<=p-2.

The first2L columns are unchanged in rank by this finite unit
convolution. Since a^(2L)=b^(2L)=1 modY^(2L), d=2L+rho gives
b^(2d)=b^(2rho) at that precision. Equation(7), after the same
convolution, becomes

    Tr(omega^(2p)a^(rho-p)b^(rho+p-1)) modY^(2L).

Here negative powers denote unit formal series; the original
unreduced exponents d-p and d+p-1 are nonnegative. If S_p belonged
to R_p, clearing both UNIT denominators would give

    P(Y)=b^(p-1)N(Y)+a^(p-1)N^sigma(Y)=0 modY^(2L),
    N=b^(2rho)Q+omega^(2p)a^(rho-1)b^(rho+p-1).

Its degree is at most2rho+2p-3<2L by(5), so P=0 EXACTLY. At the
root of a, b is a unit and N is divisible by a^(p-1). The unique
degree<=p-2 candidate in(8) is consequently

    Q_0=omega^(2p)a^(rho-1)b^(p-rho-1).              (9)

Indeed this candidate makes N=0, and Q-Q_0 would otherwise be
divisible by a^(p-1) with smaller degree. The exponents in(9)
are nonnegative by(5).

But(9) does NOT belong to the binary-constrained space(8). Set
A=a^2=1+omega^2Y^2 and B=b^2=1+omega Y^2=omega(1+omega A).
Put s=(rho-2)/2 and t=(p-rho-1)/2=m_c-rho/2. Then

    Q_0=omega^(2p+t)*a*A^s*(1+omega A)^t.

The coefficient of Y*A^s in this expression is
omega^(2p+1+t), which is nonzero. In(8), the same coefficient must
be omega^(2d+2t)*c_even,t. Their ratio is

    omega^(2p+1-2d-t)
      =omega^(rho/2-2d)=omega^(-L),                 (10)

using p=2m_c+1 and d=2L+rho with d even. Since L is a power of2,
L is nonzero mod3; omega^(-L) is not in F2. This contradicts the
binary condition on c_even,t. It proves(6).

## 3. Conditional attainment at the first strict mixed transition

The separate rectangular root theorem gives rank p-1 for R_p
under(5), because rho+(p-1)<=L. Combined with(6), the original
contact stack [R_p;S_p] has rank p on returns0,...,2L-1. Some p
ORIGINAL return columns therefore give an odd stack minor.

CONDITIONAL on the full established source/factorial-adjugate
premises and the NEW multiple-return payment, suppose(2),(4),(5)
all hold at the SAME original index. Choose the atom and those p
returns; let q=p+1 and use the first q actual residual rows.

The unique minimum pattern from Section1 has one W return and the
atom in the p-column product. Since p is ODD, the unique cheapest
top atom jet is p-1; the remaining top contact rows are0,...,p-2.
The uniquely minimal N_d minor uses T_p on both sides, and its
normalized complementary K_d determinant is odd. The actual rational
Cauchy columns on T_p and the consecutive residual rows have odd
normalized Vandermonde factors. Their first remaining weighted jet
is exactly S_p. Summing over WHICH selected return is in W is the
Laplace expansion of the stack determinant, with the full odd gamma
retained. It is odd for the selected original columns.

Every nonminimal N_d term has at least one extra binary power.
Every other h/v/atom pattern is higher by(2),(4). Hence the actual
complete selected q-common-column minor attains EXACTLY

    L_d+c_p+2E_p+B_p+lambda_p=F_(p+1)(p).            (11)

This is a proposed FIRST surviving corrected compound, not deletion
of the W layer beyond the quarter window. Odd factors and complete
columns are retained before the parity argument. It does not
evaluate a terminal border or claim an integer F4 column operation.

## 4. Remaining scope

The new nonmembership lemma is for ODD p with(5). Equality ties in
(4), EVEN p with tied top atom positions, and the existence of an
infinite original subfamily satisfying ALL of(2),(4),(5) together
remain separate obligations. The cost minimizer alone gives no
attainment. A single actual-index digital check would not establish
the required infinite set, and no original-sized computation is
authorized by this note.

All final two coefficient borders, odd-prime descents, least
clearers, actual all-prime G, primitive denominator and nonzero
whole error remain unchanged and unresolved. No final residual
coefficient upper, producer retirement or e+pi decision follows.
The full note awaits DIFFERENT proof review before any new mixed
attainment is adopted.
