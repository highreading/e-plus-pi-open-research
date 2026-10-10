> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Mesoscopic whole-error theorem for the actual centers

Put


$$
\sigma=\sqrt2,\qquad M=1+\sqrt2,\qquad S=e+\pi.
$$



The supplied uniform zero-free interface suffices to complete the mesoscopic analytic step. No limiting equilibrium measure at $c=0$ is needed. The essential replacement is a uniform, anchored holomorphic-log estimate for the **actual** characteristic expectations, followed by recentering at their finite-$n$ saddles.

## 1. Statement and index scope

**Theorem.** Let $n\to\infty$ through positive integers, and let $b=b(n)$ be integers satisfying


$$
3\le b,\qquad b\log n=o(n).
\tag{1.1}
$$


Use the exact actual reconstruction, contact matrix, forcing integrals, and original $B$-coefficient coordinates from the supplied Selberg interface. For every positive diagonal metric


$$
W_n=\operatorname{diag}(w_{0,n},\ldots,w_{b,n}),\qquad w_{j,n}>0,
$$


allowing arbitrary dependence on $n$, the following hold eventually:

1. The actual contact matrix is nonsingular.
2. Every actual reconstructed first-column coordinate $u_j$, $0\le j\le b$, is nonzero.
3. Every coordinate center $c_j=v_j/u_j$, and the actual metric center $c_W$, satisfies
   

$$
\operatorname{sign}(c_j-S)
   =\operatorname{sign}(c_W-S)=(-1)^{n+1}.
   \tag{1.2}
$$


4. Uniformly across all coordinates and all these positive diagonal metrics,
   

$$
\log|c_j-S|=-2n\log M+O(b+\log n),
   \tag{1.3}
$$


   

$$
\log|c_W-S|=-2n\log M+O(b+\log n).
   \tag{1.4}
$$



In particular, the errors are nonzero and


$$
\frac1n\log|c_W-S|\longrightarrow-2\log(1+\sqrt2).
\tag{1.5}
$$



The proof below uses the supplied **uniform** zero-free and normality theorem on $3\le b\le n/1000$, not the fixed-positive-proportion center theorem. Condition (1.1) is an explicit sufficient condition; no assertion about a larger mesoscopic domain is needed here.

For the CRT allocation


$$
b=9^r,\qquad n=2h,\qquad h=b^3+O(b^2),\qquad r\to\infty,
\tag{1.6}
$$


condition (1.1) holds. Consequently its actual centers have, eventually,


$$
c_W-S<0,\qquad
\log|c_W-S|=-2n\log M+O(b+\log n).
\tag{1.7}
$$



The analytic theorem does not depend on the CRT congruences or their arithmetic audit.

---

## 2. Uniform anchored logarithms of the actual expectations

Retain


$$
d=b-1,\qquad
A_j(q)=\nu_{n,d}\left(R_j\prod_{\ell=1}^d(z_\ell^{-1}+q)\right),
$$


with the complete reconstruction insertion $R_j$, its reference scale $B_j>0$, and its specified sign $s_j$.

The supplied upgraded interface gives


$$
\frac12 B_jZ_d(q)\le |A_j(q)|\le2B_jZ_d(q),
\tag{2.1}
$$


uniformly in every coordinate, on


$$
|q|\le\frac34
\quad\text{or}\quad
2\le |q|\le3.
$$


It also gives


$$
s_jA_j(q)>0
\tag{2.2}
$$


at positive real $q$ in those regions.

Consider the disks


$$
\mathcal D_+=\{|q-M|<1/5\},\qquad
\mathcal D_-=\{|q-M^{-1}|<1/5\}.
\tag{2.3}
$$


Their closures lie in the respective zero-free regions. On both disks every characteristic factor satisfies fixed bounds


$$
0<a_0\le |z^{-1}+q|\le a_1<\infty,\qquad |z|=1,
\tag{2.4}
$$


where the constants are independent of $n,b,j$. Hence, directly from the positive partition definition,


$$
a_0^dZ_d(0)\le Z_d(q)\le a_1^dZ_d(0).
\tag{2.5}
$$



Define the actual holomorphic logarithms


$$
T_{j,\pm}(q)
=\Log\frac{A_j(q)}{s_jB_jZ_d(0)}
\quad(q\in\mathcal D_\pm),
\tag{2.6}
$$


anchored to be real at $q=M$ or $q=M^{-1}$, respectively. Existence follows from zero-freeness and simple connectedness; (2.2) makes the specified real anchor possible.

Equations (2.1) and (2.5) give


$$
|\Re T_{j,\pm}(q)|\le Cb.
\tag{2.7}
$$


This alone is not a phase estimate. To obtain one, let $u=\Re T_{j,\pm}$. Interior harmonic estimates on a smaller concentric disk give


$$
|\nabla u|\le C'b.
$$


The Cauchy–Riemann equations give the same bound for the gradient of $\Im T_{j,\pm}$. Integrating from the real anchor, where its imaginary part is zero, yields


$$
|T_{j,\pm}(q)|\le C''b
$$


on that smaller disk. Cauchy estimates, with another fixed interior margin, then give, for every fixed $k$,


$$
\sup_j\sup_{q\in\mathcal D_\pm'}
|T_{j,\pm}^{(k)}(q)|\le C_kb.
\tag{2.8}
$$


Here one may take a fixed disk $\mathcal D_\pm'$ of radius $0.17$, and use still smaller compact sets for derivative estimates.

Thus


$$
H_{j,\pm}:=\frac{T_{j,\pm}}n
$$


satisfies


$$
\|H_{j,\pm}\|_{C^k}=O(b/n)=o(1)
\tag{2.9}
$$


uniformly in **every actual coordinate**.

This establishes the necessary phase control for the original complex expectation, without replacing it by a modulus integral.

---

## 3. Actual finite-$n$ saddles

Write


$$
g(\zeta)=1+\frac{\sigma}{2}(\zeta+\zeta^{-1}),
\qquad
h(\zeta)=\frac{\sigma}{2}(\zeta+\zeta^{-1})-1.
$$


Near $\zeta=1$, define


$$
\Psi_{j,+}(\zeta)=\log g(\zeta)+H_{j,+}(\sigma+\zeta),
$$




$$
\Psi_{j,-}(\zeta)=\log h(\zeta)+H_{j,-}(\sigma-\zeta).
\tag{3.1}
$$


All branches are real on the relevant positive real interval.

The unperturbed phases have stationary point $1$, with


$$
(\log g)''(1)=\frac{\sigma}{M}>0,\qquad
(\log h)''(1)=\frac{\sigma}{\sigma-1}>0.
\tag{3.2}
$$


By (2.9), their perturbations have real stationary points $r_{j,\pm}$ satisfying, uniformly in $j$,


$$
r_{j,\pm}=1+O(b/n).
\tag{3.3}
$$


For completeness, on a fixed small real interval about one the derivative of each phase is strictly increasing, its derivative at one is $O(b/n)$, and its second derivative is bounded below by a positive constant. Evaluating the first derivative at $1\pm Cb/n$, with sufficiently large fixed $C$, gives opposite signs and hence the asserted unique nearby zero.

Define


$$
\lambda_{j,\pm}=r_{j,\pm}^2\Psi_{j,\pm}''(r_{j,\pm}).
$$


There are absolute constants $0<c<C$ such that


$$
c\le\lambda_{j,\pm}\le C.
\tag{3.4}
$$



The characteristic value has **not** been discarded. In particular, the exponent at the recentered saddle satisfies


$$
n\Psi_{j,+}(r_{j,+})
=n\log M+T_{j,+}(M)+O(b^2/n),
\tag{3.5}
$$




$$
n\Psi_{j,-}(r_{j,-})
=-n\log M+T_{j,-}(M^{-1})+O(b^2/n).
\tag{3.6}
$$


Indeed, the unperturbed first derivative vanishes at one, so its displacement costs $O(n(r-1)^2)$; the logarithmic characteristic changes by $O(b|r-1|)$. Both are $O(b^2/n)$.

On the specified CRT family,


$$
b^2/n=O(1/b).
\tag{3.7}
$$


Equations (3.5)–(3.6) are the useful local displacement estimate. They do not assert a corresponding approximation obtained by deleting $T_{j,\pm}$.

---

## 4. Local signed integrals and remote contours

On the circular arcs $\zeta=r_{j,\pm}e^{i\theta}$, stationarity gives


$$
\Psi_{j,\pm}(r_{j,\pm}e^{i\theta})
=
\Psi_{j,\pm}(r_{j,\pm})
-\frac{\lambda_{j,\pm}}2\theta^2+O(\theta^3),
\tag{4.1}
$$


uniformly in $j$. The supplied scalar curvature bounds, together with (2.9), give uniform strictly negative angular curvature for $|\theta|\le1/10$.

On $|\theta|\le n^{-2/5}$, the cubic term in the exponent is $O(n^{-1/5})$. The remainder of the local arc is Gaussian-suppressed. Conjugate symmetry makes the leading contribution real and positive. Thus the local integral is


$$
e^{n\Psi_{j,\pm}(r_{j,\pm})}
\sqrt{\frac{2\pi}{n\lambda_{j,\pm}}}
\bigl(1+O(n^{-1/5})\bigr),
\tag{4.2}
$$


uniformly in $j$.

The plus circle is deformed to radius $r_{j,+}$. The minus arc is deformed to radius $r_{j,-}$, **with both radial endpoint connectors retained**. Integer powers and the polynomial $A_j$ make these deformations legitimate on annuli avoiding zero.

Eventually $|r_{j,\pm}-1|<1/1000$. The supplied remote scalar bounds therefore apply:


$$
|g(re^{i\theta})|\le g(r)e^{-1/400},
\quad 1/10\le|\theta|\le\pi,
$$




$$
|h(re^{i\theta})|\le h(r)e^{-1/400},
\quad 1/10\le|\theta|\le\pi/4.
\tag{4.3}
$$


The full absolute-base bound and the complete insertion bound give


$$
|A_j(q)|\le C B_jZ_d(0)4^d
\tag{4.4}
$$


on all these contours. At either real saddle, (2.1) supplies a lower bound


$$
|A_j(q_s)|\ge cB_jZ_d(0)a^d
\tag{4.5}
$$


with fixed $a>0$.

Consequently the remote/main ratio is bounded by


$$
C\sqrt n\,\exp\{-n/400+Cb\}=o(1).
\tag{4.6}
$$


This controls all plus-circle sectors, including their parity signs.

At the original minus endpoints, $h(e^{\pm i\pi/4})=0$. On the short radial connectors, the supplied bounds give $|h|\le0.002$, whereas $h(r)\ge\sigma-1>0.4$. Equations (4.4)–(4.5) therefore make the complete connector contributions exponentially negligible as well.

It follows that the **full actual** forcing integrals satisfy


$$
P_j=
\frac{n!}{2\pi}s_jB_jZ_d(0)
e^{n\Psi_{j,+}(r_{j,+})}
\sqrt{\frac{2\pi}{n\lambda_{j,+}}}(1+o(1)),
\tag{4.7}
$$




$$
F_j=
2n!s_jB_jZ_d(0)
e^{n\Psi_{j,-}(r_{j,-})}
\sqrt{\frac{2\pi}{n\lambda_{j,-}}}(1+o(1)),
\tag{4.8}
$$


uniformly across $0\le j\le b$.

In particular,


$$
\operatorname{sign}P_j=\operatorname{sign}F_j=s_j,
\qquad F_j/P_j>0.
\tag{4.9}
$$


Using (2.8) and (3.5)–(3.6),


$$
\log(F_j/P_j)=-2n\log M+O(b+1)
\tag{4.10}
$$


uniformly in $j$. These are upper **and** lower estimates for the actual signed integrals.

---

## 5. Complete exponential residual and coordinate-zero endpoint

The exact coordinate identity is


$$
c_j-S=
\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j,0}\frac{D}{P_j}.
\tag{5.1}
$$



The supplied bound is for the **whole exponential residual**:


$$
|eE_i|\le \frac{27M^n\sigma^{-i}}{n+1}.
$$


Inserted into its complete elementary-symmetric sum, it gives


$$
|E_j|\le
C B_jZ_d(0)\frac{M^n2^d}{n+1}.
\tag{5.2}
$$


No first-omitted-term substitution is being made.

Equations (3.5) and (4.7) imply


$$
|P_j|\ge
c\,n!B_jZ_d(0)n^{-1/2}M^n e^{-Cb}.
\tag{5.3}
$$


Therefore


$$
\left|\frac{E_j}{P_j}\right|
\le\frac{e^{Cb}}{n!\sqrt n}
=\exp\{-n\log n+O(n+b)\}.
\tag{5.4}
$$



For the endpoint, retain


$$
0<D\le2Z_b(0),\qquad
\frac{Z_b(0)}{Z_d(0)}=h_d\le e^\sigma M^n.
$$


The exact reference $B_0$ is greater than one eventually. Thus


$$
\left|\frac{D}{P_0}\right|
\le \frac{C\sqrt n\,e^{Cb}}{n!B_0}
=\exp\{-n\log n+O(n+b)\}.
\tag{5.5}
$$


All other endpoint coordinates are exactly zero.

Comparing (5.4)–(5.5) with the uniform lower estimate in (4.10) shows that both corrections are $o(F_j/P_j)$. Hence (5.1) has sign $(-1)^{n+1}$, is nonzero, and satisfies (1.3).

Normality follows on this index scope from the supplied uniform theorem, which gives $D>0$ eventually on both parities. Equation


$$
u_j=(-1)^nP_j/D
$$


and (4.7) then prove every required coordinate nonvanishing.

---

## 6. The actual coordinate metric and whole center

The exact Gram identity is


$$
c_W-S=
\sum_{j=0}^b
\frac{w_{j,n}u_j^2}{\sum_{\ell=0}^b w_{\ell,n}u_\ell^2}
(c_j-S).
\tag{6.1}
$$


Its weights are positive and sum to one. Every summand error has the same eventual sign, and their magnitudes have uniform upper and lower bounds from (1.3). Their convex average therefore has that same sign and those same bounds.

This proves (1.2)–(1.5), regardless of how rapidly the positive metric weights vary. It concerns precisely diagonal metrics in the supplied **actual $B$-coefficient coordinates**; it makes no claim about unrelated constructions or changes of coordinate metric.

---

## 7. Conditional arithmetic exclusion on the CRT centers

For the specified rational metric, retain the least actual two-column denominator $d_B$, the integral lift $N_B=d_B[u,v]$, and


$$
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B>0.
\tag{7.1}
$$


Thus $q_n$ is the **actual primitive center denominator**, after the final metric-dependent gcd.

On the CRT sequence the analytic result proved above gives


$$
\epsilon_n=\frac{p_n}{q_n}-S<0
\quad\text{eventually},
\qquad
\log|\epsilon_n|=-2n\log M+o(n).
\tag{7.2}
$$


The complete primitive evaluated form is therefore


$$
L_n=q_nS-p_n=-q_n\epsilon_n>0,
\qquad
\log L_n=\log q_n-2n\log M+o(n).
\tag{7.3}
$$



**Conditional corollary.** If A5’s independent audit establishes, on these same centers after the final gcd,


$$
v_2(q_n)=\frac32n-o(n),
\qquad
v_3(q_n)\ge n-o(n),
\tag{7.4}
$$


then


$$
\liminf\frac1n\log L_n
\ge \frac32\log2+\log3-2\log M>0.
\tag{7.5}
$$


The strict inequality can be verified without numerical approximations:


$$
3\cdot2^{3/2}>M^2
\iff 6\sqrt2>3+2\sqrt2
\iff4\sqrt2>3.
$$



Thus those primitive center forms would grow exponentially rather than shrink. This excludes the specified CRT center-form route from producing shrinking primitive errors. It neither decides the rationality of $e+\pi$ nor excludes other centers, metrics, or endpoint directions.

The finite control at $(n,b)=(4482,9)$ is not used to prove either the analytic theorem or the infinite arithmetic hypothesis.

---

## Concluding ledger

### (1) New result and proof status

**Proved from the supplied uniform zero-free, contour, reconstruction, and full-residual inputs:** the whole actual signed-error theorem on $b\log n=o(n)$, including $n\sim2b^3$, every actual coordinate, both parities, contact normality, nonvanishing, and every positive diagonal actual-coordinate metric.

The new anchored-log argument controls the actual complex phase uniformly in $j$. Finite-$n$ recentering retains the characteristic contribution and gives an $O(b^2/n)$ saddle-displacement correction.

### (2) Exact remaining bottleneck

For the CRT exclusion corollary, the remaining dependency is A5’s independent proof of the simultaneous two-prime lower bound for the **actual primitive denominator after the final gcd**, particularly its mesoscopic $3$-adic law. The matching analytic error theorem is now supplied.

The irrationality or rationality of $e+\pi$ remains unresolved.

### (3) Computation request

None. This analytic proof requires no additional finite sampling or exact computation.
