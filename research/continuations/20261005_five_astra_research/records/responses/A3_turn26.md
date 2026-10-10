> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3 — exact nonlinear reconstruction and the remaining centered-comparison obstruction

Put


$$
\sigma=\sqrt2,\qquad M=1+\sqrt2,\qquad \rho=M^{-1},
\qquad d=b-1,\qquad c=d/n.
$$


The target domain is


$$
d\longrightarrow\infty,\qquad d=o(n),\qquad 0\le j\le b,
$$


with integer indices and both parities of $n$.

**Status.** I do not establish or disprove the proposed uniform correction


$$
\log\frac{c_j-S}{c_b-S}
=-\frac{s_j}{n^2}+o(d/n^2).
\tag{1}
$$


I establish a uniform derivative bound for the **complete nonlinear gamma insertion**, give its exact quadratic term, and identify the centered, phase-sensitive comparison still needed. In particular, an absolute $O(c^2)$ insertion error is not the appropriate obstruction: its derivatives admit a substantially better bound. The transfer through the actual complex expectations and scalar integrals nevertheless remains to be proved at the requested scale.

The all-sublinear whole relative law is reused **conditionally at the status requested in the assignment**. A4turn27 validates UB with image coercivity; it expressly does not audit the complete scalar closure. No denominator or irrationality conclusion is inferred.

## 1. Source scope and notation

The supplied archive gate and primary-search records precede this target. I have no additional archive or browsing access in this response and therefore claim no new searches. The fixed-$b$ spread, the $b=3$ second coefficient, and the proportional leading-equivalence argument are relevant established inputs at their stated scopes:

* The fixed-$b$ remainder $O_b(n^{-3})$ supplies no growing-$b$ uniformity.
* Proportional leading equivalence supplies an $o(1)$, not an $o(d/n^2)$, comparison.
* The audited UB estimate supplies a common characteristic derivative approximation with error $O(1)$; subtracting two such estimates does not give the needed coordinate difference.

To avoid the sources’ overloaded notation, write $\varepsilon_j$ for reconstruction signs and retain


$$
s_0=d,\qquad s_j=b-j\quad(1\le j\le b)
\tag{2}
$$


for the nonnegative spread indices.

The finite matrices remain $H_b,T$ on indices $0,\ldots,d$, with reconstruction $K$ having rows $0,\ldots,b$ and columns $0,\ldots,d$. No infinite-matrix replacement is made.

## 2. Exact full gamma reconstruction

Retain


$$
R_j(z)=[t^j](t-1)(1+D_t)^{-n}
                    \prod_{\ell=1}^d(z_\ell+t/\sigma),
$$




$$
B_j=|K_{j,d}|\sigma^{-d},\qquad
\mathcal S_j(z)=\varepsilon_jR_j(z)/B_j.
$$


Thus $\mathcal S_b=1$. The exact gamma identity is


$$
R_j(z)=\frac{\sigma^{-d}}{\Gamma(n)}
\int_0^\infty u^{n-1}e^{-u}
\left[e_{d-j+1}(\sigma z-u)-e_{d-j}(\sigma z-u)\right]\,du,
\tag{3}
$$


where out-of-range elementary polynomials are zero.

Define


$$
U_k(z)=
\mathbb E_{U\sim\Gamma(n+k,1)}
\mathbb E_{\substack{I\subseteq\{1,\ldots,d\}\\|I|=k}}
\prod_{\ell\in I}(1-\sigma z_\ell/U).
$$


Then


$$
\mathcal S_0=U_d,\qquad \mathcal S_b=U_0=1.
$$


For $1\le j\le d$, put $k=d-j$. Exactly,


$$
\mathcal S_j=\omega_jU_{k+1}+(1-\omega_j)U_k,
\tag{4}
$$


where


$$
\omega_j=
\frac{\binom d{k+1}(n)_{k+1}}
{\binom d{k+1}(n)_{k+1}+\binom dk(n)_k}.
\tag{5}
$$


Here $(n)_k=\Gamma(n+k)/\Gamma(n)$.

These are positive reference weights, not weights chosen asymptotically. All $e_\ell$ terms are retained.

Expanding the finite product gives


$$
U_k(z)=
\sum_{\ell=0}^k(-\sigma)^\ell
\frac{(k)_{\underline\ell}}{(d)_{\underline\ell}}
\frac{\Gamma(n+k-\ell)}{\Gamma(n+k)}e_\ell(z).
\tag{6}
$$


There are no convergence or interchange issues: this is a finite polynomial identity.

## 3. New lemma: the nonlinear insertion has small coordinate derivatives

Write the exact polynomial as


$$
\mathcal S_j(z)=1-a_je_1(z)+V_j(z),
\tag{7}
$$


where $V_j$ contains every degree at least two. Equations (4)–(6) give


$$
a_j=\frac{\sigma}{d}\,
\mathbb E_j\frac{k}{n+k-1},
\tag{8}
$$


with $\mathbb E_j$ denoting the one- or two-point degree mixture just defined. In particular,


$$
a_j=\sigma\frac{|K_{j,d-1}|}{|K_{j,d}|}.
$$



### Lemma

For $d\ge2$, $d/n$ sufficiently small, and $|z_\ell|\le1$, the logarithm anchored by $\log\mathcal S_j(0)=0$ exists throughout the polydisk. Uniformly in $j$ and particle index $i$,


$$
\log\mathcal S_j(z)=-a_je_1(z)+H_j(z),
\tag{9}
$$


where


$$
|H_j(z)|\le C\frac{d^2}{n^2},
\qquad
|\partial_{z_i}H_j(z)|\le C\frac d{n^2}.
\tag{10}
$$



### Proof

In each degree-$k$ component, the sum of absolute degree-$\ell$ coefficients on the unit polydisk is at most


$$
\binom{k}{\ell}(\sigma/n)^\ell,
$$


because every denominator in the gamma ratio is at least $n$. Positive mixtures preserve this bound with $k\le d$. Consequently


$$
|\mathcal S_j-1|\le e^{\sigma d/n}-1,\qquad
|V_j|\le C(d/n)^2.
\tag{11}
$$


For sufficiently small $d/n$, $|\mathcal S_j-1|<1/2$, establishing the asserted logarithm.

Symmetry gives the corresponding derivative coefficient sum: differentiation in one specified variable multiplies the degree-$\ell$ coefficient sum by $\ell/d$. Hence


$$
|\partial_{z_i}V_j|
\le\frac1d\sum_{\ell\ge2}\ell
             \binom d\ell(\sigma/n)^\ell
\le C\frac d{n^2}.
\tag{12}
$$


Also $a_j\le \sigma/n$. From (9),


$$
\partial_{z_i}H_j
=\frac{-a_j+\partial_{z_i}V_j}{\mathcal S_j}+a_j
=\frac{\partial_{z_i}V_j+a_j(\mathcal S_j-1)}
       {\mathcal S_j}.
$$


Equations (11)–(12) prove the derivative estimate. The value estimate follows from the convergent logarithm expansion. ∎

This lemma is uniform over **all actual coordinates**. It is not a top-column truncation.

### A rigorous positive-ensemble consequence

On the real principal chamber, the characteristic-modulus tilted measure has Hessian at least $C^{-1}nI$. For a linear statistic


$$
F(\theta)=\sum_i f(\theta_i),\qquad \|f'\|_\infty\le C,
$$


Brascamp–Lieb and Cauchy–Schwarz give


$$
\left|\operatorname{Cov}_q
       \bigl(H_j(e^{i\theta}),F(\theta)\bigr)\right|
\le C\frac{d^2}{n^3}
=o(d/n^2).
\tag{13}
$$


Indeed, the squared gradient bounds are $Cd^3/n^4$ and $Cd$, respectively, and the variance inequality contributes $C/n$.

Equation (13) concerns the positive measure. It is **not yet** the required covariance under the normalized oscillatory functional.

## 4. The first nonlinear insertion term is explicit

Define


$$
v_j=\frac{\sigma^2}{d(d-1)}
\mathbb E_j
\frac{k(k-1)}{(n+k-1)(n+k-2)}.
\tag{14}
$$


The exact quadratic Taylor term of the logarithm is


$$
\boxed{
H_j^{[2]}(z)
=v_je_2(z)-\frac{a_j^2}{2}e_1(z)^2.
}
\tag{15}
$$


Equivalently,


$$
H_j^{[2]}(z)
=\frac{v_j-a_j^2}{2}e_1(z)^2
-\frac{v_j}{2}\sum_i z_i^2.
\tag{16}
$$


The remaining value error is uniformly $O((d/n)^3)$.

Thus the first nonlinear correction contains both a collective-square term and a one-particle quadratic statistic. Keeping only the $e_1$ column misses (15). Conversely, its absolute size does not establish an extra term in the **coordinate-error ratio**: that requires its centered response to the two actual phases and the scalar integration.

For completeness, the exact linear coefficient satisfies


$$
a_j=\frac{\sigma s_j}{dn}
       +O\!\left(\frac{s_j}{n^2}\right)
\tag{17}
$$


uniformly in $j$, with $a_b=0$. For middle coordinates, this follows from


$$
1-\omega_j
=\frac{k+1}{(d-k)(n+k)+k+1},
$$


so the mixture mean differs from $k+1=s_j$ by at most $s_j/n$. The endpoint $j=0$ follows directly from (8).

## 5. Precise obstruction to completing the target

Let


$$
Q_j(q)=\frac{B_bA_j(q)}{\varepsilon_jB_jA_b(q)}.
\tag{18}
$$


On a positive real anchor neighborhood, its principal-sector representation is


$$
Q_j(q)=
\frac{\mathbb E_q\!\left[\mathcal S_j e^{i\Phi_q}\right]}
     {\mathbb E_q e^{i\Phi_q}},
\tag{19}
$$


up to the retained exponentially small signed outer sectors. The denominator in (19) must remain present.

At the reciprocal anchors, the positive measures agree exactly. Their phases do not:


$$
\Phi_q=\eta_qX+\text{higher odd terms},
\qquad
X=\sum_i\theta_i,\qquad
\eta_q=-\sigma-\frac1{1+q},
$$


and


$$
\eta_\rho-\eta_M=-\rho.
\tag{20}
$$


Thus the suggested first contribution is


$$
-a_j\rho\,\operatorname{Var}(X).
\tag{21}
$$


If


$$
\operatorname{Var}(X)=\frac{d}{n\alpha}(1+o(1)),
\qquad \alpha=\sigma/M,
\tag{22}
$$


then (17), $\sigma\rho/\alpha=1$, and (21) yield the proposed coefficient.

But neither UB nor an upper variance bound proves the complete statement. The missing comparison must simultaneously control:

1. the normalized oscillatory quotient in (19), rather than separate numerator estimates;
2. higher odd phase terms;
3. nonlinear insertion terms (15) and their higher-degree remainder;
4. the coordinate-dependent insertion through the **common highest-coordinate scalar contours**, including their shifted stationary points and Gaussian averages.

In particular, scalar $1+o(1)$ errors cannot be divided to obtain (1). Even a separate $O(n^{-1})$ error is too large when $d=o(n)$, since $d/n^2=o(n^{-1})$.

There is a further scale warning: a bare fixed-wall error $e^{-\gamma d}$ need not be $o(d/n^2)$ on an arbitrary sublinear sequence. At this precision, wall and localization errors must carry the relevant small insertion/observable factors, or a separate slow-$d$ argument must supply a quantitative join.

### Concrete follow-on lemma

A sufficient next lemma is the following **centered scalar comparison**, stated using the exact forces:


$$
\boxed{
\log\!\left[
\frac{F_j/F_b}{P_j/P_b}
\right]
=-a_j\rho\,\frac d{n\alpha}+o(d/n^2)
}
\tag{CSC}
$$


uniformly for $d\to\infty$, $d=o(n)$, $0\le j\le b$.

A proof should establish (22) by sum-direction integration by parts, then use (10) in centered phase interpolations and on the common scalar contours. Equation (13) supplies one of the needed estimates, but does not by itself prove CSC.

**No growing-$d$ range for (1) is claimed here.** The fixed-$b$ result remains valid at its original scope. The explicit first nonlinear insertion term is (15); an evaluated first extra term in the actual center spread remains unknown.

## 6. Whole forces and exact convex-average consequence

Retain, without deletion,


$$
P_j=\frac{n!}{2\pi}\int_{-\pi}^{\pi}
g(e^{it})^nA_j(\sigma+e^{it})\,dt,
$$




$$
F_j=2n!\int_{-\pi/4}^{\pi/4}
h(e^{it})^nA_j(\sigma-e^{it})\,dt,
$$


including all actual particle phases, signed sectors, and both minus-contour connectors. Also retain


$$
E_j=\nu_{n,d}\!\left(
R_j\sum_{i=0}^d\sigma^ie_{d-i}(z^{-1})eE_i\right),
$$




$$
eE_i=-[z^{n+i}](1-z+z^2/2)^n
                    \int_0^1s^ne^{1-s+sz}\,ds.
$$


The whole coordinate error is exactly


$$
c_j-S=\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac D{P_j}.
\tag{23}
$$


The retained factorial residual bounds make the first and third terms negligible even relative to the leading error times $d/n^2$. Thus CSC would imply (1); these residuals are not its bottleneck.

For any positive diagonal metric in the original coordinates,


$$
\alpha_j=\frac{W_{jj}u_j^2}{\sum_\ell W_{\ell\ell}u_\ell^2},
\qquad
c_W-S=\sum_j\alpha_j(c_j-S)
\tag{24}
$$


holds exactly.

If (1) is proved uniformly, its precise consequence is


$$
\boxed{
\log\frac{c_W-S}{c_b-S}
=-\frac{\bar s_W}{n^2}+o(d/n^2),
\qquad
\bar s_W=\sum_j\alpha_js_j\in[0,d].
}
\tag{25}
$$


The remainder is independent of weight ratios. This follows by expanding the exponential in (1), averaging, and taking the logarithm; the quadratic remainder $O(d^2/n^4)$ is $o(d/n^2)$.

Without CSC, only the conditional whole leading equivalence, not (25), is available.

## 7. Primitive arithmetic and closing ledger

For rational positive diagonal weights, retain the least actual clearer $d_B$, an integral positive diagonal scaling $\Omega$, and


$$
N_B=d_B[u,v],\quad
A_B=N_{B,1}^{T}\Omega N_{B,1},\quad
H_B=N_{B,1}^{T}\Omega N_{B,2}.
$$


Then


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_B=A_B/g_B,\qquad p_B=H_B/g_B,
$$


and the primitive multiplier is exactly $d_B^2/g_B$. The whole evaluated error is


$$
q_BS-p_B
=\frac{d_B^2}{g_B}
\bigl[(u^T\Omega u)S-u^T\Omega v\bigr]
=q_B(S-c_W).
\tag{26}
$$



**New rigorous result:** the complete gamma insertion admits (9)–(10), with exact quadratic term (15), uniformly over all coordinates; its nonlinear remainder has the positive centered covariance bound (13).

**Remaining analytic bottleneck:** CSC, including normalized phase cancellation, the translation variance asymptotic, and scalar transfer at $o(d/n^2)$. The candidate is neither proved nor disproved here.

**Bounded exact calculation:** no finite computation is needed for these proofs. An optional algebraic verification can use (5)–(6), for $2\le d\le12$ and every $0\le j\le d+1$, to verify the constant, linear, and quadratic coefficients against (8), (14), and (15). Its expected output is identically zero discrepancies in $\mathbb Q(\sqrt2,n)$; it would certify only those finite checks.

**Irrationality status:** unresolved. Even a proof of (1) would not control the actual denominator after the final gcd. A sufficient separate arithmetic objective remains an infinite same-index sequence with $q_BM^{-2n-b}\to0$, together with the nonzero whole-error law.
