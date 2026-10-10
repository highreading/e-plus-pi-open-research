> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Agent 1 report: actual b=2 numerator and residue criterion

Status: completed mathematical deliverable at the conditional-on-seed level. The proofs are deductions from the supplied reviewed endpoint formulas and are not independently reviewed. The original exact checks and the targeted correction checks both returned PASS. No global denominator estimate or irrationality conclusion is claimed.

The precise boundary error has been corrected in PROOF_DRAFT.md and is explained in CORRECTION_NOTE.md: at n=-1 modulo p, C=-J_n need not vanish. The valid conclusions are S=W=V=Dcal_n=0 modulo p. The factors n+1 in V and (n+1)^2 in Dcal_n justify those conclusions without assuming C=0.

## Proved normalization

Retain the source's integer scalars S,C,W and its b=2 transforms

J_k=kH_k+H'_k(1),
K_k=k(k-1)H_k+2kH'_k(1)+H''_k(1).

This K is the second-derivative transform, not the b=1 quantity J_k/k. With the b=1 Rodrigues contractions Acal_n,Bcal_n and f=2^n/(n!)^2, the exact identities are

T_P=f Acal_n,
T_U=2f Bcal_n/(n+1),
Xcal_n=Qpart2_n+2f V_n,
Qpart2_n=2w_n S-(n+1)^2 w_(n+1)C,
V_n=S Acal_n-(n+1)C Bcal_n-H_(n+1)W.

The actual denominator remains

Dcal_n=(n+1)^2 P_(n+1)C-2P_n S,
X/Y=Xcal_n/Dcal_n.

For completeness, the factorial coefficient calculation is as follows. Set a_s(k)=[z^s](1-z+z^2/2)^k and D_j=j!E_j. Rodrigues gives

[t^(k-s)]L_k(t)=2^k a_s(k)(2k-s)!/[k!(k-s)!], 0<=s<=k.

At k=n, contracting against E_(n+j) and dividing by f gives (n)_s a_s(n)D_(2n-s), the terms of Acal_n. At k=n+1, division by 2f/(n+1) gives the multiplier n!(2n+2-s)/(n+1-s)!. This is 2 at s=0 and (n)_(s-1)(2n+2-s) at s>=1, exactly the terms of Bcal_n. Substitution proves the displayed complete numerator identity over the rationals. Its locally integral expression V uses no division by n+1.

## Proved all-index transfer and actual reduction

For every odd prime p and every n>=0, with r=n mod p, the complete scalar V_n is congruent to V_r modulo p. The proof transfers H and its first two derivatives through their falling-factorial sums, and transfers both exponential contractions using Frobenius and D_j=D_(j mod p) modulo p. It treats the adjacent prime-block boundary explicitly. All these contractions are p-integral.

The integral Legendre quotient and its exact moments give

v_p(Qpart2_n)>=-floor(log_p(n+1)).

For n>=p, 2v_p(n!)>floor(log_p(n+1)). Thus the factorial-normalized second-kind part vanishes modulo p. If V_r is a unit, the full numerator has valuation -2v_p(n!). Exact rational reduction then proves

v_p(q_n)=2v_p(n!)+v_p(Dcal_n)>=2v_p(n!),

under the explicit hypotheses p odd, n>=p, Dcal_n!=0, and V_r!=0 modulo p. This accounts for the actual endpoint cancellation. A nonzero Dcal_n divisible by p increases the resulting denominator exponent; it is permitted.

More generally, if t=v_p(V_n) is finite and 2v_p(n!)-t>floor(log_p(n+1)), the same separation proves

v_p(q_n)=max(0,2v_p(n!)+v_p(Dcal_n)-t).

This is conditional on the actual depth t; no bound for t at a zero seed is supplied.

## Exact evidence and useful residues

The preserved certificate.json records universal formal substitution and independent Legendre-coefficient/functionals checks at the already selected indices n=2,8. The actual reduced denominators recorded there are

| n | V_n | Dcal_n | actual q_n |
|---|---|---|---|
| 2 | 16356 | -12048 | 502 |
| 8 | 53448500944296894375715856868 | -6192556267488572753280 | 546183462792492116839296000 |

The recorded Xcal values are 70440 and 3200566255861823586331472113/88200, respectively. The certificate also gives exact seeds V_0=4 and V_1=32. Hence residues 0 and 1 satisfy the unit-seed condition for every odd prime.

The complete saved V seed vectors, ordered by r=0,...,p-1, are

| p | V residues | zero seeds |
|---|---|---|
| 3 | 1,2,0 | {2} |
| 5 | 4,2,1,3,0 | {4} |

Together with the universal proof, these give the denominator lower bound for all n>=3 with n=0,1 modulo 3, and all n>=5 with n=0,1,2,3 modulo 5, always subject to Dcal_n!=0. The finite checks comparing each seed with its next prime-block representative are verification examples, not a substitute for the all-index proof.

The resumed correction check returned PASS with exit code 0 and sandboxed=true. It checked the formal boundary identities and only the affected pairs (p,n)=(3,2),(3,5),(5,4),(5,9). The p=5 rows have J_n=3 and C=2 modulo 5, exhibiting the precise old error. The p=3 rows have J_n=C=0. All four rows have S=W=V=0; the formal check establishes Dcal=0 modulo p for arbitrary endpoints. Details are in correction_certificate.json.

The successful original checker and certificate were preserved. The correction checker loaded their definitions without rerunning the original test driver. No new degree scan, prime search, or HP nullspace construction was performed.

## Nonvanishing, exceptions, and remaining gaps

Every quotient statement assumes n>=2 and Dcal_n!=0, equivalently Y!=0 in the reviewed source. That source supplies eventual endpoint nonvanishing through its earlier normality theorem. This report inherits that result without reproving the fixed-b error estimate or claiming a new finite cutoff. A unit V seed alone does not prove endpoint nonvanishing. A congruence Dcal_n=0 modulo p does not mean the integer Dcal_n is zero.

The boundary residue n=-1 modulo p always has V_r=0 and is excluded from the unit-seed theorem. For primes 3 and 5 it is the only zero seed in the saved complete vectors. Other primes may have additional zero seeds. Their depths remain unresolved here. The next attainable lemma is a controlled valuation lift of the complete V at such a residue, retaining actual Dcal depth and the second-kind separation threshold. Any use of the corrected C=-J_n must allow C to be a unit.

For n<p, the strict factorial separation is not asserted. In particular n=p-1 is outside the theorem's n>=p scope as well as at a zero seed. The historical contiguous note reports cancellation of p from the actual denominator at n=p-1; its underlying proof was not separately inspected after the historical search refusal. This report does not use that statement as a premise or claim to reprove it. The preserved exact case n=2 has q_2=502, so p=3 does cancel there.

Other degeneracies are retained without division by H,J,K,S,C,W or either contraction. If V_n=0 exactly, Xcal_n=Qpart2_n and the unit-seed argument gives no bound. If Xcal_n=0 and Dcal_n!=0, q_n=1. If Dcal_n=0, the quotient assertions do not apply. The prime 2 is outside this odd-prime theorem.

The large-prime maximal-minor gate retains p>2n+4 and is not imported into fixed small primes. There is no proof here of a global q growth estimate, primitive shrinking, or any irrationality assertion about e+pi.

## Saved records and execution history

All deliverable files are under work/session_20261001_astra/agent1/:

- PROOF_DRAFT.md: the corrected proof and endpoint scope.
- CORRECTION_NOTE.md: old and corrected assertions, their derivation, and affected checks.
- REPORT.md: this evidence and scope report.
- check_exact.py and certificate.json: preserved original exact verification.
- check_correction.py and correction_certificate.json: targeted boundary verification.

The original controller search was refused because symbolic links were not accessed. No bypass, historical executable repair, or alternate search was performed. The resumed correction used the isolated controller runtime and completed successfully. No network or new access outside the assigned directory was used.
