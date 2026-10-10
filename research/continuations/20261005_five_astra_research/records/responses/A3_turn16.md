> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact reciprocal anchors extend the relative law to $b=o(n^{2/3})$

Write


$$
\sigma=\sqrt2,\qquad M=1+\sqrt2,\qquad \rho=M^{-1}=\sigma-1,
\qquad d=b-1,\qquad S=e+\pi.
$$



The proposed reciprocal-anchor argument works for the **actual reconstruction insertion**. Its contribution is not exactly reciprocal, but its normalized discrepancy is uniformly $O(d/n)$. This is small throughout $d=o(n)$, independently of the potentially large quantity $d^2/n$.

The resulting new analytic conclusion is:


$$
\boxed{
c_j-S=(-1)^{n+1}4\pi M^{-2n-b}(1+o(1)),
\qquad
c_W-S=(-1)^{n+1}4\pi M^{-2n-b}(1+o(1))
}
\tag{1}
$$


on the integer domain


$$
n\to\infty,\qquad 3\le b=o(n^{2/3}),\qquad 0\le j\le b.
\tag{2}
$$


The estimates are uniform in every actual coordinate, both parities, and every positive diagonal metric $W$ in those coordinates, including arbitrarily varying positive weights.

Below, the new anchor and derivative estimates are proved directly. The scalar contour, full-sector, and complete-residual interfaces used afterward are those explicitly supplied in the source documents; no growing-dimensional Gaussian determinant asymptotic is used.

## 1. The actual insertion and the positive characteristic measure

Retain exactly


$$
A_j(q)=\nu_{n,d}\!\left(
R_j(z)\prod_{\ell=1}^d(z_\ell^{-1}+q)
\right),
$$


where


$$
R_j(z)=[t^j](t-1)(1+D_t)^{-n}
       \prod_{\ell=1}^d(z_\ell+t/\sigma).
$$


Use the full reconstruction normalization


$$
B_j=|K_{j,d}|\sigma^{-d}>0,\qquad
S_j(z)=\frac{s_jR_j(z)}{B_j}.
$$



The gamma expansion, after subtracting its reference constant, gives


$$
\sup_{|z_\ell|\le1}|S_j(z)-1|
\le (1+\sigma/n)^d-1.
$$


Indeed, for every degree-$k$ selected-product term, the sum of its nonconstant normalized contributions is bounded by


$$
\sum_{\ell=1}^k
\binom{k}{\ell}\sigma^\ell
\frac{\Gamma(n+k-\ell)}{\Gamma(n+k)}
\le (1+\sigma/n)^k-1,
$$


because all denominator factors in the gamma ratio are at least $n$. The middle-coordinate references are positive weighted combinations of these terms. Consequently, uniformly in every coordinate and every circle configuration,


$$
\boxed{\ |S_j-1|\le C d/n\ }\qquad(d=o(n)).
\tag{3}
$$


In particular, this controls the insertion on the outer sectors as well.

For positive real $q\in\{M,\rho\}$, let $\mu_q$ be the normalized principal measure with partition $Z_d(q)$ and density proportional to


$$
|\Delta(e^{i\theta})|^2
\prod_{\ell=1}^d
g(\theta_\ell)^n e^{-\sigma\cos\theta_\ell}
|e^{-i\theta_\ell}+q|,
\qquad
g(t)=1+\sigma\cos t,
\tag{4}
$$


on $I^d$, where $I=(-3\pi/4,3\pi/4)$.

Choose the characteristic argument continuously from zero at $t=0$, and define the full actual phase


$$
\Phi_q(\theta)=
\sum_{\ell=1}^d
\left[-\sigma\sin\theta_\ell+
\arg(e^{-i\theta_\ell}+q)\right].
\tag{5}
$$


The principal actual integral is exactly


$$
A_j^{\rm pr}(q)
=s_jB_jZ_d(q)\,
\mathbb E_q[S_j e^{i\Phi_q}].
\tag{6}
$$



Neither the symbol phase nor the characteristic phase has been discarded.

## 2. Real-anchor concentration, with the full insertion retained

The one-particle potential in (4) is


$$
V_q(t)=-n\log g(t)+\sigma\cos t
       -\log|e^{-it}+q|.
$$


For these two fixed anchors, the last term and its first two derivatives are uniformly bounded. The supplied curvature calculation therefore gives


$$
\operatorname{Hess}V_{\rm total}\ge cnI_d
\tag{7}
$$


on an ordered chamber, for all sufficiently large $n$.

Set


$$
Q=\sum_\ell\theta_\ell^2,\qquad X=\sum_\ell\theta_\ell.
$$


Because $V_q$ is even, (7) implies $tV_q'(t)\ge cn t^2$. Integration by parts with the vector field $(\theta_1,\ldots,\theta_d)$ yields


$$
\mathbb E_q\sum_\ell \theta_\ell V_q'(\theta_\ell)
=
d+\mathbb E_q\sum_{p<\ell}
(\theta_p-\theta_\ell)
\cot\frac{\theta_p-\theta_\ell}{2}
\le d^2.
$$


The endpoint and collision boundary terms vanish as in the supplied principal-ensemble argument. Thus


$$
\boxed{\ \mathbb E_qQ\le C d^2/n.\ }
\tag{8}
$$



Reflection preserves $\mu_q$, reverses $X$, and reverses the continuously chosen phase $\Phi_q$. Hence


$$
\mathbb E_qX=\mathbb E_q\Phi_q=0.
$$


The gradients of the individual phase summands are uniformly bounded. Brascamp–Lieb applied using (7) gives


$$
\boxed{
\mathbb E_qX^2\le Cd/n,\qquad
\mathbb E_q\Phi_q^2\le Cd/n.
}
\tag{9}
$$



Define


$$
N_j(q)=\mathbb E_q[S_j e^{i\Phi_q}].
$$


The coefficients of $S_j$ are real, so reflection also shows that $N_j(q)$ is real. More quantitatively,


$$
\begin{aligned}
|N_j(q)-1|
&\le
\left|\mathbb E_qe^{i\Phi_q}-1\right|
+\mathbb E_q|S_j-1|\\
&\le \frac12\mathbb E_q\Phi_q^2+Cd/n
\le Cd/n.
\end{aligned}
\tag{10}
$$


Here reflection removes the sine expectation exactly.

The supplied adjacent-norm sector estimate, with (3), bounds the **complete signed outer contribution** by


$$
\frac{|A_j(q)-A_j^{\rm pr}(q)|}{B_jZ_d(q)}
\le C e^{-cn+Cd+O(\log n)}.
\tag{11}
$$


It bounds, rather than suppresses, every odd-sector sign $(-1)^{nk}$.

Combining (6), (10), and (11),


$$
\boxed{
\frac{A_j(q)}{s_jB_jZ_d(q)}
=1+O(d/n),\qquad q=M,\rho,\quad d=o(n).
}
\tag{12}
$$


In particular, the full actual normalized denominator is bounded away from zero.

## 3. Exact reciprocal anchors cancel the absolute partition

For every real $t$,


$$
|e^{-it}+M|^2=M^2+1+2M\cos t
=M^2|e^{-it}+\rho|^2.
$$


Thus, pointwise,


$$
|e^{-it}+M|=M|e^{-it}+\rho|.
\tag{13}
$$


Consequently,


$$
Z_d(M)=M^dZ_d(\rho),
\qquad
\mu_M=\mu_\rho
\tag{14}
$$


**exactly**.

Using (12) at both anchors now proves the requested full-coordinate result:


$$
\boxed{
\frac{A_j(M)}{A_j(\rho)}
=M^d\left(1+O(d/n)\right),
\qquad d=o(n),
}
\tag{15}
$$


uniformly in $j$.

The actual complex phases at $M$ and $\rho$ need not agree, and $S_j$ has not been removed from either integral. Instead, their normalized actual expectations are separately $1+O(d/n)$. Therefore no potentially large absolute-characteristic correction is expanded as a small error.

For the anchored real logarithms from the zero-free interface, (15) gives


$$
\boxed{
T_{j,-}(\rho)-T_{j,+}(M)
=-d\log M+O(d/n).
}
\tag{16}
$$



## 4. Actual logarithmic derivatives: retaining the denominator

Differentiate the actual characteristic product before taking its integral. At either anchor put


$$
H_q(\theta)=\sum_{\ell=1}^d\frac1{e^{-i\theta_\ell}+q}.
$$


The principal logarithmic derivative is exactly


$$
\frac{(A_j^{\rm pr})'(q)}{A_j^{\rm pr}(q)}
=
\frac{\mathbb E_q[S_j e^{i\Phi_q}H_q]}
     {\mathbb E_q[S_j e^{i\Phi_q}]}.
\tag{17}
$$


This is an identity at the fixed anchor. No differentiation of a surrogate absolute integral is involved.

Uniformly for $t\in I$,


$$
\frac1{e^{-it}+q}
=
\frac1{1+q}
+\frac{it}{(1+q)^2}
+O(t^2).
$$


Therefore


$$
H_q=\frac d{1+q}+\frac{iX}{(1+q)^2}+O(Q).
\tag{18}
$$


The constant term cancels against the **entire denominator** in (17).

One can obtain the requested $O(d^2/n+\sqrt{d/n})$ immediately from (8)–(10). Reflection gives a slightly stronger estimate. Namely,


$$
\begin{aligned}
\left|\mathbb E_q[S_j e^{i\Phi_q}X]\right|
&\le
\left|\mathbb E_q[X(e^{i\Phi_q}-1)]\right|
+\mathbb E_q[|S_j-1||X|]\\
&\le
\sqrt{\mathbb E_qX^2\,\mathbb E_q\Phi_q^2}
+C\frac dn\sqrt{\mathbb E_qX^2}\\
&\le Cd/n.
\end{aligned}
\tag{19}
$$


We used $\mathbb E_qX=0$, and $d/n$ is eventually small.

Also,


$$
\mathbb E_q[|S_j|Q]\le C d^2/n.
$$


Equations (10), (17)–(19) consequently give


$$
\frac{(A_j^{\rm pr})'(q)}{A_j^{\rm pr}(q)}
=\frac d{1+q}+O(d^2/n+d/n).
\tag{20}
$$



On all circle configurations at these anchors,


$$
|H_q|\le Cd.
$$


Thus the differentiated outer-sector integral is bounded by $Cd$ times the absolute sector bound (11). Passing to the full actual integral preserves (20):


$$
\boxed{
\frac{A_j'(q)}{A_j(q)}
=
\frac d{1+q}+O(d^2/n+d/n),
\qquad q=M,\rho,\quad d=o(n).
}
\tag{21}
$$


This is uniform in every actual coordinate. It proves, in particular, the derivative estimate requested in the assignment.

## 5. Finite-$n$ saddle corrections cancel

Use the supplied zero-free holomorphic logarithms, whose fixed-order derivatives are $O(d)$ on interior neighborhoods of the anchors. Set


$$
f_+(\zeta)=\log g(\zeta),\qquad
f_-(\zeta)=\log h(\zeta),
$$


where


$$
g(\zeta)=1+\frac{\sigma}{2}(\zeta+\zeta^{-1}),
\qquad
h(\zeta)=\frac{\sigma}{2}(\zeta+\zeta^{-1})-1,
$$


and


$$
U_+(\zeta)=T_{j,+}(\sigma+\zeta),\qquad
U_-(\zeta)=T_{j,-}(\sigma-\zeta).
$$


The unperturbed curvatures are


$$
\alpha_+=\sigma/M,\qquad \alpha_-=\sigma M.
$$



From (21),


$$
a_+:=U_+'(1)=\frac d{1+M}+O(d^2/n),
$$




$$
a_-:=U_-'(1)=-\frac d{1+\rho}+O(d^2/n).
\tag{22}
$$


Here $d\ge2$, so the $d/n$ term is absorbed.

The real saddles satisfy


$$
r_\pm-1=-\frac{a_\pm}{n\alpha_\pm}+O(d^2/n^2).
$$


Taylor expansion of the stationary equation and then of the phase gives


$$
nf_\pm(r_\pm)+U_\pm(r_\pm)
=
nf_\pm(1)+U_\pm(1)
-\frac{a_\pm^2}{2n\alpha_\pm}
+O(d^3/n^2).
\tag{23}
$$


Indeed, $r_\pm-1=O(d/n)$; the cubic base-phase remainder and the quadratic insertion remainder are both $O(d^3/n^2)$.

Replacing $a_\pm$ in the quadratic term by their leading values in (22) changes that term by at most


$$
O\left(\frac{d^3}{n^2}+\frac{d^4}{n^3}\right)
=O(d^3/n^2).
$$


The leading quadratic corrections agree exactly, since


$$
(1+M)^2\alpha_+
=(1+\rho)^2\alpha_-
=2\sigma M.
\tag{24}
$$



Combining (16), (23), and (24), the actual saddle-value difference is


$$
\boxed{
[nf_-(r_-)+U_-(r_-)]
-[nf_+(r_+)+U_+(r_+)]
=-(2n+d)\log M
+O\left(\frac{d^3}{n^2}+\frac dn\right).
}
\tag{25}
$$



This is the desired cancellation beyond square-root degree.

## 6. Scalar prefactors and the full contours

The angular curvatures satisfy


$$
\lambda_{j,+}=\alpha_++O(d/n),\qquad
\lambda_{j,-}=\alpha_-+O(d/n),
$$


so


$$
\sqrt{\lambda_{j,+}/\lambda_{j,-}}
=M^{-1}(1+O(d/n)).
\tag{26}
$$



The local scalar Taylor argument on $|\theta|\le n^{-2/5}$ has relative error $O(n^{-1/5})$, uniformly: the third derivatives of the full exponent are $O(n+d)=O(n)$, and the curvatures have a fixed positive lower bound.

The supplied full contour estimates remain valid on $d=o(n)$:

* the remote plus and minus circular pieces are bounded relatively by
  

$$
O(\sqrt n\,e^{-cn+Cd});
$$


* both radial connectors of the open minus arc remain included and exponentially negligible;
* the characteristic bounds used on these pieces are for the full actual integral, with all outer sectors retained.

Keeping the exact scalar normalizations $n!/(2\pi)$ and $2n!$, equations (25)–(26) yield


$$
\frac{F_j}{P_j}
=
4\pi M^{-2n-d-1}
\exp\!\left[
O\left(\frac{d^3}{n^2}+\frac dn+n^{-1/5}\right)
\right].
\tag{27}
$$


The saddle main terms are real with signs $s_j$, so eventually


$$
\operatorname{sign}P_j=\operatorname{sign}F_j=s_j.
$$



Since $d+1=b$, on (2) this becomes


$$
\boxed{
\frac{F_j}{P_j}
=
4\pi M^{-2n-b}
\left[
1+O\left(\frac{b^3}{n^2}+\frac bn+n^{-1/5}\right)
\right].
}
\tag{28}
$$


Uniformity can equivalently be stated on every family
$3\le b\le\eta_n n^{2/3}$ with $\eta_n\to0$.

## 7. Whole forcing, endpoint, normality, and actual metrics

The exact coordinate identity is still


$$
c_j-S=
\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac D{P_j},
\tag{29}
$$


with the complete exponential insertion


$$
E_j=\nu_{n,d}\!\left(
R_j
\sum_{i=0}^d\sigma^i e_{d-i}(z^{-1})eE_i
\right).
$$



The supplied whole-residual estimate


$$
|eE_i|\le \frac{27M^n\sigma^{-i}}{n+1}
$$


and the full absolute-partition comparison give


$$
|E_j/P_j|\le \frac{e^{Cb}}{n!\sqrt n}.
\tag{30}
$$


The actual coefficient-zero endpoint satisfies


$$
|D/P_0|
\le \frac{C\sqrt n\,e^{Cb}}{n!B_0},
\qquad B_0=(n)_d\sigma^{-d}>1
\tag{31}
$$


eventually. These bounds remain factorially smaller than $M^{-2n-b}$ throughout (2).

Thus (28)–(31) prove the whole coordinate statement (1), with eventual nonvanishing and sign $(-1)^{n+1}$.

The supplied actual-complex normality argument applies because (2) is eventually contained in $b\le n/1000$. Hence


$$
D>0,\qquad
u_j=(-1)^nP_j/D\ne0.
\tag{32}
$$


No determinant asymptotic is needed.

For every actual positive diagonal metric


$$
W=\operatorname{diag}(w_0,\ldots,w_b),\qquad w_j>0,
$$


retain the actual columns $u,v$ and center


$$
c_W=\frac{u^TWv}{u^TWu}.
$$


The exact identity


$$
c_W-S=
\sum_{j=0}^b
\frac{w_ju_j^2}{\sum_\ell w_\ell u_\ell^2}(c_j-S)
\tag{33}
$$


is a positive convex combination. The coordinate bounds are uniform, so (1), its sign, and its nonvanishing hold independently of the sizes or $n$-dependence of the weights. No assertion for general nondiagonal metrics is being made.

## 8. Primitive multiplier, final gcd, and whole evaluated form

For a rational positive diagonal metric, let $d_B$ be the least positive integer clearing the **actual two-column matrix**:


$$
N_B=d_B[u,v]\in\mathbb Z^{(b+1)\times2}.
$$


Clear the metric denominators to an integral positive diagonal matrix $\Omega$. Define


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_B=H_B/g_B,\qquad q_B=A_B/g_B>0.
\tag{34}
$$


Then $q_B$ is the actual primitive denominator of $c_W$, including the final metric-dependent gcd.

The multiplier taking the original metric linear form


$$
(u^T\Omega u)S-u^T\Omega v
$$


to its primitive integer form is exactly


$$
\frac{d_B^2}{g_B}.
$$


The whole evaluated primitive error is therefore


$$
\begin{aligned}
q_BS-p_B
&=\frac{d_B^2}{g_B}
\left[(u^T\Omega u)S-u^T\Omega v\right]\\
&=\boxed{
(-1)^n4\pi q_BM^{-2n-b}
\left[
1+O\left(\frac{b^3}{n^2}+\frac bn+n^{-1/5}\right)
\right]\ne0.
}
\end{aligned}
\tag{35}
$$


No bound for $d_B$, $g_B$, or $q_B$ follows from anchor reciprocity.

## Closing ledger

### (1) New result and proof status

**Proved new analytic lemmas:** for all $d=o(n)$, uniformly over the actual coordinates,


$$
\frac{A_j(M)}{A_j(\rho)}
=M^d(1+O(d/n)),
$$


and


$$
\frac{A_j'(q)}{A_j(q)}
=\frac d{1+q}+O(d^2/n+d/n),
\qquad q=M,\rho.
$$


The proof retains the full actual insertion, its normalization, its phase, the denominator in the logarithmic derivative, and all signed outer sectors.

**Proved analytic extension using the supplied scalar-contour and complete-residual interfaces:** the whole relative-error law (1) on $3\le b=o(n^{2/3})$, with actual normality, coordinate and whole-error nonvanishing, both parities, and every positive diagonal actual-coordinate metric.

### (2) Exact remaining bottleneck

The target irrationality of $e+\pi$ remains unresolved. For this approximation route, a sufficient missing arithmetic step is control of the **actual primitive denominator after the final gcd**, on an infinite same-index sequence, making


$$
q_BM^{-2n-b}\longrightarrow0.
$$


Then the nonzero primitive forms (35) would tend to zero and contradict rationality. The analytic theorem alone does not establish this denominator condition.

At the analytic boundary $b\asymp n^{2/3}$, the uncomputed $O(d^3/n^2)$ saddle-value difference may be order one; the present proof does not assert its cancellation.

### (3) Computation request

None. The extension follows from exact reciprocity, same-index concentration, and scalar Taylor estimates, not finite numerical evidence.
