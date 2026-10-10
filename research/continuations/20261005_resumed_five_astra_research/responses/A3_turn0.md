> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3 — Quantitative common scalar error and its first nonzero correction

## 1. Result, scope, and proof status

Write


$$
\sigma=\sqrt2,\qquad M=1+\sqrt2,\qquad \rho=M^{-1},
\qquad d=b-1,\qquad c=\frac dn,
$$


and let


$$
S=e+\pi,\qquad e_j=\frac{v_j}{u_j}-S.
$$



The finite systems remain


$$
H_b,T:\{0,\ldots,d\}\times\{0,\ldots,d\},\qquad
K:\{0,\ldots,b\}\times\{0,\ldots,d\}.
$$


All assertions below concern these original systems and their actual reconstructed coordinates.

The proposed common-error bound is correct. A sharper statement is available.

> **Quantitative common-error theorem.**  
> At the established exact reconstruction, signed-sector, zero-free, and equilibrium stationary-value inputs in the packet, there are constants
> 

$$
> \epsilon>0,\quad N<\infty,\quad C<\infty,\quad \kappa>0
>
$$


> such that, for all integers
> 

$$
> n\ge N,\qquad 2\le d\le\epsilon n,\qquad 0\le j\le b,
>
$$


> on both parities of $n$,
> 

$$
> \boxed{
> \frac{e_j}{(-1)^{n+1}4\pi M^{-2n-b}}
> =
> 1-\frac dn-\frac{\sqrt2}{8n}
> +O\!\left(
> \frac{d^2+d+1}{n^2}
> \right)
> +O\!\left((1+n+d)^6e^{-\kappa n}\right).
> }
> \tag{1}
>
$$


> The constants are independent of the actual coordinate $j$.
>
> The same formula holds for the error $c_W-S$ of every positive diagonal metric in the original coordinates, independently of its weight ratios.

In particular,


$$
\boxed{
\left|
\frac{e_j}{(-1)^{n+1}4\pi M^{-2n-b}}-1
\right|
\le C\left(\frac dn+\frac1n\right).
}
\tag{2}
$$



The first correction is genuinely common. It is not the centered correction $-s_j/n^2$. More precisely, along every allocation $2\le d=o(n)$,


$$
\boxed{
1-\frac{e_j}{(-1)^{n+1}4\pi M^{-2n-b}}
=
\frac{d+\sqrt2/8}{n}\,(1+o(1)),
}
\tag{3}
$$


uniformly in all actual coordinates and all positive diagonal metrics. This includes bounded $d$, arbitrarily slowly growing $d$, and oscillating allocations.

The decisive new ingredient is a sharpened, finite-dimension characteristic comparison:


$$
\boxed{
(\log A_b)'(q)-dL_c'(q)=O(c),
}
\tag{4}
$$


uniformly on fixed complex neighborhoods of both anchors and for **every** $d\ge2$ in the small-ratio domain. A derivation is given below. It does not infer a rate from the qualitative $o(1)$ law.

I do **not** use turn28’s stronger centered remainder as an independently accepted result. For coordinate transfer, the much weaker bound


$$
\log\frac{F_j/F_b}{P_j/P_b}=O(d/n^2)
\tag{5}
$$


suffices; it is derived below directly from the finite gamma insertion.

This is an author proof from the scoped source inputs, not an independent audit of the new argument. It supplies no primitive-denominator bound and no proof or disproof of irrationality of $e+\pi$.

No filesystem, browsing, execution, or hash-verification tool is available in this exchange. Accordingly, I report no newly executed searches, calculations, credential use, or external research streams.

---

## 2. Exact objects and the common scalar factor

Retain


$$
R_j(z)=[t^j](t-1)(1+D_t)^{-n}
                 \prod_{\ell=1}^d(z_\ell+t/\sigma)
$$


and


$$
A_j(q)=\nu_{n,d}\!\left(
R_j(z)\prod_{\ell=1}^d(z_\ell^{-1}+q)
\right).
$$



The highest-coordinate insertion is exactly constant:


$$
R_b=\sigma^{-d}.
\tag{6}
$$


Thus $A_b$ is the cleanest reference for the common scalar factor.

The original scalar forces are


$$
P_j=\frac{n!}{2\pi}\int_{-\pi}^{\pi}
g(e^{is})^n A_j(\sigma+e^{is})\,ds,
\tag{7}
$$




$$
F_j=2n!\int_{-\pi/4}^{\pi/4}
h(e^{is})^n A_j(\sigma-e^{is})\,ds,
\tag{8}
$$


where


$$
g(\zeta)=1+\frac{\sigma}{2}(\zeta+\zeta^{-1}),\qquad
h(\zeta)=\frac{\sigma}{2}(\zeta+\zeta^{-1})-1.
$$



Define the highest-coordinate scalar factor


$$
\mathcal C_{n,d}
=\frac{F_b/P_b}{4\pi M^{-2n-b}}.
\tag{9}
$$


We will prove


$$
\boxed{
\log\mathcal C_{n,d}
=
-c-\frac{\sigma}{8n}
+O(c^2+c/n+n^{-2})
+O\!\left((1+n+d)^6e^{-\kappa n}\right).
}
\tag{10}
$$



The complete highest-coordinate error differs from this scalar factor only by the explicitly retained factorial residual. Section 9 handles that residual and coordinate zero’s endpoint.

---

## 3. A stronger characteristic-bias lemma, uniform down to $d=2$

### 3.1 Statement

Fix nested complex disks around $M$ and $\rho$, with their closures strictly inside the supplied zero-free regions. After reducing a fixed upper bound for $c$, we have


$$
\boxed{
\sup_q\left|(\log A_b)'(q)-dL_c'(q)\right|\le Cc
}
\tag{11}
$$


for all $d\ge2$, $c=d/n\le\epsilon$, and $n\ge N$.

On smaller disks, Cauchy’s formula then gives


$$
\boxed{
\partial_q^m\!\left((\log A_b)'(q)-dL_c'(q)\right)
=O_m(c),\qquad m\ge0.
}
\tag{12}
$$



The proof strengthens the earlier UB estimate in two ways:

1. it keeps the small factor $c$ in the test function after symmetry is used;
2. it removes the large-$d$ absorption step by an elementary a priori bound on the actual resolvent difference.

These points are what make the expansion below uniform for slowly growing and bounded dimensions.

### 3.2 The exact unperturbed rescaled ensemble

Use


$$
\tan(\theta_i/2)=\sqrt c\,u_i.
$$


The positive unperturbed principal density is exactly


$$
\Delta(u)^2
\exp\!\left[-d\sum_iW_c(u_i)\right],
\qquad |u_i|<M/\sqrt c,
\tag{13}
$$


with


$$
W_c(u)=
\frac{\log(1+cu^2)-\log(1-cu^2/M^2)}c
+\log(1+cu^2).
$$



The packet proves directly


$$
W_c''\ge\frac1{16}
\tag{14}
$$


on the whole principal domain for sufficiently small fixed $c$. The ordered-chamber energy therefore has Hessian at least $dI/16$.

We use the packet’s resulting mode and radial bounds:

- every mode coordinate has modulus at most $16$;
- the radius about that mode is stochastically dominated by a Gaussian radius with covariance $16I/d$.

These are finite-dimensional inequalities on the full principal domain, not equilibrium approximations.

### 3.3 A wall-density bound valid for all $d\ge2$

Condition temporarily on all particles belonging to $[-24,24]$. Let $p_i(t)$ be a marginal density of an ordered coordinate before conditioning, and let $a_i^\circ$ be its mode coordinate.

Convexity gives, for $0\le s\le1$,


$$
p_i\!\left(a_i^\circ+s(24-a_i^\circ)\right)
\ge s^{d-1}p_i(24).
\tag{15}
$$


Take


$$
1-\frac1{40d}\le s\le1.
$$


Because $8\le24-a_i^\circ\le40$, the resulting interval lies above $23$, has length at least $1/(5d)$, and $s^{d-1}\ge1/2$. Hence


$$
p_i(24)\le10d\,\mathbb P(u_i\ge23).
$$



The full-domain radial bound, with radius $7$, gives


$$
p_i(24)\le Cd\,e^{-\gamma_7d},
\qquad
\gamma_7=
\frac12\left(\frac{49}{16}-1-\log\frac{49}{16}\right)>0.
\tag{16}
$$


Reflection gives the same estimate at $-24$.

The probability of the conditioning event is bounded below by a fixed positive constant for every $d\ge2$. Consequently, for the conditioned boundary densities,


$$
\boxed{
\sum_i\left(p_i^{[24]}(24)+p_i^{[24]}(-24)\right)
\le Cd^2e^{-\gamma_7d}.
}
\tag{17}
$$



Thus no “sufficiently large $d$” qualification is needed here.

### 3.4 Loop coercivity and direct absorption

For the conditioned unperturbed ensemble set


$$
\mathscr W(z)=\mathbb E\sum_i\frac1{z-u_i},
\qquad
h(z)=\mathscr W(z)-dR_c(z),
$$


where $R_c$ is the rescaled mass-one equilibrium resolvent.

On $\Gamma=\{|z|=30\}$, the exact loop equation, including the wall flux, is


$$
dK_ch+h^2+C(z,z)=J_{d,c}(z).
\tag{18}
$$


Here


$$
C(z,z)=
\mathbb E\left(\sum_i(z-u_i)^{-1}-\mathscr W(z)\right)^2,
$$


and


$$
J_{d,c}(z)=
\sum_i\left(
\frac{p_i^{[24]}(24)}{z-24}
-\frac{p_i^{[24]}(-24)}{z+24}
\right).
$$



The integration by parts is valid because the density vanishes quadratically at collisions, and the actual wall flux is explicitly retained. At $\beta=2$, the resolvent-derivative terms cancel.

The packet’s corrected operator argument gives the image-coercivity inequality


$$
\|h\|_\Gamma\le\frac1{68}\|K_ch\|_\Gamma.
\tag{19}
$$


Only this inequality is used; no surjectivity assertion is needed.

Brascamp–Lieb and (17) give


$$
\|C\|_\Gamma\le\frac1{(1/16)6^4},
\qquad
\|J_{d,c}\|_\Gamma\le Cd^2e^{-\gamma_7d}.
\tag{20}
$$



Now there is a simple a priori estimate which makes the previous coarse-convergence step unnecessary. The conditioned empirical measure is supported on $[-24,24]$, while the equilibrium support is contained in $[-2,2]$. Therefore


$$
H:=\|h\|_\Gamma
\le d\left(\frac16+\frac1{28}\right)
=\frac{17}{84}d<\frac d4.
\tag{21}
$$


Combining (18)–(21),


$$
H\le\frac1{68d}
\left(H^2+C+Cd^2e^{-\gamma_7d}\right).
$$


But


$$
\frac{H^2}{68d}\le\frac{H}{272}.
$$


It follows, for every $d\ge2$, that


$$
\boxed{
\|\mathscr W-dR_c\|_\Gamma
\le C/d+Cd\,e^{-\gamma_7d}.
}
\tag{22}
$$



This is a finite-$d$ estimate. It does not rely on a limiting empirical-measure theorem.

### 3.5 Symmetry preserves the needed factor $c$

The characteristic derivative test is


$$
f_{c,q}(u)
=
\frac1{z(\sqrt c\,u)^{-1}+q}
=
\frac{1+i\sqrt c\,u}
{(1+q)+i(q-1)\sqrt c\,u}.
\tag{23}
$$



Both the unperturbed finite-$d$ measure and its equilibrium measure are symmetric. Only the even part of this test contributes:


$$
f_{c,q}^{\mathrm{ev}}(u)
=
\frac{(1+q)+(q-1)cu^2}
{(1+q)^2+(q-1)^2cu^2}.
\tag{24}
$$


In particular,


$$
f_{c,q}^{\mathrm{ev}}(u)-\frac1{1+q}
=
\frac{2(q-1)cu^2}
{(1+q)\bigl((1+q)^2+(q-1)^2cu^2\bigr)}.
\tag{25}
$$



On the fixed contour $|u|=30$, the right side is $O(c)$, uniformly on sufficiently small fixed anchor disks. The constant term contributes nothing to a zero-mass resolvent difference. Cauchy integration of (22) consequently gives


$$
\left|
\mathbb E^{[24]}\sum_i f_{c,q}(u_i)
-d\int f_{c,q}\,d\widehat\mu_c
\right|
\le
Cc\left(d^{-1}+de^{-\gamma_7d}\right)
\le Cc.
\tag{26}
$$



Removing the conditioning retains the same rate. Indeed, on the full real principal domain,


$$
\left|f_{c,q}^{\mathrm{ev}}(u)-\frac1{1+q}\right|
\le Ccu^2.
$$


Radial domination gives


$$
\mathbb E\left(\sum_i u_i^2\right)^2\le Cd^2,
$$


while the exceptional-event probability is exponentially small in $d$. Cauchy–Schwarz therefore bounds the unconditioning correction by


$$
Cc\,d\,e^{-\gamma d/2}=O(c).
$$


Thus


$$
\boxed{
\mathbb E_{\rm base}\sum_i f_{c,q}(u_i)
-dL_c'(q)=O(c).
}
\tag{27}
$$



The factor $c$ in (25) is essential. Bounding the test merely by a fixed constant would lose the sharp common expansion.

### 3.6 Positive tilts and the actual complex expectation

For complex $q$ on the anchor disks, introduce the positive modulus tilt


$$
h_q(u)=
\sigma\cos(2\arctan(\sqrt c\,u))
-\log|z(\sqrt c\,u)^{-1}+q|.
$$


Uniformly on the full real principal domain,


$$
|h_q'(u)|\le C\sqrt c,\qquad |h_q''(u)|\le Cc.
\tag{28}
$$


The same bounds hold throughout positive interpolation between the base and tilted densities. Their Hessians remain bounded below by $k d I$, for a fixed $k>0$.

For


$$
F_q=\sum_i f_{c,q}(u_i),
$$


Brascamp–Lieb gives


$$
\operatorname{Var}_{\mathbb C}(F_q)\le Cc,\qquad
\operatorname{Var}\!\left(\sum_i h_q(u_i)\right)\le Cc.
\tag{29}
$$


The interpolation covariance identity therefore changes the mean by $O(c)$.

Finally, retain the actual phase. Subtract its exact positive-measure mean and write


$$
w=e^{i(\Phi_q-\mathbb E_q\Phi_q)},\qquad N=\mathbb E_qw.
$$


The phase is a linear statistic with uniformly $O(\sqrt c)$ particle derivatives in the $u$-coordinates, so


$$
|N-1|\le Cc,\qquad
\operatorname{Var}_{\mathbb C}(w)\le Cc.
\tag{30}
$$


Thus


$$
\left|
\frac{\mathbb E_q(wF_q)}{N}-\mathbb E_qF_q
\right|
=
\left|\frac{\operatorname{Cov}_q(F_q,w)}{N}\right|
\le Cc.
\tag{31}
$$



The original signed outer sectors, including their differentiated characteristic factors, add only


$$
C(1+n+d)^p e^{-\eta n+C_0d}
$$


for a fixed exponent $p$. After reducing $\epsilon$ and increasing $N$, this is bounded by $Cc$.

Equations (27)–(31) prove (11). This completes the outstanding sharpened characteristic lemma.

---

## 4. The reciprocal-anchor contribution

Put


$$
\alpha=\frac{\sigma}{M}=2-\sigma,\qquad
\beta=\sigma M=2+\sigma.
\tag{32}
$$



At the reciprocal anchors, the positive principal measures coincide exactly:


$$
|z^{-1}+M|=M|z^{-1}+\rho|,
\qquad
Z_d(M)=M^dZ_d(\rho).
\tag{33}
$$



For the highest coordinate,


$$
A_b(q)=B_bZ_d(q)\,
\mathbb E_qe^{i\Phi_q}
+\text{signed outer sectors},
\qquad B_b=\sigma^{-d}.
\tag{34}
$$



We need the first-order correction to this actual phase expectation.

### 4.1 Translation variance on the original chamber

Let


$$
X=\sum_i\theta_i.
$$


At either real anchor, reflection gives $\mathbb EX=0$. The original angular density has Hessian at least


$$
(n\alpha-C)I.
\tag{35}
$$



The finite-$d$ radial estimates used above, after the bounded positive tilt is included, give


$$
\mathbb E\sum_i\theta_i^{2m}\le C_mdc^m,
\tag{36}
$$


and, for a fixed sufficiently small angle $\delta>0$,


$$
\mathbb P\{\max_i|\theta_i|>\delta\}\le e^{-\kappa_0n}.
\tag{37}
$$


For completeness, the latter follows from


$$
|\theta_i|>\delta
\ \Longrightarrow\
|u_i|>\tan(\delta/2)/\sqrt c.
$$


The Gaussian radial bound then has exponent


$$
-K_\delta n+O(d\log(1/c))+O(d),
$$


which is at most $-\kappa_0n$ after a fixed reduction of $\epsilon$. No lower growth rate for $d$ is used.

The exact sum-translation identity is


$$
\mathbb E\left[X\sum_iV_q'(\theta_i)\right]=d.
\tag{38}
$$


There is no principal-endpoint flux: the density vanishes there to order $n$. Collision fluxes vanish as well.

As emphasized in turn27, the singular score cannot be replaced globally by a bounded cubic remainder. Choose instead a smooth even cutoff $\chi$, supported strictly inside the original principal interval, and use the vector field


$$
v_i=X\chi(\theta_i).
$$


For


$$
f'(t)=\frac{\sigma\sin t}{1+\sigma\cos t},
\qquad
R(t)=\chi(t)f'(t)-\alpha t,
$$


one has


$$
|R'(t)|\le Ct^2
$$


globally on that interval.

Brascamp–Lieb and (36) give


$$
\operatorname{Var}\!\left(\sum_iR(\theta_i)\right)\le Cc^3,
$$


so its covariance with $X$ is $O(c^2)$. The smooth lower-order score contributes $O(c)$ before division by $n$. The cutoff pair term is supported on the event in (37); its collision singularity is canceled by the difference of cutoff values.

Consequently,


$$
\boxed{
\operatorname{Var}(X)
=\frac c\alpha+O(c^2+c/n)
+O\!\left((1+n+d)^p e^{-\kappa_0n}\right).
}
\tag{39}
$$


This derivation is on the original chamber, with the endpoint issue explicitly handled.

### 4.2 Actual phase expectation

At a real anchor,


$$
\Phi_q=\eta_qX+T_q,\qquad
\eta_q=-\sigma-\frac1{1+q}.
\tag{40}
$$


The odd remainder satisfies


$$
\|T_q\|_2\le Cc^{3/2},
$$


while strong-log-concavity concentration gives


$$
\|\Phi_q\|_4\le C\sqrt c.
$$


Therefore


$$
\mathbb E\Phi_q^2
=\eta_q^2\operatorname{Var}(X)+O(c^2),
$$


and


$$
\log\mathbb E e^{i\Phi_q}
=-\frac12\eta_q^2\operatorname{Var}(X)+O(c^2).
\tag{41}
$$


The expectation is real and positive for sufficiently small fixed $c$.

Now


$$
\eta_\rho^2-\eta_M^2=3-\sigma.
$$


Using (33), (39), and (41), and restoring the signed outer sectors,


$$
\boxed{
\log\frac{A_b(\rho)}{A_b(M)}+d\log M
=
-\left(1+\frac{\sigma}{4}\right)c
+O(c^2+c/n)
+O\!\left((1+n+d)^p e^{-\kappa n}\right).
}
\tag{42}
$$


Indeed,


$$
\frac{3-\sigma}{2\alpha}=1+\frac{\sigma}{4}.
$$



This nonzero anchor-phase correction is one of the common terms that the qualitative reciprocal-anchor estimate conceals.

---

## 5. Actual stationary values: no surviving $nc^2$ or $nc^3$ term

Let


$$
f_+(r)=\log g(r),\qquad f_-(r)=\log h(r),
$$


and


$$
q_+(r)=\sigma+r,\qquad q_-(r)=\sigma-r.
$$


Write


$$
D_c(q)=\log A_b(q)-dL_c(q).
\tag{43}
$$


Section 3 proves


$$
D_c'(q)=O(c)
\tag{44}
$$


on fixed anchor disks.

The equilibrium phases are


$$
\Phi_\pm(r)=f_\pm(r)+cL_c(q_\pm(r)).
$$


We reuse the packet’s exact equilibrium stationary-value identity at its stated algebraic scope:


$$
r_+(c)=\frac2{2+c},\qquad
r_-(c)=\frac{2M}{2M-c},
\tag{45}
$$




$$
\Phi_+(r_+(c))-\Phi_-(r_-(c))
=(2+c)\log M.
\tag{46}
$$


This is an identity for the explicit equilibrium phases, not a scalar-integration theorem.

Let $r_{b,\pm}$ be the actual stationary radii for


$$
G_\pm(r)=nf_\pm(r)+\log A_b(q_\pm(r)).
$$


Their radial curvatures are bounded below by a positive multiple of $n$. Equation (44) therefore gives


$$
r_{b,\pm}-r_\pm(c)=O(c/n).
\tag{47}
$$



Both equilibrium radii lie $O(c)$ from $1$. Hence


$$
D_c(q_\pm(r_\pm(c)))-D_c(q_\pm(1))=O(c^2).
\tag{48}
$$


Moving from an equilibrium stationary point to the actual one changes the full stationary value by $O(c^2/n)$.

Combining (42), (46), and (48),


$$
\boxed{
G_-(r_{b,-})-G_+(r_{b,+})
=
-(2n+d)\log M
-\left(1+\frac{\sigma}{4}\right)c
+O(c^2+c/n)
+O\!\left((1+n+d)^p e^{-\kappa n}\right).
}
\tag{49}
$$



Thus the potentially large equilibrium saddle-displacement terms cancel **exactly** through the established identity (46). They are not bounded separately by $O(d^2/n)$. No term of size $nc^2$, $nc^3$, or another larger common scale survives this comparison.

---

## 6. Gaussian prefactor and the $1/n$ scalar correction

### 6.1 Curvature expansion

Let


$$
\lambda_\pm
=r_{b,\pm}^{\,2}
\left[
f_\pm''(r_{b,\pm})
+\frac1n\frac{d^2}{dr^2}
 \log A_b(q_\pm(r))\bigg|_{r=r_{b,\pm}}
\right].
\tag{50}
$$


These are the angular Gaussian curvatures of the whole actual scalar exponent.

At $c=0$,


$$
\lambda_+(0)=\alpha,\qquad
\lambda_-(0)=\beta.
$$


The symmetric equilibrium satisfies, uniformly on the anchor disks,


$$
L_c(q)=\log(1+q)+O(c),
\tag{51}
$$


with the same statement for fixed-order derivatives.

The first stationary displacements are


$$
r_+(c)=1-\frac c2+O(c^2),\qquad
r_-(c)=1+\frac{\rho c}{2}+O(c^2).
$$


Also, reciprocal symmetry of each base phase gives


$$
f_\pm'''(1)=-3f_\pm''(1).
$$



It follows that


$$
\lambda_+
=
\alpha+
c\left(\frac{\alpha}{2}-\frac1{(1+M)^2}\right)
+O(c^2+c/n),
$$




$$
\lambda_-
=
\beta+
c\left(-\frac{\rho\beta}{2}-\frac1{(1+\rho)^2}\right)
+O(c^2+c/n).
$$


The coefficients simplify to


$$
\boxed{
\lambda_+=\alpha\left(1+\frac{\sigma c}{4}\right)
+O(c^2+c/n),
}
\tag{52}
$$




$$
\boxed{
\lambda_-=\beta\left(1-\frac{\sigma c}{4}\right)
+O(c^2+c/n).
}
\tag{53}
$$


Consequently,


$$
\boxed{
\log\sqrt{\lambda_+/\lambda_-}
=
-\log M+\frac{\sigma c}{4}
+O(c^2+c/n).
}
\tag{54}
$$



The Gaussian prefactor cancels the $-\sigma c/4$ part of the anchor correction, but it does not cancel the remaining $-c$.

### 6.2 A uniform scalar expansion through relative order $1/n$

On each actual stationary circle, write


$$
G_\pm(\theta)=
n\log g_\pm(r_{b,\pm}e^{i\theta})
+\log A_b(\sigma\pm r_{b,\pm}e^{i\theta}).
$$


The entire logarithm of $A_b$ is included. Thus


$$
G_\pm'(0)=0,\qquad G_\pm''(0)=-n\lambda_\pm.
$$



On fixed central arcs, the supplied zero-free logarithmic bounds and Section 3 give uniform bounds for the required fixed-order derivatives of $G_\pm/n$. Their real parts have uniform negative angular curvature.

Let


$$
\psi_\pm(\theta)=G_\pm(\theta)/n,
\qquad
\psi_{\pm,k}=\psi_\pm^{(k)}(0).
$$


Ordinary Taylor expansion on a symmetric central arc gives


$$
\begin{aligned}
\int e^{G_\pm(\theta)}\,d\theta
={}&e^{G_\pm(0)}
\sqrt{\frac{2\pi}{n\lambda_\pm}}\\
&\times\left[
1+\frac1n\left(
\frac{\psi_{\pm,4}}{8\lambda_\pm^2}
+\frac{5\psi_{\pm,3}^2}{24\lambda_\pm^3}
\right)
+O(n^{-2})
\right].
\end{aligned}
\tag{55}
$$


The $O(n^{-2})$ constant is uniform.

Here is why the complex phase causes no missing half-order term. Reflection gives


$$
G_\pm(-\theta)=\overline{G_\pm(\theta)}.
$$


After rescaling $x=\sqrt n\,\theta$, all terms of orders $n^{-1/2}$ and $n^{-3/2}$ in the Taylor expansion are odd and integrate to zero on the symmetric central arc. The remaining errors are bounded by an integrable Gaussian times $n^{-2}$ and a fixed polynomial in $x$. This uses the whole stationary exponent, not a modulus-only saddle.

At $c=0$, the angular phases are even:


$$
\psi_{\pm,3}=0,
\qquad
\psi_{\pm,4}=\lambda_\pm(0)-3\lambda_\pm(0)^2.
$$


Thus the two $1/n$ coefficients at $c=0$ are


$$
B_+(0)=\frac1{8\alpha}-\frac38,\qquad
B_-(0)=\frac1{8\beta}-\frac38.
$$


Their difference is


$$
\boxed{
B_-(0)-B_+(0)
=\frac18\left(\frac1\beta-\frac1\alpha\right)
=-\frac{\sigma}{8}.
}
\tag{56}
$$



Uniform derivative control gives


$$
B_\pm(c,n)=B_\pm(0)+O(c),
$$


so the scalar-expansion ratio contributes


$$
\boxed{
-\frac{\sigma}{8n}+O(c/n+n^{-2})
}
\tag{57}
$$


to its logarithm.

### 6.3 Original contours, remote arcs, and both minus connectors

The plus contour is the original closed circle, deformed within its analytic annulus to the actual stationary radius.

The minus contour is the original open arc. Its deformation includes **both** radial connectors at arguments $\pm\pi/4$.

For the remote circular arcs, the source inequalities give


$$
C\sqrt n\,e^{-n/400+C_0d}.
\tag{58}
$$


At a minus connector,


$$
h(re^{\pm i\pi/4})
=\frac{r+r^{-1}}2-1
\pm i\frac{r-r^{-1}}2.
$$


The original endpoints satisfy $h(e^{\pm i\pi/4})=0$. For sufficiently small fixed $\epsilon$, both connectors obey the source bound


$$
C\sqrt n\,e^{C_0d}(0.002/0.4)^n.
\tag{59}
$$



These estimates include the actual characteristic insertion and full absolute particle-sector bounds. They are exponentially smaller than the actual nonzero central Gaussian integral.

### 6.4 The common factor

The exact scalar normalization ratio is $4\pi$. Combining (49), (54), and (57), while retaining (58)–(59), gives


$$
\log\frac{F_b/P_b}{4\pi M^{-2n-b}}
=
-\left(1+\frac{\sigma}{4}\right)c
+\frac{\sigma c}{4}
-\frac{\sigma}{8n}
+O(c^2+c/n+n^{-2})
+\text{exponentially small terms}.
$$


This proves (10):


$$
\boxed{
\log\mathcal C_{n,d}
=
-c-\frac{\sigma}{8n}
+O(c^2+c/n+n^{-2})
+\text{exponentially small terms}.
}
$$



Exponentiation gives the same first-order expansion for $\mathcal C_{n,d}$ itself.

---

## 7. Uniform transfer to every actual coordinate

This section does not use the unreviewed stronger remainder in turn28.

Let $\varepsilon_j$ denote the reconstruction sign, and put


$$
B_j=|K_{j,d}|\sigma^{-d},\qquad
\mathcal S_j=\varepsilon_jR_j/B_j.
$$


The finite gamma expansion gives


$$
\|\mathcal S_j-1\|_\infty\le e^{\sigma d/n}-1.
\tag{60}
$$



A useful derivative bound follows from the same finite expansion. In a normalized degree-$k$ term, the sum of the absolute coefficients of degree $\ell$ is at most


$$
\binom{k}{\ell}(\sigma/n)^\ell.
$$


By symmetry, differentiating with respect to one variable gives at most $1/d$ of the total degree-weighted coefficient sum. Therefore


$$
\boxed{
\sup_{|z_i|\le1}|\partial_{z_i}\mathcal S_j|
\le \frac{\sigma}{n}e^{\sigma d/n}.
}
\tag{61}
$$


The actual one- or two-degree gamma mixture is a positive combination of these normalized terms, so the same bound holds for every coordinate.

For sufficiently small $c$, define


$$
L_j=\log\mathcal S_j,
$$


anchored at $\mathcal S_j(0)=1$. Then


$$
|L_j|\le Cc,\qquad
|\partial_{\theta_i}L_j|\le C/n.
\tag{62}
$$


On each positive modulus measure on the fixed anchor disks,


$$
\operatorname{Var}_{\mathbb C}(L_j)\le C d/n^3=Cc/n^2.
\tag{63}
$$



Use the same reference at both anchors:


$$
\mathcal R_j=\exp(\mathbb E_*L_j),
$$


where $\mathbb E_*$ is the positive principal measure without a characteristic modulus.

Positive interpolation changes $\mathbb E L_j$ by at most


$$
\sqrt{Cc/n^2}\sqrt{Cc}=Cc/n.
$$


The centered actual-phase covariance has the same bound. Expanding $e^{L_j}$ about the positive-measure mean, with the quadratic remainder retained, gives


$$
\boxed{
Q_j(q):=\frac{B_bA_j(q)}{\varepsilon_jB_jA_b(q)}
=
\mathcal R_j\left(1+O(c/n)\right)
}
\tag{64}
$$


uniformly on the fixed disks, after the exponentially small full-circle outer sectors are included.

On the highest-coordinate stationary contours, the normalized absolute mass of each central integral is bounded. Hence inserting (64) changes each scalar quotient by $O(c/n)$. The remote arcs and both connectors retain their exponential estimates because $\mathcal S_j$ is uniformly bounded globally.

The constants $\varepsilon_jB_j/B_b$ and the common reference $\mathcal R_j$ cancel between the minus and plus quotients. Thus


$$
\boxed{
\log\frac{F_j/F_b}{P_j/P_b}
=O(c/n)
+O\!\left((1+n+d)^p e^{-\kappa n}\right).
}
\tag{65}
$$



This is enough for the common expansion. It is compatible with the accepted centered comparison, but does not assert turn28’s finer remainder or re-establish its coefficient.

---

## 8. Polynomial-power-six bookkeeping

The packet sometimes writes exponential errors as


$$
C(1+n+d)^p e^{-\eta n+C_0d}
\tag{66}
$$


with a fixed but unspecified polynomial exponent $p$.

It is not justified to replace $p$ by $6$ while keeping the same exponential constant. The following explicit reduction repairs that bookkeeping.

First choose


$$
\epsilon\le\frac{\eta}{4C_0}
$$


when $C_0>0$. Then


$$
-\eta n+C_0d\le-\frac{3\eta}{4}n.
$$


For any fixed $p$,


$$
(1+n+d)^{\max(p-6,0)}e^{-\eta n/2}
$$


is bounded on $d\le\epsilon n$. Consequently,


$$
\boxed{
C(1+n+d)^p e^{-\eta n+C_0d}
\le C'(1+n+d)^6e^{-\eta n/4}.
}
\tag{67}
$$



Thus one may choose


$$
\kappa=\frac14\min\{\text{the positive exponential constants used above}\},
$$


after all $C_0d$ costs have been absorbed by the fixed small-ratio restriction.

This works because the source exponents $p$ are fixed. It would not justify a polynomial exponent growing with $n$ or $d$.

---

## 9. Complete forcing, endpoint, and positive diagonal metrics

Retain the complete exponential force


$$
eE_i
=-[z^{n+i}](1-z+z^2/2)^n
\int_0^1s^ne^{1-s+sz}\,ds,
\tag{68}
$$


and


$$
E_j=\nu_{n,d}\!\left(
R_j\sum_{i=0}^d\sigma^ie_{d-i}(z^{-1})eE_i
\right).
\tag{69}
$$



With $D=\det H_b$, the exact original equations are


$$
u_j=(-1)^nP_j/D,
$$




$$
v_j-Su_j=\delta_{j0}+(-1)^nE_j/D-F_j/D.
$$


Therefore the whole error is


$$
\boxed{
e_j=
\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac D{P_j}.
}
\tag{70}
$$



The established lower-bound and residual estimates give


$$
|E_j/P_j|\le \frac{C2^d}{n!\sqrt n},
\qquad
|D/P_0|\le \frac{C\sqrt n}{n!B_0},
\qquad
B_0=(n)_d\sigma^{-d}.
\tag{71}
$$


Their size relative to the proposed leading error is bounded by


$$
\tau_{n,d}
=
CM^{2n+b}\left(
\frac{2^d}{n!\sqrt n}
+\frac{\sqrt n}{n!B_0}
\right).
\tag{72}
$$


Uniformly for $d\le\epsilon n$,


$$
\log\tau_{n,d}\le-n\log n+O(n),
$$


so this is absorbed into the exponential remainder after $N$ is enlarged.

In particular:

- the complete $eE$ insertion has not been truncated;
- coordinate zero’s endpoint has not been omitted;
- both parities retain their original sign;
- the resulting whole errors are nonzero and have sign $(-1)^{n+1}$.

Equations (10), (65), and (70)–(72) prove (1).

For a positive diagonal metric $W$, set


$$
\omega_j=\frac{W_{jj}u_j^2}{u^TWu}.
$$


Then


$$
\omega_j>0,\qquad \sum_j\omega_j=1,
\qquad
c_W-S=\sum_j\omega_je_j.
\tag{73}
$$


Since (1) is uniform in $j$, the same expansion holds after this convex combination, with no restriction on the positive weight ratios.

There is no assertion here for general nondiagonal metrics.

---

## 10. Sharpness and the remaining analytic budget

The common expansion can be written


$$
\boxed{
\mathcal C_{n,d}
=
1-\frac{d+\sqrt2/8}{n}
+O\!\left(\frac{d^2+d+1}{n^2}\right)
+\text{exponentially small terms}.
}
\tag{74}
$$



This identifies three distinct contributions:

| Contribution | First-order logarithmic term |
|---|---:|
| Actual reciprocal-anchor phase | $-\left(1+\sqrt2/4\right)d/n$ |
| Gaussian curvature ratio | $+\left(\sqrt2/4\right)d/n$ |
| First scalar saddle correction | $-\sqrt2/(8n)$ |

The remaining common $d/n$ coefficient is therefore exactly $-1$.

For $d=o(n)$, the remainder in (74) is


$$
o\!\left(\frac{d+1}{n}\right).
$$


Thus the rate $O(d/n+1/n)$ is sharp. In particular, it cannot uniformly be improved to $O(d/n^2+1/n)$ when $d\to\infty$.

The analytic decay budget for the whole error is


$$
\boxed{
\log|c_W-S|
=
\log(4\pi)-(2n+b)\log M
-\frac dn-\frac{\sqrt2}{8n}
+O\!\left(\frac{d^2+d+1}{n^2}\right).
}
\tag{75}
$$


On an all-sublinear allocation, the correction after $-(2n+b)\log M$ is $o(1)$. It is a genuine improvement in the finite asymptotic formula, but not a new exponential-in-$n$ denominator allowance.

The obstruction in the earlier quantitative route is now precise: an $O(d^2/n)$ estimate for separate stationary increments is adequate for a restricted qualitative join, but not for the uniform sharp common correction. The repair is the combination of:

1. the exact equilibrium stationary-value cancellation;
2. the strengthened $O(c)$ characteristic derivative bias;
3. the first nontrivial actual anchor-phase and Gaussian calculations.

---

## 11. Actual primitive denominator and irrationality status

For rational positive diagonal weights, preserve the least actual two-column clearer $d_B$, an integral positive diagonal scaling $\Omega$, and


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
q_B=\frac{A_B}{g_B},\qquad
p_B=\frac{H_B}{g_B}.
\tag{76}
$$


The primitive multiplier is exactly $d_B^2/g_B$.

The whole evaluated primitive form is


$$
\boxed{
q_BS-p_B
=
\frac{d_B^2}{g_B}
\bigl[(u^T\Omega u)S-u^T\Omega v\bigr]
=q_B(S-c_W).
}
\tag{77}
$$


Consequently,


$$
\boxed{
q_BS-p_B
=
(-1)^n4\pi q_BM^{-2n-b}
\left[
1-\frac dn-\frac{\sqrt2}{8n}
+O\!\left(\frac{d^2+d+1}{n^2}\right)
\right],
}
\tag{78}
$$


with the already specified exponentially small remainder understood.

No estimate for $q_B$ after the final gcd has been proved.

A sufficient remaining arithmetic statement is an infinite same-index sequence on which


$$
q_BM^{-2n-b}\longrightarrow0.
\tag{79}
$$


The new common correction neither establishes that statement nor removes its necessity for this proposed irrationality mechanism.

**The irrationality or rationality of $e+\pi$ remains unresolved.**

---

## 12. Closing ledger and bounded exact-arithmetic request

### New result and proof status

The report proves, from the scoped source interfaces:

1. the finite-dimension strengthened characteristic comparison
   

$$
(\log A_b)'-dL_c'=O(d/n),
$$


   uniformly down to $d=2$;
2. the common whole-error expansion (1);
3. the proposed uniform $C(d/n+1/n)$ bound;
4. its sharp first common correction
   

$$
-d/n-\sqrt2/(8n);
$$


5. transfer to every actual coordinate and every positive diagonal metric, with full forcing and endpoint terms retained;
6. valid power-six exponential bookkeeping after an explicit reduction of the exponential constant.

Turn28’s stronger centered remainder is not assumed to have passed its separate review.

### Exact remaining mathematical bottleneck

For the analytic refinement, the new argument’s most substantive review item is the strengthened characteristic lemma in Section 3, especially:

- the all-$d$ wall-density estimate;
- direct absorption using $H<d/4$;
- the symmetry extraction of the factor $c$;
- the centered positive-measure covariance transfer to the actual complex expectation.

Those steps are derived here rather than left as an unnamed theorem.

For irrationality, the bottleneck remains a same-index estimate for the **actual reduced denominator after the final gcd**, sufficient to make the nonzero whole primitive errors tend to zero. No such estimate is supplied.

### Bounded exact arithmetic

No finite calculation is needed to establish the uniform estimates. A small optional algebraic certificate can check the two common coefficients without any numerical integration.

**Inputs**


$$
\sigma^2=2,\quad
M=1+\sigma,\quad \rho=M^{-1},\quad
\alpha=\sigma/M,\quad \beta=\sigma M,
$$




$$
\eta_q=-\sigma-\frac1{1+q},
$$




$$
\lambda_+'=\frac{\alpha}{2}-\frac1{(1+M)^2},
\qquad
\lambda_-'=-\frac{\rho\beta}{2}-\frac1{(1+\rho)^2}.
$$



**Requested exact checks in $\mathbb Q(\sqrt2)$**


$$
-\frac{\eta_\rho^2-\eta_M^2}{2\alpha}
+\frac12\left(\frac{\lambda_+'}{\alpha}
-\frac{\lambda_-'}{\beta}\right)+1=0,
\tag{80}
$$




$$
\frac18\left(\frac1\beta-\frac1\alpha\right)
+\frac{\sigma}{8}=0.
\tag{81}
$$



**Divisions**

Only the displayed nonzero algebraic numbers are divided. Their positivity follows from $1<\sqrt2<2$; no modular or potentially zero division is involved.

**Expected verifiable output**

Two exact zero remainders after reduction by $\sigma^2-2$, certifying respectively the common coefficients $-1$ and $-\sqrt2/8$.

**Resource estimate**

A fixed calculation of well below $10^4$ rational-field operations, with negligible polynomial degree and only small exact rational coefficients. No remote execution is requested or presumed.

Such a certificate would verify only these bounded algebraic simplifications. It would not certify the uniform analytic estimates, the final denominator, or irrationality.
