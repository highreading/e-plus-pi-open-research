> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: almost full initial actual spectral band

Date: 2026-09-13. Reviewer: audit_sources.

**Verdict: PASS.** The new uniform eigenfunction-tail estimate and its combination with the earlier actual high-row approximation are valid. No mathematical correction is needed. The proof gives an almost-isometric orthogonal projection of the specified initial eigenfunction band into the actual high-row span. It gives neither an unpreconditioned singular-value estimate nor a predetermined row-grid minor.

Reviewed source: raw_almost_full_initial_spectral_band.md. I also read the precise realization/parity statements in raw_boundary_free_moment_intertwiner.md §6, the row scaling in its §2, the actual spectral normalization in raw_fixed_node_branch_asymptotics.md §1, the complete relevant approximation argument in raw_high_orthogonality_spectral_concentration.md §§2–4, and its parity interpolation input raw_arctan_dual_factorial_mass.md §§2–3. No new numerical computation or degree/prime scan is used.

## 1. Operator realization and the parity tail

The source uses the genuine self-adjoint operator


$$
T=L_0+\tfrac34+W,\qquad W=(x-\tfrac12)^2,
$$


where $L_0$ is diagonal in the complete orthonormal shifted-Legendre basis, with eigenvalues $E_j=j(j+1)$ and domain


$$
\mathcal D(L_0)=
\left\{f:\sum_j E_j^2|\langle f,\phi_j\rangle|^2<\infty\right\}.
$$


This is the previously specified realization, rather than a new choice of singular-endpoint boundary condition. Since $W$ is bounded, $T$ has the same domain. Its actual normalized eigenfunctions therefore belong to this domain.

Multiplication by $x-\tfrac12$ connects only neighboring Legendre indices. Its square $W$ connects only indices at differences zero and two, preserves reflection parity, satisfies $W\ge0$, and has operator norm at most $1/4$. The earlier min-max proof gives


$$
E_\ell\le \xi_\ell-\tfrac34\le E_\ell+\tfrac14.
$$


It also gives the parity $(-1)^\ell$ of $\psi_\ell$, by applying the same enclosures to the two parity restrictions. Thus no opposite-parity component is silently omitted in the present tail bound.

For $h\ge1$, let $Q_h$ select the parity-$\ell$ coordinates beginning at $\ell+2h$. Coordinate projection preserves $\mathcal D(L_0)$. On this tail the operator


$$
A_h=Q_h(L_0+W-\xi_\ell+\tfrac34)Q_h
$$


is self-adjoint on the diagonal tail domain and bounded below by


$$
\begin{aligned}
E_{\ell+2h}-E_\ell-\tfrac14
&=2h(2\ell+2h+1)-\tfrac14\\
&\ge \tfrac{15}{4}h^2>0.
\end{aligned}
$$


The displayed coarse lower bound is valid uniformly for every $\ell\ge0,h\ge1$. Indeed the difference from its right side is
$\tfrac14h^2+4\ell h+2h-\tfrac14>0$.
Consequently $A_h^{-1}$ exists as a bounded operator on the tail Hilbert space and has norm at most $4/(15h^2)$. This follows directly from the self-adjoint lower bound; compact resolvent is compatible with the argument but is not needed to claim an inverse.

The projected eigenvalue equation is legitimate on this domain:


$$
A_hQ_h\psi_\ell=-Q_hW(I-Q_h)\psi_\ell.
$$


The right side has just one possible nonzero coordinate. It comes from the entry connecting $\ell+2h-2$ to $\ell+2h$; there are no other crossings because $W$ has parity bandwidth one. Its coefficient has modulus at most $1/4$. Therefore, with $t_h=\|Q_h\psi_\ell\|$,


$$
t_h\le\frac1{15h^2}
|\langle\psi_\ell,\phi_{\ell+2h-2}\rangle|
\le\frac1{15h^2}t_{h-1}.
$$


Here $Q_0$ begins at $\ell$, so $t_0\le1$; it is not being identified with the norm of the entire eigenfunction. Iteration proves exactly


$$
t_h\le \frac{15^{-h}}{(h!)^2}.
$$


There is no hidden dependence on a fixed eigenfunction index.

The truncation condition is also correct. If $K\ge\ell+2h-2$, every index of parity $\ell$ strictly greater than $K$ is at least $\ell+2h$. Thus


$$
\|(I-P_{\le K})\psi_\ell\|\le t_h.
$$


The choice $M=K-2h$ used later is two indices more conservative than necessary and introduces no off-by-two error.

## 2. Actual high-row approximation and all growing constants

The actual row scaling is


$$
E_k=c_k\sqrt{2k+1}\,F_k,\qquad
c_k=2^{-k}\binom{2k}{k}\ne0.
$$


It is the same as the product normalization in the boundary-free intertwiner. Hence the spans of the specified $E_k$ and $F_k$ agree exactly, even though their unscaled Gram matrices need not have comparable condition numbers.

The earlier parity interpolation produces, for each low raw Borel polynomial, an approximant in the actual high span with uniform error


$$
4n^2(2e^3)^n/n!,\qquad n\ge4.
$$


Its exact retained monomial orders cover both parity counts when $n$ is even or odd. The inverse-Borel change of basis proved in the cited note gives


$$
\sum_{k=0}^j|a_{j,k}|
\le (j+1)^3\sqrt{2j+1}\,8^j j!.
$$


That argument retained the different even and odd normalizations through
$|P_k(0)|\le1$ and $|P'_k(0)|\le k$, respectively. Their product is precisely the source's $\epsilon_{n,K}$, after taking the nondecreasing bound at $j=K$.

For $v=\sum_{j=0}^K v_j\phi_j$, the linear combination of the individual high-row approximants has error at most


$$
\epsilon_{n,K}\sum_j|v_j|
\le \sqrt{K+1}\epsilon_{n,K}\|v\|.
$$


Thus the source's passage from individual polynomial approximation to the whole low polynomial subspace is valid. It uses orthonormal coefficients and Cauchy–Schwarz, rather than assuming that the individual approximants are independent.

Taking $v=P_{\le K}\psi_\ell$ uses $\|v\|\le1$ and the independently proved eigenfunction tail. This gives the individual defect bound


$$
\operatorname{dist}(\psi_\ell,H_n)
\le \frac{15^{-h}}{(h!)^2}
+\sqrt{K+1}\epsilon_{n,K}
$$


uniformly for the full growing range $\ell\le M$.

## 3. Cutoffs and exponential rate

For the source's


$$
w=\left\lceil\frac{8n}{\log(n+1)}\right\rceil,\quad
K=n-w,\quad
h=\left\lceil\frac{2n}{\log(n+1)}\right\rceil,\quad
M=K-2h,
$$


all degrees are in the allowed ranges for sufficiently large $n$. In particular $M\ge0$, $K\le n$, and the band dimension


$$
r=M+1=n-\frac{12n}{\log n}+o(n/\log n)
$$


is at most the high-span dimension $n-1$.

Writing $c_0=\log16+3$, the exact approximation bound gives


$$
\begin{aligned}
\log\epsilon_{n,K}
&=n\log(2e^3)+K\log8+\log(K!/n!)+O(\log n)\\
&\le c_0n-w\log n+O(w^2/n+\log n)\\
&=-(8-c_0)n+o(n).
\end{aligned}
$$


Here $w=o(n)$, and the factorial-ratio estimate follows by summing
$\log(n-j)$ for $0\le j<w$. No fixed-degree constant is reused in a growing range.

Also


$$
\log\frac{15^{-h}}{(h!)^2}
=-2h\log h+O(h)=-4n+o(n).
$$


Since $0<8-c_0<4$, the polynomial-approximation exponent dominates the sum. The additional factors $\sqrt{K+1}$ and $\sqrt r$ have logarithm $O(\log n)$ and do not alter the displayed exponential rate. The use of $o(1)$ inside the exponent is justified; no explicit finite starting value of $n$ is claimed.

## 4. Almost-isometry, actual columns, and kernels

Let $\Psi_r:\mathbb C^r\to L^2(0,1)$ have the actual normalized orthogonal eigenfunctions as columns, and let $P_H$ be the orthogonal projection onto $H_n$. The map $\Psi_r$ is exactly an isometry. The individual defects give a finite Hilbert–Schmidt bound


$$
\|(I-P_H)\Psi_r\|
\le\|(I-P_H)\Psi_r\|_{\rm HS}
\le\sqrt r\,b_{n,K,h}.
$$


The exact identity


$$
\Psi_r^*P_H\Psi_r
=I_r-\big((I-P_H)\Psi_r\big)^*
       \big((I-P_H)\Psi_r\big)
$$


therefore proves the source's lower bound by
$(1-rb_{n,K,h}^2)I_r$. In particular the map from this prescribed initial eigenfunction span into $H_n$ is injective eventually.

The $n-1$ row polynomials are linearly independent: they have distinct degrees $n+1,\ldots,2n-1$ and nonzero leading coefficients. Their actual moment matrix against $\psi_0,\ldots,\psi_M$ consequently has column rank $r$. This gives at least one nonzero $r$-row minor, but the proof does not identify its row indices.

For every $v\in H_n^\perp$,


$$
\|\Psi_r^*v\|
=\|\Psi_r^*(I-P_H)v\|
\le \sqrt r\,b_{n,K,h}\|v\|.
$$


This is the adjoint of the already bounded defect map. It needs no polynomial restriction on $v$. For a finite actual spectral expansion it yields exactly the squared-mass inequality stated in the source.

The normalization remains physical throughout. In the identity


$$
\langle E_k,\psi_\ell\rangle=g_\ell
p_k^{(\ell\bmod2)}(\xi_\ell)
$$

, the factor $g_\ell$ has not been discarded before applying the estimates. Reflection only changes actual orthonormal spectral coordinates by the signs $(-1)^\ell$. It preserves the squared-mass bound.

For clarity, the final Gram paragraph can define $U$ as the synthesis map


$$
U:\mathbb C^{n-1}\to H_n,\qquad Ua=\sum_{k=n+1}^{2n-1}a_kE_k.
$$


Then $G_H=U^*U$, $P_H=UG_H^{-1}U^*$, and the Gram of
$G_H^{-1/2}U^*\Psi_r$ is exactly $\Psi_r^*P_H\Psi_r$.
This is a notation clarification, not a mathematical repair. The canonical preconditioning does not give an estimate for the raw row-Gram inverse.

## 5. Exact scope of the accepted result

The theorem establishes a specified consecutive initial set of
$n-O(n/\log n)$ independent actual spectral columns, as well as exponentially small spectral mass in that band for every exact high kernel. Its uncontrolled complementary band still has order $n/\log n$. The theorem does not establish top-two concentration, endpoint noncancellation, a prescribed row-grid determinant, or improved total rank over the separate $n-O(\sqrt n\log n)$ count. It also gives no primitive-denominator or irrationality conclusion.

All four sections of the source pass the independent audit with those stated limits.

