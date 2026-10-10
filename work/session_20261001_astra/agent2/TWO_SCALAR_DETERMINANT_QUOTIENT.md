> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual two-scalar determinant quotient

Status: proved exact identities, a conditional endpoint theorem, and a companion bound using primitive high-minor coordinates. Exact finite checks pass at the frozen indices n=4,6,8,10. A uniform even-degree sign or pole-separation theorem remains unproved. Full-remainder nonvanishing and sufficient control of the actual reduced denominator remain unresolved.

This continuation preserves the completed domain correction, previous reviews, projection-remainder notes, and frozen certificates. It does not repeat the separate audit of the projection row bounds or their high-row slack.

## 1. Actual system and notation

The identities below hold for 1<=b<=n. The growing regime is n even, b=n/2, with the finite tests restricted to n=4,6,8,10.

Use the monic rational polynomials p_k, the moment functional

L(P)=integral_{-1}^1 P((1+iu)/2) du,
h_n=2(-1)^n/((2n+1)binom(2n,n)^2),
ell_j(t^k)=1/(n+k+1-j)!, 0<=j<=b.

Every factorial argument is at least n+1-b>=1. Set

Uref=p_(n+1),
Uhigh_lj=ell_j(p_(n+l)), 1<=l<=b-1,
evec=(1,...,1),
Bform(x,y)=det[Uhigh;x;y].

Write

A0=p_n(1)>0, A1=p_(n+1)(1)>0,
v0=L(p_n/(1-t)), v1=L(p_(n+1)/(1-t)), h=h_n,
V(t)=K_n(t,1), W(t)=1/(1-t)-H_n(t).

Here H_n is the projection polynomial. The scalar v0 is distinguished from the functional row vrow=ell(V). Define wrow=ell(W).

The actual reduced equations have matrix [Uhigh;evec+vrow]. Choose its maximal-cofactor vector Bcoeff by

Bcoeff dot x=det[Uhigh;evec+vrow;x].

Then the actual endpoints and complete evaluated remainder satisfy

Y=B(1)=C(1)=-D_V,
D_V=Bform(evec,vrow),
R(1)=D_W+T,
D_W=Bform(evec,wrow), T=Bform(vrow,wrow).

The sign in Y is from interchanging the last two rows. These identities remain valid if the cofactor vector vanishes. D_V!=0 implies full row rank of the reduced matrix and a nonzero actual matched endpoint. No quotient below is asserted on D_V=0.

Let X=A_HP(1) denote the reconstructed polynomial endpoint, avoiding confusion with A0,A1. On Y!=0, the actual primitive denominator is q=den(X/Y)>0, and the integer form is L_int=p_int+q(e+pi)=qR(1)/Y.

## 2. Rational contractions and the three exact signs

For a polynomial P define the rational partial-sum row

T_j(P)=sum_k [t^k]P(t) E_(n+k-j),
E_m=sum_(r=0)^m 1/r!.

The minimum index n-j is nonnegative. Absolute convergence of the complete factorial tails gives

ell_j(P/(1-t))=e P(1)-T_j(P).

Put

arow=ell(Uref/(1-t)), crow=ell(p_n/(1-t)),
tau_U=T(Uref), tau_P=T(p_n),
z0=Bform(evec,arow), z1=Bform(evec,crow).

Thus

arow=e A1 evec-tau_U,
crow=e A0 evec-tau_P,
z0=-Bform(evec,tau_U), z1=-Bform(evec,tau_P).

Both z0 and z1 are rational. The rows arow and crow generally contain e; their rationality is not asserted. The name arow here is the tail row in the current task, not the differently named elementary rational endpoint row in the historical frozen checker.

Christoffel-Darboux and its integrated projection identity give exactly

V=(A1 p_n-A0 Uref)/(h(1-t)),
W=(v0 Uref-v1 p_n)/(h(1-t)).

Consequently

D_V=(A1 z1-A0 z0)/h,
D_W=(v0 z0-v1 z1)/h.                                  (1)

The same projection identity, multiplied by 1-t and evaluated at t=1, gives

A1 v0-A0 v1=h.                                        (2)

Indeed (1-t)W=1-(1-t)H_n tends to 1. The functional rows are

vrow=(-A0 arow+A1 crow)/h,
wrow=(v0 arow-v1 crow)/h.

Their coefficient determinant relative to the ordered pair (arow,crow) is

(A0 v1-A1 v0)/h^2=-1/h.

Therefore the complete companion has the asserted sign:

T=-Bform(arow,crow)/h.                                (3)

No high-row estimate enters (1)-(3). They concern the actual monic cofactor system and both complete tails.

## 3. Conditional endpoint theorem, including zero coordinates

The reference analysis gives

alpha=v1/v0<0, c=-alpha in (0,1/6),
bref=A1/A0>=1/2,
epsilon_n=|v0|/A0>0.

These facts use the strict alternating signs of the second-kind moments and the positive endpoint recurrence. In particular c<bref. They are reference facts independent of b; no fixed-b determinant limit is needed.

Suppose z0*z1<=0 and (z0,z1)!=(0,0). Then

|A1 z1-A0 z0|=A0|z0|+A1|z1|>0.

Hence D_V!=0 and the actual matched endpoint is nonzero. Also

|v0 z0-v1 z1|
 =|v0| |z0+c z1|
 <=|v0|(|z0|+c|z1|)
 <=epsilon_n(A0|z0|+A1|z1|).

It follows that

|D_W/D_V|<=epsilon_n.                                 (4)

This proves the proposed conditional lemma without a repair to its hypothesis.

The boundary cases are explicit. If z0=0 and z1!=0, then

D_W/D_V=-v1/A1,
|D_W/D_V|=epsilon_n c/bref<epsilon_n/3.

If z1=0 and z0!=0, then D_W/D_V=-v0/A0 and its magnitude is epsilon_n. If both vanish, D_V vanishes and this argument supplies no usable endpoint.

For z0!=0, put eta=z1/z0. The actual quotient is

D_W/D_V=-(v0/A0)(1-alpha eta)/(1-bref eta),             (5)

with its pole at eta=A0/A1. The missing-coordinate case z0=0 has already been handled without using eta.

A sign-free formulation is useful even though all frozen tests pass. For any nonzero pair define

Delta=|A1 z1-A0 z0|/(A0|z0|+A1|z1|).

Then 0<=Delta<=1; Delta>0 is exactly endpoint nonvanishing. The opposite-sign hypothesis gives Delta=1. On Delta>0 the same triangle inequality proves

|D_W/D_V|<=epsilon_n/Delta.                            (6)

Thus a quantitative pole-avoidance question is to bound Delta from below on an unbounded even growing-degree set. Merely avoiding exact equality at the pole does not control how close the projective coordinate can approach it.

## 4. Primitive high-minor coordinates and exact companion reduction

On D_V!=0 the high block has rank b-1. Clear its monic row factors by setting

R_lj=(2n+2l)! Uhigh_lj.

Rodrigues makes these integers. Remove each nonzero row content c_l, giving R0. For 0<=i<j<=b let

m_ij=(-1)^(i+j+1) det(R0 with columns i,j deleted),
mu=gcd_(i<j)|m_ij|,
mbar_ij=m_ij/mu.

The omitted-column indices are zero based and retained columns keep their natural order. Full high-row rank gives mu>0. For b=1, the empty minor is 1 and mbar_01=1.

Define

Bbar(x,y)=sum_(i<j) mbar_ij(x_i y_j-x_j y_i),
gamma=(product_l c_l)mu/product_l(2n+2l)!.

Then exactly Bform=gamma Bbar, with gamma>0 rational. This is the previously derived primitive high-minor normalization, now applied to the actual two-scalar quotient.

Set

Z0=-Bbar(evec,tau_U), Z1=-Bbar(evec,tau_P),
K_tail=Bbar(tau_U,tau_P),
d=A1 Z1-A0 Z0.

These contractions are rational, not necessarily integers, because the endpoint rows are monic partial-sum rows. They satisfy

z0=gamma Z0, z1=gamma Z1, D_V=gamma d/h.

Expanding the two full tail rows gives

Bbar(arow,crow)=e d+K_tail.

Therefore the requested reduced companion expression is

Bform(arow,crow)/(h D_V)=e+K_tail/d,                    (7)
T/D_V=-e-K_tail/d=r_e-e,
r_e=-K_tail/d in Q.                                   (8)

The common high-row factor cancels exactly. There is no product of separate high-row norms in these formulas.

For the principal companion define the rational second-kind parts

w0=L((p_n-A0)/(t-1)),
w1=L((Uref-A1)/(t-1)).

Since L(1/(1-t))=pi, one has v0=A0*pi-w0 and v1=A1*pi-w1. Hence

r_pi=(w1 Z1-w0 Z0)/d in Q,
D_W/D_V=r_pi-pi.                                     (9)

Combining (8)-(9) with the actual cofactor signs gives

X/Y=-r_pi-r_e,
R(1)/Y=e+pi-r_pi-r_e,
q=den(-r_pi-r_e).                                    (10)

Equation (10) preserves every cancellation in the actual rational endpoint. Separate denominators of d, r_e, or r_pi do not replace q. Row, maximal-minor, and any later common contraction contents are already common scales; they cannot be counted twice as arithmetic gains.

Known irrationality of e and pi separately implies T/D_V and D_W/D_V are individually nonzero on this domain. It does not rule out cancellation of their sum. Full-remainder nonvanishing remains a separate unresolved requirement.

## 5. A companion bound using the same primitive minors

Let N be the integer antisymmetric matrix with N_ij=mbar_ij for i<j and N_ji=-mbar_ij. Then Bbar(x,y)=x^T N y.

For a coordinate vector f_j define

kappa_j=Bbar(evec,f_j),
S_j=sum_k |N_jk|,
C_(n,b)=min_(j:kappa_j!=0) S_j/|kappa_j|.

If d!=0, at least one kappa_j is nonzero: otherwise Bbar(evec,x)=0 for every x, forcing Z0=Z1=0. Thus C_(n,b) is a well-defined positive rational number. Since kappa_j is the negative of the j-th row sum of N, one has C_(n,b)>=1. No uniform upper bound for it is asserted.

The alternating form Bbar factors through the two-dimensional quotient by the high-row span. Its Plucker identity is consequently

kappa_j Bbar(arow,crow)
 =Z0 Bbar(f_j,crow)-Z1 Bbar(f_j,arow).                 (11)

For example, this identity follows immediately by writing the induced form as a two-by-two determinant and expanding. It remains valid when either Z coordinate vanishes.

The same identity with the rational partial-sum rows gives another exact companion formula:

K_tail=[Z1 Bbar(f_j,tau_U)-Z0 Bbar(f_j,tau_P)]/kappa_j. (12)

Thus either the exact expression (7) or the bound below can be evaluated from the same primitive minor coordinates.

Put N0=n+1-b>=1. For every polynomial P and every permitted j,

|ell_j(P/(1-t))|<=e ||P||_1/N0!.

To prove this, expand the complete factorial tail for each monomial. Its starting index is at least N0, and sum_(r>=0)1/(N0+r)!<=e/N0!. Absolute convergence justifies the triangle inequality.

Applying this bound to (11) gives

|Bbar(arow,crow)|
 <=C_(n,b) e[|Z0| ||p_n||_1+|Z1| ||Uref||_1]/N0!.

The pole separation Delta is unchanged on replacing z0,z1 by Z0,Z1. Therefore

|T/D_V|
 <=C_(n,b) e/(Delta N0!)
   *max(||p_n||_1/A0, ||Uref||_1/A1)
 <=C_(n,b) e 4^(n+1)/(Delta (n+1-b)!).                (13)

The last inequality uses the elementary reference bounds ||p_k||_1<=2^k and p_k(1)>=2^(-k). No separate products of high-row norms occur. C_(n,b) retains possible directional cancellation in the primitive minors; removing the common high-row scale does not automatically bound that quantity.

Equations (6) and (13) yield the complete estimate

|R(1)/Y|
 <=[epsilon_n+C_(n,b)e4^(n+1)/(n+1-b)!]/Delta.          (14)

Under the sign hypothesis Delta=1. For b=floor(n/2),

log(e4^(n+1)/(n+1-b)!)=-n log n/2+O(n).

Thus an exponential-in-n bound for C_(n,b) would make this companion upper bound factorially small. Such a bound is not proved. Nor would it establish nonvanishing of the sum by itself, since D_W may be much smaller than its upper bound.

An exact sufficient same-index target, retaining q, is

(q/Delta)[epsilon_n+C_(n,b)e4^(n+1)/(n+1-b)!] ->0,
D_V!=0 and D_W+T!=0.                                 (15)

Using the scalar reference estimate log epsilon_n=-tau*n+O(1), tau=2log(1+sqrt(2)), a convenient stronger set of hypotheses is

log(q/Delta)<=(tau-eta)n for a fixed eta>0,
log C_(n,b)=O(n),
D_W+T!=0

on the same unbounded even-degree set. These hypotheses would imply nonzero shrinking integer forms. They are not established here. This uses the scalar reference estimate from ACTUAL_PROJECTION_REMAINDER.md, not a fixed-b determinant asymptotic.

## 6. Exact frozen evidence

The controller completed check_two_scalar_quotient.py successfully. It used only the frozen controls in growing_regime_certificates.json, with n exactly 4,6,8,10 and b=n/2. It did not rerun the original canonical solver or introduce any additional approximation degree.

The checker constructs the reference polynomials from their explicit Legendre coefficients, evaluates rational factorial sums and moments, and contracts the high minors. It independently compares those contractions with determinants and the saved projection endpoint. It verifies (1)-(3), the primitive high scale, both rational companions in (8)-(10), the saved B vector in the reduced equations, and the existing fully reduced q. The source certificate was checked unchanged during execution.

| n | b | sign z0 | sign z1 | Delta | digits of the unchanged actual q |
|---:|---:|---:|---:|---:|---:|
| 4 | 2 | negative | positive | 1 | 10 |
| 6 | 3 | negative | positive | 1 | 23 |
| 8 | 4 | negative | positive | 1 | 43 |
| 10 | 5 | negative | positive | 1 | 68 |

For example, the first exact control is

z0=-309857/2633637888000,
z1=90073/146313216000,
eta=-1621314/309857,
q=1579037328.

All four pass the weaker sign condition. There is no failed-sign witness in this frozen set. This is exact finite evidence, not a proof of any unbounded sign law.

Full rational z0,z1, eta, the pole A0/A1, primitive minors, row and minor contents, gamma, Z0,Z1,K_tail,d, both rational companions, and the actual p_int,q are retained in two_scalar_quotient_evidence.json. That file also records hashes of the frozen source and checker. The saved field named K is K_tail in this note.

## 7. Concrete recurrence attempt for even growing degrees

Because the frozen sign test passes, the next question is an actual-family propagation argument. The following exact recurrence represents the relevant determinants and identifies the missing closure.

For k>=0 and m>=1 define the rational array

Q_(k,m)=sum_r [t^r]p_k(t)/(m+r)!.

Its initial rows and recurrence are

Q_(0,m)=1/m!,
Q_(1,m)=1/(m+1)!-1/(2m!),
Q_(k+1,m)=Q_(k,m+1)-Q_(k,m)/2+beta_k Q_(k-1,m), k>=1. (16)

This follows directly from the actual monic polynomial recurrence. Define

H_(k,m)=Q_(k,m)-Q_(k,m+1)
       =Q_(k,m)/2-Q_(k+1,m)+beta_k Q_(k-1,m).          (17)

After adjacent column differences in the original z determinants, the evec row becomes (1,0,...,0). The last-row difference telescopes exactly:

(ell_(j+1)-ell_j)(P/(1-t))=ell_(j+1)(P).

Consequently, for s=0,1,

z_s=(-1)^(b+1) D_s(n,b),                              (18)

where D_s(n,b) is the b-by-b determinant with columns j=0,...,b-1, high rows

H_(n+l,n-j), l=1,...,b-1,

and last row Q_(n+1-s,n-j). These are the actual contractions, not limiting Taylor-jet determinants.

An explicit two-column-shift identity, valid for k>=2, is

Q_(k,m+2)
 =Q_(k+2,m)+Q_(k+1,m)
  +(1/4-beta_(k+1)-beta_k)Q_(k,m)
  -beta_k Q_(k-1,m)+beta_k beta_(k-1)Q_(k-2,m).         (19)

It follows by applying (16), solved for Q_(k,m+1), twice. Equation (19) supplies a concrete exact transfer for the n to n+2 column shift.

A finite minor expansion makes its relation to the changing dimension explicit. Let J be the tridiagonal operator on the k index defined by

(Jq)_k=q_(k+1)+q_k/2-beta_k q_(k-1),

with beta_0=0 and the absent negative index omitted. Let Qmat_(n,d) have entries Q_(k,n-j), k>=0, 0<=j<d. Let F_s(n,b) have the b-1 rows of I-J selected at k=n+1,...,n+b-1 and final row selecting k=n+1-s. Then

D_s(n,b)=det(F_s(n,b) Qmat_(n,b)),
D_s(n+2,b+1)=det(F_s(n+2,b+1) J^2 Qmat_(n,b+1)).       (20)

In the growing even regime all factorial indices in these matrices stay positive. The left factor in the second determinant has finite support. Cauchy-Binet therefore expresses it as the finite sum

sum_(I:|I|=b+1) det((F_s(n+2,b+1)J^2)[:,I])
                    det(Qmat_(n,b+1)[I,:]).           (21)

This is an exact transfer on an enlarged array of minors. It does not close on the two previous b-by-b contractions. The column window changes from n,...,n-b+1 to n+2,...,n-b+2; the high-row degree window changes as well. Additional minors are required. Moreover J has a negative subdiagonal and (19) contains the coefficient -beta_k. The available identities do not make this a manifestly positive propagation.

I have not obtained relations eliminating those auxiliary minors with sufficient sign control, or a determinant inequality proving z0*z1<=0 for unbounded even degrees. For the stronger orientation observed in the frozen data, one precise sufficient inequality would be

(-1)^b D_0(n,b)>0,
(-1)^(b+1) D_1(n,b)>0,

eventually on even n with b=n/2. This is an unproved target, not a conclusion of (16)-(21). The weaker projective alternative is quantitative separation of eta from A0/A1, measured by Delta. No uniform sign law is assumed in the companion reduction or bound.

## 8. Outcome, dependencies, and remaining inputs

The two rational contractions and all three determinant identities are verified, with the original monic signs. The proposed sign condition is a valid sufficient theorem for a nonzero actual endpoint and |D_W/D_V|<=epsilon_n, including zero-coordinate cases. Every permitted frozen control passes it.

The complete companion has the exact reduced expression (7), a rational exponential companion (8), and a bound (13) through primitive high-minor coordinates. All common high-row scalar factors cancel. The actual reduced q is retained by (10). The recurrence attempt (16)-(21) is exact but does not prove the growing even sign theorem.

The remaining inputs are a uniform sign theorem or quantitative pole avoidance, adequate control of C_(n,b) or a sharper direct estimate of e+K_tail/d, adequate actual q on the same indices, and nonvanishing of the complete evaluated remainder. Neither finite sign success nor individual companion nonvanishing supplies those inputs.

Exact dependencies are GROWING_TWO_SCALAR_QUOTIENT_DRAFT.md, the actual monic system in PROOF_DRAFT.md and its preserved domain correction, the CD and second-kind identities recorded in ACTUAL_PROJECTION_REMAINDER.md, and the primitive high-minor construction in Agent 1's GROWING_DEGREE_ARITHMETIC.md. These are workspace research records. No external citation, networking, installation, or new canonical solve was used. The new mathematical evidence is restricted to the four frozen controls and is reproducible from check_two_scalar_quotient.py.
