> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## Status

I can complete the requested audit of the critical two-thirds calculation, within its explicitly stated analytic dependencies. I do **not** obtain an evaluated fifth weighted Schur rank. In particular, I cannot justify either $T_5=0$ or an explicit nonzero entry of $T_5$.

The new arithmetic result below is a bounded lemma: the beta identity evaluates the **complete direct functional** on the extended radical against LOW monomials to fifth-digit precision. This provides an independent, all-pole proof of the required direct annihilation, including the factorial term and endpoint-subtracted polynomial error. It does **not** evaluate the remaining HIGH/LOW Schur contractions.

No conclusion about irrationality of $e+\pi$ follows.

# 1. Weighted arithmetic: notation and retained normalization

Work on


$$
n=4^j+1,\qquad 81\mid j,\qquad
A=n-2,\qquad H=3^{h-1},\qquad
0<D=H-A<H/324.
$$


Put


$$
u=h-1,\qquad
d=\frac{3D}{2}-1,\qquad
\nu=\frac D2-1,\qquad
m=\frac{A+1}{2}.
$$


Here $D$ is even. On the nonempty stated domain, $D\ge2$ and $H>648$, so $u\ge6$.

The actual monomial indices remain


$$
\mathrm{LOW}=\{0,\ldots,d-1\},\qquad
\mathrm{HIGH}=\{d,\ldots,m\}.
$$


The LOW unit space is


$$
U=\langle1,y,\ldots,y^{D-1}\rangle,
$$


and the lifted radical vectors are


$$
z_i=y^i(y-1)^D,\qquad 0\le i<\nu.
$$


For the extended argument also use


$$
w_\nu=y^\nu(y-1)^D,\qquad \deg w_\nu=d.
$$



The primitive polynomial is not replaced by its local normalization:


$$
Q_n=\lambda Q_n^{\rm loc},\qquad
\lambda=L_n/3\in\mathbb Z_3^\times.
$$


I strip $\lambda$ only when discussing the local matrices.

The exact functional is


$$
\begin{aligned}
\mathcal M(F)
={}&-\frac{3^h}{4}\mathfrak f(F)\\
&+\sum_{r=0}^{h}
 \ \sum_{\substack{a\ge1\ {\rm odd}\\3\nmid a\\a3^r\le4n-3}}
3^{h-r}a^{-1}
[y^{(a3^r-1)/2}]
\frac{F(y)-F(-1)}{y+1},
\end{aligned}
\tag{1}
$$


where


$$
\mathfrak f(y^s)=(2s)!.
$$


Thus neither the derangement functional nor a selected-pole substitute is being used.

The five lower layers after the initial division by $3$ have weights


$$
1,\ 3,\ 9,\ 27,\ 81,
$$


at depths $h-1,\ldots,h-5$, with **every** admissible odd unit and the original cutoff $a3^r\le4n-3$.

# 2. New lemma: exact beta annihilation through the fifth direct digit

## 2.1 Audit of the beta valuation

For integers $s,H\ge0$, substitution $t=x^2$ gives


$$
\begin{aligned}
4\int_0^1x^{2s}(x^2-1)^H\,dx
&=2(-1)^H B(s+\tfrac12,H+1)\\
&=\frac{(-1)^H2^{H+2}H!}
{\prod_{v=0}^{H}(2s+2v+1)}.
\end{aligned}
\tag{2}
$$


The proposed identity is correct.

Suppose now that $H=3^u$ and


$$
0\le s\le(H-3)/2.
$$


For each $1\le r\le u$, the first $H$ factors


$$
2s+1,\ 2s+3,\ldots,2s+2H-1
$$


contain exactly $H/3^r$ multiples of $3^r$. None is divisible by $3^{u+1}$, since all are positive and less than $3H$. Consequently their product has valuation


$$
\sum_{r=1}^{u}H/3^r=v_3(H!).
$$


The remaining factor is $2s+2H+1$, and


$$
v_3(2s+2H+1)=v_3(2s+1)\le u-1.
$$


Therefore


$$
v_3\!\left(
4\int_0^1x^{2s}(x^2-1)^H\,dx
\right)
=-v_3(2s+1).
\tag{3}
$$



This is an exact valuation, not just a lower bound.

## 2.2 Fifth-depth consequence on the assigned small-$D$ domain

Let


$$
0\le s\le2D-1.
$$


Then


$$
2s+1\le4D-1<H/81=3^{u-4}.
$$


Hence


$$
v_3(2s+1)\le u-5.
$$


Combining this with (3) proves


$$
\boxed{
3^u\int_0^1x^{2s}(x^2-1)^H\,dx
\in3^5\mathbb Z_3
\qquad(0\le s\le2D-1).
}
\tag{4}
$$


All integrals here are rational numbers, so this is an ordinary statement in $\mathbb Q_3$.

Take any $\beta\in\mathbb Z_3$, and set


$$
F_s(y)=(y+1)(y-1)^Hy^s(\beta+3y).
$$


Since $F_s(-1)=0$, its rational atan contribution after the initial division by $3$ is exactly


$$
3^{h-1}\int_0^1
x^{2s}(x^2-1)^H(\beta+3x^2)\,dx.
\tag{5}
$$


For $0\le s\le2D-2$, both terms in (5) are divisible by $3^5$, by (4).

The factorial part after the same division is


$$
-\frac{3^{h-1}}4\mathfrak f(F_s)\in3^u\mathbb Z_3
\subseteq3^5\mathbb Z_3.
$$


Thus the **complete** functional satisfies


$$
\boxed{
\frac{\mathcal M(F_s)}3\equiv0\pmod{243},
\qquad 0\le s\le2D-2.
}
\tag{6}
$$



This evaluates all pole contractions in these pairings simultaneously. No cancellation between an omitted pole and a retained pole is assumed.

## 2.3 Transfer to the actual polynomial and its endpoint

Write


$$
M_0=(4^j-1)/3,\qquad \mu=v_3(M_0)=v_3(j)\ge4.
$$


The supplied sharpened original law gives


$$
Q_n^{\rm loc}
\equiv
(y+1)(y-1)^A(3y-71-3M_0)
\pmod{3^{\mu+2}}.
\tag{7}
$$


In particular, its available precision is at least $3^6=729$, while its core modulo $243$ is $3y-71$.

Use the stronger congruence (7) when transferring through a division. Put


$$
\beta=-71-3M_0,\qquad
\Delta Q=Q_n^{\rm loc}-(y+1)(y-1)^A(\beta+3y).
$$


Then


$$
\Delta Q\in729\mathbb Z_3[y].
$$


For any integral polynomial $p$,


$$
\frac{\Delta Q\,p-\Delta Q(-1)p(-1)}{y+1}
\in729\mathbb Z_3[y],
\tag{8}
$$


because division by the monic polynomial $y+1$, with the exact remainder subtracted, preserves coefficient divisibility.

Each coefficient weight in (1) is integral. Therefore, even allowing the worst loss from dividing $\mathcal M$ by $3$, the error in (8) contributes only a multiple of $243$. This explicitly retains the actual endpoint error rather than setting $Q_n^{\rm loc}(-1)$ to zero.

For $0\le a\le d$,


$$
(y-1)^Aw_\nu y^a=y^{\nu+a}(y-1)^H,
\qquad
\nu+a\le2D-2.
$$


The same bound holds with $w_\nu$ replaced by any $z_i$. Applying (6) and (8) gives


$$
\boxed{
\frac{\mathcal M(Q_n^{\rm loc}w_\nu y^a)}3
\equiv0\pmod{243},
\qquad 0\le a\le d,
}
\tag{9}
$$


and


$$
\boxed{
\frac{\mathcal M(Q_n^{\rm loc}z_i y^a)}3
\equiv0\pmod{243},
\qquad 0\le i<\nu,\quad 0\le a\le d.
}
\tag{10}
$$



In these pairings the top pole is absent by degree. Indeed the largest possible degree after endpoint subtraction is


$$
A+1+2d=H+2D-1<(3H-1)/2.
$$


Thus (9)–(10) are also statements about the actual extended lower functional $L_{\rm ext}$:


$$
\boxed{
L_{\rm ext}(w_\nu,y^a)=
L_{\rm ext}(z_i,y^a)=0\pmod{243}
}
\tag{11}
$$


on the displayed index domains.

This is the new proved arithmetic lemma.

# 3. What the beta lemma does—and does not—settle

The proof of (11) has no degree increase: it uses the linear core directly, rather than multiplying the radical by a truncated geometric inverse. It therefore avoids one proposed difficulty with the geometric-inverse route.

It nevertheless stops before the required fifth Schur evaluation.

The actual block matrix remains


$$
\begin{pmatrix}3L&3X\\3X^T&E\end{pmatrix}.
$$


After eliminating the LOW unit block first, one must use


$$
\widehat E=E-3X_U^TL_U^{-1}X_U,
$$


not merely $E$. The residual radical form also depends on the corrected coupling to HIGH.

Equations (9)–(11) control the direct pairings against LOW and the extra coordinate $y^d$. They do not evaluate all pairings against


$$
y^{d+1},\ldots,y^m,
$$


which enter the fifth HIGH inverse contraction. In particular, the already evaluated two-edge force modulo $3$ is insufficient to determine its next digit or the next inverse contractions.

There is also a genuine precision distinction:

* $3y-71\pmod{243}$ is sufficient for the direct fifth lower-pole form.
* For top-pole terms subsequently divided by $3$, one must retain the stronger original congruence (7). If $\mu=4$, the term $-3M_0$ has valuation $5$; it disappears modulo $243$, but not automatically after a further division.

I have not evaluated those corrected contractions. Accordingly:

* the rank of $T_5$ is unresolved;
* membership of the transported endpoint in $\operatorname{im}T_5$ is unresolved;
* there is **no new fifth-depth gcd lower bound** in this response.

The established endpoint residue remains


$$
\overline e_{\rm rad}=((-1)^i)_{0\le i<\nu}\ne0,
$$


but that fact alone does not determine the fifth endpoint image.

The retained, already established gcd bound on this smaller domain is


$$
v_3(g)\ge d+4\nu=\frac{7D}{2}-5.
$$


I do not repeat its proof or promote it to fifth depth.

# 4. Independent audit of A3 turn17 at the critical two-thirds scale

The audited domain is exactly


$$
\kappa_0n^{2/3}\le b\le\kappa_1n^{2/3},
\qquad 0<\kappa_0<\kappa_1<\infty,
\qquad d=b-1,
$$


on both parities and uniformly over $0\le j\le b$.

The following passes use the exact reconstruction, normality, full-contour and whole-residual interfaces expressly invoked by A3. They are not an independent reconstruction of those earlier interfaces.

## 4.1 Actual phase denominator: pass

At $q=M,\rho$,


$$
N_j(q)=\mathbb E_q[S_je^{i\Phi_q}].
$$


Reflection gives $\mathbb E_q\Phi_q=0$, and


$$
\left|\mathbb E_qe^{i\Phi_q}-1\right|
\le\tfrac12\mathbb E_q\Phi_q^2=O(d/n).
$$


Together with


$$
\sup|S_j-1|=O(d/n),
$$


this proves


$$
N_j(q)=1+O(d/n).
$$


Thus the denominator in each differentiated **actual** integral is bounded away from zero. No positivity of a complex expectation is assumed.

## 4.2 Endpoint-safe moments: pass

The safe field


$$
v(t)=tg(t)/M
$$


vanishes at both endpoints of the principal interval. Multiplication by the logarithmic derivative of $g^n$ gives


$$
v(t)\left(-n\frac{g'(t)}{g(t)}\right)
=\frac{\sigma n}{M}t\sin t
=\alpha_0nt^2+O(nt^4).
$$


The remaining one-particle terms contribute $O(t^2)$.

In the pair part of integration by parts,


$$
(v(x)-v(y))\cot((x-y)/2)=2+O(x^2+y^2).
$$


The apparent diagonal singularity is removable. Away from the origin the bound remains uniform on the compact principal square, whose differences never reach $2\pi$.

Thus the sharp identity has error


$$
O(n\mathbb E Q_4+d\mathbb E Q+\mathbb E Q),
$$


and the stated preliminary moment bounds give


$$
\mathbb E Q=\frac{d^2}{\alpha_0n}+O(d^3/n^2).
$$


Also


$$
\operatorname{Var}Q
\ll n^{-1}\mathbb E\|\nabla Q\|^2
\ll d^2/n^2.
$$


The boundary fluxes are compatible with the stated principal density.

## 4.3 First logarithmic derivative: pass

The Taylor coefficient is correct:


$$
\frac1{e^{-it}+q}
=\frac1{1+q}
+\frac{it}{(1+q)^2}
+\frac{q-1}{2(1+q)^3}t^2+O(|t|^3).
$$


The centering identity


$$
\frac{\mathbb E(W_jQ)}{N_j}-\mathbb E Q
=\frac{\mathbb E[W_j(Q-\mathbb E Q)]}{N_j}
$$


is essential: it removes the potentially large mean rather than estimating it in absolute value.

Reflection and phase covariance give


$$
\mathbb E(W_jX)=O(d/n).
$$


Hence


$$
\frac{A_j'(q)}{A_j(q)}
=\frac d{1+q}
+\frac{d^2}{n}\frac{q-1}{2\alpha_0(1+q)^3}
+O\!\left(\frac dn+\frac{d^3}{n^2}
+\frac{d^{5/2}}{n^{3/2}}\right).
$$


At the critical scale, multiplying the remainder by $d/n$ gives $o(1)$; the largest displayed term is $O(n^{-1/6})$. This is the required stationary-value precision.

## 4.4 Second logarithmic derivative: pass

Exact differentiation gives


$$
(\log A_j)''=\langle J_q\rangle_W
+\langle H_q^2\rangle_W-\langle H_q\rangle_W^2.
$$


Centering the covariance at the positive-measure mean $\mathbb E_qH_q$ is legitimate even though $\langle\cdot\rangle_W$ is complex. The bounded weight and nonzero denominator imply


$$
\left|\langle H_q^2\rangle_W-\langle H_q\rangle_W^2\right|
\ll \mathbb E_q|H_q-\mathbb E_qH_q|^2
=O(d/n).
$$


Also


$$
\langle J_q\rangle_W
=-\frac d{(1+q)^2}+O(d^{3/2}/\sqrt n).
$$


Thus the claimed $o(d)$ remainder is valid at $d\asymp n^{2/3}$.

## 4.5 Signed cubic calculation: pass

For the radial variable $\zeta$,


$$
f_\pm''(1)=\alpha_\pm,\qquad
f_\pm'''(1)=-3\alpha_\pm.
$$


The signs in


$$
a_-=-T_j'(\rho),\qquad \beta_-=T_j''(\rho)
$$


are correct.

The stationary-value expansion


$$
nf(r)+U(r)
=nf(1)+U(1)-\frac{a^2}{2n\alpha}
+\frac{\beta a^2}{2n^2\alpha^2}
-\frac{f'''(1)a^3}{6n^2\alpha^3}
+O(d^4/n^3)
$$


has the displayed signs.

Using


$$
1+M=\sigma M,\qquad 1+\rho=\sigma,\qquad \sigma^2=2,
$$


the pure cubic difference is


$$
-\frac{M+1}{2\sigma^5M^2}\frac{d^3}{n^2},
$$


and the quadratic-cross difference is


$$
+\frac{M+1}{2\sigma^5M^2}\frac{d^3}{n^2}.
$$


They cancel exactly. At the assigned scale,


$$
d^4/n^3=O(n^{-1/3})=o(1).
$$



## 4.6 Reciprocal partition identity: pass, with its scope retained

Pointwise on the unit circle,


$$
|e^{-it}+M|=M|e^{-it}+\rho|.
$$


Therefore the two positive principal measures are identical after normalization and


$$
Z_d(M)=M^dZ_d(\rho)
$$


exactly.

The actual characteristic integrals need not satisfy this identity exactly. Their additional factors are $N_j(M)$ and $N_j(\rho)$, both $1+O(d/n)$. Including the controlled outer sectors gives


$$
U_-(1)-U_+(1)=-d\log M+O(d/n).
$$


A3 makes precisely this weaker actual-integral claim; it passes.

## 4.7 Whole law and metric: pass within the supplied interfaces

The scalar normalization ratio is $4\pi$, and the Gaussian-width ratio tends to $M^{-1}$. Both minus connectors and all signed particle outer sectors remain included in the cited contour bounds.

The complete coordinate error is still


$$
c_j-(e+\pi)
=\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac D{P_j}.
$$


Using the supplied bounds for the **whole** $E_j$ and endpoint, the audited conclusion is


$$
\boxed{
c_j-(e+\pi)
=(-1)^{n+1}4\pi M^{-2n-b}(1+o(1)).
}
$$


It includes eventual nonvanishing of the whole error and, with the supplied normality interface, of $D$ and every first-column coordinate.

The metric transfer is valid for every positive **diagonal metric in the actual coordinates**, because it is a convex combination of coordinate errors. It does not extend to arbitrary nondiagonal metrics.

# 5. Primitive denominators and whole real errors

For the weighted construction retain


$$
A_{\rm det}=\det T,\qquad
B_{\rm det}=\ell Q_n(-1)\det K,
$$




$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|),\qquad
q=\frac{|B_{\rm det}|}{g},\qquad
p=-\frac{\operatorname{sgn}(B_{\rm det})A_{\rm det}}g.
$$


Where $B_{\rm det}\ne0$,


$$
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_{\rm det})\ell^k}{g}
\det H_{\rm complete},\qquad k=(n+1)/2.
$$


The primitive multiplier is the full clearer divided by the **final** gcd. The new direct-annihilation lemma proves neither complete-response nonvanishing nor whole-error nonvanishing.

For the audited analytic centers with rational positive diagonal metric, retain the least two-column clearer $d_B$, integral metric $\Omega$, and


$$
A_B=N_{B,1}^T\Omega N_{B,1},\quad
H_B=N_{B,1}^T\Omega N_{B,2},\quad
g_B=\gcd(A_B,|H_B|).
$$


Then


$$
q_B=A_B/g_B,\qquad p_B=H_B/g_B,
$$


the primitive multiplier is $d_B^2/g_B$, and


$$
\boxed{
q_B(e+\pi)-p_B
=(-1)^n4\pi q_BM^{-2n-b}(1+o(1))\ne0.
}
$$


No estimate for $q_B$ is supplied by the analytic audit.

## Closing ledger

1. **New result and proof status.**  
   Proved the beta-based complete direct annihilation (9)–(11) modulo $243$ on $81\mid j,\ D<H/324$, with the factorial functional, full pole cutoff, endpoint subtraction, and precision loss retained. Independently audited A3 turn17: the first derivative, second derivative, actual phase denominator, reciprocal partition identity, and signed cubic cancellation pass within the stated analytic dependencies and actual diagonal metric. **The fifth weighted Schur digit is not evaluated.**

2. **Exact remaining bottleneck.**  
   Evaluate the next actual HIGH/LOW elimination contractions, including the next digits of the HIGH coupling and inverse and the top-pole precision supplied by (7). Until then, the fifth rank and endpoint image are unresolved, and no fifth gcd improvement is justified. For irrationality, the separate unresolved requirement remains same-index control of the final primitive denominator together with nonzero whole primitive errors tending to zero.

3. **Computation request.**  
   None. A finite rank scan would not resolve the assigned infinite fifth-digit assertion. The outstanding task is symbolic evaluation of the corrected HIGH/LOW contractions, not another direct-moment valuation bound.
