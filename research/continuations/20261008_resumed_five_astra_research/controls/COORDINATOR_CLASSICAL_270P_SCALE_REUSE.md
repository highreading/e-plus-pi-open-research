> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Reuse of Sun--Davis for the next prefix digit

Status: classical lemma applied to the original power-of-three scale.
The complete source-specific prefix modulo81 theorem is NOT asserted.

## Known theorem and the scale application

[Sun--Davis, Lemma3.2](https://www.lehigh.edu/~dmd1/SunDavis.pdf) states
for odd prime p, n>0 and k>=0 that binom(pn,pk)-binom(n,k) is divisible
by p^(2v_p(n)+2). Its separate p=3 proof was read, so the p>3-only
Jacobsthal statement is not being extended without justification.

Let P=3^s, s>=0, and0<=a<=270. Apply that lemma at p=3,
n=270*3^r and k=a*3^r, for r=0,...,s-1. Since v3(n)=3+r,
each consecutive scale difference is divisible by3^(8+2r).
Their finite telescoping sum therefore proves

    binom(270P,aP) = binom(270,a) (mod3^8).

The endpoint cases a=0,270 and s=0 are exact equalities. This is a
reuse consequence of a published theorem, not a new general result.

## Precisely paid precision

A1turn9 Section5.2 identifies the normalized MACRO-grid pole weight
81/d, with odd0<d<=1027 and v3(d)<=6. Replacing an admitted aP
coefficient by its unscaled270 coefficient consequently has valuation
at least4+8-6=6. Thus the replacement error is zero modulo729,
in particular modulo81. The finite number of terms does not reduce
this bound. This removes the macro-scale binomial replacement as an
obstacle for the next digit.

The original beta=-71-A with A=4^j-1 divisible by243 gives
beta=-71 modulo243, hence beta=10 modulo81. There is no claim that
beta=10 modulo243. The source weights and their higher digits remain
attached to the original producer.

## Remaining source and finite inverse obligations

The old non-P-residue and discarded-pole arguments only establish
vanishing at modulo27. They must be revisited at modulo81, where
previously discarded layers can contribute. This scale application
does not establish that the COMPLETE residual remains on a P grid.
The new D_j modulo81 receipt is therefore an arithmetic receipt for
the defined macro constants, not an assignment of every actual d entry.

The full core finite inverse needs its next matrix jet and all terminal
contractions. The actual-to-core correction
Delta_A=(A_act-A_core)/27 modulo3 is still unknown. Its contraction
on the nine already evaluated leading inverse-image blocks cannot be
declared zero. These are distinct obligations; the existing modulo27
prefix candidate still awaits a DIFFERENT external full-proof audit.
