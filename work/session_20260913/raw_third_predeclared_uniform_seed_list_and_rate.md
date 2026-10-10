> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Third closed seed list and a threshold-crossing rate certificate

Date: 2026-09-13. Original finite computation and rate assembly by
audit_results. All internal exact checks PASS.
**All dependencies required for the even-degree exclusion have independent
PASS.** The all-index transfer audits are
raw_positive_residue_transfer_independent_review.md and
raw_negative_residue_transfer_independent_review.md. Complete successful-prime
reviews are raw_uniform_23_43_independent_review.md,
uniform_71_83_independent_review.md, raw_uniform_101_109_independent_review.md,
and raw_uniform_127_151_root_review.md. The exact rate comparison has
independent PASS in raw_closed_uniform_rate_independent_review.md.
The unsuccessful-prime witness rows retain their internal certificates;
they are not dependencies of the exclusion theorem.

The third predeclared list is exactly
101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,
179,181,191,193,197,199. The calculation stopped at the end of this
closed list. It built only modular small Schur seed matrices, with
Appell degrees below p; it built no original large-degree approximant.

## 1. Complete successful primes and first bad witnesses

The new internally certified uniformly good primes are
**101,109,127,151**. Each has a saved certificate for all p residues.
For every other prime the first bad residue was retained and the
calculation stopped. Untested residues are not classified.

| p | First bad residue | Branch, k | Reason | D | E |
|---:|---:|:---|:---|---:|---:|
| 101 | none | all 101 residues | all good | units | units |
| 103 | 98 | negative, 4 | endpoint zero | 64 | 0 |
| 107 | 82 | negative, 24 | determinant zero | 0 | not needed |
| 109 | none | all 109 residues | all good | units | units |
| 113 | 93 | negative, 19 | determinant zero | 0 | not needed |
| 127 | none | all 127 residues | all good | units | units |
| 131 | 105 | negative, 25 | endpoint zero | 9 | 0 |
| 137 | 24 | positive, 24 | determinant zero | 0 | not needed |
| 139 | 51 | positive, 51 | determinant zero | 0 | not needed |
| 149 | 6 | positive, 6 | determinant zero | 0 | not needed |
| 151 | none | all 151 residues | all good | units | units |
| 157 | 5 | positive, 5 | determinant zero | 0 | not needed |
| 163 | 24 | positive, 24 | endpoint zero | 64 | 0 |
| 167 | 129 | negative, 37 | endpoint zero | 96 | 0 |
| 173 | 100 | negative, 72 | endpoint zero | 120 | 0 |
| 179 | 9 | positive, 9 | endpoint zero | 19 | 0 |
| 181 | 3 | positive, 3 | determinant zero | 0 | not needed |
| 191 | 141 | negative, 49 | endpoint zero | 177 | 0 |
| 193 | 116 | negative, 76 | determinant zero | 0 | not needed |
| 197 | 136 | negative, 60 | endpoint zero | 165 | 0 |
| 199 | 175 | negative, 23 | determinant zero | 0 | not needed |

An endpoint-zero witness has unit D, so the reviewed transfer implies
that the actual exponential endpoint is zero modulo p in that residue.
A determinant-zero witness is only a failure of the normalized determinant
unit test; it gives no actual numerator or higher-gcd conclusion.

## 2. Exact arithmetic and retained certificates

The engine is the one proved and described in
raw_second_predeclared_uniform_seed_list.md. For each background it
uses one (k+1)-square Appell Wronskian, solves its transposed system
when nonsingular, and obtains every normalized cofactor by


$$
C_i=(-1)^{i+k}D\,i!(k-i)!\,(W^{-1})_{ki}.
 \tag{1}
$$


The formula includes the omitted Vandermonde ratio. Its inverse row
is checked by exact multiplication. Each full determinant is also
checked independently by hook-product times Jacobi--Trudi.

Positive endpoints are checked through the exact polynomial identity
(t-1)^kR=(1+partial_t²)^k[t^kB(t)], including R(1)=D.
Negative finite functionals are cross-checked using a nonnegative
residue representative and finite differences of the border polynomial.
Every inverse denominator is checked to be a p-unit. A singular
determinant causes a witnessed stop, never an attempted inverse.

Run:

    /opt/homebrew/bin/python3.12 check_third_predeclared_uniform_seed_list.py

This imports the guarded exact engine from
check_second_predeclared_uniform_seed_list.py; importing does not
rerun the second list. Refactoring the engine behind that guard
preserved the second certificate's exact SHA-256 on rerun.

The new full output is
raw_third_predeclared_uniform_seed_certificate.json, with SHA-256

    0c5b654d5bdff206eb6cc66c88ba5850b1beca7c4d258690935a9a055b22a033

It retains all 488 successful-prime residue rows and the 17 first
bad witnesses, including their actual matrix and functional data.
The successful-prime findings have received the independent reviews
listed in the header.

## 3. Exact rational rate comparison

Combining the successful primes from the three closed lists with the
reviewed uniform three- and seven-adic results gives the candidate set


$$
{\cal P}=\{3,7,23,43,71,83,101,109,127,151\}.
 \tag{2}
$$


Define


$$
L=\frac32\log2+\sum_{p\in{\cal P}}\frac{\log p}{p-1},
 \qquad T=5\log\phi,\quad \phi=\frac{1+\sqrt5}{2}.
 \tag{3}
$$


The following are proved by an exact rational interval calculation:


$$
\boxed{2.421687921315<L<2.421687921316,}
$$




$$
\boxed{2.406059125298<T<2.406059125299,}
$$




$$
\boxed{0.015628796017<L-T<0.015628796018.}            \tag{4}
$$


There is no floating-point input to these enclosures.

The checker check_closed_uniform_seed_rate.py uses 24 terms of


$$
\log x=2\sum_{j=0}^{23}\frac{r^{2j+1}}{2j+1}
          +\mathrm{Tail},\qquad r=\frac{x-1}{x+1},
$$




$$
0\le\mathrm{Tail}\le
 \frac{2r^{49}}{49(1-r^2)}.
 \tag{5}
$$


Integer primes are divided by powers of two into [1,2), so
0<=r<=1/3. For phi it uses the rational bounds


$$
\frac{2236067977499789696}{10^{18}}<\sqrt5<
 \frac{2236067977499789697}{10^{18}},
$$


checked by squaring. All arithmetic, interval addition and outward
rounding to denominator 10^12 use exact rational numbers.
The complete rate output is raw_closed_uniform_seed_rate_certificate.json.
This certifies the numerical inequality separately from the seed
theorems and their independent reviews.

## 4. Proved all-even consequence

The independently checked successful-prime certificates in (2) and
reviewed transfers imply, for every n>=302,


$$
v_p(q_n)=v_p(Z_n)\ge v_p(n!)\qquad(p\in{\cal P}).    \tag{6}
$$


Indeed n>=2p is sufficient for every p>=7:
if m=floor(n/p)>=2, then
2n<2p(m+1)<p^m, by induction from 6p<p².
Thus floor(log_p(2n))<m<=v_p(n!).
The separately proved three-adic threshold is n>=9.

The exact dyadic theorem gives


$$
a_n=v_2(q_n)=n+2\left\lfloor\frac{n+2}{4}\right\rfloor.
$$


For even n, a_n>=3n/2. Since distinct prime powers combine without
overlap, (6) then gives the actual reduced-denominator divisor


$$
2^{a_n}\prod_{p\in{\cal P}}p^{v_p(n!)}\mid q_n.
 \tag{7}
$$


Write C_P=prod_(p in P)p. Legendre's digit formula yields


$$
v_p(n!)=\frac{n-s_p(n)}{p-1}
 \ge\frac{n}{p-1}-\log_p n-1.
$$


Consequently (7) proves the explicit lower bound


$$
\boxed{q_n\ge\frac{\exp(Ln)}{C_{\cal P}\,n^{10}}
       \qquad(n\ge302,\ n\ {\rm even}).}             \tag{8}
$$


This is the reduced q_n of the actual endpoint rational N_n/Z_n;
no unreduced cofactor denominator is substituted.

The independently accepted even relative-error theorem is


$$
(e+\pi)-\frac{N_n}{Z_n}
 =C_{\rm app}(-1)^{n/2}\rho^{5n}(1+o(1)),
 \quad C_{\rm app}>0,\quad\rho=\phi^{-1}.
 \tag{9}
$$


Its source is raw_even_endpoint_residue_asymptotic.md and full audit
raw_even_endpoint_residue_independent_review.md. If p_n/q_n is the
same rational in reduced positive-denominator form, (8)-(9) give


$$
|q_n(e+\pi)-p_n|
 \ge \frac{C_{\rm app}}{2C_{\cal P}}
       \frac{\exp((L-T)n)}{n^{10}}\longrightarrow\infty
 \quad(n\to\infty,\ n\ {\rm even}).
 \tag{10}
$$


The factor 1/2 applies after the asymptotic's unspecified finite prefix.
Equation (4) supplies a strictly positive exponent, independently of
that prefix.

Thus the actual raw primitive errors diverge along the entire
even-degree sequence, and no even-degree subsequence can shrink.
Integer multiples of those primitive forms cannot shrink either.

This conclusion is restricted to the even sequence because (9) is
the accepted even-degree asymptotic. No odd-degree signed-error
theorem is inferred, and nothing here proves or disproves the
irrationality of e+pi.
