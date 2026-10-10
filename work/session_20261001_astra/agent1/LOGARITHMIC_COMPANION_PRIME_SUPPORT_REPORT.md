> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Logarithmic companion prime-support report

New author research, English and offline, 2026-10-01. The completed odd-gate and lifting papers are preserved without repeated calculation. The main finite-measure transfer draft was read; its external pi input remains pending source confirmation.

For N=2n+4m and J=N-n, integration by parts gives the exact rational identity

    T=sum_{d=-n, d!=0}^J c_(n+d) tau_d/d,
    sum c_h x^h=Bpoly(1+x),
    tau_d=(2/i)(((-1+i)/2)^d-((-1-i)/2)^d).

Boundary terms vanish because Bpoly has order-n zeros at both integration endpoints. Thus

    O_J T belongs to 2Z,
    Bbeta divides O_J |U|/2.

This removes moment prime-power levels above J. Primes can still remain through U, which is tracked separately.

There is an exact content factorization. Put Z_T=O_J T/2, g_T=gcd(O_J,|Z_T|), D_T=O_J/g_T and M_T=Z_T/g_T. Then

    Bbeta=D_T (|U|/2)/gcd(|U|/2,|M_T|).

D_T is the actual denominator of T. This separates cancellation before division by U from final endpoint cancellation.

For every odd p<=J, e=floor(log_p J), an explicit signed coefficient sum S_p determines p^e T modulo p. A nonzero S_p proves v_p(Bbeta)=e+v_p(U); a zero S_p removes at least one moment-denominator factor p. The proof gives a deterministic refined product bound from these tests without asserting how often they vanish.

In max(n,N/2)<p<=J, with odd gap s=J-p, the test simplifies to

    pT=2chi_p 2^(N/2) L_(n,s) modulo p,
    L_(n,s)=[x^s](1+x+x^2/2)^n(1-x^2/2)^((s-n)/2).

For s=1, L_(n,1)=n. Therefore every admissible prime p=J-1 satisfies

    v_p(T)=-1,
    v_p(Bbeta)=1+v_p(U).

This is a proved obstruction to universal cancellation of those logarithmic poles. It applies to every prime member of the explicit binary-congruence allocation with m~rho n log n. Infinitely many prime members are neither proved nor assumed.

At the previously retained cancellation example (4,37,151), this gives v_151(Bbeta)=1 although v_151(q)=0. No calculation was repeated: complete-center cancellation and logarithmic-companion cancellation are different.

The deterministic O_N-to-O_J saving is subleading: O_N/O_J divides binom(N,n), whose logarithm is O(n log log n) in this regime. A leading improvement still requires quantified content cancellation. The remaining deciding congruence is

    p^e T=0 modulo p^(e+v_p(U)),

with every regular moment contribution restored when the first test vanishes. No leading-rate improvement, prime-product asymptotic, or irrationality conclusion is claimed.

Full proof: work/session_20261001_astra/agent1/LOGARITHMIC_COMPANION_PRIME_SUPPORT.md.
