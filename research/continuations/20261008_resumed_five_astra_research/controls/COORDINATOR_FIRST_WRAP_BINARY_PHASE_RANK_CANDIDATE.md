> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Binary phase excludes the first-wrap tail on an infinite original subfamily

Coordinator derivation, 9 October2026. NEW parent rank/cofactor proof
candidate; DIFFERENT audit PENDING. This strengthens the previously OPEN
first-wrap interface. It is not a whole terminal valuation upper or an
irrationality proof. No new numerical computation is used.

Before this derivation, scoped Desktop/current MD/TEX/TXT searches for
the mixed first-wrap phase and omega^(M-2) recover only the previous OPEN
interfaces. Broader L/mod3 matches are inspected and concern unrelated
ternary LOW or producer congruences. Primary arXiv exact finite-trace/
mixed-Hankel and binomial-four-phase searches find no matching theorem.
This is a scoped applicability check, not exhaustive novelty. Classical
finite Frobenius/trace/polynomial identities are REUSE. FULL A2turn15
DIFFERENT-passes the prior source space, full mixed kernel, coupled rank
through q=L, complete relative odd factors and strict/equality compounds.
Those statements are reused at their stated finite scopes.

## 1. Retained original objects and precise new range

Keep EXACT ORIGINAL d=9^(18+32u)-1=2L+rho, L dyadic, rho even>=4,
p>=rho+1, p+rho<=L; for odd p retain p+rho+1<=L. Use all and only the
original return columns0<=r<d. The source space R_(p+1) has dimension p,
with its original binary coefficient restrictions. Put V_z=U_p(z),
z=0..h-1, q=p+h>L, and

    M+rho=max(p+rho,q+(q mod2)),
    delta=M+rho-L=q+(q mod2)-L.

Impose the NEW actual conditions

    L=2 mod3,
    1<=delta<=rho/2,
    delta<=L-rho-p.                              (1)

Then M=L-rho+delta<L, M>p, and

    K=M-p>=2delta.                               (2)

The new proposed rank theorem is

    rank_F2 [R_(p+1);V_0;...;V_(h-1)]=q           (3)

on the first d ORIGINAL columns. The new dyadic phase restriction is
essential to the argument below; the other dyadic phase is not claimed.

## 2. Exact previous first-wrap criterion, including the original tail

In F4 let omega^2+omega+1=0, a=1+omega Y, b=1+omega^2Y, sigma conjugation.
Apply the SAME unit convolution (ab)^d to every row modulo Y^d. The source
has full numerator

    N_s=b^(2rho)Q a^(M-p), deg Q<=p-1,

with the actual source restrictions. The mixed numerator N_m is the
binary combination of these complete polynomial terms:

    EVEN p, z=2v:
      omega^(2p+2v+1)b^(rho+p+1)a^(M-p-2v-2+rho);
    EVEN p, z=2v+1:
      omega^(2p+2v)b^(rho+p)a^(M-p-2v-2+rho);
    ODD p, z=2v:
      omega^(2p+2v)b^(rho+p-1)a^(M-p-2v+rho);
    ODD p, z=2v+1:
      omega^(2p+2v)b^(rho+p-1)Y(1+Y)a^(M-p-2v-3+rho).

All displayed a exponents are NONNEGATIVE by the definition of M.
The common mixed wrap is1+Y^(2L); source rows do not have this factor.
Set N=N_s+N_m and

    P_m=b^M N_m+a^M N_m^sigma,
    E=b^M N+a^M N^sigma.

The previous exact actual null-relation criterion is

    E=Y^(2L)T, T=P_m modY^rho,
    T in F2[Y], deg T<=2delta-1.                 (4)

It retains the final rho original columns, not merely the first2L.
The companion source-root interface proves from(4)

    N_s+N_m=b^(2L-M)T+a^M H0,
    H0 in F2[Y], deg H0<=2rho-1.

Modulo a^M, Frobenius replaces b^(2L-M) by omega^(2L)b^(rho-delta).
Because N_s is divisible by a^K, every null relation therefore satisfies

    N_m=omega^(2L)b^(rho-delta)T mod a^K.        (5)

Only this NECESSARY consequence of the COMPLETE criterion is used to
force T=0; the original tail equation is not discarded or made free.

## 3. New uniform binary-polynomial form of the full mixed numerator

Set z=Y+omega^2. Then

    a=omega z, b=omega^2(z+1),
    Y(1+Y)=z^2+z+1.

Let epsilon=0 for even p and epsilon=1 for odd p. EVERY full mixed
combination has the EXACT factorization

    N_m=omega^(M-2)(z+1)^(rho+p-epsilon) H(z),
    H in F2[z].                                 (6)

Here H need not be arbitrary; the statement only uses that all its
coefficients are binary, with the actual mixed bits retained.

To verify(6) term by term, write the relevant a exponent as e>=0.
For even p, the even row's scalar exponent after substituting a,b is

    2p+2v+1+2(rho+p+1)+e=M+3p+3rho+1,

which equals M-2 modulo3. Its binary polynomial is(z+1)z^e after
factoring the common(z+1)^(rho+p). The odd row scalar exponent is

    2p+2v+2(rho+p)+e=M+3p+3rho-2,

with remaining binary polynomial z^e.

For odd p, the even row gives M+3p+3rho-2 and binary z^e. The odd
row gives M+3p+3rho-5, the SAME phase modulo3, and binary
(z^2+z+1)z^e. This explicitly keeps the full odd derivative term.
Thus all rows and any last unpaired row share the claimed phase.
No paired-basis completeness or generic-rank assumption is needed.

## 4. The new phase forces the complete tail to vanish

Substitute(6) into(5), divide the unit(z+1)^(rho-delta) and the actual
omega phase, and replace a^K by its unit multiple z^K. The result is

    (z+1)^(p+delta-epsilon) H(z)
       =omega^(L+2)T(z+omega^2) mod z^K.          (7)

The exponent on the left is nonnegative and that side is binary.
The scalar exponent on the right is obtained EXACTLY as

    2L+2rho-2delta-(M-2)
       =L+3rho-3delta+2=L+2 mod3.

Under L=2 mod3 this scalar is omega. By(2),(4), deg T<K. If T is
nonzero, its highest coefficient is1, since T is binary. Translating
Y to z+omega^2 preserves this leading coefficient; multiplying by
omega changes it to omega, which is outside F2. Since its degree is
below K, truncation cannot remove that nonbinary coefficient. This
contradicts the binary left side of(7). Hence

    T=0.                                        (8)

This is an exact finite phase obstruction, not a numerical assumption
about a unit minor or an extrapolation of the q<=L rank theorem.
For L=1 mod3 the scalar in(7) is1 and this argument does not force
T=0; that case remains outside the new theorem.

## 5. Exact high-pole elimination now closes the null relation

With(8), the COMPLETE criterion(4) gives E=0 as a polynomial identity.
Thus the rational function Tr(N/a^M) is identically zero. At the root
of a, its conjugate is regular, so all negative Laurent coefficients
must vanish. The already passed higher-pole elimination is now valid
without a cleared-degree cutoff q<=L: E=0 was established directly.

For even p a new pair beyond z>=rho has common pole order n>p.
Exactly one nonzero bit leaves its highest pole; both bits leave
the pole n-1, because omega*b+1=omega^2*a. All preceding pairs
have order at most n-2 and source poles are at most p. Descend
from the highest pair; a last unpaired row is handled identically.
All such bits vanish, and the passed even small-window/source-phase
argument eliminates the remainder.

For odd p the pole orders beyond the old small window are distinct
above p, so those bits vanish from highest order down. The remaining
critical even row z=rho has pole p. Its root coefficient divided by
the actual allowed constant source phase is omega^(-L), outside F2
for any dyadic L. Its bit and the new source constant vanish. The
passed old odd small-window argument eliminates every other bit.

The original source space is independent. Thus the only actual
binary relation is zero, proving the parent candidate(3).
The complete original tail was used through(4); no r=d column,
infinite inverse, or virtual moment is added.

## 6. Complete cofactor attainment and a useful infinite window

For a common-cofactor application retain the ACTUAL minimizing count
p=s-1, s=min{r>=2:D_r>=L_d}, full relative odd factors, actual source
and adjugate divisors, and BOTH strict/equality compounds from the
passed A2turn15 proof. Additionally retain

    alpha-2>4q, d-2q+1-2m_d>0.                  (9)

In a strict crossing, (3) implies the actual leading stack
[R_p;V_0;...;V_(h-1)] has rank q-1, so some q-1 ORIGINAL returns
give a unit leading determinant and attain the nominal F_q(p).
At D_(p+1)=L_d the two complete tied sectors give the passed exact
Pascal sum

    det[R_p;V_(h-1)+v_new;
                V_0+V_1;...;V_(h-2)+V_(h-1)].

The change of mixed rows is unit triangular. Equation(3) keeps v_new
outside R_p+span(V), so the COMPLETE tied sum has rank q-1 too.
No isolated tied summand is substituted for the aggregate. All odd
units and both original coefficient borders are preserved as in the
passed normalization; no integral W descent is asserted.

On the original interval(9/8)2^a<k<(7/6)2^a, k=d+1, L=2^(a-1),
retain ONLY even a. The original logarithmic rotation is dense modulo2:
(18+32u)log_2(9) has irrational step modulo2. Hence the same open
interval with even a contains infinitely many ORIGINAL u. Then

    L=2 mod3, L/4-1<rho<L/3-1,
    p=d/4+O(log d).

Define the exact integer bound

    B=min(floor(rho/4), L-rho-p),
    q_max=L+2floor(B/2).                         (10)

For sufficiently large original tuples B has positive linear size.
EVERY q<=q_max satisfies the first-wrap bound(1) when q>L; odd q
costs its actual extra1 in delta and still fits the even q_max.
For q<=L reuse the passed theorem. Because delta<=rho/4, the
original valuation bounds give

    alpha-2-4q>=rho-s_2(d)-2>0,
    d-2q+1-2m_d>=rho/2+1-2m_d>0.

Thus(9) pays all factorial/atom competitors on this NEW window.
As p=d/4+O(log d) and rho<L/3, (10) equals

    q_max=L+rho/4+O(log d),
    q_max/d between13/28 and17/36, up toO(log d/d).

This extends the prior q<=L window, whose L/d was between3/7 and4/9.
All actual returns have r<d, jet orders<=q-1<d and the original
physical successor moment bound3d+1 remains. No auxiliary construction
or independently chosen d replaces the original infinite family.

### 6.1 A narrower infinite subfamily reaches the half-size boundary

The same proof has a stronger useful application, without a new rank
argument. Restrict the original interval further to

    (9/8)2^a<k<(17/15)2^a, with a EVEN.           (11)

This is a nonempty open interval in the SAME irrational rotation modulo2,
so infinitely many ORIGINAL indices remain. It gives

    L/4-1<rho<4L/15-1,
    p=L/2+rho/4+O(m_d).

Consequently

    L-rho-p-rho/2
       =L/2-7rho/4+O(m_d)
       >L/30+O(m_d)>0

for sufficiently large tuples. Thus delta<=rho/2 automatically pays
the SECOND bound in(1) on this narrower subfamily.

Define

    q_half=d/2-m_d-1.                            (12)

The original d is even. For EVERY p+1<=q<=q_half the actual rounded
q+(q mod2) is at most d/2-m_d; hence when q>L,
delta<=rho/2-m_d<rho/2. Equations(1)--(3) apply. Below q=L the
passed previous theorem still applies. ALL factorial/atom competitors
are explicitly paid by the original EXACT alpha=2d-s_2(d):

    alpha-2-4q >=4m_d+2-s_2(d)>0,
    d-2q+1-2m_d>=3>0.                            (13)

Therefore the same full strict/equality cofactor argument now attains
F_q(p) for EVERY q<=q_half in its stated q>=p+1 range, keeping all
original returns, odd factors and both borders. In particular

    q_half/d=1/2-O(log d/d).                      (14)

The boundary log-slack is paid rather than replaced by equality: nothing
here claims attainment at q=d/2 or at full terminal size d+2. The new
application is valid on(11), not on every tuple of the wider interval.
It is still individual complete-cofactor existence, not a nested corrected
elimination flag or an unconditional terminal/primitive-error upper bound.

## 7. Review and remaining limits

Equations(6)--(8) are the NEW proof step. The exact first-wrap/root-jet
interfaces themselves still need DIFFERENT audit with this proof, as do
the complete new range and scalar/cofactor transfer. All previous closed
auxiliary mixed/wrap receipts are REUSE; none is rerun or promoted to an
original-family proof. The newly restricted dyadic phase is preserved.

This gives individual complete cofactor existence on an infinite original
subfamily if the proof survives. It does not produce a nested elimination
flag, full paired terminal upper, other-prime content theorem, least
simultaneous clearer, ALL-prime G or primitive whole-error decay. The
literal constant border -f+4rho is unchanged. The true ternary full
kernel/force/mod9/physical7 and binary higher terminal digits remain
separate OPEN obligations. No e+pi decision or closeout is asserted.
