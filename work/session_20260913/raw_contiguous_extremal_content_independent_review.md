> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the contiguous extremal-content inequality

Date: 2026-09-13. Reviewer: audit_sources.

Reviewed in full: `raw_contiguous_extremal_content_inequality.md`, including its exact gcd refinement. The argument passes. This is a full prime-power statement about the actual determinantal contents. It does not prove saturation or an upper bound for a single extremal content.

For $r\ge1$, write $D_r$ for the maximal-minor content of the actual high matrix $H_r$, and $F_r$ for that of the actual extremal matrix $X_r$. At every prime $p>3r+3$, the proved relation is



$$
\min\{v_p(F_r),v_p(F_{r+1})\}\le v_p(D_r)\le v_p(F_r).
$$



Consequently the two localized gcds $\gcd(F_r,F_{r+1})$ and $\gcd(D_r,F_{r+1})$ agree up to units in $\mathbb Z[1/(3r+3)!]$. The following checks address the places at which a reduction to mere rank information, or a lost Taylor row, would invalidate the conclusion.

## 1. Exact omitted order in finite characteristic

Let a nonzero degree-at-most-$r-1$ extremal triple have remainder order at least $M=3r+1$. The reviewed numerator lemma gives a nonzero polynomial $N$ of degree at most $3r-1=M-2$. If the first omitted coefficient $a_0=[z^M]R$ vanished, the order bound from the remainder column and its first two derivatives would give $\operatorname{ord}_0N\ge M-1=3r$, a contradiction. Thus $a_0\ne0$.

This use of order is legitimate with finite jets. Jets through $L=3r+3<p$ suffice: the exponential jet satisfies $E_L'-E_L=O(z^L)$, and its second-derivative discrepancy begins at degree $L-1$. The corresponding arctangent jet has the same adequate differentiated error orders after the fixed rational denominators are cleared. These errors occur after the coefficient range needed for the contradiction at order $3r$. All row factorials and all Taylor denominators used here are units at $p$. No infinite characteristic-$p$ exponential is assumed.

The omitted rows on the pair $T,zT$ are therefore exactly



$$
\begin{pmatrix}a_0&0\\a_1&a_0\end{pmatrix}
$$



at degrees $M,M+1$. Its determinant is a unit. The polynomial $A$ has degree at most $r-1$, and $zA$ degree at most $r$, so neither contributes to these two high coefficients.

## 2. Primitive kernels at the full Smith valuations

Set $f=v_pF_r$, $g=v_pF_{r+1}$, and $e=v_pD_r$. Under the contradiction hypothesis $f,g>e\ge0$, both extremal matrices have a nonunit Smith invariant. The previously proved mod-$p$ nullity bound says there is at most one such invariant for each matrix. Its valuation is therefore the whole content valuation, respectively $f$ or $g$.

Taking the corresponding column of the unimodular Smith column transformation gives a primitive integral vector $t$ with $X_rt\in p^f\mathbb Z_p^{2r+1}$, and likewise a primitive $s$ with $X_{r+1}s\in p^g\mathbb Z_p^{2r+3}$. This supplies the full depths in the note, not only approximate kernels modulo $p$.

After division of each row by its unit factorial, embed $t$ in the degree-at-most-$r$ coefficient coordinates as $t_0$, and let $t_1$ be its polynomial multiple by $z$. Then $H_rt_0,H_rt_1\in p^f\mathbb Z_p^{2r}$. In the shifted case the lowest high row $k=r+1$ becomes the row $k-1=r$ of $X_r$. That lowest row is part of the actual extremal matrix. The proof explicitly retains it.

## 3. The unit two-column completion

The reduction of $t$ gives a nonzero extremal triple. The reviewed top-coefficient lemma implies $b=B_{r-1}$ is a unit. In the $B_{r-1},B_r$ coordinates the two columns $t_0,t_1$ have minor



$$
\begin{pmatrix}b&B_{r-2}\\0&b\end{pmatrix},
$$



with the convention $B_{-1}=0$ when $r=1$. Hence its determinant is a unit. Completing these columns by coordinate vectors outside those two coordinates gives an explicit unimodular matrix $P$, rather than merely a linearly independent pair over the fraction field.

In this basis $H_rP=[p^fU\mid A]$, where $A$ is square of size $2r$. Every maximal minor that uses either of the first two columns has valuation at least $f>e$. There is exactly one maximal minor using neither: $\det A$. Since unimodular change of columns preserves the determinantal ideal, $v_p(\det A)=e$.

The adjugate formula yields $A^{-1}\in p^{-e}\operatorname{Mat}_{2r}(\mathbb Z_p)$. This is a bound of at most $e$ on the loss in elimination. The argument does not require that each inverse entry attain valuation $-e$.

## 4. Elimination and the two remaining rows

Write $s=P(c,y)$. The first $2r$ rows of $X_{r+1}$, whose row indices run from $r+1$ through $3r$, are exactly $H_r$ in the same coefficient coordinates. Thus



$$
p^fUc+Ay\in p^g\mathbb Z_p^{2r}.
$$



For $h=\min(f,g)>e$, this implies $y\in p^{h-e}\mathbb Z_p^{2r}\subset p\mathbb Z_p^{2r}$. Since $P$ is unimodular and $s$ primitive, $c\bmod p\ne0$. The next two actual rows of $X_{r+1}$, of degrees $3r+1,3r+2$, now apply the unit triangular matrix from Section 1 to $c\bmod p$, forcing $c\bmod p=0$. This is the contradiction.

The final row of degree $3r+3$ is unused by the contradiction but remains in the hypothesis $X_{r+1}s\in p^g\mathbb Z_p^{2r+3}$. There is no replacement of $X_{r+1}$ by a smaller matrix and no reverse construction of its defect.

## 5. Gcd refinement and normalization

The inequalities $\min(f,g)\le e\le f$ imply



$$
\min(f,g)=\min(e,g).
$$



Indeed, if $g\le f$, the left inequality gives $g\le e$; if $f<g$, both inequalities force $e=f$. This proves the stated exact gcd identity prime by prime, including multiplicities. It does not assert $e=\min(f,g)$ in all cases.

The finite-difference reductions defining the smaller contents $\eta_r,\theta_r$ use only factorial pivots supported at primes at most $3r$, and the next-degree version at most $3r+3$. Thus at the displayed prime range the substitutions $v_pD_r=v_p\eta_r$, $v_pF_r=v_p\theta_r$ preserve every exponent. The localization introduces no hidden prime above $3r+3$.

No correction is required. The result excludes persistence of excess extremal depth in two adjacent degrees beyond the intervening high-content depth. Isolated extremal defects, their valuation size, and the size of the primitive endpoint denominator remain open.
