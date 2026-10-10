> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Distinguish one canonical certificate from optimizing all certificates

9 October2026. This is a classical primitive-row observation used as a
scope filter, NOT a claimed new source-content theorem. It prevents the
new fixed-row obstruction from being mistaken for a disproof of HC.

Use the actual signed source U=c*tau,V=c*nu, gcd(tau,nu)=1, K=Q_H[N-1]*Q_H[N].
The new A5turn13 certificate has multiplier B=c*D, D=M-E<0, and fixed
integer row(a0,b0). It therefore gives

    a0*tau+b0*nu=K*D.

ALL integer rows producing this SAME multiplier are

    a=a0+nu*t, b=b0-tau*t,  t in Z.                   (1)

If a positive d divides both coefficients, then d divides K*D.
Conversely choose integer x,y with x*tau+y*nu=1. The choice
t=-a0*y+b0*x in(1) gives(a,b)=(x*K*D,y*K*D). Thus whenever d divides
K*D, some row in(1) has both coefficients divisible by d. Requiring
also an integer divided multiplier is exactly d|B. The maximal possible
common division over ALL rows is therefore

    d_max=gcd(|c*D|,|K*D|)=|D|*gcd(c,K).

Its optimally divided multiplier is exactly

    |B|/d_max=c/gcd(c,K).                            (2)

Consequently optimizing all unrestricted certificate rows just recovers
HC itself. Generic Bezout existence or the affine lattice(1) cannot
supply an exponential upper bound for(2). The canonical TDC condition
in A5turn13 is sufficient and stronger: it restricts to that particular
row's available divisions. Its failure would not disprove HC. Conversely,
HC does not by itself force that special row to meet TDC.

The useful next mathematical target is a quantitatively controlled
original-source mechanism for HC, or directly for the intrinsic J0,
using the ACTUAL changing Gaussian data and complete forced boundaries.
No final-gcd or whole-error conclusion follows from(1)--(2).
