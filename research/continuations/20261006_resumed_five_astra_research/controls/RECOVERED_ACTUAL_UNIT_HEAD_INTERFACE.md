> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Recovered actual first-head interface at p = 29

Coordinator derivation, October 6, 2026. This recovers an exact interface from an existing source; it is not a claim of a new general Lucas theorem. Independent review of its application to A2 turn 11 is requested.

The retained complete contact source, equation (6), is



$$
f_i^0=\frac{(n+i)!}{n!}J_i,\qquad
 J_i=[t^n](1+2t+2t^2)^n(1+t)^i.
$$



Here n=2001b, p=29, p divides n. All J_i are ordinary integers and the factorial ratio is the integral product of n+1 through n+i. The head input in the finite factorization is exactly f^0; the integral transform P_- is applied afterwards. This factor order is explicit in the complete source and A2 new turn 0, section 2.

For 0 <= i < p, Frobenius gives



$$
(1+2t+2t^2)^n\equiv(1+2t^p+2t^{2p})^{n/p}\pmod p.
$$



Every exponent in the first factor is a multiple of p. Since n is a multiple of p and the degree of (1+t)^i is less than p, only its constant coefficient can contribute to the coefficient of t^n. Therefore J_i = J_0 modulo p. Moreover (n+1)...(n+i) = i! modulo p. For i >= p the integral product contains n+p, so it is divisible by p regardless of J_i. Consequently



$$
\boxed{f_i^0\equiv J_0 i!\pmod p\ (0\le i<p),\qquad f_i^0\equiv0\pmod p\ (i\ge p).}
$$



Thus the entire actual unit-order sector is J_0 times the short-head sector, in the same integral coordinates. Write f^0 = J_0 h^[0] + p h^[1], with an integral remainder; neither J_0 nor the remainder is asserted to be a unit or zero. The accepted precision-p^6 first-head cutoff makes this a bounded retained head with all tail divisibility paid. Applying the integral finite normal form preserves the explicit p factor of the remainder. This closes hypothesis H in A2 turn 11 if the named finite factorization uses precisely this head, as its source states.

At the original progression u = 2 modulo 24389, A2 turn 11 would then imply the actual complete first-column saturation Z_w in p^4, and its complete norm in p^9. This implication still needs independent review of the physical digit/event argument and upper-block contraction. It does not establish exact content, the first nonzero primitive norm layer, the mixed force, an all-prime denominator estimate, or a proof about e+pi.

Primary background: classical Frobenius/Lucas arithmetic is reused within the existing Granville/Rowland-Yassawi overlap gate. Documentary source: astra_pro5_resume_20261005/controls/COMPLETE_CONTACT_FORCE_SOURCE_EXCERPT.md, equations (4)--(11); A2 new turn 0 explicitly retains the same f^0 and factor order. No old producer or residue computation is requested again.
