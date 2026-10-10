> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3 — Quantitative centered comparison and the complex scalar first moment

## 1. Result and scope

Put


$$
\sigma=\sqrt2,\qquad M=1+\sqrt2,\qquad \rho=M^{-1},
\qquad d=b-1,\qquad \alpha=\sigma/M.
$$


Reconstruction signs are denoted by $\varepsilon_j$. The nonnegative spread indices are


$$
s_0=d,\qquad s_j=b-j\quad(1\le j\le b).
$$



The result below concerns the original finite systems


$$
H_b,T:\{0,\ldots,d\}\times\{0,\ldots,d\},\qquad
K:\{0,\ldots,b\}\times\{0,\ldots,d\}.
$$


No matrix is extended to an infinite system.

At the exact reconstruction and audited scalar inputs in the supplied sources, the centered comparison has the following quantitative form. There are constants


$$
C<\infty,\quad \kappa>0,\quad \epsilon>0,\quad N<\infty
$$


independent of $n,d,j$, such that, for


$$
n\ge N,\qquad 2\le d\le\epsilon n,\qquad 0\le j\le b,
$$




$$
\boxed{
\left|
\log\!\left[\frac{F_j/F_b}{P_j/P_b}\right]
+\frac{s_j}{n^2}
\right|
\le
C\left(\frac{d^2}{n^3}+\frac{d}{n^3}\right)
+C(1+n+d)^6e^{-\kappa n}.
}
\tag{1}
$$



In particular, this implies the requested, slightly weaker bound containing $d/n^{5/2}$.

The improvement is available because the **signed centered angular first moment** on the exact highest-coordinate stationary contour is $O(n^{-1})$. Its **first absolute angular moment** is $O(n^{-1/2})$, even though the angular density is complex. These are different assertions, and neither follows from a modulus saddle alone.

Constants in (1) are universal for fixed nested anchor disks and fixed central angular arcs. The proof below specifies how their uniformity and the positive exponential constant are obtained; it does not claim optimized numerical values.

The audited whole all-sublinear scalar law is reused:


$$
\frac{F_j}{P_j}
=4\pi M^{-2n-b}(1+o(1)),
\tag{2}
$$


uniformly in the actual coordinates. A new leading-error proof is not supplied or needed.

### Verification and search scope

I checked the supplied mathematical texts, including the distinction between the turn24 image-coercivity conclusion and its unnecessarily strong inverse-language formulation. The present argument does not need surjectivity of that loop operator.

No filesystem, browsing, or execution tool is available here. Thus I cannot report fresh archive searches, primary-literature searches, hash verification, or executed arithmetic. The bounded search records supplied with the sources precede this work. The classical inputs are positive-measure Brascamp–Lieb, strong-log-concavity concentration, and elementary complex contour estimates, at the hypotheses displayed below.

---

## 2. The exact insertion and its reference

Retain the complete gamma reconstruction


$$
R_j(z)=\frac{\sigma^{-d}}{\Gamma(n)}
\int_0^\infty u^{n-1}e^{-u}
\left[e_{d-j+1}(\sigma z-u)-e_{d-j}(\sigma z-u)\right]\,du.
$$


Out-of-range elementary polynomials are zero.

Set


$$
B_j=|K_{j,d}|\sigma^{-d},\qquad
\mathcal S_j=\varepsilon_jR_j/B_j,\qquad
L_j=\log\mathcal S_j.
$$


Here $\mathcal S_b=1$. The finite gamma expansion in turn26 proves, on the entire unit polydisk and for $d/n$ sufficiently small,


$$
L_j=-a_je_1+H_j,
\tag{3}
$$


where


$$
a_j\le C/n,\qquad
|H_j|\le C d^2/n^2,\qquad
|\partial_{z_i}H_j|\le C d/n^2.
\tag{4}
$$


The logarithm is the one anchored at $\mathcal S_j(0)=1$. No nonlinear term has been deleted.

The exact one- or two-degree gamma mixture also gives


$$
a_j=\frac{\sigma}{d}\,
\mathbb E_j\frac{k}{n+k-1},
\qquad
\left|a_j-\frac{\sigma s_j}{dn}\right|
\le C\frac{s_j}{n^2}.
\tag{5}
$$



Let $\mathbb E_*$ denote the positive principal measure without a characteristic-modulus factor. Use the same reference at both anchors:


$$
\boxed{\mathcal R_j=\exp(\mathbb E_*L_j).}
\tag{6}
$$


It satisfies


$$
e^{-Cd/n}\le|\mathcal R_j|\le e^{Cd/n}.
\tag{7}
$$


A coordinate-dependent normalization at each anchor would obscure the cancellation that is needed below.

Define


$$
Q_j(q)=\frac{B_bA_j(q)}{\varepsilon_jB_jA_b(q)}.
\tag{8}
$$


On the principal sector this is exactly


$$
Q_j(q)=
\frac{\mathbb E_q(\mathcal S_je^{i\Phi_q})}
     {\mathbb E_qe^{i\Phi_q}},
\tag{9}
$$


not an expectation under a positive measure. Signed outer sectors are added afterward, with their actual normalization.

---

## 3. Uniform moments and fixed-angle tails on the original chamber

### 3.1 Mode comparison, including non-even complex-anchor tilts

Write


$$
\tan(\theta_i/2)=\sqrt c\,u_i,\qquad c=d/n.
$$


The positive modulus density has energy


$$
\mathcal H(u)
=d\sum_iW_c(u_i)+\sum_i h_q(u_i)
-2\sum_{i<k}\log(u_k-u_i),
$$


on its original ordered chamber, where


$$
W_c(u)=
\frac{\log(1+cu^2)-\log(1-cu^2/M^2)}c
+\log(1+cu^2).
$$


The supplied direct differentiation proves $W_c''\ge1/16$.

Uniformly on fixed complex anchor disks,


$$
|h_q''(u)|\le Cc,\qquad |h_q'(0)|\le C\sqrt c.
$$


The same estimates hold for the positive modulus interpolations used later. After reducing a fixed upper bound on $c$, their one-particle energy


$$
\psi(u)=dW_c(u)+h_q(u)
$$


satisfies


$$
\psi''(u)\ge kd,\qquad k=1/32.
\tag{10}
$$


Its minimizer $t_0$ obeys


$$
|t_0|\le C\sqrt c/d.
\tag{11}
$$


This handles the loss of evenness at complex $q$.

For completeness, let $v_i$ be the ordered Gaussian mode satisfying


$$
kd\,v_i=2\sum_{\ell\ne i}\frac1{v_i-v_\ell}.
$$


The Hermite Jacobi-matrix bound gives $\max|v_i|\le2/\sqrt k$. Comparing the actual mode $a_i$ with $t_0+v_i+2/\sqrt k$, at an index maximizing their difference, gives


$$
\psi'(a_i)\le kd\,v_i.
$$


If that difference were positive, $a_i>t_0$, and strong convexity would instead give


$$
\psi'(a_i)\ge kd(a_i-t_0)>kd\,v_i,
$$


a contradiction. The lower bound is identical with reversed inequalities. Thus


$$
\max_i|a_i|\le C_0
\tag{12}
$$


for one constant $C_0$, uniformly also for complex-anchor modulus interpolations.

### 3.2 Radial normalization: no unrelated Gaussian partition quotient

Along each ray from the mode,


$$
\frac{d}{dr}\mathcal H(a+r\omega)\ge kd\,r.
$$


Consequently the radial density is


$$
C r^{d-1}e^{-kd r^2/2}A(r),
$$


with $A$ nonnegative and nonincreasing, extended by zero beyond the actual chamber boundary.

Its likelihood ratio against the normalized Gaussian radius is nonincreasing. Therefore


$$
\mathbb P\{\|u-a\|>T\}
\le
\exp\!\left[-\frac d2
\{kT^2-1-\log(kT^2)\}\right],
\quad kT^2>1.
\tag{13}
$$


The normalization is supplied by stochastic domination itself. No $e^{O(d^2)}$ quotient of independent partition estimates occurs.

Fix a sufficiently small angle $\delta>0$, and put $A=\tan(\delta/2)$. If $c$ is small enough that $C_0\le A/(2\sqrt c)$, then


$$
\max|\theta_i|>\delta
\quad\Longrightarrow\quad
\|u-a\|>\frac{A}{2\sqrt c}.
$$


Hence


$$
\mathbb P\{\max|\theta_i|>\delta\}
\le
\exp\!\left[
-\frac{kA^2}{8}n+
\frac d2\left\{1+\log\frac{kA^2}{4c}\right\}
\right].
\tag{14}
$$


Choose the fixed $\epsilon>0$ so that, for $0<c\le\epsilon$,


$$
\frac c2\left\{1+\log\frac{kA^2}{4c}\right\}
\le\frac{kA^2}{16}.
$$


Then


$$
\boxed{
\mathbb P\{\max|\theta_i|>\delta\}
\le e^{-\kappa_0 n},
\qquad \kappa_0=kA^2/16.
}
\tag{15}
$$



This explicitly covers every $d=o(n)$, including $d=\lfloor\log\log n\rfloor$. There is no lower growth-rate condition.

The same radial comparison gives


$$
\mathbb E\sum_i\theta_i^{2m}\le C_m d(d/n)^m.
\tag{16}
$$


At real anchors reflection and strong log-concavity give


$$
\left\|\sum_i\theta_i\right\|_{L^p}
\le C_p\sqrt{d/n}.
\tag{17}
$$



---

## 4. Original-chamber translation identity and quantitative anchor comparison

The positive angular potential is


$$
V_q(t)=-n\log(1+\sigma\cos t)
+\sigma\cos t-\log|e^{-it}+q|.
$$


Its Hessian, including the pair interaction, is bounded below by


$$
(n\alpha-C)I.
\tag{18}
$$



For real anchors, put $X=\sum_i\theta_i$. Sum-direction integration by parts gives exactly


$$
\mathbb E_q\!\left[X\sum_iV_q'(\theta_i)\right]=d.
\tag{19}
$$



These are integrations on the **original chamber**:

* At a principal endpoint the density vanishes to order $n$; its differentiated endpoint factor is integrable for $n\ge1$.
* At collisions the density has quadratic Vandermonde vanishing.
* The sum-translation vector is tangent to collision faces.
* For the truncated field below, its difference across a collision cancels the cotangent singularity.

Choose the smooth even cutoff $\chi$ of turn27. With


$$
f'(t)=\frac{\sigma\sin t}{1+\sigma\cos t},
\qquad
R(t)=\chi(t)f'(t)-\alpha t,
$$


one has globally on the original interval


$$
|R'(t)|\le Ct^2.
$$


Using (16) and (18),


$$
\operatorname{Var}\!\left(\sum_iR(\theta_i)\right)
\le C(d/n)^3.
$$


The identity for $v_i=X\chi(\theta_i)$, including its pair term, consequently gives


$$
\boxed{
\operatorname{Var}(X)
=\frac{d}{n\alpha}
+O\!\left(\frac{d^2}{n^2}+\frac d{n^2}\right)
+O\!\left((1+n+d)^4e^{-\kappa_0n}\right).
}
\tag{20}
$$


The polynomial exceptional terms arise from bounded cutoff derivatives and at most $d^2$ pair summands, with $|X|\le Cd$. In particular, no singular score is bounded pointwise by a global cubic polynomial.

At the reciprocal real anchors the positive measures coincide. Write


$$
\Phi_q=\eta_qX+T_q,\qquad
\eta_q=-\sigma-\frac1{1+q}.
$$


The estimates needed in the normalized phase calculation are


$$
\|T_q\|_2\le C(d/n)^{3/2},\qquad
\|\Phi_q\|_p\le C_p\sqrt{d/n},
$$




$$
\operatorname{std}\!\left(\sum_i\cos\theta_i\right)\le C d/n,
\qquad
\left\|\sum_i\sin\theta_i-X\right\|_2
\le C(d/n)^{3/2}.
$$


Parity, Taylor's inequality for sine, and the actual denominator


$$
\mathbb E_qe^{i\Phi_q}=1+O(d/n)
$$


then give


$$
\mathbb E_{e^{i\Phi_q}}e_1-\mathbb E_qe_1
=-\eta_q\operatorname{Var}(X)+O(d^2/n^2).
\tag{21}
$$



The complete nonlinear insertion satisfies


$$
\operatorname{std}(H_j)\le Cd^{3/2}n^{-5/2},
$$


so


$$
\mathbb E_{e^{i\Phi_q}}H_j-\mathbb E_qH_j
=O(d^2/n^3).
\tag{22}
$$


Also,


$$
\mathbb E|L_j-\mathbb E_qL_j|^2\le Cd/n^3.
$$


Expansion about the positive-measure mean, with the integral exponential remainder, proves


$$
\log\mathbb E_{e^{i\Phi_q}}e^{L_j}
=\mathbb E_{e^{i\Phi_q}}L_j+O(d/n^3).
\tag{23}
$$



Since $\eta_\rho-\eta_M=-\rho$, equations (20)–(23) yield


$$
\boxed{
\left|
\log Q_j(\rho)-\log Q_j(M)
+a_j\rho\,\frac d{n\alpha}
\right|
\le
C\left(\frac{d^2}{n^3}+\frac d{n^3}\right)
+C(1+n+d)^6e^{-\kappa n}.
}
\tag{24}
$$



The supplied adjacent-norm comparison controls the full signed outer sectors uniformly on the anchor disks by


$$
C(1+d)^C e^{-\eta n+Cd}.
$$


Shrinking the fixed $\epsilon$ absorbs $Cd$ into $\eta n/2$. Thus (24) is a statement about the actual full-circle $Q_j$, not only its principal restriction.

---

## 5. Complex anchors: covariance, interpolation, and Cauchy estimates

At complex $q$, $L_j$ is complex. Here is the precise positive-measure justification.

For a positive probability measure define


$$
\operatorname{Var}_{\mathbb C}(F)
=\mathbb E|F-\mathbb EF|^2.
$$


Applying real Brascamp–Lieb to the real and imaginary components gives


$$
\operatorname{Var}_{\mathbb C}(F)
\le \lambda^{-1}\mathbb E\sum_i|\partial_iF|^2.
\tag{25}
$$


For complex $F,G$, ordinary Cauchy–Schwarz gives


$$
|\mathbb E[(F-\mathbb EF)(G-\mathbb EG)]|
\le
\sqrt{\operatorname{Var}_{\mathbb C}(F)
      \operatorname{Var}_{\mathbb C}(G)}.
\tag{26}
$$


This does not apply BL to a signed measure.

Interpolate the **positive** densities through


$$
|e^{-i\theta}+q|^t,\qquad 0\le t\le1.
$$


Differentiation under the integral gives the componentwise identity


$$
\frac d{dt}\mathbb E_tL_j
=\operatorname{Cov}_t\left(
L_j,\sum_i\log|e^{-i\theta_i}+q|
\right).
$$


Equations (18), (25), and (26) bound this by $Cd/n^2$. Therefore


$$
|\mathbb E_qL_j-\mathbb E_*L_j|\le Cd/n^2.
\tag{27}
$$



Subtract the exact positive-measure phase mean and set


$$
w=e^{i(\Phi_q-\mathbb E_q\Phi_q)},\qquad N=\mathbb E_qw.
$$


Then


$$
|N-1|\le\tfrac12\operatorname{Var}(\Phi_q)\le Cd/n,
\qquad
\operatorname{std}(w)\le C\sqrt{d/n}.
$$


In particular $|N|\ge1/2$, after a fixed reduction of $\epsilon$.

Keeping $N$ in the quotient gives


$$
\log Q_j(q)=\mathbb E_qL_j+O(d/n^2).
$$


Together with (6) and (27),


$$
\left|Q_j(q)/\mathcal R_j-1\right|\le Cd/n^2.
\tag{28}
$$


This holds on fixed disks. The quotient is holomorphic there by the full-circle zero-free result. Cauchy's formula on strictly smaller disks now gives


$$
\boxed{
|\partial_q^m\log Q_j(q)|\le C_m d/n^2,\qquad m=1,2,\ldots .
}
\tag{29}
$$


The positive interpolating expectations themselves need not be holomorphic. Cauchy's formula is applied only to the actual holomorphic quotient after (28) has been established.

---

## 6. The complex scalar first moment

This is the point requiring a quantitative replacement for the informal saddle sentence in turn27.

Use the exact highest-coordinate stationary radius $r=r_{b,\pm}$, including the logarithm of $A_b$ in the stationary equation. On its central arc define the **whole** logarithmic exponent


$$
G_\pm(\theta)
=n\log g_\pm(re^{i\theta})
+\log A_b(\sigma\pm re^{i\theta}),
$$


where $g_+=g$, $g_-=h$.

The retained fixed-disk derivative and contour bounds imply


$$
G_\pm'(0)=0,\qquad
G_\pm''(0)=-n\lambda_\pm,\qquad
0<\lambda_0\le\lambda_\pm\le\lambda_1,
$$




$$
|G_\pm^{(3)}(\theta)|\le Cn,\qquad
\Re(G_\pm(\theta)-G_\pm(0))\le-\gamma n\theta^2
\tag{30}
$$


on a fixed central arc. Although $G_\pm(\theta)$ is complex,
$G_\pm(0)$ and $\lambda_\pm$ are real.

Let


$$
I_\pm=\int_{\rm central}e^{G_\pm(\theta)-G_\pm(0)}\,d\theta.
$$


Taylor expansion and


$$
|e^z-1|\le |z|e^{|z|}
$$


give, on a sufficiently small fixed arc,


$$
I_\pm=
\sqrt{\frac{2\pi}{n\lambda_\pm}}+O(n^{-1}).
\tag{31}
$$


In particular


$$
|I_\pm|\ge c_1n^{-1/2}.
\tag{32}
$$


This establishes actual noncancellation locally; it does not infer it from the modulus.

Using (30) and dividing by (32),


$$
\boxed{
\frac{\int_{\rm central}|\theta|\,
 |e^{G_\pm(\theta)-G_\pm(0)}|\,d\theta}
 {|I_\pm|}
\le Cn^{-1/2}.
}
\tag{33}
$$


Thus the first absolute moment asserted in turn27 is indeed valid.

There is also a stronger centered statement. The Gaussian odd moment vanishes on the symmetric arc, and


$$
\left|
\int_{\rm central}\theta
e^{G_\pm(\theta)-G_\pm(0)}\,d\theta
\right|
\le
Cn\int_{\mathbb R}|\theta|^4e^{-\gamma' n\theta^2}\,d\theta
\le Cn^{-3/2}.
$$


Consequently


$$
\boxed{
\left|
\frac{\int_{\rm central}\theta
e^{G_\pm(\theta)-G_\pm(0)}\,d\theta}{I_\pm}
\right|\le Cn^{-1}.
}
\tag{34}
$$


Similarly the normalized second absolute moment is $O(n^{-1})$.

These estimates remain valid if one calls part of the integrand an “amplitude,” provided its derivatives are included in the estimates. Choosing a stationary point for only the real modulus, while leaving an uncontrolled linear complex phase in the amplitude, would not justify (31)–(34).

---

## 7. Centered scalar transfer

The exact stationary radii satisfy $r_{b,\pm}=1+O(d/n)$. Equation (29) therefore gives


$$
\log Q_j(\sigma\pm r_{b,\pm})
-\log Q_j(M\text{ or }\rho)
=O(d^2/n^3).
\tag{35}
$$



On the common central contour, write


$$
q(\theta)=\sigma\pm re^{i\theta}.
$$


By (28)–(29),


$$
\frac{Q_j(q(\theta))}{Q_j(q(0))}
=1+\beta_j\theta+O((d/n^2)\theta^2),
\qquad |\beta_j|\le Cd/n^2.
$$


Equations (34) and the second-moment estimate show that its normalized insertion cost is


$$
O(d/n^3).
\tag{36}
$$


Using only (33) would instead give $O(d/n^{5/2})$, which is sufficient for the requested bound.

Remote scalar arcs and both minus connectors have normalized size


$$
C(1+n+d)^C e^{-\eta n+Cd}.
$$


The global bound on $\mathcal S_j$, and (7), preserve this estimate after insertion and reference division. For a smaller fixed $\epsilon$, this is $C(1+n+d)^Ce^{-\eta n/2}$.

Thus the scalar transfer uses one actual denominator per sign and centered insertions on its contour. It never divides two independent $1+o(1)$ saddle evaluations.

Combining (24), (35), and (36), then using (5) and


$$
\sigma\rho/\alpha=1,
$$


proves (1).

---

## 8. Whole error and sharp positive-diagonal spread

The complete forces remain


$$
eE_i=-[z^{n+i}](1-z+z^2/2)^n
\int_0^1s^ne^{1-s+sz}\,ds,
$$




$$
E_j=\nu_{n,d}\!\left(
R_j\sum_{i=0}^d\sigma^ie_{d-i}(z^{-1})eE_i
\right).
$$


With $D=\det H_b$,


$$
\boxed{
e_j:=c_j-S
=\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac D{P_j}.
}
\tag{37}
$$



The audited residual bounds give a relative correction bounded by


$$
\tau_{n,d}
=C M^{2n+b}\left(
\frac{2^d}{n!\sqrt n}
+\frac{\sqrt n}{n!B_0}
\right),
\qquad B_0=(n)_d\sigma^{-d}.
\tag{38}
$$


It is superexponentially small in $n$ on the present small-ratio domain after $N$ is enlarged. In particular it can be absorbed into the exponential term in (1). Coordinate zero has not been omitted.

Let $R_{n,d}$ denote the right side of (1), with this residual correction included. Then


$$
\boxed{
\left|\log(e_j/e_b)+s_j/n^2\right|\le R_{n,d}.
}
\tag{39}
$$


The audited whole law ensures that all ratios here are positive eventually.

For a positive diagonal metric in the original coordinates,


$$
\alpha_j=\frac{W_{jj}u_j^2}{u^TWu},\qquad
c_W-S=\sum_j\alpha_je_j,\qquad
\bar s_W=\sum_j\alpha_js_j.
$$


The elementary bounded-variable exponential estimate yields


$$
\boxed{
\left|
\log\frac{c_W-S}{e_b}+\frac{\bar s_W}{n^2}
\right|
\le R_{n,d}+\frac{d^2}{8n^4}.
}
\tag{40}
$$


This bound is independent of all positive weight ratios.

More sharply, the exact attainable closure of the metric errors is


$$
[\min_j e_j,\max_j e_j].
$$


Therefore, with logarithms taken relative to their common sign,


$$
\sup_{W,V>0\ {\rm diagonal}}
\left|\log\frac{c_W-S}{c_V-S}\right|
=
\max_j\log(e_j/e_b)-\min_j\log(e_j/e_b).
\tag{41}
$$


Because $s_b=0$ and $s_0=d$, equations (39)–(41) imply


$$
\boxed{
\left|
\sup_{W,V}
\left|\log\frac{c_W-S}{c_V-S}\right|
-\frac d{n^2}
\right|
\le2R_{n,d}.
}
\tag{42}
$$


Thus the sharp leading logarithmic spread is $d/n^2$, including the endpoint, for arbitrary positive diagonal weight ratios. This is not a statement about nondiagonal metrics.

---

## 9. Primitive arithmetic and closing ledger

For rational positive diagonal weights, preserve the least actual two-column clearer $d_B$ and an integral positive diagonal scaling $\Omega$:


$$
N_B=d_B[u,v],\qquad
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


The final reduction is


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_B=A_B/g_B,\qquad p_B=H_B/g_B.
$$


The primitive multiplier is exactly $d_B^2/g_B$, and the whole evaluated error is


$$
\boxed{
q_BS-p_B
=\frac{d_B^2}{g_B}
\bigl[(u^T\Omega u)S-u^T\Omega v\bigr]
=q_B(S-c_W).
}
\tag{43}
$$



### New result and proof status

At the stated exact reconstruction and audited whole-scalar inputs, the quantitative centered bound (1) follows. The complex stationary amplitude does **not** invalidate the $O(n^{-1/2})$ absolute first moment. Centering at the exact stationary point additionally gives the $O(n^{-1})$ signed first moment and removes the otherwise sufficient $d/n^{5/2}$ term.

The fixed-angle exceptional-tail normalization is uniform in every sublinear regime. Complex-anchor covariance estimates use positive measures componentwise, and Cauchy estimates apply only to the actual holomorphic quotient.

### Exact remaining mathematical bottleneck

This supplies no primitive-$q_B$ upper bound. Even with the nonzero whole-error law and the sharper metric spread, an irrationality argument still needs an infinite same-index sequence controlling the **actual reduced denominator after the final gcd**, for example


$$
q_BM^{-2n-b}\longrightarrow0.
$$


No such sequence is established here. Irrationality of $e+\pi$ remains unresolved.

### Bounded exact arithmetic

No bounded arithmetic calculation is required for the analytic estimates above. An optional consistency certificate is:

* inputs: $2\le d\le12$, $0\le j\le d+1$, symbolic $n$;
* calculation: expand the exact gamma mixture through quadratic degree;
* expected output: zero discrepancies in $\mathbb Q(\sqrt2,n)$ against the constant term $1$, the coefficient $-a_je_1$, and
  

$$
v_je_2-\tfrac12a_j^2e_1^2
$$


  in its logarithm.

Such output would certify only the enumerated finite identities, not uniform CSC or any denominator estimate.
