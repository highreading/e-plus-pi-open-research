> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the ternary actual-numerator root

Date: 2026-09-27. Reviewer: root. Status: FULL PASS for Sections 3--5
of `hp_b1_residue_one_actual_numerator.md`.

The normalized actual endpoint quotient is inherited from the already
independently reviewed ternary denominator note. I checked the new
coefficientwise tail cutoff: R>=12 implies k=floor(R/3)>=4, and
k-v3(k!)>=(k+1)/2>=5/2, hence integral valuation at least 3.
The D-series cutoff at length 9 supplies the same precision. The
inverse of 2+3Y is correctly retained through degree 2 modulo 27.

The exact finite polynomial checker was read and rerun. It performs
rational polynomial operations on the entire truncated germs, checks
3-integrality of every final coefficient, and verifies all displayed
residue polynomials. This is a finite coefficient certificate, with
proved tails, rather than an inference from sampled HP indices.

The index derivative H'(1)=-3/2 follows from its three s<=1 terms;
all s>=2 terms have two vanishing falling factors. For the second
x-derivative germ the same calculation yields index derivative 3.
The adjacent identity then gives K'(1)=4. Therefore C'(1)=27
is an exact rational identity. These derivatives are index derivatives
of the interpolated germs and are not confused with x derivatives.

C(1)=0 exactly and C(1+3Y)=9Y^2 mod27 imply that F=C/(9Y)
is an integral restricted series with F=Y mod3 and F(0)=9. Hensel
and restricted-series division give one root eta and a unit quotient.
The root equation implies eta=-9 mod27, and hence
xi=1+3eta=55 mod81. Restoring the two index factors proves
v3(C_n)=v3(n-1)+v3(n-xi), including possible infinite valuations.

The H and K germ congruences imply respectively valuations >=a+1
and a. The established 3-unit property of P_n then makes Delta's
two terms have unequal valuations, so v3(Delta)=a exactly.
Comparison of the actual numerator's factorial and second-kind terms
gives v3(q)=2f-c when c<2f-L, and v3(q)<=L otherwise. These are
respectively an equality and an upper bound, as the note states.
The outside-exception formula, n=7 check, and elementary factorial
inequality for n>=10 are valid. The zero-residue addendum uses the
correct four scalar seeds and strict valuation separation.

No Diophantine estimate for proximity to xi has been established.
This PASS therefore does not remove the exceptional ternary disk and
does not give a whole-family exclusion or a main irrationality proof.
The uniform-prime lift in Sections 1--2 has a separate review by the
results agent; its status is not silently inferred from this audit.
