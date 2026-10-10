> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Critical two-thirds degree: the cubic terms cancel for the actual characteristic integral

Put


$$
\sigma=\sqrt2,\qquad M=1+\sqrt2,\qquad \rho=M^{-1},\qquad d=b-1.
$$


Fix $0<\kappa _0<\kappa _1<\infty$. The index domain in this answer is


$$
n\longrightarrow\infty,\qquad
\kappa _0n^{2/3}\le b\le\kappa _1n^{2/3},
\qquad 0\le j\le b,
\tag{1}
$$


with integer $n,b$, on both parities.

**The candidate cancellation is correct.** Using the supplied exact reconstruction, zero-free, full-contour, and whole-residual interfaces, the resulting uniform law is


$$
\boxed{
c_j-(e+\pi)=(-1)^{n+1}4\pi M^{-2n-b}(1+o(1)).
}
\tag{2}
$$


The same law holds uniformly for every positive diagonal metric in the actual coordinates. In particular, all these whole errors, all first-column coordinates, and the contact determinant are nonzero eventually.

The new estimates below concern the actual differentiated characteristic integral, not a positive surrogate. They avoid absolute comparisons involving $\exp(Cd^2/n)$.

## 1. Same positive ensemble and actual denominator

Retain the exact objects


$$
A_j(q)=\nu_{n,d}\!\left(R_j(z)\prod_{\ell=1}^d(z_\ell^{-1}+q)\right),
\qquad
R_j(z)=[t^j](t-1)(1+D_t)^{-n}
             \prod_{\ell=1}^d(z_\ell+t/\sigma).
$$


Write


$$
B_j=|K_{j,d}|\sigma^{-d}>0,\qquad S_j=s_jR_j/B_j.
$$


The supplied gamma reconstruction gives


$$
\sup_{\lvert z_\ell\rvert\le1}|S_j-1|=O(d/n).
\tag{3}
$$



For $q=M,\rho$, use exactly the positive $q$-tilted principal ensemble


$$
d\mu_q\ \propto\
|\Delta(e^{i\theta})|^2
\prod_{\ell=1}^d
g(\theta_\ell)^n e^{-\sigma\cos\theta_\ell}
|e^{-i\theta_\ell}+q|\,d\theta,
\quad
g(t)=1+\sigma\cos t,
$$


on $I^d$, $I=(-3\pi/4,3\pi/4)$. Let


$$
\Phi_q=\sum_\ell\left[-\sigma\sin\theta_\ell+
                 \arg(e^{-i\theta_\ell}+q)\right],
\qquad W_j=S_je^{i\Phi_q}.
$$


Thus


$$
A_j^{\rm pr}(q)=s_jB_jZ_d(q)N_j(q),
\qquad N_j(q)=\mathbb E_qW_j.
\tag{4}
$$


Reflection, the phase variance estimate, and (3) give


$$
N_j(q)=1+O(d/n).
\tag{5}
$$


In particular, this **actual phase denominator** stays bounded away from zero.

All estimates below have constants independent of $j$ and of the indices in (1).

## 2. Endpoint-safe moments in the same $q$-tilted measure

Set


$$
Q=\sum_\ell\theta_\ell^2,\qquad
X=\sum_\ell\theta_\ell,\qquad
Q_4=\sum_\ell\theta_\ell^4,\qquad
H_3=\sum_\ell|\theta_\ell|^3,
\qquad \alpha_0=\sigma/M.
$$



The characteristic contribution to the real potential,


$$
-\log|e^{-it}+q|,
$$


is even and has bounded derivatives at these anchors. Consequently the endpoint-safe virial argument applies without changing its leading coefficient:


$$
\begin{split}
\mathbb E_qQ&=\frac{d^2}{\alpha_0 n}
                   +O(d^3/n^2),\\
\mathbb E_qQ_4&=O(d^3/n^2),\\
\mathbb E_qH_3&=O(d^{5/2}/n^{3/2}),\\
\operatorname{Var}_qQ&=O(d^2/n^2).
\end{split}
\tag{6}
$$



For clarity, the sharp first line uses the field


$$
v(t)=tg(t)/M,
$$


not an endpoint-invalid global Taylor expansion of $tV_q'(t)$. Multiplying the logarithmic derivative of $g^n$ by this field cancels its endpoint pole:


$$
v(t)V_q'(t)=\alpha_0nt^2+O(nt^4+t^2).
$$


The pair term is $2+O(x^2+y^2)$, uniformly on the full principal interval. The fields $t,t^3$ first give the upper bounds for $Q,Q_4$; substitution in the safe identity gives the sharp mean. Brascamp–Lieb gives the last line because $\|\nabla Q\|^2=4Q$. Endpoint and collision fluxes vanish with the original density.

Also,


$$
\mathbb E_qX=0,\qquad
\mathbb E_qX^2+\mathbb E_q\Phi_q^2=O(d/n).
\tag{7}
$$



A useful consequence, retaining the denominator exactly, is


$$
\frac{\mathbb E_q(W_jQ)}{N_j(q)}
=\mathbb E_qQ+O(d/n).
\tag{8}
$$


Indeed, subtract $(\mathbb E_qQ)N_j(q)$ in the numerator and use


$$
|\mathbb E_q[W_j(Q-\mathbb E_qQ)]|
\le C\sqrt{\operatorname{Var}_qQ}.
$$


There is no factor proportional to the potentially large mean $d^2/n$.

## 3. First actual logarithmic derivative, including its quadratic correction

Define


$$
H_q=\sum_\ell\frac1{e^{-i\theta_\ell}+q}.
$$


Differentiating the actual characteristic product gives


$$
\frac{(A_j^{\rm pr})'(q)}{A_j^{\rm pr}(q)}
=\frac{\mathbb E_q(W_jH_q)}{N_j(q)}.
\tag{9}
$$



The full-interval Taylor expansion is


$$
\frac1{e^{-it}+q}
=\frac1{1+q}+\frac{it}{(1+q)^2}
+\frac{q-1}{2(1+q)^3}t^2+O(|t|^3).
\tag{10}
$$


Its remainder is uniform because the denominator is separated from zero throughout the interval.

Reflection and (7) show


$$
\left|\mathbb E_q(W_jX)\right|
\le
\left|\mathbb E_q[X(e^{i\Phi_q}-1)]\right|
+\mathbb E_q[|S_j-1||X|]
=O(d/n).
\tag{11}
$$


Combining (6), (8)–(11) yields


$$
\boxed{
\frac{A_j'(q)}{A_j(q)}
=\frac d{1+q}+\frac{d^2}{n}c_1(q)+O(R_{n,d}),
\qquad
c_1(q)=\frac{q-1}{2\alpha_0(1+q)^3},
}
\tag{12}
$$


where


$$
R_{n,d}=\frac dn+\frac{d^3}{n^2}
                    +\frac{d^{5/2}}{n^{3/2}}.
\tag{13}
$$


Passing from principal to full integrals in (12) adds only an exponentially small error: the differentiated outer-sector integrand is bounded by $Cd$ times its original absolute bound.

Most importantly, on (1),


$$
\boxed{\frac dnR_{n,d}=o(1).}
\tag{14}
$$


The largest displayed contribution here is $O(n^{-1/6})$. This is the precision needed in the quadratic saddle term.

## 4. Second actual logarithmic derivative

The required leading value can be proved directly, without differentiating an asymptotic remainder.

Put


$$
J_q=-\sum_\ell\frac1{(e^{-i\theta_\ell}+q)^2}.
$$


With $\langle F\rangle_W=\mathbb E_q(W_jF)/N_j(q)$, exact differentiation gives


$$
(\log A_j^{\rm pr})''(q)
=\langle J_q\rangle_W+
 \langle H_q^2\rangle_W-\langle H_q\rangle_W^2.
\tag{15}
$$



First,


$$
J_q=-\frac d{(1+q)^2}+O\!\left(\sum_\ell|\theta_\ell|\right).
$$


Since $\mathbb E_q\sum|\theta_\ell|\le\sqrt{d\,\mathbb E_qQ}$,


$$
\langle J_q\rangle_W
=-\frac d{(1+q)^2}+O(d^{3/2}/\sqrt n).
\tag{16}
$$



For the covariance term, the gradients of the summands of $H_q$ are uniformly bounded. Applying Brascamp–Lieb separately to real and imaginary parts gives


$$
\mathbb E_q|H_q-\mathbb E_qH_q|^2=O(d/n).
$$


Centering the algebraic covariance in (15) at $\mathbb E_qH_q$, and using $|W_j|\le C$, $|N_j(q)|\ge c$, therefore gives


$$
\left|\langle H_q^2\rangle_W-\langle H_q\rangle_W^2\right|
=O(d/n).
\tag{17}
$$


The full-sector derivatives through order two contribute exponentially small errors. Thus


$$
\boxed{
(\log A_j)''(q)
=-\frac d{(1+q)^2}
+O(d^{3/2}/\sqrt n+d/n)
=-\frac d{(1+q)^2}+o(d).
}
\tag{18}
$$



This closes the second-derivative obligation for the actual integral.

## 5. Cubic saddle calculation and signs

Use the anchored logarithms $T_j(q)$ from the supplied zero-free interface, and set


$$
U_+(\zeta)=T_j(\sigma+\zeta),\qquad
U_-(\zeta)=T_j(\sigma-\zeta).
$$


For $f_+=\log g$, $f_-=\log h$, retain


$$
\alpha_+=\sigma/M,\qquad \alpha_-=\sigma M,
\qquad f_\pm'''(1)=-3\alpha_\pm.
$$


Write $a_\pm=U_\pm'(1)$, $\beta_\pm=U_\pm''(1)$. Equations (12) and (18) give


$$
\begin{split}
a_+&=\frac d{1+M}+\frac{d^2}{n}c_1(M)+O(R_{n,d}),\\
a_-&=-\frac d{1+\rho}-\frac{d^2}{n}c_1(\rho)+O(R_{n,d}),\\
\beta_+&=-\frac d{(1+M)^2}+o(d),\\
\beta_-&=-\frac d{(1+\rho)^2}+o(d).
\end{split}
\tag{19}
$$


The second chain-rule sign is positive, explaining the negative leading value of both $\beta_\pm$.

The supplied fixed-neighborhood holomorphic bounds $U^{(k)}=O(d)$ justify the cubic stationary-value expansion


$$
nf(r)+U(r)
=nf(1)+U(1)-\frac{a^2}{2n\alpha}
+\frac{\beta a^2}{2n^2\alpha^2}
-\frac{f'''(1)a^3}{6n^2\alpha^3}
+O(d^4/n^3).
\tag{20}
$$


For example, inserting $r-1=-a/(n\alpha)+O(d^2/n^2)$ into the cubic Taylor polynomial yields (20); the error caused by the remaining displacement is $O(d^4/n^3)$.

On (1), this remainder is $o(1)$. Replacing $\beta_\pm$ by their leading values costs $o(d^3/n^2)=o(1)$, and (14) controls the error in $a_\pm$.

Here is an explicit check of the two order-one coefficients. Since


$$
1+M=\sigma M,\qquad 1+\rho=\sigma,
$$


the pure cubic contribution, **minus saddle minus plus saddle**, is


$$
-\frac{M+1}{2\sigma^5M^2}\frac{d^3}{n^2}
=-\frac1{\sigma^6M}\frac{d^3}{n^2}.
\tag{21}
$$


Also


$$
c_1(M)=\frac1{2\sigma^3M^2},\qquad
c_1(\rho)=-\frac1{2\sigma^3}.
$$


The cross contribution from $-a_\pm^2/(2n\alpha_\pm)$ is consequently


$$
\left(\frac{c_1(M)}{\sigma^2}
-\frac{c_1(\rho)}{\sigma^2M}\right)\frac{d^3}{n^2}
=
\frac{M+1}{2\sigma^5M^2}\frac{d^3}{n^2}
=
\frac1{2\sigma^4M}\frac{d^3}{n^2}.
\tag{22}
$$


Because $\sigma^2=2$, (21) and (22) cancel exactly.

The leading quadratic corrections already agree. The established actual reciprocal-anchor estimate supplies


$$
U_-(1)-U_+(1)=-d\log M+O(d/n).
$$


Therefore the full saddle-value difference is


$$
\boxed{
[nf_-(r_-)+U_-(r_-)]
-[nf_+(r_+)+U_+(r_+)]
=-(2n+d)\log M+o(1),
}
\tag{23}
$$


uniformly on (1).

## 6. Full scalar forces, connectors, and whole errors

The original scalar normalizations are unchanged:


$$
P_j=\frac{n!}{2\pi}\int_{-\pi}^{\pi}
g(e^{is})^nA_j(\sigma+e^{is})\,ds,
$$




$$
F_j=2n!\int_{-\pi/4}^{\pi/4}
h(e^{is})^nA_j(\sigma-e^{is})\,ds.
$$


Their angular curvature ratio tends uniformly to $M^{-2}$. The scalar prefactor ratio is therefore $4\pi M^{-1}(1+o(1))$.

The supplied remote-contour estimates remain exponentially small on (1), since $d=o(n)$. They retain the full actual characteristic integral and all signed particle outer sectors. Both radial connectors of the open minus arc remain present and exponentially negligible. Thus (23) proves


$$
\boxed{
F_j/P_j=4\pi M^{-2n-b}(1+o(1)),
\qquad \operatorname{sign}P_j=\operatorname{sign}F_j=s_j.
}
\tag{24}
$$



The complete exponential force is still


$$
E_j=\nu_{n,d}\!\left(
R_j\sum_{i=0}^d\sigma^i e_{d-i}(z^{-1})eE_i
\right).
$$


Using the supplied whole-residual bound, not a selected term of that force,


$$
|E_j/P_j|\le\frac{e^{Cb}}{n!\sqrt n},
\qquad
|D/P_0|\le\frac{C\sqrt n\,e^{Cb}}{n!B_0},
\quad B_0=(n)_d\sigma^{-d}>1.
\tag{25}
$$


Both are $o(M^{-2n-b})$. The endpoint is exactly zero for $j\ne0$.

Hence the exact identity


$$
c_j-(e+\pi)
=\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac D{P_j}
\tag{26}
$$


proves (2), including its whole-error sign and nonvanishing.

The supplied normality theorem applies eventually on (1), giving


$$
D>0,\qquad u_j=(-1)^nP_j/D\ne0.
$$


For the actual columns $u,v$ and any


$$
W=\operatorname{diag}(w_0,\dots,w_b),\qquad w_j>0,
$$


the exact convex identity


$$
\frac{u^TWv}{u^TWu}-(e+\pi)
=\sum_j\frac{w_ju_j^2}{\sum_\ell w_\ell u_\ell^2}
             (c_j-(e+\pi))
$$


transfers the uniform law and nonvanishing to the metric center. This includes arbitrarily varying positive weights, but not general nondiagonal metrics.

## 7. Primitive multiplier, final gcd, and evaluated real form

For a rational positive diagonal metric, let $d_B$ be the least positive integer clearing the actual two-column matrix, and clear the metric to an integral positive diagonal matrix $\Omega$:


$$
N_B=d_B[u,v].
$$


Define


$$
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_B=H_B/g_B,\qquad q_B=A_B/g_B>0.
$$


The actual primitive multiplier is $d_B^2/g_B$. The whole evaluated form is


$$
\boxed{
\begin{aligned}
q_B(e+\pi)-p_B
&=\frac{d_B^2}{g_B}
 \left[(u^T\Omega u)(e+\pi)-u^T\Omega v\right]\\
&=(-1)^n4\pi q_BM^{-2n-b}(1+o(1))\ne0.
\end{aligned}}
\tag{27}
$$


No estimate for the final gcd or the actual primitive denominator is inferred from the analytic cancellation.

## Closing ledger

### (1) New result and proof status

**Proved using the supplied exact and uniform analytic interfaces:** the critical two-thirds relative law (2), uniformly on (1), for every actual coordinate and positive diagonal actual-coordinate metric, with full nonvanishing.

The new derivative estimates are (12)–(14) and (18). They use the same $q$-tilted ensemble, endpoint-safe virials, $\operatorname{Var}Q$, reflection, and the actual phase denominator. They verify both the coefficient and sign of the cubic cancellation.

No extension to $b=o(n^{3/4})$ is asserted.

### (2) Exact remaining bottleneck

Irrationality of $e+\pi$ remains unresolved. For this route, a sufficient missing arithmetic statement is an infinite same-index sequence on which the **actual primitive denominator after the final gcd** satisfies


$$
q_BM^{-2n-b}\longrightarrow0.
$$


Together with (27), that would give nonzero integer linear forms tending to zero and contradict rationality. The present analytic theorem does not establish that condition.

### (3) Computation request

None. The coefficient identities and uniform estimates above are symbolic arguments, not finite numerical evidence.
