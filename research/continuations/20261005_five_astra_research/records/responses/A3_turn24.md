> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## A3 — the instantaneous uniform bias can be closed

Set


$$
\sigma=\sqrt2,\quad M=1+\sqrt2,\quad d=b-1,\quad c=d/n,
\quad c_*=10^{-6}.
$$


The new positive-ensemble estimate below holds uniformly for $d$ sufficiently large and $0\le c\le c_*$, with $c=0$ interpreted by analytic continuation of the potential. Its application to the actual columns uses


$$
d\longrightarrow\infty,\qquad c=d/n\longrightarrow0,\qquad 0\le j\le b,
$$


on both parities.

**The uniform mean/equilibrium bias is bounded; in fact the unperturbed conditioned ensemble has $O(d^{-1})$ unnormalized resolvent bias.** I prove this by an instantaneous rank-one loop inversion, without a $1/d$-expansion hypothesis. The inversion is on the same contour norm. For the wall terms, I give a density estimate, rather than infer one from small tail probability.

The subsequent actual scalar conclusion is stated explicitly relative to the retained scalar-contour and reciprocal-anchor interfaces. No primitive-denominator bound or irrationality conclusion follows.

### 1. Normalization of the instantaneous spectral factor

Use the exact rescaled potential


$$
W_c(u)=\frac{\log(1+cu^2)-\log(1-cu^2/M^2)}c
+\log(1+cu^2).
$$


Thus


$$
W_c'(z)=\frac{2(1+c)z}{1+cz^2}+\frac{2z}{M^2-cz^2}.
$$


It is analytic on $|z|\le36$, uniformly for $0\le c\le c_*$. Let $R_c$ be the mass-one equilibrium resolvent in these rescaled coordinates. Rescaling the archived resolvent, including its multiplier $\sqrt c$, gives


$$
R_c(z)=\frac{W_c'(z)}2-y_c(z),
$$


where


$$
y_c(z)=S_c(z)\sqrt{z^2-B_c^2},
$$




$$
B_c^2=\frac{M^2(c+2)}{M^2+(1+c)^2},\qquad
S_c(z)=
\frac{\sqrt{(M^2+1)(M^2+(1+c)^2)}}
{(1+cz^2)(M^2-cz^2)}.
\tag{1}
$$


The branch is $\sqrt{z^2-B_c^2}\sim z$ at infinity.

**The proposed factor is correct with the convention**


$$
y_c=W_c'/2-R_c.
$$


With the alternative convention $W_c'-2R_c$, the factor is $2S_c$.

In particular $B_c<2$. At $c=0$, write


$$
a=2(1+M^{-2}),\qquad B_0^2=4/a.
$$


Then


$$
W_0'(z)=az,\qquad
2R_0(z)-az=-a\sqrt{z^2-B_0^2}.
\tag{2}
$$



### 2. A wall-density lemma from the retained localization estimate

This step uses the retained convexity, mode and complete-domain radial-tail lemmas, without repeating them.

Work first in the full principal ordered chamber. Its energy is


$$
H(u)=d\sum_iW_c(u_i)-2\sum_{i<k}\log(u_k-u_i),
$$


and its mode $a^{(d,c)}$ satisfies $|a_i^{(d,c)}|\le16$.
For clarity, write this mode as $a_i^\circ$.

Let $p_i(t)$ be the marginal density of the $i$-th ordered coordinate. Convexity and minimality at the mode imply


$$
H(a^\circ+s(u-a^\circ))\le H(u),\qquad 0\le s\le1.
$$


Mapping the slice $u_i=24$ inward by this homothety gives


$$
p_i\!\left(a_i^\circ+s(24-a_i^\circ)\right)
\ge s^{d-1}p_i(24).
$$


For $s\in[1-1/d,1]$, $d\ge40$, the mapped coordinate is at least $23$, and $s^{d-1}\ge1/4$. Therefore


$$
\mathbb P(u_i\ge23)
\ge \frac{24-a_i^\circ}{4d}p_i(24)
\ge \frac2d p_i(24).
$$


The retained radial estimate with $T=7$ yields


$$
p_i(24)\le \frac d2 e^{-\gamma_7d},\qquad
\gamma_7=\frac12\left(\frac{49}{16}-1-\log\frac{49}{16}\right)>0.
\tag{3}
$$


Reflection gives the same estimate at $-24$.

Now condition all coordinates to lie in $[-24,24]$. A conditioned boundary slice is a subset of the corresponding full-domain slice. Dividing by the conditioning probability, which is $1-O(e^{-\gamma d})$, gives


$$
\sum_i\bigl(p_i^{[24]}(24)+p_i^{[24]}(-24)\bigr)
\le C d^2e^{-\gamma_7d}.
\tag{4}
$$


This is an actual boundary-density estimate. In particular it justifies using the ordinary resolvent field, with its boundary flux retained.

### 3. Exact finite-$d$ loop equation, including its wall flux

All expectations in this section refer to the unperturbed conditioned ensemble


$$
\Delta(u)^2e^{-d\sum_iW_c(u_i)},\qquad u_i\in[-24,24].
$$


Put


$$
\mathscr W(z)=\mathbb E\sum_i\frac1{z-u_i},\qquad
C(z,z)=
\mathbb E\left(\sum_i\frac1{z-u_i}-\mathscr W(z)\right)^2.
$$


The covariance here is algebraic.

Integration by parts with $v(u)=(z-u)^{-1}$ gives exactly


$$
\mathscr W(z)^2+C(z,z)
-d\,\mathbb E\sum_i\frac{W_c'(u_i)}{z-u_i}
=J_{d,c}(z),
\tag{5}
$$


where the boundary flux is


$$
J_{d,c}(z)=
\sum_i\left\{
\frac{p_i^{[24]}(24)}{z-24}
-\frac{p_i^{[24]}(-24)}{z+24}
\right\}.
\tag{6}
$$


Collision fluxes vanish. The derivative and diagonal interaction terms cancel precisely at $\beta=2$; there is no remaining resolvent derivative correction.

Let $\Gamma=\{|z|=30\}$. Equations (4) and (6) imply


$$
\|J_{d,c}\|_\Gamma\le C d^2e^{-\gamma_7d}.
\tag{7}
$$


The retained Hessian bound $H''\ge kdI$, $k=1/16$, remains valid after conditioning to the convex chamber. Hence


$$
|C(z,z)|
\le \mathbb E\left|\sum_i(z-u_i)^{-1}-\mathscr W(z)\right|^2
\le \frac1{k\,6^4},
\qquad z\in\Gamma.
\tag{8}
$$



### 4. Same-contour instantaneous rank-one inverse

Define, initially for a Cauchy transform $h$ of a signed measure,


$$
T_ch(z)=\int\frac{W_c'(u)}{z-u}\,d\nu(u),
\qquad h(z)=\int\frac{d\nu(u)}{z-u}.
$$


On exterior analytic functions it has the contour representation


$$
T_ch(z)=W_c'(z)h(z)
+\frac1{2\pi i}\oint_{|w|=36}
\frac{W_c'(w)h(w)}{z-w}\,dw.
\tag{9}
$$


Define


$$
K_ch=2R_ch-T_ch.
\tag{10}
$$


We use exterior analytic functions satisfying $h(z)=O(z^{-2})$, equipped with $\|\cdot\|_\Gamma$. Their exterior maximum principle bounds $\|h\|_{|w|=36}$ by $\|h\|_\Gamma$.

For the Gaussian potential, the zero-mass condition gives $T_0h=azh$. Thus


$$
K_0h=-a\sqrt{z^2-B_0^2}\,h.
\tag{11}
$$


On $\Gamma$,


$$
a|\sqrt{z^2-B_0^2}|>69,
\qquad \|K_0^{-1}\|\le1/69.
\tag{12}
$$



Here are explicit, deliberately loose perturbation bounds. From the displayed rational formula for $W_c'$,


$$
\sup_{|z|\le36}|W_c'(z)-az|<0.1.
\tag{13}
$$


Indeed the two differences are bounded respectively by


$$
\frac{2c|z|(1+|z|^2)}{1-c|z|^2},
\qquad
\frac{2c|z|^3}{M^2(M^2-c|z|^2)};
$$


their sum is less than $0.1$ at $c=10^{-6}, |z|=36$.

Equation (9) consequently gives


$$
\|(T_c-T_0)h\|_\Gamma\le0.7\|h\|_\Gamma.
$$


Since both equilibrium measures have mass one and support in $[-2,2]$,


$$
2\|R_c-R_0\|_\Gamma\le4/28<0.143.
$$


Therefore


$$
\|K_c-K_0\|<1.
\tag{14}
$$


A Neumann series on this **same contour norm** now proves


$$
\boxed{\|K_c^{-1}\|\le1/68,\qquad 0\le c\le c_*.}
\tag{15}
$$


The analytic spaces are compatible: $K_c$ maps zero-mass exterior functions to functions $O(z^{-1})$, while division by the square root in (11) maps back to $O(z^{-2})$. No repeated contour loss or full expansion theorem is involved.

### 5. Uniform coarse convergence and nonlinear absorption

The needed coarse convergence is


$$
\left\|\frac{\mathscr W}{d}-R_c\right\|_\Gamma=o(1)
\quad\text{uniformly in }c\in[0,c_*].
\tag{16}
$$



For completeness, its hypotheses hold on the fixed compact interval:

* $W_c$ is a compact continuous family in the uniform norm;
* logarithmic energy has a unique minimizer for each continuous external field on this interval;
* the explicit equilibrium measures depend continuously on $c$;
* the resolvent kernels on $\Gamma\times[-24,24]$ are bounded and uniformly continuous.

The standard compact logarithmic-energy argument proves concentration of empirical measures at the minimizer. Its upper bound truncates the logarithmic singularity; its lower bound uses separated configurations approximating a finite-energy measure. These give exponential concentration at speed $d^2$ away from any fixed neighborhood of the minimizer.

Uniformity follows by contradiction: if it failed along $c_d$, select $c_d\to c_\infty$. Replacing $W_{c_d}$ by $W_{c_\infty}$ changes the normalized log density by at most


$$
d^2\|W_{c_d}-W_{c_\infty}\|_\infty=o(d^2).
$$


The fixed-potential concentration and continuity of the equilibrium measure then give (16). A finite net on $\Gamma$ upgrades pointwise convergence to its contour norm.

Set


$$
h=\mathscr W-dR_c.
$$


Subtracting the equilibrium loop equation from (5) gives


$$
dK_ch+h^2+C(z,z)=J_{d,c}(z).
\tag{17}
$$


Thus, with $H=\|h\|_\Gamma$,


$$
H\le \frac1{68d}
\left(H^2+\frac1{k6^4}+Cd^2e^{-\gamma_7d}\right).
\tag{18}
$$


By (16), $H/d=o(1)$ uniformly. The quadratic term is therefore absorbed for all sufficiently large $d$, yielding


$$
\boxed{
\|\mathscr W-dR_c\|_\Gamma
\le \frac{C}{d}+Cd\,e^{-\gamma_7d}.
}
\tag{19}
$$


This closes the assigned instantaneous mean/equilibrium bias.

### 6. Characteristic traces and the actual normalization

Choose fixed sufficiently small complex neighborhoods of $M$ and $\rho=M^{-1}$. The functions


$$
f_{c,q}(u)=
\frac1{z(\sqrt c\,u)^{-1}+q}
=\frac{1+i\sqrt c\,u}
{(1+q)+i\sqrt c\,u(q-1)}
$$


are uniformly analytic and bounded on $|u|\le30$. Cauchy integration of (19) gives


$$
\mathbb E^{[24]}_{d,c}\sum_i f_{c,q}(u_i)
-d\int f_{c,q}\,d\widehat\mu_c=O(d^{-1}).
\tag{20}
$$


The retained complete-domain localization adds only $O(de^{-\gamma d})$.

For real $q$ in the two anchor neighborhoods, introduce the actual positive tilt


$$
h_q(u)=\sigma\cos(2\arctan(\sqrt c\,u))
-\log|z(\sqrt c\,u)^{-1}+q|.
$$


Interpolation between the base and tilted densities gives


$$
\frac{d}{dt}\mathbb E_tF=-\operatorname{Cov}_t(F,\sum_i h_q(u_i)).
$$


The particle derivatives of $h_q$ and $f_{c,q}$ are uniformly $O(\sqrt c)$; their second derivatives are $O(c)$. Thus the interpolating measures remain strongly convex for large $d$, and Brascamp–Lieb bounds the mean shift by $O(c)$. In particular it is $O(1)$.

Finally keep exactly


$$
\mathcal W_j=S_je^{i\Phi_q},\qquad
N_j(q)=\mathbb E_q\mathcal W_j,\qquad
\langle F\rangle_j=\frac{\mathbb E_q(\mathcal W_jF)}{N_j(q)}.
$$


The retained actual insertion/phase bounds give bounded $\mathcal W_j$ and $|N_j|\ge1/2$ eventually. Centering at the positive tilted mean,


$$
|\langle F\rangle_j-\mathbb E_qF|
\le \frac{\|\mathcal W_j\|_2}{|N_j|}
\sqrt{\operatorname{Var}_qF}=O(\sqrt c)
$$


for $F=\sum_i f_{c,q}(u_i)$. This does not replace $N_j$ by one.

Including the retained differentiated signed outer-sector bounds proves, uniformly in every actual coordinate,


$$
\boxed{
(\log A_j)'(q)=dL_c'(q)+O(1).
}
\tag{21}
$$


This is the requested comparison on both real anchor neighborhoods.

### 7. Consequence for stationary increments, and its precise dependencies

Integrating (21) along intervals of length $O(c)$ gives an $O(c)=o(1)$ anchored increment discrepancy. The retained stationary-location and curvature interfaces therefore compare actual and equilibrium stationary values with $o(1)$ error. Together with the retained reciprocal-anchor estimate and exact equilibrium saddle identity, this gives


$$
[nf_-(r_-)+U_-(r_-)]-[nf_+(r_+)+U_+(r_+)]
=-(2n+d)\log M+o(1).
\tag{22}
$$



**Conditional on the retained whole scalar-contour interfaces in their stated all-sublinear form**—including remote scalar arcs, signed particle sectors, both minus connectors and the local Gaussian prefactor—the conclusion is


$$
\frac{F_j}{P_j}=4\pi M^{-2n-b}(1+o(1)).
\tag{23}
$$


The new loop proof supplies the previously missing uniform bias, not a replacement proof of those contour interfaces.

The complete exponential force remains


$$
eE_i=-[z^{n+i}](1-z+z^2/2)^n
\int_0^1s^ne^{1-s+sz}\,ds,
$$


and


$$
E_j=\nu_{n,d}\!\left(
R_j\sum_{i=0}^d\sigma^ie_{d-i}(z^{-1})eE_i\right).
$$


The retained bounds


$$
|E_j/P_j|\le\frac{e^{Cb}}{n!\sqrt n},\qquad
|D/P_0|\le\frac{C\sqrt n\,e^{Cb}}{n!B_0}
$$


are negligible relative to $M^{-2n-b}$ whenever $b=o(n)$.

Consequently, under precisely those retained scalar interfaces, the actual columns


$$
u_j=(-1)^nP_j/D,\qquad
v_j-(e+\pi)u_j=\delta_{j0}+(-1)^nE_j/D-F_j/D
$$


have the whole real error


$$
\boxed{
\frac{v_j}{u_j}-(e+\pi)
=\frac{E_j}{P_j}+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac D{P_j}
=(-1)^{n+1}4\pi M^{-2n-b}(1+o(1)).
}
\tag{24}
$$


This includes eventual nonvanishing, not merely an absolute upper estimate. Uniformity transfers it to every positive diagonal metric in these actual coordinates. No nondiagonal-metric assertion is made.

### 8. Primitive bookkeeping and closing ledger

For a rational positive diagonal metric retain the least actual clearer $d_B$, an integral positive diagonal scaling $\Omega$, and


$$
N_B=d_B[u,v],\quad
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\quad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_B=A_B/g_B,\qquad p_B=H_B/g_B.
$$


The primitive multiplier is exactly $d_B^2/g_B$. With $c_W=u^TWv/(u^TWu)$,


$$
q_B(e+\pi)-p_B
=\frac{d_B^2}{g_B}
\bigl[(u^T\Omega u)(e+\pi)-u^T\Omega v\bigr]
=q_B(e+\pi-c_W).
$$


Under the scalar interfaces just specified, (24) makes this


$$
(-1)^n4\pi q_BM^{-2n-b}(1+o(1))\ne0.
$$



1. **New result and proof status.**  
   Proved here, using the retained localization lemmas: the wall-density estimate, exact wall-flux loop equation, explicit same-contour inverse bound $\|K_c^{-1}\|\le1/68$, uniform coarse convergence and nonlinear absorption. These give $O(d^{-1})$ unnormalized base-resolvent bias and the assigned $O(1)$ actual characteristic-derivative comparison. The all-sublinear whole-error law then follows conditional on the explicitly retained whole scalar-contour and reciprocal-anchor interfaces.

2. **Exact remaining bottleneck.**  
   No uniform mean-bias residual remains in this argument. The separate arithmetic bottleneck is a same-index infinite sequence with
   

$$
q_BM^{-2n-b}\longrightarrow0,
$$


   where $q_B$ is the actual denominator **after the final gcd**. No bound for that quantity has been supplied. Irrationality of $e+\pi$ remains unresolved.

3. **Computation request.**  
   None. The inverse constants and wall estimates above are analytic inequalities; no finite computation is being used to establish an infinite assertion.
