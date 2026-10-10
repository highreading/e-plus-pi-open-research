> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of uniform interior and edge bounds for the associated measure

Date: 2026-09-13. Reviewer: audit_sources.

Target: raw_associated_measure_uniform_energy_bounds.md, Sections 1–6.
The preceding exact formula has separately passed raw_associated_measure_second_kind_independent_review.md.

**Verdict: PASS.** The uniform interior density estimate, moving-edge density and mass bounds, $L^1$ rate $4/k$, and polynomial quadrature consequence all follow with the displayed constants. There is no mathematical correction. No degree scan, numerical asymptotic fit, or external uniform asymptotic theorem is needed.

## 1. Normalization and the transformed equation

The reviewed formula uses $a=m+1$, $l=2m$, $k=l+1/2$, and


$$
w_a(y)=\frac{\sqrt y}
 {2c_m^2(4m+1)[Q_l^F(\sqrt y)^2+(\pi^2/4)P_l(\sqrt y)^2]}.
$$


Thus $4m+1=2k$. The lower endpoint of the Jacobi tail is $a$; its second-kind expression has degree $2(a-1)$, as used in the target.

I checked the primary formulas directly in [DLMF 14.2.1](https://dlmf.nist.gov/14.2.E1) and [DLMF 14.2.4](https://dlmf.nist.gov/14.2.E4). At order zero their specialization is


$$
(1-x^2)Y''-2xY'+l(l+1)Y=0,\qquad
P_l(Q_l^F)'-P_l'Q_l^F=\frac1{1-x^2}.
$$


The Ferrers convention here agrees with the real principal-value part of the integral-normalized second-kind function already reviewed.

Putting $x=\cos\theta$ first gives
$Y_{\theta\theta}+\cot\theta Y_\theta+l(l+1)Y=0$.
Then $w=\sqrt{\sin\theta}\,Y$ gives exactly


$$
w''+\left(k^2+\frac1{4\sin^2\theta}\right)w=0.
$$


Both normalized solutions $u$ and $v$ satisfy this same equation. At $\theta=\pi/2$, parity and the Wronskian give


$$
u=p_m,\quad u'=0,\quad v=0,\quad v'=-\frac2{\pi p_m}.
$$


The minus sign comes from $dx/d\theta=-1$ there and is correct.

## 2. The two-solution singular-value estimate

In coordinates $z=(w,w'/k)^T$, the skew part of the coefficient matrix is $k\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$. The symmetric part of the remaining matrix is


$$
\begin{pmatrix}0&-q/(2k)\\-q/(2k)&0\end{pmatrix},
\quad q=\frac1{4\sin^2\theta},
$$


with norm $q/(2k)$. Hence every nonzero solution vector satisfies


$$
\left|\frac{d}{d\theta}\log\|z\|\right|\le\frac{q}{2k}.
$$


Integrating in either direction bounds both singular values of the transfer matrix by $e^{\pm I}$, where
$I=\cot\theta/(8k)$.

The initial matrix for the pair of solutions is diagonal in these coordinates, with squared singular values $A_m/k$ and $B_m/k$. The quantity $E=u^2+v^2$ is the squared norm of the first row of the transferred matrix. Lower and upper singular-value bounds therefore give the stated inequality (9), including its exponent $\cot\theta/(4k)$. It does not require either solution to stay nonzero. This is why using both solutions avoids a phase or zero problem.

## 3. Wallis amplitudes and the exact density ratio

Direct substitution of the central-binomial expression gives


$$
\frac{A_{m+1}}{A_m}
=\frac{(4m+5)(2m+1)^2}{(4m+1)(2m+2)^2}
=1+\frac1{(4m+1)(2m+2)^2}.
$$


The initial value is $A_0=1/2$. The Wallis-integral squeeze in the note proves the limit $2/\pi$; hence the convergent logarithmic product legitimately gives


$$
0\le\epsilon_m
\le\frac1{16m^3}+\frac1{32m^2}
\le\frac3{32m^2},\qquad m\ge1.
$$


The last inequality includes $m=1$.

Also


$$
16c_m^2=
\left(1+\frac1{4(2m+1)^2-1}\right)
\left(1+\frac1{4(2m+2)^2-1}\right).
$$


Using $\log(1+t)\le t$ gives (13); both denominators exceed $16m^2$. The all-$m$ inequalities $1/16<c_m^2\le4/45$ follow because each $\alpha_j^2$ decreases to $1/4$.

Since


$$
Q_l^F(\cos\theta)^2+\frac{\pi^2}4P_l(\cos\theta)^2
=\frac{\pi^2E(\theta)}{4\sin\theta},
$$


direct substitution gives


$$
\frac{w_a(y)}{w_{\rm free}(y)}
=\frac1{8\pi c_m^2 kE(\theta)}.
$$


Thus the central limiting factors multiply to one:
$8\pi(1/16)(2/\pi)=1$.
The two logarithmic errors are bounded by
$3/(32m^2)+1/(8m^2)=7/(32m^2)<1/(4m^2)$.
This proves the exact constants in the interior theorem.

The convergence assertion on sets where $k\sqrt{1-y}\to\infty$ is valid: that condition itself forces $k\to\infty$, so the separate $1/(4m^2)$ term tends to zero. Both densities vanish at $y=0$, but the estimate is for $0<y<1$ and extends by their limiting ratio; no division by an endpoint zero is used.

## 4. Positivity in the moving endpoint layer

The elementary integral for $P_l$ implies $|P_l(x)|\le1$ on $[-1,1]$. Its validity can be obtained directly from the [Legendre generating function](https://dlmf.nist.gov/14.7.iv): summing the geometric series under the integral gives


$$
\frac1\pi\int_0^\pi
\frac{d\phi}{1-tx-it\sqrt{1-x^2}\cos\phi}
=(1-2xt+t^2)^{-1/2}
$$


for sufficiently small $t$; coefficient comparison yields the displayed polynomial formula. Its integrand base has modulus at most one.

The telescoping derivative identity then gives
$|P_l'|\le l(l+1)/2$. For $\sin\theta_0=1/k$,


$$
1-\cos\theta_0=\frac1{k^2(1+\cos\theta_0)}.
$$


Thus $P_l(\cos\theta)\ge1/2$ throughout $0\le\theta\le\theta_0$. This proof is uniform, includes $m=1$, and does not rely on an unproved zero location.

At $\theta_0$, the two-solution energy estimate gives


$$
P_l(\cos\theta_0)^2+\frac4{\pi^2}Q_l^F(\cos\theta_0)^2
\le\frac8{\pi^2}e^{1/4}.
$$


The target's bounds on $Q_l^F$ and $T(\theta_0)=Q_l^F/P_l$ follow, with $|T(\theta_0)|<4$.

The Wronskian gives


$$
\frac{d}{d\theta}\left(\frac{Q_l^F(\cos\theta)}
 {P_l(\cos\theta)}\right)
=-\frac1{\sin\theta\,P_l(\cos\theta)^2}.
$$


Integrating from $\theta$ to $\theta_0$ proves the plus sign in (18). There is no pole because the preceding lower bound on $P_l$ has already established positivity on this entire interval.

## 5. Endpoint logarithm, density, and mass constants

Writing $\delta=\sin^2\theta$,


$$
\int_\theta^{\theta_0}\csc t\,dt
=\frac12\log\frac1{k^2\delta}
+\log\frac{1+\cos\theta}{1+\cos\theta_0}.
$$


The last term lies between zero and $\log2$. Since $1\le P_l^{-2}\le4$, the exact ratio integral gives


$$
T\ge L-4,\qquad |T|<7+4L,
\quad L=\frac12\log\frac1{k^2\delta}.
$$


For $0\le L\le8$, the constant term $\pi^2/4$ alone is at least
$(1+L)^2/36$. For $L\ge8$, $(L-4)^2\ge L^2/4$ gives the same bound. The upper inequality
$(7+4L)^2+\pi^2/4\le52(1+L)^2<64(1+L)^2$
holds coefficientwise after expansion. This checks (20) without assuming $T$ has one sign.

Multiplying by $1/4\le P_l^2\le1$ bounds the full denominator by
$(1+L)^2/144$ and $64(1+L)^2$. In the density, use
$\sqrt y\ge1/2$, $c_m^2\le1/9$, $c_m^2\ge1/16$, and $4m+1=2k$.
The upper constant is exactly $576$; the lower estimate obtained this way is $9/512>1/64$. Hence the deliberately weaker displayed $1/64$ is valid.

For the mass lower bound, restricting the integral to
$[\delta/2,\delta]$ loses a factor two, and


$$
1+L_t\le1+L_\delta+\tfrac12\log2
<\tfrac32(1+L_\delta).
$$


This yields the stronger coefficient $1/288$, and therefore the stated $1/512$. The upper mass estimate uses $L_t\ge L_\delta$ on the full interval. No fixed-index endpoint asymptotic was reused with an index-dependent constant.

## 6. Whole-interval comparison and quadrature

On the interior $1-y\ge k^{-2}$, the logarithmic bound is at most
$1/(4m^2)+1/4\le1/2$. Thus the exponential-to-linear estimate is valid throughout that region. The weighted integral needed is exactly


$$
\int_0^1w_{\rm free}(y)
\frac{\sqrt y}{\sqrt{1-y}}\,dy=\frac4\pi,
$$


which gives the $1/(\pi k)$ term in (22).

On the endpoint layer, $P_l^2\ge1/4$ alone gives
$w_a\le64/(\pi^2k)$. Its width is $k^{-2}$; the free density contributes
$16/(3\pi k^3)$. This checks (23).

The final numerical constant can be verified purely by the loose bounds stated in the note. Multiplying the total estimate by $k$, using $k/m^2\le5/2$, $k^{-2}\le4/25$, $e^{1/2}<5/3$, and $\pi>3$, gives at most


$$
\frac53\left(\frac58+\frac13\right)
+\frac4{25}\left(\frac{64}9+\frac{16}9\right)
=\frac{115}{72}+\frac{64}{45}<4.
$$


Therefore the full $L^1$ estimate (5) holds, including both moving edges.

The bounded-test estimate follows from integration against this $L^1$ difference. Applying it to a polynomial of degree at most $2r-1$ and using the already proved exact Gaussian quadrature gives (25), uniformly in $r$ with its explicitly retained supremum norm. No approximation for arbitrary rational tests or a high-degree polynomial with uncontrolled supremum norm follows.

The final limitations are correct. Positive diagonal measures and their uniform convergence do not remove the signed cross measure, the endpoint polynomial of degree $r-1$, or the actual two-boundary factors. The note adds an all-index analytic measure theorem; it does not close the mixed zero-count or irrationality question.

