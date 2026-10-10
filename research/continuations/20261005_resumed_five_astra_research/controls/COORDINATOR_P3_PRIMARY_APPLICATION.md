> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A primary-source application closing the moving-base logarithm input

Status: coordinator derivation for independent review, October 5, 2026.
The original author-hosted paper was downloaded from
https://irma.math.unistra.fr/~bugeaud/travaux/logpadicdef.ps . Its SHA256 is
8efa1b161a1e7b3045027c3f491fdcdd2a18a50a6e889c2a2a1937976d8ba990.
The paper is Bugeaud and Laurent, Journal of Number Theory 61 (1996),
311–342, DOI 10.1006/jnth.1996.0152. Theorem 3 and its parameter definitions
were read in the source and visually checked on printed page 4. This
uses the fully explicit theorem, rather than its asymptotic Theorem 2.

## Exact theorem parameters

For multiplicatively independent p-adic units alpha1, alpha2, positive
integer exponents b1,b2, the theorem bounds the valuation of
Lambda=alpha1^b1-alpha2^b2 by

v(Lambda) <= [24 p g/( (p-1)(log p)^4 )] D^4
  max{log b' + log log p + 0.4, 10 log p/D, 10}^2
  log A1 log A2.

Here D=[Q(alpha1,alpha2):Q]/f, where f is the local residue degree;
g is the smallest positive integer making both alpha_i^g principal units;
log Ai >= max{h(alpha_i),log p/D}; and
b'=b1/(D log A2)+b2/(D log A1).
The source's valuation is normalized by v(p)=1. All logarithms in this
display are real logarithms; no guessed logarithm-convergence convention
is being added to the theorem.

## Application to the actual moving positive integer B

Take p=3, alpha1=4, alpha2=B, b1=J, b2=1, for J>=1, B>=2,
B=1 mod3, and multiplicatively independent 4,B. Both are rational
principal 3-adic units. Thus f=1, D=1 and g=1. Set A1=4 and A2=B.
An independent B in this residue class is at least 7, so both height
requirements hold. The actual difference is nonzero by multiplicative
independence (and independently by the retained actual-index positivity).

The exact theorem gives

v3(4^J-B) <= [36/(log3)^4] log4 logB
 max{log(J/logB+1/log4)+log log3+0.4,10log3,10}^2.

This exhibits the required uniform moving-height dependence directly.
For a simple deliberately loose bound, use 1<log3<2, 1<log4<2,
b'<=J+1, and log log3+0.4<2. The displayed maximum is at most
20(1+log(J+1)). Therefore

v3(4^J-B) <= 28800 logB (1+log(J+1))^2
           <= 30000(1+logB)(1+log(J+1))^2.

The absolute constant is uniform in B and J. It is intentionally not
optimized. The dependent case, B not equal to1 mod3, and finitely many
nonpositive original factors are handled separately by A1 turn0's
LTE and positivity argument. This proves the precise missing P3 input
at the usual acceptance of the cited classical theorem.

## Consequence to review

Combine this bound with A1 turn0's proven quantitative original-index
family log(j+1)=O(t), its nested-residue estimate, and the previously
audited fixed and tail terms. The moving block begins above 3^t, while
the maximum valuation loss is O((1+log u)t^2). The first term dominates
uniformly for u>=3^t as t grows. This is sufficient for the same
3^143 grouped continuation. Every actual finite upper boundary remains
unchanged. Neither this application nor the continuation evaluates the
terminal Wronskian, improves actual polynomial precision beyond3^6,
or controls the final primitive denominator.

An independent review should check the theorem's field/local parameters,
the nonzero difference, the uniform constant, and all original-index
conditions before adopting the core continuation as unconditional.
