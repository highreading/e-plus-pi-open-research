> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Critical three-quarters scale: sharp virials and quartic cancellation

Write


$$
\sigma=\sqrt2,\qquad M=1+\sqrt2,\qquad \rho=M^{-1},
\qquad \alpha _0=\frac{\sigma}{M},\qquad d=b-1.
$$


The index domain throughout the conclusion is


$$
n\longrightarrow\infty,\qquad
\kappa _0n^{3/4}\le b\le\kappa _1n^{3/4},
\qquad 0\le j\le b,
\tag{1}
$$


where $0<\kappa _0<\kappa _1<\infty$ are fixed. Both parities are included.

**The proposed sharp moments and quartic coefficient are correct.** Below I prove the new moment and actual-derivative estimates. Together with the supplied reconstruction, normality, scalar-contour, and whole-residual interfaces, they give


$$
\boxed{
c_j-(e+\pi)=(-1)^{n+1}4\pi M^{-2n-b}(1+o(1)).
}
\tag{2}
$$


The estimate is uniform in (1), including every actual coordinate. It consequently holds for every positive diagonal metric in those same actual coordinates.

This is an analytic result within the explicitly retained prior interfaces. It does **not** prove irrationality of $e+\pi$, or supply a bound for the final primitive denominator.

## 1. The ensemble and actual denominator are unchanged

At $q=M,\rho$, use the positive principal measure


$$
d\mu_q\propto
|\Delta(e^{i\theta})|^2
\prod_{\ell=1}^d
g(\theta_\ell)^n e^{-\sigma\cos\theta_\ell}
|e^{-i\theta_\ell}+q|\,d\theta,
\qquad
g(t)=1+\sigma\cos t,
\tag{3}
$$


on $I^d$, where $I=(-3\pi/4,3\pi/4)$.

Retain the actual characteristic integral and reconstruction:


$$
A_j(q)=\nu_{n,d}\!\left(
R_j(z)\prod_{\ell=1}^d(z_\ell^{-1}+q)\right),
$$




$$
R_j(z)=[t^j](t-1)(1+D_t)^{-n}
             \prod_{\ell=1}^d(z_\ell+t/\sigma).
\tag{4}
$$


With the established normalization $S_j=s_jR_j/B_j$, put


$$
W_j=S_je^{i\Phi_q},\qquad N_j(q)=\mathbb E_qW_j,
$$




$$
\Phi_q=\sum_\ell\left[-\sigma\sin\theta_\ell+
                   \arg(e^{-i\theta_\ell}+q)\right].
\tag{5}
$$


The existing estimates, valid here since $d=o(n)$, are


$$
\|S_j-1\|_\infty=O(d/n),\qquad
\mathbb E_q\Phi_q^2=O(d/n),\qquad
N_j(q)=1+O(d/n).
\tag{6}
$$


In particular, $|N_j(q)|\ge1/2$ eventually. Every complex-weighted average below means


$$
\langle F\rangle_j=\frac{\mathbb E_q(W_jF)}{N_j(q)}.
\tag{7}
$$


Neither the insertion nor this denominator is discarded.

Write


$$
Q_{2r}=\sum_\ell\theta_\ell^{2r},\qquad Q=Q_2,\qquad
X=\sum_\ell\theta_\ell,\qquad C_3=\sum_\ell\theta_\ell^3.
$$


I reuse the established lower-order estimates


$$
\mathbb EQ=\frac{d^2}{\alpha _0n}+O(d^3/n^2),\quad
\mathbb EQ_4=O(d^3/n^2),\quad
\operatorname{Var}Q=O(d^2/n^2),\quad
\mathbb EX^2=O(d/n).
\tag{8}
$$



## 2. Endpoint-safe virials

Set


$$
V_q(t)=-n\log g(t)+h_q(t),\qquad
h_q(t)=\sigma\cos t-\log|e^{-it}+q|.
$$


The function $h_q$ is even and smooth on the closed principal interval, with uniformly bounded derivatives at both anchors. In particular,


$$
h_q'(t)=O(|t|).
\tag{9}
$$



For any of the safe fields used below, integration by parts gives


$$
\mathbb E\sum_i v(\theta_i)V_q'(\theta_i)
=
\mathbb E\sum_i v'(\theta_i)
+\mathbb E\sum_{i<k}
(v(\theta_i)-v(\theta_k))
\cot\frac{\theta_i-\theta_k}{2}.
\tag{10}
$$



### Boundary and collision justification

The fields


$$
v_{2r-1}(t)=t^{2r-1}g(t)/M,\qquad r=1,2,3,
\tag{11}
$$


vanish at both endpoints. The density already contains $g(t)^n$; thus the endpoint flux vanishes, and multiplication by $v$ cancels the pole of $-ng'/g$.

At a collision, the density has a quadratic Vandermonde zero. The difference $v(x)-v(y)$ removes the cotangent singularity in the paired expression. One can therefore integrate on truncated chambers and pass to the limit. No boundary value of the singular potential derivative is Taylor-expanded.

### 2.1 Sixth moment

Use $v_5=t^5g/M$. Its base-potential contribution is exactly


$$
v_5(t)\left(-n\frac{g'(t)}{g(t)}\right)
=\alpha _0n\,t^5\sin t.
$$


Since $\sin t/t$ has a positive minimum on $\overline I$,


$$
t^5\sin t\ge c t^6.
\tag{12}
$$


Also $v_5h_q'=O(t^6)$, $v_5'=O(t^4)$, and, uniformly on $\overline I^2$,


$$
\left|
(v_5(x)-v_5(y))\cot\frac{x-y}{2}
\right|
\le C(x^4+y^4).
\tag{13}
$$


For (13), use the divided difference of $v_5$, whose derivative is bounded by $C|t|^4$, and the bounded function
$(x-y)\cot((x-y)/2)$; the interval of differences is strictly inside $(-2\pi,2\pi)$.

Consequently (10) implies


$$
cn\,\mathbb EQ_6\le Cd\,\mathbb EQ_4+C\mathbb EQ_6.
$$


Absorbing the last term and using (8) proves


$$
\boxed{\mathbb EQ_6=O(d^4/n^3).}
\tag{14}
$$



### 2.2 Sharp fourth moment

Use $v_3=t^3g/M$. Uniformly on the entire principal interval,


$$
v_3(t)V_q'(t)
=\alpha _0nt^4+O(nt^6+t^4),\qquad
v_3'(t)=3t^2+O(t^4).
\tag{15}
$$


The paired expansion is


$$
(v_3(x)-v_3(y))\cot\frac{x-y}{2}
=2(x^2+xy+y^2)+O(x^4+y^4).
\tag{16}
$$


The remainder is globally bounded as stated: near the origin this follows by Taylor expansion, and away from the origin by compactness after removing the diagonal singularity.

The exact pair sum is


$$
2\sum_{i<k}(\theta_i^2+\theta_i\theta_k+\theta_k^2)
=(2d-3)Q+X^2.
\tag{17}
$$


Thus the derivative term $3Q$ combines with (17) to give $2dQ+X^2$, not a line-ensemble substitute. Equations (10), (14)–(17) yield


$$
\alpha _0n\,\mathbb EQ_4
=2d\,\mathbb EQ+\mathbb EX^2
+O(n\mathbb EQ_6+d\mathbb EQ_4).
$$


Using (8),


$$
\boxed{
\mathbb EQ_4
=\frac{2d^3}{\alpha _0^2n^2}
+O\!\left(\frac{d^2}{n^2}+\frac{d^4}{n^3}\right).
}
\tag{18}
$$



### 2.3 Sharp quadratic moment, including the circular correction

Now use $v_1=tg/M$. Its expansions are


$$
v_1V_q'
=\alpha _0n(t^2-t^4/6)+O(nt^6+t^2),
\qquad
v_1'=1-\frac{3\alpha _0}{2}t^2+O(t^4).
\tag{19}
$$


The essential circular pair expansion is


$$
\begin{aligned}
(v_1(x)-v_1(y))\cot\frac{x-y}{2}
={}&2-\alpha _0(x^2+xy+y^2)\\
&-\frac16(x-y)^2+O(x^4+y^4).
\end{aligned}
\tag{20}
$$


In particular, the cotangent correction $- (x-y)^2/6$ is retained.

The exact identities


$$
\sum_{i<k}(x_i^2+x_ix_k+x_k^2)
=(d-\tfrac32)Q+\tfrac12X^2,
$$




$$
\sum_{i<k}(x_i-x_k)^2=dQ-X^2
$$


show that the right side of (10) is


$$
d^2-(\alpha _0+\tfrac16)d\,\math EQ
+(\tfrac16-\tfrac{\alpha _0}{2})\math EX^2
+O(d\math EQ_4).
$$


Here the $3\alpha _0Q/2$ from the pair sum cancels the derivative correction in (19). Therefore


$$
\begin{aligned}
\alpha _0n\,\math EQ
={}&d^2+\frac{\alpha _0n}{6}\math EQ_4
-(\alpha _0+\tfrac16)d\,\math EQ\\
&+O(n\math EQ_6+d\math EQ_4+\math EQ+\math EX^2).
\end{aligned}
\tag{21}
$$


Insert (18) and the leading value of $\math EQ$ from (8). The coefficient is


$$
\frac13-\alpha _0-\frac16=\frac16-\alpha _0.
$$


It follows that


$$
\boxed{
\math EQ=\frac{d^2}{\alpha _0n}
+\left(\frac16-\alpha _0\right)
  \frac{d^3}{\alpha _0^2n^2}
+O\!\left(\frac{d^2}{n^2}+\frac{d^4}{n^3}\right).
}
\tag{22}
$$


This verifies all three proposed sharp moments in the same positive tilted ensemble.

## 3. Actual insertion and phase covariances

The Hessian lower bound $cnI$, together with (14), gives


$$
\operatorname{Var}Q_4
\le \frac Cn\math E\|\nabla Q_4\|^2
=\frac Cn\math EQ_6
=O(d^4/n^4).
\tag{23}
$$


Centering before weighting is crucial:


$$
\langle Q_{2r}\rangle_j-\math EQ_{2r}
=\frac{\math E[W_j(Q_{2r}-\math EQ_{2r})]}{N_j(q)}.
$$


Thus


$$
\boxed{
\langle Q\rangle_j=\math EQ+O(d/n),\qquad
\langle Q_4\rangle_j=\math EQ_4+O(d^2/n^2).
}
\tag{24}
$$


These bounds keep the full insertion and denominator; they introduce no multiple of the large mean.

The established signed estimates remain applicable:


$$
\langle X\rangle_j=O(d/n),\qquad
\langle C_3\rangle_j=O(d^2/n^2).
\tag{25}
$$


Finally, by Cauchy–Schwarz first in the particles and then in expectation,


$$
\math E\sum_i|\theta_i|^5
\le \sqrt{\math EQ_4\,\math EQ_6}
=O(d^{7/2}/n^{5/2}).
\tag{26}
$$



## 4. Sharp actual logarithmic derivatives

Put $A=1+q$, temporarily distinguishing this scalar from $A_j$.

### 4.1 First derivative

For $h(t)=(e^{-it}+q)^{-1}$, direct series inversion gives


$$
\operatorname{Re}h(t)=A^{-1}+c_2t^2+c_4t^4+O(|t|^5),
$$


where


$$
c_2=\frac{q-1}{2A^3},\qquad
c_4=\frac{(1-q)(q^2-10q+1)}{24A^5}.
\tag{27}
$$


For example the fourth coefficient before simplification is


$$
-\frac1{24A^2}+\frac7{12A^3}
-\frac3{2A^4}+\frac1{A^5},
$$


which equals (27). The imaginary linear and cubic terms are handled by (25).

The exact identity is


$$
(\log A_j^{\rm pr})'(q)
=\left\langle\sum_i h(\theta_i)\right\rangle_j.
$$


Using (18), (22), and (24)–(27) proves


$$
\boxed{
a_q=(\log A_j)'(q)
=\frac dA+\frac{d^2}{n}\frac{c_2}{\alpha _0}
+\frac{d^3}{n^2}
 \frac{c_2(1/6-\alpha _0)+2c_4}{\alpha _0^2}
+O(R_a),
}
\tag{28}
$$


with


$$
R_a=\frac dn+\frac{d^2}{n^2}+\frac{d^4}{n^3}
+\frac{d^{7/2}}{n^{5/2}}.
\tag{29}
$$


On (1),


$$
\frac dnR_a=O(n^{-1/8})=o(1).
\tag{30}
$$


Differentiated particle outer sectors contribute exponentially small errors, as in the supplied sector interface.

### 4.2 Second derivative and its algebraic covariance

Let


$$
H_q=\sum_i h(\theta_i),\qquad J_q=-\sum_i h(\theta_i)^2.
$$


Exact differentiation gives


$$
(\log A_j^{\rm pr})''=
\langle J_q\rangle_j+
\langle H_q^2\rangle_j-\langle H_q\rangle_j^2.
\tag{31}
$$


The quadratic coefficient in $-h(t)^2$ is


$$
-\frac{2c_2}{A}+\frac1{A^4}
=\frac{2-q}{A^4}.
$$


Signed linear/cubic control and the fourth-moment bound therefore give


$$
\langle J_q\rangle_j
=-\frac d{A^2}+\frac{2-q}{A^4}\frac{d^2}{\alpha _0n}
+O(d/n+d^3/n^2).
\tag{32}
$$



For the covariance, center $H_q$ at its **positive-measure** mean. Brascamp–Lieb applied to its real and imaginary parts gives


$$
\math E|H_q-\math EH_q|^2=O(d/n).
$$


Since $W_j$ is bounded and $N_j$ is bounded away from zero,


$$
\left|\langle H_q^2\rangle_j-\langle H_q\rangle_j^2\right|
=O(d/n).
\tag{33}
$$


Consequently


$$
\boxed{
\beta_q=(\log A_j)''(q)
=-\frac d{A^2}
+\frac{d^2}{n}\frac{2-q}{\alpha _0A^4}
+O(d/n+d^3/n^2).
}
\tag{34}
$$


The remainder times $d^2/n^2$ tends to zero on (1).

### 4.3 Third derivative

Exact differentiation once more gives


$$
(\log A_j^{\rm pr})'''
=\langle K_q\rangle_j
+3\operatorname{Cov}_j(H_q,J_q)
+\operatorname{Cum}_{3,j}(H_q),
\qquad K_q=2\sum_i h(\theta_i)^3.
\tag{35}
$$


Here


$$
\langle K_q\rangle_j
=\frac{2d}{A^3}+O(d^{3/2}/\sqrt n).
$$


The covariance is $O(d/n)$, by the same centered argument as (33). Strong log-concavity gives the centered third absolute moment


$$
\math E|H_q-\math EH_q|^3=O((d/n)^{3/2});
$$


this follows from the standard sub-Gaussian concentration consequence for a $C\sqrt d$-Lipschitz statistic under the Hessian bound $cnI$. Bounded $W_j/N_j$ transfers this bound to the centered complex cumulant in (35).

Thus


$$
\boxed{
(\log A_j)'''(q)=\frac{2d}{A^3}
+O\!\left(d^{3/2}/\sqrt n+d/n+(d/n)^{3/2}\right).
}
\tag{36}
$$


Its remainder times $d^3/n^3$ is $O(n^{-1/8})$. For $U_\pm(\zeta)=\log(s_jA_j(\sigma\pm\zeta))$, the leading third derivative has the corresponding chain sign $\pm2d/A^3$.

## 5. Quartic stationary value: independent coefficient check

Let $\epsilon=d/n$. At either anchor write the coefficients from (28), (34), and (36) as


$$
a=n(a_1\epsilon+a_2\epsilon^2+a_3\epsilon^3)+\text{error},
$$




$$
\beta=n(b_1\epsilon+b_2\epsilon^2)+\text{error},
\qquad U'''=ng_1\epsilon+\text{error}.
$$


The chain signs are included in $a_i,g_1$, but not in $b_i$.

For the radial base phase,


$$
f''(1)=\alpha,\qquad f_3=-3\alpha,\qquad
f_4=12\alpha-3\alpha^2.
\tag{37}
$$


Solving the stationary equation through order $\epsilon^2$ gives


$$
x_1=-a_1/\alpha,\qquad
x_2=-\frac{a_2+b_1x_1+f_3x_1^2/2}{\alpha}.
$$


Substitution into the stationary value gives the fourth coefficient


$$
C_4=-\frac{\alpha x_2^2}{2}
+\frac{f_4x_1^4}{24}
+a_3x_1+\frac{b_2x_1^2}{2}
+\frac{g_1x_1^3}{6}.
\tag{38}
$$



Using $1+M=\sigma M$, $1+\rho=\sigma$, and $\sigma^2=2$, I obtain


$$
\begin{array}{c|cc}
&+&-\\ \hline
x_1&-1/2&(\sigma-1)/2\\
x_2&1/4&(3-2\sigma)/4
\end{array}
$$


and the five terms of (38), in order, are


$$
\begin{array}{c|cc}
&+&-\\ \hline
1&-1/16+\sigma/32&-5/16+7\sigma/32\\
2&1/64&17/64-3\sigma/16\\
3&-7/16+5\sigma/16&-3/16+\sigma/8\\
4&3/8-17\sigma/64&1/8-5\sigma/64\\
5&-5/48+7\sigma/96&-5/48+7\sigma/96
\end{array}
$$


Thus, independently of treating the receipt as authority,


$$
\boxed{C_{4,+}=C_{4,-}=\frac{-41+29\sqrt2}{192}.}
\tag{39}
$$



The coefficient errors in (28), (34), and (36) contribute $o(1)$ by their respective multipliers $\epsilon,\epsilon^2,\epsilon^3$. The supplied fixed-neighborhood holomorphic derivative bounds $U^{(k)}=O(d)$ control the remaining Taylor terms by


$$
O(n\epsilon^5)=O(d^5/n^4)=o(1).
$$


The stationary displacement omitted after $x_2\epsilon^2$ has no larger effect. Hence this is a controlled stationary-value expansion, not just coefficient algebra.

Reusing the established quadratic and cubic cancellations and the actual reciprocal-anchor comparison,


$$
U_-(1)-U_+(1)=-d\log M+O(d/n),
$$


we conclude


$$
\boxed{
[nf_-(r_-)+U_-(r_-)]-[nf_+(r_+)+U_+(r_+)]
=-(2n+d)\log M+o(1).
}
\tag{40}
$$



## 6. Full forces, whole errors, and actual metrics

The scalar forces remain exactly


$$
P_j=\frac{n!}{2\pi}\int_{-\pi}^{\pi}
g(e^{is})^nA_j(\sigma+e^{is})\,ds,
$$




$$
F_j=2n!\int_{-\pi/4}^{\pi/4}
h(e^{is})^nA_j(\sigma-e^{is})\,ds.
\tag{41}
$$


The supplied scalar-contour interface applies since $d=o(n)$: it retains all signed particle outer sectors, remote scalar arcs, and both radial connectors of the open minus contour. Its curvature ratio gives $M^{-1}(1+o(1))$; the original scalar normalization ratio is $4\pi$. Combining this with (40),


$$
F_j/P_j=4\pi M^{-2n-b}(1+o(1)),
\qquad \operatorname{sign}P_j=\operatorname{sign}F_j=s_j.
\tag{42}
$$



The complete exponential force is


$$
E_j=\nu_{n,d}\!\left(
R_j\sum_{i=0}^d\sigma^i e_{d-i}(z^{-1})eE_i
\right).
$$


The actual column identities are


$$
u_j=(-1)^nP_j/D,\qquad
v_j-(e+\pi)u_j=\delta_{j0}+(-1)^nE_j/D-F_j/D.
$$


Therefore the **whole** coordinate error is


$$
c_j-(e+\pi)
=\frac{E_j}{P_j}+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac D{P_j}.
\tag{43}
$$


The supplied whole-residual and endpoint bounds


$$
|E_j/P_j|\le \frac{e^{Cb}}{n!\sqrt n},\qquad
|D/P_0|\le\frac{C\sqrt n\,e^{Cb}}{n!B_0},
\quad B_0=(n)_d\sigma^{-d}>1,
$$


are $o(M^{-2n-b})$ on (1). This proves (2), including eventual whole-error nonvanishing. Normality gives $D>0$, and (42) gives every $u_j\ne0$.

For any positive diagonal actual-coordinate metric $W$,


$$
c_W-(e+\pi)
=\sum_j\frac{W_{jj}u_j^2}{\sum_\ell W_{\ell\ell}u_\ell^2}
       (c_j-(e+\pi)).
$$


Uniformity therefore transfers (2) and its nonvanishing to $c_W$. No assertion about general nondiagonal metrics is made.

## 7. Primitive multiplier, final gcd, and evaluated real error

For a rational positive diagonal metric, retain the least positive integer $d_B$ clearing the actual two-column matrix and an integral positive diagonal metric scaling $\Omega$:


$$
N_B=d_B[u,v].
$$


Define


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_B=A_B/g_B>0,\qquad p_B=H_B/g_B.
$$


The actual reduced denominator is $q_B$, and the primitive multiplier is exactly $d_B^2/g_B$. On (1),


$$
\boxed{
\begin{aligned}
q_B(e+\pi)-p_B
&=\frac{d_B^2}{g_B}
 \bigl[(u^T\Omega u)(e+\pi)-u^T\Omega v\bigr]\\
&=(-1)^n4\pi q_BM^{-2n-b}(1+o(1))\ne0.
\end{aligned}}
\tag{44}
$$


No estimate for $d_B$, $g_B$, or $q_B$ is inferred from the quartic cancellation.

## Closing ledger

1. **New result and proof status.**  
   Proved the sharp moments (14), (18), and (22) by endpoint-safe virials in the same positive tilted ensemble. Proved the required actual derivative expansions, including centered $Q,Q_4$ covariances, signed odd traces, the full phase denominator, and the algebraic second-derivative covariance. Independently verified the equal quartic coefficients (39). **Using the supplied prior contour and complete-residual interfaces**, this proves the critical-three-quarters whole relative law (2), with actual-coordinate diagonal metrics and eventual nonvanishing. No extension to $b=o(n^{4/5})$ is asserted.

2. **Exact remaining bottleneck.**  
   Irrationality remains unresolved. A sufficient missing arithmetic statement is an infinite same-index sequence for which the **actual reduced denominator after the final gcd** obeys
   

$$
q_BM^{-2n-b}\longrightarrow0.
$$


   Together with (44), this would contradict rationality. The analytic theorem supplies neither this bound nor a substitute for it.

3. **Computation request.**  
   None. The quartic calculation above is symbolic, and the infinite-scale conclusion uses the proved moment and remainder estimates—not finite numerical evidence.
