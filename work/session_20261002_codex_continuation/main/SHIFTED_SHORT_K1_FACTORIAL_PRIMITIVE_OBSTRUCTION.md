> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# M27. Exact inverse extraction closes the shifted short k=1 family

Author theorem: for even M tending to infinity, the COMPLETE primitive forms of the shifted short k=1 family diverge. This excludes this approximation family; it does not decide the rationality of e+pi or exclude growing k.

## Fresh archive and primary gate

The archive already contains quantitative rational-companion exclusions using the known irrationality measure of e, including sources/algebraic_translation_approximation_no_go.md and agent1_arithmetic/POLYNOMIAL_PULLBACK_FACTORIAL_CORE.md. Their general strategy and continued-fraction lemma are credited. A fresh search found no completed inverse-extraction identity for the newly introduced shifted short k=1 determinant. No novelty is claimed for the general method.

Fresh primary sources were read: Henry Cohn, *A Short Proof of the Simple Continued Fraction Expansion of e*, arXiv:math/0601660v3, six-page proof including its Euler expansion; Chan and Norrish, *Proof Pearl: Bounding Least Common Multiples with Triangles*, J. Automated Reasoning62(2019), Sections7.1--7.3, Theorems3/31. The first supports the classical uniform continued-fraction input below; the second proves lcm(1,...,X)<=4^X. Their statements are applied, not independently audited.

## Full center and an exact rational extraction

Use even M>=2, X=2M, t=X+1, d=D_X, f=X!,

    A=t^2+t+1, B=t^2+1,
    l=4 sum_(a=1)^M (-1)^(M-a)/(2a-1).

Direct evaluation of the COMPLETE2-square stack gives

    c=-l+r,
    r=[Bf+4(d-1)/t]/(Ad-t).                (1)

Let q be the actual reduced denominator of c, and let a be that of l. Then den(r)<=a q; no raw determinant clearer is substituted for q.

Define the rational inverse extraction

    v=B/(Ar-4/t).                          (2)

The exact endpoint relation implies

    v=d/f-(tr-4/t)/[f(Ar-4/t)].             (3)

For X>=4, d/f lies between1/3 and1/2. Formula(1) then gives 1<r<4, and Ar-4/t>=t^2. The alternating-series remainder and(3) imply

    0<abs(v-1/e)<=6/(X f).                 (4)

The strict lower inequality uses irrationality of1/e, since v is rational. This is an extracted exponential approximation, not the full center error.

Writing r=R/Q reduced, (2) gives

    v=B t Q/(t A R-4Q),
    den(v)<=8 t^3 a q.                     (5)

All cancellations in v and c can only reduce these upper bounds; the actual q remains present.

## Classical continued-fraction input and factorial q lower bound

Euler's partial quotients for e grow at most linearly with the convergent index, while convergent denominators grow at least geometrically. Legendre's criterion and the standard lower convergent inequality therefore give a constant c0>0 such that every rational u/b satisfies

    abs(e-u/b)>=c0/[b^2 log(2b)].

Reciprocation, restricted to rational numbers near1/e, gives the same form for1/e with another constant. This is exactly the elementary uniform lemma already saved in the archive, now sourced by the fresh Cohn read.

Let b=den(v). Combining it with(4) gives

    b^2 log(2b) >= c1 X f.                 (6)

A simultaneous raw upper bound is q<=a t(Ad-t). Also a<=lcm(1,...,X-1)<=4^X. Thus log(2b)=O(X logX), using(5) and d<=f. Substituting(5) into(6) yields

    q >= c2 sqrt(X!)/[a (X+1)^3 sqrt(logX)],
    log q >= (1/2)log(X!)-X log4-O(logX).   (7)

This lower bound applies AFTER the full final coefficient gcd, without any conjecture about gcd(D_X,X!) or the mixed endpoint pair.

## Complete signed error and final branch exclusion

The complete arctangent remainder is exactly

    pi+l=4 integral_0^1 x^X/(1+x^2) dx
         =2/(X+1)+O(X^-2).

Formula(1), d/f=1/e+O(1/(Xf)), and B/A=1-t/A give

    r=e-e/(X+1)+O(X^-2).

Consequently the COMPLETE center satisfies

    c-(e+pi)=-(e+2)/X+O(X^-2).             (8)

In particular it is below S and its full error is nonzero for sufficiently large even M. Combining(7)--(8),

    abs(q(c-S)) tends to infinity,
    log abs(q(c-S)) >= (1/2)X logX-O(X).    (9)

Thus every infinite even-shift subsequence at k=1 fails the small-nonzero-integer-form criterion. This conclusion concerns the exact primitive denominator and both errors together, not a separate exponential or logarithmic form.

## New exact normalization receipt

Three new indices M4,12,48 check the complete endpoint stack against(1), the rational extraction(3), and the exact denominator upper bound(5). Numerical checks of(4) and the scaled complete error are explicitly diagnostics. Their actual denominator bit lengths are stored in SHIFTED_SHORT_K1_EXTRACTION_CERTIFICATE.json. The infinite conclusion(9) is the author proof above, independent of these finite checks.

Files: SHIFTED_SHORT_K1_EXTRACTION_CERTIFICATE.json and shifted_short_k1_extraction.py.

Remaining scope: k>=2, especially growing k, requires a different inverse-extraction or full-content argument. No e+pi irrationality proof is asserted.
