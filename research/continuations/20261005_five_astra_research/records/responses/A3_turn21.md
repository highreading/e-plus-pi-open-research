> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## Critical four-fifths scale: a sharp sixth moment and two completed derivative precisions

Write


$$
\sigma=\sqrt2,\quad M=1+\sqrt2,\quad \rho=M^{-1},
\quad \alpha=\frac{\sigma}{M},\quad d=b-1.
$$


The target index domain is


$$
n\to\infty,\qquad
\kappa _0n^{4/5}\le b\le\kappa _1n^{4/5},\qquad
0\le j\le b,
\tag{1}
$$


with fixed $0<\kappa _0\le\kappa _1<\infty$, integer indices, and both parities.

**I do not close the critical-scale assertion.** The exact equilibrium stationary-value identity supplied in the question makes the *formal difference* of fifth coefficients zero. It does not bound the corresponding actual finite-$n$ error. Below I prove a bounded follow-on result: the sharp sixth moment, its centered actual-weight transfer, and the required third- and fourth-logarithmic-derivative precisions. The missing quantities are narrowed to the next fourth-moment coefficient and second quadratic-moment correction, needed for the first two derivatives.

No actual critical-scale $4\pi$ law or irrationality conclusion is asserted.

### 1. Actual measure, insertion, and normalization

At $q=M,\rho$, retain the principal positive measure


$$
d\mu_q\propto |\Delta(e^{i\theta})|^2
 \prod_{\ell=1}^d
 (1+\sigma\cos\theta_\ell)^n
 e^{-\sigma\cos\theta_\ell}|e^{-i\theta_\ell}+q|\,d\theta
$$


on $I^d$, $I=(-3\pi/4,3\pi/4)$. Put


$$
A_j(q)=\nu_{n,d}\!\left(R_j(z)\prod_\ell(z_\ell^{-1}+q)\right),
\quad
R_j(z)=[t^j](t-1)(1+D_t)^{-n}
             \prod_\ell(z_\ell+t/\sigma).
$$


With the supplied exact normalization $S_j=s_jR_j/B_j$, define


$$
\mathcal W_j=S_je^{i\Phi_q},\qquad
N_j(q)=\mathbb E_q\mathcal W_j,\qquad
\langle F\rangle_j=\frac{\mathbb E_q(\mathcal W_jF)}{N_j(q)}.
\tag{2}
$$


The retained bounds are


$$
\|S_j-1\|_\infty=O(d/n),\quad
\mathbb E_q\Phi_q^2=O(d/n),\quad
N_j(q)=1+O(d/n).
\tag{3}
$$


Thus $|N_j|\ge1/2$ eventually. Every weighted estimate below retains this denominator.

Let


$$
p_k=\sum_i\theta_i^k,\qquad Q_{2r}=p_{2r},\qquad X=p_1.
$$



## 2. New sharp sixth-moment lemma

Uniformly for $2\le d=o(n)$ and both anchors,


$$
\boxed{
\mathbb E_qQ_6
=\frac{5d^4}{\alpha^3n^3}
+O\!\left(\frac{d^3}{n^3}+\frac{d^5}{n^4}\right).
}
\tag{4}
$$


In particular, the coefficient $5$ is proved here by the circular loop identity, not assumed from a Gaussian Catalan model.

### Proof

Write


$$
g(t)=1+\sigma\cos t,\qquad
V_q(t)=-n\log g(t)+h_q(t),
$$


where $h_q'(t)=O(t)$. Use the endpoint-safe field


$$
v(t)=t^5g(t)/M.
$$


The exact circular integration-by-parts identity is


$$
\mathbb E\sum_i v(\theta_i)V_q'(\theta_i)
=
\mathbb E\sum_i v'(\theta_i)
+\mathbb E\sum_{i<k}
 (v(\theta_i)-v(\theta_k))
 \cot\frac{\theta_i-\theta_k}{2}.
\tag{5}
$$


Endpoint fluxes vanish because $v$ vanishes there; collision fluxes vanish by the quadratic Vandermonde zero.

Uniformly on the closed interval and its square,


$$
v(t)V_q'(t)=\alpha nt^6+O(nt^8+t^6),\qquad
v'(t)=5t^4+O(t^6),
$$


and


$$
(v(x)-v(y))\cot\frac{x-y}{2}
=2\sum_{a=0}^4x^{4-a}y^a+O(x^6+y^6).
\tag{6}
$$


The remainder includes the circular cotangent correction; it is not replaced by a line-ensemble identity. Its global bound follows by removing the diagonal singularity and using compactness away from the origin.

The exact finite-degree pair sum is


$$
2\sum_{i<k}\sum_{a=0}^4\theta_i^{4-a}\theta_k^a
=2dQ_4+2Xp_3+Q_2^2-5Q_4.
$$


The derivative contribution $5Q_4$ cancels its final term. Therefore


$$
\alpha n\,\mathbb EQ_6
=2d\,\mathbb EQ_4+\mathbb EQ_2^2
 +2\mathbb E(Xp_3)
 +O(n\mathbb EQ_8+d\mathbb EQ_6).
\tag{7}
$$



Use the supplied, previously derived lower moments:


$$
\mathbb EQ_4=\frac{2d^3}{\alpha^2n^2}
 +O(d^2/n^2+d^4/n^3),
$$




$$
\mathbb EQ_2=\frac{d^2}{\alpha n}+O(d^3/n^2),
\qquad \operatorname{Var}Q_2=O(d^2/n^2),
$$


and


$$
\mathbb EX^2=O(d/n),\quad
\mathbb Ep_3^2=O(d^3/n^3),\quad
\mathbb EQ_8=O(d^5/n^4).
$$


Consequently


$$
\mathbb EQ_2^2
=\frac{d^4}{\alpha^2n^2}
 +O(d^5/n^3+d^2/n^2),
\qquad
|\mathbb E(Xp_3)|=O(d^2/n^2).
$$


Substitution into (7), followed by division by $\alpha n$, proves (4). The two leading contributions are explicitly $4+1=5$. ∎

### Centered actual-weight transfer

The safe field $t^9g(t)/M$, by the same coercive estimate, gives


$$
\mathbb EQ_{10}\le C(d/n)\mathbb EQ_8
=O(d^6/n^5).
$$


Brascamp–Lieb then yields


$$
\operatorname{Var}Q_6
\le \frac Cn\mathbb EQ_{10}=O(d^6/n^6).
$$


Centering before inserting $\mathcal W_j$,


$$
\langle Q_6\rangle_j-\mathbb EQ_6
=\frac{\mathbb E[\mathcal W_j(Q_6-\mathbb EQ_6)]}{N_j},
$$


so


$$
\boxed{
\langle Q_6\rangle_j
=\frac{5d^4}{\alpha^3n^3}
+O\!\left(\frac{d^3}{n^3}+\frac{d^5}{n^4}\right).
}
\tag{8}
$$


There is no loss proportional to the mean $d^4/n^3$.

## 3. Third derivative through its required correction

Put $A=1+q$, $h(t)=(e^{-it}+q)^{-1}$, and


$$
H=\sum_i h(\theta_i),\quad
J=-\sum_i h(\theta_i)^2,\quad
K=2\sum_i h(\theta_i)^3.
$$


Exact differentiation gives


$$
(\log A_j^{\rm pr})'''
=\langle K\rangle_j
+3\operatorname{Cov}_j(H,J)+\operatorname{Cum}_{3,j}(H).
\tag{9}
$$



From


$$
h(t)=A^{-1}+iA^{-2}t+\frac{q-1}{2A^3}t^2+O(t^3),
$$


the quadratic coefficient of $2h^3$ is


$$
\frac{6}{A^2}\frac{q-1}{2A^3}-\frac6{A^5}
=\frac{3(q-3)}{A^5}.
$$


Expanding through the cubic term, using the retained signed bounds for $X,p_3$, and bounding the fourth-order remainder by $CQ_4$, gives


$$
\langle K\rangle_j
=\frac{2d}{A^3}
+\frac{3(q-3)}{\alpha A^5}\frac{d^2}{n}
+O(d/n+d^3/n^2).
$$


The centered covariance and third cumulant in (9) are respectively
$O(d/n)$ and $O((d/n)^{3/2})$. The latter is absorbed by $O(d/n)$ when $d=o(n)$. Including the exponentially small differentiated outer sectors,


$$
\boxed{
(\log A_j)'''(q)
=\frac{2d}{(1+q)^3}
+\frac{3(q-3)}{\alpha(1+q)^5}\frac{d^2}{n}
+O\!\left(\frac dn+\frac{d^3}{n^2}\right).
}
\tag{10}
$$


At (1), the stationary-value loss is


$$
\frac{d^3}{n^3}
 O(d/n+d^3/n^2)
=O(d^4/n^4+d^6/n^5)=o(1).
\tag{11}
$$


For $U_\pm(\zeta)=\log(s_jA_j(\sigma\pm\zeta))$, both displayed coefficients acquire the third-order chain sign.

## 4. Fourth derivative at the required precision

Let $L=-6\sum_i h(\theta_i)^4$. The exact fourth derivative is


$$
\begin{aligned}
(\log A_j^{\rm pr})''''={}&\langle L\rangle_j
+4\operatorname{Cov}_j(H,K)+3\operatorname{Cov}_j(J,J)\\
&+6\operatorname{Cum}_j(H,H,J)+\operatorname{Cum}_{4,j}(H).
\end{aligned}
\tag{12}
$$


Every one-particle function here has bounded derivative. Centering at the positive-measure means, the variance inequality gives second moments $O(d/n)$. Applying it to squares of real centered components gives fourth moments $O((d/n)^2)$. Hölder's inequality, together with bounded $\mathcal W_j/N_j$, therefore bounds the covariance terms by $O(d/n)$, third cumulants by $O((d/n)^{3/2})$, and fourth cumulants by $O((d/n)^2)$.

Meanwhile


$$
|\langle L\rangle_j+6d/A^4|
\le C\mathbb E\sum_i|\theta_i|
\le C\sqrt{d\,\mathbb EQ_2}
=O(d^{3/2}/\sqrt n).
$$


Thus, also for the full functional,


$$
\boxed{
(\log A_j)''''(q)
=-\frac{6d}{(1+q)^4}
+O\!\left(\frac{d^{3/2}}{\sqrt n}+\frac dn\right).
}
\tag{13}
$$


The fourth-order chain factor is $(\pm1)^4=1$; there is no additional minus-chain sign. On (1), its omitted contribution is


$$
\frac{d^4}{n^4}
 O(d^{3/2}/\sqrt n+d/n)=O(n^{-1/10})=o(1).
\tag{14}
$$



## 5. Exact obstruction to the fifth stationary conclusion

The supplied equilibrium identity


$$
\Phi_+(\zeta_+(c))-\Phi_-(\zeta_-(c))
=(2+c)\log M
$$


already implies zero fifth coefficient in the **formal equilibrium difference**. I do not repeat that formal cancellation.

What is still missing is an actual finite-$n$ derivation of


$$
\mathbb EQ_4
=\frac{2d^3}{\alpha^2n^2}
+\boxed{\text{explicit coefficient}}\frac{d^4}{n^3}
+\text{controlled error},
$$


and


$$
\mathbb EQ_2
=\frac{d^2}{\alpha n}
+\frac{1/6-\alpha}{\alpha^2}\frac{d^3}{n^2}
+\boxed{\text{explicit coefficient}}\frac{d^4}{n^3}
+\text{controlled error}.
\tag{15}
$$


These require the next safe-field expansions, including their circular pair corrections and mixed centered products. Equation (8) supplies one required input, but not both coefficients in (15).

Without (15), the errors in the first and second logarithmic derivatives still allow


$$
\frac dn\,O(d^4/n^3)
\quad\hbox{and}\quad
\frac{d^2}{n^2}\,O(d^3/n^2),
$$


both of order $d^5/n^4$, hence potentially order one on (1). The completed estimates (10) and (13) do not remove those losses.

## 6. Complete forces and arithmetic scope retained

The actual forces remain


$$
P_j=\frac{n!}{2\pi}\int_{-\pi}^{\pi}
 g(e^{is})^nA_j(\sigma+e^{is})\,ds,\qquad
F_j=2n!\int_{-\pi/4}^{\pi/4}
 h(e^{is})^nA_j(\sigma-e^{is})\,ds,
$$


and


$$
E_j=\nu_{n,d}\!\left(
 R_j\sum_{i=0}^d\sigma^ie_{d-i}(z^{-1})eE_i\right).
$$


With $D=\det H_b$, the actual columns satisfy


$$
u_j=(-1)^nP_j/D,\qquad
v_j-Su_j=\delta_{j0}+(-1)^nE_j/D-F_j/D.
$$


Whenever $P_j\ne0$, the whole error is exactly


$$
c_j-S=\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac D{P_j}.
\tag{16}
$$


Neither $E_j$ nor the endpoint is removed. The original remote sectors and minus connectors must likewise remain in any eventual scalar conclusion.

For the actual columns and a positive diagonal metric $W$,


$$
c_W=\frac{u^TWv}{u^TWu}.
$$


For rational such metrics, let $d_B$ be the least integer clearing $[u,v]$, and let $\Omega$ be an integral positive diagonal scaling. Retain


$$
N_B=d_B[u,v],\quad
A_B=N_{B,1}^T\Omega N_{B,1},\quad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\quad q_B=A_B/g_B,\quad p_B=H_B/g_B.
$$


When $A_B>0$, the actual reduced denominator is $q_B$, the primitive multiplier is $d_B^2/g_B$, and the whole evaluated error is exactly


$$
\boxed{
q_BS-p_B
=\frac{d_B^2}{g_B}
 \bigl[(u^T\Omega u)S-u^T\Omega v\bigr].
}
\tag{17}
$$


This report proves no new critical-scale nonvanishing of (16) or (17), and no estimate for $q_B$.

### Closing ledger

1. **New result and proof status.**  
   Proved the sharp sixth moment (4), its actual-weight version (8), the corrected third derivative (10), and the fourth derivative (13), with errors negligible after their required critical-scale multipliers. These results retain circular interactions, finite-degree terms, centered losses, and the actual complex denominator.

2. **Exact remaining bottleneck.**  
   Derive the two explicit moment coefficients in (15) with sufficient errors, then complete the first two actual derivative expansions and compare their fifth stationary contribution with the exact equilibrium identity. The critical whole relative law remains unproved here. Irrationality additionally requires same-index control of the actual reduced denominator after the final gcd and nonzero whole primitive errors tending to zero.

3. **Computation request.**  
   None. The remaining task is an analytic finite-$n$ moment calculation; finite numerical evidence would not establish its required uniform error bounds.
