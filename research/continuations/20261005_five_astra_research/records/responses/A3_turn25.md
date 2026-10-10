> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3 — scalar and sector closure for the all-sublinear relative law

Put


$$
\sigma=\sqrt2,\qquad M=1+\sqrt2,\qquad \rho=M^{-1},
\qquad d=b-1,\qquad S=e+\pi.
$$



The index domain throughout the asymptotic conclusion is


$$
n\longrightarrow\infty,\qquad 1\le b=b(n)=o(n),
\qquad 0\le j\le b,
\tag{1}
$$


with integer indices and **both parities of $n$**.

The sector, anchor, zero-free logarithm, scalar saddle, remote-contour, connector, and residual interfaces can be closed on this domain. The remaining analytic dependency is precisely the uniform bias lemma of turns23–24, which is currently under independent audit. I use that lemma **conditionally**, not as an independently audited result.

More precisely, the sole retained analytic input needed beyond the established source results is:

> **UB input.** For $d\to\infty$, $c=d/n\to0$, on fixed real neighborhoods of $M$ and $\rho$,
> 

$$
> (\log A_j)'(q)=dL_c'(q)+O(1),
> \tag{UB}
>
$$


> uniformly in every actual coordinate $0\le j\le b$. Here $A_j$ is the original full-circle complex characteristic integral and $L_c$ uses the exact mass-one principal equilibrium.

Turns23–24 propose a proof of UB. Below I correct its operator-domain formulation and prove the other all-sublinear interfaces explicitly. No additional “all-sublinear scalar interface” is assumed.

---

## 1. Actual objects and exact sector normalization

Retain


$$
R_j(z)=[t^j](t-1)(1+D_t)^{-n}
                    \prod_{\ell=1}^d(z_\ell+t/\sigma),
$$




$$
A_j(q)=\nu_{n,d}\!\left(R_j(z)\prod_{\ell=1}^d(z_\ell^{-1}+q)\right),
$$


and the signs and scales


$$
s_0=(-1)^{d+1},\qquad
s_j=(-1)^{d-j+1}\ (1\le j\le d),\qquad s_b=1,
$$




$$
B_j=|K_{j,d}|\sigma^{-d},\qquad S_j=s_jR_j/B_j.
\tag{2}
$$


For $d=0$, these give $R_0=-1,R_1=1$, $B_0=B_1=1$.

Write


$$
I=(-3\pi/4,3\pi/4),\qquad O=[-\pi,\pi]\setminus I,
\qquad g(t)=1+\sigma\cos t.
$$


For a symmetric insertion $G$, the exact circle functional decomposes as


$$
\begin{aligned}
\nu_{n,r}(G)
={}&\sum_{k=0}^r\frac{(-1)^{nk}}{k!(r-k)!}
\int_{I^{r-k}\times O^k}
G(z)\,|\Delta(z)|^2\\
&\hspace{13mm}\times
\prod_{\ell=1}^r
\left[|g(t_\ell)|^n e^{-\sigma z_\ell}
                         \frac{dt_\ell}{2\pi}\right].
\end{aligned}
\tag{3}
$$


Thus the principal sector is exactly $k=0$, and each outer sector retains its sign $(-1)^{nk}$. There is no extra binomial coefficient after using $1/[k!(r-k)!]$.

Define the positive principal partitions by


$$
Z_r(q)=\frac1{r!}\int_{I^r}|\Delta(z)|^2
\prod_{\ell=1}^r
\left[g(t_\ell)^n e^{-\sigma\cos t_\ell}
       |z_\ell^{-1}+q|\frac{dt_\ell}{2\pi}\right].
\tag{4}
$$


The notation $Z_r(0)$ denotes the same partition without a nontrivial characteristic modulus, since $|z^{-1}|=1$. All adjacent dimensions below have the **same $n$ and the same one-particle weight**.

---

## 2. Signed outer sectors and their derivatives

The supplied monic arc-norm estimate gives, uniformly on


$$
|q|\le3/4\quad\text{or}\quad 2\le|q|\le3,
$$




$$
h_\ell(q)\ge
C_\delta g_\delta^n B_\delta^\ell/(\ell+1)^2,
\qquad
Z_r(q)=\prod_{\ell=0}^{r-1}h_\ell(q).
\tag{5}
$$


Its proof depends only on the actual positive weight and monic polynomial degree, not on a positive limiting value of $r/n$.

Outside $I$, the integrated one-particle absolute weight is at most $CM^{-n}$. Bounding every cross/outer Vandermonde factor by $4$, and dividing by the same norms in (5), gives


$$
\frac{|\text{\(k\)-outer absolute sector}|}{Z_r(q)}
\le\frac1{k!}
\left[
Cr^2(4/B_\delta)^r(Mg_\delta)^{-n}
\right]^k.
\tag{6}
$$


Consequently, for $r=o(n)$,


$$
\frac{\text{sum of all nonprincipal absolute sectors}}{Z_r(q)}
\le \exp(-\eta n+Cr)
\tag{7}
$$


eventually, with fixed $\eta>0$. Polynomial factors in $r$ have been absorbed by slightly decreasing $\eta$. This applies to $r=d$ and $r=b$.

For a fixed derivative order $m$, direct differentiation of the characteristic product gives


$$
\left|\partial_q^m\prod_{\ell=1}^d(z_\ell^{-1}+q)\right|
\le (d)_{\underline m}\delta^{-m}
              \prod_{\ell=1}^d|z_\ell^{-1}+q|,
\tag{8}
$$


on any compact subset with distance at least $\delta>0$ from the characteristic zero circle. Hence the differentiated outer-sector bounds retain the form


$$
\exp(-\eta_m n+C_m d).
\tag{9}
$$


These estimates control the original signed sectors on either parity; they do not replace them by a positive ensemble.

The gamma expansion also gives, directly and uniformly on the entire circle polydisk,


$$
\|S_j-1\|_\infty
\le e^{\sigma d/n}-1=O(d/n).
\tag{10}
$$


Indeed, every normalized degree-$k$ gamma term is a polynomial with constant term $1$, and the sum of absolute nonconstant coefficients is bounded by
$(1+\sigma/n)^k-1$. Middle-coordinate references are positive combinations of these terms.

---

## 3. Normality and the actual zero-free logarithms

The concentration and sector proof in the supplied small-ratio sources is already uniform for $b\le n/1000$. Its hypotheses therefore hold eventually for every sequence (1).

For positive real $q$ in the two characteristic regions, reflection makes the principal phase


$$
\Phi_q=\sum_\ell[-\sigma\sin t_\ell+
                         \arg(e^{-it_\ell}+q)]
$$


odd, with mean zero. The actual normalized principal expectation is


$$
N_j(q)=\mathbb E_q(S_je^{i\Phi_q}).
\tag{11}
$$


The supplied Hessian estimate and Brascamp–Lieb inequality give


$$
\mathbb E_q\Phi_q^2=O(d/n).
$$


Since symmetry makes $\mathbb E_qe^{i\Phi_q}$ real,


$$
\left|\mathbb E_qe^{i\Phi_q}-1\right|
\le \tfrac12\mathbb E_q\Phi_q^2.
$$


Together with (10),


$$
N_j(q)=1+O(d/n).
\tag{12}
$$


Including (7),


$$
s_jA_j(q)=B_jZ_d(q)
 \left[1+O(d/n)+O(e^{-\eta n+Cd})\right]>0.
\tag{13}
$$



For complex $q$, the mean-phase rotation argument in the supplied zero-free proof gives, on fixed neighborhoods of both anchors,


$$
\tfrac12B_jZ_d(q)\le |A_j(q)|\le2B_jZ_d(q)
\tag{14}
$$


eventually. The proof applies also to $d=0,1$: its insertion, variance, and sector inequalities require no lower bound $d\ge2$. For $d=0$, $A_j=R_j$ exactly.

Omitting the characteristic and insertion in this same argument proves


$$
D=\det H_b>0
\tag{15}
$$


eventually, including $b=1,2$.

### Fixed-neighborhood logarithmic derivative bounds

Choose slightly smaller fixed disks around $M$ and $\rho$, contained in the zero-free regions. On each disk define


$$
\mathcal H_j(q)=
\Log\frac{A_j(q)}{s_jB_jZ_d(0)},
\tag{16}
$$


anchored real at the positive real center.

Every characteristic modulus on these disks lies between two fixed positive constants. Thus (14) implies


$$
|\Re\mathcal H_j(q)|\le C(d+1).
\tag{17}
$$


Interior harmonic estimates, the real anchor, and the Cauchy–Riemann equations then give, on smaller disks,


$$
|\mathcal H_j^{(m)}(q)|\le C_m(d+1)
\tag{18}
$$


for every fixed $m$. These are bounds for the **actual zero-free logarithm**. They do not require empirical convergence or UB.

For $d\ge1$, the right side may be written $C_md$. For $d=0$, all derivatives vanish.

---

## 4. Reciprocal anchors: an exact partition identity and an $o(1)$ actual error

For $|z|=1$,


$$
|z^{-1}+M|=M|z^{-1}+\rho|.
$$


It follows with every normalization in (4) unchanged that


$$
Z_d(M)=M^d Z_d(\rho).
\tag{19}
$$


The two normalized positive tilted measures at these anchors are in fact identical.

Using (13),


$$
\log\frac{s_jA_j(\rho)}{s_jA_j(M)}
=-d\log M+O(d/n)+O(e^{-\eta n+Cd}).
\tag{20}
$$


This proves the needed actual reciprocal-anchor relation uniformly on (1).

For the symmetric mass-one equilibrium, the same modulus identity and the real positive branches give


$$
L_c(M)-L_c(\rho)=\log M.
\tag{21}
$$


The exact identity (19), rather than a leading-order partition approximation, is important here.

---

## 5. Correction to the turn24 operator formulation

Only an inequality on the actual image of $K_c$ is needed.

Let $h$ be analytic on $\{|z|>24\}$, with $h(z)=O(z^{-2})$ at infinity; the actual application is


$$
h=\mathscr W-dR_c,
$$


a zero-mass Cauchy transform. Use the norm on $\Gamma=\{|z|=30\}$.

For $24<|z|<36$, define


$$
T_ch(z)=W_c'(z)h(z)
+\frac1{2\pi i}\oint_{|w|=36}
                 \frac{W_c'(w)h(w)}{z-w}\,dw.
\tag{22}
$$


For $|z|>36$, its exterior continuation is


$$
T_ch(z)=\frac1{2\pi i}\oint_{|w|=36}
                 \frac{W_c'(w)h(w)}{z-w}\,dw.
\tag{23}
$$


The two expressions glue by the Cauchy jump formula. For Cauchy transforms they equal


$$
T_ch(z)=\int\frac{W_c'(u)}{z-u}\,d\nu(u).
$$


In particular, the apparent rational poles of $W_c'(z)$ in (22) are **not** poles of the exterior continuation: formula (23) is analytic for every $|z|>36$.

Set $K_ch=2R_ch-T_ch$. The Gaussian identity is


$$
K_0h=-a\sqrt{z^2-B_0^2}\,h.
$$


The numerical inequalities in turn24 give on $\Gamma$


$$
\|K_0h\|_\Gamma\ge69\|h\|_\Gamma,
\qquad
\|(K_c-K_0)h\|_\Gamma<\|h\|_\Gamma.
$$


Therefore


$$
\boxed{\|h\|_\Gamma\le\frac1{68}\|K_ch\|_\Gamma.}
\tag{24}
$$


No surjectivity claim, Banach-space completion, or general inverse construction is required.

The wall-density argument, wall-flux loop equation, and nonlinear absorption of turn24 can use (24) directly. Their audit status remains the status of the UB input; this clarification does not purport to replace that independent audit.

---

## 6. Real scalar saddles and local Gaussian factors

Retain the exact scalar forces


$$
P_j=\frac{n!}{2\pi}\int_{-\pi}^{\pi}
g(e^{is})^nA_j(\sigma+e^{is})\,ds,
$$




$$
F_j=2n!\int_{-\pi/4}^{\pi/4}
h(e^{is})^nA_j(\sigma-e^{is})\,ds,
\tag{25}
$$


where


$$
g(\zeta)=1+\frac{\sigma}{2}(\zeta+\zeta^{-1}),
\qquad
h(\zeta)=\frac{\sigma}{2}(\zeta+\zeta^{-1})-1.
$$



Define


$$
\Psi_{j,+}(\zeta)=\log g(\zeta)+\frac1n\mathcal H_j(\sigma+\zeta),
$$




$$
\Psi_{j,-}(\zeta)=\log h(\zeta)+\frac1n\mathcal H_j(\sigma-\zeta).
\tag{26}
$$


Their branches are real near $\zeta=1$. By (18),


$$
\Psi_{j,\pm}'(1)=O(d/n),\qquad
\Psi_{j,+}''(1)=2a+O(d/n),\qquad
\Psi_{j,-}''(1)=2\beta+O(d/n),
\tag{27}
$$


where


$$
a=\frac{\sigma}{2M},\qquad \beta=\frac{\sigma M}{2}.
$$


For $d=0$, both stationary points are exactly $1$.

Uniform strict monotonicity of the real derivatives on a fixed neighborhood gives unique real stationary points


$$
r_{j,\pm}=1+O(d/n).
\tag{28}
$$


In particular, they eventually satisfy $|r_{j,\pm}-1|<10^{-3}$, regardless of how slowly $d/n\to0$.

Set


$$
\lambda_{j,\pm}=r_{j,\pm}^{\,2}
                         \Psi_{j,\pm}''(r_{j,\pm}).
$$


Then


$$
\lambda_{j,+}=2a+o(1),\qquad
\lambda_{j,-}=2\beta+o(1),
$$


uniformly in $j$, and hence


$$
\boxed{
\sqrt{\lambda_{j,+}/\lambda_{j,-}}
=M^{-1}(1+o(1)).
}
\tag{29}
$$



The explicit base-phase angular curvature margins in the supplied constant-upgrade source hold for $|\theta|\le1/10$. Equation (18) makes the characteristic correction to that curvature $O(d/n)=o(1)$. Thus both actual phases have uniformly negative angular curvature there.

On $|\theta|\le n^{-2/5}$,


$$
n\Psi(r e^{i\theta})
=n\Psi(r)-\frac{n\lambda\theta^2}{2}
                       +O(n|\theta|^3).
$$


The final error is $O(n^{-1/5})$. The rest of the local arc is suppressed by the uniform curvature. Consequently its integral is


$$
e^{n\Psi(r)}
\sqrt{\frac{2\pi}{n\lambda}}\,(1+o(1)),
\tag{30}
$$


uniformly in all coordinates. Conjugate symmetry makes the leading term real and positive.

---

## 7. Remote scalar contours and both minus connectors

The plus integrand is analytic on the annulus swept out between radii $1$ and $r_{j,+}$, so the entire closed circle can be moved.

The minus contour is open. Its replacement consists of the circular arc at radius $r_{j,-}$ **and both radial connectors** at arguments $\pm\pi/4$.

For radii within $10^{-3}$ of $1$, the supplied explicit quadratic-modulus inequalities give


$$
|g(re^{i\theta})|\le g(r)e^{-1/400},
\quad 1/10\le|\theta|\le\pi,
$$




$$
|h(re^{i\theta})|\le h(r)e^{-1/400},
\quad 1/10\le|\theta|\le\pi/4.
\tag{31}
$$


On every such contour, $|q|<3$, so


$$
|A_j(q)|\le C B_jZ_d(0)4^d.
\tag{32}
$$


Here the full absolute base partition is at most twice its principal partition by (7).

At either real saddle, (14) gives


$$
|A_j(q_s)|\ge C^{-1}B_jZ_d(0)\,0.58^d.
\tag{33}
$$


Combining (30)–(33), the remote/local ratio is bounded by


$$
C\sqrt n\exp\!\left[-n/400+d\log(4/0.58)\right]
=\exp(-\eta' n+O(d)).
\tag{34}
$$


This tends to zero exponentially for every $d=o(n)$.

### The connectors

At both original minus endpoints,


$$
h(e^{\pm i\pi/4})=0.
$$


On a radial connector,


$$
h(re^{\pm i\pi/4})
=\frac{r+r^{-1}}2-1
 \ \pm i\,\frac{r-r^{-1}}2.
\tag{35}
$$


Thus $|h|\le C|r-1|$; eventually the coarse bound $|h|\le0.002$ holds on each connector. Their lengths are $O(|r_{j,-}-1|)$, and $1/|\zeta|$ is uniformly bounded. Since $h(r_{j,-})>0.4$, each connector/local ratio is at most


$$
C\sqrt n\,e^{Cd}(0.002/0.4)^n.
\tag{36}
$$


Both connectors are therefore exponentially negligible. There is no missing endpoint term of the target order.

We have now proved the full scalar formulas


$$
P_j=\frac{n!}{2\pi}s_jB_jZ_d(0)
 e^{n\Psi_{j,+}(r_{j,+})}
 \sqrt{\frac{2\pi}{n\lambda_{j,+}}}(1+o(1)),
$$




$$
F_j=2n!s_jB_jZ_d(0)
 e^{n\Psi_{j,-}(r_{j,-})}
 \sqrt{\frac{2\pi}{n\lambda_{j,-}}}(1+o(1)).
\tag{37}
$$


In particular,


$$
\operatorname{sign}P_j=\operatorname{sign}F_j=s_j,
\qquad P_jF_j\ne0.
\tag{38}
$$



These conclusions did not use UB.

---

## 8. Stationary values: exactly where UB enters

For $d\to\infty$, UB compares actual and equilibrium characteristic increments over every real interval of length $O(c)$, $c=d/n$:


$$
\begin{aligned}
&\log\frac{s_jA_j(\sigma\pm r)}
                  {s_jA_j(\sigma\pm1)}\\
&\hspace{12mm}
-d\bigl[L_c(\sigma\pm r)-L_c(\sigma\pm1)\bigr]
=O(c)=o(1).
\end{aligned}
\tag{39}
$$


The sign in the minus chain derivative is included in this integral identity.

Both actual and equilibrium radial stationary points lie in a common $O(c)$ neighborhood of $1$ and have positive radial curvature. Uniform comparison of the anchored functions therefore compares their minimum values with the same $o(1)$ error.

Reuse the established exact equilibrium stationary identity, with


$$
r_+(c)=\frac2{2+c},\qquad
r_-(c)=\frac{2M}{2M-c},
$$




$$
\Phi_+(r_+(c))-\Phi_-(r_-(c))=(2+c)\log M.
$$


Combining it with (20)–(21) and (39) gives


$$
n\Psi_{j,-}(r_{j,-})-n\Psi_{j,+}(r_{j,+})
=-(2n+d)\log M+o(1).
\tag{40}
$$


Thus (29) and (37) yield


$$
\boxed{
F_j/P_j=4\pi M^{-2n-b}(1+o(1)).
}
\tag{41}
$$


The factor $4\pi$ is the exact scalar normalization ratio; the additional $M^{-1}$ is the Gaussian curvature ratio, and $b=d+1$.

### Explicit join with bounded and slow $d$

Use the established relative regime for


$$
b\le n^{1/8},
$$


which lies uniformly inside $b=o(n^{1/4})$. Its displayed error bound tends to zero uniformly on this smaller range. The same fixed-dimensional localization proof covers $b=1,2$: empty products are interpreted as $1$, and the only forcing variable has the ordinary one-dimensional Gaussian saddle. It gives the same constants $4\pi M^{-2n-b}$.

On the complementary range $b>n^{1/8}$, $d\to\infty$, so UB applies. This explicit split covers sequences that oscillate between bounded, slowly growing, and larger sublinear dimensions. No assumption $d\to\infty$ is imposed on the final domain (1).

---

## 9. Scalar lower bound, complete $eE$, and the same-weight adjacent norm

At the plus saddle, $g(r)\ge M$, and eventually $q_s=\sigma+r>2$. Hence every characteristic modulus is at least $q_s-1>1$. Equations (14) and (37) give the uniform lower bound


$$
\boxed{
|P_j|\ge C^{-1}n!n^{-1/2}M^nB_jZ_d(0).
}
\tag{42}
$$


A weaker $e^{-Cd}$ factor would suffice, but is unnecessary here.

Keep the **complete** exponential force


$$
eE_i=-[z^{n+i}](1-z+z^2/2)^n
                        \int_0^1s^ne^{1-s+sz}\,ds.
\tag{43}
$$


The already verified Cauchy estimate is


$$
\sigma^i|eE_i|\le e^\sigma M^n/(n+1).
\tag{44}
$$


Thus, for the full insertion,


$$
E_j=\nu_{n,d}\left(
R_j\sum_{i=0}^d\sigma^ie_{d-i}(z^{-1})eE_i\right),
$$




$$
|E_j|\le CB_jZ_d(0)\frac{2^dM^n}{n+1}.
$$


Using (42),


$$
\boxed{|E_j/P_j|\le C\,2^d/(n!\sqrt n).}
\tag{45}
$$



For the endpoint, the exact same-weight factorization is


$$
Z_{d+1}(0)/Z_d(0)=h_d(0).
$$


The monic trial polynomial $z^d$, with the original measure $dt/(2\pi)$, gives


$$
h_d(0)\le e^\sigma M^n.
$$


Since $D\le2Z_b(0)$, (42) yields


$$
\boxed{
|D/P_0|\le C\sqrt n/(n!B_0),
\qquad B_0=(n)_d\sigma^{-d}\ge1
}
\tag{46}
$$


eventually; $B_0=1$ when $d=0$.

Both (45) and (46) are $o(M^{-2n-b})$ uniformly whenever $b=o(n)$. This establishes the requested scalar lower-bound interface without borrowing a fixed-positive-ratio asymptotic.

---

## 10. Fully scoped whole-error theorem

**Conditional theorem, with only UB retained as an unaudited analytic input.**  
Assume the uniform bias conclusion UB of turns23–24. For every integer allocation (1), eventually:

* the original contact matrix is normal and $D>0$;
* every actual reconstructed coordinate $u_j$ is nonzero;
* for all $0\le j\le b$,
  

$$
\frac{v_j}{u_j}-S
  =(-1)^{n+1}4\pi M^{-2n-b}(1+o(1)),
  \tag{47}
$$


  uniformly in $j$;
* the same formula holds for every positive diagonal metric in these actual coordinates, even when its entries vary arbitrarily with $n,b$.

Indeed, the exact original columns are


$$
u_j=(-1)^nP_j/D,\qquad
v_j-Su_j=\delta_{j0}+(-1)^nE_j/D-F_j/D.
$$


Their whole real error is exactly


$$
\boxed{
\frac{v_j}{u_j}-S
=\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac D{P_j}.
}
\tag{48}
$$


Equations (41), (45), and (46) prove (47), including its eventual sign and nonvanishing.

For the actual positive diagonal metric $W$,


$$
c_W=\frac{u^TWv}{u^TWu},\qquad
c_W-S=\sum_j
\frac{W_{jj}u_j^2}{\sum_\ell W_{\ell\ell}u_\ell^2}
                 \left(\frac{v_j}{u_j}-S\right).
$$


Uniformity and positive convex weighting give


$$
\boxed{
c_W-S=(-1)^{n+1}4\pi M^{-2n-b}(1+o(1))\ne0.
}
\tag{49}
$$


No nondiagonal-metric assertion is made.

All interfaces other than UB have been discharged above or explicitly joined to an established relative regime. In particular, no remote contour, signed sector, anchor normalization, or minus connector remains hidden in the conditional statement.

---

## 11. Primitive multiplier, final gcd, and actual denominator

For a rational positive diagonal metric, retain the least positive actual two-column clearer $d_B$ and an integral positive diagonal scaling $\Omega$ of that metric:


$$
N_B=d_B[u,v],\quad
A_B=N_{B,1}^T\Omega N_{B,1}>0,\quad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


Set


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_B=A_B/g_B>0,\qquad p_B=H_B/g_B.
\tag{50}
$$


The actual reduced denominator is $q_B$, and the primitive multiplier relative to the uncleared quadratic form is exactly $d_B^2/g_B$.

Under UB, the whole evaluated primitive form is


$$
\begin{aligned}
q_BS-p_B
&=\frac{d_B^2}{g_B}
 \bigl[(u^T\Omega u)S-u^T\Omega v\bigr]\\
&=q_B(S-c_W)\\
&=\boxed{(-1)^n4\pi q_BM^{-2n-b}(1+o(1))\ne0.}
\end{aligned}
\tag{51}
$$


No estimate for $q_B$ after this final gcd has been proved.

## Closing ledger

1. **New result and proof status.**  
   The all-sublinear signed-sector, derivative, normality, actual zero-free logarithm, reciprocal-anchor, real-saddle, Gaussian-prefactor, remote-contour, both-connector, scalar-lower-bound, complete-$eE$, and adjacent-same-weight-norm interfaces are closed above. The turn24 operator argument needs only the coercive inequality (24) on its actual image; its exterior continuation is given by (23), with no rational poles. The complete relative theorem (49) is conditional solely on the turn23–24 uniform bias input currently under audit—not on unnamed scalar interfaces.

2. **Exact remaining bottleneck.**  
   Analytically, independent validation of UB remains the expressly identified dependency. Even after it passes, irrationality of $e+\pi$ remains unresolved: a sufficient missing arithmetic statement is an infinite same-index sequence with
   

$$
q_BM^{-2n-b}\longrightarrow0,
$$


   where $q_B$ is the actual reduced denominator **after the final gcd**. None of the analytic estimates bounds that quantity.

3. **Computation request.**  
   None. The remaining bias audit and primitive-denominator assertion are infinite analytic/arithmetic obligations; finite evaluations would not settle them.
