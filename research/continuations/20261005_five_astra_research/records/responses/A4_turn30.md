> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 research audit: the binary $T=0$ theorem and centered scalar comparison

## 1. Conclusions and verification scope

The two new arguments pass at their stated construction-level dependencies.

**Binary conclusion.** On the original domain


$$
b=9^r,\qquad n=4002b,\qquad r=18+32u,\quad u\ge0,
$$


the supplied complete $P_{64},Q_{128}$ interfaces, together with the fourth paired-column convolution, prove


$$
\boxed{T=0\ \Longrightarrow\ H-N\in64\mathbb Z_2.}
$$


In fact, every actual coordinate defect belongs to $64\mathbb Z_2$. The paired-column identity needed for this conclusion does follow from the complete turn17 formulas, with the correct sign and precision. An additional bounded evaluation gives its actual sampled unit:


$$
\boxed{K(16)\equiv48\pmod{64},\qquad \kappa_0\equiv3\pmod4.}
$$


Thus it is not necessary to infer any mixed cancellation from a norm identity.

Moreover,


$$
r\equiv50\pmod{128}\quad\Longrightarrow\quad T=0
$$


as an ordinary integer count. With the separately audited norm result on that subclass,


$$
\boxed{r=50+128w,\ w\ge0\quad\Longrightarrow\quad H\equiv N\equiv0\pmod{64}.}
$$



**Analytic conclusion.** Reusing the whole-leading scalar theorem at the scope passed in A4turn28, A3turn27’s new centered argument proves, uniformly for


$$
d=b-1\longrightarrow\infty,\qquad d=o(n),\qquad 0\le j\le b,
$$


and on both parities,


$$
\boxed{
\log\frac{c_j-S}{c_b-S}
=-\frac{s_j}{n^2}+o(d/n^2).
}
$$


Its consequence for every positive diagonal metric in the original coordinates also passes. The crucial improvement over a leading-order comparison is the common-reference complex-disk estimate and the centered insertion on the highest-coordinate contours.

These are advances in finite-precision arithmetic and fine analytic comparison. **Neither proves or disproves irrationality of $e+\pi$.**

### Verification gate

I compared the supplied mathematical texts and the explicit certificate entries. No external-search, filesystem, or execution tool is available in this exchange. Accordingly, I claim no fresh primary-literature search, independent hash verification, or executed certificate run. The supplied archive/search records retain their recorded scope.

I reuse the already passed $P_{64},Q_{128}$, 31-class support, and leading scalar interfaces rather than duplicate their audits. The new checks below concern the outstanding mixed identity and centered comparison. Classical factorial stripping, Lucas–Kummer arithmetic, strongly log-concave variance estimates, and contour estimates are used at the hypotheses exhibited here; no global novelty claim is made.

---

# Part I. Independent binary audit

## 2. Actual coordinates and the required raw precision

Keep exactly


$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4b!},\qquad
N=X^TX,\qquad H=X^TY,
$$


with


$$
R=2^{n/2}\binom n{n/2},\qquad
W_j=\binom{n+2}{j},\qquad
\Omega=\operatorname{diag}\bigl((n+2)_{\underline j}^{\,2}\bigr)_{0\le j\le b}.
$$


Every contact inverse retains its actual range $0\le i,j<b$.

The passed fifth-precision reconstruction is


$$
2X_j\equiv(-1)^{j+1}W_j\mathcal F_j\pmod{64},
$$




$$
4(Y_j-X_j)\equiv(-1)^{j+1}W_j\mathcal G_j\pmod{128}.
$$


Consequently,


$$
\boxed{
8X_j(Y_j-X_j)\equiv W_j^2\mathcal F_j\mathcal G_j\pmod{512}.
}
$$


The target for an individual defect is therefore raw divisibility by $512$, not by $256$.

The error precisions are sufficient because actual evenness gives


$$
W_j\mathcal F_j\in4\mathbb Z_2,\qquad
W_j\mathcal G_j\in8\mathbb Z_2.
$$


This permits multiplication of the two displayed residue formulas at modulus $512$.

The complete forcing is retained: all seven exterior values, every negative moment through $s=-8$, and the full logarithmic-force estimate. The latter removes the logarithmic force only because its **whole** valuation bound exceeds the required precision.

---

## 3. Audit of the fourth paired-column identity

Write


$$
k=2C+1,\qquad d=D-t,\qquad
B_d=\binom{k+d}{d},\qquad
E_t=\binom Ct B_d.
$$


Here $k$ is turn17’s $e$, not its sampled unit.

### 3.1 The sampled polynomial and its actual unit

At modulus $64$, reduction of the passed fifth vectors gives


$$
(d_0,\ldots,d_{11})
\equiv(48,38,10,60,16,24,56,0,32,16,16,32).
$$


The higher coefficients in turn17’s degree range are zero modulo $64$.

For


$$
K(L)=
\sum_{a=0}^6(-1)^aB_a\binom{L+a+4}{3}
+\sum_r d_r\binom{r+3}{3}\binom{L+4}{r+4},
$$


the boundary part has Newton coefficients


$$
(6272,2396,526,49).
$$


The nonzero coefficients


$$
m_r=d_r\binom{r+3}{3}\pmod{64}
$$


are


$$
m_0=48,\ m_1=24,\ m_2=36,\ m_3=48,\ m_4=48,\ 
m_6=32,\ m_8=32,\ m_{10}=32.
$$



These explicit values verify the required sampled properties:

* $K(4s)\equiv0\pmod4$;
* $K(16s)\equiv16\pmod{32}$;
* $K(16s+64)\equiv K(16s)\pmod{64}$.

For the second assertion, the boundary contribution is zero modulo $32$. In the polynomial contribution, $m_0\binom{16s+4}{4}\equiv16$; all remaining terms vanish modulo $32$. The only slightly stronger divisibility needed here is


$$
8\mid\binom{16s+4}{6},
$$


which follows directly by Vandermonde expansion against $16s$.

For periodicity, the polynomial terms satisfy


$$
v_2(m_r)\ge\lfloor\log_2(r+4)\rfloor.
$$


Vandermonde with


$$
v_2\binom{64}{a}\ge6-\lfloor\log_2a\rfloor
$$


then supplies six bits. For the cubic boundary term, evaluating the translation difference at $16\mid L$ supplies the same precision.

The actual value at $L=16$ can also be evaluated without a growing-index calculation. The boundary part is zero modulo $64$. The polynomial part is


$$
48\binom{20}{4}
+24\binom{20}{5}
+36\binom{20}{6}
+48\binom{20}{7}
+48\binom{20}{8}
+32\binom{20}{10}
+32\binom{20}{12}
+32\binom{20}{14},
$$


which is


$$
48+0+32+0+32+0+0+0\equiv48\pmod{64}.
$$


Thus


$$
\boxed{\kappa_0=K(16)/16\equiv3\pmod4.}
$$



### 3.2 Coordinate translation and bounded moment losses

The actual difference is $\zeta=\eta-2\theta$. At $64\mid j$, replacing the bounded polynomial argument $j+x$ by $x$ is valid modulo $64$.

Indeed, for a Newton coefficient of degree $r$, translation by $j$ loses at most $\lfloor\log_2r\rfloor$ of the six available bits. The low coefficients have the necessary extra divisibility:


$$
v_2(d_1)=v_2(d_2)=1,\qquad v_2(d_3)\ge2,
$$


and the higher coefficients supply the remaining losses. The bounded replacement


$$
\binom{2n+r-1}{r}\longmapsto\binom{r+3}{3}
$$


has seven parameter bits before its bounded-index loss and is likewise valid.

These replacements do **not** replace the actual long kernel or its finite upper boundary.

### 3.3 Unrestricted convolution and the Laurent endpoint

The binary power reduction


$$
(1-z)^{-128k}\equiv(1-z^4)^{-32k}\pmod{64}
$$


is valid in the integral formal power-series ring. Put


$$
c_v=\binom{32k+v-1}{v}.
$$


For $v>0$,


$$
v_2(c_v)\ge5-v_2(v).
$$



When $16\mid L$, the sampled divisibilities eliminate all convolution indices except $v=16w$. For those indices, periodicity makes the sampled factor equal to $K(L)$.

The required coefficient reduction is only modulo $4$:


$$
c_{16w}\equiv\binom{2k+w-1}{w}\pmod4.
$$


One way to verify it is to apply successively


$$
(1-y)^{4a}\equiv(1-y^2)^{2a}\pmod4
$$


also for negative integral exponents, until the exponent $-32k$ becomes $-2k$.

The Laurent endpoint is not omitted. Of the negative degrees $-1,\ldots,-7$, only $-4$ can meet the surviving kernel support. Its boundary coefficient is


$$
-56+4\cdot56-10\cdot16+20\cdot48=968,
$$


which is divisible by $4$. Its corresponding kernel index is odd, so the product vanishes modulo $64$.

Hence turn17’s unrestricted formula is justified:


$$
\zeta_j\equiv
K(L)\binom{2k+\lfloor L/64\rfloor}{\lfloor L/64\rfloor}
\pmod{64}.
$$



### 3.4 Paired higher binomials

For


$$
j_0=128t,\qquad j_1=128t+64,
$$


the corresponding $L=b-1-j$ values are


$$
128d+80,\qquad128d+16.
$$


Both are $16\pmod{64}$.

Even-binomial scaling and the adjacent ratio give


$$
\binom{2k+2d}{2d}\equiv B_d\pmod4,
$$




$$
\binom{2k+2d+1}{2d+1}
=\frac{2k+2d+1}{2d+1}\binom{2k+2d}{2d}
\equiv3B_d\pmod4,
$$


because $k$ is odd and the denominator is odd.

Therefore the critical identity is


$$
\boxed{
\zeta_{j_0}\equiv48\kappa_0B_d,\qquad
\zeta_{j_1}\equiv16\kappa_0B_d\pmod{64}.
}
$$


With the actual unit evaluated above, this is equivalently


$$
\zeta_{j_0}\equiv16B_d,\qquad
\zeta_{j_1}\equiv48B_d\pmod{64}.
$$



### 3.5 Reconstruction sign, $j\zeta_{j-1}$, and weights

At either paired coordinate, $j$ is even. The exact reconstruction has


$$
4(Y_j-X_j)=W_j(j\zeta_{j-1}-\zeta_j).
$$


The moment convention has


$$
4(Y_j-X_j)\equiv-W_j\mathcal G_j,
$$


so


$$
W_j\mathcal G_j\equiv W_j(\zeta_j-j\zeta_{j-1}).
$$


There is no extra minus sign in the resulting paired formula.

Since $\zeta_{j-1}$ is integral and $64\mid j$,


$$
j\zeta_{j-1}\equiv0\pmod{64}.
$$


For $j=0$, this is also consistent with the actual extension at $-1$.

The required weight congruence is


$$
W_{128t}\equiv W_{128t+64}\equiv\binom Ct\pmod4.
$$


For example, modulo $4$, the multiples-of-$64$ part of


$$
(1+x)^{128C+68}
$$


reduces to the relevant coefficients of


$$
(1+y)^{2C}(1+y),\qquad y=x^{64}.
$$


Because $C$ is even,


$$
(1+y)^{2C}\equiv(1+y^2)^C\pmod4.
$$


Both paired coefficients are therefore $\binom Ct$.

Combining these facts gives exactly the needed mixed formulas:


$$
\boxed{
W_{j_0}\mathcal G_{j_0}\equiv48\kappa_0E_t,\qquad
W_{j_1}\mathcal G_{j_1}\equiv16\kappa_0E_t\pmod{64}.
}
$$


Only weight precision $4$ is needed because the displayed scalar factors contain $16$.

**Verdict:** A5turn21’s critical identity (32), and its use in (34), pass. The fixed 1023-comparison certificate does not prove this identity; the convolution calculation does.

---

## 4. All 31 classes and overflow

Seven-level factorial stripping gives the exact common-factor formulas in turn21. In particular,


$$
M_s=
\frac{J_d}{k}P_\varepsilon k^{\delta_s}
2^{m_{\rho s}}u_{\rho s},
$$


where


$$
J_d=\binom{k+d-1}{d},\qquad P_0=k+d,\qquad P_1=d.
$$


Only the odd integer $k$ is inverted. The factors $d$, $k+d$, $k^{\delta_s}$, and $C-t$ remain present.

For non-overflow classes,


$$
W_{\rho,t}^2\mathcal F_{\rho,t}\mathcal G_{\rho,t}
=
2^{2b_\rho}w_\rho^2E_t^2
\mathfrak f_\rho\mathfrak g_\rho.
$$


The coefficient-depth bounds supplied by the explicit finite certificate imply, when $e_t=v_2(E_t)\ge2$,

| Residues $\rho$ | Raw depth lower bound |
|---|---:|
| $4,68$ | $12$ |
| $2,66$ | $10$ |
| $32$ | $9$ |
| $36$ | $14$ |
| $1,3,16,20,34,48,52,65,67$ | $9$ |
| $8,12,18,24,28,33,35,40,44,50,56,60$ | $10$ |

This covers all 27 nonpaired non-overflow classes.

For $96,100$, retain the shorter range


$$
0\le t\le D-1.
$$


The actual common factor is


$$
(C-t)\binom Ct\binom{k+d-1}{d-1},
$$


and


$$
v_2\!\left((C-t)\binom Ct\right)
=v_2\!\left(C\binom{C-1}{t}\right)\ge1.
$$


Thus $\rho=96$ has raw depth at least $6+1+2=9$, and $\rho=100$ has greater depth. No condition on $E_t$ is needed for these two classes.

For the remaining pair $0,64$:

* if $e_t\ge3$, the stripping bound already gives depth at least $9$;
* if $e_t=2$, the audited mixed identity gives
  

$$
W_j\mathcal G_j\in64\mathbb Z_2,
$$


  while stripping gives
  

$$
W_j\mathcal F_j\in2E_t\mathbb Z_2\subset8\mathbb Z_2.
$$



Hence their raw products also belong to $512\mathbb Z_2$.

The earlier high-weight exclusion covers every other interior coordinate. At the actual endpoint,


$$
X_b=\frac{W_b b\theta_{b-1}}2,\qquad
Y_b=\frac{W_b(1+b\eta_{b-1})}{4},
$$


and the retained weight depth gives a defect in $2^9\mathbb Z_2$. The $+1$ is retained before taking valuations.

Therefore


$$
\boxed{
4\mid E_t\ \text{for every }0\le t\le D
\quad\Longrightarrow\quad
X_j(Y_j-X_j)\in64\mathbb Z_2
\ \text{for every }0\le j\le b.
}
$$



---

## 5. True depth-one classification and the integer condition $T=0$

It is useful to verify the counting interface directly rather than use a parity count in its place.

Write


$$
C=4a+2,\qquad D=4v+\delta,\qquad \delta\in\{1,3\},
$$


so $k=8a+5$. Every $E_t$ is even:

* if $t$ is odd, $\binom Ct$ is even;
* if $t$ is even, $d=D-t$ is odd, and adding $d$ to the odd $k$ creates a carry.

The low-two-bit Kummer classification is:

* for $\delta=1$, depth exactly one is possible only at
  

$$
t=4i,\quad4i+1;
$$


* for $\delta=3$, it is possible only at
  

$$
t=4i+1,\quad4i+2.
$$



In each case, exactly one low carry occurs, and absence of all higher carries is equivalent to


$$
\binom ai\ \text{odd},\qquad
\binom{2a+1+v-i}{v-i}\ \text{odd}.
$$


Both representatives lie in the actual range precisely for $0\le i\le v$. Consequently,


$$
\boxed{\#\{t:v_2(E_t)=1\}=2T}
$$


as an integer equality.

For the original subclass,


$$
9^{18+32u}\equiv721+256u\pmod{1024}.
$$


Thus


$$
D\equiv5+2u\pmod8.
$$


When $r=50+128w$, one has $u=1+4w$, hence $D\equiv7\pmod8$. It follows that $v$ is odd and


$$
a=\frac{4002D+2530}{4}
$$


is even.

An admissible $i$ in the definition of $T$ must be even. Also $q=v-i$ must be even, because


$$
q\mathbin{\&}(2a+1)=0
$$


and $2a+1$ is odd. Their sum cannot be the odd integer $v$. Therefore $T=0$, not merely $T\equiv0\pmod2$.

Together with evenness and the exact count, this proves $v_2(E_t)\ge2$ for every $t$, closing the binary theorem.

The further assertion $N\equiv0\pmod{64}$ on this subclass uses the separately retained norm formula and its $\chi=0$ subclass evaluation. It is not needed to prove $H-N\equiv0$.

---

# Part II. Independent centered scalar audit

## 6. Tilted moments, endpoint integrability, and the fixed-angle event

The positive principal ensemble remains on the original ordered chamber in


$$
I=(-3\pi/4,3\pi/4).
$$


Its potential is exactly


$$
V_q(t)=-n\log(1+\sqrt2\cos t)+\sqrt2\cos t
-\frac12\log(1+q^2+2q\cos t).
$$



At a principal endpoint, the density has a factor of order $\operatorname{dist}^n$; its differentiated density has order $\operatorname{dist}^{n-1}$. Thus the score is integrable for $n\ge1$, and endpoint flux vanishes. At collisions, the Vandermonde square cancels the first-order score singularity. The sum-translation field is also tangent to collision faces.

The Hessian estimate


$$
\nabla^2\mathcal V_q\ge(n\alpha-C)I,\qquad \alpha=\sqrt2/(1+\sqrt2),
$$


holds on the actual chamber.

Under


$$
\tan(\theta/2)=\sqrt c\,u,\qquad c=d/n,
$$


the added real-anchor tilt has second derivative $O(c)$ and is even. Hence the mode comparison and radial domination from turn23 apply to the **tilted** rescaled energy. They give


$$
\mathbb E\sum_i\theta_i^{2m}\le C_mdc^m.
$$



For fixed $\delta>0$, the event $\max|\theta_i|>\delta$ requires a rescaled displacement of order $c^{-1/2}$. The radial tail exponent is


$$
-K_\delta n+O(d\log(1/c))+O(d).
$$


Since $c\log(1/c)\to0$,


$$
\boxed{\mathbb P\{\max|\theta_i|>\delta\}\le e^{-\kappa_\delta n}.}
$$


This is strong enough on arbitrarily slow-growing $d$; a bare $e^{-\gamma d}$ wall estimate would not be.

For fixed complex disks, the later argument needs Hessian and Lipschitz variance bounds, not reflection symmetry or this tilted real-mode argument. This separation of uses is important.

---

## 7. Truncated translation identity and collision bounds

The untruncated identity


$$
\mathbb E\!\left[X\sum_iV_q'(\theta_i)\right]=d,\qquad
X=\sum_i\theta_i,
$$


is legitimate by the endpoint and collision checks above.

The singular score itself cannot be assigned a globally bounded cubic remainder. Turn27 correctly replaces that invalid step by a smooth field. With even $\chi$ supported away from the endpoints,


$$
R(t)=\chi(t)\frac{\sqrt2\sin t}{1+\sqrt2\cos t}-\alpha t
$$


is smooth and odd, with


$$
|R'(t)|\le Ct^2.
$$


Brascamp–Lieb and the fourth moment yield


$$
\operatorname{Var}\Bigl(\sum_iR(\theta_i)\Bigr)\le Cc^3,
\qquad
\left|\operatorname{Cov}\Bigl(X,\sum_iR(\theta_i)\Bigr)\right|
\le Cc^2.
$$



For the field $v_i=X\chi(\theta_i)$, the interaction contribution contains


$$
X\sum_{i<k}
(\chi(\theta_i)-\chi(\theta_k))
\cot\frac{\theta_i-\theta_k}{2}.
$$


Near a collision, the difference of $\chi$ cancels the pole. There are no other cotangent poles in the closure of the allowed difference interval except the collision pole: the differences lie in $[-3\pi/2,3\pi/2]$, strictly short of $\pm2\pi$. Thus each summand is uniformly bounded.

All exceptional terms are consequently polynomial factors times $e^{-\kappa n}$. This proves


$$
\boxed{
\operatorname{Var}(X)
=\frac{d}{n\alpha}+O(c^2+c/n)+O(n^Ce^{-\kappa n}).
}
$$


Subtracting the truncated identity from the exact full identity controls the omitted singular-score contribution. No pointwise bound on that omitted score is necessary.

This repairs the first obstruction identified in turn26.

---

## 8. Actual phase normalization and the complete nonlinear insertion

At real anchors, reflection gives


$$
\Phi_q=\eta_qX+T_q,\qquad
\|T_q\|_2=O(c^{3/2}),\qquad
\eta_q=-\sqrt2-\frac1{1+q}.
$$


Strong log-concavity gives fixed-$p$ bounds


$$
\|\Phi_q\|_p=O(\sqrt c).
$$


Therefore


$$
\mathbb E e^{i\Phi_q}=1+O(c),
$$


with the actual denominator kept throughout.

Writing $e_1=C+iY$, one has


$$
\operatorname{std}(C)=O(c),\qquad
\|Y-X\|_2=O(c^{3/2}).
$$


Parity and the sine/cosine expansions then give


$$
\boxed{
\mathbb E_{e^{i\Phi_q}}e_1-\mathbb Ee_1
=-\eta_q\operatorname{Var}(X)+O(c^2).
}
$$


At $M,\rho$, the positive measures agree exactly and


$$
\eta_\rho-\eta_M=-\rho.
$$



The complete gamma insertion, rather than its linear truncation, is


$$
L_j=\log\mathcal S_j=-a_je_1+H_j,
$$


with


$$
a_j\le C/n,\qquad
|H_j|\le Cd^2/n^2,\qquad
|\partial_{z_i}H_j|\le Cd/n^2.
$$


Thus


$$
\operatorname{std}(H_j)\le Cd^{3/2}n^{-5/2}.
$$


Centering against the actual phase gives


$$
\mathbb E_wH_j-\mathbb EH_j=O(d^2/n^3).
$$



Finally,


$$
|L_j|\le Cc,\qquad
\mathbb E|L_j-\mathbb EL_j|^2\le Cd/n^3.
$$


Taylor expansion of the exponential around $\mathbb EL_j$, followed by the local logarithm, proves


$$
\log\mathbb E_we^{L_j}
=\mathbb E_wL_j+O(d/n^3).
$$


This controls the entire insertion cumulant. It is not an application of a variance inequality to a signed measure.

The reciprocal-anchor result is consequently


$$
\log Q_j(\rho)-\log Q_j(M)
=-a_j\rho\,\frac d{n\alpha}
+O(d^2/n^3+d/n^3)+O(n^Ce^{-\kappa n}).
$$


Every displayed remainder is $o(d/n^2)$.

---

## 9. Common-reference disks and centered contour transfer

Let


$$
\mathcal R_j=\exp(\mathbb E_*L_j)
$$


use the same positive measure without characteristic modulus for both disks.

For complex $q$, interpolation of the modulus tilt preserves the Hessian lower bound. Its score has variance $O(d/n)$, whereas $L_j$ has variance $O(d/n^3)$. Hence


$$
|\mathbb E_qL_j-\mathbb E_*L_j|\le Cd/n^2.
$$



The complex phase need not be odd. Subtracting its exact mean gives a phase with variance $O(c)$, whose exponential expectation is $1+O(c)$. The preceding centered covariance and cumulant estimates therefore imply


$$
\boxed{Q_j(q)/\mathcal R_j=1+O(d/n^2)}
$$


uniformly on both fixed disks. Signed outer sectors are exponentially small there at the retained scalar interface.

This bound supplies a zero-free branch close to $1$. Cauchy estimates on smaller disks give


$$
\partial_q^m\log Q_j(q)=O_m(d/n^2).
$$


A zero-free statement without the common reference would not imply this derivative scale.

Now use the **same highest-coordinate contours** for every insertion. Their real saddles differ from the anchors by $O(c)$, so the anchor-to-saddle cost is


$$
O(cd/n^2)=o(d/n^2).
$$


On the central arc, the normalized highest-coordinate integral has bounded absolute mass and first absolute angular moment $O(n^{-1/2})$. Therefore the centered insertion cost is


$$
O(d/n^{5/2})=o(d/n^2).
$$


The retained remote arcs and both minus connectors have error $\exp(-\kappa n+Cd)$, also negligible at this scale.

Thus


$$
\boxed{
\log\!\left[\frac{F_j/F_b}{P_j/P_b}\right]
=-a_j\rho\,\frac d{n\alpha}+o(d/n^2)
=-\frac{s_j}{n^2}+o(d/n^2).
}
$$



No additional restriction such as $d\gg\log n$ is introduced. Neither parity nor any actual coordinate is excluded.

---

## 10. Whole error and metric consequence

The finite systems remain


$$
H_b,T:\ 0,\ldots,d,\qquad
K:\text{ rows }0,\ldots,b,\text{ columns }0,\ldots,d.
$$


Retain the complete exponential force


$$
eE_i=-[z^{n+i}](1-z+z^2/2)^n
\int_0^1s^ne^{1-s+sz}\,ds,
$$


and its complete elementary-symmetric insertion into $E_j$.

The exact coordinate error is


$$
c_j-S=
\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac D{P_j}.
$$


The passed factorial residual bounds remain negligible even after division by the leading error times $d/n^2$. Therefore CSC applies to this **whole** error.

For any positive diagonal metric,


$$
c_W-S=\sum_j\alpha_j(c_j-S),\qquad
\alpha_j=\frac{W_{jj}u_j^2}{u^TWu}.
$$


Uniformity gives


$$
\boxed{
\log\frac{c_W-S}{c_b-S}
=-\frac{\sum_j\alpha_js_j}{n^2}+o(d/n^2).
}
$$


The remainder is independent of the ratios of the positive diagonal entries. No assertion is made for arbitrary nondiagonal metrics.

---

# Part III. Primitive arithmetic, remaining bottlenecks, and calculation ledger

## 11. The final gcd and the whole evaluated form remain indispensable

For either rational-metric construction, retain the least actual clearer $d_B$, the actual integral metric scaling $\Omega$, and


$$
N_B=d_B[u,v],\qquad
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


Then


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_B=A_B/g_B,\qquad p_B=H_B/g_B.
$$


The primitive multiplier on the uncleared quadratic pair is exactly


$$
\boxed{d_B^2/g_B.}
$$


The whole evaluated error is


$$
\boxed{q_BS-p_B=q_B(S-c_W).}
$$



For the binary family, the retained exact interface is


$$
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)
\right\}.
$$


The new theorem gives $\alpha,\gamma\ge6$ on $r\equiv50\pmod{128}$, but gives no unrestricted bound on $\gamma-\alpha$.

The binary whole signed error retains its separate fixed-ratio rate


$$
\log|\epsilon_n|
=-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n),
\qquad
q_nS-p_n=-q_n\epsilon_n.
$$


The all-sublinear analytic theorem must not be substituted into this fixed-ratio family.

For the sublinear analytic family,


$$
q_BS-p_B
=(-1)^n4\pi q_BM^{-2n-b}(1+o(1)).
$$


CSC refines relative coordinate spread; it does not bound $q_B$.

---

## 12. Closing ledger

### New results and proof status

1. **Binary mixed theorem passed:** $T=0$ implies coordinatewise defect divisibility by $64$, hence $H\equiv N\pmod{64}$.
2. **Critical mixed unit identity independently checked:** its actual sampled unit is $\kappa_0\equiv3\pmod4$; coordinate sign, $j\zeta_{j-1}$, weight precision, and Laurent endpoint all agree.
3. **Original populated subclass verified:** $r\equiv50\pmod{128}$ forces integer $T=0$. With the retained norm theorem, $H\equiv N\equiv0\pmod{64}$.
4. **CSC passed:** the original-chamber truncation, tilted radial estimates, normalized complete cumulant, common complex reference, and centered scalar transfer give the claimed $o(d/n^2)$ result for both parities and every original-coordinate positive diagonal metric.

### Exact remaining mathematical bottlenecks

At fifth binary precision, the unevaluated sector is still


$$
v_2(E_t)=1,
$$


whose population is $2T$. A concrete next lemma is to evaluate its complete stripped mixed-unit contraction, with the residue-dependent precisions in turn21, including terminal ranges. Positive even $T$ cannot be replaced by $T=0$.

Beyond fixed precision, the arithmetic task is control of the actual final gcd and reduced denominator at unrestricted depth.

For irrationality, a sufficient separate objective remains an infinite same-index sequence satisfying


$$
q_BM^{-2n-b}\longrightarrow0
$$


in the sublinear family, together with the proved nonzero whole-error law. No supplied result establishes that objective.

### Bounded exact arithmetic

The new paired-unit calculation has fixed inputs:

* $d_{0:11}\bmod64$;
* the seven boundary values modulo $64$;
* the displayed definition of $K(L)$.

Its verifiable output is


$$
K(16)\equiv48\pmod{64},
$$


together with the three sampled polynomial congruences checked above.

The supplied 1023-comparison certificate concerns only the fixed stripping inequalities. Its zero-residue entries should formally be read using the available coefficient precision, not as claims that the underlying coefficients are identically zero; those available depths already exceed every required bound.

The 32 auxiliary-$D$ checks retain only their stated finite scope. No additional auxiliary sampling is needed for the proved $T=0$ implication, and no finite sampling can replace the remaining unit-contraction or primitive-denominator lemma.



$$
\boxed{\text{The irrationality of }e+\pi\text{ remains unresolved.}}
$$


