> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the $e+\pi$ research archive

Date: 2026-08-26 UTC

## Scope and verdict

This is a line-by-line mathematical and computational audit of the current
contents of e_pi_research_20260826. It specifically checked:

1. the continued-fraction denominator inequality;
2. the conditional $\mathbf E\cap\mathbf G$, Schanuel, and exponential-period
   implications;
3. the Lindemann--Weierstrass near-relation;
4. both endpoint-matched mixed Hermite--Padé systems, their normalization,
   exact finite vanishing orders, and analytic tail estimate;
5. the all-degree $2$-adic proof for the raw-arctangent bordered matrix;
6. the degree-$65$ counterexample to the tentative $239$-adic Machin
   endpoint pattern;
7. the interpretation and evidentiary status of the recent papers cited; and
8. reproducibility and machine-readable output integrity.

The archive's main conclusion is correct: it contains no proof that
$e+\pi$ is algebraic, irrational, or transcendental. Even irrationality
remains open. The unconditional results recorded here are finite exclusions,
one all-degree matrix-rank theorem for the raw-arctangent ansatz, and exact
diagnostics of particular auxiliary constructions. None settles the
arithmetic nature of $e+\pi$.

After the corrections listed below, I found no remaining mathematical gap in
the claims that the archive currently labels as proved. In particular, I
accept the all-degree raw-arctangent rank theorem and the exact degree-$65$
$239$-adic counterexample. The large external certificate attached to the
July 2026 repository preprint was not rerun and is not certified by this
audit.

## 1. Continued-fraction certificate

### Accepted argument

The script encloses $e$ by its factorial series and $\pi$ by Machin's
formula with alternating-series bounds, entirely in exact rational
arithmetic. The interval transformations used to extract common continued-
fraction digits correctly reverse the endpoints under reciprocation.

For the maximal current interval, the exact endpoints have 1180 common
partial quotients. At the terminal transformed interval, the endpoint floors
are $12$ and $14$, and the integer $13$ lies strictly inside. If a
reduced rational terminal tail is $u/v$, then $u/v>12$, so
$u\geq13$ and $v\geq1$. The inverse continued-fraction map has reduced
denominator



$$
q_{1179}u+q_{1178}v
$$



because its integer matrix is unimodular. The tail $13$ is inside the
terminal interval, so equality is attained there. Consequently, if
$e+\pi=P/Q$ in lowest terms, then



$$
Q\geq 13q_{1179}+q_{1178},
$$



the 600-digit integer displayed in research_log.md and
results/cf_maximal_current_interval.json.

The inequality is non-strict. It is a finite conditional denominator bound,
not an irrationality proof. The earlier 1000-digit certificate uses the
weaker adjacent-convergent/Farey bound $q_{999}+q_{998}$, which is also
valid.

### Corrections incorporated

The earlier name rational_denominator_strict_lower_bound was misleading and
has been replaced by rational_denominator_lower_bound. The current
1000-digit certificate records the terminal-tail state and no longer claims a
strict inequality.

## 2. Bounded algebraicity search

The exact search through degree $5$ and naive coefficient height $10$ is
valid. For each fixed nonconstant coefficient vector, the nearest permitted
constant coefficient minimizes the fixed-point residual. The uniform error
bound includes both rounding of every power and the exact rational interval
radius. A positive minimum gap larger than that error excludes every
polynomial in the stated finite box.

The counts



$$
20,\ 420,\ 8820,\ 185220,\ 3889620
$$



are the correct numbers of nonconstant coefficient vectors of exact degrees
$1,\ldots,5$. Nonzero constant polynomials are trivially excluded. The
separate PSLQ run is only a heuristic failure to find a relation and is
correctly labeled as such.

## 3. Conditional structural consequences

The following implications in the archive are correct and remain explicitly
conditional where required.

- At least one of $e+\pi$ and $e\pi$ is transcendental.
- Schanuel's conjecture applied to $1$ and $i\pi$ implies algebraic
  independence of $e$ and $\pi$, hence transcendence of $e+\pi$.
- If $s=e+\pi$ were algebraic, then
  $\overline{\mathbb Q}(e)=\overline{\mathbb Q}(\pi)$, the pair would have
  transcendence degree one, and $e\pi$ would be transcendental.
- Under the same hypothesis, the stated Lindemann--Weierstrass consequences
  for $\exp(ire)$, $\sin(re)$, and $\cos(re)$, for nonzero rational
  $r$, are valid.
- Nesterenko's algebraic independence of $\pi$ and $e^\pi$ correctly
  transfers to $e$ and $e^\pi$ under the algebraic translation
  $e=s-\pi$.
- If $s$ were algebraic, $e$ and $\exp(ie)$ would be algebraically
  independent: a polynomial relation expands into a forbidden algebraic
  linear relation among exponentials of the distinct algebraic exponents
  $m+nis$.
- Under the stronger hypothesis $s\in\mathbb Q$, the deduction that $e$
  and $e^e$ are algebraically independent is valid.

### The $\mathbf E\cap\mathbf G$ implication

The distinction between functions and values is handled correctly. Since
$e\in\mathbf E$, $\pi\in\mathbf G$, and both value rings contain
$\overline{\mathbb Q}$, algebraicity of $s$ would put both $e$ and
$\pi$ in $\mathbf E\cap\mathbf G$. Thus the standard conjecture



$$
\mathbf E\cap\mathbf G=\overline{\mathbb Q}
$$



implies transcendence of $e+\pi$. This is not a proved intersection
theorem. Fischler and Rivoal explicitly describe it as out of reach, and the
recent $p$-adic functional results cited do not specialize to the needed
complex values. The archive now correctly identifies the exponential example
in the Vargas--Montoya work as $\exp(\pi_pz)$ with a Dwork constant, not the
ordinary complex function $e^z$.

### Exponential periods

Fresán and Jossen's Proposition 12.1.4 was checked in the primary manuscript.
Conditional on their exponential period conjecture, the exponential of a
nonzero algebraic number is transcendental over the field generated by usual
periods. If $s$ were algebraic, then $e=s-\pi$ would be a usual period,
contradicting the proposition with exponent $1$. The archive correctly
states this as a conditional implication and does not confuse comparison
theorems for exponential-period rings with a proof of the conjecture.

## 4. Lindemann--Weierstrass near-relation

Assuming $s=e+\pi$ algebraic, the identity



$$
e^{is}=-e^{ie}
$$



and the forms



$$
L_N=e^{is}+\sum_{m=0}^{N}\frac{i^m}{m!}e^m
$$



are used correctly. The exponents $is,0,1,\ldots,N$ are distinct
algebraic numbers, so Lindemann--Weierstrass gives $L_N\ne0$. Taylor's
formula gives



$$
L_N=-\sum_{m>N}\frac{(ie)^m}{m!},
$$



and, for $N+2>e$, the geometric-ratio estimate



$$
0<|L_N|\leq
\frac{e^{N+1}}{(N+1)!}
\left(1-\frac e{N+2}\right)^{-1}
$$



is valid. Multiplication by $N!$ clears all rational coefficient
denominators, but the resulting upper bound is asymptotic to a growing
quantity of order $e^{N+1}/(N+1)$. Qualitative
Lindemann--Weierstrass therefore gives no contradiction.

## 5. Mixed Hermite--Padé systems

### Linear systems and endpoint normalization

For degree bound $n$, there are $3(n+1)$ polynomial coefficients. The
conditions through Taylor degree $3n$ impose $3n+1$ equations, and the
endpoint match imposes one more. Thus expected nullity is one. The endpoint
conditions are normalized correctly:

- for $F(z)=\arctan z$, $C(1)=4B(1)$ gives
  $R(1)=A(1)+B(1)(e+\pi)$;
- for $G(z)=16\arctan(z/5)-4\arctan(z/239)$, $C(1)=B(1)$ gives the same
  endpoint form.

After making the polynomial vector primitive over the integers, it is valid
to divide the two endpoint coefficients by their gcd even when that gcd does
not divide every polynomial coefficient. The irrationality-form
normalization only requires the final two endpoint coefficients to be
coprime integers.

The exact finite computation through $n=18$ verifies nullity one,
nonvanishing of the first unconstrained coefficient at index $3n+1$, and
therefore exact order $3n+1$, for all 36 displayed forms. This is a finite
statement; the all-degree raw rank theorem below does not by itself promote
the exact-order assertion to every $n$.

### Analytic tail bound

For odd $r$, the Machin coefficient satisfies



$$
|g_r|\leq\frac{20}{r5^r},
$$



and even coefficients vanish. If the coefficient height is at most $H$,
degrees are at most $d$, and $R(z)=O(z^M)$, then with $K=M-d\geq2$,



$$
|R(1)|\leq H(d+1)
\left(\frac{K+1}{K K!}+\frac{25}{K5^K}\right).
$$



This follows by summing the untouched exponential and Machin tails term by
term. For $M=3d+1$, the sufficient condition $H=o(5^{2d})$ is correct.
It is only a sufficient upper-bound criterion. Failure to prove that height
bound, or even proof that this particular absolute-value upper bound does not
tend to zero, would not give a lower bound for the actual endpoint form,
because cancellation remains possible.

The direct Taylor-subtraction obstruction is also correct after being labeled
as asymptotic: after $N!$-normalization the arctangent remainder dominates
and the forms diverge for all sufficiently large $N$. It is not an all-
construction no-go theorem.

## 6. All-degree raw-arctangent bordered rank theorem

I accept the theorem in sources/raw_arctan_bordered_rank_proof.md:
for every $m\geq1$, the $(2m-1)$-by-$2m$ raw-arctangent bordered matrix
$D_m$ has full row rank over $\mathbb Q$. The same argument works for any
rational value in the constant $B$-block of the endpoint row.

The audit checked the following points independently.

1. Each jet row of $D_m$ is $k!$ times the coefficient equation for
   $B(z)e^z+C(z)\arctan z$, so division by $k!$ preserves the kernel and
   rank.
2. Rank failure would make the kernel at least two-dimensional. Intersecting
   it with $B(1)=0$ gives a nonzero vector; the endpoint equation then gives
   $C(1)=0$. Factoring both polynomials by $z-1$ produces exactly the
   $2\ell$-by-$2\ell$ matrix $T_\ell$, with $\ell=m-1$, row range
   $\ell+1,\ldots,3\ell$, and the entries stated in equation (1).
3. The exponential-minor determinant formula involving
   $V(S)\Lambda(W_S)$ is exact. The factorial-valuation maximizing sets are
   exactly $S_0$ and $S_*$.
4. The incidence-matrix identity (11a) has the stated sign and introduces no
   division. After parity permutations, the nonzero arctangent entries split
   into the asserted square and bordered Cauchy blocks.
5. The bordered-Cauchy formula (14a), its valuation (15), the factorial-moment
   parity statement (16), and the mod-$4$ equality case (17) are correct.
   The exponential generating function and recurrence used for (17) were
   checked coefficient by coefficient.
6. For even $\ell$, $S_0$ is the unique least-valuation Laplace term; for
   odd $\ell$, $S_*$ is. The candidate complements have the required
   consecutive parity rows in both cases. A finite sum in $\mathbb Q_2$
   with a unique least-valuation term cannot cancel to zero.

One parity statement was corrected during the audit:
$\Lambda(W_{S_*})\equiv\ell\pmod2$, not $1\pmod2$ for every $\ell$.
The proof only needs this factor to be odd for odd $\ell$, so the corrected
formula preserves the theorem and strengthens the even-$\ell$ comparison.

The theorem proves full row rank, hence a one-dimensional kernel for the
reduced raw system. It does **not** prove any of the following:

- exact vanishing order $3n+1$ for every degree;
- nonvanishing of $A(1)+B(1)(e+\pi)$;
- a useful endpoint-primitive height bound;
- Archimedean smallness after integer normalization; or
- all-degree rank for the separate Machin endpoint-matched system.

These distinctions are stated correctly in the current research log.

## 7. Exact degree-$65$ $239$-adic counterexample

I accept sources/machin_239_endpoint_audit.md and independently reran
scripts/machin_239_counterexample.py.

For $p=239$ and $n=65$, the bordered determinants have sizes
$2n+2=132$. The jet range $n+1,\ldots,3n$ has $2n$ rows; the endpoint
row and the appended $A$- or $B$-functional supply the remaining two.
Because $3n=195<p$, every factorial denominator and every odd Taylor index
involved is a $p$-unit.

The $p$-power row and column potentials sum to $8515$ for $\Delta_B$
and $8580$ for $\Delta_A$, and every scaled matrix entry is
$p$-integral. Let $M_B$ and $M_A$ denote the resulting scaled square
matrices. Exact modular elimination gives



$$
\operatorname{rank}_{\mathbb F_{239}}(M_B)=131,\qquad
\det M_B=p^{8515}\Delta_B\equiv239\cdot121\pmod{239^2},
$$



and



$$
\det M_A=p^{8580}\Delta_A\equiv181\pmod{239}.
$$



Therefore



$$
\nu_{239}(\Delta_B)=-8514,\qquad
\nu_{239}(\Delta_A)=-8580,\qquad
\nu_{239}\!\left(\frac{B(1)}{A(1)}\right)=66.
$$



After endpoint-gcd normalization, this gives



$$
\nu_{239}(A_{\rm end})=0,\qquad
\nu_{239}(B_{\rm end})=66,
$$



not the largest odd integer at most $65$, which is $65$. The recurrence
for the leading residue has no zero modulo $239$ for $1\leq m<65$ and
does vanish at $m=65$; the executable script now asserts that finite claim.

This is a counterexample to a tempting extrapolation from degrees
$1,\ldots,18$, not a counterexample to the Hermite--Padé construction and
not a no-go theorem. It also correctly illustrates why a $p$-adic height
lower bound would not be an Archimedean lower bound for the endpoint linear
form.

## 8. Literature and citation audit

- Waldschmidt's *Transcendence of Periods: The State of the Art*, PDF page
  79, explicitly lists $e+\pi$ and $e\pi$ as unknown. This is the direct
  established-status citation now used in the archive.
- Yu's June 2026 arXiv preprint explicitly states that even irrationality is
  open. Its eventual ceiling recurrence was checked and is an exact criterion
  for the rational subcase, not a finite certificate.
- Yu's July 2026 University of Alabama item is a repository preprint. Its
  stated result concerns ordinary diagonal normality for $1,e^z,G(z)$, not
  endpoint matching, coefficient heights, or small nonzero values at $z=1$.
  The archive now says that the manuscript *reports* a computer-assisted
  theorem and expressly records that its roughly 36-billion-inequality
  external certificate was not independently rerun here.
- The cited Fischler--Rivoal, Fresán--Jossen, Gallinaro, and
  Commelin--Habegger--Huber references support the limited claims assigned to
  them.
- The audits of the two Carella manuscripts identify genuine fatal gaps. The
  2017 manuscript claims only the product result and leaves the sum open; the
  2020 manuscript's universal irrationality claim is refuted by
  $\alpha=4-\pi$, and its sine inequality is zero under its own contradiction
  hypothesis. The current revision-date wording is accurate.
- DOI 10.1112/blms.70158 is **not** evidence about $e+\pi$. Crossref
  identifies it as Alsulami--Jackson, *Finite models for positive combinatorial
  and exponential algebra*. It is not used in the archive.

## 9. Computational reproducibility

All result files currently pass python -m json.tool; all scripts pass
python -m py_compile. Earlier trailing plain-text SHA256 lines made the files
invalid JSON. Those footers were removed and the generators now emit pure
JSON.

The principal generators were rerun outside the archive, and the generated
files matched the Drive files byte for byte. Current whole-file SHA-256
digests are:

| Result | SHA-256 | Recheck |
|---|---|---|
| bounded_d5_h10_and_pslq.json | b589387efabb69369c57ba9819dabec9cbb06846004968f8532e1a089586bc62 | full rerun |
| cf_1000_certificate.json | 42c1d835d95273fb6e8f62e59a6dba1c30ec07151551a210f503eaa3f6301b0c | full rerun |
| cf_maximal_current_interval.json | 5b55cdb6ed04362cee5ad4e4d9ca2678ccbb670f9eedab70a08aac1c0a3fee9c | full rerun |
| constrained_rank_n60.json | 09857952a242490f9f7c5a2b062d72d5396906aaa16d55d7683f1cd12647316b | full rerun |
| mixed_hermite_pade_n12.json | d770e44b20bffd866afe1ad98222425c703cd32c78d9b32de1323472b760b55e | full rerun |
| mixed_hermite_pade_n18.json | fc0e8d85f822179ce7f1efea3f90b1fee806998c0740358e563e7d3e50b14aa3 | full rerun |
| raw_arctan_rank_crosscheck_ell6.json | a9e12a47cd1879410fd71ba5db91e4778ed30fd25b8a1fa83878e6909ef9a328 | full rerun |
| raw_arctan_rank_crosscheck_ell7.json | 33ea2b6adc0fd0244f561d5766dedb0bc3dac4b09ff67ba9eac120195f9675a4 | full rerun |

The degree-$65$ Machin script was also rerun; it reproduced the residues
and valuations quoted in Section 7. It uses exact integer arithmetic modulo
$239$ and $239^2$, not floating point.

## 10. Exact remaining open obligations

No accepted theorem in the archive supplies an algebraic relation for
$e+\pi$, and no accepted theorem proves it transcendental. The constructive
Hermite--Padé route would still require, for an all-degree endpoint-matched
family relevant to $e+\pi$:

1. all-degree existence/nondegeneracy for the chosen family (the new theorem
   supplies this only for the raw-arctangent family, not the Machin family);
2. control of the first unconstrained coefficient if exact vanishing order is
   needed;
3. a uniform endpoint-primitive height or denominator bound after rational
   normalization;
4. a sufficiently small evaluated form at $z=1$ after that normalization;
5. a proof that the evaluated form is nonzero; and
6. enough arithmetic discreteness to turn the small nonzero value into a
   contradiction under a rationality or algebraicity hypothesis.

For a proof of algebraicity, one ultimately needs an exact nonzero polynomial
$P\in\mathbb Z[T]$ with $P(e+\pi)=0$, an equivalent exact identity, or a
proved eventual all-index arithmetic criterion. Finite continued fractions,
finite PSLQ searches, finite rank checks, and finite valuation patterns cannot
provide that conclusion by themselves.

Accordingly, the research program has produced several rigorous subsidiary
results and eliminated specific flawed routes, but the user's requested proof
has not been completed and must not be represented as completed.
