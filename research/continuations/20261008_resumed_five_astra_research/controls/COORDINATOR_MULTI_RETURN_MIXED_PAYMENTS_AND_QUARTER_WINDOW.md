> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Multiple-return mixed payments and a quarter-rank corrected window

Parent derivation, 9 October 2026. DIFFERENT proof review is PENDING.
This note is UNSENT when written. The joint kernel and rising-divisor
precursor are currently under review in A4turn21; the full new mixed
theorem in A2turn13 also awaits DIFFERENT review. The parent rectangular
rank and corrected deformed cross-block notes retain the same status.
No original-sized computation or old arithmetic receipt is rerun.

Before deriving this result, scoped English MD/TEX searches in the
current/prior continuation and Desktop research archive for a multiple
weighted-return mixed payment or a corrected d/4 window find no earlier
proved statement. A2turn13 Sections5--8, in particular its ONE-return
payment, are REUSE. Fresh primary-literature queries return general
Cauchy/factorial determinant work, including Wenchang Chu's 2021
abstract, but no applicable original corrected-compound theorem in the
inspected search-result scope. No unread external theorem is imported.
Finite Newton expansion, its product rule and Cauchy--Binet are classical
reuse. A2turn14 is already researching the full mixed/terminal problem;
this is a new proposed input, not a repeat of a closed result.

## 1. Objects and scopes

Keep the ORIGINAL d=9^(18+32u)-1, u>=0, and all definitions from FULL
A2turn13. In particular d is even, d=2 mod3, and v2(d)=4. Set

    m=1+floor(log2 d), alpha=2d-s2(d),
    L_d=alpha-12, M_d=alpha-d+1,
    lambda_j=j+v2(j!)=2j-s2(j),
    v_j=v2((d+1)_j),
    B_q=binom(q,2)+sum_(j=0)^(q-2) v_j, B_0=0,
    c_q=q(q-1)+2v2(product_(j=0)^(q-1) j!),
    E_q=sum_(n=d-q)^(d-1) v2(h_d/(2n)!),
    Theta_q=c_q+2E_q+B_q.

The complete common columns include the atom and d actual contact
returns; every selected q-column matrix has at most one atom. Its exact
decomposition remains

    C=R N_d A + 2^(L_d) gamma W,
    R=R_C-2^(alpha-2) V,
    W=[2^(M_d)c_bot/2, eta_r^(d+i)], r<d.

The full integer V keeps BOTH factorial terms. gamma is the actual
odd scalar. The full pencil additionally keeps BOTH affine borders
with their 2^alpha factor; no border is removed or assigned a unit
by the following COMMON-column comparison theorem. Every physical
residual row is0<=i<=d+1; all source/return successors remain within
the original maximum moment3d+1 and factorial(6k-4)!.

## 2. A multiple weighted-return mixed determinant divisor

Choose q residual rows M, a actual rational Cauchy columns I, t actual
normalized return columns W_r(i)=eta_r^(d+i), and v arbitrary INTEGER
columns Z, with q=a+t+v. Then

    v2 det[R_C[M,I], W_returns[M], Z[M]]
       >= c_a + sum_(j=a)^(a+t-1) lambda_j.             (1)

An empty sum is zero. No attaining residue or cancellation-free
leading term is claimed in(1).

Proof. Reuse the EXACT mixed Cauchy identity A2turn13(7.1). Its odd
row denominator is displayed there and retained in full. After that
identity pays c_a, its first a columns are the polynomials
binom(i,0),...,binom(i,a-1); all other columns are multiplied by

    Q_I(i)=product_(j in I)(2(d+i+j)+1).

For every j within the physical Newton range,

    2^j j! divides Delta^j Q_I(i),
    2^j j! divides Delta^j W_r(i).

The first assertion follows by writing Q_I as an integer polynomial
in2i: for a term(2i)^b with b>=j, its jth difference is divisible
by2^b j!, hence by2^j j!. Lower-degree terms vanish. The second is
the established EXACT identity

    Delta^j W_r(i)=2^j(r+1)_j eta_(r+j)^(d+i),

and j! divides(r+1)_j. The product rule gives

    Delta^j(Q_I W_r)(i)
      =sum_(b=0)^j binom(j,b) Delta^b Q_I(i)
                              Delta^(j-b) W_r(i+b).

Every summand is divisible by2^j j!: the binomial coefficient pays
the ratio j!/[b!(j-b)!]. All shifted indices remain within the finite
physical range when computing a Newton coefficient through max M.

Use the exact finite Newton expansion on0,...,max M, followed by
Cauchy--Binet for the selected actual rows. The a polynomial columns
force Newton rows0,...,a-1. Every other Newton row is>=a. In the
remaining determinant expand in the t weighted columns. Each term
uses t distinct such rows, whose total valuation is at least
sum_(j=a)^(a+t-1)lambda_j because lambda_j is nondecreasing. The free
integer columns do not lower this payment. Pascal minors are integral.
This proves(1) without any whole-pencil column operation, growing
determinant evaluation, or unpaid denominator change.

## 3. Complete corrected terms without the atom in W

Expand a complete selected q-common-column determinant exactly as in
A2turn13. Let h columns come from W, p=q-h from R N_d A, and v of
those p columns use the factorial part of R. Put a=p-v. If the atom
is NOT among the W columns, all h W columns are weighted returns.
Equation(1), Cauchy--Binet and the full rising divisor pay

    h L_d+v(alpha-2)+c_a+2E_p+B_p
                   +sum_(j=a)^(a+h-1)lambda_j.         (2)

This includes h=0 and v=0. Source-column selections and odd scalars
remain in the exact expansion; these are only lower valuations.

For1<=r<=q<=d, the established exact marginal formulas give the
safe inequalities

    Theta_r-Theta_(r-1)<=10r+3m,
    c_r-c_(r-1)<=4r.

They also hold at r=1, where all three increments are zero. Thus

    Theta_q-Theta_p<=h(10p+5h+5+3m),
    c_p-c_a<=4pv.

Since a+h-1<q<=d, s2(j)<=m and

    sum_(j=a)^(a+h-1)lambda_j >=h(2a+h-1-m).

Subtracting Theta_q from(2) therefore leaves at least

    h(L_d-8q+4h-6-4m)
                     +v(alpha-2-4q+2h).              (3)

This is an exact lower estimate at the stated finite ranges, not
merely a leading quadratic asymptotic.

## 4. Atom taken from the bottom correction

If the atom is among the W columns, h>=1. Its explicit scalar2^M_d
is retained. The other h-1 W columns are weighted returns. All p top
source columns are then returns, so their source payment is stronger:

    B_p^ret=B_p+v_(p-1) for p>=1,
    B_0^ret=0.

This follows from the same determinant-one finite Newton expansion
as the rising-divisor theorem, now extracting a rising factor in
EVERY selected row. Define e_p=v_(p-1) for p>=1 and e_0=0. Then

    e_p>=p-m-2, M_d>=d-m+1.

For p>=1 the first follows from
v_(p-1)=p-1+s2(d)-s2(d+p-1), with d+p-1<2d and hence s2<=m+1;
the displayed weaker estimate also holds at p=0.

Compared with(2), the exact lower payment in this case has the extra

    M_d+e_p-lambda_(a+h-1).

Because lambda_j<=2j, this extra is at least

    d+p-2q+2v+1-2m >=d-2q+1-2m.                    (4)

The atom c_bot/2 is used only as an integral FREE column in the
mixed determinant. No unproved factorial Newton divisibility of
the atom is assumed. This also covers p=0 and a=0.

## 5. A larger complete mixed-compound comparison window

Assume q<=d and the THREE strict inequalities

    L_d>8q+4m+6,
    alpha-2>4q,
    d-2q+1-2m>0.                                    (5)

Every correction term with h+v>0 has valuation at leastTheta_q+1:
use(3), and add the positive bound(4) in the atom-in-W case. The
uncorrected term keeps its old divisorTheta_q. Therefore the FULL
selected common-column minors satisfy

    det C_S[M,:] =det(R_C N_d A_S)[M,:]
                          mod2^(Theta_q+1),           (6)

and both are divisible by2^Theta_q. This strengthens the prior
10q+3m<L_d criterion by paying ALL weighted W columns simultaneously.
The factorial part of R and the atom correction are not deleted.

Let q_quarter be the largest ODD integer satisfying(5). At all
original indices,

    q_quarter=d/4-O(log d).

The second and third inequalities are then satisfied with linear
slack for sufficiently large original d. The exact first inequality,
including the log term and constant, remains in force. This theorem
does not claim comparison beyond that window or at the full d+1
common rank; the missing direction still requires bottom corrections.

## 6. Optimal physical source flag through the quarter window

CONDITIONAL on the separate parent rectangular rank proof, restrict
the SAME original k=d+1=9^(18+32u) to

    (9/8)2^a<k<(7/6)2^a, a=floor(log2 k),
    L=2^(a-1), rho=d-2L.

Then2L<=d, L/4-1<rho<L/3-1. For every odd q<=q_quarter,

    rho+q-1 <rho+d/4-1
              =L/2+5rho/4-1<L.

The root-rank criterion rho+2m_contact<=L applies with
m_contact=(q-1)/2. It produces an attaining nested ORIGINAL-column
flag on the minimizing consecutive physical top rows with source
depthB_q. Combined with(6), the COMPLETE first q residual physical
rows attainTheta_q, retaining the full odd cofactor scalar.

The original-index interval is infinite by the established irrational
rotation of18 log2 9+32u log2 9. The parent does not change k to a
freely chosen integer, assume binary digit statistics, or run a
growing column-selection algorithm. Earlier rectangular and mixed
proofs are CONDITIONAL dependencies until DIFFERENT review.

### 6.1 Even ranks and a nested flag at EVERY intervening size

The existing A2turn13 atom-cofactor criterion is REUSE: for an odd
q the contact row test is U_0,...,U_(q-2); for an even q it is
U_0,...,U_(q-3),U_(q-2)+U_(q-1). Here U_j is the actual fully rising-
normalized binary contact row. At even q the two cheapest atom
positions tie; their normalized atom units both have parity1, and
their cofactor contributions add. This tie is retained.

On the subfamily above, the root criterion gives full rank of the
first2m_contact contact rows for every2m_contact<=q_quarter-1.
Consequently the even q test also has rank q-1: it is an independent
set of q-2 ordinary rows and a nonzero sum of the next two independent
rows. In particular this is NOT an assumption that the even source
minor has a unique cheapest atom position.

These attaining ORIGINAL return subsets can be nested at EVERY
size q=5,6,...,q_quarter. Define R_q to be the q-1-dimensional contact
row space in the atom-cofactor test. Then R_q is a subspace of R_(q+1):
an odd-to-even step keeps all previous ordinary rows and adds the
new sum; an even-to-odd step embeds that sum in the two ordinary
rows that replace it. A subset of original columns giving an
invertible evaluation on R_q remains independent on R_(q+1), and
the rank statement permits extension by ONE additional original
return column. Start with the already established q5 columns1,0,5,4.
The least extending original index gives a finite selection rule.

Thus source depth B_q and complete corrected depth Theta_q are
attained at EVERY q in that interval, not only odd q. This is a
minor/flag theorem. It does not assert that the specific old
row-constant division-by2 elimination procedure extends unchanged
at all ranks, or evaluate its odd interpolation cofactors.

## 7. What this does not settle

The new proposed progress is a multiple-return lower payment and a
COMPLETE corrected comparison/attaining flag through about d/4 on
an explicit infinite ORIGINAL subfamily. It does not bound the joint
terminal coefficients, cover every original index, pay other odd
primes, or complete the rank d+1 common columns. BOTH terminal borders,
least clearers, actual all-prime final G and the nonzero whole error
remain unchanged. The required residual coefficient UPPER bound is
still OPEN. No producer retirement or rationality/irrationality
conclusion for e+pi follows from this note.

No additional finite check is needed merely to mirror the product rule.
A DIFFERENT full proof audit should inspect the mixed Newton payment,
all h/v terms, atom case, strict range and source transfer together.
