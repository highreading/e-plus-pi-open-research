> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Logarithmic companion cancellation ranges: report

New author research, English and offline, 2026-10-01. Earlier prime-support and odd-gate papers are preserved without repeated calculations or readbacks.

Two explicit floor ranges now guarantee S_p=0, with Q=p^e the highest p-power at most J.

Range A: choose r=p^h, 1<=h<e, with r dividing n. Write n=Ar and 2m=Br+s. If

    A+2B=p^(e-h)-1,
    (r+1)/2<=s<=r-1,

then J lies immediately above Q. Parity removes the low carry, and the required translated coefficient lies beyond the remaining polynomial degree. Hence S_p=0. Every such prime divides n; the aggregate one-factor saving is at most log n.

Range B: take r=p^(e-1), n<r, and 2m=Ar+s. If

    (p+1)/2<=A<=p-1,
    n+2s<r,

then the only possible high target is odd in an even polynomial. Again S_p=0. These primes satisfy p<J/n, so their aggregate saving is at most (J/n)log 4. Neither bound assumes primes exist in any moving interval.

The proof also gives a complete digit-path criterion for absence of monomials in the Frobenius product. Its scope is precise: collected coefficients can cancel even when monomial paths exist.

A new limitation theorem proves that every e=1 prime has an admissible monomial with a nonzero Laurent weight. When Q<=n, that witness uses the negative index a=-1; omitting negative indices would invalidate the conclusion. Thus all cancellation certified solely by missing monomials occurs at p<=sqrt(J). Even removal of every denominator layer supported on those primes has logarithmic mass o(n log n). Support alone cannot provide a leading saving.

For the primes relevant to a leading improvement, p>max(n,sqrt(J)), the exact remaining condition reduces to at most three collected coefficients:

    2m=Mp+r,
    ell_v=[x^(n+vp)](1+2x+2x^2)^n(1-2x^2)^r,
    S_p=chi_p sum_{v=0}^d ell_v Phi_v(M),
    d=floor((n+2r)/p)<=2.

The proof specifies all Phi_v explicitly and their legal denominators. The third weight vanishes when M+1 is divisible by four, but the first two terms remain. This identifies the coefficient cancellation still needed for a leading result.

Each certified zero removes one p from the possible denominator of T. It does not prove absence from Bbeta=den(T/U). The deciding higher-depth condition remains

    p^e T=0 modulo p^(e+v_p(U)),

with all Laurent contributions restored. Endpoint cancellation is tracked separately.

The gap-one theorem remains intact: p=J-1 has the retained nonzero translated coefficient and v_p(T)=-1. None of the new ranges incorrectly cancels that pole.

No leading-rate improvement is claimed. The confirmed safe pi exponent is 36/5, and the relevant strict threshold is the ACTUAL companion denominator rate 5/82. The existing bound remains 4rho log 4; the new support savings are subleading. Further progress requires coefficient cancellation in the leading-prime range or stronger full-content estimates.

Full proof: work/session_20261001_astra/agent1/LOGARITHMIC_COMPANION_CANCELLATION_RANGES.md.

No prime scan, numerical experiment, old checker replay, or independent review was performed. Both new files require the requested controller read-back before final handoff.
