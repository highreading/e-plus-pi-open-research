> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Primary review of three related claimed solutions

Reviewer: main Codex. Date: October 4, 2026. The judgments in this note were not delegated to subagents. Complete extracted texts of the two pinned Carella manuscripts were read, with decisive formulas also checked on the original PDF pages. Foukzon's definitions, example, and main statements were checked on the original pages. This note judges only the specific propositions below and does not claim page-by-page review of its 139-page nonstandard-analysis framework.

These three sources cannot establish that e+π has been resolved. The rejections below concern specific arguments or auxiliary claims. This note proves neither rationality of e+π nor rationality of eπ.

## 1. Carella 2007.15000v3

[Pinned original](https://arxiv.org/pdf/2007.15000v3), 23 pages, SHA-256 `7f8ef62350816b8124c40f326909952bab713dd3c4ef6d38eb90632860a0d735`. The earlier local `sources/literature_status.md` already listed the first three issues. They were confirmed directly against the original here and are not presented as new research results.

Theorem 4.1 on PDF page 7 claims that the sum of any positive irrational α with π is irrational. Take α=4−π. Since π<4 and π is irrational, α meets every condition, but α+π=4. This auxiliary proposition is explicitly false.

The proof of (4.2) on the same page uses |sin(A−Bα)|>0 under the contradiction assumption α+π=A/B. That assumption gives A−Bα=Bπ, whose sine is zero. Comparison with the sine of a small nonzero convergent error cannot yield the required lower bound. The version substituting α=e on page 8 repeats this defect.

Equation (6.8) on page 12 further lower-bounds `1/(2q_next) − π/(2q)` by `1/(2q_next)`, dropping a strictly negative term. The preceding lattice-proximity argument therefore does not establish nonvanishing. Proximity alone also cannot replace the required arithmetic separation.

Section 9 on page 16 uses a lemma asserting sin(eB+A)≠0. That assertion itself excludes eB+A being an integer multiple of π, precisely the integer relation at issue; the preceding lattice argument does not establish it independently. The nonvanishing lemma for eπ on page 18 is likewise unsupported by its cited object. The main theorem and related e+π/eπ corollaries cannot be adopted from these steps. The first-page claim is also stronger than the integer-coefficient scope handled in the body and cannot be promoted automatically from an integer contradiction.

Sections 2–3 combine hypotheses from different cases and treat an assumed transcendental number as having a minimal polynomial. This does not establish a nonzero algebraic equation for that number. Variable elimination requires proving that the same hypotheses hold simultaneously, that the eliminant is nonzero, and that its coefficients lie in the asserted field.

Some elementary parts remain independently usable. The geometric-series identity for finite exponential sums is correct, and its Cesàro limit detects angles in 2πZ. For rational α, retain the quantifier that some integer multiple mα is integral. I(2πα) itself does not send every rational to 1: for α=1/2, the alternating-sum limit is 0.

The all-index lower bound in Lemma 15.4(ii) on page 22 also has an exception. The golden ratio φ=(1+√5)/2 has convergent 5/3 and next partial quotient 1. Since 20/9<√5<7/3,



$$
0<5/3-\varphi=(7-3\sqrt5)/6<1/18=1/(2\cdot1\cdot3^2).
$$



The stated lower bound therefore does not apply unconditionally to all partial quotients. The usual valid conservative lower bound uses a_next+2 rather than 2a_next here.

Linear independence of distinct nonnegative integer powers of π and transcendence of π+π² follow directly from transcendence of π. A contrary relation makes π a root of a nonzero polynomial with algebraic coefficients; transitivity of algebraicity gives a contradiction. These facts require no sine test from this manuscript and are not new open conjectures.

Exact Machin intervals and factorial-series intervals for e confirm the first four partial quotients of e+π as [5;1,6,7], with fourth convergent 293/50. Table 2 on page 10 instead gives 47/8, which is not the fourth convergent of this sequence; another table on page 17 writes the corresponding numerator as 93. Finite data do not prove irrationality, and incorrect data cannot support a proof either.

## 2. Carella 1706.08394v7

[Pinned original](https://arxiv.org/pdf/1706.08394v7), 10 pages, SHA-256 `84f783c4c00cf18f71df81af2763248ec169126f32e3a2d70b65485e6a9fefe2`. The earlier local register already identified the gap in the denominator-synchronization lemma. Checking PDF pages 5–8 confirms it.

Lemma 3.1 adds a subsequence of specified asymptotic size to a partial-quotient upper-bound assumption, then infers infinitely many denominators from one satisfying an interval condition. Neither step is justified. The three partial-quotient growth cases also fail to cover every possible sequence for π. Thus the infinite selection of required convergents in (4.5) is not guaranteed, and a successful finite search cannot supply it.

Strictly positive error in Theorem 2.4 on page 3 also does not follow from two distinct irrational numbers whose product is not ±1. Take



$$
\alpha=\sqrt2,\qquad\beta=9/(4\sqrt2).
$$



These numbers are distinct positive irrationals with product 9/4. From 7/5<√2<3/2, α begins [1;2] and has convergent 3/2. From 27/20<√2<3/2, one has 3/2<β<5/3; β begins [1;1,1] and also has convergent 3/2. The product of these two convergents is already 9/4, so the claimed strictly positive error is zero.

A non-strict upper bound on product error survives a correct absolute-value estimate. Applying rational-spacing lower bounds additionally requires proving that the compared rationals differ. Neither this requirement nor infinite denominator synchronization can be omitted. These general counterexamples do not establish rationality of eπ.

## 3. Foukzon 0907.0467v14: an explicit recursive counterexample

[Pinned original](https://arxiv.org/pdf/0907.0467v14), 139 pages, SHA-256 `eebf1047fcbfbfbc05fca8b4c873cb7288f11a2a80b85309162513b032d5ff9a`. Definitions on page 2 and Example 1.2 / Theorems 1.3 and 1.8 on page 3 were checked on the original pages. The construction below uses no nonstandard analysis, axiom extensions, or undecidable real-number tests.

Set M_n=20n+20 and define, using finite rational operations only,



$$
E_n=\sum_{j=0}^{M_n}1/j!,\quad
\widehat r_{n-1}=1-\sum_{k=1}^{n-1}v_k E_n^k,\quad
v_n=\frac{\widehat r_{n-1}-1/(2n!)}{E_n^n}.
\tag{A}
$$



The empty sum is zero, so the first step is fully specified. Each step uses only factorials, finite sums, integer powers, and rational arithmetic, with loop counts explicitly bounded by n. Numerator and positive-denominator encodings can therefore be produced by primitive recursive operations. There is no unbounded search based on an unknown decimal digit of e.

Let the actual remainder be r_n=1−Σ_{k=1}^n v_k e^k, with r_0=1. We prove for every n≥1 that



$$
0<v_n<\frac1{2^n(n-1)!},\qquad
\frac1{3n!}<r_n<\frac1{2n!}.
\tag{B}
$$



First set δ_n=e−E_n. A geometric bound on the factorial tail gives



$$
0<\delta_n<\frac2{(M_n+1)!}
<\frac1{1000\,n!\,n^2 3^n},\qquad 2<E_n<e<3.
\tag{C}
$$



The second inequality can be checked entirely with integers: `(M_n+1)!/n! ≥ 2^(19n+21)`, while `1000 n²3^n < 2^(4n+10)`.

Assume the preceding v_k are positive and at most 1. The difference-quotient bound for powers gives



$$
0\le\Delta_r:=\widehat r_{n-1}-r_{n-1}
\le\delta_n n^2 3^n,\qquad
0<\Delta_p:=e^n-E_n^n\le\delta_n n3^n.
$$



At n=1, $\widehat r_0=1>1/2$. At n≥2, induction gives $r_{n-1}>1/[3(n-1)!]>1/(2n!)$, so the numerator in (A) is positive. Every earlier coefficient is positive, hence $\widehat r_{n-1}\le1$ and 0<v_n<1. Exact substitution yields



$$
r_n=\frac1{2n!}-\Delta_r-v_n\Delta_p.
$$



The total loss is therefore less than $2\delta_n n^2 3^n<1/(500n!)$, giving the remainder bound in (B). For n≥2, $\widehat r_{n-1}<1/[2(n-1)!]+1/(1000n!)<1/(n-1)!$; the required upper bound also holds at n=1. Dividing by E_n^n>2^n gives the coefficient bound in (B), completing the all-index induction.

Consequently,



$$
f(z)=1-\sum_{n=1}^{\infty}v_nz^n
$$



This is a nonzero entire function: its constant term is 1, and (B) bounds its coefficients by a factorial series. Its coefficients are primitive recursive rationals, and r_n→0 gives exactly f(e)=0. It meets every remainder condition in Example 1.2, directly refuting the assertion that such a sequence is nonrecursive and contradicting Theorem 1.3 under the stated definition.

For Theorem 1.8, take f_n(z)=z−n, with unique root β_(1,n)=n, and a_0=1, a_n=−v_n. All roots are distinct positive integers. The coefficients are nonzero primitive recursive rationals, and absolute convergence is ensured by



$$
\sum_{n\ge1}|a_n|e^n=1
$$



Yet $a_0+\sum a_ne^n=0$. The counterexample does not even rely on repeated polynomial roots. This infinite-family statement cannot be used as an extension of the ordinary Lindemann–Weierstrass theorem.

This suffices to reject these foundational statements as project inputs without accepting or refuting every subsequent nonstandard-analysis definition in the 139 pages. It does not affect the classical finite-family Lindemann–Weierstrass theorem and proves neither rationality nor irrationality of e+π.

## 4. Evidence and limitations

`EXTERNAL_CLAIM_MAIN_CONTROLS.json` records the primary agent's checks: exact rational intervals for the first four convergents of e+π, positivity/factorial bounds for the first six coefficients in (A), and strict intervals for the actual remainders. These computations are bounded normalization checks only. The all-index justification for the Foukzon counterexample is the induction above.

Searches and local literal matching avoid duplicate work but cannot establish absence of similar constructions throughout the internet. No historical priority claim is made for this counterexample.
