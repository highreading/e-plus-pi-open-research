> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 Turn 2 — Independent audit of the inverse ensemble, correlated trace comparison, and rectangular source bridge

## Executive conclusion

The global question remains unresolved: **this report proves neither rationality nor irrationality of $e+\pi$**.

The new inverse-ensemble argument and the sharper square correlated-trace estimate survive audit. They apply to the **same complete compact determinants**, with the same finite boundaries and the same actual primitive normalization. In particular, if


$$
R_k=\frac{J_k(\nu)}{J_{k-1}((1+x)^2\nu)},\qquad
\eta_k=\frac{2}{3k-1},\qquad
\tau_k=\frac83\,4^{-k},
$$


then


$$
\boxed{
\frac{1-\eta_k-\tau_k}{1+\tau_k}
\le
\frac{e+\pi-p_k/q_k}{R_k}
\le
\frac{1+\tau_k}{1-\tau_k}
\qquad(k\ge64).
}
\tag{0.1}
$$


The full overlap and negative-atom contributions have been restored before this ratio is formed. Formula (0.1) is not a bound on the actual primitive denominator $q_k$.

The rectangular source lemma needs a qualification:

* Its inverse-moment statement is valid for every $m,n\ge1$.
* Its numerator exterior bounds are valid for every $m,n\ge1$.
* Its stated proof of the slope lower bound requires $n\ge2$. At $n=1$, the proposed extension across the cutoff is invalid; a universally valid replacement is given below.
* The exact full-source cancellation is valid when $m\ge n$.
* When $m<n$, an extra source term cannot be discarded.

The principal new result of this report evaluates that last obstruction in the nearest unequal case. Let


$$
B_k(s)=
\det\left[
(c_{r+j})_{\substack{0\le r\le2k-2\\0\le j<k}}
\ \middle|\
(r_{r+j}+s(-1)^{r+j})_{\substack{0\le r\le2k-2\\0\le j<k-1}}
\right].
\tag{0.2}
$$


Then


$$
\boxed{B_k(e+\pi)>0\qquad(k\ge64).}
\tag{0.3}
$$


Moreover, $B_k$ is the unscaled physical last-row, last-right-column minor of the original square matrix:


$$
\boxed{
\operatorname{cof}_{2k-1,\,2k-1}\mathcal M_k(s)
=\Lambda_k^{\,k-1}B_k(s).
}
\tag{0.4}
$$



For the short-contact rectangle with $k-1$ contact columns and $k$ right columns, the exact missing source contribution is


$$
\boxed{
T_{k-1,k}(e+\pi)-\mathscr D_{k-1,k}
=(-1)^k e\,B_k(e+\pi)\ne0.
}
\tag{0.5}
$$


Here $\mathscr D_{k-1,k}$ is the pure $L/\nu$ mixed determinant defined below. Thus the naïve short-contact source bridge is not merely unproved: **it is false for every $k\ge64$ in this nearest unequal case**. In particular, at every original index


$$
K_u=9^{18+32u},
$$


which is odd, the omitted contribution is strictly negative.

This is a source-identity obstruction, not an irrationality result. No arithmetic normalization of the original pair is changed.

---

## 1. Original objects, boundaries, and closed results reused

### 1.1 The complete compact determinant

Retain


$$
a_0=1,\qquad a_d=1-da_{d-1},
$$




$$
c_n=a_{2n}-(-1)^n,
$$




$$
\rho_0=0,\qquad \rho_{n+1}+\rho_n=\frac1{2n+1},
$$




$$
r_n=-(2n)!+4\rho_n.
\tag{1.1}
$$



For


$$
0\le m<2k,\qquad 0\le j<k,
$$


put


$$
C_{mj}=c_{m+j},\qquad
\mathcal R_{mj}=r_{m+j},\qquad
w_m=(-1)^m,\qquad v_j=(-1)^j,
$$


and


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5).
$$


The original integer affine polynomial is


$$
H_k(s)=
\det[C\mid \Lambda_k\mathcal R+s\Lambda_kwv^T]
=H_{0,k}+H_{1,k}s.
\tag{1.2}
$$



The exact boundaries remain


$$
m+j\le3k-2,\qquad
(6k-4)!\ \text{as the maximum factorial},\qquad
6k-5\ \text{as the last odd denominator}.
\tag{1.3}
$$



Let


$$
s_0=e+\pi,\qquad
G_k=\gcd(|H_{0,k}|,|H_{1,k}|).
$$


The actual primitive pair is


$$
q_k=\frac{|H_{1,k}|}{G_k},\qquad
p_k=-\frac{\operatorname{sgn}(H_{1,k})H_{0,k}}{G_k}.
\tag{1.4}
$$


On the accepted sign domain, in particular for $k\ge64$,


$$
\varepsilon_k=s_0-\frac{p_k}{q_k}
=\frac{|H_k(s_0)|}{|H_{1,k}|}>0,
$$


whereas the whole primitive error is


$$
\boxed{
\ell_k=q_k\varepsilon_k
=\frac{|H_k(s_0)|}{G_k}>0.
}
\tag{1.5}
$$


The cancellation of $G_k$ from $\varepsilon_k$ does not cancel it from $\ell_k$.

### 1.2 The exact measures and source identity

Use


$$
d\mu(x)=
\frac{e^{-1}}{2\sqrt x}
\left(e^{-\sqrt x}+\mathbf1_{(0,1)}(x)e^{\sqrt x}\right)\,dx,
\qquad
L=\mu-\delta_{-1},
\tag{1.6}
$$


and


$$
d\nu(x)=
\frac{e^{\sqrt x}+4/(1+x)}{2\sqrt x}
\mathbf1_{(0,1)}(x)\,dx.
\tag{1.7}
$$



For clarity, the moment identities can be checked directly. If


$$
I_d=\int_0^1t^de^t\,dt,
$$


then integration by parts gives


$$
I_d=e\,a_d+(-1)^{d+1}d!.
$$


Also,


$$
\int_0^1\frac{t^{2n}}{1+t^2}\,dt
=(-1)^n\frac{\pi}{4}+\rho_n.
$$


Consequently


$$
\mu_n=a_{2n},\qquad L_n=c_n,
$$


and


$$
\boxed{\nu_n=e\,c_n+r_n+s_0(-1)^n.}
\tag{1.8}
$$



Thus neither the factorial endpoint nor the arctangent correction can be omitted.

Under $x=t^2$, the exterior measure is exactly


$$
d\mu_{\mathrm{ext}}(x)=e^{-1}e^{-t}\,dt,\qquad t>1.
\tag{1.9}
$$


It is not normalized to mass one. Its mass is $e^{-2}$, while


$$
\mu([0,1])=1-e^{-2}.
\tag{1.10}
$$



For a positive measure $m$, write


$$
J_n(m)=\det\left(\int x^{a+b}\,dm(x)\right)_{a,b<n},
\qquad J_0(m)=1,
$$


and let


$$
d\nu_+(x)=(1+x)^2\,d\nu(x).
$$



### 1.3 Closed analytic results are not reopened

The preceding A4 audit already established the same-$H$ comparison, ordinary-error rate, and contraction. They are reused, not re-proved here:


$$
0<\varepsilon_{k+1}\le\frac14\varepsilon_k
\qquad(k\ge64),
\tag{1.11}
$$


and, with


$$
A=17+12\sqrt2,
$$




$$
\frac{3}{2k^2A^{k-1}}\le R_k\le\frac{28}{A^{k-1}},
\qquad
R_k=\frac{J_k(\nu)}{J_{k-1}(\nu_+)}.
\tag{1.12}
$$



Also reused are the complete signed conditioning bounds. If $D_k,S_k$ are the original normalized full numerator and slope, and $E_D,E_S$ their exterior-only parts, then


$$
(-1)^kH_k(s_0)=\Lambda_k^kJ_k(\nu)D_k,
$$




$$
(-1)^kH_{1,k}=\Lambda_k^kJ_{k-1}(\nu_+)S_k,
\tag{1.13}
$$


and


$$
|D_k-E_D|\le e^{-k}Z_kd_k,\qquad
|S_k-E_S|\le e^{-k}Z_kd_k^+,
\tag{1.14}
$$


where


$$
Z_k=\det((2k+2a+2b)!)_{a,b<k},
\qquad
d_k,d_k^+\le2\,4^{-k}\quad(k\ge64).
\tag{1.15}
$$


The first error bound includes the entire overlap and the entire negative-atom contribution.

---

## 2. Direct audit of the original $V(t^2)^2$ inverse ensemble

The following statement includes A5’s square lemma and the rectangular reference generalization.

### Theorem 2.1 — Original-density inverse-moment estimate

Let $m,n\ge1$, and define


$$
Z_{m,n}=\det((2n+2a+2b)!)_{a,b<m}.
$$


On $(0,\infty)^m$, use the probability density


$$
\frac{1}{m!Z_{m,n}}
V(t_1^2,\ldots,t_m^2)^2
\prod_{i=1}^m t_i^{2n}e^{-t_i}.
\tag{2.1}
$$


Then


$$
\boxed{
\mathbb E\sum_{i=1}^m t_i^{-2}
\le a_{m,n}:=\frac{m}{2n(2n-1)}.
}
\tag{2.2}
$$


For every $u\ge0$,


$$
\boxed{
\mathbb E\prod_{i=1}^m(1+u t_i^{-2})
\le e^{u a_{m,n}}.
}
\tag{2.3}
$$



The density in (2.1) is $V(t^2)^2$, not a $V(t)V(t^\theta)$ density. No formula for the latter is used.

### 2.1 Normalization

Andréief’s identity applied to the functions $1,t^2,\ldots,t^{2m-2}$ gives


$$
\int V(t^2)^2\prod_i t_i^{2n}e^{-t_i}\,dt_i
=
m!\det\left(\int_0^\infty t^{2n+2a+2b}e^{-t}\,dt\right)_{a,b<m}.
$$


The moment integral is $(2n+2a+2b)!$, proving the normalization $m!Z_{m,n}$.

The Gram matrix is positive definite because a nonzero polynomial in $t^2$ cannot vanish almost everywhere on $(0,\infty)$.

### 2.2 Boundary justification for both integrations by parts

Write the unnormalized density as $P(t)$.

At $t_i=0$, with the other coordinates fixed,


$$
P(t)=O(t_i^{2n}),\qquad
\frac{P(t)}{t_i}=O(t_i^{2n-1}).
$$


Both vanish since $n\ge1$. The derivatives that occur have locally integrable powers, including $t_i^{2n-2}$.

At infinity, all factors other than $e^{-t_i}$ are polynomial, so the boundary terms vanish and the derivatives are absolutely integrable.

Collisions are not boundaries of the full orthant. After multiplication by $P$, the apparent collision poles in the logarithmic derivative cancel against factors of the squared Vandermonde. Equivalently, on ordered chambers the density vanishes quadratically at a collision. Thus no collision contribution is omitted. These observations justify ordinary integration by parts, or its cutoff version followed by dominated convergence.

### 2.3 First summed integration by parts

Away from collisions,


$$
\partial_{t_i}\log P
=
\frac{2n}{t_i}-1+
4t_i\sum_{j\ne i}\frac1{t_i^2-t_j^2}.
$$


Summing $\int\partial_{t_i}P=0$, and pairing $i,j$, uses


$$
\frac{t_i}{t_i^2-t_j^2}
+\frac{t_j}{t_j^2-t_i^2}
=\frac1{t_i+t_j}.
$$


Therefore


$$
2n\,\mathbb E\sum_i\frac1{t_i}
-m
+4\,\mathbb E\sum_{i<j}\frac1{t_i+t_j}=0.
\tag{2.4}
$$


The last term is nonnegative, so


$$
\mathbb E\sum_i t_i^{-1}\le\frac{m}{2n}.
\tag{2.5}
$$



### 2.4 Second summed integration by parts

Now


$$
\partial_{t_i}(P/t_i)
=
P\left[
\frac{2n-1}{t_i^2}-\frac1{t_i}
+4\sum_{j\ne i}\frac1{t_i^2-t_j^2}
\right].
$$


The double sum cancels pairwise:


$$
\sum_i\sum_{j\ne i}\frac1{t_i^2-t_j^2}=0.
$$


Consequently


$$
\boxed{
(2n-1)\mathbb E\sum_i t_i^{-2}
=
\mathbb E\sum_i t_i^{-1}.
}
\tag{2.6}
$$


Combining (2.5) and (2.6) proves (2.2).

In fact the exact identity is


$$
\mathbb E\sum_i t_i^{-2}
=
\frac{m-4\mathbb E\sum_{i<j}(t_i+t_j)^{-1}}
{2n(2n-1)}.
\tag{2.7}
$$


The upper bound is strict when $m>1$.

### 2.5 Trace identity and determinant inequality

Set


$$
M_0=((2n+2a+2b)!)_{a,b<m},
\qquad
M_{-1}=((2n-2+2a+2b)!)_{a,b<m}.
$$


Both are positive definite. Andréief gives the exact polynomial identity


$$
\mathbb E\prod_i(1+u t_i^{-2})
=
\frac{\det(M_0+uM_{-1})}{\det M_0}.
\tag{2.8}
$$


Let


$$
B=M_0^{-1/2}M_{-1}M_0^{-1/2}\succeq0.
$$


Differentiation at $u=0$ yields


$$
\operatorname{tr}B
=\mathbb E\sum_i t_i^{-2}
\le a_{m,n}.
\tag{2.9}
$$


If $\lambda_i\ge0$ are the eigenvalues of $B$, then


$$
\log\det(I+uB)
=\sum_i\log(1+u\lambda_i)
\le u\sum_i\lambda_i.
$$


This proves (2.3).

The largest factorial used is


$$
2n+4m-4.
\tag{2.10}
$$


The inverse-weight matrix lowers that boundary by two. Neither integration by parts introduces a successor moment.

**Audit decision:** A5 Section 6 is correct, including both integrations by parts, the trace normalization, and the exponential determinant bound.

---

## 3. Audit of the sharper square correlated-trace estimate

### 3.1 The two integration orders and their factors

Write


$$
\mathcal D_{\mathrm{ext}}=J_k(\nu)E_D,
\qquad
\mathcal S_{\mathrm{ext}}=J_{k-1}(\nu_+)E_S.
$$


The positive raw integrals are


$$
\mathcal D_{\mathrm{ext}}
=
\frac1{(k!)^2}
\int V(x)^2V(y)^2
\prod_{i,j}(x_i-y_j)\,
d\mu_{\mathrm{ext}}^k(x)d\nu^k(y),
\tag{3.1}
$$


and


$$
\mathcal S_{\mathrm{ext}}
=
\frac1{k!(k-1)!}
\int V(x)^2V(y)^2
\prod_i(x_i+1)\prod_{i,j}(x_i-y_j)\,
d\mu_{\mathrm{ext}}^k(x)d\nu_+^{k-1}(y).
\tag{3.2}
$$



For fixed exterior $x$, let


$$
P_x(y)=\prod_{i=1}^k(x_i-y).
$$


Integrating the compact variables first gives


$$
\mathcal D_{\mathrm{ext}}
=
\frac1{k!}\int V(x)^2J_k(P_x\nu)\,d\mu_{\mathrm{ext}}^k(x),
\tag{3.3}
$$




$$
\mathcal S_{\mathrm{ext}}
=
\frac1{k!}\int V(x)^2\prod_i(x_i+1)
J_{k-1}(P_x\nu_+)\,d\mu_{\mathrm{ext}}^k(x).
\tag{3.4}
$$



For a positive measure $m$ with positive-definite degree-$(k-1)$ moment matrix,


$$
\frac{J_k(m)}{J_{k-1}((1+y)^2m)}
=
\min_{\substack{\deg p\le k-1\\p(-1)=1}}
\int p(y)^2\,dm(y).
\tag{3.5}
$$


Every measure used here satisfies that hypothesis: $\nu$ and $P_x\nu$ have positive density on $(0,1)$.

Since


$$
\prod_i(x_i-1)\le P_x(y)\le\prod_i x_i
\quad(0\le y\le1),
$$


the variational formula gives


$$
R_k\mathcal S_-
\le\mathcal D_{\mathrm{ext}}
\le R_k\mathcal S_{\mathrm{ext}},
\tag{3.6}
$$


where $\mathcal S_-$ replaces $\prod_i(x_i+1)$ in (3.4) by $\prod_i(x_i-1)$.

Conversely, integrating the exterior variables first gives determinants of the exterior Gram matrices. The identities


$$
\int V(y)^2\,dm^r(y)=r!J_r(m)
$$


show that division by the stated $J$-factors produces normalized positive averages. No factorial or compact determinant factor is missing.

### 3.2 Pointwise matrix inequalities

For a fixed $y\in[0,1]^{k-1}$, let $B_\pm(y)$ be the $k\times k$ exterior Gram matrices with weights


$$
Q_\pm(x)=(x\pm1)\prod_{j=1}^{k-1}(x-y_j).
$$


Then


$$
B_+-B_-=2C,
$$


where $C$ has weight $\prod_j(x-y_j)$.

On $x>1$,


$$
0\le\prod_j(x-y_j)\le x^{k-1},
$$


so


$$
0\le C\le e^{-1}M_{-1}.
\tag{3.7}
$$



Also,


$$
Q_+(x)\ge x(x-1)^{k-1}
\ge x^k-(k-1)x^{k-1}.
$$


For $0<x\le1$,


$$
x^k-(k-1)x^{k-1}
=x^{k-1}(x-k+1)\le0
\qquad(k\ge2).
$$


Therefore the proposed extension to the full positive half-line has the correct direction:


$$
B_+\ge e^{-1}\bigl(M_0-(k-1)M_{-1}\bigr).
\tag{3.8}
$$



From Theorem 2.1 at $m=n=k$,


$$
\operatorname{tr}(M_0^{-1}M_{-1})\le a_k,
\qquad a_k=\frac1{4k-2}.
$$


Since the largest eigenvalue of a positive matrix is at most its trace,


$$
M_{-1}\le a_kM_0.
$$


Thus


$$
B_+\ge e^{-1}\chi_kM_0,
\qquad
\chi_k=1-(k-1)a_k=\frac{3k-1}{4k-2}>\frac34.
\tag{3.9}
$$



### 3.3 Inverse order, trace order, and determinant loss

Define


$$
L_y=2B_+^{-1/2}CB_+^{-1/2}\succeq0.
$$


Inverse order in (3.9) gives


$$
B_+^{-1}\le e\,\chi_k^{-1}M_0^{-1}.
$$


Taking traces against positive matrices is legitimate because
$\operatorname{tr}(UV)\ge0$ for $U,V\succeq0$. Hence


$$
\begin{aligned}
\operatorname{tr}L_y
&=2\operatorname{tr}(B_+^{-1}C)\\
&\le\frac{2e}{\chi_k}\operatorname{tr}(M_0^{-1}C)\\
&\le\frac{2}{\chi_k}\operatorname{tr}(M_0^{-1}M_{-1})\\
&\le\frac{2a_k}{\chi_k}
=\frac2{3k-1}
=\eta_k.
\end{aligned}
\tag{3.10}
$$


There is no illicit multiplication of a Loewner inequality by a noncommuting matrix.

For $k\ge2$, $\eta_k<1$. If $\lambda_i$ are the eigenvalues of $L_y$, then $0\le\lambda_i<1$, and


$$
\prod_i(1-\lambda_i)\ge1-\sum_i\lambda_i.
$$


Therefore


$$
\boxed{
\frac{\det B_-}{\det B_+}
=\det(I-L_y)\ge1-\eta_k.
}
\tag{3.11}
$$


The trace controls the whole determinant loss. Multiplying a spectral-norm estimate by $k$ would lose information unnecessarily.

Integrating (3.11), using (3.6), and cancelling the original $J$-normalizations gives


$$
\boxed{(1-\eta_k)E_S\le E_D\le E_S.}
\tag{3.12}
$$



### 3.4 Complete signed restoration

The original-density product argument gives


$$
E_S\ge \chi_ke^{-k}Z_k\ge\frac34e^{-k}Z_k.
$$


Together with (1.14)–(1.15),


$$
|D_k-E_D|\le\tau_kE_S,\qquad
|S_k-E_S|\le\tau_kE_S,
\qquad
\tau_k=\frac83\,4^{-k}.
\tag{3.13}
$$


Thus


$$
\frac{1-\eta_k-\tau_k}{1+\tau_k}
\le\frac{D_k}{S_k}
\le\frac{1+\tau_k}{1-\tau_k}.
\tag{3.14}
$$


For $k\ge64$, all denominators and the lower numerator are positive. Since


$$
\varepsilon_k=R_kD_k/S_k,
$$


this proves (0.1).

More explicitly,


$$
-\frac{\eta_k+2\tau_k}{1+\tau_k}
\le\frac{\varepsilon_k}{R_k}-1
\le\frac{2\tau_k}{1-\tau_k}.
\tag{3.15}
$$


The upper bound is not replaced by the unjustified assertion
$\varepsilon_k\le R_k$: full signed perturbations have been paid.

### 3.5 Boundaries and A5’s separate constants

The largest compact moment in either integration order is $3k-2$. The exterior weights have degree $k$, so the maximum factorial is $6k-4$.

A5’s separate $23/32$–$33/32$ comparison is also valid. Its final numerical inequalities reduce, for example, to


$$
\frac{95}{127}-\frac1{64}-\frac{23}{32}
=\frac{111}{8128}>0,
$$


and


$$
\frac{33}{32}-\frac1{64}-\frac{254}{253}
=\frac{189}{16192}>0.
$$


That independent comparison is weaker than (0.1), but has no normalization defect.

**Audit decision:** the parent correlated-trace theorem is accepted at its stated square scope.

---

## 4. Corrected rectangular reference theorem

Let $m,n\ge1$, with reference constant


$$
a=a_{m,n}=\frac{m}{2n(2n-1)}.
$$



For fixed compact nodes, form the $m\times m$ exterior Gram determinants with weights


$$
Q_D(x)=\prod_{j=1}^n(x-y_j),
$$


and


$$
Q_S(x)=(x+1)\prod_{j=1}^{n-1}(x-y_j).
$$



### 4.1 Valid exterior bounds

Normalized by $e^{-m}Z_{m,n}$, the numerator satisfies


$$
\boxed{1-na\le \frac{\det B_D}{e^{-m}Z_{m,n}}\le1.}
\tag{4.1}
$$


Indeed, under the reference ensemble, the normalized integrand is


$$
\mathbf1_{\{t_i>1\ \forall i\}}
\prod_{i,j}\left(1-\frac{y_j}{t_i^2}\right).
$$


On the exterior it is at least $1-n\sum_i t_i^{-2}$. Off the exterior, that right side is nonpositive.

For the slope, the upper bound is valid for all $n\ge1$:


$$
\boxed{\frac{\det B_S}{e^{-m}Z_{m,n}}\le e^a.}
\tag{4.2}
$$


For $n\ge2$, the proposed lower bound is also valid:


$$
\boxed{
1-(n-1)a
\le\frac{\det B_S}{e^{-m}Z_{m,n}}.
}
\tag{4.3}
$$


Here the cutoff extension works because, if one $t_i\le1$,


$$
1-(n-1)\sum_i t_i^{-2}\le0.
$$



### 4.2 The $n=1$ qualification

When $n=1$, the proposed right side in that cutoff argument is $1$, including outside the exterior. It cannot be bounded above by an integrand that is zero there.

Thus the supplied proof does **not** establish the asserted lower bound $1$ at $n=1$. A universally valid repair is


$$
\boxed{
1-a_{m,1}
\le\frac{\det B_S}{e^{-m}Z_{m,1}}
\le e^{a_{m,1}}.
}
\tag{4.4}
$$


The lower bound follows from


$$
\mathbf1_{\{t_i>1\ \forall i\}}\prod_i(1+t_i^{-2})
\ge1-\sum_i t_i^{-2}.
$$



This is a proof/scope correction. It is not a claim that the stronger $n=1$ numerical inequality is false in every instance.

### 4.3 Rectangular exterior correlation

Assume $n\ge2$, and put


$$
c=1-(n-1)a,\qquad \eta=\frac{2a}{c}.
$$


If


$$
c>0,\qquad \eta<1,
\tag{4.5}
$$


the same matrix argument proves


$$
\frac{\det B_-}{\det B_+}\ge1-\eta.
$$


After the raw and compact normalizations are restored,


$$
\boxed{(1-\eta)E_S^{m,n}\le E_D^{m,n}\le E_S^{m,n}.}
\tag{4.6}
$$



For completeness, the raw compact-first formulas are


$$
\mathcal D_{\mathrm{ext}}^{m,n}
=\frac1{m!}\int V(x)^2J_n(P_x\nu)\,d\mu_{\mathrm{ext}}^m(x),
$$




$$
\mathcal S_{\mathrm{ext}}^{m,n}
=\frac1{m!}\int V(x)^2\prod_i(x_i+1)
J_{n-1}(P_x\nu_+)\,d\mu_{\mathrm{ext}}^m(x),
\tag{4.7}
$$


where $P_x(y)=\prod_{i=1}^m(x_i-y)$. They are normalized by $J_n(\nu)$ and $J_{n-1}(\nu_+)$, respectively.

The boundaries are


$$
\text{contact degree }n+2m-2,\qquad
\text{compact degree }m+2n-2,
\tag{4.8}
$$


and reference factorial degree


$$
2n+4m-4.
\tag{4.9}
$$



These are positive exterior statements. Their application to an actual rational pencil still requires the source bridge and full signed restoration.

---

## 5. Exact rectangular source bridge

Define the rational affine pencil


$$
T_{m,n}(s)=
\det\left[
(c_{r+j})_{\substack{0\le r<m+n\\0\le j<m}}
\ \middle|\
(r_{r+j}+s(-1)^{r+j})_{\substack{0\le r<m+n\\0\le j<n}}
\right].
\tag{5.1}
$$



### 5.1 An exact raw entry clearer

The union of right-array moment indices is


$$
0,\ldots,M,\qquad M=m+2n-2.
$$


Its actual least simultaneous entry clearer is


$$
\boxed{
\Lambda_{m,n}=\operatorname{lcm}(1,3,\ldots,2m+4n-5).
}
\tag{5.2}
$$



To check minimality, any integer clearing all $r_0,\ldots,r_M$ also clears


$$
r_{j+1}+r_j
=-(2j+2)!-(2j)!+\frac4{2j+1}.
$$


Since $2j+1$ is odd, it must divide that integer clearer. Conversely, the recurrence for $\rho_j$ shows that (5.2) clears every entry.

This is an entry-clearer statement. It does not say that the coefficient clearer of $T_{m,n}$ is $\Lambda_{m,n}^n$, or that any resulting content equals one.

### 5.2 The bridge when $m\ge n$

Put


$$
\mathscr D_{m,n}
=
\det\left[
(c_{r+j})_{j<m}\ \middle|\ (\nu_{r+j})_{j<n}
\right]_{0\le r<m+n}.
\tag{5.3}
$$


If $m\ge n$, every contact column needed in (1.8) is present. Adding $e$ times contact column $j$ to right column $j$ gives


$$
\boxed{T_{m,n}(s_0)=\mathscr D_{m,n}.}
\tag{5.4}
$$


More generally,


$$
T_{m,n}(s)
=
\det[C_m\mid \nu_n+(s-s_0)wv_n^T].
\tag{5.5}
$$


This is determinant-preserving column addition and needs no independence assumption on the contact columns.

The generalized Andréief identity gives


$$
\boxed{
(-1)^{mn}\mathscr D_{m,n}
=
\frac1{m!n!}
\int V(x)^2V(y)^2
\prod_{i,j}(x_i-y_j)\,
dL^m(x)d\nu^n(y).
}
\tag{5.6}
$$


The sign $(-1)^{mn}$ comes from changing $\prod(y_j-x_i)$ to $\prod(x_i-y_j)$.

Differentiating (5.5), or extracting one atom from
$\nu+z\delta_{-1}$, gives


$$
\begin{aligned}
(-1)^{mn}T'_{m,n}(s)
={}&
\frac1{m!(n-1)!}
\int V(x)^2V(y)^2
\prod_i(x_i+1)\prod_{i,j}(x_i-y_j)\\
&\hspace{35mm}\cdot d\mu^m(x)d\nu_+^{n-1}(y).
\end{aligned}
\tag{5.7}
$$


The contact atom vanishes exactly because of $\prod_i(x_i+1)$. The overlap remains.

Thus the parent’s $m\ge n$ source-cancellation claim is correct, including its sign and slope interpretation.

### 5.3 What happens when $m<n$

Introduce a formal source parameter $z$:


$$
\mathscr F_{m,n}(z)=\det[C_m\mid \nu_n-zC_n].
$$


The first $m$ subtractions can be removed by column additions. The remaining $n-m$ cannot.

The coefficient of the highest possible power $z^{n-m}$ is exactly


$$
\boxed{
[z^{n-m}]\mathscr F_{m,n}(z)
=
(-1)^{(n-m)(m+1)}\mathscr D_{n,m}.
}
\tag{5.8}
$$


Indeed, select all remaining $-zC_j$ columns and move those $n-m$ contact columns across the first $m$ compact columns.

Equation (5.8) is a precise source identity. Nonzero leading coefficient alone would not exclude cancellation at $z=e$ when $n-m>1$. The one-missing-column case is stronger: it has only one source correction. That correction is evaluated next.

---

## 6. New full signed rectangular stability lemma

The parent rectangular note intentionally did not supply unequal-size overlap and atom estimates. The following sufficient criterion supplies such estimates without importing a different ensemble.

### 6.1 A bounded evaluation functional

Let


$$
\alpha=2n,\qquad d=2m-2,
$$


and define


$$
\kappa_{m,n}
=
\frac{\binom{2n+2m-1}{2m-2}}{(2n)!},
\qquad
K_{m,n}
=
\exp\!\left(\frac{4m-4}{2n+1}\right)\kappa_{m,n}.
\tag{6.1}
$$


For every real polynomial $p$ of degree at most $m-1$,


$$
\boxed{
|p(x)|^2
\le
K_{m,n}\,p^TM_0p
\qquad(x\in[0,1]\ \text{or }x=-1).
}
\tag{6.2}
$$



Here is a direct verification. The generalized Laguerre polynomials satisfy


$$
L_j^{(\alpha)}(z)
=
\sum_{r=0}^j(-1)^r
\binom{j+\alpha}{j-r}\frac{z^r}{r!},
\qquad
\|L_j^{(\alpha)}\|^2=\frac{(j+\alpha)!}{j!}.
$$


These formulas follow from Rodrigues’ formula and integration by parts for
$t^\alpha e^{-t}\,dt$.

For $|z|\le1$,


$$
|L_j^{(\alpha)}(z)|
\le
\binom{j+\alpha}{j}
\exp\!\left(\frac{j}{\alpha+1}\right),
$$


because


$$
\frac{\binom{j+\alpha}{j-r}}{\binom{j+\alpha}{j}}
=
\frac{j(j-1)\cdots(j-r+1)}
{(\alpha+1)\cdots(\alpha+r)}
\le\left(\frac{j}{\alpha+1}\right)^r.
$$


Therefore the degree-$d$ evaluation kernel is at most


$$
\frac{e^{2d/(\alpha+1)}}{\alpha!}
\sum_{j=0}^d\binom{j+\alpha}{j}
=
\frac{e^{2d/(\alpha+1)}}{\alpha!}
\binom{\alpha+d+1}{d}.
$$


Apply Cauchy–Schwarz to $P(t)=p(t^2)$. For $x\in[0,1]$, evaluate at $t=\sqrt x$; for $x=-1$, evaluate at $t=i$. No complex integration is used. This proves (6.2).

The norm uses no moment beyond


$$
\alpha+2d=2n+4m-4.
\tag{6.3}
$$



### 6.2 Complete numerator perturbation

For fixed $y\in[0,1]^n$, let


$$
Q_y(x)=\prod_{j=1}^n(x-y_j),
$$


and let $B_L(y)$ be the Gram matrix for $Q_y\,dL$.

Write


$$
B_L=B_{\mathrm{ext}}+B_{\mathrm{overlap}}
-Q_y(-1)vv^T.
$$


On the overlap, $|Q_y(x)|\le1$. At the atom,


$$
|Q_y(-1)|=\prod_j(1+y_j)\le2^n.
$$


Thus (6.2) gives the complete signed form estimate


$$
\left|p^T(B_L-B_{\mathrm{ext}})p\right|
\le
K_{m,n}\bigl(1-e^{-2}+2^n\bigr)p^TM_0p.
\tag{6.4}
$$



Put


$$
c_D=1-na_{m,n},
\qquad
b_D=eK_{m,n}\bigl(1-e^{-2}+2^n\bigr).
\tag{6.5}
$$


The exterior Bernoulli comparison and the trace-to-Loewner bound give


$$
B_{\mathrm{ext}}\ge e^{-1}c_DM_0.
$$


Consequently


$$
\boxed{
e^{-1}(c_D-b_D)M_0
\le B_L
\le e^{-1}(1+b_D)M_0.
}
\tag{6.6}
$$



### Theorem 6.1 — Full signed rectangular numerator criterion

If


$$
c_D>b_D,
\tag{6.7}
$$


then every $B_L(y)$ is positive definite and


$$
\boxed{
\begin{aligned}
&e^{-m}(c_D-b_D)^mZ_{m,n}J_n(\nu)\\
&\qquad\le
(-1)^{mn}\mathscr D_{m,n}\\
&\qquad\le
e^{-m}(1+b_D)^mZ_{m,n}J_n(\nu).
\end{aligned}
}
\tag{6.8}
$$


In particular, the full signed determinant is nonzero with sign $(-1)^{mn}$.

This proof includes the whole overlap and the entire negative atom. It does not replace $L$ by $\mu$.

### 6.3 Slope and full rectangular ratios

For $n\ge2$, the slope’s overlap weight has absolute value at most $2$, and its atom is exactly zero. Thus one may put


$$
c_S=1-(n-1)a_{m,n},
\qquad
b_S=2eK_{m,n}(1-e^{-2}).
\tag{6.9}
$$


If $b_S<c_S$, its full Gram matrices are positive definite.

More quantitatively, let


$$
r_D=b_D/c_D<1,\qquad r_S=b_S/c_S<1.
$$


Relative to each positive exterior matrix, the perturbation eigenvalues lie in $[-r_D,r_D]$ or $[-r_S,r_S]$. Therefore the determinant ratios lie between $(1-r)^m$ and $(1+r)^m$.

Combining this with (4.6), whenever its hypotheses also hold, gives


$$
\boxed{
(1-\eta)\frac{(1-r_D)^m}{(1+r_S)^m}
\le
\frac{\mathbf D_{m,n}}{\mathbf S_{m,n}}
\le
\frac{(1+r_D)^m}{(1-r_S)^m}.
}
\tag{6.10}
$$


Here $\mathbf D,\mathbf S$ are the full signed quantities normalized by their original compact $J$-factors.

For $m\ge n$, the exact source bridge makes (6.10) a theorem for the corresponding complete rational pencil. For $m<n$, it remains a theorem about the pure $L/\nu$ mixed determinant, not about the naïve pencil unless its source correction is also retained.

---

## 7. Evaluating the missing source term inside the original boundary

### 7.1 A positive full terminal minor

Take


$$
m=k,\qquad n=k-1,\qquad k\ge64,
$$


and set $h=k-1$. Then


$$
c_D=1-\frac{k}{2(2k-3)}
=\frac{3k-6}{4k-6}
=\frac{3h-3}{4h-2}\ge\frac12.
\tag{7.1}
$$


The evaluation constant satisfies


$$
K_{k,k-1}
<
e^2\frac{\binom{4h+1}{2h}}{(2h)!}.
$$


Hence


$$
b_D
<
e^3(1+2^h)\frac{\binom{4h+1}{2h}}{(2h)!}.
$$


Using


$$
\binom{4h+1}{2h}\le2^{4h+1},\qquad
1+2^h\le2^{h+1},\qquad e<3,
$$


and


$$
(2h)!\ge(2h/e)^{2h},
$$


we obtain


$$
b_D
<
108\left(\frac{72}{h^2}\right)^h
<
108\,4^{-h}
<
\frac12
\qquad(h\ge63).
\tag{7.2}
$$


Thus Theorem 6.1 applies.

Since $k(k-1)$ is even,


$$
\boxed{
B_k(s_0)=\mathscr D_{k,k-1}>0.
}
\tag{7.3}
$$


An explicit lower bound is


$$
\boxed{
B_k(s_0)\ge
e^{-k}J_{k-1}(\nu)Z_{k,k-1}
\left(
\frac{3k-6}{4k-6}-108\,4^{-(k-1)}
\right)^k>0.
}
\tag{7.4}
$$



This is an evaluated nonvanishing statement, not merely the naming of a determinant.

### 7.2 Exact finite boundary

The rows of $B_k$ are $0,\ldots,2k-2$. Its contact maximum is


$$
(2k-2)+(k-1)=3k-3,
$$


and its compact maximum is


$$
(2k-2)+(k-2)=3k-4.
$$


Its reference maximum factorial is


$$
2(k-1)+4k-4=6k-6.
\tag{7.5}
$$


All these lie strictly inside the original square boundaries $3k-2$ and $6k-4$.

Deleting the physical last row and last right column of the original integer matrix gives exactly


$$
\operatorname{cof}_{2k-1,\,2k-1}\mathcal M_k(s)
=\Lambda_k^{k-1}B_k(s).
$$


No extracted scalar, content, or gcd has been divided out.

### 7.3 The one-missing-contact identity

Let


$$
T_{k-1,k}(s)
=
\det[C_{k-1}\mid R_k+swv_k^T]
$$


on rows $0,\ldots,2k-2$, and put


$$
\mathscr D_{k-1,k}=\det[C_{k-1}\mid\nu_k]
$$


on the same rows.

At $s=s_0$, add $eC_j$ to the first $k-1$ right columns. The final right column remains $\nu_{k-1}-eC_{k-1}$. Expanding that column and moving $C_{k-1}$ across the preceding $k-1$ compact columns gives


$$
\boxed{
T_{k-1,k}(s_0)
=
\mathscr D_{k-1,k}+(-1)^keB_k(s_0).
}
\tag{7.6}
$$


By (7.3), the correction is nonzero.

At the original indices $K_u=9^{18+32u}$,


$$
\boxed{
T_{K_u-1,K_u}(s_0)-\mathscr D_{K_u-1,K_u}
=-eB_{K_u}(s_0)<0.
}
\tag{7.7}
$$



Thus reducing the contact count by one cannot preserve the pure compact-source determinant. Any attempt to use this shorter rectangle must retain and analyze the entire term in (7.6).

This is distinct from a prior shifted leading-coefficient theorem: it concerns the **whole evaluated terminal minor**, with its full signed measure, at $s_0$.

---

## 8. A bounded exact arithmetic check of the source obstruction

The smallest example is useful because every entry, clearer, content, and primitive denominator can be evaluated by hand. It is an auxiliary rectangle, not an original-index approximation.

From the complete recurrences,


$$
c_0=0,\quad c_1=2,\quad c_2=8,\quad c_3=266,
$$




$$
r_0=-1,\quad r_1=2,\quad r_2=-\frac{80}{3},
\quad r_3=-\frac{10748}{15}.
$$


For $m=1,n=2$,


$$
T_{1,2}(s)=
\det
\begin{pmatrix}
0&s-1&2-s\\
2&2-s&s-\frac{80}{3}\\
8&s-\frac{80}{3}&-\frac{10748}{15}-s
\end{pmatrix}.
$$


Direct expansion gives


$$
\boxed{
T_{1,2}(s)=\frac{19486s-20376}{15}.
}
\tag{8.1}
$$



The source coefficient is


$$
B_2(s)=
\det
\begin{pmatrix}
0&2&s-1\\
2&8&2-s\\
8&266&s-\frac{80}{3}
\end{pmatrix}
=
\boxed{448s-\frac{988}{3}}.
\tag{8.2}
$$


Thus


$$
T_{1,2}(s_0)-\mathscr D_{1,2}
=e\left(448s_0-\frac{988}{3}\right)>0.
$$



The actual least raw entry clearer is $15$. With both right columns cleared,


$$
H_{1,2}(s)=15^2T_{1,2}(s)
=292290s-305640.
$$


Its actual all-prime coefficient gcd is $30$, certified by


$$
3251(292290)+3109(-305640)=30.
$$


The actual least simultaneous coefficient clearer of the rational polynomial $T_{1,2}$ is $15$, and its content after that clearing is $2$. Its primitive pair is


$$
p=10188,\qquad q=9743,
$$


with


$$
3251q-3109p=1.
$$


Its whole error satisfies


$$
q(e+\pi)-p>9743\cdot5-10188=38527.
\tag{8.3}
$$



This finite calculation evaluates one source obstruction and one auxiliary primitive normalization. It establishes nothing about primitive decay at the original indices.

---

## 9. What the sharper theorem does—and does not—give arithmetically

### 9.1 An actual denominator consequence

Let


$$
U_k=\frac{1+\tau_k}{1-\tau_k}.
$$


From (0.1) and (1.12),


$$
\varepsilon_k\le\frac{28U_k}{A^{k-1}}.
$$


The already proved quarter-contraction gives


$$
\Delta_k:=p_{k+1}q_k-p_kq_{k+1}
=q_kq_{k+1}(\varepsilon_k-\varepsilon_{k+1})\in\mathbb Z_{>0}.
$$


Since


$$
\Delta_k<q_kq_{k+1}\varepsilon_k,
$$


integrality yields the actual, gcd-paid lower bound


$$
\boxed{
q_kq_{k+1}\ge\frac{A^{k-1}}{28U_k}
\qquad(k\ge64).
}
\tag{9.1}
$$


This is a lower-growth consequence. It is not the upper-growth estimate needed for primitive error decay.

The full error is still


$$
\boxed{
\ell_k=q_kR_k\,\frac{D_k}{S_k}.
}
\tag{9.2}
$$


Thus (0.1) evaluates its analytic factor, but does not evaluate $q_k$.

### 9.2 The paid adjacent identity remains intact

The complete nested array uses


$$
\sigma_n=c_{n+1}+c_n,
$$


and, indispensably,


$$
\boxed{
\tau_n=r_{n+1}+r_n
=-(2n+2)!-(2n)!+\frac4{2n+1}.
}
\tag{9.3}
$$


The last term is not optional.

For


$$
\lambda=\Lambda_{k+1},\qquad t=\lambda/\Lambda_k,
$$


the accepted integer bordering construction gives


$$
F(s)=\omega_kt^kH_k(s),\qquad
F^+(s)=\omega_{k+1}H_{k+1}(s),
$$


with actual contents $t^kG_k$ and $G_{k+1}$. Its integer Schur numerators satisfy


$$
\boxed{D^2F^+=\mathcal K F-\mathcal T.}
\tag{9.4}
$$


The division by $D^2$ is coefficientwise paid. At size $k+1$, the last underlying moment is $r_{3k+1}$, the maximum factorial is $(6k+2)!$, and the last odd denominator is $6k+1$: these are that matrix’s own physical boundaries.

The exact primitive identity is


$$
\boxed{
D\,t^kG_kG_{k+1}\Delta_k
=(-1)^k\lambda\mathcal T.
}
\tag{9.5}
$$


Both final all-prime gcds are required.

A legitimate cancellation occurs only in the particular ratio


$$
\boxed{
\frac{\Delta_k}{q_{k+1}}
=
\frac{|\mathcal T|}{t^kG_k|\mathcal K|}
=
\ell_k\left(1-\frac{\varepsilon_{k+1}}{\varepsilon_k}\right).
}
\tag{9.6}
$$


Therefore


$$
\frac{\Delta_k}{q_{k+1}}<\ell_k
\le\frac43\frac{\Delta_k}{q_{k+1}}.
\tag{9.7}
$$


No estimate for the right side follows from real positivity alone.

### 9.3 Original-index scope and selectors

The original set remains


$$
\mathcal O=\{K_u=9^{18+32u}:u\ge0\}.
$$



The all-integer minimum-denominator selector between $k$ and $k+1$ may leave $\mathcal O$. It must not be identified with the original-domain selector.

For consecutive original endpoints


$$
K=K_u,\qquad L=K_{u+1},
$$


define


$$
\Delta_u^{\mathcal O}=p_Lq_K-p_Kq_L>0.
$$


Both endpoints are original, and the preceding audit’s selector remains


$$
i_{\mathcal O}(u)\in\{K,L\},
$$


chosen by the smaller actual denominator, with


$$
\boxed{
0<\ell_{i_{\mathcal O}(u)}
\le
\sqrt{\frac{42\Delta_u^{\mathcal O}}{A^{K_u-1}}}.
}
\tag{9.8}
$$



There is also a direct original-index implication from (9.7): if


$$
\Delta_{K_u}=o(q_{K_u+1})
$$


on a specified infinite set of $u$, then $\ell_{K_u}\to0$. This does not select $K_u+1$; the whole error remains at $K_u$. The neighboring compact object is only an auxiliary comparison object.

Neither arithmetic hypothesis has been proved.

### 9.4 A precise remaining paid arithmetic lemma

A sufficient target, entirely in the existing adjacent integer data, is


$$
\boxed{
k|\mathcal T_k|
\le t_k^{\,k}G_k|\mathcal K_k|
\quad\text{at }k=K_u
}
\tag{9.9}
$$


for all sufficiently large $u$, or on an explicitly exhibited infinite subset. By (9.7), it would imply


$$
0<\ell_{K_u}\le\frac4{3K_u}\longrightarrow0.
$$



Equation (9.9) is an **open arithmetic obligation**, not a new proved result. The new trace estimate and source-cofactor theorem do not establish it.

---

## 10. Finite prime diagnostic: exact scope

The supplied diagnostic reports actual compact denominator valuations at $k=32,33$. For example, it reports


$$
v_{127}(H_{1,32})=v_{127}(G_{32})=1,
\qquad v_{127}(q_{32})=0,
$$


and


$$
v_{131}(H_{1,33})=v_{131}(G_{33})=1,
\qquad v_{131}(q_{33})=0.
$$


Thus an argument that simply declares every prime in


$$
2k<p\le6k-5
$$


to survive in the actual $q_k$ is contradicted at these certified finite instances.

The logical scope must remain limited:

* these calculations do not refute an eventual statement beginning beyond $33$;
* they do not evaluate any original index $K_u$;
* they do not prove infinite whole-error divergence;
* they do not bound the large-prime support or prime-power depth of $G_k$.

The reported $k=32$ valuation


$$
3375>780+2048=2828
$$


also refutes the specific all-$k\ge32$ envelope


$$
G_k\mid D_{k-1}^{\mathrm{cont}}E_k\,2^{2k^2}\Lambda_k^{2k},
$$


using the supplied finite certificate. It is not left standing as an unrefuted all-$k\ge32$ conjecture.

No $32\to33$ extension is proposed: that finite pair is already represented in the supplied completed diagnostic. The large determinant certificates are not recomputed here.

---

## 11. Unchanged normalization and original-producer ledger

### 11.1 Compact clearers and contents

Retain the established actual raw column clearers


$$
\Lambda_{k,j}=\operatorname{lcm}(1,3,\ldots,4k+2j-3),
$$


and the exact extracted factor


$$
E_k=\prod_{j=0}^{k-1}\frac{\Lambda_k}{\Lambda_{k,j}}.
$$


The proved divisor is


$$
D_{k-1}^{\mathrm{cont}}E_k\mid G_k,
\qquad
D_{k-1}^{\mathrm{cont}}=\prod_{r=0}^{k-2}(r!)^2.
\tag{11.1}
$$


It is not an evaluation of $G_k$.

For the rational polynomial $H_k/\Lambda_k^k$, let


$$
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


Its actual least simultaneous coefficient clearer and remaining content are


$$
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
\frac{G_k}{d_{H,k}}.
\tag{11.2}
$$



If a saturated contact frame $X$ is used, its projected entry clearer remains


$$
L_X=
\frac{\Lambda_k}
{\gcd(\Lambda_k,\{\Lambda_kB_{rj}^X\}_{r,j})},
$$


and its actual row contents remain


$$
\gcd\bigl(L_Xu_r,\{L_XB_{rj}^X\}_j\bigr).
$$


If


$$
L_X^k\det\mathcal M_X(s)=A_0+A_1s,
$$


the least simultaneous coefficient clearer and remaining content are


$$
\frac{L_X^k}{\gcd(L_X^k,A_0,A_1)},
\qquad
\frac{\gcd(A_0,A_1)}{\gcd(L_X^k,A_0,A_1)}.
\tag{11.3}
$$


No such frame is selected or divided out in this report. Monic-row clearers, frame-index payments, subsequent column contents, and the final gcd remain separate.

### 11.2 Separate binary producer

The original binary reconstruction is not identified with the compact determinant. Its domain remains


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


with contact indices $0,\ldots,b-1$, physical reconstruction indices $0,\ldots,b$, and


$$
z_b=0.
$$



Its complete corrected columns remain


$$
x=\frac12RA^{-1}f,
\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad
x=2^ax_0.
$$


The forcing $h^F$, endpoint correction $e_0$, division by $4b!$, and division by $2^a$ are retained.

The complete return remains


$$
S^{\mathrm{bin}}
=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f,
$$


and the paid valuation statement remains only


$$
v_2\!\left(\frac{S^{\mathrm{bin}}}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1}.
$$


Its norm


$$
Q=x_0^Tx_0,
$$


actual corrected-column contents, least simultaneous clearer, and final all-prime scalar gcd remain unevaluated here. Its reported valuation


$$
v_3(q^{\mathrm{bin}})=n-\frac{b+15}{2}
$$


does not transfer to $q_k$.

---

## 12. Proof-status ledger and bounded arithmetic endpoint

| Statement | Status |
|---|---|
| Two summed integrations by parts for the original $V(t^2)^2$ density | **Proved**, with zero, collision, and infinity boundaries checked |
| Trace/Andréief identity and exponential product bound | **Proved**, for all $m,n\ge1$ |
| Sharper square correlated-trace estimate | **Proved**, for the same full $H_k$, $k\ge64$ |
| Rectangular numerator exterior bounds | **Proved**, $m,n\ge1$ |
| Rectangular slope lower bound as supplied at $n=1$ | **Not established by its proof**; repaired by (4.4) |
| Rectangular correlated exterior theorem | **Proved** under $n\ge2$, $c>0$, $\eta<1$ |
| Exact source cancellation for $m\ge n$ | **Proved**, including full slope identity and signs |
| New full signed rectangular stability criterion | **Proved**, under the explicit inequalities in §6 |
| $B_k(s_0)>0$, the full physical terminal minor | **New proved result**, every $k\ge64$ |
| Naïve $m=k-1,n=k$ source bridge | **Disproved** for every $k\ge64$, including every original $K_u$ |
| Small $m=1,n=2$ determinant, clearer, gcd, and primitive pair | **Exact auxiliary finite calculation** |
| Supplied $k=32,33$ prime diagnostic | **Reused finite scope only** |
| Required all-prime cancellation for $\ell_{K_u}\to0$ | **Open** |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

No new large finite computation is needed for the analytic or source-identity proofs.

A bounded coordinator-checkable arithmetic certificate for §8 has inputs only


$$
a_0,\ldots,a_6,\qquad
\rho_0,\ldots,\rho_3,
$$


generated by the complete recurrences. Its expected exact outputs are


$$
15T_{1,2}(s)=19486s-20376,
$$




$$
3B_2(s)=1344s-988,
$$




$$
H_{1,2}(s)=292290s-305640,
$$


and the Bézout residual


$$
3251(292290)+3109(-305640)=30.
$$


These outputs have already been derived algebraically above. They require no experimental inference, and no code execution is requested.

---

## Final assessment

The stronger inverse-ensemble and correlated-trace estimates are valid. They sharpen the analytic factor in the same original ordinary error:


$$
\frac{\varepsilon_k}{R_k}
=
1+O(k^{-1}),
$$


with the explicit one-sided bounds in (3.15). They do not control the actual $q_k$.

The new substantive source result is the full terminal-minor positivity


$$
B_k(e+\pi)>0,
$$


proved with explicit complete signed bounds and with no moment beyond the original square boundary. It shows that the nearest short-contact rectangle has the unavoidable source correction


$$
(-1)^keB_k(e+\pi).
$$


At the original indices, that correction is strictly negative. An exterior reference estimate therefore cannot be substituted for that short rectangle’s actual evaluated determinant.

The exact remaining global bottleneck is still


$$
\boxed{
0<
\ell_{K_u}
=
\frac{|H_{K_u}(e+\pi)|}{G_{K_u}}
\longrightarrow0
\quad\text{on one infinite set of original indices}.
}
$$


Equivalently, a sufficient paid adjacent target is (9.9). Its unresolved part is arithmetic cancellation after the **actual all-prime gcd**, not an ordinary-error estimate, a missing sign, or a removable source term.

Accordingly, this continuation proves a sharper same-$H$ analytic theorem and a new infinite source-cancellation obstruction, but it does **not** resolve the rationality or irrationality of $e+\pi$.
