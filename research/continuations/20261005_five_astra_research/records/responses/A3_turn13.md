> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Relative actual-error asymptotic beyond the cubic threshold

Put


$$
\sigma=\sqrt2,\qquad M=1+\sqrt2,\qquad S=e+\pi,\qquad d=b-1.
$$


The constant $4\pi$ and the formula on $b=o(n^{1/3})$ are already in the supplied archive. The improvement below is a **normalized-expectation argument**, not a relative Gaussian approximation to the determinant.

## 1. Result and scope

For positive integer $n\to\infty$, integer $b\ge3$, and


$$
b=o(\sqrt n),
$$


the supplied actual reconstruction satisfies, eventually,


$$
\boxed{\displaystyle
c_W-S=(-1)^{n+1}4\pi M^{-2n-b}
 \left(1+O\!\left(\frac{b^2}{n}+n^{-1/5}\right)\right).
}
\tag{1}
$$


The constant in the $O$-term is absolute, uniformly over:

* every actual coefficient coordinate $0\le j\le b$;
* both parities of $n$;
* every positive diagonal metric in those actual coordinates, with arbitrary dependence on $n$.

The actual contact matrix and every $u_j$ are nonzero eventually. The **whole** coordinate and metric errors are nonzero, with sign $(-1)^{n+1}$.

The new step is proved below directly for the actual normalized characteristic expectations. It supplies the complex-neighborhood estimate missing from a real-anchor-only argument.

---

## 2. A positive reference ensemble at the same $n,d$

Let


$$
I=(-3\pi/4,3\pi/4),\qquad g(t)=1+\sigma\cos t,
$$


and let $\mu_{n,d}$ be the probability measure proportional to


$$
\prod_{\ell=1}^d g(\theta_\ell)^n e^{-\sigma\cos\theta_\ell}
\prod_{p<q}|e^{i\theta_q}-e^{i\theta_p}|^2
$$


on $I^d$. Its unnormalized partition is precisely the supplied $Z_d(0)$. Define


$$
Q=\sum_{\ell=1}^d\theta_\ell^2,\qquad
X=\sum_{\ell=1}^d\theta_\ell.
$$



All expectations in this section use this **same $n$ and dimension $d$**. There is no adjacent-dimension Gaussian substitution.

### 2.1 Virial estimates, including the boundaries

The one-particle potential is


$$
V_0(t)=-n\log g(t)+\sigma\cos t.
$$


Direct differentiation gives


$$
(-\log g)''(t)
=\frac{\sigma(\cos t+\sigma)}{(1+\sigma\cos t)^2}
\ge\frac{\sigma}{M}.
$$


Consequently, for sufficiently large $n$, the total potential on an ordered chamber has Hessian at least $cnI_d$, for an absolute $c>0$. The pair potentials have positive-semidefinite Hessians.

We also use the probability measures obtained by multiplying the density by $e^{\tau Q}$, where $\tau$ belongs to any fixed bounded interval. Their one-particle potential is


$$
V_\tau(t)=V_0(t)-\tau t^2,
$$


and, uniformly for such $\tau$,


$$
tV_\tau'(t)\ge cn t^2.
\tag{2}
$$



Integration by parts with the vector field $(\theta_1,\ldots,\theta_d)$ gives


$$
\mathbb E_\tau\sum_i\theta_iV_\tau'(\theta_i)
=d+\mathbb E_\tau\sum_{i<j}
(\theta_i-\theta_j)\cot\frac{\theta_i-\theta_j}{2}
\le d^2.
\tag{3}
$$


Here $x\cot(x/2)\le2$ for $|x|<2\pi$, and all differences lie in that interval.

The boundary terms vanish: at the interval endpoints the density vanishes as a positive power of the distance, and at collisions the squared Vandermonde vanishes quadratically. One may first excise endpoint and collision neighborhoods and then pass to the limit; the differentiated singularities are integrable. The same justification applies after multiplication by $Q$ and by $e^{\tau Q}$.

Equations (2)–(3) yield


$$
\mathbb E_\tau Q\le C\frac{d^2}{n}.
\tag{4}
$$


Using instead the vector field $Q(\theta_1,\ldots,\theta_d)$, its divergence is $(d+2)Q$, so


$$
cn\,\mathbb E_\tau Q^2
\le(d^2+2)\mathbb E_\tau Q.
$$


Thus


$$
\mathbb E_\tau Q^2\le C\frac{d^4}{n^2}.
\tag{5}
$$



Integrating


$$
\frac{d}{d\tau}\log\mathbb E e^{\tau Q}
=\mathbb E_\tau Q
$$


now proves, for every fixed $K>0$,


$$
\mathbb E e^{KQ}\le e^{C_Kd^2/n},\qquad
\mathbb E[Q^2e^{KQ}]
\le C_K\frac{d^4}{n^2}e^{C_Kd^2/n}.
\tag{6}
$$



### 2.2 Trace concentration with its mean retained

Reflection preserves the ordered ensemble after reversing particle order, so $\mathbb E X=0$. Brascamp–Lieb applies on the convex ordered chamber, using the Hessian lower bound and the boundary approximation just described.

Tilting additionally by $e^{tX}$ leaves the Hessian unchanged. Therefore


$$
\operatorname{Var}_t(X)\le C\frac dn.
$$


Integrating the second derivative of its logarithmic moment-generating function gives


$$
\mathbb E e^{tX}\le
\exp\!\left(Ct^2\frac dn\right),\qquad t\in\mathbb R.
\tag{7}
$$


In particular, for fixed $K$,


$$
\mathbb E e^{K|X|}\le 2e^{C_Kd/n},
\qquad
\mathbb E[X^2e^{K|X|}]\le C_K\frac dn
\tag{8}
$$


when $d/n$ is sufficiently small. The latter also follows directly from the sub-Gaussian tail implied by (7).

These estimates control the complex characteristic perturbation without introducing a complex probability measure.

---

## 3. The sharpened reconstruction insertion

Retain the exact gamma insertion $R_j$, its sign $s_j$, and


$$
B_j=|K_{j,d}|\sigma^{-d},\qquad S_j=\frac{s_jR_j}{B_j}.
$$



For a degree-$k$ selected-product term, subtract its reference value before estimating. Its normalized gamma integral satisfies


$$
\begin{aligned}
\left|\text{normalized term}-1\right|
&\le
\sum_{\ell=1}^k
\binom{k}{\ell}\sigma^\ell
\frac{\Gamma(n+k-\ell)}{\Gamma(n+k)}\\
&\le (1+\sigma/n)^k-1.
\end{aligned}
$$


The middle-coordinate references are positive combinations of these terms. Hence, for every circle configuration and every coordinate,


$$
\boxed{\quad
|S_j-1|\le e^{\sigma d/n}-1\le C\frac dn.
\quad}
\tag{9}
$$


This strengthens the supplied sector bound in precisely the small-ratio regime needed here. It retains the complete $K$ reconstruction.

---

## 4. Uniform complex normalized expectations

Take the fixed disks


$$
\mathcal D_+=\{|q-M|<1/5\},\qquad
\mathcal D_-=\{|q-M^{-1}|<1/5\}.
$$


For $q$ in their closures, $e^{-it}+q$ stays uniformly away from zero for every real $t\in I$. Define its logarithm continuously along $t$, anchored at $t=0$. Uniform Taylor estimates give


$$
\log\frac{e^{-it}+q}{1+q}
=-\frac{i}{1+q}t+O(t^2),
\tag{10}
$$


where the remainder is bounded in **complex modulus**, uniformly on both disks and all $t\in I$. This global-on-$I$ estimate follows from a uniform bound for the second $t$-derivative.

The actual symbol phase obeys


$$
-i\sigma\sin t=-i\sigma t+O(t^2).
$$


Therefore the principal contribution to the normalized actual characteristic expectation is exactly


$$
\frac{A_j^{\mathrm{pr}}(q)}
{s_jB_jZ_d(0)(1+q)^d}
=
\mathbb E\left[
S_j\exp\{a(q)X+R_q(\theta)\}
\right],
\tag{11}
$$


where


$$
a(q)=-i\left(\sigma+\frac1{1+q}\right),\qquad
|a(q)|\le C,\qquad |R_q(\theta)|\le CQ.
\tag{12}
$$



This representation includes the original complex symbol and characteristic phase.

Since $\mathbb EX=0$,


$$
\left|\mathbb E e^{aX}-1\right|
\le C\mathbb E[X^2e^{C|X|}]
\le C\frac dn.
\tag{13}
$$


Also, by (6), (8), and Cauchy–Schwarz,


$$
\begin{aligned}
\mathbb E\!\left[
e^{C|X|}|e^{R_q}-1|
\right]
&\le C\mathbb E[Qe^{CQ+C|X|}]\\
&\le C\frac{d^2}{n}e^{Cd^2/n}.
\end{aligned}
\tag{14}
$$


Finally, (9) bounds the insertion correction by


$$
C\frac dn\,\mathbb E e^{CQ+C|X|}
\le C\frac dn e^{Cd^2/n}.
\tag{15}
$$



Thus, when $d^2/n$ is sufficiently small,


$$
\frac{A_j^{\mathrm{pr}}(q)}
{s_jB_jZ_d(0)(1+q)^d}
=1+O(d^2/n),
\tag{16}
$$


uniformly in $j$ and throughout both complex disks.

### Full-circle sectors

The supplied adjacent-norm argument is compatible with this normalization. Its short-arc monic norm bound has the form


$$
h_k\ge Cg_\delta^nB_\delta^k/(k+1)^2.
$$


An outer particle contributes at most $CM^{-n}$, and each cross Vandermonde factor contributes at most four. Dividing by the same-$n$ adjacent norms gives the outer-sector bound


$$
\exp(-cn+Cd+O(\log n))
$$


relative to the principal positive partition.

Passing from the positive characteristic partition to
$Z_d(0)|1+q|^d$ costs at most $e^{Cd}$. Equation (9) controls the insertion on every sector. Hence the complete signed outer contribution is still exponentially small; odd-$n$ signs are bounded, not discarded.

We obtain the new interface


$$
\boxed{\displaystyle
\frac{A_j(q)}
{s_jB_jZ_d(0)(1+q)^d}
=1+O\!\left(\frac{d^2}{n}+e^{-cn+Cd}\right)
}
\tag{17}
$$


on both fixed complex disks.

In particular, the anchored holomorphic logarithms satisfy


$$
T_{j,\pm}(q)
=d\log(1+q)+O(d^2/n).
\tag{18}
$$


Cauchy estimates give the same $O(d^2/n)$ bound for every fixed derivative of the remainder on smaller disks. This is the required complex-neighborhood conclusion; no inference from real-axis bounds alone is used.

---

## 5. Recentered scalar saddles and the inherited constant

Use the exact scalar phases


$$
\Psi_{j,+}(\zeta)=\log g(\zeta)+n^{-1}T_{j,+}(\sigma+\zeta),
$$




$$
\Psi_{j,-}(\zeta)=\log h(\zeta)+n^{-1}T_{j,-}(\sigma-\zeta),
$$


with $g,h$ as in the supplied mesoscopic source.

Equation (18) and its derivative bounds give real stationary radii


$$
r_{j,\pm}=1+O(d/n).
$$


Their values satisfy


$$
n\Psi_{j,+}(r_{j,+})
=n\log M+d\log(1+M)+O(d^2/n),
$$




$$
n\Psi_{j,-}(r_{j,-})
=-n\log M+d\log(1+M^{-1})+O(d^2/n).
\tag{19}
$$


The angular curvatures obey


$$
\lambda_{j,+}=\frac{\sigma}{M}+O(d/n),\qquad
\lambda_{j,-}=\sigma M+O(d/n).
\tag{20}
$$



The local Taylor proof on $|\theta|\le n^{-2/5}$ gives relative error $O(n^{-1/5})$: third derivatives remain uniformly bounded, the exponent remainder is $O(n^{-1/5})$, and the rest of the local arc is Gaussian-suppressed. The supplied fixed remote-contour gaps apply because $r_{j,\pm}\to1$; their relative contributions are $O(\sqrt n\,e^{-cn+Cd})$. Both minus endpoint connectors remain included and exponentially negligible.

Consequently the exact scalar normalizations $n!/(2\pi)$ and $2n!$ give


$$
\frac{F_j}{P_j}
=4\pi e^{-2n\log M}
\left(\frac{1+M^{-1}}{1+M}\right)^d
\sqrt{\frac{\lambda_{j,+}}{\lambda_{j,-}}}
\left(1+O(d^2/n+n^{-1/5})\right).
$$


Since


$$
\frac{1+M^{-1}}{1+M}=M^{-1},
\qquad
\sqrt{\frac{\sigma/M}{\sigma M}}=M^{-1},
$$


this is


$$
\boxed{\displaystyle
\frac{F_j}{P_j}
=4\pi M^{-2n-b}
\left(1+O(b^2/n+n^{-1/5})\right).
}
\tag{21}
$$


The leading signs of $P_j,F_j$ are both $s_j$, so their ratio is positive.

No determinant Gaussian approximation entered this ratio. In particular, a common correction of order $d^3/n$ has not been asserted to vanish.

---

## 6. Complete forcing, endpoint, and nonvanishing

The exact whole coordinate identity remains


$$
c_j-S
=\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j,0}\frac{D}{P_j}.
\tag{22}
$$



The complete supplied exponential residual bound and the full absolute-base comparison imply


$$
|E_j|\le
CB_jZ_d(0)\frac{M^n2^d}{n+1}.
$$


The plus saddle lower bound yields


$$
|E_j/P_j|
\le \frac{e^{Cb}}{n!\sqrt n}.
\tag{23}
$$


For the coefficient-zero endpoint, the same-$n$ adjacent norm satisfies


$$
D\le2Z_b(0),\qquad
Z_b(0)/Z_d(0)=h_d\le e^\sigma M^n.
$$


Thus


$$
|D/P_0|\le \frac{C\sqrt n\,e^{Cb}}{n!B_0}.
\tag{24}
$$


Here $B_0=(n)_d\sigma^{-d}>1$ eventually. Equations (23)–(24), divided by $M^{-2n-b}$, are factorially small throughout the claimed domain.

For completeness, contact nonvanishing also follows without determinant Gaussian asymptotics: omit the characteristic and insertion, use reflection and Brascamp–Lieb to obtain


$$
\mathbb E e^{-i\sigma\sum\sin\theta_\ell}=1+O(b/n),
$$


and add the exponentially small outer sectors. Hence $D>0$ eventually on both parities. The nonzero scalar saddle for $P_j$ then gives


$$
u_j=(-1)^nP_j/D\ne0.
$$



Combining (21)–(24) proves (1) for every coordinate. The exact positive convex-combination identity


$$
c_W-S=\sum_j
\frac{w_ju_j^2}{\sum_\ell w_\ell u_\ell^2}(c_j-S)
$$


proves the same uniform formula for every positive diagonal actual metric.

---

## 7. Primitive arithmetic remains separate

For a rational metric, clear its denominators to an integral positive diagonal $\Omega$, and retain the least actual two-column denominator $d_B$ and integral lift $N_B=d_B[u,v]$. Define


$$
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p=H_B/g_B,\qquad q=A_B/g_B>0.
$$


Then $q$ is the actual primitive center denominator, including the final metric-dependent gcd. The whole evaluated primitive form is


$$
\boxed{\displaystyle
qS-p=(-1)^n4\pi qM^{-2n-b}
\left(1+O(b^2/n+n^{-1/5})\right)\ne0.
}
\tag{25}
$$


Nothing here estimates $q$, removes $g_B$, or proves that this evaluated form shrinks.

### (1) New result and proof status

**Proved analytic extension:** the normalized actual-expectation estimate (17), and hence the complete relative center formula on $b=o(\sqrt n)$, using the supplied exact reconstruction and whole-residual identities. The complex-neighborhood control follows from same-index virial moments and trace concentration. The previously established constant $4\pi$ is retained, not presented as new.

### (2) Exact remaining bottleneck

An irrationality conclusion still requires suitable control of the **actual primitive denominator after the final gcd**, so that nonzero forms such as (25) tend to zero. The analytic improvement alone supplies no such control. Rationality or irrationality of $e+\pi$ remains unresolved.

### (3) Computation request

None. The extension uses uniform analytic estimates, not finite sampling.
