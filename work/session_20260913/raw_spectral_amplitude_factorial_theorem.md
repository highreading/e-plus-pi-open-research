> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact parity amplitudes and a factorial asymptotic

Date: 2026-09-13. Original bounded continuation by audit_computations.

This note proves a quantitative formula for the actual nonzero amplitudes in `raw_boundary_free_moment_intertwiner.md`, Section 7. It uses that note's proved self-adjoint realization, parity, eigenvalue intervals, and eigenfunction perturbation bound. No new HP degree is constructed and no spheroidal asymptotic is assumed.

## 1. Statement

Use the orthonormal shifted Legendre basis $\phi_l$, and choose the real normalized eigenfunction $\psi_l$ so that



$$
c_l:=\langle\psi_l,\phi_l\rangle>0.
$$



For $l\ge1$ this is possible by the previously proved estimate



$$
\sqrt{1-(16l-1)^{-2}}\le c_l\le1.
\tag{1}
$$



For $l=0$, the nonvanishing of its initial parity coordinate permits the same phase choice. Write $l=2m+\varepsilon$, $\varepsilon\in\{0,1\}$, and define



$$
G_l=(2\sqrt3)^{\varepsilon}
\frac{(l!)^4}{((2l)!)^2(m!)^2\sqrt{2l+1}}.
\tag{2}
$$



Then the actual amplitudes $g_l$ in that note are positive in these phases and satisfy



$$
\boxed{g_l=G_l\left(1+O\left(\frac{\log(l+1)}{l+1}\right)\right).}
\tag{3}
$$



In particular,



$$
\log g_l=-l\log l+(1-\log8)l+O(\log(l+1)).
\tag{4}
$$



The actual squared spectral weights are thus known up to a relative error tending to zero. This statement by itself does not bound the interpolation polynomials multiplying them or the selected HP nullspace.

## 2. A finite principal determinant gives the exact amplitude

The column operator is $S=\Lambda+3I/4+X^2$, where



$$
t_k=\frac{k+1}{2\sqrt{(2k+1)(2k+3)}}
$$



are the off-diagonal entries of multiplication by $x-1/2$. In parity $\varepsilon$, write



$$
d_j=S_{\varepsilon+2j,\varepsilon+2j},\qquad
b_j=t_{\varepsilon+2j}t_{\varepsilon+2j+1}>0.
$$



Let $S_{\varepsilon,<l}$ be its leading $m$-by-$m$ block, on indices $\varepsilon,\varepsilon+2,\ldots,l-2$, and put



$$
D_m(z)=\det(zI-S_{\varepsilon,<l}),\qquad D_0=1.
$$



The first $m$ eigenvector equations imply the exact identity



$$
\langle\psi_l,\phi_l\rangle
=\frac{D_m(\xi_l)}{b_0\cdots b_{m-1}}
\langle\psi_l,\phi_\varepsilon\rangle.
\tag{5}
$$



For example, the determinant polynomials obey
$D_{j+1}=(z-d_j)D_j-b_{j-1}^2D_{j-1}$, and induction in the tridiagonal eigenvector equations gives (5). This also identifies the finite continued-fraction denominator involved; it does not truncate the eigenfunction.

The amplitude convention is $g_l=\langle\psi_l,\phi_0\rangle$ for even $l$, and $g_l=\langle\psi_l,\phi_1\rangle/2$ for odd $l$. Thus



$$
\boxed{g_l=2^{-\varepsilon}c_l
\frac{\prod_{k=\varepsilon}^{l-1}t_k}{D_m(\xi_l)}.}
\tag{6}
$$



Empty products have value one. Formula (6) is exact for every $l\ge0$.

## 3. Comparing the determinant with the unperturbed gaps

Let $\zeta_j$, $0\le j<m$, be the ordered eigenvalues of the finite parity block. The potential has bounds $3/4\le V\le1$ on the whole space and on every compression. Finite-dimensional min-max therefore gives



$$
\lambda_{\varepsilon+2j}+\tfrac34
\le\zeta_j\le\lambda_{\varepsilon+2j}+1.
$$



Together with the actual $\xi_l$ interval this implies



$$
\xi_l-\zeta_j=\Delta_j+e_j,\quad
\Delta_j=\lambda_l-\lambda_{\varepsilon+2j},\quad |e_j|\le\tfrac14.
\tag{7}
$$



For $m\ge1$, $l\ge2$ and $\Delta_j\ge4l-2\ge6$, so every factor is positive. In particular (6) proves the asserted positive sign of $g_l$.

Define $D_m^{(0)}=\prod_{j<m}\Delta_j$. On reversing the index with $s=m-j$,



$$
\sum_{j<m}\frac1{\Delta_j}
=\sum_{s=1}^m\frac1{2s(2l-2s+1)}
\le\frac{H_m}{2(l+1)}.
\tag{8}
$$



Since $|e_j/\Delta_j|\le1/24$, the elementary logarithm inequality $|\log(1+u)|\le |u|/(1-|u|)$ proves



$$
\left|\log\frac{D_m(\xi_l)}{D_m^{(0)}}\right|
\le\frac{3H_m}{23(l+1)}=:\eta_l.
\tag{9}
$$



Combining (1), (6), and (9) gives the explicit two-sided bound



$$
\sqrt{1-(16l-1)^{-2}}\,e^{-\eta_l}
\le \frac{g_l}{2^{-\varepsilon}\prod t_k/D_m^{(0)}}
\le e^{\eta_l}\qquad(l\ge2).
\tag{10}
$$



For $l=1$ the denominator is empty and $g_1=G_1c_1=c_1/2$. For $l=0$, $g_0=c_0$. These cases are not part of a limiting argument.

## 4. Evaluating the finite products

Direct telescoping gives



$$
\prod_{k=\varepsilon}^{l-1}t_k
=(2\sqrt3)^{\varepsilon}
\frac{(l!)^2}{(2l)!\sqrt{2l+1}}.
\tag{11}
$$



The unperturbed gaps satisfy



$$
D_m^{(0)}
=4^m m!(m+\varepsilon+\tfrac12)_m
=\frac{(2l)!(m!)^2}{2^{\varepsilon}(l!)^2}.
\tag{12}
$$



The $2^{-\varepsilon}$ in (6) cancels the extra $2^{\varepsilon}$ from (12), leaving exactly (2). Equations (9)–(12) prove (3). Applying Stirling's estimate to (2) proves (4); parity alters only polynomial factors.

Two useful consequences of the same exact factorial expression are



$$
\frac{g_{l+2}}{g_l}=\frac1{64l^2}
\left(1+O\left(\frac{\log l}{l}\right)\right)
\tag{13}
$$



on each parity branch, and



$$
\frac{g_{l+1}}{g_l}\longrightarrow\frac{\sqrt3}{8}
\quad(l\text{ even}),\qquad
\frac{g_{l+1}}{g_l}=\frac1{8\sqrt3\,l^2}
\left(1+O\left(\frac{\log l}{l}\right)\right)
\quad(l\text{ odd}).
\tag{14}
$$



These use exactly the amplitude convention of the two initial row branches; switching the odd initial amplitude to its $\phi_1$ coefficient would change the adjacent-parity constants.

## 5. What this supplies and what remains

This proves a fixed-parameter spectral-weight asymptotic directly from the natural Jacobi realization. The lower-block determinant in (6) is positive and all its factors are separated from zero by explicit gaps. It is therefore a useful exact formula, rather than a continued fraction evaluated at an uncontrolled near-pole.

For the actual identity



$$
\langle E_k,\psi_l\rangle=g_l p_k^{(\varepsilon)}(\xi_l),
$$



the spectral amplitudes are no longer unspecified. However, their factorial decay does not permit truncating at $l=n$: the factors $p_k^{(\varepsilon)}(\xi_l)$ and the selected polynomial coefficients must be controlled simultaneously when $k,n$ grow. The next concrete problem is a uniform two-branch interpolation estimate with nodes $\xi_l$ and weights (2), preserving their common origin in (6). No endpoint noncancellation, root bound for $B_n$, or shrinking primitive remainder follows from (3) alone.
