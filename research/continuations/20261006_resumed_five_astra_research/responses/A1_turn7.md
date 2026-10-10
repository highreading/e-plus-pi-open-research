> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1turn7 — The full pure-Jacobi endpoint polynomial and a factorial cancellation for the complete core scalar

## Executive conclusion

I leave the accepted suffix synchronization and the controlled-growth inverse-comparison exclusion closed. In particular, I do not infer unit normalization outside its established family.

The advance here is along the **pure-Jacobi plus factorial-perturbation route**. It has three parts:

1. **An explicit formula for the full reproducing polynomial $P_J$ at $y=-1$**, including the actual Christoffel modification, Jacobi leading coefficients, and norms. This is the endpoint polynomial on the entire original space $\mathcal P_m$, not a residual or endpoint-unit substitute.

2. **A target-specific cancellation in the complete factorial contraction.** On the controlled-growth branch with the retained normalization
   

$$
\mathfrak a\equiv25\pmod{27},
$$


   put
   

$$
s=h-2-2r,\qquad U=3^sP_J\in\mathbb Z_3[y].
$$


   Then
   

$$
\boxed{[y]U\equiv0\pmod3}
$$


   and consequently
   

$$
\boxed{\mathfrak f(Q_cU^2)\equiv0\pmod3.}
$$


   This cancellation uses the actual endpoint kernel and the actual factor $Q_c$. It is not a consequence of the factor $3^h$ alone.

3. **An explicit leading-residue formula for the complete core scalar response**, including all higher factorial corrections. Write $u_i=[y^i]U$. Then
   

$$
\boxed{
   K_c-K_J\in3^{h-2s+1}\mathbb Z_3,
   }
$$


   where
   

$$
K_J=v^TG_J^{-1}v,\qquad K_c=v^TG_c^{-1}v,
$$


   and, more precisely,
   

$$
\boxed{
   \frac{K_c-K_J}{3^{h-2s+1}}
   \equiv
   2u_0\left(\frac{u_1}{3}+u_2\right)\pmod3.
   }
   \tag{E}
$$


   Thus the first possible nonzero factorial response has been reduced to an explicit **three-jet obstruction**, rather than an original-size matrix calculation.

This is a genuine cancellation for the complete core observable. It is **not yet a scalar-preservation theorem**: neither the residue on the right of (E) nor the exact valuation of $K_J$ has been evaluated uniformly on the original family. More importantly, the actual producer correction $3^6R$ remains to be treated with its full force and nonlinear elimination.

No computation is reported as executed. No previously accepted bounded calculation is proposed for repetition.

---

## 1. Scope, domain, and notation

Retain the original family and window:


$$
j>0,\qquad j\equiv81\pmod{243},\qquad
m=2^{2j-1},\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$




$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



Throughout this report, conclusions using the unit-normalized inverse apply only on the established controlled-growth normalized branch. On that branch, reuse


$$
r=\operatorname{cont}_3(J_m)
=\operatorname{cont}_3(J_{m-1}),
$$




$$
s=s_c=h-2-2r<h,
\qquad h-s=2+2r\ge2.
\tag{1.1}
$$



For the new mod-$3$ endpoint cancellation, I also use the more precise retained normalization stated in A1_turn3:


$$
\mathfrak a=a_m/3\equiv25\pmod{27}.
\tag{1.2}
$$


In particular $\overline{\mathfrak a}=1$. A bare assertion that $\mathfrak a$ is a unit would not suffice for this step.

To avoid the source’s collision between a matrix and a scalar both denoted $F_c$, denote the factorial perturbation matrix by $\mathcal F$:


$$
G_c=G_J+3^h\mathcal F,
\qquad
\mathcal F_{ab}=-\frac14\mathfrak f(Q_cy^{a+b}),
\quad 0\le a,b\le m.
\tag{1.3}
$$



The endpoint vector is always


$$
v=(1,-1,\ldots,(-1)^m)^T.
$$



---

## 2. The exact pure measure, without altering the finite cutoff

Set


$$
\eta=A+71,\qquad r_0=\frac{\eta}{3},\qquad
c=\frac{(-1)^A3^h}{2},
$$


so that


$$
Q_c(y)=(y+1)(y-1)^A(3y-\eta).
$$



On $\mathcal P_m$,


$$
G_J(P,Q)
=
3c\int_0^1
P(y)Q(y)(y-r_0)y^{-1/2}(1-y)^A\,dy.
\tag{2.1}
$$



The identification with the pole part is exact because


$$
\deg\bigl((y-1)^A(3y-\eta)PQ\bigr)
\le A+1+2m=2n-2.
$$


Thus every coefficient is inside the original pole cutoff


$$
0\le v\le 2n-2.
$$



There is no pole-tail remainder in (1.3). Conversely, the factorial perturbation in (1.3) is not omitted.

Since $r_0>1$, the modified real weight has constant sign on $(0,1)$; hence its Gram matrix is nonsingular. This supplies the algebraic existence of the endpoint kernel independently of any $3$-adic normalization.

---

## 3. Jacobi normalization, leading coefficients, and norms

For every $s\ge0$, retain the source’s integral-at-$3$ Jacobi polynomial


$$
J_s(y)=
\sum_{k=0}^s
\binom{s+A}{k}
\binom{s-\tfrac12}{s-k}
y^k(y-1)^{s-k}.
\tag{3.1}
$$



This is the shifted normalization


$$
J_s(y)=P_s^{(A,-1/2)}(2y-1).
$$



Its actual leading coefficient is


$$
\boxed{
\kappa_s=\binom{2s+A-\tfrac12}{s}.
}
\tag{3.2}
$$



Let


$$
H_s=\int_0^1J_s(y)^2y^{-1/2}(1-y)^A\,dy.
$$


The norm is


$$
\boxed{
H_s=
\frac{\Gamma(s+A+1)\Gamma(s+\tfrac12)}
{(2s+A+\tfrac12)\,s!\,\Gamma(s+A+\tfrac12)}.
}
\tag{3.3}
$$



These are the unmodified norms; neither a leading coefficient nor a norm unit has been suppressed.

Define the unmodified kernel


$$
\mathscr K_m(y,z)=\sum_{s=0}^m\frac{J_s(y)J_s(z)}{H_s}.
\tag{3.4}
$$


For every $Q\in\mathcal P_m$,


$$
\int_0^1\mathscr K_m(y,z)Q(y)y^{-1/2}(1-y)^A\,dy=Q(z).
\tag{3.5}
$$



Its Christoffel–Darboux form is


$$
\boxed{
\mathscr K_m(y,z)=
\frac{\kappa_m}{\kappa_{m+1}H_m}
\frac{J_{m+1}(y)J_m(z)-J_m(y)J_{m+1}(z)}
{y-z}.
}
\tag{3.6}
$$


The coincident-value case is obtained by differentiation, not by deleting the denominator.

### Actual Christoffel polynomials

Put


$$
\gamma_s=\frac{J_{s+1}(r_0)}{J_s(r_0)},
\qquad
C_s(y)=\frac{J_{s+1}(y)-\gamma_sJ_s(y)}{y-r_0}.
\tag{3.7}
$$


All $J_s(r_0)$ are nonzero: the Jacobi zeros lie in $(0,1)$, whereas $r_0>1$.

The polynomial $C_s$ has degree $s$, leading coefficient $\kappa_{s+1}$, and modified norm


$$
\boxed{
\widetilde H_s
=
\int_0^1C_s(y)^2(y-r_0)y^{-1/2}(1-y)^A\,dy
=
-\gamma_s\frac{\kappa_{s+1}}{\kappa_s}H_s.
}
\tag{3.8}
$$



Indeed,


$$
(y-r_0)C_s=J_{s+1}-\gamma_sJ_s,
$$


and orthogonality kills the $J_{s+1}$ term when paired with $C_s$. The coefficient of $J_s$ in $C_s$ is $\kappa_{s+1}/\kappa_s$, giving (3.8).

The expansion in the original integral Jacobi basis is


$$
\boxed{
C_s(y)=
\frac{\kappa_{s+1}H_s}{\kappa_sJ_s(r_0)}
\sum_{i=0}^s\frac{J_i(y)J_i(r_0)}{H_i}.
}
\tag{3.9}
$$



Thus the modification and its normalization are fully specified in that basis.

---

## 4. The full endpoint polynomial $P_J$

Define $P_J\in\mathcal P_m$ by


$$
G_J(P_J,Q)=Q(-1)\qquad(Q\in\mathcal P_m).
\tag{4.1}
$$


Its coefficient vector is $G_J^{-1}v$.

The Christoffel-basis formula is


$$
\boxed{
P_J(y)=\frac1{3c}
\sum_{s=0}^m\frac{C_s(y)C_s(-1)}{\widetilde H_s}.
}
\tag{4.2}
$$


Together with (3.8)–(3.9), this gives the full polynomial in the source’s Jacobi basis.

A more compact formula, requiring only the unmodified kernel and one additional Jacobi polynomial, is


$$
\boxed{
P_J(y)=
\frac{
\mathscr K_m(y,-1)
-\displaystyle\frac{\mathscr K_m(r_0,-1)}{J_{m+1}(r_0)}J_{m+1}(y)
}
{3c(y-r_0)}.
}
\tag{4.3}
$$



### Proof of the compact formula

The numerator vanishes at $y=r_0$, so (4.3) is a polynomial of degree at most $m$. For $Q\in\mathcal P_m$,


$$
\begin{aligned}
G_J(P_J,Q)
&=
\int_0^1
\left[
\mathscr K_m(y,-1)
-\frac{\mathscr K_m(r_0,-1)}{J_{m+1}(r_0)}J_{m+1}(y)
\right]Q(y)w(y)\,dy\\
&=Q(-1),
\end{aligned}
$$


where $w(y)=y^{-1/2}(1-y)^A$. The second term vanishes by orthogonality. ∎

In particular, the whole pure scalar is


$$
\boxed{
K_J=P_J(-1)
=
\frac{
\mathscr K_m(-1,-1)
-\displaystyle
\frac{\mathscr K_m(r_0,-1)J_{m+1}(-1)}
{J_{m+1}(r_0)}
}
{3c(-1-r_0)}.
}
\tag{4.4}
$$



The subtraction in this formula is essential.

Equations (4.2)–(4.4) are symbolic evaluations of the full endpoint polynomial and scalar. They are not claims that an $O(m)$ expansion is feasible at the original moving index.

---

## 5. A low-jet constraint specific to this endpoint kernel

Let


$$
C=3^sG_J^{-1}\in M_{m+1}(\mathbb Z_3),
\qquad
U(y)=3^sP_J(y),
$$


so that the coefficient vector of $U$ is $Cv$.

Use the retained inverse numerator


$$
G_J^{-1}(X,Y)
=
\frac{2\,3^{2-h}}{\mathfrak a N_m}\mathcal E(X,Y).
$$


Because $s=h-2-2r$,


$$
C(X,Y)=
\frac{2}{\mathfrak a N_m}\,3^{-2r}\mathcal E(X,Y).
\tag{5.1}
$$



Set


$$
\widetilde J=3^{-r}J_m\in\mathbb Z_3[y].
$$


The already established noncollision reduction, used here without reopening its proof, gives


$$
3^{-2r}\mathcal E(X,Y)
\equiv
(XY-\mathfrak a)\widetilde J(X)\widetilde J(Y)\pmod3.
\tag{5.2}
$$


Consequently, using $\mathfrak a\equiv1\pmod3$,


$$
\boxed{
U(y)\equiv
-\frac{2}{\mathfrak a N_m}
(y+1)\widetilde J(y)\widetilde J(-1)
\pmod3.
}
\tag{5.3}
$$



This remains valid if $\widetilde J(-1)\equiv0$, in which case the entire endpoint vector has additional divisibility.

### The first two Jacobi coefficients

The finite hypergeometric expansion of (3.1) gives


$$
J_m(y)=
(-1)^m\frac{(\tfrac12)_m}{m!}
\sum_{a=0}^m
\frac{(-m)_a(m+A+\tfrac12)_a}
{(\tfrac12)_a\,a!}\,y^a.
$$


Therefore


$$
\boxed{
[y]J_m=-m(6m-1)[1]J_m.
}
\tag{5.4}
$$


This is an exact rational identity and remains valid after division by $3^r$.

On the original family $m\equiv2\pmod3$, so


$$
[y]\widetilde J\equiv-[1]\widetilde J\pmod3.
\tag{5.5}
$$


Taking the coefficient of $y$ in (5.3) now yields:

### Proposition 5.1 — Endpoint first-jet cancellation



$$
\boxed{u_1:=[y]U\in3\mathbb Z_3.}
\tag{5.6}
$$



Also, substituting $y=-1$ in (5.3),


$$
\boxed{U(-1)\in3\mathbb Z_3.}
\tag{5.7}
$$


Thus


$$
v_3(K_J)\ge1-s.
$$


This is a lower bound, not an exact valuation.

The normalization $\overline{\mathfrak a}=1$ is indispensable in this derivation. With an arbitrary unit $\mathfrak a$, the linear coefficient in (5.3) need not vanish.

---

## 6. Complete factorial contraction: one digit proved and the next digit isolated

The perturbation of the endpoint scalar involves


$$
\mathfrak f(Q_cP_J^2),
$$


not merely $\mathfrak f(P_J^2)$. The factor $Q_c$ matters to the cancellation.

### 6.1 Exact finite localization of factorial contractions

For any integral polynomial $V=\sum v_ay^a$,


$$
\mathfrak f(V)=\sum_a(2a)!\,v_a.
$$


At precision $3^K$, all terms with


$$
v_3((2a)!)\ge K
$$


vanish.

Define


$$
N(K)=\min\{a\ge0:v_3((2a)!)\ge K\}.
$$


Then


$$
\boxed{
\mathfrak f(V)
\equiv
\sum_{a=0}^{N(K)-1}(2a)![y^a]V
\pmod{3^K}.
}
\tag{6.1}
$$



This is an exact truncation of the whole factorial functional. It does not truncate the original pole functional or change its finite cutoff.

For $K=2$, $N(2)=3$, since


$$
v_3(4!)=1,\qquad v_3(6!)=2.
$$


Hence only the coefficients of degrees $0,1,2$ are needed modulo $9$.

### 6.2 Actual low coefficients of $Q_c$

Here $v_3(A)=5$, $A$ is odd, and


$$
Q_c=(y+1)(y-1)^A(-71-A+3y).
$$


Modulo $9$, through degree $2$,


$$
(y-1)^A\equiv-1,
$$


because $A$ and $\binom A2$ are divisible by $9$. Therefore


$$
\boxed{
Q_c(y)\equiv71+68y-3y^2
\pmod{(9,y^3)}.
}
\tag{6.2}
$$



Write $U=u_0+u_1y+u_2y^2+\cdots$. Applying the complete factorial weights $1,2,24$ gives


$$
\begin{aligned}
\mathfrak f(Q_cU^2)
\equiv{}&
135u_0^2+3548u_0u_1
+3408u_0u_2+1704u_1^2
\pmod9\\
\equiv{}&
2u_0u_1+6u_0u_2+3u_1^2
\pmod9.
\end{aligned}
\tag{6.3}
$$



By Proposition 5.1, $u_1\in3\mathbb Z_3$. It follows that


$$
\boxed{\mathfrak f(Q_cU^2)\in3\mathbb Z_3}
\tag{6.4}
$$


and


$$
\boxed{
\frac{\mathfrak f(Q_cU^2)}3
\equiv
2u_0\left(\frac{u_1}{3}+u_2\right)\pmod3.
}
\tag{6.5}
$$



This calculation has retained the whole polynomial cancellation. In particular, the cancellation of the constant-square contribution is


$$
71+2\cdot68-24\cdot3=135\equiv0\pmod9;
$$


discarding any one of these terms would give the wrong result.

For comparison,


$$
\mathfrak f(U^2)
\equiv
u_0^2+4u_0u_1+3u_0u_2+6u_1^2
\pmod9.
\tag{6.6}
$$


There is no corresponding universal divisibility conclusion for $\mathfrak f(U^2)$ alone. The proved gain belongs to the **actual correlated contraction** $\mathfrak f(Q_cU^2)$.

---

## 7. Transfer to the complete core scalar, including every higher factorial correction

Let


$$
\epsilon=3^{h-s}.
$$


By (1.1), $\epsilon\in9\mathbb Z_3$. From (1.3),


$$
G_c^{-1}=3^{-s}(I+\epsilon C\mathcal F)^{-1}C.
\tag{7.1}
$$



The inverse is well defined over $\mathbb Z_3$ after normalization. Expanding with an exact remainder,


$$
\begin{aligned}
K_c-K_J
={}&-3^{-s}\epsilon\,u^T\mathcal Fu\\
&+3^{-s}\epsilon^2
u^T\mathcal F(I+\epsilon C\mathcal F)^{-1}C\mathcal Fu,
\end{aligned}
\tag{7.2}
$$


where $u$ is the coefficient vector of $U$.

Since


$$
u^T\mathcal Fu=-\frac14\mathfrak f(Q_cU^2),
$$


the first term is


$$
\frac{3^{h-2s}}4\mathfrak f(Q_cU^2).
\tag{7.3}
$$



Every factor in the second pairing is integral, so its valuation is at least


$$
2h-3s.
\tag{7.4}
$$


But


$$
2h-3s\ge h-2s+2,
$$


because $h-s\ge2$.

Combining (6.4), (6.5), and (7.2) proves:

### Theorem 7.1 — Complete factorial response through its first possible nonzero digit

On the stated normalized branch,


$$
\boxed{
K_c-K_J\in3^{h-2s+1}\mathbb Z_3,
}
\tag{7.5}
$$


and


$$
\boxed{
\frac{K_c-K_J}{3^{h-2s+1}}
\equiv
2u_0\left(\frac{u_1}{3}+u_2\right)\pmod3.
}
\tag{7.6}
$$



In particular:

- If
  

$$
u_0\left(\frac{u_1}{3}+u_2\right)\not\equiv0\pmod3,
$$


  then
  

$$
\boxed{v_3(K_c-K_J)=h-2s+1.}
$$



- If that residue is zero, then
  

$$
\boxed{v_3(K_c-K_J)\ge h-2s+2.}
$$



These alternatives are conditional on the displayed three-jet residue, whose original-family value has not been evaluated here.

### What this theorem improves

The bare integral-matrix estimate gives only


$$
v_3(K_c-K_J)\ge h-2s.
$$


Theorem 7.1 proves one additional digit from the actual coefficient structure and identifies the next obstruction exactly.

The theorem concerns the **whole scalar** $K_c-K_J$, not just its first variation: all higher factorial corrections are included in (7.2) and are proved too deep to affect (7.6).

For the normalized whole Schur scalar


$$
\Sigma_c=e_c^T(-S_c/3^{26})^{-1}e_c-3^{26}d_c
=-3^{26}K_c,
$$


the corresponding factorial-only response has valuation at least


$$
26+h-2s+1.
$$


The LOW/HIGH contribution is already included through the full endpoint polynomial; no residual-only replacement has occurred.

---

## 8. The precise obstruction that remains

The extra digit does not, by itself, overcome the squared inverse loss.

Indeed,


$$
h-2s+1=5+4r-h,
$$


which need not be positive and need not exceed the valuation of the pure scalar.

Scalar preservation would follow from


$$
v_3(K_c-K_J)>v_3(K_J).
$$


What is proved is


$$
v_3(K_c-K_J)\ge h-2s+1,
\qquad
v_3(K_J)\ge1-s.
$$


Two lower bounds do not establish the required strict comparison. Cancellation in the complete subtraction (4.4) may make $K_J$ substantially deeper.

Accordingly, the next pure/core target is now explicit:

> **Endpoint three-jet and scalar lemma.**  
> On the actual normalized original family, determine
> 

$$
> u_0\bmod3,\qquad u_1\bmod9,\qquad u_2\bmod3,
>
$$


> together with a sufficiently sharp valuation of the complete scalar (4.4). In particular, decide whether
> 

$$
> u_0\left(\frac{u_1}{3}+u_2\right)
>
$$


> vanishes modulo $3$, and prove a comparison with $v_3(K_J)$.

The Jacobi formulas above specify these quantities algebraically, but do not yet furnish a bounded-cost original-family evaluation. The nonlocal endpoint quantities $J_s(-1)$, $J_s(r_0)$, and their correlated Christoffel cancellation remain in that evaluation. Merely observing that only three output coefficients are wanted does not make those inputs inexpensive.

This is the precise computational and mathematical obstruction—not a need to construct an enormous Schur matrix.

---

## 9. The actual producer correction remains a separate complete obligation

Theorem 7.1 advances the exact comparison $G_J\to G_c$. It does not evaluate $G_c\to G_{\rm act}$.

For that second comparison, retain


$$
Q_{\rm act}=Q_c+3^6R,
\qquad
R=R_{25}+3^{25}\Delta_{25},
$$


with


$$
R_{25}=(y+1)x^{A-54}B_{25}(x).
$$



The actual derivative remains


$$
\Sigma_\theta'
=
3^{32}\mathcal M(RP_\theta^2),
$$


where $P_\theta$ is the **full** endpoint solution.

Likewise retain both corrected representatives and the exact nonlinear Schur identity


$$
\widehat Z^{\,\rm act}
=
\widehat Z^{\,c}-3^6WE_{\rm act}^{-1}T_R,
$$




$$
S_{\rm act}-S_c
=
3^6K_Z-3^{12}T_R^TE_{\rm act}^{-1}T_R.
$$



Nothing proved here eliminates:

- the full $\Delta_H$ layers;
- the unpaired pole-cutoff terms;
- the $3^{25}\Delta_{25}$ remainder;
- either corrected factor;
- the LOW/HIGH endpoint component;
- the nonlinear Schur term.

The accepted finite HIGH masks, reflection borrow, and carry channels remain available at their stated precision. I make no claim here of a new bounded state space for their complete weighted observable.

---

## 10. Finite boundaries, forcing, terminal return, and primitive normalization

The finite columns remain exactly


$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m),
\qquad
d=\frac{3D}{2}-1,\quad \nu=\frac D2-1.
$$



The full force remains the sum of both leading extractions, every permitted lower pole, the factorial force, and the LOW subtraction in A1_turn2, equation (5.1). No omission at precision $25$ has been promoted to an exact omission or to a higher-precision assertion.

The terminal equations remain


$$
\mu_{i+\nu}^{\langle26\rangle}
+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}^{\langle26\rangle}
=b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2,
$$




$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\bigl(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\bigr).
$$


Here $s_{\rm ret}$ denotes the source’s return scalar, not the inverse loss $s$. There is still no moment beyond $D-4$, and $\omega_{\nu-1}$ remains.

The actual determinant pair is


$$
D_0=\det T,\qquad T=-S_{\rm act}/3^{26},
$$




$$
D_1=e_{\rm act}^T\operatorname{adj}(T)e_{\rm act}
-3^{26}d_{\rm act}\det T.
$$


No part of the subtraction has been replaced by a leading term.

When both members are nonzero,


$$
v_3(q)=
\max\left\{
0,\,
h-26+2v_3((n-1)!)
+v_3(D_1)-v_3(D_0)
\right\}.
$$



All row contents, the actual multiplier, and the actual least clearer remain to be restored before taking


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over **all primes**. For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and the same-index whole error remains


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
$$



The new factorial cancellation supplies no substitute for this primitive normalization or for nonvanishing and decay of the whole evaluated error.

---

## 11. Bounded arithmetic and proof-status ledger

### Bounded arithmetic actually needed

No original-size computation is needed to verify the new cancellation theorem. Its finite arithmetic consists only of:

- the low coefficients of $Q_c$ modulo $9$;
- the factorial weights $0!=1$, $2!=2$, $4!=24$;
- the fact that $6!$ is divisible by $9$;
- the polynomial identity
  

$$
\mathfrak f(Q_cU^2)
  \equiv2u_0u_1+6u_0u_2+3u_1^2\pmod9.
$$



All of these have been derived explicitly above. An implementation check would therefore be optional, constant-size, and new—not a rerun of an accepted certificate.

Its expected verifiable output is the coefficient vector


$$
(0,2,6,3)\pmod9
$$


on the monomials


$$
(u_0^2,\ u_0u_1,\ u_0u_2,\ u_1^2),
$$


followed, after setting $u_1=3b$, by


$$
\mathfrak f(Q_cU^2)/3\equiv2u_0(b+u_2)\pmod3.
$$



This verifies the symbolic contraction identity only. It does **not** evaluate the original-family values of $u_0,b,u_2$.

For a future bounded evaluation of the actual three-jet residue, the necessary compressed inputs would be


$$
u_0\bmod3,\quad u_1\bmod9,\quad u_2\bmod3
$$


with a proved original-family derivation. No such inexpensive derivation is asserted here, and I do not request these quantities from an unevaluated enormous producer or Schur matrix.

### Status ledger

| Claim | Status |
|---|---|
| Full pure-Jacobi endpoint polynomial, with actual Christoffel modification | Proved |
| Actual Jacobi leading coefficients and norms retained | Explicitly supplied |
| Exact formula for the whole pure scalar, including subtraction | Proved |
| $U=3^sP_J$ integral on the normalized branch | Reused from the retained inverse formula |
| $u_1\equiv0\pmod3$ | Proved using $\mathfrak a\equiv1\pmod3$ at its established scope |
| $\mathfrak f(Q_cU^2)\in3\mathbb Z_3$ | Proved |
| Mod-$9$ contraction and three-jet obstruction | Proved |
| Complete factorial scalar response formula (7.6) | Proved, including higher corrections |
| Original-family value of the three-jet obstruction | Not evaluated |
| Exact valuation of the whole pure scalar | Unresolved |
| Full actual-producer directional response | Unresolved |
| Actual cofactor nonvanishing and relative valuation | Unresolved |
| All-prime primitive denominator and same-index nonzero error decay | Unresolved |

## Conclusion

The new result is a target-specific cancellation for the **complete factorial response of the full endpoint scalar**:


$$
\boxed{
K_c-K_J\in3^{h-2s+1}\mathbb Z_3,\qquad
\frac{K_c-K_J}{3^{h-2s+1}}
\equiv
2u_0\left(\frac{u_1}{3}+u_2\right)\pmod3.
}
$$



It improves the bare squared-inverse estimate by one digit and identifies the next obstruction exactly. The full endpoint polynomial needed for further work is now explicitly available with its actual Christoffel normalization.

The remaining local bottleneck is to evaluate the correlated endpoint jets and the whole pure scalar on the original family, then control the complete actual-producer response—not merely its factorial part or paired pole bulk. Beyond that remain the actual cofactor pair, final all-prime gcd, primitive denominator, and infinitely many same-index nonzero whole errors tending to zero.



$$
\boxed{\text{The irrationality of }e+\pi\text{ remains unresolved by this work.}}
$$


