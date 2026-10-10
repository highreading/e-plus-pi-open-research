> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 15 — Audit of refined propagation, nonlinear divisibility, and complete-force channels

## Executive assessment

The supplied sources support further local progress, but not an unconditional proof or disproof of irrationality of $e+\pi$.

My conclusions are:

1. **A1turn8’s refined propagation and $\mathcal Q\in27M$ pass after making two precision arguments explicit.**  
   In particular, using $R$ and $\widehat z^{\,c}$ only modulo $27$ in the **LOW** force divided by $3$ is legitimate: the normalized LOW functional is integral on the entire relevant bounded-degree space. This is stronger than merely observing that one particular force value is divisible by $3$.

2. **The actual LOW inverse zeros, terminal corrected-column formula modulo $9$, terminal inverse correction, and lower-boundary return all pass on the original domain.**  
   The proof must distinguish:
   - normalized LOW evaluations, where there is no precision loss;
   - unrestricted HIGH evaluations divided by $3$, where there can be a loss;
   - undivided complete evaluations modulo $27$, used for the lower-boundary return.

3. **All signs and powers in the at-most-twenty-feature decomposition and bordered determinant pair pass.**  
   “Integral unit matrix” should mean an invertible matrix over $\mathbb Z_3$, not the identity matrix. The decomposition does not bound the rank of its bulk term or prove either member of the determinant pair nonzero.

4. **A2turn5’s factorial-tail recurrence, nearest-neighbor pullback, integral-valued impossibility, degree-$\le26$ obstruction, and degree-$27$ matching coefficient pass.**  
   The newly supplied entrywise logarithmic force permits a further exact evaluation of the recurrence’s logarithmic source.

5. **The weighted two-channel transformation is an integral isometry to a hyperbolic-coordinate presentation.**  
   Its channel criterion is equivalent to relative alignment at the normalization used in A2turn5. After removing content from the second column, the criterion must be rescaled. I give an equivalent formulation for every content level, including the case where the second column has more content than the first.

6. **A concrete new actual consequence is available for the degree-$27$ obstruction.**  
   Put
   

$$
J_0=[t^n](1+2t+2t^2)^n.
$$


   For the actual first contact solution,
   

$$
\boxed{\theta_{b-26}\equiv0,\qquad
   \theta_{b-25}\equiv J_0\pmod{29}.}
$$


   Therefore the degree-$27$ escape condition sharpens to
   

$$
\boxed{-15\lambda J_0=1\quad\text{in }\mathbb F_{29}.}
$$


   Thus $J_0\equiv0\pmod{29}$ rules out that escape on the deep branches under discussion. When $J_0$ is a unit, the equation fixes $\lambda$, but does not prove the complete force identity.

No tools were executed. The supplied arithmetic certificates are used only at their stated finite scope.

---

# I. A1turn8: refined propagation on the original finite interval

## 1. Domain and complete functional

Throughout this part retain


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$




$$
A=n-2=H-D,\qquad H=3^{h-1},\qquad0<D<H/972,
$$


and


$$
t=v_3(A)\ge5.
$$


The actual finite dimensions are


$$
m=\frac{A+1}{2},\qquad
d=\frac{3D}{2}-1,\qquad
\nu=\frac D2-1.
$$


The columns are exactly


$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),\qquad
Y_b=y^b\quad(d\le b\le m),
$$


where $x=y-1$.

In particular,


$$
\deg z_i\le d-1,\qquad i+j\le D-4.
$$



The complete functional is


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
\qquad \mathfrak f(y^r)=(2r)!.
$$


Every support argument below concerns this functional, including its endpoint subtraction and original cutoff.

The accepted producer interface is


$$
Q_n^{\rm loc}=Q_c+3^6R,\qquad
Q_c=(y+1)x^A(\beta+3y),\qquad
\deg R\le A+1.
$$



---

## 2. The complete division-safe return formula passes

Let


$$
r_*=\frac{3H-1}{2},\qquad r_1=\frac{H-1}{2}.
$$


Separating the unique top pole gives exactly


$$
G_c=\beta H_0+3H_1+3\Lambda,
$$


where $\Lambda$ contains every lower pole and the complete factorial contribution divided by $3$.

For a finite HIGH polynomial $p$, write


$$
p=Ur+x^Dq,\qquad \deg(Ur)<D,
$$


and set


$$
\varepsilon=L^{-1}\Lambda(U,x^Dq).
$$


Then


$$
L^{-1}Xp=r+\varepsilon.
$$


Consequently


$$
\begin{aligned}
(\mathsf F_Hp)_b={}&
\frac{\beta-1}{3}[y^{r_*}]x^Hq\,y^b
+[y^{r_*}]x^Hyq\,y^b\\
&+\sum_{\substack{0\le a\le h-1\\c\ge1\ {\rm odd},\ 3\nmid c\\c3^a\le4n-3}}
3^{h-1-a}c^{-1}
[y^{(c3^a-1)/2}]x^H(\beta+3y)q\,y^b\\
&-\frac{3^{h-1}}4
\mathfrak f((y+1)x^H(\beta+3y)q\,y^b)
-(X^T\varepsilon)_b .
\end{aligned}
\tag{2.1}
$$



This is an exact identity, not a congruence obtained by dividing an insufficiently precise numerator. It proves


$$
(\widehat E-E_0)p=3\mathsf F_Hp
$$


with the full LOW subtraction already present.

### Support and endpoints

At precision $3^q$, the binomial valuation formula


$$
v_3\binom Hk=h-1-v_3(k)
$$


places $x^H$ on the required integer grid. Every surviving normalized lower pole lies on its odd half-grid.

Under


$$
W+D<\frac{\Omega-1}{2},
$$


the LOW error $\varepsilon$ vanishes at that precision, and (2.1) gives the half-grid support with width $W+1$.

The finite inverse formula


$$
(R_H)_{ab}=[z^{d+m-a-b}](1-z)^{-A},
\qquad d\le a,b\le m,
$$


also passes. In its polynomial-copy interpretation:

- negative quotient exponents cannot reach HIGH after multiplication by $x^D$, since their resulting degree is at most $D-1<d$;
- the upper endpoint is respected because
  

$$
r_1-b\le r_1-d=m-D;
$$


- removing the part below $d$ changes the monic quotient only in degrees at most
  

$$
d-1-D=\nu-1.
$$



Thus, for $W\ge\nu-1$,


$$
R_H\mathsf F_H:\mathcal C_\Omega(W)\longrightarrow
\mathcal C_\Omega(W+1)
$$


at the stated precision.

### Refined window

For


$$
D<H/2916,\qquad \Omega'=H/729,
$$


the arithmetic separation


$$
\Omega'-4D\ge3^t\ge243
$$


is sufficient for the displayed return words and final contractions. The modulo-$3^7$ initial coupling and modulo-$3^6$ returned terms are compatible with the seven-term inverse expansion.

Accordingly,


$$
\boxed{V\widehat E^{-1}V^T\in3^7M}
$$


passes on this sharper domain. This conclusion is not inferred merely from the coarser result audited in Turn 13.

---

# II. A1turn8: the nonlinear claim $\mathcal Q\in27M$

## 3. The essential LOW precision lemma

The potentially dangerous operation is


$$
a_{ui}=\frac{K(U_u,\widehat z_i^{\,c})}{3}.
$$



Here is the precise reason that $R\bmod27$ and $\widehat z_i^{\,c}\bmod27$ suffice.

### Lemma 1 — bounded-degree normalized LOW integrality

For every


$$
S\in\mathbb Z_3[y],\quad \deg S\le A+1,
\qquad
f\in\mathbb Z_3[y],\quad \deg f\le m,
$$


and $0\le u<D$,


$$
\boxed{\frac{\mathcal M(SU_uf)}3\in\mathbb Z_3.}
\tag{3.1}
$$



**Proof.** The product has degree at most


$$
(A+1)+(D-1)+m=H+m<r_*.
$$


Hence the endpoint-subtracted quotient has no coefficient at $r_*$. The unique weight of valuation zero is therefore absent identically. Every remaining pole weight in $\mathcal M$ is divisible by $3$; the factorial coefficient is also divisible by $3$. ∎

This proves an integral bilinear map on the entire relevant degree-bounded spaces. Therefore replacing either argument by a congruent representative modulo $27$ changes the divided LOW force by a multiple of $27$.

**Audit finding:** A1turn8’s LOW substitution is valid, but (3.1) is the necessary precision justification. Divisibility of one evaluated value alone would not suffice.

---

## 4. Actual LOW support and actual inverse zeros

Use the accepted saturated jet


$$
R\equiv(y+1)x^{A-\kappa_3}B_3(x)\pmod{27},
\qquad \deg B_3\le\kappa_3\le9,
$$


and the corrected-column representative


$$
\widehat z_i^{\,c}\equiv x^D\psi_i\pmod{27},
\qquad
\operatorname{supp}\psi_i\subset I_\Omega(\nu+1),
\qquad \Omega=H/243.
$$



For $u\ge\kappa_3$, the normalized LOW quotient is


$$
x^H x^{u-\kappa_3}B_3(x)\psi_i.
$$


Its nongrid width is at most


$$
u+\nu+1\le\frac{3D}{2}-1<\frac{\Omega-1}{2}.
$$


Every surviving normalized lower-pole extraction vanishes. The factorial term vanishes at this modulus by its explicit coefficient. Lemma 1 justifies the substitutions before division.

Thus


$$
\boxed{a_{ui}\equiv0\pmod{27}\qquad(u\ge\kappa_3).}
\tag{4.1}
$$



For the core LOW matrix, $u+v\ge D$ gives quotient


$$
x^H x^{u+v-D}(\beta+3y).
$$


The same separation proves


$$
L_{uv}\equiv0\pmod{27}\qquad(u+v\ge D).
$$


The antidiagonal is a unit modulo $3$. Since


$$
L_{\rm act}-L\in3^5M,
$$


the actual matrix has the same zero region modulo $27$.

Column reversal produces a triangular unit matrix over $\mathbb Z/27\mathbb Z$. Reversing its inverse gives


$$
\boxed{(L_{\rm act}^{-1})_{uv}\equiv0\pmod{27}
\qquad(u+v<D-1).}
\tag{4.2}
$$



Because $D\ge486$ and $\kappa_3\le9$, (4.1)–(4.2) imply


$$
\boxed{a^TL_{\rm act}^{-1}a\in27M.}
\tag{4.3}
$$



The supplied $18\times18$ certificate corroborates the analogous modulo-three finite algebra. It does not itself establish (4.1)–(4.3) modulo $27$ or on original indices; the symbolic argument does that.

---

## 5. The terminal corrected column modulo $9$

The source formula


$$
\widehat z_i^{\,c}
\equiv z_i-3\pi(y^d)\mathbf1_{i=\nu-1}\pmod9
\tag{5.1}
$$


passes, with


$$
\pi(y^d)=y^d-\operatorname{rem}_{x^D}y^d.
$$



The relevant checks are:

1. The normalized LOW coupling of $z_i$ vanishes modulo $9$ by the complete lower-pole separation.
2. Modulo $3$, the normalized HIGH coupling is the single terminal corner. Indeed,
   

$$
H+i+b\le r_*-1;
$$


   only the additional $y$ in $3y$ reaches the top pole, and only for
   

$$
i=\nu-1,\qquad b=m.
$$


3. The finite inverse sends that terminal HIGH coordinate to the lower HIGH endpoint:
   

$$
R_He_m=e_d.
$$


4. Restoring the LOW projection turns $y^d$ into $\pi(y^d)$, rather than leaving an uncorrected monomial.

For the subsequent HIGH mixed force divided by $3$, one must not invoke Lemma 1 indiscriminately. Instead, the modulo-$9$ remainder in (5.1) contributes a multiple of $3$ after division, because the undivided complete functional is integral.

After LOW elimination, the normalized lower pole cancels. The top contribution from the correction in (5.1) is


$$
-c\,e_me_{\nu-1}^T,\qquad c=[y^{A+1}]R.
$$


Hence


$$
\boxed{\widetilde b\equiv-c\,e_me_{\nu-1}^T\pmod3.}
\tag{5.2}
$$



The minus sign is correct.

---

## 6. Terminal inverse correction and lower-boundary return

Write


$$
H_{\rm inv}=\widehat E_{\rm act}^{-1},\qquad
\mathcal C=\frac{H_{\rm inv}-R_H}{3}.
$$


Since $\widehat E_{\rm act}\equiv E_0\pmod3$, $\mathcal C$ is integral, and


$$
\mathcal C=-R_HF_{\rm act}H_{\rm inv}.
$$


Thus


$$
\mathcal C_{mm}\equiv-(F_{\rm act})_{dd}\pmod3.
$$



At this precision the actual perturbation does not change $F_{\rm act}$. The entry is represented by the normalized core pairing of $\pi(y^d)$ with itself. Its lower quotient is


$$
x^{H+D}q_d^2(\beta+3y).
$$


Modulo $3$, the low-degree part has degree at most $D+2\nu=2D-2<r_1$; its other part begins at degree $H$. The top pole is absent by degree. Therefore


$$
\boxed{\mathcal C_{mm}\in3\mathbb Z_3.}
\tag{6.1}
$$



Next define


$$
\mathcal B=\frac{\widetilde b+c\,e_me_{\nu-1}^T}{3},
\qquad w=\mathcal B^Te_d.
$$


The actual LOW projection of $y^d$ equals its monic remainder modulo $27$, so


$$
3\widetilde b_{d,\bullet}
\equiv K(\pi(y^d),\widehat Z^{\,c})\pmod{27}.
$$


This is an **undivided** evaluation modulo $27$. Substitution of the jet and corrected-column representative is consequently safe under ordinary integrality of $\mathcal M$.

Its quotient is


$$
x^H x^{D-\kappa_3}B_3q_d\psi_i,
$$


of nongrid width at most $2D-1$. Since $\Omega>4D$, it misses all six pole positions surviving in $\mathcal M\bmod27$. The endpoint subtraction is retained through $R(-1)\equiv0\pmod{27}$.

Thus


$$
\widetilde b_{d,\bullet}\in9M,\qquad
\boxed{w\in3\mathbb Z_3^\nu.}
\tag{6.2}
$$



---

## 7. Nonlinear expansion and all boundary signs

With $M=L_{\rm act}^{-1}$, $u=e_m$, $v=e_{\nu-1}$,


$$
\mathcal Q=a^TMa+3\widetilde b^TH_{\rm inv}\widetilde b.
$$


Insert


$$
\widetilde b=-cuv^T+3\mathcal B,\qquad
H_{\rm inv}=R_H+3\mathcal C,
$$


and use


$$
R_Hu=e_d,\qquad u^TR_Hu=0.
$$


Direct expansion gives


$$
\begin{aligned}
\frac{\mathcal Q}{27}={}&
\frac{a^TMa}{27}
+\mathcal B^TH_{\rm inv}\mathcal B
+\frac{c^2\mathcal C_{mm}}3vv^T\\
&-\frac c3(vw^T+wv^T)
-c\bigl(vu^T\mathcal C\mathcal B+
\mathcal B^T\mathcal Cuv^T\bigr).
\end{aligned}
\tag{7.1}
$$


Every term is integral by (4.3), (6.1), and (6.2). Therefore


$$
\boxed{\mathcal Q\in27M_\nu(\mathbb Z_3)}
$$


is proved on the original $D<H/972$ domain.

The LOW expansion


$$
a=P\alpha+27a_1
$$


gives


$$
\frac{a^TMa}{27}
=\alpha^TJ_{\rm low}\alpha+
\alpha^T\zeta+\zeta^T\alpha+27a_1^TMa_1.
$$


The definitions


$$
\tau=\frac{c^2\mathcal C_{mm}}3,\qquad
\gamma=-c\left(\frac w3+\mathcal B^T\mathcal Cu\right)
$$


then yield precisely


$$
\boxed{
\frac{\mathcal Q}{27}
=\mathcal B^TH_{\rm inv}\mathcal B
+27a_1^TMa_1+\mathcal F^T\mathcal J\mathcal F.
}
$$


The cross-term signs and factors are correct. Also


$$
\det\mathcal J=(-1)^{\kappa_3+1},
\qquad \dim\mathcal J=2\kappa_3+2\le20.
$$



---

## 8. Bordered pair, depth $16$, and primitive normalization

On the stated sufficiently large original-index window, the accepted core and saturated linear-force bounds combine with the audited nonlinear result to give


$$
S_{\rm act}=-3^{16}\Psi.
$$


This is a guaranteed common depth, not a first-nonzero-depth theorem.

For


$$
\Psi=\mathcal A+\mathcal F^T\mathcal J\mathcal F,
\qquad
\mathscr K=
\begin{pmatrix}
\mathcal A&\mathcal F^T\\
\mathcal F&-\mathcal J^{-1}
\end{pmatrix},
$$


the Schur complement is $\Psi$, with the **plus** sign. Consequently both bordered identities in A1turn8 pass, including the complete cofactor subtraction


$$
\delta_1=e^T\operatorname{adj}(\Psi)e
-3^{16}d_{\rm act}\det\Psi.
$$



When $\delta_0\delta_1\ne0$,


$$
\frac{\beta_1}{\beta_0}
=-\frac{3^{h-16}Q_n^{\rm loc}(-1)}4\frac{\delta_1}{\delta_0},
$$


and


$$
v_3(q)=
\max\{0,h-16+v_3(Q_n^{\rm loc}(-1))
+v_3(\delta_1)-v_3(\delta_0)\}.
$$



The complete normalization remains


$$
g_\ell=\gcd(|\ell^{m+1}\beta_0|,|\ell^{m+1}\beta_1|),
\qquad
q=\frac{|\ell^{m+1}\beta_1|}{g_\ell},
$$


and the whole error is


$$
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_\ell)\ell^{m+1}}{g_\ell}
\det H_{\rm complete}.
$$



Neither determinant-pair nonvanishing nor its relative valuation has been proved. The common determinant powers cancel exactly as stated in the source.

---

# III. A2turn5: complete factorial and logarithmic force recurrence

## 9. The factorial-tail recurrence passes

Retain the actual family


$$
a=432827+682892t,\quad t\ge0,\qquad
b=3^a,\qquad n=2001b,
$$


with weighted coordinates $0\le j\le b$ and contact coordinates $0\le j<b$.

For


$$
T_m=\frac1{b!}\sum_{q=b}^m(m)_{\underline q},
$$


the exact recurrence is


$$
T_m=mT_{m-1}+\binom mb.
$$


The binomial term is the genuine factorial boundary source.

Transport through $\phi(z)^n$, where


$$
\phi(z)=1-z+\frac{z^2}{2},
$$


gives the four-term operator in A2turn5:


$$
\begin{aligned}
(\mathcal D_nr)_i={}&r_{i+1}-(2n+2i+1)r_i\\
&+\frac{(n+i)(n+3i-1)}2r_{i-1}
+\frac{(n+i)(n+i-1)(1-i)}2r_{i-2}.
\end{aligned}
$$


Its coefficients and signs pass.

The interior range remains


$$
2\le i\le b-2.
$$


Initial values and the actual last contact row are not supplied by extending this recurrence outside its finite range.

---

## 10. New explicit logarithmic source

The new excerpt supplies


$$
F(z)=4\arctan\frac{z}{2-z},\qquad
\mathcal F_m=[z^m]\frac{F(z)}{1-z}.
$$


Direct differentiation gives


$$
F'(z)=\frac2{\phi(z)}.
$$



Put


$$
L_m=m!\mathcal F_m,\qquad
a_m=[z^m]\phi(z)^{-1}.
$$


Since


$$
(1-z)\left(\frac F{1-z}\right)'
=\frac F{1-z}+\frac2\phi,
$$


we obtain


$$
\boxed{L_{m+1}=(m+1)L_m+2m!a_m.}
\tag{10.1}
$$


Here


$$
a_0=a_1=1,\qquad
a_m=a_{m-1}-\frac12a_{m-2}\quad(m\ge2).
$$



Applying the same shifted exponential-generating-function transport as for the factorial tail yields


$$
\boxed{
(\mathcal D_n\mathbf r)_i=\mathcal H_i+\mathcal L_i,
\qquad2\le i\le b-2,
}
\tag{10.2}
$$


where $\mathcal H_i$ is A2turn5’s complete binomial source and


$$
\boxed{
\mathcal L_i=
\frac2{b!}
\sum_{s=0}^{\min(2n+2,n+i)}
[z^s]\phi(z)^{n+1}
(n+i)_{\underline s}
(2n+i-s)!\,a_{2n+i-s}.
}
\tag{10.3}
$$



This explicitly evaluates the previously unnamed term
$\mathcal D_n(h^F/b!)$. It does not discard it.

### Actual valuation consequence

All coefficients of $\phi^{n+1}$ and $\phi^{-1}$ are $29$-integral. Also


$$
2n+i-s\ge n
$$


throughout (10.3). Hence


$$
\boxed{
\mathcal L_i\in29^{F_n-F_b}\mathbb Z_{29},
\qquad F_r=v_{29}(r!).
}
\tag{10.4}
$$



This is an exact original-family bound on the logarithmic **recurrence source**. It is not a bound on the logarithmic contact solution after inversion, nor an all-depth alignment theorem.

---

# IV. Nearest-neighbor pullback and a new terminal evaluation

## 11. Pullback, impossibility, and degree threshold

For


$$
g_j=(j+1)(n+2-j)h(j),
$$


the adjacent-weight calculation gives


$$
(\mathcal A(g)Z_w)_j=W_jt_j,
$$


with precisely the $t_j$ in A2turn5. The endpoint is


$$
t_b=-b^2h(b-1)q^\theta_{b-1};
$$


there is no edge beyond $b$.

The partial-sum reconstruction gives


$$
\mathcal R\eta_h=\mathcal A(g)Z_w-\kappa_hW_be_b,
$$


and therefore


$$
\mathcal K(g)Z_w=\mathcal R(\eta_h+\kappa_h\xi).
$$


All signs pass.

The complete-force identity is thus equivalent to


$$
\boxed{
(1-29\kappa_h)\xi=29s_n\theta+29\eta_h-\psi.
}
\tag{11.1}
$$



Using the accepted lift valuation


$$
v_{29}(\xi_{b-B-1})=14675394-v_{29}(b-B),
$$


integral-valued $h$ makes the right side integral and $1-29\kappa_h$ a unit. The contradiction on the stated deep branches is rigorous.

For $\deg h\le26$, integral edges force integral polynomial coefficients by interpolation on the 27 residue classes other than $2,-1$. The interpolation determinant is a unit. Thus that impossibility also passes.

At degree $27$, the coefficient-denominator bound and


$$
\overline{29h}=\lambda\frac{J^{29}-J}{(J-2)(J+1)}
$$


are correct. The evaluated coefficient


$$
\kappa_{29h}\equiv
15\lambda(2\theta_{b-26}-\theta_{b-25})\pmod{29}
$$


also passes.

---

## 12. New theorem: the two actual terminal contact residues

The last combination need not remain unevaluated.

### Theorem 2

For the actual first contact solution,


$$
\boxed{
\theta_{b-26}\equiv0,\qquad
\theta_{b-25}\equiv J_0\pmod{29},
}
\tag{12.1}
$$


where


$$
J_0=[t^n](1+2t+2t^2)^n.
$$



### Proof

Let $P_b$ be the finite lower Pascal matrix and $S$ the actual upper shift. The accepted integral contact identity gives


$$
\widetilde N\equiv B(n)\pmod{29},
\qquad
B(n)_{ij}=\binom{n+i}{j}.
$$


Finite Vandermonde factorization gives


$$
B(n)=P_b(I+S)^n.
$$


Therefore


$$
\theta\equiv(I+S)^{-2n}P_b^{-1}f^0\pmod{29}.
\tag{12.2}
$$



Since $29\mid n$, the power series $(1+z)^{-2n}$ modulo $29$ has only exponents divisible by $29$. At either row $b-26$ or $b-25$, the remaining upper-shift range is less than $29$. Thus the first factor in (12.2) acts as the identity at these rows.

The complete first force is


$$
f_i^0=\frac{(n+i)!}{n!}J_i.
$$


For $i\ge29$, its factorial product contains $n+29$, so


$$
f_i^0\equiv0\pmod{29}.
$$


For $0\le i<29$,


$$
\frac{(n+i)!}{n!}\equiv i!\pmod{29}.
$$


Moreover, Frobenius and $29\mid n$ show that
$(1+2t+2t^2)^n\bmod29$ has only degrees divisible by $29$. Therefore


$$
J_i\equiv J_0\pmod{29}\qquad(0\le i<29).
$$



Using


$$
(P_b^{-1})_{jk}=(-1)^{j-k}\binom jk,
$$


the required rows are now finite sums over $0\le k\le28$.

Since $b\equiv27\pmod{29}$, the residue of $b-26$ is $1$, and Lucas’s theorem leaves only $k=0,1$. Their contributions cancel.

The residue of $b-25$ is $2$, leaving $k=0,1,2$. Since $b$ is odd, $b-25$ is even, and their sum is


$$
J_0(1-2+2)=J_0.
$$


This proves (12.1). ∎

### Consequence

The necessary degree-$27$ condition becomes


$$
\boxed{-15\lambda J_0=1\pmod{29}.}
\tag{12.3}
$$



Thus:

- if $J_0\equiv0$, degree $27$ is impossible on the deep branches;
- if $J_0$ is a unit, $\lambda$ is uniquely determined;
- neither case settles the higher matching conditions or all remaining complete-force rows.

This is an actual first-force evaluation, not an inference from a norm residue.

---

# V. Unit-only channels and all removed-content levels

## 13. The transformation passes, with a terminology clarification

A2turn5’s transformation preserves


$$
y^Tz=
\frac{\mathfrak u(y)\mathfrak v(z)+
\mathfrak v(y)\mathfrak u(z)}2
+\sum_j\mathfrak w_j(y)\mathfrak w_j(z).
$$


All divisions are by $2$ or the demonstrated unit $\mathfrak a$. Its inverse is integral.

Strictly, the displayed coordinates give an isometry from the ordinary dot-product presentation to a hyperbolic-coordinate presentation. If an ordinary orthogonal matrix is desired, convert the final hyperbolic pair back using


$$
r'=\frac{\mathfrak u+\mathfrak v}{2},\qquad
s'=\frac{\mathfrak u-\mathfrak v}{2\iota}.
$$


These are also unit-only operations.

The actual factorization


$$
D=29^{2c}\mathfrak a\mathfrak b,\qquad
2M=29^c(\mathfrak a\mathfrak v+\mathfrak b\mathfrak u)
$$


is correct. Positive real norm nonvanishing gives $\mathfrak b\ne0$; it does not make $\mathfrak b$ a $29$-adic unit.

---

## 14. Exact criterion after arbitrary permitted content removal

Let


$$
P=29^cx,\qquad Q^\parallel=29^dy,
$$


where $x$ is primitive and $y$ integral. Here $d$ may be any removed second-column content level for which $y$ remains integral.

Apply the same first-column-determined transformation to $y$, obtaining channels $u_0,v_0$. Put


$$
\nu=v_{29}(\mathfrak b).
$$


Then exactly


$$
D=29^{2c}\mathfrak a\mathfrak b,\qquad
2M=29^{c+d}(\mathfrak av_0+\mathfrak bu_0).
\tag{14.1}
$$



### Case A: $d\le c$

Set $s=c-d\ge0$. Relative alignment is equivalent to


$$
\boxed{v_0\in\mathfrak b\mathbb Z_{29},}
$$


and


$$
\boxed{
\mathfrak a\frac{v_0}{\mathfrak b}+u_0
-2\rho_n29^s\mathfrak a
\in29^{s+1}\mathbb Z_{29}.
}
\tag{14.2}
$$



This includes A2turn5’s criterion when $d=0$.

### Case B: $d>c$

Put $t=d-c>0$.

If $\nu<t$, alignment is impossible: the mixed product has valuation at least $c+d$, strictly larger than


$$
v_{29}(D)=2c+\nu,
$$


so it cannot be congruent to the unit multiple $\rho_nD$ one relative digit further.

If $\nu\ge t$, put


$$
\mathfrak b_t=\mathfrak b/29^t\in\mathbb Z_{29}.
$$


Then alignment is equivalent to


$$
\boxed{v_0\in\mathfrak b_t\mathbb Z_{29},}
$$


and


$$
\boxed{
\mathfrak a\frac{v_0}{\mathfrak b_t}
+29^tu_0-2\rho_n\mathfrak a
\in29\mathbb Z_{29}.
}
\tag{14.3}
$$



These equivalences follow directly by factoring the exact expression for $2(M-\rho_nD)$ in (14.1).

**Audit conclusion:** the original criterion is correct at its original normalization. Reapplying it unchanged after removing second-column content is not correct. Equations (14.2)–(14.3) preserve all norm cancellation and give the content-invariant version.

They remain criteria, not proofs that the actual full-force channels satisfy them.

---

# VI. Remaining bottlenecks, calculations, and global status

## 15. Concrete follow-on lemmas

The next useful obligations are now more specific.

### A1: actual bulk relative-pair theorem

Prove nonvanishing and control the relative valuation of


$$
\delta_0=\det\Psi,\qquad
\delta_1=e^T\operatorname{adj}(\Psi)e
-3^{16}d_{\rm act}\det\Psi.
$$


The at-most-twenty-feature border is exact, but the growing HIGH bulk remains. Another common zero digit would not by itself solve this relative problem.

### A2: complete-force channel divisibility

Evaluate the actual channel $v_0$, using the exact contact inverse and the complete recurrence (10.2)–(10.3), sufficiently to prove or refute (14.2) or (14.3).

The recurrence-source bound (10.4) is not enough without a finite-boundary intertwining argument. In particular, it cannot erase the logarithmic solution’s initial data or the exterior $+1$.

### Degree-$27$ branch

Use (12.3) first. Only if its actual scalar is a unit is it worthwhile to pursue the higher-precision condition


$$
v_{29}(1-29\kappa_h)
\ge k-14675394-R_d
$$


and the remaining vector equations.

---

## 16. Bounded exact arithmetic for personal inspection

No new computation is required for the symbolic proofs above. The following bounded calculation would sharpen the new degree-$27$ consequence.

Define, for $0\le r\le28$,


$$
C_r=[t^r](1+2t+2t^2)^r.
$$


These can be generated modulo $29$ by


$$
C_0=1,\qquad C_1=2,
$$




$$
(r+1)C_{r+1}=2(2r+1)C_r+4rC_{r-1},
\qquad1\le r\le27.
$$



If $n=\sum n_r29^r$, a constant-term Frobenius argument gives


$$
\boxed{J_0\equiv\prod_r C_{n_r}\pmod{29}.}
$$


Indeed, in the lowest digit factor of


$$
(t^{-1}+2+2t)^n,
$$


the exponent range is $[-28,28]$; the only multiple of $29$ in that range is zero. Iterating proves the digit product without a carry omission.

**Inputs:** the 29-entry recurrence above.

**Expected verifiable output:**

1. the complete table $C_0,\ldots,C_{28}\pmod{29}$;
2. its exact zero set;
3. agreement with direct coefficient extraction;
4. the resulting explicit digit test for $J_0\equiv0$.

This finite table, combined with the proved digit-product identity, would classify the first degree-$27$ matching obstruction for any specified original $n$. It would not prove the complete nearest-neighbor identity.

The supplied normal-$29$ certificate already closes its fixed arithmetic constants. The LOW certificate remains a finite modulo-three check, not a modulo-$27$ or moving-family determinant certificate.

---

## 17. Full gcd, primitive denominator, and whole error

For the weighted construction retain


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
$$


The least actual clearer and the full all-prime gcd remain indispensable.

The local denominator interface is still


$$
v_{29}(q_n)
=\max\{0,2F_n-F_b-1+\delta-\mu\},
$$


where


$$
\delta=v_{29}(D),\qquad \mu=v_{29}(M).
$$


The channel factorization retains $\delta-\mu$; it does not evaluate it for the actual full force.

The whole evaluated error remains


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$


The accepted signed-error and endpoint-height results keep their original hypotheses and proof status. The accepted binary high-tail compensation is unchanged and has not been replayed here.

An irrationality argument still requires, on the same infinite sequence of original indices,


$$
0<|q_n(e+\pi)-p_n|\longrightarrow0,
$$


after the actual full primitive normalization.

---

## Final proof-status ledger

| Claim | Audit status |
|---|---|
| Refined complete propagation on $D<H/2916$ | Proved from the exact divided return formula |
| LOW substitution modulo $27$ before division by $3$ | Valid by bounded-degree normalized integrality |
| Actual LOW support and inverse isotropy modulo $27$ | Proved |
| Terminal corrected column modulo $9$ | Verified |
| $\mathcal C_{mm}\in3\mathbb Z_3$, $w\in3\mathbb Z_3^\nu$ | Verified |
| $\mathcal Q\in27M$ | Proved |
| Twenty-feature and bordered-pair signs | Verified |
| Actual determinant-pair nonvanishing and relative valuation | Open |
| Complete factorial recurrence | Verified |
| Explicit logarithmic recurrence source | Newly derived |
| Integral-valued and degree-$\le26$ nearest-neighbor impossibility | Verified on stated deep original branches |
| Degree-$27$ coefficient $15\lambda$ | Verified |
| Actual terminal combination $2\theta_{b-26}-\theta_{b-25}\equiv-J_0$ | Newly proved |
| Unit-only channel transformation | Verified |
| Content-corrected channel equivalence | Newly derived for all permitted content levels |
| Actual all-depth channel divisibility/alignment | Open |
| Full gcd, primitive denominator, and whole-error comparison | Open |

**Conclusion.** This audit validates A1turn8’s nonlinear depth-$16$ advance at its stated scope, explicitly closes the logarithmic recurrence source, and replaces A2turn5’s unevaluated terminal contact combination by an actual first-force scalar. It also supplies the exact channel criterion after arbitrary permitted content removal.

None of these results determines the actual relative determinant pair or proves the saturated full-force alignment. The all-prime primitive denominator and whole nonzero error comparison remain additional unresolved obligations.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


