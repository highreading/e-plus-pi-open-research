> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Critical square-root degree: the reciprocal corrections cancel

Put


$$
\sigma=\sqrt2,\qquad M=1+\sqrt2,\qquad d=b-1,\qquad S=e+\pi.
$$



**The critical-square-root relative law holds:** for every fixed $0<\kappa_0<\kappa_1<\infty$, uniformly on the integer indices


$$
n\longrightarrow\infty,\qquad
\kappa_0\sqrt n\le b\le\kappa_1\sqrt n,
$$


every actual coordinate and every positive diagonal metric in the actual coordinates satisfy


$$
\boxed{
c_j-S=(-1)^{n+1}4\pi M^{-2n-b}(1+o(1)),
\qquad
c_W-S=(-1)^{n+1}4\pi M^{-2n-b}(1+o(1)).
}
\tag{1}
$$


Both parities are included. The contact determinant, every first-column coordinate, and every whole error in (1) are nonzero eventually.

There is one necessary repair to the proposed virial argument: the expansion


$$
tV_0'(t)=\alpha nt^2+O(nt^4+t^2),\qquad \alpha=\sigma/M,
$$


is **not uniform up to the principal endpoints**, where $V_0'$ diverges. A modified vector field removes that singularity exactly. No determinant Gaussian approximation is needed.

## 1. Same-index reference ensemble and boundaries

Use precisely the positive principal ensemble


$$
d\mu_{n,d}(\theta)=\frac1{\mathcal Z}
\prod_i g(\theta_i)^n e^{-\sigma\cos\theta_i}
\prod_{i<j}|e^{i\theta_i}-e^{i\theta_j}|^2\,d\theta,
$$


where


$$
g(t)=1+\sigma\cos t,\qquad I=(-3\pi/4,3\pi/4).
$$


Its partition, with the supplied normalization, is $Z_d(0)$. Write


$$
Q=\sum_i\theta_i^2,\quad X=\sum_i\theta_i,\quad
Q_4=\sum_i\theta_i^4,\quad H_3=\sum_i|\theta_i|^3.
$$



We also use real probability tilts proportional to


$$
e^{\tau Q+\ell X}\,d\mu_{n,d},
\tag{2}
$$


where $\tau,\ell$ range over fixed bounded intervals. Their one-particle potential is


$$
V_{\tau,\ell}(t)=V_0(t)-\tau t^2-\ell t.
$$


On an ordered chamber, the total Hessian is bounded below by $cnI_d$: the original one-particle curvature is at least $\alpha n-\sigma$, the quadratic tilt changes it by a bounded amount, and the pair Hessians are positive semidefinite.

All integration-by-parts identities below are legitimate. At an endpoint, $g(t)^n$ vanishes to order $n$, and its logarithmic derivative produces only an integrable order-$(n-1)$ factor. At a collision, the squared Vandermonde vanishes quadratically, while its differentiated factor has only a simple pole. Excising endpoint and collision neighborhoods and then passing to the limit therefore gives zero boundary flux for the bounded polynomial vector fields used below. The bounded tilts do not change these conclusions. The same chamber approximation justifies Brascamp–Lieb.

## 2. Fourth moments under fixed quadratic and linear tilts

For a componentwise vector field $v$, integration by parts gives


$$
\mathbb E_{\tau,\ell}\sum_i v(\theta_i)V_{\tau,\ell}'(\theta_i)
=
\mathbb E_{\tau,\ell}\sum_i v'(\theta_i)
+
\mathbb E_{\tau,\ell}\sum_{i<j}
(v(\theta_i)-v(\theta_j))
\cot\frac{\theta_i-\theta_j}{2}.
\tag{3}
$$



First take $v(t)=t$. Since


$$
x\cot(x/2)\le2 \qquad (|x|<2\pi)
$$


and $tV_0'(t)\ge cn t^2$ for large $n$, the bounded linear tilt can be absorbed using


$$
|\ell|\sum_i|\theta_i|
\le \frac{cn}{2}Q+C\frac dn.
$$


Thus


$$
\mathbb E_{\tau,\ell}Q\le C\frac{d^2}{n}.
\tag{4}
$$



Next take $v(t)=t^3$. With $x=\theta_i-\theta_j$,


$$
(\theta_i^3-\theta_j^3)\cot(x/2)
=(\theta_i^2+\theta_i\theta_j+\theta_j^2)x\cot(x/2)
\le3(\theta_i^2+\theta_j^2).
$$


The multiplier in parentheses is nonnegative, so this upper bound remains valid when the cotangent expression is negative. Also,


$$
t^3V_0'(t)\ge cn t^4.
$$


The linear-tilt contribution is absorbed by


$$
|\ell|\,|t|^3\le \frac{cn}{2}t^4+C n^{-3}.
$$


Equation (3), followed by (4), yields


$$
\boxed{
\mathbb E_{\tau,\ell}Q_4\le C\frac{d^3}{n^2}.
}
\tag{5}
$$


Consequently,


$$
\boxed{
\mathbb E_{\tau,\ell}H_3
\le
\sqrt{\mathbb E_{\tau,\ell}Q\,
      \mathbb E_{\tau,\ell}Q_4}
\le C\frac{d^{5/2}}{n^{3/2}}.
}
\tag{6}
$$


These estimates are uniform under all the fixed tilts in (2).

## 3. The sharp mean of $Q$: an endpoint-safe virial identity

Define


$$
v(t)=\frac{t\,g(t)}M.
\tag{7}
$$


This field vanishes at both principal endpoints. Uniformly on the closed principal interval,


$$
v'(t)=1+O(t^2),\qquad v(t)=t+O(t^3).
$$



Crucially, multiplication by $g$ cancels the endpoint pole:


$$
v(t)V_{\tau,0}'(t)
=
\frac{n\sigma}{M}t\sin t
-\frac{\sigma}{M}t g(t)\sin t
-\frac{2\tau}{M}t^2g(t).
$$


Hence, now genuinely uniformly on the whole interval,


$$
v(t)V_{\tau,0}'(t)
=\alpha nt^2+O(nt^4+t^2).
\tag{8}
$$



The pair term also admits a uniform estimate:


$$
(v(x)-v(y))\cot\frac{x-y}{2}
=2+O(x^2+y^2).
\tag{9}
$$


Indeed,


$$
\frac{v(x)-v(y)}{x-y}=1+O(x^2+y^2),
$$


and $(x-y)\cot((x-y)/2)=2+O((x-y)^2)$ uniformly for differences in the closed interval $[-3\pi/2,3\pi/2]$.

Substitution of (8)–(9) into (3) gives


$$
\alpha n\,\mathbb E_{\tau,0}Q
=
d^2+
O\!\left(n\mathbb E_{\tau,0}Q_4
+d\mathbb E_{\tau,0}Q\right).
$$


Using (4)–(5),


$$
\boxed{
\mathbb E_{\tau,0}Q
=\frac{d^2}{\alpha n}\left(1+O(d/n)\right).
}
\tag{10}
$$



Brascamp–Lieb applied to $Q$, with $\|\nabla Q\|^2=4Q$, gives


$$
\boxed{
\operatorname{Var}_{\tau,0}(Q)
\le \frac Cn\mathbb E_{\tau,0}Q
=O(d^2/n^2).
}
\tag{11}
$$


This proves the requested mean and variance, including fixed $Q$-tilts, without approximating a determinant.

## 4. Exponentially weighted cubic control

Integrating (4) with $\ell=0$ gives, for fixed $K>0$,


$$
\mathbb E e^{KQ}\le \exp(C_Kd^2/n).
\tag{12}
$$


For every fixed quadratic tilt, reflection gives $\mathbb E_{\tau,0}X=0$. Linear tilting does not change the Hessian, so


$$
\operatorname{Var}_{\tau,\ell}(X)\le Cd/n.
$$


Integration in $\ell$ consequently gives


$$
\mathbb E_{\tau,0}e^{\ell X}\le e^{C\ell^2d/n}.
\tag{13}
$$



Since $e^{K|X|}\le e^{KX}+e^{-KX}$, equations (6), (12), and (13) imply


$$
\boxed{
\mathbb E\!\left[H_3e^{KQ+K|X|}\right]
\le C_K e^{C_Kd^2/n}\frac{d^{5/2}}{n^{3/2}}.
}
\tag{14}
$$


For $d=O(\sqrt n)$, this tends to zero, at rate $O(n^{-1/4})$. This supplies the weighted estimate needed for actual complex expectations, rather than only an unweighted Taylor remainder.

## 5. Uniform actual complex characteristic asymptotic

Retain the exact insertion and its full reconstruction normalization:


$$
S_j=\frac{s_jR_j}{B_j},\qquad B_j=|K_{j,d}|\sigma^{-d}.
$$


The gamma expansion gives, pointwise on every circle configuration,


$$
|S_j-1|\le e^{\sigma d/n}-1=O(d/n).
\tag{15}
$$



On the closed disks of radius $1/5$ centered at $M$ and $M^{-1}$, the characteristic factors remain uniformly separated from zero. Their continuously anchored logarithms satisfy


$$
\log\frac{e^{-it}+q}{1+q}
=-\frac{it}{1+q}
-\frac{q\,t^2}{2(1+q)^2}
+O(|t|^3)
\tag{16}
$$


uniformly for $t\in I$. The symbol phase has


$$
-i\sigma\sin t=-i\sigma t+O(|t|^3).
$$


Therefore the normalized principal integral is exactly


$$
\frac{A_j^{\rm pr}(q)}
{s_jB_jZ_d(0)(1+q)^d}
=
\mathbb E\left[
S_j\exp\{a(q)X-c(q)Q+\mathcal R_q\}
\right],
\tag{17}
$$


where


$$
a(q)=-i\left(\sigma+\frac1{1+q}\right),\qquad
c(q)=\frac{q}{2(1+q)^2},\qquad
|\mathcal R_q|\le CH_3.
$$



All coefficient bounds here are uniform. Since $H_3\le (3\pi/4)Q$, the exponential of the remainder is controlled by fixed $Q$-tilts. Equations (14)–(15) show that removing $\mathcal R_q$ and $S_j-1$ incurs $o(1)$.

Likewise, trace concentration and exponential moments give


$$
\mathbb E\bigl[e^{CQ}|e^{a(q)X}-1|\bigr]=o(1).
$$


For example, Cauchy–Schwarz reduces this to (12) and
$\mathbb E[X^2e^{C|X|}]=O(d/n)$.

Set $m=\mathbb EQ$. By (11)–(12),


$$
\mathbb E e^{-c(q)Q}=e^{-c(q)m}+o(1)
$$


uniformly in $q$. Indeed,


$$
|e^{-cQ}-e^{-cm}|
\le C|Q-m|(e^{CQ}+e^{Cm}),
$$


and Cauchy–Schwarz bounds its expectation by $O(d/n)$ on the critical domain. Equation (10) replaces $m$ by $d^2/(\alpha n)$ with an $o(1)$ error.

Finally, the supplied same-$n$ adjacent-norm sector comparison bounds the complete outer contribution, after this normalization, by


$$
e^{-cn+Cd+O(\log n)}.
$$


It includes all odd-sector signs. Thus


$$
\boxed{
\frac{A_j(q)}
{s_jB_jZ_d(0)(1+q)^d}
=
\exp\!\left[
-\frac{d^2}{n}\frac{q}{2\alpha(1+q)^2}
\right](1+o(1)).
}
\tag{18}
$$


The leading exponential is uniformly bounded away from zero. The estimate holds on fixed complex disks, not merely at their real centers. Cauchy estimates therefore give $o(1)$ bounds for each fixed derivative of the logarithmic remainder on smaller disks.

## 6. Both order-one corrections cancel

Write the resulting logarithm as


$$
T_j(q)=d\log(1+q)-\frac{d^2}{n}C(q)+o(1),
\qquad
C(q)=\frac{q}{2\alpha(1+q)^2}.
\tag{19}
$$


At the two anchors,


$$
C(M)=C(M^{-1}).
\tag{20}
$$



For the scalar phases, retain


$$
g(\zeta)=1+\frac{\sigma}{2}(\zeta+\zeta^{-1}),\qquad
h(\zeta)=\frac{\sigma}{2}(\zeta+\zeta^{-1})-1,
$$


and


$$
U_+(\zeta)=T_j(\sigma+\zeta),\qquad
U_-(\zeta)=T_j(\sigma-\zeta).
$$


Their unperturbed curvatures are


$$
\alpha_+=\sigma/M,\qquad \alpha_-=\sigma M.
$$


Equation (19) gives


$$
U_+'(1)=\frac{d}{1+M}+O(1),\qquad
U_-'(1)=-\frac{d}{1+M^{-1}}+O(1).
$$



Expansion of the stationary equation and then the phase gives


$$
nf_\pm(r_\pm)+U_\pm(r_\pm)
=
nf_\pm(1)+U_\pm(1)
-\frac{U_\pm'(1)^2}{2n\alpha_\pm}
+O(d^3/n^2).
\tag{21}
$$


Here the remainder is $o(1)$. The $O(1)$ terms in $U_\pm'(1)$ alter its displayed quadratic contribution by only $O(d/n)=o(1)$.

The two surviving scalar corrections agree because


$$
(1+M)^2\alpha_+
=(1+M^{-1})^2\alpha_-
=2\sigma M.
\tag{22}
$$


Consequently both (20) and (22) cancel in the minus/plus logarithmic ratio:


$$
[nf_-(r_-)+U_-(r_-)]
-[nf_+(r_+)+U_+(r_+)]
=-(2n+d)\log M+o(1).
\tag{23}
$$



The angular curvatures tend uniformly to $\alpha_\pm$, so their Gaussian-prefactor ratio tends to $M^{-1}$. The original scalar integrals are


$$
P_j=\frac{n!}{2\pi}\int_{-\pi}^{\pi}g(e^{is})^n
 A_j(\sigma+e^{is})\,ds,
$$




$$
F_j=2n!\int_{-\pi/4}^{\pi/4}h(e^{is})^n
 A_j(\sigma-e^{is})\,ds.
$$


Their local saddle errors are $o(1)$. The fixed remote gaps give relative bounds $O(\sqrt n e^{-cn+Cd})$. Both radial connectors for the minus arc remain included; their scalar bases are uniformly smaller than the saddle base and their contributions are exponentially negligible.

The exact scalar normalization ratio is $4\pi$. Thus


$$
\boxed{
\frac{F_j}{P_j}=4\pi M^{-2n-b}(1+o(1)),
\qquad \operatorname{sign}P_j=\operatorname{sign}F_j=s_j.
}
\tag{24}
$$


There is no surviving $\kappa$-dependent factor.

## 7. Whole forcing, endpoint, normality, and metrics

The full residual remains


$$
E_j=\nu_{n,d}\!\left(
R_j\sum_{i=0}^d\sigma^i e_{d-i}(z^{-1})eE_i
\right).
$$


Using the supplied bound for the **whole** $eE_i$ gives


$$
|E_j/P_j|\le \frac{e^{Cb}}{n!\sqrt n}.
$$


The coefficient-zero endpoint satisfies


$$
|D/P_0|\le\frac{C\sqrt n\,e^{Cb}}{n!B_0},
\qquad B_0=(n)_d\sigma^{-d}>1
$$


eventually. These are factorially smaller than (24).

Hence the exact identity


$$
c_j-S=
\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac{D}{P_j}
$$


proves the whole coordinate formula (1), including its sign and nonvanishing.

For contact normality, the principal determinant phase
$-\sigma\sum_i\sin\theta_i$ has reflection mean zero and variance $O(b/n)$ by Brascamp–Lieb. Its expectation tends to one; the same outer-sector bound gives $D>0$. Thus


$$
u_j=(-1)^nP_j/D\ne0.
$$


The exact convex identity


$$
c_W-S=\sum_j
\frac{w_ju_j^2}{\sum_\ell w_\ell u_\ell^2}(c_j-S)
$$


then proves (1) uniformly for arbitrary positive diagonal weights.

## 8. Actual primitive scalar and remaining arithmetic

For a rational metric, retain the least actual two-column denominator $d_B$, the integral lift $N_B=d_B[u,v]$, and an integral positive diagonal metric $\Omega$. Define


$$
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p=H_B/g_B,\qquad q=A_B/g_B>0.
$$


Then the **actual primitive, whole evaluated form** is


$$
\boxed{
q(e+\pi)-p
=(-1)^n4\pi qM^{-2n-b}(1+o(1))\ne0.
}
\tag{25}
$$


No estimate for $q$ or its final metric-dependent gcd is inferred from the analytic cancellation.

### (1) New result and proof status

**Proved from the supplied exact reconstruction, sector, contour, and whole-residual inputs:** the critical-square-root relative law (1). The new ingredients are the endpoint-safe sharp virial identity, fourth moments under bounded quadratic and linear tilts, the uniform actual complex limit (18), and cancellation of both order-one corrections.

### (2) Exact remaining bottleneck

Irrationality still requires control of the **actual primitive denominator after the final gcd** on suitable same-index centers, sufficient to make the nonzero forms (25) tend to zero. This result supplies no such arithmetic estimate. The rationality or irrationality of $e+\pi$ remains unresolved.

### (3) Computation request

None. The critical-square-root conclusion follows from uniform analytic estimates, not finite computations.
