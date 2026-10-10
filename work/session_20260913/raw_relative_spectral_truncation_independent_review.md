> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the relative spectral truncation theorem

Date: 2026-09-13. Reviewer: audit_computations.

Reviewed `raw_relative_spectral_truncation.md`, Sections 1–4, using the proved amplitude theorem, the separately assigned shifted-positivity theorem, and the uniform spectral-projection estimate. **The deduction passes with no correction required.** This review checks the relative truncation argument; it does not supply the remaining finite-matrix inverse or kernel-angle bound.

## 1. A genuinely uniform ratio

The same-parity amplitude asymptotic implies one eventual integer threshold L such that



$$
g_{l+2}/g_l\le1/(32l^2)\quad\text{for every }l\ge L.
$$



This is an ordinary uniform tail of a convergent sequence; L need not depend on n or on the row index k. The positive phase convention and shifted positivity imply positive $u_k(l)$ for the used range $k,l\ge1$. No assertion about the sign of the $l=0$ column is needed.

For $n+1\le k\le2n-1$, both branch degree caps are at most $n-1$. For $l\ge n-1$, the ratio inequality therefore gives



$$
\frac{p_k^{(\sigma)}(\xi_{l+2})}{p_k^{(\sigma)}(\xi_l)}
\le\left(\frac{(l+2)(l+3)}{l(l+1)-1/4}\right)^{n-1}.
$$



The fixed row and odd-branch normalization factors cancel because the two nodes have the same parity. The elementary upper bound by $(1+6/l)^{n-1}$ is correct: after multiplying by the positive denominators, its difference is $2l^2-l/4-3/2$, which is positive for every integer $l\ge1$. Finally $n-1\le l$ gives the uniform bound $e^6$. Thus the constant $C_0=e^6/32$ is valid for the entire growing row block, not merely each fixed k.

## 2. Both parity chains and the actual normalizer

The first tail node in the parity of $n-1$ is $n+1$, and the first in the parity of n is $n+2$. Their successive step sizes are two, so these two chains cover exactly all $l>n$, with no overlap or omitted node.

At every step the bound $C_0/l^2\le q_n=C_0/(n-1)^2$ applies. Summing the squares along both chains gives precisely



$$
\sum_{l>n}u_k(l)^2\le
\frac{q_n^2}{1-q_n^2}
\left(u_k(n-1)^2+u_k(n)^2\right).
$$



The normalizer $d_{k,n}$ is strictly positive because both retained entries are positive in the used index range. It contains the **actual** values of those columns. This prevents an unrelated absolute upper bound from entering the denominator.

The series equality with the squared spectral tail norm follows from Parseval for the actual polynomial $E_k$. There is no unjustified pointwise or growing-index interchange.

## 3. Omitted pairings and the finite residual

For every polynomial of degree at most n, the uniform projection theorem gives



$$
\|(I-Q_{\le n})P\|\le\frac{\|P\|}{16n+15}.
$$



Cauchy–Schwarz for the two spectral coefficient sequences therefore yields the absolute omitted-series bound with constant



$$
\frac{q_n}{(16n+15)\sqrt{1-q_n^2}}=O(n^{-3}).
$$



This bound is uniform in every high row $k=n+1,\ldots,2n-1$. After division by $d_{k,n}$, stacking exactly $n-1$ rows introduces $\sqrt{n-1}$, giving the stated $O(n^{-5/2})\|P\|$ residual. The sign of that residual can be absorbed into its definition and does not affect the claim.

Pythagoras gives the retained-vector lower norm bound exactly. The finite coefficient vector is therefore not being replaced by one whose norm might collapse relative to $\|P\|$.

The original high equations are those for the unreflected U polynomial. Reflection multiplies each spectral coefficient by $(-1)^l$, because the eigenfunctions have the corresponding reflection parity; the reflected test functions receive the same sign. The final-two-column squares, tail norms, and projection inequalities are unchanged. The note keeps these conventions separate correctly.

## 4. Scope of the conditional inverse implication

If the row-normalized $(n-1)$-by-$(n+1)$ matrix has full row rank and smallest nonzero singular value at least $c/n^2$, the pseudoinverse corrects the retained coefficient vector to a true kernel vector by at most



$$
(n^2/c)O(n^{-5/2})\|P\|=O(n^{-1/2})\|P\|.
$$



This is $o(\sqrt{\log n/n})\|P\|$, as stated. Full row rank and the singular-value bound are explicit hypotheses here, not consequences of row normalization, positivity, or the truncation theorem. The additional low-coordinate estimate for the finite kernel is also still required.

Thus the result resolves the earlier uncontrolled infinite tail relative to the retained columns. It leaves a finite, quantitatively specified cofactor/singular-value problem. No new degree computation, spectral-node sample, or numerical fit is used in this review.
