> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An explicit degree81 integral-Hurwitz polynomial with composition radius greater than2

Root original construction,2026-10-02. Author certificate; main research ACTIVE.

## Result

Freeze the80 integers K_k in EXPLICIT_DEGREE81_RADIUS2005_CERTIFICATE.json and set

    P(z)=z+sum_(k=1)^80 K_k z^k(1-z)/k!,
    F(w)=4 arctan(w/(2-w)), G=F composed with P.

Then P(0)=0, P(1)=1, P'(0)=1, every derivative P^(j)(0) is integral, G(1)=pi, every derivative G^(j)(0) is an even integer, and

    TaylorRadius(G)>401/200=2.005.

This is a concrete fixed polynomial reaching beyond2. The prior explicit degree61 result certified1.98; the earlier infinite-Schur theorem already proved the existence of some finite polynomial at every radius below2.665. The novelty here is the complete finite integer vector and its exact zero-free certificate beyond2, rather than a stronger abstract existence theorem.

## Exact arithmetic certificate

The endpoint basis contributes K_k at derivative order k and-(k+1)K_k at order k+1. For q(z)=P(z)-(1+i), form the degree81 reciprocal polynomial w^81 q((401/200)/w) and clear its rational Gaussian denominators. All81 exact Gaussian Schur gaps are strictly positive. Its roots lie strictly inside the unit circle, hence every root of q lies strictly outside the closed disk radius401/200. Real coefficients give the same assertion for P-(1-i).

The composition is therefore analytic on a neighborhood of that closed disk. Its branch is defined at0 and along the real endpoint path gives G(1)=pi. The integer derivative recurrence for F and the Bell-polynomial composition identity prove all-order even integral jets, independently of finite numerical computations.

The certificate saves the basis, all polynomial jets, initial state hash,81 positive gap records, removed Gaussian contents and final nonzero constant. The largest norm has323685 bits. The driver imports only definition-level Gaussian arithmetic from scripts/nonpolynomial_integral_hurwitz_pullback_certificate.py and records that dependency's SHA256; it does not replay an older candidate or perform a floating-point proof decision.

## Candidate generation and scope

The numerical generator extends the finite Schur interpolant to formal order100 at260-digit precision, then rounds in the endpoint basis. It proposes degree81 and degree101 vectors. The diagnostic closest root moduli are approximately2.01027 and2.01176. These approximate values are not asserted as proved bounds. Only the degree81 candidate was subjected to the new exact certificate at401/200.

This fixed P can now serve as the concrete base in the actual-denominator cancellation constructions. It does not itself prove irrationality: the ordinary Taylor denominator retains its factorial core, and the exponential-gauged center still requires a favorable global gcd estimate. No claim that the main problem has been solved is made.

## Prior-work gate and primary sources

Before generation, the archive's integral-Hurwitz constructions, degree61 receipt and infinite-Schur continuation were checked. They did not contain this vector or an explicit certified polynomial with radius beyond2. Fresh primary-paper searches and reads included Waldschmidt, Integer-valued functions, Hurwitz functions and related topics: a survey (https://arxiv.org/html/2002.01223v1), and Dym and Young, A Schur-Cohn theorem for matrix polynomials (https://www.cambridge.org/core/services/aop-cambridge-core/content/view/5AB9F1B5788EC10C3C510CB2218B26FE/S0013091500004806a.pdf/schurcohn_theorem_for_matrix_polynomials.pdf), especially its scalar Schur criterion. Those sources provide general tools, not this endpoint-fixed finite vector or an e+pi proof.
