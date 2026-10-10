> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent Research Report: Complete Schur Transfer, Finite Weighted Kernels, and Reduced Endpoint Arithmetic

## Executive assessment

The supplied work does **not** prove that $e+\pi$ is rational or irrational. The three newly assigned sources do, however, contain substantial valid reductions.

The principal audit conclusions are:

1. **A1turn13’s weighted inverse transfer and complete nonlinear Schur restoration are valid under the simultaneous hypotheses stated there**, together with the previously accepted finite support-return results. On the sufficiently large original fixed window,
   

$$
\boxed{S_{\rm act}\in 3^{26}M_\nu(\mathbb Z_3),\qquad
   S_{\rm act}-S_c\in3^{32}M_\nu(\mathbb Z_3).}
$$


   The upper-degree restriction $\deg f_i\le m-1$, not merely $\deg f_i\le m$, is essential to the extra transfer digit.

2. **A1’s first normalized coefficient formula is correct**, provided it is understood as a complete bilinear core calculation: both corrected-column representatives must be used, all surviving lower-pole carries must be retained, and the entire bracket must be evaluated before division.

3. **A2turn10’s actual finite inverse, adjoint telescope, squared-weight kernel, and finite coefficient gluing are correct.** Their combination does not establish the norm-relative congruence. The source contraction and exterior reconstruction remain genuine terms.

4. **A2’s aggregate bounds can be justified by an explicit construction**, but the construction needs more bookkeeping than the source supplies. In particular:
   - the finite coefficient problems can be kept within $32$ variables;
   - the coordinate-degree bound $256K+16$ is safe;
   - the task bound $100(29K+2)^4$ is safe if endpoint symbol matrices are multiplied outside the coefficient-extraction tasks.
   
   There is a minor source-numerator bookkeeping issue: directly combining $\mathscr H-\mathscr H(0)$ into one atom gives a safe numerator bound $145K+1$, rather than the displayed $145K$. Splitting off the constant-source subtraction repairs this without changing the advertised aggregate bounds.

5. **A3turn8’s Toeplitz normalization, endpoint transformation determinant, fixed-shift saddle asymptotic, reduced-denominator formula, and selected-prime law survive audit.** In particular,
   

$$
\boxed{(|AB|)_{\mathcal P}=5n}
$$


   concerns the factors obtained **after reducing both complete endpoint rows**. It is not a statement about the primitive numerator-denominator product of $u_0/u_3$.

6. A useful additional consequence of A1’s six-digit forgetting interval is available:

   > The complete normalized determinant/cofactor pair itself transfers from core to actual modulo $3^6$, without first proving an inverse-loss estimate.

   Thus nonzero core pair residues below depth $6$ would certify the corresponding actual valuations directly.

No executable tools were supplied or used. No reported PASS receipt, matrix, hash, or original-index computation was independently regenerated. The literature gate is treated as supplied background, not as evidence of an exhaustive novelty search.

---

# 1. Domains and accepted dependencies

The four active routes have different original domains and must remain separate.

### Ternary determinant route

Retain


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$


and


$$
A=n-2=H-D,\qquad H=3^{h-1},\qquad 0<D<H/972.
$$


For the fixed-window conclusions, additionally retain


$$
j\equiv81\pmod{243},\qquad
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$


The finite parameters are


$$
m=\frac{A+1}{2},\qquad d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
$$


With $x=y-1$, the original columns are


$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),\qquad
Y_b=y^b\quad(d\le b\le m).
$$


No additional HIGH column or residual moment is permitted.

### $29$-adic Gram route

Retain


$$
b=3^{249005515+574312172u},\qquad n=2001b,\qquad u\ge0.
$$


Contact coordinates are $0,\ldots,b-1$; recurrence rows are $1,\ldots,b-2$; reconstruction includes the separate coordinate $b$.

### Fixed-$d$ endpoint route

Retain


$$
n=15^r,\quad r\ge2,\quad \mathcal P=\{3,5\},
$$


or


$$
n=105^r,\quad r\ge2,\quad \mathcal P=\{3,5,7\}.
$$


Here $d=2$, $b=3$, contact indices are $0,1,2$, reconstructed coordinates are $0,1,2,3$, and the complete force ends at $2n+2$.

### Binary Gram route

Retain


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


The final contact block in $b=128D+81$ is shortened, and the reconstructed coordinate $b$ is separate.

The previously accepted saturation, finite support-return, contact factorization, source, endpoint transport, and whole-error results are reused at their stated scopes. The already closed p380, basic nilpotent-memory, ordinary finite endpoint-inverse, and characteristic-zero closure calculations are not reopened.

---

# Part I. A1turn13

## 2. The complete functional and its integral range

The functional is


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^r)=(2r)!.
$$


The actual and core producers are


$$
Q_{\rm act}=Q_c+3^6R,\qquad
Q_c=(y+1)x^A(\beta+3y),\qquad
\beta=-71-A.
$$



On the retained window,


$$
4n-3<3^{h+1}.
$$


Every denominator in the finite sum therefore has $3$-adic valuation at most $h$. Division of $F-F(-1)$ by the monic polynomial $y+1$ preserves integral coefficients. Hence


$$
\mathcal M(\mathbb Z_3[y])\subseteq\mathbb Z_3.
$$



There is exactly one possible valuation-zero pole: $2v+1=3^h=3H$, at


$$
r_*=\frac{3H-1}{2}.
$$


Consequently,


$$
\deg F\le r_*
\quad\Longrightarrow\quad
\mathcal M(F)\in3\mathbb Z_3,
\tag{2.1}
$$


because the endpoint-subtracted quotient has degree at most $r_*-1$.

This bounded-degree improvement is the extra digit used in the transfer. It is not an assertion that $\mathcal M/3$ is integral on arbitrary polynomial inputs.

---

## 3. The support input and its exact scope

The new support statement uses


$$
\Omega=\frac{H}{3^{P-1}},
\qquad
g_P=\frac{\Omega-4D-2P-3}{2},
$$


under


$$
P\ge7,\qquad h-1\ge P,\qquad
\Omega>4D+2P+3.
\tag{3.1}
$$



The accepted finite support-return machinery supplies core representatives


$$
\phi_i=x^D\psi_i,\qquad
\phi_i\equiv\widehat z_i^{\,c}\pmod{3^P},
\qquad
\phi_i\equiv z_i\pmod3,
$$


with the stated grid-strip support and


$$
\deg\phi_i\le m-g_P.
\tag{3.2}
$$



The precision bookkeeping behind the extension is consistent:

- From
  

$$
v_3\binom Hk=h-1-v_3(k),
$$


  the coefficients of $x^H\bmod3^P$ occur only at multiples of $\Omega$.

- The surviving lower poles of the normalized return occur on the corresponding half-grid.

- Every retained return increases the nongrid width by at most one, giving the width $\nu+P$.

- The inequality
  

$$
(\nu+P)+D<\frac{\Omega-1}{2}
$$


  follows from (3.1), so the complete LOW subtraction vanishes at the working modulus.

- The finite HIGH interval remains $d,\ldots,m$. The finite inverse does not introduce coefficients beyond $m$.

For the final core pairing, the remaining nongrid width is bounded by


$$
D+i+1+\nu+P\le2D-2+P,
$$


which is strictly smaller than the required half-grid gap.

The extra factor of $3$ is also justified: $G_c(z_i,\cdot)/3$ is integral on the original degree-$\le m$ space. Thus replacing $\widehat z_j^{\,c}$ by $\phi_j$ preserves the desired congruence after this division. It follows that


$$
\boxed{S_c\in3^{P+1}M_\nu(\mathbb Z_3).}
\tag{3.3}
$$



**Audit status.** This is accepted as a consequence of the previously accepted complete finite support-return theorem, with the displayed precision and degree hypotheses. It is not an unrestricted infinite-block support theorem. The underlying support-set definitions and return invariance remain dependencies; the present audit does not silently replace them by a new infinite inverse.

---

## 4. Weighted inverse transfer

### 4.1 Saturation input

Let


$$
R_p=(y+1)x^{A-\kappa_p}B_p(x),\qquad
R\equiv R_p\pmod{3^p},\qquad
\deg B_p\le\kappa_p,
$$


where $\kappa_p=\ell_{6+p}-2$ is obtained from the exact terminal factorial valuation condition, including


$$
2v_3((A+1)!)\ge6+p.
$$



Write


$$
a(y)=x^{-\kappa_p}B_p(x),\qquad c(y)=\beta+3y.
$$


The formal multiplier is


$$
\frac{c}{c+3^6a}
=
1+\sum_{r\ge1}\sum_{b\ge0}
(-1)^{r+b}\binom{r+b-1}{b}
\beta^{-r-b}3^{6r+b}a^ry^b.
\tag{4.1}
$$



To see this, first expand


$$
\frac{c}{c+3^6a}
=\sum_{r\ge0}(-3^6a)^rc^{-r},
$$


then expand $c^{-r}$ by the negative-binomial theorem.

Retain exactly the terms with


$$
6r+b<L.
$$


There are at most


$$
q_L=\left\lfloor\frac{L-1}{6}\right\rfloor
$$


powers of $a$.

### 4.2 Polynomiality and degree

For each retained term,


$$
\phi_i a^r
=x^{D-r\kappa_p}\psi_iB_p^r.
$$


It is a polynomial if


$$
q_L\kappa_p\le D.
\tag{4.2}
$$


Since $\deg B_p\le\kappa_p$, multiplication by $a^r$ does not increase degree. The largest possible $b$ is $L-7$, occurring at $r=1$. Therefore


$$
\deg f_i\le\deg\phi_i+L-7.
$$


Under


$$
g_P\ge L-6,
\tag{4.3}
$$


we obtain the decisive bound


$$
\boxed{\deg f_i\le m-1.}
\tag{4.4}
$$



The truncated formal identity gives


$$
\boxed{Q_pf_i-Q_c\phi_i\in3^L\mathbb Z_3[y],}
\tag{4.5}
$$


and


$$
f_i-\phi_i\in3^6\mathbb Z_3[y].
\tag{4.6}
$$



There is no Laurent-polynomial ambiguity in (4.5). The retained terms are polynomials by (4.2); both products are polynomials; coefficientwise divisibility in the completed Laurent ring therefore restricts to coefficientwise divisibility in the polynomial ring.

### 4.3 Simultaneous hypotheses

The conditions must be imposed together:


$$
\begin{gathered}
P,L\ge7,\quad p\ge1,\quad h-1\ge P,\\
\Omega>4D+2P+3,\\
\ell_{6+p}\text{ exists},\qquad
2v_3((A+1)!)\ge6+p,\\
\kappa_p=\ell_{6+p}-2,\qquad
\left\lfloor\frac{L-1}{6}\right\rfloor\kappa_p\le D,\\
\Omega\ge4D+2P+2L-9.
\end{gathered}
\tag{4.7}
$$


The last inequality is exactly the upper-degree budget (4.3). A lower-factor budget alone would not validate the transfer.

---

## 5. Complete Schur comparison

Write $G_Q(f,g)=\mathcal M(Qfg)$.

### 5.1 The extra transfer digit

Set


$$
E_i=\frac{Q_pf_i-Q_c\phi_i}{3^L}.
$$


Since $\deg Q_p,\deg Q_c\le A+2$ and $\deg f_i,\deg\phi_i\le m-1$,


$$
\deg E_i\le A+m+1.
$$


Using $\deg z_j\le d-1$,


$$
\deg(E_iz_j)\le A+m+d=r_*.
$$


Equation (2.1) gives


$$
\mathcal M(E_iz_j)\in3\mathbb Z_3.
$$


The corrected columns satisfy


$$
\widehat z_j^{\,p}\equiv z_j\pmod3.
$$


Integrality of $\mathcal M$ therefore gives


$$
\mathcal M(E_i\widehat z_j^{\,p})\in3\mathbb Z_3.
$$


Thus


$$
G_p(f_i,\widehat z_j^{\,p})
\equiv G_c(\phi_i,\widehat z_j^{\,p})
\pmod{3^{L+1}}.
\tag{5.1}
$$



### 5.2 Basis comparison

The original monic degree-ordered basis is integral and unimodular. In the integral basis $[W,\widehat Z^{\,c}]$, write


$$
\Phi=WB+\widehat Z^{\,c}C.
$$


Because $\Phi-\widehat Z^{\,c}\in3^P$,


$$
B\in3^PM,\qquad C\equiv I\pmod{3^P}.
\tag{5.2}
$$



Let


$$
T_p=\mathcal M(R_pW\widehat Z^{\,c}).
$$


The original degree argument, followed by
$\widehat Z^{\,c}\equiv Z\pmod3$, proves


$$
T_p\in3M.
$$


Exact elimination gives


$$
\widehat Z^{\,p}
=\widehat Z^{\,c}-3^6WE_p^{-1}T_p.
$$


The accepted inverse loss is one digit. Moreover,


$$
E_cE_p^{-1}
=I-3^6K_p(W,W)E_p^{-1}
$$


is integral. Hence


$$
G_c(W,\widehat Z^{\,p})
=-3^6E_cE_p^{-1}T_p\in3^7M.
\tag{5.3}
$$



If $A_f$ denotes the residual-coordinate matrix of $f_i$, then


$$
A_f\equiv C\pmod{3^6}.
$$


Pairing (5.1) and using (5.2)–(5.3) yields


$$
A_f^TS_p-C^TS_c
\in3^{\min(L+1,P+7)}M.
$$


Thus


$$
U=C^{-T}A_f^T\equiv I\pmod{3^6},
$$


and


$$
US_p-S_c\in3^{\min(L+1,P+7)}M.
\tag{5.4}
$$



### 5.3 Restoration of the complete producer

Define the whole remainder


$$
\Delta_p=\frac{R-R_p}{3^p},\qquad
Q_{\rm act}=Q_p+3^{p+6}\Delta_p.
$$


In the $Q_p$-corrected basis, the exact Schur identity is


$$
\boxed{
S_{\rm act}
=S_p+3^{p+6}\Phi_{\Delta_p}
-3^{2(p+6)}
T_{\Delta_p}^TE_{\rm act}^{-1}T_{\Delta_p}.
}
\tag{5.5}
$$


The inverse is the complete actual eliminated-block inverse. No nonlinear terms have been discarded.

Because $\deg\Delta_p\le A+1$,


$$
\deg(\Delta_pz_i g)\le(A+1)+(d-1)+m=r_*
$$


for every original degree-$\le m$ polynomial $g$. Therefore


$$
T_{\Delta_p}\in3M,\qquad
\Phi_{\Delta_p}\in3M.
$$


It follows that the linear term has depth $p+7$, while the quadratic return has depth at least


$$
2(p+6)+1.
$$


Consequently,


$$
S_{\rm act}-S_p\in3^{p+7}M.
\tag{5.6}
$$



Combining (5.4) and (5.6), put


$$
J=\min(L+1,P+7,p+7),\qquad
V=\min(P+1,L+1,p+7).
$$


Then


$$
US_{\rm act}-S_c\in3^JM,
$$


and $S_c\in3^{P+1}M$ first gives $S_{\rm act}\in3^VM$. Finally,


$$
S_{\rm act}-S_c
=(US_{\rm act}-S_c)-(U-I)S_{\rm act}.
$$


Since $V+6\ge J$,


$$
\boxed{
S_{\rm act}-S_c\in3^JM,\qquad
S_{\rm act}\in3^VM.
}
\tag{5.7}
$$



**Verdict:** the complete forgetting theorem is proved under (4.7) and the accepted finite support input.

---

## 6. The fixed-window specialization

On $j\equiv81\pmod{243}$,


$$
v_3(A)=5.
$$


Since $D=H-A$ is even and has $3$-adic valuation $5$ in the sufficiently large range,


$$
D\ge2\cdot3^5=486.
$$



For $p=25$, the terminal condition becomes


$$
5+v_3(k!)\ge31.
$$


Now


$$
v_3(53!)=17+5+1=23,\qquad
v_3(54!)=18+6+2=26.
$$


Hence


$$
\kappa_{25}=54.
$$



With


$$
P=25,\qquad L=31,\qquad p=25,
$$


the lower budget is


$$
q_{31}\kappa_{25}=5\cdot54=270<D.
$$


The upper budget is


$$
\Omega_{25}\ge4D+103.
$$


But


$$
\frac{\Omega_{25}}D
>
\frac{147968}{19683}>7.5,
$$


so


$$
\Omega_{25}-4D>3.5D\ge1701>103.
$$


The sufficiently-large factorial and $h$-conditions are retained. Therefore


$$
\boxed{
S_c\in3^{26}M,\qquad
S_{\rm act}-S_c\in3^{32}M.
}
\tag{6.1}
$$



The audited normalization


$$
S_{\rm act}=-3^{16}\Psi,\qquad
\mathsf H=\mathsf V^T\Psi\mathsf V
$$


then gives


$$
\Psi,\mathsf H\in3^{10}M.
$$


Thus every original moment satisfies


$$
\boxed{\mu_k\in3^{10}\mathbb Z_3,\qquad0\le k\le D-4.}
$$


The complete forcing vector has the same divisibility, and the recurrence remains on rows $0,\ldots,\nu-2$:


$$
\mu_{i+\nu}^{\langle26\rangle}
+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}^{\langle26\rangle}
=b_i^{\langle26\rangle}.
$$


No moment $\mu_{2\nu-1}$ is introduced.

The endpoint return remains


$$
J^T\varepsilon+\omega
=
-\varepsilon-s\bigl(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\bigr).
$$


The terminal component of $\omega$ is not removed.

The stated $P=26$ partial-window conclusions are also consistent:


$$
\kappa_{26}=57,\qquad q_{32}\kappa_{26}=285<D.
$$


For $P=27$,


$$
\frac{\Omega_{27}}D
<
\frac{295936}{177147}<4,
$$


so this separation certificate fails everywhere on the retained window. That is a limitation of the certificate, not a proof of a surviving coefficient.

---

## 7. The first normalized coefficient

Let


$$
T_{ij}=x^{H+D}(\beta+3y)\psi_i\psi_j.
$$


Then


$$
Q_c\phi_i\phi_j=(y+1)T_{ij}.
$$



A small clarification is needed in the source’s comparison with $S_c$. Orthogonality alone does not annihilate every cross term, because $\phi_i-\widehat z_i^{\,c}$ can have residual coordinates. Instead use


$$
\Phi=WB+\widehat Z^{\,c}C,
$$


which gives the exact identity


$$
G_c(\Phi,\Phi)=B^TE_cB+C^TS_cC.
$$


Since $B\in3^P$, $C-I\in3^P$, and $S_c\in3^{P+1}$,


$$
G_c(\Phi,\Phi)-S_c\in3^{2P}M.
\tag{7.1}
$$


For $P\ge7$, this is sufficient modulo $3^{P+2}$.

Grouping the finite poles according to $2v+1=c3^{h-\ell}$, one obtains


$$
\boxed{
\frac{(S_c)_{ij}}{3^{P+1}}
\equiv
\frac1{3^{P+1}}
\left[
-\frac{3^h}{4}\mathfrak f((y+1)T_{ij})
+
\sum_{\ell=0}^{P+1}
\ \sum_{\substack{c\ge1\ {\rm odd},\,3\nmid c\\
c3^{h-\ell}\le4n-3}}
3^\ell c^{-1}
[y^{(c3^{h-\ell}-1)/2}]T_{ij}
\right]\pmod3.
}
\tag{7.2}
$$


The hypotheses ensure that all exponents $h-\ell$ appearing here are nonnegative.

Terms with $\ell\ge P+2$ vanish at the required absolute modulus. The retained terms must be summed **before** division. The factorial contribution remains unless its exact valuation proves that it vanishes.

At $P=25$,


$$
\boxed{
-\frac{S_{\rm act}}{3^{26}}
\equiv-\frac{S_c}{3^{26}}\pmod3.
}
\tag{7.3}
$$



The finest-pole window calculation is also correct. Since $\beta\equiv1\pmod3$,


$$
T_{ij}\equiv(y^H-1)x^Dy^{i+j}\pmod3.
$$


This produces the two stated coefficient windows. Their geometric collision does not imply a nonzero complete entry: poles separated by $H$ may cancel modulo $3$, and lower-pole carries remain in (7.2).

---

## 8. New consequence: direct six-digit transfer of the complete pair

Define


$$
\Theta_{\rm act}=-S_{\rm act}/3^{26},\qquad
\Theta_c=-S_c/3^{26}.
$$


Equation (6.1) gives


$$
\Theta_{\rm act}\equiv\Theta_c\pmod{3^6}.
\tag{8.1}
$$


Retain the accepted endpoint comparisons


$$
e_{\rm act}-e_c\in3^6\mathbb Z_3^\nu,\qquad
d_{\rm act}-d_c\in3^4\mathbb Z_3.
$$



For $\star\in\{\mathrm{act},c\}$, put


$$
D_{0,\star}=\det\Theta_\star,
$$




$$
D_{1,\star}
=e_\star^T\operatorname{adj}(\Theta_\star)e_\star
-3^{26}d_\star\det\Theta_\star.
\tag{8.2}
$$



### Proposition 8.1 — Complete pair transfer

At the accepted endpoint-integrality scope,


$$
\boxed{
D_{0,\rm act}\equiv D_{0,c}\pmod{3^6},\qquad
D_{1,\rm act}\equiv D_{1,c}\pmod{3^6}.
}
\tag{8.3}
$$



#### Proof

Determinant and adjugate entries are polynomials with integer coefficients in the matrix entries. Hence (8.1) transfers both modulo $3^6$. The endpoint quadratic expression transfers modulo $3^6$ because $e_{\rm act}\equiv e_c\pmod{3^6}$. Finally,


$$
3^{26}(d_{\rm act}-d_c)\in3^{30}\mathbb Z_3,
$$


and the individual scaled endpoint scalars are integral at the accepted normalization. This proves (8.3). ∎

In particular, if


$$
v_3(D_{0,c})<6,\qquad v_3(D_{1,c})<6,
$$


then both actual members are nonzero and


$$
\boxed{
v_3(D_{1,\rm act})-v_3(D_{0,\rm act})
=
v_3(D_{1,c})-v_3(D_{0,c}).
}
\tag{8.4}
$$



This avoids a preliminary inverse comparison. It does not assert that either valuation is below $6$.

### A useful corank-one specialization

Suppose $\Theta_c\bmod3$ has corank one, with radical generated by $r$, and


$$
e_c^Tr\ne0\pmod3.
$$


For a symmetric corank-one matrix over $\mathbb F_3$,


$$
\operatorname{adj}(\Theta_c)=\gamma rr^T
$$


for some $\gamma\ne0$. Therefore


$$
e_c^T\operatorname{adj}(\Theta_c)e_c
=\gamma(e_c^Tr)^2\ne0.
$$


The scaled $d_c$-term vanishes modulo $3$, so


$$
D_{1,c}\in\mathbb Z_3^\times.
$$


If, in addition, the determinant becomes nonzero before precision $3^6$, then the actual relative valuation is certified.

This is a concrete rank-and-endpoint target, not an inference from common matrix depth.

### Radical reduction with the whole scalar retained

For subsequent layers, choose an integral congruence basis in which


$$
\Theta=
\begin{pmatrix}A&B\\B^T&C\end{pmatrix},
\qquad A\in\operatorname{GL}(\mathbb Z_3),
$$


and split $e=(e_C,e_R)$. Set


$$
K=C-B^TA^{-1}B,\qquad
e'=e_R-B^TA^{-1}e_C,\qquad
t'=3^{26}d-e_C^TA^{-1}e_C.
$$


Then


$$
D_0=\det A\,\det K,
$$




$$
\boxed{
D_1=\det A\left(e'^T\operatorname{adj}(K)e'-t'\det K\right).
}
\tag{8.5}
$$


Thus the complete subtraction survives radical/complement reduction. A calculation that retains only the endpoint adjugate term would not compute the actual pair.

---

# Part II. A2turn10

## 9. Actual finite inverse

Let


$$
\phi(z)=1-z+\frac{z^2}{2},\qquad
b_s(n)=[z^s]\phi(z)^{-n},\qquad c_s(n)=s!b_s(n).
$$


Multiplication of exponential generating polynomials by $\phi(z)^n$, truncated below degree $b$, gives the finite lower factor. Its inverse is therefore


$$
(H^{-1})_{jk}=b_{j-k}(n)\frac{j!}{k!}
=c_{j-k}(n)\binom jk.
\tag{9.1}
$$


This is an exact finite lower-triangular identity.

Since $b_s(n)\in\mathbb Z_{29}$,


$$
v_{29}(c_s(n))\ge v_{29}(s!)\ge\lfloor s/29\rfloor.
$$


Hence, modulo $29^K$, only


$$
0\le j-k\le29K-1
$$


can contribute.

The coefficient formula


$$
b_s(n)=(-1)^s
\sum_{v=0}^{\lfloor s/2\rfloor}
2^{-v}\binom{-n}{s-v}\binom{s-v}{v}
$$


is correct. Integer generalized binomial coefficients must be formed before any division-sensitive modular reduction.

The accepted finite factorization is


$$
A\equiv\mathsf P\,T(H+F\overline K E)T\pmod{29^K}.
$$


With


$$
\mathsf R=T^{-1},\quad
\mathsf P_-=\mathsf P^{-1},\quad
\mathsf S_{\rm end}=I+E\mathsf DF\overline K,
$$


the correct ordered inverse is


$$
\boxed{
A^{-1}
\equiv
\mathsf R\mathsf D\mathsf R\mathsf P_-
-
\mathsf R\mathsf DF\overline K
\mathsf S_{\rm end}^{-1}
E\mathsf D\mathsf R\mathsf P_-.
}
\tag{9.2}
$$



The order $E\mathsf DF\overline K$ is essential. Reversing the endpoint factors without changing boundary variables produces a different matrix problem.

Because $29\mid n$, positive symbol coefficients below degree $29$ vanish modulo $29$, while every crossing term of length at least $29$ contains a factorial factor divisible by $29$. Thus the endpoint update is divisible by $29$, and


$$
\mathsf S_{\rm end}^{-1}
\equiv
\sum_{q=0}^{K-1}(-E\mathsf DF\overline K)^q
\pmod{29^K}.
$$


This checks the specialization of the accepted finite inverse; it does not reopen the ordinary endpoint-inversion calculation.

The finite head-transform formula also retains its necessary endpoint:


$$
\begin{aligned}
(\mathsf R\mathsf P_-h)_j
={}&(-1)^j\sum_{i=0}^{L-1}(-1)^ih_i
\sum_{t=0}^i
\binom j{i-t}\binom{n+t-1}{t}\\
&\hspace{25mm}\times
\binom{n+b-1-j}{b-1-j-t}.
\end{aligned}
\tag{9.3}
$$


The final binomial is the finite hockey-stick sum through $b-1-j$; it cannot be replaced by an infinite convolution.

---

## 10. Adjoint telescope and exterior reconstruction

Write


$$
W_j=\binom{n+2}{j},\qquad
L=\mathcal R^T\mathcal R,\qquad
w=A^{-T}LA^{-1}f^0.
$$


The recurrence operator is


$$
(\mathcal Dh)_i
=h_{i+1}-\alpha_i h_i+\beta_i h_{i-1}+\gamma_i h_{i-2},
\qquad1\le i\le b-2,
$$


with $\gamma_1=0$.

Define only $\lambda_1,\ldots,\lambda_{b-2}$, by


$$
\lambda_{j-1}
=w_j+\alpha_j\lambda_j
-\beta_{j+1}\lambda_{j+1}
-\gamma_{j+2}\lambda_{j+2},
\qquad j=b-1,\ldots,2.
$$


Terms involving absent terminal $\lambda$-coordinates are omitted. This convention does not require evaluating an artificial forward recurrence row.

Set


$$
a_0=w_0-\beta_1\lambda_1-\gamma_2\lambda_2,
$$




$$
a_1=w_1+\alpha_1\lambda_1-\beta_2\lambda_2-\gamma_3\lambda_3.
$$


Collecting coefficients of each actual $h_j$ proves


$$
\boxed{
w^Th=a_0h_0+a_1h_1+
\sum_{\ell=1}^{b-2}\lambda_\ell(\mathcal Dh)_\ell.
}
\tag{10.1}
$$


There are exactly two initial charges and no extra terminal recurrence charge.

The accepted $58K+1$ memory law identifies this $\lambda_\ell$ with the finite-lag kernel $\Psi_\ell$ modulo $29^K$. That identification does not annihilate its source contraction.

The reconstruction includes


$$
Y=\mathcal R\psi+W_be_b,
$$


and


$$
\mathcal R^T(W_be_b)=bW_b^2e_{b-1}.
$$


Therefore the exterior contribution is exactly


$$
\boxed{E_{\rm out}=bW_b^2(A^{-1}f^0)_{b-1}.}
\tag{10.2}
$$


It is not a completed-block substitute.

For


$$
A^{-1}h=\mathsf Bh-\mathsf Uc_h,
$$


the complete weighted contraction is


$$
\boxed{
\mathcal Q(h,k)
=J(h,k)-c_h^Tv_k-v_h^Tc_k+c_h^TG_{\rm end}c_k
\pmod{29^K}.
}
\tag{10.3}
$$


Every term follows by direct bilinear expansion.

The equal source impulses at phases $26,27$ yield


$$
\sum_{\ell=1}^{b-2}\mathcal H_\ell\lambda_\ell
\equiv
\sum_{q=0}^{B-1}\kappa_q
\bigl(w_{29q+27}-2w_{29q+28}\bigr)\pmod{29},
$$


where $b=29B+27$. The upper bound $q<B$ is exact because the last source row is $29B+25$. This confirms the obstruction: later block-end cancellation does not imply cancellation of the weighted interior output.

---

## 11. Exact squared-weight kernel and finite gluing

Let


$$
F(z)=\sum_{j\ge0}W_j^2z^j.
$$


The coefficient identity


$$
F(z)
=[u^{n+2}v^{n+2}]
\frac1{(1-u)(1-v)-zuv}
$$


follows by expanding the geometric series: its $z^j$-coefficient is


$$
\frac{(uv)^j}{(1-u)^{j+1}(1-v)^{j+1}},
$$


whose indicated coefficient is $\binom{n+2}{j}^2$.

For $z=xy$, the full tridiagonal kernel is


$$
F(z)+(1-x-y)F'(z)+zF''(z).
$$


Indeed:

- $F$ contributes $W_j^2$ to the diagonal;
- $F'+zF''$ contributes $(j+1)^2W_{j+1}^2$;
- $-(x+y)F'$ contributes the two off-diagonals.

Thus


$$
\boxed{
\mathscr K_L(x,y)
=[u^{n+2}v^{n+2}]
\left(
\frac1\Delta+
\frac{(1-x-y)uv}{\Delta^2}
+\frac{2xyu^2v^2}{\Delta^3}
\right),
}
$$


where $\Delta=(1-u)(1-v)-xyuv$.

Finite restriction to $0,\ldots,b-1$ retains


$$
L_{b-1,b-1}=W_{b-1}^2+b^2W_b^2.
$$


No identification with an unverified full Hahn measure is used.

The gluing identity is also exact:


$$
[x^{b-1}y^{b-1}]
\frac{x^iy^j}{1-xy}
=
\begin{cases}
1,&i=j<b,\\
0,&\text{otherwise}.
\end{cases}
$$


Applying one such factor at each contraction node enforces every finite matrix index before the infinite rational kernels are used.

The remaining kernels have the stated ordinary power-series interpretations:


$$
\mathscr K_{\mathsf R}(x,y)
=[u^{n-1}]\frac1{(1-xy)(1-u+y)},
$$




$$
\mathscr K_{\mathsf P_-}(x,y)=\frac1{1+x-xy},
$$




$$
\mathscr K_{\mathsf D}(x,y)
=\sum_{s=0}^{29K-1}c_s(n)\frac{x^s}{(1-xy)^{s+1}}.
$$


The finite-end column formula likewise retains its actual extraction index $b+u$.

**Verdict:** the algebraic kernels and finite gluing are accepted.

---

## 12. Separate audit of variables, degrees, and task counts

These claims require a construction, not merely the existence of rational coefficient representations.

### 12.1 Variable count

The main core source contraction has nine matrix factors:


$$
\mathsf P_-^T,\mathsf R^T,\mathsf D^T,\mathsf R^T,
L,\mathsf R,\mathsf D,\mathsf R,\mathsf P_-.
$$


It therefore uses:

- $20$ gluing variables;
- four parameter variables for the four $\mathsf R$-kernels;
- two for the squared-weight kernel;
- at most two for each source atom.

The total is $28$.

For endpoint terms, work first with


$$
\mathsf U_0=\mathsf R\mathsf DF,\qquad \mathsf U=\mathsf U_0\overline K.
$$


Compute weighted contractions involving $\mathsf U_0$, then multiply by $\overline K$ as a finite scalar matrix operation. Those paths are shorter than the nine-factor path. Each occurrence of an $F$-atom adds only its two extraction variables.

Thus


$$
\boxed{V\le32}
$$


is safe for every primitive coefficient problem. The endpoint inverse does not need to be expanded into coefficient words of increasing length.

### 12.2 Source numerator bookkeeping

For fixed $s$, put


$$
t=z(1+X),\qquad
R_s(t)=\frac{A_s(t)}{(1-t)^{s+1}},
\qquad \deg A_s\le s.
$$


Applying a differential operator of degree $d$ gives a denominator of order at most $s+d+1$ and numerator degree in $z$ at most $s+d$. Multiplication by $z^{d+1}$ gives degree at most


$$
s+2d+1.
$$


After grouping $0\le d\le58K$ at a common denominator, this is at most $145K$.

However,


$$
R_s(t)-R_s(0)
$$


can have numerator degree $s+1$. If that subtraction is combined into the same atom before this bookkeeping, the safe bound is $145K+1$.

There are two repairs:

1. use $145K+1$; or
2. retain the $\mathscr H(0)$ subtraction as a separate polynomial-source atom.

The second repair preserves the displayed $145K$ bound for the main rational atom. The subtraction atom has only degree $58K+1$ in $z$. Both preserve the exact zero initial particular coordinates.

### 12.3 Coordinate-degree bound

The divided-power kernel can be put over


$$
(1-xy)^{29K},
$$


with numerator coordinate degrees at most $29K-1$.

For a source atom, a safe denominator order is $87K$. Including its parameter-marker factor gives coordinate degrees bounded by $87K+1$; its numerator degree in the contact variable is bounded by $145K+1$. A gluing factor adds one to the relevant coordinate degree.

The other kernels have bounded coordinate degrees independent of $K$. Therefore


$$
\boxed{\deg_{x_j}P,\deg_{x_j}Q\le256K+16}
$$


is comfortably valid.

The parameter $n$ occurs in supplied scalar coefficients and actual extraction targets, not as a polynomial variable silently reduced to a residue class.

### 12.4 Task count

Let


$$
N=29K,\qquad m,t_0\le N-1.
$$


After expanding the finite sum inside each $F_r$, the total number of $F$-atoms is


$$
A_F=\sum_{r=0}^{m-1}(r+1)=\frac{m(m+1)}2\le\frac{N^2}{2}.
$$


Allowing the source-subtraction split, the number of source atoms is at most $2N$.

A sufficient task list consists of:

- the few $J(f^0,h)$ contractions;
- $\mathsf U_0^TL\mathsf Bh$ for the three head inputs and source atoms;
- $\mathsf U_0^TL\mathsf U_0$;
- terminal input contractions;
- any endpoint entries not already evaluated by small-index arithmetic;
- the exterior weight and terminal coordinate.

One explicit upper count is


$$
A_F^2
+A_F(2N+3+t_0+1)
+t_0(2N+3)
+2N+5.
$$


This is less than


$$
\boxed{100(N+2)^4.}
$$


Multiplication by $\overline K$, and the precision-sized endpoint solve, are finite scalar operations outside this count.

**Aggregate verdict.** The advertised variable, degree, and task bounds are justified by this construction, with the source-subtraction clarification. They were author estimates in the reviewed packet; they are not reported implemented counts.

The dense Cartier bounds remain valid construction upper bounds. They are neither practical feasibility results nor lower bounds against other algorithms.

---

## 13. What the A2 representation still does not prove

The exact target remains


$$
\boxed{
\mathcal C-29\rho_n\mathcal N
\equiv0\pmod{29^{v_{29}(\mathcal N)+2}}.
}
$$


The rational representation does not establish that coefficient identity.

The complete initial force remains


$$
r_i=
\sum_s a_s(n)(n+i)_{\underline s}
\left(T_{2n+i-s}+\frac{L_{2n+i-s}}{b!}\right),
\qquad i=0,1,
$$


where


$$
T_m=\frac1{b!}\sum_{q=b}^m(m)_{\underline q},
$$




$$
L_0=0,\qquad L_m=mL_{m-1}+2(m-1)!u_{m-1},
\qquad u_r=[z^r]\phi(z)^{-1}.
$$


The logarithmic part cannot be deleted without the accepted protection inequality, including the entire primitive-norm loss:


$$
N_{\log}\ge c+4+\nu.
$$



The independent $\rho_n$ must also be supplied from its original definition. Defining it from the computed ratio would make the proposed alignment test circular.

---

# Part III. A3turn8

## 14. Toeplitz normalization and complete endpoints

Let


$$
Q(z)=1-z+\frac{z^2}{2},\qquad
c_j=[z^j](e^zQ(z)^n),
$$


and


$$
a=c_{n-2},\quad b=c_{n-1},\quad c=c_n,\quad
d=c_{n+1},\quad e_*=c_{n+2}.
$$


Since


$$
C_{ij}=(n+i)^{\underline j}(n+i-j)!\,c_{n+i-j},
$$


we have


$$
C=\operatorname{diag}(n!,(n+1)!,(n+2)!)T_n,
$$


with


$$
T_n=
\begin{pmatrix}
c&b&a\\ d&c&b\\ e_*&d&c
\end{pmatrix}.
$$


The determinant and adjugate displayed in A3 are correct.

The first force, divided by the three row factorials, is


$$
n!\bigl(\tau_n\mathbf v_n+\tau_{n+1}\mathbf w_n\bigr).
$$


Thus, for


$$
R_j=\ell_j^T\operatorname{adj}(T_n),\quad
\alpha_j=R_j\mathbf v_n,\quad
\beta_j=R_j\mathbf w_n,\quad
\xi_j=\alpha_j\tau_n+\beta_j\tau_{n+1},
$$


the first endpoints are


$$
u_j=\frac{n!\xi_j}{\Delta_T},\qquad j=0,3.
$$



The complete force is


$$
w_i=
\sum_{j=0}^{\min(2n,n+i)}
q_j(n+i)^{\underline j}\mathcal W_{2n+i-j},
$$


where


$$
\mathcal W_L=L!\left(
\sum_{r=0}^L\frac1{r!}
+\sum_{r=1}^L\frac{2\alpha_{r-1}}r
\right).
$$


Thus both factorial/exponential and logarithmic contributions remain.

Writing $\widehat w_i=w_i/(n+i)!$, the complete endpoint numerators are


$$
N_0=\Delta_T+R_0\widehat w,\qquad
N_3=R_3\widehat w.
$$


Therefore


$$
\boxed{
\frac{v_0}{u_0}=\frac{N_0}{n!\xi_0},\qquad
\frac{v_3}{u_3}=\frac{N_3}{n!\xi_3}.
}
\tag{14.1}
$$


The $+\Delta_T$ is the exterior $+1$. It affects both the center and its row content.

The formulas determine the endpoint ratios exactly. They do not by themselves compute the least clearer of all four reconstructed rows; that requires the complete original reconstruction, including rows $1,2$.

---

## 15. Classical logarithmic normalization

The Legendre logarithmic companion is established classical material. The source-specific question is its normalization against the complete original force.

The recurrence for


$$
D_n=n![z^n]A_n^{\log}
$$


gives


$$
D_{n+2}
=(n+2)(2n+3)D_{n+1}
+(n+2)(n+1)^3D_n.
$$


Dividing by $((n+2)!)^2$ gives exactly the recurrence for $\rho_n$. The initial values $D_0=0,D_1=4$ imply


$$
D_n=4(n!)^2\rho_n.
$$


The accepted terminal relations then recover all three logarithmic contacts:


$$
\widehat w^{\log}
=4n!(\rho_n\mathbf v_n+\rho_{n+1}\mathbf w_n).
$$


Consequently,


$$
v_j^{\log}
=\frac{4n!}{\Delta_T}
(\alpha_j\rho_n+\beta_j\rho_{n+1}).
$$



Using


$$
\tau_n\rho_{n+1}-\tau_{n+1}\rho_n
=\frac{(-1)^n}{n+1},
$$


one obtains


$$
\boxed{
\frac{v_j^{\log}}{u_j}
=\frac{4\rho_n}{\tau_n}
+\frac{4(-1)^n\beta_j}{(n+1)\tau_n\xi_j}.
}
\tag{15.1}
$$


This verifies the normalization and the extra correction. The classical reference does not absorb that correction.

---

## 16. Endpoint determinant and fixed-shift saddle

### 16.1 Determinant identity

For row vectors $u,v$ and an invertible matrix $M$,


$$
(uM)\times(vM)=\det(M)M^{-1}(u\times v).
$$


Here


$$
\ell_0=(-1,n,-n(n+1)),\qquad \ell_3=(0,0,1),
$$


so


$$
\ell_0\times\ell_3=(n,1,0)^T.
$$


Taking $M=\operatorname{adj}(T_n)$ gives


$$
R_0\times R_3
=\Delta_T\bigl(n\operatorname{col}_0(T_n)+\operatorname{col}_1(T_n)\bigr).
$$


Also,


$$
\mathbf v_n\times\mathbf w_n
=
\begin{pmatrix}
1/4\\ -(2n+3)/(2(n+2))\\1/2
\end{pmatrix}.
$$


Their scalar product proves


$$
\boxed{\alpha_0\beta_3-\beta_0\alpha_3=\Delta_T\mathcal H_n.}
\tag{16.1}
$$



The coefficient recurrence


$$
(j+1)c_{j+1}
=(j+1-n)c_j+
\left(n-\frac{j+1}{2}\right)c_{j-1}
+\frac12c_{j-2}
$$


follows by comparing coefficients in


$$
Q(e^zQ^n)'=(Q+nQ')e^zQ^n.
$$


Substitution at $j=n,n+1$ verifies both simplifications of $\mathcal H_n$, including


$$
\mathcal H_n
=\frac{n+1}{2(n+2)}
\bigl(b+(n-3)c-2(n-1)d\bigr).
\tag{16.2}
$$



### 16.2 Saddle asymptotic

Let


$$
A(z)=1+z+\frac{z^2}{2},\qquad R=\sqrt2,\qquad M=1+\sqrt2.
$$


Then


$$
\tau_n=[z^n]A(z)^n,
$$


and


$$
c_{n+s}=(-1)^{n+s}[z^{n+s}]A(z)^ne^{-z}.
$$



On $z=Re^{i\theta}$,


$$
\frac{A(Re^{i\theta})e^{-i\theta}}{A(R)}
=\frac{R+2\cos\theta}{2+R}
=:\varphi(\theta).
$$


Thus


$$
\tau_n=\frac{M^n}{2\pi}
\int_{-\pi}^{\pi}\varphi(\theta)^n\,d\theta,
$$


while


$$
c_{n+s}
=\frac{(-1)^{n+s}M^nR^{-s}}{2\pi}
\int_{-\pi}^{\pi}
\varphi(\theta)^n e^{-Re^{i\theta}}e^{-is\theta}\,d\theta.
$$



Now


$$
\varphi(\theta)
=1-\frac{2-\sqrt2}{2}\theta^2+O(\theta^4),
$$


and $|\varphi(\theta)|<1$ on every closed arc excluding $0$. On the central arc, the even part of


$$
e^{-Re^{i\theta}}e^{-is\theta}
$$


is $e^{-R}(1+O(\theta^2))$, uniformly for the five fixed shifts. Gaussian scaling shows that the relative error is $O(n^{-1})$; the complementary arcs are exponentially smaller. Hence


$$
\boxed{
c_{n+s}
=(-1)^{n+s}e^{-\sqrt2}(\sqrt2)^{-s}\tau_n
(1+O(n^{-1})).
}
\tag{16.3}
$$



Substitution in (16.2) yields


$$
\boxed{
\mathcal H_n
=(-1)^n\frac{1+\sqrt2}{2}\,
n e^{-\sqrt2}\tau_n(1+O(n^{-1})).
}
\tag{16.4}
$$


Thus $\mathcal H_n\ne0$ eventually.

At the accepted local nonvanishing scope,


$$
\kappa_0-\kappa_3
=
-\frac{4(-1)^n\Delta_T\mathcal H_n}
{(n+1)\xi_0\xi_3}\ne0
$$


eventually on both original smooth families.

**Verdict:** the noncollapse theorem is rigorous. It proves nonvanishing of this correction difference, not nonvanishing of the final whole error.

---

## 17. Reduced endpoint denominators and the selected-prime law

Let


$$
c_j=\frac{v_j}{u_j},\qquad d_j=\operatorname{den}(c_j)>0.
$$


After any common clearing of the complete columns, primitive reduction of endpoint row $j$ gives an integer pair whose first coordinate has absolute value $d_j$. Therefore


$$
h=\gcd(d_0,d_3),\qquad
\boxed{|AB|=\frac{d_0d_3}{h^2}.}
\tag{17.1}
$$



This is independent of the preliminary clearer, but it is not independent of the complete companion force.

For every prime $p$,


$$
E_j(p)=
\max\{0,v_p(n!\xi_j)-v_p(N_j)\}
$$


is exactly $v_p(d_j)$. Thus


$$
\boxed{
v_p(|AB|)=|E_0(p)-E_3(p)|.
}
\tag{17.2}
$$


The formula accounts for cancellation inside $\xi_j$, cancellation against $N_j$, both endpoint row contents, and the common endpoint factor $h$.

At selected primes, the accepted theorem gives


$$
v_p(u_0)=v_p(u_3)=m_p=2v_p(n!),\qquad
v_p(v_3)=0,
$$


and


$$
v_3(v_0)=r,\qquad v_5(v_0)=r+1,\qquad
v_7(v_0)=r
$$


when the prime is selected. Since these values are less than $m_p$,


$$
v_p(d_0)=m_p-v_p(v_0),\qquad
v_p(d_3)=m_p.
$$


Therefore


$$
\boxed{(|AB|)_{\mathcal P}=5n.}
\tag{17.3}
$$



The complementary factor is still


$$
\boxed{
|AB|_{\mathcal P^c}
=
\prod_{p\notin\mathcal P}
p^{\left|
[v_p(n!\xi_0)-v_p(N_0)]_+
-
[v_p(n!\xi_3)-v_p(N_3)]_+
\right|}.
}
\tag{17.4}
$$


No supplied argument bounds this product sufficiently for the desired global conclusion.

The obstruction to importing the $b=0$ growth theorem is therefore precise: the additional rational corrections have no proved reduced-height bound, and the complete row contents outside $\mathcal P$ remain uncontrolled. Real asymptotic smallness does not bound rational denominator height.

---

# Part IV. Primitive arithmetic and whole errors

## 18. Ternary determinant route

Retain


$$
D_0=\det\Theta,\qquad
D_1=e_{\rm act}^T\operatorname{adj}(\Theta)e_{\rm act}
-3^{26}d_{\rm act}\det\Theta.
$$


The subtraction is indispensable.

When both members are nonzero,


$$
v_3(q)=
\max\left\{
0,h-26+2v_3((n-1)!)+v_3(D_1)-v_3(D_0)
\right\}.
$$


There is no dimension-multiplied primitive-denominator gain from the common matrix depth.

With the least actual clearer,


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,\qquad
g_\ell=\gcd(|A_\ell|,|B_\ell|),
$$


the primitive pair is


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole evaluated error is


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
\tag{18.1}
$$



---

## 19. Gram routes

For A2 and A5, retain the least actual two-column clearer $d_B$, all reconstructed rows, and the complete integer Gram pair:


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


Then


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
}
\tag{19.1}
$$


Every prime remains in this gcd.

For A2,


$$
v_{29}(q_n)
=
\max\{0,2F_n-F_b-1+\delta-\mu\}.
$$


The local alignment, if proved, would determine only this local contribution.

For A5, the accepted binary endpoint solve is an input. The coordinator reports a nontrivial actual endpoint correction, not the identity. The weighted norm and mixed outputs remain uncomputed. The complete force, all valid factorial channels, the justified logarithmic budget, and the exterior term $W_b\mathsf a_b$ must still be combined at norm-sensitive precision.

In both routes,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi)
$$


must be used through the whole identity


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
\tag{19.2}
$$


Signed-error asymptotics alone do not control the actual primitive denominator.

---

## 20. Endpoint-weight route

After complete endpoint row reduction, retain


$$
\widetilde u_0=hA,\qquad
\widetilde u_3=hB,\qquad \gcd(A,B)=1,
$$


and


$$
J=B\widetilde v_0-A\widetilde v_3,\qquad
T=aJ+kA\widetilde v_3.
$$


For reduced $a/k$, the full gcd factors are


$$
F_{\rm gcd}=\gcd(|A|,|a|)\gcd(|B|,|a-k|),
$$




$$
G=\gcd(k,|J|),\qquad
H_{\rm gcd}=
\gcd\!\left(h,\frac{|T|}{F_{\rm gcd}G}\right).
$$


The actual primitive pair remains


$$
q_\lambda=
\frac{kh|AB|}{F_{\rm gcd}GH_{\rm gcd}},
$$




$$
p_\lambda=
\operatorname{sgn}(AB)\frac{T}{F_{\rm gcd}GH_{\rm gcd}}.
$$



The complete moving residue still includes


$$
F(n)=\sum_{t=0}^n n^{\underline t}
$$


and the complete logarithmic restoration. The whole error is


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
}
\tag{20.1}
$$


A favorable denominator estimate does not prove $\lambda\ne\Lambda_{n,2}$. Conversely, a large denominator does not alone rule out an exceptionally small distance to the actual threshold.

---

# Part V. Proof-status ledgers

## 21. A1turn13

| Claim | Verdict | Exact qualification |
|---|---|---|
| Same-factor precision-$11/12$ saturation compatibility | Accept | Monic multiplication is injective modulo $3^{11}$ |
| Finite core representatives and upper gap | Accept at accepted support scope | Requires (3.1), original HIGH boundaries, complete return |
| Weighted inverse truncation | Accept | Retain $6r+b<L$; require both factor and degree budgets |
| Extra transfer digit | Accept | Uses $\deg f_i\le m-1$ and absence of the unique unit pole |
| Complete nonlinear restoration | Accept | Full $E_{\rm act}^{-1}$ retained in the exact identity |
| General forgetting theorem | Accept | All conditions (4.7) simultaneous |
| $P=25,L=31,p=25,\kappa_{25}=54$ | Accept | Sufficiently large original fixed window |
| Depth $26$, agreement through depth $32$ | Accept | Conditional only on the accepted underlying support scope |
| First normalized coefficient formula | Accept with clarified derivation | Both core representatives; whole bracket before division |
| First-layer rank or pair valuations | Open | No coefficient matrix computed |
| Six-digit complete-pair transfer | Proved here | Polynomial continuity; no inverse hypothesis needed |
| All-prime denominator and whole error | Open | Local depth does not settle either |

## 22. A2turn10

| Claim | Verdict | Exact qualification |
|---|---|---|
| Divided-power finite lower inverse | Accept | Exact finite triangular identity |
| Precision cutoff $j-k<29K$ | Accept | Factorial valuation |
| Actual finite inverse | Accept | Original factor order and finite correction retained |
| Adjoint telescope | Accept | Actual rows $1,\ldots,b-2$, two initial charges |
| Interior impulse output difference | Accept | Does not imply actual nonzero defect |
| Exterior term | Accept | Exactly $bW_b^2(A^{-1}f^0)_{b-1}$ |
| Squared-weight kernel | Accept | Includes nearest neighbors and terminal diagonal |
| Finite gluing | Accept | Enforces every contracted index $<b$ |
| $32$-variable bound | Accept with explicit construction | Endpoint symbol matrices multiplied externally |
| $256K+16$ degree bound | Accept | Source-subtraction bookkeeping supplied above |
| $100(29K+2)^4$ task bound | Accept with explicit construction | Small scalar-input generation remains separate |
| Displayed $145K$ source numerator bound | Clarify/repair | Split the constant subtraction, or use $145K+1$ |
| Feasible original-index realization | Open | Dense bound is prohibitive, not an impossibility theorem |
| True-norm alignment | Open | Must reach $v_{29}(\mathcal N)+2$ |
| Full gcd and whole-error comparison | Open | All primes and complete force remain |

## 23. A3turn8

| Claim | Verdict | Exact qualification |
|---|---|---|
| Five-moment Toeplitz normalization | Accept | Original $3\times3$ matrix only |
| Adjugate endpoint formulas | Accept | Row factorials and exterior $+1$ retained |
| Classical logarithmic normalization | Accept | Uses accepted terminal identities; no novelty claim |
| Transformation determinant | Accept | Cross-product identity gives the stated sign |
| Three-moment simplification | Accept | Direct coefficient recurrence |
| Fixed-shift saddle asymptotic | Accept | Five fixed shifts, not a growing-shift assertion |
| Eventual logarithmic noncollapse | Accept | Not final whole-error nonvanishing |
| Reduced endpoint-denominator formula | Accept | Both complete rows reduced first |
| Selected-prime law $5n$ | Accept | Original smooth families and accepted local theorem |
| Complementary-prime growth | Open | Force-dependent row cancellation remains |
| Transfer of the $b=0$ growth theorem | Open | Extra correction heights are unbounded by current results |
| Favorable primitive whole forms | Open | Actual denominator and threshold distance both needed |

---

# 24. Bounded exact calculations worth requesting

These are proposals, not computations reported as completed.

## 24.1 Highest-value local structural calculation: A1 core pair

**Inputs**

- A certified original tuple $(j,n,H,D,h)$ on the retained fixed window.
- The complete finite core blocks on $U,Z,Y$.
- Core representatives $\phi_i\bmod3^{25}$.
- Complete core endpoint transport.
- Target normalized precision $K=6$.

**Calculation**

The same representatives suffice for all six digits. Indeed, (7.1) at $P=25$ gives an absolute error in $3^{50}$, well beyond the required modulus $3^{32}$. Compute


$$
-\frac{G_c(\Phi,\Phi)}{3^{26}}\pmod{3^6}
$$


using the complete factorial term and every finite pole that survives modulo $3^{32}$.

Then compute the complete pair (8.2), including its scalar subtraction.

**Required verifiable output**

1. Original-index and finite-boundary certificate.
2. Divisibility before every normalization.
3. The normalized matrix, or an exact structured representation with reconstruction identity.
4. Rank, radical, and endpoint restriction modulo $3$.
5. $D_{0,c},D_{1,c}\bmod3^6$.
6. If a residue is nonzero, its certified valuation; otherwise only the corresponding lower bound.

No nonzero output is predicted. The computation may be extremely large; no feasible runtime claim is made.

## 24.2 Bounded A2 weighted/telescope audit

Use the auxiliary input


$$
n=203,\qquad b=143,\qquad K=2.
$$


This is not an original-family index.

Take the certified finite contact inverse as input rather than reopening the endpoint solve. Retain contact coordinates $0,\ldots,142$, source rows $1,\ldots,141$, and reconstruction through $143$.

Verify:

- direct weighted contractions against the squared-weight rational kernel;
- the complete adjoint identity at every source row;
- the three contact-end correction terms separately;
- the exterior term separately;
- finite coefficient gluing against direct finite sums;
- the four actual impulse pairs $q=0,1,2,3$, without adding a fifth pair.

If complete initial-force checks are included, generate the factorial/logarithmic data through index $548$. Expected output is zero identity discrepancy, not a predicted normalized alignment defect.

## 24.3 Practical all-prime normalization audit: A3 at $n=225$

Use the original-family input


$$
n=225=15^2.
$$


Retain the complete force through $452$ and the full reconstruction at rows $0,1,2,3$.

Return:

- the least full two-column clearer;
- all row contents;
- the two reduced endpoint denominators $d_0,d_3$;
- $h,A,B$;
- the actual integer $|AB|_{\{3,5\}^c}$;
- agreement with the four-rational-number reduction from $n!\xi_0,n!\xi_3,N_0,N_3$.

The selected-prime outputs predicted by the accepted theorem are


$$
\begin{array}{c|ccc}
p&v_p(d_0)&v_p(d_3)&v_p(|AB|)\\ \hline
3&218&220&2\\
5&107&110&3.
\end{array}
$$


Thus the selected part should be $1125$.

For the fixed probes


$$
\lambda=0,\quad1,\quad\tfrac12,\quad\tfrac{n^2}{2},
$$


return the complete gcd factors and primitive pair, with direct fraction reduction as an independent check. Any whole-error interval must evaluate the complete center against the complete $e+\pi$; an interval containing zero is inconclusive.

This is the most manageable proposed new exact arithmetic audit. Its conclusions would remain finite.

---

# 25. Highest-value next obligation and final conclusion

The highest-value **next symbolic obligation** is now the A1 core relative-pair problem within the proved six-digit interval:

> Determine the radical and endpoint action of
> 

$$
> \Theta_c=-S_c/3^{26}\pmod3,
>
$$


> then use the complete radical/complement reduction to prove that the two core pair members become nonzero before precision $3^6$, or establish a stronger structured relative-valuation law if they do not.

This is more decisive than another producer digit or another common zero layer. Proposition 8.1 shows exactly how a successful core result transfers to the actual pair.

Across the other routes:

- **A2:** the missing lemma is the boundary-aware weighted coefficient alignment at the true norm depth.
- **A3:** the missing lemma controls the difference of the two fully reduced denominator valuations outside the selected primes.
- **A5:** the missing lemma constructs a usable output-compatible modular realization for the complete weighted contractions, beyond the accepted endpoint solve.

The global bottleneck remains unchanged. To prove irrationality by any of these constructions, one needs infinitely many original indices with actual primitive integers $p,q$ satisfying


$$
\boxed{0<|q(e+\pi)-p|\longrightarrow0.}
$$


That requires, on the same indices:

1. complete-force evaluation;
2. all row contents and the final all-prime gcd;
3. the actual primitive denominator;
4. nonvanishing and decay of the whole evaluated error.

The new rigorous results of this audit are the verified complete A1 transfer, a direct six-digit transfer theorem for its full determinant/cofactor pair, and an explicit construction validating A2’s aggregate representation bounds with the stated bookkeeping repair. A3’s endpoint reduction and infinite noncollapse theorem also survive independent review.

None of these results supplies the missing all-prime, same-index whole-error theorem.



$$
\boxed{\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$


