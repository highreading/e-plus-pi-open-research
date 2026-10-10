> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent rate and all-even denominator audit

Date: 2026-09-13. Reviewer: audit_sources.
**FULL PASS for the exact rate certificate and the mathematical implication.**
The implication uses the successful-prime certificates separately; this
review does not substitute for their assigned arithmetic audits.

Audited sources:

- raw_third_predeclared_uniform_seed_list_and_rate.md, Sections 3--4;
- check_closed_uniform_seed_rate.py;
- raw_closed_uniform_seed_rate_certificate.json.

The source checker was rerun unchanged. A second exact calculation is
saved in check_closed_uniform_rate_independent.py and
closed_uniform_rate_independent_certificate.json. Neither rate checker
computes a new seed, prime classification, or large-degree approximant.

## 1. Rational certificate

The exact prime set used by the source and independently checked is



$$
{\cal P}=\{3,7,23,43,71,83,101,109,127,151\}.
$$



Its ten elements are distinct odd primes, and



$$
C_{\cal P}=\prod_{p\in{\cal P}}p=25839289479611181.
$$



The source's 24-term atanh series is valid after its exact rational
range reduction into [1,2). The omitted exponents start at 49.
Replacing every denominator in the positive tail by 49 and summing
the geometric series gives exactly the displayed tail bound.
Fraction division by two preserves exact rational arithmetic.
The square-root bracket is checked by rational squaring; endpoint
monotonicity gives the correct lower and upper bounds for log(phi).
The final integer floor/ceiling operations round outward.

For an independent check, the second verifier uses the different series



$$
\log x=\sum_{j=1}^{72}\frac{u^j}{j}+\mathcal T,\qquad
 u=1-\frac1x,\quad 0\le u\le\frac12,
$$




$$
0\le\mathcal T\le
 \frac{u^{73}}{73(1-u)}.
$$



It uses the separate rational bracket



$$
\frac{22360679774997896964}{10^{19}}
 <\sqrt5<
 \frac{22360679774997896965}{10^{19}},
$$



again checked by squaring. Its independently derived intervals lie
strictly inside every source display. In particular, with



$$
L=\frac32\log2+\sum_{p\in{\cal P}}\frac{\log p}{p-1},
 \qquad T=5\log\phi,
$$



both calculations certify



$$
2.421687921315<L<2.421687921316,
$$




$$
2.406059125298<T<2.406059125299,
$$




$$
0.015628796017<L-T<0.015628796018.
$$



The strict gap also exceeds 3/200. No ordinary floating-point logarithm,
square root, or tolerance is used.

## 2. Uniform factorial threshold

For p>=7 and n>=2p, put m=floor(n/p)>=2. Then



$$
2n<2p(m+1)<p^m.
$$



The last inequality starts from 6p<p^2 and propagates because
p(m+1)>m+2. Hence



$$
\lfloor\log_p(2n)\rfloor<m\le v_p(n!).
$$



This proves the strict factorial-versus-arctangent-loss inequality
needed by each reviewed residue transfer. It is uniform over all residue
classes and includes n divisible by p. The separately proved ternary
threshold n>=9 is sufficient for p=3.

Thus n>=302=2*151 handles all ten primes at once. Once the specified
finite certificates have PASS, the actual numerator N_n is a unit at
each p in this set, and the actual reduced denominator satisfies



$$
v_p(q_n)=v_p(Z_n)\ge v_p(n!).
$$



This is stronger than a bound on an unreduced denominator: the unit
numerator explicitly prevents cancellation at these primes.

## 3. Combining the same-index divisors

The exact dyadic theorem gives



$$
a_n=v_2(q_n)=n+2\left\lfloor\frac{n+2}{4}\right\rfloor.
$$



For even n, a_n>=3n/2. All odd prime powers concern the same actual
index n, so their pairwise coprimality gives



$$
2^{a_n}\prod_{p\in{\cal P}}p^{v_p(n!)}\mid q_n.
$$



Legendre's digit formula and the elementary digit bound give



$$
v_p(n!)=\frac{n-s_p(n)}{p-1}
 \ge\frac{n}{p-1}-\lfloor\log_p n\rfloor-1
 \ge\frac{n}{p-1}-\log_p n-1.
$$



Multiplication of the ten resulting inequalities yields exactly



$$
\boxed{\displaystyle
 q_n\ge
 \frac{\exp(Ln)}{25839289479611181\,n^{10}}
 \qquad(n\ge302,\ n\text{ even}).}
$$



There is one factor n and one factor p lost for each of the ten odd
primes. The dyadic estimate incurs no additional polynomial factor.
The constant, the exponent n^10, and the use of the reduced q all check.

## 4. Consequence for primitive errors

The independently reviewed even asymptotic is



$$
(e+\pi)-\frac{N_n}{Z_n}
 =C_{\rm app}(-1)^{n/2}\exp(-Tn)(1+o(1)),
 \qquad C_{\rm app}>0.
$$



If p_n/q_n is the same rational number in reduced form with q_n>0,
then multiplication by q_n is exact. After an unspecified finite
prefix, its absolute error is at least



$$
\frac{C_{\rm app}}{2C_{\cal P}}
 \frac{\exp((L-T)n)}{n^{10}},
$$



which tends to infinity along even n. The factorial denominator bound
is explicit from n=302, but the factor 1/2 in the asymptotic need not
be valid already at n=302; the source correctly distinguishes these.
No effective asymptotic starting index is claimed.

Therefore, after the separate finite certificate gates close, no
subsequence with even degrees tending to infinity can have shrinking
primitive errors. Nonzero integer multiples of these primitive forms
cannot shrink either. This says nothing about an odd-degree asymptotic,
other approximating families, or the rationality or irrationality of
e+pi.

## 5. Dependency status and corrections

This reviewer separately completed the full arithmetic PASS at 71 and
83 in uniform_71_83_independent_review.md. The 23/43 and 101/109
certificates are assigned to audit_computations; the 127/151 certificates
are assigned to root. Uniform 3 and 7 are prior reviewed results.

No correction to the rate code, displayed intervals, threshold proof,
or all-even implication was needed. Its conditional status should be
removed only when those separate certificate reviews are complete.
