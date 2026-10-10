> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## Audit verdict

**The instantaneous positive-ensemble bias argument passes, with one functional-analytic repair:** use the $1/68$ estimate as coercivity on the actual image of $K_c$, rather than claiming a Neumann inverse between unspecified exterior-analytic Banach spaces.

**The binary pair calculation also passes, but its explanation needs repair.** The ratio $-1\bmod8$ is sufficient to make a valuation-one pair contribute $8\bmod64$. No additional absolute-unit congruence is needed. Individual squares can indeed be $4$ or $36\bmod64$; the ratio forces the two square residues to agree, and both possible sums are $8\bmod64$.

These conclusions do not evaluate the fifth mixed discrepancy, prove the all-sublinear scalar-contour interfaces, or bound the actual primitive denominator.

---

# 1. A3turn23: rescaling, convexity, mode and localization

Throughout this section,


$$
d\ge2,\qquad c=d/n,\qquad 0<c\le10^{-3},
\quad \sigma=\sqrt2,\quad M=1+\sqrt2.
$$



### 1.1 Exact rescaling: pass

In the unperturbed positive principal ensemble, the transformation


$$
x=\tan(\theta/2)=\sqrt c\,u
$$


changes the particle-dependent weight to


$$
(1-cu^2/M^2)^n(1+cu^2)^{-n-d}.
$$


Since $n=d/c$, its negative logarithm is exactly $dW_c(u)$, with


$$
W_c(u)=
\frac{\log(1+cu^2)-\log(1-cu^2/M^2)}c
+\log(1+cu^2).
$$


The remaining scaling factors are partition-function constants. Neither the amplitude nor the characteristic tilt belongs in this base potential.

### 1.2 Global convexity: pass

Writing $y=cu^2$,


$$
W_c''(u)=
2(1+c)\frac{1-y}{(1+y)^2}
+\frac2{M^2}\frac{1+y/M^2}{(1-y/M^2)^2}.
$$


For $y\le1$, the lower bound $2/M^2$ applies. For $y\ge1$,


$$
\frac{y-1}{(1+y)^2}\le\frac18,
$$


so


$$
W_c''(u)\ge-\frac{1+c}{4}+\frac2{M^2}>\frac1{16}.
$$


This holds on the **entire** principal interval. The logarithmic pair interaction has positive-semidefinite Hessian, hence


$$
\nabla^2H\ge\frac d{16}I.
$$



### 1.3 Hermite comparison: pass

The Gaussian comparison configuration has Jacobi off-diagonal entries


$$
\sqrt{\frac{i}{kd}},\qquad k=\frac1{16},
$$


and therefore $\max_i|v_i|\le2/\sqrt k$.

At an index maximizing $a_i-v_i-R_0$, the inequalities


$$
a_i-a_j\ge v_i-v_j
$$


hold for every $j$. Both differences have the same sign because both configurations are ordered. Consequently reciprocal monotonicity is legitimately applied separately on the positive and negative half-lines. With $R_0=2/\sqrt k$, a positive maximum would give


$$
kd\,a_i\le dW_c'(a_i)
=2\sum_{j\ne i}\frac1{a_i-a_j}
\le kd\,v_i,
$$


contradicting $a_i>v_i+R_0$. Reflection supplies the other side. Thus $|a_i|\le16$.

### 1.4 Radial stochastic domination: pass

The translated convex chamber is star-shaped about its interior mode. Along an admissible ray,


$$
\partial_r H(a+r\omega)\ge kd\,r.
$$


Extending the ray factor by zero after its boundary preserves monotonicity. Angular integration therefore produces a nonincreasing multiplier of


$$
r^{d-1}e^{-kd r^2/2}.
$$


This gives the claimed monotone-likelihood-ratio comparison with the Gaussian radius. In particular,


$$
\mathbb P(\max_i|u_i|>24)
\le e^{-d(3-\log4)/2}.
$$


No independence of particle coordinates is used.

---

# 2. Wall densities: both proposed arguments are valid

## 2.1 A3’s homothetic slice argument: pass

Let $p_i$ be a normalized ordered-coordinate marginal. The homothety


$$
u\longmapsto a^\circ+s(u-a^\circ)
$$


maps the slice $u_i=24$ into the slice


$$
u_i=a_i^\circ+s(24-a_i^\circ).
$$


Its slice Jacobian is $s^{d-1}$. Convexity and minimality at $a^\circ$ imply that the density does not decrease under this map. Thus


$$
p_i(a_i^\circ+s(24-a_i^\circ))
\ge s^{d-1}p_i(24).
$$



For $d\ge40$, $s\in[1-1/d,1]$, and $|a_i^\circ|\le16$, the mapped coordinate lies in $[23,24]$, and $s^{d-1}\ge1/4$. Integration gives


$$
\mathbb P(u_i\ge23)\ge\frac{2}{d}p_i(24).
$$


The radial bound with $T=7$ therefore proves


$$
p_i(24)\le\frac d2e^{-\gamma_7d}.
$$



Conditioning on all particles lying in $[-24,24]$ restricts each boundary slice and divides its mass by the conditioning probability. Hence the stated


$$
\sum_i\bigl(p_i^{[24]}(24)+p_i^{[24]}(-24)\bigr)
=O(d^2e^{-\gamma_7d})
$$


is valid. It is a density estimate, not an inference from a small tail probability alone.

## 2.2 Coordinator’s alternative: pass

On the ordered chamber, the maximum is the linear coordinate $u_d$. Its marginal is log-concave, and Brascamp–Lieb gives


$$
\operatorname{Var}(u_d)\le16/d.
$$


Radial domination gives $\mathbb Eu_d\le20$.

The supplied unimodal representation yields


$$
|\mathbb Eu_d-m|\le\sqrt{3\operatorname{Var}(u_d)}.
$$


For $d\ge48$, a mode is therefore at most $21$. Monotonicity of the marginal density above its mode gives


$$
f_{u_d}(24)\le\int_{23}^{24}f_{u_d}(t)\,dt
\le e^{-\gamma_7d}.
$$


Differentiating the ordered truncated partition in its upper wall exposes exactly the maximum-coordinate boundary face. Thus this alternative removes the unnecessary polynomial factor $d^2$. Either estimate suffices for the loop argument.

---

# 3. A3turn24: instantaneous loop argument

Here the uniform domain is


$$
0\le c\le10^{-6},\qquad d\ge d_*,
$$


where $c=0$ denotes the Gaussian limiting potential.

## 3.1 Spectral normalization: pass

The rescaled resolvent is $\sqrt c$ times the original resolvent evaluated at $\sqrt c\,z$. Applying this multiplier to the archived spectral term gives


$$
y_c(z)=
\frac{\sqrt{(M^2+1)(M^2+(1+c)^2)}}
{(1+cz^2)(M^2-cz^2)}
\sqrt{z^2-B_c^2},
$$




$$
B_c^2=\frac{M^2(c+2)}{M^2+(1+c)^2}.
$$


Thus


$$
R_c=W_c'/2-y_c.
$$


There is no missing factor of two under this convention. At $c=0$,


$$
2R_0-az=-a\sqrt{z^2-4/a},
\qquad a=2(1+M^{-2}).
$$



## 3.2 Exact beta-two equation and algebraic covariance: pass

For $v(u)=(z-u)^{-1}$, integration by parts gives


$$
\mathscr W^2+C(z,z)
-d\,\mathbb E\sum_i\frac{W_c'(u_i)}{z-u_i}
=J_{d,c}(z).
$$


Indeed,


$$
v'(u)=\frac1{(z-u)^2},\qquad
\frac{v(u_i)-v(u_j)}{u_i-u_j}
=\frac1{(z-u_i)(z-u_j)}.
$$


The diagonal derivative terms and the interaction terms combine into the square of the trace. There is no residual derivative term at $\beta=2$.

The covariance is algebraic:


$$
C(z,z)=\mathbb E(F-\mathbb EF)^2,
$$


not a variance with complex conjugation. Nevertheless,


$$
|C(z,z)|\le\mathbb E|F-\mathbb EF|^2
\le\frac1{k6^4}
$$


on $|z|=30$, by applying the variance inequality to real and imaginary parts.

The flux signs are correct:


$$
J_{d,c}(z)=
\sum_i\left(
\frac{p_i^{[24]}(24)}{z-24}
-\frac{p_i^{[24]}(-24)}{z+24}
\right).
$$



## 3.3 Contour formula and coercivity: pass after repair

For a Cauchy transform $h$ supported inside the circle,


$$
T_ch(z)=W_c'(z)h(z)
+\frac1{2\pi i}\oint_{|w|=36}
\frac{W_c'(w)h(w)}{z-w}\,dw.
$$


The plus sign is correct: the residue at $w=z$ has a minus sign.

For zero-mass $h$,


$$
T_0h=azh,\qquad
K_0h=-a\sqrt{z^2-B_0^2}\,h.
$$


Consequently


$$
\|K_0h\|_{30}>69\|h\|_{30}.
$$


The rational-potential estimate $\sup_{|z|\le36}|W_c'-az|<0.1$, the exterior maximum principle, and the contour separation $36-30=6$ give


$$
\|(T_c-T_0)h\|_{30}\le0.7\|h\|_{30}.
$$


The equilibrium supports lie in $[-2,2]$, so


$$
2\|R_c-R_0\|_{30}\le4/28.
$$


Therefore


$$
\|(K_c-K_0)h\|_{30}<\|h\|_{30},
$$


and directly


$$
\boxed{\|h\|_{30}\le\frac1{68}\|K_ch\|_{30}.}
$$



**Repair:** this proves precisely what the application needs. It does not require an onto statement or a globally specified Neumann inverse. The potential’s distant poles also make an unrestricted “exterior analytic codomain” description unnecessarily problematic.

## 3.4 Uniform coarse convergence and absorption: pass

The fixed compact interval, compact continuous family of potentials, unique equilibrium minimizers, and bounded equicontinuous resolvent kernels supply uniform coarse convergence.

The subsequence argument works for an arbitrary $c_d$: after selecting $c_d\to c_\infty$, the density comparison costs


$$
O\!\left(d^2\|W_{c_d}-W_{c_\infty}\|_\infty\right)=o(d^2),
$$


which preserves fixed-neighborhood exponential concentration. A finite contour net gives the supremum norm.

Thus, for


$$
h=\mathscr W-dR_c,\qquad H=\|h\|_{30},
$$


one has $H/d=o(1)$ uniformly. Subtraction of the equilibrium equation gives


$$
dK_ch+h^2+C=J.
$$


Coercivity implies


$$
68dH\le H^2+O(1)+O(d^2e^{-\gamma_7d}).
$$


Eventually $H\le34d$, so


$$
\boxed{H=O(d^{-1})+O(de^{-\gamma_7d}).}
$$


No full $1/d$ expansion, fixed positive limiting ratio, or regularity of the sequence $c(d)$ is imported.

---

# 4. Transfer to the actual characteristic derivative

This passes on the stated real anchor neighborhoods.

The function


$$
f_{c,q}(u)=
\frac{1+i\sqrt c\,u}
{1+q+i\sqrt c\,u(q-1)}
$$


is uniformly analytic on the required fixed disk. Cauchy integration transfers the resolvent estimate to its trace.

For the positive tilt, both particle derivatives are $O(\sqrt c)$, and the tilt Hessian is $O(c)$. Interpolation therefore changes the mean trace by $O(c)$.

For the actual insertion, retain


$$
\mathcal W_j=S_je^{i\Phi_q},\qquad
N_j=\mathbb E_q\mathcal W_j,\qquad
\langle F\rangle_j=\frac{\mathbb E_q(\mathcal W_jF)}{N_j}.
$$


The retained insertion and phase estimates give bounded $\|\mathcal W_j\|_2$ and $|N_j|\ge1/2$ eventually. Centering **before** applying Cauchy–Schwarz yields


$$
|\langle F\rangle_j-\mathbb E_qF|
\le\frac{\|\mathcal W_j\|_2}{|N_j|}
\sqrt{\operatorname{Var}_qF}
=O(\sqrt c).
$$



There is no need to differentiate a separately centered phase: differentiating the original characteristic product gives the exact logarithmic derivative trace. Differentiated outer-sector bounds gain at most a uniform constant times $d$, because every characteristic denominator remains separated from zero. Their exponential suppression survives.

Hence


$$
\boxed{(\log A_j)'(q)=dL_c'(q)+O(1)}
$$


uniformly in $0\le j\le b$, along $d\to\infty$, $d/n\to0$, on both parities.

The complete scalar-contour conclusion remains a separate conditional interface.

---

# 5. A5turn19: fifth $Q$-precision and next norm

The domain remains exactly


$$
b=9^r,\quad n=4002b,\quad r=18+32u,\quad u\ge0,
$$




$$
b=128D+81,\quad C=4002D+2532,\quad n=128C+66.
$$



## 5.1 Fifth $Q$-lift: pass at the stated source dependencies

The fixed coefficient controls agree with the displayed factorial residues, boundary polynomial, and degree-$23$ formula. The infinite parameter transfer is consistent with the required precision:

* $v_2(b-81)=7$;
* the boundary lower-index bounds $7,11,15,19,23$ lose at most $2,3,3,4,4$ bits;
* multiplication by $2^{\ell+1}$ restores precision $128$;
* the exceptional first inverse correction from $E(n)-E_0\equiv16T(-4)\pmod{32}$ is retained;
* higher inverse occurrences of that correction vanish modulo $128$.

The contact correction and boundary correction combine as stated:


$$
Q_5=
2\sum_{\ell=0}^{5}(-2\mathscr E_0)^\ell a_{32}
+64\left(1+\binom X7\right)\pmod{128}.
$$


The actual $T(-2n)$, range $0\le i<b$, seven exterior terms, and endpoint $+W_b$ remain unchanged.

This does **not** supply the missing normalized $P$-forcing modulo $64$.

## 5.2 First-column unrestricted convolution: pass

The sampled identity


$$
J_{32}(8s)=2+20s\pmod{32}
$$


and the binary power congruence give a finite convolution through its actual endpoint $2q$. The weighted first moment is


$$
\sum_{t=0}^{2q}(2q-t)\binom{16e+t-1}{t}
=\binom{16e+2q}{2q-1}.
$$


Thus the adjacent-binomial reduction gives


$$
X_j\equiv
-(1+4q)W_j\binom{8e+q}{q}\pmod{16},
\quad q=\frac{b-1-j}{16},
\quad32\mid j<b.
$$


The translation correction is removed only after the stated weight-parity check. There are no Laurent boundary terms in this first-column convolution.

## 5.3 The questioned pair-unit step: valid, with a necessary explanatory repair

Write a depth-one pair as


$$
X_{128t}=2u,\qquad X_{128t+64}=2v,
$$


with $u,v$ odd. The supplied weight and binomial ratios give


$$
v/u\equiv-1\pmod8.
$$


Therefore


$$
v^2\equiv u^2\pmod{16},
$$


and


$$
X_{128t}^2+X_{128t+64}^2
\equiv8u^2\equiv8\pmod{64}.
$$



The last congruence uses $u^2\equiv1\pmod8$. Equivalently, if $u^2\bmod16$ is $1$ or $9$, the pair sum is $8$ or $72$, which are equal modulo $64$.

**No absolute-unit hypothesis is missing.** What would be false is asserting that each individual depth-one square is always $4\bmod64$.

For reference, the two ratio formulas are compatible with $C\equiv2\bmod4$, $e=2C+1\equiv5\bmod8$, and opposite parities of $t,D-t$. Their product is indeed $7\bmod8$.

## 5.4 Support, counts and finite boundaries

The norm calculation correctly uses the stronger support $8\mid X_j$ for $32\nmid j$, not merely the earlier defect support.

The surviving ranges are exactly


$$
128t,\ 128t+32,\ 128t+64:\quad0\le t\le D,
$$




$$
128t+96:\quad0\le t\le D-1.
$$


The latter class has weight depth at least three, using


$$
(C-t)\binom Ct=C\binom{C-1}{t}.
$$


Its squares vanish modulo $64$, as do the retained endpoint and all coordinates outside these classes.

Consequently


$$
N\equiv24C_1+32C_2\pmod{64}.
$$


The parity reduction of $C_2$ pairs the even-$t$ contributions with the even internal-index contributions from odd $t$. The unmatched odd internal indices give exactly


$$
C_2\equiv
a\binom{a+v+\varepsilon+1}{v+\varepsilon-1}\pmod2.
$$


Thus


$$
\boxed{N\equiv48T+32\chi\pmod{64}.}
$$



The two-state count is also correctly normalized. At bit $k$, $h_k$ counts the freely selectable bits of $i$ and $q$, and


$$
\binom{h_k}{v_k+2c'-c}
$$


counts precisely the selections compatible with incoming carry $c$ and outgoing carry $c'$. Initial and terminal zero carries enforce $i+q=v$, including the upper boundary. No high digit is freely substituted.

In particular, on $r=50+128w$, $a$ is even and $v$ odd. Every admissible $i$ and $q$ is even, so $T=0$ as an integer count; also $\chi=0$. Therefore the next-norm conclusion


$$
N\equiv0\pmod{64}
$$


survives this audit. It says nothing new about $H\bmod64$.

---

# 6. A bounded follow-on unit lemma

The pair argument admits a useful sharper formulation.

**Lemma.** For odd $u,v$,


$$
4(u^2+v^2)\equiv
\begin{cases}
8\pmod{64},&v/u\equiv\pm1\pmod8,\\
40\pmod{64},&v/u\equiv\pm3\pmod8.
\end{cases}
$$



**Proof.** The square of the ratio modulo $16$ is respectively $1$ or $9$. Hence the expression is respectively $8u^2$ or $40u^2$, and $u^2\equiv1\bmod8$. ∎

This identifies exactly which relative-unit information is needed at the next norm level; it avoids imposing an unnecessary absolute-unit condition.

---

# 7. Whole error and primitive bookkeeping

For A3, retain the actual columns


$$
u_j=(-1)^nP_j/D,\qquad
v_j-Su_j=\delta_{j0}+(-1)^nE_j/D-F_j/D,
$$


including the complete exponential force in $E_j$. On $D\ne0$, $P_j\ne0$,


$$
\frac{v_j}{u_j}-S
=\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac D{P_j}.
$$


For a positive diagonal metric, no different column system is substituted.

For the binary family, retain


$$
X=Z_w/(2R),\quad Y=V_w/(4b!),\quad
N=X^TX,\quad H=X^TY,
$$


and


$$
\Omega=\operatorname{diag}\bigl((n+2)_{\underline j}^{\,2}\bigr)_{0\le j\le b}.
$$


With the least actual clearer $d_B$,


$$
N_B=d_B[u,v],\quad
A_B=N_{B,1}^T\Omega N_{B,1},\quad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\quad
q_n=A_B/g_B,\quad p_n=H_B/g_B.
$$


The primitive multiplier on the uncleared quadratic pair is $d_B^2/g_B$.

The exact binary denominator interface remains


$$
v_2(q_n)=
\max\left\{0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)\right\}.
$$


Neither $\alpha\ge6,\gamma\ge5$ nor the next norm digit controls $\gamma-\alpha$.

At the retained status of the complete signed-error theorem on this binary domain,


$$
\epsilon_n=c_n-S<0,\qquad
\log|\epsilon_n|
=-\left(2+\frac1{4002}\right)n\log M+o(n),
$$


and the **whole**, eventually nonzero primitive error is


$$
q_nS-p_n=-q_n\epsilon_n>0.
$$



The secondary A1 and MAIN29 closures are not rejected for missing definitions. Their now-supplied source interfaces are separate from the main audits above.

---

## Closing ledger

1. **New result and proof status.**  
   The instantaneous bias proof passes with image coercivity replacing an unnecessary onto-inverse claim. The actual characteristic derivative comparison follows on the stated anchor domains. The binary fifth $Q$-lift and next-norm formula survive the audit. The questioned pair-unit implication is valid; its repaired proof and the sharper two-case unit lemma are explicit above.

2. **Exact remaining bottleneck.**  
   Analytically, the complete all-sublinear scalar-contour interfaces remain separate. Arithmetically, the normalized $P$-forcing modulo $64$ and the whole mixed contraction $(H-N)/32\bmod2$ remain unresolved. Beyond fixed precision, a same-index bound on the actual denominator after the final gcd is still required. No irrationality or rationality conclusion for $e+\pi$ follows.

3. **Computation request.**  
   None. The repairs above are exact analytic and modular arguments. The supplied fixed polynomial controls are not being used as finite evidence for an infinite assertion.
