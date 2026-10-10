> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual b=2 numerator normalization and odd-prime transfer

Status: proved deductions from the supplied, reviewed endpoint formulas; not independently reviewed. The saved certificate.json records successful exact checks; the boundary correction is documented separately in CORRECTION_NOTE.md. Scope: n>=2 and Dcal_n!=0 whenever the actual quotient or q_n is used.

## Definitions and exact normalization

Use precisely H_k(x)=k![z^k]exp(xz)(1-z+z^2/2)^k, H_k=H_k(1), J_k=kH_k+H'_k(1), and K_k=k(k-1)H_k+2kH'_k(1)+H''_k(1). This K is the b=2 second derivative, NOT the b=1 quantity J_k/k.

Put P_k=L_k(1), with L_k(t)=2^k i^k Leg_k(-i(2t-1)), and let w_k be the source's rational second-kind integral. Retain

S=J_(n+1)^2-H_(n+1)K_(n+1),
C=(J_(n+1)-H_(n+1))J_n-(K_(n+1)-J_(n+1))H_n,
W=J_(n+1)J_n-K_(n+1)H_n,
Dcal_n=(n+1)^2 P_(n+1) C-2P_n S.

Let a_s(k)=[z^s](1-z+z^2/2)^k, D_j=j! sum_(h=0)^j 1/h!, and (n)_s denote a falling factorial. Define the dyadically integral contractions

Acal_n=sum_(s=0)^n (n)_s a_s(n) D_(2n-s),
Bcal_n=2D_(2n+1)+sum_(s=1)^(n+1) (n)_(s-1)(2n+2-s)a_s(n+1)D_(2n+1-s).

For f=2^n/(n!)^2, Rodrigues gives T_P=f Acal_n and T_U=2f Bcal_n/(n+1). Substitution into the reviewed b=2 numerator gives the EXACT rational identity

Xcal_n=Qpart2_n+2f V_n,
Qpart2_n=2w_n S-(n+1)^2 w_(n+1) C,
V_n=S Acal_n-(n+1)C Bcal_n-H_(n+1)W.

Indeed its three exponential terms become respectively 2f S Acal_n, -2f(n+1)C Bcal_n, and -2f H_(n+1)W. This verifies every scalar and sign without replacing the actual numerator. The actual quotient remains Xcal_n/Dcal_n.

All H,J,K,S,C,W,Dcal are integers, and Acal,Bcal,V belong to Z[1/2]. Thus V is integral at every odd prime. A useful factorial normalization is

(n!)^2 Xcal_n/2^(n+1)=V_n+(n!)^2 Qpart2_n/2^(n+1).

## All-index odd-prime transfer: proof

Fix an odd prime p and r=n mod p in {0,...,p-1}. Scalar seeds at n=0,1 are legitimate finite expressions, independently of the HP degree scope.

For every k>=0 and d=0,1,2,

H_k^(d)(1)=sum_(s=0)^(k-d) (k)_(s+d) a_s(k),

with an empty sum equal to zero. If t=k mod p, terms with s+d>t contain a factor p. For the remaining terms s<p, Frobenius implies a_s(k)=a_s(t) mod p, and the falling factorial reduces as well. Hence H_k^(d)(1)=H_t^(d)(1) mod p. This proof also covers d>t and k<d. Multiplication by k and k(k-1) proves transfer of J and K.

For Acal, only s<=r survive. Frobenius transfers a_s and the falling factorial. The recurrence D_j=jD_(j-1)+1, D_0=1, proves D_j=D_(j mod p) mod p, so the D factor transfers too.

For Bcal when r<=p-2, only s<=r+1<p survive, and every factor transfers to its r counterpart. When r=p-1, all s>=p+1 vanish through (n)_(s-1); for 1<=s<p the coefficient a_s(n+1) vanishes by Frobenius; at s=p the factor 2n+2-s vanishes. Only 2D_(2n+1) remains. Exactly the same cancellation occurs at seed r=p-1. No division by n+1 is used locally.

Consequently the ENTIRE tuple

(H_n,J_n,H_(n+1),J_(n+1),K_(n+1),Acal_n,Bcal_n,S_n,C_n,W_n,V_n)

is congruent modulo p to the tuple at seed r. For the adjacent state at r=p-1, compare both states with k=0 using the derivative transfer above. This proves periodicity, rather than assuming adjacent indices avoid the block boundary.

## Second-kind separation, without an endpoint-gcd gate

The quotient (L_k(t)-L_k(1))/(t-1) has integer coefficients and degree at most k-1. The source functional has moments

L(t^j)=2^(-j) sum_(even h<=j) binom(j,h)(-1)^(h/2) 2/(h+1).

For odd p these moments have valuation at least -floor(log_p(j+1)). Therefore v_p(w_k)>=-floor(log_p k) for k>=1, directly from the integral definition. It follows that

v_p(Qpart2_n)>=-floor(log_p(n+1)).

For n>=p, 2v_p(n!)>floor(log_p(n+1)). To prove this, let a be the floor. If a=1, v_p(n!)>=1. If a>=2, n>=p^a-1, so 2v_p(n!)>=2(p^(a-1)-1)>a for every odd p.

Thus the factorial-normalized second-kind term is in p Z_(p). This bound includes the full second-kind part; no convolution identity or Legendre-unit assumption is needed.

## Conditional-on-seed theorem for the actual reduced q

Let p be odd, n>=p, r=n mod p, Dcal_n!=0, and V_r!=0 mod p. Then

v_p(Xcal_n)=-2v_p(n!),
v_p(q_n)=2v_p(n!)+v_p(Dcal_n)>=2v_p(n!).

Proof: transfer makes V_n a unit, while the normalized second-kind part vanishes modulo p. The numerator valuation follows by strict separation. Since Dcal_n is an integer, exact rational reduction gives the displayed q valuation, including all endpoint cancellation. In particular, a nonunit Dcal strengthens this conclusion; it is not an excluded degeneracy.

More generally, if t=v_p(V_n)<infinity and 2v_p(n!)-t>floor(log_p(n+1)), then

v_p(q_n)=max(0,2v_p(n!)+v_p(Dcal_n)-t).

This is a conditional higher-depth criterion, not a bound for t.

## Boundary and degeneracies

At r=p-1, H_(n+1)=1 and J_(n+1)=K_(n+1)=0 mod p. Hence S=W=0 and C=-J_n mod p; C need not vanish. Since n+1=0 mod p, the term (n+1)C Bcal_n vanishes, so V=0 mod p. Likewise (n+1)^2 P_(n+1)C vanishes and S=0, giving Dcal_n=0 mod p. These conclusions do not require C=0. The unit-seed theorem NEVER applies to this residue. Its higher-depth behavior is unresolved here.

At the finite seeds r=0 and r=1, exact evaluation gives respectively (S,C,W,Acal,Bcal,V)=(1,-1,-2,1,3,4) and (4,-1,0,3,10,32). Thus both residues are good for every odd prime. These are scalar algebra evaluations, not a degree scan. Consequently the theorem already gives a lower bound for n=0 or 1 mod p, subject to n>=p and Dcal_n!=0.

For any other r with V_r=0 mod p, no numerator-depth upper bound is claimed. Simultaneous or individual zeros among H,J,K,S,C,W,Acal,Bcal require no divisions and are encompassed by the polynomial seed formula. If V_n=0 exactly, its factorial contribution is absent and only Qpart2 remains. If Dcal_n=0, the quotient and q statements do not apply. If n<p, strict separation is not asserted, even if a seed is a unit. In particular n=p-1 is outside the theorem's n>=p range as well as inside its zero-seed set.

The supplied contiguous note reports a passed cancellation theorem at n=p-1 saying p does not divide actual q. Its underlying proof was NOT inspected: the attempted search was refused with a symbolic-link safety error, and no alternate access was attempted. The present boundary calculation is consistent with that report but does not reprove it. No universal prime bound is asserted.

## Scope and next lemma

The reviewed maximal-minor endpoint-gcd theorem and cubic refinements retain p>2n+4; none is used above. Fixed-b error estimates are inherited and not reproved. This is not a solution of e+pi or a global growth/shrinking theorem.

Next attainable lemma: obtain a controlled first nonzero p-adic expansion of the COMPLETE V and Dcal at n=-1 mod p, retaining both contractions and the second-kind separation threshold. A mod-p calculation of H,J alone cannot supply it. Other zero seeds likewise require a valuation lift, not another coefficient clearer.

Sources read from supplied controller results: work/session_20260913/hp_b2_contiguous_endpoint_arithmetic.md and hp_b2_contiguous_endpoint_independent_review.md; work/session_20260927/hp_b1_ternary_actual_denominator.md and hp_b1_prime_seed_transfer_and_closed_atlas.md; the cubic note was consulted only with its strict boundary preserved.

## Endpoint nonvanishing and verification scope

Every quotient and valuation formula above assumes Dcal_n!=0 (and n>=2). The reviewed source identifies this with Y!=0 and supplies eventual nonvanishing from its earlier normality theorem. We inherit that eventual statement; we do not prove nonvanishing at every finite index or infer it from a unit V seed. A congruence Dcal_n=0 modulo p does not mean Dcal_n=0 as an integer. If Xcal_n=0 with Dcal_n!=0, the actual ratio is zero and q_n=1. Otherwise exact reduction always gives v_p(q_n)=max(0,v_p(Dcal_n)-v_p(Xcal_n)), independently of any coefficient clearer.

The preserved certificate records formal substitution, independent direct contractions and rational endpoints at n=2,8, and complete seed vectors (1,2,0) modulo 3 and (4,2,1,3,0) modulo 5. The universal transfer proof, together with these exact finite seeds, gives the stated denominator bound for all n>=3 with n=0,1 modulo 3, and all n>=5 with n=0,1,2,3 modulo 5, always subject to Dcal_n!=0. No unit-seed conclusion covers the remaining residues. These checks support the algebra; finite transferred examples are not the proof of all-index transfer.
