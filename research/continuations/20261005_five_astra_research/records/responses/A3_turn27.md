> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3 — Centered scalar comparison on the original principal chamber

## Result and scope

Write


$$
\sigma=\sqrt2,\qquad M=1+\sqrt2,\qquad \rho=M^{-1},
\qquad d=b-1,\qquad c=d/n,\qquad \alpha=\sigma/M.
$$


The centered result below concerns


$$
d\longrightarrow\infty,\qquad d=o(n),\qquad 0\le j\le b,
$$


with integer indices and both parities of $n$. Reconstruction signs are denoted by $\varepsilon_j$, and the spread indices remain


$$
s_0=d,\qquad s_j=b-j\quad(1\le j\le b).
$$



The proposed centered scalar comparison can be closed. The essential repair is that the singular translation score must **not** be treated as a globally bounded cubic remainder. A smooth truncation of the translation field, used only as an integration-by-parts device on the original chamber, supplies the needed covariance estimate. Its exceptional event has probability $e^{-\kappa n}$, not merely $e^{-\gamma d}$.

The resulting statement is


$$
\boxed{
\log\left[\frac{F_j/F_b}{P_j/P_b}\right]
=-a_j\rho\,\frac{d}{n\alpha}+o(d/n^2)
=-\frac{s_j}{n^2}+o(d/n^2),
}
\tag{1}
$$


uniformly in the actual coordinates. Consequently,


$$
\boxed{
\log\frac{c_j-S}{c_b-S}
=-\frac{s_j}{n^2}+o(d/n^2),\qquad S=e+\pi.
}
\tag{2}
$$


For every positive diagonal metric in those same coordinates,


$$
\boxed{
\log\frac{c_W-S}{c_b-S}
=-\frac{\bar s_W}{n^2}+o(d/n^2),
\qquad
\bar s_W=\sum_j\frac{W_{jj}u_j^2}{u^TWu}s_j\in[0,d].
}
\tag{3}
$$


No bound for the actual primitive denominator follows.

### Source and search scope

I have read the supplied turn26 in full and use its exact gamma insertion, including its nonlinear derivative estimate. The all-sublinear leading scalar law is reused at the scope validated in A4turn28, including its self-contained slow-dimension join; it is not reproved here.

No filesystem, browsing, or execution tools are available in this exchange. Thus there are no new archive searches, primary-literature searches, hash checks, or executed arithmetic calculations to report. The supplied bounded search records precede this work. The classical inputs used below are the strongly log-concave variance/concentration inequalities and ordinary contour saddle estimates, with their hypotheses specified rather than inferred from a modulus-only ensemble.

---

## 1. Exact chamber, score, and endpoint integration

For positive real $q$ near either anchor, the positive principal density on the ordered chamber in


$$
I=(-3\pi/4,3\pi/4)
$$


is proportional to


$$
|\Delta(e^{i\theta})|^2
\prod_{i=1}^d
g(\theta_i)^n e^{-\sigma\cos\theta_i}
|e^{-i\theta_i}+q|,
\qquad g(t)=1+\sigma\cos t.
\tag{4}
$$


Its particle potential is


$$
V_q(t)=-n\log g(t)+\sigma\cos t
-\frac12\log(1+q^2+2q\cos t).
$$


Hence


$$
V_q'(t)=
\sin t\left(
\frac{n\sigma}{g(t)}-\sigma+
\frac{q}{1+q^2+2q\cos t}
\right).
\tag{5}
$$



The circle Vandermonde is invariant under simultaneous translation. With


$$
X=\sum_i\theta_i,
$$


sum-direction integration by parts therefore gives exactly


$$
\boxed{
\mathbb E_q\left[X\sum_iV_q'(\theta_i)\right]=d.
}
\tag{6}
$$



There is no endpoint flux. At an actual endpoint, $g(t)$ has a simple zero, so the density vanishes as distance to the endpoint to the power $n$. The differentiated density has an integrable endpoint factor of order distance$^{\,n-1}$, for $n\ge1$. The characteristic factor stays separated from zero. Collision boundaries contribute no flux; alternatively, the sum-translation field is tangent to their faces and the Vandermonde vanishes there.

Direct differentiation yields


$$
(-\log g)''(t)
=\frac{\sigma(\cos t+\sigma)}{g(t)^2}\ge\alpha.
$$


The remaining particle terms have uniformly bounded second derivatives. The pair Hessian is positive semidefinite. Thus


$$
\nabla^2\mathcal V_q\ge(n\alpha-C)I
\tag{7}
$$


throughout the original chamber. The same assertion holds for the positive modulus measures on fixed complex anchor disks.

The important qualification is that (7) does **not**, by itself, make the cubic score remainder globally regular: $g^{-1}$ is singular at the endpoints.

---

## 2. Moments and a fixed-angle exceptional event

The moment inputs needed here hold for the tilted, not merely the unperturbed, ensemble:


$$
\boxed{
\mathbb E_q\sum_i\theta_i^{2m}\le C_m d c^m
\quad(m\text{ fixed}),
}
\tag{8}
$$


and, for every fixed sufficiently small $\delta>0$,


$$
\boxed{
\mathbb P_q\{\max_i|\theta_i|>\delta\}
\le e^{-\kappa_\delta n}
}
\tag{9}
$$


eventually on every sublinear allocation.

Here is the uniform transfer from turns23–24. In coordinates


$$
\tan(\theta_i/2)=\sqrt c\,u_i,
$$


the added particle potential is


$$
h_q(u)=\sigma\cos(2\arctan(\sqrt c\,u))
-\log|e^{-2i\arctan(\sqrt c\,u)}+q|.
$$


On the full real principal domain its second derivative is $O(c)$, uniformly on the anchor sets. For real $q$, it is even. Consequently the complete rescaled energy has Hessian at least $k'dI$, for some fixed $k'>0$, eventually. The mode-comparison argument of turn23 applies to


$$
W_c+h_q/d
$$


and bounds every mode coordinate by a fixed constant.

The radial stochastic domination about that mode then implies


$$
\mathbb E\|u-u^\circ\|^{2m}\le C_m.
$$


Thus


$$
\mathbb E\sum_i|u_i|^{2m}\le C_m d.
$$


Using $|\theta_i|\le2\sqrt c\,|u_i|$ proves (8).

If $|\theta_i|>\delta$, then


$$
|u_i|>\tan(\delta/2)/\sqrt c.
$$


The radial tail bound is consequently


$$
\exp\{-K_\delta n+O(d\log(1/c))+O(d)\}.
$$


Since $c\log(1/c)\to0$, this proves (9). It does not impose any lower growth rate on $d$.

Reflection gives $\mathbb EX=0$. Strong log-concavity also gives


$$
\|X\|_{L^p}\le C_p\sqrt c
\tag{10}
$$


for fixed $p$. The same estimate holds for a centered sum of uniformly Lipschitz particle functions.

---

## 3. Translation variance: removing the singular-score obstruction

Define


$$
f'(t)=\frac{\sigma\sin t}{g(t)}.
$$


Locally,


$$
f'(t)=\alpha t+O(t^3),
$$


but this is not a globally bounded cubic remainder.

Choose a fixed smooth even function $\chi$, equal to one on $|t|\le\delta$, and zero on $|t|\ge2\delta$, with $2\delta<3\pi/4$. Put


$$
R(t)=\chi(t)f'(t)-\alpha t.
$$


It is smooth and odd on all of $I$, and


$$
|R'(t)|\le C t^2.
\tag{11}
$$


Indeed, this follows from the Taylor expansion near zero, while away from zero all derivatives involved are bounded and $t^2$ is bounded below.

Brascamp–Lieb, (8), and (7) give


$$
\operatorname{Var}\!\left(\sum_iR(\theta_i)\right)
\le \frac Cn\mathbb E\sum_i\theta_i^4
\le Cc^3.
$$


Therefore


$$
\left|\operatorname{Cov}\!\left(X,\sum_iR(\theta_i)\right)\right|
\le Cc^2.
\tag{12}
$$



Apply integration by parts with the vector field


$$
v_i(\theta)=X\chi(\theta_i).
$$


This is an identity on the original chamber; no conditioned box is introduced. Its divergence is


$$
\sum_i\chi(\theta_i)+X\sum_i\chi'(\theta_i).
$$


The pair-potential contribution contains


$$
X\sum_{i<k}
\bigl(\chi(\theta_i)-\chi(\theta_k)\bigr)
\cot\frac{\theta_i-\theta_k}{2},
\tag{13}
$$


up to the immaterial overall sign convention. It vanishes when all particles lie in $[-\delta,\delta]$. Its summands are bounded: the difference of $\chi$ cancels the collision singularity, and particle differences lie strictly between $-3\pi/2$ and $3\pi/2$, away from the other cotangent poles. Thus (9) bounds its expectation, and all other exceptional terms, by a polynomial in $n,d$ times $e^{-\kappa n}$.

Writing $V_q'=nf'+h_q'$, the smooth lower-order term satisfies


$$
\left|\operatorname{Cov}\left(X,\sum_i\chi(\theta_i)h_q'(\theta_i)\right)\right|
\le Cc.
$$


Consequently the truncated-field identity gives


$$
n\alpha\operatorname{Var}(X)
=d+O(nc^2+c)+O(n^C e^{-\kappa n}).
$$


In particular,


$$
\boxed{
\operatorname{Var}(X)
=\frac{d}{n\alpha}
+O(c^2+c/n)+O(n^C e^{-\kappa n}).
}
\tag{14}
$$



This also checks the proposed full-score statement. Subtracting the truncated-field identity from the exact identity (6) controls the omitted singular-score covariance by the displayed exceptional terms. A pointwise estimate of that singular remainder was neither asserted nor needed.

---

## 4. Normalized phase response of $e_1$

At either real anchor let


$$
w_q=e^{i\Phi_q},\qquad
\Phi_q=\sum_i\left[-\sigma\sin\theta_i+
\arg(e^{-i\theta_i}+q)\right].
$$


The phase is odd, and


$$
\Phi_q=\eta_qX+T_q,\qquad
\eta_q=-\sigma-\frac1{1+q}.
\tag{15}
$$


The derivative of the particle summand of $T_q$ is $O(\theta^2)$ on all of $I$. Thus


$$
\|T_q\|_2=O(c^{3/2}).
\tag{16}
$$


Also,


$$
\|\Phi_q\|_{L^p}=O(\sqrt c),\qquad
\mathbb Ew_q=1+O(c).
\tag{17}
$$



Write


$$
e_1=C+iY,\qquad C=\sum_i\cos\theta_i,\quad Y=\sum_i\sin\theta_i.
$$


Then


$$
\operatorname{std}(C)=O(c),\qquad
\|Y-X\|_2=O(c^{3/2}).
\tag{18}
$$


Reflection removes the inappropriate parity terms. Furthermore,


$$
\operatorname{std}(\cos\Phi_q)=O(c),
$$


by $|1-\cos x|\le x^2/2$ and (17). Hence


$$
\operatorname{Cov}(C,\cos\Phi_q)=O(c^2).
$$


For the odd contribution, (10), (16)–(18), and


$$
|\sin x-x|\le |x|^3/6
$$


give


$$
\mathbb E[Y\sin\Phi_q]
=\eta_q\operatorname{Var}(X)+O(c^2).
$$


Dividing by the actual denominator in (17), rather than replacing it by one prematurely, proves


$$
\boxed{
\mathbb E_{w_q}e_1-\mathbb Ee_1
=-\eta_q\operatorname{Var}(X)+O(c^2).
}
\tag{19}
$$



At $q=M,\rho$, the positive measures coincide exactly, and


$$
\eta_\rho-\eta_M=-\rho.
\tag{20}
$$



---

## 5. Complete nonlinear insertion and exponential cumulant

Retain turn26’s exact logarithm


$$
L_j=\log\mathcal S_j=-a_je_1+H_j,
$$


with


$$
a_j\le C/n,\qquad
|H_j|\le Cd^2/n^2,\qquad
|\partial_{z_i}H_j|\le Cd/n^2.
\tag{21}
$$


These bounds concern the complete insertion, not its quadratic truncation.

From (7),


$$
\operatorname{std}(H_j)\le C d^{3/2}n^{-5/2}.
$$


The exact centered identity


$$
\mathbb E_wH_j-\mathbb EH_j
=\frac{\operatorname{Cov}(H_j,w)}{\mathbb Ew}
$$


and $\operatorname{std}(w)=O(\sqrt c)$ therefore give


$$
\boxed{
\mathbb E_wH_j-\mathbb EH_j=O(d^2/n^3).
}
\tag{22}
$$



It remains important to control the logarithm of the expectation of the exponential. Since


$$
|L_j|\le Cc,\qquad
\operatorname{Var}(L_j)\le Cd/n^3,
\tag{23}
$$


Taylor expansion about $\mathbb EL_j$, with its integral remainder, gives


$$
\boxed{
\log\mathbb E_w e^{L_j}
=\mathbb E_w L_j+O(d/n^3).
}
\tag{24}
$$


For clarity, after writing $Z=L_j-\mathbb EL_j$, the quadratic remainder is bounded by $C\mathbb E|Z|^2$. The square of the normalized first moment is bounded by the same quantity. The denominator $\mathbb Ew$ stays uniformly separated from zero. This is an ordinary positive-measure calculation with a bounded oscillatory multiplier, not a signed-measure Brascamp–Lieb inequality.

At the reciprocal anchors, the unweighted expectations of both $e_1$ and $H_j$ cancel. Equations (19), (20), (22), and (24) yield


$$
\log Q_j(\rho)-\log Q_j(M)
=-a_j\rho\operatorname{Var}(X)
+O(d^2/n^3+d/n^3).
\tag{25}
$$


The retained outer-sector estimates change this by only exponentially small terms. Using (14),


$$
\boxed{
\log Q_j(\rho)-\log Q_j(M)
=-a_j\rho\,\frac d{n\alpha}+o(d/n^2).
}
\tag{26}
$$



---

## 6. Fixed complex disks and the common insertion reference

The proposed fixed-disk claim is valid. It does not require extending the real-anchor parity argument to complex $q$.

Let $\mathbb E_*$ be the positive principal measure with weight


$$
g(\theta)^n e^{-\sigma\cos\theta}
$$


and no characteristic modulus. Define the $q$-independent reference


$$
\mathcal R_j=\exp(\mathbb E_*L_j).
\tag{27}
$$


It may depend on $n,d,j$, but the same reference is used at both anchors and throughout both disks.

For complex $q$ in fixed sufficiently small anchor disks, interpolate the positive modulus weight through


$$
|e^{-i\theta}+q|^t,\qquad 0\le t\le1.
$$


All interpolation Hessians retain the lower bound $n\alpha-C$. The logarithmic tilt is a linear statistic with bounded particle derivative. Therefore


$$
|\mathbb E_qL_j-\mathbb E_*L_j|
\le C\sqrt{d/n^3}\sqrt{d/n}
=C d/n^2.
\tag{28}
$$



The complex phase need not have mean zero. Subtract its exact mean. Its variance is $O(c)$, so its centered exponential has expectation $1+O(c)$, and standard deviation $O(\sqrt c)$. The same centered identity and exponential expansion used above give


$$
\log Q_j(q)=\mathbb E_qL_j+O(d/n^2).
$$


Thus, uniformly on both fixed disks,


$$
\boxed{
Q_j(q)/\mathcal R_j=1+O(d/n^2).
}
\tag{29}
$$


The full-circle signed sectors contribute exponentially small errors uniformly there.

Cauchy estimates on smaller fixed disks consequently give, for every fixed derivative order $m\ge1$,


$$
\boxed{
\partial_q^m\log Q_j(q)=O_m(d/n^2).
}
\tag{30}
$$


A zero-free bound alone would not have supplied (30); the subtraction of the common reference is essential.

---

## 7. Transfer on the highest-coordinate scalar contours

Use the actual $j=b$ scalar contours, not separate coordinate-dependent contours. Their stationary radii satisfy


$$
r_{b,\pm}=1+O(c).
$$


By (30), moving from the corresponding anchor to the real saddle changes $\log Q_j$ by


$$
O(c\,d/n^2)=o(d/n^2).
\tag{31}
$$



On the central arc, the normalized highest-coordinate scalar integral has bounded absolute mass, by its nonzero Gaussian asymptotic and the uniform curvature estimate. Its first absolute angular moment is $O(n^{-1/2})$. Hence insertion of


$$
Q_j(\sigma\pm r_{b,\pm}e^{i\theta})
-Q_j(\sigma\pm r_{b,\pm})
$$


costs, after division by $\mathcal R_j$,


$$
O\!\left(\frac d{n^2\sqrt n}\right)
=o(d/n^2).
\tag{32}
$$


This is a centered insertion estimate, not a division of two independent $1+o(1)$ saddle formulas.

The remote arcs and both minus connectors retain their estimates


$$
\exp(-\kappa n+Cd).
$$


The global bound on $\mathcal S_j$, together with $\mathcal R_j=e^{O(c)}$, makes these negligible at the present scale as well.

The constant reconstruction factors cancel between the two scalar quotients. Combining (26), (31), and (32) proves the first equality in (1). Finally,


$$
a_j=\frac{\sigma s_j}{dn}+O(s_j/n^2),
\qquad
\frac{\sigma\rho}{\alpha}=1,
$$


proves its second equality.

---

## 8. Whole forces, original metric, and primitive arithmetic

The finite systems are unchanged:


$$
H_b,T:\ 0,\ldots,d,\qquad
K:\ \text{rows }0,\ldots,b,\ \text{columns }0,\ldots,d.
$$


The scalar forces are the original $P_j,F_j$, including all particle phases, signed sectors, finite scalar arcs, and both minus connectors.

Retain the complete exponential force


$$
eE_i=-[z^{n+i}](1-z+z^2/2)^n
\int_0^1s^ne^{1-s+sz}\,ds,
$$




$$
E_j=\nu_{n,d}\left(
R_j\sum_{i=0}^d\sigma^i e_{d-i}(z^{-1})eE_i
\right).
$$


With $D=\det H_b$, the whole error remains exactly


$$
\boxed{
c_j-S=
\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac D{P_j}.
}
\tag{33}
$$


The retained factorial bounds make the first and third terms negligible relative to the leading error times $d/n^2$. Thus (1) implies (2), with the endpoint still included.

The exact positive diagonal convex combination then proves (3). Uniformity makes its remainder independent of the weight ratios. Nothing here applies to arbitrary nondiagonal metrics.

For rational positive diagonal weights, preserve


$$
N_B=d_B[u,v],\qquad
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$


where $d_B$ is the least actual two-column clearer and $\Omega$ an integral positive diagonal scaling. Then


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_B=A_B/g_B,\qquad p_B=H_B/g_B.
$$


The primitive multiplier is exactly $d_B^2/g_B$, and the whole evaluated form is


$$
\boxed{
q_BS-p_B
=\frac{d_B^2}{g_B}
\bigl[(u^T\Omega u)S-u^T\Omega v\bigr]
=q_B(S-c_W).
}
\tag{34}
$$



## Closing ledger

**New result and proof status.**  
At the retained exact reconstruction and audited leading-scalar inputs, the argument above proves CSC and its original-coordinate convex-metric consequence. The new steps are the original-chamber truncated translation identity, the $e^{-\kappa n}$ fixed-angle tail, normalized nonlinear and exponential-cumulant estimates, and the common-reference complex-disk bound. No finite computation is used as evidence for uniformity.

**Precise repaired obstruction.**  
The full score is singular at the actual endpoints. A bare claim that its cubic remainder has derivative $O(\theta^2)$ globally is false. The smooth translation-field calculation supplies that bound for a regularized observable, while exact integration by parts controls the omitted score contribution. It avoids a fixed rescaled-wall discard.

**Remaining bottleneck for irrationality.**  
The centered correction does not control the actual denominator after the final gcd. A sufficient separate objective remains an infinite same-index sequence with


$$
q_BM^{-2n-b}\longrightarrow0,
$$


together with the retained nonzero whole-error law. Neither that assertion nor another irrationality criterion is established here. The irrationality of $e+\pi$ remains unresolved.

**Bounded exact arithmetic.**  
No bounded calculation is necessary for the analytic proof. An optional consistency certificate is the turn26 check with inputs $2\le d\le12$, all $0\le j\le d+1$, and symbolic $n$: expand the exact finite gamma mixture and verify its constant, linear, and quadratic logarithmic coefficients against $a_j,v_j$, and


$$
v_je_2-\tfrac12a_j^2e_1^2.
$$


The expected verifiable output is zero discrepancy in $\mathbb Q(\sqrt2,n)$ for every enumerated pair. Such output would certify only that bounded algebraic check, not CSC or a primitive-denominator estimate.
