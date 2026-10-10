> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1 turn9 — A complete endpoint quadratic form and a correlated lift; the strict comparison is not yet proved

## 1. Executive assessment

I retain the original family, the exact finite cutoff, and the normalized branch specified in the sources. In particular, I retain **turn8 formula (38), with its factor $2$**:


$$
\frac{K_c-K_J}{3^{h-2s+2g-2}}
\equiv 2L^2\zeta^2J(-1)^2\pmod3.
\tag{1.1}
$$



The main new result is an exact reduction of the **complete pure Christoffel scalar** to a binary quadratic form in a genuinely correlated endpoint pair. It includes the coincident-endpoint derivative and therefore includes the subtraction in the Christoffel formula. It does not replace that subtraction by one summand.

More precisely, put


$$
j_*=J(-1),\qquad z_*=Z(-1).
$$


The established polynomial congruence $Z(y)\equiv yJ(y)\pmod3$ gives the integral correlated lift


$$
\boxed{\xi_*=\frac{z_*+j_*}{3}\in\mathbb Z_3.}
\tag{1.2}
$$


I derive an explicit rational binary quadratic form $\mathcal Q$ such that


$$
\boxed{3^sK_J=L\,\mathcal Q(j_*,\xi_*).}
\tag{1.3}
$$


All coefficients of $\mathcal Q$ are given below in terms of the actual $m,a_m,b_m,\rho,\eta$. This converts a nonlocal endpoint subtraction into a **local coefficient calculation plus a correlated endpoint evaluation**.

There is also a stronger version of the factorial bound. If


$$
\tau=\min\{v_3(j_*),v_3(z_*)\},
$$


then the turn8 weighted-jet proof gives


$$
\boxed{
v_3(K_c-K_J)\ge h-2s+2g-2+2\tau.
}
\tag{1.4}
$$


The correlation (1.2), rather than separate endpoint estimates, can now be used on both sides of the comparison.

What is **not** decided in this report is whether the resulting quadratic form is anisotropic with a sufficiently small uniform valuation loss on the actual normalized original family. I give an explicit coefficient test that would settle that alternative without evaluating the enormous endpoint polynomial. If the quadratic form is split, a genuine original-family line-avoidance theorem remains necessary.

I also derive the exact mod-$3$ differential reduction


$$
\boxed{J(y)\equiv y^2F(y^3)\pmod3}
\tag{1.5}
$$


and its finite hypergeometric decimation relation. This does **not** decide $J(-1)\bmod3$: it leaves $F(-1)$. I do not present that residual evaluation as cheaply available from the original power.

Finally, I give explicit factorial-weighted pole-pair and complete-layer transfer inequalities. They retain all $\Delta_H$ layers and both cutoff boundaries. They identify precisely why the factorial norm alone does not yet control the actual-producer response.

Thus this turn advances the comparison structurally, but does not claim strict scalar preservation or irrationality.

---

## 2. Scope and normalization audit

The domain remains


$$
j>0,\qquad j\equiv81\pmod{243},\qquad
m=2^{2j-1},\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,\qquad
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\quad C_{16}=147968\,3^{15}.
$$



The present Jacobi conclusions use the cylinder


$$
m\equiv851\pmod{6561}
$$


and, where the inverse formula is used, the established controlled-growth normalized branch:


$$
r=\operatorname{cont}_3(J_m)=\operatorname{cont}_3(J_{m-1}),
\qquad s=h-2-2r,
$$




$$
h-s=2+2r\ge2,\qquad
\mathfrak a=a_m/3\equiv25\pmod{27},
\qquad N_m\in\mathbb Z_3^\times.
$$



Write


$$
J=3^{-r}J_m,\qquad D_-=3^{-r}J_{m-1},\qquad
Z=3^{-r}Z_{\rm source},
\qquad L=\frac2{\mathfrak a N_m}.
$$


Here $D_-$ is a polynomial, not the window parameter $D$.

The retained valuations are


$$
v_3(A)=5,\qquad v_3(a_m)=v_3(b_m)=1,\qquad v_3(\rho)=4.
$$


The accepted constant-gap proof gives


$$
g=v_3(J(0))\ge5.
$$



### Sign checks used below

The normalized Christoffel identity is


$$
(3y-\eta)Z(y)
=(y-b_m-a_m)J(y)-\rho D_-(y),
\qquad \eta=A+71.
\tag{2.1}
$$



The quotient-free endpoint identity is


$$
(y+1)U(y)
=L\left[
Z(y)\bigl(Z(-1)-\mathfrak aJ(-1)+yZ(-1)\bigr)
+\mathfrak aJ(y)Z(-1)
\right],
\tag{2.2}
$$


with $U=3^sP_J$.

Equivalently,


$$
U(y)=L\left[
Z(y)Z(-1)
+\mathfrak a
\frac{J(y)Z(-1)-Z(y)J(-1)}{y+1}
\right].
\tag{2.3}
$$



At $y=-1$, the quotient is evaluated by differentiation:


$$
\boxed{
3^sK_J
=L\left[
z_*^2+\mathfrak a\bigl(J'(-1)z_*-Z'(-1)j_*\bigr)
\right].
}
\tag{2.4}
$$


The order in this Wronskian-like expression matters. Reversing it changes the scalar.

Equation (2.4) is a reformulation of the **whole** reproducing scalar, not a new normalization of it.

---

## 3. What the finite hypergeometric relation says about $J(-1)\bmod3$

### 3.1 A rigorous mod-$3$ reduction

The shifted Jacobi differential equation is


$$
y(1-y)J''+
\left(\frac12-\left(A+\frac32\right)y\right)J'
+m\left(m+A+\frac12\right)J=0.
\tag{3.1}
$$


Division by $3^r$ does not alter this equation.

On the cylinder, $m\equiv2\pmod3$ and $A\equiv0\pmod3$. Therefore


$$
y(1-y)\overline J''+2\overline J'+2\overline J=0
\qquad\text{in }\mathbb F_3[y].
\tag{3.2}
$$



Every polynomial has a unique decomposition


$$
\overline J(y)=F_0(y^3)+yF_1(y^3)+y^2F_2(y^3).
$$


In characteristic $3$,


$$
\overline J'=F_1(y^3)+2yF_2(y^3),\qquad
\overline J''=2F_2(y^3).
$$


Substitution into (3.2) gives


$$
2F_0(y^3)+2F_1(y^3)+2yF_1(y^3)=0.
$$


The residue classes of the exponents modulo $3$ are independent, so


$$
F_1=0,\qquad F_0=0.
$$


Consequently,


$$
\boxed{\overline J(y)=y^2F(y^3).}
\tag{3.3}
$$



Because $J$ is content-normalized, $\overline J\ne0$, hence $F\ne0$. Nevertheless,


$$
\boxed{J(-1)\equiv F(-1)\pmod3,}
\tag{3.4}
$$


and nonzero $F$ need not have nonzero value at $-1$.

The derivative is correlated:


$$
\boxed{J'(-1)\equiv J(-1)\pmod3.}
\tag{3.5}
$$



These are uniform polynomial identities. They do not require the ternary expansion of the original power.

### 3.2 Exact finite decimation

Let $c_i=[y^i]J$. The exact recurrence is


$$
\frac{c_{i+1}}{c_i}
=
\frac{(i-m)(6m-1+2i)}{(i+1)(2i+1)}.
\tag{3.6}
$$



For the surviving residue class, put $d_k=c_{3k+2}$. Where both indices are within the degree,


$$
\boxed{
\frac{d_{k+1}}{d_k}
=
\prod_{t=0}^{2}
\frac{(3k+2+t-m)(6m+3+6k+2t)}
{(3k+3+t)(6k+5+2t)}.
}
\tag{3.7}
$$


This is an exact rational identity; a modular implementation must remove the actual powers of $3$ before inverting denominators.

The endpoint residue is the finite contraction


$$
J(-1)\equiv
\sum_{0\le k\le\lfloor(m-2)/3\rfloor}(-1)^k d_k
\pmod3.
\tag{3.8}
$$



Equation (3.7) is a hypergeometric decimation relation, but (3.8) remains an original-length sum unless an additional compression theorem is proved. Singular numerator and denominator positions prevent treating (3.7) as an ordinary unit recurrence over $\mathbb F_3$.

### 3.3 Exact conclusion of this attempt

The reduction proves neither that a unit endpoint is impossible nor that it is forced.

In particular, the differential equation and the constant-gap normalization alone cannot decide the endpoint: modulo $3$, both $y^2$ and $y^2(1+y^3)$ satisfy (3.2), while their values at $-1$ differ. These are examples illustrating the insufficiency of the reduced equation, not assertions that both occur in the original family.

The unresolved input is the **normalized hypergeometric solution selected by the original $m$**, including valuation information lost in a bare mod-$3$ differential equation.

No $O(m)$ endpoint expansion is proposed.

---

## 4. Eliminating the adjacent polynomial without discarding the Christoffel modification

The next reduction avoids requiring an endpoint-unit decision first.

Set


$$
T_0=2m+A-\frac12=4m-\frac32,
\qquad
E_0=(m+A)\left(m-\frac12\right).
$$


The classical adjacent-degree differential identity, in the present shifted normalization, is


$$
\boxed{
E_0D_-(y)
=
T_0y(1-y)J'(y)
-m\bigl((m+A)-T_0y\bigr)J(y).
}
\tag{4.1}
$$



One sign check is available at $y=0$:


$$
\frac{D_-(0)}{J(0)}
=-\frac{m}{m-\frac12}
=-\frac{2m}{A},
$$


which is the source’s exact signed constant ratio.

Define rational functions


$$
d(y)=3y-\eta,
$$




$$
p(y)=y-b_m-a_m
+\frac{\rho m}{E_0}\bigl((m+A)-T_0y\bigr),
$$




$$
q(y)=-\frac{\rho T_0}{E_0}y(1-y),
$$


and


$$
f(y)=\frac{p(y)}{d(y)},\qquad
k(y)=\frac{q(y)}{d(y)}.
\tag{4.2}
$$



Substituting (4.1) into (2.1) gives the exact identity


$$
\boxed{Z(y)=f(y)J(y)+k(y)J'(y).}
\tag{4.3}
$$



There is no omitted Christoffel scalar in this formula.

### Denominator audit

At $y=-1$,


$$
d(-1)=-(A+74)
$$


is a $3$-adic unit. Moreover,


$$
v_3(E_0)=v_3((3m-1)A/2)=5,
\qquad v_3(T_0)=0.
$$


It follows that


$$
\boxed{v_3(k(-1))=-1.}
\tag{4.4}
$$



Thus (4.3) is not an integral change of endpoint coordinates. Its apparent division by $3$ is genuine, and the integral polynomial $Z$ reflects cancellation between its two terms. Treating $fJ$ and $kJ'$ separately would lose that cancellation.

The coordinate system in §6 below restores the known correlation explicitly.

---

## 5. An explicit quadratic form for the complete scalar

Rewrite (3.1) as


$$
J''=\alpha(y)J'+\beta(y)J,
$$


where


$$
\alpha(y)=
\frac{(A+\frac32)y-\frac12}{y(1-y)},
\qquad
\beta(y)=
-\frac{m(m+A+\frac12)}{y(1-y)}.
\tag{5.1}
$$


At $y=-1$,


$$
\boxed{
\alpha_*=\frac{A+2}{2},\qquad
\beta_*=\frac{m(6m-1)}4.
}
\tag{5.2}
$$



In this section all $f,k,f',k'$ are evaluated at $-1$. Put


$$
t_*=f+k'+k\alpha_*.
$$


Differentiating (4.3),


$$
Z'=(f'+k\beta_*)J+t_*J'
\qquad\text{at }-1.
$$


Since $k\ne0$,


$$
J'(-1)=\frac{z_*-fj_*}{k}.
$$


Consequently,


$$
J'(-1)z_*-Z'(-1)j_*
=
\frac{z_*^2}{k}
-\frac{f+t_*}{k}j_*z_*
+\left(\frac{t_*f}{k}-f'-k\beta_*\right)j_*^2.
\tag{5.3}
$$



Define


$$
C_{02}=1+\frac{\mathfrak a}{k},
$$




$$
C_{11}=-\frac{\mathfrak a(f+t_*)}{k},
$$




$$
C_{20}=
\mathfrak a\left(\frac{t_*f}{k}-f'-k\beta_*\right).
\tag{5.4}
$$



Then the complete scalar satisfies


$$
\boxed{
3^sK_J
=
L\left(C_{20}j_*^2+C_{11}j_*z_*+C_{02}z_*^2\right).
}
\tag{5.5}
$$



This is the promised exact evaluation of the complete subtraction in a two-coordinate form.

In particular,


$$
v_3(C_{02})=0,
\tag{5.6}
$$


because $v_3(\mathfrak a/k)=1$. This coefficient supplies a useful normalization check.

---

## 6. The genuine correlated lift and a coefficient-only comparison route

The retained polynomial identity


$$
Z(y)\equiv yJ(y)\pmod3
$$


implies


$$
z_*=-j_*+3\xi_*,
\qquad \xi_*\in\mathbb Z_3.
$$


Substituting into (5.5) gives


$$
\boxed{
3^sK_J=L\,\mathcal Q(j_*,\xi_*),
}
\tag{6.1}
$$


where


$$
\mathcal Q(X,Y)=A_0X^2+B_0XY+C_0Y^2
\tag{6.2}
$$


and


$$
\boxed{
\begin{aligned}
A_0&=C_{20}-C_{11}+C_{02},\\
B_0&=3(C_{11}-2C_{02}),\\
C_0&=9C_{02}.
\end{aligned}}
\tag{6.3}
$$


In particular,


$$
\boxed{v_3(C_0)=2.}
\tag{6.4}
$$



This lift is valid whether $j_*$ is a unit or not. It is not an assumption that the endpoints vary independently.

### 6.1 Correlated strengthening of the factorial response

Let


$$
\tau=\min\{v_3(j_*),v_3(z_*)\}.
$$


Both endpoint factors on the right of (2.2), including


$$
z_*-\mathfrak a j_*,
$$


are divisible by $3^\tau$.

Repeating the turn8 weighted recurrence with this extra common factor gives


$$
v_3(u_i)+w_i\ge g-1+\tau,\qquad
w_i=v_3((2i)!).
\tag{6.5}
$$


The stronger degree-$\ge2$ bound also gains $\tau$. Therefore the complete factorial contraction and the higher resolvent remainder gain $2\tau$:


$$
\boxed{
v_3(K_c-K_J)\ge h-2s+2g-2+2\tau.
}
\tag{6.6}
$$


This uses the same integral normalized resolvent as turn8; no new inverse-stability hypothesis has been introduced.

Put


$$
e_*=\min\{v_3(j_*),v_3(\xi_*)\}.
$$


Since $z_*=-j_*+3\xi_*$,


$$
\tau\ge e_*.
\tag{6.7}
$$



### 6.2 A comparison criterion that does not assume the missing endpoint valuation

Suppose the explicit form (6.2) admits a **coefficient-proved** bound


$$
v_3(\mathcal Q(X,Y))
\le 2\min\{v_3(X),v_3(Y)\}+M
\tag{6.8}
$$


for every nonzero pair $(X,Y)\in\mathbb Q_3^2$.

Then


$$
v_3(K_J)\le -s+2e_*+M,
$$


whereas (6.6)–(6.7) give


$$
v_3(K_c-K_J)\ge h-2s+2g-2+2e_*.
$$


Thus strict preservation follows if


$$
\boxed{M<h-s+2g-2.}
\tag{6.9}
$$



Unlike an upper bound whose hypothesis is the desired valuation of $K_J$, (6.8) is a separate, finite-dimensional algebraic assertion about three explicit rational coefficients. It can potentially be proved without evaluating any original-family endpoint.

For example, if


$$
3^{-\lambda}\mathcal Q
$$


is integral and its reduction is an anisotropic binary quadratic form over $\mathbb F_3$, then


$$
v_3(\mathcal Q(X,Y))
=\lambda+2\min\{v_3(X),v_3(Y)\}.
$$


In that case $M=\lambda$.

More generally, a nonsquare discriminant over $\mathbb Q_3$ gives an anisotropic form and a finite bound of the type (6.8), obtainable by completing the square and keeping the exact coefficient valuations.

### 6.3 What happens if the form splits

If


$$
B_0^2-4A_0C_0
$$


is a square in $\mathbb Q_3$, the form can factor into two rational linear forms. There is then no universal bound (6.8): primitive pairs can approach an isotropic line arbitrarily closely.

That would identify the genuine remaining endpoint obligation:


$$
\text{bound the original pair }(j_*,\xi_*)\text{ away from those two lines.}
$$


Such a theorem would have to use the original hypergeometric solution, not merely its content or its low jet.

### Status

The coefficients (6.3) are explicit, but their decisive valuation/discriminant test has **not** been evaluated here. Accordingly, (6.9) is not announced as a finished comparison.

The supplied packet gives the normalizer valuations and congruences, but does not display exact formulas or sufficiently detailed certified residues for all of $a_m,b_m,\rho$ needed to finish that coefficient test. I do not assign them unstated values.

---

## 7. Transfer of factorial weights to the complete pole response

The factorial norm is well adapted to $\mathfrak f$. Its transfer to the pole functional requires an additional, explicitly measurable loss.

For a finite polynomial $P=\sum p_i y^i$, define


$$
\mu_w(P)=\min_i\{v_3(p_i)+w_i\},
\qquad w_i=v_3((2i)!).
\tag{7.1}
$$



For a finite bilinear kernel $M_{ij}$,


$$
\mathcal B(P,Q)=\sum_{i,j}p_iq_jM_{ij},
$$


one always has


$$
\boxed{
v_3(\mathcal B(P,Q))
\ge
\mu_w(P)+\mu_w(Q)
+\min_{i,j}\{v_3(M_{ij})-w_i-w_j\}.
}
\tag{7.2}
$$


The index sets in this minimum are the actual finite supports.

For factorial kernels, the factorial divisibility gives a favorable final minimum. For pole kernels, that is not automatic.

### 7.1 Explicit pole-pair factorial weights

Retain


$$
B_{\rm cut}=2n-2,\qquad
w^{\rm pole}_r=\frac{3^h}{2r+1}.
$$


For a paired index,


$$
w^{\rm pole}_{r+H}-w^{\rm pole}_r
=
-\frac{2\,3^hH}{(2r+1)(2r+2H+1)}.
$$


Its exact valuation is


$$
h+(h-1)-v_3(2r+1)-v_3(2r+2H+1).
\tag{7.3}
$$



If a term of a coefficient product has index


$$
r=i+j+k
$$


and multiplier coefficient $b_k$, its explicit weighted defect is


$$
\boxed{
\begin{aligned}
\delta_{\rm pair}(i,j,k)
={}&v_3(b_k)+h+(h-1)\\
&-v_3(2r+1)-v_3(2r+2H+1)-w_i-w_j.
\end{aligned}}
\tag{7.4}
$$


This is the pole-pair counterpart of the factorial-weight inequality. The condition $r+H\le B_{\rm cut}$ is part of its definition.

When $a=v_3(2r+1)<h-1$, the pole-pair contribution has depth $h+(h-1)-2a$, as in turn6. Equation (7.4) records the additional losses needed when that depth is paired with factorial-weighted coefficients.

### 7.2 Every $\Delta_H$ layer

For


$$
\Delta_H(y)=\sum_{\ell=1}^{H-1}
(-1)^{H-\ell}\binom H\ell y^\ell,
$$


the exact coefficient valuation is


$$
v_3\binom H\ell=(h-1)-v_3(\ell).
$$


Thus the term with final index $i+j+k+\ell\le B_{\rm cut}$ has weighted defect


$$
\boxed{
\begin{aligned}
\delta_\Delta(i,j,k,\ell)
={}&v_3(b_k)+h+(h-1)-v_3(\ell)\\
&-v_3(2(i+j+k+\ell)+1)-w_i-w_j.
\end{aligned}}
\tag{7.5}
$$


There is no omission of shallow layers with large $v_3(\ell)$.

### 7.3 Unpaired and factorial pieces

For an unpaired term at an allowed endpoint $r$, the defect is


$$
\boxed{
\delta_{\rm unpaired}(i,j,k)
=v_3(b_k)+h-v_3(2r+1)-w_i-w_j,
}
\tag{7.6}
$$


with its actual sign and cutoff indicator retained.

The factorial term is treated with its complete multiplier. If that multiplier has coefficient $t_k$, the defect is


$$
\boxed{
\delta_{\rm fac}(i,j,k)
=h+v_3(t_k)+w_{i+j+k}-w_i-w_j.
}
\tag{7.7}
$$


The factor $1/4$ has no $3$-adic loss.

These formulas give a complete finite weighted lower-bound interface for the decomposition in turn6, equation (8.5).

---

## 8. Why this does not yet control the full actual producer

The original saturated residual identity remains


$$
R_{25}\phi_i\phi_j=(y+1)x^HV_{ij}.
$$


For this part, equations (7.4)–(7.7) apply term by term to the exact decomposition


$$
\begin{aligned}
\mathcal M((y+1)x^HV)
={}&-\frac{3^h}{4}\mathfrak f((y+1)x^HV)\\
&+\sum_rV_r\left(
\mathbf1_{r+H\le B_{\rm cut}}w^{\rm pole}_{r+H}
-\mathbf1_{r\le B_{\rm cut}}w^{\rm pole}_r
\right)\\
&+\sum_{v=0}^{B_{\rm cut}}w^{\rm pole}_v[y^v](\Delta_HV).
\end{aligned}
\tag{8.1}
$$



But three substantive difficulties remain.

### 8.1 Factorial weights do not bound ordinary pole evaluation

A monomial $y^N$ has weighted valuation $w_N$, while an allowed pole weight has valuation only


$$
h-v_3(2N+1).
$$


Thus a large factorial weight is not itself a large pole valuation. The subtraction $w_i+w_j$ in (7.4)–(7.6) is real, not an artifact that can be dropped.

Integral coefficients permit sharpening


$$
v_3(p_i)\ge\max\{0,\mu_w(P)-w_i\},
$$


but this still supplies no universal large-index pole cancellation.

The target needs correlated coefficient cancellation across the actual finite pole sum.

### 8.2 The full endpoint solution has exterior components

The derivative is


$$
\Sigma_\theta'=3^{32}\mathcal M(RP_\theta^2),
$$


with the full $P_\theta$, not just the saturated residual component. Writing it as residual plus eliminated component produces residual–residual, two cross terms, and eliminated–eliminated terms. Only the first automatically has the displayed $x^H$ factor.

The other terms must use the original divided-difference pole functional


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{v=0}^{B_{\rm cut}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1}.
\tag{8.2}
$$


This formula retains the exterior endpoint subtraction.

### 8.3 Nonlinear elimination remains

Both corrected columns remain:


$$
\widehat Z^{\,\rm act}
=\widehat Z^{\,c}-3^6WE_{\rm act}^{-1}T_R,
$$


and


$$
S_{\rm act}-S_c
=3^6K_Z-3^{12}T_R^TE_{\rm act}^{-1}T_R.
\tag{8.3}
$$


Also,


$$
R=R_{25}+3^{25}\Delta_{25}
$$


is exact; the final remainder has not been deleted.

The weighted inequalities above control a bilinear functional once its complete finite kernel is supplied. They do not establish invariance of a weighted module under $E_{\rm act}^{-1}$, nor under the full directional solve.

### Concrete producer follow-on lemma

A useful next theorem would establish a finite weighted module containing:

1. the full core endpoint column;
2. its actual producer force, including the exterior cross terms and $\Delta_{25}$;
3. the complete $\Delta_H$ layer response;
4. the nonlinear correction $E_{\rm act}^{-1}T_R$;

and prove an operator bound for the complete directional response on that module.

The exact defects (7.4)–(7.7) specify what that theorem must overcome. A paired-bulk bound alone does not meet it.

---

## 9. Finite boundaries, complete forcing, and primitive arithmetic

No finite space has been changed:


$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m),
\qquad d=\frac{3D}{2}-1,\quad \nu=\frac D2-1.
$$



The full force still contains both leading extractions, every permitted lower pole, factorial forcing, and LOW subtraction.

The terminal return remains


$$
\mu_{i+\nu}^{\langle26\rangle}
+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}^{\langle26\rangle}
=b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2,
$$




$$
J^T\varepsilon+\omega
=-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$


There is no added moment beyond $D-4$, and $\omega_{\nu-1}$ is retained.

All row contents, the actual multiplier, and the least actual clearer still precede


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
\qquad
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over **all primes**.

For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
\tag{9.1}
$$


Nothing in the local quadratic-form reduction evaluates this whole error or its actual primitive denominator.

---

## 10. New bounded arithmetic: exact inputs and expected output

No computation was executed, and no accepted producer, suffix, path, or jet computation is proposed for repetition.

The newly isolated bounded calculation is the **three-coefficient endpoint-form audit**.

### Inputs

Certified exact rational formulas, or certified sufficient $3$-adic residues with division-loss bounds, for


$$
m,\quad a_m,\quad b_m,\quad \rho,\quad \eta,\quad \mathfrak a
$$


on the actual normalized branch.

The required operations are the constant-size rational evaluations (4.2), their derivatives at $-1$, and formulas (5.4), (6.3). In particular, the known loss


$$
v_3(E_0)=5
$$


must be accounted for before modular division.

A certificate for the necessary normalizer residues is part of the input requirement; their inexpensive original-family production is not assumed.

### Expected verifiable output

1. The exact coefficients $A_0,B_0,C_0$, or certified residues at stated sufficient precision.
2. The normalization check
   

$$
v_3(C_0)=2.
$$


3. The valuation and unit square class of
   

$$
B_0^2-4A_0C_0.
$$


4. Either:
   - an explicit anisotropic valuation bound (6.8), with numerical $M$, followed by a verified comparison with $h-s+2g-2$; or
   - a split form, with its two endpoint lines explicitly identified; or
   - a statement that the available precision does not decide the square class.

For odd $3$, a nonzero discriminant’s square class is determined by the parity of its valuation and the square class of its unit part. A zero residue at insufficient precision is not a square-class decision.

This calculation has a bounded number of scalar operations. Its **certified input production and precision** remain separate obligations. No favorable output is predicted.

---

## 11. Proof-status ledger and conclusion

| Claim | Status |
|---|---|
| Constant-gap theorem $g\ge5$ | Reused, closed |
| Turn8 factor-$2$ residue formula | Retained |
| Mod-$3$ reduction $J=y^2F(y^3)$ | Proved here |
| Exact three-step hypergeometric decimation | Proved here |
| Decision of $J(-1)\bmod3$ on the original family | Unresolved |
| Correlated lift $(Z(-1)+J(-1))/3\in\mathbb Z_3$ | Proved from retained polynomial congruence |
| Exact quadratic form for the complete Christoffel scalar | Proved here |
| Correlated factorial bound with gain $2\tau$ | Proved from the retained weighted theorem |
| Coefficient-only anisotropy route to strict comparison | Rigorous criterion; coefficient test unevaluated |
| Strict core scalar preservation | Not proved |
| Explicit pole-pair, layer, boundary, and factorial weighted defects | Proved |
| Complete actual-producer weighted response | Unresolved |
| All-prime primitive denominator and same-index nonzero error decay | Unresolved |

### Final result

The new exact reduction is


$$
\boxed{
3^sK_J=L\,\mathcal Q\!\left(
J(-1),\frac{Z(-1)+J(-1)}3
\right),
}
$$


with the complete coefficients (5.4), (6.3), together with


$$
\boxed{
v_3(K_c-K_J)\ge
h-2s+2g-2+
2\min\{v_3(J(-1)),v_3(Z(-1))\}.
}
$$



The immediate bottleneck is now sharply divided:

- **If the explicit endpoint form is anisotropic with a small certified loss**, the endpoint valuation can cancel out of the comparison, and strict preservation can follow without an endpoint-unit decision.
- **If it splits**, the required new theorem is original-family avoidance of its actual isotropic lines by the correlated lifted endpoint pair.
- The full actual producer additionally requires cancellation beyond the factorial norm, across all finite pole layers, boundary terms, exterior components, and nonlinear elimination.

Neither alternative has been completed in this report.



$$
\boxed{\text{The irrationality of }e+\pi\text{ remains unresolved by this work.}}
$$


