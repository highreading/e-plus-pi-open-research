> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact first-wrap interface beyond the dyadic mixed window

Coordinator derivation, 9 October 2026. NEW interface only; its injectivity
and useful complete-cofactor extension are OPEN. DIFFERENT review PENDING.
This does not alter the admitted h<=rho-1 note or the separate UNSENT q<=L
proof. Scoped current/prior/Desktop mixed-pole searches recover those notes,
the earlier weighted-stack barriers and A4turn23's two-return theorem;
no larger mixed-wrap theorem is recovered in that scope. Ordinary binomial
Frobenius, trace and existing finite Cauchy identities are REUSE. No unread
primary theorem is imported or claimed to prove injectivity.

## 1. Actual original columns and expanded cutoff

Keep d=9^(18+32u)-1=2L+rho, dyadic L, rho even>=4, p>=rho+1,
p+rho<=L. The common return columns remain EXACTLY0<=r<d; the virtual
r=d column is not installed. Set q=p+h, V_z=U_p(z) for0<=z<h. Let M be
the maximum of p and the a-pole orders from the full mixed kernel:

    p EVEN: n_(2v)=n_(2v+1)=p+2v+2-rho;
    p ODD:  n_(2v)=p+2v-rho, n_(2v+1)=p+2v+3-rho.

Assume the precise finite degree cutoff

    M+rho=max(p+rho,q+(q mod2))<=d/2.               (1)

For a complete attainment application also retain alpha-2>4q and
d-2q+1-2m>0. Thus one should keep logarithmic slack below d/2, rather
than assigning a mixed unit at the equality where corrections can enter.

## 2. The previously invisible wrap is common to ALL mixed rows

Put a=1+omega Y, b=1+omega^2Y in F4, Tr coefficientwise. On the first d
original return coordinates apply the SAME unit convolution C_d=(ab)^d.
It is invertible moduloY^d. For a source row the full formula is

    Tr(b^(2d)*Q/a^p), deg Q<=p-1,

with the actual binary source restrictions. Since2d=4L+2rho and4L>d,
b^(2d)=b^(2rho) modY^d. This source simplification is still valid.

For a mixed row, the original a,b exponents have exactly one common2L
factor. After extracting it, its reduced rational numerator/pole is the
one in the q<=L note, multiplied by

    g(Y)=(ab)^(2L)=1+Y^(2L)+Y^(4L)
                   =1+Y^(2L) modY^d.              (2)

The equality uses Frobenius, and2L<d<4L. Thus the mixed rows share g,
while source rows do not. Deleting g beyond the first2L coordinates is
invalid. Conjugation fixes g, so it may pass through the trace.

## 3. All explicit reduced numerators

At denominator a^M, the source numerator is

    N_s=b^(2rho)Q a^(M-p).

The reduced mixed numerator N_m is a binary linear combination of:

    p EVEN, z=2v:
      omega^(2p+2v+1)b^(rho+p+1)a^(M-n_z);
    p EVEN, z=2v+1:
      omega^(2p+2v)b^(rho+p)a^(M-n_z);
    p ODD, z=2v:
      omega^(2p+2v)b^(rho+p-1)a^(M-n_z);
    p ODD, z=2v+1:
      omega^(2p+2v)b^(rho+p-1)Y(1+Y)a^(M-n_z).

These are POLYNOMIALS: M>=n_z. The full odd derivative is retained in
the higher odd row formula. Their degrees and the source degree are
at mostM+2rho-1. Define binary trace polynomials

    P_s=b^M N_s+a^M N_s^sigma,
    P_m=b^M N_m+a^M N_m^sigma,
    E=P_s+P_m.

Every one has degree<=2M+2rho-1<=d-1 by(1). Both denominators have been
cleared, with conjugation fixing Y, so no denominator or scalar is lost.

## 4. Exact finite null-relation criterion

An actual relation between R_(p+1) and the mixed V rows on0<=r<d is
equivalent to

    P_s+(1+Y^(2L))P_m=0 modY^d.                  (3)

The first2L coefficients of(3) say E is divisible byY^(2L). Since
deg E<d, write E=Y^(2L)T, with deg T<rho. The remaining rho coefficients
are precisely

    T+P_m=0 modY^rho.                            (4)

Therefore the COMPLETE criterion is

    E=Y^(2L)T, degT<rho,
    T=P_m modY^rho.                              (5)

This equivalence is exact and retains every actual return coordinate.
It does not assert that only the zero binary coefficient vector satisfies
(5). T is not free: its coefficients are paid by the actual low-Y trace
of the mixed numerator. The first2L rank criterion alone does not evaluate
this new tail coupling.

When the old degree cutoff M+rho<=L holds, degE<2L forcesT=0; the earlier
pole/source-phase argument excludes nonzero relations already on the
first2L coordinates. For q>L the nonzero small T is the new obligation.
The last rho ORIGINAL columns may eliminate those relations, but this
must be proved in the original restricted source/mixed binary spaces.

## 5. Open research target and normalization

Prove injectivity of(5) for an explicit useful original subfamily and
q up to d/2-O(log d), or identify an exact original rank obstruction.
A numerical generic matrix or an auxiliary example is not an original
counterexample. A reduced small-polynomial representation is not a
proof merely because rho is less than d; rho still grows linearly.
No rho-sized solve or original-sized coefficient table is proposed.

If injectivity holds, the previously independently passed complete
Cauchy-Newton-source-adjugate prefactors and exact Pascal tie sum give
the corresponding ORIGINAL-column cofactor attainment, provided all
factorial and atom exclusions are paid. Odd mu, both full coefficient
borders and exact scalar transfer remain. This interface supplies no
full terminal valuation upper, no other odd-prime control, no all-prime
final G or primitive whole-error decay, and no e+pi decision.
