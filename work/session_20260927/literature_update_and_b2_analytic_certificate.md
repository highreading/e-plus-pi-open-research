> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Primary-source update and a finite local certificate for the b=2 minor gate

Date: 2026-09-27. Bounded continuation by audit_sources.
Status: local mathematical lemma FULL PASS by root in two_local_lemmas_independent_root_review.md. The literature section is a scoped primary-source review, not a claimed exhaustive survey.
No new degree or prime scan. This note does not reopen the excluded raw family.

## 1. Archive delta and retained target

The relocated project was compared by SHA-256 against
work/session_20260913/inventory.json. All 4,765 entries remaining after removal
of AppleDouble names are present. The only changed old entry is a Python
bytecode cache. Outside the accepted September 13 session, the new substantive
files are its closing register, report and session index. No mathematical
file with a post-September-13 modification date was found before this resumed
session; the September 18 modifications are .DS_Store metadata. The detailed
delta is inventory_delta_from_20260913.json. This is a provenance observation,
not a re-audit of the old proofs.

I read CLOSING_VERIFICATION_REGISTER_20260913.md, the surviving-family portion
of the report, hp_auxiliary_simple_root_analytic_reduction.md and its root
review, and the final b=1/b=2 endpoint reductions. The b=2 large-prime gate is
the gcd of the maximal minors of



$$
M_n=\begin{pmatrix}
 H_n&J_n\\ J_{n+1}&K_{n+1}\\ K_{n+2}&M_{n+2}
 \end{pmatrix}.                                                   \tag{1}
$$



Here H,J,K,M have exactly the derivative normalization of
hp_b2_contiguous_endpoint_arithmetic.md. Its bound for the endpoint gcd of
the primitive full triple applies only at p>2n+4. The exact actual quotient
also contains second-kind and partial-exponential sums. Neither those
sums nor the final numerator cancellation is removed by (1).

## 2. Targeted primary literature, checked through September 27

This was a bounded search, not an exhaustive claim about all published
mathematics. Search-result crawl dates were not treated as publication dates.
The following are the strongest close statements located and inspected.

* [Delaygue, A Lindemann–Weierstrass theorem for E-functions,
  arXiv:2210.12046v2, 7 March 2025](https://arxiv.org/pdf/2210.12046):
  Theorem 1.2, PDF pp. 2–3, concerns E-functions whose transformed singularity
  sets are disjoint and whose selected values are transcendental. Corollary
  1.3 varies algebraic arguments. The logarithmic germ
  4 atan(z/(2-z)) has finite branch singularities, hence is not an entire
  E-function. Applying a coefficient factorial transform changes its endpoint
  value. These results therefore supply no endpoint-gcd bound here.

* [Adamczewski–Faverjon, Algebraic Independence Measures for Values of
  E-functions and M-functions, arXiv:2502.09999](https://arxiv.org/abs/2502.09999):
  the primary abstract and classification concern E-functions and Mahler
  functions. The M in this title means Mahler, not the fourth derivative
  combination in (1) or an arbitrary mixed exponential/logarithmic germ.
  No applicable quantitative endpoint-gcd statement was identified.

* [Fischler–Rivoal, Relations between values of arithmetic Gevrey series,
  JNT 261 (2024), 36–54](https://www.imo.universite-paris-saclay.fr/~stephane.fischler/ssmixte.pdf):
  Theorem 1 realizes G-values using E-values and renormalized Gevrey-1
  values. The mixed-value lifting theorem is Theorem 4, explicitly conditional
  on Conjecture 3 (§2, pp. 41–43). Its mixed functions are sums of an
  E-function and a Gevrey-1 series in 1/z; an arbitrary exponential plus
  logarithmic germ is not automatically such a function. This is neither an
  unconditional lifting theorem for our pair nor a gcd theorem.

* [Palojärvi, Explicit results for Euler's factorial series in arithmetic
  progressions under GRH, arXiv:2208.00294v3](https://arxiv.org/html/2208.00294v3):
  Theorem 2.1 requires nonzero integer arguments and a product condition on
  a set of primes. Theorems 2.2, 2.5 and 2.8 add RH/GRH and give existence
  of a prime or a prime in specified collections with a nonzero linear form.
  Our weighted auxiliary boundary uses arguments -(1+i)/2 and -(1-i)/2.
  The argument hypotheses and, independently, the specified-prime
  valuation conclusion do not match.

* [Chalebgwa–Rabenantoandro, Euler factorial-series talk slides](https://www.fields.utoronto.ca/talk-media/1/51/63/slides.pdf):
  slides 7–10 define the across-prime notion of infinite transcendence and
  state a Wronskian-rank conclusion at infinitely many primes. They explicitly
  distinguish this from a conclusion at a given prime. The author's
  [research list](https://sites.google.com/a/aims.ac.za/taboka/research-interests)
  labels the related paper as in preparation. This is a lead, not a verified
  fixed-prime theorem or a usable valuation estimate.

* [Ikonomov–Suetin, On Convergence of Rational Hermite–Padé Approximants,
  arXiv:2605.14760](https://arxiv.org/pdf/2605.14760):
  Theorems 1–2, PDF pp. 3–4, give convergence rates for the stated
  inverse-Zhukovsky model class. The approximation systems involve powers
  of one function. They do not identify our two distinct germs or control
  primitive endpoint denominators.

The earlier checked fraction-free HP and Mahler-duality identities remain
as recorded in literature_hp_dvr_content_and_obstruction.md. Their
nonunit determinant pivots cannot be deleted. I found no new primary
statement that changes that normalization issue.

## 3. Exact index interpolation of all four b=2 entries

Use the falling factorial (X)_r=X(X-1)...(X-r+1). For r>=0 put



$$
{\cal D}_r(X)=\sum_{b,c\ge0}
 \frac{(-1)^b}{2^c b!c!}(X)_{b+2c+r}(X)_{b+c}.             \tag{2}
$$



For each nonnegative integer n this series terminates and equals



$$
{\cal D}_r(n)=H_n^{(r)}(1),\qquad
 H_n(x)=n![z^n]e^{xz}(1-z+z^2/2)^n.                       \tag{3}
$$



Indeed the multinomial expansion first selects b linear and c quadratic
terms, while the r derivatives replace n!/(n-b-2c)! by
n!/(n-b-2c-r)!. Terms whose derivative degree is negative vanish by the
falling factorial. This includes r>n.

Fix any odd prime p and any integer a. On X=a+pY every series (2)
belongs to Z_p<Y>. Set R=b+2c, s=b+c, k=floor(R/p),
q=floor(s/p). The product (a+pY)_L contains at least floor(L/p)
factors in p Z_p[Y]. Also



$$
v_p(b!c!)\le v_p(s!)=q+v_p(q!).
$$



Thus each summand of (2) has Gauss valuation at least



$$
\lfloor(R+r)/p\rfloor+q-v_p(s!)
 \ge k-v_p(q!)\ge k-v_p(k!).                              \tag{4}
$$



The last quantity tends to infinity. This proves restricted analytic
convergence, not merely convergence on integer inputs.

For requested precision d>=1 choose



$$
K_d=\left\lceil \frac{d(p-1)}{p-2}\right\rceil.             \tag{5}
$$



Since v_p(k!)<=k/(p-1), deleting every term with R>=p K_d
changes (2) by an element of p^d Z_p<Y>, uniformly for every r.
This is an explicit finite polynomial truncation rule.

Define integral restricted analytic functions on each disk by



$$
{\cal H}={\cal D}_0,\quad
 {\cal J}=X{\cal D}_0+{\cal D}_1,
$$




$$
{\cal K}=X(X-1){\cal D}_0+2X{\cal D}_1+{\cal D}_2,
$$




$$
{\cal M}=X(X-1)(X-2){\cal D}_0+
 3X(X-1){\cal D}_1+3X{\cal D}_2+{\cal D}_3.                \tag{6}
$$



They interpolate the actual H,J,K,M. Form the three minors F_i(Y)
of the matrix (1), replacing n by a+pY and using (6) at the
appropriate shifts. These are elements of Z_p<Y>. Truncating (2)
according to (5) computes all F_i modulo p^d with no precision loss:
the remaining operations are additions and products of integral series.

## 4. A finite certificate criterion with an exact scope

For a fixed p and disk a+p Z_p, the following are equivalent:

1. The three analytic minors have no common zero in that disk.
2. Their minimum valuation is bounded on that disk.
3. There is a d>=1 such that for each y in Z/p^d Z at least one
   of the three explicitly truncated F_i(y) is nonzero modulo p^d.

Proof. Integral restricted series preserve congruences modulo p^d,
so (3) gives minimum valuation <d everywhere. If (1) holds, the
continuous nonnegative function max_i|F_i|_p has a positive minimum
on compact Z_p, proving (2). Conversely unbounded simultaneous
valuation gives a convergent subsequence in Z_p with a common zero.
Finally a uniform bound permits a sufficiently large d and proves (3).

In particular, a successful finite certificate yields the rigorous
all-index statement



$$
v_p\gcd(\text{maximal minors of }M_n)<d
 \quad(n\equiv a\pmod p).                                \tag{7}
$$



This is a stopping certificate, not a proof that the computation always
terminates successfully. A common p-adic zero is a genuine obstruction.
No such certificate is asserted to have been found here, and no new
residue enumeration was performed.

The lemma is stronger than reusing x-derivative nonvanishing as an index
derivative: it supplies the actual index-analytic functions and an
explicit coefficientwise precision. It is weaker than the desired
global arithmetic theorem. Fixed p only lies in the proved endpoint-gcd
range p>2n+4 for finitely many n; neither compactness nor (7) bounds
the constants uniformly as p grows. The actual reduced numerator
remains a separate object.

## 5. Concrete next certificate

If a structural identity makes one of the minors in (1) a unit modulo p
on every relevant disk, (7) gives the sharp bound zero at once. If only
joint residue zeros remain, use the finite truncation at d=2 to test
index slopes and compatibility; do not substitute the derivatives in
the variable x of H_n(x). An effective bound uniform in growing p,
or an identity linking these minors to the exact cleared numerator,
is the missing additional lemma needed for an endpoint conclusion.
