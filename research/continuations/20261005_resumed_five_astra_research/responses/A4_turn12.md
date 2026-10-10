> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 12 — Corrected-column audit and a uniform proof of the zero precision-$96$ coefficient

## Executive conclusions

The most decisive result of this audit is a **uniform polynomial identity for the complete binary contact operator**, not an extrapolation from the two supplied endpoint calculations.

Write $B_r(x)=\binom{x}{r}$, and let $\mathscr E_{n,b}$ be the complete contact operator with its suffix endpoint $b-1$. Then, coefficientwise in the integral Newton lattice,


$$
\boxed{
\begin{aligned}
\mathscr E_{n,b}(B_1+B_2+B_3)&\equiv B_3\pmod2,\\
\mathscr E_{n,b}B_3&\equiv0\pmod2,
\end{aligned}
\qquad n\equiv2\pmod8,\quad b\equiv1\pmod8.
}
$$


Consequently,


$$
\boxed{\mathscr E_{n,b}^{\,2}(B_1+B_2+B_3)\equiv0\pmod2.}
$$



The complete precision-$96$ filtration proposed by the coordinator is valid. Combining it with this identity proves


$$
\boxed{\mathfrak p_{380}^{*}(-3)\equiv0\pmod{2^{96}}.}
$$


In fact, the same proof applies on **every original binary index**


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0:
$$




$$
\boxed{\mathfrak p_{380}(u)\equiv0\pmod{2^{96}}.}
$$



This is one more uniform bit than the earlier envelope proved. It is **not** an all-depth coefficient-zero theorem, a local $k+3$ factorization, or a complete norm-residual theorem.

The other conclusions are:

1. **The exact central formulas close the earlier denominator qualification.** Their normalized scalar summands are $2$-integral, with valuation $v_2(s!)$; their falling prefactors give the required factorial central-index depths. Thus the earlier $4p-1$ envelope now has its formula-level dependency discharged.

2. **A1’s corrected-column localization argument is sound from its stated supported-propagation inputs.** It genuinely treats the complete corrected columns, including the LOW remainder restoration, rather than only the bare force. Exact supported lifts can be chosen without altering the original finite degree bounds. All six poles modulo $27$ are accounted for.

3. **A1’s extension to the next LOW/HIGH precision needs a more qualified audit verdict.** Its numerical precision budget is consistent, and its inverse-expansion conclusion follows from the displayed stronger propagation statement. But the new statement
   

$$
R_H\mathsf F_H:\mathcal C(W)\longrightarrow\mathcal C(W+1)\pmod{3^6}
$$


   at the refined scale is not proved by the width inequality alone. The attached packet does not reproduce the complete block formulas or the earlier propagation proof needed to verify that extension term by term. Accordingly, the claimed actual depth-eight operator remains a **conditional deduction from that extended complete-propagation lemma**, not an independently completed proof in this audit.

4. **The companion-integrality qualification is resolved.** The supplied defining recurrence proves $\alpha_r\in\mathbb Z[1/2]$ for every $r$, uniformly through the growing endpoint.

5. **The new $29$-adic receipt has precisely finite corroborative scope:** 29 seeds and 435 bounded auxiliary tails. It supplies no all-depth actual norm/mixed-product theorem.

No tools were executed. No external source was opened. The supplied literature gate is used only at its stated scope.

---

# I. Exact central formulas: the denominator dependency is now closed

## 1. The complete formulas and their integrality

The newly supplied formulas are


$$
\begin{aligned}
B_{2j}(h)
={}&
\left(\prod_{t=1}^{j}(2h+2t-1)\right)
(h)_{\underline j}\\
&\times
\sum_{s\ge0}
\frac{2^s(s!)^2}{(2s)!}
\binom{h-j}{s}\binom{h+j}{s},
\end{aligned}
\tag{1.1}
$$


and


$$
\begin{aligned}
B_{2j+1}(h)
={}&
\left(\prod_{t=0}^{j}(2h+2t+1)\right)
(h)_{\underline{j+1}}\\
&\times
\sum_{s\ge0}
\frac{2^s(s!)^2}{(2s+1)!}
\binom{h-j-1}{s}\binom{h+j}{s}.
\end{aligned}
\tag{1.2}
$$



These formulas are sufficient to inspect every denominator relevant to the earlier argument.

Let $L(s)=v_2(s!)$. Since


$$
v_2((2s)!)=s+L(s),\qquad
v_2((2s+1)!)=s+L(s),
$$


both normalized scalar factors have valuation


$$
v_2\!\left(\frac{2^s(s!)^2}{(2s)!}\right)
=
v_2\!\left(\frac{2^s(s!)^2}{(2s+1)!}\right)
=L(s).
\tag{1.3}
$$



After extracting $2^{L(s)}$, the remaining rational factor is a $2$-adic unit. There is no hidden even denominator.

For every fixed $s$, the binomial polynomials $\binom{h+c}{s}$ are integral-valued on $\mathbb Z_2$. Hence every central summand is integral, and its valuation is at least $L(s)$. Because $L(s)\to\infty$, the sums converge uniformly for $h\in\mathbb Z_2$.

Moreover,


$$
(h)_{\underline j}=j!\binom hj,\qquad
(h)_{\underline{j+1}}=(j+1)!\binom h{j+1}.
$$


All other prefactor factors are integral. Therefore


$$
\boxed{
v_2(B_{2j}(h))\ge L(j),\qquad
v_2(B_{2j+1}(h))\ge L(j+1)
}
\tag{1.4}
$$


uniformly on $\mathbb Z_2$.

### Correction to an incidental statement in old A5 Turn 20

The assertion


$$
h\equiv1\pmod{32}\Longrightarrow v_2(h-1)=5
$$


is false as written: that congruence gives only $v_2(h-1)\ge5$.

This does not damage the application. On the actual cylinder,


$$
h\equiv161\pmod{256},
$$


one does have $v_2(h-1)=5$. The weaker inequality would also suffice for the stated tail omission.

## 2. The complete forcing envelope

The complete first force is


$$
F_i(h,n)=
\sum_{\ell=0}^{i}
\binom i\ell
(n+i)_{\underline{i-\ell}}B_\ell(h).
\tag{2.1}
$$



A product of $q$ consecutive $2$-adic integers is divisible by $q!$. Combining this with (1.4), including the binomial coefficient in (2.1), yields the previously derived bound


$$
\boxed{
v_2(F_i(h,n))
\ge w_i:=L\!\left(\left\lfloor\frac i2\right\rfloor\right).
}
\tag{2.2}
$$



For completeness, if $i=2m$ and $\ell=2j$, the summand depth is at least


$$
v_2\binom mj+L(j)+L(2m-2j)
=L(m)+(m-j).
$$


The odd-$\ell$ case gives at least


$$
L(m)+(m-j)+v_2(j+1).
$$


For $i=2m+1$, the analogous two lower bounds are


$$
L(m)+(m-j),\qquad
L(m)+(m-j)+v_2(j+1).
$$


Thus every complete summand has depth at least $L(m)$.

In particular,


$$
i-4w_i\le3.
\tag{2.3}
$$



Together with integral contact transport, this proves the established envelope


$$
\boxed{\deg P_p\le4p-1\pmod{2^p}}
\tag{2.4}
$$


without the earlier missing-formula qualification.

The relevant integrality is that of the **Newton coefficient lattice**. It is not a claim that all ordinary-power coefficients have odd denominators.

---

# II. The complete precision-$96$ reduction passes

## 3. Original family and continued parameters

The original family remains


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


with


$$
b=128D+81,\qquad C=4002D+2532,\qquad k=2C+1,
$$


and


$$
h=32k+1,\qquad n=64k+2,\qquad b=\frac{32k+1}{2001}.
$$



At the continued parameter $k=-3$,


$$
h=-95,\qquad n=-190,\qquad b=-95/2001.
\tag{3.1}
$$



These are parameters of polynomial continuation, not dimensions of a negative-sized matrix.

Both the original family and (3.1) satisfy


$$
h\equiv161\pmod{256},\qquad
n\equiv322\pmod{512},\qquad
b\equiv209\pmod{256}.
\tag{3.2}
$$


In particular,


$$
v_2(h-1)=5,\qquad n\equiv2\pmod8,\qquad b\equiv1\pmod8.
\tag{3.3}
$$



The actual contact matrices still have indices $0\le i,j<b$. Coefficient $380$ is determined by the original rows $0,\ldots,380$, all of which exist on this family.

## 4. The additional factorial depth in a contact order

Write


$$
U=-z^{[1]}+2z^{[2]}-3z^{[3]}+3z^{[4]}.
$$


The contact-symbol contribution of order $r$ is


$$
2^r\binom hr U^r.
\tag{4.1}
$$



The assertion that $U^r$ is coefficientwise divisible by $r!$ in the divided-power lattice is valid.

One way to see it is to expand by multiplicities of the positive degrees $1,2,3,4$. After dividing a coefficient by $r!$, the remaining factorial quotient counts partitions of a labelled set into unordered blocks of those sizes, multiplied by integral powers of the coefficients of $U$. Thus it is an integer. The absence of a constant term is important.

Consequently, (4.1) has coefficientwise depth at least


$$
r+v_2((h)_{\underline r}).
\tag{4.2}
$$


When $r\ge2$, the falling product contains $h-1$, so on (3.2),


$$
v_2((h)_{\underline r})\ge5.
\tag{4.3}
$$



This stronger symbol bound transfers through the integral contact operator. No multiplicativity of contact transport is being assumed.

## 5. Every word containing an order $r\ge2$ is irrelevant to degree $380$

Consider a contact word of total symbol order $R$, originating from forcing index $i$. If at least one occurrence has order at least two, its valuation is at least


$$
w_i+R+5,
$$


while its degree is at most $i+4R$.

To survive modulo $2^{96}$, it must satisfy


$$
w_i+R+5\le95.
$$


Hence


$$
i+4R
\le4(w_i+R)+3
\le363.
\tag{5.1}
$$


It cannot contribute to coefficient $380$.

This argument includes all endpoint-generated lower-degree terms: it uses a degree bound for the **whole contact image**, not only its interior leading term.

## 6. Repetitions of the order-one operator

Only repetitions of


$$
\mathscr K_1=2h\mathscr E_{n,b}
$$


remain relevant.

A word of length $q$ originating in degree $i$ has depth at least $q+w_i$ and degree at most $i+4q$.

### Lengths $q\le93$

Put $z=95-q\ge2$. To reach degree $380$, one needs


$$
i\ge380-4q=4z.
$$


Then


$$
w_i\ge L(2z)\ge z+1.
$$


The last inequality follows because the even factors alone contribute $z$, while $z!$ contributes at least one more for $z\ge2$.

Thus


$$
q+w_i\ge q+z+1=96.
$$


These words vanish modulo $2^{96}$.

### Length $q=94$

Survival requires $w_i\le1$, hence $i\le7$. Reaching degree $380$ requires $i\ge4$.

The complete force transfer supplied by the central formulas gives


$$
(F_0,\ldots,F_7)
\equiv(2,9,51,57,12,36,48,16)\pmod{64}
\tag{6.1}
$$


on (3.2), including at the continued parameter.

In particular,


$$
F_4,F_5,F_6,F_7\equiv0\pmod4.
$$


These words also vanish modulo $2^{96}$.

This transfer is legitimate: the retained central indices and summation indices are first justified by uniform tail bounds, and only then are their finite parameter-dependent values transferred. It is not a lift of an old force residue to arbitrary precision.

### Length $q=95$

Only $i\le3$ can survive. From (6.1),


$$
(F_0,F_1,F_2,F_3)\equiv(0,1,1,1)\pmod2.
$$


Signs disappear modulo two, so the input is


$$
g=B_1+B_2+B_3.
\tag{6.2}
$$



Since $h$ is odd, the proposed reduction is therefore correct:


$$
\boxed{
\frac{\mathfrak p_{380}}{2^{95}}
\equiv[B_{380}]\,\mathscr E_{n,b}^{95}g\pmod2.
}
\tag{6.3}
$$


It holds at the continued parameter and on the entire original family.

---

# III. A uniform identity for the complete $\mathbb F_2$ operator

## 7. Preserve the suffix endpoint before reducing

Let


$$
\mathscr S_b B_r(x)=B_{r+1}(b)-B_{r+1}(x).
\tag{7.1}
$$


The exact finite identity


$$
\mathscr T_{v,b}=\mathscr S_b^{\,v}
\tag{7.2}
$$


retains the original endpoint $b-1$, and then extends by polynomial continuation.

Modulo two, the complete contact operator is particularly simple. Since


$$
(c_1,c_2,c_3,c_4)\equiv(1,0,1,1)\pmod2
$$


and


$$
\binom nv\equiv1\pmod2
\quad\Longleftrightarrow\quad v=0,2
\qquad(0\le v\le4,\ n\equiv2\pmod8),
$$


we obtain


$$
\begin{aligned}
\mathscr E f(x)\equiv{}&
B_1(x)f(x-1)+B_3(x)f(x-3)+B_4(x)f(x-4)\\
&+B_1(x)\mathscr S_b^2f(x-1)
+B_2(x)\mathscr S_b^2f(x-2)
\pmod2.
\end{aligned}
\tag{7.3}
$$



No interior-only replacement has been made.

If $b\equiv1\pmod8$, then


$$
B_r(b)\equiv0\pmod2\qquad(2\le r\le5).
$$


Equation (7.1) therefore gives


$$
\mathscr S_b^2g\equiv B_3+B_4+B_5,\qquad
\mathscr S_b^2B_3\equiv B_5.
\tag{7.4}
$$


This is where the finite endpoint enters the identity.

## 8. Exact verification in the eight residue classes

Every polynomial appearing after applying (7.3) to $g$ or $B_3$ has Newton degree at most seven. Modulo two, each $B_r(x)$, $r<8$, depends only on $x\bmod8$.

Substituting (7.4) into (7.3), using Lucas’s formula for these three binary digits, gives


$$
\begin{array}{c|rrrrrrrr}
x\bmod8&0&1&2&3&4&5&6&7\\ \hline
g(x)&0&1&1&1&0&1&1&1\\
(\mathscr E g)(x)&0&0&0&1&0&0&0&1\\
(\mathscr E B_3)(x)&0&0&0&0&0&0&0&0.
\end{array}
\tag{8.1}
$$



This is an exhaustive symbolic residue calculation, not a sampled large-endpoint experiment. The Newton evaluation matrix on $0,\ldots,7$ is unit lower triangular. Thus the table proves coefficientwise identities:


$$
\boxed{\mathscr E g=B_3,\qquad \mathscr E B_3=0\quad\text{modulo }2.}
\tag{8.2}
$$



They hold uniformly for every $2$-adic parameter pair


$$
n\equiv2\pmod8,\qquad b\equiv1\pmod8.
$$



In particular,


$$
\mathscr E^{95}g=0\pmod2.
$$


Equation (6.3) now proves


$$
\boxed{
\mathfrak p_{380}^{*}(-3)\in2^{96}\mathbb Z_2,
\qquad
\mathfrak p_{380}(u)\in2^{96}\mathbb Z_2
\quad(u\ge0).
}
\tag{8.3}
$$



## 9. What the identity does and does not improve

The identity implies that, on the cyclic $\mathbb F_2$-space generated by $g$,


$$
(I+2h\mathscr E)^{-1}g
\equiv g-2h\mathscr E g\pmod8,
\tag{9.1}
$$


because the residual is


$$
-(2h)^2\mathscr E^2g\in8\operatorname{Int}(\mathbb Z_2).
$$


This is a small, division-safe inverse improvement for that input.

It does **not** imply that $\mathscr E^2$ is zero on the whole Newton lattice. Nor does it imply repeated extra divisibility for arbitrary lifted inputs. In particular, the complete force is not exactly $g$, and the complete contact operator is not exactly $2h\mathscr E$.

The dangerous individual moment is now proved integral through one additional reachable depth:


$$
v_2\!\left(
\frac{\mathfrak p_{380}a_{380}(2n)\mathcal M_{380}(0)}
{\mathcal B_0}
\right)
\ge98-\ell.
$$


Thus the established range becomes


$$
\boxed{5\le\ell=v_2(k+3)\le98.}
\tag{9.2}
$$



Unbounded-depth compensation remains unproved.

### Assessment of the supplied binary certificate

The supplied code implements the complete suffix sums and the correct surviving $v=0,2$ contact terms. Its two endpoint representatives are consistent with the continuation.

The reported zero vectors are now explained by (8.2). The certificate is useful corroboration, but it is no longer the proof of the precision-$96$ conclusion.

---

# IV. A1: complete corrected-column force localization

## 10. Domain and finite boundaries

Retain exactly


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$




$$
A=n-2=H-D,\qquad H=3^{h-1},\qquad0<D<H/972,
$$


and


$$
m=(A+1)/2,\qquad d=3D/2-1,\qquad \nu=D/2-1.
$$



The columns remain


$$
U_a=(y-1)^a\quad(0\le a<D),
$$




$$
z_i=y^i(y-1)^D\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m).
$$



The accepted producer interface and its audited factorial consequence give


$$
R(y)\equiv(y+1)(y-1)^{A-\kappa}B_3(y-1)\pmod{27},
\qquad \deg B_3\le\kappa\le9.
\tag{10.1}
$$


The signed producer denominator


$$
\eta_n=((n-1)!)^2-u^T\mathsf T_n^{-1}u
$$


is still retained; it has not been replaced by a unit.

## 11. The corrected columns—not merely the bare columns

The exact core-corrected column is


$$
\widehat z_i^{\,c}
=z_i-Yp_i+UL^{-1}Xp_i-UL^{-1}B_i,
\tag{11.1}
$$


with


$$
p_i=3\widehat E^{-1}\widetilde V_i^{\,T}.
$$



A1 uses


$$
p_i\equiv
3R_HV_i^T-9R_H\mathsf F_HR_HV_i^T\pmod{27}.
\tag{11.2}
$$



The precision requirements implicit in this formula are modest but must be explicit:

* $R_HV_i^T$ must have the required supported representative modulo $9$;
* $R_H\mathsf F_HR_HV_i^T$ needs it modulo $3$;
* the LOW remainder restoration must hold modulo $27$ after multiplication by the displayed factors.

Under the retained propagation hypotheses, these requirements are met.

### Exact supported, divisible lifts

There is no need to divide an arbitrary congruence by three.

Choose finite polynomial representatives $a_i,b_i$ for the two terms in (11.2), with their asserted support after removal of the $x^D$-remainder. Then


$$
p_i^{\mathrm{lift}}=3a_i-9b_i
$$


is exactly divisible by three and congruent to $p_i\pmod{27}$. All representatives can retain degree at most $m$.

Because division by the monic polynomial $x^D$, $x=y-1$, is integral, the supported quotients can be lifted coefficientwise without adding higher finite coordinates. The complete LOW term restores precisely the removed remainder. Since $B\equiv0\pmod{27}$,


$$
\boxed{
\widehat z_i^{\,c}\equiv x^D\psi_i\pmod{27},
\quad
\deg\psi_i\le m-D,
\quad
\operatorname{supp}\psi_i\subseteq I_\Omega(\nu+1),
}
\tag{11.3}
$$


where $\Omega=H/243$.

This closes the distinction left open by Turn 10’s bare-force theorem.

## 12. Endpoint subtraction, support, and every pole

Using (10.1) and (11.3),


$$
\frac{R\widehat z_i^{\,c}\widehat z_j^{\,c}
-(R\widehat z_i^{\,c}\widehat z_j^{\,c})(-1)}{y+1}
\equiv
x^H\,x^{D-\kappa}B_3(x)\psi_i\psi_j
\pmod{27}.
\tag{12.1}
$$


The endpoint subtraction is legitimate because $R(-1)\equiv0\pmod{27}$. Monic division by $y+1$ preserves the congruence.

The factor outside $x^H$ has support in $I_\Omega(2D)$, since


$$
\deg(x^{D-\kappa}B_3)\le D,\qquad
2(\nu+1)=D.
$$


Also,


$$
x^H\equiv(y^{H/9}-1)^9\pmod{27},
\qquad H/9=27\Omega.
$$


Thus the quotient remains supported in $I_\Omega(2D)$.

The complete pole set modulo $27$, at the original finite cutoff, consists of


$$
\frac{3H-1}{2},\qquad
\frac{H-1}{2},\qquad
\frac{cH/3-1}{2}\quad(c=1,5,7,11),
$$


with weights respectively


$$
1,\quad3,\quad9c^{-1}.
$$


All lie on $J_\Omega(0)$. Since $\Omega>4D$, the support sets are disjoint. The factorial contribution vanishes at this precision by the retained valuation estimate.

Therefore


$$
\boxed{\Phi_R\equiv0\pmod{27}}
\tag{12.2}
$$


follows for the complete corrected columns, from the stated supported-propagation inputs. The loss-one Schur perturbation interface then gives


$$
\boxed{\mathscr R_{\rm act}\equiv\mathscr R_c\pmod{3^9}.}
\tag{12.3}
$$



This is actual force transfer. It is not an assertion that $R$, $B_3$, or the exact force is zero.

---

# V. A1: extended precision and the actual depth-eight claim

## 13. What the precision arithmetic does establish

On


$$
D<H/2916,\qquad \Omega'=H/729,
$$


the claimed margin


$$
\Omega'-4D\ge3^t\ge243
$$


is sufficient for the displayed widths.

For the LOW coupling, the polynomial degree excludes the top pole exactly. Consequently, dividing $G_c(U_a,z_i)$ by three does not require an additional digit for that absent pole. The congruence


$$
x^H\equiv(y^{\Omega'}-1)^{729}\pmod{3^7}
$$


is correct. Subject to the stated identification of the remaining poles and factorial valuation, the proof of


$$
B\in3^7M
$$


has the right precision.

For HIGH, suppose the complete refined propagation statement is valid:


$$
R_H\mathsf F_H:\mathcal C(W)\to\mathcal C(W+1)\pmod{3^6},
\tag{13.1}
$$


together with $R_HV^T\in\mathcal C(\nu)\pmod{3^7}$.

Then the inverse-expansion accounting is correct:

* the $\ell=0$ contraction needs and is asserted to have modulus $3^7$;
* every $\ell\ge1$ term carries $3^\ell$, so a modulus-$3^6$ contraction suffices for modulus $3^7$;
* omitted terms have at least $3^7$;
* the maximal contraction width $2D+4$ lies strictly below the half-grid separation.

There is no implicit need for modulus $3^7$ in every propagated $\ell\ge1$ contraction.

## 14. The unresolved proof detail in the extension

However, a stronger window does not by itself prove (13.1). To establish it, one must inspect the complete numerator


$$
\widehat E-E_0
$$


before division by three, including the LOW subtraction and the top-pole cancellation, modulo $3^7$.

The attached report states that the earlier proof extends, but does not reproduce the needed complete block calculation. The earlier Turn 4 source is not attached. Thus I cannot independently certify this new modulus solely from the displayed width inequalities.

A concrete missing lemma is:

> **Refined supported-return lemma.** For each exact finite supported lift $p$ in the relevant class, prove coefficientwise, with the original HIGH interval $d\le a,b\le m$, that
> 

$$
> R_H(\widehat E-E_0)p
>
$$


> has an exactly divisible-by-three representative whose quotient, after the complete LOW remainder restoration, belongs to $\mathcal C(W+1)\pmod{3^6}$. The proof must evaluate the full numerator modulo $3^7$, including every surviving pole and the factorial part.

This is a specific formula-level obligation, not a request for a large numerical test.

## 15. What follows conditionally for depth eight

If that refined lemma is supplied, the whole numerator satisfies


$$
\mathscr R_{\rm act}\equiv
G_c(Z,Z)-9V\widehat E^{-1}V^T
+3^8\mathcal K_{\rm LOW}+3^6\Phi_R
\equiv G_c(Z,Z)\pmod{3^9}.
$$


All corrections are then individually divisible by $3^9$, so division by $3^8$ is safe.

Using the retained beta-moment stripping calculation gives


$$
\frac{\mathscr R_{\rm act}}{3^8}\equiv\mathcal C_8\pmod3,
\qquad
(\mathcal C_8)_{ij}
=[y^{(H/2187-1)/2-i-j}](y-1)^D,
$$


on the unchanged range


$$
0\le i,j<D/2-1.
$$



The endpoint is transported by the actual Schur formula


$$
e_{\rm res}
=Z(-1)^T-C_{\rm act}^TE_{\rm act}^{-1}W(-1)^T.
$$


Modulo three, the protected corrections vanish and


$$
\overline e_8=\bigl((-1)^i\bigr)_{0\le i<\nu}.
$$



The shortened terminal residue class has size $s-1$, not $s$, in the decomposition $D=2\cdot3^t s$. Hence the exceptional coupling remains genuinely rectangular. Its singularity conclusion is a valid consequence of the accepted binomial residue algebra.

The distinction is:

* the finite algebra proves singularity of the displayed binomial matrix;
* its identification with the **actual** depth-eight digit additionally requires the complete refined return lemma.

---

# VI. Companion integrality and the $29$-adic receipt

## 16. The companion qualification is resolved uniformly

The supplied defining series is


$$
\sum_{r\ge0}\alpha_rz^r=\frac1{1-z+z^2/2}.
$$


Multiplication gives


$$
\alpha_0=\alpha_1=1,\qquad
\alpha_r=\alpha_{r-1}-\frac12\alpha_{r-2}.
$$


Induction proves


$$
\boxed{\alpha_r\in\mathbb Z[1/2]\quad\text{for every }r.}
$$



Equivalently, $\beta_r=2^r\alpha_r$ satisfies


$$
\beta_0=1,\quad\beta_1=2,\quad
\beta_r=2\beta_{r-1}-2\beta_{r-2},
$$


so $\beta_r\in\mathbb Z$.

This supplies exactly the odd-prime integrality needed in the companion-divisibility proof, uniformly through its growing force endpoint. The resulting conclusion remains


$$
v_p(v_0)\ge v_p(n)
$$


under the earlier hypotheses, not an exact valuation formula.

## 17. The new $29$-adic compression receipt

The receipt reports:

* 29 finite seeds;
* 435 bounded auxiliary-tail comparisons;
* all comparisons passing;
* maximum seed degree 42;
* zero scalar at the stated $z=9,\ R\equiv28\pmod{29}$ prefix.

These outputs agree with the earlier symbolic seed-degree and annihilation arguments. The receipt does not display the full comparison data, and I have not recomputed it.

Its proper status is finite corroboration. It neither proves nor strengthens an all-depth actual norm/mixed-product relation. In particular, a vanishing normalized scalar still provides only the established absolute lower bounds; it does not control cancellation one digit beyond an arbitrarily deep actual norm.

---

# VII. Full primitive normalization and the whole error

None of the new local results replaces the final gcd.

For the two-column constructions, retain the least actual clearer $d_B$, the integer columns $N_B=d_B[u,v]$, and


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


Then


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
$$


All primes are included. The whole evaluated error is


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$



The binary coefficient result does not determine the actual norm and mixed-product valuations, their difference, or the full primitive denominator.

For A1, retain


$$
A_\ell=\ell^k\beta_0,\qquad B_\ell=\ell^k\beta_1,\qquad
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


When $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
\det H_{\rm complete}.
}
$$



Producer endpoint nonvanishing does not establish $B_\ell\ne0$ or nonvanishing of the complete determinant error. Likewise, modular nilpotence does not establish real vanishing of any complete evaluated error.

---

# VIII. Next lemmas and bounded exact arithmetic

## 18. No dense precision-$96$ calculation is now needed

The uniform proof above replaces the proposed dense calculation at precision $96$.

An optional compact exact certificate has the following inputs:

* the Newton basis $B_0,\ldots,B_7$;
* $n=2,\ b=1$, interpreted by the suffix polynomial recurrence;
* $g=B_1+B_2+B_3$;
* the complete operator (7.3).

Its expected coefficient outputs modulo two are


$$
[\mathscr E g]_{B_0,\ldots,B_7}
=(0,0,0,1,0,0,0,0),
$$




$$
[\mathscr E B_3]_{B_0,\ldots,B_7}
=(0,0,0,0,0,0,0,0).
$$


The parameter reduction to these representatives is proved above; it is not supplied by the computation.

## 19. The next informative binary calculation starts at precision $97$

The next coefficient question is


$$
\mathfrak p_{380}^{*}(-3)\pmod{2^{97}}.
$$


The only possible residues, given the theorem, are


$$
\boxed{0\quad\text{or}\quad2^{96}.}
$$



A bounded exact calculation may use:

* $p=97$;
* $h=-95,\ n=-190,\ b=-95/2001$;
* complete central sums with $L(s)<97$;
* force indices satisfying $w_i<97$;
* complete contact words surviving the valuation filtration;
* Newton degree through $4p-1=387$;
* the exact suffix recurrence, retaining every endpoint constant.

Words containing any order $r\ge2$ still cannot reach coefficient $380$: their surviving degree is at most


$$
4(96)-20+3=367.
$$


Thus the coefficient calculation can restrict to repetitions of the order-one operator, but must retain the higher force digits and the higher residues of that operator. The modulo-two nilpotence alone does not evaluate them.

Expected verifiable outputs are:

1. the residue $0$ or $2^{96}$;
2. compatibility with zero modulo $2^{96}$;
3. a coefficient-valued inverse residual at the stated precision;
4. exact endpoint dependence, without replacing $b$ by an unjustified small finite boundary.

For the unbounded compensation problem, the sharper mathematical target remains a local factorization or quantitative estimate such as


$$
\mathfrak p_{380}^{*}(k)=(k+3)G(k),
\qquad G(k)\in2^{-2}\mathbb Z_2,
$$


on the relevant neighborhood. Even vanishing at the single limit point would not by itself prove this bound.

---

# Final result and proof status

The principal new theorem is


$$
\boxed{
\mathscr E_{n,b}g\equiv B_3,\qquad
\mathscr E_{n,b}B_3\equiv0\pmod2
}
$$


for the complete endpoint-preserving operator when $n\equiv2\pmod8$, $b\equiv1\pmod8$. Combined with the audited filtration and complete central-force transfer, it proves


$$
\boxed{
\mathfrak p_{380}^{*}(-3)\equiv0\pmod{2^{96}},
\qquad
\mathfrak p_{380}(u)\equiv0\pmod{2^{96}}
\ \text{for every original }u.
}
$$



The earlier central-formula and companion-coefficient integrality qualifications are resolved.

For A1, the complete corrected-column force localization passes from its stated supported-propagation inputs. The remaining independent-audit bottleneck for the claimed actual depth-eight transfer is the **refined complete HIGH propagation calculation modulo $3^6$, obtained by division from its full numerator modulo $3^7$**. Width separation and the inverse-series budget are sufficient only after that lemma is proved.

Globally, the work still lacks a same-index infinite family whose **actual full primitive denominator** and **whole nonzero evaluated error** satisfy


$$
0<|q_n(e+\pi)-p_n|\longrightarrow0.
$$





$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


