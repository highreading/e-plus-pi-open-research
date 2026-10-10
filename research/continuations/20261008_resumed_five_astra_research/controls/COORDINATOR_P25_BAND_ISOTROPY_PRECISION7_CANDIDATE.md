> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Candidate: one more paid actual/core matrix digit from p25 and HIGH-band isotropy

9 October2026, active parent derivation. Independent review REQUIRED.
This is a concrete candidate improvement of A4turn8's precision6 matrix
comparison. It reuses that report's exact Schur identities and one-lift
mixed bounds, the existing p25 filter, and an OLD anti-triangular inverse
isotropy theorem. It is not an accepted higher-producer theorem yet.

## Archive/literature gate and precise dependencies

Before this derivation, the parent read current A4turn8 Sections3--8,
the parent p25 bulk note, and old A1turn20 Section9.1 in the archived
6 October record. The OLD proof already gives

    (E_HIGH^-1)_(i,j)=0 mod3 when i+j>m+d.            (1)

Terminal isotropy is therefore reused, not rediscovered. The finite-band
extension below follows immediately from the same zero region. Classical
finite Jacobi, Frobenius, integral monic division and exact Schur identities
are already paid inputs; no new general literature theorem is imported.
The particular p25 whole-middle extension and precision7 propagation were
not supplied as evaluated conclusions in the checked current report.
No exhaustive absence or novelty claim is made.

Keep the SAME sufficiently large original family and all complete source
terms, physical cutoffs, actual inverse matrices, signed xi*v, q31 and
the entire degree30 reciprocal. Use A4turn8 notation, c=3^7 and
B(f,g)=M(R*f*g). The proposed conclusions are

    deltaS=S_act-S_c in3^29 on the entire middle space,
    deltaS(one,one) in3^33 on prescribed one-lift columns,
    T_act,red-T_c,red in3^7 on the common amplitude basis.  (2)

All three claims need the audit below. They concern a MATRIX before exact
endpoint adaptation; neither endpoint-difference digits nor a primitive
denominator gain are asserted.

## 1. A p25 representative for the entire middle, including its last column

Use N=3^24, L=81Q and RN=R_N(y^L). The current p22 terminal construction
is proposed to extend as follows, with the already known unit t25:

    Omega_k=y^(d+k)-sum_(u<D)binom(d+k,u)x^u=x^D*s_k,
    theta=-3/beta,
    D25=RN/(beta*t25)*sum_(k=0..24)theta^k*Omega_k.

The necessary finite claims to audit are

    Gc(W,D25)-e_Ym in3^25,
    Gc(W,x^D*p*RN)=3*t25*tau(p)*e_Ym mod3^25,
    tau(p)=[y^(nu-1)]p, deg p<nu.                    (3)

They use the SAME geometric convolution as A4turn8(3.3)--(3.6), with
one additional bounded precision range. All Omega_k*RN are in W and
below m because L>4D+2k-3. LOW nonsparse degrees are below (L-1)/2;
HIGH degrees see only the first exceptional macro moment; its final
denominator4H-L lies below4H-4D+5. These physical conditions hold for
every0<=k<=24. The uncancelled geometric term has valuation25.

Define

    Ftilde[p]=x^D*pi_p*RN,
    pi_p=p-(3*tau(p)/beta)*sum_(k=0..24)theta^k*s_k.

Then deg pi_p<=nu+24 and, IF(3) is validated,

    Ftilde[p]-F[p] in3^24 W.                         (4)

No p26 overflow is introduced. The last middle residue in(3) must be
verified rather than suppressed or borrowed from ordinary compression.

## 2. Compact norms and shortened W representatives at p25

The compact norm proof in A4turn8 Section4.1 applies to integral B0
of degree<=2D+107 with this p25 filter. Indeed, c_s=2s+1<81Q gives
v3(c_s)<=h-26 and

    v3(3^h*(1/(c_s+2qL)-1/c_s)) >=27.

Frobenius replacement costs3^25; the complete macro sum has total
coefficient sum0. Every macro term remains physical because

    2H-L+deg B0 <=2H-2D+2.

Thus the complete filtered norm lies in3^25. Full factorial and endpoint
subtraction remain in the integral functional.

Applying the original shortened-multiplier decomposition to pi_p now
gives the proposed exact representation

    h_p=B(W,F[p])=E_c*u_p+3^24*e_p,
    U_p=W*u_p=x^(D-72)*a_p(y)*RN,
    deg a_p<=nu+126.                                (5)

Here the unfiltered multiplier has degree<=d+54. Remove its HIGH terms
with monic Omega_0,...,Omega_54 and its LOW Taylor remainder, then include
the bounded terminal correction for its middle quotient. The result is
in the ACTUAL W, integral, and divisible by x^(D-72). This must be checked
as in current A4turn8(4.4)--(4.6), not assumed from a degree label.

The complete compact factors for two such U columns have degrees

    Gc(U_p,U_q): (D-144)+1+2(nu+126)=2D+107,
    B(U_p,U_q): (D-216)+72+2(nu+126)=2D+106.

Consequently both pairings are in3^25, while B(F[p],F[q]) is in3^24
by(4) and coefficientwise integrality.

## 3. Reused inverse isotropy on a fixed HIGH band supplies one missing digit

Put w_p=B(W,U_p). Mod3 the filter is1 and the complete source quotient
is x^(H-144)*q31*a_p times the actual row. Its degree before a HIGH
row y^i is at most H+nu+54. The sole unit-weight physical pole is at

    r3=(3H-1)/2=H+m+nu.

Therefore

    (w_p)_HIGH,i=0 mod3 for i<m-54.                  (6)

All LOW coordinates are divisible by3 by the same finite degree gap.
The already proved actual inverse-image criterion gives

    z_p=E_act^-1*w_p integral.

Modulo3, its HIGH part solves E_HIGH*z_HIGH=w_HIGH because the LOW
rows and LOW/HIGH couplings vanish mod3. The LOW contribution to w_p^T*z_q
vanishes. By the OLD inverse zero region(1), every HIGH pairing between
the supports in(6) vanishes whenever

    2(m-54)>m+d, equivalently m-d>108.

This holds on the sufficiently large original family. Thus

    w_p^T E_act^-1 w_q in3 Z3 for ALL original p,q.   (7)

This is the only proposed improvement over the coarse integrality bound
in A4turn8(4.9). It reuses the whole actual HIGH inverse modulo3 and
retains the LOW transport; it does not assume the full inverse is a HIGH
inverse or ignore its one-digit global cost.

## 4. Exact nonlinear Schur payment: proposed uniform deltaS in3^29

Keep the exact identity

    E_c E_act^-1 E_c
      =E_c-c*B_WW+c^2*B_WW*E_act^-1*B_WW.

On u_p,u_q from(5), the first term is in3^25, the second in3^32 and
the third in3^15 by(7). Thus their sum is in3^15. In

    deltaS(p,q)=c*B(F[p],F[q])-c^2*h_p^T E_act^-1*h_q,

the direct term is in3^31. The u/u contraction is in3^(14+15)=3^29.
Both cross errors from(5) are in3^38 since E_c E_act^-1 is integral.
The error/error term is in3^(14+48-1)=3^61. This proves the proposed
uniform3^29 in(2), IF the finite p25 representation has passed audit.

## 5. One-sided p25 substitution strengthens one/one pairing by one digit

A4turn8 independently supplies B(W,F_one) in3^25. For a one-lift middle
input p, the admissible UNCORRECTED ordinary p25 trial V[p] obeys

    V[p]-F[p] in3^24 W.

Replace only the first argument in B(F_one,F_one). Its error is now
in3^(24+25)=3^49, using the newly supplied mixed bound. The parent p25
monic quotient/remainder argument with the complete degree30 reciprocal
then gives, modulo3^31, a complete-core pairing Gc(F[p'],F_one). The
whole original middle normalization is in3^26. Hence

    B(F_one,F_one) in3^26,
    deltaS(one,one) in3^33.                          (8)

The quadratic source return in this one/one case has valuation at least
14+25+25-1=63. For a general middle direction versus one-lift, retain
the validated weaker deltaS in3^32 from A4turn8. This deduction has no
unpaid double stationary substitution or p26 overflowing input.

## 6. Proposed propagation to a precision7 returned matrix comparison

The EXACT core-prefix lift of G0 is one-lift+9*Z with integral Z.
Using(2),(8) and the general/one bound3^32 gives physical perturbations:

| Pair | Proposed precision before prefix return |
|---|---:|
| general/general |29|
| general/core-prefix-lifted G0 |31|
| lifted G0/lifted G0 |33|

The actual prefix inverse costs3^-26. Its unit normalization remains
valid because the normalized whole perturbation is in3^3. The exact
prefix Schur correction gives normalized R differences in3^3 overall,
3^5 on general/G0 and3^7 on G0/G0; the respective quadratic corrections
start at higher valuations6,8,10 after normalization.

For the entire J return, B_act-B_c is in3^2, and
(L_act-L_c)^T*G0 is in3^3. Since L_c^T*G0 is in3, set
C_alpha=L_alpha^T*G0/3. Then C_act-C_c is in3^2 and the complete
3^5*C_alpha^T*B_alpha^-1*C_alpha difference lies in3^7.

On the original rank-b complement, the normalized A_b difference is
in3, and M_b,act-M_b,c is in3^2. Both M_b are in3. Therefore the
FULL81*M_b^T*A_b^-1*M_b difference is in3^7, including the change of
the unit inverse. This yields the candidate T_act,red-T_c,red in3^7.

Common saturated unit-complement eliminations preserve this comparison:
physical core cross3^5, complement inverse3^-4, producer difference3^7
make the change of the return start at3^8 or deeper. The common radicand
matrix digits at physical3^5 AND3^6 would then agree.

## 7. The endpoint restriction still needs its own higher digits

The parent H2 reuse note closes the leading endpoint pivot. It does NOT
prove actual/core exact endpoint equality modulo9. Exact endpoint-adapted
bases can differ by3, which may change a3^5 radical matrix at3^6.
Therefore(2), even if accepted, does not automatically compare the
actual/core second digit AFTER separate exact endpoint adaptations.
That missing synchronization must be derived from complete actual
endpoint returns. Complete earlier1/3 and1/9 diagonal returns remain.

The candidate does not evaluate the critical directional inverse or
grant a growing valuation saving. Its next useful audit target is the
entire precise p25/finite-band proof above, followed by the actual higher
endpoint normalization where the chosen matrix digit requires it.
All global column contents, least clearer, ALL-prime cofactor gcd,
physical resonance and nonzero whole-error obligations are unchanged.
