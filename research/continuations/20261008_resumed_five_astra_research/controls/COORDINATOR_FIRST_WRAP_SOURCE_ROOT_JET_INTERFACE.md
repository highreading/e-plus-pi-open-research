> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact source-root jet interface for the retained first dyadic wrap

Coordinator derivation, 9 October2026. NEW parent algebraic interface;
DIFFERENT audit PENDING. It is not an injectivity or rank theorem. Scoped
current/Desktop mixed-pole/wrap searches recover the already recorded
first-wrap criterion, but no evaluated injectivity result. The present
calculation is an additional exact identity for that OPEN criterion.
Standard finite Frobenius and trace identities are REUSE, not claimed new;
the previous primary binomial/DLMF gate applies. No unread theorem is used.

## 1. Same ORIGINAL columns and degree budget

Use the complete definitions and restricted binary coefficient spaces of
COORDINATOR_FIRST_DYADIC_WRAP_MIXED_INTERFACE.md. In particular keep

    d=9^(18+32u)-1=2L+rho, L dyadic, rho even>=4,
    p>=rho+1, p+rho<=L, q=p+h>L,
    M+rho=max(p+rho,q+(q mod2))<=d/2.

ALL actual return columns are0<=r<d. No virtual r=d column is installed.
Let delta=M+rho-L=q+(q mod2)-L. Then

    1<=delta<=rho/2, M=L-rho+delta<L, M>p,
    L-M=rho-delta>0.

In F4 use a=1+omega Y, b=1+omega^2Y, coefficientwise conjugation sigma,
omega^2+omega+1=0. Keep exactly the earlier full numerators N_s,N_m and
N=N_s+N_m, with

    N_s=b^(2rho) Q a^(M-p), deg Q<=p-1,
    deg N<=M+2rho-1.

The binary trace polynomials are

    P_s=b^M N_s+a^M N_s^sigma,
    P_m=b^M N_m+a^M N_m^sigma,
    E=P_s+P_m.

The actual common mixed wrap factor remains1+Y^(2L), rather than1.
The previous EXACT null-relation criterion is

    E=Y^(2L)T, deg T<rho, T=P_m modY^rho.        (1)

Its degree sharpens to

    deg T<=2delta-1,                            (2)

because deg E<=2M+2rho-1=2L+2delta-1.
The binary polynomial T is thus bounded by distance beyond L, not by the
full rho; it is still fixed by the actual low trace, not a free target.

## 2. Exact polynomial source-root representation

For binary T satisfying(2), the FIRST equation of(1) is equivalent to

    N_s+N_m=b^(2L-M)T+a^M H,
    H in F2[Y], deg H<=2rho-1.                  (3)

Proof: Frobenius gives

    a^(2L)+b^(2L)=Y^(2L),

since omega^(2L)+omega^(4L)=1. Put C=N-b^(2L-M)T. Then the first equation
of(1) is exactly b^M C+a^M C^sigma=0. As a,b are coprime, a^M divides C.
Write C=a^M H. The zero trace becomes a^M b^M(H+H^sigma)=0, so H is
binary. Conversely a binary H makes that trace zero and proves E=Y^(2L)T.
The term b^(2L-M)T has degree at most M+2rho-1 by(2), as does N. Dividing
by a^M gives the stated degree bound. This proves(3) in both directions.

Equation(3) clears both denominators and loses no source phase. Its Q is
still in the actual source space R_(p+1), and N_m still uses exactly the
full EVEN/ODD mixed numerators, including the odd derivative.

## 3. The long dyadic factor collapses at the source root

Since b=omega^2+omega a, Frobenius gives

    b^L=omega^(2L)+omega^L a^L.

As M<L, (3) implies the EXACT root-jet congruence

    N_s+N_m=omega^(2L)b^(rho-delta)T mod a^M.    (4)

The large exponent2L-M has become rho-delta in this finite root quotient.
No original coefficient table or rho-sized numerical solve is required
to derive(4). It is a polynomial identity modulo the explicit power a^M.
Because N_s contains a^(M-p), a further necessary condition is

    N_m=omega^(2L)b^(rho-delta)T mod a^(M-p).    (5)

M-p>0 follows from p+rho<=L and delta>=1. The source numerator has not
been discarded from(4); it disappears only in the weaker quotient(5).

## 4. The original tail still supplies independent conditions

Equations(3)--(5) do NOT replace the second equation of(1). The FULL
criterion is(3) TOGETHER WITH T=P_m modY^rho. With(2), this says

    T=trunc_(0..2delta-1) P_m,
    [Y^j]P_m=0 for2delta<=j<rho.                (6)

Every one of these tail conditions comes from ORIGINAL columns2L..d-1.
Deleting them or regarding T as arbitrary would change the problem.
At delta=rho/2 the second interval is empty; smaller delta retains a
nonempty band of actual low-trace constraints.

## 5. Open evaluation target and arithmetic payment

The additional usable target is injectivity of the restricted source/mixed
coefficient map satisfying(3) and(6), perhaps first with an explicit slack
delta<=rho/4-O(log d). That slack is a proposed research range, NOT a proved
rank statement. The known q<=L proof corresponds to T=0; the higher-pole
elimination and actual source phase are reused there. For T nonzero their
evaluated interaction with(6) remains OPEN. The new identities alone do
not remove a null relation.

For cofactor attainment one must additionally retain the full factorial and
atom exclusions, BOTH strict/equality compounds and relative odd factors,
and the original scalar transfer. No original-sized calculation, old
closed auxiliary receipt, new numerical test, terminal coefficient upper,
all-prime G or primitive whole-error saving is asserted. No e+pi decision
follows from this exact interface.
