> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Reflection conventions linking the moment and endpoint calculations

Date: 2026-09-13. Root cross-note audit. This bridge makes a change of
variable explicit; it does not change the proved norm bounds.

There are two useful polynomial conventions:

    U_n(x)=sum_j B_(n,j)(1−x)^(n−j)/(n−j)!,
    P_n(t)=sum_j B_(n,j)t^(n−j)/(n−j)!=U_n(1−t).

The original raw moment equations and inverse-norm note use U_n:

    <U_n,F_k>=0 for n+1<=k<=2n−1,
    <U_n,T_n>=−4.

The endpoint-coefficient and factorial-transfer notes use P_n:

    <P_n,F_k(1−t)>=0,
    <P_n,T_n(1−t)>=−4,
    B_(n,n)=P_n(0), B_(n,n−r)=P_n^(r)(0).

It would be incorrect to identify these two high orthogonalities
without reflecting the test functions. The transfer formulas are
already derived from the reflected coefficient definition and do not
require that incorrect identification.

Let Rf(x)=f(1−x). It is unitary on L2(0,1), and

    R phi_l=(-1)^l phi_l,     RT=TR,
    R psi_l=(-1)^l psi_l.

Therefore every Legendre or T spectral projection commutes with R.
All relative norms of spectral blocks, all L1/L2 masses, and the
worst principal angles in the top-two graph question are identical
for the two conventions. Specifically the low graph matrix transforms
as G_ref=D_low G D_high, with diagonal signs (−1)^l on both blocks;
its singular values and weighted squared cofactor norm are unchanged.

The proved broad high-orthogonality concentration theorem applies
first to U_n. The identities above transfer it verbatim to P_n. This
justifies its use in raw_top_legendre_normalization.md,
raw_weaker_top_two_endpoint_criterion.md, and
raw_conditional_endpoint_scaling.md. It does not identify their signed
endpoint values; those are explicitly evaluated on P_n at0.

The endpoint functional is

    b_U(U)=sum_r (−1)^r U^(r)(1)=B_n(1),
    b_P(P)=sum_r P^(r)(0)=B_n(1).

If z_l=b_P(phi_l)>0, then b_U(phi_l)=(−1)^l z_l.
In the two-measure model with seeds v0=1 and v1=sqrt3(x−1/2), reflection
replaces the polynomial pair (f0,f1) by (f0,−f1). The original plus
high-row equations apply to U_n. For the reflected P_n pair, the odd
branch has a minus sign. The measures and squared norms stay the same.

This explicit distinction prevents an invalid spectral truncation or
an accidental odd-branch sign change from being hidden in notation.
