> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Averaged arithmetic route: fixed-prime slices, finite-log zero bounds, and multiplicity — 2026-09-13

Status: rigorous reductions and primary-source applicability audit; no actual distribution estimate proved, no booking, no conclusion on e+pi.

## Main finding

Averaging the global index changes the useful question. For the actual ordinary-j2 carrier, it is enough to prove that **for one prime p, only o(p) of its admissible parameter rows collide**. Summing over primes then proves that the fixed-global-index collision weight is o(M) for almost all M. This removes the need to control a prescribed singleton at each prime on one fixed-M slice. Finite-logarithm and truncated-hypergeometric zero bounds are therefore more relevant to an averaged strategy than the older fixed-M obstruction discussion suggests.

The missing step is concrete: the currently known formulas give a moving truncation/parameter evaluated at a fixed argument. Existing theorems count zeros in the argument of one fixed polynomial for that prime. A transformation between those two problems, retaining the original joint target, has not been proved.

For the Item427 ordinary rank-zero Witt component, an analogous first-prime zero bound must be paired with a multiplicity moment bound. Fixed-layer sparsity alone cannot control the entire infinite valuation tail. The second-moment criterion below states a precise sufficient extra theorem.

## 1. Exact fixed-prime to almost-all-index lemma for Item334

Assume the exact identities of the archived `sources/item334_j2_coupled_cartier_carrier_report.md`. The actual rows satisfy



$$
p=2r+6s+3,\quad r\ge1\text{ odd},\quad3\nmid r,\quad s\ge1,
\qquad2M=5r+14s+7.
$$



Let $T_0(r,s),T_1(r,s)$ be the actual cleared coordinate residuals of that report. Their denominators are p-units on admissible rows. Define



$$
\chi(p,r,s)=1_{\{T_0(r,s)=T_1(r,s)=0\pmod p\}}.
$$



For a fixed p, define the actual row count



$$
Z(p)=\sum_{\substack{r,s\text{ admissible}\\2r+6s+3=p}}\chi(p,r,s).
\tag{A1}
$$



The fixed-global-index collision weight is



$$
W(M)=\sum_{\substack{r,s\text{ admissible}\\5r+14s+7=2M\,,\,p=2r+6s+3\text{ prime}}}
\chi(p,r,s)\log p.
\tag{A2}
$$



The exact inverse coordinates are



$$
r=6M-7p,\qquad s=\frac{5p-4M-1}{2}.
\tag{A3}
$$



In particular, p determines at most one row on each M, and



$$
\frac45M<p<\frac67M.
\tag{A4}
$$



Conversely, at fixed p increasing M by one changes (r,s) by (6,-2). Thus averaging M traverses a genuine one-parameter family at each prime, of length O(p); it no longer selects only one preassigned point.

**Lemma A.** If



$$
\sum_{p\le Y}Z(p)\log p=o(Y^2),
\tag{A5}
$$



then



$$
\sum_{X<M\le2X}W(M)=o(X^2).
\tag{A6}
$$



Consequently, for every fixed epsilon>0, only o(X) integers M in (X,2X] satisfy W(M)>epsilon M. Equivalently, W(M)/M tends to zero in natural density. A density-one subsequence on which W(M)=o(M) can be chosen by the usual diagonal selection.

**Proof.** All summands are nonnegative. Exchange the order of summation in (A2). By (A4), every contributing prime is below 12X/7, and each counted row contributes once. Hence



$$
\sum_{X<M\le2X}W(M)
\le\sum_{p\le12X/7}Z(p)\log p=o(X^2).
$$



If W(M)>epsilon M on a set E in the block, its contribution is at least epsilon X|E|. Thus |E|=o(X). Summing dyadic blocks, after discarding finitely many initial blocks, gives the natural-density formulation. This proves the lemma.

A simple sufficient hypothesis for (A5) is Z(p)=o(p), uniformly as primes grow. Indeed Chebyshev's bound sum_{p<=Y} log p=O(Y) implies sum_{p<=Y}p log p=O(Y^2), and the finitely many initial primes contribute o(Y^2). The weighted averaged condition (A5) is strictly weaker than requiring a bound at every prime.

**Quantitative form.** If Z(p)<=C p^(1-delta) for some 0<delta<1, then



$$
\sum_{X<M\le2X}W(M)\ll X^{2-\delta}.
\tag{A7}
$$



In particular W(M)<=X^(1-delta/2) outside O(X^(1-delta/2)) indices in the block. No equidistribution or independence between different primes is used anywhere in this reduction.

This is a component upper estimate, not a content lower bound. A proved instance would remove the ordinary-j2 collision component on almost all indices; its maximum normalized scope remains 1/105. The conclusion helps an irrationality construction only if combined with a correctly normalized **lower** gain estimate at the same indices. It does not itself book a positive divisor or close the overall deficit.

## 2. A precise bridge that would make a known finite-log theorem applicable

For p fixed, let the parameter be any injective affine encoding x of the admissible s rows. To apply a root theorem it would suffice to prove the following weaker implication, rather than a complete evaluation:

> Outside o(p) exceptional rows, every actual simultaneous collision forces one of at most B equations
> $L_p(a_jx+b_j)+H_{p,j}(a_jx+b_j)=0$, where B is fixed, each a_j is nonzero, and the maximum degree of H_{p,j} is o(p), uniformly in j and p.

Here $L_p(X)=\sum_{i=1}^{p-1}X^i/i$. The affine maps are bijections on the field, so the number of collision rows is bounded by the sum of the root counts plus the exceptional rows. The implication must hold for the full original collision and include degenerate charts, or those charts must receive a separate o(p) estimate.

**Relevant exact primary theorem.** Chen and Winterhof, *Interpolation of Fermat quotients*, Lemma 2, bound the number of roots of L_p+H, with deg H<=d and 1<=d<p, by



$$
\ll \begin{cases}d^{1/2}p^{2/3},&d\le p^{1/3},\\
d^{1/4}p^{3/4},&d>p^{1/3}.
\end{cases}
$$



Their Theorem 1 bounds coincidences q_p(u)=P(u) on the canonical representatives 1<=u<p by d^(1/4)p^(5/6) in the first range and d^(1/8)p^(7/8) in the second. Thus sublinear perturbation degree is sufficient for o(p) in both versions; fixed degree is not necessary. The Fermat-quotient version additionally needs the canonical integer lift of u, since q_p(u) is not a function of the residue class alone. [Author manuscript, Lemma 2 and Theorem 1](https://www.sfb-qmc.jku.at/fileadmin/publications/Winter-Chen-interpolation_Fermat.pdf); [published article](https://doi.org/10.1137/130907951).

These theorems do not cover an arbitrary sum of many finite logarithms, a determinant of endpoint moments, or an affine target whose interpolation degree is proportional to p. In Item334, the exact scalar is the incomplete binomial period H_(s-1) together with a determinant gate and a moving target; no formula of the required form in the index s has been established. The variable of the existing generating polynomial is an auxiliary argument, while s controls truncation length and r=(p-6s-3)/2 controls its parameters. Relabelling s as that argument is invalid.

The fresh concrete research step is therefore an **index-to-argument transformation** for the actual coupled gate or a Stepanov construction directly in the index variable. Before developing a full auxiliary-function argument, derive the discrete derivative/shift equations of the actual pair along (r,s)->(r+6,s-2) at fixed p and determine whether a low-complexity algebraic-independence/nonvanishing lemma can be established. Finite order alone is insufficient; the proof must quantify auxiliary degree and nonvanishing in characteristic p.

## 3. Other finite-field primary theorems and their scope

Ghosh and Ward's *The number of roots of polynomials of large degree in a prime field* treats natural truncations of fixed analytic functions. Its Theorem 1 gives O_k(p/log p) zeros for the finite polylogarithm of fixed order k>=2; Theorem 2 gives O_k(p/sqrt(log p)) for the stated polyexponential truncations. Their proofs require controlled differential identities and a nonvanishing theorem for auxiliary polynomials involving the function and its derivatives. A bound o(p), even without a power saving, would suffice in Lemma A. Neither theorem directly counts zeros while truncation length/parameters vary at one fixed evaluation point. The constants depend on the fixed order; letting k grow with Witt depth is not licensed. [Primary preprint](https://arxiv.org/pdf/1210.1893).

Their later paper develops O(p^(11/12)) root estimates for specified truncated hypergeometric families; again these count field arguments of one polynomial at a fixed prime. This is relevant as a method for the missing transformation but not an immediate theorem for the Item334 row index. The 2016 preprint's current v2 was located, but intermittent extraction errors prevented a complete hypothesis audit of that version during this bounded search; do not book any result from its abstract alone. [Primary record](https://arxiv.org/abs/1601.06765); [v2 PDF](https://arxiv.org/pdf/1601.06765v2).

The existing archive's conductor barriers concern specified Kummer or character-sum realizations. A Stepanov method does not automatically inherit every such geometric obstruction: it has its own auxiliary-degree and nonvanishing requirements. This makes it a distinct candidate method worth testing at fixed p. It does not eliminate the need to retain the moving target.

## 4. The higher-Witt component needs both rarity and a moment bound

Item427, still marked work-only/unaudited in the project, proposes the exact identity



$$
d_{m,p}=v_p(c_m)-b_{m,p}
=\min(v_p(\mathcal K_{m,p}),1+v_p(\mathcal X_{m,p})),
$$



on ordinary rank-zero rows p in P_m with p^2>4m+1. Here K=A_m/p and X=8B_m/p^2 are integral at p. Conditional on that identity, define the higher-layer weight



$$
H(m)=\sum_{\substack{p\in P_m\\p^2>4m+1}}(d_{m,p}-1)_+\log p.
\tag{W1}
$$



This is exactly sum_{n>=2} log R_n(m), with the old baseline and first layer removed.

For a dyadic m block define the weighted rare-row count and quadratic valuation moment



$$
A(X)=\sum_{X<m\le2X}\sum_{p\text{ in the stated scope}}1_{d_{m,p}\ge2}\log p,
$$




$$
B(X)=\sum_{X<m\le2X}\sum_{p\text{ in the stated scope}}d_{m,p}^2\log p.
\tag{W2}
$$



**Lemma B.** If A(X)=o(X^2) and B(X)=O(X^2), then



$$
\sum_{X<m\le2X}H(m)=o(X^2),
\tag{W3}
$$



and hence H(m)=o(m) in density, with a density-one subsequence as in Lemma A.

**Proof.** Use (d-1)_+<=d 1_{d>=2} and apply Cauchy–Schwarz to the finite weighted incidence set, with weights log p:



$$
\sum H(m)\le\sqrt{\left(\sum d^2\log p\right)
\left(\sum1_{d\ge2}\log p\right)}=\sqrt{B(X)A(X)}=o(X^2).
$$



The set is finite because p<=6m in this component, and d is finite whenever the defining nonzero integer pair is well-defined. The finitely many exceptional early m are irrelevant. Markov's inequality gives the density statement.

A sufficient concrete fixed-prime estimate for A(X) is, uniformly over relevant primes,



$$
\#\{X<m\le2X:p\in P_m,\ p^2>4m+1,\ d_{m,p}\ge2\}
\ll (X/p+1)p^{1-\delta}
\tag{W4}
$$



for some delta>0. Since p<=12X in the block, weighted prime summation yields A(X)<<X^(2-delta). Combined with the quadratic moment, this gives sum H(m)<<X^(2-delta/2). A similar bound for the larger event kappa_0=0 would also suffice for (W4).

The factor X/p+1 in (W4) describes what a root-count theorem on successive p-sized m intervals could deliver. **Periodicity of the actual Witt gate modulo p has not been proved.** In particular, m->m+p changes the quotient exponents in the Bockstein rational function, so an unproved periodicity assumption cannot be used to repeat one field count. A valid argument must establish the relevant reduction separately and uniformly for every interval/quotient parameter.

The quadratic moment B(X)=O(X^2) is a separate missing arithmetic lemma. Generic coefficient height only bounds an individual valuation by O(m/log p), far too weak to turn first-layer rarity into (W3). A promising way to seek the moment is a uniform Hensel-root or p-adic nondegeneracy theorem for the actual paired determinant functions; any repeated-root strata must be included. The tiny p^2<=4m+1 omitted tail has small radical but is **not** bounded in arbitrary multiplicity by either lemma.

An alternative to the second moment is uniform integrability of depth: fixed-level average sparsity plus a bound making the average tail sum (d-K)_+ log p negligible as K->infinity. This is mathematically weaker than a uniform depth cap but still requires a proof; one cannot interchange the infinite layer sum and a limiting estimate without it.

## 5. Why currently known gcd theorems do not fill these hypotheses

Grieve and Wang's moving-target gcd theorem (Theorem 1.2) uses one fixed number field, one fixed finite set S, a fixed number of S-unit arguments, polynomial degrees independent of the index, coprime target polynomials with a nonzero constant term, and target heights little-o of argument height. Its alternative is a small-gcd infinite subset or a multiplicative exceptional relation; the general statement is not an almost-all-index theorem. Their recurrence applications concern exponential polynomials sum_i f_i(n)alpha_i^n, namely constant-coefficient linear recurrences. [Primary paper, Theorem 1.2 and recurrence definition](https://arxiv.org/pdf/1902.09109); [published version](https://doi.org/10.1090/tran/8220).

The Item334 and Item427 formulas have factorial/binomial and moving denominator support and are holonomic, with polynomial coefficients depending on the index. They have not been expressed as the fixed-S-unit, fixed-degree, small-target-height objects required above. A P-recursive identity does not imply a constant-coefficient exponential-polynomial representation. Taking S to contain all primes up to the current index violates the fixed-S hypothesis. Encoding the whole endpoint as a moving polynomial coefficient makes the small-height condition the very unproved arithmetic estimate. Therefore no cited gcd theorem presently proves A5, W4, or the moment bound.

A recent alternative also does not give a free bound: Yasufuku (2026), Theorem 1.2, proves a codimension-two gcd inequality for a fixed complete intersection avoiding the coordinate points, outside a proper Zariski-closed exceptional set. Its right side includes an outside-S coordinate contribution in addition to a positive height multiple. Remark 3.6 explicitly explains the resulting near-S-unit requirement. For the current factorial/binomial carriers, neither negligible outside-S contribution nor avoidance of the exceptional set is established. This recent theorem does not provide o(m) gcd merely from codimension two. [Primary publication, Theorem 1.2 and Remark 3.6](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.70349).

## 6. Priority adjustment

1. The **fixed-prime averaged Item334 route** deserves a short, focused mathematical attempt. Its missing target is Z(p)=o(p), or only the weighted average A5. It avoids cross-prime independence and requires no valuation-tail theorem. Seek an index-to-argument transformation or a genuine discrete Stepanov construction for the target-retaining residual pair.
2. Keep **Item427 higher-Witt averaging** live, but separate the first-gate root count from the valuation moment. The exact tower formula is not distribution information. A low-degree finite-log representation could solve the rarity side; it would still leave the moment or uniform-integrability theorem.
3. Deprioritize generic **S-unit/linear-recurrence gcd substitution** unless a new exact representation verifies the fixed-S and constant-recurrence hypotheses. Existing holonomic certificates are not sufficient.
4. These are routes to component upper bounds and better allocation of effort. They cannot replace the positive synchronized gain inequality needed for the main irrationality proof. No central ledger change follows from the reductions alone.
