> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Below three-quarters degree: signed cubic control closes the relative law

Put


$$
\sigma=\sqrt2,\qquad M=1+\sqrt2,\qquad \rho=M^{-1},\qquad
d=b-1,\qquad S=e+\pi.
$$



**The proposed improvement works.** The signed cubic trace remains controllable with the actual reconstruction insertion and the full complex-weight denominator. Using the exact reconstruction, sector, scalar-contour, and complete-residual interfaces supplied in the question, it gives


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
\boxed{
n\to\infty,\qquad 3\le b=o(n^{3/4}),\qquad 0\le j\le b.
}
\tag{2}
$$


Both parities are included. The metric is any positive diagonal metric in the **actual coordinates**, with arbitrary index-dependent positive weights.

More precisely, the relative error in (1) is


$$
O\!\left(\frac bn+\frac{b^4}{n^3}+n^{-1/5}\right).
\tag{3}
$$


Uniformity means, for example, uniformity over $3\le b\le\eta_n n^{3/4}$ for each $\eta_n\to0$. All first-column coordinates and whole errors are eventually nonzero, and the contact determinant is positive.

This does **not** settle the critical scale $b\asymp n^{3/4}$, nor the irrationality of $e+\pi$.

## 1. The actual insertion and denominator

Retain the original functional and reconstruction:


$$
A_j(q)=\nu_{n,d}\!\left(
R_j(z)\prod_{\ell=1}^d(z_\ell^{-1}+q)
\right),
$$




$$
R_j(z)=[t^j](t-1)(1+D_t)^{-n}
            \prod_{\ell=1}^d(z_\ell+t/\sigma).
$$


Let


$$
B_j=|K_{j,d}|\sigma^{-d}>0,\qquad S_j=s_jR_j/B_j.
$$


The exact gamma expansion gives, on every circle configuration,


$$
\|S_j-1\|_\infty\le(1+\sigma/n)^d-1=O(d/n)
\tag{4}
$$


whenever $d=o(n)$, uniformly in $j$.

At either real anchor $q=M,\rho$, use the positive principal measure


$$
d\mu_q\propto
|\Delta(e^{i\theta})|^2
\prod_{\ell=1}^d
g(\theta_\ell)^n e^{-\sigma\cos\theta_\ell}
|e^{-i\theta_\ell}+q|\,d\theta,
\quad
g(t)=1+\sigma\cos t,
$$


on $I^d$, $I=(-3\pi/4,3\pi/4)$. Define the full phase


$$
\Phi_q=\sum_{\ell=1}^d
\left[-\sigma\sin\theta_\ell+
\arg(e^{-i\theta_\ell}+q)\right],
$$


with the argument continuously anchored at zero, and write


$$
\mathcal W_j=S_je^{i\Phi_q},\qquad
N_j(q)=\mathbb E_q\mathcal W_j.
$$


Thus


$$
A_j^{\rm pr}(q)=s_jB_jZ_d(q)N_j(q).
\tag{5}
$$



The supplied reflection and concentration estimates give


$$
N_j(q)=1+O(d/n),\qquad
\mathbb E_q\Phi_q^2=O(d/n).
\tag{6}
$$


In particular, $|N_j(q)|\ge1/2$ eventually. Every weighted expectation below means


$$
\langle F\rangle_j=\frac{\mathbb E_q(\mathcal W_jF)}{N_j(q)};
\tag{7}
$$


the denominator is never replaced by one.

## 2. New signed cubic lemma

The needed estimates hold throughout $2\le d=o(n)$, not only on (2). Set


$$
Q=\sum_\ell\theta_\ell^2,\quad
Q_4=\sum_\ell\theta_\ell^4,\quad
X=\sum_\ell\theta_\ell,\quad
C_3=\sum_\ell\theta_\ell^3,\qquad
\alpha_0=\sigma/M.
$$



The endpoint-safe moment estimates in the same $q$-tilted measure are


$$
\mathbb E_qQ=\frac{d^2}{\alpha_0n}+O(d^3/n^2),\quad
\mathbb E_qQ_4=O(d^3/n^2),\quad
\operatorname{Var}_qQ=O(d^2/n^2),
\tag{8}
$$


and


$$
\mathbb E_qX=0,\qquad \mathbb E_qX^2=O(d/n).
\tag{9}
$$


These estimates use the endpoint-safe field $tg(t)/M$ for the sharp mean, rather than a Taylor expansion of the singular potential derivative at the endpoints.

Reflection preserves $\mu_q$ and reverses $C_3$, so


$$
\mathbb E_qC_3=0.
$$


On an ordered chamber, the Hessian lower bound is $cnI_d$. Since


$$
\|\nabla C_3\|^2=9Q_4,
$$


Brascamp–Lieb gives


$$
\boxed{\mathbb E_qC_3^2=\operatorname{Var}_qC_3
\le \frac Cn\mathbb E_qQ_4
=O(d^3/n^3).}
\tag{10}
$$


As for the other symmetric statistics, reflection can be implemented within a chamber by reversing the particle order after changing all signs.

Now retain both the phase and insertion:


$$
\begin{aligned}
|\mathbb E_q(\mathcal W_jC_3)|
&\le
|\mathbb E_q[C_3(e^{i\Phi_q}-1)]|
+\mathbb E_q[|S_j-1||C_3|]\\
&\le
\sqrt{\mathbb E_qC_3^2\,\mathbb E_q\Phi_q^2}
+C\frac dn\sqrt{\mathbb E_qC_3^2}\\
&=O\!\left(\frac{d^2}{n^2}
+\frac{d^{5/2}}{n^{5/2}}\right).
\end{aligned}
$$


Dividing by the actual denominator yields the new bound


$$
\boxed{
\langle C_3\rangle_j=O(d^2/n^2).
}
\tag{11}
$$


Here $d/n\to0$ absorbs the second term. The insertion need not be reflection-even: its entire symmetry defect was bounded by (4).

For later use, the same argument with $X$ gives


$$
\langle X\rangle_j=O(d/n).
\tag{12}
$$


Centering $Q$ before weighting gives


$$
\begin{aligned}
\langle Q\rangle_j-\mathbb E_qQ
&=\frac{\mathbb E_q[\mathcal W_j(Q-\mathbb E_qQ)]}{N_j(q)}
=O\!\left(\sqrt{\operatorname{Var}_qQ}\right),
\end{aligned}
$$


hence


$$
\boxed{
\langle Q\rangle_j
=\frac{d^2}{\alpha_0n}+O(d/n+d^3/n^2).
}
\tag{13}
$$


No error proportional to the large mean $d^2/n$ is introduced by normalizing.

## 3. Improved first and second logarithmic derivatives

### First derivative

At a fixed real anchor define


$$
H_q=\sum_\ell\frac1{e^{-i\theta_\ell}+q}.
$$


Differentiating the actual characteristic product gives exactly


$$
(\log A_j^{\rm pr})'(q)=\langle H_q\rangle_j.
\tag{14}
$$



The denominator in each summand is uniformly separated from zero on the whole principal interval. Taylor’s theorem through degree three therefore gives


$$
H_q=
\frac d{1+q}
+\frac{iX}{(1+q)^2}
+\frac{q-1}{2(1+q)^3}Q
+i\gamma(q)C_3+\mathcal R_q,
\qquad |\mathcal R_q|\le C Q_4,
\tag{15}
$$


where $\gamma(q)$ is a bounded real coefficient. Its value is unnecessary: its contribution is already $O(d^2/n^2)$ by (11).

Since $|\mathcal W_j|\le C$ and $|N_j(q)|\ge1/2$, (8), (11)–(15) imply


$$
\boxed{
a_q:=(\log A_j)'(q)
=\frac d{1+q}+\frac{d^2}{n}c_1(q)
+O\!\left(\frac dn+\frac{d^3}{n^2}\right),
\qquad
c_1(q)=\frac{q-1}{2\alpha_0(1+q)^3}.
}
\tag{16}
$$


The passage from principal to full integrals is justified by the supplied signed-sector bound: one derivative introduces at most a factor $Cd$, while the relative sector bound is exponentially small.

Thus the previously limiting absolute cubic remainder has been removed.

### Second derivative

Put


$$
J_q=-\sum_\ell(e^{-i\theta_\ell}+q)^{-2}.
$$


Exact differentiation, without differentiating any asymptotic remainder, gives


$$
(\log A_j^{\rm pr})''(q)
=\langle J_q\rangle_j+
\langle H_q^2\rangle_j-\langle H_q\rangle_j^2.
\tag{17}
$$


Taylor expansion through the linear term gives


$$
J_q=-\frac d{(1+q)^2}
-\frac{2iX}{(1+q)^3}+O(Q).
$$


Consequently,


$$
\langle J_q\rangle_j
=-\frac d{(1+q)^2}+O(d/n+d^2/n).
\tag{18}
$$



For completeness, let $m_H=\mathbb E_qH_q$ and $\widetilde H=H_q-m_H$. The gradients of the summands of $H_q$ are bounded, so Brascamp–Lieb on real and imaginary parts gives


$$
\mathbb E_q|\widetilde H|^2=O(d/n).
$$


The algebraic covariance in (17) is exactly


$$
\langle\widetilde H^2\rangle_j-\langle\widetilde H\rangle_j^2,
$$


whose modulus is $O(d/n)$, using the same bounds on $\mathcal W_j,N_j$. Full-sector derivatives through order two again contribute exponentially small errors. Therefore


$$
\boxed{
\beta_q:=(\log A_j)''(q)
=-\frac d{(1+q)^2}+O(d/n+d^2/n).
}
\tag{19}
$$



No derivative of $S_j$ occurs here: $S_j$ is independent of the characteristic parameter $q$.

## 4. Saddle precision below $n^{3/4}$

Use the supplied zero-free holomorphic logarithms $T_j=\log(s_jA_j)$, anchored to be real at the positive anchors. On fixed interior neighborhoods, their fixed-order derivatives are $O(d)$.

Set


$$
U_+(\zeta)=T_j(\sigma+\zeta),\qquad
U_-(\zeta)=T_j(\sigma-\zeta),
$$


and retain


$$
f_+=\log g,\quad f_-=\log h,\quad
\alpha_+=\sigma/M,\quad \alpha_-=\sigma M,\quad
f_\pm'''(1)=-3\alpha_\pm.
$$


For $a=U'(1)$, $\beta=U''(1)$, the real stationary value satisfies


$$
nf(r)+U(r)
=nf(1)+U(1)-\frac{a^2}{2n\alpha}
+\frac{\beta a^2}{2n^2\alpha^2}
-\frac{f'''(1)a^3}{6n^2\alpha^3}
+O(d^4/n^3).
\tag{20}
$$


Indeed $r-1=O(d/n)$; fourth-order base terms and third-order insertion terms are $O(d^4/n^3)$. Solving the stationary equation through its quadratic correction leaves the same error in the stationary value.

Inserting (16) into the quadratic term costs


$$
O\!\left(\frac{d^2}{n^2}+\frac{d^4}{n^3}\right).
\tag{21}
$$


Inserting (19) into the cubic-order terms costs $O(d^4/n^3)$. Corrections to $a$ inside those cubic-order terms have the same bound.

The quadratic leading terms agree. At cubic order, the pure saddle contribution to “minus minus plus” is


$$
-\frac{M+1}{2\sigma^5M^2}\frac{d^3}{n^2},
$$


whereas the cross term from the $c_1$-correction is


$$
\left(\frac{c_1(M)}{\sigma^2}
-\frac{c_1(\rho)}{\sigma^2M}\right)\frac{d^3}{n^2}
=\frac{M+1}{2\sigma^5M^2}\frac{d^3}{n^2}.
$$


They cancel exactly.

The exact reciprocal-anchor comparison remains


$$
U_-(1)-U_+(1)=-d\log M+O(d/n).
$$


Combining it with (20)–(21) gives


$$
\boxed{
[nf_-(r_-)+U_-(r_-)]
-[nf_+(r_+)+U_+(r_+)]
=-(2n+d)\log M
+O\!\left(\frac dn+\frac{d^4}{n^3}\right).
}
\tag{22}
$$



## 5. Full scalar integrals and whole errors

The original scalar forces are unchanged:


$$
P_j=\frac{n!}{2\pi}\int_{-\pi}^{\pi}
g(e^{is})^nA_j(\sigma+e^{is})\,ds,
$$




$$
F_j=2n!\int_{-\pi/4}^{\pi/4}
h(e^{is})^nA_j(\sigma-e^{is})\,ds.
$$


Their curvature-prefactor ratio is $M^{-1}(1+O(d/n))$. The supplied local scalar Taylor estimate contributes $O(n^{-1/5})$. Remote arcs are relatively $O(\sqrt n e^{-cn+Cd})$; both radial connectors of the minus arc remain included and exponentially negligible. These estimates use the full actual characteristic integral, including all signed particle outer sectors.

Thus


$$
\boxed{
\frac{F_j}{P_j}
=4\pi M^{-2n-b}
\left[1+O\!\left(\frac bn+\frac{b^4}{n^3}+n^{-1/5}\right)\right],
\qquad
\operatorname{sign}P_j=\operatorname{sign}F_j=s_j.
}
\tag{23}
$$



Retain the **complete** exponential force


$$
E_j=\nu_{n,d}\!\left(
R_j\sum_{i=0}^d\sigma^i e_{d-i}(z^{-1})eE_i
\right)
$$


and the exact endpoint. The actual identities are


$$
u_j=(-1)^nP_j/D,
$$




$$
v_j-Su_j=\delta_{j0}+(-1)^nE_j/D-F_j/D,
$$


so


$$
c_j-S=\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac D{P_j}.
\tag{24}
$$


The supplied whole-residual and endpoint estimates remain


$$
|E_j/P_j|\le\frac{e^{Cb}}{n!\sqrt n},\qquad
|D/P_0|\le\frac{C\sqrt n\,e^{Cb}}{n!B_0},
\quad B_0=(n)_d\sigma^{-d}>1.
\tag{25}
$$


They are factorially smaller than the main term throughout (2). Equations (23)–(25) prove the coordinate law (1), including its eventual sign and nonvanishing.

Normality applies because (2) eventually lies within $b\le n/1000$:


$$
D>0,\qquad u_j\ne0.
$$


For the actual columns $u,v$ and


$$
W=\operatorname{diag}(w_0,\ldots,w_b),\qquad w_j>0,
$$


the exact convex identity


$$
c_W-S=
\sum_j\frac{w_ju_j^2}{\sum_\ell w_\ell u_\ell^2}(c_j-S),
\qquad c_W=\frac{u^TWv}{u^TWu},
$$


transfers the uniform relative estimate and nonvanishing to the metric center. No assertion for general nondiagonal metrics is made.

## 6. Primitive multiplier, final gcd, and evaluated error

For a rational positive diagonal metric, let $d_B$ be the least positive integer clearing the **actual two-column matrix**, and let $\Omega$ be an integral positive diagonal scaling of that metric:


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
p_B=H_B/g_B,\qquad q_B=A_B/g_B>0.
$$


Then $q_B$ is the actual reduced denominator, and the primitive multiplier is exactly $d_B^2/g_B$. The **whole evaluated real error** is


$$
\boxed{
\begin{aligned}
q_BS-p_B
&=\frac{d_B^2}{g_B}
\left[(u^T\Omega u)S-u^T\Omega v\right]\\
&=(-1)^n4\pi q_BM^{-2n-b}
\left[1+O\!\left(\frac bn+\frac{b^4}{n^3}+n^{-1/5}\right)\right]
\ne0.
\end{aligned}}
\tag{26}
$$


No estimate of $d_B$, $g_B$, or $q_B$ follows from the analytic cancellation.

## Closing ledger

### (1) New result and proof status

**Proved new bounds:** the signed cubic estimate (11), the improved actual first logarithmic derivative (16), and the improved second logarithmic derivative (19), uniformly for $d=o(n)$. They retain the full insertion, phase denominator, and differentiated outer-sector contributions.

**Proved using the supplied exact and uniform analytic interfaces:** the whole relative law (1) on $3\le b=o(n^{3/4})$, with both parities, actual-coordinate positive diagonal metrics, normality, and eventual nonvanishing.

### (2) Exact remaining bottleneck

At $b\asymp n^{3/4}$, the uncomputed $O(d^4/n^3)$ saddle-value difference can be order one. Nothing here evaluates its coefficient or proves its cancellation.

For irrationality, the remaining sufficient arithmetic condition is an infinite same-index sequence satisfying


$$
q_BM^{-2n-b}\longrightarrow0
$$


for the **actual primitive denominator after the final gcd**. Together with (26), this would contradict rationality. That condition is not proved here; irrationality or rationality of $e+\pi$ remains unresolved.

### (3) Computation request

None. The new estimates and the subcritical three-quarters conclusion are derived analytically, not inferred from finite computations.
