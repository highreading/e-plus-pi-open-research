> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Below four-fifths degree: signed fifth control closes the new remainder estimates

Put


$$
\sigma=\sqrt2,\qquad M=1+\sqrt2,\qquad \rho=M^{-1},
\qquad \alpha _0=\sigma/M,\qquad d=b-1,\qquad S=e+\pi.
$$


The index domain for the resulting relative law is


$$
\boxed{n\to\infty,\qquad 3\le b=o(n^{4/5}),\qquad 0\le j\le b,}
\tag{1}
$$


with integer indices and both parities. Uniformity means, in particular, uniformity over $3\le b\le\eta_n n^{4/5}$ for each positive sequence $\eta_n\to0$.

**The proposed signed-fifth improvement closes.** The new estimates proved below remove both remainder obstructions identified in the critical-$3/4$ report. Combined with the retained scalar-contour and complete-residual interfaces, they yield


$$
\boxed{
c_j-S=(-1)^{n+1}4\pi M^{-2n-b}
\left[1+O\!\left(\frac bn+\frac{b^5}{n^4}+n^{-1/5}\right)\right].
}
\tag{2}
$$


The same estimate holds uniformly for every positive diagonal metric in the actual coordinates. All whole errors and first-column coordinates are eventually nonzero.

The distinction in proof status is important: the signed-fifth and third-derivative estimates below are proved directly. The passage to (2) uses the same fixed-neighborhood logarithm, scalar-contour, and complete-residual estimates stated in the supplied prior reports; those interfaces are not replaced by a positive-ensemble approximation. No assertion at critical $b\asymp n^{4/5}$, and no irrationality conclusion, follows here.

## 1. Actual insertion, measure, and denominator

Retain exactly


$$
A_j(q)=\nu_{n,d}\!\left(
R_j(z)\prod_{\ell=1}^d(z_\ell^{-1}+q)\right),
$$




$$
R_j(z)=[t^j](t-1)(1+D_t)^{-n}
             \prod_{\ell=1}^d(z_\ell+t/\sigma),
\qquad
B_j=|K_{j,d}|\sigma^{-d},\qquad S_j=s_jR_j/B_j.
$$


At either real anchor $q=M,\rho$, let $\mu_q$ be the same positive principal measure


$$
d\mu_q\propto
|\Delta(e^{i\theta})|^2
\prod_{\ell=1}^d
g(\theta_\ell)^n e^{-\sigma\cos\theta_\ell}
|e^{-i\theta_\ell}+q|\,d\theta,
\quad
g(t)=1+\sigma\cos t,
$$


on $I^d$, $I=(-3\pi/4,3\pi/4)$. Write


$$
\Phi_q=\sum_\ell\left[-\sigma\sin\theta_\ell+
                  \arg(e^{-i\theta_\ell}+q)\right],
\quad
\mathcal W_j=S_je^{i\Phi_q},
\quad N_j(q)=\mathbb E_q\mathcal W_j.
$$


Every actual weighted expectation in this answer is


$$
\boxed{\langle F\rangle_j=\frac{\mathbb E_q(\mathcal W_jF)}{N_j(q)}.}
\tag{3}
$$



The retained estimates, uniformly for $2\le d=o(n)$, are


$$
\|S_j-1\|_\infty=O(d/n),\qquad
\mathbb E_q\Phi_q^2=O(d/n),\qquad
N_j(q)=1+O(d/n).
\tag{4}
$$


Thus $|\mathcal W_j|\le C$ and $|N_j(q)|\ge1/2$ eventually. In particular, the complex normalization in (3) is never dropped.

Use the notation


$$
Q_{2r}=\sum_\ell\theta_\ell^{2r},\qquad Q=Q_2,
\qquad X=\sum_\ell\theta_\ell,\qquad
C_{2r+1}=\sum_\ell\theta_\ell^{2r+1}.
$$



## 2. New eighth-moment and signed-fifth bounds

### 2.1 Endpoint-safe eighth moment

Write


$$
V_q(t)=-n\log g(t)+h_q(t),\qquad
h_q(t)=\sigma\cos t-\log|e^{-it}+q|.
$$


At the two anchors, $h_q$ is even with $h_q'(t)=O(|t|)$ uniformly on $\overline I$.

Apply the retained integration-by-parts identity


$$
\mathbb E\sum_i v(\theta_i)V_q'(\theta_i)
=
\mathbb E\sum_i v'(\theta_i)
+
\mathbb E\sum_{i<k}
(v(\theta_i)-v(\theta_k))
\cot\frac{\theta_i-\theta_k}{2}
\tag{5}
$$


to the new safe field


$$
v_7(t)=t^7g(t)/M.
$$


It vanishes at both endpoints, and


$$
v_7(t)\left(-n\frac{g'(t)}{g(t)}\right)
=\alpha _0n\,t^7\sin t\ge c n t^8.
$$


The remaining terms satisfy


$$
v_7h_q'=O(t^8),\qquad v_7'=O(t^6),
$$


and


$$
\left|(v_7(x)-v_7(y))\cot\frac{x-y}{2}\right|
\le C(x^6+y^6).
\tag{6}
$$


Indeed, $v_7'=O(|t|^6)$, while
$(x-y)\cot((x-y)/2)$ is bounded for $x,y\in\overline I$, with its diagonal value defined by continuity.

Endpoint fluxes vanish because $v_7$ vanishes there and the density contains $g^n$. Collision fluxes vanish by the quadratic Vandermonde zero; the paired expression (6) is nonsingular. Consequently


$$
cn\,\mathbb EQ_8\le Cd\,\mathbb EQ_6+C\mathbb EQ_8.
$$


Using the established $\mathbb EQ_6=O(d^4/n^3)$ and absorbing the last term gives


$$
\boxed{\mathbb EQ_8=O(d^5/n^4).}
\tag{7}
$$



### 2.2 Signed fifth trace with the actual weight

Reflection gives $\mathbb EC_5=0$. On an ordered chamber the Hessian lower bound is $cnI$, and


$$
\|\nabla C_5\|^2=25Q_8.
$$


Thus Brascamp–Lieb and (7) imply


$$
\boxed{
\mathbb EC_5^2=\operatorname{Var}C_5
\le \frac Cn\mathbb EQ_8
=O(d^5/n^5).
}
\tag{8}
$$



Retaining both the insertion defect and phase,


$$
\begin{aligned}
|\mathbb E(\mathcal W_jC_5)|
&\le
|\mathbb E[C_5(e^{i\Phi_q}-1)]|
+\mathbb E[|S_j-1||C_5|]\\
&\le
\sqrt{\mathbb EC_5^2\,\mathbb E\Phi_q^2}
+\|S_j-1\|_\infty\sqrt{\mathbb EC_5^2}\\
&=O(d^3/n^3)+O(d^{7/2}/n^{7/2}).
\end{aligned}
$$


Division by the actual $N_j(q)$, using $d/n\to0$, proves


$$
\boxed{\langle C_5\rangle_j=O(d^3/n^3).}
\tag{9}
$$


No reflection symmetry of $S_j$ has been assumed.

## 3. Improved first logarithmic derivative

Let $A=1+q$ and


$$
h(t)=(e^{-it}+q)^{-1}.
$$


On the full principal interval its Taylor expansion through degree five has the form


$$
h(t)=A^{-1}+\frac{i}{A^2}t+c_2t^2
+i\gamma_3t^3+c_4t^4+i\gamma_5t^5+\mathcal R_6(t),
\quad
|\mathcal R_6(t)|\le C|t|^6,
\tag{10}
$$


where the coefficients are real and bounded at the two anchors, and


$$
c_2=\frac{q-1}{2A^3},\qquad
c_4=\frac{(1-q)(q^2-10q+1)}{24A^5}.
$$


The uniform remainder follows from separation of $e^{-it}+q$ from zero.

The retained sharp moment coefficients are


$$
\mathbb EQ=
\frac{d^2}{\alpha _0n}
+\left(\frac16-\alpha _0\right)
 \frac{d^3}{\alpha _0^2n^2}
+O(d^2/n^2+d^4/n^3),
$$




$$
\mathbb EQ_4=
\frac{2d^3}{\alpha _0^2n^2}
+O(d^2/n^2+d^4/n^3).
\tag{11}
$$


Their centered actual-weight corrections are $O(d/n)$ and $O(d^2/n^2)$, respectively. Also retain


$$
\langle X\rangle_j=O(d/n),\qquad
\langle C_3\rangle_j=O(d^2/n^2).
\tag{12}
$$



The exact derivative identity is


$$
(\log A_j^{\rm pr})'(q)
=\left\langle\sum_i h(\theta_i)\right\rangle_j.
$$


Equations (9)–(12), together with


$$
\left|\left\langle\sum_i\mathcal R_6(\theta_i)\right\rangle_j\right|
\le C\mathbb EQ_6=O(d^4/n^3),
$$


therefore give the improved expansion


$$
\boxed{
\begin{aligned}
(\log A_j)'(q)
={}&\frac dA+\frac{d^2}{n}\frac{c_2}{\alpha _0}\\
&+\frac{d^3}{n^2}
\frac{c_2(1/6-\alpha _0)+2c_4}{\alpha _0^2}
+O\!\left(\frac dn+\frac{d^4}{n^3}\right).
\end{aligned}}
\tag{13}
$$


Here $d^2/n^2$ and $d^3/n^3$ are absorbed by $d/n$. The passage from principal to full integrals adds only exponentially small errors: a fixed number of characteristic derivatives introduces a polynomial in $d$ into the retained outer-sector estimate.

This is the required improvement over the absolute fifth-moment remainder:


$$
\boxed{
\frac dn\,O\!\left(\frac dn+\frac{d^4}{n^3}\right)
=O(d^2/n^2+d^5/n^4)=o(1)
}
\tag{14}
$$


on (1).

## 4. Third derivative: signed linear trace and centered cumulants

Define


$$
H=\sum_i h(\theta_i),\qquad
J=-\sum_i h(\theta_i)^2,\qquad
K=2\sum_i h(\theta_i)^3.
$$


Exact differentiation of the characteristic product gives


$$
(\log A_j^{\rm pr})'''
=
\langle K\rangle_j+
3\operatorname{Cov}_j(H,J)+\operatorname{Cum}_{3,j}(H),
\tag{15}
$$


with algebraic complex covariance and cumulant.

### 4.1 Signed linear term in $K$

Instead of bounding the linear term absolutely, retain it:


$$
2h(t)^3=\frac2{A^3}+\frac{6i}{A^4}t+O(t^2).
$$


Hence (12) and $\mathbb EQ=O(d^2/n)$ give


$$
\boxed{
\langle K\rangle_j
=\frac{2d}{A^3}+O(d/n+d^2/n).
}
\tag{16}
$$



### 4.2 Covariance with the actual denominator

Set


$$
Y=H-\mathbb EH,\qquad Z=J-\mathbb EJ.
$$


Bounded one-particle derivatives and Brascamp–Lieb imply


$$
\mathbb E|Y|^2+\mathbb E|Z|^2=O(d/n).
$$


Covariance is invariant under these constant shifts, so


$$
\operatorname{Cov}_j(H,J)
=\langle YZ\rangle_j-\langle Y\rangle_j\langle Z\rangle_j.
$$


Using $|\mathcal W_j|\le C$, $|N_j|\ge1/2$, and Cauchy–Schwarz yields


$$
\boxed{\operatorname{Cov}_j(H,J)=O(d/n).}
\tag{17}
$$


This is a bound for the actual algebraic covariance, not a claim that it is a positive variance.

### 4.3 Third cumulant without an unproved moment transfer

A short Poincaré argument supplies the needed fourth moment. For a real centered component $Y_0$ of $Y$, its gradient satisfies
$\|\nabla Y_0\|^2\le Cd$. Applying the same variance inequality to $Y_0^2$,


$$
\begin{aligned}
\mathbb EY_0^4-(\mathbb EY_0^2)^2
&=\operatorname{Var}(Y_0^2)\\
&\le \frac Cn\mathbb E\|\nabla(Y_0^2)\|^2
\le C\frac dn\mathbb EY_0^2
=O((d/n)^2).
\end{aligned}
$$


Consequently


$$
\mathbb E|Y|^4=O((d/n)^2),\qquad
\mathbb E|Y|^3=O((d/n)^{3/2}).
\tag{18}
$$



The actual cumulant is exactly


$$
\operatorname{Cum}_{3,j}(H)
=\langle Y^3\rangle_j
-3\langle Y^2\rangle_j\langle Y\rangle_j
+2\langle Y\rangle_j^3.
$$


Each term is bounded using (3), (18), and the second-moment estimate. Thus


$$
\boxed{\operatorname{Cum}_{3,j}(H)=O((d/n)^{3/2}).}
\tag{19}
$$



Combining (15)–(19), and then including differentiated outer sectors, proves


$$
\boxed{
(\log A_j)'''(q)
=\frac{2d}{(1+q)^3}
+O\!\left(\frac dn+\frac{d^2}{n}+(d/n)^{3/2}\right).
}
\tag{20}
$$


For $U_\pm(\zeta)=\log(s_jA_j(\sigma\pm\zeta))$, the leading value acquires the chain sign $\pm$.

Its new error has exactly the required size:


$$
\frac{d^3}{n^3}
O\!\left(\frac dn+\frac{d^2}{n}+(d/n)^{3/2}\right)
=
O\!\left(\frac{d^4}{n^4}+\frac{d^5}{n^4}
+(d/n)^{9/2}\right)=o(1).
\tag{21}
$$



## 5. Stationary-value precision below four-fifths degree

The established second-derivative expansion remains


$$
(\log A_j)''(q)
=-\frac d{(1+q)^2}
+\frac{d^2}{n}\frac{2-q}{\alpha _0(1+q)^4}
+O(d/n+d^3/n^2).
\tag{22}
$$


Its remainder multiplied by $d^2/n^2$ is


$$
O(d^3/n^3+d^5/n^4).
$$



No previously computed coefficient changes: (13), (22), and (20) retain exactly the coefficients entering the controlled quadratic, cubic, and quartic stationary expansion. In particular, the established quartic equality remains


$$
C_{4,-}-C_{4,+}=0.
$$


The new work is the uniform control of its omitted terms, not another finite verification of this equality.

With $\epsilon=d/n$, the retained fixed-neighborhood bounds $U^{(k)}=O(d)$ make the next scalar Taylor remainder


$$
O(n\epsilon^5)=O(d^5/n^4).
$$


The errors in the first, second, and third insertion derivatives are multiplied, respectively, by $O(\epsilon)$, $O(\epsilon^2)$, and $O(\epsilon^3)$. Equations (14), (21), and (22) show that all are absorbed by


$$
O(d/n+d^5/n^4).
$$


The actual reciprocal-anchor estimate contributes $O(d/n)$. Therefore


$$
\boxed{
[nf_-(r_-)+U_-(r_-)]-[nf_+(r_+)+U_+(r_+)]
=-(2n+d)\log M+O(d/n+d^5/n^4).
}
\tag{23}
$$



At $d\asymp n^{4/5}$, the last displayed remainder is potentially order one. Equation (23) does not evaluate that critical-scale term.

## 6. Full forces, endpoint, normality, and metrics

The forces remain the original ones:


$$
P_j=\frac{n!}{2\pi}\int_{-\pi}^{\pi}
g(e^{is})^nA_j(\sigma+e^{is})\,ds,
$$




$$
F_j=2n!\int_{-\pi/4}^{\pi/4}
h(e^{is})^nA_j(\sigma-e^{is})\,ds,
$$


and


$$
E_j=\nu_{n,d}\!\left(
R_j\sum_{i=0}^d\sigma^i e_{d-i}(z^{-1})eE_i
\right).
\tag{24}
$$



Under the retained contour interface, the curvature-prefactor ratio is
$M^{-1}(1+O(d/n))$, the local scalar relative error is $O(n^{-1/5})$, and remote contributions are exponentially small for $d=o(n)$. This includes all signed particle outer sectors and both radial connectors of the open minus arc. The original scalar normalization ratio is $4\pi$. Thus (23) gives


$$
\frac{F_j}{P_j}
=4\pi M^{-2n-b}
\left[1+O\!\left(\frac bn+\frac{b^5}{n^4}+n^{-1/5}\right)\right],
\quad
\operatorname{sign}P_j=\operatorname{sign}F_j=s_j.
\tag{25}
$$



The exact actual-column equations are


$$
u_j=(-1)^nP_j/D,\qquad
v_j-Su_j=\delta_{j0}+(-1)^nE_j/D-F_j/D.
$$


Hence the whole coordinate error is


$$
\boxed{
c_j-S=
\frac{E_j}{P_j}+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac D{P_j}.
}
\tag{26}
$$


The retained complete-residual bounds are


$$
|E_j/P_j|\le\frac{e^{Cb}}{n!\sqrt n},\qquad
|D/P_0|\le\frac{C\sqrt n\,e^{Cb}}{n!B_0},
\qquad B_0=(n)_d\sigma^{-d}>1.
\tag{27}
$$


They remain $o(M^{-2n-b})$ on (1). Thus (25)–(27) give (2) for the **whole** error, including its sign and nonvanishing.

The normality range $b\le n/1000$ eventually contains (1), so $D>0$. Equation (25) gives $u_j\ne0$ for every actual coordinate.

For any positive diagonal actual-coordinate metric


$$
W=\operatorname{diag}(w_0,\ldots,w_b),\qquad w_j>0,
$$


retain the actual center


$$
c_W=\frac{u^TWv}{u^TWu}.
$$


The exact identity


$$
c_W-S
=\sum_j\frac{w_ju_j^2}{\sum_\ell w_\ell u_\ell^2}(c_j-S)
\tag{28}
$$


transfers (2) uniformly to $c_W$, even for arbitrarily varying positive weights. This does not cover general nondiagonal metrics.

## 7. Primitive multiplier, final gcd, and whole evaluated form

For a rational positive diagonal metric, let $d_B$ be the least positive integer clearing the actual two-column matrix, and let $\Omega$ be an integral positive diagonal scaling of that metric:


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


The actual reduced denominator is $q_B$, and the primitive multiplier is exactly $d_B^2/g_B$. On (1), with the same analytic interfaces,


$$
\boxed{
\begin{aligned}
q_BS-p_B
&=\frac{d_B^2}{g_B}
 \bigl[(u^T\Omega u)S-u^T\Omega v\bigr]\\
&=(-1)^n4\pi q_BM^{-2n-b}
\left[1+O\!\left(\frac bn+\frac{b^5}{n^4}+n^{-1/5}\right)\right]
\ne0.
\end{aligned}}
\tag{29}
$$


Neither $d_B$, the final gcd $g_B$, nor $q_B$ has been estimated by the new analytic argument.

## Closing ledger

### (1) New result and proof status

**Proved directly, uniformly for $2\le d=o(n)$:**


$$
\mathbb EQ_8=O(d^5/n^4),\qquad
\langle C_5\rangle_j=O(d^3/n^3),
$$


the improved first-derivative remainder $O(d/n+d^4/n^3)$, and the improved third-derivative remainder


$$
O(d/n+d^2/n+(d/n)^{3/2}).
$$


The covariance and cumulant bounds retain the actual insertion and actual complex denominator.

**Using the explicitly retained prior contour and complete-residual interfaces:** these estimates extend the whole $4\pi$ relative law to $3\le b=o(n^{4/5})$, with both parities, every actual coordinate, every positive diagonal actual-coordinate metric, normality, and eventual nonvanishing. No critical-$4/5$ theorem or all-sublinear symmetry is asserted.

### (2) Exact remaining bottleneck

At critical four-fifths degree, the fifth stationary coefficient and its complete error control remain unresolved.

For irrationality, a sufficient missing arithmetic statement is an infinite same-index sequence with the **actual reduced denominator after the final gcd** satisfying


$$
q_BM^{-2n-b}\longrightarrow0.
$$


Then (29) would supply nonzero primitive forms tending to zero and contradict rationality of $S$. No such denominator bound is proved here. Irrationality of $e+\pi$ remains unresolved.

### (3) Computation request

None. The new infinite-range remainder estimates are analytic; a finite calculation is not being used to establish them.
