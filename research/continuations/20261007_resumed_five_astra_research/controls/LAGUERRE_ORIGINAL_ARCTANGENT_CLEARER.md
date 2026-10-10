> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An exact original-domain simplification of the Laguerre arctangent clearer

Coordinator derivation, 7 October2026. Active structural arithmetic, not a
primitive-decay theorem. This follows directly from the already specified
integer charge recurrence of A2turn13; no new classical identity is claimed.

Let d=b-1, h=n-d, and let r be the primitive integer polynomial used there.
The expansion coefficients satisfy



$$
\gamma_j=(-1)^{n-j}(n-j)!r_{n-j}
-\sum_{i<j}\binom{n+1}{j-i}\gamma_i,
\quad 0\le j\le d.
$$



Since n-j>=h, induction gives h! dividing EVERY gamma_j, hence every
w_j=binom(n,j)gamma_j and F=sum_j w_j. Retain the complete arctangent correction



$$
B_j=4\sum_{v=0}^{2j-1}\frac{(-1)^v}{2v+1}.
$$



Let Lambda_B=lcm(1,3,5,...,4d-1), with Lambda_B=1 if d=0. Its last possible
odd denominator is4d-1, so it clears every B_j. If h>=4d-1, then Lambda_B
divides h!, and the COMPLETE combined charge



$$
\mathcal B=\sum_j w_jB_j
$$



is an INTEGER. Thus its ACTUAL reduced denominator ell is exactly1.

Every original n=2001b index has h=2000b+1>=4(b-1)-1. Consequently



$$
\boxed{\ell=1,\quad T=\mathcal B\in\mathbb Z,\quad h!\mid F}
$$



on the full original family. More precisely h!/Lambda_B divides T, including
all prime powers, because each summand w_jB_j has that factor. This common
factor of F and T is not a factor of E without a separate proof.

Independently, the repeated root at1 in r=a(x-1)^d p_h implies



$$
E=e\int_1^\infty e^{-x}r(x)\,dx
=\sum_{j=0}^h (d+j)!s_j,
$$



where s_j are the INTEGER coefficients of r(1+u)/u^d. Therefore d! divides E.
This is a lower divisor of E, not an upper bound on gcd(F,E+T).

The actual remaining primitive denominator and whole error are accordingly



$$
g=\gcd(|F|,|E+T|),\qquad q=|F|/g,
\qquad q(e+\pi)-p=-M/g
$$



on the original odd-n family. A2turn14's claimed paid comparison reduces to
R/(2g)<q(e+pi)-p<6005R/g, conditional on independent validation of its sign
and root proofs. The raw divisors above do not establish a sufficiently large
g, bound R/|F|, or imply irrationality. No gains are transferred to the older
prime29 producer or to the different even-contact compact family.
