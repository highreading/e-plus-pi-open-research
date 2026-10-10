> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Audit of the first-wrap mixed rank theorem and a paid near-half-size descent

## 1. Conclusions and scope

The rationality or irrationality of $e+\pi$ remains unresolved.

The first-wrap candidate **passes**, with one useful repair to its presentation: the final $T=0$ argument should explicitly cover the last even small-pole pair rather than refer beyond the stated $h\le \rho-1$ scope of the supplied turn-15 theorem. Below, an exact description of the **actual binary source space** supplies that missing verification and also checks the odd critical row.

The conclusions are as follows.

1. **The two parent first-wrap interfaces pass.**  
   The common mixed wrap is $1+Y^{2L}$, not $1$. The complete finite null criterion is
   

$$
E=Y^{2L}T,\qquad T=P_m\pmod{Y^\rho},
$$


   on all original columns $0\le r<d$. The source-root representation, the bound
   $\deg T\le 2\delta-1$, and the Frobenius reduction modulo the actual $a$-root power are correct.

2. **The new binary-phase argument passes under its exact hypotheses.**  
   Every complete mixed numerator has the stated common phase. When
   

$$
L\equiv2\pmod3,\qquad
   1\le\delta\le\rho/2,\qquad
   \delta\le L-\rho-p,
$$


   the necessary root congruence forces the **whole actual tail $T$** to be zero. It does not replace the low-trace condition by a freely chosen polynomial.

3. **The full coupled rank and cofactor transfer pass.**  
   This is independence of the entire $q$-row stack, not separate source and mixed ranks. Both strict and equality sectors are retained, including their relative odd units and the complete Pascal tie sum.

4. **The narrower original rotation interval reaches**
   

$$
q_{\rm half}=d/2-m_d-1.
$$


   This holds on infinitely many of the same original indices
   $k=9^{18+32u}$, with no assumption about equality-tie frequency and no claim at $q=d/2$.

5. **A further paid result is proved here.**  
   An attaining near-half-size cofactor gives an exact, linearly sized $2$-primary Cramer denominator:
   

$$
L_d+\lambda_{q-1}
   =2d+2q-s_2(d)-s_2(q-1)-14.
$$


   At $q=q_{\rm half}$, this is
   

$$
3d-2m_d-s_2(d)-s_2(q-1)-16.
$$


   The proof constructs a one-shot descent over $\mathbb Z_{(2)}$, pays an additional common-column divisor, retains both literal coefficient borders, and gives an exact all-prime content identity. It does **not** assume the disproved integral $W$-descent.

The remaining terminal arithmetic is still substantial. The new cofactor window does not bound the unextracted invariant factors or the cancellation between the two complete terminal coefficient forms.

No tools or new finite computations are used.

---

## 2. Original objects and unchanged arithmetic normalization

### 2.1 Domain, sequences, and physical terminal

Throughout,


$$
\boxed{k=9^{18+32u},\quad u\ge0,\qquad d=k-1.}
$$


In particular,


$$
v_2(d)=4,\qquad d\equiv2\pmod3,\qquad d\equiv208\pmod{256}.
$$



Retain


$$
a_0=1,\qquad a_n=1-na_{n-1},
$$




$$
u_n=a_{2n},\qquad f_n=(2n)!,\qquad
w_n=(-1)^n,\qquad c_n=u_n-w_n,
$$


and


$$
\rho_0=0,\qquad \rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad r_n=-f_n+4\rho_n.
$$


The dyadic remainder denoted by $\rho$ below is distinct from this sequence $\rho_n$.

The complete returns remain


$$
\sigma_n=u_{n+1}+u_n=c_{n+1}+c_n
$$


and


$$
\boxed{\tau_n=-(2n+2)!-(2n)!+\frac4{2n+1}.}
$$


Set


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),\qquad
T_n=\Lambda_k\tau_n.
$$


Both factorial terms remain in $T_n$.

Top-source rows are $0\le n<d$. Original return orders are exactly


$$
\boxed{0\le r<d.}
$$


Residual row $i$, $0\le i\le d+1$, is physical row $d+i$. Thus the terminal data remain


$$
\boxed{
2d+1=2k-1,\quad
3d+1=3k-2,\quad
(6k-4)!,\quad
6k-5.
}
$$



### 2.2 Actual contents, clearers, primitive denominator, and whole error

The original affine determinant is


$$
H_k(s)=
\det\left[
(c_{m+j})\
\middle|\
\bigl(\Lambda_k(r_{m+j}+s(-1)^{m+j})\bigr)
\right]
=H_{0,k}+H_{1,k}s,
$$


with $0\le m<2k$, $0\le j<k$.

The individual least right-column entry clearers are


$$
\Lambda_{k,j}
=\operatorname{lcm}(1,3,\ldots,4k+2j-3).
$$


Retain the actual all-prime quantities


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),\qquad
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


The least simultaneous coefficient clearer of $H_k/\Lambda_k^k$, and its content after that clearing, are


$$
\boxed{
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
\frac{G_k}{d_{H,k}}.
}
$$



For the original rectangles


$$
Z_k=
\left[
(c_{m+j})_{\substack{m<2k\\j<k}}
\ \middle|\
(T_{m+j})_{\substack{m<2k\\j<k-1}}
\right],
$$




$$
Y_k=
\left[
(\sigma_{m+j})_{\substack{m<2k-1\\j<k}}
\ \middle|\
(T_{m+j})_{\substack{m<2k-1\\j<k}}
\right],
$$


write


$$
\mathscr R_k=\delta_{2k-1}(Z_k),\qquad
\mathscr L_k=\delta_{2k-1}(Y_k).
$$


Their established relation is retained at its stated scope:


$$
\operatorname{lcm}(\mathscr L_k,\mathscr R_k)
\mid G_k\mid\Lambda_k\mathscr L_k\mathscr R_k.
$$



The actual primitive approximant and the whole evaluated error remain


$$
q_k=\frac{|H_{1,k}|}{G_k}>0,\qquad
p_k=-\frac{(-1)^kH_{0,k}}{G_k},
$$




$$
\boxed{
0<\ell_k=q_k(e+\pi)-p_k
=\frac{|H_k(e+\pi)|}{G_k}.
}
$$


No binary content or selected error summand replaces these quantities.

### 2.3 Complete forcing and corrected pencil

Put


$$
P_d(x)=\prod_{h=0}^{d-1}(2x+2h+1),\qquad
\mathcal A_dy=\Delta^d(P_dy),
$$




$$
\Omega_k=\prod_{n=0}^{d-1}P_d(n).
$$


The complete top forcing is


$$
F_k(n,j)=
-\Lambda_k\sum_{h=0}^d(-1)^h\binom dh
P_d(n+h)b(n+h+j)(2(n+h+j))!,
$$


where


$$
b(t)=4t^2+6t+3,\qquad
b(t)(2t)!=(2t+2)!+(2t)!.
$$


Write


$$
F_k=-\Lambda_kD_fK_dD_f,\qquad
D_f=\operatorname{diag}((2n)!)_{n<d},
\qquad \eta_d^F=\det K_d.
$$


The established oddness of the relevant leading principal $K_d$-determinants is reused.

Retain


$$
h_d=(2d-2)!,\quad
\beta=v_2(h_d),\quad
\alpha=v_2((2d)!)=2d-s_2(d)=\beta+5,
$$




$$
\widehat D_f=h_dD_f^{-1},\qquad
N_d=\widehat D_f\operatorname{adj}(K_d)\widehat D_f,
$$




$$
\delta_k=\Lambda_k\eta_d^Fh_d^2,\qquad
F_k^{-1}=-N_d/\delta_k,
$$




$$
f_k=(-\Lambda_k)^d\eta_d^F
\left(\prod_{n<d}(2n)!\right)^2.
$$



The bottom forcing is exactly


$$
R(i,j)=
\frac{\Lambda_k}{2(d+i+j)+1}
-\frac{\Lambda_k}{4}b(d+i+j)(2(d+i+j))!,
$$


for $0\le i\le d+1$, $0\le j<d$.

Every Newton divisor remains


$$
D_r=2^rr!,\qquad
\mathfrak D_d=\prod_{r<d}D_r.
$$


With


$$
\mathsf a_n=\frac{(\mathcal A_dc)_n}{2^d},\qquad
t_n^{(r)}
=\frac{(\mathcal A_d\Delta^r\sigma)_n}
{2^{\alpha+1}D_r},
$$


the complete columns are


$$
x=RN_d\mathsf a+\frac{\delta_k}{2^{d+2}}c_{\rm bot},
$$




$$
z^{(r)}
=RN_dt^{(r)}
+\frac{\delta_k}{2^{\alpha+3}D_r}(\Delta^r\sigma)_{\rm bot},
$$




$$
\mathfrak b_h
=RN_d\Lambda_k(\mathcal A_d\psi_h)_{\rm top}
+\frac{\delta_k\Lambda_k}{4}(\psi_h)_{\rm bot},
\quad \psi_0=r,\quad\psi_1=w.
$$


Thus


$$
\mathcal Q_k(s)
=[x,z^{(0)},\ldots,z^{(d-1)},\mathfrak b_0+s\mathfrak b_1].
$$



Its complete decomposition is


$$
\mathcal Q_k(s)=RN_d\mathcal A_k(s)
+2^{L_d}\gamma_k\mathcal W_k(s),
$$


where


$$
L_d=\alpha-12,\qquad M_d=\alpha-d+1,
$$




$$
\gamma_k=\Lambda_k\eta_d^F\operatorname{odd}(h_d)^2,
$$




$$
\mathcal W_k(s)=
\left[
2^{M_d}\frac{c_{\rm bot}}2,\
(\eta_r^{(d+i)})_{r<d},\
2^\alpha\Lambda_k(r+sw)_{\rm bot}
\right],
$$


and


$$
\eta_r^{(m)}=\frac{\Delta^r\sigma_m}{2^{r+1}r!}.
$$


Also,


$$
R=R^{\rm C}-2^{\alpha-2}V,
$$




$$
R^{\rm C}(i,j)=\frac{\Lambda_k}{2(d+i+j)+1},\qquad
V(i,j)=\frac{\Lambda_kb(d+i+j)(2(d+i+j))!}{2^\alpha}.
$$



No factorial correction is deleted in what follows.

### 2.4 The exact original scalar

Write


$$
\det\mathcal Q_k(s)=I_{0,k}+I_{1,k}s,\qquad
g_{\mathcal Q,k}=\gcd(|I_{0,k}|,|I_{1,k}|).
$$


The original forcing elimination gives, up to one common sign,


$$
\delta_k^{d+2}\Omega_k H_k(s)
=
f_k\,2^{\lambda_d^{\rm tr}}\mathfrak D_d
\det\mathcal Q_k(s),
\qquad
\lambda_d^{\rm tr}=d\alpha+4d+4.
\tag{2.1}
$$


Indeed, the residual Schur columns are $(4/\delta_k)\mathscr T(y)$, where


$$
\mathscr T(y)=RN_d(\mathcal A_dy)_{\rm top}
+\frac{\delta_k}{4}y_{\rm bot}.
$$


The $d+2$ residual columns contribute $4^{d+2}$; the atom and $d$ returns contribute


$$
2^d\prod_{r<d}(2^{\alpha+1}D_r).
$$


Their total binary exponent is precisely $d\alpha+4d+4$.

Consequently the all-prime identity is


$$
\boxed{
|\delta_k|^{d+2}\Omega_kG_k
=
|f_k|\,2^{\lambda_d^{\rm tr}}\mathfrak D_d\,g_{\mathcal Q,k}.
}
\tag{2.2}
$$



The already paid five-column normalization is not recomputed. Its payments $2^{13},2^{19},2^{32}$, its actual odd pivot quotients, and its resulting identity remain


$$
|\delta_k|^{d+2}\Omega_k|\mu_{5,k}|^{d-4}G_k
=
|f_k|\,2^{\lambda_d^{\rm tr}+d+69}
\mathfrak D_d\,g_k^{[5]}.
\tag{2.3}
$$


In particular,


$$
|\mu_{5,k}|^{d-4}g_{\mathcal Q,k}
=2^{d+69}g_k^{[5]}.
\tag{2.4}
$$


No odd quotient in these formulas is identified with the integer $1$.

---

## 3. Complete mixed kernel and actual source restrictions

Let


$$
\mathbb F_4=\mathbb F_2(\omega),\qquad
\omega^2+\omega+1=0,
$$


and let $\sigma$ denote coefficient conjugation. Set


$$
a=1+\omega Y,\qquad b=1+\omega^2Y.
$$



The retained contact parity is


$$
\eta_n=\operatorname{Tr}\bigl(\omega^{n+2}+(n+1)\omega^n\bigr).
$$


The normalized mixed rows are


$$
U_p(j,r)=
\sum_{t=0}^p\binom pt\binom{r+j+t}{r}\eta_{r+j+t}.
\tag{3.1}
$$



### 3.1 The odd derivative cannot be omitted

Put


$$
B_p(Y)=\omega^{2p}\frac{b^p}{a^p},\qquad S=X+Y,
\qquad \varepsilon=p\bmod2.
$$


The complete kernel is


$$
\sum_{j,r\ge0}U_p(j,r)X^jY^r
=
\operatorname{Tr}\left[
B_p(Y)\frac{\omega+S}{(1+\omega S)^2}
+
\varepsilon\frac{\omega B_{p-1}(Y)}
{a^2(1+\omega S)}
\right].
\tag{3.2}
$$


The second term comes from the filter-index derivative as well as the $Y$-derivative:


$$
YB_p'
=\varepsilon\frac{\omega^2YB_{p-1}}{a^2},
$$




$$
YB_p'+\varepsilon\frac{\omega B_{p-1}}a
=\varepsilon\frac{\omega B_{p-1}}{a^2}.
$$


Thus the odd term is not optional.

Coefficient extraction gives, for even $p$,


$$
U_p(2v,Y)
=\operatorname{Tr}\left(
\omega^{2p+2v+1}\frac{b^{p+1}}{a^{p+2v+2}}
\right),
$$




$$
U_p(2v+1,Y)
=\operatorname{Tr}\left(
\omega^{2p+2v}\frac{b^p}{a^{p+2v+2}}
\right),
\tag{3.3}
$$


and for odd $p$,


$$
U_p(2v,Y)
=\operatorname{Tr}\left(
\omega^{2p+2v}\frac{b^{p-1}}{a^{p+2v}}
\right),
$$




$$
U_p(2v+1,Y)
=\operatorname{Tr}\left(
\omega^{2p+2v}
\frac{b^{p-1}Y(1+Y)}{a^{p+2v+3}}
\right).
\tag{3.4}
$$



Pascal’s identity, applied directly to (3.1), gives


$$
\boxed{U_{p+1}(j)=U_p(j)+U_p(j+1).}
\tag{3.5}
$$



**Verdict: PASS**, including both parities and the odd derivative.

### 3.2 Actual atom-source row spaces

Write $U_j=U_d(j,\bullet)$. The paid source lists are


$$
R_q=
\begin{cases}
(U_0,\ldots,U_{q-2}),&q\ \text{odd},\\
(U_0,\ldots,U_{q-3},U_{q-2}+U_{q-1}),&q\ \text{even}.
\end{cases}
\tag{3.6}
$$


These are the actual lists produced by the normalized atom expansion.

After multiplication by $(ab)^d$, a source vector in $R_{p+1}$ has representative


$$
\operatorname{Tr}\left(\frac{b^{2\rho}Q}{a^p}\right),
\qquad \deg Q\le p-1.
\tag{3.7}
$$


Here $d=2L+\rho$, as below.

The binary restrictions on $Q$ can be checked explicitly.

For $p=2m$,


$$
Q=
\omega^{2d}\sum_{l=0}^{m-1}
\omega^{2l}
(c_{{\rm odd},l}+c_{{\rm even},l}\omega b)
a^{p-2l-2},
\quad c_{{\rm odd},l},c_{{\rm even},l}\in\mathbb F_2.
\tag{3.8}
$$



For $p=2m+1$,


$$
Q=aQ_{\rm old}+c_{\rm new}\omega^{2d+p+1},
\qquad c_{\rm new}\in\mathbb F_2,
\tag{3.9}
$$


where $Q_{\rm old}$ is the even-size expression of degree at most $p-2$.

A useful exact verification is obtained by setting


$$
z=Y+\omega^2.
$$


Then


$$
a=\omega z,\qquad b=\omega^2(z+1),\qquad \omega b=z+1.
$$


In (3.8), every summand has the common scalar


$$
\omega^{2d+2l+p-2l-2}=\omega^{2d+p-2}.
$$


Its remaining polynomial is


$$
\bigl(c_{{\rm odd},l}+c_{{\rm even},l}(z+1)\bigr)z^{p-2l-2}.
$$


The pairs cover all consecutive degrees $0,\ldots,p-1$, with an invertible binary coefficient change. Formula (3.9) supplies the same phase: multiplication of $Q_{\rm old}$ by $a=\omega z$ gives phase $\omega^{2d+p-2}$, and the new constant differs from it by $\omega^3=1$.

Therefore the **actual**, not enlarged, source space is


$$
\boxed{
Q=\omega^{2d+p-2}S(z),
\qquad S\in\mathbb F_2[z],\quad \deg S<p,
}
\tag{3.10}
$$


with a binary bijection between $S$ and the original source coefficients.

This identity does not free the tail $T$. It describes the source coefficients themselves.

---

## 4. Audit of the complete first-wrap and source-root interfaces

Assume


$$
d=2L+\rho,\qquad L\ \text{dyadic},\qquad \rho\ge4\ \text{even},
$$




$$
p\ge\rho+1,\qquad p+\rho\le L,
$$


and retain $p+\rho+1\le L$ when $p$ is odd.

Let


$$
V_j=U_p(j),\qquad 0\le j<h,\qquad q=p+h.
$$


All columns remain $0\le r<d$.

### 4.1 The common wrap is exactly $1+Y^{2L}$

Apply the same unit-triangular binary convolution


$$
C_d(Y)=(ab)^d
$$


modulo $Y^d$ to every row.

For the source rows, the full numerator contains $b^{2d}$. Since


$$
2d=4L+2\rho,\qquad 4L>d,
$$


Frobenius gives


$$
b^{2d}\equiv b^{2\rho}\pmod{Y^d}.
$$



For every mixed row, extracting its common $2L$-factor gives


$$
(ab)^{2L}=(1+Y+Y^2)^{2L}
=1+Y^{2L}+Y^{4L}.
$$


Hence on the original $d$ coordinates,


$$
\boxed{g(Y)=1+Y^{2L}.}
\tag{4.1}
$$


Conjugation fixes $g$, so this factor passes through the trace. It is present in every mixed row and absent from the simplified source representative.

Deleting it beyond the first $2L$ columns would change the matrix.

### 4.2 Exact pole orders and degree bounds

The reduced pole orders are


$$
\begin{array}{ll}
p\ \text{even}:&
n_{2v}=n_{2v+1}=p+2v+2-\rho,\\[2mm]
p\ \text{odd}:&
n_{2v}=p+2v-\rho,\quad
n_{2v+1}=p+2v+3-\rho.
\end{array}
$$


Let $M$ be the maximum of $p$ and the pole orders actually present. Then


$$
\boxed{
M+\rho=\max\bigl(p+\rho,\ q+(q\bmod2)\bigr).
}
\tag{4.2}
$$


This also accounts for a last unpaired row.

At denominator $a^M$,


$$
N_s=b^{2\rho}Q\,a^{M-p}.
$$


The complete mixed numerator $N_m$ is the actual binary combination of



$$
\begin{array}{ll}
p\ \text{even},\ j=2v:
&
\omega^{2p+2v+1}b^{\rho+p+1}
a^{M-p-2v-2+\rho},
\\
p\ \text{even},\ j=2v+1:
&
\omega^{2p+2v}b^{\rho+p}
a^{M-p-2v-2+\rho},
\\
p\ \text{odd},\ j=2v:
&
\omega^{2p+2v}b^{\rho+p-1}
a^{M-p-2v+\rho},
\\
p\ \text{odd},\ j=2v+1:
&
\omega^{2p+2v}b^{\rho+p-1}Y(1+Y)
a^{M-p-2v-3+\rho}.
\end{array}
\tag{4.3}
$$



All displayed $a$-exponents are nonnegative by the definition of $M$. The even-row degree is $M+2\rho-2v-1$; the odd-row degree is $M+2\rho-2v-2$. Thus


$$
\deg N_s,\deg N_m\le M+2\rho-1.
$$



Set


$$
P_s=b^MN_s+a^MN_s^\sigma,\qquad
P_m=b^MN_m+a^MN_m^\sigma,
$$




$$
E=P_s+P_m.
$$


If


$$
M+\rho\le d/2,
$$


then


$$
\deg P_s,\deg P_m,\deg E
\le2M+2\rho-1\le d-1.
\tag{4.4}
$$



### 4.3 The complete finite null criterion

Clearing both unit denominators, an actual row relation is equivalent to


$$
P_s+(1+Y^{2L})P_m\equiv0\pmod{Y^d}.
\tag{4.5}
$$


Its first $2L$ coefficients force $Y^{2L}\mid E$. Since $\deg E<d$,


$$
E=Y^{2L}T,\qquad \deg T<\rho.
$$


The remaining $\rho$ coefficients are exactly


$$
T=P_m\pmod{Y^\rho}.
$$


Thus


$$
\boxed{
E=Y^{2L}T,\qquad
T=P_m\pmod{Y^\rho},\qquad T\in\mathbb F_2[Y].
}
\tag{4.6}
$$



For $q>L$, put


$$
\delta=M+\rho-L=q+(q\bmod2)-L.
$$


Then


$$
M=L-\rho+\delta,
$$


and (4.4) sharpens the tail degree to


$$
\boxed{\deg T\le2\delta-1.}
\tag{4.7}
$$



The second equation of (4.6) remains an actual restriction:


$$
T=\operatorname{trunc}_{<2\delta}P_m,\qquad
[Y^j]P_m=0\quad(2\delta\le j<\rho).
$$


It has not been discarded.

### 4.4 Exact source-root representation

Write $N=N_s+N_m$. Frobenius gives


$$
a^{2L}+b^{2L}=Y^{2L}.
$$


Therefore $E=Y^{2L}T$ is equivalent to


$$
b^M\bigl(N-b^{2L-M}T\bigr)
+a^M\bigl(N-b^{2L-M}T\bigr)^\sigma=0.
$$


Since $a$ and $b$ are coprime,


$$
a^M\mid N-b^{2L-M}T.
$$


Writing the quotient as $H_0$, the trace identity forces
$H_0=H_0^\sigma$. Hence


$$
\boxed{
N_s+N_m=b^{2L-M}T+a^MH_0,
\quad
H_0\in\mathbb F_2[Y],\quad
\deg H_0\le2\rho-1.
}
\tag{4.8}
$$


The degree bound follows because


$$
\deg\bigl(b^{2L-M}T\bigr)
\le2L-M+2\delta-1=M+2\rho-1.
$$


The converse follows by taking the trace, so (4.8) is genuinely equivalent to the first equation of (4.6).

### 4.5 Frobenius at the actual source root

If $1\le\delta\le\rho/2$, then


$$
M=L-\rho+\delta<L.
$$


Since


$$
b=\omega^2+\omega a,
\qquad
b^L=\omega^{2L}+\omega^La^L,
$$


we obtain


$$
b^{2L-M}
=b^{L+\rho-\delta}
\equiv\omega^{2L}b^{\rho-\delta}\pmod{a^M}.
$$


Thus


$$
N_s+N_m
\equiv\omega^{2L}b^{\rho-\delta}T\pmod{a^M}.
\tag{4.9}
$$



Let


$$
K=M-p.
$$


Because $N_s$ contains $a^K$, every actual null relation necessarily satisfies


$$
\boxed{
N_m\equiv\omega^{2L}b^{\rho-\delta}T\pmod{a^K}.
}
\tag{4.10}
$$



**Verdict: PASS.** Both denominators, the actual root, the finite cutoff, and the entire original tail are retained.

---

## 5. Binary phase forces $T=0$, and the full stack is independent

### 5.1 Termwise mixed phase, including both parities

Again set


$$
z=Y+\omega^2.
$$


Then


$$
a=\omega z,\qquad b=\omega^2(z+1),\qquad
Y(1+Y)=z^2+z+1.
$$


Let $\varepsilon=0$ for even $p$, and $\varepsilon=1$ for odd $p$.

For an even-$p$ even row, writing its $a$-exponent as $e$, the scalar exponent after substitution is


$$
2p+2v+1+2(\rho+p+1)+e
=M+3p+3\rho+1\equiv M-2\pmod3.
$$


After extracting $(z+1)^{\rho+p}$, its remaining binary polynomial is
$(z+1)z^e$.

For an even-$p$ odd row, the scalar exponent is


$$
M+3p+3\rho-2,
$$


and the remaining polynomial is $z^e$.

For odd $p$, the even and odd scalar exponents are respectively


$$
M+3p+3\rho-2,\qquad M+3p+3\rho-5.
$$


Their remaining polynomials are $z^e$ and
$(z^2+z+1)z^e$.

Thus, term by term,


$$
\boxed{
N_m=\omega^{M-2}(z+1)^{\rho+p-\varepsilon}H(z),
\qquad H\in\mathbb F_2[z].
}
\tag{5.1}
$$


This statement retains the actual mixed bits. It applies to a last unpaired row as well.

### 5.2 The leading-coefficient obstruction

Substitute (5.1) into (4.10), and divide the unit
$(z+1)^{\rho-\delta}$. The result is


$$
(z+1)^{p+\delta-\varepsilon}H(z)
\equiv
\omega^{L+2}T(z+\omega^2)\pmod{z^K},
\tag{5.2}
$$


because the scalar exponent is


$$
2L+2\rho-2\delta-(M-2)
=L+3\rho-3\delta+2\equiv L+2\pmod3.
$$



Assume precisely


$$
\boxed{
L\equiv2\pmod3,\qquad
1\le\delta\le\rho/2,\qquad
\delta\le L-\rho-p.
}
\tag{5.3}
$$


Then


$$
K=L-\rho+\delta-p\ge2\delta,
$$


whereas $\deg T\le2\delta-1<K$. The left side of (5.2), reduced modulo $z^K$, is binary. The scalar on the right is $\omega$.

If $T\ne0$, its leading coefficient is $1$. Translation preserves that coefficient, and multiplication by $\omega$ changes it to the nonbinary coefficient $\omega$. Its degree is below $K$, so truncation cannot remove it. This contradicts (5.2).

Therefore


$$
\boxed{T=0.}
\tag{5.4}
$$



This excludes even the larger set of all binary $T$ of the allowed degree. In particular it excludes the actual $T$ fixed by $T=P_m\bmod Y^\rho$. No freedom has been granted to that low-trace constraint.

For $L\equiv1\pmod3$, the scalar in (5.2) is $1$, and this obstruction does not apply. No theorem for that phase is claimed.

### 5.3 Higher poles, including the unpaired cases

With $T=0$, the complete criterion gives the polynomial identity $E=0$. Consequently


$$
a^M\mid N_s+N_m.
$$


Since $a^K\mid N_s$,


$$
a^K\mid N_m.
\tag{5.5}
$$



For even $p$, each pair with pole order $n>p$ has two bits. Exactly one nonzero bit leaves its pole of order $n$. If both bits are nonzero, the identity


$$
\omega b+1=\omega^2a
$$


reduces the pole by exactly one. Because $n-p$ is a positive even number, $n-1>p$. All preceding pairs have order at most $n-2$. Descending from the largest pole therefore forces both bits of every such pair to vanish. A last unpaired even row has a nonzero root numerator and is eliminated in the same way.

For odd $p$, all pole orders above $p$ are distinct. Both $b$ and $Y(1+Y)$ are nonzero at the root of $a$, so descending pole order eliminates each corresponding bit. This includes the odd row $j=\rho-1$, whose pole order is $p+1$.

The remaining odd critical row $j=\rho$ has pole order $p$; it is not eliminated by a higher-pole argument and must be checked against the actual source phase.

### 5.4 Actual source phase closes the remaining relation

Because $p\ge\rho+1$,


$$
\rho+p-\varepsilon\ge2\rho.
$$


Thus $b^{2\rho}\mid N_m$. Together with (5.5),


$$
N_m=b^{2\rho}a^KQ_m
$$


for a polynomial $Q_m$ of degree at most $p-1$.

From (5.1), division gives


$$
Q_m=\omega^{p-4\rho-2}S_m(z),
\qquad S_m\in\mathbb F_2[z],\quad \deg S_m<p.
\tag{5.6}
$$


Here the divisibility by $z^K$ makes the quotient binary.

Now


$$
a^M\mid b^{2\rho}a^K(Q+Q_m)
$$


implies $a^p\mid Q+Q_m$. Since its degree is below $p$,


$$
Q+Q_m=0.
$$


Using the exact source description (3.10), the relative phase is


$$
\omega^{p-4\rho-2-(2d+p-2)}
=\omega^{-4\rho-2d}
=\omega^{-L}\notin\mathbb F_2.
\tag{5.7}
$$


Two binary polynomials with this nonbinary relative scalar can be equal only if both are zero. Hence


$$
Q=Q_m=0,\qquad N_m=0.
$$



For completeness, the odd critical row gives the same obstruction directly. Its candidate source numerator is


$$
\omega^{2p+\rho}b^{p-\rho-1}.
$$


At $a=0$, its ratio to the allowed source constant
$\omega^{2d+p+1}$ is $\omega^{-L}$. Thus its bit and the new source constant both vanish.

This also explicitly handles the even pair ending at $j=\rho-1$. That pair lies just beyond the literal $h\le\rho-1$ range displayed in the supplied turn-15 rank theorem. No extension of that old scope is silently assumed.

Finally, $N_m=0$ forces every mixed bit to vanish:

- for even $p$, successive pairs give disjoint adjacent lowest-degree slots after the binary change
  $(z+1)z^e,z^e\mapsto z^{e+1},z^e$;
- for odd $p$, every row has a distinct lowest degree, with coefficient $1$.

The source coefficient map (3.10) is also injective. Therefore the complete null relation is zero.

We have proved


$$
\boxed{
\operatorname{rank}_{\mathbb F_2}
[R_{p+1};V_0;\ldots;V_{h-1}]=p+h=q.
}
\tag{5.8}
$$



**Verdict: PASS, with the small-window endpoint explicitly repaired.**

The same argument also supplies the $q\le L$ case: there the cleared degree is below $2L$, so a relation already forces $T=0$, and Sections 5.3–5.4 apply. Thus this report does not need to cite a larger $q\le L$ theorem than is literally displayed in the supplied turn-15 text.

---

## 6. Complete cofactor transfer: strict crossing and equality tie

### 6.1 Exact payments and minimizing count

Retain


$$
\lambda_j=j+v_2(j!)=2j-s_2(j),\qquad
S_n=\sum_{j=0}^{n-1}\lambda_j,
$$




$$
e_n=v_2\!\left(\frac{h_d}{(2n)!}\right),\qquad
E_b=\sum_{n=d-b}^{d-1}e_n,
$$




$$
B_b=\binom b2+\sum_{j=0}^{b-2}v_2((d+1)_j),
\qquad
T_b=S_b+2E_b+B_b.
$$


The no-factorial, atom-in-product payment for a $q$-minor is


$$
\boxed{
F_q(b)=(q-b)L_d+S_b+S_q+2E_b+B_b.
}
\tag{6.1}
$$


Equivalently,


$$
F_q(b)=qL_d+S_q+T_b-bL_d.
$$



For $b\ge2$,


$$
D_b=T_b-T_{b-1}
=
8b-9+s_2(d)-2s_2(d-1)+2s_2(d-b)
-s_2(b-1)-s_2(d+b-2),
$$


and


$$
D_{b+1}-D_b
=
1+v_2(b)+2(1+v_2(d-b))+1+v_2(d+b-1)\ge4.
$$


Let


$$
s=\min\{r\ge2:D_r\ge L_d\},\qquad p=s-1.
$$


Then


$$
D_p<L_d\le D_{p+1}.
\tag{6.2}
$$


The minimum is at $p$, or at exactly $p,p+1$ when $D_{p+1}=L_d$.

### 6.2 Global exclusions remain valid

For a term with $v>0$ factorial-forcing columns, the established complete payment exceeds the corresponding $F_q(b)$ by at least


$$
v(\alpha-2-4q).
$$


For an atom-in-bottom term, the extra payment is at least


$$
d-2q+1-2m_d,
\qquad m_d=1+\lfloor\log_2d\rfloor.
$$


The all-bottom case is included; its formal cost exceeds $F_q(1)$ by $L_d$.

Thus the required exclusions are exactly


$$
\boxed{
\alpha-2>4q,\qquad d-2q+1-2m_d>0.
}
\tag{6.3}
$$



These bounds concern complete correction patterns. They do not delete $V$, the bottom atom, or either factorial term entrywise.

### 6.3 Every leading-sector odd factor

Let


$$
\mathcal T_b=\{d-b,\ldots,d-1\},\qquad
Q_{\mathcal T_b}(i)
=\prod_{j\in\mathcal T_b}(2(d+i+j)+1),
$$


and


$$
\Phi_b=\prod_{j=0}^{b-1}j!,\qquad
\mathcal B_b(d)=2^{\binom b2}\prod_{j=0}^{b-2}(d+1)_j.
$$


For the first $q$ residual rows, the complete minimal-pair scalar is


$$
2^{F_q(b)}\Xi_{q,b},
$$


where


$$
\boxed{
\begin{aligned}
\Xi_{q,b}={}&
\gamma_k^{q-b}
\frac{\Lambda_k^b\operatorname{odd}(\Phi_b)^2}
{\prod_{i=0}^{q-1}Q_{\mathcal T_b}(i)}
\frac{\det N_d[\mathcal T_b,\mathcal T_b]}{2^{2E_b}}
\\
&\times
\frac{\mathcal B_b(d)}{2^{B_b}}
\prod_{j=b}^{q-1}\operatorname{odd}(j!).
\end{aligned}}
\tag{6.4}
$$


The source atom coefficients inside the normalized stack remain


$$
\frac{(d+1)_{b-1}}{(d+1)_j}
\frac{\Delta^j\mathsf a_{d-b}}{2^j}.
\tag{6.5}
$$



The actual adjugate minor is


$$
\det N_d[\mathcal T_b,\mathcal T_b]
=
\left(\prod_{j\in\mathcal T_b}\frac{h_d}{(2j)!}\right)^2
(\eta_d^F)^{b-1}
\det K_d[0{:}d-b-1,0{:}d-b-1].
\tag{6.6}
$$


The last two factors are odd. The minimizing pair is unique because


$$
e_n-e_{n+1}=1+v_2(n+1)>0.
$$



Thus every factor in (6.4) is an actual retained odd unit in
$\mathbb Z_{(2)}$, and only after retaining it may one use


$$
\Xi_{q,b}\equiv1\pmod2.
$$


This is enough for the relative binary normalization of tied sectors; it is not an integer identity $\Xi_{q,b}=1$.

### 6.4 Strict crossing

Put $q=p+h$. If $D_{p+1}>L_d$, the complete leading stack is


$$
[R_p;V_0;\ldots;V_{h-1}].
$$


It has $q-1$ independent rows by (5.8). Therefore some $q-1$ original return columns, together with the atom, give a complete $q$-minor of exact valuation


$$
\boxed{F_q(p).}
\tag{6.7}
$$



### 6.5 Equality tie

If $D_{p+1}=L_d$, define


$$
v_{\rm new}=
\begin{cases}
U_d(p-1)+U_d(p),&p\text{ odd},\\
U_d(p-1),&p\text{ even}.
\end{cases}
$$


Then $R_{p+1}$ is obtained from $[R_p;v_{\rm new}]$ by a binary determinant-one basis change.

The $p+1$-sector mixed rows are, by (3.5),


$$
V_j+V_{j+1}.
$$


After the determinant-one change of mixed rows, the **sum of both complete minimum sectors** is


$$
\boxed{
\det[
R_p;\
v_{\rm new}+V_{h-1};\
V_0+V_1;\
\ldots;\
V_{h-2}+V_{h-1}
].
}
\tag{6.8}
$$


The relative units in (6.4) are what justify this sum.

Equation (5.8) places $v_{\rm new}$ outside
$\operatorname{span}(R_p,V_0,\ldots,V_{h-1})$. Hence the rows in (6.8) are independent, and an original-column minor attains


$$
\boxed{F_q(p)=F_q(p+1).}
\tag{6.9}
$$



**Verdict: PASS.** No isolated tied summand is substituted for the aggregate.

---

## 7. Original rotation intervals, minimizing $p$, and all physical bounds

### 7.1 A quantitative bound for the actual minimizer

Since $v_2(d)=4$,


$$
s_2(d-1)=s_2(d)+3.
$$


Subtracting $L_d=2d-s_2(d)-12$ from the exact marginal formula gives


$$
D_b-L_d
=
8b-2d-3
+2s_2(d-b)-s_2(b-1)-s_2(d+b-2).
\tag{7.1}
$$


For $2\le b\le d$, the digit correction has absolute value at most
$2m_d+1$. Applying (7.1) to (6.2) gives, in particular, the convenient bound


$$
\boxed{\left|p-\frac d4\right|\le m_d+3.}
\tag{7.2}
$$


This is a bound for the actual minimizing count, not a replacement count.

Write


$$
C=m_d+3,\qquad p=L/2+\rho/4+\epsilon_p,\qquad |\epsilon_p|\le C.
$$



### 7.2 The wider window and its exact rounded bound

Let


$$
a_k=\lfloor\log_2k\rfloor,\qquad L=2^{a_k-1},
$$


and retain


$$
\frac98\,2^{a_k}<k<\frac76\,2^{a_k},
\qquad a_k\ \text{even}.
$$


Then


$$
L/4-1<\rho<L/3-1,\qquad L\equiv2\pmod3.
$$



The exact bound remains


$$
\boxed{
B=\min\bigl(\lfloor\rho/4\rfloor,\ L-\rho-p\bigr),
\qquad
q_{\max}=L+2\lfloor B/2\rfloor.
}
\tag{7.3}
$$


It is not replaced by $\rho/4$.

Since $q_{\max}$ is even, every $q\le q_{\max}$ satisfies


$$
q+(q\bmod2)\le q_{\max}.
$$


Thus, for $q>L$,


$$
\delta\le B\le\rho/4,\qquad \delta\le L-\rho-p.
$$


The actual odd-$q$ extra $1$ has been paid.

The valuation exclusions are


$$
\alpha-2-4q\ge\rho-s_2(d)-2>0,
$$




$$
d-2q+1-2m_d\ge\rho/2+1-2m_d>0
$$


for sufficiently large original tuples. Also


$$
B=\rho/4+O(m_d),
$$


so


$$
q_{\max}=L+\rho/4+O(m_d),
$$


with the quoted asymptotic ratio between $13/28$ and $17/36$.

The cofactor range here is understood to retain $q\ge p+1$.

### 7.3 The narrower interval really reaches $q_{\rm half}$

Now restrict to


$$
\boxed{
\frac98\,2^{a_k}<k<\frac{17}{15}\,2^{a_k},
\qquad a_k\ \text{even}.
}
\tag{7.4}
$$


This gives exactly


$$
L/4-1<\rho<4L/15-1.
\tag{7.5}
$$



The critical slack is


$$
\begin{aligned}
L-\rho-p-\rho/2
&=L/2-7\rho/4-\epsilon_p\\
&>L/30+7/4-C.
\end{aligned}
\tag{7.6}
$$


It is positive with linear slack for sufficiently large original tuples. Thus


$$
\delta\le\rho/2
\quad\Longrightarrow\quad
\delta\le L-\rho-p
$$


on this narrower subfamily.

The other source hypotheses are also validated, not presumed:


$$
p-\rho
=L/2-3\rho/4+\epsilon_p
>3L/10+3/4-C,
$$


and


$$
p+\rho+1
<L-\bigl(L/6-C+1/4\bigr).
$$


Hence $p\ge\rho+1$, $p+\rho\le L$, and the odd-$p$ extra condition all hold. For example, the explicit sufficient condition


$$
L>128(m_d+4)
$$


has more than enough slack and excludes at most finitely many original indices.

Define


$$
\boxed{q_{\rm half}=d/2-m_d-1.}
\tag{7.7}
$$


For every


$$
p+1\le q\le q_{\rm half},
$$




$$
q+(q\bmod2)\le d/2-m_d.
$$


Thus, when $q>L$,


$$
\delta\le\rho/2-m_d<\rho/2,
$$


and the first-wrap rank hypotheses hold.

Using the exact original
$\alpha=2d-s_2(d)$,


$$
\boxed{
\alpha-2-4q\ge4m_d+2-s_2(d)>0,
}
\tag{7.8}
$$




$$
\boxed{
d-2q+1-2m_d\ge3.
}
\tag{7.9}
$$


These pay every factorial and atom-in-bottom competitor.

Therefore the complete strict/equality argument attains $F_q(p)$ at every


$$
\boxed{p+1\le q\le q_{\rm half}}
$$


on the stated infinite original subfamily.

The wider bound $B$ in (7.3) has not been altered. The narrower application uses the larger $\delta\le\rho/2$ range already present in the rank theorem.

### 7.4 Infinitely many of the same original indices

Let


$$
x_u=(18+32u)\log_2 9=\log_2 k.
$$


Unique factorization proves $\log_2 9\notin\mathbb Q$. Hence the rotation


$$
x_u\pmod2
$$


has irrational step and every tail is dense modulo $2$.

The interval


$$
\left(\log_2(9/8),\ \log_2(17/15)\right)\subset(0,1)
$$


is nonempty. Membership of $x_u\bmod2$ in this interval is exactly the condition that $a_k$ is even and (7.4) holds. Thus infinitely many original $u$ satisfy all the conditions, including any fixed sufficiently-large threshold.

No independently chosen $d$, auxiliary dyadic sequence, or distribution assumption for ties is used.

### 7.5 Physical row and moment bounds

All selected return columns satisfy $r<d$. The largest bottom Newton order in a $q$-minor is $q-1$, including the tied sector. It lies within $0,\ldots,d+1$.

The top source transformations use rows ending at $d-1$. In an equality sector, the extra source jet is at most $p$, which is already inside the retained top normalization.

A normalized bottom expression may contain notation such as $\eta_{r+j}^{(d)}$, but this is a re-expression of a finite difference, not installation of a new return column. Its largest physical moment is bounded by


$$
d+i+j+r+1\le3d+1
$$


whenever $i+j\le d+1$ and $r\le d-1$.

Thus the original physical terminal, factorial terminal, and odd-denominator terminal remain unchanged.

---

## 8. New paid lemma: near-half-size Cramer control in the actual pencil

This section advances the cofactor result quantitatively. It uses the actual common columns


$$
\mathcal C=[x,z^{(0)},\ldots,z^{(d-1)}]
\in\mathbb Z^{(d+2)\times(d+1)}.
$$


It does not use integral $W$-descent.

### 8.1 Uniform minor lower bounds, including minors without the atom

Cofactor attainment alone gives an upper bound for a determinantal divisor. To obtain the following Cramer result, the matching **uniform lower bound** must also be checked.

For a minor containing the atom, the complete lower payment is the one audited in Section 6.

For a minor containing only return columns, a $b$-column top source determinant has payment at least


$$
\binom b2+\sum_{j=0}^{b-1}v_2((d+1)_j)
=
B_b+v_2((d+1)_{b-1})\ge B_b.
\tag{8.1}
$$


This follows from the same full rising-factor Newton normalization, now with no atom position omitted. All bottom columns are weighted returns, so there is no missing atom jet to pay.

For nonconsecutive physical rows, finite Newton expansion introduces determinants of integer binomial collocation matrices. It cannot reduce the valuation. The Cauchy-polynomial orders force $0,\ldots,b-1$; the remaining minimal orders are $b,\ldots,q-1$. Thus the same $S_b+S_q$ lower payment applies. Factorial patterns retain the complete bounds of Section 6.

Consequently, under (6.3), **every** $j$-minor of $\mathcal C$ has depth at least


$$
f_j:=F_j(p)
$$


whenever the minimizing count $p$ is in range. Together with attainment,


$$
\boxed{
v_2\bigl(\delta_j(\mathcal C)\bigr)=f_j,
\qquad p+1\le j\le q_{\rm half}.
}
\tag{8.2}
$$


Here $\delta_j(\mathcal C)$ is the actual all-prime determinantal content; only its $2$-valuation has been evaluated.

In particular, for $p+2\le j\le q_{\rm half}$, the corresponding $2$-primary invariant-factor exponent is


$$
\boxed{
f_j-f_{j-1}=L_d+\lambda_{j-1}.
}
\tag{8.3}
$$


This is an invariant-factor statement. It is not a claim that the separately attaining original minors form a nested physical elimination flag.

### 8.2 One lower-only step beyond $q_{\rm half}$

Put


$$
q=q_{\rm half}.
$$


The uniform lower-bound argument also applies to $q+1=d/2-m_d$, because


$$
\alpha-2-4(q+1)\ge4m_d-2-s_2(d)>0,
$$




$$
d-2(q+1)+1-2m_d=1>0.
\tag{8.4}
$$


No attainment at $q+1$ is needed here.

Define


$$
c_q=f_q-f_{q-1}=L_d+\lambda_{q-1},
$$




$$
c_{q+1}=f_{q+1}-f_q=L_d+\lambda_q.
\tag{8.5}
$$


Then


$$
c_{q+1}-c_q=1+v_2(q)>0.
$$



### 8.3 An attaining block and its exact Cramer cost

Choose any attaining $q$-minor $A$ on the first $q$ residual rows, using the atom and $q-1$ original returns. Write


$$
D_A=\det A=2^{f_q}\mu_A,\qquad \mu_A\ \text{odd}.
\tag{8.6}
$$


The integer $\mu_A$ is retained in full.

Every entry of $\operatorname{adj}A$ is a $(q-1)$-minor of $\mathcal C$, so


$$
2^{f_{q-1}}\mid\operatorname{adj}A.
$$


Therefore


$$
\boxed{2^{c_q}A^{-1}\in M_q(\mathbb Z_{(2)}).}
\tag{8.7}
$$



This upper bound is in fact exact for the least simultaneous $2$-primary clearer of $A^{-1}$. Here is the additional verification.

After row and column permutations, write


$$
\mathcal C=
\begin{pmatrix}
A&B\\
C_0&D_0
\end{pmatrix}.
$$


Every entry of $A^{-1}B$ is a ratio of a common $q$-minor to $D_A$, and every entry of $C_0A^{-1}$ is such a row-replacement ratio. The uniform $q$-minor lower bound makes both matrices integral over $\mathbb Z_{(2)}$.

Thus $\mathcal C$ is equivalent over $\mathbb Z_{(2)}$ to


$$
\operatorname{diag}(A,S),\qquad
S=D_0-C_0A^{-1}B.
$$


Every entry of $S$, multiplied by $D_A$, is a common $(q+1)$-minor. By (8.4),


$$
v_2(S_{ij})\ge c_{q+1}>c_q.
$$


All invariant-factor exponents of $A$ are at most $c_q$, by (8.7), whereas all those of $S$ are at least $c_{q+1}$. Hence the first $q$ invariant factors of $\mathcal C$ are precisely those of $A$. In particular,


$$
v_2\bigl(\delta_{q-1}(A)\bigr)=f_{q-1}.
$$



The actual least simultaneous integer clearer of $A^{-1}$ is


$$
\boxed{
\mathcal C_A=\frac{|D_A|}{\delta_{q-1}(A)},
\qquad
v_2(\mathcal C_A)=c_q.
}
\tag{8.8}
$$


Its odd part has not been evaluated or discarded.

At $q=q_{\rm half}$,


$$
\boxed{
c_q
=3d-2m_d-s_2(d)-s_2(q-1)-16.
}
\tag{8.9}
$$


Thus the Cramer payment is linear in $d$, not the quadratic $f_q$.

### 8.4 Both complete borders pay their actual factors

The supplied complete source normalization gives


$$
2^d\mid N_d\Lambda_k(\mathcal A_dw)_{\rm top},
$$




$$
2^{d+1}\mid N_d\Lambda_k(\mathcal A_dr)_{\rm top}.
$$


The second assertion includes both parts of $r=-f+4\rho$:

- the factorial part pays $2^\beta$;
- the recurrence $(\Delta+2)\rho=(2n+1)^{-1}$ gives
  $v_2(\Delta^t\rho_n)\ge t-1$, so the $4\rho$ part pays $2^{d+1}$.

Integrality of reciprocal differences follows from the finite sum of original reciprocals, not from asserting that their displayed product denominator divides $\Lambda_k$.

The bottom terms have still larger depth:


$$
v_2(\delta_k/4)=2\alpha-12,
$$


and $\Lambda_kr_m$ is divisible by $4$ on the retained bottom rows. Therefore


$$
\boxed{
2^{d+1}\mid\mathfrak b_0,\qquad
2^d\mid\mathfrak b_1.
}
\tag{8.10}
$$



Let $u_h$ be the restriction of $\mathfrak b_h$ to the pivot rows, and put


$$
d_0=d+1,\qquad d_1=d.
$$


Then


$$
v_2(A^{-1}u_h)\ge d_h-c_q.
$$


The actual least simultaneous clearer of that Cramer vector is


$$
\mathcal C_{A,h}
=
\frac{|D_A|}
{\gcd\bigl(|D_A|,\text{all entries of }\operatorname{adj}A\,u_h\bigr)},
$$


and hence


$$
\boxed{
v_2(\mathcal C_{A,h})\le\max(0,c_q-d_h).
}
\tag{8.11}
$$


This is a paid quantitative bound for both literal borders.

### 8.5 A one-shot odd-localized descent with all divisions paid

Let


$$
n=d+2,\qquad
t=d+1-q,\qquad s=t+1=n-q.
$$


In the same row and common-column order, write


$$
\mathcal Q_h=
\begin{pmatrix}
A&B&u_h\\
C_0&D_0&v_h
\end{pmatrix},
\qquad h=0,1.
$$


Define the integer matrix


$$
K_A=\frac{C_0\operatorname{adj}A}{2^{f_q}}.
\tag{8.12}
$$


This division is paid by the uniform $q$-minor lower bound.

Set


$$
E_A=\mu_AD_0-K_AB,
\qquad
e_h=\mu_Av_h-K_Au_h.
\tag{8.13}
$$


Every entry of $2^{f_q}E_A$ is an actual bordered $(q+1)$-minor. Thus


$$
2^{c_{q+1}}\mid E_A.
$$


Also (8.10) gives $2^{d_h}\mid e_h$. Therefore the matrices


$$
\widehat E_A=\frac{E_A}{2^{c_{q+1}}},
\qquad
\widehat e_h=\frac{e_h}{2^{d_h}}
\tag{8.14}
$$


are integral.

All divisions in (8.12)–(8.14) have now been proved. They are performed on actual corrected columns, not on an assumed integral $W$-descent.

Put


$$
J_h=\det[\widehat E_A,\widehat e_h].
$$


A block determinant calculation gives, with the same sign $\epsilon$ for both coefficients,


$$
\mu_A^t I_{0,k}
=
\epsilon\,2^{f_q+t c_{q+1}+d+1}J_0,
$$




$$
\mu_A^t I_{1,k}
=
\epsilon\,2^{f_q+t c_{q+1}+d}J_1.
\tag{8.15}
$$


Consequently


$$
\boxed{
|\mu_A|^t g_{\mathcal Q,k}
=
2^{\mathcal E_q}\gcd(2|J_0|,|J_1|),
\qquad
\mathcal E_q=f_q+t c_{q+1}+d.
}
\tag{8.16}
$$


This is an exact all-prime identity, including the actual odd pivot quotient.

Combining it with the original scalar (2.2),


$$
\boxed{
|\mu_A|^t|\delta_k|^{d+2}\Omega_kG_k
=
|f_k|\,2^{\lambda_d^{\rm tr}+\mathcal E_q}
\mathfrak D_d\,
\gcd(2|J_0|,|J_1|).
}
\tag{8.17}
$$



The new evaluated payments are


$$
f_q=d^2+O(dm_d),\qquad
c_{q+1}=3d+O(m_d),\qquad
t=d/2+O(m_d),
$$


so


$$
\boxed{\mathcal E_q=\frac52d^2+O(dm_d).}
\tag{8.18}
$$



For the full maximal-minor content of the common rectangle, the same local block argument gives


$$
\boxed{
v_2\delta_{d+1}(\mathcal C)
=
f_q+t c_{q+1}
+v_2\delta_t(\widehat E_A).
}
\tag{8.19}
$$


Thus the window supplies a substantial **paid lower extraction** and exact Cramer control, but no upper bound for the remaining maximal content.

This is the new paid lemma. It is more than a renamed terminal determinant: the inverse clearer, both border Cramer bounds, the one-step common-column divisor, and the exact odd-factor transfer have all been evaluated.

---

## 9. The literal paired coefficient system remains intact

The preceding descent applies to the original coefficient pair $I_{0,k},I_{1,k}$. It does not replace either border by a simpler one.

For clarity, retain the exact paired identities. Define


$$
\theta_r^{(m)}=\frac{\Delta^ru_m}{2^rr!},
\qquad
v^{(r)}=\frac{\mathscr T(\Delta^ru)}{2^\alpha D_r},
\quad 0\le r\le d,
$$




$$
w_*=\frac{\mathscr T(w)}{2^d},
\qquad
\varkappa_d=2^{\alpha-d}d!,
\qquad
\mathfrak c_k=\Lambda_k2^\alpha d!.
$$


The full divisor $D_d=2^dd!$ remains paid. The order-$d$ column is a re-expression of the original terminal border, not a new original return.

Exactly,


$$
\boxed{
I_{1,k}
=-\mathfrak c_k
\det[w_*,v^{(0)},\ldots,v^{(d)}],
}
\tag{9.1}
$$


and


$$
\boxed{
\begin{aligned}
I_{0,k}={}&
\varkappa_d\det[v^{(0)},\ldots,v^{(d)},\mathfrak b_0]\\
&-\sum_{r=0}^d\frac{d!}{r!}
\det[w_*,v^{(0)},\ldots,\widehat{v^{(r)}},
\ldots,v^{(d)},\mathfrak b_0].
\end{aligned}}
\tag{9.2}
$$


Moreover,


$$
\mathfrak b_0=\Lambda_k2^{-d}\mathscr T(\Delta^dr)
$$


still contains both $-\Delta^df$ and $4\Delta^d\rho$.

The full-$\theta$ rank/corank and higher effective-block assertions mentioned in the assignment are separate pending work. They are not used as evidence either for or against the mixed-$\eta$ theorem proved here.

---

## 10. Exact remaining bottleneck

The new result does **not** give a terminal upper bound.

From (8.16),


$$
v_2(g_{\mathcal Q,k})
=
\mathcal E_q+
v_2\gcd(2J_0,J_1).
\tag{10.1}
$$


The extracted block and the actual odd quotient $\mu_A$ are controlled, but the remaining pair has size


$$
s=d/2+m_d+3.
$$


Its maximal content and its two-border cancellation are not bounded above by the near-half-size cofactor theorem.

For the stated binary terminal target,


$$
v_2(g_{\mathcal Q,k})
\le
\frac{15}{4}k^2+d+5+O(k\log k),
$$


the exact remaining requirement in this descent is


$$
\boxed{
v_2\gcd(2J_0,J_1)
\le
\frac{15}{4}k^2+d+5-\mathcal E_q+O(k\log k).
}
\tag{10.2}
$$


Its leading required allowance is


$$
\frac54d^2+O(d\log d).
$$


No such upper bound has been proved here.

There are two distinct obstructions:

1. **Remaining common maximal content.**  
   Equation (8.19) leaves $v_2\delta_t(\widehat E_A)$ uncontrolled above.

2. **Primitive two-border alignment.**  
   Even an upper bound for that common content would not by itself bound the gcd of the two complete bordered determinants. The actual constant border and linear border must be treated together.

The partial invariant factors cannot control either obstruction merely by monotonicity. Individual attaining minors also do not provide a prescribed nested corrected elimination flag.

Finally, a binary upper alone would still not determine the all-prime $G_k$, the actual primitive denominator, or the same-index whole error. Those independent arithmetic and analytic obligations remain.

---

## 11. Proof-status ledger and computation scope

| Statement | Status |
|---|---|
| Common mixed wrap $1+Y^{2L}$ on all $r<d$ | **PASS** |
| Complete finite criterion $E=Y^{2L}T,\ T=P_m\bmod Y^\rho$ | **PASS** |
| Exact source-root representation and degree bounds | **PASS** |
| Frobenius reduction at the actual $a$-root | **PASS** |
| Termwise mixed phase, both parities and unpaired rows | **PASS** |
| Phase $\omega^{L+2}$ and $T=0$ under $L\equiv2\pmod3$ | **PASS** |
| Higher-pole elimination and odd critical row | **PASS** |
| Even last small-pole pair | **Explicitly repaired and proved** |
| Full $q$-row coupled independence | **PASS under (5.3)** |
| Complete strict/equality cofactor transfer and odd factors | **PASS** |
| Exact wider bound $B$ and odd-$q$ rounding | **PASS** |
| Narrower original interval and all $q\le q_{\rm half}$ | **PASS** |
| Exact Cramer exponent and one-shot odd-localized descent | **New proved result** |
| Remaining maximal-content and two-border upper bounds | **OPEN** |
| Integral $W$-descent | **Not used; its disproof is respected** |
| Separate full-$\theta$ higher-block audit | **Not undertaken here** |
| All-prime terminal control and an $e+\pi$ decision | **OPEN** |

No original-sized solve, old scan, closed auxiliary receipt, or optional constant calculation has been repeated.

**No bounded exact arithmetic calculation is needed for the proofs in this report, and none is requested.** The outstanding requirement is a uniform theorem about the complete residual maximal content and the complete two-border pair in (10.2). A finite calculation, if later proposed, would establish only its specified finite instances; it would not prove this infinite-family upper bound.

---

## Final conclusion

The first-wrap binary-phase proof survives a complete audit on its stated dyadic phase. It retains all original columns, the full odd derivative, the common wrap, both trace denominators, and the actual low-trace tail. Its full-rank conclusion yields complete cofactor attainment, including equality ties, through


$$
\boxed{q_{\rm half}=d/2-m_d-1}
$$


on infinitely many of the original indices in the narrower interval


$$
\boxed{
(9/8)2^{a_k}<k<(17/15)2^{a_k},\qquad a_k\ \text{even}.
}
$$



The new quantitative advance is a paid near-half-size Cramer and content theorem: an attaining block has exact $2$-primary inverse-clearer exponent $L_d+\lambda_{q-1}$, both literal borders satisfy explicit Cramer bounds, and the one-shot descent gives the exact all-prime transfer (8.17).

What remains is not another phase-rank assertion. It is a full-terminal **upper bound** for the remaining common content and the two complete bordered determinants, followed by the other-prime and whole-error controls. The actual least clearers, all-prime $G_k$, primitive denominator $q_k$, and positive whole error $\ell_k$ remain unchanged.

No unconditional rationality or irrationality conclusion for $e+\pi$ follows.
