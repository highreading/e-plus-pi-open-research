> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Critical four-fifths: the proposed moments pass, and the fifth comparison closes

Put


$$
\sigma=\sqrt2,\quad M=1+\sqrt2,\quad \rho=M^{-1},
\quad \alpha=\frac{\sigma}{M},\quad d=b-1,\quad S=e+\pi.
$$


The critical index domain in this report is


$$
n\to\infty,\qquad
\kappa _0n^{4/5}\le b\le\kappa _1n^{4/5},\qquad
0\le j\le b,                                      \tag{1}
$$


where $0<\kappa _0\le\kappa _1<\infty$ are fixed. All indices are integers, and both parities of $n$ are included.

**Both proposed moment coefficients are correct.** Their stated errors also close after accounting for the finite-degree cancellations, the $h_q$ terms, and the centered product errors. They give the missing first- and second-derivative precisions. Combined with the already established third/fourth precisions and the retained actual scalar-contour interfaces, this completes the critical fifth stationary comparison and gives


$$
\boxed{
c_j-S=(-1)^{n+1}4\pi M^{-2n-b}(1+o(1)).
}                                                     \tag{2}
$$


The error is uniform on (1), over every actual coordinate. Consequently (2) holds for every positive diagonal metric in those coordinates.

The analytic conclusion uses the retained contour interfaces explicitly listed below. It supplies **no bound for the actual primitive denominator** and no irrationality conclusion.

## 1. Normalizations and reused results

At $q=M,\rho$, all positive expectations below use precisely the principal measure


$$
d\mu_q\propto |\Delta(e^{i\theta})|^2
 \prod_{\ell=1}^d g(\theta_\ell)^n
 e^{-\sigma\cos\theta_\ell}|e^{-i\theta_\ell}+q|\,d\theta,
\quad g(t)=1+\sigma\cos t,
$$


on $I^d$, $I=(-3\pi/4,3\pi/4)$.

The actual characteristic integral and reconstruction remain


$$
A_j(q)=\nu_{n,d}\!\left(R_j(z)\prod_\ell(z_\ell^{-1}+q)\right),
\qquad
R_j(z)=[t^j](t-1)(1+D_t)^{-n}
                  \prod_\ell(z_\ell+t/\sigma).
$$


With $S_j=s_jR_j/B_j$, use the actual complex normalization


$$
\mathcal W_j=S_je^{i\Phi_q},\qquad
N_j(q)=\mathbb E_q\mathcal W_j,\qquad
\langle F\rangle_j=\frac{\mathbb E_q(\mathcal W_jF)}{N_j(q)}. \tag{3}
$$


The retained estimates are


$$
\|S_j-1\|_\infty=O(d/n),\quad
\mathbb E_q\Phi_q^2=O(d/n),\quad
N_j(q)=1+O(d/n).
$$


In particular, division by $N_j$ is legitimate eventually and uniformly.

Write


$$
Q=Q_2=\sum_i\theta_i^2,\quad Q_{2r}=\sum_i\theta_i^{2r},
\quad X=\sum_i\theta_i,\quad C_{2r+1}=\sum_i\theta_i^{2r+1}.
$$


I reuse, without repeating their proofs, turn21’s sharp $Q_6$, its centered transfer, and its third/fourth derivative estimates. I also reuse the lower moments, Poincaré estimates, and signed $X,C_3,C_5$ estimates from turns19–20, with their original measure and normalization.

## 2. Audit of the safe-virial coefficients

Let


$$
V_q(t)=-n\log g(t)+h_q(t),\qquad
h_q(t)=\sigma\cos t-\log|e^{-it}+q|.
$$


At both anchors, $h_q$ is smooth and even on $\overline I$, so


$$
|h_q'(t)|\le C|t|.                                    \tag{4}
$$


Use the endpoint-safe fields $v_k(t)=t^kg(t)/M$. The exact loop identity is


$$
\mathbb E\sum_i v(\theta_i)V_q'(\theta_i)
=\mathbb E\sum_i v'(\theta_i)
+\mathbb E\sum_{i<k}(v(\theta_i)-v(\theta_k))
                   \cot\frac{\theta_i-\theta_k}{2}.     \tag{5}
$$


The fields vanish at the endpoints. At collisions the Vandermonde zero and the paired difference remove the boundary flux and cotangent singularity.

All Taylor remainders used here are bounds on the **whole closed interval or square**. After removing the diagonal singularity, the paired functions are smooth; their local orders at $(0,0)$, followed by compactness away from $(0,0)$, give the stated global polynomial bounds.

### 2.1 The fourth moment

Set $S_k(x,y)=\sum_{a=0}^k x^{k-a}y^a$. For $v_3$,


$$
(v_3(x)-v_3(y))\cot\frac{x-y}{2}
=2S_2-\alpha S_4-\frac16(x-y)^2S_2
 +O(|x|^6+|y|^6).
$$


The exact finite-degree sums are


$$
2\sum_{i<k}S_2=(2d-3)Q+X^2,
$$




$$
\sum_{i<k}S_4=(d-\tfrac52)Q_4+XC_3+\tfrac12Q^2,
$$




$$
\sum_{i<k}(x_i-x_k)^2S_2=dQ_4-XC_3.
$$


Meanwhile


$$
v_3'=3t^2-\frac{5\alpha}{2}t^4+O(t^6).
$$


Thus both finite-degree corrections cancel exactly against the derivative terms. Since $v_3h_q'=O(t^4)$, equation (5) gives


$$
\begin{aligned}
\alpha n(\mathbb EQ_4-\mathbb EQ_6/6)
={}&2d\,\mathbb EQ+\mathbb EX^2
-(\alpha+\tfrac16)d\,\mathbb EQ_4\\
&+(\tfrac16-\alpha)\mathbb E(XC_3)
-\frac{\alpha}{2}\mathbb EQ^2\\
&+O(n\mathbb EQ_8+d\mathbb EQ_6+\mathbb EQ_4).
\end{aligned}                                         \tag{6}
$$


In particular, the $h_q$ contribution has been bounded before absorption.

The centered product bounds needed in (6) are


$$
|\mathbb E(XC_3)|=O(d^2/n^2),
$$


and


$$
\mathbb EQ^2
=\frac{d^4}{\alpha^2n^2}
+O(d^5/n^3+d^2/n^2).                                  \tag{7}
$$


The second follows from the mean expansion and
$\operatorname{Var}Q=O(d^2/n^2)$; it is not an uncentered factorization assumption.

Put $T=1/6-\alpha$. The coefficient of $d^4/(\alpha^2n^2)$ on the right side of the equation solved for $\alpha n\mathbb EQ_4$ is


$$
2T+\frac56-2(\alpha+\tfrac16)-\frac{\alpha}{2}
=\frac56-\frac92\alpha.
$$


Therefore


$$
\boxed{
\mathbb EQ_4=
\frac{2d^3}{\alpha^2n^2}
+\frac{V}{\alpha^3}\frac{d^4}{n^3}
+O(d^2/n^2+d^5/n^4),\qquad
V=\frac56-\frac92\alpha .
}                                                       \tag{8}
$$



For clarity, the errors in (7), after their occurrence in (6) and division by $n$, are


$$
O(d^5/n^4+d^2/n^3).
$$


The errors from $2d\,\mathbb EQ$, the old $Q_4$ expansion, and the sharp $Q_6$ expansion contribute at most


$$
O(d^3/n^3+d^5/n^4).
$$


These are covered by the remainder in (8) for $2\le d=o(n)$.

### 2.2 The quadratic moment

For $v_1$, the paired expansion through degree four is


$$
\begin{aligned}
(v_1(x)-v_1(y))\cot\frac{x-y}{2}
={}&2-\alpha S_2-\frac16(x-y)^2\\
&+\frac{\alpha}{12}S_4
+\frac{\alpha}{12}(x-y)^2S_2
-\frac1{360}(x-y)^4\\
&+O(|x|^6+|y|^6).
\end{aligned}
$$


In addition to the preceding sums, use


$$
\sum_{i<k}(x_i-x_k)^4=dQ_4-4XC_3+3Q^2.
$$


The finite $Q_4$ contribution from $S_4$ is
$-5\alpha Q_4/24$, which cancels $+5\alpha Q_4/24$ from


$$
v_1'=1-\frac{3\alpha}{2}t^2+\frac{5\alpha}{24}t^4+O(t^6).
$$


The $XC_3$ terms proportional to $\alpha$ cancel each other. Since $v_1h_q'=O(t^2)$, the resulting identity is exactly


$$
\begin{aligned}
\alpha n(\mathbb EQ-\mathbb EQ_4/6+\mathbb EQ_6/120)
={}&d^2-(\alpha+\tfrac16)d\,\mathbb EQ
+(\tfrac16-\tfrac\alpha2)\mathbb EX^2\\
&+(\tfrac\alpha6-\tfrac1{360})d\,\mathbb EQ_4\\
&+(\tfrac\alpha{24}-\tfrac1{120})\mathbb EQ^2
+\tfrac1{90}\mathbb E(XC_3)\\
&+O(n\mathbb EQ_8+d\mathbb EQ_6+\mathbb EQ).
\end{aligned}                                         \tag{9}
$$



The next coefficient, after substitution of (8), is


$$
\begin{aligned}
U
&=\frac V6-\frac5{120}
-(\alpha+\tfrac16)T
+2(\tfrac\alpha6-\tfrac1{360})
+(\tfrac\alpha{24}-\tfrac1{120})\\
&=\alpha^2-\frac{3\alpha}{8}+\frac1{18}.
\end{aligned}
$$


Thus


$$
\boxed{
\mathbb EQ=
\frac{d^2}{\alpha n}
+\frac{T}{\alpha^2}\frac{d^3}{n^2}
+\frac{U}{\alpha^3}\frac{d^4}{n^3}
+O(d^2/n^2+d^5/n^4).
}                                                       \tag{10}
$$


In particular, the $h_q$ term contributes
$O(\mathbb EQ/n)=O(d^2/n^2)$. The $Q^2$ error in (7) again contributes only $O(d^5/n^4+d^2/n^3)$.

Equations (8) and (10) prove both proposals with their claimed errors.

## 3. First and second actual derivatives

### 3.1 Signed seventh trace

The already established safe-field recursion gives


$$
\mathbb EQ_{10}=O(d^6/n^5).
$$


Applying it once more, with $t^{11}g(t)/M$, gives


$$
\mathbb EQ_{12}=O(d^7/n^6).
$$


Consequently


$$
\mathbb EC_7^2\le Cn^{-1}\mathbb EQ_{12}=O(d^7/n^7).
$$


Reflection gives $\mathbb EC_7=0$. Keeping the phase and insertion defect separately, exactly as for $C_5$,


$$
|\mathbb E(\mathcal W_jC_7)|
\le \sqrt{\mathbb EC_7^2\,\mathbb E\Phi_q^2}
+\|S_j-1\|_\infty\sqrt{\mathbb EC_7^2}.
$$


Division by $N_j$ proves


$$
\boxed{\langle C_7\rangle_j=O(d^4/n^4).}                \tag{11}
$$


All signed odd terms through degree seven are therefore retained, rather than estimated by their absolute particle moments.

### 3.2 First derivative

Let $A=1+q$ and $h(t)=(e^{-it}+q)^{-1}$. Write its even coefficients as


$$
c_2=\frac{q-1}{2A^3},\qquad
c_4=\frac{(1-q)(q^2-10q+1)}{24A^5},
$$




$$
c_6=\frac{(q-1)(q^4-56q^3+246q^2-56q+1)}
                 {720A^7}.                            \tag{12}
$$


The expansion through degree seven includes imaginary odd terms and a remainder bounded by $C|t|^8$.

The centered actual corrections remain


$$
\langle Q\rangle_j-\mathbb EQ=O(d/n),\quad
\langle Q_4\rangle_j-\mathbb EQ_4=O(d^2/n^2),\quad
\langle Q_6\rangle_j-\mathbb EQ_6=O(d^3/n^3).
$$


Using (8), (10), turn21’s sharp $Q_6$, and the signed odd estimates gives


$$
\boxed{
\begin{aligned}
(\log A_j)'(q)
={}&\frac dA+\frac{c_2}{\alpha}\frac{d^2}{n}
+\frac{c_2T+2c_4}{\alpha^2}\frac{d^3}{n^2}\\
&+\frac{c_2U+c_4V+5c_6}{\alpha^3}\frac{d^4}{n^3}
+O(d/n+d^5/n^4).
\end{aligned}}                                         \tag{13}
$$


The degree-eight remainder costs $O(\mathbb EQ_8)=O(d^5/n^4)$. No mean-sized loss is introduced by complex normalization.

### 3.3 Second derivative

The exact identity remains


$$
(\log A_j^{\rm pr})''
=\left\langle-\sum_i h(\theta_i)^2\right\rangle_j
+\operatorname{Cov}_j\!\left(\sum_i h(\theta_i),
                              \sum_i h(\theta_i)\right).
$$


The covariance is algebraic, not positive; centering at the positive-measure mean bounds it by $O(d/n)$.

Since $\partial_q h=-h^2$, the needed even coefficients are


$$
c_2'=\frac{2-q}{A^4},\qquad
c_4'=\frac{q^3-18q^2+33q-8}{12A^6}.
$$


Expand through signed degree five and bound the remaining term by $CQ_6$. This yields


$$
\boxed{
(\log A_j)''(q)
=-\frac d{A^2}
+\frac{c_2'}{\alpha}\frac{d^2}{n}
+\frac{c_2'T+2c_4'}{\alpha^2}\frac{d^3}{n^2}
+O(d/n+d^4/n^3).
}                                                       \tag{14}
$$


As previously, a fixed number of characteristic derivatives adds only polynomial factors to the exponentially small particle outer-sector errors.

With $\epsilon=d/n$, the new errors contribute to stationary values at most


$$
\epsilon\,O(d/n+d^5/n^4)
=O(d^2/n^2+d^6/n^5)=o(1),
$$




$$
\epsilon^2\,O(d/n+d^4/n^3)
=O(d^3/n^3+d^6/n^5)=o(1)                              \tag{15}
$$


on (1). These are precisely the formerly unresolved losses.

## 4. Controlled fifth stationary comparison

There is one identification needed before using the exact equilibrium identity: the derivative coefficients just obtained must be those of the equilibrium characteristic phase, not merely a plausible Gaussian approximation.

For the explicit principal equilibrium $\mu_c$, let


$$
m_k(c)=\int \theta^k\,d\mu_c,\qquad c=d/n.
$$


Its support has size $O(\sqrt c)$. The continuum loop equation obtained from


$$
V_0'(\theta)=c\,\mathrm{PV}\!\int
                  \cot\frac{\theta-\phi}{2}\,d\mu_c(\phi)
$$


has the same symmetrized pair terms as (5), with the finite derivative terms absent. Symmetry removes odd moments. Expanding these equations, with support $O(\sqrt c)$, gives


$$
m_2(c)=\frac c\alpha+\frac T{\alpha^2}c^2
                        +\frac U{\alpha^3}c^3+O(c^4),
$$




$$
m_4(c)=\frac{2c^2}{\alpha^2}+\frac V{\alpha^3}c^3+O(c^4),
\qquad
m_6(c)=\frac{5c^3}{\alpha^3}+O(c^4).                    \tag{16}
$$


Here products such as $Q^2$ become products of equilibrium moments. Thus (16) is also a direct identification of the coefficients in (13)–(14) with those of $ncL_c^{(k)}(q)$.

For


$$
U_\pm(\zeta)=\log(s_jA_j(\sigma\pm\zeta)),
$$


include the chain sign in every odd derivative. Equations (13)–(14) and turn21’s third/fourth estimates match the equilibrium derivatives to the necessary orders.

More explicitly, on $|x|\le C\epsilon$, comparison of the increments at $\zeta=1+x$ gives an $o(1)$ error:

* first and second derivative losses are (15);
* the retained third-derivative loss is
  $O(d^4/n^4+d^6/n^5)$;
* the retained fourth-derivative loss is $O(n^{-1/10})$;
* the remaining insertion Taylor term is
  $O(d\epsilon^5)=O(d^6/n^5)$.

The base phases are identical in the actual and equilibrium comparisons. Uniform increment comparison therefore also compares their local stationary values: both stationary points are in this $O(\epsilon)$ neighborhood, and the real radial phases have positive curvature of order $n$.

Now use the exact archived identity


$$
\Phi_+(\zeta_+(c))-\Phi_-(\zeta_-(c))
=(2+c)\log M.
$$


Together with the retained actual reciprocal-anchor estimate


$$
U_-(1)-U_+(1)=-d\log M+O(d/n),
$$


this proves


$$
\boxed{
[nf_-(r_-)+U_-(r_-)]-[nf_+(r_+)+U_+(r_+)]
=-(2n+d)\log M+o(1).
}                                                       \tag{17}
$$



This is the actual fifth comparison. It is not merely an equality of formal fifth coefficients: the aggregate actual error has been shown to tend to zero on (1).

## 5. Full scalar forces and complete exponential-force review

The scalar integrals retain their original normalizations:


$$
P_j=\frac{n!}{2\pi}\int_{-\pi}^{\pi}
g(e^{is})^nA_j(\sigma+e^{is})\,ds,
$$




$$
F_j=2n!\int_{-\pi/4}^{\pi/4}
h(e^{is})^nA_j(\sigma-e^{is})\,ds.
$$


The retained scalar-contour interface includes the full signed particle sectors, remote scalar arcs, and **both connectors of the open minus contour**. Its local prefactor ratio is $M^{-1}(1+o(1))$; the original normalization ratio is $4\pi$. Thus (17) gives


$$
\frac{F_j}{P_j}=4\pi M^{-2n-b}(1+o(1)),
\qquad \operatorname{sign}P_j=\operatorname{sign}F_j=s_j. \tag{18}
$$



### Complete $eE_i$, located and bounded

The attached `LOGARITHMIC_FORCING_VECTOR`, §6, defines


$$
\boxed{
eE_i=-[z^{n+i}]Q_0(z)^n
          \int_0^1s^n e^{1-s+sz}\,ds,\qquad
Q_0(z)=1-z+z^2/2.
}                                                       \tag{19}
$$


This is the complete exponential forcing.

On $|z|=\sigma$,


$$
|Q_0(z)|\le2+\sigma=\sigma M,\qquad
|e^{1-s+sz}|\le e^\sigma.
$$


Cauchy’s coefficient estimate therefore gives, for every $i\ge0$,


$$
\sigma^i|eE_i|\le \frac{e^\sigma M^n}{n+1}.              \tag{20}
$$


Consequently the complete insertion


$$
E_j=\nu_{n,d}\!\left(
R_j\sum_{i=0}^d\sigma^ie_{d-i}(z^{-1})eE_i\right)
$$


satisfies, using $|e_k(z^{-1})|\le\binom dk$,


$$
|E_j|\le C B_j Z_d^{\rm abs}(0)
                    \frac{2^dM^n}{n+1}.               \tag{21}
$$


No selected entry or truncated exponential series replaces (19).

The retained scalar lower bound is


$$
|P_j|\ge C^{-1}n!n^{-1/2}M^nB_jZ_d^{\rm pr}(0)e^{-Cd}.
$$


The established absolute/principal partition comparison gives
$Z_d^{\rm abs}(0)\le2Z_d^{\rm pr}(0)$. Hence


$$
\boxed{|E_j/P_j|\le \frac{e^{Cb}}{n!\sqrt n}.}           \tag{22}
$$



For the endpoint, adjacent principal partitions satisfy


$$
Z_{d+1}^{\rm pr}(0)/Z_d^{\rm pr}(0)\le e^\sigma M^n:
$$


in the monic norm variational principle, the trial polynomial $z^d$ has modulus one on the circle. Together with the same absolute-partition and scalar bounds, this gives


$$
\boxed{
|D/P_0|\le\frac{C\sqrt n\,e^{Cb}}{n!B_0},
\qquad B_0=(n)_d\sigma^{-d}>1.
}                                                       \tag{23}
$$


Thus the original residual estimates are justified with the now-supplied complete $eE_i$, rather than assumed to follow from logarithmic forcing.

Both (22) and (23) are $o(M^{-2n-b})$ on (1).

## 6. Whole errors, normality, and actual diagonal metrics

The exact actual columns are


$$
u_j=(-1)^nP_j/D,\qquad
v_j-Su_j=\delta_{j0}+(-1)^nE_j/D-F_j/D.
$$


Therefore


$$
\boxed{
c_j-S=\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac D{P_j}.
}                                                       \tag{24}
$$


Equations (18), (22), and (23) prove (2) for the **whole** real error, including its eventual sign and nonvanishing.

The retained normality theorem applies because (1) eventually lies in $b\le n/1000$. Thus $D>0$; equation (18) also gives every actual $u_j\ne0$.

For any positive diagonal metric $W=\operatorname{diag}(w_j)$,


$$
c_W=\frac{u^TWv}{u^TWu},\qquad
c_W-S=\sum_j\frac{w_ju_j^2}{\sum_\ell w_\ell u_\ell^2}(c_j-S).
$$


Uniformity transfers (2) and nonvanishing to every such metric, even if its positive entries vary arbitrarily with $n,b$. No nondiagonal-metric conclusion is asserted.

### Precisely retained analytic dependencies

The new proof uses:

1. the actual reconstruction normalization and phase bounds (3), for $d=o(n)$;
2. the established moment/Poincaré and signed-odd estimates on the same principal tilted measure;
3. actual zero-free logarithms and fixed-neighborhood derivative bounds;
4. differentiated signed particle outer-sector bounds;
5. the original scalar-contour interface, including remote arcs, both minus connectors, local Gaussian error, and curvature prefactor;
6. turn21’s sharp $Q_6$ and third/fourth precisions;
7. the exact equilibrium stationary identity and actual reciprocal-anchor estimate.

The new moment and derivative estimates close the critical range **within these retained interfaces**. No proportional empirical convergence theorem is being substituted for the critical quantitative errors.

## 7. Primitive multiplier, final gcd, and whole evaluated form

For a rational positive diagonal metric, let $d_B$ be the least positive integer clearing the actual two-column matrix, and let $\Omega$ be an integral positive diagonal scaling of the metric. Define


$$
N_B=d_B[u,v],\qquad
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_B=A_B/g_B>0,\qquad p_B=H_B/g_B.
$$


The actual reduced denominator is $q_B$. The primitive multiplier is exactly $d_B^2/g_B$. On (1),


$$
\boxed{
\begin{aligned}
q_BS-p_B
&=\frac{d_B^2}{g_B}
 \bigl[(u^T\Omega u)S-u^T\Omega v\bigr]\\
&=(-1)^n4\pi q_BM^{-2n-b}(1+o(1))\ne0.
\end{aligned}}                                         \tag{25}
$$


Neither the clearing multiplier nor the final gcd has been estimated by this analytic argument.

## Closing ledger

1. **New result and proof status.**  
   Both proposed moment expansions pass, including their finite-degree cancellations, $h_q$ corrections, centered $Q^2$ errors, and full-interval remainders. The new signed seventh estimate completes the first derivative; the second derivative also has the required precision. Together with the retained third/fourth estimates, these prove the actual fifth stationary comparison. Using the explicitly listed prior scalar interfaces, the whole critical-$4/5$ relative $4\pi$ law follows on both parities, for all actual coordinates and positive diagonal metrics, with full forcing, endpoint, normality, and eventual nonvanishing retained.

2. **Exact remaining bottleneck.**  
   Irrationality of $e+\pi$ remains unresolved. A sufficient missing arithmetic statement is an infinite same-index sequence in this analytic domain for which the **actual denominator after the final gcd** satisfies
   

$$
q_BM^{-2n-b}\longrightarrow0.
$$


   Equation (25) would then give nonzero primitive forms tending to zero. Nothing proved here supplies that denominator bound.

3. **Computation request.**  
   None. The coefficient audit and critical error bounds above are analytic and symbolic; no finite computation is used to establish an infinite assertion.
