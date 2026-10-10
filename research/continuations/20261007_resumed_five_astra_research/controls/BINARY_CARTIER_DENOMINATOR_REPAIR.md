> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Parent audit: a missing factor in the new denominator transition

The original bytes of A5 turn2 remain unmodified. Its displayed identity
`(1-t)^2=(1-t^2)-2t` is false over the integers. The right identity is



$$
(1-t)^2=(1-t^2)-2t(1-t).
$$



Consequently its K0 in (5.6) is missing the factor `(1-t)^s` in each
summand. A small decisive example is M=2,L=2: its proposed right side has
t^2 coefficient 1 modulo4, whereas `(1-t)^(-2)` has coefficient3.
This is a mathematical error; it is not evidence of prompt injection.

The following parent-derived replacement preserves the state convention.
Put M=2h+epsilon, M'=h+epsilon+L-1 and



$$
K_0^{\rm repaired}(t)=\sum_{s=0}^{L-1}
 2^s\binom{h+s-1}{s}t^s(1-t)^s(1-t^2)^{L-1-s},
$$



with the same h=0 convention (coefficient1 for s=0, otherwise0). Then



$$
(1-t)^{-M}\equiv
\frac{(1+t)^{\epsilon}K_0^{\rm repaired}(t)}
     {(1-t^2)^{M'}}\pmod{2^L}.
$$



Proof: factor `(1-t)^2=(1-t^2)(1-2t(1-t)/(1-t^2))`, expand the
negative binomial series for exponent h, and discard s>=L because of its
factor2^s. For the odd part use `(1-t)^(-1)=(1+t)/(1-t^2)` exactly.
Each surviving term has integral coefficients. The maximum degree of
`t^s(1-t)^s(1-t^2)^(L-1-s)` is2L-2; the optional odd factor increases
it to2L-1. Thus the author's support-width argument has the same degree
input after this correction. Other claims, including coefficient acceptance,
assembly merging, runtime, source coefficients and primitive precision,
must still be independently inspected.

The parent is authoring a bounded direct-kernel versus corrected-Cartier
audit. Its finite outputs are auxiliary identity checks, not an original
primitive digit or an infinite-family congruence. No remote code is executed.
