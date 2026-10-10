> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 18 — Audit of the terminal representer, finite contact transfer, and normalized binary digit evaluation

## Executive assessment

The attached work does **not** prove or disprove the irrationality of $e+\pi$. It does establish useful evaluation mechanisms, provided their arithmetic hypotheses and finite boundaries are retained.

The principal conclusions of this audit are:

1. **A1turn10’s terminal-representer reduction is correct at the accepted original-family scope.** The identities
   

$$
\tau=c^2g,\qquad \gamma=-ck-\tau v
$$


   include the actual LOW return. The normalized evaluation of $K/3$, before the final division by $9$, justifies the two-digit terminal loss. The resulting producer-input budget is $p+9$, subject to the retained producer hypotheses.

2. **The LOW and HIGH convolution orientations in A1 are correct.** They implement different reversal conventions; interchanging those conventions would be an error. Their Neumann sums are finite precision computations on original-length vectors, not bounded-state computations in the original index.

3. **A1’s full residual displacement and endpoint transport are correct without residual invertibility.** In particular,
   

$$
\mathscr D=\mathscr C-e_0\ell^T
$$


   must be accompanied by the complete eliminated-space boundary block $B_{WZ}$. Neither the terminal coefficient vector nor the displacement equation alone is the endpoint cofactor theorem.

4. **A2turn7’s contact factorization, endpoint correction, and projected Gram transfer are valid.** The middle recurrence and endpoint solve have width bounded by $29K-1$, but the binomial transforms retain their original length $b$. The unweighted saturation statement is valid; weighting is not unimodular.

5. **A2’s reduced-force and relative-unit numerator tests are valid equivalences, not established family congruences.** Their precision ledger needs to distinguish division-free numerator evaluation from normalized channel evaluation. The latter requires additional guard digits.

6. **A5turn15 repairs the raw-normalization problem by a genuinely different construction.** Its normalized tail, logarithmic split, finite inverse expansion, and unit-sensitive binomial mechanism are sound. The digit lemma needs an explicit fixed-length padding and flush convention to justify exact counting. These details can be supplied. The resulting mechanism establishes generic finite evaluability, not practical execution or actual norm/mixed alignment.

7. **The coordinator receipt contains two complete auxiliary systems and four original initial-force calculations.** Its singular “one system” scope string is stale. The original calculations do not contain original Gram matrices. The imported central-force routine is not supplied here, so the first-force implementation is not independently reproducible from the displayed file alone.

8. **A new rigorous finite-precision consequence is available:** an initial-force perturbation lemma transfers certified initial-force digits to an actual normalized mixed/norm ratio, with the full actual norm valuation paid. Applied to the reported four original cases, it gives a finite-scope reduction of the mixed contraction to the genuine inhomogeneous boundary column. It does not produce a norm law from zero initial digits.

No tools were used, and no receipt or hash was independently regenerated.

---

## 1. Scope and retained hypotheses

The three original domains remain distinct.

### Ternary residual family

Retain


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$


and


$$
A=n-2=H-D,\qquad H=3^{h-1},\qquad 0<D<H/972,
$$


with


$$
m=\frac{A+1}{2},\qquad d=\frac{3D}{2}-1,\qquad
\nu=\frac D2-1.
$$


The spaces are exactly


$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),\qquad
Y_b=y^b\quad(d\le b\le m),
$$


where $x=y-1$.

The depth-$16$ determinant-pair reduction is used only on its accepted sufficiently large original-index window. The scalar producer theorem has its separately established broader scope; that broader scope does not enlarge the residual theorem.

### $29$-adic family

Retain


$$
a=432827+682892t,\qquad b=3^a,\qquad n=2001b,
$$


and the preferred cylinder


$$
t\equiv364\pmod{841}
$$


where required. Contact coordinates are $0\le i,j<b$, reconstructed coordinates $0\le j\le b$.

### Binary family

Retain


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


The shortened block is exactly


$$
j=128D+\rho,\qquad0\le\rho\le80,
$$


followed by the separate endpoint $j=b=128D+81$.

The scalar, displacement, raw-normalization, and weighted-tail audits accepted in A4turn17 are not reopened here.

---

# Part I. A1turn10: terminal representer and full residual boundary

## 2. The actual terminal representer

Write the actual eliminated block as


$$
E_{\rm act}=
\begin{pmatrix}
3L_{\rm act}&3X_{\rm act}\\
3X_{\rm act}^T&E_{Y,\rm act}
\end{pmatrix},
$$


with


$$
M=L_{\rm act}^{-1},\qquad
H_{\rm inv}
=\bigl(E_{Y,\rm act}-3X_{\rm act}^TMX_{\rm act}\bigr)^{-1}.
$$



At the accepted scope, both displayed normalized inverses are integral. This does **not** say that $E_{\rm act}$ itself is unimodular: its LOW normalization contains the factor $3$.

For the terminal HIGH coordinate $u=e_m$, set


$$
a_\rho=H_{\rm inv}u,\qquad
\rho=Ya_\rho-UMX_{\rm act}a_\rho.
$$


Direct multiplication gives


$$
G_{\rm act}(U,\rho)=0,\qquad
G_{\rm act}(Y,\rho)=u.
$$


Thus this is indeed the actual terminal dual polynomial, including the LOW return.

No residual inverse occurs. No nonvanishing of its terminal coefficient is asserted.

---

## 3. Audit of the $\tau,\gamma$ reduction

Use the accepted mixed-force identities


$$
K(W,\widehat Z^{\,c})=3\binom ab,\qquad
\widetilde b=b-X_{\rm act}^TMa=-cuv^T+3\mathcal B.
$$


Then


$$
K(\widehat Z^{\,c},\rho)=3\widetilde b^TH_{\rm inv}u.
$$



Let


$$
\widehat E_{\rm act}=E_0+3F_{\rm act},\qquad
f=F_{\rm act}e_d.
$$


The accepted endpoint identity $E_0e_d=u$ gives


$$
H_{\rm inv}u=e_d-3H_{\rm inv}f.
$$


With


$$
h_{\rm term}=u^TH_{\rm inv}u=9g,\qquad
w=\mathcal B^Te_d,
$$


one obtains the complete contraction


$$
K(\widehat Z^{\,c},\rho)
=-3c\,h_{\rm term}v+9w-27\mathcal B^TH_{\rm inv}f.
$$


Consequently


$$
k:=\frac{K(\widehat Z^{\,c},\rho)}{27}
=-cgv+\frac w3-\mathcal B^TH_{\rm inv}f.
$$


The accepted facts $h_{\rm term}\in9\mathbb Z_3$ and $w\in3\mathbb Z_3^\nu$ prove $k$ integral.

Moreover,


$$
\mathcal Cu
=\frac{H_{\rm inv}u-e_d}{3}
=-H_{\rm inv}f.
$$


Substitution into the old feature definitions gives


$$
\boxed{\tau=c^2g,\qquad \gamma=-ck-c^2gv=-ck-\tau v.}
$$



This is an exact rearrangement, not a valuation estimate. In particular, the terminal contribution becomes


$$
-c^2g\,vv^T-c(vk^T+kv^T).
$$


The HIGH bulk and its possible cancellations remain present.

---

## 4. Why $K/3$ can be evaluated before the final division by $9$

The complete functional must remain


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
\qquad \mathfrak f(y^r)=(2r)!.
$$



For arbitrary integral $R,f$ within the stated degree bounds,


$$
\deg(Rz_if)\le A+d+m=\frac{3H-1}{2}=r_*.
$$


The endpoint-subtracted quotient therefore has degree at most $r_*-1$. Its contributing odd denominators satisfy


$$
2v+1\le3H-2.
$$


The first denominator with valuation $h$, namely $3H=3^h$, is absent. Every remaining logarithmic coefficient has the required factor $3$; the factorial part also has that factor.

Hence


$$
(R,f)\longmapsto \frac{\mathcal M(Rz_if)}3
$$


is an integral bilinear map on the whole bounded-degree input space—not merely on the actual evaluated solution.

The normalized LOW assertion follows by the same degree argument, with


$$
\deg(RU_uf)\le A+D+m\le A+d+m.
$$



This uniform integrality is what makes reduction of inputs modulo $3^P$ safe. Divisibility proved only for one final evaluated value would not suffice for that purpose.

Now let


$$
C_c=G_c(W,Z)=3C_1,\qquad
s=E_c^{-1}K(W,\rho).
$$


The normalized LOW solve makes $s$ integral. Therefore


$$
\boxed{
k=\frac19\left(\frac{K(Z,\rho)}3-C_1^Ts\right).
}
$$


All maps inside parentheses are integral before the final division. The whole numerator is in $9\mathbb Z_3^\nu$, by the terminal identity already proved.

**Verdict:** the advertised two-digit loss is justified.

---

## 5. LOW and HIGH convolution orientations

### 5.1 LOW

Put $a=r_1+1$. The reference matrix $L_*$ has


$$
L_*J_D
$$


upper triangular Toeplitz with coefficients of $(1+z)^{-a}$. Thus


$$
L_*^{-1}=J_D(L_*J_D)^{-1}.
$$


For a column $b$,


$$
(L_*^{-1}b)_i
=\sum_{j=0}^{i}\binom a{i-j}b_{D-1-j}.
$$


Equivalently,


$$
\boxed{
(L_*^{-1}b)_i
=[z^i](1+z)^a\sum_{j=0}^{D-1}b_{D-1-j}z^j.
}
$$


This confirms A1’s formula: **reverse the input, then take ordinary increasing output coefficients.**

### 5.2 HIGH

The accepted HIGH formula is


$$
\boxed{
(R_Hb)_i
=[z^{L_H-1-i}](1-z)^{-A}
\sum_{j=0}^{L_H-1}b_jz^j.
}
$$


Here the input is not reversed; the extracted coefficient index decreases with $i$. It gives


$$
R_Hu=e_d
$$


and, when the HIGH interval has more than one coordinate,


$$
u^TR_Hu=0.
$$



These two convolution orientations must not be interchanged.

### 5.3 Finite stopping and precision

If


$$
\Delta_L=L_{\rm act}-L_*\in3M,
$$


then


$$
\sum_{j=0}^{P-1}(-L_*^{-1}\Delta_L)^jL_*^{-1}
$$


is the actual LOW inverse modulo $3^P$. The analogous HIGH sum uses


$$
\Delta_H=\widehat E_{\rm act}-E_0\in3M.
$$


Each omitted term has at least $P$ factors of $3$.

With $P=p+2$, the two final divisions by $9$ produce $g,k\bmod3^p$. Thus the terminal computation needs


$$
R\bmod3^{p+2}.
$$


The accepted producer budget then gives


$$
\boxed{\text{producer input precision }3^{p+9}.}
$$



This remains subject to the actual producer-jet and endpoint hypotheses, including the stated factorial-tail condition when that representation is used. It is not an arbitrary-order extension of the core approximation.

The computation retains original-length LOW and HIGH vectors. A bounded number of right-hand sides is not a bounded dimension in $n$.

---

## 6. Full residual displacement and the complete endpoint block

The truncated multiplication is


$$
\mathscr Tf=yf-t(f)y^{m+1},\qquad t(f)=[y^m]f.
$$


The endpoint-subtracted functional


$$
\mathfrak r(f)=
\mathcal M\!\left(
Q_n^{\rm loc}y^{m+1}(f-t(f)y^m)
\right)
$$


avoids introducing an exterior moment. Expansion gives


$$
G_{\rm act}(f,\mathscr Tg)-G_{\rm act}(\mathscr Tf,g)
=t(f)\mathfrak r(g)-\mathfrak r(f)t(g).
$$



The original multiplication blocks satisfy:

* the residual block on $Z$ is $\mathscr C$;
* multiplication of LOW columns creates a residual component only through
  

$$
yU_{D-1}=U_{D-1}+z_0;
$$


* truncated multiplication of HIGH columns creates no residual coordinate.

For


$$
K_{\rm elim}=E_{\rm act}^{-1}C_{\rm act},
\qquad
\widehat Z^{\,\rm act}=Z-WK_{\rm elim},
$$


this gives exactly


$$
\boxed{\mathscr D=\mathscr C-e_0\ell^T,\qquad
\ell^T=e_{U_{D-1}}^TK_{\rm elim}.}
$$



Orthogonality to $W$, not invertibility of the residual form, then proves


$$
\boxed{
S_{\rm act}\mathscr D-\mathscr D^TS_{\rm act}
=t_{\rm act}r_{\rm act}^T-r_{\rm act}t_{\rm act}^T.
}
$$


The correction to the terminal generator is also exact:


$$
\boxed{t_{\rm act}=t_c-3^9k.}
$$



For the endpoint, the block transformation gives


$$
B_{WZ}
=T_{WZ}-T_{WW}K_{\rm elim}+K_{\rm elim}\mathscr D.
$$


Since


$$
(\mathscr Tf)(-1)=-f(-1)-(-1)^{m+1}t(f),
$$


the full endpoint identity is


$$
\boxed{
\mathscr D^Te_{\rm act}+B_{WZ}^TW(-1)
=-e_{\rm act}-(-1)^{m+1}t_{\rm act}.
}
$$



**Audit conclusion:** the signs and boundary correction are correct. Omitting $B_{WZ}$ would create an unjustified endpoint recurrence.

---

## 7. A concrete radical alternative for the residual pair

The displacement identity does not establish nonvanishing. A useful follow-on lemma should address the singular case explicitly.

For


$$
\delta_0=\det\Psi,\qquad
\delta_1=e_{\rm act}^T\operatorname{adj}(\Psi)e_{\rm act}
-3^{16}d_{\rm act}\det\Psi,
$$


ordinary adjugate algebra gives the following exhaustive singular alternatives over $\mathbb Q_3$:

* If $\operatorname{rank}\Psi\le\nu-2$, then
  

$$
\delta_0=\delta_1=0.
$$


* If $\operatorname{rank}\Psi=\nu-1$, and $z\ne0$ spans its radical, then symmetry gives
  

$$
\operatorname{adj}(\Psi)=\kappa zz^T,\qquad\kappa\ne0,
$$


  and hence
  

$$
\boxed{\delta_1=\kappa(e_{\rm act}^Tz)^2.}
$$



Thus a singular-case theorem must determine the **actual endpoint pairing with the radical**, not merely the radical dimension.

The displacement identity further gives, for $z\in\ker\Psi$,


$$
-3^{16}\Psi\mathscr Dz
=t_{\rm act}(r_{\rm act}^Tz)-r_{\rm act}(t_{\rm act}^Tz).
$$


It does not automatically make the radical $\mathscr D$-invariant.

A concrete outstanding lemma is therefore:

> Determine the radical of the actual original $\Psi$, or prove it trivial; in the corank-one case determine $e_{\rm act}^Tz$, using the complete endpoint transport including $B_{WZ}$.

This is a sharper obligation than assuming residual invertibility.

---

# Part II. A2turn7: finite contact transfer and reduced force

## 8. Factorization and all tail indices

Set


$$
m=\min(2n,29K-1),\qquad t_0=\min(m,b).
$$


Uniform falling-factorial divisibility justifies truncation of the **matrix entries** at $s=m$.

After the finite Pascal transform,


$$
(\mathsf P^{-1}\widetilde N)_{ij}
\equiv
\sum_{s=0}^{m}
a_s(n)\frac{(j+s)!}{j!}\binom n{j+s-i}
\pmod{29^K}.
$$



The interior terms have $j+s<b$. Every crossing term has


$$
j+s=b+r,\qquad0\le r<m.
$$


Thus the stated tail range is complete, including when $m>b$. The lower condition $s\ge1$ excludes a nonexistent $s=0$ crossing.

Only the last $t_0$ original contact columns can occur. The finite convolution identity gives


$$
F_{jr}
=-\sum_{u=0}^{r}
\binom{-n}{b+u-j}\binom n{r-u}.
$$


The minus sign comes from moving the omitted range
$\ell=b,\ldots,b+r$ to the other side of the full zero convolution.

Consequently


$$
\boxed{
A\equiv\mathsf P\,T(H+LE)T\pmod{29^K}.
}
$$


This is a congruence at the requested precision, not generally an exact rational factorization after truncation.

---

## 9. Unit endpoint matrix

For $1\le s<29$, the coefficients $a_s(n)$ vanish modulo $29$, since $29\mid n$. For $s\ge29$, the factorial quotient supplies a factor $29$. Therefore


$$
H\equiv I,\qquad K^{\rm tail}\equiv0,\qquad L\equiv0\pmod{29}.
$$


The lower triangular matrix $H$ has diagonal exactly $1$, and


$$
\Gamma=H^{-1}L\equiv0\pmod{29}.
$$


Hence


$$
S_{\rm end}=I+E\Gamma\equiv I\pmod{29}.
$$



Its inverse modulo $29^K$ is the stated $K$-term geometric sum. No primitive-norm factor or unidentified contact minor is divided out.

The reconstruction


$$
y=v-\Gamma S_{\rm end}^{-1}Ev
$$


is valid over the finite residue ring: multiplication directly verifies


$$
(H+LE)y=g.
$$



---

## 10. Bounded width is not original-length compression

The following parts are bounded in terms of $K$:

* recurrence order at most $29K-1$;
* endpoint dimension at most $29K-1$;
* number of geometric terms $K$.

The transforms


$$
\beta_j=\sum_{i=0}^{j}(-1)^{j-i}\binom ji h_i,
$$




$$
g_j=\sum_{k=j}^{b-1}\binom{-n}{k-j}\beta_k,
$$


and the final transform of the same upper-triangular type still range over the original interval.

Thus “no $b\times b$ inverse remains” is valid as an evaluation formula. It is not a proof of $b$-independent runtime, storage, or streaming state.

---

## 11. Projected Gram charge and unweighted saturation

The reconstruction is


$$
\mathbf B_j
=W_j\bigl(j\zeta_{j-1}-\zeta_j+\mathbf1_{j=b}e_*^T\bigr).
$$


At the actual endpoint,


$$
\mathbf B_b=W_b(b\zeta_{b-1}+e_*^T).
$$


The exterior $+1$ is retained.

Since


$$
\ell_jW_j=\frac{\omega_b}{j!},
$$


the charge of the $C$-part telescopes over the complete interval $0\le j\le b$. Therefore


$$
\ell^TB_0=\ell^TB_1=0,\qquad\ell^TB_*=W_b.
$$


It follows exactly that


$$
\boxed{
G=G^{\rm raw}-\frac{W_b^2}{\mathscr S}e_*e_*^T.
}
$$


Only the $(*,*)$ entry changes. The demonstrated unit $\mathscr S$ is sufficient for this projection.

The saturation proof is also valid:


$$
[C,e_b]\in\mathrm{GL}_{b+1}(\mathbb Z_{29}),
$$


and the recurrence uses unit leading coefficients and precisely two initial values. This proves an integral basis of the unweighted kernel.

It does not prove that the weighted image is saturated. The actual $W_j$, actual coefficient vectors, and any resulting weighted content must remain.

---

## 12. Reduced-force numerator criteria

The complete residual vector is


$$
U=Y^\parallel-\alpha Z_w
=\Delta B_1+\widehat B_*,
$$


where


$$
\alpha=\frac{r_0}{f_0^0},\qquad
\Delta=r_1-\frac{f_1^0}{f_0^0}r_0.
$$


The logarithmic force remains in $r_0,r_1$.

With


$$
\chi=Z_w^TU=\Delta H_1+H_*,
\qquad
P=29^cx,\qquad x^Tx=\mathfrak a\mathfrak b,
$$


the channel identity gives


$$
\mathcal E_{\rm force}
=\frac{2\chi}{29^{c+2}\mathfrak a}
-\frac{\mathfrak b}{\mathfrak a}s_U.
$$


Because


$$
U\in29^3\mathbb Z_{29}^{b+1},
$$


the second term is already in $29^3\mathfrak b\mathbb Z_{29}$. Hence


$$
\boxed{
\mathcal E_{\rm force}\in29^3\mathfrak b\mathbb Z_{29}
\iff
\chi\in29^{c+5}\mathfrak b\mathbb Z_{29}.
}
$$



The norm


$$
\mathcal N=f^TGf=29^{2c+4}\mathfrak a\mathfrak b
$$


and complete mixed contraction satisfy


$$
\chi+\mathcal N(\alpha-29\rho_n)
=29^5(M-\rho_nD).
$$


Thus the second numerator criterion


$$
\boxed{
\chi+\mathcal N(\alpha-29\rho_n)
\in29^2\mathcal N\mathbb Z_{29}
}
$$


is equivalent to


$$
M-\rho_nD\in29D\mathbb Z_{29}.
$$



These derivations are sound. They do not establish that the actual family satisfies either criterion.

### A useful simplification

Under the retained $c\ge0$, $\alpha\in29\mathbb Z_{29}$, and $\rho_n\in\mathbb Z_{29}$, the second numerator congruence itself implies the first:


$$
v_{29}(\chi)\ge2c+5+v_{29}(\mathfrak b)
\ge c+5+v_{29}(\mathfrak b).
$$


If $\rho_n$ is a unit, it also implies


$$
v_{29}(M)=v_{29}(D).
$$



This is a rigorous conditional simplification of the outstanding lemma, not an actual-family proof of its hypothesis.

---

## 13. Complete guard-digit ledger

Let


$$
\nu=v_{29}(\mathfrak b),\qquad
v_{29}(\mathcal N)=2c+4+\nu.
$$



### Division-free tests

To test the two stated congruences it suffices to know integral Gram data and integral initial inputs modulo


$$
\boxed{29^K,\qquad K=2c+6+\nu.}
$$


This contains:

* the norm-factor threshold $c+5+\nu$;
* the relative-unit threshold $2c+6+\nu$;
* a nonzero norm digit needed to identify $\nu$, once $c$ is known.

The content $c$ must itself be certified from actual nonzero coordinate digits of $Z_w/29^2$, not inferred from a common zero precision.

### Quotient evaluations

The same $K$ does **not** automatically deliver every normalized channel modulo $29^K$.

For a desired output precision $29^s$:

| Quantity formed by division | Sufficient precision of its numerator |
|---|---:|
| $H_i/29^{c+2}$ | $s+c+2$ |
| $s_U/29^3$ | $s+3$ |
| $\chi/(29^{c+5}\mathfrak b)$ | $s+c+5+\nu$ |
| A numerator divided by $\mathcal N$ | $s+2c+4+\nu$ |

Odd-unit inversions lose no digits.

Finally, if the complete $r_i$ are computed from a raw numerator followed by division by $b!$, obtaining them modulo $29^K$ requires raw precision at least


$$
K+v_{29}(b!).
$$


A separately proved normalized force formula may avoid that raw computation. The matrix-entry truncation at $s<29K$ does not, by itself, justify truncating a raw force before a nonunit division.

---

# Part III. A5turn15: normalized force and unit-sensitive digit transfer

## 14. Normalized force tail and logarithmic split

The accepted symbol filtration gives


$$
v_2(\lambda_s^{(a)})\ge a,\qquad s\le4a.
$$


Since


$$
\frac{(b+t)!}{b!}=t!\binom{b+t}{t},
$$


each normalized exponential summand has depth at least


$$
a+v_2(t!).
$$


Therefore the retained domain


$$
a+v_2(t!)<M
$$


is valid, and the rough bounds


$$
a<M,\qquad t<2M,\qquad s<4M
$$


are sufficient.

The high lower index $b+t$ remains. This is not a bounded Newton-degree assertion.

The normalized logarithmic budget is correctly


$$
K_{\rm norm}
=1+v_2((n/2)!)-v_2(b!)
-\lfloor\log_2(2n+b-1)\rfloor.
$$


For $n=4002b$,


$$
K_{\rm norm}
=1+2000b-s_2(2001b)+s_2(b)
-\lfloor\log_2(8005b-1)\rfloor.
$$


Using $s_2(N)\le\lfloor\log_2N\rfloor+1$,


$$
K_{\rm norm}\ge
2000b-\lfloor\log_2(2001b)\rfloor
-\lfloor\log_2(8005b-1)\rfloor.
$$


For $b\ge16$, the two logarithms are bounded by $25+2\log_2b$, which is far below $1999b$. Hence


$$
\boxed{K_{\rm norm}\ge b}
$$


throughout the original family.

Thus


$$
M>K_{\rm norm}\implies b<M,\qquad n<4002M.
$$


In that branch a complete direct finite calculation is indeed size-controlled by $M$. In the other branch logarithmic omission is justified by its complete normalized valuation bound.

---

## 15. Finite inverse and word expansion

The factorization


$$
\mathsf P=\mathsf L U
$$


is the finite Vandermonde identity, with


$$
\mathsf L_{it}=\binom it,\qquad U_{tr}=\binom n{r-t}.
$$


Its inverses are integral. Since


$$
\widetilde N=\mathsf P+\mathsf E,\qquad \mathsf E\in2M_b(\mathbb Z_2),
$$


one has


$$
\boxed{
\mathsf A^{-1}\equiv
U^{-1}\sum_{k=0}^{M-1}(-\mathsf P^{-1}\mathsf E)^k\mathsf P^{-1}
\pmod{2^M}.
}
$$



The finite entry formula


$$
(\mathsf P^{-1})_{ri}
=\sum_{t=\max(r,i)}^{b-1}
\binom{-n}{t-r}(-1)^{t-i}\binom ti
$$


has the correct orientation and endpoint. Expanding a matrix word introduces only $O(M)$ contact-index variables per word.

The conversion


$$
\binom{-n}{d}=(-1)^d\binom{n+d-1}{d}
$$


is exact. Both this sign and the inverse-Pascal sign must be retained.

The use of the accepted central-force filtration is a dependency of the first-column application. A proof of that filtration is not reproduced in A5turn15, and the displayed coordinator file imports its evaluator from an omitted module.

---

## 16. Completing the digit-transfer lemma

The odd-unit part is correct. Define


$$
O_M(N)=\prod_{\substack{1\le j\le N\\j\text{ odd}}}j\pmod{2^M}.
$$


Its period divides $2^{M+1}$: over an interval of that length each odd residue modulo $2^M$ occurs twice, and the squared product of all units is $1$.

The odd factorial part satisfies


$$
F_M(N)=\prod_{\ell\ge0}O_M(\lfloor N/2^\ell\rfloor),
$$


so it can be evaluated from windows of $M+1$ binary digits. Kummer carries supply the valuation. Consequently


$$
\binom LK
\equiv
2^{v_2\binom LK}F_M(L)F_M(K)^{-1}F_M(L-K)^{-1}
\pmod{2^M},
$$


with only odd-unit inversions.

The missing operational details can be supplied as follows.

### 16.1 Exact finite length

For each expanded word, choose one common bit length $L$ large enough for all valid summation variables. In the application, variables are bounded by $b$ plus precision-sized constants, so such a bound follows explicitly from the bit lengths of the actual input parameters.

Every variable is represented by exactly $L$ digits, including leading zero padding. Do not sum over several possible stopping lengths.

### 16.2 Affine constraints

Use bounded carry or borrow registers for affine expressions. If inequalities are encoded using slack variables, use


$$
\text{slack}=\text{specified affine difference}
$$


with a nonnegative slack and a proven sufficient bit length. The slack is then unique for a valid tuple, so it introduces no multiplicity.

Negative-upper-binomial conversions are performed first, and branches violating


$$
0\le K\le L
$$


are rejected rather than evaluated using an unintended generalized binomial.

### 16.3 Flush convention

After the $L$ free variable-digit positions:

1. force all subsequent variable digits to zero;
2. feed enough deterministic zero positions to resolve affine carries;
3. feed at least $M$ additional zeros to complete every $M+1$-digit odd-factorial window;
4. accept only states satisfying the terminal carry and inequality conditions.

These flush positions contain no new branching choices.

Each valid integer tuple is therefore counted exactly once. Windows beginning above the last nonzero digit contribute $O_M(0)=1$.

### 16.4 Signs and polynomial factors

Affine signs use parity registers. Polynomial factors use variable residues modulo $2^M$. The signs from both negative binomials and finite inverse Pascal factors are included independently.

### 16.5 State bound

For the displayed matrix-word application:

* the number of variables and binomial factors is polynomial in $M$;
* each factorial window stores $O(M)$ bits;
* unit products, clipped valuations, and variable residues require polynomially many further bits;
* affine carry sizes have logarithmic dependence on the precision-sized coefficients.

Thus a deliberately loose bound


$$
2^{\operatorname{poly}(M)}
$$


for the weighted transfer is justified, provided the first-force expansion has the stated accepted precision-sized description.

This is an existence bound for a potentially enormous transfer, not evidence that it has been built or run.

A separate caution concerns content search: nonzero output at a coordinate is a property **after summing all branches for that coordinate**. Marking a coordinate because one summand is nonzero would ignore cancellation. Any Boolean content-search implementation must first preserve the aggregated residue, or use an appropriately determinized residue-state construction. The Gram-evaluation lemma itself does not have this defect.

---

## 17. What the digit theorem establishes—and what it does not

The mechanism evaluates


$$
\mathsf a^T\mathsf a,\qquad
\mathsf a^T\mathsf b,\qquad
\mathsf b^T\mathsf b\pmod{2^M},
$$


where


$$
\mathsf a=2X,\qquad
\mathsf b=4Y=\mathcal R\mathsf A^{-1}r+W_be_b.
$$


The endpoint contributes the separate terms


$$
W_b\mathsf a_b,\qquad
2W_b(\mathcal R\psi)_b,\qquad W_b^2.
$$


The shortened final block is not completed artificially.

The output normalization still costs


$$
\mathsf a^T\mathsf a=4N,\qquad
\mathsf a^T\mathsf b=8H.
$$


Hence $N\bmod2^s$ requires $s+2$ Gram digits and $H\bmod2^s$ requires $s+3$.

Nothing here controls


$$
v_2(H)-v_2(N)
$$


uniformly. Finite evaluability and actual alignment are different claims.

---

# Part IV. Coordinator certificate and a new relative consequence

## 18. Scope of the displayed certificate

The code and receipt describe:

* two complete auxiliary systems:
  

$$
(b,n)=(81,324162),\qquad(209,836418);
$$


* four original cases $u=0,1,2,3$, but only their two normalized initial-force entries for each column.

The scope string saying “One complete normalized auxiliary finite contact system” should be corrected to **two**.

### What the code verifies structurally

The displayed code:

* retains the normalized factorial tail before inversion;
* truncates the symbol at orders $a<13$;
* retains $t=0,\ldots,25$, with
  

$$
v_2(26!)=23\ge13;
$$


* checks that the whole normalized logarithmic depth exceeds $13$;
* solves both normalized contact columns with odd pivots;
* reconstructs all $b+1$ coordinates, including the exterior $+1$.

Its odd-factorial implementation is consistent with separating odd and even factorial factors.

The loop count $2585$ is also consistent with the stated small-binomial test ranges. Those tests are not an exhaustive test of high lower indices.

### What is not independently verified here

The code imports `central` and `L` from another module. The intended $L$ is the factorial valuation, but that imported implementation and the central-force evaluator are not displayed. I therefore regard the reported first-force residues as supplied finite evidence, not independently regenerated results.

The full auxiliary coordinate arrays are also omitted from the receipt. The source explains how they are produced, but the short receipt alone does not permit checking every displayed summary contraction.

### Finite consequences of the reported nonzero digits

If the supplied receipt is accepted, the two auxiliary systems have:



$$
\begin{array}{c|cc|c}
b&v_2(N)&v_2(H)&v_2(H)-v_2(N)\\ \hline
81&1&1&0\\
209&4&4&0
\end{array}
$$


because $1062,486$ have valuation $1$, and $560,304$ have valuation $4$.

These are genuine finite relative observations, but neither input is an original exponential-family index.

The four original entries


$$
r_0\equiv r_1\equiv0\pmod{2^{13}}
$$


do not say that the complete force vector is zero. Its inhomogeneous recurrence has source $\mathcal Ve_b$.

---

## 19. New result: endpoint-preserving initial-force protection

This result is distinct from the previously accepted logarithmic-protection bound.

### Proposition

Work in the actual binary system. Let


$$
B_0=\mathcal R\mathsf A^{-1}h^{(0)},\qquad
B_1=\mathcal R\mathsf A^{-1}h^{(1)},\qquad
B_*=\mathcal R\mathsf A^{-1}\tau+W_be_b,
$$


using the complete recurrence and original endpoint.

Then


$$
\mathsf b=r_0B_0+r_1B_1+B_*.
$$


Choose integral approximations $\widetilde r_0,\widetilde r_1$ such that


$$
r_i-\widetilde r_i\in2^T\mathbb Z_2,
$$


and define


$$
\widetilde{\mathsf b}
=\widetilde r_0B_0+\widetilde r_1B_1+B_*.
$$



Let


$$
a_0=\min_jv_2(\mathsf a_j),\qquad
d_0=v_2(\mathsf a^T\mathsf a).
$$


Then


$$
\boxed{
v_2\!\left(
\frac HN-
\frac{\mathsf a^T\widetilde{\mathsf b}}
     {2\,\mathsf a^T\mathsf a}
\right)
\ge T+a_0-d_0-1.
}
$$



### Proof

The actual contact inverse and reconstruction are integral, so $B_0,B_1$ are integral. Therefore


$$
\mathsf b-\widetilde{\mathsf b}\in2^T\mathbb Z_2^{b+1}.
$$


Consequently


$$
v_2\bigl(\mathsf a^T(\mathsf b-\widetilde{\mathsf b})\bigr)
\ge T+a_0.
$$


Since


$$
\frac HN=\frac{\mathsf a^T\mathsf b}
{2\,\mathsf a^T\mathsf a},
$$


division by the nonzero actual norm gives the result. ∎

### Application to the four reported original initial pairs

At each of the four reported original inputs, set


$$
T=13,\qquad\widetilde r_0=\widetilde r_1=0.
$$


The receipt then supports, at exactly those four inputs,


$$
\mathsf b\equiv B_*\pmod{2^{13}},
$$


and the proposition gives


$$
\boxed{
v_2\!\left(
\frac HN-\frac{\mathsf a^TB_*}{2\,\mathsf a^T\mathsf a}
\right)
\ge12+a_0-d_0.
}
$$



This is an actual endpoint-sensitive relative reduction, conditional on the reported initial residues. It retains the inhomogeneous boundary column $B_*$, including $W_be_b$.

It does **not** imply useful relative precision until the actual $a_0,d_0$ are certified. Nor does it imply $H=0$, alignment, or a norm factor.

A sufficient threshold for a ratio congruence modulo $2^s$ is


$$
\boxed{T\ge s+d_0+1-a_0.}
$$


The full primitive-norm cancellation is present in $d_0$.

---

# Part V. Remaining bottlenecks, bounded checks, and final arithmetic

## 20. Concrete next mathematical obligations

### A1: actual residual pair

Prove either:

* nonvanishing and a relative valuation theorem for the actual pair $(\delta_0,\delta_1)$; or
* a radical theorem that determines the pair, including the actual endpoint pairing in the corank-one case.

The complete $B_{WZ}$ relation must remain.

### A2: endpoint-sensitive Gram congruence

Prove, on the original preferred cylinder,


$$
\chi+\mathcal N(\alpha-29\rho_n)
\in29^2\mathcal N\mathbb Z_{29},
$$


with the complete initial force and actual primitive norm. Under the retained integrality hypotheses, this also supplies the norm-factor divisibility.

An absolute-precision transfer does not establish a congruence whose required precision depends on the first nonzero norm digit.

### A5: original-family transfer invariant

Construct and prove an invariant of the actual norm and mixed output channels under the original parameter progression


$$
b\longmapsto9^{32}b.
$$


It must survive arbitrary additional parameter digits and preserve the actual primitive-norm factor.

The generic digit-transfer construction does not itself provide such an invariant.

The classical structured-matrix and prime-power digit methods are appropriate reusable background. The scoped literature search does not establish exhaustive novelty, and no unchecked Hankel/Bezoutian theorem is needed for the conclusions above.

---

## 21. Bounded exact arithmetic proposed for personal inspection

No computation below is represented as executed.

### Check A: A1 convolution and boundary implementation

Use the proposed auxiliary data


$$
H=81,\quad h=5,\quad D=6,\quad A=75,\quad n=77,
\quad m=38,\quad d=8,\quad\nu=2,
$$


with the supplied synthetic $R_{\rm test}$, at modulus $3^8$.

Expected verifiable output:

1. direct agreement of the LOW reference inverse with the reversed-input convolution;
2. direct agreement of the HIGH reference inverse with the decreasing-coefficient extraction;
3. actual unit-pivot checks before using each modular block inverse;
4. zero terminal-duality residual;
5. zero full displacement residual;
6. zero endpoint residual including $B_{WZ}$.

Because this is outside the original window, original-family divisibilities must be tested, not presumed.

### Check B: A2 transfer with complete force

Use


$$
p=29,\qquad n=29,\qquad b=4,\qquad K=2.
$$


Expected output:

* zero matrix for the contact factorization residual;
* zero residual for each of the three reconstructed contact solutions;
* zero difference between direct and transferred projected Gram matrices;
* the stated common reduction
  

$$
G\equiv
  \begin{pmatrix}
  21&19&0\\
  19&5&0\\
  0&0&0
  \end{pmatrix}\pmod{29};
$$


* exact agreement for the complete-force reconstruction, including logarithmic initial terms and the exterior $+1$.

This tests formulas, not the original norm factor.

### Check C: binary unit transfer and fixed-length counting

For


$$
M=1,\ldots,5,\qquad0\le K\le L\le127,
$$


compare direct binomials against carry-plus-odd-unit evaluation.

Additionally test a small affine-bounded sum using two different sufficient padding lengths. The output must be identical, and the terminal flush must introduce no new branches.

Expected output: zero discrepancies, including high lower indices and all sign conversions.

### Check D: the new initial-force relative lemma

Using the two supplied auxiliary systems, retain their complete normalized data and construct $B_*$ from the actual recurrence. Report:

* $r_0,r_1$ to the working precision;
* actual $a_0,d_0$;
* the whole contraction difference
  

$$
\mathsf a^T\mathsf b-\mathsf a^TB_*;
$$


* verification of the bound when the initial residues permit it.

For the four original initial cases, a bounded extension to a declared precision such as $2^{16}$ can check only their initial-force digits unless the full digit-transfer contraction is separately implemented. No original Gram conclusion should be attached to that extension.

---

## 22. Least clearers, full gcds, and whole same-index errors

For the Gram constructions, retain the least actual two-column clearer $d_B$, the actual integer pair


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$


and


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
}
$$


The primitive multiplier remains $d_B^2/g_B$. Every prime is included.

For A1, retain the least original rational-matrix clearer $\ell$, not a convenient larger substitute, and


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


When $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


with whole error


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_\ell)\ell^{k_0}}{g_\ell}
\det H_{\rm complete}.
}
$$



For the Gram routes, the whole error is


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$


Under the retained signed-error results it is eventually positive in the binary family and negative in the $29$-adic family. Its sign and magnitude refer to the complete evaluated error, not to an isolated force component.

No result in this audit bounds the full primitive denominator sufficiently to make that whole nonzero same-index expression tend to zero.

---

## Final proof-status summary

| Claim | Status |
|---|---|
| Actual A1 terminal dual with full LOW return | Valid |
| $\tau=c^2g,\ \gamma=-ck-\tau v$ | Valid exact reduction |
| Integral $K/3$ before final division by $9$ | Valid on the complete stated degree spaces |
| Two-digit terminal loss; producer $p+9$ budget | Valid with retained producer hypotheses |
| LOW/HIGH convolution orientations | Correct |
| Whole residual displacement and $B_{WZ}$ endpoint relation | Correct without residual invertibility |
| Actual residual pair nonvanishing/relative law | Open |
| A2 finite contact factorization and all tail indices | Valid |
| Unit endpoint solve and projected charge correction | Valid |
| Unweighted saturation | Valid; weighted saturation does not follow |
| Reduced-force and unit numerator criteria | Valid equivalences |
| Actual original-family Gram congruence | Open |
| A5 normalized force and logarithmic split | Valid |
| Finite inverse word expansion | Valid |
| Unit-sensitive digit transfer | Valid with explicit fixed-length and flush conventions |
| Practical execution of the full transfer | Not demonstrated |
| Original norm/mixed alignment | Open |
| Two auxiliary normalized systems | Supplied finite evidence |
| Four original initial-force pairs | Supplied finite initial-data evidence only |
| Initial-force relative-protection proposition | Proved here |
| Full all-prime denominator/whole-error comparison | Open |

## Conclusion

The main new proved result is the **endpoint-preserving initial-force relative-protection proposition**, together with the explicit completion of the binary digit-transfer counting and flush argument. The audit also confirms A1’s two-digit terminal evaluation and A2’s endpoint-exact finite contact transfer, while exposing the guard digits and scope limits needed for their use.

The exact remaining obstruction is not finite evaluability. It is an actual-family **relative theorem**: nonvanishing and relative cofactor valuation for A1, or a norm-sensitive mixed-contraction congruence for A2/A5, followed by control of the least clearer, full gcd, actual primitive denominator, and whole nonzero same-index error.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


