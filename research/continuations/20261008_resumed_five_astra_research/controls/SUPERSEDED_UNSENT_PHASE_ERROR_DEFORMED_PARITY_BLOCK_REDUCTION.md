> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# SUPERSEDED: UNSENT parent phase error; never use as a mathematical premise

# Exact deformation of the even contact blocks

Parent algebraic continuation, 9 October 2026. DIFFERENT review is
pending. No arithmetic scan, original-index array or coefficient
determinant calculation is run. This note concerns the additionally
normalized contact PARITY matrix U, not a complete integer pencil.

Before this continuation, scoped current/previous/Desktop English
MD/TEX searches for this specific Toeplitz--Kronecker reduction and
leading64/128 distinction recover no existing evaluated statement.
The exact rising divisor, F4 trace formula and joint kernel already
overlap the parent's earlier note and A2turn13(4.2)/(5.5); reuse them.
Classical Pascal tensors and finite triangular determinants are reuse.
No new external theorem is adopted. The parent joint kernel itself
is currently being independently audited in A4turn21. Results below
are conditional on that kernel until its independent audit completes.

Keep d=9^(18+32u)-1, d=2 mod3, v2(d)=4 and d=16 mod64.
Write U_q=(U_(j,r)) for j,r=0,...,q-1. Multiplication of its column
generating series by C(Y)=(1+Y+Y^2)^d preserves det(U_q) over F2.
The transformed kernel is

    Tr((1+omega^2 Y)^(2d) R(X+Y)),
    R(S)=(omega^2+omega S)/(1+omega S)^2.

The coefficient of S^s in R is omega^(s+2) for s even and omega^s
for s odd. The numerator contains only even powers of Y. Therefore
on reordering the first2m rows and columns by parity, the transformed
matrix is EXACTLY

    [[C_(m,d), A_(m,d)], [A_(m,d), 0]],                (1)

where the two cross blocks coincide: Lucas reduces both relevant
binomials to binom(h+l-v,l-v). This proves

    det(U_(2m))=det(A_(m,d))^2.                       (2)

Define, over F4,

    P_m(h,l)=binom(h+l,l) mod2,
    B_alpha=D_alpha P_m D_alpha, D_alpha=diag(alpha^h),
    T_alpha(d)=(I+alpha N_m)^d,
    N_m(h,l)=1_(l=h+1).

All these are finite m-by-m matrices. Squaring inside the trace
and expanding the numerator proves the exact cross-block identity

    A_(m,d)=Tr(omega^2 B_omega T_omega(d))
      =omega^2 B_omega T_omega(d)
        +omega B_(omega^2) T_(omega^2)(d).            (3)

Indeed, its (h,l) entry is

    Tr sum_(v=0)^l binom(d,v) binom(h+l-v,l-v)
                       omega^(2h+2l-v+1).

For m=2^a, Lucas gives the finite tensor Pascal identity and the
already derived literal digit ratio

    B_omega^(-1) B_(omega^2)=omega^(m-1) J_m,
    J_m=([[1,0],[1,1]]) tensor ... tensor ([[1,0],[1,1]]).

Since T_omega(d) is unit upper triangular, (3) has nonzero determinant
if and only if the fully evaluated finite matrix

    D_(m,d)=T_omega(d)+lambda J_m T_(omega^2)(d),
    lambda=omega^(m+1),                              (4)

has nonzero determinant. In fact

    det(A_(m,d))=omega^(2m) det(B_omega) det(D_(m,d)).

This is an exact determinant reduction with all scalars shown; it
is not a generic statement that a sum of two units is a unit.

## The actual sixteen-fold reduction

For m=16n a power of2 and d=16e, characteristic2 gives

    T_alpha,m(d)=T_alpha,n(e) tensor I_16,
    J_m=J_n tensor J_16.

Here alpha^16=alpha for alpha=omega,omega^2, and N_m^16=N_n tensor I_16.
Reorder the tensor basis so the16-coordinate is first. Because J_16
is lower triangular with diagonal1, (4) becomes a16-by-16 lower
block-triangular matrix, with identical diagonal blocks

    D_reduced=T_omega,n(e)+lambda J_n T_(omega^2),n(e).

Thus

    det(D_(m,d))=det(D_reduced)^16.                   (5)

This reduction uses the actual v2(d)=4 and retains the full e in the
finite Toeplitz exponent. It does not erase the d-dependent deformation.

## Two exact evaluations beyond the previous degree32 boundary

For q=64, m=32, n=2, the actual e is odd. Since N_2^2=0,
T_alpha,2(e)=I+alpha N_2. Also lambda=omega^33=1. Hence

    D_reduced=[[0,1],[1,omega^2]],
    det(D_reduced)=1.

Equations(2)--(5) prove the additionally normalized leading contact
block U_64 is a UNIT at EVERY original index.

For q=128, m=64, n=4, the actual d=16 mod64 implies e=1 mod4.
Since (I+alpha N_4)^4=I, T_alpha,4(e)=I+alpha N_4.
Now lambda=omega^65=omega^2, and literal matrix multiplication gives

    D_reduced=
      [[omega,   0,     0,     0],
       [omega^2, 0,     0,     0],
       [omega^2, omega, omega, 0],
       [omega^2, 1,     1,     0]].

Its last column is zero. Equations(2)--(5) prove det(U_128)=0 at
EVERY original index. No small sample or conjecture about power-of9
digits is used. Thus the earlier unit sizes2/8/32 do not extend to
all sizes2*4^a. The first actual deformation can also rescue size64,
which would be singular in the undeformed kernel.

These are statements about LEADING columns r=0,...,q-1. The singular
leading128 block does not prove that every128-column choice has
deficient rank. Alternative actual return columns may still attain
the repaired physical source payment. No general rank law for U,
optimal growing source flag, integer corrected cofactor, joint
terminal depth, all-prime G bound, primitive-error decay or e+pi
decision is asserted here. The full varying rising divisors and
both bottom corrections remain indispensable for such transfers.

The next useful task is an evaluated all-column rank/excess law or
a recursive choice of actual return columns for consecutive jet
rows, coupled to the already paid mixed-compound window. Repeated
fixed-block scans do not solve that growing physical source problem.
