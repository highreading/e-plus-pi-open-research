> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large-selector odd gate lifting report

New author research, offline, 2026-10-01. The completed odd-arithmetic proof is retained unchanged. No independent review or prime scan was performed.

The complete gate admits a new algebraic reduction for every odd gap s=J-p. Replacing the reverse-polynomial exponent 2m by (s-n)/2 modulo p leaves a finite coefficient expression depending only on n and s. It retains the logarithmic term -2chi r!.

For the explicit gap-one slice p=J-1, the condition reduces to the integer

    F_n=nD_n+2n n!+1,
    W=2^(N/2) F_n modulo p.

Therefore p not dividing F_n proves the actual law

    v_p(q)=1+v_p(U).

If p divides F_n and U is a p-unit, p cancels completely. Universal survival is false: the algebraically selected example (n,m,p)=(4,37,151) has F_4=453, U=6204=13 modulo p, and v_p(q)=0.

For every rho>0 the note specifies an infinite parameter family

    n=4k,
    m=P ceil((rho n log n+k)/P)-k,
    p=n+4m-1,

where P is the least power of two greater than k. It satisfies m~rho n log n and p=-1 modulo 4P. Whenever the candidate p is prime, it lies in the requested interval. Infinitely many prime candidates, or infinitely many surviving candidates, are NOT proved.

The new first-depth theorem retains both complete numerator terms:

    W=2^(N/2)F_n+p Xi modulo p^2.

Xi explicitly contains the recurrence correction, Wilson quotient, moment-pole correction, regular logarithmic sum, and the previously suppressed exponential terms. When p divides F_n, put Theta=2^(N/2)F_n/p+Xi modulo p. If Theta is nonzero, then v_p(W)=1 and v_p(q)=v_p(U).

A separate exact endpoint expansion is

    U=Aend_n+p Bend_n modulo p^2,

with both coefficients defined by finite formal coefficient extraction. If Aend_n vanishes but Aend_n/p+Bend_n does not, then v_p(U)=1. Combined with nonzero Theta, this proves v_p(q)=1 even though the first numerator gate vanished. If Theta vanishes and v_p(U)<=1, p cancels entirely. Higher simultaneous zeros retain an explicit complete lifting problem.

The one new exact check returned PASS_SINGLE_NEW_GATE_AND_FIRST_LIFT_WITNESS. At the cancellation witness it gave Theta=28 modulo 151 and v_151(W)=1, while checking the complete numerator and endpoint expansions modulo p^2. This finite evidence is not substituted for the all-index proof, and the successful check was not repeated.

Deliverables:

    work/session_20261001_astra/agent1/LARGE_SELECTOR_ODD_GATE_LIFTING.md
    work/session_20261001_astra/agent1/LARGE_SELECTOR_ODD_GATE_LIFTING_REPORT.md

Supporting script and result:

    work/session_20261001_astra/agent1/check_large_selector_odd_gate_lifting.py
    work/session_20261001_astra/agent1/large_selector_odd_gate_lifting_check.json

No complete-error, asymptotic prime-product, or irrationality conclusion is claimed. The main dyadic result remains an author dependency and was not audited.
