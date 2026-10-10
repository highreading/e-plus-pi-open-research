> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A paid p25 bulk-producer transport, with the terminal exception retained

Coordinator derivation, 8 October 2026. This reuses the existing p<=25
mixed-projection filter, integral finite basis, actual mixed observation,
precision31 producer support, and A4turn5 Lemma2.1. It introduces no new
general filter or unbounded precision claim. The result below is a locally
derived implication of those retained theorems; independent A4 review is
still required. It does NOT evaluate the physical last-middle endpoint or
the complete J/rank-b/diagonal returns.

The scoped overlap check read the relevant old A1turn9 Sections2--4,
A1turn14 Sections1--2, current A1turn4 physical-terminal theorem and
A4turn5 Sections1--2 and7. Old precision20/21/24 support and fixed extra
mixed digits are reused. The precise p25 transport below was not supplied
as a completed theorem in that scoped material. No exhaustive archive or
literature absence claim is made; the steps are elementary finite Schur,
monic polynomial division and the already paid compression identity.

## Retained data and the exact scope

Keep the sufficiently large original indices, Q=3^(h-29), D=10Q-b,
0.064Q<b<0.073Q, nu=D/2-1, d=D+nu, and m=(H-D+1)/2.
Write x=y-1. The complete functional M is integral on the actual allowed
polynomial degree<=2n-1, with its fixed pole cutoff; the source is

    Qact=Qc+3^7 R,
    Qc=(y+1)x^A(beta+3y),
    R=(y+1)x^(A-72)q31(x) modulo3^31, deg q31<=72.

The entire reciprocal r31 has degree<=30 and
(beta+3y)r31=1 modulo3^31. All its coefficients are ternary integral.
The exact core corrections F[p] of x^D p are integral and core-orthogonal
to W. E_c^-1 is in3^-1. The retained actual mixed observation gives

    B_R(F[p],w)=M(R F[p]w) in3 Z_3 for every integral w in W.

This follows by integral linear combination from the existing mixed
observation on original columns, not from positivity. The whole Phi_R
bound is not strengthened by assertion.

Here is the NEW bulk statement to audit:

    B_R(F[p],F[q]) in3^25 Z_3

whenever p,q are integral, deg p<=nu-32 and deg q<=nu-2.
The last-middle input q=y^(nu-1) is EXCLUDED. This is a source-pairing
statement before the complete J and endpoint returns, not a claim about
the fully returned Bsharp or primitive denominator.

## 1. Use the admissible p25 trial instead of the p26 physical overflow

Let N25=3^24, L25=3^(h-25)=81Q, M25=(N25-1)/2, and

    V[p]=x^D p R_N25(y^L25).

The reused p25 filter has R_N25(0)=1. Its actual W residual is in3^25
for deg p<=nu-2, and V[p]-x^D p belongs to the actual W space. The
established degree bound is

    m-deg V[p] >= (L25-4D+7)/2 > 20Q.

In particular V[p] is physically admissible and has gap much larger than
30. The complete-core rather than pole residual has the same precision
by the already paid comparison. Applying the inverse loses one digit:

    V[p]-F[p] in3^24 W Z_3.

Therefore, using the COMPLETE mixed observation on F[q],

    B_R(F[p],F[q]) = B_R(V[p],F[q]) modulo3^25.

Only one argument is replaced. There is no unpaid stationary quadratic
substitution, and no p26 overflowing trial is needed for this step.

## 2. The actual multiplier stays inside the finite space

Set

    L[p]=x^(D-72)q31(x)r31(y)p(y)R_N25(y^L25).

Then Qc L[p]=R V[p] modulo3^31. Since D>=72, L[p] is integral.
Its degree is at most deg V[p]+30<=m, so no physical overflow is present.
Both products paired with F[q] stay inside degree<=2n-1. Hence integrality
of the complete M, including endpoint subtraction and factorial term,
gives

    B_R(V[p],F[q]) = G_c(L[p],F[q]) modulo3^31.

Do not assume p is divisible by x^72. Instead perform MONIC division in x:

    x^(D-72)q31 r31 p = x^D p' + u,
    deg p'<=deg p+30<=nu-2, deg u<D.

The remainder u is a genuine LOW polynomial. The nonconstant terms of
u R_N25(y^L25) start at degree at least L25>d. Independently of any
cancellation between quotient and remainder, their total degree is at
most D-1+(H-L25)/2, leaving physical gap

    m-deg(u R_N25) >= (L25-3D+3)/2 > 25Q.

Thus u R_N25 belongs to the original W:
its constant-filter term is LOW and all the others are actual HIGH.
Likewise the filtered x^D p' differs from x^D p' by an element of W.
Consequently

    L[p]-x^D p' in W Z_3,
    G_c(L[p],F[q]) = G_c(F[p'],F[q]) EXACTLY.

This uses the finite monic LOW/MIDDLE decomposition. It does not apply
the core compression to an inadmissible x^(D-72) input.

## 3. Pay the complete core pairing by the original small degree

A4turn5 Lemma2.1, independently checked in A1turn5, states for
deg p',deg q<=nu-2 that

    G_c(F[p'],F[q]) = K_N J_h(B) modulo3^31,
    B=x^D(beta+3y)p' q,
    J_h(B)=3^h sum_s B_s/(2s+1), K_N a ternary unit.

The polynomial B has degree at most

    D+1+2(nu-2)=2D-5 < 20Q.

Thus every denominator 2s+1 is strictly below40Q, whereas
3^(h-25)=81Q. It follows that v3(2s+1)<=h-26, and EACH complete
coefficient term in J_h(B) is in3^26. Therefore

    G_c(F[p'],F[q]) in3^26.

Combining this with the one-sided substitution error in3^25 proves the
claimed bulk bound B_R(F[p],F[q]) in3^25. No values of q31, no leading
radical support calculation, and no new pole-grid separation are needed
for THIS bound. It only uses a paid core compression on admissible inputs.

## 4. Application and the remaining terminal/return obligations

For the prescribed one-lift inputs

    p_a=x^b y^(k0+a)(y^(3Q)+3), k0=(3Q+1)/2, 0<=a<=b/2,

the largest degree is (9Q+3b+1)/2. The margin to nu-32 is

    (Q-4b-67)/2 > 0

at all sufficiently large original indices. Thus all prescribed one-lift
columns, their full exact radical combinations, and the saturated
complement combinations satisfy the deep-middle hypothesis for p.
Other ordinary input columns q of degree<=nu-2 may be paired with them.
The existing quadratic-chain term3^13 Q_chain in3^34 remains retained;
the direct source contribution on these pairs is now in3^32.

However, the actual J block reaches the exceptional last-middle input
y^(nu-1). That input is outside the reused generic compression theorem.
Its physical-terminal residual and endpoint charge are essential. The
core gamma=0 calculation is not a theorem about the actual source charge.
After J inversion and rank-b elimination, the excluded terminal channel
can still return at the relevant normalized digit. The actual1/9 diagonal
channel also remains open. The direct bulk bound by itself does NOT prove
Delta_GG=Delta_bG=0 for the fully returned matrices, identify the returned
endpoint, or establish a favorable Bsharp direction.

The useful next task is therefore precise: independently audit the bulk
transport, then evaluate the ONE remaining actual source pairing with
F[y^(nu-1)] and carry it through the exact physical J/endpoint/diagonal
returns. The earlier p26 terminal theorem and exact R(-1), signed xi*v
and source force remain available. This may simplify the producer problem;
it does not close the rationality question or the all-prime normalization.

## 5. A concrete terminal extension to check independently

The exclusion above is needed for the reused modulo3^31 compression.
At the weaker precision3^25 there is a specific way to include the last
middle input, PROVIDED its actual filtered residual is in3. This weaker
residual is consistent with the paid p25 macro moment: only the top HIGH
row can reach the exceptional exponent n_*=(H-1)/2, with coefficient3;
the resulting residual is 3*t25*e_(Y_m) modulo3^25. The derivation must
retain the physical cutoff and complete-core/pole comparison. It may
also be checked from the existing complete column jet and R_N25=1 mod3.
The parent does not silently apply the ordinary3^25 residual to this row.

Here is the rest of the extension, conditional on that actual residual:
put q=y^(nu-1), V[q]=x^D q R_N25(y^L25). This trial is finite, with gap
(L25-4D+5)/2>0. For the ordinary p' above, r_(p') is in3^25 and r_q is
in3. Hence the exact stationary Schur correction is in3^25:

    r_(p')^T E_c^-1 r_q in3^(25-1+1)=3^25.

The RAW filtered pairing is also in3^25 by an elementary pole-support
argument, without the stronger generic compression theorem. Its pole
polynomial is

    x^H B(y) R_N25(y^L25)^2,
    B=x^D(beta+3y)p' q, deg B<=2D-4 <(L25-1)/2.

The already paid Frobenius congruence makes x^H R_N25^2 a polynomial in
y^L25 modulo3^25. Any physical pole surviving this modulus has
v3(2v+1)>=h-24, so its coefficient index satisfies

    v=(L25-1)/2 modulo L25.

The small B support misses that residue. Every surviving extraction is
zero. The fixed cutoff is retained; the full factorial contribution is
in3^h, beyond this precision. Thus

    G_c(V[p'],V[q]) in3^25,
    G_c(F[p'],F[q]) in3^25.

The same one-sided ACTUAL producer transport then gives
B_R(F[p],F[y^(nu-1)]) in3^25. This would include all original middle
inputs in the direct bulk bound. It still does NOT dispose of complete
prefix/J/endpoint/diagonal returns: changes in an eliminated block's
inverse can return even when the direct selected source pairing is deep.
Evaluate those terms explicitly rather than replacing the actual returned
endpoint with the unreturned core or interpreting this as a q saving.
