> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The actual raw primitive errors diverge in every degree

Date: 2026-09-13. Assembly by audit_results from fully independently
reviewed arithmetic, even analytic, and odd analytic inputs.
No new computation of an approximant is used.

Let S=e+pi. In the original raw family write


$$
Z_n=\widehat Q_n(1),\qquad
 N_n=\widehat P_{e,n}(1)+4\widehat P_{a,n}(1),
$$




$$
g_n=\gcd(|Z_n|,|N_n|),\qquad
 q_n=|Z_n|/g_n,\qquad
 p_n=\operatorname{sign}(Z_n)N_n/g_n.
 \tag{1}
$$


Thus p_n/q_n=N_n/Z_n, q_n>0, and gcd(p_n,q_n)=1.
All large indices under discussion are defined by the established
normality and nonzero-endpoint theorems.

**Theorem.** For this actual raw family,


$$
\boxed{|q_n(e+\pi)-p_n|\longrightarrow\infty
                    \quad(n\longrightarrow\infty).}    \tag{2}
$$


There is an unspecified finite N_0 such that, for every n>=N_0,


$$
\boxed{|q_n(e+\pi)-p_n|
 \ge\frac{\exp(3n/200)}
 {4\sqrt2\,(25839289479611181)\,n^{10}}.}               \tag{3}
$$


Consequently no subsequence of these primitive forms can shrink to zero.
No nonzero integer multiples of them can shrink either.
This excludes this raw construction as a source of shrinking integer
forms. It does not prove or disprove irrationality of e+pi.

## 1. Uniform denominator divisor, including odd indices

The fully checked uniform-prime set is


$$
{\cal P}=\{3,7,23,43,71,83,101,109,127,151\},\qquad
 C_{\cal P}=\prod_{p\in{\cal P}}p=25839289479611181.
 \tag{4}
$$


The reviewed positive and negative residue transfers and their complete
successful-prime certificates prove, for every n>=302,


$$
v_p(q_n)=v_p(Z_n)\ge v_p(n!)\quad(p\in{\cal P}).
 \tag{5}
$$


These are bounds on the reduced q_n in (1), after its endpoint gcd.
They are not coefficient-clearer or unreduced-height bounds.

The exact dyadic theorem is


$$
a_n=v_2(q_n)=n+2\left\lfloor\frac{n+2}{4}\right\rfloor
                  \ge\frac32n-\frac12.
 \tag{6}
$$


The half-unit loss is retained for the odd degrees. Legendre's digit
formula and the elementary digit-sum bound give


$$
v_p(n!)=\frac{n-s_p(n)}{p-1}
       \ge\frac n{p-1}-\log_p n-1.
 \tag{7}
$$


Combining distinct prime powers in the same actual q_n, (5)-(7) prove


$$
q_n\ge\frac{\exp(Ln)}{\sqrt2\,C_{\cal P}\,n^{10}},
 \quad n\ge302,
 \quad
 L=\frac32\log2+\sum_{p\in{\cal P}}\frac{\log p}{p-1}.
 \tag{8}
$$



## 2. Both actual relative-error asymptotics

Put rho=(sqrt5-1)/2 and phi=1/rho.
The fully reviewed even theorem gives, for n=2m,


$$
S-\frac{N_n}{Z_n}
 =(-1)^m C_{\rm e}\rho^{5n}(1+o(1)),\qquad
 C_{\rm e}=4\pi\rho A_{\rm e}/B_{\rm e}>0.
 \tag{9}
$$


The fully reviewed odd multiplier and contour theorems give, for n=2m+1,


$$
S-\frac{N_n}{Z_n}
 =(-1)^m C_{\rm o}\rho^{5n}(1+o(1)),\qquad
 C_{\rm o}=-4\pi\rho A_{\rm o}/B_{\rm o}>0.
 \tag{10}
$$


The odd exterior amplitude is negative, whereas the odd interior
amplitude is positive. This sign is already incorporated in (10).
The extra odd reference factor z and the odd contour minus sign are
both retained in the reviewed derivations.

The accepted rational amplitude intervals imply


$$
A_{\rm e}>49/1000,\quad B_{\rm e}<121/200,\quad
 -A_{\rm o}>1,\quad 0<B_{\rm o}<1.
 \tag{11}
$$


Using pi>3 and rho>3/5, one obtains
C_e>1764/3025>1/2 and C_o>36/5>1/2.
There are only two parity classes, so their separate o(1) errors
are simultaneously smaller in modulus than 1/2 past one finite index.
Therefore


$$
\left|S-\frac{N_n}{Z_n}\right|
 \ge\frac14\rho^{5n}
 \quad\hbox{for every sufficiently large integer }n.
 \tag{12}
$$


This all-index conclusion combines two independently proved asymptotics;
it does not infer an odd asymptotic from the even one.

## 3. Strict rate margin and divergence

The exact rational interval certificate and its independent review prove


$$
L-5\log\phi>0.015628796017>\frac3{200}.
 \tag{13}
$$


Multiplying (12) by the reduced q_n and using (8),(13) gives (3).
Its right side tends to infinity. This proves (2).

The initial index in (3) is not claimed effective: the arithmetic bound
starts at 302, but the accepted analytic limits have an unspecified
finite prefix. This does not affect the limit or any subsequence exclusion.

## 4. Dependency ledger

The all-index residue transfers are independently reviewed in
raw_positive_residue_transfer_independent_review.md and
raw_negative_residue_transfer_independent_review.md.
The uniform-prime certificate reviews are:

* raw_uniform_23_43_independent_review.md;
* uniform_71_83_independent_review.md;
* raw_uniform_101_109_independent_review.md;
* raw_uniform_127_151_root_review.md.

The three- and seven-adic all-index consequences are included in the
reviewed residue theorems and their synthesis; the latter's explicit
threshold n>=14 is in the negative-transfer review.
The dyadic identity is the original raw_arctan_endpoint_dyadic_attempt.md
theorem. The strict margin has independent PASS in
raw_closed_uniform_rate_independent_review.md.

The even relative-error source and full review are
raw_even_endpoint_residue_asymptotic.md and
raw_even_endpoint_residue_independent_review.md.
The odd sources and full reviews are
raw_odd_saddle_multiplier_limits.md,
raw_odd_saddle_multipliers_independent_review.md,
raw_odd_reference_and_contour_asymptotic.md, and
raw_odd_reference_contour_independent_review.md.
The odd Hardy framework has its separate independent PASS in
raw_odd_hardy_framework_independent_review.md.

None of the odd multiplier, contour, or arithmetic inputs assumes the
conclusion (2). The rate certificate concerns a fixed finite list of
primes; no density conjecture or unchecked infinite scan is used.
