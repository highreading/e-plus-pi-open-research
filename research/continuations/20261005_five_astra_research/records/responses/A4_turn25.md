> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 — independent audit of critical four-fifths and the binary fourth norm digit

## Verdict

**Both assigned conclusions pass within their explicitly retained interfaces.**

* **Analytic:** A3turn22’s two new virial coefficients, first- and second-derivative errors, and equilibrium-derivative identification give an **actual $o(1)$ stationary-value comparison**, not merely a formal fifth-coefficient cancellation. The now-supplied complete exponential forcing also justifies its residual estimate. The relative whole-error conclusion remains dependent on the stated zero-free, signed-sector, reciprocal-anchor, and scalar-contour interfaces.
* **Binary:** A5turn18’s formula
  

$$
\boxed{\frac N{16}\equiv\binom{a+v+1}{v}\pmod2}
$$


  passes on the entire original exponent domain. The first-column convolution and the residual norm contributions are essential; the previously audited mixed-discrepancy identity alone would not establish this formula.

No higher $Q$-forcing is needed for the norm audit. I reuse the accepted off-pair and mixed-discrepancy audits rather than re-proving them.

Neither conclusion decides irrationality of $S=e+\pi$.

---

## 1. Analytic audit: domain and actual normalization

Throughout this part,


$$
\sigma=\sqrt2,\quad M=1+\sqrt2,\quad \rho=M^{-1},
\quad \alpha=\frac{\sigma}{M},\quad d=b-1,
$$


and


$$
n\to\infty,\qquad
\kappa _0n^{4/5}\le b\le\kappa _1n^{4/5},\qquad
0\le j\le b,
$$


with fixed positive $\kappa _0,\kappa _1$, integer indices, and both parities.

The positive auxiliary measure is exactly the principal tilted circular ensemble on $I=(-3\pi/4,3\pi/4)$, with particle weight


$$
g(t)^ne^{-\sigma\cos t}|e^{-it}+q|,
\qquad g(t)=1+\sigma\cos t,\qquad q=M,\rho.
$$


The actual insertion remains


$$
R_j=[t^j](t-1)(1+D_t)^{-n}
       \prod_{\ell=1}^d(z_\ell+t/\sigma),
$$


and actual averages use


$$
\langle F\rangle_j
=\frac{\mathbb E(\mathcal W_jF)}{N_j},
\qquad
\mathcal W_j=S_je^{i\Phi_q},\qquad N_j=\mathbb E\mathcal W_j.
$$


The retained bounds imply bounded $\mathcal W_j$ and $|N_j|\ge1/2$ eventually. None of the following transfers substitutes the positive ensemble for the actual complex expectation.

### 1.1 Safe-field expansions — pass

For


$$
V_q=-n\log g+h_q,\qquad
h_q=\sigma\cos t-\log|e^{-it}+q|,
$$


the anchors stay away from the characteristic zero circle, so


$$
h_q'(t)=O(t)
$$


uniformly on the closed principal interval.

The fields $v_k=t^kg/M$ cancel the base-potential pole and vanish at the endpoints. At collisions, the Vandermonde zero and the paired difference justify the integrated circular loop identity. Since differences lie strictly inside $(-2\pi,2\pi)$, the paired cotangent functions have removable diagonal singularities and no other poles. Their stated global remainder bounds follow from their Taylor orders at the origin and compactness elsewhere.

In particular, neither the endpoint nor the circular interaction has been replaced by a line-ensemble approximation.

### 1.2 Fourth moment coefficient — pass

Put


$$
T=\frac16-\alpha,\qquad V=\frac56-\frac92\alpha.
$$


The finite pair identities give


$$
\begin{aligned}
\alpha n(\mathbb EQ_4-\mathbb EQ_6/6)
={}&2d\,\mathbb EQ+\mathbb EX^2
-(\alpha+\tfrac16)d\,\mathbb EQ_4\\
&+(\tfrac16-\alpha)\mathbb E(XC_3)
-\frac{\alpha}{2}\mathbb EQ^2\\
&+O(n\mathbb EQ_8+d\mathbb EQ_6+\mathbb EQ_4).
\end{aligned}
$$


The $-5\alpha Q_4/2$ derivative term cancels the finite-degree contribution from the $S_4$ pair sum.

The required product estimates are centered:


$$
\mathbb EQ^2=(\mathbb EQ)^2+\operatorname{Var}Q
=\frac{d^4}{\alpha^2n^2}
 +O(d^5/n^3+d^2/n^2),
$$


and


$$
|\mathbb E(XC_3)|=O(d^2/n^2).
$$


The coefficient in the equation for $\alpha n\mathbb EQ_4$ is


$$
2T+\frac56-2(\alpha+\tfrac16)-\frac{\alpha}{2}
=\frac56-\frac92\alpha.
$$


Consequently,


$$
\boxed{
\mathbb EQ_4=
\frac{2d^3}{\alpha^2n^2}
+\frac{Vd^4}{\alpha^3n^3}
+O(d^2/n^2+d^5/n^4).
}
$$


The $h_q$ contribution is bounded first by $O(\mathbb EQ_4)$ in the loop equation; division by $n$ makes it harmless. It is not silently omitted.

### 1.3 Quadratic moment coefficient — pass

The degree-four circular corrections give


$$
\begin{aligned}
\alpha n(\mathbb EQ-\mathbb EQ_4/6+\mathbb EQ_6/120)
={}&d^2-(\alpha+\tfrac16)d\,\mathbb EQ
+(\tfrac16-\tfrac\alpha2)\mathbb EX^2\\
&+(\tfrac\alpha6-\tfrac1{360})d\,\mathbb EQ_4
+(\tfrac\alpha{24}-\tfrac1{120})\mathbb EQ^2\\
&+\tfrac1{90}\mathbb E(XC_3)
+O(n\mathbb EQ_8+d\mathbb EQ_6+\mathbb EQ).
\end{aligned}
$$


Here the finite $Q_4$ terms cancel, and the two $\alpha XC_3$ terms cancel.

The next coefficient is


$$
\begin{aligned}
U={}&\frac V6-\frac5{120}
-(\alpha+\tfrac16)T
+2(\tfrac\alpha6-\tfrac1{360})
+\frac\alpha{24}-\frac1{120}\\
={}&\alpha^2-\frac{3\alpha}{8}+\frac1{18}.
\end{aligned}
$$


Thus


$$
\boxed{
\mathbb EQ=
\frac{d^2}{\alpha n}
+\frac{Td^3}{\alpha^2n^2}
+\frac{Ud^4}{\alpha^3n^3}
+O(d^2/n^2+d^5/n^4).
}
$$


In this identity the $h_q$ term costs $O(\mathbb EQ/n)=O(d^2/n^2)$. The stated remainder therefore retains the complete bounded tilt.

---

## 2. Actual derivatives and fifth stationary comparison

### 2.1 First and second derivatives — pass

For $A=1+q$, expansion of $h(t)=(e^{-it}+q)^{-1}$ gives the stated $c_2,c_4,c_6$. These coefficients can be checked without sampling by recursively solving


$$
(q+e^{-it})h(t)=1
$$


through degree seven. Differentiating the even coefficients gives


$$
c_2'=\frac{2-q}{A^4},\qquad
c_4'=\frac{q^3-18q^2+33q-8}{12A^6}.
$$



The signed seventh-trace argument is valid: the safe-field recursion and Poincaré estimate yield


$$
\mathbb EC_7^2=O(d^7/n^7),
$$


while reflection makes its positive mean zero. Splitting the phase and insertion defect gives


$$
|\langle C_7\rangle_j|
\le C\left[
(\mathbb EC_7^2\,\mathbb E\Phi_q^2)^{1/2}
+\|S_j-1\|_\infty(\mathbb EC_7^2)^{1/2}
\right]
=O(d^4/n^4).
$$



Together with the centered even-moment transfers, this proves


$$
\begin{aligned}
(\log A_j)'(q)
={}&\frac dA+\frac{c_2}{\alpha}\frac{d^2}{n}
+\frac{c_2T+2c_4}{\alpha^2}\frac{d^3}{n^2}\\
&+\frac{c_2U+c_4V+5c_6}{\alpha^3}\frac{d^4}{n^3}
+O(d/n+d^5/n^4),
\end{aligned}
$$


and


$$
(\log A_j)''(q)
=-\frac d{A^2}
+\frac{c_2'}{\alpha}\frac{d^2}{n}
+\frac{c_2'T+2c_4'}{\alpha^2}\frac{d^3}{n^2}
+O(d/n+d^4/n^3).
$$


The second derivative’s covariance is algebraic. Centering at the positive-measure mean and using bounded $\mathcal W_j/N_j$ bounds it by $O(d/n)$; no positivity of a complex covariance is invoked.

Writing $\epsilon=d/n$, the first two stationary losses are


$$
O(d^2/n^2+d^6/n^5),\qquad
O(d^3/n^3+d^6/n^5),
$$


both $o(1)$ at the critical scale.

### 2.2 Equilibrium identification — pass, with the normalization made explicit

Let $m_k$ denote moments of the mass-one equilibrium measure. Its continuum loop identity is


$$
\int vV_0'\,d\mu_c
=\frac c2\iint
(v(\theta)-v(\phi))
\cot\frac{\theta-\phi}{2}\,d\mu_c(\theta)d\mu_c(\phi).
$$


This factor $c/2$ is important.

For example, its leading $v_5$ equation is


$$
\alpha m_6=c(2m_4+m_2^2)+O(c^4),
$$


so $m_2=c/\alpha+O(c^2)$ and
$m_4=2c^2/\alpha^2+O(c^3)$ give
$m_6=5c^3/\alpha^3+O(c^4)$.

The next $v_3,v_1$ equations are exactly the normalized leading versions of the audited equations above. The support bound $O(\sqrt c)$ controls their remainders. They yield


$$
m_2=\frac c\alpha+\frac T{\alpha^2}c^2+\frac U{\alpha^3}c^3+O(c^4),
$$




$$
m_4=\frac{2c^2}{\alpha^2}+\frac V{\alpha^3}c^3+O(c^4),
\qquad
m_6=\frac{5c^3}{\alpha^3}+O(c^4).
$$


Thus the actual derivative coefficients really match those of $ncL_c^{(k)}$, rather than merely resembling Gaussian coefficients.

### 2.3 Why the comparison is actually $o(1)$

The retained third/fourth precisions, together with the new first/second precisions, bound the increment discrepancy uniformly on $|x|\le C\epsilon$ by $o(1)$. The fifth insertion Taylor remainder is


$$
O(d\epsilon^5)=O(d^6/n^5)=O(n^{-1/5}),
$$


and the largest displayed fourth-derivative loss is $O(n^{-1/10})$.

A useful explicit stability lemma closes the stationary-value step:

> If two real functions $F,G$ attain their local minima in a common interval and $\sup|F-G|\le\delta$ there, then their minimum values differ by at most $\delta$.

Indeed, evaluate $F-G$ at each minimizer and use the two minimizing inequalities. Apply this to the anchored actual and equilibrium radial phases. Their positive curvature and stationary-location interfaces place both minimizers in the comparison interval.

The exact equilibrium stationary identity and actual reciprocal-anchor estimate therefore give


$$
\boxed{
[nf_-(r_-)+U_-(r_-)]-[nf_+(r_+)+U_+(r_+)]
=-(2n+d)\log M+o(1).
}
$$


This is an actual asymptotic comparison. No formal coefficient identity is being used as a substitute for an error estimate.

---

## 3. Complete forcing, adjacent norm, and whole analytic error

### Cauchy forcing bound — pass

From the complete definition


$$
eE_i=-[z^{n+i}]Q_0(z)^n\int_0^1s^ne^{1-s+sz}\,ds,
$$


on $|z|=\sigma$,


$$
|Q_0(z)|\le2+\sigma=\sigma M,\qquad
|e^{1-s+sz}|\le e^\sigma.
$$


Hence, for every $i\ge0$,


$$
\boxed{\sigma^i|eE_i|\le e^\sigma M^n/(n+1).}
$$


The complete elementary-symmetric insertion consequently costs $2^d$, not an unrecorded truncation:


$$
|E_j|\le CB_jZ_d^{\rm abs}(0)\frac{2^dM^n}{n+1}.
$$



### Actual adjacent-partition trial norm — pass

For the same fixed $n$ and the same principal weight,


$$
Z_{d+1}^{\rm pr}(0)/Z_d^{\rm pr}(0)=h_d.
$$


The monic trial polynomial is $z^d$, whose modulus is one. With the original $dt/(2\pi)$ normalization,


$$
h_d\le\int_I g(t)^ne^{-\sigma\cos t}\frac{dt}{2\pi}
\le e^\sigma M^n.
$$


This is a genuine adjacent-partition upper bound, not a comparison between unrelated partition estimates.

Together with the retained scalar lower bound and absolute/principal comparison,


$$
|E_j/P_j|\le\frac{e^{Cb}}{n!\sqrt n},\qquad
|D/P_0|\le\frac{C\sqrt n\,e^{Cb}}{n!B_0}.
$$


Here $B_0=\Gamma(n+d)\sigma^{-d}/\Gamma(n)>1$ eventually. Both residuals are $o(M^{-2n-b})$.

The scalar normalization ratio is $4\pi$, and the curvature ratio is $M^{-1}(1+o(1))$. Thus the retained contour interfaces give


$$
F_j/P_j=4\pi M^{-2n-b}(1+o(1)).
$$


Keeping the actual columns,


$$
u_j=(-1)^nP_j/D,\qquad
v_j-Su_j=\delta_{j0}+(-1)^nE_j/D-F_j/D,
$$


the whole error is


$$
\boxed{
c_j-S=\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac D{P_j}
=(-1)^{n+1}4\pi M^{-2n-b}(1+o(1)).
}
$$


It is eventually nonzero uniformly in $j$, and transfers by positive convex weighting to every positive diagonal metric in these actual coordinates.

---

## 4. Binary norm audit

The unchanged domain is


$$
b=9^r,\quad n=4002b,\quad r=18+32u,\quad u\ge0,
$$


with


$$
b=128D+81,\quad C=4002D+2532,\quad
a=(C-2)/4,\quad v=\lfloor D/4\rfloor.
$$


The actual weighted columns and metric remain


$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4b!},\qquad
\Omega_{jj}=(n+2)_{\underline j}^{\,2},\quad0\le j\le b.
$$



### 4.1 Sampled first-column polynomial and convolution — pass

The accepted off-pair identities eliminate all coordinates except $32\mid j$. From the accepted $P\bmod16$, the bounded moment products are exactly $2,12,6,4$, giving


$$
J(L)=2\binom{L+4}{4}+12\binom{L+4}{5}
 +6\binom{L+4}{6}+4\binom{L+4}{7}.
$$


Vandermonde gives


$$
\boxed{J(16s)=2+8s\pmod{16}\quad(s\ge0).}
$$


The lower-index binomial valuations in A5turn18 are sufficient for every $s$, including $s=0$.

Put $e=2C+1$ and $q=(b-1-j)/16$. At surviving coordinates $q$ is positive and odd. The unrestricted convolution is


$$
\theta_j\equiv\sum_{t=0}^q
 \binom{8e+t-1}{t}[2+8(q-t)]\pmod{16}.
$$


The unweighted sum is $T_q=\binom{8e+q}{q}$; modulo two the kernel is supported on multiples of eight. Therefore


$$
\theta_j\equiv10T_q\pmod{16},\qquad
\boxed{X_j\equiv-5W_jT_q\pmod8.}
$$


There are no Laurent boundary terms in this first-column calculation.

### 4.2 Four surviving residue classes — pass

Let


$$
E_t=\binom Ct\binom{e+D-t}{D-t},\qquad
\mathcal C=\#\{0\le t\le D:v_2(E_t)=1\}.
$$


The odd multiplier $-5$ preserves valuations through depth two.

* $j=128t,128t+64$, $0\le t\le D$: both coordinates have the truncated valuation of $E_t$. Their combined norm contribution is $8\mathcal C\bmod32$.
* $j=128t+32$, $0\le t\le D$: the weight adds exactly one valuation, giving $16\mathcal C\bmod32$.
* $j=128t+96$, **$0\le t\le D-1$**:
  

$$
v_2(W_j)=2+v_2((C-t)\binom Ct)\ge3,
$$


  because $(C-t)\binom Ct=C\binom{C-1}{t}$. These coordinates vanish modulo eight.

Thus


$$
\boxed{N\equiv24\mathcal C\pmod{32}.}
$$


The $32$-residue contribution cannot be discarded before evaluating the count.

### 4.3 Exact doubling and parity convolution — pass

Write $C=2c$, $c=2a+1$, $D=2d+1$, and $d=2v+\varepsilon$.
The even and odd index reductions respectively give


$$
v_2(E_{2s})
=1+v_2\!\left[\binom cs\binom{2c+d-s+1}{d-s}\right],
$$




$$
v_2(E_{2s+1})
=1+v_2\!\left[(c-s)\binom cs\binom{2c+d-s}{d-s}\right].
$$


For the first bracket to be odd, $s=2i+\varepsilon$; for the second, $s=2i$. Both have exactly $0\le i\le v$ and reduce to the same two parity conditions. Consequently, as ordinary finite counts,


$$
\mathcal C=2\mathcal T.
$$


Then


$$
\mathcal T\equiv[z^v](1+z)^a(1-z)^{-2a-2}
\equiv\binom{a+v+1}{v}\pmod2.
$$


Therefore


$$
\boxed{\frac N{16}\equiv\binom{a+v+1}{v}\pmod2.}
$$



The original subclass calculation also passes:


$$
D\equiv5+2u\pmod8.
$$


Thus $u\equiv1\pmod4$, equivalently $r=50+128w$, gives $D\equiv7\pmod8$, so $v$ and $a+1$ are both odd. This proves a populated infinite **zero** subclass. It does not prove that the nonzero branch is populated.

---

## 5. Final primitive bookkeeping and scope

For either actual rational-metric center, retain


$$
N_B=d_B[u,v],\quad
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\quad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_B=A_B/g_B,\qquad p_B=H_B/g_B.
$$


The primitive multiplier relative to the uncleared quadratic form is $d_B^2/g_B$, and


$$
q_BS-p_B
=\frac{d_B^2}{g_B}\bigl[(u^T\Omega u)S-u^T\Omega v\bigr].
$$



On the critical analytic domain this is


$$
(-1)^n4\pi q_BM^{-2n-b}(1+o(1))\ne0.
$$



On the separate binary fixed-ratio domain, the retained complete signed-error theorem gives


$$
q_nS-p_n=-q_n\epsilon_n>0,\qquad
\log|\epsilon_n|
=-\left(2+\frac1{4002}\right)n\log M+o(n).
$$


The exact denominator interface remains


$$
v_2(q_n)=
\max\left\{0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)\right\}.
$$


Combining the new norm digit with the already audited $H\equiv N\pmod{32}$ selects $\alpha=\gamma=4$ on the nonzero carry-test branch, and only $\alpha,\gamma\ge5$ on its complement. Lower bounds on both valuations cannot be subtracted to bound their difference.

## Closing ledger

1. **New result and proof status.** Both assigned audits pass within the retained interfaces. The analytic comparison is genuinely $o(1)$; the binary norm digit is proved by an unrestricted convolution and exact count doubling. The stationary-minimum stability lemma above makes explicit the final analytic comparison step.

2. **Exact remaining bottleneck.** No sufficient same-index bound on the actual reduced denominator after the final gcd has been established. In particular, the binary common-zero branch leaves unrestricted $\gamma-\alpha$ uncontrolled. Irrationality of $e+\pi$ remains unresolved.

3. **Computation request.** None. No finite growing-index calculation is required for these audits, and none would settle the remaining infinite denominator assertion.
