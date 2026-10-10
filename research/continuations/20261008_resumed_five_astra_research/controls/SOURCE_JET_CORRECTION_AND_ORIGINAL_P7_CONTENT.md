> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Source-coordinate correction and actual original7-adic content

Coordinator correction,8 October2026. All original admitted requests and
old receipts are preserved. The withdrawal manifest lists exact affected
files and pre-correction hashes. This is a parent mathematical sign error,
not evidence of prompt injection or a malicious transport response.

## Precise sign correction

The actual source is

    eta(Q)=int_(-infinity)^1 e^(t-1)Q(t)dt.

Set x=1-t. Then

    eta(Q)=int_0^infinity e^(-x)Q(1-x)dx
          =sum_r [x^r]Q(1-x)*r!.

The weights are POSITIVE r!. The old source-jet scripts incorrectly used
another(-1)^r, despite the variable substitution already changing the
polynomial coefficient signs. They therefore evaluated a different
functional. In particular, for H=t(1-t)(1+t^2)^2, the correct source is
eta(H)=-332, while the erroneous weighting gives-1732.

The independent seed checks are eta(C_0)=1,eta(C_1)=-1,eta(C_2)=9. All new
v2 scripts check these small coordinate identities and eta(H)=-332.
The closed N3..12 and N13..80 calculations use direct t moments
eta(t^j)=1-j*eta(t^(j-1)), not the erroneous x weights. Their source
normalization and selected actual-c outliers are unaffected by this bug.

WITHDRAWN: all numeric source/U/V/c conclusions in the old original-source
jets, their summary, the old five missing jets, the old first/complete
period receipts, and both old source-period/fixed-prime-exclusion notes.
In particular the asserted all-original7/11 exclusion is withdrawn.
Gaussian evaluation periods themselves do not use source weights, but
none of the old source tables is accepted merely because its Gaussian
columns happen to be correct. A3turn5 and A5turn6 received old material;
their next packet must receive this explicit correction and v2 evidence.

## Correct complete U periods

The coefficient periodicity proof still applies after replacing the weights:
every retained coefficient of T_n(1-2x), r<p, has N period p^2 modulo p,
by the integer binomial formula and Vandermonde. The COMPLETE actual U
cycles now give:

| p | original u period | classes where actual U=0 modulo p |
| --- | --- | --- |
| 7 | 21 | 9,13,17 |
| 11 | 5 | 2 |
| 13 | 39 | 23,27 |

These tables are in signed_chebyshev_first_source_period_certificate_v2.
They do not by themselves determine c=gcd(U,(I-d^2)/g_B^2).

## Correct original local calculations

The corrected24 original source pairs,u0..7,p7/11/13, still give v_p(c)=0
at all24 pairs. Their actual U/V residues and some source depths change.
For example U is divisible by11 at u2 and u7; V' is a unit, so c remains
a unit there. The false inference that U itself is always a unit is removed.

Five NEW correct source jets cover the first actual U-zero classes at7/13:

| u | p | v_p(g_B) | v_p(U) | v_p(I-d^2) | exact v_p(c) |
| --- | --- | --- | --- | --- | --- |
| 9 | 7 | 1 | 1 | 2 | 0 |
| 13 | 7 | 1 | 1 | 3 | 1 |
| 17 | 7 | 1 | 1 | 3 | 1 |
| 23 | 13 | 0 | 1 | 0 | 0 |
| 27 | 13 | 0 | 1 | 0 | 0 |

Each coefficient recurrence divides EXACT integers before modular reduction.
Tail factorials vanish at the declared precision. The g_B^2 division costs
two p-adic digits at the7 cases. The actual first two7-adic factors in c
are proved at gigantic ORIGINAL indices by bounded jets, not auxiliary N.
Therefore c=4 on the entire prescribed original sequence is FALSE.
No full integer c, least lambda, final G or primitive q is computed here.

## A short INFINITE divisibility theorem at7, subject to independent audit

For z=-1+2i, the actual Chebyshev transfer T=[[2z,-1],[1,0]] satisfies
T^24=I modulo7. This explicit bounded identity is in the complete Gaussian
period receipt. Consequently T^168=I modulo49, by the finite expansion
(I+7A)^7=I modulo49. Every original N is9 modulo24, while N modulo49
cycles with u period21. Thus BOTH adjacent Gaussian values modulo49 and
all modulo7 polynomial source jets return after21 original u steps.

At zero-U classes13 and17, b_N,b_(N-1) have common7-adic depth exactly1.
Let B_tilde=B/7,d_tilde=d/7. Then

    (I-d^2)/49 mod7 = eta(B_tilde^2)-d_tilde^2 mod7.

Only jet degrees0..6 contribute, with positive factorial weights. These
depend only on N modulo49 and the divided Gaussian values modulo7.
The corrected values at u13,u17 are BOTH0 modulo7. Hence V' is divisible
by7 in every corresponding original21-step class. The g_B/7 factor is a
unit, so replacing49 by the ACTUAL g_B^2 preserves this divisibility.

At u9 the corrected value is271=5 modulo7 and V' is a unit. All remaining
classes have U a unit. Therefore the exact infinite first-digit statement is

    7 divides actual c_N  IF AND ONLY IF  u=13 or17 modulo21.

Only the divisibility statement is uniform here. The depth equals1 at the
two computed first representatives, but deeper uniform valuations require
more precision and are not inferred. This proves infinitely many original
counterexamples to c_N=4. It does NOT imply that c has factorial size.

## Current proof status and next task

A5turn6's independent all-prime theorem is based on the correct source
recurrence and eta(H)=-332; it explicitly does not derive its proof from
the24 supplied jets. Its proposed bound c<2^(15N)*N^(N+15) is being audited.
It reaches the critical N log N scale, not the strict saving needed to
retire the signed family. The new7-adic theorem is compatible with that
bound and does not decide e+pi. No ALL-prime quantitative saving, primitive
whole-error decay or global rationality proof is accepted from these jets.
