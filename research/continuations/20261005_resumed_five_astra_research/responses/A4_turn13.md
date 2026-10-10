> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 13 — Audit of nonlinear Schur protection, contact-lattice loss, and bulk–boundary transport

## Executive conclusions

The three reports contain useful advances, but they concern different mathematical objects and must not be combined into an irrationality argument without the missing relative and global arithmetic.

My principal findings are:

1. **A1turn7’s exact nonlinear Schur identity, mixed-force factor $3$, LOW-inverse isotropy, transported endpoint, determinant-pair signs, and primitive $3$-denominator formula pass.**  
   The newly attached old closure supplies enough information to discharge the **coarser, precision-parameterized supported-return obligation actually needed in A1turn7**. The key is an exact cancellation in $(\widehat E-E_0)p$ before division by $3$, displayed below. This is not a waiver of the numerator-modulus requirement.

   Consequently, A1turn7’s depth-$14$ result on its very narrow fixed window is justified from the accepted producer interface. It still supplies neither a relative inverse comparison nor nonvanishing of the determinant pair.

2. **A2turn4’s normal charge, integral projector, zero boundary currents, and unbounded negative contact-lift valuations pass at the stated complete-force and original-lifting scope.**  
   The obstruction is genuine for the actual unsaturated contact lattice. It does **not** refute relative norm/mixed alignment in the saturated weighted space. The proposed skew-reconstruction identity has the correct scaling and is sufficient, but remains unproved.

3. **A5turn10’s exact suffix and bulk–boundary decomposition, complete-symbol factorial bound, changed force, and precision-$138$ negative-continuation argument pass.**  
   The path argument can be strengthened substantially without evaluating any endpoint coefficient:
   

$$
\boxed{\mathfrak p_{380}^{*}(-3)\in2^{180}\mathbb Z_2.}
$$


   The improvement uses the **last endpoint injection**, followed by the exact telescoping factorial multiplier of the remaining bulk path. All earlier endpoint injections and all retained high input degrees are included.

4. **There is also a uniform actual-family consequence, but only on a sufficiently deep explicitly bounded cylinder.** A finite polynomial denominator bound given below transfers the new precision-$180$ result to original indices. It does not replace the accepted, stronger-in-scope statement
   

$$
\boxed{\mathfrak p_{380}(u)\in2^{96}\mathbb Z_2\quad\text{for every original }u\ge0.}
$$



5. None of these results establishes the full norm/mixed valuation difference, the all-prime final gcd, or a same-index sequence with
   

$$
0<|q_n(e+\pi)-p_n|\longrightarrow0.
$$


   **The irrationality or rationality of $e+\pi$ remains unresolved.**

No tools were executed.

---

# I. A1turn7: the missing modulus and the exact nonlinear arithmetic

## 1. Original domain and normalization

Retain


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$




$$
A=n-2=H-D,\qquad H=3^{h-1},\qquad0<D<H/972,
$$


and


$$
m=\frac{A+1}{2},\qquad d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
$$



The finite columns are exactly


$$
U_a=(y-1)^a\quad(0\le a<D),\qquad
z_i=(y-1)^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m).
$$



The complete functional remains


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
\qquad \mathfrak f(y^s)=(2s)!.
$$



In particular, no support proof below deletes the factorial force, extends HIGH, or changes the finite pole cutoff.

---

## 2. Discharging the coarse supported-return obligation

### 2.1 Why the old proof requires an additional explicit calculation

Turn 12 correctly required control of the full numerator


$$
(\widehat E-E_0)p
$$


one digit before division. Merely knowing that the numerator is integral and supported modulo $3^r$ would not prove a statement about its quotient modulo $3^r$.

The attached full closure now permits that calculation. The right way to do it is to cancel the top term **algebraically**, rather than separately dividing two approximate top-pole expressions.

Put $x=y-1$, and define


$$
T_0(f,g)=[y^{r_*}]x^Afg,\qquad
T_1(f,g)=[y^{r_*}]yx^Afg,
\quad r_*=\frac{3H-1}{2}.
$$


Let $\mathcal L_<$ denote the complete remaining normalized core form: all poles other than the unique top pole, together with the factorial contribution divided by $3$. Thus, exactly,


$$
G_c(f,g)=\beta T_0(f,g)+3T_1(f,g)+3\mathcal L_<(f,g).
\tag{2.1}
$$


Every pole coefficient in $\mathcal L_<$ is integral.

For a HIGH polynomial $p$, write its monic division as


$$
p=Ur+\pi(p),\qquad \pi(p)=x^DQ,
$$


and put


$$
\eta=Xp-Lr=\frac{G_c(U,\pi(p))}{3}.
\tag{2.2}
$$


The top coefficient in the LOW pairing is absent by the original degree bounds. Hence this division is legitimate without a top-pole loss.

Since


$$
\widehat E=E_Y-3X^TL^{-1}X,
$$


we have


$$
\widehat Ep=G_c(Y,\pi(p))-3X^TL^{-1}\eta.
\tag{2.3}
$$


The top matrix kills the remainder $Ur$, so


$$
E_0p=T_0(Y,\pi(p)).
$$


Substituting (2.1) into (2.3) gives the exact identity


$$
\boxed{
Fp=
\frac{\beta-1}{3}T_0(Y,\pi(p))
+T_1(Y,\pi(p))
+\mathcal L_<(Y,\pi(p))
-X^TL^{-1}\eta.
}
\tag{2.4}
$$



This is the required division-safe formula. Equivalently, it gives the full numerator as $3$ times the displayed expression.

### 2.2 Precision and support consequences

Here $(\beta-1)/3\in\mathbb Z_3$. For the coarse grid


$$
\Omega_r=H/3^{r-1},
$$


all coefficients of $x^H\bmod3^r$ lie on the integer grid. The pole extractions in $\mathcal L_<$, at their respective weighted precisions, lie on the odd half-grid.

The old closure’s width inequality


$$
4(r+1)(D+2)+2D+2<\Omega_r/8
$$


therefore proves:

* $\eta\equiv0\pmod{3^r}$ for internal divisible copies;
* the corresponding remainder identification for lower-edge vectors modulo $3^r$;
* support of the three remaining terms in (2.4) on the stated half-grid and upper-edge modules;
* the lower-edge width increase at most $\nu+1=D/2$.

The factorial part of $\mathcal L_<$ has factor $3^{h-1}$, so $h\ge r+2$ is more than sufficient.

Thus (2.4) proves the needed numerator assertion modulo $3^{r+1}$, including its LOW subtraction. No missing digit is silently recovered from a width estimate.

### Audit conclusion

The attached old closure, supplemented by (2.4), proves the **coarse supported-return lemma used by A1turn7**. Its proof does not require $v_3(j)\ge r-2$: for these core operations, the relevant arithmetic conditions are $D$ even, $3\mid D$, $\beta\equiv1\pmod3$, the finite endpoints, and the displayed $h$ and width inequalities.

This does **not** automatically certify every sharper $W\mapsto W+1$ assertion on the larger windows of intervening reports. Those have different numerical scope. But A1turn7 deliberately uses the weaker width growth $D/2$, and that obligation is now discharged.

---

## 3. Producer jet and linear-force protection

The accepted saturation bounds imply, with the actual terminal length retained,


$$
R\equiv(y+1)x^{A-\kappa_p}B_p(x)\pmod{3^p},
\qquad \deg B_p\le\kappa_p.
$$


The conditions


$$
2v_3((A+1)!)\ge6+p,\qquad \kappa_p\le D
$$


are essential. In particular,


$$
\kappa_p\le D
\iff
6+p\le v_3\!\left(\frac{(A+1)!}{(A-D-1)!}\right).
$$



Using the supported-return result above gives supported exact representatives


$$
\widehat z_i^{\,c}\equiv x^D\psi_i\pmod{3^p},
\qquad
\deg\psi_i\le m-D,
$$


with width at most $pD/2$.

After endpoint subtraction and monic division by $y+1$, the relevant quotient is


$$
x^H x^{D-\kappa_p}B_p\psi_i\psi_j\pmod{3^p}.
$$


The condition


$$
(p+1)D<\frac{\Omega_r-1}{2},\qquad r=\max(6,p),
$$


separates its support from **every** pole that can survive modulo $3^p$. The factorial contribution vanishes at this precision.

Therefore A1turn7’s conclusion


$$
\Phi_R\in3^pM_\nu(\mathbb Z_3)
$$


passes under its stated inequalities.

Its fixed-window limitation also passes: the condition


$$
512(r+1)^2\,3^{r-1}(D/H)<1
$$


cannot provide unbounded precision on a fixed positive-width ratio window.

---

## 4. Exact Schur identity and the factor $3$ in the mixed force

In core-orthogonal coordinates, let


$$
T=K(W,\widehat Z^{\,c}),\qquad
E_{\rm act}=E_c+3^6K_{WW}.
$$


Exact elimination gives


$$
\boxed{
S_{\rm act}=S_c+3^6\Phi_R-3^{12}T^TE_{\rm act}^{-1}T.
}
\tag{4.1}
$$



The inverse estimate


$$
E_{\rm act}^{-1}\in3^{-1}M(\mathbb Z_3)
$$


follows from $E_c^{-1}\in3^{-1}M$ and the perturbation beginning at relative depth $5$.

The mixed-force factor is valid. Modulo $3$, replace $\widehat z_i^{\,c}$ by $z_i$; the endpoint-subtracted quotient has degree below $r_*$, since


$$
\deg(Rwz_i)\le A+d+m=r_*.
$$


Thus its top coefficient is absent and


$$
T=3T_1.
$$


With $J_{\rm act}=3E_{\rm act}^{-1}$, (4.1) becomes


$$
\boxed{
S_{\rm act}=S_c+3^6\Phi_R-3^{13}\mathcal Q,
\qquad
\mathcal Q=T_1^TJ_{\rm act}T_1.
}
\tag{4.2}
$$



All higher perturbation orders remain inside the actual inverse.

---

## 5. LOW inverse isotropy and the actual $\mathcal Q/3$

The LOW matrix satisfies


$$
L_{ab}=0\pmod3\quad(a+b\ge D),\qquad
L_{a,D-1-a}=1\pmod3.
$$


Reversal therefore gives


$$
(L^{-1})_{ab}=0\pmod3\quad(a+b<D-1).
$$



For $T_1=\binom ab$, the actual LOW force $a$ is supported modulo $3$ in its first $\kappa_1\le6$ rows. The proof correctly uses the top-pole degree exclusion before dividing by $3$; consequently, changes in the corrected column or in the terminal jet that are divisible by $3$ contribute only modulo $9$ before that division.

Since $D\ge486$, this initial-coordinate subspace is totally isotropic for $L^{-1}\bmod3$. Hence


$$
\boxed{\mathcal Q\in3M_\nu(\mathbb Z_3).}
$$



The exact next expression is also correct:


$$
\mathcal Q
=a^TL_{\rm act}^{-1}a
+3\widetilde b^T\widehat E_{\rm act}^{-1}\widetilde b,
$$




$$
\widetilde b=b-X_{\rm act}^TL_{\rm act}^{-1}a,
$$


so


$$
\boxed{
\frac{\mathcal Q}{3}
=
\frac{a^TL_{\rm act}^{-1}a}{3}
+\widetilde b^T\widehat E_{\rm act}^{-1}\widetilde b.
}
\tag{5.1}
$$


This is integral but not evaluated. No nonzero digit at order $14$ has been proved.

---

## 6. Depth $14$, endpoint transport, and determinant-pair signs

On A1turn7’s fixed original-index window


$$
j\equiv81\pmod{243},\qquad
\frac1{2C_{16}}<D/H<\frac1{C_{16}},
$$


the accepted rotation reachability gives infinitely many original indices. For sufficiently large such indices,


$$
S_c\in3^{17}M,\qquad \Phi_R\in3^9M,\qquad \mathcal Q\in3M.
$$


Therefore


$$
S_{\rm act}\in3^{14}M.
$$



The exact transported endpoint is


$$
e_{\rm act}
=e_c-3^6T^TE_{\rm act}^{-1}w
=e_c-3^6T_1^TJ_{\rm act}w.
$$


Both equalities and their powers of $3$ are correct.

Define


$$
\Upsilon=\mathcal Q/3-\Phi_R/3^8-S_c/3^{14}.
$$


Then


$$
S_{\rm act}=-3^{14}\Upsilon.
$$


With


$$
\mathcal D_0=\det\Upsilon,\qquad
\mathcal D_1=e_{\rm act}^T\operatorname{adj}(\Upsilon)e_{\rm act}
-3^{14}d_{\rm act}\det\Upsilon,
$$


the exact pair is


$$
\det G_{\rm act}
=\det E_{\rm act}(-3^{14})^\nu\mathcal D_0,
$$




$$
v^T\operatorname{adj}(G_{\rm act})v
=\det E_{\rm act}(-3^{14})^{\nu-1}\mathcal D_1.
$$


The minus sign in $\mathcal D_1$ is necessary and correct.

When $\mathcal D_0\mathcal D_1\ne0$,


$$
\frac{\beta_1}{\beta_0}
=-\frac{3^{h-14}Q_n^{\rm loc}(-1)}4
\frac{\mathcal D_1}{\mathcal D_0},
$$


and therefore


$$
\boxed{
v_3(q)=
\max\!\left\{0,\,
h-14+v_3(Q_n^{\rm loc}(-1))
+v_3(\mathcal D_1)-v_3(\mathcal D_0)
\right\}.
}
\tag{6.1}
$$



The actual endpoint cannot be replaced by $Q_c(-1)=0$.

### Remaining A1 obstruction

The core inverse loss satisfies $s_c\ge17$, whereas the guaranteed actual-core protection is only $14$. Thus the relative criterion $N>s_c$ fails.

The remaining lemma is still a **relative actual determinant-pair theorem**, including nonvanishing. Common depth does not determine


$$
v_3(\mathcal D_1)-v_3(\mathcal D_0).
$$



---

# II. A2turn4: actual normal charge and unsaturated contact-lattice loss

## 7. Charge, projector, and both boundary currents

Retain the original family


$$
a=432827+682892t,\quad b=3^a,\quad n=2001b,
$$


with weighted coordinates $0\le j\le b$ and contact coordinates $0\le j<b$.

For


$$
\ell_j=\frac{\omega_b}{\omega_j},
$$


the exact reconstruction gives


$$
\ell_jZ_{w,j}
=\omega_b\left(
\frac{\theta_{j-1}}{(j-1)!}-\frac{\theta_j}{j!}
\right).
$$


The actual endpoints telescope to


$$
\boxed{\ell^TZ_w=0,\qquad \ell^TY=W_b.}
$$


The exterior $+1$ is precisely the nonzero affine charge.

The stated rising-factorial recurrence verifies


$$
\sum_{r=0}^{24}(5^{\overline r})^2\equiv8\pmod{29}.
$$


All later terms vanish modulo $29$, so this proves uniformly


$$
\mathscr S=\ell^T\ell\equiv8\pmod{29}.
$$


Thus


$$
\Pi=I-\ell\ell^T/\mathscr S
$$


is an integral self-adjoint projector onto the saturated module $\ell^\perp$.

The current


$$
\mathfrak c_k=-\frac{\omega_b}{29^2}
\frac{\theta_{k-1}}{(k-1)!}
$$


satisfies


$$
P_j\ell_j=\mathfrak c_{j+1}-\mathfrak c_j,
\qquad
\mathfrak c_0=\mathfrak c_{b+1}=0.
$$


Its integrality follows from $v_{29}(W_b)\ge3$ and the complete-force integrality of $\theta$.

The block telescoping retains the shorter final block and has both genuine exterior currents zero. It is not a solution of the remaining parallel defect.

---

## 8. Exact lift loss and fixed arithmetic

The projected exterior term has the unique contact lift


$$
\xi_j=\frac{j!}{b!\mathscr S}\sum_{i=0}^j\ell_i^2.
$$



For


$$
B=410910916,\qquad k=v_{29}(b-B)\ge9,\qquad j=b-B-1,
$$


the argument correctly yields


$$
v_{29}(\ell_j)=E_B,\qquad
v_{29}\!\left(\sum_{i=0}^j\ell_i^2\right)=2E_B.
$$


The latter uses the unit


$$
1+16\cdot8\equiv13\pmod{29},
$$


not an unsupported absence-of-cancellation assumption.

The finite Legendre sums give


$$
F_B=14675386,\qquad E_B=14675390,
$$


hence


$$
\boxed{v_{29}(\xi_{b-B-1})=14675394-k.}
\tag{8.1}
$$



Every factor in the fixed numerator product is below $29^9$, so the factorwise valuation stability for $k\ge9$ is justified.

The accepted original-parameter lifting bijection applies separately to each finite condition


$$
b\equiv B+29^k\pmod{29^{k+1}}.
$$


Thus the bad lifts occur at actual original indices, not at independently chosen auxiliary $b$'s.

Because the complete $\psi$ is integral,


$$
v_{29}((\psi+\xi)_{b-B-1})=14675394-k
$$


once the right side is negative.

**Normalization clarification:** this is the valuation of the divided coefficient vector reconstructing $Y^\parallel$, namely $\psi+\xi$. If “the contact lift of $Q^\parallel$” means the direct lift of $Q^\parallel=Y^\parallel/29^3$, its valuation is three lower. The report’s formulas themselves use the former convention consistently.

---

## 9. Skew-reconstruction: sufficient, correctly scaled, still open

The finite Gram identities


$$
29^4D=\theta^TK\theta,
$$




$$
29^5M=\theta^TK\psi+bW_b^2\theta_{b-1}
$$


retain the endpoint term and pass.

The proposed force identity implies


$$
\psi+\xi
=29s_n\theta+29\mathcal L(\mathcal K(g)Z_w).
$$


Reconstruction therefore gives


$$
Y^\parallel=29s_nZ_w+29\mathcal K(g)Z_w,
$$


and division by $29^3$ gives exactly


$$
Q^\parallel=s_nP+\mathcal K(g)P.
$$



Skew-adjointness then implies


$$
M=s_nD.
$$


For $s_n\equiv\rho_n\not\equiv0\pmod{29}$,


$$
v_{29}(M-\rho_nD)\ge v_{29}(D)+1,\qquad
v_{29}(M)=v_{29}(D).
$$



These are valid **conditional deductions**. No complete-force identity constructing $s_n$ and $g_j$ has been proved.

The actual obstruction is to an integral pullback in the original contact lattice. It is not an obstruction to a rational pullback of an integral skew operator on the saturated weighted space.

Accordingly, the exact denominator formula remains


$$
v_{29}(q_n)
=\max\{0,\,2F_n-F_b-1+\delta-\mu\},
$$


with $\delta-\mu$ still unknown.

---

# III. A5turn10: exact endpoint separation and a stronger theorem

## 10. Audit of the decomposition and changed force

The suffix identity


$$
\mathscr S_bE_d=\binom b{d+1}E_0-E_{d+1}
$$


gives, by induction,


$$
\mathscr S_b^vE_d=(-1)^vE_{d+v}+Q_{v,d;b},
\qquad \deg Q_{v,d;b}\le v-1.
$$


Its recurrence retains every endpoint constant.

Substitution into the complete contact formula, followed by Vandermonde, proves


$$
\boxed{
\mathscr C_{s;n,b}E_d
=(-1)^s\binom{n+d+s}{s}E_{d+s}+R_{s,d;n,b},
\quad \deg R_{s,d;n,b}\le s-1.
}
\tag{10.1}
$$



At $n=-190$, a bulk transition from $d<190$ across $190$ is exactly zero. Endpoint transitions remain present.

For the complete symbol, the ordinary-power denominator bound gives


$$
v_2(\lambda_s)\ge a(s):=L(s)-2\lfloor s/4\rfloor.
$$


This is valid for each expansion-order contribution as well as their truncated sum.

The changed force is also correct:


$$
F_i=\sum_{\ell=190}^i
\binom i\ell\frac{(i-190)!}{(\ell-190)!}B_\ell(-95)
\quad(i\ge190).
$$


The terms $\ell<190$ vanish exactly; they are not obtained by carrying over an old force residue.

Thus the reported precision-$138$ proof passes. Its path cases include high forcing degrees and endpoint overshoots. The following improvement makes fuller use of the same exact formulas.

---

## 11. New theorem: negative-continuation precision $180$

### Theorem
At


$$
h=-95,\qquad n=-190,\qquad b=-95/2001,
$$




$$
\boxed{\mathfrak p_{380}^{*}(-3)\in2^{180}\mathbb Z_2.}
\tag{11.1}
$$



### Proof

Work modulo $2^{180}$. The accepted complete filtration permits degree cutoff


$$
4\cdot180-1=719.
$$


Every contact application is expanded into its bulk and endpoint terms.

For $190\le i\le719$, the changed-force proof still gives


$$
v_2(F_i)\ge\lfloor i/2\rfloor-3.
\tag{11.2}
$$


Indeed,


$$
94+\lceil i/2\rceil\le454,
$$


whose possible binary digit sums are at most $8$. The same termwise derivation as in A5turn10 therefore applies.

### A. Paths having an endpoint transition

Choose the **last** endpoint transition on the path. Let its output degree be $e$.

All subsequent transitions are bulk transitions, so degrees only increase. A path ending at $380$ must have $e\le380$. Moreover, $e<190$ is impossible, because a subsequent bulk path cannot cross the barrier. Thus


$$
190\le e\le380.
$$



Put $x=e-190$. The endpoint transition uses symbol degree at least $e+1$, so its cost is at least $a(e+1)$.

If the subsequent bulk symbol degrees are $s_1,\ldots,s_q$, then


$$
\sum s_i=380-e=190-x.
$$


Combining the complete symbol bound with the exact telescoping multiplier gives bulk cost at least


$$
L(190)-L(x)-2\sum_i\lfloor s_i/4\rfloor
\ge184-L(x)-2\lfloor(190-x)/4\rfloor.
$$


The entire suffix beginning with the last endpoint injection therefore has cost at least


$$
a(x+191)+184-L(x)-2\lfloor(190-x)/4\rfloor.
\tag{11.3}
$$



Using $L(t)=t-s_2(t)$, this equals


$$
\begin{cases}
187+s_2(x)-s_2(x+191),&x\equiv0,3\pmod4,\\
185+s_2(x)-s_2(x+191),&x\equiv1,2\pmod4.
\end{cases}
$$



If $x\equiv0\pmod4$, digit subadditivity and $s_2(191)=7$ give a lower bound $180$. If $x$ is odd, adding $191$, whose six lowest bits are $1$, forces at least six carries, giving


$$
s_2(x+191)-s_2(x)\le1.
$$


If $x\equiv2\pmod4$, at least five carries are forced, giving a difference at most $2$. All cases are therefore at least $180$.

Every earlier part of the path has nonnegative valuation. In particular, earlier endpoint injections, excursions above degree $380$, and high forcing inputs cannot lower this bound.

### B. Paths having no endpoint transition

Such a path can reach $380$ only from forcing degree


$$
d=190+x,\qquad0\le x\le190.
$$


By (11.2) and the same bulk calculation, its cost is at least


$$
92+\lfloor x/2\rfloor+184-L(x)
-2\lfloor(190-x)/4\rfloor.
$$


For $x\bmod4=0,1,2,3$, this is respectively


$$
182+s_2(x),\quad181+s_2(x),\quad
181+s_2(x),\quad182+s_2(x).
$$


Every value is at least $182$.

Forcing inputs above $380$ cannot contribute without an endpoint transition and were already covered in Case A.

Thus every complete retained path vanishes modulo $2^{180}$. The filtration excludes all discarded paths at that same precision. ∎

### Interpretation

Precision $139$ is no longer informative for this coefficient. Neither is any precision through $180$.

This proof does **not** establish a nonzero residue at precision $181$, an infinite-depth zero, or a local factor $k+3$.

---

## 12. A uniform actual-cylinder consequence with an explicit denominator budget

The original family remains


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


The accepted precision-$96$ theorem remains valid on **all** these indices.

For the new result, one can make the fixed-precision transfer explicit, albeit very conservatively.

Let $L(t)=v_2(t!)$, and define


$$
\Delta=
2L(183)+179\bigl(L(179)+L(716)+716L(1436)\bigr).
\tag{12.1}
$$



A precision-$180$ polynomial representative $\Pi_{180}(k)$ can be constructed with


$$
2^\Delta\Pi_{180}(k)\in\mathbb Z_2[k].
$$



Here is the denominator bookkeeping:

* Central sums need only indices $s\le183$, since $L(184)=180$. The two parameter-binomial denominators cost at most $2L(183)$.
* Contact expansion orders satisfy $r\le179$, and symbol degree satisfies $s\le716$.
* Before a complete contact application is truncated, its degree is at most $719+716=1435$.
* The suffix recurrence contains at most $716$ endpoint-binomial factors per contact term, each with index at most $1436$.
* The remaining parameter binomials cost at most $L(179)+L(716)$.
* A surviving Neumann word has at most $179$ contact applications.

Newton shifts and products introduce no additional parameter denominator. Substitution of $h=32k+1$, $n=64k+2$, and $b=(32k+1)/2001$ introduces only odd denominators.

It follows that every original index satisfying


$$
\boxed{v_2(k+3)\ge180+\Delta}
\tag{12.2}
$$


has


$$
\boxed{\mathfrak p_{380}(u)\equiv0\pmod{2^{180}}.}
\tag{12.3}
$$



This is a uniform actual-family statement on an explicitly bounded cylinder, using the accepted original reachability of finite compatible refinements. It is not a claim about all original indices.

The bound is intentionally crude. More importantly, fixed depth $180$ still does not prove


$$
v_2(\mathfrak p_{380}^{*}(k))\ge v_2(k+3)-2.
$$


On arbitrarily deeper cylinders the required compensation continues to grow.

---

# IV. Consequences for full arithmetic and the next obligations

## 13. What changes—and what does not

### A1

The support dependency needed for the narrow-window depth-$14$ theorem is now closed. The unresolved local object is genuinely the exact actual pair


$$
(\mathcal D_0,\mathcal D_1),
$$


including nonvanishing and relative valuation.

The full gcd remains


$$
g_\ell=\gcd(|\ell^k\beta_0|,|\ell^k\beta_1|),
$$


and the whole error remains


$$
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
\det H_{\rm complete}.
$$



### A2

The normal projection preserves the actual norm and mixed scalar exactly. The unbounded loss belongs to the contact lift, not to weighted column content.

The open skew-force identity would settle $\delta-\mu=0$ at $29$, but not the all-prime denominator.

### A5

The new precision-$180$ theorem concerns one coefficient. It does not prove the complete grouped norm residual, the mixed contraction, or their relative valuation. It does not remove the second force, its exterior $+1$, or the logarithmic force.

For both weighted constructions, retain


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B,
$$


with the least actual clearer and primitive multiplier $d_B^2/g_B$. The whole evaluated error is


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$



The supplied signed-error asymptotics retain their existing hypotheses and proof status. The present local results do not establish sufficiently small growth of the actual $q_n$.

---

## 14. Concrete follow-on lemmas

The useful next targets are now:

1. **A1 — actual relative-pair lemma.**  
   Prove nonvanishing and a uniform bound or law for
   

$$
v_3(\mathcal D_1)-v_3(\mathcal D_0),
$$


   using the actual $\mathcal Q/3$, actual endpoint transport, and full radical.

2. **A2 — saturated full-force identity.**  
   Construct $s_n$ independently of $D$, together with an explicit integral weighted skew operator, satisfying the stated complete force identity. Its rational contact pullback must retain the unbounded losses proved above.

3. **A5 — last-endpoint injection lemma.**  
   Evaluate the complete endpoint injection into degrees $190,\ldots,380$, including its dependence on all retained input degrees, and propagate it through the triangular bulk inverse. This is now the precise source of the possible depth-$180$ contribution.

Even successful local lemmas would leave the same-index all-prime gcd and whole-error comparison.

---

## 15. Bounded exact arithmetic for personal inspection

No computation is required for the symbolic proofs above.

A useful next finite screen is:

* precision $p=181$;
* degree states $0,\ldots,723$;
* parameters $h=-95,n=-190,b=-95/2001$;
* complete expansion orders $1\le r\le180$;
* exact symbol coefficients, bulk binomials, and endpoint support $e<s$;
* complete force lower bounds, refined where necessary.

The expected verifiable output is:

1. a certified minimum path cost to degree $380$;
2. all last-endpoint transitions that can have total cost below $181$;
3. a certificate excluding discarded high degrees and expansion orders;
4. agreement of bulk-chain valuation sums with the exact factorial quotient.

A surviving path is only a candidate; it is not evidence of a nonzero coefficient. Any later coefficient evaluation must independently verify the full coefficient-valued residual using the original suffix/contact formula.

The two A2 arithmetic receipts—normal sums $8,13$ modulo $29$, and Legendre sums $14675386,14675390$—remain small, fixed checks of constants, not substitutes for original-family lifting.

---

## Final proof-status statement

The new results of this audit are:

* a division-safe complete-numerator identity closing A1turn7’s coarse supported-return dependency;
* verification of A1’s exact nonlinear and determinant-pair arithmetic;
* verification of A2’s actual unbounded contact-lattice obstruction, distinct from the open saturated relative alignment;
* the stronger negative-continuation theorem
  

$$
\boxed{\mathfrak p_{380}^{*}(-3)\in2^{180}\mathbb Z_2},
$$


  together with an explicit fixed-precision actual-cylinder transfer.

The exact remaining global bottleneck is unchanged: control the **actual full primitive denominator**, after the **full all-prime gcd**, on the same original indices for which the **whole evaluated error is nonzero and sufficiently small**.



$$
\boxed{\text{No unconditional proof or disproof of irrationality of }e+\pi
\text{ is obtained.}}
$$


