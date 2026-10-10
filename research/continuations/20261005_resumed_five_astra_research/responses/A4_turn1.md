> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 independent review: the quantitative COMMON law and the completed prime-$29$ third-defect calculation

## 1. Conclusions and verification scope

The supplied work still does **not** prove either rationality or irrationality of $e+\pi$. The two assigned new items nevertheless yield substantive results at their proper scopes.

### Analytic conclusion

A3’s claimed common correction


$$
-\frac dn-\frac{\sqrt2}{8n}
$$


is consistent with, and follows from, the supplied exact reconstruction and equilibrium stationary-value interfaces. The decisive strengthened characteristic estimate can be justified uniformly down to $d=2$. In particular, the wall argument and the small-$d$ absorption do not require an unstated condition $d\to\infty$.

One point deserves an explicit repair in the presentation: the loop image-coercivity estimate should be established for the **actual conditioned resolvent difference**, with its zero-mass condition and the divided-potential term retained. I give that derivation below. It avoids reliance on an unspecified inverse or a large-$d$ convergence theorem.

At the retained analytic interfaces, the resulting whole-error theorem is


$$
\boxed{
\frac{e_j}{(-1)^{n+1}4\pi M^{-2n-b}}
=
1-\frac dn-\frac{\sqrt2}{8n}
+O\!\left(\frac{d^2+d+1}{n^2}\right)
+O(e^{-\kappa n}),
}
\tag{1.1}
$$


uniformly for


$$
n\ge N,\qquad 2\le d=b-1\le\epsilon n,\qquad 0\le j\le b,
$$


on both parities. The constants are independent of the positive diagonal weight ratios when the coordinate errors are combined into a diagonal-metric center.

This is a quantitative theorem on a fixed sufficiently small strip. Its **asymptotic first-correction interpretation** is strongest on $d=o(n)$, where the remainder is $o((d+1)/n)$.

### Arithmetic conclusion

The completed receipts close the previously missing $\Gamma _0$ calculation. More importantly than the 25 zero contractions, their output proves the ordinary polynomial identity


$$
\boxed{
R_C(D,J)=27K_D(J)\quad\text{in }\mathbb F_{29}[D,J].
}
\tag{1.2}
$$


Together with the retained, already settled


$$
R_{29}=20K_d,
$$


this proves the intended conditional third-defect theorem:


$$
\boxed{
M-(6C_n)^{-1}D\equiv0\pmod{29^3}
}
\tag{1.3}
$$


for actual original-family indices satisfying


$$
0\le d\le24,\qquad T=0,\qquad D_1=0,
$$


at the supplied original-force and reconstruction interfaces.

It does **not** prove that the simultaneous locus $T=D_1=0$ is populated infinitely often—or populated at all—on the original exponent progression. Nor does it give all-depth norm–mixed alignment or a global primitive-denominator bound.

### Verification limitations and overlap gate

I compared the new arguments with the supplied accepted CSC/contact scopes. I do not reopen the completed $\Gamma _1$ calculation or use the centered comparison as a substitute for a common-amplitude proof.

No browsing, filesystem access, execution, or hash-verification facility is available in this exchange. Thus:

* the mathematical arguments and displayed coordinator source are reviewed directly;
* the two implementations’ numerical agreement is used as the supplied finite arithmetic certificate;
* the listed hashes are provenance data, not hashes independently checked here;
* no fresh archive or primary-literature search is claimed.

The analytic tools used below are the supplied positive-measure convexity and loop-equation framework. The arithmetic transfer uses the supplied finite contact reconstruction and prime-power factorial stripping. No novelty claim is inferred from this review.

---

# Part I. The quantitative COMMON error law

## 2. What has to be proved beyond centered comparison

Write


$$
\sigma=\sqrt2,\quad M=1+\sqrt2,\quad \rho=M^{-1},
\quad c=\frac dn,\quad
\alpha=\frac{\sigma}{M},\quad \beta=\sigma M.
$$



The original finite systems remain


$$
H_b,T:\{0,\ldots,d\}^2,\qquad
K:\{0,\ldots,b\}\times\{0,\ldots,d\}.
$$


Nothing below replaces a finite inverse by an infinite one.

The accepted centered estimate controls


$$
\log\frac{F_j/F_b}{P_j/P_b}.
$$


It does not determine


$$
\mathcal C_{n,d}
=\frac{F_b/P_b}{4\pi M^{-2n-b}}.
$$


A3 correctly introduces a separate proof of the latter.

The genuinely new estimate needed for that proof is


$$
\boxed{
(\log A_b)'(q)-dL_c'(q)=O(c)
}
\tag{2.1}
$$


on fixed complex neighborhoods of $M,\rho$, uniformly for every $d\ge2$ in the small-ratio strip.

An $O(1)$ bound would not suffice: moving the saddle by $O(c)$ would then leave an uncontrolled $O(c)$ contribution, precisely at the scale of the claimed coefficient $-1$.

---

## 3. Wall estimates: the all-$d$ argument passes

The unperturbed rescaled positive ensemble has density


$$
\Delta(u)^2e^{-d\sum_iW_c(u_i)}
$$


on its original ordered chamber, where


$$
W_c(u)=
\frac{\log(1+cu^2)-\log(1-cu^2/M^2)}c
+\log(1+cu^2).
$$


The retained bounds give


$$
W_c''\ge\frac1{16},\qquad
\max_i|a_i^\circ|\le16
$$


for its joint mode $a^\circ$, and Gaussian radial domination about that mode with covariance $16I/d$.

### 3.1 Why the marginal contraction inequality is legitimate

Let $\varrho$ be the normalized joint density, and fix a coordinate $i$. For $0<s\le1$, the map


$$
u\longmapsto a^\circ+s(u-a^\circ)
$$


preserves the convex ordered chamber.

Convexity of the energy and minimality at $a^\circ$ give


$$
\varrho(a^\circ+s(u-a^\circ))\ge \varrho(u).
$$


Applying this map to the slice $u_i=24$, its $(d-1)$-dimensional Jacobian is $s^{d-1}$. The image is contained in the slice


$$
u_i=a_i^\circ+s(24-a_i^\circ).
$$


Therefore


$$
p_i(a_i^\circ+s(24-a_i^\circ))
\ge s^{d-1}p_i(24).
\tag{3.1}
$$



The center here is the **joint mode coordinate**. It need not be a mode of the one-dimensional marginal. That distinction causes no problem because the proof is by contraction of joint-density slices.

For


$$
1-\frac1{40d}\le s\le1,
$$


the resulting interval has length at least $1/(5d)$, lies above $23$, and $s^{d-1}\ge1/2$. Hence


$$
p_i(24)\le10d\,\mathbb P(u_i\ge23).
\tag{3.2}
$$



Since $a_i^\circ\le16$, the event on the right implies


$$
\|u-a^\circ\|\ge7.
$$


The radial tail thus yields


$$
p_i(24)\le Cd\,e^{-\gamma_7d},
\quad
\gamma_7=\frac12\left(\frac{49}{16}-1-\log\frac{49}{16}\right)>0.
\tag{3.3}
$$


The negative wall is treated similarly.

### 3.2 Conditioning does not introduce a small-$d$ denominator

Let


$$
E=\{\max_i|u_i|\le24\}.
$$


Its complement implies $\|u-a^\circ\|>8$, so


$$
\mathbb P(E^c)
\le
\exp\left[-\frac d2(4-1-\log4)\right].
$$


For all $d\ge2$, this is bounded strictly below one by a fixed constant. Thus


$$
\mathbb P(E)\ge c_*>0
$$


uniformly, and conditioning only multiplies the wall estimates by $c_*^{-1}$.

Consequently


$$
\boxed{
\sum_i\bigl(p_i^{[24]}(24)+p_i^{[24]}(-24)\bigr)
\le Cd^2e^{-\gamma_7d}.
}
\tag{3.4}
$$



This estimate is valid for bounded $d$. It is not necessary that the wall probability itself tend to zero with $n$.

---

## 4. Explicit loop coercivity and absorption for every $d\ge2$

The source invokes a corrected image-coercivity estimate. Here is a direct justification adequate for the specific resolvent difference.

Let


$$
\mathscr W(z)=\mathbb E^{[24]}\sum_{i=1}^d\frac1{z-u_i},
\qquad
h(z)=\mathscr W(z)-dR_c(z),
$$


and take


$$
\Gamma=\{|z|=30\}.
$$


The signed measure represented by $h$ has total mass zero. Both component measures are supported inside $[-24,24]$, with the equilibrium support inside $[-2,2]$.

The linearized loop operator has the form


$$
K_ch(z)
=
(2R_c(z)-W_c'(z))h(z)
+
\int
\frac{W_c'(z)-W_c'(u)}{z-u}\,d\nu(u),
\tag{4.1}
$$


where $h(z)=\int(z-u)^{-1}d\nu(u)$.

The exact conditioned loop equation, up to the immaterial sign convention for the wall term, is


$$
dK_ch+h^2+C(z,z)=J_{d,c}(z).
\tag{4.2}
$$



### 4.1 The quadratic part has a uniform margin

Put


$$
a=1+M^{-2}=4-2\sqrt2.
$$


At $c=0$,


$$
W_0'(z)=2az.
$$


The divided-potential term for this quadratic potential is


$$
2a\int d\nu=0.
$$



On $\Gamma$,


$$
|R_c(z)|\le\frac1{28},
$$


because its measure has mass one and support in $[-2,2]$. Therefore


$$
|2az-2R_c(z)|
\ge60a-\frac1{14}>70.
\tag{4.3}
$$



### 4.2 The nonquadratic operator is $O(c)$

On any fixed disk, say $|z|\le60$, the displayed rational derivative of $W_c$ gives


$$
W_c'(z)=2az+E_c(z),
\qquad
\sup_{|z|\le60}|E_c(z)|\le Cc,
\tag{4.4}
$$


after reducing $\epsilon$ so that the poles remain outside that disk.

The multiplication contribution is immediately bounded by


$$
Cc\|h\|_\Gamma.
$$



For the divided-potential contribution, write


$$
E_c(z)=\sum_{k\ge0}e_kz^k.
$$


Cauchy estimates on the radius-$60$ disk give


$$
|e_k|\le Cc\,60^{-k}.
$$


The moments $m_\ell=\int u^\ell d\nu(u)$ satisfy


$$
m_\ell=\frac1{2\pi i}\int_\Gamma z^\ell h(z)\,dz,
\qquad
|m_\ell|\le30^{\ell+1}\|h\|_\Gamma.
$$


Since $m_0=0$, expansion of


$$
\frac{E_c(z)-E_c(u)}{z-u}
$$


and summation of the resulting convergent geometric series show


$$
\sup_\Gamma
\left|
\int\frac{E_c(z)-E_c(u)}{z-u}\,d\nu(u)
\right|
\le Cc\|h\|_\Gamma.
\tag{4.5}
$$



Equations (4.3)–(4.5) imply, for a sufficiently small fixed $\epsilon$,


$$
\boxed{
\|K_ch\|_\Gamma\ge68\|h\|_\Gamma.
}
\tag{4.6}
$$


This is an image estimate for the actual zero-mass resolvent difference. It asserts neither surjectivity nor an inverse on an unspecified function space.

### 4.3 Direct absorption is valid at small $d$

The support bounds give the a priori estimate


$$
H:=\|h\|_\Gamma
\le d\left(\frac16+\frac1{28}\right)
=\frac{17}{84}d<\frac d4.
\tag{4.7}
$$



Positive-measure Brascamp–Lieb gives


$$
\|C\|_\Gamma\le C,
$$


while (3.4) gives


$$
\|J_{d,c}\|_\Gamma\le Cd^2e^{-\gamma_7d}.
$$


Thus


$$
H\le\frac1{68d}
\left(H^2+C+Cd^2e^{-\gamma_7d}\right).
$$


By (4.7),


$$
\frac{H^2}{68d}\le\frac{H}{272}.
$$


Absorption proves


$$
\boxed{
H\le \frac Cd+Cd\,e^{-\gamma_7d},
\qquad d\ge2.
}
\tag{4.8}
$$



This closes the potential small-dimension gap. No empirical-measure limit is used.

---

## 5. Symmetric-test cancellation and the $O(c)$ bias

The characteristic derivative test is


$$
f_{c,q}(u)
=
\frac{1+i\sqrt c\,u}
{(1+q)+i(q-1)\sqrt c\,u}.
$$


The finite unperturbed ensemble, its symmetric conditioning, and its equilibrium measure are invariant under reflection of the particle configuration. Thus only the even part contributes:


$$
f_{c,q}^{\rm ev}(u)
=
\frac{(1+q)+(q-1)cu^2}
{(1+q)^2+(q-1)^2cu^2}.
$$


Subtracting its constant value gives


$$
\boxed{
f_{c,q}^{\rm ev}(u)-\frac1{1+q}
=
\frac{2(q-1)cu^2}
{(1+q)\bigl((1+q)^2+(q-1)^2cu^2\bigr)}.
}
\tag{5.1}
$$



On $|u|=30$, this is $O(c)$, uniformly on sufficiently small fixed anchor disks. The constant term integrates to zero against the mass-zero resolvent difference. By Cauchy integration and (4.8),


$$
\left|
\mathbb E^{[24]}\sum_i f_{c,q}(u_i)
-dL_c'(q)
\right|
\le
Cc\left(d^{-1}+de^{-\gamma_7d}\right)
\le Cc.
\tag{5.2}
$$



### Removing the conditioning

On the full real principal interval,


$$
\left|f_{c,q}^{\rm ev}(u)-\frac1{1+q}\right|
\le Ccu^2.
$$


The radial bound supplies


$$
\mathbb E\left(\sum_i u_i^2\right)^2\le Cd^2.
$$


The covariance identity for conditioning, followed by Cauchy–Schwarz, bounds the change in expectation by


$$
Cc\,d\,e^{-\gamma d/2}\le Cc.
\tag{5.3}
$$



The crucial factor is still $c$. For fixed $d$, the wall probability need not vanish as $n\to\infty$, but the centered even test does vanish at order $c$. This is why the argument covers arbitrarily slow growth and bounded dimension.

---

## 6. Positive tilts and the actual phase

For complex $q$ in the anchor disks, the real modulus-tilt potential satisfies


$$
|h_q'|\le C\sqrt c,\qquad |h_q''|\le Cc.
$$


The positive interpolation retains Hessian lower bound $kdI$.

For


$$
F_q=\sum_i f_{c,q}(u_i),
$$


one has


$$
\sum_i|\partial_iF_q|^2\le Cdc.
$$


Componentwise Brascamp–Lieb therefore gives


$$
\operatorname{Var}_{\mathbb C}(F_q)\le Cc.
$$


The same bound holds for the real tilt statistic. Differentiating the positive interpolation yields a covariance bounded by $Cc$, so it changes the mean by $O(c)$.

For the phase, put


$$
w=e^{i(\Phi_q-\mathbb E_q\Phi_q)},\qquad N_q=\mathbb E_qw.
$$


The phase is real under the positive modulus measure. Its particle derivatives are $O(\sqrt c)$, so


$$
\operatorname{Var}(\Phi_q)\le Cc,
\qquad
|N_q-1|\le \tfrac12\operatorname{Var}(\Phi_q)\le Cc,
$$


and


$$
\operatorname{Var}_{\mathbb C}(w)\le Cc.
$$


After shrinking $\epsilon$, $|N_q|\ge1/2$. Consequently


$$
\left|
\frac{\mathbb E_q(wF_q)}{N_q}-\mathbb E_qF_q
\right|
\le Cc.
\tag{6.1}
$$



These are all estimates under positive measures; no signed-measure Brascamp–Lieb assertion is used.

The differentiated outer-sector remainder is of the retained form


$$
C(1+n+d)^K e^{-\eta n+C_0d}
$$


with fixed $K$. It is $O(c)$ uniformly on the strip, since $c=d/n\ge2/n$.

Combining these steps proves (2.1). Cauchy estimates on smaller anchor disks also give


$$
\partial_q^m\bigl((\log A_b)'-dL_c'\bigr)=O_m(c).
\tag{6.2}
$$



**Audit result:** the exact slow-growth characteristic-bias obligation is met.

---

## 7. The common coefficient: three contributions, not one

The accepted exact equilibrium stationary-value identity is indispensable here. I reuse it at its stated scope rather than infer it from a qualitative saddle estimate.

### 7.1 Reciprocal-anchor phase correction

At the real reciprocal anchors the positive measures coincide. With


$$
X=\sum_i\theta_i,\qquad
\eta_q=-\sigma-\frac1{1+q},
$$


the original-chamber cutoff translation calculation gives


$$
\operatorname{Var}(X)
=\frac c\alpha+O(c^2+c/n)+O(e^{-\kappa n}).
\tag{7.1}
$$



The cutoff is necessary: the singular full score cannot be assigned a globally bounded cubic remainder. The fixed-angle exceptional event has bound


$$
\exp\{-Kn+O(d\log(1/c))+O(d)\},
$$


which becomes $e^{-\kappa n}$ for one fixed small $\epsilon$. This is uniform down to $d=2$.

Reflection, the odd phase remainder, and the fourth-moment bound give


$$
\log\mathbb E e^{i\Phi_q}
=-\frac12\eta_q^2\operatorname{Var}(X)+O(c^2).
$$


Since


$$
\eta_\rho^2-\eta_M^2=3-\sigma,
$$


the anchor contribution is


$$
\boxed{
\log\frac{A_b(\rho)}{A_b(M)}+d\log M
=
-\left(1+\frac{\sigma}{4}\right)c
+O(c^2+c/n)+O(e^{-\kappa n}).
}
\tag{7.2}
$$



### 7.2 Actual stationary values

Set


$$
D_c(q)=\log A_b(q)-dL_c(q).
$$


The new estimate proves $D_c'=O(c)$.

The exact equilibrium radii are


$$
r_+(c)=\frac2{2+c},\qquad
r_-(c)=\frac{2M}{2M-c},
$$


and their stationary-value difference is exactly


$$
\Phi_+(r_+)-\Phi_-(r_-)=(2+c)\log M.
\tag{7.3}
$$



Because the actual radial curvature is comparable to $n$,


$$
r_{b,\pm}-r_\pm(c)=O(c/n).
$$


The displacement from an anchor to its equilibrium saddle is $O(c)$, so the $D_c$-increment is $O(c^2)$. Moving to the actual saddle costs only $O(c^2/n)$.

Thus the full stationary-value difference is


$$
\boxed{
G_-(r_{b,-})-G_+(r_{b,+})
=
-(2n+d)\log M
-\left(1+\frac{\sigma}{4}\right)c
+O(c^2+c/n)+O(e^{-\kappa n}).
}
\tag{7.4}
$$



There is no surviving uncontrolled $nc^2$ term. Its exclusion comes from the **exact** identity (7.3), not from separately estimating two saddle shifts.

### 7.3 Gaussian curvature correction

The curvature expansions are


$$
\lambda_+
=\alpha\left(1+\frac{\sigma c}{4}\right)
+O(c^2+c/n),
$$




$$
\lambda_-
=\beta\left(1-\frac{\sigma c}{4}\right)
+O(c^2+c/n).
$$


Hence


$$
\boxed{
\log\sqrt{\lambda_+/\lambda_-}
=
-\log M+\frac{\sigma c}{4}
+O(c^2+c/n).
}
\tag{7.5}
$$



The Gaussian factor cancels the $-\sigma c/4$ portion of (7.2), leaving $-c$.

### 7.4 First scalar saddle correction

For the whole stationary exponent $G=n\psi$,


$$
\int e^{G(\theta)}\,d\theta
=
e^{G(0)}\sqrt{\frac{2\pi}{n\lambda}}
\left[
1+\frac1n\left(
\frac{\psi_4}{8\lambda^2}
+\frac{5\psi_3^2}{24\lambda^3}
\right)+O(n^{-2})
\right].
\tag{7.6}
$$



The sign of the cubic-square term is correctly written: $\psi_3$ is generally imaginary, so $\psi_3^2$, not $|\psi_3|^2$, occurs.

For a rigorous uniform remainder, fixed-order holomorphic derivative bounds through sufficiently high order—eight orders are more than sufficient—are obtained on smaller disks. Expand on a shrinking central window after $x=\sqrt n\,\theta$; outside it use the fixed Gaussian curvature bound. Odd orders integrate to zero on the symmetric window. This produces the asserted relative $O(n^{-2})$ remainder without a modulus-only saddle argument.

At $c=0$, the cubic derivatives vanish and


$$
B_\pm(0)=\frac1{8\lambda_\pm(0)}-\frac38.
$$


Therefore


$$
B_-(0)-B_+(0)
=\frac18\left(\frac1\beta-\frac1\alpha\right)
=-\frac{\sigma}{8}.
$$


The scalar correction is


$$
\boxed{
-\frac{\sigma}{8n}+O(c/n+n^{-2}).
}
\tag{7.7}
$$



Combining (7.4), (7.5), (7.7), and the exact normalization $4\pi$ proves


$$
\boxed{
\log\mathcal C_{n,d}
=
-c-\frac{\sigma}{8n}
+O(c^2+c/n+n^{-2})+O(e^{-\kappa n}).
}
\tag{7.8}
$$



---

## 8. Contours, full forcing, endpoint, and both parities

### 8.1 Both minus connectors are retained

The minus integral is an open arc. Deforming it requires both radial connectors at $\arg\zeta=\pm\pi/4$. Their base factor is


$$
h(re^{\pm i\pi/4})
=
\frac{r+r^{-1}}2-1
\pm i\frac{r-r^{-1}}2.
$$


At $r=1$, it vanishes. For the small saddle displacement, its modulus is uniformly much smaller than the central base value.

The supplied connector and remote-arc estimates include the characteristic insertion. Their fixed polynomial prefactors are absorbed by reducing the exponential constant. I retain the simpler valid remainder $Ce^{-\kappa n}$, rather than attach significance to the displayed power six.

### 8.2 Coordinate transfer

The accepted centered theorem gives, in particular,


$$
\log\frac{F_j/F_b}{P_j/P_b}=O(d/n^2)+O(e^{-\kappa n}).
$$


This is within the remainder in (1.1). A3’s weaker direct insertion argument also suffices.

### 8.3 The whole error is not just $F_j/P_j$

The exact error remains


$$
\boxed{
e_j=
\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac D{P_j},
}
\tag{8.1}
$$


where


$$
eE_i
=-[z^{n+i}](1-z+z^2/2)^n
\int_0^1s^ne^{1-s+sz}\,ds
$$


and


$$
E_j=\nu_{n,d}\!\left(
R_j\sum_{i=0}^d\sigma^ie_{d-i}(z^{-1})eE_i
\right).
$$



The retained residual bounds give relative size


$$
CM^{2n+b}
\left(
\frac{2^d}{n!\sqrt n}
+\frac{\sqrt n}{n!B_0}
\right),
\qquad B_0=(n)_d\sigma^{-d}.
$$


Uniformly on $d\le\epsilon n$, its logarithm is at most


$$
-n\log n+O(n).
$$


Thus it is absorbed into the exponential remainder.

For sufficiently small $\epsilon$ and sufficiently large $N$, the normalized scalar factor is bounded away from zero. Consequently:

* every $P_j$ remains nonzero under the retained normality/saddle interfaces;
* every whole error is nonzero;
* its sign is exactly $(-1)^{n+1}$;
* coordinate zero’s endpoint is included;
* both parities are covered.

For a positive diagonal metric,


$$
c_W-S=\sum_j\omega_je_j,\qquad
\omega_j=\frac{W_{jj}u_j^2}{u^TWu}>0,\qquad
\sum_j\omega_j=1.
$$


Uniformity in $j$ proves the same expansion for $c_W-S$, independently of the positive weight ratios.

### Strongest proved analytic scope

At the retained exact interfaces, (1.1) is proved uniformly on the small fixed strip. On every allocation $2\le d=o(n)$,


$$
1-\frac{e_j}{(-1)^{n+1}4\pi M^{-2n-b}}
=
\frac{d+\sqrt2/8}{n}(1+o(1)).
$$


On a strip with $d/n$ bounded away from zero, the displayed first-order expansion remains a uniform estimate with $O(c^2)$ uncertainty; it is not an asymptotic equivalence for the first correction.

---

# Part II. The completed universal prime-$29$ calculation

## 9. Domain and what the calculation actually certifies

Here $d$ has a different meaning from Part I. It is the low digit in


$$
h=29H+d.
$$


The original arithmetic family remains


$$
p=29,\qquad b=3^a,\qquad n=2001b,
$$




$$
a\ge1,\qquad a\equiv432827\pmod{682892},
$$


with finite contact indices $0\le i,j<b$ and actual coordinates $0\le j\le b$.

The metric is falling-factorial:


$$
\omega_j=j!\binom{n+2}{j}=(n+2)_{\underline j},
\qquad \Omega=\operatorname{diag}(\omega_j^2).
$$



The calculation uses the auxiliary odd representative


$$
b^\circ=1395217,\qquad n^\circ=2791829217.
$$


It is not an original power-$3$ index. Its role is to evaluate universal bounded low-block coefficients whose parameter transfer is separately justified.

The supplied independent crosscheck certifies agreement in:

* all 27 universal constants;
* all 25 ordinary contractions;
* the finite pass through all $707281$ low coordinates.

That closes the finite task. It does not by itself prove the infinite reconstruction transfer.

---

## 10. The actual $q=-2$ boundary and normalization precision

The complete raw boundary coefficient is


$$
t_{-k}(x)=E_k+x(E_k+E_{k-1}),
\qquad 0\le k\le60,
\tag{10.1}
$$


modulo $p^4$, with $E_{-1}=E_{60}=0$.

At $k=2$, the slope $E_2+E_1$ is a unit. Thus replacing $x$ by $x\bmod p^2$ is generally invalid.

The coordinator source uses
```text
boundary = (ee[k] + x*(ee[k]+ee[k-1])) % L
```
with the **full vector $x=0,\ldots,L-1$**. The sliding-window implementation maintains the equivalent affine recurrence modulo $L=p^4$. These both preserve the required boundary.

### 10.1 Exact division rule

If a raw coefficient is known modulo $p^m$, and normalization multiplies it by $p^\Delta$, then its normalized value modulo $p^2$ is determined only if


$$
m+\Delta\ge2.
\tag{10.2}
$$


When $\Delta<0$, divisibility by $p^{-\Delta}$ must also be checked before division.

Here


$$
z_A=p^{c_{xq}-2}a_q(x),\qquad
z_Q=p^{c_{xq}-3}y_q(x).
$$



The precision requirements are therefore:

| Term | Available raw precision | Required carry/precision condition |
|---|---:|---|
| $A$, $q\ge0$ | $p^2$ | $c_{xq}\ge2$ |
| positive $Q$ contact | $p^3$ | $c_{xq}\ge2$ |
| $Q$, $q=0$, contact plus boundary | at least $p^3$ | actual carry suffices; no use of a fictitious $p^4$ contact precision |
| negative $Q$ boundary | $p^4$ | $c_{xq}\ge1$ |
| $q=-2$, carry one | $p^4$ | exact division of the whole coefficient by $p^2$ |

The coordinator deliberately marks $q=0$ as precision three despite adding a precision-four boundary representative. This is correct.

The receipt reports no precision obstruction and successful exact divisions. Zero coefficients are not used as a reason to bypass a missing precision requirement.

### 10.2 Counts and integer safety

The coordinator records


$$
128725142=2\cdot707281\cdot91
$$


normalization checks because it also checks the identically zero $A$-entries at negative Laurent powers. The streaming implementation’s nontrivial $A$-count is instead $707281\cdot31$. This is a bookkeeping difference, not a discrepancy.

The displayed NumPy calculation uses signed 64-bit integer arrays, but its modular reductions keep all products safely below overflow. For example:

* the unreduced affine boundary product is below $10^{12}$;
* normalized slot products are below $10^9$;
* shape sums are below $10^{12}$.

Thus the displayed operations are genuinely exact integer arithmetic at their stated bounded ranges, not floating-point approximations or overflowing modular arithmetic.

---

## 11. From the finite constants to an ordinary polynomial identity

The only nonzero divided flat entries are


$$
203/29=7,\qquad 638/29=22,
$$


and every harmonic entry is zero. Therefore the universal reconstruction gives


$$
R_C(D,J)=7(D+7-J)^2+22(3-J)^2.
\tag{11.1}
$$



The norm polynomial is


$$
K_D(J)=11(D+7-J)^2+18(3-J)^2.
$$


Since


$$
27\cdot11\equiv7,\qquad
27\cdot18\equiv22\pmod{29},
$$


we obtain the coefficientwise identity


$$
\boxed{R_C(D,J)=27K_D(J).}
\tag{11.2}
$$



Expanding (11.1) gives


$$
R_C(D,J)=7D^2+15DJ+11D+2J+19.
\tag{11.3}
$$


In particular the $J^2$-coefficient vanishes because $7+22=29$.

This is stronger than agreement at field values. No quotient by $J^{29}-J$ has been used.

### Ordinary differentiation

For example,


$$
\partial_JR_C(D,J)=15D+2,
$$


which agrees with


$$
27\,\partial_JK_D(J).
$$


The functional $\mathcal L_d$ therefore annihilates $R_C(d,\cdot)$ because it annihilates $K_d$:


$$
\Gamma _0(d)=27\mathcal L_d(K_d)=0.
\tag{11.4}
$$



The 25 contractions are thus consequences of one ordinary polynomial identity and the normalization of $\mathcal L_d$, not merely a collection of unrelated zeros.

---

## 12. Why the finite coefficient calculation transfers

Three distinct transfers must not be conflated.

### 12.1 Bounded contact/kernel transfer

The retained contact proof works coefficientwise in the integral Newton representation and retains


$$
\binom{b-1-X+s}{v+i}
$$


from the actual finite endpoint.

For bounded lower indices $k<p^2$, a parameter shift by $p^4t$ changes a binomial coefficient by a multiple of $p^3$:


$$
\binom{z+p^4t}{k}\equiv\binom zk\pmod{p^3}.
$$


For $k<p$, the stronger modulus $p^4$ holds.

The contact coefficients supply the extra powers of $p$ required by the kernel precisions. The boundary rising products retain their actual valuation factors. This justifies transfer of the bounded kernel data within the fixed low-digit cylinder, with odd parity preserved.

### 12.2 The low-polynomial calculation retains high variables before specialization

Four-level stripping gives the natural multiplier


$$
(N-J)^e(2N+h-J+1)^u(h-J)^{r_q}.
$$


The table uses formal $D,J$ only after the aggregate residual has been formed.

Why is $N=3,\ h=D$ then permissible? The leading contracted norm–mixed difference is a sum of the two relevant squared linear factors with coefficients


$$
g_e-\kappa_e/6
$$


divisible by $p$. Replacing $N,h$ by congruent values modulo $p$ changes those squared factors by multiples of $p$, hence changes this leading residual only modulo $p^2$. The harmonic corrections already carry an explicit factor $p$.

Thus the residual divided by $p$, modulo $p$, depends only on


$$
N\bmod p=3,\qquad h\bmod p=d.
$$



This argument requires the natural leading-column identities as ordinary polynomial identities. The supplied inspected pass checks the corresponding slot identities at every low row, including the vanishing leading $r=1$ slots and the two-shape support. The retained reconstruction and coefficient-period argument are what transfer those finite low-row checks; the leading scalar constants alone would not suffice.

### 12.3 Exact high-index boundaries

The actual ranges are


$$
0\le J\le h\quad(x\le b_*),\qquad
0\le J\le h-1\quad(x>b_*).
$$


For $x>b_*$, the positive $P$-reconstruction carries an actual factor $h-J$. Consequently both norm and mixed contractions acquire zero at the added endpoint $J=h$. Only after retaining this factor may one use a common upper range.

The original endpoint remains


$$
Y_b=W_b(1+b\theta^Q_{b-1}),
$$


including the $1$.

**Transfer verdict:** the finite table has the intended infinite-family meaning at the retained finite reconstruction and whole-force interfaces. It is not a universal consequence of numerical agreement alone.

---

## 13. Precision three and the residual contraction

The universal table determines $P,Q\bmod p^2$. The third-defect theorem needs a stronger justification modulo $p^3$. The supplied A2 argument retains:

* $Z_w\bmod p^5$ and $Y\bmod p^6$;
* positive Newton degree through $86$;
* boundary factorial indices through $88$;
* negative Laurent powers through $-89$;
* the complete logarithmic-force valuation bound;
* the unfrozen high-part boundary correction.

In particular,


$$
j=x+p^4J
$$


cannot be frozen entirely at precision three. The omitted term would be


$$
\delta Y_{p^4J+x}
\equiv(-1)^{j+1}p^4J\,W_jB_{-2}(j)\pmod{p^6}.
\tag{13.1}
$$


It contributes to the second residual polynomial, not to the $R_C$ table.

Write


$$
\sum_x(P_xQ_x-c_0P_x^2)
=p\widetilde R(J)+p^2\widetilde S(J)\pmod{p^3},
\qquad c_0=(6C_n)^{-1}.
$$


Then


$$
M-c_0D
\equiv
p\sum_JF(J)^2\widetilde R(J)
+p^2\sum_JF(J)^2\widetilde S(J)
\pmod{p^3}.
\tag{13.2}
$$



On $T=0$, the leading Lucas contraction kills the second sum modulo $p$. This is why (13.1), though necessary in the proof, does not alter the third-defect answer.

For admissible $t$,


$$
0\le t\le3,\qquad 0\le d-t\le22,
$$


the retained first-order digit expansion gives


$$
F(pk+t)^2
\equiv
w_tX_k^2\bigl(1+2p(E_t+kr_t)\bigr)\pmod{p^2},
$$


and ordinary Taylor expansion gives


$$
\widetilde R(pk+t)
\equiv\widetilde R(t)+pk\widetilde R'(t)\pmod{p^2}.
$$


Therefore


$$
\frac{M-c_0D}{p^2}
=
r_0T_1+r_1U\pmod p,
\tag{13.3}
$$


where


$$
r_0=\sum_{\rm adm.\ t}w_tR(t),
\qquad
r_1=\sum_{\rm adm.\ t}w_t\bigl(R'(t)+2r_tR(t)\bigr).
$$



On $D_1=0$,


$$
T_1=-\frac{\beta(d)}{f(d)}U.
$$


The division is legitimate for $0\le d\le24$: the supplied contraction certificate gives $f(d)\ne0$ in every one of these cases.

Using


$$
R=C_nR_C+J_{29}R_{29}
=(27C_n+20J_{29})K_d,
$$


we obtain


$$
r_1-r_0\frac{\beta(d)}{f(d)}=0.
$$


This proves (1.3).

No recomputation of $\Gamma _1$ is required.

---

## 14. Exact conditional theorem and population status

### Conditional third-defect theorem

For the original family


$$
b=3^a,\quad n=2001b,\quad
a\equiv432827\pmod{682892},
$$


retain the stated finite reconstruction and complete-force identities. If


$$
0\le d\le24,\qquad T=0,\qquad D_1=0,
$$


then


$$
D,M\in29^2\mathbb Z_{29},
\qquad
\frac M{29^2}
\equiv(6C_n)^{-1}\frac D{29^2}\pmod{29}.
\tag{14.1}
$$



Since $C_n$ is a unit:

* if $D/29^2\not\equiv0\pmod{29}$, then
  

$$
v_{29}(D)=v_{29}(M)=2;
$$


* if $D/29^2\equiv0\pmod{29}$, then
  

$$
v_{29}(D),v_{29}(M)\ge3.
$$



The second alternative is only simultaneous passage to the next depth. It is not equality of the two valuations beyond that depth.

### Which infinite-family facts are proved?

The low-digit reachability statement is proved:


$$
a=432827+682892t
\quad\Longrightarrow\quad
d(t)=16-t\pmod{29}.
$$


Thus every $d\in\{0,\ldots,28\}$, and in particular every eligible $d\le24$, occurs infinitely often on the original progression.

What remains unproved is simultaneous reachability of the residual conditions


$$
T=0,\qquad D_1=0.
$$


The completed $\Gamma _0$ table places no restriction on whether these conditions occur.

For this zero-defect theorem, $U\ne0$ is **not** an additional hypothesis. It would have mattered in using a nonzero table entry to construct a defect, but the completed table vanishes.

The cases $d=25,26,27,28$ are not covered by the stated theorem. The polynomial identity (11.2) does not authorize dividing by $f(d)$ or extending the residual interface outside its established eligible range.

---

# Part III. Primitive denominators and the remaining research bottleneck

## 15. Both norm and mixed depths are indispensable

Retain


$$
N_B=d_B[u,v],
\quad
A_B=N_{B,1}^T\Omega N_{B,1}>0,
\quad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),
\qquad
q_B=A_B/g_B,\qquad p_B=H_B/g_B.
$$


The primitive multiplier is $1/g_B$ on the integer Gram pair and $d_B^2/g_B$ on the rational Gram pair.

For the prime-$29$ family, let


$$
\delta=v_{29}(D),\qquad \mu=v_{29}(M),
\qquad F_n=v_{29}(n!),\quad F_b=v_{29}(b!).
$$


The exact retained formulas are


$$
v_{29}(g_B)
=
\min\{4F_n+4+\delta,\;2F_n+F_b+5+\mu\},
$$




$$
\boxed{
v_{29}(q_B)
=
\max\{0,\;2F_n-F_b-1+\delta-\mu\}.
}
\tag{15.1}
$$



If the third-defect theorem gives $\delta=\mu=2$, then their contribution cancels in the difference:


$$
v_{29}(q_B)=\max\{0,2F_n-F_b-1\}.
$$


If it gives only $\delta,\mu\ge3$, no corresponding upper bound on $\delta-\mu$ follows.

Increasing the norm depth alone cannot be read as increased cancellation in the denominator. The mixed depth must be known at the same index.

### All primes and the full gcd

For the actual reduced fraction,


$$
\boxed{
\log q_B
=
\sum_{\ell\ {\rm prime}}
\max\{0,v_\ell(A_B)-v_\ell(H_B)\}\log\ell.
}
\tag{15.2}
$$


The completed prime-$29$ table controls only a finite-depth portion of one summand. It does not determine (15.2).

Norm nonvanishing is supplied by positivity. Any use of finite mixed valuation retains the stated original-family mixed-nonvanishing dependency.

---

## 16. The whole evaluated form must remain attached to its own family

The exact primitive form is


$$
\boxed{
q_B(e+\pi)-p_B=q_B(S-c_\Omega).
}
\tag{16.1}
$$



For the sublinear analytic family, the reviewed COMMON law gives


$$
q_BS-p_B
=
(-1)^n4\pi q_BM^{-2n-b}
\left[
1-\frac dn-\frac{\sqrt2}{8n}
+O\!\left(\frac{d^2+d+1}{n^2}\right)
+O(e^{-\kappa n})
\right].
\tag{16.2}
$$



For the prime-$29$ family $n=2001b$, the retained fixed-ratio whole-error theorem is the relevant input:


$$
\epsilon_n=c_\Omega-S>0\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)n\log M+o(n).
\tag{16.3}
$$


Its evaluated form is $-q_B\epsilon_n$.

The new small-strip COMMON expansion is not a reason to replace the fixed-ratio theorem by a sublinear equivalence. Its strip constant has not been numerically certified to include any particular fixed ratio, and the two statements have different asserted scopes.

If $S=a/t$ were rational, every nonzero integer form $q_BS-p_B$ would have absolute value at least $1/t$. The desired contradiction therefore still requires an infinite admissible same-index sequence with


$$
q_B|S-c_\Omega|\longrightarrow0.
\tag{16.4}
$$


Neither new result establishes this.

---

## 17. Concrete follow-on lemmas

Two separate follow-on obligations are now appropriate.

### 17.1 Local arithmetic: joint population and deeper alignment

A precise population target is:

> **Joint residual-population lemma.**  
> Determine whether infinitely many
> 

$$
> a=432827+682892t,\qquad t\ge0,
>
$$


> satisfy $d\le24$ and
> 

$$
> \mathcal T\equiv0\pmod{29},\qquad
> f(d)\,\frac{\mathcal T}{29}+\beta(d)U\equiv0\pmod{29}.
>
$$



Here


$$
A=69h+67,\qquad h=29H+d,
$$




$$
X_k=\binom Ak\binom{2A+H-k}{H-k},
\quad
\mathcal T=\sum_{k=0}^H X_k^2,
\quad
U=\sum_{k=0}^HkX_k^2\pmod{29}.
$$



A useful first proof step is an exact digit recursion for the pair


$$
(\mathcal T\bmod29^2,\ U\bmod29)
$$


with the relation $A=2001H+69d+67$ built in. Such a recursion must retain carries and terminal ranges. Low-digit reachability of $d$ alone does not prove this lemma.

Separately, all-depth denominator control would require a theorem bounding $\delta-\mu$, not just another simultaneous lower-depth result.

### 17.2 Global arithmetic: uncancelled cofactor

The decisive global target remains a bound on


$$
\sum_\ell
\max\{0,v_\ell(A_B)-v_\ell(H_B)\}\log\ell
$$


on an infinite admissible sequence.

For the sublinear family, a sufficient statement is


$$
\log q_B-(2n+b)\log M\longrightarrow-\infty.
$$


For the prime-$29$ fixed-ratio family, a robust sufficient statement is


$$
\log q_B
\le
\left[
\left(2+\frac1{2001}\right)\log M-\delta_0
\right]n
$$


for some fixed $\delta_0>0$, jointly with the retained whole-error theorem.

A common-divisor construction may prove this without explicitly computing the full gcd: exhibit $G_B\mid A_B,H_B$ with $A_B/G_B$ sufficiently small. But it must include enough primes to control the actual cofactor.

---

## 18. Bounded exact arithmetic: what is and is not still needed

### No repeat of the universal pass is mathematically required

The $707281$-row universal calculation has completed twice and agrees. Repeating it would be replication, not the outstanding mathematical step.

No finite calculation is needed for the uniform analytic proof above.

### Small optional audit certificate

A compact independent certificate can check the algebraic end of both new results.

**Inputs**

1. In $\mathbb Q(\sqrt2)$:
   

$$
\eta_q=-\sqrt2-\frac1{1+q},\quad
   \alpha=\sqrt2/M,\quad\beta=\sqrt2M,
$$


   and the two displayed curvature derivatives.
2. In $\mathbb F_{29}[D,J]$:
   

$$
R_C=7(D+7-J)^2+22(3-J)^2,
$$


   

$$
K_D=11(D+7-J)^2+18(3-J)^2.
$$


3. The 25 supplied $f(d),\beta(d)$ values.

**Exact divisions**

* only nonzero algebraic denominators in $\mathbb Q(\sqrt2)$;
* the integer divisions $203/29=7,\ 638/29=22$;
* inversions of $6$ and of the 25 nonzero $f(d)$ in $\mathbb F_{29}$.

**Expected verifiable output**

* zero remainder for the combined common $c$-coefficient plus $1$;
* zero remainder for the scalar $1/n$-coefficient plus $\sqrt2/8$;
* zero ordinary polynomial $R_C-27K_D$;
* agreement of $\partial_JR_C$ with $27\partial_JK_D$;
* 25 exact zero functional contractions.

**Resources**

Well below $10^5$ small-field or rational-field operations; negligible memory. This is optional verification, not a new population or denominator calculation.

### Optional bounded exploration for the next lemma

To inspect a candidate digit recursion before applying it to original powers, one may enumerate


$$
0\le d\le24,\qquad 0\le H\le840,
$$


set


$$
A=2001H+69d+67,
$$


and compute the exact finite sums $\mathcal T\bmod841$ and $U\bmod29$.

Use the exact rational recurrence


$$
X_{k+1}
=
X_k\,
\frac{(A-k)(H-k)}
{(k+1)(2A+H-k)}
$$


with numerator multiplication followed by verified exact integer division; do **not** invert the displayed denominator modulo $841$.

This entails fewer than $9\times10^6$ recurrence steps. A conservative inspection allocation is one CPU, 256 MiB, and a separately approved wall-time cap. Expected output is a finite residual-state table and the locations of the two congruence conditions, with no predicted population count.

These are auxiliary $(H,d)$ values, not original power-$3$ indices. Such a table can test a proposed recursion only on its enumerated scope; it cannot establish infinite reachability.

---

## 19. Final ledger

### New result and proof status

1. **Analytic:** the strengthened characteristic bias
   

$$
(\log A_b)'-dL_c'=O(d/n)
$$


   is justified uniformly down to $d=2$. The wall conditioning, zero-mass loop coercivity, direct small-$d$ absorption, symmetric-test cancellation, positive interpolation, and phase normalization support A3’s claimed common correction.

2. **Whole error:** at the retained exact interfaces,
   

$$
\frac{e_j}{(-1)^{n+1}4\pi M^{-2n-b}}
   =
   1-\frac dn-\frac{\sqrt2}{8n}
   +O\!\left(\frac{d^2+d+1}{n^2}\right)
   +O(e^{-\kappa n}),
$$


   with full forcing, coordinate-zero endpoint, both minus connectors, both parities, and nonvanishing retained.

3. **Finite arithmetic:** the completed universal receipts certify
   

$$
R_C=27K
$$


   as an ordinary polynomial identity. The actual $x$-dependent $q=-2$ boundary and all normalization precisions are correctly preserved in the displayed coordinator source.

4. **Conditional infinite-family consequence:** the finite table, combined with the retained contact, stripping, precision-three, and whole-force interfaces, proves third-depth alignment on
   

$$
d\le24,\quad T=0,\quad D_1=0.
$$



### Exact remaining bottlenecks

* Simultaneous original-index population of $T=0,D_1=0$ is unproved.
* Third-depth alignment does not imply all-depth control of $\delta-\mu$.
* A one-prime result does not control the sum over all primes in the actual primitive denominator.
* No infinite same-index sequence has been shown to make the **whole nonzero primitive form** tend to zero.



$$
\boxed{\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$


