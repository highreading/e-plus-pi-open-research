> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Seed-sensitive contact reduction with exact primitive payments

## Abstract

The rationality or irrationality of $e+\pi$ remains unresolved.

The universal rational tensor gauge is **closed**: its nonexistence follows from the supplied denominator and degree arguments together with the independent exact decision. No additional gauge search is proposed.

This report instead gives a sequence-specific endpoint reduction of the actual paid-contact correlation. The factorial affine term is represented exactly by a canonical companion of the actual reference recurrence. This representation preserves the transverse seed $\mathcal K_2=14$; it does not replace the transverse coordinate by a free variable or discard the factorial term.

For each actual contact, an additional **explicitly paid** content


$$
b_j=\gcd\!\left(\gcd(\pi_{j,1},\pi_{j,2}),\,|C|\right),
\qquad
\pi_j=\frac{\mathbf c_j}{\kappa_j}
      =\varepsilon_j\frac{(z\times W_j)^T}{h_j},
$$


leads to an integral seeded endpoint residual $\mathscr E_j$. The principal new result is the exact equality


$$
\boxed{
\gcd(|T_{\rm aff}|,D_j)_{>n+2}
=
\gcd(|\mathscr E_j|,D_j)_{>n+2}.
}
$$


It holds wherever the retained nonzero contact construction is defined. It covers both $p\nmid F$ and $p\mid F$, and requires **no assumption that $W_{j,3}$ is a unit**.

The previous $\widehat{\mathcal B}_j$-support bound can now be compared exactly with this residual. Its excess support comes from $W_{j,3}$; the new equality removes that potentially extraneous factor rather than merely assuming it is harmless. A further explicit exclusion rule removes primes dividing a specified seed-dependent endpoint projection.

These are proved arithmetic reductions, not a subfactorial gcd theorem. No supplied almost-$S$-unit theorem has yet been shown applicable. The remaining tasks are a quantitative bound for the new **evaluated** residuals, moving-prime alignment acquisition, and a nonzero whole-error estimate using the actual all-prime primitive denominator at the same infinite original indices.

---

## 1. Domain, hypotheses, and closed work

The approximation domain remains exactly


$$
\boxed{
n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2.
}
$$


Thus every original $n$ is odd. Write


$$
m=n+1,\qquad N=n+2,\qquad L=2^{(n+1)/2}.
$$



Consecutive auxiliary indices used below serve only to define or prove identities for the supplied recurrences. They do not enlarge the approximation domain.

The following work is reused, not repeated:

* the finite producer and its physical boundaries;
* the actual contact definitions;
* the complete transverse recurrence with seed $14$;
* the universal rational-gauge nonexistence result;
* the previously accepted producer calculation and the old recurrence checks.

The universal-gauge receipt reports ranks $22$ and $23$, without the seed equation. The accompanying full machine certificate is not reproduced in the present packet, but the supplied Laurent obstruction also gives a mathematical contradiction under the proved universal denominator and degree bounds. Nothing below depends on reopening that decision.

### Nonvanishing hypotheses

The contact calculations use the retained construction at indices where


$$
\det T\ne0,\qquad F\ne0,
$$


and, for a contact denominator under discussion,


$$
\widehat R_j\ne0.
$$


The sources invoke retained nonvanishing results for the producer and the globally valid $F$-chart. Their underlying proofs are not reproduced here. The new local theorem below is proved explicitly whenever these stated original objects are defined and nonzero; it does not silently supply an additional nonvanishing theorem for every reference contact.

---

## 2. The actual seeded objects

Set


$$
q(z)=1-z+\frac{z^2}{2},\qquad
a_k(n)=k![z^k]e^zq(z)^n.
$$


At a fixed parameter $n$, retain


$$
X=ma_n,\qquad Y=mn\,a_{n-1},\qquad Z=2a_{n+1}-ma_n,
$$


and


$$
P=nX+Y,\qquad Q=nZ+2X-Y,
$$




$$
F=2m\bigl(Y-2X-(n-1)Z\bigr)=2m(Z-Q),\qquad C=mZ.
$$



The actual moment state $z_n=(P_n,Q_n,F_n)^T$ satisfies


$$
z_{n+1}=\mathsf U_nz_n,\qquad z_2=(0,10,-66)^T,
$$


where


$$
\mathsf U_n=
\begin{pmatrix}
0&mN&N/2\\
N&-(n^2+3n+1)&-\dfrac{nN}{2m}\\
-N(2n+3)&N(n^2+3n+1)&\dfrac{N(n^2-2)}{2m}
\end{pmatrix}.
$$



The actual reference satisfies


$$
N\tau_{n+2}=(2n+3)\tau_{n+1}+m\tau_n,
\qquad (\tau_2,\tau_3)=(2,4).
$$


Equivalently,


$$
y_{n+1}=\mathsf R_ny_n,\qquad
\mathsf R_n=
\begin{pmatrix}
0&1\\ m/N&(2n+3)/N
\end{pmatrix}.
$$



With the tensor ordering in the sources,


$$
\mathcal K_{n+1}=-m^2\mathcal K_n+\gamma_n\mathbf Y_n,
\qquad \boxed{\mathcal K_2=14},
$$


where


$$
\gamma_n=
\left(
0,\frac N2,-\frac{m^2}{2},\frac{m^2+1}{2},
-\frac m4,\frac{n^2+3n+3}{4m}
\right).
$$



At original indices,


$$
\widehat h=L\tau_n,\qquad
\widehat\ell=L\tau_{n+1},\qquad
M=Q\widehat h-P\widehat\ell,
$$




$$
\mathscr K_n^\circ=L\mathcal K_n,
$$


and


$$
\Theta=CM+F\bigl(2L(n!)^2-\mathscr K_n^\circ\bigr),
$$




$$
g_{\rm aff}=\gcd(|F|,|CM|),\qquad
T_{\rm aff}=\frac{\Theta}{g_{\rm aff}}.
$$



In particular, the full factorial term $2L(n!)^2$ remains present.

---

## 3. An exact companion representation of the factorial affine term

This section supplies a sequence-specific endpoint identity. It is not a rational tensor gauge.

### 3.1 The actual response endpoints

Reuse the proved generating-function identity


$$
B_n(z)
=-e^zq(z)^n+
\frac{q(z)^n}{(1-z)^{n+1}}
\bigl(e^zS_n(z)-E_n\bigr),
$$


where


$$
S_n(z)=n!\sum_{k=0}^n\frac{(1-z)^k}{k!},
\qquad
E_n=n!\sum_{k=0}^n\frac1{k!},
$$


and


$$
B_n(z)=\sum_{k\ge0}b_k(n)\frac{z^k}{k!}.
$$



For exact evaluation without a Green kernel, put


$$
u_0(n)=0,\qquad
u_{k+1}(n)=(n+k+1)u_k(n)+1.
$$


Then


$$
b_k(n)
=
\sum_{j=0}^{\min(2n,k)}
\binom{k}{j}\bigl(j![z^j]q(z)^n\bigr)u_{k-j}(n)
-a_k(n).
$$


All these $b_k(n)$ are integers. Indeed, $u_k(n)$ is integral, and
$j![z^j]q(z)^n$ is integral: each denominator $2^s$ in a term using $s$ quadratic factors is absorbed by the corresponding falling factorial.

Define


$$
\xi_n=\frac m2 b_n(n),\qquad
\zeta_n=b_{n+1}(n)-\frac m2b_n(n).
$$


At original odd indices, both are integers. The supplied transverse identity becomes


$$
\boxed{
\mathcal K_n=\tau_n\zeta_n-\tau_{n+1}\xi_n.
}
\tag{3.1}
$$



This retains the actual response seed. At $n=2$,


$$
b_2(2)=0,\qquad b_3(2)=7,
$$


so (3.1) gives $\mathcal K_2=14$.

### 3.2 A canonical reference companion

Extend the reference backward to


$$
\tau_0=\tau_1=1,
$$


which is forced by the given values $\tau_2=2,\tau_3=4$.

Define the companion $\sigma_n$ by the **same** recurrence


$$
(n+2)\sigma_{n+2}
=(2n+3)\sigma_{n+1}+(n+1)\sigma_n,
$$


with


$$
\sigma_0=0,\qquad \sigma_1=1.
$$



Its Casoratian is evaluated exactly.

### Lemma 3.1
For every $n\ge0$,


$$
\boxed{
\tau_n\sigma_{n+1}-\tau_{n+1}\sigma_n
=\frac{(-1)^n}{n+1}.
}
\tag{3.2}
$$



#### Proof
The determinant of the reference transfer at index $n$ is


$$
-\frac{n+1}{n+2}.
$$


Thus the Casoratian is multiplied by this factor at each step. Its value at $n=0$ is $1$, proving (3.2). ∎

The companion is also explicitly described by


$$
\sum_{n\ge0}\tau_nz^n=\frac1{\sqrt{1-2z-z^2}},
$$




$$
\sum_{n\ge0}\sigma_nz^n
=
\frac1{\sqrt{1-2z-z^2}}
\int_0^z\frac{dt}{\sqrt{1-2t-t^2}}.
$$


Consequently,


$$
\sigma_n
=
\sum_{k=0}^{n-1}
\frac{\tau_k\tau_{n-1-k}}{k+1}.
$$


The proof below does not leave this convolution as an unevaluated gcd target; it uses the exact Casoratian (3.2).

For integer arithmetic, define


$$
s_n=n!\sigma_n.
$$


Then


$$
\boxed{
s_0=0,\quad s_1=1,\quad
s_{n+2}=(2n+3)s_{n+1}+(n+1)^2s_n.
}
\tag{3.3}
$$


Thus every $s_n$ is integral.

### 3.3 The seeded affine endpoint pair

Define


$$
\boxed{
U_n^\sharp=\xi_n+2m!s_n,\qquad
V_n^\sharp=\zeta_n+2n!s_{n+1}.
}
\tag{3.4}
$$


These are integers at original indices. Since


$$
2m!s_n=2m!n!\sigma_n,\qquad
2n!s_{n+1}=2m!n!\sigma_{n+1},
$$


equations (3.1)–(3.2) give


$$
\begin{aligned}
\tau_nV_n^\sharp-\tau_{n+1}U_n^\sharp
&=\mathcal K_n
 +2m!n!\frac{(-1)^n}{n+1}\\
&=\mathcal K_n+2(-1)^n(n!)^2.
\end{aligned}
$$


Therefore, at every original odd index,


$$
\boxed{
2(n!)^2-\mathcal K_n
=\tau_{n+1}U_n^\sharp-\tau_nV_n^\sharp.
}
\tag{3.5}
$$



This is the required exact incorporation of the factorial affine term.

As a seed check,


$$
s_2=3,\qquad s_3=19,
$$


so


$$
U_2^\sharp=36,\qquad V_2^\sharp=83,
$$


and


$$
\tau_2V_2^\sharp-\tau_3U_2^\sharp=22=14+8.
$$


Thus the affine determinant has seed $22$, or its negative has seed $-22$. The transverse seed $14$ has not disappeared.

Equation (3.5) is compatible with universal tensor nonsplitting because the companion $\sigma_n$ is not a rational row in the original six tensor coordinates.

---

## 4. Actual contacts and an additional paid planar content

The finite matrix is still


$$
T=
\begin{pmatrix}
c&b&a\\
d&c&b\\
e_*&d&c
\end{pmatrix},
$$


with


$$
a=c_{n-2},\quad b=c_{n-1},\quad c=c_n,\quad
d=c_{n+1},\quad e_*=c_{n+2},
\qquad c_k=[z^k]e^zq(z)^n.
$$



The actual raw rows are


$$
R_j=\ell_j\operatorname{adj}(T),\qquad
\ell_0=(-1,n,-nm),\quad \ell_3=(0,0,1).
$$


The actual primitive row $r_j$ is obtained by the least coordinate denominator and then the three-coordinate gcd, with the recorded sign convention.

Retain


$$
V=
\begin{pmatrix}
2N&0&0\\
N&N&0\\
m&2n+3&1
\end{pmatrix},
\qquad
\mathbf c_j=r_jV.
$$



The supplied actual directions are


$$
W_3=
\begin{pmatrix}
X\\ Z\\ Y-X-(2n+1)Z
\end{pmatrix},
$$


and


$$
W_0=
\begin{pmatrix}
mZ-(n^2+1)X-(n-1)Y\\
mY+(1-n)X-m^2Z\\
2m\bigl(mX+(n^2+n+1)Z-NY\bigr)
\end{pmatrix}.
$$


They satisfy


$$
\mathbf c_jz=0,\qquad \mathbf c_jW_j=0.
$$



Write


$$
A_j=z\times W_j,\qquad
h_j=\gcd(|A_{j,1}|,|A_{j,2}|,|A_{j,3}|),
$$




$$
\kappa_j=\gcd(|c_{j,1}|,|c_{j,2}|,|c_{j,3}|).
$$


The actual normalization is


$$
\mathbf c_j
=\varepsilon_j\kappa_j\frac{A_j^T}{h_j},
\qquad
\kappa_j\mid2N^2.
$$



Define the all-prime primitive contact


$$
\boxed{
\pi_j=\frac{\mathbf c_j}{\kappa_j}
=\varepsilon_j\frac{A_j^T}{h_j}.
}
\tag{4.1}
$$


This is not a substitute contact: it is the recorded actual contact with its recorded content explicitly paid.

For a fixed $j$, suppress the subscript temporarily and write


$$
d_c=\gcd(|\pi_1|,|\pi_2|),\qquad
\pi=(d_c A,d_c B,c_0),
\qquad \gcd(A,B)=1.
$$


Here $d_c>0$, because $F\ne0$ excludes $\pi_1=\pi_2=0$. Since $\pi$ is primitive,


$$
\gcd(d_c,c_0)=1.
$$



The contact equations imply


$$
d_c(AP+BQ)+c_0F=0,
$$




$$
d_c(AW_1+BW_2)+c_0W_3=0.
$$


Hence


$$
\boxed{
d_c\mid F,\qquad d_c\mid W_3.
}
\tag{4.2}
$$



Now make the additional explicit payment


$$
\boxed{
b_c=\gcd(d_c,|C|),\qquad f_0=\frac F{d_c},
\qquad \omega=\frac{W_3}{d_c}.
}
\tag{4.3}
$$



Define the integral seeded contact residual


$$
\boxed{
\mathscr E_j
=
\frac{\pi_{j,1}U_n^\sharp+
      \pi_{j,2}V_n^\sharp+
      \pi_{j,3}C}{b_{c,j}}.
}
\tag{4.4}
$$


Its integrality is immediate from $b_c\mid d_c$ and $b_c\mid C$. In terms of the original cross-product content,


$$
\boxed{
\mathscr E_j
=
\frac{\varepsilon_j}{h_jb_{c,j}}
(z\times W_j)\cdot(U_n^\sharp,V_n^\sharp,C).
}
\tag{4.5}
$$


Thus neither $h_j$ nor $\kappa_j$ has been silently dropped.

---

## 5. Exact contact-chart identities

Choose integers $s,t$ such that


$$
As+Bt=1.
$$


Define


$$
\mathcal R=A\widehat h+B\widehat\ell,
\qquad
\nu=s\widehat\ell-t\widehat h.
$$


Then


$$
\binom{\widehat h}{\widehat\ell}
=
\mathcal R\binom{s}{t}
+\nu\binom{-B}{A},
\tag{5.1}
$$


and the actual paid reference is


$$
\boxed{
\widehat R_j=\kappa_jd_c\mathcal R.
}
\tag{5.2}
$$



The construction depends on an integer Bézout choice, but $\mathscr E_j$ does not.

Put


$$
J=Qs-Pt.
$$


Using $AP+BQ=-c_0f_0$, equation (5.1) gives the exact identity


$$
\boxed{
M=J\mathcal R+c_0f_0\nu.
}
\tag{5.3}
$$



By (3.5),


$$
2L(n!)^2-\mathscr K_n^\circ
=\widehat\ell U_n^\sharp-\widehat hV_n^\sharp.
$$


Substituting (5.1) and then (5.3) into $\Theta$ yields


$$
\boxed{
\Theta=b_c\bigl(\mathcal R H+f_0\nu\mathscr E_j\bigr),
}
\tag{5.4}
$$


where the coefficient


$$
\boxed{
H=\frac{CJ+F(tU_n^\sharp-sV_n^\sharp)}{b_c}
}
\tag{5.5}
$$


is an integer.

For the previous contact residual


$$
\widehat{\mathcal B}_j
=
W_3\bigl(2L(n!)^2-\mathscr K_n^\circ\bigr)
-C(W_1\widehat\ell-W_2\widehat h),
$$


the same calculation gives


$$
\boxed{
\widehat{\mathcal B}_j
=
b_c\bigl(\mathcal R H_W+\omega\nu\mathscr E_j\bigr),
}
\tag{5.6}
$$


where


$$
\boxed{
H_W=
\frac{C(W_2s-W_1t)+W_3(tU_n^\sharp-sV_n^\sharp)}
     {b_c}
}
\tag{5.7}
$$


is integral because $b_c\mid C,W_3$.

These are evaluated, seed-sensitive endpoint identities. No transverse coordinate has been declared algebraically free.

---

## 6. Exact large-prime gcd reduction

Recall the actual paid denominator


$$
D_j=
\frac{|\widehat R_j|}
{\gcd(|\widehat R_j|,|F|)}.
$$



### Theorem 6.1 — Exact seeded primitive-contact reduction

At every original index satisfying the stated nonvanishing hypotheses,


$$
\boxed{
\gcd(|T_{\rm aff}|,D_j)_{>N}
=
\gcd(|\mathscr E_j|,D_j)_{>N},
\qquad j=0,3.
}
\tag{6.1}
$$



There is no restriction on whether $p\mid F$ or $p\mid W_{j,3}$.

### Proof

Fix $p>N$ with $p\mid D_j$. All valuations below are $p$-adic.

Since $\kappa_j\mid2N^2$, $\kappa_j$ is a unit. The reference pair is primitive over $\mathbb Z_p$: its transfer matrices and inverses are integral and invertible at $p>N$, and its seed $(2,4)$ is primitive at such a prime. Since $L$ is a power of $2$, $(\widehat h,\widehat\ell)$ is also primitive.

The change of coordinates (5.1) is unimodular. Therefore, if $p\mid\mathcal R$, then


$$
\nu\in\mathbb Z_p^\times.
\tag{6.2}
$$



Write


$$
a=v_p(d_c),\qquad w=v_p(f_0),\qquad
r=v_p(\mathcal R),\qquad k=v_p(b_c).
$$


Equation (5.2) gives


$$
v_p(D_j)=r-w>0.
\tag{6.3}
$$


In particular $r>w$, so (6.2) applies.

We first evaluate the **actual** affine payment:


$$
\boxed{
v_p(g_{\rm aff})=w+k.
}
\tag{6.4}
$$



If $a=0$, then $v_p(F)=w$, and (5.3), with $r>w$, gives
$v_p(M)\ge w$. Hence $v_p(g_{\rm aff})=w=w+k$.

If $a>0$, primitivity gives $v_p(c_0)=0$. In (5.3), the first term has valuation greater than $w$, whereas the second has valuation exactly $w$. Thus


$$
v_p(M)=w,
$$


and


$$
v_p(g_{\rm aff})
=\min(a+w,v_p(C)+w)
=w+\min(a,v_p(C))
=w+k.
$$


This proves (6.4).

Divide (5.4) by the actual $g_{\rm aff}$:


$$
T_{\rm aff}
=
\frac{b_cf_0}{g_{\rm aff}}
\left(
\frac{\mathcal R}{f_0}H+\nu\mathscr E_j
\right).
\tag{6.5}
$$


By (6.4), the prefactor is a $p$-adic unit. By (6.3),


$$
v_p(\mathcal R/f_0)=v_p(D_j).
$$


Consequently,


$$
T_{\rm aff}
\equiv
\frac{b_cf_0}{g_{\rm aff}}\nu\mathscr E_j
\pmod{p^{v_p(D_j)}},
$$


with a unit coefficient multiplying $\mathscr E_j$. Therefore


$$
\min(v_p(T_{\rm aff}),v_p(D_j))
=
\min(v_p(\mathscr E_j),v_p(D_j)).
$$


Taking the product over $p>N$ proves (6.1). ∎

### Why the content $b_c$ matters

Without dividing by $b_c$, the valuation comparison would retain an avoidable loss. The proof shows exactly why this division is legitimate:

* $b_c$ divides both endpoint coefficients in (5.4);
* $v_p(g_{\rm aff})=v_p(f_0b_c)$ at every prime contributing to $D_j$;
* the resulting coefficient in (6.5) is a unit.

Thus the improvement is a paid primitive reduction, not an illicit cancellation.

---

## 7. What happens to the old $\widehat{\mathcal B}_j$ bound

At a prime $p>N$ dividing $D_j$, equation (5.6) gives


$$
\frac{\widehat{\mathcal B}_j}{b_c}
\equiv\omega\nu\mathscr E_j
\pmod{p^{v_p(D_j)}}.
\tag{7.1}
$$


More directly,


$$
\boxed{
\frac F{g_{\rm aff}}\widehat{\mathcal B}_j
\equiv
\frac{b_cf_0}{g_{\rm aff}}\,
W_{j,3}\nu\mathscr E_j
\pmod{p^{v_p(D_j)}}.
}
\tag{7.2}
$$


The displayed coefficient outside $W_{j,3}\mathscr E_j$ is a unit.

Let


$$
\mathfrak S_j=\gcd(|T_{\rm aff}|,D_j)_{>N},
$$


and denote the previous upper bound by


$$
\mathfrak U_j
=
\gcd\!\left(
D_j,
\left|\frac F{g_{\rm aff}}\widehat{\mathcal B}_j\right|
\right)_{>N}.
$$


For $d=v_p(D_j)$ and $e=v_p(\mathscr E_j)$,


$$
v_p(\mathfrak S_j)=\min(d,e),
$$


whereas


$$
v_p(\mathfrak U_j)=\min(d,e+v_p(W_{j,3})).
\tag{7.3}
$$



In particular,


$$
\boxed{
\mathfrak S_j\mid\mathfrak U_j,\qquad
\frac{\mathfrak U_j}{\mathfrak S_j}
\mid\gcd(D_j,|W_{j,3}|)_{>N}.
}
\tag{7.4}
$$



This identifies the precise obstruction in the old residual when $p\mid W_{j,3}$: its vanishing can be caused by the contact-direction coordinate rather than by seeded affine resonance. The new residual removes that ambiguity.

If $W_{j,3}=0$ at an index, (6.1) remains valid. Formula (7.4) then uses $\gcd(D_j,0)=D_j$.

No uniform asymptotic saving is asserted from (7.4). The saving is an exact, inspectable arithmetic factor; proving that it is large on an infinite original subsequence is a separate question.

---

## 8. A seed-sensitive modular exclusion rule

Expand (4.4) using (3.4). Define


$$
\boxed{
Z_j^{\rm seed}
=
\frac{d_c}{b_c}(A\xi_n+B\zeta_n)
+c_0\frac C{b_c}.
}
\tag{8.1}
$$


Then


$$
\boxed{
\mathscr E_j=Z_j^{\rm seed}+Q_j^{\rm fac},
}
\tag{8.2}
$$


where the full factorial contribution is


$$
\boxed{
Q_j^{\rm fac}
=
2m!n!\frac{d_c}{b_c}
\bigl(A\sigma_n+B\sigma_{n+1}\bigr).
}
\tag{8.3}
$$


Although the companion projection is rational, (3.3) shows that (8.3) is integral.

### Lemma 8.1 — The companion projection is a unit on the reference contact

If $p>N$ and $p\mid D_j$, then


$$
A\sigma_n+B\sigma_{n+1}\in\mathbb Z_p^\times.
\tag{8.4}
$$



#### Proof

The matrix with rows


$$
(\tau_n,\tau_{n+1}),\qquad
(\sigma_n,\sigma_{n+1})
$$


has unit determinant by (3.2). The vector $(A,B)^T$ is primitive over $\mathbb Z_p$. Its first image coordinate
$A\tau_n+B\tau_{n+1}=\mathcal R/L$ is divisible by $p$. Its second image coordinate must therefore be a unit. ∎

Consequently,


$$
v_p(Q_j^{\rm fac})=v_p(d_c/b_c)
\qquad(p>N,\ p\mid D_j).
\tag{8.5}
$$



There are two cases.

1. **If $v_p(d_c)>v_p(C)$, then resonance is impossible.**  
   Here $d_c/b_c$ is divisible by $p$, while $c_0C/b_c$ is a unit. Thus $Z_j^{\rm seed}$, and hence $\mathscr E_j$, is a unit.

2. **Otherwise $Q_j^{\rm fac}$ is a unit.**  
   For every $1\le e\le v_p(D_j)$,
   

$$
\boxed{
   p^e\mid T_{\rm aff}
   \iff
   \frac{Z_j^{\rm seed}}{Q_j^{\rm fac}}
   \equiv-1\pmod{p^e}.
   }
   \tag{8.6}
$$


   In particular, $p\mid Z_j^{\rm seed}$ excludes resonance.

This is an explicit seeded congruence, not a resultant in a free $\mathcal K_n$.

For a positive integer $D$, define the full $D$-supported saturation


$$
\operatorname{sat}_D(H)
=
\prod_{\substack{p\mid D\\p\mid H}}p^{v_p(D)},
$$


with $\operatorname{sat}_D(0)=D$. Then


$$
\boxed{
\mathfrak S_j
\mid
\left(
\frac{D_j}
{\operatorname{sat}_{D_j}((d_c/b_c)Z_j^{\rm seed})}
\right)_{>N}.
}
\tag{8.7}
$$



Equation (8.7) is a genuine quantitative deletion rule at each evaluated index. It is not yet known to provide a uniform subfactorial bound: its deletion factor could be $1$ along an infinite set.

---

## 9. Assessment of the supplied gcd literature

The literature gate identifies Zheng Xiao’s almost-unit polynomial gcd results and applications to suitable algebraic linear recurrences. At the supplied scope, an application would require, among other things:

1. a fixed number field and a fixed finite set $S$ of places;
2. a proved representation by polynomial evaluations at the required almost-$S$-unit points;
3. the requisite polynomial coprimality;
4. the theorem’s small outside-$S$ height condition;
5. control of the exceptional algebraic sets.

None of those requirements follows merely from the polynomial-coefficient recurrences above.

### 9.1 The factorial obstruction remains after the new identity

For a fixed finite set of rational primes $S$,


$$
\sum_{p\in S}v_p(n!)\log p=O_S(n),
$$


because $v_p(n!)\le n/(p-1)$. Hence


$$
\sum_{p\notin S}v_p(n!)\log p
=\log(n!)-O_S(n).
$$


Relative to $h(n!)=\log(n!)$, this has ratio tending to $1$, not $0$.

The new representation keeps the factorial term in (8.3). Dividing by it transfers large outside-$S$ contributions into denominators unless extensive cancellations are proved. No such cancellation theorem is available here.

### 9.2 The reference is not itself a constant-coefficient recurrence sequence

Its ordinary generating function


$$
(1-2z-z^2)^{-1/2}
$$


is not rational. Therefore $\tau_n$ is not a constant-coefficient linear recurrence sequence.

Nor does passage to $n=15^r$ or $105^r$ automatically create an applicable algebraic recurrence. For example, positivity and the reference recurrence already give exponential growth in $n$, hence growth faster than $C^r r^d$ after either geometric substitution.

These observations do not rule out every possible arithmetic normalization or representation. They do rule out a direct transfer of the cited theorem under the currently established hypotheses.

**Conclusion of the literature assessment:** no quantitative consequence of that theorem is invoked in this report.

---

## 10. What the new result does—and does not—do for the budget

The exact resonance quantity is now


$$
\boxed{
J_{\rm res}
=
\operatorname{lcm}_{j=0,3}
\gcd(D_j,|\mathscr E_j|)_{>N}.
}
\tag{10.1}
$$



The established saturation simplification remains


$$
\mathfrak S_0\mathfrak S_3\mid J_{\rm res}^2.
$$


Thus no separate height bound for all unselected contact collision is reintroduced.

The new result improves the arithmetic formulation in three specific ways:

* it is an equality, not only a support implication;
* it retains the actual $g_{\rm aff}$ and evaluates its valuation on every contributing contact prime;
* it removes the $W_{j,3}$-unit restriction, with an exact accounting of the old excess factor.

It does **not** prove


$$
\log J_{\rm res}=o(n\log n).
$$



### Concrete remaining contact lemma

A sufficient next lemma is:

> On an infinite subset of one original geometric family, prove
> 

$$
> \log\operatorname{lcm}_{j=0,3}
> \gcd(D_j,|\mathscr E_j|)_{>n+2}
> =o(n\log n),
>
$$


> where $\mathscr E_j$ is exactly (4.4), with the actual response endpoints, companion seeds, contact contents, and payment $b_{c,j}$.

A more targeted route is to bound the aggregate depth of the congruences (8.6), after applying the exclusions in (8.7). That is now a concrete seeded factorial-residue problem. Merely estimating the heights of its two summands gives only a factorial-scale upper bound and does not settle it.

---

## 11. Preservation of the finite producer and final arithmetic

The new contact reduction changes none of the following objects.

### 11.1 Complete source and physical return

The force remains


$$
q_j=[z^j]q(z)^n,
$$




$$
\alpha_0=\alpha_1=1,\qquad
\alpha_r=\alpha_{r-1}-\frac12\alpha_{r-2},
$$




$$
\eta_L=\sum_{r=0}^{L}\frac1{r!}
+\sum_{r=1}^{L}\frac{2\alpha_{r-1}}r,
\qquad
\mathcal W_L=L!\eta_L,
$$




$$
\boxed{
w_i=
\sum_{j=0}^{\min(2n,n+i)}
q_j(n+i)^{\underline j}\mathcal W_{2n+i-j},
\qquad 0\le i\le2.
}
$$


Its maximum force index is exactly $2n+2$. Both exponential and logarithmic terms remain.

The equivalent differential source is retained through


$$
K=2n+2,
$$


and the coefficient of $\mathfrak f_K$ in $b_{K+1}$ remains $1$. No finite inverse has been extended beyond its physical terminal.

With $\widehat w_i=w_i/(n+i)!$, the physical endpoint returns remain


$$
N_0=\det T+R_0\widehat w,\qquad
N_3=R_3\widehat w.
$$


The companion $\sigma_n$ in this report is an algebraic device for representing the factorial affine term. It does **not** replace the logarithmic force, the complete return, or either corrected boundary column.

### 11.2 Complete corrected columns and actual contents

Retain


$$
x=T^{-1}(n!t),\qquad y=T^{-1}\widehat w,
$$


where


$$
t=
\begin{pmatrix}
\tau_n\\
(\tau_n+\tau_{n+1})/2\\
\tau_{n+2}/2
\end{pmatrix},
\qquad
S=
\begin{pmatrix}
1&-n&nm\\
0&1&-2n\\
0&0&1
\end{pmatrix}.
$$


Writing $sx=Sx,\ sy=Sy$,


$$
u=(-sx_0,\ sx_0-sx_1,\ sx_1-sx_2,\ sx_2),
$$




$$
\boxed{
v=(1-sy_0,\ sy_0-sy_1,\ sy_1-sy_2,\ sy_2).
}
$$


The exterior $+1$ is retained.

The least simultaneous clearer is exactly


$$
D_8=
\operatorname{lcm}_{0\le j\le3}
\bigl(\operatorname{den}(u_j),\operatorname{den}(v_j)\bigr).
$$


The actual all-prime row contents and primitive entries are


$$
g_j^{(8)}=\gcd(|D_8u_j|,|D_8v_j|),
$$




$$
\widetilde u_j=\frac{D_8u_j}{g_j^{(8)}},
\qquad
\widetilde v_j=\frac{D_8v_j}{g_j^{(8)}}.
$$


These contents are distinct from $h_j,\kappa_j,d_c,b_c$. The accepted $3375$ contents are not recomputed or extrapolated.

For a nonzero endpoint $\widetilde u_j$, the actual primitive endpoint denominator is


$$
|\widetilde u_j|,
$$


not $D_j$, $b_c$, or a denominator attached only to the affine scalar.

### 11.3 Moving-prime acquisition

For an original block $t=bn$, $b\in\{15,105\}$, the inventory remains


$$
\boxed{
\mathcal I_t
=
\frac{\mathcal I_n c^{\min}_{n,t}}
{\mathcal M_{n,t}\mathcal L_{n,t}},
}
$$


where


$$
\mathcal M_{n,t}
=
\prod_{n+2<p\le t+2}
p^{\min(v_p(F_n),v_p(M_n))}
$$


and


$$
\mathcal L_{n,t}
=
\prod_{p>t+2}p^{(a_n-a_t)_+}.
$$



Neither medium-prime loss nor terminal-depth loss is removed by the contact theorem. The retained whole-telescope congruence continues to require its original hypotheses; its intermediate divisions and primitive exterior payment remain paid.

In particular, the aggregate acquisition


$$
\sum_{p>t+2}(a_t-a_n)_+\log p
$$


is still an independent open quantity.

### 11.4 The all-prime final gcd and actual primitive denominator

Let


$$
h_{\rm end}=\gcd(|\widetilde u_0|,|\widetilde u_3|),
\qquad
\widetilde u_0=h_{\rm end}A_{\rm wt},\quad
\widetilde u_3=h_{\rm end}B_{\rm wt}.
$$


For a reduced weight $\lambda=a/k_{\rm wt}$, retain


$$
J_{\rm wt}
=B_{\rm wt}\widetilde v_0-A_{\rm wt}\widetilde v_3,
$$




$$
T_{\rm wt}
=aJ_{\rm wt}+k_{\rm wt}A_{\rm wt}\widetilde v_3,
$$




$$
F_{\rm gcd}
=
\gcd(|A_{\rm wt}|,|a|)
\gcd(|B_{\rm wt}|,|a-k_{\rm wt}|),
$$




$$
G_{\rm wt}=\gcd(k_{\rm wt},|J_{\rm wt}|),
$$




$$
H_{\rm gcd}
=
\gcd\!\left(
h_{\rm end},
\frac{|T_{\rm wt}|}{F_{\rm gcd}G_{\rm wt}}
\right).
$$


Then


$$
\boxed{
q_\lambda=
\frac{k_{\rm wt}h_{\rm end}|A_{\rm wt}B_{\rm wt}|}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}},
}
$$




$$
\boxed{
p_\lambda=
\operatorname{sgn}(A_{\rm wt}B_{\rm wt})
\frac{T_{\rm wt}}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}}.
}
$$



Every gcd in these formulas is all-prime. The new contact residual does not replace $q_\lambda$.

The whole error is directly


$$
q_\lambda\left[
(e+\pi)-
\lambda\frac{\widetilde v_0}{\widetilde u_0}
-(1-\lambda)\frac{\widetilde v_3}{\widetilde u_3}
\right],
$$


or, in the retained error notation,


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}).
}
$$



An irrationality proof still requires


$$
0<|q_\lambda(e+\pi)-p_\lambda|\longrightarrow0
$$


at the **same infinite original indices** carrying the arithmetic estimates. This report does not prove that condition.

---

## 12. A bounded exact-arithmetic audit directed at the new gap

No computation was executed. The following optional audit is new, bounded, and does not repeat the universal gauge decision, the old $21$ comparisons, or the $3375$ producer.

### Input

Use the single original index


$$
\boxed{n=225=15^2.}
$$



Compute:

1. the five coefficients defining the actual $3\times3$ matrix $T$;
2. the actual primitive rows $r_0,r_3$, their contact coordinates, and the exact contents $h_j,\kappa_j,d_{c,j},b_{c,j}$;
3. $\tau_{225},\tau_{226}$;
4. $b_{225}(225),b_{226}(225)$ from the actual response coefficient formula;
5. $s_{225},s_{226}$ from (3.3);
6. $U^\sharp,V^\sharp,\mathscr E_j,Z_j^{\rm seed}$;
7. the actual $F,C,M,g_{\rm aff},T_{\rm aff},\widehat R_j,D_j$ and $\widehat{\mathcal B}_j$.

One terminal comparison with the supplied seeded transverse recurrence may verify


$$
\mathcal K_{225}
=\tau_{225}\zeta_{225}-\tau_{226}\xi_{225}.
$$


This is not a request to rerun the old list of recurrence comparisons.

### Expected verifiable output

The output should contain the exact integers or reduced rationals needed to verify:

* the actual row normalizations and all contents;
* $d_{c,j}\mid F,W_{j,3}$;
* integrality of $\mathscr E_j$;
* zero residuals in (3.5), (5.4), and (5.6);
* the exact equality
  

$$
\gcd(|T_{\rm aff}|,D_j)_{>227}
  =
  \gcd(|\mathscr E_j|,D_j)_{>227};
$$


* the diagnostic quotient
  

$$
\mathfrak U_j/\mathfrak S_j
$$


  and its divisibility by $\gcd(D_j,|W_{j,3}|)_{>227}$;
* the exact deletion factor in (8.7).

No factorization of an unrestricted large integer is needed. Compute ordinary gcds exactly, then remove the finitely many prime powers at $p\le227$. The saturation in (8.7) can likewise be computed by repeated gcd extraction.

A straightforward coefficient-convolution implementation uses $O(n^2)$ arithmetic operations, plus fixed-size rational matrix operations and gcds. At $n=225$, a conservative planning allowance is below $10^7$ integer/rational operations with a generous $10^5$-bit working-size allowance. These are resource estimates, not measured execution results.

If a special branch is absent at this index, the output must say so. A finite check cannot certify that branch’s behavior at infinitely many original indices.

---

## 13. Proof ledger and conclusion

| Statement | Status |
|---|---|
| Universal rational tensor gauge | **Closed: nonexistence reused** |
| Companion Casoratian (3.2) | **Proved** |
| Exact factorial-affine endpoint identity preserving seed $14$ | **Proved** |
| Paid divisibilities $d_c\mid F,W_{j,3}$ | **Proved** |
| Actual primitive seeded residual $\mathscr E_j$ | **Explicitly defined and integral** |
| Exact large-prime gcd equality (6.1) | **Proved under stated nonvanishing hypotheses** |
| Treatment of $p\nmid F$ and $p\mid W_{j,3}$ | **Included in the proof** |
| Exact excess factor in the previous $\widehat{\mathcal B}_j$ bound | **Proved** |
| Seed-sensitive modular exclusion (8.6)–(8.7) | **Proved** |
| Uniform subfactorial contact correlation | **Open** |
| Applicability of supplied almost-$S$-unit theorem | **Not established; no invocation made** |
| Moving-prime alignment acquisition | **Open** |
| Same-index nonzero primitive whole-error decay | **Open** |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

The principal new result is


$$
\boxed{
\gcd(|T_{\rm aff}|,D_j)_{>n+2}
=
\gcd\!\left(
D_j,
\left|
\frac{\pi_{j,1}U_n^\sharp+
      \pi_{j,2}V_n^\sharp+
      \pi_{j,3}C}{b_{c,j}}
\right|
\right)_{>n+2}.
}
$$



Its proof uses the actual seeded endpoints, an evaluated Casoratian, the actual primitive contact, and the exact affine payment. It neither assumes universal tensor splitting nor loses primes dividing the third contact direction.

The remaining contact bottleneck is now the aggregate depth of the explicit congruence


$$
Z_j^{\rm seed}/Q_j^{\rm fac}\equiv-1
$$


at the surviving large contact primes. A subfactorial bound for those congruences must still be proved on an infinite original subsequence. It must then be combined with moving-prime acquisition control and the nonzero whole error using the actual all-prime $q_\lambda$ at those same indices.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi\text{ is obtained.}}
$$


